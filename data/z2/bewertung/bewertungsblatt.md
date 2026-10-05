# Z2 — Bewertungsblatt (VERBLINDET)
**Auftrag S10 · Repo `masterarbeit` · Werkzeug `tools/prepare_z2_review.py`**
**Protokollstand:** `z2_protokoll_regelableitung.md`, SHA256 `862fdc3b7cfb264482db155575437edb25b1b436f92b5444b2137f1e332d9dde`. Alle Entscheidungsregeln und Wertelisten unten sind **wörtlich aus §6 dieses Standes ausgeschnitten**, nicht nacherzählt.
**Seed der Reihenfolge:** `random.Random(20260903)` — im Schlüssel wiederholt.
**Einträge:** 17, mechanisch verschieden nach der Definition unten.

---

## 0. Was dieses Blatt ist — und was der Bewerter zu tun hat

Nach Protokoll **§2** ist die **Einheit der Auswertung der einzelne Regelvorschlag (nach Dedup, §6 Z2-R)**. Nach **§6** werden alle Vorschläge aller Läufe gepoolt, **anonymisiert (ohne Modell-/Bedingungs-Label)** und in **randomisierter Reihenfolge von EINEM Bewerter** bewertet; die Zuordnung wird **erst nach Abschluss der Bewertung aufgelöst**.

**AUFLAGE — der Zuordnungsschlüssel `zuordnungsschluessel.json` liegt im selben Verzeichnis und ist VOR ABSCHLUSS DER BEWERTUNG NICHT ZU ÖFFNEN.** Er trägt Bedingung, Slot, Position, ursprüngliche `id` und Vielfachheit je Eintrag. Wer ihn vorher öffnet, hebt die Verblindung auf, gegen die Erwartung **E2** gerichtet ist (§6, T-Z2-7).

**AUSZUFÜLLEN sind vier Dimensionen je Eintrag:** `kind`, **Z2-P**, **Z2-G**, **Z2-Z**. Sie sind hier **leer** und werden von Hand gesetzt.

**NICHT auszufüllen:** **Z2-W** und die **Granularitätszählung** stehen je Eintrag bereits da — sie sind **maschinell** aus der archivierten `validation.json` des jeweiligen Laufs **übernommen** und **keine Bewerterleistung**. Die Granularitätszählung ist ausdrücklich eine **BEOBACHTUNG, kein Kriterium**: sie steht in keiner Entscheidungsregel des §6 und geht in keine der vier Dimensionen ein.

**GRENZFÄLLE:** Jeder Grenzfall wird nach **§6 Punkt 1** und **§7 Punkt 7** in die **Grenzfall-Tabelle (Anhang B des Protokolls)** eingetragen — mit **Vorschlag-ID, Kriterium, Entscheidung und Begründung** — und im Befund **vollständig ausgewiesen, nicht nur gezählt**. Die Form der Tabelle steht unten in Abschnitt 6. Als Vorschlag-ID dient das Etikett `P-xx` dieses Blattes.

---

## 1. Die mechanische Zusammenführung, die diesem Blatt zugrunde liegt

Zwei Vorschläge sind MECHANISCH IDENTISCH, wenn das Tupel (category, statement, severity, sorted(scope.components)) nach Unicode-NFC und Abschneiden führender und schliessender Leerzeichen ZEICHENGLEICH ist. `id` geht NICHT ein -- sie ist je Lauf frei gewählt. Keine weitere Normalisierung: keine Kleinschreibung, keine Interpunktions-, Zahlen- oder Synonymbehandlung, kein Zusammenziehen innerer Leerzeichen. MECHANISCHE IDENTITÄT IST NUR EINE TEILMENGE DESSEN, WAS Z2-R VERLANGT (§6: Kategorie, Scope und Kernaussage; Umformulierungen zählen als ein Vorschlag) -- die inhaltliche Zusammenführung steht aus und ist Sache des Bewerters.

**Folge für die Bewertung:** Zwei Einträge, die **dasselbe sagen**, aber **anders formuliert** sind, stehen hier als **ZWEI Einträge**. Die inhaltliche Zusammenführung nach **Z2-R** ist **Sache des Bewerters** und wird in der Spalte **„identisch mit P-xx“** je Eintrag festgehalten.

---

## 2. Z2-R — der Wortlaut, nach dem zusammenzuführen ist (§6, wörtlich)

**Z2-R Redundanz/Dedup** ~~(K5)~~ — **eine Regel, kein Bewertungskriterium.** Zwei
Vorschläge sind Duplikate, wenn Kategorie,
Scope und Kernaussage übereinstimmen (Umformulierungen zählen als ein
Vorschlag). Dedup passiert pro Lauf UND über Läufe hinweg getrennt
ausgewiesen: pro-Lauf-Dedup für die Mengenangaben, laufübergreifende
Wiederkehr als Stabilitätsmaß (§7).

---

## 3. Die vier auszufüllenden Dimensionen (§6, wörtlich)

### 3.1 `kind` — `structural` | `semantic`

**`kind` (`structural` | `semantic`) — NEU als Dimension** *(01.09.2026, S1-A1)*: `kind`
wird **BEWERTET, nicht vorgegeben**. Die **Achse, auf der E2 liegt**, wird damit
**gemessen statt vom Schema gesetzt** (§5.2 (ii); `rules.ts:56`). Die Zuweisung ist
zugleich die eine Feldeinfügung der Umschreibung in §7 Punkt 8.

### 3.2 Z2-P — Prüfbarkeit

> Die **alte Fassung ist überholt** (02.09.2026, S1-A1c) und steht im Protokoll durchgestrichen; **gültig ist die folgende**.

**Z2-P Prüfbarkeit — NEUE FASSUNG** *(02.09.2026, Auftrag S1-A1c)*. Entscheidungsregel:
*Ein Vorschlag ist prüfbar, wenn seine Verletzung **allein aus den IMPORTKANTEN DES
IST-MODELLS und den SIGNATUREN der Faktenbasis** entscheidbar wäre.*

- **Positivbeispiele:** „`identity_api` darf `identity_repository` nicht importieren"
  (**Importkante des Ist-Modells**, dort modulscharf geführt); „Funktionen in
  `depot.*.models` dürfen keinen Request-Parameter annehmen" (**Signatur** sichtbar);
  „Öffentliche Methoden in `*_repository` geben keine ORM-Entität zurück"
  (**Signatur** sichtbar).
- **Negativbeispiele, unverändert:** „Repository-Funktionen dürfen keinen globalen State
  mutieren" (nur im **Funktionskörper** sichtbar); „Module sollen lose gekoppelt
  sein" (nicht operationalisiert).
- **NEU hinzugekommenes Negativbeispiel — und es ist genau das alte erste
  Positivbeispiel:** „domain darf flask nicht importieren". `flask` ist ein
  **EXTERNER** Import; **externe Ziele haben keinen Container und stehen im Export nicht**.
  Unter der neuen Evidenzbasis ist ein solcher Vorschlag **nicht entscheidbar** — **er
  wechselt mit Stufe 0b die Seite**, und das ist der **gemessene Preis**, kein Versehen.

**BEFUND, der die Änderung auslöst:** in **S2c-2** (Commit **`89b70e6`**) wurden **Stufe 0**
(Docstrings, leere `__init__.py`) **und Stufe 0b** (Importblöcke) **gezogen**; die abgelegte
Eingabe `data/z2/eingaben/input_facts.json` trägt **52 Records OHNE `imports`-Blöcke und MIT
Signaturen**.

**PREIS — GEMESSEN statt angenommen** (vollständige Tabelle in **§3a-2**, Nachtrag
02.09.2026): das Testrepo verwendet **ausschliesslich `import a.b.c`** — **Aliasnamen 0**,
**`from X import Y` mit `names[]` 0**, **relative Importe 0**. Von **90 Importfakten** haben
**81 ein Ziel in `depot.*`**, und das **Ist-Modell führt genau 81 Relationen mit 81
eindeutigen `(from,to)`-Paaren** — **dieselbe Menge, eins zu eins**. **Verloren gehen
ausschliesslich die NEUN externen Importe:** **acht `sqlalchemy.orm`** und **einer
`typing`** (in `depot.core.ports`).

**KONSEQUENZ — ausdrücklich, und sie bindet die Bewertung:** **ein Vorschlag, dessen
Prüfbarkeit von einem EXTERNEN Import abhängt, ist aus der Eingabe nicht entscheidbar.**
**Framework-Typen bleiben über die SIGNATUREN sichtbar, nicht mehr über eine Importliste.**
Bewertet wird ein solcher Vorschlag unter **Z2-P als nicht entscheidbar, MIT VERMERK DER
URSACHE** — **er ist damit kein Modellfehler, sondern eine Folge der registrierten
Kürzung.** **Der Vermerk ist Pflicht**, damit der Befund nicht als Fähigkeitsdefizit des
Modells gelesen wird.

**ZEITLICHE EINORDNUNG, mitzuregistrieren:** **die Kürzung ist VORAB registriert** — Stufe
0b steht seit dem **01.09.2026 (S1-A1)** in §3b — und **aus einem Fensterbefund gezogen**
(**38 748 > 32 768**), **nicht nach Kenntnis der Ergebnisse**: zum Zeitpunkt des Ziehens
existiert **kein einziger Z2-Lauf**. **Nachgezogen in §10, T-Z2-6 und T-Z2-9.**

### 3.3 Z2-G — Gehalt, DREIWERTIG plus „unklar“

> **Werteliste:** **Spiegelung** · **negierte Spiegelung** · **normativ** — plus **„unklar“** nach der Grenzfall-Regel am Ende dieses Abschnitts. **Alle drei Werte werden getrennt berichtet.** „unklar“ wird **nicht stillschweigend einer Seite zugeschlagen**.

**Z2-G Gehalt** ~~(K3)~~ — das Kernkriterium, **drei Werte**:

| Wert | Entscheidungsregel | Beispiele |
|---|---|---|
| **Spiegelung** (extensional, positiv) | Zählt **vorhandene Kanten als erlaubt** auf. | (a) „`identity_services` darf `identity_repository` importieren" — die Kante steht in der Whitelist und ist realisiert. (b) „Erlaubt sind genau die folgenden Komponentenkanten: …" mit Aufzählung des Ist-Graphen. |
| **Negierte Spiegelung** (extensional, komplementär) | Verbietet eine im Ist **ABWESENDE** Kante, **ohne über die beobachtete Extension hinauszugehen**. | (a) „`identity_api` darf `identity_repository` nicht importieren" — die Kante ist im Ist abwesend (`<k>_api → <k>_repository`, Komponentenschnitt: „abwesend"). (b) „`billing_repository` darf `billing_services` nicht importieren" — ebenfalls im Ist abwesend. |
| **Normativ** (intensional) | **Quantifiziert über nicht beobachtete Module**, ODER verbietet eine im Ist **REALISIERTE** Konstellation, ODER fordert eine Eigenschaft, **die nicht aus dem Importgraphen folgt**. | (a) „**Kein** Modul unterhalb `depot.*.models` darf ein Framework-Paket importieren" — quantifiziert über Module, die es im Ist noch nicht gibt. (b) „Öffentliche Methoden in `*_repository` geben keine ORM-Entität zurück" — eine **Signatur**-Eigenschaft, aus dem Importgraphen nicht ableitbar. |

**GRUND, hier zu registrieren: die Baseline ist GESÄTTIGT.** `00_stand_und_entscheidungen.md`
§7: **39 von 39 Whitelist-Relationen realisiert**, **0 unbenutzt**, **0 Kanten außerhalb
der Whitelist** (81 Modulkanten), **0 Zyklen** auf Komponenten- und Modulebene. Damit ist
die **Closed-World-Negation informationsgleich mit der Spiegelung**, und die **alte
Zweiwertigkeit klassifizierte DASSELBE Objekt in beide Klassen**: die Klammer „verbietet
nur, was ohnehin nicht vorkommt" (= **deskriptiv**) gegen den Hauptsatz „verbietet eine
im Ist nicht realisierte, aber realisierbare Konstellation" (= **normativ**) — **das
Positivbeispiel „api darf infrastructure nicht direkt importieren" fiel unter beide.**

**ZUSATZ: die Sättigung ist im Ist-Modell KONSTRUKTIV.** Der Export führt in
`perspectives.relations` **genau die BEOBACHTETEN Importkanten, dedupliziert**
(`containerImportRelations`, `codeModelToIlograph.ts:575-589`). **Die Spiegelung liegt
dem Modell damit als Datenstruktur vor** — das ist der Grund, warum die Achse
**dreiwertig sein muss**.

**Alle drei Werte werden getrennt berichtet.**

- Grenzfall-Regel: Ist die Äquivalenz zur Whitelist nicht eindeutig
  entscheidbar, kommt der Vorschlag in die Grenzfall-Tabelle (Pflichtfeld:
  Begründung) und zählt in der Hauptauswertung als „unklar" (eigene Spalte,
  wird nicht stillschweigend einer Seite zugeschlagen).

### 3.4 Z2-Z — Zuordnung zum Abweichungstyp (Ebene 1)

> **Werteliste, sechs Kategorien plus zwei getrennte Auffangwerte:** `FORBIDDEN_RELATION` · `CYCLE` · `ABSENCE_REQUIRED` · `FORBIDDEN_SIGNATURE_TYPE` · `STRUCTURAL_PLACEMENT` · `API_CONTRACT` — dazu **„sonstige“** (Auffangkategorie **innerhalb** der Kodierung) und **„keiner der sechs“** (begründete Feststellung, dass die **Kodierung den Vorschlag nicht trägt**). Die beiden sind **getrennt auszuweisen**.

**Z2-Z Zuordnung zum Abweichungstyp (Ebene 1)** ~~(K4)~~ — `FORBIDDEN_RELATION` / `CYCLE` / `ABSENCE_REQUIRED` /
`FORBIDDEN_SIGNATURE_TYPE` / `STRUCTURAL_PLACEMENT` / `API_CONTRACT` / „sonstige", nach
den Kategoriedefinitionen des Hauptprotokolls (§3 dort, Ebene 1). Die Ebene-2-Szenarien
werden nur vermerkt, wo ein Vorschlag eindeutig auf eines von ihnen zielt; tragend für
die Auswertung ist Ebene 1. „Sonstige" werden
qualitativ beschrieben und, falls sich wiederkehrende Klassen zeigen,
induktiv gruppiert — ein Befund, kein Abfall.

> **Ergänzt 02.09.2026 (Auftrag S1-A1b) — zusätzlicher Wert „keiner der sechs".** Die
> Eingabe trägt **zwölf Vererbungskanten** (`extends`, §3a-1 Nachtrag 02.09.2026). Ein
> daraus abgeleiteter Vorschlag — etwa ein **Vererbungsverbot über Komponentengrenzen** —
> entspricht **keiner** der sechs Kategorien. Z2-Z erhält dafür den Wert **„keiner der
> sechs"**, **getrennt von „sonstige" auszuweisen**: „sonstige" ist die
> **Auffangkategorie INNERHALB** der Kodierung, „keiner der sechs" die **begründete
> Feststellung, dass die Kodierung den Vorschlag nicht trägt** (Begründung in §7 Punkt 3).
> **Kein Alttext entfällt:** „sonstige" bleibt unverändert die Auffangkategorie.

---

## 4. Z2-W und Granularität — maschinell, nicht auszufüllen (§6, wörtlich)

**Z2-W Wohlgeformtheit** ~~(K1)~~ — maschinell, **zweistufig nach §5.3**:
Schemakonformität unter `strict: true` ist **keine Messgröße**, gemessen wird die dort
registrierte binäre Liste. ~~Nicht wohlgeformte Vorschläge werden
für K2–K4 trotzdem manuell bewertet, sofern menschenlesbar (getrennt
ausgewiesen), damit Formatfehler nicht als Fähigkeitsdefizit zählen.~~ — *Wortlaut
nachgezogen 01.09.2026:* nicht wohlgeformte Vorschläge werden für **Z2-P, Z2-G, Z2-Z**
trotzdem manuell bewertet, sofern menschenlesbar (getrennt ausgewiesen), damit
Formatfehler nicht als Fähigkeitsdefizit zählen.

> **Herkunft der Werte in diesem Blatt:** je Eintrag aus der archivierten `validation.json` des Laufs **übernommen**, in dem der Vorschlag steht (Prüfliste **§5.3 Punkt 2**). **Maschinell entstanden, keine Bewerterleistung.** Bei mechanisch identischen Vorschlägen stimmten die Werte aller Herkünfte überein; das Werkzeug bricht ab, wenn sie es nicht tun.

> **Granularitätszählung:** wie viele Einträge in `scope.components` sich gegen das Ist-Modell als **package**, **module** oder **artefact** auflösen und wie viele **unresolved** bleiben. **BEOBACHTUNG, KEIN KRITERIUM.**

---

## 5. Die Einträge

**Reihenfolge randomisiert** (Seed oben) — sie trägt **keine Information** über Bedingung, Modell oder Lauf. **Nicht enthalten sind** Bedingung, Modellname, Slot, die ursprüngliche `id`, die Zahl der Läufe je Eintrag, die Position im Array und Zeitstempel. Sie stehen **ausschliesslich im Zuordnungsschlüssel**.

---

### P-01

| Feld | Wert |
|---|---|
| `category` | `dependency-inversion` |
| `severity` | `error` |
| `scope.components` | `depot.billing.services` · `depot.identity.services` · `depot.orders.services` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Service classes must have their dependencies limited to interfaces defined in depot.core.ports; they must not directly instantiate or depend on concrete adapter or repository classes.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 3 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `structural` — Import-/Abhängigkeitsregel über Modulkanten |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — die verletzenden Kanten stehen im Ist-Modell (services → repository/adapters); „instantiate" impliziert einen Import |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — verbietet REALISIERTE Kanten (u. a. `invoice_service → invoice_repo`, `invoice_service → core.adapters.storage`) |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | `FORBIDDEN_RELATION` — verbotene Importbeziehung |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | nein |
| Bemerkung | P-11 ist nach Z2-R mit diesem Eintrag identisch (dort vermerkt und in Abschnitt 6 begründet). |

---

### P-02

| Feld | Wert |
|---|---|
| `category` | `dependency-control` |
| `severity` | `error` |
| `scope.components` | `depot.billing.services` · `depot.orders.services` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Services in depot.billing.services and depot.orders.services must not depend on services in each other's packages. They may only depend on services in depot.identity.services and depot.core.services (if any) and on repositories and ports.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 2 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `structural` — Import-/Abhängigkeitsregel über Paketgrenzen |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — alle genannten Ziele sind interne Kanten des Ist-Modells; `depot.core.services` existiert nicht, die Klausel ist leer erfüllbar |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | unklar — Grenzfall, siehe Abschnitt 6: die Erlaubnislisten-Lesart verbietet realisierte Kanten, die enge Service-zu-Service-Lesart nur abwesende |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | `FORBIDDEN_RELATION` — zielt eindeutig auf Ebene 2 `INDEPENDENCE` (wechselseitige Unabhängigkeit billing ↔ orders) |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | Realisiert und je nach Lesart verboten: `order_service`/`invoice_service → core.adapters.storage`, `orders.services.pricing.engine → core.errors`. |

---

### P-03

| Feld | Wert |
|---|---|
| `category` | `error-handling-consistency` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api.schemas` · `depot.identity.api.schemas` · `depot.orders.api.schemas` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
These modules must not define a function named error_body; they must import it from a shared location.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 0 · module 3 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `semantic` — Regel über Symboldefinitionen, nicht über den Importgraphen |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — Funktionsdefinitionen (Name je Modul) stehen in der Faktenbasis |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — verbietet Realisiertes: alle drei Schemas-Module definieren `error_body` |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | sonstige — Symbolzentralisierung/Duplikatverbot (Grenzfall, Abschnitt 6) |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | Familie mit P-09/P-10/P-17; nach Z2-R nicht identisch (Kategorie, Scope bzw. Symbol verschieden). |

---

### P-04

| Feld | Wert |
|---|---|
| `category` | `dependency-management` |
| `severity` | `warning` |
| `scope.components` | `depot.billing.api` · `depot.billing.services` · `depot.billing.repository` · `depot.billing.models` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Classes and functions within the billing components must not directly import the standard logging module. Instead, they should obtain a logger from a shared logging helper module.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 4 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `structural` — Importregel |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | nicht entscheidbar — URSACHE (Pflichtvermerk §6): `logging` ist ein EXTERNES Importziel; externe Ziele haben nach der Stufe-0b-Kürzung keine Kante im Ist-Modell und keinen Signaturniederschlag. Folge der registrierten Kürzung, kein Modellfehler |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — fordert eine Eigenschaft, die nicht aus dem Importgraphen folgt (externer Import in der Eingabe unsichtbar); der geforderte Logging-Helper existiert nicht |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | `FORBIDDEN_RELATION` — verbotene Importbeziehung, Ziel jedoch extern (Grenzfall, Abschnitt 6) |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | — |

---

### P-05

| Feld | Wert |
|---|---|
| `category` | `code-quality` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api` · `depot.billing.services` · `depot.billing.repository` · `depot.billing.models` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
All classes and functions within the billing components should be well-documented and follow a consistent coding style. This includes using docstrings to describe the purpose and behavior of each function, and following a consistent naming convention for variables and functions.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 4 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `semantic` — Dokumentations-/Stileigenschaft |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | nicht prüfbar — nicht operationalisiert („consistent style"); Docstrings sind mit Stufe 0 aus der Eingabe gezogen |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — fordert Eigenschaften, die nicht aus dem Importgraphen folgen |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | sonstige — Dokumentations-/Stilregel, kein Abweichungstyp der Kodierung |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | nein |
| Bemerkung | — |

---

### P-06

| Feld | Wert |
|---|---|
| `category` | `code-reusability` |
| `severity` | `warning` |
| `scope.components` | `depot.billing.api` · `depot.billing.services` · `depot.billing.repository` · `depot.billing.models` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Classes and functions within the billing components should not duplicate logic found in other modules. Instead, they should reuse existing functions or classes where possible.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 4 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `semantic` — Eigenschaft der Implementierung, nicht der Struktur |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | nicht prüfbar — Logikduplikation ist nur im Funktionskörper sichtbar, nicht in Kanten oder Signaturen |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — fordert eine Eigenschaft, die nicht aus dem Importgraphen folgt |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | sonstige — Wiederverwendungs-/Duplikationsregel auf Logikebene |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | nein |
| Bemerkung | — |

---

### P-07

| Feld | Wert |
|---|---|
| `category` | `data-access-layer` |
| `severity` | `error` |
| `scope.components` | `depot.billing.repository` · `depot.identity.repository` · `depot.orders.repository` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
A repository module may only import models from its own package (e.g., depot.billing.models for billing.repository) and from depot.core.ports. It must not import models from any other package.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 3 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `structural` — modulscharfe Importregel |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — alle Repository-Importkanten stehen modulscharf im Ist-Modell |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | Spiegelung — geschlossene Erlaubnisliste, deckungsgleich mit den realisierten Kanten: alle sieben Repository-Module importieren genau eigene models + `core.ports` (Grenzfall, Abschnitt 6) |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | `FORBIDDEN_RELATION` — verbotene Importbeziehung (repo → fremde models) |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | — |

---

### P-08

| Feld | Wert |
|---|---|
| `category` | `interface-segregation` |
| `severity` | `error` |
| `scope.components` | `depot` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
All protocols (classes inheriting from typing.Protocol) must be defined in the depot.core.ports module. No other module may define a class that inherits from typing.Protocol.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 1 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `semantic` — Regel über Klassendefinition/Vererbung, nicht über Importkanten |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — Grenzfall, Abschnitt 6: entscheidbar über das `bases`-Feld der Faktenbasis (`typing.Protocol` steht dort wörtlich); kein externer Importfakt nötig |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — Vererbungs-/Definitionsort-Eigenschaft, folgt nicht aus dem Importgraphen; im Ist erfüllt (alle 11 Protocols liegen in `core.ports`) |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | keiner der sechs — vererbungsbasierte Definitionsortsregel (Grenzfall, Abschnitt 6) |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | — |

---

### P-09

| Feld | Wert |
|---|---|
| `category` | `error-handling-centralization` |
| `severity` | `warning` |
| `scope.components` | `depot.billing.api.routes` · `depot.identity.api.routes` · `depot.orders.api.routes` · `depot.billing.api.schemas` · `depot.identity.api.schemas` · `depot.orders.api.schemas` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Functions that map DepotError to HTTP status codes or error response bodies must be defined only in depot.core.errors; all other modules must obtain these functions by importing from that module.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 0 · module 6 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `semantic` — Regel über Symboldefinitionen und deren Bedeutung |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — Grenzfall, Abschnitt 6: „maps DepotError to HTTP status codes" ist eine Deutung, entschieden über die sichtbaren Signaturen (`DepotError -> int` bzw. `-> dict[str, str]`) |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — verbietet Realisiertes: `status_for`/`error_body` sind in routes/schemas definiert, `core.errors` führt keine solchen Funktionen |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | sonstige — Symbolzentralisierung, wie P-03 (Grenzfall, Abschnitt 6) |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | Familie mit P-03/P-10/P-17; nach Z2-R nicht identisch (Kategorie und Scope verschieden, deckt beide Funktionsfamilien zugleich). |

---

### P-10

| Feld | Wert |
|---|---|
| `category` | `error-handling-consistency` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api.routes` · `depot.identity.api.routes` · `depot.orders.api.routes` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
These modules must not define a function named status_for; they must obtain the error-to-status mapping from a shared location (e.g., depot.core.errors).
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 0 · module 3 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `semantic` — Regel über Symboldefinitionen |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — Funktionsdefinitionen stehen in der Faktenbasis |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — verbietet Realisiertes: alle drei Routes-Module definieren `status_for` |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | sonstige — Symbolzentralisierung, wie P-03 (Grenzfall, Abschnitt 6) |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | Familie mit P-03/P-09/P-17; nach Z2-R nicht identisch (anderes Symbol und anderer Scope als P-03). |

---

### P-11

| Feld | Wert |
|---|---|
| `category` | `dependency-inversion` |
| `severity` | `warning` |
| `scope.components` | `depot.billing.services` · `depot.identity.services` · `depot.orders.services` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Service classes in these packages must not import or depend on concrete adapter classes; they may only depend on protocols defined in depot.core.ports or other abstract interfaces.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 3 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `structural` — Import-/Abhängigkeitsregel über Modulkanten |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — wie P-01: verletzende Kanten (services → repository/adapters) im Ist-Modell sichtbar |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — verbietet REALISIERTE Kanten: „may only depend on protocols … or other abstract interfaces" schliesst die realisierten Repository- und Adapter-Kanten aus |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | `FORBIDDEN_RELATION` — verbotene Importbeziehung |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | P-01 |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | Duplikat von P-01 nach Z2-R (Abschnitt 6); `severity` weicht ab (warning statt error), geht aber nicht in Z2-R ein. |

---

### P-12

| Feld | Wert |
|---|---|
| `category` | `code-organization` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api` · `depot.billing.services` · `depot.billing.repository` · `depot.billing.models` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
All classes and functions within the billing components should be organized into logical modules and packages. This includes grouping related classes and functions together and ensuring that each module has a single responsibility.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 4 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `semantic` — Organisations-/Verantwortlichkeitseigenschaft |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | nicht prüfbar — „logical modules", „single responsibility" nicht operationalisiert |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — fordert Eigenschaften, die nicht aus dem Importgraphen folgen |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | sonstige — Organisations-/SRP-Regel, kein Abweichungstyp der Kodierung |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | nein |
| Bemerkung | — |

---

### P-13

| Feld | Wert |
|---|---|
| `category` | `error-handling` |
| `severity` | `error` |
| `scope.components` | `depot` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Only the depot.core.errors module may define error classes (classes inheriting from Exception). All other modules in the codebase must not define any error classes.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 1 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `semantic` — Regel über Klassendefinition/Vererbung |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — Grenzfall, Abschnitt 6, wie P-08: `bases`-Feld der Faktenbasis zeigt die Exception-Vererbung |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — Vererbungs-/Definitionsort-Eigenschaft, folgt nicht aus dem Importgraphen; im Ist erfüllt (alle Fehlerklassen liegen in `core.errors`) |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | keiner der sechs — vererbungsbasierte Definitionsortsregel, wie P-08 (Grenzfall, Abschnitt 6) |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | Kein Duplikat von P-08 nach Z2-R: andere Kategorie und andere Kernaussage (Fehlerklassen statt Protocols). |

---

### P-14

| Feld | Wert |
|---|---|
| `category` | `layered-architecture` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api.routes` · `depot.identity.api.routes` · `depot.orders.api.routes` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
API route classes shall receive only service-layer dependencies (and optionally mappers) in their constructors and must not import repository, model, or adapter modules directly.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 0 · module 3 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `structural` — Schichtenregel über Importe; die Konstruktorklausel ist signaturseitig (siehe Bemerkung) |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — Importkanten UND Konstruktorsignaturen stehen beide in der Evidenzbasis (routes-`__init__` nehmen sichtbar nur Service-Typen) |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | unklar — Grenzfall, Abschnitt 6: Importverbots-Teil rein extensional (Kanten im Ist abwesend), Konstruktorklausel Signatureigenschaft (intensional) |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | `FORBIDDEN_RELATION` — verbotene Importbeziehungen routes → repository/models/adapters |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | Doppelnatur Kante + Signatur; kein einzelnes Ebene-2-Szenario eindeutig angezielt (deckt Skip- und Back-Richtung zugleich). |

---

### P-15

| Feld | Wert |
|---|---|
| `category` | `error-handling` |
| `severity` | `error` |
| `scope.components` | `depot.billing.api` · `depot.billing.services` · `depot.billing.repository` · `depot.billing.models` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
All error handling within the billing components should be consistent and follow a common pattern. This includes using a shared error handling module and ensuring that all error messages are localized and user-friendly.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 4 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `semantic` — Muster-/Meldungseigenschaft |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | nicht prüfbar — „common pattern", Lokalisierung und Nutzerfreundlichkeit von Meldungen liegen nicht in der Evidenzbasis |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — fordert Eigenschaften, die nicht aus dem Importgraphen folgen |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | sonstige — vage Konsistenzregel zur Fehlerbehandlung |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | nein |
| Bemerkung | Berührt die Fehlerbehandlungs-Familie (P-03/P-09/P-10), nach Z2-R nicht identisch: Musterforderung statt Symbolverbot, anderer Scope. |

---

### P-16

| Feld | Wert |
|---|---|
| `category` | `mapper-purity` |
| `severity` | `warning` |
| `scope.components` | `depot.billing.mappers` · `depot.identity.mappers` · `depot.orders.mappers` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
Modules in these packages must not import depot.core.errors or any other error-related modules; they should perform only data transformation without error handling.
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 3 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `structural` — Importregel |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — die Kanten mappers → `core.errors` stehen im Ist-Modell; der „without error handling"-Teil läge im Rumpf, die Verletzung ist aber schon über die Kante entscheidbar |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — verbietet REALISIERTE Kanten: alle sechs Mapper-Module importieren `core.errors` |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | `FORBIDDEN_RELATION` — verbotene Importbeziehung |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | nein |
| Bemerkung | — |

---

### P-17

| Feld | Wert |
|---|---|
| `category` | `duplication` |
| `severity` | `warning` |
| `scope.components` | `depot` |

**`statement`** — zeichengleich wie im Rohartefakt:

~~~~text
The functions `status_for` (signature: (error: depot.core.errors.DepotError) -> int) and `error_body` (signature: (error: depot.core.errors.DepotError) -> dict[str, str]) must not be defined in more than one module. They should be defined in a single shared utility module (e.g., depot.core.utils).
~~~~

**Maschinell übernommen (nicht auszufüllen):**

| Maschinelle Angabe | Wert |
|---|---|
| **Z2-W** wohlgeformt | **ja** |
| Z2-W Einzelprüfungen (§5.3 Punkt 2) | components_aufloesbar=ja, statement_nicht_leer=ja, statement_keine_wiederholung=ja, id_eindeutig=ja, category_nicht_leer=ja |
| Z2-W Befunde | — |
| Granularität (BEOBACHTUNG, kein Kriterium) | package 1 · module 0 · artefact 0 · unresolved 0 |

**Auszufüllen — vier Dimensionen aus §6:**

| Dimension | Werteliste | Eintrag |
|---|---|---|
| `kind` | `structural` \| `semantic` | `semantic` — Regel über Symboldefinitionen |
| **Z2-P** Prüfbarkeit | prüfbar \| nicht prüfbar — bei Abhängigkeit von einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** (§6, Pflicht) | prüfbar — beide Funktionsnamen samt Signaturen stehen in der Faktenbasis; Mehrfachdefinition ist abzählbar |
| **Z2-G** Gehalt | Spiegelung \| negierte Spiegelung \| normativ \| unklar | normativ — verbietet Realisiertes: `status_for` und `error_body` sind je dreifach definiert; das genannte `depot.core.utils` existiert nicht |
| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \| `CYCLE` \| `ABSENCE_REQUIRED` \| `FORBIDDEN_SIGNATURE_TYPE` \| `STRUCTURAL_PLACEMENT` \| `API_CONTRACT` \| sonstige \| keiner der sechs | sonstige — Duplikat-/Zentralisierungsregel für Symbole, wie P-03 (Grenzfall, Abschnitt 6) |

**Dedup nach Z2-R (inhaltlich, vom Bewerter):**

| Feld | Eintrag |
|---|---|
| identisch mit P-xx | — |
| Grenzfall nach §6 Punkt 1? | ja |
| Bemerkung | Familie mit P-03/P-09/P-10; nach Z2-R nicht identisch (Kategorie `duplication`, Scope `depot`, beide Symbole zugleich). |

---

## 6. Grenzfall-Tabelle — Form nach Anhang B des Protokolls (wörtlich)

## Anhang B — Grenzfall-Tabelle (während der Bewertung zu führen)

> **Diese Tabelle wird im Befund VOLLSTÄNDIG ausgewiesen, nicht nur gezählt**
> (§6 Punkt 1, §7 Punkt 7; Amendment 31.08.2026). Seit dem Wegfall des
> Zweitbewerter-Triggers ist sie der Ersatz für ein Übereinstimmungsmaß — kein
> Äquivalent, sondern die Offenlegung des Ermessens (Threat **T-Z2-7**).

| Vorschlag-ID | Kriterium | Entscheidung | Begründung |
|---|---|---|---|
| P-02 | Z2-G | unklar | Die Erlaubnislisten-Lesart („may only depend on …") verbietet realisierte Kanten (`invoice_service`/`order_service → core.adapters.storage`, `pricing.engine → core.errors`), die enge Service-zu-Service-Lesart nur im Ist abwesende. Äquivalenz zur Whitelist damit nicht eindeutig entscheidbar — nach der Grenzfall-Regel „unklar". |
| P-03 | Z2-Z | sonstige | Verbot der Mehrfachdefinition eines Funktionssymbols. `STRUCTURAL_PLACEMENT`/`INCORRECT_LOCATION` ist im Hauptprotokoll modulbezogen und trägt eine funktionsbezogene Zentralisierungsregel nicht; kodierbar bleibt sie als eigener Typ → Auffangkategorie. |
| P-04 | Z2-Z | `FORBIDDEN_RELATION` | Der Typ (verbotene Importbeziehung) passt, das Ziel (`logging`) ist aber extern; der Injektionsplan kennt nur repo-interne Kanten. Zuordnung zum Typ, mit Vermerk des externen Ziels. |
| P-07 | Z2-G | Spiegelung | Geschlossene Erlaubnisliste, deckungsgleich mit den realisierten Kanten (Spiegelungs-Beispiel (b)); der Verbotsschwanz trifft unter der gesättigten Baseline nur Abwesendes — kein Überschreiten der beobachteten Extension, die positive Listenform gibt den Ausschlag. |
| P-08 | Z2-P | prüfbar | Entscheidend ist das `bases`-Feld der Faktenbasis, in dem `typing.Protocol` wörtlich steht — kein externer Importfakt nötig. Grenzfall, weil `bases` keine „Signatur" im engen Wortsinn der Z2-P-Regel ist; die extends-Fakten sind aber als Eingabebestandteil registriert (§3a-1). |
| P-08 | Z2-Z | keiner der sechs | Aus Vererbungsinformation abgeleitete Definitionsortsregel — der in §6 (S1-A1b) vorgesehene Fall; nicht `STRUCTURAL_PLACEMENT`, das modulbezogene Ortsregeln meint. |
| P-09 | Z2-P | prüfbar | „Functions that map DepotError to HTTP status codes" verlangt eine Deutung; entschieden über die sichtbaren Signaturen (`(error: DepotError) -> int` bzw. `-> dict[str, str]`), die die gemeinten Funktionen eindeutig ausweisen. |
| P-09 | Z2-Z | sonstige | Wie P-03: funktionsbezogene Zentralisierungsregel, von der Kodierung nicht als eigener Typ getragen. |
| P-10 | Z2-Z | sonstige | Wie P-03. |
| P-11 | Z2-R | identisch mit P-01 | Kategorie (`dependency-inversion`) und Scope (drei services-Pakete) identisch; Kernaussage — Services hängen nur von Abstraktionen in `core.ports` ab, nicht von konkreten Klassen — deckungsgleich: „may only depend on protocols … or other abstract interfaces" schliesst Repositories ebenso aus wie P-01s explizite Aufzählung. Umformulierung im Sinn von Z2-R; `severity` ist kein Z2-R-Kriterium. |
| P-13 | Z2-P | prüfbar | Wie P-08: `bases`-Feld zeigt die Exception-Vererbung. |
| P-13 | Z2-Z | keiner der sechs | Wie P-08: vererbungsbasierte Definitionsortsregel. |
| P-14 | Z2-G | unklar | Der Importverbots-Teil verbietet nur im Ist abwesende Kanten (extensional); die Konstruktorklausel („receive only service-layer dependencies") ist eine Signatureigenschaft (intensional). Nicht eindeutig einer Seite zuordenbar — nach der Grenzfall-Regel „unklar". |
| P-17 | Z2-Z | sonstige | Wie P-03, auf beide Symbole zugleich bezogen. |

> **Für dieses Blatt:** als **Vorschlag-ID** dient das Etikett `P-xx`. Die ausgefüllte Tabelle gehört **vollständig in den Befund** (§7 Punkt 7), nicht in die Ablage.

---

## 7. Grenze der Verblindung — nach T-Z2-7 zu vermerken

Die Verblindung entfernt jede **Kennung** und jede **Kennzahl**, aus der die Bedingung ableitbar wäre — insbesondere die **Zahl der Läufe je Eintrag**: sie steht **nur im Zuordnungsschlüssel**, weil sie in einer der beiden Zellen mit der Bedingung zusammenfiele.

**Nicht heilbar, hier benannt:** **Stil und Länge der `statement`-Texte** können die **Modellklasse** dennoch erkennbar machen; ebenso die **Zuschnittsgewohnheit** der `scope.components`. Der Wortlaut der Vorschläge ist die **Messgrösse selbst** und darf nicht angetastet werden — die Verblindung ist deshalb **eine Verblindung gegen die Kennzeichnung, keine gegen den Text**. Das ist unter **T-Z2-7** zu führen: die vorab fixierten Entscheidungsregeln aus §6 und die vollständig ausgewiesene Grenzfall-Tabelle tragen die Kodierung, nicht die Undurchdringlichkeit der Darreichung.

---

## 8. Was dieses Blatt NICHT enthält

- **Keine Bewertung.** `kind`, Z2-P, Z2-G und Z2-Z sind **leer** — nicht vorgeschlagen, nicht angedeutet.
- **N₁ ist NICHT gezählt.** N₁ ist nach §7 Punkt 9 die **Pro-Lauf-Dedup des ersten Laufs** nach **Z2-R**; Z2-R ist inhaltlich und steht aus.
- **Kein Verdikt zu E1–E4**, keine Kennzahl, kein Anteil, kein Vergleich zwischen den Zellen.
- **Keine inhaltliche Zusammenführung** — nur die mechanische aus Abschnitt 1.
- **Keine Umformulierung**: `category`, `statement`, `severity` und `scope.components` stehen **zeichengleich** wie in `raw_response.json`.
