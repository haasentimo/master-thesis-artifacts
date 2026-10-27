# MANIFEST — C3b-K2, Rohdaten des Kontrolllaufs über die 52 Kontrollmodule (Ollama)

**Datum des Laufs:** 24. August 2026, 17:08:52–17:41:54 CEST (33 min 2 s)
**Bericht:** [`docs/repo-kontext/c3b_k2_bericht_kontrolllauf.md`](../../docs/repo-kontext/c3b_k2_bericht_kontrolllauf.md)
**Protokollbezug:** §5 (Metriken, Falsch-Positiv-Rate, vorregistrierte Meldungen Rev. 16/18),
§6 Nachtrag Rev. 24 (Aufrufspezifikation, Build-Provenienz), Rev. 25 (getrennte Recordmengen),
Rev. 26 (Wiederholungsfaktor in den Akzeptanzregeln, Exit-Code kein Gültigkeitskriterium)
**Vorlauf:** [`docs/repo-kontext/k2_machbarkeitslauf_bericht.md`](../../docs/repo-kontext/k2_machbarkeitslauf_bericht.md)
— dieselbe Maschine, dasselbe Muster (Einzeldatei-Zerlegung, 30-Sekunden-Pause), an fünf
Dateien validiert, hier auf alle 52 ausgeführt.

Dieses Verzeichnis enthält die unveränderten Laufdaten von **C3b-K2** — der Ollama-Hälfte des
Kontrolllaufs, ausgeführt als **52 Einzeldatei-Invocationen** statt der einen registrierten
Mehrdatei-Invocation (Begründung im Bericht §2: Verlustgranularität, validiert im
Machbarkeitslauf). **Alle 52 Invocationen sind gültig, keine Wiederholung nötig.**
`data/c3b/` (der gescheiterte Notebook-Lauf) bleibt unverändert liegen — dieses Verzeichnis
ersetzt es nicht, sondern ist der erste erfolgreiche Kontrolllauf der Kampagne.

> **Nicht reproduzierbar. Niemals überschreiben.** LLM-Läufe gegen einen lokalen Ollama-Endpoint
> mit `temperature=0`/`seed=42` sind auch bei fixem Modellstand nicht bitgleich wiederholbar.

## Aufrufzeile, wörtlich (Vorlage)

Aus Protokoll §6 Rev. 24, Abschnitt „K2, Ollama" / „Kontrolllauf K2 und K3 auf B". Je Invocation
variiert **nur** `--control-files` (eine Einzeldatei-Liste statt der vollen `control_files.txt`)
und die beiden Ausgabepfade (Laufindex `f01`…`f52` im Dateinamen); `control_files.txt` selbst
wurde an keiner Stelle verändert.

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

Arbeitsverzeichnis jeder Invocation: `~/ma/ma-conformance-testrepo` (bei Tag `baseline`), Grund
siehe `k2_machbarkeitslauf_bericht.md` §3 (`repoRoot: process.cwd()`, `cli.ts:78`).
`<scratch>` ist der Sitzungs-Scratchpad des ausführenden Auftrags, nicht Teil dieses Repos;
das Feld `cli_args` in jedem `run_header` unten trägt den tatsächlichen absoluten Pfad, der die
Sitzung überlebt hat, weil er in den Rohdaten steht — er ist informativ, kein Zitierpfad.

## Build-Provenienz des ausgeführten Codes (Protokoll §1 Nachtrag Rev. 24)

| Feld | Wert |
|---|---|
| `checker_dist_cli_sha256` | `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` |
| `checker_build_timestamp` | `2026-08-24T17:06:31+02:00` (Beginn) – `2026-08-24T17:06:32+02:00` (Ende), esbuild 14 ms |
| `checker_git_status_porcelain` | leer, vor **und** nach dem Build, sowie vor **und** nach allen 52 Invocationen (außer dem gitignorierten `dist/`) |
| `checker_git_head` | `348ca9daa456af4954f11f7152fc45201035297e` |
| `target_repo_git_head` | `0d651041ed87dd03f2f78359713633fac01c0a66` (Tag `baseline`) |
| `target_repo_git_status_porcelain` | leer, vor **und** nach allen 52 Invocationen |

`c0bbdfeb…` ist SHA256-identisch mit dem im Machbarkeitslauf gebauten `dist/cli.js**` und mit den
vier Bauten des gescheiterten Notebook-Laufs (`data/c3b/MANIFEST.md`) — derselbe Quellstand
`348ca9d` erzeugt auf drei verschiedenen Maschinen dasselbe Artefakt.

## Die vier Inhaltshashes, in allen 52 `run_header` zeichengleich

```
topology_sha256           e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d
rules_sha256              72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95
prompt_template_sha256    65e78f38e7b1fee20000ea70c654df042f5e0831fc6a68ccb340f833bd915035
user_prompt_render_sha256 45780c70c486ea8f608d1b2ca11178049a02b7a6ece9ba33fcdc8d1b815b03ef
```

Zeichengleich mit `c3a_bericht_clean_state_audit.md` §2c, `data/c3b/MANIFEST.md` und
`data/soll/SHA256SUMS`, soweit dort geführt.

## Modell und Umgebung

| Feld | Wert |
|---|---|
| Modell | `qwen2.5-coder:7b`, Digest `dae161e27b0e`, Quantisierung Q4_K_M (7,6 B Parameter) |
| Ollama | 0.32.15 |
| Endpoint | `http://localhost:11434/v1` |
| `CONFORMANCE_PROVIDER_PIN` | nicht gesetzt (K2 läuft lokal, kein Provider-Routing) |
| `temperature_requested` / `seed_requested` | 0 / 42 (aus `cli.ts:37-39`, in jedem `run_header` bestätigt) |
| Kontextfenster (gemessen) | `ollama ps` → `CONTEXT 4096` während der gesamten Laufzeit (Modellgrenze laut `ollama show`: 32768) |
| Maschine | AMD Ryzen 5 5600X (6C/12T), 15 GiB RAM, NVIDIA GeForce RTX 3070 Ti (8192 MiB VRAM), Treiber 596.49, CUDA 13.2 |
| OS / Kernel | Ubuntu 24.04.1 LTS, `5.15.153.1-microsoft-standard-WSL2` (WSL2) |
| Node / Python | v22.23.2 / 3.12.3 |
| Datum | 24. August 2026 |
| Gesamtdauer | 17:08:52–17:41:54 CEST = **33 min 2 s** (Prognose aus dem Machbarkeitslauf: ≈35,7 min, §9 dort) |

Dieselbe Maschine wie der Machbarkeitslauf (`k2_machbarkeitslauf_bericht.md`), nicht dieselbe wie
der gescheiterte Notebook-Lauf in `data/c3b/` (Dell Inspiron, thermischer Kollaps bei 53 min
Dauerlast).

## Temperaturprotokoll — Invocation 1, 26, 52

`nvidia-smi` und `ollama ps` während der Ausführung (roher Auszug in `temperature_log.json`,
volle Ausgabe dort; hier die GPU-Last-Zeile und `ollama ps`-Zeile):

| Invocation | Zeitpunkt | GPU-Last | VRAM | Temperatur | Leistung | `ollama ps` |
|---|---|---|---|---|---|---|
| 1 (während) | 17:08:55 | 92 % | 5868 MiB | 58 °C | 287 W | `CONTEXT 4096` |
| 1 (danach) | 17:09:01 | 59 % | 5871 MiB | 60 °C | 272 W | wie oben |
| 26 (während) | 17:25:39 | 91 % | 6060 MiB | 57 °C | 276 W | wie oben |
| 26 (danach) | 17:25:44 | 65 % | 6060 MiB | 59 °C | 264 W | wie oben |
| 52 (während) | 17:41:49 | 91 % | 5862 MiB | 59 °C | 283 W | wie oben |
| 52 (danach) | 17:41:54 | 92 % | 5862 MiB | 60 °C | 265 W | wie oben |

**Befund:** Spitzentemperatur über den gesamten Lauf **60 °C**, bei Invocation 1 wie bei
Invocation 52 — keine Erwärmungstendenz über die 33 Minuten. Bestätigt die Prognose aus dem
Machbarkeitslauf §11 auf 52er-Skala statt an fünf Stichproben.

## Akzeptanzregeln und Zählungen — Zusammenfassung (Details im Bericht §3)

| Prüfpunkt | Ergebnis |
|---|---|
| `control_files_count == calls_total` je Invocation (Rev. 26: `== 1 * 3`) | alle 52 grün (`tools/postcheck_run.py --mode control --expect-files 1`) |
| `changed_files_count` | 0 in allen 52 Headern |
| `calls_total` gesamt | 156 (= 52 × 3) |
| `invalid_reasons` | `[]` in allen 52 Footern |
| Token-Budget je Call (`tokens_in + tokens_out`) | Maximum 2356 (Invocation 21, `core/ports.py`, run 0), keine Überschreitung von 4096 |
| `DERIVED:`-Records | 0 (erwartet, `changed_files_count = 0` in allen Läufen) |
| LLM-Records gesamt | 461 (155 / 153 / 153 über die drei Run-Indizes) |
| unbekannte `rule_id` | 0 |
| wiederholte Invocationen | 0 |

## Inhalt

| Datei/Verzeichnis | Beschreibung |
|---|---|
| `runs/control_k2_f01.jsonl` … `f52.jsonl` | Run-Logs, eine je Invocation (Header + 3 `llm_call` + Footer) |
| `runs/control_k2_f01.json` … `f52.json` | JSON-Ausgaben, eine je Invocation (`runs[0..2].findings`) |
| `run_manifest.json` | Maschinenlesbares Laufmanifest: Start/Ende je Invocation, Exit-Code, Dauer, Postcheck-Ergebnis, `valid`-Flag |
| `temperature_log.json` | Rohe `nvidia-smi`/`ollama ps`-Ausgaben zu Invocation 1, 26, 52 (während und danach) |
| `SHA256SUMS` | Prüfsummen aller Dateien oben (nicht von `README.md`/`MANIFEST.md`) |

Die Zuordnung Dateiindex → Kontrolldatei folgt der Zeilenreihenfolge in
`data/soll/control_files.txt` (Zeile 1 = `f01`, … Zeile 52 = `f52`); `control_files.txt` selbst
wurde an keiner Stelle verändert und ist nicht Teil dieses Verzeichnisses.

## Integrität

```bash
cd data/c3b-k2 && sha256sum -c SHA256SUMS
```
