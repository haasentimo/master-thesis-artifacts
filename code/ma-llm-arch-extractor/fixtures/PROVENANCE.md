# Provenienz der `rich_repo`-Fixture

Dieses Dokument hält fest, woher die `rich_repo`-Fixture stammt, was an ihr belegbar ist
und was nicht. Es ist Voraussetzung der Head-to-Head-Messung „Triton vs. LLM-Abstraktion"
der Masterarbeit: dort steht die Fixture für **Ansatz 1** (deterministische Ableitung), und
eine Messung, deren Eingang keine dokumentierte Herkunft hat, trägt nichts.

**Stand:** 30.08.2026, Repo-HEAD `1223e78`. Jede Angabe unten ist in diesem Repo mit den
jeweils genannten Kommandos nachprüfbar.

## Handhabungsregel: der Blob-Hash ist die Referenz

**Für jede Hashangabe zu diesen Dateien gilt der Blob-Hash aus der Git-Objektdatenbank,
nicht die Datei im Arbeitsbaum.** Der Arbeitsbaum dieses Klons liegt auf einem
Windows-Dateisystem und trägt CRLF-Zeilenenden; die Blobs tragen LF. `core.autocrlf` ist
`false`, eine `.gitattributes` existiert nicht, also gleicht Git die Differenz nicht aus:
`git status` meldet dauerhaft 60 Dateien als geändert, `git diff --ignore-cr-at-eol` ist
leer. Beide Hashstände fallen dadurch auseinander:

| Datei | Blob (LF, Referenz) | Arbeitsbaum (CRLF, **nicht** Referenz) |
|---|---|---|
| `rich_repo.full.ilograph.yaml` | `ef8e0d0181eccddf5b2e88f3315c418cc1270208` | `7c65d1abfbd68c191ab00e0f1d3212e274798ab8` |
| `rich_repo.gold.json` | `f34f74849ab6e74cf16e0212cf090045041387be` | `5919e08594da9538392f0f9b24e71a383bf6aac3` |

Prüfung: `git rev-parse HEAD:fixtures/<datei>` gegen `git hash-object -- fixtures/<datei>`.

---

## 1 Gegenstand

Die Fixture besteht aus drei Teilen: dem Beispielrepo `rich_repo/`, dem Triton-Export
`rich_repo.full.ilograph.yaml` und der Gold-Referenz `rich_repo.gold.json`.

### 1.1 `rich_repo/` — das Beispielrepo

Sechzehn Python-Dateien, alle in **einem** Commit angelegt und seither **nie berührt**:

| Datei | Blob-Hash |
|---|---|
| `rich_repo/bookshop/__init__.py` | `d7a77ac4854dbe1c9134adae23ebbd6d1f9fb3e5` |
| `rich_repo/bookshop/api/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| `rich_repo/bookshop/api/catalog_routes.py` | `6772d542150e1e71f298182f9d5d97b74746c1ef` |
| `rich_repo/bookshop/api/checkout_routes.py` | `6aff2cbd01edaf989d8292e09d39ebeacdf7d5cb` |
| `rich_repo/bookshop/application/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| `rich_repo/bookshop/application/checkout.py` | `5bad7691614fef54793e17a3247f098c0c1d980d` |
| `rich_repo/bookshop/application/inventory.py` | `fe27bcbfb642c71dcad1488b0bdb4eaa594b2ff9` |
| `rich_repo/bookshop/domain/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| `rich_repo/bookshop/domain/book.py` | `06405dc040f30f87203c6a4387d364830e0fa2c7` |
| `rich_repo/bookshop/domain/catalog.py` | `a23a28aefa60483b7c4173b75f416a98694eddd8` |
| `rich_repo/bookshop/domain/order.py` | `f3ee4afec980f026d12165a2c296da4711fd3918` |
| `rich_repo/bookshop/domain/pricing.py` | `ee9e35df44db588cd46a38237637a5c943f245d5` |
| `rich_repo/bookshop/infrastructure/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| `rich_repo/bookshop/infrastructure/book_repository.py` | `ee479d6a0b8bd693b267cfbf13f5ce61ec362ca4` |
| `rich_repo/bookshop/infrastructure/order_repository.py` | `859c30e3993bb9cb6c34dac97b88d44bde65cb3d` |
| `rich_repo/bookshop/infrastructure/payment_gateway.py` | `1e8e1fbaff286959689cda0eb4ad18c0adf78cdd` |

- **Erster Commit = letzter berührender Commit:** `34e368c`, 2026-06-25 14:03:52 +0200,
  Timo Haas — `test: add richer bookshop fixture with multiple modules per layer`.
  Aus dem Commit-Körper: „Add fixtures/rich_repo (bookshop) with four layers (domain,
  application, infrastructure, api), several modules each and realistic cross-layer
  imports, so abstraction runs are forced to group modules rather than map 1:1."
- Prüfung: `git log --diff-filter=A -- fixtures/rich_repo` und
  `git log --format=%h -- fixtures/rich_repo` — beide liefern genau `34e368c`.

**Zur Zahl 11.** Die Kennzahlen sprechen von *elf Modulen*, das Verzeichnis enthält
sechzehn Dateien. Beides ist richtig: fünf der sechzehn sind `__init__.py` — vier davon
leer (Blob `e69de29…`, der leere Blob), `bookshop/__init__.py` enthält nur einen
Docstring. `substantive_modules()` (`src/llm_arch/facts/extractor.py:113-123`) zählt nur
Module mit Klassen, Funktionen oder Importen; damit fallen genau diese fünf heraus und
16 − 5 = **11** bleiben. Dieselben elf Module und dieselben vier Schichten stehen im
Export und in der Gold-Referenz.

### 1.2 `rich_repo.full.ilograph.yaml` — der Triton-Export

| Angabe | Wert |
|---|---|
| Blob-Hash | `ef8e0d0181eccddf5b2e88f3315c418cc1270208` |
| Erster Commit | `2625af9`, 2026-06-26 10:16:53 +0200, Timo Haas |
| Betreff | `feat: add tool-agnostic Ilograph reader and canonical reduced form` |
| Letzter berührender Commit | `2625af9` — **derselbe**, die Datei wurde nie geändert |

Inhalt: ein Dokument mit den drei Schlüsseln `description`, `resources`, `perspectives`;
16 Ressourcenknoten (5 Pakete, 11 Module), 20 innere Artefakte, 16 Importkanten.

### 1.3 `rich_repo.gold.json` — die Gold-Referenz

| Angabe | Wert |
|---|---|
| Blob-Hash | `f34f74849ab6e74cf16e0212cf090045041387be` |
| Erster Commit | `f74d8a5`, 2026-06-25 15:52:27 +0200, Timo Haas |
| Betreff | `feat: add gold-free fact-fidelity metrics and ARI similarity` |
| Letzter berührender Commit | `f74d8a5` — **derselbe**, die Datei wurde nie geändert |

Inhalt: eine flache Abbildung Modul → Schichtlabel für die elf Module.

---

## 2 `rich_repo.full.ilograph.yaml` ist ein echter Triton-Export

Der Erzeuger ist `codeModelToFullExportDocument` aus dem Repo **`tritongraph`**
(`packages/triton-core/src/codeModelToIlograph.ts`). Dieses Repo liegt nicht hier; die
Zeilenangaben unten beziehen sich auf `tritongraph` HEAD `348ca9d` (23.08.2026), die
Formeln sind unverändert seit `17fc000` (16.06.2026), also seit vor dem Fixture-Datum
(§4 nennt die Prüfung).

Vier Strukturmerkmale der Datei folgen je einer Codestelle des Exporters. Keines davon
ist beim Abschreiben oder Nachbauen von Hand plausibel zu treffen; zusammengenommen
belegen sie die Herkunft.

### 2.1 Die sich ausschliessenden Schlüssel `node-type` / `project-kind`

`codeModelToIlograph.ts:219-221` setzt genau **einen** der beiden Schlüssel, nie beide:

```ts
...(container.kind === 'module'
  ? { 'x-triton-project-kind': 'module' as const }
  : { 'x-triton-node-type': 'package' }),
```

**Befund an der Fixture:** von 16 Knoten tragen 5 `x-triton-node-type: package` und 11
`x-triton-project-kind: module`. **Kein Knoten trägt beide, kein Knoten trägt keinen.**
Eine von Hand geschriebene Datei hätte hier keinen Grund, zwei verschiedene Schlüssel für
denselben Zweck strikt komplementär zu vergeben.

### 2.2 Die `package-scope`-Bedingung

`codeModelToIlograph.ts:223` setzt `x-triton-package-scope` **nur**, wenn der Knoten
Kinder hat **und** kein Modul ist:

```ts
...(children.length && container.kind !== 'module' ? { 'x-triton-package-scope': true as const } : {}),
```

**Befund an der Fixture:** `x-triton-package-scope: true` steht auf genau fünf Knoten —
`bookshop`, `bookshop.api`, `bookshop.application`, `bookshop.domain`,
`bookshop.infrastructure`. Das ist zeichengleich die Menge der Knoten mit `children`, und
zeichengleich die Menge der Paketknoten. Kein Modulknoten trägt den Schlüssel. Die
Bedingung ist also an der Fixture in beiden Richtungen erfüllt.

### 2.3 Die `· `-Untertitelformel

`containerSubtitle` (`codeModelToIlograph.ts:166-175`) baut den Untertitel aus bis zu drei
Teilen, verbunden mit `' · '` (Leerzeichen, U+00B7, Leerzeichen): der Art des Knotens,
`N folder(s)` bei Kindern, `N artefact(s)` bei Artefakten — Singular/Plural über
`length === 1`.

**Befund an der Fixture:** die Formel wurde für **alle 16 Knoten** nachgerechnet;
**null Abweichungen**. Drei Eigenheiten, die das über einen Zufallstreffer hinausheben:

- Die Singular-/Pluralregel greift korrekt in beide Richtungen — `module · 1 artefact`
  gegen `module · 3 artefacts`.
- `folders` zählt `container.children.length` **ohne Rücksicht auf die Art der Kinder**.
  `bookshop.api` hat zwei Kinder, und beide sind Module, keine Ordner — der Untertitel
  lautet trotzdem `package · 2 folders`. Diese Ungenauigkeit ist eine Eigenart des
  Exporters, kein Ergebnis, das jemand von Hand so schriebe.
- Kein Untertitel trägt einen Zeilenzahl-Zusatz. `withLoc(…, subtreeLoc(container,
  options.fileLineCounts))` hängt einen solchen nur an, wenn Zeilenzahlen vorliegen;
  `codeModelToFullExportDocument` reicht keine durch. Auch das Fehlen passt zum Exporter.

### 2.4 Die dreifeldrige „slim"-Reduktion

`slimExportResource` (`codeModelToIlograph.ts:830-853`) wirft die schweren Felder
(`declaration`, Konstruktor- und Methodensignaturen, Quelldatei, Quellzeile) weg und
reduziert **jedes innere Artefakt auf `{ id, name, subtitle }`**. Der Exportknopf ruft
den Exporter mit `detail: 'slim'` (`editor/src/App.vue:1406`), und `slim` ist ohnehin die
Vorgabe (`codeModelToIlograph.ts:875`).

**Befund an der Fixture:** über alle 20 inneren Artefakte hinweg ist die Vereinigung der
Schlüsselmengen exakt `['id', 'name', 'subtitle']` — kein Artefakt trägt mehr, keines
weniger. Kein `x-triton-declaration`, keine Signatur, keine Quellangabe irgendwo in der
Datei.

### 2.5 Zusätzlich: der `perspectives`-Block

Nicht als eigenes Merkmal gefordert, aber im selben Sinn beweiskräftig: die Datei trägt
genau eine Perspektive mit `name: dependencies`, `orientation: leftToRight`,
`color: royalblue` — die drei Konstanten aus `codeModelToIlograph.ts:892-896`, in dieser
Reihenfolge.

**Nachprüfung.** Die Auswertungen in §2.1–2.4 stammen aus einem Lesedurchlauf über die
Fixture (YAML laden, Knoten rekursiv abgehen, Schlüssel und Untertitel gegen die Formeln
halten). Sie sind mit jedem YAML-Parser reproduzierbar; es wurde nichts an der Datei
verändert.

---

## 3 Die `description`-Zeile ist von Hand gesetzt

Die erste Zeile der Fixture lautet:

```yaml
description: Full code-model export for rich_repo.
```

**Diese Zeile kann der Exporter so nicht erzeugt haben.** Der Beleg in vier Schritten:

1. **Der Exporter baut die Beschreibung aus dem Tab-Titel.** Der Exportknopf ruft
   (`editor/src/App.vue:1394-1411`):
   ```ts
   description: `Full code-model export for ${tab.title}.`,
   ```
   Der Rumpftext stimmt also — die Formel ist es, aus der die Zeile stammt. Eingesetzt
   wird `tab.title`, nicht der Repo- oder Verzeichnisname.
2. **Beide Python-Ladewege präfixen den Tab-Titel.** Zum Fixture-Datum gab es genau zwei
   Wege, einen Python-Tab zu öffnen, und beide setzen den Titel mit Präfix:
   - gebündeltes Beispiel — `title` wird auf das Template-Literal `Python: ${dir}`
     gesetzt (`App.vue:4160`, heute; `3586` im Stand vom 16.06.),
   - Laufzeit-Arbeitsbereich — `title` wird auf `Python packages: ${workspaceName}`
     gesetzt (`App.vue:4857`, heute; `4285` im Stand vom 16.06.).

   Ein Export aus `rich_repo` hätte damit `Full code-model export for Python: rich_repo.`
   oder `Full code-model export for Python packages: rich_repo.` ergeben — nie den nackten
   Namen.
3. **Auch der dritte Weg hilft nicht.** Ein aufgebohrter Unterbereich („drill") erbt als
   Titel den blossen Paketnamen (`App.vue:613`), hier also `bookshop`; die Beschreibung
   hiesse dann `… for bookshop.`. Auch das ist nicht `rich_repo`.
4. **Eine Umbenennungsfunktion für Tabs existiert nicht** — weder heute (`348ca9d`) noch
   im Stand vom 16.06.2026 (`17fc000`). Eine Suche über `editor/src` und `packages/*/src`
   nach `renameTab` bzw. „rename … tab" liefert nichts; der einzige Treffer,
   `applyRenamesInPlace` in `targetTopology/targetEditSession.ts:155`, benennt Container
   einer Soll-Architektur um, keine Tabs — und stammt ohnehin erst aus dem Juli.

Denselben Weg zeigt der **Dateiname**: der Exporter leitet ihn aus demselben `tab.title`
ab (`App.vue:1412-1413`, `base = tab.title.replace(/[^A-Za-z0-9._-]+/g, '-')`), ein Export
hiesse also `Python-rich_repo.full.ilograph.yaml`. Die Fixture heisst
`rich_repo.full.ilograph.yaml`.

**Konsequenz — ausdrücklich festgehalten, damit es später niemand als Defekt liest.**
Beschreibungszeile und Dateiname wurden nach dem Export von Hand auf den nackten Namen
gekürzt. Das ist **kosmetisch**: `description` ist ein Freitextfeld, es geht in keine
Kennzahl ein; der Leser (`read_ilograph`) wertet ausschliesslich `resources` und
`perspectives` aus. Es ist aber der Grund, **warum ein Re-Export nicht byte-identisch
ausfallen kann** — und zwar unabhängig davon, ob sich am Exporter sonst etwas geändert
hat. Wer künftig einen Byte-Vergleich anstellt, muss diese eine Zeile (und den
Dateinamen) ausnehmen; eine Abweichung dort ist erwartet und kein Fehler.

---

## 4 Nicht entscheidbar: der Erzeuger-Commit

**Welcher `tritongraph`-Commit die Datei erzeugt hat, ist nicht entscheidbar.** Das ist
eine Lücke, keine offene Aufgabe: die Angabe ist aus den vorhandenen Artefakten nicht
zu gewinnen und wird auch nicht nachträglich beschafft werden können.

Was fehlt: die Datei trägt keinen Erzeuger-Vermerk — kein Werkzeug-, Versions- oder
Commit-Feld; der Exporter schreibt keines. Der Commit `2625af9`, der sie diesem Repo
hinzufügt, nennt keinen Stand des Editors. Ein Lauf-, Export- oder Sitzungsprotokoll aus
dem Editor existiert nicht (der Export ist ein Browser-Download, siehe §8).

Was sich eingrenzen lässt, mehr nicht: die Datei wurde am **26.06.2026 vor 10:16:53**
erzeugt; der jüngste `tritongraph`-Commit vor diesem Zeitpunkt ist `17fc000`
(16.06.2026, `feat(diagram): show lines-of-code per package for all CodeModel languages`).
Aus dieser Eingrenzung folgt **nicht**, dass `17fc000` der Erzeuger war — der Editor kann
aus einem beliebigen älteren Arbeitsstand gelaufen sein.

Was sich sagen lässt und in §2 belegt ist: der Erzeuger war **ein** Stand dieses
Exporters, und die vier tragenden Formeln sind in `17fc000` bereits zeichengleich
vorhanden (`description` `codeModelToIlograph.ts:912` und `App.vue:1146`, `package-scope`
`:223`, `' · '`-Verbindung `:174`, `{ id, name, subtitle }` `:889`).

---

## 5 `rich_repo.gold.json`

**Belegt** ist, was Commit-Historie und Datei hergeben:

| Frage | Antwort | Fundstelle |
|---|---|---|
| Von wem? | Timo Haas | Autor von `f74d8a5` und `34e368c` |
| Wann? | 2026-06-25 15:52:27 +0200 | `f74d8a5` |
| Wie oft geändert? | nie — ein Commit, Blob am HEAD identisch | `git log -- fixtures/rich_repo.gold.json` |
| Wozu? | ARI-Ähnlichkeitssignal, ausdrücklich **nicht** Korrektheitsmass | `src/llm_arch/eval/metrics.py:7,209-212`; geladen über die Geschwisterkonvention `<repo>.gold.json` in `src/llm_arch/cli.py:22-26` |

**Zum Verfahren.** `f74d8a5` sagt über sich selbst: „Replace the *.expected.json files
with a slim `fixtures/rich_repo.gold.json` module->label map." Die abgelöste Datei
`rich_repo.expected.json` kam aus `34e368c`, und dieser Commit bezeichnet sie als
**„a hand-written gold reference"**. Ein Verfahren im Sinne einer Ableitungsvorschrift ist
für die Gold-Referenz damit **nicht belegt** — sie ist von Hand gesetzt.

Der Übergang von `expected.json` zu `gold.json` ist nachgerechnet und **rein
mechanisch**: die 15 Modulnennungen der alten Datei (`contained_modules` über vier
Komponenten) verlieren die vier Paketmodule `bookshop.api`, `bookshop.application`,
`bookshop.domain`, `bookshop.infrastructure`; die verbleibenden **elf** behalten als Label
je die `id` ihrer Komponente. Für alle elf stimmt das Label überein. Dass der Autor genau
so vorgegangen ist, sagt allerdings **kein** Commit und keine Datei — die Übereinstimmung
ist ein Befund, keine belegte Herleitung, und wird hier nicht als solche geführt.

**Nicht belegbar:** nach welchen Kriterien die Schichtzuordnung der elf Module
ursprünglich entschieden wurde. Sie ist naheliegend (jedes Modul erhält das Paket, in dem
es liegt), aber nirgends aufgeschrieben.

### 5.1 `DEFERRED.md:11-12` ist veraltet

`DEFERRED.md` sagt in Stufe 1 (Zeilen 10–12):

> **Single fixture repo only** — RESOLVED: added `fixtures/rich_repo` (`bookshop`,
> 4 layers, multiple modules each) with a gold reference at
> `fixtures/rich_repo.expected.json` to test real grouping, not 1:1 mapping.

**Die dort genannte `rich_repo.expected.json` existierte** — angelegt in `34e368c` — **und
wurde in `f74d8a5` durch `rich_repo.gold.json` ersetzt** (`git show --name-status f74d8a5`
zeigt `D fixtures/rich_repo.expected.json` und `A fixtures/rich_repo.gold.json`).
`f74d8a5` hat `DEFERRED.md` zwar angefasst, aber nur einen neuen Abschnitt
„Evaluation v1 — metrics" angehängt; die Stelle in Stufe 1 blieb stehen. **Der Text ist
veraltet.** Er beschreibt keine Datei, die es gibt.

Dieselbe Veraltung trifft `DEFERRED.md:52-53`, das auf
`fixtures/sample_repo.expected.json` verweist — ebenfalls in `f74d8a5` gelöscht. Der
Textnachzug in `DEFERRED.md` ist mit diesem Dokument **nicht** erledigt; er ist hier nur
als bekannt vermerkt.

---

## 6 Unverändertheit

Die Fixture ist seit ihrer Entstehung nicht angefasst worden. Belegt über drei Stände:

| Vergleich | Kommando | Ergebnis |
|---|---|---|
| `689a9cf` → `80e13f4d` | `git diff --name-only 689a9cf 80e13f4 -- fixtures/` | **leer** |
| `80e13f4d` → `HEAD` (`1223e78`) | `git diff --name-only 80e13f4 HEAD -- fixtures/` | **leer** |

Zusätzlich einzeln geprüft: die Blobs von `rich_repo.full.ilograph.yaml`
(`ef8e0d01…`) und `rich_repo.gold.json` (`f34f7484…`) sind in `689a9cf`, in `80e13f4` und
am HEAD **zeichengleich** (`git ls-tree <commit> -- fixtures/…`). Für jede Datei der
Fixture ist ausserdem der erste Commit zugleich der letzte berührende (§1).

Es gilt die Handhabungsregel vom Kopf dieses Dokuments: **verglichen werden Blobs, nicht
Dateien im Arbeitsbaum.** Ein `sha256sum` über den Arbeitsbaum liefert wegen CRLF andere
Werte und ist als Beleg unbrauchbar.

---

## 7 Zeitverhältnis zu den Kennzahlen

Als Tatsache festgehalten, ohne Wertung:

| Zeitpunkt | Commit | Was entsteht |
|---|---|---|
| 26.06.2026, 10:16:53 +0200 | `2625af9` | `fixtures/rich_repo.full.ilograph.yaml` **und** `tests/test_reader.py` (mit der Treuerechnung) — **derselbe Commit** |
| 26.06.2026, 10:20:59 +0200 | `ac30da6` | die Kompressionsrechnung: `compression()` in `metrics.py`, `test_triton_compression` in `test_reader.py`, Kompressionsfelder in `meta.json` |

Der Abstand beträgt **vier Minuten**. Die in `tests/test_reader.py` fest verdrahteten
Sollwerte der Kompression — `module_compression == 11 / 4` (2,75) und
`relation_compression == 16 / 5` (3,2) — sind aus genau dieser Fixture gerechnet; die
Commit-Nachricht von `ac30da6` sagt es selbst: „Tests cover a hand example and the real
Triton export (2.75 module, 3.2 relation)."

Ebenso im selben Commit wie die Fixture entstand der Treue-Sollwert
`test_triton_is_faithful_baseline` (P = R = Coverage = 1,0, Phantoms 0). `2625af9` sagt:
„The real Triton export of rich_repo is the test fixture; it scores a faithful P=R=1.0
baseline."

Diese Chronologie ist der Bestandsaufnahme der Masterarbeit entnommen
(`z1_2_bericht_chronologie.md`, Zeilen 62–63 und 810–811) und in diesem Repo mit
`git log --format='%h %ad %s' --date=iso` über `2625af9` und `ac30da6` sowie
`git show --name-status 2625af9` **gegengeprüft**; Zeitstempel, Betreffzeilen und
Dateilisten stimmen überein.

---

## 8 Re-Export als optionale Bestätigung — **nicht ausgeführt**

Ein Re-Export wurde **bewusst nicht durchgeführt** und ist auch nicht Voraussetzung
dieses Dokuments.

**Was er praktisch verlangte.** Es gibt **kein CLI-Kommando** für diesen Export. Die
Datei entsteht ausschliesslich über `exportFullModelYaml` (`editor/src/App.vue:1394`) im
Vue-Editor: die Funktion serialisiert das Modell des aktiven Python-Tabs und übergibt es
an `downloadTextFile` — einen **Browser-Download** über ein `<a download>`-Element. Ein
Re-Export setzt also einen laufenden Dev-Server, einen geladenen `rich_repo`-Tab und eine
Interaktion im Browser voraus.

**Was er beantwortete — und was nicht.** Er zeigte, ob der **heutige** Exporter aus
demselben Eingang dieselbe Struktur erzeugt. Er sagt **nichts** über die Herkunft der
vorliegenden Datei. Beide Fragen sind getrennt zu führen, denn der Exportpfad hat sich
seit dem 26.06.2026 verändert:

| Commit | Datum | Änderung | Art |
|---|---|---|---|
| `2b95ccb` | 02.07.2026 | `refactor(diagram): remove flat-modules view toggle, default to package graph` — entfernt `codeModelToFlatModulesDocument` aus derselben Datei | am Exporter, nicht am Vollexport-Pfad |
| `2003e50` | 03.07.2026 | `feat(editor): visual target-architecture editor for the conformance checker` — Sichtbarkeiten, `rollupImportRelations` über einen Owner-Index | am Exporter, nicht am Vollexport-Pfad |
| `d26c790` | 04.07.2026 | `fix(python): resolve relative imports in __init__.py against the package itself` | **semantisch** — verändert das Modell, das exportiert wird |

`d26c790` ist der Fall, auf den es ankommt: er korrigiert die Auflösung relativer Importe
in `__init__.py` und verschiebt damit **Importkanten**, also genau das, woraus die
Kennzahlen 16/5 gerechnet sind. Für `rich_repo` ist kein Effekt zu erwarten — die vier
Paket-`__init__.py` sind leer und die Fixture nutzt absolute Importe —, aber „nicht zu
erwarten" ist keine Messung. Ein Re-Export wäre daher als eigener, datierter Vorgang zu
protokollieren und nicht als Provenienzbeleg zu lesen.

**Und in jedem Fall gilt §3:** byte-identisch fiele ein Re-Export ohnehin nicht aus, weil
Beschreibungszeile und Dateiname von Hand gekürzt wurden.

---

## 9 Verwendung

Wofür die Fixture in der Arbeit steht:

- **Ansatz 1 — deterministische Ableitung.** In der Head-to-Head-Messung Z1 vertritt
  `rich_repo.full.ilograph.yaml` den werkzeuggestützten, deterministischen Weg
  (Triton liest den Quelltext und schreibt die Architektur heraus) gegenüber Ansatz 2,
  der LLM-gestützten Abstraktion. Beide werden über dieselbe kanonische Reduktion
  (`ReducedModel`, `read_ilograph` / `reduce_arch`) auf dieselben Kennzahlen abgebildet
  und sind erst dadurch vergleichbar.
- **Eingang der Treue- und Kompressionsrechnung.** `tests/test_reader.py:13` bindet die
  Datei als `TRITON` ein. Auf ihr laufen:
  - `test_triton_reads_modules_to_layer_components` — 11 Module auf 4 Schichten,
  - `test_triton_lifts_relations_to_component_edges` — 5 Komponentenkanten, keine
    unauflösbaren Relationen,
  - `test_triton_no_unmatched_against_facts` — kein Modul ohne Entsprechung in den
    AST-Fakten aus `fixtures/rich_repo`,
  - `test_triton_is_faithful_baseline` — Präzision, Recall und Coverage je 1,0, null
    Phantommodule,
  - `test_triton_compression` — 11/4 und 16/5.
- **`rich_repo/`** ist dabei die gemeinsame Grundwahrheit: dieselben Quelldateien speisen
  über `extract_repo` die AST-Fakten, gegen die beide Ansätze gemessen werden.
- **`rich_repo.gold.json`** liefert allein das ARI-Ähnlichkeitssignal — ausdrücklich ein
  Referenzsignal, **nie** Korrektheit (`src/llm_arch/eval/metrics.py:7`).
