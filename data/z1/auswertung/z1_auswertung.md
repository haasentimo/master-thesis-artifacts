# Z1 — Auswertungsausgabe (maschinell erzeugt)

Erzeugt: 2026-08-31T22:04:57+00:00 · `tools/evaluate_z1.py`
Extractor-`HEAD`: `5c0b65a82cc3d8af47c022d779ff63d8a20a9e08` · Protokoll Rev. 5, SHA256 `a6a42f3a65b62a73…`

> **Diese Datei rechnet nichts.** Jede Treue- und Kompressionszahl kommt aus
> `llm_arch.eval.metrics`, jedes Gültigkeitsverdikt aus `llm_arch.ilograph.validate`,
> beide unverändert aus dem Extractor importiert.

## 1. Ergebnistabelle (Protokoll §7.1)

| Kennzahl | Ansatz 1 — Triton (deterministisch, ein Wert) | Ansatz 2 — K2 `qwen2.5-coder:7b` | Ansatz 2 — K3 `nvidia-nemotron-3-super-120b` |
|---|---|---|---|
| `relation_precision` | **1.0** | *nicht erhoben* | *nicht erhoben* |
| `relation_recall` | **1.0** | *nicht erhoben* | *nicht erhoben* |
| `module_coverage` | **1.0** | *nicht erhoben* | *nicht erhoben* |
| `phantom_modules` | **0** | *nicht erhoben* | *nicht erhoben* |
| `module_count` | **11** | *nicht erhoben* | *nicht erhoben* |
| `component_count` | **4** | *nicht erhoben* | *nicht erhoben* |
| `module_compression` | **2.75** | *nicht erhoben* | *nicht erhoben* |
| `import_edge_count` | **16** | *nicht erhoben* | *nicht erhoben* |
| `component_relation_count` | **5** | *nicht erhoben* | *nicht erhoben* |
| `relation_compression` | **3.2** | *nicht erhoben* | *nicht erhoben* |
| `gold_similarity` *(gold-bezogen, Referenzsignal)* | **1.0** | *nicht erhoben* | *nicht erhoben* |
| `valid_raw` / `valid_final` / `attempts_used` | *entfällt — kein Lauf* | `false` / `false` / 3 in allen sechs | `false` / `false` / 3 in allen sechs |

**„nicht erhoben" ist kein Nullwert** (Protokoll §5.4). Auf ungültiger Ausgabe wird
keine Treue gemessen; die Zellen tragen deshalb keine Zahl, auch keine 0.

## 2. E1 und E2 — die gehashten Festlegungen

Alle zehn Werte treffen `tests/test_reader.py:53-73` **zeichengleich**. E1 und E2 sind **BESTÄTIGT**.

## 3. Ansatz 2 je Bedingung — Gültigkeit, Zähler, Ursache

### K2 · `qwen2.5-coder:7b` · Profil `ollama`, Fenster 16384

- Läufe: **6**, davon gültig: **0** → **NICHT ERHOBEN**
- `arch_model.json` über alle Läufe bytegleich: **ja** (ein Hash über 6 Läufe)
- Läufe mit `relation:`-Fehlern in irgendeinem Versuch: **6 von 6** (im Endversuch: 6)
- `validate_arch`-Gegenprobe gegen `meta.json`: **abweichungsfrei**
- **Gegenprobe `compare_runs.py`** (Blob `c6db316b3904…`, unverändert): `output byte-identical: True` · `validity_rate(valid_final): 0.00` — deckungsgleich mit der Zeile darüber

| Slot | `run_index` | `valid_raw`/`valid_final` | Versuche | Fehler (Endversuch) | Klassen | Komp. | Rel. | Moduleinträge | `arch_model` sha256 | `prompt_tokens` | `latency_ms` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `run0` | 0 | nein / nein | 3 | 26 | relation:26 | 5 | 13 | 15 | `96a645677397…` | 6685 | 9166 |
| `run0_w1` | 0 | nein / nein | 3 | 26 | relation:26 | 5 | 13 | 15 | `96a645677397…` | 6685 | 9449 |
| `run0_w2` | 0 | nein / nein | 3 | 26 | relation:26 | 5 | 13 | 15 | `96a645677397…` | 6685 | 9427 |
| `run0_w3` | 0 | nein / nein | 3 | 26 | relation:26 | 5 | 13 | 15 | `96a645677397…` | 6685 | 9372 |
| `run1` | 1 | nein / nein | 3 | 26 | relation:26 | 5 | 13 | 15 | `96a645677397…` | 6685 | 9351 |
| `run2` | 2 | nein / nein | 3 | 26 | relation:26 | 5 | 13 | 15 | `96a645677397…` | 6685 | 9332 |

### K3 · `nvidia-nemotron-3-super-120b` · Profil `digitalocean`

- Läufe: **6**, davon gültig: **0** → **NICHT ERHOBEN**
- `arch_model.json` über alle Läufe bytegleich: **nein** (6 verschiedene Hashes über 6 Läufe)
- Läufe mit `relation:`-Fehlern in irgendeinem Versuch: **2 von 6** (im Endversuch: 1)
- `validate_arch`-Gegenprobe gegen `meta.json`: **abweichungsfrei**
- **Gegenprobe `compare_runs.py`** (Blob `c6db316b3904…`, unverändert): `output byte-identical: False` · `validity_rate(valid_final): 0.00` — deckungsgleich mit der Zeile darüber

| Slot | `run_index` | `valid_raw`/`valid_final` | Versuche | Fehler (Endversuch) | Klassen | Komp. | Rel. | Moduleinträge | `arch_model` sha256 | `prompt_tokens` | `latency_ms` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `run0` | 0 | nein / nein | 3 | 11 | completeness:11 | 4 | 5 | 0 | `7849acc362cb…` | 5811 | 69852 |
| `run0_w1` | 0 | nein / nein | 3 | 11 | completeness:11 | 5 | 5 | 0 | `1ec41e36b5ed…` | 5823 | 30747 |
| `run0_w2` | 0 | nein / nein | 3 | 11 | completeness:11 | 4 | 0 | 0 | `e8c4085eb104…` | 5763 | 65188 |
| `run0_w3` | 0 | nein / nein | 3 | 19 | completeness:11, relation:8 | 1 | 5 | 0 | `fcdaf709b728…` | 5517 | 160210 |
| `run1` | 1 | nein / nein | 3 | 11 | completeness:11 | 4 | 5 | 0 | `c716ac82fe32…` | 5883 | 84278 |
| `run2` | 2 | nein / nein | 3 | 11 | completeness:11 | 4 | 5 | 0 | `a869604da7bc…` | 5793 | 55330 |

### K2 (Altblock) · Fenster 4096 — LIEFERAUSFALL

- Läufe: **6**, davon gültig: **0** → **NICHT ERHOBEN**
- `arch_model.json` über alle Läufe bytegleich: **ja** (ein Hash über 6 Läufe)
- Läufe mit `relation:`-Fehlern in irgendeinem Versuch: **0 von 6** (im Endversuch: 0)
- `validate_arch`-Gegenprobe gegen `meta.json`: **abweichungsfrei**
- **Gegenprobe `compare_runs.py`** (Blob `c6db316b3904…`, unverändert): `output byte-identical: True` · `validity_rate(valid_final): 0.00` — deckungsgleich mit der Zeile darüber

| Slot | `run_index` | `valid_raw`/`valid_final` | Versuche | Fehler (Endversuch) | Klassen | Komp. | Rel. | Moduleinträge | `arch_model` sha256 | `prompt_tokens` | `latency_ms` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `run0` | 0 | nein / nein | 3 | 11 | completeness:11 | 11 | 11 | 0 | `12ad74ecbe7c…` | 2086 | 14621 |
| `run0_w1` | 0 | nein / nein | 3 | 11 | completeness:11 | 11 | 11 | 0 | `12ad74ecbe7c…` | 2086 | 14830 |
| `run0_w2` | 0 | nein / nein | 3 | 11 | completeness:11 | 11 | 11 | 0 | `12ad74ecbe7c…` | 2086 | 14706 |
| `run0_w3` | 0 | nein / nein | 3 | 11 | completeness:11 | 11 | 11 | 0 | `12ad74ecbe7c…` | 2086 | 14652 |
| `run1` | 1 | nein / nein | 3 | 11 | completeness:11 | 11 | 11 | 0 | `12ad74ecbe7c…` | 2086 | 13909 |
| `run2` | 2 | nein / nein | 3 | 11 | completeness:11 | 11 | 11 | 0 | `12ad74ecbe7c…` | 2086 | 14622 |

## 4. Kontextfenster — EXTRAPOLATION, keine Messung

Zählgatter gegen die bereits archivierten Ollama-Zählungen:

| Gatter | Gegenstand | Soll | Ist | Quelle |
|---|---|---|---|---|
| G1 | attempt_0/prompt.txt mit Chat-Template | `4281` | `4281` | Z1-Protokoll §3.3 (6) |
| G2 | dieselbe Datei ohne Template | `4274` | `4274` | z1_t_bericht_kontextfenster.md §1.1 |
| G3 | k2_trunkiert attempt_2 ohne Template | `6010` | `6010` | Z1-Protokoll §3.3 (6), Tabelle |
| G4 | die drei Versuchsprompts des Blocks k2/, mit Template | `[4281, 5483, 6685]` | `[4281, 5483, 6685]` | data/z1/MANIFEST.md (= usage.prompt_tokens der Artefakte) |

| Teil | Zeichen | Token |
|---|---|---|
| konstanter Systemteil (Systemtext + ChatML-Marken + Nutzertextrahmen) | 1772 | **365** |
| Faktenteil (die 16 JSON-Einträge) | 17048 | **3916** |
| **gerenderter Prompt gesamt** | 18842 | **4281** |

**Token je Modul:** 3916 / 11 = **356.0** Token je substanziellem Modul.

| Schwelle | erste Modulzahl darüber | Token dort |
|---|---|---|
| 4096 | **11** | 4281.0 |
| 16384 | **45** | 16385.0 |
| 32768 | **92** | 33117.0 |

**Annahmen, offengelegt:**

- Linearität: der Faktenteil wächst proportional zur Modulzahl.
- Gleichverteilte Modulgrösse: jedes Modul kostet den Mittelwert dieser Fixture.
- rich_repo als Maßstab: Docstring-Dichte, Signaturlänge und Importzahl dieser Fixture gelten als typisch; ein anderes Repo verschiebt den Wert je Modul.
- Der konstante Rahmen enthält den Systemtext, den Nutzertextrahmen und die ChatML-Marken; er wächst nicht mit der Modulzahl.
- Gerechnet ist der ERSTE Versuch. Die Retry-Konversation wächst darüber hinaus (hier 4 281 → 5 483 → 6 685 Token); die Schwellen sind insofern optimistisch.

