# MANIFEST — K3-Block der Konformitätskampagne (DigitalOcean-Direktzugang)

> ~~**DIESER BLOCK IST NICHT ABGESCHLOSSEN.** 22 der 32 Injektionen sind gültig, 10 sind
> offen: I05, I06, I07, I09, I11, I13, I16, I20, I21, I23~~ · ~~fortgeschrieben am
> 28.08.2026 (C10c): jetzt 29 der 32 gültig, DREI sind offen — I09, I11, I23~~ —
> **abgeschlossen am 28.08.2026 (C10d): 32 von 32 Injektionen tragen einen gültigen Lauf,
> keine ist offen.** Jede Ungültigkeit auf dem Weg dorthin hatte denselben Grund,
> **Ratelimit (HTTP 429)** des Endpunkts; **kein einziger Call lieferte je eine ungültige
> Antwort**.
>
> **Die 32 gültigen Läufe sind zu FÜNF verschiedenen Zeitpunkten und unter unterschiedlichen,
> nicht kontrollierten serverseitigen Bedingungen entstanden.** Verteilung der gültigen Läufe:
>
> | Zeitpunkt (CEST) | Injektionen |
> |---|---|
> | 27.08., 09:00-Stunde | 7 |
> | 27.08., 10:00-Stunde | 14 |
> | 27.08., 12:00-Stunde | 1 (I22) |
> | 28.08., 08:00-Stunde | 7 |
> | 28.08., 09:00-Stunde | 3 (I09, I11, I23) |
>
> 21 Injektionen wurden im **ersten** Versuch gültig, 1 im zweiten, 7 im dritten, 1 im fünften,
> 2 im sechsten. Der Endpunkt ist **nicht gepinnt** (§6 Rev. 32), seine Auslastung ist weder
> gemessen noch kontrollierbar; **T14 (§9) gilt für diese Streuung in vollem Umfang** und ist
> bei jeder Auswertung mitzuführen.

**Datum der Läufe:** 27. August 2026 — Versuch 1: 09:04:59–10:58:54 CEST · Versuch 2
(Wiederholung der elf ungültigen): 12:00:07–12:19:18 CEST · **28. August 2026 — Versuche 3
und 4 (C10c, die zehn offenen): 08:02:13–08:20:40 CEST · Versuche 5 und 6 (C10d, die drei
offenen, EINZELAUFRUFE mit Pausen): 08:51:41–09:32:21 CEST**
**Auftrag:** C10 Phase 2, fortgeschrieben durch C10c und **abgeschlossen durch C10d**
**Bericht:** [`docs/repo-kontext/c10_bericht_kampagne.md`](../../../docs/repo-kontext/c10_bericht_kampagne.md)
**Protokollbezug:** §0.1 (Messstand, Amendments Rev. 34/35), §6 Rev. 32 (Direktzugang, kein
Pin), §6 Nachtrag Rev. 24 (Aufrufspezifikation), Rev. 25 (getrennte Recordmengen), Rev. 26
(Wiederholungsfaktor, Exit-Code kein Gültigkeitskriterium), §7 (Wiederholung bei
Transportfehler), §9 T14 (Anbieter- und Endpunktwechsel)

> **Nicht reproduzierbar. Niemals überschreiben.** Wiederholungen liegen auf `_r<n>`-Pfaden
> neben dem Erstversuch; kein Artefakt wurde ersetzt.

> **Keine Auswertung.** Rohbestand. Metriken, Findingbeurteilung und Vergleiche gehören nach
> C6b; die Eine-Iteration-Regel (§7) und die Amendment-Sperre aus §0.1 gelten.

## Messstand (§6 Punkt 4)

| Grösse | Wert |
|---|---|
| **Datum** | 27.08.2026, 09:04:59–12:19:18 CEST (zwei Versuche) |
| **Repo-Commit (Messgegenstand)** | je Injektion `inj/01`…`inj/32`, sternförmig an `baseline` = `0d651041ed87dd03f2f78359713633fac01c0a66`; `--base` durchgehend dieser SHA |
| **Checker-Commit** | `348ca9daa456af4954f11f7152fc45201035297e` (Tag `phase04-freeze`, Messpfad `~/ma/tritongraph-measure`) |
| **Checker-Artefakt** | `dist/cli.js` = `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` |
| **Prompt-Hash** | `prompt_template_sha256` = `65e78f38e7b1fee20000ea70c654df042f5e0831fc6a68ccb340f833bd915035` |
| **Regel-Hash** | `rules_sha256` = `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` |
| **Topologie-Hash** | `topology_sha256` = `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` |
| **Modell** | `nvidia-nemotron-3-super-120b` · Endpoint `https://inference.do-ai.run/v1` · **kein Pin** (§6 Rev. 32) · `seed=42`, `temperature=0` |
| **Kontextfenster** | **1 000 000** (Katalogwert, §1 Nachtrag Rev. 30) · `--timeout-ms 600000` |
| **Runner-Commit** | `4caf083d5e21f36440579af6888513ca897f1dd4` |

`model_version` meldet in **allen** gemessenen Calls zeichengleich `nvidia-nemotron-3-super-120b`;
`provider_served` ist auf dem Direktweg durchgehend `null` — beides wie in T14 beschrieben.

## Gültigkeit

Entschieden allein von `tools/postrun_check.py` (§6 Nachtrag Rev. 24); der Exit-Code ist
**kein** Kriterium (Rev. 26).

| Grösse | Wert |
|---|---|
| Injektionen mit gültigem Lauf | **32 von 32** |
| Injektionen **ohne** gültigen Lauf | **keine** |
| Invocationen gesamt (inkl. Wiederholungen) | **61** — 32 VALID, 29 INVALID |
| Calls gesamt | **183** |
| davon `outcome: measured` | **133** |
| davon `outcome: transport_failed` | **50** |
| `calls_invalid` (ungültige Modellantwort) | **0** |
| `http_429`-Ereignisse | **194** |
| `valid_final` über die gemessenen Calls | **133 / 133 = 1,000** |
| `changed_files_count == 1` | in allen 61 |
| max `tokens_in_total + tokens_out_total` je Call | **3058** (I08) gegen Fenster **1 000 000** — **0** Überschreitungen |
| Records `DERIVED:` / übrige | **35** / **133** |
| externe Wanduhrzeit, Summe | **9 190 542 ms** (153,2 min) |

**Kein einziger Call lieferte eine ungültige Antwort.** Jede Ungültigkeit stammt aus dem
Transport: das Retry-Budget (`transport_max_retries: 2`, also drei Versuche) reichte unter
der beobachteten 429-Rate nicht aus.

## Verlauf der Wiederholungen (§7)

| Injektion | V1 | V2 | V3 | V4 | V5 | V6 |
|---|---|---|---|---|---|---|
| die 21 sofort gültigen | **VALID** | — | — | — | — | — |
| I22 | INVALID | **VALID** | — | — | — | — |
| I05, I06, I07, I13, I16, I20, I21 | INVALID | INVALID | **VALID** | — | — | — |
| I09 | INVALID | INVALID | INVALID | INVALID | **VALID** | — |
| I11 | INVALID | INVALID | INVALID | INVALID | INVALID | **VALID** |
| I23 | INVALID | INVALID | INVALID | INVALID | INVALID | **VALID** |

Versuch 2 (27.08., 12:00 CEST) rettete **eine** von elf; der Block wurde angehalten.
Versuch 3 (28.08., 08:02 CEST, **unverändertes Werkzeug**, nur ein anderes Zeitfenster) rettete
**sieben** von zehn. Versuch 4 über die verbleibenden drei scheiterte **hart** — je 3 von 3
Calls, je Injektion in unter 19 Sekunden, also sofortige 429 ohne Antwort. Neun
aufeinanderfolgende gescheiterte Calls, weit über dem Richtwert von fünf: erneut
**angehalten**.

**C10d (28.08., 08:51–09:32 CEST) schloss den Block mit EINZELAUFRUFEN und Pausen.** Statt
eines Aufrufs über alle drei offenen Injektionen wurde je Injektion ein eigener Runner-Aufruf
gefahren, mit mindestens zehn Minuten Abstand. Begründung: das Limit ist **schubweise**, nicht
monoton — Einzelaufrufe mit Abstand treffen mit höherer Wahrscheinlichkeit einen offenen
Schub. **Die Aufrufplanung ist der einzige bewegte Parameter**; Retry-Budget, Pacing im
Werkzeug und Runner-Commit blieben unverändert.

| Aufruf | Zeit (CEST) | Injektion | Ergebnis |
|---|---|---|---|
| 1 | 08:51:41–08:53:04 | I23 | INVALID — 3/3 Calls in **18,98 s** → Schub geschlossen, 30 min Sperre |
| 2 | 09:03:16–09:05:23 | I09 | **VALID** (123 315 ms) |
| 3 | 09:06:46–09:07:45 | I11 | INVALID — 2/3 Calls, 54,5 s (keine Schubsperre) |
| 4 | 09:17:58–09:19:58 | I11 | **VALID** (124 780 ms) |
| 5 | 09:30:05–09:32:21 | I23 | **VALID** (140 659 ms) |

**Vorab festgelegte Obergrenze:** höchstens **drei** weitere Versuche je offener Injektion,
insgesamt an diesem Tag. Verbraucht wurden **2 von 3** für I23, **1 von 3** für I09 und
**2 von 3** für I11 — die Grenze wurde nicht ausgeschöpft und nicht überschritten.

**Kein Werkzeug wurde geändert.** Retry-Budget, Pacing und Runner stehen unverändert auf dem
in §0.1 registrierten Stand (`4caf083`); §7 registriert den **Neustart**, nicht die Änderung
des Werkzeugs. Der einzige bewegte Parameter ist das **Zeitfenster**.

**Zeitliche Lage der 429 im Erstversuch** (UTC, Zehn-Minuten-Fächer, Calls / 429-Ereignisse):

```
07:00  4/1    07:10  8/1    07:20  8/14   07:30  6/7
07:40  5/0    07:50  9/12   08:00 11/11   08:10 11/14
08:20 11/17   08:30 11/0    08:40  5/0    08:50  7/0
```

Längste Folge aufeinanderfolgender gescheiterter Calls im Erstversuch: **4** (Richtwert 5).
Die Abbruchschwelle war **während** des Erstversuchs nicht erreicht; er lief mit Fortschritt
durch. Die letzten drei Fächer tragen **null** 429.

**Zeitliche Lage am 28.08. (C10c, CEST, Calls / 429-Ereignisse / gescheiterte Calls):**

```
08:00  14/11/2    08:10  19/14/4    08:20   6/18/6
08:50   3/ 9/3    09:00   6/ 7/2    09:10   3/ 0/0    09:30   3/ 0/0
```

Das Fenster war zu Beginn tragfähig — die ersten sieben Injektionen kamen durch — und schloss
sich im Verlauf einer knappen halben Stunde: im Fächer 08:20 kommen auf 6 Calls 18
429-Ereignisse, alle sechs Calls scheitern. Danach das **schubweise** Muster, an dem die
C10d-Aufrufplanung ansetzt: 08:50 wieder geschlossen (3 Calls, 9 Ereignisse, alle drei
gescheitert), 09:00 halb offen (6 Calls, 7 Ereignisse, zwei gescheitert), **09:10 und 09:30
vollständig offen — null 429**. **Das Zeitfenster ist der einzige beobachtete Hebel; es ist
weder gemessen noch kontrollierbar** (T14, §9).

## Inhalt

| Pfad | Inhalt |
|---|---|
| `data/campaign/k3/k3_<repo-sha>.jsonl` / `.json` | Erstversuch je Injektion |
| `data/campaign/k3/k3_<repo-sha>_r2.jsonl` / `.json` | Wiederholung, **neben** dem Erstversuch |
| `data/campaign/manifests/k3_<repo-sha>[_r2].json` | Laufmanifest je Versuch |
| `data/campaign/k3/SHA256SUMS` | ~~129~~ ~~168~~ **183 Zeilen**, neu erzeugt nach C10d, Stand bei Abschluss |

**`SHA256SUMS` ist ein Stand, kein Abschluss.** Der Block ist abgeschlossen; die Datei
bewegt sich nicht mehr.
`data/campaign/journal.jsonl` steht wie beim K2-Block bewusst **nicht** darin — sie ist
append-only. Schnappschuss bei Abschluss des Blocks nach C10d, 61 K3-Einträge:

```
e594e77dbe94197616ac6963fa253f6d083f66bb56899fba861962f0297d3335  data/campaign/journal.jsonl
```

## Offen

~~Die zehn Injektionen ohne gültigen Lauf.~~ · ~~fortgeschrieben am 28.08.2026 (C10c):
noch drei — `I09`, `I11`, `I23`.~~ — **erledigt am 28.08.2026 (C10d): keine offene Injektion
mehr, K3 trägt 32 von 32.**

Was **bleibt**, ist kein offener Punkt, sondern eine Eigenschaft des Bestandes: die 32 gültigen
Läufe stammen aus **fünf** Zeitfenstern über zwei Tage, und der Endpunkt ist in dieser Zeit
weder gepinnt noch in seiner Auslastung gemessen. **T14 (§9) ist bei jeder Auswertung dieses
Blocks mitzuführen.**
