# C14 — Artefaktauswahl repariert, Overlap-Tabelle T10, vierter Auswertungslauf

**Masterarbeit Timo Haas · HTWG Konstanz**
Datum: 28. August 2026 · Auftrag **C14** · Schreibendes Repo: `masterarbeit`;
`tritongraph`, `tritongraph-measure` und `ma-conformance-testrepo` **nur lesend**

**Commits dieses Auftrags:**

| # | SHA | Titel |
|---|---|---|
| 1 | `fd1222e` | `docs: register the valid-artefact selection rule and table T10` |
| 2 | `e7a192b` | `test: hand-computed expectations for artefact selection and the overlap table` |
| 3 | `02d480e` | `fix: select the valid run artefact and assert against invalid ones` |
| 4 | `9d2772b` | `feat: render the overlap table T10` |
| 5 | `8744a30` | `docs: refreeze the evaluation instruments` |
| 6 | `3b5684d` | `data: archive the fourth evaluation run` |
| 7 | `ec7ef7a` | `chore: index the evaluation runs and bundle the canonical output` |
| 8 | *(dieser Bericht)* | `docs: report the artefact-selection repair, T10 and the fourth run` |

> **DEUTUNGSSPERRE, wie in C11b und C11d.** Dieser Bericht **bewertet keine Ergebnisse**,
> **vergleicht keine Konfigurationen in Worten** und **empfiehlt nichts** zu Prompt,
> Schema, Regeldatei, Manifest oder Metrikdefinition. Wo unten eine Zahl neben einer
> anderen steht, steht sie dort, weil die Gegenüberstellung sie nebeneinander führt —
> nicht als Aussage über ihr Verhältnis. Was der vierte Lauf **bedeutet**, gehört nach
> Befund 08 und Kapitel 8 und wird hier nicht vorweggenommen.
>
> **Nicht Gegenstand dieses Auftrags:** Befund 08, der C10-Abschlussbericht,
> Kapitelprosa, ein fünfter Lauf, Standdokument, offene Punkte, Arbeitsplan, Gate-Notiz,
> Z1, L1, A-38, die Wurzel-README, die Bündel-Anhangskürzung. **Kein `git push`.** Keine
> Datei gelöscht, kein git-Verlauf berührt, kein Artefakt unter `data/campaign/k*`
> bewegt.

---

## 0 Vorbedingungen

| Prüfung | Erwartet | Befund |
|---|---|---|
| `masterarbeit` porcelain | leer | leer, HEAD `33dd4af` ✅ |
| `tritongraph` porcelain | leer | leer (Branch `feat/conformance-checker`) ✅ |
| `tritongraph-measure` porcelain | leer | leer (detached `348ca9d`, der Messstand) ✅ |
| `ma-conformance-testrepo` porcelain | leer | leer ✅ |
| Runner aktiv? | nein | Prozessliste ohne Treffer ✅ |
| `python3 tools/check_doc_invariants.py` | Exit 0 | **alle 5 Invarianten erfüllt** ✅ |
| `sha256sum -c data/campaign/eval/SHA256SUMS` | 6 / 6 OK | **6 von 6 OK** ✅ |

**C11, C12 und C13 sind über diesen Auftrag hinweg unberührt:** nicht überschrieben,
nicht gelöscht, nicht nachbearbeitet. `sha256sum -c` bestätigt das nach jedem Commit.

---

## 1 Phase 1 — die Registrierung, vor jeder Rechnung (Protokoll Rev. 44)

Registriert **vor** der ersten Zeile Reparaturcode und **vor** dem Lauf, an allen drei
Stellen: Kopf-Revisionshistorie, §10-Amendmenttabelle, dazu Auswertungsspezifikation und
Tabellenskelett; beide Hashes nachgezogen, Protokoll-SHA in `c5b` §3 bezeugt, Prüfer
Exit 0.

### 1.1 Der Defekt, ungeschminkt

**Was verletzt wurde, wörtlich aus Protokoll §7:**

> „liegt `valid_final` einer LLM-Konfiguration unter 0.9, wird das als Befund dokumentiert
> und die Konfiguration mit den vorhandenen validen Läufen ausgewertet — nicht
> nachgebessert. Operationalisierung: `valid_final=false`-Läufe sind über Exit-Code 3 bzw.
> das persistierte Run-Log (CLI-Inkremente 2 und 4) identifizierbar; **stille Zählung
> invalider Läufe als „0 Findings" ist damit ausgeschlossen**."

**Genau das ist in der Auswertung geschehen.** Die Auflösungsregel
`<cfg>_*<injection_sha256>.json` trifft die Datei **ohne** `_r<n>`-Suffix, also den
**ersten** Versuch. Für **elf** K3-Injektionen — I05, I06, I07, I09, I11, I13, I16, I20,
I21, I22, I23 — trägt dieses Artefakt im gehashten Laufmanifest
`postrun.verdict = INVALID` mit Grund `transport_failure`; ausgezählt in
`c11d_bericht_befund08_grundlagen.md` §A6b. K2 ist nicht betroffen (null
Wiederholungen). **T7 wies die Gültigkeit dabei die ganze Zeit korrekt aus** — T7.4
listet alle 29 ungültigen Invocationen namentlich, T7.3 meldet null Injektionen ohne
gültigen Lauf. Die Auswertung las **an ihrer eigenen, richtig gedruckten
Gültigkeitstabelle vorbei**.

**Die Stufe toleriert das nicht.** Z3 ist als **kontrolliertes Experiment** registriert
(`00_stand_und_entscheidungen.md` §5, `methodik_begruendung` §6). Auf dieser Evidenzstufe
ist die Auswahl der ausgewerteten Läufe Teil des Messverfahrens.

**Die Richtung, benannt und nicht umschrieben: die Reparatur wird die K3-Zahlen
voraussichtlich VERBESSERN.** Vier Gründe tragen sie trotzdem, jeder für sich:

1. **Die verletzte Regel war vorregistriert** — §7, oben wörtlich, seit Rev. 33
   eingefroren. Nichts daran ist nach Sichtung der Daten formuliert.
2. **Der Defekt fiel durch eine vor dem Befund beauftragte mechanische Auszählung auf**
   (C11d A6b) — nicht durch die Suche nach einer Erklärung für eine unbefriedigende Zahl.
3. **Es ist eine Artefaktauswahl, KEINE Metrikänderung.** `strict`, `localized`,
   Precision, Recall, F1, Median, Spannweite, FP-Rate und die vier Marker stehen
   zeichengleich.
4. **C11, C12 und C13 bleiben archiviert** und werden gegenübergestellt, nicht ersetzt.

**Zur T1-Abweichung „K3: Soll ja / Ist teilweise".** Sie war nach damaligem Stand ein
Artefakt der Dateiauswahl (C11d §A6.1: das gelesene Artefakt von I23 trägt
`calls_transport_failed: 3`, Exit 3, null Records). **In Phase 1 wurde das ausdrücklich
nicht vorweggenommen**; was der Lauf zeigt, steht in §5.3.

### 1.2 Die registrierte Regel

Für jedes Paar (Konfiguration, Injektion) liest die Auswertung das Artefakt, dessen
**gehashtes Laufmanifest** `postrun.verdict == VALID` trägt; bei mehreren gültigen
Versuchen den **frühesten** (kleinster `attempt`); bei keinem gilt **`n. e.`** mit
Eintrag in **T7.3**. Entschieden wird aus dem **Laufmanifest** — **nicht** aus dem
Dateinamen und **nicht** aus der Zahl der Records. Fundstelle:
**Auswertungsspezifikation §1.9** (neu).

Dazu **R12**: der Lauf bricht mit **Exit 2** ab, wenn ein Artefakt gelesen wird, dessen
Laufmanifest ein Verdikt ≠ `VALID` trägt oder das gar keines hat. **Ausgenommen und
benannt:** die Run-Logs `*.jsonl`, die **T6** über **alle** Invocationen liest — die
Laufkosten sind angefallen, gültig oder nicht, und sie tragen keine Trefferzelle.

### 1.3 T10 — die Lücke gegen §8

Protokoll §8 verlangt für **UF3** eine „Overlap-Analyse K1/K4/K5 vs. K2/K3";
`c11d_bericht_befund08_grundlagen.md` §B5 hat belegt, dass die registrierte Ausgabe keine
enthielt. Registriert als **T10** im Tabellenskelett (eigener Abschnitt,
Druckreihenfolge Position 10, §0.3-Zuordnung, Anhangzeile **A-39**) und in der
Auswertungsspezifikation (**§8 Punkt 10**):

- **Basis: die bereits gerechneten Trefferzellen** — keine neue Metrik, keine neue
  Schwelle, keine neue Vergleichsvorschrift, kein neuer Nenner.
- **T10a** = `localized`, **T10b** = `strict`, in **getrennten** Teiltabellen.
- **K2 und K3 werden NICHT zu „dem LLM-Pfad" vereinigt** — je Konfiguration eine eigene
  Zeilengruppe.
- Die **Baselineseite ist eine Vereinigung** K1 ∪ K4 ∪ K5, im Kopf **und in jeder Zelle**
  als solche benannt (die Zelle nennt die tragenden Konfigurationen).
- Vier Zustände je Injektion: **nur Baseline · nur die LLM-Konfiguration · beide ·
  keiner**.
- **Markerdisziplin:** eine Injektion, die eine Seite nach T8 nicht **ausdrücken** kann,
  ist dort **nicht verfehlt**; eigene Klasse, **nie** in „nur die andere Seite"
  umgedeutet. `n. b.`, `n. e.` und T9 Fall 6/7 gehen weder als Treffer noch als
  Verfehlung ein.
- **Aggregatzeile je Gruppe mit ausgewiesenem Nenner**, wie in T5.
- Nach Skelett §0.3 eine **gerechnete** Tabelle, **kein Aufschrieb**.

### 1.4 Eine Vorrangregel, die noch in Phase 1 korrigiert wurde — ungeschminkt

Die erste Fassung der Registrierung führte die Zellzustände in der Reihenfolge
`n. b.` → `n. e.` → **Sonderklasse** → ` — `. Das widerspricht **T5 Auflage (2)** für
genau eine Konstellation: eine ` — `-Zelle, die **zugleich** eine vorregistrierte
Sonderklasse trägt — **K2/`CYCLE` und K3/`CYCLE`**, wo jeder Fund T9 Fall 6 ist. In T5
gewinnt dort ` — `, weil ` — ` eine Aussage über das **Werkzeug** ist und die
Sonderklasse eine über einen **Fund**. Die Reihenfolge wurde auf
`n. b.` → `n. e.` → ` — ` → Sonderklasse gebracht und die Konstellation **namentlich** in
Skelett und Spezifikation aufgenommen — **vor** dem Abschluss des Registrierungscommits,
so dass keine Fassung mit der falschen Vorrangregel je Grundlage einer Rechnung war.
**Der Registrierungscommit `fd1222e` trägt die korrigierte Fassung.**

### 1.5 Der überholte T5-Vermerk (R14)

Die Ausgabe druckte an T5 weiter „**LÜCKE, benannt und nicht gefüllt**", während Skelett
T5 (ii), Spezifikation §8 Punkt 1 und Protokoll die Anforderung seit **Rev. 42** als
**gegenstandslos erledigt** führen (C11c §2). Der Renderertext ist mit der
Rev.-42-Begründung nachgezogen: die Anforderung wird **nicht abgewiesen**, sie
**entfällt**; die Laufstreuung steht seit Rev. 40 je Repetition einzeln in der
T4-Spalte „Läufe (Ruhe · Kampagne)". **Keine Zelle bewegt sich.**

### 1.6 Hash-Kette nach Phase 1

| Gegenstand | vorher | nachher |
|---|---|---|
| `c6_auswertungsspezifikation.md` | `fe991be6…092c20d1` | **`39822edc…d2cd71c7`** |
| Protokoll (Rev. 43 → **44**) | `759b11ed…369343f4` | **`ba865b2b…aa18309b`** |

Beide an **beiden** registrierten Stellen nachgezogen (Protokoll §0.1 **und** §1
Nachtrag Rev. 30), der Protokoll-SHA in `c5b_bericht_protokoll_freeze.md` §3 bezeugt.
**Prüfer nach Commit 1: alle 5 Invarianten erfüllt, Exit 0.**

---

## 2 Phase 2 — die Erwartungen, ALLEIN und ZUERST committet

`tests/fixtures/harness/EXPECTED.md` §16 ist mit den Fixture-Daten in **Commit 2**
(`e7a192b`) committet — **vor** jeder Zeile der Reparatur (Commit 3) und vor jedem Lauf.
Der Zeitstempel ist der Beleg. Dieselbe Disziplin wie in C6b und C11b.

### 2.1 Was am Fixture ergänzt wurde

**(A) K2/I25 wird zur Wiederholungskette** — der von der Auflage verlangte Fall „erster
Versuch INVALID, dritter VALID":

| Versuch | Verdikt | Artefakt | Inhalt |
|---|---|---|---|
| 1 | **INVALID** (`transport_failure`, 3 Calls) | `k2_ef114806….json` | **Köder: null Findings** |
| 2 | **INVALID** | `k2_ef114806…_r2.json` | **Köder: null Findings** |
| 3 | **VALID** | `k2_ef114806…_r3.json` | der bisherige Inhalt (Schlüssel E, dreimal) |

**Der Köder liegt genau unter dem Namen, den die alte Regel traf.** Damit ist die
Erwartung entscheidbar: mit R11 wird `_r3` gelesen und **jede** Ergebniszelle von K2/I25
bleibt, was sie in §5.2, §8, §11 und §13 von EXPECTED steht; mit der alten Namensregel
fiele K2/I25 auf `strict` 0, `localized` 0, Kampagne 0, Δ −3, Läufe `[3,3,3] · [0,0,0]`.
**Die zweite Hälfte der Auflage — „eine ohne Wiederholung" — ist vierfach besetzt**
(K2/I02, I04, I14, I21) und unverändert.

**(B) K3/I25 bekommt den R12-Köder.** K3/I25 hat weiterhin **genau eine** Invocation und
die ist **INVALID**; die Injektion bleibt **ohne gültigen Lauf** und trägt **`n. e.`**
Daneben liegt jetzt ein Artefakt `k3/k3_ef114806….json`, das den **richtigen** Fund
trägt — die Konstellation von C13 im Kleinen.

### 2.2 Was der Lauf gegen das Fixture zeigt

**Gegen die alte Namensregel, gleicher Fixture-Bestand** (Negativprobe): K2/I25 fällt
zusammen — T1 `**K2: Soll ja / Ist nein**`, T2 `0/1 | 0/1`, T4 Kampagne 0, Δ −3, Läufe
`[0,0,0] · [0,0,0]`, T5 `STRUCTURAL_PLACEMENT` auf `0/0` bzw. `0/1 = 0,000`.
**Mit R11**: alle diese Zellen stehen auf den handgerechneten Werten.

**Gegen den Stand VOR C14** (altes Werkzeug, altes Fixture) ist der Fixture-Lauf in
**jeder** Metrikzelle von T1, T2, T3, T4, T5, T8 und T9 **zeichengleich**. Bewegt sind
allein:

| bewegt | warum |
|---|---|
| T7.1 K2: 5 → **7** Invocationen, 0 → **2** INVALID, 15 → **21** Calls, 0 → **6** `transport_failed`, 0 → **2** Wiederholungen; `valid_final` **15/15 = 1,000** unverändert | die zwei neuen Fixture-Invocationen |
| T7.2: 15 → **17** Invocationen in der Zählregel | dieselben |
| T7.4: **zwei neue Zeilen** (K2/I25 Versuch 1 und 2, je „VALID in einem späteren Versuch"); die Zeile K3/I25 bleibt „ohne gültigen Lauf" | dieselben |
| T6 K2: 5 → **7**, 15 → **21** Calls, 12 500 → **17 500 ms** aussen, 12 000 → **16 800 ms** innen, 1500 → **2100** Tokens in, 750 → **1050** Tokens out; Mediane und Spannweiten **unverändert** | dieselben |
| der T5-Vermerk | **R14** |
| **T10** | **R13**, neu |

**Jede dieser Zahlen steht so in EXPECTED §16.2 — von Hand gerechnet, vor dem Lauf.**
T7.3 ist zeichengleich: die `n. e.`-Menge bleibt genau `{I25}` bei K3, Journal und
Prosa-Manifest deckungsgleich.

### 2.3 T10 am Fixture — gegen die Handrechnung

Die vier Zeilengruppen (T10a/T10b × K2/K3) stimmen **Zelle für Zelle** mit EXPECTED
§16.3 überein, einschliesslich der Seitenzustände und der Aggregate:

| | `nur Baseline` | `nur K2`/`nur K3` | `beide` | `keiner` | **Nenner** | ausserhalb |
|---|---|---|---|---|---|---|
| T10a / K2 | 0 | 0 | 2 | 1 | **3** | Baseline n.a. 1 · K2 n.a. 1 · beide n.a. 0 · n.beurt. 0 |
| T10a / K3 | 0 | 1 | 1 | 0 | **2** | Baseline n.a. 1 · K3 n.a. 1 · beide n.a. 0 · n.beurt. 1 |
| T10b / K2 | 0 | 1 | 1 | 1 | **3** | Baseline n.a. 1 · K2 n.a. 1 · beide n.a. 0 · n.beurt. 0 |
| T10b / K3 | 0 | 1 | 1 | 0 | **2** | Baseline n.a. 1 · K3 n.a. 1 · beide n.a. 0 · n.beurt. 1 |

**Die Konstellation, die die Vorrangregel entscheidet, kommt im Fixture vor:** K2/I14 und
K3/I14 tragen ` — ` **und** die Sonderklasse T9-6 und bleiben **nicht ausdrückbar**;
K5/I14 trägt **keinen** Marker und die Sonderklasse T9-7 und ist in **beiden** Metriken
Sonderklasse.

**Zusätzlich erschöpfend geprüft:** die Zuordnung (Baselinezustand, LLM-Zustand) → Klasse
gegen **alle 16** Paare der handgerechneten Tabelle in EXPECTED §16.4 — **16 von 16 OK,
0 Abweichungen**. Die vier Zeilen, in denen eine schlampige Implementierung eine nicht
ausdrückbare Seite zu „nur die andere Seite" machte, sind darin enthalten.

### 2.4 Alle bestehenden Fixtures erneut

| Prüfung | Erwartet | Gemessen | |
|---|---|---|---|
| `match_k4k5.py --selftest` | 34 von 34 | **34 von 34, 0 Abweichungen** | ✅ |
| Selbsttest B — K2 modulweise je Lauf | 49 / 49 / 49 | 49 / 49 / 49 | ✅ |
| Selbsttest B — K2 Headline | **49/52** | **49/52**, Median 49, Spannweite 49–49 | ✅ |
| Selbsttest B — K2 findingweise | **461** (155/153/153) | 155 / 153 / 153, Summe **461** | ✅ |
| Selbsttest B — K3 modulweise je Lauf | 2 / 1 / 0 | 2 / 1 / 0 | ✅ |
| Selbsttest B — K3 Headline | **1/52** | **1/52**, Median 1, Spannweite 0–2 | ✅ |
| Selbsttest B — K3 findingweise | **3** (2/1/0) | 2 / 1 / 0, Summe **3** | ✅ |
| Fixture-Lauf `--with-campaign` | Exit 0 | **Exit 0**, kein `stderr` | ✅ |

### 2.5 Alle Zusicherungen negativ probiert

| # | Zusicherung | Provokation | Ergebnis |
|---|---|---|---|
| P1 | `Cell.__post_init__` — Marker **und** Wert | `Cell(value=0, marker=" — ")` | `MarkerViolation: Zelle trägt Marker ' — ' UND Wert 0 …` |
| P2 | `Cell.__post_init__` — unbekannter Marker | `Cell(marker="n. x.")` | `MarkerViolation: unbekannter Marker 'n. x.'` |
| P3 | **R2** — gerechnete Grösse rendert leer | `num("")` · Gegenprobe `num(0)` | `MarkerViolation: … (R2)` · `num(0) = '0'` |
| P4 | `assert_marker_discipline` | ` — `-Zelle mit Wert 0 vorbeigeschmuggelt | zwei Meldungen: `Marker ' — ' und Wert 0` · `' — ' als 0 gebucht` |
| P5 | **R1** Ende-zu-Ende | `kein_en_cell` liefert `""` | `LEERZELLE: T4 … Spalte 'K2 kein-EN'` …, **Exit 2** |
| P7 | `n. e.` ohne T7-Beleg | Laufmanifest K3/I25 aus der Fixture-Kopie entfernt | `HARNESS-FEHLER: I25/K3 trägt n. e. ohne T7-Beleg`, **Exit 2** |
| P8 | Blindheit | Kampagnenartefakt geöffnet · Gegenprobe Laufmanifest | `BLINDHEITSVERLETZUNG: …/k2/…json` · Manifest: keine Verletzung |
| P10 | T7-Gegenprobe weicht ab | Journalzeile K2/I25 `_r3` auf `INVALID` | 2 × `HARNESS-BEFUND` auf `stderr`, **Exit 0** (Befund, kein Defekt) |
| P11 | UF4-Nenner gegen T8 | `UF4_DENOMINATOR["K4"]` auf 18 | `HARNESS-FEHLER: UF4-Nenner K4: 19 … gegen vorregistrierte 18 (T8)`, **Exit 2** |
| P13 | **R10 (a)** Marker ohne Auszeichnung · Gegenprobe | roher `—`/`n. b.` in einer Zelle · Gedankenstrich im Satz | zwei Meldungen · **keine** Meldung |
| P14 | **R10 (b)** Exponentialform | `9.19054e+06 ms` | `Zeile 3: Zahl in Exponentialform '9.19054e+06'` |
| P15 | **R10 (a)** Ende-zu-Ende | `Score.cells()` auf den rohen Markerstring zurückgesetzt | `DARSTELLUNG: T5 … Marker '—' ohne Code-Auszeichnung`, **Exit 2** |
| P16 | **R10 (b)** Ende-zu-Ende | `plain()` auf blosses `%g` zurückgesetzt | 2 Meldungen (`9.19054e+06`, `9.13543e+06`), **Exit 2** |
| **P17** | **R12** am **Fixture** | Auswähler auf die alte Namensregel zurückgesetzt | **2** Verstösse (K2/I25 und K3/I25), **Exit 2** |
| **P18** | **R12** am **echten Bestand** | dieselbe Rücksetzung | **11** Verstösse — **genau die elf K3-Injektionen aus C11d §A6b** —, **Exit 2** |
| **P19** | **R12** — Artefakt ohne Laufmanifest | erfundener Pfad `k2/k2_deadbeef.json` | `… — kein Laufmanifest gleichen Namens` |
| **P20** | **R12** — Gegenprobe Run-Log | `k2_…jsonl` in die Leseliste gelegt | **keine** Meldung — T6 liest alle Invocationen, richtig |
| **P21** | **T10-Buchungsprobe** | eine Injektion aus der Klassenzählung entfernt | `HARNESS-FEHLER: T10/… 0 gebuchte gegen 1 der Zeilengruppe`, **Exit 2** |
| **P22** | **R11** — Artefakt des gültigen Versuchs fehlt | `k2_…_r3.json` aus der Kopie gelöscht | `HARNESS-FEHLER: K2/I25 hat einen gültigen Lauf …, das zugehörige Artefakt … fehlt` |
| **P23** | **R11** — Commit-Gegenprobe | `target_repo_git_head` im Laufmanifest verstellt | `HARNESS-FEHLER: Laufmanifest … steht auf Commit 000…, das Injektionsmanifest nennt für I25 ef114806…` |

Nach jeder Probe wurde `tools/evaluate_campaign.py` wiederhergestellt und mit `cmp`
**byte-identisch** gegengeprüft; keine Probe hat in `data/` geschrieben.

> **Ungeschminkt: solange der Auswähler richtig ist, KANN kein Fixture R12 auslösen.**
> R11 wählt nur Artefakte mit Verdikt `VALID`, R12 prüft, dass nur solche gelesen wurden
> — beide sind dann per Konstruktion einig, und **genau das ist die Aussage von R12**.
> Der Abbruch wird deshalb an dem dafür gebauten Fixture ausgelöst, indem der Auswähler
> auf die alte Namensregel zurückgesetzt wird (**P17**); **P18** zeigt dieselbe Probe am
> echten Bestand. Das ist zugleich der Nachweis, dass R12 **den Defekt von C13
> abgefangen hätte**: mit R12 wäre der dritte Lauf mit Exit 2 abgebrochen, statt elf
> ungültige Artefakte still auszuwerten.

### 2.6 Instrumenten-Hashes neu gebildet — Protokollrevision 45

Commit **`8744a30`**. **Eine eigene Revision, obwohl reiner Bytestandsnachzug** — §0.1
Punkt 5, Präzedenz Rev. 36, 41 und 43. Unter Rev. 44 vollzogen, stünde der in `c5b` §3
bezeugte Bytestand von Rev. 44 in keinem Dokument mehr.

| Datei | Rev. 43 | Rev. 45 |
|---|---|---|
| `tools/evaluate_campaign.py` | `eb206a6f…b520653` | **`b66be750…f079a93428`** |
| `tools/match_k4k5.py` | `c16e7c43…799f4ca6` | **unverändert** |
| `tools/check_doc_invariants.py` | `6cc16ef9…1e52b7018` | **unverändert** |

Protokoll-SHA nach Rev. 45: **`0ce57d29…5ff92eca`**, in `c5b` §3 bezeugt.
**Invariante (E) grün, Prüfer Exit 0 — Gatter passiert.**

**Ungeschminkt: (E) war zwischen Commit 4 und Commit 5 rot** (`FEHL
tools/evaluate_campaign.py`, IST gegen SOLL). Das ist die vorgesehene Reihenfolge, keine
Panne: ein Nachzug im selben Commit machte Reparatur und Registrierung
ununterscheidbar, ein Nachzug unter Rev. 44 machte deren Bytestand unbezeugt. Dieselbe
Lage bestand in C11b und C11c. **Nach den Commits 1, 2, 5, 6 und 7 stand der Prüfer auf
Exit 0.**

---

## 3 Phase 3 — der vierte Lauf

**Ein Lauf**, vollständiger Bestand, unverändert gegenüber den ersten drei (alle sechs
Block-`SHA256SUMS` zeichengleich).

```
$ python3 tools/evaluate_campaign.py --with-campaign \
    --json-out data/campaign/eval/c14_eval_full.json \
    --markdown-out data/campaign/eval/c14_eval_full.md
                                                           → Exit 0
```

| | |
|---|---|
| **Zeitstempel** | 2026-08-28T23:49:10+02:00 bis 2026-08-28T23:49:10+02:00 |
| **Laufzeit** | 0:00.26 wall, 27 308 KB maxrss |
| **git HEAD** | `8744a30` (Rev.-45-Stand) |
| **Protokoll** | Rev. 45, `0ce57d29…5ff92eca` |
| **Spezifikation** | `39822edc…d2cd71c7` |
| **Instrumente** | `b66be750…` / `c16e7c43…` / `6cc16ef9…` |
| **gelesene Dateien** | **658**, davon **253** Kampagnen-Laufartefakte — **wie im zweiten und dritten Lauf** |
| **`stderr`** | **leer** — keine Markerverletzung, kein Harness-Fehler, kein Harness-Befund, **kein R12-Verstoss** |
| **Ausgabe** | `c14_eval_full.json` / `.md`, Kopf mit Instrumenten-, Protokoll-, Spezifikations- und Blockhashes vorangestellt |

**Sofort archiviert und committet**, vor jeder weiteren Arbeit: Commit **`3b5684d`**,
`SHA256SUMS` ergänzt, `sha256sum -c` **8 von 8 OK**, Prüfer Exit 0.

| Datei | SHA256 |
|---|---|
| `c14_eval_full.json` | `46ba024d266398cea278103592daf12c2a04193f9b45caa4812ce20333cc0a71` |
| `c14_eval_full.md` | `ed59aa95f01b2a73e773110e5aa56b45b6d687c49f812dcca1bad8ed65e2329b` |

**C11, C12 und C13 liegen unberührt daneben.**

### 3.1 Welche Artefakte anders gelesen wurden — mechanisch, vor jeder Zelle

Die Leseliste des Laufs (`reads.campaign_run_artifacts`, 253 Pfade in beiden Läufen)
unterscheidet sich in **genau elf** Einträgen, **1 : 1 getauscht**, alle in K3:

| Injektion | c13 gelesen | c14 gelesen |
|---|---|---|
| I05 | `k3_dbcd05b8….json` | `k3_dbcd05b8…_r3.json` |
| I06 | `k3_531a1ff2….json` | `k3_531a1ff2…_r3.json` |
| I07 | `k3_0993e01b….json` | `k3_0993e01b…_r3.json` |
| I09 | `k3_06e052e1….json` | `k3_06e052e1…_r5.json` |
| I11 | `k3_5601a944….json` | `k3_5601a944…_r6.json` |
| I13 | `k3_3be646fe….json` | `k3_3be646fe…_r3.json` |
| I16 | `k3_43f9fa5e….json` | `k3_43f9fa5e…_r3.json` |
| I20 | `k3_35061d85….json` | `k3_35061d85…_r3.json` |
| I21 | `k3_dd414657….json` | `k3_dd414657…_r3.json` |
| I22 | `k3_08a622b0….json` | `k3_08a622b0…_r2.json` |
| I23 | `k3_28a75749….json` | `k3_28a75749…_r6.json` |

**Deckungsgleich mit der Vorhersage in EXPECTED §16.6**, die vor dem Lauf committet war
— dieselben elf Paare, dieselben Suffixe. **Für alle übrigen 149 Paare ist es
buchstäblich dieselbe Datei.**

---

## 4 Gegenüberstellung c13 → c14, zellweise

### 4.1 Die Bilanz auf den Injektionszellen (JSON, 1952 Zellen)

| | Zahl |
|---|---|
| Injektionszellen gesamt (32 Injektionen × 5 Konfigurationen × alle Felder) | **1952** |
| **geändert** | **35** |
| neu hinzugekommen / entfallen | **0 / 0** |
| geänderte Zellen in **K1** | **0** |
| geänderte Zellen in **K2** | **0** |
| geänderte Zellen in **K3** | **35** |
| geänderte Zellen in **K4** | **0** |
| geänderte Zellen in **K5** | **0** |
| betroffene Injektionen | **11** — I05, I06, I07, I09, I11, I13, I16, I20, I21, I22, I23 |
| betroffene Felder | `campaign`, `campaign_per_run`, `delta`, `kein_en`, `localized`, `runs`, `strict` |

> **DER ABBRUCHGRUND IST NICHT EINGETRETEN.** Der Auftrag nennt **jede** Änderung in
> einer K2-, K1-, K4- oder K5-Zelle als Abbruchgrund. Es gibt **keine**. Die betroffenen
> Injektionen sind **exakt** die elf aus C11d §A6b — keine zwölfte, keine zehnte.

**Die übrigen Aggregate des JSON, Schlüssel für Schlüssel:**

| Schlüssel | c13 gegen c14 |
|---|---|
| `false_positives` (T3), `preregistered_control` (T3.1), `rule_id_distribution`, `reference_classes` | **zeichengleich** |
| `t7` (T7.1–T7.4 vollständig) | **zeichengleich** |
| `cost` (T6) | **zeichengleich** |
| `co_findings`, `specials`, `preregistered` (T9) | **zeichengleich** |
| `journal`, `manifest_missing`, `manifest_completeness`, `control_denominator` | **zeichengleich** |
| `reads` | **geändert** — die elf getauschten Pfade, Gesamtzahl 658 unverändert |
| `t10`, `invalid_artifacts_read` | **neu** (`invalid_artifacts_read` ist leer) |

### 4.2 Jede geänderte Tabellenzelle, einem Grund zugeordnet

Über die gerenderte Ausgabe (2070 Tabellenzellen in c13): **46 geänderte Zellen, 792 neue
(T10a/T10b), 0 entfallene.**

| Tabelle | geänderte Zellen | Grund |
|---|---|---|
| **T1** | **2** | **R11** |
| **T2** | **2** | **R11** |
| **T4** | **24** | **R11** |
| **T5** | **18** | **R11** |
| **T3, T6, T7, T8, T9** | **0** | — |
| **T10a / T10b** | **792 neu** | **T10 (neu)** |
| T5-Vermerk (Fliesstext, keine Zelle) | — | **R14 (Text)** |
| **sonstiges** | **0** | — |

**Nicht eine einzige geänderte Zelle steht ausserhalb dieser Zuordnung.** Die einzige
geänderte Zelle, deren Zeilen- oder Spaltenbeschriftung nicht selbst „K3" nennt, ist die
`Abweichung`-Zelle der T1-Zeile `FRAMEWORK_TYPE_IN_SIGNATURE` — ihr **Inhalt** nennt K3
(siehe §5.3).

**T1 — 2 Zellen**

| Zeile | Spalte | c13 | c14 |
|---|---|---|---|
| `FRAMEWORK_TYPE_IN_SIGNATURE` | Ist K3 | `3/4` | `4/4` |
| `FRAMEWORK_TYPE_IN_SIGNATURE` | Abweichung | `**K3: Soll ja / Ist teilweise**` | *(leer = gerechnet, keine Abweichung)* |

**T2 — 2 Zellen**

| Zeile | Spalte | c13 | c14 |
|---|---|---|---|
| `FRAMEWORK_TYPE_IN_SIGNATURE` (4) | K3 loc | `3/4` | `4/4` |
| `FRAMEWORK_TYPE_IN_SIGNATURE` (4) | K3 str | `3/4` | `4/4` |

**T4 — 24 Zellen, alle in der K3-Hälfte der elf Zeilen**

| Injektion | Spalte | c13 | c14 |
|---|---|---|---|
| I05 | K3 Läufe | `[0,0,0] · [1,0,1]` | `[0,0,0] · [1,1,1]` |
| I06 | K3 Kampagne · Δ · Läufe | `0` · `0` · `[0,0,0] · [0,0,1]` | `1` · `1` · `[0,0,0] · [1,1,1]` |
| I07 | K3 Läufe | `[0,0,0] · [1,0,1]` | `[0,0,0] · [1,1,1]` |
| I09 | K3 Läufe | `[0,0,0] · [0,1,1]` | `[0,0,0] · [1,1,1]` |
| I11 | K3 Läufe | `[0,0,0] · [1,1,0]` | `[0,0,0] · [1,1,1]` |
| I13 | K3 Läufe | `[0,0,0] · [1,1,0]` | `[0,0,0] · [1,1,1]` |
| I16 | K3 Kampagne · Δ · Läufe | `0` · `0` · `[0,0,0] · [0,0,0]` | `1` · `1` · `[0,0,0] · [1,1,1]` |
| I20 | K3 Kampagne · Δ · Läufe | `0` · `0` · `[0,0,0] · [1,0,0]` | `1` · `1` · `[0,0,0] · [1,1,1]` |
| I21 | K3 Kampagne · Δ · Läufe | `0` · `0` · `[0,0,0] · [0,0,1]` | `1` · `1` · `[0,0,0] · [1,1,1]` |
| I22 | K3 Läufe | `[0,0,0] · [1,0,1]` | `[0,0,0] · [1,1,1]` |
| **I23** | K3 `loc` · K3 `strict` · Kampagne · Δ · kein-EN · Läufe | `0` · `0` · `0` · `0` · `entfällt` · `[0,0,0] · [0,0,0]` | `1` · `1` · `1` · `1` · `nein` · `[0,0,0] · [1,1,1]` |

**T5 — 18 Zellen, alle in K3-Zeilen**

| Zeile | c13 (`strict` P / R / F1 — `loc` P / R / F1) | c14 |
|---|---|---|
| K3 · `FORBIDDEN_SIGNATURE_TYPE` | `3/3 = 1,000` / `3/4 = 0,750` / `0,857` — dieselben drei | `4/4 = 1,000` / `4/4 = 1,000` / `1,000` — dieselben drei |
| K3 · **Gesamt UF3** | `27/27 = 1,000` / `27/32 = 0,844` / `0,915` — dieselben drei | `28/28 = 1,000` / `28/32 = 0,875` / `0,933` — dieselben drei |
| K3 · **Gesamt UF4** | `27/27 = 1,000` / `27/28 = 0,964` / `0,982` — dieselben drei | `28/28 = 1,000` / `28/28 = 1,000` / `1,000` — dieselben drei |

**T7.4 ist zeichengleich geblieben.** Der Auftrag führte sie unter den erwarteten
Änderungsorten; sie steht auf den Laufmanifesten und wird von einer Artefaktauswahl
nicht berührt. Die 29 ungültigen Invocationen stehen in c14 wie in c13.

### 4.3 T10, die neue Tabelle — die gerechneten Aggregate

| Teiltabelle | Gruppe | nur Baseline | nur K2 / nur K3 | beide | keiner | **Nenner** | ausserhalb des Nenners |
|---|---|---|---|---|---|---|---|
| **T10a** `localized` | K2 gegen die Baselines | **1** | **0** | **19** | **0** | **20** | Baseline n.a. **8** · K2 n.a. **4** · beide n.a. **0** · nicht beurteilbar **0** |
| **T10a** `localized` | K3 gegen die Baselines | **0** | **0** | **20** | **0** | **20** | Baseline n.a. **8** · K3 n.a. **4** · beide n.a. **0** · nicht beurteilbar **0** |
| **T10b** `strict` | K2 gegen die Baselines | **2** | **3** | **14** | **1** | **20** | Baseline n.a. **8** · K2 n.a. **4** · beide n.a. **0** · nicht beurteilbar **0** |
| **T10b** `strict` | K3 gegen die Baselines | **0** | **4** | **16** | **0** | **20** | Baseline n.a. **8** · K3 n.a. **4** · beide n.a. **0** · nicht beurteilbar **0** |

**Die Probe geht in allen vier Gruppen auf:** 20 + 8 + 4 + 0 + 0 = **32**. Die
Nicht-ausdrückbar-Zahlen **8** und **4** sind die aus **T8** vorhersagbaren — 8 =
`FRAMEWORK_TYPE_IN_SIGNATURE` (4) + `SIGNATURE_DEVIATION` (4), wo K1, K4 und K5 sämtlich
` — ` tragen; 4 = `CYCLE_SIBLING` (3) + `CYCLE_PARENT_CHILD` (1), wo K2/K3 nach T8.1
` — ` tragen. **Sie stehen so in EXPECTED §16.5, vor dem Lauf gerechnet.** Keine
Injektion fällt in die Klasse `nicht beurteilbar`: nach R11 hat jede Injektion in jeder
Konfiguration einen gültigen Lauf.

**Die Zeilen ausserhalb von „beide", namentlich** — reine Aufzählung, ohne Deutung:

| Teiltabelle | Gruppe | Zustand | Injektionen |
|---|---|---|---|
| T10a | K2 | nur Baseline | I28 (`INCORRECT_LOCATION`, Baseline: K4) |
| T10b | K2 | nur Baseline | I17, I20 (`MISSING_PORT_REFERENCE`, Baseline: K5) |
| T10b | K2 | nur K2 | I25, I26, I27 (`INCORRECT_LOCATION`) |
| T10b | K2 | keiner | I28 (`INCORRECT_LOCATION`) |
| T10b | K3 | nur K3 | I25, I26, I27, I28 (`INCORRECT_LOCATION`) |

---

## 5 Ausdrücklich berichtet: die T1-Abweichungen

**Der Auftrag verlangt hier eine Zahl und einen Zellinhalt, ohne Deutung.**

### 5.1 c13 — zwei Abweichungen

```
| FRAMEWORK_TYPE_IN_SIGNATURE | … | 4/4 | 3/4 | **K3: Soll ja / Ist teilweise** |
| INCORRECT_LOCATION          | … | 3/4 | 4/4 | **K2: Soll ja / Ist teilweise** |
```

### 5.2 c14 — eine Abweichung

```
| FRAMEWORK_TYPE_IN_SIGNATURE | 4 | nein | nein | nein | ja | ` — ` | ` — ` | ` — ` | 4/4 | 4/4 |  |
| INCORRECT_LOCATION          | 4 | nein | teilweise | nein | ja | ` — ` | 4/4 | ` — ` | 3/4 | 4/4 | **K2: Soll ja / Ist teilweise** |
```

### 5.3 Die drei verlangten Auskünfte

1. **Bleibt die K3-Abweichung bestehen? NEIN — sie entfällt.** Die Zelle `Ist K3` der
   Zeile `FRAMEWORK_TYPE_IN_SIGNATURE` steht in c14 auf **`4/4`** statt **`3/4`**; die
   Zelle `Abweichung` ist **leer**, und leer heisst in dieser einen Spalte
   ausgewiesenermassen **„gerechnet, keine Abweichung"**. Die betroffene Injektion ist
   **I23**, deren `localized` und `strict` von **0** auf **1** gehen (§4.2, T4-Zeile
   I23).
2. **Tritt eine neue Abweichung auf? NEIN.** Die Abweichungsspalte trägt in c14 genau
   drei nichtleere Zellen: die beiden unveränderten Vermerke
   ``K4 `n. b.` (kein Vergleich bildbar)`` bei `CYCLE_SIBLING` und `CYCLE_PARENT_CHILD`
   — sie stehen zeichengleich schon in c13 — und die K2-Abweichung bei
   `INCORRECT_LOCATION`.
3. **Die K2-Abweichung bleibt bestehen**, zeichengleich: **`K2: Soll ja / Ist
   teilweise`**, `Ist K2` = **`3/4`**. Sie betrifft **I28** und ist von der
   Artefaktauswahl nicht berührt — K2 hat null Wiederholungen.

**Zahl der T1-Abweichungszeilen: c13 = 2, c14 = 1.** Mehr steht hier nicht; was daraus
folgt, gehört nach Befund 08.

---

## 6 Phase 4 — Index und Bündel

### 6.1 `data/campaign/eval/README.md` — neu

Tabelle aller vier Läufe mit Datum, Protokollrevision, Instrumenten-SHA, Ausgabepfad und
SHA256, dazu je ein Satz, **warum der nächste Lauf nötig wurde**. **Der kanonische Lauf
ist genau einer und namentlich benannt: `c14`.** Die drei früheren sind als **ÜBERHOLT,
ABER GÜLTIG ARCHIVIERT** gekennzeichnet — Beleg der Reparaturkette, nicht Ergebnis.
**Kein Lauf gelöscht, keine Datei nachbearbeitet.**

Die README steht selbst in `data/campaign/eval/SHA256SUMS`
(`6ae1d15b…34aa24b4`) — sie liegt in einem gehashten Bestand, und der Prüfer meldet
einen ungelisteten Pfad dort als **Fehlschlag**, nicht als Ausnahme. Der Nachzug gehört
damit in denselben Commit wie jede Fortschreibung; die Regel steht in der README selbst.

### 6.2 Bündler

`tools/bundle-docs.sh`: `data/campaign/eval/c13_eval_full.md` →
**`c14_eval_full.md`**, dazu neu **`data/campaign/eval/README.md`** — damit die eine
gebündelte Ausgabe nicht ohne ihre Herkunft dasteht. Der Warnhinweis im Skript ist auf
`c14 -> c15` fortgeschrieben.

**Bündel neu erzeugt**, auf sauberem Baum nach dem letzten Commit dieses Auftrags
(`Uncommittete Aenderungen: 0`): **109 Dateien**, rund **3,8 MB** (≈ 55 800 Zeilen) —
vorher **108** Dateien und rund **3,8 MB**. Hinzugekommen ist die README; getauscht ist
`c13_eval_full.md` gegen `c14_eval_full.md`. **Die exakte Byte- und Zeilenzahl hängt vom
Bytestand dieses Berichts ab, der selbst im Bündel liegt** — derselbe Selbstbezug wie
beim Protokoll-SHA; die Dateizahl **109** ist davon unberührt.

### 6.3 Kopfvermerk in `c11d_bericht_befund08_grundlagen.md`

Datierter Vermerk ergänzt: Teil A ruht auf `c13`; die **K3-Zahlen in A1, A3, A4, A5 und
A6 sind durch C14 überholt**, die K1/K2/K4/K5-Zahlen **nicht**; **A6b ist die Belegquelle
des Defekts** und bleibt tragend. **Der Bericht ist nicht umgeschrieben** — er ist der
Stand vor der Reparatur und als solcher Teil der Kette.

---

## 7 Endstand

**Vier Bäume porcelain leer, `git log --oneline -9`, Bündelzahlen und der letzte
Prüferlauf: siehe die Auftragsantwort dieses Laufs.** Kein `git push`; das Pushen bleibt
Handarbeit.

| Prüfung | Ergebnis |
|---|---|
| `python3 tools/check_doc_invariants.py` nach jedem Commit an Protokoll, Spezifikation, Instrumenten oder `data/` | **Exit 0** (Ausnahme: (E) planmäßig rot zwischen Commit 4 und Commit 5, §2.6) |
| `sha256sum -c data/campaign/eval/SHA256SUMS` | **9 von 9 OK** |
| `c11`, `c12`, `c13` | **unberührt** |
| `data/campaign/k1..k5`, `data/campaign/manifests`, `data/soll` | **unberührt** |
| Abbruchgrund „Änderung in einer K1-, K2-, K4- oder K5-Zelle" | **nicht eingetreten — 0 Zellen** |
