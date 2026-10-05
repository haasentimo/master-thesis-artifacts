# MANIFEST — Rohbestand der Konformitätskampagne (K1–K5)

**Auftrag:** C10 / C10a / C10b · **Datum:** 27. August 2026
**Berichte:** [`docs/repo-kontext/c10_bericht_kampagne.md`](../../docs/repo-kontext/c10_bericht_kampagne.md) ·
[`docs/repo-kontext/c10a_bericht_validator_punkt6.md`](../../docs/repo-kontext/c10a_bericht_validator_punkt6.md)

> ~~**Stand: vier von fünf Blöcken vollständig.** K3 ist offen — 22 von 32 gültig~~ ·
> ~~29 von 32 gültig, 3 ohne gültigen Lauf (I09, I11, I23), fortgeschrieben am 28.08.2026
> durch C10c~~ — **Stand 28.08.2026 (C10d): ALLE FÜNF BLÖCKE VOLLSTÄNDIG.** K1, K2, K3, K4
> und K5 tragen je **32 von 32** gültigen Injektionsläufen. Einzelheiten zum Weg dorthin —
> 29 ungültige K3-Invocationen, durchgehend Ratelimit (HTTP 429), kein einziger Call mit
> ungültiger Antwort — in [`k3/MANIFEST.md`](k3/MANIFEST.md).
>
> **Vorbehalt zu K3:** die 32 gültigen Läufe stammen aus **fünf Zeitfenstern über zwei Tage**
> (27.08. 09:00/10:00/12:00, 28.08. 08:00/09:00 CEST); der Endpunkt ist nicht gepinnt und
> seine Auslastung nicht gemessen. **T14 (§9) ist bei jeder Auswertung mitzuführen.**

> **Nicht reproduzierbar. Niemals überschreiben.** Wiederholungen liegen auf `_r<n>`-Pfaden
> neben dem Erstversuch.

> **Keine Auswertung.** Rohbestand. Metriken, Findingbeurteilung und Vergleiche gehören nach
> C6b; die Eine-Iteration-Regel (§7) und die Amendment-Sperre aus §0.1 gelten.

## Messstand (§0.1, eingefroren)

| Grösse | Wert |
|---|---|
| **Protokoll** | `docs/protokolle/eval_protokoll_phase04.md`, **Rev. 35** · SHA256 `876680b13c568312059d9143b146617b3be6887e5e89a2badfd05c5361f3b910` (Anker der Vorregistrierung bleibt Rev. 33, `2cb0385f…17ac181e`) |
| **Auswertungsspezifikation** | `docs/protokolle/c6_auswertungsspezifikation.md` = `2f1354bbabdfaef8c858a6726521e224c30d6293513d83ea98cd1ef3f6608f97` |
| **Messeingänge** | die sieben Dateien aus `data/soll/SHA256SUMS`, `sha256sum -c` 7 von 7 OK |
| **Topologie-Hash** | `topology_sha256` = `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` |
| **Regel-Hash** | `rules_sha256` = `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` |
| **Prompt-Hash** | `prompt_template_sha256` = `65e78f38e7b1fee20000ea70c654df042f5e0831fc6a68ccb340f833bd915035` |
| **Checker** | `phase04-freeze` = `348ca9daa456af4954f11f7152fc45201035297e`, Messpfad `~/ma/tritongraph-measure` |
| **Checker-Artefakt** | `dist/cli.js` = `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` |
| **Runner** | `4caf083d5e21f36440579af6888513ca897f1dd4` (Amendment Rev. 35) |
| **Testrepo** | `baseline` = `0d651041ed87dd03f2f78359713633fac01c0a66`, 32 Tags `inj/01`–`inj/32`, sternförmig |
| **Archivwurzel** | `data/campaign/` (Amendment Rev. 34) |

## Die fünf Blöcke

| Block | Werkzeug / Modell | Läufe | Invocationen | Gültig | Wanduhr | Stand |
|---|---|---|---|---|---|---|
| **K1** | Checker, deterministischer Pfad | `--runs 1` | 32 | **32 / 32** | 2 513 ms | vollständig |
| **K2** | Checker + Ollama `qwen2.5-coder:7b` | `--runs 3` | 32 | **32 / 32** | 252 155 ms | vollständig |
| **K3** | Checker + DO `nvidia-nemotron-3-super-120b` | `--runs 3` | 61 (inkl. Wiederholungen) | **32 / 32** | 9 190 542 ms | vollständig ᵀ |
| **K4** | import-linter 2.13 (grimp 3.15) | — | 32 | **32 / 32** | 3 621 ms | vollständig |
| **K5** | PyTestArch 4.0.1 | — | 32 | **32 / 32** | 9 917 ms | vollständig |

ᵀ **K3 ist vollständig, aber über fünf Zeitfenster verteilt entstanden** — 29 der 61
Invocationen sind am Ratelimit gescheitert und wurden nach §7 wiederholt, ohne dass am
Werkzeug etwas geändert wurde. **T14 (§9) gilt.** Einzelheiten in `k3/MANIFEST.md`.

Gültigkeit entscheidet allein `tools/postrun_check.py` (§6 Nachtrag Rev. 24); der Exit-Code
ist **kein** Kriterium (Rev. 26).

## Graphmodus (§6 Nachtrag Rev. 31)

**K1** leitet den Modus aus `category_l1` ab — **4 × `full`** (I13–I16, die `CYCLE`-Injektionen),
**28 × `diff`**; Quelle im Laufmanifest: `derived from category_l1`. **K2/K3** tragen
durchgehend `diff`. **K4/K5** kennen den Schalter nicht.

## Positive Akzeptanzregel (Rev. 32)

| Regel | Erwartet | Gemessen |
|---|---|---|
| **K4** | `kept + broken` = 13 ausgewertete Contracts | **13 in allen 32 Aufrufen** |
| **K5** | 24 gesammelte Tests, Sammelphase fehlerfrei | **24 in allen 32 Aufrufen**, keine Sammelfehler |

Die **Trefferzahlen** sind hier ausdrücklich **nicht** beurteilt — bestätigt ist allein, dass
die Regelmenge in voller Breite gelesen wurde.

## Vorbedingungen je Lauf (C7)

Über alle 96 deterministischen Laufmanifeste geprüft und einheitlich:

- `git status --porcelain` im Testrepo vor jedem Lauf leer, Checker-Repo ebenfalls
- `dist_cli_js_sha256` in allen 96 = `c0bbdfeb…d35d95`
- `base_ref` in allen 96 = `0d651041…c0a66` (**SHA**, nie eine relative Referenz)
- Soll-Validator Punkte **(1)–(5)** „all OK" in allen 96; die commit-scharfe **(6)**-Erwartung
  ist in allen 96 mitgeschrieben, ebenso (7) und (8)
- **I1-Prüfung (Validatorpunkt 4) in allen 96 aufgezeichnet**, nicht unterdrückt
  (§3 Rev. 12) — **0** Verletzungen

## Ablage je Block

| Pfad | Inhalt |
|---|---|
| `k1/k1_<modus>_<repo-sha>.jsonl` / `.json` | K1, Modus im Dateinamen |
| `k2/k2_<repo-sha>.jsonl` / `.json` | K2 |
| `k3/k3_<repo-sha>[_r<n>].jsonl` / `.json` | K3, Wiederholungen daneben |
| `k4/k4_<repo-sha>.stdout.txt` / `.stderr.txt` | K4 — **Rohtext**, kein `stdout_tail`, nicht vorgeparst (§6 Nachtrag Rev. 30 (2)) |
| `k5/k5_<repo-sha>.stdout.txt` / `.stderr.txt` | K5, ebenso |
| `manifests/<cfg>_<repo-sha>[_r<n>].json` | Laufmanifest je Invocation |
| `<block>/SHA256SUMS` | je Block, aus der Repowurzel mit `sha256sum -c` prüfbar |

**Beobachtung zu K4/K5 (§6 Nachtrag Rev. 30 (2)):** stdout und stderr sind für **alle 64**
Aufrufe abgelegt. **stdout** trägt in allen 64 Inhalt. **stderr ist in allen 64 leer (0 Bytes)** —
import-linter und PyTestArch schreiben ihre vollständige Ausgabe auf stdout und nutzen stderr
im fehlerfreien Lauf nicht. Festgehalten, nicht verändert.

## Journal

`journal.jsonl` ist append-only und steht in **keinem** `SHA256SUMS`. Schnappschuss nach
Phase 3, C10c und C10d, 189 Einträge:

```
e594e77dbe94197616ac6963fa253f6d083f66bb56899fba861962f0297d3335  data/campaign/journal.jsonl
```

## Offen

~~Die zehn K3-Injektionen ohne gültigen Lauf.~~ · ~~fortgeschrieben (C10c): noch drei —
I09, I11, I23.~~ — **erledigt am 28.08.2026 (C10d). Kein Block ist mehr offen; der Rohbestand
der Kampagne ist vollständig.**

Was bleibt, ist kein offener Punkt, sondern der **T14-Vorbehalt zu K3** oben: fünf
Zeitfenster, ungepinnter Endpunkt, nicht gemessene Auslastung — bei jeder Auswertung
mitzuführen.
