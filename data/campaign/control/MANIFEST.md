# MANIFEST — Ruhezustandsblock der deterministischen Konfigurationen (K1, K4, K5)

**Auftrag:** C6b-1, Punkt 1 (**A-14**) · **Datum:** 27. August 2026, 15:20 CEST
**Bericht:** [`docs/repo-kontext/c6b1_bericht_nachtraege.md`](../../../docs/repo-kontext/c6b1_bericht_nachtraege.md)
**Protokollbezug:** §0 Punkt 3 (Clean-Control-Set als Voraussetzung der Auswertung), §6
Nachtrag Rev. 23 (C3a — Audit, hartes Gate), §6 Nachtrag Rev. 24 (Aufrufspezifikation),
Rev. 32 (1) (`DEPOT_SRC`), Rev. 32 (3) (positive Lauf-Akzeptanzregel K4/K5), Rev. 32
(Schreibform K4), §6 Nachtrag Rev. 30 (1) (externe Wanduhrzeit) und (2) (Rohtext
stdout/stderr), §2 Rev. 11 (Soll-Validator als Vorbedingung je Lauf)

> **KEINE NEUE FESTLEGUNG, KEINE NACHTRÄGLICHE MESSERWEITERUNG.** Dieser Block **archiviert**
> einen Ruhezustand, den **§0 Punkt 3** als Voraussetzung der Auswertung ohnehin verlangt und
> den **C3a am 23.08.2026 bereits gemessen** hat — aber in einen **Scratch-Pfad** geschrieben
> (`<sp>/k1_full.jsonl`, `<sp>/k1_full.json`), der nicht mehr existiert. Für K2 und K3 liegt
> derselbe Ruhezustand seit C3b als Artefakt vor (`data/c3b-k2/`, `data/c3b-k3/`); für K1, K4
> und K5 fehlte er. Genau diese Lücke ist in
> [`kapitel7_tabellenskelette.md`](../../../docs/kapitel/kapitel7_tabellenskelette.md)
> **Anhang A, Zeile A-14** als offener Punkt registriert und wird hiermit geschlossen.

> **ZEITPUNKT UNGESCHMINKT.** Diese Läufe stehen **nach dem Beginn der Kampagne** (K1/K2/K4/K5
> am 27.08.2026 vormittags, K3 bis 12:19 CEST). Drei Umstände machen das unbedenklich, und sie
> werden hier genannt, nicht vorausgesetzt: **(1)** die drei Konfigurationen sind
> **deterministisch** — dieselbe Eingabe liefert dieselbe Ausgabe —, **(2)** es ist **kein
> Modell-Call** beteiligt, und **(3)** das Ergebnis war **vorab publiziert** (C3a §2a, §2b,
> §3a, §3b vom 23.08.2026). Der Lauf reproduziert einen bekannten Stand; **genau das ist der
> Beleg**. Er kann nichts herbeiführen, was nicht schon vor der Kampagne veröffentlicht war.

> **Keine Auswertung.** Rohbestand. Metriken, Findingbeurteilung und Vergleiche gehören nach
> C6b; die Eine-Iteration-Regel (§7) und die Amendment-Sperre aus §0.1 gelten.

## Messstand

| Grösse | Wert |
|---|---|
| **Zustand** | Clean-Baseline `B`, Tag `baseline` = `0d651041ed87dd03f2f78359713633fac01c0a66`, `--base` durchgehend dieser **SHA** |
| **Checker-Commit** | `348ca9daa456af4954f11f7152fc45201035297e` (Tag `phase04-freeze`, Messpfad `~/ma/tritongraph-measure`) |
| **Checker-Artefakt** | `dist/cli.js` = `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` (geprüft, **nicht** neu gebaut) |
| **Prompt-Hash** | `prompt_template_sha256` = `65e78f38e7b1fee20000ea70c654df042f5e0831fc6a68ccb340f833bd915035` |
| **Regel-Hash** | `rules_sha256` = `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` |
| **Topologie-Hash** | `topology_sha256` = `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` |
| **Prompt-Render-Hash** | `user_prompt_render_sha256` = `45780c70c486ea8f608d1b2ca11178049a02b7a6ece9ba33fcdc8d1b815b03ef` — **zeichengleich mit C3a §2a** |
| **Runner** | `4caf083d5e21f36440579af6888513ca897f1dd4` (§0.1, Amendment Rev. 35) — `tools/run_campaign.py`, `tools/campaign_spec.py`, `tools/postrun_check.py` unverändert **importiert**, nicht nachgebaut |
| **Werkzeuge** | import-linter 2.13 / grimp 3.15 · PyTestArch 4.0.1 / pytest 9.0.1 · Python 3.12.3 · Node v22.23.2 |
| **Maschine** | `Linux DESKTOP-PJA89CF 5.15.153.1-microsoft-standard-WSL2 … x86_64` — identisch zur Referenz aus `d2_bericht_vormessungen.md` M5(d) |

## Die vier Läufe

| Lauf | Graphmodus | Aufrufzeile aus | Exit | externe Wanduhr |
|---|---|---|---|---|
| **K1** | `full` | §6 Rev. 24, „K1, Full-Graph" | 0 | 222 ms |
| **K1** | `diff` | §6 Rev. 24, „K1, Diff-Graph" | 0 | 52 ms |
| **K4** | — | §6 Rev. 24 + Rev. 32 (Schreibform) | 0 | 171 ms |
| **K5** | — | §6 Rev. 32, „KORRIGIERTE FASSUNG" | 0 | 439 ms |

Summe der externen Wanduhrzeit: **884 ms**. Gemessen wie in der Kampagne — **monotone Uhr,
Subprozess-Start bis -Ende**, je Invocation (§6 Nachtrag Rev. 30 (1)).

**Warum K1 ZWEIMAL läuft.** §6 Rev. 24 registriert für K1 **zwei** Aufrufzeilen, und **C3a hat
beide ausgeführt** (§2a `full`, §2b `diff` am Leerfall). Die Ableitung des Modus aus
`category_l1` (§6 Nachtrag Rev. 31) hat auf der Clean-Baseline **keinen Gegenstand** — es gibt
keine Injektion und damit keine Kategorie. Nur ein Modus zu archivieren liesse den
Ruhezustandsbezug der jeweils anderen Hälfte des K1-Blocks unbelegt; der Kampagnenblock trägt
**4 × `full`** (I13–I16) und **28 × `diff`**.

## Erwartungsabgleich — die vor der Kampagne publizierten Werte, wörtlich

**K4, wörtlich reproduziert** (C3a §3a; das ASCII-Banner von import-linter steht im
archivierten Rohtext und war in C3a weggelassen — es trägt keine Messinformation):

```
Analyzed 75 files, 90 dependencies.
-----------------------------------

Layered spine of every bounded context KEPT
identity.api skips no layer KEPT
identity.services skips no layer KEPT
orders.api skips no layer KEPT
orders.services skips no layer KEPT
billing.api skips no layer KEPT
billing.services skips no layer KEPT
Only the adapter facade may reach into the adapter internals KEPT
orders and billing are mutually independent KEPT
No cycles between sibling packages KEPT
identity declares all of its direct children KEPT
orders declares all of its direct children KEPT
billing declares all of its direct children KEPT

Contracts: 13 kept, 0 broken.
```

Zeilenweise gegen den in C3a §3a abgedruckten Block verglichen: **19 von 19 Zeilen
zeichengleich, keine Abweichung.**

**K5, wörtlich reproduziert** (C3a §3b):

```
........................                                                 [100%]
24 passed in 0.24s
```

`24 passed`, Exit 0. Einziger Unterschied zu C3a §3b ist die **Laufzeitangabe** (`0.24s` gegen
`0.18s`) — eine Uhr, keine Messgrösse.

**K1, gegen C3a §2a und §2b:**

| Grösse | C3a publiziert | hier gemessen |
|---|---|---|
| Findings, `full` | 0 | **0** |
| Findings, `diff` | 0 | **0** |
| `graph_files_count`, `full` | 73 | **73** |
| `graph_files_count`, `diff` | 0 | **0** |
| `changed_files_count` (beide) | 0 | **0** |
| `calls_total` (beide) | 0 | **0** |
| `invalid_reasons` (beide) | leer | **leer** |
| Exit (beide) | 0 | **0** |
| Records `DERIVED:` / übrige | 0 / 0 | **0 / 0** |

**Eine benannte Abweichung in der AUFRUFZEILE, nicht im Ergebnis.** Die in C3a §2a
protokollierte `cli_args`-Liste des `full`-Laufs trägt **kein** `--base`; die in §6 Rev. 24
registrierte Zeile trägt es. Hier läuft die **registrierte** Zeile. Auf der Clean-Baseline ist
`--base` == `HEAD`, der Diff also leer, und der `full`-Modus liest ohnehin den ganzen Baum —
`graph_files_count: 73` in beiden Fällen. Die Gleichheit ist damit **gemessen**, nicht
angenommen.

## Gültigkeit — welche Regel gilt und welche nicht

| Lauf | angewandte Regel | Verdikt |
|---|---|---|
| K4 | positive Lauf-Akzeptanzregel §6 Nachtrag Rev. 32 (3): `kept + broken` == 13 | **VALID** (13 ausgewertet) |
| K5 | positive Lauf-Akzeptanzregel §6 Nachtrag Rev. 32 (3): 24 gesammelte Tests, Sammelphase fehlerfrei | **VALID** (24 gesammelt) |
| K1 `full` / `diff` | **keine registrierte Zählregel anwendbar** — s. u. | Kriterium: die publizierten C3a-Werte, **erfüllt** |

**Die Zählregel des Injektionslaufs kann auf der Clean-Baseline NICHT gelten.** Sie verlangt
`changed_files_count == 1`; auf `B` ist `--base` == `HEAD`, der Wert also **0 durch
Konstruktion**. Genau das hat C3a §2b protokolliert, und `tools/postrun_check.py` führt den Fall
in seinem eigenen Kopf als Beispiel. Die Zählregel des Kontrolllaufs zielt auf `--control-files`
und den LLM-Pfad; K1 führt beides nicht.

**Verschwiegen wird nichts:** das Verdikt der Injektionsregel ist in beiden K1-Laufmanifesten
unter `campaign_rule_verdict` **mitgeschrieben** — es lautet dort `INVALID` mit der Begründung
`changed_files_count = 0` — und daneben steht unter `campaign_rule_note`, warum die Regel hier
keinen Gegenstand hat. Das Kriterium dieses Blocks steht unter `c3a_expectation`. **Es wurde
keine Regel erfunden und keine abgesenkt**; herangezogen ist der Wert, den C3a selbst
veröffentlicht hat.

## Vorbedingungen je Lauf

Über alle vier Läufe geprüft und einheitlich, mit **denselben Funktionen** des Kampagnen-Runners:

- `git status --porcelain` im Testrepo vor jedem Lauf **leer** (vor und nach dem Checkout),
  Checker-Repo ebenfalls leer
- `dist_cli_js_sha256` in allen vier = `c0bbdfeb…d35d95`; **kein Bau nötig**
- `checker_git_head` und `phase04-freeze` in allen vier = `348ca9da…35297e`
- `base_ref` in allen vier = `0d651041…c0a66` (**SHA**, nie eine relative Referenz)
- **Soll-Validator** in allen vier: Exit 0, Punkte **(1)–(5) „all OK"**, Punkt **(6)** gemessene
  Importeursmengen gleich der aus der Soll-Whitelist berechneten Erwartung, Punkt **(7)** gegen
  `--expect-cycles 0`, Punkt **(8)** ohne Kante ausserhalb der Whitelist — die Erwartung ist hier
  die **des Ruhezustands**: keine Injektion, keine registrierte Kante, kein Zyklus
- **I1-Prüfung (Validatorpunkt 4) in allen vier aufgezeichnet**, nicht unterdrückt
  (§3 Rev. 12) — **0** Verletzungen
- **`.grimp_cache/` vor dem K4-Lauf entfernt**, Zustand vorher und nachher aufgezeichnet;
  `--no-cache` steht in der Aufrufzeile (§1 Amendment 11.08., B9+ (b))

## Ablage

| Pfad | Inhalt |
|---|---|
| `k1/k1_full_<baseline-sha>.jsonl` / `.json` | K1, Vollgraph |
| `k1/k1_diff_<baseline-sha>.jsonl` / `.json` | K1, Diffgraph (Leerfall) |
| `k4/k4_<baseline-sha>.stdout.txt` / `.stderr.txt` | K4 — **Rohtext**, kein `stdout_tail`, nicht vorgeparst (§6 Nachtrag Rev. 30 (2)) |
| `k5/k5_<baseline-sha>.stdout.txt` / `.stderr.txt` | K5, ebenso |
| `manifests/<cfg>_<baseline-sha>.json` | Laufmanifest je Invocation — Vorbedingungen, Soll-Validator-Ausgabe, Aufrufzeile, externe Wanduhrzeit, Erwartungsabgleich |
| `run_clean_state.py` | der **Treiber dieses einen Archivierungslaufs** — s. u. |
| `SHA256SUMS` | aus der Repowurzel mit `sha256sum -c` prüfbar |

**Beobachtung zu K4/K5 (§6 Nachtrag Rev. 30 (2)):** stdout und stderr sind für **beide** Aufrufe
abgelegt. **stdout** trägt in beiden Inhalt, **stderr ist in beiden leer (0 Bytes)** — dieselbe
Beobachtung wie über die 64 Kampagnenaufrufe. Festgehalten, nicht verändert.

**Zum Treiber.** `run_clean_state.py` ist **kein** Teil der registrierten Werkzeugkette und
steht deshalb hier im Archiv statt in `tools/`. Er **importiert** `tools/run_campaign.py`,
`tools/campaign_spec.py` und `tools/postrun_check.py` auf Commit `4caf083` und ruft deren
Funktionen auf — Vorbedingungen, Aufrufzeilenbau, Soll-Validator, Maschinenkennung,
Wanduhrmessung, Artefaktpfade und die K4/K5-Akzeptanzregel sind **dieselben Codepfade** wie in
der Kampagne, nicht nachgebaute. Was er selbst beisteuert, ist allein die Zeile des
Ruhezustands (Baseline statt Injektion) und der Erwartungsabgleich gegen die C3a-Werte.
`tools/` ist von diesem Auftrag **nicht berührt**; der Runner-Commit bewegt sich nicht.

## Journal

`journal.jsonl` steht wie in den Kampagnenblöcken **nicht** in `SHA256SUMS` — sie ist
append-only und wüchse bei einer Wiederholung weiter. Schnappschuss bei Abschluss dieses Blocks,
**4 Einträge**, alle `MATCHES_C3A`, alle `attempt 1`:

```
c835e3d765cdbf4967fa8c4b3c95900afde867eb1a826d1596411388d1242793  data/campaign/control/journal.jsonl
```

## Offen

Nichts. Der Block ist vollständig: vier Läufe, vier Laufmanifeste, vier Erwartungsabgleiche,
keine Abweichung. **A-14 ist damit geschlossen** — die Ruhezustandsseite der Tabelle **T4
Symmetrieteil** hat ab hier einen Artefaktpfad und nicht mehr nur einen Berichtsverweis.
