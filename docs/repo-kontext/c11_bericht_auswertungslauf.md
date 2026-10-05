# C11 — Auswertungslauf über den vollständigen Messbestand

**Auftrag:** C11 — der erste und einzige Lauf der Auswertungsharness über
`data/campaign/`. Ein Lauf, ausgeführt am 28.08.2026.

**Deutungssperre.** Dieser Bericht führt Laufmetadaten, Zusicherungsergebnisse,
strukturelle Vollständigkeit, die Listen der Harness und die Ausgabepfade. Er enthält
**keine** Deutung der Werte, keinen Vergleich zwischen Konfigurationen, keine Empfehlung
und keine Ursachenhypothese.

---

## 1 Vorbedingungen

### 1.1 Vier Bäume sauber, kein Runner aktiv, HEAD wie verlangt

```
$ for d in ma-conformance-testrepo masterarbeit tritongraph tritongraph-measure; do
      git -C $d status --porcelain; done
(alle vier leer)

$ git -C masterarbeit rev-parse HEAD
dc865d1aa90fb0816ac5f9d7bcd268025fdfe9bf
$ git -C masterarbeit log --oneline -1
dc865d1 docs: report the pre-evaluation corrections

$ git -C tritongraph            rev-parse --short HEAD   → 348ca9d
$ git -C ma-conformance-testrepo rev-parse --short HEAD   → 0d65104
$ git -C tritongraph-measure     rev-parse --short HEAD   → 348ca9d

$ ps aux | grep -Ei "evaluate_campaign|run_campaign|tritongraph|checker" | grep -v grep
(keine)
```

`masterarbeit` stand vor dem Lauf auf `dc865d1`. Schreibend war ausschliesslich
`masterarbeit`; die drei übrigen Bäume wurden nur gelesen.

### 1.2 Prüfer — Ausgabe wörtlich

```
check_doc_invariants — Repo /home/haasentimo/ma/masterarbeit

[OK ] (A) Protokoll-SHA gegen c5b_bericht_protokoll_freeze.md §3
        SHA256 9e63c37067a5a62ef95dd2d0710620939b9f03e5b0258995f01e597db5653f48
        bezeugt in c5b_bericht_protokoll_freeze.md §3 als Rev. 39

[OK ] (B) Kopf-Revision = §10-Höchstzeile = neuester Historieneintrag
        Kopf Rev. 39 = Revisionshistorie Rev. 39 = §10-Zeile 39

[OK ] (C) Spezifikations-SHA gegen Protokoll §1 UND §0.1
        SHA256 50f593d07801dd421aad1e644016bf4861af382afbc41749546e1ecad8785017, an beiden Stellen zeichengleich
        §0.1 (Messstand): 50f593d07801dd421aad1e644016bf4861af382afbc41749546e1ecad8785017
        §1 (Nachtrag Rev. 30): 50f593d07801dd421aad1e644016bf4861af382afbc41749546e1ecad8785017

[OK ] (D) sha256sum -c UND Listing beidseitig, data/soll und data/campaign
        OK   data/soll: 7 von 7 OK
        OK   data/campaign/control: 14 von 14 OK
        OK   data/campaign/k1: 96 von 96 OK
        OK   data/campaign/k2: 96 von 96 OK
        OK   data/campaign/k3: 183 von 183 OK
        OK   data/campaign/k4: 96 von 96 OK
        OK   data/campaign/k5: 96 von 96 OK
        
        OK   Listing gegen SHA256SUMS, beide Richtungen:
             602 Dateien in 13 Verzeichnissen geprüft, 588 Pfade gelistet
             AUSNAHME lebende Dokumente, 7 von 7 entschiedenen — Protokoll Rev. 39; ein achter ungelisteter Pfad ist ein FEHLSCHLAG, keine Ausnahme
             MELDUNG  data/soll/MANIFEST.md — lebendes Dokument: Herleitungsdoku der sieben Messeingaenge, selbst kein Messeingang (0.1 fuehrt sieben von sieben) — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/MANIFEST.md — lebendes Dokument: fortzuschreibendes Kampagnenmanifest, seit C6c-a Gegenprobe zu T7, nicht dessen Quelle — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/README.md — lebendes Dokument: Ablagebeschreibung, traegt keinen Messwert — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/journal.jsonl — append-only und planmaessig wachsend: ein Hash risse bei jeder legitimen Fortschreibung; seit C6c-a Gegenprobe zu T7, nicht dessen Quelle — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/control/journal.jsonl — append-only und planmaessig wachsend: Journal des Kontrollbestands, dessen Laufmanifeste und Rohartefakte sehr wohl gehasht sind — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/k2/MANIFEST.md — lebendes Dokument: fortzuschreibendes Blockmanifest — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/k3/MANIFEST.md — lebendes Dokument: fortzuschreibendes Blockmanifest — entschieden C6c-a 28.08.2026, Protokoll Rev. 39

[OK ] (E) SHA256 der drei Auswertungsinstrumente gegen Protokoll §0.1
        OK   tools/evaluate_campaign.py  5125cd595913b1226b888e67035f24f2831e0f4818b28dad4b261a57a0528eed
        OK   tools/match_k4k5.py  ad3edcb1ee8537ee758d8212055371957c0493f3d8e218267d182fb9fc060022
        OK   tools/check_doc_invariants.py  6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018

ERGEBNIS: alle 5 Invarianten erfüllt
EXIT=0
```

Exit 0. Damit sind Protokoll, Spezifikation, die sieben `data/`-Bestände und die drei
Instrumenten-Hashes gegen §0.1 geprüft.

### 1.3 `git diff -- tools/` leer, Instrumenten-SHA gezeigt

```
$ git diff -- tools/
(leer)
$ git diff --stat HEAD -- tools/
(leer)

$ sha256sum tools/evaluate_campaign.py tools/match_k4k5.py tools/check_doc_invariants.py
5125cd595913b1226b888e67035f24f2831e0f4818b28dad4b261a57a0528eed  tools/evaluate_campaign.py
ad3edcb1ee8537ee758d8212055371957c0493f3d8e218267d182fb9fc060022  tools/match_k4k5.py
6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018  tools/check_doc_invariants.py
```

Zeichengleich mit den in §0.1 registrierten Werten — Invariante (E) des Prüfers oben
führt dieselben drei Zeilen. Gezeigt, nicht angenommen.

### 1.4 `sha256sum -c` in allen Blockbeständen von `data/campaign/`

Die Block-`SHA256SUMS` unter `data/campaign/` tragen **repo-wurzelrelative** Pfade und
werden deshalb aus der Repo-Wurzel geprüft (`data/soll/SHA256SUMS` trägt Basisnamen und
wird aus seinem eigenen Verzeichnis geprüft — dieselbe Auflösung, die `verify_sums` im
Prüfer vornimmt).

| Bestand | Exit | OK | FAILED |
| --- | --- | --- | --- |
| `data/campaign/control` | 0 | 14 | 0 |
| `data/campaign/k1` | 0 | 96 | 0 |
| `data/campaign/k2` | 0 | 96 | 0 |
| `data/campaign/k3` | 0 | 183 | 0 |
| `data/campaign/k4` | 0 | 96 | 0 |
| `data/campaign/k5` | 0 | 96 | 0 |
| `data/soll` | 0 | 7 | 0 |

Alle Vorbedingungen erfüllt. Der Lauf wurde daraufhin ausgeführt.

---

## 2 Der Lauf

### 2.1 Aufrufzeile, wörtlich

```
python3 tools/evaluate_campaign.py --with-campaign \
    --json-out data/campaign/eval/c11_eval_full.json \
    --markdown-out data/campaign/eval/c11_eval_full.md
```

Die Eingabepfade sind die Vorgabewerte des Instruments und decken den im Auftrag
genannten Bestand: `--soll data/soll`, `--control-k2 data/c3b-k2`,
`--control-k3 data/c3b-k3`, `--campaign data/campaign`.

| Feld | Wert |
| --- | --- |
| Zeitstempel Start | 2026-08-28T13:16:10+02:00 |
| Zeitstempel Ende | 2026-08-28T13:16:11+02:00 |
| Laufzeit | 0,29 s Wanduhr, 23 868 KB maxrss |
| `cwd` | `/home/haasentimo/ma/masterarbeit` |
| git HEAD | `dc865d1aa90fb0816ac5f9d7bcd268025fdfe9bf` |
| Maschine | DESKTOP-PJA89CF · Linux 5.15.153.1-microsoft-standard-WSL2 x86_64 |
| Exit | **0** |
| `stdout` | leer (beide Ausgaben gingen in Dateien) |
| `stderr` | **leer** |

Der Lauf lief im Hintergrund, damit ein Werkzeug-Timeout einen nicht wiederholbaren Lauf
nicht abschneiden kann. Er endete regulär mit Exit 0.

**Leeres `stderr` heisst:** keine `MARKERVERLETZUNG`, kein `HARNESS-FEHLER`, kein
`HARNESS-BEFUND: T7-Gegenprobe weicht ab`, keine `BLINDHEITSVERLETZUNG`. Kein Exit 2,
kein Exit 3. Der Abbruchpfad des Auftrags wurde nicht betreten.

### 2.2 Ausgabekopf

Das Instrument erzeugt von sich aus keinen Ausgabekopf, und Instrumente zu ändern ist
nicht Gegenstand dieses Auftrags. Der vom Auftrag verlangte Kopf wurde deshalb **nach**
dem Lauf mechanisch und inhaltserhaltend eingefügt:

- **Markdown:** der Kopf ist **vorangestellt**; das Rendering beginnt darunter mit seiner
  ersten Zeile und ist bytegleich mit der Rohausgabe.
- **JSON:** **ein** Schlüssel `c11_run_head` ist unmittelbar nach der öffnenden Klammer
  eingefügt; alle übrigen Bytes sind unverändert. Die Datei bleibt gültiges JSON.

Beides ist nachgerechnet: der Rumpf beider Dateien ist bytegleich zur Rohausgabe
(SHA256 des Rumpfes = SHA256 der Rohausgabe, geprüft). **Keine Zelle wurde angefasst,
nichts umformatiert, kein Wert nachbearbeitet.** Die SHA256 der Rohausgabe **vor**
Kopfeinfügung stehen im Kopf selbst und hier:

| Datei | SHA256 der Rohausgabe (vor Kopf) |
| --- | --- |
| `c11_eval_full.json` | `28fc40bb334f73615b669cda45eccd8cca62d71d49aa613d429ddd0e2075283c` |
| `c11_eval_full.md` | `aecba18c8187f8bdd2693883cf46406687f42fd7ce55e7cd9809793af43c8df5` |

Der Kopf trägt in beiden Ausgaben: Auftrag, Zeitstempel, Laufzeit, `cwd`, git HEAD,
Maschinenkennung, Aufrufzeile, Exit, SHA256 der drei Instrumente, SHA256 des Protokolls
und der Spezifikation, die Blockhashes und Artefaktzahlen von `data/campaign/`, die
SHA256 der Rohausgabe und die Beschreibung der Kopfeinfügung.

Die im Kopf geführten Blockhashes (SHA256 des jeweiligen Block-`SHA256SUMS`):

| Block | SHA256 des `SHA256SUMS` | gelistete Artefakte |
| --- | --- | --- |
| control | `c9699b4417833a6a6a006ce51ce5062589c3c4a1266bb6ea5579539ac2b8fdda` | 14 |
| k1 | `ced9954f333936dc20630f91b275f63a47e7e69f9d530bf8a0abe5680ead6907` | 96 |
| k2 | `debd5a93309e682126de886928b6fcc1c9ba4e2dd9548d2037f33512ac1bb26e` | 96 |
| k3 | `7023d23663ba022dff98a4d888cde16e3f3b198849144344a6ba83a1281bfb88` | 183 |
| k4 | `cc8dbce674920d2a61f9954eca3fa6eb766e971705283f8ca4321fa9906f29d0` | 96 |
| k5 | `07ff89aaff4956afc2dfb3b88efa7b3fa548dcc8d4978c49a56677ba3b0d0741` | 96 |

Laufmanifeste unter `data/campaign/manifests/`: 189 JSON-Dateien.

Protokoll `9e63c37067a5a62ef95dd2d0710620939b9f03e5b0258995f01e597db5653f48`,
Spezifikation `50f593d07801dd421aad1e644016bf4861af382afbc41749546e1ecad8785017`.

---

## 3 Strukturprüfung — Zahlen

### 3.1 Zellen je Tabelle

Gezählt sind die **Datenzellen** der gerenderten Tabellen: Kopfzeile und Trennzeile
ausgenommen, die erste Spalte (Zeilenbezeichner) ausgenommen. Jede Tabelle wurde
blockweise gegen ihre eigene Kopfbreite geparst; **Breitenfehler: 0** in allen Blöcken,
die Zählung sitzt also auf der tatsächlichen Tabellengeometrie auf.

| Tabelle | Blöcke | Zeilen | Zellen | gefüllt | ` — ` | `n. b.` | `n. e.` | *(leer)* |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| T1 | 1 | 10 | 110 | 84 | 14 | 2 | 0 | 10 |
| T7.1 | 2 | 10 | 65 | 65 | 0 | 0 | 0 | 0 |
| T7.2 | 1 | 4 | 16 | 15 | 0 | 1 | 0 | 0 |
| T7.3 | 1 | 5 | 20 | 20 | 0 | 0 | 0 | 0 |
| T7.4 | 1 | 29 | 174 | 174 | 0 | 0 | 0 | 0 |
| T2 | 1 | 10 | 120 | 89 | 29 | 2 | 0 | 0 |
| T3 | 2 | 6 | 42 | 40 | 2 | 0 | 0 | 0 |
| T3.1 | 4 | 13 | 62 | 62 | 0 | 0 | 0 | 0 |
| T4 | 2 | 64 | 800 | 580 | 16 | 0 | 0 | 204 |
| T5 | 1 | 40 | 360 | 96 | 72 | 27 | 0 | 165 |
| T6 | 1 | 5 | 45 | 0 | 12 | 2 | 0 | 31 |
| T8 | 1 | 10 | 50 | 50 | 0 | 0 | 0 | 0 |
| T9 | 1 | 10 | 50 | 48 | 0 | 0 | 0 | 2 |
| **Summe** | **19** | **216** | **1914** | **1323** | **145** | **34** | **0** | **412** |

`*(leer)*` ist ein in der Ausgabe selbst geführter Zustand („von diesem Lauf nicht
eingesetzt", Markerlegende der Harness). Die 412 leeren Zellen verteilen sich spaltenweise
so:

| Tabelle | Spalte | leer |
| --- | --- | ---: |
| T1 | Abweichung | 10 |
| T4 (17 Spalten) | `K2 kein-EN` | 7 |
| T4 (17 Spalten) | `K3 kein-EN` | 5 |
| T4 (10 Spalten) | `K1 Kampagne`, `K1 Δ`, `K4 Kampagne`, `K4 Δ`, `K5 Kampagne`, `K5 Δ` | je 32 |
| T5 | `strict` P / R / F1 | je 28 |
| T5 | `loc` P / R / F1 | je 27 |
| T6 | Invocationen, Model-Calls, Wanduhr aussen Summe, Wanduhr aussen je Invocation | je 5 |
| T6 | Wanduhr innen (`wall_clock_ms`) | 3 |
| T6 | Tokens in / Tokens out / Tokens je Check / Latenz je Call | je 2 |
| T9 | Häufigkeit | 2 |

### 3.2 Zusicherung „keine Zelle trägt 0, wo ein Marker gilt" — grün

Die Zusicherung ist im Instrument als Abbruchbedingung verdrahtet:
`assert_marker_discipline` prüft `strict` und `localized` jeder Injektion in jeder
Konfiguration und beendet den Lauf mit **Exit 2** und `MARKERVERLETZUNG` auf `stderr`,
sobald eine Zelle eine 0 trägt, wo ` — ` oder `n. e.` gilt. Der Lauf endete mit
**Exit 0** bei leerem `stderr` — die Zusicherung ist **grün**, geprüft über
32 Injektionen × 5 Konfigurationen × 2 Metriken = 320 Zellenprüfungen.

Ebenso grün die zweite verdrahtete Kontrollregel: jedes `n. e.` in T2/T4/T5 braucht eine
Entsprechung in T7.3, sonst `HARNESS-FEHLER` und Exit 2. Nicht ausgelöst.

### 3.3 `n. e.`-Liste — leer

```
t7.missing = {"K1": [], "K2": [], "K3": [], "K4": [], "K5": []}
```

Leer in allen fünf Konfigurationen, wie erwartet. Passend dazu 0 `n. e.`-Zellen in der
Zählung oben. `manifest_missing` = `{"K2": [], "K3": []}`.

### 3.4 Abweichungsliste zu T1

Die Spalte **Abweichung** der T1-Tabelle ist in allen zehn Zeilen **leer**.

Sie ist im Renderer unbedingt leer gesetzt — die Zeile wird als
`… + " | ".join(ist) + " | |"` geschrieben (`tools/evaluate_campaign.py:1215-1216`), es
gibt keinen Rechenweg, der in diese Spalte schriebe. Die Harness erzeugt in dieser Spalte
also **keine** Abweichungsliste; die zehn leeren Zellen sind kein berechnetes „keine
Abweichung".

**Das wird hiermit gemeldet und nicht behoben.** Der Lauf wurde nicht wiederholt, am
Instrument nichts geändert. Ob dies ein Defekt der Harness ist und was daraus folgt, ist
eine Entscheidung ausserhalb dieses Auftrags (Defektregel Rev. 38 Punkt 6).

### 3.5 Gegenprobe Journal gegen Laufmanifeste

Aus `t7.crosscheck_journal`, Quelle sind die gehashten Laufmanifeste, Gegenprobe ist
`journal.jsonl`:

| Konfiguration | Invocationen (Journal) | VALID (Journal) | `journal_missing` | `divergences` |
| --- | ---: | ---: | --- | --- |
| K1 | 32 | 32 | leer | **leer** |
| K2 | 32 | 32 | leer | **leer** |
| K3 | 61 | 32 | leer | **leer** |
| K4 | 32 | 32 | leer | **leer** |
| K5 | 32 | 32 | leer | **leer** |

**Deckungsgleich** in allen fünf Konfigurationen; keine Abweichung auszuweisen. Passend
dazu blieb `stderr` frei von `HARNESS-BEFUND` (Rev. 39: Ausweis, Exit 0 auch bei
Abweichung).

### 3.6 Laufzeit, gelesene Dateien, Blindheitsauditierung

| Grösse | Wert |
| --- | ---: |
| Laufzeit | 0,29 s Wanduhr |
| gelesene Dateien gesamt (`reads.total`) | 565 |
| davon Kampagnen-Laufartefakte | 160 |

Der Lauf lief mit `--with-campaign`; das Lesen der Laufartefakte ist damit zugelassen und
wird von der Harness als Liste ausgewiesen statt als Verletzung (ohne den Schalter wäre
es Exit 3). Gelesene Klassen von Laufartefakten:

| Block | Klasse | Anzahl |
| --- | --- | ---: |
| k1 | `k1_diff_<sha>.json` | 28 |
| k1 | `k1_full_<sha>.json` | 4 |
| k2 | `k2_<sha>.json` | 32 |
| k3 | `k3_<sha>.json` | 32 |
| k4 | `k4_<sha>.stdout.txt` | 32 |
| k5 | `k5_<sha>.stdout.txt` | 32 |
| | **Summe** | **160** |

Je Konfiguration 32 Artefakte, entsprechend 32 Injektionen. Die übrigen 405 gelesenen
Dateien sind Soll-Bestand, Laufmanifeste und die Kontrollläufe `data/c3b-k2/`,
`data/c3b-k3/`.

---

## 4 Ausgabepfade und SHA256

Beide Dateien liegen unverändert (Rumpf bytegleich, siehe §2.2) unter
`data/campaign/eval/` und sind mit `data/campaign/eval/SHA256SUMS` bezeugt:

| Pfad | SHA256 |
| --- | --- |
| `data/campaign/eval/c11_eval_full.json` | `ad8f0483ffd2c261d8e33a21c425c5f6a492dedae0cc99c4e135dc56b371ea30` |
| `data/campaign/eval/c11_eval_full.md` | `3d4874842a5baf92d455c1140b4874d396550fe87c50714d537a15a0a0e595af` |

Archiviert und committet **vor** diesem Bericht:
`5b2f284 data: archive the first evaluation run over the complete campaign`.

Der Prüfer erfasst das neue Verzeichnis von selbst — er läuft mit `rglob("SHA256SUMS")`
über `data/campaign/` und vergleicht das Listing beidseitig; beide Ausgabedateien sind
gelistet, `SHA256SUMS` ist wie überall selbstbefreit. Kein achter ungelisteter Pfad.

---

## 5 Prüfer nach dem Archivierungs-Commit

Derselbe Prüfer, nach dem Commit `5b2f284`, mit dem neuen Verzeichnis:

```
check_doc_invariants — Repo /home/haasentimo/ma/masterarbeit

[OK ] (A) Protokoll-SHA gegen c5b_bericht_protokoll_freeze.md §3
        SHA256 9e63c37067a5a62ef95dd2d0710620939b9f03e5b0258995f01e597db5653f48
        bezeugt in c5b_bericht_protokoll_freeze.md §3 als Rev. 39

[OK ] (B) Kopf-Revision = §10-Höchstzeile = neuester Historieneintrag
        Kopf Rev. 39 = Revisionshistorie Rev. 39 = §10-Zeile 39

[OK ] (C) Spezifikations-SHA gegen Protokoll §1 UND §0.1
        SHA256 50f593d07801dd421aad1e644016bf4861af382afbc41749546e1ecad8785017, an beiden Stellen zeichengleich
        §0.1 (Messstand): 50f593d07801dd421aad1e644016bf4861af382afbc41749546e1ecad8785017
        §1 (Nachtrag Rev. 30): 50f593d07801dd421aad1e644016bf4861af382afbc41749546e1ecad8785017

[OK ] (D) sha256sum -c UND Listing beidseitig, data/soll und data/campaign
        OK   data/soll: 7 von 7 OK
        OK   data/campaign/control: 14 von 14 OK
        OK   data/campaign/eval: 2 von 2 OK
        OK   data/campaign/k1: 96 von 96 OK
        OK   data/campaign/k2: 96 von 96 OK
        OK   data/campaign/k3: 183 von 183 OK
        OK   data/campaign/k4: 96 von 96 OK
        OK   data/campaign/k5: 96 von 96 OK
        
        OK   Listing gegen SHA256SUMS, beide Richtungen:
             605 Dateien in 14 Verzeichnissen geprüft, 590 Pfade gelistet
             AUSNAHME lebende Dokumente, 7 von 7 entschiedenen — Protokoll Rev. 39; ein achter ungelisteter Pfad ist ein FEHLSCHLAG, keine Ausnahme
             MELDUNG  data/soll/MANIFEST.md — lebendes Dokument: Herleitungsdoku der sieben Messeingaenge, selbst kein Messeingang (0.1 fuehrt sieben von sieben) — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/MANIFEST.md — lebendes Dokument: fortzuschreibendes Kampagnenmanifest, seit C6c-a Gegenprobe zu T7, nicht dessen Quelle — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/README.md — lebendes Dokument: Ablagebeschreibung, traegt keinen Messwert — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/journal.jsonl — append-only und planmaessig wachsend: ein Hash risse bei jeder legitimen Fortschreibung; seit C6c-a Gegenprobe zu T7, nicht dessen Quelle — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/control/journal.jsonl — append-only und planmaessig wachsend: Journal des Kontrollbestands, dessen Laufmanifeste und Rohartefakte sehr wohl gehasht sind — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/k2/MANIFEST.md — lebendes Dokument: fortzuschreibendes Blockmanifest — entschieden C6c-a 28.08.2026, Protokoll Rev. 39
             MELDUNG  data/campaign/k3/MANIFEST.md — lebendes Dokument: fortzuschreibendes Blockmanifest — entschieden C6c-a 28.08.2026, Protokoll Rev. 39

[OK ] (E) SHA256 der drei Auswertungsinstrumente gegen Protokoll §0.1
        OK   tools/evaluate_campaign.py  5125cd595913b1226b888e67035f24f2831e0f4818b28dad4b261a57a0528eed
        OK   tools/match_k4k5.py  ad3edcb1ee8537ee758d8212055371957c0493f3d8e218267d182fb9fc060022
        OK   tools/check_doc_invariants.py  6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018

ERGEBNIS: alle 5 Invarianten erfüllt
EXIT=0
```

Exit 0. Die beiden Ausgabedateien sind gelistet und geprüft (`data/campaign/eval: 2 von 2 OK`); die Listing-Gegenprobe zählt jetzt 605 Dateien in 14 Verzeichnissen, 590 gelistete Pfade — die drei zusätzlichen Dateien und das zusätzliche Verzeichnis sind die Archivierung dieses Laufs.

---

## 6 Was dieser Auftrag nicht getan hat

Ein Lauf, kein zweiter. Keine Änderung an Instrumenten, Skelett, Spezifikation oder
Protokoll. Kein Befund 08, kein C10-Abschlussbericht, keine Kapitelprosa, kein
Standdokument, keine Wurzel-README, kein Arbeitsplan, keine Gate-Notiz, kein Z1, L1,
A-38. Kein `git push`.
