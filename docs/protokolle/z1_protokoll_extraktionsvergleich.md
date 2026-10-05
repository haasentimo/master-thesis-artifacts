# Z1-Protokoll — Extraktionsvergleich: deterministische Ableitung gegen LLM-Abstraktion (UF1)

Stand: 1. September 2026 (Rev. 6) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 1,
31. August 2026** (Commit `34d6738`, SHA256 bezeugt in `z1_p_bericht_freeze.md` §3) —
darauf die Amendments Rev. 2 (Z1-R, §8 E8), Rev. 3 (Z1-T, Kontextfenster als
registrierter Laufparameter, Lieferzusicherung P3, Rücksetzung des K2-Wiederholungsbudgets,
Archivpfade), Rev. 4 (Z1-A, Klarstellung der beiden Fälle von „nicht erhoben" in §5.4,
Registrierung des Ollama-Digests als Messeingang in §3.3 (7)), Rev. 5 (Z1-A, SHA256 des
Auswertungsskripts nach der Auflage in §7.2) und Rev. 6 (N07, Ausführungsgeometrie des
Inferenzservers als bezeugungspflichtiger Umgebungsparameter, §9 T-Z1-11)
~~Stand: 1. September 2026 (Rev. 5) · Status: EINGEFROREN zur Vorregistrierung, Rev. 1,
31. August 2026 (Commit `34d6738`, SHA256 bezeugt in `z1_p_bericht_freeze.md` §3) —
darauf die Amendments Rev. 2 (Z1-R, §8 E8), Rev. 3 (Z1-T, Kontextfenster als
registrierter Laufparameter, Lieferzusicherung P3, Rücksetzung des K2-Wiederholungsbudgets,
Archivpfade), Rev. 4 (Z1-A, Klarstellung der beiden Fälle von „nicht erhoben" in §5.4,
Registrierung des Ollama-Digests als Messeingang in §3.3 (7)) und Rev. 5 (Z1-A, SHA256 des
Auswertungsskripts nach der Auflage in §7.2)~~
(überholt am 01.09.2026 durch N07, Rev. 6 — die Zeile führte die Amendments bis Rev. 5.
**Kein Kennzahlenteil ist berührt**: §4, §7 und §8 stehen unbewegt; bewegt ist §9 um einen
Threat)
~~Stand: 31. August 2026 (Rev. 4) · Status: EINGEFROREN zur Vorregistrierung, Rev. 1,
31. August 2026 (Commit `34d6738`, SHA256 bezeugt in `z1_p_bericht_freeze.md` §3) —
darauf die Amendments Rev. 2 (Z1-R, §8 E8), Rev. 3 (Z1-T, Kontextfenster als
registrierter Laufparameter, Lieferzusicherung P3, Rücksetzung des K2-Wiederholungsbudgets,
Archivpfade) und Rev. 4 (Z1-A, Klarstellung der beiden Fälle von „nicht erhoben" in §5.4,
Registrierung des Ollama-Digests als Messeingang in §3.3 (7))~~
(überholt am 01.09.2026 durch Z1-A, Rev. 5 — die Zeile führte die Amendments bis Rev. 4.
**Kein Kennzahlenteil ist berührt**: §4, §7.1 und §8 stehen unbewegt; bewegt ist §7.2 um
zwei Hashes)
~~Stand: 31. August 2026 (Rev. 3) · Status: EINGEFROREN zur Vorregistrierung, Rev. 1,
31. August 2026 (Commit `34d6738`, SHA256 bezeugt in `z1_p_bericht_freeze.md` §3) —
darauf die Amendments Rev. 2 (Z1-R, §8 E8) und Rev. 3 (Z1-T, Kontextfenster als
registrierter Laufparameter, Lieferzusicherung P3, Rücksetzung des K2-Wiederholungsbudgets,
Archivpfade)~~
(überholt am 31.08.2026 durch Z1-A, Rev. 4 — die Zeile führte nur die ersten drei
Amendments. **Kein Kennzahlenteil ist berührt**: §4, §7 und §8 stehen unbewegt; bewegt sind
§3.3 um einen Umgebungsparameter und §5.4 um eine Berichtsunterscheidung)
~~Stand: 31. August 2026 (Rev. 2) · Status: EINGEFROREN zur Vorregistrierung, Rev. 1,
31. August 2026 (Commit `34d6738`, SHA256 bezeugt in `z1_p_bericht_freeze.md` §3) —
darauf das Amendment Rev. 2 (Z1-R, Klarstellung der Entscheidungsregel in §8 E8 und
Auflage zur Handrechnung des ARI)~~
(überholt am 31.08.2026 durch Z1-T, Rev. 3 — die Zeile führte nur das erste Amendment.
**Kein Kennzahlenteil ist berührt**: §4 steht unbewegt; bewegt sind §3.3 um einen
Umgebungsparameter, §5.3 um eine Zusicherung, §5.4 um die Budgetlage einer Bedingung und
§6.4 um zwei Pfade)
~~Stand: 31. August 2026 (Rev. 1) · Status: Entwurf zur Vorregistrierung — Freeze steht aus~~
(überholt am 31.08.2026 durch Z1-R, Rev. 2 — die Zeile stand noch auf dem Stand **vor**
dem Freeze; eingefroren ist das Dokument seit `34d6738` vom 31.08.2026, bezeugt in
`z1_p_bericht_freeze.md` §3. **Kein Messteil ist berührt**: Kennzahlen §4, Gültigkeit §5,
Aufzeichnung §6 und Berichtsform §7 stehen unbewegt)

**Revisionshistorie**

Rev. 6: 01.09.2026 (Auftrag N07) — Amendment nach dem Freeze, **eine Stelle, kein
Kennzahlenteil berührt**. §9 **T-Z1-11 neu**: die **Ausführungsgeometrie des
Inferenzservers** — `n_ctx` (`-c`), die daraus abgeleitete Batchgrösse (`-b`/`-ub`) und die
KV-Cache-Geometrie — ist ein **bezeugungspflichtiger Umgebungsparameter**; künftige Läufe
führen sie samt Serverversion und Startparametern im **Laufrecord**, erhoben am laufenden
Prozess statt angenommen. **Belegt, nicht vermutet** (Diagnoseläufe Z1-S/Z1-S2,
`z1_s_bericht_diagnoselauf.md` §6–§8): identische Eingabe — token-für-token derselbe
Erstprompt, 4 095 IDs —, identisches Modell, identische Binärversion 0.30.10,
`temperature=0` und `seed=0`, und dennoch **verschiedene Ausgabe** (1 517 gegen 2 261
Zeichen); der eine Lauf `valid_final = true` mit 0 Fehlern, der andere `valid_final = false`
mit 14 Fehlern der Klasse `relation`. **Rev. 4** registrierte den **Modell**-Digest als
Messeingang (§3.3 (7)); dies ist die **Ergänzung um die Serverkonfiguration** — derselbe
Blob unter anderer Geometrie ist nicht derselbe Messstand. **Registriert wird kein Wert
rückwirkend**, und für den vorhandenen Bestand folgt **keine** Aufzeichnungspflicht. **Keine
Kennzahl, keine Schwelle, keine Erwartung aus §8 bewegt; kein Re-Run.**

Rev. 5: 01.09.2026 (Auftrag Z1-A) — Amendment nach dem Freeze, **eine Stelle, kein
Kennzahlenteil berührt**. §7.2 **Nachtrag**: der **SHA256 des Auswertungsskripts**
`tools/evaluate_z1.py` — `669a0a648598cb7fcf2d33d1491c89d46cd486fd13d08258f0e2ccc9672b8e06`
— und der seines Zählwerkzeugs `tools/z1_tokenizer.py` —
`b1d1f6c466e0a517ab6b27c5a118cf77872b6d0dd0e493e24ff78fc580b7c534` — sind registriert.
Damit ist die **Auflage aus §7.2** erfüllt („sein SHA256 wird als Amendment (§10) in dieses
Protokoll aufgenommen"), die seit Z1-R als Restposten offenstand. **Reiner Hash-Nachzug —
und genau deshalb eine eigene Revision** (§0.1: „auch ein reiner Hash-Nachzug"). Kein
Kennzahlenteil, keine Schwelle, keine Erwartung bewegt; kein Re-Run.

Rev. 4: 31.08.2026 (Auftrag Z1-A) — Amendment nach dem Freeze, **zwei Stellen, kein
Kennzahlenteil berührt**. **(a)** §5.4 **Klarstellung**: „nicht erhoben" deckt **zwei**
verschiedene Sachlagen — **keine Antwort** (Transportfehler, Zeitüberschreitung,
Lieferausfall) und **Antwort erhalten, durchgängig ungültig**. Beide werden **getrennt**
berichtet, je Bedingung mit Gültigkeit, Zähler und Ursache. Das ist die Präzisierung einer
**bestehenden** Regel und **keine neue Metrik**: §5.4 verlangte schon bisher „die Zeile
trägt ‚nicht erhoben' und den Grund" — der Satz sagt nun, dass der **Grund** die beiden
Fälle scheidet. **(b)** §3.3 **(7) neu**: der **Ollama-Digest** wird als Messeingang
registriert, für **künftige** Läufe. Anlass ist eine Lücke, nicht ein Fehler: `model_version`
trägt nur den beweglichen Tag, und für die Juni-Serie ist die Modellidentität deshalb
nicht mehr entscheidbar. Registriert wird **kein** Wert rückwirkend. **Keine Kennzahl, keine
Schwelle, keine Erwartung aus §8 bewegt; kein Re-Run.**

Rev. 3: 31.08.2026 (Auftrag Z1-T) — Amendment nach dem Freeze, **vier Stellen, kein
Kennzahlenteil berührt**. Anlass ist ein **Lieferausfall**, nachgewiesen in Z1-T Phase 1: der
gerenderte Prompt (Blob-Rendering `cb2fcefd…`, 18 842 B) zählt unter dem Tokenizer von
`qwen2.5-coder:7b` **4 281 Token**, der Ollama-Server lud aber mit dem Vorgabefenster
**4096** und liess davon **2 050 Token** herein — genau der Wert, den alle sechs K2-Läufe
vom 31.08.2026 in `usage.prompt_tokens` tragen. Die Bedingung K2 ist damit **nicht
gemessen**, nicht schlecht gemessen. Registriert werden deshalb: **(a)** §3.3 (6) das
**Kontextfenster des Ollama-Servers als expliziter Laufparameter**
(`OLLAMA_CONTEXT_LENGTH=16384`, am Server gesetzt, nicht über ein abgeleitetes Modell);
**(b)** §5.3 die **Lieferzusicherung P3** — P1 und P2 sichern die Antwort, P3 sichert die
**Lieferung**; **(c)** §5.4 die **Rücksetzung des Wiederholungsbudgets für K2** (für K3
bleibt es erschöpft); **(d)** §6.4 die **Archivpfade** — der Altblock wandert unverändert
nach `data/z1/k2_trunkiert/`, die Neuläufe belegen ein frisches `data/z1/k2/`. Kein
Eingriff am Extractor, am Prompt, am Schema oder an `tools/run_z1.py`; keine Kennzahl,
keine Schwelle, keine Erwartung aus §8 bewegt.

Rev. 2: 31.08.2026 (Auftrag Z1-R) — Amendment nach dem Freeze, **beide Punkte in §8 E8**.
(a) Klargestellt, dass der `adjusted_rand_index` in E8 die **Entscheidungsregel** der
Erwartung ist und **keine berichtete Kennzahl**: er erscheint nicht in der Ergebnistabelle
§7.1, sondern nur im Verdikt zu E8; §4 („was der Code nicht rechnet, wird nicht
registriert") regelt die **berichteten Kennzahlen**, E8 eine **Prüfregel**, und beide lesen
damit nicht gegeneinander. (b) **Auflage:** die Partitionsabbildung Modul→Komponente wird
gegen Fixtures **handgerechnet** geprüft, bevor der ARI ein Verdikt trägt — mindestens eine
identische Partition (ARI 1.0), eine verschobene (< 1.0) und die Triton-Reduktion gegen
sich selbst; die Prüfung liegt in **Z1-A**, nicht im Laufauftrag. Ausserdem die
Freeze-Aussage in der `Stand:`-Zeile nachgezogen (der Alttext trug noch „Freeze steht
aus"). Kein Messteil berührt, kein Re-Run.

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

**(6) Kontextfenster des Ollama-Servers — expliziter Laufparameter für K2.**
*(Nachtrag Rev. 3, 31.08.2026, Auftrag Z1-T. Der Text von (1)–(5) bleibt unberührt.)*

**Der Messbefund zuerst.** Der gerenderte Prompt der Bedingung K2 — das Rendering des
registrierten Prompt-Blobs `6c8e4639…` über die Faktenbasis `fixtures/rich_repo`, archiviert
als `attempts/attempt_0/prompt.txt`, SHA256 `cb2fcefddbbb…0ee2d`, 18 842 B — zählt unter dem
Tokenizer von `qwen2.5-coder:7b` **4 281 Token** (mit Chat-Template; ohne Template 4 274).
Der Ollama-Server lud das Modell am 31.08.2026 mit dem Vorgabefenster **4096** und liess
davon **2 050 Token** herein. Beide Zahlen sind an diesem Rechner nachgemessen und in
`z1_t_bericht_kontextfenster.md` §1 mit Rohausgabe belegt; 2 050 ist zugleich der Wert, den
**alle sechs K2-Läufe vom 31.08.2026** in `usage.prompt_tokens` des ersten Versuchs tragen.

**Warum das hierher gehört und nicht in den Laufrecord.** Der Extractor sendet **keine**
Ollama-Optionen: `openai_compatible.py` baut den Request aus `messages`, `temperature`,
`seed` und `response_format` und kennt weder `options` noch `extra_body` (§3.3 (1), (3)).
Das Kontextfenster ist damit **keine Eigenschaft des Calls**, sondern eine des Servers —
dieselbe Lage wie bei `seed` und `temperature`: ein Wert, der in jeden Lauf eingeht und im
Record nicht steht. Er wird deshalb hier registriert.

**Registrierter Wert: `OLLAMA_CONTEXT_LENGTH=16384`**, gesetzt am **Ollama-Server**
(systemd-Drop-in zu `ollama.service`, Neustart des Dienstes), **vor** dem Lauf festgelegt
und danach nicht mehr bewegt. Begründung der Höhe, aus gemessenen Grössen:

| Grösse | Wert | Quelle |
|---|---|---|
| Prompt des ersten Versuchs | 4 281 Token | Messung Z1-T §1 |
| längster archivierter Versuchsprompt (`attempt_2`, gewachsene Retry-Konversation) | 6 010 Token | Messung Z1-T §1 |
| beobachtete Ausgabelänge je Versuch | ≤ 781 Token | `meta.json` der sechs Altläufe |
| Modellgrenze | 32 768 | `ollama show qwen2.5-coder:7b` |

16 384 fasst den längsten bekannten Versuchsprompt mit **rund 2,4-fachem** Abstand und
lässt Raum für eine unter voller Lieferung längere Antwort. **Nicht 32 768:** in dieser
Grösse rutscht die Instanz auf diesem Rechner aus dem Grafikspeicher (gemessen: `ollama ps`
meldet bei 32 768 `8%/92% CPU/GPU` und 6,8 GB auf einer RTX 3070 Ti mit 8 GB, bei 16 384
dagegen `100% GPU` und 5,5 GB) — das Rechensubstrat der Bedingung würde mitten im
Experiment wechseln. **Nicht 8 192:** es fasst den längsten Versuchsprompt nur mit rund
1,4-fachem Abstand.

**Am Server, nicht über ein abgeleitetes Modell.** Ein `Modelfile` mit `PARAMETER num_ctx`
erzeugte ein Modell mit **anderem Namen und anderem Digest** — eine andere Modellidentität
mitten in der Vergleichskette. Der Modellname `qwen2.5-coder:7b` und der Digest
`dae161e27b0e` bleiben unverändert.

**Vorbedingung mit Abbruch (ergänzt §6.1).** Vor jeder Invocation der Bedingung K2 wird das
**tatsächlich geladene** Fenster gemessen — `ollama ps`, Spalte `CONTEXT`, Rohausgabe ins
Laufmanifest — und muss **16384** lauten. Weicht es ab, wird der Lauf **nicht gestartet**.
Die Spalte trägt nur eine residente Instanz; ist keine geladen, wird die Messung nach dem
ersten Call wiederholt (Methode aus C5 Schritt 3b).

**Ungeschminkt, damit die Reichweite nicht überschätzt wird.** Auch die Juni-Läufe haben den
Prompt **nicht vollständig** erhalten: sie melden 4 095 Token, also 4096 − 1, gegen 4 281
erwartete. Der Neulauf stellt damit **nicht den Juni-Zustand her**, sondern liefert die
registrierte Bedingung **zum ersten Mal vollständig**. Jeder Vergleich mit den Juni-Läufen
hat das zu tragen. Für K3 stellt sich die Frage nicht: der DigitalOcean-Endpunkt meldet in
allen sechs Läufen `prompt_tokens: 4455` im ersten Versuch und über die Versuche **steigende**
Werte (bis 5 883) — dieselbe Zahl, die OpenRouter im Juni für denselben Prompt meldete.

**(7) Der Ollama-Digest — Modellidentität, ab jetzt bezeugt.**
*(Nachtrag Rev. 4, 31.08.2026, Auftrag Z1-A. Der Text von (1)–(6) bleibt unberührt. Diese
Registrierung gilt für **künftige** Läufe; rückwirkend wird kein Wert eingetragen.)*

**Die Lücke zuerst.** `run_logger.py` schreibt `model` und `model_version`; beide tragen
für die Bedingung K2 zeichengleich den **Tag** `qwen2.5-coder:7b`. Ein Tag ist beweglich:
`ollama pull` derselben Zeichenkette kann jederzeit auf ein anderes Manifest zeigen. Der
Record enthält **keinen** Digest. Für die Juni-Serie ist die Modellidentität deshalb
**nicht mehr entscheidbar** — es gibt kein Artefakt, aus dem hervorginge, welche Gewichte
damals liefen. Das ist die **dritte Instanz derselben Klasse** in dieser Arbeit
(`repo_commit` als Nicht-Anker, §0.2 (b) und T-Z1-10; T14 im Z3-Protokoll; der bewegliche
Tag ohne Digest hier): **ein Bezeichner, der wie ein Anker aussieht und keiner ist.**

**Registriert wird, was heute messbar ist**, aus dem lokalen Modellspeicher, ohne
Modell-Call:

| Gegenstand | Wert | Herkunft |
|---|---|---|
| Manifest-Digest (die von `ollama ps` / `ollama list` gezeigte ID) | `dae161e27b0e90dd1856c8bb3209201fd6736d8eb66298e75ed87571486f4364` | SHA256 von `manifests/registry.ollama.ai/library/qwen2.5-coder/7b` |
| Kurzform, wie im Werkzeug sichtbar | `dae161e27b0e` | ebenda, erste 12 Hexstellen |
| Digest der Modellschicht (GGUF) | `sha256:60e05f2100071479f596b964f89f510f057ce397ea22f2833a0cfe029bfc2463` | `layers[]`, `mediaType` `…image.model`, 4 683 074 048 B |
| Quantisierung / Architektur | `Q4_K_M` / `qwen2`, `context length` 32768 | GGUF-Metadatenblock |

**Auflage für künftige Läufe.** Vor jeder Invocation gegen einen **lokal bedienten**
Endpunkt wird der Manifest-Digest erhoben und **ins Laufmanifest** geschrieben — dorthin,
wo schon Prompt-Blob, Schema-Hash und die drei Laufzeitversionen stehen (§6.3), und nicht
in den Extractor: der Extractor wird dafür **nicht** angefasst. Weicht der Digest von dem
oben registrierten ab, ist das **kein Abbruch**, sondern eine **Meldepflicht**: der Lauf
wird gefahren und die Abweichung berichtet. Ein Abbruch wäre hier unangemessen, weil der
Digest bis heute **nie** bezeugt war — eine Schwelle gegen einen unbekannten Ausgangswert
wäre keine Zusicherung, sondern eine Behauptung.

**Für K3 gilt die Auflage nicht, und das ist der Punkt.** Der DigitalOcean-Endpunkt
bedient das Modell fremd; es gibt dort **keinen** Digest zu lesen, `system_fingerprint` ist
`null`, und die Identität der Gewichte ist nicht verifizierbar (T-Z1-5). Aufzuzeichnen ist
dort, was es gibt: das `model`-Echo und das leere `system_fingerprint` — **als Beleg der
Lücke**, nicht als Anker. Der Unterschied zwischen einer schliessbaren und einer nicht
schliessbaren Lücke wird damit im Protokoll sichtbar, statt in beiden Fällen gleich zu
schweigen.

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

**Nachtrag Rev. 3 (31.08.2026, Auftrag Z1-T) — (P3) Lieferzusicherung.** *Der Text zu P1 und
P2 bleibt unberührt; P3 tritt daneben.*

**Warum eine dritte Zusicherung.** P1 und P2 sichern die **Antwort**: sie stellen die
Rohantwort gegen das geparste Modell und fangen, was zwischen Draht und Modell still
verschwindet. Keine von beiden sieht, ob das Modell die **Frage** überhaupt vollständig
bekommen hat. Genau dieser Fall ist am 31.08.2026 eingetreten: von 4 281 Token des
gerenderten Prompts kamen 2 050 an, der Rest wurde vom Server verworfen — **ohne Fehler,
ohne Logzeile, ohne HTTP-Status ungleich 200** (§3.3 (6); dieselbe Fehlerklasse wie die
stille Null oben, nur eine Stufe früher). P1 und P2 liefen dabei sauber durch: die Antwort
war formal in Ordnung, sie war nur die Antwort auf einen halben Prompt. **P1 und P2 sichern
die Antwort, P3 sichert die Lieferung.**

| | Prüfung | Zeitpunkt | Abbruch bei |
|---|---|---|---|
| **(P3a)** | **Liefersonde, kalt**: die Modellinstanz wird entladen (`ollama stop <modell>`), dann geht der **registrierte gerenderte Prompt** — Systemtext und Nutzertext aus dem Blob-Rendering `cb2fcefd…` — über **denselben Endpunkt** wie der Messlauf (`/v1/chat/completions`, `max_tokens: 1`) hinaus; gelesen wird `usage.prompt_tokens` | **vor** der Invocation | Wert ausserhalb **4 260 – 4 302** |
| **(P3b)** | **Fensterzeuge**: `ollama ps`, Spalte `CONTEXT`, Rohausgabe, vor und nach der Invocation | vor und nach | Wert ≠ **16384** |
| **(P3c)** | **Bytezeuge**: SHA256 von `attempts/attempt_0/prompt.txt` jedes archivierten Laufs | nach dem Lauf | ≠ `cb2fcefddbbb1f2e81c62bc4b4231b458d12bfcc0948d3764dad7f287db0ee2d` |

**Der Referenzwert und seine Toleranz.** Referenz ist **4 281 Token**, gemessen am
31.08.2026 in dieser Umgebung gegen das Blob-Rendering (Chat-Template; roh 4 274). Prompt
und Modell sind bytefest — der Erwartungswert ist deshalb **exakt**, nicht geschätzt. Die
Toleranz von **± 0,5 % (± 21 Token)** deckt allein eine Änderung des Chat-Templates bei
einem Neuzug des Modells ab; sie ist **beidseitig**: eine Überschreitung hiesse, dass nicht
der registrierte Prompt gesendet wurde, eine Unterschreitung, dass er nicht vollständig
angekommen ist. Beides bricht ab.

**Warum P3 NICHT je Versuch auf `prompt_tokens` gerechnet wird — und was das kostet.**
Ollama meldet in `prompt_tokens` den `prompt_eval_count`, also die **neu ausgewerteten**
Token; ein im KV-Cache liegendes Präfix wird nicht mitgezählt. Gemessen an den eigenen
Artefakten: die sechs Läufe vom 31.08. melden für `attempt_1` **1 065** Token, obwohl dessen
Konversation länger ist als die von `attempt_0` (2 050); die Juni-Läufe melden nach 4 095
ein `attempt_1` von 884. Eine Untergrenze je Versuch erzeugte damit **Fehlabbrüche auf
zwischengespeicherten Präfixen**. P3 sitzt deshalb auf der **kalten Sonde** (P3a) und dem
**Fenster** (P3b): ist das Fenster 16 384 und der längste Versuchsprompt 6 010 Token, kann
keine Kürzung mehr stattfinden — die Sonde belegt es empirisch, der Fensterzeuge strukturell.
Die Werte je Versuch werden weiterhin **aufgezeichnet und berichtet** (§6.3), tragen aber
keine Zusicherung. Das ist die Grenze dieser Zusicherung, und sie steht hier, statt
weggelassen zu werden.

**Wo P3 ausgeführt wird.** In `tools/check_z1_delivery.py` — **ausschliesslich lesend** über
die Artefakte und über die beiden genannten Sonden, ohne Extractor-Aufruf. `tools/run_z1.py`
bleibt **unverändert**; P3 greift wie P1 und P2 **an der Artefaktgrenze**, nicht im Treiber
und nicht im Extractor. Ein Lauf, dessen P3 fällt, wird nach §5.4 behandelt: archiviert,
journalisiert, mit Abbruchgrund, Wiederholung im Rahmen des Budgets.

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

**Nachtrag Rev. 3 (31.08.2026, Auftrag Z1-T) — Rücksetzung des Budgets für K2, einmalig und
begründet.** *Die Regeln oben bleiben unberührt.*

**Der Sachverhalt.** Für K2 sind am 31.08.2026 sechs Läufe gefahren worden — drei aus der
Erstinvocation und drei Wiederholungen —, und mit ihnen ist das Budget dieses Abschnitts
erschöpft; die Bedingung steht seither als **NICHT ERHOBEN**. Die sechs Läufe haben den
registrierten Messeingang **nicht erhalten**: 2 050 von 4 281 Token, der Server hat den
Prompt vorn abgeschnitten, ohne Fehler und ohne Logzeile (§3.3 (6)). Damit ist die Bedingung
K2 **nicht gemessen** — nicht schlecht gemessen, nicht ungültig gemessen, sondern gar nicht.
Die drei Wiederholungen sind auf einer Bedingung verbraucht worden, **die nicht zustande
gekommen ist**.

**Festgelegt.** Das Budget dieses Abschnitts wird für **K2** auf drei Wiederholungen
**zurückgesetzt**. Die sechs Altläufe zählen **nicht** gegen das neue Budget. Sie bleiben
vollständig im Bestand — archiviert, gehasht, journalisiert — als **Beleg des
Lieferausfalls**; gelöscht oder überschrieben wird nichts (§6.4).

**Für K3 bleibt das Budget erschöpft.** K3 hat den vollständigen Prompt erhalten
(`prompt_tokens: 4455` im ersten Versuch aller sechs Läufe, über die Versuche steigend);
sein Ausfall ist Modellverhalten und keine Lieferstörung. Über K3 wird **getrennt**
entschieden; dieser Nachtrag ändert an der Bedingung K3 nichts.

**Die Regel, damit die Rücksetzung nicht zum Muster wird.** Ein Wiederholungsbudget darf
**nur** zurückgesetzt werden, wenn eine **vorregistrierte Lieferzusicherung** (§5.3 P3)
gefallen ist oder — wie hier, vor deren Registrierung — der Lieferausfall nachträglich mit
Zahlen belegt wird. Ein Budget wird **nie** zurückgesetzt, weil ein Ergebnis missfällt. Der
Unterschied ist prüfbar und nicht Ermessenssache: im ersten Fall ist der **Messeingang** ein
anderer als der registrierte, im zweiten die **Antwort** eine andere als die erhoffte.

**Nachtrag Rev. 4 (31.08.2026, Auftrag Z1-A) — „nicht erhoben" deckt zwei Sachlagen, und
sie werden getrennt berichtet.** *Die Regeln oben bleiben unberührt; dies ist die
Präzisierung einer bestehenden Regel, keine neue Metrik und keine neue Kennzahl.*

Der Abschnitt oben sagt: nach erschöpftem Budget trägt die Zeile „nicht erhoben" **und den
Grund**. Er sagt **nicht**, dass der Grund von zwei sehr verschiedenen Sachlagen erzählen
kann — und genau die sind in Z1 beide eingetreten:

| Fall | Sachlage | Was fehlt | Beleg in Z1 |
|---|---|---|---|
| **(i)** | **keine Antwort auf die registrierte Frage** — Transportfehler, Zeitüberschreitung, oder **Lieferausfall**: der Messeingang ist gar nicht angekommen | der **Eingang** | `data/z1/k2_trunkiert/`: 2 050 von 4 281 Token (§3.3 (6)) |
| **(ii)** | **Antwort erhalten, durchgängig ungültig** — der registrierte Eingang ist vollständig geliefert, das Modell hat geantwortet, und keine Antwort besteht §5.2 | die **Gültigkeit** | `data/z1/k2/` und `data/z1/k3/` |

**Beide Fälle stehen unter derselben Berichtsform** — „nicht erhoben", nie 0, nie ein
Strich —, aber sie sagen Verschiedenes: **(i)** ist ein Befund über das **Instrument**,
**(ii)** einer über das **Modell**. Eine Auswertung, die sie zusammenzieht, schriebe einen
Serverfehler dem Modell zu (oder umgekehrt) und wäre genau die Vermischung, die §5.4 mit
dem Wort „Grund" von Anfang an verhindern wollte.

**Festgelegt:** je Bedingung werden **Gültigkeit, Zähler und Ursache** berichtet, und die
Ursache benennt den Fall (i) oder (ii). Ein Block des Falls (i) wird **nicht als
Modellbefund geführt** und trägt in keiner Aussage über Modellverhalten Gewicht. Der
Unterschied ist prüfbar und nicht Ermessenssache — dieselbe Trennlinie, die schon die
Budgetregel oben zieht: im Fall (i) ist der **Messeingang** ein anderer als der
registrierte, im Fall (ii) die **Antwort** eine andere als die erhoffte.

**Was hier ausdrücklich NICHT eingeführt wird:** keine Kennzahl, kein Zähler, keine
Schwelle, keine Aggregation. §4 bleibt zeichengleich; die Ergebnistabelle §7.1 bekommt
keine Spalte. Bewegt wird allein die **Berichtsform** der nicht erhobenen Zeile.

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

**Nachtrag Rev. 3 (31.08.2026, Auftrag Z1-T) — zwei Vorbedingungen kommen hinzu, nur für
K2.** *Die Tabelle oben bleibt unberührt und gilt weiter.*

| Vorbedingung | Soll | Quelle |
|---|---|---|
| `ollama ps`, Spalte `CONTEXT`, Rohausgabe ins Laufmanifest | **16384** | §3.3 (6), §5.3 P3b |
| Liefersonde auf kalter Instanz, `usage.prompt_tokens` | **4 260 – 4 302** (Referenz 4 281) | §5.3 P3a |

Beide sind **Abbruchbedingungen, keine Warnungen**: weicht eine ab, wird der Lauf nicht
gestartet. Sie gelten für die Bedingung **K2**; K3 spricht einen anderen Endpunkt an, dessen
Fenster nicht in dieser Hand liegt und dessen Lieferung über `prompt_tokens: 4455` bezeugt
ist (§3.3 (6)).

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

**Nachtrag Rev. 3 (31.08.2026, Auftrag Z1-T) — zwei K2-Blöcke, zwei Lieferregime.**

| Block | Inhalt | Kontextfenster | Stand |
|---|---|---|---|
| `data/z1/k2_trunkiert/` | die **sechs Altläufe** vom 31.08.2026, unverändert | **4096**, geliefert 2 050 von 4 281 Token | abgeschlossen, `NICHT ERHOBEN` |
| `data/z1/k2/` | die **Neuläufe** nach diesem Amendment, `run0`/`run1`/`run2` | **16384**, vollständige Lieferung | ab Z1-T Phase 3 |
| `data/z1/k3/` | unberührt | — | abgeschlossen, `NICHT ERHOBEN` |

**Der Altblock wandert, er ändert sich nicht.** `data/z1/k2/` wird als Ganzes nach
`data/z1/k2_trunkiert/` umbenannt; die Dateien sind **byte-identisch**, das mitwandernde
`SHA256SUMS` führt relative Pfade und bleibt im neuen Verzeichnis gültig (`sha256sum -c`
Exit 0). Verweise auf `data/z1/k2/…` in `z1_r_bericht_laeufe.md` und
`z1_d_bericht_formausfall.md` meinen den **Altblock** und werden dort als überholt
gekennzeichnet, nicht ersetzt.

**Warum nicht in den bestehenden Block hinein.** `tools/run_z1.py` leitet den Zielpfad aus
dem Bedingungsschlüssel ab und vergibt bei belegten Plätzen die Namen `run0_w4`, `run1_w1`,
`run2_w1` (`free_slot`). Die Neuläufe hiessen dann **„Wiederholungen"** — und zwar
ausgerechnet die Wiederholungen eines gerade zurückgesetzten Budgets (§5.4) — und zwei
Lieferregime lägen in **einem** Block nebeneinander. Genau diese Mehrdeutigkeit schliesst
§6.2 unter Verweis auf Befund 04 aus. Die Trennung in zwei Blöcke ist die Alternative, die
**ohne Änderung am Treiber** auskommt: `tools/run_z1.py` bleibt bytegleich.

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

**Nachtrag Rev. 5 (01.09.2026, Auftrag Z1-A) — die Auflage ist erfüllt, die Hashes stehen
hier.** *Der Text der Auflage oben bleibt unberührt.*

| Werkzeug | SHA256 | Rolle |
|---|---|---|
| `tools/evaluate_z1.py` | `669a0a648598cb7fcf2d33d1491c89d46cd486fd13d08258f0e2ccc9672b8e06` | die Auswertung: Ansatz 1 gerechnet, Ansatz 2 als *nicht erhoben* berichtet, zwei Ausgaben (JSON und Markdown nach §7.1) |
| `tools/z1_tokenizer.py` | `b1d1f6c466e0a517ab6b27c5a118cf77872b6d0dd0e493e24ff78fc580b7c534` | der Zähler für die Kontextfenster-**Extrapolation**; **keine Kennzahl**, kein Teil von §4 |

**Was das Skript nicht tut, und warum das die Registrierung trägt.** Es importiert
`llm_arch.eval.metrics` und `llm_arch.ilograph.validate` **unverändert** aus dem Extractor
am registrierten `HEAD` und **rechnet selbst keine Kennzahl** — es liest, ruft auf und
stellt zusammen. Die Kompressionsgrössen kommen nach dem Weg (ii) dieses Abschnitts
**direkt aus `meta.json`**; `scripts/compare_runs.py` bleibt byteidentisch
(`c6db316b…`) und wird als Gegenprobe **ausgeführt**, für genau seine zwei Aggregate.
Ein **Fixture-Test** liegt bei (`--selftest` gegen `tests/fixtures/z1/`): der Abbruch nach
§5.2 muss auf `fehlendes_valid_final/` anschlagen, und Ansatz 1 muss E1/E2 zeichengleich
treffen.

**`z1_tokenizer.py` ist ausdrücklich KEIN Messinstrument nach §4.** Er zählt Token für eine
**Extrapolation**, die als solche gekennzeichnet ist und in keiner Zelle von §7.1 erscheint.
Registriert ist er trotzdem — aus derselben Lehre, aus der §3.3 (7) entstand: ein Werkzeug,
das eine Zahl in einen Bericht trägt, gehört bezeugt, auch wenn die Zahl keine Kennzahl ist.

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

> **Nachtrag 31.08.2026 (Z1-R, Rev. 2) — der ARI in E8 ist die Entscheidungsregel, keine
> berichtete Kennzahl.** Der Alttext oben bleibt zeichengleich stehen; die folgenden zwei
> Absätze präzisieren ihn, ohne eine Zahl, eine Schwelle oder eine Falsifikationsbedingung
> zu verschieben.
>
> **(a) Verhältnis zu §4.** Der `adjusted_rand_index` zwischen der Modul→Komponente-Abbildung
> eines Laufs und der Reduktion des Triton-Exports **erscheint nicht in der Ergebnistabelle
> von §7.1**. Er erscheint **ausschliesslich im Verdikt zu E8** — als die Regel, die
> „schichtenorientiert" von „nicht schichtenorientiert" trennt. Damit ist §4 („Was der Code
> nicht rechnet, wird nicht registriert") **nicht verletzt: §4 regelt die berichteten
> Kennzahlen, E8 eine Prüfregel.** Ohne diesen Satz lesen §4 und §8 gegeneinander — §4
> schlösse eine Grösse aus, die §8 gebraucht.
>
> **Nicht zu verwechseln mit `gold_similarity` (§4.4).** Das ist eine **berichtete**
> Kennzahl, sie steht in der Tabelle §7.1, und sie rechnet den ARI gegen
> `fixtures/rich_repo.gold.json`. Die Regel in E8 rechnet gegen die **Triton-Reduktion**.
> Dieselbe Funktion (`metrics.py:179-216`), zwei verschiedene Bezugspartitionen, zwei
> verschiedene Rollen: die eine wird **berichtet**, die andere **entscheidet**. Wo beide
> nebeneinander stehen, sind sie als solche zu benennen.
>
> **(b) Auflage: der ARI wird handgerechnet geprüft, bevor er ein Verdikt trägt.** Die
> Partitionsabbildung Modul→Komponente ist die Stelle, an der sich Fehler verstecken — die
> Präzedenz ist der **K4/K5-Join in Z3**, wo ein Nullergebnis wie ein Befund aussah (Befund
> 08; dieselbe Fehlerklasse wie die stille Null aus §5.3: eine Fehlkonfiguration, die ein
> plausibles Ergebnis erzeugt, ohne zu scheitern). **Festgelegt:** vor der ersten Anwendung
> auf einen Z1-Lauf wird der ARI gegen Fixtures gerechnet, deren Wert **von Hand** bestimmt
> ist, und die Rechnung muss diesen Wert treffen. Mindestens drei Fälle:
>
> | Fall | Soll |
> |---|---|
> | zwei **identische** Partitionen | ARI **1.0** |
> | eine **verschobene** Partition (mindestens ein Modul in einer anderen Komponente) | ARI **< 1.0** |
> | die **Triton-Reduktion gegen sich selbst** | ARI **1.0** |
>
> **Die Prüfung liegt in Z1-A** (dem Auswertungsauftrag), **nicht** im Laufauftrag: der Lauf
> erhebt, die Auswertung verdikt. Trägt der ARI ein E8-Verdikt, ohne dass diese Prüfung
> gefahren und berichtet ist, ist das Verdikt **nicht zu stellen**.

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

> **Amendment (01.09.2026, Rev. 6) — NEUER THREAT T-Z1-11. Begründung:**
> `z1_s_bericht_diagnoselauf.md` §6–§8; Archiv `data/z1_s_diagnose/` (51 Dateien,
> `sha256sum -c` Exit 0); Befund 07.3, Nachtrag vom 01.09.2026. T-Z1-1 bis T-Z1-10 bleiben
> **unverändert stehen**.
>
> **T-Z1-11 — Die Ausführungsgeometrie des Inferenzservers bewegt die Ausgabe und ist in
> keinem Laufrecord bezeugt.** Gemeint sind drei Grössen, die der Server beim Laden des
> Modells festlegt: **`n_ctx`** (`-c`), die daraus **abgeleitete Batchgrösse** (`-b`/`-ub`)
> und die **KV-Cache-Geometrie**.
>
> **Belegt, nicht vermutet.** Zwei Diagnoseläufe auf **derselben Maschine**, derselben
> Ollama-Fassung **0.30.10**, demselben Modell-Blob `sha256:60e05f21…bfc2463`, demselben
> Chat-Template (`chatml`, `--no-jinja`) und mit **token-für-token demselben Erstprompt**
> (4 095 IDs, geprüft als `probe_ids == ids[:4] + ids[190:]`) haben **verschieden
> geantwortet** — **1 517 gegen 2 261 Zeichen** —, bei `temperature=0` und `seed=0`
> (§3.3 (1)). Der eine Lauf war `valid_final = true` mit **0** Fehlern und 8 von 8
> auflösbaren Relationsendpunkten, der andere `valid_final = false` mit **14** Fehlern der
> Klasse `relation`, in allen drei Versuchen unbewegt. Verändert war **allein `-c 4096`
> gegen `-c 16384`** und was der Server daraus ableitet: `-b`/`-ub` **512 gegen 1024**,
> KV-Cache **224 gegen 896 MiB**. `--flash-attn`, `--context-shift --keep 4`, Rechensubstrat,
> Maschine und Stunde waren gleich.
>
> **Was daraus für dieses Protokoll folgt.** §3.3 (6) registriert seit Rev. 3 den
> **Fensterwert** (`OLLAMA_CONTEXT_LENGTH=16384`), und §6.1 prüft ihn je Lauf mit Abbruch;
> die **übrigen Grössen der Geometrie** waren bisher weder registriert noch aufgezeichnet.
> **Registriert wird hiermit: künftige Läufe führen die Ausführungsgeometrie des Servers im
> Laufrecord** — Serverversion und die Startparameter des Inferenzprozesses (`-c`, `-b`,
> `-ub`, KV-Cache-Typ und -Grösse, `--flash-attn`, `--context-shift`/`--keep`,
> Chat-Template), **am laufenden Prozess erhoben**, nicht angenommen. **Rev. 4** registrierte
> den **Modell**-Digest (§3.3 (7)); dies ist die **zweite Hälfte derselben Lücke**: derselbe
> Blob unter anderer Geometrie ist nicht derselbe Messstand. Vierte Instanz der Klasse
> „registrierter Anker, der den Messstand nicht trägt" — nach `repo_commit` (§0.2 (b),
> T-Z1-10), `model_version` (Rev. 4) und T14 im Z3-Protokoll.
>
> **Reichweite, offen benannt — der Threat behauptet nicht mehr, als er trägt.**
>
> - **(a)** **Welche** der drei gebündelten Grössen trägt, ist **nicht entschieden**: der
>   Server leitet Batchgrösse und Cache-Geometrie aus `n_ctx` ab. Ein Lauf, der `-c` gegen
>   `-b`/`-ub` trennt, ist **nicht gefahren** und ist **Future Work**.
> - **(b)** Der Nachweis stammt aus **Diagnoseläufen ausserhalb dieses Protokolls**, auf
>   einer **anderen Maschine** als der Messrechner. Er trägt **diesen Threat**, **keine
>   Z1-Kennzahl**; keine Zahl aus `data/z1_s_diagnose/` geht in §7.1 oder in ein Verdikt zu
>   §8 ein.
> - **(c)** Die Läufe unter `data/z1/k2/` sind dadurch **nicht entwertet**: ihr Fenster ist
>   nach §3.3 (6) und §6.1 vor **und** nach jedem Lauf bezeugt (P3b), und die Lieferung ist
>   über P3a/P3c gesichert. **Unbezeugt sind die übrigen Geometriegrössen** — genau die
>   Lücke, die diese Registrierung für **künftige** Läufe schliesst. **Kein Wert wird
>   rückwirkend registriert und kein vorhandener Lauf nachgetragen.**
>
> **Mitigation** ist deshalb keine Nachbesserung am Bestand, sondern die
> **Aufzeichnungspflicht ab hier**. Für den vorhandenen Bestand bleibt der Threat als
> **Reproduzierbarkeitsgrenze** stehen: eine Wiederholung auf einer **anders konfigurierten
> Serverinstanz** ist nicht als dieselbe Bedingung zu lesen, auch bei gleichen Gewichten,
> gleicher Binärversion und gleichem Prompt.
>
> **Keine Kennzahl, keine Schwelle, keine Erwartung aus §8 ist bewegt; §4, §7 und §8 stehen
> zeichengleich. Kein Re-Run.**

---

## 10. Amendments

**Revisionshistorie vor Freeze** (Änderungen am Entwurf, solange keine Messung läuft):

| Rev | Datum | Änderung | Begründung |
|---|---|---|---|
| — | — | *(keine)* | — |

**Amendments nach Freeze** (datiert, mit Begründung; geführt zugleich in der
Revisionshistorie im Kopf):

| Rev | Datum | Änderung | Begründung | Re-Run |
|---|---|---|---|---|
| 6 | 01.09.2026 | **Eine Stelle, kein Kennzahlenteil.** §9 **T-Z1-11 neu**: die **Ausführungsgeometrie des Inferenzservers** — `n_ctx` (`-c`), die daraus **abgeleitete Batchgrösse** (`-b`/`-ub`) und die **KV-Cache-Geometrie** — ist ein **bezeugungspflichtiger Umgebungsparameter**. Registriert wird, dass **künftige** Läufe diese Grössen samt Serverversion und Startparametern (`-c`, `-b`, `-ub`, KV-Cache-Typ und -Grösse, `--flash-attn`, `--context-shift`/`--keep`, Chat-Template) im **Laufrecord** führen, **am laufenden Prozess erhoben**. Ausdrücklich **kein** Wert rückwirkend, **keine** Aufzeichnungspflicht für den vorhandenen Bestand, **keine** Entwertung von `data/z1/k2/` — dessen Fenster ist über §3.3 (6)/§6.1 und P3b bezeugt, unbezeugt sind die **übrigen** Geometriegrössen. Als Reichweitengrenzen mitregistriert: die drei Grössen sind **gebündelt** und nicht getrennt, und der Nachweis stammt aus Diagnoseläufen **ausserhalb** dieses Protokolls auf einer **anderen Maschine** | **Belegt aus einer Messung, nicht vermutet** (Z1-S/Z1-S2, `z1_s_bericht_diagnoselauf.md` §6–§8, Archiv `data/z1_s_diagnose/`): identische Eingabe (token-für-token derselbe Erstprompt, 4 095 IDs), identisches Modell, identische Binärversion **0.30.10**, `temperature=0` und `seed=0` — und **verschiedene Ausgabe**, 1 517 gegen 2 261 Zeichen; der eine Lauf gültig mit 0 Fehlern, der andere ungültig mit 14 `relation`-Fehlern. Verändert war allein `-c 4096` gegen `-c 16384` samt der abgeleiteten `-b`/`-ub` 512 gegen 1024 und 224 gegen 896 MiB KV-Cache. **Rev. 4** registrierte den **Modell**-Digest (§3.3 (7)) — die Serverkonfiguration ist die zweite Hälfte derselben Lücke: derselbe Blob unter anderer Geometrie ist nicht derselbe Messstand. Vierte Instanz der Klasse „registrierter Anker, der den Messstand nicht trägt" (`repo_commit` §0.2 (b)/T-Z1-10; `model_version` Rev. 4; T14 im Z3-Protokoll). Die Registrierung kostet nichts und schliesst die Lücke für alles Künftige | **nein** — keine Kennzahl, keine Schwelle, keine Erwartung aus §8 bewegt; §4, §7 und §8 zeichengleich |
| 5 | 01.09.2026 | **Eine Stelle, kein Kennzahlenteil.** §7.2 **Nachtrag**: der **SHA256 des Auswertungsskripts** `tools/evaluate_z1.py` (`669a0a648598cb7f…`) und der seines Zählwerkzeugs `tools/z1_tokenizer.py` (`b1d1f6c466e0a517…`) sind registriert; dazu die Feststellung, dass das Skript `metrics.py` und `validate.py` **unverändert importiert** und selbst keine Kennzahl rechnet, dass `compare_runs.py` byteidentisch als Gegenprobe **ausgeführt** wird, und dass `z1_tokenizer.py` **kein** Messinstrument nach §4 ist | **Erfüllung der Auflage aus §7.2** („sein SHA256 wird als Amendment (§10) in dieses Protokoll aufgenommen"), seit Z1-R als Restposten offen. **Reiner Hash-Nachzug — und genau deshalb eine eigene Revision** (§0.1 Punkt 5, Anlass `c6b0a_bericht_invarianten.md`): der Protokoll-SHA taugt als Bewegungsdetektor nur, wenn kein Bytewechsel unregistriert bleibt | **nein** — keine Kennzahl, keine Schwelle, keine Erwartung bewegt; §4, §7.1 und §8 zeichengleich |
| 4 | 31.08.2026 | **Zwei Stellen, kein Kennzahlenteil.** **(a)** §5.4 **Nachtrag**: „nicht erhoben" deckt **zwei** Sachlagen — **(i)** keine Antwort auf die registrierte Frage (Transportfehler, Zeitüberschreitung, **Lieferausfall**) und **(ii)** Antwort erhalten, durchgängig ungültig. Beide werden **getrennt** berichtet, je Bedingung mit **Gültigkeit, Zähler und Ursache**; ein Block des Falls (i) wird **nicht als Modellbefund geführt**. **(b)** §3.3 **(7) neu**: der **Ollama-Digest** wird als Messeingang registriert (Manifest-Digest `dae161e27b0e90dd…`, Modellschicht `sha256:60e05f21…`), zu erheben ins **Laufmanifest**, nicht in den Extractor; Abweichung ist **Meldepflicht, kein Abbruch**. Für K3 gilt die Auflage nicht — dort gibt es keinen Digest zu lesen (T-Z1-5), und das ist als Lücke zu vermerken | **(a)** In Z1 sind **beide** Sachlagen eingetreten: `k2_trunkiert/` ist ein **Instrumenten**befund (2 050 von 4 281 Token), `k2/` und `k3/` sind **Modell**befunde (vollständig geliefert, durchgängig ungültig). §5.4 verlangte schon „den Grund"; ohne diese Unterscheidung liefe der Serverfehler als Modellverhalten mit — dieselbe Vermischung, die die Budgetregel desselben Abschnitts ausschliesst. **(b)** `model_version` trägt nur den **beweglichen Tag**; für die Juni-Serie ist die Modellidentität dadurch **nicht mehr entscheidbar**. Dritte Instanz derselben Klasse (`repo_commit` als Nicht-Anker §0.2 (b)/T-Z1-10; T14 im Z3-Protokoll). Die Registrierung kostet nichts und schliesst die Lücke für alles Künftige | **nein** — keine Kennzahl, keine Schwelle, keine Erwartung aus §8 bewegt; §4, §7 und §8 zeichengleich |
| 3 | 31.08.2026 | **Vier Stellen, kein Kennzahlenteil.** **(a)** §3.3 **(6) neu**: das **Kontextfenster des Ollama-Servers** wird als expliziter Umgebungsparameter registriert — `OLLAMA_CONTEXT_LENGTH=16384`, am Server gesetzt (systemd-Drop-in), nicht über ein abgeleitetes Modell, vor dem Lauf festgelegt und danach unbewegt; dazu §6.1 um zwei Vorbedingungen mit Abbruch ergänzt (`ollama ps` → `CONTEXT` 16384; kalte Liefersonde 4 260–4 302). **(b)** §5.3 **Nachtrag P3**, die **Lieferzusicherung** in drei Teilen (P3a kalte Sonde vor der Invocation, P3b Fensterzeuge vor und nach, P3c Bytezeuge des archivierten Erstprompts), ausgeführt in `tools/check_z1_delivery.py`, **lesend**; `tools/run_z1.py` bleibt bytegleich. **(c)** §5.4 **Nachtrag**: das Wiederholungsbudget für **K2** wird zurückgesetzt, für **K3** bleibt es erschöpft; dazu die Regel, dass ein Budget nur bei Lieferausfall, nie bei missfallendem Ergebnis zurückgesetzt wird. **(d)** §6.4 **Nachtrag**: der Altblock wandert unverändert nach `data/z1/k2_trunkiert/`, die Neuläufe belegen ein frisches `data/z1/k2/` | **Lieferausfall, mit Zahlen belegt** (Z1-T Phase 1): der gerenderte Prompt `cb2fcefd…` zählt **4 281 Token**, der Server lud mit dem Vorgabefenster **4096** und liess **2 050** herein — genau der Wert in `usage.prompt_tokens` aller sechs K2-Läufe vom 31.08.2026; nachgestellt an diesem Rechner mit demselben Endpunkt (2 050 bei Vorgabefenster, 4 281 bei `num_ctx` 8192/16384/32768). Die Bedingung K2 ist damit **nicht gemessen**, nicht schlecht gemessen. Das Setzen des Fensters ist **keine Prompt-Revision und kein Ergebnis-Tuning**: es stellt die in §3.1/§3.3 registrierte Bedingung her, die bisher nie vollständig geliefert wurde — auch im Juni nicht (4 095 von 4 281). P1 und P2 konnten den Fall nicht sehen: sie sichern die **Antwort**, nicht die **Lieferung** | **ja, für K2** — drei neue Läufe unter dem registrierten Fenster, in einem eigenen Block; **nein für K3** und **nein** für jede Kennzahl, Schwelle oder Erwartung: §4, §7 und §8 stehen zeichengleich |
| 2 | 31.08.2026 | **§8 E8, zwei Präzisierungen** (Nachtrag im Anschluss an E8, Alttext unberührt): **(a)** der `adjusted_rand_index` in E8 ist die **Entscheidungsregel** der Erwartung, **keine berichtete Kennzahl** — er steht nicht in der Ergebnistabelle §7.1, sondern nur im E8-Verdikt; Abgrenzung zu `gold_similarity` (§4.4), das dieselbe Funktion gegen die **Gold**-Partition rechnet und **berichtet** wird. **(b)** Auflage: der ARI wird gegen Fixtures **handgerechnet** geprüft, bevor er ein Verdikt trägt (identische Partition → 1.0, verschobene → < 1.0, Triton-Reduktion gegen sich selbst → 1.0); die Prüfung liegt in **Z1-A**. Dazu die `Stand:`-Zeile im Kopf auf den Freeze nachgezogen (Alttext gestrichen sichtbar) | **(a)** Ohne den Satz lesen **§4 und §8 gegeneinander**: §4 schliesst aus, „was der Code nicht rechnet", §8 gebraucht eine Grösse, die in keiner Ergebnistabelle steht. Die Trennung ist damit registriert statt implizit — §4 regelt die **berichteten Kennzahlen**, E8 eine **Prüfregel**. **(b)** Die Partitionsabbildung Modul→Komponente ist die Stelle, an der sich Fehler verstecken; Präzedenz ist der **K4/K5-Join in Z3**, wo ein Nullergebnis wie ein Befund aussah (Befund 08) — dieselbe Fehlerklasse wie die stille Null in §5.3 | **nein** — keine Kennzahl, keine Schwelle, keine Falsifikationsbedingung bewegt; §4, §5, §6 und §7 zeichengleich |
