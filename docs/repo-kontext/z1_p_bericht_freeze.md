# Z1-P — Bericht: Freeze des Z1-Protokolls und die Invariante (F)

**Masterarbeit Timo Haas · HTWG Konstanz**
**Datum:** 31. August 2026 · **Auftrag:** Z1-P (Z1-Protokoll schreiben und einfrieren)
**Schreibendes Repo:** `masterarbeit` (vier Commits)
**Nur lesend:** `ma-llm-arch-extractor` (HEAD `5c0b65a`), `tritongraph`,
`ma-conformance-testrepo`

> **Kein Modell-Call, kein Extractor-Lauf, kein Export, kein Build, kein Checkout.**
> E4 wurde nicht begonnen. Der Auftrag ist die **Vorregistrierung** von Z1: er legt fest,
> was gemessen und wie ausgewertet wird, bevor ein einziger neuer Lauf existiert. Der Lauf
> ist ein eigener Auftrag.

**Vorgängerberichte:** `z1_0_bericht_bestandsaufnahme.md`, `z1_1_bericht_extractor_stand.md`,
`z1_2_bericht_chronologie.md`, `z1_p_bericht_endpunktfrage.md`,
`ex_bericht_extractor_aenderungen.md`.

---

## 0. Vorbedingungen — geprüft, nicht angenommen

| Prüfung | Soll | Ist (31.08.2026) | |
|---|---|---|---|
| `git status --porcelain` in `masterarbeit` | leer | **leer** | OK |
| `git status --porcelain` in `tritongraph` | leer | **leer** | OK |
| `git status --porcelain` in `ma-conformance-testrepo` | leer | **leer** | OK |
| `git status --porcelain` in `ma-llm-arch-extractor` | leer | **leer** | OK |
| Extractor-`HEAD` | `5c0b65a` | `5c0b65a82cc3d8af47c022d779ff63d8a20a9e08` | OK |
| `python3 tools/check_doc_invariants.py` | Exit 0 | **Exit 0**, alle 5 Invarianten erfüllt (Protokoll Rev. 46) | OK |

Kein Abbruchgrund.

---

## 1. Was dieser Auftrag geschrieben hat

| Commit | Message | Pfade |
|---|---|---|
| `371609d` | `docs: state how run 1 is handled if Z2 moves to future work` | `docs/planung/gate_notiz_2026-08-31.md` |
| `34d6738` | `docs: pre-register the Z1 extraction comparison protocol` | `docs/protokolle/z1_protokoll_extraktionsvergleich.md` |
| `f328761` | `feat: check the Z1 protocol hash in the document invariants` | `tools/check_doc_invariants.py`, `docs/protokolle/eval_protokoll_phase04.md`, `docs/repo-kontext/c5b_bericht_protokoll_freeze.md` |
| *(dieser)* | `docs: record the Z1 protocol freeze` | `docs/repo-kontext/z1_p_bericht_freeze.md` |

Gestaged wurde ausschliesslich pfadweise (`git add <pfad>`); **kein `git add -A`, kein
`git add .`, kein `git commit -a`**. **Kein Push.** Keine Trailer in den Messages.

### 1.1 Der Gate-Nachtrag (`371609d`)

`gate_notiz_2026-08-31.md` §5c trägt jetzt einen datierten Nachtrag zum dritten Ausgang
(**N₁ > 45**, „Z2 nach Future Work"). Entschieden **vor** dem Lauf und damit vor Kenntnis
von N₁: **Lauf 1 der Zelle K2 × B1 wird auch im Future-Work-Fall archiviert, gehasht und
als einzelner ausgeführter Lauf berichtet — mit N₁ als Begründung der Entscheidung, nicht
gelöscht und nicht verschwiegen.** Dazu die Berichtsform für diesen Fall: **ein** Lauf, nie
eine Messreihe — kein Median, keine Spannweite, keine Aussage über die Zelle, und das
Protokoll bleibt vorregistriertes, **nicht ausgeführtes** Design.

Begründet mit zwei Sätzen, die beide aus der Notiz selbst folgen: der Lauf ist nach §5b
**Lauf 1 von 3** und kein Wegwerflauf — diese Eigenschaft hängt nicht daran, wie die Zahl
ausfällt, die er liefert; und N₁ ist im dritten Ausgang die **Begründung** der Entscheidung,
deren tragende Zahl aus einem gelöschten Artefakt nicht nachprüfbar wäre.

**Der Alttext ist unberührt.** Die Schwellentabelle, §5b, §5d und §5e stehen zeichengleich;
der Nachtrag steht zwischen §5c und §5d, mit Datum und Auftragskürzel.

### 1.2 Das Z1-Protokoll (`34d6738`)

`docs/protokolle/z1_protokoll_extraktionsvergleich.md`, 1110 Zeilen, §0–§10 vollständig,
§10 leer. Aufbau nach dem Vorbild von `eval_protokoll_phase04.md`, aber deutlich kürzer:
Z1 ist ein Vergleich auf **einer** Fixture, kein Kampagnenapparat.

Sechs Festlegungen, die der Auftrag als zu **entscheiden** benannt hatte, sind entschieden:

1. **Endpunkt K3** — DigitalOcean-Direktzugang `https://inference.do-ai.run/v1`, Modell
   `nvidia-nemotron-3-super-120b`, Profil `digitalocean`. **Derselbe Zugangsweg wie K3 in
   Z3** (`eval_protokoll_phase04.md` §1 und §6, Fassung Rev. 32) — der Modellzugang ist
   damit zwischen den beiden kontrollierten Experimenten der Arbeit kein zusätzlicher
   Confounder. Das Profil liegt seit E-X (`57b77a0`) im Extractor.
2. **Asymmetrie benannt** — Ansatz 1 ist ein deterministisches Artefakt, Ansatz 2 eine
   gemessene Verteilung. Verbindliche Sprachregelung: **Extraktionsvergleich**, nie
   „Head-to-Head-Lauf" (§2.3).
3. **Aggregat** — Median und Spannweite über drei Läufe je Bedingung; kein Mittelwert, keine
   Nachkommastellen-Interpretation, alle drei Läufe berichtet, keiner ausgewählt (§5.1).
4. **Gültigkeit** — `valid_final == true`; ein **fehlendes** Feld ist ein **Abbruch**, nicht
   ein `false`, weil `bool(None)` einen Lauf sonst stillschweigend als ungültig führte
   (§5.2).
5. **Parse-Zusicherung** — Rohantwort gegen geparstes Modell, Schlüsselmenge und Zählwerte;
   jede Differenz bricht den Lauf ab (§5.3, siehe §2 dieses Berichts).
6. **Bauposten D1b** — die Kompressionsgrössen werden **direkt aus `meta.json`** gelesen;
   `scripts/compare_runs.py` bleibt byteidentisch und dient als Gegenprobe (§7.2, siehe §6
   dieses Berichts).

### 1.3 Die Invariante (F) (`f328761`)

Siehe §4 (Negativprobe) und §5 (Umsetzung, Nachzug Rev. 47, Positivprobe).

---

## 2. Die Parse-Zusicherung — was sie abfängt und was sie nicht ist

Die Auflage stammt aus **Befund 08, methodische Konsequenz (d)**: *„Ein Werkzeug, das aus
mehreren Artefakten eines auswählt, braucht eine Zusicherung gegen die Auswahl ungültiger
Läufe. Was in Z3 vier Auswertungsläufe gekostet hat, wird in Z1 **vorher** gebaut."*

**Der Anlass ist gemessen, nicht befürchtet.** Im Testcall vom 31.08.2026 lieferte die
Antwort **zwei Kanten**, das geparste `ArchModel` **null**
(`z1_p_bericht_endpunktfrage.md` §3.3, Prüfung C). Die Kanten fielen **still** heraus: das
Dokument trug sie unter `dependencies` statt `relations`, das Schema erlaubt Fremdschlüssel
(kein `additionalProperties: false`), pydantic verwirft unbekannte Felder, und `relations`
hat einen Default. `ArchModel.model_validate_json()` nahm die Antwort **ohne Fehler** an.

**Registriert ist deshalb, je Lauf:** (P1) Schlüsselmenge der Rohantwort gegen die
Feldmenge von `ArchModel`, `Component` und `Relation`; (P2) Anzahl Komponenten und
Relationen roh gegen geparst. Massgeblich ist der **letzte** Versuch — er erzeugt
`arch_model.json` und damit jede berichtete Zahl; frühere Versuche werden mitgerechnet und
berichtet, brechen aber nicht ab, denn dafür existiert die Retry-Schleife.

**Dieselbe Fehlerklasse dreimal im Projekt:** die stille Null aus Z3 (Protokoll §9 **T12**,
Ergänzung Rev. 32 — Graphmodus und `DEPOT_SRC` erzeugten null Findings ohne Fehlermeldung),
der Artefaktauswahldefekt (Befund 08, **08.10** — elf K3-Injektionen wurden aus einem
Artefakt mit `postrun.verdict = INVALID` als „0 Findings" gelesen), und die verlorenen
Kanten oben. Gemeinsames Merkmal: **eine Fehlkonfiguration, die ein plausibles Ergebnis
erzeugt, ohne zu scheitern.**

**Das Schema wird NICHT angepasst.** Es ist das Instrument, so wie die 17 archivierten Läufe
es benutzt haben; ein `additionalProperties: false` änderte den Messgegenstand mitten in der
Vergleichskette. Die Zusicherung sitzt an der **Parse-Grenze** und arbeitet ausschliesslich
auf Artefakten, die der Extractor ohnehin schreibt (`attempts/attempt_<n>/raw_response.json`
und `arch_model.json`) — **kein Eingriff in den Extractor**.

---

## 3. Der SHA256 des eingefrorenen Z1-Protokolls

Nachgetragen unmittelbar nach Commit `34d6738`
(„docs: pre-register the Z1 extraction comparison protocol"):

```
$ sha256sum docs/protokolle/z1_protokoll_extraktionsvergleich.md
60cd6b3a255e148611cb5425e24c410db9d2e81235df75fc31e8cdf1fdba85c4  docs/protokolle/z1_protokoll_extraktionsvergleich.md
```

| Datei | Rev. | Commit | SHA256 |
|---|---|---|---|
| ~~`docs/protokolle/z1_protokoll_extraktionsvergleich.md`~~ | ~~**1**~~ | ~~`34d6738`~~ | ~~**`60cd6b3a255e148611cb5425e24c410db9d2e81235df75fc31e8cdf1fdba85c4`**~~ |
| ~~`docs/protokolle/z1_protokoll_extraktionsvergleich.md`~~ | ~~**2**~~ | ~~`34d6738` + Amendment Z1-R (Rev. 2)~~ | ~~**`9e02556139bd598e7f0e046db760a5f0bdf5e5b295881e9801e4e92eed71f405`**~~ |
| ~~`docs/protokolle/z1_protokoll_extraktionsvergleich.md`~~ | ~~**3**~~ | ~~`34d6738` + Amendments Z1-R (Rev. 2) und Z1-T (Rev. 3)~~ | ~~**`5fd18ef3f62035c027f5e060fc79574adaedc1e247ea586f7f7d8148eb49d27d`**~~ |
| ~~`docs/protokolle/z1_protokoll_extraktionsvergleich.md`~~ | ~~**4**~~ | ~~`34d6738` + Amendments Z1-R (Rev. 2), Z1-T (Rev. 3) und Z1-A (Rev. 4)~~ | ~~**`4789f92acbc56f83f618e614259f033a77c3ce5bf7fd962b18540cb281552445`**~~ |
| ~~`docs/protokolle/z1_protokoll_extraktionsvergleich.md`~~ | ~~**5**~~ | ~~`34d6738` + Amendments Z1-R (Rev. 2), Z1-T (Rev. 3), Z1-A (Rev. 4) und Z1-A (Rev. 5)~~ | ~~**`a6a42f3a65b62a73a0c7c4e849174c274dc56202ac838edde2e215dcb999fe95`**~~ |
| `docs/protokolle/z1_protokoll_extraktionsvergleich.md` | **6** | `34d6738` + Amendments Z1-R (Rev. 2), Z1-T (Rev. 3), Z1-A (Rev. 4 und Rev. 5) und **N07 (Rev. 6)** | **`618ebde09d66201034013a0b7ed92c97df6b8234ab5c92c7588d2c574eca7679`** |

> **Nachtrag 31.08.2026 (Z1-R, Phase 1) — der Z1-Protokoll-SHA ist nachgezogen; der Wert
> von Rev. 1 steht gestrichen darüber.** Das Amendment **Rev. 2** betrifft
> **ausschliesslich §8 E8** und bewegt **keine Zahl, keine Schwelle und keine
> Falsifikationsbedingung**:
>
> - **(a)** Klargestellt, dass der `adjusted_rand_index` in E8 die **Entscheidungsregel**
>   der Erwartung ist und **keine berichtete Kennzahl** — er erscheint nicht in der
>   Ergebnistabelle §7.1, sondern nur im Verdikt zu E8. Damit ist §4 („was der Code nicht
>   rechnet, wird nicht registriert") **nicht verletzt: §4 regelt die berichteten
>   Kennzahlen, E8 eine Prüfregel.** Ohne diesen Satz lesen §4 und §8 gegeneinander.
>   Dazu die Abgrenzung zu `gold_similarity` (§4.4): dieselbe Funktion
>   (`metrics.py:179-216`), aber gegen die **Gold**-Partition statt gegen die
>   **Triton-Reduktion**, und **berichtet** statt **entscheidend**.
> - **(b)** Auflage: der ARI wird gegen Fixtures **handgerechnet** geprüft, bevor er ein
>   Verdikt trägt — mindestens eine identische Partition (ARI 1.0), eine verschobene
>   (< 1.0) und die Triton-Reduktion gegen sich selbst. Anlass ist der **K4/K5-Join in
>   Z3**, wo ein Nullergebnis wie ein Befund aussah (Befund 08). **Die Prüfung liegt in
>   Z1-A**, nicht im Laufauftrag.
>
> **Mitgezogen, offen benannt:** die `Stand:`-Zeile im Kopf trug noch „Entwurf zur
> Vorregistrierung — Freeze steht aus", obwohl das Dokument seit `34d6738` eingefroren ist.
> Sie steht jetzt auf **Rev. 2 · EINGEFROREN zur Vorregistrierung, Rev. 1**, der Alttext
> gestrichen sichtbar darunter. Das ist ein **Nachzug einer Tatsachenaussage**, keine
> Bewegung am Messteil — er war ohnehin nötig, weil die Kopf-Revision mit §10 und der
> Revisionshistorie dieselbe Nummer tragen muss.
>
> ```
> $ sha256sum docs/protokolle/z1_protokoll_extraktionsvergleich.md
> 9e02556139bd598e7f0e046db760a5f0bdf5e5b295881e9801e4e92eed71f405  docs/protokolle/z1_protokoll_extraktionsvergleich.md
> ```
>
> **Kein Re-Run**, weil zum Zeitpunkt des Amendments **kein Z1-Lauf existiert**: das
> Amendment steht in Phase 1 des Laufauftrags, vor dem ersten Modell-Call. Belege:
> Protokoll §8 E8 (Nachtrag), Revisionshistorie Rev. 2 und §10 Zeile 2,
> `z1_r_bericht_laufskript.md`.

> **Nachtrag 31.08.2026 (Z1-T, Phase 2) — der Z1-Protokoll-SHA ist erneut nachgezogen; der
> Wert von Rev. 2 steht gestrichen darüber.** Das Amendment **Rev. 3** hat einen **Anlass
> mit Zahlen**: die sechs K2-Läufe vom 31.08.2026 haben den registrierten Messeingang
> **nicht erhalten**. Der gerenderte Prompt (`cb2fcefd…`, 18 842 B) zählt unter dem
> Tokenizer von `qwen2.5-coder:7b` **4 281 Token**; der Ollama-Server lud mit dem
> Vorgabefenster **4096** und liess **2 050** herein — genau der Wert, den alle sechs Läufe
> in `usage.prompt_tokens` des ersten Versuchs tragen. Die Bedingung K2 ist damit **nicht
> gemessen**, nicht schlecht gemessen.
>
> Registriert sind vier Stellen, **keine davon im Kennzahlenteil**:
>
> - **(a) §3.3 (6) neu** — das **Kontextfenster des Ollama-Servers** als expliziter
>   Umgebungsparameter: `OLLAMA_CONTEXT_LENGTH=16384`, gesetzt am **Server**
>   (systemd-Drop-in), **nicht** über ein abgeleitetes Modell per Modelfile — das wäre eine
>   andere Modellidentität. Der Wert steht **vor** dem Lauf fest und wird danach nicht mehr
>   bewegt. Dazu §6.1 um zwei Vorbedingungen **mit Abbruch** ergänzt.
> - **(b) §5.3 Nachtrag P3** — die **Lieferzusicherung**: P1 und P2 sichern die **Antwort**,
>   P3 sichert die **Lieferung**, also genau den Fall, den beide nicht sehen konnten. Drei
>   Teile: kalte Liefersonde vor der Invocation (P3a), Fensterzeuge vor und nach (P3b),
>   Bytezeuge des archivierten Erstprompts (P3c). Ausgeführt in
>   `tools/check_z1_delivery.py`, **ausschliesslich lesend**; `tools/run_z1.py` bleibt
>   bytegleich.
> - **(c) §5.4 Nachtrag** — das Wiederholungsbudget für **K2** wird zurückgesetzt: die drei
>   Wiederholungen wurden auf einer Bedingung verbraucht, die nicht zustande gekommen ist.
>   Für **K3** bleibt es **erschöpft**; über K3 wird getrennt entschieden.
> - **(d) §6.4 Nachtrag** — der Altblock wandert unverändert nach `data/z1/k2_trunkiert/`,
>   die Neuläufe belegen ein frisches `data/z1/k2/`.
>
> **Ausdrücklich:** das Setzen des Fensters ist **keine Prompt-Revision und kein
> Ergebnis-Tuning**. Prompt, Schema und Extractor sind unberührt; das Fenster stellt die
> registrierte Bedingung her. **Ungeschminkt** dazu: auch die Juni-Läufe hatten den Prompt
> nicht vollständig (4 095 von 4 281) — der Neulauf stellt nicht den Juni-Zustand her,
> sondern liefert die Bedingung zum ersten Mal ganz.
>
> ```
> $ sha256sum docs/protokolle/z1_protokoll_extraktionsvergleich.md
> 5fd18ef3f62035c027f5e060fc79574adaedc1e247ea586f7f7d8148eb49d27d  docs/protokolle/z1_protokoll_extraktionsvergleich.md
> ```
>
> **Re-Run: ja, für K2** — drei neue Läufe unter dem registrierten Fenster, in einem eigenen
> Block; **nein für K3**, und **keine Kennzahl, Schwelle oder Erwartung bewegt** (§4, §7, §8
> zeichengleich). Belege: Protokoll §3.3 (6), §5.3, §5.4, §6.1, §6.4, Revisionshistorie
> Rev. 3 und §10 Zeile 3, `z1_t_bericht_kontextfenster.md`.

**Warum der Wert hier steht und nicht im Protokoll.** Ein Selbstbezug im gehashten Dokument
ist unmöglich: der Hash ändert sich in dem Augenblick, in dem man ihn einträgt. Präzedenz
ist der Z3-Freeze — `eval_protokoll_phase04.md` §0.1 verweist für seinen eigenen SHA auf
`c5b_bericht_protokoll_freeze.md` §3, mit derselben Begründung.

**Der Wert bezeugt den Stand nach Commit `34d6738` und ist der Anker der
Vorregistrierung.** Jede spätere Änderung am Z1-Protokoll ändert ihn; genau das ist der
Zweck.

### Regel für die Zeit nach dem Freeze

**Jede Änderung am Z1-Protokoll ist eine datierte Revision** — auch ein reiner Hash-Nachzug,
auch eine Änderung, die inhaltlich nichts verschiebt. Geführt wird sie in **beiden** Stellen:
Revisionshistorie im Kopf des Protokolls **und** Amendments-Tabelle §10, nie nur an einer.
Der neue SHA wird in der Tabelle oben nachgetragen, der alte bleibt **durchgestrichen
sichtbar** stehen.

Der Grund ist im Projekt belegt und keine Vorsicht: der Hash-Nachzug aus C6b-2b war in
`0c1cc34` vollzogen, ohne als Revision registriert zu sein — der Bytestand des eingefrorenen
Z3-Protokolls war dadurch **in keinem Dokument bezeugt**
(`c6b0a_bericht_invarianten.md`, Protokoll Rev. 36). Aus diesem Ausfall ist der Prüfer
überhaupt erst entstanden.

---


> **Nachtrag 31.08.2026 (Z1-A) — der Z1-Protokoll-SHA ist auf Rev. 4 nachgezogen; der Wert
> von Rev. 3 steht gestrichen darüber.** Das Amendment **Rev. 4** betrifft **zwei Stellen**
> und bewegt **keine Zahl, keine Schwelle und keine Falsifikationsbedingung**:
>
> - **(a)** §5.4 **Klarstellung**: „nicht erhoben" deckt **zwei** Sachlagen — **(i)** keine
>   Antwort auf die registrierte Frage (Transportfehler, Zeitüberschreitung,
>   **Lieferausfall**) und **(ii)** Antwort erhalten, durchgängig ungültig. Beide werden
>   **getrennt** berichtet, je Bedingung mit **Gültigkeit, Zähler und Ursache**; ein Block
>   des Falls (i) wird **nicht als Modellbefund geführt**. Das ist die Präzisierung der
>   bestehenden Regel („die Zeile trägt ‚nicht erhoben' und den Grund"), **keine neue
>   Metrik**.
> - **(b)** §3.3 **(7) neu**: der **Ollama-Digest** wird als Messeingang registriert —
>   Manifest-Digest `dae161e27b0e90dd…`, Modellschicht `sha256:60e05f21…` —, zu erheben
>   ins **Laufmanifest**, nicht in den Extractor. Anlass: `model_version` trägt nur den
>   beweglichen Tag; für die Juni-Serie ist die Modellidentität deshalb nicht mehr
>   entscheidbar. Registriert wird **kein** Wert rückwirkend; eine Abweichung ist
>   **Meldepflicht, kein Abbruch**.
>
> ```
> $ sha256sum docs/protokolle/z1_protokoll_extraktionsvergleich.md
> 4789f92acbc56f83f618e614259f033a77c3ce5bf7fd962b18540cb281552445  docs/protokolle/z1_protokoll_extraktionsvergleich.md
> ```
>
> **Kein Kennzahlenteil ist berührt**: §4, §7 und §8 stehen zeichengleich. **Kein Re-Run** —
> das Amendment ändert **keinen** Messeingang der zwölf bereits erhobenen Läufe: (a) bewegt
> allein die Berichtsform, (b) gilt ausdrücklich nur für **künftige** Läufe.


> **Nachtrag 01.09.2026 (Z1-A) — der Z1-Protokoll-SHA ist auf Rev. 5 nachgezogen; der Wert
> von Rev. 4 steht gestrichen darüber.** Das Amendment **Rev. 5** ist ein **reiner
> Hash-Nachzug** und genau deshalb eine eigene Revision (Protokoll §0.1 Punkt 5): §7.2
> registriert den **SHA256 des Auswertungsskripts** `tools/evaluate_z1.py`
> (`669a0a648598cb7f…`) und den seines Zählwerkzeugs `tools/z1_tokenizer.py`
> (`b1d1f6c466e0a517…`).
>
> Damit ist die **Auflage aus §7.2** erfüllt, die seit Z1-R als Restposten offenstand
> (`z1_r_bericht_laufskript.md`, „Restposten, gemeldet und nicht erledigt"). Registriert
> ist zugleich, **was das Skript nicht tut**: es importiert `metrics.py` und `validate.py`
> unverändert und rechnet selbst keine Kennzahl; `compare_runs.py` bleibt byteidentisch und
> wird als Gegenprobe ausgeführt; `z1_tokenizer.py` ist **kein** Messinstrument nach §4,
> sondern der Zähler einer als solche gekennzeichneten **Extrapolation**.
>
> ```
> $ sha256sum docs/protokolle/z1_protokoll_extraktionsvergleich.md
> a6a42f3a65b62a73a0c7c4e849174c274dc56202ac838edde2e215dcb999fe95  docs/protokolle/z1_protokoll_extraktionsvergleich.md
> ```
>
> **Kein Kennzahlenteil ist berührt**: §4, §7.1 und §8 stehen zeichengleich. **Kein Re-Run.**

> **Nachtrag 01.09.2026 (N07) — der Z1-Protokoll-SHA ist erneut nachgezogen; der Wert von
> Rev. 5 steht gestrichen darüber.** Das Amendment **Rev. 6** trägt **einen neuen Threat**
> in §9 ein und berührt **keinen Kennzahlenteil**: §4, §7 und §8 stehen zeichengleich, T-Z1-1
> bis T-Z1-10 unverändert.
>
> **T-Z1-11 — die Ausführungsgeometrie des Inferenzservers** (`n_ctx` / `-c`, die daraus
> abgeleitete Batchgrösse `-b`/`-ub`, die KV-Cache-Geometrie) **ist ein
> bezeugungspflichtiger Umgebungsparameter**; künftige Läufe führen sie samt Serverversion
> und Startparametern im **Laufrecord**, am laufenden Prozess erhoben.
>
> **Der Anlass ist eine Messung, keine Vermutung** (`z1_s_bericht_diagnoselauf.md` §6–§8;
> Archiv `data/z1_s_diagnose/`, 51 Dateien, `sha256sum -c` Exit 0): zwei Diagnoseläufe auf
> derselben Maschine, derselben Ollama-Fassung **0.30.10**, demselben Modell-Blob
> `sha256:60e05f21…bfc2463` und mit **token-für-token demselben Erstprompt** (4 095 IDs)
> haben bei `temperature=0` und `seed=0` **verschieden geantwortet** — **1 517 gegen 2 261
> Zeichen** —, der eine `valid_final = true` mit 0 Fehlern, der andere `valid_final = false`
> mit 14 Fehlern der Klasse `relation`. Verändert war allein `-c 4096` gegen `-c 16384` samt
> der daraus abgeleiteten `-b`/`-ub` 512 gegen 1024 und 224 gegen 896 MiB KV-Cache.
>
> **Ausdrücklich kein Wert rückwirkend, keine Entwertung des Bestandes.** Für `data/z1/k2/`
> ist das Fenster über §3.3 (6)/§6.1 und die Lieferzusicherung P3b vor **und** nach jedem
> Lauf bezeugt; unbezeugt sind allein die **übrigen** Geometriegrössen — genau die Lücke, die
> die Registrierung für **künftige** Läufe schliesst. **Rev. 4** hatte den **Modell**-Digest
> registriert (§3.3 (7)); dies ist die zweite Hälfte derselben Lücke.
>
> **Als Reichweitengrenzen mitregistriert:** die drei Grössen sind **gebündelt** (der Server
> leitet Batchgrösse und Cache-Geometrie aus `n_ctx` ab) und in diesen Läufen **nicht
> getrennt**; der Nachweis stammt aus **Diagnoseläufen ausserhalb des Protokolls**, auf einer
> **anderen Maschine** als der Messrechner, und trägt **keine Z1-Kennzahl**.
>
> ```
> $ sha256sum docs/protokolle/z1_protokoll_extraktionsvergleich.md
> 618ebde09d66201034013a0b7ed92c97df6b8234ab5c92c7588d2c574eca7679  docs/protokolle/z1_protokoll_extraktionsvergleich.md
> ```
>
> **Kein Re-Run** — keine Kennzahl, keine Schwelle, keine Erwartung aus §8 bewegt. Belege:
> Protokoll §9 (Amendment Rev. 6), Revisionshistorie Rev. 6 und §10 Zeile 6;
> `z1_s_bericht_diagnoselauf.md`; `n07_bericht_nachtrag.md`.

## 4. Negativprobe zu (F) — der Prüfer schlägt an

Die Invariante ist nur ein Detektor, wenn sie in **beiden** Richtungen anschlägt: wenn
sich das Protokoll bewegt, und wenn sich der Bericht bewegt. Beide Richtungen sind
gefahren und danach zurückgesetzt — die Arbeitsbäume sind hinterher unverändert (§8). Die
Umsetzung von (F) selbst steht in §5.

### 4a — Das Protokoll bewegt sich, der Bericht nicht

Ein einzelnes Byte an das
Z1-Protokoll angehängt, Prüfer gefahren, danach `git checkout --` zurückgesetzt:

```
$ printf '\n' >> docs/protokolle/z1_protokoll_extraktionsvergleich.md
$ python3 tools/check_doc_invariants.py; echo "EXIT=$?"
...
[FEHL] (F) Z1-Protokoll-SHA gegen z1_p_bericht_freeze.md §3
        IST  (Datei)               8a97f195d4134322645190ff23a00787b9f8af10879e8fec16744dee75999506
        SOLL (z1_p_bericht_freeze.md §3, Rev. 1)  60cd6b3a255e148611cb5425e24c410db9d2e81235df75fc31e8cdf1fdba85c4
        Der Bytestand des Z1-Protokolls ist nicht bezeugt. Entweder ist das Protokoll
        geändert und die Änderung nicht als Revision registriert (Z1-Protokoll §0), oder
        der Nachzug in §3 des Z1-Freeze-Berichts fehlt.

ERGEBNIS: FEHLGESCHLAGEN — Invariante(n) F
EXIT=1
```

### 4b — Der Bericht bewegt sich, das Protokoll nicht

Ein Zeichen im bezeugten Hash dieses
Berichts geändert, Prüfer gefahren, danach zurückgesetzt:

```
$ python3 tools/check_doc_invariants.py; echo "EXIT=$?"
...
[FEHL] (F) Z1-Protokoll-SHA gegen z1_p_bericht_freeze.md §3
        IST  (Datei)               60cd6b3a255e148611cb5425e24c410db9d2e81235df75fc31e8cdf1fdba85c4
        SOLL (z1_p_bericht_freeze.md §3, Rev. 1)  60cd6b3a255e148611cb5425e24c410db9d2e81235df75fc31e8cdf1fdba85c0

ERGEBNIS: FEHLGESCHLAGEN — Invariante(n) F
EXIT=1
```

### 4c — Der Bericht fehlt ganz

Dieser Fall ist im Lauf dieses Auftrags **von selbst**
eingetreten: zwischen Commit `f328761` (Prüfer mit (F)) und Commit 4 (dieser Bericht) gab es
die Datei noch nicht.

```
[FEHL] (F) Z1-Protokoll-SHA gegen z1_p_bericht_freeze.md §3
        PARSE-FEHLER: Datei fehlt: docs/repo-kontext/z1_p_bericht_freeze.md
```

**Ungeschminkt vermerkt:** nach Commit `f328761` stand der Prüfer damit auf **Exit 1** —
allein wegen (F), (A) bis (E) waren grün. Das ist der Preis der im Auftrag vorgegebenen
Commit-Reihenfolge (Prüfer vor Bericht) und war unvermeidbar, ohne die Reihenfolge zu
ändern. Ab Commit 4 ist der Prüfer wieder auf Exit 0.

---

## 5. Die Invariante (F) — Umsetzung und Nachzug

### 5.1 Was (F) prüft

**SHA256 des Z1-Protokolls gegen den in §3 dieses Berichts als aktuell geführten Wert** —
dieselbe Bewegungsprüfung, die **(A)** für das Z3-Protokoll gegen
`c5b_bericht_protokoll_freeze.md` §3 leistet.

Umgesetzt ohne Doppelung: die Leseroutine der Freeze-Tabelle
(`expected_protocol_hash`) ist um zwei Parameter erweitert — Berichtspfad und Dateiname —
und wird von **(A) und (F) geteilt**. Sie liest weiterhin nach derselben Regel: gestrichene
Zeilen sind überholt, eine Zeile mit *(keine)* in der Revisionsspalte ist ein bezeugter
Bytestand, der nie eine Revision war, aktuell ist die ungestrichene Zeile mit der höchsten
Revisionsnummer. **(A) liest dieselbe Tabelle mit demselben Ergebnis** — belegt in §5.3:
die Ausgabe von (A) ist vor und nach der Erweiterung zeichengleich bis auf die
Revisionsnummer, die der Nachzug aus §5.2 ohnehin verschiebt.

Der Prüfer bleibt **ausschliesslich lesend** und repariert nichts.

### 5.2 Der Nachzug: Z3-Protokoll Rev. 47

Der Prüfer ist selbst ein registriertes Auswertungsinstrument: sein SHA256 steht in
`eval_protokoll_phase04.md` §0.1 und wird dort von **Invariante (E)** geprüft. Die
Erweiterung um (F) bewegt diesen Hash und liess (E) fehlschlagen — nachgemessen:

```
[FEHL] (E) SHA256 der drei Auswertungsinstrumente gegen Protokoll §0.1
        FEHL tools/check_doc_invariants.py
               IST  (Datei)      c351a137e3f32e00b67e8f73d7cce0777f607c872fda4a7719c1b142b8707fdf
               SOLL (§0.1)       6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018
```

**Rückfrage gestellt und vom Auftraggeber entschieden:** Hash-Nachzug im Z3-Protokoll als
**Rev. 47**, nach der Präzedenz Rev. 39 / 41 / 43 / 45, statt eines zweiten, eigenständigen
Prüferskripts. Der Auftragstext hatte das Z3-Protokoll als „nicht Gegenstand" geführt; die
Abweichung ist damit **entschieden und hier vermerkt**, nicht stillschweigend geschehen.

| Datei | vorher (Rev. 45) | nachher (Rev. 47) |
|---|---|---|
| `tools/evaluate_campaign.py` | `b66be750…9a93428` | **unverändert** |
| `tools/match_k4k5.py` | `c16e7c43…799f4ca6` | **unverändert** |
| `tools/check_doc_invariants.py` | `6cc16ef9…1e52b7018` | **`c351a137…2b8707fdf`** |

Geführt an **allen drei** Stellen, im selben Commit `f328761`:

- **§0.1**, Zeile Auswertungsinstrumente — alter Wert gestrichen sichtbar, neuer daneben,
  mit Anlass;
- **Kopf** — Stand auf Rev. 47, Alttext (Rev. 46) gestrichen stehen gelassen,
  Revisionshistorieneintrag „Rev. 47" mit Begründung;
- **§10**, Amendments nach Messbeginn — Zeile 47 mit Änderung, Begründung und
  Re-Run-Spalte **„nein"**;
- **`c5b_bericht_protokoll_freeze.md` §3** — die Zeile Rev. 46 gestrichen, Zeile Rev. 47 mit
  dem neuen Protokoll-SHA `71d30352834e519ae019ecc8e947a452a906f4559186452cb6243a4bf718811a`
  daneben, dazu der Nachtragsabsatz.

**Keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein Prompt und kein
Schema ist berührt; kein Re-Run folgt.** Die Invarianten (A)–(E) stehen wörtlich
unverändert; bewegt hat sich die Zahl der geprüften Invarianten, **fünf → sechs**.

### 5.3 Positivprobe — der Prüfer nach Commit 4

```
check_doc_invariants — Repo /home/haasentimo/ma/masterarbeit

[OK ] (A) Protokoll-SHA gegen c5b_bericht_protokoll_freeze.md §3
        SHA256 71d30352834e519ae019ecc8e947a452a906f4559186452cb6243a4bf718811a
        bezeugt in c5b_bericht_protokoll_freeze.md §3 als Rev. 47

[OK ] (B) Kopf-Revision = §10-Höchstzeile = neuester Historieneintrag
        Kopf Rev. 47 = Revisionshistorie Rev. 47 = §10-Zeile 47

[OK ] (C) Spezifikations-SHA gegen Protokoll §1 UND §0.1
        SHA256 39822edc0d9c109d7f1c1cfc285af9dd1363ec48b1a96a69334c173cd2cd71c7, an beiden Stellen zeichengleich
        §0.1 (Messstand): 39822edc0d9c109d7f1c1cfc285af9dd1363ec48b1a96a69334c173cd2cd71c7
        §1 (Nachtrag Rev. 30): 39822edc0d9c109d7f1c1cfc285af9dd1363ec48b1a96a69334c173cd2cd71c7

[OK ] (D) sha256sum -c UND Listing beidseitig, data/soll und data/campaign
        (Ausgabe gekürzt — 612 Dateien in 14 Verzeichnissen, 7 von 7 lebenden Dokumenten als entschiedene Ausnahme; zeichengleich zum Stand vor der Erweiterung)
[OK ] (E) SHA256 der drei Auswertungsinstrumente gegen Protokoll §0.1
        OK   tools/evaluate_campaign.py  b66be750f9b7cf524b9afa8edbab0138d17c409de4637465eb82d0f079a93428
        OK   tools/match_k4k5.py  c16e7c4380034163f3034916193bd96cfc6bb957768fe610cb7018d7799f4ca6
        OK   tools/check_doc_invariants.py  c351a137e3f32e00b67e8f73d7cce0777f607c872fda4a7719c1b142b8707fdf

[OK ] (F) Z1-Protokoll-SHA gegen z1_p_bericht_freeze.md §3
        SHA256 60cd6b3a255e148611cb5425e24c410db9d2e81235df75fc31e8cdf1fdba85c4
        bezeugt in z1_p_bericht_freeze.md §3 als Rev. 1

ERGEBNIS: alle 6 Invarianten erfüllt

EXIT=0
```

---

## 6. Bauposten D1b — die Entscheidung und ihr Preis

**Der Befund.** `scripts/compare_runs.py:18-22` führt in `COLS` alle vier **Treuegrössen**,
aber **keine** der sechs **Kompressionsgrössen** — obwohl `run_logger.py:116-121` sie in jede
`meta.json` schreibt. Die Zahlen liegen vor; das Anzeigewerkzeug holt sie nicht ab.

**Entschieden: direkt aus `meta.json` lesen, kein Extractor-Eingriff.**
`scripts/compare_runs.py` bleibt byteidentisch (`c6db316b3904338d034ac65297aa8557f1fee028`)
und wird unverändert als **Gegenprobe** für das benutzt, was es rechnet: Byte-Identität der
`arch_model.json` über eine Gruppe und `validity_rate(valid_final)`.

**Der tragende Grund ist nicht die Sparsamkeit, sondern dass der andere Weg nichts gekauft
hätte.** Die Ergebnistabelle des Protokolls (§7.1) verlangt **Median und Spannweite** je
Bedingung sowie den deterministischen Einzelwert von Ansatz 1. `compare_runs.py` bildet
**weder** Median **noch** Spannweite **noch** eine Ansatz-1-Zeile (`:51-64`: eine Zeile je
Lauf, zwei Gruppenaggregate). Ein Auswertungsskript in `masterarbeit` ist damit **ohnehin**
nötig — und es liest `meta.json`. Ergänzte man `COLS`, läse es die Kompressionsgrössen
trotzdem aus derselben Quelle. Dazu: der Extractor ist der Messgegenstand
(`00_stand_und_entscheidungen.md` §0, „Eingefroren außer dem zurückgestellten Logging-Fix
(D3)"); ein vierter Commit für eine reine Anzeigespalte verlangte denselben Apparat wie
E-X — eigener schreibender Auftrag, Fixture-Test, Blob-Nachzug in `z1_1`, `z1_2` und
`PROVENANCE.md` — ohne dessen Gewicht zu haben.

**Der Preis, offen benannt:** ein zweites Werkzeug neben `compare_runs.py`, das dieselben
`meta.json` liest. Die Doppelung ist **gewollt** — sie ist die Gegeninstanz aus §5.3 in
Werkzeugform. Weichen die beiden in einer Zahl voneinander ab, ist das ein **Befund**, der
berichtet und nicht durch Angleichen aufgelöst wird (Praxis der T7-Gegenprobe,
`eval_protokoll_phase04.md` §0.1).

**Auflage aus dem Protokoll:** das Auswertungsskript wird **vor** dem ersten Z1-Lauf
geschrieben, mit Fixture-Test versehen, gehasht, und sein SHA256 wird als **Amendment**
(§10) in das Z1-Protokoll aufgenommen.

---

## 7. Was dieser Auftrag NICHT getan hat

- **Kein Z1-Lauf**, kein Modell-Call, kein Extractor-Lauf, kein Export, kein Build.
  **E4 nicht begonnen.**
- **Keine Änderung an `scripts/compare_runs.py`, `src/llm_arch/eval/metrics.py` oder
  `src/llm_arch/abstraction/schema.py`** — der Extractor ist in diesem Auftrag
  ausschliesslich gelesen worden; `git status --porcelain` dort ist unverändert leer und
  `HEAD` steht auf `5c0b65a`.
- **Kein Push** in keinem Repo. Keine Trailer in den Commit-Messages.
- **Z2, Z4, Kapitelprosa und `data/campaign/`** nicht angefasst; `data/z1/` **nicht
  angelegt** — die Archivwurzel entsteht im Laufauftrag.
- **Das Auswertungsskript aus §3 ist nicht geschrieben** — es gehört nach §7.2 des
  Protokolls vor den Lauf, nicht in die Vorregistrierung.

### Restposten, gemeldet und nicht erledigt

- **`DEFERRED.md:47-48` und `:58-59` im Extractor** sind weiterhin veraltet
  (`ex_bericht_extractor_aenderungen.md` §3.2). Nicht angefasst, hier nur erneut vermerkt.
- **`seed` fehlt im Laufrecord** (`ex_bericht_extractor_aenderungen.md` §2.4). Im
  Z1-Protokoll §3.3 (1) als **Umgebungsparameter** registriert statt behoben — der Extractor
  bleibt für Z1 unangetastet.

---

## 8. Abschlusshygiene

**Der Prüfer nach jedem Commit:**

| nach Commit | Ergebnis |
|---|---|
| `371609d` (Gate-Nachtrag) | **Exit 0**, alle 5 Invarianten erfüllt |
| `34d6738` (Z1-Protokoll) | **Exit 0**, alle 5 Invarianten erfüllt |
| `f328761` (Invariante (F) + Nachzug Rev. 47) | **Exit 1** — (A) bis (E) grün, **(F) FEHL: „Datei fehlt"**, weil dieser Bericht erst mit Commit 4 entsteht (§4c) |
| Commit 4 (dieser Bericht) | **Exit 0**, alle **6** Invarianten erfüllt (§5.3) |

**`git status --porcelain`, alle vier Bäume**, unmittelbar vor Commit 4 gemessen:

```
--- ~/ma/masterarbeit
?? docs/repo-kontext/z1_p_bericht_freeze.md
--- ~/ma/tritongraph
(leer)
--- ~/ma/ma-conformance-testrepo
(leer)
--- ~/ma/ma-llm-arch-extractor
(leer)
```

Der einzige Eintrag ist dieser Bericht selbst; mit Commit 4 ist auch `masterarbeit` leer.
Die drei nur lesenden Bäume sind über den gesamten Auftrag unberührt geblieben — insbesondere
der Extractor, dessen `HEAD` unverändert auf `5c0b65a82cc3d8af47c022d779ff63d8a20a9e08` steht.

**Die beiden Negativproben aus §4 sind vollständig zurückgesetzt** (`git checkout --` für
das Protokoll, Rücksicherung des Berichts aus dem Scratchpad); die gehashten Bytestände sind
danach gegengeprüft: das Z1-Protokoll steht wieder auf
`60cd6b3a255e148611cb5425e24c410db9d2e81235df75fc31e8cdf1fdba85c4`, und der Prüfer meldet
Exit 0.

**Kein Push.**
