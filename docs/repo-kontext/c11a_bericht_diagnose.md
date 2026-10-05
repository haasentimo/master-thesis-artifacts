# C11a — Diagnose ohne Fix: drei offene Stellen im ersten Auswertungslauf

**Auftrag:** C11a, 28.08.2026. Feststellen, ob eine offene Stelle des ersten
Auswertungslaufs ein **Harness-Defekt** oder ein **Messergebnis** ist. Kein Code, keine
Zahl, kein Instrument, kein Skelett, keine Spezifikation und nichts unter
`data/campaign/eval/` wurde verändert.

**Deutungssperre, abgeschwächt.** Berichtet werden Mechanik und Zahlen. Keine Bewertung,
ob ein Ergebnis gut, schlecht oder überraschend ist; kein Vergleich zwischen
Konfigurationen; keine Empfehlung zu Prompt, Schema, Regeldatei, Manifest oder
Metrikdefinition. Jeder Blick in ein Kampagnenartefakt ist in §6 protokolliert.

---

## 0 Vorbedingungen

```
$ for d in masterarbeit tritongraph ma-conformance-testrepo tritongraph-measure; do
      git -C $d status --porcelain; done
(alle vier leer)

$ git -C masterarbeit rev-parse HEAD
a287045c72edab92763671f7222d65bfc8777fe3
$ git -C masterarbeit log --oneline -1
a287045 docs: report the first evaluation run

$ ps aux | grep -Ei "evaluate_campaign|run_campaign|tritongraph|checker" | grep -v grep
(keine)

$ python3 tools/check_doc_invariants.py
ERGEBNIS: alle 5 Invarianten erfüllt          → Exit 0
```

**Der archivierte erste Lauf ist unverändert** — gezeigt, nicht angenommen:

```
$ sha256sum -c data/campaign/eval/SHA256SUMS
data/campaign/eval/c11_eval_full.json: OK
data/campaign/eval/c11_eval_full.md: OK          → rc=0

$ cat data/campaign/eval/SHA256SUMS
ad8f0483ffd2c261d8e33a21c425c5f6a492dedae0cc99c4e135dc56b371ea30  data/campaign/eval/c11_eval_full.json
3d4874842a5baf92d455c1140b4874d396550fe87c50714d537a15a0a0e595af  data/campaign/eval/c11_eval_full.md
```

Beide SHA256 sind zeichengleich mit den in `c11_bericht_auswertungslauf.md` §4
berichteten Werten.

---

## 1 Frage 1 — K5 bei CYCLE, und T9 Fall 7

### 1.1 (a) Der archivierte K5-Rohtext der vier CYCLE-Injektionen

Zuordnung aus `data/soll/injection_manifest.json`: I13 `3be646fe…`, I14 `a9d64451…`,
I15 `616cb029…`, I16 `43f9fa5e…`. Alle vier Dateien sind 40 Zeilen lang.

**I13 — `data/campaign/k5/k5_3be646fed3bdb2449b153f912d42fbb63b719776.stdout.txt`**

```
.........F..............                                                 [100%]
=================================== FAILURES ===================================
______ test_component_imports_only_whitelisted_modules[identity_mappers] _______
…
E           AssertionError: "depot.identity.mappers.customer_mapper" imports "depot.identity.api.routes".
…
=========================== short test summary info ============================
FAILED ../masterarbeit/data/soll/test_architecture.py::test_component_imports_only_whitelisted_modules[identity_mappers]
1 failed, 23 passed in 0.17s
```

**I14 — `k5_a9d644515812b98877af4e63e0f9a3f119ee7e88.stdout.txt`**

```
_______ test_component_imports_only_whitelisted_modules[orders_mappers] ________
E           AssertionError: "depot.orders.mappers.order_mapper" imports "depot.orders.api.routes".
FAILED …::test_component_imports_only_whitelisted_modules[orders_mappers]
1 failed, 23 passed in 0.16s
```

**I15 — `k5_616cb02982e634670c4dbaa84d5efbf4df63c61a.stdout.txt`**

```
_______ test_component_imports_only_whitelisted_modules[billing_mappers] _______
E           AssertionError: "depot.billing.mappers.invoice_mapper" imports "depot.billing.api.routes".
FAILED …::test_component_imports_only_whitelisted_modules[billing_mappers]
1 failed, 23 passed in 0.17s
```

**I16 — `k5_43f9fa5ec1b6fbf4aaae26296a41b752c2e3f9cf.stdout.txt`**

```
___ test_component_imports_only_whitelisted_modules[orders_services_pricing] ___
E           AssertionError: "depot.orders.services.pricing.engine" imports "depot.orders.services".
FAILED …::test_component_imports_only_whitelisted_modules[orders_services_pricing]
1 failed, 23 passed in 0.16s
```

**Feststellung:** K5 hat in allen vier Läufen eine FAILURES-Sektion, je genau eine
gebrochene Regel, je `1 failed, 23 passed`. Das genannte Modul an erster Stelle ist in
allen vier Fällen **das Trägermodul der Injektion** laut Manifest
(I13 `depot.identity.mappers.customer_mapper`, I14 `depot.orders.mappers.order_mapper`,
I15 `depot.billing.mappers.invoice_mapper`, I16 `depot.orders.services.pricing.engine`).

### 1.2 (b) Der Parser hat die Zeilen erfasst

`python3 tools/match_k4k5.py --tool K5 --injection I13|I14|I15|I16 <datei>` — je Datei
**genau ein** Finding, `uncovered_nonempty_lines: 0`. Fundliste, verkürzt auf die
entscheidenden Felder:

| Datei | `scenario_l2` | `form` | `source_module` | `target_module` | `classification` | `strict_eligible` | `localized` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I13 | `CYCLE_SIBLING` | `allowlist_violation` | `depot.identity.mappers.customer_mapper` | `depot.identity.api.routes` | `begleitmeldung` | `false` | `treffer (richtige Stelle, falsche Kategorie)` |
| I14 | `CYCLE_SIBLING` | `allowlist_violation` | `depot.orders.mappers.order_mapper` | `depot.orders.api.routes` | `begleitmeldung` | `false` | `treffer (richtige Stelle, falsche Kategorie)` |
| I15 | `CYCLE_SIBLING` | `allowlist_violation` | `depot.billing.mappers.invoice_mapper` | `depot.billing.api.routes` | `begleitmeldung` | `false` | `treffer (richtige Stelle, falsche Kategorie)` |
| I16 | `CYCLE_PARENT_CHILD` | `allowlist_violation` | `depot.orders.services.pricing.engine` | `depot.orders.services` | `begleitmeldung` | `false` | `treffer (richtige Stelle, falsche Kategorie)` |

Die `cell_rule` je Datei trägt `"strict": "nie"`, `"localized": "bildbar"` und die Notiz
`footnote 7 — the back edge is reported as a non-listed edge, not as a cycle; strict no
hit, localized hit on the place (T9 case 7)`. Das `reason`-Feld jedes Findings zitiert
Fussnote 7 wörtlich.

**Zuordnung Datei → Injektion ist korrekt:** der Parser löst je Datei das erwartete
Szenario und das Trägermodul der zugehörigen Injektion auf.

### 1.3 (c) Der Harness-Join bucht sie nicht — die Stelle

[`tools/evaluate_campaign.py:917-920`](../../tools/evaluate_campaign.py#L917-L920):

```python
strict_hit = any(f["classification"] == "treffer" and f.get("strict_eligible")
                 for f in result["findings"])
localized_hit = any(f["classification"] == "treffer" and f.get("localized") == "treffer"
                    for f in result["findings"])
```

**Zwei voneinander unabhängige Gatter, von denen keines passiert wird:**

1. `f["classification"] == "treffer"` — der Parser liefert `begleitmeldung`.
2. `f.get("localized") == "treffer"` — der Parser liefert die Zeichenkette
   `treffer (richtige Stelle, falsche Kategorie)`; der Vergleich ist auf Gleichheit,
   nicht auf Präfix oder Teilzeichenkette.

Beide Bedingungen stehen in **einer** `and`-Verknüpfung; `localized_hit` ist damit
`False`, und `localized` wird zu `valued(0)` ([Zeile 927](../../tools/evaluate_campaign.py#L927)).

Es ist **nicht** die Kategoriezuordnung (der Parser trifft `CYCLE_SIBLING` bzw.
`CYCLE_PARENT_CHILD`), **nicht** die `localized`-Bildung im Parser (sie ist gebildet und
benannt), und **nicht** die Zuordnung Datei → Injektion (sie stimmt). Es ist die
**Buchungsregel für Fall 7 im Join**.

Die vier Funde sind nicht verloren: `classification == "begleitmeldung"` führt sie in die
Liste `co` ([Zeile 923](../../tools/evaluate_campaign.py#L923)). Im Archiv des ersten
Laufs stehen sie dort:

```
co_findings (11 Einträge): K1 4 · K4 acyclic_block 3 · K5 allowlist_violation 4
  K5: I13 allowlist_violation · I14 · I15 · I16
specials (70 Einträge): ausschliesslich K2
```

**Zur Vollständigkeit die Verteilung aller K4/K5-Findings** über die 32 Injektionen,
durch den Parser gelaufen:

| Konfiguration | `classification` | `strict_eligible` | `localized` | Anzahl |
| --- | --- | --- | --- | ---: |
| K4 | `begleitmeldung` | `None` | `n. b.` | 3 |
| K4 | `treffer` | `False` | `treffer` | 4 |
| K4 | `treffer` | `True` | `n. b.` | 3 |
| K4 | `treffer` | `True` | `treffer` | 12 |
| K5 | `begleitmeldung` | `False` | `treffer (richtige Stelle, falsche Kategorie)` | **4** |
| K5 | `treffer` | `True` | `treffer` | 16 |

Die vier CYCLE-Funde sind die **einzigen** K5-Findings, deren `localized`-Wert vom
Literal `"treffer"` abweicht.

### 1.4 Der vorregistrierte Wortlaut, gegen den das zu messen ist

`docs/protokolle/c6_auswertungsspezifikation.md:504`, Fall 7:

> In `strict`: kein Treffer (Kategoriesegment weicht ab). In `localized`: **Treffer auf
> der Stelle**, Kategorie „nicht gelistete Kante" statt `CYCLE` → Klasse „richtige
> Stelle, falsche Kategorie" — **ohne neue Regel** gebucht (Präfix-/Kategorielogik
> identisch zu Fall 6). Matrixzelle: „teilweise".

`docs/kapitel/kapitel7_tabellenskelette.md:888`, T9 Fall 7, wortgleich in der Buchungsregel.
Protokoll Rev. 22 (§3 Fussnote 7, B39) führt dieselbe Buchung aus und hält fest, die
Zellen `CYCLE_SIBLING`/K5 und `CYCLE_PARENT_CHILD`/K5 bewegten sich von „nein" auf
„teilweise⁷".

Die Zellen sind **nicht** durch einen Marker vorbelegt: T1 des ersten Laufs zeigt für
K5 `0/3` bzw. `0/1` — ein berechneter Wert, kein ` — ` und kein `n. b.`

### 1.5 (d) VERDIKT — **DEFEKT**

Der Buchungspfad greift nicht. K5 **hat** die Rückkante in allen vier Läufen gemeldet
(§1.1), der Parser **hat** sie erfasst und als `localized`-Treffer benannt (§1.2), und
der Join verwirft sie an zwei Zeichenkettenvergleichen (§1.3). Das Nullergebnis
`0/3` und `0/1` in T1/T2 ist nicht die Messung, sondern deren Verlust im Join.

Die BEFUND-Alternative ist damit ausgeschlossen; die Zusatzfrage zum Schärfenachweis
`c2c_bericht_k5_konfiguration.md` §B5 stellt sich nicht als Widerspruch. Der Vollständigkeit
halber: §B5 hat für `CYCLE_SIBLING` und `CYCLE_PARENT_CHILD` je `1 failed, 23 passed`,
Exit 1 gemessen und die Meldeform als nicht gelistete Kante abgedruckt — der
Kampagnenrohtext aus §1.1 zeigt **dieselbe** Form, dieselbe Testfunktion und dieselbe
Zusammenfassungszeile. Kampagne und Schärfenachweis stimmen überein.

**Zur Relevanznotiz des Auftrags:** die vier CYCLE-Injektionen sind genau die Stellen, an
denen K5 im Join eine Positivpaarung hätte. Die übrigen 16 K5-Findings tragen
`classification == "treffer"` und passieren beide Gatter.

---

## 2 Frage 2 — T9 Fall 6 bei K3, und die leeren Häufigkeiten in Fall 7

### 2.1 Rechnet die Harness Fall 6 für K3?

**Ja, mit demselben Rechenweg wie für K2.**
[`tools/evaluate_campaign.py:1666-1670`](../../tools/evaluate_campaign.py#L1666-L1670):

```python
for config in ("K2", "K3"):
    hits = [s for s in specials if s["config"] == config and s["injection"] in cyc]
    w(f"| 6 | `CYCLE`: {config} meldet `FORBIDDEN_RELATION` am **richtigen Modul** | {config} | "
      f"{', '.join(sorted(cyc))} | {len(hits) or ''} | …")
```

Die Schleife läuft über beide Konfigurationen; es gibt keine K2-Sonderverdrahtung. Die
Quelle `specials` wird für K1/K2/K3 in
[`evaluate_llm_injection`](../../tools/evaluate_campaign.py#L893-L899) gefüllt: ein Record
am Trägermodul, dessen Tripel `(component, module, category)` von der Erwartung abweicht.

### 2.2 Der Wert für K3 ist 0 — und er ist echt

Im Archiv: `specials` hat 70 Einträge, **alle mit `config == "K2"`**. Für K3 auf den
CYCLE-Injektionen: 0.

Gegen die Rohartefakte geprüft, nicht angenommen (Zugriff in §6 protokolliert): über alle
32 K3-Injektionen und alle Repetitionen liegen **78 LLM-Records**, davon **78 am
Trägermodul**, und alle 78 treffen das erwartete Tripel exakt — es bleibt **kein**
Record für den `special`-Eimer übrig.

```
{'llm_records': 78, 'derived': 16, 'am_traegermodul': 78, 'treffer_localized': 78, 'special_kandidat': 0}
```

**Der Wert 0 ist ein Messergebnis.** Kein Defekt im Rechenweg.

### 2.3 Warum er als leere Zelle erscheint

`{len(hits) or ''}` — in Python ist `0 or ''` die leere Zeichenkette. Eine berechnete
**0** wird damit als **leere Zelle** gedruckt. Die Markerlegende der Ausgabe führt
*(leer)* aber als „von diesem Lauf nicht eingesetzt". Eine gerechnete Null und eine nicht
eingesetzte Zelle sind in T9 folglich **nicht unterscheidbar**.

### 2.4 Dieselbe Frage für Fall 7

[`Zeile 1671-1674`](../../tools/evaluate_campaign.py#L1671-L1674):

```python
k5 = [s for s in specials if s["config"] == "K5" and s["injection"] in cyc]
w(f"| 7 | … | {len(k5) or ''} | …")
```

Fall 7 zählt aus **`specials`**. Für K4/K5 wird `specials` in
[`evaluate_k4k5_injection`](../../tools/evaluate_campaign.py#L924-L926) ausschliesslich
aus `classification == "sonstiger_fund"` gefüllt. Die vier K5-CYCLE-Funde tragen
`begleitmeldung` und liegen deshalb in `co_findings` (§1.3). `len(k5)` ist 0, die Zelle
wird leer.

**Fall 7 zählt aus dem falschen Eimer** — dieselbe Wurzel wie §1.3, eine Ebene später:
der Parser klassifiziert die vorregistrierte Sonderklasse als `begleitmeldung`, Join und
T9-Zähler erwarten sie in `specials`.

**Verdikt Fall 6/K3: BEFUND** (Wert 0, echt gerechnet) — **mit DEFEKT in der Darstellung**
(0 wird als leer gedruckt).
**Verdikt Fall 7: DEFEKT** (falscher Eimer; der Wert wäre 4, siehe `co_findings`).

---

## 3 Frage 3 — kein-EN und die Medianzählung

### 3.1 (a) Wie ist `Kampagne` gebildet?

**Median über die Repetitionen einer je Lauf gebildeten Zählgrösse.**
[`evaluate_campaign.py:871-872`](../../tools/evaluate_campaign.py#L871-L872) im
Lauf-über-`doc["runs"]`:

```python
counts.append(len([f for f in mine
                   if f.get("module") == module and f.get("category") == entry["category_l1"]]))
```

und [`Zeile 1062-1063`](../../tools/evaluate_campaign.py#L1062-L1063):

```python
camp_med = median(counts)
entry_cfg["campaign"] = valued(f"{camp_med:g}")
```

Filter der Zählgrösse: **Trägermodul UND `category_l1`**. Nicht der `match_key`.

### 3.2 (b) Wie ist `strict` gebildet?

**Existenzquantor über alle Repetitionen — „mindestens ein Lauf", binär.**
[`Zeile 880-884`](../../tools/evaluate_campaign.py#L880-L884) setzt `strict_hit = True`,
sobald **ein** Record in **einem** Lauf den erwarteten `match_key` trägt;
[`Zeile 905`](../../tools/evaluate_campaign.py#L905) macht daraus `valued(1 if strict_hit else 0)`.
Filter: **`match_key`**, ein vierteiliger Schlüssel.

### 3.3 (c) Wie ist kein-EN gebildet?

[`Zeile 1070-1072`](../../tools/evaluate_campaign.py#L1070-L1072):

```python
hit = strict_cell.value == 1
entry_cfg["kein_en"] = valued(
    "ja" if (hit and camp_med <= rest_med) else ("nein" if hit else ""))
```

Drei Zustände: `ja` (strict-Treffer, der die Ruhezustandsrate nicht übersteigt), `nein`
(strict-Treffer, der sie übersteigt), **leer** (kein strict-Treffer). Die leere Zelle ist
hier ein **berechneter dritter Zustand**, nicht eine nicht eingesetzte Zelle.

### 3.4 (d) Rohwerte je Repetition, K3, für I06, I20, I21, I23

Aus den Kampagnenartefakten gelesen (Zugriff in §6 protokolliert):

| ID | Trägermodul | `category_l1` | Lauf 0 | Lauf 1 | Lauf 2 | `counts` | Median = `Kampagne` | `strict` |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| I06 | `depot.billing.api.routes` | `FORBIDDEN_RELATION` | 0 Records | 0 Records | **1 Record, `match_key` trifft** | `[0,0,1]` | **0** | **1** |
| I20 | `depot.billing.services.ledger_service` | `ABSENCE_REQUIRED` | **1 Record, `match_key` trifft** | 0 Records | 0 Records | `[1,0,0]` | **0** | **1** |
| I21 | `depot.identity.models.customer_models` | `FORBIDDEN_SIGNATURE_TYPE` | 0 Records | 0 Records | **1 Record, `match_key` trifft** | `[0,0,1]` | **0** | **1** |
| I23 | `depot.orders.models.order_line_models` | `FORBIDDEN_SIGNATURE_TYPE` | 0 Records | 0 Records | 0 Records | `[0,0,0]` | **0** | **0** |

Die getroffenen `match_key` wörtlich:

```
I06  FORBIDDEN_RELATION|billing_api|depot.billing.api.routes|billing_api->billing_repository
I20  ABSENCE_REQUIRED|billing_services|depot.billing.services.ledger_service|depot.core.ports.Clock
I21  FORBIDDEN_SIGNATURE_TYPE|identity_models|depot.identity.models.customer_models|sqlalchemy.orm.Session
I23  (kein Record in keinem der drei Läufe)
```

In allen vier Fällen ist `category` des Records gleich `category_l1` und gleich
`expected_category(LLM)`; die Zählgrösse und der `match_key` greifen also auf **dieselben**
Records zu. Der Unterschied liegt allein in der Aggregation.

**I23** trägt `strict` = 0, weil kein Lauf gemeldet hat; kein-EN ist deshalb der dritte
Zustand **leer**, nicht `ja`. (Der Auftragstext führt I23 unter den kein-EN-Fällen; im
Archiv steht dort die leere Zelle. Die vier K3-Zeilen mit kein-EN = `ja` sind
**I06, I20, I21 und I31**.)

### 3.5 (e) FESTSTELLUNG zur Aggregationsstufe

**`Kampagne` und `strict` sind nicht auf derselben Aggregationsstufe gebildet.**

| Grösse | Filter | Aggregation über die drei Repetitionen |
| --- | --- | --- |
| `Kampagne` | Trägermodul **und** `category_l1` | **Median** der Zählwerte je Lauf |
| `strict` | erwarteter **`match_key`** | **Existenz** („mindestens ein Lauf"), binär |

Bei `[0,0,1]` liefert der Median 0 und der Existenzquantor 1. Genau diese Konstellation
tragen I06, I20 und I21.

**kein-EN ist aus diesen beiden verschieden aggregierten Grössen gebildet:** die
Bedingung `hit and camp_med <= rest_med` verknüpft einen Existenzwert (`strict` = 1) mit
einem Median (`Kampagne` = 0) und einem zweiten Median (`Ruhe` = 0). Das wird hier
**benannt, nicht gelöst.**

### 3.6 Deskriptiv: die kein-EN-Verteilung und der Auslöser

Aus dem Archiv, je 32 Zeilen:

| Konfiguration | kein-EN = `ja` | `nein` | leer |
| --- | ---: | ---: | ---: |
| K2 | **20** | 5 | 7 |
| K3 | **4** | 23 | 5 |

(Der Auftragstext nennt für K2 21 Zeilen; im Archiv stehen 20.)

**Die K2-Fälle.** Alle 20 tragen `Ruhe` ≥ 1 und `Kampagne` ≥ 1, mit `Kampagne ≤ Ruhe`.
Ausschnitt: I01–I05 `Ruhe`=1/`Kampagne`=1/Δ=0 · I06, I07 2/2/0 · I08 3/2/−1 · I09, I11
3/3/0 · I22 5/1/−4 · I23 4/1/−3. **Auslöser: die Ruhezustandsrate.**

**Die K3-Fälle.**

| ID | `Ruhe` | `Kampagne` | Δ | `strict` | `rest_per_run` | Auslöser |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| I06 | 0 | **0** | 0 | 1 | `[0,0,0]` | **Nullwert in `Kampagne`** (Median über `[0,0,1]`) |
| I20 | 0 | **0** | 0 | 1 | `[0,0,0]` | **Nullwert in `Kampagne`** (Median über `[1,0,0]`) |
| I21 | 0 | **0** | 0 | 1 | `[0,0,0]` | **Nullwert in `Kampagne`** (Median über `[0,0,1]`) |
| I31 | 1 | 1 | 0 | 1 | `[1,1,0]` | **Ruhezustandsrate** (`Kampagne` = `Ruhe` = 1) |

**Feststellung:** die vier K3-Fälle haben **nicht** durchgehend denselben mechanischen
Auslöser wie die K2-Fälle. Drei von ihnen (I06, I20, I21) entstehen bei einer
Ruhezustandsrate von **0** aus dem Vergleich `0 ≤ 0`, also aus dem Nullwert in
`Kampagne`; einer (I31) entsteht wie die K2-Fälle aus einer Ruhezustandsrate ≥ 1.
Keine Bewertung, keine Empfehlung zur Trennung.

---

## 4 Frage 4 — Zählen, was fehlt

Vollständige Liste der **markerfreien, leeren** Ergebniszellen des ersten Laufs. Gezählt
sind Datenzellen ohne ` — `, ohne `n. b.`, ohne `n. e.`; Kopf- und Trennzeilen sowie die
erste Spalte je Tabelle sind ausgenommen (dieselbe Zählweise wie
`c11_bericht_auswertungslauf.md` §3.1, Summe **412**).

| Tabelle | Spalte(n) | leer | Rechenweg im Code? | Fundstelle |
| --- | --- | ---: | --- | --- |
| T1 | Abweichung | 10 | **kein Rechenweg** — die Zeile endet auf dem Literal `" \| \|"` | [1217](../../tools/evaluate_campaign.py#L1217) |
| T4 (17 Sp.) | K2 kein-EN | 7 | **gerechnet** — dritter Zustand „kein strict-Treffer" | [1070-1072](../../tools/evaluate_campaign.py#L1070-L1072) |
| T4 (17 Sp.) | K3 kein-EN | 5 | **gerechnet** — dito (I13–I16 mit Marker in `strict`, dazu I23) | [1070-1072](../../tools/evaluate_campaign.py#L1070-L1072) |
| T4 Symmetrieteil | K1 Kampagne, K1 Δ | 64 | **berechnet, aber verworfen** — `campaign_counts` entstehen für K1, werden aber nur für `LLM_CONFIGS = ["K2","K3"]` gespeichert | [871](../../tools/evaluate_campaign.py#L871), [1049](../../tools/evaluate_campaign.py#L1049), [1527](../../tools/evaluate_campaign.py#L1527) |
| T4 Symmetrieteil | K4 Kampagne, K4 Δ, K5 Kampagne, K5 Δ | 128 | **kein Rechenweg** — `evaluate_k4k5_injection` gibt `campaign_counts=None`; die Zeile ist das Literal `["0 ᴬ¹⁴", "", ""]` | [929](../../tools/evaluate_campaign.py#L929), [1527](../../tools/evaluate_campaign.py#L1527) |
| T5 | `strict` P, R, F1 | 84 | **kein Rechenweg** — die Zeichenfolgen `precision`, `recall`, `f1` kommen in der Harness nur in Prosa vor; die Zellen sind `[""] * 6` | [1558](../../tools/evaluate_campaign.py#L1558) |
| T5 | `loc` P, R, F1 | 81 | **kein Rechenweg** — dito | [1558](../../tools/evaluate_campaign.py#L1558) |
| T6 | Invocationen, Model-Calls, Wanduhr aussen (Summe), Wanduhr aussen je Invocation | 20 | **Daten vorhanden, nicht gerendert** — `invocations`, `calls_total` und `wall_clock_ms` (gespeist aus `external_wall_clock_ms`) stehen in `t7["totals"]`; die T6-Zeile schreibt vier leere Felder | [645](../../tools/evaluate_campaign.py#L645), [1588](../../tools/evaluate_campaign.py#L1588) |
| T6 | Wanduhr innen (`wall_clock_ms`), für K1/K2/K3 | 3 | **Daten vorhanden, nicht gerendert** — dito | [1586](../../tools/evaluate_campaign.py#L1586), [1588](../../tools/evaluate_campaign.py#L1588) |
| T6 | Tokens in, Tokens out, Tokens je Check, Latenz je Call, für K2/K3 | 8 | **kein Rechenweg** — kein Token- und kein Latenzfeld wird irgendwo gelesen | [1587-1588](../../tools/evaluate_campaign.py#L1587-L1588) |
| T9 | Häufigkeit (Fall 6/K3, Fall 7/K5) | 2 | **gerechnet, Ergebnis 0** — `len(hits) or ''` druckt eine 0 als leer | [1669](../../tools/evaluate_campaign.py#L1669), [1673](../../tools/evaluate_campaign.py#L1673) |
| | **Summe** | **412** | | |

**Zur T4-Symmetriezeile:** die Spalte `K1/K4/K5 Ruhe` trägt keinen leeren Wert, sondern
konstant `0 ᴬ¹⁴` — ein ausgewiesener Berichtswert aus dem Clean-State-Audit, kein
gemessenes Artefakt (Anhang A, Zeile A-14; die Fussnote steht in der Ausgabe).

**Zur Erwartung des Auftrags:** T5 ist vollständig leer (165 von 165 markerfreien Zellen),
T6 vollständig (31 von 31), der T4-Symmetrieteil in `Kampagne` und `Δ` für K1/K4/K5
vollständig (192 von 192), die T1-Abweichungsspalte vollständig (10 von 10), die
T9-Häufigkeiten in zwei von neun Zeilen. Die T4-kein-EN-Zellen (12) waren in der
Erwartungsliste nicht genannt; sie sind gerechnete leere Zustände, keine Lücke.

---

## 5 Kosmetik — die doppelten Fallnummern in T9

**Feststellung: Renderabweichung vom Skelett, nicht Skelettvorgabe.**

Das Skelett (`docs/kapitel/kapitel7_tabellenskelette.md`, Zeilen 880–889) führt
**sieben Zeilen mit sieben verschiedenen Nummern**. Die Fälle 4, 5 und 6 tragen dort in
der Spalte *Pfad* den Wert **`K2/K3`** — eine Zeile für beide Konfigurationen. Das
Skelett hat ausserdem **sieben Spalten**; die letzte heisst *vorregistriert in*.

Die Harness rendert stattdessen **eine Zeile je (Fall, Konfiguration)**
([1663-1670](../../tools/evaluate_campaign.py#L1663-L1670)): Fall 4 und 5 je einmal für
K2 und einmal für K3 aus der Schleife über `LLM_CONFIGS`, Fall 6 ebenso aus der Schleife
über `("K2", "K3")`. Dadurch erscheinen die Nummern 4, 5 und 6 doppelt. Die Harness-Tabelle
hat zudem **sechs Spalten**; die Skelettspalte *vorregistriert in* fehlt.

Nicht geändert.

---

## 6 Protokoll der Zugriffe auf Kampagnenartefakte

| # | Datei(en) | Gesucht | Gefunden |
| --- | --- | --- | --- |
| 1 | `data/campaign/k5/k5_{3be646fe,a9d64451,616cb029,43f9fa5e}….stdout.txt` (4 Dateien, je 40 Zeilen, vollständig gelesen) | FAILURES-Sektion, Testname, genannte Kante/Modul, Zusammenfassungszeile | je genau eine FAILURES-Sektion, `test_component_imports_only_whitelisted_modules[<component>]`, je eine `AssertionError`-Zeile mit Trägermodul und Zielmodul, je `1 failed, 23 passed`, Wortlaut in §1.1 |
| 2 | dieselben 4 Dateien, durch `tools/match_k4k5.py --tool K5 --injection I13…I16` | Fundliste je Datei | je 1 Finding, `form=allowlist_violation`, `classification=begleitmeldung`, `strict_eligible=false`, `localized="treffer (richtige Stelle, falsche Kategorie)"`, `uncovered_nonempty_lines=0`; Tabelle in §1.2 |
| 3 | `data/campaign/{k4,k5}/*.stdout.txt` (64 Dateien) durch `match_k4k5.match` | Verteilung `(classification, strict_eligible, localized)` über alle Findings | 6 Kombinationen, Tabelle in §1.3; die 4 K5-CYCLE-Funde sind die einzigen K5-Findings mit abweichendem `localized`-Literal |
| 4 | `data/campaign/k3/k3_<sha>.json` (32 Dateien) | LLM-Records am Trägermodul, deren Kategorie von der erwarteten abweicht (`special`-Eimer) | 78 LLM-Records, 16 DERIVED-Records; 78 am Trägermodul, alle 78 mit erwartetem Tripel; **0** `special`-Kandidaten (§2.2) |
| 5 | `data/campaign/k3/k3_{531a1ff2,35061d85,dd414657,28a75749}….json` | je Repetition alle LLM-Records: `match_key`, `module`, `category` | I06 1 Record in Lauf 2 · I20 1 Record in Lauf 0 · I21 1 Record in Lauf 2 · I23 kein Record; `match_key` je wörtlich in §3.4 |
| 6 | `data/campaign/eval/c11_eval_full.json` (Archiv des ersten Laufs, nur gelesen) | `co_findings`, `specials`, T4-Werte je Injektion und Konfiguration, `t7.totals` | Zahlen in §1.3, §2.2, §3.4, §3.6 |

---

## 7 Arbeitsliste des zweiten Auswertungslaufs

| # | Punkt | Stelle | Einordnung |
| --- | --- | --- | --- |
| 1 | K5/`CYCLE_*`: `localized` wird 0 statt Treffer; die vier Funde passieren weder `classification == "treffer"` noch `localized == "treffer"` | [`evaluate_campaign.py:917-920`](../../tools/evaluate_campaign.py#L917-L920) | **DEFEKT** |
| 2 | T9 Fall 7 zählt aus `specials`, die Funde liegen in `co_findings` | [`evaluate_campaign.py:1671-1674`](../../tools/evaluate_campaign.py#L1671-L1674) | **DEFEKT** |
| 3 | T9 Häufigkeit: eine gerechnete 0 wird über `or ''` als leere Zelle gedruckt und ist von *(leer)* nicht unterscheidbar | [`evaluate_campaign.py:1669`](../../tools/evaluate_campaign.py#L1669), [1673](../../tools/evaluate_campaign.py#L1673) | **DEFEKT** (Darstellung) |
| 4 | T9 Fall 6 bei K3 = 0 | gegen alle 32 K3-Artefakte geprüft (§2.2) | **BEFUND** |
| 5 | T1-Abweichungsspalte: kein Rechenweg, die zehn leeren Zellen sind kein gerechnetes „keine Abweichung" | [`evaluate_campaign.py:1217`](../../tools/evaluate_campaign.py#L1217) | **DEFEKT** (bereits in C11 §3.4 gemeldet) |
| 6 | T5 P/R/F1: kein Rechenweg vorhanden, 165 Zellen | [`evaluate_campaign.py:1558`](../../tools/evaluate_campaign.py#L1558) | **NICHT IMPLEMENTIERT** |
| 7 | T6 Invocationen / Model-Calls / Wanduhr: Daten liegen in `t7["totals"]`, werden nicht gerendert, 23 Zellen | [`evaluate_campaign.py:1588`](../../tools/evaluate_campaign.py#L1588) | **NICHT GERENDERT** |
| 8 | T6 Tokens und Latenz: kein Feld wird gelesen, 8 Zellen | [`evaluate_campaign.py:1587-1588`](../../tools/evaluate_campaign.py#L1587-L1588) | **NICHT IMPLEMENTIERT** |
| 9 | T4 Symmetrieteil K1 `Kampagne`/`Δ`: für K1 gerechnet, wegen `LLM_CONFIGS` verworfen, 64 Zellen | [`evaluate_campaign.py:1049`](../../tools/evaluate_campaign.py#L1049), [1527](../../tools/evaluate_campaign.py#L1527) | **BERECHNET, VERWORFEN** |
| 10 | T4 Symmetrieteil K4/K5 `Kampagne`/`Δ`: kein Rechenweg, 128 Zellen | [`evaluate_campaign.py:929`](../../tools/evaluate_campaign.py#L929), [1527](../../tools/evaluate_campaign.py#L1527) | **NICHT IMPLEMENTIERT** |
| 11 | `Kampagne` (Median) und `strict` (Existenz über alle Läufe) stehen auf verschiedenen Aggregationsstufen; kein-EN verknüpft beide | [`evaluate_campaign.py:871`](../../tools/evaluate_campaign.py#L871), [883](../../tools/evaluate_campaign.py#L883), [1070-1072](../../tools/evaluate_campaign.py#L1070-L1072) | **OFFEN** — benannt, nicht entschieden |
| 12 | T4 kein-EN leer als dritter gerechneter Zustand, 12 Zellen | [`evaluate_campaign.py:1070-1072`](../../tools/evaluate_campaign.py#L1070-L1072) | **BEFUND** (keine Lücke) |
| 13 | T9 rendert eine Zeile je (Fall, Konfiguration) statt je Fall; Nummern 4, 5, 6 doppelt, Skelettspalte *vorregistriert in* fehlt | [`evaluate_campaign.py:1663-1670`](../../tools/evaluate_campaign.py#L1663-L1670), Skelett Zeilen 880–889 | **DEFEKT** (Darstellung, kosmetisch) |

**Punkt 11 ist keine Reparaturanweisung.** Ob `Kampagne` und `strict` auf dieselbe
Aggregationsstufe gehören, ist eine Entscheidung über die Metrikdefinition und liegt
ausserhalb dieses Auftrags.

---

## 8 Was dieser Auftrag nicht getan hat

Kein Fix, kein zweiter Auswertungslauf, keine Änderung an `tools/`, an den Instrumenten,
am Skelett, am Protokoll, an der Spezifikation oder unter `data/campaign/eval/`. Kein
Befund 08, kein C10-Abschlussbericht, kein Standdokument, keine offenen Punkte, kein
Arbeitsplan, keine Gate-Notiz, kein Z1. Kein `git push`.
