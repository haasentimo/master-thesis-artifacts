# MANIFEST — Soll-Modell der Konformitätskampagne

**Datum der Ablage:** 23. August 2026 · **ergänzt um die Regeldatei:** 23. August 2026 (C2a)
**Ergänzt um die K5-Testdatei:** 23. August 2026 (C2c)
**Ergänzt um die Kontrollliste:** 23. August 2026 (C3a)
**Injektionsmanifest zuletzt geändert:** 25. August 2026 (Auftrag C4B-0 — I16-Zielmodul und
`offending_type` I21–I24 aufgelöst, vor dem Bau der Injektions-Commits, Protokoll §3 Nachtrag
Rev. 28; davor C4a — erste Ableitung)
**K4-Konfiguration zuletzt geändert:** 23. August 2026 (B39/B40-Nachzug — **nur der
Kopfkommentar** zu `include_external_packages`, siehe *Erzeugung* unten; kein Contract, keine
Einstellung berührt)
**Regeldatei zuletzt geändert:** 23. August 2026 (C2b Teil A — die Subjektform in allen
sechzehn Statements vereinheitlicht, Protokoll §4 Nachtrag Rev. 19; davor C2a-Nachtrag — die
vier R-PORT-Statements gekürzt, Protokoll §3 Nachtrag Rev. 18)
**Bezug:** Phase 04, Schritt 4c (Soll-Ilograph, Phantomliste, Soll-Validator), Schritt C2a
(Regeldatei), C2b (K4-Konfiguration), C2c (K5-Konfiguration) und C3a (Clean-Control-Set)
**Berichte:** [docs/repo-kontext/4c_bericht_soll_und_validator.md](../../docs/repo-kontext/4c_bericht_soll_und_validator.md) ·
[docs/repo-kontext/c2a_bericht_regeldatei.md](../../docs/repo-kontext/c2a_bericht_regeldatei.md) ·
[docs/repo-kontext/c2b_bericht_k4_konfiguration.md](../../docs/repo-kontext/c2b_bericht_k4_konfiguration.md) ·
[docs/repo-kontext/c2c_bericht_k5_konfiguration.md](../../docs/repo-kontext/c2c_bericht_k5_konfiguration.md) ·
[docs/repo-kontext/c3a_bericht_clean_state_audit.md](../../docs/repo-kontext/c3a_bericht_clean_state_audit.md)

## Zweck

Dies ist der **eingefrorene Messeingang** der Kampagne. Er besteht aus **zwei** gehashten
Dateien, die der Checker im selben Ausdruck lädt (`loadSoll`, `run.ts:262-266`):
`depot_soll.ilograph.yaml` (Topologie) und `architecture-rules.yaml` (Regelmenge).

Die SHA256 der beiden Checker-Eingänge gehen in die **Provenienz jedes Messlaufs** ein — als
**`topology_sha256`** (`run.ts:283`) und **`rules_sha256`** (`run.ts:284`) in den
`run_header` und über `buildProvenance` in das `--json-out`-Dokument (`run.ts:311`), das
seine Werte ohne Neuberechnung aus dem Header übernimmt. **Präzisierung:** die einzelnen
`llm_call`-Zeilen tragen die Felder **nicht**; sie sind über `run_id` an den Header gejoint.
Zwei Läufe mit verschiedenem Soll oder verschiedener Regelmenge sind an diesen beiden Hashes
und nur an ihnen unterscheidbar.

Das Soll deckt den **gesamten Messraum** ab, nicht einen Zustand (Protokoll §2, Amendment
12.08., Punkt (1)): neben den 73 Modulen der Clean-Baseline `B` listet es die **vier Zielorte
der `INCORRECT_LOCATION`-Injektionen** I25–I28. Grund ist `componentOf` — ein exakter Lookup
ohne Präfixlogik; ein Modul an einem nicht gelisteten Ort ist **unmapped**, erzeugt **keinen**
LLM-Call und erschiene als False Negative.

## Inhalt

| Datei | Beschreibung |
|---|---|
| `depot_soll.ilograph.yaml` | Soll-Modell im Ilograph-Format: 19 Komponenten, 77 Module, 39 Relationen |
| `architecture-rules.yaml` | Regelmenge der Zielarchitektur: 16 Regeln, 6 Kategorien, 53 Scope-Einträge |
| `importlinter.ini` | K4-Konfiguration: 13 Contracts, import-linter 2.13 |
| `test_architecture.py` | K5-Konfiguration: 23 Regeln, PyTestArch 4.0.1 |
| `control_files.txt` | Clean-Control-Set: 52 repo-relative Pfade, ein Pfad je Zeile |
| `injection_manifest.md` / `injection_manifest.json` | Injektionsmanifest (C4a): erwartete Schlüssel je Injektion I01–I32, von Hand aus der Spezifikation abgeleitet, **bevor** die Injektions-Commits existieren; in C4c um die 32 `injection_sha256` und die tragenden Methoden/Modulpfade ergänzt |
| `SHA256SUMS` | Prüfsummen aller Dateien dieses Verzeichnisses |

| Datei | SHA256 | Provenienzfeld |
|---|---|---|
| `depot_soll.ilograph.yaml` | `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` | `topology_sha256` |
| `architecture-rules.yaml` | `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` | `rules_sha256` |
| `importlinter.ini` | `0c9a1e0e0430ff01e8383407ec6212c58ddcbec6e529db7b044a30132b528751` | eigener SHA256 im Messmanifest (Protokoll §1 Rev. 10) |
| `test_architecture.py` | `7504e30ce993803f4f3dab3023ed60742fcbd2382b9deb481d1860a67186a289` | eigener SHA256 im Messmanifest (Protokoll §1 Rev. 10) |
| `control_files.txt` | `7356e6d332e5165acdfdcfac1a66bd9803a7fa36cb4b3e7d5480bcb3526fee62` | eigener SHA256 im Messmanifest; `control_files_count` im `run_header` (Protokoll §6 Rev. 22) |
| `injection_manifest.md` | `63425d5501c8f5c13459e78782e370981db8e4aa68072aae46137550b98629e1` | gehashter Messeingang; erwartete Schlüssel entstanden vor den Injektions-Commits (C4a, Nachtrag C4b-0); Hash nachgezogen in C4c und in D1 (K2/K3-Schlüssel I21–I24, siehe unten) |
| `injection_manifest.json` | `2744116e513c9e79e3174e6e3681abdcdc7c18f36d00b6d334875e4e918cfb1f` | gehashter Messeingang; erwartete Schlüssel entstanden vor den Injektions-Commits (C4a, Nachtrag C4b-0); Hash nachgezogen in C4c und in D1 (K2/K3-Schlüssel I21–I24, siehe unten) |

## Erzeugung

### `test_architecture.py`

**Halb maschinell.** Die beiden Tabellen `COMPONENTS` und `WHITELIST` sind aus dem
eingefrorenen Soll `depot_soll.ilograph.yaml` **erzeugt**, nicht von Hand kuratiert: die
19 Komponenten mit ihren Modulen aus dem `resources`-Block, die 39 Whitelist-Kanten aus
dem `dependencies`-Perspektivblock. Zwei mechanische Umsetzungen liegen dazwischen und
**nur dort**:

1. Das Soll führt eine `__init__.py` unter ihrem **Paketnamen** (Protokoll §2, Punkt (6)),
   PyTestArch führt `<paket>` und `<paket>.__init__` als **zwei** Knoten und schreibt einen
   Import in einer `__init__.py` dem zweiten zu (c2a §5.3). Jedes Soll-Modul, das ein Paket
   der Clean-Baseline ist, wird deshalb auf `…__init__` umgeschrieben. Die Paketknoten
   selbst werden **nie** genannt.
2. **Bauvorschrift K5-1:** die vier `INCORRECT_LOCATION`-Träger und ihre vier
   Phantom-Zielorte fallen weg. 77 − 4 − 4 = **69** genannte Module.

Der Regeltext selbst ist von Hand geschrieben. **23 Regeln:** 19 Erlaubnislisten
(`should_not().import_modules_except_modules_that().are_named([…])`, je Komponente eine)
und 4 Portregeln (`are_named(<Träger>).should().import_modules_that()`, je eine auf ein
Trägermodul, auf Untermodulebene). **Ein** Architekturobjekt mit
`exclude_external_libraries = True`; das zweite Objekt aus Rev. 14 entfällt mit der
Framework-Regel (Protokoll §1 Nachtrag Rev. 21). Damit ist die in Rev. 14 verlangte
**Zuordnung Regel → Architekturobjekt** trivial: **alle 23 Regeln laufen gegen dieses eine
Objekt.**

`root_path` **und** `module` zeigen auf das **Wurzelpaketverzeichnis** `<repo>/src/depot`,
nicht auf den Source-Root — nur so lauten die Knotennamen `depot.core.ports` statt
`src.depot.core.ports` und fallen mit den `match_key` des Manifests zusammen (c2a §5.2).

**Clean-State-Vorprüfung gegen `baseline`: `24 passed`, Exit 0** — 23 Regeln plus ein
Wächtertest zu K5-1. Belege in `docs/repo-kontext/c2c_bericht_k5_konfiguration.md`.

```
DEPOT_SRC=<testrepo>/src python -m pytest -p no:cacheprovider -q data/soll/test_architecture.py
```

### `importlinter.ini`

**Von Hand geschrieben und gemessen.** Abgeleitet aus der Whitelist
(`c1_komponentenschnitt.md` §4) und der Contract-Typ-Vorregistrierung (Protokoll §3), **nicht
aus dem Injektionsplan** (Protokoll §1 Rev. 13). 13 Contracts: 1 × `layers` (Spine),
6 × `forbidden` (Schichtsprünge, alle mit `allow_indirect_imports = True`), 1 × `protected`,
1 × `independence`, 1 × `acyclic_siblings` (`ancestors = depot`), 3 × `layers` mit
`exhaustive = True`. Kopfeinstellungen `root_packages = depot` (eingerückter Block) und
`include_external_packages = True`.

**Clean-State-Vorprüfung gegen `baseline`: `13 kept, 0 broken`, Exit 0.** Jeder Lauf mit
`--no-cache`. Belege in `docs/repo-kontext/c2b_bericht_k4_konfiguration.md`.

```
PYTHONPATH=<testrepo>/src lint-imports --config data/soll/importlinter.ini --no-cache
```

**Änderung vom 23.08.2026 (B39/B40-Nachzug), vor jeder Messung:** der **Kopfkommentar** zu
`include_external_packages = True` trug noch die FP⁴-Begründung („beide Werkzeuge müssen den
Framework-Import sehen"), die **Protokoll §1 Rev. 21 (Teil C1)** ersetzt hat. Neu und tragend:
die externen Importe bleiben im Graphen **sichtbar**, und dass K4 dennoch nichts meldet, ist
damit eine **inspizierbare Nicht-Abdeckung** statt eines Artefakts der Unsichtbarkeit.
**Es ist ausschließlich ein Kommentar** — kein Contract, keine Einstellung, kein Schalter ist
berührt; der Clean-State von K4 ist unverändert. Nicht bis C5 aufgeschoben, weil die Datei
**gehashter Messeingang** ist: ein Kommentar, der dem Protokoll widerspricht, ist derselbe
Defekt wie die `README.md`-Behauptung in `B` (Protokoll §1 Rev. 17, Grund (c)) — nur hier noch
behebbar, weil noch nichts gemessen wurde. Der Datei-SHA256 verschiebt sich von `652b2352…`
auf `0c9a1e0e…`; **kein `expected_match_key` und kein Contract-Ergebnis ändert sich.**

**Nachlauf zur Änderung, 23.08.2026:** `13 kept, 0 broken`, **Exit 0**, `Analyzed 75 files,
90 dependencies` — gegen Tag `baseline` (`0d651041ed87dd03f2f78359713633fac01c0a66`,
Working Tree clean), import-linter 2.13 / grimp 3.15, `--no-cache`. Identisch zum
C2b-Stand.

### `depot_soll.ilograph.yaml`

Maschinell durch **`tools/generate_soll.py`** (Protokoll §2, Amendment 12.08., Punkt (2) —
die Modulliste wird generiert, nicht von Hand geschrieben) aus drei Quellen:

1. **Dateibaum des Testrepos** bei Tag **`baseline`** = `0d651041ed87dd03f2f78359713633fac01c0a66`
   — entscheidet, **welche** Module existieren (73 `.py`-Dateien; `README.md` und `.gitignore`
   werden ignoriert). `__init__.py` bildet auf den **Paketnamen** ab (Protokoll §2, Punkt (6)).
2. **`docs/planung/c1_modulliste.md` §1** (Rev. 5) — entscheidet, **zu welcher Komponente** ein
   Modul gehört. Die Zuordnung ist aus dem Pfad **nicht** ableitbar (§D.11): die fünf leeren
   Paketmodule `depot`, `depot.core`, `depot.identity`, `depot.orders`, `depot.billing` gehören
   zur Komponente `core`, obwohl drei davon außerhalb von `src/depot/core/**` liegen.
3. **Explizite Phantomliste im Generator** — die vier Zielorte, Komponente **geerbt** von der
   Herkunftskomponente (Protokoll §2, Nachtrag 13./14.08. (a)).

Die **39 Relationen** stammen aus `docs/planung/c1_komponentenschnitt.md` §4 (Rev. 2).

### `architecture-rules.yaml`

**Von Hand geschrieben und geprüft**, nicht generiert — anders als die Topologie. Die
Regelliste folgt `docs/planung/c1_komponentenschnitt.md` §8 (Rev. 2), ergänzt um **R-CORE-1**;
Kategorien, Rezepte, Portreservierung, die beiden R-PLACE-1-Klauseln und die Singular-Regel
aus `docs/protokolle/eval_protokoll_phase04.md` §3 (Rev. 17); die vier wörtlichen
Soll-Signaturen aus den Bauberichten `4b2…` §5, `4b3…` §4 und `4b4…` §3.

Die Regelmenge drückt die **eingefrorene Zielarchitektur** aus, **nicht** den Injektionsplan
(Protokoll §1 Rev. 13). **R-CORE-1 hat keine Injektion** — das ist beabsichtigt und trägt zur
Falsch-Positiv-Messung bei.

**Änderung vom 23.08.2026 (C2a-Nachtrag), vor jeder Messung:** die vier `R-PORT`-Statements
führen die **wörtliche Soll-Signatur nicht mehr**. Es bleiben Trägermodul, die Methode als
`Class.method` und der Porttyp in der bindenden Schreibweise. Grund: Komponentenschnitt §8
verlangt für diese Regeln die **Typschreibweise**, nicht die Signatur; die volle Signatur machte
die Prüfung zum Zeichenkettenvergleich und inflationierte `ABSENCE_REQUIRED` gegenüber den
Baselines. Vorregistriert in Protokoll §3 Nachtrag Rev. 18; belegt im c2a-Bericht, Nachtrag §N1.
Der `rules_sha256` verschiebt sich von `943b4820…` auf `0bf17dc6…`; **kein
`expected_match_key` ändert sich** — die Portschreibweise ist unverändert. Die vier
`R-SIG`-Statements sind **nicht** berührt: dort ist die wörtliche Signatur der Vertrag.

**Änderung vom 23.08.2026 (C2b Teil A), ebenfalls vor jeder Messung:** **alle sechzehn**
Statements schließen jetzt einheitlich mit der erwarteten **Subjektform** in den Feldnamen des
Antwortschemas — `subject.from`/`subject.to` bei `FORBIDDEN_RELATION` und `CYCLE`,
`subject.offending_type` bei den vier Elementkategorien. Grund: `subjectKey` ist das vierte
Segment des `match_key` und aus **beiden** Formen baubar (`matchKey.ts:23-26`); ohne die
Zuordnung misst `strict` die Formatwahl des Modells statt seiner Erkennung. Vorregistriert in
Protokoll §4 Nachtrag Rev. 19; belegt im c2b-Bericht, Teil A. Der `rules_sha256` verschiebt sich
von `0bf17dc6…` auf `72fa851f…`; **kein `expected_match_key` ändert sich**.

**Reproduzierbar:** der Lauf ist deterministisch (sortierte Ausgabe); ein zweiter Lauf aus
denselben Eingaben erzeugt die Datei **byte-identisch** (belegt im 4c-Bericht §4).

```
tools/generate_soll.py --testrepo ~/Schreibtisch/ma-conformance-testrepo --rev baseline
```

### `injection_manifest.md` / `injection_manifest.json`

**Von Hand aus der Spezifikation abgeleitet, nicht aus Werkzeugausgaben.** Quellen ausschließlich
`docs/planung/c1_modulliste.md` Rev. 5, `docs/planung/c1_komponentenschnitt.md` Rev. 3,
`docs/protokolle/eval_protokoll_phase04.md` Rev. 27, `architecture-rules.yaml` (diese Datei),
`docs/ddr/checker_entscheidungen_l_m.md` §M/§M.2 und die vier Bauberichte 4b-1…4b-4. Kein
Modell-Call, kein Aufruf des Checkers, der Rule-Engine, von import-linter oder PyTestArch.

**`injection_sha256` bleibt in dieser Fassung leer** und wird erst in C4c ergänzt, nachdem die 32
Injektions-Commits über der Clean-Baseline `B` existieren — siehe die Begründung im Kopf von
`injection_manifest.md` (Anti-Tautologie-Regel, Decision Record M). Die beiden Dateien selbst sind
bereits jetzt gehashte Messeingänge und fallen ab Ablage unter dieselbe Änderungssperre wie die
übrigen Dateien dieses Verzeichnisses; eine spätere Änderung ist ein Amendment mit
vollständigem Re-Run, kein stiller Edit.

~~**Zwei offene Punkte**, im Bericht (`docs/repo-kontext/c4a_bericht_injektionsmanifest.md`)
benannt statt durch Annahme geschlossen: der `offending_type` (Framework-Typname) und die
tragende Methode/Signatur der vier `FRAMEWORK_TYPE_IN_SIGNATURE`-Injektionen (I21–I24) — beide
entscheidet erst der Bauauftrag C4b; und ein Widerspruch zwischen dem Injektionsrezept von I16
und einer im Protokoll zitierten K5-Messausgabe.~~

**Aufgelöst 25.08.2026 (Auftrag C4B-0), vor dem Bau der Injektions-Commits, ausschließlich aus
`docs/protokolle/eval_protokoll_phase04.md` §3 Nachtrag Rev. 28 — kein Modell-Call, kein
Werkzeuglauf:** der Widerspruch bei **I16** ist zugunsten des Injektionsrezepts entschieden
(Rückkante auf das Paketmodul `depot.orders.services`, nicht auf `order_service`; die zitierte
K5-Ausgabe stammte aus der C2c-Prüfsonde gegen zehn Baseline-Kopien). Der injizierte **Typ** der
vier `FRAMEWORK_TYPE_IN_SIGNATURE`-Injektionen (I21–I24) ist festgelegt: `sqlalchemy.orm.Session`.
**Weiterhin offen**, bis C4b: die tragende Methode/Signatur bei I21–I24 und ihre wörtliche
Schreibweise im Code. Einzelheiten in `injection_manifest.md` §5.6/§6 und
`injection_manifest.json` (`resolution_addendum_2026_08_25`).

**Nachtrag 25.08.2026 (Auftrag C4C) — SHAs und Methodennamen ergänzt, keine Erwartung geändert.**
Ergänzt wurden ausschließlich (1) die **32 `injection_sha256`** (`injection_manifest.md` §2.1 und
`injection_sha256` je Eintrag der JSON-Fassung), Quelle `data/testrepo/MANIFEST.md` (Nachtrag
25.08.2026), dort lokal aus `git bundle verify` gelesen und gegen `git ls-remote --tags origin`
abgeglichen, in C4c zusätzlich Eintrag für Eintrag gegen `git rev-parse inj/NN` gestellt (**32/32
zeichengleich**), und (2) die von C4b benannten **tragenden Methoden bzw. Modulpfade** je Injektion
(`injection_manifest.md` §2.2).

**Kein `expected_match_key` ist geändert** — maschinell gegengeprüft, die Wertemenge ist vor und
nach dem Auftrag zeichengleich. Die erwarteten Schlüssel selbst wurden vor dem Bau der Commits
abgeleitet (C4a, Commit `56055de`, 25.08.2026 11:03 +02:00; Injektions-Commits 18:32 +02:00) — die
Anti-Tautologie-Regel bleibt gewahrt. Die **Hashes oben sind entsprechend nachgezogen**; das ist
der in C4a angekündigte Nachtrag, kein stiller Edit.

Bei **I21–I24** sind tragende Methode (`Customer.reload` / `Order.reload` / `OrderLine.reload` /
`Invoice.reload`), Signatur (`def reload(self, session: sqlalchemy.orm.Session) -> None:`) und
wörtliche Schreibweise (`sqlalchemy.orm.Session`, durch die Top-Level-Import-Regel **erzwungen**)
nachgetragen; **weiterhin offen** bleibt allein der Eintrag des `expected_match_key`, der außerhalb
des Auftrags C4C liegt (`injection_manifest.md` §6, Bericht
`docs/repo-kontext/c4c_bericht_vorabpruefung.md` §A2).

**Nachtrag 26.08.2026 (Auftrag D1) — der K2/K3-`expected_match_key` von I21–I24 ist eingetragen.**
Die vier Werte (`FORBIDDEN_SIGNATURE_TYPE|<Komponente>|<Trägermodul>|sqlalchemy.orm.Session`)
stehen jetzt in beiden Manifestfassungen; gebildet **mechanisch** aus den Feldern des Manifests und
aus `depot_soll.ilograph.yaml` (Modul→Komponente wie `load_soll` in
`tools/evaluate_control_run.py`), Trennzeichen und Segmentordnung an `matchKey.ts:26` verifiziert,
und zeichengleich (**4 von 4, 0 Abweichungen**) gegen `c4c_bericht_vorabpruefung.md` §A2 gestellt.
Maschinell gegengeprüft: die Wertemenge aller `expected_match_key` unterscheidet sich vor/nach dem
Auftrag in **genau vier** Einträgen, alle I21–I24, alle von Platzhalter auf Schlüssel; `.md` und
`.json` tragen für alle 32 Einträge identische Werte. Die vollständige Ableitungskette mit Datum
und Fundstelle je Glied — samt der Offenlegung, dass der K2-Kontrolllauf vom 24.08.2026
`R-FRAMEWORK-1` 63-mal gesehen hat, davon neun Findings auf Dateien ohne `sqlalchemy` im
gerenderten Prompt (`c3b_k2_nachtrag_findingbezug.md` §B5) — steht im **Ableitungsvermerk unter der
§3-Tabelle** von `injection_manifest.md`. Anker gegen den Verdacht nachträglicher Anpassung ist die
am 23.08.2026 gehashte Regeldatei, also vor jenem Kontrolllauf. Die **Hashes oben sind entsprechend
nachgezogen**. Zu I21–I24 führt §6 damit keinen offenen Punkt mehr.

## Kennzahlen

| Größe | Ist |
|---|---|
| Komponenten (Relationsendpunkte) | **19** |
| Module | **77** = 73 Dateien + 4 Phantome |
| Phantomeinträge | **4** (I25–I28) |
| Relationen (Whitelist) | **39** |
| Regeln | **16** |
| Kategorien (Ebene 1) | **6**, jede von ≥ 1 Regel getragen |
| Scope-Einträge, alle aufgelöst | **53** |
| Komponenten von ≥ 1 Regel gescopt | **19 von 19** |
| `statement`-Zeichen insgesamt | **10 211** |
| K4-Contracts | **13** |
| K5-Regeln | **23** = 19 Erlaubnislisten + 4 Portregeln |
| K5-Architekturobjekte | **1** (`exclude_external_libraries = True`) |

## Geprüft

Beide Dateien sind vom **Checker selbst** geladen (`loadSoll` → `resolveTopology` +
`parseArchitectureRules`, Wegwerf-Aufruf, kein Modell-Call) und vom **Soll-Validator**
`tools/validate_soll.py` gegen die Clean-Baseline geprüft. Ergebnisse im 4c-Bericht §5/§6 und
im c2a-Bericht §5.

**Punkt (3) des Validators ist seit C2a eingeschaltet** — über den vorgesehenen Schalter
`--rules`, ohne Codeänderung — und seit dem C2a-Nachtrag **vierteilig**: (3a) Scopes gegen die
Topologie, (3b) jede Komponente gescopt, **(3c) `category` zeichengleich mit den sechs
Ebene-1-Strings** (Exit ≠ 0 bei Abweichung), **(3d) jede Kategorie von ≥ 1 Regel getragen**:

```
tools/validate_soll.py --soll data/soll/depot_soll.ilograph.yaml \
                       --testrepo ~/Schreibtisch/ma-conformance-testrepo \
                       --rules data/soll/architecture-rules.yaml
```

```
[3] rules[]: scopes against the topology, categories against protocol §3
      rules 16
  OK   (3a) scoped components outside the topology = 0 []
  OK   (3b) components scoped by no rule = 0 []
  OK   (3c) categories outside the level-1 encoding = 0 []
  OK   (3d) level-1 categories carried by no rule = 0 []
RESULT: OK
```

**Warum (3c) dort und nicht in der C5-Freeze-Liste:** ein Zeichenfehler in `category` wird weder
von `parseArchitectureRules` (`rules.ts:67` verlangt nur einen nicht-leeren String) noch von
(3a)/(3b) gefangen und fällt sonst erst am Join auf — als **Recall 0** in der betroffenen
Kategorie, dem Modell zugeschrieben. Der Validator läuft in C3 und in C7 **je Injektionscommit**;
dort muss die Prüfung sitzen.

## Abgrenzung — dies ist NOCH NICHT der Freeze-Stand

Der **Freeze** ist C5 und steht aus. Bis dahin können sich **beide** Dateien ändern; jede
Änderung verschiebt `topology_sha256` bzw. `rules_sha256` und ist im Messmanifest zu erklären.
Ebenfalls abzugrenzen: `data/testrepo/` sichert das **Messobjekt** (`--base` = `0d65104`),
`data/checker/` den **Checker-Stand** (Bundle auf `fe66357`; `checker_git_head` ist seit Increment 7 **`348ca9d`**, noch ohne eigenes Bundle), und dieses Verzeichnis
den **Messeingang** (`topology_sha256` + `rules_sha256`).

**Die K4-Konfiguration liegt seit C2b hier** und trägt ihren eigenen SHA256 (Protokoll §1
Rev. 10). Sie ist **kein** Eingang des Checkers — `loadSoll` liest sie nicht —, sondern die
vollständige Regelmenge des Baseline-Werkzeugs **K4**; für sie **ist** die Datei die Regel, und
die B38-Fallen laufen still grün durch. Sie fällt ab der ersten Messung unter dieselbe
Änderungssperre.

~~**Offen und ausdrücklich nicht Gegenstand von C2b:** die **K5-Testdatei** (C2c) bekommt
ebenfalls einen eigenen SHA256; sie liegt noch nicht hier.~~ **Erledigt mit C2c
(23.08.2026):** `test_architecture.py` liegt hier und trägt ihren eigenen SHA256. Die
**Zuordnung Regel → Architekturobjekt** ist mit dem Wegfall des zweiten Objekts trivial —
alle 23 Regeln laufen gegen das eine Objekt — und oben unter *Erzeugung* festgehalten. Der
**`ancestor`** des K4-`acyclic_siblings`-Contracts (`depot`) bleibt im Messmanifest zu
führen; der Datei-SHA allein macht ihn nicht rekonstruierbar.

Wie `importlinter.ini` ist auch `test_architecture.py` **kein** Eingang des Checkers —
`loadSoll` liest sie nicht —, sondern die vollständige Regelmenge des Baseline-Werkzeugs
**K5**. Sie fällt ab der ersten Messung unter dieselbe Änderungssperre.


## `control_files.txt` — das Clean-Control-Set

**Maschinell erzeugt**, wie die Modulliste des Soll und aus demselben Grund: eine von Hand
gepflegte Liste ist der Ort, an dem eine Datei still verschwindet, und jede fehlende Zeile senkt
den **Nenner der Falsch-Positiv-Rate**, ohne dass es auffällt.

```
tools/build_control_set.py --testrepo <testrepo> --out data/soll/control_files.txt
```

**Kriterium, aus dem Protokoll (§5, Nachtrag 14.08.2026, Rev. 17), nicht aus dem Werkzeug:** alle
`.py`-Dateien des Baums **außer den LEEREN `__init__.py`** — leer heißt kein Import, kein `def`,
kein `class`, kein `__all__`, mit `ast` entschieden und **nicht** über die Dateigröße. Der Checker
leitet **kein** Control-Set ab (`cliExtractor.ts:113-136`, Kommentar dort); die Menge ist eine
Protokollentscheidung und bleibt als gehashtes Artefakt außerhalb des Messpfads.

**Abgezählt auf `B` (`0d65104`):** 73 `.py`-Dateien, davon **21 leere Paketmodule** ausgeschlossen,
**52 Zeilen** in der Liste — die 50 inhaltstragenden Module plus die beiden inhaltstragenden
Paketmodule `depot/core/adapters/__init__.py` und `depot/orders/services/__init__.py`.

**Sie ist ein Messeingang wie Soll und Regeldatei** und fällt unter dieselbe Änderungssperre. Der
Checker liest sie über `--control-files`; `control_files_count` im `run_header` zählt sie **nach**
Abzug der Überschneidung mit dem Diff (`run.ts:161`), und die Lauf-Akzeptanzregel des
Kontrolllaufs lautet `control_files_count == calls_total` (Protokoll §6, Nachtrag Rev. 22).
