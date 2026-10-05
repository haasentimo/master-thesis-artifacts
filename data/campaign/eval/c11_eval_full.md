# C11 — Ausgabekopf (Laufidentifikation)

Dieser Kopf ist dem unveränderten Rendering vorangestellt; darunter beginnt die
Harness-Ausgabe bytegleich mit ihrer ersten Zeile.

- **Auftrag:** C11 — erster und einziger Auswertungslauf über den vollständigen Messbestand
- **Zeitstempel:** 2026-08-28T13:16:10+02:00 bis 2026-08-28T13:16:11+02:00 (0.29 s wall, 23868 KB maxrss)
- **cwd:** `/home/haasentimo/ma/masterarbeit`
- **git HEAD:** `dc865d1aa90fb0816ac5f9d7bcd268025fdfe9bf`
- **Maschine:** DESKTOP-PJA89CF · Linux 5.15.153.1-microsoft-standard-WSL2 x86_64
- **Aufrufzeile:** `python3 tools/evaluate_campaign.py --with-campaign --json-out data/campaign/eval/c11_eval_full.json --markdown-out data/campaign/eval/c11_eval_full.md`  → Exit 0

**Instrumente (SHA256):**

- `tools/evaluate_campaign.py` — `5125cd595913b1226b888e67035f24f2831e0f4818b28dad4b261a57a0528eed`
- `tools/match_k4k5.py` — `ad3edcb1ee8537ee758d8212055371957c0493f3d8e218267d182fb9fc060022`
- `tools/check_doc_invariants.py` — `6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018`

**Protokoll:** `9e63c37067a5a62ef95dd2d0710620939b9f03e5b0258995f01e597db5653f48`  
**Auswertungsspezifikation:** `50f593d07801dd421aad1e644016bf4861af382afbc41749546e1ecad8785017`

**Messbestand `data/campaign/` (SHA256 des Block-`SHA256SUMS`, gelistete Artefakte):**

| Block | SHA256 des `SHA256SUMS` | gelistete Artefakte |
| --- | --- | --- |
| control | `c9699b4417833a6a6a006ce51ce5062589c3c4a1266bb6ea5579539ac2b8fdda` | 14 |
| k1 | `ced9954f333936dc20630f91b275f63a47e7e69f9d530bf8a0abe5680ead6907` | 96 |
| k2 | `debd5a93309e682126de886928b6fcc1c9ba4e2dd9548d2037f33512ac1bb26e` | 96 |
| k3 | `7023d23663ba022dff98a4d888cde16e3f3b198849144344a6ba83a1281bfb88` | 183 |
| k4 | `cc8dbce674920d2a61f9954eca3fa6eb766e971705283f8ca4321fa9906f29d0` | 96 |
| k5 | `07ff89aaff4956afc2dfb3b88efa7b3fa548dcc8d4978c49a56677ba3b0d0741` | 96 |

Laufmanifeste unter `data/campaign/manifests/`: 189 JSON-Dateien.

**Rohausgabe vor Kopfeinfügung (SHA256):**

- `c11_eval_full.json` — `28fc40bb334f73615b669cda45eccd8cca62d71d49aa613d429ddd0e2075283c`
- `c11_eval_full.md` — `aecba18c8187f8bdd2693883cf46406687f42fd7ce55e7cd9809793af43c8df5`

Markdown: Kopf vorangestellt, Rendering danach bytegleich. JSON: ein Schlüssel `c11_run_head` nach der öffnenden Klammer eingefügt, alle Ergebniswerte bytegleich. Keine Zelle angefasst.

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
| `LAYER_BACK_CALL` | 3 | ja | ja | ja | ja | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | |
| `LAYER_SKIP_CALL` | 3 | ja | ja | ja | ja | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | |
| `PROTECTED_MODULE` | 3 | ja | ja | ja | ja | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | |
| `INDEPENDENCE` | 3 | ja | ja | ja | ja | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | |
| `CYCLE_SIBLING` | 3 | ja | ja | teilweise | nein | 3/3 | `n. b.` | 0/3 | ` — ` | ` — ` | |
| `CYCLE_PARENT_CHILD` | 1 | ja | nein | teilweise | nein | 1/1 | `n. b.` | 0/1 | ` — ` | ` — ` | |
| `MISSING_PORT_REFERENCE` | 4 | nein | nein | ja | ja | ` — ` | ` — ` | 4/4 | 4/4 | 4/4 | |
| `FRAMEWORK_TYPE_IN_SIGNATURE` | 4 | nein | nein | nein | ja | ` — ` | ` — ` | ` — ` | 4/4 | 3/4 | |
| `INCORRECT_LOCATION` | 4 | nein | teilweise | nein | ja | ` — ` | 4/4 | ` — ` | 3/4 | 4/4 | |
| `SIGNATURE_DEVIATION` | 4 | nein | nein | nein | ja | ` — ` | ` — ` | ` — ` | 4/4 | 4/4 | |

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
| `CYCLE_SIBLING` (3) | 3/3 | 3/3 | ` — ` | ` — ` | **49/52** | ` — ` | ` — ` | **1/52** | `n. b.` | 3/3 | 0/3 | 0/3 |
| `CYCLE_PARENT_CHILD` (1) | 1/1 | 1/1 | ` — ` | ` — ` | **49/52** | ` — ` | ` — ` | **1/52** | `n. b.` | ` — ` | 0/1 | 0/1 |
| `MISSING_PORT_REFERENCE` (4) | ` — ` | ` — ` | 4/4 | 2/4 | **49/52** | 4/4 | 4/4 | **1/52** | ` — ` | ` — ` | 4/4 | 4/4 |
| `FRAMEWORK_TYPE_IN_SIGNATURE` (4) | ` — ` | ` — ` | 4/4 | 4/4 | **49/52** | 3/4 | 3/4 | **1/52** | ` — ` | ` — ` | ` — ` | ` — ` |
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
| K2 | **findingweise** (Findings gesamt, undedupliziert) | Bezug für `strict` und Precision | 155 | 153 | 153 | **153** | 153–155 | — |
| K3 | **modulweise** (Module mit ≥ 1 Finding / 52) | Bezug für `localized` | 2 | 1 | 0 | **1** | 0–2 | **1/52** |
| K3 | **findingweise** (Findings gesamt, undedupliziert) | Bezug für `strict` und Precision | 2 | 1 | 0 | **1** | 0–2 | — |

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

| ID | Szenario | Trägermodul | K2 Ruhe | K2 Kampagne | K2 Δ | K2 `strict` | K2 `loc` | K2 SV | K2 kein-EN | K3 Ruhe | K3 Kampagne | K3 Δ | K3 `strict` | K3 `loc` | K3 SV | K3 kein-EN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I01 | `LAYER_BACK_CALL` | `depot.identity.repository.customer_repo` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I02 | `LAYER_BACK_CALL` | `depot.orders.repository.order_repo` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I03 | `LAYER_BACK_CALL` | `depot.billing.repository.invoice_repo` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I04 | `LAYER_SKIP_CALL` | `depot.identity.api.routes` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I05 | `LAYER_SKIP_CALL` | `depot.orders.api.routes` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I06 | `LAYER_SKIP_CALL` | `depot.billing.api.routes` | 2 | 2 | 0 | 1 | 1 | nein | ja | 0 | 0 | 0 | 1 | 1 | nein | ja |
| I07 | `PROTECTED_MODULE` | `depot.identity.services.customer_service` | 2 | 2 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I08 | `PROTECTED_MODULE` | `depot.orders.services.order_service` | 3 | 2 | -1 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I09 | `PROTECTED_MODULE` | `depot.billing.services.invoice_service` | 3 | 3 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I10 | `INDEPENDENCE` | `depot.orders.services.checkout_service` | 2 | 3 | 1 | 1 | 1 | nein | nein | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I11 | `INDEPENDENCE` | `depot.billing.services.dunning_service` | 3 | 3 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I12 | `INDEPENDENCE` | `depot.orders.repository.order_line_repo` | 1 | 2 | 1 | 1 | 1 | nein | nein | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I13 | `CYCLE_SIBLING` | `depot.identity.mappers.customer_mapper` | 1 | 1 | 0 | ` — ` | ` — ` | nein |  | 0 | 1 | 1 | ` — ` | ` — ` | nein |  |
| I14 | `CYCLE_SIBLING` | `depot.orders.mappers.order_mapper` | 0 | 0 | 0 | ` — ` | ` — ` | nein |  | 0 | 1 | 1 | ` — ` | ` — ` | nein |  |
| I15 | `CYCLE_SIBLING` | `depot.billing.mappers.invoice_mapper` | 0 | 0 | 0 | ` — ` | ` — ` | nein |  | 0 | 1 | 1 | ` — ` | ` — ` | nein |  |
| I16 | `CYCLE_PARENT_CHILD` | `depot.orders.services.pricing.engine` | 1 | 1 | 0 | ` — ` | ` — ` | nein |  | 0 | 0 | 0 | ` — ` | ` — ` | nein |  |
| I17 | `MISSING_PORT_REFERENCE` | `depot.identity.services.token_service` | 1 | 1 | 0 | 0 | 1 | ja |  | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I18 | `MISSING_PORT_REFERENCE` | `depot.orders.services.catalog_service` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I19 | `MISSING_PORT_REFERENCE` | `depot.orders.services.refund_service` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I20 | `MISSING_PORT_REFERENCE` | `depot.billing.services.ledger_service` | 1 | 1 | 0 | 0 | 1 | ja |  | 0 | 0 | 0 | 1 | 1 | nein | ja |
| I21 | `FRAMEWORK_TYPE_IN_SIGNATURE` | `depot.identity.models.customer_models` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 0 | 0 | 1 | 1 | nein | ja |
| I22 | `FRAMEWORK_TYPE_IN_SIGNATURE` | `depot.orders.models.order_models` | 5 | 1 | -4 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I23 | `FRAMEWORK_TYPE_IN_SIGNATURE` | `depot.orders.models.order_line_models` | 4 | 1 | -3 | 1 | 1 | nein | ja | 0 | 0 | 0 | 0 | 0 | nein |  |
| I24 | `FRAMEWORK_TYPE_IN_SIGNATURE` | `depot.billing.models.invoice_models` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I25 | `INCORRECT_LOCATION` | `depot.orders.legacy_order_index` | 0 | 1 | 1 | 1 | 1 | nein | nein | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I26 | `INCORRECT_LOCATION` | `depot.billing.legacy_invoice_index` | 0 | 1 | 1 | 1 | 1 | nein | nein | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I27 | `INCORRECT_LOCATION` | `depot.identity.legacy_token_index` | 0 | 1 | 1 | 1 | 1 | nein | nein | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I28 | `INCORRECT_LOCATION` | `depot.billing.legacy_tax_models` | 0 | 0 | 0 | 0 | 0 | nein |  | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I29 | `SIGNATURE_DEVIATION` | `depot.identity.repository.session_repo` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I30 | `SIGNATURE_DEVIATION` | `depot.orders.repository.order_query` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |
| I31 | `SIGNATURE_DEVIATION` | `depot.billing.repository.invoice_query` | 1 | 1 | 0 | 1 | 1 | nein | ja | 1 | 1 | 0 | 1 | 1 | nein | ja |
| I32 | `SIGNATURE_DEVIATION` | `depot.orders.mappers.order_line_mapper` | 1 | 1 | 0 | 1 | 1 | nein | ja | 0 | 1 | 1 | 1 | 1 | nein | nein |

**Spaltenbedeutung.** **Ruhe** = Ruhezustandszahl desselben Moduls in derselben
Kategorie aus C3b (Median über drei Läufe) · **Kampagne** = dieselbe Zählgrösse auf
dem Injektionscommit · **Δ** = Kampagne − Ruhe · **SV** = Schreibweisenverfehlung,
mechanisch gebildet (`localized` Treffer **und** `strict` 0 **und** Abweichung allein
in Segment 4) · **kein-EN** = ein `strict`-Treffer, der die Ruhezustandsrate **nicht
übersteigt**, wird nicht als Erkennungsnachweis geführt.

### T4 Symmetrieteil — K1, K4, K5

| ID | K1 Ruhe | K1 Kampagne | K1 Δ | K4 Ruhe | K4 Kampagne | K4 Δ | K5 Ruhe | K5 Kampagne | K5 Δ |
|---|---|---|---|---|---|---|---|---|---|
| I01 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I02 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I03 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I04 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I05 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I06 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I07 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I08 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I09 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I10 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I11 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I12 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I13 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I14 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I15 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I16 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I17 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I18 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I19 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I20 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I21 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I22 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I23 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I24 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I25 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I26 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I27 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I28 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I29 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I30 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I31 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |
| I32 | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  | 0 ᴬ¹⁴ |  |  |

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
| K1 | `FORBIDDEN_RELATION` | 12 |  |  |  |  |  |  | `n. b.` |
| K1 | `CYCLE` | 4 |  |  |  |  |  |  | `n. b.` |
| K1 | `ABSENCE_REQUIRED` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K1 | `FORBIDDEN_SIGNATURE_TYPE` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K1 | `STRUCTURAL_PLACEMENT` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K1 | `API_CONTRACT` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K1 | **Gesamt — UF3, Abdeckung des Kategoriespektrums, Nenner 32 (alle Kategorien)** | 32 | | | | | | | `n. b.` |
| K1 | **Gesamt — UF4, Leistung im ausdrückbaren Bereich, Nenner 16** | 16 | | | | | | | `n. b.` |
| K2 | `FORBIDDEN_RELATION` | 12 |  |  |  |  |  |  | **49/52** |
| K2 | `CYCLE` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | **49/52** |
| K2 | `ABSENCE_REQUIRED` | 4 |  |  |  |  |  |  | **49/52** |
| K2 | `FORBIDDEN_SIGNATURE_TYPE` | 4 |  |  |  |  |  |  | **49/52** |
| K2 | `STRUCTURAL_PLACEMENT` | 4 |  |  |  |  |  |  | **49/52** |
| K2 | `API_CONTRACT` | 4 |  |  |  |  |  |  | **49/52** |
| K2 | **Gesamt — UF3, Abdeckung des Kategoriespektrums, Nenner 32 (alle Kategorien)** | 32 | | | | | | | **49/52** |
| K2 | **Gesamt — UF4, Leistung im ausdrückbaren Bereich, Nenner 28** | 28 | | | | | | | **49/52** |
| K3 | `FORBIDDEN_RELATION` | 12 |  |  |  |  |  |  | **1/52** |
| K3 | `CYCLE` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | **1/52** |
| K3 | `ABSENCE_REQUIRED` | 4 |  |  |  |  |  |  | **1/52** |
| K3 | `FORBIDDEN_SIGNATURE_TYPE` | 4 |  |  |  |  |  |  | **1/52** |
| K3 | `STRUCTURAL_PLACEMENT` | 4 |  |  |  |  |  |  | **1/52** |
| K3 | `API_CONTRACT` | 4 |  |  |  |  |  |  | **1/52** |
| K3 | **Gesamt — UF3, Abdeckung des Kategoriespektrums, Nenner 32 (alle Kategorien)** | 32 | | | | | | | **1/52** |
| K3 | **Gesamt — UF4, Leistung im ausdrückbaren Bereich, Nenner 28** | 28 | | | | | | | **1/52** |
| K4 | `FORBIDDEN_RELATION` | 12 |  |  |  |  |  |  | `n. b.` |
| K4 | `CYCLE` | 4 |  |  |  | `n. b.`ᵃ | `n. b.`ᵃ | `n. b.`ᵃ | `n. b.` |
| K4 | `ABSENCE_REQUIRED` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K4 | `FORBIDDEN_SIGNATURE_TYPE` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K4 | `STRUCTURAL_PLACEMENT` | 4 |  |  |  |  |  |  | `n. b.` |
| K4 | `API_CONTRACT` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K4 | **Gesamt — UF3, Abdeckung des Kategoriespektrums, Nenner 32 (alle Kategorien)** | 32 | | | | | | | `n. b.` |
| K4 | **Gesamt — UF4, Leistung im ausdrückbaren Bereich, Nenner 19** | 19 | | | | | | | `n. b.` |
| K5 | `FORBIDDEN_RELATION` | 12 |  |  |  |  |  |  | `n. b.` |
| K5 | `CYCLE` | 4 |  |  |  |  |  |  | `n. b.` |
| K5 | `ABSENCE_REQUIRED` | 4 |  |  |  |  |  |  | `n. b.` |
| K5 | `FORBIDDEN_SIGNATURE_TYPE` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K5 | `STRUCTURAL_PLACEMENT` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K5 | `API_CONTRACT` | 4 | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | ` — ` | `n. b.` |
| K5 | **Gesamt — UF3, Abdeckung des Kategoriespektrums, Nenner 32 (alle Kategorien)** | 32 | | | | | | | `n. b.` |
| K5 | **Gesamt — UF4, Leistung im ausdrückbaren Bereich, Nenner 20** | 20 | | | | | | | `n. b.` |

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
| K1 | | | | |  | ` — ` | ` — ` | ` — ` | ` — ` |
| K2 | | | | |  |  |  |  |  |
| K3 | | | | |  |  |  |  |  |
| K4 | | | | | `n. b.`ᵃ | ` — ` | ` — ` | ` — ` | ` — ` |
| K5 | | | | | `n. b.`ᵃ | ` — ` | ` — ` | ` — ` | ` — ` |

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

| # | Fall | Pfad | Betroffen | Häufigkeit | Buchungsregel |
|---|---|---|---|---|---|
| 1 | `CYCLE`-Injektion (Modus `full`) erzeugt zusätzlich `layer-violation` | K1 | I13, I14, I15, I16 | 4 Records / 4 Läufe | `expected_co_findings`; **kein FP** |
| 2 | `FORBIDDEN_RELATION` erzeugt **keinen** `cycle`-Record | K1 | `FORBIDDEN_RELATION`-Injektionen | **Nullerwartung** | ein `cycle`-Record wäre ein **Befund** |
| 3 | `LAYER_BACK_CALL` von K4 **zweifach** gemeldet | K4 | I01, I02, I03 | 3 Records / 3 Läufe | vorregistrierte Doppelmeldung, **kein FP** |
| 4 | Adapterfassade `depot.core.adapters`, `R-PROTECT-1` | K2 | Kontrollset | **3/3 Läufe** | vorhergesagt, **kein** unerwarteter FP |
| 5 | Nicht-Träger-Portregel auf `orders_services` (`R-PORT-2`/`R-PORT-3`) | K2 | Kontrollset | **1/3 Läufe** | vorhergesagt, **kein** unerwarteter FP |
| 4 | Adapterfassade `depot.core.adapters`, `R-PROTECT-1` | K3 | Kontrollset | **0/3 Läufe** | vorhergesagt, **kein** unerwarteter FP |
| 5 | Nicht-Träger-Portregel auf `orders_services` (`R-PORT-2`/`R-PORT-3`) | K3 | Kontrollset | **0/3 Läufe** | vorhergesagt, **kein** unerwarteter FP |
| 6 | `CYCLE`: K2 meldet `FORBIDDEN_RELATION` am **richtigen Modul** | K2 | I13, I14, I15, I16 | 9 | **kein** Treffer, **kein** FP — „richtige Stelle, falsche Kategorie“ |
| 6 | `CYCLE`: K3 meldet `FORBIDDEN_RELATION` am **richtigen Modul** | K3 | I13, I14, I15, I16 |  | **kein** Treffer, **kein** FP — „richtige Stelle, falsche Kategorie“ |
| 7 | `CYCLE_*`: K5 meldet die Rückkante als **nicht gelistete Kante** | K5 | I13, I14, I15, I16 |  | `strict` kein Treffer · `localized` Treffer auf der **Stelle** — **ohne neue Regel** gebucht |

**Allgemeine Regel, von der die Fälle 6 und 7 die einzigen Ausnahmen sind:**
„falsche Regel/Kategorie, richtige Stelle“ → der `match_key` matcht nicht → zählt
als **FP *und* FN**.

