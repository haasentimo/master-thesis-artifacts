# C5b — Bericht: Freeze des Evaluationsprotokolls auf Rev. 33

**Masterarbeit Timo Haas · HTWG Konstanz**
**Datum:** 27. August 2026 · **Auftrag:** C5b (Protokoll Rev. 33 — Freeze zur
Vorregistrierung) · **Schreibendes Repo:** `masterarbeit`
**Ausgangsstand:** `masterarbeit` `06b2630`, Protokoll Rev. 32

> **Der Auftrag war der letzte Schritt vor dem ersten Kampagnenlauf.** Kein Modell-Call, kein
> Messlauf, kein Checkout, kein Build. Geändert wurde ausschliesslich Dokumentation.

---

## 0. Vorbedingungen — alle vier erfüllt

| Prüfung | Erwartet | Gemessen am 27.08.2026 |
|---|---|---|
| `git status --porcelain` in `masterarbeit` | leer | **leer** |
| `git status --porcelain` in `tritongraph` | leer | **leer** |
| `git status --porcelain` in `tritongraph-measure` | leer | **leer** |
| `git status --porcelain` in `ma-conformance-testrepo` | leer | **leer** |
| `git -C ~/ma/masterarbeit log --oneline -2` | zeigt `06b2630` | **`06b2630`** (davor `70a2dd8`) |
| `eval_protokoll_phase04.md` | Rev. 32 | **Rev. 32** (Kopfzeile: „Stand: 26. August 2026 (Rev. 32) · Status: Entwurf zur Vorregistrierung — Freeze steht aus") |
| `sha256sum -c data/soll/SHA256SUMS` | 7 von 7 OK | **7 von 7 OK**, Exit 0 |

Kein Abbruchgrund. Der Auftrag ist vollständig ausgeführt.

---

## 1. Teil 1 — §0 Punkt 2 entschieden: das Validitäts-Gate 0.9 ist bestätigt

### Setup

§0 des Protokolls führte seit dem 12.08.2026 **einen** offenen Punkt: das Validitäts-Gate
0.9 aus §7 zu bestätigen, „technisch prüfbar erst nach CLI-Inkrement 4 (Exit-Code 3 bei
`valid_final=false`)". Solange dieser Punkt offen war, durfte das Protokoll nicht als
eingefroren gelten.

Zu entscheiden war nicht der **Wert** — 0.9 steht seit Rev. 2 in §7 —, sondern ob die
technische Vorbedingung erfüllt ist und ob der Beobachtungsstand die Regel trägt. Der
Beobachtungsstand wurde **ausgelesen**, nicht aus Berichten übernommen: über die
`llm_call`-Records der archivierten Laufprotokolle beider Kontrollbestände.

### Resultat

**(a) Die technische Vorbedingung ist erfüllt.** `valid_final=false`-Läufe sind über
**Exit-Code 3** bzw. über das **persistierte Run-Log** identifizierbar (CLI-Inkremente 2
und 4); der eingefrorene Messstand enthält **Increment 7**. Die stille Zählung invalider
Läufe als „0 Findings" — der Grund, aus dem der Punkt überhaupt offen war — ist damit durch
ein Feld im Artefakt ausgeschlossen, nicht durch Aufmerksamkeit beim Auswerten.

**(b) Anteil valider Calls in den Kontrollläufen**, ausgezählt am 27.08.2026 über
`record_type == "llm_call"`:

| Kontrollbestand | Invocations (`*.jsonl`) | `llm_call` | `valid_final=true` | **Anteil** | `valid_raw=true` | Retries (`attempts_used-1`) | `outcome` |
|---|---|---|---|---|---|---|---|
| **K2** — `data/c3b-k2/runs/` | 52 | 156 | 156 | **1.0** | 156 | 0 | `measured` × 156 |
| **K3** — `data/c3b-k3/runs/` | 52 | 156 | 156 | **1.0** | 156 | 0 | `measured` × 156 |

Es gibt in beiden Beständen **keinen** Fall, in dem erst ein Repair-Versuch die Gültigkeit
hergestellt hat (`valid_raw` ist überall schon `true`, `attempts_used` überall 1).
Deckungsgleich mit den `run_footer`-Feldern (`calls_invalid: 0`, `invalid_calls: []`,
`invalid_reasons: []`) und mit den Nachlaufprüfungen in
[c3b_k2_bericht_kontrolllauf.md](c3b_k2_bericht_kontrolllauf.md) und
[c3b_k3_bericht_kontrolllauf.md](c3b_k3_bericht_kontrolllauf.md).

**Beide Anteile liegen bei 1.0, also über 0.9.** Der Abbruchfall des Auftrags — Anteil unter
0.9 in einem der beiden Bestände, dann nicht das Gate verschieben, sondern abbrechen — ist
**nicht eingetreten**.

**(c) Die Richtung der Regel ist konservativ.** Unterschreitet eine Konfiguration das Gate,
folgt **Dokumentation als Befund** und **Auswertung mit den vorhandenen validen Läufen**,
ausdrücklich **ohne Nachbesserung**: kein Prompt-Tuning (Eine-Iteration-Regel, §7), kein
selektives Nachmessen (§1), keine Anpassung des Gates. Die Regel kann ein Ergebnis nur
**verschlechtern oder unangetastet lassen** — sie ist eine Berichtspflicht, keine
Ausstiegsklausel.

**(d) Der Zeitpunkt ist der Punkt.** Die Bestätigung erfolgt **vor dem ersten
Kampagnenlauf**; die ausgezählten Anteile stammen ausschliesslich aus den Kontrollläufen auf
der **sauberen Baseline** (C3b), nicht aus Injektionsläufen. Eine Bestätigung **nach**
Sichtung der Kampagnen-`valid_final`-Werte wäre nicht mehr vorregistriert, sondern an den
Daten gewählt. Dieser Vermerk steht wörtlich im Protokoll (§0 Punkt 2 (d)), nicht nur hier.

### Konsequenz

**Das Gate 0.9 ist bestätigt, unverändert.** §0 Punkt 2 steht durchgestrichen mit
auflösendem Text; die einleitende Zeile von §0 („offen ist allein Punkt 2") steht ebenfalls
gestrichen, daneben der neue Stand: alle vier Punkte entschieden. **Damit fällt der letzte
Punkt, der dem Freeze entgegenstand.**

---

## 2. Teil 2 — Kopfstatus und Messstandstabelle

### Setup

Die Kopfzeile trug bis hierher „Entwurf zur Vorregistrierung — Freeze steht aus (§0)". Ein
eingefrorenes Protokoll ohne ausgewiesenen Messstand ist ausserdem nur die halbe
Vorregistrierung: es sagt, **was** gemessen wird, aber nicht, **wogegen**.

### Resultat

**Kopfzeile.** Neu: „Stand: 27. August 2026 (Rev. 33) · Status: **EINGEFROREN zur
Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1". Der Alttext steht
darunter **durchgestrichen** mit Datum und Auftragsverweis.

**Neuer Abschnitt §0.1 „Messstand (eingefroren)".** Als `## 0.1` zwischen §0 und §1
eingesetzt, damit die Nummerierung von §1–§10 und die hunderten Querverweise darauf
unangetastet bleiben. Jeder Wert ist am 27.08.2026 aus Datei bzw. Repositorium **gelesen**
(`sha256sum`, `git rev-parse`, `git tag -l`), keiner aus einem Bericht übernommen:

| Gegenstand | Wert |
|---|---|
| **Protokoll** | `docs/protokolle/eval_protokoll_phase04.md`, ~~**Rev. 33**~~ ~~**Rev. 34** (Amendment C5c, 27.08.2026)~~ ~~**Rev. 35** (Amendments C5c und C10a, 27.08.2026)~~ **Rev. 36** (Amendments C5c, C10a und C6b-0a, 27.08.2026) · SHA256 siehe §3 dieses Berichts — **alle vier Werte** plus der **unbezeugte Zwischenstand nach `0c1cc34`**, der nie eine Revision war: der des Freeze-Standes und je einer nach den drei Amendments |
| **Auswertungsspezifikation** | `docs/protokolle/c6_auswertungsspezifikation.md` = `2f1354bbabdfaef8c858a6726521e224c30d6293513d83ea98cd1ef3f6608f97` |
| **Messeingänge `data/soll/`** | `architecture-rules.yaml` = `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` |
| | `depot_soll.ilograph.yaml` = `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` |
| | `importlinter.ini` = `0c9a1e0e0430ff01e8383407ec6212c58ddcbec6e529db7b044a30132b528751` |
| | `test_architecture.py` = `7504e30ce993803f4f3dab3023ed60742fcbd2382b9deb481d1860a67186a289` |
| | `control_files.txt` = `7356e6d332e5165acdfdcfac1a66bd9803a7fa36cb4b3e7d5480bcb3526fee62` |
| | `injection_manifest.md` = `63425d5501c8f5c13459e78782e370981db8e4aa68072aae46137550b98629e1` |
| | `injection_manifest.json` = `2744116e513c9e79e3174e6e3681abdcdc7c18f36d00b6d334875e4e918cfb1f` |
| **Checker** | `phase04-freeze` = `348ca9daa456af4954f11f7152fc45201035297e` · Tag-Objekt `19e7a7a5332c577dea194717f4bbe64cebcfdac4` · Messpfad `/home/haasentimo/ma/tritongraph-measure` |
| **Checker-Artefakt** | `packages/triton-conformance/dist/cli.js` = `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` |
| **Runner** | ~~Commit `70a2dd87905284cb36a4a5ba1e42e851c6fa9e95` (`70a2dd8`)~~ — **nachgezogen am 27.08.2026 durch C5c:** `b6f9972067f6c7b4288c14bb52723f5c8a4a7a82` (`b6f9972`), einzige Differenz ist die Vorgabe von `--out` |
| **Testrepo** | `baseline` = `0d651041ed87dd03f2f78359713633fac01c0a66` · 32 Tags `inj/01`–`inj/32` · Injektions-Bundle = `1b9f8b58f271332e2d66ead83a3858271a04f3aebce95b7927977d9fa1be508b` |
| **Archivwurzel** | ~~`/home/haasentimo/scratch/c7/out`~~ — **überholt am 27.08.2026 durch C5c (Protokoll Rev. 34):** `~/ma/masterarbeit/data/campaign/` |

**Herkunft jedes Wertes, wörtlich:**

- **Auswertungsspezifikation** — `sha256sum docs/protokolle/c6_auswertungsspezifikation.md`.
  Erwartet war laut Auftrag `2f1354bb…f6608f97`; gemessen
  `2f1354bbabdfaef8c858a6726521e224c30d6293513d83ea98cd1ef3f6608f97` — **zeichengleich**.
  Das ist der in §1 Hash-Nachzug Rev. 31 registrierte Wert.
- **Messeingänge** — die sieben Zeilen aus `data/soll/SHA256SUMS`, vollständig übernommen;
  `sha256sum -c` bestätigt sie am 27.08.2026 als **7 von 7 OK**.
- **Checker** — `git -C ~/ma/tritongraph-measure rev-parse phase04-freeze` liefert
  `19e7a7a5332c577dea194717f4bbe64cebcfdac4` (das **annotierte Tag-Objekt**),
  `rev-parse phase04-freeze^{commit}` liefert `348ca9daa456af4954f11f7152fc45201035297e`
  (den **Commit**). Beide Werte stehen im Protokoll, weil §6 Rev. 7 ausdrücklich verlangt,
  den Freeze-Tag **über seinen SHA** zu führen und nicht über den Namen (Push-Rechte auf
  `origin` umfassen das Löschen von Tags, B20). `git -C ~/ma/tritongraph-measure log
  --oneline -1` bestätigt `348ca9d`.
- **Checker-Artefakt** — `sha256sum
  ~/ma/tritongraph-measure/packages/triton-conformance/dist/cli.js`. Erwartet laut Auftrag
  `c0bbdfeb…d35d95`; gemessen
  `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` — **zeichengleich**.
- **Runner** — `git log --oneline -1 -- tools/run_campaign.py` liefert `70a2dd8`; dasselbe
  gilt für `tools/campaign_spec.py` und `tools/postrun_check.py`. Voller SHA aus
  `git rev-parse 70a2dd8`. **Nachtrag 27.08.2026 (C5c):** durch die Archivwurzel-Änderung
  liefert `git log --oneline -1 -- tools/run_campaign.py` jetzt `b6f9972`; `campaign_spec.py`
  und `postrun_check.py` stehen unverändert auf `70a2dd8`.
- **Testrepo** — `git -C ~/ma/ma-conformance-testrepo rev-parse baseline` und
  `rev-parse HEAD` liefern beide `0d651041ed87dd03f2f78359713633fac01c0a66`;
  `git tag -l 'inj/*' | wc -l` liefert **32**; die Bundle-Hashes aus
  `data/testrepo/SHA256SUMS`, mit `sha256sum -c` als OK bestätigt. **Im Testrepo wurde nur
  gelesen** — kein Commit, kein Tag, kein Checkout.
- **Archivwurzel** — ~~die Vorgabe von `--out` in [tools/run_campaign.py:820](../../tools/run_campaign.py#L820):
  `Path.home() / "scratch" / "c7" / "out"`~~. Die Unterverzeichnisse `k1/`…`k5/` und
  `manifests/` folgen aus `artefact_paths`. **Nachtrag 27.08.2026 (C5c):** die Vorgabe steht
  jetzt als Konstante `CAMPAIGN_OUT` = `MA / "data" / "campaign"` in
  [tools/run_campaign.py:64](../../tools/run_campaign.py#L64) und wird dem CLI-Parameter `--out`
  in [tools/run_campaign.py:826](../../tools/run_campaign.py#L826) als Default mitgegeben —
  **nicht hart verdrahtet**. `artefact_paths` ist **unverändert**
  ([tools/run_campaign.py:124-149](../../tools/run_campaign.py#L124-L149)); die Unterordnerstruktur
  bleibt dieselbe. Begründung siehe `c5c_bericht_archivwurzel.md`.

**Der SHA256 des Protokolls selbst** steht als „wird im Freeze-Bericht geführt" in der
Tabelle, mit Begründung: ein Selbstbezug im gehashten Dokument ist unmöglich — das Eintragen
des Hashes ändert den Hash. Der Wert steht in §3 dieses Berichts.

**Regel für die Zeit nach dem Freeze** (§0.1, Unterabschnitt): Änderungen nur als datierte
Amendments mit Begründung, geführt in **Revisionshistorie und §10**; **ab dem ersten
Kampagnenlauf ändert kein Amendment mehr** Metrikdefinition, Injektionsmanifest, Regeldatei,
Prompt oder Schema — Amendments danach dürfen **nur beschreiben, nicht festlegen**. Die
bestehende Defektklausel aus §1 (höchstens **ein** Amendment, mit **vollständigem Re-Run
aller** Konfigurationen) bleibt unverändert und ist die einzige Ausnahme. Derselbe Vorbehalt
steht als Sperrvermerk zusätzlich über der Tabelle „Amendments nach Messbeginn" in §10, weil
das die Stelle ist, an der ein späterer Eintrag geschrieben würde.

### Konsequenz

Das Protokoll trägt seinen Messstand jetzt **in sich**. Ein Leser, der wissen will, wogegen
gemessen wurde, muss keinen zweiten Bericht öffnen — und ein nachträglich verschobener
Eingang fiele beim Nachrechnen der Hashes sofort auf.

---

## 3. Der SHA256 des eingefrorenen Protokolls

Nachgetragen unmittelbar nach Commit 1 (`3e17f44`, „docs: freeze the evaluation protocol at
rev 33"):

```
$ sha256sum docs/protokolle/eval_protokoll_phase04.md
2cb0385f08e88333863d83d0819943e352d3f1b857d4870801211b4817ac181e  docs/protokolle/eval_protokoll_phase04.md
```

| Datei | Rev. | Commit | SHA256 |
|---|---|---|---|
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**33**~~ | ~~`3e17f44`~~ | ~~**`2cb0385f08e88333863d83d0819943e352d3f1b857d4870801211b4817ac181e`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**34**~~ | ~~`3e17f44` + Amendment C5c~~ | ~~**`013ddc0341d647afaebede0c300c8808e19f00a5cc8dad30b685847a48d6899f`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**35**~~ | ~~`3e17f44` + Amendments C5c und C10a~~ | ~~**`876680b13c568312059d9143b146617b3be6887e5e89a2badfd05c5361f3b910`**~~ |
| `docs/protokolle/eval_protokoll_phase04.md` | *(keine)* | `0c1cc34` | `620f11739d65ba759ea8b78eb2d710be684c40fb4c52e9e3d74a7464283d80d3` — **Bytestand nach `0c1cc34`, nachträglich bezeugt, nie als Revision geführt** |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**36**~~ | ~~`3e17f44` + Amendments C5c, C10a und C6b-0a~~ | ~~**`1240f47ebfc1b89f25068f8cc68190e7d0f54f6ad18ce10e470b74c7fb4a975e`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**37**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a und C6c~~ | ~~**`bb99fd8e3bff101714ed4d302879807d2ba90003d1ff9a3009c4b434ff01a3e5`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**38**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a und C6c (Rev. 37 und 38)~~ | ~~**`06a36473719dd3b27e9337a55b2ca1a6df5d5a3cd7357570eb7b66c347cec7fc`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**39**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a, C6c (Rev. 37 und 38) und C6c-a (Rev. 39)~~ | ~~**`9e63c37067a5a62ef95dd2d0710620939b9f03e5b0258995f01e597db5653f48`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**40**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a, C6c (Rev. 37 und 38), C6c-a (Rev. 39) und C11b (Rev. 40)~~ | ~~**`736290279992f863682b29fc02ef44f27a41d27093c52a00f04175f494da2956`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**41**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a, C6c (Rev. 37 und 38), C6c-a (Rev. 39) und C11b (Rev. 40 und 41)~~ | ~~**`e94150ae6e433fdd7f43da6b309ec4e6d11d1d6e40873e65dce4c63267218e78`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**42**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a, C6c (Rev. 37 und 38), C6c-a (Rev. 39), C11b (Rev. 40 und 41) und C11c (Rev. 42)~~ | ~~**`6988a93bfe466b8014f9052f2345485d1733d3b133e200e2178eba33f5714e2b`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**43**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a, C6c (Rev. 37 und 38), C6c-a (Rev. 39), C11b (Rev. 40 und 41) und C11c (Rev. 42 und 43)~~ | ~~**`759b11ede90232c2e3e8ce7d7e0149a9db7726d5cc87e35da7ceddb4369343f4`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**44**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a, C6c (Rev. 37 und 38), C6c-a (Rev. 39), C11b (Rev. 40 und 41), C11c (Rev. 42 und 43) und C14 (Rev. 44)~~ | ~~**`ba865b2bed9dd7f1a4bddad40f587e8a81df165222ecc2f7a3d14d09aa18309b`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**45**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a, C6c (Rev. 37 und 38), C6c-a (Rev. 39), C11b (Rev. 40 und 41), C11c (Rev. 42 und 43) und C14 (Rev. 44 und 45)~~ | ~~**`0ce57d29110214d13e888e44750b6ee3ae1e5a934aebaeb116883d005ff92eca`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**46**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a, C6c (Rev. 37 und 38), C6c-a (Rev. 39), C11b (Rev. 40 und 41), C11c (Rev. 42 und 43), C14 (Rev. 44 und 45) und G1 (Rev. 46)~~ | ~~**`96c89358a198fb230f686204f4138dd7c1c0a04e6c142f56216c6605c0fe74e2`**~~ |
| ~~`docs/protokolle/eval_protokoll_phase04.md`~~ | ~~**47**~~ | ~~`3e17f44` + Amendments C5c, C10a, C6b-0a, C6c (Rev. 37 und 38), C6c-a (Rev. 39), C11b (Rev. 40 und 41), C11c (Rev. 42 und 43), C14 (Rev. 44 und 45), G1 (Rev. 46) und Z1-P (Rev. 47)~~ | ~~**`71d30352834e519ae019ecc8e947a452a906f4559186452cb6243a4bf718811a`**~~ |
| `docs/protokolle/eval_protokoll_phase04.md` | **48** | `3e17f44` + Amendments C5c, C10a, C6b-0a, C6c (Rev. 37 und 38), C6c-a (Rev. 39), C11b (Rev. 40 und 41), C11c (Rev. 42 und 43), C14 (Rev. 44 und 45), G1 (Rev. 46), Z1-P (Rev. 47) und **N07 (Rev. 48)** | **`fd0a6b4e6638022e70da6d8ff5f0cd66930a6264d63fa4db0e02bc222ca899b0`** |

> **Nachtrag 28.08.2026 (C11b, zweiter Schritt) — der Protokoll-SHA ist ein weiteres Mal
> nachgezogen; der Wert von Rev. 40 steht gestrichen darüber.** Das Amendment **Rev. 41**
> ist ein **reiner Hash-Nachzug** der Auswertungsinstrumente nach der Reparatur R1–R9:
> `tools/evaluate_campaign.py` und `tools/match_k4k5.py` sind geändert,
> `tools/check_doc_invariants.py` ist unberührt.
>
> **Warum eine eigene Revision und nicht Rev. 40 mit anderem Bytestand.** §0.1 Punkt 5:
> „**jede** Änderung am Protokoll ist eine Revision — auch ein reiner Hash-Nachzug, auch
> eine Änderung, die inhaltlich nichts verschiebt". Rev. 40 hat den Nachzug **angekündigt**;
> vollzogen worden ist er **nach** dem Revisions-Commit, weil die Instrumente erst danach
> repariert wurden. Wäre er unter derselben Nummer vollzogen worden, stünde der in dieser
> Tabelle bezeugte Bytestand von Rev. 40 **in keinem Dokument mehr** — genau der Ausfall aus
> C6b-2b, aus dem Rev. 36 diese Regel gemacht hat.
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> e94150ae6e433fdd7f43da6b309ec4e6d11d1d6e40873e65dce4c63267218e78  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **Keine Rechenregel und kein Marker ist verschoben** (§0.1 Punkt 6). Belege:
> `c11a_bericht_diagnose.md` §7, `c11b_bericht_zweiter_lauf.md`,
> `tests/fixtures/harness/EXPECTED.md` §11–§15 (**vor** der Reparatur allein committet),
> Protokoll §0.1 Zeile Auswertungsinstrumente, Revisionshistorie Rev. 41 und §10 Zeile 41.

> **Nachtrag 28.08.2026 (C11c) — der Protokoll-SHA ist erneut nachgezogen; der Wert von
> Rev. 41 steht gestrichen darüber.** Das Amendment **Rev. 42** erklärt die Forderung nach
> **Median und Spannweite über drei Läufe** für die **P/R/F1-Tabelle** als **gegenstandslos
> und damit erledigt** — sie wird nicht abgewiesen: `strict` ist nach Spezifikation §3 ein
> **Existenzquantor über die Repetitionen** und hat konstruktiv keine Verteilung über Läufe;
> eine laufweise Fassung wäre eine **neue Metrikdefinition** und ist nach §0.1 Punkt 2
> gesperrt. Die Laufstreuung steht seit **Rev. 40** je Repetition einzeln in der
> T4-Läufespalte. **Mitgezogen** ist der SHA der Auswertungsspezifikation an beiden Stellen:
> ~~`be3491e2…acb21d6e1`~~ → **`fe991be6…092c20d1`**.
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 6988a93bfe466b8014f9052f2345485d1733d3b133e200e2178eba33f5714e2b  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **Keine Metrikdefinition, kein Manifest, keine Regeldatei, kein Prompt, kein Schema ist
> berührt, und kein Re-Run folgt daraus** — keine Zelle rechnet anders. Belege:
> `c11c_bericht_dritter_lauf.md`, `c6_auswertungsspezifikation.md` §7.5 Punkte 1, 2 und 5,
> Protokoll Revisionshistorie Rev. 42 und §10 Zeile 42.

> **Nachtrag 28.08.2026 (C11c, zweiter Schritt) — der Protokoll-SHA ist ein weiteres Mal
> nachgezogen; der Wert von Rev. 42 steht gestrichen darüber.** Das Amendment **Rev. 43**
> ist ein **reiner Hash-Nachzug** der Auswertungsinstrumente nach der
> **Darstellungsreparatur D1–D3**: `tools/evaluate_campaign.py` ist geändert,
> `tools/match_k4k5.py` und `tools/check_doc_invariants.py` sind unberührt.
>
> **Eine eigene Revision, obwohl reiner Bytestandsnachzug** — §0.1 Punkt 5. Unter Rev. 42
> vollzogen, stünde der in dieser Tabelle bezeugte Bytestand von Rev. 42 **in keinem
> Dokument mehr**; dieselbe Trennung wie zwischen Rev. 40 und Rev. 41.
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 759b11ede90232c2e3e8ce7d7e0149a9db7726d5cc87e35da7ceddb4369343f4  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **KEINE Rechenregel, KEIN Filter, KEIN Nenner und KEINE Aggregationsstufe ist berührt**
> (§0.1 Punkt 6) — verschoben ist allein die **Notation**: Markerauszeichnung und
> Exponentialschreibweise, auf bereits gerechnetem Text. Belege:
> `c11b_bericht_zweiter_lauf.md` §7, `c11c_bericht_dritter_lauf.md` §3 und §5, Protokoll
> §0.1 Zeile Auswertungsinstrumente, Revisionshistorie Rev. 43 und §10 Zeile 43.

> **Nachtrag 28.08.2026 (C14) — der Protokoll-SHA ist erneut nachgezogen; der Wert von
> Rev. 43 steht gestrichen darüber.** Das Amendment **Rev. 44** stellt die **Artefaktauswahl
> auf das Laufverdikt** (Auswertungsspezifikation §1.9 neu, dazu die Zusicherung **R12**),
> registriert die **Overlap-Tabelle T10** (Skelett T10, Spezifikation §8 Punkt 10) und zieht
> den seit **Rev. 42** überholten T5-Vermerk im **Renderer** nach.
>
> **Der Anlass ist die Defektklausel §0.1 Punkt 6, und der Defekt ist ungeschminkt benannt:**
> die bisherige Auflösungsregel las für **elf** K3-Injektionen ein Artefakt, dessen
> Laufmanifest `INVALID` trägt — die von §7 ausgeschlossene „stille Zählung invalider Läufe
> als ‚0 Findings‘", **während T7 die Gültigkeit korrekt auswies**. **Die Reparatur wird die
> K3-Zahlen voraussichtlich verbessern**; tragend sind die Vorregistrierung der verletzten
> Regel, der Fundweg über eine vor dem Befund beauftragte Auszählung (C11d §A6b), dass es
> eine **Artefaktauswahl und keine Metrikänderung** ist, und dass **C11–C13 archiviert
> bleiben** und gegenübergestellt werden.
>
> **Mitgezogen** ist der SHA der Auswertungsspezifikation an **beiden** Stellen:
> ~~`fe991be6…092c20d1`~~ → **`39822edc…d2cd71c7`**. Die drei Instrumentenhashes in §0.1
> werden nach der Implementierung derselben Auftragsphase **gesondert** nachgezogen — nach
> §0.1 Punkt 5 eine eigene Revision.
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> ba865b2bed9dd7f1a4bddad40f587e8a81df165222ecc2f7a3d14d09aa18309b  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **Keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein Prompt, kein
> Schema ist berührt** — bewegt hat sich, **welche Datei** dieselbe Metrik liest. Belege:
> `c11d_bericht_befund08_grundlagen.md` §A6b, §A6.1 und §B5, Protokoll §7, §8 UF3,
> Revisionshistorie Rev. 44 und §10 Zeile 44, Auswertungsspezifikation §1.9 und §8 Punkt 10.

> **Nachtrag 28.08.2026 (C14, zweiter Schritt) — der Protokoll-SHA ist ein weiteres Mal
> nachgezogen; der Wert von Rev. 44 steht gestrichen darüber.** Das Amendment **Rev. 45**
> ist ein **reiner Hash-Nachzug** der Auswertungsinstrumente nach der Umsetzung von
> **R11–R14**: `tools/evaluate_campaign.py` ist geändert, `tools/match_k4k5.py` und
> `tools/check_doc_invariants.py` sind unberührt.
>
> **Eine eigene Revision, obwohl reiner Bytestandsnachzug** — §0.1 Punkt 5. Unter Rev. 44
> vollzogen, stünde der in dieser Tabelle bezeugte Bytestand von Rev. 44 **in keinem
> Dokument mehr**; dieselbe Trennung wie zwischen Rev. 40 und Rev. 41 und zwischen Rev. 42
> und Rev. 43.
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 0ce57d29110214d13e888e44750b6ee3ae1e5a934aebaeb116883d005ff92eca  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **KEINE Rechenregel, KEIN Filter, KEIN Nenner und KEINE Aggregationsstufe ist berührt**
> (§0.1 Punkt 6) — bewegt hat sich, **welche Datei** dieselbe Metrik liest, und dass eine
> bereits gerechnete Zelle in **T10** ein zweites Mal, schnittweise, ausgewiesen wird.
> Belege: `tests/fixtures/harness/EXPECTED.md` §16 (**vor** der Umsetzung allein
> committet), `c14_bericht_vierter_lauf.md` §3 und §5, Protokoll §0.1 Zeile
> Auswertungsinstrumente und Punkt 6, Revisionshistorie Rev. 45 und §10 Zeile 45.

> **Nachtrag 28.08.2026 (C11b) — der Protokoll-SHA ist erneut nachgezogen; der Wert von
> Rev. 39 steht gestrichen darüber.** Das Amendment **Rev. 40** bildet **kein-EN auf EINER
> Aggregationsstufe** — der **Existenzstufe** —, führt in T4 die **Läufespalte** mit den drei
> Repetitionswerten einzeln ein und **lehnt** eine Aufspaltung von kein-EN **nach Ursache**
> ausdrücklich ab. Mitgezogen ist der SHA der Auswertungsspezifikation (§7.5 (3) präzisiert,
> §7.5 (5) und (6) neu) an **beiden** Stellen; die drei Instrumentenhashes in §0.1 werden nach
> der Reparatur derselben Auftragsphase gesondert nachgezogen.
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 736290279992f863682b29fc02ef44f27a41d27093c52a00f04175f494da2956  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **ZEITPUNKT UNGESCHMINKT: gesetzt NACH dem ersten Auswertungslauf und NACH der Diagnose
> C11a.** Zulässig als **Metrikbildung, nicht Metrikdefinition** — die Regel aus Rev. 31 bleibt
> wörtlich, `strict`, `localized`, Precision, Recall, F1, Median, Spannweite und FP-Rate stehen
> unverändert. **Der erste Auswertungslauf** (`data/campaign/eval/c11_eval_full.*`) **bleibt
> archiviert, gehasht und unverändert**; er wird nach §0.1 Punkt 6 dem zweiten Lauf
> Zelle für Zelle gegenübergestellt, nicht ersetzt. Belege: `c11a_bericht_diagnose.md` §3,
> `c11b_bericht_zweiter_lauf.md`, Protokoll §0.1, Revisionshistorie Rev. 40 und §10 Zeile 40.

> **Nachtrag 28.08.2026 (C6c-a) — der Protokoll-SHA ist erneut nachgezogen; der Wert von
> Rev. 38 steht gestrichen darüber.** Das Amendment **Rev. 39** stellt **T7 auf die
> gehashten Laufmanifeste** unter `data/campaign/manifests/` (`journal.jsonl` und die
> Prosa-`MANIFEST.md` sind seither **Gegenprobe, nicht Quelle**), **entscheidet** die
> sieben ungelisteten **lebenden Dokumente** als **Ausnahme statt Fehlschlag** — sie
> bleiben ungehasht, ihre Liste steht namentlich im Prüfer, eine **achte** ungelistete
> Datei ist ein Fehlschlag — und **präzisiert die Blindheitsauflage**: Funde bleiben
> gesperrt, die Laufmanifeste sind ausdrücklich erlaubt, und die Selbstauditierung prüft
> jetzt gegen eine **positive** Erlaubnisliste. Mitgezogen sind der SHA der
> Auswertungsspezifikation (§1.8, §7.4, §8 Punkt 9) an beiden Stellen und **zwei der
> drei Instrumentenhashes** in §0.1 — `tools/evaluate_campaign.py` und
> `tools/check_doc_invariants.py` sind geändert, `tools/match_k4k5.py` ist unberührt.
> Gemessen am 28.08.2026 nach der Protokolländerung:
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 9e63c37067a5a62ef95dd2d0710620939b9f03e5b0258995f01e597db5653f48  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **Gesetzt vor dem ersten Auswertungslauf** über `data/campaign/k*`. **Kein Messwert
> bewegt sich** — dieselben T7-Zahlen werden aus einer anderen, **bezeugten** Datei
> gelesen; alle drei Lesungen (Laufmanifeste, Journal, Prosa-Manifeste) sind
> deckungsgleich. Belege: `c6ca_bericht_t7_quellen.md`, Protokoll §0.1 (Zeile
> **T7-Quelle**, Zeile Auswertungsinstrumente, Punkt 7), Revisionshistorie und §10
> Rev. 39.

> **Nachtrag 28.08.2026 (C6c, zweiter Schritt) — der Protokoll-SHA ist ein weiteres Mal
> nachgezogen; der Wert von Rev. 37 steht gestrichen darüber.** Das Amendment **Rev. 38**
> nimmt die drei **Auswertungsinstrumente** mit SHA256 in den Messstand auf —
> `tools/evaluate_campaign.py`, `tools/match_k4k5.py` und `tools/check_doc_invariants.py`,
> der sich damit **selbst mitregistriert** — und legt als Punkt 6 der Amendment-Regel
> fest, dass ab dem ersten Auswertungslauf jede Änderung an ihnen eine datierte Revision
> mit Begründung ist, keine eine Rechenregel oder einen Marker verschieben darf und
> allein die Behebung eines Defekts zulässig bleibt, mit vollständiger Neuauswertung und
> Ausweis beider Ergebnisse. Gemessen am 28.08.2026 nach der Protokolländerung:
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 06a36473719dd3b27e9337a55b2ca1a6df5d5a3cd7357570eb7b66c347cec7fc  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **Warum es dieses Amendment braucht:** der Messstand bezeugte den **Eingang** und, über
> die Bewegungsprüfung, Protokoll und Auswertungsspezifikation — **nicht** den Weg
> dazwischen. Eine stille Änderung an einer Rechenregel verschöbe **jede** Tabelle des
> Kapitels 7, ohne dass ein registrierter Wert sich bewegte. **Gesetzt vor dem ersten
> Auswertungslauf** über `data/campaign/k*`. Belege: `c6c_bericht_selbsttest_freeze.md`,
> Protokoll §0.1 (Zeile Auswertungsinstrumente und Punkt 6), Revisionshistorie und §10
> Rev. 38.

> **Nachtrag 28.08.2026 (C6c) — der Protokoll-SHA ist erneut nachgezogen; der Wert von
> Rev. 36 steht gestrichen darüber.** Das Amendment **Rev. 37** entscheidet eine
> **Zweideutigkeit** zwischen zwei vorregistrierten Formulierungen: §7.2 der
> Auswertungsspezifikation verlangte, die beiden vorregistrierten Meldungen des
> Clean-Control-Sets aus dem Zähler der Headline-Rate **herauszurechnen**, während die
> Ergebniszeile des K2-Berichts sie „getrennt **darin** enthalten" führt. **Entschieden:
> sie bleiben im Zähler und werden getrennt ausgewiesen.** Gemessen am 28.08.2026 nach der
> Protokolländerung:
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> bb99fd8e3bff101714ed4d302879807d2ba90003d1ff9a3009c4b434ff01a3e5  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **Der Zeitpunkt ist der Punkt:** auf dem Kontrollbestand ergeben beide Lesarten
> **denselben Wert 49**, im Harness-Fixture **3/6 gegen 4/6** — die Entscheidung fällt
> **vor ihrer ersten wirksamen Anwendung**, der Auswertungslauf über `data/campaign/k*`
> hat nicht stattgefunden. **Keine Metrikdefinition ist geändert:** der Zähler ist seit
> Rev. 3 „Zahl der Kontrollmodule mit ≥ 1 Finding", und die entschiedene Lesart ist dessen
> wörtliche Anwendung. Mitgezogen ist der SHA256 der **Auswertungsspezifikation** an
> beiden registrierten Stellen (§0.1 und §1 Nachtrag Rev. 30), im selben Commit. Belege:
> `c6c_bericht_selbsttest_freeze.md`, Protokoll §0.1, Revisionshistorie und §10 Rev. 37.

> **Nachtrag 27.08.2026 (C5c) — der Protokoll-SHA ist nachgezogen, der alte Wert steht
> gestrichen darüber.** Das Amendment Rev. 34 zieht die **Archivwurzel** in §0.1 von
> `/home/haasentimo/scratch/c7/out` nach `~/ma/masterarbeit/data/campaign/` und die **Runner**-Zeile
> auf den Commit, der diese Änderung trägt. Beides ist **Ablage**, nicht Messung: keine Messgrösse,
> kein Messeingang, keine Metrik, keine Matrixzelle — und die Änderung liegt **vor dem ersten
> Kampagnenlauf**. Gemessen am 27.08.2026 nach der Protokolländerung:
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 013ddc0341d647afaebede0c300c8808e19f00a5cc8dad30b685847a48d6899f  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> Der Wert oben (`2cb0385f…17ac181e`) bleibt als
> **Anker des Freeze-Standes Rev. 33** stehen und ist weiterhin der Wert, gegen den die
> Vorregistrierung selbst zu prüfen ist; `013ddc03…48d6899f` bezeugt den Stand
> **mit** dem Amendment. Belege: `c5c_bericht_archivwurzel.md`, Protokoll §0.1 und §10 Rev. 34.

> **Nachtrag 27.08.2026 (C10a) — der Protokoll-SHA ist erneut nachgezogen; beide älteren
> Werte stehen gestrichen darüber.** Das Amendment **Rev. 35** führt **Validator-Punkt (6)**
> („sole importer per component") commit-scharf: der Punkt zählt Kanten des **Codegraphen** und
> ist unter einer `FORBIDDEN_RELATION`-Injektion auf `core_adapters_internal` zwangsläufig
> verletzt (I07, I08, I09) — der Kampagnenlauf C10 brach deshalb an I07 ab. Erwartet wird jetzt
> die **exakte Importeursmenge**, berechnet aus dem Soll-Whitelist-Importeur plus der
> registrierten Kante; die Prüfung wird damit **schärfer**, nicht lockerer. Mitgezogen: die
> **Runner**-Zeile in §0.1 auf `4caf083`. **Anders als Rev. 34 liegt dieses Amendment NACH dem
> ersten Kampagnenlauf** — sechs K2-Invocationen sind deshalb verworfen und werden neu gefahren
> (`c10a_bericht_validator_punkt6.md`). Berührt sind **weder Metrik noch Manifest, Regeldatei,
> Prompt oder Schema**. Gemessen am 27.08.2026 nach der Protokolländerung:
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 876680b13c568312059d9143b146617b3be6887e5e89a2badfd05c5361f3b910  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> Der Anker der Vorregistrierung bleibt `2cb0385f…17ac181e` (Rev. 33). `013ddc03…48d6899f`
> bezeugt den Stand mit Amendment Rev. 34, der Wert oben den Stand mit Rev. 34 **und** Rev. 35.
> Belege: `c10a_bericht_validator_punkt6.md`, Protokoll §0.1 und §10 Rev. 35.

> **Nachtrag 27.08.2026 (C6b-0a) — der Protokoll-SHA ist erneut nachgezogen, und dazwischen
> steht ein Stand, der NIE eine Revision war.** Der Auftrag **C6b-2b** (Commit `0c1cc34`) hat
> den SHA der **Auswertungsspezifikation** im Protokoll nachgezogen — an beiden vorgeschriebenen
> Stellen, §1 und §0.1, im selben Commit wie die Spezifikationsänderung. **Dieser Nachzug war
> richtig.** Er hat aber die **Bytes des Protokolls** verändert, **ohne** Kopf-Revision, ohne
> Historieneintrag und ohne §10-Zeile — und **ohne Nachzug in dieser Tabelle**. Der Bytestand
> `620f1173…283d80d3` war damit **in keinem Dokument bezeugt**; er steht jetzt oben als
> Zwischenzeile, ausdrücklich **ohne Revisionsnummer**.
>
> **Aufgefallen ist es an der Bewegungsprüfung von C6b**, die den Protokoll-SHA gegen den hier
> als aktuell geführten Wert vergleicht: sie schlug an, und der Auftrag brach ab, bevor eine
> Zeile Harness geschrieben war. **Die Prüfung hat funktioniert — ihr fehlte der
> Vergleichswert.**
>
> Das Amendment **Rev. 36** registriert diesen Bytewechsel nachträglich und schreibt die Lesart
> fest, die ihn künftig ausschliesst (Protokoll §0.1 Punkt 5): **jede Änderung am Protokoll ist
> eine Revision, auch ein reiner Hash-Nachzug** — weil eine Ausnahme für „inhaltsneutrale"
> Bytewechsel ein Urteil darüber verlangte, welche Änderung substanziell ist, und weil der
> Protokoll-SHA als Detektor nur taugt, wenn kein Bytewechsel unregistriert bleibt. Gemessen am
> 27.08.2026 **nach** der Protokolländerung und **vor** dem Eintrag dieser Zeile:
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 1240f47ebfc1b89f25068f8cc68190e7d0f54f6ad18ce10e470b74c7fb4a975e  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> Der Anker der Vorregistrierung bleibt `2cb0385f…17ac181e` (Rev. 33). Ab jetzt wacht
> `tools/check_doc_invariants.py` maschinell darüber, dass Protokoll-SHA und diese Tabelle nicht
> auseinanderfallen und dass Kopf-Revision, §10 und Revisionshistorie dieselbe Nummer tragen.
> Belege: `c6b0a_bericht_invarianten.md`, `c6b2_bericht_matchregel.md`, Protokoll §0.1 Punkt 5
> und §10 Rev. 36.

> **Nachtrag 31.08.2026 (G1, Gate-Notiz) — der Protokoll-SHA ist nachgezogen; der Wert von
> Rev. 45 steht gestrichen darüber.** Das Amendment **Rev. 46** streicht in **§7** die
> Kürzungsreihenfolge „zuerst Z4 (Transfer-Demonstration), dann erst Z2" als **überholt**
> (Alttext durchgestrichen sichtbar) und nimmt den **Ausgang des Gates** als Vermerk unter
> die Regel auf: geprüft und entschieden am Stichtag **31.08.2026**, **Kriterium erfüllt,
> Variante C bleibt, Z2 fällt nicht**.
>
> **Warum überhaupt eine Revision.** §0.1 Punkt 5: „**jede** Änderung am Protokoll ist eine
> Revision — auch ein reiner Hash-Nachzug, auch eine Änderung, die inhaltlich nichts
> verschiebt". Der Bytestand hat sich bewegt, also bewegt sich die Nummer und diese Tabelle
> mit ihr. Gemessen **nach** der Protokolländerung und **vor** dem Eintrag dieser Zeile:
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 96c89358a198fb230f686204f4138dd7c1c0a04e6c142f56216c6605c0fe74e2  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **KEINE Metrikdefinition, KEIN Injektionsmanifest, KEINE Regeldatei, KEIN Prompt und KEIN
> Schema ist berührt; kein Re-Run folgt** — §7 ist die Entscheidungs- und Stop-Regel-Sektion,
> bewegt hat sich eine **Scope-Klausel**. Messstand §0.1, Matching-Regel §4, Metriken §5 und
> Ablauf §6 sind unberührt; die drei Instrumentenhashes stehen unverändert auf den Werten von
> Rev. 45. Belege: `docs/planung/gate_notiz_2026-08-31.md`, Protokoll §7,
> Revisionshistorie Rev. 46 und §10 Zeile 46, `g1_bericht_gate.md`.

> **Nachtrag 31.08.2026 (Z1-P) — der Protokoll-SHA ist erneut nachgezogen; der Wert von
> Rev. 46 steht gestrichen darüber.** Das Amendment **Rev. 47** ist ein **reiner
> Hash-Nachzug** an einem Auswertungsinstrument: `tools/check_doc_invariants.py` hat die
> **Invariante (F)** aufgenommen — SHA256 des Z1-Protokolls
> `docs/protokolle/z1_protokoll_extraktionsvergleich.md` gegen den in
> `z1_p_bericht_freeze.md` §3 als aktuell geführten Wert. `tools/evaluate_campaign.py` und
> `tools/match_k4k5.py` sind unberührt.
>
> **Warum eine eigene Revision.** §0.1 Punkt 5: „**jede** Änderung am Protokoll ist eine
> Revision — auch ein reiner Hash-Nachzug". Unter Rev. 46 vollzogen, stünde der in dieser
> Tabelle bezeugte Bytestand von Rev. 46 **in keinem Dokument mehr**; dieselbe Trennung wie
> zwischen Rev. 40 und Rev. 41, Rev. 42 und Rev. 43, Rev. 44 und Rev. 45.
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> 71d30352834e519ae019ecc8e947a452a906f4559186452cb6243a4bf718811a  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **KEINE Rechenregel, KEIN Marker und KEINE Metrikdefinition ist berührt; kein Re-Run
> folgt.** Die Invarianten (A)–(E) stehen wörtlich unverändert und liefern zeichengleiche
> Ausgaben; der Prüfer ist ausschliesslich lesend und rechnet keine Kennzahl. Was sich
> bewegt hat, ist die Zahl der geprüften Invarianten: **fünf → sechs**. Belege:
> `z1_p_bericht_freeze.md`, Protokoll §0.1 Zeile Auswertungsinstrumente, Revisionshistorie
> Rev. 47 und §10 Zeile 47.

**Der Wert bezeugt den Stand nach Commit 1 und ist der Anker der Vorregistrierung.** Jede
spätere Änderung am Protokoll ändert ihn; genau das ist der Zweck. Er ist bewusst **nicht**
in das Protokoll selbst eingetragen — der Eintrag hätte ihn ungültig gemacht.

---

> **Nachtrag 01.09.2026 (N07) — der Protokoll-SHA ist erneut nachgezogen; der Wert von
> Rev. 47 steht gestrichen darüber.** Das Amendment **Rev. 48** trägt **einen neuen Eintrag
> T15** in das Threat-Register §9; T1 bis T14 stehen **unverändert**.
>
> **T15 — die Ausführungsgeometrie des Inferenzservers** (`n_ctx` / `-c`, die daraus
> abgeleitete Batchgrösse `-b`/`-ub`, die KV-Cache-Geometrie) **bewegt die Ausgabe und ist in
> keinem Laufrecord bezeugt.** Belegt aus zwei Diagnoseläufen **ausserhalb** dieses
> Messstands (`z1_s_bericht_diagnoselauf.md` §6–§8; `data/z1_s_diagnose/`, 51 Dateien,
> `sha256sum -c` Exit 0): dieselbe Maschine, dieselbe Ollama-Fassung **0.30.10**, derselbe
> Modell-Blob, **token-für-token derselbe Erstprompt** (4 095 IDs), `temperature=0` und
> `seed=0` — und **verschiedene Ausgabe**, 1 517 gegen 2 261 Zeichen; der eine Lauf gültig
> mit 0 Fehlern, der andere ungültig mit 14. Verändert war allein `-c 4096` gegen `-c 16384`
> samt der abgeleiteten `-b`/`-ub` 512 gegen 1024 und 224 gegen 896 MiB KV-Cache.
>
> **DIE ABGRENZUNG GEHÖRT ZUM EINTRAG: die Vergleichbarkeit innerhalb der Kampagne ist
> UNBERÜHRT.** Alle K2-Läufe liefen auf demselben **gemessenen** Fenster `CONTEXT 4096`
> (§1 Nachtrag Rev. 26), das Nachlaufskript prüfte es **je Call**, und die Prompts lagen mit
> Median **1 346** und Maximum **1 948** Token weit darunter. **Kein Messergebnis ist
> betroffen, keine Metrik, keine Zelle der Erwartungsmatrix.** Was nach dieser Messung
> **nicht** mehr behauptet werden kann, ist **Reproduzierbarkeit auf einer anders
> konfigurierten Serverinstanz**. Die Entscheidung aus **Rev. 26**, `num_ctx` **nicht** zu
> setzen, war **richtig und bleibt unangetastet** — ein Eingriff hätte den eingefrorenen
> Messpfad bewegt.
>
> **Ein Amendment, das BESCHREIBT und nicht festlegt** — zulässig nach §0.1 Punkt 2 auch nach
> Messbeginn. **Keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein
> Prompt und kein Schema** ist berührt; die drei Instrumentenhashes stehen zeichengleich auf
> den Werten von Rev. 47.
>
> ```
> $ sha256sum docs/protokolle/eval_protokoll_phase04.md
> fd0a6b4e6638022e70da6d8ff5f0cd66930a6264d63fa4db0e02bc222ca899b0  docs/protokolle/eval_protokoll_phase04.md
> ```
>
> **Kein Re-Run** — keine Zelle rechnet anders. Belege: Protokoll §9 (Amendment Rev. 48),
> Revisionshistorie Rev. 48 und §10 Zeile 48; Z1-Protokoll §9 T-Z1-11 (Rev. 6);
> `z1_s_bericht_diagnoselauf.md`; `n07_bericht_nachtrag.md`.

## 4. Teil 3 — zwei Klarstellungen, keine neuen Festlegungen

### 4a. §6 — der Graphmodus-Nachtrag Rev. 31 ist auf K1 eingeschränkt

**Setup.** Der Nachtrag Rev. 31 zu §6 schreibt die Ableitungsregel generisch:
„`category_l1` des Manifesteintrags → `full` bei `CYCLE`, sonst `diff`", **ohne die
Konfiguration zu nennen**. Der Absatz, den er präzisiert, heisst in §6 Rev. 7 ausdrücklich
„Graphmodus je Kategorie **für K1**" — die Einschränkung war also da, ist aber im Nachtrag
verlorengegangen.

**Resultat.** Wörtlich gelesen deckte der Nachtrag **12** Full-Läufe: K1, K2 und K3 auf
I13–I16. Gemeint und überall sonst festgelegt sind **4**. Der Wortlaut ist präzisiert;
verbindlich ist ab Rev. 33:

- **K1** — `full` bei `category_l1 == CYCLE`, sonst `diff`, aus dem Manifesteintrag
  abgeleitet und je Lauf ins Laufmanifest geschrieben (Rev. 31, unverändert).
- **K2/K3** — **immer** `--rule-graph diff`, für alle 32 Injektionen, ohne Ableitung. So
  steht es seit §6 Rev. 24 in beiden Aufrufzeilen; §4 Nachtrag Rev. 25 ruht darauf (der
  deterministische Pfad läuft in K2/K3-Läufen mit, **weil** dort `diff` steht), ebenso die
  konstruktionsbedingte `CYCLE`-Nullzeile für K2/K3 (§6 Rev. 7, Absatz „Asymmetrie").
- **K4/K5** — kennen den Schalter nicht; Modus `n/a`.

**Belege, beide nachgezählt statt behauptet:**

1. **C5-Planausgabe** über alle 160 Invocations
   ([c5_bericht_freeze.md](c5_bericht_freeze.md) §8): **4 × `--rule-graph full`** (K1 auf
   I13–I16, den vier `CYCLE`-Injektionen), **92 × `--rule-graph diff`** (K1 auf den übrigen
   28, K2 und K3 auf allen 32). 4 + 92 = 96 = die drei LLM-fähigen Konfigurationen × 32; die
   64 K4/K5-Invocations tragen keinen Modus.
2. **C4c Teil B** ([c4c_bericht_vorabpruefung.md](c4c_bericht_vorabpruefung.md)): I01–I12 mit
   `diff`, I13–I16 mit `full` gefahren; die 16-von-16-Gegenprobe attestiert die Kampagne
   **nur unter genau dieser Zuordnung**.

Dazu die Implementierung, die schon so gebaut ist:
[tools/campaign_spec.py:73-75](../../tools/campaign_spec.py#L73-L75) liefert den Modus aus
`category_l1`, und [tools/run_campaign.py:111-112](../../tools/run_campaign.py#L111-L112)
setzt ihn **nur für K1** — für K2/K3 fest auf `"diff"`, für K4/K5 auf `None`.

**Konsequenz.** **Die Festlegung ändert sich nicht.** Sie stand so in §6 Rev. 7, ist so
gegengeprüft (C4c), so geplant (C5) und so implementiert (C7). Präzisiert ist der
**Protokolltext**, der als einzige der vier Stellen generisch formuliert war. Ohne die
Präzisierung hätte das eingefrorene Protokoll eine Aussage getragen, die von der geplanten,
gegengeprüften und implementierten Kampagne abweicht — und das ausgerechnet an der Stelle,
an der ein abweichender Modus die Records-Menge für I13–I16 **stumm** auf null fallen liesse
(Rev. 31, Begründung).

### 4b. §1 — die K3-Zeile der Konfigurationsmatrix

**Setup.** Zu prüfen war, ob die Zeile „nemotron-120B (OpenRouter)" gestrichen ist und die
Direktzugangszeile daneben steht (Rev. 30/32). Wenn nicht: nachziehen.

**Resultat — sie stand nicht so.** Die Tabellenzeile lautete unverändert und
**ungekennzeichnet**:

```
| K3 | triton-conformance, LLM-Checker, nemotron-120B (OpenRouter) | strukturell + semantisch | 3 |
```

Der Nachtrag Rev. 30 weiter unten in §1 erklärt sie für überholt und schreibt, sie „bleibt
gestrichen stehen" — **gestrichen war sie nie**: Rev. 30 hat den Nachtrag geschrieben und
die Tabellenzeile unangetastet gelassen. §6 Rev. 32 hat denselben Widerspruch für die
**Aufrufzeilen** aufgelöst (dort trugen beide K3-Blöcke noch OpenRouter-Endpunkt, -Slug und
`CONFORMANCE_PROVIDER_PIN`), aber die **Matrix** nicht berührt. Das Protokoll behauptete
seither an einer Stelle eine Streichung, die an der anderen nicht vollzogen war.

**Nachgezogen.** Die alte Zeile steht jetzt vollständig durchgestrichen, die verbindliche
Direktzugangszeile daneben:

```
| ~~K3~~ | ~~triton-conformance, LLM-Checker, nemotron-120B (OpenRouter)~~ | ~~strukturell + semantisch~~ | ~~3~~ |
| K3 | triton-conformance, LLM-Checker, `nvidia-nemotron-3-super-120b` — **DigitalOcean-Direktzugang**, `https://inference.do-ai.run/v1`, **kein** `CONFORMANCE_PROVIDER_PIN` | strukturell + semantisch | 3 |
```

Darunter steht ein Vermerk, der den Befund benennt statt ihn zu glätten: dass die Streichung
in Rev. 30 **behauptet, aber nicht vollzogen** war.

**Konsequenz.** **Keine Festlegung geändert.** Verbindlich ist der Direktzugang seit Rev. 30
(§1 Nachtrag Rev. 30, Base-URL, Modell, kein Pin — letzteres B32: ohne Router gibt es nichts
zu pinnen), und der Kontrolllauf ist bereits über ihn gefahren
([c3b_k3_bericht_kontrolllauf.md](c3b_k3_bericht_kontrolllauf.md) §2, `model_version`
zeichengleich in 156/156 Calls). Korrigiert ist allein der **Aufschrieb** — dieselbe
Richtung wie bei der K5-Aufrufzeile in Rev. 32.

**Dass dies der zweite Fund dieser Art in zwei Aufträgen ist, ist selbst ein Befund:** ein
Nachtrag, der eine Streichung *beschreibt*, vollzieht sie nicht. Die Prüfung galt in C5b
ausdrücklich der Tabelle, nicht dem Nachtrag — und nur deshalb ist es aufgefallen.

---

## 5. Führung der Änderungen an beiden Stellen

Repo-Regel: Änderungen an einem vorregistrierten Protokoll werden im **Kopf
(Revisionshistorie)** *und* in der **Amendments-Tabelle (§10)** geführt, nie nur an einer.

- **Kopf:** neuer Absatz „Rev. 33: **FREEZE ZUR VORREGISTRIERUNG**, gesetzt vor dem ersten
  Kampagnenlauf — …", unmittelbar vor dem Zweck-Block, in der Form der Absätze Rev. 30–32.
- **§10:** neue Zeile `| 33 | 27.08.2026 | … | … |` in der Revisionshistorie vor Freeze, mit
  allen vier Teilen (Gate-Entscheidung mit den ausgezählten Anteilen, §0.1 Messstand,
  Graphmodus-Klarstellung, K3-Matrixnachzug) und der Belegspalte.
- **§10 zusätzlich:** Sperrvermerk über der Tabelle „Amendments nach Messbeginn", weil dort
  ein späterer Eintrag geschrieben würde und die Sperre genau ihn betrifft.

Bestehender Text wurde **ergänzt, nicht ersetzt**. Der `git diff` von Commit 1 entfernt
**sechs** Zeilen, und jede davon steht durchgestrichen wieder im Dokument: die alte
Kopfzeile, die zwei Zeilen der §0-Einleitung, die zwei Zeilen von §0 Punkt 2 und die alte
K3-Matrixzeile. **178 Zeilen hinzugefügt, 6 ersetzt.**

---

## 6. Commits

| # | SHA | Message | Gestagte Pfade |
|---|---|---|---|
| 1 | `3e17f44` | `docs: freeze the evaluation protocol at rev 33` | `docs/protokolle/eval_protokoll_phase04.md` |
| 2 | *siehe `git log`* | `docs: record the frozen measurement state` | `docs/repo-kontext/c5b_bericht_protokoll_freeze.md` |

---

## 7. Abschlusshygiene

- **Kein `git push`.**
- **Kein `git add -A`**, kein `git add .`, kein `git commit -a` — gestaged wurden
  ausschliesslich die beiden im Auftrag genannten Pfade, je Commit einer.
- **Keine Trailer** in den Commit-Messages.
- **Schreibend war nur `masterarbeit`.** In `tritongraph`, `tritongraph-measure` und
  `ma-conformance-testrepo` wurde ausschliesslich **gelesen** (`rev-parse`, `tag -l`,
  `log`, `sha256sum`) — kein Commit, kein Tag, kein Checkout, kein Build, kein Werkzeuglauf.
- **Kein Modell-Call, kein Messlauf.** Die Zahlen in §1 stammen aus **archivierten**
  Artefakten des Bestands C3b.
- `data/soll/` wurde nicht verändert; `SHA256SUMS` und `MANIFEST.md` sind daher
  unangetastet und weiter gültig (7 von 7 OK).

---

## 8. Nicht Gegenstand dieses Auftrags

Die Kampagne selbst, C6b/C6c, C4d, Standdokument Rev. 11, die offenen Punkte, Befund 08 und
der Arbeitsplan. **Ausdrücklich weiter offen:** der Punkt „C5b" im Sinne des `git bundle`
des Freeze-Stands in `offene_punkte.md` — ein anderer Punkt gleichen Namens, von diesem
Auftrag nicht berührt.
