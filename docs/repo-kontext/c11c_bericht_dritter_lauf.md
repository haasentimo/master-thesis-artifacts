# C11c — Darstellungsmängel geschlossen, Bündel entlastet, dritter Lauf

**Masterarbeit Timo Haas · HTWG Konstanz**
Datum: 28. August 2026 · Auftrag **C11c** · Schreibendes Repo: `masterarbeit`;
`tritongraph`, `tritongraph-measure` und `ma-conformance-testrepo` **nur lesend**

**Commits dieses Auftrags:**

| # | SHA | Titel |
|---|---|---|
| 1 | `db6552d` | `docs: label the computed denominators in the T5 aggregate rows` |
| 2 | `6572f2b` | `docs: amend the protocol to rev 42 and resolve the T5 (ii) requirement` |
| 3 | `06d9d53` | `fix: render markers and large numbers consistently` |
| 4 | `b979f14` | `docs: refreeze the evaluation instruments as rev 43` |
| 5 | `dd9e896` | `data: archive the third evaluation run after the rendering fixes` |
| 6 | `55bd8a5` | `chore: bundle the current evaluation output and drop superseded reports` |
| 7 | *(dieser Bericht)* | `docs: report the rendering fixes, the third run and the bundle change` |

> **Deutungssperre, wie in C11b.** Dieser Bericht **bewertet kein Ergebnis**, vergleicht
> **keine Konfigurationen** und empfiehlt **nichts** zu Prompt, Schema, Regeldatei, Manifest
> oder Metrik. Er berichtet, was aufgesetzt wurde, was dabei herauskam und was daraus folgt.

> **Was dieser Auftrag NICHT getan hat.** Kein vierter Auswertungslauf. Kein Befund 08, kein
> C10-Abschlussbericht, keine Kapitelprosa, keine Rechenregel, kein Standdokument, keine
> offenen Punkte, kein Arbeitsplan, keine Gate-Notiz, kein Z1, kein L1, kein A-38, keine
> Wurzel-README. Keine Änderung an `data/campaign/k*`, an `data/soll/`, am
> Injektionsmanifest, am Prompt oder am Schema. **Kein `git push`.** Keine Datei gelöscht,
> kein git-Verlauf berührt.

---

## 0 Vorbedingungen

| Prüfung | Erwartet | Befund |
|---|---|---|
| `masterarbeit` porcelain | leer | leer, HEAD `165a925` ✅ |
| `tritongraph` porcelain | leer | leer (`348ca9d`) ✅ |
| `tritongraph-measure` porcelain | leer | leer (`348ca9d`) ✅ |
| `ma-conformance-testrepo` porcelain | leer | leer (`0d65104`) ✅ |
| Runner aktiv? | nein | Prozessliste ohne Treffer ✅ |
| `tools/check_doc_invariants.py` | Exit 0 | **alle 5 Invarianten erfüllt**, Exit 0 ✅ |
| `sha256sum -c` in `data/campaign/eval/` | 4 / 4 OK | **4 von 4 OK** ✅ |

**Beide bestehenden Läufe sind unberührt geblieben.** `c11_eval_full.*` und
`c12_eval_full.*` sind über den ganzen Auftrag hinweg weder geöffnet-schreibend noch
überschrieben noch gelöscht worden; ihre `SHA256SUMS`-Zeilen stehen am Ende zeichengleich
wie am Anfang.

---

## 1 Phase 1 — der Aufschrieb: Zeilenbeschriftung der T5-Gesamtzeilen

### 1.1 Setup

Die beiden Gesamtzeilen von T5 trugen die Beschriftung „**Nenner 32 (alle Kategorien)**"
bzw. „**Nenner 16 / 28 / 28 / 19 / 20**". Die Zellen daneben rechnen aber mit dem
**gerechneten** Nenner, der nach Auflage (2) bei `n. b.`, `n. e.` und den vorregistrierten
Sonderklassen **sinkt** — in der **UF3**-Zeile von **K4 und K5 auf 28**, ablesbar im zweiten
Lauf als `16/28 = 0,571` in einer Zeile, deren Beschriftung „Nenner 32" sagte.

Die Leseregel stand **bereits richtig** unter der gedruckten Tabelle („Wie die Zellen zu
lesen sind": *„Der Nenner ist der gerechnete, ausgewiesene Nenner"*). Die Beschriftung
**widersprach** ihr.

### 1.2 Resultat

Neue Fassung, in allen zehn Gesamtzeilen:

```
| K4 | **Gesamt — UF3, Abdeckung des Kategoriespektrums,**
       ~~Nenner 32 (alle Kategorien)~~
       **vorregistrierter Nenner 32, gerechneter Nenner je Zelle ausgewiesen** | 32 | …
```

**Als AUFSCHRIEB nach Skelett §0.3 (B) korrigiert, nicht als Vorhersage.** Die **32** ist die
Zahl der Injektionen des Injektionsplans (Protokoll §3), die Zahlen 16 · 28 · 28 · 19 · 20
folgen aus **T8**; beide stehen **vor jeder Messung** fest und sind ohne Blick in die
Kampagnendaten belegbar — die Prüfregel des §0.3 ist damit erfüllt. Der Fehler lag **nicht
im Nenner**, sondern darin, dass die Beschriftung ihn als den **gerechneten** ausgab. Alttext
**durchgestrichen sichtbar**, mit Datum und Auftragsverweis; dazu ein Korrekturabsatz unter
T5 und der Zeiger in der §0.3-Zuordnungstabelle, nach dem Muster der T7.2-Korrektur aus
C6c-b.

### 1.3 Maschineller Nachweis, dass sonst nichts berührt ist

Zellenweiser Vergleich des Skeletts vor und nach der Änderung — jede Markdown-Tabellenzelle
jeder Tabelle, adressiert über (Tabelle, Zeilenindex, Spaltenindex):

| | |
|---|---|
| Tabellenzellen vorher | **2 068** |
| Tabellenzellen nachher | **2 068** |
| Zellen nur vorher / nur nachher | **0 / 0** |
| **GEÄNDERT** | **12** |
| davon Beschriftungsspalte T5 (Spaltenindex 1) | **10** |
| davon §0.3-Zuordnungstabelle, Zeile T5 | **2** |
| geänderte Zellen in **T1** | **0** |
| geänderte Zellen in **T8** | **0** |
| geänderte Zellen in irgendeiner anderen Spalte von T5 | **0** |

Zusätzlich blockweise geprüft: der **T1**-Abschnitt (44 Zeilen) und der **T8**-Abschnitt
(65 Zeilen) sind **zeichengleich**. Die `git diff`-Hunks liegen sämtlich ausserhalb beider
Bereiche (alte Zeilen 107, 658–659, 666–667, 674–675, 682–683, 690–691 und eine reine
Einfügung bei 715). Die Zeilenzahl der Datei steigt von **1 015** auf **1 038** — die
23 Zeilen sind **ausschliesslich** der Korrekturabsatz, keine Tabellenzeile.

### 1.4 Konsequenz

Die Beschriftung sagt jetzt, **welchen** Nenner sie nennt. Der Widerspruch zur Leseregel ist
weg; die Rechnung ist unverändert. **Kein Befund, keine Abweichungszeile** — der Aufschrieb
war falsch, nicht das Werkzeug.

---

## 2 Phase 2 — T5 (ii) erledigt, Protokollrevision 42

### 2.1 Setup

Skelett T5 (ii) und Auswertungsspezifikation §7.5 Punkt 1 verlangten für K2/K3 zusätzlich
**Median und Spannweite über drei Läufe**. C11b hat das als **offene, nicht gefüllte Lücke**
geführt (`c11b_bericht_zweiter_lauf.md` §8), und die Ausgabe trägt den Vermerk an T5 selbst.

### 2.2 Resultat — die Anforderung entfällt gegenstandslos, sie wird nicht abgewiesen

Median und Spannweite setzen eine **laufweise** Grösse voraus, über die gestreut werden
kann. Precision, Recall und F1 dieser Tabelle stehen auf `strict` und `localized`; **`strict`
ist nach Spezifikation §3 ein Existenzquantor über die Repetitionen** und ist über die drei
Läufe hinweg **definiert** — es hat **konstruktiv keine Verteilung über Läufe**.

Eine laufweise Fassung wäre **keine zweite Auslesart derselben Metrik**, sondern eine **neue
Metrikdefinition**, und Metrikdefinitionen sind seit dem ersten Kampagnenlauf **gesperrt**
(Protokoll §0.1 Punkt 2). Die Anforderung zu „erfüllen" hiesse also, die Sperre zu brechen;
sie stehen zu lassen hiesse, eine konstruktiv unerfüllbare Forderung als offene Lücke zu
führen. **Beides ist falsch, und beides ist hier vermieden.**

**Die Laufstreuung ist ausgewiesen, und zwar feiner:** die mit **Rev. 40** eingeführte
T4-Spalte **Läufe (Ruhe · Kampagne)** trägt die Zählgrösse für **jede der drei Repetitionen
einzeln** (`[0,0,1]`, Spezifikation §7.5 (5)) — nicht zu einem Median zusammengezogen.

**Nicht berührt: §7.5 Punkt 2.** Die Falsch-Positiv-Raten-Tabelle führt Median **und**
Spannweite über drei Läufe für K2/K3 **unverändert** weiter; dort ist die Headline-Rate eine
**je Lauf** gebildete Grösse (§7.1). T3 druckt sie wie bisher.

### 2.3 Als Protokollrevision 42 geführt

| Stelle | Eintrag |
|---|---|
| Kopf | Rev. 41 → **Rev. 42**, Alttext gestrichen sichtbar; Freeze-Aussage unverändert Rev. 33 |
| Revisionshistorie | Eintrag **Rev. 42**, hinter Rev. 41 |
| §10 Amendments nach Messbeginn | **Zeile 42**, Spalte Re-Run: **nein** |
| Spezifikations-SHA §1 (Nachtrag Rev. 30) | ~~`be3491e2…acb21d6e1`~~ → **`fe991be6…092c20d1`** |
| Spezifikations-SHA §0.1 (Messstand) | ~~`be3491e2…acb21d6e1`~~ → **`fe991be6…092c20d1`** |
| `c5b_bericht_protokoll_freeze.md` §3 | Zeile Rev. 41 gestrichen, **Rev. 42** = `6988a93b…f5714e2b` |

Nachzug **im selben Commit** wie die Spezifikationsänderung. **Prüfer Exit 0**, alle fünf
Invarianten grün.

**Kein Re-Run folgt aus Rev. 42** — keine Zelle rechnet anders. Der dritte Lauf ist von der
**Darstellungsreparatur** ausgelöst, nicht von diesem Amendment.

### 2.4 Ausdrücklich vermerkt: Phase 1 berührt keinen gehashten Wert

Die Zeilenbeschriftung steht im **Tabellenskelett**. Das ist **kein gehashtes Dokument**: es
steht **weder** in Protokoll §0.1 **noch** in `data/soll/SHA256SUMS` **noch** unter
`data/campaign`, und es ist **keines** der drei Auswertungsinstrumente. Die Korrektur bewegt
deshalb **weder** den Protokoll-SHA **noch** den Spezifikations-SHA **noch** einen
Instrumentenhash **noch** eine `SHA256SUMS`-Zeile. Der Vermerk steht auch im
Protokoll-Historieneintrag Rev. 42 (b) und in der §10-Zeile 42, damit die Bewegungsprüfung
nicht nach einem Nachzug sucht, den es nicht gibt.

---

## 3 Phase 3 — Renderer, ohne jede Wertänderung

### 3.1 Setup — die drei Punkte

**D1 · T5 druckte seine Marker ohne Code-Auszeichnung (72 Zellen im zweiten Lauf).**
`Score.cells()` gab den **rohen Markerstring** zurück, während jede andere Tabelle über
`Cell.text` lief:

```
c12: | K1 | `ABSENCE_REQUIRED` | 4 |  —  |  —  | …
c13: | K1 | `ABSENCE_REQUIRED` | 4 | ` — ` | ` — ` | …
```

Ein Marker ohne Auszeichnung ist **von Prosa nicht zu unterscheiden**, und die drei Marker
tragen drei verschiedene Aussagen, die Kapitel 8 verschieden liest (Skelett §1.1).

**D2 · T6 druckte zwei K3-Summen in Exponentialschreibweise** — `9.19054e+06 ms` (Wanduhr
aussen, Summe) und `9.13543e+06 ms` (Wanduhr innen), der `%g`-Rückfall oberhalb von sechs
signifikanten Stellen.

**D3 · Nachschau über ALLE Tabellen nach beiden Klassen.** Ergebnis unten in §3.2.

### 3.2 Resultat — D3, die vollständige Liste

Die Nachschau lief maschinell über **jede Datenzelle jeder Tabelle** der Ausgabe des zweiten
Laufs. Eine Zelle gilt als Markerzelle, wenn ihr **gesamter** Inhalt — nach Abzug von
Fettung und Fussnotenzeichen — einer der drei Marker ist; ein Gedankenstrich **innerhalb
eines Satzes** ist Interpunktion.

| Klasse | Tabelle | Spalte | Zellen | Befund |
|---|---|---|---|---|
| Marker ohne Auszeichnung | **T5** | `strict` P/R/F1, `loc` P/R/F1 | **72** | die bereits in C11b §7 (1) ausgewiesenen |
| Marker ohne Auszeichnung | **T3** | `Headline` (findingweise Zeilen K2 und K3) | **2** | **NEU gefunden** — blosser Gedankenstrich |
| Zahl in Exponentialform | **T6** | Wanduhr aussen Summe, Wanduhr innen | **2** | die bereits in C11b §7 (2) ausgewiesenen |
| **Summe behoben** | | | **76** | |

**Geprüft und ausdrücklich NICHT angetastet** — Treffer der rohen Textsuche, die **keine**
Markerzellen sind:

| Stelle | Inhalt | Warum kein Marker |
|---|---|---|
| **T5**, Spalte `Kategorie (Ebene 1)`, 10 Zellen | „Gesamt **—** UF3, Abdeckung des …" | Gedankenstrich in der **Zeilenbeschriftung** |
| **T9**, Spalte `Buchungsregel`, 2 Zellen | „… `localized`: Treffer auf der **Stelle** **—** ohne neue Regel gebucht" | Gedankenstrich im **Fliesstext** |
| **T3.2**, Spalte `fällt auseinander?`, 2 Zellen | „nein **—** beide Lesarten gleich" | Gedankenstrich im **Fliesstext** |

**Die zwei T3-Zellen im Klartext.** Das Skelett lässt die `Headline`-Zelle der findingweisen
Zeile **leer**; der Renderer füllte sie mit einem blossen Gedankenstrich. Ergänzt ist
**allein die Auszeichnung** — die Zelle sagt, was sie vorher sagte. Es ist **keine** Bedeutung
zugewiesen und **kein** Marker neu vergeben worden.

### 3.3 Wie repariert wurde

- **`marker_text()`** ist jetzt die **einzige** Stelle, die einen Marker rendert; `Cell.text`
  und `Score.cells()` gehen beide darüber. Ein zweiter Renderpfad kann nicht mehr auseinander
  laufen.
- **`plain()`** rendert eine Zahl **ohne Exponent**. Nur die **Notation** ändert sich: ein
  `int` rendert exakt, ein `float` behält seine `%g`-Darstellung und fällt nur dort auf eine
  gewöhnliche Dezimalform zurück, wo `%g` einen Exponenten geschrieben hätte. **Alle** übrigen
  `%g`-Aufrufstellen laufen seither darüber (T3-Mediane und -Spannweiten, T4 Ruhe/Kampagne/Δ,
  die Headline-Rate, `median_span_text`).

**AUSDRÜCKLICH: keine Rechenregel, kein Filter, kein Nenner, keine Aggregationsstufe ist
berührt.** `strict`, `localized`, Precision, Recall, F1, Median, Spannweite, die
Falsch-Positiv-Rate und die vier Marker stehen unverändert.

### 3.4 Neue Zusicherung R10

Geprüft am **fertig gerenderten** Text, wie R1 — nicht am Zellobjekt, weil der zweite Lauf
gerade gezeigt hat, dass ein Renderpfad Werte **auf dem Weg in die Tabelle** verändert, ohne
je ein `Cell` anzufassen:

> **R10 — kein gerenderter Marker ohne Code-Auszeichnung, keine Zahl in Exponentialform.**
> Exit 2.

Sie läuft bei **jedem** Lauf, auch ohne `--with-campaign`: Marker und Zahlen rendern in
beiden Betriebsarten gleich. Die Nummer **R10** ist gewählt, weil **R3–R9** in C11a/C11b als
**Reparaturnummern** vergeben sind; die bestehenden Zusicherungen sind R1 (Leerzelle) und
R2 (gerechnete Null).

### 3.5 Verifikation vor dem Lauf

**(a) Alle Fixtures erneut**

| Prüfung | Erwartet | Gemessen | |
|---|---|---|---|
| `match_k4k5.py --selftest` | 34 von 34 | **34 von 34, 0 Abweichungen** | ✅ |
| Selbsttest B — K2 modulweise je Lauf | 49 / 49 / 49 | 49 / 49 / 49 | ✅ |
| Selbsttest B — K2 Headline | **49/52** | **49/52**, Median 49, Spannweite 49–49 | ✅ |
| Selbsttest B — K2 findingweise | **461** (155/153/153) | 155 / 153 / 153, Summe **461** | ✅ |
| Selbsttest B — K3 modulweise je Lauf | 2 / 1 / 0 | 2 / 1 / 0 | ✅ |
| Selbsttest B — K3 Headline | **1/52** | **1/52**, Median 1, Spannweite 0–2 | ✅ |
| Selbsttest B — K3 findingweise | **3** (2/1/0) | 2 / 1 / 0, Summe **3** | ✅ |
| Harness gegen `tests/fixtures/harness/mini` | nur Darstellung bewegt | **60** geänderte Zellen: **50** reine Auszeichnung, **10** Zeilenbeschriftung — **0 unerklärt** | ✅ |
| Fixture-Lauf mit `--with-campaign` | Exit 0 | **Exit 0**, kein `stderr` | ✅ |

**(b) Alle Zusicherungen negativ probiert**

| # | Zusicherung | Provokation | Ergebnis |
|---|---|---|---|
| P1 | `Cell.__post_init__` — Marker **und** Wert | `Cell(value=0, marker=" — ")` | `MarkerViolation: Zelle trägt Marker ' — ' UND Wert 0 …` |
| P2 | `Cell.__post_init__` — unbekannter Marker | `Cell(marker="n. x.")` | `MarkerViolation: unbekannter Marker 'n. x.'` |
| P3 | **R2** — gerechnete Grösse rendert leer | `num("")` · Gegenprobe `num(0)` | `MarkerViolation: … (R2)` · `num(0) = '0'` |
| P4 | `assert_marker_discipline` | ` — `-Zelle mit Wert 0 vorbeigeschmuggelt | zwei Meldungen: `Marker ' — ' und Wert 0` · `' — ' als 0 gebucht` |
| P5/P6 | **R1** Ende-zu-Ende | `kein_en_cell` liefert `""` | `LEERZELLE: T4 Zeile 245 (I04), Spalte 'K3 kein-EN'` … 4 Meldungen + Sammelzeile, **Exit 2** |
| P7 | `n. e.` ohne T7-Beleg | ein Laufmanifest aus der Fixture-Kopie entfernt | `HARNESS-FEHLER: I04/K1 trägt n. e. ohne T7-Beleg`, **Exit 2** |
| P8 | Blindheit | Kampagnen-Laufartefakt geöffnet, Lauf **ohne** `--with-campaign` | `BLINDHEITSVERLETZUNG: …/campaign/k2/…json`, **Exit 3** |
| P9 | Blindheit deckt `control/` | `campaign/control/k1/…json` geöffnet | `BLINDHEITSVERLETZUNG: …`, **Exit 3** |
| P10 | T7-Gegenprobe weicht ab | Journalzeile K3 auf `VALID` gesetzt | 2 × `HARNESS-BEFUND` auf `stderr`, **Exit 0** (Befund, kein Defekt) |
| P11 | UF4-Nenner gegen T8 | `UF4_DENOMINATOR["K4"]` auf 18 gesetzt | `HARNESS-FEHLER: UF4-Nenner K4: 19 … gegen vorregistrierte 18 (T8)`, **Exit 2** |
| P12 | Invariante (E) | Kommentarzeile an `match_k4k5.py` angehängt | `FEHL tools/match_k4k5.py`, IST gegen SOLL, **Exit 1** |
| **P13** | **R10 (a)** Einheit | `table_render_defects` mit `—` und `n. b.` roh | `T5 … Marker '—' ohne Code-Auszeichnung`, `… 'n. b.' …` |
| **P13b** | **R10 (a)** Gegenprobe | Gedankenstrich **im Satz** | **keine Meldung** — Interpunktion wird nicht gemeldet |
| **P14** | **R10 (b)** Einheit | `9.19054e+06 ms` in einer Zelle | `Zeile 5: Zahl in Exponentialform '9.19054e+06'` |
| **P15** | **R10 (a)** Ende-zu-Ende | `Score.cells()` auf den rohen Markerstring zurückgesetzt | **48** Meldungen + Sammelzeile, **Exit 2** |
| **P16** | **R10 (b)** Ende-zu-Ende | `plain()` auf blosses `%g` zurückgesetzt | 2 Meldungen (`9.19054e+06`, `9.13543e+06`), **Exit 2** |

Nach jeder Probe wiederhergestellt; der Baum war danach porcelain leer.

### 3.6 Instrumenten-Hashes neu gebildet — Protokollrevision 43

Commit **`b979f14`**. **Eine eigene Revision, obwohl reiner Bytestandsnachzug** — §0.1
Punkt 5. Unter **Rev. 42** vollzogen, stünde der in `c5b_bericht_protokoll_freeze.md` §3
bezeugte Bytestand von Rev. 42 **in keinem Dokument mehr**: der Ausfall aus C6b-2b, aus dem
Rev. 36 diese Regel gemacht hat, und dieselbe Trennung wie zwischen Rev. 40 und Rev. 41.

| Datei | Rev. 41 | Rev. 43 |
|---|---|---|
| `tools/evaluate_campaign.py` | `20bcdae0…23d306` | **`eb206a6f…b520653`** |
| `tools/match_k4k5.py` | `c16e7c43…799f4ca6` | **unverändert** |
| `tools/check_doc_invariants.py` | `6cc16ef9…1e52b7018` | **unverändert** |

Protokoll-SHA nach Rev. 43: **`759b11ed…369343f4`**, in `c5b` §3 bezeugt.

```
$ python3 tools/check_doc_invariants.py
[OK ] (A) … [OK ] (B) … [OK ] (C) … [OK ] (D) … [OK ] (E)
ERGEBNIS: alle 5 Invarianten erfüllt                       → Exit 0
```

**Invariante (E) grün gegen den neuen Hash. Gatter passiert.**

### 3.7 Ungeschminkt: (E) war zwischen Commit 3 und Commit 4 rot

Zwischen der Renderer-Reparatur (`06d9d53`) und ihrem Hash-Nachzug (`b979f14`) meldete der
Prüfer **(E) FEHL** für `tools/evaluate_campaign.py`, IST gegen SOLL. **Das ist die
vorgesehene Reihenfolge, kein Versehen:** ein Nachzug im selben Commit machte die Reparatur
und ihre Registrierung ununterscheidbar, ein Nachzug unter Rev. 42 machte deren Bytestand
unbezeugt. Dieselbe Lage bestand in C11b zwischen Reparatur und Rev. 41.

**Nach den Commits 1, 2, 4, 5 und 6 stand der Prüfer auf Exit 0.** Die Zeilenbeschriftung
aus Phase 1 ist deshalb **nicht** mit Commit 1 in den Renderer gegangen, sondern erst mit
Commit 3 — so wird der Instrumentenhash **genau einmal** neu gebildet, und Phase 2 konnte,
wie verlangt, gegen einen grünen Prüfer abschliessen.

---

## 4 Phase 4 — der dritte Lauf

**Ein Lauf**, vollständiger Bestand, unverändert gegenüber dem ersten und zweiten (alle sechs
Block-`SHA256SUMS` zeichengleich).

```
$ python3 tools/evaluate_campaign.py --with-campaign \
    --json-out data/campaign/eval/c13_eval_full.json \
    --markdown-out data/campaign/eval/c13_eval_full.md
                                                           → Exit 0
```

| | |
|---|---|
| **Zeitstempel** | 2026-08-28T16:17:24+02:00 bis 2026-08-28T16:17:24+02:00 |
| **Laufzeit** | 0:00.28 wall, 27 152 KB maxrss |
| **git HEAD** | `b979f14` (Rev.-43-Stand) |
| **Protokoll** | Rev. 43, `759b11ed…369343f4` |
| **Spezifikation** | `fe991be6…092c20d1` |
| **Instrumente** | `eb206a6f…` / `c16e7c43…` / `6cc16ef9…` |
| **gelesene Dateien** | **658**, davon **253** Kampagnen-Laufartefakte — **wie im zweiten Lauf** |
| **`stderr`** | leer — keine Markerverletzung, kein Harness-Fehler, kein Harness-Befund |
| **Ausgabe** | `c13_eval_full.json` / `.md`, Kopf mit Instrumenten-, Protokoll-, Spezifikations- und Blockhashes, Zeitstempel und Aufrufzeile vorangestellt |

**Sofort archiviert und committet**, vor jeder weiteren Arbeit: Commit **`dd9e896`**,
`SHA256SUMS` ergänzt, `sha256sum -c` **6 von 6 OK**, Prüfer Exit 0.

**C11 und C12 liegen unberührt daneben** — nicht überschrieben, nicht gelöscht, nicht
nachbearbeitet (Protokoll §0.1 Punkt 6: Ausweis der Ergebnisse nebeneinander).

---

## 5 Gegenüberstellung c12 gegen c13 — das eigentliche Kriterium

### 5.1 Bilanz, Zelle für Zelle

Verglichen wird der **Rendering-Teil** beider Ausgaben (der Kopf unterscheidet sich
konstruktionsgemäss und ist in §4 geführt), jede Datenzelle adressiert über (Tabelle,
Zeilenindex, Spaltenindex):

| | |
|---|---|
| Datenzellen c12 | **2 345** |
| Datenzellen c13 | **2 345** |
| Zellen nur in c12 / nur in c13 | **0 / 0** |
| vergleichbare Zellen | **2 345** |
| davon **UNVERÄNDERT** | **2 259** |
| davon **GEÄNDERT** | **86** |

### 5.2 Jede geänderte Zelle, klassifiziert

| Klasse | Zellen | Tabellen |
|---|---:|---|
| nur **Auszeichnung** (Backticks um einen Marker) | **74** | T5 (72), T3 (2) |
| nur **Zahlenformat** (Exponent → ganzzahlig) | **2** | T6 |
| **Zeilenbeschriftung** aus Phase 1 | **10** | T5 |
| **WERTÄNDERUNG** | **0** | — |
| **Summe** | **86** | |

**KEINE WERTÄNDERUNG. Der Abbruchgrund ist nicht eingetreten.**

### 5.3 Zeichengleichheit nach Normalisierung

Normalisiert wird beidseitig: **Backticks entfernt**, **Ganzzahlen ab sieben Stellen in die
`%g`-Form zurückgeführt**, Leerraum vereinheitlicht.

```
Zeilen c12 / c13                              : 584 / 584
abweichende Zeilen nach Normalisierung        :  10
  davon Zeilenbeschriftungen aus Phase 1      :  10
  UNERKLÄRT                                   :   0
```

**c13 ist nach Normalisierung zu c12 zeichengleich, ausser in den zehn in Phase 1
geänderten Zeilenbeschriftungen und im Kopf.** Genau die vorab benannte Erwartung.

### 5.4 Die stärkste Probe: der JSON-Rumpf ist identisch

```
JSON-Rumpf (ohne den Kopfschlüssel c12_run_head / c13_run_head) zeichengleich: True
```

**Jeder gerechnete Wert beider Läufe ist bitgleich.** Die Darstellungsänderungen leben
ausschliesslich im Markdown-Rendering; die Zeilenbeschriftung aus Phase 1 ebenfalls (sie ist
eine Beschriftung, kein Wert).

### 5.5 Die zwei Zahlenformat-Zellen im Einzelnen

| Zelle | c12 | c13 | JSON-Rohwert c12 | JSON-Rohwert c13 |
|---|---|---|---|---|
| T6 / K3 / Wanduhr aussen, Summe | `9.19054e+06 ms` | `9190542 ms` | **9190542** | **9190542** |
| T6 / K3 / Wanduhr innen | `9.13543e+06 ms` | `9135427 ms` | **9135427** | **9135427** |

**Setup → Resultat → Konsequenz.** Die alte Notation war eine auf sechs signifikante Stellen
**gerundete Ausgabe** desselben Wertes; die letzten beiden Stellen (`…42`, `…27`) waren in
der gedruckten Tabelle nicht sichtbar, im JSON aber die ganze Zeit vorhanden. Der **Wert hat
sich nicht bewegt** — sichtbar geworden ist er.

### 5.6 Strukturprüfung des dritten Laufs

| | |
|---|---|
| Markerzellen gesamt | **192** — ` — ` **153**, `n. b.` **39**, `n. e.` **0** |
| markerfreie Leerzellen (R1) | **0** |
| Marker ohne Auszeichnung (R10 a) | **0** |
| Zahlen in Exponentialform (R10 b) | **0** |
| Zeilen / Bytes der Markdown-Ausgabe | 639 / 51 073 (c12: 637 / 50 203) |

---

## 6 Bündel entlastet

### 6.1 B1 — die aktuelle Auswertungsausgabe kommt hinein

`data/campaign/eval/c13_eval_full.md` steht jetzt in der Dateiliste von
`tools/bundle-docs.sh`. Sie liegt **ausserhalb von `docs/`** und wurde deshalb weder von der
Prioritätsliste noch vom Auffang-Durchlauf erfasst.

**Nur die jeweils aktuelle Fassung.** `c11` und `c12` bleiben in git und in
`data/campaign/eval/`, archiviert und gehasht, aber **ausserhalb des Bündels** — zwei
Fassungen derselben Tabellen im Projektwissen sind nicht auseinanderzuhalten; derselbe Grund,
aus dem `docs/historisch/` ausgeschlossen ist.

Im Skript als Kommentar festgehalten: **bei jedem neuen Auswertungslauf ist der Pfad
nachzuziehen.** Still fällt er nicht aus — die `add`-Funktion meldet eine fehlende Datei auf
`stderr`.

### 6.2 B2 — überholte Berichte: KEINE Datei wird herausgenommen

Das Kriterium ist mechanisch auf **alle 70** Berichte in `docs/repo-kontext/` angewandt
worden. **Keine Datei erfüllt beide Hälften.**

**Kriterium (ii), maschinell:** `grep -rl` über `docs/` nach dem Dateinamen, ohne die Datei
selbst und ohne `docs/historisch/`. **67 von 70** Berichte werden von **mindestens einem**
aktuellen Dokument genannt — damit scheitert (ii), und nach der Regel „trifft nur eines von
beiden zu: **drin lassen**" bleiben sie im Bündel.

**Die drei Kandidaten mit null Zitaten, je mit Nachweis:**

| Datei | (ii) Zitate | (i) Inhalt in Protokollrevision oder Spezifikation? | Entscheid |
|---|---|---|---|
| `c6b1_bericht_nachtraege.md` | **0** — auch das Kürzel **„C6b-1" kommt in `docs/` nirgends vor** | **NEIN.** Die drei Nachträge gingen ins **Skelett** (A-14/T4, T5-Beschriftung) und in ein **Kampagnenmanifest** — nicht in eine Protokollrevision und nicht in die Spezifikation | **DRIN LASSEN** |
| `c6cb_bericht_vorkorrekturen.md` | **0** nach Dateiname, **aber** das Skelett schreibt zweimal „Auftrag **C6c-b**" an eine Korrektur (§0.3 und T7.2) | **NEIN.** Die beiden Korrekturen gingen ins **Skelett** und in eine **README** | **DRIN LASSEN** — beide Hälften scheitern |
| `b9plus_nachtrag_independence_und_indirect.md` | **0** | **TEILWEISE.** Die operativen Befunde zu `independence` und `allow_indirect_imports` stehen im Protokoll (§ zu den Skip-Contracts); **§6 „Aufgefallen, aber nicht verfolgt" trägt acht Beobachtungen, die nirgends eingegangen sind** (Kantendifferenz zum B9+-Fixture, geschluckte Contract-Optionen, Sortierstabilität, `independence` mit >2 Modulen, `as_packages`, Pfaddarstellung, PyTestArch-Regelzahl für n>3, „ein Test = eine Regel") | **DRIN LASSEN** — (i) nicht vollständig |

**Konsequenz.** Das Bündel wird durch B2 **nicht kleiner**. Das ist das ehrliche Ergebnis der
mechanischen Anwendung, nicht ein Ausweichen: die Berichte sind quer vernetzt, und ein
Bericht, dessen Beobachtungen nirgends sonst stehen, ist keine überholte Fassung, sondern die
einzige Fundstelle. **Keine Datei ist gelöscht, kein git-Verlauf berührt.**

### 6.3 B3 — Bündel neu erzeugt

| | vorher | nachher | Differenz |
|---|---:|---:|---:|
| Dateien | **104** | **105** | **+1** |
| Bytes | **3 691 864** | **3 743 169** | **+51 305** (**+50,1 KB**) |
| Zeilen | 52 258 | 52 904 | +646 |

Die Zunahme ist **genau** die aufgenommene Auswertungsausgabe.

---

## 7 Endstand

```
$ git status --porcelain          # masterarbeit, tritongraph,
                                  # tritongraph-measure, ma-conformance-testrepo
(leer, alle vier)

$ python3 tools/check_doc_invariants.py
ERGEBNIS: alle 5 Invarianten erfüllt                       → Exit 0

$ sha256sum -c data/campaign/eval/SHA256SUMS
6 von 6 OK
```

**Was jetzt gilt.** Die Markerdarstellung ist über **alle** Tabellen einheitlich und durch
**R10** maschinell gesichert; keine Zahl steht mehr in Exponentialform. Die
T5-Zeilenbeschriftungen sagen, **welchen** Nenner sie nennen. Die Anforderung aus T5 (ii) ist
**erledigt statt offen**, mit Begründung in Skelett, Spezifikation und Protokoll (Rev. 42).
Der dritte Lauf liegt archiviert und gehasht neben dem ersten und dem zweiten, und die
Gegenüberstellung weist **null Wertänderungen** aus — der JSON-Rumpf beider Läufe ist
bitgleich.

**Ein Punkt bleibt offen und wird nicht stillschweigend gelassen.** Der Vermerk **an T5 in
der Ausgabe** trägt weiter den Wortlaut „**LÜCKE, benannt und nicht gefüllt**", während
Skelett, Spezifikation und Protokoll Rev. 42 die Anforderung als **erledigt und
gegenstandslos** führen. Der Vermerk steht im Renderer; ihn nachzuziehen ist eine
Instrumentenänderung und zöge einen **vierten Lauf** nach sich, den dieser Auftrag
ausschliesst — und er hätte die Gegenüberstellung dieses Auftrags über die vorab benannten
Ausnahmen hinaus verschoben. Der Punkt gehört in einen Folgeauftrag, zusammen mit dem
nächsten ohnehin fälligen Lauf.
