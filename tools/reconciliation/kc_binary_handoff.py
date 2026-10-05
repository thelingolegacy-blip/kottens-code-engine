#!/usr/bin/env python3
"""
Kotton's Code — private binary handoff bridge.

Reads the exact local DOCX, verifies its SHA-256, creates a native Git blob,
creates a tree/commit on the reconciliation branch, and updates the branch ref.

Requirements:
  Python 3.9+
  GITHUB_TOKEN environment variable with write access to the repository.

This script never prints source bytes or Base64 payloads.
"""

import argparse
import base64
import hashlib
import json
import os
import sys
import urllib.request
import urllib.error

EXPECTED_SHA256 = "47187900d5ae2f4e03f34b258318e259141d4b1bda61db26da8e052bb0f11758"
EXPECTED_SIZE = 37214
DEFAULT_REPO = "thelingolegacy-blip/kottens-code-engine"
DEFAULT_BRANCH = "governance/kc-sc0-sc1-reconciliation-v0.1"
DEFAULT_PATH = "source/KottonsCode_DraftOne.docx"
API = "https://api.github.com"

def request(method, path, token, body=None):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        API + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "LINGO-Kottons-Code-Source-Reconciliation",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        raise RuntimeError(f"GitHub API {e.code} on {method} {path}: {detail[:1000]}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="exact local KottonsCode_DraftOne.docx")
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--branch", default=DEFAULT_BRANCH)
    ap.add_argument("--path", default=DEFAULT_PATH)
    ap.add_argument("--expected-sha256", default=EXPECTED_SHA256)
    ap.add_argument("--expected-size", type=int, default=EXPECTED_SIZE)
    ap.add_argument("--message", default="reconcile: bind exact Kotton's Code Book 1 source bytes")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with open(args.source, "rb") as f:
        raw = f.read()

    digest = hashlib.sha256(raw).hexdigest()
    size = len(raw)

    print(f"LOCAL_SIZE={size}")
    print(f"LOCAL_SHA256={digest}")

    if size != args.expected_size:
        raise SystemExit(f"FAIL: size mismatch; expected {args.expected_size}, got {size}")
    if digest != args.expected_sha256:
        raise SystemExit("FAIL: SHA-256 mismatch; refusing repository mutation")

    if args.dry_run:
        print("DRY_RUN=PASS")
        return

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("FAIL: GITHUB_TOKEN is required; no repository mutation attempted")

    owner, repo = args.repo.split("/", 1)
    ref = request("GET", f"/repos/{owner}/{repo}/git/ref/heads/{args.branch}", token)
    base_sha = ref["object"]["sha"]

    # Native Git object: exact source bytes, base64 encoded only for API transport.
    blob = request(
        "POST",
        f"/repos/{owner}/{repo}/git/blobs",
        token,
        {"encoding": "base64", "content": base64.b64encode(raw).decode("ascii")},
    )
    blob_sha = blob["sha"]

    tree = request(
        "POST",
        f"/repos/{owner}/{repo}/git/trees",
        token,
        {
            "base_tree": base_sha,
            "tree": [
                {
                    "path": args.path,
                    "mode": "100644",
                    "type": "blob",
                    "sha": blob_sha,
                }
            ],
        },
    )

    commit = request(
        "POST",
        f"/repos/{owner}/{repo}/git/commits",
        token,
        {
            "message": args.message,
            "tree": tree["sha"],
            "parents": [base_sha],
        },
    )

    updated = request(
        "PATCH",
        f"/repos/{owner}/{repo}/git/refs/heads/{args.branch}",
        token,
        {"sha": commit["sha"], "force": False},
    )

    print(f"BASE_COMMIT={base_sha}")
    print(f"GIT_BLOB_SHA={blob_sha}")
    print(f"TREE_SHA={tree['sha']}")
    print(f"COMMIT_SHA={commit['sha']}")
    print(f"BRANCH={args.branch}")
    print(f"BRANCH_HEAD={updated['object']['sha']}")
    print(f"REPOSITORY_PATH={args.path}")
    print("HANDOFF=COMMITTED")

if __name__ == "__main__":
    main()
