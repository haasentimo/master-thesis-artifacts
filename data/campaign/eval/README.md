# Auswertungsläufe über den Kampagnenbestand — Index

**Masterarbeit Timo Haas · HTWG Konstanz** · Stand: 28. August 2026, Auftrag **C14**

Dieses Verzeichnis führt **jeden** Auswertungslauf über `data/campaign/k1..k5`. Es wird
**nichts gelöscht und nichts nachbearbeitet**: ein überholter Lauf bleibt Byte für Byte
liegen und bleibt gehasht. Das ist die Vorschrift aus Protokoll §0.1 Punkt 6 — eine
Defektbehebung an den Auswertungsinstrumenten verlangt **vollständige Neuauswertung** und
**Ausweis beider Ergebnisse, nebeneinander, nicht ersetzend**.

## Der kanonische Lauf

> **Kanonisch ist genau EIN Lauf, und er heisst `c14_eval_full`.** Solange kein fünfter
> folgt, ist er die Fassung, aus der Kapitel 7 zitiert und die das Dokumentbündel trägt.
> Die drei früheren sind **ÜBERHOLT, ABER GÜLTIG ARCHIVIERT**: sie sind Beleg der
> Reparaturkette, **nicht** Ergebnis. Wer eine Zahl der Arbeit sucht, nimmt `c14`; wer
> prüfen will, wie sie zustande kam, liest die Kette.

## Die vier Läufe

| # | Ausgabe | Auftrag · Datum | Protokoll | `evaluate_campaign.py` | SHA256 der Ausgabe | Status |
|---|---|---|---|---|---|---|
| 1 | `c11_eval_full.json` / `.md` | **C11** · 28.08.2026, 13:16 | Rev. 39 | `5125cd59…0528eed` | `.json` `ad8f0483…56b371ea30`<br>`.md` `3d487484…5a0a0e595af` | **überholt, gültig archiviert** |
| 2 | `c12_eval_full.json` / `.md` | **C11b** · 28.08.2026, 14:52 | Rev. 41 | `20bcdae0…23d306` | `.json` `12751c3e…9d200b09f0c7`<br>`.md` `afe28bc2…44c27e80c921918` | **überholt, gültig archiviert** |
| 3 | `c13_eval_full.json` / `.md` | **C11c** · 28.08.2026, 16:17 | Rev. 43 | `eb206a6f…b520653` | `.json` `873893e7…a85a1c1914977c`<br>`.md` `f8cd9c07…e1e5777f414c8a2` | **überholt, gültig archiviert** |
| 4 | **`c14_eval_full.json` / `.md`** | **C14** · 28.08.2026, 23:49 | **Rev. 45** | **`b66be750…f079a93428`** | `.json` `46ba024d…e20333cc0a71`<br>`.md` `ed59aa95…ad8ed65e2329b` | **KANONISCH** |

`tools/match_k4k5.py` steht seit Lauf 2 unverändert auf
`c16e7c4380034163f3034916193bd96cfc6bb957768fe610cb7018d7799f4ca6` (Lauf 1:
`ad3edcb1ee8537ee758d8212055371957c0493f3d8e218267d182fb9fc060022`);
`tools/check_doc_invariants.py` steht über alle vier Läufe unverändert auf
`6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018`.

**Die vollständigen Hashes stehen in `SHA256SUMS` dieses Verzeichnisses**; `sha256sum -c`
läuft dort durch, und der Prüfer `tools/check_doc_invariants.py` (Invariante D) prüft es
bei jedem schreibenden Auftrag mit.

## Warum jeweils ein weiterer Lauf nötig wurde — je ein Satz

| Lauf | Warum der NÄCHSTE nötig wurde |
|---|---|
| **1 — c11** | Die Diagnose C11a fand neun Defekte an den Instrumenten, darunter gerechnete Werte, die als **leere Zelle** in die Tabelle liefen, und einen Join über Zeichenketten, der vier K5/`CYCLE`-Funde verlor (`c11a_bericht_diagnose.md` §7). |
| **2 — c12** | Die Reparatur R1–R9 wirkte, aber der Lauf druckte **72 T5-Marker ohne Code-Auszeichnung** und zwei Millisekundensummen in **Exponentialschreibweise** — beides in `c11b_bericht_zweiter_lauf.md` §7 ausgewiesen und **nicht** behoben. |
| **3 — c13** | Die mechanische Auszählung in **C11d §A6b** zeigte, dass die Auflösungsregel `<cfg>_*<injection_sha256>.json` für **elf** K3-Injektionen das Artefakt des **ersten** Versuchs las, dessen Laufmanifest `INVALID` (`transport_failure`) trägt — die von Protokoll §7 ausgeschlossene stille Zählung invalider Läufe. Dazu fehlte die von §8 UF3 verlangte **Overlap-Analyse** ganz (§B5). |
| **4 — c14** | *(kein weiterer Lauf beauftragt)* |

## Was den vierten Lauf vom dritten unterscheidet

- **R11** — die Artefaktauswahl je Paar (Konfiguration, Injektion) steht auf
  `postrun.verdict == VALID` des **gehashten Laufmanifests**, bei mehreren gültigen
  Versuchen auf dem **frühesten**; nicht mehr auf dem Dateinamen
  (Auswertungsspezifikation §1.9, Protokoll Rev. 44).
- **R12** — der Lauf bricht mit **Exit 2** ab, wenn ein Artefakt gelesen wird, dessen
  Laufmanifest kein `VALID` trägt.
- **R13** — neue Tabelle **T10**, die von Protokoll §8 UF3 verlangte Overlap-Analyse,
  gebildet aus den **bereits gerechneten** Trefferzellen.
- **R14** — der Vermerk an T5 druckt die Rev.-42-Begründung statt „LÜCKE, benannt und
  nicht gefüllt".

**Gegenüberstellung c13 → c14, gerechnet und nicht behauptet:** von **1952**
Injektionszellen haben sich **35** geändert, **alle** in **K3**, **alle** in genau den
**elf** Injektionen aus C11d §A6b (I05, I06, I07, I09, I11, I13, I16, I20, I21, I22,
I23). **Keine einzige K1-, K2-, K4- oder K5-Zelle hat sich bewegt.** T3, T6 und T7 sind im
JSON zeichengleich. Der Rechenweg steht in `docs/repo-kontext/c14_bericht_vierter_lauf.md`.

## Regeln für dieses Verzeichnis

1. **Kein Lauf wird gelöscht, keine Datei nachbearbeitet.** Ein neuer Lauf tritt
   **daneben**, nie an die Stelle.
2. **Jede Datei hier ist in `SHA256SUMS` gehasht** — auch diese README. Wird sie
   fortgeschrieben, gehört der Hash-Nachzug in **denselben Commit**.
3. **Der kanonische Lauf ist genau einer und steht oben namentlich.** Kommt ein fünfter,
   wandert die Kennzeichnung dorthin und `c14` wird als überholt, aber gültig archiviert
   geführt — mit einem Satz dazu, warum er nötig wurde.
4. **Das Dokumentbündel führt nur den kanonischen Lauf** (`tools/bundle-docs.sh`): zwei
   Fassungen derselben Tabellen sind im Projektwissen nicht auseinanderzuhalten.
