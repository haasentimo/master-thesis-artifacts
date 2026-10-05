# C11d — Zahlen und Belegstellen für Befund 08

**Masterarbeit Timo Haas · HTWG Konstanz**
Datum: 28. August 2026 · Auftrag **C11d** · Schreibendes Repo: `masterarbeit`;
`tritongraph`, `tritongraph-measure` und `ma-conformance-testrepo` **nur lesend**

**Commits dieses Auftrags:**

| # | SHA | Titel |
|---|---|---|
| 1 | `c4c5c22` | `feat: add a descriptive campaign summariser (not a registered instrument)` |
| 2 | *(dieser Bericht)* | `docs: compile the facts and citations for finding 08` |

> **KOPFVERMERK, ergänzt am 28.08.2026 durch Auftrag C14 — TEIL A DIESES BERICHTS RUHT
> AUF `c13`, UND `c13` IST ÜBERHOLT.** Alle Zahlen des Teils A sind aus
> `data/campaign/eval/c13_eval_full.json` gezogen (so dort ausgewiesen). Der vierte
> Auswertungslauf **`c14`** hat die Artefaktauswahl auf das Laufverdikt gestellt
> (Protokoll Rev. 44/45, Auswertungsspezifikation §1.9); **die K3-Zahlen in A1, A3, A4,
> A5 und A6 sind damit überholt** und durch die entsprechenden Zellen von
> `data/campaign/eval/c14_eval_full.md` zu ersetzen. **Nicht überholt sind die
> K1-, K2-, K4- und K5-Zahlen** — von 1952 Injektionszellen haben sich c13 → c14 genau
> **35** geändert, sämtlich in **K3** und sämtlich in den elf Injektionen aus **A6b**.
>
> **A6b ist die Belegquelle des Defekts** und bleibt damit gültig und tragend: die dortige
> Auszählung — welches Artefakt die Auswertung je Injektion gelesen hat und welches Verdikt
> dessen Laufmanifest trägt — ist der Nachweis, aus dem C14 die Reparatur begründet hat.
>
> **Dieser Bericht wird NICHT umgeschrieben.** Er ist der Stand vom 28.08.2026 vor der
> Reparatur und als solcher Beleg der Reparaturkette. Rechenweg und Gegenüberstellung
> stehen in `c14_bericht_vierter_lauf.md`, der Index der vier Läufe in
> `data/campaign/eval/README.md`.

> **Was dieser Bericht IST.** Eine Zusammenstellung: Zahlen mit Rechenweg, Zitate
> wörtlich, Fundstellen mit Datei und Zeile.
>
> **Was er NICHT ist.** Er schreibt **Befund 08 nicht**. Kein Eintrag in
> `befunde_log.md`, keine Formulierung von Setup, Resultat oder Konsequenz, keine
> Deutung, keine Bewertung, kein Vergleich zwischen Konfigurationen in Worten. Wo
> unten eine Zahl neben einer anderen steht, steht sie dort, weil die Tabelle sie
> nebeneinander führt — nicht als Aussage über ihr Verhältnis.
>
> **Was dieser Auftrag ausserdem nicht getan hat.** Kein vierter Auswertungslauf.
> Keine Änderung an den drei registrierten Instrumenten, an `data/campaign/k*`, an
> `data/soll/`, am Injektionsmanifest, am Prompt, am Schema, am Protokoll, an der
> Auswertungsspezifikation oder an den Tabellenskeletten. Kein C10-Abschlussbericht,
> kein Standdokument, keine offenen Punkte, kein Arbeitsplan, keine Gate-Notiz, kein
> Z1, keine Bündeländerung, keine Kapitelprosa. **Kein `git push`.** Keine Datei
> gelöscht, kein git-Verlauf berührt.

---

## 0 Vorbedingungen

| Prüfung | Erwartet | Befund |
|---|---|---|
| `masterarbeit` porcelain | leer | leer, HEAD `2c3e7ae` ✅ |
| `tritongraph` porcelain | leer | leer ✅ |
| `tritongraph-measure` porcelain | leer | leer ✅ |
| `ma-conformance-testrepo` porcelain | leer | leer ✅ |
| Runner aktiv? | nein | Prozessliste ohne Treffer (nur VSCode-Server-Prozesse) ✅ |
| `python3 tools/check_doc_invariants.py` | Exit 0 | **alle 5 Invarianten erfüllt**, Exit 0 ✅ |
| `sha256sum -c data/campaign/eval/SHA256SUMS` | 6 / 6 OK | **6 von 6 OK**, Exit 0 ✅ |

```
$ sha256sum -c data/campaign/eval/SHA256SUMS
data/campaign/eval/c11_eval_full.json: OK
data/campaign/eval/c11_eval_full.md: OK
data/campaign/eval/c12_eval_full.json: OK
data/campaign/eval/c12_eval_full.md: OK
data/campaign/eval/c13_eval_full.json: OK
data/campaign/eval/c13_eval_full.md: OK          → rc=0
```

`c11`, `c12` und `c13` sind über diesen Auftrag hinweg **unberührt**: nicht
überschrieben, nicht gelöscht, nicht nachbearbeitet. Der Prüfer lief nach dem ersten
Commit erneut mit **Exit 0**.

---

## 0.1 Das Werkzeug dieses Auftrags und seine Abgrenzung

Für die abgeleiteten Aggregate in Teil A ist ein **eigenes, klar getrenntes** Werkzeug
entstanden: [`tools/describe_campaign.py`](../../tools/describe_campaign.py),
SHA256 `d058e477e34826c5998979975834a107857a31cf3d26ad554eabf8238f89ca65`.

**Es ist kein Instrument.** Die Trennung ist nicht behauptet, sondern nachgewiesen:

| Eigenschaft | Zustand |
|---|---|
| in Protokoll §0.1 registriert | **nein** — und ausdrücklich nicht aufzunehmen |
| definiert eine Metrik | **nein** — jede Zahl ist entweder aus der archivierten Ausgabe übernommen oder eine **Zählung** über dort stehende Zahlen |
| schreibt eine Zelle, ein Artefakt, ein Manifest, ein `SHA256SUMS` | **nein** |
| berührt eine Invariante von `check_doc_invariants.py` | **nein** — der Prüfer läuft nach dem Commit des Werkzeugs mit **Exit 0**, Invariante (E) hasht die **drei** registrierten Werkzeuge und kennt dieses nicht |

**Jede Zahl aus Teil A ist ABGELEITET, DESKRIPTIV** und steht unten mit ihrem
Rechenweg. Die drei registrierten Instrumente (`evaluate_campaign.py`,
`match_k4k5.py`, `check_doc_invariants.py`) sind **nicht angefasst**; ihre SHA256
stehen unverändert auf dem in Protokoll Rev. 43 registrierten Stand.

### 0.1.1 Benannte Abweichung von der Quellenvorgabe des Auftrags

Der Auftrag gibt vor, das Werkzeug lese „ausschliesslich `data/campaign/eval/c13_eval_full.json`
und die archivierten Kampagnenartefakte". **Es liest eine dritte Datei:**
`data/soll/injection_manifest.json`.

**Grund, benannt statt verschwiegen.** Die in A4/A5 verlangte Zerlegung der
Falsch-Positiven nach `rule_id` setzt voraus, dass **entschieden werden kann, welcher
Record der Treffer ist**. Dafür braucht es den vorregistrierten
`expected_match_key`, dazu `carrier_component` (dritte Komponente des
`localized`-Tripels) und `injection_sha256` (Auflösung des Artefaktpfads). **Keine
dieser drei Angaben steht in der archivierten Ausgabe.** Sie anders herzuleiten
hiesse, eine **zweite Matching-Regel zu erfinden** — genau das, was der Auftrag
untersagt. Das Injektionsmanifest ist ein gehashter Messeingang aus §0.1
(`2744116e513c9e79e3174e6e3681abdcdc7c18f36d00b6d334875e4e918cfb1f`), wird hier
**nur gelesen** und nicht verändert.

### 0.1.2 Das Gatter, das die Zerlegung ehrlich hält

Die Zerlegung **wiederholt** die Klassifikation aus
`evaluate_campaign.evaluate_llm_injection` wörtlich und merkt sich die Records, die
dabei gezählt wurden. Sie erfindet keine Schwelle und entscheidet keinen Fall neu.
Danach gilt ein **hartes Gatter**:

> Für **alle 64** Paare (Konfiguration × Injektion) müssen `strict_fp` und
> `localized_fp` **nachgerechnet = archiviert** sein. Bei einer einzigen Abweichung
> bricht das Werkzeug mit Exit 2 ab und nennt das Paar.

**Ergebnis: 64 von 64.** Ausgabe wörtlich:

```
Gate: 64 von 64 Paaren: strict_fp und localized_fp nachgerechnet = archiviert
```

**Zweite, unabhängige Gegenprobe** — die Summen der Zerlegung gegen die
**gerechneten Nenner der T5-Zellen** derselben Ausgabe (`Nenner − TP`):

| Zelle in T5 (c13) | Nenner − TP | Summe der Zerlegung |
|---|---|---|
| K2 `FORBIDDEN_RELATION` `strict` 12/68 | 56 | **56** ✅ |
| K2 `ABSENCE_REQUIRED` `strict` 2/29 | 27 | **27** ✅ |
| K2 `FORBIDDEN_SIGNATURE_TYPE` `strict` 4/7 | 3 | **3** ✅ |
| K2 `STRUCTURAL_PLACEMENT` `strict` 3/6 | 3 | **3** ✅ |
| K2 `API_CONTRACT` `strict` 4/13 | 9 | **9** ✅ |
| K2 Gesamt UF3 `strict` 25/123 | 98 | **98** ✅ |
| K2 Gesamt UF3 `loc` 27/46 | 19 | **19** ✅ |
| K3 Gesamt UF3 `strict` 27/27 | 0 | **0** ✅ |
| K3 Gesamt UF3 `loc` 27/27 | 0 | **0** ✅ |

### 0.1.3 Die Auflösungsregel, unter der jede Zahl in A4–A6 steht

Welches Artefakt zu einer Injektion gelesen wird, entscheidet die **Regel des
Instruments** (`evaluate_campaign.campaign_artifact`): der Glob
`<cfg>_*<injection_sha256>.json`. Er trifft die Datei **ohne** `_r<n>`-Suffix, also
den **ersten Versuch**. Das steht hier, weil es zum Rechenweg gehört; die Folgen
davon sind in **A6b** ausgezählt und nicht bewertet.

---

# TEIL A — AGGREGATE AUS DER ARCHIVIERTEN AUSGABE

> **Alle Zahlen dieses Teils: ABGELEITET, DESKRIPTIV.**
> Quelle: `data/campaign/eval/c13_eval_full.json`
> (SHA256 `873893e771f3dd8a1a195b283f874858990dcd27a75a1c348fa85a1c1914977c`),
> die archivierten Kampagnenartefakte unter `data/campaign/k2/` und `data/campaign/k3/`,
> und `data/soll/injection_manifest.json`.
> Rechenweg je Abschnitt angegeben. Erzeugt mit
> `python3 tools/describe_campaign.py`, Exit 0.

## A1 — kein-EN, ausgezählt je Konfiguration

**Rechenweg.** Auszählung der Spalte `kein_en` der 32 T4-Zeilen je Konfiguration,
Zelle für Zelle aus `injections[<ID>].configs[<K>].kein_en` der archivierten Ausgabe.
**Es wird nichts neu gebildet** — der Wert der Zelle wird gezählt, nicht hergestellt.
Trägt die Zelle einen Marker, wird sie als **Markerzelle** gezählt und nicht als
Wert; die Ausgabe setzt kein-EN dort aus `strict` (`note: "aus 'strict' übernommen"`).

### A1.1 Gesamtzählung

| Klasse | K2 | K3 |
|---|---|---|
| `ja` | **22** | **2** |
| `nein` | **3** | **25** |
| `entfällt` | **3** | **1** |
| Marker ` — ` | **4** | **4** |
| **Summe** | **32** | **32** |

### A1.2 Injektions-IDs je Klasse, namentlich

**K2**

| Klasse | IDs |
|---|---|
| `ja` (22) | I01, I02, I03, I04, I05, I06, I07, I08, I09, I10, I11, I12, I18, I19, I21, I22, I23, I24, I29, I30, I31, I32 |
| `nein` (3) | I25, I26, I27 |
| `entfällt` (3) | I17, I20, I28 |
| Marker ` — ` (4) | I13, I14, I15, I16 |

**K3**

| Klasse | IDs |
|---|---|
| `ja` (2) | I30, I31 |
| `nein` (25) | I01, I02, I03, I04, I05, I06, I07, I08, I09, I10, I11, I12, I17, I18, I19, I20, I21, I22, I24, I25, I26, I27, I28, I29, I32 |
| `entfällt` (1) | I23 |
| Marker ` — ` (4) | I13, I14, I15, I16 |

### A1.3 Aufgeschlüsselt je Kategorie (Ebene 1)

| Kategorie (n) | K2 | K3 |
|---|---|---|
| `FORBIDDEN_RELATION` (12) | `ja` 12 — I01–I12 | `nein` 12 — I01–I12 |
| `CYCLE` (4) | Marker ` — ` 4 — I13–I16 | Marker ` — ` 4 — I13–I16 |
| `ABSENCE_REQUIRED` (4) | `ja` 2 — I18, I19 · `entfällt` 2 — I17, I20 | `nein` 4 — I17–I20 |
| `FORBIDDEN_SIGNATURE_TYPE` (4) | `ja` 4 — I21–I24 | `nein` 3 — I21, I22, I24 · `entfällt` 1 — I23 |
| `STRUCTURAL_PLACEMENT` (4) | `nein` 3 — I25, I26, I27 · `entfällt` 1 — I28 | `nein` 4 — I25–I28 |
| `API_CONTRACT` (4) | `ja` 4 — I29–I32 | `ja` 2 — I30, I31 · `nein` 2 — I29, I32 |

**Vorregistrierte Lesart der drei Werte, wörtlich aus der Ausgabe (T4-Kopfblock):**

> „**`ja`** = beides vorhanden (übersteigt nicht) · **`nein`** = `strict`-Treffer bei
> leerem Ruhezustand (übersteigt) · **`entfällt`** = kein `strict`-Treffer, die Frage
> stellt sich nicht — ein **gerechneter** Wert, **kein Marker**. Trägt `strict` einen
> Marker, trägt kein-EN denselben."

## A2 — SV (Schreibweisenverfehlung), ausgezählt

**Rechenweg.** Wie A1, über die Spalte `sv`. Diese Spalte trägt in der archivierten
Ausgabe **keinen Marker**; alle 64 Zellen sind Werte.

### A2.1 Gesamtzählung und IDs

| Klasse | K2 | K3 |
|---|---|---|
| `ja` | **2** — I17, I20 | **0** |
| `nein` | **30** | **32** |
| **Summe** | **32** | **32** |

### A2.2 Je Kategorie

| Kategorie (n) | K2 `ja` | K2 `nein` | K3 `ja` | K3 `nein` |
|---|---|---|---|---|
| `FORBIDDEN_RELATION` (12) | 0 | 12 | 0 | 12 |
| `CYCLE` (4) | 0 | 4 | 0 | 4 |
| `ABSENCE_REQUIRED` (4) | **2** — I17, I20 | 2 — I18, I19 | 0 | 4 |
| `FORBIDDEN_SIGNATURE_TYPE` (4) | 0 | 4 | 0 | 4 |
| `STRUCTURAL_PLACEMENT` (4) | 0 | 4 | 0 | 4 |
| `API_CONTRACT` (4) | 0 | 4 | 0 | 4 |

**Bildungsvorschrift, wörtlich aus der Ausgabe (T4-Spaltenbedeutung):**

> „**SV** = Schreibweisenverfehlung, mechanisch gebildet (`localized` Treffer **und**
> `strict` 0 **und** Abweichung allein in Segment 4)."

## A3 — Die Δ-Verteilung aus T4, je Konfiguration

**Rechenweg.** Auszählung der Spalte `delta` der 32 T4-Zeilen je Konfiguration, aus
`injections[<ID>].configs[<K>].delta`. **Getrennt von A1 geführt** — Δ steht nach der
Ausgabe auf dem **Median** von Ruhe und Kampagne, kein-EN auf der **Existenzstufe**;
das sind verschiedene Grössen und werden hier nicht ineinandergerechnet. Keine
Δ-Zelle trägt einen Marker.

| | K2 | K3 |
|---|---|---|
| Δ **> 0** | **5** | **26** |
| Δ **= 0** | **24** | **6** |
| Δ **< 0** | **3** | **0** |
| Marker | 0 | 0 |
| **Summe** | **32** | **32** |

**K2, IDs mit Wert**

| Klasse | IDs (Wert) |
|---|---|
| Δ > 0 (5) | I10 (+1), I12 (+1), I25 (+1), I26 (+1), I27 (+1) |
| Δ = 0 (24) | I01, I02, I03, I04, I05, I06, I07, I09, I11, I13, I14, I15, I16, I17, I18, I19, I20, I21, I24, I28, I29, I30, I31, I32 |
| Δ < 0 (3) | I08 (−1), I22 (−4), I23 (−3) |

**K3, IDs mit Wert**

| Klasse | IDs (Wert) |
|---|---|
| Δ > 0 (26) | I01, I02, I03, I04, I05, I07, I08, I09, I10, I11, I12, I13, I14, I15, I17, I18, I19, I22, I24, I25, I26, I27, I28, I29, I30, I32 — **jede mit +1** |
| Δ = 0 (6) | I06, I16, I20, I21, I23, I31 |
| Δ < 0 (0) | *(keine)* |

**Wertehistogramm.** K2: −4 ×1 · −3 ×1 · −1 ×1 · 0 ×24 · +1 ×5.
K3: 0 ×6 · +1 ×26.

## A4 — Zusammensetzung der `strict`-Falsch-Positiven

**Rechenweg.** Die Gesamtzahl je Zelle ist **Nenner − TP** der `strict`-Precision aus
T5 der archivierten Ausgabe; die Zerlegung entsteht durch Wiederholung der
Klassifikation und Attribution der dabei gezählten Records nach ihrem `rule_id` und
ihrer `category` (Ebene 1 des **gemeldeten** Records, nicht der Injektion). **Die
Zähleinheit ist der Record** — `strict` dedupliziert nicht (Spez. §3.2). Gatter und
Gegenprobe: §0.1.2.

### A4.1 K2 — 98 Falsch-Positive gesamt

**Nach `rule_id`** (Summe 98):

| `rule_id` | Anzahl |
|---|---|
| `R-LAYER-1` | 24 |
| `R-PLACE-1` | 18 |
| `R-INDEP-1` | 17 |
| `R-PROTECT-1` | 16 |
| `R-CYCLE-1` | 6 |
| `R-CYCLE-2` | 6 |
| `R-SIG-1` | 3 |
| `R-PORT-1` | 3 |
| `R-PORT-4` | 3 |
| `R-PORT-3` | 2 |
| **Summe** | **98** |

**Nach `category_l1` des gemeldeten Records** (Summe 98):

| Kategorie des Records | Anzahl |
|---|---|
| `FORBIDDEN_RELATION` | 57 |
| `STRUCTURAL_PLACEMENT` | 18 |
| `CYCLE` | 12 |
| `ABSENCE_REQUIRED` | 8 |
| `API_CONTRACT` | 3 |
| **Summe** | **98** |

**Je Kategorie der Injektion:**

| Kategorie der Injektion | FP | nach `rule_id` | nach Kategorie des Records |
|---|---|---|---|
| `FORBIDDEN_RELATION` | **56** | `R-PLACE-1` 12 · `R-PROTECT-1` 12 · `R-INDEP-1` 11 · `R-CYCLE-1` 6 · `R-CYCLE-2` 6 · `R-LAYER-1` 6 · `R-SIG-1` 3 | `FORBIDDEN_RELATION` 29 · `STRUCTURAL_PLACEMENT` 12 · `CYCLE` 12 · `API_CONTRACT` 3 |
| `CYCLE` | **0** | *(keine)* | *(keine)* |
| `ABSENCE_REQUIRED` | **27** | `R-LAYER-1` 12 · `R-PROTECT-1` 4 · `R-PORT-1` 3 · `R-INDEP-1` 3 · `R-PORT-4` 3 · `R-PORT-3` 2 | `FORBIDDEN_RELATION` 19 · `ABSENCE_REQUIRED` 8 |
| `FORBIDDEN_SIGNATURE_TYPE` | **3** | `R-INDEP-1` 3 | `FORBIDDEN_RELATION` 3 |
| `STRUCTURAL_PLACEMENT` | **3** | `R-LAYER-1` 3 | `FORBIDDEN_RELATION` 3 |
| `API_CONTRACT` | **9** | `R-PLACE-1` 6 · `R-LAYER-1` 3 | `STRUCTURAL_PLACEMENT` 6 · `FORBIDDEN_RELATION` 3 |
| **Summe** | **98** | | |

**Je Injektion (K2), zur Nachprüfbarkeit der Kategoriesummen:**

| ID | `strict` FP | ID | `strict` FP | ID | `strict` FP | ID | `strict` FP |
|---|---|---|---|---|---|---|---|
| I01 | 6 | I09 | 6 | I17 | 6 | I25 | 0 |
| I02 | 3 | I10 | 9 | I18 | 3 | I26 | 0 |
| I03 | 3 | I11 | 6 | I19 | 6 | I27 | 3 |
| I04 | 3 | I12 | 5 | I20 | 12 | I28 | 0 |
| I05 | 3 | I13 | 0 | I21 | 0 | I29 | 3 |
| I06 | 3 | I14 | 0 | I22 | 0 | I30 | 3 |
| I07 | 3 | I15 | 0 | I23 | 0 | I31 | 3 |
| I08 | 6 | I16 | 0 | I24 | 3 | I32 | 0 |

### A4.2 K3 — 0 Falsch-Positive gesamt

Über **alle sechs Kategorien** und **alle 32 Injektionen** ist die Zahl **0**. Es gibt
folglich keine Verteilung nach `rule_id` und keine nach Kategorie des Records; die
Gegenprobe gegen T5 (`27/27`, Nenner − TP = 0) stimmt.

## A5 — Zusammensetzung der `localized`-Falsch-Positiven, getrennt geführt

**Rechenweg.** Gesamtzahl je Zelle = Nenner − TP der `localized`-Precision aus T5.
**Die Zähleinheit ist hier das Tripel** `(component, module, category)`, nicht der
Record — `localized` dedupliziert (Spez. §7.3). Daraus folgt für die
`rule_id`-Spalte eine **benannte Unschärfe**: gezählt wird, in wie vielen **Tripeln**
ein `rule_id` vorkommt; ein Tripel, das von Records zweier verschiedener Regeln
getragen wird, erscheint unter beiden. **Die `rule_id`-Spalte summiert deshalb auf
mindestens die Gesamtzahl, nicht auf genau sie.** Die Spalte „Kategorie des Records"
ist dagegen exakt: sie ist das dritte Segment des Tripels und je Tripel eindeutig.

### A5.1 K2 — 19 Falsch-Positive gesamt

**Nach `rule_id`** (Tripel je Regel; Summe 22 ≥ 19, siehe Unschärfe oben):

| `rule_id` | Tripel |
|---|---|
| `R-PLACE-1` | 6 |
| `R-LAYER-1` | 6 |
| `R-CYCLE-1` | 2 |
| `R-CYCLE-2` | 2 |
| `R-PROTECT-1` | 2 |
| `R-INDEP-1` | 2 |
| `R-SIG-1` | 1 |
| `R-SIG-4` | 1 |

**Nach Kategorie des Tripels** (Summe 19, exakt):

| Kategorie | Anzahl |
|---|---|
| `FORBIDDEN_RELATION` | 7 |
| `STRUCTURAL_PLACEMENT` | 6 |
| `CYCLE` | 4 |
| `API_CONTRACT` | 2 |
| **Summe** | **19** |

**Je Kategorie der Injektion:**

| Kategorie der Injektion | FP | nach `rule_id` (Tripel) | nach Kategorie des Tripels |
|---|---|---|---|
| `FORBIDDEN_RELATION` | **9** | `R-PLACE-1` 4 · `R-CYCLE-1` 2 · `R-CYCLE-2` 2 · `R-SIG-1` 1 | `STRUCTURAL_PLACEMENT` 4 · `CYCLE` 4 · `API_CONTRACT` 1 |
| `CYCLE` | **1** | `R-SIG-4` 1 | `API_CONTRACT` 1 |
| `ABSENCE_REQUIRED` | **4** | `R-LAYER-1` 4 · `R-PROTECT-1` 2 · `R-INDEP-1` 1 | `FORBIDDEN_RELATION` 4 |
| `FORBIDDEN_SIGNATURE_TYPE` | **1** | `R-INDEP-1` 1 | `FORBIDDEN_RELATION` 1 |
| `STRUCTURAL_PLACEMENT` | **1** | `R-LAYER-1` 1 | `FORBIDDEN_RELATION` 1 |
| `API_CONTRACT` | **3** | `R-PLACE-1` 2 · `R-LAYER-1` 1 | `STRUCTURAL_PLACEMENT` 2 · `FORBIDDEN_RELATION` 1 |
| **Summe** | **19** | | |

**Je Injektion (K2):** I01 2 · I02 1 · I03 1 · I04 1 · I05 1 · I06 0 · I07 0 ·
I08 1 · I09 0 · I10 1 · I11 0 · I12 1 · I13 0 · I14 1 · I15 0 · I16 0 · I17 1 ·
I18 1 · I19 1 · I20 1 · I21 0 · I22 0 · I23 0 · I24 1 · I25 0 · I26 0 · I27 1 ·
I28 0 · I29 1 · I30 1 · I31 1 · I32 0.

### A5.2 K3 — 0 Falsch-Positive gesamt

Über alle sechs Kategorien und alle 32 Injektionen **0**; Gegenprobe gegen T5
(`27/27`) stimmt.

## A6 — Die zwei T1-Abweichungen im Einzelnen

**Die Abweichungszeilen der Ausgabe, wörtlich (T1, c13):**

> `| FRAMEWORK_TYPE_IN_SIGNATURE | 4 | nein | nein | nein | ja | ` — ` | ` — ` | ` — ` | 4/4 | 3/4 | **K3: Soll ja / Ist teilweise** |`
> `| INCORRECT_LOCATION | 4 | nein | teilweise | nein | ja | ` — ` | 4/4 | ` — ` | 3/4 | 4/4 | **K2: Soll ja / Ist teilweise** |`

**Rechenweg der Zuordnung „welche Injektion fehlt".** Gesucht ist je Konfiguration
die Injektion, deren archivierte Zellen `strict` **und** `localized` beide **0** sind
und keinen Marker tragen. Über alle 64 Paare gibt es **genau zwei**:

| Konfiguration | Injektion | Szenario (Ebene 2) | Kategorie (Ebene 1) | Trägermodul |
|---|---|---|---|---|
| **K3** | **I23** | `FRAMEWORK_TYPE_IN_SIGNATURE` | `FORBIDDEN_SIGNATURE_TYPE` | `depot.orders.models.order_line_models` |
| **K2** | **I28** | `INCORRECT_LOCATION` | `STRUCTURAL_PLACEMENT` | `depot.billing.legacy_tax_models` |

Das deckt sich mit den T4-Zeilen der Ausgabe: K3/I23 trägt `strict` 0, `loc` 0,
`kein-EN entfällt`, Läufe `[0,0,0] · [0,0,0]`; K2/I28 trägt `strict` 0, `loc` 0,
`kein-EN entfällt`, Läufe `[0,0,0] · [0,0,0]`.

### A6.1 Was in den Läufen dieser beiden Injektionen stattdessen gemeldet wurde

**K3 / I23** — vorregistrierter Schlüssel
`FORBIDDEN_SIGNATURE_TYPE|orders_models|depot.orders.models.order_line_models|sqlalchemy.orm.Session`
Gelesenes Artefakt: `data/campaign/k3/k3_28a75749496229bb1db37d85f68347572bd84c49.json`

| Repetition | Records (`rule_id` · `category` · `module`) |
|---|---|
| 0 | *(keiner)* |
| 1 | *(keiner)* |
| 2 | *(keiner)* |

**K2 / I28** — vorregistrierter Schlüssel
`STRUCTURAL_PLACEMENT|billing_models|depot.billing.legacy_tax_models|depot.billing.legacy_tax_models`
Gelesenes Artefakt: `data/campaign/k2/k2_72dc7461f9ecb5cdd53293f1f94d7418e98a3401.json`

| Repetition | Records (`rule_id` · `category` · `module`) |
|---|---|
| 0 | *(keiner)* |
| 1 | *(keiner)* |
| 2 | *(keiner)* |

**In beiden Fällen ist die Antwort auf „was wurde stattdessen gemeldet": nichts.**
In keiner der je drei Repetitionen des gelesenen Artefakts steht ein einziger Record
— weder ein LLM-Record noch ein `DERIVED:`-Record, weder am Trägermodul noch
anderswo.

**Der `validity`-Block der beiden Artefakte, wörtlich aus der Datei:**

| Artefakt | `calls_total` | `calls_invalid` | `calls_transport_failed` | `invalid_reasons` | `exit_code` |
|---|---|---|---|---|---|
| `k2_72dc7461….json` (I28) | 3 | 0 | **0** | `[]` | 0 |
| `k3_28a75749….json` (I23) | 3 | 0 | **3** | `['transport_failure']` | 3 |

### A6b — Welches Artefakt die Auswertung je Injektion gelesen hat

**Rechenweg.** Für jede der 32 Injektionen und beide LLM-Konfigurationen: Auflösung
des Artefakts mit der Regel des Instruments (§0.1.3), dann Nachschlagen des Verdikts
im **gehashten Laufmanifest** gleichen Namens unter `data/campaign/manifests/`
(`postrun.verdict` — die nach Protokoll Rev. 39 registrierte T7-Quelle). Reine
Zählung.

| Konfiguration | Injektionen mit `_r<n>`-Wiederholungen | gelesenes Artefakt trägt Verdikt **≠ VALID** |
|---|---|---|
| K2 | **0** | **0** |
| K3 | **11** | **11** — I05, I06, I07, I09, I11, I13, I16, I20, I21, I22, I23 |

**Die elf K3-Injektionen im Einzelnen** (`<==` markiert das von der Auswertung
gelesene Artefakt):

| Injektion | Versuche und Verdikte |
|---|---|
| I05 | 1 INVALID `<==` · 2 INVALID · 3 **VALID** |
| I06 | 1 INVALID `<==` · 2 INVALID · 3 **VALID** |
| I07 | 1 INVALID `<==` · 2 INVALID · 3 **VALID** |
| I09 | 1 INVALID `<==` · 2 INVALID · 3 INVALID · 4 INVALID · 5 **VALID** |
| I11 | 1 INVALID `<==` · 2 INVALID · 3 INVALID · 4 INVALID · 5 INVALID · 6 **VALID** |
| I13 | 1 INVALID `<==` · 2 INVALID · 3 **VALID** |
| I16 | 1 INVALID `<==` · 2 INVALID · 3 **VALID** |
| I20 | 1 INVALID `<==` · 2 INVALID · 3 **VALID** |
| I21 | 1 INVALID `<==` · 2 INVALID · 3 **VALID** |
| I22 | 1 INVALID `<==` · 2 **VALID** |
| I23 | 1 INVALID `<==` · 2 INVALID · 3 INVALID · 4 INVALID · 5 INVALID · 6 **VALID** |

**Rein deskriptiv festgehalten, ohne Deutung und ohne Reparatur:** die
Auflösungsregel des Instruments trifft in diesen elf Fällen den ersten Versuch; das
Laufmanifest desselben Namens trägt dort das Verdikt `INVALID` mit dem Grund
`transport_failure`. Die Zahl der Records im gelesenen Artefakt ist je Injektion:
I05 3 · I06 2 · I07 3 · I09 3 · I11 3 · I13 3 · I16 1 · I20 1 · I21 1 · I22 2 ·
**I23 0**. **Kein vierter Auswertungslauf ist Gegenstand dieses Auftrags**, kein
Instrument wurde geändert, keine Zelle angefasst.

---

# TEIL B — ZITATE UND FUNDSTELLEN, WÖRTLICH

## B1 — Die registrierte Evidenzstufe für Z3

**Vorbemerkung zur Fundstelle.** Der Auftrag verweist auf
`00_stand_und_entscheidungen.md` **§6 (Drei Evidenzstufen)**. **§6 jener Datei heisst
„Protokoll-Stand & Freeze"** und führt keine Evidenzstufen. Die Stufung steht dort in
**§5 Methodik** und in **§4** (Z3-Zeile); die Tabelle „Drei Evidenzstufen" steht in
`docs/planung/methodik_begruendung.md` **§6**. Alle drei Stellen wörtlich:

**(1) `docs/00_stand_und_entscheidungen.md` §5 Methodik, Zeilen 260–264:**

> „**Rahmen: Design Science Research** (Hevner; Prozessmodell Peffers et al.),
> mit drei eingebetteten empirischen Methoden unterschiedlicher, explizit
> benannter Evidenzstärke: **kontrolliertes Experiment (Z1, Z3) > explorative
> klassifizierende Studie (Z2) > Demonstration (Z4)**. Die Stufen dürfen
> sprachlich nie gleichgezogen werden."

**(2) `docs/00_stand_und_entscheidungen.md` §4 Ziele Z1–Z4, Zeile 244:**

> „- **Z3** Phase-04-Evaluation nach `eval_protokoll_phase04.md` → **Befund 08**."

Dazu, Zeilen 253–254 derselben Datei (Befund-Nummerierung):

> „**Befund-Nummerierung (verbindlich):** 01–05 Extraktion · **06** Provider-Smoke-Test
> und `subject`-Schema · **07** Z1 · **08** Z3 · **09** Z2."

**(3) `docs/planung/methodik_begruendung.md` §6, Zeilen 155–164:**

> „## 6. Drei Evidenzstufen — die zentrale Designeigenschaft
>
> Die Arbeit berichtet Ergebnisse **explizit unterschiedlicher Beweiskraft**. Diese
> Asymmetrie wird in Kapitel 4.1 benannt, nicht in Fußnoten versteckt:
>
> | Stufe | Methode | Gilt für | Was daraus folgt |
> |---|---|---|---|
> | stark | kontrolliertes Experiment, vorregistriert, mit Baselines und Ground Truth | Z1, Z3 | quantitative Aussagen mit Fehlerdiskussion |
> | mittel | explorative klassifizierende Studie, vorregistrierte Kriterien, Einzelrater | Z2 | Klassifikation und Tendenz, keine Signifikanzaussage |
> | schwach | Demonstration, keine Kontrolle, keine Ground Truth | Z4 | Existenz-/Machbarkeitsaussage, Scheitern ebenfalls berichtbar |"

**(4) Aus der Kapitelskizze `docs/kapitel/kapitel_skelette.md` §4.1, Zeilen 63–68:**

> „**4.1 Forschungsdesign im Überblick**
> - Kernaussage: Die Arbeit folgt Design Science Research (Peffers-Prozessmodell) mit drei
>   eingebetteten empirischen Methoden **explizit unterschiedlicher Evidenzstärke**:
>   kontrolliertes Experiment (Z1, Z3) > explorative klassifizierende Studie (Z2) >
>   Demonstration (Z4)."

**(5) Dieselbe Datei, §4.3, Zeilen 82–87:**

> „**4.3 Evaluationsdesign Z1/Z3 (kontrollierte Experimente)**
> - Kernaussage: Beide Experimente sind vorregistriert (Erwartungen, Matching, Stop-Regeln vor
>   der Messung fixiert); Z1 vergleicht Ableitungswege gold-frei auf identischer Faktenbasis,
>   Z3 misst Erkennungsleistung auf einem synthetischen, kontaminationsfreien Testrepo mit
>   injizierter Ground Truth gegen statische Baselines."

**(6) `docs/kapitel/kapitel1_entwurfsgrundlage.md`, Zeile 151:**

> „- Die drei Evidenzstufen (Experiment > Exploration > Demonstration) schon in Kapitel 1
>   ankündigen — sie sind Systemeigenschaft des Designs (Methodik 4.1), keine Fußnote."

## B2 — Der Reservierungsvermerk im Befunde-Log und die Reihenfolge 08 vor 07

**Der Vermerk, wörtlich — `docs/befunde_log.md` Zeilen 762–764, ein HTML-Kommentar am
Dateiende:**

> ```
> <!-- Nächster Eintrag: Befund 07 (Z1 — Head-to-Head Triton vs. LLM-Abstraktion) — oben unter dem Titel einfügen.
>      Nummerierung ist projektweit fortlaufend und repo-unabhängig: Befunde 01–05 stammen aus dem
>      Extractor-Repo, Befund 06 aus tritongraph. Nummern werden nicht reserviert. -->
> ```

**Der Kopf des Logs, wörtlich — Zeilen 3–5:**

> „> Laufendes Protokoll empirischer Befunde und der daraus folgenden methodischen Entscheidungen.
> > Neueste Einträge oben. Jeder Eintrag: Setup → Befund → methodische Konsequenz → Bezug zu Forschungsfragen.
> > Quelle für Zwischenbericht, Methodik- und Evaluationskapitel."

**Feststellung zur Reihenfolge, sachlich.**

1. **Z1 ist nicht gelaufen.** Befund 07 ist Z1 zugeordnet
   (`00_stand_und_entscheidungen.md` §4, Zeile 236 f.: „**Z1** Extraktionsvergleich,
   gold-frei, geloggter Lauf → **Befund 07** (4.4-Lücke: Rechnung existiert als Tests
   in `test_reader.py`, fehlt als zitierbarer Lauf + Fixture-Provenienz;
   Voraussetzung D1)"). Im Log steht als jüngster Eintrag **Befund 06**; ein Eintrag
   07 existiert nicht.
2. **Die Nummernvergabe ist fest, nicht laufend.** `00_stand_und_entscheidungen.md`
   §4 Zeilen 253–254 binden die Nummer an das **Ziel**, nicht an die Reihenfolge des
   Entstehens: „07 Z1 · **08** Z3 · 09 Z2". Befund 08 kann daher vor Befund 07
   entstehen, ohne dass eine Nummer wandert.
3. **Wie das Log den Fall handhabt — und wo es sich reibt.** Das Log ordnet
   **„Neueste Einträge oben"** an; die Nummern sind aber **fest vergeben**. Ein
   Befund 08, der vor Befund 07 geschrieben wird, steht damit **über** dem künftigen
   Befund 07 und die Nummernfolge im Dokument liest sich von oben nach unten als
   08 → 06 → 05 …, mit einer Lücke bei 07. **Der Vermerk am Dateiende sagt „Nummern
   werden nicht reserviert"** und weist zugleich Befund 07 als „nächsten Eintrag" aus
   — die beiden Sätze sind unter der Reihenfolge 08-vor-07 nicht beide gleichzeitig
   erfüllbar, ohne dass einer von ihnen fortgeschrieben wird. **Hier festgestellt,
   nicht entschieden** und nicht geändert.

## B3 — Die fünf Entscheidungs- und Stopregeln aus §7, und ob sie gegriffen haben

**Fundstelle: `docs/protokolle/eval_protokoll_phase04.md` §7, Zeilen 4298–4316.**
Wortlaut vollständig, danach je Regel die Feststellung mit Belegstelle.

### B3.1 Eine-Iteration-Regel — Zeilen 4300–4301

> „- **Eine-Iteration-Regel:** kein Prompt-Tuning nach Sichtung von Evaluationsdaten
>   (Fortsetzung der Disziplin aus Befund 04, Konsequenz 1)."

**Feststellung: GEHALTEN.** Belegstellen:

- Protokoll §10 Amendments, Zeile **Rev. 35**, zum verworfenen K2-Teilbestand:
  „**Die Eine-Iteration-Regel (§7) galt durchgehend: an dem Teilbestand wurde keine
  Metrik berechnet und kein Finding beurteilt**."
- `data/campaign/k3/MANIFEST.md`, Abschnitt „Verlauf der Wiederholungen (§7)":
  „**Kein Werkzeug wurde geändert.** Retry-Budget, Pacing und Runner stehen
  unverändert auf dem in §0.1 registrierten Stand (`4caf083`); §7 registriert den
  **Neustart**, nicht die Änderung des Werkzeugs. Der einzige bewegte Parameter ist
  das **Zeitfenster**."
- Die drei Auswertungsberichte C11, C11a, C11b, C11c tragen je eine
  **Deutungssperre** und halten fest, dass Prompt, Schema, Regeldatei und Manifest
  nicht berührt wurden (z. B. `c11c_bericht_dritter_lauf.md` Zeilen 22–29).

### B3.2 Validitäts-Gate — Zeilen 4302–4306

> „- **Validitäts-Gate:** liegt `valid_final` einer LLM-Konfiguration unter 0.9, wird das als
>   Befund dokumentiert und die Konfiguration mit den vorhandenen validen Läufen ausgewertet —
>   nicht nachgebessert. Operationalisierung: `valid_final=false`-Läufe sind über Exit-Code 3
>   bzw. das persistierte Run-Log (CLI-Inkremente 2 und 4) identifizierbar; stille Zählung
>   invalider Läufe als „0 Findings" ist damit ausgeschlossen."

**Feststellung: NICHT GEGRIFFEN.** Belegstelle: T7.1 der archivierten Ausgabe
(`c13_eval_full.md`), Zeilen der Tabelle und der Satz darunter:

> „| K2 | 32 | 32 | 0 | 96 | 0 | 0 | 96 / 96 = 1,000 | 0 | *(keine)* | 0 |"
> „| K3 | 61 | 32 | 29 | 183 | 0 | 50 | 133 / 133 = 1,000 | 0 | `transport_failure` ×29 | 29 |"
> „**Validitäts-Gate §7:** kein `valid_final`-Anteil unter 0,9."

Beide Anteile stehen auf **1,000**; die Schwelle 0,9 ist nicht berührt.

### B3.3 API-Fehler-Regel — Zeilen 4307–4308

> „- **API-Fehler** (Timeout, 429): betroffenen Call wiederholen, im Log kennzeichnen;
>   systematischer Ausfall → Lauf abbrechen, neu starten, beides protokollieren."

**Feststellung: GEGRIFFEN, in beiden Hälften.** Belegstellen:

- **Wiederholen und kennzeichnen:** T7.4 der archivierten Ausgabe führt **29 ungültige
  K3-Invocationen** einzeln auf, jede mit `invalid_reasons = transport_failure` und
  je `calls_total / calls_invalid / calls_transport_failed`; T7.1 weist
  `transport_failure` ×29 und **29 Wiederholungen (`_r<n>`)** aus.
- **Abbrechen und neu starten:** `data/campaign/k3/MANIFEST.md`: „Versuch 2 (27.08.,
  12:00 CEST) rettete **eine** von elf; der Block wurde angehalten. … Versuch 4 über
  die verbleibenden drei scheiterte **hart** … Neun aufeinanderfolgende gescheiterte
  Calls, weit über dem Richtwert von fünf: erneut **angehalten**." Und: „**C10d
  (28.08., 08:51–09:32 CEST) schloss den Block mit EINZELAUFRUFEN und Pausen.**"
- **Beides protokolliert:** ebd., Tabellen „Verlauf der Wiederholungen (§7)" und die
  Fünf-Zeilen-Tabelle der C10d-Aufrufe; dazu **194** `http_429`-Ereignisse im
  Abschnitt „Gültigkeit".

### B3.4 Erwartungsmatrix-Widerspruch — Zeilen 4309–4310

> „- **Ergebnis widerspricht Erwartungsmatrix:** dokumentieren und diskutieren. Die Matrix wird
>   nicht rückwirkend angepasst."

**Feststellung: GEGRIFFEN.** Belegstellen:

- Die **zwei** Abweichungen in T1 der archivierten Ausgabe (Wortlaut in **A6**):
  `FRAMEWORK_TYPE_IN_SIGNATURE` / K3 „**K3: Soll ja / Ist teilweise**" und
  `INCORRECT_LOCATION` / K2 „**K2: Soll ja / Ist teilweise**".
- Der Ausweisungsvermerk unter T1, wörtlich: „**Abweichungen werden AUSGEWIESEN,
  nicht aufgelöst** — die Soll-Spalten reproduzieren Protokoll §3 und werden hier
  nicht neu entschieden (Protokoll §7)."
- Die Matrix selbst ist unbewegt: die beiden Zellen stehen seit Rev. 21 bzw. seit der
  Ersetzung vom 12.08.2026 unverändert auf **`ja`** (Wortlaut in **B6**); Protokoll
  §3 Schlusssatz: „Abweichung der Messung von dieser Matrix ist ein Befund, kein
  Anlass zum Nachjustieren."

### B3.5 Scope-Gate — Zeilen 4311–4316

> „- **Scope-Gate (Variante C → A, festgelegt 18.07.):** Stichtag **31.08.2026**. Sind die
>   K1–K5-Läufe abgeschlossen und ausgewertet (oder Verzug ≤ 1 Woche), bleibt Variante C
>   (Z2-Regelableitungsstudie nach `z2_protokoll_regelableitung.md` wird ausgeführt). Andernfalls
>   automatischer Rückfall auf Variante A — ohne neue Diskussion; die Z2-Studie wandert nach
>   Future Work, der Kapitel-1-Präzisierungsabschnitt adressiert die Titellücke aktiv.
>   Kürzungsreihenfolge bei Verzug: zuerst Z4 (Transfer-Demonstration), dann erst Z2."

**Feststellung: SEPARAT — die Regel ist am Berichtsdatum weder gegriffen noch
verfallen.** Faktenlage, ohne Bewertung und ohne Entscheidung:

| Tatsache | Wert | Beleg |
|---|---|---|
| Stichtag | **31.08.2026** | §7 Zeile 4311 |
| Berichtsdatum | 28.08.2026 | dieser Bericht |
| K1–K5-Läufe abgeschlossen | ja, **32 von 32 je Konfiguration** | T7.1/T7.3 der Ausgabe; `data/campaign/k3/MANIFEST.md`: „abgeschlossen am 28.08.2026 (C10d)" |
| ausgewertet | ja, **drei Auswertungsläufe**, jüngster 28.08.2026 16:17 CEST | Teil **C4** |
| Gate-Notiz im Repo | **existiert nicht** | Volltextsuche über `docs/`: nur Erwähnungen in Nicht-Gegenstand-Listen der Berichte C6b, C6c, C6c-a, C6c-b, C11, C11a, C11b, C11c |

Die Gate-Entscheidung ist **nicht Gegenstand dieses Auftrags** und wird hier nicht
getroffen.

## B4 — §8, UF3 und UF4 wörtlich

**Fundstelle: `docs/protokolle/eval_protokoll_phase04.md` §8, ab Zeile 4329.**

### B4.1 Der UF3-Kopf — Zeilen 4336–4340

> „- **UF3:** Overlap-Analyse K1/K4/K5 vs. K2/K3, P/R/F1 pro Kategorie; Kategorie-Ausfälle und
>   Falsche-Regel-Fälle aus §4 als Fähigkeitsprofil des LLM-Pfads. Framing: Für die
>   **Kantenkategorien** gilt der Non-Inferiority-Vergleich. Bei den übrigen Kategorien ist die
>   Lage nach den Messungen aus B9+ **kategorienspezifisch** und nicht mehr entlang
>   „strukturell gegen semantisch" zu beschreiben:"

### B4.2 Die echten Nullzeilen in ihrer AKTUELLEN Fassung — Zeilen 4341–4354

Wörtlich, **mit den Streichungen als Streichungen**:

> „  - **Echte Nullzeile** und damit Ausdrucksmächtigkeits-Feststellung, kein Messbefund:
>     ~~`CYCLE` bei K5,~~ `SIGNATURE_DEVIATION` bei K4 und K5, `MISSING_PORT_REFERENCE` bei K4,
>     `INCORRECT_LOCATION` bei K5, **und `FRAMEWORK_TYPE_IN_SIGNATURE` bei K4 und K5**.
>     **Ergänzt Rev. 22 (B40), Nachzug zu Rev. 20:** beide Werkzeuge werten ausschließlich
>     Importkanten, und die Injektion lässt die Importmenge unverändert — vor und nach der
>     Injektion sehen K4 und K5 dasselbe (Fußnote 4). Ein **Import-Proxy** als Ersatz käme nicht in
>     Frage: er widerspräche **R-FRAMEWORK-1**, das den Import ausdrücklich erlaubt (§3 Amendment
>     (d)), und erzeugte auf der **sauberen** Baseline **acht Findings** — vier Träger und vier
>     Zwillinge, je Werkzeug (K4: `c2b_bericht_k4_konfiguration.md` §B6; K5:
>     `c2c_bericht_k5_konfiguration.md` §B6) —, während C3 über alle fünf Konfigurationen **null**
>     fordert. Damit ist `FORBIDDEN_SIGNATURE_TYPE` die **einzige** Kategorie, in der allein K2/K3
>     etwas finden können: strukturelle Nicht-Abdeckung beider Baselines, kein Werkzeugversagen.
>     **`CYCLE` bei K5 ist mit Rev. 22 (B39) aus dieser Aufzählung genommen** — siehe die eigene
>     Zeile unten."

**Die aktuelle Aufzählung besteht damit aus vier Einträgen** (die gestrichene
`CYCLE`/K5-Zeile ist nicht mitgezählt): `SIGNATURE_DEVIATION` bei K4 und K5 ·
`MISSING_PORT_REFERENCE` bei K4 · `INCORRECT_LOCATION` bei K5 ·
`FRAMEWORK_TYPE_IN_SIGNATURE` bei K4 und K5.

**Die zurückgezogene Zeile, wörtlich mitgeführt — Zeilen 4355–4361:**

> „  - ~~**Kein** Nullzeilen-Fall, sondern **messbarer False Positive**:
>     `FRAMEWORK_TYPE_IN_SIGNATURE` bei K4 und K5 — beide melden das konforme Zwillingsmodul
>     mit, weil sie nur den Import sehen.~~ **Mit Rev. 20 zurückgezogen** (Fußnote 4: „keine
>     verminderte Precision, sondern **gar keine Messung**") und **mit Rev. 22 (B40) ersetzt**; die
>     Kategorie steht jetzt eine Zeile höher. Rev. 20 hatte Komponentenschnitt, B38 und
>     Standdokument nachgezogen, **§8 aber nicht** — der Alttext bleibt gestrichen stehen, damit
>     der Nachzug sichtbar bleibt."

**Der Ausdrucksmächtigkeitsbefund eigener Art — Zeilen 4362–4370:**

> „  - **Ausdrucksmächtigkeitsbefund EIGENER ART (neu Rev. 22, B39):** `CYCLE_SIBLING` und
>     `CYCLE_PARENT_CHILD` bei **K5**. K5 meldet `CYCLE_*` an der **richtigen Stelle** unter
>     **falscher Kategorie** — die **Erlaubnisliste erreicht die Stelle, das Vokabular erreicht die
>     Kategorie nicht**: gemeldet wird die injizierte Rückkante als **nicht gelistete Kante**, nicht
>     als Zyklus, weil PyTestArch keine Zyklenregel hat (§3, Fußnote 7;
>     `c2c_bericht_k5_konfiguration.md` §B5). Weder Nullzeile noch Treffer — in `strict` kein
>     Treffer, in `localized` „richtige Stelle, falsche Kategorie". Für UF3 ist das die
>     interessantere Aussage als beide Randfälle: eine **Regelform** kann eine Stelle erreichen,
>     die ihr **Vokabular** nicht benennen kann."

### B4.3 UF4 — Zeilen 4393–4394

> „- **UF4:** Kosten/Latenz pro Check und Modell; Run-Varianz; roh-vs-final-Validität;
>   Grenze „nur Imports + Signaturen sichtbar"."

## B5 — Die von §8 UF3 verlangte Overlap-Analyse: FESTGESTELLTE LÜCKE

**Verlangt** ist nach §8 Zeile 4336 eine „**Overlap-Analyse K1/K4/K5 vs. K2/K3**".

**Festgestellt: die registrierte Auswertungsausgabe enthält keine solche Analyse.**
Nachweis durch Volltextsuche nach `overlap`, ohne Berücksichtigung der
Gross-/Kleinschreibung:

| Datei | Treffer |
|---|---|
| `data/campaign/eval/c13_eval_full.md` | **0** |
| `data/campaign/eval/c13_eval_full.json` | **0** |
| `docs/kapitel/kapitel7_tabellenskelette.md` | **0** |
| `docs/protokolle/c6_auswertungsspezifikation.md` | **1**, Zeile 100 — der Manifest-Feldname `control_files_overlap` in einer Feldaufzählung, **kein** Analyseabschnitt |

Auch der Sache nach steht in T1–T9 keine Tabelle, die die Treffermengen von K1/K4/K5
und K2/K3 **schnittweise** ausweist: T2 stellt die Konfigurationen **spaltenweise
nebeneinander**, T5 rechnet **je Konfiguration und Kategorie getrennt**, und beide
Tabellen tragen die Auflage „K2 und K3 werden nirgends addiert" bzw. „K2 und K3
stehen in getrennten Zeilen und werden NIRGENDS zu ‚dem LLM-Pfad' addiert oder
gemittelt".

**Die Lücke ist hier benannt und nicht gefüllt.** Sie wird nicht nachgerüstet und
nicht gerechnet; ob sie gebraucht wird, ist nicht Gegenstand dieses Auftrags.

## B6 — Die vorregistrierten Matrixzellen zu den zwei Kategorien aus A6

**Fundstelle: `docs/protokolle/eval_protokoll_phase04.md` §3, Erwartungsmatrix,
Zeilen 2420–2437.** Kopf und die beiden Zeilen wörtlich:

> „**Erwartungsmatrix (vorregistriert — das ist die falsifizierbare Fassung der Pointe aus §5
> Umsetzungsplan):**
>
> **Gilt für die Metrik `localized` (§4, Decision Record O). Für `strict` besteht keine
> Vorhersage.** K4 = import-linter 2.13, K5 = PyTestArch 4.0.1 — versionsgebunden.
>
> | Ebene 2 | K1 det. | K4 | K5 | K2/K3 LLM | Belegquelle der K4/K5-Zellen |
> |---|---|---|---|---|---|"

**Zeile 2435 — `FRAMEWORK_TYPE_IN_SIGNATURE` (betrifft K3 / I23):**

> „| `FRAMEWORK_TYPE_IN_SIGNATURE` | nein | **nein⁴** | **nein⁴** | **ja** | **K4 gemessen** (`c2b…K4-Konfiguration` §B6) · **K5 gemessen** (`c2c…K5-Konfiguration` §B6) — aufgespalten im Nachtrag Rev. 21 |"

**Die vorregistrierte Zelle K2/K3 lautet also: `ja`.**

**Zeile 2436 — `INCORRECT_LOCATION` (betrifft K2 / I28):**

> „| `INCORRECT_LOCATION` | nein | **teilweise⁵** ᴳ | nein⁶ ᴱ | **ja** | gemessen (B9+ Nachtrag) |"

**Die vorregistrierte Zelle K2/K3 lautet also: `ja`.**

**Der Schlusssatz des Matrixabschnitts, wörtlich:**

> „Abweichung der Messung von dieser Matrix ist ein Befund, kein Anlass zum Nachjustieren."

**Und das Amendment vom 11.08.2026, wörtlich:**

> „> **Amendment (11.08.2026) — Begründung: B36a.** Die Vorhersagen dieser Matrix gelten für
> > `localized` (§4). Für `strict` besteht **keine** Vorhersage; eine nachträglich formulierte
> > wäre nach Sichtung der Daten entstanden und damit keine. Die Matrix selbst bleibt unverändert."

**Zwei mitgeltende Bauvorschriften an der `INCORRECT_LOCATION`-Zeile**, wörtlich aus
demselben Abschnitt (die hochgestellten Buchstaben ᴳ und ᴱ):

> „**Hochgestellte Buchstaben = die Zelle ist an eine Bauvorschrift gebunden** (ergänzt
> 12.08.2026, Amendments in diesem Abschnitt): **ᴱ** = (e), das verschobene Modul hat keine
> Importkanten · **ᴳ** = (g), die `layers`-Liste des `exhaustive`-Contracts kommt aus dem
> Dateibaum und nicht aus der Soll-Modulliste … Diese drei Zellen sagen aus, was die Werkzeuge
> **unter diesen Bauvorschriften** leisten; unter anderen Vorschriften wären sie anders besetzt.
> In Kapitel 4 als **Konstruktionsbedingung** zu benennen, nicht als Werkzeugbefund."

---

# TEIL C — SETUP-FAKTEN, GEGENGEPRÜFT

## C1 — Der eingefrorene Messstand aus Protokoll §0.1

**Fundstelle: `docs/protokolle/eval_protokoll_phase04.md` §0.1, ab Zeile 947.**
Kopfvermerk wörtlich:

> „**Gesetzt am 27.08.2026 mit Rev. 33 (C5b), vor dem ersten Kampagnenlauf.** Jeder Wert
> unten ist am 27.08.2026 aus der Datei bzw. dem Repositorium **gelesen** — `sha256sum`,
> `git rev-parse`, `git tag -l` —, keiner aus einem Bericht übernommen."

Die Tabelle im **aktuellen** Stand (Rev. 43); durchgestrichene Vorgängerwerte sind hier
weggelassen und stehen im Protokoll sichtbar:

| Gegenstand | Wert |
|---|---|
| **Protokoll — Revision** | **Rev. 43** |
| **Protokoll — SHA256** | `759b11ede90232c2e3e8ce7d7e0149a9db7726d5cc87e35da7ceddb4369343f4` — geführt in `c5b_bericht_protokoll_freeze.md` §3, weil ein Selbstbezug im gehashten Dokument unmöglich ist; maschinell geprüft durch Invariante (A) |
| **Auswertungsspezifikation** | `docs/protokolle/c6_auswertungsspezifikation.md` = `fe991be6ade440fe973b20cdf149ebdb9acd9291fbe6bb990e8e35f1092c20d1`, an beiden registrierten Stellen (§1 und §0.1) zeichengleich; Invariante (C) |
| **Messeingang 1/7** | `data/soll/architecture-rules.yaml` = `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` |
| **Messeingang 2/7** | `data/soll/depot_soll.ilograph.yaml` = `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` |
| **Messeingang 3/7** | `data/soll/importlinter.ini` = `0c9a1e0e0430ff01e8383407ec6212c58ddcbec6e529db7b044a30132b528751` |
| **Messeingang 4/7** | `data/soll/test_architecture.py` = `7504e30ce993803f4f3dab3023ed60742fcbd2382b9deb481d1860a67186a289` |
| **Messeingang 5/7** | `data/soll/control_files.txt` = `7356e6d332e5165acdfdcfac1a66bd9803a7fa36cb4b3e7d5480bcb3526fee62` |
| **Messeingang 6/7** | `data/soll/injection_manifest.md` = `63425d5501c8f5c13459e78782e370981db8e4aa68072aae46137550b98629e1` |
| **Messeingang 7/7** | `data/soll/injection_manifest.json` = `2744116e513c9e79e3174e6e3681abdcdc7c18f36d00b6d334875e4e918cfb1f` |
| **Messeingänge — Gesamtbeleg** | „**sieben von sieben**, `sha256sum -c data/soll/SHA256SUMS` am 27.08.2026 OK"; am 28.08.2026 durch Invariante (D) erneut bestätigt (7 von 7 OK) |
| **`phase04-freeze`** | `348ca9daa456af4954f11f7152fc45201035297e` (annotiertes Tag, Tag-Objekt `19e7a7a5332c577dea194717f4bbe64cebcfdac4`) · Messpfad `~/ma/tritongraph-measure` (Worktree, detached `348ca9d`) |
| **`dist/cli.js`** | `packages/triton-conformance/dist/cli.js` = `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` |
| **Runner-Commit** | `4caf083d5e21f36440579af6888513ca897f1dd4` (`4caf083`, „fix: expect the injected importer at soll validator point (6)") — nachgezogen durch C10a, Amendment Rev. 35; `campaign_spec.py` und `postrun_check.py` unverändert |
| **Instrument 1/3** | `tools/evaluate_campaign.py` = `eb206a6fcad515f653dd25394682e0d05e4f72902b3fb0beebe9d19c0b520653` (neu gebildet C11c, Rev. 43) |
| **Instrument 2/3** | `tools/match_k4k5.py` = `c16e7c4380034163f3034916193bd96cfc6bb957768fe610cb7018d7799f4ca6` (neu gebildet C11b, Rev. 41) |
| **Instrument 3/3** | `tools/check_doc_invariants.py` = `6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018` (neu gebildet C6c-a, Rev. 39) |
| **Archivwurzel** | `~/ma/masterarbeit/data/campaign/` (= `data/campaign/` im Thesis-Repo) — Vorgabe des CLI-Parameters `--out` in `tools/run_campaign.py` (`CAMPAIGN_OUT`), **nicht hart verdrahtet**; darunter `k1/`…`k5/` und `manifests/`. Nachgezogen durch C5c, Amendment Rev. 34, **vor** dem ersten Kampagnenlauf |

**Mitgeltend, aus derselben Tabelle:** Testrepo `baseline` =
`0d651041ed87dd03f2f78359713633fac01c0a66`, 32 Injektionstags `inj/01`–`inj/32`,
Injektions-Bundle = `1b9f8b58f271332e2d66ead83a3858271a04f3aebce95b7927977d9fa1be508b`,
Baseline-Bundle = `597fa466c5ff4e05ab5c1f3550fb88e0407c3968fae8fafd420166324d4a7b18`.

**Werkzeugstände, wörtlich:**

> „**Werkzeugstände** (§1 Amendment 11.08., Nachtrag Rev. 31 T13): import-linter 2.13
> (grimp 3.15), PyTestArch 4.0.1 (networkx 3.6.1, pytest 9.0.1), Python 3.12.3, Node
> **v22.23.2** — die Node-Differenz zu C3a (`v22.22.2`) ist als folgenlos benannt, weil der
> Gatterbeleg der Build-Hash `dist/cli.js` ist und der zeichengleich stimmt."

**Gegengeprüft.** Alle vier Hashwerte der Zeilen Protokoll, Spezifikation und
Instrumente sind am 28.08.2026 durch `tools/check_doc_invariants.py` (Invarianten A,
C, E) mit **Exit 0** bestätigt; die sieben Messeingänge durch Invariante (D).

## C2 — Die Kampagnenlage je Konfiguration

**Quelle: die gehashten Laufmanifeste** unter `data/campaign/manifests/` — ein
Manifest je Invocation, jedes von einem Block-`SHA256SUMS` bezeugt (Protokoll §0.1
T7-Quelle, Rev. 39). `journal.jsonl` und die Prosa-Manifeste sind **Gegenprobe, nicht
Quelle**. Werte aus T7.1 und T6 der archivierten Ausgabe übernommen.

| Konfiguration | Invocationen | gültige Injektionen | Model-Calls (`calls_total`) | `calls_transport_failed` | externe Wanduhrzeit, Summe |
|---|---|---|---|---|---|
| **K1** | 32 | **32 / 32** | 0 | 0 | 2 513 ms |
| **K2** | 32 | **32 / 32** | 96 | 0 | 252 155 ms |
| **K3** | **61** | **32 / 32** | 183 | **50** | **9 190 542 ms** |
| **K4** | 32 | **32 / 32** | 0 | 0 | 3 621 ms |
| **K5** | 32 | **32 / 32** | 0 | 0 | 9 917 ms |

**Mitgeltende Zahlen aus derselben Tabelle:** K3 trägt **29 INVALID**-Invocationen und
**29 Wiederholungen** (`_r<n>`), alle mit `invalid_reasons = transport_failure`;
`calls_invalid` ist bei **allen fünf** Konfigurationen **0**; `valid_final` steht bei
K2 auf 96/96 = 1,000 und bei K3 auf 133/133 = 1,000.

**Gegenprobe `journal.jsonl`** (T7.1, unten): für alle fünf Konfigurationen
**deckungsgleich** in Invocationen und gültigen Injektionen. **T7.3:** keine
Konfiguration hat eine Injektion ohne gültigen Lauf; beide Gegenproben
deckungsgleich.

**Herkunftsvermerk der Kostenspalte, wörtlich aus T6:**

> „*Invocationen*, *Model-Calls* und beide Wanduhren stammen aus den **gehashten
> Laufmanifesten** (`external_wall_clock_ms` für aussen,
> `postrun.detail.wall_clock_ms_inner` für innen) und sind deshalb auch ohne
> `--with-campaign` verfügbar."

## C3 — Die fünf Messzeitfenster von K3

**Fundstelle: `data/campaign/k3/MANIFEST.md`, Kopfblock.** Wörtlich:

> „**Die 32 gültigen Läufe sind zu FÜNF verschiedenen Zeitpunkten und unter unterschiedlichen,
> nicht kontrollierten serverseitigen Bedingungen entstanden.** Verteilung der gültigen Läufe:"

| Zeitpunkt (CEST) | Injektionen |
|---|---|
| 27.08., 09:00-Stunde | 7 |
| 27.08., 10:00-Stunde | 14 |
| 27.08., 12:00-Stunde | 1 (I22) |
| 28.08., 08:00-Stunde | 7 |
| 28.08., 09:00-Stunde | 3 (I09, I11, I23) |
| **Summe** | **32** |

Direkt anschliessend, wörtlich:

> „21 Injektionen wurden im **ersten** Versuch gültig, 1 im zweiten, 7 im dritten, 1 im fünften,
> 2 im sechsten. Der Endpunkt ist **nicht gepinnt** (§6 Rev. 32), seine Auslastung ist weder
> gemessen noch kontrollierbar; **T14 (§9) gilt für diese Streuung in vollem Umfang** und ist
> bei jeder Auswertung mitzuführen."

Und am Dateiende, wörtlich:

> „Was **bleibt**, ist kein offener Punkt, sondern eine Eigenschaft des Bestandes: die 32 gültigen
> Läufe stammen aus **fünf** Zeitfenstern über zwei Tage, und der Endpunkt ist in dieser Zeit
> weder gepinnt noch in seiner Auslastung gemessen. **T14 (§9) ist bei jeder Auswertung dieses
> Blocks mitzuführen.**"

### C3.1 Der T14-Vorbehalt, wörtlich

**Fundstelle: `docs/protokolle/eval_protokoll_phase04.md` §9, Amendment 26.08.2026
(Rev. 30), Zeilen 4496–4531.**

> „- **T14 Anbieter- und Endpunktwechsel bei K3.** Die Vormessungen, auf denen die
>   K3-Erwartungen dieses Protokolls ruhen, sind über einen **anderen Zugangsweg** erhoben als
>   den, der gemessen wird. **Befund 06.5/06.6** (Schema-Fähigkeit; kein honorierter `seed`)
>   und **B36a** (Aufspaltung in **zwei** Findings je Verstoss, wechselnder Schema-Zweig — die
>   **empirische Grundlage von Decision Record O**) liefen über **OpenRouter** mit dem Slug
>   `nvidia/nemotron-3-super-120b-a12b`, gepinnt auf `digitalocean`. Gemessen wird der
>   **DigitalOcean-Direktzugang** `https://inference.do-ai.run/v1` mit der Katalog-`id`
>   `nvidia-nemotron-3-super-120b` (§1 Nachtrag Rev. 30).
>
>   **Belegstand.** Der Katalog kennt die angeforderte `id` zeichengleich; das geloggte
>   `model_version` weicht in **156 von 156** C3b-K3-Calls **nicht** vom angeforderten Namen
>   ab (`runLog.ts:270` schreibt dort `model_version_reported` — den Wert, den der Anbieter
>   selbst meldet, **nie** aus dem Anforderungsnamen zurückgefüllt); eine stille Substitution
>   wäre genau hier sichtbar und ist **nicht beobachtet**. Der Slug unterscheidet sich
>   (`nvidia/nemotron-3-super-120b-a12b` gegen `nvidia-nemotron-3-super-120b`), `provider_served`
>   ist auf dem Direktweg durchgehend `null` gegen `DigitalOcean` bei OpenRouter, und
>   `context_length` ist auf beiden Seiten mit 1 000 000 ausgewiesen.
>
>   **Was NICHT belegbar ist und hier auch nicht behauptet wird:** Quantisierung, Präzision,
>   Gewichts-Revision und Serving-Stack-Version sind über die API-Metadaten **nicht
>   ausgewiesen** (die Feldmenge des Katalogs ist erschöpfend `id`, `object`, `owned_by`,
>   `created`, `context_length`, `max_output_tokens`). Ein Tokenizer- oder Verhaltensvergleich
>   über **identische Prompts** ist nicht möglich, weil die OpenRouter-Vormessungen auf
>   **anderen Eingaben** liefen (anderes Wegwerf-Repo, anderer `checker_git_head` `e52ddbe`
>   bzw. `c493daf`, andere `topology_sha256`/`rules_sha256`). **Die Identität der Gewichte ist
>   nicht verifiziert.**
>
>   **Auflage.** Die **B36a-Charakteristik** — Aufspaltung eines Verstosses in zwei Findings,
>   wechselnder Schema-Zweig — ist an den **ERSTEN K3-Kampagnenläufen gegenzuprüfen** und das
>   Ergebnis zu **berichten, gleich in welche Richtung es ausfällt**. Bestätigt sie sich nicht,
>   ist das ein Befund über die Vormessung, kein Anlass nachzubessern: **nicht nachbessern, nur
>   berichten** (Eine-Iteration-Regel, §7).
>
>   **Strukturell dieselbe Lage** wie der bereits geführte Risikoeintrag „Befund 06.7 bezeugt
>   `c493daf`, gemessen wird `348ca9d`": **eine Vormessung bezeugt nicht den Messstand.**
>   T14 ist eine Verschärfung von T13 (Maschinenwechsel), nicht dessen Ersatz — dort war der
>   Wechsel per SHA256-Gegenprobe als folgenlos **belegbar**, hier ist er es **nicht**."

**Die Ergänzung aus Rev. 31, wörtlich:**

> „- **Zu T14 — eine schwache, indirekte Stütze der Gewichtsidentität, mehr nicht.** … Das ist eine
>   **SCHWACHE, INDIREKTE** Stütze der Gewichtsidentität und wird ausdrücklich nur als solche
>   geführt: `context_length` ist eine **Serving-Konfiguration**, keine Eigenschaft der Gewichte,
>   sie ist von jedem Betreiber frei setzbar, und beide Angaben stammen aus **Selbstauskünften der
>   Anbieter**, nicht aus einer Messung. **Der Satz aus T14 bleibt unangetastet: die Identität der
>   Gewichte ist nicht verifiziert.**"

## C4 — Die drei Auswertungsläufe

| | **Lauf 1 (C11)** | **Lauf 2 (C11b)** | **Lauf 3 (C11c)** |
|---|---|---|---|
| **Datum / Uhrzeit** | 28.08.2026, 13:16:10–13:16:11 CEST | 28.08.2026, 14:52:55–14:52:56 CEST | 28.08.2026, 16:17:24 CEST |
| **git HEAD** | `dc865d1aa90fb0816ac5f9d7bcd268025fdfe9bf` | `93089dbb863c5192b7f7dd221a119ea4d4900300` | `b979f14ac5b3b777571a6c587152e808d62689a3` |
| **Protokoll-Revision** | Rev. 39 (`9e63c370…5653f48`) | **Rev. 41** (`e94150ae…67218e78`) | **Rev. 43** (`759b11ed…69343f4`) |
| **Spezifikation** | `50f593d0…8785017` | `be3491e2…acb21d6e1` | `fe991be6…1092c20d1` |
| `tools/evaluate_campaign.py` | `5125cd595913b1226b888e67035f24f2831e0f4818b28dad4b261a57a0528eed` | `20bcdae0ebaec12930cad9ef91731f0b1e7e593b68c768be85e7d811ea23d306` | `eb206a6fcad515f653dd25394682e0d05e4f72902b3fb0beebe9d19c0b520653` |
| `tools/match_k4k5.py` | `ad3edcb1ee8537ee758d8212055371957c0493f3d8e218267d182fb9fc060022` | `c16e7c4380034163f3034916193bd96cfc6bb957768fe610cb7018d7799f4ca6` | `c16e7c4380034163f3034916193bd96cfc6bb957768fe610cb7018d7799f4ca6` |
| `tools/check_doc_invariants.py` | `6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018` | *(unverändert)* | *(unverändert)* |
| **Ausgabepfad JSON** | `data/campaign/eval/c11_eval_full.json` | `data/campaign/eval/c12_eval_full.json` | `data/campaign/eval/c13_eval_full.json` |
| **SHA256 JSON** | `ad8f0483ffd2c261d8e33a21c425c5f6a492dedae0cc99c4e135dc56b371ea30` | `12751c3e506e3f28d4d32c7c4a104e97c826dad4e71c83f00dc49d200b09f0c7` | `873893e771f3dd8a1a195b283f874858990dcd27a75a1c348fa85a1c1914977c` |
| **Ausgabepfad Markdown** | `data/campaign/eval/c11_eval_full.md` | `data/campaign/eval/c12_eval_full.md` | `data/campaign/eval/c13_eval_full.md` |
| **SHA256 Markdown** | `3d4874842a5baf92d455c1140b4874d396550fe87c50714d537a15a0a0e595af` | `afe28bc2d3d81da4b565d0b2f735745f09422f39523de2f44b27e2c80c921918` | `f8cd9c074353cefcfe52d55e0df06a76b41c3f4ff75164c3ee1e5777f414c8a2` |
| **Exit** | 0 | 0 | 0 |

**Aufrufzeile, in allen drei Läufen dieselbe bis auf die Ausgabepfade:**

```
python3 tools/evaluate_campaign.py --with-campaign \
    --json-out data/campaign/eval/c1<n>_eval_full.json \
    --markdown-out data/campaign/eval/c1<n>_eval_full.md
```

**Warum je Lauf der nächste nötig war, ein Satz je Lauf:**

1. **Nach Lauf 1** war nötig, was C11a in dreizehn Punkten aufgeschrieben hat: **drei
   Defekte, zwei nicht implementierte und zwei nicht gerenderte Tabellenteile** —
   unter anderem, dass K5 bei `CYCLE_*` in `localized` **0 statt Treffer** trug,
   dass T9 Fall 7 aus `specials` zählte, während die Funde in `co_findings` lagen, und
   dass eine **gerechnete 0** über `or ''` als leere Zelle gedruckt und damit von
   einer nicht eingesetzten Zelle nicht unterscheidbar war
   (`c11a_bericht_diagnose.md` §7).
2. **Nach Lauf 2** war ein dritter nötig, weil die Darstellung zwei Klassen von
   Mängeln trug, die die Zahlen zwar nicht bewegen, aber ihre Lesbarkeit
   entscheiden: **T5 druckte 72 Markerzellen ohne Code-Auszeichnung** — „Ein Marker
   ohne Auszeichnung ist **von Prosa nicht zu unterscheiden**, und die drei Marker
   tragen drei verschiedene Aussagen" — und **T6 druckte zwei K3-Summen in
   Exponentialschreibweise** (`9.19054e+06 ms` statt `9190542 ms`)
   (`c11c_bericht_dritter_lauf.md` §3.1, D1/D2).
3. **Nach Lauf 3** ist kein weiterer Lauf beauftragt; C11c weist nach, dass der
   **JSON-Rumpf gegen Lauf 2 identisch** ist und alle geänderten Zellen der
   Darstellungsreparatur zuzuordnen sind (`c11c_bericht_dritter_lauf.md` §5.4).

**Regel, unter der die drei Läufe nebeneinander stehen — Protokoll §0.1 Punkt 6,
wörtlich:**

> „**Keine solche Änderung darf eine Rechenregel oder einen Marker verschieben**;
> zulässig ist allein die **Behebung eines Defekts**, und zwar mit **vollständiger
> Neuauswertung** und **Ausweis beider Ergebnisse** — des Standes vor und des Standes
> nach der Behebung, nebeneinander, nicht ersetzend."

---

## Endstand

| Prüfung | Befund |
|---|---|
| `tools/check_doc_invariants.py` nach beiden Commits | **Exit 0**, alle 5 Invarianten erfüllt |
| `tools/describe_campaign.py` berührt eine Invariante | **nein** — der Prüfer läuft grün, das Werkzeug ist damit **kein Instrument** |
| `sha256sum -c data/campaign/eval/SHA256SUMS` | **6 von 6 OK** |
| Registrierte Instrumente verändert | **nein**, alle drei SHA256 unverändert |
| `data/campaign/`, `data/soll/`, Protokoll, Spezifikation, Skelette verändert | **nein** |
| `git push` | **nicht ausgeführt** |
