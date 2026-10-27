# C10 — Bericht: die Konformitätskampagne K1–K5

**Auftrag:** C16 (nachgereichter Abschlussbericht zu C10 / C10a / C10c / C10d)
**Datum des Berichts:** 29. August 2026 · **Repo (schreibend):** `masterarbeit`
**Gegenstand:** die Messkampagne vom 27./28. August 2026, archiviert unter `data/campaign/`
**Verlinkt aus:** [`data/campaign/MANIFEST.md`](../../data/campaign/MANIFEST.md) ·
[`data/campaign/k2/MANIFEST.md`](../../data/campaign/k2/MANIFEST.md) ·
[`data/campaign/k3/MANIFEST.md`](../../data/campaign/k3/MANIFEST.md)

---

## 0. Was dieser Bericht ist — und was er nicht ist

**Dies ist die Verfahrensdokumentation der Kampagne, keine Auswertung.** Er hält fest, unter
welchem Messstand, in welcher Reihenfolge, mit welchen Wiederholungen und mit welchen
Zwischenfällen der Rohbestand entstanden ist. **Keine Metrik, keine Precision, kein Vergleich
zwischen Konfigurationen, keine Deutung eines Findings.** Wo Ergebnisse berührt werden, steht
ein Verweis: die Ergebnisse der Kampagne stehen in `docs/befunde_log.md` **Befund 08** und im
kanonischen Auswertungslauf `data/campaign/eval/c14_eval_full.md` / `.json`.

**Quellenregel dieses Berichts.** Jede Zahl und jedes Verdikt unten ist aus dem
**Repositorium** gelesen — aus den gehashten Laufmanifesten unter `data/campaign/manifests/`,
den archivierten Roh- und Findingartefakten der fünf Blöcke, den Blockmanifesten,
`data/campaign/journal.jsonl` und `data/campaign/eval/`. **Kein Wert ist aus einer
Sitzungsausgabe übernommen.** Wo eine Angabe nur aus einer Sitzung stammen könnte, ist sie
**neu erhoben** oder ausdrücklich als **nicht belegbar** ausgewiesen (§1, Fussnote zur
Bewegungsprüfung).

**Der Bericht kam nach.** `data/campaign/MANIFEST.md`, `k2/MANIFEST.md` und `k3/MANIFEST.md`
verlinken ihn seit dem 27.08.2026; geschrieben ist er am 29.08.2026. Befund 08, 08.9 hat die
Lücke benannt („der C10-Bericht … existiert **nicht**"). Sie ist mit diesem Dokument
geschlossen.

---

## 1. Messstand und Vorbedingungen

### 1.1 Der Freeze-Anker

Das Evaluationsprotokoll `docs/protokolle/eval_protokoll_phase04.md` ist **am 27.08.2026 als
Rev. 33 zur Vorregistrierung eingefroren** worden, **vor dem ersten Kampagnenlauf**. Der
Bytestand jenes Freeze ist

```
2cb0385f08e88333863d83d0819943e352d3f1b857d4870801211b4817ac181e
```

bezeugt in `c5b_bericht_protokoll_freeze.md` §3, Zeile Rev. 33, Commit `3e17f44`. Das ist der
**Beleg der Vorregistrierung**; der heutige Stand des Protokolls (Rev. 45,
`0ce57d29…5ff92eca`) ist ein anderer Wert und in derselben Tabelle geführt. Die
Auswertungsspezifikation stand zum Zeitpunkt des Freeze auf
`2f1354bbabdfaef8c858a6726521e224c30d6293513d83ea98cd1ef3f6608f97`
(`c5b_bericht_protokoll_freeze.md` §2; Protokoll Revisionshistorie Rev. 33).

Der eingefrorene Messstand steht in Protokoll **§0.1**; die für den Lauf verbindlichen Werte
sind unten in 1.3 nicht zitiert, sondern **aus den Artefakten der Kampagne selbst
nachgemessen**.

### 1.2 Die vier Bäume

Die Kampagne läuft über vier Arbeitsbäume mit klar getrennten Rollen:

| Baum | Rolle in der Kampagne |
|---|---|
| `~/ma/masterarbeit` | schreibend — Protokoll, Spezifikation, Messeingänge `data/soll/`, Runner, Archivwurzel `data/campaign/` |
| `~/ma/tritongraph` | Entwicklungsbaum des Checkers — **in der Kampagne nicht benutzt** |
| `~/ma/tritongraph-measure` | **Messpfad**: Worktree auf dem Tag `phase04-freeze`; hieraus läuft `dist/cli.js` |
| `~/ma/ma-conformance-testrepo` | **Messgegenstand**: Baseline `0d651041…c0a66`, 32 Injektionstags `inj/01`…`inj/32`, sternförmig |

Dass die Messung aus `tritongraph-measure` und nicht aus dem Entwicklungsbaum lief, ist je
Invocation bezeugt: `measurement_path` steht in **allen 189** Laufmanifesten zeichengleich auf
`/home/haasentimo/ma/tritongraph-measure`, `checker_git_status_porcelain` in allen 189 auf
**leer**, `cwd` und `abs_repo_path` in allen 189 auf
`/home/haasentimo/ma/ma-conformance-testrepo`.

### 1.3 Die Bewegungsprüfung — neu erhoben

**Zur Belegbarkeit, ungeschminkt.** Die Bewegungsprüfung vor Phase 0 war ein **Sitzungsvorgang**
und ist als solcher im Repositorium **nicht** als eigenes Dokument abgelegt; ihre Durchführung
lässt sich aus dem Repo nicht zitieren. **Belegbar — und stärker — ist ihr Gegenstand:** die
registrierten Grössen sind **je Invocation** ins gehashte Laufmanifest bzw. in die
Provenienzkopfzeile des Artefakts geschrieben worden. Die folgende Tabelle ist daher **neu
erhoben**, über **alle 189 Laufmanifeste** und **alle 125 Checker-Artefakte** (K1 32, K2 32,
K3 61), nicht aus einem Bericht übernommen.

| Registrierte Grösse (§0.1) | Wert, über den ganzen Bestand zeichengleich | Belegbreite |
|---|---|---|
| **Checker** — Freeze-Tag und Commit | `phase04-freeze = 348ca9daa456af4954f11f7152fc45201035297e` | 189 / 189 Laufmanifeste |
| **Checker-Artefakt** `dist/cli.js` | `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` | 189 / 189 Laufmanifeste |
| **Messeingang Topologie** `depot_soll.ilograph.yaml` | `topology_sha256` = `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` | 125 / 125 Artefakte |
| **Messeingang Regeldatei** `architecture-rules.yaml` | `rules_sha256` = `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` | 125 / 125 Artefakte |
| **Prompt-Vorlage** | `prompt_template_sha256` = `65e78f38e7b1fee20000ea70c654df042f5e0831fc6a68ccb340f833bd915035` | 125 / 125 Artefakte |

**Kein einziger abweichender Wert in keiner der fünf Zeilen.** Mitgemessen und ebenfalls
durchgehend konstant: `base_ref` = `0d651041ed87dd03f2f78359713633fac01c0a66` (der **SHA**, nie
eine relative Referenz) in 189 / 189, `user_prompt_render_sha256` =
`45780c70c486ea8f608d1b2ca11178049a02b7a6ece9ba33fcdc8d1b815b03ef` in 125 / 125, und die
Maschinenkennung (`Linux DESKTOP-PJA89CF 5.15.153.1-microsoft-standard-WSL2 … x86_64`,
Python 3.12.3, Node v22.23.2) in 189 / 189 — identisch zur Referenz aus
`d2_bericht_vormessungen.md` M5(d), die jedes Manifest als `machine_reference_d2_m5d`
mitführt.

### 1.4 Der Runner

Alle fünf Blöcke sind unter **einem** Runner-Stand gelaufen: Commit
`4caf083d5e21f36440579af6888513ca897f1dd4`, definiert nach §0.1 als der letzte Commit, der
eine der drei Runner-Dateien berührt. Die Dateien tragen heute unverändert die dort
registrierten Hashes:

```
eba3b95a0bfb21192f6b49ed6a3e02c4c1d26ec68e2abd1a8f2de939b07e62c4  tools/run_campaign.py
c95d38140f00ee1d1823d9c96a03fbcbff28f94a96281ce940772b6944a63995  tools/campaign_spec.py
d179dcba0530c6806ce964d282611ee680b674f69497a0fde46aa4a980ed9d31  tools/postrun_check.py
```

Zeichengleich mit den in `data/campaign/k2/MANIFEST.md` (Nachtrag C6b-1) für `4caf083`
abgedruckten Werten.

### 1.5 Umgebungsparameter je Konfiguration

Aus `env_overrides` und `argv` der Laufmanifeste, je Konfiguration über alle Invocationen
zeichengleich:

| Konf. | `env_overrides` | `--runs` | `--timeout-ms` | `--rule-graph` |
|---|---|---|---|---|
| K1 | *(keine)* | 1 | 120000 | `full` 4 × (I13–I16), `diff` 28 × — abgeleitet aus `category_l1` |
| K2 | `CONFORMANCE_BASE_URL=http://localhost:11434/v1` · `CONFORMANCE_MODEL=qwen2.5-coder:7b` · `CONFORMANCE_API_KEY=<redacted>` | 3 | 240000 | `diff` 32 × |
| K3 | `CONFORMANCE_BASE_URL=https://inference.do-ai.run/v1` · `CONFORMANCE_MODEL=nvidia-nemotron-3-super-120b` · `CONFORMANCE_API_KEY=<redacted>` | 3 | 600000 | `diff` 61 × |
| K4 | `PYTHONPATH=src` | — | — | *(Schalter unbekannt)* |
| K5 | `DEPOT_SRC=/home/haasentimo/ma/ma-conformance-testrepo/src` | — | — | *(Schalter unbekannt)* |

Die K5-Zeile ist der Beleg, dass die C7-Korrektur (§8.2) tatsächlich in der Kampagne stand:
`DEPOT_SRC` ist in **32 von 32** K5-Invocationen gesetzt. Das K2-Kontextfenster ist je
Invocation **gemessen**, nicht angenommen: in 32 von 32 Manifesten steht
`measured_context_length = 4096` mit `measurement_source = "read from the CONTEXT column of
the resident instance"` — der in §1 Nachtrag Rev. 26 registrierte Wert. Der grimp-Cache ist
für K4 in 32 von 32 vor **und** nach dem Lauf als `present: false` protokolliert.

---

## 2. Ablauf je Block

**Quelle dieses Abschnitts:** die 189 Laufmanifeste (Feld `started`, `external_wall_clock_ms`,
`postrun.verdict`) und die `run_header`-Zeitstempel der Rohlogs; Gegenprobe
`data/campaign/journal.jsonl`.

> **Eine Lesehilfe zum Feld `started`.** Es heisst so, wird aber **nach** dem Subprozess
> geschrieben: `tools/run_campaign.py` startet den Prozess in Zeile 783 und baut das Manifest
> mit `"started": now()` erst in Zeile 828. Das Feld trägt also das **Ende** der Invocation.
> Wo unten eine Blockuntergrenze angegeben ist, stammt sie aus dem `run_header`-Zeitstempel
> des ersten Rohlogs, nicht aus `started`. Festgehalten, nicht geändert.

### 2.1 Die Reihenfolge

| # | Block | Zeitfenster (CEST) | Invocationen | Model-Calls | Wiederholungen | Verdikte |
|---|---|---|---|---|---|---|
| 1 | **K2** (Ollama) | 27.08. 08:46:02 – 08:50:18 | 32 | 96 | keine | 32 VALID, 0 INVALID |
| 2 | **K3** (DO-Direktzugang) | 27.08. 09:04:59 – 28.08. 09:32:21 | 61 | 183 | 29 | 32 VALID, 29 INVALID |
| 3 | **K1 / K4 / K5** | 27.08. 12:30:15 – 12:30:42 | 32 / 32 / 32 | 0 / 0 / 0 | keine | je 32 VALID, 0 INVALID |
| 4 | **`control/`** (Ruhezustand K1/K4/K5) | 27.08. 15:20 | 4 | 0 | keine | 4 × `MATCHES_C3A` |

**Externe Wanduhrzeit, Summe je Block** (monotone Uhr, Subprozess-Start bis -Ende, je
Invocation — §6 Nachtrag Rev. 30 (1)):

| Block | Summe |
|---|---|
| K1 | 2 513 ms |
| K2 | 252 155 ms |
| K3 | 9 190 542 ms |
| K4 | 3 621 ms |
| K5 | 9 917 ms |
| `control/` (vier Läufe) | 884 ms |

### 2.2 K2 — Ollama, 32 Invocationen ohne Wiederholung

Der Block lief in **vier Minuten und sechzehn Sekunden** durch: 32 Invocationen, je
`--runs 3`, zusammen **96** Model-Calls, alle `attempt 1`, alle **VALID**,
`invalid_reasons` durchgehend leer, `calls_invalid` und `calls_transport_failed` je **0**.
`changed_files_count == 1` in allen 32.

Der Block ist **vollständig neu gefahren** worden, nachdem ein erster Anlauf am selben Morgen
an I07 abgebrochen war; Einzelheiten in §8.1.

### 2.3 K3 — DigitalOcean-Direktzugang, 61 Invocationen über zwei Tage

Sechs Versuche, 61 Invocationen, 183 Model-Calls. Der Verlauf steht im Einzelnen in §3.

### 2.4 K1, K4, K5 — die deterministischen Blöcke

Alle drei liefen am 27.08.2026 im selben 27-Sekunden-Fenster (12:30:15 – 12:30:42), je 32
Invocationen, je 32 VALID, keine Wiederholung, kein Model-Call. K1 trägt den Graphmodus
**abgeleitet** aus `category_l1` — `full` für die vier `CYCLE`-Injektionen I13–I16, `diff` für
die übrigen 28 —, und die Ableitung steht je Lauf im Manifest (`rule_graph_mode_source:
"derived from category_l1 (protocol §6 Nachtrag Rev. 31)"`), damit sie nachprüfbar ist und
nicht dem Runner geglaubt werden muss.

### 2.5 Der Ruhezustandslauf `control/`

Vier Invocationen auf der **sauberen** Baseline: K1 zweimal (einmal `full`, einmal `diff` —
§6 Rev. 24 registriert für K1 zwei Aufrufzeilen, und C3a hat beide ausgeführt), K4 einmal,
K5 einmal. Verdikt je Lauf `MATCHES_C3A`.

**Der Zeitpunkt ist ungeschminkt zu nennen und steht so auch im Blockmanifest:** dieser Lauf
steht **nach** dem Beginn der Kampagne (27.08., 15:20 CEST). Drei Umstände machen ihn
unbedenklich, und sie werden genannt, nicht vorausgesetzt: die drei Konfigurationen sind
**deterministisch**, es ist **kein Modell-Call** beteiligt, und das Ergebnis war **vorab
publiziert** (C3a §2a/§2b/§3a/§3b vom 23.08.2026). Der Lauf reproduziert einen bekannten,
veröffentlichten Stand — genau das ist sein Beleg. Er schliesst den in
`kapitel7_tabellenskelette.md` Anhang A als **A-14** registrierten offenen Punkt: für K2 und K3
lag der Ruhezustand seit C3b als Artefakt vor (`data/c3b-k2/`, `data/c3b-k3/`), für K1, K4 und
K5 hatte C3a ihn in einen inzwischen nicht mehr existierenden Scratch-Pfad geschrieben.

---

## 3. Der K3-Verlauf im Einzelnen

**Quelle:** die 61 K3-Laufmanifeste und die 61 K3-Rohlogs (`llm_call`-Records mit
`transport_failures`). Alle Zahlen unten sind daraus **ausgezählt**.

### 3.1 Die sechs Versuche

| Versuch | Datum · Zeitfenster (CEST) | Invocationen | Calls | 429-Ereignisse | gescheiterte Calls | zurückgeholte Injektionen | danach offen |
|---|---|---|---|---|---|---|---|
| **V1** | 27.08. 09:04:59 – 10:58:54 | 32 | 96 | 77 | 18 | 21 (I01–I04, I08, I10, I12, I14, I15, I17–I19, I24–I32) | 11 |
| **V2** | 27.08. 12:00:07 – 12:18:33 | 11 | 33 | 58 | 15 | **1** (I22) | 10 |
| **V3** | 28.08. 08:02:14 – 08:18:35 | 10 | 30 | 16 | 3 | **7** (I05, I06, I07, I13, I16, I20, I21) | 3 |
| **V4** | 28.08. 08:19:37 – 08:20:32 | 3 | 9 | 27 | **9 von 9** | **0** | 3 |
| **V5** | 28.08. 08:52:45 – 09:07:38 | 3 | 9 | 16 | 5 | **1** (I09) | 2 |
| **V6** | 28.08. 09:17:59 – 09:32:21 | 2 | 6 | **0** | **0** | **2** (I11, I23) | **0** |
| | **Summe** | **61** | **183** | **194** | **50** | **32 von 32** | — |

> **Zu den Zeitfenstern.** Die Grenzen oben sind die **Log-Grenzen des Checkers**: erster
> `run_header`-Zeitstempel bis letzter `run_footer`-Zeitstempel des Versuchs. Das Blockmanifest
> `data/campaign/k3/MANIFEST.md` nennt geringfügig **weitere** Grenzen (z. B. V2 bis 12:19:18
> statt 12:18:33, V5 ab 08:51:41 statt 08:52:45) — es misst die **Runner-Invocation**, also
> einschliesslich Checkout, Soll-Validator und Manifestschreibung vor und nach dem Checkerlauf.
> Beide Angaben sind richtig; sie messen Verschiedenes. **Hier ist nichts angeglichen.**

Die elf nach V1 offenen Injektionen sind **I05, I06, I07, I09, I11, I13, I16, I20, I21, I22,
I23** — dieselbe Menge, an der später der Artefaktauswahldefekt sichtbar wurde (§8.3).

**Verteilung der Versuchsnummern über die 32 gültigen Läufe:** 21 im ersten, 1 im zweiten,
7 im dritten, 1 im fünften, 2 im sechsten. **Kein gültiger Lauf stammt aus V4.**

### 3.2 Die zeitliche Lage der 429

Zehn-Minuten-Fächer, Calls / 429-Ereignisse / gescheiterte Calls, aus den `llm_call`-Records
ausgezählt.

**Erstversuch V1** (UTC, wie im Blockmanifest geführt):

```
07:00   4/ 1/0     07:10   8/ 1/0     07:20   8/14/4     07:30   6/ 7/1
07:40   5/ 0/0     07:50   9/12/2     08:00  11/11/3     08:10  11/14/4
08:20  11/17/4     08:30  11/ 0/0     08:40   5/ 0/0     08:50   7/ 0/0
```

**V2** (UTC): `10:00 15/24/6` · `10:10 18/34/9`.

**V3 bis V6, 28.08.** (CEST, so wie das Blockmanifest sie zusammenfasst — V3 und V4
überlappen im Fächer 08:10):

```
08:00  14/11/2     08:10  19/14/4     08:20   6/18/6
08:50   3/ 9/3     09:00   6/ 7/2     09:10   3/ 0/0     09:30   3/ 0/0
```

Das Muster ist **schubweise, nicht monoton**: das Fenster am 28.08. trug zu Beginn (die ersten
sieben Injektionen kamen durch) und schloss sich innerhalb einer knappen halben Stunde — im
Fächer 08:20 kommen auf **6** Calls **18** 429-Ereignisse und **alle sechs** Calls scheitern.
Danach 08:50 wieder geschlossen (3 / 9 / 3), 09:00 halb offen (6 / 7 / 2), **09:10 und 09:30
vollständig offen — null 429**.

**Alle 194 Transportereignisse des Blocks sind `http_429`.** Kein Timeout, kein anderer
Transportfehler, in keinem der 183 Calls.

### 3.3 Die Anhalteregel und wann sie griff

Protokoll **§7** legt fest: *„**API-Fehler** (Timeout, 429): betroffenen Call wiederholen, im
Log kennzeichnen; systematischer Ausfall → Lauf abbrechen, neu starten, beides
protokollieren."* Als Richtwert für „systematisch" ist im Blockmanifest **fünf
aufeinanderfolgende gescheiterte Calls** geführt.

Längste Folge aufeinanderfolgender gescheiterter Calls je Versuch, aus dem chronologisch
sortierten Callstrom ausgezählt:

| Versuch | längste Folge | Richtwert erreicht |
|---|---|---|
| V1 | **4** von 96 | nein — der Versuch lief mit Fortschritt durch |
| V2 | 3 von 33 | nein — angehalten wegen der **Ausbeute** (1 von 11) |
| V3 | 2 von 30 | nein |
| **V4** | **9 von 9** | **ja — alle drei Invocationen scheiterten hart, je 3 von 3 Calls in unter 19 Sekunden** |
| V5 | 3 von 9 | nein |
| V6 | 0 von 6 | nein |

**Zweimal wurde angehalten.** Nach **V2**, weil elf Wiederholungen genau **eine** Injektion
zurückholten; nach **V4**, weil neun aufeinanderfolgende Calls scheiterten — weit über dem
Richtwert von fünf. In beiden Fällen ist **neu gestartet**, nicht nachgebessert worden; das ist
genau die von §7 vorgesehene Reaktion.

### 3.4 Die Aufrufplanung von C10d — eine Änderung des Zeitpunkts, nicht des Werkzeugs

Nach dem harten Ausfall von V4 hat C10d den Block mit **Einzelaufrufen und Pausen**
geschlossen. Statt eines Runner-Aufrufs über alle drei offenen Injektionen wurde je Injektion
ein eigener Aufruf gefahren, mit mindestens zehn Minuten Abstand.

Zeiten in dieser Tabelle nach `data/campaign/k3/MANIFEST.md` — also **Runner-Grenzen**, nicht
Checker-Log-Grenzen (siehe den Hinweis in 3.1).

| Aufruf | Zeit (CEST) | Injektion | Ergebnis |
|---|---|---|---|
| 1 | 08:51:41 – 08:53:04 | I23 | INVALID — 3/3 Calls in **18,98 s**, Schub geschlossen |
| 2 | 09:03:16 – 09:05:23 | I09 | **VALID** (123 315 ms) |
| 3 | 09:06:46 – 09:07:45 | I11 | INVALID — 2/3 Calls, 54,5 s |
| 4 | 09:17:58 – 09:19:58 | I11 | **VALID** (124 780 ms) |
| 5 | 09:30:05 – 09:32:21 | I23 | **VALID** (140 659 ms) |

**Die Begründung, so wie sie im Blockmanifest steht:** das Limit ist **schubweise**, nicht
monoton — Einzelaufrufe mit Abstand treffen mit höherer Wahrscheinlichkeit einen offenen Schub.
**Vorab festgelegt** war eine Obergrenze von **höchstens drei** weiteren Versuchen je offener
Injektion an diesem Tag; verbraucht wurden **2 von 3** (I23), **1 von 3** (I09) und **2 von 3**
(I11). Die Grenze wurde weder ausgeschöpft noch überschritten.

**Was sich bewegt hat und was nicht — das ist der tragende Punkt dieses Abschnitts.** Bewegt
hat sich allein die **Aufrufplanung**, also der **Zeitpunkt** der Calls. **Nicht bewegt** haben
sich: Retry-Budget (`transport_max_retries: 2`, also drei Versuche je Call), das Pacing im
Werkzeug, der Runner (durchgehend `4caf083`, in allen 61 K3-Manifesten derselbe Stand nach
1.4), das Modell, der Endpunkt, die Aufrufzeile im Übrigen, Prompt, Schema, Regeldatei und
Manifest. §7 registriert den **Neustart eines Laufs**; genau das ist geschehen. Eine Änderung
des Werkzeugs wäre eine Amendment-pflichtige Bewegung am eingefrorenen Messstand gewesen und
hat nicht stattgefunden.

### 3.5 Der T14-Vorbehalt, der daraus folgt

Die 32 gültigen K3-Läufe stammen aus **fünf Zeitfenstern über zwei Tage**: 27.08. 09:00-Stunde
**7**, 27.08. 10:00-Stunde **14**, 27.08. 12:00-Stunde **1** (I22), 28.08. 08:00-Stunde **7**,
28.08. 09:00-Stunde **3** (I09, I11, I23). Der Endpunkt ist **nicht gepinnt** (§6 Rev. 32 —
ohne Router gibt es nichts zu pinnen), seine Auslastung ist weder gemessen noch kontrollierbar.
**Das Zeitfenster ist der einzige beobachtete Hebel, und er ist unkontrolliert.** T14 (§9) gilt
für diese Streuung in vollem Umfang und ist bei jeder Auswertung mitzuführen.

---

## 4. Gültigkeit

### 4.1 T7 aus den Laufmanifesten

Gültigkeit entscheidet allein `tools/postrun_check.py` (§6 Nachtrag Rev. 24); der **Exit-Code
ist kein Kriterium** (Rev. 26). Die folgenden Zahlen sind aus den 189 gehashten Laufmanifesten
ausgezählt — der seit Protokoll Rev. 39 registrierten Quelle von T7 — und decken sich
zeichengleich mit T7.1 des kanonischen Auswertungslaufs.

| Konf. | Invocationen | VALID | INVALID | Model-Calls | `calls_invalid` | `calls_transport_failed` | Injektionen mit gültigem Lauf |
|---|---|---|---|---|---|---|---|
| K1 | 32 | 32 | 0 | 0 | 0 | 0 | **32 / 32** |
| K2 | 32 | 32 | 0 | 96 | 0 | 0 | **32 / 32** |
| K3 | 61 | 32 | 29 | 183 | 0 | 50 | **32 / 32** |
| K4 | 32 | 32 | 0 | 0 | 0 | 0 | **32 / 32** |
| K5 | 32 | 32 | 0 | 0 | 0 | 0 | **32 / 32** |

**`calls_invalid` steht bei allen fünf Konfigurationen durchgehend auf 0.** Die 29 ungültigen
K3-Invocationen tragen als `invalid_reasons` ausnahmslos `transport_failure`.

**Aus den Rohlogs gegengezählt** (`llm_call`-Records mit `outcome: measured`): K2 **96 von 96**
mit `valid_final: true`, K3 **133 von 133** mit `valid_final: true`, `attempts_used` in allen
229 gemessenen Calls **1** — kein Fall, in dem erst ein Repair-Versuch die Gültigkeit
hergestellt hätte. **Kein einziger Call lieferte je eine ungültige Antwort.** Die
Transportausfälle stehen **neben** der Gültigkeitsrate, nie darin.

### 4.2 Zählregeln

`changed_files_count == 1` in **125 von 125** Injektionsläufen der Konfigurationen mit
Laufprotokoll (K1, K2, K3). `calls_total` je Invocation: K1 **0** (deterministischer Pfad, kein
Modell — so verlangt es der ausgeführte Akzeptanztest in `tools/postrun_check.py`), K2 und K3 je
**3** (`1 × runs`).

### 4.3 Gegenprobe Journal

`data/campaign/journal.jsonl` ist append-only und steht in **keinem** `SHA256SUMS`; es ist seit
C6c-a **Gegenprobe** zu T7, nicht dessen Quelle. Für diesen Bericht neu gerechnet:

- **189 Journaleinträge gegen 189 Laufmanifeste**, Schlüsselmengen **identisch**;
- je Eintrag Konfiguration, Injektions-ID, `attempt` und Verdikt gegen das Manifest verglichen:
  **null Divergenzen**.

Weicht eine Gegenprobe ab, wird das berichtet und **nicht** durch Angleichen aufgelöst. Es wich
nichts ab.

### 4.4 Das Validitäts-Gate hat nicht gegriffen

Protokoll **§7** legt fest: liegt der `valid_final`-Anteil einer LLM-Konfiguration **unter
0,9**, wird das als Befund dokumentiert und die Konfiguration mit den vorhandenen validen
Läufen ausgewertet — **nicht nachgebessert**. Der Anteil steht bei **K2 auf 96/96 = 1,000** und
bei **K3 auf 133/133 = 1,000**. **Das Gate hat nicht gegriffen.**

Das Gate war **vor** dem ersten Kampagnenlauf bestätigt worden (Protokoll Rev. 33, §0 Punkt 2),
und zwar an den Kontrollläufen auf der sauberen Baseline — eine Bestätigung nach Sichtung der
Kampagnenwerte wäre nicht mehr vorregistriert, sondern an den Daten gewählt gewesen.

---

## 5. Die positive Lauf-Akzeptanz von K4 und K5

Aus den 64 archivierten Rohtexten für diesen Bericht **neu ausgezählt**:

| Konf. | Regel (§6 Nachtrag Rev. 32 (3)) | Erwartet | Gemessen |
|---|---|---|---|
| **K4** | ausgewertete Contracts, `kept + broken` | 13 | **13 in 32 von 32 Aufrufen** |
| **K5** | gesammelte Tests, Sammelphase fehlerfrei | 24 | **24 in 32 von 32 Aufrufen**, kein Sammelfehler |

Die Verteilung hinter der K4-Zeile: `12 kept, 1 broken` 16 ×, `13 kept, 0 broken` 13 ×,
`11 kept, 2 broken` 3 × — **stets 13**. Hinter der K5-Zeile: `1 failed, 23 passed` 20 ×,
`24 passed` 12 × — **stets 24**. Die **Trefferzahlen** sind hier ausdrücklich **nicht**
beurteilt; geprüft ist allein, dass die Regelmenge in voller Breite gelesen wurde.

**Warum das keine Formalie ist.** K4 und K5 schreiben **kein Laufprotokoll**. Für K1/K2/K3
fängt die Zählregel über `changed_files_count` und `calls_total` eine Fehlkonfiguration ab,
weil sie eine **positive** Aussage über den Lauf verlangt; K4 und K5 hatten bis Rev. 32
**überhaupt kein** positives Kriterium. Protokoll §9, T12-Ergänzung Rev. 32, benennt die
Ausfallklasse: eine Fehlkonfiguration, die den Lauf **nicht** durchfallen lässt, sondern **null
Findings ohne Fehlermeldung** erzeugt — die **stille Null**. Zwei Instanzen sind belegt, beide
**vor** der Kampagne gefunden: der per Aufrufzeile gesetzte Graphmodus (Rev. 31), der die vier
`CYCLE`-Injektionen stumm auf null fallen liesse, und das fehlende `DEPOT_SRC` (Rev. 32), unter
dem pytest in der **Sammelphase** abbricht und **0 von 23** Regeln laufen, ohne dass Exit-Code
oder Ausgabe diesen Fall von einem sauberen Lauf trennen.

Die Akzeptanzregel greift **generisch**, unabhängig davon, welche Fehlkonfiguration die
Regelmenge verkürzt hätte — sie ist keine Reaktion allein auf die beiden bekannten Fälle. **Als
Restrisiko benannt** und hier mitgeführt: eine Fehlkonfiguration, welche die Regelmenge
**vollzählig** lässt und dennoch das Ergebnis verschiebt, fängt auch diese Regel nicht.

---

## 6. Die T14-Gegenprobe an den K3-Kampagnenläufen

### 6.1 Die Auflage

Protokoll **§9 T14** (Rev. 30) legt auf: *„Die **B36a-Charakteristik** — Aufspaltung eines
Verstosses in zwei Findings, wechselnder Schema-Zweig — ist an den **ERSTEN
K3-Kampagnenläufen gegenzuprüfen** und das Ergebnis zu **berichten, gleich in welche Richtung
es ausfällt**. Bestätigt sie sich nicht, ist das ein Befund über die Vormessung, kein Anlass
nachzubessern: **nicht nachbessern, nur berichten** (Eine-Iteration-Regel, §7)."*

**Dieser Abschnitt ist rein deskriptiv.** Aus ihm folgt keine Handlung: kein Abbruch, keine
Änderung an Prompt, Schema, Metrik, Manifest oder Decision Record O.

### 6.2 Woran gemessen wurde

Gelesen sind die nach **Protokoll Rev. 44** / Auswertungsspezifikation **§1.9** gültigen
Läufe — das Artefakt, dessen **gehashtes Laufmanifest** `postrun.verdict == VALID` trägt, bei
mehreren gültigen Versuchen das **früheste** —, **nicht** die erstversuchten. Für vier der acht
Injektionen ist das ein Wiederholungsartefakt:

| Injektion | Versuchskette | gewähltes Artefakt |
|---|---|---|
| I01 | V1 VALID | `k3_439125ece20060321bff983d7b8295f1b33dda50` |
| I02 | V1 VALID | `k3_4165fab5c82b1194572461fdb232c1af264e66f5` |
| I03 | V1 VALID | `k3_b3fb12905f7f3becc803d1915af5654da35643bb` |
| I04 | V1 VALID | `k3_3de8357bc191821fe60922022be257c47959d35d` |
| I21 | V1 INVALID · V2 INVALID · **V3 VALID** | `k3_dd414657d12197a1ca79152d401f75eb4b5f5f57_r3` |
| I22 | V1 INVALID · **V2 VALID** | `k3_08a622b024e9174d7ce62863f385b369c8c27b12_r2` |
| I23 | V1–V5 INVALID · **V6 VALID** | `k3_28a75749496229bb1db37d85f68347572bd84c49_r6` |
| I24 | V1 VALID | `k3_91ed6a80d415c68eed7661a21ea554ba32da9c83` |

Der Commit des gewählten Laufmanifests ist je Injektion gegen `injection_sha256` des
Injektionsmanifests geprüft — **acht von acht deckungsgleich**.

### 6.3 (a) `FORBIDDEN_RELATION` — I01 bis I04, die Kontrolle

Diese Trägerform bietet **keine Wahl** zwischen Schema-Zweigen: ein Verstoss ist eine Kante,
und `subject` kann sie nur als `from`/`to` tragen. I01–I04 sind deshalb die **Kontrolle**, nicht
die eigentliche Gegenprobe.

| Injektion | LLM-Findings je Repetition | Schema-Zweig | `subject` über die drei Läufe | `rule_id` |
|---|---|---|---|---|
| I01 | **1 · 1 · 1** | `from`/`to` in 3/3 | konstant `{"from": "identity_repository", "to": "identity_services"}` | `R-LAYER-1` 3/3 |
| I02 | **1 · 1 · 1** | `from`/`to` in 3/3 | konstant `{"from": "orders_repository", "to": "orders_services"}` | `R-LAYER-1` 3/3 |
| I03 | **1 · 1 · 1** | `from`/`to` in 3/3 | konstant `{"from": "billing_repository", "to": "billing_services"}` | `R-LAYER-1` 3/3 |
| I04 | **1 · 1 · 1** | `from`/`to` in 3/3 | konstant `{"from": "identity_api", "to": "identity_repository"}` | `R-LAYER-1` 3/3 |

**Zwölf von zwölf LLM-Findings: ein Finding je injiziertem Verstoss, ein Schema-Zweig, ein
`subject`-Wert je Injektion über alle drei Repetitionen, die richtige `rule_id`.** Kein
`symbol`, kein `line` in keinem der zwölf.

> **Ein zweiter Record je Injektion, der nicht dem Modell gehört.** In `run_index 0` — und nur
> dort — steht bei allen vier Injektionen zusätzlich ein Record mit
> `source: "rule-engine"` und `rule_id: "DERIVED:forbidden-edge"`. Das ist der
> **deterministische Pfad**, der in K2/K3-Läufen mitläuft (§4 Nachtrag Rev. 25: die
> Konfiguration ist der **Mechanismus**, nicht der Aufruf; **K1** := Präfix `DERIVED:`,
> **K2/K3** := jedes andere `rule_id`). Er wird **vor** beiden Metriken herausgefiltert und ist
> **keine** Modellmeldung. Die Recordzahlen stehen im Laufmanifest getrennt
> (`records_by_mechanism`: `run_index 0` → 1 derived / 1 llm, `run_index 1` und `2` → je 0
> derived / 1 llm) und werden **nie summiert**. Er ist hier genannt, damit die Zahl „2 Findings
> in `run_index 0`" nicht mit der B36a-Aufspaltung verwechselt wird — sie ist etwas anderes.

### 6.4 (b) `FORBIDDEN_SIGNATURE_TYPE` — I21 bis I24, die eigentliche Gegenprobe

Diese Trägerform bietet den Zweig `offending_type` **überhaupt erst an** — und damit die Wahl,
an der B36a den wechselnden Schema-Zweig gemessen hat.

| Injektion | LLM-Findings je Repetition | Schema-Zweig | `subject` über die drei Läufe | Schreibweise | `rule_id` |
|---|---|---|---|---|---|
| I21 | **1 · 1 · 1** | `offending_type` in 3/3 | konstant `sqlalchemy.orm.Session` | **vollqualifiziert** 3/3 | `R-FRAMEWORK-1` 3/3 |
| I22 | **1 · 1 · 1** | `offending_type` in 3/3 | konstant `sqlalchemy.orm.Session` | **vollqualifiziert** 3/3 | `R-FRAMEWORK-1` 3/3 |
| I23 | **1 · 1 · 1** | `offending_type` in 3/3 | konstant `sqlalchemy.orm.Session` | **vollqualifiziert** 3/3 | `R-FRAMEWORK-1` 3/3 |
| I24 | **1 · 1 · 1** | `offending_type` in 3/3 | konstant `sqlalchemy.orm.Session` | **vollqualifiziert** 3/3 | `R-FRAMEWORK-1` 3/3 |

**Zwölf von zwölf LLM-Findings.** Kein `from`/`to`-Zweig in einem einzigen. **Keine einzige
verkürzte Schreibweise** — die in Protokoll Rev. 31 als Ausfallmodus **deklarierte** Kurzform
`sqlalchemy.orm` (im K2-Ruhezustand an 6 von 63 `R-FRAMEWORK-1`-Findings gemessen, sämtlich an
`*_view_models`-Zwillingen) tritt auf **keinem** der vier Träger auf. Kein derived Record: bei
diesen vier Injektionen steht `records_by_mechanism` in allen drei Repetitionen auf
0 derived / 1 llm.

### 6.5 (c) Gegenüberstellung zur B36a-Charakteristik, Merkmal für Merkmal

Links steht der Wortlaut aus `b36a_bericht_k3_varianzlauf.md`, rechts die Kampagnenerhebung.

| Merkmal | B36a, wörtlich | K3-Kampagne (I01–I04 und I21–I24) |
|---|---|---|
| **Zahl der Findings je Verstoss** | „**Konstant über alle fünf Wiederholungen:** je **zwei** Findings für **einen** injizierten Verstoß, ohne Ausnahme" · „Aufspaltung als solche: der eine Verstoß wird durchgehend auf zwei Findings verteilt, nie auf eines zusammengezogen" | **Ein** LLM-Finding je Verstoss, in **24 von 24** Repetitionen. **Keine Aufspaltung, in keiner Injektion, in keiner Repetition.** |
| **Rollenverteilung** | „die Rollenverteilung kippt nie (Position 1 bezeichnet Import oder Kante, Position 2 die Signatur)" | **Gegenstandslos** — es gibt keine zweite Position. |
| **Schema-Zweig** | „Dabei schwankt nicht nur der Wert, sondern der **Schema-Zweig**: 3 von 5 tragen `offending_type`, 2 von 5 stattdessen `from`/`to`." | **Kein Wechsel.** I01–I04: `from`/`to` in 12/12 (die einzige mögliche Form). I21–I24: `offending_type` in 12/12 — die Form, die B36a in 3 von 5 Fällen trug, hier in 12 von 12. |
| **Konstanz des `subject`-Werts** | „**Nicht konstant: der Träger.** Vier verschiedene `subject`-Werte über zehn Findings … in drei verschiedenen Paarmustern" | **Konstant.** Je Injektion **ein** `subject`-Wert über alle drei Repetitionen; über die acht Injektionen acht verschiedene Werte, aber **null** Varianz innerhalb einer Injektion. |
| **Funktionsname statt Typ** | „in Position 2 steht mit `price_for_request` in 3 von 5 Wiederholungen der **Funktionsname**, nicht der Framework-Typ" | **Tritt nicht auf.** I21–I24 tragen in 12/12 den **Typ** `sqlalchemy.orm.Session`, nie den Namen der injizierten Methode (`Customer.reload`, `Order.reload`, `OrderLine.reload`, `Invoice.reload`). |
| **`rule_id`** | „`no-domain-framework-coupling` in allen zehn Findings — die richtige und einzige in Scope stehende Regel. Keine Abweichung." | **Deckungsgleich im Verhalten:** die richtige `rule_id` in **24 von 24** (`R-LAYER-1` bzw. `R-FRAMEWORK-1`). Keine Abweichung. |
| **`symbol` / `line`** | „Beide in allen zehn Findings null." | **Deckungsgleich:** beide in **24 von 24** null. |
| **Validität** | „`valid_raw` und `valid_final` true, `attempts_used: 1`, kein Repair, kein Transportverlust" | **Deckungsgleich für die gewählten Läufe:** `valid_final` true, `attempts_used: 1`, `calls_invalid: 0`, `calls_transport_failed: 0` in allen acht. |

**Ergebnis, in einem Satz:** die **B36a-Charakteristik bestätigt sich nicht** — weder die
Aufspaltung noch der wechselnde Schema-Zweig noch die Varianz des `subject`-Werts treten in den
gültigen K3-Kampagnenläufen auf; **konstant geblieben sind** dagegen die richtige `rule_id` und
das Fehlen von `symbol`/`line`.

**Die Erhebung widerspricht keiner im Repo bereits stehenden Zahl.** T4 des kanonischen Laufs
führt für I01–I04 und I21–I24 auf der K3-Seite durchgehend `[1,1,1]` je Repetition und die
Spalte Schreibvarianz auf `nein` — deckungsgleich mit dieser Auszählung.

### 6.6 (d) Der Vergleichsrahmen-Vorbehalt

**Dies ist eine Aussage über den VERGLEICH, keine Deutung des Ergebnisses.** B36a und die
Kampagne sind in mindestens vier Hinsichten nicht dasselbe Setup, und T14 sagt das selbst:

1. **Anderer Zugangsweg.** B36a lief über **OpenRouter** mit dem Slug
   `nvidia/nemotron-3-super-120b-a12b`, gepinnt auf `digitalocean` (`provider_served` je Call
   `DigitalOcean`). Gemessen wurde der **DigitalOcean-Direktzugang**
   `https://inference.do-ai.run/v1` mit der Katalog-`id` `nvidia-nemotron-3-super-120b`, **ohne
   Pin**, `provider_served` durchgehend `null`.
2. **Anderes Repositorium.** B36a lief auf einem **Wegwerf-Repo** (aus `setup.sh` frisch
   erzeugt, anderer `checker_git_head` `c493daf`, andere `topology_sha256`/`rules_sha256`);
   gemessen wurde `ma-conformance-testrepo` an der eingefrorenen Baseline unter
   `checker_git_head` `348ca9da…`.
3. **Andere Injektionsform.** B36a injizierte `from flask import Request` **und** eine Signatur
   `def price_for_request(request: Request)` in dasselbe Modul — einen Verstoss, der **zwei
   Angriffsflächen** (Import **und** Signatur) zugleich bietet. I21–I24 ändern nach Manifest
   **nur die Signatur** (`Customer.reload` u. a.), I01–I04 **nur eine Kante**. Dass ein
   Ein-Flächen-Verstoss nicht auf zwei Findings zerfällt, ist mit dieser Setupdifferenz
   verträglich.
4. **Andere Wiederholungszahl.** B36a `--runs 5`, die Kampagne `--runs 3`.

**Deshalb gilt:** die Gegenprobe zeigt, dass die B36a-Charakteristik **am gemessenen Setup nicht
auftritt**. Sie zeigt **nicht**, dass sie am B36a-Setup nicht aufträte, und sie ist **kein**
Beleg für Gewichtsidentität oder -differenz. Der Satz aus T14 bleibt unangetastet: **die
Identität der Gewichte ist nicht verifiziert.**

**Keine Folgehandlung.** T14 verlangt zu berichten, nicht nachzubessern. Prompt, Schema,
Metrik, Injektionsmanifest und Decision Record O bleiben unberührt.

---

## 7. Aufzeichnungslage

**Rohtext für alle 64 K4/K5-Aufrufe.** §6 Nachtrag Rev. 30 (2) verlangt stdout **und** stderr
jedes K4/K5-Aufrufs wörtlich und vollständig neben das Laufmanifest. Nachgezählt:

| | Dateien | stdout mit Inhalt | stderr leer (0 Bytes) | Bytes stdout gesamt |
|---|---|---|---|---|
| K4 | 32 + 32 | 32 | **32** | 49 872 |
| K5 | 32 + 32 | 32 | **32** | 42 669 |

**stderr ist in allen 64 Aufrufen leer** — import-linter und PyTestArch schreiben ihre
vollständige Ausgabe auf stdout und nutzen stderr im fehlerfreien Lauf nicht. Festgehalten,
nicht verändert. Der Text ist **nicht vorgeparst** und **nicht** über ein `stdout_tail`
gekürzt.

**Die Terminalbreiten-Prägung des K4-Rohtexts.** import-linter rendert über `rich`; eine
`rich`-Konsole, deren Datei kein Terminal ist, fällt auf **80 Spalten** zurück. Der Runner
erfasst stdout über eine Pipe (`tools/run_campaign.py:783`, `capture_output=True`), und
`COLUMNS` steht in der Runner-Umgebung nicht. Gemessen unter genau dieser Bedingung:
`console.width = 80`, `is_terminal = False`, `encoding = utf-8` (Auswertungsspezifikation §1.4,
Nachtrag C6b-2b). **Am Archiv nachgeprüft:** über alle 32 K4-stdout-Dateien (1363 Zeilen) ist
die **längste Zeile exakt 80 Zeichen** lang, keine ist länger; **eine** der 32 Dateien trägt
eine Zeile von exakt 80 Spalten, also einen Umbruchpunkt. **Die Bezeugung gilt für diese
Zeilenaufteilung**, nicht für eine beliebig nacherzeugte — deshalb stellt `tools/match_k4k5.py`
(`unwrap_k4`) die logische Zeile vor jedem Mustervergleich wieder her. K5 ist davon nicht
betroffen: pytest schreibt dort Zeilen bis 127 Zeichen.

**Umgebungsparameter je Lauf.** Aufgezeichnet ist je Invocation: die vollständige `argv`, die
gerenderte `command`-Zeile, `env_overrides` (API-Schlüssel als `<redacted>`), der absolute
Testrepo-Pfad, `cwd`, die Maschinenkennung samt Referenzwerten aus D2 M5(d), `checker_git_head`
mit Porcelain-Status, `dist_cli_js_sha256` mit `mtime`, der Freeze-Tag, `base_ref`,
`target_repo_git_head`, der abgeleitete Graphmodus mit Quellenangabe, die vollständige
Ausgabe des Soll-Validators, für K2 die gemessene Kontextfenstergrösse und für K4 der
grimp-Cache-Zustand vor und nach dem Lauf. Die vier Auflagen aus §6 Nachtrag Rev. 30 sind damit
belegt; die Liste „NICHT AUFZEICHNUNGSGEDECKT" ist leer.

**Vorbedingungen je Lauf.** Über alle 96 deterministischen Laufmanifeste einheitlich:
`git status --porcelain` im Testrepo und im Checker-Repo vor jedem Lauf leer, Soll-Validator
Punkte (1)–(5) „all OK", die commit-scharfe (6)-Erwartung mitgeschrieben, ebenso (7) und (8);
die **I1-Prüfung (Validatorpunkt 4) in allen 96 aufgezeichnet** statt unterdrückt (§3 Rev. 12)
— **0** Verletzungen.

**Was bewusst ungehasht bleibt.** Sieben lebende Dokumente stehen in keinem `SHA256SUMS`
(Protokoll Rev. 39, §0.1 Punkt 7): `data/soll/MANIFEST.md`, `data/campaign/MANIFEST.md`,
`k2/MANIFEST.md`, `k3/MANIFEST.md`, `data/campaign/README.md`, `data/campaign/journal.jsonl`
und `data/campaign/control/journal.jsonl`. Ein Hash wäre für sie das falsche Instrument — er
risse bei jeder legitimen Fortschreibung. Ihre Integrität liefert die Commit-Historie, dazu ein
**Schnappschuss-Hash** im Manifest. Eine **achte** ungelistete Datei ist im Prüfer ein
Fehlschlag, keine Ausnahme.

---

## 8. Abweichungen und Zwischenfälle

Vollständig, in der Reihenfolge ihres Auftretens. Je Fall: **was passierte**, **wie es
auffiel**, **was daraus registriert wurde.**

### 8.1 Der Abbruch am Soll-Validator, Punkt (6), bei I07 — und die sechs verworfenen K2-Invocationen

**Was passierte.** Der Kampagnenlauf C10 schrieb am 27.08.2026 ab 08:25:20 sechs
K2-Invocationen (I01–I06) und brach dann an **I07** ab:

```
ABORT: Soll validator failed for I07:
  validator point (6): core_adapters_internal   importers = 2 ['core_adapters', 'identity_services']
```

`run_soll_validator` behandelte die Validator-Punkte (1)–(6) einheitlich als
**commit-invariant**. Punkt (6) — Z2′ (ii), „sole importer per component" — prüft aber die
Importeursmenge von fünf geschützten Komponenten und ist damit eine Eigenschaft des
**Codegraphen**, nicht des **Soll-Modells**. Eine `FORBIDDEN_RELATION`-Injektion, deren Ziel im
Ruhezustand genau einen Importeur trägt, verletzt den Punkt **zwangsläufig** — sie zieht ja
gerade einen zweiten ein. Betroffen waren **I07, I08 und I09** (alle drei mit Ziel
`core_adapters_internal`), und zwar in **allen fünf Konfigurationen**, weil
`run_soll_validator` unbedingt vor der Verzweigung nach K1…K5 steht.

**Wie es auffiel.** Der Runner brach ab, **bevor ein Call entstand** — die Prüfung hat
funktioniert, ihr Kriterium war falsch.

**Was daraus registriert wurde.**
1. Die sechs Invocationen sind **verworfen**, nicht ausgewertet und nicht committet: alle **19
   Dateien** wurden gehasht und nach `~/scratch/c10a/abgebrochener_k2_teilbestand/` verschoben;
   die vollständige Hashliste steht in `c10a_bericht_validator_punkt6.md` §2. Sie waren unter
   dem **alten** Runner-Stand (`b6f9972`) entstanden und durften nicht in denselben Block wie
   die Neumessung geraten.
2. **K2 ist vollständig neu gefahren** worden, damit der Block geschlossen unter **einem**
   Runner-Commit steht (`4caf083`).
3. Die acht Validator-Punkte sind **klassifiziert** worden — (1)–(5) commit-invariant, (6), (7)
   und (8) commit-variant (`c10a_bericht_validator_punkt6.md` §4).
4. Die Erwartung für (6) wird seither **berechnet, nicht gewählt**: aus dem whitelisted
   Importeur je geschützter Komponente (gelesen aus `depot_soll.ilograph.yaml`) und der
   Quellkomponente der registrierten `expected_edge_boundary` des Manifesteintrags. **Die
   Prüfung wurde dadurch schärfer, nicht lockerer** — Rev. 34 verglich eine **Zahl**
   (`len(importers) == 1`), Rev. 35 vergleicht die **Menge**; eine Schärfeprobe gegen vier
   falsche Mengen bricht in allen vier Fällen ab, darunter einer, den die alte Fassung
   durchgelassen hätte.
5. **Protokoll Rev. 35** registriert den Fix; `4caf083` ist der Commit, der ihn trägt.

### 8.2 Die Aufrufspezifikations-Defekte vor dem Runnerbau

**Was passierte.** Auftrag C7 (Kampagnen-Runner bauen) ist am 26.08.2026 in **Schritt 0**
abgebrochen worden, **bevor eine Zeile Runner geschrieben und bevor ein Call abgesetzt war**.
Zwei vorregistrierte Aufrufzeilen waren defekt:

- **A1 — K5: `DEPOT_SRC` fehlt.** Die Protokollzeile (§6 Nachtrag Rev. 24) trug die Variable
  nicht; `data/soll/test_architecture.py` leitet `root_path` **und** `module` aus ihr ab und
  wirft ohne sie in der **Sammelphase**. Der Ausfall wäre **still** gewesen: 0 von 23 Regeln
  laufen, und weder Exit-Code noch Ausgabe trennen den Fall von einem sauberen Lauf.
- **A2 — K3: zwei verbindliche Aufrufzeilen im selben Protokoll.** §6 Nachtrag Rev. 24 trug
  weiter den OpenRouter-Block (`CONFORMANCE_BASE_URL=https://openrouter.ai/api/v1`,
  `CONFORMANCE_MODEL=nvidia/nemotron-3-super-120b-a12b`,
  `CONFORMANCE_PROVIDER_PIN=digitalocean`), während §1 Nachtrag Rev. 30 den
  **DigitalOcean-Direktzugang** für verbindlich erklärt hatte. Sachlich war der Widerspruch
  aufgelöst (Rev. 30 ist jünger); **dokumentarisch war er es nicht** — ein Runner, der die
  vorregistrierten Zeilen wörtlich übernimmt, hätte **wählen** müssen.

**Wie es auffiel.** Beim **Lesen** der vorregistrierten Aufrufzeilen in Schritt 0, gegen die
Abbruchregel des Auftrags: *„Weicht eine Zeile zwischen zwei Dokumenten ab oder fehlt eine:
ABBRECHEN und melden, nichts rekonstruieren."* Die naheliegende Selbsthilfe — die fehlende
Umgebungsvariable aus einem Bericht zu ergänzen — ist **unterblieben**: eine aus drei Quellen
zusammengesetzte Aufrufzeile ruht nicht mehr auf der Vorregistrierung, sondern auf der
Auslegung des Ausführenden.

**Was daraus registriert wurde** — **Protokollrevision Rev. 32**, fünf Punkte: die K5-Zeile um
`DEPOT_SRC` ergänzt (Alttext gestrichen sichtbar); beide K3-Zeilen auf den Direktzugang gezogen
(ebenso); die **positive Lauf-Akzeptanzregel** für K4 und K5 neu eingeführt (§5 dieses
Berichts); die K4-Schreibform festgelegt; **§9 T12** um die Ausfallklasse „stille Null durch
Fehlkonfiguration bei den Konfigurationen ohne Laufprotokoll" ergänzt, mit beiden Instanzen.
**C7 ist danach unverändert neu gestartet.** Dass die Korrektur in der Kampagne tatsächlich
stand, ist in §1.5 belegt: `DEPOT_SRC` in 32 von 32 K5-Invocationen, der DO-Endpunkt in 61 von
61 K3-Invocationen, kein `CONFORMANCE_PROVIDER_PIN` in keiner.

Dieser Fall trägt **keine Befundnummer**: es ist ein **Spezifikationsdefekt**, keine Messung.
Er ist in `c7_abbruch_bericht_aufrufspezifikation.md` dokumentiert.

### 8.3 Der Artefaktauswahldefekt

**Was passierte.** Die Auflösungsregel der Auswertungsharness lautete
`<cfg>_*<injection_sha256>.json` und traf damit die Datei **ohne** `_r<n>`-Suffix, also den
**ersten** Versuch. Für **elf K3-Injektionen** — **I05, I06, I07, I09, I11, I13, I16, I20,
I21, I22, I23**, genau die nach V1 offenen — trägt dieses Artefakt im gehashten Laufmanifest
`postrun.verdict = INVALID` mit Grund `transport_failure`. Die ersten drei Auswertungsläufe
haben damit genau das getan, was Protokoll §7 ausschliesst: **stille Zählung invalider Läufe als
„0 Findings"**. K2 war nicht betroffen (null Wiederholungen). **T7 wies die Gültigkeit dabei die
ganze Zeit korrekt aus** — die Auswertung las an ihrer eigenen, richtig gedruckten
Gültigkeitstabelle vorbei.

**Wie es auffiel.** Durch die mechanische Auszählung in
`c11d_bericht_befund08_grundlagen.md` §A6b — **beauftragt vor dem Schreiben von Befund 08**,
nicht als Suche nach einer Erklärung für eine unbefriedigende Zahl.

**Was daraus registriert wurde.** Protokoll **Rev. 44** / Auswertungsspezifikation **§1.9**:
gelesen wird das Artefakt, dessen **gehashtes Laufmanifest** `postrun.verdict == VALID` trägt,
bei mehreren gültigen Versuchen das **früheste**. Das ist eine **Artefaktauswahlregel, keine
Metrikänderung** — `strict`, `localized`, Precision, Recall, F1, Median, Spannweite, FP-Rate
und die vier Marker stehen zeichengleich. Dazu die Zusicherung **R12**: der Lauf bricht mit
**Exit 2** ab, sobald ein Artefakt gelesen wird, dessen Laufmanifest kein `VALID` trägt;
negativ probiert an der alten Namensregel am echten Bestand (Probe P18: **11 Verstösse, genau
die elf Injektionen, Exit 2**).

**Die vollständige Darstellung dieses Befundes samt Wirkung auf die Zahlen steht in
`docs/befunde_log.md` Befund 08, 08.10** und wird hier nicht wiederholt.

### 8.4 Zwei benannte, folgenlose Umgebungsdifferenzen

Der Vollständigkeit halber, beide **vor** der Kampagne registriert und beide belegt statt
angenommen:

- **Node-Version** (T13, Rev. 31): auf dem Messrechner läuft **v22.23.2**, in C3a protokolliert
  war **v22.22.2**. Folgenlos, weil der Gatterbeleg der **Build-Hash** von `dist/cli.js` ist,
  und der stimmt zeichengleich; alle übrigen Werkzeugstände sind gegen C3a §1 identisch. Die
  Kampagnenmanifeste bezeugen `v22.23.2` in 189 von 189.
- **Runner-Provenienz im K2-Blockmanifest** (C6b-1): die Zeile trug zunächst `bd422b1` — den
  Repo-HEAD zum Laufzeitpunkt — statt `4caf083`, des letzten Commits, der eine der drei
  Runner-Dateien berührt. **Der Runner-Code war identisch** (Datei für Datei gegengeprüft); es
  bewegte sich keine Messung, kein Artefakt und keine Zahl. Korrigiert wurde eine
  **Provenienzangabe**, weil das Gesamtmanifest **eine** Runner-Zeile führt und damit
  stillschweigend behauptete, alle fünf Blöcke stünden unter demselben Wert — sie tun es; die
  Zeile sagte es falsch.

---

## 9. Die vier Auswertungsläufe

Über den hier dokumentierten Rohbestand sind **vier** Auswertungsläufe gefahren worden. Sie
liegen alle vollständig und gehasht unter `data/campaign/eval/`; **keiner ist überschrieben oder
nachbearbeitet**.

| # | Ausgabe | Auftrag · Protokoll | Status |
|---|---|---|---|
| 1 | `c11_eval_full` | C11 · Rev. 39 | überholt, gültig archiviert |
| 2 | `c12_eval_full` | C11b · Rev. 41 | überholt, gültig archiviert |
| 3 | `c13_eval_full` | C11c · Rev. 43 | überholt, gültig archiviert |
| 4 | **`c14_eval_full`** | **C14 · Rev. 45** | **KANONISCH** |

**Kanonisch ist genau ein Lauf, und er heisst `c14_eval_full`.** Warum jeweils ein weiterer Lauf
nötig wurde, welche Reparatur welchen Lauf von seinem Vorgänger trennt und wie sich die Zellen
zwischen c13 und c14 bewegt haben, steht in
[`data/campaign/eval/README.md`](../../data/campaign/eval/README.md); die Ergebnisse selbst
stehen in `c14_eval_full.md` / `.json` und in Befund 08. **Hier wird beides nicht wiederholt.**

---

## 10. Belegquellen mit Hashes

**Gehashte Bestände** (je Block aus der Repowurzel mit `sha256sum -c` prüfbar; maschinell
mitgeprüft von `tools/check_doc_invariants.py`, Invariante D):

```
d8b840aedd393183d2d1009c3cf32bce6fa6e8f5947c5c7adb5a3abe8e7f83cd  data/soll/SHA256SUMS                (7 Zeilen)
ced9954f333936dc20630f91b275f63a47e7e69f9d530bf8a0abe5680ead6907  data/campaign/k1/SHA256SUMS         (96 Zeilen)
debd5a93309e682126de886928b6fcc1c9ba4e2dd9548d2037f33512ac1bb26e  data/campaign/k2/SHA256SUMS         (96 Zeilen)
7023d23663ba022dff98a4d888cde16e3f3b198849144344a6ba83a1281bfb88  data/campaign/k3/SHA256SUMS        (183 Zeilen)
cc8dbce674920d2a61f9954eca3fa6eb766e971705283f8ca4321fa9906f29d0  data/campaign/k4/SHA256SUMS         (96 Zeilen)
07ff89aaff4956afc2dfb3b88efa7b3fa548dcc8d4978c49a56677ba3b0d0741  data/campaign/k5/SHA256SUMS         (96 Zeilen)
c9699b4417833a6a6a006ce51ce5062589c3c4a1266bb6ea5579539ac2b8fdda  data/campaign/control/SHA256SUMS    (14 Zeilen)
703485ed75317bd8dfdcf7d71832bdd9212d8c32894719574c3cccbc341a6026  data/campaign/eval/SHA256SUMS        (9 Zeilen)
```

**Lebende Dokumente** (bewusst ungehasht, Protokoll Rev. 39 §0.1 Punkt 7 — hier als
**Schnappschuss** zum Berichtsstand 29.08.2026):

```
36d6e80561a3d1f259a85db6ccf76e91224b5477cbcbd0784c0236ca3578415e  data/campaign/MANIFEST.md
8ad3faac1bf783f3ef03d8b3701d4f8be08d6090dad400a5002ade53747cfbaf  data/campaign/k2/MANIFEST.md
5dd72f9bc6b7e0d31609659b78a802fb6b442e9c9580d524d05201d80100a731  data/campaign/k3/MANIFEST.md
5db059bcbc9d163275fe084ece610ccce45e7c74d070974f08d191c508f7a0c9  data/campaign/README.md
d044619ea9dcc7a44367ccb1b3c24e7b3cb4f8db4b848c0a4d5a1004ce15b8cd  data/campaign/control/MANIFEST.md
e594e77dbe94197616ac6963fa253f6d083f66bb56899fba861962f0297d3335  data/campaign/journal.jsonl        (189 Zeilen)
c835e3d765cdbf4967fa8c4b3c95900afde867eb1a826d1596411388d1242793  data/campaign/control/journal.jsonl  (4 Zeilen)
```

**Protokoll, Spezifikation, Runner:**

```
2cb0385f08e88333863d83d0819943e352d3f1b857d4870801211b4817ac181e  eval_protokoll_phase04.md  Rev. 33 — FREEZE, Beleg der Vorregistrierung (c5b §3)
0ce57d29110214d13e888e44750b6ee3ae1e5a934aebaeb116883d005ff92eca  eval_protokoll_phase04.md  Rev. 45 — Stand bei Berichtserstellung
2f1354bbabdfaef8c858a6726521e224c30d6293513d83ea98cd1ef3f6608f97  c6_auswertungsspezifikation.md — Stand zum Freeze (c5b §2)
39822edc0d9c109d7f1c1cfc285af9dd1363ec48b1a96a69334c173cd2cd71c7  c6_auswertungsspezifikation.md — Stand der Auswertung
eba3b95a0bfb21192f6b49ed6a3e02c4c1d26ec68e2abd1a8f2de939b07e62c4  tools/run_campaign.py    | Runner
c95d38140f00ee1d1823d9c96a03fbcbff28f94a96281ce940772b6944a63995  tools/campaign_spec.py   | Commit
d179dcba0530c6806ce964d282611ee680b674f69497a0fde46aa4a980ed9d31  tools/postrun_check.py   | 4caf083
```

**Messstand der Kampagne** (aus den Artefakten nachgemessen, §1.3):

```
348ca9daa456af4954f11f7152fc45201035297e                          Checker, Tag phase04-freeze
c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95  packages/triton-conformance/dist/cli.js
e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d  topology_sha256   (depot_soll.ilograph.yaml)
72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95  rules_sha256      (architecture-rules.yaml)
65e78f38e7b1fee20000ea70c654df042f5e0831fc6a68ccb340f833bd915035  prompt_template_sha256
45780c70c486ea8f608d1b2ca11178049a02b7a6ece9ba33fcdc8d1b815b03ef  user_prompt_render_sha256
0d651041ed87dd03f2f78359713633fac01c0a66                          Testrepo, Tag baseline (= --base)
```

**Kanonischer Auswertungslauf** (nur benannt, hier nicht ausgewertet):

```
46ba024d266398cea278103592daf12c2a04193f9b45caa4812ce20333cc0a71  data/campaign/eval/c14_eval_full.json
ed59aa95f01b2a73e773110e5aa56b45b6d687c49f812dcca1bad8ed65e2329b  data/campaign/eval/c14_eval_full.md
```

**Berichte, aus denen dieser Bericht Wortlaute zitiert** (nicht Zahlen — Zahlen stammen
durchgehend aus den Artefakten): `c5b_bericht_protokoll_freeze.md` §2 und §3,
`c10a_bericht_validator_punkt6.md` §2–§6, `c7_abbruch_bericht_aufrufspezifikation.md` §1, §2
und §5, `b36a_bericht_k3_varianzlauf.md` (die B36a-Charakteristik in §6.5),
`c11d_bericht_befund08_grundlagen.md` §A6b, `c14_bericht_vierter_lauf.md` §2.5,
`c6b1_bericht_nachtraege.md` (Ruhezustandsblock). Protokollstellen: §0.1, §2 Rev. 11, §3
Rev. 12, §4 Nachtrag Rev. 25, §6 Nachträge Rev. 24, 26, 30, 31 und Rev. 32, §7, §9 T12/T13/T14,
§10.
