# C3b-K3 — Kontrolllauf über die 52 Kontrollmodule (DigitalOcean-Direktzugang): Falsch-Positiv-Rate

**Datum:** 25. August 2026
**Bezug:** Protokoll §5 (Metriken, vorregistrierte Meldungen Rev. 16/18), §6 Nachtrag Rev. 24
(Aufrufspezifikation, Build-Provenienz), Rev. 25 (getrennte Recordmengen), Rev. 26
(Wiederholungsfaktor, Exit-Code kein Gültigkeitskriterium); Vorlauf
[`k3_machbarkeitslauf_direktzugang_bericht.md`](k3_machbarkeitslauf_direktzugang_bericht.md) ·
Gegenstück [`c3b_k2_bericht_kontrolllauf.md`](c3b_k2_bericht_kontrolllauf.md) (Ollama-Hälfte,
dasselbe Control-Set)
**Messobjekt:** `ma-conformance-testrepo` bei Tag `baseline` = `0d651041ed87dd03f2f78359713633fac01c0a66`
**Checkerstand:** `tritongraph` = `348ca9daa456af4954f11f7152fc45201035297e`

---

## 0. Abgrenzung — was dieser Bericht ist und was er nicht ist

**Dies ist eine Messung, kein Machbarkeitslauf.** Die Records sind archiviert
(`data/c3b-k3/`), werden hier ausgewertet und fließen in die Falsch-Positiv-Rate der Arbeit ein.

**C3b zerfällt ausführungsseitig in C3b-K2 (Ollama/lokal, bereits berichtet) und C3b-K3 (dieser
Auftrag, DigitalOcean-Direktzugang)** — eine Aufteilung der **Ausführung**, keine Designänderung
des Protokolls; Falsch-Positiv-Rate und Median werden nach Protokoll §5 ohnehin **je
Konfiguration** gebildet.

**Kein Bestehenskriterium.** Protokoll §6 Nachtrag Rev. 23 legt für K2/K3 fest: das Ergebnis ist
die Falsch-Positiv-Rate, keine Schwelle, gegen die bestanden oder durchgefallen wird. Zwei
Meldungen sind **vorregistriert** (§5 Nachtrag Rev. 16: `depot.core.adapters`; Rev. 18: die
Nicht-Träger-Portregel auf `orders_services`) und werden **getrennt** von der übrigen Rate
geführt (§4.3 unten). Dieser Bericht **zählt und klassifiziert**; er **interpretiert nicht** — ob
ein Finding „berechtigt" ist oder was die Rate für die Forschungsfragen bedeutet, gehört nach
Kapitel 7.

**Bezugsweg wie im Direktzugang-Machbarkeitslauf, abweichend von der Rev.-24-Registrierung.**
Base-URL `https://inference.do-ai.run/v1`, Modell `nvidia-nemotron-3-super-120b`, Schlüssel aus
`~/ma/.secrets/do.env` (`DO_MODEL_ACCESS_KEY`), **kein** `CONFORMANCE_PROVIDER_PIN` — ohne Router
gibt es nichts zu pinnen (B32). Alle übrigen Parameter der registrierten Zeile (Temperatur,
Timeout, `--runs 3`) unverändert.

**Ausführungsform: 52 Einzeldatei-Invocationen statt einer registrierten Mehrdatei-Invocation.**
Dieselbe Abweichung wie C3b-K2, aus demselben Grund (Verlustgranularität,
`c3b_k2_bericht_kontrolllauf.md` §0, `k2_machbarkeitslauf_bericht.md` §11). `control_files.txt`
selbst wurde an keiner Stelle verändert; nur `--control-files` und die Ausgabepfade variieren je
Invocation.

**Wiederaufnahme, ausdrücklich Teil dieses Auftrags:** 2 der 52 Invocationen scheiterten in
Runde 1 an transportfehlerhaften Calls und wurden in Runde 2 einzeln nachgefahren — beide danach
gültig. Details in §2 und §3g.

### ERGEBNIS IN EINEM SATZ

Nach Wiederaufnahme liegen alle 52 Invocationen gültig vor (2 h 04 min 32 s Gesamtdauer, 2
Invocationen in Runde 2 nachgefahren, 8 HTTP-429 und 1 HTTP-5xx insgesamt beobachtet); die
Falsch-Positiv-Rate (Median über drei Läufe, Nenner 52) liegt bei **1/52 = 0,0192** — nur ein
einziges Kontrollmodul erhielt im Medianlauf ein Finding, und **keine** der beiden vorregistrierten
Meldungen (Fassade Rev. 16, Portregel Rev. 18) trat in irgendeinem der drei Läufe auf.

---

## 1. Vorbedingungen — je einzeln belegt

### 1a — Checker neu gebaut, `sha256sum dist/cli.js`

```
$ date -Iseconds
2026-08-25T11:47:16+02:00
$ cd ~/ma/tritongraph/packages/triton-conformance && npm run build
> esbuild src/cli.ts --bundle --platform=node --format=esm --packages=external --outfile=dist/cli.js
  dist/cli.js  51.5kb
⚡ Done in 12ms
$ sha256sum dist/cli.js
c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95  dist/cli.js
```

**Erwartet:** `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` — **identisch**.

`git -C ~/ma/tritongraph status --porcelain` vor dem Build: leer. Nach dem Build: leer (außer dem
gitignorierten `dist/`). Kein Commit, kein Push, keine Quelltextänderung im Checker-Repo während
des gesamten Auftrags.

### 1b — `sha256sum -c SHA256SUMS` in `data/soll`

```
$ cd ~/ma/masterarbeit/data/soll && sha256sum -c SHA256SUMS
architecture-rules.yaml: OK
depot_soll.ilograph.yaml: OK
importlinter.ini: OK
test_architecture.py: OK
control_files.txt: OK
injection_manifest.md: OK
injection_manifest.json: OK
```

Alle sieben OK (zwei zusätzliche Einträge gegenüber C3b-K2, seit `56055de` abgeleitetes
Injektionsmanifest, keine Abweichung). `control_files.txt`: `wc -l` = 52, `sha256sum` =
`7356e6d332e5165acdfdcfac1a66bd9803a7fa36cb4b3e7d5480bcb3526fee62` — identisch mit der erwarteten
Prüfsumme.

### 1c — Referenz-Commits

```
$ git -C ~/ma/ma-conformance-testrepo rev-parse baseline
0d651041ed87dd03f2f78359713633fac01c0a66
$ git -C ~/ma/ma-conformance-testrepo rev-parse HEAD
0d651041ed87dd03f2f78359713633fac01c0a66
$ git -C ~/ma/ma-conformance-testrepo status --porcelain
(leer)
$ git -C ~/ma/tritongraph rev-parse HEAD
348ca9daa456af4954f11f7152fc45201035297e
```

`baseline` und `HEAD` des Testrepos identisch, Arbeitsbaum sauber, Checker auf dem registrierten
Stand.

### 1d — `tools/validate_soll.py` gegen `B`

```
$ python3 tools/validate_soll.py \
    --soll data/soll/depot_soll.ilograph.yaml --testrepo ~/ma/ma-conformance-testrepo \
    --rules data/soll/architecture-rules.yaml
[1] OK  Soll-Only = 4 (die vier Legacy-Phantome), tree-only = 0
[2] OK  Komponenten ohne Relation = 0
[3] OK  (3a) Scope außerhalb Topologie = 0   (3b) Komponenten ohne Regel = 0
        (3c) Kategorien außerhalb Level-1 = 0   (3d) Level-1-Kategorien ohne Regel = 0
[4] OK  I1-Verstöße = 0
[5] OK  vier Zyklenpaare in Code-Unit-Reihenfolge
[6] OK  Alleinimporteur je Komponente, fünf Fälle
[7] OK  Zyklen im Ist-Graph = 0
[8] OK  Kanten außerhalb Whitelist = 0 (81 gemappte Kanten, 39 Whitelist-Relationen)
RESULT: OK
Exit: 0
```

Alle acht Punkte, (3a)–(3d) eingeschaltet, Exit 0 — keine Abweichung.

### 1e — Schema-Testcall gegen den Direktzugang

Identischer Aufbau wie im Machbarkeitslauf §1d (`llmClient.ts:120-123`, `VIOLATIONS_SCHEMA`
wörtlich, `schemaName: 'conformance_violations'`), gegen
`https://inference.do-ai.run/v1/chat/completions`:

```
HTTP status: 200
latency_ms: 3215
body: {"choices":[{"finish_reason":"stop", …, "message":{"content":"{\"violations\": []}", …}}],
  "model":"nvidia-nemotron-3-super-120b",
  "usage":{"completion_tokens":46,"prompt_tokens":42,"total_tokens":88, …}}
```

HTTP 200, schemakonform, `usage` vollständig vorhanden — keine Abweichung.

**Alle fünf Vorbedingungen bestanden, keine Abweichung. Kein Abbruch nötig.**

---

## 2. Der Lauf

### Die Aufrufzeile — wörtlich, je Invocation eine Kontrolldatei

Vorlage aus Protokoll §6 Rev. 24, Abschnitt „Kontrolllauf K2 und K3 auf B", mit dem im Auftrag
vorgeschriebenen Bezugsweg:

```sh
CONFORMANCE_API_KEY=<DO_MODEL_ACCESS_KEY aus ~/ma/.secrets/do.env> \
CONFORMANCE_BASE_URL=https://inference.do-ai.run/v1 \
CONFORMANCE_MODEL=nvidia-nemotron-3-super-120b \
node ~/ma/tritongraph/packages/triton-conformance/dist/cli.js \
  --topology ~/ma/masterarbeit/data/soll/depot_soll.ilograph.yaml \
  --rules ~/ma/masterarbeit/data/soll/architecture-rules.yaml \
  --src-root src --rule-graph diff --base 0d651041ed87dd03f2f78359713633fac01c0a66 \
  --runs 3 --timeout-ms 600000 \
  --control-files <scratch>/c3bk3_ctrl/f<NN>.txt \
  --run-log <out>/control_k3_f<NN>.jsonl --json-out <out>/control_k3_f<NN>.json
```

Nur `--control-files` (Einzeldatei-Liste, eine Zeile aus `control_files.txt`) und die beiden
Ausgabepfade (Laufindex `f01`…`f52` im Dateinamen) variieren je Invocation; jede weitere Zeile ist
wortgleich mit der Registrierung, bis auf den im Auftrag vorgeschriebenen Bezugsweg
(`CONFORMANCE_BASE_URL`, `CONFORMANCE_MODEL`, kein `CONFORMANCE_PROVIDER_PIN`).
Arbeitsverzeichnis jeder Invocation: `~/ma/ma-conformance-testrepo` (`repoRoot: process.cwd()`,
`cli.ts:78`).

Ein Orchestrator-Skript im Sitzungs-Scratchpad hat die 52 Invocationen sequentiell abgesetzt, je
Datei in der Reihenfolge von `control_files.txt`, mit **30 Sekunden Pause** zwischen den
Invocationen (dasselbe Profil wie im Machbarkeitslauf), und implementierte die im Auftrag
verlangte Wiederaufnahmeregel: eine Invocation mit nicht-leerem `invalid_reasons` oder
`calls_transport_failed > 0` wurde notiert, der Durchgang lief weiter, und alle notierten Dateien
wurden nach Abschluss von Runde 1 einzeln, mit derselben 30-Sekunden-Pause, in Runde 2 nachgefahren.
Das Skript wurde **nicht committet** (Auftragsvorgabe); sein Ergebnis ist ausschließlich in
`data/c3b-k3/` und in diesem Bericht sichtbar.

### Verlauf

| | |
|---|---|
| Start (Runde 1) | 2026-08-25T11:50:16+02:00 |
| Ende (Runde 2) | 2026-08-25T13:54:48+02:00 |
| Gesamtdauer | **2 h 04 min 32 s** |
| Prognose (Auftrag) | ≈ 3 h |
| Invocationen Runde 1 | 52 von 52 abgesetzt, **2 gescheitert** |
| Invocationen Runde 2 (Wiederholungen) | 2 von 2, **beide gültig** |
| Nach Runde 2 offen | **0** |
| Einzeldauer je gezählter Invocation | min 21,8 s (`orders/services/pricing/engine.py`), max 319,4 s (`billing/repository/invoice_query.py`), Mittel 105,8 s |
| Exit-Code-Verteilung (gezählt) | Exit 1 (Finding in Run-Index 0): 2 · Exit 0: 50 |

Die gemessene Gesamtdauer liegt **unter** der im Auftrag genannten Prognose von rund drei Stunden
— plausibel, weil die Prognose aus dem Machbarkeitslauf (5 Dateien, darunter die regelreichste
Datei `catalog_service.py`) hochgerechnet wurde, während die tatsächliche 52er-Stichprobe deutlich
weniger Findings und damit kürzere Ausgaben produzierte (§4).

### Wiederaufnahme — die beiden Runde-2-Fälle, mit Grund, Zeitpunkt und Ergebnis

| Datei | Runde 1: Grund des Scheiterns | Zeitpunkt Runde 1 | Runde 2: Zeitpunkt | Runde 2: Ergebnis |
|---|---|---|---|---|
| `src/depot/identity/repository/session_repo.py` | `run_index 1`: 3× HTTP 429 in Folge, Transport-Retry-Budget (3 Versuche) erschöpft → `transport_failed`; `invalid_reasons: ["transport_failure"]` | 11:04:40+02:00 (Fußzeile) | 11:47:05–11:50:48+02:00 | vollständig gültig, `invalid_reasons: []`, `calls_transport_failed: 0` |
| `src/depot/identity/services/customer_service.py` | `run_index 0`: 3× HTTP 429 in Folge, Transport-Retry-Budget erschöpft → `transport_failed`; `invalid_reasons: ["transport_failure"]` | 11:06:51+02:00 (Fußzeile) | 11:51:19–11:54:48+02:00 | vollständig gültig, `invalid_reasons: []`, `calls_transport_failed: 0` |

Beide Runde-1-Invocationen hatten zusätzlich je einen weiteren, folgenlos per Transport-Retry
behobenen 429 auf einem anderen `run_index` derselben Datei (`session_repo.py#2`,
`customer_service.py#1`) — insgesamt 4 × 429 je Datei in Runde 1 (3 erschöpfende + 1 behobener).
Das für §3–§4 gezählte Ergebnis für beide Dateien ist **ausschließlich Runde 2**; die
Runde-1-Rohdaten sind nicht Teil der Zählung, bleiben aber vollständig in `run_manifest.json`
(`data/c3b-k3/`, Feld `attempt: 1`) sowie oben und in §3g dokumentiert — analog zur
Doppelausführung in `k2_machbarkeitslauf_bericht.md` §8: „für §4 wurde ausschließlich die zweite …
Ausführung gezählt."

---

## 3. Nachlaufprüfung je Invocation (Protokoll §6 Rev. 26)

### 3a — `calls_total == control_files_count * runs`

Über alle 52 gezählten Ergebnisse: `control_files_count == 1`, `calls_total == 3` (`1 * 3 == 3`),
`changed_files_count == 0` in jedem der 52 Header — **ohne Ausnahme**. Summiert: `calls_total`
gesamt = **156** (= 52 × 3), wie erwartet. Die vier Inhaltshashes (`topology_sha256`,
`rules_sha256`, `prompt_template_sha256`, `user_prompt_render_sha256`) sind in allen 52
`run_header` zeichengleich (Beleg `data/c3b-k3/MANIFEST.md`).

### 3b — Exit-Code ist kein Gültigkeitskriterium

Gemessen: Exit 1 bei 2 Invocationen (Finding in Run-Index 0 — genau die beiden Dateien mit
überhaupt einem Finding, §4.1), Exit 0 bei 50. Gültigkeit wurde ausschließlich an
`invalid_reasons`, `calls_invalid`, `calls_transport_failed` bemessen: **`invalid_reasons: []`,
`calls_transport_failed: 0` in allen 52 gezählten Fußzeilen.**

### 3c — Token-Budget je Call

Über alle 156 gezählten Calls:

| | |
|---|---|
| `tokens_in` gesamt | 170 880 |
| `tokens_out` gesamt | 88 758 |
| Maximum `tokens_in` | **1590** (`src/depot/orders/services/order_service.py`, Run-Index 0) |
| Maximum `tokens_out` | **1823** (`src/depot/billing/repository/invoice_query.py`, Run-Index 1) |
| Mittel je Call | 1096 in / 569 out |

Kein dokumentiertes Kontextfenster für `nvidia-nemotron-3-super-120b` auf diesem Zugangsweg
bekannt; keine der 156 Antworten zeigte ein Anzeichen von Abschneiden (jede war schemakonformes,
vollständiges JSON, §3f).

### 3d — Getrennte Zählung (Protokoll §4 Rev. 25)

| run_index | `DERIVED:`-Records | LLM-Records |
|---|---|---|
| 0 | 0 | 52 |
| 1 | 0 | 52 |
| 2 | 0 | 52 |
| **gesamt** | **0** | **156** |

0 `DERIVED:`-Records in allen drei Läufen — strukturell erwartet, weil `--rule-graph diff` mit
`changed_files_count: 0` dem Regel-Engine eine leere `observedImports`-Menge liefert
(`ruleEngine.ts:76`/`:157` können unter diesen Bedingungen keinen `DERIVED:forbidden-edge`/
`DERIVED:cycle`-Record erzeugen). Alle 3 gemeldeten Findings (§4) sind LLM-Records.

### 3e — Unbekannte `rule_id` (B1 D1)

**0 Fälle.** Alle 3 gezählten Findings tragen eine der 16 in `architecture-rules.yaml`
definierten `rule_id` (`R-SIG-2`, `R-SIG-3`). Auch unter den (hier: keinen) verworfenen
Validierungsversuchen wurde keine unbekannte `rule_id` gefunden — `calls_invalid: 0` in allen 52
gezählten Fußzeilen.

### 3f — Schemakonformität

**156 von 156 gezählten Calls schemakonform** (`calls_invalid: 0`, `valid_final: true` in jedem
Call). Keine Wiederholung wegen Formatfehlers, keine Halluzination unbekannter `rule_id`.

### 3g — Transport: 429-Statistik über die gesamte Kampagne (Kernkennzahl)

Über **beide** Runden (52 Invocationen Runde 1 plus 2 Wiederholungen Runde 2, 162 tatsächlich
angeforderte Call-Slots):

| | Runde 1 | Runde 2 | gesamt |
|---|---|---|---|
| HTTP 429 | 8 | 0 | **8** |
| HTTP 5xx | 1 | 0 | **1** |
| Transport-Retry griff (Call am Ende gültig) | 3 | 0 | **3** |
| Transport-Retry reichte nicht (Call dauerhaft verloren) | 2 | 0 | **2** |

Die 8 HTTP-429 in Runde 1 verteilen sich auf genau zwei Dateien (`session_repo.py`,
`customer_service.py`, §2) mit je vier 429 (drei erschöpfende + ein behobener); der einzige 5xx
betraf `src/depot/identity/api/routes.py` und wurde sofort per Retry behoben. Auf den **gezählten**
156 Calls (also nach Ersetzung der beiden Runde-1-Fehlschläge durch ihre Runde-2-Wiederholung)
bleiben davon nur der eine 5xx-Fall übrig: `calls_with_transport_retry: 1`,
`calls_transport_failed: 0` insgesamt. **Für die Durchführbarkeit der Kampagne heißt das: 2 von 52
Invocationen (3,8 %) brauchten eine zweite Runde, keine brauchte eine dritte** — die
Wiederaufnahmeregel des Auftrags war ausreichend, ohne dass eine dritte Runde nötig wurde.

**Alle 52 Nachlaufprüfungen grün nach Wiederaufnahme.**

---

## 4. Auswertung — rein deskriptiv

### 4.1 — Je Run-Index: Module mit Finding, Gesamtzahl, Kategorien, Komponenten

| run_index | Module mit ≥1 Finding | Findings gesamt |
|---|---|---|
| 0 | 2 von 52 | 2 |
| 1 | 1 von 52 | 1 |
| 2 | 0 von 52 | 0 |

**Die beiden Module mit mindestens einem Finding in mindestens einem Lauf:**
`depot.billing.repository.invoice_query` (Läufe 0 und 1) und
`depot.orders.repository.order_query` (nur Lauf 0). Alle übrigen 50 Module: 0 Findings in allen
drei Läufen.

**Verteilung über die sechs Kategorien:**

| Kategorie | run 0 | run 1 | run 2 |
|---|---|---|---|
| ABSENCE_REQUIRED | 0 | 0 | 0 |
| API_CONTRACT | 2 | 1 | 0 |
| CYCLE | 0 | 0 | 0 |
| FORBIDDEN_RELATION | 0 | 0 | 0 |
| FORBIDDEN_SIGNATURE_TYPE | 0 | 0 | 0 |
| STRUCTURAL_PLACEMENT | 0 | 0 | 0 |

Jedes der 3 Findings ist `API_CONTRACT` (`R-SIG-2`, `R-SIG-3`) — die einzige Kategorie, in der
dieses Control-Set überhaupt ein Finding erhielt.

**Verteilung über die 19 Komponenten** (nur besetzte gezeigt, alle übrigen 17 sind 0 in jedem
Lauf):

| Komponente | run 0 | run 1 | run 2 |
|---|---|---|---|
| billing_repository | 1 | 1 | 0 |
| orders_repository | 1 | 0 | 0 |

2 von 19 Komponenten mit mindestens einem Finding in mindestens einem Lauf; die übrigen 17,
einschließlich `core_adapters` (Zielkomponente der vorregistrierten Fassaden-Meldung, §4.3) und
`orders_services` (Zielkomponente der vorregistrierten Portregel-Meldung, §4.3), blieben in allen
drei Läufen unbesetzt.

### 4.2 — Falsch-Positiv-Rate, Median über die drei Läufe (Nenner 52)

| Kennzahl | run 0 | run 1 | run 2 | Median | Spannweite |
|---|---|---|---|---|---|
| Module mit ≥1 Finding | 2 | 1 | 0 | **1** | 0–2 (2) |
| Findings (LLM) gesamt | 2 | 1 | 0 | 1 | 0–2 (2) |

**HEADLINE Falsch-Positiv-Rate (Median Module-mit-Finding / 52): 1/52 = 0,0192.**

Bemerkenswert und ohne Interpretation festgehalten: hier streut die Modul-Ebene der Rate **über**
die drei Läufe (2, 1, 0), anders als bei C3b-K2, wo sie über alle drei Läufe konstant blieb
(`c3b_k2_bericht_kontrolllauf.md` §4.2). Die gesamte Streuung entfällt auf zwei Module
(`invoice_query`, `order_query`), von denen keines in allen drei Läufen dasselbe Finding trägt
(§4.4).

### 4.3 — Die beiden vorregistrierten Meldungen, getrennt geführt

**Adapterfassade `depot.core.adapters` / `R-PROTECT-1`** (§5 Nachtrag Rev. 16)

Aufgetreten in **0 von 3 Läufen.** `depot.core.adapters` (Kontrolldatei
`src/depot/core/adapters/__init__.py`) meldete in keinem der drei Läufe irgendein Finding —
weder `R-PROTECT-1` noch eine andere `rule_id`.

**Nicht-Träger-Portregel auf `orders_services` (R-PORT-2 / R-PORT-3)** (§5 Nachtrag Rev. 18)

Aufgetreten in **0 von 3 Läufen.** Keines der `orders_services`-Module (u. a.
`catalog_service.py`, `refund_service.py`, `checkout_service.py`, `order_service.py`,
`services/__init__.py`) meldete in irgendeinem Lauf `R-PORT-2` oder `R-PORT-3` — weder als
Träger- noch als Nicht-Träger-Finding; die Komponente `orders_services` blieb in allen drei
Läufen vollständig unbesetzt (§4.1).

**Beide vorregistrierten Meldungen sind hier nur gezählt, nicht bewertet** — ob ihr Nichtauftreten
bedeutet, dass das Modell die einschränkende Hälfte des jeweiligen `statement` korrekt liest, oder
schlicht Ausdruck der insgesamt sehr niedrigen Finding-Rate dieser Konfiguration ist, ist
Kapitel-7-Fragestellung.

### 4.4 — Stabilität über die drei Repetitionen

| | |
|---|---|
| Identische Findingmenge in allen drei Läufen | **50 von 52 Modulen** |
| Unterschiedliche Findingmenge | **2 von 52 Modulen** |

Die beiden nicht stabilen Module:

| Modul | Lauf 0 | Lauf 1 | Lauf 2 |
|---|---|---|---|
| `depot.billing.repository.invoice_query` | R-SIG-3 (`InvoiceQuery.settled_cents`) | R-SIG-3 (`InvoiceQuery.settled_cents`) | — (kein Finding) |
| `depot.orders.repository.order_query` | R-SIG-2 (`OrderQuery.percent_for`) | — (kein Finding) | — (kein Finding) |

Beide Instabilitäten sind vom selben Typ wie die K2-Seite des Varianzbefunds
(`c3b_k2_bericht_kontrolllauf.md` §4.4, `b36a_bericht_k3_varianzlauf.md`): auch bei
`temperature=0`/`seed=42` ist das Modell über Repetitionen hinweg **nicht** deterministisch
reproduzierbar — hier zeigt sich das als vollständiges Verschwinden eines Findings zwischen
Wiederholungen, nicht als abweichende `subject`-Zuschreibung wie bei K2. Alle übrigen 50
Kontrollmodule lieferten in allen drei Läufen exakt dieselbe (leere) Findingmenge.

### 4.5 — Alle Findings, tabellarisch

**Alle drei** gezählten Findings der gesamten Kampagne, ohne Abzug — keine vorregistrierte
Meldung ist unter ihnen (§4.3: beide traten 0-mal auf). Die vollständigen Rohdaten aller drei
Läufe liegen unverkürzt in `data/c3b-k3/runs/`. **Keine Bewertung, ob die Findings berechtigt
sind** — das ist Kapitel 7.

| run_index | Modul | Komponente | `rule_id` | Kategorie | `subject` |
|---|---|---|---|---|---|
| 0 | `depot.billing.repository.invoice_query` | `billing_repository` | `R-SIG-3` | API_CONTRACT | offending_type=`InvoiceQuery.settled_cents` |
| 1 | `depot.billing.repository.invoice_query` | `billing_repository` | `R-SIG-3` | API_CONTRACT | offending_type=`InvoiceQuery.settled_cents` |
| 0 | `depot.orders.repository.order_query` | `orders_repository` | `R-SIG-2` | API_CONTRACT | offending_type=`OrderQuery.percent_for` |

### 4.6 — Kosten (Auftrag 4f)

Preisquelle: die im Auftrag genannten Sätze **0,30 $/1M Eingabetoken, 0,65 $/1M
Ausgabetoken** (nicht recherchiert, wie im Auftrag vorgegeben — im Unterschied zum
Machbarkeitslauf, wo kein Preis vorlag, `k3_machbarkeitslauf_direktzugang_bericht.md` §12).

| | |
|---|---|
| `tokens_in` gesamt | 170 880 |
| `tokens_out` gesamt | 88 758 |
| Kosten Eingabe | 170 880 × 0,30 $ / 1 000 000 = **0,051264 $** |
| Kosten Ausgabe | 88 758 × 0,65 $ / 1 000 000 = **0,057693 $** |
| **Kosten gesamt** | **0,108957 $** |

Die 8 transportfehlerhaften 429-Antworten und der eine 5xx aus Runde 1 (§3g) sind nicht
gesondert in Rechnung zu stellen — ein Fehlerstatus liefert keine abrechenbare Antwort; nur die
156 tatsächlich gezählten, gemessenen Calls tragen Token.

---

## 5. Ablage

Run-Logs (52 × `.jsonl`), JSON-Ausgaben (52 × `.json`) und ein maschinenlesbares Laufmanifest
(beide Runden, 54 Invocationen) liegen unter [`data/c3b-k3/`](../../data/c3b-k3/) mit
`SHA256SUMS` und `MANIFEST.md` nach der Konvention aus `00_stand_und_entscheidungen.md` §0.
`data/c3b/` (der gescheiterte Notebook-Lauf) und `data/c3b-k2/` (Ollama) bleiben **unverändert**
liegen — dieses Verzeichnis ersetzt keines von beiden.

Das Manifest führt: die Aufrufzeile, `sha256(dist/cli.js)` und Bauzeitpunkt, die vier
Inhaltshashes, `checker_git_head`, `target_repo_git_head`, Modell-ID und Bezugsweg, Datum,
Gesamtdauer und die 429-Statistik beider Runden.

**Read-only-Nachweis der beiden Fremdrepos**, vor und nach dem gesamten Auftrag:

```
git -C ~/ma/tritongraph status --porcelain            → leer (vor und nach)
git -C ~/ma/ma-conformance-testrepo status --porcelain → leer (vor und nach)
git -C ~/ma/tritongraph rev-parse HEAD                 → 348ca9daa456af4954f11f7152fc45201035297e (unverändert)
git -C ~/ma/ma-conformance-testrepo rev-parse HEAD     → 0d651041ed87dd03f2f78359713633fac01c0a66 (unverändert)
```

Kein Commit, kein Push, keine Quelltextänderung in einem der beiden Fremdrepos während des
gesamten Auftrags.
