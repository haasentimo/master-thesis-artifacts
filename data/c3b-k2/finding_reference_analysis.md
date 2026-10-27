# C3b-K2 — finding-to-checked-file reference analysis

Total LLM findings analyzed (all 3 run-indices, DERIVED: excluded): **461**

## B3 — classification (overall)

| class | count | % |
|---|---|---|
| K1 | 329 | 71.4% |
| K2 | 36 | 7.8% |
| K3 | 12 | 2.6% |
| K4 | 84 | 18.2% |

### by run_index

| run_index | K1 | K2 | K3 | K4 |
|---|---|---|---|---|
| 0 | 111 | 12 | 4 | 28 |
| 1 | 109 | 12 | 4 | 28 |
| 2 | 109 | 12 | 4 | 28 |

### by category

| category | K1 | K2 | K3 | K4 |
|---|---|---|---|---|
| ABSENCE_REQUIRED | 0 | 14 | 0 | 0 |
| API_CONTRACT | 0 | 0 | 0 | 21 |
| CYCLE | 15 | 0 | 9 | 0 |
| FORBIDDEN_RELATION | 260 | 22 | 3 | 0 |
| FORBIDDEN_SIGNATURE_TYPE | 0 | 0 | 0 | 63 |
| STRUCTURAL_PLACEMENT | 54 | 0 | 0 | 0 |

### by rule_id

| rule_id | K1 | K2 | K3 | K4 |
|---|---|---|---|---|
| R-CORE-1 | 153 | 0 | 0 | 0 |
| R-CYCLE-1 | 12 | 0 | 0 | 0 |
| R-CYCLE-2 | 3 | 0 | 9 | 0 |
| R-FRAMEWORK-1 | 0 | 0 | 0 | 63 |
| R-INDEP-1 | 28 | 2 | 0 | 0 |
| R-LAYER-1 | 63 | 0 | 3 | 0 |
| R-PLACE-1 | 54 | 0 | 0 | 0 |
| R-PORT-1 | 0 | 3 | 0 | 0 |
| R-PORT-2 | 0 | 4 | 0 | 0 |
| R-PORT-3 | 0 | 4 | 0 | 0 |
| R-PORT-4 | 0 | 3 | 0 | 0 |
| R-PROTECT-1 | 16 | 20 | 0 | 0 |
| R-SIG-1 | 0 | 0 | 0 | 9 |
| R-SIG-2 | 0 | 0 | 0 | 3 |
| R-SIG-3 | 0 | 0 | 0 | 3 |
| R-SIG-4 | 0 | 0 | 0 | 6 |

## B5 — offending_type occurrence in the checked file's own prompt

offending_type findings: 152, found in own Imports/Signatures: 81, not found there: 71 (of which header-only match, i.e. the file's own module path: 54; absent everywhere in the prompt: 17)

## C1 — top 20 (rule_id, subject) pairs

| rule_id | subject | hit_count | n_distinct_files |
|---|---|---|---|
| R-FRAMEWORK-1 | `{"offending_type": "sqlalchemy.orm.Session"}` | 57 | 9 |
| R-PROTECT-1 | `{"from": "orders_services", "to": "core_adapters_internal"}` | 13 | 5 |
| R-PROTECT-1 | `{"from": "billing_services", "to": "core_adapters_internal"}` | 12 | 4 |
| R-CYCLE-2 | `{"from": "orders_services_pricing", "to": "orders_services"}` | 12 | 4 |
| R-PROTECT-1 | `{"from": "identity_services", "to": "core_adapters_internal"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "identity_api"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "identity_mappers"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "identity_models"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "identity_repository"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "identity_services"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "orders_api"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "orders_mappers"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "orders_models"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "orders_repository"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "orders_services"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "orders_services_pricing"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "billing_api"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "billing_mappers"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "billing_models"}` | 9 | 3 |
| R-CORE-1 | `{"from": "core", "to": "billing_repository"}` | 9 | 3 |

## C2 — 78 distinct (rule_id, subject) pairs (runs carry {0: 155, 1: 153, 2: 153} findings)

## C3 — pairs on more than 26 of 52 files: 0

## C4 — unique (single-file) pairs: 40

## D1 — the three zero-finding modules vs. the 49 reporting modules

| module | rules_in_scope | prompt_len | n_imports | n_signatures |
|---|---|---|---|---|
| depot.billing.models.legacy_tax_models | 3 | 4967 | 0 | 8 |
| depot.core.adapters.internal.cache | 2 | 3245 | 0 | 6 |
| depot.core.adapters.internal.session | 2 | 3354 | 0 | 8 |
| *(mean of 49 reporting modules)* | 3.10 | 4599 | 1.84 | 5.90 |

## D2 — rules in scope vs. mean finding count, over all 52 modules

| rules_in_scope | n_modules | mean_findings |
|---|---|---|
| 1 | 5 | 10.00 |
| 2 | 12 | 1.83 |
| 3 | 20 | 2.30 |
| 4 | 10 | 2.00 |
| 6 | 5 | 3.13 |
