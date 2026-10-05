# C11b — Metrikentscheidung, Instrumentenreparatur, zweiter Auswertungslauf

**Auftrag:** C11b, 28.08.2026. Drei Phasen mit harten Gattern: eine Metrikbildung als
Protokollrevision, die Reparatur der Auswertungsinstrumente mit Verifikation **vor** dem
Lauf, und der zweite Auswertungslauf mit Gegenüberstellung jeder geänderten Zelle.

**Deutungssperre.** Berichtet werden **Mechanik, Zahlen und Zellendifferenzen**. Keine
Bewertung, ob ein Ergebnis gut, schlecht oder überraschend ist; kein Vergleich zwischen
Konfigurationen; keine Empfehlung zu Prompt, Schema, Regeldatei, Manifest oder
Metrikdefinition über die in Phase 1 beauftragte hinaus.

**Der erste Auswertungslauf ist unverändert.** `data/campaign/eval/c11_eval_full.json`
und `…md` sind nicht überschrieben, nicht gelöscht, nicht nachbearbeitet; beide Hashes
sind vor und nach dem zweiten Lauf geprüft. Der zweite Lauf liegt **daneben**.

---

## 0 Vorbedingungen

```
$ for d in masterarbeit tritongraph ma-conformance-testrepo tritongraph-measure; do
      git -C $d status --porcelain; done
(alle vier leer)

$ git -C masterarbeit log --oneline -1
db2c9d8 docs: diagnose the gaps in the first evaluation run

$ ps aux | grep -Ei "evaluate_campaign|run_campaign|tritongraph|checker" | grep -v grep
(keine)

$ python3 tools/check_doc_invariants.py
ERGEBNIS: alle 5 Invarianten erfüllt                       → Exit 0
```

**Der archivierte erste Lauf, gezeigt statt angenommen:**

```
$ sha256sum -c data/campaign/eval/SHA256SUMS
data/campaign/eval/c11_eval_full.json: OK
data/campaign/eval/c11_eval_full.md: OK                    → rc=0
```

---

## 1 Phase 1 — die Metrikentscheidung als Protokollrevision 40

Commit **`3b1b818`** „docs: amend the protocol for the single-stage kein-EN comparison".

### 1.1 Die Frage, wie C11a sie hinterlassen hat

`Kampagne` ist der **Median** der Zählwerte je Lauf, `strict` ein **Existenzquantor** über
alle Läufe. kein-EN verknüpft beide (`hit and camp_med <= rest_med`) und bezeichnet dadurch
bei `[0,0,1]` etwas anderes als bei `[1,1,1]` (`c11a_bericht_diagnose.md` §3.5,
Arbeitslistenpunkt 11 — **„OFFEN — benannt, nicht entschieden"**).

### 1.2 (a) Die gewählte Stufe: die EXISTENZSTUFE

```
kein-EN = "ja"    wenn strict = 1  UND  Ruhe-Existenz = 1
        = "nein"  wenn strict = 1  UND  Ruhe-Existenz = 0
        = entfällt  wenn strict = 0                (dritter Zustand, unverändert)

Ruhe-Existenz = 1, wenn die Ruhezustandszählgrösse desselben Moduls in derselben
                   Kategorie in MINDESTENS EINEM der drei C3b-Läufe > 0 ist.
```

**Begründung.** Der Wortlaut aus Rev. 31 — „ein `strict`-Treffer, der die Ruhezustandsrate
nicht übersteigt" — macht **den `strict`-Treffer zum Subjekt** des Vergleichs. `strict` ist
nach §4 ein Existenzquantor über die Repetitionen; das ist eine **Metrikdefinition** und
steht seit dem ersten Kampagnenlauf unter der Sperre aus §0.1 Punkt 2. Die Stufe, die der
Wortlaut trägt, ist damit die des Subjekts. Die Kampagnenseite des Vergleichs **ist** der
`strict`-Treffer; die Ruhezustandsseite wird auf **dieselbe** Stufe gebracht.

**Beide Kandidaten, gegenübergestellt** — gerechnet am 28.08.2026 aus den
Kampagnenartefakten und `data/c3b-k2/`, `data/c3b-k3/`, **vor** dem zweiten Lauf:

| | **A — Existenzstufe** *(gewählt)* | **B — Medianstufe** *(verworfen)* |
|---|---|---|
| Kampagnenseite | `strict` (Existenz über 3 Läufe), **unverändert** | Median der `strict`-Treffer je Lauf („Treffer in ≥ 2 von 3 Läufen") |
| Ruhezustandsseite | Existenz über 3 C3b-Läufe | Median über 3 C3b-Läufe, unverändert |
| bewegte Zeilen K2 | **2** von 32 — I10, I12 (`nein`→`ja`) | **1** von 32 — I19 (`ja`→leer) |
| bewegte Zeilen K3 | **4** von 32 — I06, I20, I21 (`ja`→`nein`), I30 (`nein`→`ja`) | **3** von 32 — I06, I20, I21 (`ja`→leer) |
| Richtung | **beide** — 3 Zeilen je Seite | nur **eine** — 4 Zeilen verlassen `ja` |
| bewegt eine **vorregistrierte** Zelle? | **nein** | **JA — vier `strict`-Zellen** (I06/K3, I19/K2, I20/K3, I21/K3 von 1 auf 0) und mit ihnen T1, T2, T4 und T5 |

**Kandidat B ist unabhängig von seinen Zahlen nicht wählbar:** er verschiebt eine
Metrikdefinition **nach** Sichtung der Daten — genau das, was §0.1 Punkt 2 ausschliesst.
Die Begründung steht **vor** den Zahlen, nicht hinter ihnen.

**Kein Ergebnis wird verbessert.** Bei K2 steigt die Zahl der Zeilen ohne
Erkennungsnachweis von **20 auf 22**, bei K3 sinkt sie von **4 auf 2**. „kein
Erkennungsnachweis" ist die für das Werkzeug **ungünstige** Buchung; die Wahl macht sie für
K2 häufiger und für K3 seltener.

**Nicht geändert, ausdrücklich:** die Spalten `Ruhe`, `Kampagne` und `Δ` bleiben auf dem
Median (eigenständige paarweise Auslesart nach §7.5 (4); kein-EN liest sie seither nicht
mehr) · der **Filterunterschied** `match_key` gegen Trägermodul + Kategorie bleibt bestehen
und ist als Lesevorbehalt benannt — Rev. 40 legt die **Stufe** fest, nicht den Filter ·
`strict`, `localized`, Precision, Recall, F1, Median, Spannweite, FP-Rate.

### 1.3 (b) Die neue T4-Spalte

Je Konfiguration **`Läufe (Ruhe · Kampagne)`**: die drei Repetitionszählwerte **einzeln**,
Form `[0,0,0] · [0,0,1]`, in `run_index`-Reihenfolge. **Rein deskriptiv** — keine Wertung,
keine Aggregation, kein Eingang in irgendeine Rechnung. Zweck: ein Median `0` über `[0,0,1]`
und einer über `[0,0,0]` sind als gedruckte Zelle nicht unterscheidbar und tragen doch
verschiedene Buchungen.

### 1.4 (c) Die abgelehnte Ursachenaufspaltung — registriert

Eine Spalte, die kein-EN nach der Ursache in „Rauschen" und „Instabilität" trennte, ist
**ausdrücklich abgelehnt** und in Protokoll Rev. 40 sowie Spezifikation §7.5 (6) als
Ablehnung registriert. Begründung: eine **neue, nach Sicht auf die Daten gebildete
Klassifikation** — die Klassen existierten vor dem ersten Auswertungslauf nicht, ihre Grenze
läge an genau den Zeilen, die sie sortieren soll (§0.1 Punkt 4). Der Ursachenunterschied
(C11a §3.6) gehört in die **Prosa von Kapitel 7**, belegt aus der neuen Läufespalte.

### 1.5 (d) Der Zeitpunkt, ungeschminkt

Die Entscheidung folgt dem **ersten Auswertungslauf** und der Diagnose **C11a**. Sie ist
im Protokoll an allen drei Stellen als solche registriert. Zulässig ist sie, weil sie eine
**Metrikbildung** ist und keine **Metrikdefinition**: der Wortlaut aus Rev. 31 bleibt
zeichengleich, seine Umsetzung wird auf **eine** Stufe gebracht.

**Registriert an allen Stellen:** Kopf (Rev. 40, Alttext gestrichen sichtbar),
Revisionshistorie, §10 — und zwar in der Tabelle **„Amendments nach Messbeginn"**, deren
erste Zeile Rev. 40 ist, mit der Spalte **Re-Run** ausgefüllt. Mitgezogen: Spezifikation
§7.5 (3) präzisiert, §7.5 (5) und (6) neu, SHA an beiden registrierten Stellen; Skelett T4
um die Spalte erweitert; Protokoll-SHA in `c5b_bericht_protokoll_freeze.md` §3.
**Prüfer Exit 0.**

---

## 2 Phase 2 — die Reparatur, je mit Fundstelle

Commits **`c8e31d4`** (Handrechnung, allein), **`7e7b7c5`** (Buchung, Nullen, Zusicherung),
**`3f7862e`** (P/R/F1, Kostentabelle, Abweichungsspalte), **`93089db`** (Hash-Nachzug).

| # | Reparatur | Fundstelle | Commit |
|---|---|---|---|
| **R1** | Zusicherung **keine markerfreie Leerzelle**, über **alle** Tabellen, geprüft am **fertig gerenderten** Text, Exit 2 — mit expliziter, kurzer Ausnahmeliste | [`evaluate_campaign.py:1189`](../../tools/evaluate_campaign.py#L1189) (`EMPTY_CELL_ALLOWED`), [1198](../../tools/evaluate_campaign.py#L1198) (`table_empty_cells`) | `7e7b7c5` |
| **R2** | gerechnete Nullen werden als `0` gedruckt; eigene Zusicherung, dass keine gerechnete Grösse zu einer Leerzeichenkette rendert | [`evaluate_campaign.py:229`](../../tools/evaluate_campaign.py#L229) (`num`) | `7e7b7c5` |
| **R3** | **T5 implementiert** — Precision, Recall, F1 je Kategorie und beide Gesamtzeilen, fünf Konfigurationen, `strict` und `localized` getrennt | [`evaluate_campaign.py:1458`](../../tools/evaluate_campaign.py#L1458) (`Score`), [1500](../../tools/evaluate_campaign.py#L1500) (`score_rows`), [1551](../../tools/evaluate_campaign.py#L1551) (`t5_row`) | `3f7862e` |
| **R4** | **T6 gerendert** — Invocationen, Model-Calls, beide Wanduhren aus den gehashten Laufmanifesten; Tokens und Latenz aus den `llm_call`-Records | [`evaluate_campaign.py:667`](../../tools/evaluate_campaign.py#L667) (`outer_clock`), [673](../../tools/evaluate_campaign.py#L673) (`inner_clock`), [896](../../tools/evaluate_campaign.py#L896) (`call_costs`) | `3f7862e` |
| **R5** | **T4-Symmetrieteil** für K1/K4/K5, Kampagne und Δ; Ruhezustandsseite bleibt der gekennzeichnete Berichtswert `0` ᴬ¹⁴ | [`evaluate_campaign.py:1130`](../../tools/evaluate_campaign.py#L1130) (`k4k5_campaign_count`) | `7e7b7c5` |
| **R6** | **T1-Abweichungsspalte** — Rechenweg Soll gegen Ist je Zeile; leere Zelle = „berechnet, keine Abweichung", an der Spalte vermerkt | [`evaluate_campaign.py:1568`](../../tools/evaluate_campaign.py#L1568) (`ist_verdict`), [1607](../../tools/evaluate_campaign.py#L1607) (`t1_divergence`) | `3f7862e` |
| **R7** | **T9 Fall 7** aus einer **benannten Sonderklasse** statt aus `specials`; **Fall 6** als gerechnete Zahl statt als Leerzelle | [`match_k4k5.py:807`](../../tools/match_k4k5.py#L807) (`T9_CASE_7`), [`evaluate_campaign.py:1041`](../../tools/evaluate_campaign.py#L1041) (`is_case_6`) | `7e7b7c5` |
| **R8** | **Join-Buchung Fall 7 repariert** — über die Klassifikation des Parsers, **nicht** auf Zeichenketten geflickt | [`match_k4k5.py:792-807`](../../tools/match_k4k5.py#L792-L807) (benanntes Vokabular, `LOCALIZED_HIT`, `special_class`), [`evaluate_campaign.py:1053`](../../tools/evaluate_campaign.py#L1053) (`evaluate_k4k5_injection`) | `7e7b7c5` |
| **R9** | **T9 in Skelettform** — sieben Zeilen, sieben Nummern, Pfad `K2/K3`, Spalte *vorregistriert in* | [`evaluate_campaign.py:1952`](../../tools/evaluate_campaign.py#L1952) ff. | `7e7b7c5` |

### 2.1 R8 im Einzelnen — warum nicht am Literal geflickt

Der erste Lauf verwarf die vier K5/`CYCLE`-Funde an **zwei** Zeichenkettenvergleichen:
`classification == "treffer"` (der Parser liefert `begleitmeldung`) und
`localized == "treffer"` (der Parser liefert `treffer (richtige Stelle, falsche Kategorie)`).

**Repariert ist die Buchungsregel, nicht der Vergleich.** `tools/match_k4k5.py` benennt
sein `localized`-Vokabular (`LOC_TREFFER`, `LOC_STELLE`, `LOC_KEIN`, `LOC_NB`) und die
Menge der Verdikte, die einen Treffer **auf der Stelle** bezeichnen (`LOCALIZED_HIT`);
jeder Fund trägt zusätzlich eine **benannte Sonderklasse** (`special_class`, Werte `T9-3`
und `T9-7`). Der Join fragt diese Namen:

```python
strict_hit    = any(f.get("strict_eligible") is True for f in findings)
localized_hit = any(f.get("localized") in match_k4k5.LOCALIZED_HIT for f in findings)
preregistered = [f for f in findings if f.get("special_class")]
```

`strict_eligible is True` ist **schärfer** als „Klassifikation ist Treffer": K4/
`INCORRECT_LOCATION` ist ein Treffer, der ausdrücklich **nicht** `strict`-fähig ist
(Fussnote 5). Der Zähler von T9 Zeile 7 liest aus `special_class`, nicht aus einem Eimer,
den der Fall sich mit anderen teilt.

**Vorregistrierte Fassung getroffen:** `strict` kein Treffer, `localized` **Treffer auf der
Stelle** (Fussnote 7, Rev. 22) — und in T5 **weder TP noch FP noch FN**, vor der Rechnung
abgefangen (T5 Auflage (4)).

### 2.2 Zwei Defekte, die die Reparatur mitgefunden hat

Beide sind **vor** ihrer Behebung in `tests/fixtures/harness/EXPECTED.md` festgehalten und
in Protokoll Rev. 41 registriert:

1. **Die Zählgrösse filterte auf dem K1-Pfad ins Leere.** „Findings desselben Moduls in
   derselben Kategorie" verglich gegen `category_l1`; die Rule-Engine schreibt aber
   `layer-violation` bzw. `cycle`, nie einen Ebene-1-Namen. Die K1-Kampagnenzahl war in
   **jeder** Zeile 0. Folgenlos, solange die Spalte verworfen wurde (C11a Punkt 9) — mit dem
   Symmetrieteil sichtbar. Behoben durch denselben **pfadabhängigen** Kategoriewert, den
   `localized` schon benutzt (§4). **Für K2 und K3 ändert sich dadurch nichts.**
2. **Die `strict`-Falsch-Positiven wurden über die Läufe hinweg gebildet.** §3.2 ist eine
   **laufweise** Regel: je Lauf ein TP, jeder weitere Record desselben Laufs ein FP. Der
   alte Code liess die Trefferkennung über alle drei Repetitionen stehen und machte damit
   aus einem in der nächsten Repetition **wiederholten richtigen** Treffer ein
   Falsch-Positiv. Folgenlos, solange T5 leer war.

### 2.3 Was nicht weiter gefasst wurde, als vorregistriert ist

**T9 Fall 6 ist auf die vorregistrierte Fassung begrenzt.** Spezifikation §5 Fall 6 nennt
`FORBIDDEN_RELATION`; ein Record am Trägermodul einer `CYCLE`-Injektion mit **anderer**
Kategorie ist **nicht** Fall 6 und fällt unter die Allgemeinregel **FP *und* FN**. Im
Messbestand sind das **3 K2-Records** mit `API_CONTRACT`. Sie werden in T9 Zeile 6
**ausgewiesen**, nicht absorbiert. Eine weitere Fassung hätte Falsch-Positive entfernt, die
die Vorregistrierung nie entfernt hat — die Ad-hoc-Regel zugunsten des eigenen Werkzeugs,
die das Skelett bei T9 ausschliesst.

---

## 3 Verifikation VOR dem Lauf

### 3.1 (a) Handrechnung zuerst, allein committet

`tests/fixtures/harness/EXPECTED.md` §11–§15, Commit **`c8e31d4`** — **allein**, und **vor**
jeder Zeile Reparaturcode. Zum Zeitpunkt dieses Commits ist die Harness unrepariert: T5
leer, T6 leer, die Fall-7-Buchung greift nicht, kein-EN auf der alten Mischstufe. Keine
dieser Zahlen kann von einer Maschine abgelesen sein.

Enthalten: die Rechenvorschrift für P/R/F1 mit den vier Ausschlüssen in ihrer bindenden
Reihenfolge, TP/FP/FN je Injektion für alle fünf Konfigurationen, die erwartete T5-Tabelle
je Konfiguration, T9 in Skelettform mit den **zwei Fall-7-Prüffällen**, kein-EN auf der
Existenzstufe, die neue Läufespalte, der T4-Symmetrieteil und die zwei neuen Zusicherungen.

**Für R8 die zwei geforderten Fixture-Fälle:**

| Prüffall | Injektion | Rohtext nennt | Ergebnis |
|---|---|---|---|
| **positiv — wird gebucht** | I14/K5 | `depot.orders.mappers.order_mapper` → Ziel in `orders_api` | Trägermodul **und** Zielkomponente stimmen → Sonderklasse `T9-7` → T9 Zeile 7 zählt **1**, `localized` = Treffer, `strict` = 0, in T5 **nicht** enthalten |
| **negativ — wird NICHT gebucht** | I04/K5 | `depot.orders.api.routes` (Rohtext gehört zu I05) | Trägermodul stimmt **nicht** → `sonstiger_fund`, **keine** Sonderklasse → T9 zählt ihn nicht, er ist ein **regulärer FP** in T5 |

**Eine Handrechnung ist dabei korrigiert worden**, mit Nachweis und durchgestrichenem
Alttext: I14/K5 `localized` stand in §5.4 und §8 als **0**. Fall 6 lässt die Matrixzelle
ausdrücklich auf `nein`, Fall 7 bewegt sie ausdrücklich auf `teilweise` — und **Rev. 22**
hat genau diese Bewegung in T1/T8 vollzogen. Eine `localized`-Zelle mit 0 kann sie nicht
tragen. Die Korrektur ist erfolgt, **weil der Fehler in der Handrechnung nachgewiesen ist**,
nicht weil eine Maschine etwas anderes sagt: die Harness lieferte zu diesem Zeitpunkt
weiterhin 0.

### 3.2 (b) Alle bestehenden Fixtures erneut

| Prüfung | Erwartet | Gemessen | |
|---|---|---|---|
| `match_k4k5.py --selftest` | 34 von 34 | **34 von 34, 0 Abweichungen** | ✅ |
| Selbsttest B — K2 modulweise je Lauf | 49 / 49 / 49 | 49 / 49 / 49 | ✅ |
| Selbsttest B — K2 Headline | **49/52** | **49/52** | ✅ |
| Selbsttest B — K2 findingweise | **461** (155/153/153) | 155 / 153 / 153, Summe **461** | ✅ |
| Selbsttest B — K3 modulweise je Lauf | 2 / 1 / 0 | 2 / 1 / 0 | ✅ |
| Selbsttest B — K3 Headline | **1/52** | **1/52** | ✅ |
| Selbsttest B — K3 findingweise | **3** (2/1/0) | 2 / 1 / 0, Summe **3** | ✅ |
| Harness gegen `tests/fixtures/harness/mini` | jede Zelle wie handgerechnet | **jede Zelle** aus T1, T2, T4, T5, T6 und T9 zeichengleich zur Handrechnung | ✅ |
| Fixture-Lauf mit `--with-campaign` | Exit 0, keine Leerzelle | **Exit 0** | ✅ |

### 3.3 (c) Alle Zusicherungen negativ probiert

| # | Zusicherung | Provokation | Ergebnis |
|---|---|---|---|
| P1 | `Cell.__post_init__` — Marker **und** Wert | `Cell(value=0, marker=" — ")` | `MarkerViolation: Zelle trägt Marker ' — ' UND Wert 0 …` |
| P2 | `Cell.__post_init__` — unbekannter Marker | `Cell(marker="n. x.")` | `MarkerViolation: unbekannter Marker 'n. x.'` |
| P3 | **R2** — gerechnete Grösse rendert leer | `num("")` · Gegenprobe `num(0)` | `MarkerViolation: gerechnete Grösse '' rendert zu einer Leerzeichenkette (R2)` · `num(0) = '0'` |
| P4 | `assert_marker_discipline` | Zelle mit ` — ` und Wert 0 an der Prüfung vorbeigeschmuggelt | zwei Meldungen: `Marker ' — ' und Wert 0` · `' — ' als 0 gebucht` |
| P5 | **R1** — Lokalisierung | eine gerechnete T4-Zelle auf `""` gesetzt | `LEERZELLE: T4 Zeile 244 (I02), Spalte 'K2 kein-EN'` — Tabelle, Zeile **und** Spaltenname |
| P6 | **R1** Ende-zu-Ende | `kein_en_cell` liefert `""` | 4 Meldungen + Sammelzeile, **Exit 2** |
| P7 | `n. e.` ohne T7-Beleg | ein Laufmanifest aus der Fixture-Kopie entfernt | `HARNESS-FEHLER: I02/K1 trägt n. e. ohne T7-Beleg`, **Exit 2** |
| P8 | Blindheit | ein Kampagnen-Laufartefakt geöffnet, Lauf **ohne** `--with-campaign` | `BLINDHEITSVERLETZUNG: …/campaign/k2/…json`, **Exit 3** |
| P9 | Blindheit deckt `control/` | `campaign/control/k1/probe.json` geöffnet | `BLINDHEITSVERLETZUNG: …/campaign/control/k1/probe.json`, **Exit 3** |
| P10 | T7-Gegenprobe weicht ab | Journalzeile K3/I25 auf `VALID` gesetzt | Banner im Kopf · 3× `ABWEICHUNG` in T7 · zwei `HARNESS-BEFUND`-Zeilen auf `stderr` · **Exit 0** (Befund, kein Defekt) |
| P11 | UF4-Nenner gegen T8 | `UF4_DENOMINATOR["K4"]` auf 18 gesetzt | `HARNESS-FEHLER: UF4-Nenner K4: 19 ausdrückbare Injektionen gegen vorregistrierte 18 (T8)`, **Exit 2** |
| P12 | Invariante (E) | Kommentarzeile an `match_k4k5.py` angehängt | `FEHL tools/match_k4k5.py`, IST gegen SOLL, **Exit 1** |

Nach jeder Probe `git checkout --` bzw. Wiederherstellung; der Baum war danach porcelain
leer.

### 3.4 Instrumenten-Hashes neu gebildet — Protokollrevision 41

Commit **`93089db`**. **Eine eigene Revision, obwohl reiner Bytestandsnachzug** — §0.1
Punkt 5: „jede Änderung am Protokoll ist eine Revision, auch ein reiner Hash-Nachzug, auch
eine Änderung, die inhaltlich nichts verschiebt". Rev. 40 hatte den Nachzug **angekündigt**;
vollzogen werden konnte er erst **nach** der Reparatur. Unter derselben Nummer vollzogen,
stünde der in `c5b §3` bezeugte Bytestand von Rev. 40 **in keinem Dokument mehr** — der
Ausfall aus C6b-2b, aus dem Rev. 36 diese Regel gemacht hat.

| Datei | Rev. 39 | Rev. 41 |
|---|---|---|
| `tools/evaluate_campaign.py` | `5125cd59…0528eed` | **`20bcdae0…23d306`** |
| `tools/match_k4k5.py` | `ad3edcb1…fc060022` | **`c16e7c43…799f4ca6`** |
| `tools/check_doc_invariants.py` | `6cc16ef9…1e52b7018` | **unverändert** |

```
$ python3 tools/check_doc_invariants.py
[OK ] (A) … [OK ] (B) … [OK ] (C) … [OK ] (D) … [OK ] (E)
ERGEBNIS: alle 5 Invarianten erfüllt                       → Exit 0
```

**Invariante (E) grün gegen die neuen Hashes.**

---

## 4 Phase 3 — der zweite Lauf

**Ein Lauf.** Vollständiger Bestand, unverändert gegenüber dem ersten (alle sechs
Block-`SHA256SUMS` zeichengleich).

```
$ python3 tools/evaluate_campaign.py --with-campaign \
    --json-out data/campaign/eval/c12_eval_full.json \
    --markdown-out data/campaign/eval/c12_eval_full.md
                                                           → Exit 0
```

| | |
|---|---|
| **Zeitstempel** | 2026-08-28T14:52:55+02:00 bis 2026-08-28T14:52:56+02:00 |
| **Laufzeit** | 0,27 s wall, 27 144 KB maxrss |
| **git HEAD** | `93089dbb863c5192b7f7dd221a119ea4d4900300` |
| **Protokoll** | Rev. 41, `e94150ae…67218e78` |
| **Spezifikation** | `be3491e2…acb21d6e1` |
| **gelesene Dateien** | **658** (erster Lauf: 565), davon **253** Kampagnen-Laufartefakte |
| **Ausgabe** | `data/campaign/eval/c12_eval_full.json` / `.md`, Kopf mit Instrumenten-, Protokoll-, Spezifikations- und Blockhashes vorangestellt |

**Sofort archiviert und committet**, vor jeder weiteren Arbeit: Commit **`3e7816f`**
„data: archive the second evaluation run after the instrument repairs", `SHA256SUMS`
ergänzt, `sha256sum -c` **4 von 4 OK**, Prüfer Exit 0.

**Die 93 zusätzlich gelesenen Dateien** sind die K2- und K3-Laufprotokolle (`*.jsonl`), aus
denen T6 Tokens und Latenz liest — ein Rechenweg, den es im ersten Lauf nicht gab.

---

## 5 Gegenüberstellung — jede geänderte Zelle

**Beide Ergebnisse bleiben ausgewiesen.** Der erste Lauf wird nicht ersetzt.

### 5.1 Bilanz

| | |
|---|---|
| Datenzellen erster Lauf | **1 926** |
| Datenzellen zweiter Lauf | **1 982** (+56) |
| **vergleichbare Zellen** (gleiche Tabelle, Zeile, Spalte; ohne Schlüsselspalte) | **1 899** |
| davon **UNVERÄNDERT** — gezählt, nicht aufgelistet | **1 396** |
| davon **GEÄNDERT** | **503** |
| Zellen in **neuen Spalten** | **71** — T4 `Läufe (Ruhe · Kampagne)` 2 × 32 = 64, T9 *vorregistriert in* 7 |
| Zellen in **entfallenen Zeilen** | **15** — die drei doppelten T9-Nummern 4, 5 und 6 |
| Markerlegende vor T1 (unverändert) | 12 |

Abgleich: 1 899 + 71 + 12 = **1 982** = Datenzellen des zweiten Laufs.

### 5.2 Geänderte Zellen je Tabelle und Grund

| Tabelle | geändert | davon aus einer **leeren** Zelle | Grund |
|---|---:|---:|---|
| **T1** | 6 | 4 | 2 × **R8** (Ist K5), 4 × **R6** (Abweichungsspalte) |
| **T2** | 2 | 0 | **R8** |
| **T4** | 210 | 176 | 192 × **R5** (Symmetrieteil K1/K4/K5, Kampagne und Δ) · 18 × **Phase 1 (a)** (kein-EN) |
| **T5** | 237 | 165 | **R3** — 165 aus leer; 72 sind eine **Darstellungsabweichung**, siehe §7 |
| **T6** | 31 | 31 | **R4** |
| **T9** | 17 | 1 | **R7** (Häufigkeiten), **R9** (Skelettform), **R2** (gerechnete 0) |
| **Summe** | **503** | **377** | |

### 5.3 Die einzeln aufgeführten Zellen

Aufgelistet sind **alle** Zellen aus T1, T2, T9 und die kein-EN-Zellen von T4. Die
Massenfüllungen — T4-Symmetrieteil (192), T5 (165 aus leer), T6 (31) — sind in §5.4 als
Gruppe geführt, weil sie sämtlich denselben Grund und dieselbe Richtung haben: **aus leer
in einen gerechneten Wert**.

| Tabelle | Zeile | Spalte | erster Lauf | zweiter Lauf |
|---|---|---|---|---|
| T1 | `CYCLE_PARENT_CHILD` | Ist K5 | 0/1 | 1/1 |
| T1 | `CYCLE_PARENT_CHILD` | Abweichung | *(leer)* | K4 `n. b.` (kein Vergleich bildbar) |
| T1 | `CYCLE_SIBLING` | Ist K5 | 0/3 | 3/3 |
| T1 | `CYCLE_SIBLING` | Abweichung | *(leer)* | K4 `n. b.` (kein Vergleich bildbar) |
| T1 | `FRAMEWORK_TYPE_IN_SIGNATURE` | Abweichung | *(leer)* | **K3: Soll ja / Ist teilweise** |
| T1 | `INCORRECT_LOCATION` | Abweichung | *(leer)* | **K2: Soll ja / Ist teilweise** |
| T2 | `CYCLE_PARENT_CHILD` (1) | K5 loc | 0/1 | 1/1 |
| T2 | `CYCLE_SIBLING` (3) | K5 loc | 0/3 | 3/3 |
| T4 | I06 | K3 kein-EN | ja | nein |
| T4 | I10 | K2 kein-EN | nein | ja |
| T4 | I12 | K2 kein-EN | nein | ja |
| T4 | I13 | K2 kein-EN | *(leer)* | ` — ` |
| T4 | I13 | K3 kein-EN | *(leer)* | ` — ` |
| T4 | I14 | K2 kein-EN | *(leer)* | ` — ` |
| T4 | I14 | K3 kein-EN | *(leer)* | ` — ` |
| T4 | I15 | K2 kein-EN | *(leer)* | ` — ` |
| T4 | I15 | K3 kein-EN | *(leer)* | ` — ` |
| T4 | I16 | K2 kein-EN | *(leer)* | ` — ` |
| T4 | I16 | K3 kein-EN | *(leer)* | ` — ` |
| T4 | I17 | K2 kein-EN | *(leer)* | entfällt |
| T4 | I20 | K2 kein-EN | *(leer)* | entfällt |
| T4 | I20 | K3 kein-EN | ja | nein |
| T4 | I21 | K3 kein-EN | ja | nein |
| T4 | I23 | K3 kein-EN | *(leer)* | entfällt |
| T4 | I28 | K2 kein-EN | *(leer)* | entfällt |
| T4 | I30 | K3 kein-EN | nein | ja |
| T9 | 1 | Fall | `CYCLE`-Injektion (Modus `full`) erzeugt zusätzlich `layer-violation` | `CYCLE`-Injektion (Modus `full`) erzeugt zusätzlich `layer-violation` auf derselben Kante |
| T9 | 1 | Buchungsregel | `expected_co_findings`; **kein FP** | `expected_co_findings` im Manifest; **kein FP** |
| T9 | 2 | Fall | `FORBIDDEN_RELATION` erzeugt **keinen** `cycle`-Record | `FORBIDDEN_RELATION`-Injektion (Modus `diff`) erzeugt **keinen** `cycle`-Record |
| T9 | 2 | Betroffen | `FORBIDDEN_RELATION`-Injektionen | I01, I02, I03, I04, I05, I06, I07, I08, I09, I10, I11, I12 |
| T9 | 3 | Fall | `LAYER_BACK_CALL` von K4 **zweifach** gemeldet | `LAYER_BACK_CALL` wird von K4 **zweifach** gemeldet (`layers` **und** `acyclic_siblings`) |
| T9 | 3 | Buchungsregel | vorregistrierte Doppelmeldung, **kein FP** | vorregistrierte Doppelmeldung, **nicht wegkonfigurierbar**, **kein FP** |
| T9 | 4 | Pfad | K2 | K2/K3 |
| T9 | 4 | Häufigkeit | **3/3 Läufe** | K2 3/3 Läufe · K3 0/3 Läufe |
| T9 | 5 | Pfad | K2 | K2/K3 |
| T9 | 5 | Häufigkeit | **1/3 Läufe** | K2 1/3 Läufe · K3 0/3 Läufe |
| T9 | 6 | Fall | `CYCLE`: K2 meldet `FORBIDDEN_RELATION` am **richtigen Modul** | `CYCLE`: K2/K3 melden `FORBIDDEN_RELATION` am **richtigen Modul** |
| T9 | 6 | Pfad | K2 | K2/K3 |
| T9 | 6 | Häufigkeit | 9 | K2 6 · K3 0 |
| T9 | 6 | Buchungsregel | **kein** Treffer, **kein** FP — „richtige Stelle, falsche Kategorie“ | **kein** Treffer für `CYCLE` (Zelle bleibt `nein`), **kein** FP; in `localized` als „richtige Stelle, falsche Kategorie“ · **daneben 3 Records** am selben Modul mit anderer Kategorie (K2/API_CONTRACT) — **nicht** Fall 6, sie fallen unter die Allgemeinregel **FP *und* FN** |
| T9 | 7 | Fall | `CYCLE_*`: K5 meldet die Rückkante als **nicht gelistete Kante** | `CYCLE_*`: K5 meldet die Rückkante als **nicht gelistete Kante**, nicht als Zyklus |
| T9 | 7 | Häufigkeit | *(leer)* | 4 |
| T9 | 7 | Buchungsregel | `strict` kein Treffer · `localized` Treffer auf der **Stelle** — **ohne neue Regel** gebucht | `strict`: kein Treffer (Kategoriesegment weicht ab) · `localized`: Treffer auf der **Stelle**, Klasse „richtige Stelle, falsche Kategorie“ — **ohne neue Regel** gebucht |

### 5.4 Die Massenfüllungen, als Gruppe

| Gruppe | Zellen | erster Lauf | zweiter Lauf | Grund |
|---|---:|---|---|---|
| T4 Symmetrieteil, `K1/K4/K5 Kampagne` und `Δ` | **192** | sämtlich **leer** | gerechnete Werte; bei K4 tragen `I13`–`I15` `n. b.` (der `acyclic_siblings`-Block trägt strukturell kein Modul, A-17) | **R5** |
| T5, alle sechs Kennzahlspalten | **165** | sämtlich **leer** | `TP/Nenner = Wert` bzw. `0/0` bei leerem Nenner | **R3** |
| T6, alle neun Spalten | **31** | sämtlich **leer** | Zählwerte, Zeiten, Tokens, Latenzen | **R4** |

**Die T4-Ruhezustandsseite für K1/K4/K5 hat sich nicht bewegt** — sie bleibt der
gekennzeichnete Berichtswert `0 ᴬ¹⁴` aus C3a, in beiden Läufen zeichengleich.

### 5.5 Die kein-EN-Bewegung gegen die Vorhersage der Revision

Rev. 40 hat **vor** dem Lauf sechs bewegte Zeilen angekündigt. Gemessen sind **genau diese
sechs**:

| Injektion | Konfig | erster Lauf | zweiter Lauf | in Rev. 40 angekündigt? |
|---|---|---|---|---|
| I10 | K2 | `nein` | **`ja`** | ja |
| I12 | K2 | `nein` | **`ja`** | ja |
| I06 | K3 | `ja` | **`nein`** | ja |
| I20 | K3 | `ja` | **`nein`** | ja |
| I21 | K3 | `ja` | **`nein`** | ja |
| I30 | K3 | `nein` | **`ja`** | ja |

Verteilung: K2 `ja` **20 → 22**, `nein` **5 → 3**; K3 `ja` **4 → 2**, `nein` **23 → 25** —
zeichengleich mit der Ankündigung. Die übrigen **12** kein-EN-Änderungen sind
Darstellung des dritten Zustands: **8** Zellen (I13–I16 × K2/K3) tragen jetzt den aus
`strict` übernommenen Marker ` — `, **4** den gerechneten Wert `entfällt`. Damit ist die
Zahl der leeren kein-EN-Zellen von **12 auf 0** gefallen.

---

## 6 Strukturprüfung

### 6.1 Zellen je Marker

| | erster Lauf | zweiter Lauf |
|---|---:|---:|
| ` — ` (code-gesetzt) | 143 | 79 |
| `n. b.` (code-gesetzt) | 28 | 34 |
| `n. e.` | 0 | 0 |
| **leer** | **412** | **6** |
| Wert | 1 341 | 1 789 |
| Marker **ohne** Code-Auszeichnung | 2 (T3) | **74** (2 T3 + 72 T5) |

**Die 6 verbliebenen leeren Zellen sind sämtlich die Spalte `Abweichung` in T1** — in den
sechs Zeilen ohne Abweichung. Das ist die einzige, an der Spalte vermerkte und in der
Ausnahmeliste von R1 namentlich geführte Bedeutung von „leer" in dieser Ausgabe:
**berechnet, keine Abweichung**. Zeilen: `LAYER_BACK_CALL`, `LAYER_SKIP_CALL`,
`PROTECTED_MODULE`, `INDEPENDENCE`, `MISSING_PORT_REFERENCE`, `SIGNATURE_DEVIATION`.

**Der Anstieg von `n. b.` um 6** ist der T4-Symmetrieteil: K4 trägt bei `I13`, `I14`, `I15`
je `n. b.` in `Kampagne` **und** `Δ` — die Zählgrösse ist dort nicht bildbar.

### 6.2 `n. e.`-Liste

**Leer, in allen fünf Konfigurationen** — wie im ersten Lauf. T7.3 führt für K1, K2, K3, K4
und K5 je *(keine)*, Anzahl 0. Keine Injektion ohne gültigen Lauf.

### 6.3 Gegenprobe Journal und Prosa-Manifeste gegen die Laufmanifeste

**Deckungsgleich in allen fünf Konfigurationen**, für die Zahl der gültigen Injektionen und
für die `n. e.`-Liste. Kein `ABWEICHUNG`-Eintrag, kein Banner im Kopf, keine
`HARNESS-BEFUND`-Zeile auf `stderr`.

### 6.4 T1 — die gerechneten Abweichungen

Vier Zeilen tragen einen Eintrag, sechs sind leer (= keine Abweichung):

| Szenario | Eintrag | Art |
|---|---|---|
| `CYCLE_SIBLING` | K4 `n. b.` (kein Vergleich bildbar) | **kein Vergleich**, nicht Abweichung — `localized` ist für K4/`CYCLE` nicht bildbar |
| `CYCLE_PARENT_CHILD` | K4 `n. b.` (kein Vergleich bildbar) | ebenso |
| `FRAMEWORK_TYPE_IN_SIGNATURE` | **K3: Soll ja / Ist teilweise** | **Abweichung** — Ist K3 = 3/4 |
| `INCORRECT_LOCATION` | **K2: Soll ja / Ist teilweise** | **Abweichung** — Ist K2 = 3/4 |

**Die drei vorregistrierten `teilweise`-Zellen reproduzieren sich ohne Abweichung**:
K5/`CYCLE_SIBLING`, K5/`CYCLE_PARENT_CHILD` und K4/`INCORRECT_LOCATION`. Sie sind die drei
Zellen, deren Zellregel `strict: "nie"` lautet — der Treffer liegt auf der **Stelle**, nie
auf der Kategorie —, und genau das ist die Aussage `teilweise`. **Abweichungen werden
ausgewiesen, nicht aufgelöst**: keine Soll-Zelle ist angetastet.

### 6.5 Laufzeit und Umfang

0,27 s wall, 27 144 KB maxrss, 658 gelesene Dateien, Exit 0.

---

## 7 Befunde des zweiten Laufs — Darstellung, nicht Werte

**Zwei Darstellungsabweichungen, nach dem Lauf festgestellt und NICHT behoben**: ein dritter
Lauf ist ohne ausdrückliche Freigabe ausgeschlossen, und ein Renderer-Fix ohne Lauf machte
den registrierten Instrumentenhash und die archivierte Ausgabe unvereinbar.

**(1) T5 setzt die Marker ohne Code-Auszeichnung — 72 Zellen.** Die Ausgabe schreibt in T5
` — ` und `n. e.` als blossen Text, während T1, T2 und T4 dieselben Marker als `` ` — ` ``
und `` `n. e.` `` setzen:

```
c11_eval_full.md : | K1 | `ABSENCE_REQUIRED` | 4 | ` — ` | ` — ` | …
c12_eval_full.md : | K1 | `ABSENCE_REQUIRED` | 4 |  —  |  —  | …
```

**Kein Wert und keine Markerbedeutung ist betroffen** — es ist dieselbe Zeichenfolge in
anderer Auszeichnung, und die Zusicherung R1 greift korrekt (die Zelle ist nicht leer). Es
ist eine **Uneinheitlichkeit innerhalb eines Dokuments**: `Score.cells()` gibt den rohen
Markerstring zurück statt `Cell.text`. Betroffen sind ausschliesslich T5-Zellen.

**(2) T6 druckt zwei Summen in Exponentialschreibweise.** Die Wanduhrsumme und der
Innenwert von K3 erscheinen als `9.19054e+06 ms` bzw. `9.13543e+06 ms` — Folge des
`%g`-Formats für grosse Zahlen. Lesbar, aber uneinheitlich zu den übrigen
Millisekundenangaben derselben Zeile.

**Beide gehören in einen Folgeauftrag zusammen mit einem dritten Lauf**, falls freigegeben.
Sie sind hier ausgewiesen und nicht stillschweigend gelassen.

---

## 8 Was dieser Auftrag nicht getan hat

Kein dritter Auswertungslauf. Kein Befund 08, kein C10-Abschlussbericht, keine
Kapitelprosa, kein Standdokument, keine offenen Punkte, kein Arbeitsplan, keine Gate-Notiz,
kein Z1, kein L1, kein A-38, keine Wurzel-README. Keine Änderung an `data/campaign/k*`, an
`data/soll/`, am Injektionsmanifest, an einer Regeldatei, am Prompt oder am Schema. **Kein
`git push`.**

**Eine Lücke ist benannt und nicht gefüllt:** Skelett T5 (ii) verlangt für K2/K3 zusätzlich
**Median und Spannweite über drei Läufe**. Eine laufweise Precision/Recall verlangt eine
laufweise `strict`-Grösse; `strict` ist nach Spezifikation §3 ein **Existenzquantor über die
Läufe**, und eine zweite, laufweise Fassung wäre eine **neue Metrikdefinition** — gesperrt
nach Protokoll §0.1 Punkt 2 und ausserhalb dieses Auftrags. Der Vermerk steht in der
Ausgabe an T5 selbst.
