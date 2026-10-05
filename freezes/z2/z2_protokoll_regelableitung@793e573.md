# Z2-Protokoll — Explorative Studie zur LLM-basierten Regelableitung (UF2)

> **Status:** Entwurf zur Vorregistrierung. Eingefroren wird dieses Dokument
> (Commit-Hash) **vor** dem ersten Z2-LLM-Lauf. Änderungen danach nur über die
> Amendments-Tabelle (§11).
> **Zeitfenster:** nach dem Scope-Gate (31.08.) und nach dem Phase-04-Regel-Freeze;
> Ausführung geplant erste Septemberwoche.
> **Evidenzstufe:** explorativ-klassifizierend — bewusst schwächer als die
> kontrollierten Experimente Z1/Z3; diese Asymmetrie wird in der Arbeit explizit
> benannt (Methodikkapitel §4).
>
> ~~**Letzte Änderung: 31.08.2026 (Auftrag G1)** — Bewertung auf **Einzelbewerter,
> verblindet** umgestellt, Zweitbewerter-Trigger entfallen, neuer Threat **T-Z2-7**
> (§6, §7 Punkt 7, §10, Amendment §11). **Anhang A ist weiterhin ein Platzhalter; das
> Dokument ist nicht eingefroren.** Frist für Anhang A und Freeze: **07.09.2026**
> (`docs/planung/gate_notiz_2026-08-31.md` §5).~~ — überholt am 01.09.2026 (Auftrag
> S1-A1) durch den folgenden Vermerk; die Frist 07.09.2026 gilt unverändert weiter.
>
> ~~**Letzte Änderung: 01.09.2026 (Auftrag S1-A1)** — das Protokoll wird **vor dem ersten
> Z2-Lauf und vor seinem Freeze** auf den entschiedenen Zuschnitt gebracht. Gegenstände,
> vierzehn: **(1)** dieser Kopfvermerk · **(2)** **eigenes Ausgabeformat** statt des
> Checker-Regelschemas (§5) · **(3)** dessen Begründung — **Ankerwirkung, nicht
> Ausdrucksgrenze** (§5) · **(4)** neues, zweistufiges **Wohlgeformtheits-Orakel Z2-W**
> (§5, §6) · **(5)** neue Sekundärgröße **Ladbarkeit** (§7) · **(6)** **B2 entfällt**
> (§2, §3 Punkt 3, §7 Punkt 6, E3, T-Z2-5) · **(7)** Asymmetriesatz zum Kontextfenster
> (§3) · **(8)** **Umbenennung der Bewertungsdimensionen** K1–K5 → **Z2-W/Z2-P/Z2-G/
> Z2-Z/Z2-R**, `kind` neu als bewertete Dimension (§5, §6, §7, §10) · **(9)**
> **Gehaltsachse Z2-G dreiwertig** (§6, E1) · **(10)** **Eingaben** registriert — Erzeugung
> des Ist-Modells und der Faktenbasis (§2, §3a) · **(11)** **Größenregel** mit Schwelle
> und Wegeleiter, vor der Messung registriert (§3b) · **(12)** zwei neue Threats
> **T-Z2-8** und **T-Z2-9**, T-Z2-6 nachgezogen (§10) · **(13)** Nennerkorrektur in
> §7 Punkt 5 · **(14)** **Nachbesserungsregel** präzisiert, Auszählreihenfolge der Zelle
> (§4, §7). **Das Dokument ist zum Zeitpunkt dieser Änderung NICHT eingefroren** (Kopf
> oben: „Eingefroren wird dieses Dokument (Commit-Hash) **vor** dem ersten Z2-LLM-Lauf").
> **Anhang A ist weiterhin ein Platzhalter.** Frist für Anhang A und Freeze:
> **07.09.2026** (`docs/planung/gate_notiz_2026-08-31.md` §5).~~ — überholt am 02.09.2026
> (Auftrag S1-A1b) durch den folgenden Vermerk; **die vierzehn Gegenstände von S1-A1
> bleiben sachlich in Kraft**, überholt ist allein der Vermerk als *jüngster* Stand, und
> die Frist 07.09.2026 gilt unverändert weiter.
>
> ~~**Letzte Änderung: 02.09.2026 (Auftrag S1-A1b)** — **Nachtrag** aus dem Bericht zu
> **S2b-2** (Commit **`2b0ff04`**, Fundstelle der Befunde `data/z2/MANIFEST.md`),
> registriert **vor der Tokenmessung, vor dem ersten Z2-Lauf und vor dem Freeze dieses
> Dokuments**. Gegenstände, **drei**: **(1)** **§3b — das Messinstrument der Größenregel
> wird ausgewechselt.** `tools/z1_tokenizer.py` weist die abgelegte B1-Eingabe durch
> **seinen eigenen Wächter** ab; primäre Messgröße ist ab jetzt die **serverseitig
> gemeldete Prompt-Tokenzahl** aus einem als **INSTRUMENTENMESSUNG** registrierten
> Kaltlauf, mit **Messfenster und Kürzungsdetektor**, **additivem Rückfall**, dem
> **künftigen** Werkzeug `tools/z2_tokenizer.py` samt **zwei vorab registrierten Toren**
> und dem **Geltungsbereich der Schwelle** (§3b (a)–(e)). **(2)** **§3a-1/§3a-2 — die
> Evidenzbasis wird um ZWÖLF VERERBUNGSKANTEN erweitert**, die die abgelegte Eingabe
> trägt und die die Aufzählung in §3a-1 nicht nannte; **zwei Konsequenzen**, nachgezogen
> in **§6/§7 Punkt 3** (Z2-Z erhält den Wert „keiner der sechs") und **§10 (T-Z2-8)**.
> **(3)** **§3a-1 — Einordnung des Formbefunds** aus S2b-2, entschieden nach einer rein
> lesenden Vorablesung an `fixtures/rich_repo`: **FASSUNG A** — die Formidentität mit der
> Z1-Fixture ist **NICHT verletzt**, und **T-Z1-4 wird hierfür nicht in Anspruch
> genommen**. **`data/z2/` wird dabei NICHT angefasst** — die Eingabe bleibt bytegleich,
> ein Nachzug an `data/z2/MANIFEST.md` ist ein eigener Auftrag. **Das Dokument ist zum
> Zeitpunkt dieser Änderung NICHT eingefroren** (Kopf oben: „Eingefroren wird dieses
> Dokument (Commit-Hash) **vor** dem ersten Z2-LLM-Lauf"). **Anhang A ist weiterhin ein
> Platzhalter.** Frist für Anhang A und Freeze: **07.09.2026**
> (`docs/planung/gate_notiz_2026-08-31.md` §5).~~ — überholt am 02.09.2026 (Auftrag
> S1-A1c) durch den folgenden Vermerk; **die drei Gegenstände von S1-A1b bleiben sachlich
> in Kraft**, überholt ist allein der Vermerk als *jüngster* Stand, und die Frist
> 07.09.2026 gilt unverändert weiter.
>
> ~~**Letzte Änderung: 02.09.2026 (Auftrag S1-A1c)** — **DIES IST DAS LETZTE AMENDMENT VOR
> DEM FREEZE.** **Nachtrag** aus dem Lauf **S2c-2** (Commit **`89b70e6`**, Fundstelle der
> Befunde `data/z2/MANIFEST.md` und `data/z2/messungen/tokenmessung_2026-09-02.json`),
> registriert **vor dem Schreiben von Anhang A, vor dem ersten Z2-Lauf und vor dem Freeze
> dieses Dokuments**. Gegenstände, **drei**: **(1)** **§3b — der KÜRZUNGSDETEKTOR wird um
> zwei gleichrangige Kriterien ERWEITERT**: **(b2) MONOTONIE** und **(b3)
> HALBFENSTER-SIGNATUR `Fenster / 2 + 2`**. Der bisherige Fenstergleichheits-Wortlaut
> **bleibt gültig und bleibt stehen** — er ist **nicht falsch, sondern unzureichend**: in
> S2c-2 meldete der volle Prompt **16 386** Token, **weniger als die Faktenbasis allein**
> (**29 095**), und der registrierte Detektor **sprach nicht an**. **(2)** **§3a-2 und §6
> (Z2-P) — die EVIDENZBASIS wird nach dem Ziehen von Stufe 0b nachgezogen** auf
> „**Importkanten des Ist-Modells + Signaturen der Faktenbasis**"; der **gemessene Preis**
> sind **neun externe Importe**, Alttext **durchgestrichen sichtbar**; **T-Z2-6 und
> T-Z2-9** sind entsprechend ergänzt. **(3)** **§3b — das INSTRUKTIONSBUDGET R1 wird
> registriert und VERSCHÄRFT** auf eine **bindende Obergrenze von 1 000 Token** (bisher
> 1 200), samt **gezogenem Stand der Wegeleiter**, **Nachrichtenstruktur R3** und einer
> **zwingenden Auflage an S3**. **DIE VORREGISTRIERTE SCHWELLE VON 24 000 TOKEN BLEIBT
> UNVERÄNDERT** — sie wird **nicht angehoben**, **nicht durch ihre Begründung ersetzt** und
> **nicht mit einer Toleranz versehen**. **`data/z2/` ist dabei NICHT angefasst** — keine
> Eingabe, keine Messung, kein Manifest und kein Hash sind berührt. **Das Dokument ist zum
> Zeitpunkt dieser Änderung NICHT eingefroren** (Kopf oben: „Eingefroren wird dieses
> Dokument (Commit-Hash) **vor** dem ersten Z2-LLM-Lauf"). **Anhang A ist weiterhin ein
> Platzhalter; S3 schreibt ihn als nächstes, danach wird eingefroren.** Frist für Anhang A
> und Freeze: **07.09.2026** (`docs/planung/gate_notiz_2026-08-31.md` §5).~~ — überholt am
> 02.09.2026 (Auftrag S3) durch den folgenden Vermerk; **die drei Gegenstände von S1-A1c
> bleiben sachlich in Kraft**, und die Frist 07.09.2026 gilt unverändert weiter.
> **AUSDRÜCKLICH ÜBERHOLT ist darin der Satz „DIES IST DAS LETZTE AMENDMENT VOR DEM
> FREEZE":** S3 registriert **drei weitere Nachträge** (§5.1, §2, §10), die der Auftrag S3
> selbst verlangt. Der Satz war die **Absicht** zum Zeitpunkt seiner Niederschrift, nicht
> der eingetretene Verlauf; er bleibt **durchgestrichen sichtbar** stehen, weil auf ihm
> die Reihenfolge von S1-A1c registriert wurde.
>
> **Letzte Änderung: 02.09.2026 (Auftrag S3) — ANHANG A EINGESETZT UND GEMESSEN.**
> Gegenstände, **fünf**: **(1)** dieser Kopfvermerk. **(2)** **ANHANG A ist eingesetzt** —
> der Platzhalter ist eingelöst und bleibt durchgestrichen sichtbar stehen; der Anhang hat
> **sechs Teile A1–A6**: Zweck und Status · Nachrichtenstruktur nach **R3** · **der Prompt
> im Wortlaut** (englisch, R2) · **das gesendete JSON-Schema** · **Begründung der
> Auflösung** gegen die vier Auflagen aus §4 · **externe Gegenlesung**. **(3)** **§5.1 —
> `minItems: 1`** auf `rules` und auf `scope.components`, **additiv**, kein Alttext
> berührt; **§5.3 bleibt UNVERÄNDERT**, weil `minItems` providerseitig erzwungen und nach
> §5.3 **keine Messgröße** ist. **(4)** **§2 — die Evidenzbasis der Zeile B1 nachgezogen**
> auf **Importkanten des Ist-Modells (Block 1) + Signaturen der Faktenbasis (Block 2)**,
> Alttext **durchgestrichen sichtbar**. **(5)** **§10 — neuer Threat T-Z2-10** (Priming
> durch das Ausgabebeispiel). **DIE MESSUNG nach der Auflage aus §3b (f):** der **volle
> Prompt mit dem TATSÄCHLICHEN Instruktionstext** meldet **23 405 Token** (**M11**) bei
> einer Instruktion von **480 Token netto** (**M10**; Obergrenze **1 000** bindend,
> Zielgröße rund **700** — **beide gehalten**). **DIE VORREGISTRIERTE SCHWELLE VON 24 000
> TOKEN IST GEHALTEN**, mit **595 Token Reserve**; die **Generat-Reserve** bis zum Fenster
> beträgt **9 363 Token** (verlangt **≥ 8 000**). **Die Schwelle ist dabei NICHT bewegt,
> nicht angehoben und nicht durch ihre Begründung ersetzt worden**, und **Anhang A ist
> NICHT gekürzt worden** — er hält sie ungekürzt. **Der Satz „Anhang A ist weiterhin ein
> Platzhalter" ist damit überholt**; er steht in allen früheren Vermerken durchgestrichen
> sichtbar. **Das Dokument ist zum Zeitpunkt DIESER Änderung NOCH NICHT eingefroren** —
> der Freeze wird mit dem **unmittelbar folgenden Commit** vollzogen und **oben im
> Statusblock** vermerkt. Frist für Anhang A und Freeze: **07.09.2026**
> (`docs/planung/gate_notiz_2026-08-31.md` §5).

---

## 1. Untersuchungsfrage

**UF2 (kanonische Fassung):** Welche Klassen normativer Architekturregeln schlägt
ein LLM auf Basis eines automatisch abgeleiteten Ist-Modells vor, wie
unterscheiden sich die Vorschläge nach Wohlgeformtheit, Prüfbarkeit und
normativem Gehalt — und hängt dies von der Art der Ist-Ableitung
(deterministisch vs. LLM-basiert) ab?

Der letzte Halbsatz wird durch die sekundäre Kontrastbedingung B2 (§2)
explorativ adressiert; die Hauptantwort trägt Bedingung B1.

## 2. Design

| Element | Festlegung |
|---|---|
| **Bedingung B1 (primär)** | Input: Triton-Ist-Modell des Phase-04-Testrepos (Ilograph) + ~~AST-Fakten (Imports + Signaturen) — die **Bezeichnung bleibt unverändert richtig**~~, ihre **Erzeugung** ist seit 01.09.2026 (S1-A1) in **§3a** registriert. **NACHGEZOGEN 02.09.2026 (Auftrag S3):** die Evidenzbasis von B1 sind die **Importkanten des Ist-Modells (Block 1)** und die **Signaturen der Faktenbasis (Block 2)**. **Fundstellen:** **§3a-2** (Nachtrag 02.09.2026) und **§6 (Z2-P)** in der **Fassung vom 02.09.2026** (`bf6c6e0`). **Ursache: Stufe 0b der Wegeleiter ist GEZOGEN** (§3b) — die abgelegte Faktenbasis trägt **keine `imports`-Blöcke** mehr; der gemessene Preis sind **neun externe Importe**. Der Alttext bleibt **durchgestrichen sichtbar** stehen, weil auf ihm das Design registriert wurde; **mitgestrichen ist der Halbsatz zur Bezeichnung**, weil er **genau diesen** Alttext für unverändert richtig erklärte. Trägt die UF2-Antwort. Begründung der Primärstellung: der deterministische Ableitungsweg ist der skalierungszuverlässige (Befund 05) und damit der praxisrelevante Regelableitungs-Input. |
| **Bedingung B2** — ~~sekundär, explorativ~~ **ENTFÄLLT (01.09.2026, Auftrag S1-A1)** | ~~Input: LLM-extrahiertes Ist-Modell desselben Testrepos (Prompt v3) + identische AST-Fakten. Nur Kontrast: Verändert die Art des Ist-Modells die Vorschläge? Keine konfirmatorische Auswertung.~~ — **B2 entfällt.** Begründung, Charakter der Kürzung und der benannte Verlust stehen in **§3 Punkt 3**. |
| **Modelle** | K2 (`qwen2.5-coder:7b`, Ollama) und K3 (nemotron-120B, OpenRouter) — identisch zur Hauptevaluation, kein neuer Modell-Confounder. |
| **Läufe** | ~~3 pro Modell × Bedingung = **12 Läufe gesamt**.~~ — **mitkorrigiert am 01.09.2026 (S1-A1)** mit dem Wegfall von B2: 3 pro Modell × Bedingung, **zwei Zellen** (K2 × B1, K3 × B1) = **6 Läufe gesamt**. temperature=0, Seed fix, volles Contract-Logging (inkl. der in der Konsolidierung nachgerüsteten Felder seed/endpoint). |
| **Einheit der Auswertung** | der einzelne Regelvorschlag (nach Dedup, §6 **Z2-R**, bis 01.09.2026 „K5"). |

## 3. Eingaben & Freeze-Reihenfolge

1. Phase-04-Freeze ist Voraussetzung: Testrepo, Soll-Modell und
   `architecture-rules.yaml` sind committet und gehasht, **bevor** der erste
   Z2-Lauf startet.
2. Das LLM sieht die Regeldatei **niemals** — Input ist ausschließlich
   Ist-Modell + Fakten + Aufgabenbeschreibung. (Umkehrschutz zur
   T2-Reihenfolge des Hauptprotokolls: die Vorschläge dürfen das Soll nicht
   kontaminieren, das Soll nicht die Vorschläge.)
3. ~~Erzeugung des B2-Inputs wird dokumentiert: Prompt v3, Modell, Run-Verzeichnis,
   Auswahlregel = der erste valide Lauf (valid_final = true) des stärkeren
   Modells (K3); ist keiner valide, der erste valide K2-Lauf; ist keiner valide,
   entfällt B2 ersatzlos (kein Nachbessern) und der Ausfall wird als Befund
   berichtet.~~
   — **überholt am 01.09.2026 (Auftrag S1-A1): B2 entfällt.** *(Diese Regel wird
   anderswo als „§3.3" zitiert; gemeint ist stets **§3 Punkt 3**. Das Dokument führt
   keine numerierten Unterabschnitte in §3.)*

   **Die Fassung, eng:**

   > „Für `fixtures/rich_repo`, unter Prompt v3 und der registrierten
   > Ausführungsgeometrie, war kein gültiges LLM-Ist herstellbar — 12 von 12 Läufen
   > ohne gültige Ausgabe, GEMESSEN (Befund 07). Die Übertragung auf das Testrepo ist
   > ABGELEITET; es ist nicht ausgeschlossen, dass eine gültige Extraktion des
   > Testrepos möglich gewesen wäre."

   **Übertragbarkeit, nicht Analogie.** Der Ausfallmechanismus — falsche Granularität
   der Relationsendpunkte bei **dreimal ausgesprochener** Anweisung, abhängig von
   Prompt-Inhalt und Ausführungsgeometrie (Befund 07.2: `prompt.py:27`, `:28`,
   `:43-45`; sechs bytegleiche K2-Läufe, je 26 `relation:`-Fehler, 0 von 11
   Relationsendpunkten eine Komponenten-`id`) — ist **nicht objektspezifisch**; nichts
   daran hing an `rich_repo`. **Befund 05** (Single-Prompt-Kollaps am echten Repo,
   ROT auf beiden Modellen) weist in dieselbe Richtung.

   **Charakter: dies ist eine KÜRZUNG, keine ausgelöste Regel.** §3 Punkt 3 hat
   **NICHT gegriffen** — es wurde **entschieden, sie nicht zu prüfen**, mit Datum,
   **VOR jedem Z2-Lauf**, ohne Wirkung auf irgendeine Z2-Zahl. Die Vorprüfung nach
   §3 Punkt 3 wird **nicht gefahren**, weil der Extraktionsprompt für das Testrepo
   nach **N(m) = 365 + 356 · m** (Befund 07.5) weit über dem registrierten Fenster
   liegt: ein Ausfall wäre mit hoher Wahrscheinlichkeit ein **LIEFERAUSFALL**, kein
   **GÜLTIGKEITSAUSFALL**, und ein Fensterausfall darf §3 Punkt 3 **nicht auslösen**
   — derselbe Fehler wie beim trunkierten K2-Block (`data/z1/k2_trunkiert`, Befund
   07.4: dort meldet `validate_arch` denselben Text wie bei K3, aus völlig anderer
   Ursache).

   **E3 und §7 Punkt 6 sind damit NICHT AUSGEFÜHRT** — ausdrücklich **nicht** negativ
   ausgefallen (Gate-Notiz §5c: „beide sind als explorativ registriert und werden im
   Kürzungsfall als **nicht ausgeführt** ausgewiesen, nicht als negativ ausgefallen").

   **Der Verlust, benannt.** B2 hätte gezeigt, **ob die Art des Ist-Modells bis in die
   Regelableitung durchschlägt**. Den nachgelagerten Teil des Titel-Halbsatzes trägt
   nach Befund 07 nun **Z1 unmittelbarer**. Die **UF2-Folge wird hier NICHT
   weggeschrieben** — sie steht im Standdokument (`00_stand_und_entscheidungen.md` §2).

   **Es wird KEIN Befund behauptet.** Der Satz „die zweite Pipeline-Stufe kann nicht
   auf einem LLM-abgeleiteten Ist-Modell aufsetzen" wird **nicht** aufgenommen; er
   widerspräche der Markierung **ABGELEITET** oben.
4. Beide Ist-Modelle und die Fakten-Datei werden mit Hash im Z2-Manifest
   festgehalten. — *nachgezogen 01.09.2026 (S1-A1): mit dem Wegfall von B2 sind es
   **das eine** Ist-Modell (`ist_modell.yaml`) und die Faktenbasis
   (`input_facts.json`), beide nach §3a erzeugt und im Z2-Manifest gehasht.*
5. **Asymmetriesatz zum Kontextfenster** *(neu 01.09.2026, S1-A1)*: Das Kontextfenster
   wird **für B1 angehoben, für B2 nicht** — weil B2 ein **vorbestimmtes Resultat** hat
   und **keinen Auswegkatalog**, B1 dagegen die in **§3b** registrierte Wegeleiter.

### 3a Eingaben — Erzeugung, Laufparameter, Provenienz *(neu 01.09.2026, S1-A1)*

Zwei Dateien, beide **gehasht im Z2-Manifest**. §2 nennt die Eingabe „Triton-Ist-Modell
des Phase-04-Testrepos (Ilograph)"; die **Bezeichnung** bleibt dem Wortlaut nach richtig,
präzisiert wird hier die **Erzeugung**.

#### 3a-1 `ist_modell.yaml` — erzeugt mit Tritons eigenem Exporter, über den Editor

**Instrument, registriert:** `codeModelToFullExportDocument`
(`packages/triton-core/src/codeModelToIlograph.ts:863`), gerufen aus
`exportFullModelYaml` (`editor/src/App.vue:1394-1413`), serialisiert über
`stringifyIlographYaml` (`editor/src/ilograph/parse.ts:12-20`).

Es ist **derselbe Pfad**, der die Z1-Fixture `fixtures/rich_repo.full.ilograph.yaml`
erzeugt hat (Blob `ef8e0d01…`, SHA256 `34d6f2f4…`, 7 644 B). **Formidentität ist an
dieser Fixture nachweisbar**: acht Knotenschlüssel (`id`, `name`, `subtitle`,
`x-triton-node-type`, `x-triton-package-scope`, `x-triton-project-kind`,
`x-triton-inner-artefacts`, `children`), die `subtitle`-Muster „package · N folders"
bzw. „module · N artefacts" (Singular „N artefact" bei einem), `::`-Artefakt-Ids
(`…::function:search_books`), und **eine** Perspektive `dependencies` mit
`{from, to, label: 'imports'}`.

> **NACHTRAG 02.09.2026 (Auftrag S1-A1b) — die abgelegte Eingabe trägt ZWÖLF
> VERERBUNGSKANTEN, die die Achtermenge oben nicht nennt.** Belegt aus **S2b-2**
> (Commit `2b0ff04`; Fundstelle `data/z2/MANIFEST.md`, Prüfung 2):
>
> | Schlüssel | Knoten mit dem Schlüssel | Einträge | Schlüssel je Eintrag | Labelmenge |
> |---|---|---|---|---|
> | `x-triton-inner-artefact-relations` | **1** von 73 | **4** | `from`, `to`, `label` | `extends` |
> | `x-triton-cross-artefact-relations` | **5** von 73 | **8** | `from`, `to`, `label` | `extends` |
>
> **Zusammen ZWÖLF Kanten**, Label **durchgehend `extends`**, **Träger ausschliesslich
> Modulknoten**. Beispiel: `{from: depot.core.errors::class:NotFoundError, to:
> depot.core.errors::class:DepotError, label: extends}`. Sie stehen **AUSSERHALB** von
> `perspectives[0].relations` und **verschieben die 81 Importkanten NICHT** (Prüfung 4:
> 81 Relationen, 81 eindeutige `(from,to)`-Paare, 0 Selbstkanten).
>
> **Die acht Knotenschlüssel oben bleiben als Aufzählung der Z1-FIXTURE richtig; als
> Aufzählung der Z2-EINGABE sind sie unvollständig** — diese führt **zehn**. Was daraus
> für die Arbeitsteilung der beiden Eingaben folgt, steht in **§3a-2** (dort nachgezogen),
> die beiden Konsequenzen in **§6/§7 Punkt 3** und **§10 (T-Z2-8)**.
>
> **NICHT zu tun: die Kanten aus der Eingabe entfernen.** Sie sind Teil eines **gehashten
> Messeingangs** (`146dbb055e059b9dd948b27e185f33a2cb56557a534c55e0daf983c892336673`,
> 988 Zeilen, 42 959 B) und werden **nicht nachbearbeitet**.

> **NACHTRAG 02.09.2026 (Auftrag S1-A1b) — EINORDNUNG DES FORMBEFUNDS: FASSUNG A. Die
> Formidentität mit der Z1-Fixture ist NICHT verletzt.**
>
> Der Vergleich mit der Z1-Fixture (`rich_repo.full.ilograph.yaml`) ergab in S2b-2 genau
> die **zwei Knotenschlüssel** oben, die die Fixture **nicht kennt**. Der Code emittiert
> **beide NUR bei nichtleerem Inhalt** — `codeModelToIlograph.ts:224-225` (`tritongraph`
> @ `348ca9d`, rein lesend gegengelesen 02.09.2026):
> `...(innerRelations.length ? { 'x-triton-inner-artefact-relations': innerRelations } : {})`
> und **zeichengleich dasselbe Muster** für `crossRelations`.
>
> **VORABLESUNG an der Fixture** (S1-A1b, 02.09.2026, `~/ma/ma-llm-arch-extractor` @
> `5c0b65a`, **rein lesend — kein Commit, keine Änderung, kein Werkzeuglauf**):
> `rg -n --glob '!__pycache__' 'class [A-Za-z_]+\(' fixtures/rich_repo` liefert **VIER**
> Klassendefinitionen mit Basisklasse, von **VIERZEHN** Klassendefinitionen insgesamt:
>
> | Fundstelle | Zeile wörtlich | Basisklasse(n) | in der Fixture definiert? |
> |---|---|---|---|
> | `bookshop/infrastructure/payment_gateway.py:4` | `class PaymentError(Exception):` | `Exception` | **nein** — builtin |
> | `bookshop/domain/book.py:10` | `class Genre(str, Enum):` | `str`, `Enum` | **nein** — builtin bzw. `from enum import Enum` (`book.py:7`) |
> | `bookshop/domain/order.py:9` | `class OrderStatus(str, Enum):` | `str`, `Enum` | **nein** — builtin bzw. `from enum import Enum` (`order.py:4`) |
> | `bookshop/domain/order.py:46` | `class EmptyOrderError(Exception):` | `Exception` | **nein** — builtin |
>
> **Zahl der Klassendefinitionen mit Basisklasse insgesamt: 4. Davon mit einer
> Basisklasse, die selbst in der Fixture definiert ist: 0.** Die zehn übrigen Klassen
> (`CheckoutService`, `InventoryService`, `InMemoryBookRepository`, `FakePaymentGateway`,
> `InMemoryOrderRepository`, `Author`, `Book`, `Catalog`, `LineItem`, `Order`) tragen
> **gar keine Basisklasse**.
>
> **FASSUNG A gilt.** Das Merkmal war **an der Fixture nicht auslösbar**, weil das
> **Vergleichsobjekt es nicht erzeugt**: ohne Vererbung zwischen fixtureeigenen Klassen
> bleiben `innerRelations` und `crossRelations` **leer**, und der Exporter emittiert die
> beiden Schlüssel nach `codeModelToIlograph.ts:224-225` **gar nicht**. **Die Abweichung
> ist damit erklärt, OHNE eine Exporter-Änderung anzunehmen; T-Z1-4 wird hierfür
> ausdrücklich NICHT in Anspruch genommen.** Dazu passt der **Wortlaut** von T-Z1-4
> (Z1-Protokoll §10, `z1_protokoll_extraktionsvergleich.md:1443`): die dort geführten
> drei Commits sind `2b95ccb` (Ansichts-Toggle entfernt), `2003e50` (Sichtbarkeiten und
> `rollupImportRelations`) — **beide am Exporter, nicht am Vollexport-Pfad** — und
> `d26c790` („resolve relative imports in `__init__.py` against the package itself"),
> semantisch, aber an den **Importkanten**. **Keiner der drei betrifft Vererbungskanten.**
>
> **Damit ist die Einordnung in `data/z2/MANIFEST.md` („das ist genau der Fall, den der
> Geltungsvermerk vorgesehen hat") überholt** — dort war sie ausdrücklich **„nicht
> entschieden"**. **Entschieden wird sie HIER, nicht dort: `data/z2/` wird NICHT
> angefasst**, die Eingabe bleibt **bytegleich**, und ein Nachzug an `MANIFEST.md` ist
> **ein eigener Auftrag**.
>
> **Unverändert gilt:** der Export bezeugt den **Exporterstand vom Erzeugungsdatum**, und
> **jede Aussage „gleicher deterministischer Pfad wie in Z1" trägt diesen Vorbehalt**
> (Geltungsvermerk weiter unten). **Fassung A entkräftet den Vorbehalt NICHT** — sie
> entzieht ihm nur **diesen einen** Beleg.

**Zu registrierende Laufparameter** — sie verändern die Ausgabe und sind am Artefakt
**nicht ablesbar**:

| Parameter | Wert | Fundstelle und Wirkung |
|---|---|---|
| `detail` | `'slim'` | Vorgabe in `codeModelToIlograph.ts:875` (`options.detail ?? 'slim'`), vom Aufrufer zusätzlich **explizit gesetzt** (`App.vue:1406`). Entfernt Deklarationen, Signaturen und Quellorte und reduziert innere Artefakte auf `{id, name, subtitle}` (`slimExportResource`, Z. 830-853). **Die Signaturen trägt die Faktenbasis (3a-2), nicht das Ist-Modell — das ist die registrierte Arbeitsteilung.** |
| `scopeContainerId` | **NICHT GESETZT** (ganzer Wurzelbaum) | Bei gesetztem Scope werden **Ressourcen UND Kanten** beschnitten (Z. 867-886); der Wert kommt aus `entry.scopeId` und hängt daran, **wie der Tab geöffnet wurde**. **Am Artefakt zu PRÜFEN, nicht anzunehmen.** |
| `fileLineCounts` | wird im Exportpfad **nicht durchgereicht** | Z. 873-874 rufen `containerToResource(child, model.relations)` ohne das Optionsobjekt, das `fileLineCounts` trüge (Signatur Z. 195-198); der `, N loc`-Zusatz im `subtitle` (`withLoc`, Z. 289-291) entsteht damit **nicht**. Als **Formmerkmal** notieren. |
| `pythonSourceRoots` | bestimmt der **Runtime-Server** (`discoverPythonSourceRoots`), nicht der Aufrufer | **SOLLWERT: die Ressourcen-Ids lauten `depot.*`, NICHT `src.depot.*`.** Abweichung heißt: **Export verwerfen, Ursache klären, nicht nachbearbeiten.** |

**Provenienz — und hier ausdrücklich BESSER als bei Z1.** Der Export ist eine
**UI-Handlung ohne Commit**. Bei Z1 musste D1 den Erzeuger-Commit als **„nicht
entscheidbar"** ausweisen (`d1_bericht_fixture_provenienz.md` §4: „Welcher
`tritongraph`-Commit die Datei erzeugt hat, ist nicht entscheidbar"). Für Z2 wird
stattdessen **VOR dem Freeze** protokolliert: Editor-Repo und Commit (`tritongraph`,
**`348ca9d`**), Datum und Uhrzeit, Runtime-Version und Port, `workspacePath`, der
geöffnete Tab, die **vier Laufparameter** oben, Dateiname der Ausgabe und ihr **SHA256**.

**Auflagen an die Exportsitzung, mitzuregistrieren:**

- Das Testrepo steht auf Tag `baseline` (**`0d651041…`**) und **bleibt clean**. Der
  **SOLL-EDITOR wird NICHT benutzt**: `saveTargetTopologyYaml` schreibt nach
  `<workspace>/.triton/target.ilograph.yaml`, also **IN das Messobjekt**
  (`editor/src/conformance/loadProject.ts:148-161`).
- Am Checker wird **nichts gebaut und nichts committet**; `checker_git_head` bleibt
  unbewegt. Gearbeitet wird in `~/ma/tritongraph` (dort liegt `editor/node_modules`),
  **nicht im Messworktree**.
- Ladeweg ist `loadRuntimeWorkspaceProject` über `GET /api/workspace/bundle` —
  **ARBEITSBAUMSTAND, KEIN Git** (`loadProject.ts:37-66`).
  `loadRuntimeWorkspaceBaseProject` (ebd. Z. 75 ff.) wird **nicht** verwendet.

**Geltungsvermerk, verbindlich.** Der Exporter **hat sich seit der Z1-Fixture geändert**
(Z1-Protokoll **T-Z1-4**: drei Commits nach dem Fixture-Export, einer davon semantisch).
Der Z2-Export bezeugt daher den **Exporterstand vom Erzeugungsdatum**. Jede Aussage
„gleicher deterministischer Pfad wie in Z1" trägt **diesen Vorbehalt**. Ob T-Z1-4s
Begründung (`rollupImportRelations`, Sichtbarkeiten) den **Exportpfad** überhaupt
berührt, ist **OFFEN und wird HIER NICHT entschieden** — der heutige Code zeigt für
beide **keinen Aufrufpunkt im Exportpfad** (`rollupImportRelations` steht in
`codeModelToIlograph.ts:810`, im gefalteten Render-Zweig, gegen den Exportpfad
Z. 863-899, der `containerImportRelations` ruft; `hidden` nur am Flow-Knoten). Als
**Restposten außerhalb dieses Amendments** führen.

**KEIN Rückfall wird registriert** — zwei Wege sind **erwogen und verworfen**, mit Grund:

1. **`read_import_graph` / `component_edges`** (`tools/validate_soll.py:140-174`) ist
   **UNBRAUCHBAR**: `module_to_component` entsteht dort **ausschließlich** aus dem per
   `--soll` übergebenen Ilograph-YAML (`validate_soll.py:115` liest den Soll-Pfad,
   `:120` legt die Abbildung an, `:126-127` füllt sie aus den Soll-Ressourcen). Ein
   damit erzeugtes Ist **erbte die Komponentenstruktur des SOLLS** und verletzte
   **§3 Punkt 2** (Kontaminationsverbot).
2. **`deriveTopologyFromCodeModel`** erzeugt eine **`ResolvedTopology`** — das
   Prüfmodell der Rule-Engine, Komponenten als Punkt-Präfix nach `componentDepth`
   (Vorgabe **2**, `packages/triton-conformance/src/deriveTopology.ts:18-23`) —,
   **nicht** das von §2 verlangte **Ilograph-Architekturdokument**.

#### 3a-2 `input_facts.json` — Faktenextraktion des Extractors

**Aufrufargument ZWINGEND `<testrepo>/src`.** `extract_repo` kennt **keine
`src/`-Behandlung**: `_module_name` bildet den Modulnamen relativ zur übergebenen
Wurzel (`extractor.py:23-29`), die Modulnamen lauteten sonst `src.depot.…`.

**Gegenprobe nach der Erzeugung:** die **Modulnamenmenge der Faktenbasis** und die
**Menge der Modul-Ressourcen-Ids des Ist-Modells** sind **bis auf leere `__init__.py`
deckungsgleich**. **Abweichung melden, nicht angleichen.**

~~**Arbeitsteilung der beiden Eingaben, ausdrücklich registriert:** das **Ist-Modell**
trägt **Struktur** (Paket-/Modulbaum, innere Artefaktnamen) und die **deduplizierten
Importkanten auf Containerebene**; die **Faktenbasis** trägt die **SIGNATUREN**, die im
`slim`-Export fehlen. **Beides zusammen ist die Evidenzbasis, an der Z2-P gemessen wird.**~~
— **präzisiert am 02.09.2026 (Auftrag S1-A1b); der Alttext bleibt vollständig stehen, weil
die Evidenzbasis von Z2-P auf ihm registriert wurde.**

**Arbeitsteilung der beiden Eingaben, PRÄZISIERTE FASSUNG (02.09.2026, S1-A1b):** das
**Ist-Modell** trägt **Struktur** (Paket-/Modulbaum, innere Artefaktnamen), die
**deduplizierten Importkanten auf Containerebene** **UND — neu registriert —
VERERBUNGSKANTEN ZWISCHEN ARTEFAKTEN (`extends`)**, **zwölf** an der Zahl, in
`x-triton-inner-artefact-relations` (4) und `x-triton-cross-artefact-relations` (8),
Träger ausschliesslich Modulknoten (**§3a-1**, Nachtrag 02.09.2026); die **Faktenbasis**
trägt die **SIGNATUREN**, die im `slim`-Export fehlen. ~~**Beides zusammen ist die
Evidenzbasis, an der Z2-P gemessen wird.**~~ — **nachgezogen am 02.09.2026 (Auftrag
S1-A1c), weil Stufe 0b gezogen ist; der Satz bleibt stehen, die neue Fassung steht im
Nachtrag unten.**

**ZWEI KONSEQUENZEN aus den zwölf Vererbungskanten, ausdrücklich registriert:**

1. **Das Modell kann aus ihnen Regeln ableiten, die KEINER der sechs
   Verletzungskategorien entsprechen** — etwa **Vererbungsverbote über
   Komponentengrenzen**. Ein solcher Vorschlag ist **KEIN Fehler, sondern ein BEFUND**
   und wird in **§7 Punkt 3** als **nicht zuordenbar** geführt; **Z2-Z erhält dafür
   ausdrücklich den Wert „keiner der sechs"** (§6 und §7 Punkt 3, dort nachgezogen).
2. **T-Z2-8 wird ergänzt** (§10): neben den vier **reservierten Ports**, den
   **Suffixkonventionen**, den **geschützten Internals** und den **Zweierzyklen** trägt
   die Eingabe **auch die VERERBUNGSSTRUKTUR des Testrepos**; die **Abdeckungsmatrix
   (§7 Punkt 3) ist insoweit ebenfalls Eigenschaft des Messobjekts**, nicht des Modells.

**NACHTRAG 02.09.2026 (Auftrag S1-A1c) — DIE EVIDENZBASIS NACH DEM ZIEHEN VON STUFE 0b.**

**BEFUND:** in **S2c-2** (Commit **`89b70e6`**) wurden **Stufe 0** (Docstrings, leere
`__init__.py`) **und Stufe 0b** (Importblöcke) **gezogen**; die abgelegte Eingabe
`data/z2/eingaben/input_facts.json` trägt **52 Records OHNE `imports`-Blöcke und MIT
Signaturen**.

**NEUE FASSUNG der Evidenzbasis, an der Z2-P gemessen wird** — nachgezogen, wie es §3b,
Stufe 0b, letzter Satz verlangt: **„entscheidbar allein aus den IMPORTKANTEN DES
IST-MODELLS und den SIGNATUREN der Faktenbasis"** — **statt „aus Imports + Signaturen"**.
Ausgeschrieben mit Entscheidungsregel und Beispielen steht sie in **§6 (Z2-P)**; dort steht
auch der **Alttext durchgestrichen sichtbar**.

**PREIS — GEMESSEN statt angenommen**, an dieser Faktenbasis (`data/z2/MANIFEST.md`, Block
„Grössenregel angewandt", Abschnitt *Preis von Stufe 0b*):

| Posten | Zahl |
|---|---|
| Importfakten in den **52** behaltenen Records | **90** |
| davon `import x as y` (**Aliasname** gesetzt) | **0** |
| davon `from X import Y` mit `names[]` | **0** |
| davon **relative** Importe | **0** |
| davon mit Ziel **innerhalb** des Messobjekts (`depot.*`) | **81** |
| davon mit Ziel **ausserhalb** (**extern**) | **9** |

**Das Testrepo verwendet ausschliesslich die Form `import a.b.c`** — **drei der vier in
§3b registrierten Preisposten sind an dieser Eingabe leer.** Von den **90 Importfakten**
haben **81 ein Ziel in `depot.*`**, und das **Ist-Modell führt genau 81 Relationen mit 81
eindeutigen `(from,to)`-Paaren** — **dieselbe Menge, eins zu eins; hier geht nichts
verloren.** **Verloren gehen ausschliesslich die NEUN externen Importe:** **acht
`sqlalchemy.orm`** (`depot.billing.models.invoice_models`, `…invoice_view_models`,
`depot.identity.models.customer_models`, `…customer_view_models`,
`depot.orders.models.order_line_models`, `…order_line_view_models`,
`depot.orders.models.order_models`, `…order_view_models`) und **einer `typing`**
(`depot.core.ports`). Externe Ziele haben **keinen Container** und stehen im Export
**nicht**.

**KONSEQUENZ — ausdrücklich:** **ein Vorschlag, dessen Prüfbarkeit von einem EXTERNEN
Import abhängt, ist aus der Eingabe nicht entscheidbar.** **Framework-Typen bleiben über
die SIGNATUREN sichtbar, nicht mehr über eine Importliste.** Ein solcher Vorschlag wird
unter **Z2-P als NICHT ENTSCHEIDBAR bewertet, MIT VERMERK DER URSACHE** — **er ist damit
kein Modellfehler, sondern eine Folge der registrierten Kürzung.**

**DIE KÜRZUNG IST VORAB REGISTRIERT.** **Stufe 0b steht seit dem 01.09.2026 (S1-A1) in
§3b**, sie ist **aus einem Fensterbefund gezogen** (**38 748 > 32 768**, Messung S2c-2) und
**NICHT nach Kenntnis der Z2-Ergebnisse**: zum Zeitpunkt des Ziehens existiert **kein
einziger Z2-Lauf**. **Nachgezogen in §10, T-Z2-6 und T-Z2-9.**

### 3b Größenregel — vor der Messung registriert *(neu 01.09.2026, S1-A1)*

~~Gemessen wird mit **`tools/z1_tokenizer.py`** (**parametrisiert**, nicht neu
geschrieben — `DEFAULT_STORE`/`DEFAULT_MODEL` sind Funktionsvorgaben), an **beiden
Eingaben** und am **gerenderten Prompt**.~~ — **überholt am 02.09.2026 (Auftrag S1-A1b);
ersetzt durch (a)–(e) unmittelbar darunter.** Der Satz **bleibt stehen**, weil die
Schwelle und die Wegeleiter dieses Abschnitts **auf ihm** registriert wurden.

**BEFUND, der die Auswechslung auslöst** *(S2b-2, Commit `2b0ff04`; Fundstelle
`data/z2/MANIFEST.md`, Prüfung 7)* — **wörtlich zu registrieren:**

> `tools/z1_tokenizer.py` **weist `data/z2/eingaben/ist_modell.yaml` durch seinen eigenen
> Wächter ab**: `assert_ascii` (`z1_tokenizer.py:197-200`) wirft
> `TokenizerUnavailable — ist_modell.yaml is not pure ASCII; the ASCII split pattern
> would be wrong`. **Ursache ist das Zeichen `·` in jedem `subtitle`** des Triton-Exports
> („package · 4 folders", „module · N artefacts"). Das Werkzeug **rendert `\p{L}`/`\p{N}`
> des qwen2-Prätokenizers als `[A-Za-z]`/`[0-9]`** und **dokumentiert selbst**, dass das
> **nur für reines ASCII exakt** ist (Kopfkommentar Z. 22-24). **Der gerenderte Prompt
> enthält das Ist-Modell und ist damit ebenfalls nicht ASCII** — die Abweisung trifft
> also **nicht nur die Eingabe, sondern die Messgröße der Schwelle selbst**. Der **unter
> Umgehung des Wächters** erhaltene Wert **8 438** ist **KEIN Messwert** und wird
> **nirgends als solcher geführt**.

**Das in §3b registrierte Messinstrument kann den Messgegenstand nicht messen.** Die
folgenden fünf Punkte **(a)–(e)** treten an seine Stelle — **registriert VOR der
Messung**, wie der Abschnitt es verlangt.

**(a) PRIMÄRE MESSGRÖSSE: die SERVERSEITIG gemeldete Prompt-Tokenzahl.** Gemessen wird
`usage.prompt_tokens` bzw. `prompt_eval_count` bei einem **Kaltlauf mit
`max_tokens: 1`** gegen den **lokalen Endpunkt** — **dieselbe Zählweise, mit der Z1-T
gemessen hat** und die `tools/check_z1_delivery.py` verwendet (`usage.prompt_tokens`,
Z. 177; Kopfkommentar Z. 24-25: „Cold, because Ollama reports `prompt_eval_count` —
NEWLY evaluated"). **Begründung:** sie ist die **faithfulste** Quelle — sie zählt, was
der Server tatsächlich zählt, statt es aus einem nachgebauten Muster zu schätzen — und
sie **erfordert keinen Umbau an einem Werkzeug, dessen vier Tore G1-G4 die
Z1-Hochrechnung tragen** (`z1_tokenizer.py:220-247`).

> **AUSDRÜCKLICH ZU REGISTRIEREN — dieser Kaltlauf ist eine INSTRUMENTENMESSUNG, KEIN
> Z2-LAUF.** Er **zählt gegen kein Z2-Budget** (§2: sechs Läufe, drei je Zelle), er wird
> **nicht als Lauf archiviert**, **seine Ausgabe wird nicht gelesen und nicht bewertet**.
> Abgelegt werden **ausschliesslich**: die **gemeldete Tokenzahl**, das **gesetzte
> Fenster**, **Modell**, **Endpunkt**, **Zeitstempel** und der **SHA256 des gemessenen
> Textes**. Er braucht **keinen Schlüssel** (lokaler Endpunkt) und **keine rekonstruierte
> Extractor-Laufzeit** (reiner HTTP-Aufruf).

**(b) MESSFENSTER UND KÜRZUNGSDETEKTOR — die Messung darf sich nicht selbst
verfälschen.** Bei **zu kleinem Fenster kürzt der Server vorn** und meldet die
**GEKÜRZTE** Zahl — **ohne Fehler und ohne Logzeile** (Z1: **4 281 gesendet, 2 050
gemeldet**). Eine unbemerkt gekürzte Messung machte die Schwelle **wertlos**, weil sie
**genau dann** eine kleine Zahl meldete, wenn der Text zu gross ist. Daher:

- **gemessen wird bei Fenster 32 768** — der **Modellgrenze** von `qwen2.5-coder:7b`
  (`ollama show qwen2.5-coder:7b`: `context length 32768`; rein lesend gegengelesen am
  02.09.2026, **kein Laden des Modells**);
- die gemeldete Zahl gilt als **UNGÜLTIG**, wenn sie dem **gesetzten Fenster gleicht**
  oder es um **weniger als 64 Token unterschreitet** — dann **liegt Kürzung vor**, und es
  wird **nach (c)** gemessen;
- **das Anheben des Fensters FÜR DIE MESSUNG ist ausdrücklich NICHT gleichbedeutend mit
  dem Ziehen von Stufe 1 der Wegeleiter.** Welche Stufe für die **LÄUFE** gezogen wird,
  **folgt erst aus der gemessenen Zahl**; die Messung geht der Entscheidung voraus und
  darf sie nicht vorwegnehmen. Die **Fensteränderung ist DATIERT zu protokollieren**, sie
  liegt **NACH Z1s Messung**, und `tools/check_z1_delivery.py`
  (`REGISTERED_CONTEXT = 16384`, Z. 61) ist danach **umgebungsfremd** — **Konstante
  parametrisieren, nicht umschreiben** (§3b, Weg 1, unverändert).

**NACHTRAG 02.09.2026 (Auftrag S1-A1c) — DER DETEKTOR AUS (b) IST FÜR DIE TATSÄCHLICH
EINGETRETENE KÜRZUNGSART BLIND.** Der Wortlaut oben **bleibt vollständig gültig und bleibt
stehen**; **nichts an ihm wird zurückgenommen**. Das Fenstergleichheits-Kriterium ist
**nicht falsch, sondern unzureichend** — es wird um **zwei weitere Kriterien** ergänzt.

**BEFUND, der die Ergänzung auslöst** *(S2c-2, Commit `89b70e6`; Fundstelle
`data/z2/MANIFEST.md`, Block „Grössenregel angewandt")* — **wörtlich zu registrieren:**

> In S2c-2 meldete die **Messung des vollen Prompts (M6) 16 386 Token** — **WENIGER als
> die Messung der darin enthaltenen Faktenbasis allein (M5, 29 095)**. Das registrierte
> Kriterium (**Gleichstand mit dem Fenster oder weniger als 64 Token Abstand**,
> Verdachtsbereich **ab 32 705**) sprach **NICHT** an: **16 386 liegt 16 382 Token unter
> dem Fenster**. **Die Kürzung war also unter dem bisherigen Detektor unsichtbar.**

**ZWEI NEUE KRITERIEN — GLEICHRANGIG zum bisherigen, JE FÜR SICH HINREICHEND für das
Urteil UNGÜLTIG:**

**(b2) MONOTONIE.** **Enthält eine Nutzlast eine andere vollständig, so muss ihre gemeldete
Tokenzahl mindestens so gross sein.** **Jede Verletzung heisst UNGÜLTIG.** Praktisch: **der
volle Prompt wird stets GEGEN die Einzelmessung seiner grössten Komponente geprüft, nie
allein bewertet.**

**(b3) HALBFENSTER-SIGNATUR.** Eine gemeldete Zahl gilt als **UNGÜLTIG**, wenn sie
**`Fenster / 2 + 2` gleicht** oder es um **weniger als 64 Token unterschreitet**. **BELEG,
zwei unabhängige Punkte:** **32768 / 2 + 2 = 16 386** (**S2c-2, M6**) und
**4096 / 2 + 2 = 2 050** (**Z1, aktenkundig** — **4 281 gesendet, 2 050 gemeldet**, Fenster
**4 096**).

> **EVIDENZEINORDNUNG — VERBINDLICH.** Dass der Server bei Überschreitung auf die **HALBE**
> Fenstergrösse kürzt, ist **ABGELEITET**: **zwei übereinstimmende Messpunkte**, **keine
> Bestätigung aus Quellcode oder Dokumentation von Ollama 0.32.15**. **Als REGULARITÄT ist
> es gemessen, als MECHANISMUS nicht.** **Diese Unterscheidung ist in jeder Verwendung des
> Kriteriums zu wahren** — (b3) ist ein **Detektor**, keine Aussage über die
> Implementierung des Servers.

**NACHZUG AN DIE LIEFERZUSICHERUNG — hier registriert, umzusetzen in S4:** der **Wächter
von `tools/run_z2.py`** prüft **NICHT nur Gleichstand mit dem Fenster**, sondern **(b2) und
(b3) mit**. **Ein Lauf, dessen gemeldete Prompt-Tokenzahl eines der drei Kriterien erfüllt,
BRICHT AB und wird nicht als Lauf gezählt.**

**(c) RÜCKFALL — ADDITIVE TEILMESSUNG.** Falls das Fenster **nicht angehoben werden
kann** oder **(b) Kürzung anzeigt**: der Text wird in **N Teile** zerlegt, die **je
sicher unter dem Fenster** liegen, **jeder Teil einzeln gemessen** und die **Summe**
gebildet. Der Fehler entsteht **nur an den Teilgrenzen** und ist damit **auf höchstens
N Token beschränkt**; **N wird mit dem Ergebnis ausgewiesen**. Für eine **Schwelle von
24 000** ist er **unerheblich**; er wäre es **NICHT für die Lieferzusicherung**, die auf
**zeichengleiche** Zahlen prüft.

**ERFAHRUNGSWERT, nachgetragen 02.09.2026 (Auftrag S1-A1c) — DIE REGEL SELBST BLEIBT
UNVERÄNDERT:** das Verfahren aus **(c)** ist in **S2c-2 angewandt** worden (**N = 3**) und
hat in **drei ungekürzten Kontrollfällen auf das Token genau** getroffen
(Kontrollmessung **9 668 / 9 668**, **M8 27 525 / 27 525**, **M9 24 104 / 24 104** —
Differenz je **0**, Fehler **≤ 3**). Die registrierte **Fehlerschranke ≤ N Token bleibt
unangetastet**: sie ist die **Zusicherung**, der gemessene Fehler ist der
**Erfahrungswert**. **Aus drei Fällen wird keine engere Schranke abgeleitet.**

**(d) `tools/z2_tokenizer.py` — KÜNFTIGES WERKZEUG, NICHT Gegenstand dieser Messung.**
Die **Lieferzusicherung in S4** braucht eine **erwartete Tokenzahl OHNE Modell-Call** —
so, wie `check_z1_delivery.py` sie für Z1 hatte. Sie wird durch ein **NEUES** Werkzeug
`tools/z2_tokenizer.py` erzeugt: **Kopie der Zähllogik** mit **korrektem Unicode-Muster**
für `\p{L}`/`\p{N}` anstelle der ASCII-Ersatzklassen. **`tools/z1_tokenizer.py` wird
dafür NICHT umgebaut** — seine Tore **tragen die Z1-Hochrechnung**, und ein Musterwechsel
unter ihnen entwertete sie. **Zwei Tore für das neue Werkzeug, hier vorab registriert:**

| Tor | gemessen an | bestanden, wenn | was damit belegt ist |
|---|---|---|---|
| **T1** | dem **Z1-Prompt** `data/z1/k2/run0/extractor/attempts/attempt_0/prompt.txt` (SHA256 `cb2fcefd…0ee2d`) | es die **archivierte Zahl 4 281** liefert | die **Musteränderung verschiebt auf ASCII nichts** |
| **T2** | `data/z2/eingaben/ist_modell.yaml` (SHA256 `146dbb05…36673`) | es die **nach (a) gemessene serverseitige Zahl innerhalb von 0,5 %** trifft | die **Musteränderung ist auf Nicht-ASCII validiert** |

**Fällt ein Tor, wird das Werkzeug NICHT verwendet**, und die Lieferzusicherung stützt
sich **auf einen Kaltlauf je Lauf**.

**(e) GELTUNGSBEREICH DER SCHWELLE.** Die Schwelle von **24 000 Token bei Fenster
32 768** bindet **auf der Modellbedingung K2** — sie ist **die einschränkende**. Für
**K3** wird die gemeldete Prompt-Tokenzahl **berichtet**, sie ist aber **nicht
schwellenbildend**. **Die Tokenzahlen der beiden Modelle sind NICHT vergleichbar** —
verschiedene Tokenisierer — und werden **nie gegeneinander gerechnet**, weder als
Differenz noch als Verhältnis.

**SCHWELLE:** gerenderter Prompt **≤ 24 000 Token** bei Fenster **32 768**, Reserve
**≥ 8 000 Token für das Generat** — ein **abgeschnittenes Generat** sähe sonst wie
**Modellversagen** aus.

**Lagebild — ABGELEITET und als solches ausgewiesen:** Ist-Modell grob **9–12 k Token**
(Z1-Fixture 7 644 B für **elf** substanzielle Module, skaliert auf **50** — die Zahl der
inhaltstragenden Module der Baseline, `00_stand_und_entscheidungen.md` §7), Faktenbasis
**N(50) = 365 + 356 · 50 = 18 165 Token** (Befund 07.5), Instruktion rund **1 k**.
Erwartete Summe **28–31 k**, also **OBERHALB der Schwelle**. **Die Leiter ist der
wahrscheinliche Fall, nicht die Vorsichtsklausel.**

**Wege, in dieser Reihenfolge, je ausgelöst durch „die vorige Stufe reicht nicht":**

| Stufe | Maßnahme | Preis |
|---|---|---|
| **0** | **Docstrings aus der Faktenbasis streichen** (`ModuleFacts.module_docstring`, `FunctionFact.docstring`, `ClassFact.docstring`) und **leere `__init__.py` auslassen** | **Kostet die Evidenzbasis von Z2-P nichts.** |
| **0b** | **Importblöcke aus der Faktenbasis streichen** (`ImportFact`), weil die Importkanten im Ist-Modell bereits **modulscharf** stehen (`containerImportRelations`, `codeModelToIlograph.ts:575-589`; `endpointContainerId` bildet Artefakt-Ids auf ihren Container ab) | **Zu benennen:** verloren gehen **Aliasnamen**, die `names[]`-Listen von `from X import Y`, **relative Importe** und — der eigentliche Preis — **EXTERNE Importe**, weil externe Ziele **keinen Container** haben und im Export **nicht erscheinen**. Framework-Typen bleiben über die **Signaturen** sichtbar, nicht mehr über die Importliste. **Wird diese Stufe gezogen, ist die Evidenzbasis in §6 (Z2-P) nachzuziehen:** „Imports (als **Kantenmenge des Ist-Modells**) + Signaturen". |
| **1** | **Fenster auf 32 768** (Z1-T: K2 dort `8%/92% CPU/GPU` bei 6,8 GB gegen `100% GPU` bei 5,5 GB) | **Mitzuregistrieren:** das Fenster ist **nur über den systemd-Drop-in** änderbar (`/etc/systemd/system/ollama.service.d/context.conf`; der Extractor-Client sendet **kein `options`**); die Änderung ist **DATIERT** und liegt **NACH** Z1s Messung, und `tools/check_z1_delivery.py` (`REGISTERED_CONTEXT = 16384`, Z. 61) ist dann **umgebungsfremd** — **Konstante parametrisieren, nicht umschreiben.** |
| **3** | **Ausschnitt des Testrepos** über `scopeContainerId` | **Ändert das Messobjekt**, gesondert zu registrieren, und beschneidet nach `codeModelToIlograph.ts:878-886` **AUCH die Kantenmenge**. |
| **4** | **K3-only** | Verliert die **Modellklassen-Achse**, die nach Befund 07/08 die **interessanteste** ist. |
| **2** | **Faktenbasis auf Importe reduzieren, SIGNATUREN WEG** | **LETZTE Wahl:** `FORBIDDEN_SIGNATURE_TYPE` und `API_CONTRACT` wären dann **konstruktionsbedingt unvorschlagbar**, und **E2/E4 mäßen die Kürzung statt das Modell**. |

**Gezogen wird die erste Stufe, die die Schwelle hält;** jede gezogene Stufe wird im
**Z2-Manifest mit der gemessenen Tokenzahl vor und nach ihr** ausgewiesen.

**(f) INSTRUKTIONSBUDGET R1, GEZOGENER STAND DER WEGELEITER, AUFLAGE AN S3** *(neu
02.09.2026, Auftrag S1-A1c)*. Dieser Punkt schliesst an **(a)–(e)** an und steht
**hinter** der Wegeleiter-Tabelle, weil er den **Stand NACH deren Anwendung** festhält.
Herkunft **aller** Zahlen: **S2c-2, Commit `89b70e6`**; Fundstellen
`data/z2/MANIFEST.md` (Block „Grössenregel angewandt") und
`data/z2/messungen/tokenmessung_2026-09-02.json`.

**DIE LAGE, GEMESSEN.** Der **volle Prompt** misst **nach den gezogenen Stufen 0 und 0b**
**24 104 Token** bei einer **Instruktion von 1 200 Token**. **Die vorregistrierte Schwelle
von 24 000 Token ist damit um 104 Token ÜBERSCHRITTEN.**

> **DIE SCHWELLE BLEIBT UNVERÄNDERT BEI 24 000.** **Ausdrücklich zu registrieren:** sie
> **NACH Kenntnis der Zahl 24 104 anzuheben**, oder sie **durch ihre Begründung zu
> ersetzen** — die **Generat-Reserve ≥ 8 000**, hier mit **8 664** erfüllt —, **wäre
> Nachverhandlung und ist ausgeschlossen.** Die Reservebedingung ist die **Begründung** der
> Schwelle, **nicht die Schwelle**; dass sie erfüllt ist, **entbindet nicht von ihr**.

**VERSCHÄRFT WIRD STATTDESSEN DAS INSTRUKTIONSBUDGET.** Es ist **erst am 02.09.2026 in
S2c-2 gesetzt** worden und ist **selbst keine vorregistrierte Grösse** — es zu verschärfen
ist daher **keine** Nachverhandlung:

| Grösse | gesetzt 02.09.2026 (S2c-2) | **ab jetzt (S1-A1c)** | Charakter |
|---|---|---|---|
| **R1 OBERGRENZE** | ~~**1 200 Token**~~ | **1 000 Token** | **BINDEND für Anhang A** |
| **R1 ZIELGRÖSSE** | rund 700 Token | **rund 700 Token — unverändert** | **NICHT bindend** |

**Begründung der Obergrenze 1 000:** der **gemessene Kipppunkt** liegt bei **1 096 Token**
(1 200 − 104); **1 000 lässt 96 Token Sicherheit** für die Messung des **tatsächlichen**
Anhang A und liegt **weiter deutlich über der Zielgrösse**. **Erwarteter voller Prompt bei
einer Instruktion von 1 000 Token: rund 23 904 Token.** **Die Begründung der Zielgrösse
bleibt unverändert:** in **Z1 kippte die Formatgültigkeit an 909 Zeichen**
Instruktionstext.

**DIE VERSCHÄRFUNG ZIEHT KEINE WEITERE STUFE DER WEGELEITER.** Das **Messobjekt bleibt
unverändert** (**nicht Stufe 3**), die **Modellklassen-Achse bleibt erhalten** (**nicht
Stufe 4**), die **Signaturen bleiben erhalten** (**nicht Stufe 2**). **E2 und E4 sind
unberührt.**

**GEZOGENER STAND DER WEGELEITER — abschliessend festgehalten.** Fundstelle
`data/z2/MANIFEST.md`, Block **„Grössenregel angewandt"**, Commit **`89b70e6`**:

| Stufe | Stand | Beleg |
|---|---|---|
| **1** — Fenster 32 768 | **WIRKSAM**, nicht erneut gezogen | wirksam seit der **datierten Umgebungsänderung vom 02.09.2026**; das Anheben **für die Messung** ist nach **(b)** ausdrücklich **nicht** das Ziehen von Stufe 1 — hier ist es die **Laufumgebung** und steht bereits |
| **0** — Docstrings streichen, leere `__init__.py` auslassen | **GEZOGEN** | **38 748 → 27 525** (−11 223); **73 → 52 Records** |
| **0b** — Importblöcke streichen | **GEZOGEN** | **27 525 → 24 104** (−3 421); Preis gemessen in **§3a-2 (Nachtrag 02.09.2026)** und **§6 (Z2-P)** |
| **3** — Ausschnitt über `scopeContainerId` | **NICHT gezogen** | Messobjekt unverändert |
| **4** — K3-only | **NICHT gezogen** | Modellklassen-Achse erhalten |
| **2** — Signaturen weg | **NICHT gezogen** | Signaturen erhalten; **E2/E4 unberührt** |

**ZWINGENDE AUFLAGE AN S3 — hier vorab registriert:** **nach dem Schreiben von Anhang A
wird der VOLLE Prompt mit dem TATSÄCHLICHEN Instruktionstext gemessen**, nach dem Verfahren
**(a)–(c)** und mit dem **Detektor einschliesslich (b2) und (b3)**. **Hält er die 24 000
nicht, wird ANHANG A GEKÜRZT — NICHT die Schwelle bewegt.** **Die Messung und ihr Ergebnis
gehen nach `data/z2/messungen/` und in `data/z2/MANIFEST.md`, vor dem Freeze.**

**NACHRICHTENSTRUKTUR — aus S2c-2 übernommen und hier festgeschrieben (R3):** **ZWEI
Nachrichten.** Die **`system`**-Nachricht trägt **die Instruktion**; die
**`user`**-Nachricht trägt **Block 1 (Ist-Modell)** und **Block 2 (Faktenbasis)** mit den
in `data/z2/MANIFEST.md` **wörtlich abgelegten Blocküberschriften**. **Weicht Anhang A
davon ab, ist die Messung zu wiederholen.**

**RAHMUNGSAUFWAND — Erfahrungswert, keine Regel:** die Differenz zwischen dem **vollen
Prompt** und der **Summe seiner Teile** betrug **−14 Token**. Erklärung: eine **eigene
`system`-Nachricht ersetzt den Standard-System-Prompt** (**13 gegen 29 Token**, je
gemessen); dem stehen **+17** und **+14 Token** für die **zwei Trennzeilen** gegenüber.

## 4. Prompt

- **Eine** Prompt-Version, im Wortlaut Teil dieses Dokuments vor dem Freeze
  (Anhang A, vor Ausführung einzufügen und mitzufrieren).
- Der Prompt fordert ausdrücklich **normative** Regeln („was sollte gelten /
  verboten sein — auch wenn der Code es derzeit einhält"), nicht Beschreibung
  des Ist-Zustands. Er nennt keine der sechs Kategorien beim Namen (sonst wird
  Kategorien-Abdeckung zur Prompt-Folge statt zum Befund).
- ~~Output-Format: das implementierte Checker-Regelschema (§5), als striktes
  JSON-Schema im Request.~~ — **überholt am 01.09.2026 (S1-A1):** Output-Format ist das
  **eigene Umschlagformat** (§5), handgeschrieben, als striktes JSON-Schema im Request.
- **Nachbesserungsregel:** maximal eine Prompt-Revision, und nur bei
  technischem Scheitern (Format-Invalidität in > 50 % der Läufe einer
  Bedingung). Inhaltliches Nachsteuern („mehr semantische Regeln bitte") ist
  verboten. Jede Revision ist ein Amendment (§11).
  **Auswertbarkeit und Folge für N₁** *(neu 01.09.2026, S1-A1)*:
  - Die Regel wird **erst bewertbar, wenn ALLE DREI Läufe einer Bedingung vorliegen**;
    **`> 50 %` ist bei n = 1 nicht auswertbar.**
  - Tritt sie ein, **beginnt die Zelle mit dem revidierten Prompt NEU**. Alle Läufe des
    alten Prompts **bleiben archiviert und gehasht** und werden als **Läufe des
    ÜBERHOLTEN PROMPTS** berichtet — ausdrücklich **NICHT als ungültig**: nach Befund 07
    ist **Formatinvalidität selbst ein Ergebnis** und trägt dort den halben Befund.
  - **N₁ wird in diesem Fall am ersten Lauf unter dem revidierten Prompt NEU gezählt**;
    die alte Zahl bleibt **archiviert und wird als überholt geführt**, die **SCHWELLE
    bleibt unverändert** (Gate-Notiz §5c).

## 5. Output-Format & Wohlgeformtheits-Orakel

~~Referenzschema ist das **implementierte** Regelschema des Checkers
(`packages/triton-conformance/src/rules.ts`):
`id`, `category`, `kind` (structural|semantic), `scope.components[]`,
`statement`, `severity` (error|warning), optional `predicate` (import-boundary).~~

- ~~Wohlgeformtheit (K1) entscheidet ausschließlich der vorhandene Parser
  (`parseArchitectureRules`) — maschinell, binär, kein Ermessen.~~
  — **überholt am 01.09.2026 (S1-A1); mit dem Formatwechsel gegenstandslos.** An seine
  Stelle tritt das zweistufige Orakel **Z2-W** unten.
- ~~Bewusste Abweichung vom ursprünglich geplanten Entscheidung-G-Schema
  (sechswertiges `typ`-Enum, `evidence`): Referenz ist der gebaute Stand;
  die Abweichung wird in der Arbeit einmal begründet (Kapitel 5).~~
  — **überholt am 01.09.2026 (S1-A1):** Referenz ist **weder** das Entscheidung-G-Schema
  **noch** das Checker-Regelschema, sondern das **eigene Umschlagformat** unten.
- Threat daraus: gemessen wird auch Schema-Folgsamkeit, nicht nur
  Regel-Erfindungsfähigkeit (§10, T-Z2-6). — *nachgezogen 01.09.2026: das
  Format-Korsett ist **gewechselt**, nicht entfallen; dazu T-Z2-6 und der neue T-Z2-9.*

### 5.1 Ausgabeformat — ein EIGENES Umschlagformat, handgeschrieben *(01.09.2026, S1-A1)*

Das Ausgabeformat ist ein **eigenes Umschlagformat**, **HANDGESCHRIEBEN**, mit
**`additionalProperties: false`** und **explizitem `required`**. Felder:

| Feld | Form | Bemerkung |
|---|---|---|
| `id` | String, im Lauf eindeutig | |
| `category` | String, **FREI** | kein Enum — die Kategorienabdeckung soll Befund sein, nicht Prompt-Folge (§4) |
| `scope.components[]` | **Objektform, zwingend so** | sie deckt sich mit dem Checker-Regelschema und **trägt die Umschreibung aus §7 Punkt 8** |
| `statement` | natürliche Sprache | **TRÄGT die Regel** |
| `severity` | `error` \| `warning` | |

**KEIN `kind`. KEIN `predicate`.**

**NACHTRAG 02.09.2026 (Auftrag S3) — `minItems: 1` ERGÄNZT.** Der Zusatz ist **rein
additiv**: **kein Alttext ist berührt**, die Feldtabelle oben bleibt **unverändert**, und
**kein Feld kommt hinzu**. Das gesendete Schema (**Anhang A, A4**) trägt **`minItems: 1`**
an **zwei** Stellen — auf **`rules`** und auf **`scope.components`**.

**Begründung.** Ohne die Auflage ist **`{"rules": []}`** formal gültig, und ebenso ein
**`{"components": []}`** in einem einzelnen Vorschlag. Eine **leere Antwort** wäre dann
unter **Z2-W nicht als Ausfall erkennbar** — sie verletzte keine der vier Bedingungen aus
§5.3 —, und **N₁ = 0 wäre nicht von einem Modellbefund unterscheidbar**: die Zahl 0 hiesse
einmal „das Modell schlägt keine Regel vor" und einmal „das Modell hat geantwortet, ohne
etwas zu sagen", **ohne dass die Messung die beiden trennen könnte**.

**AUSDRÜCKLICH: KEINE ZIELZAHL, KEINE OBERGRENZE.** `minItems: 1` schliesst **allein den
trivialen Nullfall** aus. Es nennt **keine erwartete Menge**, setzt **keine Obergrenze**,
und die vierte Auflage an den Prompt — **er nennt keine Zahl und keine Mengenangabe**
(**Anhang A, A5 (d)**) — ist davon **unberührt**: das Schema ist nicht der Prompt, und
**N₁ bleibt Messgröße** (Gate-Notiz §5c).

**FERNER: §5.3 BLEIBT UNVERÄNDERT.** Die Wohlgeformtheitsliste **Z2-W** wird **nicht** um
`minItems` ergänzt. Grund ist §5.3 Punkt 1: **Schemakonformität ist unter `strict: true`
providerseitig erzwungen und ausdrücklich KEINE Messgröße** — sie in die Liste zu nehmen
hiesse, die **Providerimplementierung** zu messen statt das Modell.

### 5.2 Begründung — ANKERWIRKUNG, nicht Ausdrucksgrenze

**(i) Das Checker-Regelschema KANN alle sechs Kategorien tragen.** `predicate` ist
**optional** (`types.ts:44` — `predicate?: RulePredicate`; `parsePredicate` gibt bei
`undefined`/`null` **sofort** `undefined` zurück, `rules.ts:77`), und die eigene
Regeldatei prüft die **semantischen Kategorien über den `statement`-Wortlaut**
(Hauptprotokoll §3 Rev. 16: „**Alle vier `API_CONTRACT`-Regeln (R-SIG-1…4) prüfen
einheitlich über den `statement`-Wortlaut**, nicht über ein Protocol im Repo";
Rev. 18: die vier **R-PORT-Statements**). **DIESE KLARSTELLUNG MUSS DASTEHEN — die
gegenteilige Behauptung wäre unwahr.**

**(ii) Der Einwand ist die ANKERWIRKUNG.** Die einzige **maschinenprüfbare**
Prädikatsform ist eine **Import-Erlaubnisliste** (`rules.ts:80-82`: nur
`type === 'import-boundary'` mit `allowed_importers`), und **`kind` legt mit
`structural|semantic` die Achse vor, auf der E2 liegt** (`rules.ts:56`). Ein Modell,
das dieses Schema als `response_format` sieht, **wird zur Spiegelung gezogen** — also
zu dem, **was E1 als BEFUND vorhersagt**.

**(iii) Warum das Checker-Schema mit beschnittenen Feldern NICHT geht.** `kind` ist
**Pflichtfeld**: `rules.ts:55` `const kind = str('kind')`, und `str()` **wirft** bei
Nicht-String oder Leerstring (`rules.ts:49-53`); `types.ts:39` führt `kind: RuleKind`
**ohne `?`**. **Eine Ausgabe ohne `kind` parst nicht** — `parseArchitectureRules`
könnte dafür also **nicht das Wohlgeformtheits-Orakel** sein. **FUNDSTELLE, nicht
Präferenz.**

**(iv) Schema HANDGESCHRIEBEN, nicht pydantic-generiert.** Das in Z1 generierte trug
**weder `additionalProperties: false` noch `required`** (Befund 07.4: „Das gesendete
pydantic-Schema trägt an **keiner** Stelle `additionalProperties: false` und hat ein
**minimales** `required`"), und **zwei Kanten** (unter `dependencies` statt `relations`,
Mechanismus 1) sowie ein **Doppelpunkt-Schlüssel** (`"contained_modules:"`,
Mechanismus 2) **verschwanden geräuschlos** (Befund 07, 07.4). **Nebengewinn:** die
Schema-Bytes werden **unabhängig von der pydantic-Version**.

### 5.3 Wohlgeformtheits-Orakel **Z2-W** — zweistufig *(01.09.2026, S1-A1)*

1. **Schemakonformität ist unter `strict: true` providerseitig erzwungen und ist
   AUSDRÜCKLICH KEINE Messgröße** — sonst wird die **Providerimplementierung** gemessen,
   nicht das Modell. (Befund 07.4 zeigt, wie wenig das trägt: der dort gemessene
   Endpunkt fährt den strengen Prüfer **nicht**, HTTP 200 trotz fehlendem
   `additionalProperties`.)
2. **Gemessen wird eine hier registrierte, binäre, maschinelle Liste:**
   - `scope.components` **vollständig gegen `ist_modell.yaml` auflösbar**;
   - `statement` **nicht leer** und **keine Wiederholung** von `id` oder `category`;
   - `id` **im Lauf eindeutig**;
   - `category` **nicht-leer**.

   **Implementiert in `tools/run_z2.py` (S4)**, dort **selbstgetestet mit Positiv- und
   Negativfall je Bedingung**.

## 6. Bewertungskriterien (pro dedupliziertem Vorschlag)

> **Umbenennung der Bewertungsdimensionen, 01.09.2026 (Auftrag S1-A1), durchgängig in
> §5, §6, §7 und §10.** ~~K1~~ → **Z2-W** Wohlgeformtheit · ~~K2~~ → **Z2-P**
> Prüfbarkeit · ~~K3~~ → **Z2-G** Gehalt · ~~K4~~ → **Z2-Z** Zuordnung zum
> Abweichungstyp (Ebene 1) · ~~K5~~ → **Z2-R** Redundanz/Dedup (**eine Regel, kein
> Bewertungskriterium**).
> **Begründung:** `00_stand_und_entscheidungen.md` §9 führt K1–K5 **ausschließlich als
> Konfigurationsnamen** („Die Bezeichner K1–K5 sind ausschließlich Konfigurationsnamen",
> Protokoll Rev. 33 §9); die Kollision ist in `c3b_k2_nachtrag_findingbezug.md` **schon
> einmal aufgetreten**. In diesem Dokument bezeichnen **K2 und K3 weiterhin die beiden
> Modelle** (§2) — genau daher die Kollision.
> **Jede Zitatstelle, die „§6 K5" o. ä. nennt, bekommt einen Klammerzusatz; der
> WORTLAUT datierter Entscheidungen wird nicht geglättet.**

**Z2-W Wohlgeformtheit** ~~(K1)~~ — maschinell, **zweistufig nach §5.3**:
Schemakonformität unter `strict: true` ist **keine Messgröße**, gemessen wird die dort
registrierte binäre Liste. ~~Nicht wohlgeformte Vorschläge werden
für K2–K4 trotzdem manuell bewertet, sofern menschenlesbar (getrennt
ausgewiesen), damit Formatfehler nicht als Fähigkeitsdefizit zählen.~~ — *Wortlaut
nachgezogen 01.09.2026:* nicht wohlgeformte Vorschläge werden für **Z2-P, Z2-G, Z2-Z**
trotzdem manuell bewertet, sofern menschenlesbar (getrennt ausgewiesen), damit
Formatfehler nicht als Fähigkeitsdefizit zählen.

**`kind` (`structural` | `semantic`) — NEU als Dimension** *(01.09.2026, S1-A1)*: `kind`
wird **BEWERTET, nicht vorgegeben**. Die **Achse, auf der E2 liegt**, wird damit
**gemessen statt vom Schema gesetzt** (§5.2 (ii); `rules.ts:56`). Die Zuweisung ist
zugleich die eine Feldeinfügung der Umschreibung in §7 Punkt 8.

~~**Z2-P Prüfbarkeit** (K2) — Entscheidungsregel: *Ein Vorschlag ist prüfbar, wenn seine
Verletzung allein aus Imports + Signaturen (der Evidenzbasis des Extractors)
entscheidbar wäre.*~~
- ~~Positivbeispiele: „domain darf flask nicht importieren" (Import sichtbar);
  „Funktionen in domain/ dürfen keinen Request-Parameter annehmen" (Signatur
  sichtbar).~~
- ~~Negativbeispiele: „Repository-Funktionen dürfen keinen globalen State
  mutieren" (nur im Funktionskörper sichtbar); „Module sollen lose gekoppelt
  sein" (nicht operationalisiert).~~

— **überholt am 02.09.2026 (Auftrag S1-A1c), weil in S2c-2 STUFE 0b der Wegeleiter gezogen
wurde** (§3b, Stufe 0b, letzter Satz; §3a-2, Nachtrag 02.09.2026). **Der Alttext bleibt
vollständig stehen**, weil die Kriterien in §6 und §7 auf ihm registriert wurden.

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

~~**K3 Normativer Gehalt** — das Kernkriterium. Entscheidungsregel: *Ein Vorschlag
ist deskriptiv, wenn er logisch äquivalent zu einer Teilmenge der
Whitelist des Ist-Import-Graphen ist (er verbietet nur, was ohnehin nicht
vorkommt, und erlaubt, was vorkommt — Spiegelung). Er ist normativ, wenn er
mindestens eine im Ist nicht realisierte, aber realisierbare Konstellation
verbietet ODER eine semantische Eigenschaft fordert, die nicht aus dem
Import-Graphen folgt.*~~
- ~~Positivbeispiele (normativ): „api darf infrastructure nicht direkt
  importieren" wenn diese Kante im Ist nicht existiert, aber möglich wäre;
  „*_repository-Module enthalten keine Berechnungsfunktionen".~~
- ~~Negativbeispiele (deskriptiv): „api importiert application" als Gebot
  umformuliert; Aufzählung der vorhandenen Kanten als erlaubte Kanten.~~

— **überholt am 01.09.2026 (Auftrag S1-A1): die Gehaltsachse ist DREIWERTIG.**

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

> **Amendment (12.08.2026) — Begründung: Decision Record P.** Die Kategorien-Zuordnung
> der Regelvorschläge (K4 — *jetzt Z2-Z*), die Abdeckungsmatrix (§7.3 = §7 Punkt 3) und die vorregistrierte
> Erwartung E2 (§8) sind von den alten Kürzeln S1–S4/M1/M2 auf die **sechs
> Ebene-1-Abweichungstypen** des Hauptprotokolls umgestellt. Die Klassifikation der
> Regelvorschläge folgt damit **derselben Kodierung wie die Verletzungskategorien des
> Hauptexperiments**, damit die Ergebnisse beider Stufen — welche Regelklassen ein LLM
> *vorschlägt* (Z2/UF2) und welche Verletzungsklassen es *erkennt* (Z3/UF3) —
> aufeinander beziehbar bleiben. „Sonstige" bleibt als Auffangkategorie.

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

**Z2-R Redundanz/Dedup** ~~(K5)~~ — **eine Regel, kein Bewertungskriterium.** Zwei
Vorschläge sind Duplikate, wenn Kategorie,
Scope und Kernaussage übereinstimmen (Umformulierungen zählen als ein
Vorschlag). Dedup passiert pro Lauf UND über Läufe hinweg getrennt
ausgewiesen: pro-Lauf-Dedup für die Mengenangaben, laufübergreifende
Wiederkehr als Stabilitätsmaß (§7).

**Bewertungsablauf — EINZELBEWERTER, VERBLINDET** *(Fassung vom 31.08.2026,
Amendment §11)*: Alle Vorschläge aller Läufe werden gepoolt, anonymisiert (ohne
Modell-/Bedingungs-Label) und in randomisierter Reihenfolge von **einem** Bewerter
bewertet; die Zuordnung wird erst nach Abschluss der Bewertung aufgelöst (Verblindung
gegen Erwartung E2). Alle Grenzfälle landen mit Begründung in der Grenzfall-Tabelle
(Anhang B). **Die Kodierung ist damit eine Einzelkodierung ohne Reliabilitätsmaß**; was
an die Stelle des Maßes tritt, steht in den drei folgenden Punkten und als Threat
**T-Z2-7** in §10.

1. **Vollständiger Ausweis der Grenzfälle statt Zählung.** Jeder Grenzfall wird in
   **Anhang B** mit **Vorschlag-ID, Kriterium, Entscheidung und Begründung** geführt und
   im Befund **vollständig ausgewiesen** — nicht nur als Anteil gezählt. Die Tabelle ist
   Teil des berichteten Ergebnisses, nicht ein Anhang zur Ablage: sie macht jede
   Ermessensentscheidung einzeln nachprüfbar und damit widersprechbar.
2. **Ein Zweitbewerter ist OPTIONAL.** Steht einer zur Verfügung, wird er
   **ausschließlich auf die Grenzfallmenge** angesetzt (gleiche verblindete Darreichung),
   und das Ergebnis wird als **Übereinstimmung auf dieser Teilmenge** berichtet —
   ausdrücklich **nicht** als Reliabilitätsmaß der Gesamtkodierung. Eine Übereinstimmung
   auf der schwierigsten Teilmenge ist keine Stichprobe aus der Gesamtmenge und darf nicht
   als solche gelesen werden. Wird eine Zweitbewertung durchgeführt, wird das **vorab**
   festgehalten (vor Sichtung der eigenen Ergebnisse durch den Zweitbewerter).
3. **Kein Trigger, keine Pflicht.** Es gibt keine Grenzfallquote, ab der eine
   Zweitbewertung ausgelöst wird. Der Anteil der Grenzfälle wird berichtet, weil er
   informativ ist, aber er löst nichts aus.

~~**Bewertungsablauf:** Alle Vorschläge aller 12 Läufe werden gepoolt,
anonymisiert (ohne Modell-/Bedingungs-Label) und in randomisierter Reihenfolge
bewertet; die Zuordnung wird erst nach Abschluss der Bewertung aufgelöst
(Verblindung gegen Erwartung E2). Alle Grenzfälle landen mit Begründung in der
Grenzfall-Tabelle (Anhang B).~~

~~**Zweitbewerter-Regel (vorregistriert):** Übersteigt der Anteil der
Grenzfälle 20 % der deduplizierten Vorschläge, wird eine Zweitbewertung einer
Zufallsstichprobe von 20 Vorschlägen (oder aller, wenn < 20) durch den
fachlichen Betreuer bei Unisphere durchgeführt (nur K2/K3-Kriterien — *jetzt Z2-P/Z2-G*, gleiche
verblindete Darreichung); berichtet wird einfaches prozentuales Agreement.
Unterhalb des Triggers ist die Zweitbewertung optional; wird sie dennoch
durchgeführt, wird das vorab (vor Sichtung der eigenen Ergebnisse durch den
Zweitbewerter) festgehalten.~~
— **überholt am 31.08.2026 (Auftrag G1, Amendment §11).** Der Zweitbewerter-Trigger bei
20 % Grenzfällen **entfällt als Pflicht**; die Zweitbewertung durch den fachlichen
Betreuer bei Unisphere ist nicht zugesagt und darf nicht als vorregistrierte Zusage
stehenbleiben. An seine Stelle treten die drei Punkte oben.

## 7. Auswertung

Pro Modell × Bedingung:
1. Anzahl Vorschläge roh / dedupliziert.
2. Anteile: wohlgeformt (**Z2-W**), prüfbar (**Z2-P**), ~~normativ (K3)~~ **Gehalt
   (Z2-G) in allen drei Werten getrennt** — Spiegelung, negierte Spiegelung, normativ
   (§6) —, unklar; dazu die Verteilung der bewerteten Dimension **`kind`**.
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
4. **Stabilität:** Anteil der Vorschläge, die in ≥ 2 der 3 Läufe derselben
   Zelle wiederkehren (nach **Z2-R**-Äquivalenz, bis 01.09.2026 „K5").
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
6. ~~**B1-vs-B2-Kontrast:** rein deskriptive Gegenüberstellung der Punkte 1–4;
   keine Signifikanz-, keine Überlegenheitsaussage.~~
   — **NICHT AUSGEFÜHRT** (01.09.2026, S1-A1; B2 entfällt, §3 Punkt 3). Ausdrücklich
   **NICHT negativ ausgefallen**.
7. **Grenzfälle vollständig, nicht nur gezählt** *(neu am 31.08.2026, Amendment §11)*:
   Der Befund weist die **vollständige Grenzfall-Tabelle (Anhang B)** aus — je Grenzfall
   Vorschlag-ID, Kriterium, Entscheidung und Begründung —, zusätzlich zum Anteil der
   Grenzfälle an den deduplizierten Vorschlägen. Liegt eine optionale Zweitbewertung der
   Grenzfallmenge vor (§6), wird ihre Übereinstimmung **auf dieser Teilmenge** berichtet
   und als solche bezeichnet, nie als Reliabilitätsmaß der Gesamtkodierung.
8. **Sekundärgröße: LADBARKEIT** *(neu 01.09.2026, S1-A1)*. Berichtet wird die **Zahl
   der deduplizierten Vorschläge, die `parseArchitectureRules` nach MECHANISCHER
   Umschreibung annimmt**. Die Umschreibung ist **genau EINE Feldeinfügung** — `kind`;
   `id`, `category`, `scope`, `statement` und `severity` werden **unverändert**
   übernommen, `predicate` **bleibt leer** (zulässig: `types.ts:44`, `rules.ts:77`).
   **Ausdrücklich:** die `kind`-Zuweisung ist eine **BEWERTUNG** (Dimension aus §6), das
   Ergebnis ist **deskriptiv** und **KEIN Korrektheitsmaß**.
   **Zweck, wörtlich zu registrieren:** *E4 bleibt diskriminierend statt definitorisch
   wahr, und die Anbindung der Regelableitung an die Prüfstufe bleibt sichtbar.*
9. **Reihenfolge der Auszählung** *(neu 01.09.2026, S1-A1)*: **Die drei Läufe der Zelle
   K2 × B1 laufen VOLLSTÄNDIG, bevor irgendetwas bewertet wird** — erst dann ist die
   **Nachbesserungsregel (§4) prüfbar**, und erst dann steht **N₁** fest. **Die
   Volumenprobe ist damit ZELLE 1, nicht Lauf 1.** Das ist **KEINE Änderung der Sache**
   (die drei Läufe waren in §2 ohnehin registriert), sondern eine **Auszählregel**; ohne
   sie zählt jemand nach Lauf 1 aus und entscheidet zu früh. **N₁ selbst bleibt die
   PRO-LAUF-Dedup des ersten Laufs** (**Z2-R**), **nicht** die Dedup über drei Läufe —
   **die Schwellenrechnung der Gate-Notiz ruht darauf** (Gate-Notiz §5b: „N₁ = Zahl der
   deduplizierten Regelvorschläge **dieses einen Laufs**", §5c die Schwellen).

## 8. Vorregistrierte Erwartungen (falsifizierbar)

- ~~**E1:** Die Mehrheit der Vorschläge beider Modelle ist deskriptiv
  (Whitelist-Spiegelung)~~ — *nachgezogen 01.09.2026 (S1-A1) mit der dreiwertigen
  Gehaltsachse:* **E1:** Die Mehrheit der Vorschläge beider Modelle ist **EXTENSIONAL
  (Spiegelung oder negierte Spiegelung)** — Stufe-2-Entsprechung der
  Arbeitsteilungs-These und konsistent mit dem Mirror-Verhalten aus
  Befund 02/04. **Alle drei Werte werden getrennt berichtet** (§6, §7 Punkt 2).
- **E2:** Normative, semantische Vorschläge — Vorschläge der Typen
  `FORBIDDEN_SIGNATURE_TYPE`, `STRUCTURAL_PLACEMENT` und `API_CONTRACT` — sind
  selten und treten bei K3 (120B) häufiger auf als bei K2 (7B).
- ~~**E3 (nur B2, explorativ):** Auf dem komprimierten LLM-Ist-Modell sind die
  Scopes der Vorschläge gröber (Komponenten- statt Modulebene). Keine
  gerichtete Erwartung darüber hinaus.~~
  — **NICHT AUSGEFÜHRT** (01.09.2026, S1-A1; B2 entfällt, §3 Punkt 3). Ausdrücklich
  **NICHT negativ ausgefallen**.
- **E4:** Von besonderem Interesse ist, ob die abgeleiteten Regeln überhaupt
  Vorschläge des Typs `ABSENCE_REQUIRED` enthalten — also **erforderliche** statt
  verbotene Abhängigkeiten. Diese Kategorie kann die implementierte Rule-Engine
  nicht ausdrücken (sie emittiert ausschließlich `DERIVED:forbidden-edge` und
  `DERIVED:cycle`); ein Regelvorschlag dieses Typs wäre daher ein **eigener Befund
  zur Ausdrucksmächtigkeit des LLM-Pfads über die Erkennungsstufe hinaus** — das
  LLM formulierte dann eine Regelklasse, die der deterministische Pfad nicht
  prüfen kann. Keine gerichtete Häufigkeitserwartung; berichtet wird Vorkommen
  oder Nicht-Vorkommen je Modell und Bedingung.

## 9. Verhältnis zu Z3 (Nicht-Vermischung)

Z2-Vorschläge fließen **nicht** in die Z3-Evaluation ein; geprüft wird dort
ausschließlich gegen die vor Z2 eingefrorene Regeldatei. (Abgrenzungspunkt 4
der Zielsetzung; verhindert die in Umsetzungsplan §2 benannte Vermischung von
Regel-Ableiten und Regel-Prüfen.)

## 10. Threats to Validity

| ID | Threat | Umgang |
|---|---|---|
| T-Z2-1 | Einzelrater + Autorenschaft der Kriterien | vorab fixierte Entscheidungsregeln mit Beispielen (§6), Verblindung, **vollständig ausgewiesene** Grenzfall-Tabelle. ~~Zweitbewerter-Trigger~~ *(entfallen 31.08.2026, §11 — siehe T-Z2-7)* |
| T-Z2-2 | Prompt-Sensitivität: eine Prompt-Version = eine Stichprobe aus dem Prompt-Raum | Befunde gelten „unter diesem Prompt"; Nachbesserungsregel §4 |
| T-Z2-3 | Ein-Repo-Basis (synthetisches Testrepo) | Geltungsbereich explizit; Anschluss an 04.2-Caveat |
| T-Z2-4 | Modellfamilien-Confounder (7B vs. 120B ≠ nur Größe) | geerbt aus Befund 03; nur „Fähigkeitsspanne", keine Skalierungsaussage |
| T-Z2-5 | ~~B2-Kontrast mehrdimensional konfundiert (Ist-Modelle unterscheiden sich in mehr als einer Eigenschaft)~~ | ~~B2 nur explorativ; keine kausale Zuschreibung~~ — **gegenstandslos seit 01.09.2026 (S1-A1): B2 entfällt** (§3 Punkt 3). Der Threat wird **nicht gelöscht**, weil er das Design bis zu diesem Datum trug |
| T-Z2-6 | Format-Korsett misst Schema-Folgsamkeit mit | ~~K1 getrennt von K2–K4 berichtet~~ **Z2-W getrennt von Z2-P, Z2-G und Z2-Z berichtet**; nicht wohlgeformte, aber lesbare Vorschläge werden inhaltlich mitbewertet. **Nachgezogen 01.09.2026 (S1-A1): das Format-Korsett ist GEWECHSELT, nicht entfallen** — gemessen wird jetzt Folgsamkeit gegenüber dem **eigenen Umschlagformat** (§5.1), nicht mehr gegenüber dem Produktivschema. **Ergänzt 02.09.2026 (S1-A1c): dasselbe Muster liegt auf der EINGABEseite vor** — mit **Stufe 0b** ist die **Evidenzbasis von Z2-P gekürzt** auf **Importkanten des Ist-Modells + Signaturen der Faktenbasis** (§3a-2 Nachtrag 02.09.2026, §6). **Die Kürzung ist VORAB registriert** — Stufe 0b steht seit dem **01.09.2026 (S1-A1)** in §3b — und **aus einem FENSTERBEFUND gezogen** (**38 748 > 32 768**, Messung S2c-2), **NICHT nach Kenntnis der Ergebnisse**: zum Zeitpunkt des Ziehens existiert **kein einziger Z2-Lauf**. **Der gemessene Preis sind neun externe Importe** (acht `sqlalchemy.orm`, einer `typing`); ein Vorschlag, der auf einem von ihnen beruht, wird als **nicht entscheidbar MIT VERMERK DER URSACHE** geführt und **NICHT als Modellfehler** |
| **T-Z2-8** | **Die EINGABE trägt die sechs Kategorien strukturell** (neu 01.09.2026). Vier **reservierte Ports** in öffentlichen Signaturen (`TokenSigner`, `RateProvider`, `PaymentGateway`, `Clock`; Hauptprotokoll §3 Rev. 16 (A): „erscheinen in der Clean-Baseline in **genau einem** Modul — ihrem Träger — und dort in einer **öffentlichen Methodensignatur**"), die **Suffixkonventionen** `_repo` / `_query` / `_index` / `_models` (`customer_repo`, `session_repo`, `invoice_repo`; `invoice_query`; `legacy_token_index`, `legacy_order_index`, `legacy_invoice_index`; `*_models`), **geschützte Internals** (`depot.core.adapters.internal`, R-PROTECT-1) und **Zyklen mit genau zwei Komponenten** (R-CYCLE-2: `orders_services` / `orders_services_pricing`) — **und, ergänzt 02.09.2026 (Auftrag S1-A1b), die VERERBUNGSSTRUKTUR des Testrepos: zwölf `extends`-Kanten, in `x-triton-inner-artefact-relations` (1 Knoten, 4 Einträge) und `x-triton-cross-artefact-relations` (5 Knoten, 8 Einträge), Träger ausschliesslich Modulknoten (§3a-1 Nachtrag 02.09.2026, §3a-2)** | **Nicht heilbar, benannt.** Die **Abdeckungsmatrix (§7 Punkt 3) ist damit teils Eigenschaft des synthetischen Messobjekts, nicht des Modells.** Die Prompt-Auflage aus §4 (**keine Kategorie beim Namen**) deckt das **NICHT** ab — sie hält die Kategorien aus dem *Prompt*, nicht aus dem *Repositorium*. **Ergänzt 02.09.2026 (S1-A1b): das gilt AUCH für den nicht zuordenbaren Teil der Matrix** — Vorschläge mit Z2-Z-Wert **„keiner der sechs"** (§6, §7 Punkt 3) entstehen an einer Struktur, die **die Eingabe mitbringt** |
| **T-Z2-9** | **Mit dem eigenen Umschlagformat wird Schema-Folgsamkeit gegenüber dem Produktivschema NICHT mehr mitgemessen** (neu 01.09.2026), und die **Anbindung an die Prüfstufe** besteht nur noch über die **Sekundärgröße Ladbarkeit** (§7 Punkt 8) | Bewusst in Kauf genommen: die **Ankerwirkung** des Produktivschemas (§5.2 (ii)) zöge das Modell zu **genau dem Verhalten, das E1 als Befund vorhersagt**. Die Ladbarkeit hält die Anbindung **sichtbar**, ist aber **deskriptiv und kein Korrektheitsmaß**; zusammen mit T-Z2-6 ist zu lesen: das Korsett ist **gewechselt**, nicht entfallen. **Ergänzt 02.09.2026 (S1-A1c):** auf der **Eingabeseite** ist mit **Stufe 0b** ebenfalls gekürzt worden — **vorab registriert und aus einem Fensterbefund gezogen, nicht nach Kenntnis der Ergebnisse**. Einzelheiten und **gemessener** Preis in **T-Z2-6**, **§3a-2** (Nachtrag 02.09.2026) und **§6 (Z2-P)** |
| **T-Z2-7** | **Einzelkodierung ohne Reliabilitätsmaß** (neu 31.08.2026). Die Kodierung ist **vom Autor der Regeldatei und des Prompts** vorgenommen — dieselbe Person setzt das Soll, formuliert den Prompt und bewertet die Vorschläge | Verblindung und vorab fixierte Entscheidungsregeln (§6) bleiben; **die vollständig ausgewiesene Grenzfall-Tabelle (Anhang B) ist der Ersatz für ein Übereinstimmungsmaß, kein Äquivalent** — sie macht Ermessen sichtbar, sie misst es nicht. Getragen wird das von der **Evidenzstufe der Studie**: explorativ-klassifizierend, bewusst schwächer als Z1/Z3 (Kopf dieses Dokuments, `00_stand_und_entscheidungen.md` §5). **Eine konfirmatorische Aussage trüge es nicht** — und wird aus Z2 auch nicht abgeleitet |
| **T-Z2-10** | **PRIMING DURCH DAS AUSGABEBEISPIEL** (neu 02.09.2026, Auftrag S3). Der Prompt trägt ein **Ausgabebeispiel** (Anhang A, A3). Nach **Befund 07** ist es **unverzichtbar** — in Z1 fehlte es (**kein `{`, kein `[`** im Prompt), und **beide Modelle verfehlten die Feldsemantik**, **12 von 12 Läufen** ohne gültige Ausgabe. **Es primt aber unvermeidbar die ART der vorgeschlagenen Regeln**, und zwar in **vier** Hinsichten: das **Kategorie-Label**, die **Scope-Granularität**, die **Informationsart, auf die sich das `statement` beruft**, und die **`severity`** | **Nicht heilbar, benannt.** **Mitigation, vierfach und vorab registriert (Anhang A, A5 (c)):** das Beispiel stammt aus einer **fremden Domäne**, sein **Scope existiert im Testrepo nicht** (`shop.web`, `shop.jobs`), seine **Kategorie liegt ausserhalb der sechs** (`logging-discipline`), und die **Informationsart ist eine, die in der Eingabe VORKOMMT** (ein Import, Block 1) — **bewusst gewählt** gegen eine frühere Fassung, deren Beispielregel auf **Schreiben nach stdout** beruhte und damit vorgeführt hätte, dass Regeln über **nicht sichtbare Eigenschaften** erwünscht sind. **Die Mitigation verschiebt das Priming, sie hebt es nicht auf.** **Reichweite:** berührt **Z2-Z** (Abdeckung — über das Kategorie-Label und die Scope-Granularität), **Z2-P** (Prüfbarkeit — über die Informationsart) und die **`kind`-Achse** (§6; damit **E2**) |

## 11. Amendments

| Datum | Abschnitt | Änderung | Begründung |
|---|---|---|---|
| 12.08.2026 | §6 (K4 — *jetzt Z2-Z*), §7.3 (= §7 Punkt 3), §8 | Klassifikation der Regelvorschläge von S1–S4/M1/M2 auf die sechs Ebene-1-Abweichungstypen des Hauptprotokolls umgestellt („sonstige" bleibt Auffangkategorie); neue vorregistrierte Erwartung **E4** zu `ABSENCE_REQUIRED`-Vorschlägen ergänzt | Decision Record P — gemeinsame Kodierung für Regelableitung und Verletzungserkennung, damit beide Stufen aufeinander beziehbar bleiben. Vor dem ersten Z2-Lauf |
| **31.08.2026** | **§6 (Bewertungsablauf), §7 (neuer Punkt 7), §10 (T-Z2-1, neuer T-Z2-7)** | **Bewertung auf EINZELBEWERTER, VERBLINDET umgestellt.** Der **Zweitbewerter-Trigger bei 20 % Grenzfällen entfällt als Pflicht**; an seine Stelle treten: (1) vollständiger Ausweis jedes Grenzfalls in **Anhang B** mit Vorschlag-ID, Kriterium, Entscheidung und Begründung, im Befund ausgewiesen statt nur gezählt; (2) ein **optionaler** Zweitbewerter, ausschließlich auf die **Grenzfallmenge** angesetzt, berichtet als Übereinstimmung **auf dieser Teilmenge**, nicht als Reliabilitätsmaß der Gesamtkodierung; (3) neuer Threat **T-Z2-7** (Einzelkodierung ohne Reliabilitätsmaß, Kodierung durch den Autor von Regeldatei und Prompt). Alttext in §6 und in T-Z2-1 durchgestrichen sichtbar | **Auftrag G1, Gate-Notiz vom 31.08.2026** (`docs/planung/gate_notiz_2026-08-31.md`). Die Zweitbewertung durch den fachlichen Betreuer bei Unisphere ist **nicht zugesagt**; eine Pflichtregel, deren Erfüllung von einer nicht zugesagten fremden Verfügbarkeit abhängt, ist keine Vorregistrierung, sondern eine Hoffnung. Ehrlicher ist die Einzelkodierung mit **offengelegtem** Ermessen. **Vor dem ersten Z2-Lauf und vor dem Freeze dieses Dokuments** — das Dokument ist zum Zeitpunkt dieser Änderung **nicht eingefroren** (Kopf: „Eingefroren wird dieses Dokument (Commit-Hash) **vor** dem ersten Z2-LLM-Lauf") |

| **01.09.2026** | **Kopf; §2 (B2-Zeile, Läufe, Einheit der Auswertung, B1-Verweis); §3 (Punkt 3, Punkt 4, neuer Punkt 5); §3a und §3b (neu); §4 (Output-Format, Nachbesserungsregel); §5 (vollständig, neue §5.1–§5.3); §6 (Umbenennung, `kind` als Dimension, Z2-G dreiwertig, Zitatstellen); §7 (Punkte 2, 4, 5, 6, neue Punkte 8 und 9); §8 (E1, E3); §10 (T-Z2-5, T-Z2-6, neue T-Z2-8 und T-Z2-9)** | **Vierzehn Gegenstände.** **(1)** Kopfvermerk. **(2)** **Ausgabeformat ist ein eigenes, HANDGESCHRIEBENES Umschlagformat** mit `additionalProperties: false` und explizitem `required` (`id`, `category` frei, `scope.components[]` in Objektform, `statement`, `severity`) — **kein `kind`, kein `predicate`**. **(3)** Begründung als **ANKERWIRKUNG, nicht Ausdrucksgrenze**, in vier Punkten mit Fundstellen. **(4)** Neues **zweistufiges Wohlgeformtheits-Orakel Z2-W**; der Satz „Wohlgeformtheit (K1) entscheidet ausschließlich der vorhandene Parser" ist **durchgestrichen sichtbar ersetzt**. **(5)** Neue Sekundärgröße **Ladbarkeit** (§7 Punkt 8). **(6)** **B2 entfällt** — als **KÜRZUNG, nicht als ausgelöste Regel**; E3 und §7 Punkt 6 sind **NICHT AUSGEFÜHRT**, nicht negativ ausgefallen; Gesamtzahl der Läufe **12 → 6**. **(7)** **Asymmetriesatz** zum Kontextfenster (§3 Punkt 5). **(8)** **Umbenennung K1–K5 → Z2-W / Z2-P / Z2-G / Z2-Z / Z2-R**, durchgängig; **`kind` neu als bewertete Dimension**. **(9)** **Z2-G dreiwertig** (Spiegelung · negierte Spiegelung · normativ), E1 nachgezogen. **(10)** **Eingaben registriert:** `ist_modell.yaml` (Tritons eigener Exporter über den Editor, vier Laufparameter, Provenienzauflagen, Geltungsvermerk, zwei verworfene Rückfälle) und `input_facts.json` (Aufruf auf `<testrepo>/src`, Gegenprobe, Arbeitsteilung). **(11)** **Größenregel** mit Schwelle (≤ 24 000 Token bei Fenster 32 768, Reserve ≥ 8 000) und sechsstufiger Wegeleiter. **(12)** Zwei neue Threats **T-Z2-8** (die Eingabe trägt die sechs Kategorien strukturell) und **T-Z2-9** (Produktivschema-Folgsamkeit nicht mehr mitgemessen); **T-Z2-6 nachgezogen**. **(13)** **Nennerkorrektur** in §7 Punkt 5: **16** statt 6 autorenformulierte Statements. **(14)** **Nachbesserungsregel** präzisiert (erst mit drei Läufen auswertbar; überholte Läufe archiviert und als solche berichtet, **nicht** ungültig; N₁ neu gezählt, Schwelle unverändert) und **Auszählreihenfolge**: die Zelle läuft vollständig, bevor bewertet wird. | **Auftrag S1-A1.** Der Zuschnitt der Studie wird auf den entschiedenen Stand gebracht, **bevor** gemessen und **bevor** eingefroren wird: das Produktivschema würde das Modell durch seine **Ankerwirkung** zu genau dem Verhalten ziehen, das **E1 als Befund** vorhersagt (§5.2); die **gesättigte Baseline** (39/39 realisiert, 0 unbenutzt, 0 außerhalb, 0 Zyklen) macht die alte **zweiwertige** Gehaltsachse **in sich widersprüchlich** (§6); die **Erzeugung der Eingaben** und die **Größenregel** müssen **vor** der Messung feststehen, weil beide die Ausgabe verändern und am Artefakt nicht ablesbar sind; und **B2** ist nach Befund 07 **nicht mehr herstellbar** — die Kürzung wird als Kürzung geführt, mit **benanntem Verlust** und **ohne behaupteten Befund**. **Vor dem ersten Z2-Lauf und vor dem Freeze dieses Dokuments** — das Dokument ist zum Zeitpunkt dieser Änderung **nicht eingefroren** (Kopf: „Eingefroren wird dieses Dokument (Commit-Hash) **vor** dem ersten Z2-LLM-Lauf") |
| **02.09.2026** | **Kopf; §3a-1 (zwei Nachträge); §3a-2 (Arbeitsteilung, zwei Konsequenzen); §3b (Messinstrument, neue (a)–(e)); §6 (Z2-Z, zusätzlicher Wert); §7 Punkt 3; §10 (T-Z2-8)** | **Drei Gegenstände, alle aus dem Bericht zu S2b-2** (Commit **`2b0ff04`**; Fundstelle der Befunde **`data/z2/MANIFEST.md`**). **(1) §3b — DAS MESSINSTRUMENT DER GRÖSSENREGEL WIRD AUSGEWECHSELT.** `tools/z1_tokenizer.py` weist `data/z2/eingaben/ist_modell.yaml` durch **seinen eigenen Wächter** ab (`TokenizerUnavailable — is not pure ASCII`); Ursache ist das Zeichen `·` in jedem `subtitle`, und der gerenderte Prompt enthält das Ist-Modell, ist also **ebenfalls nicht ASCII**. Der unter Umgehung des Wächters erhaltene Wert **8 438** ist **kein Messwert**. Der alte Satz steht **durchgestrichen sichtbar** und ist durch **(a)–(e)** ersetzt: **(a)** primäre Messgröße ist die **serverseitig gemeldete Prompt-Tokenzahl** (`usage.prompt_tokens` / `prompt_eval_count`, Kaltlauf `max_tokens: 1`, lokaler Endpunkt, Zählweise von Z1-T und `tools/check_z1_delivery.py`), ausdrücklich registriert als **INSTRUMENTENMESSUNG, kein Z2-Lauf** — kein Budget, keine Archivierung, Ausgabe ungelesen und unbewertet, abgelegt nur Tokenzahl, Fenster, Modell, Endpunkt, Zeitstempel und SHA256 des gemessenen Textes; **(b)** **Messfenster 32 768** und **Kürzungsdetektor** (ungültig bei Gleichstand mit dem Fenster oder weniger als 64 Token Abstand; Z1: 4 281 gesendet, 2 050 gemeldet, ohne Fehler und ohne Logzeile), mit dem Satz, dass das Anheben **für die Messung** NICHT das Ziehen von **Stufe 1** der Wegeleiter ist; **(c)** Rückfall **additive Teilmessung**, Fehler ≤ N Token, N ausgewiesen; **(d)** **künftiges** Werkzeug **`tools/z2_tokenizer.py`** für die Lieferzusicherung in S4, mit **zwei vorab registrierten Toren** (T1: **4 281** auf dem Z1-Prompt `cb2fcefd…`; T2: **±0,5 %** gegen die serverseitige Zahl auf `ist_modell.yaml`) — **`z1_tokenizer.py` wird NICHT umgebaut**, seine Tore G1-G4 tragen die Z1-Hochrechnung; **(e)** **Geltungsbereich der Schwelle**: 24 000 bei Fenster 32 768 bindet auf **K2**, für **K3** wird die Zahl nur berichtet, und die Tokenzahlen beider Modelle werden **nie gegeneinander gerechnet**. **(2) §3a-1/§3a-2 — DIE EVIDENZBASIS WIRD UM ZWÖLF VERERBUNGSKANTEN ERWEITERT.** Die abgelegte Eingabe trägt `x-triton-inner-artefact-relations` (1 Knoten, 4 Einträge) und `x-triton-cross-artefact-relations` (5 Knoten, 8 Einträge), Label durchgehend **`extends`**, Träger ausschliesslich Modulknoten, **ausserhalb** von `perspectives[0].relations` und **ohne** Wirkung auf die 81 Importkanten. Die **Arbeitsteilung** in §3a-2 ist entsprechend präzisiert (Alttext durchgestrichen sichtbar). **Zwei Konsequenzen registriert:** ein Vorschlag, der keiner der sechs Kategorien entspricht, ist **ein Befund, kein Fehler** — **§7 Punkt 3** führt ihn als **nicht zuordenbar**, und **Z2-Z erhält dafür den Wert „keiner der sechs"** (§6, getrennt von „sonstige"); ferner ist **T-Z2-8 ergänzt** um die **Vererbungsstruktur des Testrepos**. **Die Kanten werden NICHT aus der Eingabe entfernt** — sie sind Teil eines gehashten Messeingangs (988 Zeilen, 42 959 B, SHA256 `146dbb05…36673`). **(3) §3a-1 — EINORDNUNG DES FORMBEFUNDS: FASSUNG A.** Der Exporter emittiert die zwei Knotenschlüssel **nur bei nichtleerem Inhalt** (`codeModelToIlograph.ts:224-225`); die rein lesende Vorablesung an `fixtures/rich_repo` (`ma-llm-arch-extractor` @ `5c0b65a`) ergibt **4 von 14** Klassendefinitionen mit Basisklasse und davon **0** mit einer **fixtureeigenen** Basisklasse. **Die Formidentität mit der Z1-Fixture ist damit NICHT verletzt** — das Merkmal war an der Fixture **nicht auslösbar** —, die Abweichung ist **ohne Annahme einer Exporter-Änderung** erklärt, und **T-Z1-4 wird hierfür NICHT in Anspruch genommen**. Der Vorbehalt „Exporterstand vom Erzeugungsdatum" bleibt **unberührt**. | **Auftrag S1-A1b.** Die drei Befunde müssen registriert sein **vor der Tokenmessung, vor dem ersten Z2-Lauf und vor dem Freeze dieses Dokuments** — das Dokument ist zum Zeitpunkt dieser Änderung **nicht eingefroren** (Kopf: „Eingefroren wird dieses Dokument (Commit-Hash) **vor** dem ersten Z2-LLM-Lauf"). Der Grund je Gegenstand: ein **Messinstrument, das den Messgegenstand abweist**, trägt die Schwelle nicht, und die Ersatzregel muss **vor** der Zahl feststehen, damit nicht die Zahl die Regel wählt; eine **Evidenzbasis, die mehr enthält als registriert ist**, machte einen regulären Modellvorschlag nachträglich zum „Fehler"; und ein **Formbefund ohne Einordnung** liesse im Manifest den Anschein einer Exporter-Änderung stehen, den die Vorablesung ausräumt. **`data/z2/` ist dabei NICHT angefasst** — die Eingabe bleibt bytegleich, ein Nachzug an `data/z2/MANIFEST.md` ist ein eigener Auftrag. |
| **02.09.2026** | **Kopf; §3a-2 (Evidenzbasissatz durchgestrichen, Nachtrag); §3b ((b) ergänzt um (b2)/(b3), (c) Erfahrungswert, neues (f)); §6 (Z2-P vollständig, Alttext durchgestrichen); §10 (T-Z2-6, T-Z2-9)** | **Drei Gegenstände, alle aus dem Lauf S2c-2** (Commit **`89b70e6`**; Fundstellen **`data/z2/MANIFEST.md`**, Block „Grössenregel angewandt", und **`data/z2/messungen/tokenmessung_2026-09-02.json`**). **(1) §3b — DER KÜRZUNGSDETEKTOR WIRD ERWEITERT.** Der in **(b)** registrierte Wortlaut **bleibt gültig und bleibt stehen** — er ist **nicht falsch, sondern unzureichend**: in S2c-2 meldete die Messung des vollen Prompts (**M6**) **16 386** Token, **WENIGER als die Messung der darin enthaltenen Faktenbasis allein** (**M5, 29 095**), und das registrierte Kriterium (Gleichstand mit dem Fenster oder weniger als **64** Token Abstand, Verdachtsbereich ab **32 705**) **sprach NICHT an** — 16 386 liegt **16 382** Token unter dem Fenster, die Kürzung war unter dem bisherigen Detektor **unsichtbar**. Ergänzt werden **zwei gleichrangige, je hinreichende** Kriterien: **(b2) MONOTONIE** — enthält eine Nutzlast eine andere vollständig, muss ihre gemeldete Tokenzahl mindestens so gross sein, **jede Verletzung heisst UNGÜLTIG**, und der volle Prompt wird **stets gegen die Einzelmessung seiner grössten Komponente** geprüft, nie allein bewertet; **(b3) HALBFENSTER-SIGNATUR** — **UNGÜLTIG** bei Gleichstand mit **`Fenster / 2 + 2`** oder weniger als **64** Token darunter, belegt an **zwei unabhängigen Punkten** (**32768/2+2 = 16 386**, S2c-2 M6; **4096/2+2 = 2 050**, Z1 aktenkundig, **4 281 gesendet**). **EVIDENZEINORDNUNG, verbindlich mitregistriert:** dass der Server auf die **HALBE** Fenstergrösse kürzt, ist **ABGELEITET** — zwei übereinstimmende Messpunkte, **keine Bestätigung aus Quellcode oder Dokumentation von Ollama 0.32.15**; **als Regularität gemessen, als Mechanismus nicht**, und diese Unterscheidung ist **in jeder Verwendung des Kriteriums zu wahren**. Ferner ist **(c) als Erfahrungswert vermerkt** — in S2c-2 angewandt, **N = 3**, in **drei ungekürzten Kontrollfällen auf das Token genau** (Fehler **≤ 3**) —, **die Regel selbst bleibt unverändert**. **NACHZUG AN DIE LIEFERZUSICHERUNG**, hier registriert und **in S4 umzusetzen**: der Wächter von **`tools/run_z2.py`** prüft **nicht nur Gleichstand mit dem Fenster**, sondern **(b2) und (b3) mit**; ein Lauf, dessen gemeldete Prompt-Tokenzahl eines der **drei** Kriterien erfüllt, **bricht ab und wird nicht als Lauf gezählt**. **(2) §3a-2 UND §6 (Z2-P) — DIE EVIDENZBASIS WIRD NACH DEM ZIEHEN VON STUFE 0b NACHGEZOGEN**, wie §3b, Stufe 0b, letzter Satz es verlangt: **„entscheidbar allein aus den IMPORTKANTEN DES IST-MODELLS und den SIGNATUREN der Faktenbasis"** statt **„aus Imports + Signaturen"**; der Alttext steht in beiden Abschnitten **durchgestrichen sichtbar**. **BEFUND:** in S2c-2 sind **Stufe 0** (Docstrings, leere `__init__.py`) **und Stufe 0b** (Importblöcke) gezogen worden; die abgelegte Eingabe `data/z2/eingaben/input_facts.json` trägt **52 Records OHNE `imports`-Blöcke und MIT Signaturen**. **PREIS, gemessen statt angenommen:** das Testrepo verwendet **ausschliesslich `import a.b.c`** — **Aliasnamen 0**, **`from X import Y` mit `names[]` 0**, **relative Importe 0**; von **90 Importfakten** haben **81** ein Ziel in `depot.*`, und das Ist-Modell führt **genau 81 Relationen mit 81 eindeutigen `(from,to)`-Paaren** — **dieselbe Menge, eins zu eins**. **Verloren gehen ausschliesslich die NEUN externen Importe:** **acht `sqlalchemy.orm`** und **einer `typing`** (in `depot.core.ports`). **KONSEQUENZ, ausdrücklich:** ein Vorschlag, dessen Prüfbarkeit von einem **EXTERNEN** Import abhängt, ist aus der Eingabe **nicht entscheidbar**; Framework-Typen bleiben über die **Signaturen** sichtbar, nicht mehr über eine Importliste. Bewertet wird ein solcher Vorschlag unter Z2-P **als nicht entscheidbar, MIT VERMERK DER URSACHE** — **kein Modellfehler, sondern eine Folge der registrierten Kürzung**. **T-Z2-6 und T-Z2-9 sind entsprechend ergänzt:** die Kürzung ist **vorab registriert** (Stufe 0b steht seit **01.09.2026, S1-A1**, in §3b) und **aus einem Fensterbefund gezogen** (**38 748 > 32 768**), **nicht nach Kenntnis der Ergebnisse** — zum Zeitpunkt des Ziehens existiert **kein einziger Z2-Lauf**. **(3) §3b — DAS INSTRUKTIONSBUDGET R1 WIRD REGISTRIERT UND VERSCHÄRFT (neues (f)).** Der volle Prompt misst nach den gezogenen Stufen 0 und 0b **24 104 Token** bei einer Instruktion von **1 200** Token; die vorregistrierte Schwelle von **24 000** ist damit um **104 Token ÜBERSCHRITTEN**. **DIE SCHWELLE BLEIBT UNVERÄNDERT BEI 24 000** — sie **nach Kenntnis der Zahl 24 104** anzuheben oder durch ihre Begründung (**Generat-Reserve ≥ 8 000**, hier mit **8 664** erfüllt) zu ersetzen, **wäre Nachverhandlung und ist ausgeschlossen**. **Verschärft wird stattdessen das Instruktionsbudget**, das **erst am 02.09.2026 in S2c-2 gesetzt** wurde und **selbst keine vorregistrierte Grösse** ist: **OBERGRENZE 1 000 Token, BINDEND für Anhang A** (bisher **1 200**); **ZIELGRÖSSE rund 700 Token, unverändert und NICHT bindend**. Begründung: der **gemessene Kipppunkt** liegt bei **1 096** Token, **1 000** lässt **96 Token Sicherheit** für die Messung des **tatsächlichen** Anhang A und liegt weiter deutlich über der Zielgrösse; **erwarteter voller Prompt bei 1 000: rund 23 904 Token**; die Begründung der Zielgrösse bleibt (**in Z1 kippte die Formatgültigkeit an 909 Zeichen** Instruktionstext). **Die Verschärfung zieht KEINE weitere Stufe der Wegeleiter:** Messobjekt unverändert (**nicht Stufe 3**), Modellklassen-Achse erhalten (**nicht Stufe 4**), Signaturen erhalten (**nicht Stufe 2**), **E2 und E4 unberührt**. **GEZOGENER STAND der Wegeleiter, abschliessend festgehalten:** **Stufe 1** (Fenster **32 768**) **wirksam** seit der Umgebungsänderung vom 02.09.2026 · **Stufe 0 gezogen** · **Stufe 0b gezogen** · **Stufen 3, 4 und 2 NICHT gezogen**. **ZWINGENDE AUFLAGE AN S3:** nach dem Schreiben von Anhang A wird der **VOLLE Prompt mit dem tatsächlichen Instruktionstext gemessen** (Verfahren **(a)–(c)**, Detektor **einschliesslich (b2) und (b3)**); **hält er die 24 000 nicht, wird ANHANG A GEKÜRZT, NICHT die Schwelle bewegt** — Messung und Ergebnis gehen **vor dem Freeze** nach `data/z2/messungen/` und in `data/z2/MANIFEST.md`. **NACHRICHTENSTRUKTUR (R3) festgeschrieben:** **zwei Nachrichten** — **`system`** trägt die Instruktion, **`user`** trägt **Block 1 (Ist-Modell)** und **Block 2 (Faktenbasis)** mit den in `data/z2/MANIFEST.md` **wörtlich abgelegten Blocküberschriften**; weicht Anhang A davon ab, **ist die Messung zu wiederholen**. **Rahmungsaufwand als Erfahrungswert:** die Differenz zwischen dem vollen Prompt und der Summe seiner Teile betrug **−14 Token**, weil eine eigene `system`-Nachricht den **Standard-System-Prompt ersetzt** (**13 gegen 29** Token, je gemessen), dem **+17** und **+14** Token für die zwei Trennzeilen gegenüberstehen. | **Auftrag S1-A1c. DIES IST DAS LETZTE AMENDMENT VOR DEM FREEZE.** Alle drei Gegenstände sind registriert **vor dem Schreiben von Anhang A, vor dem ersten Z2-Lauf und vor dem Freeze dieses Dokuments** — das Dokument ist zum Zeitpunkt dieser Änderung **nicht eingefroren** (Kopf: „Eingefroren wird dieses Dokument (Commit-Hash) **vor** dem ersten Z2-LLM-Lauf"). Der Grund je Gegenstand: ein **Detektor, der die tatsächlich eingetretene Kürzung durchlässt**, taugt als Wächter der Läufe nicht, und die Ergänzung muss **vor** dem ersten Lauf stehen; eine **Evidenzbasis, die im Protokoll weiter mehr nennt, als die Eingabe trägt**, machte einen aus der Kürzung folgenden Befund nachträglich zum „Modellfehler"; und ein **Budget, das die vorregistrierte Schwelle reissen lässt**, ist zu verschärfen, **damit die Schwelle selbst unangetastet bleibt** — nicht umgekehrt. **`data/z2/` ist dabei NICHT angefasst** — keine Eingabe, keine Messung, kein Manifest, kein Hash. |
| **02.09.2026** | **Kopf; §2 (Zeile B1); §5.1 (Nachtrag `minItems`); §10 (neuer T-Z2-10); Anhang A (vollständig)** | **Anhang A eingesetzt und drei Nachträge.** **(1) ANHANG A — der Platzhalter ist eingelöst**, Alttext durchgestrichen sichtbar. Sechs Teile: **A1** Zweck und Status (eine Prompt-Version, im Wortlaut Teil dieses Dokuments, eingefroren vor dem ersten Z2-Lauf; Nachbesserungsregel aus §4, inhaltliches Nachsteuern verboten) · **A2** Nachrichtenstruktur nach **R3** — zwei Nachrichten, `system` trägt die Instruktion aus A3, `user` trägt Block 1 und Block 2 mit den in `data/z2/MANIFEST.md` **wörtlich abgelegten** Blocküberschriften und der dort abgelegten **Zusammensetzungsformel**, beide unverändert übernommen · **A3** **der Prompt im Wortlaut**, englisch (R2) · **A4** **das gesendete JSON-Schema**, aufgebaut aus §5.1: fünf Felder, `additionalProperties: false` auf jeder Objektebene, explizites `required` für alle fünf, `severity` als Enum, **kein `kind`, kein `predicate`**, dazu **`minItems: 1`** · **A5** **Begründung der Auflösung** in vier Punkten — **Normativität dreimal in VERSCHIEDENER Form** (weil nach Befund 07 eine dreimal **wörtlich** wiederholte Anweisung wirkungslos war), **keine Kategorie beim Namen** (die Auflage schützt die Abdeckungsmatrix §7 Punkt 3 und verbietet **nicht**, die Feldsemantik zu bestimmen; `category` bleibt frei), **Ausgabebeispiel** (es fehlte in Z1, 12 von 12 Läufen ungültig; eine Regel, fremder Scope, Kategorie ausserhalb der sechs, und **die Informationsart kommt in der Eingabe vor** — bewusst gegen eine frühere Fassung mit stdout-Beispiel, die Z2-P und die `kind`-Achse geprimt hätte), **keine Zielzahl** (N₁ ist Messgröße, Gate-Notiz §5c; dass keine Zahl genannt ist, ist selbst Registrierungsgegenstand) · **A6** **externe Gegenlesung** vor dem Freeze durch ein projektfremdes Modell gegen die vier Auflagen aus §4: **drei Änderungen übernommen** (unescapter Zeilenumbruch im `statement` des Beispiels, „given file" → „the codebase", `minItems: 1`), **NICHT übernommen jede Verschärfung der Normativitätsanweisung**, weil sie das Kernkriterium **Z2-G** in die Intervention einbaute; **als Qualitätsschritt vermerkt, NICHT als Evidenz**. **(2) §5.1 — `minItems: 1`** auf `rules` und auf `scope.components`, additiv: ohne die Auflage ist `{"rules": []}` formal gültig, eine leere Antwort wäre unter **Z2-W nicht als Ausfall erkennbar** und **N₁ = 0 nicht von einem Modellbefund unterscheidbar**; **keine Zielzahl, keine Obergrenze**, **§5.3 bleibt unverändert**, weil `minItems` providerseitig erzwungen und dort ausdrücklich **keine Messgröße** ist. **(3) §2 — Evidenzbasis der Zeile B1 nachgezogen** von „AST-Fakten (Imports + Signaturen)" auf **Importkanten des Ist-Modells (Block 1) + Signaturen der Faktenbasis (Block 2)**; Fundstellen §3a-2 und §6 (Z2-P) in der Fassung vom 02.09.2026 (`bf6c6e0`), Ursache **Stufe 0b** der Wegeleiter; Alttext durchgestrichen sichtbar. **(4) §10 — neuer T-Z2-10, Priming durch das Ausgabebeispiel**: unverzichtbar nach Befund 07, primt aber Kategorie-Label, Scope-Granularität, Informationsart und `severity`; Mitigation fremde Domäne, nicht existierender Scope, Kategorie ausserhalb der sechs, Informationsart aus der Eingabe; **nicht heilbar, benannt**; Reichweite **Z2-Z**, **Z2-P** und die **`kind`-Achse (E2)**. **(5) DIE MESSUNG nach §3b (f):** die `system`-Nachricht allein misst **509 gemeldet / 480 netto** (**M10**) — **Obergrenze 1 000 bindend und Zielgröße rund 700 beide gehalten**; der **volle Prompt nach R3** misst **23 405 Token** (**M11**), und der **Kürzungsdetektor spricht in keinem seiner DREI Kriterien an** (Fensterabstand **9 363**; Monotonie gegen die Einzelmessung der GEZOGENEN Faktenbasis **14 451** (**M11a**) und gegen `ist_modell.yaml` allein **8 467** (M3); Halbfenster-Signatur **16 386**, Abstand **7 019**) — **eine additive Teilmessung nach §3b (c) war NICHT erforderlich**. **URTEIL (M12): die vorregistrierte Schwelle von 24 000 Token ist GEHALTEN, mit 595 Token Reserve**, und die **Generat-Reserve** bis zum Fenster beträgt **9 363 ≥ 8 000**. **Die Schwelle ist nicht bewegt und Anhang A nicht gekürzt worden.** Messung abgelegt in `data/z2/messungen/tokenmessung_2026-09-02.json` (M10, M10g, M11a, M11, M12) und in `data/z2/MANIFEST.md`, Block **„Anhang A gemessen"**. | **Auftrag S3.** Anhang A ist der **letzte offene Teil** des Protokolls; §4 verlangt seinen **Wortlaut als Teil dieses Dokuments vor dem Freeze**, und §3b (f) verlangt, dass der **volle Prompt mit dem tatsächlichen Instruktionstext** gegen die Schwelle **gemessen** wird, **bevor** eingefroren wird — hielte er sie nicht, wäre **Anhang A zu kürzen, nicht die Schwelle zu bewegen**. Die drei Nachträge stehen **vor** dem Freeze, weil jeder von ihnen sonst nachträglich wäre: **`minItems: 1`** ist Teil des **gesendeten** Schemas und damit der Intervention; die **Evidenzbasis in §2** war die **einzige verbliebene aktive Stelle**, die nach dem Ziehen von Stufe 0b noch „Imports + Signaturen" nannte; und ein **Threat, der erst nach den Läufen benannt wird**, ist keine Vorregistrierung. **Der Satz „DIES IST DAS LETZTE AMENDMENT VOR DEM FREEZE" aus S1-A1c ist damit überholt** — er steht durchgestrichen sichtbar im Kopf. **Das Dokument ist zum Zeitpunkt dieser Änderung NICHT eingefroren**; der Freeze folgt unmittelbar als eigener Commit. |


## Anhang A — Prompt (vor Freeze einzufügen)

~~*[Wortlaut des Z2-Prompts; wird vor dem Einfrieren dieses Dokuments ergänzt.]*~~
— **eingelöst am 02.09.2026 (Auftrag S3).** Der Platzhalter bleibt **durchgestrichen
sichtbar** stehen, weil die Freeze-Reihenfolge des Kopfes auf ihm registriert ist.

### A1 Zweck und Status

Dieser Anhang trägt **die eine Prompt-Version** der Studie, **im Wortlaut Teil dieses
Dokuments** (§4, erster Punkt). Er ist **vor dem ersten Z2-Lauf** geschrieben und wird
**mit diesem Dokument eingefroren**; der Freeze-Vermerk steht im Kopf. Gemessen ist er
**gegen die vorregistrierte Schwelle**, bevor er eingefroren wurde (§3b (f), Auflage an
S3; Messung M10/M11/M12 in `data/z2/messungen/tokenmessung_2026-09-02.json` und
`data/z2/MANIFEST.md`, Block „Anhang A gemessen").

**Nachbesserungsregel (§4), hier wiederholt, weil sie den Status dieses Anhangs
bestimmt:** höchstens **EINE** Prompt-Revision, und **nur bei technischem Scheitern** —
Format-Invalidität in **mehr als 50 %** der Läufe einer Bedingung, auswertbar erst, wenn
**alle drei Läufe** der Zelle vorliegen. **Inhaltliches Nachsteuern ist VERBOTEN**: ein
„mehr semantische Regeln bitte" nach Sicht der ersten Ausgaben machte den Befund zur
Folge des Nachsteuerns. Jede Revision ist ein **Amendment (§11)**; die Zelle beginnt mit
dem revidierten Prompt **neu**, die Läufe des überholten Prompts bleiben **archiviert und
gehasht** und werden als Läufe des überholten Prompts berichtet — **nicht als ungültig**.

### A2 Nachrichtenstruktur

**ZWEI Nachrichten**, registriert als **R3** in §3b (f):

- die **`system`**-Nachricht trägt **die Instruktion** — den Wortlaut aus **A3**,
  zeichengleich;
- die **`user`**-Nachricht trägt **Block 1 (Ist-Modell)** und **Block 2 (Faktenbasis)**.

Die **Blocküberschriften** sind die in `data/z2/MANIFEST.md` **wörtlich abgelegten**
(Block „Grössenregel angewandt", Abschnitt *Trennzeilen, wörtlich — sie gelten auch für
Anhang A*) und werden hier **unverändert übernommen, nicht neu formuliert**:

```
### BLOCK 1 - CURRENT ARCHITECTURE MODEL (Ilograph YAML)
### BLOCK 2 - EXTRACTED CODE FACTS (JSON)
```

Die **Zusammensetzungsformel** der `user`-Nachricht, ebenfalls wörtlich aus dem Manifest,
deterministisch:

```python
f"{BLOCK1}\n\n{ist_modell.rstrip()}\n\n{BLOCK2}\n\n{faktenbasis.rstrip()}\n"
```

Dabei ist `ist_modell` der Inhalt von `data/z2/eingaben/ist_modell.yaml` und
`faktenbasis` der von `data/z2/eingaben/input_facts.json` — der Fassung **nach den
gezogenen Stufen 0 und 0b** (§3b, Wegeleiter). **Weicht ein Lauf von dieser Struktur ab,
ist die Messung zu wiederholen** (§3b (f), R3).

### A3 Der Prompt

**Sprache: Englisch** (R2). Der folgende Wortlaut ist **der Inhalt der
`system`-Nachricht**, zeichengleich:

```
You are a software architect reviewing a Python codebase.

You will receive two blocks of input:
BLOCK 1 is a model of the code's current structure: packages, modules,
the classes and functions they contain, and the import and inheritance
edges that exist between them.
BLOCK 2 lists, for each module, the signatures of its classes and functions.

Your task is to PROPOSE ARCHITECTURE RULES for this codebase.

A rule states what SHOULD hold or SHOULD BE FORBIDDEN. Propose a rule
even when the current code already satisfies it — the point is not to
describe what the code does, but to state a constraint a reviewer could
enforce against future changes. Do not summarise the input.

Base your rules on what you can see in the two blocks, but you are not
limited to restating it. Consider what a codebase of this shape should
require, and where a plausible future change would be a mistake.

Return one JSON object with a single key "rules", holding an array.
Each element has exactly these fields:

  "id"       a short unique identifier for this rule within your answer
  "category" a short label you choose yourself, naming the kind of
             constraint this rule expresses. Use whatever labels fit the
             rules you propose; they are not taken from a fixed list.
  "scope"    an object with one key, "components", holding one or more
             names taken verbatim from BLOCK 1 — the parts of the
             codebase the rule applies to
  "statement" one or two sentences of plain English stating the rule.
             This field carries the rule: it must be specific enough
             that a reviewer could decide whether the codebase violates
             it. Do not restate the id or the category here.
  "severity" either "error" or "warning"

Example of the required shape, for an unrelated codebase:

{"rules": [
  {"id": "R1",
   "category": "logging-discipline",
   "scope": {"components": ["shop.web", "shop.jobs"]},
   "statement": "Modules in these components must not import the standard logging module directly. They obtain a logger from the shared logging helper instead.",
   "severity": "warning"}
]}

Output the JSON object and nothing else. No prose before or after it, no
markdown fences, no fields other than the five listed above.
```

### A4 Das gesendete JSON-Schema

Das folgende Schema ist **Teil des eingefrorenen Anhangs**. Es ist **handgeschrieben**
(§5.2 (iv)), aufgebaut aus der Feldtabelle in **§5.1** und um **`minItems: 1`** ergänzt
(§5.1, Nachtrag 02.09.2026). Es trägt `additionalProperties: false` **auf jeder
Objektebene**, ein **explizites `required` für alle fünf Felder**, `severity` als
**Enum** — und **KEIN `kind`, KEIN `predicate`** (§5.1, §5.2 (iii)).

```json
{
  "name": "architecture_rules",
  "strict": true,
  "schema": {
    "type": "object",
    "additionalProperties": false,
    "required": ["rules"],
    "properties": {
      "rules": {
        "type": "array",
        "minItems": 1,
        "items": {
          "type": "object",
          "additionalProperties": false,
          "required": ["id", "category", "scope", "statement", "severity"],
          "properties": {
            "id": {"type": "string"},
            "category": {"type": "string"},
            "scope": {
              "type": "object",
              "additionalProperties": false,
              "required": ["components"],
              "properties": {
                "components": {
                  "type": "array",
                  "minItems": 1,
                  "items": {"type": "string"}
                }
              }
            },
            "statement": {"type": "string"},
            "severity": {"type": "string", "enum": ["error", "warning"]}
          }
        }
      }
    }
  }
}
```

**`category` trägt bewusst KEIN Enum** — die Kategorienabdeckung soll **Befund** sein,
nicht **Prompt-Folge** (§5.1, §4; Begründung in A5 (b)). Das **Beispiel aus A3 ist gegen
dieses Schema gültig**; das ist vor dem Einfrieren maschinell geprüft worden (A5 (c),
Prüfung (ii)).

### A5 Begründung der Auflösung

Dieser Abschnitt hält fest, **wie** der Wortlaut die vier Auflagen aus **§4** auflöst —
und **warum jeweils so und nicht anders**. Er ist der inhaltlich tragende Teil dieses
Anhangs: der Prompt ist die **Intervention** der Studie, und was an ihm registriert ist,
kann nachher nicht mehr als Fund ausgegeben werden.

**(a) NORMATIVITÄT (§4).** Die Auflage — der Prompt fordert **normative** Regeln, nicht
die Beschreibung des Ist-Zustands — steht **dreimal, in verschiedener Form**:

1. als **Definition**: „A rule states what SHOULD hold or SHOULD BE FORBIDDEN";
2. als **Negation**: „the point is not to describe what the code does" und „Do not
   summarise the input";
3. als **Handlungsanweisung**: „Propose a rule even when the current code already
   satisfies it" und „where a plausible future change would be a mistake".

**Grund für die Dreifachform, und zwar für die VERSCHIEDENHEIT der drei Formen:** nach
**Befund 07** war eine **dreimal WÖRTLICH wiederholte** Anweisung **wirkungslos** — die
Granularität der Relationsendpunkte war in `prompt.py` an drei Stellen verlangt
(`:27`, `:28`, `:43-45`) und wurde in **sechs bytegleichen K2-Läufen** in **0 von 11**
Relationsendpunkten eingehalten. Die Wiederholung desselben Satzes ist also **kein
Wirkmittel**; wiederholt wird hier der **Gehalt**, nicht der **Wortlaut**.

**(b) KEINE KATEGORIE BEIM NAMEN GENANNT (§4).** Der Prompt nennt **keinen** der sechs
Ebene-1-Abweichungstypen und **keine Paraphrase** davon. **Was die Auflage schützt:** die
**Abdeckungsmatrix (§7 Punkt 3)**. Nennte der Prompt die sechs Typen als abzudeckende
Taxonomie, wäre jede Zelle der Matrix **Prompt-Folge statt Befund**, und **E2** mässe die
Aufzählung im Prompt.

**Was die Auflage NICHT verbietet:** die **Feldsemantik zu bestimmen**. Dass `category`
ein „short label" ist, das der Kategorie **einer Regel** einen Namen gibt, ist eine
Aussage über das **Feld**, nicht über die **Taxonomie**. **`category` bleibt ausdrücklich
frei** — „Use whatever labels fit the rules you propose; they are not taken from a fixed
list" —, und dieser Satz ist **Teil der Auflage, nicht ihre Verletzung**: ohne ihn
erriete das Modell ein **implizites Vokabular**, das es für erwartet hielte, und die
Kategorien wären wieder Prompt-Folge, nur unausgesprochen.

**(c) DAS AUSGABEBEISPIEL.** In **Z1 fehlte** ein Ausgabebeispiel — der dortige Prompt
enthielt **kein `{` und kein `[`** —, und **beide Modelle verfehlten die Feldsemantik**:
**12 von 12 Läufen** ohne gültige Ausgabe (**Befund 07**). Der Anhang trägt deshalb ein
Beispiel. Es ist so gewählt, dass es **so wenig wie möglich vorgibt**:

- es zeigt **EINE** Regel, nicht mehrere — ein zweites Beispiel legte eine Menge nahe;
- sein **Scope existiert im Testrepo nicht** (`shop.web`, `shop.jobs`) — er stammt aus
  einer **fremden Domäne**;
- seine **Kategorie liegt ausserhalb der sechs** (`logging-discipline`).

**AUSDRÜCKLICH ZU REGISTRIEREN — die Informationsart, auf die sich die Beispielregel
beruft.** Die gezeigte Regel stützt sich auf einen **Import** — also auf eine
Informationsart, die **in Block 1 vorkommt** —, nicht auf eine, die **nirgends in der
Eingabe steht**. Das war eine **bewusste Wahl** gegen eine frühere Fassung, deren
Beispielregel auf **Schreiben nach stdout** beruhte: jene hätte vorgeführt, dass Regeln
über **nicht sichtbare Eigenschaften** erwünscht sind, und damit **Z2-P (Prüfbarkeit)**
und die **`kind`-Achse** geprimt. **Das Restrisiko bleibt** — ein Beispiel primt, welche
Art von Regel als erwünscht gilt, und diese Wahl verschiebt es nur — und ist als
**T-Z2-10** (§10) geführt.

**(d) KEINE ZIELZAHL.** Der Prompt nennt **keine Zahl** und **keine Mengenangabe** — kein
„propose at least N rules", kein „a handful", kein „as many as you can". **Grund:**
**N₁ ist Messgröße** und entscheidet über den **Umfang der Studie** (Gate-Notiz §5c);
eine Zahl im Prompt nähme diese Entscheidung **vorweg** und machte N₁ zur Antwort auf die
eigene Vorgabe. **Dass keine Zahl genannt ist, ist selbst REGISTRIERUNGSGEGENSTAND** —
sonst liesse sich hinterher nicht mehr unterscheiden, ob die Zahl der Vorschläge eine
Eigenschaft des Modells oder eine des Prompts ist.

**`minItems: 1` ist KEINE Zielzahl.** Es schliesst **allein den trivialen Nullfall** aus
— eine leere `rules`-Liste bzw. ein leeres `components`-Feld —, nennt **keine erwartete
Menge** und hat **keine Obergrenze** (§5.1, Nachtrag 02.09.2026).

### A6 Externe Gegenlesung

Der Wortlaut ist **vor dem Freeze** von einem **projektfremden Modell** gegen die **vier
Auflagen aus §4** gegengelesen worden. **Übernommen wurden drei Änderungen:** der
**unescapte Zeilenumbruch** im `statement` des Beispiels — er machte das Vorbild zu
**formal ungültigem JSON**, bei einem 7B-Modell ein Formatrisiko —, die Ersetzung von
„given file" durch **„the codebase"**, weil die meisten Architekturregeln **Relationen**
betreffen und nicht eine Datei, und **`minItems: 1`** im Schema. **Ausdrücklich NICHT
übernommen wurde jede Verschärfung der Normativitätsanweisung:** Sätze, die
**Spiegelung** des Ist-Zustands oder deren **Negation** untersagen, bauten das
**Kernkriterium Z2-G** in die **Intervention** ein und machten die Antwort auf Z2-G zur
**Prompt-Folge**. **Die Gegenlesung ist als Qualitätsschritt vermerkt, NICHT als
Evidenz** — sie ist weder ein Messwert noch eine Validierung des Prompts.

## Anhang B — Grenzfall-Tabelle (während der Bewertung zu führen)

> **Diese Tabelle wird im Befund VOLLSTÄNDIG ausgewiesen, nicht nur gezählt**
> (§6 Punkt 1, §7 Punkt 7; Amendment 31.08.2026). Seit dem Wegfall des
> Zweitbewerter-Triggers ist sie der Ersatz für ein Übereinstimmungsmaß — kein
> Äquivalent, sondern die Offenlegung des Ermessens (Threat **T-Z2-7**).

| Vorschlag-ID | Kriterium | Entscheidung | Begründung |
|---|---|---|---|
| — | — | — | — |
