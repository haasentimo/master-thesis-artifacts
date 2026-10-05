# `data/z2/` — Archivwurzel der Z2-Eingaben und -Läufe

**Lebendes Dokument.** Es wird fortgeschrieben und trägt selbst keinen Messwert; gehasht
sind die Blöcke, nicht diese Datei. Angelegt am 02.09.2026, Auftrag **S2b-2**, für die
erste der beiden B1-Eingaben nach Z2-Protokoll **§3a-1** (Amendment 01.09.2026, `e40bad3`).

## Zweck des Blocks `eingaben/`

Er trägt die **Messeingänge** der Bedingung B1 — nicht Läufe, nicht Auswertungen. B1 hat
nach §3a **zwei** Eingaben:

| Datei | Registriert in | Stand |
|---|---|---|
| `eingaben/ist_modell.yaml` | §3a-1 — Tritons eigener Exporter über den Editor | **liegt** (02.09.2026, S2b-2) |
| `eingaben/input_facts.json` | §3a-2 — Faktenextraktion des Extractors | **FEHLT NOCH** |

**Die zweite Eingabe fehlt.** `input_facts.json` ist nach §3a-2 mit dem Aufrufargument
**`<testrepo>/src`** zu erzeugen — `extract_repo` kennt keine `src/`-Behandlung
(`extractor.py:23-29`), die Modulnamen lauteten sonst `src.depot.…`. Ihre Gegenprobe steht
ebenfalls in §3a-2: die Modulnamenmenge der Faktenbasis und die Menge der
Modul-Ressourcen-Ids des Ist-Modells sind bis auf leere `__init__.py` deckungsgleich;
Abweichung melden, nicht angleichen.

## Ablage

```
data/z2/
  MANIFEST.md          ← diese Datei, lebend, ungehasht
  eingaben/            ← die B1-Messeingänge
    SHA256SUMS         ← hasht ALLES im Block ausser sich selbst
    ist_modell.yaml    ← der Triton-Export, BYTEGLEICH zur Downloaddatei
    input_facts_raw.json  ← NEU 02.09.2026 (S2c-2): Rohfaktenbasis, 73 Records — PROVENIENZ
    input_facts.json      ← NEU 02.09.2026 (S2c-2): finale Faktenbasis nach Stufe 0 + 0b, 52 Records
  messungen/           ← NEU 02.09.2026 (S2c-1): Instrumentenmessungen nach §3b (a)
    SHA256SUMS         ← hasht ALLES im Block ausser sich selbst
    tokenmessung_2026-09-02.json
```

Die Konvention ist die von `data/z1/MANIFEST.md` übernommene:

- **`SHA256SUMS` je Block, nicht global.** Spätere Blöcke (Läufe, Auswertung) werden nach
  diesem erhoben und committet; ein globales `SHA256SUMS` risse bei jedem Folgecommit den
  bezeugten Stand der Eingaben auf. Prüfung: `cd data/z2/<block> && sha256sum -c SHA256SUMS`.
- **`MANIFEST.md` lebend und ungehasht** — es wird fortgeschrieben und ist kein Messeingang.
- **Nachzugsregel:** jede Änderung unter `data/z2/` zieht `SHA256SUMS` und diese Datei im
  **selben Commit** nach (analog `data/z1/` und `data/soll/`).

**Die Eingabedatei wird nicht angefasst.** Keine Zeile ist umformatiert, sortiert,
eingerückt oder kommentiert; der Provenienzblock steht **hier**, nicht in der Datei. Sie
ist ein Messeingang und muss bytegleich zum Export bleiben. Der registrierte Name ist
`ist_modell.yaml` (§3a-1); der originale Downloadname steht unten in der Provenienz und ist
selbst ein Beleg (Prüfung 3, `scopeContainerId`).

## Provenienz `eingaben/ist_modell.yaml` — sechs Angaben nach §3a-1

**1 — Instrument.** `codeModelToFullExportDocument`
(`packages/triton-core/src/codeModelToIlograph.ts:863`), gerufen aus `exportFullModelYaml`
(`editor/src/App.vue:1394-1413`), serialisiert über `stringifyIlographYaml`
(`editor/src/ilograph/parse.ts:12-20`).

**2 — Exporter-Repo und Commit.** `tritongraph` @
`348ca9daa456af4954f11f7152fc45201035297e`. Arbeitsbaum **clean**
(`git status --porcelain` leer, gemessen 02.09.2026 nach dem Export). Der Auftraggeber hat
vor dem Export `npm install` in `packages/triton-runtime` ausgeführt: **es hat keine
versionierte Datei geändert**. `packages/triton-runtime/package-lock.json` ist versioniert
und **unverändert** (`git diff --stat` auf die Datei ist leer; ihre mtime steht auf
02.09.2026 10:46:38, der Inhalt ist byte-identisch zum Commit). Berührt ist allein das
ignorierte `packages/triton-runtime/node_modules/`. Es wurde **nichts bereinigt, nichts
committet, nichts ausgecheckt**.

**3 — Laufumgebung.** Runtime `[triton-runtime] listening on http://127.0.0.1:4317`,
`version=0.7.5`, `persistence=file`, `TRITON_HTTP_PATH_PREFIX` unset,
`TRITON_ALLOWED_REPO_ROOTS` **nicht gesetzt**. Editor via `npm run dev` auf
`127.0.0.1:5173`. Ladeweg `loadRuntimeWorkspaceProject` über `GET /api/workspace/bundle` —
**Arbeitsbaumstand, kein Git**; `loadRuntimeWorkspaceBaseProject` wurde nicht verwendet.

**4 — Messobjekt.** `~/ma/ma-conformance-testrepo` @
`0d651041ed87dd03f2f78359713633fac01c0a66` (Tag `baseline`), Arbeitsbaum **clean**, **kein
`.triton/`** vorhanden — der Soll-Editor ist nicht benutzt worden, er hätte sonst
`<workspace>/.triton/target.ilograph.yaml` **in das Messobjekt** geschrieben
(`editor/src/conformance/loadProject.ts:148-161`). Alle drei Punkte am 02.09.2026 rein
lesend nachgemessen und nach dem Ablegen erneut bestätigt.

**5 — Handlung.** `workspacePath` `/home/haasentimo/ma/ma-conformance-testrepo`
(Repowurzel), Tab `ma-conformance-testrepo`, **kein Drilldown** — belegt über den
Downloadnamen, siehe Prüfung 3. Seitenpanel „YAML" → „Export full YAML".

| Angabe | Wert |
|---|---|
| Zeitstempel (mtime der Downloaddatei) | **2026-09-02 10:57:46.432965905 +0200** |
| Originaler Downloadname | `ma-conformance-testrepo.full.ilograph.yaml` |
| Grösse | 42 959 B |
| SHA256 | `146dbb055e059b9dd948b27e185f33a2cb56557a534c55e0daf983c892336673` |

**6 — Geltungsvermerk, verbindlich** (wörtlich aus §3a-1): „Der Exporter **hat sich seit
der Z1-Fixture geändert** (Z1-Protokoll **T-Z1-4**: drei Commits nach dem Fixture-Export,
einer davon semantisch). Der Z2-Export bezeugt daher den **Exporterstand vom
Erzeugungsdatum**. Jede Aussage ‚gleicher deterministischer Pfad wie in Z1' trägt **diesen
Vorbehalt**." Ob T-Z1-4s Begründung den Exportpfad überhaupt berührt, ist nach §3a-1 offen
und wird hier nicht entschieden.

**Warum diese Protokollierung so ausführlich ist.** Die Erzeugung ist eine **UI-Handlung
ohne Commit**; es gibt keinen Erzeuger-Commit, auf den verwiesen werden könnte. Bei Z1
musste D1 den Erzeuger-Commit deshalb als **„nicht entscheidbar"** ausweisen
(`d1_bericht_fixture_provenienz.md` §4). Für Z2 wird stattdessen die Sitzung **vollständig
vor dem Freeze** protokolliert — das ist die in §3a-1 registrierte Verbesserung gegenüber
Z1, und sie trägt nur, solange dieser Block hier steht.

## Prüfungen — Ergebnisse (Auftrag S2b-2, 02.09.2026)

| # | Prüfung | Gegenprobe | Gelesener Wert | Urteil |
|---|---|---|---|---|
| 1 | Identität: SHA256 | `146dbb05…36673` | `146dbb055e059b9dd948b27e185f33a2cb56557a534c55e0daf983c892336673` | **trifft** |
| 1 | Identität: Bytes | 42 959 | 42 959 | **trifft** |
| 1 | Identität: Zeilen | 988 | 988 | **trifft** |
| 2 | Top-Level-Schlüssel und Reihenfolge | `description`, `resources`, `perspectives` | `description`, `resources`, `perspectives` | **trifft** |
| 2 | Knotenschlüssel (Vereinigung über alle Knoten) | genau die acht: `children`, `id`, `name`, `subtitle`, `x-triton-inner-artefacts`, `x-triton-node-type`, `x-triton-package-scope`, `x-triton-project-kind` | die acht **plus zwei weitere**: `x-triton-inner-artefact-relations`, `x-triton-cross-artefact-relations` | **ABWEICHUNG** — siehe unten |
| 2 | Perspektivschlüssel | `color`, `name`, `orientation`, `relations`; `name: dependencies` | zeichengleich; eine Perspektive | **trifft** |
| 2 | Relationsschlüssel | genau `from`, `to`, `label`; `label` durchgehend `imports` | genau diese drei; Labelmenge `{imports}` | **trifft** |
| 2 | Schlüssel je inneres Artefakt | genau `id`, `name`, `subtitle` | genau diese drei, in **allen** 102 Einträgen (eine einzige Schlüsselform) | **trifft** |
| 3 | `detail = 'slim'`: verbotene Schlüssel | keiner von `x-triton-declaration`, `x-triton-constructor-signatures`, `x-triton-method-signatures`, `x-triton-source-file`, `x-triton-source-row` | `grep -nE` über die ganze Datei: **leer** (Exit 1) | **trifft** |
| 3 | `scopeContainerId` nicht gesetzt: Wurzelressourcen | genau 1 | **1** (`depot`) | **trifft** |
| 3 | `scopeContainerId` nicht gesetzt: Downloadname | kein Zwischensegment zwischen Titel und `.full.ilograph.yaml` | `ma-conformance-testrepo.full.ilograph.yaml` — Titel direkt gefolgt von `.full.ilograph.yaml`; `App.vue:1411` hängte bei gesetztem Scope `.<leaf>` an (`scopeLeaf = entry.scopeId ? '.'+… : ''`) | **trifft** |
| 3 | `fileLineCounts` nicht durchgereicht | kein `subtitle` mit `loc`-Suffix | 0 von 73 `subtitle`s enthalten `loc`; Muster durchgehend `package · N folders` bzw. `module · N artefacts` | **trifft** |
| 3 | `pythonSourceRoots` korrekt erkannt | keine Id mit Präfix `src.`; alle Ids beginnen mit `depot` | 0 Ids mit `src.`; **0** Ids ohne Präfix `depot` (73 von 73) | **trifft** |
| 4 | Zahl der Relationen in `perspectives[0].relations` | **81** (Modulkanten der Clean-Baseline, `00_stand_und_entscheidungen.md` §7) | **81** | **trifft** |
| 4 | eindeutige `(from,to)`-Paare | — | **81** (also keine Dublette; `containerImportRelations` dedupliziert) | — |
| 4 | Selbstkanten | 0 | **0** | **trifft** |
| 5 | Knoten mit `x-triton-project-kind: module` | (drei Gegenproben, siehe unten) | **50** | siehe unten |
| 5 | Knoten mit `x-triton-node-type: package` | — | **23** | siehe unten |
| 5 | maximale Verschachtelungstiefe | — | **5** | siehe unten |
| 7 | Bytegrösse | — | **42 959 B** | berichtet |
| 7 | Zeilenzahl | — | **988** | berichtet |
| 7 | Tokenzahl | — | **nicht gemessen** — siehe unten | **nach S2c verschoben** |
| 8 | Geheimnisprobe `grep -nE 'sk-or-\|sk-ant-\|Bearer \|api[_-]?key'` | leer | **leer** (Exit 1) | **trifft** |

### Prüfung 2 — die eine Abweichung, gemeldet und nicht korrigiert

Das Ist-Modell trägt **zwei Knotenschlüssel, die die Z1-Fixture nicht kennt** und die in der
in §3a-1 aufgezählten Achtermenge nicht vorkommen:

| Schlüssel | Knoten mit dem Schlüssel | Einträge gesamt | Schlüssel je Eintrag | Labelmenge |
|---|---|---|---|---|
| `x-triton-inner-artefact-relations` | 1 von 73 | 4 | `from`, `to`, `label` | `extends` |
| `x-triton-cross-artefact-relations` | 5 von 73 | 8 | `from`, `to`, `label` | `extends` |

Träger sind ausschliesslich Modulknoten. Beispiel:
`{from: depot.core.errors::class:NotFoundError, to: depot.core.errors::class:DepotError,
label: extends}`. Die Einträge sind **Vererbungskanten zwischen inneren Artefakten**, nicht
Importkanten; sie stehen **ausserhalb** von `perspectives[0].relations` und ändern die Zahl
81 aus Prüfung 4 nicht.

**Nicht korrigiert, nicht nachbearbeitet, nicht gedeutet.** Festgehalten wird nur: die
Eingabe trägt zwei Schlüssel, die in der Achtermenge des §3a-1 nicht vorkommen.

~~Die Formidentität mit der Z1-Fixture ist in diesem einen Punkt **nicht** gegeben. Das ist
genau der Fall, den der Geltungsvermerk (§3a-1, T-Z1-4) vorgesehen hat — der Exporter hat
sich seit der Fixture geändert. Ob diese beiden Schlüssel die Änderung sind, ist hier
**nicht entschieden**.~~ — **überholt am 02.09.2026 (Auftrag S2c-1)** durch **FASSUNG A**
(§3a-1, Amendment 02.09.2026, Commit **`8fa6173`**, Auftrag S1-A1b).

**Neue Fassung (FASSUNG A).** Die **Formidentität ist NICHT verletzt.** Der Exporter emittiert
die beiden Knotenschlüssel **nur bei nichtleerem Inhalt** (`codeModelToIlograph.ts:224-225`);
die rein lesende Vorablesung an `fixtures/rich_repo` (`ma-llm-arch-extractor` @ `5c0b65a`)
ergibt **4 von 14** Klassendefinitionen mit Basisklasse und davon **0** mit einer
**fixtureeigenen** Basisklasse. Das Merkmal war an der Z1-Fixture also **gar nicht
auslösbar** — die Abweichung ist **ohne Annahme einer Exporter-Änderung** erklärt, und
**T-Z1-4 wird hierfür NICHT in Anspruch genommen**. Der Geltungsvermerk aus §3a-1
(Exporterstand vom Erzeugungsdatum) bleibt **unberührt**; er wird durch diesen Befund weder
gestützt noch aufgehoben.

### Prüfung 5 — Modulabdeckung neben den drei Gegenproben

| Gegenprobe | Quelle | Wert | Gelesen am Artefakt | Differenz |
|---|---|---|---|---|
| `.py`-Dateien im Repo | §7 („Dateien 73") | **73** | **73 Knoten** insgesamt | **0** |
| inhaltstragende Module | §7 („davon inhaltstragend 50") | **50** | **50** mit `x-triton-project-kind: module` | **0** |
| Zeilen im Clean-Control-Set | `data/soll/control_files.txt` | **52** | **50** Modulknoten | **−2** |

Ferner: **23** Knoten mit `x-triton-node-type: package` — das ist zeichengleich die Zahl der
`__init__.py` aus §7 („davon `__init__.py` 23"). 50 + 23 = 73 = Zahl der Knoten.
Maximale Verschachtelungstiefe **5** (Wurzel `depot` = Tiefe 1).

**Ohne Deutung und ohne Anpassung**, wie beauftragt. Die Zahlen müssen sich nach §3a-1
nicht deckungsgleich abbilden: leere `__init__.py` bilden auf Paketnamen ab
(`pythonCodeModel.ts`), das Control-Set schliesst nach Protokoll §5 Rev. 17 nur *leere*
`__init__.py` aus. Die Differenz −2 wird hier nur festgestellt.

### Prüfung 7 — die Tokenzahl fehlt und gehört nach S2c

`tools/z1_tokenizer.py` ist auf diese Datei **ohne Anpassung nicht gültig anwendbar**. Sein
eigener Wächter weist sie ab:

```
assert_ascii: TokenizerUnavailable — ist_modell.yaml is not pure ASCII;
              the ASCII split pattern would be wrong
```

Grund ist ein einziges Zeichen: das `·` in jedem `subtitle` (`package · 4 folders`). Das
Werkzeug rendert `\p{L}`/`\p{N}` des qwen2-Prätokenizers als `[A-Za-z]`/`[0-9]` und
dokumentiert selbst, dass das **nur für reinen ASCII-Text exakt** ist. Ein Aufruf von
`count()` unter Umgehung des Wächters liefert **8 438** — diese Zahl ist **kein gültiger
Messwert** und wird hier nur genannt, damit nachvollziehbar ist, was geprüft wurde.

**Das Werkzeug wurde nicht angepasst.** ~~Die Messung gehört nach **S2c**; §3b sieht die
Parametrisierung ohnehin vor („parametrisiert, nicht neu geschrieben").~~ — **überholt am
02.09.2026 (Auftrag S2c-1)**: der Halbsatz zur Parametrisierung ist durch das Amendment
**§3b (a)–(e)** vom 02.09.2026 (Commit **`8fa6173`**, Auftrag S1-A1b) **überholt** — das
Messinstrument der Grössenregel ist **ausgewechselt**, nicht parametrisiert worden.
**Neue Fassung:** primäre Messgrösse ist nach **§3b (a)** die **serverseitig gemeldete
Prompt-Tokenzahl** (`usage.prompt_tokens`, Kaltlauf `max_tokens: 1`, lokaler Endpunkt);
`tools/z1_tokenizer.py` wird **nicht** parametrisiert und **nicht** umgebaut — seine Tore
G1-G4 tragen die Z1-Hochrechnung (§3b (d)). Der Satz „Das Werkzeug wurde nicht angepasst"
bleibt gültig und ist seit dem Amendment nicht mehr Aufschub, sondern **Regel**. Die Messung
ist am 02.09.2026 in **S2c-1** erfolgt — Block **Tokenmessung** unten. Die **Wegeleiter aus
§3 Punkt 11 / §3b ist hier NICHT angewandt und keine Stufe gezogen.**


## Tokenmessung `eingaben/ist_modell.yaml` — Block `messungen/` (Auftrag S2c-1, 02.09.2026)

**Was hier steht und was nicht.** Der Block trägt **Instrumentenmessungen nach §3b (a)**,
**keine Z2-Läufe**. Die Kaltläufe zählen **gegen kein Z2-Budget** (§2: sechs Läufe, drei je
Zelle), sind **nicht als Lauf archiviert**, und ihre **Ausgabe ist nicht gelesen und nicht
bewertet** worden — `choices[*].message.content` wird vom Werkzeug ungelesen verworfen.
Abgelegt sind ausschliesslich die in §3b (a) genannten Angaben. Rohdatensatz:
`messungen/tokenmessung_2026-09-02.json`.

**Werkzeug.** `tools/measure_prompt_tokens.py` — stdlib-only, ein Aufruf gegen
`http://localhost:11434/v1/chat/completions`, `temperature: 0`, `max_tokens: 1`, ohne
`response_format`; gelesen wird **ausschliesslich** `usage.prompt_tokens` und
`usage.completion_tokens`. Es **zählt nicht selbst**, es liest, was der Server meldet. Es ist
**nicht** `tools/z2_tokenizer.py` (§3b (d)) und ersetzt dieses nicht: jenes künftige Werkzeug
muss die erwartete Zahl **ohne Modell-Call** liefern. `tools/z1_tokenizer.py` und
`tools/check_z1_delivery.py` sind **unverändert**.

**Kaltlaufregel.** Vor **jeder** der drei Messungen lief `ollama stop qwen2.5-coder:7b`.
Grund ist der in `check_z1_delivery.py` registrierte: Ollama meldet **neu ausgewertete**
Token; ein warmes KV-Cache-Präfix senkt die Zahl legitim (Z1: `attempt_1` meldete 1 065 nach
den 2 050 von `attempt_0`, auf der **längeren** Konversation).

### Ergebnisse M1–M4

| # | Nutzlast | Nachrichtenstruktur | gemeldet | netto | Kürzungsdetektor |
|---|---|---|---|---|---|
| **M1** | Literal `x` (1 B) | 1 × `user` | **30** | — (M1 **ist** die Basis B) | **gültig** |
| **M2** | Z1-Prompt `cb2fcefd…`, 18 842 B | 2 × (`system`, `user`) | **4 281** | **4 252** | **gültig** |
| **M3** | `eingaben/ist_modell.yaml`, 42 959 B, SHA256 `146dbb05…36673` | 1 × `user` | **8 467** | **8 438** | **gültig** |
| **M4** | — (Auswertung über M2 und M3, kein eigener Aufruf) | — | — | — | beide **gültig** |

**Nettozahl = `gemeldet − B + tokens("x")`** mit **B = 30** aus M1 und der ausdrücklichen
**ANNAHME `tokens("x") = 1`** — diese eine Token ist **angenommen, nicht gemessen**; jede
Nettozahl oben trägt sie. **B wird roh berichtet.** B umfasst das Chat-Template und einen
etwaigen **Standard-System-Prompt** des Modells (`ollama show` zeigt „You are Qwen, created by
Alibaba Cloud…"); **welcher Anteil auf welches entfällt, ist nicht gemessen** und wird hier
nicht behauptet.

### M2 — das Tor der Messkette: **getroffen, exakt**

Gemessen wurde `data/z1/k2_trunkiert/run0/extractor/attempts/attempt_0/prompt.txt` (SHA256
`cb2fcefddbbb1f2e81c62bc4b4231b458d12bfcc0948d3764dad7f287db0ee2d`, 18 842 B — vor der
Messung rein lesend geprüft, Datei nicht angefasst), zerlegt nach der **zeichengleichen
Trennregel von `check_z1_delivery.py`** (`SYSTEM_MARK '### system\n'`,
`USER_MARK '\n### user\n'`) in die zwei Nachrichten, die der Extractor baut. Die beiden
Teile lagen im Scratchpad und sind **nicht archiviert**; ihre SHA256 stehen im Rohdatensatz.

| Angabe | Wert |
|---|---|
| Gegenprobe (`z1_protokoll` §3.3 (6); `check_z1_delivery.py` `TOKENS_REFERENCE`) | **4 281** |
| gemessen | **4 281** |
| Differenz | **0** |
| Urteil | **TREFFER EXAKT — die Messkette ist VALIDIERT** |

**Fensterunabhängigkeit belegt.** 4 281 wurde am 31.08.2026 unter Fenster **16 384** gemeldet
und wird hier unter Fenster **32 768** zeichengleich gemeldet. Die gemeldete Prompt-Tokenzahl
ist damit **fensterunabhängig, solange keine Kürzung eintritt**. Der Gegenfall ist aktenkundig
und ist der Grund für den Detektor: 4 281 gesendet, **2 050 gemeldet** unter dem Vorgabefenster
4 096, **ohne Fehler und ohne Logzeile** (`data/z1/MANIFEST.md`, Nachtrag 31.08.2026).

### M4 — Kürzungsdetektor nach §3b (b)

Regel: ungültig bei **Gleichstand** mit dem gesetzten Fenster oder **weniger als 64 Token**
Abstand darunter. Fenster **32 768** → **Verdachtsbereich ab 32 705**.

| Messung | gemeldet | Abstand zum Fenster | Urteil |
|---|---|---|---|
| M2 | 4 281 | 28 487 | **gültig** |
| M3 | 8 467 | 24 301 | **gültig** |

**Eine additive Teilmessung nach §3b (c) war NICHT nötig** und wurde **nicht durchgeführt**;
ein **N** ist folglich nicht ausgewiesen, weil nicht geteilt wurde.

### Wirksames Fenster — erstmals abgelesen

S0-7 hatte die Frage ausdrücklich offen gelassen, weil ohne residente Instanz nichts zu
bezeugen war. Nach M1 ist das Modell resident; `ollama ps` liest dann:

```
NAME                ID              SIZE      PROCESSOR         CONTEXT    UNTIL
qwen2.5-coder:7b    dae161e27b0e    6.8 GB    8%/92% CPU/GPU    32768      4 minutes from now
```

**CONTEXT = 32 768** — erwartet 32 768, **trifft**. **PROCESSOR = `8%/92% CPU/GPU`**: die
Instanz liegt zu 92 % auf der GPU und zu 8 % auf der CPU. Dieselbe Zeile stand nach M2 und
nach M3. Keine Messung ist als fensterunklar zu kennzeichnen.

### Umgebungsänderung — datiert protokolliert (§3b (b))

Das Kontextfenster ist **am 02.09.2026 von 16 384 auf 32 768 gehoben** worden; die Änderung
liegt **nach** Z1s Messung. Sicherungskopie `context.conf.bak-16384` im selben Drop-in-
Verzeichnis, beide Dateien **52 B**. **Die mtime der Sicherung ist durch `cp` auf den
02.09.2026 gesetzt worden** und bezeugt daher **nicht** das Alter des gesicherten Standes; der
**Originalzeitstempel 31.08.2026 19:53** ist im archivierten Bericht
`docs/repo-kontext/s0_bericht_z2_sondierung.md` bezeugt. Gelesener Stand am 02.09.2026, rein
lesend, ohne `sudo`, ohne Änderung an systemd und ohne Dienstneustart durch den Agenten:
`OLLAMA_CONTEXT_LENGTH=32768`, Dienst `active`, `ollama --version` = **0.32.15**.

**Folge für `tools/check_z1_delivery.py`:** seine Konstante `REGISTERED_CONTEXT = 16384`
(Z. 61) ist seit dieser Änderung **umgebungsfremd** — sein Fensterzeuge P3b würde jetzt
abbrechen. Nach §3b (b) ist die Konstante zu **parametrisieren, nicht umzuschreiben**; in
diesem Auftrag ist die Datei **nicht angefasst** worden.

**Die Fensteranhebung FÜR DIE MESSUNG ist ausdrücklich NICHT das Ziehen von Stufe 1 der
Wegeleiter** (§3b (b)). Welche Stufe für die **Läufe** gezogen wird, folgt erst aus der
gemessenen Zahl.

### Beobachtung ohne Deutung: 8 438

Die Nettozahl aus M3 ist **8 438** — zeichengleich mit dem Wert, den `tools/z1_tokenizer.py`
unter **Umgehung** seines ASCII-Wächters lieferte (Prüfung 7 oben). Das wird **nur
festgestellt**. Es macht 8 438 **nicht nachträglich zum Messwert**: der Wert stammt aus einem
Werkzeug, dessen Muster für diesen Text nach seiner **eigenen** Dokumentation nicht exakt ist,
und §3b (a) benennt die **serverseitige** Zahl als Messgrösse. Der Messwert dieses Blocks ist
die **gemeldete** Zahl **8 467**; 8 438 ist deren Nettoform unter der Annahme
`tokens("x") = 1`. **Gedeutet wird hier nichts.**

### Was dieser Block NICHT tut

- **Die Wegeleiter (§3 Punkt 11 / §3b) ist NICHT angewandt; keine Stufe ist gezogen.** Die
  Stufenentscheidung fällt in **S2c-2**, wenn die zweite Eingabe gemessen ist.
- **Die zweite B1-Eingabe `eingaben/input_facts.json` (§3a-2) FEHLT weiterhin.** Ohne sie ist
  die Summe der B1-Eingabe nicht gemessen, sondern nur abgeleitet — und eine Abgeleitete
  entscheidet keine Stufe.
- **`eingaben/ist_modell.yaml` ist nicht angefasst** worden: SHA256 vor und nach der Messung
  `146dbb05…36673`, `eingaben/SHA256SUMS` unverändert. `data/z1/` ist rein lesend geblieben.


## Extractor-Laufzeit — Rekonstruktion und Validierung (Auftrag S2a, 02.09.2026)

**Zweck.** Vorbedingung der **zweiten B1-Eingabe** nach §3a-2: `eingaben/input_facts.json`
wird von `llm_arch.facts.extractor` erzeugt. Nach **S0-6c** war auf diesem Rechner **kein**
Interpreter vorhanden, der `pydantic` oder `openai` importieren kann; die am 31.08.2026
verwendete Umgebung ist **in keinem Artefakt lokalisiert**. Dieser Block bezeugt die
hergestellte Ersatzumgebung und ihr Validierungstor. **Die Eingabe selbst ist damit noch
nicht erzeugt** — sie fehlt weiterhin (siehe Tabelle oben, §3a-2).

### Ort, Interpreter, Aufrufform

| Angabe | Wert |
|---|---|
| Venv | `~/ma/venv-extractor` — **ausserhalb aller Repositorien**, nicht im Repo abgelegt |
| Interpreter | `~/ma/venv-extractor/bin/python`, **Python 3.12.3** |
| `pip` | 24.0 (aus `ensurepip` des Venv; systemweit ist **kein** `pip` vorhanden) |
| Extractor-Paket | **nicht installiert** — kein `pip install -e .`, das schriebe `*.egg-info` in das Messgegenstands-Repo |
| Aufrufform | `PYTHONPATH=~/ma/ma-llm-arch-extractor/src ~/ma/venv-extractor/bin/python …` |

Ausserdem `PYTHONDONTWRITEBYTECODE=1` bei jedem Lauf gegen das Extractor-Repo, damit kein
`__pycache__` neu geschrieben wird.

### Gepinnte und nicht gepinnte Versionen, je mit Quelle

Quellenvorrang war **(c) Lockfile → (a) Laufmanifest → (b) `pyproject.toml`**.

| Paket | Version | Quelle |
|---|---|---|
| Python | **3.12.3** | **(a)** `data/z1/k2/run0/run_manifest.json`, `vorbedingungen.environment.python` |
| `pydantic` | **2.13.5** | **(a)** `…environment.pydantic` — `==`-Pin |
| `openai` | **3.6.0** | **(a)** `…environment.openai` — `==`-Pin |
| `ruamel.yaml` | 0.19.1 | **NICHT GEPINNT** — (b) nennt nur `ruamel.yaml>=0.18`; von pip aufgelöst |
| `typer` | 0.27.2 | **NICHT GEPINNT** — (b) nennt nur `typer>=0.12`; von pip aufgelöst |
| 18 transitive Pakete | siehe `pip freeze` | **NICHT GEPINNT** — keine Quelle nennt eine Version |

**Quelle (c) existiert nicht.** Im Extractor-Repo @ `5c0b65a` gibt es **keine**
`requirements*.txt`, `uv.lock`, `poetry.lock` oder `requirements.lock`
(`git ls-files | grep -iE 'requirement|lock'` ohne Treffer, Exit 1; `find` über den
Arbeitsbaum ohne Treffer). Die **vorrangige** Quelle fehlt also, und die Pins stammen aus
dem Laufmanifest.

**Nicht gepinnt, vollständig:** `ruamel.yaml`, `typer`, `annotated-doc`, `annotated-types`,
`anyio`, `h11`, `httpcore2`, `httpx2`, `idna`, `jiter`, `markdown-it-py`, `mdurl`,
`pydantic_core`, `Pygments`, `rich`, `shellingham`, `sniffio`, `truststore`,
`typing-inspection`, `typing_extensions` — **20 von 22** Paketen im `pip freeze`.
Die `dev`-Extras (`pytest>=8.0`, `tiktoken>=0.7`) sind **nicht installiert**.

**Importprobe.** `import pydantic, openai, llm_arch` und
`from llm_arch.facts.extractor import extract_repo` laufen durch; aus dem Import gelesen:
`pydantic 2.13.5`, `openai 3.6.0` — **zeichengleich zu (a)**, keine Abweichung.

### Datei der Pins

`tools/z2_extractor_requirements.txt` — wörtlicher `pip freeze` mit Kopfkommentar
(Zweck, Datum, Quelle je Pin, Rekonstruktionsvermerk).
SHA256 **`78c6401cd53ae3350928918626a5ab2bdc6bd745d279e76107bae54db2776d43`**.
Das Venv selbst liegt **nicht** im Repositorium.

### Extractor-Repo

`~/ma/ma-llm-arch-extractor` @ **`5c0b65a82cc3d8af47c022d779ff63d8a20a9e08`**,
Arbeitsbaum **clean** vor und nach dem Auftrag (`git status --porcelain` leer,
`git clean -nd` ohne Ausgabe). **Nichts angelegt, nichts geändert, nichts committet** —
auch nicht unter `runs/`.

### DAS TOR — bytegleiche Faktenextraktion: **BESTANDEN**

Nachgebildet wurde die Schreibform aus `src/llm_arch/logging/run_logger.py:62-64`, dort
wörtlich:

```python
    (out / "input_facts.json").write_text(
        json.dumps([f.model_dump() for f in facts], indent=2)
    )
```

Also `extract_repo("<extractor>/fixtures/rich_repo")` →
`json.dumps([f.model_dump() for f in facts], indent=2)`, geschrieben mit `write_text`
in eine Datei **unter `/tmp`** (nicht ins Repositorium, nicht ins Extractor-Repo).
`llm_arch.cli` wurde **nicht** verwendet, **kein Modell-Call**, **kein Schlüssel** gelesen
oder gesetzt.

| Vergleich | Bytes | SHA256 | `cmp` |
|---|---|---|---|
| Rekonstruktion (`/tmp`) | **17 048** | `f8976558e498fb374f9ce63c1ec9bfb522a3ceb156ba1e421aeeea79b42afdae` | — |
| `data/z1/k2/run0/extractor/input_facts.json` | **17 048** | dasselbe | **Exit 0 — bytegleich** |
| `data/z1/k2_trunkiert/run0/extractor/input_facts.json` | **17 048** | dasselbe | **Exit 0 — bytegleich** |

Gegenproben des Auftrags: **17 048 B — trifft**; SHA256-Präfix `f8976558e498fb37…` gegen
`data/z1/k2/SHA256SUMS` gelesen (`f8976558e498fb374f9ce63c1ec9bfb522a3ceb156ba1e421aeeea79b42afdae`)
— **trifft**. Faktenrecords: **16** auf beiden Seiten. Kein Unterschied in Zeilenende oder
Kodierung, da byteidentisch.

**Urteil: die Rekonstruktion ist VALIDIERT.**

### REKONSTRUKTIONSVERMERK, verbindlich

Diese Umgebung ist eine **Rekonstruktion** aus `data/z1/k2/run0/run_manifest.json` bzw.
`pyproject.toml`. **Die am 31.08.2026 verwendete Umgebung ist in keinem Artefakt
lokalisiert** und bleibt es. Da das Tor positiv ausgefallen ist, ist die **ÄQUIVALENZ FÜR
DIE FAKTENEXTRAKTION** belegt — **nicht die Identität der Umgebung**. Für jeden anderen
Pfad des Extractors (Abstraktion, Provider, Serialisierung, CLI) trägt dieser Beleg
**nicht**; 20 der 22 Pakete sind nicht gepinnt.

### Was dieser Block nicht berührt

- **`~/ma/venv` (Vergleichsansätze: `grimp`, `import-linter`, `PyTestArch`, `SQLAlchemy`)
  ist unberührt** — nicht angefasst, nicht erweitert, nicht gelesen ausser dem Namen.
- **Keine Installation in die Systemumgebung**; kein `--break-system-packages`, kein
  `--user`, kein `sudo`, kein `apt`.
- `data/z1/` ist rein lesend geblieben; `eingaben/` und `messungen/` sind unverändert.

### ~~Offener Posten~~ **GESCHLOSSEN 02.09.2026**: Provenienz von `5c0b65a` — **Gegenprobe des Auftrags trifft NICHT**

Der Auftrag S2a hiess, hier zu vermerken, der Extractor liege **3 Commits vor `origin/main`**
und `5c0b65a` existiere **nur lokal**. **Das trifft am 02.09.2026 nicht mehr zu.** Rein
lesend gemessen:

```
git rev-parse HEAD        5c0b65a82cc3d8af47c022d779ff63d8a20a9e08
git rev-parse origin/main 5c0b65a82cc3d8af47c022d779ff63d8a20a9e08
git rev-list --left-right --count origin/main...HEAD   ->   0   0
git branch -vv            * main 5c0b65a [origin/main] docs: correct the stale expected.json references
```

**Vorbehalt, und deshalb bleibt der Posten offen:** `origin/main` ist ein **lokaler
Remote-Tracking-Ref**; `.git/refs/remotes/origin/main` trägt mtime **01.09.2026 18:10**.
Gemessen ist also der Stand der letzten Synchronisation, **keine Abfrage gegen GitHub** —
eine solche ist in diesem Auftrag **nicht** durchgeführt worden. Ob `5c0b65a` beim Remote
tatsächlich liegt, ist damit **nicht bezeugt**, nur wahrscheinlich gemacht.
**Nicht angeglichen, nichts gefetcht, nichts gepusht.** ~~Der Posten bleibt beim
Auftraggeber und ist **nicht Gegenstand dieses Auftrags**.~~

**GESCHLOSSEN am 02.09.2026 (Auftrag S1-M1).** Der Vorbehalt ist ausgeräumt: eine Abfrage
**gegen das Remote** — nicht gegen den Tracking-Ref — liefert

```
git ls-remote origin main
5c0b65a82cc3d8af47c022d779ff63d8a20a9e08  refs/heads/main
```

**`5c0b65a` liegt damit beim Remote und der registrierte Z1-Messstand ist remote bezeugt.**
Der Satz aus S2a, der Extractor liege **3 Commits vor `origin/main`** und `5c0b65a`
existiere **nur lokal**, ist endgültig überholt. **Herkunft der Zahl, ausdrücklich:** die
Abfrage ist im **Auftrag S1-M1 vom 02.09.2026 als Ergebnis mitgeteilt** und in diesem Lauf
**nicht erneut ausgeführt** worden — das Extractor-Repo ist hier **nur lesend** und wurde
nicht angefasst (stehende Regel 4). **Nichts gefetcht, nichts angeglichen, nichts
gepusht.**

## Zweite B1-Eingabe `eingaben/input_facts.json` (Auftrag S2c-2, 02.09.2026)

Damit **liegen beide** B1-Eingaben nach §3a. Die Tabelle unter *Zweck des Blocks
`eingaben/`* führt `input_facts.json` noch als **„FEHLT NOCH"** — ~~diese Zeile ist
überholt~~; sie bleibt stehen, weil die Ablage auf ihr registriert wurde. Stand seit dem
02.09.2026: **liegt** (S2c-2).

### Erzeuger, Aufrufargument, Umgebung

| Angabe | Wert |
|---|---|
| Erzeuger | `extract_repo` (`src/llm_arch/facts/extractor.py:103-110`), Serialisierung nachgebildet nach `run_logger.py:62-64` — `json.dumps([f.model_dump() for f in facts], indent=2)`, **ohne abschliessenden Zeilenumbruch**, wie die archivierten Z1-Kopien |
| Aufrufargument | `/home/haasentimo/ma/ma-conformance-testrepo/src` — **zwingend das Unterverzeichnis `src`**, nicht die Repowurzel (§3a-2; `_module_name`, `extractor.py:23-29`) |
| Umgebung | die in **S2a validierte**: `~/ma/venv-extractor/bin/python` 3.12.3, `PYTHONPATH=~/ma/ma-llm-arch-extractor/src`, Pins in **`tools/z2_extractor_requirements.txt`**; `pip freeze` am 02.09.2026 **zeichengleich** zu jener Datei |
| Extractor | `~/ma/ma-llm-arch-extractor` @ `5c0b65a82cc3d8af47c022d779ff63d8a20a9e08`, Arbeitsbaum **clean vor und nach dem Lauf** |
| Messobjekt | `~/ma/ma-conformance-testrepo` @ `0d651041ed87dd03f2f78359713633fac01c0a66`, `git status --porcelain` **leer**, `ls -a \| grep -i triton` **leer**, **vor und nach dem Lauf unverändert** |

**Der Lauf hat in keinem der beiden Fremd-Repos etwas geschrieben.** Die `__pycache__`
des Extractors tragen mtime **31.08.2026 14:46** und sind damit **älter als dieser
Auftrag**; in das Messobjekt-Repo ist nichts geschrieben worden (kein `__pycache__`, kein
`*.egg-info`).

### Gegenproben zur Rohfassung — beide getroffen

| Gegenprobe | Soll | Ist |
|---|---|---|
| Zahl der Records gegen die `.py`-Dateien unter `<testrepo>/src` | 73 | **73** |
| Ids, die mit `src.` beginnen | 0 | **0** |

`eingaben/input_facts_raw.json`: **128 707 B**, 3 605 Zeilen, 73 Records,
SHA256 `85b7a2c1834b4f954a630f3ff3ccf01ebc139a9f51039365b7759f7fbcc28951`.

### Deckungsgleichheit mit dem Ist-Modell — die inhaltliche Verklammerung der zwei Eingaben

Die Gegenprobe aus **§3a-2**: Modulnamenmenge der Faktenbasis gegen die Ids des
Ist-Modells, **bis auf leere `__init__.py` deckungsgleich**. Gemessen rein lesend über
`json` und `yaml.safe_load`:

| Menge | Definition | Erwartet | Gemessen |
|---|---|---|---|
| `M_facts` | alle `module_name` aus `input_facts_raw.json` | — | **73** |
| `M_ist` | Ids der Knoten mit `x-triton-project-kind: module` | 50 | **50** |
| `P_ist` | Ids der Knoten mit `x-triton-node-type: package` | 23 | **23** |

**Beide Differenzen sind LEER:**

```
M_facts \ (M_ist u P_ist)  =  []      (n = 0)
(M_ist u P_ist) \ M_facts  =  []      (n = 0)
```

`|M_ist ∪ P_ist| = 73 = |M_facts|`, und die Mengen sind **identisch**, nicht nur
gleichmächtig. Das ist die **erwartete** Lage und wird hier als Erwartung ausgewiesen:
leere `__init__.py` bilden im Export auf **Paketnamen** ab (`pythonCodeModel.ts`), und
`_module_name` (`extractor.py:23-29`) kürzt `__init__` **ebenfalls** auf den Paketnamen.
**Es gibt keine Abweichung zu melden.**

### Arbeitsteilung der beiden Eingaben — Fassung vom 02.09.2026 (`8fa6173`)

Nach **§3a-2, PRÄZISIERTE FASSUNG (S1-A1b)**:

- Das **Ist-Modell** trägt **Struktur** (Paket-/Modulbaum, innere Artefaktnamen), die
  **deduplizierten Importkanten auf Containerebene** **und — neu registriert — die
  VERERBUNGSKANTEN zwischen Artefakten (`extends`)**: **zwölf** an der Zahl, in
  `x-triton-inner-artefact-relations` (**4**, an 1 von 73 Knoten) und
  `x-triton-cross-artefact-relations` (**8**, an 5 von 73 Knoten), **Träger
  ausschliesslich Modulknoten**, Label **durchgehend `extends`**. Sie stehen
  **ausserhalb** von `perspectives[0].relations` und verschieben die **81 Importkanten
  nicht**.
- Die **Faktenbasis** trägt die **SIGNATUREN**, die im `slim`-Export fehlen.
- **Beides zusammen ist die Evidenzbasis, an der Z2-P gemessen wird.**

**Nachzuziehen, weil Stufe 0b gezogen wurde** (§3b, Stufe 0b, letzter Satz): die
Evidenzbasis in §6 (Z2-P) lautet nun **„Imports (als Kantenmenge des Ist-Modells) +
Signaturen"**. Der Nachzug am Protokoll ist ein **eigener Auftrag**; hier wird er nur
angezeigt.

**ERLEDIGT am 02.09.2026 mit Commit `bf6c6e0`** — der Anzeigetext oben bleibt stehen.
Nachgezogen in **§6 (Z2-P)** und **§3a-2 (Nachtrag 02.09.2026)** auf **„entscheidbar allein
aus den IMPORTKANTEN DES IST-MODELLS und den SIGNATUREN der Faktenbasis"**; der Alttext
steht an beiden Stellen durchgestrichen sichtbar. Mitregistriert ist die Konsequenz: ein
Vorschlag, dessen Prüfbarkeit von einem **externen** Import abhängt, wird unter Z2-P als
**nicht entscheidbar, MIT VERMERK DER URSACHE** geführt — **kein Modellfehler**, sondern
Folge der vorab registrierten Kürzung. **T-Z2-6 und T-Z2-9** sind entsprechend ergänzt.

### Hashes beider Fassungen

| Datei | Bytes | Zeilen | Records | SHA256 |
|---|---|---|---|---|
| `eingaben/input_facts_raw.json` | 128 707 | 3 605 | 73 | `85b7a2c1834b4f954a630f3ff3ccf01ebc139a9f51039365b7759f7fbcc28951` |
| `eingaben/input_facts.json` | 64 245 | 2 391 | 52 | `f670593a7add275c364ebff5a5529cb95a787a10de5e0c80f97cd46574eb282a` |

**Die Rohfassung bleibt abgelegt** — sie ist die **Provenienz** der finalen Fassung: nur
an ihr ist nachprüfbar, was die Leiter weggenommen hat.

## Grössenregel angewandt (Auftrag S2c-2, 02.09.2026)

### Vorregistrierung, wörtlich

> **R1 INSTRUKTIONSBUDGET für Anhang A: OBERGRENZE 1 200 Token, BINDEND.** Anhang A darf
> sie nicht überschreiten; andernfalls wäre die hier gezogene Stufe nachträglich falsch.
> **ZIELGRÖSSE rund 700 Token, NICHT bindend.** Begründung der Zielgrösse: in Z1 kippte
> die Formatgültigkeit an 909 Zeichen Instruktionstext (Z1-Befund, offene
> 901/909-Divergenz) — Instruktionslänge hängt bei diesem Modell nachweislich mit der
> Formatgültigkeit zusammen, und 1 200 Token entsprechen grob dem Fünffachen jener
> Zeichenzahl.
>
> *[NACHZUG 02.09.2026, Commit `bf6c6e0`, Protokoll §3b (f): die Obergrenze dieses Absatzes
> ist ~~**1 200 Token**~~ → **1 000 Token, BINDEND**. Der Zitattext selbst bleibt
> unverändert stehen, weil er die Vorregistrierung aus S2c-2 **wörtlich** wiedergibt; die
> geltende Fassung steht im Abschnitt **„Nachzug R1"** unmittelbar unter diesem Zitat.]*
>
> **R2 PROMPTSPRACHE: ENGLISCH.** Begründung: Z1s Prompt v3 ist englisch (`prompt.py`),
> die Ausgabefelder sind englische Bezeichner, die Eingaben sind englischer Code; die
> Arbeitsregel weist Code und Bezeichner dem Englischen zu. Der Rahmen- und
> Begründungstext von Anhang A ist DEUTSCH, der eingefrorene Prompt steht darin als
> englischer Block.
>
> **R3 NACHRICHTENSTRUKTUR für die Messung und für Z2: ZWEI Nachrichten** — `system`
> trägt die Instruktion, `user` trägt die zwei Eingabeblöcke (Ist-Modell, Faktenbasis),
> analog zu Z1 (`prompt.py` `build_messages`). S3 bestätigt sie in Anhang A; weicht
> Anhang A davon ab, ist die Messung zu wiederholen.

### Nachzug R1 — Obergrenze auf 1 000 Token verschärft (02.09.2026, `bf6c6e0`, §3b (f))

**Dies ist die für Anhang A geltende Fassung des Instruktionsbudgets.** Sie ersetzt den
Zitatblock darüber nicht, sie zieht ihn nach; der Alttext bleibt dort durchgestrichen
sichtbar stehen.

| Grösse | gesetzt 02.09.2026 (S2c-2) | **geltend ab `bf6c6e0`** | Charakter |
|---|---|---|---|
| **R1 OBERGRENZE** | ~~**1 200 Token**~~ | **1 000 Token** | **BINDEND für Anhang A** |
| **R1 ZIELGRÖSSE** | rund 700 Token | **rund 700 Token — unverändert** | **NICHT bindend** |

**Grund, kurz:** der volle Prompt misst bei einer Instruktion von **1 200** Token
**24 104** Token und **überschreitet die Schwelle um 104**; der **gemessene Kipppunkt**
liegt bei **1 096** Token, **1 000 lässt 96 Token Sicherheit** für die Messung des
**tatsächlichen** Anhang A und liegt weiter deutlich über der Zielgrösse. **Erwarteter
voller Prompt bei einer Instruktion von 1 000 Token: rund 23 904 Token** — aus Protokoll
§3b (f) übernommen, hier **nicht nachgerechnet**.

> **DIE SCHWELLE VON 24 000 TOKEN IST UNVERÄNDERT.** Verschärft wurde das
> **Instruktionsbudget**, das erst am 02.09.2026 in S2c-2 gesetzt wurde und **selbst keine
> vorregistrierte Grösse** ist; es zu verschärfen ist deshalb keine Nachverhandlung. Die
> **Schwelle** dagegen **nach Kenntnis der Zahl 24 104** zu bewegen — anzuheben oder durch
> ihre Begründung (Generat-Reserve ≥ 8 000, hier mit 8 664 erfüllt) zu ersetzen — **wäre
> Nachverhandlung und ist ausgeschlossen.**

**Die gemessenen Zahlen dieses Blocks bleiben unverändert.** M5–M9, die Stufen 0 und 0b und
die **24 104** sind **Messwerte**; der Nachzug rechnet sie **nicht um**. Sie gelten weiter
für diejenige Instruktionsgrösse, bei der sie gemessen wurden (**1 200** Token).

### Trennzeilen, wörtlich — sie gelten auch für Anhang A

```
### BLOCK 1 - CURRENT ARCHITECTURE MODEL (Ilograph YAML)
### BLOCK 2 - EXTRACTED CODE FACTS (JSON)
```

Zusammensetzung der `user`-Nachricht, deterministisch:

```python
f"{BLOCK1}\n\n{ist_modell.rstrip()}\n\n{BLOCK2}\n\n{faktenbasis.rstrip()}\n"
```

### Füllinstruktion — an der Obergrenze gemessen, nicht geschätzt

Ein englischer Platzhaltertext, **iterativ auf genau 1 200 Token netto getrimmt**, in
**fünf** Iterationen (1 018 → 1 173 → 1 195 → 1 199 → **1 200**), 1 060 Wörter, 6 634 B,
SHA256 `b1b01448…d6282`. Er dient **ausschliesslich** der Messung, ist **nicht abgelegt**
und ist **nicht Anhang A**. Gemessen wurde damit der ~~**ungünstigste nach R1 zulässige
Fall**~~ — **so galt es bei der Obergrenze 1 200**. **Nachgezogen 02.09.2026 (`bf6c6e0`,
§3b (f)):** seit der Verschärfung liegen die 1 200 Token **über** der geltenden Obergrenze
von **1 000**; die Messung ist damit **konservativ** — sie misst einen Fall, den Anhang A
**nicht mehr ausschöpfen darf**. **Die Messzahlen selbst bleiben unverändert.**

### Messreihe M5–M9

Basiswert **B = 30** aus S2c-1 **nachgemessen und zeichengleich getroffen**.

| Kennung | Gegenstand | gemeldet | netto | Urteil |
|---|---|---|---|---|
| **M5** | `input_facts_raw.json` allein, 1 × `user` | 29 095 | 29 066 | gültig |
| **M6** | **voller Prompt** nach R3, rohe Faktenbasis | ~~16 386~~ | — | **UNGÜLTIG — gekürzt** |
| **M6′** | derselbe Prompt, additiv teilgemessen nach §3b (c), N = 3 | **38 748** | — | gültig, Fehlerschranke ≤ 3 |
| **M7** | Kürzungsdetektor über M5 und M6 | — | — | siehe unten |
| **M8** | voller Prompt **nach Stufe 0** | **27 525** | — | gültig |
| **M9** | voller Prompt **nach Stufe 0 + 0b** | **24 104** | — | gültig |

Die Nettozahl ist `gemeldet − 29` und gilt **nur für Einzelmessungen mit einer
`user`-Nachricht**. Für die **R3-Struktur** ist die **gemeldete** Zahl selbst die
Messgrösse — **sie** steht gegen die Schwelle.

### BEFUND: der Kürzungsdetektor aus §3b (b) ist für die beobachtete Kürzungsart BLIND

**Setup.** §3b (b) erklärt eine gemeldete Zahl für ungültig, wenn sie dem gesetzten
Fenster **gleicht** oder es um **weniger als 64 Token unterschreitet** — Verdachtsbereich
also ab 32 705.

**Resultat.** M6 meldete **16 386** — **16 382 Token unter** dem Fenster, weit ausserhalb
des Verdachtsbereichs. Der registrierte Detektor hätte die Zahl **durchgelassen**. Dass
gekürzt wurde, zeigen zwei andere Kriterien:

1. **Monotonie.** M6 enthält M5 (die Faktenbasis) **vollständig**, dazu Ist-Modell,
   Trennzeilen und Instruktion — und meldet **12 709 Token weniger** als M5 (16 386 gegen
   29 095). Arithmetisch unmöglich ohne Kürzung.
2. **Signatur `Fenster / 2 + 2`.** 32 768 / 2 + 2 = **16 386**, exakt der gemeldete Wert.
   Der **aktenkundige Z1-Gegenfall** trägt dieselbe Signatur: 4 281 gesendet, **2 050**
   gemeldet unter Fenster 4 096 — und 4 096 / 2 + 2 = **2 050**
   (`data/z1/MANIFEST.md`, Nachtrag 31.08.2026; §3b (b)). **Der Server kürzt auf die
   HÄLFTE des Fensters, nicht auf das Fenster.**

**Konsequenz.** §3b (b) ist um diese zwei Kriterien zu ergänzen. Das ist ein **eigener
Auftrag am Protokoll**; hier wird der Befund nur festgestellt. **Für diese Messung ist er
folgenlos**, weil die Kürzung erkannt und nach §3b (c) ersetzt wurde.

**ERLEDIGT am 02.09.2026 mit Commit `bf6c6e0`** — der Anzeigetext oben bleibt stehen.
Registriert in **§3b (b2)/(b3)**: der bisherige Wortlaut von (b) bleibt gültig und bleibt
stehen, ergänzt um zwei **gleichrangige, je hinreichende** Kriterien — **(b2) MONOTONIE**
(enthält eine Nutzlast eine andere vollständig, muss ihre gemeldete Tokenzahl mindestens so
gross sein; der volle Prompt wird stets gegen die Einzelmessung seiner grössten Komponente
geprüft) und **(b3) HALBFENSTER-SIGNATUR** (ungültig bei Gleichstand mit `Fenster / 2 + 2`
oder weniger als 64 Token darunter). Mitregistriert ist die **Evidenzeinordnung**: dass der
Server auf die **halbe** Fenstergrösse kürzt, ist aus zwei Messpunkten **abgeleitet** — als
Regularität gemessen, als Mechanismus **nicht**. **Nachzug an die Lieferzusicherung, in S4
umzusetzen:** der Wächter von `tools/run_z2.py` prüft **(b2) und (b3) mit**, nicht nur den
Gleichstand mit dem Fenster; ein Lauf, dessen gemeldete Prompt-Tokenzahl eines der **drei**
Kriterien erfüllt, **bricht ab und wird nicht als Lauf gezählt**.

### Additive Teilmessung nach §3b (c) — N = 3, dreifach validiert

Der gerenderte Prompt zerfällt **verlustfrei** (`cmp` Exit 0 gegen den gesendeten Text)
in drei Teile:

| Teil | Inhalt | Bytes | gemeldet | Tokens |
|---|---|---|---|---|
| P1 | Füllinstruktion (`system`) | 6 634 | 1 229 | 1 200 |
| P2 | Trennzeile 1 + `ist_modell.yaml` + `\n\n` | 43 018 | 8 484 | 8 455 |
| P3 | Trennzeile 2 + `input_facts_raw.json` + `\n` | 128 751 | 29 109 | 29 080 |

Rahmenkonstante der **Zwei**-Nachrichten-Struktur, eigens gemessen (`system:'x'` +
`user:'x'` meldet **15**): **F₂ = 13**. Sie ist **kleiner** als die Rahmenkonstante der
Ein-Nachrichten-Struktur (F₁ = 29), weil eine eigene `system`-Nachricht den
**Standard-System-Prompt ersetzt**, den der OpenAI-kompatible Pfad sonst einsetzt.

```
M6' = F2 + P1 + P2 + P3 = 13 + 1 200 + 8 455 + 29 080 = 38 748
```

Fehlerschranke **≤ N = 3 Token** an den Teilgrenzen (§3b (c)) — bei einer Schwelle von
24 000 unerheblich. **Die Formel ist an drei ungekürzten Fällen auf das Token genau
validiert:** Kontrollmessung (gemeldet 9 668, gerechnet 9 668), M8 (27 525 / 27 525),
M9 (24 104 / 24 104), Differenz jeweils **0**.

### Rahmungsaufwand

| Grösse | Wert |
|---|---|
| M3 + M5 + 1 200 | 8 467 + 29 095 + 1 200 = **38 762** |
| M6′ (rekonstruiert) | **38 748** |
| **Differenz** | **−14** |

Die Differenz ist **negativ**, und das ist erklärbar, nicht rätselhaft: M3 und M5 tragen
die Rahmenkonstante F₁ = 29 **je einmal**, zusammen 58; der wirkliche Prompt trägt F₂ = 13
**einmal**. Dem stehen die **Trennzeilen** gegenüber: +17 Token für Block 1 (8 455 − 8 438)
und +14 für Block 2 (29 080 − 29 066). Probe: 38 762 − 58 + 17 + 14 + 13 = **38 748**.

### Gezogene und nicht gezogene Stufen

| Stufe | Gezogen? | Zahl vorher → nachher | Begründung und Preis |
|---|---|---|---|
| **0** — Docstrings streichen, leere `__init__.py` auslassen | **JA** | 38 748 → **27 525** (−11 223) | Kostet die Evidenzbasis von Z2-P nichts (§3b). 73 → 52 Records. |
| **0b** — Importblöcke streichen | **JA** | 27 525 → **24 104** (−3 421) | Nötig: Stufe 0 reicht **für keine zulässige Instruktionsgrösse** — selbst bei einer Instruktion von **null** Token bliebe der Prompt bei 26 325 > 24 000. Preis unten. |
| **1** — Fenster 32 768 | **nicht erneut gezogen** | — | **Bereits wirksam** durch die datierte Umgebungsänderung vom 02.09.2026 (S2c-1, Block *Umgebungsänderung* oben). Das Anheben des Fensters **für die Messung** ist nach §3b (b) ausdrücklich nicht das Ziehen von Stufe 1; hier ist es die **Laufumgebung** und steht bereits. |
| **3** — Ausschnitt über `scopeContainerId` | **NEIN** | — | Ändert das **Messobjekt**. Braucht eine Entscheidung des Auftraggebers. |
| **4** — K3-only | **NEIN** | — | Verlöre die **Modellklassen-Achse**. Braucht eine Entscheidung des Auftraggebers. |
| **2** — Signaturen weg | **NEIN** | — | Entwertete **E2/E4**. Braucht eine Entscheidung des Auftraggebers. |

**Reihenfolge innerhalb von Stufe 0, und sie ist nicht beliebig:** die Docstrings werden
**zuerst** entfernt, die Leerheitsprüfung läuft auf dem **schon gestrippten** Record. In
dieser Faktenbasis tragen **alle 23** Paketrecords einen `module_docstring`; auf der
Rohfassung geprüft wäre **keiner** leer und die zweite Hälfte von Stufe 0 ein
**Leerlauf**. Nach dem Strippen sind **21** der 23 leer (die zwei übrigen tragen
`imports` und `functions`) und fallen weg — 73 − 21 = **52**. Das ist die Leerheit von
`substantive_modules` (`extractor.py:113-123`), die das Protokoll in Stufe 0 meint.

### Preis von Stufe 0b — an dieser Faktenbasis gemessen, nicht angenommen

Der in §3b registrierte Preis nennt **Aliasnamen**, die `names[]`-Listen von
`from X import Y`, **relative Importe** und — als eigentlichen Preis — **externe
Importe**. Gemessen am Messobjekt:

| Posten | Zahl |
|---|---|
| Importfakten in den 52 behaltenen Records | **90** |
| davon `import x as y` (Alias gesetzt) | **0** |
| davon `from X import …` mit `names[]` | **0** |
| davon relative Importe (`relative_level > 0`) | **0** |
| davon mit Ziel **innerhalb** des Messobjekts (`depot.*`) | **81** |
| davon mit Ziel **ausserhalb** (extern) | **9** |

Das Testrepo verwendet **ausschliesslich** die Form `import a.b.c`. **Drei der vier
registrierten Preisposten sind an dieser Eingabe also leer.** Es bleibt **einer**:

- **Die 81 internen Importfakten sind vollständig ersetzt.** Das Ist-Modell führt
  **81 Relationen** mit **81 eindeutigen `(from,to)`-Paaren** — Zahl für Zahl dieselbe
  Menge. Hier geht **nichts** verloren.
- **Die 9 externen Importe gehen verloren.** Vollständig: 8 × `sqlalchemy.orm`
  (`depot.billing.models.invoice_models`, `…invoice_view_models`,
  `depot.identity.models.customer_models`, `…customer_view_models`,
  `depot.orders.models.order_line_models`, `…order_line_view_models`,
  `depot.orders.models.order_models`, `…order_view_models`) und 1 × `typing`
  (`depot.core.ports`). Externe Ziele haben **keinen Container** und stehen im Export
  **nicht**. Framework-Typen bleiben über die **Signaturen** sichtbar, nicht mehr über
  die Importliste.

### Endzahl gegen die Schwelle — und der Punkt, an dem eine Entscheidung nötig ist

| Grösse | Wert |
|---|---|
| Schwelle (§3b) | **24 000** |
| **M9 bei R1-Obergrenze 1 200** | **24 104** — **überschritten um 104** |
| M9 bei R1-Zielgrösse 700 | **23 604** — gehalten, 396 Reserve |
| Kipppunkt | Die Schwelle hält genau dann, wenn Anhang A **höchstens 1 096 Token** trägt |
| **M9 bei der geltenden R1-Obergrenze 1 000** *(Nachzug 02.09.2026, `bf6c6e0`, §3b (f))* | **rund 23 904** — gehalten; **Erwartungswert aus dem Protokoll übernommen, nicht gemessen und nicht nachgerechnet** |
| Reserve bis zum Fenster 32 768 | **8 664** — die verlangten **≥ 8 000** für das Generat sind **auch bei 1 200** erfüllt |

**Stufe 0 und 0b zusammen halten die Schwelle bei der bindenden Obergrenze R1 NICHT** —
sie fehlen **104 Token**. Bei der (nicht bindenden) Zielgrösse von rund 700 Token hielte
sie mit 396 Token Reserve. **Die Reservebedingung von ≥ 8 000 Token für das Generat — der
sachliche Zweck der Schwelle — ist in beiden Fällen erfüllt.**

~~**Die Entscheidung liegt beim Auftraggeber**~~ — **DIE ENTSCHEIDUNG IST GEFALLEN,
02.09.2026, `bf6c6e0`, §3b (f); siehe den Vermerk unter der Liste.** Sie ist **nicht** die
Wahl einer weiteren Leiterstufe, solange eine billigere Möglichkeit offensteht:

1. **R1 verschärfen**: bindende Obergrenze von ~~1 200~~ auf ~~**≤ 1 096 Token**~~
   — **gewählt und schärfer gefasst: 1 000 Token** (02.09.2026, `bf6c6e0`, §3b (f)). Kostet
   **keine** Stufe, ändert **nicht** das Messobjekt, verliert **nicht** die
   Modellklassen-Achse, entwertet **nicht** E2/E4 — und liegt oberhalb der ohnehin
   angestrebten Zielgrösse von 700. **Das ist die naheliegende Lösung.**
2. **Stufe 3, 4 oder 2 ziehen.** Jede trägt den in §3b registrierten Preis. Diese drei
   sind in diesem Auftrag **ausdrücklich nicht ausgeführt** worden.

**ENTSCHEIDUNG, 02.09.2026, Commit `bf6c6e0`, §3b (f): Möglichkeit 1 ist gewählt — und
schärfer als hier vorgeschlagen.** Die bindende Obergrenze steht **nicht** bei ≤ 1 096,
sondern bei **1 000 Token**; die **96 Token** Abstand zum Kipppunkt sind die Sicherheit für
die Messung des **tatsächlichen** Anhang A. **Möglichkeit 2 ist nicht gewählt:** die Stufen
**3, 4 und 2 bleiben NICHT gezogen** (§3b (f), Tabelle „Gezogener Stand der Wegeleiter").
**Auflage an S3, dort zwingend vorab registriert:** nach dem Schreiben von Anhang A wird der
**volle** Prompt mit dem **tatsächlichen** Instruktionstext gemessen — Verfahren (a)–(c),
Detektor **einschliesslich (b2) und (b3)**; hält er die **24 000** nicht, wird **Anhang A
gekürzt, NICHT die Schwelle bewegt**. Messung und Ergebnis gehen vor dem Freeze nach
`data/z2/messungen/` und in dieses Manifest.

**Bis zur Entscheidung steht `input_facts.json` als Ausgabe von Stufe 0 + 0b fest** — sie
ist von der Entscheidung unabhängig, weil Stufe 0b, wie oben gezeigt, für **jede**
zulässige Instruktionsgrösse unausweichlich ist.

### Werkzeug `tools/reduce_facts.py`

Neu in diesem Auftrag, **stdlib-only**, Flags `--drop-docstrings`, `--drop-empty-init`,
`--drop-imports`, Ein- und Ausgabepfad, Serialisierung `json.dumps(..., indent=2)` ohne
abschliessenden Zeilenumbruch wie das Original. **Es bearbeitet nie an Ort und Stelle**
und fasst seine Eingabe nicht an. **Deterministisch, belegt:** zweimal auf dieselbe
Eingabe angewandt liefert es bytegleiche Ausgabe (`cmp` Exit 0, SHA256 beide Male
`f670593a…eb282a`). **Keine Handbearbeitung der Datei hat stattgefunden.**

Kommandozeilen der zwei gezogenen Stufen:

```
python3 tools/reduce_facts.py --drop-docstrings --drop-empty-init \
    data/z2/eingaben/input_facts_raw.json <zwischenfassung>
    -> 73 Records -> 52 Records, 77 592 B, sha256 ea884ee6…e1395  (NICHT abgelegt)

python3 tools/reduce_facts.py --drop-docstrings --drop-empty-init --drop-imports \
    data/z2/eingaben/input_facts_raw.json data/z2/eingaben/input_facts.json
    -> 73 Records -> 52 Records, 64 245 B, sha256 f670593a…eb282a  (abgelegt)
```

## Anhang A gemessen (Auftrag S3, 02.09.2026)

Dieser Block hält die von **§3b (f)** verlangte Messung fest: **nach** dem Schreiben von
Anhang A wird der **volle Prompt mit dem TATSÄCHLICHEN Instruktionstext** gemessen, mit
dem Detektor **einschliesslich (b2) und (b3)**, und **vor** dem Freeze abgelegt. Fundstelle
der Datensätze: `data/z2/messungen/tokenmessung_2026-09-02.json`, Kennungen **M10, M10g,
M11a, M11, M12**; die Datensätze **M1–M9 sind unverändert geblieben**.

### Der gemessene Wortlaut

| Angabe | Wert |
|---|---|
| **Was** | die `system`-Nachricht: der Wortlaut von **Anhang A, A3** |
| **SHA256** | `60ae777bf40ccd6bfc25ba2847b8d47fede7c0f3be0ae5582f88d05b7a4ed2a0` |
| **Grösse** | **2 283 B**, **47 Zeilen** |
| **Als Datei abgelegt** | **nein** — der Wortlaut **IST** Teil des Protokolls (`docs/protokolle/z2_protokoll_regelableitung.md`, Anhang A, A3); genau wie die Füllinstruktion aus S2c-2 ist er kein eigener Messeingang und erscheint in keinem `SHA256SUMS` |

Der SHA256 ist **derselbe** für den aus dem Protokoll extrahierten Promptblock und für den
gemessenen Text — die Messung gilt also **dem eingefrorenen Wortlaut**, nicht einer Kopie.

### M10 — die Instruktion allein, gegen R1

| Kennung | Nachrichtenform | gemeldet | netto | gegen R1 |
|---|---|---|---|---|
| **M10** | eine `system`-Nachricht | **509** | **480** | **Obergrenze 1 000 GEHALTEN** (Reserve 520) · **Zielgrösse rund 700 GEHALTEN** (Reserve rund 220) |
| **M10g** | eine `user`-Nachricht (Gegenprobe) | **530** | **501** | dasselbe Urteil; **501 liegt 595 Token unter dem Kipppunkt 1 096** |

Die Nettozahl ist `gemeldet − 29` (Basiswert **B = 30** aus M1). **Vorbehalt, ausdrücklich:**
diese Konvention ist in S2c-1 an der **`user`**-Form gesetzt; der Rahmenaufwand der
**`system`**-Form ist **nicht eigens gemessen**. Deshalb steht **M10g** daneben — sie ist
mit der auf **1 200 netto** getrimmten Füllinstruktion **unmittelbar vergleichbar**. Das
Urteil hängt an der Wahl nicht: **auch die gemeldete Zahl 509 liegt unter der Obergrenze.**

### M11 — der volle Prompt nach R3

**Nachrichtenstruktur**, unverändert nach **R3** und nach den Blocküberschriften dieses
Manifests: `system` = Wortlaut A3 · `user` = Block 1 (`ist_modell.yaml`) + Block 2
(`input_facts.json`), zusammengesetzt nach der oben abgelegten Formel.

> **TOR der Messung, getroffen:** die zur Laufzeit komponierte `user`-Nachricht misst
> **107 307 B** mit SHA256 `21741e03…6b8d4eb1` — **bytegleich mit der `user`-Nachricht aus
> M9** (S2c-2). Anhang A weicht von der registrierten Zusammensetzung also **nicht** ab;
> eine Wiederholung der Messung nach R3 ist nicht ausgelöst.

**Gemeldet: 23 405 Token.** Für die R3-Struktur ist die **gemeldete** Zahl selbst die
Messgrösse (Rahmenkonstante F2, S2c-2).

### Kürzungsdetektor — alle DREI Kriterien einzeln

| Kriterium | Regel | Rechnung | Urteil |
|---|---|---|---|
| **(b) Fenstergleichstand** | ungültig bei Gleichstand mit dem Fenster oder weniger als 64 Token Abstand (Verdachtsbereich ab **32 705**) | 32 768 − 23 405 = **9 363** | **spricht nicht an** |
| **(b2) Monotonie** | der volle Prompt wird **gegen die Einzelmessung seiner grössten Komponente** geprüft | **23 405 ≥ 14 451** (M11a, Faktenbasis in der **gezogenen** Fassung) und **23 405 ≥ 8 467** (M3, `ist_modell.yaml` allein) | **spricht nicht an** |
| **(b3) Halbfenster-Signatur** | ungültig bei Gleichstand mit `Fenster / 2 + 2` = **16 386** oder weniger als 64 Token darunter | 23 405 − 16 386 = **7 019**, und 23 405 liegt **über** der Signatur | **spricht nicht an** |

**Keines der drei Kriterien ist erfüllt — die Messung ist GÜLTIG, und eine additive
Teilmessung nach §3b (c) war NICHT erforderlich (N entfällt).**

> **Zur Bezugsgrösse von (b2), ausdrücklich:** **M5 (29 095) ist NICHT die Bezugsgrösse.**
> M5 misst `input_facts_raw.json`, die **rohe** Fassung; sie ist in M11 **nicht enthalten**,
> weil die Stufen 0 und 0b gezogen sind. Die Einzelmessung der **gezogenen** Fassung fehlte
> im Journal und ist in diesem Auftrag als **M11a** erhoben worden.

### Drei unabhängige Gegenproben auf die Zahl 23 405

1. **Additiv.** 8 438 (`ist_modell.yaml` netto, M3) + 14 422 (`input_facts.json` netto,
   M11a) + 501 (Instruktion netto, M10g) + 13 (F2) + 17 + 14 (Trennzeilen) = **23 405** —
   **auf das Token genau**.
2. **Differenz der beiden vollen Prompts.** M9 − M11 = 24 104 − 23 405 = **699**, und
   1 200 − 501 = **699**. Die beiden vollen Prompts unterscheiden sich **exakt** um die
   Differenz ihrer Instruktionen.
3. **Vorhersage aus §3b (f).** Dort steht für eine Instruktion von 1 000 Token ein
   erwarteter voller Prompt von **rund 23 904**; dieselbe Rechnung sagt bei 501 Token
   **23 405** voraus — **gemessen 23 405**.

### M12 — Urteil

| Grösse | verlangt | gemessen | Urteil |
|---|---|---|---|
| **Schwelle** | **≤ 24 000** Token bei Fenster 32 768 | **23 405** | **GEHALTEN**, Reserve **595** Token |
| **Generat-Reserve** | **≥ 8 000** Token bis zum Fenster | **9 363** | **ERFÜLLT** |
| **Instruktionsbudget R1** | **≤ 1 000** Token, bindend | **480** netto | **GEHALTEN**, Reserve 520 |
| **R1-Zielgrösse** | rund **700**, nicht bindend | **480** netto | **GEHALTEN** |

> **DIE SCHWELLE IST NICHT BEWEGT WORDEN.** Sie steht unverändert bei **24 000** Token —
> nicht angehoben, nicht durch ihre Begründung (die Generat-Reserve) ersetzt, nicht mit
> einer Toleranz versehen. **ANHANG A IST NICHT GEKÜRZT WORDEN**; er hält die Schwelle im
> abgenommenen Wortlaut. Die in §3b (f) für den Gegenfall vorgesehene Kürzung ist damit
> **nicht ausgelöst**.

**Was dieser Block nicht tut.** Er ändert **keine Eingabe**: `data/z2/eingaben/` ist
bytegleich geblieben, und `data/z2/eingaben/SHA256SUMS` ist **nicht angefasst**. Er ändert
**keinen Messwert aus S2c-1 oder S2c-2** — M1–M9 stehen unverändert. Er trifft **keine
Aussage über einen Z2-Lauf**: die vier Kaltläufe sind **Instrumentenmessungen** nach
§3b (a), zählen gegen kein Budget, und ihre Ausgabe ist ungelesen verworfen.

---

## Zelle K2 × B1 — die drei Läufe (Auftrag S5, 02.09.2026)

**DIES IST DIE MESSUNG.** Drei Läufe der Bedingung **K2 × B1** nach Z2-Protokoll §2,
seriell gefahren, jeder mit **Kaltstart** (`ollama stop`) davor. **Kein vierter Lauf, kein
Probelauf, kein Wegwerflauf** (§4). Abgelegt unter `data/z2/k2_b1/run{0,1,2}/` mit je fünf
Dateien, gehasht in `data/z2/k2_b1/SHA256SUMS`.

> **N₁ IST NICHT GEZÄHLT. DIE BEWERTUNG STEHT AUS.** Z2-P, Z2-G und Z2-Z sind **nicht
> angewandt**, es ist **nicht dedupliziert**, und über Inhalt oder Qualität der Vorschläge
> ist **nichts** ausgesagt. **Die unten genannte Zahl der Vorschläge je Lauf ist die
> ROHZAHL, NICHT N₁** — sie zählt die Elemente des `rules`-Feldes, vor jeder Redundanz-
> prüfung. Die Bewertung nach §4/§7 Punkt 9 geschieht in einem eigenen Auftrag, erst
> nachdem alle drei Läufe vorliegen; dieser Block ist ihre Eingabe, nicht ihr Ergebnis.

### Instrumentenstand, an dem gemessen wurde

| Gegenstand | Stand |
|---|---|
| **Protokoll** (eingefroren) | `docs/protokolle/z2_protokoll_regelableitung.md`, Commit **`35aff9b`**, SHA256 **`862fdc3b7cfb264482db155575437edb25b1b436f92b5444b2137f1e332d9dde`** |
| **Werkzeug** (eingefroren) | `tools/run_z2.py`, Commit **`3c6545c`**, SHA256 **`c886da13fac988fffe462b0bb3b0d9cecdfdd1cbe109f6751304e0949a107975`** |
| **HEAD zur Laufzeit** | `3c6545cbd9b12983408f28421ae5c0a6b83338b5`, Arbeitsbaum **sauber** |
| **Eingabe Block 1** | `eingaben/ist_modell.yaml`, 42 959 B, SHA256 `146dbb05…36673` |
| **Eingabe Block 2** | `eingaben/input_facts.json`, 64 245 B, SHA256 `f670593a…4eb282a` |
| **Bytegatter vor dem ersten Aufruf** | **G1** `60ae777b…`, 2 283 B · **G2** `21741e03…`, 107 307 B — beide **GEHALTEN** |
| **Selbsttest vor dem ersten Aufruf** | **24 von 24** Proben bestanden |

### Modell, Fenster, Ausführungsgeometrie

| Gegenstand | Wert | Quelle |
|---|---|---|
| **Modell** | `qwen2.5-coder:7b` | angefordert **und** vom Endpunkt echoed (`modell_echo`) |
| **Digest** | **`dae161e27b0e`** | `ollama list` (Spalte ID) und `ollama ps` (Spalte ID), je Lauf bezeugt |
| **Fenster gesetzt** | **32 768** | `/etc/systemd/system/ollama.service.d/context.conf`, `OLLAMA_CONTEXT_LENGTH` |
| **Fenster wirksam** | **32 768** | `ollama ps`, Spalte CONTEXT, **nach** jedem der drei Aufrufe erhoben |
| **PROCESSOR** | **8%/92% CPU/GPU** | `ollama ps`, in **allen drei** Läufen identisch |
| **Ollama-Version** | 0.32.15 | `ollama --version` |
| **Endpunkt** | `http://localhost:11434/v1/chat/completions` | — |
| **Aufrufparameter** | `temperature: 0`, `seed: 0` (gesendet, **nicht als wirksam angenommen**, T-Z1-5), `max_tokens` **nicht gesetzt** | Laufmanifest |

**Zum Fensterzeugen vor dem Aufruf:** weil jedem Lauf ein `ollama stop` vorausgeht, ist
`ollama ps` **vor** dem Aufruf planmässig **leer** (nur die Kopfzeile). Das wirksame
Fenster ist deshalb, wie im Auftrag vorgesehen, **nach** dem Aufruf erhoben — dort zeigt
die Spalte CONTEXT in allen drei Läufen **32 768**. Beide Erhebungen stehen roh im
jeweiligen `run_manifest.json` unter `ollama.ollama_ps_vor` und `ollama.ollama_ps_nach`.

### Die drei Läufe — Zeitpunkte, Latenz, Token

| Lauf | Start | Ende | Latenz | HTTP | `finish_reason` | `prompt_tokens` gemeldet | netto | `completion_tokens` | `total_tokens` |
|---|---|---|---|---|---|---|---|---|---|
| **run0** | 2026-09-02T20:25:32+0200 | 20:26:03+0200 | **30 653,652 ms** | 200 | **`stop`** | **23 405** | **23 392** | **529** | 23 934 |
| **run1** | 2026-09-02T20:26:20+0200 | 20:26:48+0200 | **27 858,853 ms** | 200 | **`stop`** | **23 405** | **23 392** | **529** | 23 934 |
| **run2** | 2026-09-02T20:26:58+0200 | 20:27:25+0200 | **26 810,375 ms** | 200 | **`stop`** | **23 405** | **23 392** | **529** | 23 934 |

**Zur Nettozahl, ausdrücklich.** Für die **R3-Zwei-Nachrichten-Struktur ist die gemeldete
Zahl selbst die Messgrösse** (Rahmenkonstante F₂, S2c-2, oben in diesem Manifest unter
M11). Die Spalte „netto" ist deshalb **keine zweite Messung**, sondern die Ableitung
`gemeldet − F₂` mit **F₂ = 13**: **23 405 − 13 = 23 392**. Sie geht **auf das Token genau**
mit der additiven Zerlegung aus M11 auf — 8 438 (`ist_modell.yaml`) + 14 422
(`input_facts.json`) + 501 (Instruktion) + 17 + 14 (Trennzeilen) = **23 392**. Für
`completion_tokens` ist **keine Nettoform definiert**: F₂ sitzt auf der Prompt-Seite; die
529 sind **roh berichtet**.

**Die gemeldete Prompt-Tokenzahl trifft den Sollwert aus M11 exakt** — 23 405 gegen
Sollwert 23 405, in allen drei Läufen, **Abweichung 0**.

### `delivery_assurance`, Bandurteil und die drei Detektorkriterien — je Lauf

**`delivery_assurance: hard`** in allen drei Läufen. Begründung aus dem Laufmanifest:
lokaler Endpunkt, Sollwert aus M11 registriert, derselbe Tokenisierer, Fenster über den
systemd-Drop-in gesetzt und über `ollama ps` bezeugt — **alle drei Detektorkriterien aus
§3b (b)/(b2)/(b3) binden**.

| Prüfung | Regel | Rechnung (identisch in run0, run1, run2) | Urteil |
|---|---|---|---|
| **Band** (Soll-Toleranz) | gemeldete Zahl im Band **[23 288, 23 522]** (Sollwert 23 405, ±0,5 %, **beidseitig**) | 23 405 im Band [23 288, 23 522] | **spricht nicht an** |
| **(b) Fenstergleichstand** | ungültig bei Gleichstand mit dem Fenster 32 768 oder < 64 Token Abstand darunter (Verdachtsbereich ab 32 705) | 32 768 − 23 405 = **9 363** | **spricht nicht an** |
| **(b2) Monotonie** | die gemeldete Zahl des vollen Prompts ≥ Einzelmessung seiner grössten Komponente (**14 451**, M11a) | 23 405 gegen 14 451 | **spricht nicht an** |
| **(b3) Halbfenster** | ungültig bei Gleichstand mit `Fenster / 2 + 2` = **16 386** oder < 64 Token darunter | 16 386 − 23 405 = **−7 019** | **spricht nicht an** |

**Bandurteil je Lauf: `LIEFERUNG ZUGESICHERT`** — run0, run1, run2, `verletzt: []`.

**Bytegatter je Lauf**, im Laufmanifest mitgeführt: **G1** und **G2** je **GEHALTEN**, ist
gleich soll in SHA256 **und** Bytezahl.

### Vorschläge, Z2-W und Granularität — je Lauf

| Lauf | Schema (`architecture_rules`, `strict: true`) | **Rohzahl** Vorschläge | Z2-W wohlgeformt | Z2-W **nicht** wohlgeformt |
|---|---|---|---|---|
| **run0** | **konform**, `verstoesse: []` | **5** | **5** | **0** |
| **run1** | **konform**, `verstoesse: []` | **5** | **5** | **0** |
| **run2** | **konform**, `verstoesse: []` | **5** | **5** | **0** |

**Z2-W je Vorschlag**, in allen drei Läufen und für alle fünf Vorschläge (`R1`…`R5`):
`components_aufloesbar`, `statement_nicht_leer`, `statement_keine_wiederholung`,
`id_eindeutig`, `category_nicht_leer` — **je `true`**, `befunde: []`.

> **Schemakonformität ist AUSDRÜCKLICH KEINE MESSGRÖSSE** (§5.3 Punkt 1): unter
> `strict: true` ist sie providerseitig erzwungen und hier **nur protokolliert**.

**Granularitätszählung** (§5.3, Beobachtung im Anschluss an Befund 07):

| Lauf | Vorschläge mit ≥ 1 Artefakt-ID | `package` | `module` | `artefact` | `unresolved` |
|---|---|---|---|---|---|
| **run0** | **0** von 5 | **20** (4 je Vorschlag) | 0 | 0 | **0** |
| **run1** | **0** von 5 | **20** (4 je Vorschlag) | 0 | 0 | **0** |
| **run2** | **0** von 5 | **20** (4 je Vorschlag) | 0 | 0 | **0** |

> **Die Granularitätszählung ist KEIN Z2-W-Kriterium und KEIN Bewertungskriterium.** Ein
> Vorschlag auf Artefaktebene ist **wohlgeformt**. Sie wird berichtet, **nicht gewertet**,
> und geht in keine Kennzahl ein. **`unresolved: 0`** heisst: jede genannte Komponente war
> im Ist-Modell auflösbar.

### Lieferausfälle

**KEINE.** Kein Lauf ist nach Fall (i) ausgefallen — kein HTTP-Fehler, keine
Zeitüberschreitung, kein Bandverstoss, kein ansprechendes Detektorkriterium.
**Versuchszähler je Slot: run0 = 1, run1 = 1, run2 = 1.** Es ist **kein Slot entfernt und
keiner wiederholt** worden; die zulässigen drei Wiederholungen je Slot sind **nicht in
Anspruch genommen**. Auch **Fall (ii)** ist nicht eingetreten: alle drei Antworten sind
schemakonform, Z2-W-vollständig und mit `finish_reason: stop` **nicht abgeschnitten**.

### Formbefund ohne Deutung: die drei Generate sind zeichengleich

Der Inhalt von `choices[0].message.content` ist in **allen drei Läufen bytegleich** —
SHA256 `f71c9c743093e0c3…`, **2 356 Zeichen**. Die drei `raw_response.json` unterscheiden
sich **ausschliesslich** in den Umschlagfeldern `id` (`chatcmpl-874` / `-552` / `-298`) und
`created` (1788373563 / 1788373608 / 1788373645); die drei `validation.json` sind
**identisch** (SHA256 `c08f6450…`). **Dies ist eine Beobachtung an der Form, keine Aussage
über Determinismus, über die Wirksamkeit von `seed`, über Inhalt oder Qualität der
Vorschläge und keine Vorwegnahme der Bewertung.**

### Werkzeugbefund, gemeldet und NICHT behoben

In allen drei `run_manifest.json` steht `ollama.digest.digest: null` mit dem Hinweis
**„Manifest nicht gefunden — Digest nicht erhoben"**: das Werkzeug sucht den Digest unter
`~/.ollama/models/manifests/registry.ollama.ai/library/qwen2.5-coder/7b` und findet dort
nichts. **Der Digest ist dadurch nicht unbezeugt** — er steht in derselben Datei zweimal,
aus `ollama ps` (`ID: dae161e27b0e`), und ist vor dem ersten Aufruf über `ollama list`
gegen die Vorbedingung P5 geprüft worden. **Am Werkzeug ist nichts geändert worden**
(Auftragsgrenze: melden, nicht beheben).

### Was dieser Block NICHT tut

Er ändert **keine Eingabe**: `data/z2/eingaben/` ist bytegleich geblieben und dessen
`SHA256SUMS` **nicht angefasst**; ebenso `data/z2/messungen/`. Er ändert **das Protokoll
nicht** (`git diff 35aff9b HEAD` auf die Protokolldatei ist **leer**) und **das Werkzeug
nicht** (`git diff 3c6545c HEAD -- tools/` ist **leer**). Er trifft **keine Aussage über
die Bedingung K3**, die in diesem Auftrag **nicht gerufen** wurde. Und er **bewertet
nicht**: **N₁ ist nicht gezählt**, Z2-P/Z2-G/Z2-Z sind nicht angewandt, es ist nicht
dedupliziert.

## Zelle K3 × B1 — die drei Läufe (Auftrag S5-K3, 02./03.09.2026)

**DIES IST DIE MESSUNG.** Drei Läufe der Bedingung **K3 × B1** nach Z2-Protokoll §2,
seriell gefahren gegen den **DigitalOcean-Direktzugang**. **Kein vierter Lauf, kein
Probelauf, kein Wegwerflauf** (§4). Abgelegt unter `data/z2/k3_b1/run{0,1,2}/` mit je fünf
Dateien, gehasht in `data/z2/k3_b1/SHA256SUMS`. Der Auftrag lief nach der
FORTSETZUNGS-Regel über **drei Sitzungen** — `run0` am 02.09., `run1` und `run2` am
03.09.; die Ausfälle dazwischen sind unten vollständig geführt.

> **N₁ IST NICHT GEZÄHLT. DIE BEWERTUNG STEHT AUS.** Z2-P, Z2-G und Z2-Z sind **nicht
> angewandt**, es ist **nicht dedupliziert**, und über Inhalt oder Qualität der Vorschläge
> ist **nichts** ausgesagt. **Die unten genannte Zahl der Vorschläge je Lauf ist die
> ROHZAHL, NICHT N₁** — sie zählt die Elemente des `rules`-Feldes, vor jeder Redundanz-
> prüfung. Die Bewertung nach §4/§7 Punkt 9 geschieht in einem eigenen Auftrag; dieser
> Block ist ihre Eingabe, nicht ihr Ergebnis. Ein **qualitativer Vergleich mit K2 × B1
> findet hier nicht statt.**

### Instrumentenstand, an dem gemessen wurde

| Gegenstand | Stand |
|---|---|
| **Protokoll** (eingefroren) | `docs/protokolle/z2_protokoll_regelableitung.md`, Commit **`35aff9b`**, SHA256 **`862fdc3b7cfb264482db155575437edb25b1b436f92b5444b2137f1e332d9dde`** |
| **Werkzeug** (eingefroren) | `tools/run_z2.py`, Commit **`3c6545c`**, SHA256 **`c886da13fac988fffe462b0bb3b0d9cecdfdd1cbe109f6751304e0949a107975`** |
| **HEAD zur Laufzeit** | `7d2c4ae39965b1767aacde1055c1dc533d8b3049`, in allen drei Laufmanifesten identisch |
| **Eingabe Block 1** | `eingaben/ist_modell.yaml`, 42 959 B, SHA256 `146dbb05…36673` |
| **Eingabe Block 2** | `eingaben/input_facts.json`, 64 245 B, SHA256 `f670593a…4eb282a` |
| **Bytegatter vor jedem Sitzungsbeginn** | **G1** `60ae777b…`, 2 283 B · **G2** `21741e03…`, 107 307 B — je **GEHALTEN** |
| **Selbsttest vor jedem Sitzungsbeginn** | **24 von 24** Proben bestanden |

### Modell, Endpunkt, Ausführungsgeometrie

| Gegenstand | Wert | Quelle |
|---|---|---|
| **Modell** | `nvidia-nemotron-3-super-120b` | angefordert **und** vom Endpunkt echoed (`modell_echo`), in allen drei Läufen zeichengleich |
| **Endpunkt** | `https://inference.do-ai.run/v1/chat/completions` (Base-URL `https://inference.do-ai.run/v1`) | Z1-Protokoll §2.2 Zeile K3 und §3.3 (5), aus dem Repositorium gegengelesen |
| **Profil** | `digitalocean`, **kein** `CONFORMANCE_PROVIDER_PIN` | Z1-Protokoll §2.2 (B32) |
| **Digest** | **existiert nicht** | DO-Direktzugang stellt keinen bereit (T-Z1-5) |
| **`system_fingerprint`** | **`null`** in allen drei Läufen **und** in allen drei Sonden | `meta.json`, `run_manifest.json` |
| **Fenster gesetzt** | — | `fenster.wirksam`: „nicht kontrollierbar und nicht ablesbar (fremder Anbieter)" |
| **Aufrufparameter** | `temperature: 0`, `seed: 0` (gesendet, **nicht als wirksam angenommen**, T-Z1-5), `max_tokens` **nicht gesetzt** | Laufmanifest |
| **Gesendeter Schemaname** | **`architecture_rules`**, `strict: true` | `meta.json`, `validation.json` |

**Zum fehlenden Fensterzeugen, ausdrücklich.** `ollama ps` und `ollama stop` sind **nicht
gelaufen** und **konnten nicht laufen**: sie betreffen den lokalen Endpunkt und haben für
K3 keine Bedeutung. Das Feld `ollama` steht in allen drei Laufmanifesten auf **`null`**.
**Es ist später nach keinem Fensterzeugen zu suchen — es kann für diese Zelle keinen
geben.** Ebenso wenig gibt es einen Kaltstart-Vermerk: der Serverzustand des fremden
Anbieters ist weder herstellbar noch ablesbar.

### Erreichbarkeitssonden — Instrumentenmessungen nach §3b (a), gegen kein Budget

| Sonde | Zeitpunkt | HTTP | Modell-Echo | `usage` | `system_fingerprint` | Latenz |
|---|---|---|---|---|---|---|
| vor `run0` | 2026-09-02T20:55:25+0200 | **200** | zeichengleich | 17 / 1 / 18 | `null` | 2 230,22 ms |
| vor `run1` | 2026-09-03T07:53:06+0200 | **200** | zeichengleich | 17 / 1 / 18 | `null` | 1 339,81 ms |
| vor `run2` | 2026-09-03T08:22:31+0200 | **200** | zeichengleich | 17 / 1 / 18 | `null` | 1 063,20 ms |

Nutzlast je Sonde: das Literal `x`, `max_tokens: 1`, Ausgabe **ungelesen verworfen**. Alle
drei sind Vorbedingung des jeweils folgenden Laufs gewesen und haben gehalten.

### Die drei Läufe — Zeitpunkte, Latenz, Token

| Lauf | Start | Ende | Latenz | HTTP | `finish_reason` | `prompt_tokens` | `completion_tokens` | `total_tokens` |
|---|---|---|---|---|---|---|---|---|
| **run0** | 2026-09-02T20:55:45+0200 | 20:58:21+0200 | **154 424,988 ms** | 200 | **`stop`** | **25 030** | **1 874** | 26 904 |
| **run1** | 2026-09-03T07:59:47+0200 | 08:02:37+0200 | **164 457,858 ms** | 200 | **`stop`** | **25 030** | **1 607** | 26 637 |
| **run2** | 2026-09-03T08:22:41+0200 | 08:26:45+0200 | **236 897,347 ms** | 200 | **`stop`** | **25 030** | **3 863** | 28 893 |

**Keine Nettozahl.** Anders als bei K2 wird hier **keine** Rahmenkonstante abgezogen: die
Zerlegung aus M11 ist am Ollama-Tokenisierer gemessen und auf den fremden Tokenisierer
**nicht übertragbar**. Die Zahl **25 030** ist roh berichtet.

**Der für K2 registrierte Sollwert 23 405 ± 0,5 % gilt hier NICHT und ist nicht angewandt
worden.** Die Differenz 25 030 gegen 23 405 ist eine Eigenschaft **zweier verschiedener
Tokenisierer über bytegleicher Nutzlast** — sie ist **kein** Bandverstoss, weil es für K3
kein Band gibt.

### `delivery_assurance = record_only` — die Asymmetrie zu K2, und ihre Begründung

**`delivery_assurance: record_only`** in allen drei Läufen (§3b (e)). Begründung, wörtlich
aus dem Laufmanifest:

> „Fremder Tokenisierer: es gibt keinen berechenbaren Sollwert, und das Kontextfenster des
> Anbieters ist weder gesetzt noch ablesbar. (b) und (b3) sind Ollama-Eigenschaften und
> binden hier NICHT; geprueft wird ausschliesslich (b2) gegen fruehere Messungen DERSELBEN
> Bedingung. §3b (e): die Schwelle bindet auf K2, K3s Tokenzahl wird berichtet und ist
> nicht schwellenbildend."

**Dieses Feld steht ausdrücklich im Record, damit ein späterer K3-Ausfall nicht wie ein
Modellbefund gelesen wird.**

| Kriterium | Bindet? | Rechnung je Lauf | Urteil |
|---|---|---|---|
| **Band** (Soll-Toleranz) | **nein** | kein berechenbarer Sollwert | **gilt nicht** — fremder Tokenisierer |
| **(b) Fenstergleichstand** | **nein** | Fenster nicht kontrollierbar | **gilt nicht** — serverseitig, Ollama-Eigenschaft |
| **(b2) Monotonie** | **ja**, nur gegen dieselbe Bedingung | `run0`: kein Bezugswert · `run1`: 25030 gegen 25030 · `run2`: 25030 gegen 25030 | `run0` **gegenstandslos**, `run1`/`run2` **spricht nicht an** |
| **(b3) Halbfenster** | **nein** | Signatur ist eine Ollama-Eigenschaft | **gilt nicht** |

**(b2)-Urteil der Zelle: erfüllt, keine Abweichung.** Die gemeldete `prompt_tokens` ist in
allen drei Läufen **identisch 25 030** — wie bei identischer Nutzlast erwartet. Es gibt
**nichts nach der Meldepflicht zu melden.** Für `run0` ist das Kriterium **gegenstandslos**
(kein früherer Lauf derselben Bedingung), ausdrücklich **nicht** „bestanden".

**Bandurteil je Lauf: `LIEFERUNG AUFGEZEICHNET`** — run0, run1, run2, `verletzt: []`.

**Bytegatter je Lauf**: **G1** und **G2** je **GEHALTEN**, ist gleich soll in SHA256 **und**
Bytezahl. Nachgemessen zusätzlich an der abgelegten Datei: alle drei `prompt.txt` sind
**untereinander bytegleich** (SHA256 `d19b2521…`, je 109 612 B) und zerlegen sich in
**2 283 B System** (`60ae777b…` = G1) + **107 307 B User** (`21741e03…` = G2) + **22 B**
Rollenrahmen (`### system\n` 11 B, Blockabschluss `\n` 1 B, `\n### user\n` 10 B):
11 + 2 283 + 1 + 10 + 107 307 = **109 612**.

### Vorschläge, Z2-W und Granularität — je Lauf

| Lauf | Schema (`architecture_rules`, `strict: true`) | **Rohzahl** Vorschläge | Z2-W wohlgeformt | Z2-W **nicht** wohlgeformt |
|---|---|---|---|---|
| **run0** | **konform**, `verstoesse: []` | **4** (`R1`…`R4`) | **4** | **0** |
| **run1** | **konform**, `verstoesse: []` | **3** (`R1`…`R3`) | **3** | **0** |
| **run2** | **konform**, `verstoesse: []` | **5** (`R1`…`R5`) | **5** | **0** |

**Z2-W je Vorschlag**, in allen drei Läufen und für jeden Vorschlag:
`components_aufloesbar`, `statement_nicht_leer`, `statement_keine_wiederholung`,
`id_eindeutig`, `category_nicht_leer` — **je `true`**, `befunde: []`.

> **Schemakonformität ist AUSDRÜCKLICH KEINE MESSGRÖSSE** (§5.3 Punkt 1): unter
> `strict: true` ist sie providerseitig erzwungen und hier **nur protokolliert**. Für
> diesen Endpunkt ist `strict: true` nach Z1-Protokoll §3.3 (3) **keine Formgarantie** —
> dass alle drei Antworten dennoch konform ausfielen, ist protokolliert, nicht gewertet.

**Granularitätszählung** (§5.3, Beobachtung im Anschluss an Befund 07):

| Lauf | Vorschläge mit ≥ 1 Artefakt-ID | `package` | `module` | `artefact` | `unresolved` |
|---|---|---|---|---|---|
| **run0** | **0** von 4 | **6** | **6** | 0 | **0** |
| **run1** | **0** von 3 | **3** | **9** | 0 | **0** |
| **run2** | **0** von 5 | **8** | 0 | 0 | **0** |

Je Vorschlag: `run0` — R1 3×`module`, R2 3×`module`, R3 3×`package`, R4 3×`package`;
`run1` — R1 3×`package`, R2 3×`module`, R3 6×`module`; `run2` — R1 1×`package`,
R2 1×`package`, R3 1×`package`, R4 2×`package`, R5 3×`package`.

> **Die Granularitätszählung ist KEIN Z2-W-Kriterium und KEIN Bewertungskriterium.** Sie
> wird berichtet, **nicht gewertet**, und geht in keine Kennzahl ein. **`unresolved: 0`**
> heisst: jede genannte Komponente war im Ist-Modell auflösbar.

### Lieferausfälle — Fall (i), Präzedenz Z1-Amendment 4a

~~**Acht Aufrufe, drei gültige Läufe, fünf Lieferausfälle.**~~ Kein Ausfall hat einen Slot
hinterlassen: das Werkzeug legt das Zielverzeichnis erst nach erhaltener Antwort an, es war
**in keinem Fall etwas zu entfernen**.

> **KORRIGIERTE ZÄHLUNG — 03.09.2026 (Auftrag S8).** Der durchgestrichene Summensatz oben
> **widersprach der Tabelle unmittelbar darunter**. Gefunden in **S7a** (`ad4142d`,
> `docs/planung/offene_punkte.md` Zeile **I6**), dort als Abweichung gemeldet und nicht
> angeglichen; hier angeglichen. **DIE TABELLE WAR UND IST RICHTIG — korrigiert wird
> ausschliesslich der zusammenfassende Satz, der ihr widersprach.** Keine Zeile der Tabelle
> ist berührt, kein Laufrecord, keine Eingabe, kein `SHA256SUMS`.
>
> **NEUE FASSUNG: zehn Aufrufe, drei gelieferte Läufe, sieben Lieferausfälle.** Ausgezählt
> aus der Tabelle unten, Zeile für Zeile:
>
> - **Zahl der Aufrufe insgesamt: 10** — die Tabelle führt **zehn** Zeilen, je eine je
>   Aufruf gegen die registrierte Frage (`run0` eine, `run1` fünf, `run2` vier).
> - **Zahl der gelieferten Läufe: 3** — die drei Zeilen mit **HTTP 200** und dem Ergebnis
>   **LAUF GILT**: `run0` S1 · 1, `run1` S2 · 2, `run2` S3 · 1.
> - **Zahl der Lieferausfälle: 7** — die sieben Zeilen mit dem Ergebnis **Ausfall (i)**.
> - **Aufteilung nach HTTP-Status: fünf × `424`** (`litellm.Timeout:
>   Hosted_vllmException - stream timeout`; `run1` S1 · 1, S1 · 2, S1 · 3, S2 · 1 und
>   `run2` S2 · 1) **und zwei × `429`** (`Platform overloaded. Please try again later.`;
>   `run2` S2 · 2 und S2 · 3).
> - **Versuchszähler je Slot: `run0` = 1, `run1` = 5, `run2` = 4** — unverändert wie unten
>   ausgewiesen.
>
> **Zwei Gegenproben, beide gehen auf:** **1 + 5 + 4 = 10**, gleich der Zahl der
> Tabellenzeilen; und **3 gelieferte + 7 ausgefallene = 10**, dieselbe Zahl. Der alte Satz
> zählte erkennbar **nur die fünf `424`** als Ausfälle und liess die **beiden `429`** aus —
> daraus ergab sich zugleich die Aufrufzahl **acht** statt **zehn**. Die Beobachtung weiter
> unten („vier der fünf `424`-Ausfälle") war davon **nicht** betroffen und ist richtig.
>
> **Die Einordnung bleibt unverändert.** Alle **sieben** Ausfälle sind **Fall (i)** nach der
> Präzedenz **Z1-Amendment 4a** — HTTP-Fehler ohne `usage`, also **keine Antwort auf die
> registrierte Frage**: **Lieferausfälle und KEINE Modellbefunde**, kein Lauf zählt. Die
> **Wiederholung ist nach Z1-Amendment 3c gedeckt**, weil ein Wiederholungsbudget **nur bei
> Lieferausfall** zurückgesetzt wird, nie bei missfallendem Ergebnis. Es ist **nicht
> bewertet** und **N₁ ist nicht gezählt**.
>
> **ZWEI ZEITREIHEN FÜR DIE LAUFDAUERN — sie sind NICHT dieselbe Messung und nicht zu
> vermischen.** Dieser Manifestblock führt beide:
>
> | Lauf | **Wanduhr** — Spalte *Dauer* der Aufruftabelle unten, aus `run_manifest.json`, `zeitstempel.start`/`.ende` | **Latenzfeld** — Spalte *Latenz* der Tabelle „Die drei Läufe", aus `meta.json`, `latenz_ms` | Differenz |
> |---|---|---|---|
> | `run0` | **2:36** (156 s) | **154 424,988 ms** ≙ 2:34,4 | 1,6 s |
> | `run1` | **2:50** (170 s) | **164 457,858 ms** ≙ 2:44,5 | 5,5 s |
> | `run2` | **4:04** (244 s) | **236 897,347 ms** ≙ 3:56,9 | 7,1 s |
>
> Die **Wanduhr** umschliesst den Aufruf samt Vor- und Nachlauf des Werkzeugs und ist in der
> Aufruftabelle **auf die Sekunde gerundet** ausgewiesen; das **Latenzfeld** misst die
> Client-Zeit um den HTTP-Aufruf selbst. Nur die **Wanduhr** ist auch für die **Ausfälle**
> verfügbar — ein Ausfall schreibt kein `meta.json`. **Daran ist nichts geprüft und nichts
> gedeutet**; beide stehen hier, damit ein späterer Leser weiss, welche Zahl welche ist.

| Slot | Sitzung / Versuch | Start | Ende | Dauer | HTTP | Meldung | Ergebnis |
|---|---|---|---|---|---|---|---|
| **run0** | S1 · 1 | 02.09. 20:55:45 | 20:58:21 | 2:36 | **200** | — | **LAUF GILT** |
| **run1** | S1 · 1 | — (nicht gestempelt) | 02.09. 21:07:43 | — | **424** | `litellm.Timeout: Hosted_vllmException - stream timeout` | Ausfall (i) |
| **run1** | S1 · 2 | 02.09. 21:09:18 | 21:14:19 | 5:01 | **424** | dieselbe Meldung | Ausfall (i) |
| **run1** | S1 · 3 | 02.09. 21:43:39 | 21:48:40 | 5:01 | **424** | dieselbe Meldung | Ausfall (i) |
| **run1** | S2 · 1 | 03.09. 07:53:18 | 07:58:19 | 5:01 | **424** | dieselbe Meldung | Ausfall (i) |
| **run1** | S2 · 2 | 03.09. 07:59:47 | 08:02:37 | 2:50 | **200** | — | **LAUF GILT** |
| **run2** | S2 · 1 | 03.09. 08:02:48 | 08:07:49 | 5:01 | **424** | `litellm.Timeout: Hosted_vllmException - stream timeout` | Ausfall (i) |
| **run2** | S2 · 2 | 03.09. 08:09:16 | 08:09:17 | 0:01 | **429** | `Platform overloaded. Please try again later.` | Ausfall (i) |
| **run2** | S2 · 3 | 03.09. 08:13:36 | 08:13:37 | 0:01 | **429** | dieselbe Meldung | Ausfall (i) |
| **run2** | S3 · 1 | 03.09. 08:22:41 | 08:26:45 | 4:04 | **200** | — | **LAUF GILT** |

**Versuchszähler je Slot: `run0` = 1, `run1` = 5 (über zwei Sitzungen), `run2` = 4 (über
zwei Sitzungen).** Die Grenze von **drei Versuchen je Slot** ist **in jeder einzelnen
Sitzung eingehalten** — S1 fuhr drei Versuche an `run1`, S2 zwei an `run1` und drei an
`run2`, S3 einen an `run2`. Über die Sitzungsgrenze hinweg summieren sie sich, weil die
FORTSETZUNGS-Regel des Auftrags einen Folgelauf ausdrücklich vorsieht, der **nur die
fehlenden Slots** fährt. **Vollständige Slots sind nie neu gefahren worden.**

Die Abstände **zwischen einem Ausfall und dem nächsten Versuch desselben Slots**, aus den
Zeitstempeln gerechnet: `run1` **95 s**, **1 760 s**, **36 278 s** (Sitzungswechsel über
Nacht), **88 s**; `run2` **87 s**, **259 s**, **544 s** (Sitzungswechsel). **Jeder liegt
über den geforderten 60 Sekunden.**

**Fall (ii) ist nicht eingetreten:** alle drei gültigen Antworten sind schemakonform,
Z2-W-vollständig und mit `finish_reason: stop` **nicht abgeschnitten**. Kein Ausweichen auf
einen anderen Endpunkt oder Modellstring, keine Ersatzbedingung, keine Änderung an Prompt,
Werkzeug, Eingaben, Schema oder Schwelle.

**Beobachtung ohne Deutung:** vier der fünf `424`-Ausfälle endeten nach **exakt 5:01 min**;
die drei gültigen Läufe brauchten 2:36, 2:50 und 4:04 min. Die beiden `429` kamen nach je
einer Sekunde mit Auslastungsmeldung. **Daran ist nichts geprüft und nichts unternommen
worden**; die Zahlen stehen hier, damit ein späterer Leser sie nicht rekonstruieren muss.

### Formbefund ohne Deutung: die drei Generate sind NICHT zeichengleich

| Lauf | SHA256 von `choices[0].message.content` | Zeichen | `id` | `created` |
|---|---|---|---|---|
| **run0** | `f3514cf678fc7bec…` | 1 403 | `chatcmpl-cf7b8be7-…` | 1788375346 |
| **run1** | `2ffde87ee71cd79c…` | 1 256 | `chatcmpl-ecff2da9-…` | 1788415189 |
| **run2** | `1fe29dd6972bd5f6…` | 1 797 | `chatcmpl-efe1607e-…` | 1788416563 |

**Das ist erwartet und kein Fehler.** Nach T-Z1-5 ist beim DO-Direktzugang
`system_fingerprint` `null`, ein Seed wird gesendet, aber **nicht als wirksam angenommen**,
und die Identität der Gewichte ist **nicht verifiziert**; Varianz über die drei Läufe ist
Teil des Messgegenstands, keine Störung. **Dies ist eine Beobachtung an der Form** — keine
Aussage über Determinismus, über Inhalt oder Qualität der Vorschläge und keine Vorwegnahme
der Bewertung.

### Werkzeugbefund, gemeldet und NICHT behoben

`tools/run_z2.py` schreibt `data/z2/k3_b1/SHA256SUMS` **nach jedem einzelnen Lauf** neu,
nicht erst mit der vollständigen Zelle. Zwischen den Sitzungen lag die Datei deshalb
unversioniert auf der Platte und deckte nur die bis dahin vorhandenen Slots. **Am Werkzeug
ist nichts geändert worden** (Auftragsgrenze: melden, nicht beheben); die eingecheckte
Fassung deckt alle **15** Dateien der vollständigen Zelle, `sha256sum -c` läuft durch.

### Was dieser Block NICHT tut

Er ändert **keine Eingabe**: `data/z2/eingaben/` und `data/z2/messungen/` sind bytegleich
geblieben, deren `SHA256SUMS` **nicht angefasst**. Er fasst **`data/z2/k2_b1/` nicht an**
(15 von 15 unverändert OK) und stellt **keinen qualitativen Vergleich** mit K2 an. Er
ändert **das Protokoll nicht** (`git diff 35aff9b HEAD` auf die Protokolldatei ist **leer**)
und **das Werkzeug nicht** (`git diff 3c6545c HEAD -- tools/` ist **leer**). Und er
**bewertet nicht**: **N₁ ist nicht gezählt**, Z2-P/Z2-G/Z2-Z sind nicht angewandt, es ist
nicht dedupliziert.

---

## Aufbereitung der Bewertung (Auftrag S10, 03.09.2026)

**Was dieser Block ist.** Nach Protokoll **§2** ist die Auswertungseinheit der **einzelne
Regelvorschlag (nach Dedup, §6 Z2-R)**, bewertet von **einem** Bewerter, **verblindet**
(§6 „Bewertungsablauf — EINZELBEWERTER, VERBLINDET“, Threat **T-Z2-7** in §10). Dieser
Block trägt das **aufbereitete Blatt** und den **getrennt abgelegten Zuordnungsschlüssel**.
Er trägt **keine Bewertung**.

### Ablage

```
data/z2/
  bewertung/
    SHA256SUMS                  ← hasht ALLES im Block ausser sich selbst
    bewertungsblatt.md          ← das verblindete Arbeitsblatt, 17 Einträge
    zuordnungsschluessel.json   ← Herkunft je Etikett; VOR ABSCHLUSS NICHT ÖFFNEN
```

| Datei | SHA256 |
|---|---|
| ~~`bewertung/bewertungsblatt.md`~~ | ~~`4db42263f729c8ea0f83c50c4166eeb570a2ed40829af255f031d99dfa747dd7`~~ — **überholt am 04.09.2026 (Auftrag S11)**: das ist der Hash des **leeren** Blattes; `9b6c76b` hat es ausgefüllt. |
| `bewertung/bewertungsblatt.md` (ausgefüllt, seit `9b6c76b`) | `72ebc3170f484a391a1d991c4fa155d57d04f6bfc5374c609ac8d601c109c029` |
| `bewertung/zuordnungsschluessel.json` | `0215a8b2ed377df1e4e074dd5f489c58a7341fc93e54362b61fcef8b78a320f2` |
| `tools/prepare_z2_review.py` (Erzeuger, ausserhalb des Blocks) | `ff39f50602e6c0f9cde21d49a9642a487d98554bf33d5c489e853b40aa5eb8f5` |

### Die Identitätsdefinition, nach der zusammengeführt wurde

Zwei Vorschläge sind **mechanisch identisch**, wenn das Tupel

```
(category, statement, severity, sorted(scope.components))
```

nach **Unicode-NFC** und **Abschneiden führender und schliessender Leerzeichen**
**ZEICHENGLEICH** ist. **`id` geht NICHT ein** — sie ist je Lauf frei gewählt. **Keine
weitere Normalisierung:** keine Kleinschreibung, keine Interpunktions-, Zahlen- oder
Synonymbehandlung, kein Zusammenziehen innerer Leerzeichen.

**MECHANISCHE IDENTITÄT IST NUR EINE TEILMENGE DESSEN, WAS Z2-R VERLANGT.** §6 Z2-R
lautet wörtlich: *„Zwei Vorschläge sind Duplikate, wenn Kategorie, Scope und Kernaussage
übereinstimmen (Umformulierungen zählen als ein Vorschlag).“* **Kernaussage** und
**Umformulierungen** sind eine **inhaltliche** Entscheidung und gehören dem Bewerter.
Zwei Vorschläge, die **dasselbe sagen**, aber **anders formuliert** sind, stehen im Blatt
deshalb als **ZWEI Einträge**; das Blatt führt je Eintrag eine Spalte **„identisch mit
P-xx“**, in der die inhaltliche Zusammenführung von Hand einzutragen ist.

### Die Zahlen

| Grösse | Wert |
|---|---|
| Vorschläge **roh**, über die sechs Läufe | **27** |
| davon **mechanisch verschieden** | **17** |
| — aus **K2 × B1** | **5** (je Vielfachheit **3**) |
| — aus **K3 × B1** | **12** (je Vielfachheit **1**) |
| **konditionsübergreifend** zusammengeführt | **0** |

**Gegenprobe der Rohzahl, wie der Auftrag sie vorgab und wie sie eintraf:** K2 × B1
**5 / 5 / 5 = 15**, K3 × B1 **4 / 3 / 5 = 12**, zusammen **27**. Keine Abweichung.

### Seed und Reihenfolge

`random.Random(20260903)` auf die Einträge in **Reihenfolge ihres ersten Auftretens**
(Zellen `k2_b1`, `k3_b1`; Slots `run0`, `run1`, `run2`; Position aufsteigend); danach
die Etiketten `P-01` … `P-17` in der geschüttelten Reihenfolge. Der Seed steht **im Blatt
und im Schlüssel**. Die Reihenfolge ist **nicht nach Bedingung sortiert**.

### Blindungsauflagen — und ihre Grenze

**Im Blatt erscheinen NICHT:** Bedingung, Modellname, Slot, die ursprüngliche `id`, die
**Zahl der Läufe je Eintrag**, die Position im Array, Zeitstempel.

**Die Vielfachheit ist ausdrücklich eine solche Kennzahl** und steht deshalb **nur im
Schlüssel**: in **K2 × B1 sind die drei Generate zeichengleich** (SHA256 von
`choices[0].message.content` identisch über `run0`/`run1`/`run2`, je 2 356 Zeichen —
Formbefund des K2-Blocks), eine **Vielfachheit 3 wäre daher gleichbedeutend mit „K2“**.

**GRENZE, nicht heilbar, unter T-Z2-7 vermerkt:** **Stil und Länge der
`statement`-Texte** — und die **Zuschnittsgewohnheit der `scope.components`** — können
die **Modellklasse** dennoch erkennbar machen. Der Wortlaut der Vorschläge ist die
**Messgrösse selbst** und darf nicht angetastet werden; die Verblindung ist eine
**Verblindung gegen die Kennzeichnung, keine gegen den Text**.

### Was dieser Block NICHT tut

**N₁ ist NICHT gezählt, es ist NICHT bewertet, und die inhaltliche Dedup nach Z2-R steht
aus.** `kind`, **Z2-P**, **Z2-G** und **Z2-Z** sind im Blatt **leer** — nicht ausgefüllt,
nicht vorgeschlagen, nicht angedeutet. Kein Verdikt zu **E1–E4**, keine Kennzahl, kein
Anteil, kein Vergleich zwischen den Zellen. **Z2-W** und die **Granularitätszählung**
stehen je Eintrag im Blatt, sind aber **maschinell aus der archivierten
`validation.json` übernommen** und als solche gekennzeichnet; die Granularität
ausdrücklich als **BEOBACHTUNG, kein Kriterium**.

Er ändert **nichts** an `eingaben/`, `messungen/`, `k2_b1/`, `k3_b1/`, an
`tools/run_z2.py` oder am eingefrorenen Protokoll.

---

## Auswertung der Bewertung (Auftrag S11, 04.09.2026)

**Was dieser Block ist.** Der Bewerter hat das verblindete Blatt ausgefüllt (`9b6c76b`).
Dieser Block hält fest, **wann der Zuordnungsschlüssel geöffnet wurde**, **welche Herkunft
sich hinter den Etiketten verbirgt**, **wie N₁ zustande kommt** und **welche Zahlen §7
mechanisch hergibt**. Er **deutet nichts**: keine vorregistrierte Erwartung wird beurteilt,
keine Zuweisung des Bewerters korrigiert, kein Ergebnis formuliert.

### Zeitpunkt des Schlüsselöffnens

| Angabe | Wert |
|---|---|
| **Geöffnet am** | **04.09.2026, 09:38:19 CEST** (`2026-09-04T09:38:19+02:00`) |
| Commit mit dem **vollständig ausgefüllten** Blatt | `9b6c76b` — „docs: fill in bewertungsblatt.md“ |
| SHA256 `zuordnungsschluessel.json` | `0215a8b2ed377df1e4e074dd5f489c58a7341fc93e54362b61fcef8b78a320f2` (unverändert seit `b17fc98`) |
| SHA256 `bewertungsblatt.md` | `72ebc3170f484a391a1d991c4fa155d57d04f6bfc5374c609ac8d601c109c029` |

**Die Bewertung war VOR dem Öffnen abgeschlossen.** Belegt durch zweierlei, beides vor dem
Öffnen geprüft: (i) alle **17** Etiketten tragen in `kind`, **Z2-P**, **Z2-G**, **Z2-Z**
sowie in „identisch mit P-xx“ und „Grenzfall“ einen Eintrag; (ii) die Commit-Reihenfolge —
`b17fc98` legt das **leere** Blatt an (die vier Dimensionen sind dort nachweislich leer),
`9b6c76b` füllt es aus, das Öffnen des Schlüssels geschieht danach in S11. Die
**maschinellen** Angaben (`category`, `severity`, `scope.components`, `statement`, **Z2-W**,
Granularität) sind gegen `b17fc98` **zeichengleich** — keine Abweichung in 17 × 8 Feldern.

### Auflösung der Zuordnung

| Etikett | Bedingung | Slot(s) | Position(en) | `id`(s) | Vielfachheit |
|---|---|---|---|---|---|
| `P-01` | K3 × B1 | `run1` | 0 | `R1` | 1 |
| `P-02` | K3 × B1 | `run2` | 3 | `R4` | 1 |
| `P-03` | K3 × B1 | `run0` | 1 | `R2` | 1 |
| `P-04` | **K2 × B1** | `run0`, `run1`, `run2` | 0 | `R1` | **3** |
| `P-05` | **K2 × B1** | `run0`, `run1`, `run2` | 4 | `R5` | **3** |
| `P-06` | **K2 × B1** | `run0`, `run1`, `run2` | 1 | `R2` | **3** |
| `P-07` | K3 × B1 | `run2` | 4 | `R5` | 1 |
| `P-08` | K3 × B1 | `run2` | 1 | `R2` | 1 |
| `P-09` | K3 × B1 | `run1` | 2 | `R3` | 1 |
| `P-10` | K3 × B1 | `run0` | 0 | `R1` | 1 |
| `P-11` | K3 × B1 | `run0` | 2 | `R3` | 1 |
| `P-12` | **K2 × B1** | `run0`, `run1`, `run2` | 3 | `R4` | **3** |
| `P-13` | K3 × B1 | `run2` | 0 | `R1` | 1 |
| `P-14` | K3 × B1 | `run1` | 1 | `R2` | 1 |
| `P-15` | **K2 × B1** | `run0`, `run1`, `run2` | 2 | `R3` | **3** |
| `P-16` | K3 × B1 | `run0` | 3 | `R4` | 1 |
| `P-17` | K3 × B1 | `run2` | 2 | `R3` | 1 |

**Gegenproben, alle acht ohne Abweichung:** 17 Etiketten · Σ Vielfachheiten **27** · fünf
Etiketten mit Vielfachheit 3, **alle aus K2 × B1** · zwölf mit Vielfachheit 1 · Z2-R
symmetrisch und transitiv auflösbar · jedes Etikett mit „Grenzfall = ja“ hat eine Zeile in
Anhang B und umgekehrt · Blatt und Schlüssel führen dieselben Etiketten.

### Z2-R — die Äquivalenzklassen des Bewerters

**Eine** nichttriviale Klasse: **{`P-01`, `P-11`}**, eingetragen einseitig bei `P-11` auf
`P-01` (zulässig, als gerichtete Angabe **symmetrisiert**), begründet in Anhang B.
**16 Klassen** aus **17 Etiketten**.

**ZELLÜBERGREIFEND: nein.** Beide Mitglieder stammen aus **K3 × B1** (`run0` und `run1`);
**keine** Klasse führt Etiketten aus beiden Bedingungen zusammen. Das ist eine **Tatsache**;
ihre Bedeutung bleibt offen.

**Gemeldet, nicht geändert:** die beiden Mitglieder tragen auf der Spalte „Grenzfall“
**verschiedene** Werte (`P-01` = nein, `P-11` = ja). Es wurde **nicht** eingegriffen; die
Klasse wird auf dieser Dimension als uneinheitlich geführt, die Grenzfallquote zusätzlich
auf Klassenbasis ausgewiesen.

### N₁ — Herleitung

Nach **§7 Punkt 9** und **Gate-Notiz §5b** ist N₁ die **PRO-LAUF-Dedup des ERSTEN Laufs der
Zelle K2 × B1** nach **Z2-R** — *nicht* die Dedup über die drei Läufe.

1. Etiketten, deren Herkunft `k2_b1/run0` einschliesst: **`P-04`, `P-05`, `P-06`, `P-12`,
   `P-15`** — fünf.
2. Äquivalenzklassen aus Z2-R darauf angewandt: die einzige nichttriviale Klasse
   ({`P-01`, `P-11`}) liegt **vollständig in K3 × B1** und berührt keines der fünf.
3. Zahl der Klassen: **fünf**.

> **N₁ = 5**

**Zahlenvergleich gegen die Schwelle**, ohne Entscheidung: **N₁ = 5 ≤ 50**. Die
**Entscheidung I3 fällt datiert am 13.09.2026 durch den Autor.**

**Pro-Lauf-Dedup aller sechs Läufe** (§6 Z2-R verlangt Pro-Lauf-Dedup und laufübergreifende
Wiederkehr **getrennt**):

| Lauf | roh | pro-Lauf-Dedup |
|---|---|---|
| K2 × B1 `run0` | 5 | **5** ← N₁ |
| K2 × B1 `run1` | 5 | 5 |
| K2 × B1 `run2` | 5 | 5 |
| K3 × B1 `run0` | 4 | 4 |
| K3 × B1 `run1` | 3 | 3 |
| K3 × B1 `run2` | 5 | 5 |

### Die Verteilungen

**Bezugsmenge, ausdrücklich:** „nach inhaltlicher Dedup“ heisst **Äquivalenzklassen nach
Z2-R** — gepoolt **16**, K2 × B1 **5**, K3 × B1 **11**. Die Rohzahlen daneben sind die
**17 Etiketten** (mechanisch verschieden, ohne Z2-R) bzw. die **27 Vorschlagsinstanzen**
der sechs Läufe.

**(a) Z2-G Gehalt** — „unklar“ als **eigene** Spalte, keiner Seite zugeschlagen (§6):

| Bezugsmenge | Spiegelung | negierte Spiegelung | normativ | unklar |
|---|---|---|---|---|
| **gepoolt, nach Dedup (16)** | 1 | **0** | 13 | 2 |
| **K2 × B1, nach Dedup (5)** | 0 | **0** | 5 | 0 |
| **K3 × B1, nach Dedup (11)** | 1 | **0** | 8 | 2 |
| gepoolt, roh (17 Etiketten) | 1 | **0** | 14 | 2 |
| K2 × B1, roh (5) | 0 | **0** | 5 | 0 |
| K3 × B1, roh (12) | 1 | **0** | 9 | 2 |

**(b) Z2-P Prüfbarkeit**:

| Bezugsmenge | prüfbar | nicht prüfbar |
|---|---|---|
| **gepoolt, nach Dedup (16)** | 11 | 5 |
| **K2 × B1, nach Dedup (5)** | 0 | 5 |
| **K3 × B1, nach Dedup (11)** | 11 | 0 |
| gepoolt, roh (17 Etiketten) | 12 | 5 |

**Die von §6 zwingend verlangte Trennung der Ursachen** — alle fünf „nicht prüfbar“
stammen aus **K2 × B1**; die Ursache steht wörtlich, wie vom Bewerter vermerkt:

| Etikett | Ursache ein **EXTERNER Import** (registrierter Preis der Stufe 0b)? | Ursache, wörtlich |
|---|---|---|
| `P-04` | **ja** | „URSACHE (Pflichtvermerk §6): `logging` ist ein EXTERNES Importziel; externe Ziele haben nach der Stufe-0b-Kürzung keine Kante im Ist-Modell und keinen Signaturniederschlag. Folge der registrierten Kürzung, kein Modellfehler“ |
| `P-05` | nein | „nicht operationalisiert („consistent style“); Docstrings sind mit Stufe 0 aus der Eingabe gezogen“ |
| `P-06` | nein | „Logikduplikation ist nur im Funktionskörper sichtbar, nicht in Kanten oder Signaturen“ |
| `P-12` | nein | „„logical modules“, „single responsibility“ nicht operationalisiert“ |
| `P-15` | nein | „„common pattern“, Lokalisierung und Nutzerfreundlichkeit von Meldungen liegen nicht in der Evidenzbasis“ |

> **1 von 5** externer Import · **4 von 5** andere Ursachen.

**(c) `kind`** — bewertet, nicht vorgegeben (§6):

| Bezugsmenge | `structural` | `semantic` |
|---|---|---|
| **gepoolt, nach Dedup (16)** | 6 | 10 |
| **K2 × B1, nach Dedup (5)** | 1 | 4 |
| **K3 × B1, nach Dedup (11)** | 5 | 6 |
| gepoolt, roh (17 Etiketten) | 7 | 10 |

**(d) Z2-Z** — die sechs Ebene-1-Kategorien einzeln, „sonstige“ und „keiner der sechs“
**getrennt** (§6, Ergänzung 02.09.2026):

| Bezugsmenge | `FORBIDDEN_RELATION` | `CYCLE` | `ABSENCE_REQUIRED` | `FORBIDDEN_SIGNATURE_TYPE` | `STRUCTURAL_PLACEMENT` | `API_CONTRACT` | sonstige | keiner der sechs |
|---|---|---|---|---|---|---|---|---|
| **gepoolt, nach Dedup (16)** | 6 | 0 | 0 | 0 | 0 | 0 | **8** | **2** |
| **K2 × B1, nach Dedup (5)** | 1 | 0 | 0 | 0 | 0 | 0 | **4** | **0** |
| **K3 × B1, nach Dedup (11)** | 5 | 0 | 0 | 0 | 0 | 0 | **4** | **2** |
| gepoolt, roh (17 Etiketten) | 7 | 0 | 0 | 0 | 0 | 0 | **8** | **2** |

### Abdeckungsmatrix (§7 Punkt 3)

**Das Kriterium des Protokolls ist enger als das Wort „belegt“ nahelegt.** §7 Punkt 3
lautet wörtlich: *„welche Klassen tauchen überhaupt auf (**≥ 1 normativer, prüfbarer
Vorschlag**)?“* — also **normativ UND prüfbar**. Beide Lesarten stehen hier, die
protokollgemässe zuerst.

| Kategorie | gepoolt, streng (≥ 1 normativ **und** prüfbar) | K2 × B1, streng | K3 × B1, streng | gepoolt, weit (≥ 1 Vorschlag) |
|---|---|---|---|---|
| `FORBIDDEN_RELATION` | **belegt** | — | **belegt** | **belegt** |
| `CYCLE` | — | — | — | — |
| `ABSENCE_REQUIRED` | — | — | — | — |
| `FORBIDDEN_SIGNATURE_TYPE` | — | — | — | — |
| `STRUCTURAL_PLACEMENT` | — | — | — | — |
| `API_CONTRACT` | — | — | — | — |
| **Summe belegt** | **1 von 6** | **0 von 6** | **1 von 6** | **1 von 6** |

**Zwingend mitzuführen, als Zahl ohne Deutung:** die Matrix stützt sich gepoolt auf
**16** Vorschläge (K2 × B1: **5**, K3 × B1: **11**). Bei dieser Vorschlagszahl wären
**6** der sechs Kategorien überhaupt besetzbar — in K2 × B1 mit fünf Vorschlägen nur **5**.

### Grenzfallquote (§7 Punkt 7)

| Bezugsmenge | Grenzfälle | Anteil |
|---|---|---|
| **gepoolt, 17 Etiketten** | **11** | **64,71 %** |
| **K2 × B1, 5 Etiketten** | **1** (`P-04`) | **20,00 %** |
| **K3 × B1, 12 Etiketten** | **10** | **83,33 %** |
| gepoolt, 16 Klassen nach Z2-R | 11 | 68,75 % |

Die **Grenzfall-Tabelle (Anhang B)** trägt **14 Zeilen** auf diese **11 Etiketten** — ein
Etikett kann **mehrere Kriterien** tragen (`P-08`, `P-09`, `P-13` je zwei). Die Tabelle
steht vollständig im Blatt, Abschnitt 6, und ist nach §7 Punkt 7 **vollständig
auszuweisen, nicht nur zu zählen**.

**Zur Kenntnis, ohne Deutung:** der mit **G1** (31.08.2026, Amendment §11) **entfallene**
Zweitbewerter-Trigger lag bei **20 %**. Fundstelle: `z2_protokoll_regelableitung.md` §6,
durchgestrichene „**Zweitbewerter-Regel (vorregistriert)**“ — „*Übersteigt der Anteil der
Grenzfälle 20 % der deduplizierten Vorschläge …*“; die geltende Fassung sagt in §6 Punkt 3
ausdrücklich: „**Kein Trigger, keine Pflicht.**“ Die Zahl wird hier genannt, **weil der
Auftrag es verlangt**, und **löst nichts aus**.

### Stabilität (§7 Punkt 4), je Zelle getrennt

| Zelle | Klassen | mit Wiederkehr ≥ 2 von 3 | Anteil |
|---|---|---|---|
| **K2 × B1** | 5 | **5** | **100 %** |
| **K3 × B1** | 11 | **1** | **9,09 %** |

**DETERMINISMUSVERMERK, verbindlich mitzuführen:** in der Zelle **K2 × B1** sind die drei
Generate **zeichengleich** — SHA256 `f71c9c743093e0c3…` über `choices[0].message.content`,
2 356 Zeichen (Fundstelle: dieses Manifest, Abschnitt „Formbefund ohne Deutung: die drei
Generate sind zeichengleich“). Die Wiederkehr ist dort daher **konstruktiv 3/3 für jeden
Vorschlag**. **Die Größe misst in dieser Zelle Determinismus und nicht Wiederkehr über
unabhängige Ziehungen.** In **K3 × B1** sind die Generate **verschieden**
(`f3514cf678fc7bec…` / `2ffde87ee71cd79c…` / `1fe29dd6972bd5f6…`). **Die Zahlen der beiden
Zellen werden NICHT zusammengefasst und NICHT gegeneinander gerechnet.**

Die eine wiederkehrende Klasse in K3 × B1 ist **{`P-01`, `P-11`}** — `run0` und `run1`,
also **2/3**.

### Granularität — BEOBACHTUNG, ausdrücklich KEIN Kriterium

| Bezugsmenge | package | module | artefact | unresolved |
|---|---|---|---|---|
| **K2 × B1** (5 Etiketten), Summe der `scope`-Einträge | 20 | 0 | 0 | 0 |
| **K3 × B1** (12 Etiketten), Summe | 17 | 15 | 0 | 0 |
| **gepoolt** (17 Etiketten), Summe | 37 | 15 | 0 | 0 |
| K2 × B1: Etiketten mit mindestens einem | 5 | 0 | 0 | 0 |
| K3 × B1: Etiketten mit mindestens einem | 8 | 4 | 0 | 0 |

### Ladbarkeit (§7 Punkt 8) — DURCHGEFÜHRT

> **16 von 16** deduplizierten Vorschlägen werden von `parseArchitectureRules`
> **angenommen** (auf Etikettenbasis 17 von 17; ebenso alle 17 in **einem** Array).
> **Keine Ablehnung, kein Fehler.**

Die Umschreibung ist **genau EINE Feldeinfügung**: das vom Bewerter zugewiesene `kind` zu
den fünf vorhandenen Feldern; `id`, `category`, `scope`, `statement` und `severity`
unverändert, `predicate` bleibt leer (zulässig: `types.ts:44`, `rules.ts:77`).

**Ausführung nur lesend** gegen den Messworktree `~/ma/tritongraph-measure` (detached auf
`348ca9d`), Import **direkt aus `rules.ts`**, **nicht** über die Paket-Barrel `index.ts`
(sie lädt `llmClient` mit). **Kein Commit, kein Bau, kein `npm install`**; `git status` war
in `~/ma/tritongraph-measure` **und** in `~/ma/tritongraph` vorher und nachher **leer**,
HEAD unverändert `348ca9d`.

**Abweichung vom vorgeschlagenen Werkzeug, zu registrieren:** der im Auftrag genannte `tsx`
aus `tools/ts-to-ilograph/node_modules/.bin/` (er liegt in `~/ma/tritongraph`, nicht in
`masterarbeit`) ist auf dieser Maschine **unbrauchbar** — sein `esbuild` ist als
`@esbuild/darwin-arm64` installiert, der Host ist `linux-x64`; ein `npm install` in
`tritongraph` ist ausgeschlossen. Gefahren wurde stattdessen mit dem **Type-Stripping von
Node v22.23.2** selbst. Das lädt **dieselbe** `rules.ts` und braucht **kein** Werkzeug aus
`tritongraph`. **Eine Nachbildung des Parsers in Python fand NICHT statt** — sie war
ausgeschlossen und wäre eine andere Messung.

### T-Z2-10 — textliche Nähe zum Ausgabebeispiel aus Anhang A A3

**Erhoben wird die textliche Nähe. Es wird KEINE Aussage getroffen, ob ein Vorschlag aus
dem Beispiel stammt.** T-Z2-10 ist der registrierte Threat, unter dem der Autor sie
einordnet.

Maß: `difflib.SequenceMatcher.ratio` über NFC-normalisierte, kleingeschriebene
`statement`-Texte. Die drei höchsten Werte:

| Rang | Etikett | Bedingung | ratio |
|---|---|---|---|
| 1 | **`P-04`** | **K2 × B1** | **0,7414** |
| 2 | `P-16` | K3 × B1 | 0,4967 |
| 3 | `P-10` | K3 × B1 | 0,4407 |

**Beispiel (Anhang A A3, eingefroren):** `category` `logging-discipline`, `severity`
`warning`, `scope.components` `["shop.web", "shop.jobs"]`,
`statement` „*Modules in these components must not import the standard logging module
directly. They obtain a logger from the shared logging helper instead.*“

**`P-04`:** `category` `dependency-management`, `severity` `warning`, `scope.components`
`depot.billing.api` · `depot.billing.services` · `depot.billing.repository` ·
`depot.billing.models`, `statement` „*Classes and functions within the billing components
must not directly import the standard logging module. Instead, they should obtain a logger
from a shared logging helper module.*“

**Felderabgleich:** `severity` **gleich** (`warning`) · `category` **verschieden** ·
`scope.components` **verschieden**. Der vollständige Wortdiff steht in
`bewertung/auswertung.json` unter `t_z2_10_textliche_naehe.hoechster`.

### Methodendetail für Kapitel 6, hier registriert

**Der Bewerter hat während der Bewertung Code und Eingaben des Testrepos eingesehen.** Das
ist **mit der Verblindung vereinbar** — sie richtet sich gegen **Bedingungs- und
Modellkennzeichnung**, nicht gegen das **Repositorium**; für **Z2-G** („verbietet
Realisiertes“) ist der Blick auf das **Ist** notwendig. **Kein Threat**, aber ein zu
berichtendes **Methodendetail**.

### Was dieser Block NICHT tut

- **§7 Punkt 5 steht aus** — der Überlapp mit den **sechzehn** autorenformulierten
  Statements wurde **nicht** erhoben; „sinngemäß vorgeschlagen“ ist eine **Bewerterleistung**.
- **Die Verdikte zu E1–E4 und Befund 09 stehen aus** — sie schreibt der **Autor**.
- **Die Entscheidung I3 fällt datiert am 13.09.2026.**
- **Keine Nachbewertung:** keine Dimension wurde korrigiert, ergänzt, plausibilisiert oder
  hinterfragt. Was auffiel, steht oben als **gemeldet, nicht geändert**.

Er ändert **nichts** an `eingaben/`, `messungen/`, `k2_b1/`, `k3_b1/`, an
`bewertungsblatt.md`, an `zuordnungsschluessel.json`, an `tools/run_z2.py` oder am
eingefrorenen Protokoll.

### Ablage, ergänzt

```
data/z2/
  bewertung/
    SHA256SUMS                  ← hasht ALLES im Block ausser sich selbst
    auswertung.json             ← NEU (S11): alle Größen aus §7, je mit Bezugsmenge
    bewertungsblatt.md          ← unverändert seit `9b6c76b`
    zuordnungsschluessel.json   ← unverändert seit `b17fc98`
```

| Datei | SHA256 |
|---|---|
| `bewertung/auswertung.json` | `309d02476332106aefeb518b79f4e99a1979a9540ec69f35c13ffbd61d1bab1e` |
| `bewertung/bewertungsblatt.md` | `72ebc3170f484a391a1d991c4fa155d57d04f6bfc5374c609ac8d601c109c029` (unverändert) |
| `bewertung/zuordnungsschluessel.json` | `0215a8b2ed377df1e4e074dd5f489c58a7341fc93e54362b61fcef8b78a320f2` (unverändert) |
| `tools/tally_z2_review.py` (Erzeuger, ausserhalb des Blocks) | `0fc7de59789b0b2e9fb3b93fe1100c5464cdd720b02b76a81ccf4b59c678bbfc` |

**Nachzug, der in `9b6c76b` fehlte und hier vollzogen wird:** `bewertung/SHA256SUMS` trug
bis zu diesem Commit den Hash des **leeren** Blattes (`4db42263…`). Das Ausfüllen in
`9b6c76b` hat den Hash nicht nachgezogen; der Bytestand des ausgefüllten Blattes war
dadurch **unbezeugt**. `sha256sum -c` schlug im Block entsprechend fehl. Mit diesem Commit
steht dort `72ebc317…`, und der Block läuft durch. **Der Hash des Schlüssels ist
unverändert** — er wurde gelesen, nicht geschrieben.

---

## Überlappmatrix §7 Punkt 5 (Auftrag S12, 04.09.2026)

### Zweck

Das Blatt `bewertung/ueberlappmatrix.md` ist das **Erhebungsblatt** für die sekundäre,
deskriptive Größe des **§7 Punkt 5**: „**n von 16 autorenformulierten Statements wurden
sinngemäß vorgeschlagen**“. Es stellt je Soll-Statement einen Abschnitt bereit — Soll-ID,
`category`, `kind`, `severity`, `scope.components`, `statement` zeichengleich,
`predicate` falls vorhanden — dazu die **16 bewerteten Vorschläge als Nachschlageteil**,
einen **maschinellen Vorbefund** und drei **leere** Felder je Statement.

~~**Die Matrix ist LEER.** Die drei Spalten — „vorgeschlagen?“, „durch welche(s) P-xx“,
„Begründung“ — sind **nicht ausgefüllt, nicht vorbelegt und nicht angedeutet**, auch
nicht durch Sortierung, Hervorhebung oder eine Ähnlichkeitszahl. **Es wurde kein
Textvergleich, kein Ranking und keine Kandidatenzuordnung vorgenommen.**~~
— **überholt am 04.09.2026 (Auftrag S12, zweite Fassung).** Der erste Lauf des Auftrags
(Commit `e520a45`) erzeugte das Blatt **ohne** Vorbefund; die überarbeitete
Auftragsfassung verlangt die **Nachschlagearbeit** ausdrücklich. Was gilt, steht im
Abschnitt „**Das zweistufige Verfahren**“ unten. **Unverändert gilt:** kein
Ähnlichkeitsmaß, kein `ratio`, kein Ranking, keine Sortierung nach Nähe — und **die drei
Entscheidungsspalten sind LEER**.

**Die drei Entscheidungsspalten sind LEER.** „**ENTSCHEIDUNG (ja | nein)**“, „**durch
welche(s) P-xx**“ und „**Begründung des Autors**“ sind **nicht ausgefüllt und nicht
vorbelegt**. Der **Vorbefund** steht in eigenen, als **MASCHINELL** gekennzeichneten
Feldern, **sichtbar davon getrennt**.

### Nenner 16 — aus der Datei gezählt, nicht übernommen

`data/soll/architecture-rules.yaml`, SHA256
`72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` — geprüft gegen
`data/soll/SHA256SUMS`, unverändert; die Datei wurde **nur gelesen**.

| `category` | Zahl |
|---|---|
| `FORBIDDEN_RELATION` | 4 |
| `ABSENCE_REQUIRED` | 4 |
| `API_CONTRACT` | 4 |
| `CYCLE` | 2 |
| `FORBIDDEN_SIGNATURE_TYPE` | 1 |
| `STRUCTURAL_PLACEMENT` | 1 |
| **Summe** | **16** |

**Die gezählte Verteilung stimmt mit der in §7 Punkt 5 registrierten überein** — der
registrierte Nenner trägt. Die Reihenfolge der Abschnitte ist die **Dateireihenfolge**,
**nicht nach Kategorie gruppiert**: eine Gruppierung wäre bereits eine Lesehilfe in eine
Richtung.

### Die Auslegung von „sinngemäss“, im Blatt registriert

**Derselbe Sachverhalt wird verboten oder gefordert — unabhängig von Wortlaut,
Kategorielabel und Scope-Granularität.** NICHT verlangt sind derselbe Wortlaut, dieselbe
Kategorie oder dieselbe Präzision. Fasst ein Vorschlag den Sachverhalt **BREITER** als
das Soll-Statement, zählt er **MIT VERMERK**; fasst er ihn enger oder trifft er nur einen
Teil, ist das in der Begründung auszuweisen. **Mehrfachnennung ist zulässig:** ein
Vorschlag kann mehreren Statements entsprechen und umgekehrt.

### Das zweistufige Verfahren — Vorbefund maschinell, ENTSCHEIDUNG durch den Autor

*(neu 04.09.2026, Auftrag S12 zweite Fassung)*

**Stufe 1 — maschinell.** Je Soll-Statement trägt das Blatt einen **VORBEFUND
(MASCHINELL, kein Ergebnis)** mit vier Feldern: **(a)** das Verdikt „Kandidat vorhanden“
oder „kein Kandidat“, **(b)** die **Etiketten** der Vorschläge, die über denselben
Sachverhalt sprechen, **(c)** eine **Begründung**, die bei einem Kandidaten ausweist, wo
Reichweite oder Granularität abweichen, und **(d)** eine **PRÜFSPUR** mit den erwogenen
und ausgeschlossenen Etiketten, je mit Grund. **Die Prüfspur ist Pflicht** — auch und
besonders bei „kein Kandidat“: sie macht die Nachschlagearbeit **gegenlesbar**, statt nur
ein Ergebnis zu behaupten.

**Stufe 2 — der Autor, je Zeile.** Die drei Entscheidungsfelder sind **leer**. **Der
Autor bestätigt oder überstimmt JEDE der sechzehn Zeilen; eine unbestätigte Zeile gilt
nicht als entschieden.** Der Vorbefund ist ein **Vorschlag, keine Feststellung**, und
sprachlich entsprechend gehalten („spricht über denselben Sachverhalt“, „Kandidat“, „zu
prüfen“ — nicht „entspricht“, „deckt sich“, „ist erfüllt“).

**Warum zweistufig.** „Sinngemäss“ ist **dieselbe Urteilsart wie das Z2-R-Kriterium**
(§6: Duplikate bei Übereinstimmung in **Kategorie, Scope und Kernaussage**). **Z2-R wurde
in S10 ausdrücklich NICHT maschinisiert** — die Zusammenführung war dort auf
**Zeichengleichheit** beschränkt, damit das Werkzeug **keine inhaltliche Entscheidung
abnimmt**. Damit **beide Größen konsistent behandelt** werden, entscheidet der Autor auch
hier je Zeile; das Werkzeug leistet die **Nachschlagearbeit** und legt seine **Prüfspur
offen**.

**Der Maßstab, im Blatt registriert:** „**derselbe Sachverhalt wird verboten oder
gefordert**“ — unabhängig von Wortlaut, Kategorielabel und Scope-Granularität. **Kein
Ähnlichkeitsmaß, kein `ratio`, kein Ranking, keine Sortierung nach Nähe:** der Vorbefund
ist eine **Sachverhaltsprüfung, kein Textvergleich**. Kandidaten und Prüfspur stehen in
**Etikettreihenfolge**. Die Vorbefunde liegen im Werkzeug als **Datenkonstanten**; eine
Formprüfung (`check_vorbefunde`) bricht ab, wenn eine Zeile ohne Vorbefund, ohne
Begründung oder **ohne Prüfspur** bliebe oder ein Etikett nennt, das keine gelesene
Z2-R-Klasse ist.

**In diesem Manifest steht KEINE Summe über die Vorbefunde.** Eine solche Zahl würde als
Ergebnis gelesen, obwohl keine einzige Zeile entschieden ist.

### Die Einhegung — mitregistriert, nicht nachgereicht

- **Sekundär und deskriptiv**, wörtlich aus §7 Punkt 5: „**Der Charakter der Größe bleibt
  unverändert:** sekundär, deskriptiv. Ausdrücklich KEIN Korrektheits- oder Recall-Maß
  (Autor beider Seiten; gleiche Logik wie Gold-Degradierung in Befund 01).“
- **KEIN Recall-Maß.** **Der Autor hat beide Seiten formuliert** — die sechzehn
  Soll-Statements **und** das Messobjekt, auf das sie passen. Die Zahl darf **nie** als
  „das Modell hat n von 16 Regeln gefunden“ gelesen werden, sondern **nur** als „n
  Statements haben eine Entsprechung unter den Vorschlägen“.
- **T-Z2-8:** die **Affordanzen der sechs Kategorien stecken strukturell im Testrepo**.
  Eine hohe Überschneidung wäre **insoweit Eigenschaft des Messobjekts**.
- **Abgrenzung zu §7 Punkt 3:** die Abdeckungsmatrix fragt nach den **sechs KATEGORIEN**
  (Nenner 6, in `bewertung/auswertung.json` bereits ausgezählt), §7 Punkt 5 nach den
  **sechzehn EINZELNEN Statements** (Nenner 16, steht aus). **Verschiedene Größen,
  verschiedene Nenner — nicht gegeneinander zu rechnen.**

### Aufgehobene Verblindung — vermerkt

Der Nachschlageteil **nennt die Herkunft je Klasse** (`k2_b1` / `k3_b1` samt Läufen). Das
ist zulässig, weil der Zuordnungsschlüssel mit **S11** aufgelöst wurde und die Bewertung
zu diesem Zeitpunkt abgeschlossen war. **Die Größe des §7 Punkt 5 ist nicht
bedingungsvergleichend**; wird sie je Zelle aufgeschlüsselt, geschieht das **nach
Aufhebung der Verblindung**, und **das ist zu berichten**.

### Was dieser Block NICHT tut

- ~~**Die Matrix ist LEER** — keine Zeile ist ausgefüllt, keine Zuordnung
  vorgeschlagen.~~ — **überholt 04.09.2026 (S12, zweite Fassung).** Es gilt: **die drei
  ENTSCHEIDUNGSSPALTEN sind LEER** — keine Zeile ist **entschieden**. Der maschinelle
  Vorbefund benennt Kandidaten und ist ausdrücklich **kein Ergebnis**.
- ~~**Die Größe „n von 16“ steht aus** — sie bildet der Autor beim Ausfüllen der
  Entscheidungsfelder, **nicht** aus den Vorbefunden; **S13** rechnet sie mechanisch
  nach. Das Summenfeld im Blatt ist **leer**.~~ — **überholt 06.09.2026 (S13):** die
  Entscheidungsfelder sind ausgefüllt (`5ad1cb8`) und mechanisch ausgezählt; das Ergebnis
  steht im Block **„Überlapp §7 Punkt 5 — Ergebnis"** unten. **Das Summenfeld in Teil 4
  des Blattes ist unausgefüllt geblieben** und wurde von S13 **nicht** nachgetragen —
  das Blatt wird nicht geändert.
- **Die Verdikte zu E1–E4 und Befund 09 stehen aus** — sie schreibt der Autor.
- **Kein Ähnlichkeitsmaß** zwischen Soll-Statements und Vorschlägen, in keiner Form.
- **Kein Modell-Call, kein Messlauf, keine Deutung.**

Er ändert **nichts** an `data/soll/**`, an `eingaben/`, `messungen/`, `k2_b1/`, `k3_b1/`,
an `bewertungsblatt.md`, an `zuordnungsschluessel.json`, an `auswertung.json`, an
`tools/run_z2.py`, `tools/prepare_z2_review.py`, `tools/tally_z2_review.py` oder am
eingefrorenen Protokoll.

### Ablage, ergänzt

```
data/z2/
  bewertung/
    SHA256SUMS                  ← hasht ALLES im Block ausser sich selbst
    auswertung.json             ← S13: um `ueberlapp_p5` ergänzt (bis dahin
                                  unverändert seit `7dd8a05`)
    bewertungsblatt.md          ← unverändert seit `9b6c76b`
    ueberlappmatrix.md          ← S12: Blatt zu §7 Punkt 5, Vorbefund
                                  maschinell, Entscheidungsspalten LEER
    zuordnungsschluessel.json   ← unverändert seit `b17fc98`
```

| Datei | SHA256 |
|---|---|
| `bewertung/ueberlappmatrix.md` | ~~`9df43ab9…` (erste Fassung, `e520a45`)~~ ~~`b2b3144f…` (S12, Entscheidungsfelder leer)~~ `57031cb7515519d91184d4111588c60025175f6d815a66549ccaa03acf7abe23` (**vom Autor ausgefüllt**, `5ad1cb8`; von S13 nur gelesen, der Hash in S13 nachgezogen) |
| `bewertung/auswertung.json` | ~~`309d0247…` (Stand S12)~~ `ed75e49d797dfda69931f390fef86818c0f4e6e63d42458da4cc41258e71043e` (S13, Abschnitt `ueberlapp_p5` ergänzt) |
| `bewertung/bewertungsblatt.md` | `72ebc3170f484a391a1d991c4fa155d57d04f6bfc5374c609ac8d601c109c029` (unverändert) |
| `bewertung/zuordnungsschluessel.json` | `0215a8b2ed377df1e4e074dd5f489c58a7341fc93e54362b61fcef8b78a320f2` (unverändert) |
| `tools/prepare_z2_overlap.py` (Erzeuger, ausserhalb des Blocks) | ~~`4b8e4b55…` (erste Fassung)~~ `ee31664321b105a3111946ec72e66518a253eb2d2146f9aeb2a54491366b7c06` |

**Determinismus:** `tools/prepare_z2_overlap.py --check` erzeugt das Blatt in ein
temporäres Verzeichnis neu und vergleicht byteweise; zwei Läufe liefern denselben SHA256
`b2b3144f…`. Stdlib plus **PyYAML 6.0.1** (im System vorhanden, nach S0-6c); ein
minimaler eigener Leser für diese eine Datei liegt als Rückfallweg im Werkzeug und liefert
dieselben 16 Regeln.

---

## Überlapp §7 Punkt 5 — Ergebnis

**Auftrag S13 · 06.09.2026 · Werkzeug `tools/tally_z2_overlap.py` · MECHANISCHE
AUSZÄHLUNG OHNE DEUTUNG UND OHNE NACHBEWERTUNG**

Die Überlappmatrix ist vom Autor ausgefüllt (Commit `5ad1cb8`, alle sechzehn Zeilen
entschieden). S13 **liest** das Blatt, prüft es auf Vollständigkeit und Konsistenz und
zählt aus. **Keine Entscheidung des Autors wurde korrigiert, ergänzt, plausibilisiert
oder aus der Zählung genommen.** Das Blatt selbst, `bewertungsblatt.md` und
`zuordnungsschluessel.json` sind **bytegleich** geblieben.

### Die Zahl

> **7 / 16** — **sieben von sechzehn autorenformulierten Statements haben eine
> Entsprechung unter den Vorschlägen.**

**Herleitung:** die Zahl der Abschnitte in Teil 3 des Blattes mit Entscheidungsfeld „ja“.
Die Zahl wird als **Bruch `n / 16` und ohne Prozentangabe** geführt — bei sechzehn Fällen
wäre eine Prozentzahl Scheingenauigkeit.

| Entscheidung | Soll-IDs |
|---|---|
| **ja** (7) | `R-LAYER-1` · `R-PROTECT-1` · `R-INDEP-1` · `R-PORT-1` · `R-PORT-2` · `R-PORT-3` · `R-PORT-4` |
| **nein** (9) | `R-CORE-1` · `R-CYCLE-1` · `R-CYCLE-2` · `R-FRAMEWORK-1` · `R-PLACE-1` · `R-SIG-1` · `R-SIG-2` · `R-SIG-3` · `R-SIG-4` |

**Summenfeld des Blattes:** Teil 4 trägt weiterhin den Platzhalter `___` — der Autor hat
es nicht ausgefüllt. Ein Gegenhalten der eigenen Zählung gegen eine Autorenzahl war
deshalb **nicht möglich**; maßgeblich ist die mechanische Zählung. **Das Blatt wurde
nicht geändert.**

### Aufschlüsselung je Soll-Kategorie

**Bezugsmenge:** die 16 Statements; die Nenner sind aus `data/soll/architecture-rules.yaml`
gezählt.

| `category` | mit Entsprechung | Bezugsmenge |
|---|---|---|
| `FORBIDDEN_RELATION` | 3 | 4 |
| `ABSENCE_REQUIRED` | 4 | 4 |
| `API_CONTRACT` | 0 | 4 |
| `CYCLE` | 0 | 2 |
| `FORBIDDEN_SIGNATURE_TYPE` | 0 | 1 |
| `STRUCTURAL_PLACEMENT` | 0 | 1 |
| **Summe** | **7** | **16** |

### Aufschlüsselung je Bedingung

**Bezugsmenge:** die **7** Statements mit Entscheidung „ja“, aufgeschlüsselt nach der
Herkunft der vom Autor genannten Vorschlagsklassen.

| Herkunft | Zahl | Soll-IDs |
|---|---|---|
| `k3_b1` | 7 | `R-LAYER-1` · `R-PROTECT-1` · `R-INDEP-1` · `R-PORT-1` · `R-PORT-2` · `R-PORT-3` · `R-PORT-4` |
| `k2_b1` | 0 | — |
| beide | 0 | — |

**Vermerk zur aufgehobenen Verblindung:** der Zuordnungsschlüssel ist mit **S11**
aufgelöst; die Bewertung war zu diesem Zeitpunkt abgeschlossen. **Diese Aufschlüsselung
entsteht danach und wird als solche berichtet.** §7 Punkt 5 ist **sekundär und
deskriptiv, nicht bedingungsvergleichend** — die Aufschlüsselung wird **ohne
Vergleichsaussage** geführt.

### Mehrfachnennungen, in beide Richtungen

**Bezugsmenge:** die 7 Statements mit Entscheidung „ja“.

| Richtung | Eintrag |
|---|---|
| Klasse für **mehrere Statements** genannt | `P-01 + P-11` → `R-PROTECT-1`, `R-PORT-1`, `R-PORT-2`, `R-PORT-3`, `R-PORT-4` (fünf) · `P-14` → `R-LAYER-1`, `R-PROTECT-1` (zwei) |
| Statement nennt **mehrere Klassen** | `R-PROTECT-1` → `P-01 + P-11`, `P-14` · `R-INDEP-1` → `P-02`, `P-07` |

**In keiner Zeile genannt** — Bezugsmenge: die 16 Z2-R-Äquivalenzklassen der bewerteten
Vorschläge. **Zwölf von sechzehn:** `P-03` · `P-04` · `P-05` · `P-06` · `P-08` · `P-09` ·
`P-10` · `P-12` · `P-13` · `P-15` · `P-16` · `P-17`.

### Überstimmungsquote — der maschinelle Vorbefund gegen die Entscheidung des Autors

**Bezugsmenge:** alle 16 Zeilen. Die Kennzahl des **zweistufigen Verfahrens**: Stufe 1
war die maschinelle Nachschlagearbeit aus S12 (Vorbefund, Kandidaten, Begründung,
Prüfspur), Stufe 2 die Entscheidung des Autors je Zeile. Ausgezählt wird **ausschliesslich
Stufe 2**.

| Vorbefund | Entscheidung | Zahl | Soll-IDs |
|---|---|---|---|
| Kandidat vorhanden | ja (bestätigt) | **7** | `R-LAYER-1` · `R-PROTECT-1` · `R-INDEP-1` · `R-PORT-1` · `R-PORT-2` · `R-PORT-3` · `R-PORT-4` |
| Kandidat vorhanden | nein (überstimmt, verworfen) | **0** | — |
| kein Kandidat | ja (überstimmt, ergänzt) | **0** | — |
| kein Kandidat | nein (bestätigt) | **9** | `R-CORE-1` · `R-CYCLE-1` · `R-CYCLE-2` · `R-FRAMEWORK-1` · `R-PLACE-1` · `R-SIG-1` · `R-SIG-2` · `R-SIG-3` · `R-SIG-4` |

**Etikettvergleich bei „ja“ mit Kandidat** — hat der Autor die Kandidaten des Vorbefunds
übernommen oder andere genannt?

| Soll-ID | Kandidaten des Vorbefunds | vom Autor genannt | Verhältnis |
|---|---|---|---|
| `R-LAYER-1` | `P-07`, `P-14` | `P-14` | **echte Teilmenge** — `P-07` nicht übernommen |
| `R-PROTECT-1` | `P-01 + P-11`, `P-14` | `P-01 + P-11`, `P-14` | deckungsgleich |
| `R-INDEP-1` | `P-02`, `P-07` | `P-02`, `P-07` | deckungsgleich |
| `R-PORT-1` | `P-01 + P-11` | `P-01 + P-11` | deckungsgleich |
| `R-PORT-2` | `P-01 + P-11` | `P-01 + P-11` | deckungsgleich |
| `R-PORT-3` | `P-01 + P-11` | `P-01 + P-11` | deckungsgleich |
| `R-PORT-4` | `P-01 + P-11` | `P-01 + P-11` | deckungsgleich |

Diese Zahlen sind für Kapitel 6 zu berichten; sie belegen, ob der Vorbefund
Nachschlagearbeit oder faktische Vorentscheidung war. **Hier steht keine Deutung dazu.**

### Die Einhegung

1. **Sekundär und deskriptiv** (§7 Punkt 5) — die Größe steht **neben** den Punkten 1–4
   des §7, nicht über ihnen.
2. **KEIN Korrektheitsmaß und KEIN Recall-Maß.** **Der Autor hat beide Seiten
   formuliert** — die sechzehn Soll-Statements **und** das Messobjekt, auf das sie
   passen (§7 Punkt 5, gleiche Logik wie die Gold-Degradierung in Befund 01).
3. **Die Zahl heisst ausschliesslich:** „7 von 16 autorenformulierten Statements haben
   eine Entsprechung unter den Vorschlägen“ — **nie** „das Modell hat 7 von 16 Regeln
   geliefert“ und in keiner Formulierung, die die Größe als Leistung liest.
4. **T-Z2-8:** die **Affordanzen der sechs Kategorien stecken strukturell im Testrepo**.
   Eine hohe Überschneidung wäre **insoweit Eigenschaft des Messobjekts**, nicht Leistung
   des Modells.

### Abgrenzung zu §7 Punkt 3

Die **Abdeckungsmatrix** (§7 Punkt 3, dort **1 von 6**) fragt, welche der sechs
**KATEGORIEN** durch mindestens einen normativen, prüfbaren Vorschlag belegt sind;
**§7 Punkt 5** fragt nach Entsprechungen zu den sechzehn **EINZELNEN Statements**.
**Verschiedene Größen, verschiedene Nenner — nicht zu verwechseln, nicht gegeneinander
zu rechnen.**

### Was aussteht

- **Die Verdikte zu E1–E4 stehen aus.**
- **Befund 09 steht aus.**
- **Die Entscheidung I3 fällt datiert am 13.09.2026.**

### Ablage und Bytestand

| Datei | SHA256 |
|---|---|
| `bewertung/auswertung.json` | `ed75e49d797dfda69931f390fef86818c0f4e6e63d42458da4cc41258e71043e` (Abschnitt `ueberlapp_p5` ergänzt; die bestehenden Abschnitte unverändert) |
| `bewertung/ueberlappmatrix.md` | `57031cb7515519d91184d4111588c60025175f6d815a66549ccaa03acf7abe23` (Autorenfassung `5ad1cb8`, von S13 nur gelesen; der Hash war in `5ad1cb8` nicht nachgezogen und wird hier nachgetragen — Präzedenz S11) |
| `bewertung/bewertungsblatt.md` | `72ebc3170f484a391a1d991c4fa155d57d04f6bfc5374c609ac8d601c109c029` (unverändert) |
| `bewertung/zuordnungsschluessel.json` | `0215a8b2ed377df1e4e074dd5f489c58a7341fc93e54362b61fcef8b78a320f2` (unverändert) |
| `tools/tally_z2_overlap.py` (Werkzeug, ausserhalb des Blocks) | siehe `docs/repo-kontext/s13_bericht_ueberlapp.md` |

**Determinismus:** `tools/tally_z2_overlap.py` ist stdlib-only und zieht keine Uhrzeit,
keinen Zufall und keine Verzeichnisreihenfolge heran; zwei Läufe liefern bytegleiche
Ausgabe (SHA256 `fe7342f052f0146b922886527a0e4d4de531fc39e0b250557fc0ed5f40c6bf64`).

**Dieser Block ändert nichts** an `data/soll/**`, an `eingaben/`, `messungen/`, `k2_b1/`,
`k3_b1/`, an `ueberlappmatrix.md`, `bewertungsblatt.md`, `zuordnungsschluessel.json`, an
den bestehenden Werkzeugen, am eingefrorenen Protokoll oder an `befunde_log.md`.
**Kein Modell-Call, kein Messlauf, keine Deutung, keine Nachbewertung.**

---

## K3-Abschaltung zum 08.09.2026 (Auftrag S13b, 06.09.2026)

**Der Anbieter hat die Abschaltung des K3-Modells angekündigt.** Dieser Block legt den
Beleg ab, hält die Chronologie fest, berichtet die Vollständigkeitsprüfung der
K3-Artefakte und registriert die Folge. **Kein Modell-Call, keine Sonde, kein Lauf gegen
den Endpunkt** — auch nicht „zur Kontrolle, solange es noch geht"; ein Aufruf wäre ein Lauf
ausserhalb des Designs (§4). **Keine Deutung, kein Verdikt zu E1–E4.**

### Der Beleg

| Datei | Bytes | SHA256 |
|---|---|---|
| `docs/repo-kontext/do_deprecation_2026-09-01.pdf` — Originalbeleg, unverändert | **296 032** | `8deefae60ecf7340251d2d1a141403f830fbf4569cc7311324d8c5dcc232b596` |
| `docs/repo-kontext/do_deprecation_2026-09-01.md` — Textfassung mit Provenienzkopf | **5 771** | `38efd310e7bd9fab8f6ff1df0b6c04974ab600322d969d1c44ae6a593bf0c3b4` |

**Die vier belegenden Angaben, wörtlich:** Absender `DigitalOcean
<team@info.digitalocean.com>` · Datum `1. September 2026 um 21:45` · Modellstring
`nvidia-nemotron-3-super-120b` · Abschaltdatum `September 8, 2026`. Die Fehlerfolge,
wörtlich: „requests to this model will fail with a 404 error (model_not_found)".

**Status des Belegs:** **ANBIETERKOMMUNIKATION**, vom Auftraggeber als PDF-Export einer
Gmail-Ansicht geliefert (exportiert 06.09.2026). **KEIN Agentenbericht, KEINE Evidenz über
das Verhalten des Modells.** **Bytegleichheit gegen die Original-E-Mail ist NICHT
bezeugt.**

### Chronologie — aus den Laufrecords gelesen

**Die Ankündigung datiert VOR den Läufen der Zelle K3 × B1.** Sie ist **kein nachträglich
eingetretener Umstand**; die Läufe sind davon **unberührt** — sie sind vollständig,
bezeugt und gehasht.

| Zeitpunkt | Ereignis | Quelle |
|---|---|---|
| **2026-08-25 09:51:52Z – 11:54:48Z** | K3-Machbarkeitsläufe, 52 Slots | `data/c3b-k3/runs/*.json`, Feld `timestamp` |
| **2026-08-27 07:08:11Z – 2026-08-28 07:32:21Z** | Kampagnenblock K3, 61 Slots | `data/campaign/k3/*.json`, Feld `timestamp` |
| **2026-08-31 14:20:07Z – 14:45:03Z** | Z1-Zelle K3, 6 Slots | `data/z1/k3/*/extractor/meta.json`, Feld `timestamp` |
| **2026-09-01 21:45** | **ANKÜNDIGUNG DER ABSCHALTUNG** | Beleg, Kopfzeile der Nachricht |
| **2026-09-02 20:55:25+0200** | Erreichbarkeitssonde vor `run0`, HTTP 200 | Sondentabelle im K3-Block dieses Manifests oben; gleichlautend `docs/repo-kontext/s5k3_bericht_zelle_k3b1.md`, Abschnitt „Erreichbarkeitssonden“ |
| **2026-09-02 20:55:45 – 20:58:21+0200** | **`run0`** der Zelle K3 × B1 | `data/z2/k3_b1/run0/meta.json`, `run_manifest.json` |
| **2026-09-03 07:53:06+0200** | Erreichbarkeitssonde vor `run1`, HTTP 200 | wie oben |
| **2026-09-03 07:59:47 – 08:02:37+0200** | **`run1`** der Zelle K3 × B1 | `data/z2/k3_b1/run1/meta.json` |
| **2026-09-03 08:22:31+0200** | Erreichbarkeitssonde vor `run2`, HTTP 200 | wie oben |
| **2026-09-03 08:22:41 – 08:26:45+0200** | **`run2`** der Zelle K3 × B1 | `data/z2/k3_b1/run2/meta.json` |
| **2026-09-08** | **Abschaltung wirksam** — ab hier `404 (model_not_found)` | Beleg |

**Alle K3-Artefakte ausserhalb von Z2 sind VOR der Ankündigung erhoben**, alle drei Läufe
der Zelle K3 × B1 und alle drei Sonden **danach**. Die Erreichbarkeit ist **bis zuletzt
bezeugt**: die letzte Sonde am 03.09.2026 um 08:22:31+0200 lieferte **HTTP 200** mit
zeichengleichem Modell-Echo.

> **AUSSAGE DES AUTORS, kein Befund.** Die Ankündigung war zum Zeitpunkt der Läufe dem
> Autor **nicht präsent**; sie hat **keine Entscheidung des Designs beeinflusst**. Das ist
> eine Aussage des Autors und als solche gekennzeichnet — sie ist aus keinem Artefakt
> ableitbar und wird hier **nicht** als Messung geführt.

### Vollständigkeitsprüfung der K3-Artefakte — rein lesend

**Zelle K3 × B1, `data/z2/k3_b1/` — drei Slots, je fünf Dateien: 15 von 15 vorhanden und
nichtleer. KEINE LÜCKE.**

| Gegenstand | `run0` | `run1` | `run2` |
|---|---|---|---|
| `run_manifest.json` · `meta.json` · `prompt.txt` · `raw_response.json` · `validation.json` | **5/5**, nichtleer | **5/5**, nichtleer | **5/5**, nichtleer |
| Modell angefordert / Modell-Echo | `nvidia-nemotron-3-super-120b` / **zeichengleich** | dito | dito |
| Endpunkt | `https://inference.do-ai.run/v1/chat/completions` | dito | dito |
| HTTP-Status | **200** | **200** | **200** |
| `prompt_tokens` | **25 030** | **25 030** | **25 030** |
| `completion_tokens` | 1 874 | 1 607 | 3 863 |
| `finish_reason` | **`stop`** | **`stop`** | **`stop`** |
| `system_fingerprint` | **`null`** | **`null`** | **`null`** |
| Latenz | 154 424,988 ms | 164 457,858 ms | 236 897,347 ms |
| Zeitstempel Start/Ende | 02.09. 20:55:45 / 20:58:21 | 03.09. 07:59:47 / 08:02:37 | 03.09. 08:22:41 / 08:26:45 |
| Gesendeter Schemaname | `architecture_rules`, `strict: true` | dito | dito |
| `delivery_assurance` | `record_only` | `record_only` | `record_only` |
| Vollständige Antwort im Rohartefakt | **ja** — volle API-Hülle (`id`, `model`, `created`, `object`, `usage`, `choices[0]` mit `finish_reason`, `logprobs`, `message.content`, `message.reasoning_content`, `message.refusal`, `message.role`) | **ja** | **ja** |

**Gegenproben — alle getroffen, keine Abweichung:**

| Gegenprobe | Erwartet | Gemessen |
|---|---|---|
| `prompt_tokens` in allen drei | 25 030 | **25 030 / 25 030 / 25 030** — trifft |
| `finish_reason` in allen drei | `stop` | **`stop` / `stop` / `stop`** — trifft |
| Rohzahlen der `rules` | 4 / 3 / 5 | **4 / 3 / 5** — trifft |
| System-Anteil bytegleich mit **G1** | 2 283 B, SHA256 `60ae777b…` | **2 283 B, Hash zeichengleich** in allen drei — trifft |
| User-Anteil bytegleich mit **G2** | 107 307 B, SHA256 `21741e03…` | **107 307 B, Hash zeichengleich** in allen drei — trifft |

Die drei `prompt.txt` sind untereinander **bytegleich** (SHA256
`d19b2521d61eafa795b5a1a8ee57e5ff0d77141656a7aa9b687b6add94bf9ace`, je 109 612 B). Die
Datei trägt zwei Rollenmarkierungen `### system` und `### user`; nach Abzug der zwei
Trennzeilenumbrüche ist der System-Anteil **byte- und hashgleich** zu G1, der User-Anteil
**ohne jeden Abzug** byte- und hashgleich zu G2.

**K3-Artefakte ausserhalb von Z2 — nur Vorhandensein und Nichtleere geprüft, keine
inhaltliche Prüfung:**

| Block | Umfang | Rohantwort je Slot | Laufrecord je Slot | Ergebnis |
|---|---|---|---|---|
| `data/z1/k3/` | **6 Slots** (`run0`, `run0_w1`, `run0_w2`, `run0_w3`, `run1`, `run2`), je **3 Versuche** | **18 von 18** `attempts/attempt_{0,1,2}/raw_response.json`, alle nichtleer (4 264 – 22 829 B) | `run_manifest.json` **6/6** · `extractor/meta.json` **6/6** · je Versuch `prompt.txt` und `validation.json` **18/18** · `journal.jsonl` (13 Zeilen) | **vollständig** |
| `data/campaign/k3/` | **61 Slots**, je `.json` (Ergebnis) + `.jsonl` (Log), **183 `llm_call`-Records** | **133 von 183** `llm_call` mit nichtleerem `raw_response` | **61/61** `.json` **und** **61/61** `.jsonl`, keine leere Datei, kein Waisenpaar | **vollständig, mit Erläuterung unten** |
| `data/c3b-k3/` (K3-Machbarkeit) | **52 Slots**, je `.json` + `.jsonl`, **156 `llm_call`-Records** | **156 von 156** mit nichtleerem `raw_response` | **52/52** `.json` **und** **52/52** `.jsonl`, keine leere Datei | **vollständig** |

**Zu den 50 `llm_call`-Records ohne `raw_response` in `data/campaign/k3/`:** sie tragen
sämtlich `outcome: "transport_failed"` mit **drei** `transport_failures` je Record, durchweg
`http_429`, `attempts_used: 0`, `tokens_out_total: 0`. **Es hat nie eine Modellantwort
gegeben, die hätte archiviert werden können** — der Record dokumentiert den Ausfall
vollständig. **Das ist keine Lücke im Archiv**, sondern ein bezeugter Ausfall; es ist
folglich auch **nichts nachzutragen**. Die verbleibenden 133 Records verteilen sich auf 104
ohne, 15 mit zwei und 14 mit einer vorausgegangenen Transportwiederholung, je
`outcome: "measured"` und `valid_final: true`.

**KEINE LÜCKE GEFUNDEN.** Es gibt in keinem der vier Blöcke ein Artefakt, das ohne einen
Lauf gegen den Endpunkt nachzutragen wäre — es gibt **überhaupt kein** nachzutragendes
Artefakt. Alle 25 Hashblöcke unter `data/` sind im selben Lauf mit `sha256sum -c` geprüft
worden und **je OK**; die vier K3-tragenden darunter sind `data/z2/k3_b1` (15/15),
`data/z1/k3` (85/85), `data/campaign/k3` (183/183) und `data/c3b-k3` (105/105).

### DIE FOLGE — wörtlich registriert

> **Ab dem 08.09.2026 ist kein K3-Lauf mehr möglich; die Befunde der Zelle K3 × B1 ruhen
> ausschliesslich auf den archivierten Rohantworten und ihren Hashes. Eine Wiederholung,
> ein vierter Lauf, eine zusätzliche Bedingung oder ein Auslösen der Nachbesserungsregel
> (§4) sind für K3 ab diesem Datum ausgeschlossen. Das Design sah drei Läufe je Zelle vor;
> es wurde vollständig ausgeführt, es ist nichts nachzuholen.**

### Bezug zu T-Z1-5

**Bereits registriert war** (Z1-Protokoll §9, §3.3 (1) und (7); im K3-Block dieses
Manifests oben): beim DigitalOcean-Direktzugang ist `system_fingerprint` **`null`**, ein
**Seed wird gesendet, aber nicht als wirksam angenommen**, es existiert **kein Digest**, und
die **Identität der Gewichte ist nicht verifiziert**.

**Mit der Abschaltung kommt hinzu, dass das Messobjekt selbst nicht mehr existiert.**

> **ZUR EINORDNUNG: das ist eine Reproduzierbarkeitsgrenze, KEIN Befund über das Modell
> und KEIN Mangel der Erhebung.** Die Erhebung ist vollständig, bezeugt und gehasht; was
> entfällt, ist die Möglichkeit einer erneuten Erhebung durch Dritte.

### Keine Migration

**Die Nachricht empfiehlt den Nachfolger `nemotron-3-ultra-550b`. Er wird NICHT
eingerichtet, NICHT getestet, NICHT im Protokoll erwähnt und NICHT als Ersatz
vorgeschlagen.** **K3 ist eine registrierte Konfiguration**; ein anderes Modell wäre eine
**andere Bedingung**, kein Weiterführen derselben.

### Was dieser Block NICHT tut

**Dieser Block ändert nichts** an `data/z2/k3_b1/**`, `data/z1/**`, `data/z2/eingaben/**`,
`data/z2/messungen/**`, `data/z2/bewertung/**`, `data/soll/**`, `tools/**`, am
**eingefrorenen Z2-Protokoll**, an der Gate-Notiz, am Standdokument oder an
`befunde_log.md`. **Das Protokoll ist NICHT geändert:** die Abschaltung berührt **keine
registrierte Grösse, keine Schwelle und keine Entscheidung**. **Kein Modell-Call, keine
Sonde, kein Messlauf, keine Deutung, kein Verdikt zu E1–E4.**
