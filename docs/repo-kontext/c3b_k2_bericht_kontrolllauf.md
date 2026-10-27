# C3b-K2 — Kontrolllauf über die 52 Kontrollmodule (Ollama): Falsch-Positiv-Rate

**Datum:** 24. August 2026
**Bezug:** Protokoll §5 (Metriken, vorregistrierte Meldungen Rev. 16/18), §6 Nachtrag Rev. 24
(Aufrufspezifikation, Build-Provenienz), Rev. 25 (getrennte Recordmengen), Rev. 26
(Wiederholungsfaktor, Exit-Code kein Gültigkeitskriterium); Vorlauf
[`k2_machbarkeitslauf_bericht.md`](k2_machbarkeitslauf_bericht.md)
**Messobjekt:** `ma-conformance-testrepo` bei Tag `baseline` = `0d651041ed87dd03f2f78359713633fac01c0a66`
**Checkerstand:** `tritongraph` = `348ca9daa456af4954f11f7152fc45201035297e`

---

## 0. Abgrenzung — was dieser Bericht ist und was er nicht ist

**Dies ist eine Messung, kein Machbarkeitslauf.** Die Records sind archiviert
(`data/c3b-k2/`), werden hier ausgewertet und fließen in die Falsch-Positiv-Rate der Arbeit ein.

**C3b zerfällt ausführungsseitig in C3b-K2 (dieser Auftrag, Ollama/lokal) und C3b-K3** (sobald
der DigitalOcean-Zugang steht, OpenRouter-Provider-Pin). Das ist eine Aufteilung der
**Ausführung**, keine Designänderung des Protokolls — Falsch-Positiv-Rate und Median werden nach
Protokoll §5 ohnehin **je Konfiguration** gebildet, K2 und K3 waren nie eine gemeinsame Zahl.

**Kein Bestehenskriterium.** Protokoll §6 Nachtrag Rev. 23 legt für K2/K3 fest: das Ergebnis ist
die Falsch-Positiv-Rate, keine Schwelle, gegen die bestanden oder durchgefallen wird. Zwei
Meldungen sind **vorregistriert** (§5 Nachtrag Rev. 16: `depot.core.adapters`; Rev. 18: die
Nicht-Träger-Portregel auf `orders_services`) und werden **getrennt** von der übrigen Rate
geführt (§4.3 unten). Dieser Bericht **zählt und klassifiziert**; er **interpretiert nicht** — ob
ein Finding „berechtigt" ist oder was die Rate für die Forschungsfragen bedeutet, gehört nach
Kapitel 7.

**Ausführungsform: 52 Einzeldatei-Invocationen statt einer registrierten Mehrdatei-Invocation.**
Die im Protokoll §6 Rev. 24 wörtlich registrierte Zeile („Kontrolllauf K2 … auf B") setzt
`--control-files` auf die volle `control_files.txt` in **einer** Invocation. Diese Ausführung
zerlegt sie stattdessen in 52 Einzeldatei-Invocationen — dieselbe Abweichung, die der
Machbarkeitslauf bereits an fünf Dateien validiert hat, und aus demselben Grund: der
gescheiterte Notebook-Lauf (`data/c3b/`) verlor bei zwei Abstürzen den **gesamten** Fortschritt,
weil die einzige Verlustgranularität der Run-Index einer Mehrdatei-Invocation war
(`data/c3b/MANIFEST.md` §3.3, `k2_machbarkeitslauf_bericht.md` §11). Bei Einzeldatei-Zerlegung
kostet ein Abbruch höchstens eine Datei, nie den Durchgang. `control_files.txt` selbst wurde an
keiner Stelle verändert; nur `--control-files` und die Ausgabepfade variieren je Invocation.

### ERGEBNIS IN EINEM SATZ

Alle 52 Invocationen liefen gültig und ohne Wiederholung durch (33 min 2 s Gesamtdauer, GPU
konstant ≤ 60 °C); die Falsch-Positiv-Rate (Median über drei Läufe, Nenner 52) liegt bei
**49/52 = 0,9423** — 49 der 52 Kontrollmodule erhielten in jedem der drei Läufe mindestens ein
Finding, mit den beiden vorregistrierten Meldungen (Fassade: 3/3 Läufe; Portregel: 1/3 Läufe)
getrennt darin enthalten.

---

## 1. Vorbedingungen — je einzeln belegt

### 1a — Checker neu gebaut, `sha256sum dist/cli.js`

```
$ date -Iseconds
2026-08-24T17:06:31+02:00
$ cd ~/ma/tritongraph/packages/triton-conformance && npm run build
> esbuild src/cli.ts --bundle --platform=node --format=esm --packages=external --outfile=dist/cli.js
  dist/cli.js  51.5kb
⚡ Done in 14ms
$ date -Iseconds
2026-08-24T17:06:32+02:00
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
```

Alle fünf OK. `control_files.txt`: `wc -l` = 52, `sha256sum` = `7356e6d332e5165acdfdcfac1a66bd9803a7fa36cb4b3e7d5480bcb3526fee62` — identisch mit der
erwarteten Prüfsumme.

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

### 1d — Ollama

```
$ ollama --version
ollama version is 0.32.15
$ curl -s localhost:11434/api/version
{"version":"0.32.15"}
$ ollama show qwen2.5-coder:7b
  architecture   qwen2      parameters   7.6B   context length 32768
  embedding length 3584     quantization Q4_K_M
  capabilities   completion, tools, insert
$ ollama list | grep qwen2.5-coder
qwen2.5-coder:7b    dae161e27b0e    4.7 GB
$ ollama ps
(leer — kein Modell geladen)
$ nvidia-smi
GPU 0 NVIDIA GeForce RTX 3070 Ti, 0 % Last, 43 °C, 1138 MiB / 8192 MiB (Xwayland-Anteil)
```

Digest `dae161e27b0e` — identisch mit dem erwarteten Wert. Ollama im Leerlauf vor dem Lauf: kein
Modell geladen, GPU bei 43 °C.

### 1e — `tools/validate_soll.py` gegen `B`

```
$ ~/ma/venv/bin/python tools/validate_soll.py \
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
[8] OK  Kantenaußerhalb Whitelist = 0 (81 gemappte Kanten, 39 Whitelist-Relationen)
RESULT: OK
Exit: 0
```

Alle acht Punkte, (3a)–(3d) eingeschaltet, Exit 0 — keine Abweichung.

**Alle fünf Vorbedingungen bestanden, keine Abweichung. Kein Abbruch nötig.**

---

## 2. Der Lauf

### Die Aufrufzeile — wörtlich, je Invocation eine Kontrolldatei

Vorlage aus Protokoll §6 Rev. 24, Abschnitt „K2, Ollama" / „Kontrolllauf K2 und K3 auf B":

```sh
CONFORMANCE_API_KEY=ollama \
CONFORMANCE_BASE_URL=http://localhost:11434/v1 \
CONFORMANCE_MODEL=qwen2.5-coder:7b \
node ~/ma/tritongraph/packages/triton-conformance/dist/cli.js \
  --topology ~/ma/masterarbeit/data/soll/depot_soll.ilograph.yaml \
  --rules ~/ma/masterarbeit/data/soll/architecture-rules.yaml \
  --src-root src --rule-graph diff --base 0d651041ed87dd03f2f78359713633fac01c0a66 \
  --runs 3 --timeout-ms 240000 \
  --control-files <scratch>/k2_files/f<NN>.txt \
  --run-log <out>/control_k2_f<NN>.jsonl --json-out <out>/control_k2_f<NN>.json
```

Nur `--control-files` (Einzeldatei-Liste, eine Zeile aus `control_files.txt`) und die beiden
Ausgabepfade (Laufindex `f01`…`f52` im Dateinamen) variieren je Invocation; jede weitere Zeile
ist wortgleich mit der Registrierung. Arbeitsverzeichnis jeder Invocation: `~/ma/ma-conformance-testrepo` (`repoRoot: process.cwd()`, `cli.ts:78`).

Ein Treiberskript im Sitzungs-Scratchpad hat die 52 Invocationen sequentiell abgesetzt, je Datei
in der Reihenfolge von `control_files.txt`, mit **30 Sekunden Pause** zwischen den Invocationen
(dasselbe Profil wie im Machbarkeitslauf). Das Skript wurde **nicht committet** (Auftragsvorgabe);
sein Ergebnis ist ausschließlich in `data/c3b-k2/` und in diesem Bericht sichtbar.

### Verlauf

| | |
|---|---|
| Start | 2026-08-24T17:08:52+02:00 |
| Ende | 2026-08-24T17:41:54+02:00 |
| Gesamtdauer | **33 min 2 s** |
| Prognose (Machbarkeitslauf §9) | ≈ 35,7 min |
| Invocationen | 52 von 52, alle gültig |
| Wiederholte Invocationen | **0** |
| Einzeldauer je Invocation | min 1,0 s, max 47,6 s, Mittel 11,6 s |
| Exit-Code-Verteilung | Exit 1 (Findings vorhanden): 49 · Exit 0 (0 Findings): 3 |

Die gemessene Gesamtdauer liegt **unter** der Hochrechnung des Machbarkeitslaufs — plausibel,
weil dort die mittlere Einzeldauer aus einer kleinen, tendenziell regelreicheren Stichprobe
(u. a. der regelreichste Datei `catalog_service.py`) hochgerechnet wurde.

### Temperaturprotokoll — Invocation 1, 26, 52

`nvidia-smi` und `ollama ps` während der Ausführung, wörtlich (volle Rohausgabe in
`data/c3b-k2/temperature_log.json`):

| Invocation | Zeitpunkt | GPU-Last | VRAM | Temperatur | Leistung | `ollama ps` |
|---|---|---|---|---|---|---|
| 1 (während) | 17:08:55 | 92 % | 5868 MiB | **58 °C** | 287 W | `qwen2.5-coder:7b`, CONTEXT 4096 |
| 1 (danach) | 17:09:01 | 59 % | 5871 MiB | 60 °C | 272 W | wie oben |
| 26 (während) | 17:25:39 | 91 % | 6060 MiB | **57 °C** | 276 W | wie oben |
| 26 (danach) | 17:25:44 | 65 % | 6060 MiB | 59 °C | 264 W | wie oben |
| 52 (während) | 17:41:49 | 91 % | 5862 MiB | **59 °C** | 283 W | wie oben |
| 52 (danach) | 17:41:54 | 92 % | 5862 MiB | 60 °C | 265 W | wie oben |

**Befund, auf 52er-Skala statt hochgerechnet:** Spitzentemperatur über den gesamten Lauf **60 °C**
— bei Invocation 1 wie bei Invocation 52 identisch, keine Erwärmungstendenz über die 33 Minuten.
Weit unterhalb der 95 °C, an denen der Notebook-Lauf in `data/c3b/` nach dauerhafter Last
thermisch kollabierte. Bestätigt den Machbarkeitsbefund §11 mit vollständiger 52er-Abdeckung
statt einer Fünferstichprobe.

---

## 3. Nachlaufprüfung je Invocation (Protokoll §6 Rev. 26)

### 3a — `calls_total == control_files_count * runs`

Je Invocation lief `tools/postcheck_run.py --mode control --expect-files 1` gegen das jeweilige
`--run-log`/`--json-out`-Paar. **Alle 52 grün:** `control_files_count == 1`, `calls_total == 3`
(`1 * 3 == 3`), `changed_files_count == 0` in jedem der 52 Header. Summiert über alle 52
Invocationen: `calls_total` gesamt = **156** (= 52 × 3), wie erwartet.

### 3b — Exit-Code ist kein Gültigkeitskriterium

Gemessen: Exit 1 bei 49 Invocationen (mindestens ein Finding in mindestens einer Repetition),
Exit 0 bei 3 (0 Findings in allen drei Repetitionen — die drei importfreien/leeren Träger, §4.1).
Gültigkeit wurde ausschließlich an `invalid_reasons`, `calls_invalid`, `calls_transport_failed`
bemessen: **`invalid_reasons: []`, `calls_transport_failed: 0` in allen 52 Footern.**

### 3c — Token-Budget je Call

`tokens_in + tokens_out` gegen die 4096 Token des gemessenen Ollama-Kontextfensters, über alle
156 Calls:

| | |
|---|---|
| Maximum | **2356 Token** (Invocation 21, `src/depot/core/ports.py`, Run-Index 0: 1018 in / 1338 out) |
| Anteil am Fenster | 57,5 % |
| Überschreitungen ≥ 4096 | **0** |

Keine Überschreitung — auch nicht bei der regelreichsten Datei des Control-Sets (`core/ports.py`
trägt viele Signaturen und wird von mehreren Komponenten referenziert, daher der lange
User-Prompt). Der offene Punkt aus dem Machbarkeitslauf §6 (Abschneiden ohne Fehler/Logzeile)
bleibt damit für diese Kampagne **ungetestet in der Grenze**, aber **auf keiner der 156
tatsächlichen Kampagnen-Anfragen eingetreten**.

### 3d — Getrennte Zählung (Protokoll §4 Rev. 25)

| run_index | `DERIVED:`-Records | LLM-Records |
|---|---|---|
| 0 | 0 | 155 |
| 1 | 0 | 153 |
| 2 | 0 | 153 |
| **gesamt** | **0** | **461** |

0 `DERIVED:`-Records in allen drei Läufen — strukturell erwartet, weil `--rule-graph diff` mit
`changed_files_count: 0` dem Regel-Engine eine leere `observedImports`-Menge liefert
(`ruleEngine.ts:76`/`:157` können unter diesen Bedingungen keinen `DERIVED:forbidden-edge`/
`DERIVED:cycle`-Record erzeugen). Alle 461 gemeldeten Findings sind LLM-Records.

### 3e — Unbekannte `rule_id` (B1 D1)

**0 Fälle.** Alle 461 gezählten Findings tragen eine der 16 in `architecture-rules.yaml`
definierten `rule_id`. Auch in den (hier: keinen) verworfenen Versuchen wurde keine unbekannte
`rule_id` gefunden. Kein Lauf ist durch B1 D1 invalidiert.

**Alle 52 Nachlaufprüfungen grün. 0 Wiederholungen nötig — die Wiederaufnahmeregel des Auftrags
(§2) kam nicht zur Anwendung.**

---

## 4. Auswertung — rein deskriptiv

### 4.1 — Je Run-Index: Module mit Finding, Gesamtzahl, Kategorien, Komponenten

| run_index | Module mit ≥1 Finding | Findings gesamt |
|---|---|---|
| 0 | 49 von 52 | 155 |
| 1 | 49 von 52 | 153 |
| 2 | 49 von 52 | 153 |

**Die drei Module ohne jedes Finding in allen drei Läufen:**
`depot.billing.models.legacy_tax_models`, `depot.core.adapters.internal.cache`,
`depot.core.adapters.internal.session` — die importfreie Legacy-Datei und die beiden
Internum-Dateien, die selbst nichts Verbotenes importieren (sie sind das *Ziel* von
`R-PROTECT-1`, nicht dessen Quelle).

**Verteilung über die sechs Kategorien** (identisch in Form über alle drei Läufe, Zahlen s. u.):

| Kategorie | run 0 | run 1 | run 2 |
|---|---|---|---|
| ABSENCE_REQUIRED | 6 | 4 | 4 |
| API_CONTRACT | 7 | 7 | 7 |
| CYCLE | 8 | 8 | 8 |
| FORBIDDEN_RELATION | 95 | 95 | 95 |
| FORBIDDEN_SIGNATURE_TYPE | 21 | 21 | 21 |
| STRUCTURAL_PLACEMENT | 18 | 18 | 18 |

Die einzige Kategorie mit Streuung ist `ABSENCE_REQUIRED` — exakt die zwei zusätzlichen Findings
der vorregistrierten Portregel in Lauf 0 (§4.3).

**Verteilung über die 19 Komponenten** (besetzte, identisch über alle drei Läufe außer
`orders_services`):

| Komponente | run 0 | run 1 | run 2 |
|---|---|---|---|
| billing_api | 3 | 3 | 3 |
| billing_mappers | 2 | 2 | 2 |
| billing_models | 8 | 8 | 8 |
| billing_repository | 5 | 5 | 5 |
| billing_services | 8 | 8 | 8 |
| core | 48 | 48 | 48 |
| core_adapters | 9 | 9 | 9 |
| identity_api | 3 | 3 | 3 |
| identity_mappers | 2 | 2 | 2 |
| identity_models | 6 | 6 | 6 |
| identity_repository | 9 | 9 | 9 |
| identity_services | 4 | 4 | 4 |
| orders_api | 3 | 3 | 3 |
| orders_mappers | 2 | 2 | 2 |
| orders_models | 17 | 17 | 17 |
| orders_repository | 7 | 7 | 7 |
| **orders_services** | **17** | **15** | **15** |
| orders_services_pricing | 2 | 2 | 2 |
| core_adapters_internal (unbesetzt) | 0 | 0 | 0 |

18 von 19 Komponenten mit mindestens einem Finding in jedem Lauf; `core_adapters_internal` bleibt
in allen drei Läufen unbesetzt — sie ist im Regelwerk ausschließlich Ziel (`to`), nie Quelle
(`from`) einer Regel, kann also strukturell nie selbst als meldendes Modul erscheinen.

### 4.2 — Falsch-Positiv-Rate, Median über die drei Läufe (Nenner 52)

| Kennzahl | run 0 | run 1 | run 2 | Median | Spannweite |
|---|---|---|---|---|---|
| Module mit ≥1 Finding | 49 | 49 | 49 | **49** | 49–49 (0) |
| Findings (LLM) gesamt | 155 | 153 | 153 | 153 | 153–155 (2) |

**HEADLINE Falsch-Positiv-Rate (Median Module-mit-Finding / 52): 49/52 = 0,9423.**

Bemerkenswert und ohne Interpretation festgehalten: die Modul-Ebene der Rate streut **nicht**
über die drei Läufe (49 in jedem Lauf), obwohl die Finding-**Zahl** streut (155/153/153) — die
gesamte Streuung entfällt auf ein einziges bereits gemeldetes Modul (`depot.orders.services`,
§4.4), nicht auf ein Umschalten von Modulen zwischen „hat Finding" und „hat keins".

### 4.3 — Die beiden vorregistrierten Meldungen, getrennt geführt

**Adapterfassade `depot.core.adapters` / `R-PROTECT-1`** (§5 Nachtrag Rev. 16)

Aufgetreten in **3 von 3 Läufen**:

| run | `rule_id` | Modul | Komponente | `subject` |
|---|---|---|---|---|
| 0 | R-PROTECT-1 | `depot.core.adapters` | core_adapters | `{"from": "identity_services", "to": "core_adapters_internal"}` |
| 0 | R-PROTECT-1 | `depot.core.adapters` | core_adapters | `{"from": "orders_services", "to": "core_adapters_internal"}` |
| 0 | R-PROTECT-1 | `depot.core.adapters` | core_adapters | `{"from": "billing_services", "to": "core_adapters_internal"}` |
| 1 | R-PROTECT-1 | `depot.core.adapters` | core_adapters | `{"from": "identity_services", "to": "core_adapters_internal"}` |
| 1 | R-PROTECT-1 | `depot.core.adapters` | core_adapters | `{"from": "orders_services", "to": "core_adapters_internal"}` |
| 1 | R-PROTECT-1 | `depot.core.adapters` | core_adapters | `{"from": "billing_services", "to": "core_adapters_internal"}` |
| 2 | R-PROTECT-1 | `depot.core.adapters` | core_adapters | `{"from": "identity_services", "to": "core_adapters_internal"}` |
| 2 | R-PROTECT-1 | `depot.core.adapters` | core_adapters | `{"from": "orders_services", "to": "core_adapters_internal"}` |
| 2 | R-PROTECT-1 | `depot.core.adapters` | core_adapters | `{"from": "billing_services", "to": "core_adapters_internal"}` |

**Nicht-Träger-Portregel auf `orders_services` (R-PORT-2 / R-PORT-3)** (§5 Nachtrag Rev. 18)

Aufgetreten in **1 von 3 Läufen** (Lauf 0):

| run | `rule_id` | Modul | Komponente | `subject` |
|---|---|---|---|---|
| 0 | R-PORT-2 | `depot.orders.services` | orders_services | `{"offending_type": "depot.core.ports.RateProvider"}` |
| 0 | R-PORT-3 | `depot.orders.services` | orders_services | `{"offending_type": "depot.core.ports.PaymentGateway"}` |

Beide Meldungen sind **hier nur gezählt, nicht bewertet** — ob sie die `allowed_importers`-Hälfte
bzw. die einschränkende Hälfte des jeweiligen `statement` korrekt lesen, ist Kapitel-7-Fragestellung.

### 4.4 — Stabilität über die drei Repetitionen

| | |
|---|---|
| Identische Findingmenge in allen drei Läufen | **51 von 52 Modulen** |
| Unterschiedliche Findingmenge | **1 von 52 Modulen** |

Das einzige nicht stabile Modul: **`depot.orders.services`** (Kontrolldatei
`src/depot/orders/services/__init__.py`, Zeile 47 — der zweite inhaltstragende Init-Träger des
Control-Sets, trägt die `CYCLE_PARENT_CHILD`-Kante der Komponente `orders_services`):

| Lauf | Findings (rule_id, subject) |
|---|---|
| 0 | R-CYCLE-2 (orders_services_pricing→orders_services), R-INDEP-1 (orders_services→identity_services), R-LAYER-1 (orders_services_pricing→orders_services), **R-PORT-2** (RateProvider), **R-PORT-3** (PaymentGateway), R-PROTECT-1 (orders_services→core_adapters_internal) |
| 1 | R-CYCLE-2 (orders_services_pricing→orders_services), R-INDEP-1 (**orders_services_pricing**→identity_services), R-LAYER-1 (orders_services_pricing→orders_services), R-PROTECT-1 (**orders_services_pricing**→core_adapters_internal) |
| 2 | identisch mit Lauf 1 |

Zwei unabhängige Achsen der Instabilität an diesem einen Modul: (a) das Auftreten der beiden
vorregistrierten Portregel-Findings nur in Lauf 0 (bereits in §4.3 gezählt), und (b) eine
abweichende `from`-Zuschreibung bei R-INDEP-1/R-PROTECT-1 zwischen Lauf 0
(`orders_services`) und Läufen 1/2 (`orders_services_pricing`) — das Modell attribuiert dieselbe
Verletzungsklasse in verschiedenen Repetitionen unterschiedlichen Komponenten im Scope. Dies ist
die **K2-Seite des Varianzbefunds**, den B36a für K3 gemessen hat (`b36a_bericht_k3_varianzlauf.md`):
auch bei `temperature=0`/`seed=42` ist Ollama/qwen2.5-coder:7b **nicht** deterministisch
reproduzierbar über Repetitionen hinweg. Alle übrigen 51 Kontrollmodule lieferten in allen drei
Läufen exakt dieselbe Findingmenge (gleiche `rule_id` **und** gleiches `subject`).

### 4.5 — Alle übrigen Findings, tabellarisch

150 Findings je Lauf nach Abzug der beiden vorregistrierten Meldungen (155−5 in Lauf 0, 153−3 in
den Läufen 1/2 — alle drei Läufe damit **150 „übrige" Findings**). Läufe 1 und 2 sind bis auf das
in §4.4 dokumentierte eine Modul (`depot.orders.services`) inhaltlich identisch mit Lauf 0; die
Tabelle unten zeigt **Lauf 0** als vollständigen Referenzlauf, die Abweichung der Läufe 1/2 ist
vollständig in §4.4 dokumentiert. Die vollständigen Rohdaten aller drei Läufe liegen unverkürzt
in `data/c3b-k2/runs/`. **Keine Bewertung, ob die Findings berechtigt sind** — das ist Kapitel 7.

| Modul | Komponente | `rule_id` | Kategorie | `subject` |
|---|---|---|---|---|
| `depot.billing.api.routes` | `billing_api` | `R-LAYER-1` | FORBIDDEN_RELATION | from=billing_api to=core |
| `depot.billing.api.routes` | `billing_api` | `R-INDEP-1` | FORBIDDEN_RELATION | from=billing_api to=billing_services |
| `depot.billing.api.schemas` | `billing_api` | `R-LAYER-1` | FORBIDDEN_RELATION | from=billing_api to=core |
| `depot.billing.mappers.invoice_mapper` | `billing_mappers` | `R-INDEP-1` | FORBIDDEN_RELATION | from=billing_mappers to=core |
| `depot.billing.mappers.payment_mapper` | `billing_mappers` | `R-INDEP-1` | FORBIDDEN_RELATION | from=billing_mappers to=core |
| `depot.billing.models.invoice_models` | `billing_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.billing.models.invoice_view_models` | `billing_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.billing.models.invoice_view_models` | `billing_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.billing.models.invoice_view_models` | `billing_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.billing.models.invoice_view_models` | `billing_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.billing.models.payment_models` | `billing_models` | `R-INDEP-1` | FORBIDDEN_RELATION | from=billing_models to=core |
| `depot.billing.models.payment_models` | `billing_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.billing.models.payment_models` | `billing_models` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.billing.models.payment_models |
| `depot.billing.repository.invoice_query` | `billing_repository` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.billing.repository.invoice_query |
| `depot.billing.repository.invoice_query` | `billing_repository` | `R-SIG-3` | API_CONTRACT | offending_type=InvoiceQuery.settled_cents |
| `depot.billing.repository.invoice_repo` | `billing_repository` | `R-LAYER-1` | FORBIDDEN_RELATION | from=billing_repository to=core |
| `depot.billing.repository.invoice_repo` | `billing_repository` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.billing.repository.invoice_repo |
| `depot.billing.repository.legacy_invoice_index` | `billing_repository` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.billing.repository.legacy_invoice_index |
| `depot.billing.services.dunning_service` | `billing_services` | `R-LAYER-1` | FORBIDDEN_RELATION | from=billing_services to=billing_repository |
| `depot.billing.services.dunning_service` | `billing_services` | `R-PROTECT-1` | FORBIDDEN_RELATION | from=billing_services to=core_adapters_internal |
| `depot.billing.services.dunning_service` | `billing_services` | `R-INDEP-1` | FORBIDDEN_RELATION | from=billing_services to=identity_services |
| `depot.billing.services.invoice_service` | `billing_services` | `R-LAYER-1` | FORBIDDEN_RELATION | from=billing_services to=identity_services |
| `depot.billing.services.invoice_service` | `billing_services` | `R-PROTECT-1` | FORBIDDEN_RELATION | from=billing_services to=core_adapters_internal |
| `depot.billing.services.invoice_service` | `billing_services` | `R-INDEP-1` | FORBIDDEN_RELATION | from=billing_services to=identity_services |
| `depot.billing.services.ledger_service` | `billing_services` | `R-LAYER-1` | FORBIDDEN_RELATION | from=billing_services to=billing_repository |
| `depot.billing.services.ledger_service` | `billing_services` | `R-PORT-4` | ABSENCE_REQUIRED | offending_type=depot.core.ports.Clock |
| `depot.core.adapters` | `core_adapters` | `R-CORE-1` | FORBIDDEN_RELATION | from=core_adapters to=identity_services |
| `depot.core.adapters` | `core_adapters` | `R-CORE-1` | FORBIDDEN_RELATION | from=core_adapters to=orders_services |
| `depot.core.adapters` | `core_adapters` | `R-CORE-1` | FORBIDDEN_RELATION | from=core_adapters to=billing_services |
| `depot.core.adapters.storage` | `core_adapters` | `R-PROTECT-1` | FORBIDDEN_RELATION | from=identity_services to=core_adapters_internal |
| `depot.core.adapters.storage` | `core_adapters` | `R-PROTECT-1` | FORBIDDEN_RELATION | from=orders_services to=core_adapters_internal |
| `depot.core.adapters.storage` | `core_adapters` | `R-PROTECT-1` | FORBIDDEN_RELATION | from=billing_services to=core_adapters_internal |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_api |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_mappers |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_models |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_repository |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_services |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_api |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_mappers |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_models |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_repository |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_services |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_services_pricing |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_api |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_mappers |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_models |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_repository |
| `depot.core.config` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_services |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_api |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_mappers |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_models |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_repository |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_services |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_api |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_mappers |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_models |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_repository |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_services |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_services_pricing |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_api |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_mappers |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_models |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_repository |
| `depot.core.errors` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_services |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_api |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_mappers |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_models |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_repository |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=identity_services |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_api |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_mappers |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_models |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_repository |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_services |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=orders_services_pricing |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_api |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_mappers |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_models |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_repository |
| `depot.core.ports` | `core` | `R-CORE-1` | FORBIDDEN_RELATION | from=core to=billing_services |
| `depot.identity.api.routes` | `identity_api` | `R-LAYER-1` | FORBIDDEN_RELATION | from=identity_api to=core |
| `depot.identity.api.routes` | `identity_api` | `R-CYCLE-1` | CYCLE | from=identity_api to=identity_mappers |
| `depot.identity.api.schemas` | `identity_api` | `R-LAYER-1` | FORBIDDEN_RELATION | from=identity_api to=core |
| `depot.identity.mappers.customer_mapper` | `identity_mappers` | `R-CYCLE-1` | CYCLE | from=identity_mappers to=core |
| `depot.identity.mappers.role_mapper` | `identity_mappers` | `R-CYCLE-1` | CYCLE | from=identity_mappers to=core |
| `depot.identity.models.customer_models` | `identity_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.identity.models.customer_models` | `identity_models` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.identity.models.customer_models |
| `depot.identity.models.customer_view_models` | `identity_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.identity.models.customer_view_models` | `identity_models` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.identity.models.customer_view_models |
| `depot.identity.models.role_models` | `identity_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.identity.models.role_models` | `identity_models` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.identity.models.role_models |
| `depot.identity.repository.customer_repo` | `identity_repository` | `R-LAYER-1` | FORBIDDEN_RELATION | from=identity_repository to=core |
| `depot.identity.repository.customer_repo` | `identity_repository` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.identity.repository.customer_repo |
| `depot.identity.repository.customer_repo` | `identity_repository` | `R-SIG-1` | API_CONTRACT | offending_type=CustomerRepository.touch |
| `depot.identity.repository.legacy_token_index` | `identity_repository` | `R-LAYER-1` | FORBIDDEN_RELATION | from=identity_repository to=identity_services |
| `depot.identity.repository.legacy_token_index` | `identity_repository` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.identity.repository.legacy_token_index |
| `depot.identity.repository.legacy_token_index` | `identity_repository` | `R-SIG-1` | API_CONTRACT | offending_type=SessionRepository.touch |
| `depot.identity.repository.session_repo` | `identity_repository` | `R-LAYER-1` | FORBIDDEN_RELATION | from=identity_repository to=core |
| `depot.identity.repository.session_repo` | `identity_repository` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.identity.repository.session_repo |
| `depot.identity.repository.session_repo` | `identity_repository` | `R-SIG-1` | API_CONTRACT | offending_type=SessionRepository.touch |
| `depot.identity.services.customer_service` | `identity_services` | `R-LAYER-1` | FORBIDDEN_RELATION | from=identity_services to=identity_repository |
| `depot.identity.services.customer_service` | `identity_services` | `R-PROTECT-1` | FORBIDDEN_RELATION | from=identity_services to=core_adapters_internal |
| `depot.identity.services.token_service` | `identity_services` | `R-LAYER-1` | FORBIDDEN_RELATION | from=identity_services to=identity_repository |
| `depot.identity.services.token_service` | `identity_services` | `R-PORT-1` | ABSENCE_REQUIRED | offending_type=depot.core.ports.TokenSigner |
| `depot.orders.api.routes` | `orders_api` | `R-LAYER-1` | FORBIDDEN_RELATION | from=orders_api to=core |
| `depot.orders.api.routes` | `orders_api` | `R-CYCLE-1` | CYCLE | from=orders_api to=orders_mappers |
| `depot.orders.api.schemas` | `orders_api` | `R-LAYER-1` | FORBIDDEN_RELATION | from=orders_api to=core |
| `depot.orders.mappers.order_line_mapper` | `orders_mappers` | `R-SIG-4` | API_CONTRACT | offending_type=to_payload |
| `depot.orders.mappers.order_mapper` | `orders_mappers` | `R-SIG-4` | API_CONTRACT | offending_type=to_payload |
| `depot.orders.models.discount_models` | `orders_models` | `R-INDEP-1` | FORBIDDEN_RELATION | from=orders_models to=core |
| `depot.orders.models.discount_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.orders.models.discount_models` | `orders_models` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.orders.models.discount_models |
| `depot.orders.models.order_line_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.orders.models.order_line_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.orders.models.order_line_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.orders.models.order_line_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.orders.models.order_line_models` | `orders_models` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.orders.models.order_line_models |
| `depot.orders.models.order_line_view_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm |
| `depot.orders.models.order_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.orders.models.order_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.orders.models.order_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.orders.models.order_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.orders.models.order_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm.Session |
| `depot.orders.models.order_models` | `orders_models` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.orders.models.order_models |
| `depot.orders.models.order_view_models` | `orders_models` | `R-FRAMEWORK-1` | FORBIDDEN_SIGNATURE_TYPE | offending_type=sqlalchemy.orm |
| `depot.orders.models.order_view_models` | `orders_models` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.orders.models.order_view_models |
| `depot.orders.repository.legacy_order_index` | `orders_repository` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.orders.repository.legacy_order_index |
| `depot.orders.repository.order_line_repo` | `orders_repository` | `R-LAYER-1` | FORBIDDEN_RELATION | from=orders_repository to=core |
| `depot.orders.repository.order_line_repo` | `orders_repository` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.orders.repository.order_line_repo |
| `depot.orders.repository.order_query` | `orders_repository` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.orders.repository.order_query |
| `depot.orders.repository.order_query` | `orders_repository` | `R-SIG-2` | API_CONTRACT | offending_type=OrderQuery.percent_for |
| `depot.orders.repository.order_repo` | `orders_repository` | `R-LAYER-1` | FORBIDDEN_RELATION | from=orders_repository to=core |
| `depot.orders.repository.order_repo` | `orders_repository` | `R-PLACE-1` | STRUCTURAL_PLACEMENT | offending_type=depot.orders.repository.order_repo |
| `depot.orders.services` | `orders_services` | `R-LAYER-1` | FORBIDDEN_RELATION | from=orders_services_pricing to=orders_services |
| `depot.orders.services` | `orders_services` | `R-PROTECT-1` | FORBIDDEN_RELATION | from=orders_services to=core_adapters_internal |
| `depot.orders.services` | `orders_services` | `R-INDEP-1` | FORBIDDEN_RELATION | from=orders_services to=identity_services |
| `depot.orders.services` | `orders_services` | `R-CYCLE-2` | CYCLE | from=orders_services_pricing to=orders_services |
| `depot.orders.services.catalog_service` | `orders_services` | `R-LAYER-1` | FORBIDDEN_RELATION | from=orders_services to=core |
| `depot.orders.services.catalog_service` | `orders_services` | `R-PORT-2` | ABSENCE_REQUIRED | offending_type=depot.core.ports.RateProvider |
| `depot.orders.services.checkout_service` | `orders_services` | `R-LAYER-1` | FORBIDDEN_RELATION | from=orders_services to=orders_repository |
| `depot.orders.services.checkout_service` | `orders_services` | `R-PROTECT-1` | FORBIDDEN_RELATION | from=orders_services to=core_adapters_internal |
| `depot.orders.services.checkout_service` | `orders_services` | `R-CYCLE-2` | CYCLE | from=orders_services_pricing to=orders_services |
| `depot.orders.services.order_service` | `orders_services` | `R-LAYER-1` | FORBIDDEN_RELATION | from=orders_services to=identity_services |
| `depot.orders.services.order_service` | `orders_services` | `R-PROTECT-1` | FORBIDDEN_RELATION | from=orders_services to=core_adapters_internal |
| `depot.orders.services.order_service` | `orders_services` | `R-INDEP-1` | FORBIDDEN_RELATION | from=orders_services to=identity_services |
| `depot.orders.services.order_service` | `orders_services` | `R-CYCLE-2` | CYCLE | from=orders_services_pricing to=orders_services |
| `depot.orders.services.pricing.engine` | `orders_services_pricing` | `R-INDEP-1` | FORBIDDEN_RELATION | from=orders_services_pricing to=core |
| `depot.orders.services.pricing.engine` | `orders_services_pricing` | `R-CYCLE-2` | CYCLE | from=orders_services_pricing to=orders_services |
| `depot.orders.services.refund_service` | `orders_services` | `R-LAYER-1` | FORBIDDEN_RELATION | from=orders_services to=orders_repository |
| `depot.orders.services.refund_service` | `orders_services` | `R-PORT-3` | ABSENCE_REQUIRED | offending_type=depot.core.ports.PaymentGateway |

---

## 5. Ablage

Run-Logs (52 × `.jsonl`), JSON-Ausgaben (52 × `.json`), ein maschinenlesbares Laufmanifest und die
Temperaturaufzeichnung liegen unter [`data/c3b-k2/`](../../data/c3b-k2/) mit `SHA256SUMS` und
`MANIFEST.md` nach der Konvention aus `00_stand_und_entscheidungen.md` §0. `data/c3b/` (der
gescheiterte Notebook-Lauf) bleibt **unverändert** liegen — Beleg für B37 und die
Verlustgranularität, nicht ersetzt durch diesen erfolgreichen Lauf.

Das Manifest führt: die Aufrufzeile, `sha256(dist/cli.js)` und Bauzeitpunkt, die vier
Inhaltshashes, `checker_git_head`, `target_repo_git_head`, Modell-Digest und Quantisierung,
Maschine, Datum, Gesamtdauer, Temperaturprotokoll und die Zahl der wiederholten Invocationen (0).

**Read-only-Nachweis der beiden Fremdrepos**, vor und nach dem gesamten Auftrag:

```
git -C ~/ma/tritongraph status --porcelain            → leer (vor und nach)
git -C ~/ma/ma-conformance-testrepo status --porcelain → leer (vor und nach)
git -C ~/ma/tritongraph rev-parse HEAD                 → 348ca9daa456af4954f11f7152fc45201035297e (unverändert)
git -C ~/ma/ma-conformance-testrepo rev-parse HEAD     → 0d651041ed87dd03f2f78359713633fac01c0a66 (unverändert)
```

Kein Commit, kein Push, keine Quelltextänderung in einem der beiden Fremdrepos während des
gesamten Auftrags.
