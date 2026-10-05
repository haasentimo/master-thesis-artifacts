# Z1-Protokoll — Extraktionsvergleich: deterministische Ableitung gegen LLM-Abstraktion (UF1)

Stand: 31. August 2026 (Rev. 1) · Status: Entwurf zur Vorregistrierung — Freeze steht aus

**Revisionshistorie**

Rev. 1: 31.08.2026 (Auftrag Z1-P) — Erstfassung. Vorregistrierung vor dem ersten
Z1-Lauf; §0–§10 vollständig, §10 leer.

---

## 0. Status und Evidenzstufe

> **Entwurf zur Vorregistrierung — eingefroren wird dieses Dokument (Commit-Hash) vor dem
> ersten Z1-Lauf. Änderungen danach nur über die Amendments-Tabelle (§10).**

Der SHA256 des eingefrorenen Dokuments wird **nicht hier**, sondern in
`docs/repo-kontext/z1_p_bericht_freeze.md` geführt: ein Selbstbezug im gehashten Dokument
ist unmöglich, weil sich der Hash beim Eintragen ändert. Präzedenz: Z3-Protokoll §0.1,
geführt in `c5b_bericht_protokoll_freeze.md` §3. Maschinell geprüft wird die
Übereinstimmung durch `tools/check_doc_invariants.py`, Invariante **(F)**.

**Regel für die Zeit nach dem Freeze.** Jede Änderung an diesem Protokoll ist eine
**datierte Revision** — auch ein reiner Hash-Nachzug, auch eine Änderung, die inhaltlich
nichts verschiebt. Geführt wird sie in **beiden** Stellen: Revisionshistorie im Kopf **und**
Amendments-Tabelle §10, nie nur an einer. Der Protokoll-SHA ist der Anker der
Bewegungsprüfung und taugt als Detektor nur, wenn kein Bytewechsel unregistriert bleibt
(Z3-Protokoll §0.1 Punkt 5, Rev. 36; Anlass `c6b0a_bericht_invarianten.md`).

### 0.1 Evidenzstufe: kontrolliertes Experiment

Z1 ist in `00_stand_und_entscheidungen.md` §5 als **kontrolliertes Experiment** registriert
(„kontrolliertes Experiment (Z1, Z3) > explorative klassifizierende Studie (Z2) >
Demonstration (Z4)"). Die Stufe wird von **einer** Tatsache getragen, und die ist prüfbar:

**Die Kennzahlformeln liegen seit `689a9cf` (26.06.2026, 10:24:39) blob-konstant vor** —
`src/llm_arch/eval/metrics.py` = `54a8021c51f1a05447b5ec64005853d5a8c9760b`,
`tests/test_reader.py` = `7fc33d1b795debca65488afb863c35dc2517622d`
(`z1_2_bericht_chronologie.md` §3.4: „Keine Formel hat sich seit dem 26.06.2026,
10:24:39 bewegt"), **in E-X am 31.08.2026 gegen den heutigen Extractor-HEAD `5c0b65a`
erneut gegengeprüft** und zeichengleich befunden (`ex_bericht_extractor_aenderungen.md`
§5.1). Die Formeln stehen damit **vor** der hier registrierten Messung fest. Dieses
Protokoll friert eine Festlegung ein, **die es gibt** — es erfindet sie nicht nachträglich.

### 0.2 Ungeschminkt: die 17 archivierten Läufe aus Juni sind NICHT Gegenstand

Die 17 in `data/befunde01-05/runs/` archivierten Läufe (25.–29.06.2026) tragen Z1 **nicht**
und werden hier **nicht** ausgewertet. Sie sind **formative Evaluation** im
Build-Evaluate-Zyklus (Befunde 01–05, `00_stand_und_entscheidungen.md` §5) und bleiben es.
Drei Gründe, alle in `z1_2_bericht_chronologie.md` belegt:

| # | Grund | Fundstelle |
|---|---|---|
| (a) | **Die Formeln entstanden erst nach Lauf 1.** Die Treuegrössen kommen mit `b6b910b` (nach Lauf 4), die Kompressionsgrössen mit `ac30da6` (nach Lauf 7), `induced_edges` bekommt seine Zeugen erst mit `689a9cf` (nach Lauf 7). Eine Vorregistrierung, die das behauptete, wäre eine nachträgliche | §2.1, §3.2.1–§3.2.3 |
| (b) | **`repo_commit` ist für 10 von 17 Läufen kein Codeanker.** Die Läufe 8–10 tragen `provider: openrouter`, obwohl das Profil auf ihrem `repo_commit` `689a9cf` auskommentiert ist; die Läufe 11–17 tragen `prompt_version: v3`, obwohl `PROMPT_VERSION` auf ihrem `repo_commit` `1704976` auf `"v2"` steht. Der ausgeführte Code war zur Laufzeit uncommittet | §4.2 |
| (c) | **7 von 17 Läufen tragen keine Kompressionsgrösse** (Läufe 1–7), 4 von 17 tragen weder `valid_raw` noch `valid_final`, sondern das alte Feld `valid` (Läufe 1–4) | §4.3 |

**Diese Feststellung ist selbst ein methodischer Befund für Kapitel 6** und wird dort als
solcher berichtet: der Unterschied zwischen einer Messreihe, die aus der Entwicklung
mitläuft, und einer, die gegen eine vorher eingefrorene Rechenvorschrift erhoben wird. Die
17 Läufe bleiben als **Herkunft der Erwartungen** in §8 zitierbar — als Vorwissen, nicht als
Messung.

---

## 1. Untersuchungsfrage

**UF1 (kanonische Fassung, `00_stand_und_entscheidungen.md` §2):**

> **UF1:** Unterschiede strukturell-deterministische Ableitung (Triton→Ilograph) vs.
> LLM-Abstraktion bei identischer Faktenbasis und identischem Interchange-Format —
> gemessen gold-frei (Faktentreue, Kompression, Validität, Determinismus). („Korrektheit"
> und „manuelle Nacharbeit" sind aus der alten Fassung gestrichen; Terminologie:
> **„Faktentreue"**.)

Dieselbe Zuordnung im Z3-Protokoll `eval_protokoll_phase04.md` §8: dort ist UF1
**ausdrücklich nicht Gegenstand** („Ausdrücklich NICHT UF1 — die Extraktionsfrage ist Z1 und
damit Befund 07", `befunde_log.md` Befund 08, Bezug zu Forschungsfragen). Z1 ist die einzige
Messung der Arbeit, die UF1 beantwortet; ihr Ergebnis wird als **Befund 07** geführt
(`00_stand_und_entscheidungen.md` §4, Nummernvergabe verbindlich).

### 1.1 Bezug zum Titel-Halbsatz

Der angemeldete Titel fragt zusätzlich, *„welche Ansätze zur Architekturableitung erweisen
sich dabei als besonders effektiv"*. `00_stand_und_entscheidungen.md` §1 bildet diesen
Halbsatz auf **Z1 (Ableitungsvergleich)** und **Z2 (Regelableitung)** ab.

**Nach der Gate-Notiz vom 31.08.2026 trägt Z1 den Halbsatz unmittelbarer als Z2.** Z2 steht
unter der gestuften Bedingung aus `gate_notiz_2026-08-31.md` §5 — Anhang A ist am Gate ein
Platzhalter geblieben, die Frist läuft bis 07.09.2026, der Umfang entscheidet sich am
13.09.2026 an der Schwelle N₁, und der dritte Ausgang verschiebt die Studie vollständig nach
Future Work. Z1 steht unter keiner solchen Bedingung. Der Kapitel-1-Abschnitt „Präzisierung
der Forschungsfrage" ist entsprechend zu schreiben: **Z1 ist die getragene Hälfte des
Halbsatzes, Z2 die bedingte.**

---

## 2. Gegenstand und Bedingungen

### 2.1 Ansatz 1 — deterministische Ableitung (Triton)

Vertreten durch die archivierte Fixture `fixtures/rich_repo.full.ilograph.yaml`
(Blob `ef8e0d0181eccddf5b2e88f3315c418cc1270208`, ein echter Triton-Vollexport). Provenienz
vollständig in `fixtures/PROVENANCE.md` (Blob `a3221fa9419f1405989bb199ab2891a5694fac9f`),
zusammengefasst in `d1_bericht_fixture_provenienz.md`: fünf unabhängige Merkmale des
Exporters sind in der Datei nachgewiesen (sich ausschliessende Schlüssel `node-type` /
`project-kind`, `package-scope`-Bedingung, `· `-Untertitelformel, dreifeldrige
„slim"-Reduktion, `perspectives`-Block), die `description`-Zeile und der Dateiname sind von
Hand gekürzt.

**Kein neuer Lauf.** Ansatz 1 wird **nicht** neu erzeugt. Gerechnet wird die Fixture
einmalig durch `read_ilograph` und dieselben Kennzahlfunktionen wie Ansatz 2 (§4); das
Ergebnis wird als Artefakt archiviert und muss die in `tests/test_reader.py:53-73`
zugesicherten Werte **zeichengleich** treffen (§8, E1/E2).

### 2.2 Ansatz 2 — LLM-Abstraktion, frische Läufe

Zwei Modellbedingungen, **drei Läufe je Bedingung**:

| Bedingung | Modell | Profil | Zugangsweg |
|---|---|---|---|
| **K2** | `qwen2.5-coder:7b` | `ollama` | lokal, `http://localhost:11434/v1` |
| **K3** | `nvidia-nemotron-3-super-120b` | `digitalocean` | `https://inference.do-ai.run/v1` |

**K3 nimmt denselben Zugangsweg wie K3 in Z3.** `eval_protokoll_phase04.md` §1 (Zeile K3)
und §6 (Aufrufblöcke, Fassung Rev. 32) führen für die Phase-04-Kampagne: Base-URL
`https://inference.do-ai.run/v1`, Modell `nvidia-nemotron-3-super-120b`, **kein**
`CONFORMANCE_PROVIDER_PIN` (ohne Router gibt es nichts zu pinnen, B32). Z1 gebraucht
denselben Endpunkt und dieselbe Modell-ID; damit ist der Modellwechsel zwischen den beiden
kontrollierten Experimenten der Arbeit **kein** zusätzlicher Confounder.

**Begründung und Vorprüfung des Endpunkts:** `z1_p_bericht_endpunktfrage.md`. Ein einziger
Testcall am 31.08.2026 mit dem **unveränderten** `response_format` des Extractors endete mit
**HTTP 200**, das `model`-Echo war zeichengleich mit der angeforderten ID (kein
Router-Suffix, anders als bei OpenRouter), die Antwort war parsebar. Das Schema ist damit
**angenommen** (§3.3 dieses Protokolls sagt, was daraus **nicht** folgt).

Der Profileintrag `digitalocean` liegt seit **E-X** (`57b77a0`) im Extractor; `base_url`
reist seit `1681169` im Laufrecord. Beide Commits sind in
`ex_bericht_extractor_aenderungen.md` §1 und §2 mit vollständigem Diff belegt; §5.3 dort
weist nach, dass **keine Fixture und keine Formel** dabei berührt wurde.

**Prompt:** die im Extractor eingefrorene Version.

| Gegenstand | Wert |
|---|---|
| Datei | `src/llm_arch/abstraction/prompt.py` |
| Blob (git) | `6c8e4639441df6081c6d5bf9bc29b40c04033f61` |
| SHA256 der Blob-Bytes | `ed9e1ebd51c6328968ecd7645bd073c4512f99b2512ad75f35f486272f946d46` |
| `PROMPT_VERSION` | **`v3`** (`prompt.py:17`) |

`v3` = v2 + verpflichtende, import-abgeleitete Komponentenrelationen, Perspektive weiterhin
frei (Befund 04). Der Prompt wird **nicht** angefasst; Prompt-Tuning ist mit Befund 04
Konsequenz 1 („genau **eine** Iteration — keine weitere Tuning-Runde") abgeschlossen.

### 2.3 Die Asymmetrie, offengelegt

**Ansatz 1 ist deterministisch und liegt als Artefakt vor; Ansatz 2 wird neu gemessen.**
Das ist **kein Head-to-Head zweier Laufserien**, sondern der Vergleich **eines
deterministischen Artefakts** mit **einer gemessenen Verteilung**. Diese Asymmetrie ist
konstitutiv und wird nirgends weggeschrieben:

- Ansatz 1 hat **keine** Verteilung — kein Median, keine Spannweite, keine Varianz. Er
  liefert **einen** Wert je Kennzahl, und derselbe Eingang liefert ihn beliebig oft wieder.
- Ansatz 2 hat eine Verteilung über drei Läufe je Bedingung, und die Streuung ist selbst
  ein Messgegenstand (§8, E6).
- Ein Aggregat über beide Ansätze existiert nicht und wird nicht gebildet.

**Sprachregelung, verbindlich für Kapitel 5 und 6:** Z1 heisst **Extraktionsvergleich**,
nie „Head-to-Head-Lauf". Die Formulierung „Head-to-Head" aus `00_stand_und_entscheidungen.md`
§4 und `befunde_log.md` (Kommentarblock zu Befund 07) bezeichnet den **Vergleich**, nicht
zwei gefahrene Serien; wo sie stehen bleibt, ist sie in diesem Sinn zu lesen.

---

## 3. Gehashte Messeingänge und Umgebungsparameter

**Extractor-Commit: `5c0b65a82cc3d8af47c022d779ff63d8a20a9e08` (`5c0b65a`).**

**Der BLOB-Hash ist die Referenz, nicht die Arbeitsbaumdatei.** Gehasht wird, was im Objekt
der Datei steht, nicht was gerade im Arbeitsbaum liegt — sonst hinge der Messstand an
Zeilenenden und Editorzuständen (die CRLF-Lage des alten Klons, `z1_1` §0.3, ist genau
dieser Fall). Alle Werte unten sind am 31.08.2026 mit `git ls-files -s` und
`git cat-file blob` **aus dem Repositorium gelesen**; für jede Datei wurde zusätzlich
`git hash-object <datei>` gegen den Blob gestellt — **12 von 12 gleich**, der Arbeitsbaum
ist byteidentisch mit dem Index.

### 3.1 Messeingänge

| Gegenstand | Blob (git, SHA1) | SHA256 der Blob-Bytes |
|---|---|---|
| `fixtures/rich_repo.full.ilograph.yaml` | `ef8e0d0181eccddf5b2e88f3315c418cc1270208` | `34d6f2f4c7731c5a1a8640e6d1583218d0b73d2875a623f311208f20345d915f` |
| `fixtures/rich_repo.gold.json` | `f34f74849ab6e74cf16e0212cf090045041387be` | `481c3aad5c5d6c4a19d446c0519ea9209820a4cb57d954e41a044a5b71a278a3` |
| `src/llm_arch/eval/metrics.py` | `54a8021c51f1a05447b5ec64005853d5a8c9760b` | `668d6d47e68923b78cb339b38ea7b39b64a5f4ce7bd3c9c99a8004825934cdb6` |
| `tests/test_reader.py` | `7fc33d1b795debca65488afb863c35dc2517622d` | `3c58a2d0480f7baca70946bbafe1836e3e78b3a47da274ab32011146833bd1b7` |
| `src/llm_arch/abstraction/prompt.py` | `6c8e4639441df6081c6d5bf9bc29b40c04033f61` | `ed9e1ebd51c6328968ecd7645bd073c4512f99b2512ad75f35f486272f946d46` |
| `fixtures/PROVENANCE.md` | `a3221fa9419f1405989bb199ab2891a5694fac9f` | `c5dda4dcedcacd35330ada9833a97dfc304c3ddced281daa065003ca011ca3b6` |

**Die `rich_repo/`-Fixture, alle 18 Blobs** (16 Dateien des Beispielrepos + Export + Gold):

| Blob (git, SHA1) | SHA256 der Blob-Bytes | Pfad |
|---|---|---|
| `ef8e0d0181eccddf5b2e88f3315c418cc1270208` | `34d6f2f4c7731c5a1a8640e6d1583218d0b73d2875a623f311208f20345d915f` | `fixtures/rich_repo.full.ilograph.yaml` |
| `f34f74849ab6e74cf16e0212cf090045041387be` | `481c3aad5c5d6c4a19d446c0519ea9209820a4cb57d954e41a044a5b71a278a3` | `fixtures/rich_repo.gold.json` |
| `d7a77ac4854dbe1c9134adae23ebbd6d1f9fb3e5` | `3375f2d18b7a39c306831decb09b23b4d5d734bda42d7f16b10ca1ca310f654f` | `fixtures/rich_repo/bookshop/__init__.py` |
| `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `fixtures/rich_repo/bookshop/api/__init__.py` |
| `6772d542150e1e71f298182f9d5d97b74746c1ef` | `56787ef8075a0cdf338d7f7964a6febf4396bb12dbd370ac0ed3a950dae1df55` | `fixtures/rich_repo/bookshop/api/catalog_routes.py` |
| `6aff2cbd01edaf989d8292e09d39ebeacdf7d5cb` | `b8cb66670cd614010bf9466fcd3d962e944e2edd402562df7c86db0ef4386a2e` | `fixtures/rich_repo/bookshop/api/checkout_routes.py` |
| `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `fixtures/rich_repo/bookshop/application/__init__.py` |
| `5bad7691614fef54793e17a3247f098c0c1d980d` | `d70971541fe42658927c5163370800f05d298efe3f259417d257a82f0f611119` | `fixtures/rich_repo/bookshop/application/checkout.py` |
| `fe27bcbfb642c71dcad1488b0bdb4eaa594b2ff9` | `046398eff2645522379f2b8b96f6ff6f313e93f001921faac93d0ce6f011614a` | `fixtures/rich_repo/bookshop/application/inventory.py` |
| `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `fixtures/rich_repo/bookshop/domain/__init__.py` |
| `06405dc040f30f87203c6a4387d364830e0fa2c7` | `eda3a2da15155a3f8698ba017dbe78f0db019bc9b9856b34beeacb92c0771100` | `fixtures/rich_repo/bookshop/domain/book.py` |
| `a23a28aefa60483b7c4173b75f416a98694eddd8` | `628ecefda4324d75d2ec092c88912e598003cc110e9bc64789a59ed1c0b1074c` | `fixtures/rich_repo/bookshop/domain/catalog.py` |
| `f3ee4afec980f026d12165a2c296da4711fd3918` | `76f2a392c67b8bf05a3280f724b219e1edf83aee37b6402a6e81037f504ad323` | `fixtures/rich_repo/bookshop/domain/order.py` |
| `ee9e35df44db588cd46a38237637a5c943f245d5` | `6fa1fd05e27119acf50398fdc8aed54ff5df0ffa524294bd4d1d8875975f0e8a` | `fixtures/rich_repo/bookshop/domain/pricing.py` |
| `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `fixtures/rich_repo/bookshop/infrastructure/__init__.py` |
| `ee479d6a0b8bd693b267cfbf13f5ce61ec362ca4` | `57e851ff56ed5357cb823cbb070f61096e7ba99ff4120c3edf15a353bff9c9ae` | `fixtures/rich_repo/bookshop/infrastructure/book_repository.py` |
| `859c30e3993bb9cb6c34dac97b88d44bde65cb3d` | `8fe4ebdd394f5de1fd7ffff253ecf5637f8a72afb8b0c964c87f9491d826548c` | `fixtures/rich_repo/bookshop/infrastructure/order_repository.py` |
| `1e8e1fbaff286959689cda0eb4ad18c0adf78cdd` | `e8049b0af15df9144d1753351941427c1212a83756213a3f7d7aa0086381d893` | `fixtures/rich_repo/bookshop/infrastructure/payment_gateway.py` |

Die vier leeren Paket-`__init__.py` teilen erwartungsgemäss den Leerblob
`e69de29b…` / `e3b0c442…`. Elf der sechzehn Dateien sind Leaf-Module; die Zählkonvention
(16 AST-Einträge, davon 5 leere Paket-`__init__`, verbleiben **11 substanzielle Module**)
ist in Befund 02, Anmerkung 03.08.2026, verifiziert und gilt hier unverändert.

### 3.2 Weitere gehashte Instrumente

| Gegenstand | Blob (git, SHA1) | SHA256 der Blob-Bytes |
|---|---|---|
| `src/llm_arch/abstraction/schema.py` | `5846232d9328685294f8d49f84a1546b2c843ec5` | `03379c14f304ba37b1cccd797f42b61ec3a28350ee95fcec617c93271a8e4636` |
| `src/llm_arch/abstraction/abstractor.py` | `84ae1a024aac1973be99993dff149edfe3402ac0` | `ef7a8c15410a884f5dbd945257fe43af493d756145a9c01fd86d7864881ac09d` |
| `src/llm_arch/providers/openai_compatible.py` | `9cbfc91e7bfda91ebc41d11ecd50a63f32a8a1d8` | `6a48a882be339d713add7f8a2460c1ac80d008af9c133771954f8578017ce07f` |
| `src/llm_arch/logging/run_logger.py` | `cc6d3cc4d71446b1ace9cc64a0ad94eea1410257` | `6e6d2b3d1da65639faba31c46a086ce40f214dffe16fd55cd8cad29ba35dbe5d` |
| `src/llm_arch/cli.py` | `f1fe37dd56ca8ef4b430edfc8dcabf176356ca5a` | `407b04e56ba5a49180982e25caedb8aac65696ed6077a7c47b9d2977db0a8c9d` |
| `scripts/compare_runs.py` | `c6db316b3904338d034ac65297aa8557f1fee028` | `5728c1438187bd7b3208402f229ae05876aaac444a45fc57735eec018c9efa16` |

**Das gesendete JSON-Schema.** `abstractor.py:66` ruft `ArchModel.model_json_schema()`. Die
erzeugte, archivierte Fassung liegt als `docs/repo-kontext/z1_p_arch_model_schema.json` im
Thesis-Repo, SHA256 **`a83a84af306d647f2d4d9618a39f9b0059431015d3e5234bce931df642012ec0`**
(123 Zeilen, LF, `json.dumps(schema, indent=2, ensure_ascii=False) + "\n"`). Die **Drahtform**
(`separators=(",",":")`) hat einen anderen Hash,
`1a4cf09cbe22e08dba4ff2d4a4c09234e37131e8d4fab78be654ff7248f70b23`; registriert ist die
**archivierte** Form, weil sie an eine versionierte Datei gebunden und damit prüfbar ist
(`z1_p_bericht_endpunktfrage.md` §2.1).

### 3.3 Umgebungsparameter — nicht je Lauf bezeugt, deshalb hier registriert

Die folgenden Werte gehen in jeden Lauf ein, stehen aber **nicht** oder **nicht in dieser
Form** im Laufrecord. Sie sind Umgebungsparameter des Experiments und werden hier
festgehalten; die `meta.json` der Z1-Läufe belegt sie **nicht** und darf nicht so gelesen
werden (`z1_p_bericht_endpunktfrage.md`, Folgeposten 3).

**(1) `temperature=0.0` und `seed=0` sind hart verdrahtet und von der CLI nicht erreichbar.**
`openai_compatible.py:34-35` setzt sie als Konstruktor-Vorgaben (`temperature: float = 0.0`,
`seed: int = 0`), `openai_compatible.py:49-50` sendet sie in jedem Call. `cli.py` hat für
beide **keine** Option. `temperature` reist nach `meta.json` (`run_logger.py:100`),
**`seed` nicht** — der geschriebene Record hat **29 Felder**, `seed` ist keines davon,
nachgemessen in E-X an einem gestubbten Lauf
(`ex_bericht_extractor_aenderungen.md` §2.4, §4.4). Beide werden deshalb **als
Umgebungsparameter registriert, nicht als Laufbeleg**.

**Bezug zu DDR N** (`docs/ddr/checker_entscheidungen_n.md`, Punkte 5 und 6): Bei OpenRouter
wurde der Seed **nicht honoriert** — dreifach belegt (DigitalOcean führt `seed` nicht in
`supported_parameters`, DeepInfra führt ihn ohne `structured_outputs`, Nebius weist ihn mit
HTTP 422 zurück). Die Reproduzierbarkeit ruht dort auf `temperature: 0`; der Seed war „das
Feinwerkzeug obendrauf, nicht das Hauptinstrument". **Für den DigitalOcean-Direktzugang ist
die Honorierung ungemessen**: der Testcall nahm `seed=0` an (kein HTTP 400), lieferte aber
`system_fingerprint: null` — keinen Backend-Anker —, und ob der Seed **beachtet** wird, ist
mit einem Call nicht feststellbar (`z1_p_bericht_endpunktfrage.md` §3.2, Folgeposten 2).
**Festgelegt:** `seed=0` wird **gesendet, aber nicht als wirksam angenommen**; die Varianz
über die drei Läufe ist Teil des Messgegenstands (§8, E6), keine Störung. Eine
Reproduzierbarkeitsbehauptung unter Berufung auf den Quelltextkommentar wird **nicht**
aufgestellt.

**(2) `base_url` steht im Record in der Client-Form MIT Schrägstrich.**
`cli.py:58` schreibt `str(prov.client.base_url)`; der `openai`-Client normalisiert die URL
und hängt einen Schrägstrich an. Im Record steht daher
`https://inference.do-ai.run/v1/`, im `PROFILES`-Eintrag
(`openai_compatible.py`) dagegen `https://inference.do-ai.run/v1` — **ohne**. Nachgemessen
in `ex_bericht_extractor_aenderungen.md` §2.3 (b) und §4.4. Es ist **dieselbe URL**, benannte
Normalisierung des SDK, bewusst ungeschönt geloggt. **Ein Zeichenvergleich über Läufe oder
gegen das Profil muss das berücksichtigen** und ist entweder auf der Client-Form oder auf
einer normalisierten Form zu führen, nie gemischt.

**(3) `strict: true` ist gegenüber diesem Endpunkt KEINE Formgarantie.**
`openai_compatible.py:53-60` sendet `response_format: {type: json_schema, json_schema:
{name: arch_model, schema: …, strict: true}}`. Das gesendete pydantic-Schema trägt
**kein** `additionalProperties: false` an keiner Stelle und hat ein **minimales** `required`
(`ArchModel` nur `components`; `Component` nur `id` und `name`) — Bedingungen, unter denen
OpenAIs strenger Prüfer `strict: true` mit HTTP 400 zurückwiese
(`z1_p_bericht_endpunktfrage.md` §2.3). Der Testcall lief mit **HTTP 200** durch: **der
Endpunkt fährt diesen Prüfer nicht.** Die zurückgegebene Antwort war formal schemagültig und
trotzdem formfremd (`type`/`depends_on` statt `kind`/`role`/`contained_modules`,
`dependencies`/`layers` statt `relations`) — erlaubt, weil das Schema zusätzliche Schlüssel
zulässt (§3.3 dort). **Die Form trägt in Produktion der Prompt**, nicht das
`response_format`: v3 benennt `contained_modules` und `relations` wörtlich und verlangt
Relationen ausdrücklich. Z1 beschreibt seine Ausgabe deshalb **nicht** als „strukturierte
Ausgabe erzwungen".

**(4) Laufzeitversionen.** `pyproject.toml` deklariert `openai>=1.0` und `pydantic>=2.0`;
eine **Lockdatei existiert nicht** (`requirements*.txt`, `uv.lock`, `poetry.lock` — keine
vorhanden, `z1_p_bericht_endpunktfrage.md` §1.2). Die Drahtform des Requests **und die
Schema-Bytes** hängen damit an der installierten Version. Registriert sind die Versionen, in
denen Schema-Hash und Testcall gemessen wurden:

| | Version | gemessen in |
|---|---|---|
| Python | **3.12.3** | Z1-P0 §2.1, E-X §4 |
| pydantic | **2.13.5** | Z1-P0 §2.1, E-X §4 |
| openai (SDK) | **3.6.0** | Z1-P0 §3.2, E-X §4 |

**Auflage:** Vor dem ersten Z1-Lauf werden die drei Versionen in der tatsächlichen
Laufumgebung erhoben und ins Laufjournal geschrieben, und der Schema-Hash aus §3.2 wird
gegen `ArchModel.model_json_schema()` **in dieser Umgebung** nachgerechnet. Weicht eine
Version ab, wird die Abweichung **berichtet**; weicht der Schema-Hash ab, ist der Lauf
**nicht zu starten**, bis die Abweichung als Amendment (§10) registriert ist.

**(5) Schema-Smoke gegen den Zielendpunkt als Vorbedingung.** Es existiert im Extractor
**kein** Test, der das echte `ArchModel`-Schema gegen den Zielendpunkt schickt;
`tests/test_provider_smoke.py` läuft gegen lokales Ollama mit einem Mini-Schema, das genau
die Eigenschaften hat, die das echte Schema nicht hat (`z1_p_bericht_endpunktfrage.md`,
Folgeposten 1). **Festgelegt:** Vor dem K3-Messlauf wird ein Call mit dem gehashten Schema
gegen `inference.do-ai.run` abgesetzt und mit HTTP-Status, `model`-Echo, Schema-Hash und
pydantic-Version protokolliert. **Bricht er, ist der Messlauf nicht zu starten.**

---

## 4. Kennzahlen — wörtlich aus dem Code

Registriert wird **ausschliesslich**, was `src/llm_arch/eval/metrics.py`
(Blob `54a8021c…`) heute rechnet, in der Fassung, die dort steht. **Keine Umformulierung,
keine neue Kennzahl. Was der Code nicht rechnet, wird nicht registriert.**

Beide Ansätze werden auf **dieselbe kanonische Reduktion** projiziert und mit **denselben
Funktionen** bewertet — Ansatz 2 über `reduce_arch`, Ansatz 1 über den Ilograph-Reader
(`metrics.py:1-8`, Moduldocstring): *„Both approaches are projected to the same canonical
reduced form … so the identical metric functions score Approach 2 (via reduce_arch) and
Triton (via the Ilograph reader)."*

### 4.1 Faktentreue — `metrics.py:92-125`, gold-frei

```python
@dataclass
class FactFidelity:
    """How well the model's claims match the facts (all gold-free)."""

    relation_precision: float  # claimed edges backed by >=1 real import
    relation_recall: float  # real cross-component deps the model captured
    module_coverage: float  # placed substantive modules / |M|
    phantom_modules: int  # placed modules not present in the facts


def fact_fidelity(
    facts: list[ModuleFacts],
    reduced: ReducedModel,
    required_modules: set[str],
) -> FactFidelity:
    """Compute fact-fidelity metrics for one reduced model against the facts."""
    induced = induced_edges(facts, reduced.module_to_component)
    claimed = reduced.component_relations
    hit = claimed & induced

    # ponytail: with no claimed relations precision is vacuous (no false claims).
    precision = len(hit) / len(claimed) if claimed else 1.0
    recall = len(hit) / len(induced) if induced else 1.0

    placed = set(reduced.module_to_component)
    coverage = (
        len(placed & required_modules) / len(required_modules)
        if required_modules
        else 1.0
    )
    known = {f.module_name for f in facts}
    phantom = sum(1 for m in placed if m not in known)

    return FactFidelity(precision, recall, coverage, phantom)
```

| Kennzahl | Feld in `meta.json` | Bezug |
|---|---|---|
| `relation_precision` | `relation_precision` | **gold-frei** |
| `relation_recall` | `relation_recall` | **gold-frei** |
| `module_coverage` | `module_coverage` | **gold-frei** |
| `phantom_modules` | `phantom_modules` | **gold-frei** |

**Zwei Randfälle sind Teil der Definition und werden so berichtet:** ohne behauptete
Relationen ist `precision` **1.0** (vakuum, keine falsche Behauptung), ohne induzierte Kanten
ist `recall` **1.0**. Eine Precision von 1.0 bei null Relationen ist deshalb **kein**
Treuebeleg; die Zahl ist stets neben `component_relation_count` zu lesen. Beleg, dass der
Fall real auftritt: die Läufe 8–10 der Juni-Serie tragen `P 1.0 · R 0.0` bei **null**
Komponentenrelationen (`z1_2` §4.3).

**Zulieferung, `metrics.py:60-89`:** `induced_edge_witnesses` bildet jede
komponentenübergreifende Kante auf ihre Modul-Importzeugen ab, `induced_edges` ist deren
Schlüsselmenge. `_resolve_targets` (`metrics.py:38-57`) löst absolute Importe vollständig
und relative auf Best-Effort-Basis auf; die Fixture nutzt absolute Importe.

### 4.2 Kompression — `metrics.py:128-176`, gold-frei, **deskriptiv**

```python
@dataclass
class Compression:
    """Descriptive only -- how much was folded, NOT how well (guardrail 3)."""

    module_count: int  # substantive modules placed
    component_count: int
    module_compression: float | None  # modules per component
    import_edge_count: int  # raw module-level import edges
    component_relation_count: int
    relation_compression: float | None  # import edges per component relation
```

```python
def compression(
    facts: list[ModuleFacts], reduced: ReducedModel, modules: set[str]
) -> Compression:
    """Compute descriptive compression ratios for one reduced model."""
    placed = {m: c for m, c in reduced.module_to_component.items() if m in modules}
    module_count = len(placed)
    component_count = len(set(placed.values()))
    import_edge_count = count_import_edges(facts, modules)
    relation_count = len(reduced.component_relations)

    return Compression(
        module_count=module_count,
        component_count=component_count,
        module_compression=(
            module_count / component_count if component_count else None
        ),
        import_edge_count=import_edge_count,
        component_relation_count=relation_count,
        # decision 5: None (not inf/NaN) when there are no component relations.
        relation_compression=(
            import_edge_count / relation_count if relation_count else None
        ),
    )
```

| Kennzahl | Feld in `meta.json` | Bezug |
|---|---|---|
| `module_count` | `module_count` | **gold-frei** |
| `component_count` | `component_count` | **gold-frei** |
| `module_compression` | `module_compression` | **gold-frei**, `null` möglich |
| `import_edge_count` | `import_edge_count` | **gold-frei** |
| `component_relation_count` | `component_relation_count` | **gold-frei** |
| `relation_compression` | `relation_compression` | **gold-frei**, `null` möglich |

**`null` ist ein Wert, keine Lücke** (Kommentar „decision 5" im Code): ohne
Komponentenrelation gibt es keine Relationskompression, und der Code schreibt bewusst `None`
statt `inf` oder `NaN`. In der Auswertung wird `null` als **nicht gebildet** ausgewiesen und
geht in **keine** Aggregation ein — weder in einen Median noch in eine Spannweite.

**Der Docstring ist Teil der Registrierung:** *„Descriptive only — how much was folded, NOT
how well (guardrail 3)."* Kompression ist **kein Gütemass**. Ein hoher Wert ist weder gut
noch schlecht; er sagt, wie stark gefaltet wurde. Ohne die Treuegrössen daneben ist er nicht
interpretierbar (Befund 02, Konsequenz 3: „Erst Treue **und** Kompression zusammen ergeben
die UF1-Aussage").

### 4.3 Bezugsgrösse — `substantive_modules`, `facts/extractor.py:113-123`

```python
def substantive_modules(facts: list[ModuleFacts]) -> set[str]:
    """Module names carrying architecture signal (classes, functions or imports).

    Empty/namespace `__init__` packages are excluded: they must not be required
    in a component (completeness) nor counted in coverage.
    """
    return {
        m.module_name
        for m in facts
        if m.classes or m.functions or m.imports
    }
```

Für `rich_repo` sind das **11** von 16 AST-Einträgen. Alle Kompressions- und
Coverage-Zahlen stehen auf dieser Basis. **Verbindlich für Kapitel 5** (Befund 01,
Anmerkung 03.08.2026): Kompressionszahlen werden durchgehend auf der Leaf-Modul-Basis
berichtet, die Bezugsbasis wird einmal explizit genannt, und die Formulierung „16 → 4" darf
**nicht** neben metrisch berechneten Kompressionswerten stehen.

### 4.4 Gold-Ähnlichkeit — `metrics.py:179-216`, **gold-bezogen**

`gold_similarity(module_to_component, gold)` ist der **Adjusted Rand Index** zwischen der
Modul→Komponente-Abbildung und der Referenzpartition `fixtures/rich_repo.gold.json`; das
Feld `gold_similarity_method` trägt konstant `"adjusted_rand_index"`. Der Docstring sagt,
was der Wert ist: *„This is a SIMILARITY signal to a chosen reference partition, NOT
correctness."*

**Die Gold-Degradierung aus Befund 01 gilt weiter und wird hier erneut registriert.** Befund
01.3 hat gezeigt, dass das Modell eine **andere, aber legitime** Architektursicht wählte
(vertikale Feature-Services statt horizontaler Schichten); Konsequenz 2 dort: „**Gold
degradiert** vom ‚korrekten Ergebnis' zur **einen Referenz-Zerlegung**; Übereinstimmung wird
als *Ähnlichkeitssignal* berichtet, nicht als Korrektheit." Dazu kommt die
**Autorenidentität**: `rich_repo.gold.json` und die Fixture stammen von derselben Person, und
`gold.json` entstand im **selben Commit** `f74d8a5` wie die ARI-Rechnung, die sie auswertet
(`z1_2` §5.1). **`gold_similarity` ist damit kein Korrektheitsmass** und wird in keiner
Tabelle als solches geführt.

**Verbindlicher Begriff:** Wo gold-frei gemessen wird, heisst die Grösse **Faktentreue**
(`00_stand_und_entscheidungen.md` §2 und §9). Nicht „Korrektheit", nicht „Genauigkeit". Die
genauere Fassung aus Befund 02, Konsequenz 1 gilt: gemessen wird **strukturelle /
Import-Faktentreue**, und eine Abweichung von 1.0 ist **mehrdeutig** (bewusste Abstraktion
gegen echten Verlust; semantische Inferenz gegen Halluzination).

### 4.5 Was NICHT registriert wird

Nicht Gegenstand von Z1, weil der Code sie nicht rechnet oder weil sie eine Deutung wären:
eine Gesamtnote, ein gewichteter Index aus Treue und Kompression, eine Rate über beide
Ansätze, eine Signifikanzaussage, eine Aussage über andere Fixtures oder andere Modelle.
Die qualitative Kantenklassifikation aus Befund 02 (Konsequenz 2) und Befund 03.3 —
`abstracted` gegen `lost`, `hallucination` gegen semantische Inferenz — ist **kein Teil
dieses Protokolls**; sie ist Interpretationsarbeit für Kapitel 5 und wird dort als solche
gekennzeichnet, nie als Messung.

---

## 5. Gültigkeit und Auswahl — die Auflage aus Befund 08 (d)

Befund 08, methodische Konsequenz **(d)**: *„Ein Werkzeug, das aus mehreren Artefakten eines
auswählt, braucht eine Zusicherung gegen die Auswahl ungültiger Läufe. Was in Z3 vier
Auswertungsläufe gekostet hat, wird in Z1 **vorher** gebaut."*

**Ausgangslage, nachgemessen:** `scripts/compare_runs.py` **wählt nicht aus**. Es legt alle
übergebenen Läufe nebeneinander (`compare_runs.py:53-56`, eine Zeile je Lauf) und bildet
über die Gruppe nur zwei Aggregate: Byte-Identität der `arch_model.json` und
`validity_rate(valid_final)` (`:57-64`). Die Korrektur der Fehlannahme aus `z1_0` L-6 steht
in `z1_1` §4.4. **Die Auswahl geschieht heute von Hand und hinterlässt keine Spur.** Genau
deshalb steht sie vorab hier.

### 5.1 Alle Läufe werden berichtet, keiner ausgewählt

Je Bedingung werden **alle drei** Läufe berichtet, mit ihren Einzelwerten. Es wird **kein**
Lauf als „der beste", „der repräsentative" oder „der zitierte" ausgewählt.

- **Aggregat ist der Median** über die drei Läufe, **dazu die Spannweite** (Minimum und
  Maximum).
- **Kein Mittelwert.** Bei n = 3 mit möglicher Ausreisserlage ist der Median die robustere
  und die bereits im Projekt verwendete Form (Z3-Protokoll §5, Berichtsform
  Grössenordnungen).
- **Keine Nachkommastellen-Interpretation.** Unterschiede in der dritten Nachkommastelle
  werden nicht gedeutet.
- **`null`-Werte gehen in kein Aggregat ein** (§4.2) und werden als *nicht gebildet*
  ausgewiesen, nicht als 0.

Präzedenz für die Berichtsform: Befund 04 zitiert die nemotron-v3-Serie als „drei Läufe",
nachdem sich nicht mehr rekonstruieren liess, welche drei von vier Verzeichnissen ausgewertet
worden waren (Anmerkung 03.08.2026 zu Befund 04). Genau das soll hier nicht wieder
entstehen können.

### 5.2 Gültigkeit: `valid_final == true`, ein fehlendes Feld ist ein ABBRUCH

Ein Lauf ist **gültig**, wenn `meta.json` das Feld `valid_final` führt **und** es `true`
ist.

**Ein FEHLENDES Feld ist ein ABBRUCH, nicht ein `false`.** `bool(None)` ist in Python
`False`; eine Auswertung, die `m.get("valid_final")` durch `bool()` schickt — so tut es
`compare_runs.py:59` — führte einen Lauf ohne dieses Feld **stillschweigend als ungültig**.
Das ist kein hypothetischer Fall: **die vier ältesten Archivläufe tragen `valid_final`
nicht**, sondern das ältere Feld `valid` (`z1_2` §4.3, Läufe 1–4). Für Z1-Läufe ist das
Feld vorhanden — aber die Regel steht hier, weil ein stiller Ausfall **an derselben Stelle**
entstünde, wenn sie fehlte.

**Festgelegt:** fehlt `valid_final` in einer `meta.json`, bricht die Auswertung mit einer
benannten Meldung ab. Der Lauf wird **nicht** als ungültig gezählt und **nicht** als 0
verrechnet.

Berichtet werden daneben, je Lauf, `valid_raw` und `attempts_used` — die Roh-gegen-Final-
Validität ist eine eigene UF4-Kennzahl (Befund 02.1) und wird nicht in die Gültigkeitsfrage
eingeschmolzen.

### 5.3 Parse-Zusicherung — der Kern dieser Registrierung

**Je Lauf wird die Rohantwort gegen das geparste Modell gestellt.** Zwei Vergleiche, beide
über die archivierten Artefakte, beide ohne Eingriff in den Extractor:

| | Vergleich | Quelle links | Quelle rechts |
|---|---|---|---|
| **(P1)** | **Schlüsselmenge** der Rohantwort gegen die **Feldmenge von `ArchModel`** — auf oberster Ebene (`components`, `relations`) und je Komponente (`id`, `name`, `kind`, `description`, `role`, `contained_modules`) und je Relation (`from`, `to`, `kind`) | `attempts/attempt_<n>/raw_response.json`, Feld `choices[0].message.content`, als JSON geparst | `ArchModel`, `Component`, `Relation` aus `abstraction/schema.py` (Blob `5846232d…`) |
| **(P2)** | **Anzahl Komponenten und Relationen roh gegen geparst** | dieselbe Rohantwort | `arch_model.json` des Laufs |

**Jede Differenz bricht den Lauf ab und wird berichtet.** Massgeblich ist der **letzte**
Versuch — er erzeugt `arch_model.json` und damit jede berichtete Zahl. Die beiden Vergleiche
werden **zusätzlich** für jeden früheren Versuch gerechnet und mitberichtet, brechen aber
nicht ab: ein früher Versuch darf formfremd sein, dafür existiert die Retry-Schleife.

**Anlass, wörtlich gemessen.** Im Testcall vom 31.08.2026 lieferte die Antwort **zwei
Kanten**, das geparste Modell **null** (`z1_p_bericht_endpunktfrage.md` §3.3, Prüfung C:
*„components: 3 | relations: 0 · Relationen des Modells gehen verloren: 2 Kanten im Dokument
→ 0 im ArchModel"*). Die Kanten fielen **still** heraus: das Dokument trug sie unter
`dependencies` statt `relations`, das Schema erlaubt Fremdschlüssel
(kein `additionalProperties: false`), pydantic verwirft unbekannte Felder, und `relations`
hat einen Default. `ArchModel.model_validate_json()` nahm die Antwort **ohne Fehler** an und
lieferte ein **inhaltlich amputiertes** Modell.

**Dieselbe Fehlerklasse dreimal:**

- die **stille Null** aus Z3 (Protokoll §9 **T12**, Ergänzung Rev. 32: „stille Null durch
  Fehlkonfiguration bei den Konfigurationen ohne Laufprotokoll" — Graphmodus und `DEPOT_SRC`,
  beide erzeugten null Findings ohne Fehlermeldung);
- der **Artefaktauswahldefekt** (Befund 08, 08.10: elf K3-Injektionen wurden aus einem
  Artefakt mit `postrun.verdict = INVALID` als „0 Findings" gelesen);
- die **verlorenen Kanten** oben.

Gemeinsames Merkmal: **eine Fehlkonfiguration, die ein plausibles Ergebnis erzeugt, ohne zu
scheitern.** Dagegen hilft kein Exit-Code, sondern nur eine Gegeninstanz.

**Das Schema wird NICHT angepasst.** Es ist das Instrument, so wie die 17 archivierten Läufe
es benutzt haben; ein `additionalProperties: false` änderte den Messgegenstand mitten in der
Vergleichskette und machte die Juni-Läufe unvergleichbar. **Die Zusicherung sitzt an der
Parse-Grenze**, nicht im Schema.

**Was die Zusicherung nicht ist.** Sie ersetzt `validate_arch` nicht und greift nicht in die
Retry-Schleife ein. Sie ist eine Gegeninstanz **nach** dem Lauf, über Artefakte, die der
Extractor ohnehin schreibt.

### 5.4 Wiederholungen

- **Höchstens drei Wiederholungen je Bedingung.** Eine Wiederholung wird ausgelöst durch
  einen Abbruch nach §5.2 oder §5.3, oder durch einen technischen Fehlschlag (Transportfehler,
  HTTP-Fehler, Zeitüberschreitung).
- Danach wird die Bedingung als **nicht erhoben** ausgewiesen — **nicht als Nullwert**, nicht
  als 0, nicht als leere Zeile mit Strichen, die sich wie eine Messung liest. Die Zeile trägt
  „nicht erhoben" und den Grund.
- **Wiederholungsartefakte unter neuem Pfad, nie überschreiben.** Der Extractor legt je Lauf
  ein Verzeichnis `<zeitstempel>_r<index>` an (`run_logger.py:59`); Zeitstempel unterscheiden
  Wiederholungen bereits. Zusätzlich wird jede Wiederholung im Journal (§6) als solche mit
  Anlass geführt. Ein bestehendes Artefakt wird unter **keinen** Umständen ersetzt.
- **Auch abgebrochene Läufe werden archiviert und gehasht**, mit Abbruchgrund. Ein Lauf, der
  nur bei brauchbarem Ergebnis in den Bestand kommt, wäre die Auswahl nach Ergebnis, die
  dieser Abschnitt ausschliesst.

---

## 6. Aufzeichnung je Lauf

### 6.1 Vorbedingungen, je Lauf zu prüfen und zu protokollieren

| Vorbedingung | Soll |
|---|---|
| `git status --porcelain` im Extractor | **leer** — im neuen WSL-Klon `~/ma/ma-llm-arch-extractor` **wirklich leer**, nicht „60 CRLF-Zeilen" wie im alten Klon unter `/mnt/c/…` (`z1_1` §0.3; Gegenprobe E-X §0: „**leer** (keine 60 Zeilen)") |
| Extractor-`HEAD` | `5c0b65a82cc3d8af47c022d779ff63d8a20a9e08` |
| `git status --porcelain` in `masterarbeit` | leer |
| `python3 tools/check_doc_invariants.py` | Exit 0 |
| Schema-Hash in der Laufumgebung | `a83a84af…12ec0` (§3.2, §3.3 (4)) |
| Schema-Smoke gegen `inference.do-ai.run` | HTTP 200 (§3.3 (5)), nur vor K3 |

**Warum der leere Arbeitsbaum eine Messvorbedingung ist und keine Hygiene:** `repo_commit`
in `meta.json` entsteht als `git -C <repo_path> rev-parse HEAD` (`run_logger.py:103`, `:25-36`)
und ist damit der Extractor-`HEAD` zur Laufzeit. Genau dieses Feld war für 10 der 17
Juni-Läufe **kein** Codeanker, weil der Arbeitsbaum uncommittete Änderungen trug (§0.2 (b)).
Bei leerem Arbeitsbaum ist es einer.

### 6.2 Aufrufform

Eine Invocation je **Bedingung**, mit `--runs 3`:

```
cwd = ~/ma/ma-llm-arch-extractor
llm-arch extract fixtures/rich_repo --provider ollama       --model qwen2.5-coder:7b            --runs 3
llm-arch extract fixtures/rich_repo --provider digitalocean --model nvidia-nemotron-3-super-120b --runs 3
```

**Begründung für eine Invocation je Bedingung statt dreier Einzelaufrufe:** `cli.py:47`
zählt `run_index` über die Schleife hoch, sodass die drei Läufe **0, 1, 2** tragen und
eindeutig unterscheidbar sind. Drei Einzelaufrufe mit `--runs 1` trügen dreimal
`run_index: 0` — genau die Mehrdeutigkeit, an der Befund 04 nachträglich scheiterte (vier
Verzeichnisse mit `run_index [0, 0, 1, 2]`, „welche drei Verzeichnisse hier ausgewertet
wurden, ist nicht mehr rekonstruierbar"). Wiederholungen nach §5.4 laufen als
Einzelinvocation mit `--runs 1` und werden im Journal ausdrücklich als Wiederholung geführt.

`max_retries` bleibt auf der Vorgabe **2** (`cli.py:36`), wie in den Befunden 02–04.
`--gold` gibt es nicht: `_load_gold` (`cli.py:22-27`) findet `fixtures/rich_repo.gold.json`
als Geschwisterdatei selbsttätig, `gold_similarity` wird deshalb in jedem Lauf gerechnet.

### 6.3 Aufzuzeichnen je Lauf

Aus dem Laufartefakt (schreibt der Extractor selbst):

`timestamp` · `provider` · `base_url` · `model` · `model_version` · `temperature` ·
`prompt_version` · `repo_path` · `repo_commit` · `run_index` · `prompt_tokens` ·
`completion_tokens` · `latency_ms` · `valid_raw` · `valid_final` · `attempts_used` ·
`validation_errors` · die vier Treuegrössen · die sechs Kompressionsgrössen ·
`gold_similarity` · `gold_similarity_method`.

Dazu die vollständigen Verzeichnisse `attempts/attempt_<n>/` mit `prompt.txt`,
**`raw_response.json` unverändert** und `validation.json`, sowie `input_facts.json`,
`arch_model.json` und `output.ilograph.yaml`.

Vom Journal daneben zu schreiben (steht **nicht** im Laufrecord):

| Wert | Grund |
|---|---|
| Extractor-`HEAD` und `git status --porcelain` **vor** dem Lauf | §6.1 |
| Prompt-Blob `6c8e4639…` | `meta.json` führt nur `prompt_version` |
| Schema-Hash `a83a84af…` | nirgends im Log (Folgeposten 3) |
| `seed` = 0 | nicht im Record, 29 Felder ohne ihn (§3.3 (1)) |
| Python-, pydantic-, openai-Version | nirgends erfasst (§3.3 (4)) |
| **externe Wanduhrzeit** je Invocation, monotone Uhr | Innen- und Aussenmessung nie mischen (Z3-Protokoll §5, Nachtrag Rev. 30) |
| Ergebnis der Parse-Zusicherung (P1, P2) je Lauf und je Versuch | §5.3 |
| Anlass bei Wiederholungen | §5.4 |

`latency_ms` bleibt der Innenwert je Lauf aus `meta.json` und wird als solcher benannt.

### 6.4 Archivwurzel

**`masterarbeit/data/z1/`**, im Thesis-Repo versioniert, mit `SHA256SUMS` und `MANIFEST.md`
nach Abschluss. Der Extractor schreibt nach `<cwd>/runs/` (`run_logger.py:55`, Vorgabe
`runs_dir="runs"`, im Extractor über `.gitignore` Zeile 1 ausgenommen); die Laufverzeichnisse
werden **unverändert** dorthin kopiert und dort gehasht.

**Nicht im Scratchpad.** Präzedenz ist der **C4c-Verlustfall**: die sechzehn Laufdateien der
Vorabprüfung lagen „im flüchtigen Arbeitsverzeichnis dieses Auftrags" und sind nicht abgelegt
(`c4c_bericht_vorabpruefung.md` Teil C; deshalb wurde die Z3-Archivwurzel mit Amendment
Rev. 34 vom Scratchpad nach `data/campaign/` gezogen, Z3-Protokoll §0.1). Das Scratchpad ist
flüchtig; ein Rohlogarchiv verlangt einen versionierten Pfad.

**Nachzugsregel, wie unter `data/soll/`:** jede Änderung unter `data/z1/` zieht `SHA256SUMS`
und `MANIFEST.md` im **selben Commit** nach.

---

## 7. Auswertung und Berichtsform

### 7.1 Die Ergebnistabelle

**Eine** Tabelle, Ansatz × Kennzahl. Ansatz 2 steht mit **Median und Spannweite** je
Bedingung, Ansatz 1 mit seinem **deterministischen Einzelwert**:

| Kennzahl | Ansatz 1 — Triton (deterministisch, ein Wert) | Ansatz 2 — K2 `qwen2.5-coder:7b` (Median · Spannweite, n=3) | Ansatz 2 — K3 `nvidia-nemotron-3-super-120b` (Median · Spannweite, n=3) |
|---|---|---|---|
| `relation_precision` | | | |
| `relation_recall` | | | |
| `module_coverage` | | | |
| `phantom_modules` | | | |
| `module_count` | | | |
| `component_count` | | | |
| `module_compression` | | | |
| `import_edge_count` | | | |
| `component_relation_count` | | | |
| `relation_compression` | | | |
| `gold_similarity` *(gold-bezogen, Referenzsignal)* | | | |
| `valid_raw` / `valid_final` / `attempts_used` | *(entfällt — kein Lauf)* | | |

Daneben, **nicht** in derselben Tabelle: die drei Einzelläufe je Bedingung mit allen Werten,
und die Kostenzeile (`prompt_tokens`, `completion_tokens`, `latency_ms`, externe Wanduhrzeit).

**Berichtsform: Grössenordnungen.** Keine Nachkommastellen-Interpretation (§5.1).

**K2 und K3 stehen in getrennten Zeilen und werden NIRGENDS addiert oder gemittelt.**
Befund 08, methodische Konsequenz **(a)**: *„Kapitel 7 und 8 führen ‚der LLM-Pfad' nicht mehr
als eine Grösse — nicht aus Formulierungsvorsicht, sondern weil K2 und K3 bei nahezu gleicher
Meldequote um den Faktor fünf in der Präzision auseinanderliegen. Aussagen über
‚LLM-gestützte Konformitätsprüfung' ohne Angabe der Modellklasse sind durch diese Messung
nicht gedeckt."* Für Z1 gilt dasselbe eine Stufe früher: es gibt keinen „LLM-Ansatz", es gibt
K2 und K3.

Die Zelle `valid_*` für Ansatz 1 trägt **„entfällt — kein Lauf"**, nicht 1.0 und nicht einen
Strich: Validität ist eine Eigenschaft einer Modellausgabe, und Ansatz 1 erzeugt keine
(§2.3).

### 7.2 BAUPOSTEN D1b — hier entschieden

**Der Befund.** `scripts/compare_runs.py:18-22` führt in `COLS`:

```python
COLS = [
    "model", "run_index", "module_coverage", "relation_precision",
    "relation_recall", "phantom_modules", "valid_raw", "valid_final",
    "attempts_used", "prompt_tokens", "completion_tokens", "latency_ms",
]
```

Alle vier **Treuegrössen** stehen darin, **keine** der sechs **Kompressionsgrössen** —
obwohl `run_logger.py:116-121` sie in jede `meta.json` schreibt. Die Zahlen liegen also vor;
das Anzeigewerkzeug holt sie nur nicht ab.

**Zwei Wege standen zur Wahl:** (i) `COLS` ergänzen — eine Werkzeugänderung im Extractor,
**vor** dem Lauf, mit Fixture-Test; (ii) die Kompressionsgrössen direkt aus `meta.json`
lesen — kein Extractor-Eingriff.

**Entschieden: Weg (ii).** Die Kompressionsgrössen werden **direkt aus `meta.json`** gelesen,
über ein Auswertungsskript in `masterarbeit/tools/`. `scripts/compare_runs.py` bleibt
**byteidentisch** (`c6db316b…`) und wird unverändert als **Gegenprobe** benutzt für genau
das, was es rechnet: Byte-Identität der `arch_model.json` über die Läufe einer Gruppe und
`validity_rate(valid_final)`.

**Begründung, in der Reihenfolge ihres Gewichts.**

1. **Weg (i) löste das Problem nicht, sondern nur ein Achtel davon.** Die Ergebnistabelle
   aus §7.1 verlangt **Median und Spannweite** je Bedingung sowie den deterministischen
   Einzelwert von Ansatz 1. `compare_runs.py` bildet **weder** Median **noch** Spannweite
   **noch** eine Ansatz-1-Zeile — es druckt eine Zeile je Lauf und zwei Gruppenaggregate
   (`:51-64`). Ein Auswertungsskript in `masterarbeit` ist also **ohnehin** nötig; und dieses
   Skript liest `meta.json`. Wären die Kompressionsspalten in `COLS` ergänzt, läse es sie
   trotzdem aus derselben Quelle. Die Extractor-Änderung kaufte **nichts**, was nicht
   anderswo ohnehin entsteht.
2. **Der Extractor ist der Messgegenstand, und jede Änderung bewegt ihn.** Er ist als
   eingefroren geführt (`00_stand_und_entscheidungen.md` §0, „Eingefroren außer dem
   zurückgestellten Logging-Fix (D3)"). E-X hat ihn mit drei Commits bewegt — begründet, mit
   Blob-Gegenprobe, dass keine Fixture und keine Formel berührt wurde. Ein vierter Commit
   für eine reine Anzeigespalte hat dieses Gewicht nicht, verlangte aber denselben Apparat:
   eigenen schreibenden Auftrag (stehende Regel 4), Fixture-Test, Blob-Nachzug in `z1_1`,
   `z1_2` und `PROVENANCE.md`.
3. **Die Zusicherung aus §5.3 sitzt ohnehin ausserhalb des Extractors.** Parse-Zusicherung,
   Gültigkeitsprüfung und Aggregation gehören in ein Werkzeug, das im Thesis-Repo versioniert,
   gehasht und registriert ist — dorthin, wo auch `tools/evaluate_campaign.py` für Z3 liegt.
   Die Kompressionsgrössen dort abzuholen ist keine Ausnahme, sondern der Regelfall.

**Was Weg (ii) kostet, offen benannt:** ein zweites Werkzeug neben `compare_runs.py`, das
dieselben `meta.json` liest. Die Doppelung ist gewollt — sie ist die Gegeninstanz aus §5.3
in Werkzeugform. Weichen die beiden in einer Zahl voneinander ab, ist das ein **Befund**, der
berichtet und nicht durch Angleichen aufgelöst wird (Praxis der T7-Gegenprobe, Z3-Protokoll
§0.1).

**Auflage.** Das Auswertungsskript wird **vor** dem ersten Z1-Lauf geschrieben, mit einem
Fixture-Test versehen, gehasht, und sein SHA256 wird als **Amendment** (§10) in dieses
Protokoll aufgenommen — analog zur Registrierung der drei Auswertungsinstrumente in
Z3-Protokoll §0.1. Es liest ausschliesslich Felder, die `run_logger.py` bereits schreibt, und
**erfindet keine Kennzahl** (§4.5).

### 7.3 Was NICHT gerechnet wird

Kein Aggregat über K2 und K3. Kein Aggregat über Ansatz 1 und Ansatz 2. Kein Verhältnis
„Ansatz 2 zu Ansatz 1" als einzelne Zahl. Keine Signifikanzaussage bei n = 3. Keine
Extrapolation auf andere Fixtures (Befund 02, Integritätshinweis: Faktentreue-Zahlen sind
**nur innerhalb desselben Fixtures** vergleichbar).

---

## 8. Vorregistrierte Erwartungen

Jede Erwartung mit Fundstelle und in einer Fassung, die **scheitern kann**. Wo die Befunde
keine gerichtete Erwartung hergeben, steht das ausdrücklich da.

**Vorbemerkung zur Sicherheit dieser Erwartungen.** Sie stammen aus den Befunden 01–05, also
aus der formativen Serie, die Z1 nach §0.2 **nicht trägt**. Sie sind **Vorwissen**, nicht
Messung; sie werden hier registriert, damit die Z1-Zahlen an etwas scheitern können, und
nicht, um sie zu stützen. Die K3-Erwartungen ruhen zusätzlich auf einem **anderen
Zugangsweg** (OpenRouter, §9 T-Z1-5).

### E1 — Ansatz 1, Faktentreue: die vier Werte sind bekannt und müssen zeichengleich fallen

`tests/test_reader.py:53-61` (Blob `7fc33d1b…`) sichert für die Fixture zu:
`relation_precision == 1.0`, `relation_recall == 1.0`, `module_coverage == 1.0`,
`phantom_modules == 0`, mit dem Kommentar *„Triton transcribes imports deterministically →
perfect fact-fidelity."*

**Keine Erwartung im Sinne einer Vorhersage, sondern eine gehashte Festlegung.** Die
Nachrechnung in Z1 (§2.1) muss diese vier Werte **zeichengleich** treffen. **Falsifiziert
durch:** jede Abweichung — sie wäre ein Befund über das Instrument (Reader, Metrik oder
Fixture), nicht über Triton, und bricht die Auswertung ab.

### E2 — Ansatz 1, Kompression: 11 / 4 / 2.75 · 16 / 5 / 3.2

`tests/test_reader.py:64-73` sichert zu: `module_count == 11`, `component_count == 4`,
`module_compression == 11/4`, `import_edge_count == 16`, `component_relation_count == 5`,
`relation_compression == 16/5`.

**Ebenfalls eine Festlegung, keine Vorhersage.** Falsifiziert durch jede Abweichung.

> **Eine ältere Erwartung ist damit bereits überholt und wird nicht stillschweigend fallen
> gelassen.** Befund 02, Konsequenz 4 erwartete für Triton „~1.0 Treue / **~1.0 Kompression**
> (treu, flach)". Die Treuehälfte trifft zu; die **Kompressionshälfte ist falsch**: Triton
> faltet auf dieser Fixture mit **2.75** Modulen je Komponente und **3.2** Importkanten je
> Komponentenrelation, weil seine Komponenten die **Schichtenpakete** sind und nicht die
> Module (`test_reader.py:31`, „decision 3: component = layer package"). **Ansatz 1
> abstrahiert also ebenfalls** — er ist flach in der Treue, nicht in der Faltung. Die
> UF1-Pointe „Abstraktion erkauft man mit struktureller Treue" ist damit **nicht** als
> „Triton komprimiert nicht" zu erzählen. Festgehalten vor der Messung, damit die Korrektur
> nicht nachher wie eine Anpassung an die Daten aussieht.

### E3 — K2, Faktentreue: Precision hoch, Recall bei etwa der Hälfte

Befund 04.1 misst für `qwen2.5-coder:7b` unter **Prompt v3**, drei Läufe:
`relation_precision` 1.00, `relation_recall` **0.57 / 0.50 / 0.50**, `module_coverage` 1.00,
`phantom_modules` 0.

**Erwartung:** `relation_precision` ≥ 0.9 im Median; `relation_recall` im Median **zwischen
0.40 und 0.70**; `module_coverage` == 1.0 in allen drei Läufen; `phantom_modules` == 0 in
allen drei Läufen.

**Falsifiziert durch:** einen Median-Recall ausserhalb [0.40, 0.70]; eine Coverage < 1.0;
ein `phantom_modules` > 0 in irgendeinem Lauf; eine Median-Precision < 0.9.

### E4 — K3, Faktentreue: Precision hoch, Recall hoch

Befund 04.1 misst für nemotron-120B unter Prompt v3, drei Läufe: `relation_precision` 1.00,
`relation_recall` **1.00 / 1.00 / 0.80**, `module_coverage` 1.00, `phantom_modules` 0. Der
dritte Lauf verlor genau die „nach innen"-Kante `infrastructure → domain` (Befund 04.3,
Varianz-Detail).

**Erwartung:** `relation_precision` ≥ 0.9 im Median; `relation_recall` im Median **≥ 0.80**;
`module_coverage` == 1.0; `phantom_modules` == 0.

**Falsifiziert durch:** einen Median-Recall < 0.80; eine Coverage < 1.0; ein
`phantom_modules` > 0.

**Ausdrücklich schwächer gestützt als E3:** die Zahlen stammen von OpenRouter mit dem Slug
`nvidia/nemotron-3-super-120b-a12b:free`, gemessen wird der Direktzugang mit der Katalog-ID
`nvidia-nemotron-3-super-120b` (§9 T-Z1-5).

### E5 — K3 erreicht mindestens den Recall von K2

Befund 04.2: die Recall-**Lücke** war der Prompt (beide Modelle steigen mit v3), die
verbleibende Recall-**Decke** ist **Kapazität** — „sobald der Prompt Relationen einfordert,
nutzt das 120B sie voll aus (recall ~1.0); das 7B plateauert bei ~0.5 (lässt Querkanten weg,
**obwohl** gefordert)".

**Erwartung:** Median-`relation_recall` von **K3 ≥ K2**, mit einem Abstand von mindestens
0.20.

**Falsifiziert durch:** einen Median-Recall von K3, der den von K2 nicht um mindestens 0.20
übersteigt. Das wäre der interessantere Ausgang: er stellte den Kapazitätsbefund aus 04.2 auf
diesem Zugangsweg in Frage.

### E6 — Determinismus: KEINE der beiden Bedingungen ist byte-identisch über drei Läufe

Befund 04.3: unter v2 waren die drei 7B-Läufe **byte-identisch** (Befund 01.1), unter **v3
nicht mehr** — 5 gegen 6 Komponenten, Recall 0.57 gegen 0.50, „der anspruchsvollere Prompt
bringt Run-Varianz selbst bei `temperature=0`". Befund 03.1: nemotron ist hosted **nicht**
byte-deterministisch trotz gesetztem Seed (Completion-Tokens 1464 / 1822 / 1061). DDR N,
Punkt 5: der Seed ist über OpenRouter nachweislich nicht honoriert; für den Direktzugang
ungemessen (§3.3 (1)).

**Erwartung:** in **beiden** Bedingungen sind die drei `arch_model.json` **nicht** alle
byte-identisch (gemessen mit `compare_runs.py`, „output byte-identical: False").

**Falsifiziert durch:** eine Bedingung, deren drei Läufe byte-identisch ausfallen. Für K3
wäre das ein starker, positiver Nebenbefund zur Seed-Honorierung des Direktzugangs — und der
einzige Anlass, DDR N Punkt 5 für diesen Endpunkt zu relativieren.

### E7 — Kompression: beide LLM-Bedingungen falten stärker als 1:1, K2 feiner als K3

Aus `z1_2` §4.3 (v3-Läufe, Zeilen 11–17): K3 lieferte durchgehend **11 / 4 / 2.75**, K2
**11 / 5 / 2.2** und zweimal **11 / 6 / 1.8333**.

**Erwartung:** `module_count` == 11 in allen sechs Läufen; `component_count` in beiden
Bedingungen **zwischen 3 und 7**; `module_compression` überall **> 1.0** (also keine
1:1-Wiedergabe der Modulliste); Median-`component_count` von **K2 ≥ K3**.

**Falsifiziert durch:** ein `module_compression` ≤ 1.0 (das wäre Transkription statt
Abstraktion und widerlegte die Kernhypothese von Ansatz 2, Befund 01.2); ein
`component_count` ausserhalb [3, 7]; ein Median-`component_count` von K2 unter dem von K3.

### E8 — Perspektivendivergenz: K3 schichtenorientiert, K2 nicht

Befund 01.3, 03.3 und 04.1: das 7B schneidet **vertikal** (service-orientiert: api-gateway,
catalog-service, order-service, …), nemotron **horizontal** (die vier Schichten api /
application / domain / infrastructure) — beides legitime Sichten, keine ist ein Fehler.

**Entscheidungsregel, damit die Erwartung prüfbar ist statt interpretativ:** eine Zerlegung
heisst **schichtenorientiert**, wenn ihre Modul→Komponente-Abbildung mit der Reduktion des
Triton-Exports einen `adjusted_rand_index` von **1.0** ergibt (also dieselbe Partition, ohne
Rücksicht auf die Namen), sonst **nicht schichtenorientiert**.

**Erwartung:** K3 schichtenorientiert im Median der drei Läufe; K2 in keinem Lauf
schichtenorientiert.

**Falsifiziert durch:** einen K2-Lauf, der die Schichtenpartition trifft, oder eine
K3-Mehrheit, die sie verfehlt.

### E9 — `gold_similarity`: K3 nahe 1.0, K2 deutlich darunter — als Referenzsignal, nicht als Güte

`z1_2` §4.3: die v3-Läufe tragen `gold_similarity` **1.0** (K3) und **0.3902 / 0.3836 /
0.3836** (K2). Der Grund ist E8, nicht Qualität: die Gold-Partition ist die Schichtensicht.

**Erwartung:** Median-`gold_similarity` K3 **≥ 0.9**, K2 **≤ 0.6**.

**Falsifiziert durch:** Werte ausserhalb. **Ausdrücklich keine Güteaussage** (§4.4): ein
niedriger Wert bei K2 belegt eine **andere legitime Sicht**, keine schlechtere Ableitung.

### E10 — Validität: alle sechs Läufe final gültig, Roh-Validität offen

Befund 02.1 und 04: die Retry-Schleife wirkt wie entworfen; `valid_final` war in allen
v3-Läufen `true`, `valid_raw` teils `false` (`z1_2` §4.3: bei K2 in allen drei v3-Läufen
`false`, bei K3 in zwei von drei `true`).

**Erwartung:** `valid_final == true` in **allen sechs** Läufen.

**Falsifiziert durch:** einen einzigen Lauf mit `valid_final == false` nach drei Versuchen.
Für `valid_raw` und `attempts_used` besteht **keine gerichtete Erwartung** — die Werte
schwanken in der Vorgeschichte in beide Richtungen und sind selbst UF4-Messgrössen.

### Wo keine gerichtete Erwartung besteht

- **Kosten und Latenz.** Der einzige Datenpunkt für den Direktzugang ist der Testcall vom
  31.08.2026 (18,2 s für 376 Completion-Token) — mit einem **minimalen** Prompt, nicht dem
  Produktionsprompt v3 (`z1_p_bericht_endpunktfrage.md` §3.4). Die Juni-Zahlen stammen von
  OpenRouter. **Keine gerichtete Erwartung** für `latency_ms`, `prompt_tokens`,
  `completion_tokens` oder die externe Wanduhrzeit; die Werte werden erhoben und berichtet.
- **`attempts_used` und `valid_raw`** — siehe E10.
- **Skalierung.** Befund 05 (Single-Prompt kollabiert am echten Repo, ROT auf beiden
  Modellen) betrifft ein Repo mit ~19 Paketen, nicht die 11-Modul-Fixture. Er trägt für Z1
  **keine** Erwartung und wird hier **nicht** als eine geführt.
- **`relation_compression` bei null Relationen.** Ob der Fall eintritt, ist offen (er trat in
  der v2-K3-Serie ein, `z1_2` §4.3 Läufe 8–10); tritt er ein, steht dort `null` (§4.2), und
  das ist der Wert, nicht eine fehlende Messung.

---

## 9. Threats to Validity (vorregistriert)

**T-Z1-1 — Fixture-Asymmetrie: Artefakt gegen Verteilung.** Ansatz 1 liegt als
archiviertes, deterministisches Artefakt vor; Ansatz 2 wird neu gemessen (§2.3). Die beiden
Seiten des Vergleichs sind damit **methodisch ungleich**: eine hat keine Streuung, die andere
hat eine, und die Werte der einen Seite waren vor der Messung bekannt (E1/E2), die der
anderen nicht. **Gegenposition:** ein Neulauf von Triton änderte daran nichts — er ist
deterministisch und lieferte dieselbe Datei; die Asymmetrie liegt in der Natur der beiden
Ansätze, nicht in der Versuchsanordnung. **Mitigation:** offene Benennung in §2.3, getrennte
Spalten in §7.1, Sprachregelung „Extraktionsvergleich" statt „Head-to-Head-Lauf".

**T-Z1-2 — Eine einzige Fixture mit 11 Modulen und 5 induzierten Kanten.** Jede Zahl dieses
Protokolls ist an `rich_repo` gemessen. Befund 04.2, Geltungsbereich: *„Single-Fixture-Befund
(11 Module, 5 induzierte Kanten — n klein). ‚Decke = Kapazität' ist über **ein** Fixture
generalisiert."* Befund 02, Integritätshinweis: Faktentreue- und Kompressionszahlen sind
**nur innerhalb desselben Fixtures** vergleichbar. Bei fünf induzierten Kanten verschiebt
**eine** Kante den Recall um 0.20. **Keine Mitigation im Rahmen von Z1** — ein zweites
Fixture ist Future Work; der Threat wird in Kapitel 6 als Geltungsgrenze geführt und begrenzt
jede Aussage auf diese Fixture.

**T-Z1-3 — Gold-Degradierung und Autorenidentität.** `gold_similarity` misst Ähnlichkeit zu
**einer** Referenzpartition, die derselbe Autor geschrieben hat wie die Fixture, im **selben
Commit** wie die ARI-Rechnung, die sie auswertet (`z1_2` §5.1). Befund 01.3 hat gezeigt, dass
eine Abweichung von Gold eine **legitime andere Sicht** sein kann. **Mitigation:** `gold`
ist als Referenzsignal deklariert (§4.4), die tragenden Kennzahlen sind gold-frei, und E9
sagt die Divergenz **vorher** — sie kann daher nicht nachträglich als Qualitätsaussage
gelesen werden.

**T-Z1-4 — Der Exporter hat sich seit der Fixture dreimal geändert, einmal semantisch.**
`fixtures/PROVENANCE.md` §8 (`d1_bericht_fixture_provenienz.md` §8) führt drei Commits nach
dem Fixture-Export vom 26.06.2026: `2b95ccb` (02.07., Ansichts-Toggle entfernt), `2003e50`
(03.07., Sichtbarkeiten und `rollupImportRelations`) — beide am Exporter, **nicht** am
Vollexport-Pfad — und **`d26c790`** (04.07.,
*„fix(python): resolve relative imports in `__init__.py` against the package itself"*),
**semantisch**: er verschiebt **Importkanten**, also genau die Grösse, aus der 16/5 gerechnet
ist. **Für `rich_repo` ist kein Effekt zu erwarten** — die vier Paket-`__init__.py` sind leer
(Blob `e69de29b…`) und die Fixture nutzt absolute Importe — **aber „nicht zu erwarten" ist
keine Messung.** Ein Re-Export wurde bewusst **nicht** ausgeführt (es gibt kein
CLI-Kommando; die Datei entsteht nur über den Vue-Editor als Browser-Download) und fiele
ohnehin nicht byte-identisch aus, weil Beschreibungszeile und Dateiname von Hand gekürzt
wurden. **Der Threat bleibt offen und wird als offener geführt.**

**T-Z1-5 — K3-Endpunkt ungepinnt, kein bezeugter Seed.** Strukturell dieselbe Lage wie
**T14** im Z3-Protokoll: die Vormessungen, auf denen die K3-Erwartungen ruhen (Befunde 03/04,
`z1_2` §4.3), liefen über **OpenRouter** mit dem Slug
`nvidia/nemotron-3-super-120b-a12b:free`; gemessen wird der **DigitalOcean-Direktzugang** mit
`nvidia-nemotron-3-super-120b`. Belegt ist: das `model`-Echo des Testcalls ist zeichengleich
mit der angeforderten ID, ohne Router-Suffix. **Nicht belegbar und hier nicht behauptet:**
Quantisierung, Präzision, Gewichts-Revision, Serving-Stack — **die Identität der Gewichte ist
nicht verifiziert**. Dazu: `system_fingerprint` ist `null` (kein Backend-Anker), `seed=0`
wird gesendet, aber nicht als wirksam angenommen (§3.3 (1)), und es existiert im Extractor
**kein** Gegenstück zu `CONFORMANCE_PROVIDER_PIN` (B32 ist ein Instrument des Checkers).
**Mitigation:** E6 macht die Varianz zum vorhergesagten Messgegenstand statt zur Störung;
E4 ist als schwächer gestützt gekennzeichnet.

**T-Z1-6 — `strict` ohne Formgarantie.** Der Endpunkt nimmt das Schema an, ohne OpenAIs
strengen Prüfer zu fahren; eine formal schemagültige Antwort kann formfremd sein, und
pydantic verwirft die fremden Felder still (§3.3 (3), §5.3). **Die Form trägt in Produktion
der Prompt.** **Mitigation:** die Parse-Zusicherung aus §5.3, die genau diese Lücke schliesst
— und zwar **vor** der Messung gebaut, nicht nach dem ersten unplausiblen Ergebnis.

**T-Z1-7 — Zirkularität zwischen Prompt v3 und der Recall-Metrik.** Befund 04.1,
Zirkularitäts-Caveat: v3 instruiert das Modell, den Import-Graphen zu spiegeln (*„emit a
relation whenever a module imports across components"*) — und **genau gegen diesen
Import-Graphen** misst `relation_recall`. Ein hoher Recall ist damit **teilweise
hineininstruiert**. **Das diskriminierende Signal ist deshalb nicht ein hoher Wert, sondern
die Abweichung davon trotz ausdrücklicher Aufforderung** (E5). Zugleich schaltet die Klausel
*„do not invent unbacked ones"* den semantischen Inferenzkanal ab, den Befund 02.4
hypothetisiert hatte — für UF1 gewollt (rein strukturelle Treue), als Vorwärtsrisiko in
Befund 04, Konsequenz 4 benannt. **Keine Mitigation, sondern eine Lesevorschrift:** Z1
misst **strukturelle Import-Faktentreue** und nichts darüber hinaus.

**T-Z1-8 — Laufzeitversionen ungelockt.** `pyproject.toml` deklariert nur `openai>=1.0` und
`pydantic>=2.0`, eine Lockdatei existiert nicht (§3.3 (4)). Die Drahtform des Requests und
die **Schema-Bytes** hängen an der installierten Version; ein anderer pydantic-Stand kann bei
unverändertem Quelltext einen anderen Schema-Hash erzeugen. **Mitigation:** die drei
Versionen werden registriert (§3.3 (4)), in der Laufumgebung erhoben und ins Journal
geschrieben, und der Schema-Hash wird vor dem Lauf nachgerechnet; eine Abweichung des
Schema-Hashs verhindert den Lauf.

**T-Z1-9 — Die Erwartungen stammen aus der Serie, die Z1 nicht trägt.** §8 leitet aus den
Befunden 01–05 ab, und §0.2 stellt fest, dass genau diese Läufe Z1 nicht tragen. **Das ist
kein Widerspruch, sondern die Rollenverteilung:** sie liefern **Vorwissen** für falsifizierbare
Erwartungen, nicht Evidenz. **Mitigation:** die Trennung ist in §8, Vorbemerkung, ausdrücklich
benannt; keine Z1-Aussage stützt sich auf eine Juni-Zahl.

**T-Z1-10 — `repo_commit` verankert den Code, nicht den Eingang.** Das Feld ist der
Extractor-`HEAD` zur Laufzeit (`run_logger.py:103`, `:25-36`) und unterscheidet **keine
Eingänge** — die Fixture liegt im selben Repo. Für die Juni-Läufe war es zusätzlich **kein**
Codeanker (§0.2 (b)). **Mitigation:** der leere Arbeitsbaum als Messvorbedingung (§6.1) macht
es für die Z1-Läufe zu einem; die Eingangsseite ist über die Blob-Hashes aus §3 verankert,
nicht über `repo_commit`.

---

## 10. Amendments

**Revisionshistorie vor Freeze** (Änderungen am Entwurf, solange keine Messung läuft):

| Rev | Datum | Änderung | Begründung |
|---|---|---|---|
| — | — | *(keine)* | — |

**Amendments nach Freeze** (datiert, mit Begründung; geführt zugleich in der
Revisionshistorie im Kopf):

| Rev | Datum | Änderung | Begründung |
|---|---|---|---|
| — | — | *(keine)* | — |
