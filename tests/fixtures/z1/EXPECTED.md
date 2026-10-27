# Erwartete Werte der Z1-Auswertung — VON HAND GERECHNET

**Masterarbeit Timo Haas · HTWG Konstanz**
Datum: 31. August 2026 · Auftrag **Z1-A**, Schritt 1 ·
Protokoll: `z1_protokoll_extraktionsvergleich.md` Rev. 3
(SHA256 `5fd18ef3f62035c027f5e060fc79574adaedc1e247ea586f7f7d8148eb49d27d`)

> **Diese Datei wird ALLEIN und ZUERST committet — vor `tools/evaluate_z1.py` und vor
> jedem Lauf des Skripts gegen sie.** Der Zeitstempel des Commits ist der Beleg: die
> Erwartung stand fest, bevor die Maschine sie bestätigen oder widerlegen konnte.
> Dieselbe Disziplin wie in C6b (`tests/fixtures/harness/EXPECTED.md`) und C4c.
>
> **Jede Zahl unten ist aus den gehashten Messeingängen und dem Wortlaut von
> `metrics.py` / `validate.py` von Hand abgeleitet, mit der Rechnung, nicht nur dem
> Ergebnis.** Keine Zahl ist aus einem Lauf des Auswertungsskripts abgelesen — es gibt
> noch keinen.
>
> **Weicht die Maschine ab, wird beides gemeldet.** Die Handrechnung wird **nicht** an
> die Maschine angepasst, ohne dass der Fehler in der Handrechnung nachgewiesen ist; und
> dann mit durchgestrichenem Alttext an Ort und Stelle.

**Gerechnet wird gegen** (Extractor-`HEAD` `5c0b65a82cc3d8af47c022d779ff63d8a20a9e08`):

| Gegenstand | Blob (git, SHA1) | Rolle |
|---|---|---|
| `fixtures/rich_repo.full.ilograph.yaml` | `ef8e0d0181eccddf5b2e88f3315c418cc1270208` | Ansatz 1, der Triton-Vollexport |
| `fixtures/rich_repo/` (16 `.py`) | 18 Blobs, Protokoll §3.1 | die Faktenbasis beider Ansätze |
| `fixtures/rich_repo.gold.json` | `f34f74849ab6e74cf16e0212cf090045041387be` | Referenzpartition für `gold_similarity` |
| `src/llm_arch/eval/metrics.py` | `54a8021c51f1a05447b5ec64005853d5a8c9760b` | **die Formeln** (SHA256 `668d6d47…`) |
| `src/llm_arch/eval/ilograph_reader.py` | `99a9566e50211a2e86db25924f58ed9ab473743d` | der Reader (SHA256 `aa7dd31a…`) |
| `src/llm_arch/ilograph/validate.py` | `1265156e1361370e7d4ecdea3a87527734a32378` | `validate_arch` (SHA256 `a17f620e…`) |
| `src/llm_arch/facts/extractor.py` | `2e7a40e41795f02cc1192ea7cb07386a834025cf` | `substantive_modules` (SHA256 `ba5ca4e9…`) |

---

## 1. Die Bezugsgrösse: 16 AST-Einträge, 11 substanzielle Module

`extract_repo` erzeugt einen `ModuleFacts` je `.py`-Datei; `__init__.py` wird auf den
Paketnamen abgebildet (`facts/extractor.py:24-30`). Die Fixture hat **16** Dateien, also
**16** Einträge. `substantive_modules` (`facts/extractor.py:113-123`) behält, was
`classes or functions or imports` trägt.

| # | Modulname | `classes`/`functions`/`imports`? | substanziell |
|---|---|---|---|
| 1 | `bookshop` | Docstring, sonst leer (Blob `d7a77ac4…`, 72 B) | **nein** |
| 2 | `bookshop.api` | leer (Leerblob `e69de29b…`) | **nein** |
| 3 | `bookshop.api.catalog_routes` | 2 Importe, 2 Funktionen | ja |
| 4 | `bookshop.api.checkout_routes` | 2 Importe, 1 Funktion | ja |
| 5 | `bookshop.application` | leer | **nein** |
| 6 | `bookshop.application.checkout` | 4 Importe, 1 Klasse | ja |
| 7 | `bookshop.application.inventory` | 2 Importe, 1 Klasse | ja |
| 8 | `bookshop.domain` | leer | **nein** |
| 9 | `bookshop.domain.book` | 2 Importe (stdlib), 3 Klassen | ja |
| 10 | `bookshop.domain.catalog` | 1 Import, 1 Klasse | ja |
| 11 | `bookshop.domain.order` | 3 Importe, 4 Klassen | ja |
| 12 | `bookshop.domain.pricing` | 1 Import, 3 Funktionen | ja |
| 13 | `bookshop.infrastructure` | leer | **nein** |
| 14 | `bookshop.infrastructure.book_repository` | 2 Importe, 1 Klasse | ja |
| 15 | `bookshop.infrastructure.order_repository` | 1 Import, 1 Klasse | ja |
| 16 | `bookshop.infrastructure.payment_gateway` | 0 Importe, **2 Klassen** | ja |

**16 − 5 = 11.** Die fünf Ausgeschlossenen sind die vier leeren Paket-`__init__.py`
(Leerblob) und `bookshop/__init__.py`, das nur einen Docstring trägt. Deckungsgleich mit
Protokoll §3.1 und §4.3 und mit Befund 02, Anmerkung 03.08.2026.

> `bookshop.infrastructure.payment_gateway` ist der Grenzfall, der die Regel zeigt: es
> hat **keinen** Import und ist trotzdem substanziell, weil `classes` nicht leer ist.

**M** (`required_modules`) = die 11 mit „ja".

---

## 2. Die 16 Importkanten — `count_import_edges`, `metrics.py:128-140`

Gezählt werden **verschiedene gerichtete Kanten** zwischen Modulen aus **M**;
`_resolve_targets` (`metrics.py:38-57`) löst absolute Importe vollständig auf. Die Fixture
nutzt ausschliesslich absolute Importe (`relative_level == 0`).

| # | von | nach | Quelle |
|---|---|---|---|
| 1 | `…api.catalog_routes` | `…application.inventory` | `catalog_routes.py:3` |
| 2 | `…api.catalog_routes` | `…domain.book` | `catalog_routes.py:4` |
| 3 | `…api.checkout_routes` | `…application.checkout` | `checkout_routes.py:3` |
| 4 | `…api.checkout_routes` | `…domain.order` | `checkout_routes.py:4` |
| 5 | `…application.checkout` | `…domain.pricing` | `checkout.py:7` (`from bookshop.domain import pricing`) |
| 6 | `…application.checkout` | `…domain.order` | `checkout.py:8` |
| 7 | `…application.checkout` | `…infrastructure.order_repository` | `checkout.py:9` |
| 8 | `…application.checkout` | `…infrastructure.payment_gateway` | `checkout.py:10` |
| 9 | `…application.inventory` | `…domain.book` | `inventory.py:3` |
| 10 | `…application.inventory` | `…infrastructure.book_repository` | `inventory.py:4` |
| 11 | `…domain.catalog` | `…domain.book` | `catalog.py:3` |
| 12 | `…domain.order` | `…domain.book` | `order.py:6` |
| 13 | `…domain.pricing` | `…domain.order` | `pricing.py:3` |
| 14 | `…infrastructure.book_repository` | `…domain.book` | `book_repository.py:3` |
| 15 | `…infrastructure.book_repository` | `…domain.catalog` | `book_repository.py:4` |
| 16 | `…infrastructure.order_repository` | `…domain.order` | `order_repository.py:3` |

**Nicht gezählt und warum:** `dataclasses` und `enum` (`book.py:6-7`, `order.py:3-4`) sind
keine Repo-Module und fallen in `_resolve_targets` durch (`base in known` ist falsch).
`checkout.py:7` erzeugt **zwei** Kandidaten — `bookshop.domain` (Paket, in `known`) und
`bookshop.domain.pricing` (über `names`) —; der erste ist **nicht in M** und wird von
`count_import_edges` verworfen, der zweite bleibt. `payment_gateway` importiert nichts.

**`import_edge_count` = 16.**

---

## 3. Die Reduktion des Triton-Exports — `read_ilograph`

### 3.1 Modul → Komponente: 11 Blätter, 4 Komponenten

`_flatten` bildet jedes **Blatt** des `resources`-Baumes auf seinen **unmittelbaren
Elternknoten** ab. `x-triton-inner-artefacts` ist **nicht** `children` und wird deshalb
nicht betreten — die Modulknoten sind Blätter, obwohl sie Artefakte tragen.

| Komponente | Module |
|---|---|
| `bookshop.api` | `catalog_routes`, `checkout_routes` |
| `bookshop.application` | `checkout`, `inventory` |
| `bookshop.domain` | `book`, `catalog`, `order`, `pricing` |
| `bookshop.infrastructure` | `book_repository`, `order_repository`, `payment_gateway` |

**11 Einträge, 4 verschiedene Werte.** Die vier Werte sind genau die vier
Schichtenpakete (`test_reader.py:31`: „decision 3: component = layer package"). Der
Wurzelknoten `bookshop` hat `children` und ist deshalb selbst kein Blatt; er erscheint
**nicht** in der Abbildung.

### 3.2 Relationen: 16 Zeilen im Dokument → 5 Komponentenkanten

Die Perspektive `dependencies` führt **16** `relations`. `_resolve_endpoint` löst jeden
Endpunkt erst über die Modulabbildung, dann über die Komponenten-Ids; gleiche Endpunkte
(`a == b`) fallen weg, und die Menge dedupliziert.

| Zeile | roh | aufgelöst |
|---|---|---|
| 1 | `api.catalog_routes` → `application.inventory` | (api, application) |
| 2 | `api.catalog_routes` → `domain.book` | (api, domain) |
| 3 | `api.checkout_routes` → `application.checkout` | (api, application) *dupl.* |
| 4 | `api.checkout_routes` → `domain.order` | (api, domain) *dupl.* |
| 5 | `application.checkout` → **`bookshop.domain`** | (application, domain) — Endpunkt ist ein **Komponentenknoten**, kein Modul |
| 6 | `application.checkout` → `domain.order` | (application, domain) *dupl.* |
| 7 | `application.checkout` → `infrastructure.order_repository` | (application, infrastructure) |
| 8 | `application.checkout` → `infrastructure.payment_gateway` | (application, infrastructure) *dupl.* |
| 9 | `application.inventory` → `domain.book` | (application, domain) *dupl.* |
| 10 | `application.inventory` → `infrastructure.book_repository` | (application, infrastructure) *dupl.* |
| 11 | `domain.catalog` → `domain.book` | **`a == b`, fällt weg** |
| 12 | `domain.order` → `domain.book` | **`a == b`, fällt weg** |
| 13 | `domain.pricing` → `domain.order` | **`a == b`, fällt weg** |
| 14 | `infrastructure.book_repository` → `domain.book` | (infrastructure, domain) |
| 15 | `infrastructure.book_repository` → `domain.catalog` | (infrastructure, domain) *dupl.* |
| 16 | `infrastructure.order_repository` → `domain.order` | (infrastructure, domain) *dupl.* |

**`component_relations` = 5:** (api, application), (api, domain), (application, domain),
(application, infrastructure), (infrastructure, domain).
**`unresolved_relations` = []** — jeder der 32 Endpunkte löst auf.

### 3.3 Die induzierten Kanten — `induced_edges`, `metrics.py:60-89`

Dieselben 16 Importkanten aus §2, über die Abbildung aus §3.1 auf Komponenten gehoben,
Selbstkanten verworfen. Die Zeilen 11–13 (`domain` → `domain`) fallen weg; Zeile 5 der
Importliste (`checkout` → `domain.pricing`) landet auf (application, domain).

**`induced` = 5**, und zwar **dieselben fünf** wie `component_relations` in §3.2.

> Der Unterschied zu §3.2 ist die Herkunft, nicht das Ergebnis: dort aus den
> `perspectives` des Exports, hier aus dem AST. Dass beide Wege dieselbe Fünfermenge
> liefern, **ist** der Treuebefund.

---

## 4. ANSATZ 1 — die elf erwarteten Werte

`claimed` = 5 (§3.2), `induced` = 5 (§3.3), `hit = claimed & induced` = **5**.

| Kennzahl | Formel (`metrics.py`, Blob `54a8021c…`) | Rechnung | **Erwartet** |
|---|---|---|---|
| `relation_precision` | `len(hit)/len(claimed)` (`:113`) | 5 / 5 | **1.0** |
| `relation_recall` | `len(hit)/len(induced)` (`:114`) | 5 / 5 | **1.0** |
| `module_coverage` | `len(placed & M)/len(M)` (`:117-121`) | 11 / 11 | **1.0** |
| `phantom_modules` | placed ∉ `known` (`:122-123`) | alle 11 sind echte Modulnamen | **0** |
| `module_count` | `len(placed ∩ M)` (`:161-162`) | 11 | **11** |
| `component_count` | `len(set(placed.values()))` (`:163`) | 4 | **4** |
| `module_compression` | `module_count/component_count` (`:169`) | 11 / 4 | **2.75** |
| `import_edge_count` | `count_import_edges` (`:164`) | §2 | **16** |
| `component_relation_count` | `len(component_relations)` (`:165`) | §3.2 | **5** |
| `relation_compression` | `import_edge_count/relation_count` (`:174`) | 16 / 5 | **3.2** |
| `gold_similarity` | `adjusted_rand_index` (`:183-216`) | §4.1 | **1.0** |

Die ersten zehn Werte sind zeichengleich die Zusicherungen aus `tests/test_reader.py:53-73`
(Blob `7fc33d1b…`) und damit die **Festlegungen** E1 und E2 aus Protokoll §8. Eine
Abweichung ist ein Instrumentenbefund und Abbruchgrund.

### 4.1 `gold_similarity` für Ansatz 1 = 1.0, von Hand

`rich_repo.gold.json` bildet **genau die 11 substanziellen Module** auf die vier Etiketten
`api` / `application` / `domain` / `infrastructure` ab. Die Triton-Reduktion bildet
dieselben 11 Module auf `bookshop.api` / `bookshop.application` / `bookshop.domain` /
`bookshop.infrastructure` ab. `adjusted_rand_index` arbeitet über
`common = set(a) & set(b)` = alle 11 und ist **etikettinvariant** (Docstring `:185`).

Beide Partitionen sind {2, 2, 4, 3}, und **jedes** Modul liegt in beiden in derselben
Gruppe. Damit ist `pair` identisch mit `rows` und mit `cols`:
`index = sum_rows = sum_cols = C(2,2)+C(2,2)+C(4,2)+C(3,2) = 1+1+6+3 = 11`.
`expected = 11·11 / C(11,2) = 121/55 = 2.2`; `max_index = (11+11)/2 = 11`;
`(11 − 2.2)/(11 − 2.2) = 1.0`. → **1.0**

### 4.2 Was für Ansatz 1 NICHT gilt

`valid_raw` / `valid_final` / `attempts_used` tragen für Ansatz 1 den Text
**„entfällt — kein Lauf"** (Protokoll §7.1), **nicht** `1.0` und **nicht** einen Strich.
Ansatz 1 erzeugt keine Modellausgabe, also auch keine Validität.

---

## 5. ANSATZ 2 — keine Kennzahl, sondern Gültigkeit, Zähler, Ursache

Protokoll §5.4: eine Bedingung ohne gültigen Lauf ist **NICHT ERHOBEN** — nicht 0, nicht
ein Strich. Auf ungültiger Ausgabe wird **keine Treue gemessen**. Erwartet werden deshalb
nur die Zähler; sie sind unten aus den archivierten `arch_model.json` und dem Wortlaut von
`validate_arch` (`validate.py:23-66`, Blob `1265156e…`) **von Hand** abgeleitet.

### 5.1 K2 (`data/z1/k2/`, Fenster 16384) — 26 `relation:`-Fehler, hergeleitet

Das abgelegte Modell trägt **5 Komponenten** — `bookshop`, `bookshop.api`,
`bookshop.application`, `bookshop.domain`, `bookshop.infrastructure` — und **13
Relationen**, deren Endpunkte **Modulnamen** sind (`bookshop.api.catalog_routes` → …),
nicht Komponenten-Ids.

`validate_arch` prüft in vier Schleifen:

| Schleife | `validate.py` | Ergebnis | Zahl |
|---|---|---|---|
| `disjointness` | `:38-45` | kein Modul steht in zwei Komponenten | **0** |
| `phantom_module` | `:47-49` | alle platzierten Namen sind echte Module (auch die vier Paketnamen unter `bookshop`) | **0** |
| `completeness` | `:51-55` | alle 11 aus **M** sind platziert | **0** |
| `relation` | `:57-64` | 13 Relationen × 2 Endpunkte, **keiner** in `{bookshop, bookshop.api, bookshop.application, bookshop.domain, bookshop.infrastructure}` | **26** |

**Erwartet: 26 Fehler, alle der Klasse `relation:`, `valid_final == false`,
`attempts_used == 3`, in allen sechs Läufen; `arch_model.json` über alle sechs
bytegleich.**

**`component_count` = 4, nicht 5:** `compression` filtert `placed` auf **M**
(`metrics.py:160`). Die Komponente `bookshop` enthält nur die vier Paketnamen, und keiner
davon ist substanziell — sie fällt aus dem Nenner. `module_count` bleibt 11.

### 5.2 K3 (`data/z1/k3/`) — 11 `completeness:`-Fehler aus einem Doppelpunkt

Die Rohantwort schreibt den Schlüssel als **`"contained_modules:"`** — mit angehängtem
Doppelpunkt. Das Schema hat **kein** `additionalProperties: false` (Protokoll §3.3 (3)),
pydantic verwirft den unbekannten Schlüssel **still**, und `contained_modules` hat einen
Default. Ergebnis: **kein** Modul ist platziert.

`completeness` meldet dann jedes der 11 Module aus **M**: **11 Fehler**.
`relation:` meldet nur, wo ein Endpunkt keine Komponenten-Id trifft — bei vier bzw. fünf
korrekt benannten Komponenten also **nicht**.

**Erwartet: `valid_final == false` in allen sechs Läufen; alle sechs `arch_model.json`
untereinander verschieden; `relation:`-Fehler in genau zwei der sechs Läufe** (dort, wo
das Modell Komponenten anders benennt als es sie referenziert).

### 5.3 `k2_trunkiert` (`data/z1/k2_trunkiert/`, Fenster 4096) — Lieferausfall

**Kein Modellbefund.** Der Server liess 2 050 von 4 281 Token herein (Protokoll §3.3 (6));
die registrierte Bedingung war nicht geliefert. Das Modell antwortete auf einen halben
Prompt — ohne Systemtext, denn Ollama schneidet **vorn** ab — und lieferte **11
Komponenten mit leeren `contained_modules`**, also die 1:1-Transkription, die der
Systemtext ausdrücklich verbietet.

**Erwartet: 11 `completeness:`-Fehler je Lauf, `valid_final == false`, sechs bytegleiche
`arch_model.json`.** Diese Zeile wird **nicht** als Modellbefund geführt.

---

## 6. Die Zählgatter der Kontextfenster-Hochrechnung

Die Hochrechnung (Auftrag §5) braucht einen Tokenizer. Er wird aus dem
**GGUF-Metadatenblock** des Modells gebaut, das die Messung selbst gefahren hat — Vokabular,
Merges und Pre-Tokenizer-Id aus der Datei, die Ollama geladen hat, ohne Modell-Call. Er ist
nur brauchbar, wenn er die **bereits aufgezeichneten** Ollama-Zählungen zeichengleich
reproduziert. Vier Gatter, alle aus registrierten Quellen:

| # | Gegenstand | Soll | Fundstelle |
|---|---|---|---|
| G1 | `attempt_0/prompt.txt` (`cb2fcefd…`, 18 842 B), **mit** Chat-Template | **4 281** | Protokoll §3.3 (6) |
| G2 | dieselbe Datei **ohne** Template | **4 274** | `z1_t_bericht_kontextfenster.md` §1.1 |
| G3 | `k2_trunkiert/*/attempt_2/prompt.txt` ohne Template | **6 010** | Protokoll §3.3 (6), Tabelle |
| G4 | die drei Versuchsprompts des Blocks `k2/`, mit Template | **4 281 · 5 483 · 6 685** | `data/z1/MANIFEST.md`, Nachtrag Z1-T Phase 3 (= `usage.prompt_tokens` der Artefakte) |

**Verfehlt der Tokenizer eines der vier Gatter, wird die Hochrechnung nicht gestellt.**
Sie ist ohnehin als **EXTRAPOLATION** zu kennzeichnen und keine Messung.

---

## 7. Was hier bewusst NICHT steht

- **Kein ARI-Verdikt zu E8.** Ansatz 2 ist nicht erhoben; die Entscheidungsregel kommt
  nicht zur Anwendung. Die Handrechnungs-Auflage aus Protokoll Rev. 2 ist an die Bedingung
  „bevor er ein Verdikt trägt" geknüpft und wird damit **nicht fällig**.
- **Kein Median, keine Spannweite** für K2 oder K3: Aggregate über nicht erhobene
  Bedingungen gibt es nicht (§5.1, §5.4).
- **Keine Zahl für die Zeile „Ansatz 2"** in der Ergebnistabelle §7.1 ausser dem Text
  „nicht erhoben" und dem Grund.
