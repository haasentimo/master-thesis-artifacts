# Fixtures der Z1-Parse-Zusicherung

Drei Laufverzeichnisse in der Form, die `run_logger.py` schreibt (`meta.json`,
`arch_model.json`, `attempts/attempt_<n>/`). Sie sind **keine Messung** und stehen unter
keinem Protokollparagraphen; sie existieren nur, damit die Zusicherungen aus
`tools/run_z1.py` **gezeigt** anschlagen und nicht nur behauptet werden.

| Verzeichnis | zeigt | Erwartetes Verhalten |
|---|---|---|
| `p1_fremdschluessel/` | den **gemessenen** Anlass: die Antwort trägt ihre Kanten unter `dependencies` statt `relations` | **P1 FEHL**, P2 OK |
| `p2_verlorene_relation/` | eine Relation geht zwischen Antwort und abgelegtem Modell verloren | P1 OK, **P2 FEHL** |
| `fehlendes_valid_final/` | `meta.json` ohne das Feld `valid_final` | **harter Abbruch** (Instrumentenklasse) |

## `p1_fremdschluessel` — warum P2 hier grün bleibt

Das ist der Fall aus dem Testcall vom 31.08.2026
(`z1_p_bericht_endpunktfrage.md` §3.3, Prüfung C: „components: 3 | relations: 0 ·
Relationen des Modells gehen verloren: 2 Kanten im Dokument → 0 im ArchModel").
`ArchModel.model_validate_json()` nahm die Antwort **ohne Fehler** an: das Schema erlaubt
Fremdschlüssel, pydantic verwirft sie still, und `relations` hat einen Default.

**P2 sieht davon nichts** — roh `relations` 0, geparst `relations` 0, kein Unterschied.
Erst P1 sieht den Schlüssel `dependencies`, der in keiner Feldmenge von `ArchModel`,
`Component` oder `Relation` vorkommt. Genau deshalb stehen **beide** Zusicherungen
nebeneinander; eine allein liesse diesen Lauf durch.

## `p2_verlorene_relation` — ein konstruiertes Paar, offen benannt

Rohantwort und `arch_model.json` sind hier **von Hand** auseinandergesetzt: die Antwort
trägt zwei Relationen, das abgelegte Modell eine. Ein Weg, auf dem pydantic einen
Listeneintrag **still** verliert, ohne zugleich einen Fremdschlüssel zu tragen, ist im
Schema nicht vorhanden — die Fixture bildet deshalb die **Fehlerklasse** ab (Zähler der
Antwort ≠ Zähler des Artefakts), nicht einen beobachteten Mechanismus. Das ist der Zweck:
P2 ist die Gegeninstanz für den Fall, dass ein solcher Weg entsteht.

Der Lauf fällt dabei an **zwei** Stellen auf: roh gegen geparst, und `arch_model.json`
gegen den Re-Parse derselben Rohantwort. Die zweite ist die kostenlose Zusatzprobe, dass
das Archiv zur Antwort passt.

## `fehlendes_valid_final` — Abbruch, nicht `false`

`bool(None)` ist in Python `False`; eine Auswertung, die `m.get("valid_final")` durch
`bool()` schickt — so tut es `compare_runs.py:59` — führte einen Lauf ohne dieses Feld
**stillschweigend als ungültig**. Protokoll §5.2: fehlt das Feld, **bricht** die
Verarbeitung ab; der Lauf wird **nicht** als ungültig gezählt und **nicht** als 0
verrechnet.
