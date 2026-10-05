# data/campaign/

Rohbestand der Konformitätskampagne K1–K5 (Aufträge C10, C10a, C10c, C10d) und des
Ruhezustandsblocks der deterministischen Konfigurationen (C6b-1). **Das inhaltliche
Manifest ist [`MANIFEST.md`](MANIFEST.md)** — Messstand nach Protokoll §0.1, Blocktabelle,
Aufrufspezifikation, Journalschnappschuss. Diese Datei beschreibt allein die **Ablage**.

> ~~Messlaeufe der Evaluationskampagne, je Kampagne ein eigenes Unterverzeichnis mit
> `MANIFEST.md` und `SHA256SUMS`. Noch leer — wird ab Messbeginn gefuellt.~~
> — **überholt am 28.08.2026 (Auftrag C6c-b).** Das Verzeichnis ist seit dem 27.08.2026
> gefüllt und seit dem 28.08.2026 (C10d) vollständig; die Gliederung ist **nicht** „je
> Kampagne ein Unterverzeichnis", sondern **je Konfiguration ein Block** plus `control/`,
> `manifests/` und `journal.jsonl`. Eine `MANIFEST.md` liegt **nicht** in jedem Block.

## Was hier liegt

| Pfad | Inhalt | Dateien |
|---|---|---|
| `k1/` | K1 — Checker, deterministische Rule-Engine · `k1_<modus>_<repo-sha>.json` / `.jsonl` | 32 + 32 |
| `k2/` | K2 — Checker + Ollama `qwen2.5-coder:7b` · `k2_<repo-sha>.json` / `.jsonl` · dazu `MANIFEST.md` | 32 + 32 |
| `k3/` | K3 — Checker + DO `nvidia-nemotron-3-super-120b` · `k3_<repo-sha>[_r<n>].json` / `.jsonl`, Wiederholungen **neben** dem Erstversuch · dazu `MANIFEST.md` | 61 + 61 |
| `k4/` | K4 — import-linter 2.13 · `k4_<repo-sha>.stdout.txt` / `.stderr.txt`, **Rohtext** | 32 + 32 |
| `k5/` | K5 — PyTestArch 4.0.1 · `k5_<repo-sha>.stdout.txt` / `.stderr.txt`, **Rohtext** | 32 + 32 |
| `control/` | **Ruhezustand** K1/K4/K5 auf der Baseline `0d651041…` (C6b-1, A-14) — eigener Baum mit `k1/`, `k4/`, `k5/`, `manifests/`, eigener `MANIFEST.md`, `SHA256SUMS`, `journal.jsonl` und dem Läuferskript `run_clean_state.py`. Der Ruhezustand von **K2/K3** liegt **nicht** hier, sondern in `data/c3b-k2/` und `data/c3b-k3/` | 12 |
| `manifests/` | **Laufmanifest je Invocation**, `<cfg>[_<modus>]_<repo-sha>[_r<n>].json` — Verdikte, Zähler, Provenienz, **keine Funde**. Seit Protokoll Rev. 39 die **Quelle von T7** | 189 |
| `journal.jsonl` | **append-only**, ein Eintrag je Invocation (`config`, `injection_id`, `attempt`, `verdict`) | 189 Zeilen |
| `MANIFEST.md` | Kampagnenmanifest, fortzuschreiben — Messstand, Blöcke, Ablage, Journal | — |

**Zur Blockgrösse.** K1, K2, K4 und K5 tragen je **32 Invocationen** (eine je Injektion), K3
**61** — 29 Invocationen sind am Ratelimit (HTTP 429) gescheitert und wurden nach Protokoll §7
wiederholt, ohne Änderung am Werkzeug. **Gültig sind in allen fünf Blöcken 32 von 32.**
Einzelheiten in [`k3/MANIFEST.md`](k3/MANIFEST.md); der Vorbehalt T14 (§9) zu den fünf
Zeitfenstern des K3-Blocks gilt bei jeder Auswertung.

## Rohlogs unverändert archiviert (§6 Punkt 4)

**Protokoll §6 Punkt 4 verlangt, die Rohlogs unverändert zu archivieren.** Das ist der Grund,
aus dem die Archivwurzel am 27.08.2026 mit Amendment Rev. 34 vom flüchtigen Scratch-Pfad
hierher, in einen **versionierten** Pfad, gewandert ist — der C4c-Verlustfall (sechzehn
Laufdateien im flüchtigen Arbeitsverzeichnis, nicht abgelegt) zeigt die Folge des Gegenteils.

Konkret heisst „unverändert":

- **K4/K5 liegen als Rohtext**, `stdout` und `stderr` getrennt, **nicht vorgeparst** und ohne
  `stdout_tail`-Kürzung (§6 Nachtrag Rev. 30 (2)). Der Rohtext ist bei **80 Spalten**
  umgebrochen; die Bezeugung gilt für **diese** Zeilenaufteilung, nicht für eine beliebig
  nacherzeugte (Auswertungsspezifikation §1.4). `stderr` ist in **allen 64** Aufrufen **leer
  (0 Bytes)** — beide Werkzeuge schreiben im fehlerfreien Lauf alles auf `stdout`.
  Festgehalten, nicht verändert.
- **Nie überschreiben, nur hinzufügen.** Auch ein ungültiger Lauf bleibt liegen; er wird
  gekennzeichnet, nicht gelöscht. Wiederholungen stehen auf eigenen `_r<n>`-Pfaden **neben**
  dem Erstversuch, nie an seiner Stelle.
- **Nicht reproduzierbar.** LLM-Läufe sind auch mit `temperature=0` und festem `seed` nicht
  bitgleich wiederholbar (Wurzel-README, Abschnitt „Messdaten").
- **Kein Auswertungsergebnis in diesem Verzeichnis.** Metriken, Findingbeurteilung und
  Vergleiche gehören nach C6b; die Eine-Iteration-Regel (§7) und die Amendment-Sperre aus
  §0.1 gelten.

## Hashes — und die sechs Dateien, die bewusst keinen tragen

Jeder Block trägt eine `SHA256SUMS`, aus der **Repowurzel** mit `sha256sum -c` prüfbar; die
Laufmanifeste sind darin **mitbezeugt** (je Block die 32 bzw. 61 Zeilen `manifests/…`).
Zusammen **581 gelistete Pfade**: k1/k2/k4/k5 je 96, k3 183, `control/` 14. Maschinell geprüft
durch `tools/check_doc_invariants.py`, Invariante **(D)**.

**Sechs Dateien dieses Verzeichnisbaums stehen in keinem `SHA256SUMS` und bleiben ungehasht** —
entschieden am 28.08.2026 mit **Protokoll Rev. 39, §0.1 Punkt 7**, das sie zusammen mit
`data/soll/MANIFEST.md` als die **sieben lebenden Dokumente** führt:

| Datei | Warum ungehasht |
|---|---|
| `MANIFEST.md` | fortzuschreibendes Kampagnenmanifest |
| `k2/MANIFEST.md`, `k3/MANIFEST.md` | fortzuschreibende Blockmanifeste |
| `README.md` (diese Datei) | Ablagebeschreibung, trägt keinen Messwert |
| `journal.jsonl` | append-only, wächst planmässig je Invocation |
| `control/journal.jsonl` | ebenso — die Laufmanifeste und Rohartefakte des Kontrollbestands sind sehr wohl gehasht |

**Begründung (Rev. 39).** Ein Hash wäre für sie das **falsche Instrument**: er risse bei
**jeder legitimen** Fortschreibung und erzöge dazu, ihn routinemässig nachzuziehen — ein
Detektor, dessen Anschlagen zur Routine wird, ist keiner mehr. Integrität liefert für sie die
**Commit-Historie**; der **Schnappschuss-Hash** im Manifest bleibt, wo er steht.

**Was die Ausnahme nicht deckt.** Keine der Genannten ist ein **Laufartefakt**, und seit
Rev. 39 ist keine mehr **Quelle** eines T-Wertes: T7 steht auf den gehashten Laufmanifesten in
`manifests/`, während `MANIFEST.md`, `k3/MANIFEST.md` und `journal.jsonl` **Gegenprobe** sind.
Weicht Quelle von Gegenprobe ab, ist das ein **Befund** — er wird berichtet und **nicht** durch
Angleichen aufgelöst. Die Liste steht namentlich als `KNOWN_UNLISTED` im Prüfer; eine **achte**
ungelistete Datei ist dort ein **Fehlschlag**, keine Ausnahme.
