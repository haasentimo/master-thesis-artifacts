# Z1-T — Bericht: das Kontextfenster als Messeingang

**Masterarbeit Timo Haas · HTWG Konstanz**
**Datum:** 31. August 2026 · **Auftrag:** Z1-T
**Schreibendes Repo:** `masterarbeit`
**Nur lesend:** `ma-llm-arch-extractor` (HEAD `5c0b65a`), `tritongraph` (`348ca9d`), `tritongraph-measure` (`348ca9d`), `ma-conformance-testrepo` (`0d65104`)

> **Charakter dieses Dokuments.** Drei Teile in dieser Reihenfolge: **§1 der Nachweis** —
> lesend, mit Zahlen, mit einem Gatter am Ende; **§2 das Amendment** — vor dem Lauf, datiert,
> mit nachgezogenem Protokoll-SHA; **§3 die drei Läufe** — unter der registrierten Bedingung.
>
> **AUSWERTUNGSSPERRE, wie in Z1-R.** §3 berichtet **Gültigkeit, Zähler und Provenienz** —
> keine Kennzahl, kein Wert gegen §8, kein Vergleich zwischen Läufen oder Bedingungen, keine
> Deutung. Die Auswertung ist **Z1-A**.
>
> **Nicht Gegenstand:** K3, die Nachbesserungsregel für K3, ARI, Befund 07 und jede Änderung
> an Prompt, Schema, `metrics.py` oder Extractor.

**Vorberichte:** `z1_d_bericht_formausfall.md` (Diagnose der zwölf Läufe),
`z1_r_bericht_laeufe.md` (die zwölf Läufe), `z1_p_bericht_freeze.md` (Protokoll-Freeze).

---

## 0. Vorbedingungen

| Vorbedingung | Soll | Ist | |
|---|---|---|---|
| `git status --porcelain`, fünf Bäume | leer (`data/z1/` ausgenommen wie §6.1) | alle fünf leer | OK |
| `masterarbeit` | `main` @ `94241d9` zu Beginn | zeichengleich | OK |
| `ma-llm-arch-extractor` | `main` @ `5c0b65a` | zeichengleich | OK |
| `tritongraph` | `feat/conformance-checker` @ `348ca9d` | zeichengleich | OK |
| `tritongraph-measure` | @ `348ca9d` | zeichengleich | OK |
| `ma-conformance-testrepo` | `main` @ `0d65104` | zeichengleich | OK |
| `python3 tools/check_doc_invariants.py` vor dem Auftrag | Exit 0 | **Exit 0**, sechs Invarianten | OK |
| SHA256 des Z1-Protokolls vor dem Auftrag | `9e02556139bd…71f405` (Rev. 2) | zeichengleich | OK |

---

## 1. Phase 1 — der Nachweis

### 1.1 Wie der Prompt gezählt wurde, und warum so

**Kein Tokenizer-Paket auf diesem Rechner.** `transformers` und `tokenizers` sind nicht
installiert, ein Hugging-Face-Cache existiert nicht:

```
$ python3 -c "import transformers"
ModuleNotFoundError: No module named 'transformers'
$ python3 -c "import tokenizers"
ModuleNotFoundError: No module named 'tokenizers'
$ ls ~/.cache/huggingface
ls: cannot access '/home/haasentimo/.cache/huggingface': No such file or directory
```

**`/api/tokenize` gibt es in dieser Ollama-Fassung nicht** (HTTP 404, Version 0.32.15).
Gezählt wurde deshalb mit **dem Tokenizer, der die Messung selbst gefahren hat**: dem des
geladenen Modells, über Ollamas eigene Zahl `prompt_eval_count` bei `num_predict: 1`. Das
ist kein Ersatzmass, sondern die genauere Quelle — es ist derselbe Tokenizer, dieselbe
Modelldatei, dasselbe Chat-Template wie im Messlauf.

**Gezählt wurde das Blob-Rendering selbst.** Die archivierte Datei
`attempts/attempt_0/prompt.txt` trägt die beiden gesendeten Nachrichten mit den Marken
`### system` und `### user`; die Rückzerlegung ist bytegenau:

```
system 1 691 B + user 17 130 B + Marken 21 B = 18 842 B
SHA256 der Datei: cb2fcefddbbb1f2e81c62bc4b4231b458d12bfcc0948d3764dad7f287db0ee2d
```

**Die Zahlen:**

| Messung | `num_ctx` | gezählt |
|---|---|---|
| `/api/chat`, System- und Nutzernachricht wie gesendet (mit Chat-Template) | 32768 | **4 281** |
| dieselbe Messung | 16384 | **4 281** |
| dieselbe Messung | 8192 | **4 281** |
| dieselbe Messung | **4096** (Vorgabe) | **2 050** |
| `/api/generate` mit `raw: true`, die 18 842 Bytes ohne Template | 32768 | 4 274 |

**Der erwartete Wert liegt damit bei 4 281 Token, nicht bei den im Auftrag geschätzten
4 500–5 500.** Die Grössenordnung stimmt, die Zahl ist kleiner; berichtet wird die gemessene.

### 1.2 Modellgrenze und tatsächlich geladenes Fenster

```
$ ollama show qwen2.5-coder:7b
  Model
    architecture        qwen2
    parameters          7.6B
    context length      32768
    embedding length    3584
    quantization        Q4_K_M
```

`ollama ps` **vor jedem Call** — keine residente Instanz, die Spalte `CONTEXT` trägt nichts:

```
$ ollama ps
NAME    ID    SIZE    PROCESSOR    CONTEXT    UNTIL
```

Nach einem Anstosscall **ohne jede Option** (Methode aus C5 Schritt 3b — die Spalte trägt
nur eine residente Instanz, also erst laden, dann lesen):

```
$ ollama ps
NAME                ID              SIZE      PROCESSOR    CONTEXT    UNTIL
qwen2.5-coder:7b    dae161e27b0e    4.7 GB    100% GPU     4096       4 minutes from now
```

**Das geladene Fenster war 4096, die Modellgrenze ist 32768.** Der Vorgabewert ist keine
Modelleigenschaft, sondern eine Serverentscheidung nach Grafikspeicher:

```
$ ollama serve --help
      OLLAMA_CONTEXT_LENGTH         Context length to use unless otherwise specified
                                    (default: 4k/32k/256k based on VRAM)
```

Auf der RTX 3070 Ti mit 8 GB wählt der Server die kleinste Stufe.

### 1.3 Die sechs K2-Läufe gegen die Zählung

`usage.prompt_tokens` — bei Ollama der `prompt_eval_count` — aus den archivierten
Rohantworten aller sechs Läufe vom 31.08.2026 (Block `data/z1/k2_trunkiert/`):

| Lauf | `attempt_0` | `attempt_1` | `attempt_2` |
|---|---|---|---|
| `run0`, `run0_w1`, `run0_w2`, `run0_w3`, `run1`, `run2` — **alle sechs zeichengleich** | **2 050** | 1 065 | 2 086 |

Gegen die Zählung aus §1.1: **2 050 von 4 281 Token, 47,9 %.** Es fehlen **2 231 Token**.

**Nachgestellt, nicht erschlossen.** Derselbe Prompt, derselbe Endpunkt
(`/v1/chat/completions`), dasselbe Vorgabefenster, `max_tokens: 1`:

```
usage= {'prompt_tokens': 2050, 'completion_tokens': 1, 'total_tokens': 2051}
```

**2 050 — zeichengleich der Wert der sechs Läufe.** Der Ausfall ist reproduzierbar.

**Zur Zahl 1 065 in `attempt_1`, damit sie nicht falsch gelesen wird:** sie ist *kleiner* als
die von `attempt_0`, obwohl die Konversation dort *länger* ist. Ollama zählt in
`prompt_eval_count` die **neu ausgewerteten** Token; ein im KV-Cache liegendes Präfix wird
nicht mitgezählt. Diese Beobachtung trägt die Konstruktion von P3 (§2).

### 1.4 Die Juni-Läufe — der entscheidende Vergleich

Die drei Juni-Läufe mit Profil `ollama`, Modell `qwen2.5-coder:7b`, `prompt_version v3`
(`data/befunde01-05/runs/`) tragen eine Prompt-Tokenzahl:

| Juni-Lauf | `attempt_0` | `attempt_1` | `attempt_2` |
|---|---|---|---|
| `20260629T091415_r0` | **4 095** | 884 | 1 344 |
| `20260629T092004_r1` | **4 095** | 884 | 1 360 |
| `20260629T092645_r2` | **4 095** | 884 | 1 360 |

Zum Vergleich dieselbe Grösse bei den Nemotron-Läufen, die denselben gerenderten Prompt über
einen fremden Endpunkt schickten — Juni über OpenRouter, heute über DigitalOcean:

| | `attempt_0` |
|---|---|
| Juni, OpenRouter, v3, drei Läufe | **4 455** |
| heute, DigitalOcean, sechs Läufe | **4 455** |

**Die Auskunft, ungeschminkt.** Der Auftrag erwartete eine Juni-Zahl nahe 5 000 gegen heutige
2 086. Gemessen ist **4 095 gegen 2 050**. Die Aussage trägt trotzdem, und zwar doppelt:

- **Das geliefolgte Fenster hat sich verändert, nicht das Modell.** 4 095 gegen 2 050 bei
  bytegleichem Prompt (`cb2fcefd…`, in `z1_d_bericht_formausfall.md` §3.1 als identisch
  nachgewiesen) ist ein Unterschied in der **Lieferung**, nicht in der Antwort.
- **Auch der Juni-Stand war nicht vollständig.** 4 095 ist **4096 − 1**, gegen 4 281
  erwartete Token: auch damals lief der Server auf einem 4096er-Fenster, kürzte aber nach
  einer anderen Regel — er behielt das Ende bis auf ein Token, heute behält er etwa das halbe
  Fenster. Der Verlust betrug im Juni 186 Token (4,3 %), heute 2 231 (52,1 %).

Diese zweite Feststellung ist **eine Folgerung aus zwei Zahlen, kein direkter Zeuge**: die
Juni-Serverversion ist nicht aufgezeichnet (`z1_d_bericht_formausfall.md` §5). Dass 4 095
genau ein Token unter dem Fenster liegt, ist als Zufall allerdings schwer zu haben.

### 1.5 Welches Ende abgeschnitten wird

Zwei Sondierungen mit je exakt 2 050 Token — einmal der **Kopf** des Prompts (erste 9 126
Zeichen), einmal der **Schwanz** (ab Zeichen 9 882) —, gefahren im Vorgabefenster gegen den
trunkierten Vollprompt, jeweils 96 Token Ausgabe bei `temperature 0`:

```
voll@4096       " To do this, remove all the implementation details and only keep the
                  high-level structure and relationships between the modules and classes.
                  Here's an example of how the abstracted architecture might look: …"
nur Schwanz     " To do this, remove all the details and only keep the high-level structure
                  of the system. … bookshop ├── domain │ ├── book …"
nur Kopf        "dataclass\"], \"docstring\": \"A person who wrote a book.\", \"methods\": …"
```

Die Kopf-Variante **schreibt die Faktenliste weiter**, die Schwanz-Variante **antwortet wie
der trunkierte Vollprompt**. **Vorn wird abgeschnitten.** Byte-identisch sind die beiden
Ausgaben nicht, und das passt zum Mechanismus: der Server startet `llama-server` mit
`--context-shift --keep 4`, behält also die ersten vier Token und darauf das Ende —

```
$ ps aux | grep llama-server
/usr/local/lib/ollama/llama-server --model …/blobs/sha256-60e05f21…  -c 16384  -np 1
  … --no-jinja --chat-template chatml --flash-attn auto -b 512 -ub 512
  --context-shift --keep 4
```

— eine reine Schwanz-Sondierung trifft das deshalb nur bis auf diese vier Token. Die
**Richtung** ist damit belegt, die exakte Schnittkante nicht bis aufs Token rekonstruiert;
sie wird auch nicht gebraucht.

### 1.6 VERDIKT

> **Trunkierung: BESTÄTIGT.**
>
> Der gerenderte Prompt zählt **4 281 Token**. Der Ollama-Server lud mit dem Vorgabefenster
> **4096** und liess **2 050** herein — genau den Wert, den alle sechs K2-Läufe vom
> 31.08.2026 melden, heute am selben Endpunkt nachgestellt. Es fehlten **2 231 Token
> (52,1 %)**, abgeschnitten **vorn**, ohne Fehler, ohne Logzeile, mit HTTP 200.
>
> Die Bedingung K2 ist damit **nicht gemessen**, nicht schlecht gemessen.
>
> **Mit derselben Schärfe dazu:** auch die Juni-Läufe waren betroffen (4 095 von 4 281,
> 4,3 % Verlust). Ein Neulauf stellt **nicht den Juni-Zustand** her — er liefert die
> registrierte Bedingung **zum ersten Mal vollständig**.

**Das Gatter des Auftrags ist damit passiert**, und nur deshalb geht es weiter.

---

## 2. Phase 2 — das Amendment, vor dem Lauf

Registriert als **Revision 3** des Z1-Protokolls, datiert, geführt in **beiden** Stellen —
Revisionshistorie im Kopf **und** Amendments-Tabelle §10 — und der Protokoll-SHA in
`z1_p_bericht_freeze.md` §3 nachgezogen, der Wert von Rev. 2 gestrichen sichtbar darüber.

```
$ sha256sum docs/protokolle/z1_protokoll_extraktionsvergleich.md
5fd18ef3f62035c027f5e060fc79574adaedc1e247ea586f7f7d8148eb49d27d
```

```
[OK ] (F) Z1-Protokoll-SHA gegen z1_p_bericht_freeze.md §3
        SHA256 5fd18ef3f62035c027f5e060fc79574adaedc1e247ea586f7f7d8148eb49d27d
        bezeugt in z1_p_bericht_freeze.md §3 als Rev. 3
ERGEBNIS: alle 6 Invarianten erfüllt
```

### 2.1 Befund und Einordnung, ungeschminkt

Die sechs K2-Läufe vom 31.08.2026 haben den registrierten Messeingang **nicht erhalten**:
2 050 von 4 281 Token, vorn abgeschnitten, ohne Fehler und ohne Logzeile (§1). Die Bedingung
K2 ist damit **nicht gemessen**, nicht schlecht gemessen. Die Unterscheidung ist nicht
sprachlich: ein schlecht gemessener Wert wäre ein Datum, ein nicht gelieferter Messeingang
ist keins.

**Ausdrücklich, weil der Verdacht naheliegt und beantwortet gehört:** das Setzen des Fensters
ist **keine Prompt-Revision und kein Ergebnis-Tuning**. Prompt (Blob `6c8e4639…`), Schema
(Blob `5846232d…`), Extractor (`5c0b65a`) und Treiber (`tools/run_z1.py`) sind **bytegleich
unberührt**; verändert ist allein, **wie viel von der registrierten Frage beim Modell
ankommt**. Der Extractor sendet gar keine Ollama-Optionen — das Fenster ist eine Eigenschaft
des Servers, keine des Calls, und steht deshalb bei `temperature` und `seed` unter den
Umgebungsparametern (§3.3).

Die sechs Altläufe bleiben **vollständig im Bestand**, archiviert, gehasht und journalisiert
— als **Beleg des Lieferausfalls**. Gelöscht oder überschrieben ist nichts.

### 2.2 Was registriert wurde

| Stelle | Registrierung |
|---|---|
| **§3.3 (6)** neu | **`OLLAMA_CONTEXT_LENGTH=16384`** am Ollama-Server, vor dem Lauf festgelegt, danach unbewegt |
| **§5.3** Nachtrag | **P3**, die Lieferzusicherung, in drei Teilen (P3a/P3b/P3c) |
| **§5.4** Nachtrag | **Rücksetzung** des Wiederholungsbudgets für **K2**; für K3 bleibt es **erschöpft** |
| **§6.1** Nachtrag | zwei Vorbedingungen **mit Abbruch**: geladenes `CONTEXT` = 16384, kalte Liefersonde im Band |
| **§6.4** Nachtrag | zwei Blöcke: Altblock nach `data/z1/k2_trunkiert/`, Neuläufe in `data/z1/k2/` |

**Die Höhe des Fensters, begründet aus gemessenen Grössen** — nicht gegriffen:

| Grösse | Wert |
|---|---|
| Prompt des ersten Versuchs | 4 281 Token |
| längster archivierter Versuchsprompt (`attempt_2` der Altläufe) | 6 010 Token |
| beobachtete Ausgabelänge je Versuch | ≤ 781 Token |
| Modellgrenze | 32 768 |

**16 384** fasst den längsten bekannten Versuchsprompt mit rund **2,4-fachem** Abstand.
**Nicht 32 768**, weil die Instanz dort auf diesem Rechner aus dem Grafikspeicher rutscht —
gemessen `8%/92% CPU/GPU` bei 6,8 GB gegen `100% GPU` bei 5,5 GB —, das Rechensubstrat der
Bedingung also mitten im Experiment wechselte. **Nicht 8 192**, weil der Abstand dort nur
rund 1,4-fach ist.

**Am Server, nicht über ein Modelfile.** Ein abgeleitetes Modell mit `PARAMETER num_ctx`
trüge einen anderen Namen und einen anderen Digest — eine andere **Modellidentität** mitten
in der Vergleichskette. Gesetzt ist deshalb ein systemd-Drop-in zu `ollama.service`:

```
$ cat /etc/systemd/system/ollama.service.d/context.conf
[Service]
Environment="OLLAMA_CONTEXT_LENGTH=16384"

$ systemctl show ollama -p Environment
Environment="PATH=…" OLLAMA_CONTEXT_LENGTH=16384
```

Modellname `qwen2.5-coder:7b` und Digest `dae161e27b0e` sind unverändert.

### 2.3 P3 — warum sie nötig war und was sie nicht kann

**P1 und P2 sichern die Antwort, P3 sichert die Lieferung.** Die beiden bestehenden
Zusicherungen stellen die Rohantwort gegen das geparste Modell; keine von beiden kann sehen,
ob das Modell die **Frage** vollständig bekommen hat. Genau dieser Fall ist eingetreten — und
P1 und P2 liefen dabei **grün** durch: die Antwort war formal in Ordnung, sie war nur die
Antwort auf einen halben Prompt.

| | Prüfung | Zeitpunkt | Abbruch bei |
|---|---|---|---|
| **P3a** | kalte Liefersonde mit dem registrierten Prompt über denselben Endpunkt, `max_tokens: 1` | vor der Invocation | `prompt_tokens` ausserhalb **4 260 – 4 302** |
| **P3b** | `ollama ps`, Spalte `CONTEXT`, Rohausgabe | vor und nach | ≠ **16384** |
| **P3c** | SHA256 von `attempts/attempt_0/prompt.txt` je archiviertem Lauf | nach dem Lauf | ≠ `cb2fcefd…0ee2d` |

**Die benannte Grenze.** P3 rechnet **nicht** je Versuch auf `prompt_tokens`, und das ist
eine Entscheidung, keine Nachlässigkeit: Ollama meldet dort den `prompt_eval_count`, also die
**neu ausgewerteten** Token; ein zwischengespeichertes Präfix senkt die Zahl **zu Recht**
(gemessen: `attempt_1` meldet 1 065 nach 2 050, auf der längeren Konversation; im Juni 884
nach 4 095). Eine Untergrenze je Versuch erzeugte Fehlabbrüche auf Cache-Treffern. P3 sitzt
deshalb auf der **kalten Sonde** und dem **Fenster**: ist das Fenster 16 384 und der längste
Versuchsprompt 6 010 Token, kann nicht mehr gekürzt werden — die Sonde belegt es empirisch,
der Fensterzeuge strukturell. Die Werte je Versuch werden weiter aufgezeichnet, tragen aber
keine Zusicherung.

**Ausgeführt in `tools/check_z1_delivery.py`** — ausschliesslich lesend, ohne
Extractor-Aufruf. **`tools/run_z1.py` ist bytegleich unverändert**; P3 greift wie P1 und P2
an der Artefaktgrenze.

### 2.4 Wiederholungsbudget

Zurückgesetzt für **K2**: die drei Wiederholungen vom 31.08. sind auf einer Bedingung
verbraucht worden, die **nicht zustande gekommen ist**. Die sechs Altläufe zählen nicht
gegen das neue Budget und bleiben im Bestand.

Für **K3 bleibt das Budget erschöpft.** K3 hat den vollständigen Prompt erhalten — der
Endpunkt meldet in allen sechs Läufen `prompt_tokens: 4455` im ersten Versuch und über die
Versuche **steigende** Werte (bis 5 883), dieselbe Zahl wie OpenRouter im Juni für denselben
Prompt. Sein Ausfall ist Modellverhalten und keine Lieferstörung; über K3 wird **getrennt**
entschieden. **An der Bedingung K3 ist in diesem Auftrag nichts geändert, nichts neu
gefahren, nichts nachgebessert.**

Damit die Rücksetzung kein Muster wird, ist im Protokoll die Regel mitregistriert: ein
Budget darf **nur** bei gefallener Lieferzusicherung zurückgesetzt werden, **nie**, weil ein
Ergebnis missfällt. Der Unterschied ist prüfbar — im ersten Fall ist der **Messeingang** ein
anderer als der registrierte, im zweiten die **Antwort** eine andere als die erhoffte.

---

## 3. Phase 3 — die Läufe unter dem registrierten Fenster

### 3.1 Vor dem Lauf: Fenster und Liefersonde

```
$ python3 tools/check_z1_delivery.py --pre
=== P3 vor der Invocation (Protokoll §5.3, Rev. 3)
  (P3a) Liefersonde · Referenzprompt cb2fcefddbbb… (data/z1/k2_trunkiert/run0/extractor/attempts/attempt_0/prompt.txt)
        Instanz entladen (`ollama stop`) -- die Sonde läuft kalt, damit kein Cache-Präfix die Zahl senkt
        usage.prompt_tokens = 4281 · Referenz 4281 · zulässig 4260–4302
  (P3b) Fensterzeuge nach der Sonde -- `ollama ps`, Rohausgabe:
        NAME                ID              SIZE      PROCESSOR    CONTEXT    UNTIL
        qwen2.5-coder:7b    dae161e27b0e    5.5 GB    100% GPU     16384      4 minutes from now
        CONTEXT = 16384 · registriert 16384

P3 ERFÜLLT
```

**4 281 gegen 4 281, über denselben Endpunkt, der am Vormittag 2 050 lieferte.** Das
geladene Fenster liest **16384**, zeichengleich dem registrierten Wert; kein Abbruch.

### 3.2 Vorbedingungen des Treibers

```
$ PYTHONPATH=…/ma-llm-arch-extractor/src python tools/run_z1.py --condition k2
=== Bedingung K2 · qwen2.5-coder:7b · Profil ollama
  Vorbedingungen OK · HEAD 5c0b65a · Blobs 28 von 28 gleich · Schema a83a84af… ·
    python 3.12.3 pydantic 2.13.5 openai 3.6.0
  → -m llm_arch.cli extract fixtures/rich_repo --provider ollama --model qwen2.5-coder:7b --runs 3
```

Die drei registrierten Laufzeitversionen (§3.3 (4)) treffen die im Protokoll registrierten
zeichengleich; der Schema-Hash ist in der Laufumgebung nachgerechnet und trifft
`a83a84af…12ec0`.

### 3.3 Die Läufe — Gültigkeit, Zähler, Provenienz

**Erstinvocation mit `--runs 3`, dann drei Wiederholungen nach §5.4** (jede als
Einzelinvocation mit `--runs 1`, jede im Journal als Wiederholung geführt):

| Slot | gültig | `valid_raw` | `valid_final` | `attempts_used` | P1 | P2 | `module_count` | `component_count` | `prompt_tokens` | `completion_tokens` | `latency_ms` (innen) | ext. Wanduhr Lauf (abgeleitet) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `run0` | nein | `false` | **`false`** | 3 | OK | OK | 11 | 4 | 6685 | 776 | 9 166 ms | 29,5 s |
| `run1` | nein | `false` | **`false`** | 3 | OK | OK | 11 | 4 | 6685 | 776 | 9 351 ms | 27,5 s |
| `run2` | nein | `false` | **`false`** | 3 | OK | OK | 11 | 4 | 6685 | 776 | 9 332 ms | 27,5 s |
| `run0_w1` | nein | `false` | **`false`** | 3 | OK | OK | 11 | 4 | 6685 | 776 | 9 449 ms | 28,1 s |
| `run0_w2` | nein | `false` | **`false`** | 3 | OK | OK | 11 | 4 | 6685 | 776 | 9 427 ms | 28,0 s |
| `run0_w3` | nein | `false` | **`false`** | 3 | OK | OK | 11 | 4 | 6685 | 776 | 9 372 ms | 27,9 s |

`prompt_tokens` in dieser Tabelle ist der Wert des **letzten** Versuchs, wie ihn `meta.json`
führt. Über die drei Versuche steht in jedem der sechs Läufe:

| | `attempt_0` | `attempt_1` | `attempt_2` |
|---|---|---|---|
| gemeldete `prompt_tokens` | **4 281** | 5 483 | 6 685 |

**Das ist die Lieferung, die der Auftrag herstellen sollte:** der erste Versuch meldet
zeichengleich die erwartete Tokenisierung, und die Zahl **steigt** mit der wachsenden
Retry-Konversation, statt an einer Fenstergrenze zu kleben.

**Externe Wanduhrzeit je Invocation** (monotone Uhr, der nach §6.3 verlangte Wert):
**85,4 s** für die Erstinvocation mit `--runs 3`; **28,8 s · 28,7 s · 28,7 s** für die drei
Wiederholungen. Die Laufwerte der Tabelle sind aus den Fortschrittszeilen des Kindprozesses
**abgeleitet** und im Manifest als Ableitung gekennzeichnet; `latency_ms` ist der
**Innenwert** aus `meta.json`.

**Provenienz, je Lauf im Manifest** — für alle sechs zeichengleich: `provider` `ollama`,
`base_url` `http://localhost:11434/v1/` (Client-Form mit Schrägstrich, §3.3 (2)), `model` und
`model_version` `qwen2.5-coder:7b`, `prompt_version` `v3`, `temperature` `0.0`, `repo_path`
`fixtures/rich_repo`, `repo_commit` `5c0b65a82cc3d8af47c022d779ff63d8a20a9e08`, `seed` 0 als
Umgebungsparameter. Zeitstempel 17:56:46 bis 17:58:58 UTC.

**Kein Transportfehler, kein Timeout, kein Abbruch der Anhalteregel.** Alle sechs Läufe
endeten regulär und sind vollständig archiviert.

### 3.4 Abbruchgrund, wie er im Artefakt steht

Alle sechs Läufe sind nach **§5.2** abgewiesen — `valid_final == false` nach allen drei
Versuchen. Der Grund im Laufmanifest lautet je Lauf:

```
"gruende": ["valid_final == false nach allen Versuchen (§5.2)"]
```

`meta.json` führt je Lauf **26 `validation_errors`**, alle aus derselben Klasse
`relation:`, erste Zeile:

```
relation: from 'bookshop.api.catalog_routes' references unknown component
```

**P1 und P2 stehen bei allen sechs Läufen und allen drei Versuchen auf `OK`**; roh und
geparst stimmen in Komponenten und Relationen überein (5 und 13 im entscheidenden Versuch).
Der Abbruch kommt aus `validate_arch`, nicht aus der Parse-Grenze.

> **Hier endet dieser Bericht auftragsgemäss.** Warum die Läufe an dieser Stelle scheitern,
> ob die Fehlerklasse eine andere ist als am Vormittag, was daraus für E10 oder für die
> Nachbesserungsregel folgt: **nicht Gegenstand.** Kein Vergleich, keine Kennzahl, keine
> Deutung — das ist **Z1-A**.

### 3.5 Zustand der Bedingung

```
  Bedingung K2: NICHT ERHOBEN -- 3 Wiederholungen erschöpft, 0 von 3 Läufen gültig.
  Kein Nullwert, keine leere Zeile (§5.4).
```

**Die Bedingung K2 steht damit erneut als NICHT ERHOBEN** — diesmal jedoch auf einem
gelieferten Messeingang. Das zurückgesetzte Budget ist mit diesen drei Wiederholungen
**verbraucht**; eine weitere Rücksetzung ist durch §5.4 (Nachtrag Rev. 3) nur bei einem
neuen Lieferausfall gedeckt, und ein solcher liegt nicht vor.

### 3.6 Nach dem Lauf: P3b und P3c

```
$ python3 tools/check_z1_delivery.py --post data/z1/k2
  (P3b) Fensterzeuge nach dem Lauf -- `ollama ps`, Rohausgabe:
        qwen2.5-coder:7b    dae161e27b0e    5.5 GB    100% GPU     16384      4 minutes from now
        CONTEXT = 16384 · registriert 16384
  (P3c) Bytezeuge über 6 Läufe in data/z1/k2:
        OK  run0  cb2fcefddbbb1f2e…      OK  run0_w1  cb2fcefddbbb1f2e…
        OK  run1  cb2fcefddbbb1f2e…      OK  run0_w2  cb2fcefddbbb1f2e…
        OK  run2  cb2fcefddbbb1f2e…      OK  run0_w3  cb2fcefddbbb1f2e…
P3 ERFÜLLT
```

Das Fenster stand vor **und** nach der Invocation auf 16384; der gesendete Erstprompt trägt
in allen sechs Läufen den registrierten SHA256.

### 3.7 Archiv

| Block | Inhalt | Fenster | `SHA256SUMS` |
|---|---|---|---|
| `data/z1/k2_trunkiert/` | die sechs Altläufe, **unverändert umbenannt** | 4096, geliefert 2 050 von 4 281 | 85 Dateien, `sha256sum -c` Exit 0 **auch nach der Umbenennung** |
| `data/z1/k2/` | die sechs Neuläufe | **16384**, vollständig geliefert | 85 Dateien, `sha256sum -c` Exit 0 |
| `data/z1/k3/` | **unberührt** | — | unverändert |

Der Altblock ist byte-identisch; sein mitgewandertes `SHA256SUMS` führt relative Pfade und
prüft im neuen Verzeichnis durch. Verweise auf `data/z1/k2/…` in `z1_r_bericht_laeufe.md`
und `z1_d_bericht_formausfall.md` meinen den **Altblock**, also `k2_trunkiert/`.

---

## 4. Abschlusshygiene

| Prüfung | Ergebnis |
|---|---|
| `python3 tools/check_doc_invariants.py` vor dem Auftrag | **Exit 0**, sechs Invarianten |
| … nach dem Amendment-Commit | **Exit 0**, (F) auf Rev. 3 |
| … nach dem letzten Commit | **Exit 0**, sechs Invarianten |
| SHA256 des Z1-Protokolls | `9e02556139bd…` (Rev. 2) → **`5fd18ef3f620…`** (Rev. 3), in `z1_p_bericht_freeze.md` §3 bezeugt |
| `sha256sum -c` in `data/z1/k2` | Exit 0, 85 von 85 |
| `sha256sum -c` in `data/z1/k2_trunkiert` | Exit 0, 85 von 85 |
| `git status --porcelain`, alle fünf Bäume | leer |
| `ma-llm-arch-extractor` `HEAD` | unverändert `5c0b65a`, Arbeitsbaum leer |

**Was dieser Auftrag nicht getan hat:** keine Änderung am **Prompt**, am **Schema**, an
**`metrics.py`**, am **Extractor** oder an **`tools/run_z1.py`** — alle fünf sind bytegleich.
Keine Änderung an **K3**, kein K3-Lauf, keine Nachbesserung dort. Keine Kennzahl gerechnet,
kein Wert gegen §8 gestellt, kein Vergleich zwischen Läufen oder Bedingungen, keine Deutung
des Ausfalls. **Kein Push.**

**Geändert ausserhalb der Repos:** ein systemd-Drop-in
`/etc/systemd/system/ollama.service.d/context.conf` mit
`OLLAMA_CONTEXT_LENGTH=16384` und ein Neustart von `ollama.service`. Das ist
Maschinenzustand, kein Repo-Inhalt, und deshalb im Protokoll §3.3 (6) als
Umgebungsparameter registriert — sonst wäre er nirgends bezeugt.

**Commits** (in `masterarbeit`, **kein Push**, keine Trailer, pfadweise gestaged):

| Commit | Message |
|---|---|
| `e9c83a0` | `docs: amend the Z1 protocol on the context window and delivery assurance P3` |
| `a0c7e17` | `data: set the truncated K2 block aside as k2_trunkiert` |
| `da59ba1` | `feat: add the P3 delivery checker for Z1 condition K2` |
| *(dieser Auftrag)* | `data: archive the K2 runs under the registered context window` |
| *(dieser Auftrag)* | `docs: report the Z1-T context window task` |
