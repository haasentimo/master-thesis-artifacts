# MANIFEST — C3b-K3, Rohdaten des Kontrolllaufs über die 52 Kontrollmodule (DigitalOcean-Direktzugang)

**Datum des Laufs:** 25. August 2026, 11:50:16–13:54:48 CEST (2 h 04 min 32 s)
**Bericht:** [`docs/repo-kontext/c3b_k3_bericht_kontrolllauf.md`](../../docs/repo-kontext/c3b_k3_bericht_kontrolllauf.md)
**Protokollbezug:** §5 (Metriken, Falsch-Positiv-Rate, vorregistrierte Meldungen Rev. 16/18),
§6 Nachtrag Rev. 24 (Aufrufspezifikation, Build-Provenienz), Rev. 25 (getrennte Recordmengen),
Rev. 26 (Wiederholungsfaktor, Exit-Code kein Gültigkeitskriterium)
**Vorlauf:** [`k3_machbarkeitslauf_direktzugang_bericht.md`](../../docs/repo-kontext/k3_machbarkeitslauf_direktzugang_bericht.md)
— derselbe Bezugsweg, an fünf Dateien validiert, hier auf alle 52 ausgeführt.

Dieses Verzeichnis enthält die unveränderten Laufdaten von **C3b-K3** über den **Direktzugang bei
DigitalOcean** (`https://inference.do-ai.run/v1`, Modell `nvidia-nemotron-3-super-120b`, kein
Router, kein `CONFORMANCE_PROVIDER_PIN`) — ausgeführt als **52 Einzeldatei-Invocationen** statt der
einen registrierten Mehrdatei-Invocation, aus demselben Grund wie C3b-K2
(`c3b_k2_bericht_kontrolllauf.md` §0, `k2_machbarkeitslauf_bericht.md` §11: Verlustgranularität).
`data/c3b/` (der gescheiterte Notebook-Lauf) und `data/c3b-k2/` (Ollama) bleiben **unverändert**
liegen — dieses Verzeichnis ersetzt keines von beiden.

> **Nicht reproduzierbar. Niemals überschreiben.** LLM-Läufe gegen einen Remote-Endpoint mit
> `temperature=0`/`seed=42` sind auch bei fixem Modellstand nicht bitgleich wiederholbar.

## Aufrufzeile, wörtlich (Vorlage)

Aus Protokoll §6 Rev. 24, Abschnitt „Kontrolllauf K2 und K3 auf B", mit dem im Auftrag
vorgeschriebenen Bezugsweg (Base-URL, Modell-ID, Schlüsselquelle; `CONFORMANCE_PROVIDER_PIN`
entfällt, B32). Je Invocation variiert **nur** `--control-files` (eine Einzeldatei-Liste statt der
vollen `control_files.txt`) und die beiden Ausgabepfade (Laufindex `f01`…`f52` im Dateinamen);
`control_files.txt` selbst wurde an keiner Stelle verändert.

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

Arbeitsverzeichnis jeder Invocation: `~/ma/ma-conformance-testrepo` (bei Tag `baseline`), Grund
siehe `k3_machbarkeitslauf_direktzugang_bericht.md` §3 (`repoRoot: process.cwd()`, `cli.ts:78`).
`<scratch>` ist der Sitzungs-Scratchpad des ausführenden Auftrags, nicht Teil dieses Repos; das
Feld `cli_args` in jedem `run_header` unten trägt den tatsächlichen absoluten Pfad, der die
Sitzung überlebt hat, weil er in den Rohdaten steht — er ist informativ, kein Zitierpfad.

Ein Orchestrator-Skript im Sitzungs-Scratchpad hat die 52 Invocationen sequentiell abgesetzt, je
Datei in der Reihenfolge von `control_files.txt`, mit **30 Sekunden Pause** zwischen den
Invocationen. Das Skript wurde **nicht committet** (Auftragsvorgabe); sein Ergebnis ist
ausschließlich in diesem Verzeichnis und im Bericht sichtbar.

## Build-Provenienz des ausgeführten Codes (Protokoll §1 Nachtrag Rev. 24)

| Feld | Wert |
|---|---|
| `checker_dist_cli_sha256` | `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` |
| `checker_build_timestamp` | `2026-08-25T11:47:16+02:00`, esbuild 12 ms (praktisch augenblicklich) |
| `checker_git_status_porcelain` | leer, vor **und** nach dem Build, sowie vor **und** nach allen 52 Invocationen (außer dem gitignorierten `dist/`) |
| `checker_git_head` | `348ca9daa456af4954f11f7152fc45201035297e` |
| `target_repo_git_head` | `0d651041ed87dd03f2f78359713633fac01c0a66` (Tag `baseline`) |
| `target_repo_git_status_porcelain` | leer, vor **und** nach allen 52 Invocationen |

## Die vier Inhaltshashes, in allen 52 `run_header` zeichengleich

| Feld | Wert |
|---|---|
| `topology_sha256` | `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` |
| `rules_sha256` | `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` |
| `prompt_template_sha256` | `65e78f38e7b1fee20000ea70c654df042f5e0831fc6a68ccb340f833bd915035` |
| `user_prompt_render_sha256` | `45780c70c486ea8f608d1b2ca11178049a02b7a6ece9ba33fcdc8d1b815b03ef` |

## Modell und Bezugsweg

| Feld | Wert |
|---|---|
| `model_requested` | `nvidia-nemotron-3-super-120b` |
| `endpoint` | `https://inference.do-ai.run/v1` |
| `provider_pin` | `null` (kein Router, `CONFORMANCE_PROVIDER_PIN` unbenannt — B32 gegenstandslos) |
| `temperature_requested` / `seed_requested` | `0` / `42`, unverändert gegenüber der Registrierung |
| `runs_requested` | `3` |
| `timeout_ms` | `600000` |

## Wiederaufnahme und 429-Statistik — Kernkennzahl für die Durchführbarkeit

**52 von 52 Kontrollmodulen liegen als gültiges Ergebnis vor. 2 Invocationen benötigten eine
zweite Runde; nach der zweiten Runde ist keine Datei mehr offen.**

| | Runde 1 (52 Invocationen) | Runde 2 (2 Wiederholungen) |
|---|---|---|
| HTTP 429 | 8 | 0 |
| HTTP 5xx | 1 | 0 |
| Transport-Retry griff (Call am Ende gültig) | 3 | 0 |
| Transport-Retry reichte nicht (Call dauerhaft verloren) | 2 | 0 |

Die beiden dauerhaft verlorenen Calls aus Runde 1 — `src/depot/identity/repository/session_repo.py`
(`run_index 1`, drei aufeinanderfolgende 429, Transport-Retry-Budget erschöpft) und
`src/depot/identity/services/customer_service.py` (`run_index 0`, ebenso drei aufeinanderfolgende
429) — sind die einzigen beiden Invocationen, deren `invalid_reasons` in Runde 1 nicht leer war;
beide liefen in Runde 2 vollständig und ohne jede Transportstörung durch. Das im gezählten Ergebnis
(unten, `runs/`) archivierte Paar für diese beiden Dateien ist **ausschließlich Runde 2** — Runde 1
ist nicht Teil der Zählung, wird aber vollständig in `run_manifest.json` (Feld `attempt: 1`) und im
Bericht (§2, §3g) mitgeführt. Die einzige weitere Transportstörung des gesamten Laufs betraf
`src/depot/identity/api/routes.py` (`run_index 1`, ein einzelnes HTTP 5xx, sofort per Retry
behoben) — dieser Call zählt in der Zählung als `calls_with_transport_retry`, nicht als
`transport_failed`, und bleibt Teil von Runde 1.

## Zählungen — Zusammenfassung (Details im Bericht §3–§4)

| | Wert |
|---|---|
| `calls_total` (gezählt, 52 × 3) | 156 |
| `calls_invalid` | 0 |
| `calls_transport_failed` (gezähltes Ergebnis) | 0 |
| `calls_with_transport_retry` (gezähltes Ergebnis) | 1 |
| unbekannte `rule_id` | 0 |
| `DERIVED:`-Records | 0 |
| LLM-Records | 156 |
| Findings gesamt (drei Läufe) | 3 (run 0: 2, run 1: 1, run 2: 0) |
| Falsch-Positiv-Rate (Median, Nenner 52) | 1/52 ≈ 0,0192 |
| Vorregistrierte Meldung Rev. 16 (Fassade, R-PROTECT-1) | 0 von 3 Läufen |
| Vorregistrierte Meldung Rev. 18 (Nicht-Träger-Portregel, `orders_services`) | 0 von 3 Läufen |
| Token gesamt (in/out) | 170 880 / 88 758 |
| Kosten (0,30 $/1M in, 0,65 $/1M out) | 0,051264 $ + 0,057693 $ = **0,108957 $** |

## Inhalt

- `runs/control_k3_f01.jsonl` … `runs/control_k3_f52.jsonl` — Run-Logs, ein `run_header`, 3×
  `llm_call`, ein `run_footer` je Datei; für `f31` und `f32` ist dies die **zweite** (gültige)
  Ausführung, siehe oben.
- `runs/control_k3_f01.json` … `runs/control_k3_f52.json` — die zugehörigen JSON-Ergebnisdokumente.
- `run_manifest.json` — maschinenlesbares Orchestrator-Protokoll **beider** Runden (54 Einträge:
  52 aus Runde 1, 2 aus Runde 2), mit Zeitstempeln, Exit-Codes und dem vollständigen `run_footer`
  je Invocation.
- `SHA256SUMS` — Prüfsummen aller Dateien in diesem Verzeichnis außer sich selbst und dieser
  `MANIFEST.md`.

## Integrität

```
$ sha256sum -c SHA256SUMS
… (105 Zeilen OK)
```

**Read-only-Nachweis der beiden Fremdrepos**, vor und nach dem gesamten Auftrag:

```
git -C ~/ma/tritongraph status --porcelain            → leer (vor und nach)
git -C ~/ma/ma-conformance-testrepo status --porcelain → leer (vor und nach)
git -C ~/ma/tritongraph rev-parse HEAD                 → 348ca9daa456af4954f11f7152fc45201035297e (unverändert)
git -C ~/ma/ma-conformance-testrepo rev-parse HEAD     → 0d651041ed87dd03f2f78359713633fac01c0a66 (unverändert)
```

Kein Commit, kein Push, keine Quelltextänderung in einem der beiden Fremdrepos während des
gesamten Auftrags.
