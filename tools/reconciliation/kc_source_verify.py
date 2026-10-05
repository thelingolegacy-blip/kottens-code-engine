#!/usr/bin/env python3
import hashlib
from pathlib import Path

EXPECTED_SIZE = 37214
EXPECTED_SHA256 = "47187900d5ae2f4e03f34b258318e259141d4b1bda61db26da8e052bb0f11758"
SOURCE = Path("source/KottonsCode_DraftOne.docx")

if not SOURCE.is_file():
    raise SystemExit("FAIL: source/KottonsCode_DraftOne.docx is absent")

data = SOURCE.read_bytes()
actual_size = len(data)
actual_sha = hashlib.sha256(data).hexdigest()

print(f"SIZE={actual_size}")
print(f"SHA256={actual_sha}")
print(f"EXPECTED_SIZE={EXPECTED_SIZE}")
print(f"EXPECTED_SHA256={EXPECTED_SHA256}")

if actual_size != EXPECTED_SIZE:
    raise SystemExit("FAIL: byte-size mismatch")
if actual_sha != EXPECTED_SHA256:
    raise SystemExit("FAIL: SHA-256 mismatch")

print("KC_SOURCE_VERIFY=PASS")
