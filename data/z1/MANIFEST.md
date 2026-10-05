# `data/z1/` — Archivwurzel der Z1-Läufe

**Lebendes Dokument.** Es wird fortgeschrieben und trägt selbst keinen Messwert; gehasht
sind die Bedingungsblöcke, nicht diese Datei. Registriert als Archivwurzel in
`z1_protokoll_extraktionsvergleich.md` §6.4 — **nicht im Scratchpad**, Präzedenz ist der
C4c-Verlustfall.

## Ablage

```
data/z1/
  MANIFEST.md          ← diese Datei, lebend, ungehasht
  k2/                  ← Bedingung K2, qwen2.5-coder:7b, Profil ollama
    SHA256SUMS         ← hasht ALLES im Block ausser sich selbst
    journal.jsonl      ← append-only, mit dem Blockabschluss fertig und mitgehasht
    run0/ run1/ run2/  ← die drei Läufe der Erstinvocation (run_index 0, 1, 2)
    run0_w<k>/         ← Wiederholungen nach §5.4, nie auf einem bestehenden Pfad
  k2_trunkiert/        ← NEU 31.08.2026 (Z1-T): der Altblock K2, unverändert umbenannt
  k3/                  ← Bedingung K3, nvidia-nemotron-3-super-120b, Profil digitalocean
  auswertung/          ← NEU 01.09.2026 (Z1-A): die Ausgabe von tools/evaluate_z1.py
```

**Nachtrag 31.08.2026 (Auftrag Z1-T) — zwei K2-Blöcke, zwei Lieferregime.** Registriert im
Protokoll §6.4 (Nachtrag Rev. 3). Der bisherige Block `k2/` ist **unverändert** nach
`k2_trunkiert/` umbenannt: dieselben Dateien, dieselben Hashes, `sha256sum -c` im neuen
Verzeichnis Exit 0 (das mitgewanderte `SHA256SUMS` führt relative Pfade). Grund ist der in
Z1-T Phase 1 nachgewiesene **Lieferausfall**: die sechs Läufe dieses Blocks haben **2 050
von 4 281 Token** des gerenderten Prompts erhalten, weil der Ollama-Server mit dem
Vorgabefenster 4096 lud und vorn abschnitt. Der Block bleibt vollständig im Bestand — er ist
der **Beleg** dieses Ausfalls, nicht sein Abfall. Die Neuläufe unter dem registrierten
Fenster `OLLAMA_CONTEXT_LENGTH=16384` (Protokoll §3.3 (6)) belegen ein frisches `k2/`.
Verweise auf `data/z1/k2/…` in `z1_r_bericht_laeufe.md` und `z1_d_bericht_formausfall.md`
meinen den **Altblock**, also `k2_trunkiert/`.

Je Slot:

```
<slot>/extractor/        ← das Laufverzeichnis des Extractors, UNVERÄNDERT kopiert:
                           meta.json · arch_model.json · input_facts.json ·
                           output.ilograph.yaml · attempts/attempt_<n>/{prompt.txt,
                           raw_response.json, validation.json}
<slot>/run_manifest.json ← das Laufmanifest von tools/run_z1.py: Vorbedingungen,
                           Provenienz, externe Wanduhrzeit, P1/P2 je Versuch, Verdikt
```

Artefakt des Extractors und Manifest des Treibers liegen **nebeneinander**, nicht
ineinander — damit im Nachhinein nicht zu klären ist, welche Datei von wem stammt.

**`SHA256SUMS` je Bedingungsblock, nicht global.** K3 wird nach K2 erhoben und committet;
ein globales `SHA256SUMS` risse beim K3-Commit den bezeugten K2-Stand auf. Dieselbe Form
wie unter `data/campaign/`. Prüfung: `cd data/z1/<block> && sha256sum -c SHA256SUMS`.

**Nachzugsregel:** jede Änderung unter `data/z1/` zieht `SHA256SUMS` und diese Datei im
**selben Commit** nach (Protokoll §6.4, analog `data/soll/`).

## Bestand

| Block | Läufe archiviert | davon gültig | `SHA256SUMS` | Stand |
|---|---|---|---|---|
| ~~`k2/`~~ → `k2_trunkiert/` | **6** (3 Erstinvocation + 3 Wiederholungen) | **0** | 85 Dateien, `sha256sum -c` Exit 0 — auch nach der Umbenennung | umbenannt 31.08.2026, Auftrag Z1-T Phase 2; Inhalt unverändert seit Z1-R Phase 3a |
| `k3/` | **6** (3 Erstinvocation + 3 Wiederholungen) | **0** | 85 Dateien, `sha256sum -c` Exit 0 | 31.08.2026, Auftrag Z1-R Phase 3b |
| `k2/` | **6** (3 Erstinvocation + 3 Wiederholungen) | **0** | 85 Dateien, `sha256sum -c` Exit 0 | 31.08.2026, Auftrag Z1-T Phase 3 |
| `auswertung/` | — (kein Lauf) | — | 2 Dateien, `sha256sum -c` Exit 0 | 01.09.2026, Auftrag Z1-A |

**Nachtrag 31.08.2026 (Z1-T Phase 3) zum Block `k2/`.** Die sechs Läufe dieses Blocks sind
unter dem registrierten Kontextfenster `OLLAMA_CONTEXT_LENGTH=16384` (Protokoll §3.3 (6))
gefahren und haben den Messeingang **vollständig** erhalten: gemeldete `prompt_tokens`
**4 281 · 5 483 · 6 685** über die drei Versuche, gegen **2 050 · 1 065 · 2 086** im Block
`k2_trunkiert/`. Die Lieferzusicherung **P3** ist vor und nach der Invocation erfüllt
(`tools/check_z1_delivery.py`). Gültig ist gleichwohl **kein** Lauf (`valid_final == false`,
26 `validation_errors` der Klasse `relation:` je Lauf, P1 und P2 durchweg `OK`); die
Bedingung steht erneut als **NICHT ERHOBEN**, das zurückgesetzte Budget ist verbraucht.
**Die Deutung dieses Ausfalls steht hier nicht** — sie ist Z1-A. Einzelheiten:
`docs/repo-kontext/z1_t_bericht_kontextfenster.md`.

**Nachtrag 01.09.2026 (Z1-A) — der Block `auswertung/`.** Er trägt **keinen Lauf**, sondern
die **Ausgabe** von `tools/evaluate_z1.py` (SHA256 im Protokoll §7.2, Nachtrag Rev. 5):
`z1_auswertung.json` maschinenlesbar und `z1_auswertung.md` in der Tabellenform aus §7.1.
Er wird gehasht wie ein Bedingungsblock — ein eigenes `SHA256SUMS`, geprüft mit
`cd data/z1/auswertung && sha256sum -c SHA256SUMS` —, weil er Zahlen trägt, die in Kapitel 5
zitiert werden. **Er ist kein Messeingang:** jede Zahl darin ist aus den drei
Bedingungsblöcken und aus der Fixture erzeugt und dort bezeugt.

Was in ihm steht: **Ansatz 1 gerechnet** (die zehn Kennzahlen aus §4 plus `gold_similarity`,
E1 und E2 zeichengleich getroffen), **Ansatz 2 nicht gerechnet** — je Bedingung Gültigkeit,
Zähler und Ursache nach §5.4 in der Fassung Rev. 4 —, und die
**Kontextfenster-Extrapolation**, ausdrücklich als Extrapolation und nicht als Messung
gekennzeichnet. Die **Deutung** steht auch dort nicht; sie ist Befund 07.

**Alle drei Blöcke sind nach Protokoll §5.4 als NICHT ERHOBEN geführt** — nicht als
Nullwert, nicht als 0, nicht als leere Zeile. Grund in beiden Fällen: `valid_final == false`
in allen sechs Läufen nach je drei Versuchen; die drei zulässigen Wiederholungen sind
erschöpft. **Auch die abgewiesenen Läufe sind vollständig archiviert und gehasht**, mit
Rohantwort und Abbruchgrund — ein Lauf, der nur bei brauchbarem Ergebnis in den Bestand
käme, wäre die Auswahl nach Ergebnis, die §5.4 ausschliesst.

Die zwölf Läufe scheitern an **derselben Stelle** (kein Modul ist einer Komponente
zugeordnet), aber über **zwei verschiedene Mechanismen**, und die Parse-Zusicherungen
trennen sie: K2 **lässt `contained_modules` weg** (P1 grün — kein Fremdschlüssel, das Feld
hat einen Default), K3 **schreibt den Schlüssel als `"contained_modules:"`** mit
angehängtem Doppelpunkt (**P1 FEHL** — pydantic verwirft ihn still). Der zweite Fall ist
genau die Fehlerklasse, gegen die §5.3 vorregistriert wurde.

Die Zahlen je Lauf stehen in `docs/repo-kontext/z1_r_bericht_laeufe.md`; die **Auswertung**
steht dort ausdrücklich nicht — sie ist Z1-A.
