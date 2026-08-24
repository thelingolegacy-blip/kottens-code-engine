# KottonsCode Activation Matrix

| Layer | Target | State | Gate |
|---|---|---|---|
| Frontend | Next.js/TypeScript world UI | Prepared | CI/build |
| Animation | cloud drift, Kotton float, radial soundwave | Prepared | accessibility QA |
| Content | Watch/Play/Read/Collect manifests | Foundation | content sources |
| Firebase | auth/content/security baseline | Prepared | project credentials |
| Cloudflare | Worker API/edge layer | Prepared | account + secrets |
| Netlify | production build target | Prepared | site/domain binding |
| GitHub | feature branch + PR + CI | Active | workflow run |
| Flutter | shared client architecture | Planned | API contract |
| Agents | ingestion/normalization workers | Planned | approved provider credentials |
| Phone assets | original Kotton images/media | Blocked | user upload/resource flow |
| Secrets | primary/backup key slots | Safe placeholders | authorized secret entry |
| Domain | custom production hostname | Pending | DNS ownership/verification |

## Audit rule
A layer is not marked production-live merely because its code exists. It becomes live only after its external provisioning and verification gate succeeds.

## Required release evidence
1. Successful typecheck.
2. Successful production build.
3. Passing responsive smoke tests.
4. Passing accessibility/reduced-motion checks.
5. Passing API health/content checks.
6. Verified secrets without source exposure.
7. Verified domain/DNS.
8. Rollback target retained.
