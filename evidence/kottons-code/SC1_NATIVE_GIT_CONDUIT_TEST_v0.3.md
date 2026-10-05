# SC1 Native Git Object Conduit Test — v0.3

Date: 2026-10-04
Asset: KottonsCode_DraftOne.docx
Expected bytes: 37214
Expected SHA-256: 47187900d5ae2f4e03f34b258318e259141d4b1bda61db26da8e052bb0f11758
Repository: thelingolegacy-blip/kottens-code-engine
Branch: governance/kc-sc0-sc1-reconciliation-v0.1

## Observed
- GitHub native create_blob operation is available and explicitly supports encoding=base64.
- Exact source artifact was materialized and independently re-hashed locally at 37,214 bytes with the expected SHA-256.
- A local base64 representation was generated at 49,620 characters.
- The current execution bridge does not provide a safe binary/file-reference handoff from the materialized local artifact into the create_blob content parameter.
- Attempts to relay the base64 through intermediate text retrieval were truncated and therefore were not submitted as a Git blob.

## Decision
SC1 remains EVIDENCE PARTIAL. No blob, tree, commit, or source-byte repository binding is claimed from this test.

## Acceptance invariant
SC1 may advance only after:
1. exact source bytes are submitted to create_blob with encoding=base64;
2. the resulting blob is bound into the reconciliation branch;
3. the blob is independently fetched;
4. reconstructed bytes are exactly 37,214 bytes; and
5. independent SHA-256 equals 47187900d5ae2f4e03f34b258318e259141d4b1bda61db26da8e052bb0f11758.

FAIL CLOSED remains active.
