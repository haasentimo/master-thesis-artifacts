# C6 — Auswertungsspezifikation (vor der Implementierung)

**Masterarbeit Timo Haas · HTWG Konstanz**
Stand: 26.08.2026 · Auftrag C6A. Dieses Dokument SPEZIFIZIERT die Auswertungsharness (C6); es
implementiert sie nicht. Kein Modell-Call, kein Werkzeuglauf, kein Code ist für seine Erstellung
gelaufen. Alle Aussagen sind aus den unten zitierten Quellen gezogen; jede Stelle, an der die
Quellen sich widersprechen oder eine Frage offenlassen, steht in Abschnitt 10 und wurde nicht
stillschweigend aufgelöst.

**Randbemerkung zur Arbeitsumgebung:** Der Auftrag geht von `~/ma/masterarbeit` und
`~/ma/tritongraph` aus; auf dieser Maschine liegen die Repos unter `~/Schreibtisch/masterarbeit`
und `~/Schreibtisch/tritongraph`. Beide wurden vor Beginn geprüft: `git status --porcelain` leer
in beiden, kein ausstehender `git fetch`-Unterschied zum jeweiligen `origin`. `tritongraph` wurde
ausschließlich mit `Read` gelesen; `git status --porcelain` dort ist auch nach Abschluss dieses
Auftrags leer.

**Nachtrag 26.08.2026 (Auftrag D3a) — dieses Dokument ist auf den D1-Stand gezogen.** Zwei
Arten von Änderung, beide ergänzend, kein Alttext entfernt: **(a)** §1.6 und §10.1 führten
`expected_match_key.K2_K3` für I21–I24 noch als Platzhalter — die vier Schlüssel stehen seit
**D1** (Commit `40bf33a`) im Manifest und sind hier **wörtlich aus
`data/soll/injection_manifest.json`** eingetragen; der überholte Text steht **durchgestrichen**
stehen. **(b)** Vier in **Protokoll Rev. 31** neu registrierte Punkte sind als Anforderungen an
C6b aufgenommen: der `FORBIDDEN_SIGNATURE_TYPE`-Ausfallmodus und die
`STRUCTURAL_PLACEMENT`-Fussnote in **§3.4**, die Ruhezustandszahl je Injektion und die
paarweise Spalte in **§7.5**, beides mit Pflichtbestandteilen in **§8** (Punkte 7 und 8). **Der
SHA256 dieses Dokuments ändert sich damit**; er ist in Protokoll §1 (Nachtrag Rev. 30,
Auswertungseingang) nachgezogen — alter Hash gestrichen, neuer daneben.

**Nachtrag 27.08.2026 (Aufträge C6b-2, C6b-2a, C6b-2b) — die K4/K5-Matchregel ist
spezifiziert.** Drei Änderungen, alle ergänzend, kein Alttext entfernt: **(a)** §10.4 (offener
Punkt 4, Anhang-A-Zeile A-21 des Tabellenskeletts) ist **erledigt** und mit auflösendem
Nachtrag gekennzeichnet — die generische Regel steht in `tools/match_k4k5.py`, eine je besetzter
Zelle von T8. **(b)** §6.2 trägt eine **Korrektur**: der Parameter der Test-ID der vier
Portregeln ist die `rule_id`, nicht der Modulname; der Schluss der Passage bleibt richtig.
**(c)** §1.4 nimmt die **Terminalbreite** als Umgebungsparameter der K4-Messung auf — der
archivierte Rohtext ist bei 80 Spalten umgebrochen. **Der SHA256 dieses Dokuments ändert sich
damit**; er ist in Protokoll §1 (Nachtrag Rev. 30, Auswertungseingang) und in §0.1 nachgezogen —
alter Hash gestrichen, neuer daneben. **Keine Metrikänderung, keine Manifeständerung, keine
Zelle der Erwartungsmatrix bewegt sich.**

**Nachtrag 28.08.2026 (Auftrag C6c-a) — T7 steht auf den gehashten Laufmanifesten.** Drei
Änderungen, alle ergänzend, kein Alttext entfernt: **(a)** neues **§1.8** — die Eingänge von
T7 sind die Laufmanifeste unter `data/campaign/manifests/`, ein Manifest je Invocation,
jedes von einem Block-`SHA256SUMS` bezeugt; `journal.jsonl` und die Prosa-Manifeste sind
seither **Gegenprobe, nicht Quelle**, und eine Abweichung ist ein **Befund**, der berichtet
und **nicht** durch Angleichen einer Seite aufgelöst wird. **(b)** §8 erhält **Punkt 9** —
die Blindheitsauflage ist präzisiert: die Laufmanifeste sind ausdrücklich **erlaubt** (sie
tragen Verdikte, Zähler und Provenienz, **keine Funde**), Findings bleiben gesperrt, und die
Selbstauditierung der Harness prüft das über eine **positive** Erlaubnisliste. **(c)** §7.4
nennt die **lebenden Dokumente**, die planmäßig ungehasht bleiben. **Der SHA256 dieses
Dokuments ändert sich damit**; er ist in Protokoll §1 (Nachtrag Rev. 30, Auswertungseingang)
und in §0.1 nachgezogen — alter Hash gestrichen, neuer daneben. **Keine Metrikänderung,
keine Manifeständerung, keine Zelle der Erwartungsmatrix bewegt sich** — bewegt hat sich
allein, aus **welcher Datei** dieselben T7-Zahlen gelesen werden.

**Nachtrag 28.08.2026 (Auftrag C14) — die ARTEFAKTAUSWAHL steht auf dem Laufverdikt, und
die Overlap-Analyse aus Protokoll §8 UF3 bekommt eine Tabelle.** Drei Änderungen, alle
ergänzend, kein Alttext entfernt: **(a)** neues **§1.9** — welches Laufartefakt je Paar
(Konfiguration, Injektion) gelesen wird, entscheidet **`postrun.verdict` des gehashten
Laufmanifests**, nicht der Dateiname; dazu die Zusicherung **R12**, die den Lauf abbricht,
wenn ein Artefakt mit einem Verdikt ≠ `VALID` in die Auswertung gelangt. **(b)** §8 erhält
**Punkt 10** — die **Overlap-Tabelle T10**, gebildet aus den **bereits gerechneten**
Trefferzellen, ohne neue Metrik und ohne neue Schwelle. **(c)** §8 Punkt 1 trägt einen
**Verweis** darauf, dass die Ausgabe die mit **Rev. 42** erledigte Anforderung T5 (ii) auch
im gedruckten Text als erledigt führt. **Der SHA256 dieses Dokuments ändert sich damit**; er
ist in Protokoll §1 (Nachtrag Rev. 30, Auswertungseingang) und in §0.1 nachgezogen — alter
Hash gestrichen, neuer daneben. **Keine Metrikdefinition, kein Injektionsmanifest, keine
Regeldatei, kein Prompt, kein Schema ist berührt**; `strict`, `localized`, Precision, Recall,
F1, Median, Spannweite und die FP-Rate stehen zeichengleich. Bewegt hat sich allein, **welche
Datei** dieselbe, unveränderte Metrik liest — und dass eine bereits gerechnete Zelle ein
zweites Mal, schnittweise, ausgewiesen wird.

---

## 1. Eingänge — erschöpfend, mit Feldnamen und Fundstelle

### 1.1 `--json-out` — `ConformanceResultDocument` (`jsonOut.ts`)

Ein Objekt je CLI-Aufruf (= je Konfiguration je Injektions-Commit bzw. je Kontrolllauf).
Enthält **jede** Repetition, ohne Aggregation (`jsonOut.ts:94-104`, `RESULT_SCHEMA_VERSION = '1'`).

```
ConformanceResultDocument
├─ result_schema_version, run_id, timestamp
├─ provenance: ResultProvenance
│   ├─ topology_sha256, rules_sha256          ← NUR HIER und im run_header, s. 1.3
│   ├─ prompt_template_sha256, user_prompt_render_sha256
│   ├─ checker_git_head, target_repo_git_head, base_ref, rule_graph_mode
│   ├─ model_requested, endpoint, seed_requested, temperature_requested
│   ├─ runs_requested, timeout_ms
│   ├─ changed_files_count                    ← Teil der Lauf-Akzeptanzregel Injektionslauf
│   └─ control_files_count                    ← Teil der Lauf-Akzeptanzregel Kontrolllauf
├─ runs: JsonRun[]                            ← run_index, findings[], checks_performed[]
│   └─ JsonFinding (`jsonOut.ts:49-67`, `toJsonFinding` 142-159):
│       match_key, source ('rule-engine'|'llm'), rule_id, category, component, module,
│       file, line, symbol, severity, subject { offending_type?, via?, from?, to? },
│       reason, suggestion, confidence
├─ validity: ResultValidity
│   status, runs_completed, calls_total, calls_invalid, calls_transport_failed,
│   skipped_count, invalid_reasons, exit_code
└─ skipped: SkippedFile[]
```

`match_key` ist **verbatim** aus `matchKey.ts` zu übernehmen (`jsonOut.ts:50`, Kommentar: „never
reformat it"). Der Harness-Join läuft ausschließlich hierüber (§3, §4).

### 1.2 `--run-log` — JSON-Lines (`runLog.ts`)

Drei Satzarten, `record_type` diskriminiert:

**`run_header`** (`runLog.ts:29-97`, vor jedem Modell-Call geschrieben): trägt u. a. `run_id`,
`cli_args`, `rule_graph_mode`, `topology_path`/`topology_sha256`, `rules_path`/`rules_sha256`,
`prompt_template_sha256`, `user_prompt_render_sha256`, `target_repo_git_head`, `checker_git_head`,
`base_ref`, `src_roots`, `model_requested`, `endpoint`, `seed_requested`,
`temperature_requested`, `provider_pin`, `runs_requested`, `timeout_ms`,
`transport_max_retries`, `transport_abort_threshold`, `changed_files_count`,
`control_files_count`, `control_files_overlap`, `graph_files_count`, `skipped`.

**`llm_call`** (`runLog.ts:99-140`, ein Satz je geprüfter Datei je Repetition): `run_id`, `file`,
`module`, `diff_kind` ('modified'|'control'|…), `model_requested`, `model_version`,
`provider_served`, `attempts[]`, `attempts_used`, `valid_raw`, `valid_final`, `outcome`
('measured'|'transport_failed'), `transport_failures[]`, `tokens_in_total`, `tokens_out_total`,
`latency_ms_total`, `temperature_requested`, `seed_requested`, `run_index`.

**`run_footer`** (`runLog.ts:147-169`, immer letzte Zeile, auch bei Absturz geschrieben —
Abwesenheit heißt „Lauf hart gestorben"): `run_id`, `status` ('completed'|'aborted'),
`runs_requested`, `runs_completed`, `calls_total`, `calls_invalid`, `invalid_calls[]`,
`calls_transport_failed`, `failed_calls[]`, `calls_with_transport_retry`, `skipped_count`,
`exit_code`, `invalid_reasons[]`, **`wall_clock_ms`** (`Date.now() - startedAt` über den ganzen
CLI-Aufruf, `run.ts:112,260`).

`InvalidReason` (`reporter.ts:22-26`) kennt genau vier Werte: `invalid_final_response`,
`transport_failure`, `incomplete_runs`, `skipped_files`. **`changed_files_count` gehört NICHT zu
`invalid_reasons`** — das Nachlaufskript/die Harness müssen die Lauf-Akzeptanzregeln (§7)
zusätzlich selbst prüfen, der CLI-Runner vollstreckt sie nicht (Protokoll §6 Nachtrag Rev. 24,
`reporter.ts:59-64`).

### 1.3 `topology_sha256` und `rules_sha256` stehen NUR im Kopf

Bestätigt am Quelltext: beide Felder existieren ausschließlich in `RunHeaderRecord`
(`runLog.ts:40,42`) und in `ResultProvenance` (`jsonOut.ts:29-30`) — **nicht** in `JsonFinding`
und nicht in `llm_call`. Eine Harness, die pro Fund die Provenienz prüfen will, muss den Kopf des
jeweiligen Dokuments mitlesen und mit jedem Finding assoziieren, nicht das Finding selbst danach
durchsuchen (4c-Bericht §8.3 referenziert dieselbe Eigenschaft für den Soll-Validator-Lauf).

### 1.4 K4 — Textausgabe von `lint-imports` (import-linter 2.13)

Belegt in `c2a_bericht_contract_semantik.md`, `c2b_bericht_erlaubnislisten.md`,
`c2b_bericht_k4_konfiguration.md`. Zeilenformen, wörtlich gemessen:

- **Kopfzeile je Lauf:** `Analyzed N files, M dependencies.` — `N`/`M` sind **nur zusammen mit der
  Schaltereinstellung `include_external_packages`** interpretierbar (mit Schalter zählen
  zusammengefasste externe Wurzeln mit; `c2b_bericht_erlaubnislisten.md` §B5, Nebenbefund zu den
  Zählern: `21 files` → `23 files` bei identischem Baum).
- **Contract-Zusammenfassung, je Contract eine Zeile:** `<statement-artiger Name> KEPT` oder
  `<…> BROKEN`, z. B. `orders.services darf core.adapters.internal nicht importieren BROKEN`.
- **Fußzeile:** `Contracts: N kept, M broken.`
- **`layers`/`forbidden`-Detailzeilen** (nur bei `BROKEN`, mit Modulpfad und Zeilennummer):
  `<Modul-A> -> <Modul-B> (l.<N>)`, z. B. `depot.orders.api.routes -> sqlalchemy (l.3)`.
- **`layers` mit `exhaustive=True`, undeklariertes Kind** (trägt sehr wohl den vollen Modulpfad,
  anders als der Zyklenblock unten):
  ```
  The following modules are not listed as layers:
  - depot.orders.legacy_order_index

  (Since this contract is marked as 'exhaustive', every child of every container
  must be declared as a layer.)
  ```
- **`acyclic_siblings`, Zyklenblock — OHNE Modulnamen, relativ zum `ancestor`, mit
  Importzähler, führendem Punkt:**
  ```
  No cycles are allowed in depot.orders.
  It could be made acyclic by removing 1 dependency:
  - .mappers -> .api (1 import)
  ```
  **Ein gebrochener Contract kann MEHRERE solcher `No cycles are allowed in …`-Blöcke enthalten,
  je Ebene einen** (c2a §2.2c, gemessen mit `ancestors` auf der Wurzel: ein Contract meldet
  gleichzeitig einen Block für `depot` und einen für `depot.orders`). Die K4-Auswertung muss also
  eine **Liste von Blöcken je Contract** lesen, nicht einen Block je Contract.
- **Konfigurationsabbruch, vor jeder Contract-Auswertung** (kein `KEPT`/`BROKEN`, kein Contract
  ausgewertet): z. B. `The top level configuration must have include_external_packages=True when
  there are external forbidden modules.` oder `Contract "…" is not configured correctly:
  containers.`

> **Nachtrag 27.08.2026 (C6b-2b) — DER K4-ROHTEXT IST AN DER TERMINALBREITE GEFORMT.**
> Begründung: `c6b2_bericht_matchregel.md` Teil II/III; gemessen am Messstand.
>
> import-linter rendert über **`rich`** (`importlinter/application/output.py`:
> `console = Console(highlight=False)`). Eine `rich`-Konsole, deren Datei **kein Terminal**
> ist, fällt auf **80 Spalten** zurück. Der Kampagnen-Runner erfasst stdout über eine **Pipe**
> (`tools/run_campaign.py:783`, `subprocess.run(..., capture_output=True)`), und **`COLUMNS`
> steht in der Runner-Umgebung nicht**. Gemessen unter genau dieser Bedingung:
> `console.width = 80`, `is_terminal = False`, `encoding = utf-8`.
>
> **Folge:** jede gerenderte Zeile über 80 Spalten steht im Archiv als **mehrere physische
> Zeilen**. Eine reale Detailzeile `- <Modul-A> -> <Modul-B> (l.<N>)` ist bei voller
> Modultiefe **über 80 Zeichen** lang und daher regelmässig umgebrochen. Drei Umbruchformen
> sind gemessen und in `tools/match_k4k5.py` (`unwrap_k4`) modelliert: **weich** an der
> Wortgrenze (Bruchteil behält das Trennzeichen), **hart** innerhalb eines Tokens, das breiter
> ist als die Konsole (Bruchteil exakt 80 Spalten, Token zerschnitten), und **bündig** an einer
> Wortgrenze bei exakt 80 Spalten (Bruchteil exakt 80 Spalten, **Trennzeichen verworfen**).
> Die letzten beiden sehen von aussen gleich aus und werden strukturell unterschieden.
>
> **Das ist ein Umgebungsparameter der Messung, kein Werkzeugbefund.** Die K4-Auswertung
> **muss die logische Zeile vor jedem Mustervergleich wiederherstellen**; ein Muster, das auf
> physischen Zeilen arbeitet, verfehlt jede umgebrochene Detailzeile. **Ein
> Reproduktionsversuch mit anderer Terminalbreite (oder gesetztem `COLUMNS`, oder Ausgabe auf
> ein Terminal) steht vor ANDEREM ROHTEXT** bei identischem Werkzeug, identischer
> Konfiguration und identischem Baum — die Befundmenge ist dieselbe, ihre Zeilenaufteilung
> nicht. Wer die Kampagne nachfährt, muss die Breite mitführen.
>
> **Der archivierte Rohtext bleibt wie er ist.** Keine Neuerfassung, keine Änderung am Runner,
> kein Amendment am Protokoll: die Zeilenaufteilung ist reversibel, und die Reversion ist
> spezifiziert.

### 1.5 K5 — pytest-Ausgabe (PyTestArch 4.0.1 / pytest 9.0.1)

Belegt in `c2a_bericht_contract_semantik.md` §5.1, `c2c_bericht_k5_konfiguration.md`.

- **Erfolgsform:** `N passed in X.XXs`, Exit 0.
- **Gebrochene Regel — FAILED, mit parametrisierter Test-ID, die die Komponente trägt:**
  ```
  FAILED …::test_component_imports_only_whitelisted_modules[orders_mappers]
  E   AssertionError: "depot.orders.mappers.order_mapper" imports "depot.orders.api.routes".
  ```
  Der Regelname ist darin **die parametrisierte Test-ID** (`test_component_imports_only_
  whitelisted_modules[<Komponente>]`); die verbietende Hälfte der Erlaubnislistenregel wertet **je
  Import und je Modul** und benennt das schuldige Modul in der `AssertionError`-Nachricht
  (`"<Modul>" imports "<Modul>".`, c2b §1c/§1d). Bei mehreren nicht gelisteten Importen entstehen
  mehrere Zeilen, alphabetisch nach Zielmodul, ohne Abschneidung.
- **`NetworkXError`-Abbruch — ERROR, keine `AssertionError`, kein `FAILED`, kein Befund:**
  ```
  NetworkXError: The node depot.core.portz is not in the digraph.
  ```
  Auslöser: eine Regel nennt ein Modul, das nicht (mehr) im Graphen ist — Tippfehler im Ziel
  (§2, „vierter Ausfallmodus") oder ein externer Knoten, dessen letzter Importeur durch eine
  Injektion verschwindet (§2, „fünfter Ausfallmodus", nur unter `exclude_external_libraries =
  False`). Für die K5-Auswertung heißt das: **ERROR ≠ FAILED ≠ „kein Befund, weil konform"** — ein
  `NetworkXError` ist ein Werkzeugabbruch für **diese eine** Regel und liefert für sie **keine**
  Aussage, unterscheidet sich damit von einem regulären `passed`.

### 1.6 `data/soll/injection_manifest.json` — Felder je Injektion

32 Einträge (`I01`–`I32`), Top-Level-Schlüssel `injections[]`, `distribution_l2`,
`completeness_check`. Je Injektion (Feldnamen wie im JSON, nicht alle bei jeder Kategorie
vorhanden):

`id`, `scenario_l2`, `category_l1`, `injection_ref`, `injection_sha256`, `carrier_module`,
`carrier_component`, `affected_method_or_signature`, `rule_id`, `expected_edge_boundary`,
`z2prime` (nur `CYCLE`: `S`, `T`, `S_lt_T`, `S_sole_importer_of_T`, `candidate_set_size`),
`expected_match_key` (Objekt mit den Schlüsseln `K1` und `K2_K3`; einer der beiden ist bei
strukturell nicht-K1-fähigen bzw. LLM-nicht-vorhergesagten Kategorien `null`),
`expected_co_findings` (Array, s. §5), `co_findings_note`, `k4_match_rule`, `k5_match_rule`
(beides **Prosa**-Beschreibungen je Injektion, keine maschinenlesbare generische Regel — s.
Abschnitt 10), `matrix_cell_ref`.

~~Vier Injektionen (`I21`–`I24`, `FRAMEWORK_TYPE_IN_SIGNATURE`) tragen bei~~
~~`expected_match_key.K2_K3` **den Literal-String `"OFFEN — …"`** statt eines Schlüssels — dazu~~
~~Abschnitt 10.~~

**Nachtrag 26.08.2026 (D3a) — überholt, gestrichen stehen gelassen.** Die vier Schlüssel
stehen seit **D1** (Commit `40bf33a`, `d1_bericht_matchkey_eintrag.md`) im Manifest; der
Platzhalter-String existiert dort nicht mehr. **Wörtlich aus
`data/soll/injection_manifest.json` gelesen** — `expected_match_key.K2_K3`, nicht aus einem
Bericht übernommen; `expected_match_key.K1` ist bei allen vieren `null`:

```
I21  FORBIDDEN_SIGNATURE_TYPE|identity_models|depot.identity.models.customer_models|sqlalchemy.orm.Session
I22  FORBIDDEN_SIGNATURE_TYPE|orders_models|depot.orders.models.order_models|sqlalchemy.orm.Session
I23  FORBIDDEN_SIGNATURE_TYPE|orders_models|depot.orders.models.order_line_models|sqlalchemy.orm.Session
I24  FORBIDDEN_SIGNATURE_TYPE|billing_models|depot.billing.models.invoice_models|sqlalchemy.orm.Session
```

Damit trägt **jede** der 32 Injektionen entweder einen realen Schlüssel oder ein bewusstes
`null` (I13–I16 bei `K2_K3`, `CYCLE`); ein Platzhalter-String kommt im Manifest **nicht
mehr** vor. Das ist kampagnenkritisch, weil `FORBIDDEN_SIGNATURE_TYPE` **die einzige
Kategorie ist, in der allein K2/K3 etwas finden können** (Protokoll §3, Amendment Rev. 20:
K1 nein, K4 und K5 nein) — ein Platzhalter an dieser Stelle liesse den Join genau dort
ausfallen. Siehe Abschnitt 10.1.

`completeness_check` (Top-Level) dokumentiert maschinell geprüfte Eigenschaften des Manifests
selbst: `line_count: 32`, `ids_gapless`, `distribution_by_scenario`,
`each_carrier_module_appears_exactly_once`, `all_rule_ids_exist_in_architecture_rules_yaml_…`,
`cycle_rows_satisfy_z1_z4_and_z2prime_i_ii`, `layer_back_call_rows_carry_preregistered_k4_double_
report`, `no_forbidden_relation_row_carries_k1_co_finding`, u. a. — die Harness sollte diese Sätze
als Vorbedingungen prüfen, bevor sie das Manifest als Ground Truth verwendet.

### 1.7 Kontrollläufe `data/c3b-k2/` und `data/c3b-k3/`

Je Konfiguration: 52 Einzeldatei-Invocations (Einzeldatei-Zerlegung, nicht ein `--control-files`
mit 52 Zeilen in einem Aufruf), mit eigenem `run_manifest.json` des Kampagnen-Runners:

```
run_manifest.json
├─ overall_start, overall_end, aborted_files
└─ invocations[]: { index, attempt, file, control_file, start, end, duration_s,
                     exit_code, timed_out, crashed, run_log, json_out,
                     stdout_tail, postcheck_exit, postcheck_output, valid }
```

`duration_s` ist die vom **Kampagnen-Runner** gemessene Wanduhrzeit je Invocation (Subprozess-Start
bis -Ende) — zu unterscheiden von `run_footer.wall_clock_ms`, das nur die Zeit **innerhalb** des
CLI-Prozesses selbst misst (s. Abschnitt 10, wall-clock-Frage). Zusätzlich je Kontrolllauf:
`finding_reference_analysis.json`/`.md` (Selbst-/Fremd-/Zielbezug der Findings, R-CORE-1-Analyse)
und `control_files_facts.json`.

### 1.8 T7 — die Laufmanifeste `data/campaign/manifests/` (nachgetragen 28.08.2026, C6c-a)

**Quelle von T7.1, T7.2, T7.3 und T7.4 sind die Laufmanifeste**, ein Manifest je Invocation,
benannt `<cfg>[_<modus>]_<repo-sha>[_r<n>].json` und **von einem Block-`SHA256SUMS`
bezeugt**. Gelesen wird je Invocation:

| Feld im Manifest | geht ein in |
|---|---|
| `run.config`, `run.injection_id`, `attempt`, Dateiname-Suffix `_r<n>` | T7.1 (Invocationen, Wiederholungen), T7.4 |
| `postrun.verdict` | T7.1 (VALID/INVALID), T7.3 (Injektionen ohne gültigen Lauf) |
| `postrun.detail.invalid_reasons` | T7.1 (Werte, `skipped_count`), T7.4 (Grund) |
| `postrun.detail.calls_total` | T7.1 (Model-Calls), T7.2 (Zählregel `1 × runs`) |
| `postrun.detail.calls_invalid`, `…calls_transport_failed` | T7.1; daraus **abgeleitet** `valid_final` |
| `postrun.detail.changed_files_count` | T7.2 (Zählregel `== 1`) |
| `postrun.detail.kept`/`broken`/`evaluated`/`expected_contracts` (K4) | T7.2 (positive Akzeptanz) |
| `postrun.detail.collected`/`expected_collected` (K5) | T7.2 (positive Akzeptanz) |
| `external_wall_clock_ms` | T7.1 (Wanduhr), §8 Punkt 6 |
| `not_performed`, `is_smoke_test` | Ausschluss aus jeder Zählung |

**`valid_final` ist kein Feld, sondern eine Ableitung** und als solche auszuweisen:
gemessene Calls = `calls_total` − `calls_transport_failed`; `valid_final` = gemessene Calls
− `calls_invalid`. Der **Anteil** steht über den **gemessenen** Calls (`outcome: measured`);
die Transportausfälle stehen **daneben, nie darin** (Skelett T7.1). Ebenso ist
`skipped_count` abgeleitet — der Checker führt übersprungene Dateien als
`invalid_reasons`-Wert `skipped_files` (`reporter.ts:59-64`), ein eigenes Feld gibt es nicht.

**Warum nicht `journal.jsonl` und nicht die Prosa-Manifeste.** Beide sind **ungehasht** und
bleiben es planmäßig (§7.4): das Journal ist append-only und wächst, die `MANIFEST.md` sind
fortzuschreibende Dokumente. T7 ist die Tabelle, die den **Messbestand bezeugt**; sie darf
nicht auf einer Datei ruhen, deren Bytestand kein `SHA256SUMS` deckt.

**Beide bleiben als GEGENPROBE verbindlich** (Skelett T7.3 nennt sie namentlich). Verglichen
werden je Konfiguration: Zahl der Invocationen, Zahl der gültigen Injektionen und die Liste
der Injektionen ohne gültigen Lauf. **Weichen sie ab, ist das ein Befund** — er wird in T7
als `ABWEICHUNG` gedruckt, im Kopf der Ausgabe als Banner geführt und auf `stderr` gemeldet;
**keine Seite wird an die andere angeglichen**, und die Ausgabe ist nicht zu verwenden,
bevor geklärt ist, welche Seite falsch ist.

### 1.9 Welches Artefakt je Paar (Konfiguration, Injektion) gelesen wird (nachgetragen 28.08.2026, C14)

**Die Auswahl steht auf dem Laufmanifest, nicht auf dem Dateinamen.** Für jedes Paar
(Konfiguration, Injektion) liest die Auswertung das Laufartefakt, dessen **gehashtes
Laufmanifest** (§1.8) `postrun.verdict == VALID` trägt. Liegen **mehrere** gültige Versuche
vor, gilt der **früheste** — der kleinste `attempt`. Liegt **keiner** vor, ist die Zelle
`n. e.` mit Eintrag in **T7.3**; ein Artefakt wird dann **nicht** gelesen.

**Der Pfad folgt aus dem Manifestnamen**, nicht aus einem Glob: das Manifest
`<cfg>[_<modus>]_<repo-sha>[_r<n>].json` benennt das Artefakt
`data/campaign/<cfg>/<derselbe Name>` — für K1/K2/K3 mit der Endung `.json`, für K4/K5 mit
`.stdout.txt`. **Weder der Dateiname noch die Zahl der Records** entscheidet die Auswahl:
beide sind stumm darüber, ob der Lauf gültig war.

**Anlass, ungeschminkt.** Die bis dahin implementierte Regel war der Glob
`<cfg>_*<injection_sha256>.json`; er trifft die Datei **ohne** `_r<n>`-Suffix, also den
**ersten** Versuch. Für **elf** K3-Injektionen (I05, I06, I07, I09, I11, I13, I16, I20, I21,
I22, I23) trägt dieses Artefakt im Laufmanifest `postrun.verdict = INVALID` mit dem Grund
`transport_failure`; ausgezählt in `c11d_bericht_befund08_grundlagen.md` §A6b. K2 ist nicht
betroffen (null Wiederholungen).

**R12 — Zusicherung, Exit 2.** Die Harness prüft am Ende des Laufs jedes Artefakt, aus dem
sie Funde gelesen hat, gegen das Laufmanifest desselben Namens: fehlt das Manifest oder trägt
es ein Verdikt ≠ `VALID`, bricht der Lauf mit **Exit 2** ab und nennt Artefakt, Paar und
Verdikt. **Die Zusicherung ist unabhängig von der Auswahlregel formuliert** — sie fragt die
gelesenen Dateien, nicht den Auswähler; eine Rückkehr zur Namensregel fiele damit auf, statt
still zu wirken.

**Was R12 NICHT abdeckt, ausdrücklich benannt.** Die Run-Logs `*.jsonl` unter
`data/campaign/k2/` und `k3/` werden für **T6** (Tokens, Latenz je Call) über **alle**
Invocationen gelesen, gültige wie ungültige — die Laufkosten sind angefallen, unabhängig vom
Verdikt. Sie tragen **keine** Zelle einer Trefferrechnung und stehen deshalb ausserhalb von
R12. **T6 bewegt sich durch diese Änderung nicht.**

---

## 2. Erste Stufe: Filter nach Mechanismus

**Vor jeder der beiden Metriken** ist die Recordmenge nach dem Mechanismus zu filtern, nicht nach
dem Aufruf (Protokoll §4 Nachtrag Rev. 25):

- **K1** := alle Records mit `rule_id`-Präfix `DERIVED:` (aktuell `DERIVED:forbidden-edge`,
  `DERIVED:cycle`).
- **K2, K3** := alle Records mit **jedem anderen** `rule_id`.

**Grund.** Die registrierten K2/K3-Aufrufzeilen führen `--rule-graph diff`, wodurch der
deterministische Pfad **mitläuft** und in dasselbe `--run-log`/`--json-out` schreibt. Ein K2- oder
K3-Dokument enthält also grundsätzlich die **Vereinigung** aus LLM-Findings und
`DERIVED:*`-Findings. Ohne den Filter:

- **`strict` ist unbetroffen** (die Kategoriesegmente von `DERIVED:*`-Records — `layer-violation`,
  `cycle` — treffen den erwarteten K2/K3-Schlüssel `FORBIDDEN_RELATION|…`/`CYCLE|…` nie), gilt
  aber trotzdem einheitlich, weil die Menge vor beiden Metriken **gleich** zu bilden ist.
- **`localized` wäre konfundiert**, weil es auf **Stelle** trifft, nicht auf Kategorie: ein
  `DERIVED:*`-Record liegt bei jeder der sechzehn strukturellen Injektionen am richtigen Modul —
  K2/K3 bekämen dort einen `localized`-Treffer, **auch wenn das Modell nichts gemeldet hat**, und
  zwar in genau den Kategorien, in denen K1 der Vergleichsmaßstab ist.

Der Filter greift **vor** beiden Metriken und **vor** der FP-Rate. Für den Kontrolllauf auf `B`
ist die K1-Menge leer (C3a: 0 Findings), der Filter dort ohne Zahlenwirkung, aber unverändert
anzuwenden.

---

## 3. `strict` — exakte Übereinstimmung

**Definition:** exakter String-Vergleich `Finding.match_key` ↔
`Manifest.expected_match_key[K1 | K2_K3]` (Pfadauswahl nach §2-Filter). **Keine Normalisierung** —
Zeichenkettenvergleich, Zeichen für Zeichen. Zeilennummern sind nicht match-relevant.

### 3.1 Schlüsselbildende Schreibweisen (verbindlich, Protokoll §3 Nachtrag Rev. 18/19)

`match_key = category|component|module|subjectKey` (`matchKey.ts:26`).

| Kategorie | `subject`-Form | `subjectKey` trägt | Beispiel |
|---|---|---|---|
| `FORBIDDEN_RELATION`, `CYCLE` | `subject.from`/`subject.to` | `from->to` | `identity_repository->identity_services` |
| `ABSENCE_REQUIRED` | `subject.offending_type` | Porttyp **vollqualifiziert, mit Punktkette**, in der Schreibweise des `statement` | `depot.core.ports.TokenSigner` |
| `API_CONTRACT` | `subject.offending_type` | Symbolname als **`Class.method`**, bei Top-Level-Funktion der bloße Name | `SessionRepository.touch`, `to_payload` |
| `STRUCTURAL_PLACEMENT` | `subject.offending_type` | **volle Punktkette** des fehlplatzierten Moduls | `depot.billing.legacy_tax_models` |
| `FORBIDDEN_SIGNATURE_TYPE` | `subject.offending_type` | **Framework-Typname**, wörtlich wie im Code (Decision Record L/P) | `sqlalchemy.orm.Session` |

Für alle sechzehn Regelstatements ist die erwartete Subjektform **im `statement` selbst benannt**
(Protokoll §4 Nachtrag Rev. 19) — das ist Instrumenteneigenschaft, nicht Modellleistung: wählt das
Modell die andere Form (Kantenpaar statt `offending_type` oder umgekehrt), trifft der Schlüssel
nie, unabhängig von der inhaltlichen Richtigkeit der Erkennung.

### 3.2 Mehrere Records auf dieselbe Injektion

`strict` dedupliziert **nicht**. Von mehreren Findings zählt das mit passendem Schlüssel als
**einen** TP, **jedes weitere** — mit demselben oder abweichendem Schlüssel — als FP (Protokoll
§4 Hauptregel, Decision Record O §1). Das gilt auch für zwei Findings, die inhaltlich denselben
Verstoß beschreiben, aber unterschiedliche `subjectKey`-Schreibweisen tragen (Befund 06.7: `import`,
`parameter`, `function`, `flask` für denselben Verstoß) — jede zusätzliche Schreibweise ist ein FP.

### 3.3 Zyklen (`CYCLE`) — Sonderregel für K1

Der Record trägt genau eine Kante (`subject = {from, to}`, `ruleEngine.ts:155`). `strict` ist ein
Treffer, wenn der `match_key` dem **handabgeleiteten** `expected_match_key` entspricht; unter den
Bauvorschriften Z1–Z2′ (Protokoll §3, DDR M/M.2) ist die Kandidatenmenge einelementig, ein
gesonderter `localized`-Sonderfall für K1/`CYCLE` ist deshalb nicht nötig — es wird wie jede
andere Kategorie auf Modulebene gejoint.


### 3.4 Zwei vorregistrierte Eigenschaften von `strict`, die C6b abbilden muss

**Nachgetragen 26.08.2026 (D3a), Quelle: Protokoll §4 Nachträge Rev. 31.** Beide Punkte ändern
**keine** Metrikdefinition — §3 oben bleibt Zeichen für Zeichen gültig. Sie sind **Auflagen an
die Ausgabe**, nicht an die Rechnung.

**(1) `FORBIDDEN_SIGNATURE_TYPE` — vorhergesagter `strict`-Ausfall, deklariert.** Im
K2-Ruhezustand schreiben **57 von 63** `R-FRAMEWORK-1`-Findings den Typ als
`sqlalchemy.orm.Session` (die Manifestform) und **6** als `sqlalchemy.orm`, um das
Klassensegment gekürzt — reproduzierbar über alle drei Repetitionen, auf zwei
`*_view_models`-Zwillingen, auf **keinem** der vier Träger von I21–I24
(`d2_bericht_vormessungen.md` M0(c)). Verkürzt ein Träger in der Kampagne ebenso, ist `strict`
für diese Injektion **0** bei gleichzeitigem `localized`-**Treffer**.

- C6b **normalisiert nicht** und ändert den Manifestwert **nicht** (Decision Record O, H3b
  verworfen). Der Vergleich bleibt Zeichen für Zeichen nach §3.
- C6b muss diesen Fall aber **als solchen erkennbar ausgeben**: eine Injektion mit
  `localized` = Treffer **und** `strict` = 0, bei der die Abweichung **allein in Segment 4**
  liegt, ist in der Ausgabe als **Schreibweisenverfehlung** zu kennzeichnen (eigene Spalte oder
  Flag, nicht in einer Fussnote am Tabellenende). Grund: der Ausfallmodus ist **vor** der
  Messung deklariert; er darf im Ergebnis nicht wie ein gewöhnlicher Nichttreffer aussehen.
- Die Kennzeichnung ist **mechanisch** zu bilden (Segmente 1–3 gleich, Segment 4 ungleich),
  nicht per Hand vergeben.

**(2) `STRUCTURAL_PLACEMENT` — `strict` ist dort nicht unabhängig von `localized`.** In **54 von
54** `R-PLACE-1`-Findings des K2-Ruhezustands ist **Segment 4 zeichengleich mit Segment 3**: das
Modell nennt als fehlplatziertes Modul stets das geprüfte. Segment 3 setzt der Checker ohnehin
aus dem `ChangedFact` (§4.1), also trägt der Subjektwert dort **keine unabhängige Information**;
`strict` ist für diese Kategorie **nicht schärfer als „`localized` + Kategorie"**.

- Die Zelle wird **weiterhin berichtet** — es wird nichts zusammengelegt und nichts geschwärzt.
- Sie trägt in der Ergebnistabelle eine **Fussnote an der Zelle** mit genau dieser
  Einschränkung, damit die Tabelle nicht **zwei unabhängige Metriken suggeriert, wo eine
  steht**. Die Fussnote ist **Pflichtbestandteil** der Ausgabe (§8 Punkt 1).
- Abzugrenzen von der „n. b."-Festlegung für K4/`CYCLE` (§10.2, Protokoll §4 Nachtrag Rev. 30):
  dort ist `localized` **nicht berechenbar**, hier ist `strict` berechenbar, aber **nicht
  unabhängig**. Verschiedene Sachverhalte, verschiedene Kennzeichnung.

---

## 4. `localized` — mit der Lesekorrektur

**Definition je Pfad (Decision Record O §2, Protokoll §4):** ein injizierter Verstoß gilt als
erkannt, wenn mindestens ein Finding **(a)** im erwarteten Modul der erwarteten Komponente liegt
**und (b)** die für diese Konfiguration erwartete Kategorie trägt. `subjectKey`/`subject` wird
nicht verglichen, aber archiviert und qualitativ ausgewertet.

**Dedup:** Findings, die auf dasselbe `(component, module, category)` fallen, zählen als **ein**
TP und erzeugen **keine** FP. Ein Finding im erwarteten Modul mit **anderer** Kategorie ist kein
TP — es fällt in die gesonderte Klasse „richtige Stelle, falsche Kategorie" (§5).

**Erwartete Kategorie ist pfadabhängig:** die Rule-Engine kennt nur `layer-violation` und `cycle`
(`ruleEngine.ts:77,132`); die vier `FORBIDDEN_RELATION`-Szenarien tragen dort einheitlich
`layer-violation` (`rule_id` diskriminiert nicht: einheitlich `DERIVED:forbidden-edge`). Im
LLM-Pfad kommt `category` aus `rule.category` der Regeldatei (`llmChecker.ts:292`, dort
`rule.category`, entspricht dem in Protokoll referenzierten `llmChecker.ts:288`). Das Manifest
führt die erwartete Kategorie je Pfadtyp.

### 4.1 Die Lesekorrektur auf dem LLM-Pfad (Protokoll §4 Nachtrag Rev. 27)

**Gemessen:** `location.module` und `location.component` setzt der Checker **aus dem geprüften
`ChangedFact`** (`llmChecker.ts:282-285`: `location = { file: fact.path, module: fact.module,
component: fact.component, … }`), **nie aus der Modellantwort** — das Antwortschema hat für den
Ort kein eigenes Feld (`llmChecker.ts` `parseAndFinalize`, Aufruf von `buildMatchKey` erst nach
Konstruktion dieses `location`-Objekts). Ein K2/K3-Finding kann strukturell **nie** an einem
anderen Modul landen als dem geprüften.

**Konsequenz, als Lesekorrektur, keine Änderung der Metrikdefinition:**

- Auf dem LLM-Pfad (K2, K3) misst `localized` die **Meldequote auf der geprüften Datei**, nicht
  die Lokalisationsgenauigkeit des Modells.
- Für K1, K4 und K5 gilt das **nicht** — dort wählt das Werkzeug das gemeldete Modul selbst, und
  ein `localized`-Treffer setzt tatsächlich voraus, dass das Werkzeug die richtige Stelle
  gefunden hat.
- `strict` bleibt unterscheidungsfähig, weil dort zusätzlich Kategorie **und** `subject` in der
  vom Modell selbst gesetzten Form übereinstimmen müssen.

### 4.2 Pflichtfeld der Ausgabe: `localized` für K2/K3 nie ohne FP-Rate

Das ist eine **Eigenschaft der Harness**, keine redaktionelle Bitte (Decision Record O, Konsequenz
2; Protokoll §5 Amendment 11.08.; Protokoll §4 Nachtrag Rev. 27). Begründung: bei der gemessenen
Basisrate **49/52 = 0,9423** (K2, Median über drei Läufe, `c3b_k2_bericht_kontrolllauf.md` §4.2)
trifft nahezu jedes injizierte Modul ohnehin ein Finding, unabhängig davon, ob das Modell den
Verstoß **erkannt** hat.

**Spezifikation für C6/C6b:** die Harness darf `localized` für K2 oder K3 **nicht** als
eigenständige Zahl ausgeben, ohne im selben Ausgabeobjekt/derselben Tabellenzeile die zugehörige
Falsch-Positiv-Rate (§7) mitzuführen. Ein Ausgabeschema, das eine Trennung erlaubte (z. B.
`localized` in einer Tabelle, FP-Rate in einer anderen ohne Rückverweis), erfüllt die Vorschrift
nicht.

---

## 5. Begleitmeldungen und vorhergesagte Falschmeldungen — erschöpfende Liste

Alle folgenden Fälle: **getrennt geführt**, **kein False Positive**, in der Ausgabe **gesondert
ausgewiesen** (eigene Zeile/Spalte, nicht in Precision/Recall der Hauptzahl versteckt).

| # | Fall | Pfad | Fundstelle | Buchungsregel |
|---|---|---|---|---|
| 1 | `CYCLE`-Injektion (Modus `full`) erzeugt zusätzlich `layer-violation` auf derselben Kante | K1 | Protokoll §4 Am. 13.08.(a); DDR M.2 Festlegung 3 | Manifest-Eintrag `expected_co_findings`: Präfixersatz `cycle\|` → `layer-violation\|` auf dem handabgeleiteten `expected_match_key`, `location`/`subject` unverändert, `rule_id = DERIVED:forbidden-edge`. Vorregistriert (I13–I16 im Manifest bereits als `expected_co_findings`-Eintrag hinterlegt). |
| 2 | `FORBIDDEN_RELATION`-Injektion (Modus `diff`) erzeugt **keinen** `cycle`-Record | K1 | DDR M.2 Festlegung 2, bewiesen (`ruleEngine.ts:120`) | `expected_co_findings` ist für alle zwölf `FORBIDDEN_RELATION`-Injektionen **konstruktionsbedingt leer** — als **Nullerwartung** zu führen: ein `cycle`-Record hier wäre ein **Befund**, kein erwartetes Verhalten. Auch für I01–I03 (`LAYER_BACK_CALL`), obwohl deren injizierte Rückkante einen echten Komponentenzyklus `<k>_repository ↔ <k>_services` schließt (Protokoll §3 Nachtrag Rev. 29) — der Zyklus wirkt auf K1 **nicht**, weil `--rule-graph diff` einen Ein-Datei-Diff mit genau einem Adjazenz-Knoten erzeugt. |
| 3 | `LAYER_BACK_CALL`-Injektionen (I01–I03) werden von K4 **zweifach** gemeldet: `layers`-Contract (Schichtverletzung) **plus** `acyclic_siblings`-Contract (Geschwisterzyklus `services ↔ repository`) | K4 | Komponentenschnitt §6.2; Protokoll §4 Am. 13.08.(a)/(c), §3 Nachtrag Rev. 29 | Vorregistrierte K4-Doppelmeldung, **nicht wegkonfigurierbar** (kein `ancestor`, der `api`/`mappers` einschließt und `services`/`repository` ausschließt). `LAYER_SKIP_CALL` und `INDEPENDENCE` erzeugen sie **nicht**. |
| 4 | Adapterfassade `depot.core.adapters` (`R-PROTECT-1` im Scope) meldet im Clean-Control-Lauf | K2/K3 | Protokoll §5 Nachtrag Rev. 16 | Vorhergesagt, **nicht** unerwarteter FP; misst, ob das Modell die Erlaubnishälfte des `statement` liest. Gemessen K2: 3/3 Läufe; K3: 0/3 Läufe (`c3b_k3_bericht_kontrolllauf.md` §4.3). |
| 5 | Nicht-Träger-Portregel auf `orders_services` (`R-PORT-2`/`R-PORT-3`, beide im Scope jedes Moduls der Komponente) | K2/K3 | Protokoll §5 Nachtrag Rev. 18 | Vorhergesagt, **nicht** unerwarteter FP; nur `orders_services` betroffen (einzige Portträgerkomponente mit zwei Portregeln). Gemessen K2: erneut gefunden im unabhängigen Prompt-Abgleich (Rev. 27 Nachtrag); K3: 0/3 Läufe. |
| 6 | `CYCLE`-Injektionen: K2/K3 melden `FORBIDDEN_RELATION` am **richtigen Modul** (Kategorieverwechslung) | K2/K3 | Protokoll §4 Am. 13.08.(f) | **Kein** Treffer für `CYCLE` (Zelle K2/K3 = nein bleibt), **kein** False Positive (Stelle richtig, Kante existiert), in `localized` als eigene Klasse **„richtige Stelle, falsche Kategorie"**. Vorab benannt, damit sie nicht als Ermessensentscheidung erscheint. |
| 7 | `CYCLE_SIBLING`/`CYCLE_PARENT_CHILD`: K5 meldet die injizierte Rückkante als **nicht gelistete Kante**, nicht als Zyklus | K5 | Protokoll §3 Fußnote 7 (B39); `c2c_bericht_k5_konfiguration.md` §B5 | In `strict`: kein Treffer (Kategoriesegment weicht ab). In `localized`: Treffer auf der **Stelle**, Kategorie „nicht gelistete Kante" statt `CYCLE` → Klasse „richtige Stelle, falsche Kategorie" — **ohne neue Regel** gebucht (Präfix-/Kategorielogik identisch zu Fall 6). Matrixzelle: „teilweise". |

**Falsche Regel/Kategorie, richtige Stelle — allgemeine Regel (Protokoll §4 Hauptregel):**
`match_key` matcht nicht (Kategorie ist Schlüsselbestandteil) → zählt als **FP *und* FN**
gleichzeitig. Fälle 6 und 7 sind **Ausnahmen von dieser Allgemeinregel**, weil sie vorab benannt
und aus der FP/FN-Zählung herausgenommen wurden — die Harness muss sie **vor** der allgemeinen
FP/FN-Berechnung abfangen, sonst würden sie doppelt gezählt (einmal als vorregistrierte Klasse,
einmal als generisches „falsche Kategorie, richtige Stelle").

---

## 6. K4 und K5 haben keinen `match_key` — Vergleichsvorschrift

Import-linter und PyTestArch kennen den `match_key` nicht; ihre Textausgabe muss von der Harness
deterministisch auf ein Trefferkriterium abgebildet werden. Es gibt **zwei** getrennte
Vergleichsvorschriften, keine gemeinsame.

### 6.1 K4 — Mengenregel (nur für `CYCLE`, `acyclic_siblings`)

`acyclic_siblings` gibt eine **minimale Menge zu entfernender Kanten** aus, keine Zyklenpfade
(B9+ §6; Protokoll §4 Am. 12.08.). **Vergleichsvorschrift:** Treffer, wenn die im gebrochenen
Contract genannte Kantenmenge die **injizierte Kante enthält**. Bei einem Zyklus der Länge 2
(alle 4 `CYCLE`-Injektionen dieser Kampagne, Bauvorschrift Z1) enthält die minimale Menge **genau
eine** der beiden Kanten der injizierten Rückkante — die Vorschrift ist damit äquivalent zu:
Treffer, wenn die genannte Kante (`- .<Quellpaket relativ zum ancestor> -> .<Zielpaket relativ
zum ancestor> (N import)`) dem package-relativen Bild der injizierten Kante entspricht.

**Für alle übrigen K4-Fundformen** (`layers`-Contract `BROKEN` mit Detailzeile, `forbidden`,
`protected`, `independence`) gilt **kein** Mengenvergleich, sondern ein direkter Abgleich der in
der Detailzeile genannten Modulpfade (`<Modul-A> -> <Modul-B> (l.<N>)` bzw. die
`exhaustive`-Zeile mit vollem Modulpfad) gegen `expected_edge_boundary`/`carrier_module` des
Manifest-Eintrags.

**Abgleich Paketebene ↔ Injektion auf Modulebene, präzise:** die `ancestor`-Einstellung des
jeweiligen `acyclic_siblings`-Contracts (im Messmanifest je Contract festgehalten, Protokoll §1
Am. 13.08.) legt fest, **relativ zu welchem Wurzelpfad** die Kante notiert ist (führender Punkt =
direktes Kind des `ancestor`). Die Harness muss:

1. den `ancestor` des Contracts nachschlagen (Messmanifest, nicht der Textblock selbst — der
   Textblock nennt ihn nur in der Kopfzeile `No cycles are allowed in <ancestor-oder-Unterpaket>.`),
2. die relative Kante `.<a> -> .<b>` zu vollen **Komponentennamen** auflösen
   (`<Kopfzeilen-Präfix>.<a>` bzw. `.<b>`),
3. gegen das **Komponentenpaar** aus `expected_edge_boundary` des Manifests vergleichen (nicht
   gegen den Modulnamen — der Block trägt keinen).

Ein gebrochener Contract kann **mehrere** `No cycles are allowed in …`-Blöcke enthalten
(§1.4) — die Mengenregel ist **je Block** anzuwenden, dessen Kopfzeile das betroffene Paket
nennt, nicht auf den ganzen Contract in einem Schritt.

### 6.2 K5 — Regelname

**Vergleichsvorschrift:** Treffer, wenn eine `FAILED`-Zeile mit der Test-ID
`test_component_imports_only_whitelisted_modules[<erwartete Komponente>]` auftritt **und** die
zugehörige `AssertionError`-Nachricht das erwartete Träger- oder Zielmodul wörtlich als
Zeichenkette enthält (`"<Modul>" imports "<Modul>".`). Für die vier `MISSING_PORT_REFERENCE`-
Einzelregeln (`are_named(<Trägermodul>)`) ist ~~der Regelname direkt der Modulname im Parameter der
Test-ID~~; ein Treffer erfordert keinen zusätzlichen Textabgleich, weil die Regel modulscharf
gebunden ist.

> **Korrektur 27.08.2026 (C6b-2b) — DER PARAMETER DER TEST-ID IST DIE `rule_id`, NICHT DER
> MODULNAME.** Begründung: `data/soll/test_architecture.py:309-310`, wörtlich:
>
> ```python
> @pytest.mark.parametrize("rule_id", sorted(PORT_RULES))
> def test_carrier_references_the_core_ports(rule_id: str) -> None:
> ```
>
> Die Test-ID lautet damit `test_carrier_references_the_core_ports[R-PORT-1]`, **nicht**
> `…[depot.identity.services.token_service]`. Der **Modulname erscheint allein in der
> `AssertionError`-Nachricht** (`"<Trägermodul>" does not import "depot.core.ports".`).
> Zu unterscheiden ist die Portregel damit auch vom Erlaubnislistentest: dort heisst die
> Funktion `test_component_imports_only_whitelisted_modules` und der Parameter ist die
> **Komponente**.
>
> **Der Schluss der Passage bleibt unverändert richtig.** Ein Treffer erfordert keinen
> zusätzlichen Textabgleich, weil jede der vier Regeln auf **genau ein** Trägermodul
> (`are_named(<Trägermodul>)`) gebunden ist — nur trägt die Bindung über die **`rule_id`** und
> nicht über den Parameter. Die Harness vergleicht den Parameter gegen `rule_id` des
> Manifest-Eintrags und das in der Nachricht genannte Modul gegen `carrier_module`.
> **Keine Metrikänderung, keine Matrixzelle bewegt sich.**

**`ERROR` (`NetworkXError`) ist kein Nicht-Treffer, sondern ein separat zu führender
Werkzeugabbruch** (§1.5) — er darf in keiner Zählung als FN erscheinen, weil für die betroffene
Regel **keine Messung** stattgefunden hat, sondern als eigene Kategorie „Regel nicht ausgewertet".

---

## 7. Aggregation, Falsch-Positiv-Rate, Ausschlüsse

### 7.1 Median und Streuung

Median über drei Läufe ist die Headline-Zahl für jede LLM-Konfiguration (K2, K3); **die Streuung
wird IMMER mitgeführt**, nie eine nackte Median-Zahl (Protokoll §5). Bei K3 ist die Streuung ein
**größerer Anteil des Werts** als bei K2: gemessen ist die Modul-mit-Finding-Reihe **2/1/0**
(Median 1, Spannweite 0–2) gegenüber K2, wo dieselbe Kennzahl über alle drei Läufe **konstant**
blieb (`c3b_k3_bericht_kontrolllauf.md` §4.2, `c3b_k2_bericht_kontrolllauf.md` §4.2). **Konsequenz
für das Ausgabeschema:** eine Darstellung, die nur den Medianwert zeigt (z. B. eine einzelne
Zahl ohne Intervall-/Min-Max-Spalte), kann bei K3 den Wert **1/52 = 0,0192** nicht von einem
Bereich **0/52 … 2/52** unterscheiden — die Ausgabe muss Median und Spannweite **in derselben
Zelle oder Zeile** führen, sonst ist der K3-Wert falsch lesbar.

### 7.2 Falsch-Positiv-Rate

**Nenner: 52** (Protokoll §5 Nachtrag Rev. 17) — die 52 inhaltstragenden Module des
Clean-Control-Sets; ausgeschlossen sind **leere** `__init__.py` (21 von 23 Paketmodulen), **nicht**
Paketmodule als Gattung. Die beiden inhaltstragenden Paketmodule (`depot.core.adapters`,
`depot.orders.services`) zählen zum Nenner **mit**.

**Zähler:** Zahl der Kontrollmodule mit ≥ 1 Finding im jeweiligen Lauf (Modul-Ebene, nicht
Finding-Ebene — „Findings gesamt" wird zusätzlich, aber getrennt geführt, s. die Tabellen in
`c3b_k2/k3_bericht_kontrolllauf.md` §4.2).

~~Die beiden vorregistrierten Meldungen (§5, Fälle 4 und 5 oben) sind **aus dem Zähler der Headline-Rate herauszurechnen und separat auszuweisen** — sie sind vorhergesagt, keine unerwarteten FP, aber sie bleiben reale Findings auf dem Clean-Control-Set und müssen in einer eigenen Zeile sichtbar bleiben.~~
(überholt am 28.08.2026 durch C6c, Protokoll Rev. 37 — die Formulierung war
zweideutig: „herausrechnen und separat ausweisen" gegen die Ergebniszeile des
K2-Berichts, die sie „getrennt **darin** enthalten" führt. Entschieden ist der
Verbleib im Zähler; der Wortlaut steht unten.)

**ENTSCHIEDEN am 28.08.2026 (C6c, Protokoll Rev. 37): die beiden vorregistrierten
Meldungen (§5, Fälle 4 und 5 oben) BLEIBEN IM ZÄHLER der Headline-Rate und werden
GETRENNT AUSGEWIESEN — sie werden NICHT herausgerechnet.** Die Headline-Rate ist die
Zahl der Kontrollmodule mit ≥ 1 Finding, **alle Findings gezählt**. Die vorregistrierten
Meldungen stehen zusätzlich in einer eigenen Zeile (T3.1), damit sichtbar bleibt, welcher
Teil der Rate vorhergesagt war; die zweite Lesart — dieselbe Zahl **ohne** sie — wird
**mitgeführt**, aber sie ist nicht die Headline.

**Drei Gründe, jeder für sich tragend:**

1. **Die Herausrechnung verbesserte die gemessene Grösse.** Sie senkt die
   K2-Falsch-Positiv-Rate, und zwar zugunsten des Prüfgegenstandes. Eine Lesart, die den
   gemessenen Wert verbessert und **gewählt** ist statt von der Messung erzwungen, ist
   von einer an den Daten gewählten Festlegung nachträglich nicht mehr zu unterscheiden
   — dieselbe Begründung, mit der §0.1 Punkt 4 des Protokolls Metrikänderungen nach
   Messbeginn sperrt.
2. **Sie widerspräche der Auflage aus §4.2.** `localized` darf für K2/K3 **nie ohne die
   vollständige FP-Rate** berichtet werden (Protokoll §5 Amendment 11.08.). Eine
   Headline-Rate, aus der zwei reale Meldungen herausgerechnet sind, ist nicht die
   vollständige FP-Rate; die Auflage wäre dem Buchstaben nach erfüllt und dem Sinn nach
   verfehlt.
3. **Eine vorhergesagte Meldung ist auf sauberem Code trotzdem eine Meldung.**
   Vorhersagbarkeit ist ein **Zusatz**, kein **Abzug**: sie sagt, dass wir die Meldung
   erklären können, nicht dass sie nicht stattgefunden hätte. Ein Leser des
   Kontrollbestands sieht ein Modul mit einem Finding; genau das zählt die Rate.

**Der Zeitpunkt, ausdrücklich:** Auf dem Kontrollbestand ergeben **beide Lesarten
denselben Wert 49** — beide betroffenen Module tragen ausserdem andere Findings
(`c6b_bericht_harness.md` §4.5). Im Harness-Fixture fallen sie auseinander, **3/6 gegen
4/6**. Die Entscheidung fällt damit **vor ihrer ersten wirksamen Anwendung**: sie
verschiebt keine bereits berichtete Zahl, und sie ist an keinem Kampagnenergebnis
gewählt worden — der Auswertungslauf über `data/campaign/k*` hat zum Zeitpunkt dieser
Entscheidung nicht stattgefunden.

**Nur inhaltstragende Module gehen in die Headline-Rate ein.** Laufen leere Init-Module aus
anderem Grund mit, ist ihre FP-Rate **getrennt** auszuweisen, nie in die Gesamtrate eingerechnet
(Protokoll §5, Amendment 13.08. und Nachtrag Rev. 17).

### 7.3 Dedup nach Decision Record O

- **`strict`:** keine Dedup. Mehrfache Findings auf denselben `match_key` sind bereits durch die
  §3.2-Regel abgedeckt (ein TP, jedes weitere ein FP).
- **`localized`:** Dedup auf `(component, module, category)` — mehrere Findings darauf zählen als
  **ein** TP, erzeugen **keine** FP.
- Für die **Falsch-Positiv-Rate des Clean-Control-Sets** gilt die `localized`-Dedup-Logik
  sinngemäß auf Modulebene: „Modul mit ≥ 1 Finding" ist bereits ein dedupliziertes Kriterium
  (mehrere Findings auf demselben Kontrollmodul erhöhen nicht die Modulzahl im Zähler), die
  zusätzliche Zeile „Findings (LLM) gesamt" bleibt undedupliziert und ist eine reine
  Zusatzinformation, kein Bestandteil der Headline-FP-Rate.

### 7.4 Ausschlussregeln

- **Ein Lauf mit nicht leerem `invalid_reasons` ist ungültig** (`run_footer.invalid_reasons`
  bzw. `validity.invalid_reasons` im `--json-out`) und wird von der Auswertung ausgeschlossen,
  nicht „als 0 Findings" gezählt.
- **Eine unbekannte `rule_id` invalidiert den ganzen Versuch**, nicht nur das betroffene Finding
  (`llmChecker.ts:277-280`, `parseAndFinalize`: `unknown or missing rule_id "…"` → Parse-Fehler
  → Retry → bei Erschöpfung `invalid_final_response`; belegt in `b1_bericht_matchkey.md` Abschnitt
  D1: „Eine unbekannte `rule_id` macht zudem den ganzen Versuch invalide … ein falscher
  Regelbezug verwirft auch die korrekten Findings derselben Antwort"). Ein einziges Finding mit
  Phantom-`rule_id` in einer Antwort mit sonst korrekten Findings kostet also **alle** Findings
  dieses Calls.
- **Der Exit-Code ist KEIN Gültigkeitskriterium** (Protokoll §6 Nachtrag Rev. 26; gemessen: Exit 0
  bei 0 Findings, Exit 1 bei ≥ 1 Finding — Normalverhalten, kein Fehlschlag). Gültigkeit bemisst
  sich an `invalid_reasons`, `calls_invalid`, `calls_transport_failed` und den beiden folgenden
  Zählregeln.
- **Die Zählregeln tragen den Wiederholungsfaktor** (Protokoll §6 Nachtrag Rev. 26,
  `run.ts:169-206`, `CallTally.total`):
  - Injektionslauf: `changed_files_count == 1 ∧ calls_total == 1 * runs`
  - Kontrolllauf: `calls_total == control_files_count * runs`
  - Für den Vollbild-Lauf gilt **keine** der beiden Regeln (Protokoll §6 Am. 12.08.).
  - **Präzisierung 28.08.2026 (C6c-a):** die Zählregel `calls_total == 1 * runs` gilt für
    **K2/K3**; für **K1** verlangt der ausgeführte Test `calls_total == 0` — der
    deterministische Pfad ruft **kein** Modell auf (`tools/postrun_check.py`,
    Injektionszweig, seit §6 Nachtrag Rev. 24). Das Tabellenskelett führt in der Spalte
    *Erwartet* von T7.2 „K1: 1"; die Abweichung ist in der Ausgabe **ausgewiesen** und
    **nicht** angeglichen. Gemessen ist in allen 32 K1-Invocationen `calls_total = 0`.

**Lebende Dokumente — planmäßig ungehasht (nachgetragen 28.08.2026, C6c-a).** Sieben Dateien
in den gehashten Beständen stehen in **keinem** `SHA256SUMS` und **sollen** dort nicht
stehen: `data/soll/MANIFEST.md`, `data/campaign/MANIFEST.md`, `data/campaign/README.md`,
`data/campaign/journal.jsonl`, `data/campaign/control/journal.jsonl`,
`data/campaign/k2/MANIFEST.md` und `data/campaign/k3/MANIFEST.md`. **`journal.jsonl` ist
append-only und wächst planmäßig; die `MANIFEST.md` sind fortzuschreibende Dokumente.** Ein
Hash wäre für sie das falsche Instrument — er risse bei **jeder legitimen** Fortschreibung
und erzöge dazu, ihn nachzuziehen, was den Detektor zerstört. **Integrität liefert die
Commit-Historie**; der Schnappschuss-Hash im Manifest bleibt, wo er steht. **Keine davon ist
ein Laufartefakt**, und seit §1.8 ist keine davon mehr **Quelle** eines T-Wertes. Die Liste
steht **namentlich** in `tools/check_doc_invariants.py` (`KNOWN_UNLISTED`) und wird bei
jedem Lauf als **entschiedene Ausnahme** gemeldet, nicht als Fehlschlag; **eine achte
ungelistete Datei ist ein Fehlschlag**.


### 7.5 Vorbelastung je Injektion und paarweise Differenz

**Nachgetragen 26.08.2026 (D3a), Quelle: Protokoll §5 Nachträge Rev. 31.** Beides tritt
**neben** die Kennzahlen aus §7.1–§7.4, nie an ihre Stelle; Precision, Recall und F1 werden
unverändert gebildet, und es wird **nichts subtrahiert**.

**(3) Ruhezustandszahl je Injektion — berichtspflichtig.** Für **15 der 32** Injektionen tritt
der erwartete `match_key` bereits im K2-Ruhezustand als tatsächlich gebildeter Schlüssel auf
(I07–I09, I17–I24, I29–I32): drei der vier semantischen Familien vollständig — je 4/4 —,
`STRUCTURAL_PLACEMENT` dagegen 0/4, weil die Injektion das Modul erst verschiebt. Zwei Lagen
sind für die Auswertung besonders:

- **I17–I20 (`ABSENCE_REQUIRED`):** die Injektion **entfernt** einen Portbezug, die saubere
  Baseline **erfüllt** die Regel — und das Modell meldet den Verstoss dort trotzdem, mit
  **exakt dem erwarteten Schlüssel**, in jeder der drei Repetitionen.
- **I25–I27 (`STRUCTURAL_PLACEMENT`):** die Trägermodule ziehen im Ruhezustand je **3**
  Meldungen derselben Kategorie; bei **I28 nie**.

**Auflage an C6b:** zu **jedem** Kampagnenergebnis wird die **Ruhezustandszahl desselben Moduls
in derselben Kategorie** aus C3b mitgeführt — konfigurationsgleich aus `data/c3b-k2/` bzw.
`data/c3b-k3/` (§1.7). **Ein `strict`-Treffer, der die Ruhezustandsrate nicht übersteigt, wird
nicht als Erkennungsnachweis geführt** und ist in der Ausgabe entsprechend zu kennzeichnen. Die
Zahl steht **in derselben Zeile** wie das Kampagnenergebnis; ein Ausgabeschema, das sie in eine
andere Tabelle ohne Rückverweis auslagert, erfüllt die Vorschrift nicht — dieselbe Härte wie
bei `localized` und der FP-Rate in §4.2.

> **Nachtrag 28.08.2026 (C11b, Protokoll Rev. 40) — DIE AGGREGATIONSSTUFE DIESES VERGLEICHS
> IST FESTGELEGT: die EXISTENZSTUFE.** Der Satz oben bleibt **wörtlich stehen**; präzisiert
> ist allein, **wie seine beiden Seiten gebildet werden**. Die Fassung von C6b hat die
> Kampagnenseite über `strict` (**Existenz** über die drei Repetitionen, §3) und die
> Ruhezustandsseite über einen **Median** gebildet — zwei verschiedene Stufen in einer
> Bedingung, festgestellt in `c11a_bericht_diagnose.md` §3.5.
>
> **Bildungsvorschrift, verbindlich:**
>
> ```
> kein-EN = "ja"    wenn strict = 1  UND  Ruhe-Existenz = 1
>         = "nein"  wenn strict = 1  UND  Ruhe-Existenz = 0
>         = leer    wenn strict = 0                     (dritter Zustand, unverändert)
>
> Ruhe-Existenz = 1, wenn die Zählgrösse dieses Abschnitts — Findings desselben Moduls in
>                    derselben Kategorie — in MINDESTENS EINEM der drei C3b-Läufe > 0 ist.
> ```
>
> **Warum die Existenzstufe.** Der Wortlaut macht **den `strict`-Treffer zum Subjekt**;
> `strict` ist nach §3 ein Existenzquantor über die Repetitionen und als **Metrikdefinition**
> nach Protokoll §0.1 Punkt 2 gesperrt. Die Stufe des Subjekts ist damit die zu wählende, und
> die Ruhezustandsseite folgt ihr — nicht umgekehrt.
>
> **Nicht berührt:** die **paarweise Differenz** unter (4). Ihre Spalten `Ruhe`, `Kampagne`
> und `Δ` bleiben auf dem **Median**; sie sind eine eigenständig vorregistrierte Grösse mit
> eigener Bildungsvorschrift, ihre beiden Seiten sind bereits gleich aggregiert, und kein-EN
> liest sie seit diesem Nachtrag **nicht mehr**.
>
> **Ebenfalls nicht berührt — und hiermit als Lesevorbehalt benannt:** der **Filter** beider
> Seiten bleibt verschieden. `strict` filtert über den vierteiligen `match_key` (§3), die
> Ruhezustandszahl über **Trägermodul und Kategorie** (dieser Abschnitt). Beide Filter sind
> vorregistriert; dieser Nachtrag legt die **Aggregationsstufe** fest, nicht den Filter.

Diese Auflage ist die **injektionsscharfe Fassung** von §4.2: dort wirkt die Kontrolle **global**
über das Clean-Control-Set, hier **je Injektion**, weil die Vorbelastung nachweislich ungleich
verteilt ist (4/4 in einer Familie, 0/4 in der nächsten) und eine globale FP-Rate genau diese
Ungleichheit wegmittelt.

**(4) Paarweise Differenz je Injektion — eigene Spalte.** Je Injektion und je Konfiguration
wird die **Differenz zwischen injiziertem Zustand und Ruhezustand desselben Moduls** berichtet.

- **Zählgrösse:** Findings desselben Moduls in derselben Kategorie, wie unter (3).
- **Ruhezustandsseite:** konfigurationsgleich aus `data/c3b-k2/` bzw. `data/c3b-k3/`.
- **Gleiche Repetitionszahl auf beiden Seiten** — beide Bestände tragen drei Läufe je Modul;
  wird auf einer Seite anders aggregiert als auf der anderen, ist die Differenz eine Zahl ohne
  Gegenstand.
- **Für K1, K4 und K5** ist die Differenz mangels LLM-Streuung trivial, aus Symmetrie der
  Tabelle aber **ebenfalls auszuweisen**.
- **Deskriptiv, ohne inferenzstatistische Deutung:** kein Test, kein Konfidenzintervall, keine
  Signifikanz; Berichtsform **Grössenordnungen** (§7.1, Protokoll §5 Amendment 12.08.).
- **Bindend: die Differenz wird auch berichtet, wenn sie null oder negativ ist.** C6b darf
  solche Zeilen **nicht** unterdrücken, nicht auf null runden und nicht durch die Aggregatzahl
  ersetzen.

**(5) Die drei Repetitionswerte einzeln — eigene Spalte, rein deskriptiv.**
*Nachgetragen 28.08.2026 (C11b, Protokoll Rev. 40).*

Je Injektion und je Konfiguration (K2, K3) trägt T4 eine Spalte **Läufe (Ruhe · Kampagne)**, in
der die Zählgrösse dieses Abschnitts für **jede der drei Repetitionen einzeln** steht — Form
`[0,0,0] · [0,0,1]`, links der Ruhezustand, rechts die Kampagne, Reihenfolge nach `run_index`.

- **Rein deskriptiv.** Keine Wertung, **keine** Aggregation, **keine** neue Metrik, **kein**
  Eingang in Precision, Recall, F1, in die paarweise Differenz oder in kein-EN. Die Spalte
  **zeigt** die Zahlen, aus denen die anderen Spalten gebildet werden; sie bildet selbst nichts.
- **Zweck.** Ein Median `0` über `[0,0,1]` und ein Median `0` über `[0,0,0]` sind als gedruckte
  Zelle **nicht unterscheidbar** — und sie tragen unter (3) verschiedene Buchungen. Die Spalte
  macht die **Aggregationsstufe an der Tabelle lesbar**, statt sie dem Leser zu unterschlagen.
- **Bei `n. e.`** trägt die Spalte `n. e.` wie die übrigen Zellen derselben Zeile; sie ist
  **nie** ein leerer String und **nie** `[]`.

**(6) kein-EN wird NICHT nach Ursache aufgespalten — ausdrücklich abgelehnt.**
*Registriert 28.08.2026 (C11b, Protokoll Rev. 40).*

`c11a_bericht_diagnose.md` §3.6 hat festgestellt, dass die kein-EN-Fälle **nicht durchgehend
denselben mechanischen Auslöser** haben. Eine zusätzliche Spalte, die kein-EN nach dieser Ursache
in „Rauschen" und „Instabilität" **trennte**, **wird nicht eingeführt**: sie wäre eine **neue,
nach Sicht auf die Daten gebildete Klassifikation** — die Klassen existierten vor dem ersten
Auswertungslauf nicht, und ihre Grenze läge an genau den Zeilen, die sie sortieren soll
(Protokoll §0.1 Punkt 4). Der Ursachenunterschied gehört in die **Prosa von Kapitel 7**, belegt
aus der Läufespalte unter (5) — als **Beschreibung**, nicht als **Buchung**.

---

## 8. Was die Ausgabe enthalten muss — Schema für Kapitel 7

Die folgenden Tabellen/Objekte sind als **Pflichtbestandteile** der Harness-Ausgabe zu
spezifizieren; die konkrete Serialisierung (CSV, JSON, Markdown-Tabelle) ist C6b überlassen.

1. **Precision/Recall/F1-Tabelle**, je Konfiguration (K1–K5) × Kategorie (die sechs Ebene-1-Typen
   plus Gesamt) × Metrik (`strict`, `localized`), ~~mit Median **und** Spannweite für K2/K3
   (§7.1)~~ — **ERLEDIGT, gegenstandslos (Nachtrag unten, 28.08.2026, C11c, Protokoll Rev. 42)**.
   `localized` für K2/K3 trägt in jeder Zelle einen Verweis auf oder eine benachbarte Spalte mit
   der FP-Rate desselben Laufs (§4.2 — Pflichtfeld, kein optionaler Zusatz).

   > **Nachtrag 28.08.2026 (C11c, Protokoll Rev. 42) — DIE FORDERUNG NACH MEDIAN UND
   > SPANNWEITE IST FÜR DIESE TABELLE GEGENSTANDSLOS UND DAMIT ERLEDIGT; sie wird NICHT
   > abgewiesen.** Median und Spannweite setzen eine **laufweise** Grösse voraus. Precision,
   > Recall und F1 dieser Tabelle stehen auf `strict` und `localized`; `strict` ist nach
   > **§3** ein **Existenzquantor über die Repetitionen** und hat konstruktiv **keine
   > Verteilung über Läufe**. Eine laufweise Fassung wäre keine zweite Auslesart derselben
   > Metrik, sondern eine **neue Metrikdefinition** — und die sind seit dem ersten
   > Kampagnenlauf gesperrt (Protokoll §0.1 Punkt 2).
   >
   > **Die Laufstreuung wird stattdessen dort ausgewiesen, wo sie laufweise vorliegt:** in der
   > mit **Rev. 40** eingeführten T4-Spalte **Läufe (Ruhe · Kampagne)** — **je Repetition
   > einzeln**, Form `[0,0,1]`, §7.5 (5). Das ist feinkörniger als ein Median, nicht gröber;
   > die Anforderung hat damit keinen Gegenstand mehr.
   >
   > **Nachtrag 28.08.2026 (C14):** Die **gedruckte Ausgabe** führte an T5 weiterhin den
   > Vermerk „LÜCKE, benannt und nicht gefüllt“ — überholt seit Rev. 42. Der Text der
   > Harness ist mit **R14** auf diese Erledigung nachgezogen; **keine Zelle bewegt sich**.
   >
   > **Nicht berührt:** Punkt 2 dieser Liste. Die **Falsch-Positiv-Raten-Tabelle** führt Median
   > **und** Spannweite über drei Läufe für K2/K3 **unverändert** weiter — dort ist die
   > Headline-Rate eine je Lauf gebildete Grösse (§7.1), und dieser Nachtrag rührt nicht daran.
   > Ebenso unverändert: `strict`, `localized`, Precision, Recall, F1, Median, Spannweite und
   > die vier Marker. **Es wird nichts festgelegt, was nicht schon galt** — festgestellt ist
   > allein, dass eine Anforderung aus der Konstruktion der Metrik heraus leerläuft.
2. **Falsch-Positiv-Raten-Tabelle**, je Konfiguration: Headline-Rate (Nenner 52, Median +
   Spannweite über drei Läufe für K2/K3), plus getrennte Zeilen für die beiden vorregistrierten
   Meldungen (§5, Fälle 4/5) und für ggf. mitlaufende leere Init-Module (§7.2).
3. **Erwartungsmatrix Soll gegen Ist**, Zelle für Zelle (zehn Szenarien × fünf Konfigurationen),
   mit **Kennzeichnung jeder Abweichung** von der vorregistrierten Matrix (Protokoll §3, zuletzt
   Nachtrag Rev. 22/28) — Übereinstimmung wird nicht extra vermerkt, jede Abweichung ist ein
   eigener Eintrag mit Fundstellenverweis auf den betroffenen Einzelfall.
4. **Liste der Begleitmeldungen**, alle sieben Fälle aus §5, je mit Fundort (Injektions-ID,
   Konfiguration), gemessener Häufigkeit (z. B. „3/3 Läufe" für Fall 4 bei K2) und Verweis auf die
   vorregistrierende Quelle.
5. **Liste der ungültigen Läufe**, mit Grund (§7.4), betroffener Konfiguration und Injektions-ID
   bzw. Kontrolldatei, und ob eine Wiederholung erfolgte.
6. **Wanduhrzeit je Injektionslauf und Konfiguration**, als eigene Kennzahl (nicht nur als
   Nebenspalte der Kostenrechnung). Quelle und Granularität sind konfigurationsabhängig — s.
   Abschnitt 10, offener Punkt zur Feldwahl. Diese Spalte trägt die Aussage zur
   Pipeline-Tauglichkeit („ein Injektionslauf ist genau der Fall ‚ein Push ändert eine Datei'");
   ohne sie ist diese Aussage nicht belegbar.
7. **Vorbelastungs- und Differenzspalte je Injektion** (§7.5, nachgetragen 26.08.2026 (D3a),
   Protokoll §5 Nachträge Rev. 31): je Injektion × Konfiguration die **Ruhezustandszahl
   desselben Moduls in derselben Kategorie** aus C3b **und** die **paarweise Differenz**
   injizierter Zustand ↔ Ruhezustand — beide **in derselben Zeile** wie das Kampagnenergebnis,
   nicht in einer separaten Tabelle ohne Rückverweis. Ein `strict`-Treffer, der die
   Ruhezustandsrate nicht übersteigt, ist als **kein Erkennungsnachweis** gekennzeichnet. Die
   Differenz erscheint **auch dann**, wenn sie null oder negativ ist.
8. **Kennzeichnung der Schreibweisenverfehlung** (§3.4 (1)): jede Injektion mit
   `localized` = Treffer **und** `strict` = 0, deren Abweichung **allein in Segment 4** liegt,
   trägt ein mechanisch gebildetes Flag. Der Fall ist als **vorhergesagter `strict`-Ausfall**
   vorregistriert (Protokoll §4 Nachtrag Rev. 31) und darf im Ergebnis nicht wie ein
   gewöhnlicher Nichttreffer aussehen. **Keine Normalisierung, keine Manifeständerung.**
9. **Blindheit bis zum Auswertungslauf, präzisiert (28.08.2026, C6c-a).** Solange die
   Kampagne nicht ausgewertet wird, liest die Harness aus `data/campaign/` **ausschliesslich**
   die Metadaten einer **positiven Erlaubnisliste**: die **Laufmanifeste** unter
   `manifests/`, `journal.jsonl`, `MANIFEST.md`, `README.md` und `SHA256SUMS`. **Die
   Laufmanifeste sind ausdrücklich erlaubt** — sie tragen Verdikte, Zähler und Provenienz,
   **keine Funde**. Gesperrt bleiben die Funde: `--json-out`-Artefakte, Run-Log-Records und
   der Rohtext (stdout/stderr) der Kampagne. Die Harness **auditiert das an sich selbst**:
   sie zeichnet jeden Dateizugriff auf und bricht mit **Exit 3** ab, wenn ein Pfad unter der
   Kampagnenwurzel geöffnet wurde, der nicht auf der Erlaubnisliste steht — `control/`
   eingeschlossen. Die Liste ist **positiv** formuliert, damit eine neue Artefaktsorte unter
   `data/campaign/` **standardmässig** als Verletzung gilt und nicht durch Übersehen
   durchfällt.
10. **Overlap-Tabelle T10** (nachgetragen 28.08.2026, C14). Protokoll §8 verlangt für **UF3**
   eine „**Overlap-Analyse K1/K4/K5 vs. K2/K3**“; die registrierte Ausgabe enthielt keine
   (festgestellt in `c11d_bericht_befund08_grundlagen.md` §B5). Sie wird als **T10**
   nachgetragen, **aus den bereits gerechneten Trefferzellen** — **keine neue Metrik, keine
   neue Schwelle, keine neue Vergleichsvorschrift**.

   **(a) Zwei Teiltabellen, getrennt nach Metrik:** **T10a** = `localized`, **T10b** =
   `strict`. Die beiden Metriken werden **nicht** gemischt.

   **(b) Zwei Zeilengruppen je Teiltabelle, K2 und K3 GETRENNT:** „K2 gegen die Baselines“
   und „K3 gegen die Baselines“. **K2 und K3 werden nicht zu „dem LLM-Pfad“ vereinigt** —
   dieselbe Auflage wie in T2 und T5.

   **(c) Die Baselineseite IST eine Vereinigung und wird als solche benannt:** K1 ∪ K4 ∪ K5.
   Zulässig, weil die Arbeit die drei als **Baseline-Menge** führt; die Zelle nennt
   ausserdem, **welche** Konfigurationen den Zustand tragen, damit die Vereinigung nicht
   verdeckt, aus wem sie besteht.

   **(d) Zustand je Seite, in dieser bindenden Reihenfolge gebildet** — je Zelle zuerst:
   `n. b.` → nicht bildbar · `n. e.` → nicht erhoben · ` — ` → **nicht ausdrückbar** ·
   vorregistrierte Sonderklasse **T9 Fall 6/7** → Sonderklasse · Wert 1 → **Treffer** ·
   Wert 0 → **Verfehlung**. **Die Reihenfolge ist die von T5 Auflage (2)** und wird hier
   nicht neu gesetzt; sie entscheidet **eine** Konstellation, und die ist zu benennen:
   eine ` — `-Zelle, die zugleich eine vorregistrierte Sonderklasse trägt — **K2/`CYCLE`
   und K3/`CYCLE`, wo jeder Fund T9 Fall 6 ist** —, bleibt **nicht ausdrückbar**. ` — ` ist
   eine Aussage über das **Werkzeug**, die Sonderklasse eine über einen **Fund**; die
   zweite kann die erste nicht überschreiben (so auch `score_rows` in T5). Daraus der
   Seitenzustand: **eine** Trefferzelle macht die Seite zum **Treffer**; sonst macht
   **eine** Verfehlungszelle sie zur **Verfehlung**; sonst ist die Seite **nicht
   ausdrückbar**, wenn **alle** ihre Zellen es sind; sonst **nicht beurteilbar**.

   **(e) Vier Zustände je Injektion:** **nur Baseline** · **nur K2** bzw. **nur K3** ·
   **beide** · **keiner**.

   **(f) MARKERDISZIPLIN — der kritische Punkt.** Eine Injektion, die eine Seite nach **T8**
   nicht **ausdrücken** kann, ist dort **nicht verfehlt**. Solche Fälle stehen in einer
   **eigenen Klasse** („für diese Seite nicht ausdrückbar“, je Seite benannt) und werden
   **nie** in „nur die andere Seite“ umgedeutet — sonst würde **Ausdrucksmächtigkeit zu
   Leistung**, und genau das verbietet das G2-Reframing (**B17**, Skelett §1.1). Ebenso gehen
   `n. b.`, `n. e.` und die vorregistrierten Sonderklassen **T9 Fall 6 und Fall 7 weder als
   Treffer noch als Verfehlung** ein; sie stehen in der Klasse **nicht beurteilbar**.

   **(g) Aggregatzeile je Zeilengruppe mit ausgewiesenem Nenner**, wie in **T5**: der Nenner
   ist die Zahl der Injektionen in den **vier** Zuständen aus (e); die ausgeschlossenen
   Klassen aus (f) stehen **daneben, nie darin**, und werden einzeln beziffert.

   **(h) Zuordnung nach Skelett §0.3:** T10 ist eine **gerechnete** Tabelle. Sie trägt
   **keinen** vorgegebenen Wert — weder Vorhersage (A) noch Aufschrieb (B) — und erzeugt
   deshalb **keine** Abweichungszeile.


---

## 9. Was nicht zu tun ist

- Kein Code für C6/C6b in diesem Auftrag.
- Keine Änderung an Protokoll, Manifest, Soll-Modell oder Regeldatei — dieser Auftrag **liest**
  sie, verändert sie nicht (`git status --porcelain` in `tritongraph` vor und nach diesem Auftrag
  leer, keine Injektions-, Soll- oder Regeldatei in `masterarbeit` verändert).
- Kein Werkzeuglauf, kein Modell-Call.
- Widersprüche zwischen den Quellen werden **gemeldet** (Abschnitt 10), nicht entschieden.

---

## 10. Zu entscheiden, bevor C6b implementiert wird

Diese vier Punkte sind reale Lücken bzw. Widersprüche zwischen den Quellen, keine
Verständnisfragen dieses Dokuments. Sie sind hier **gemeldet**, nicht aufgelöst.

**Nachtrag 26.08.2026 (D3a):** Punkt **10.1 ist erledigt** — die vier Schlüssel
stehen seit D1 (Commit `40bf33a`) im Manifest, wörtlich abgedruckt in §1.6. Der
Abschnitt bleibt gestrichen stehen, mit auflösendem Nachtrag am Ende. Die übrigen
Punkte dieses Abschnitts sind von D3a **nicht** berührt.

### 10.1 ~~`expected_match_key.K2_K3` für I21–I24 ist im Manifest ein Platzhalter-String, kein Schlüssel~~ — **ERLEDIGT (D1, 26.08.2026)**

**ERLEDIGT seit D1 (26.08.2026, Commit `40bf33a`). Nachgezogen in D3a (26.08.2026).** Der
folgende Abschnitt beschreibt einen Stand, der **nicht mehr besteht**; er bleibt ungekürzt
stehen, weil er die Herkunft der vier Schlüssel dokumentiert. Verbindlich ist der Nachtrag am
Ende dieses Abschnitts und die Tabelle in §1.6.

`data/soll/injection_manifest.json` trägt für die vier `FRAMEWORK_TYPE_IN_SIGNATURE`-Injektionen
(I21–I24) bei `expected_match_key.K2_K3` wörtlich den String `"OFFEN — Typ festgelegt
(sqlalchemy.orm.Session, 25.08.2026), wörtliche Schreibweise und tragende Methode bleiben offen,
siehe offending_type_resolution_note"`. `c4c_bericht_vorabpruefung.md` §A2 hat die vier
tatsächlich resultierenden Schlüssel bereits **mechanisch aus §1c abgeleitet** und tabelliert:

```
I21  FORBIDDEN_SIGNATURE_TYPE|identity_models|depot.identity.models.customer_models|sqlalchemy.orm.Session
I22  FORBIDDEN_SIGNATURE_TYPE|orders_models|depot.orders.models.order_models|sqlalchemy.orm.Session
I23  FORBIDDEN_SIGNATURE_TYPE|orders_models|depot.orders.models.order_line_models|sqlalchemy.orm.Session
I24  FORBIDDEN_SIGNATURE_TYPE|billing_models|depot.billing.models.invoice_models|sqlalchemy.orm.Session
```

trägt sie aber **ausdrücklich nicht ins Manifest ein**, mit der Begründung, der C4c-Auftrag dürfe
nur SHAs und Methodennamen nachtragen, keinen `expected_match_key` setzen (§A2: „**Der Eintrag ist
als eigener Punkt zu entscheiden**, bevor die K2/K3-Kampagne über I21–I24 ausgewertet wird — sonst
fehlt dort der Join-Schlüssel."). **Widerspruch/Lücke:** das eingefrorene Ground-Truth-Artefakt
und der abgeleitete Wert existieren an zwei verschiedenen Stellen und sind bewusst nicht
zusammengeführt. C6b braucht für `strict` auf diesen vier Injektionen einen realen Schlüssel — ob
der c4c-abgeleitete Wert einfach ins Manifest übernommen wird (und wenn ja, mit welchem
Freeze-/Commit-Verfahren, da das Manifest laut `injection_sha256_rationale` bewusst **vor** den
Injektions-Commits gehasht wurde) oder ob die Harness ihn zur Laufzeit selbst herleitet, ist offen.

> **Nachtrag 26.08.2026 (D3a) — AUFGELÖST, NICHT MEHR OFFEN.** In **D1** sind die vier
> abgeleiteten Schlüssel ins Manifest eingetragen worden (Commit `40bf33a`,
> `d1_bericht_matchkey_eintrag.md`); `expected_match_key.K2_K3` trägt für I21–I24 jetzt den
> realen Schlüssel, wörtlich abgedruckt in **§1.6**. Von den beiden im Absatz oben genannten
> Wegen ist damit der **erste** gewählt: der Wert steht **im Manifest**, die Harness leitet
> ihn **nicht zur Laufzeit her**. C6b darf `expected_match_key.K2_K3` für diese vier
> Injektionen **wie für jede andere Injektion behandeln** und braucht **keinen Sonderpfad**.
>
> **Zum Freeze-Verfahren, das der Absatz oben als offen benennt:** das Manifest ist laut
> `injection_sha256_rationale` bewusst **vor** den Injektions-Commits gehasht; der Eintrag ist
> als **Manifeständerung mit eigenem Commit und nachgezogenem `SHA256SUMS`/`MANIFEST.md`**
> vollzogen, nicht stillschweigend (D1). Ein zweiter Punkt bleibt davon unberührt und ist
> **nicht** mit diesem Nachtrag erledigt: die **Schreibvarianz** des Modells bei diesem Typ
> (57 zu 6 im K2-Ruhezustand) — sie ist als **vorhergesagter `strict`-Ausfall** vorregistriert
> (Protokoll §4 Nachtrag Rev. 31) und wird **nicht** durch Normalisierung des Schlüssels
> behandelt; s. §3.4 (1).

### 10.2 K4/`CYCLE`: die Ausgabeform trägt strukturell kein Modul — `localized` ist dafür nicht wie definiert berechenbar

`localized` verlangt „mindestens ein Finding **im erwarteten Modul** der erwarteten Komponente"
(§4). Der `acyclic_siblings`-Zyklenblock (§1.4, §6.1) ist **ausdrücklich ohne Modulnamen**
spezifiziert: „relativ zum `ancestor` notiert, mit Importzähler, **OHNE Modulnamen**" (Protokoll
§4 Am. 13.08.(c), gemessen `c2a_bericht_contract_semantik.md` §2.2a: `- .mappers -> .api (1
import)`). Für K4 bei `CYCLE_SIBLING` (Matrixzelle „ja") und die K4-Doppelmeldung bei
`LAYER_BACK_CALL` (§5 Fall 3) gibt es also **keine Modulinformation**, aus der die Harness ein
`(component, module, category)`-Tripel für den `localized`-Vergleich bilden könnte — nur ein
Komponentenpaar. Zwei mit den Quellen vereinbare, aber unterschiedliche Lesarten sind denkbar:
(a) `localized` für diese spezifischen K4-Funde auf Komponentenebene statt Modulebene zu prüfen
(Modul-Bedingung als automatisch erfüllt behandeln, sobald die Komponente stimmt), oder (b) diese
Funde von `localized` grundsätzlich auszunehmen und nur über die in §6.1 spezifizierte
Mengenregel (eine reine Ja/Nein-Erkennungsaussage ohne Modulauflösung) zu führen. Keine der beiden
Lesarten steht so explizit in einer Quelle; die Erwartungsmatrix selbst (die für K4/`CYCLE_
SIBLING` „ja" vorhersagt) setzt implizit voraus, dass irgendeine Form von `localized` dafür
berechenbar ist, ohne die Modulfrage zu benennen.

### 10.3 Wanduhrzeit „je Injektionslauf und Konfiguration" — zwei nicht deckungsgleiche Felder, konfigurationsabhängig

Für K1/K2/K3 liegt eine Wanduhrzeit im `run_footer.wall_clock_ms` des Checkers vor (`run.ts:112,
260`: `Date.now() - startedAt`, gemessen **innerhalb** des CLI-Prozesses). Für K4/K5 existiert
**kein** `run_footer` — beide sind externe Werkzeuge ohne das Checker-Logformat; Protokoll §6
Nachtrag Rev. 24 stellt fest: „Für K4/K5 muss die **Harness** Ausgabe und Exit-Code selbst
archivieren; eine native strukturierte Ausgabepfad-Option ist im festgelegten Aufrufweg nicht
vorhanden." Die Wanduhrzeit für K4/K5 kann also nur vom **Kampagnen-Runner** gemessen werden —
strukturell analog zum `duration_s`-Feld, das für die K2/K3-Kontrollläufe bereits im
`run_manifest.json` des Runners vorliegt (`data/c3b-k2/run_manifest.json`,
`data/c3b-k3/run_manifest.json`, §1.7), aber inhaltlich **nicht dasselbe misst** wie
`wall_clock_ms` (Runner-Außensicht inkl. Subprozess-Overhead vs. Checker-Innensicht ohne
Checkout-/Build-Overhead). Für die Injektionsläufe (im Unterschied zu den bereits gelaufenen
Kontrollläufen) existiert noch kein `run_manifest.json`, weil die Kampagne noch nicht gelaufen
ist. **Offen:** ob C6b für K1/K2/K3 einheitlich `run_footer.wall_clock_ms` nimmt und für K4/K5
eine vom Runner zu schaffende äquivalente Messung, oder ob durchgehend die Runner-Außensicht
(analog `duration_s`) verwendet wird, damit die Zahl über alle fünf Konfigurationen
vergleichbar ist — die Pipeline-Tauglichkeits-Aussage aus §8 Punkt 6 braucht eine **einheitliche**
Definition, sonst vergleicht sie fünf verschiedene Uhren.

### 10.4 ~~K4/K5-Matchregeln liegen im Manifest nur als Prosa je Injektion vor, nicht als generische Regel~~ — **ERLEDIGT (C6b-2/2a/2b, 27.08.2026)**

**ERLEDIGT.** Der folgende Abschnitt beschreibt einen Stand, der **nicht mehr besteht**; er
bleibt ungekürzt stehen, weil er die Herkunft der generischen Regel dokumentiert. Verbindlich
ist der Nachtrag am Ende dieses Abschnitts.

Protokoll §4 Hauptregel verlangt: „Die Abbildungsregeln werden **vor der Messung im Harness-Code
fixiert** und im Manifest referenziert." Der tatsächliche Zustand des Manifests
(`injection_manifest.json`, §1.6) trägt `k4_match_rule`/`k5_match_rule` als **freien Text je
Injektion** (z. B. bei I01: „layers-Spine-Contract meldet BROKEN für die Rückkante
repository->services; ZUSÄTZLICH meldet der acyclic_siblings-Contract …"), nicht als
parametrisierte, von C6b direkt ausführbare Vergleichsfunktion. Abschnitt 6 dieses Dokuments
formuliert die **allgemeinen** Vergleichsvorschriften (Mengenregel für K4/`CYCLE`, Regelname für
K5) so präzise, wie die Quellen es hergeben — ob diese allgemeine Formulierung ausreicht, um alle
32 Fälle automatisiert (ohne Einzelfallprüfung anhand der Prosa je Injektion) zu matchen, oder ob
C6b für einzelne Kategorien (insbesondere `PROTECTED_MODULE`, `INDEPENDENCE`, `MISSING_PORT_
REFERENCE` mit ihren je eigenen Contract-Typen und Detailzeilenformaten, §1.4) je eine eigene
Parserfunktion braucht, ist nicht vorentschieden.

> **Nachtrag 27.08.2026 (C6b-2, C6b-2a, C6b-2b) — AUFGELÖST, NICHT MEHR OFFEN.** Die
> generische Regel steht in **`tools/match_k4k5.py`**, die Herleitung je Zelle in
> `docs/repo-kontext/c6b2_bericht_matchregel.md`.
>
> **Von den beiden im Absatz oben genannten Wegen ist der ERSTE gewählt.** Die allgemeinen
> Vorschriften tragen; es braucht **keine** Parserfunktion je Kategorie. Die Granularität ist
> **eine Regel je besetzter Zelle von T8** — also je (Werkzeug × Ebene-2-Szenario), **nicht**
> je Injektion: **13 Regeln** (sechs für K4, sieben für K5) statt 32 handgeschriebener
> Erwartungen. Die sieben unbesetzten Zellen bekommen **keine** Regel; sie tragen ` — ` aus
> T1/T8 und können darum nie einen Treffer erzeugen. Die Prosa in
> `MAN.injections[].k4_match_rule`/`.k5_match_rule` ist **nicht** in Code übersetzt worden;
> sie ist als Gegenprobe gelesen worden und hat an einer Stelle die Richtung einer Buchung
> geklärt (I25, s. u.).
>
> **Die beiden „teilweise"-Zellen sind abgeleitet, nicht festgelegt.** K4/`INCORRECT_LOCATION`
> (Fussnote 5) und K5/`CYCLE_*` (Fussnote 7): Treffer in `localized`, **nie** in `strict`.
> Für Fussnote 7 steht die Buchung wörtlich im Protokoll; für Fussnote 5 steht die Richtung
> wörtlich im eingefrorenen Manifest (I25 `k4_match_rule`: „richtige Stelle, falsche Art
> (Fussnote 5); **zaehlt in localized, nie in strict**"). **Es ist nichts entschieden worden,
> was nicht dastand** — die Sperre aus §0.1 ist gewahrt, es bewegt sich **keine Matrixzelle**
> und es ändert sich **keine Metrikdefinition**.
>
> **Was der Parser NICHT tut:** keine Metrik, keine Aggregation, kein Vergleich über Läufe.
> Er liefert je Fund Werkzeug, Zelle, extrahierte Bestandteile und Klassifikation
> (`treffer` / `begleitmeldung` / `sonstiger_fund` / `regel_nicht_ausgewertet` /
> `werkzeugabbruch`). Das Rechnen ist Sache der Harness.
>
> **Belegt.** 32 Fixtures unter `tests/fixtures/k4k5/`, Selbsttest 32/32. Die Regel erfasst
> die **64 archivierten K4/K5-Kampagnenausgaben vollständig** — 0 nicht erfasste nicht leere
> Zeilen. Das ist ein Befund über die **Stabilität der Ausgabeformen**, kein
> Auswertungsergebnis: keine Fundliste, keine Klassifikation, keine Zahl über die Kampagne.
>
> **Zur Blindheit, exakt gefasst.** Die 13 Regeln und die Rahmengrammatik sind aus
> **vorregistrierten Quellen** (c2b/c2c/c2a/b9+, Protokoll §3–§5, die gehashten Messeingänge,
> der archivierte Ruhezustand) und aus **eigenen Läufen der Werkzeuge gegen Wegwerfeingaben**
> gebaut. Von den 64 Kampagnenausgaben wurden **zwei Zeilen einer Datei gelesen** — nach
> einer **vor** dem Lesen festgelegten Abbruchbedingung, protokolliert in
> `c6b2_bericht_matchregel.md` Teil III; die Anpassung erfolgte an der **Werkzeuggrammatik**
> und ist durch einen eigenen Lauf belegt. **63 von 64 Dateien sind unangesehen.** Keine
> Fundzeile, keine Fundliste, keine Klassifikation, keine Zelle bewegt.
>
> **Offen bleibt eine Lücke, ausdrücklich als solche geführt (L1).** Die in
> `c2b_bericht_k4_konfiguration.md` §B4 abgedruckte `INDEPENDENCE`-Ausgabe nennt als Träger
> `depot.orders.services.order_service`; **keine** der drei `INDEPENDENCE`-Injektionen
> (I10–I12) trägt dieses Modul. Die **Ausgabeform** dieser Zelle ist damit belegt, ein
> zellenscharfer Positivfall der **Vergleichsregel** nicht; sie läuft über denselben Codepfad
> wie K4/`LAYER_BACK_CALL` und K4/`LAYER_SKIP_CALL`, die je einen belegten Positivfall tragen.
> Ein selbst erzeugter Lauf schliesst diese Lücke **nicht** — das wäre eine neue Belegquelle
> für eine vorregistrierte Zelle.

### 10.5 Nachrichtlich, nicht blockierend: der deskriptive Vollbild-Commit fehlt noch

Protokoll §6 Nachtrag Rev. 29 registriert einen 33. Commit (alle 32 Injektionen auf `B`, für einen
rein deskriptiven K1/K4/K5-Lauf) als vorregistriert, aber von C4b nicht gebaut — „als OFFEN
geführt, ohne Wirkung auf eine Metrik und ohne Blockade von C4c oder der Kampagne". C6b muss ihn
nicht bedienen (er wird gegen kein Manifest gejoint und geht in keine Metrik ein), sollte aber so
gebaut sein, dass ein später nachgereichter Vollbild-Lauf **nicht** versehentlich durch dieselbe
Pipeline wie die 32 Injektionsläufe gegen das Manifest gejoint wird — die Lauf-Akzeptanzregeln aus
§7.4 gelten für ihn ausdrücklich nicht, und ein Join würde bei mehreren gleichzeitigen Zyklen
falsche `expected_match_key`-Vergleiche erzeugen (Protokoll §6 Am. 12.08.).

---

## Quellenverzeichnis (zentrale Belege)

- `docs/protokolle/eval_protokoll_phase04.md` (Rev. 29), insb. §1–§9.
- `docs/ddr/checker_entscheidungen_o.md` (Decision Record O).
- `docs/ddr/checker_entscheidungen_l_m.md` (Decision Records L, M, M.2).
- `docs/ddr/checker_entscheidungen_p.md` (Decision Record P).
- `data/soll/injection_manifest.json`, `data/soll/injection_manifest.md`.
- `docs/repo-kontext/c2a_bericht_regeldatei.md`, `c2a_bericht_contract_semantik.md`,
  `c2b_bericht_erlaubnislisten.md`, `c2b_bericht_k4_konfiguration.md`,
  `c2c_bericht_k5_konfiguration.md`, `4c_bericht_soll_und_validator.md`,
  `c4a_bericht_injektionsmanifest.md`, `c4b_bericht_injektionen.md`,
  `c4c_bericht_vorabpruefung.md`, `c3b_bericht_kontrolllauf.md`,
  `c3b_k2_bericht_kontrolllauf.md`, `c3b_k2_nachtrag_findingbezug.md`,
  `c3b_k3_bericht_kontrolllauf.md`, `b1_bericht_matchkey.md`,
  `c1b_bericht_komponentenschnitt.md`, `c1b_bericht_ruleengine_verifikation.md`.
- `tritongraph` (Commit `348ca9d`, read only): `packages/triton-conformance/src/run.ts`,
  `runLog.ts`, `reporter.ts`, `jsonOut.ts`, `matchKey.ts`, `validate.ts`, `llmChecker.ts`.
