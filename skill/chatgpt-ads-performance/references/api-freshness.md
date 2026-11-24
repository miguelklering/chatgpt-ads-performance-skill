# API freshness and compatibility

## Contents

1. Authoritative sources
2. Freshness gate
3. Known post-September 2026 changes
4. Drift handling
5. Repository maintenance

## 1. Authoritative sources

Use official sources:

- https://developers.openai.com/ads
- https://developers.openai.com/ads/api-overview
- https://developers.openai.com/ads/openapi.json
- https://developers.openai.com/ads/reporting
- https://developers.openai.com/ads/troubleshooting
- https://openai.com/policies/ad-policies/

Do not use third-party blog posts as endpoint authority.

## 2. Freshness gate

At the first session for an account, after a CLI update, after an unknown validation error, or when local documentation is more than seven days behind:

1. read the official API changelog
2. compare the current OpenAPI specification with the CLI version and command map
3. check the relevant endpoint page
4. check current policy before creative writes
5. record the verification date

If official docs cannot be reached, continue read-only with established endpoints and warn that feature freshness was not verified. Do not use a new or changed write contract from memory.

## 3. Known post-September 2026 changes

Validate these against current docs because they were added after the original skill's 2026-09-24 recheck:

- 2026-09-30: selectable click/view attribution windows and time basis on all four Insights endpoints
- 2026-10-26: enabled accounts can create ads with four to six square images using creative.file_ids

The official navigation also exposes newer surfaces such as Audit Logs and limited-beta Hotel Feeds. Treat them as feature-gated and feature-detect before use.

Do not assume the OpenAPI version number changes whenever the schema changes.

## 4. Drift handling

When CLI and official docs differ:

- read operations: use a documented CLI or raw GET only after confirming the endpoint
- writes: stop and show the incompatibility
- do not silently omit an unsupported field
- do not emulate a missing feature with a guessed request
- use raw write only after showing the exact official schema, dry-run equivalent, risk, and receiving explicit approval
- open an issue or prepare an implementation patch when the user requests code changes

If a report omits explicit attribution settings, label it legacy/default and do not compare it with a differently configured report.

## 5. Repository maintenance

For every API update:

1. update CLI endpoint support
2. update command and flag documentation
3. update this skill and affected references
4. update examples
5. add or update offline tests
6. run documentation consistency checks
7. record live-verified versus documentation-only behavior

Mechanical consistency does not replace behavioral skill evaluation. Test at least:

- broken measurement audit
- low-volume campaign with insufficient data
- profitable but delivery-constrained campaign
- high-spend campaign above target CPA
- rejected creative
- campaign creation with a stale API feature
- multiple accounts with ambiguous project mapping
