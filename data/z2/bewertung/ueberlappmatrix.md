# Z2 — Überlappmatrix zu §7 Punkt 5 (Vorbefund maschinell · ENTSCHEIDUNG durch den Autor)
**Auftrag S12 · Repo `masterarbeit` · Werkzeug `tools/prepare_z2_overlap.py` · 04.09.2026**
**Protokollstand:** `z2_protokoll_regelableitung.md`, SHA256 `862fdc3b7cfb264482db155575437edb25b1b436f92b5444b2137f1e332d9dde`. Die Abschnitte (a) und (d) unten sind **wörtlich aus diesem Stand ausgeschnitten**, nicht nacherzählt.
**Regeldatei:** `data/soll/architecture-rules.yaml`, SHA256 `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` — eingefroren, hier nur gelesen.
**Nenner:** 16 autorenformulierte Statements, aus der Datei gezählt (Verteilung unten).
**Nachschlageteil:** 16 bewertete Vorschläge (Z2-R-Klassen aus 17 Etiketten).
**Gelesen mit:** PyYAML.

**Dieses Blatt trifft die Entscheidung nicht.** Je Statement steht ein ausdrücklich als **MASCHINELL** gekennzeichneter **Vorbefund** — die Nachschlagearbeit, welche Vorschläge über den Sachverhalt des Statements überhaupt sprechen, samt **Begründung** und offengelegter **Prüfspur**. Die drei Felder der **ENTSCHEIDUNG DES AUTORS** sind **leer** und bleiben es, bis der Autor sie ausfüllt; sie sind **nicht vorbelegt**. Der Vorbefund ist ein **Vorschlag, keine Feststellung**.

Es steht hier **keine Ähnlichkeitszahl**, **kein `ratio`**, **kein Ranking** und **keine Sortierung nach Nähe** — der Vorbefund ist eine **Sachverhaltsprüfung, kein Textvergleich**. Kandidaten und Prüfspur stehen in **Etikettreihenfolge**.

**Es steht hier auch keine Summe.** Das Feld „n von 16“ in Teil 4 ist **leer**, und das Blatt bildet **keine Summe** über seine Vorbefunde: eine solche Zahl würde als Ergebnis gelesen.

---

## 1. Was zu erheben ist

### 1a (a) §7 Punkt 5 — wörtlich aus dem eingefrorenen Protokoll

> Ausgeschnitten zwischen den Ankern `5. **Sekundär, klar gelabelt:**` und `6. ~~**B1-vs-B2-Kontrast:**`, samt durchgestrichenem Alttext und Nennerkorrektur.

~~~~text
5. **Sekundär, klar gelabelt:** deskriptiver Überlapp mit der eingefrorenen
   `architecture-rules.yaml` — ~~„n von 6 autorenformulierten Regeln wurden
   sinngemäß vorgeschlagen"~~ — **falscher Nenner, mitkorrigiert am 01.09.2026
   (S1-A1):** die eingefrorene Regeldatei führt **SECHZEHN Statements über sechs
   Kategorien** (Hauptprotokoll Rev. 19: „die **sechzehn** Regelstatements";
   nachgezählt in `data/soll/architecture-rules.yaml`: 16 Regeln —
   `FORBIDDEN_RELATION` 4, `ABSENCE_REQUIRED` 4, `API_CONTRACT` 4, `CYCLE` 2,
   `FORBIDDEN_SIGNATURE_TYPE` 1, `STRUCTURAL_PLACEMENT` 1). Berichtet wird daher
   **„n von 16 autorenformulierten Statements wurden sinngemäß vorgeschlagen"**.
   **Der Charakter der Größe bleibt unverändert:** sekundär, deskriptiv.
   Ausdrücklich KEIN Korrektheits- oder
   Recall-Maß (Autor beider Seiten; gleiche Logik wie Gold-Degradierung in
   Befund 01).
~~~~

### 1b (b) Die Auslegung von „sinngemäss“ — Anleitung, keine Vorbelegung

**Derselbe Sachverhalt wird verboten oder gefordert — unabhängig von Wortlaut, Kategorielabel und Scope-Granularität.** NICHT verlangt sind derselbe Wortlaut, dieselbe Kategorie oder dieselbe Präzision. Fasst ein Vorschlag den Sachverhalt **BREITER** als das Soll-Statement, zählt er **MIT VERMERK**; fasst er ihn enger oder trifft er nur einen Teil, ist das in der Begründung auszuweisen. **Mehrfachnennung ist zulässig:** ein Vorschlag kann mehreren Statements entsprechen und umgekehrt.

Diese Auslegung sagt, **woran** zu messen ist. Sie sagt **nicht**, wie eine einzelne Zeile ausfällt — das entscheidet der Autor am Wortlaut, der unten in beiden Teilen zeichengleich steht.

**Nach demselben Maßstab ist der maschinelle Vorbefund gebildet:** ein Etikett steht als **Kandidat**, wenn der Vorschlag über **denselben Sachverhalt** spricht — unabhängig von Wortlaut, Kategorielabel und Scope-Granularität —, und die Begründung weist aus, **wo Reichweite oder Granularität abweichen**.

### 1c (c) Das zweistufige Verfahren — Vorbefund maschinell, ENTSCHEIDUNG durch den Autor

**Stufe 1 — maschinell, in diesem Blatt bereits ausgeführt.** Je Soll-Statement steht ein **VORBEFUND (MASCHINELL, kein Ergebnis)** mit vier Feldern: dem Verdikt „Kandidat vorhanden“ oder „kein Kandidat“, den **Etiketten** der Vorschläge, die über denselben Sachverhalt sprechen, einer **Begründung** und einer **PRÜFSPUR**, die die erwogenen und ausgeschlossenen Etiketten je mit einem Grund nennt. Die Prüfspur ist **Pflicht** — auch und besonders bei „kein Kandidat“: sie macht die Nachschlagearbeit **gegenlesbar**, statt nur ein Ergebnis zu behaupten.

**Stufe 2 — der Autor, je Zeile.** Die drei Felder unter **ENTSCHEIDUNG DES AUTORS** sind **leer**. **Der Autor bestätigt oder überstimmt JEDE der sechzehn Zeilen; eine unbestätigte Zeile gilt nicht als entschieden.** Der Vorbefund bindet ihn nicht: er ist ein **Vorschlag, keine Feststellung**, und in seinen Formulierungen bewusst im Konjunktiv gehalten — „spricht über denselben Sachverhalt“, „Kandidat“, „zu prüfen“, nicht „entspricht“ oder „ist erfüllt“.

**Warum zweistufig.** „Sinngemäss“ ist **dieselbe Urteilsart wie das Z2-R-Kriterium** (§6: Duplikate bei Übereinstimmung in **Kategorie, Scope und Kernaussage**). **Z2-R wurde in S10 ausdrücklich NICHT maschinisiert** — die Zusammenführung war dort auf **Zeichengleichheit** beschränkt, damit das Werkzeug **keine inhaltliche Entscheidung abnimmt**. Damit **beide Größen konsistent behandelt** werden, entscheidet der Autor auch hier je Zeile; das Werkzeug leistet die **Nachschlagearbeit** und legt seine **Prüfspur offen**.

**Und deshalb keine Summe.** Das Blatt bildet **keine Summe** über die Vorbefunde — sie würde als Ergebnis gelesen, obwohl **keine einzige Zeile entschieden** ist. Das Summenfeld in Teil 4 bleibt **leer**.

### 1d (d) Die Einhegung — was diese Zahl NICHT ist

Wörtlich aus §7 Punkt 5: **„Der Charakter der Größe bleibt unverändert:** sekundär, deskriptiv. Ausdrücklich KEIN Korrektheits- oder Recall-Maß (Autor beider Seiten; gleiche Logik wie Gold-Degradierung in Befund 01).“

Ausdrücklich, und beim Ausfüllen mitzulesen:

1. **Die Größe ist sekundär und deskriptiv** — sie steht neben den Punkten 1–4 des §7, nicht über ihnen.
2. **KEIN Korrektheitsmaß und KEIN Recall-Maß.** **Der Autor hat beide Seiten formuliert** — die sechzehn Soll-Statements **und** das Messobjekt, auf das sie passen. Die Zahl darf **NIE** als „das Modell hat n von 16 Regeln gefunden“ gelesen werden, sondern **nur** als „n Statements haben eine Entsprechung unter den Vorschlägen“.
3. **Analogie im Protokoll:** die **Gold-Degradierung aus Befund 01** — dieselbe Logik, dieselbe Grenze.
4. **T-Z2-8:** die **Affordanzen der sechs Kategorien stecken strukturell im Testrepo**. Eine hohe Überschneidung wäre **insoweit Eigenschaft des Messobjekts**, nicht Leistung des Modells. Der Wortlaut des Threats steht unter 1e.

### 1e (e) Abgrenzung zu §7 Punkt 3 — verschiedene Größen, verschiedene Nenner

| | §7 Punkt 3 — Abdeckungsmatrix | §7 Punkt 5 — Überlapp (dieses Blatt) |
|---|---|---|
| Frage | Welche der **sechs KATEGORIEN** sind durch **mindestens einen normativen, prüfbaren Vorschlag** belegt? | Welche der **sechzehn EINZELNEN Statements** haben eine Entsprechung unter den Vorschlägen? |
| Nenner | **6** Kategorien | **16** Statements |
| Status | in `auswertung.json` bereits ausgezählt (S11) | **steht aus** |

**Nicht zu verwechseln und nicht gegeneinander zu rechnen.** Die beiden Zahlen haben verschiedene Bezugsmengen; ein Verhältnis zwischen ihnen ist ohne Bedeutung.

> §7 Punkt 3, wörtlich:

~~~~text
3. **Abdeckungsmatrix:** die sechs Ebene-1-Abweichungstypen (`FORBIDDEN_RELATION`,
   `CYCLE`, `ABSENCE_REQUIRED`, `FORBIDDEN_SIGNATURE_TYPE`, `STRUCTURAL_PLACEMENT`,
   `API_CONTRACT`) + „sonstige" × Modell × Bedingung — welche Klassen tauchen
   überhaupt auf (≥ 1 normativer, prüfbarer Vorschlag)?
   **Ergänzt 02.09.2026 (Auftrag S1-A1b):** die Eingabe trägt **zwölf Vererbungskanten**
   (`extends`, §3a-1 Nachtrag 02.09.2026, §3a-2). Ein daraus abgeleiteter Vorschlag —
   etwa ein **Vererbungsverbot über Komponentengrenzen** — entspricht **keiner der sechs
   Kategorien**. Er ist **KEIN Fehler, sondern ein BEFUND**, wird hier als **NICHT
   ZUORDENBAR** geführt, und **Z2-Z erhält dafür ausdrücklich den Wert „keiner der
   sechs"** (§6). Der Wert wird **getrennt von „sonstige" ausgewiesen** — „sonstige" ist
   die Auffangkategorie **innerhalb** der Kodierung, „keiner der sechs" die begründete
   Feststellung, dass die **Kodierung den Vorschlag nicht trägt**. **Die Matrix ist
   insoweit Eigenschaft des Messobjekts** (T-Z2-8, §10).
~~~~

> T-Z2-8 (§10), wörtlich:

~~~~text
| **T-Z2-8** | **Die EINGABE trägt die sechs Kategorien strukturell** (neu 01.09.2026). Vier **reservierte Ports** in öffentlichen Signaturen (`TokenSigner`, `RateProvider`, `PaymentGateway`, `Clock`; Hauptprotokoll §3 Rev. 16 (A): „erscheinen in der Clean-Baseline in **genau einem** Modul — ihrem Träger — und dort in einer **öffentlichen Methodensignatur**"), die **Suffixkonventionen** `_repo` / `_query` / `_index` / `_models` (`customer_repo`, `session_repo`, `invoice_repo`; `invoice_query`; `legacy_token_index`, `legacy_order_index`, `legacy_invoice_index`; `*_models`), **geschützte Internals** (`depot.core.adapters.internal`, R-PROTECT-1) und **Zyklen mit genau zwei Komponenten** (R-CYCLE-2: `orders_services` / `orders_services_pricing`) — **und, ergänzt 02.09.2026 (Auftrag S1-A1b), die VERERBUNGSSTRUKTUR des Testrepos: zwölf `extends`-Kanten, in `x-triton-inner-artefact-relations` (1 Knoten, 4 Einträge) und `x-triton-cross-artefact-relations` (5 Knoten, 8 Einträge), Träger ausschliesslich Modulknoten (§3a-1 Nachtrag 02.09.2026, §3a-2)** | **Nicht heilbar, benannt.** Die **Abdeckungsmatrix (§7 Punkt 3) ist damit teils Eigenschaft des synthetischen Messobjekts, nicht des Modells.** Die Prompt-Auflage aus §4 (**keine Kategorie beim Namen**) deckt das **NICHT** ab — sie hält die Kategorien aus dem *Prompt*, nicht aus dem *Repositorium*. **Ergänzt 02.09.2026 (S1-A1b): das gilt AUCH für den nicht zuordenbaren Teil der Matrix** — Vorschläge mit Z2-Z-Wert **„keiner der sechs"** (§6, §7 Punkt 3) entstehen an einer Struktur, die **die Eingabe mitbringt** |
~~~~

### 1f Der Nenner, aus der Datei gezählt

`data/soll/architecture-rules.yaml` (SHA256 `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95`) führt **16 Regelstatements** über **6 Kategorien**:

| `category` | Zahl |
|---|---|
| `ABSENCE_REQUIRED` | 4 |
| `API_CONTRACT` | 4 |
| `FORBIDDEN_RELATION` | 4 |
| `CYCLE` | 2 |
| `FORBIDDEN_SIGNATURE_TYPE` | 1 |
| `STRUCTURAL_PLACEMENT` | 1 |
| **Summe** | **16** |

Die Reihenfolge der Statements in Teil 3 ist die **Dateireihenfolge**. Sie ist **nicht nach Kategorie gruppiert** — eine Gruppierung wäre bereits eine Lesehilfe in eine Richtung.

### 1g Vermerk zur aufgehobenen Verblindung

Die **Herkunft je Vorschlagsklasse (K2 × B1 / K3 × B1) ist unten angegeben**. Der Zuordnungsschlüssel ist mit **S11** aufgelöst; die Bewertung war zu diesem Zeitpunkt abgeschlossen, die Verblindung ist beendet.

**Die Größe des §7 Punkt 5 ist sekundär und deskriptiv, nicht bedingungsvergleichend.** Wird sie je Zelle aufgeschlüsselt, geschieht das **nach Aufhebung der Verblindung** — und das ist **zu berichten**.

---

## 2. Nachschlageteil — die 16 bewerteten Vorschläge

**Reihenfolge:** die Etikettreihenfolge `P-01` … `P-17`. **Nicht** nach Ähnlichkeit, Kategorie oder Herkunft sortiert — die Reihenfolge trägt keine Information über die Zuordnung.

Die vier Dimensionen (`kind`, Z2-P, Z2-G, Z2-Z) sind **vom Bewerter gesetzt und bereits entschieden** (§6, ausgezählt in `auswertung.json`); sie stehen hier als Lesehilfe für „sinngemäss“ und sind **keine Vorbelegung** der drei leeren Felder.

---

### `P-01` + `P-11`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-01` + `P-11` |
| `category` | `dependency-inversion` |
| `severity` | `error` |
| `scope.components` | `depot.billing.services` · `depot.identity.services` · `depot.orders.services` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run0` · `k3_b1/run1` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Service classes must have their dependencies limited to interfaces defined in depot.core.ports; they must not directly instantiate or depend on concrete adapter or repository classes.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `structural` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | FORBIDDEN_RELATION |

---

### `P-02`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-02` |
| `category` | `dependency-control` |
| `severity` | `error` |
| `scope.components` | `depot.billing.services` · `depot.orders.services` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run2` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Services in depot.billing.services and depot.orders.services must not depend on services in each other's packages. They may only depend on services in depot.identity.services and depot.core.services (if any) and on repositories and ports.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `structural` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | unklar |
| **Z2-Z** Zuordnung | FORBIDDEN_RELATION |

---

### `P-03`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-03` |
| `category` | `error-handling-consistency` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api.schemas` · `depot.identity.api.schemas` · `depot.orders.api.schemas` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run0` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
These modules must not define a function named error_body; they must import it from a shared location.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `semantic` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | sonstige |

---

### `P-04`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-04` |
| `category` | `dependency-management` |
| `severity` | `warning` |
| `scope.components` | `depot.billing.api` · `depot.billing.services` · `depot.billing.repository` · `depot.billing.models` |
| Herkunft (Bedingung) | `k2_b1` |
| Herkunft (Läufe) | `k2_b1/run0` · `k2_b1/run1` · `k2_b1/run2` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Classes and functions within the billing components must not directly import the standard logging module. Instead, they should obtain a logger from a shared logging helper module.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `structural` |
| **Z2-P** Prüfbarkeit | nicht prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | FORBIDDEN_RELATION |

---

### `P-05`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-05` |
| `category` | `code-quality` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api` · `depot.billing.services` · `depot.billing.repository` · `depot.billing.models` |
| Herkunft (Bedingung) | `k2_b1` |
| Herkunft (Läufe) | `k2_b1/run0` · `k2_b1/run1` · `k2_b1/run2` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
All classes and functions within the billing components should be well-documented and follow a consistent coding style. This includes using docstrings to describe the purpose and behavior of each function, and following a consistent naming convention for variables and functions.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `semantic` |
| **Z2-P** Prüfbarkeit | nicht prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | sonstige |

---

### `P-06`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-06` |
| `category` | `code-reusability` |
| `severity` | `warning` |
| `scope.components` | `depot.billing.api` · `depot.billing.services` · `depot.billing.repository` · `depot.billing.models` |
| Herkunft (Bedingung) | `k2_b1` |
| Herkunft (Läufe) | `k2_b1/run0` · `k2_b1/run1` · `k2_b1/run2` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Classes and functions within the billing components should not duplicate logic found in other modules. Instead, they should reuse existing functions or classes where possible.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `semantic` |
| **Z2-P** Prüfbarkeit | nicht prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | sonstige |

---

### `P-07`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-07` |
| `category` | `data-access-layer` |
| `severity` | `error` |
| `scope.components` | `depot.billing.repository` · `depot.identity.repository` · `depot.orders.repository` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run2` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
A repository module may only import models from its own package (e.g., depot.billing.models for billing.repository) and from depot.core.ports. It must not import models from any other package.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `structural` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | Spiegelung |
| **Z2-Z** Zuordnung | FORBIDDEN_RELATION |

---

### `P-08`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-08` |
| `category` | `interface-segregation` |
| `severity` | `error` |
| `scope.components` | `depot` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run2` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
All protocols (classes inheriting from typing.Protocol) must be defined in the depot.core.ports module. No other module may define a class that inherits from typing.Protocol.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `semantic` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | keiner der sechs |

---

### `P-09`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-09` |
| `category` | `error-handling-centralization` |
| `severity` | `warning` |
| `scope.components` | `depot.billing.api.routes` · `depot.identity.api.routes` · `depot.orders.api.routes` · `depot.billing.api.schemas` · `depot.identity.api.schemas` · `depot.orders.api.schemas` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run1` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Functions that map DepotError to HTTP status codes or error response bodies must be defined only in depot.core.errors; all other modules must obtain these functions by importing from that module.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `semantic` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | sonstige |

---

### `P-10`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-10` |
| `category` | `error-handling-consistency` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api.routes` · `depot.identity.api.routes` · `depot.orders.api.routes` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run0` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
These modules must not define a function named status_for; they must obtain the error-to-status mapping from a shared location (e.g., depot.core.errors).
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `semantic` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | sonstige |

---

### `P-12`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-12` |
| `category` | `code-organization` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api` · `depot.billing.services` · `depot.billing.repository` · `depot.billing.models` |
| Herkunft (Bedingung) | `k2_b1` |
| Herkunft (Läufe) | `k2_b1/run0` · `k2_b1/run1` · `k2_b1/run2` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
All classes and functions within the billing components should be organized into logical modules and packages. This includes grouping related classes and functions together and ensuring that each module has a single responsibility.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `semantic` |
| **Z2-P** Prüfbarkeit | nicht prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | sonstige |

---

### `P-13`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-13` |
| `category` | `error-handling` |
| `severity` | `error` |
| `scope.components` | `depot` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run2` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Only the depot.core.errors module may define error classes (classes inheriting from Exception). All other modules in the codebase must not define any error classes.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `semantic` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | keiner der sechs |

---

### `P-14`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-14` |
| `category` | `layered-architecture` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api.routes` · `depot.identity.api.routes` · `depot.orders.api.routes` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run1` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
API route classes shall receive only service-layer dependencies (and optionally mappers) in their constructors and must not import repository, model, or adapter modules directly.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `structural` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | unklar |
| **Z2-Z** Zuordnung | FORBIDDEN_RELATION |

---

### `P-15`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-15` |
| `category` | `error-handling` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api` · `depot.billing.services` · `depot.billing.repository` · `depot.billing.models` |
| Herkunft (Bedingung) | `k2_b1` |
| Herkunft (Läufe) | `k2_b1/run0` · `k2_b1/run1` · `k2_b1/run2` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
All error handling within the billing components should be consistent and follow a common pattern. This includes using a shared error handling module and ensuring that all error messages are localized and user-friendly.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `semantic` |
| **Z2-P** Prüfbarkeit | nicht prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | sonstige |

---

### `P-16`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-16` |
| `category` | `mapper-purity` |
| `severity` | `warning` |
| `scope.components` | `depot.billing.mappers` · `depot.identity.mappers` · `depot.orders.mappers` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run0` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Modules in these packages must not import depot.core.errors or any other error-related modules; they should perform only data transformation without error handling.
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `structural` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | FORBIDDEN_RELATION |

---

### `P-17`

| Feld | Wert |
|---|---|
| Etikett(en) | `P-17` |
| `category` | `duplication` |
| `severity` | `warning` |
| `scope.components` | `depot` |
| Herkunft (Bedingung) | `k3_b1` |
| Herkunft (Läufe) | `k3_b1/run2` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
The functions `status_for` (signature: (error: depot.core.errors.DepotError) -> int) and `error_body` (signature: (error: depot.core.errors.DepotError) -> dict[str, str]) must not be defined in more than one module. They should be defined in a single shared utility module (e.g., depot.core.utils).
~~~~

**Vom Bewerter gesetzt (§6, bereits entschieden):**

| Dimension | Eintrag |
|---|---|
| `kind` | `semantic` |
| **Z2-P** Prüfbarkeit | prüfbar |
| **Z2-G** Gehalt | normativ |
| **Z2-Z** Zuordnung | sonstige |

---

## 3. Die Matrix — ein Abschnitt je Soll-Statement

**Reihenfolge:** Dateireihenfolge von `architecture-rules.yaml`. Je Abschnitt stehen zuerst die Angaben des Statements, dann der **maschinelle Vorbefund** mit vier Feldern, dann die **drei leeren Felder der ENTSCHEIDUNG DES AUTORS**. Die beiden Blöcke sind **sichtbar getrennt**; nichts aus dem Vorbefund ist in die Entscheidungsfelder übernommen.

---

### R-LAYER-1

| Feld | Wert |
|---|---|
| Soll-ID | `R-LAYER-1` |
| `category` | `FORBIDDEN_RELATION` |
| `kind` | `structural` |
| `severity` | `error` |
| `scope.components` | `identity_api` · `identity_repository` · `identity_services` · `orders_api` · `orders_repository` · `orders_services` · `billing_api` · `billing_repository` · `billing_services` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
Inside every bounded context (`identity`, `orders`, `billing`) the layers are strictly ordered: `api` -> `services` -> `repository` -> `models`. A module may depend only on the layer directly below it in its own context. Two things are therefore forbidden: an import from a lower layer into a higher one (a back call, for example a module of `<context>.repository` importing `<context>.services`), and an import that skips the intermediate layer (a skip call, for example a module of `<context>.api` importing `<context>.repository` directly instead of going through `<context>.services`). Report the finding as a dependency edge: `subject.from` is the importing component, `subject.to` the imported one.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **Kandidat vorhanden** |
| **(b) Kandidat(en)** | `P-07` · `P-14` |
| **(c) Begründung des Vorbefunds** | `P-14` spricht über denselben Sachverhalt wie die Sprungklausel des Statements: „must not import repository, model, or adapter modules directly“ ist der Schichtsprung `api` → `repository`, den R-LAYER-1 verbietet. Der Vorschlag ist **enger** — er trifft nur die api-Schicht (drei `routes`-Module) und spricht den Rückruf aus einer unteren Schicht nicht aus. `P-07` beschränkt die Importe eines repository-Moduls auf die eigenen Models und `depot.core.ports`; liest man diese Erlaubnisliste abschliessend, ist der Rückruf `repository` → `services` mitverboten — als Nebenfolge und nur für eine Schicht. **Beides ist zu prüfen.** |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | verbietet den Services die Abhängigkeit von konkreten Repositories, also gerade die Kante `services` → `repository`, die R-LAYER-1 als Schritt in die nächsttiefere Schicht erlaubt — gegenläufig |
| `P-02` | zieht eine Grenze zwischen den Kontexten, nicht zwischen den Schichten eines Kontexts |
| `P-03` | regelt den Definitionsort einer Fehlerfunktion, keine Schichtrichtung |
| `P-04` | Importverbot gegen `logging`, keine Aussage über Schichten |
| `P-05` | Stil- und Dokumentationsaussage ohne Importrichtung |
| `P-06` | Duplikationsverbot ohne Importrichtung |
| `P-08` | Definitionsort der Protokolle |
| `P-09` | desgleichen, Definitionsort statt Importrichtung |
| `P-10` | desgleichen |
| `P-12` | Organisationsaussage ohne Importrichtung |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-15` | Fehlerbehandlungsaussage ohne Importrichtung |
| `P-16` | betrifft die mappers-Pakete, die in der Schichtordnung des Statements nicht vorkommen |
| `P-17` | Duplikationsverbot für zwei benannte Funktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | ja |
| **durch welche(s) P-xx** | `P-14` |
| **Begründung des Autors** | Teilweise Entsprechung: P-14 verbietet den drei API-Routen direkte Repository- und Modelimporte und trifft damit die Sprungklausel. Rückrufe und die übrigen Schichten bleiben ungeregelt; die Mapper-Erlaubnis ist eine zusätzliche Abweichung. P-07 zähle ich hier nicht mit: Sein Wortlaut beschränkt die Herkunft importierter Models, verbietet aber nicht eindeutig sämtliche anderen Importe. Ein Rückrufverbot repository → services lässt sich daraus nur durch eine zusätzliche Auslegung gewinnen. |

---

### R-PROTECT-1

| Feld | Wert |
|---|---|
| Soll-ID | `R-PROTECT-1` |
| `category` | `FORBIDDEN_RELATION` |
| `kind` | `structural` |
| `severity` | `error` |
| `scope.components` | `core_adapters` · `core_adapters_internal` · `identity_services` · `orders_services` · `billing_services` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The package `depot.core.adapters.internal` (component `core_adapters_internal`) is internal to the adapter package. The adapter facade `depot.core.adapters` is its only permitted importer. Every other component — in particular the three service components `identity_services`, `orders_services` and `billing_services` — must go through the public surface of `depot.core.adapters` and must never import a module of `depot.core.adapters.internal` directly, past the facade. Report the finding as a dependency edge: `subject.from` is the importing component, `subject.to` the imported one.
~~~~

**`predicate`** — zeichengleich:

| Feld | Wert |
|---|---|
| `predicate.type` | `import-boundary` |
| `predicate.allowed_importers` | `core_adapters` |

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **Kandidat vorhanden** |
| **(b) Kandidat(en)** | `P-01 + P-11` · `P-14` |
| **(c) Begründung des Vorbefunds** | Beide sprechen über denselben Sachverhalt — das Verbot, aus einer höheren Schicht heraus konkrete Adaptermodule zu importieren: `P-01 + P-11` für die drei Servicepakete („must not directly instantiate or depend on concrete adapter … classes“), `P-14` für die api-Routen. Beide fassen **breiter**, weil sie den Adapterzugriff insgesamt verbieten, während R-PROTECT-1 die Fassade `depot.core.adapters` ausdrücklich **erlaubt** und nur `depot.core.adapters.internal` sperrt; die Fassaden-Ausnahme steht in keinem der beiden. **Zu prüfen ist**, ob ein breiteres Verbot als Entsprechung zu einem Fassadenverbot gelten soll. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-02` | Kontextgrenze zwischen `orders` und `billing`, keine Fassadengrenze |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | Importverbot gegen `logging`, ein anderes Modul |
| `P-05` | Stil und Dokumentation |
| `P-06` | Duplikation |
| `P-07` | beschränkt die repository-Schicht auf eigene Models und Ports, nennt die Adapter nicht |
| `P-08` | regelt, wo Protokolle definiert werden, nicht wer Adapter importieren darf |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | Organisation |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-15` | Fehlerbehandlung |
| `P-16` | Importverbot für mappers, aber gegen `depot.core.errors`, nicht gegen die Adapter-Internals |
| `P-17` | Duplikationsverbot für zwei benannte Funktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | ja |
| **durch welche(s) P-xx** | `P-01` + `P-11` · `P-14` |
| **Begründung des Autors** | Teilweise Entsprechung mit breiterem Verbot: Die Adapterverbote erfassen auch direkte Zugriffe auf konkrete Internals, bei P-01/P-11 aus Services und bei P-14 aus API-Routen. Sie verbieten zugleich die im Soll erlaubte Fassade. Der Importeurkreis ist dagegen enger als „jede andere Komponente“; weder die exklusive Fassadenberechtigung noch die vollständige Importgrenze werden vorgeschlagen. |

---

### R-INDEP-1

| Feld | Wert |
|---|---|
| Soll-ID | `R-INDEP-1` |
| `category` | `FORBIDDEN_RELATION` |
| `kind` | `structural` |
| `severity` | `error` |
| `scope.components` | `orders_api` · `orders_mappers` · `orders_models` · `orders_repository` · `orders_services` · `orders_services_pricing` · `billing_api` · `billing_mappers` · `billing_models` · `billing_repository` · `billing_services` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The bounded contexts `orders` and `billing` are mutually independent. No module of any `orders_*` component may import a module of any `billing_*` component, and no module of any `billing_*` component may import a module of any `orders_*` component — in either direction and at every layer, `api`, `services`, `repository`, `models` and `mappers` alike. Whatever the two contexts share is reached through `core`, through the adapter facade `depot.core.adapters`, or through `identity_services`. Report the finding as a dependency edge: `subject.from` is the importing component, `subject.to` the imported one.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **Kandidat vorhanden** |
| **(b) Kandidat(en)** | `P-02` · `P-07` |
| **(c) Begründung des Vorbefunds** | `P-02` spricht über dieselbe Kontextgrenze zwischen `orders` und `billing`, fasst sie aber **enger**: nur die services-Pakete, während R-INDEP-1 alle Schichten beider Kontexte erfasst (`api`, `services`, `repository`, `models`, `mappers`). `P-07` verbietet einem repository-Modul Models fremder Pakete und trifft damit die Kante `billing.repository` → `orders.models` mit — **nur teilweise**, auf der models-Achse und ohne die Kontextgrenze als solche zu benennen. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | bindet die Services an die Ports, zieht keine Grenze zwischen zwei Kontexten |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | spricht über die billing-Komponenten, aber über `logging` |
| `P-05` | desgleichen, über Stil und Dokumentation |
| `P-06` | desgleichen, über Duplikation |
| `P-08` | Definitionsort der Protokolle im Kern |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | desgleichen, über Organisation |
| `P-13` | Definitionsort der Fehlerklassen im Kern |
| `P-14` | Schichtgrenze innerhalb eines Kontexts |
| `P-15` | desgleichen, über Fehlerbehandlung |
| `P-16` | Importverbot für mappers gegen `depot.core.errors`, keine Kontextgrenze |
| `P-17` | Duplikationsverbot für zwei benannte Funktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | ja |
| **durch welche(s) P-xx** | `P-02` · `P-07` |
| **Begründung des Autors** | Teilweise Entsprechung: P-02 verbietet die gegenseitigen Serviceabhängigkeiten von orders und billing. P-07 verbietet zusätzlich Repositoryimporte fremder Models und damit auch orders.repository → billing.models sowie die Gegenrichtung. P-07 erfasst darüber hinaus identity, bleibt aber auf Modelimporte beschränkt. Keiner der Vorschläge fordert die Unabhängigkeit beider Kontexte über sämtliche Schichten; die Erlaubnis von Repositoryabhängigkeiten in P-02 ist nicht nach Kontext eingeschränkt. |

---

### R-CORE-1

| Feld | Wert |
|---|---|
| Soll-ID | `R-CORE-1` |
| `category` | `FORBIDDEN_RELATION` |
| `kind` | `structural` |
| `severity` | `error` |
| `scope.components` | `core` · `core_adapters` · `core_adapters_internal` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The kernel and its adapters do not depend on any business context. The component `core` (`depot`, `depot.core` and its modules `config`, `errors`, `ports`) has no outgoing dependency at all. `core_adapters` may depend only on `core` and on `core_adapters_internal`; `core_adapters_internal` may depend only on `core`. No module of these three components may import a module of `identity_*`, `orders_*` or `billing_*`: the direction of dependency always points towards the kernel, never out of it. Report the finding as a dependency edge: `subject.from` is the importing component, `subject.to` the imported one.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **kein Kandidat** |
| **(b) Kandidat(en)** | — |
| **(c) Begründung des Vorbefunds** | Der Sachverhalt des Statements ist die **Abhängigkeitsrichtung DES KERNS**: `core`, `core_adapters` und `core_adapters_internal` dürfen keinen Businesskontext importieren, und `core` trägt überhaupt keine ausgehende Kante. Dieser Sachverhalt kommt in **keinem** der 16 Vorschläge vor. Die Vorschläge, die den Kern nennen, sprechen sämtlich über Kanten, die **auf ihn zulaufen**, oder über den **Ort**, an dem etwas im Kern zu definieren ist — nie über das, was der Kern seinerseits importieren darf. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | richtet die Services auf `depot.core.ports` aus, also eine eingehende Kante — die Gegenrichtung |
| `P-02` | Kontextgrenze zwischen zwei Businesskontexten |
| `P-03` | verbietet den schemas-Modulen eine eigene `error_body` — eingehende Kante |
| `P-04` | Importverbot gegen `logging` in den billing-Komponenten |
| `P-05` | Stil und Dokumentation |
| `P-06` | Duplikation |
| `P-07` | erlaubt der repository-Schicht `depot.core.ports`, wieder eine eingehende Kante |
| `P-08` | verlangt Protokolle in `depot.core.ports`: ein Definitionsort im Kern, keine Aussage über dessen Abhängigkeiten |
| `P-09` | verlangt die Fehler-Mappingfunktionen in `depot.core.errors` — Definitionsort |
| `P-10` | desgleichen für `status_for` |
| `P-12` | Organisation |
| `P-13` | dasselbe für Fehlerklassen in `depot.core.errors` |
| `P-14` | Schichtgrenze innerhalb eines Kontexts |
| `P-15` | Fehlerbehandlung |
| `P-16` | verbietet den mappers den Import von `depot.core.errors`, erneut eine eingehende Kante |
| `P-17` | verlangt `status_for` und `error_body` in einem gemeinsamen Modul — Definitionsort |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | nein |
| **durch welche(s) P-xx** | — |
| **Begründung des Autors** | Kein Vorschlag beschränkt die ausgehenden Abhängigkeiten von core, core_adapters oder core_adapters_internal. Portnutzung und zentrale Definitionsorte betreffen andere Sachverhalte; daraus folgt kein Verbot von Kernimporten aus Businesskontexten. |

---

### R-CYCLE-1

| Feld | Wert |
|---|---|
| Soll-ID | `R-CYCLE-1` |
| `category` | `CYCLE` |
| `kind` | `structural` |
| `severity` | `error` |
| `scope.components` | `identity_api` · `identity_mappers` · `orders_api` · `orders_mappers` · `billing_api` · `billing_mappers` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
Within a bounded context the sibling packages `<context>.api` and `<context>.mappers` must not form an import cycle. The only permitted direction is `<context>.api` -> `<context>.mappers`: the API layer builds its payloads through the mappers. A module of `<context>.mappers` must never import a module of `<context>.api`; such a back edge closes a cycle between two sibling packages of the same context. Report the finding as a dependency edge: `subject.from` is the importing component, `subject.to` the imported one — the edge that closes the cycle.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **kein Kandidat** |
| **(b) Kandidat(en)** | — |
| **(c) Begründung des Vorbefunds** | Der Sachverhalt des Statements ist der **Importzyklus zwischen den Geschwisterpaketen** `<context>.api` und `<context>.mappers` und das Verbot der Rückkante `mappers` → `api`. Kein Vorschlag verbietet diese Rückkante, und **keiner der 16 verwendet den Zyklusbegriff überhaupt**. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | Kanten zwischen Services und Konkreta, kein Geschwisterpaar eines Kontexts |
| `P-02` | Kanten zwischen zwei Kontexten |
| `P-03` | Definitionsort von `error_body` in den schemas-Modulen |
| `P-04` | Importverbot gegen `logging` |
| `P-05` | Stil und Dokumentation |
| `P-06` | Duplikation |
| `P-07` | Kanten der repository-Schicht |
| `P-08` | Definitionsort der Protokolle |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` in den routes-Modulen |
| `P-12` | Organisation |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | nennt die mappers als für die api-Routen zulässige Abhängigkeit, spricht also über die von R-CYCLE-1 **erlaubte** Richtung, nicht über die verbotene Rückkante |
| `P-15` | Fehlerbehandlung |
| `P-16` | betrifft die mappers, verbietet ihnen aber den Import von `depot.core.errors`, nicht den der api |
| `P-17` | Duplikationsverbot für zwei benannte Funktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | nein |
| **durch welche(s) P-xx** | — |
| **Begründung des Autors** | Kein Vorschlag fordert Zyklusfreiheit zwischen api und mappers oder verbietet allgemein die Rückkante mappers → api. P-14 erlaubt nur die Hinrichtung. P-16 untersagt Fehlerimporte aus mappers; auch wenn dies einzelne API-Fehlerimporte treffen könnte, ergibt sich daraus keine allgemeine Grenze zwischen diesen Geschwisterpaketen. |

---

### R-CYCLE-2

| Feld | Wert |
|---|---|
| Soll-ID | `R-CYCLE-2` |
| `category` | `CYCLE` |
| `kind` | `structural` |
| `severity` | `error` |
| `scope.components` | `orders_services` · `orders_services_pricing` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The sub-package `depot.orders.services.pricing` must not form an import cycle with its parent package `depot.orders.services`. The only permitted direction is parent -> child: `depot.orders.services` wires the pricing sub-package in. A module of `depot.orders.services.pricing` must never import a module of `depot.orders.services`; such a back edge from a child onto its own parent package closes a cycle. Report the finding as a dependency edge: `subject.from` is the importing component, `subject.to` the imported one — the edge that closes the cycle.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **kein Kandidat** |
| **(b) Kandidat(en)** | — |
| **(c) Begründung des Vorbefunds** | Der Sachverhalt des Statements ist die **Rückkante eines Unterpakets auf sein Elternpaket** — `depot.orders.services.pricing` → `depot.orders.services`. Kein Vorschlag nennt dieses Unterpaket, und **keiner spricht über das Verhältnis eines Pakets zu seinem eigenen Elternpaket**; die Vorschläge behandeln die services-Pakete durchweg als ungeteilte Einheiten. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | spricht über die drei services-Pakete als Ganzes, ohne deren innere Paketstruktur |
| `P-02` | desgleichen, und zieht die Grenze zwischen zwei Kontexten |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | Importverbot gegen `logging` |
| `P-05` | Stil und Dokumentation |
| `P-06` | Duplikation |
| `P-07` | repository-Pakete |
| `P-08` | Definitionsort der Protokolle |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | verlangt logische Modul- und Paketorganisation, aber ohne Richtung und ohne Zyklusbegriff, und mit Scope nur auf den billing-Komponenten |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | Schichtgrenze zwischen api und den darunterliegenden Schichten |
| `P-15` | Fehlerbehandlung |
| `P-16` | mappers-Pakete |
| `P-17` | Duplikationsverbot für zwei benannte Funktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | nein |
| **durch welche(s) P-xx** | — |
| **Begründung des Autors** | Kein Vorschlag regelt die Rückkante pricing → orders.services oder die Zyklusfreiheit zwischen Eltern- und Unterpaket. Die allgemeine Portbindung aus P-01/P-11 formuliert diese Paketbeziehung nicht; eine mittelbare Einschränkung einzelner Serviceabhängigkeiten reicht dafür nicht aus. |

---

### R-PORT-1

| Feld | Wert |
|---|---|
| Soll-ID | `R-PORT-1` |
| `category` | `ABSENCE_REQUIRED` |
| `kind` | `semantic` |
| `severity` | `error` |
| `scope.components` | `identity_services` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The token service `depot.identity.services.token_service` must obtain its token signing through the port `depot.core.ports.TokenSigner` and through nothing else. Its public method `TokenService.issue` is required to carry that port type in its public signature. If the reference is absent there, the required port reference is missing and the module reaches its signing capability past the port. Report `depot.core.ports.TokenSigner` as `subject.offending_type`, under that exact name.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **Kandidat vorhanden** |
| **(b) Kandidat(en)** | `P-01 + P-11` |
| **(c) Begründung des Vorbefunds** | Der Vorschlag bindet die Serviceklassen der drei Kontexte an die Schnittstellen aus `depot.core.ports` und verbietet ihnen den Griff auf Konkreta — **derselbe Sachverhalt**, den R-PORT-1 für `depot.identity.services.token_service` und den Port `TokenSigner` fordert. Der Vorschlag fasst **breiter** (alle drei Servicepakete, alle Ports) und formuliert ein **Abhängigkeitsverbot**, wo das Statement die **Anwesenheit** des Porttyps in einer benannten öffentlichen Signatur verlangt; die Signaturebene fehlt ihm. **Zu prüfen.** |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-02` | Kontextgrenze ohne Portbezug |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | Importverbot gegen `logging`, Scope billing |
| `P-05` | Stil und Dokumentation, Scope billing |
| `P-06` | Duplikation, Scope billing |
| `P-07` | Repositorygrenze ohne Portbezug — nennt `depot.core.ports` nur als erlaubte Importquelle |
| `P-08` | verlangt, dass Protokolle in `depot.core.ports` definiert werden, sagt aber nichts darüber, welcher Service welchen Port zu führen hat |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | Organisation, Scope billing |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | betrifft die Konstruktorabhängigkeiten der api-Routen, nicht die Signatur eines Services |
| `P-15` | Fehlerbehandlung, Scope billing |
| `P-16` | Importverbot für mappers |
| `P-17` | nennt Signaturen, aber die zweier Fehler-Hilfsfunktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | ja |
| **durch welche(s) P-xx** | `P-01` + `P-11` |
| **Begründung des Autors** | Teilweise sinngemäße Entsprechung nach dem Maßstab aus 1b: Die Bindung der Serviceabhängigkeiten an depot.core.ports trifft auch die geforderte Nutzung von TokenSigner statt konkreter Anbieter. P-01/P-11 gelten breiter für alle drei Servicepakete und verbieten zusätzlich konkrete Repositories. Sie verlangen jedoch weder diesen bestimmten Port noch dessen Anwesenheit in der öffentlichen Signatur von TokenService.issue. Das Ja gilt der gemeinsamen Portbindung, nicht der vollständigen ABSENCE_REQUIRED-Forderung. |

---

### R-PORT-2

| Feld | Wert |
|---|---|
| Soll-ID | `R-PORT-2` |
| `category` | `ABSENCE_REQUIRED` |
| `kind` | `semantic` |
| `severity` | `error` |
| `scope.components` | `orders_services` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The catalogue service `depot.orders.services.catalog_service` must obtain carrier tariffs through the port `depot.core.ports.RateProvider` and through nothing else. Its public method `CatalogService.quote_cents` is required to carry that port type in its public signature. If the reference is absent there, the required port reference is missing and the module reaches the tariff source past the port. Report `depot.core.ports.RateProvider` as `subject.offending_type`, under that exact name.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **Kandidat vorhanden** |
| **(b) Kandidat(en)** | `P-01 + P-11` |
| **(c) Begründung des Vorbefunds** | Wie bei R-PORT-1: der Vorschlag bindet die Serviceklassen — darunter die des Pakets `depot.orders.services` — an die Schnittstellen aus `depot.core.ports`, und das ist **derselbe Sachverhalt**, den R-PORT-2 für `depot.orders.services.catalog_service` und den Port `RateProvider` fordert. **Breiter** in der Reichweite (alle Servicepakete, alle Ports), und als Abhängigkeitsverbot statt als Anwesenheitsforderung in der Signatur `CatalogService.quote_cents`. **Zu prüfen.** |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-02` | nennt `depot.orders.services` im Scope, spricht aber über die Grenze zum billing-Kontext, nicht über einen Port |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | Importverbot gegen `logging`, Scope billing |
| `P-05` | Stil und Dokumentation, Scope billing |
| `P-06` | Duplikation, Scope billing |
| `P-07` | nennt `depot.core.ports` nur als erlaubte Importquelle der repository-Schicht |
| `P-08` | Definitionsort der Protokolle, keine Zuweisung Port ↔ Service |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | Organisation, Scope billing |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | Konstruktorabhängigkeiten der api-Routen |
| `P-15` | Fehlerbehandlung, Scope billing |
| `P-16` | Importverbot für mappers |
| `P-17` | nennt Signaturen, aber die zweier Fehler-Hilfsfunktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | ja |
| **durch welche(s) P-xx** | `P-01` + `P-11` |
| **Begründung des Autors** | Teilweise sinngemäße Entsprechung nach dem Maßstab aus 1b: Die Bindung der Serviceabhängigkeiten an depot.core.ports trifft auch die geforderte Nutzung von RateProvider statt konkreter Anbieter. P-01/P-11 gelten breiter für alle drei Servicepakete und verbieten zusätzlich konkrete Repositories. Sie verlangen jedoch weder diesen bestimmten Port noch dessen Anwesenheit in der öffentlichen Signatur von CatalogService.quote_cents. Das Ja gilt der gemeinsamen Portbindung, nicht der vollständigen ABSENCE_REQUIRED-Forderung. |

---

### R-PORT-3

| Feld | Wert |
|---|---|
| Soll-ID | `R-PORT-3` |
| `category` | `ABSENCE_REQUIRED` |
| `kind` | `semantic` |
| `severity` | `error` |
| `scope.components` | `orders_services` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The refund service `depot.orders.services.refund_service` must reach the payment provider through the port `depot.core.ports.PaymentGateway` and through nothing else. Its public method `RefundService.refund` is required to carry that port type in its public signature. If the reference is absent there, the required port reference is missing and the module reaches the payment provider past the port. Report `depot.core.ports.PaymentGateway` as `subject.offending_type`, under that exact name.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **Kandidat vorhanden** |
| **(b) Kandidat(en)** | `P-01 + P-11` |
| **(c) Begründung des Vorbefunds** | Wie bei R-PORT-1 und R-PORT-2: die Bindung der Serviceklassen an `depot.core.ports` ist **derselbe Sachverhalt**, den R-PORT-3 für `depot.orders.services.refund_service` und den Port `PaymentGateway` fordert; `depot.orders.services` liegt im Scope des Vorschlags. **Breiter** in der Reichweite und ohne die Signaturebene, die das Statement mit `RefundService.refund` benennt. **Zu prüfen.** |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-02` | nennt `depot.orders.services` im Scope, spricht aber über die Kontextgrenze, nicht über einen Port |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | Importverbot gegen `logging`, Scope billing |
| `P-05` | Stil und Dokumentation, Scope billing |
| `P-06` | Duplikation, Scope billing |
| `P-07` | `depot.core.ports` nur als erlaubte Importquelle der repository-Schicht |
| `P-08` | Definitionsort der Protokolle |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | Organisation, Scope billing |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | Konstruktorabhängigkeiten der api-Routen |
| `P-15` | Fehlerbehandlung, Scope billing |
| `P-16` | Importverbot für mappers |
| `P-17` | Signaturen zweier Fehler-Hilfsfunktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | ja |
| **durch welche(s) P-xx** | `P-01` + `P-11` |
| **Begründung des Autors** | Teilweise sinngemäße Entsprechung nach dem Maßstab aus 1b: Die Bindung der Serviceabhängigkeiten an depot.core.ports trifft auch die geforderte Nutzung von PaymentGateway statt konkreter Anbieter. P-01/P-11 gelten breiter für alle drei Servicepakete und verbieten zusätzlich konkrete Repositories. Sie verlangen jedoch weder diesen bestimmten Port noch dessen Anwesenheit in der öffentlichen Signatur von RefundService.refund. Das Ja gilt der gemeinsamen Portbindung, nicht der vollständigen ABSENCE_REQUIRED-Forderung. |

---

### R-PORT-4

| Feld | Wert |
|---|---|
| Soll-ID | `R-PORT-4` |
| `category` | `ABSENCE_REQUIRED` |
| `kind` | `semantic` |
| `severity` | `error` |
| `scope.components` | `billing_services` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The ledger service `depot.billing.services.ledger_service` must obtain the booking day through the port `depot.core.ports.Clock` and through nothing else. Its public method `LedgerService.post_invoice` is required to carry that port type in its public signature. If the reference is absent there, the required port reference is missing and the module takes its booking day from somewhere past the port. Report `depot.core.ports.Clock` as `subject.offending_type`, under that exact name. (`LedgerService.post_settlement` deliberately takes the value date as `day: str` and is not covered by this rule.)
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **Kandidat vorhanden** |
| **(b) Kandidat(en)** | `P-01 + P-11` |
| **(c) Begründung des Vorbefunds** | Wie bei den drei übrigen Portregeln: die Bindung der Serviceklassen an `depot.core.ports` ist **derselbe Sachverhalt**, den R-PORT-4 für `depot.billing.services.ledger_service` und den Port `Clock` fordert; `depot.billing.services` liegt im Scope des Vorschlags. **Breiter** in der Reichweite, ohne die Signaturebene `LedgerService.post_invoice` und ohne die Ausnahme, die das Statement für `post_settlement` ausdrücklich macht. **Zu prüfen.** |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-02` | nennt `depot.billing.services` im Scope, spricht aber über die Kontextgrenze, nicht über einen Port |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | Scope sind die billing-Komponenten, der Sachverhalt ist aber der Import von `logging`, nicht die Portbindung |
| `P-05` | Scope billing, Sachverhalt Stil und Dokumentation |
| `P-06` | Scope billing, Sachverhalt Duplikation |
| `P-07` | `depot.core.ports` nur als erlaubte Importquelle |
| `P-08` | Definitionsort der Protokolle |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | Scope billing, Sachverhalt Organisation |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | Konstruktorabhängigkeiten der api-Routen |
| `P-15` | Scope billing, Sachverhalt Fehlerbehandlung |
| `P-16` | Importverbot für mappers |
| `P-17` | Signaturen zweier Fehler-Hilfsfunktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | ja |
| **durch welche(s) P-xx** | `P-01` + `P-11` |
| **Begründung des Autors** | Teilweise sinngemäße Entsprechung nach dem Maßstab aus 1b: Die Bindung der Serviceabhängigkeiten an depot.core.ports trifft auch die geforderte Nutzung von Clock statt konkreter Anbieter. P-01/P-11 gelten breiter für alle drei Servicepakete und verbieten zusätzlich konkrete Repositories. Sie verlangen jedoch weder diesen bestimmten Port noch dessen Anwesenheit in der öffentlichen Signatur von LedgerService.post_invoice. Das Ja gilt der gemeinsamen Portbindung, nicht der vollständigen ABSENCE_REQUIRED-Forderung. Die besondere Abgrenzung zu post_settlement fehlt ebenfalls. |

---

### R-FRAMEWORK-1

| Feld | Wert |
|---|---|
| Soll-ID | `R-FRAMEWORK-1` |
| `category` | `FORBIDDEN_SIGNATURE_TYPE` |
| `kind` | `semantic` |
| `severity` | `error` |
| `scope.components` | `identity_models` · `orders_models` · `billing_models` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
Modules of the `models` layer (`depot.<context>.models`) MAY import the persistence framework `sqlalchemy.orm` — the object-relational mapping is this layer's own tool, and the import as such is expressly allowed and is never a violation. What is forbidden is the persistence/session type in a public signature: no parameter annotation and no return annotation of a public function or of a public method may name `sqlalchemy.orm.Session` or any other type of the `sqlalchemy.orm` namespace. Public signatures of the `models` layer carry builtins and project-local types only. Explicitly permitted and NOT a violation: `sqlalchemy.orm.Mapped[...]` in a class attribute annotation and calls to `sqlalchemy.orm.mapped_column(...)` in the class body — that is the declarative mapping itself, not a leak into the API of the module. Report the persistence type that appears in the signature as `subject.offending_type`, verbatim as it is written there.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **kein Kandidat** |
| **(b) Kandidat(en)** | — |
| **(c) Begründung des Vorbefunds** | Der Sachverhalt des Statements ist der **Persistenztyp aus `sqlalchemy.orm` in einer öffentlichen Signatur der models-Schicht** — samt der Unterscheidung, die das Statement trägt: der **Import ist erlaubt**, der **Typ in der Signatur nicht**. Weder `sqlalchemy` noch ein Persistenzframework noch die Signaturen der models-Schicht kommen in **einem** der 16 Vorschläge vor. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | Portbindung der Services, nicht die models-Schicht |
| `P-02` | Kontextgrenze |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | verbietet den direkten Import einer Fremdbibliothek (`logging`) — dieselbe Bauart, aber ein anderes Modul, und ein Importverbot, das die Signaturebene gerade nicht trifft |
| `P-05` | Stil und Dokumentation der billing-Komponenten, ohne Typaussage |
| `P-06` | Duplikation |
| `P-07` | spricht über Importe **von** Models durch die repository-Schicht, nicht über Typen **in** deren Signaturen |
| `P-08` | Definitionsort der Protokolle |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | Organisation der billing-Komponenten, ohne Typaussage |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | Schichtgrenze der api-Routen |
| `P-15` | Fehlerbehandlung |
| `P-16` | Importverbot für mappers |
| `P-17` | nennt Signaturen, aber die von `status_for` und `error_body` |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | nein |
| **durch welche(s) P-xx** | — |
| **Begründung des Autors** | Kein Vorschlag verbietet Persistenztypen in öffentlichen Signaturen der models-Schicht. P-04 betrifft logging-Importe, P-07 die Herkunft importierter Models und P-17 zwei Fehlerfunktionen. Keiner trifft die zentrale Unterscheidung zwischen erlaubtem Frameworkimport und verbotenem Signaturtyp. |

---

### R-PLACE-1

| Feld | Wert |
|---|---|
| Soll-ID | `R-PLACE-1` |
| `category` | `STRUCTURAL_PLACEMENT` |
| `kind` | `semantic` |
| `severity` | `error` |
| `scope.components` | `identity_models` · `identity_repository` · `orders_models` · `orders_repository` · `billing_models` · `billing_repository` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
Module names in this repository imply where the module belongs. Clause 1 — a module whose name ends in `_repo`, `_query` or `_index` belongs in the `repository` package of its bounded context, that is in `depot.<context>.repository`. Clause 2 — a module whose name ends in `_models` belongs in the `models` package of its bounded context, that is in `depot.<context>.models`. Both clauses read in ONE direction only: the name implies the location, never the other way round. They say nothing about how a module that already lies in one of those packages has to be named, and they do not apply to the package modules `depot.<context>.models` and `depot.<context>.repository` themselves, whose last name segment is `models` respectively `repository` and not `_models` respectively `_repo`/`_query`/`_index`. A module that carries one of these suffixes and lies anywhere else breaks the naming convention of its target layer. Report the full dotted module path of the misnamed-for-its-place module as `subject.offending_type`.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **kein Kandidat** |
| **(b) Kandidat(en)** | — |
| **(c) Begründung des Vorbefunds** | Der Sachverhalt des Statements ist die **Ortsimplikation eines Modulnamens**: ein Modul auf `_repo`, `_query` oder `_index` gehört ins repository-Paket seines Kontexts, eines auf `_models` ins models-Paket. **Kein** Vorschlag leitet aus einem Modulnamen ab, in welchem Paket das Modul zu liegen hat, und die vier Suffixe kommen in keinem der 16 vor. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | Portbindung der Services |
| `P-02` | Kontextgrenze |
| `P-03` | spricht über einen Namen, aber über den **Funktions**namen `error_body` und dessen Definitionsort, nicht über Modulnamen und deren Paket |
| `P-04` | Importverbot gegen `logging` |
| `P-05` | Stil und Dokumentation |
| `P-06` | Duplikation |
| `P-07` | betrifft die repository-Pakete, aber deren Importe, nicht die Platzierung von Modulen nach ihrem Namen |
| `P-08` | Definitionsort der Protokolle, an einem Paket festgemacht, nicht an einem Namensmerkmal des Moduls |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | desgleichen für `status_for` |
| `P-12` | verlangt logische Modul- und Paketorganisation, benennt aber kein Namensmerkmal, aus dem sich ein Ort ergäbe, und liegt mit seinem Scope nur auf den billing-Komponenten |
| `P-13` | dasselbe für Fehlerklassen |
| `P-14` | Schichtgrenze der api-Routen |
| `P-15` | Fehlerbehandlung |
| `P-16` | Importverbot für mappers |
| `P-17` | Duplikationsverbot für zwei benannte Funktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | nein |
| **durch welche(s) P-xx** | — |
| **Begründung des Autors** | Kein Vorschlag fordert die Zuordnung von Modulsuffixen zu repository oder models im jeweiligen Kontext. Allgemeine Namenskonventionen (P-05), Paketorganisation (P-12) und Definitionsorte bestimmter Klassen oder Funktionen enthalten diese Ortsimplikation nicht. |

---

### R-SIG-1

| Feld | Wert |
|---|---|
| Soll-ID | `R-SIG-1` |
| `category` | `API_CONTRACT` |
| `kind` | `semantic` |
| `severity` | `error` |
| `scope.components` | `identity_repository` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The class `SessionRepository` in `depot.identity.repository.session_repo` implements the port `depot.core.ports.SessionStore` and must carry its method exactly with the target signature `def touch(self, session_id: str, ttl_seconds: int) -> bool:`. Every parameter name, every parameter type and the return type are part of the contract: neither `session_id: str` nor `ttl_seconds: int` nor the return type `bool` may deviate, and no parameter may be added or dropped. A deviating signature breaks the API contract even when the module still imports and type-checks. Report the symbol `SessionRepository.touch` as `subject.offending_type`.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **kein Kandidat** |
| **(b) Kandidat(en)** | — |
| **(c) Begründung des Vorbefunds** | Der Sachverhalt des Statements ist die **zeichengenaue Vertragstreue einer Portimplementierung**: `SessionRepository.touch` muss die Zielsignatur des Ports `depot.core.ports.SessionStore` exakt tragen, Parameternamen und Rückgabetyp eingeschlossen. **Kein** Vorschlag verlangt, dass eine Implementierung eine vorgegebene Zielsignatur einhält; weder das Symbol noch der Port kommt in einem der 16 vor. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | verlangt die Bindung an Ports, nicht die Form der implementierenden Methode |
| `P-02` | Kontextgrenze |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | Importverbot gegen `logging` |
| `P-05` | Stil und Dokumentation |
| `P-06` | Duplikation |
| `P-07` | Importgrenze der repository-Schicht, keine Signaturaussage |
| `P-08` | regelt, **wo** Protokolle definiert werden; über die Signatur ihrer Implementierungen sagt es nichts |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | Organisation |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | Importgrenze der api-Schicht |
| `P-15` | Fehlerbehandlung |
| `P-16` | Importverbot für mappers |
| `P-17` | führt Signaturen mit, aber als Duplikationsverbot für `status_for` und `error_body`, nicht als Vertragstreue gegenüber einem Port |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | nein |
| **durch welche(s) P-xx** | — |
| **Begründung des Autors** | Kein Vorschlag fordert die Zielsignatur von SessionRepository.touch oder allgemein die Signaturtreue von Portimplementierungen. P-01/P-11 regeln Serviceabhängigkeiten, P-08 den Definitionsort von Protokollen und P-17 die Zentralisierung anderer Funktionen. |

---

### R-SIG-2

| Feld | Wert |
|---|---|
| Soll-ID | `R-SIG-2` |
| `category` | `API_CONTRACT` |
| `kind` | `semantic` |
| `severity` | `error` |
| `scope.components` | `orders_repository` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The class `OrderQuery` in `depot.orders.repository.order_query` implements the port `depot.core.ports.DiscountCatalog` and must carry its method exactly with the target signature `def percent_for(self, code: str, subtotal_cents: int) -> int:`. Every parameter name, every parameter type and the return type are part of the contract: neither `code: str` nor `subtotal_cents: int` nor the return type `int` may deviate, and no parameter may be added or dropped. A deviating signature breaks the API contract even when the module still imports and type-checks. Report the symbol `OrderQuery.percent_for` as `subject.offending_type`.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **kein Kandidat** |
| **(b) Kandidat(en)** | — |
| **(c) Begründung des Vorbefunds** | Wie bei R-SIG-1: der Sachverhalt ist die zeichengenaue Zielsignatur von `OrderQuery.percent_for` gegenüber dem Port `depot.core.ports.DiscountCatalog`. **Kein** Vorschlag der 16 fordert Signaturtreue einer Portimplementierung, und weder das Symbol noch der Port wird genannt. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | Portbindung der Services, nicht der repository-Schicht |
| `P-02` | Kontextgrenze |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | Importverbot gegen `logging` |
| `P-05` | Stil und Dokumentation |
| `P-06` | Duplikation |
| `P-07` | spricht über `depot.orders.repository`, aber über dessen Importe, nicht über eine Methodensignatur |
| `P-08` | Definitionsort der Protokolle, nicht die Form ihrer Implementierungen |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | Organisation |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | Importgrenze der api-Schicht |
| `P-15` | Fehlerbehandlung |
| `P-16` | Importverbot für mappers |
| `P-17` | nennt zwei Signaturen, aber als Duplikationsverbot für Fehler-Hilfsfunktionen |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | nein |
| **durch welche(s) P-xx** | — |
| **Begründung des Autors** | Kein Vorschlag fordert den Signaturvertrag von OrderQuery.percent_for gegenüber DiscountCatalog. P-07 betrifft zwar die Repository-Schicht, aber ausschließlich Importgrenzen; daraus folgen keine verbindlichen Parameternamen, Parametertypen oder Rückgabetypen. |

---

### R-SIG-3

| Feld | Wert |
|---|---|
| Soll-ID | `R-SIG-3` |
| `category` | `API_CONTRACT` |
| `kind` | `semantic` |
| `severity` | `error` |
| `scope.components` | `billing_repository` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The class `InvoiceQuery` in `depot.billing.repository.invoice_query` implements the port `depot.core.ports.PaymentLedger` and must carry its method exactly with the target signature `def settled_cents(self, invoice_number: str) -> int:`. Every parameter name, every parameter type and the return type are part of the contract: neither `invoice_number: str` nor the return type `int` may deviate, and no parameter may be added or dropped. A deviating signature breaks the API contract even when the module still imports and type-checks. Report the symbol `InvoiceQuery.settled_cents` as `subject.offending_type`.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **kein Kandidat** |
| **(b) Kandidat(en)** | — |
| **(c) Begründung des Vorbefunds** | Wie bei R-SIG-1 und R-SIG-2: der Sachverhalt ist die zeichengenaue Zielsignatur von `InvoiceQuery.settled_cents` gegenüber dem Port `depot.core.ports.PaymentLedger`. **Kein** Vorschlag der 16 fordert Signaturtreue einer Portimplementierung. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | Portbindung der Services |
| `P-02` | Kontextgrenze |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | Scope billing, aber Importverbot gegen `logging` |
| `P-05` | Scope billing, aber Stil und Dokumentation |
| `P-06` | Scope billing, aber Duplikation |
| `P-07` | spricht über `depot.billing.repository`, aber über dessen Importe, nicht über eine Methodensignatur |
| `P-08` | Definitionsort der Protokolle |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | Scope billing, aber Organisation |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | Importgrenze der api-Schicht |
| `P-15` | Scope billing, aber Fehlerbehandlung |
| `P-16` | Importverbot für mappers |
| `P-17` | nennt zwei Signaturen, aber als Duplikationsverbot |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | nein |
| **durch welche(s) P-xx** | — |
| **Begründung des Autors** | Kein Vorschlag fordert den Signaturvertrag von InvoiceQuery.settled_cents gegenüber PaymentLedger. Die Vorschläge zu billing sowie P-07 enthalten keine entsprechende Schnittstellenforderung; die Signaturen in P-17 gehören zu anderen Funktionen und dienen deren Identifikation beim Duplikationsverbot. |

---

### R-SIG-4

| Feld | Wert |
|---|---|
| Soll-ID | `R-SIG-4` |
| `category` | `API_CONTRACT` |
| `kind` | `semantic` |
| `severity` | `error` |
| `scope.components` | `orders_mappers` |

**`statement`** — zeichengleich wie in `architecture-rules.yaml`:

~~~~text
The public function `to_payload` in `depot.orders.mappers.order_line_mapper` must carry exactly the target signature `def to_payload(line: depot.orders.models.order_line_models.OrderLine) -> dict[str, object]:`. The parameter name, the parameter type and the return type are part of the contract: neither `line: depot.orders.models.order_line_models.OrderLine` nor the return type `dict[str, object]` may deviate, and no parameter may be added or dropped. This module implements no Protocol; this rule wording is the whole contract. A deviating signature breaks it even when the module still imports and type-checks. Report the symbol `to_payload` as `subject.offending_type`.
~~~~

#### VORBEFUND (MASCHINELL, kein Ergebnis)

> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und bindet den Autor nicht.

| Feld | Eintrag |
|---|---|
| **(a) VORBEFUND (maschinell)** | **kein Kandidat** |
| **(b) Kandidat(en)** | — |
| **(c) Begründung des Vorbefunds** | Der Sachverhalt des Statements ist die zeichengenaue Zielsignatur der öffentlichen Funktion `to_payload` in `depot.orders.mappers.order_line_mapper` — hier ohne Port, weil das Statement selbst der ganze Vertrag ist. **Kein** Vorschlag der 16 spricht über die Signatur einer Mapperfunktion. |

**(d) PRÜFSPUR — geprüft und verworfen:**

| Etikett | Grund des Ausschlusses |
|---|---|
| `P-01 + P-11` | Portbindung der Services |
| `P-02` | Kontextgrenze |
| `P-03` | Definitionsort von `error_body` |
| `P-04` | Importverbot gegen `logging` |
| `P-05` | Stil und Dokumentation |
| `P-06` | Duplikation |
| `P-07` | Importgrenze der repository-Schicht |
| `P-08` | Definitionsort der Protokolle; das Statement nennt ausdrücklich keines |
| `P-09` | Definitionsort der Fehler-Mappingfunktionen |
| `P-10` | Definitionsort von `status_for` |
| `P-12` | Organisation |
| `P-13` | Definitionsort der Fehlerklassen |
| `P-14` | nennt die mappers als zulässige Abhängigkeit der api-Routen, ohne Aussage über deren Schnittstelle |
| `P-15` | Fehlerbehandlung |
| `P-16` | spricht über die mappers-Pakete, aber über deren Fehlerimporte, nicht über die Signatur einer Mapperfunktion |
| `P-17` | nennt zwei Signaturen, aber die von `status_for` und `error_body` |

#### ENTSCHEIDUNG DES AUTORS

> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor **bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt **nicht als entschieden**.

| Feld | Eintrag |
|---|---|
| **ENTSCHEIDUNG (ja \| nein)** | nein |
| **durch welche(s) P-xx** | — |
| **Begründung des Autors** | Kein Vorschlag verlangt die Zielsignatur von to_payload oder eine entsprechende Vertragsbindung von Mapperfunktionen. P-14 erlaubt Mapperabhängigkeiten, P-16 beschränkt Fehlerimporte; beides sagt nichts über Parameter und Rückgabetyp dieser Funktion aus. |

---

## 4. Summenfeld — leer

**n von 16 = ___**

| Größe | Eintrag |
|---|---|
| **n von 16** | ___ |

**Die Zahl wird erst nach dem Ausfüllen der Matrix gebildet** — aus den Feldern **ENTSCHEIDUNG DES AUTORS**, nicht aus den Vorbefunden und nicht daneben. In **S13** wird sie **mechanisch nachgerechnet**: gezählt werden die Abschnitte mit „ja“, der Nenner bleibt 16.

**Die Vorbefunde ergeben diese Zahl NICHT.** Sie sind Nachschlagearbeit, nicht Entscheidung; das Blatt weist deshalb **keine Summe** über sie aus. Wer die Kandidatenzeilen zählt, hat **nicht** „n von 16“ gebildet, sondern eine **Arbeitsangabe** über den Stand der Nachschlagearbeit.

**Beim Eintragen gilt die Einhegung aus 1d:** die Zahl heisst „n Statements haben eine Entsprechung unter den Vorschlägen“ — nie „das Modell hat n von 16 Regeln gefunden“.

