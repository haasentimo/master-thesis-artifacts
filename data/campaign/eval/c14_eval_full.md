# C14 — Ausgabekopf (Laufidentifikation)

Dieser Kopf ist dem unveränderten Rendering vorangestellt; darunter beginnt die
Harness-Ausgabe bytegleich mit ihrer ersten Zeile.

- **Auftrag:** C14 — vierter Auswertungslauf über den vollständigen Messbestand, nach der Reparatur der Artefaktauswahl (R11), der Zusicherung R12, der neuen Overlap-Tabelle T10 (R13) und dem Textnachzug am T5-Vermerk (R14); Protokoll Rev. 44 (Registrierung) und Rev. 45 (Instrumenten-Hashes)
- **Zeitstempel:** 2026-08-28T23:49:10+02:00 bis 2026-08-28T23:49:10+02:00 (0:00.26 wall, 27308 KB maxrss)
- **cwd:** `/home/haasentimo/ma/masterarbeit`
- **git HEAD:** `8744a30f7312a3bc4b067059245b6e771bd0271c`
- **Maschine:** DESKTOP-PJA89CF · Linux 5.15.153.1-microsoft-standard-WSL2 x86_64
- **Aufrufzeile:** `python3 tools/evaluate_campaign.py --with-campaign --json-out data/campaign/eval/c14_eval_full.json --markdown-out data/campaign/eval/c14_eval_full.md`  → Exit 0

**Instrumente (SHA256) — NEU gebildet in Protokoll Rev. 45:**

- `tools/evaluate_campaign.py` — `b66be750f9b7cf524b9afa8edbab0138d17c409de4637465eb82d0f079a93428`
- `tools/match_k4k5.py` — `c16e7c4380034163f3034916193bd96cfc6bb957768fe610cb7018d7799f4ca6`
- `tools/check_doc_invariants.py` — `6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018`

**Protokoll (Rev. 45):** `0ce57d29110214d13e888e44750b6ee3ae1e5a934aebaeb116883d005ff92eca`  
**Auswertungsspezifikation:** `39822edc0d9c109d7f1c1cfc285af9dd1363ec48b1a96a69334c173cd2cd71c7`

**Messbestand `data/campaign/` (SHA256 des Block-`SHA256SUMS`, gelistete Artefakte) — gegenüber dem ersten, zweiten und dritten Lauf UNVERÄNDERT:**

| Block | SHA256 des `SHA256SUMS` | gelistete Artefakte |
| --- | --- | --- |
| control | `c9699b4417833a6a6a006ce51ce5062589c3c4a1266bb6ea5579539ac2b8fdda` | 14 |
| k1 | `ced9954f333936dc20630f91b275f63a47e7e69f9d530bf8a0abe5680ead6907` | 96 |
| k2 | `debd5a93309e682126de886928b6fcc1c9ba4e2dd9548d2037f33512ac1bb26e` | 96 |
| k3 | `7023d23663ba022dff98a4d888cde16e3f3b198849144344a6ba83a1281bfb88` | 183 |
| k4 | `cc8dbce674920d2a61f9954eca3fa6eb766e971705283f8ca4321fa9906f29d0` | 96 |
| k5 | `07ff89aaff4956afc2dfb3b88efa7b3fa548dcc8d4978c49a56677ba3b0d0741` | 96 |

Laufmanifeste unter `data/campaign/manifests/`: 189 JSON-Dateien.
Gelesene Dateien: **658**, davon **253** Kampagnen-Laufartefakte — **wie im zweiten und
dritten Lauf**. Die elf durch R11 neu gewählten K3-Artefakte treten **an die Stelle** von
elf zuvor gelesenen, sie treten nicht hinzu.

**Rohausgabe vor Kopfeinfügung (SHA256):**

- `c14_eval_full.json` — `c7c6d003946129f64b4ae7b180d1a251cf4e5c243ed9bf022918a22cd359280a`
- `c14_eval_full.md` — `759c72c89f2cf30ed60539ba02ac5fb0028d71ac5c81d407348e1b66dba8aa24`

Markdown: Kopf vorangestellt, Rendering danach bytegleich. JSON: ein Schlüssel
`c14_run_head` nach der öffnenden Klammer eingefügt, alle Ergebniswerte bytegleich.
Keine Zelle angefasst.

**Der erste, zweite und dritte Auswertungslauf bleiben unberührt daneben liegen** — sie
werden nicht überschrieben, nicht gelöscht und nicht nachbearbeitet (Protokoll §0.1
Punkt 6: vollständige Neuauswertung mit **Ausweis der Ergebnisse**, nebeneinander,
nicht ersetzend):

- `c11_eval_full.json` — `ad8f0483ffd2c261d8e33a21c425c5f6a492dedae0cc99c4e135dc56b371ea30`
- `c11_eval_full.md` — `3d4874842a5baf92d455c1140b4874d396550fe87c50714d537a15a0a0e595af`
- `c12_eval_full.json` — `12751c3e506e3f28d4d32c7c4a104e97c826dad4e71c83f00dc49d200b09f0c7`
- `c12_eval_full.md` — `afe28bc2d3d81da4b565d0b2f735745f09422f39523de2f44b27e2c80c921918`
- `c13_eval_full.json` — `873893e771f3dd8a1a195b283f874858990dcd27a75a1c348fa85a1c1914977c`
- `c13_eval_full.md` — `f8cd9c074353cefcfe52d55e0df06a76b41c3f4ff75164c3ee1e5777f414c8a2`

---

# Kapitel 7 — Ergebnistabellen (Ausgabe der Auswertungsharness)

**Erzeugt von `tools/evaluate_campaign.py`.** Struktur, Spalten, Reihenfolge und
Fussnoten folgen `docs/kapitel/kapitel7_tabellenskelette.md` unverändert;
Druckreihenfolge **T1, T7, T2, T3, T4, T5, T6, T8, T9**.

**Marker:** ` — ` nicht ausdrückbar (T1/T8, vorregistriert) · `n. b.` nicht bildbar
(vorregistriert) · `n. e.` nicht erhoben (aus T7) · *(leer)* von diesem Lauf nicht
eingesetzt. **Keine Zelle trägt 0, wo ein Marker gilt.**

---

## T1 — Erwartungsmatrix, Kategorie × Konfiguration (Soll gegen Ist)

**Soll gilt für `localized`. Für `strict` besteht keine Vorhersage** (Protokoll §3,
Amendment 11.08.2026). Die Soll-Spalten reproduzieren Protokoll §3 und werden
**nicht neu entschieden**; jede Abweichung ist ein **Befund**.

| Szenario (Ebene 2) | n | Soll K1 | Soll K4 | Soll K5 | Soll K2/K3 | Ist K1 | Ist K4 | Ist K5 | Ist K2 | Ist K3 | Abweichung |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `LAYER_BACK_CALL` | 3 | ja | ja | ja | ja | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |  |
| `LAYER_SKIP_CALL` | 3 | ja | ja | ja | ja | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |  |
| `PROTECTED_MODULE` | 3 | ja | ja | ja | ja | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |  |
| `INDEPENDENCE` | 3 | ja | ja | ja | ja | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |  |
| `CYCLE_SIBLING` | 3 | ja | ja | teilweise | nein | 3/3 | `n. b.` | 3/3 | ` — ` | ` — ` | K4 `n. b.` (kein Vergleich bildbar) |
| `CYCLE_PARENT_CHILD` | 1 | ja | nein | teilweise | nein | 1/1 | `n. b.` | 1/1 | ` — ` | ` — ` | K4 `n. b.` (kein Vergleich bildbar) |
| `MISSING_PORT_REFERENCE` | 4 | nein | nein | ja | ja | ` — ` | ` — ` | 4/4 | 4/4 | 4/4 |  |
| `FRAMEWORK_TYPE_IN_SIGNATURE` | 4 | nein | nein | nein | ja | ` — ` | ` — ` | ` — ` | 4/4 | 4/4 |  |
| `INCORRECT_LOCATION` | 4 | nein | teilweise | nein | ja | ` — ` | 4/4 | ` — ` | 3/4 | 4/4 | **K2: Soll ja / Ist teilweise** |
| `SIGNATURE_DEVIATION` | 4 | nein | nein | nein | ja | ` — ` | ` — ` | ` — ` | 4/4 | 4/4 |  |

**Die Spalte `Abweichung` ist gerechnet.** Verglichen wird die vorregistrierte
Soll-Zelle mit der Ist-Feststellung derselben Zeile, im Matrixvokabular
**`ja` / `teilweise` / `nein`** und über `localized` (für `strict` besteht keine
Vorhersage). **`ja`** = jede auswertbare Injektion des Szenarios ist erkannt ·
**`nein`** = keine · **`teilweise`** = ein Teil, **oder** die Erkennung liegt
allein auf der **Stelle** (vorregistrierte Klasse „richtige Stelle, falsche
Kategorie“, T9 Fall 6/7) — genau die Unterscheidung, aus der Fussnote 7 die
Zelle `teilweise` bildet. Eine ` — `-Zeile wird als **`nein`** gelesen, weil das
Soll dort auf Ausdrucksmächtigkeit beruht (Skelett, Lesehilfe zu T2).

> **EINE LEERE ZELLE IN DIESER SPALTE BEDEUTET: GERECHNET, KEINE ABWEICHUNG.** Sie
> ist **nicht** „nicht eingesetzt“. Das ist die einzige Spalte dieser Ausgabe, in
> der eine leere Zelle etwas aussagt, und sie steht deshalb namentlich in der
> Ausnahmeliste der Zusicherung R1. **Abweichungen werden AUSGEWIESEN, nicht
> aufgelöst** — die Soll-Spalten reproduzieren Protokoll §3 und werden hier nicht
> neu entschieden (Protokoll §7).

---

## T7 — Gültigkeit und Vollständigkeit des Messbestands

> **Diese Tabelle steht VOR T2, T4 und T5.** Sie rechtfertigt **jedes** `n. e.`
> dort. Ein `n. e.`, das hier keine Entsprechung hat, ist ein Harness-Fehler.

**Quelle: die gehashten Laufmanifeste** unter `data/campaign/manifests/`, ein
Manifest je Invocation, jedes von einem Block-`SHA256SUMS` bezeugt (Protokoll
Rev. 39). `journal.jsonl` und die Prosa-Manifeste sind **Gegenprobe, nicht Quelle**.

### T7.1 — Gültigkeit je Konfiguration

| Konfiguration | Invocationen | VALID | INVALID | Model-Calls | `calls_invalid` | `calls_transport_failed` | `valid_final`-Anteil | `skipped_count` | `invalid_reasons` (Werte) | Wiederholungen (`_r<n>`) |
|---|---|---|---|---|---|---|---|---|---|---|
| K1 | 32 | 32 | 0 | 0 | 0 | 0 | *(keine Model-Calls)* | 0 | *(keine)* | 0 |
| K2 | 32 | 32 | 0 | 96 | 0 | 0 | 96 / 96 = 1,000 | 0 | *(keine)* | 0 |
| K3 | 61 | 32 | 29 | 183 | 0 | 50 | 133 / 133 = 1,000 | 0 | `transport_failure` ×29 | 29 |
| K4 | 32 | 32 | 0 | 0 | 0 | 0 | *(keine Model-Calls)* | 0 | *(keine)* | 0 |
| K5 | 32 | 32 | 0 | 0 | 0 | 0 | *(keine Model-Calls)* | 0 | *(keine)* | 0 |

`valid_final` ist **kein Manifestfeld**, sondern hier abgeleitet: gemessene Calls
(`calls_total` − `calls_transport_failed`) minus `calls_invalid`. Der Anteil steht
über den **gemessenen** Calls (`outcome: measured`); die Transportausfälle stehen
**daneben, nie darin** (Skelett T7.1). `skipped_count` ist aus den Werten von
`invalid_reasons` gezählt — der Checker führt übersprungene Dateien dort als
`skipped_files`, ein eigenes Feld gibt es nicht. Die Vielfachheit hinter den
`invalid_reasons`-Werten zählt **Invocationen**, nicht Calls.

**Validitäts-Gate §7:** kein `valid_final`-Anteil unter 0,9.

**Gegenprobe `journal.jsonl` (append-only, keine gehashte Quelle):**

| Konfiguration | Invocationen Journal | gültige Injektionen Journal | Ergebnis |
|---|---|---|---|
| K1 | 32 | 32 | **deckungsgleich** |
| K2 | 32 | 32 | **deckungsgleich** |
| K3 | 61 | 32 | **deckungsgleich** |
| K4 | 32 | 32 | **deckungsgleich** |
| K5 | 32 | 32 | **deckungsgleich** |

### T7.2 — Zählregeln und positive Lauf-Akzeptanz

| Konfiguration | Regel | Erwartet | Gemessen | erfüllt |
|---|---|---|---|---|
| K1/K2/K3, Injektionslauf | `changed_files_count == 1` | 1 je Invocation | 1 in 125 von 125 Invocationen | **ja** |
| K1/K2/K3, Injektionslauf | `calls_total == 1 × runs` | K1: 1 · K2/K3: 3 | K1: 0 · K2: 3 · K3: 3 | **ja** (1) |
| K4 | ausgewertete Contracts `kept + broken` | 13 | 32 von 32 Aufrufen mit `kept + broken` = 13 | `n. b.` (2) |
| K5 | gesammelte Tests, Sammelphase fehlerfrei | 24 | 32 von 32 Aufrufen mit `collected` = 24 | **ja** |

(1) **Abweichung zum Skelettwortlaut bei K1:** der ausgeführte Akzeptanztest verlangt für K1 `calls_total == 0` (deterministischer Pfad, kein Modell) — `tools/postrun_check.py`, §6 Nachtrag Rev. 24/26. Gemessen ist 0. Beide Fassungen stehen hier nebeneinander; angeglichen wird keine.

(2) `erfüllt` ist im Skelett als `n. b.` vorregistriert — die Trefferzahl ist die Messung, geprüft ist allein die Vollständigkeit der Regelmenge.

**Warum diese Zeilen keine Formalie sind.** K4 und K5 schreiben **kein**
Laufprotokoll; ohne eine **positive** Aussage über den Lauf ist eine
Fehlkonfiguration, die die Regelmenge verkürzt, **unsichtbar** — sie erzeugt null
Findings ohne Fehlermeldung (Protokoll §9, T12-Ergänzung Rev. 32). Die Bezeugung
des K4-Rohtexts gilt für die **archivierte Zeilenaufteilung** (80 Spalten), nicht
für eine beliebig nacherzeugte (Skelett T7.2, C6b-2b).

### T7.3 — Nicht erhobene Injektionen (Quelle jedes `n. e.`)

| Konfiguration | Injektionen ohne gültigen Lauf | Anzahl | Gegenprobe Journal | Gegenprobe Prosa-Manifest |
|---|---|---|---|---|
| K1 | *(keine)* | 0 | **deckungsgleich** | **deckungsgleich** |
| K2 | *(keine)* | 0 | **deckungsgleich** | **deckungsgleich** |
| K3 | *(keine)* | 0 | **deckungsgleich** | **deckungsgleich** |
| K4 | *(keine)* | 0 | **deckungsgleich** | **deckungsgleich** |
| K5 | *(keine)* | 0 | **deckungsgleich** | **deckungsgleich** |

**Weicht eine Gegenprobe ab, wird das berichtet, nicht aufgelöst** — die Harness
passt keine Seite an die andere an (Skelett T7.3 Bildungsvorschrift; Protokoll
Rev. 39). Die Abweichung erscheint zusätzlich auf `stderr`.

### T7.4 — Ungültige Läufe im Einzelnen

| Konfiguration | Injektion | `attempt` | Laufmanifest | Grund (`invalid_reasons`) | `calls_total` / `calls_invalid` / `calls_transport_failed` | Verdikt danach |
|---|---|---|---|---|---|---|
| K3 | I09 | 1 | `k3_06e052e19c153503f751611d7f813f18f204d8f0.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I09 | 2 | `k3_06e052e19c153503f751611d7f813f18f204d8f0_r2.json` | `transport_failure` | 3 / 0 / 2 | **VALID** in einem späteren Versuch |
| K3 | I09 | 3 | `k3_06e052e19c153503f751611d7f813f18f204d8f0_r3.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I09 | 4 | `k3_06e052e19c153503f751611d7f813f18f204d8f0_r4.json` | `transport_failure` | 3 / 0 / 3 | **VALID** in einem späteren Versuch |
| K3 | I22 | 1 | `k3_08a622b024e9174d7ce62863f385b369c8c27b12.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I07 | 1 | `k3_0993e01b26b7cc91bb70840207860fcc15dba286.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I07 | 2 | `k3_0993e01b26b7cc91bb70840207860fcc15dba286_r2.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I23 | 1 | `k3_28a75749496229bb1db37d85f68347572bd84c49.json` | `transport_failure` | 3 / 0 / 3 | **VALID** in einem späteren Versuch |
| K3 | I23 | 2 | `k3_28a75749496229bb1db37d85f68347572bd84c49_r2.json` | `transport_failure` | 3 / 0 / 2 | **VALID** in einem späteren Versuch |
| K3 | I23 | 3 | `k3_28a75749496229bb1db37d85f68347572bd84c49_r3.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I23 | 4 | `k3_28a75749496229bb1db37d85f68347572bd84c49_r4.json` | `transport_failure` | 3 / 0 / 3 | **VALID** in einem späteren Versuch |
| K3 | I23 | 5 | `k3_28a75749496229bb1db37d85f68347572bd84c49_r5.json` | `transport_failure` | 3 / 0 / 3 | **VALID** in einem späteren Versuch |
| K3 | I20 | 1 | `k3_35061d852631049ff74f65451368d7e85fd733bd.json` | `transport_failure` | 3 / 0 / 2 | **VALID** in einem späteren Versuch |
| K3 | I20 | 2 | `k3_35061d852631049ff74f65451368d7e85fd733bd_r2.json` | `transport_failure` | 3 / 0 / 2 | **VALID** in einem späteren Versuch |
| K3 | I13 | 1 | `k3_3be646fed3bdb2449b153f912d42fbb63b719776.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I13 | 2 | `k3_3be646fed3bdb2449b153f912d42fbb63b719776_r2.json` | `transport_failure` | 3 / 0 / 2 | **VALID** in einem späteren Versuch |
| K3 | I16 | 1 | `k3_43f9fa5ec1b6fbf4aaae26296a41b752c2e3f9cf.json` | `transport_failure` | 3 / 0 / 3 | **VALID** in einem späteren Versuch |
| K3 | I16 | 2 | `k3_43f9fa5ec1b6fbf4aaae26296a41b752c2e3f9cf_r2.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I06 | 1 | `k3_531a1ff2616aaa13f8c317fe7d40f56135caacaf.json` | `transport_failure` | 3 / 0 / 2 | **VALID** in einem späteren Versuch |
| K3 | I06 | 2 | `k3_531a1ff2616aaa13f8c317fe7d40f56135caacaf_r2.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I11 | 1 | `k3_5601a944ea1da65b1e2b03c5e74a8237336a2e85.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I11 | 2 | `k3_5601a944ea1da65b1e2b03c5e74a8237336a2e85_r2.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I11 | 3 | `k3_5601a944ea1da65b1e2b03c5e74a8237336a2e85_r3.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I11 | 4 | `k3_5601a944ea1da65b1e2b03c5e74a8237336a2e85_r4.json` | `transport_failure` | 3 / 0 / 3 | **VALID** in einem späteren Versuch |
| K3 | I11 | 5 | `k3_5601a944ea1da65b1e2b03c5e74a8237336a2e85_r5.json` | `transport_failure` | 3 / 0 / 2 | **VALID** in einem späteren Versuch |
| K3 | I05 | 1 | `k3_dbcd05b8935ac3d007464f2e0d72c08ef0a9931e.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I05 | 2 | `k3_dbcd05b8935ac3d007464f2e0d72c08ef0a9931e_r2.json` | `transport_failure` | 3 / 0 / 1 | **VALID** in einem späteren Versuch |
| K3 | I21 | 1 | `k3_dd414657d12197a1ca79152d401f75eb4b5f5f57.json` | `transport_failure` | 3 / 0 / 2 | **VALID** in einem späteren Versuch |
| K3 | I21 | 2 | `k3_dd414657d12197a1ca79152d401f75eb4b5f5f57_r2.json` | `transport_failure` | 3 / 0 / 2 | **VALID** in einem späteren Versuch |

**Eine unbekannte `rule_id` invalidiert den ganzen Versuch**, nicht nur das
betroffene Finding (Auswertungsspezifikation §7.4). Der Exit-Code ist **kein**
Gültigkeitskriterium (Protokoll §6 Nachtrag Rev. 26).

---

## T2 — Haupttabelle Erkennung

**Erste Stufe vor beiden Metriken: Filter nach Mechanismus** — K1 := Records mit
`rule_id`-Präfix `DERIVED:`, K2/K3 := jeder andere `rule_id` (Protokoll §4 Nachtrag
Rev. 25). **K2 und K3 werden nirgends addiert.**

| Szenario (n) | K1 loc | K1 str | K2 loc | K2 str | K2 FP-M | K3 loc | K3 str | K3 FP-M | K4 loc | K4 str | K5 loc | K5 str |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LAYER_BACK_CALL` (3) | 3/3 | 3/3 | 3/3 | 3/3 | **49/52** | 3/3 | 3/3 | **1/52** | 3/3 | 3/3 | 3/3 | 3/3 |
| `LAYER_SKIP_CALL` (3) | 3/3 | 3/3 | 3/3 | 3/3 | **49/52** | 3/3 | 3/3 | **1/52** | 3/3 | 3/3 | 3/3 | 3/3 |
| `PROTECTED_MODULE` (3) | 3/3 | 3/3 | 3/3 | 3/3 | **49/52** | 3/3 | 3/3 | **1/52** | 3/3 | 3/3 | 3/3 | 3/3 |
| `INDEPENDENCE` (3) | 3/3 | 3/3 | 3/3 | 3/3 | **49/52** | 3/3 | 3/3 | **1/52** | 3/3 | 3/3 | 3/3 | 3/3 |
| `CYCLE_SIBLING` (3) | 3/3 | 3/3 | ` — ` | ` — ` | **49/52** | ` — ` | ` — ` | **1/52** | `n. b.` | 3/3 | 3/3 | 0/3 |
| `CYCLE_PARENT_CHILD` (1) | 1/1 | 1/1 | ` — ` | ` — ` | **49/52** | ` — ` | ` — ` | **1/52** | `n. b.` | ` — ` | 1/1 | 0/1 |
| `MISSING_PORT_REFERENCE` (4) | ` — ` | ` — ` | 4/4 | 2/4 | **49/52** | 4/4 | 4/4 | **1/52** | ` — ` | ` — ` | 4/4 | 4/4 |
| `FRAMEWORK_TYPE_IN_SIGNATURE` (4) | ` — ` | ` — ` | 4/4 | 4/4 | **49/52** | 4/4 | 4/4 | **1/52** | ` — ` | ` — ` | ` — ` | ` — ` |
| `INCORRECT_LOCATION` (4) | ` — ` | ` — ` | 3/4 | 3/4 | **49/52** | 4/4 | 4/4 | **1/52** | 4/4 | 0/4 | ` — ` | ` — ` |
| `SIGNATURE_DEVIATION` (4) | ` — ` | ` — ` | 4/4 | 4/4 | **49/52** | 4/4 | 4/4 | **1/52** | ` — ` | ` — ` | ` — ` | ` — ` |

**Die Spalten `K2 FP-M` / `K3 FP-M` sind Pflicht** und tragen die modulweise
Falsch-Positiv-Rate derselben Konfiguration aus T3 in **jeder** Zeile: `localized`
darf für K2/K3 nie ohne sie erscheinen (Protokoll §5 Amendment 11.08.;
Auswertungsspezifikation §4.2, §8 Punkt 1).

**Fussnoten (Pflicht, Wortlaut im Skelett):** (a) `localized` bei K4/`CYCLE` ist
`n. b.`, nicht 0 · (b) die K2/K3-Nullzeilen bei `CYCLE` sind konstruktionsbedingt ·
**(c) `FORBIDDEN_SIGNATURE_TYPE` — vorregistrierter `strict`-Ausfallmodus** (Segmente
1–3 gleich, Segment 4 gekürzt; Kennzeichnung als eigene Spalte **SV** in T4, nicht
als Fussnote am Tabellenende) · **(d) `STRUCTURAL_PLACEMENT` — `strict` ist dort
nicht unabhängig von `localized`** (Segment 4 == Segment 3) · (e) `localized` misst
auf dem LLM-Pfad die **Meldequote** · (f) die erwartete Kategorie ist pfadabhängig ·
(g) die Subjektform ist im Regelstatement vorgegeben.

---

## T3 — Falsch-Positiv-Raten je LLM-Konfiguration, zwei Granularitäten

> **AUFLAGE IM KOPF DER TABELLE (Protokoll §5, Amendment 11.08.2026):** `localized`
> ist **nur zusammen mit dieser Messreihe interpretierbar**. **`localized` wird nie
> ohne diese Tabelle berichtet.** **K2 und K3 werden nirgends addiert.**

**Quelle:** `/home/haasentimo/ma/masterarbeit/data/c3b-k2` und `/home/haasentimo/ma/masterarbeit/data/c3b-k3` — **nicht** die Kampagne.
**Nenner 52** (inhaltstragende Kontrollmodule).

| Konfiguration | Granularität | Bezugsmetrik | run 0 | run 1 | run 2 | Median | Spannweite | Headline |
|---|---|---|---|---|---|---|---|---|
| K2 | **modulweise** (Module mit ≥ 1 Finding / 52) | Bezug für `localized` | 49 | 49 | 49 | **49** | 49–49 | **49/52** |
| K2 | **findingweise** (Findings gesamt, undedupliziert) | Bezug für `strict` und Precision | 155 | 153 | 153 | **153** | 153–155 | ` — ` |
| K3 | **modulweise** (Module mit ≥ 1 Finding / 52) | Bezug für `localized` | 2 | 1 | 0 | **1** | 0–2 | **1/52** |
| K3 | **findingweise** (Findings gesamt, undedupliziert) | Bezug für `strict` und Precision | 2 | 1 | 0 | **1** | 0–2 | ` — ` |

**Die Headline zählt ALLE Findings — die beiden vorregistrierten Meldungen bleiben
darin und stehen zusätzlich getrennt in T3.1** (§7.2 in der Fassung der
Protokoll-Rev. 37, 28.08.2026: nicht herausgerechnet, weil die Herausrechnung die
gemessene Rate verbesserte, gewählt und nicht erzwungen wäre und der Auflage
widerspräche, `localized` nie ohne die vollständige FP-Rate zu berichten).

**Zweite Lesart, mitgeführt und ausdrücklich NICHT die Headline:** dieselbe
modulweise Zahl **ohne** die vorregistrierten Meldungen — sie steht hier, damit
sichtbar bleibt, ob die beiden Lesarten auseinanderfallen:

| Konfiguration | run 0 | run 1 | run 2 | Median | fällt auseinander? |
|---|---|---|---|---|---|
| K2 | 49 | 49 | 49 | **49** | nein — beide Lesarten gleich |
| K3 | 2 | 1 | 0 | **1** | nein — beide Lesarten gleich |

### T3.1 — Die vorregistrierten Meldungen, getrennt ausgewiesen

**Sie sind im Headline-Zähler oben ENTHALTEN** (§7.2, Protokoll Rev. 37) und stehen
hier zusätzlich, damit sichtbar bleibt, welcher Teil der Rate vorhergesagt war.

| Konfiguration | Fall | Zähler je Lauf (0/1/2) | Häufigkeit | vorregistriert in |
|---|---|---|---|---|
| K2 | Adapterfassade `depot.core.adapters`, `R-PROTECT-1` | 3/3/3 | **3 von 3 Läufen** | Protokoll §5 Nachtrag Rev. 16 |
| K2 | Nicht-Träger-Portregel auf `orders_services` (`R-PORT-2`/`R-PORT-3`) | 2/0/0 | **1 von 3 Läufen** | Protokoll §5 Nachtrag Rev. 18 |
| K3 | Adapterfassade `depot.core.adapters`, `R-PROTECT-1` | 0/0/0 | **0 von 3 Läufen** | Protokoll §5 Nachtrag Rev. 16 |
| K3 | Nicht-Träger-Portregel auf `orders_services` (`R-PORT-2`/`R-PORT-3`) | 0/0/0 | **0 von 3 Läufen** | Protokoll §5 Nachtrag Rev. 18 |

**Getrennte Recordzählung (Protokoll §4 Rev. 25), nie als Summe:**

| Konfiguration | `DERIVED:`-Records je Lauf | LLM-Records je Lauf |
|---|---|---|
| K2 | 0/0/0 | 155/153/153 |
| K3 | 0/0/0 | 2/1/0 |

**Findings je `rule_id`** (aus den Artefakten gezählt, nicht aus einem Bericht
übernommen — Anhang A, Zeile A-10):

| Konfiguration | `R-CORE-1` | `R-CYCLE-1` | `R-CYCLE-2` | `R-FRAMEWORK-1` | `R-INDEP-1` | `R-LAYER-1` | `R-PLACE-1` | `R-PORT-1` | `R-PORT-2` | `R-PORT-3` | `R-PORT-4` | `R-PROTECT-1` | `R-SIG-1` | `R-SIG-2` | `R-SIG-3` | `R-SIG-4` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| K2 | 153 | 12 | 12 | 63 | 30 | 66 | 54 | 3 | 4 | 4 | 3 | 36 | 9 | 3 | 3 | 6 |
| K3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 |

**Bezug der K2-Findings zum geprüften Modul** (deskriptive Gegenprobe,
Anhang A Zeile A-09/A-10). **Die Klassen heissen Selbstbezug, Fremdbezug,
Zielbezug und nicht zuordenbar** — nicht K1–K4: jene Bezeichner kollidieren mit
den Konfigurationsnamen dieser Arbeit:

| Klasse | Anzahl | Anteil |
|---|---|---|
| Selbstbezug | 329 | 71.4 % |
| Fremdbezug | 36 | 7.8 % |
| Zielbezug | 12 | 2.6 % |
| nicht zuordenbar | 84 | 18.2 % |
| **gesamt** | **461** | Gegenprobe gegen das archivierte `finding_reference_analysis.json`: **deckungsgleich** |

---

## T4 — Vorbelastung, Kampagnenwert und paarweise Differenz je Injektion

> **BINDEND: Die Differenz wird auch berichtet, wenn sie null oder negativ ist.**
> Sie fällt nicht heraus, wird nicht gerundet und wird nicht kommentarlos durch die
> Aggregatzahl ersetzt (Protokoll §5 Rev. 31). **Es wird nichts subtrahiert** —
> die Differenz tritt **neben** Precision/Recall/F1, nie an ihre Stelle.

**Ruhezustandsseite:** `data/c3b-k2/` bzw. `data/c3b-k3/`, konfigurationsgleich,
gleiche Repetitionszahl auf beiden Seiten. **Berichtsform Grössenordnungen**, ohne
Nachkommastellen-Interpretation.

| ID | Szenario | Trägermodul | K2 Ruhe | K2 Kampagne | K2 Δ | K2 Läufe (Ruhe · Kampagne) | K2 `strict` | K2 `loc` | K2 SV | K2 kein-EN | K3 Ruhe | K3 Kampagne | K3 Δ | K3 Läufe (Ruhe · Kampagne) | K3 `strict` | K3 `loc` | K3 SV | K3 kein-EN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I01 | `LAYER_BACK_CALL` | `depot.identity.repository.customer_repo` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I02 | `LAYER_BACK_CALL` | `depot.orders.repository.order_repo` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I03 | `LAYER_BACK_CALL` | `depot.billing.repository.invoice_repo` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I04 | `LAYER_SKIP_CALL` | `depot.identity.api.routes` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I05 | `LAYER_SKIP_CALL` | `depot.orders.api.routes` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I06 | `LAYER_SKIP_CALL` | `depot.billing.api.routes` | 2 | 2 | 0 | [2,2,2] · [2,2,2] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I07 | `PROTECTED_MODULE` | `depot.identity.services.customer_service` | 2 | 2 | 0 | [2,2,2] · [2,2,2] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I08 | `PROTECTED_MODULE` | `depot.orders.services.order_service` | 3 | 2 | -1 | [3,3,3] · [2,2,2] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I09 | `PROTECTED_MODULE` | `depot.billing.services.invoice_service` | 3 | 3 | 0 | [3,3,3] · [3,3,3] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I10 | `INDEPENDENCE` | `depot.orders.services.checkout_service` | 2 | 3 | 1 | [2,2,2] · [3,3,3] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I11 | `INDEPENDENCE` | `depot.billing.services.dunning_service` | 3 | 3 | 0 | [3,3,3] · [3,3,3] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I12 | `INDEPENDENCE` | `depot.orders.repository.order_line_repo` | 1 | 2 | 1 | [1,1,1] · [1,2,2] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I13 | `CYCLE_SIBLING` | `depot.identity.mappers.customer_mapper` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | ` — ` | ` — ` | nein | ` — ` | 0 | 1 | 1 | [0,0,0] · [1,1,1] | ` — ` | ` — ` | nein | ` — ` |
| I14 | `CYCLE_SIBLING` | `depot.orders.mappers.order_mapper` | 0 | 0 | 0 | [0,0,0] · [0,0,0] | ` — ` | ` — ` | nein | ` — ` | 0 | 1 | 1 | [0,0,0] · [1,1,1] | ` — ` | ` — ` | nein | ` — ` |
| I15 | `CYCLE_SIBLING` | `depot.billing.mappers.invoice_mapper` | 0 | 0 | 0 | [0,0,0] · [0,0,0] | ` — ` | ` — ` | nein | ` — ` | 0 | 1 | 1 | [0,0,0] · [1,1,1] | ` — ` | ` — ` | nein | ` — ` |
| I16 | `CYCLE_PARENT_CHILD` | `depot.orders.services.pricing.engine` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | ` — ` | ` — ` | nein | ` — ` | 0 | 1 | 1 | [0,0,0] · [1,1,1] | ` — ` | ` — ` | nein | ` — ` |
| I17 | `MISSING_PORT_REFERENCE` | `depot.identity.services.token_service` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 0 | 1 | ja | entfällt | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I18 | `MISSING_PORT_REFERENCE` | `depot.orders.services.catalog_service` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I19 | `MISSING_PORT_REFERENCE` | `depot.orders.services.refund_service` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I20 | `MISSING_PORT_REFERENCE` | `depot.billing.services.ledger_service` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 0 | 1 | ja | entfällt | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I21 | `FRAMEWORK_TYPE_IN_SIGNATURE` | `depot.identity.models.customer_models` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I22 | `FRAMEWORK_TYPE_IN_SIGNATURE` | `depot.orders.models.order_models` | 5 | 1 | -4 | [5,5,5] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I23 | `FRAMEWORK_TYPE_IN_SIGNATURE` | `depot.orders.models.order_line_models` | 4 | 1 | -3 | [4,4,4] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I24 | `FRAMEWORK_TYPE_IN_SIGNATURE` | `depot.billing.models.invoice_models` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I25 | `INCORRECT_LOCATION` | `depot.orders.legacy_order_index` | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I26 | `INCORRECT_LOCATION` | `depot.billing.legacy_invoice_index` | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I27 | `INCORRECT_LOCATION` | `depot.identity.legacy_token_index` | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I28 | `INCORRECT_LOCATION` | `depot.billing.legacy_tax_models` | 0 | 0 | 0 | [0,0,0] · [0,0,0] | 0 | 0 | nein | entfällt | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I29 | `SIGNATURE_DEVIATION` | `depot.identity.repository.session_repo` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |
| I30 | `SIGNATURE_DEVIATION` | `depot.orders.repository.order_query` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [1,0,0] · [1,1,1] | 1 | 1 | nein | ja |
| I31 | `SIGNATURE_DEVIATION` | `depot.billing.repository.invoice_query` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 1 | 1 | 0 | [1,1,0] · [1,1,1] | 1 | 1 | nein | ja |
| I32 | `SIGNATURE_DEVIATION` | `depot.orders.mappers.order_line_mapper` | 1 | 1 | 0 | [1,1,1] · [1,1,1] | 1 | 1 | nein | ja | 0 | 1 | 1 | [0,0,0] · [1,1,1] | 1 | 1 | nein | nein |

**Spaltenbedeutung.** **Ruhe** = Ruhezustandszahl desselben Moduls in derselben
Kategorie aus C3b (Median über drei Läufe) · **Kampagne** = dieselbe Zählgrösse auf
dem Injektionscommit (Median) · **Δ** = Kampagne − Ruhe · **Läufe (Ruhe ·
Kampagne)** = dieselbe Zählgrösse für **jede der drei Repetitionen einzeln**, in
`run_index`-Reihenfolge, **rein deskriptiv** (Spez. §7.5 (5), Protokoll Rev. 40) ·
**SV** = Schreibweisenverfehlung, mechanisch gebildet (`localized` Treffer **und**
`strict` 0 **und** Abweichung allein in Segment 4) · **kein-EN** = ein
`strict`-Treffer, der die Ruhezustandsrate **nicht übersteigt**, wird nicht als
Erkennungsnachweis geführt.

> **kein-EN steht auf EINER Aggregationsstufe — der Existenzstufe** (Protokoll
> Rev. 40, gesetzt **nach** dem ersten Auswertungslauf und dort ungeschminkt
> registriert). Verglichen wird `strict` (Existenz über die drei Repetitionen,
> unverändert nach §4) mit der **Existenz** der Ruhezustandszählgrösse — mindestens
> einer der drei C3b-Läufe > 0. **`ja`** = beides vorhanden (übersteigt nicht) ·
> **`nein`** = `strict`-Treffer bei leerem Ruhezustand (übersteigt) ·
> **`entfällt`** = kein `strict`-Treffer, die Frage stellt sich nicht — ein
> **gerechneter** Wert, **kein Marker**. Trägt `strict` einen Marker, trägt kein-EN
> denselben. **Die Spalten `Ruhe`, `Kampagne` und `Δ` bleiben auf dem Median** und
> werden von kein-EN **nicht gelesen** — sie sind die eigenständige paarweise
> Auslesart nach §7.5 (4). **Der Filterunterschied bleibt und ist benannt:**
> `strict` filtert über den `match_key`, die Ruhezustandszahl über Trägermodul und
> Kategorie; Rev. 40 legt die **Stufe** fest, nicht den Filter.

### T4 Symmetrieteil — K1, K4, K5

| ID | K1 Ruhe | K1 Kampagne | K1 Δ | K4 Ruhe | K4 Kampagne | K4 Δ | K5 Ruhe | K5 Kampagne | K5 Δ |
|---|---|---|---|---|---|---|---|---|---|
| I01 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I02 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I03 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I04 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I05 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I06 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I07 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I08 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I09 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I10 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I11 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I12 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 1 | 1 |
| I13 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | `n. b.` | `n. b.` | 0 ᴬ¹⁴ | 1 | 1 |
| I14 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | `n. b.` | `n. b.` | 0 ᴬ¹⁴ | 1 | 1 |
| I15 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | `n. b.` | `n. b.` | 0 ᴬ¹⁴ | 1 | 1 |
| I16 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 1 | 1 |
| I17 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 1 | 1 |
| I18 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 1 | 1 |
| I19 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 1 | 1 |
| I20 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 1 | 1 |
| I21 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 |
| I22 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 |
| I23 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 |
| I24 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 |
| I25 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 0 | 0 |
| I26 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 0 | 0 |
| I27 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 0 | 0 |
| I28 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 1 | 1 | 0 ᴬ¹⁴ | 0 | 0 |
| I29 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 |
| I30 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 |
| I31 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 |
| I32 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 | 0 ᴬ¹⁴ | 0 | 0 |

**Kampagnenseite für K1/K4/K5 (nachgetragen C11b).** Dieselbe Zählgrösse wie im
Hauptteil — **Findings desselben Moduls in derselben Kategorie** —, mit der
**pfadabhängigen** Kategorie (Spez. §4): auf dem K1-Pfad `layer-violation` bzw.
`cycle`, nie ein Ebene-1-Name. Für K4/K5 stammt der gemeldete Modulname aus
`tools/match_k4k5.py`; wo die Ausgabeform **strukturell kein Modul** trägt
(`acyclic_siblings`-Block), ist die Zählgrösse **nicht bildbar** und die Zelle
trägt `n. b.` — **nicht 0** (A-17, Protokoll §4 Rev. 30). Alle drei
Konfigurationen tragen **einen** Lauf; die Differenz ist mangels Streuung trivial
und wird aus Symmetrie der Tabelle **dennoch ausgewiesen** (Spez. §7.5 (4)).

**ᴬ¹⁴ Herkunft der Ruhezustandsseite für K1/K4/K5:** der Clean-State-Audit (C3a,
**0 Findings**), **nicht** C3b — C3b umfasst nur die LLM-Pfade. Ein
maschinenlesbares C3a-Artefakt ist **nicht archiviert**; die 0 ist aus
`c3a_bericht_clean_state_audit.md` übernommen und hier als **Berichtswert**
gekennzeichnet, nicht als gemessenes Artefakt (Anhang A, Zeile **A-14**).

---

## T5 — Precision / Recall / F1

> **AUFLAGE IM KOPF DER TABELLE:** **K2 und K3 stehen in getrennten Zeilen und
> werden NIRGENDS zu „dem LLM-Pfad“ addiert oder gemittelt.**

Kennzahlen **ohne Nachkommastellen-Interpretation**; die Arbeit macht Existenz-,
Non-Inferiority- und Nicht-Abdeckungsaussagen, keine Präzisionsschätzungen.

| Konfiguration | Kategorie (Ebene 1) | n | `strict` P | `strict` R | `strict` F1 | `loc` P | `loc` R | `loc` F1 | FP-Bezug (T3) |
|---|---|---|---|---|---|---|---|---|---|
| K1 | `FORBIDDEN_RELATION` | 12 | 12/12 = 1,000 | 12/12 = 1,000 | 1,000 | 12/12 = 1,000 | 12/12 = 1,000 | 1,000 | `n. b.` |
| K1 | `CYCLE` | 4 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | `n. b.` |
| K1 | `ABSENCE_REQUIRED` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K1 | `FORBIDDEN_SIGNATURE_TYPE` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K1 | `STRUCTURAL_PLACEMENT` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K1 | `API_CONTRACT` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K1 | **Gesamt — UF3, Abdeckung des Kategoriespektrums, vorregistrierter Nenner 32, gerechneter Nenner je Zelle ausgewiesen** | 32 | 16/16 = 1,000 | 16/32 = 0,500 | 0,667 | 16/16 = 1,000 | 16/32 = 0,500 | 0,667 | `n. b.` |
| K1 | **Gesamt — UF4, Leistung im ausdrückbaren Bereich, vorregistrierter Nenner 16, gerechneter Nenner je Zelle ausgewiesen** | 16 | 16/16 = 1,000 | 16/16 = 1,000 | 1,000 | 16/16 = 1,000 | 16/16 = 1,000 | 1,000 | `n. b.` |
| K2 | `FORBIDDEN_RELATION` | 12 | 12/68 = 0,176 | 12/12 = 1,000 | 0,300 | 12/21 = 0,571 | 12/12 = 1,000 | 0,727 | **49/52** |
| K2 | `CYCLE` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | **49/52** |
| K2 | `ABSENCE_REQUIRED` | 4 | 2/29 = 0,069 | 2/4 = 0,500 | 0,121 | 4/8 = 0,500 | 4/4 = 1,000 | 0,667 | **49/52** |
| K2 | `FORBIDDEN_SIGNATURE_TYPE` | 4 | 4/7 = 0,571 | 4/4 = 1,000 | 0,727 | 4/5 = 0,800 | 4/4 = 1,000 | 0,889 | **49/52** |
| K2 | `STRUCTURAL_PLACEMENT` | 4 | 3/6 = 0,500 | 3/4 = 0,750 | 0,600 | 3/4 = 0,750 | 3/4 = 0,750 | 0,750 | **49/52** |
| K2 | `API_CONTRACT` | 4 | 4/13 = 0,308 | 4/4 = 1,000 | 0,471 | 4/7 = 0,571 | 4/4 = 1,000 | 0,727 | **49/52** |
| K2 | **Gesamt — UF3, Abdeckung des Kategoriespektrums, vorregistrierter Nenner 32, gerechneter Nenner je Zelle ausgewiesen** | 32 | 25/123 = 0,203 | 25/32 = 0,781 | 0,323 | 27/46 = 0,587 | 27/32 = 0,844 | 0,692 | **49/52** |
| K2 | **Gesamt — UF4, Leistung im ausdrückbaren Bereich, vorregistrierter Nenner 28, gerechneter Nenner je Zelle ausgewiesen** | 28 | 25/123 = 0,203 | 25/28 = 0,893 | 0,331 | 27/45 = 0,600 | 27/28 = 0,964 | 0,740 | **49/52** |
| K3 | `FORBIDDEN_RELATION` | 12 | 12/12 = 1,000 | 12/12 = 1,000 | 1,000 | 12/12 = 1,000 | 12/12 = 1,000 | 1,000 | **1/52** |
| K3 | `CYCLE` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | **1/52** |
| K3 | `ABSENCE_REQUIRED` | 4 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | **1/52** |
| K3 | `FORBIDDEN_SIGNATURE_TYPE` | 4 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | **1/52** |
| K3 | `STRUCTURAL_PLACEMENT` | 4 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | **1/52** |
| K3 | `API_CONTRACT` | 4 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | **1/52** |
| K3 | **Gesamt — UF3, Abdeckung des Kategoriespektrums, vorregistrierter Nenner 32, gerechneter Nenner je Zelle ausgewiesen** | 32 | 28/28 = 1,000 | 28/32 = 0,875 | 0,933 | 28/28 = 1,000 | 28/32 = 0,875 | 0,933 | **1/52** |
| K3 | **Gesamt — UF4, Leistung im ausdrückbaren Bereich, vorregistrierter Nenner 28, gerechneter Nenner je Zelle ausgewiesen** | 28 | 28/28 = 1,000 | 28/28 = 1,000 | 1,000 | 28/28 = 1,000 | 28/28 = 1,000 | 1,000 | **1/52** |
| K4 | `FORBIDDEN_RELATION` | 12 | 12/12 = 1,000 | 12/12 = 1,000 | 1,000 | 12/12 = 1,000 | 12/12 = 1,000 | 1,000 | `n. b.` |
| K4 | `CYCLE` | 4 | 3/3 = 1,000 | 3/4 = 0,750 | 0,857 | `n. b.`ᵃ | `n. b.`ᵃ | `n. b.`ᵃ | `n. b.` |
| K4 | `ABSENCE_REQUIRED` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K4 | `FORBIDDEN_SIGNATURE_TYPE` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K4 | `STRUCTURAL_PLACEMENT` | 4 | 0/0 | 0/4 = 0,000 | 0/0 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | `n. b.` |
| K4 | `API_CONTRACT` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K4 | **Gesamt — UF3, Abdeckung des Kategoriespektrums, vorregistrierter Nenner 32, gerechneter Nenner je Zelle ausgewiesen** | 32 | 15/15 = 1,000 | 15/32 = 0,469 | 0,638 | 16/16 = 1,000 | 16/28 = 0,571 | 0,727 | `n. b.` |
| K4 | **Gesamt — UF4, Leistung im ausdrückbaren Bereich, vorregistrierter Nenner 19, gerechneter Nenner je Zelle ausgewiesen** | 19 | 15/15 = 1,000 | 15/19 = 0,789 | 0,882 | 16/16 = 1,000 | 16/16 = 1,000 | 1,000 | `n. b.` |
| K5 | `FORBIDDEN_RELATION` | 12 | 12/12 = 1,000 | 12/12 = 1,000 | 1,000 | 12/12 = 1,000 | 12/12 = 1,000 | 1,000 | `n. b.` |
| K5 | `CYCLE` | 4 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | `n. b.` |
| K5 | `ABSENCE_REQUIRED` | 4 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | 4/4 = 1,000 | 4/4 = 1,000 | 1,000 | `n. b.` |
| K5 | `FORBIDDEN_SIGNATURE_TYPE` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K5 | `STRUCTURAL_PLACEMENT` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K5 | `API_CONTRACT` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K5 | **Gesamt — UF3, Abdeckung des Kategoriespektrums, vorregistrierter Nenner 32, gerechneter Nenner je Zelle ausgewiesen** | 32 | 16/16 = 1,000 | 16/28 = 0,571 | 0,727 | 16/16 = 1,000 | 16/28 = 0,571 | 0,727 | `n. b.` |
| K5 | **Gesamt — UF4, Leistung im ausdrückbaren Bereich, vorregistrierter Nenner 20, gerechneter Nenner je Zelle ausgewiesen** | 20 | 16/16 = 1,000 | 16/16 = 1,000 | 1,000 | 16/16 = 1,000 | 16/16 = 1,000 | 1,000 | `n. b.` |

**Wie die Zellen zu lesen sind.** `TP/Nenner = Wert`. **Der Nenner ist der
gerechnete, ausgewiesene Nenner** — er sinkt bei `n. e.` und `n. b.` und bei den
vorregistrierten Sonderklassen, und eine Rate über weniger Injektionen ist eine
andere Rate (Auflage (2)). Die Spalte `n` bleibt daneben der **vorregistrierte**
Wert aus dem Skelett und wird nicht nachgeführt. **`0/0`** heisst: der Nenner ist
**leer** — bei Precision, dass die Konfiguration in dieser Zeile **nichts** gemeldet
hat, bei Recall, dass **keine** Injektion der Zeile in die Rechnung eingeht. Das ist
eine **gerechnete Angabe, kein Marker**, und ausdrücklich **nicht** dasselbe wie 0.

**Die vier Ausschlüsse, in dieser Reihenfolge.** **(1)** `n. b.` und `n. e.` — keine
Messung, aus dem Nenner **beider** Gesamtzeilen genommen · **(2)** die
vorregistrierten Sonderklassen **T9 Fall 6 und Fall 7** — **weder** Treffer **noch**
FP **noch** FN, **vor** der allgemeinen FP/FN-Rechnung abgefangen (Auflage (4));
ihre Häufigkeit steht in **T9** · **(3)** ` — ` — **nicht** ausgeschlossen, sondern
richtungsabhängig: in **UF3** geht es als **0** ein (Abdeckung ist genau die Frage),
in **UF4** ist es aus dem Nenner **genommen**; die Falsch-Positiven einer
` — `-Injektion gehen nach Skelett §1 Kontrollregel 2 dennoch in T5 ein — in UF3, und
mit ihrer Injektion zusammen fallen sie aus UF4 · **(4)** `ERROR` und
Werkzeugabbruch sind **kein** FN (Auflage (5)) — sie erreichen die Rechnung nicht.

**FP-Bildung.** `strict` dedupliziert **nicht**: je **Lauf** zählt der passende
Record als **ein** TP, jeder weitere Record desselben Laufs als FP, über die Läufe
summiert (§3.2). Ein in der nächsten Repetition **wiederholter richtiger** Treffer
ist Reproduzierbarkeit, kein Falsch-Positiv. `localized` **dedupliziert** auf
`(component, module, category)`; jedes andere Tripel ist **ein** FP, unabhängig
davon, wie oft es auftritt (§7.3).

> **ERLEDIGT, GEGENSTANDSLOS — die Anforderung entfällt, sie wird nicht
> abgewiesen** (Protokoll Rev. 42, Skelett T5 (ii), Spezifikation §8 Punkt 1).
> Skelett T5 (ii) verlangte für K2/K3 zusätzlich **Median und Spannweite über drei
> Läufe**. Beide setzen eine **laufweise** Grösse voraus, über die gestreut werden
> kann; `strict` ist nach Spezifikation §3 ein **Existenzquantor über die
> Repetitionen** und hat konstruktiv **keine Verteilung über Läufe**. Eine
> laufweise Fassung wäre keine zweite Auslesart derselben Metrik, sondern eine
> **neue Metrikdefinition** — gesperrt nach Protokoll §0.1 Punkt 2. **Die
> Laufstreuung ist ausgewiesen, an der dafür vorregistrierten Stelle:** seit
> Rev. 40 trägt **T4** die Spalte **Läufe (Ruhe · Kampagne)** mit **jeder der drei
> Repetitionen einzeln** — feinkörniger als ein Median, nicht gröber. **T3 führt
> Median und Spannweite über drei Läufe unverändert weiter**; die Erledigung
> betrifft allein diese Tabelle.

**Beide Gesamtzeilen werden immer gemeinsam gedruckt.** In der UF3-Zeile gehen die
nicht ausdrückbaren Kategorien **als 0** ein — das ist gewollt und steht **an der
Zeile**: Abdeckung ist genau die Frage. In der UF4-Zeile sind sie aus dem Nenner
**genommen**, nicht als 0 gezählt; die Nenner folgen aus **T8**, nicht aus einer
Messung. **(3)** `localized` für K2/K3 nie ohne FP-Bezug; für K1/K4/K5 trägt die
Spalte `n. b.` **(4)** die vorregistrierten Sonderklassen (T9 Fälle 6 und 7) gehen
**nicht** in P/R/F1 ein und werden **vor** der allgemeinen FP/FN-Rechnung
abgefangen **(5)** `ERROR` ist **kein** FN — eigene Klasse „Regel nicht
ausgewertet“.

---

## T6 — Laufkosten je Konfiguration

| Konfiguration | Invocationen | Model-Calls | Wanduhr aussen, Summe | Wanduhr aussen je Invocation (Median / Spannweite) | Wanduhr innen (`wall_clock_ms`) | Tokens in gesamt | Tokens out gesamt | Tokens je Check (Median) | Latenz je Call (Median / Spannweite) |
|---|---|---|---|---|---|---|---|---|---|
| K1 | 32 | 0 | 2513 ms | 69.5 (67–193) ms | 1384 ms | ` — ` | ` — ` | ` — ` | ` — ` |
| K2 | 32 | 96 | 252155 ms | 7620 (716–18798) ms | 251010 ms | 110127 | 22285 | 1346 (767–1948) | 2460 (114–10894) ms |
| K3 | 61 | 183 | 9190542 ms | 127860 (18650–404302) ms | 9135427 ms | 158288 | 121469 | 1961 (0–3058) | 43145 (316–168972) ms |
| K4 | 32 | 0 | 3621 ms | 111 (104–179) ms | `n. b.`ᵃ | ` — ` | ` — ` | ` — ` | ` — ` |
| K5 | 32 | 0 | 9917 ms | 308.5 (279–486) ms | `n. b.`ᵃ | ` — ` | ` — ` | ` — ` | ` — ` |

**Herkunft jeder Spalte.** *Invocationen*, *Model-Calls* und beide Wanduhren
stammen aus den **gehashten Laufmanifesten** (`external_wall_clock_ms` für aussen,
`postrun.detail.wall_clock_ms_inner` für innen) und sind deshalb auch ohne
`--with-campaign` verfügbar. *Tokens* und *Latenz* stammen aus den `llm_call`-
Records der Kampagnen-Laufprotokolle (`tokens_in_total`, `tokens_out_total`,
`latency_ms_total`) — **ein `llm_call` ist ein Check**, also ein Dateiprompt
(Protokoll §5, Entscheidung I). Sie werden **nur** mit `--with-campaign` gelesen;
die Laufprotokolle tragen Funde und sind sonst durch die Blindheitsauflage
gesperrt. **`0/0`** heisst auch hier: leere Menge, kein gemessener Nullwert.

**Fussnoten (Pflicht).** **(a)** Die berichtete Wanduhrzeit ist für alle fünf
Konfigurationen **extern** gemessen; für K4/K5 existiert **kein** `run_footer`, der
Innenwert ist dort `n. b.` Feldname der externen Zeit im Laufmanifest:
**`external_wall_clock_ms`** (Anhang A, Zeile **A-28**, hiermit geschlossen) ·
**(b)** K4 baut den Graphen bei jedem Lauf neu (`--no-cache` ist Ablaufregel) —
die gemessene Zeit **enthält den vollen Graphaufbau** · **(c)** K5 bricht beim
ersten fehlgeschlagenen Assert ab; die Laufzeit hängt am **Trefferzeitpunkt** ·
**(d)** Berichtsform **Grössenordnungen**, ohne Interpretation von
Nachkommastellen; Token-Zahlen tragen den **Tokenizer-Vorbehalt** (§9 T5) ·
**(e) Der K4-Rohtext ist an der Terminalbreite geformt:** `rich` fällt bei Ausgabe
in eine Pipe auf **80 Spalten** zurück, gemessen `console.width = 80`,
`is_terminal = False`; **ein Reproduktionsversuch mit anderer Terminalbreite steht
vor ANDEREM ROHTEXT** — die Befundmenge ist dieselbe, ihre Zeilenaufteilung nicht.

**Weitere Umgebungsparameter, durchgezogen (Spezifikation §1.4):** Graphmodus —
**K1** `full` bei `CYCLE`, sonst `diff`; **K2/K3** immer `diff`; **K4/K5** kennen
den Schalter nicht (`n/a`).

---

## T8 — Ausdrucksmächtigkeit der Baselines

**Benötigte Harness-Ausgabe: keine.** Die Tabelle steht vor der Messung fertig da;
die Harness **liest** sie, sie schreibt sie nicht. Sie ist die **Begründung jedes
` — `** in T2, T4 und T5 und enthält **Werkzeugeigenschaften, keine Messergebnisse**.

| Szenario | K1 | K4 | K5 | K2/K3 | Beleg |
|---|---|---|---|---|---|
| `LAYER_BACK_CALL` | ausdrückbar | ausdrückbar | ausdrückbar | ausdrückbar | gemessen |
| `LAYER_SKIP_CALL` | ausdrückbar | ausdrückbar | ausdrückbar | ausdrückbar | gemessen |
| `PROTECTED_MODULE` | ausdrückbar | ausdrückbar | ausdrückbar | ausdrückbar | gemessen |
| `INDEPENDENCE` | ausdrückbar | ausdrückbar | ausdrückbar | ausdrückbar | gemessen |
| `CYCLE_SIBLING` | ausdrückbar | ausdrückbar | **teilweise** | **nicht ausdrückbar** | gemessen |
| `CYCLE_PARENT_CHILD` | ausdrückbar | **nicht ausdrückbar** | **teilweise** | **nicht ausdrückbar** | gemessen |
| `MISSING_PORT_REFERENCE` | **nicht ausdrückbar** | **nicht ausdrückbar** | ausdrückbar | ausdrückbar | gemessen |
| `FRAMEWORK_TYPE_IN_SIGNATURE` | **nicht ausdrückbar** | **nicht ausdrückbar** | **nicht ausdrückbar** | ausdrückbar | gemessen |
| `INCORRECT_LOCATION` | **nicht ausdrückbar** | **teilweise** | **nicht ausdrückbar** | ausdrückbar | gemessen |
| `SIGNATURE_DEVIATION` | **nicht ausdrückbar** | **nicht ausdrückbar** | **nicht ausdrückbar** | ausdrückbar | **abgeleitet, nicht gemessen** |

**`SIGNATURE_DEVIATION` ist die einzige nicht gemessene Zeile der Erwartungsmatrix.**

---

## T9 — Begleitmeldungen und vorhergesagte Falschmeldungen

Alle Fälle: **getrennt geführt**, **kein False Positive**, **gesondert
ausgewiesen** — und **vor** der allgemeinen FP/FN-Berechnung abgefangen, sonst
würden sie doppelt gezählt (Auswertungsspezifikation §5, Schlussabsatz).

| # | Fall | Pfad | Betroffen | Häufigkeit | Buchungsregel | vorregistriert in |
|---|---|---|---|---|---|---|
| 1 | `CYCLE`-Injektion (Modus `full`) erzeugt zusätzlich `layer-violation` auf derselben Kante | K1 | I13, I14, I15, I16 | 4 Records / 4 Läufe | `expected_co_findings` im Manifest; **kein FP** | Protokoll §4 Am. 13.08. (a) |
| 2 | `FORBIDDEN_RELATION`-Injektion (Modus `diff`) erzeugt **keinen** `cycle`-Record | K1 | I01, I02, I03, I04, I05, I06, I07, I08, I09, I10, I11, I12 | **Nullerwartung** | ein `cycle`-Record wäre ein **Befund** | DDR M.2 Festlegung 2; §3 Nachtrag Rev. 29 |
| 3 | `LAYER_BACK_CALL` wird von K4 **zweifach** gemeldet (`layers` **und** `acyclic_siblings`) | K4 | I01, I02, I03 | 3 Records / 3 Läufe | vorregistrierte Doppelmeldung, **nicht wegkonfigurierbar**, **kein FP** | Protokoll §4 Am. 13.08. (a)/(c) |
| 4 | Adapterfassade `depot.core.adapters`, `R-PROTECT-1` | K2/K3 | Kontrollset | K2 3/3 Läufe · K3 0/3 Läufe | vorhergesagt, **kein** unerwarteter FP | Protokoll §5 Nachtrag Rev. 16 |
| 5 | Nicht-Träger-Portregel auf `orders_services` (`R-PORT-2`/`R-PORT-3`) | K2/K3 | Kontrollset | K2 1/3 Läufe · K3 0/3 Läufe | vorhergesagt, **kein** unerwarteter FP | Protokoll §5 Nachtrag Rev. 18 |
| 6 | `CYCLE`: K2/K3 melden `FORBIDDEN_RELATION` am **richtigen Modul** | K2/K3 | I13, I14, I15, I16 | K2 6 · K3 0 | **kein** Treffer für `CYCLE` (Zelle bleibt `nein`), **kein** FP; in `localized` als „richtige Stelle, falsche Kategorie“ · **daneben 3 Records** am selben Modul mit anderer Kategorie (K2/API_CONTRACT) — **nicht** Fall 6, sie fallen unter die Allgemeinregel **FP *und* FN** | Protokoll §4 Am. 13.08. (f) |
| 7 | `CYCLE_*`: K5 meldet die Rückkante als **nicht gelistete Kante**, nicht als Zyklus | K5 | I13, I14, I15, I16 | 4 | `strict`: kein Treffer (Kategoriesegment weicht ab) · `localized`: Treffer auf der **Stelle**, Klasse „richtige Stelle, falsche Kategorie“ — **ohne neue Regel** gebucht | Protokoll §3 Fussnote 7 (B39) |

**Die Häufigkeiten der Fälle 6 und 7 werden aus einer BENANNTEN Sonderklasse
gezählt** (`special_class`), nicht aus einem Klassifikationseimer, den sie sich mit
anderen Funden teilen. Im ersten Auswertungslauf zählte Fall 7 aus `specials`,
während die Funde in `co_findings` lagen; die Zelle blieb leer und war von einer
nicht eingesetzten Zelle nicht zu unterscheiden (C11a §2.4). **Eine gerechnete 0
wird als `0` gedruckt.**

**Allgemeine Regel, von der die Fälle 6 und 7 die einzigen Ausnahmen sind:**
„falsche Regel/Kategorie, richtige Stelle“ → der `match_key` matcht nicht → zählt
als **FP *und* FN**.

---

## T10 — Overlap-Analyse: die Baselines gegen K2 bzw. gegen K3

> **AUFLAGE IM KOPF DER TABELLE.** **K2 und K3 werden NICHT zu „dem LLM-Pfad“
> vereinigt** — je Konfiguration eine eigene Zeilengruppe, dieselbe Auflage wie in
> T2 und T5. **Die Baselineseite IST eine Vereinigung** — K1 ∪ K4 ∪ K5 — und heisst
> hier so; jede Zelle nennt, **welche** Konfigurationen den Zustand tragen.
> **Eine Injektion, die eine Seite nach T8 nicht AUSDRÜCKEN kann, ist dort NICHT
> verfehlt** und wird **nie** als „nur die andere Seite“ gebucht (Auflage (3),
> G2-Reframing/B17). `n. b.`, `n. e.` und die vorregistrierten Sonderklassen **T9
> Fall 6/7** sind **weder Treffer noch Verfehlung** (Auflage (4)).

**Quelle: die bereits gerechneten Trefferzellen aus T2/T4 und die vorregistrierte
Ausdrucksmächtigkeit aus T8. Keine neue Metrik, keine neue Schwelle, kein neuer
Nenner** (Protokoll §8 UF3, Rev. 44; Auswertungsspezifikation §8 Punkt 10).
**Weicht T10 von T2 ab, ist T10 falsch — nicht T2.**

### T10a — Metrik `localized`

| Gruppe | Injektion | Szenario (Ebene 2) | Baselineseite (Vereinigung K1 ∪ K4 ∪ K5) | LLM-Seite | Zustand |
|---|---|---|---|---|---|
| K2 gegen die Baselines | I01 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I02 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I03 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I04 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I05 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I06 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I07 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I08 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I09 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I10 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I11 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I12 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I13 | `CYCLE_SIBLING` | Treffer (K1) | nicht ausdrückbar (K2) | **K2 nicht ausdrückbar** |
| K2 gegen die Baselines | I14 | `CYCLE_SIBLING` | Treffer (K1) | nicht ausdrückbar (K2) | **K2 nicht ausdrückbar** |
| K2 gegen die Baselines | I15 | `CYCLE_SIBLING` | Treffer (K1) | nicht ausdrückbar (K2) | **K2 nicht ausdrückbar** |
| K2 gegen die Baselines | I16 | `CYCLE_PARENT_CHILD` | Treffer (K1) | nicht ausdrückbar (K2) | **K2 nicht ausdrückbar** |
| K2 gegen die Baselines | I17 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I18 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I19 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I20 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I21 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I22 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I23 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I24 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I25 | `INCORRECT_LOCATION` | Treffer (K4) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I26 | `INCORRECT_LOCATION` | Treffer (K4) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I27 | `INCORRECT_LOCATION` | Treffer (K4) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I28 | `INCORRECT_LOCATION` | Treffer (K4) | Verfehlung (K2) | **nur Baseline** |
| K2 gegen die Baselines | I29 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I30 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I31 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I32 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | **Aggregat** | alle 32 | *ausserhalb des Nenners:* Baseline nicht ausdrückbar 8 · K2 nicht ausdrückbar 4 · beide Seiten nicht ausdrückbar 0 · nicht beurteilbar 0 | *Nenner = die vier Zustände* | **nur Baseline 1 · nur K2 0 · beide 19 · keiner 0 — Nenner 20** |
| K3 gegen die Baselines | I01 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I02 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I03 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I04 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I05 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I06 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I07 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I08 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I09 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I10 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I11 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I12 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I13 | `CYCLE_SIBLING` | Treffer (K1) | nicht ausdrückbar (K3) | **K3 nicht ausdrückbar** |
| K3 gegen die Baselines | I14 | `CYCLE_SIBLING` | Treffer (K1) | nicht ausdrückbar (K3) | **K3 nicht ausdrückbar** |
| K3 gegen die Baselines | I15 | `CYCLE_SIBLING` | Treffer (K1) | nicht ausdrückbar (K3) | **K3 nicht ausdrückbar** |
| K3 gegen die Baselines | I16 | `CYCLE_PARENT_CHILD` | Treffer (K1) | nicht ausdrückbar (K3) | **K3 nicht ausdrückbar** |
| K3 gegen die Baselines | I17 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I18 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I19 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I20 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I21 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I22 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I23 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I24 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I25 | `INCORRECT_LOCATION` | Treffer (K4) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I26 | `INCORRECT_LOCATION` | Treffer (K4) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I27 | `INCORRECT_LOCATION` | Treffer (K4) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I28 | `INCORRECT_LOCATION` | Treffer (K4) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I29 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I30 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I31 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I32 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | **Aggregat** | alle 32 | *ausserhalb des Nenners:* Baseline nicht ausdrückbar 8 · K3 nicht ausdrückbar 4 · beide Seiten nicht ausdrückbar 0 · nicht beurteilbar 0 | *Nenner = die vier Zustände* | **nur Baseline 0 · nur K3 0 · beide 20 · keiner 0 — Nenner 20** |

### T10b — Metrik `strict`

| Gruppe | Injektion | Szenario (Ebene 2) | Baselineseite (Vereinigung K1 ∪ K4 ∪ K5) | LLM-Seite | Zustand |
|---|---|---|---|---|---|
| K2 gegen die Baselines | I01 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I02 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I03 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I04 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I05 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I06 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I07 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I08 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I09 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I10 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I11 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I12 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I13 | `CYCLE_SIBLING` | Treffer (K1, K4) | nicht ausdrückbar (K2) | **K2 nicht ausdrückbar** |
| K2 gegen die Baselines | I14 | `CYCLE_SIBLING` | Treffer (K1, K4) | nicht ausdrückbar (K2) | **K2 nicht ausdrückbar** |
| K2 gegen die Baselines | I15 | `CYCLE_SIBLING` | Treffer (K1, K4) | nicht ausdrückbar (K2) | **K2 nicht ausdrückbar** |
| K2 gegen die Baselines | I16 | `CYCLE_PARENT_CHILD` | Treffer (K1) | nicht ausdrückbar (K2) | **K2 nicht ausdrückbar** |
| K2 gegen die Baselines | I17 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Verfehlung (K2) | **nur Baseline** |
| K2 gegen die Baselines | I18 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I19 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K2) | **beide** |
| K2 gegen die Baselines | I20 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Verfehlung (K2) | **nur Baseline** |
| K2 gegen die Baselines | I21 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I22 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I23 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I24 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I25 | `INCORRECT_LOCATION` | Verfehlung (K4) | Treffer (K2) | **nur K2** |
| K2 gegen die Baselines | I26 | `INCORRECT_LOCATION` | Verfehlung (K4) | Treffer (K2) | **nur K2** |
| K2 gegen die Baselines | I27 | `INCORRECT_LOCATION` | Verfehlung (K4) | Treffer (K2) | **nur K2** |
| K2 gegen die Baselines | I28 | `INCORRECT_LOCATION` | Verfehlung (K4) | Verfehlung (K2) | **keiner** |
| K2 gegen die Baselines | I29 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I30 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I31 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | I32 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K2) | **Baseline nicht ausdrückbar** |
| K2 gegen die Baselines | **Aggregat** | alle 32 | *ausserhalb des Nenners:* Baseline nicht ausdrückbar 8 · K2 nicht ausdrückbar 4 · beide Seiten nicht ausdrückbar 0 · nicht beurteilbar 0 | *Nenner = die vier Zustände* | **nur Baseline 2 · nur K2 3 · beide 14 · keiner 1 — Nenner 20** |
| K3 gegen die Baselines | I01 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I02 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I03 | `LAYER_BACK_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I04 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I05 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I06 | `LAYER_SKIP_CALL` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I07 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I08 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I09 | `PROTECTED_MODULE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I10 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I11 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I12 | `INDEPENDENCE` | Treffer (K1, K4, K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I13 | `CYCLE_SIBLING` | Treffer (K1, K4) | nicht ausdrückbar (K3) | **K3 nicht ausdrückbar** |
| K3 gegen die Baselines | I14 | `CYCLE_SIBLING` | Treffer (K1, K4) | nicht ausdrückbar (K3) | **K3 nicht ausdrückbar** |
| K3 gegen die Baselines | I15 | `CYCLE_SIBLING` | Treffer (K1, K4) | nicht ausdrückbar (K3) | **K3 nicht ausdrückbar** |
| K3 gegen die Baselines | I16 | `CYCLE_PARENT_CHILD` | Treffer (K1) | nicht ausdrückbar (K3) | **K3 nicht ausdrückbar** |
| K3 gegen die Baselines | I17 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I18 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I19 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I20 | `MISSING_PORT_REFERENCE` | Treffer (K5) | Treffer (K3) | **beide** |
| K3 gegen die Baselines | I21 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I22 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I23 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I24 | `FRAMEWORK_TYPE_IN_SIGNATURE` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I25 | `INCORRECT_LOCATION` | Verfehlung (K4) | Treffer (K3) | **nur K3** |
| K3 gegen die Baselines | I26 | `INCORRECT_LOCATION` | Verfehlung (K4) | Treffer (K3) | **nur K3** |
| K3 gegen die Baselines | I27 | `INCORRECT_LOCATION` | Verfehlung (K4) | Treffer (K3) | **nur K3** |
| K3 gegen die Baselines | I28 | `INCORRECT_LOCATION` | Verfehlung (K4) | Treffer (K3) | **nur K3** |
| K3 gegen die Baselines | I29 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I30 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I31 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | I32 | `SIGNATURE_DEVIATION` | nicht ausdrückbar (K1, K4, K5) | Treffer (K3) | **Baseline nicht ausdrückbar** |
| K3 gegen die Baselines | **Aggregat** | alle 32 | *ausserhalb des Nenners:* Baseline nicht ausdrückbar 8 · K3 nicht ausdrückbar 4 · beide Seiten nicht ausdrückbar 0 · nicht beurteilbar 0 | *Nenner = die vier Zustände* | **nur Baseline 0 · nur K3 4 · beide 16 · keiner 0 — Nenner 20** |

**Wie die Aggregatzeile zu lesen ist.** Der **Nenner** ist die Zahl der
Injektionen in den **vier** Zuständen — `nur Baseline`, `nur K2` bzw. `nur K3`,
`beide`, `keiner`. Die Klassen daneben stehen **ausserhalb** des Nenners und
werden einzeln beziffert; eine Rate über weniger Injektionen ist eine andere Rate
(dieselbe Auflage wie T5 (2)). **Probe:** Nenner plus die vier ausgewiesenen
Klassen ergibt die Injektionszahl der Zeilengruppe.

**Zustand je Seite, in der Reihenfolge von T5 Auflage (2):** `n. b.` und `n. e.`
(keine Messung) · ` — ` (nicht ausdrückbar, T8/T8.1) · vorregistrierte Sonderklasse
T9 Fall 6/7 · Wert 1 (Treffer) · Wert 0 (Verfehlung). Eine ` — `-Zelle, die
**zugleich** eine Sonderklasse trägt — K2/`CYCLE` und K3/`CYCLE` —, bleibt **nicht
ausdrückbar**: ` — ` ist eine Aussage über das **Werkzeug**, die Sonderklasse eine
über einen **Fund**. Eine Seite ist **Treffer**, sobald **eine** ihrer Zellen
trifft; sonst **Verfehlung**, sobald **eine** verfehlt; sonst **nicht ausdrückbar**,
wenn **alle** es sind; sonst **nicht beurteilbar**.

> **Was T10 NICHT ist.** Kein Non-Inferiority-Test, keine Rangfolge, keine Aussage
> darüber, welche Seite die bessere ist. Sie zählt aus, **wo sich die Trefferseiten
> schneiden und wo nicht**; die Deutung gehört nach Kapitel 8.

