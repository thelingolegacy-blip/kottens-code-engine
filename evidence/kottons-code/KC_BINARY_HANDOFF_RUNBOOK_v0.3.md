# KC Binary Handoff + Independent Verification Runbook v0.3

## Purpose
Complete SC1 only when the exact captured source bytes are committed to the reconciliation branch and independently re-hashed from repository checkout.

## Host-side handoff
1. Ensure the exact Library source exists as `KottonsCode_DraftOne.docx`.
2. Ensure `GITHUB_TOKEN` is available only to the host-side execution environment and has the minimum repository write permission required.
3. From the repository checkout, run:
   `python3 tools/reconciliation/kc_binary_handoff.py /absolute/path/to/KottonsCode_DraftOne.docx`
4. Record the emitted `GIT_BLOB_SHA`, `TREE_SHA`, `COMMIT_SHA`, branch, and path.
5. Do not edit or transform the DOCX before execution.

## Independent verification
After the commit exists:
1. Checkout the resulting reconciliation commit.
2. Run:
   `python3 tools/reconciliation/kc_source_verify.py`
3. Confirm:
   - SIZE=37214
   - SHA256=47187900d5ae2f4e03f34b258318e259141d4b1bda61db26da8e052bb0f11758
   - KC_SOURCE_VERIFY=PASS
4. Preserve the workflow run URL/job/log evidence with the commit SHA.
5. Independently compare the handoff commit and verification commit/run.

## Acceptance boundary
SC1 remains NOT ACCEPTED until repository bytes are demonstrably identical to the captured source artifact and the result is independently verified. Metadata, a script, a workflow definition, or an asserted commit is not itself sufficient.

## Security
Never transport the manuscript through public issues, comments, pull-request text, logs, or other public content. Do not print Base64 source bytes into logs.
