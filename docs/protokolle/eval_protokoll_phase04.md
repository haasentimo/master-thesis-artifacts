# Evaluationsprotokoll Phase 04 — vorregistriert

**Masterarbeit Timo Haas · HTWG Konstanz**
Stand: 1. September 2026 (Rev. 48) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33,
27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 bis Rev. 47 (unten
einzeln aufgeführt) und **Rev. 48 (N07, Ausführungsgeometrie des Inferenzservers als
Threat T15, §9)**.
~~Stand: 31. August 2026 (Rev. 47) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 bis Rev. 47~~
(überholt am 01.09.2026 durch N07, Rev. 48 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 48 sind datierte Amendments
darauf. **Kein Messteil ist berührt**: Metriken, Matching-Regeln, Injektionsmanifest,
Regeldatei, Prompt und Schema stehen unbewegt; bewegt ist §9 um einen Threat)

Die Amendments Rev. 34 bis Rev. 47 im einzelnen: Rev. 34 (C5c, Archivwurzel),
Rev. 35 (C10a, Validator-Punkt (6) commit-scharf), Rev. 36 (C6b-0a, Nachregistrierung des
Hash-Nachzugs aus C6b-2b), Rev. 37 (C6c, Zweideutigkeit in §7.2 der
Auswertungsspezifikation entschieden), Rev. 38 (C6c, Registrierung der
Auswertungsinstrumente), Rev. 39 (C6c-a, T7 auf die gehashten Laufmanifeste, Ausnahme
für lebende Dokumente, Präzisierung der Blindheitsauflage), Rev. 40 (C11b, kein-EN auf
EINER Aggregationsstufe, Läufespalte in T4, Ursachenaufspaltung abgelehnt), Rev. 41
(C11b, Hash-Nachzug der Auswertungsinstrumente nach der Reparatur R1–R9), Rev. 42
(C11c, die Forderung nach Median und Spannweite in der P/R/F1-Tabelle als
gegenstandslos ERLEDIGT), Rev. 43 (C11c, Hash-Nachzug der Auswertungsinstrumente
nach der Darstellungsreparatur D1–D3), Rev. 44 (C14, Artefaktauswahl auf das
Laufverdikt gestellt, Overlap-Tabelle T10 registriert, überholter T5-Vermerk im
Renderer nachgezogen), Rev. 45 (C14, Hash-Nachzug der Auswertungsinstrumente nach
der Umsetzung R11–R14) und Rev. 46 (G1, Kürzungsreihenfolge in der Scope-Gate-Regel
§7 als überholt gestrichen — **der Gate selbst ist am 31.08.2026 entschieden: Variante C
bleibt**) und Rev. 47 (Z1-P, Hash-Nachzug von `tools/check_doc_invariants.py` nach der
Aufnahme der Z1-Invariante (F)).
~~Stand: 31. August 2026 (Rev. 46) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 bis Rev. 46~~
(überholt am 31.08.2026 durch Z1-P, Rev. 47 — **reiner Bytestandsnachzug an EINEM
Auswertungsinstrument; die Freeze-Aussage selbst ist unverändert**, und kein Messteil ist
berührt)
~~Stand: 28. August 2026 (Rev. 45) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 bis Rev. 45~~
(überholt am 31.08.2026 durch G1, Rev. 46 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 46 sind datierte Amendments
darauf. **Kein Messteil ist berührt**: Metriken, Matching-Regeln, Injektionsmanifest,
Regeldatei, Prompt und Schema stehen unbewegt)
~~Stand: 28. August 2026 (Rev. 44) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 bis Rev. 44~~
(überholt am 28.08.2026 durch C14, Rev. 45 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 45 sind datierte Amendments
darauf)
~~Stand: 28. August 2026 (Rev. 43) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 bis Rev. 43~~
(überholt am 28.08.2026 durch C14, Rev. 44 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 44 sind datierte Amendments
darauf)
~~Stand: 28. August 2026 (Rev. 42) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 bis Rev. 42~~
(überholt am 28.08.2026 durch C11c, Rev. 43 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 43 sind datierte Amendments
darauf)
~~Stand: 28. August 2026 (Rev. 41) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 bis Rev. 41~~
(überholt am 28.08.2026 durch C11c, Rev. 42 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 42 sind datierte Amendments
darauf)
~~Stand: 28. August 2026 (Rev. 40) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 bis Rev. 40~~
(überholt am 28.08.2026 durch C11b, Rev. 41 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 41 sind datierte Amendments
darauf)
~~Stand: 28. August 2026 (Rev. 39) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 (C5c, Archivwurzel), Rev. 35 (C10a, Validator-Punkt (6) commit-scharf), Rev. 36 (C6b-0a, Nachregistrierung des Hash-Nachzugs aus C6b-2b), Rev. 37 (C6c, Zweideutigkeit in §7.2 der Auswertungsspezifikation entschieden), Rev. 38 (C6c, Registrierung der Auswertungsinstrumente) und Rev. 39 (C6c-a, T7 auf die gehashten Laufmanifeste, Ausnahme für lebende Dokumente, Präzisierung der Blindheitsauflage)~~
(überholt am 28.08.2026 durch C11b, Rev. 40 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 40 sind datierte Amendments
darauf)
~~Stand: 28. August 2026 (Rev. 38) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 (C5c, Archivwurzel), Rev. 35 (C10a, Validator-Punkt (6) commit-scharf), Rev. 36 (C6b-0a, Nachregistrierung des Hash-Nachzugs aus C6b-2b), Rev. 37 (C6c, Zweideutigkeit in §7.2 der Auswertungsspezifikation entschieden) und Rev. 38 (C6c, Registrierung der Auswertungsinstrumente)~~
(überholt am 28.08.2026 durch C6c-a, Rev. 39 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 39 sind datierte Amendments
darauf)
~~Stand: 28. August 2026 (Rev. 37) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 (C5c, Archivwurzel), Rev. 35 (C10a, Validator-Punkt (6) commit-scharf), Rev. 36 (C6b-0a, Nachregistrierung des Hash-Nachzugs aus C6b-2b) und Rev. 37 (C6c, Zweideutigkeit in §7.2 der Auswertungsspezifikation entschieden)~~
(überholt am 28.08.2026 durch C6c, Rev. 38 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 38 sind datierte Amendments
darauf)
~~Stand: 27. August 2026 (Rev. 36) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 (C5c, Archivwurzel), Rev. 35 (C10a, Validator-Punkt (6) commit-scharf) und Rev. 36 (C6b-0a, Nachregistrierung des Hash-Nachzugs aus C6b-2b)~~
(überholt am 28.08.2026 durch C6c, Rev. 37 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 37 sind datierte Amendments
darauf)
~~Stand: 27. August 2026 (Rev. 35) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin die Amendments Rev. 34 (C5c, Archivwurzel) und Rev. 35 (C10a, Validator-Punkt (6) commit-scharf)~~
(überholt am 27.08.2026 durch C6b-0a, Rev. 36 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 bis Rev. 36 sind datierte Amendments
darauf)
~~Stand: 27. August 2026 (Rev. 34) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1, darin das Amendment Rev. 34 (C5c, Archivwurzel)~~
(überholt am 27.08.2026 durch C10a, Rev. 35 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 und Rev. 35 sind datierte Amendments
darauf)
~~Stand: 27. August 2026 (Rev. 33) · Status: **EINGEFROREN zur Vorregistrierung, Rev. 33, 27. August 2026** — Messstand in §0.1~~
(überholt am 27.08.2026 durch C5c, Rev. 34 — **die Freeze-Aussage selbst ist unverändert**:
eingefroren wurde mit Rev. 33 am 27.08.2026, Rev. 34 ist ein datiertes Amendment darauf)
~~Stand: 26. August 2026 (Rev. 32) · Status: **Entwurf zur Vorregistrierung — Freeze steht aus** (§0)~~
(überholt am 27.08.2026 durch C5b, Rev. 33)
Rev. 3: zwei Matching-Metriken vorregistriert (`strict` und `localized`, §4), Clean-Control-Set
als Voraussetzung der Auswertung (§5).
Rev. 4: Diff-Erzeugung der Kampagne festgelegt (Injektions-Commits, `--base` mit SHA, Working
Tree clean als Vorbedingung, §6), Lauf-Akzeptanzregel um `changed_files_count: 0` und fehlenden
`run_header` erweitert (§6).
Rev. 5: Versionen der Baseline-Werkzeuge in den eingefrorenen Messstand aufgenommen (§1),
`--no-cache` als Ablaufregel für import-linter (§1).
Rev. 6: Kategorientabelle und Erwartungsmatrix in §3 ersetzt (sechs Abweichungstypen, zehn
Szenarien, zweistufige Kodierung, 32 Injektionen); Abbildung der alten Kürzel S1–S4, M1, M2
ergänzt (§3); verworfene Importgraph-Option in den Limitationen (§9) und Aussagekraft bei
kleinem n (§5) dokumentiert. Die Matching-Regeln in §4 bleiben unverändert.
Rev. 7: Datensatzbeschreibung auf die c1a-Messung gestützt (§2); CYCLE-Verteilung 3 + 1 und
Bauvorschriften Z1–Z4 für CYCLE-Injektionen (§3); Matchregel für `CYCLE` getrennt nach K1 und
K4, `expected_co_findings` vorregistriert — **schließt B28** (§4); **Sternhistorie** statt
linearer Kette, deskriptiver Vollbild-Lauf, Graphmodus je Kategorie, Lauf-Akzeptanzregel
`changed_files_count == 1 UND calls_total == 1`, Freeze-Tag über SHA (§6); Threats T6–T10 (§9).
Rev. 8: Ausführung der Entscheidung **Option B** — das Soll deckt den gesamten Messraum ab und
listet die vier Zielorte der `INCORRECT_LOCATION`-Injektionen, Modulliste maschinell erzeugt,
**Soll-Validator je Injektionscommit** (§2); zwei Rezeptpräzisierungen (§3, (e) und (f));
zwei Altlasten bereinigt — `HEAD~1` in §6 und die Punkte 3 und 4 in §0.
Rev. 9: zwei weitere Rezeptpräzisierungen (§3, (g) und (h)) — die K4-`layers`-Liste des
`exhaustive`-Contracts kommt aus dem **Dateibaum**, nicht aus der Soll-Modulliste, und
`SIGNATURE_DEVIATION` **ändert die Importmenge nicht**; toter Verweis „Fußnote ¹" in §0
korrigiert.
Rev. 10: Freeze auf die **Baseline-Konfigurationen** ausgedehnt — K4-Contract-Datei und
K5-Testdatei je mit SHA256 im Messmanifest und unter der Änderungssperre (§1); **Contract-Typ
je Szenario** vorregistriert, nur auf Typebene, mit „nicht ausdrückbar" wo zutreffend, plus
K5-Regelebene auf Untermodulnamen (§3); die drei bauvorschriftsgebundenen Zellen der
Erwartungsmatrix sind dort jetzt **annotiert** (§3).
Rev. 11: die beiden offenen Amendments aus Decision Record M.2 eingesetzt — Begleitmeldung in
der **richtigen Richtung** (`layer-violation` zu einer `CYCLE`-Injektion), `expected_co_findings`
für `FORBIDDEN_RELATION` **konstruktionsbedingt leer**, „identische `location`" nur unter Z2,
Bildungsregel und Fundstellenkorrektur, dazu die **Kategorieverwechslung K2/K3** neu
vorregistriert (§4); Begründung des Diff-Modus-Ausschlusses ersetzt und der Vollbild-Lauf als
**Messaufgabe** formuliert (§6); **dritter stiller Ausfall** — Soll-Validator prüft Regel-Scopes
gegen die Topologie, Gegenrichtung als Warnung, `__init__.py` → Paketname (§2);
`__init__.py`-Module **nicht** im Clean-Control-Set (§5); `c1b`-Zitate im ganzen Dokument auf
den vollen Dateinamen gebracht.
Rev. 12: die sechs offenen Punkte des Komponentenschnitts vollzogen —
**K4/K5-Konfiguration auf Contract-Typ- und Einstellungsebene vorregistriert** (§1);
**vierter Ausfallmodus** (`NetworkXError`, laut aber ergebnislos), Richtwert auf
**19 Pakete / rund 70 Dateien** korrigiert, drei Fidelitätsverzichte, Korrektur am
Amendment vom 13.08., Punkt (6) (§2); **Z2′** als Verschärfung von Z2 mit Beweisskizze,
`CYCLE_SIBLING`-Träger auf `api ↔ mappers`, Bauvorschriften **I1** und **K5-1**,
Matrixzelle K4/`PROTECTED_MODULE` an den Contract-Typ annotiert (§3); **vorregistrierte
K4-Begleitmeldung** für `LAYER_BACK_CALL` und die Form der K4-Zyklusmeldung (§4);
Ausnahmeklausel zum Clean-Control-Set gegenstandslos (§5); zwei Threat-Einträge
**T11/T12** (§9).
Rev. 13: **Ableitungsregel der K4-Konfiguration** vorregistriert — die
`forbidden`-Contracts für Schichtsprünge werden **mechanisch aus der Schichtliste**
abgeleitet, nicht aus dem Injektionsplan; damit **sechs** Skip-Contracts statt drei
(n−2 je Kontext, deckungsgleich mit Fußnote ¹ in §3), dazu das allgemeine **Prinzip**
für alle K4/K5-Regeln und die **Nicht-Abdeckung** der Whitelist durch das
Contract-Vokabular (§1); die Asymmetrie Erlaubnisliste ↔ Contract-Liste als
vorab benannter Vergleichsgegenstand in **UF3** (§8).
Rev. 14: **K5 wird als ERLAUBNISLISTE gebaut** — je Komponente eine Regel
`should_not().import_modules_except_modules_that().are_named([…])` unter
`exclude_external_libraries = True`, die Framework-Regeln über ein **zweites
Architekturobjekt** in derselben Datei unter `False`; **`include_external_packages = True`**
als erforderliche K4-Einstellung (§1); **fünfter Ausfallmodus** — eine PyTestArch-Regel auf
ein externes Modul bricht das Werkzeug ab, sobald der Import verschwindet; **Zuordnungsregel
für die vier Phantomeinträge** und für die **fünf Paketmodule**, Richtwert auf **72–75
Dateien** (§2); R-PLACE-1 als **Namensregel** vermerkt (§3); UF3-Zeile auf die genauere
Fassung gebracht — die Erlaubnisliste ist dem **Contract-Vokabular** von import-linter
überlegen, **nicht** dem Regel-DSL von PyTestArch (§8).
Rev. 15 (Nachträge auf **14.08.2026** datiert — der auslösende Auftrag hatte 13.08. vorgegeben,
das war ein Fehler im Auftrag; korrigiert mit Rev. 16, ältere Nachträge unberührt):
**die zweite Klausel von R-PLACE-1 vorregistriert** — die Regel hat **zwei**
suffixbasierte, **einseitig** formulierte Klauseln („Name impliziert Ort"): `_repo`/`_query`/
`_index` → `repository`, **`_models` → `models`**. Die Endung ist im Vorbild gemessen
(`iam/models`, `permission_models.py`), nicht erfunden. Die beiden Kandidaten aus
`c1_modulliste.md` §D.9 sind **ausdrücklich verworfen**: eine reine Ortsklausel verschöbe die
vorregistrierte Zelle K4/`INCORRECT_LOCATION`, ein `legacy_`-Präfixverbot bräche auf der
CLEAN-Baseline. Damit ist **I28 geschlossen** und der `rule_id`-Eintrag für alle vier
`INCORRECT_LOCATION`-Injektionen besetzbar; **keine Matrixzelle bewegt sich** (§3). Zwei
Mitkorrekturen aus derselben Ursache: die Phantomzeile zu I28 in §2 trägt den neuen Namen
(sie geht in den `expected_match_key` ein), und die Zahl der `__init__.py` in §5 ist von
„rund elf" auf **23 von 73** korrigiert — das Argument gegen Init-Module im Clean-Control-Set
wird dadurch **stärker**.
Rev. 16: drei Festlegungen aus dem ersten Bauauftrag der Clean-Baseline, alle mit
`4b1_bericht_baseline_kern.md` belegt — **die vier Ports der `MISSING_PORT_REFERENCE`-Träger
sind reserviert** (jeder erscheint in genau einem Modul, dort in einer öffentlichen
Methodensignatur; `ports.py` bleibt in 4b-2…4b-4 erweiterbar); **alle vier
`API_CONTRACT`-Regeln prüfen einheitlich über den `statement`-Wortlaut**, weil I32
`depot.core.ports` nicht importiert und kein Protocol referenzieren kann; **die Adapter-Fassade
löst ihre Re-Exporte über ein Modul-`__getattr__` auf** (PEP 562) — die eager Form bricht in
CPython, V12 bleibt damit **ohne Ausnahme** (§3). Dazu ein **vorhergesagter Falsch-Positiv** auf
eben dieser Fassade im Clean-Control-Lauf, getrennt zu führen (§5). Ferner die
**Datumskorrektur** der Rev.-15-Nachträge in §2, §3 und §5 auf den **14.08.2026**.
Rev. 17: vier Nachträge aus der fertigen Clean-Baseline, alle vor jeder Messung —
**das Ausschlusskriterium des Clean-Control-Sets ist präzisiert**: ausgeschlossen sind nur
**leere** `__init__.py`, nicht Paketmodule als Gattung; zwei der 23 sind inhaltstragend
(`depot.core.adapters`, `depot.orders.services`), das Control-Set umfasst **52 statt 50**
Module — zwingend, weil der in Rev. 16 vorregistrierte Falsch-Positiv auf der Fassade sonst
nicht messbar wäre (§5). **`sqlalchemy` 2.0.52 gehört in den eingefrorenen Messstand** (§1),
die **Kontaminationsfreiheit ist auf den Evaluationszeitraum zu datieren** (§2), jede Injektion
benennt die betroffene **Signatur namentlich** (§3), und der **Leer-Prompt wird vor der
Kampagne einmal gerendert und geprüft** (§6).
Rev. 18: zwei Nachträge aus der geschriebenen Regeldatei, beide **vor jeder Messung** —
die **drei schlüsselbildenden Schreibweisen** für `ABSENCE_REQUIRED`, `API_CONTRACT` und
`STRUCTURAL_PLACEMENT` sind vorregistriert und verbindlich für C4, und die vier
**R-PORT-Statements sind gekürzt** auf den vorregistrierten Umfang (Typschreibweise statt
wörtlicher Signatur) (§3); die **zweite vorhergesagte Falschmeldung** auf `orders_services`
ist vorregistriert und getrennt zu führen (§5).
Rev. 19: die sechzehn Regelstatements benennen **einheitlich die erwartete Subjektform** —
`subject.from`/`subject.to` bei den strukturellen Kategorien, `subject.offending_type` bei
den vier Elementkategorien. **Instrumenteneigenschaft**, damit `strict` die Erkennung misst
und nicht die Formatwahl des Modells (§4).
Rev. 20: die Zellen `FRAMEWORK_TYPE_IN_SIGNATURE` für **K4 und K5** stehen nach der
K4-Konfigurationsmessung auf **„nein"** statt FP⁴. Fußnote 4 bewahrt den alten Wortlaut
gestrichen und dokumentiert die falsch übertragene, nicht falsch gemessene B9+-Aussage. Der
Zweck der vier Zwillinge ist als direkter Test lexikalischen Schließens (UF1/UF2) neu gefasst
(§3); Komponentenschnitt, B38-Prüfliste und Standdokument sind auf die gemessenen
K4-Konfigurationsbefunde nachgezogen.
Rev. 21: die K5-Konfiguration ist geschrieben und gemessen (`data/soll/test_architecture.py`,
23 Regeln, Clean-State `24 passed`), und die drei Folgen aus Rev. 20 sind nachgezogen —
`include_external_packages = True` **bleibt** mit **neuer** Begründung (sichtbare, damit
**inspizierbare** Nicht-Abdeckung statt Artefakt der Unsichtbarkeit; gemessen wirkungslos für
alle dreizehn Contracts), der `sqlalchemy`-Pin **bleibt** und ruht ab hier **allein auf Grund
(c)** plus Smoke-Test, und K5 verwendet **EIN** Architekturobjekt (§1). Dazu die zwei
Nachzüge, die Rev. 20 offen ließ: die Begründung der Annotation **ᴾ** gilt für den
allgemeinen Fall, **nicht für das Testrepo** — dort ist die Kette `services → storage →
internal` nicht gebaut und beide Contract-Typen verhalten sich gleich; als **deklarierte
Grenze** geführt, `protected` bleibt die Wahl. Und die **Belegquellenspalte** der Zeile
`FRAMEWORK_TYPE_IN_SIGNATURE` ist **je Zelle aufgespalten**; die K5-Zelle ist mit der C2c-Sonde
von **abgeleitet** auf **gemessen** gehoben (§3). **Kein Matrixwert bewegt sich.**
Rev. 22: **B39 und B40 sind entschieden**, dazu die Lauf-Akzeptanzregel des Kontrolllaufs.
**B39:** die Zellen `CYCLE_SIBLING`/K5 und `CYCLE_PARENT_CHILD`/K5 gehen von **„nein"** auf
**„teilweise"** — K5 meldet beide Injektionen, aber **nicht als Zyklus**, sondern als **nicht
gelistete Kante** der Erlaubnisliste; gebucht wird **ohne neue Regel**: in `strict` kein Treffer,
in `localized` die bestehende Klasse „richtige Stelle, falsche Kategorie". Beide Alternativen
(`expected_co_findings`, „ja") sind erwogen und mit Begründung verworfen; die Richtung liegt
**gegen** die Hypothese und ist offengelegt — Symmetrie zu Rev. 20, wo sie umgekehrt lag (§3,
neue Fußnote 7). **B40:** die mit Rev. 20 zurückgezogene False-Positive-Zeile in §8 ist
**ersetzt** — `FRAMEWORK_TYPE_IN_SIGNATURE` steht bei den **echten Nullzeilen**, `CYCLE` bei K5
verlässt diese Aufzählung und bekommt eine eigene Zeile als Ausdrucksmächtigkeitsbefund eigener
Art (§8). **§6:** für den **Kontrolllauf** gilt **`control_files_count == calls_total`**; die
Vorbedingung ist aus vorliegenden Messungen **abgeleitet**, ein weiterer Lauf war nicht nötig.
`--control-files` und `control_files_count` gehören zum Messpfad, `checker_git_head` ist
**`348ca9d`**. Dazu die Mitkorrektur am **Kopfkommentar** von `data/soll/importlinter.ini`
(Rev.-21-Nachzug, neuer Datei-SHA256, Nachlauf `13 kept, 0 broken`).
Rev. 23: **C3 ist in C3a und C3b geteilt**, weil das Bestehenskriterium nicht für alle fünf
Konfigurationen gelten kann. **C3a** ist das **Audit** der deterministischen und statischen
Konfigurationen — K1, K4, K5 auf `B`, 0 Findings, **hartes Gate**, am 23.08.2026 in einem
Durchgang bestanden. **C3b** ist der **Kontrolllauf** von K2/K3 über die 52 Kontrollmodule; sein
Ergebnis ist die **Falsch-Positiv-Rate**, also eine **Messgröße**, kein Bestehenskriterium — zwei
Meldungen sind dort ausdrücklich **vorregistriert** (§5 Nachtrag Rev. 16 und Rev. 18). Die
Formulierung „C3 fordert über alle fünf Konfigurationen 0 Findings" (Fußnote 4, Rev. 20) ist
entsprechend **präzisiert**; ihre Beweislast trägt sie unverändert (§3 Fußnote 4 Nachtrag, §6
Nachtrag). Dazu: die **Leer-Prompt-Vorbedingung** aus §6 Rev. 17 ist **erfüllt** — der Prompt
eines importfreien `INCORRECT_LOCATION`-Trägers ist gerendert, wörtlich abgelegt und mit dem Auge
geprüft; und das **Clean-Control-Set** liegt als gehashter Messeingang
`data/soll/control_files.txt` (52 Zeilen, SHA256 `7356e6d3…`).
Rev. 24: vollständige Aufrufspezifikation für K1–K5 und den Kontrolllauf (§6),
Build-Provenienz des tatsächlich ausgeführten `dist/cli.js` (§1), Nachlaufskript als alleiniger
Vollstrecker beider Lauf-Akzeptanzregeln (§6) sowie getrennte Pins für Messpfad und
Prüfwerkzeug (§1); C3a-Aufrufe als Ausgangspunkt kenntlich gemacht.
Rev. 25: **Recordmenge je Konfiguration getrennt** (§4) — weil `--rule-graph diff` in den
K2/K3-Aufrufzeilen steht, läuft der deterministische Pfad mit und schreibt in dasselbe Log; die
Konfiguration ist ab hier durch den **Mechanismus** bestimmt (`DERIVED:`-Präfix = K1, jedes
andere `rule_id` = K2/K3), der Filter greift **vor** beiden Metriken, und das Nachlaufskript weist
je Lauf **beide** Zahlen getrennt aus (§6). Ohne den Filter wäre `localized` konfundiert.
Rev. 26: K2-Machbarkeitslauf auf der neuen Maschine ausgewertet — **beide Lauf-Akzeptanzregeln
tragen den Wiederholungsfaktor** (`calls_total` akkumuliert über alle Repetitionen; korrigierte
Fassungen `changed_files_count == 1 ∧ calls_total == 1 * runs` und
`calls_total == control_files_count * runs`), der **Exit-Code ist kein Gültigkeitskriterium**,
und das **Kontextfenster ist ein gemessener Umgebungsparameter** (kein `num_ctx` gesetzt, Ollama
lädt `CONTEXT 4096` statt der Modellgrenze 32768) (§6, §1). Dazu die **Messumgebung K2**
vollständig übernommen und ein Reproduzierbarkeitsbefund (Checker-Build plattform- und
toolchain-unabhängig bitgleich) sowie ein Threat-Eintrag zum Maschinenwechsel (§1, §9).
Rev. 27: **Lesekorrektur zu `localized` auf dem LLM-Pfad** — die Metrik misst dort die
Meldequote auf der geprüften Datei, nicht die Lokalisationsgenauigkeit (§4); deskriptiver
Nachtrag zu den 461 Findings des K2-Kontrolllaufs — Selbst-/Fremd-/Zielbezug, `R-CORE-1` als
153 identische Findings, neun `sqlalchemy`-Halluzinationen (§3); K2-Kontrolllauf auf **voller
Skala** bestätigt, Kontextfenster empirisch geschlossen (§1); **Poolbefund K3** — der geteilte
Anbieter-Pool bricht auch unter einem auf ein Fünfzehntel reduzierten, entkoppelten
Lastprofil in drei von fünf Invocationen ab (§1, §6, B37); Schlüsselvorfall dokumentiert (§7).
Rev. 28: **I16-Zielkante klargestellt** — die in Fußnote 7 zitierte K5-Ausgabe zu I16 stammt aus
der C2c-Prüfsonde gegen zehn Baseline-Kopien, nicht aus der I16-Injektion dieses Testrepos;
verbindlich ist die Rückkante auf das **Paketmodul** `depot.orders.services`, mit Begründung aus
Decision Record P und einem Vermerk zum echten Laufzeit-Zirkelimport (§3); **Typwahl für
I21–I24 festgelegt** — injiziert wird `sqlalchemy.orm.Session`, mit drei Auflagen für C4b (§3).

Rev. 29: zwei Nachträge aus dem gebauten Injektionsdatensatz (C4b), beide **vor jeder Messung** —
**Klarstellung zu den Zyklen der `LAYER_BACK_CALL`-Injektionen:** I01–I03 tragen je einen
Komponentenzyklus `<k>_repository ↔ <k>_services`, **konstruktionsnotwendig** und als
**K4-Doppelmeldung vorregistriert** (Komponentenschnitt §6.2, §4 Amendment 13.08.); auf **K1**
wirkt er **nicht**, weil `FORBIDDEN_RELATION` in `--rule-graph diff` läuft und eine
`cycle`-Begleitmeldung dort strukturell unmöglich ist (Decision Record M.2 Festlegung 2), Z1 und
Z3 sind unberührt (§3). **Der deskriptive Vollbild-Commit fehlt noch** — C4b hat ihn nicht gebaut,
weil sein Auftrag auf 32 Commits begrenzt war; als **OFFEN** geführt, ohne Wirkung auf eine Metrik
und ohne Blockade von C4c oder der Kampagne, mechanisch aus den 32 Tags herstellbar, eigener
Auftrag (§6).

Rev. 30: Vormessungen vor der Kampagne (D2), alle **vor** dem ersten Injektionslauf —
**§4: `localized` ist für K4/`CYCLE` NICHT DEFINIERT** und wird für die Zellen
`CYCLE_SIBLING`/K4 und `CYCLE_PARENT_CHILD`/K4 als **„n. b."** ausgewiesen, nicht als 0; die
Alternative, die Paketebene als Modul-Match zu zählen, ist **erwogen und verworfen** (§4).
**§5: die berichtete Wanduhrzeit ist für alle fünf Konfigurationen extern je Invocation
gemessen**, `run_footer.wall_clock_ms` bleibt Innenwert im Anhang (§5). **§1: der
K3-Zugangsweg ist registriert** — Base-URL `https://inference.do-ai.run/v1`, Modell
`nvidia-nemotron-3-super-120b`, **kein** `CONFORMANCE_PROVIDER_PIN`; das Kontextfenster
`1 000 000` ist **gemessener Umgebungsparameter** aus dem Anbieterkatalog, Quantisierung und
Serving-Stack sind **nicht belegbar** (§1). **§6: vier zusätzliche Aufzeichnungsauflagen für
C7** (externe Wanduhrzeit, wörtliches stdout/stderr je K4/K5-Aufruf, Pfad-/Maschinenkennung im
Laufmanifest). **§9: Threat T14** — Anbieter- und Endpunktwechsel bei K3; die Vormessungen
Befund 06.5/06.6 und B36a liefen über OpenRouter, gemessen wird der DigitalOcean-Direktzugang.
**§1: `c6_auswertungsspezifikation.md` als gehashter Auswertungseingang registriert.** Keine
Änderung an Manifest, Soll-Modell, Regeldatei, Prompt oder Schema (§10).

Rev. 31: sechs Nachträge aus den Vormessungen D2/D2N, alle **vor** dem ersten Injektionslauf —
**§4: die Schreibvarianz bei `FORBIDDEN_SIGNATURE_TYPE` ist als vorhergesagter `strict`-Ausfall
DEKLARIERT**, nicht nachträglich erklärt (57 zu 6 im K2-Ruhezustand, auf zwei Zwillingsmodulen,
auf keinem Injektionsträger; **keine** Normalisierung, **kein** Eingriff ins Manifest — Decision
Record O, H3b); **§4: `strict` ist für `STRUCTURAL_PLACEMENT` nicht unabhängig von `localized`**
— Segment 4 ist in 54 von 54 Findings zeichengleich mit Segment 3, die Zelle wird weiter
berichtet, aber mit Fussnote; **§5: die Vorbelastung je Injektion ist berichtspflichtig** — zu
jedem Kampagnenergebnis die Ruhezustandszahl desselben Moduls in derselben Kategorie aus C3b,
und ein `strict`-Treffer, der die Ruhezustandsrate nicht übersteigt, ist **kein**
Erkennungsnachweis; **§5: paarweise Auslesart je Injektion** — Differenz injizierter Zustand
gegen Ruhezustand desselben Moduls, deskriptiv, bindend auch bei null oder negativ; **§6: der
Graphmodus wird aus der Kategorie ABGELEITET, nicht per Aufrufzeile gesetzt, und je Lauf ins
Laufmanifest geschrieben** (Auflage für C7); **§9: zwei Ergänzungen an bestehenden Threats** —
T13 um die Node-Versionsdifferenz `v22.23.2` gegen `v22.22.2` (folgenlos, Gatterbeleg ist der
Build-Hash), T14 um die schwache indirekte Katalogstütze `context_length`, ohne den Satz zur
nicht verifizierten Gewichtsidentität anzutasten. Dazu der **Nachzug des
Auswertungseingangs**: `c6_auswertungsspezifikation.md` ist auf den D1-Stand gezogen (I21–I24
wörtlich aus dem Manifest, die vier neuen Punkte als Anforderungen an C6b), ihr **SHA256 in §1
nachgezogen** — alter Hash gestrichen, neuer daneben. Keine Metrikänderung, keine
Manifeständerung, keine Matrixzelle bewegt sich.

Rev. 32: vier Nachträge aus der Aufrufspezifikationsprüfung vor dem Bau des Kampagnen-Runners
(C7, Schritt 0), alle **vor** dem ersten Injektionslauf und ohne Wirkung auf ein Messergebnis —
**§6: die K5-Aufrufzeile war UNVOLLSTÄNDIG REGISTRIERT und ist korrigiert.** Die in §6 Rev. 24
registrierte Zeile trägt `DEPOT_SRC` nicht; ohne die Variable wirft `data/soll/test_architecture.py`
schon beim **Sammeln**, pytest bricht ab und **0 von 23** Architekturregeln laufen, ohne dass
Exit-Code oder Ausgabe diesen Fall von einem sauberen Lauf trennen. **Korrigiert wird der
AUFSCHRIEB, nicht die Konfiguration:** alle drei gemessenen K5-Läufe (C2c §B4, C3a §3b, D2 M5(c))
sind **mit** der Variablen gefahren, `-q` **bleibt**; **§6: die K3-Aufrufzeile ist auf den
Direktzugang gezogen** — §6 Rev. 24 trug noch OpenRouter-Endpunkt, OpenRouter-Slug und
`CONFORMANCE_PROVIDER_PIN=digitalocean`, während §1 Nachtrag Rev. 30 den DigitalOcean-Direktzugang
ohne Pin für verbindlich erklärt; Rev. 30 hatte nur die **Matrixzeile** in §1 gestrichen, das
Protokoll trug seither **zwei** verbindliche K3-Zeilen; **§6: POSITIVE LAUF-AKZEPTANZREGEL FÜR
K4 UND K5** — beide Werkzeuge schreiben kein Laufprotokoll und hatten deshalb **kein** positives
Gültigkeitskriterium; geprüft wird ab hier je Invocation, dass das Werkzeug seine **Regelmenge**
gelesen hat (K5 **24** gesammelte Tests bei fehlerfreier Sammelphase, K4 **13** ausgewertete
Contracts als `kept + broken`), **nicht** wie viele Verstösse es gefunden hat; **§9: T12 ergänzt**
um die Ausfallklasse „stille Null durch Fehlkonfiguration bei den Konfigurationen ohne
Laufprotokoll", mit beiden Instanzen (Graphmodus Rev. 31, `DEPOT_SRC` Rev. 32). Dazu die
**Festlegung der K4-Schreibform** in §6 (Teil 3), damit der Runner zwischen zwei wirkungsgleichen
Pfadformen nicht wählen muss. **Keine Metrikänderung, keine Manifeständerung, keine Matrixzelle
bewegt sich, kein Messergebnis betroffen.**

Rev. 33: **FREEZE ZUR VORREGISTRIERUNG**, gesetzt **vor** dem ersten Kampagnenlauf —
**§0 Punkt 2 ist entschieden und damit der letzte offene Punkt des Freeze geschlossen:** das
**Validitäts-Gate 0.9 aus §7 ist BESTÄTIGT, unverändert**. Die technische Vorbedingung ist
erfüllt (Exit-Code 3 bzw. persistiertes Run-Log, CLI-Inkremente 2 und 4; der Messstand enthält
Increment 7), der Anteil valider Calls liegt in **beiden** Kontrollbeständen bei **156/156 =
1.0** (`data/c3b-k2/runs/`, `data/c3b-k3/runs/`), und die Richtung der Regel ist konservativ:
Dokumentation als Befund und Auswertung mit den vorhandenen validen Läufen, **ohne
Nachbesserung**. **§0.1 neu: Messstand (eingefroren)** — Protokoll, Auswertungsspezifikation,
die sieben Messeingänge aus `data/soll/SHA256SUMS`, Checker-Tag und Build-Hash, Runner-Commit,
Testrepo-Baseline mit Injektions-Bundle und Archivwurzel, jeder Wert aus Datei bzw. Repo
**gelesen**; dazu die **Amendment-Sperre ab dem ersten Kampagnenlauf**. **§6: der
Graphmodus-Nachtrag Rev. 31 ist im Wortlaut auf K1 EINGESCHRÄNKT** — `full` bei
`category_l1 == CYCLE` gilt für **K1**; K2/K3 tragen nach §6 Rev. 25 immer `--rule-graph diff`,
K4/K5 kennen den Schalter nicht. **Klarstellung, keine Änderung der Festlegung:** der generische
Wortlaut hätte **12** statt **4** Full-Läufe gedeckt; belegt durch die C5-Planausgabe
(4 × `full`, 92 × `diff`) und C4c Teil B. **§1: die K3-Matrixzeile ist nachgezogen** — die als
überholt bezeichnete OpenRouter-Zeile stand seit Rev. 30 **ungestrichen** in der Tabelle; sie ist
jetzt gestrichen und die Direktzugangszeile steht daneben. **Keine Metrikänderung, keine
Manifeständerung, keine Matrixzelle der Erwartungsmatrix bewegt sich, kein Messergebnis
betroffen.**

Rev. 34: **Amendment zur Archivwurzel (C5c), gesetzt VOR dem ersten Kampagnenlauf.** Die
Archivwurzel der Kampagne wandert von ~~`/home/haasentimo/scratch/c7/out`~~ nach
**`~/ma/masterarbeit/data/campaign/`** — ein **versionierter** Pfad im Thesis-Repo statt eines
flüchtigen Scratchpad-Verzeichnisses. Begründung: **§6 Punkt 4 verlangt, die Rohlogs unverändert
zu archivieren**; ein Scratchpad trägt sie nicht. Der **C4c-Verlustfall** zeigt die Folge —
dort liegen die sechzehn `--run-log`/`--json-out`-Dateien der Vorabprüfung „im flüchtigen
Arbeitsverzeichnis dieses Auftrags" und sind **nicht** abgelegt (`c4c_bericht_vorabpruefung.md`
Teil C); bei der Kampagne wäre derselbe Weg ein Verstoss gegen §6 Punkt 4. Der Pfad ist in
`tools/run_campaign.py` **nicht hart verdrahtet**, sondern Vorgabe des CLI-Parameters `--out`.
**Die Änderung betrifft ausschliesslich die ABLAGE: keine Messgrösse, kein Messeingang, keine
Metrik, keine Zelle der Erwartungsmatrix, keine Aufrufsemantik.** Belegt durch den erneuten
`--plan`-Lauf (Exit 0): **160 Invocations, 192 Model-Calls, 480 Zielpfade, alle eindeutig** —
gegen die C5-Planausgabe zeichengleich **bis auf das Pfadpräfix** (577 Zeilen tragen es in
beiden Ausgaben) und den Erzeugungszeitstempel. Mitgezogen: die Zeile **Runner** in §0.1, weil
der Commit-Wert dort „der letzte Commit, der eine dieser drei Dateien berührt" bezeichnet und
`tools/run_campaign.py` mit dieser Änderung berührt ist. **Der Zeitpunkt ist der Punkt:** die
Änderung erfolgt vor dem ersten Kampagnenlauf, es existiert noch kein Messbestand, der
umzuziehen wäre.

Rev. 35: **Amendment zum Soll-Validator, Punkt (6), gesetzt NACH dem ersten Kampagnenlauf
(C10a).** Der **Defekt im Wortlaut:** Validator-Punkt (6), Z2′ (ii) „sole importer per
component", ist eine Eigenschaft des **Codegraphen**, nicht des **Soll-Modells**. Der Runner
behandelte die Punkte (1)–(6) gleichermassen als commit-invariant und brach bei jedem FAIL ab.
Unter einer `FORBIDDEN_RELATION`-Injektion, deren Ziel im Ruhezustand **genau einen** Importeur
trägt, ist Punkt (6) jedoch **zwangsläufig** verletzt — die Injektion zieht ja gerade einen
zweiten Importeur ein. Betroffen sind **I07, I08, I09**, alle drei auf das Ziel
**`core_adapters_internal`**. Der Abbruch war das Kriterium, nicht die Injektion.

**Klassifikation der acht Validator-Punkte** — der eigentliche Ertrag dieses Amendments, weil
die nächste Injektionsmenge damit nicht mehr blind in dieselbe Wand läuft:

| Punkt | Prüft | Art | Begründung in einem Satz |
|---|---|---|---|
| (1) | Soll-Modulliste gegen den Dateibaum, beidseitig | **commit-invariant** | Die Phantommenge ist eine Eigenschaft des Soll-Modells; nur `INCORRECT_LOCATION` verschiebt sie, und dafür trägt der Validator bereits `--injection I25…I28`. |
| (2) | Jede Komponente kommt in mindestens einer Relation vor | **commit-invariant** | Reine Wohlgeformtheit des Soll-Modells — keine Injektion legt eine Komponente an oder entfernt eine Relation aus dem Soll. |
| (3a–d) | Regelskopes und -kategorien gegen Topologie und §3 | **commit-invariant** | Prüft `architecture-rules.yaml` gegen das Soll; beide Dateien sind Messeingänge unter der Änderungssperre und bewegen sich während der Kampagne nicht. |
| (4) | Bauregel I1 — keine Kante aus den geteilten Komponenten nach `orders_*`/`billing_*` | **commit-invariant** | Bauregel des Soll-Entwurfs; I1-Vorkommen werden nach §3 Rev. 12 ohnehin **aufgezeichnet statt unterdrückt** und sind kein Abbruchgrund. |
| (5) | Z2′ (i) — Ordnung der vier Zyklenpaare in Code-Unit-Reihenfolge | **commit-invariant** | Vergleicht **Namen** miteinander, nicht den Graphen; kein Commit benennt eine Komponente um. |
| **(6)** | **Z2′ (ii) — Importeursmenge der fünf geschützten Komponenten** | **commit-VARIANT** | **Zählt Kanten des Codegraphen; jede Injektion, die eine Kante auf eine geschützte Komponente einzieht, verändert sie zwangsläufig.** |
| (7) | Zyklenzahl des Ist-Zustands | commit-variant | Zählt Zyklen des Codegraphen; `CYCLE`-Injektionen und die bauvorschriftsgebundenen I01–I03 verändern sie — seit Rev. 29 gegen `--expect-cycles` geführt. |
| (8) | Modulkanten ausserhalb der Whitelist | commit-variant | Zählt Kanten des Codegraphen gegen das Soll; die sechzehn strukturellen Injektionen ziehen je genau eine ein — gegen `expected_edge_boundary` geführt. |

**Die neue Regel für (6):** erwartet wird die **exakte Importeursmenge** je geschützter
Komponente, **berechnet** aus zwei registrierten Quellen — dem **whitelisted Importeur** aus
`depot_soll.ilograph.yaml` und der **Quellkomponente** der in `expected_edge_boundary`
registrierten Kante. Abgebrochen wird weiterhin bei mehr als einem zusätzlichen Importeur, bei
einem anderen als dem registrierten, bei fehlendem Ruhezustands-Importeur und bei jeder
Abweichung an einer Komponente, die die Injektion nicht berührt.

**Die Richtung ist schärfeerhaltend, genauer: schärfend.** Rev. 34 verglich eine **Zahl**
(`len(importers) == 1`) und sah nie nach, **welche** Komponente importiert; Rev. 35 vergleicht
die **Menge**. Ein Lauf, den Rev. 34 durchgelassen hätte — Ruhezustands-Importeur weg, dafür ein
fremder da, Anzahl weiterhin 1 — bricht ab.

**Warum das KEINE nach §0.1 gesperrte Änderung ist**, vier Punkte: **(a)** Der registrierte
Entwurf verlangt diese Commit-Schärfe ausdrücklich — `docs/planung/offene_punkte.md`, C7,
Zusatz (12.08.): der Runner führt den Soll-Validator „als Vorbedingung je Lauf … **mit der für
den jeweiligen Commit erwarteten** Phantommenge" aus. Punkt (6) commit-scharf zu führen, holt
nach, was dort steht. **(b)** Berührt sind **weder Metrikdefinition noch Injektionsmanifest,
Regeldatei, Prompt oder Schema** — die fünf Gegenstände, die §0.1 Punkt 2 ab dem ersten
Kampagnenlauf sperrt. Berührt ist allein eine **Vorbedingung des Runners**. **(c)** Die
Erwartung ist aus den Messeingängen **berechnet**, nicht gewählt: kein Wert ist hart verdrahtet,
keiner aus einem Bericht abgetippt. **(d)** Die Richtung schliesst Datenwahl aus — ein
schärferes Gatter kann ein Ergebnis nur verwerfen, nie herbeiführen.

**Der Zeitpunkt, ungeschminkt:** dieses Amendment steht **nach** dem ersten Kampagnenlauf.
Am 27.08.2026 um 08:25 liefen **sechs K2-Invocationen** (I01–I06, 18 Calls, `valid_final`
18/18, gemessenes Fenster 4096, maximales `tokens_in_total + tokens_out_total` 1599), bevor der
Runner bei I07 abbrach. Diese sechs Läufe sind **verworfen**: nicht ausgewertet, nicht
committet, aus `data/campaign/` entfernt und nach
`~/scratch/c10a/abgebrochener_k2_teilbestand/` abgelegt; ihre SHA256 stehen in
`c10a_bericht_validator_punkt6.md`. **K2 wird vollständig neu gefahren**, damit der Block unter
**einem** Runner-Commit steht. Die Auswertungssperre der Eine-Iteration-Regel (§7) galt und
gilt: an dem Teilbestand wurde keine Metrik berechnet und kein Finding beurteilt.

Mitgezogen: die Zeile **Runner** in §0.1, weil der Commit-Wert dort „der letzte Commit, der eine
dieser drei Dateien berührt" bezeichnet und `tools/run_campaign.py` berührt ist.

Rev. 36: **Nachregistrierung eines bereits vollzogenen Bytewechsels (C6b-0a), gesetzt NACH dem
ersten Kampagnenlauf — dieses Amendment BESCHREIBT nur, es legt nichts fest.**

**Was C6b-2b geändert hat, und zwar richtig.** Der Auftrag C6b-2b hat die
Auswertungsspezifikation `docs/protokolle/c6_auswertungsspezifikation.md` an drei Stellen
**ergänzt** — §10.4 (offener Punkt 4, die K4/K5-Matchregel, ERLEDIGT), §6.2 (korrigiert:
Parameter der Test-ID der vier Portregeln ist die `rule_id`, nicht der Modulname, belegt an
`data/soll/test_architecture.py:309-310`) und §1.4 (erweitert um die **Terminalbreite** als
Umgebungsparameter der K4-Messung, gemessen `console.width = 80`, `is_terminal = False`).
Damit ändert sich der SHA256 des **registrierten Auswertungseingangs** notwendig:
~~`2f1354bbabdfaef8c858a6726521e224c30d6293513d83ea98cd1ef3f6608f97`~~ →
**`8f6d358073d7f580fd8741bec2611fa2638c6f80f55ca9d10bb03ada82c37749`**. Dieser Nachzug ist in
`0c1cc34` an **beiden** vorgeschriebenen Stellen vollzogen — §1 (Nachtrag Rev. 30, Tabelle des
Auswertungseingangs) und §0.1 (Messstand) —, im **selben Commit** wie die
Spezifikationsänderung. **Der Nachzug selbst war richtig und von der Repo-Regel verlangt**;
er wird hier nicht revidiert, sondern registriert.

**Was dabei unterblieb, ungeschminkt.** Der Nachzug wurde in `0c1cc34` vollzogen **ohne
Kopf-Revision, ohne Eintrag in dieser Revisionshistorie und ohne Zeile in §10**. Das Protokoll
trug danach unverändert „Rev. 35" im Kopf, während seine Bytes nicht mehr die von Rev. 35
waren. Der SHA256 des Protokolls wechselte damit von
`876680b13c568312059d9143b146617b3be6887e5e89a2badfd05c5361f3b910` (Rev. 35, bezeugt in
`c5b_bericht_protokoll_freeze.md` §3) auf
`620f11739d65ba759ea8b78eb2d710be684c40fb4c52e9e3d74a7464283d80d3` — und **dieser Bytestand
war in keinem Dokument bezeugt**. Er ist in `c5b_bericht_protokoll_freeze.md` §3
nachgetragen, als Zwischenstand kenntlich, **nie als Revision geführt**.

**Wie es aufgefallen ist.** An der **Bewegungsprüfung** von C6b: der Auftrag misst als
Vorbedingung den SHA256 des Protokolls und vergleicht ihn gegen den in
`c5b_bericht_protokoll_freeze.md` §3 als aktuell geführten Wert. Der Vergleich schlug an und
der Auftrag brach ab, bevor eine Zeile Harness geschrieben war. **Die Prüfung hat also
funktioniert — ihr fehlte der Vergleichswert**, nicht die Schärfe. Genau das ist der Grund,
aus dem Rev. 36 nachträglich geschrieben wird, statt den Bytewechsel als folgenlos abzutun.

**Die Lesart, ab jetzt verbindlich: JEDE Änderung am Protokoll ist eine Revision, auch ein
reiner Hash-Nachzug.** Zwei Gründe, beide unabhängig tragend. **(a)** Eine Ausnahme für
„inhaltsneutrale" Bytewechsel verlangte ein **Urteil darüber, welche Änderung substanziell
ist** — und dieses Urteil nimmt der Freeze gerade aus dem Verkehr; wer es nach dem Freeze
wieder einführt, hebt die Vorregistrierung an der Stelle auf, an der sie wirken soll. **(b)**
Der Protokoll-SHA ist der **Anker der Bewegungsprüfung** und als Detektor nur brauchbar, wenn
**kein** Bytewechsel unregistriert bleibt; ein einziger geduldeter Wechsel macht jede spätere
Abweichung mehrdeutig — sie kann dann ebenso gut ein zweiter geduldeter Wechsel sein. Der Satz
steht als Punkt 5 in der Amendment-Regel in §0.1.

**Der Riegel.** `tools/check_doc_invariants.py` prüft ab jetzt maschinell, dass (a) der
SHA256 des Protokolls dem in `c5b_bericht_protokoll_freeze.md` §3 als aktuell geführten Wert
entspricht, (b) Kopf-Revision, höchste §10-Zeile und oberster Eintrag dieser
Revisionshistorie **dieselbe** Nummer tragen, (c) der SHA256 der Auswertungsspezifikation dem
in §1 **und** dem in §0.1 geführten Wert entspricht, und (d) `sha256sum -c` in `data/soll`
und in jedem `data/campaign`-Unterordner mit `SHA256SUMS` durchläuft. Der Prüfer ist
**ausschliesslich lesend** und läuft als Vorbedingung jedes schreibenden Auftrags
(`CLAUDE.md`).

**Ausdrücklich, und in diesem Fall ohne Einschränkung:** **keine Metrikdefinition, kein
Injektionsmanifest, keine Regeldatei, kein Prompt, kein Schema** berührt — die fünf
Gegenstände, die §0.1 Punkt 2 ab dem ersten Kampagnenlauf sperrt. **Keine Zelle der
Erwartungsmatrix bewegt sich, kein Messergebnis ist betroffen**, kein Wert der §0.1-Tabelle
ändert sich. Die Sperre aus §0.1 Punkt 2 ist gewahrt, weil dieses Amendment **ausschliesslich
beschreibt**, was bereits geschehen ist, und **nichts festlegt**, wogegen gemessen wird.

Rev. 37: **Entscheidung einer Zweideutigkeit in der Auswertungsspezifikation (C6c), gesetzt
VOR ihrer ersten wirksamen Anwendung.**

**Die Zweideutigkeit.** §7.2 der Auswertungsspezifikation verlangte, die beiden
vorregistrierten Meldungen des Clean-Control-Sets (§5, Fälle 4 und 5 — Adapterfassade
`R-PROTECT-1`, Nicht-Träger-Portregel `R-PORT-2`/`R-PORT-3`) „**aus dem Zähler der
Headline-Rate herauszurechnen und separat auszuweisen**". Die Ergebniszeile des K2-Berichts
führt dieselben Meldungen dagegen „getrennt **darin** enthalten" (`c3b_k2_bericht_kontrolllauf.md`
§4.2). Zwei Lesarten desselben Sachverhalts, in zwei vorregistrierten Dokumenten.

**Entschieden: die vorregistrierten Meldungen BLEIBEN IM ZÄHLER und werden GETRENNT
AUSGEWIESEN — sie werden NICHT herausgerechnet.** Die Headline-Rate zählt die
Kontrollmodule mit ≥ 1 Finding, **alle Findings**; die vorregistrierten Meldungen stehen
zusätzlich in einer eigenen Zeile (T3.1), und die zweite Lesart wird mitgeführt, ist aber
nicht die Headline.

**Begründung, drei Gründe, jeder für sich tragend.** **(a)** Die Herausrechnung
**verbesserte die K2-Falsch-Positiv-Rate**, also die gemessene Grösse, zugunsten des
Prüfgegenstandes — und sie wäre **gewählt**, nicht von der Messung erzwungen. Genau diese
Sorte Festlegung sperrt §0.1 Punkt 4 nach Messbeginn, weil sie von einer an den Daten
gewählten nachträglich nicht mehr zu unterscheiden ist. **(b)** Sie widerspräche der
Auflage aus §5 Amendment 11.08.: `localized` wird für K2/K3 **nie ohne die vollständige
FP-Rate** berichtet. Eine Rate, aus der zwei reale Meldungen herausgerechnet sind, ist
nicht die vollständige. **(c)** Eine vorhergesagte Meldung ist auf sauberem Code trotzdem
eine Meldung. **Vorhersagbarkeit ist ein Zusatz, kein Abzug** — sie sagt, dass wir die
Meldung erklären können, nicht dass sie nicht stattgefunden hätte.

**Der Zeitpunkt, ausdrücklich.** Auf dem Kontrollbestand ergeben **beide Lesarten
denselben Wert 49** (beide betroffenen Module tragen ausserdem andere Findings;
`c6b_bericht_harness.md` §4.5); im Harness-Fixture fallen sie auseinander, **3/6 gegen
4/6**. Die Entscheidung fällt damit **vor ihrer ersten wirksamen Anwendung**: keine
berichtete Zahl verschiebt sich, und der Auswertungslauf über `data/campaign/k*` hat zum
Zeitpunkt dieser Entscheidung **nicht stattgefunden**.

**Was das für §0.1 Punkt 2 bedeutet, ungeschminkt.** Die Sperre nach dem ersten
Kampagnenlauf verbietet, eine **Metrikdefinition** zu ändern. Dieses Amendment ändert
keine Definition, es **entscheidet eine Zweideutigkeit zwischen zwei vorregistrierten
Formulierungen** — der Zähler ist seit Rev. 3 „Zahl der Kontrollmodule mit ≥ 1 Finding",
und die entschiedene Lesart ist die **wörtliche** Anwendung dieses Satzes; die verworfene
war der Zusatz, der ihn einschränkte. Berührt sind **kein Injektionsmanifest, keine
Regeldatei, kein Prompt, kein Schema**, keine Zelle der Erwartungsmatrix und kein bereits
berichteter Wert. Geändert wird allein §7.2 der Auswertungsspezifikation, deren SHA256
damit notwendig nachzieht (§0.1 und §1).

Rev. 38: **Registrierung der AUSWERTUNGSINSTRUMENTE im Messstand (C6c), gesetzt VOR dem
ersten Auswertungslauf über `data/campaign/k*`.**

**Die Lücke.** Der Messstand nach §0.1 bezeugt den **Eingang** (sieben Dateien unter
`data/soll/`, Checker-Tag und Build-Hash, Testrepo und beide Bundles) und — über die
Bewegungsprüfung — das **Protokoll** und die **Auswertungsspezifikation**. Nicht bezeugt
war der **Weg dazwischen**: die drei Werkzeuge, die aus den Eingängen die Zahlen des
Kapitels 7 **erzeugen**. Eine stille Änderung an `false_positive_rates()`, an `NB_CELLS`
oder an einer Zellenregel in `tools/match_k4k5.py` verschöbe **jede** Tabelle, ohne dass
ein einziger registrierter Wert sich bewegte — und die Bewegungsprüfung über die
Eingangshashes bliebe dabei **grün**.

**Registriert sind drei Dateien mit ihrem SHA256** (§0.1, Zeile
**Auswertungsinstrumente**): `tools/evaluate_campaign.py`, `tools/match_k4k5.py` und
`tools/check_doc_invariants.py`. **Der Prüfer registriert sich selbst mit** — sonst wäre
er die eine Datei, deren Änderung er nicht meldet.

**Die Regel dazu steht als Punkt 6 in der Amendment-Regel unter §0.1:** ab dem ersten
Auswertungslauf ist jede Änderung an diesen drei Dateien eine **datierte Revision mit
Begründung**; **keine** darf eine **Rechenregel** oder einen **Marker** verschieben;
zulässig ist allein die **Behebung eines Defekts**, mit **vollständiger Neuauswertung**
und **Ausweis beider Ergebnisse**, nebeneinander und nicht ersetzend.

**Maschinell geprüft** durch `tools/check_doc_invariants.py` **Invariante (E)** —
Negativprobe in `c6c_bericht_selbsttest_freeze.md` §7.

**Was dieses Amendment NICHT tut, ausdrücklich:** es ändert **keine** Metrikdefinition,
**kein** Injektionsmanifest, **keine** Regeldatei, **keinen** Prompt und **kein** Schema
— die fünf Gegenstände der Sperre aus §0.1 Punkt 2. Es **beschreibt** einen Bytestand und
**legt eine Änderungssperre darauf**; kein Wert der §0.1-Tabelle bewegt sich, keine Zelle
der Erwartungsmatrix, kein Messergebnis.

Rev. 39: **T7 STEHT AUF DEN GEHASHTEN LAUFMANIFESTEN; Ausnahmeregel für lebende Dokumente;
Präzisierung der Blindheitsauflage (C6c-a), gesetzt VOR dem ersten Auswertungslauf über
`data/campaign/k*`.** Drei Festlegungen, eine Begründung.

**(1) Die Quelle von T7 wechselt.** T7.1, T7.2, T7.3 und T7.4 werden aus den
**Laufmanifesten** unter `data/campaign/manifests/` gerechnet — ein Manifest je Invocation,
**jedes von einem Block-`SHA256SUMS` bezeugt**. Gelesen wird je Invocation: `postrun.verdict`,
`postrun.detail.invalid_reasons`, `…calls_total`, `…calls_invalid`,
`…calls_transport_failed`, `…changed_files_count`, die K4/K5-Akzeptanzzähler und
`external_wall_clock_ms`; **`valid_final` ist kein Feld, sondern eine Ableitung** (gemessene
Calls = `calls_total` − `calls_transport_failed`, davon `calls_invalid` ab) und wird als
solche ausgewiesen. **Warum:** `journal.jsonl` und die Prosa-`MANIFEST.md` sind **ungehasht**
und bleiben es planmäßig (2). T7 ist aber die Tabelle, die den **Messbestand bezeugt** — sie
darf nicht auf Dateien ruhen, deren Bytestand kein `SHA256SUMS` deckt. **Beide bleiben
GEGENPROBE**, wie die Bildungsvorschrift des Skeletts sie namentlich nennt: verglichen werden
Invocationszahl, Zahl der gültigen Injektionen und die `n. e.`-Liste. **Weicht eine
Gegenprobe ab, ist das ein BEFUND** — gedruckt als `ABWEICHUNG` in T7, als Banner im Kopf der
Ausgabe und auf `stderr`; **keine Seite wird an die andere angeglichen**, und die Ausgabe ist
nicht zu verwenden, bevor geklärt ist, welche Seite falsch ist.

**Gemessen am 28.08.2026, alle drei Lesungen deckungsgleich:** K1 32/32, K2 32/32, K3 32/32
aus 61 Invocationen (29 INVALID, durchgehend `transport_failure`), K4 32/32, K5 32/32 —
**keine Injektion ohne gültigen Lauf, in keiner Konfiguration**, `n. e.` kommt in der
Kampagne nicht vor. `valid_final` über die gemessenen Calls: K2 96/96, K3 133/133, beide
1,000; das Validitäts-Gate 0,9 aus §7 ist nirgends unterschritten.

**(2) Lebende Dokumente bleiben ungehasht — entschieden, nicht offen.** Sieben Dateien in den
gehashten Beständen stehen in **keinem** `SHA256SUMS` und werden **nicht** aufgenommen:
`data/soll/MANIFEST.md`, `data/campaign/MANIFEST.md`, `data/campaign/README.md`,
`data/campaign/journal.jsonl`, `data/campaign/control/journal.jsonl`,
`data/campaign/k2/MANIFEST.md`, `data/campaign/k3/MANIFEST.md`. **`journal.jsonl` ist
append-only und wächst planmäßig; die `MANIFEST.md` sind fortzuschreibende Dokumente.** Ein
Hash wäre für sie das **falsche Instrument**: er risse bei **jeder legitimen** Fortschreibung
und erzöge dazu, ihn routinemässig nachzuziehen — womit der Detektor aufhört, einer zu sein.
**Integrität liefert die Commit-Historie**; der Schnappschuss-Hash im Manifest bleibt.
**Keine der sieben ist ein Laufartefakt**, und nach (1) ist keine mehr **Quelle** eines
T-Wertes. Der Prüfer meldet sie weiterhin bei **jedem** Lauf, aber als **bekannte,
entschiedene Ausnahme** mit Verweis auf diese Festlegung — **nicht als Fehlschlag**. Die
Liste steht **namentlich im Code** (`KNOWN_UNLISTED` in `tools/check_doc_invariants.py`),
damit eine **achte** ungelistete Datei auffällt: was weder gelistet noch auf der Liste ist,
ist ein **Fehlschlag**.

**(3) Die Blindheitsauflage ist präzisiert, nicht gelockert.** Gesperrt bleiben die **Funde**:
kein `--json-out`-Artefakt, kein Run-Log-Record, kein stdout/stderr der Kampagne. **Die
Laufmanifeste sind ausdrücklich ERLAUBT** — sie tragen Verdikte, Zähler und Provenienz,
**keine Funde**. Die **Selbstauditierung der Harness ist entsprechend angepasst, nicht
ausgeschaltet**, und dabei **schärfer** geworden: sie prüft jetzt gegen eine **positive
Erlaubnisliste** (Laufmanifeste, `journal.jsonl`, `MANIFEST.md`, `README.md`, `SHA256SUMS`)
statt gegen eine Aufzählung der fünf Blockordner. Jeder andere Pfad unter der
Kampagnenwurzel führt zu **Exit 3** — `data/campaign/control/` eingeschlossen, das die alte
Prüfung **gar nicht sah**. Negativ probiert in `c6ca_bericht_t7_quellen.md` §4.

**Was dieses Amendment NICHT tut, ausdrücklich:** es ändert **keine** Metrikdefinition,
**kein** Injektionsmanifest, **keine** Regeldatei, **keinen** Prompt und **kein** Schema —
die fünf Gegenstände der Sperre aus §0.1 Punkt 2. Es bewegt **keine Zelle** der
Erwartungsmatrix und **keinen Messwert**: dieselben T7-Zahlen werden aus einer **anderen,
bezeugten Datei** gelesen. **Mitgezogen:** die Auswertungsspezifikation (neues §1.8, §7.4
und §8 Punkt 9) mit ihrem SHA an **beiden** Stellen, und die drei Instrumentenhashes in
§0.1, weil `tools/evaluate_campaign.py` und `tools/check_doc_invariants.py` geändert sind
(§0.1 Punkt 6). **Zeitpunkt:** vor dem ersten Auswertungslauf über `data/campaign/k*`.

Rev. 40: **kein-EN WIRD AUF EINER AGGREGATIONSSTUFE GEBILDET; NEUE LÄUFESPALTE IN T4;
AUFSPALTUNG NACH URSACHE ABGELEHNT (C11b), gesetzt NACH dem ersten Auswertungslauf und
NACH der Diagnose C11a.** Vier Festlegungen.

**ZEITPUNKT UNGESCHMINKT.** Dieses Amendment folgt dem **ersten** Auswertungslauf
(`data/campaign/eval/c11_eval_full.*`, archiviert und gehasht) und der Diagnose **C11a**.
Es ist damit **nach** Sichtung von Ergebnissen gesetzt, und das ist hier festgehalten und
nicht beschönigt. Was es zulässig macht, ist die Art der Änderung: **es ist eine
Metrikbildung, keine Metrikdefinition.** Die Regel aus **Rev. 31** bleibt **wörtlich
stehen** — „ein `strict`-Treffer, der die Ruhezustandsrate **nicht übersteigt**, wird
nicht als Erkennungsnachweis geführt" —, und `strict`, `localized`, Precision, Recall,
F1, Median, Spannweite und die Falsch-Positiv-Rate bleiben **unangetastet**. Geändert
wird allein, **auf welcher Aggregationsstufe die beiden Seiten dieses einen Vergleichs
gebildet werden** — eine Frage, die Rev. 31 offengelassen hatte und die die Umsetzung in
C6b stillschweigend in zwei verschiedene Richtungen beantwortet hat (C11a §3.5). **Der
erste Lauf bleibt archiviert**, wird **nicht überschrieben** und wird in C11b
Zelle für Zelle gegenübergestellt (§0.1 Punkt 6: Ausweis beider Ergebnisse, nebeneinander,
nicht ersetzend).

**(a) DIE STUFE: die EXISTENZSTUFE.** kein-EN wird gebildet als

```
kein-EN = "ja"    wenn strict = 1  UND  Ruhe-Existenz = 1
        = "nein"  wenn strict = 1  UND  Ruhe-Existenz = 0
        = leer    wenn strict = 0                       (dritter Zustand, unverändert)

Ruhe-Existenz = 1, wenn die Ruhezustandszählgrösse desselben Moduls in derselben
                   Kategorie in MINDESTENS EINEM der drei C3b-Läufe grösser 0 ist.
```

**Begründung — warum diese und nicht die andere.** Der Wortlaut aus Rev. 31 macht **den
`strict`-Treffer zum Subjekt** des Vergleichs. `strict` ist nach **§4** ein
**Existenzquantor über die Repetitionen**, binär — das ist eine **Metrikdefinition** und
steht seit dem ersten Kampagnenlauf unter der Sperre aus §0.1 Punkt 2. Die Stufe, die der
Wortlaut trägt, ist folglich die Stufe des Subjekts: die **Existenzstufe**. Die
Kampagnenseite des Vergleichs **ist** der `strict`-Treffer; die Ruhezustandsseite wird auf
**dieselbe** Stufe gebracht. Damit ist die Auflage erfüllt, dass beide Seiten gleich
aggregiert sein müssen — und keine vorregistrierte Grösse muss dafür bewegt werden.

**Die beiden Kandidaten, gegenübergestellt — mit den Zeilen, die jeder von beiden bewegt.**
Gerechnet am 28.08.2026 aus den Kampagnenartefakten und `data/c3b-k2/`, `data/c3b-k3/`;
IST = Buchung des ersten Auswertungslaufs.

| | **Kandidat A — Existenzstufe** *(gewählt)* | **Kandidat B — Medianstufe** *(verworfen)* |
|---|---|---|
| Kampagnenseite | `strict` (Existenz über 3 Läufe) — **unverändert** | Median der `strict`-Treffer je Lauf, also „Treffer in ≥ 2 von 3 Läufen" |
| Ruhezustandsseite | Existenz über 3 C3b-Läufe | Median über 3 C3b-Läufe — unverändert |
| bewegte kein-EN-Zeilen K2 | **2** von 32 (I10, I12: `nein` → `ja`) | **1** von 32 (I19: `ja` → leer) |
| bewegte kein-EN-Zeilen K3 | **4** von 32 (I06, I20, I21: `ja` → `nein`; I30: `nein` → `ja`) | **3** von 32 (I06, I20, I21: `ja` → leer) |
| Richtung | **beide** — 3 Zeilen `ja` → `nein`, 3 Zeilen `nein` → `ja` | nur in **eine** Richtung: 4 Zeilen verlassen `ja` |
| bewegt eine **vorregistrierte** Zelle? | **nein** | **JA — vier `strict`-Zellen** (I06/K3, I19/K2, I20/K3, I21/K3 fielen von 1 auf 0) und damit T1, T2, T4 und T5 mit |

**Kandidat B ist deshalb nicht wählbar**, unabhängig davon, welche Zahlen er erzeugt: er
verschiebt eine **Metrikdefinition** nach Sichtung der Daten, und genau das schliesst
§0.1 Punkt 2 aus. Die Begründung steht **vor** den Zahlen und nicht hinter ihnen.

**Was die Wahl bewirkt, ausdrücklich und ohne Beschönigung.** Sie **verschiebt Fälle in
beide Richtungen** und **verbessert kein Ergebnis**: bei K2 steigt die Zahl der Zeilen
ohne Erkennungsnachweis von **20 auf 22**, bei K3 sinkt sie von **4 auf 2**. „kein
Erkennungsnachweis" ist die für das Werkzeug **ungünstige** Buchung; die Wahl macht sie
für K2 häufiger und für K3 seltener. Eine Stufe, die für beide Konfigurationen in
dieselbe Richtung wirkte, wäre begründungsbedürftig — diese tut es nicht.

**Was NICHT geändert wird, ausdrücklich.**
- **Die Spalten `Ruhe`, `Kampagne` und `Δ` bleiben auf dem Median.** Sie sind die
  **paarweise Auslesart** aus Rev. 31 §7.5 (4) — eine eigenständig vorregistrierte
  Grösse mit eigener Bildungsvorschrift („Berichtsform Grössenordnungen", „auch null und
  negativ wird berichtet"), **nicht** der kein-EN-Vergleich. Beide Seiten dieser Grösse
  sind bereits gleich aggregiert (Median gegen Median); an ihr ist nichts zu reparieren.
  Seit diesem Amendment liest kein-EN sie **nicht mehr**.
- **Der Filterunterschied bleibt bestehen und wird nicht mitverschoben.** `strict` filtert
  über den vierteiligen `match_key` (§4), die Ruhezustandszahl über **Trägermodul und
  Kategorie** (Rev. 31, §7.5 (3)). Beide Filter sind **vorregistriert**, jeder an seiner
  Stelle; dieses Amendment betrifft die **Aggregationsstufe**, nicht den Filter. Der
  Unterschied ist hiermit **benannt** und bleibt als Lesevorbehalt an der Spalte stehen.
- **`strict` selbst bleibt unverändert** — Existenzquantor, binär, §4.

**(b) NEUE SPALTE IN T4: die drei Repetitionswerte einzeln.** Je Konfiguration (K2, K3)
trägt T4 eine neue Spalte **Läufe (Ruhe · Kampagne)**, die die Zählwerte der **drei
Repetitionen einzeln** ausweist — `[0,0,0] · [0,0,1]` statt zweier Mediane `0` und `0`.
**Rein deskriptiv:** keine Wertung, keine neue Aggregation, keine neue Metrik, kein
Eingang in irgendeine Rechnung. **Zweck:** die Aggregationsstufe wird an der Tabelle
**lesbar**. Ein Median 0 über `[0,0,1]` und ein Median 0 über `[0,0,0]` sind in der
bisherigen Fassung dieselbe gedruckte Null; die Spalte macht den Unterschied sichtbar,
aus dem die Buchung von kein-EN folgt. Das Skelett `kapitel7_tabellenskelette.md` (T4
Hauptteil) und die Auswertungsspezifikation §7.5 sind entsprechend nachgezogen.

**(c) kein-EN WIRD NICHT NACH URSACHE AUFGESPALTEN — ausdrücklich abgelehnt.** C11a §3.6
hat festgestellt, dass die kein-EN-Fälle **nicht durchgehend denselben mechanischen
Auslöser** haben: bei K2 durchweg eine Ruhezustandsrate ≥ 1, bei K3 in drei von vier
Fällen ein Nullwert auf beiden Seiten. Eine zusätzliche Spalte, die kein-EN nach dieser
Ursache in „Rauschen" und „Instabilität" trennte, **wird nicht eingeführt**. **Warum:**
das wäre eine **neue Klassifikation, gebildet nach Sicht auf die Daten** — die Klassen
existierten vor dem ersten Lauf nicht, ihre Namen kämen aus der Betrachtung der Ergebnisse,
und ihre Grenze wäre an genau den Zeilen gezogen, die sie sortieren soll. Das ist der Fall,
den §0.1 Punkt 4 beschreibt: nachträglich nicht mehr von einer an den Daten gewählten
Festlegung zu unterscheiden. **Wohin der Unterschied stattdessen gehört:** in die
**Prosa von Kapitel 7**, belegt aus der neuen Läufespalte (b), die die Rohwerte offenlegt
und den Leser die Unterscheidung selbst nachvollziehen lässt — als **Beschreibung**, nicht
als **Buchung**.

**(d) Mitgezogen:** die Auswertungsspezifikation (§7.5 (3) präzisiert, §7.5 (5) neu) mit
ihrem SHA an **beiden** Stellen (§0.1 und §1 Nachtrag Rev. 30), das Tabellenskelett T4,
und — nach der Instrumentenreparatur derselben Auftragsphase — die drei Instrumentenhashes
in §0.1 (§0.1 Punkt 6).

Rev. 41: **HASH-NACHZUG DER AUSWERTUNGSINSTRUMENTE nach der Reparatur (C11b), gesetzt
NACH dem ersten Auswertungslauf und VOR dem zweiten.** Ein reiner Bytestandsnachzug — und
nach §0.1 Punkt 5 deshalb **eine eigene Revision**: „jede Änderung am Protokoll ist eine
Revision, auch ein reiner Hash-Nachzug, auch eine Änderung, die inhaltlich nichts
verschiebt". Rev. 40 hatte den Nachzug angekündigt; **vollzogen** wird er hier, und wäre er
unter derselben Nummer vollzogen worden, stünde der Bytestand von Rev. 40 in keinem
Dokument mehr — genau der Ausfall, aus dem Rev. 36 diese Regel gemacht hat.

**Zwei der drei Instrumente sind geändert**, `tools/check_doc_invariants.py` ist unberührt:

| Datei | vorher (Rev. 39) | nachher (Rev. 41) |
|---|---|---|
| `tools/evaluate_campaign.py` | `5125cd59…0528eed` | **`20bcdae0…23d306`** |
| `tools/match_k4k5.py` | `ad3edcb1…fc060022` | **`c16e7c43…799f4ca6`** |
| `tools/check_doc_invariants.py` | `6cc16ef9…1e52b7018` | **unverändert** |

**Der Anlass ist die Defektklausel aus §0.1 Punkt 6** — „zulässig ist allein die Behebung
eines Defekts, und zwar mit vollständiger Neuauswertung und Ausweis beider Ergebnisse".
Behoben sind die in `c11a_bericht_diagnose.md` §7 aufgelisteten Punkte:

- **R8/R7** die Buchung der vorregistrierten Sonderklasse **T9 Fall 7** (K5/`CYCLE`): der
  Join verwarf sie an zwei Zeichenkettenvergleichen, und der T9-Zähler las aus dem falschen
  Eimer. Repariert **über die Klassifikation des Parsers**, nicht am Literal: `match_k4k5.py`
  benennt sein `localized`-Vokabular und trägt eine **benannte Sonderklasse**.
- **R2** gerechnete Nullen wurden über `len(hits) or ''` als **leere Zelle** gedruckt.
- **R1** neue Zusicherung: **keine markerfreie Leerzelle** in irgendeiner Tabelle, geprüft
  am **fertig gerenderten** Text, Exit 2.
- **R3/R4** T5 (Precision/Recall/F1) und T6 (Laufkosten) waren **nicht implementiert** bzw.
  **nicht gerendert**; 165 + 31 Zellen.
- **R5** T4-Symmetrieteil für K1/K4/K5; dabei ein **Defekt der Zählgrösse** behoben, die auf
  dem K1-Pfad auf `category_l1` filterte und dort **nie** traf.
- **R6** T1-Abweichungsspalte: Rechenweg geschaffen, Soll gegen Ist je Zeile.
- **R9** T9 in Skelettform: sieben Zeilen, sieben Nummern, Spalte *vorregistriert in*.
- die **laufweise** Bildung der `strict`-Falsch-Positiven nach §3.2 — sie wurde über die
  Läufe hinweg gebildet und machte aus einem in der nächsten Repetition **wiederholten
  richtigen** Treffer ein Falsch-Positiv. Folgenlos, solange T5 leer war.
- die Umsetzung von **Rev. 40** (kein-EN auf der Existenzstufe, Läufespalte).

**KEINE Rechenregel und KEIN Marker ist verschoben worden**, wie §0.1 Punkt 6 es verlangt:
`strict`, `localized`, Precision, Recall, F1, Median, Spannweite, die Falsch-Positiv-Rate
und die vier Marker ` — ` / `n. b.` / `n. e.` / *(leer)* stehen unverändert. Bewegt sind
**Buchungswege, Rechenwege, die dort fehlten, und die Darstellung**. **Belegt, nicht
behauptet:** die Handrechnung zu den reparierten Stellen ist **vor** der Reparatur und
**allein** committet (`tests/fixtures/harness/EXPECTED.md` §11–§15, Commit `c8e31d4`), die
Harness ist danach dagegen gelaufen, und Selbsttest B reproduziert unverändert K2 49/52 und
461, K3 1/52 und 3.

**Der erste Auswertungslauf bleibt archiviert, gehasht und unverändert**
(`data/campaign/eval/c11_eval_full.*`); der zweite tritt **daneben**, nicht an seine Stelle.

Rev. 42: **DIE FORDERUNG NACH MEDIAN UND SPANNWEITE IN DER P/R/F1-TABELLE IST
GEGENSTANDSLOS UND DAMIT ERLEDIGT — sie wird NICHT abgewiesen.** Skelett T5 (ii) und
Auswertungsspezifikation §7.5 Punkt 1 verlangten für K2/K3 zusätzlich **Median und
Spannweite über drei Läufe**. Die Anforderung **hat keinen Gegenstand**: Median und
Spannweite setzen eine **laufweise** Grösse voraus, über die gestreut werden kann;
Precision, Recall und F1 dieser Tabelle stehen auf `strict` und `localized`, und `strict`
ist nach Spezifikation **§3** ein **Existenzquantor über die Repetitionen** — die Grösse ist
über die drei Läufe hinweg **definiert** und hat konstruktiv **keine Verteilung über Läufe**.

**Warum das nicht durch eine laufweise Fassung zu heilen ist.** Eine laufweise Precision
verlangte eine laufweise `strict`-Grösse. Die gibt es nicht als andere Auslesart derselben
Metrik — sie wäre eine **zweite Metrikdefinition**, und Metrikdefinitionen sind seit dem
ersten Kampagnenlauf **gesperrt** (§0.1 Punkt 2). Die Anforderung zu „erfüllen" hiesse also,
die Sperre zu brechen; sie stehenzulassen hiesse, eine dauerhaft unerfüllbare Forderung als
offene Lücke zu führen. Beides ist falsch, und beides ist hier vermieden.

**Wo die Laufstreuung stattdessen steht — und zwar feiner.** Mit **Rev. 40** trägt **T4** die
Spalte **Läufe (Ruhe · Kampagne)**: die Zählgrösse für **jede der drei Repetitionen einzeln**,
Form `[0,0,1]` (Spezifikation §7.5 (5)). Was die Anforderung sichtbar machen wollte — ob die
LLM-Konfigurationen zwischen den Repetitionen streuen —, ist damit **je Repetition** in der
Ausgabe, nicht zu einem Median zusammengezogen. Die Anforderung **entfällt gegenstandslos**,
sie wird nicht abgewiesen.

**Nicht berührt: die Falsch-Positiv-Raten-Tabelle.** Spezifikation §7.5 Punkt **2** führt
Median und Spannweite über drei Läufe für K2/K3 **unverändert** weiter — die Headline-Rate ist
dort eine **je Lauf** gebildete Grösse (§7.1), und an ihr rührt dieses Amendment nicht. T3
druckt Median und Spannweite wie bisher.

**KEINE Metrikdefinition ist geändert.** `strict`, `localized`, Precision, Recall, F1,
Median, Spannweite, die Falsch-Positiv-Rate und die vier Marker ` — ` / `n. b.` / `n. e.` /
*(leer)* stehen unverändert; **kein** Injektionsmanifest, **keine** Regeldatei, **kein**
Prompt, **kein** Schema ist berührt. Dieses Amendment **beschreibt** eine Eigenschaft, die
`strict` seit §3 hat, und zieht die Folge daraus — es **legt nichts fest**, was nicht schon
galt (Sperre §0.1 Punkt 2). **Kein Re-Run** folgt daraus: keine Zelle rechnet anders.

**(a) Mitgezogen:** die Auswertungsspezifikation (§7.5 Punkt 1 mit Nachtrag) mit ihrem SHA an
**beiden** Stellen — §1 (Nachtrag Rev. 30) und §0.1 (Messstand) —, im **selben Commit** wie
die Spezifikationsänderung; das Tabellenskelett T5 (ii).

**(b) Der Aufschrieb aus Phase 1 desselben Auftrags berührt KEINEN gehashten Wert.** Die
Zeilenbeschriftung der beiden T5-Gesamtzeilen ist in `docs/kapitel/kapitel7_tabellenskelette.md`
korrigiert worden (Aufschriebfehler nach Skelett §0.3 (B), Alttext gestrichen). Das
Tabellenskelett ist **kein** gehashtes Dokument: es steht **weder** in §0.1 **noch** in
`data/soll/SHA256SUMS` **noch** unter `data/campaign`, und es ist **keines** der drei
Auswertungsinstrumente. Die Korrektur bewegt deshalb **weder** den Protokoll-SHA **noch** den
Spezifikations-SHA **noch** einen Instrumentenhash **noch** eine `SHA256SUMS`-Zeile; sie ist
hier vermerkt, damit die Bewegungsprüfung nicht nach einem Nachzug sucht, den es nicht gibt.

Rev. 43: **HASH-NACHZUG DER AUSWERTUNGSINSTRUMENTE nach der Darstellungsreparatur
(C11c), gesetzt NACH dem zweiten Auswertungslauf und VOR dem dritten.** Ein reiner
Bytestandsnachzug — und nach §0.1 Punkt 5 deshalb **eine eigene Revision**, nicht unter
Rev. 42 mitvollzogen: läge er dort, stünde der in `c5b_bericht_protokoll_freeze.md` §3
bezeugte Bytestand von Rev. 42 **in keinem Dokument mehr**. Genau der Ausfall aus C6b-2b,
aus dem Rev. 36 diese Regel gemacht hat, und dieselbe Trennung wie zwischen Rev. 40 und
Rev. 41.

**Ein Instrument ist geändert**, `tools/match_k4k5.py` und `tools/check_doc_invariants.py`
sind unberührt:

| Datei | vorher (Rev. 41) | nachher (Rev. 43) |
|---|---|---|
| `tools/evaluate_campaign.py` | `20bcdae0…23d306` | **`eb206a6f…b520653`** |
| `tools/match_k4k5.py` | `c16e7c43…799f4ca6` | **unverändert** |
| `tools/check_doc_invariants.py` | `6cc16ef9…1e52b7018` | **unverändert** |

**Der Anlass ist wieder die Defektklausel aus §0.1 Punkt 6** — und die Defekte sind
diesmal **ausschliesslich darstellend**. Behoben sind die beiden in
`c11b_bericht_zweiter_lauf.md` §7 ausgewiesenen und nicht behobenen Punkte, plus die zwei
Zellen derselben Klassen, die die Nachschau über alle Tabellen gefunden hat:

- **D1** T5 druckte seine Marker **ohne Code-Auszeichnung** (72 Zellen im zweiten Lauf):
  `Score.cells()` gab den rohen Markerstring zurück, während jede andere Tabelle über
  `Cell.text` lief. Ein Marker ohne Auszeichnung ist von Prosa nicht zu unterscheiden, und
  die drei Marker tragen drei verschiedene Aussagen (Skelett §1.1). **`marker_text()` ist
  jetzt die einzige Stelle**, die einen Marker rendert.
- **D2** T6 druckte zwei K3-Millisekundensummen in **Exponentialschreibweise**
  (`9.19054e+06 ms`) — der `%g`-Rückfall oberhalb von sechs signifikanten Stellen.
  **`plain()`** rendert denselben Wert ohne Exponent; alle übrigen `%g`-Aufrufstellen
  laufen darüber.
- **D3** Nachschau über **alle** Tabellen nach beiden Klassen: **zwei** weitere Zellen —
  die Headline-Zellen der findingweisen T3-Zeilen trugen einen **blossen Gedankenstrich**.
  **Nur die Auszeichnung** ist ergänzt; die Zelle sagt, was sie vorher sagte. Gedankenstriche
  **in Fliesstext** (T9-Buchungsregeln, Spalte „fällt auseinander?") sind Interpunktion,
  keine Marker, und bleiben unangetastet.
- **R10**, neue Zusicherung, geprüft am **fertig gerenderten** Text wie R1: **kein Marker
  ohne Code-Auszeichnung, keine Zahl in Exponentialform**, Exit 2.

**KEINE Rechenregel, KEIN Filter, KEIN Nenner und KEINE Aggregationsstufe ist berührt.**
`strict`, `localized`, Precision, Recall, F1, Median, Spannweite, die Falsch-Positiv-Rate
und die vier Marker ` — ` / `n. b.` / `n. e.` / *(leer)* stehen unverändert; verschoben ist
allein die **Notation** auf bereits gerechnetem Text. **Belegt, nicht behauptet:**
`match_k4k5.py --selftest` 34 von 34, Selbsttest B unverändert (K2 **49/52** und **461**,
K3 **1/52** und **3**), der Fixture-Lauf zeigt **60** geänderte Zellen — **50** reine
Auszeichnung, **10** die Zeilenbeschriftung aus Rev. 42 desselben Auftrags —, und jede
Zusicherung ist negativ probiert, R10 in **beiden** Hälften.

**Die Gegenüberstellung ist das Kriterium:** der dritte Lauf muss nach Entfernen der
Backticks und Umwandlung der Exponentialzahlen zum zweiten **zeichengleich** sein. Jede
Wertänderung wäre ein Abbruchgrund und ist zu melden, nicht zu erklären
(`c11c_bericht_dritter_lauf.md` §5).

**Der erste und der zweite Auswertungslauf bleiben archiviert, gehasht und unverändert**
(`data/campaign/eval/c11_eval_full.*`, `c12_eval_full.*`); der dritte tritt **daneben**,
nicht an ihre Stelle.

Rev. 44: **DIE ARTEFAKTAUSWAHL STEHT AUF DEM LAUFVERDIKT, NICHT AUF DEM DATEINAMEN;
OVERLAP-TABELLE T10 REGISTRIERT; ÜBERHOLTER T5-VERMERK IM RENDERER NACHGEZOGEN (C14),
gesetzt NACH dem dritten Auswertungslauf und VOR dem vierten.**

**(a) Der Defekt, ungeschminkt benannt.** Bis einschliesslich des dritten
Auswertungslaufs löste `evaluate_campaign.campaign_artifact` das je Paar (Konfiguration,
Injektion) zu lesende Artefakt über den Glob `<cfg>_*<injection_sha256>.json` auf. Der
trifft die Datei **ohne** `_r<n>`-Suffix, also den **ersten** Versuch. Für **elf**
K3-Injektionen — **I05, I06, I07, I09, I11, I13, I16, I20, I21, I22, I23** — trägt genau
dieses Artefakt im gehashten Laufmanifest `postrun.verdict = INVALID` mit dem Grund
`transport_failure`. K2 ist nicht betroffen (null Wiederholungen). Ausgezählt in
`c11d_bericht_befund08_grundlagen.md` §A6b — **durch eine mechanische Auszählung, die vor
dem Befund beauftragt war**, nicht durch eine Suche nach ihm.

**Was damit verletzt ist, wörtlich aus §7 dieses Protokolls:**

> „liegt `valid_final` einer LLM-Konfiguration unter 0.9, wird das als Befund dokumentiert
> und die Konfiguration mit den vorhandenen validen Läufen ausgewertet — nicht
> nachgebessert. Operationalisierung: `valid_final=false`-Läufe sind über Exit-Code 3 bzw.
> das persistierte Run-Log (CLI-Inkremente 2 und 4) identifizierbar; **stille Zählung
> invalider Läufe als „0 Findings" ist damit ausgeschlossen**."

**Genau das ist in der Auswertung geschehen.** Elf Artefakte, deren Laufmanifest sie als
ungültig ausweist, sind in die Trefferrechnung eingegangen; eines davon (I23) trägt
`calls_transport_failed: 3`, Exit 3 und **null Records**, und wurde als Nichttreffer
gebucht. **T7 wies die Gültigkeit dabei die ganze Zeit korrekt aus** — T7.4 listet alle
29 ungültigen Invocationen namentlich, T7.3 meldet null Injektionen ohne gültigen Lauf.
Die Auswertung las **an ihrer eigenen, richtig gedruckten Gültigkeitstabelle vorbei**.

**Und die Stufe toleriert das nicht.** Z3 ist als **kontrolliertes Experiment**
registriert (`00_stand_und_entscheidungen.md` §5, `methodik_begruendung` §6). Auf dieser
Evidenzstufe ist die Auswahl der ausgewerteten Läufe Teil des Messverfahrens, nicht eine
Implementierungsbeiläufigkeit.

**Die Richtung, benannt und nicht umschrieben: die Reparatur wird die K3-Zahlen
voraussichtlich VERBESSERN.** Zehn der elf ersetzten Artefakte tragen weniger Records als
der jeweils gültige Versuch tragen kann, eines gar keine. Vier Gründe tragen die Reparatur
trotz dieser Richtung, jeder für sich:

1. **Die verletzte Regel war vorregistriert** — §7, oben wörtlich zitiert, seit Rev. 33
   eingefroren. Nichts daran ist nach Sichtung der Daten formuliert.
2. **Der Defekt fiel durch eine vor dem Befund beauftragte mechanische Auszählung auf**
   (C11d A6b) — nicht durch die Suche nach einer Erklärung für eine unbefriedigende Zahl.
3. **Es ist eine Artefaktauswahl, KEINE Metrikänderung.** `strict`, `localized`,
   Precision, Recall, F1, Median, Spannweite, die Falsch-Positiv-Rate und die vier Marker
   stehen zeichengleich. Bewegt hat sich allein, **welche Datei** dieselbe, unveränderte
   Metrik liest.
4. **C11, C12 und C13 bleiben archiviert, gehasht und unverändert** und werden dem vierten
   Lauf **gegenübergestellt** — nicht ersetzt (§0.1 Punkt 6: Ausweis beider Ergebnisse,
   nebeneinander).

**Die in C13 gedruckte T1-Abweichung „K3: Soll ja / Ist teilweise"** bei
`FRAMEWORK_TYPE_IN_SIGNATURE` ist nach derzeitigem Stand ein **Artefakt der
Dateiauswahl**: das gelesene Artefakt von I23 trägt `calls_transport_failed: 3`, Exit 3
und null Records (C11d §A6.1). **Ob sie bestehen bleibt oder entfällt, zeigt der vierte
Lauf.** Hier wird das **nicht vorweggenommen**; das Ergebnis wird berichtet, wie es
ausfällt.

**Registriert wird die Regel, nicht das Ergebnis:** für jedes Paar (Konfiguration,
Injektion) liest die Auswertung das Artefakt, dessen **Laufmanifest**
`postrun.verdict == VALID` trägt; bei mehreren gültigen Versuchen der **früheste**
(kleinster `attempt`); bei keinem gilt **`n. e.`** mit Eintrag in **T7.3**. Die Auswahl
wird aus dem **gehashten Laufmanifest** entschieden — **nicht** aus dem Dateinamen und
**nicht** aus der Zahl der Records. Dazu die Zusicherung **R12**: der Lauf bricht mit
**Exit 2** ab, wenn ein Artefakt gelesen wird, dessen Laufmanifest ein Verdikt ≠ `VALID`
trägt. **R12 ist der Riegel gegen die Wiederholung und trägt weiter als die Reparatur
selbst** — sie ist unabhängig vom Auswähler formuliert und fragt die **gelesenen
Dateien**. Ausgenommen und ausdrücklich benannt: die Run-Logs `*.jsonl`, die **T6** über
**alle** Invocationen liest — Laufkosten sind angefallen, gültig oder nicht; sie tragen
keine Trefferzelle. **T6 bewegt sich durch diese Revision nicht.**
Fundstelle: Auswertungsspezifikation **§1.9** (neu).

**(b) Overlap-Tabelle T10 — die Lücke gegen §8.** §8 verlangt für **UF3** eine
„Overlap-Analyse K1/K4/K5 vs. K2/K3"; `c11d_bericht_befund08_grundlagen.md` §B5 hat
belegt, dass die registrierte Ausgabe keine enthält. Sie wird als **T10** registriert —
in `kapitel7_tabellenskelette.md` (neuer Abschnitt T10, Druckreihenfolge Position 10,
§0.3-Zuordnung, Anhangzeile **A-39**) und in der Auswertungsspezifikation (**§8 Punkt
10**). **Basis sind die BEREITS GERECHNETEN Trefferzellen: keine neue Metrik, keine neue
Schwelle, keine neue Vergleichsvorschrift, kein neuer Nenner.** `localized` und `strict`
stehen in **getrennten** Teiltabellen (**T10a**/**T10b**). **K2 und K3 werden NICHT zu
„dem LLM-Pfad" vereinigt** — je LLM-Konfiguration eine eigene Zeilengruppe. Die
**Baselineseite ist eine Vereinigung** von K1, K4 und K5, zulässig, weil die Arbeit sie
als Baseline-Menge führt, und in Kopf und Zelle **als Vereinigung benannt**. Je Injektion
vier Zustände: **nur Baseline · nur die LLM-Konfiguration · beide · keiner**.
**Markerdisziplin:** eine Injektion, die eine Seite nach **T8** nicht **ausdrücken** kann,
ist dort **nicht verfehlt**; solche Fälle stehen in einer eigenen Klasse („für diese Seite
nicht ausdrückbar") und werden **nie** in „nur die andere Seite" umgedeutet — sonst würde
Ausdrucksmächtigkeit zu Leistung, was das G2-Reframing (**B17**) ausschliesst. Ebenso
gehen `n. b.`, `n. e.` und die vorregistrierten Sonderklassen **T9 Fall 6/7** weder als
Treffer noch als Verfehlung ein. **Aggregatzeile je Gruppe mit ausgewiesenem Nenner**, wie
in T5. Nach Skelett §0.3 ist T10 eine **gerechnete** Tabelle und **kein Aufschrieb**: sie
trägt keinen vorgegebenen Wert und erzeugt keine Abweichungszeile.

**(c) Der überholte T5-Vermerk im Renderer.** Die Ausgabe druckte an T5 weiterhin
„**LÜCKE, benannt und nicht gefüllt**", während Skelett T5 (ii), Auswertungsspezifikation
§8 Punkt 1 und dieses Protokoll die Anforderung seit **Rev. 42** als **gegenstandslos
erledigt** führen (C11c §2). Der Text der Harness wird mit **R14** auf die Rev.-42-Begründung
nachgezogen: die Anforderung wird **nicht abgewiesen**, sie **entfällt** — `strict` ist nach
Spezifikation §3 ein Existenzquantor über die Repetitionen und hat konstruktiv keine
Verteilung über Läufe; die Laufstreuung steht seit **Rev. 40** je Repetition **einzeln** in
der T4-Spalte „Läufe (Ruhe · Kampagne)". **Keine Zelle bewegt sich**, es ist eine
Textänderung an bereits gerechnetem Text.

**Was diese Revision NICHT tut.** Keine Metrikdefinition, kein Injektionsmanifest, keine
Regeldatei, kein Prompt und kein Schema ist berührt — die fünf Gegenstände der Sperre aus
§0.1 Punkt 2 stehen unangetastet. **Kein Artefakt unter `data/campaign/k*` bewegt sich**;
der vierte Lauf ist eine **vollständige Neuauswertung über den unveränderten
Kampagnenbestand**, keine Neumessung. Die Instrumenten-Hashes werden **nicht** unter
dieser Nummer nachgezogen — das ist nach §0.1 Punkt 5 eine **eigene** Revision (Präzedenz
Rev. 36, Rev. 41, Rev. 43).

Rev. 45: **HASH-NACHZUG DER AUSWERTUNGSINSTRUMENTE nach der Umsetzung von R11–R14
(C14), gesetzt NACH dem dritten Auswertungslauf und VOR dem vierten.** Ein reiner
Bytestandsnachzug — und nach §0.1 Punkt 5 deshalb **eine eigene Revision**, nicht unter
Rev. 44 mitvollzogen: läge er dort, stünde der in `c5b_bericht_protokoll_freeze.md` §3
bezeugte Bytestand von Rev. 44 **in keinem Dokument mehr**. Dieselbe Trennung wie
zwischen Rev. 40 und Rev. 41 und zwischen Rev. 42 und Rev. 43.

**Ein Instrument ist geändert**, `tools/match_k4k5.py` und `tools/check_doc_invariants.py`
sind unberührt:

| Datei | vorher (Rev. 43) | nachher (Rev. 45) |
|---|---|---|
| `tools/evaluate_campaign.py` | `eb206a6f…b520653` | **`b66be750…9a93428`** |
| `tools/match_k4k5.py` | `c16e7c43…799f4ca6` | **unverändert** |
| `tools/check_doc_invariants.py` | `6cc16ef9…1e52b7018` | **unverändert** |

**Der Anlass ist die Defektklausel aus §0.1 Punkt 6.** Umgesetzt sind die vier in
Rev. 44 registrierten Punkte:

- **R11** — die Artefaktauswahl je Paar (Konfiguration, Injektion) entscheidet
  `postrun.verdict` des gehashten Laufmanifests, bei mehreren gültigen Versuchen der
  **früheste**; der Pfad folgt aus dem **Manifestnamen**, nicht aus einem Glob. Die
  Injektions-SHA bleibt in Gebrauch, aber als **Gegenprobe**: das Manifest des gewählten
  Versuchs muss denselben Commit nennen wie das Injektionsmanifest.
- **R12** — Zusicherung, **Exit 2**, wenn ein Artefakt gelesen wurde, dessen Laufmanifest
  ein Verdikt ≠ `VALID` trägt oder das gar kein Manifest hat. **Unabhängig vom Auswähler
  formuliert:** sie fragt die **gelesenen Dateien**. Ausgenommen und benannt: die Run-Logs
  `*.jsonl`, die T6 über **alle** Invocationen liest.
- **R13** — **T10** gerendert, zwei Teiltabellen (`localized`, `strict`), je zwei
  Zeilengruppen (K2, K3), Baselineseite als **benannte Vereinigung** K1 ∪ K4 ∪ K5,
  Aggregatzeile mit ausgewiesenem Nenner, dazu die Buchungsprobe als **Exit 2**.
- **R14** — der Vermerk an T5 druckt die **Rev.-42-Begründung** statt „LÜCKE, benannt und
  nicht gefüllt". **Keine Zelle bewegt sich.**

**KEINE Rechenregel, KEIN Filter, KEIN Nenner und KEINE Aggregationsstufe ist berührt.**
`strict`, `localized`, Precision, Recall, F1, Median, Spannweite, die
Falsch-Positiv-Rate und die vier Marker stehen unverändert; bewegt hat sich, **welche
Datei** dieselbe Metrik liest, und T10 weist eine bereits gerechnete Zelle ein zweites
Mal, schnittweise, aus. **Belegt, nicht behauptet:** `match_k4k5.py --selftest` **34 von
34**; Selbsttest B unverändert (K2 **49/52** und **461**, K3 **1/52** und **3**); der
Fixture-Lauf reproduziert **jede** Metrikzelle von T1–T5, T8 und T9 **zeichengleich**
gegen den Stand vor C14 — bewegt sind allein die T6/T7-Zahlen der neuen
Fixture-Invocationen, der T5-Vermerk und die neue T10; die Zuordnung
(Baselinezustand, LLM-Zustand) → Klasse ist gegen alle **16** Paare der handgerechneten
Tabelle geprüft (`tests/fixtures/harness/EXPECTED.md` §16.4); jede Zusicherung ist
negativ probiert, **R12 gegen den echten Bestand mit elf Verstössen und Exit 2**.

**Der erste, zweite und dritte Auswertungslauf bleiben archiviert, gehasht und
unverändert** (`data/campaign/eval/c11_eval_full.*`, `c12_*`, `c13_*`); der vierte tritt
**daneben**, nicht an ihre Stelle.

Rev. 46: **DIE KÜRZUNGSREIHENFOLGE „ZUERST Z4, DANN Z2" IST IN §7 ALS ÜBERHOLT
GESTRICHEN (G1, 31.08.2026).** Anlass ist der **Scope-Gate selbst**: er ist am
31.08.2026 am Termin geprüft und entschieden — **das Kriterium ist erfüllt, Variante C
bleibt, Z2 fällt nicht** (`docs/planung/gate_notiz_2026-08-31.md`; Belege: Kampagne
27./28.08.2026 mit 32 von 32 gültigen Injektionen je Konfiguration,
`c10_bericht_kampagne.md` §2.1/§4.1; vier Auswertungsläufe, kanonisch `c14`,
`data/campaign/eval/README.md`; **Befund 08**, `docs/befunde_log.md`).

**Warum die Reihenfolge fällt.** Der Gate ist ein **binärer Kalendermechanismus** mit
Stichtag 31.08.2026 und liegt **konstruktiv vor Z4s Slot** (Arbeitsplan Rev. 1, Block 6:
Z4 am 11.09.). Am Stichtag ist Z4 noch nicht gelaufen; ein negativer Ausgang streicht
unmittelbar Z2, ohne Zwischenstufe. Die Reihenfolge **konnte nie zur Anwendung kommen** —
die in `00_stand_und_entscheidungen.md` §3 seit dem 04.08.2026 als **offen** geführte
Inkonsistenz. **Z4 wird ab sofort eigenständig entschieden, nicht über den Gate**:
Demonstration, nie „Fallstudie", ohne P/R-Messung, erst nach dem Schreibblock, falls Zeit
bleibt (`00_stand_und_entscheidungen.md` §4/§5).

**KEINE Metrikdefinition, KEIN Injektionsmanifest, KEINE Regeldatei, KEIN Prompt und KEIN
Schema ist berührt; kein Re-Run folgt.** §7 ist die Entscheidungs- und Stop-Regel-Sektion;
bewegt hat sich **eine Scope-Klausel**, keine Rechenvorschrift. Der Messstand §0.1, die
Matching-Regel §4, die Metriken §5 und der Ablauf §6 sind **unberührt**; die drei
Instrumentenhashes stehen unverändert auf den Werten von Rev. 45. Der Rest von §7 —
Eine-Iteration-Regel, Validitäts-Gate 0.9, API-Fehlerregel, Erwartungsmatrix-Regel und
der Schlüsselvorfall-Nachtrag Rev. 27 — steht **wörtlich unverändert**.

Rev. 47: **HASH-NACHZUG VON `tools/check_doc_invariants.py` nach der Aufnahme der
Z1-Invariante (F) (Z1-P, 31.08.2026).** Ein reiner Bytestandsnachzug — und nach §0.1
Punkt 5 deshalb **eine eigene Revision**, nicht unter Rev. 46 mitvollzogen: läge er dort,
stünde der in `c5b_bericht_protokoll_freeze.md` §3 bezeugte Bytestand von Rev. 46 **in
keinem Dokument mehr**. Dieselbe Trennung wie zwischen Rev. 40 und Rev. 41, Rev. 42 und
Rev. 43, Rev. 44 und Rev. 45.

**Ein Instrument ist geändert**, `tools/evaluate_campaign.py` und `tools/match_k4k5.py`
sind unberührt:

| Datei | vorher (Rev. 45) | nachher (Rev. 47) |
|---|---|---|
| `tools/evaluate_campaign.py` | `b66be750…9a93428` | **unverändert** |
| `tools/match_k4k5.py` | `c16e7c43…799f4ca6` | **unverändert** |
| `tools/check_doc_invariants.py` | `6cc16ef9…1e52b7018` | **`c351a137…2b8707fdf`** |

**Der Anlass liegt ausserhalb dieses Protokolls.** Das Z1-Protokoll
`docs/protokolle/z1_protokoll_extraktionsvergleich.md` ist am 31.08.2026 zur
Vorregistrierung geschrieben und eingefroren worden (Auftrag Z1-P); sein Bytestand wird
— wie der dieses Protokolls — in einem eigenen Bericht bezeugt
(`z1_p_bericht_freeze.md` §3), weil ein Selbstbezug im gehashten Dokument unmöglich ist.
Der Prüfer bekommt dafür die **Invariante (F)**: SHA256 des Z1-Protokolls gegen den dort
als aktuell geführten Wert, in derselben Tabellenform, die (A) für dieses Protokoll liest.
Die Leseroutine der §3-Tabelle ist dafür um zwei Parameter erweitert und wird von (A) und
(F) geteilt; **(A) liest weiterhin dieselbe Tabelle mit demselben Ergebnis**.

**KEINE Rechenregel, KEIN Filter, KEIN Nenner, KEINE Aggregationsstufe und KEIN Marker
ist berührt.** Der Prüfer ist **ausschliesslich lesend** und rechnet keine Kennzahl; die
Invarianten (A)–(E) stehen **wörtlich unverändert** und liefern zeichengleiche Ausgaben.
Kein Artefakt unter `data/campaign/k*` und kein Messeingang unter `data/soll/` bewegt
sich, kein Re-Run folgt. Belegt in `z1_p_bericht_freeze.md` §4 (Negativprobe zu (F)) und
§5 (Ausgabe des Prüfers vor und nach der Erweiterung).

Rev. 48: **NEUER THREAT T15 — DIE AUSFÜHRUNGSGEOMETRIE DES INFERENZSERVERS IST EIN
UMGEBUNGSPARAMETER, DER DIE AUSGABE BEWEGT (N07, 01.09.2026).** Gemeint sind `n_ctx`
(`-c`), die daraus abgeleitete Batchgrösse (`-b`/`-ub`) und die KV-Cache-Geometrie.
**Belegt, nicht vermutet** (`z1_s_bericht_diagnoselauf.md` §6–§8, Archiv
`data/z1_s_diagnose/`): zwei Läufe auf derselben Maschine, derselben Ollama-Fassung
0.30.10, demselben Modell-Blob und mit **token-für-token demselben Erstprompt** haben bei
`temperature=0` und `seed=0` **verschieden geantwortet** — 1 517 gegen 2 261 Zeichen —, der
eine gültig, der andere mit 14 Fehlern ungültig; verändert war allein `-c 4096` gegen
`-c 16384` samt der abgeleiteten `-b`/`-ub` 512 gegen 1024 und 224 gegen 896 MiB KV-Cache.

**Die Abgrenzung gehört zum Eintrag und steht mit ihm im Text: die Vergleichbarkeit
innerhalb dieser Kampagne ist UNBERÜHRT.** Alle K2-Läufe liefen auf demselben **gemessenen**
Fenster `CONTEXT 4096` (§1 Nachtrag Rev. 26), das Nachlaufskript prüfte es **je Call**, und
die Prompts lagen mit Median **1 346** und Maximum **1 948** Token weit darunter. **Kein
Messergebnis ist betroffen, keine Metrik, keine Zelle der Erwartungsmatrix.** Was nach
dieser Messung **nicht** mehr behauptet werden kann, ist **Reproduzierbarkeit auf einer
anders konfigurierten Serverinstanz**. Die Entscheidung aus **Rev. 26**, `num_ctx`
**nicht** zu setzen, war **richtig und bleibt unangetastet** — ein Eingriff hätte den
eingefrorenen Messpfad bewegt.

**Dieses Amendment BESCHREIBT, es legt nichts fest** — zulässig nach §0.1 Punkt 2 auch nach
Messbeginn. **Keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein
Prompt, kein Schema** ist berührt; die drei Instrumentenhashes stehen zeichengleich auf den
Werten von Rev. 47. **Kein Re-Run.**

> **Zweck:** Dieses Protokoll legt Datensatz, Injektionsplan, Matching-Regeln, Metriken und
> Entscheidungsregeln fest, *bevor* die erste Messung läuft — gleiche Disziplin wie die
> Vorab-Entscheidungsregeln in Befund 03/05. Änderungen nach Messbeginn nur als dokumentiertes
> Amendment (§10), nie stillschweigend. Das Protokoll ergänzt §5 des Umsetzungsplans und macht
> ihn ausführbar. Änderungen vor dem Freeze werden in der Revisionshistorie (§10) geführt.

---

## 0. Offene Punkte vor dem Freeze (Entscheidung Timo)

~~Das Protokoll darf erst als eingefroren gelten, wenn diese vier Punkte entschieden sind~~
~~(Stand 12.08.2026: **1, 3 und 4 erledigt**, offen ist allein Punkt 2):~~
**Stand 27.08.2026 (Rev. 33, C5b): alle vier Punkte sind entschieden.** Mit Punkt 2 unten fällt
der letzte; das Protokoll ist **eingefroren** (Kopf, Messstand in §0.1).

1. ~~**Injektionszahl**~~ — **entschieden (Decision Record P, 12.08.2026):** Die
   Injektionsverteilung steht mit **32 Injektionen** nach der Verteilung in §3 fest, dazu
   **4 Zwillingsmodule** im Clean-Control-Set. Zur Aussagekraft bei 3–4 Injektionen je
   Szenario siehe den Vermerk in §5 und Threat T4.
2. ~~**Validitäts-Gate 0.9** (§7) bestätigen. Technisch prüfbar erst nach CLI-Inkrement 4~~
   ~~(Exit-Code 3 bei `valid_final=false`).~~ — **entschieden (27.08.2026, C5b, Rev. 33): das
   Gate 0.9 aus §7 ist BESTÄTIGT, unverändert.** Vier Gründe, in dieser Reihenfolge:

   **(a) Die technische Vorbedingung ist erfüllt.** Läufe mit `valid_final=false` sind über
   **Exit-Code 3** bzw. über das **persistierte Run-Log** identifizierbar (CLI-Inkremente 2
   und 4; der eingefrorene Messstand enthält Increment 7, §0.1). Die stille Zählung invalider
   Läufe als „0 Findings" — der Grund, aus dem der Punkt überhaupt offen war — ist damit
   **ausgeschlossen**, und zwar durch ein Feld im Artefakt, nicht durch Aufmerksamkeit beim
   Auswerten.

   **(b) Beobachtungsstand aus den Kontrollläufen, mit Fundstelle.** Ausgezählt am
   27.08.2026 über die `llm_call`-Records der archivierten Laufprotokolle:

   | Kontrollbestand | Invocations | `llm_call` | `valid_final=true` | Anteil | Retries |
   |---|---|---|---|---|---|
   | K2 (`data/c3b-k2/runs/*.jsonl`) | 52 | 156 | 156 | **1.0** | 0 |
   | K3 (`data/c3b-k3/runs/*.jsonl`) | 52 | 156 | 156 | **1.0** | 0 |

   `valid_raw` ist in beiden Beständen ebenfalls 156/156, `outcome` durchweg `measured`,
   `attempts_used` durchweg 1 — es gibt also **keinen** Fall, in dem erst ein Repair-Versuch
   die Gültigkeit hergestellt hat. Deckungsgleich mit den `run_footer`-Feldern
   (`calls_invalid: 0`, `invalid_reasons: []`) und mit den Nachlaufprüfungen in
   `c3b_k2_bericht_kontrolllauf.md` und `c3b_k3_bericht_kontrolllauf.md`. **Der Abstand zum
   Gate ist damit maximal** — die Frage, ob 0.9 zu hoch greift, stellt sich auf dem
   Beobachtungsstand nicht.

   **(c) Die Richtung der Regel ist konservativ.** Unterschreitet eine Konfiguration das Gate,
   folgt daraus **Dokumentation als Befund** und **Auswertung mit den vorhandenen validen
   Läufen** — **ausdrücklich OHNE Nachbesserung**: kein Prompt-Tuning (Eine-Iteration-Regel,
   §7), kein selektives Nachmessen (§1), keine Anpassung des Gates. Die Regel kann ein
   Ergebnis also nur **verschlechtern oder unangetastet lassen**, nie verbessern; sie ist
   keine Ausstiegsklausel, sondern eine Berichtspflicht.

   **(d) Der Zeitpunkt ist der Punkt.** Die Bestätigung erfolgt **VOR dem ersten
   Kampagnenlauf**; die ausgezählten Anteile stammen ausschliesslich aus den Kontrollläufen
   auf der **sauberen Baseline** (C3b), nicht aus Injektionsläufen. Eine Bestätigung **nach**
   Sichtung der Kampagnen-`valid_final`-Werte wäre **nicht mehr vorregistriert**, sondern
   an den Daten gewählt — genau der Fehler, gegen den §7 und die Vorregistrierung insgesamt
   gerichtet sind. Der Punkt wird deshalb hier geschlossen und nicht später.
3. ~~**FP-Messreihe auf sauberem Code:** entscheiden, ob während der Messläufe zusätzlich
   nicht-injizierte Dateien geprüft werden.~~ — **kein Entscheidungspunkt mehr, sondern Pflicht
   (12.08.2026):** Nach Decision Record O, Konsequenz 2 ist `localized` **ohne
   Falsch-Positiv-Rate nicht interpretierbar** — eine Lokalisationsmetrik ist durch Übermelden
   manipulierbar. Das Clean-Control-Set ist damit **Voraussetzung der Auswertung**, nicht
   Option; die Zwillingsmodule gehören hinein. Ausführung in **B5** (Increment 7) und **B8**.
   Der ursprüngliche Grund gilt unverändert fort: ohne die Reihe entsteht Precision nur aus den
   Injektions-Commits, was die FP-Rate des per-File-LLM-Checkers systematisch unterschätzen kann.
4. ~~**Fußnote ¹ (§3):**~~ **import-linter-Zyklenfähigkeit** praktisch verifizieren — betrifft
   heute die Matrixzeilen `CYCLE_SIBLING` und `CYCLE_PARENT_CHILD` in §3; der Verweis auf
   „Fußnote ¹" ist seit Rev. 6 **tot**, weil Fußnote ¹ dort inzwischen die zu `LAYER_SKIP_CALL`
   ist (korrigiert 12.08.2026) — **erledigt
   (11.08.2026, B9/B9+):** `acyclic_siblings` erkennt Geschwisterzyklen und steigt bis
   Standardtiefe 10 in Unterpakete ab, erfasst aber **keine Eltern/Kind-Zyklen**; die Ausgabe
   nennt eine **minimale Menge zu entfernender Kanten**, keine Zyklenpfade
   (`b9plus_bericht_baseline_ausdrucksmaechtigkeit.md`, Frage 5). Die Matrix in §3 ist
   entsprechend gestellt (`CYCLE_SIBLING` K4 = ja, `CYCLE_PARENT_CHILD` K4 = nein), die
   Matchregel für die K4-Ausgabeform steht in §4 (Rev. 7).

---

## 0.1 Messstand (eingefroren)

> **Gesetzt am 27.08.2026 mit Rev. 33 (C5b), vor dem ersten Kampagnenlauf.** Jeder Wert
> unten ist am 27.08.2026 aus der Datei bzw. dem Repositorium **gelesen** — `sha256sum`,
> `git rev-parse`, `git tag -l` —, keiner aus einem Bericht übernommen. Der Abschnitt ist
> die Antwort auf die Frage „wogegen ist gemessen worden?", ohne dass ein Leser dafür einen
> zweiten Bericht öffnen muss.

| Gegenstand | Wert |
|---|---|
| **Protokoll** | `docs/protokolle/eval_protokoll_phase04.md`, **Rev. 33** · SHA256 der Datei nach dieser Änderung: **wird im Freeze-Bericht `c5b_bericht_protokoll_freeze.md` geführt** — ein Selbstbezug im gehashten Dokument ist unmöglich (der Hash änderte sich beim Eintragen) |
| **Auswertungsspezifikation** | `docs/protokolle/c6_auswertungsspezifikation.md` = ~~`2f1354bbabdfaef8c858a6726521e224c30d6293513d83ea98cd1ef3f6608f97`~~ → ~~`8f6d358073d7f580fd8741bec2611fa2638c6f80f55ca9d10bb03ada82c37749`~~ → ~~`f9b949e0b398f32b4780d74273d465d1a8fca4ea681c1d3a344741505ae25a30`~~ → ~~`50f593d07801dd421aad1e644016bf4861af382afbc41749546e1ecad8785017`~~ → ~~`be3491e272c3672a7f05fd9c37152d30dfe2ad80c11aa085028edd3acb21d6e1`~~ → ~~`fe991be6ade440fe973b20cdf149ebdb9acd9291fbe6bb990e8e35f1092c20d1`~~ → **`39822edc0d9c109d7f1c1cfc285af9dd1363ec48b1a96a69334c173cd2cd71c7`** (§1 Nachtrag Rev. 30 / Hash-Nachzüge Rev. 31, C6b-2b 27.08.2026, C6c Rev. 37 28.08.2026, C6c-a Rev. 39 28.08.2026 und C11b Rev. 40 28.08.2026; Alttext gestrichen sichtbar, die Fassung selbst ist nur **ergänzt** — §10.4 erledigt, §6.2 korrigiert, §1.4 um die Terminalbreite erweitert, §1.8 neu — die Laufmanifeste als Eingang von T7 —, §7.4 um die lebenden Dokumente und §8 um Punkt 9 (Blindheit) ergänzt; **Rev. 40**: §7.5 (3) um die Aggregationsstufe von kein-EN präzisiert, §7.5 (5) — Läufespalte — und §7.5 (6) — Ablehnung der Ursachenaufspaltung — neu. **Keine Metrikdefinition berührt:** `strict`, `localized`, Precision, Recall, F1, Median, Spannweite und FP-Rate stehen unverändert; Rev. 40 legt fest, auf welcher Stufe die beiden Seiten EINES vorregistrierten Vergleichs gebildet werden. **Rev. 44** (C14 28.08.2026): §1.9 neu — die Artefaktauswahl je Paar (Konfiguration, Injektion) steht auf `postrun.verdict` des gehashten Laufmanifests, dazu die Zusicherung R12; §8 Punkt 10 neu — die Overlap-Tabelle **T10**, gebildet aus den bereits gerechneten Trefferzellen; §8 Punkt 1 um den Verweis auf den nachgezogenen T5-Vermerk ergänzt. **Wieder keine Metrikdefinition berührt** — bewegt hat sich, WELCHE DATEI dieselbe Metrik liest, und dass eine bereits gerechnete Zelle ein zweites Mal, schnittweise, ausgewiesen wird) |
| **Messeingänge `data/soll/`** | `architecture-rules.yaml` = `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` |
| | `depot_soll.ilograph.yaml` = `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` |
| | `importlinter.ini` = `0c9a1e0e0430ff01e8383407ec6212c58ddcbec6e529db7b044a30132b528751` |
| | `test_architecture.py` = `7504e30ce993803f4f3dab3023ed60742fcbd2382b9deb481d1860a67186a289` |
| | `control_files.txt` = `7356e6d332e5165acdfdcfac1a66bd9803a7fa36cb4b3e7d5480bcb3526fee62` |
| | `injection_manifest.md` = `63425d5501c8f5c13459e78782e370981db8e4aa68072aae46137550b98629e1` |
| | `injection_manifest.json` = `2744116e513c9e79e3174e6e3681abdcdc7c18f36d00b6d334875e4e918cfb1f` |
| | **sieben von sieben**, `sha256sum -c data/soll/SHA256SUMS` am 27.08.2026 OK |
| **Checker** | `phase04-freeze` = `348ca9daa456af4954f11f7152fc45201035297e` (annotiertes Tag, Tag-Objekt `19e7a7a5332c577dea194717f4bbe64cebcfdac4`) · **Messpfad `~/ma/tritongraph-measure`** (Worktree auf `phase04-freeze`, detached `348ca9d`) |
| **Checker-Artefakt** | `packages/triton-conformance/dist/cli.js` = `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` |
| **Runner** | ~~`tools/run_campaign.py`, `tools/campaign_spec.py`, `tools/postrun_check.py` auf Commit `70a2dd87905284cb36a4a5ba1e42e851c6fa9e95` (`70a2dd8`, „feat: measure the K2 context window and print validator expectations")~~ · ~~**nachgezogen am 27.08.2026 durch C5c (Amendment Rev. 34)**, weil die Archivwurzel `tools/run_campaign.py` berührt: jetzt Commit **`b6f9972067f6c7b4288c14bb52723f5c8a4a7a82`** (`b6f9972`, „fix: archive campaign artifacts under data/ instead of scratch") — der letzte Commit, der eine dieser drei Dateien berührt. **Einzige Differenz zu `70a2dd8` ist die Vorgabe von `--out`**; `tools/campaign_spec.py` und `tools/postrun_check.py` sind unverändert~~ — **erneut nachgezogen am 27.08.2026 durch C10a (Amendment Rev. 35)**, weil der commit-scharfe Validator-Punkt (6) `tools/run_campaign.py` berührt: jetzt Commit **`4caf083d5e21f36440579af6888513ca897f1dd4`** (`4caf083`, „fix: expect the injected importer at soll validator point (6)") — weiterhin der letzte Commit, der eine dieser drei Dateien berührt. **Einzige Differenz zu `b6f9972` ist die Auswertung von Validator-Punkt (6)**; `tools/campaign_spec.py` und `tools/postrun_check.py` sind unverändert |
| **Testrepo** | `baseline` = `0d651041ed87dd03f2f78359713633fac01c0a66` · **32 Injektionstags** `inj/01`–`inj/32` (gezählt: 32) · Bundle `data/testrepo/ma-conformance-testrepo-injections.bundle` = `1b9f8b58f271332e2d66ead83a3858271a04f3aebce95b7927977d9fa1be508b` (Baseline-Bundle `ma-conformance-testrepo-baseline.bundle` = `597fa466c5ff4e05ab5c1f3550fb88e0407c3968fae8fafd420166324d4a7b18`), beide `sha256sum -c` OK |
| **Archivwurzel** | ~~`/home/haasentimo/scratch/c7/out`~~ — **überholt am 27.08.2026 durch C5c (Amendment Rev. 34), vor dem ersten Kampagnenlauf** · jetzt **`~/ma/masterarbeit/data/campaign/`** (= `data/campaign/` im Thesis-Repo, neben `data/c3b-k2/`) — Vorgabe des CLI-Parameters `--out` in `tools/run_campaign.py` (`CAMPAIGN_OUT`), **nicht hart verdrahtet**; darunter unverändert `k1/`, `k2/`, `k3/`, `k4/`, `k5/` und `manifests/`. Begründung: **Scratchpad ist flüchtig; die Rohlogarchivierung nach §6 Punkt 4 verlangt einen versionierten Pfad** — der C4c-Verlustfall (`c4c_bericht_vorabpruefung.md` Teil C: die sechzehn Laufdateien der Vorabprüfung liegen „im flüchtigen Arbeitsverzeichnis dieses Auftrags" und sind nicht abgelegt) zeigt die Folge. **Ablageänderung — KEINE Messgrösse, KEIN Messeingang, KEINE Metrik**; `--plan` danach Exit 0 mit 160/192/480, gegen die C5-Ausgabe zeichengleich bis auf das Pfadpräfix |
| **Auswertungsinstrumente** | **Nachgetragen am 28.08.2026 durch C6c (Amendment Rev. 38), VOR dem ersten Auswertungslauf über `data/campaign/k*`.** Die drei Werkzeuge, die die Zahlen des Kapitels 7 **erzeugen** — sie sind kein Messeingang, aber sie stehen zwischen Messeingang und Ergebnis, und eine stille Änderung an einer Rechenregel oder einem Marker verschöbe **jede** Tabelle, ohne einen einzigen Eingang zu verschieben |
| | `tools/evaluate_campaign.py` = ~~`1cdaadbcebd99791b28a74a7fb3ffecd651cb9d61b9bf13a16b519b8cb672f94`~~ → ~~`5125cd595913b1226b888e67035f24f2831e0f4818b28dad4b261a57a0528eed`~~ → ~~`20bcdae0ebaec12930cad9ef91731f0b1e7e593b68c768be85e7d811ea23d306`~~ → ~~`eb206a6fcad515f653dd25394682e0d05e4f72902b3fb0beebe9d19c0b520653`~~ → **`b66be750f9b7cf524b9afa8edbab0138d17c409de4637465eb82d0f079a93428`** · **neu gebildet am 28.08.2026 (C14, Rev. 45)**, Artefaktauswahl **R11** auf das Laufverdikt, Zusicherung **R12** gegen das Lesen ungültiger Artefakte, Overlap-Tabelle **T10** (**R13**) und der Textnachzug am T5-Vermerk (**R14**); der Commit-SHA steht in `c14_bericht_vierter_lauf.md` §3 · **neu gebildet am 28.08.2026 (C11c, Rev. 43)**, Darstellungsreparatur D1–D3 (Markerauszeichnung, Exponentialschreibweise) und neue Zusicherung R10; der Commit-SHA steht in `c11c_bericht_dritter_lauf.md` §3 · **neu gebildet am 28.08.2026 (C11b, Rev. 41)**, Defektbehebung R1–R9 nach `c11a_bericht_diagnose.md` §7; der Commit-SHA steht in `c11b_bericht_zweiter_lauf.md` §2 · **neu gebildet am 28.08.2026 (C6c-a, Rev. 39)**, weil T7 auf die gehashten Laufmanifeste gestellt und die Blindheitsprüfung auf eine positive Erlaubnisliste umgestellt wurde; der Commit-SHA steht in `c6ca_bericht_t7_quellen.md` §6 · ~~zuletzt berührt in Commit `1fe3141`~~ (überholt am 28.08.2026 durch C6c-a) |
| | `tools/match_k4k5.py` = ~~`ad3edcb1ee8537ee758d8212055371957c0493f3d8e218267d182fb9fc060022`~~ → **`c16e7c4380034163f3034916193bd96cfc6bb957768fe610cb7018d7799f4ca6`** · **neu gebildet am 28.08.2026 (C11b, Rev. 41)**: das `localized`-Vokabular ist **benannt** (`LOC_TREFFER`, `LOC_STELLE`, `LOC_KEIN`, `LOC_NB`, die Menge `LOCALIZED_HIT`) und jeder Fund trägt eine **benannte Sonderklasse** (`special_class`), damit der Join nicht mehr auf Zeichenketten vergleicht (C11a §1.3). **Keine Zellenregel, keine Vergleichsvorschrift und keine Klassifikation ist inhaltlich verschoben** — der Selbsttest reproduziert alle **34 von 34** Fixtures unverändert · ~~zuletzt berührt in Commit `61b3bd1`~~ (überholt am 28.08.2026 durch C11b) |
| | `tools/check_doc_invariants.py` = ~~`d1c75ae57fb4865670a3bd01e42e3794dcdb3cc47f7030c837c3c0b88a738b18`~~ → ~~`6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018`~~ → **`c351a137e3f32e00b67e8f73d7cce0777f607c872fda4a7719c1b142b8707fdf`** · **neu gebildet am 31.08.2026 (Z1-P, Rev. 47)**, weil der Prüfer die **Invariante (F)** aufgenommen hat — SHA256 des Z1-Protokolls `docs/protokolle/z1_protokoll_extraktionsvergleich.md` gegen den in `z1_p_bericht_freeze.md` §3 als aktuell geführten Wert, in derselben Tabellenform, die (A) für dieses Protokoll liest; die §3-Leseroutine ist parametrisiert und wird von (A) und (F) geteilt. **Keine der Invarianten (A)–(E) ist inhaltlich berührt**, der Prüfer bleibt ausschliesslich lesend und rechnet keine Kennzahl; der Commit-SHA steht in `z1_p_bericht_freeze.md` §5 · **neu gebildet am 28.08.2026 (C6c-a, Rev. 39)**, weil die sieben lebenden Dokumente aus einer gemeldeten Beobachtung eine **entschiedene Ausnahme** geworden sind — ein Selbstbezug ist hier so unmöglich wie beim Protokoll-SHA eine Zeile weiter oben; der Commit-SHA steht in `c6ca_bericht_t7_quellen.md` §6, der vorige in `c6c_bericht_selbsttest_freeze.md` §7 |
| | **Maschinell geprüft** durch `tools/check_doc_invariants.py` Invariante **(E)**: die drei Dateihashes gegen die drei Werte dieser Tabelle |
| **T7-Quelle** | **Nachgetragen am 28.08.2026 durch C6c-a (Amendment Rev. 39), VOR dem ersten Auswertungslauf.** T7.1–T7.4 werden aus den **Laufmanifesten** `data/campaign/manifests/<cfg>[_<modus>]_<repo-sha>[_r<n>].json` gerechnet — ein Manifest je Invocation, **jedes von einem Block-`SHA256SUMS` bezeugt** (`data/campaign/k1..k5/SHA256SUMS`, zusammen 189 Manifeste). Sie tragen **Verdikte, Zähler und Provenienz, keine Funde** |
| | **Gegenprobe, nicht Quelle:** `data/campaign/journal.jsonl`, `data/campaign/MANIFEST.md` und die Blockmanifeste — sie sind **ungehasht und bleiben es planmäßig** (Regel für lebende Dokumente, §0.1 Punkt 7). Eine Abweichung zwischen Quelle und Gegenprobe ist ein **Befund**, der berichtet und **nicht** durch Angleichen aufgelöst wird |

> **Amendment 27.08.2026 (C5c, Rev. 34) — zwei Zeilen dieser Tabelle sind nachgezogen,
> vor dem ersten Kampagnenlauf.** Betroffen sind **Archivwurzel** (Ablage der Rohlogs von
> Scratchpad nach `data/campaign/`) und **Runner** (Commit, weil die Archivwurzel
> `tools/run_campaign.py` berührt). **Kein anderer Wert dieser Tabelle bewegt sich** —
> Protokollrevision, Auswertungsspezifikation, die sieben Messeingänge, Checker-Tag,
> Build-Hash, Testrepo-Baseline und beide Bundles stehen zeichengleich. Die Änderung ist
> eine **Ablageänderung**, keine Messgrösse, kein Messeingang, keine Metrik. Der SHA256 des
> Protokolls ändert sich damit; der neue Wert steht in `c5b_bericht_protokoll_freeze.md` §3
> neben dem gestrichenen alten.

> **Amendment 27.08.2026 (C10a, Rev. 35) — EINE Zeile dieser Tabelle ist nachgezogen,
> NACH dem ersten Kampagnenlauf.** Betroffen ist allein **Runner** (Commit, weil der
> commit-scharfe Validator-Punkt (6) `tools/run_campaign.py` berührt): `b6f9972` → `4caf083`.
> **Kein anderer Wert dieser Tabelle bewegt sich** — Protokollrevision, Auswertungsspezifikation,
> die sieben Messeingänge, Checker-Tag, Build-Hash, Testrepo-Baseline, beide Bundles und die
> Archivwurzel stehen zeichengleich. Berührt ist eine **Vorbedingung des Runners**, **keine**
> Metrikdefinition, **kein** Injektionsmanifest, **keine** Regeldatei, **kein** Prompt, **kein**
> Schema — die fünf Gegenstände der Sperre aus §0.1 Punkt 2 sind unangetastet. Der SHA256 des
> Protokolls ändert sich damit; der neue Wert steht in `c5b_bericht_protokoll_freeze.md` §3
> neben den gestrichenen alten. **Zeitpunkt ungeschminkt:** sechs K2-Invocationen liefen vor
> diesem Amendment und sind **verworfen**, nicht ausgewertet, nicht committet
> (`c10a_bericht_validator_punkt6.md`).

**Werkzeugstände** (§1 Amendment 11.08., Nachtrag Rev. 31 T13): import-linter 2.13
(grimp 3.15), PyTestArch 4.0.1 (networkx 3.6.1, pytest 9.0.1), Python 3.12.3, Node
**v22.23.2** — die Node-Differenz zu C3a (`v22.22.2`) ist als folgenlos benannt, weil der
Gatterbeleg der Build-Hash `dist/cli.js` ist und der zeichengleich stimmt.

### Regel für die Zeit nach dem Freeze

1. **Ab Rev. 33 sind Änderungen am Protokoll nur noch als datierte Amendments mit
   Begründung zulässig**, geführt in **beiden** Stellen — Revisionshistorie im Kopf **und**
   Amendments-Tabelle (§10) —, nie nur an einer.
2. **Ab dem ersten Kampagnenlauf ändert KEIN Amendment mehr** eine **Metrikdefinition**, das
   **Injektionsmanifest**, die **Regeldatei**, den **Prompt** oder das **Schema**. Amendments
   ab diesem Zeitpunkt dürfen **nur beschreiben, nicht festlegen**: sie halten fest, was
   beobachtet wurde und wie es zu lesen ist, und verschieben nicht, wogegen gemessen wird.
3. Die bestehende Ausnahme bleibt, wie sie in §1 steht und **nicht weiter**: wird während der
   Messung ein Defekt gefunden, wird der Lauf zu Ende geführt, der Defekt dokumentiert, und
   es ist **höchstens ein** Amendment mit **vollständigem Re-Run aller Konfigurationen**
   zulässig — kein selektives Nachmessen.
4. Der Grund für die Schärfe von (2): eine nach Sichtung der Ergebnisse geänderte Metrik oder
   ein nachgezogener Manifestwert ist von einer **an den Daten gewählten** Festlegung
   nachträglich nicht mehr zu unterscheiden. Was vorher gilt, ist vorregistriert; was nachher
   käme, wäre es nicht — unabhängig von der Absicht, in der es geschieht.
5. **JEDE Änderung am Protokoll ist eine Revision — auch ein reiner Hash-Nachzug, auch eine
   Änderung, die inhaltlich nichts verschiebt.** Ergänzt am 27.08.2026 durch **C6b-0a
   (Rev. 36)**, nachdem der Hash-Nachzug aus C6b-2b in `0c1cc34` ohne Kopf-Revision, ohne
   Historieneintrag und ohne §10-Zeile vollzogen worden war und der Bytestand des Protokolls
   dadurch **in keinem Dokument bezeugt** war. Zwei Gründe, beide unabhängig tragend:
   **(a)** eine Ausnahme für „inhaltsneutrale" Bytewechsel verlangte ein **Urteil darüber,
   welche Änderung substanziell ist** — und genau dieses Urteil nimmt der Freeze aus dem
   Verkehr; **(b)** der Protokoll-SHA ist der **Anker der Bewegungsprüfung** und als Detektor
   nur brauchbar, wenn **kein** Bytewechsel unregistriert bleibt — ein einziger geduldeter
   Wechsel macht jede spätere Abweichung mehrdeutig. Maschinell geprüft durch
   `tools/check_doc_invariants.py` (Invarianten (a) und (b)), der als Vorbedingung jedes
   schreibenden Auftrags läuft.

6. **Ab dem ersten Auswertungslauf über `data/campaign/k*` ist jede Änderung an den drei
   in §0.1 registrierten AUSWERTUNGSINSTRUMENTEN eine datierte Revision mit Begründung**
   — `tools/evaluate_campaign.py`, `tools/match_k4k5.py`, `tools/check_doc_invariants.py`.
   Ergänzt am 28.08.2026 durch **C6c (Rev. 38)**, vor dem ersten Auswertungslauf.
   **Keine solche Änderung darf eine Rechenregel oder einen Marker verschieben**;
   zulässig ist allein die **Behebung eines Defekts**, und zwar mit **vollständiger
   Neuauswertung** und **Ausweis beider Ergebnisse** — des Standes vor und des Standes
   nach der Behebung, nebeneinander, nicht ersetzend. **Warum die Instrumente überhaupt
   in den Messstand gehören:** Messeingang und Ergebnis sind gehasht und bezeugt, der Weg
   dazwischen war es nicht — eine stille Änderung an `false_positive_rates()` oder an
   `NB_CELLS` verschöbe **jede** Tabelle des Kapitels 7, ohne dass ein einziger
   registrierter Wert sich bewegte, und die Bewegungsprüfung über die Eingangshashes
   bliebe dabei grün. Maschinell geprüft durch `tools/check_doc_invariants.py`
   (Invariante **(E)**). **Der Prüfer registriert sich selbst mit** — sonst wäre der
   Prüfer die eine Datei, deren Änderung er nicht meldet.

7. **LEBENDE DOKUMENTE bleiben ungehasht — entschieden am 28.08.2026 durch C6c-a
   (Rev. 39), vor dem ersten Auswertungslauf.** Sieben Dateien in den gehashten Beständen
   stehen in **keinem** `SHA256SUMS` und werden **nicht** aufgenommen:

   | Datei | Art |
   |---|---|
   | `data/soll/MANIFEST.md` | Herleitungsdoku der sieben Messeingänge, selbst kein Messeingang |
   | `data/campaign/MANIFEST.md` | Kampagnenmanifest, fortzuschreiben |
   | `data/campaign/README.md` | Ablagebeschreibung |
   | `data/campaign/journal.jsonl` | append-only, wächst je Invocation |
   | `data/campaign/control/journal.jsonl` | append-only, Journal des Kontrollbestands |
   | `data/campaign/k2/MANIFEST.md` | Blockmanifest, fortzuschreiben |
   | `data/campaign/k3/MANIFEST.md` | Blockmanifest, fortzuschreiben |

   **Begründung.** `journal.jsonl` ist **append-only und wächst planmäßig**; die
   `MANIFEST.md` sind **fortzuschreibende Dokumente**. Ein Hash wäre für sie das **falsche
   Instrument** — er risse bei **jeder legitimen** Fortschreibung und erzöge dazu, ihn
   routinemässig nachzuziehen; ein Detektor, dessen Anschlagen zur Routine wird, ist
   keiner mehr (dieselbe Logik, aus der Rev. 36 den Protokoll-SHA als Anker gesetzt hat,
   hier in die andere Richtung angewandt). **Integrität liefert für sie die
   Commit-Historie**; der **Schnappschuss-Hash im Manifest** bleibt, wo er steht.

   **Was diese Ausnahme NICHT deckt.** **Keine** der sieben ist ein **Laufartefakt**, und
   seit Rev. 39 Punkt (1) ist **keine** mehr **Quelle** eines T-Wertes — T7 steht auf den
   gehashten Laufmanifesten, die drei mit T7-Zahlen (`data/campaign/MANIFEST.md`,
   `data/campaign/k3/MANIFEST.md`, `journal.jsonl`) sind **Gegenprobe**. Ein Laufartefakt
   oder eine Datei, die einen T-Wert **trägt**, gehört **nicht** auf diese Liste.

   **Die Liste ist abschliessend und steht namentlich im Code** (`KNOWN_UNLISTED` in
   `tools/check_doc_invariants.py`). Der Prüfer meldet die sieben bei **jedem** Lauf als
   **bekannte, entschiedene Ausnahme** mit Verweis auf diese Festlegung — **nicht als
   Fehlschlag**. Was **weder** gelistet **noch** auf dieser Liste ist, ist ein
   **FEHLSCHLAG**: das ist die Sperrklinke, an der eine **achte** ungelistete Datei
   auffällt. Ein Eintrag, dessen Datei inzwischen gelistet oder fort ist, wird als
   `HINWEIS` gemeldet, damit die Liste nicht schleichend veraltet.

---

## 1. Gegenstand & Konfigurationen

Geprüft wird der Konformitäts-Checker (`packages/triton-conformance`) gegen ein manuell
fixiertes Soll-Modell (Ilograph) auf einem gelabelten Datensatz, im Vergleich zu Python-nativen
statischen Baselines.

**Konfigurationsmatrix:**

| # | Konfiguration | Pfad | Läufe |
|---|---|---|---|
| K1 | triton-conformance, deterministische Rule-Engine | strukturell | 1 (deterministisch) |
| K2 | triton-conformance, LLM-Checker, `qwen2.5-coder:7b` (Ollama) | strukturell + semantisch | 3 |
| ~~K3~~ | ~~triton-conformance, LLM-Checker, nemotron-120B (OpenRouter)~~ | ~~strukturell + semantisch~~ | ~~3~~ |
| K3 | triton-conformance, LLM-Checker, `nvidia-nemotron-3-super-120b` — **DigitalOcean-Direktzugang**, `https://inference.do-ai.run/v1`, **kein** `CONFORMANCE_PROVIDER_PIN` | strukturell + semantisch | 3 |
| K4 | import-linter (YAML-Contracts) | strukturell | 1 |
| K5 | PyTestArch / pytest-archon | strukturell | 1 |

> **Zeile K3 nachgezogen (27.08.2026, Rev. 33, C5b).** Der Nachtrag Rev. 30 unten erklärt die
> OpenRouter-Zeile für überholt und sagt, sie „bleibt gestrichen stehen" — **gestrichen war sie
> nicht**: Rev. 30 hat den Nachtrag geschrieben, die Tabellenzeile aber unangetastet gelassen,
> und §6 Rev. 32 hat denselben Widerspruch für die **Aufrufzeilen** aufgelöst, nicht für die
> Matrix. Die Tabelle trug damit bis hierher den überholten Zugangsweg **ungekennzeichnet**.
> Jetzt steht die alte Zeile **gestrichen** und die verbindliche Direktzugangszeile daneben.
> **Keine Festlegung geändert** — verbindlich war der Direktzugang seit Rev. 30 (§1 Nachtrag
> Rev. 30), gemessen ist der Kontrolllauf bereits über ihn gefahren
> (`c3b_k3_bericht_kontrolllauf.md` §2); korrigiert ist allein der **Aufschrieb**, wie schon
> bei der K5-Aufrufzeile in Rev. 32.

Provider-Logging nach dem Contract aus Entscheidung H (`checker_entscheidungen.md`):
`model_requested` und `model_version` getrennt, Tokens in/out, Latenz, Attempt-Index,
Run-Index, Seed, Temperature. Für K2/K3 gilt `temperature=0` + fixer Seed; Varianz wird
gemessen, nicht angenommen (Befund 03.1).

**Prompt- & Regel-Freeze:** Eingefroren werden der Checker-Prompt **und** die Regeldatei
`architecture-rules.yaml` gemeinsam (je Commit-Hash im Manifest) — bei semantischen Regeln ist
das `statement` Bestandteil des effektiven Prompts, der Freeze muss deshalb beide Hashes
umfassen. Ab der ersten Messung: keine Änderung an Prompt oder Regeln.
Wird während der Messung ein Defekt gefunden → Lauf zu Ende führen, Defekt dokumentieren,
höchstens **ein** Amendment mit vollständigem Re-Run *aller* Konfigurationen (kein selektives
Nachmessen). Die Suppressions-Klausel aus Extraktions-Prompt v3 („do not invent unbacked ones")
darf im Checker-Prompt **nicht** enthalten sein (Befund 04, Konsequenz 4) — das wird vor dem
Freeze explizit geprüft und im Manifest bestätigt.

> **Amendment (11.08.2026) — Begründung: B9+.** Die **Versionen der Baseline-Werkzeuge**
> gehören zum eingefrorenen Messstand und werden im `run_header` bzw. im Messmanifest
> festgehalten: import-linter 2.13 (grimp 3.15), PyTestArch 4.0.1 (networkx 3.6.1,
> pytest 9.0.1), Python 3.12.3. Begründung: die gemessene Ausdrucksmächtigkeit beider
> Werkzeuge ist versionsabhängig, und die Aussagen der Arbeit über K4 und K5 sind ohne
> Versionsangabe nicht reproduzierbar. Zusätzlich zur Ablaufregel: `--no-cache` bei jedem
> import-linter-Lauf.

> **Amendment (12.08.2026) — Begründung: B38, Analogie zum Regel-Freeze, B9+.** Der Freeze
> umfasst neben dem Prompt und `architecture-rules.yaml` auch die **K4-Contract-Datei** und die
> **K5-Testdatei**, je mit **eigenem SHA256 im Messmanifest**, neben den oben festgehaltenen
> Werkzeugversionen.
>
> **Begründung:** Für K4 und K5 **ist die Konfigurationsdatei die vollständige Regelmenge** —
> dasselbe Argument wie für das `statement` semantischer Regeln, nur stärker: dort ist die
> Regeldatei ein Teil des effektiven Prompts, hier ist sie das gesamte Prüfverfahren. Zusammen
> mit den vier Formulierungsfallen aus B38, die eine Regel **still grün** durchlaufen lassen,
> ruhten die K4/K5-Ergebnisse sonst **an der entscheidenden Stelle auf Commit-Disziplin statt
> auf der Vorregistrierung** — dieselbe Lückenklasse, die B27 für das gesendete Schema und die
> nicht gerenderten Prompt-Zweige beschreibt (siehe Freeze-Definition in
> `00_stand_und_entscheidungen.md` §6).
>
> **Ab der ersten Messung gilt die Änderungssperre dieses Abschnitts auch für diese beiden
> Dateien.** Ein Defekt in einer Baseline-Konfiguration fällt damit unter dieselbe Regel wie ein
> Prompt-Defekt: Lauf zu Ende führen, dokumentieren, höchstens **ein** Amendment mit
> vollständigem Re-Run aller Konfigurationen.

> **Amendment (13.08.2026) — Begründung: `c2a_bericht_contract_semantik.md`.** Die
> **Konfigurationen von K4 und K5** werden hier auf **Contract-Typ- und
> Einstellungsebene** vorregistriert. Das erweitert die Typvorregistrierung in §3
> (Rev. 10) um die **Schalter**, ohne die ein Contract das Szenario nicht oder falsch
> prüft. Container- und Modulnamen folgen aus dem Komponentenschnitt
> (`planung/c1_komponentenschnitt.md` §6) und stehen in den Dateien aus C2.
>
> | Szenario | Contract-Typ | Zwingende Einstellung | Beleg |
> |---|---|---|---|
> | `LAYER_BACK_CALL` | `layers`, `containers` = die **drei Kontextpakete**, `layers = api / services / repository / models` | **`exhaustive` ist auf diesem Contract NICHT gesetzt** — siehe Absatz unten | c2a §2.2c (Begleitmeldung), Schnitt §6.1 |
> | `LAYER_SKIP_CALL` | `forbidden`, ~~je Kontext `api` → `repository`~~ — **korrigiert im Nachtrag unten (Rev. 13): je Kontext ZWEI Contracts, mechanisch aus der Schichtliste abgeleitet, insgesamt sechs** | **`allow_indirect_imports = True`** | c2a §1.1c |
> | `PROTECTED_MODULE` | **`protected`** mit `protected_modules` / `allowed_importers`, **nicht** `forbidden` | — (`protected` ist direkt-only) | c2a §1.1c |
> | `INDEPENDENCE` | `independence` über die beiden Kontextpakete | **keine Einstellung möglich**; die Bedingung liegt im Schnitt (Bauvorschrift **I1**, §3) | c2a §3 |
> | `CYCLE_SIBLING` | **ein** `acyclic_siblings`-Contract mit `ancestors` = **Wurzelpaket** | `ancestor` je Contract im **Messmanifest** festhalten | c2a §2.2c |
> | `INCORRECT_LOCATION` | `layers` mit **`exhaustive = True`**, `containers` = das **Zielpaket** | Layerliste aus dem **Dateibaum** (bereits §3 Am. (g)) | B9+ Nachtrag §3 |
>
> **`allow_indirect_imports = True` auf den `LAYER_SKIP_CALL`-Contracts.** `forbidden`
> wertet in der Vorgabe **transitiv** (c2a §1.1c), und `api → services → repository` ist
> die legitime Kette des Spine; ohne den Schalter bricht der Contract auf der **sauberen**
> Baseline, und C3 fällt aus einem **Konfigurationsfehler** durch, der wie ein
> **Repo-Fehler** aussieht.
>
> **`protected` statt `forbidden` für `PROTECTED_MODULE`.** `protected` ist
> **direkt-only**; ein naives `forbidden` meldet die indirekte Kette
> `services → storage → internal` und macht ein Paket mit privatem Innenleben
> **unkonfigurierbar** (c2a §1.1c). Der Typ existiert in import-linter 2.13
> (`importlinter/contracts/protected.py`).
>
> **`exhaustive` ist auf dem Spine-`layers`-Contract NICHT gesetzt** — im
> Komponentenschnitt nur als Prüflistenpunkt geführt, hier ausdrücklich vorregistriert.
> Grund: `mappers` steht nicht in der Layer-Liste und wäre unter `exhaustive` ein **nicht
> deklariertes Kind**; der Contract bräche auf der **sauberen** Baseline. Das ist eine
> **ungemessene Annahme** und als solche gekennzeichnet; sie steht als Punkt **(h)** in der
> B38-Prüfliste und ist mit Positiv- **und** Negativfall zu belegen.
>
> **`CYCLE_SIBLING`.** Ein einziger `acyclic_siblings`-Contract mit `ancestors` auf dem
> Wurzelpaket genügt: der Contract steigt bis `depth` (Vorgabe 10) ab und deckt die
> Kontextebene mit (c2a §2.2c). Der `ancestor` je Contract ist im Messmanifest
> festzuhalten, sonst ist die Zuordnung **Befund → Ebene** nicht rekonstruierbar.
>
> **K5: `root_path` und `module` beide auf das WURZELPAKET-Verzeichnis**, nicht auf den
> Source-Root. Begründung: PyTestArch leitet die Knotennamen aus `root_path` ab
> (c2a §5.2) — nur so lauten sie wie die Modulnamen des Checkers, der den Source-Root
> abschneidet, und nur so fallen sie mit den `match_key` des Manifests zusammen. **Ohne
> diese Wahl ist K5 nicht joinbar.**

> **Nachtrag (13.08.2026, Rev. 13) zum Amendment oben — Begründung: Deckungsgleichheit
> mit Fußnote ¹ in §3.** Die Zeile zu `LAYER_SKIP_CALL` in der Tabelle oben ist
> **korrigiert**: „je Kontext ein Contract `api` → `repository`" war mit Fußnote ¹ in §3
> („für n Schichten sind n−2 Zusatz-Contracts nötig") **nicht deckungsgleich** — und die
> Fußnote hat recht. Der alte Wortlaut bleibt durchgestrichen stehen.
>
> **Ableitungsregel, vorregistriert.** Die `forbidden`-Contracts für Schichtsprünge werden
> **MECHANISCH aus der Schichtliste** abgeleitet, **nicht aus dem Injektionsplan**: je
> Container ein Contract für **jede Quellschicht, die nicht-benachbarte Schichten unterhalb
> hat**, mit **allen diesen Schichten** in `forbidden_modules`. Bei vier Schichten
> (`api` > `services` > `repository` > `models`) sind das **zwei Contracts je Kontext** —
>
> | Container | `source_modules` | `forbidden_modules` |
> |---|---|---|
> | `depot.<k>` | `depot.<k>.api` | `depot.<k>.repository`, `depot.<k>.models` |
> | `depot.<k>` | `depot.<k>.services` | `depot.<k>.models` |
>
> — bei drei Kontexten also **SECHS**, nicht drei. Das entspricht der Zahl **n−2** aus
> Fußnote ¹ in §3 (n = Zahl der Schichten).
>
> **`allow_indirect_imports = True` gilt für alle sechs.** Ohne den Schalter brechen sie auf
> der **sauberen** Baseline an den legitimen Ketten `api → services → repository → models`
> und `api → mappers → models` (c2a §1.1c).
>
> **Begründung, die über die Arithmetik hinausgeht.** Eine Konfiguration, die nur die
> **injizierte** Grenze kennt, misst das Werkzeug **gegen den Testfall statt gegen die
> Zielarchitektur**. Auf den **Recall** wirkt das nicht — injiziert wird nur
> `api → repository` —, wohl aber auf die **Vergleichbarkeit mit K1**, das aus der Whitelist
> **jede** nicht gelistete Kante ableitet, und auf die **Falsch-Positiv-Reihe**, weil mehr
> Contracts mehr Gelegenheiten zum Feuern auf der sauberen Baseline bedeuten. **Die
> vollständigere Konfiguration ist der härtere Test für K4.**
>
> **PRINZIP, für alle K4- und K5-Regeln gültig, hier einmal festgehalten.** Die
> Baseline-Konfigurationen drücken die **eingefrorene Zielarchitektur** so vollständig aus,
> wie das **Vokabular des jeweiligen Werkzeugs** es zulässt, und werden **aus der Whitelist
> bzw. der Schichtliste abgeleitet — nicht aus dem Injektionsplan**. Wo das Vokabular nicht
> reicht, wird die Lücke als **Nicht-Abdeckung dokumentiert**, nicht durch eine engere
> Konfiguration **verdeckt**.
>
> **NICHT-ABDECKUNG, ausdrücklich benannt.** Eine **vollständige Spiegelung der Whitelist
> ist nicht schreibbar.** Bei **19 Komponenten** und einer Whitelist, in der **nur gelistete
> Kanten erlaubt** sind, ist die Menge der verbotenen Paare **dreistellig**; import-linter
> formuliert Architektur über eine **kleine Zahl von Contract-Typen**, nicht über eine
> **Erlaubnisliste**. Nicht in K4 ausgedrückt sind insbesondere die Paare, an denen
> **`mappers`** beteiligt ist (außer dem Zyklus-Contract), und die
> **kontextübergreifenden** Paare jenseits von `independence`. Das ist ein **UF3-Befund zur
> Ausdrucksmächtigkeit** — die Erlaubnisliste ist in der **negativen Richtung stärker** als
> eine Contract-Liste — und als solcher in **§8 (UF3)** geführt, nicht nur hier vermerkt.

> **Nachtrag (13.08.2026, Rev. 14) — Begründung: `c2b_bericht_erlaubnislisten.md`.** Zwei
> Festlegungen zur Baseline-Konfiguration. **Beide sind nicht wählbar**: sie folgen aus dem
> in Rev. 13 vorregistrierten **PRINZIP** (Konfiguration aus der Whitelist bzw. der
> Schichtliste, nicht aus dem Injektionsplan) zusammen mit gemessenem Werkzeugverhalten.
>
> ### (A) K5 wird als ERLAUBNISLISTE gebaut, nicht als Sammlung von Einzelverboten
>
> **Je Komponente eine Regel** über die Whitelist-Nachbarn dieser Komponente:
>
> ```
> should_not().import_modules_except_modules_that().are_named([<Whitelist-Nachbarn>])
> ```
>
> auf einem Architekturobjekt mit **`exclude_external_libraries = True`**. Bei 19 Komponenten
> sind das **19 Regeln**. Die **Framework-Regeln** (`FRAMEWORK_TYPE_IN_SIGNATURE` als
> Import-Proxy) laufen über ein **ZWEITES Architekturobjekt in derselben Testdatei** unter
> **`exclude_external_libraries = False`**.
>
> **Warum nicht `should_only()`.** `should_only` ist **keine Erlaubnisliste, sondern eine
> Mengengleichheit**: gemessen verlangt die positive Hälfte, dass **jedes** gelistete Ziel auch
> tatsächlich importiert wird — ein Modul, das nur eine **Teilmenge** seiner erlaubten Nachbarn
> benutzt, bricht die Regel auf der **sauberen** Baseline (c2b §1c-Zusatz: `"…routes" does not
> import "…order_models".`, obwohl nichts Verbotenes importiert wird). Aus der Whitelist
> abgeleitet — wie das PRINZIP es verlangt — wäre `should_only` damit **dieselbe Falle** wie
> `exhaustive` auf dem Spine-`layers`-Contract, nur auf der K5-Seite: **C3 fiele aus einem
> Konfigurationsfehler durch, der wie ein Repo-Fehler aussieht.** Die gewählte Form hat
> **keine positive Hälfte**; gemessen hält sie bei Teilmenge **und** bei leerem Importsatz und
> bricht bei jedem nicht gelisteten Import (c2b §1, Vier-Lagen-Tabelle).
>
> **Warum die verbietende Hälfte trägt.** Sie wertet **je Import** und zählt **vollständig**
> auf: zwei nicht gelistete Importe → zwei Zeilen, drei → drei, alphabetisch nach Zielmodul,
> ohne Abschneidung (c2b §1c). Und sie wertet **je Modul** des Subjektpakets, mit **Nennung des
> schuldigen Moduls** (`"…pricing.engine" imports "depot.core.ports".`, c2b §1d) — ein sauberes
> Geschwistermodul verhindert den Befund nicht. Für §4 folgt daraus: eine gebrochene
> K5-Erlaubnislistenregel liefert **n Befunde auf Modulebene** und ist auf **Kantenebene**
> joinbar. `are_sub_modules_of` ist damit für **Verbote** ein tragfähiges Subjekt; für
> **Gebote** bleibt es bei der Aggregatsemantik, weshalb `MISSING_PORT_REFERENCE` weiter **vier
> Einzelregeln** auf Untermodulebene braucht (Rezeptpräzisierung (f), unverändert).
>
> **Warum zwei Architekturobjekte.** Unter `exclude_external_libraries = True` erscheint
> **kein** Fremdknoten im Graphen (c2b §2a: 33 Knoten, keiner außerhalb von `depot`; eine Regel
> auf `typing` endet in `NetworkXError`). Unter `False` erscheinen sie mit **voller Pfadtiefe**
> — aber dann bricht die Erlaubnislistenregel schon an **`typing` allein** (c2b §2b,
> Kernfrage). Eine Erlaubnisliste, die jeden Standardbibliotheks-Import mit aufführen müsste,
> wäre eine Liste **aus dem Repo** statt **aus der Zielarchitektur** und verstieße gegen das
> PRINZIP. Die beiden Anforderungen sind unter **einer** Einstellung nicht gleichzeitig
> erfüllbar, unter **zwei Objekten in einer Datei** schon: gemessen `4 passed in 0.11s`,
> Exit 0, die Objekte sind unabhängig (c2b §2c). **Die Zuordnung Regel → Architekturobjekt ist
> Bestandteil des Freeze** und im Messmanifest festzuhalten — die K5-Testdatei trägt nach dem
> Amendment vom 12.08. einen eigenen SHA256, aber der Hash allein macht nicht rekonstruierbar,
> gegen welches Objekt eine Regel lief. Beide Objekte lesen die Platte zum Zeitpunkt ihres
> Aufrufs und sind **vor dem ersten Test** zu bauen.
>
> **Keine vorregistrierte Matrixzelle verschiebt sich.** Die K5-Spalte steht bei allen vier
> `FORBIDDEN_RELATION`-Szenarien bereits auf **„ja"** (§3, gemessen B9+ F1–F3). Die
> Erlaubnisliste ändert die **Ausdrucksform**, mit der dieses „ja" erreicht wird, nicht die
> Vorhersage. Auch `FRAMEWORK_TYPE_IN_SIGNATURE`/K5 = **FP⁴** und `INCORRECT_LOCATION`/K5 =
> **nein⁶** bleiben unberührt: die erste hängt am zweiten Architekturobjekt, die zweite an
> Bauvorschrift (e).
>
> ### (B) `include_external_packages = True` als erforderliche K4-Einstellung
>
> Der Schalter steht im **Kopf** der Contract-Datei und gilt für **alle** Contracts. Er ist
> **erforderlich**, weil die vorregistrierte Zelle `FRAMEWORK_TYPE_IN_SIGNATURE`/K4 = **FP⁴**
> voraussetzt, dass **beide** Werkzeuge den Framework-Import sehen; ohne ihn bricht die
> Konfiguration bei einem externen `forbidden_module` sogar ab, ohne einen einzigen Contract
> auszuwerten (c2b §3a: *„The top level configuration must have include_external_packages=True
> when there are external forbidden modules."*). Drei gemessene Randbedingungen gehören dazu:
>
> - **Externe Importe erscheinen als Kante, aber auf die PAKETWURZEL zusammengefasst.** Aus
>   `import sqlalchemy.ext.asyncio` wird die Kante `… -> sqlalchemy (l.3)`; ein **Unterpaket**
>   als Contract-Ziel wird **abgelehnt** (c2b §3d: *„subpackages of external packages are not
>   valid"*, Konfigurationsabbruch). Die K4-Framework-Regel kann also nur `sqlalchemy` sagen.
> - **Externe Knoten sind `squashed` und haben keine ausgehenden Kanten** (c2b §3c, direkt an
>   grimp 3.15 gemessen). Sie können deshalb **keine indirekte Kette** zwischen zwei
>   Projektmodulen schließen — genau das, worauf `forbidden` (transitiv) und `independence`
>   (transitiv, ohne Abschalter) empfindlich sind. `depot.orders -> sqlalchemy` und
>   `depot.billing -> sqlalchemy` zeigen **auf** denselben Knoten; ein Pfad entsteht daraus
>   nicht. **Bauvorschrift I1 bleibt davon unberührt** — sie betrifft geteilte
>   **Projekt**pakete.
> - **Keiner der sechs Skip-Contracts und auch `independence` bricht unter dem Schalter auf der
>   sauberen Menge** (c2b §3c: `7 kept, 0 broken`, Exit 0, mit **und** ohne Schalter bei
>   identischen Kanten; beide Regelarten mit Positivkontrolle scharf gestellt — injizierter
>   Schichtsprung → genau **ein** Contract `BROKEN`). Der Schalter ändert nur die **Zähler**:
>   `38 files, 24 dependencies` gegen `36 files, 18 dependencies`. **Folge:** `Analyzed N
>   files` ist **nur zusammen mit der Schaltereinstellung** interpretierbar und ist keine
>   Dateizahl des Repos.

> **Nachtrag (14.08.2026, Rev. 17) — FRAMEWORK-PIN: `sqlalchemy` 2.0.52 gehört in den
> eingefrorenen Messstand.** Begründung: `c2b_bericht_erlaubnislisten.md` §0/§2b/§3d;
> `4b4_bericht_baseline_billing.md` §7 und §8.
>
> Neben den Werkzeugversionen des Amendments vom 11.08. (import-linter 2.13 / grimp 3.15,
> PyTestArch 4.0.1 / networkx 3.6.1 / pytest 9.0.1, Python 3.12.3) wird **`sqlalchemy` in der
> Version 2.0.52** im `run_header` bzw. im Messmanifest festgehalten. **Drei Gründe, alle
> tragend:**
>
> - **(a) Die vorregistrierte Zelle `FORBIDDEN_SIGNATURE_TYPE`/K4 = FP⁴ hängt daran.** Es ist
>   die Umgebung, in der K4 unter `include_external_packages = True` und K5 unter
>   `exclude_external_libraries = False` den **externen** Import auflösen müssen. Beide
>   Auflösungen sind an dieser Version gemessen — die Zusammenfassung externer Ziele auf die
>   **Paketwurzel** und die Ablehnung von Unterpaketen als Contract-Ziel (c2b §3d) ebenso wie
>   die Sichtbarkeit im zweiten Architekturobjekt (c2b §2b).
> - **(b) c2b hat unter genau dieser Version gemessen** und führt sie dort ausdrücklich als
>   „**Fixture-Requisite, nicht registriert**" (c2b §0, Versionstabelle). Diese Einordnung war
>   richtig, solange `sqlalchemy` nur Requisite eines Fixtures war; seit die Clean-Baseline
>   selbst acht `sqlalchemy`-führende Module trägt, ist es Bestandteil des **Messobjekts**.
> - **(c) Die `README.md` des Baseline-Commits behauptet den Pin bereits** — *„All modules
>   import cleanly under the framework version the specification pins"*
>   (`4b4_bericht_baseline_billing.md` §8). Der Baseline-Commit **ist `B` und wird nicht
>   geändert**; der Pin ist deshalb **hier** nachzuliefern, damit die Aussage der `README.md`
>   trägt statt auf eine Spezifikationsstelle zu zeigen, die es nicht gibt.
>
> **Ergänzend, gemessen:** der Smoke-Test unter 2.0.52 importiert **alle 73 Module fehlerfrei**
> (`73 importiert, 0 gebrochen`, `4b4_bericht_baseline_billing.md` §7) — bis dahin waren die
> acht `sqlalchemy`-führenden Module nur `compileall`-geprüft.
>
> **Ungemessen und als solches gekennzeichnet:** ob die Werkzeuge externe Importe auch bei
> **fehlendem** Paket auflösen. Gemessen ist nur der Fall „Paket installiert". Der Punkt geht
> als weiterer Eintrag in die **B38-Prüfliste**.

> **Nachtrag (23.08.2026, Rev. 21) — DREI FOLGEN AUS REV. 20.** Begründung:
> `c2b_bericht_k4_konfiguration.md` §B5 (k) und §B6, `c2c_bericht_k5_konfiguration.md`.
> Mit dem Wegfall der Zelle FP⁴ verlieren zwei Begründungen dieses Abschnitts ihren Grund;
> die **Festlegungen selbst bleiben**, ausgetauscht werden allein die Gründe. Dazu die
> Konsequenz für die Zahl der K5-Architekturobjekte. **Keine Matrixzelle bewegt sich durch
> diesen Nachtrag** — die betroffene Zelle ist mit Rev. 20 bereits bewegt.
>
> **(C1) `include_external_packages = True` BLEIBT — mit neuer Begründung.** Der alte Grund
> im Nachtrag Rev. 14 (B), „weil die vorregistrierte Zelle `FRAMEWORK_TYPE_IN_SIGNATURE`/K4 =
> **FP⁴** voraussetzt, dass **beide** Werkzeuge den Framework-Import sehen", **war** die
> FP⁴-Zelle und fällt mit Rev. 20. Der alte Wortlaut bleibt dort stehen.
>
> **Neu, und tragend:** die externen Importe bleiben unter dem Schalter im Graphen
> **sichtbar**. Dass K4 dennoch **nichts** meldet, ist damit eine **inspizierbare
> Nicht-Abdeckung** statt eines Artefakts der Unsichtbarkeit. Die Aussage „K4 erreicht die
> Signaturebene nicht" ist an einem Graphen geprüft, der die Kante `…models.customer_models
> -> sqlalchemy` **enthält**; ohne den Schalter wäre sie an einem Graphen geprüft, in dem die
> Kante gar nicht erst vorkommt, und die Nullzeile ruhte auf der Konfiguration statt auf dem
> Werkzeug. Das ist derselbe Unterschied wie zwischen „nicht gefunden" und „nicht gesucht".
>
> **Gemessen wirkungslos für alle dreizehn Contracts** (`c2b_bericht_k4_konfiguration.md`
> §B5 (k)): `13 kept, 0 broken`, Exit 0, mit **und** ohne Schalter — kein Contract nennt ein
> externes Ziel. Der Schalter verändert allein die Zähler der Kopfzeile `Analyzed N files`,
> die deshalb nur zusammen mit der Schaltereinstellung interpretierbar ist. **Folge für die
> Kosten der Festlegung: sie sind null.**
>
> **(C2) Der `sqlalchemy`-Pin (2.0.52) BLEIBT — auf einem Bein statt auf dreien.** Von den
> drei im Nachtrag Rev. 17 als „alle tragend" bezeichneten Gründen fallen **zwei** mit der
> Zelle weg:
>
> - **(a) entfällt** — er lautete „die vorregistrierte Zelle `FORBIDDEN_SIGNATURE_TYPE`/K4 =
>   FP⁴ hängt daran". Die Zelle steht seit Rev. 20 auf „nein"; nichts hängt mehr daran.
> - **(b) entfällt als tragender Grund** — „c2b hat unter genau dieser Version gemessen" ist
>   eine Provenienzangabe, kein Grund, die Version festzuschreiben. Sie bleibt als Angabe
>   richtig und ist im Messmanifest geführt.
> - **(c) TRÄGT WEITER** — die `README.md` des Baseline-Commits behauptet den Pin bereits
>   (*„All modules import cleanly under the framework version the specification pins"*,
>   `4b4_bericht_baseline_billing.md` §8). Der Baseline-Commit **ist `B` und wird nicht
>   geändert**; ohne den Pin zeigt die `README.md` auf eine Spezifikationsstelle, die es
>   nicht gibt.
> - **Dazu der Smoke-Test** (`4b4_bericht_baseline_billing.md` §7): unter 2.0.52 importieren
>   **alle 73 Module fehlerfrei** (`73 importiert, 0 gebrochen`). Das ist eine Aussage über
>   das **Messobjekt**, nicht über eine Matrixzelle, und überlebt Rev. 20 unberührt.
>
> **Der Pin bleibt.** Ein Grund genügt, wenn er trägt, und (c) trägt: er hält eine Aussage
> des eingefrorenen Messobjekts wahr. Ausdrücklich vermerkt, weil die **Zahl** der Gründe
> sich geändert hat und eine spätere Lesart sonst aus „drei tragende Gründe" auf eine
> Wichtigkeit schlösse, die der Pin nicht mehr hat.
>
> **Ergänzend gemessen (schließt B38 (l) auf BEIDEN Seiten):** die Werkzeuge lösen externe
> Importe **auch bei fehlendem Paket** auf. K4 mit deinstalliertem `sqlalchemy`:
> `13 kept, 0 broken`, Exit 0, und die FP-Sonde mit **identischer** Befundmenge
> (`c2b_bericht_k4_konfiguration.md` §B5 (l)). K5 unter `exclude_external_libraries = False`
> mit deinstalliertem `sqlalchemy`: die Knoten `sqlalchemy` und `sqlalchemy.orm` stehen
> unverändert im Graphen, die Sonde meldet **dieselben acht Module**
> (`c2c_bericht_k5_konfiguration.md` §C6). **Beide Werkzeuge lesen den Importgraphen aus dem
> Quelltext, nicht aus der Installation.** Der Prüfpunkt (l) ist damit geschlossen; der Pin
> ruht nicht auf ihm.
>
> **(C3) K5 VERWENDET EIN ARCHITEKTUROBJEKT.** Der Nachtrag Rev. 14 (A) sieht ein
> **zweites** Architekturobjekt unter `exclude_external_libraries = False` vor, allein für
> die Framework-Regeln. Mit Rev. 20 gibt es **keine** Framework-Regel: sie widerspräche
> R-FRAMEWORK-1, das den Import ausdrücklich erlaubt, und meldete auf der **sauberen**
> Baseline acht Module, während C3 null fordert. Das zweite Objekt trüge damit **keine
> Regel** — und ein ungenutztes Objekt in einer einzufrierenden Datei ist totes Gewicht, das
> beim Lesen der Datei eine Regelmenge suggeriert, die es nicht gibt.
>
> **Festgelegt:** die K5-Testdatei baut **genau ein** Architekturobjekt, mit
> `exclude_external_libraries = True`. **Alle 23 Regeln** (19 Erlaubnislisten + 4 Portregeln)
> laufen gegen dieses eine Objekt. Die in Rev. 14 verlangte **Zuordnung Regel →
> Architekturobjekt im Messmanifest** wird dadurch nicht gegenstandslos, sondern trivial und
> ist in `data/soll/MANIFEST.md` als solche festgehalten. Ausgeführt und clean gemessen in
> `c2c_bericht_k5_konfiguration.md` (`24 passed`, Exit 0).

---

> **Nachtrag (23.08.2026, Rev. 24) — BUILD-PROVENIENZ UND WERKZEUG-PINS.**
>
> `checker_git_head` bezeugt den Stand des Checker-Repositoriums, **nicht den ausgeführten
> Code**. Der Messpfad führt `packages/triton-conformance/dist/cli.js` aus; `dist/` ist
> gitignoriert. In C3a lag dort zunächst ein Build vom 11.08.2026 neben HEAD `348ca9d`
> (`c3a_bericht_clean_state_audit.md` §8 Punkt 5). Auch die vier Inhaltshashes schließen diese
> Lücke nicht: der laufende Code bildet sie zur Laufzeit, sodass ein veralteter Build bei
> unverändertem Prompt dieselben Werte liefert. Das ist ein realer Fall: B24 änderte die
> Kanonisierung in `ruleEngine.ts`, während alle vier Hashes byte-identisch blieben. Ein alter
> Build hätte daher `348ca9d` geloggt, nichtkanonisierte Kanten gewählt und die vier
> `CYCLE`-Schlüssel systematisch verfehlt.
>
> **Festlegung ohne weiteren Eingriff in den eingefrorenen Messpfad:** (a) Vor **jedem**
> Messlauf wird der Checker neu gebaut. (b) Der Kampagnen-Runner bildet SHA256 der anschließend
> ausgeführten `dist/cli.js` und schreibt diesen Wert zusammen mit dem Bauzeitpunkt und der
> vollständigen Ausgabe von `git status --porcelain` des Checker-Repos in das Laufmanifest.
> (c) Das Manifest führt `checker_dist_cli_sha256`, `checker_build_timestamp` und
> `checker_git_status_porcelain` neben `checker_git_head`. Die Außenlösung ist Absicht: ein
> weiterer Eingriff in den eingefrorenen Pfad bewegte `checker_git_head` zum vierten Mal, ohne
> zusätzliche Beweiskraft zu schaffen.
>
> **Pins nach Rolle, nicht wahllos:** Im **Messpfad** wird `networkx==3.6.1` gepinnt; es ist
> Laufzeitabhängigkeit von PyTestArch und genau die Version, unter der C2a und C2b gemessen
> haben (`c2a_bericht_contract_semantik.md` §0; `c2b_bericht_erlaubnislisten.md` §0). Als
> **Prüfwerkzeug, nicht als Messeingang**, wird `PyYAML==6.0.2` gepinnt; darauf beruht der
> Soll-Validator. Beide Werte sind in C3a tatsächlich erhoben (`c3a_bericht_clean_state_audit.md`
> §1), nicht geschätzt. Die übrigen Pins dieses Abschnitts bleiben unverändert.

> **Nachtrag (24.08.2026, Rev. 26) — KONTEXTFENSTER ALS GEMESSENER UMGEBUNGSPARAMETER.**
> Begründung: `k2_machbarkeitslauf_bericht.md` §6.
>
> Der Checker setzt beim Ollama-Aufruf **kein** `num_ctx`: der vollständige Request-Body in
> `llmClient.ts:114-124` (`JSON.stringify({model, messages, temperature, seed, ...(pin ?
> {provider: pin} : {}), response_format})`) enthält kein `options`- und kein `num_ctx`-Feld, und
> `OpenAiClientOptions` (`llmClient.ts:37-53`) kennt kein entsprechendes Feld. Ollama fällt damit
> auf sein Default-Kontextfenster zurück — **gemessen `CONTEXT 4096`** in beiden überwachten
> Läufen des Machbarkeitslaufs, obwohl das Modell laut `ollama show` **32768** Token trägt. Bei
> Überschreitung schneidet Ollama **vorn** ab, **ohne Fehler und ohne Logzeile**.
>
> **Festlegung, ohne Eingriff in den eingefrorenen Messpfad:** das Nachlaufskript prüft **je
> Call**, dass `tokens_in + tokens_out` unter dem tatsächlich geladenen Fenster bleibt; beide
> Werte liefert Ollama im `usage`-Feld der Antwort und stehen im Log. Ein Codeeingriff (`num_ctx`
> setzen) wäre der falsche Weg: er bewegte `checker_git_head` ein fünftes Mal (Nachtrag Rev. 24)
> und änderte die effektive Modellkonfiguration — das entwertete den Machbarkeitslauf als Aussage
> über die **eingefrorene** Konfiguration.
>
> **Belegdaten** (`k2_machbarkeitslauf_bericht.md` §6): größter gemessener Prompt **1394 Token**
> (`catalog_service.py`, 34 % des 4096-Token-Fensters), System-Prompt konstant **1292 Zeichen**.
> Der in c2a §7.1 genannte längste bekannte Prompt der Kampagne (4920 Zeichen) liegt über dem
> längsten hier gemessenen User-Prompt und wurde nicht direkt geprüft; der offene Punkt bleibt für
> die Gesamtkampagne **ungeschlossen**.

> **Nachtrag (24.08.2026, Rev. 26) — MESSUMGEBUNG K2 UND REPRODUZIERBARKEITSBEFUND.**
> Begründung: `k2_machbarkeitslauf_bericht.md` §1.
>
> Der Machbarkeitslauf K2 (24.08.2026) lief auf einer **anderen** Maschine als die Vorarbeiten bis
> C3a: AMD Ryzen 5 5600X (6C/12T), 15 GiB RAM unter WSL2, NVIDIA RTX 3070 Ti (8192 MiB VRAM),
> Ubuntu 24.04.1 LTS unter WSL2, Kernel `5.15.153.1-microsoft-standard-WSL2`, `node v22.23.2`,
> Python 3.12.3, Ollama-Server **und** -Client **0.32.15**, Modell `qwen2.5-coder:7b`, Digest
> `dae161e27b0e`, Architektur `qwen2`, 7.6B Parameter, Quantisierung `Q4_K_M`,
> Modell-Kontextlänge **32768**, Ausführung **100 % GPU** bei rund **5,9 GiB VRAM**.
>
> **Reproduzierbarkeitsbefund:** `dist/cli.js`, auf dieser Maschine gebaut, ergibt SHA256
> `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` — **identisch** mit den vier
> auf dem Notebook gebauten Fassungen, trotz anderem Betriebssystem und anderer Node-Version
> (`22.23.2` statt `22.22.2`). Der Build ist damit **plattform- und toolchain-unabhängig
> reproduzierbar**, mehr als Nachtrag Rev. 24 verlangt (dort: SHA256 neben `checker_git_head`,
> ohne Aussage über Maschinenunabhängigkeit).

> **Nachtrag (24.08.2026, Rev. 27) — KONTROLLLAUF K2 AUF VOLLER SKALA: MACHBARKEITSHYPOTHESE
> BESTÄTIGT.** Begründung: `c3b_k2_bericht_kontrolllauf.md` §2, §3.
>
> Der Machbarkeitslauf (Nachtrag oben) deckte fünf Dateien ab; der tatsächliche Kontrolllauf
> C3b-K2 lief über **alle 52** Kontrollmodule, in derselben Einzeldatei-Zerlegung und demselben
> 30-Sekunden-Pausenprofil. **Gemessen:** 52 von 52 Invocationen gültig, **0 Wiederholungen**,
> Gesamtdauer **33 min 2 s**, `calls_total` summiert auf **156 von 156** erwarteten Calls
> (`52 × 3`), `invalid_reasons: []` und `calls_transport_failed: 0` in allen 52 `run_footer`.
> Token-Budget je Call: Maximum **2356 von 4096** Token (57,5 %, Invocation 21,
> `core/ports.py`), keine Überschreitung. Temperaturprotokoll über Invocation 1, 26 und 52:
> **57–60 °C**, ohne Erwärmungstendenz über die 33 Minuten — weit unter der Schwelle, an der der
> Notebook-Lauf in C3b nach 53 Minuten Dauerlast thermisch abbrach.
>
> **Damit ist die im Machbarkeitslauf aufgestellte Hypothese auf voller Skala bestätigt, nicht
> nur hochgerechnet**, und die im Nachtrag oben offene Frage des Kontextfensters ist für K2
> **empirisch geschlossen**: keine der 156 tatsächlichen Anfragen näherte sich der
> 4096-Token-Grenze.

> **Nachtrag (24.08.2026, Rev. 27) — POOLBEFUND K3: GETEILTES KONTINGENT ALS AUSFALLURSACHE,
> NICHT DER BURST.** Begründung: `k3_machbarkeitslauf_bericht.md` §5, §15; B37.
>
> Unter einem gegenüber C3b um den Faktor 15 reduzierten und über fünf getrennte, durch
> 30-Sekunden-Pausen entkoppelte Invocationen verteilten Lastprofil (drei Calls je Invocation
> statt 156 in einer) brechen **drei von fünf** Invocationen mit `http_429` ab; **6 von 15**
> angeforderten Calls gehen verloren, bei unverändertem Provider-Pin `digitalocean` und
> `allow_fallbacks: false`. Die sofortige Gegenprobe nach dem dritten Abbruch trägt dieselbe
> Signatur wie in C3b: `limit_source: upstream_provider_shared_pool`, `is_byok: false` — das
> Kontingent liegt **beim Anbieter**, geteilt über dessen Nutzer, **nicht** an diesem Konto
> (9,94 von 10 USD frei) und **nicht** an der Aufrufrate dieses Laufs.
>
> **Festzuhalten:** ein höheres eigenes Guthaben ändert daran nichts. Zusammen mit B37
> (Kampagnendauer/Wiederaufnahme) und der Beschränkung auf **einen** schema-fähigen Provider
> (`c3b_bericht_kontrolllauf.md` §4.3) ist ein Poolengpass beim gepinnten Backend gleichbedeutend
> mit Laufausfall — unabhängig von der eigenen Aufrufdisziplin. Das ist der empirische Befund,
> der einen **Direktzugang beim Anbieter** als Vorbedingung für C3b-K3 begründet; **welcher**
> Zugang das ist, entscheidet sich erst nach einem verifizierten Testcall und ist hier **nicht**
> festgeschrieben.
>
> **Nebenbefund, positiv:** die Einzeldatei-Zerlegung, die K2 trägt (Nachtrag oben,
> `c3b_k2_bericht_kontrolllauf.md` §0), macht die Abbruchursache erstmals im `llm_call`-Record
> selbst sichtbar (`transport_failures[].kind: "http_429"`) — in C3b existierte für verlorene
> Calls kein Record, die Ursache war nur über eine externe Gegenprobe rekonstruierbar.
> `run_footer.failed_calls` trägt den Grund weiterhin nicht.
>
> **Nebenbefund, offen, nicht untersucht:** zwei `transport_failures`-Einträge tragen einen
> **negativen** `latency_ms`-Wert (`k3_machbarkeitslauf_bericht.md` §5). Der Checker wurde
> auftragsgemäß nicht angefasst; die Beobachtung ist als offener Punkt geführt
> (`offene_punkte.md` Abschnitt F), weil Latenzen in Kapitel 7 berichtet werden könnten.

> **Nachtrag (26.08.2026, Rev. 30) — K3-ZUGANGSWEG REGISTRIERT; KATALOGANGABEN GEMESSEN,
> NICHT ANGENOMMEN.** Begründung: `d2_bericht_vormessungen.md` M1–M4; Poolbefund im Nachtrag
> Rev. 27 oben; B32.
>
> Der Poolbefund der Rev. 27 begründet den **Direktzugang beim Anbieter**, ohne ihn zu
> benennen; hiermit ist er benannt. Die Zeile K3 der Konfigurationsmatrix oben —
> „nemotron-120B (OpenRouter)" — ist damit ~~OpenRouter~~ **überholt** und bleibt gestrichen
> stehen; verbindlich ist:
>
> - **Base-URL** `https://inference.do-ai.run/v1` (`CONFORMANCE_BASE_URL`)
> - **Modell** `nvidia-nemotron-3-super-120b` (`CONFORMANCE_MODEL`)
> - **kein `CONFORMANCE_PROVIDER_PIN`.** Ohne Router gibt es nichts zu pinnen (B32); das
>   Feld `provider_pin` im `run_header` bleibt `null`, und `provider_served` bleibt je Call
>   `null` — in C3b-K3 gemessen in **156 von 156** Calls. Das ist **Datenlage, kein Ausfall**
>   (`llmClient.ts:24-29`: `provider` wird nie zurückgefüllt).
>
> **Katalogangaben, wörtlich aus `GET /v1/models` am 26.08.2026 (HTTP 200, 72 Einträge):**
>
> ```json
> {"context_length": 1000000, "created": 1773783814,
>  "id": "nvidia-nemotron-3-super-120b", "max_output_tokens": 32768,
>  "object": "model", "owned_by": "digitalocean"}
> ```
>
> Die `id` ist **zeichengleich** mit dem angeforderten `CONFORMANCE_MODEL`; der Katalog kennt
> den Namen unter keiner abweichenden ID.
>
> **Das Kontextfenster wird als GEMESSENER Umgebungsparameter geführt** — parallel zur
> bestehenden Führung des Ollama-Fensters (Nachtrag Rev. 26: `CONTEXT 4096` statt der
> Modellgrenze 32768). Registriert: `context_length` **1 000 000**, `max_output_tokens`
> **32 768**. Gegenprobe an den 156 archivierten C3b-K3-Calls: Maximum
> `tokens_in + tokens_out` = **3136** (0,31 % des Fensters), grösstes `tokens_out_total`
> **1823** von 32 768. **Keine Annäherung an eine der beiden Grenzen.** Das Nachlaufskript
> prüft je Call weiterhin gegen das Fenster, ohne Eingriff in den Messpfad.
>
> **Was der Katalog NICHT ausweist, und was deshalb nicht behauptet wird.** Die Feldmenge des
> Katalogs ist über alle 72 Einträge erschöpfend `id`, `object`, `owned_by`, `created`,
> `context_length`, `max_output_tokens`. **Quantisierung, Präzision, Gewichts-Revision und
> Serving-Stack-Version: FEHLT** — kein Feld benennt sie. Sie werden **nicht** aus
> Modellkarten anderer Quellen ergänzt und **nicht** geschätzt. **Die Identität der Gewichte
> ist nicht verifiziert** (T14, §9).

> **Nachtrag (26.08.2026, Rev. 30) — AUSWERTUNGSEINGANG, GEHASHT.** Begründung: Analogie zu
> den gehashten Messeingängen in `data/soll/` (Amendment 12.08. oben);
> `d2_bericht_vormessungen.md` M6.
>
> Neben den Messeingängen wird der **Auswertungseingang** registriert:
>
> | Datei | SHA256 |
> |---|---|
> | `docs/protokolle/c6_auswertungsspezifikation.md` | ~~`dc1d17f822ca0dabca2699b717d92e1e3de55cd86222277f89e63be74d1d7785`~~ → ~~`2f1354bbabdfaef8c858a6726521e224c30d6293513d83ea98cd1ef3f6608f97`~~ → ~~`8f6d358073d7f580fd8741bec2611fa2638c6f80f55ca9d10bb03ada82c37749`~~ → ~~`f9b949e0b398f32b4780d74273d465d1a8fca4ea681c1d3a344741505ae25a30`~~ → ~~`50f593d07801dd421aad1e644016bf4861af382afbc41749546e1ecad8785017`~~ → ~~`be3491e272c3672a7f05fd9c37152d30dfe2ad80c11aa085028edd3acb21d6e1`~~ → ~~`fe991be6ade440fe973b20cdf149ebdb9acd9291fbe6bb990e8e35f1092c20d1`~~ → **`39822edc0d9c109d7f1c1cfc285af9dd1363ec48b1a96a69334c173cd2cd71c7`** |
>
> Sie legt fest, **wie** aus den Messartefakten Kennzahlen werden (Filter, `strict`,
> `localized`, FP-Rate, Aggregation, Pflichtbestandteile der Ausgabe). Damit fällt sie unter
> dieselbe Disziplin wie Prompt, Regeldatei, K4-Contract-Datei und K5-Testdatei: ab der ersten
> Messung keine stillschweigende Änderung, jede Änderung als Amendment (§10).
>
> ~~**Bekannter Stand-Unterschied, nicht stillschweigend aufgelöst:** §1.6 und §10.1 der~~
> ~~Spezifikation führen `expected_match_key.K2_K3` für I21–I24 noch als Platzhalter-String.~~
> ~~Dieser Punkt ist seit dem 26.08.2026 **erledigt** — die vier Schlüssel stehen im Manifest~~
> ~~(`d1_bericht_matchkey_eintrag.md`); die Spezifikation ist an dieser Stelle älter als das~~
> ~~Manifest. Der Hash oben bezeugt den Stand, **nicht** dessen Aktualität.~~

> **Hash-Nachzug (26.08.2026, Rev. 31) — Begründung: der Stand-Unterschied oben ist
> aufgelöst.** Der Absatz darüber steht **gestrichen**, weil sein Gegenstand entfallen ist. Die
> Spezifikation ist in **D3a** auf den D1-Stand gezogen worden: die vier `K2_K3`-Schlüssel für
> I21–I24 stehen jetzt **wörtlich aus `data/soll/injection_manifest.json`** in §1.6 (Alttext
> durchgestrichen stehen gelassen), §10.1 ist als **erledigt** gekennzeichnet, und die vier in
> **Rev. 31** neu registrierten Punkte sind als Anforderungen an C6b aufgenommen (§3.4 (1) und
> (2), §7.5 (3) und (4), Pflichtbestandteile in §8 Punkte 7 und 8).
>
> **Der Hash ändert sich damit notwendig.** Alter Wert gestrichen, neuer Wert daneben — beide
> bleiben sichtbar, damit die Registrierung des Rev.-30-Standes nachvollziehbar bleibt und die
> Änderung nicht als stille Ersetzung erscheint. **Der registrierte Auswertungseingang ist ab
> hier die neue Fassung**; die Disziplin bleibt unverändert: ab der ersten Messung keine
> stillschweigende Änderung, jede weitere als Amendment (§10). Der Nachzug erfolgt **im selben
> Commit** wie die Spezifikationsänderung, damit Spezifikation und registrierter Hash nie
> auseinanderfallen.

> **Hash-Nachzug (27.08.2026, C6b-2b) — die K4/K5-Matchregel ist spezifiziert.** Die
> Auswertungsspezifikation ist in **C6b-2/2a/2b** an drei Stellen ergänzt worden: §10.4
> (offener Punkt 4 / A-21) ist **erledigt** — die generische K4/K5-Matchregel steht in
> `tools/match_k4k5.py`, eine je besetzter Zelle von T8; §6.2 trägt eine **Korrektur** (der
> Parameter der Test-ID der vier Portregeln ist die `rule_id`, nicht der Modulname, belegt an
> `data/soll/test_architecture.py:309-310` — der Schluss der Passage bleibt richtig); §1.4
> nimmt die **Terminalbreite** als Umgebungsparameter der K4-Messung auf (`rich` fällt bei
> Ausgabe in eine Pipe auf 80 Spalten zurück, gemessen `console.width = 80`,
> `is_terminal = False`; der archivierte Rohtext ist dort umgebrochen).
>
> **Der Hash ändert sich damit notwendig:** ~~`2f1354bb…f6608f97`~~ → **`8f6d3580…82c37749`**.
> Alter Wert gestrichen, neuer daneben; die Kette der drei registrierten Stände bleibt
> sichtbar. Nachzug **im selben Commit** wie die Spezifikationsänderung, und dieselbe Zeile
> ist in **§0.1** (Messstand) mitgezogen, damit die beiden Stellen nicht auseinanderfallen.
>
> **Keine Metrikänderung, keine Manifeständerung, keine Zelle der Erwartungsmatrix bewegt
> sich, kein Messergebnis betroffen.** Der archivierte Rohtext bleibt unangetastet: es wird
> **nicht** neu erfasst, der Runner **nicht** geändert, und der Umbruch ist reversibel und
> spezifiziert.

## 2. Datensatz

**Test-Repository:** eigenständiges Repo, das die Modulstruktur von `nova-modulith`
verkleinert nachbildet (gleiche Top-Level-Pakete, reduzierte Modulzahl pro Paket).
Strikt getrennt von der Live-Codebase; kein Code aus `nova-backend` wird kopiert.
Zielgröße: klein genug, dass jeder Datei-Check ins 7B-Fenster passt (Befund 05 —
kein Paket über ~15k Tokens Fakten), groß genug für realistische Schichtung
(Richtwert: 5–6 Pakete, 30–50 Module).

**Kontaminationsfreiheit (Validitäts-Stärke, ergänzt 18.07.):** Das Testrepo wird neu
geschrieben und ist nie öffentlich verfügbar gewesen. Damit ist ausgeschlossen, dass die
Evaluationsmodelle den Code aus dem Pretraining kennen und Verletzungen aus Memorierung statt
Inferenz erkennen — ein Vorteil des synthetischen Designs gegenüber öffentlichen
Benchmark-Repos, der in der Arbeit als Gegenposition zu T1 argumentiert wird.

**Reihenfolge der Erstellung (verbindlich, wegen Zirkularitätsrisiko):**

1. Repo-Struktur bauen, sauberer Zustand.
2. **Soll-Modell manuell fixieren** (Ilograph) + Regeln formulieren (`architecture-rules.yaml`,
   Entscheidung G). Ab hier sind Soll und Regeln eingefroren (Commit-Hash).
3. **Clean-State-Audit:** alle fünf Konfigurationen auf dem sauberen Repo laufen lassen.
   Sollwert: 0 Findings. Restbefunde werden einzeln geprüft: echte Altlast → Repo fixen und
   Audit wiederholen; Tool-Eigenheit → in die **Known-Deviations-Liste** aufnehmen und aus
   allen späteren FP-Zählungen ausschließen. Erst nach bestandenem Audit wird injiziert.
4. Verletzungen injizieren (§3), jede als eigener Commit.

Die Reihenfolge Soll → Regeln → Injektionen mitigiert das Risiko, dass Regeln unbewusst auf
die geplanten Injektionen zugeschnitten werden (Threat T2, §9).

> **Amendment (12.08.2026) — Begründung: c1a.** Die Aussage, das Testrepo bilde die Struktur
> von `nova-modulith` verkleinert nach, ruht ab hier auf einer **Messung** statt auf einer
> Behauptung. Grundlage: `c1a_bericht_nova_modulith_struktur.md` (Commit `559491b`,
> Source-Root `nova-backend/src/app`, ein Skriptlauf, streng read only).
>
> **Gemessene Struktur des Vorbilds.** **6 Top-Level-Pakete** = fünf fachliche Kontexte plus
> ein **nicht geschichtetes Infrastrukturpaket `core`**. Die **Schichtung sitzt innerhalb der
> Kontexte** (`api`, `core`, `models`, `repository`, `services`) und ist in **3 von 5**
> Kontexten vollständig. Der Top-Level-Importgraph hat **15 Kanten**, davon laufen **190 von
> 220 Einheiten Kantengewicht auf `core`**; zwischen den vier Kontexten außer `iam` existiert
> **keine einzige Kante** (c1a §1, B2, B4). Das Testrepo bildet also einen **Stern mit
> kontextinterner Schichtung** nach, keine flach geschichteten Top-Level-Pakete.
>
> **Größenordnung des Vorbilds** (c1a A4, Commit `559491b`): **407** `.py`-Dateien, **349**
> ohne `__init__.py`, **299** ohne `__init__.py` und ohne `alembic`. Diese Zahlen ersetzen die
> Bezugsgröße aus Befund 05 (siehe dort Nachtrag 05.4).
>
> **Bewusste Auslassung.** Das Testrepo bildet **keine `alembic`-Migrationen** nach. Im Vorbild
> sind das **50 der 349** Nicht-Init-Module mit eigener Signaturform
> (`def upgrade() -> None`, c1a D2). Die Auslassung ist bewusst und spart Modulbudget; die
> Zielgröße von 30–50 Modulen bezieht sich damit auf Anwendungscode.

> **Amendment (12.08.2026) — Begründung: `c1b_bericht_komponentenschnitt.md` Punkte 6 und 7,
> Entscheidung dieser Session.**
> Ergänzt Schritt 2 der Erstellungsreihenfolge (Soll-Modell fixieren) um drei Vorschriften.
>
> **(1) Das Soll deckt den gesamten Messraum ab, nicht einen Zustand.** Neben allen Modulen der
> Clean-Baseline listet es die **vier Zielorte der `INCORRECT_LOCATION`-Injektionen**.
> Grund: `componentOf` ist ein **exakter Lookup** ohne Präfixlogik; ein Modul an einem nicht
> gelisteten Ort ist **unmapped**, erzeugt **keinen** LLM-Call und erschiene als False Negative,
> obwohl die Erwartungsmatrix für K2/K3 „ja" vorhersagt (`c1b_bericht_komponentenschnitt.md`
> Punkt 6, ausgeführt: `calls_total = 0`, `checks_performed` leer, keine Fehlermeldung). Bei **28 der 32**
> Injektionen ändert sich kein Modulname; nur `INCORRECT_LOCATION` erzeugt neue. Die vier
> zusätzlichen Einträge sind damit **Vollständigkeit über alle Messzustände**, nicht
> Antizipation einer Injektion.
> **Entlastend gegenüber T2 (Autor-Zirkularität):** die Modulliste des Soll geht **nicht in den
> Prompt** ein — `buildUserPrompt` emittiert ausschließlich `# Changed file`, `## Imports`,
> `## Signatures`, `## Allowed dependency edges touching this component` und `## Rules to check`
> (`b1_bericht_matchkey.md`, Abschnitt C3). Das Modell sieht die Phantomeinträge nie.
>
> **(2) Die Modulliste wird maschinell erzeugt.** Sie wird **aus dem Dateibaum der
> Clean-Baseline generiert**, nicht von Hand geschrieben, und um eine **explizite Phantomliste**
> der vier Zielorte ergänzt. Danach wird die Datei eingefroren und gehasht (`topology_sha256`,
> §1).
>
> **(3) Soll-Validator, je Injektionscommit statt nur auf B.** Abgleich der Soll-Modulliste
> gegen den Dateibaum. Die **erwartete Differenz ist commit-abhängig**: auf der Clean-Baseline
> `B` sind es die vier Zielorte; auf einem `INCORRECT_LOCATION`-Commit die drei übrigen Zielorte
> **plus die ursprüngliche Position** des dort verschobenen Moduls. Grund: ein im Soll
> deklariertes, aber nicht existierendes Modul erzeugt **keine Warnung, keine Report-Zeile, kein
> Log-Feld und keinen Exit-Code** (`c1b_bericht_komponentenschnitt.md` Punkt 7) — der
> Clean-State-Audit kann einen vergessenen
> oder falsch geschriebenen Eintrag also nicht bemerken. Der Validator gehört in **C3** und als
> **Vorbedingung in den Runner (C7)**.

> **Amendment (13.08.2026) — Begründung: `c1b_bericht_ruleengine_verifikation.md` §8.3, Punkt 7
> Abschnitt 7 und Punkt 4; Decision Record M.2.** Erweitert den Soll-Validator um zwei
> Prüfungen und präzisiert die maschinelle Erzeugung der Modulliste.
>
> **(4) Regel-Scopes gegen die Topologie prüfen — dritter stiller Ausfall.**
> `rules[].scope.components` muss **Teilmenge** von `topology.components` sein; eine Verletzung
> bricht den Lauf ab. Grund: `parseArchitectureRules` prüft **nur die Form** und sieht die
> Topologie nie (`rules.ts:60-63`), obwohl der Typkommentar die Prüfung ausdrücklich behauptet
> (`types.ts:18-21`, „must exist in the resolved topology"). Eine Regel mit Tippfehler im Scope
> wird **akzeptiert** und läuft danach **nie** — gemessen: `scope.components: ["persistenz"]`
> wird angenommen, und `buildPromptContext(...).rules` bleibt für einen realen Fakt der
> Komponente `persistence` leer. Sie fällt an **keiner** Stelle auf: sie erscheint in keiner
> `checks_performed`-Zeile, weil `checks_performed` aus `context.rules` gebildet wird
> (`llmChecker.ts:89`) — also aus genau der Menge, aus der sie herausgefiltert wurde. Für die
> Messung ist das der teuerste der drei stillen Ausfälle: eine Kategorie lieferte **vier
> garantierte False Negatives**, die in der Auswertung dem Modell zugeschrieben würden statt
> der Konfiguration.
>
> **(5) Gegenrichtung als Warnung, nicht als Abbruch.** Jede Komponente aus
> `topology.components`, die von **keiner** Regel gescopt ist, wird gemeldet. Sie ist nicht
> zwingend ein Fehler — nicht jede Komponente trägt eine Regel —, aber sie ist der Zustand, in
> dem eine geplante Regel fehlt, ohne dass irgendetwas es anzeigt.
>
> **Beide Seiten liegen bereits beisammen.** `loadSoll` (`run.ts:262-266`) gibt
> `resolveTopology(...)` und `parseArchitectureRules(...)` im **selben `return`-Ausdruck**
> zurück; die Prüfung ist eine Mengenoperation über zwei vorhandene Werte und braucht keine
> neue Datenquelle. Sie gehört wie (3) in **C3** und als **Vorbedingung in den Runner (C7)**.
>
> **(6) `__init__.py` bildet auf den Paketnamen ab, nicht auf `…​.__init__`.** Die maschinelle
> Erzeugung der Modulliste (2) muss `pkg/audit/__init__.py` als **`pkg.audit`** eintragen.
> `relativeFilePathToModulePath` schneidet das ganze Segment ab und prüft den
> `/__init__.py`-Zweig **vor** dem allgemeinen `.py`-Zweig (`pythonCodeModel.ts:70-80`);
> gemessen in allen drei Layout-Varianten (flach, `src/`-Fallback, expliziter `sourceRoot`).
> Init-Dateien erscheinen als **eigener `ChangedFact`** und werden von keiner der beiden
> Dateilisten gefiltert (`gitDiff.ts:30`, `cliExtractor.ts:128`). Für
> `CYCLE_PARENT_CHILD` ist das Elternmodul **genau diese Datei** — der Injektionsträger ist
> also eine `__init__.py`, und ihr Soll-Eintrag lautet auf den Paketnamen. Da `componentOf` ein
> exakter Lookup ohne Präfixlogik ist, deckt der Eintrag des Elternpakets das Kindmodul
> **nicht** ab: beide brauchen je einen eigenen Eintrag, in **verschiedenen** Komponenten,
> sonst greift `from === to` (`ruleEngine.ts:47`) und es entsteht überhaupt kein Record.

> **Amendment (13.08.2026) — Begründung: `c2a_bericht_contract_semantik.md` §5.1;
> `planung/c1_komponentenschnitt.md` §3 und §7.** Vier Punkte: ein vierter Ausfallmodus,
> der korrigierte Richtwert, drei Fidelitätsverzichte und eine Korrektur am Amendment vom
> 13.08. oben.
>
> **(7) Vierter Ausfallmodus — und ausdrücklich NICHT still.** Nennt eine **K5-Regel** ein
> Modul, das nicht im Graphen ist, wirft PyTestArch `NetworkXError` — in pytest ein
> **ERROR**, kein **FAILURE** (c2a §5.1: `NetworkXError: The node depot.core.portz is not
> in the digraph.`). Der Lauf bricht ab und liefert für diese Regel **keinen Befund**.
> **Abgrenzung zu den drei stillen Ausfällen** aus dem Amendment oben: dieser ist **laut,
> aber ergebnislos** — er ist im Lauf sichtbar, produziert aber keine Messung. Die
> zugehörige Bauvorschrift **K5-1** steht in §3.
>
> **(8) Der Richtwert „5–6 Pakete, 30–50 Module" ist überholt.** Er stammt aus der Zeit
> **vor** der Rasterentscheidung „ein Paket = eine Komponente" mit Kontext × Schicht. Neu:
> **19 Pakete**, **rund 70 Dateien**, davon **rund 50 inhaltstragend**
> (`c1_komponentenschnitt.md` §7). **Die Tokenrechnung aus Befund 05 wird NICHT neu
> gerechnet** — sie galt für die verworfene **Ein-Prompt-je-Paket**-Variante (~15k Tokens
> je Paket); der heutige Messpfad prüft **je Datei**. Die Zahl ist nur tragbar, weil die
> Modulliste **maschinell** erzeugt und je Injektionscommit validiert wird (Punkte (2) und
> (3) oben) — ein vergessener Ilograph-Eintrag ist ein stiller Messausfall.
>
> **(9) Drei Fidelitätsverzichte gegenüber dem Vorbild, hiermit vermerkt.**
> - **Kein kontexteigener Verdrahtungs-`core`** (obwohl im Vorbild vorhanden, c1a B3/B5).
>   Begründung: er importiert im Vorbild **quer durch seinen Kontext**, also auch
>   `mappers` — damit wäre `api` nicht mehr der einzige Importeur von `mappers` und
>   **Z2′ (ii) fiele für alle drei `CYCLE_SIBLING`-Paare** (§3).
> - **Keine Kompositionswurzel** (kein `app`-Paket, kein `main.py`); das **Wurzelmodul**
>   `depot` aus `src/depot/__init__.py` wird der **Kern-Komponente** zugeordnet. Zulässig,
>   weil `componentOf` ein exakter Lookup ist (Punkt (6) oben) — und deklarationspflichtig.
> - **Die Relation `<k>_services → <k>_models` ist ausgelassen**, obwohl im Vorbild
>   vorhanden, um `models` **frei von Zusatzimporteuren** zu halten.
>
> **(10) KORREKTUR am eigenen Amendment vom 13.08., Punkt (6).** Der dortige Satz „der
> **Injektionsträger** ist also eine `__init__.py`" ist **FALSCH** und wird hiermit
> korrigiert; der alte Text bleibt unverändert stehen. Richtig ist: die **Clean-Kante
> Eltern→Kind** liegt in der `__init__.py`; die **INJIZIERTE Kante Kind→Eltern** liegt im
> **Kindmodul**, **Träger ist das Kindmodul** (im Entwurf `…services.pricing.engine`).
> Der erste Halbsatz — das **Elternmodul** ist die `__init__.py`, und ihr Soll-Eintrag
> lautet auf den Paketnamen — **bleibt richtig**. Folge für §5 siehe dortiges Amendment.

> **Nachtrag (13.08.2026, Rev. 14) — Begründung: `planung/c1_modulliste.md` (Schritt 4),
> `planung/c1_komponentenschnitt.md` §3.1 Rev. 2, `c2b_bericht_erlaubnislisten.md` §2.**
> Drei Zuordnungs- bzw. Größenfestlegungen und ein fünfter Ausfallmodus.
>
> **(a) Zuordnungsregel für die vier PHANTOMEINTRÄGE: der Zielort erbt die Komponente des
> Moduls an seinem sauberen Ort.** Das Amendment vom 12.08. (Punkt (1)) verlangt, dass das Soll
> die vier Zielorte listet, sagt aber nicht, **welcher Komponente** sie zugeordnet werden. Die
> Lücke war nicht folgenlos: `component` ist Bestandteil des `match_key`
> (`category|component|module|subjectKey`), und ohne die Regel sind die vier
> `expected_match_key` für die `INCORRECT_LOCATION`-Injektionen **nicht berechenbar**.
>
> | Injektion | sauberer Ort | Zielort (Phantom) | geerbte Komponente |
> |---|---|---|---|
> | I25 | `depot.orders.repository.legacy_order_index` | `depot.orders.legacy_order_index` | `orders_repository` |
> | I26 | `depot.billing.repository.legacy_invoice_index` | `depot.billing.legacy_invoice_index` | `billing_repository` |
> | I27 | `depot.identity.repository.legacy_token_index` | `depot.identity.legacy_token_index` | `identity_repository` |
> | I28 | `depot.billing.models.legacy_tax_models` | `depot.billing.legacy_tax_models` | `billing_models` |
>
> **Nachtrag (14.08.2026, Rev. 15).** Die Zeile zu I28 trug bis Rev. 14 den Namen
> `legacy_tax_table`; sie ist mit der Umbenennung der `models`-Schicht auf `*_models`
> nachgezogen (§3 Nachtrag Rev. 15, `c1_modulliste.md` Rev. 3 §D.9). Sauberer Ort, Zielort und
> geerbte Komponente sind sonst unverändert — der Zielort bleibt **direktes Kind** von
> `depot.billing`. Die Namen dieser Tabelle gehen in den `expected_match_key` ein; sie müssen
> mit `c1_modulliste.md` zeichengleich sein.
>
> **Drei Gründe, die zusammen tragen.** Erstens ist **R-PLACE-1 für genau diese Komponenten
> gescopt** (alle `…_models` und `…_repository`, Komponentenschnitt §8) — der Regelaufruf
> findet also statt, das verschobene Modul erhält die Regel, die es verletzt. Bei jeder anderen
> Zuordnung liefe es entweder in eine ungescopte Komponente (kein `checks_performed`-Eintrag,
> garantierter False Negative) oder es bräuchte eine Zusatzregel, die es sonst nirgends gibt.
> Zweitens ist die Aussage **inhaltlich richtig**: das Soll nennt die **vorgesehene**
> Komponente, und dass die Datei anderswo liegt, ist genau der zu meldende Verstoß — das Soll
> beschreibt den Sollzustand, nicht den Fundort. Drittens wird der `component`-Anteil des
> `match_key` damit für I25–I28 berechenbar und im Manifest vorab eintragbar. **Entlastend
> gegenüber T2 unverändert:** die Modulliste des Soll geht nicht in den Prompt ein
> (`b1_bericht_matchkey.md` C3), das Modell sieht die Phantomeinträge nie.
>
> **(b) Zuordnungsregel für die FÜNF PAKETMODULE.** `depot`, `depot.core`, `depot.identity`,
> `depot.orders` und `depot.billing` gehören im Soll zur Komponente **`core`**
> (Komponentenschnitt §3.1 (2)). Hintergrund ist die dortige Festlegung (1): **alle** Pakete
> erhalten eine `__init__.py`, auch die Kontextpakete und `depot.core`, die selbst keine
> Komponenten sind — **keine PEP-420-Namensraumpakete**. Grund ist ein Werkzeugrisiko: die
> K4-Konfiguration verwendet die Kontextpakete als `containers` der `layers`-Contracts, als
> `modules` des `independence`-Contracts und als Abstiegsziel von `acyclic_siblings`; ob
> **grimp 3.15** dort ein Paket ohne `__init__.py` auflöst, ist **ungemessen**, und die
> Fixtures aus c2a und c2b trugen auf allen diesen Ebenen eine `__init__.py`. Ein Ausfall
> zeigte sich frühestens in **C3** — also **nach** dem Freeze der beiden
> Baseline-Konfigurationsdateien (§1, Amendment 12.08.), und ein Amendment danach kostet den
> vollständigen Re-Run aller Konfigurationen. Die fünf Paketmodule sind **leer**, tragen kein
> Szenario, erzeugen keine Kante, stehen in keinem Diff und sind als `__init__.py` aus dem
> Clean-Control-Set ausgeschlossen (§5); ihr Soll-Eintrag verhindert allein den
> **unmapped**-Fall. Die frühere Ableitung „genau eine `__init__.py` je Komponente" **entfällt
> damit**; normiert ist nur noch, dass jede Komponente **mindestens ein inhaltstragendes
> Modul** hat.
>
> **(c) Richtwert erneut korrigiert: 72–75 Dateien**, davon **50–52 inhaltstragend**, bei
> **19 Komponenten in 23 Paketen**. Der in Rev. 12 gesetzte Wert „rund 70 Dateien" ist damit
> überholt; er kannte die vier zusätzlichen `__init__.py` aus (b) noch nicht und buchte
> Wurzelmodul und Adapter-Fassade doppelt (Nachweis in `c1_modulliste.md` §D.2/§D.3).
> **Ausgeführt: 73 Dateien, 50 inhaltstragend, 23 `__init__.py`** — maschinell nachgerechnet
> (`c1_modulliste.md` §3). **Die Tokenrechnung aus Befund 05 wird weiterhin NICHT neu
> gerechnet** (Begründung unverändert, Punkt (8) oben).
>
> **(d) FÜNFTER Ausfallmodus — eine K5-Regel auf ein externes Modul bricht das Werkzeug ab,
> sobald der Import verschwindet.** Externe Knoten existieren in PyTestArch nur, **solange sie
> importiert werden** — anders als Projektmodule, die als Dateien im Baum liegen. Gemessen
> (c2b §2b, Nebenbefund): dieselbe Regel auf `sqlalchemy`, die im Positivfall bricht, endet im
> **Negativfall** nicht in KEPT, sondern in `NetworkXError: The node sqlalchemy is not in the
> digraph.` **Abgrenzung:** derselbe Ausfalltyp wie Punkt (7) — laut, aber ergebnislos —, aber
> **ein anderer Auslöser**: dort ein Tippfehler im Regelziel, hier ein Regelziel, das durch die
> **Injektion** aus dem Graphen verschwindet. K4 hat das Problem nicht: dort bleibt der Knoten
> `sqlalchemy` im Graphen, solange ihn **irgendein** Modul importiert, und der Negativfall
> läuft KEPT durch (c2b §3a). **Konsequenz, als Bauvorschrift:** die K5-Framework-Regeln dürfen
> **kein externes Modul namentlich als Ziel führen**, wenn eine Injektion den zugehörigen
> Import entfernen kann. Für `FRAMEWORK_TYPE_IN_SIGNATURE` ist das erfüllt — das Rezept lässt
> den Import ausdrücklich **unverändert** (§3, Rezepttabelle) und der Zwilling trägt ihn
> ohnehin —, aber die Bedingung ist zu prüfen und nicht vorauszusetzen. Sie erweitert
> **Bauvorschrift K5-1** (§3, (iv)) um die externe Seite: dort sind Projektmodule gesperrt, die
> eine Injektion verschiebt oder entfernt, hier externe Module, deren letzter Importeur
> wegfallen kann.

> **Nachtrag (14.08.2026, Rev. 17) — KONTAMINATIONSFREIHEIT IST ZU DATIEREN.** Begründung:
> `planung/arbeitsplan_bis_abgabe.md` Block 8 (Reproduzierbarkeits-Anhang);
> `4b4_bericht_baseline_billing.md` §8.
>
> Der Absatz „Kontaminationsfreiheit" oben sagt, das Testrepo sei **„nie öffentlich verfügbar
> gewesen"**. Die Aussage bleibt stehen, ist aber **auf den EVALUATIONSZEITRAUM zu beziehen** —
> also auf die Zeit bis zur **letzten Messung** —, nicht auf „nie".
>
> **Grund:** Nach **Block 8 des Arbeitsplans** ist das Testrepo Teil des
> **Reproduzierbarkeits-Anhangs** und wird damit **nach Abschluss der Messungen zugänglich**.
> Das ist keine Schwächung der Validitätsaussage, sondern ihre korrekte Reichweite: was die
> Aussage gegen T1 trägt, ist die Unzugänglichkeit **zum Zeitpunkt des Pretrainings der
> gemessenen Modelle und während der Kampagne**. Eine spätere Veröffentlichung berührt keine
> gemessene Zahl; eine unbefristete Behauptung wäre dagegen mit dem eigenen Arbeitsplan
> unvereinbar und in der Verteidigung angreifbar.
>
> **Die `README.md` des Baseline-Commits formuliert es weiterhin absolut** (*„has never been
> publicly accessible … has stayed private since the first commit"*). Sie wird **NICHT
> geändert** — sie liegt in `B`, und `B` ist der Messbezugspunkt aller Läufe. Zum Zeitpunkt
> ihres Commits ist ihre Aussage zutreffend. Die zeitliche Präzisierung erfolgt **hier** und in
> **Kapitel 4**, nicht im Datensatz.

---

## 3. Verletzungskategorien & Injektionsplan

> **Amendment (12.08.2026) — Begründung: Decision Record P.** Die bisherige Kategorientabelle
> (S1–S4, M1, M2) und die darauf beruhende Erwartungsmatrix werden **ersetzt**, nicht ergänzt.
> Die bisherigen Kategorien waren operational definiert, aber **ohne Literaturanker**; **zwei
> von ihnen haben nachweislich keinen Beleg**; **keine von ihnen war gemessen worden**. Die
> Ersetzung erfolgt **vor dem Freeze und vor der ersten Injektion**. Der nachstehende Vermerk
> aus Rev. 3 („die Matrix selbst bleibt unverändert") bezieht sich auf die damalige, hier
> ersetzte Matrix; seine Sachaussage — Vorhersage gilt für `localized`, keine für `strict` —
> gilt für die neue Matrix unverändert fort.

**Sechs Abweichungstypen (Ebene 1), darunter zehn Policy-Szenarien (Ebene 2). Jede Injektion
wird zweistufig kodiert.** Insgesamt **32 Injektionen**, verteilt als **12/4/4/4/4/4**.
Platzierung verteilt über Pakete und Verschachtelungstiefen (nicht alle im selben Paket).
Jede Injektion = eigener Commit mit Manifest-Eintrag.

**Manifest-Felder (Ground Truth):** `id`, `kategorie`, `rule_id` (verletzte Regel aus
`architecture-rules.yaml`; bei rein topologie-abgeleiteten Verstößen der erwartete
`DERIVED:*`-Wert), `datei(en)`, `commit`, `beschreibung`, `injektions_rezept`,
`expected_match_key` (vorab berechneter Join-Schlüssel nach dem implementierten Schema
`category|component|module|subjectKey` aus `matchKey.ts`; `subjectKey` = `from->to` bei
Import-Kanten bzw. `offending_type` — nach
Decision Record L und P trägt `offending_type` bei `FORBIDDEN_SIGNATURE_TYPE` den
**Framework-Typnamen**, bei `STRUCTURAL_PLACEMENT` den **Modulnamen** und bei
`API_CONTRACT` den **Symbolnamen der abweichenden Funktion**; die Kantenkategorien
`FORBIDDEN_RELATION` und `CYCLE` tragen weiter `from`/`to`. Der erwartete Träger ist aus dem
Injektionsrezept bekannt und wird im Manifest festgehalten).

| Ebene 1 | Ebene 2 | Injektionen |
|---|---|---|
| `FORBIDDEN_RELATION` | `LAYER_BACK_CALL`, `LAYER_SKIP_CALL`, `PROTECTED_MODULE`, `INDEPENDENCE` | 3 je Szenario = 12 |
| `CYCLE` | `CYCLE_SIBLING`, `CYCLE_PARENT_CHILD` | **3 + 1 = 4** (geändert 12.08., siehe Amendment) |
| `ABSENCE_REQUIRED` | `MISSING_PORT_REFERENCE` | 4 |
| `FORBIDDEN_SIGNATURE_TYPE` | `FRAMEWORK_TYPE_IN_SIGNATURE` | 4 |
| `STRUCTURAL_PLACEMENT` | `INCORRECT_LOCATION` | 4 |
| `API_CONTRACT` | `SIGNATURE_DEVIATION` | 4 |
| **Summe** | **10 Szenarien** | **32 Injektionen** |

Dazu **4 Zwillingsmodule** im Clean-Control-Set (Decision Record P, Konsequenz 4).

Die Ebene-1-Bezeichnungen sind Bezeichner im Manifest und in der Harness (Englisch); die
deutschen Kapitelbezeichnungen werden hier einmal zugeordnet.

**Injektionsrezepte.** Alle Rezepte halten die Bauvorschriften aus Decision Record O (eine
Injektion je Modul) und aus B9+ (`import pkg.modul`, nie `from pkg import modul`) ein.

| Ebene 2 | Rezept |
|---|---|
| `LAYER_BACK_CALL` | Import aus einer tieferen in eine höhere Schicht ergänzen |
| `LAYER_SKIP_CALL` | Import aus der obersten Schicht direkt in die unterste, Zwischenschicht übersprungen; Richtung bleibt erlaubt |
| `PROTECTED_MODULE` | Import eines paketinternen Moduls von außerhalb der Allow-List, am Facade-Modul vorbei |
| `INDEPENDENCE` | Import zwischen zwei per Regel wechselseitig unabhängigen Paketen ergänzen |
| `CYCLE_SIBLING` | Rückkante zwischen zwei Geschwisterpaketen bzw. deren Nachkommen ergänzen |
| `CYCLE_PARENT_CHILD` | Rückkante von einem Untermodul auf sein eigenes Paket ergänzen |
| `MISSING_PORT_REFERENCE` | Vorgeschriebene Port-Typ-Referenz aus der öffentlichen Signatur entfernen **und den zugehörigen Import** (ergänzt 12.08., siehe Amendment (f)); Modul bleibt sonst unverändert |
| `FRAMEWORK_TYPE_IN_SIGNATURE` | Framework-Typ in einen Parameter- oder Rückgabetyp einer öffentlichen Funktion eines Domänenmoduls setzen. **Der Import bleibt unverändert erlaubt** — das Zwillingsmodul trägt denselben Import ohne Signaturbezug |
| `INCORRECT_LOCATION` | Modul unter Verstoß gegen eine explizite Namens- oder Platzierungsregel verschieben, Inhalt unverändert; **Zielort im Soll vorab gelistet, Modul ohne Importkanten** (ergänzt 12.08., siehe Amendment (e)) |
| `SIGNATURE_DEVIATION` | Parameter- oder Rückgabetyp einer Protocol-Implementierung von der in der Regel deklarierten Soll-Signatur abweichen lassen; **abweichender Typ ist ein Builtin oder bereits importiert, die Importmenge bleibt unverändert** (ergänzt 12.08., siehe Amendment (h)) |

**Zwingende Präzisierung zu `API_CONTRACT`.**

`SIGNATURE_DEVIATION` ist nur messbar, wenn die **Soll-Signatur in der Regel steht**, nicht
in einer anderen Datei. Der LLM-Pfad sieht ausschließlich die geänderte Datei; die
Protocol-Deklaration in `domain/ports.py` erreicht ihn bei einer Änderung an der
Implementierung **nicht**.

Die Regel muss die erwartete Signatur daher wörtlich im `statement` führen, etwa: *jede
Implementierung von `OrderPort` muss die Signatur `get(order_id: str) -> OrderDTO`
aufweisen.* Damit ist die Soll-Information Teil des Prompts, der ohnehin die Regeln enthält,
und die Kategorie bleibt diff-treu.

**Das ist der Unterschied zu `CYCLE`:** dort wären **Graphdaten** nötig, die mit dem Repo
wachsen; hier genügt eine **Regelaussage**, die statisch in der Regeldatei steht. Deshalb
ist `API_CONTRACT` messbar und `CYCLE` nicht.

> **Amendment (12.08.2026) — Begründung: Decision Records M und P.**
>
> **(a) CYCLE-Verteilung 3 + 1 statt 2 + 2.** Die vier `CYCLE`-Injektionen verteilen sich auf
> **3 `CYCLE_SIBLING`** und **1 `CYCLE_PARENT_CHILD`** (Tabelle oben entsprechend geändert).
> Begründung: c1a C6 fand am Vorbildsystem 5 Modulzyklen — 4 zwischen Geschwistern, 1 über
> Ebenen, **0** zwischen Paket und eigenem Untermodul. Die Gesamtzahl von **32 Injektionen
> bleibt unverändert**. `CYCLE_PARENT_CHILD` bleibt mit einer Injektion vertreten, weil es den
> gemessenen Blindfleck von `acyclic_siblings` prüft (B9+ F5) — das Szenario misst einen
> Werkzeugblindfleck, keine Häufigkeit.
>
> **(b) Vier Bauvorschriften für CYCLE-Injektionen, Z1–Z4.** Sie folgen aus der Kanonisierung
> der Zyklus-Kantenwahl (Decision Record M) und sind Bauparameter des Testrepos, keine
> Auswertungsregeln:
>
> **Z1 — genau zwei Komponenten, genau zwei Kanten.** Je `CYCLE`-Injektion sind genau zwei
> Komponenten und genau zwei Kanten beteiligt; die Clean-Baseline ist zyklenfrei. Grund: nur
> dann ist die Kandidatenmenge des `expected_match_key` abgeschlossen. Bei längeren Zyklen ist
> die Rückkante pfadabhängig (Decision Record M, Geltungsbereich der Handregel).
>
> **Z2 — das Ziel sortiert vor der Quelle.** Das Ziel der injizierten Kante sortiert in
> Code-Unit-Ordnung **vor** der Quelle. Grund: K1 meldet die Kante, die auf den kleineren
> Komponentennamen zeigt. Andernfalls beschuldigt K1 ein **unberührtes** Modul, was in
> **beiden** Metriken ein False Positive erzeugt und die FP-Reihe verunreinigt (Decision
> Record O, Nachtrag vom 12.08.).
>
> **Z3 — keine parallele Zeugenkante.** Zwischen dem Paar liegt keine zweite Kante derselben
> Richtung: genau **ein** Modul der Quellkomponente importiert die Zielkomponente. Grund: sonst
> entscheidet der Tiebreak `fromModule → file → line`, welches Modul beschuldigt wird.
>
> **Z4 — ASCII-Namen, Ordnung per Skript geprüft.** Komponenten- und Modulnamen bestehen nur
> aus ASCII-Kleinbuchstaben und Unterstrich; die Ordnung jedes `CYCLE`-Paares wird **per
> Skript** geprüft, nicht nach Augenmaß. Grund: `compareStrings` ist Code-Unit-Ordnung, in der
> der Unterstrich (`0x5F`) **vor** `a`–`z` sortiert.
>
> **(c) Importe.** Ausschließlich `import pkg.modul` (B9+) **und** ausschließlich auf
> **Modulebene** — keine Importe im Funktionsrumpf und keine unter `if TYPE_CHECKING`. Grund:
> der Extractor liest nur Top-Level-Importe.
>
> **(d) `FORBIDDEN_SIGNATURE_TYPE` — Regelwortlaut.** Die Regel nennt den
> **Persistenz-/Session-Typ**, nicht „Framework" allgemein. Begründung: `pydantic` ist in der
> `models`-Schicht des Vorbilds das Eigenwerkzeug (31 Statements, `c1a_nachtrag` §1.3), eine
> generische Framework-Regel wäre daher möglicherweise schon von der Clean-Baseline verletzt;
> `sqlalchemy` ist die gemessene saubere Grenze (Decision Record P, Nachtrag Punkt 4).
> **Injektion und Zwilling liegen in derselben Komponente und tragen dieselbe Importmenge**;
> der Zwilling verwendet den Typ ausschließlich in einer **Klassenattribut-Annotation** oder in
> einem **Aufruf im Klassenkörper**, also unterhalb der Extraktionsgrenze.
>
> **Nachtrag (23.08.2026, Rev. 20) — Zweck des Zwillings.** Träger und Zwilling haben
> **identische Importmengen** und unterscheiden sich allein darin, ob der Persistenztyp in einer
> öffentlichen Signatur steht. Ein Modell, das lexikalisch schließt („Import vorhanden" →
> Verstoß), meldet beide; ein Modell, das R-FRAMEWORK-1 liest (Import erlaubt, allein die
> Signaturverwendung verboten), meldet nur den Träger. Der Zwilling misst damit **UF1/UF2
> direkt**. Er bleibt im Clean-Control-Set und wird getrennt geführt. Die frühere Begründung
> über einen Falsch-Positiv der Baselines entfällt mit der Matrixkorrektur unten.
>
> **(e) `INCORRECT_LOCATION` — Zielort vorab gelistet, Modul ohne Importkanten.** Der Zielort
> steht im Soll (siehe §2, Amendment). Das verschobene Modul hat **keine ausgehenden Importe**
> und wird **von niemandem importiert**. Grund: nur so ist die vorregistrierte Zelle
> **K5 = nein** (Fußnote 6) begründet — PyTestArch erreicht ein falsch platziertes Modul
> ausschließlich als **Import-Proxy** und nur, sofern es überhaupt Importkanten hat. Hätte das
> Modul ausgehende Importe, wäre die Zelle „teilweise" und die vorregistrierte Vorhersage
> falsch. Der Umzug erscheint im Diff als **hinzugefügte Datei**; gelöschte Dateien fallen aus
> dem Diff heraus (`b33_bericht_diff_erzeugung.md`, Schritt 1).
>
> **(f) `MISSING_PORT_REFERENCE` — Annotation und Import entfernen.** Die Injektion entfernt die
> Port-Typ-Referenz aus der öffentlichen Signatur **und den zugehörigen Import**. Grund: die
> Erwartungsmatrix sagt **K5 = ja**, und PyTestArch wertet ausschließlich `ast.Import` und
> `ast.ImportFrom` aus (B9+ Frage 1); ohne Entfernen des Imports ist die Zelle **nicht
> erfüllbar**. **Ergänzend zur K5-Konfiguration:** `should()` hat **Aggregatsemantik** und gilt
> für die Modulmenge als Ganzes („mindestens eines"), nicht je Modul (B9+ Frage 4,
> Einschränkung 1). K5 braucht deshalb **vier Einzelregeln**, je eine auf ein Trägermodul
> benannt (`are_named`), **nicht** eine Regel über `are_sub_modules_of`.
>
> **(g) `INCORRECT_LOCATION` — die K4-Layerliste kommt aus dem Dateibaum, nicht aus dem Soll.**
> Fußnote 5 begründet **K4 = „teilweise"** damit, dass import-linter das verschobene Modul über
> `layers` mit `exhaustive = True` als **nicht deklariertes Kind** eines Containers findet.
> Seit Option B (§2) enthält die **Soll-Modulliste die vier Zielorte**. Würden die K4-Contracts
> aus derselben Liste erzeugt, wäre der Zielort deklariert, der Contract liefe **KEPT** durch
> und die vorregistrierte Zelle wäre **unerfüllbar** — gemessen belegt: „wird `order_repository`
> in dieselbe Layer-Liste aufgenommen, ist der Contract KEPT"
> (`b9plus_nachtrag_namensregeln.md`, Abschnitt 3). Das ist **dieselbe Klasse wie die vier
> Formulierungsfallen aus B38**: still grün trotz Verstoß.
> **Daher:** die `layers`-Liste des `exhaustive`-Contracts wird **aus dem Dateibaum der
> Clean-Baseline** erzeugt; die Differenz zur Soll-Modulliste sind genau die **vier
> Phantomeinträge**.
> **Platzierungsbedingung:** `exhaustive` setzt `containers` voraus und betrachtet nur
> **direkte Kinder** (ebd.) — der Zielort muss **direktes Kind eines Pakets** sein, das ein
> `exhaustive`-Contract abdeckt. Ausführung in **C2**, **B17** und der **B38-Prüfliste**.
>
> **(h) `SIGNATURE_DEVIATION` — die Importmenge bleibt unverändert.** **K1 = nein ist
> strukturell**: die Rule-Engine emittiert ausschließlich `DERIVED:forbidden-edge` und
> `DERIVED:cycle`. **K4 = K5 = nein hängt dagegen an der Bauweise**, denn beide werten
> ausschließlich `ast.Import` und `ast.ImportFrom` aus (B9+ Frage 1).
> **Daher:** der abweichende Typ ist ein **Builtin** oder ein Typ, den das Modul **bereits
> importiert**; die Injektion **fügt keinen Import hinzu und entfernt keinen**. Sonst könnten
> K4/K5 **aus dem falschen Grund** melden — je nach Contract als Treffer oder als False
> Positive —, und die **einzige nicht gemessene Zeile** der Erwartungsmatrix ruhte auf einer
> Annahme statt auf einer prüfbaren Vorschrift. Die **Soll-Signatur steht weiterhin wörtlich im
> `statement`** der Regel (Decision Record P), sonst erreicht sie den LLM-Pfad nicht.
> **Empirischer Anker:** die Signaturen des Vorbilds führen projektlokale Namen und Builtins
> (`c1a_nachtrag` §4.3); 6 `Protocol`-Klassen, davon 2 in `core/ports.py` (c1a C5).

> **Amendment (12.08.2026) — Begründung: B9+. Schließt die Lücke zwischen Erwartungsmatrix
> und C2.** Der **Contract-Typ je Szenario** wird hier vorregistriert, **nur auf Typebene**;
> konkrete Container- und Modulnamen folgen aus dem Komponentenschnitt und stehen in den
> Dateien aus C2. Wo ein Szenario in einem Werkzeug nicht ausdrückbar ist, steht das
> ausdrücklich — es wird **kein Typ erfunden**.
>
> | Szenario | K4 — import-linter 2.13 | K5 — PyTestArch 4.0.1 | Beleg |
> |---|---|---|---|
> | `LAYER_BACK_CALL` | `layers` | `should_only().import_modules_that()` bzw. `LayerRule` mit `should_only().access_layers_that()` | B9+ Frage 3 |
> | `LAYER_SKIP_CALL` | `forbidden` **zusätzlich** zu `layers`, mit `allow_indirect_imports = True`; n−2 Contracts für n Schichten | dieselbe `should_only()`-Regel wie beim Back-call — sie erfasst beide Fälle | B9+ Frage 3 |
> | `PROTECTED_MODULE` | `protected` (gleichwertig, aber schlechter wartbar: `forbidden` mit aufgezähltem Komplement) | `should_only().be_imported_by_modules_that()` | B9+ Frage 2 |
> | `INDEPENDENCE` | `independence`¹ | `should_not().import_modules_that()` | B9+ Frage 4 (Typliste), Frage 1 (Regelform) |
> | `CYCLE_SIBLING` | `acyclic_siblings` (`ancestors`, Standardtiefe 10) | **nicht ausdrückbar** — keine Zyklenregel, die Zeichenfolge `cycl` kommt im Paket nicht vor (**unverändert richtig**; dass die Erlaubnisliste die Injektion dennoch als nicht gelistete Kante meldet, ist eine **andere Regel** und steht in Fußnote 7) | B9+ Frage 5 |
> | `CYCLE_PARENT_CHILD` | **nicht ausdrückbar** — `acyclic_siblings` vergleicht ausschließlich Geschwister; Fall C blieb auch mit `ancestors = shop.audit` unerkannt, obwohl beide Kanten im Graph liegen | **nicht ausdrückbar** (wie oben; siehe Fußnote 7) | B9+ Frage 5 |
> | `MISSING_PORT_REFERENCE` | **nicht ausdrückbar** — `type = required` existiert nicht (`NoSuchContractType: required`); kein Contract-Typ ist positiv | `are_named(<Untermodul>).should().import_modules_that()`, **vier Einzelregeln** (Amendment (f)) | B9+ Frage 4 |
> | `FRAMEWORK_TYPE_IN_SIGNATURE` | Signaturebene **nicht ausdrückbar**; **kein Import-Proxy**, weil er R-FRAMEWORK-1 und C3 widerspräche | Signaturebene **nicht ausdrückbar**; **kein Import-Proxy**, weil er R-FRAMEWORK-1 und C3 widerspräche | B9+ Frage 1; c2b K4-Konfiguration §B6; Rev. 20 |
> | `INCORRECT_LOCATION` | Namens-/Ortsregel **nicht ausdrückbar** (kein Namensmuster in Modulfeldern, nur ganzsegmentige Wildcards); faktisch erkannt über `layers` mit `containers` und `exhaustive = True`, **namensblind** als nicht deklariertes Kind — Layerliste nach Amendment (g) aus dem Dateibaum | **nicht ausdrückbar** — kein Ortsprädikat als Regelobjekt; die Näherung `should_not().import_anything()` greift unter Amendment (e) nicht, weil das Modul keine Importkanten hat | B9+ Nachtrag, Abschnitte 1 und 3 |
> | `SIGNATURE_DEVIATION` | **nicht ausdrückbar** — kein Contract-Typ und keine Option erreicht die Signaturebene | **nicht ausdrückbar** — der Parser wertet ausschließlich `ast.Import`/`ast.ImportFrom` aus | B9+ Frage 1 |
>
> ¹ Der Typ stammt aus der vollständigen Contract-Liste von 2.13 (B9+ Frage 4, Semantik aus dem
> Docstring: „Mengen dürfen sich in keiner Richtung importieren"). Ein **eigener Fixture-Lauf
> für `independence` existiert nicht**; die Matrixzelle ist mit „F1-Kontext" belegt. Vor der
> Kampagne ist der Contract nach B38 mit Positiv- **und** Negativfall zu belegen.
>
> **K5-Regelebene.** Die vier `MISSING_PORT_REFERENCE`-Einzelregeln nennen den
> **Untermodulnamen** (`are_named`), **nicht das Paket**. Grund: das Testrepo schreibt
> durchgehend `import pkg.modul`, und diese Syntax löst PyTestArch **auf das Untermodul** auf
> (B9+ B17c); eine Regel auf Paketebene bzw. auf der falschen Ebene schlägt nach B9+ Frage 4,
> **Einschränkung 2** auch beim **konformen** Modul fehl (gemessen:
> `"…application.order_service" does not import "…domain.ports"`).
> **Vermerk zur Risikorichtung:** dieser Fehlerfall zeigt sich als **fehlgeschlagener
> Clean-State-Audit** — C3 fordert 0 Findings — und **nicht als stille Fehlmessung**. Er ist
> damit die **Gegenrichtung** zu den B38-Fallen und zu Amendment (g), die still grün
> durchlaufen.

> **Amendment (13.08.2026) — Begründung: `planung/c1_komponentenschnitt.md` §2 und §4.6;
> `c2a_bericht_contract_semantik.md` §5.1 und §3.** Verschärft **Z2**, benennt die
> Trägerwahl der `CYCLE_SIBLING`-Paare neu und ergänzt zwei Bauvorschriften. **Z1, Z3 und
> Z4 bleiben unverändert.**
>
> **(i) Z2′ — Verschärfung von Z2, nicht Ersatz.** Für ein `CYCLE`-Paar mit Clean-Kante
> S→T und injizierter Kante T→S ist der Träger des `CYCLE`-Records **genau dann ohne
> Traversierungssimulation vorhersagbar**, wenn
> **(i)** S in Code-Unit-Ordnung **vor** T sortiert **und**
> **(ii)** S im **Komponentengraphen des Injektionscommits** der **einzige Importeur** von
> T ist.
> Dann trägt der Record die **injizierte** Kante T→S, `location.component = T`, und
> `location.module` ist das importierende Modul in T — der Injektionsträger.
>
> **Beweisskizze** (aus `ruleEngine.ts:99-135`, Herleitung in
> `c1_komponentenschnitt.md` §2.3): `adjacency` ist über `edge.from` geschlüsselt, T hat
> die injizierte ausgehende Kante und ist damit möglicher DFS-Startknoten. Jeder Eintritt
> in T geschieht als Wurzel oder über eine Kante X→T; nach (ii) ist X = S, und dann ist S
> `VISITING`. Der Fall „T als Wurzel" tritt nicht ein, weil Wurzeln **aufsteigend**
> iteriert werden (`[...adjacency.keys()].sort(compareStrings)`) und T nach (i) über S
> bereits `DONE` ist. Ein **Umweg** von S nach T bräuchte eine Kante X→T mit X ≠ S, die
> (ii) ausschließt. Folglich erfüllt T→S stets `childState === VISITING`
> (`ruleEngine.ts:120`) und erzeugt den Record. ∎
> **Das ist eine Eigenschaft des Algorithmus, keine Fixture-Beobachtung.**
> **Konsequenz:** die in Decision Record M vorregistrierte Vorabprüfung **bleibt
> bestehen**, wird aber von einer **Ableitungsstütze** zu einer **Kontrolle**.
>
> **(ii) Folge für die Trägerwahl: die drei `CYCLE_SIBLING`-Paare liegen auf
> `<kontext>.api ↔ <kontext>.mappers`, nicht auf `models ↔ mappers`.** Letzteres verletzt
> Bedingung (ii): `models` hat mehrere Importeure (`api`, `services`, `repository`,
> `mappers`). Injizierte Richtung ist damit `mappers → api`, Clean-Kante `api → mappers`;
> (i) ist erfüllt (`…_api` < `…_mappers`) und per Skript zu prüfen (Z4).
> **Preis, als Abweichung deklariert:** das **häufigste reale Zyklusmotiv** sind gegenseitig
> verwiesene `mappers`-/`schemas`-Paare **innerhalb** eines Pakets (c1a C6, **4 von 5**) —
> für K1 strukturell unsichtbar, weil `from === to` (`ruleEngine.ts:47`) —, und der
> **fünfte** reale Zyklus liegt auf `models ↔ repository`. Nachgebildet wird die **LAGE**
> des Motivs (zwei Geschwisterpakete eines Kontextes verweisen gegenseitig), **nicht das
> Schichtenpaar**. Gehört zu T6/T8 in §9.
>
> **(iii) Bauvorschrift I1 — geteilte Komponenten bleiben importfrei gegenüber den
> unabhängigen Kontexten.** In **KEINEM** Commit trägt eine der geteilten Komponenten
> (Kern, Adapter, Adapter-Internum) oder eine Komponente des **gemeinsam genutzten
> Kontextes** eine Kante in einen der beiden **wechselseitig unabhängigen** Kontexte.
> Grund: `independence` wertet **transitiv** und besitzt in import-linter 2.13 **kein**
> `allow_indirect_imports` (c2a §3). Eine Kette `orders → core → billing` oder
> `orders → identity → billing` würde als Verletzung gemeldet — in einem Commit, dessen
> Injektion mit `INDEPENDENCE` **nichts zu tun hat**. I1 ist maschinell **gegen die
> Whitelist** und **gegen jeden Injektionscommit** prüfbar und gehört in die **Prüfschrift
> zu Z4**.
>
> **(iv) Bauvorschrift K5-1 — keine K5-Regel nennt ein Modul, das eine Injektion
> verschiebt oder entfernt.** Gesperrt sind die **vier `INCORRECT_LOCATION`-Träger** und
> ihre **Phantom-Zielorte**. Grund: ein Regelziel, das nicht im Graphen ist, erzeugt
> `NetworkXError` — Werkzeugabbruch statt Befund (§2, Amendment 13.08. Punkt (7);
> c2a §5.1). **`MISSING_PORT_REFERENCE` ist unbetroffen:** die Injektion entfernt den
> **Import**, das Portmodul bleibt bestehen.
>
> **(vi) Ergänzt 13.08.2026 (Rev. 14): R-PLACE-1 ist als NAMENSREGEL zu formulieren, nicht als
> reine Platzierungsregel.** Grund: **Fußnote 5** begründet die vorregistrierte Zelle
> `INCORRECT_LOCATION`/K4 = **„teilweise"** damit, dass import-linter das verschobene Modul
> über `layers` mit `exhaustive = True` findet, aber **namensblind** — als nicht deklariertes
> Kind, nicht als Namensverstoß. Das ist der Fall „richtige Stelle, falsche Art", der in
> `localized` anders zählt als in `strict`. Wäre R-PLACE-1 eine reine **Platzierungs**regel,
> fände K4 **dieselbe Art** von Verstoß wie K1/K2/K3, und die Zelle rutschte auf **„ja"** —
> eine vorregistrierte Zelle wäre damit nachträglich durch eine **Regelformulierung**
> verschoben statt durch eine Messung. Das ist unzulässig, unabhängig davon, in welche Richtung
> es die Zahlen bewegte. **Daher:** R-PLACE-1 führt die **Namenskonvention der Zielschicht**
> wörtlich im `statement`. Ausführung in **C2**; die Clean-Baseline muss die Konvention
> durchhalten, sonst bricht die Regel schon dort (`c1_modulliste.md` §D.9).
>
> **Nachtrag (14.08.2026, Rev. 15) zu (vi) — R-PLACE-1 hat ZWEI Klauseln, beide suffixbasiert,
> beide einseitig.** Vorregistriert wird hier die **Form**, nicht der Wortlaut; der genaue
> Regeltext bleibt **C2**. Einseitig heißt: die Klausel liest sich **„Name impliziert Ort"**,
> nicht umgekehrt — sie sagt nichts darüber, wie ein Modul heißen muss, das in einem der
> genannten Pakete liegt. Damit sind die Paketmodule (`depot.<k>.models`, `depot.<k>.repository`)
> und Module ohne das Suffix unbetroffen.
>
> > **Klausel 1** — Module, deren Name auf `_repo`, `_query` oder `_index` endet, liegen im
> > `repository`-Paket ihres Kontextes.
> > **Klausel 2** — Module, deren Name auf `_models` endet, liegen im `models`-Paket ihres
> > Kontextes.
>
> **Begründung für Klausel 2 — die Konvention ist gemessen, nicht erfunden.** Die
> `models`-Schicht des Vorbildsystems führt genau diese Endung: fünf der sechs inhaltstragenden
> Module in `iam/models` heißen `*_models.py` (darunter `permission_models.py`, das einzige
> `models`-Modul des Systems mit `sqlalchemy`-Import), in `vertiport/models` steht sie neben
> `*_schemas` (`c1a_nachtrag_framework_importe.md` §2/§3.2). Das Testrepo wählt eine der beiden
> gemessenen Endungen und hält sie in allen drei `models`-Komponenten durch — eine **Verengung**
> des Vorbilds, keine Erfindung. Ausgeführt in `planung/c1_modulliste.md` Rev. 3: alle zwölf
> `models`-Module inklusive der vier Zwillinge und des I28-Trägers tragen die Endung; maschinell
> geprüft mit **0** Verstößen im Clean-Zustand und **genau einem** verletzenden Phantom (I28).
>
> **Ausdrücklich festgehalten: warum die beiden in `c1_modulliste.md` §D.9 genannten Kandidaten
> ausfallen.** Beide sind geprüft und **verworfen**:
>
> - *Eine Ortsklausel nur für `models`* ist **keine Namensregel** und fällt damit unter genau den
>   Vermerk von (vi): import-linter fände über `layers`/`exhaustive` **dieselbe Art** Verstoß wie
>   K1/K2/K3, und die vorregistrierte Zelle K4/`INCORRECT_LOCATION` verschöbe sich von
>   **„teilweise" auf „ja"**. Eine vorregistrierte Zelle darf **nicht durch eine
>   Regelformulierung** bewegt werden — unabhängig davon, in welche Richtung.
> - *Ein Verbot des Präfix `legacy_` in `models`* würde **von der CLEAN-Baseline selbst
>   verletzt**: der Träger von I28 liegt im Clean-Zustand in `billing/models` und hieße dort
>   weiterhin `legacy_*`. Die Regel bräche **vor** der ersten Injektion und ließe den
>   **Clean-State-Audit** durchfallen (C3 fordert 0 Findings) — derselbe Fehler, den die
>   Umbenennung von `legacy_token` in `c1_modulliste.md` Rev. 2 gerade vermieden hat.
>
> **Folge:** I28 ist nicht länger die einzige `INCORRECT_LOCATION`-Injektion ohne verletzte
> Regel. Alle vier Träger I25–I28 sind von einer der beiden Klauseln getroffen, und der
> `rule_id`-Eintrag im Manifest ist für alle vier besetzbar. **Keine Matrixzelle bewegt sich.**
>
> **(v) Erwartungsmatrix — eine Zelle bekommt eine Annotation, kein Wert ändert sich.**
> Die Zelle **K4/`PROTECTED_MODULE` (ja)** ist an den **Contract-TYP `protected`**
> gebunden: mit `forbidden` in Vorgabestellung wäre sie **nicht erfüllbar** (indirekte
> Kette `services → storage → internal`, c2a §1.1c). Annotiert als **ᴾ**, in derselben
> Form wie (e), (g), (h), mit Zeiger auf das **§1-Amendment vom 13.08.**
> **Die Matrixwerte bleiben unverändert.**

> **Nachtrag (14.08.2026, Rev. 16) — Begründung: `4b1_bericht_baseline_kern.md` §3.1–§3.4, §5.1
> und §6.3.** Drei Bauentscheidungen aus dem ersten Baucommit der Clean-Baseline, hier
> vorregistriert, weil jede von ihnen an einer vorregistrierten Regel oder Zelle hängt.
> **Keine Matrixzelle bewegt sich.**
>
> **(A) RESERVIERUNGSREGEL FÜR PORTS.** Die vier Ports der `MISSING_PORT_REFERENCE`-Träger
> I17–I20 — **`TokenSigner`** (I17 `…identity.services.token_service`), **`RateProvider`**
> (I18 `…orders.services.catalog_service`), **`PaymentGateway`** (I19
> `…orders.services.refund_service`), **`Clock`** (I20 `…billing.services.ledger_service`) —
> sind **reserviert**: jeder dieser vier Ports erscheint in der Clean-Baseline in **genau EINEM**
> Modul, nämlich seinem Träger, und dort in einer **öffentlichen Methodensignatur**. Alle
> übrigen Importeure von `depot.core.ports` verwenden **andere** Ports; `depot.core.ports` darf
> zu diesem Zweck in den Bauaufträgen **4b-2 bis 4b-4 erweitert** werden.
>
> **Grund.** `R-PORT-1…4` sind nach Komponentenschnitt §6.3 **vier Einzelregeln**, je auf ein
> **Trägermodul** mit `are_named` gebunden. Ein mehrfach verwendeter Port machte die Zuordnung
> **Befund → Regel mehrdeutig** — der `rule_id`-Eintrag im Manifest wäre nicht mehr eindeutig
> einer der vier Injektionen zuzuordnen. Zweiter, unabhängiger Grund: dieselbe Portschnittstelle
> in fachlich unverwandten Modulen wäre bei der **Sichtprüfung als konstruiert erkennbar** und
> schwächte die Nachbildungsgüte des Datensatzes. Dass `ports.py` dadurch **in mehreren Commits
> wächst**, ist unerheblich: die Datei wandert durch vier Baucommits, aber `B` ist der **letzte**
> der vier, und für den Messpfad zählt allein **sein Zustand** (§6, Sternhistorie mit `B` als
> einzigem Elternteil). Die Alternative „Wiederverwendung der sieben vorhandenen Ports"
> (`4b1_bericht_baseline_kern.md` §3.4 (a)) ist damit **verworfen**.
>
> **(B) ALLE VIER `API_CONTRACT`-Regeln (R-SIG-1…4) prüfen EINHEITLICH über den
> `statement`-Wortlaut**, nicht über ein Protocol im Repo. Grund:
> `depot.orders.mappers.order_line_mapper` (**I32**) importiert nach `c1_modulliste.md` §1
> `depot.core.ports` **nicht** — die Importmenge bleibt nach Amendment (h) unverändert — und kann
> deshalb **kein** Protocol referenzieren. Für I29–I31 wären beide Wege gangbar; eine
> **Ungleichbehandlung** der vier Regeln derselben Kategorie wäre aber nicht begründbar und
> machte `API_CONTRACT` uneinheitlich prüfbar. Die drei Ports aus dem 4b-1-Bericht §3.2
> (`SessionStore`, `DiscountCatalog`, `PaymentLedger`) **bleiben** als **Implementierungsvorlage**
> im Repo; für die Regelprüfung sind sie ohne Bedeutung. Der **Wortlaut** des `statement` bleibt
> **C2** (Modulliste §D.8, unverändert).
>
> **(C) FASSADENFORM: `core/adapters/__init__.py` löst die re-exportierten Namen über ein
> Modul-`__getattr__` (PEP 562) auf.** Grund, **gemessen** in `4b1_bericht_baseline_kern.md`
> §5.1: `import depot.x.y` plus **eager** Symbol-Zuweisung im eigenen `__init__.py` bricht in
> CPython mit `AttributeError: cannot access submodule 'adapters' of module 'depot.core'` — die
> Importmaschinerie setzt das Attribut auf dem Elternmodul erst **nach** `exec_module`; während
> die Fassade läuft, ist der Pfad `depot.core.adapters` nicht traversierbar. **V12 bleibt damit
> ohne Ausnahme.**
>
> Zwei Gründe **gegen** die geprüfte Alternative (V12-Ausnahme für Re-Export-`__init__.py`):
> **(i)** die Auflösung von `from <vollqualifiziertes modul> import <symbol>` ist für dieses
> Werkzeugpaar **UNGEMESSEN** — B9+ und B17c betreffen `from <paket> import <modul>`, eine
> **andere** Form; **(ii)** die Fassade ist für **keines** der zehn Szenarien Messobjekt, ihre
> innere Codeform ist für **jede** Regel irrelevant — eine Bauvorschrift dafür aufzuweichen wäre
> ein **Tausch ohne Messgewinn**.
>
> **Statisch ist die Form folgenlos:** die drei Top-Level-Importe stehen unverändert im
> Modulkopf, die Kante `core_adapters → core_adapters_internal` ist sichtbar, und `core_adapters`
> bleibt ihr **einziger** Importeur (Z2′ (ii), Abnahmebedingung 7). K1, K4 und K5 arbeiten rein
> statisch, und die Kampagne importiert das Repo nicht (`c1_modulliste.md` §D.6). Die
> **Abweichung vom gemessenen Vorbild** — c1a C2: **9 von 9** realen Fassaden schreiben
> `from .x import Y` — gehört nach **§9 zu T6**.

> **Nachtrag (23.08.2026, Rev. 18) — SCHLÜSSELBILDENDE SCHREIBWEISEN, VERBINDLICH FÜR C4.**
> Begründung: `c2a_bericht_regeldatei.md` §4 und §8. Die drei Angaben bilden das **vierte
> Segment** des `match_key` (`matchKey.ts:26`,
> `category|component|module|subjectKey`); ohne sie ist `expected_match_key` für zwölf der
> 32 Injektionen nicht berechenbar. Sie standen bisher **nur in einem Bericht** und gehören
> in die Vorregistrierung. **Keine Matrixzelle bewegt sich.**
>
> | Kategorie | `subject.offending_type` trägt | Beispiel | Herleitung |
> |---|---|---|---|
> | `ABSENCE_REQUIRED` | den **Porttyp in der Schreibweise des `statement`** — vollqualifiziert, mit Punktkette | `depot.core.ports.TokenSigner` | c2a §4.1; bei einer Absence fehlt das Beanstandete im Code und hat dort keinen Namen (Decision Record P, Punkt 3), der Name kommt aus der Regel |
> | `API_CONTRACT` | den **Symbolnamen der abweichenden Funktion als `Class.method`**, bei einer Top-Level-Funktion den bloßen Namen | `SessionRepository.touch`, `to_payload` | c2a §4.2; das ist die Form, die der Extractor in `FactSignature.symbol` schreibt (`rawAstFacts.ts:51-55`) und die im Prompt erscheint |
> | `STRUCTURAL_PLACEMENT` | die **volle Punktkette des fehlplatzierten Moduls** | `depot.billing.legacy_tax_models` | c2a §4.3; sie kommt im Prompt als `module: …` wörtlich vor, das letzte Segment nicht |
>
> Die vier Portschreibweisen im Einzelnen: **`depot.core.ports.TokenSigner`** (I17),
> **`depot.core.ports.RateProvider`** (I18), **`depot.core.ports.PaymentGateway`** (I19),
> **`depot.core.ports.Clock`** (I20). Die vier Symbolschreibweisen:
> **`SessionRepository.touch`** (I29), **`OrderQuery.percent_for`** (I30),
> **`InvoiceQuery.settled_cents`** (I31), **`to_payload`** (I32).
>
> **Ergänzung zu Decision Record L/P**, der bei `STRUCTURAL_PLACEMENT` „den Modulnamen" und bei
> `API_CONTRACT` „den Symbolnamen" sagt, ohne zwischen voller Kette und letztem Segment bzw.
> zwischen `method` und `Class.method` zu entscheiden. Beide Wahlen folgen demselben Kriterium:
> **genommen wird die Form, die im Prompt wörtlich vorkommt**, weil das Systemprompt „verbatim
> as it appears in the imports or signatures given to you" verlangt (`contextBuilder.ts:58-59`)
> und weil die `strict`-Metrik den Zeichenvergleich führt.
>
> **Vermerk zu `FORBIDDEN_SIGNATURE_TYPE`:** hier bleibt es beim Framework-Typnamen (Decision
> Record L/P, unverändert). **Welcher** Typ injiziert wird, entscheidet C4; die Auflage aus
> R-FRAMEWORK-1 ist, dass er aus dem Namensraum **`sqlalchemy.orm`** stammt.

> **Nachtrag (23.08.2026, Rev. 18) — DIE VIER R-PORT-STATEMENTS SIND GEKÜRZT.** Begründung:
> `c2a_bericht_regeldatei.md` Nachtrag §N1. Änderung am **Messeingang vor jeder Messung**;
> sie ist eine **Rückkehr zum vorregistrierten Wortlaut**, keine Erweiterung.
>
> **Was entfällt:** die **wörtliche Soll-Signatur** in `R-PORT-1…4`.
> **Was bleibt, unverändert zwingend:** das **Trägermodul namentlich**, die betroffene
> **öffentliche Methode als `Class.method`**, der **Porttyp in der bindenden Schreibweise**,
> und die Aussage, dass die Referenz **in der öffentlichen Signatur dieser Methode** zu führen
> ist.
>
> **Grund 1 — keine Vorgabe verlangte die Signatur.** Komponentenschnitt §8 verlangt für
> `R-PORT-1…4` die **Typschreibweise** („Typschreibweise im `statement` **identisch** zur
> Manifest-Erwartung"), nicht die Signatur. Die wörtliche Signatur ist **Regelinhalt bei
> `API_CONTRACT`** — dort verlangt sie die „Zwingende Präzisierung zu `API_CONTRACT`" in diesem
> Abschnitt ausdrücklich, weil der LLM-Pfad die Protocol-Deklaration sonst nicht erreicht — und
> bei `ABSENCE_REQUIRED` gerade **nicht**.
>
> **Grund 2 — sie inflationiert die Kategorie.** Mit der vollen Signatur im `statement` wird die
> Prüfung zum **Zeichenkettenvergleich**: das Modell hält die gegebene Signatur gegen die
> gesehene und meldet die Differenz. `ABSENCE_REQUIRED` trüge dann einen Vorteil, der aus dem
> Regeltext stammt und nicht aus der semantischen Leistung — und zwar in genau der Kategorie, in
> der K1 und K4 **nein** tragen und K2/K3 als Mehrwert ausgewiesen werden (UF3). Der Vergleich
> gegen die Baselines wäre verzerrt, und zwar **zugunsten** des LLM-Pfades.
>
> **Grund 3 — die Trägernennung ist davon unberührt und bleibt.** Regel-Scopes sind
> **komponentenweit** (`contextBuilder.ts:19`), eine Modulgranularität gibt es im Checker nicht.
> Ohne Nennung von Modul und Methode wären `R-PORT-2` und `R-PORT-3` auf jedem Modul von
> `orders_services` nicht unterscheidbar. Siehe dazu den §5-Nachtrag derselben Revision.
>
> **Wirkung, abgezählt** (c2a-Nachtrag §N5): die vier Statements schrumpfen von 651/678/690/757
> auf 480/487/488/596 Zeichen, der Prompt des am dichtesten gescopten Moduls
> (`depot.orders.services.refund_service`, sechs Regeln) von **4 920 auf 4 527 Zeichen**. Der
> `rules_sha256` verschiebt sich entsprechend und ist im Messmanifest nachgezogen. **Keine
> Matrixzelle bewegt sich, kein `expected_match_key` ändert sich** — die Portschreibweise, die
> allein in den Schlüssel eingeht, ist unverändert.

**Abbildung der alten Kürzel (alt → neu).** Damit die Befunde 01–06 zitierfähig bleiben:

| alt | neu (Ebene 1 / Ebene 2) |
|---|---|
| S1 | `FORBIDDEN_RELATION` / `LAYER_BACK_CALL` |
| S2 | `CYCLE` |
| S3 | `FORBIDDEN_RELATION` / `PROTECTED_MODULE` |
| S4 | `FORBIDDEN_RELATION` / `INDEPENDENCE` |
| M1 | `FORBIDDEN_SIGNATURE_TYPE` / `FRAMEWORK_TYPE_IN_SIGNATURE` (umformuliert: Import bleibt erlaubt, Verstoß nur in der Signatur) |
| M2 | **entfallen**, ersetzt durch `STRUCTURAL_PLACEMENT` / `INCORRECT_LOCATION` |

**Vermerk:** Die alten Kürzel bleiben in den Befunden 01–06 als historische Bezeichnung
stehen und werden in der Arbeit nicht mehr verwendet.

Die semantischen Kategorien `FORBIDDEN_SIGNATURE_TYPE`, `STRUCTURAL_PLACEMENT` und
`API_CONTRACT` sind so konstruiert, dass sie unter der **Extraktionsgrenze** (Imports und
Signaturen) sichtbar sind; der AST-Extractor liefert keine Funktionskörper. Regeln, die nur
im Funktionskörper sichtbar wären, sind außerhalb des Messbereichs und werden in der
Diskussion als Grenze benannt. Dass die Baseline-Werkzeuge diese Kategorien nicht ausdrücken
können, ist **gemessen** (B9+, import-linter 2.13 und PyTestArch 4.0.1) und nicht
vorausgesetzt: beide werten ausschließlich `ast.Import` und `ast.ImportFrom` aus. Bei
`FORBIDDEN_SIGNATURE_TYPE` entsteht für K4 und K5 eine **strukturelle Nicht-Abdeckung**:
allein K2/K3 können etwas finden. Das ist kein Werkzeugversagen, sondern folgt aus der
Importkanten-Grenze beider Baselines.

**Erwartungsmatrix (vorregistriert — das ist die falsifizierbare Fassung der Pointe aus §5
Umsetzungsplan):**

**Gilt für die Metrik `localized` (§4, Decision Record O). Für `strict` besteht keine
Vorhersage.** K4 = import-linter 2.13, K5 = PyTestArch 4.0.1 — versionsgebunden.

| Ebene 2 | K1 det. | K4 | K5 | K2/K3 LLM | Belegquelle der K4/K5-Zellen |
|---|---|---|---|---|---|
| `LAYER_BACK_CALL` | ja | ja | ja | ja | gemessen (B9+ F3) |
| `LAYER_SKIP_CALL` | ja | ja¹ | ja | ja | gemessen (B9+ F3) |
| `PROTECTED_MODULE` | ja | ja ᴾ | ja | ja | gemessen (B9+ F2) |
| `INDEPENDENCE` | ja | ja | ja | ja | gemessen (B9+ F1-Kontext) |
| `CYCLE_SIBLING` | ja | ja | ~~nein~~ **teilweise⁷** | **nein²** | K4 gemessen (B9+ F5) · **K5-Zelle gemessen** (`c2c…K5-Konfiguration` §B5) — geändert im Nachtrag Rev. 22 |
| `CYCLE_PARENT_CHILD` | ja | **nein** | ~~nein~~ **teilweise⁷** | **nein²** | K4 gemessen (B9+ F5) · **K5-Zelle gemessen** (`c2c…K5-Konfiguration` §B5) — geändert im Nachtrag Rev. 22 |
| `MISSING_PORT_REFERENCE` | **nein³** | **nein** | ja | **ja** | gemessen (B9+ F4) |
| `FRAMEWORK_TYPE_IN_SIGNATURE` | nein | **nein⁴** | **nein⁴** | **ja** | **K4 gemessen** (`c2b…K4-Konfiguration` §B6) · **K5 gemessen** (`c2c…K5-Konfiguration` §B6) — aufgespalten im Nachtrag Rev. 21 |
| `INCORRECT_LOCATION` | nein | **teilweise⁵** ᴳ | nein⁶ ᴱ | **ja** | gemessen (B9+ Nachtrag) |
| `SIGNATURE_DEVIATION` | nein | nein ᴴ | nein ᴴ | **ja** | abgeleitet, nicht gemessen |

**Hochgestellte Buchstaben = die Zelle ist an eine Bauvorschrift gebunden** (ergänzt
12.08.2026, Amendments in diesem Abschnitt): **ᴱ** = (e), das verschobene Modul hat keine
Importkanten · **ᴳ** = (g), die `layers`-Liste des `exhaustive`-Contracts kommt aus dem
Dateibaum und nicht aus der Soll-Modulliste · **ᴴ** = (h), die Injektion ändert die Importmenge
nicht. Diese drei Zellen sagen aus, was die Werkzeuge **unter diesen Bauvorschriften** leisten;
unter anderen Vorschriften wären sie anders besetzt. In Kapitel 4 als **Konstruktionsbedingung**
zu benennen, nicht als Werkzeugbefund.

**Ergänzt 13.08.2026 (Amendment zu Z2′/I1/K5-1 in diesem Abschnitt): ᴾ** = die Zelle ist nicht
an eine Bauvorschrift, sondern an einen **Contract-Typ** gebunden — K4/`PROTECTED_MODULE` gilt
für `type = protected`; mit `forbidden` in Vorgabestellung wäre sie wegen der transitiven
Auswertung **nicht erfüllbar** (§1, Amendment 13.08.; c2a §1.1c). Damit ist die Matrix an
**vier** Stellen an Bauvorschriften (ᴱ, ᴳ, ᴴ) und an **einer** Stelle an einen Contract-Typ
(ᴾ) gebunden.

> **Nachtrag (23.08.2026, Rev. 21) — ZWEI NACHZÜGE AUS REV. 20.** Begründung:
> `c2b_bericht_k4_konfiguration.md` §B5 (g) und §B6, `c2c_bericht_k5_konfiguration.md` §B6,
> `planung/c1_komponentenschnitt.md` **Rev. 3** §3.1 (4) und §6.1. **Der Alttext oben bleibt
> unverändert stehen**; korrigiert wird hier, nicht dort. **Keine Matrixzelle bewegt sich.**
>
> **(1) DIE BEGRÜNDUNG DER ANNOTATION ᴾ GILT NICHT FÜR DEN MESSGEGENSTAND.** Der Satz „mit
> `forbidden` in Vorgabestellung wäre sie wegen der transitiven Auswertung **nicht
> erfüllbar**" ist für den **allgemeinen Fall** richtig und dort gemessen (c2a §1.1c: ein
> naives `forbidden` meldet die indirekte Kette `services → storage → internal`). Für das
> **Testrepo** gilt er **nicht**: die Kette ist dort **nicht realisiert**.
> `src/depot/core/adapters/storage.py` importiert ausschließlich `depot.core.ports`, die
> beiden Importe auf das Internum liegen in der **Fassade** `core/adapters/__init__.py`
> (gemessen, `c2b_bericht_k4_konfiguration.md` §B5 (g), mit abgedruckter Importliste).
>
> **Am Testrepo hielten beide Contract-Typen auf clean und beide meldeten die Injektion**
> (ebd., Vier-Fall-Tabelle: naives `forbidden` auf der gebauten Baseline **KEPT**, Exit 0;
> `protected` gegen die `PROTECTED_MODULE`-Injektion **BROKEN**, naives `forbidden` gegen
> dieselbe Injektion ebenfalls **BROKEN**).
>
> **`protected` bleibt die Wahl.** Zwei Gründe, beide unabhängig: die Zelle ist **an den Typ
> vorregistriert**, und die Falle ist **real** — sie schlägt zu, sobald die Kette entsteht,
> gemessen mit drei Befunden auf der sauberen Baseline in Negativ-2 (ebd.). Eine Fassade, die
> ein zweites Inhaltsmodul bekommt, brächte sie zurück. Ein stillschweigender Wechsel zu
> `forbidden` ist damit ausgeschlossen.
>
> **Was sich ändert, ist allein der Status der Annotation.** ᴾ beschreibt **am
> Messgegenstand** eine Lage, die dort **nicht vorliegt**. Der Punkt wird deshalb als
> **DEKLARIERTE GRENZE** geführt und nicht als Befund: *der allgemeine Kettenfall, an dem die
> Typwahl hängt, wird im Testrepo nicht durchgemessen; die Typwahl ist dort nicht tragend.*
> In Kapitel 4 ist die Zelle entsprechend zu lesen — als Aussage über den **Contract-Typ**,
> nicht als am Testrepo erhobener Unterschied zwischen beiden Typen. Die **Parallelstelle ist
> bereits nachgezogen**: `planung/c1_komponentenschnitt.md` **Rev. 3** §3.1 (4) und §6.1
> („Die Wahl bleibt vorregistriert, ist am Testrepo aber nicht tragend"). Die Baseline wird
> dafür **nicht neu gebaut** — ein weiterer Commit über `B` erforderte ein neues Tag, einen
> neuen `--base`-SHA und die Wiederholung aller 4b-Prüfungen; Aufwand ohne Ertrag für die
> Kampagne (ebd.).
>
> **(2) DIE BELEGQUELLE DER ZEILE `FRAMEWORK_TYPE_IN_SIGNATURE` IST AUFGESPALTEN.** Bis
> Rev. 20 stand dort **eine** Angabe für **zwei** Zellen. Die beiden Zellen waren aber
> **ungleich belegt**, und die Unterscheidung Belegt/Abgeleitet trägt in dieser Arbeit
> überall — gerade in einer Zeile, die soeben **in Richtung der Hypothese** bewegt worden ist
> (Fußnote 4). Ab hier steht je Zelle, worauf sie ruht:
>
> | Zelle | Status | Fundstelle |
> |---|---|---|
> | `FRAMEWORK_TYPE_IN_SIGNATURE` / **K4** | **gemessen** | `c2b_bericht_k4_konfiguration.md` §B6 — acht Findings auf der **sauberen** Baseline (vier Träger, vier Zwillinge), wörtliche Ausgabe abgedruckt |
> | `FRAMEWORK_TYPE_IN_SIGNATURE` / **K5** | ~~abgeleitet~~ → **gemessen** | ~~B9+ F1 (`converter.py:78,89`: nur `ast.Import`/`ast.ImportFrom`)~~ → `c2c_bericht_k5_konfiguration.md` §B6 |
>
> **Zum Zeitpunkt von Rev. 20 war die K5-Zelle abgeleitet**, nicht gemessen: aus B9+ F1
> zusammen mit `converter.py:78,89` (der Parser wertet ausschließlich `ast.Import` und
> `ast.ImportFrom` aus) folgte, dass K5 die Signaturebene nicht erreicht — eine **korrekte,
> aber nicht am Messgegenstand geprüfte** Schlussfolgerung, in derselben Lage wie Fußnote 4
> vor ihrer Korrektur („nicht falsch gemessen, sondern falsch übertragen").
>
> **Mit C2c ist sie gemessen.** Die K5-Sonde — eine **Wegwerf**-Regel unter einem Objekt mit
> `exclude_external_libraries = False`, ausdrücklich **nicht** in die Konfiguration
> aufgenommen — meldet auf der **sauberen** Baseline **acht Module**: dieselben vier Träger
> und vier Zwillinge wie K4, mit wörtlicher Ausgabe. **Vor und nach der Injektion ist die
> Befundmenge identisch**, weil die Injektion die Importmenge nicht antastet
> (`c2c_bericht_k5_konfiguration.md` §B6). Damit ist auch für K5 belegt, was Fußnote 4 sagt:
> **keine verminderte Precision, sondern gar keine Messung.** Beide Zellen der Zeile ruhen
> jetzt auf einer Messung am Messgegenstand, nicht auf einer Übertragung.

> **Nachtrag (23.08.2026, Rev. 22) — B39 IST ENTSCHIEDEN: ZWEI MATRIXZELLEN BEWEGEN SICH.**
> Begründung: `c2c_bericht_k5_konfiguration.md` §B5 (zehn Baseline-Kopien, je eine Injektion, je
> ein vollständiger K5-Lauf, Ausgabe wörtlich). **Der Alttext oben bleibt stehen**; die alten
> Zellwerte stehen **gestrichen sichtbar** in der Matrix.
>
> | Zelle | vorher | nachher |
> |---|---|---|
> | `CYCLE_SIBLING` / **K5** | ~~nein~~ | **teilweise⁷** |
> | `CYCLE_PARENT_CHILD` / **K5** | ~~nein~~ | **teilweise⁷** |
>
> **Die vollständige Begründung steht in der neuen Fußnote 7** — sie hat die Form von Fußnote 5
> („richtige Stelle, falsche Art") und führt: den gemessenen Befund, die Unwählbarkeit der Ursache
> (einseitige Whitelist, DDR M.2 Festlegung 4), die beiden **erwogenen und verworfenen**
> Alternativen (`expected_co_findings` und „ja"), die Buchung in `strict` und `localized`
> **ohne neue Regel**, und die **offengelegte Richtung**.
>
> **Was sich NICHT bewegt.** Die **K4-Zellen** dieser beiden Zeilen (`ja` bzw. `nein`) sind
> unberührt. Die **K2/K3-Zellen** bleiben `nein²` — konstruktionsbedingt, §9. **B9+ F5 bleibt
> richtig:** PyTestArch hat keine Zyklenregel; genau deshalb heißt die Zelle „teilweise" und
> nicht „ja". Die **K5-Konfiguration wird nicht geändert** — sie ist korrekt aus der Whitelist
> abgeleitet, und eine Abschwächung wäre eine andere Zielarchitektur (§1 Rev. 13).
>
> **Warum vor C3 und nicht nach der Messung.** Ohne Entscheidung fiele der Befund unter „falsche
> Regel, richtige Stelle" (§4) und zählte in `strict` als **FP *und* FN** — für **vier**
> Injektionen, auf Grundlage einer Regel, die nach Sichtung der Daten entstanden wäre. Das ist
> die einzige der drei Möglichkeiten, die nicht gewählt, sondern **versäumt** wäre.

¹ Nur mit zusätzlichen `forbidden`-Contracts; `layers` allein ist relaxiert und erlaubt
Schichtsprünge. Für n Schichten sind n−2 Zusatz-Contracts nötig. **Die Kategorie misst
Konfigurationsaufwand (UF4), nicht Erkennungsfähigkeit (UF3)** — K4 wird fair konfiguriert,
also mit den Zusatz-Contracts, und der Aufwand wird berichtet.

² **Konstruktionsbedingt, nicht Modellschwäche.** Der LLM-Pfad prüft pro geänderter Datei
und sieht den Importgraphen nicht; ein Zyklus benötigt Kanten in mehreren Dateien. Siehe
„Verworfen — Importgraph im Prompt" (§9).

³ Die Rule-Engine emittiert ausschließlich `DERIVED:forbidden-edge` und `DERIVED:cycle`;
eine erforderliche Abhängigkeit kann sie nicht ausdrücken.

⁴ ~~**False Positive, keine Nullzeile.** Beide Werkzeuge erreichen die Signaturebene nicht und
melden bei identischer Importmenge auch das konforme Zwillingsmodul. Das ist ein messbarer
Precision-Effekt.~~ **Ersetzt mit Rev. 20:** Beide Werkzeuge werten ausschließlich Importkanten
aus (B9+ Frage 1; `converter.py:78,89`; import-linter über grimp). Die Injektion hebt den
Persistenztyp in eine öffentliche Signatur und lässt die Importmenge unverändert; vor und nach
der Injektion sehen K4 und K5 dasselbe. Das ist keine verminderte Precision, sondern **gar keine
Messung**. Ein Contract bzw. eine Regel, die den Import verbietet, widerspricht
R-FRAMEWORK-1, das den Import ausdrücklich erlaubt (§3 Amendment (d)); K4/K5 würden damit eine
andere Zielarchitektur ausdrücken und gegen den Grundsatz aus §1 Rev. 13 verstoßen. Die
Konfigurationssonde ergab außerdem auf der **sauberen Baseline acht Findings** — vier Träger und
vier Zwillinge, wörtliche Ausgabe in `c2b_bericht_k4_konfiguration.md` §B6 —, während C3 über
alle fünf Konfigurationen 0 Findings fordert. Fußnote 4 war daher **nicht falsch gemessen,
sondern falsch übertragen**: B9+ F1 hat das Contract-Verhalten richtig gemessen, konnte aber
nicht prüfen, ob der Contract in einer C3-tauglichen Konfiguration überhaupt stehen kann.

> **Nachtrag (23.08.2026, Rev. 23) — die Wendung „über alle fünf Konfigurationen 0 Findings" ist
> zu PRÄZISIEREN; der Alttext oben bleibt stehen.** Begründung:
> `c3a_bericht_clean_state_audit.md` §0; §5 Nachträge Rev. 16 und Rev. 18; §6 Nachtrag Rev. 23.
>
> **Richtig ist:** das 0-Findings-Kriterium ist ein **hartes Gate für K1, K4 und K5** — die
> deterministischen und statischen Konfigurationen, deren Ausgabe auf einem gegebenen Baum
> reproduzierbar dieselbe ist. Für **K2/K3** ist der Lauf über die saubere Baseline **keine
> Bestehensprüfung, sondern die Messung der Falsch-Positiv-Rate**; ein 0-Findings-Kriterium wäre
> dort durch die **eigene Vorregistrierung ausgeschlossen**, denn §5 sagt für die Adapterfassade
> (Rev. 16) und für die beiden Portregeln auf `orders_services` (Rev. 18) je eine Meldung
> **vorher** an.
>
> **Die Beweislast der Fußnote bleibt unberührt.** Sie trägt gegen einen **K4-Contract**, und für
> K4 gilt das Gate unverändert: acht Findings auf der sauberen Baseline sind acht Findings zu
> viel. Präzisiert wird die Reichweite des Satzes, nicht sein Schluss.

Die Änderung macht eine **Baseline schlechter** und die LLM-Konfigurationen relativ besser;
sie liegt damit in Richtung der Hypothese. Sie ist allein zulässig, weil sie durch die Messung
**erzwungen** und über die wörtliche Ausgabe reproduzierbar ist, nicht weil sie gewählt wurde.

⁵ import-linter findet das verschobene Modul über `layers` mit `exhaustive = True`, aber
**namensblind** — als nicht deklariertes Kind, nicht als Namensverstoß. Das ist der Fall
„richtige Stelle, falsche Art" und zählt in `localized` anders als in `strict`.
**Ergänzt 12.08.2026 (Amendment (g)):** die Zelle gilt nur, wenn die `layers`-Liste des
`exhaustive`-Contracts **aus dem Dateibaum** erzeugt wird. Stammte sie aus der Soll-Modulliste,
wäre der Zielort seit Option B (§2) deklariert, der Contract liefe **KEPT** durch und die Zelle
wäre unerfüllbar.

⁶ Nur als Import-Proxy und nur, sofern das Modul überhaupt Importkanten hat; ein falsch
platziertes Modul ohne Importe bleibt in K5 unsichtbar. **Ergänzt 12.08.2026 (Amendment (e)):**
genau das ist als Bauvorschrift festgelegt — das verschobene Modul hat keine ausgehenden
Importe und wird von niemandem importiert. Hätte es Importkanten, wäre die Zelle „teilweise"
und diese Vorhersage falsch.

⁷ **„Richtige Stelle, falsche Art" auf der K5-Seite** — gemessen mit C2c, entschieden als **B39**
(Rev. 22). Die Form ist die der Fußnote 5, die Sache ist eine andere: dort findet K4 den Ort und
verfehlt die **Art**, hier findet K5 die Kante und verfehlt die **Kategorie**.

**Was gemessen ist.** K5 meldet **beide** Injektionen, aber **NICHT als Zyklus**: PyTestArch hat
**keine Zyklenregel** — die Zeichenfolge `cycl` kommt im Paket nicht vor (B9+ F5, **unverändert
richtig**). Gemeldet wird die injizierte **Rückkante** als **nicht gelistete Kante der
Erlaubnisliste**, je `1 failed, 23 passed`, Exit 1
(`c2c_bericht_k5_konfiguration.md` §B5, wörtliche Ausgabe):
`"depot.orders.mappers.order_mapper" imports "depot.orders.api.routes"` und
~~`"depot.orders.services.pricing.engine" imports "depot.orders.services.order_service"`.~~
**Korrektur 25.08.2026 — siehe Nachtrag am Ende dieses Abschnitts:** die zweite Zeile stammt aus
der C2c-Prüfsonde gegen zehn Baseline-Kopien mit je einer nachgebauten Injektion, nicht aus der
I16-Injektion dieses Testrepositoriums, die zum Zeitpunkt jener Messung noch nicht existierte.

**Die Ursache ist nicht wählbar.** Die Whitelist ist **einseitig** (Decision Record M.2,
Festlegung 4): `<k>_mappers → <k>_api` und `orders_services_pricing → orders_services` sind dort
ausdrücklich als **abwesend** geführt, *weil* dort injiziert wird
(`c1_komponentenschnitt.md` §4.1/§4.4). Eine aus dieser Whitelist abgeleitete Erlaubnisliste
**MUSS** die Rückkante melden. Die Kante aufzunehmen hieße, eine **andere Zielarchitektur**
auszudrücken (§1 Rev. 13) — und zerstörte nebenbei den Nachweis für `LAYER_BACK_CALL` und
`LAYER_SKIP_CALL`. **Die K5-Konfiguration wird NICHT geändert.**

**Beide Alternativen sind erwogen und verworfen.** **(i) `expected_co_findings`** setzt einen
**Treffer** voraus, den die Begleitmeldung *begleitet* — bei K1 ist das der `cycle`-Record (§4,
Amendment 13.08. (a)), bei K5 gibt es **keinen**. Die Meldung dort zu parken zählte **vier**
Injektionen als „nichts" und untertriebe K5 systematisch. **(ii) „ja"** behauptete
**Zyklenerkennung**, die B9+ F5 widerlegt: dieselbe Regel feuert bei **jeder** nicht gelisteten
Kante, auch ohne Gegenkante — sie erkennt keinen Zyklus, sie erkennt eine verbotene Kante.

**Buchung in den Metriken, OHNE neue Regel.** In **`strict`** kein Treffer: das
**Kategoriesegment** des `match_key` weicht ab. In **`localized`** Treffer auf der **Stelle** bei
abweichender Kategorie — also die **bestehende** Klasse **„richtige Stelle, falsche Kategorie"**
(§4, Amendment 13.08. (f)). Genau der Fall, für den Decision Record O `localized` eingeführt hat;
es wird keine Klasse erfunden, sondern eine vorhandene angewandt.

**RICHTUNG OFFENGELEGT.** Die Änderung macht eine **Baseline BESSER** und liegt damit **GEGEN**
die Hypothese. Zulässig ist sie allein, weil die Messung sie **erzwingt** und die Ausgabe wörtlich
reproduzierbar ist. Bei **Rev. 20** lag die Richtung **umgekehrt** — dort wurden die Baselines
schlechter und die LLM-Konfigurationen relativ besser (Fußnote 4). **Die Symmetrie ist der Beleg**,
dass beide Änderungen der **Messung** folgen und nicht der These.

**Gemessen und abgeleitet.** Die Spalte „Belegquelle" kennzeichnet, welche K4/K5-Zellen
**gemessen** sind (B9+, versionsgebunden auf import-linter 2.13 und PyTestArch 4.0.1) und
welche **abgeleitet** sind. `SIGNATURE_DEVIATION` ist die einzige nicht gemessene Zeile.

**Die K2/K3-Nullzeilen bei `CYCLE` sind konstruktionsbedingt**, weil der LLM-Pfad pro Datei
prüft und den Importgraphen nicht sieht.

Abweichung der Messung von dieser Matrix ist ein Befund, kein Anlass zum Nachjustieren.

> **Amendment (11.08.2026) — Begründung: B36a.** Die Vorhersagen dieser Matrix gelten für
> `localized` (§4). Für `strict` besteht **keine** Vorhersage; eine nachträglich formulierte
> wäre nach Sichtung der Daten entstanden und damit keine. Die Matrix selbst bleibt unverändert.

> **Nachtrag (14.08.2026, Rev. 17) — SINGULAR-REGEL FÜR INJEKTIONEN.** Begründung:
> `4b4_bericht_baseline_billing.md` §2 (gemessene Beinahe-Unbestimmtheit bei I20).
>
> **Regel:** Jede Injektion benennt im Manifest die betroffene **Methode oder Signatur
> NAMENTLICH** — auch dort, wo der `match_key` sie nicht führt.
>
> **Anlass, gemessen und nicht konstruiert.** Der erste Entwurf von
> `depot.billing.services.ledger_service` führte `depot.core.ports.Clock` in **zwei**
> öffentlichen Signaturen (`post_invoice` und `post_settlement`). Die Reservierungsregel aus
> Rev. 16 (A) wäre formal eingehalten gewesen — die **Modulzahl** bleibt 1 —, aber das Rezept zu
> I20 entfernt „**die** Port-Annotation" im **Singular**: bei zwei Vorkommen ist nicht bestimmt,
> ob die Injektion eines oder beide trifft. Der Bau hat das korrigiert (`post_settlement` nimmt
> jetzt das Wertstellungsdatum als `day: str`), aber die **Regel** fehlte, die den Fall
> allgemein ausschließt. Sie steht hiermit.
>
> **Betroffen sind zwei Szenarien, aus unterschiedlichem Grund:**
>
> - **`FORBIDDEN_SIGNATURE_TYPE` (I21–I24).** Der `match_key` hängt **nicht** daran —
>   `offending_type` trägt nach Decision Record L/P den **Framework-Typnamen**, der bei zwei
>   Fundstellen derselbe wäre. Die **Reproduzierbarkeit** hängt sehr wohl daran: ohne
>   Signaturnennung ist der Injektionscommit aus dem Manifest nicht eindeutig rekonstruierbar.
> - **`SIGNATURE_DEVIATION` (I29–I32).** Hier hängt der **Schlüssel selbst** daran: nach
>   Decision Record L/P trägt `offending_type` bei `API_CONTRACT` den **Symbolnamen der
>   abweichenden Funktion**. Ohne namentliche Festlegung ist `expected_match_key` nicht
>   berechenbar.
>
> **Für I17–I20 und I29–I32 ist die Signatur bereits wörtlich festgelegt** — durch die
> Bauberichte (`4b2…` §5, `4b3…` §4, `4b4…` §3), die die betroffenen Signaturen im Wortlaut
> abdrucken. Die Regel schreibt nichts um; sie hebt die dort schon getroffene Festlegung auf
> **Manifestebene** und macht sie für **alle** Injektionen verbindlich, statt sie von der
> Sorgfalt des jeweiligen Bauauftrags abhängen zu lassen.

> **Nachtrag (24.08.2026, Rev. 27) — WAS DER K2-KONTROLLLAUF ÜBER DIE FINDINGS ZEIGT, REIN
> DESKRIPTIV.** Begründung: `c3b_k2_nachtrag_findingbezug.md` Teil A/B; `c3b_k2_bericht_kontrolllauf.md`
> §4.
>
> Ohne Bewertung der Modellfähigkeit, allein als Beschreibung der 461 LLM-Findings über die drei
> Repetitionen des Kontrolllaufs auf den 52 Kontrollmodulen (49 von 52 Modulen tragen mindestens
> ein Finding):
>
> - **Bezug zum geprüften Modul:** 71,4 % Selbstbezug, 7,8 % Fremdbezug, 2,6 % Zielbezug,
>   18,2 % nicht zuordenbar. Von 152 `offending_type`-Findings referenzieren 135 nachweislich die
>   geprüfte Datei (81 in Imports/Signaturen, 54 im Modulpfad-Kopf); **17 nennen etwas, das im
>   gerenderten Prompt an keiner Stelle vorkommt.**
> - **`R-CORE-1` erzeugt 153 der 461 Findings:** auf den drei reinen `core`-Dateien meldet das
>   Modell in jedem Lauf exakt eine Kante zu jeder der 16 möglichen Zielkomponenten außerhalb
>   des Kerns — vollständig und über alle drei Repetitionen identisch.
> - **9 Fälle melden `sqlalchemy.orm.Session`** auf Dateien, deren gerenderter Prompt
>   `sqlalchemy` an keiner Stelle enthält.
> - Die beiden vorregistrierten Meldungen (§5 Nachtrag Rev. 16: Fassade `R-PROTECT-1`, 3 von 3
>   Läufen; §5 Nachtrag Rev. 18: Nicht-Träger-Portregel auf `orders_services`, 1 von 3 Läufen)
>   werden im unabhängigen Prompt-Abgleich **erneut gefunden** — derselbe Befund aus zwei
>   Richtungen.
> - **Methodisch:** der zur Prüfung neu gerenderte Prompt reproduziert alle 156 archivierten
>   `prompt_hash` bitgenau; der Abgleich lief damit gegen das, was das Modell tatsächlich sah.
> - **51 von 52 Modulen liefern in allen drei Repetitionen dieselbe Findingmenge**;
>   `depot.orders.services` ist die einzige Ausnahme — die K2-Seite dessen, was
>   `b36a_bericht_k3_varianzlauf.md` für K3 gemessen hat, für K2 bisher nirgends festgehalten.
>
> Interpretation dieser Beobachtungen — insbesondere die Frage, was Selbst-/Fremdbezug und die
> identische `R-CORE-1`-Meldung über die Erkennungsleistung aussagen — gehört nach Kapitel 7,
> nicht hierher.

> **Nachtrag (25.08.2026, Rev. 28) — I16-ZIELKANTE KLARGESTELLT.** Begründung: Abgleich der in
> Fußnote 7 zitierten K5-Ausgabe mit ihrer tatsächlichen Quelle.
>
> Die dort als gemessene K5-Ausgabe zu I16 zitierte Zeile
> `"depot.orders.services.pricing.engine" imports "depot.orders.services.order_service"` stammt
> aus der **C2c-Prüfsonde**, die gegen **zehn Baseline-Kopien mit je einer nachgebauten
> Injektion** lief (`c2c_bericht_k5_konfiguration.md` §B5) — **nicht** gegen die I16-Injektion
> dieses Testrepositoriums, die zum Zeitpunkt jener Messung noch nicht existierte. Der alte
> Wortlaut bleibt oben **gestrichen stehen**, statt gelöscht zu werden.
>
> **Verbindlich für C4b:** I16 ergänzt in `src/depot/orders/services/pricing/engine.py` den
> Import des **Paketmoduls** `depot.orders.services`, nicht eines Submoduls darin.
>
> **Begründung.** Die Kategorie `CYCLE_PARENT_CHILD` prüft den Blindfleck von
> `acyclic_siblings` bei **Paket UND eigenem Untermodul** (Decision Record P). Ein Import auf
> `order_service` wäre auf **Modulebene** eine Kante zwischen zwei Cousins — keiner ist Vorfahre
> des anderen —, und die Eltern/Kind-Eigenschaft bestünde nur noch auf **Komponentenebene**; die
> Kategorie verlöre ihren Gegenstand. Auf den `match_key` wirkt die Wahl **nicht**:
> `location.module` ist in beiden Fällen `…pricing.engine`, `subject` in beiden Fällen
> `orders_services_pricing -> orders_services`. Unterschiedlich ist allein der **Meldetext von
> K5**.
>
> **Zusatz.** Der I16-Commit erzeugt einen echten **Laufzeit-Zirkelimport**
> (`c1_modulliste.md` §D.6). Für die statische Messung folgenlos; der Commit darf **keinem**
> Laufzeit-Smoke-Test unterworfen werden, er würde erwartungsgemäß brechen. `python -m
> compileall` bleibt anwendbar.

> **Nachtrag (25.08.2026, Rev. 28) — TYPWAHL FÜR I21–I24 (`FORBIDDEN_SIGNATURE_TYPE`)
> FESTGELEGT.** Begründung: §6 des Injektionsmanifests führte den Typ und die tragende Methode
> als offen; die Methode bleibt bis C4b offen, der Typ ist hiermit entschieden.
>
> Injiziert wird **`sqlalchemy.orm.Session`** als Annotation eines Parameters oder des
> Rückgabewerts einer **öffentlichen** Methode der Trägerklasse. `Session` ist der kanonische
> Typ des Namensraums und wird im `statement` von R-FRAMEWORK-1 selbst als Beispiel genannt; eine
> Persistenz-Session in der Signatur eines Modells ist der fachlich einleuchtendste Verstoß.
> `Mapped` wäre ungeeignet, weil es in Klassenattributen **erlaubt** vorkommt — genau der
> Kontrast, auf dem die Zwillingskonstruktion ruht.
>
> **Drei Auflagen, die C4b einzuhalten hat:**
>
> - **(a)** die Methode ist öffentlich und wird vom Extractor erfasst (Top-Level-Def oder
>   Klassenmethode, `b1_bericht_matchkey.md` C4);
> - **(b)** es entsteht **kein** neuer Import — `sqlalchemy.orm` ist in allen vier Trägern
>   bereits importiert, und die Importmenge muss identisch zu der des Zwillings bleiben;
> - **(c)** es bricht **kein** Aufrufer, sonst wäre der Diff größer als eine Datei.
>
> Genau **ein** Vorkommen je Träger (Singular-Regel, §3 Nachtrag Rev. 17). Der Zwilling bleibt
> unberührt. `offending_type` im Manifest ist die Schreibweise, die im Code steht — von C4b
> wörtlich zu melden und von C4c ins Manifest zu übernehmen.

> **Nachtrag (25.08.2026, Rev. 29) — KLARSTELLUNG ZU DEN ZYKLEN DER
> `LAYER_BACK_CALL`-INJEKTIONEN.** Begründung: `repo-kontext/c4b_bericht_injektionen.md` §8.5
> (gemessen am gebauten Datensatz, ohne Werkzeuglauf der Kampagne).
>
> **Gemessen.** Die drei `LAYER_BACK_CALL`-Injektionen **I01–I03** tragen je **einen**
> Komponentenzyklus `<k>_repository ↔ <k>_services` — auf Modul- wie auf Komponentenebene ein
> Zweierzyklus. Die übrigen Nicht-`CYCLE`-Injektionen (I04–I12, I17–I32) tragen **je 0**.
>
> **Er ist KONSTRUKTIONSNOTWENDIG, nicht ein Baufehler.** Die Spine-Kante
> `<k>_services → <k>_repository` steht in der Whitelist (Komponentenschnitt §4) und ist in der
> Clean-Baseline realisiert; `LAYER_BACK_CALL` injiziert definitionsgemäß die **Gegenrichtung**.
> Ihn zu vermeiden hieße, entweder die Spine-Kante zu entfernen — sie ist Rückgrat des Modells —
> oder dem Szenario seinen Gegenstand zu nehmen. Es gibt keine dritte Möglichkeit.
>
> **Er ist bereits vorregistriert — als K4-Doppelmeldung.** Komponentenschnitt §6.2 und §4
> Amendment 13.08. führen ihn: der einzige `acyclic_siblings`-Contract meldet **denselben**
> Verstoß ein **zweites Mal** als Geschwisterzyklus `services ↔ repository`. Manifest §5.1 nennt
> das ausdrücklich **„kein False Positive, getrennt zu führen"**. Diese Buchung gilt unverändert;
> der Nachtrag stellt nur klar, dass die Zahl gemessen und erwartet ist, nicht ein Nebeneffekt.
>
> **AUSDRÜCKLICH: auf K1 wirkt der Zyklus NICHT.** `FORBIDDEN_RELATION` läuft nach §6
> (Graphmodus je Kategorie) in **`--rule-graph diff`**, und dort ist eine `cycle`-Begleitmeldung
> **strukturell unmöglich**: ein Ein-Datei-Diff erzeugt genau **einen** Adjazenz-Knoten, alle
> beobachteten Komponentenkanten tragen dieselbe Quellkomponente, die DFS besucht einen Knoten,
> und `childState === VISITING` kann **nie** eintreten (Decision Record M.2 Festlegung 2, bewiesen;
> §6 Amendment 13.08.). `expected_co_findings` bleibt für alle zwölf
> `FORBIDDEN_RELATION`-Injektionen **konstruktionsbedingt leer** — I01–I03 eingeschlossen.
>
> **Z1 und Z3 sind unberührt.** Beide Bauvorschriften gelten laut §3 **nur für die
> `CYCLE`-Injektionen** (I13–I16); dort sind sie erfüllt (`c4b_bericht_injektionen.md` §8.5).
> Der Zyklus von I01–I03 ist kein `CYCLE`-Injektionsziel und wird in keiner `CYCLE`-Zeile der
> Erwartungsmatrix mitgezählt. **Keine Matrixzelle bewegt sich.**

---

## 4. Matching-Regel (TP/FP/FN)

> **Geändert vor Freeze (Rev. 2, 18.07.):** Match-Ebene von „`rule_id` + Datei" auf den
> **erwarteten `match_key` aus dem Manifest** umgestellt. Begründung: (a) Der implementierte
> Checker sieht diesen Schlüssel als designierten Eval-Join vor (`matchKey.ts`-Docstring:
> exakter Join ohne Fuzzy-Matching); (b) die Rule-Engine emittiert für die Szenarien
> `LAYER_BACK_CALL`, `LAYER_SKIP_CALL`, `PROTECTED_MODULE` und `INDEPENDENCE` unter
> `FORBIDDEN_RELATION` einheitlich
> `DERIVED:forbidden-edge` — eine `rule_id`-basierte Kategorien-Attribution wäre nicht
> unterscheidbar, die Kategorie kommt stattdessen aus dem Manifest; (c) der `match_key` ist
> präziser als Datei-Ebene (zwei Injektionen in derselben Datei bleiben unterscheidbar).

- **Match-Ebene:** exakter String-Vergleich Finding-`match_key` ↔ Manifest-`expected_match_key`.
  Die Kategorien-Zuordnung eines Treffers kommt aus dem Manifest-Eintrag, nicht aus der
  `rule_id` des Findings. Zeilennummern werden geloggt, sind aber nicht match-relevant
  (LLM-Zeilenangaben sind unzuverlässig; das wäre ein eigener Befund, kein Match-Kriterium).
- **TP:** Finding, dessen `match_key` mit einem `expected_match_key` des Manifests
  übereinstimmt. Mehrere Findings auf derselben Injektion (Dedup über `match_key`) = **1** TP.
- **Zyklen (`CYCLE`):** gemeldeter Zyklus zählt als TP, wenn er die injizierte Kante enthält
  (Zyklus-Mengen können je Tool unterschiedlich geschnitten sein; der `expected_match_key`
  einer `CYCLE`-Injektion referenziert die injizierte Rückkante).
- **Baselines (K4/K5):** import-linter/PyTestArch kennen den `match_key` nicht; ihre Findings
  werden von der Eval-Harness deterministisch auf das Schlüsselschema abgebildet
  (Kante/Modul aus dem Tool-Report → `category|component|module|from->to`). Die
  Abbildungsregeln werden vor der Messung im Harness-Code fixiert und im Manifest referenziert.
- **FP:** Finding ohne Manifest-Match, das nicht auf der Known-Deviations-Liste steht.
- **FN:** Manifest-Eintrag ohne passendes Finding.
- **`FORBIDDEN_SIGNATURE_TYPE`, `STRUCTURAL_PLACEMENT`, `API_CONTRACT` und
  `ABSENCE_REQUIRED`:** TP nur bei vollem Schlüssel-Match — d. h. das LLM muss
  die **richtige Kategorie** und den **richtigen `offending_type`** benennen, nicht bloß
  „hier stimmt etwas nicht" an der richtigen Stelle. Kein Partial Credit.
- **Falsche Regel/Kategorie, richtige Stelle:** `match_key` matcht nicht (Kategorie ist
  Schlüsselbestandteil) → zählt als FP *und* FN (die injizierte Verletzung wurde nicht
  erkannt; zusätzlich wurde etwas behauptet, das nicht injiziert ist). Solche Fälle werden
  einzeln im Anhang gelistet — sie sind qualitativ interessant (Fähigkeitsprofil des
  LLM-Pfads, UF3/UF4).
- **Ambige Fälle:** einzeln dokumentieren, Entscheidung nach dieser Regel-Liste; reicht die
  Liste nicht, wird der Fall konservativ (gegen das LLM-Tool) gewertet und als Grenzfall
  ausgewiesen. Keine Ad-hoc-Regeln zugunsten des eigenen Tools.

> **Amendment (11.08.2026) — Begründung: B36a.** Ergänzt um eine zweite, ebenfalls
> vorregistrierte Metrik auf Lokalisationsebene (Decision Record O,
> `docs/ddr/checker_entscheidungen_o.md`). Der vorstehende Text zur exakten Regel bleibt
> **unverändert** in Kraft — die Ergänzung tritt daneben und ersetzt nichts. Beide Metriken
> werden berichtet.

**`strict` — exakte Übereinstimmung:** exakter String-Vergleich `match_key` gegen
`expected_match_key`, kein Partial Credit, **keine** Deduplizierung. Von mehreren Findings
zählt das mit passendem Schlüssel als TP, jedes weitere als FP. Unverändert wie bisher
vorregistriert.

**`localized` — Lokalisationsübereinstimmung:** ein injizierter Verstoß gilt als erkannt, wenn
mindestens ein Finding im erwarteten Modul der erwarteten Komponente liegt **und** die für diese
Konfiguration erwartete Kategorie trägt. Der `subjectKey` wird nicht verglichen, aber weiter
archiviert und qualitativ ausgewertet. Deduplizierung: mehrere Findings auf dasselbe
`(component, module, category)` zählen als **ein** TP und erzeugen **keine** FP. Ein Finding im
erwarteten Modul mit anderer Kategorie ist kein TP; es wird als eigene Klasse gezählt und im
Anhang gelistet — das ist die oben bereits vorgesehene Liste „falsche Regel, richtige Stelle".

**Die erwartete Kategorie ist pfadabhängig.** Die Rule-Engine kennt nur `layer-violation` und
`cycle` (`ruleEngine.ts:77`, `:132`); die vier `FORBIDDEN_RELATION`-Szenarien
`LAYER_BACK_CALL`, `LAYER_SKIP_CALL`, `PROTECTED_MODULE` und `INDEPENDENCE` tragen dort alle
`layer-violation`, und
`rule_id` diskriminiert nicht (einheitlich `DERIVED:forbidden-edge`). Im LLM-Pfad stammt
`category` aus `rule.category` der Regeldatei (`llmChecker.ts:288`). Das Manifest führt die
erwartete Kategorie je Pfadtyp (deterministisch / LLM / Baseline).

> **Amendment (12.08.2026) — Begründung: Decision Records M und P. Schließt B28.**
>
> **`CYCLE` auf dem Pfad K1 — exakter Vergleich.** Der Record trägt genau **eine** Kante
> (`subject = {from, to}`, `ruleEngine.ts:129`). `strict` ist ein Treffer, wenn der `match_key`
> dem im Manifest **handabgeleiteten** Kandidatenschlüssel entspricht; unter Z1–Z3 (§3) ist die
> Kandidatenmenge **einelementig**. Ein Sonderfall für `localized` ist damit **nicht**
> erforderlich: `CYCLE` wird auf Modulebene gejoint wie alle übrigen Kategorien.
>
> **`CYCLE` auf dem Pfad K4 — Mengenregel.** `acyclic_siblings` gibt eine **minimale Menge zu
> entfernender Kanten** aus, keine Zyklenpfade (B9+ §6). Treffer, wenn die genannte Kantenmenge
> die **injizierte Kante enthält**; bei einem Zyklus der Länge 2 enthält sie genau eine der
> beiden Kanten. Die beiden Ausgabeformen sind hiermit **getrennt benannt**.
>
> **Damit ist der bisher in §4 bestehende Widerspruch aufgelöst** — der Text oben verlangt
> einen exakten `match_key`-Vergleich und enthält für Zyklen zugleich die Mengenregel „zählt,
> wenn er die injizierte Kante enthält". Beide sind mit dem implementierten Werkzeug nicht
> gleichzeitig ausführbar. Es gilt ab hier: **exakter Vergleich für K1, Mengenregel für K4.**
>
> **`expected_co_findings`.** Für `FORBIDDEN_RELATION` kann K1 zusätzlich zum
> `layer-violation`-Record einen `cycle`-Record erzeugen, wenn die injizierte Kante einen
> Komponentenzyklus schließt: **derselbe Import trägt dann beide Records** mit identischer
> `location` und identischem `subject`, unterschieden nur in `category` und `rule_id`
> (`c1b_bericht_komponentenschnitt.md`, Abschnitt 1c, ausgeführt: `count = 2`). Solche
> Begleitmeldungen werden **vorregistriert**, **getrennt geführt** und zählen **nicht als False
> Positive**. Im Messpfad treten sie nicht auf (siehe §6, Graphmodus je Kategorie), sondern nur
> im deskriptiven Vollbild-Lauf.

> **Amendment (13.08.2026) — Begründung: Decision Record M.2, Festlegungen 2 und 3;
> `c1b_bericht_ruleengine_verifikation.md` Punkte 2, 3, 5 und 7.** Der Absatz
> `expected_co_findings` oben bleibt unverändert stehen; er benennt die Begleitmeldung in der
> **falschen Richtung** und lässt eine Bedingung weg. Beides wird hier korrigiert.
>
> **(a) Die im Messpfad tatsächlich auftretende Begleitmeldung ist die `layer-violation` ZU
> einer `CYCLE`-Injektion**, nicht der `cycle` zu einer `FORBIDDEN_RELATION`-Injektion. Für
> `CYCLE` gilt `--rule-graph full` (§6), die injizierte Kante steht **nicht** in der Whitelist —
> das Soll erklärt keine Rückkante für erlaubt —, `cycleViolations` prüft die Whitelist
> überhaupt nicht (`ruleEngine.ts:91-92`, „Considers all observed edges, allowed or not"), und
> `runRuleEngine` konkateniert beide Ergebnislisten **ohne Kreuzprüfung**
> (`ruleEngine.ts:58`). Die injizierte Kante fällt damit durch **beide** Filter. Gemessen in
> Punkt 2b und 5b: je zwei Records aus **einem** Import.
>
> **(b) Für `FORBIDDEN_RELATION` ist das Feld leer — konstruktionsbedingt, nicht mangels
> Beobachtung.** Für diese Kategorie gilt `--rule-graph diff` (§6) zusammen mit der
> Lauf-Akzeptanzregel `changed_files_count == 1`. Alle beobachteten Importe stammen dann aus
> **einem** Modul, alle Komponentenkanten tragen dieselbe Quellkomponente, die Adjazenz hat
> genau **einen** Knoten, und `childState === VISITING` (`ruleEngine.ts:120`) kann nie
> eintreten. Ein Ein-Datei-Diff kann keinen `cycle`-Record erzeugen — unabhängig davon, was der
> Rest des Repos enthält. Der leere Eintrag wird **mit dieser Begründung** ins Manifest
> geschrieben.
>
> **(c) „identische `location` und identisches `subject`" gilt nur unter Z2.** Die beiden
> Records fallen genau dann zusammen, wenn die nicht gewhitelistete Kante zugleich die vom
> Zyklus gemeldete ist — also wenn ihr **Ziel** in Code-Unit-Ordnung **vor** ihrer Quelle
> sortiert (Bauvorschrift Z2, §3). Gegenbeispiel, gemessen (Punkt 5b): bei `C < P` und
> verbotener Kante `C -> P` liegt die `layer-violation` auf `pkg.audit.trail`
> (`subject C->P`), der `cycle` auf `pkg.audit` (`subject P->C`) — **verschiedene Module,
> verschiedene Komponenten, verschiedenes `subject`**. Z2 gilt deshalb ausdrücklich auch für
> `CYCLE_PARENT_CHILD`, nicht nur für `CYCLE_SIBLING`.
>
> **(d) Fundstellenkorrektur.** `subject = {from, to}` steht bei **`ruleEngine.ts:155`**, nicht
> bei 129; Zeile 129 ist leer.
>
> **(e) Bildungsregel für das Manifest.** Unter Z2 ist der `expected_co_findings`-Eintrag eine
> **Zeichenkettenoperation auf dem handabgeleiteten `expected_match_key`**: Präfix `cycle|`
> durch `layer-violation|` ersetzen, `location` und `subject` unverändert übernehmen,
> `rule_id` auf `DERIVED:forbidden-edge` setzen. Tragfähig ist das, weil `forbiddenEdgeRecord`
> (`ruleEngine.ts:72-73`) und `cycleRecord` (`ruleEngine.ts:153-155`) `location` und `subject`
> mit **identischem Ausdruck** aus derselben Kante bilden. Es ist **kein** Engine-Aufruf; die
> Anti-Tautologie-Regel aus Decision Record M bleibt gewahrt. Die vorregistrierte Vorabprüfung
> vergleicht ab jetzt zusätzlich die **Zahl** der Records je `CYCLE`-Injektion gegen die
> Erwartung **2**; eine Abweichung ist ein Befund und kein Anlass, das Manifest zu ändern.
>
> **(f) Kategorieverwechslung bei K2/K3, hiermit vorregistriert — neu, nicht aus M.2.** Für die
> vier `CYCLE`-Injektionen ist ein `FORBIDDEN_RELATION`-Finding von K2 oder K3 auf dem
> **Trägermodul** eine **vorregistrierte Kategorieverwechslung**. Ursache: dieselbe einseitige
> Whitelist, die (a) erzeugt, macht die injizierte Kante im Prompt-Abschnitt
> `## Allowed dependency edges touching this component` **sichtbar unerlaubt**
> (`b1_bericht_matchkey.md`, Abschnitt C3) — das Modell sieht eine verbotene Kante und meldet
> sie als solche, ohne den Zyklus zu erkennen. Behandlung: **kein Treffer für `CYCLE`** (die
> vorregistrierte Zelle K2/K3 = nein bleibt bestehen und wird nicht nachträglich aufgeweicht),
> **kein False Positive** (die Stelle ist richtig und die gemeldete Kante existiert), und in
> `localized` als **„richtige Stelle, falsche Kategorie"** getrennt zu führen. Der Fall ist
> vorab benannt, damit er in der Auswertung nicht als Ermessensentscheidung erscheint.

> **Amendment (13.08.2026) — Begründung: `c2a_bericht_contract_semantik.md` §2.2c.** Eine
> zweite Begleitmeldung wird vorregistriert, diesmal auf dem Pfad **K4**, und die Form der
> K4-Zyklusmeldung wird präzisiert, weil sie jetzt **gemessen** ist.
>
> **(a) Vorregistrierte K4-Begleitmeldung: die drei `LAYER_BACK_CALL`-Injektionen werden
> von K4 ZWEIFACH gemeldet** — vom `layers`-Contract als **Schichtverletzung** und vom
> `acyclic_siblings`-Contract als **Geschwisterzyklus**. Grund: `repository` und `services`
> sind **Geschwister** unter dem Kontextpaket, die Clean-Kante `services → repository`
> schließt mit der injizierten Rückkante einen **Zyklus**, und `acyclic_siblings` meldet
> Zyklen **auf jeder Ebene bis `depth`** (c2a §2.2c). Es gibt **KEINEN** `ancestor`, der
> `api`/`mappers` einschließt und `services`/`repository` ausschließt — die Meldung ist
> **nicht wegkonfigurierbar**.
>
> **(b) Behandlung analog zur K1-Begleitmeldung** (Amendment 13.08. (a) oben):
> **vorregistriert**, **getrennt geführt**, **KEIN False Positive**. `LAYER_SKIP_CALL`
> (`api → repository`, keine Gegenkante) und `INDEPENDENCE` (Einzelkante zwischen
> Wurzelgeschwistern) erzeugen sie **nicht**.
>
> **(c) Form der K4-Zyklusmeldung, präzisiert.** `acyclic_siblings` gibt eine **minimale
> Entfernungsmenge auf Paketebene** aus, **relativ zum `ancestor` notiert** (führender
> Punkt), **mit Importzähler**, **OHNE Modulnamen** (c2a §2.2a, gemessen:
> `- .mappers -> .api (1 import)`). Und: ein **gebrochener Contract kann MEHRERE
> `No cycles are allowed in …`-Blöcke enthalten**, je Ebene einen — **die K4-Auswertung
> liest eine Liste von Blöcken, nicht einen Block je Contract**. Die Mengenregel für
> `CYCLE` auf dem Pfad K4 (Amendment 12.08.) bleibt unverändert; sie ist ab hier auf den
> **jeweiligen Block** anzuwenden, dessen Kopfzeile das betroffene Paket nennt.

> **Nachtrag (23.08.2026, Rev. 19) — DIE REGELSTATEMENTS BENENNEN DIE ERWARTETE SUBJEKTFORM.
> EINHEITLICH ÜBER ALLE SECHZEHN REGELN.** Begründung: `c2b_bericht_k4_konfiguration.md`
> Teil A. Das ist eine **Eigenschaft des Messinstruments**, hier vorregistriert, damit sie in
> Kapitel 4 als solche benannt und nicht als Modellleistung gelesen wird. **Keine Matrixzelle
> bewegt sich, kein `expected_match_key` ändert sich.**
>
> **Die Festlegung.** Jedes der sechzehn `statement` schließt mit einem Satz, der die im
> Antwortschema erwartete Form des `subject` nennt, in den **Feldnamen des Schemas**
> (`llmClient.ts:200-214`, geprüft in `validate.ts:56-58`):
>
> | Kategorie | Subjektform | Schlusssatz des `statement` |
> |---|---|---|
> | `FORBIDDEN_RELATION`, `CYCLE` | Kantenpaar | „Report the finding as a dependency edge: `subject.from` is the importing component, `subject.to` the imported one." (bei `CYCLE` mit dem Zusatz „— the edge that closes the cycle") |
> | `ABSENCE_REQUIRED` | `offending_type` | „Report `depot.core.ports.<Port>` as `subject.offending_type`, under that exact name." |
> | `FORBIDDEN_SIGNATURE_TYPE` | `offending_type` | „Report the persistence type that appears in the signature as `subject.offending_type`, verbatim as it is written there." |
> | `STRUCTURAL_PLACEMENT` | `offending_type` | „Report the full dotted module path … as `subject.offending_type`." |
> | `API_CONTRACT` | `offending_type` | „Report the symbol `<Class.method>` as `subject.offending_type`." |
>
> Die Zuordnung Kategorie → Subjektform folgt **Decision Record L** und dem Antwortschema, die
> Schreibweisen folgen **§3 Nachtrag Rev. 18**; beides ist hier nur angewandt, nichts davon neu
> entschieden.
>
> **Warum die Anweisung nötig ist.** `subjectKey` ist das **vierte Segment** des `match_key`
> und wird aus `offending_type` **ODER** aus `from->to` gebaut (`matchKey.ts:23-26`). Beide
> Formen sind im Schema zulässig und für dieselbe Beobachtung formulierbar: ein Modell kann
> eine Schichtverletzung als Kantenpaar **oder** als `offending_type` = importiertes Modul
> melden. Wählt es die andere Form als das Manifest, trifft der Schlüssel **nie** — und
> `strict` misst dann die **Formatwahl des Modells**, nicht seine Erkennungsleistung. Die
> Absicherung gegen alles Übrige — Trägerwahl, Kategorienwahl, Mengenfragen — ist unverändert
> `localized` (Decision Record O, §4); die Subjektform ist der eine Freiheitsgrad, den
> `localized` **nicht** auffängt, weil er in **beide** Metriken durchschlägt.
>
> **Warum EINHEITLICH und nicht nur dort, wo es nötig scheint.** Eine ungleiche Belegung
> verzerrte den Vergleich **ZWISCHEN den Kategorien** aus einem Grund, der mit dem Modell
> nichts zu tun hat: die Kategorien mit Formhinweis hätten systematisch höhere
> `strict`-Werte als die ohne, und der kategorienweise Precision/Recall-Ausweis (§5) läse
> sich als Modellbefund, wo er ein Regeltextbefund wäre. Dieselbe Erwägung trägt die
> einheitliche `severity` (c2a §3, Punkt 6).
>
> **Abgrenzung — was die Anweisung NICHT tut.** Sie sagt **nicht**, ob ein Verstoß vorliegt,
> **nicht**, welche Regel verletzt ist, **nicht**, welches Modul der Träger ist, und **nicht**,
> welchen Wert das Feld trägt — außer dort, wo der Wert ohnehin aus der Regel kommen **muss**,
> weil er im Code nicht steht (`ABSENCE_REQUIRED`, Decision Record P, Punkt 3). Sie legt
> ausschließlich das **Feld** fest, in das die Antwort gehört. Das Systemprompt nannte die
> beiden Formen schon vorher (`contextBuilder.ts:57-62`), aber **generisch**, ohne Zuordnung zur
> einzelnen Regel.
>
> **In Kapitel 4 als Konstruktionsbedingung zu benennen**, in derselben Form wie die
> Bauvorschriften ᴱ, ᴳ, ᴴ und der Contract-Typ ᴾ in §3.

> **Nachtrag (23.08.2026, Rev. 25) — RECORDMENGE JE KONFIGURATION. DIE KONFIGURATION IST DER
> MECHANISMUS, NICHT DER AUFRUF.** Begründung: die Aufrufzeilen für K2 und K3 (§6 Nachtrag
> Rev. 24) enthalten `--rule-graph diff`; der **deterministische Pfad läuft also mit**, und seine
> Records landen im **selben** `--run-log` und `--json-out`. Ein K2- oder K3-Lauf erzeugt damit
> die **Vereinigung** aus LLM-Findings und `DERIVED:forbidden-edge` / `DERIVED:cycle`.
>
> **Die Festlegung.** Die Recordmenge einer Konfiguration ist durch den **Mechanismus** bestimmt,
> nicht durch den Aufruf:
>
> - **K1** := Records mit `rule_id`-Präfix `DERIVED:`
> - **K2, K3** := Records mit **jedem anderen** `rule_id`
>
> Der Filter wird **vor** der Berechnung **beider** Metriken angewandt, in der Harness (C6) und im
> Nachlaufskript (§6 Nachtrag Rev. 25). Er wird **nicht** durch eine Änderung am Checker gelöst —
> ein weiterer Eingriff in den eingefrorenen Pfad bewegte `checker_git_head` ein **viertes** Mal,
> ohne Beweiskraft hinzuzufügen.
>
> **Warum beide Metriken getrennt zu begründen sind.**
>
> **`strict` ist ohne Filter unbetroffen.** Die Kategoriesegmente differieren
> (`layer-violation` bzw. `cycle` gegen die sechs Ebene-1-Strings des Manifests); ein
> DERIVED-Record trifft den erwarteten K2/K3-Schlüssel **nie**. Der Filter ändert dort keine Zahl
> und gilt trotzdem, weil die Menge vor beiden Metriken einheitlich zu bilden ist.
>
> **`localized` wäre ohne Filter KONFUNDIERT.** Es trifft auf **Stelle**, nicht auf Kategorie
> (Decision Record O; B39 baut ausdrücklich darauf auf). Ein DERIVED-Record liegt bei **jeder der
> sechzehn strukturellen Injektionen** am richtigen Modul — K2 und K3 bekämen dort einen
> `localized`-Treffer, **auch wenn das Modell nichts gemeldet hat**, und zwar in genau den
> Kategorien, in denen **K1 der Vergleichsmaßstab** ist. Der Vergleich LLM gegen deterministisch
> zerfiele, weil die eine Seite die andere mitzählte.
>
> **Für den Kontrolllauf auf `B` ist die Menge leer** (C3a: K1 mit 0 Findings, §6 Nachtrag
> Rev. 23) — der Filter ist dort **ohne Wirkung**, gilt aber unverändert.

> **Nachtrag (24.08.2026, Rev. 27) — LESEKORREKTUR: `localized` MISST AUF DEM LLM-PFAD DIE
> MELDEQUOTE, NICHT DIE LOKALISATIONSGENAUIGKEIT.** Begründung:
> `c3b_k2_nachtrag_findingbezug.md` Teil A; Decision Record O, Konsequenz 2.
>
> **Gemessen:** `location.module` und `location.component` werden vom Checker **aus dem
> geprüften `ChangedFact`** gesetzt (`llmChecker.ts:282-305`), **nie** aus der Modellantwort —
> das Antwortschema hat für den Ort kein eigenes Feld (`check.ts:24-45`). Ein LLM-Finding kann
> strukturell **nie** an einem anderen Modul landen als dem geprüften.
>
> **Festlegung, als Lesekorrektur — keine Änderung der Metrikdefinition:**
>
> - `localized` misst auf dem LLM-Pfad (K2, K3) die **Meldequote auf der geprüften Datei**,
>   nicht die Lokalisationsgenauigkeit des Modells. Für K1, K4 und K5 gilt das **nicht** — dort
>   wählt das Werkzeug das gemeldete Modul selbst, und ein `localized`-Treffer setzt tatsächlich
>   voraus, dass das Werkzeug die richtige Stelle gefunden hat.
> - **Deshalb darf `localized` für K2 und K3 nur gemeinsam mit der Falsch-Positiv-Rate berichtet
>   werden** — unverändert die Auflage aus dem Amendment vom 11.08.2026 (oben, Begründung
>   B36a) —, und die gemessene Basisrate von **49/52 = 0,9423** (Median über drei Läufe,
>   `c3b_k2_bericht_kontrolllauf.md` §4.2) lässt dem Wert kaum Kopffreiheit: bei einer derart
>   hohen Meldequote auf der sauberen Baseline trifft nahezu jedes injizierte Modul ohnehin ein
>   Finding, unabhängig davon, ob das Modell den Verstoß **erkannt** hat.
> - `strict` bleibt unterscheidungsfähig: dort müssen Kategorie **und** `subject` in der vom
>   Modell selbst gesetzten Form (§4 Nachtrag Rev. 19) übereinstimmen.
> - **Das ist genau der Fall, den Decision Record O, Konsequenz 2 vorweggenommen hat** —
>   „`localized` ist durch Übermelden manipulierbar, deshalb ist die Falsch-Positiv-Reihe
>   Voraussetzung". Die Vorregistrierung hat getragen; die Messung zeigt, **wie hoch** die
>   Basisrate tatsächlich ausfällt.
>
> **Keine Änderung** an Metrikdefinition (oben), Regeldatei, Prompt oder Antwortschema — nur die
> Berichtspflicht ist hiermit ausdrücklich bekräftigt.

> **Nachtrag (26.08.2026, Rev. 30) — `localized` IST FÜR K4/`CYCLE` NICHT DEFINIERT UND WIRD
> ALS „n. b." AUSGEWIESEN, NICHT ALS 0.** Begründung: V16;
> `c2a_bericht_contract_semantik.md` §2 (gemessene Ausgabeform);
> `c6_auswertungsspezifikation.md` §10.2 (die Lücke ist dort gemeldet, nicht entschieden —
> hier wird sie entschieden).
>
> **Der Befund.** Die `acyclic_siblings`-Ausgabe trägt **strukturell keinen Modulnamen**.
> Gemeldet wird eine **minimale Entfernungsmenge auf PAKETEBENE**, relativ zum `ancestor`
> notiert, mit führendem Punkt und Importzähler — `- .mappers -> .api (1 import)` — und je
> gebrochenem Contract in **mehreren Blöcken**, einer je Ebene. `localized` verlangt nach
> Decision Record O §2 ein Finding **im erwarteten Modul der erwarteten Komponente**. Ein
> Modul-Match ist aus dieser Ausgabe **nicht bildbar**; es gibt kein Modul, das man vergleichen
> könnte, nur ein Komponentenpaar.
>
> **Festlegung.** Für die Zellen **`CYCLE_SIBLING`/K4** und **`CYCLE_PARENT_CHILD`/K4** wird
> `localized` als **„n. b."** (nicht bildbar) ausgewiesen. **Nicht als 0** — eine 0 behauptete
> eine Messung mit dem Ergebnis „nicht lokalisiert", und das wäre falsch: es hat keine Messung
> stattgefunden, weil die Ausgabeform die Eingabe der Metrik nicht hergibt. Dieselbe
> Unterscheidung, die §6.2 der Auswertungsspezifikation für den `NetworkXError` bei K5 trifft
> (Werkzeugabbruch ≠ Nicht-Treffer).
>
> **`strict` bleibt unberührt.** Es gilt unverändert §4 Rev. 7: exakter Vergleich für K1,
> **Mengenregel** für K4 (Treffer, wenn die genannte Kantenmenge die injizierte Kante enthält).
> Die Erkennungsaussage für `CYCLE_SIBLING`/K4 — die vorregistrierte Matrixzelle „ja" — ruht
> auf der Mengenregel, nicht auf `localized`, und ist von dieser Festlegung **nicht** berührt.
> Ebenso unberührt: die vorregistrierte K4-Doppelmeldung bei `LAYER_BACK_CALL` (§5 Fall 3), die
> denselben Blocktyp verwendet und ebenfalls kein Modul trägt.
>
> **Erwogen und verworfen — Offenlegung nach der Praxis der Rev. 20 und Rev. 22.** Die
> Alternative war, die **Paketebene als Modul-Match zu zählen**: die Modulbedingung als
> automatisch erfüllt zu behandeln, sobald die Komponente stimmt (Lesart (a) in
> `c6_auswertungsspezifikation.md` §10.2). Sie ist **verworfen**. Grund: sie hätte die
> **Metrikdefinition in genau einer Zelle verschoben** — und zwar in derjenigen, in der K4 der
> Vergleichsmassstab des Checkers ist. K4 wäre dort **besser** geworden, nicht weil es mehr
> gefunden hätte, sondern weil für es eine mildere Definition gegolten hätte als für K1, K2 und
> K3, bei denen `localized` ein echtes Modul verlangt. Das ist **gewählt statt gemessen**. Eine
> Metrik, die je Zelle ihre Anforderung senkt, wo das Werkzeug sie nicht erfüllen kann, misst
> das Werkzeug nicht mehr.
>
> **Keine Änderung** an `strict`, an der Mengenregel, an der Erwartungsmatrix (§3) oder am
> Manifest. Es bewegt sich **keine Matrixzelle**.

> **Nachtrag (26.08.2026, Rev. 31) — SCHREIBVARIANZ BEI `FORBIDDEN_SIGNATURE_TYPE` IST EIN
> VORHERGESAGTER `strict`-AUSFALL, HIER DEKLARIERT.** Begründung:
> `d2_bericht_vormessungen.md` M0(c); **D2N**, §4 (Kontrollzeile `R-FRAMEWORK-1`) und §6 —
> Rohbeleg `~/scratch/d2n/schluesselform_semantische_familien.md`, der Bericht dazu folgt in
> D3b.
>
> **Gemessen im K2-Ruhezustand**, auf der sauberen Baseline, ohne jede Injektion: von **63**
> `R-FRAMEWORK-1`-Findings schreiben **57** den beanstandeten Typ als `sqlalchemy.orm.Session`
> — die im Manifest registrierte Form — und **6** als `sqlalchemy.orm`, um das Klassensegment
> gekürzt. Die sechs verteilen sich auf **zwei Module × drei Run-Indizes**, sind also je Modul
> **über alle drei Repetitionen reproduzierbar** und keine Einzelausreisser. Beide
> Abweichungsmodule sind `*_view_models`-**Zwillinge** des Clean-Control-Sets
> (`depot.orders.models.order_line_view_models`, `depot.orders.models.order_view_models`);
> auf **keinem** der vier Trägermodule von I21–I24 tritt die Kurzform auf.
>
> **Vorhergesagte Folge, ab jetzt deklariert.** Verkürzt ein Trägermodul in der Kampagne
> ebenso, dann ist `strict` für diese Injektion **0** bei gleichzeitigem `localized`-**Treffer**
> — Kategorie, Komponente und Modul stimmen, allein Segment 4 weicht ab. Dieser Ausfallmodus
> ist damit ein **vor der Messung deklarierter**, kein nachträglich erklärter. Tritt er ein,
> wird er als das berichtet, was er ist: eine Schreibweisenverfehlung des Modells, die `strict`
> definitionsgemäss als Nichttreffer führt.
>
> **Ausdrücklich: es wird NICHT normalisiert, und der Manifestwert wird NICHT angepasst.** Der
> Manifestschlüssel hält fest, **was injiziert wurde** (`sqlalchemy.orm.Session`, wörtlich aus
> dem Code, Decision Record L/P); ob das Modell diese Schreibweise trifft, ist genau das, was
> `strict` misst. Ein Manifest, das sich der beobachteten Modellschreibweise anpasst, misst
> nicht mehr das Modell. Das ist konsistent zu **Decision Record O**, wo **H3b** (Normalisierung
> der Subjektschreibweise) an genau diesem Argument verworfen wurde — die Festlegung wird hier
> nicht neu getroffen, sondern auf den nun gemessenen Fall angewandt.
>
> **Reichweite des Vorbehalts.** Er gilt **allein** für `FORBIDDEN_SIGNATURE_TYPE`. Die drei
> übrigen semantischen Familien treffen die vorregistrierte Form in **92 von 92** Findings
> (`R-PLACE-1` 54/54, `R-SIG-1…4` 24/24, `R-PORT-1…4` 14/14; 89 in K2, 3 in K3), ohne eine
> einzige gekürzte, relative oder dateipfadartige Schreibweise. Es bewegt sich **keine
> Matrixzelle**, es ändert sich **keine Metrikdefinition**.

> **Nachtrag (26.08.2026, Rev. 31) — `strict` IST FÜR `STRUCTURAL_PLACEMENT` NICHT UNABHÄNGIG
> VON `localized`.** Begründung: **D2N**, §1, Familie `R-PLACE-1`, Gegenprobe 1 — Rohbeleg
> `~/scratch/d2n/schluesselform_semantische_familien.md`, der Bericht dazu folgt in D3b.
>
> **Gemessen:** in **54 von 54** `R-PLACE-1`-Findings des K2-Ruhezustands ist **Segment 4
> (Subjektwert) zeichengleich mit Segment 3 (geprüftes Modul)**. Das Modell nennt als
> fehlplatziertes Modul **stets das geprüfte**; ein *anderes* Modul wird nie genannt.
>
> **Konsequenz für die Metrik.** Segment 3 setzt der Checker ohnehin aus dem `ChangedFact`
> (Lesekorrektur §4 Nachtrag Rev. 27), nicht aus der Modellantwort. Trägt Segment 4 in dieser
> Kategorie denselben Wert, so trägt der **Subjektwert dort keine von Segment 3 unabhängige
> Information**: `strict` ist für `STRUCTURAL_PLACEMENT` **nicht schärfer als „`localized` +
> Kategorie"**. Das ist eine Eigenschaft der Schlüsselform dieser Kategorie, kein Messfehler,
> und hier zum ersten Mal **an Daten belegt** statt aus dem Schema erschlossen.
>
> **Festlegung.** Die Zelle wird **weiterhin berichtet** — beide Metriken bleiben für diese
> Kategorie in der Ergebnistabelle stehen —, aber **mit dieser Einschränkung als Fussnote an
> der Zelle**, damit die Tabelle nicht **zwei unabhängige Metriken suggeriert, wo eine steht**.
> Die Fussnote ist Pflichtbestandteil der Ausgabe (`c6_auswertungsspezifikation.md` §3, §8).
>
> **Keine Metrikänderung.** `strict` und `localized` behalten ihre Definitionen aus §4
> unverändert; es wird **nichts zusammengelegt, nichts weggelassen und keine Zelle
> geschwärzt**. Die Einschränkung ist eine **Lesehilfe**, keine Rechenvorschrift — anders als
> die „n. b."-Festlegung für K4/`CYCLE` (Nachtrag Rev. 30), wo die Metrik **nicht berechenbar**
> ist; hier ist sie berechenbar, aber **nicht unabhängig**.

---

## 5. Metriken

- **Precision, Recall, F1** — gesamt und **pro Kategorie**, pro Konfiguration.
- **Pro LLM-Konfiguration:** Median über 3 Läufe als Headline-Zahl; alle Einzelläufe im
  Anhang; Spannweite als Reliability-Kennzahl (UF4, Linie aus 03.1/04.3).
- **Validität:** roh vs. final (Retry-Aufwand, `max_retries=2`), pro Lauf.
- **Kosten:** Tokens in/out und Latenz **pro Check** (= pro Datei-Prompt, Entscheidung I),
  aggregiert pro Commit und pro Gesamtlauf, pro Modell.
- **Baseline-Overlap (UF3):** Kategorie-weise Gegenüberstellung K1/K4/K5 vs. K2/K3 —
  wo sind die statischen Tools gleichauf, wo liegt der LLM-Mehrwert.

> **Amendment (11.08.2026) — Begründung: B36a.** `localized` (§4) ist **nur zusammen mit der
> Falsch-Positiv-Messreihe interpretierbar**: eine Lokalisationsmetrik ist durch Übermelden
> manipulierbar, ein Werkzeug, das für jede Datei irgendetwas meldet, erreicht hohen Recall.
> Ohne Clean-Control-Set ist `localized` keine belastbare Aussage.

> **Amendment (12.08.2026) — Begründung: Decision Record P.** **Aussagekraft bei kleinem n.**
> Bei 3–4 Injektionen je Szenario entspricht jede einzelne Verfehlung **25–33 Prozentpunkten**.
> Die Arbeit macht **Existenz-, Non-Inferiority- und Nicht-Abdeckungsaussagen**, keine
> Präzisionsschätzungen; Kennzahlen werden ohne Nachkommastellen-Interpretation berichtet.

> **Amendment (13.08.2026) — Begründung: `c1a_bericht_nova_modulith_struktur.md` C2; B27;
> `c1b_bericht_ruleengine_verifikation.md` Punkt 4.** **`__init__.py`-Module gehören nicht ins
> Clean-Control-Set.**
>
> Sie erscheinen als eigener `ChangedFact` und werden von keiner Dateiliste gefiltert
> (`gitDiff.ts:30`, `cliExtractor.ts:128`) — ohne ausdrückliche Regel liefen sie also mit. Im
> Vorbild sind **49 von 58** Init-Dateien leer (nichts oder nur Docstring, c1a C2); im Testrepo
> entstehen ~~bei sechs Paketen mit Unterpaketen rund **elf**~~ — **korrigiert 14.08.2026
> (Rev. 15): 23 von 73 Dateien** — davon. Die alte Zahl stammte aus dem inzwischen entfallenen
> Richtwert „eine `__init__.py` je Komponente"; seit `c1_komponentenschnitt.md` Rev. 2 bekommt
> **jedes** Paket eine (`c1_modulliste.md` Rev. 3, §4 Bedingung 9). **Das Argument wird durch
> die größere Zahl stärker, nicht schwächer:** 23 leere gegen 50 inhaltstragende Module ist
> keine Randkorrektur mehr — eine über alle 73 Dateien gerechnete Rate läge bei
> 50/73 = **0,685** der korrekten, also **um rund ein Drittel zu niedrig**.
> Eine Falsch-Positiv-Rate,
> deren Nenner mit leeren Modulen aufgefüllt ist, ist **optimistisch verzerrt**: gemessen
> werden soll die Neigung, in **Code** Verstöße zu sehen, nicht die trivial erfüllte
> Enthaltsamkeit gegenüber leeren Dateien.
>
> Zweiter Grund, unabhängig vom ersten: der Prompt eines leeren Moduls (keine Imports, keine
> Signaturen) ist ein **Rendering-Zweig, den der Canary-Hash nicht abdeckt** — `CANARY_CONTEXT`
> hat genau eine Regel, einen Import, eine Signatur, eine Kante und nicht-null `component`
> (`promptCanary.ts:11-39`, B27 / `b1_bericht_matchkey.md` E3). Ein Lauf über leere Module
> prüft damit einen Pfad, dessen Unverändertheit `user_prompt_render_sha256` gerade **nicht**
> bezeugt.
>
> **Ausnahme mit Auflage:** laufen Init-Module dennoch mit — etwa weil das
> `CYCLE_PARENT_CHILD`-Elternmodul konstruktionsbedingt eine `__init__.py` ist (§2, Amendment
> 13.08., Punkt 6) —, ist ihre Falsch-Positiv-Rate **getrennt auszuweisen**, nie in die
> Gesamtrate eingerechnet. Die Headline-Rate bezieht sich auf **inhaltstragende Module**.

> **Amendment (13.08.2026) — Begründung: `planung/c1_komponentenschnitt.md` §9;
> §2-Korrektur in diesem Protokoll.** **Die Ausnahmeklausel des Amendments oben ist
> gegenstandslos.** Sie setzte voraus, dass das `CYCLE_PARENT_CHILD`-**Elternmodul** als
> **Injektionsträger** mitlaufen muss; Träger ist aber das **Kindmodul** (§2, Amendment
> 13.08., Punkt (10)). Der Ausschluss der Init-Module aus dem Clean-Control-Set kollidiert
> mit `CYCLE_PARENT_CHILD` **nicht**, weil K1 im **Vollmodus** den ganzen Baum liest (§6,
> Graphmodus je Kategorie) und das Control-Set **nur den LLM-Pfad** betrifft.
> **Die Auflage bleibt als allgemeine Regel stehen:** laufen Init-Module aus einem anderen
> Grund dennoch mit, ist ihre Falsch-Positiv-Rate getrennt auszuweisen.

> **Nachtrag (14.08.2026, Rev. 16) — Begründung: `4b1_bericht_baseline_kern.md` §2 und §5.1;
> `c1_modulliste.md` §1.** **Vorhergesagter Falsch-Positiv auf der Adapter-Fassade.**
>
> `depot.core.adapters` ist das **einzige** Modul der Clean-Baseline, das das geschützte Internum
> importiert (`…internal.session`, `…internal.cache`) — genau das ist die Einzigartigkeitsbedingung
> aus Abnahmebedingung 7. Im **Clean-Control-Lauf** hat dieses Modul damit **R-PROTECT-1 im Scope**
> und zeigt im Prompt **genau die Importe, die die Regel verbietet**; erlaubt sind sie allein ihm,
> über die `allowed_importers`-Hälfte des `statement`.
>
> Ein K2/K3-Finding auf der Fassade ist deshalb **vorhergesagt** und **getrennt zu führen** — nicht
> als unerwarteter FP, sondern als **vorregistrierte Beobachtung**. Sie prüft eine bestimmte
> Fähigkeit: ob das Modell die **Erlaubnishälfte** des `statement` liest oder nur die
> **Verbotshälfte**. Ein Treffer hier ist ein Lesefehler am Regeltext, kein Architekturbefund, und
> wird in der Auswertung als solcher ausgewiesen; die Headline-FP-Rate trägt ihn mit, die
> Einzelnennung steht daneben.

> **Nachtrag (14.08.2026, Rev. 17) — DAS AUSSCHLUSSKRITERIUM DES CLEAN-CONTROL-SETS IST
> PRÄZISIERT.** Begründung: `4b1_bericht_baseline_kern.md` §5.1;
> `4b3_bericht_baseline_orders.md` §7.1; `4b4_bericht_baseline_billing.md` §2;
> `c1_modulliste.md` §1. **Änderung an einer vorregistrierten Regel VOR jeder Messung.**
>
> **Neue Fassung des Kriteriums:** Ausgeschlossen sind **LEERE `__init__.py`** — kein Import,
> kein `def`, kein `class`, kein `__all__` — **nicht Paketmodule als Gattung**.
>
> **Warum das keine Aufweichung ist.** Der tragende Grund der Amendments vom 13.08. und der
> Rev.-15-Korrektur war „**keine leeren Module im Falsch-Positiv-Nenner**": eine Rate, deren
> Nenner mit leeren Dateien aufgefüllt ist, misst die trivial erfüllte Enthaltsamkeit gegenüber
> leeren Dateien statt der Neigung, in **Code** Verstöße zu sehen. „Paketmodul" war die
> **Abkürzung** für „leer", weil zum Zeitpunkt jener Fassung alle Paketmodule als leer geführt
> wurden. Die gebaute Baseline widerlegt diese Gleichsetzung: **zwei der 23 Paketmodule sind
> inhaltstragend.**
>
> | Modul | Inhalt | Beleg |
> |---|---|---|
> | `depot.core.adapters` | Re-Export-Fassade: **drei** Top-Level-Importe, `__all__` mit fünf Namen, Modul-`__getattr__` (PEP 562) | `4b1…` §5.1 |
> | `depot.orders.services` | trägt die **Eltern/Kind-Kante** des `CYCLE_PARENT_CHILD`-Paares (Import auf `…services.pricing.engine`) plus **zwei** Funktionen | `4b3…` §7.1 |
>
> **ZWINGEND, weil die beiden Amendments sich sonst widersprechen.** Unter dem alten Wortlaut
> liefe `depot.core.adapters` **nie durch den LLM-Pfad** — und damit wäre der im §5-Nachtrag der
> Rev. 16 **VORREGISTRIERTE Falsch-Positiv auf eben dieser Fassade nicht messbar**. Eine
> vorregistrierte Beobachtung, deren Messobjekt eine zweite vorregistrierte Regel aus dem
> Messraum entfernt, ist kein Widerspruch, den man stehen lassen kann; einer der beiden Sätze
> muss weichen, und es ist der, dessen Begründung die Gleichsetzung „Paketmodul = leer" schon
> nicht mehr deckt.
>
> **Wirkung, abgezählt.** **21 leere Paketmodule** bleiben draußen (23 minus die beiden oben).
> Das **Clean-Control-Set umfasst damit 52 statt 50 Module** — die 50 inhaltstragenden Module
> aus `c1_modulliste.md` §4, Bedingung 9, plus die beiden inhaltstragenden Paketmodule. Das
> Argument gegen leere Module im Nenner bleibt in voller Stärke bestehen; es trifft jetzt nur
> genau die Dateien, für die es formuliert wurde.
>
> **Die Auflage aus dem Amendment vom 13.08. bleibt unberührt:** laufen **leere** Init-Module
> aus einem anderen Grund dennoch mit, ist ihre Falsch-Positiv-Rate getrennt auszuweisen. Die
> Headline-Rate bezieht sich unverändert auf **inhaltstragende Module** — der Kreis dieser
> Module ist mit diesem Nachtrag korrekt gezogen, nicht erweitert.


> **Nachtrag (23.08.2026, Rev. 18) — ZWEITE VORHERGESAGTE FALSCHMELDUNG: die beiden Portregeln
> auf `orders_services`.** Begründung: `c2a_bericht_regeldatei.md` §7.1 und §9 Punkt 5.
> Strukturell **derselbe Fall** wie die Adapterfassade (Nachtrag Rev. 16, §5) und wie diese
> **vorregistrierte Beobachtung, kein unerwarteter Falsch-Positiv, getrennt zu führen**.
> **Keine Matrixzelle bewegt sich.**
>
> **Der Sachverhalt.** Die Komponente `orders_services` trägt **zwei** `ABSENCE_REQUIRED`-Regeln
> im Scope: **R-PORT-2** für `depot.orders.services.catalog_service` und **R-PORT-3** für
> `depot.orders.services.refund_service`. Regel-Scopes sind **komponentenweit**
> (`contextBuilder.ts:19`), eine Modulgranularität gibt es im Checker nicht. Bei **jedem** Modul
> dieser Komponente — also auch bei `checkout_service`, `order_service` und dem jeweils anderen
> Portträger — sieht das Modell **eine Regel, die ein anderes Modul betrifft**. Am gerenderten
> Prompt belegt (c2a §7.1): auf `refund_service` steht R-PORT-2 neben R-PORT-3.
>
> **Vorregistriert:** ein Finding, das die **Nicht-Träger-Regel** zitiert — R-PORT-2 auf einem
> anderen Modul als `catalog_service`, R-PORT-3 auf einem anderen als `refund_service` — ist
> **erwartet** und wird **getrennt ausgewiesen**, nicht in die Falsch-Positiv-Reihe des
> Clean-Control-Sets gemischt. Es misst dasselbe wie die Fassade: **ob das Modell die
> einschränkende Hälfte eines `statement` liest**, hier die Trägernennung, dort die
> Erlaubnisliste.
>
> **Betroffen ist NUR `orders_services`.** Die drei anderen Portträgerkomponenten
> (`identity_services`, `billing_services`) tragen je **eine** Portregel; dort tritt der Fall
> nicht auf. Ursache ist die Verteilung der vier `MISSING_PORT_REFERENCE`-Injektionen
> (Komponentenschnitt §5: `orders_services` **2×**), nicht die Regelformulierung.
>
> **Warum die Trägernennung im `statement` bleibt und nicht der bessere Weg wäre, sie
> wegzulassen.** Ohne sie wären die beiden Regeln auf jedem Modul der Komponente **überhaupt
> nicht unterscheidbar**, und die Meldung wäre keine vorhergesagte Beobachtung mehr, sondern
> eine **garantierte Falschmeldung ohne Erkenntniswert**. Die Nennung verschiebt den Fall von
> „unvermeidbar" nach „prüfbar" — genau die Bewegung, die den Fassaden-Nachtrag der Rev. 16
> trägt. Die Asymmetrie zum Baseline-Werkzeug bleibt bestehen und ist als **UF3-Befund** zu
> führen: **K5** bindet dieselbe Regel mit `are_named` an das **Modul** (Komponentenschnitt
> §6.3, vier Einzelregeln), der Checker kann das nicht.

> **Nachtrag (26.08.2026, Rev. 30) — WANDUHRZEIT EINHEITLICH EXTERN, FÜR ALLE FÜNF
> KONFIGURATIONEN.** Begründung: `c6_auswertungsspezifikation.md` §8 Punkt 6 und §10.3 (dort
> gemeldet, nicht entschieden); §6 Nachtrag Rev. 24; B9+ (a) und (b);
> `d2_bericht_vormessungen.md` M5.
>
> **Der Befund.** Für K1/K2/K3 liegt eine Wanduhrzeit im `run_footer.wall_clock_ms` des
> Checkers vor (`run.ts:112,260`, gemessen **innerhalb** des CLI-Prozesses). Für **K4 und K5
> existiert kein Äquivalent** — beide sind externe Werkzeuge ohne das Checker-Logformat. Innen-
> und Aussenmessung zu mischen macht die Kostentabelle **konfigurationsübergreifend
> unvergleichbar**: sie verglichen dann fünf verschiedene Uhren.
>
> **Festlegung.** Die **berichtete** Wanduhrzeit ist für **alle fünf** Konfigurationen
> **extern je Invocation** gemessen — monotone Uhr, vom Kampagnen-Runner geschrieben,
> Subprozess-Start bis -Ende, strukturell analog dem `duration_s`-Feld, das in den
> C3b-Kontrollläufen bereits vorliegt (`data/c3b-k2/run_manifest.json`,
> `data/c3b-k3/run_manifest.json`). `run_footer.wall_clock_ms` bleibt für K1/K2/K3 als
> **Innenwert im Anhang** erhalten und erlaubt, die **Differenz Prozessstart/Nutzarbeit**
> auszuweisen. Gemessen an den Kontrollläufen ist diese Differenz klein und richtungsstabil:
> Median aussen 8,4 s gegen innen 8,3 s (K2), 97,8 s gegen 96,3 s (K3).
>
> **Zwei Randbedingungen, die die Zahlen lesbar machen:**
>
> - **K4 baut den Graphen jedes Mal neu.** `--no-cache` ist je import-linter-Lauf
>   **Ablaufregel** (§1 Amendment 11.08., B9+ (b)) — die gemessene Zeit enthält den vollen
>   Graphaufbau. Das ist **die ehrliche Laufkost** dieser Konfiguration, kein Messartefakt und
>   nichts, was durch Cache-Aktivierung „verbessert" werden dürfte.
> - **K5 bricht beim ersten fehlgeschlagenen Assert ab** (pytest-basiert, B9+ (a)) — die
>   Laufzeit hängt am **Trefferzeitpunkt** innerhalb der 24 Tests, nicht allein an der
>   Repositoriumsgrösse. Ein Lauf ohne Treffer (Clean-Baseline: `24 passed`) und ein Lauf mit
>   frühem Treffer sind deshalb **nicht ohne Weiteres vergleichbar**.
>
> **Berichtsform.** **Grössenordnungen**, ohne Interpretation von Nachkommastellen — §5
> Amendment 12.08. gilt unverändert fort. Eine Differenz von Zehntelsekunden zwischen zwei
> Konfigurationen ist **keine** berichtsfähige Aussage.

> **Nachtrag (26.08.2026, Rev. 31) — DIE VORBELASTUNG JE INJEKTION IST BERICHTSPFLICHTIG.**
> Begründung: **D2N**, Bilanz (§5, §6) und Zusatzbefunde (§1, §3) — Rohbeleg
> `~/scratch/d2n/schluesselform_semantische_familien.md`, der Bericht dazu folgt in D3b;
> `d2_bericht_vormessungen.md` M0(d); `c3b_k2_bericht_kontrolllauf.md`.
>
> **Gemessen:** für **15 der 32** Injektionen tritt der im Manifest erwartete `match_key`
> **bereits im K2-Ruhezustand** — auf der sauberen Baseline, vor jeder Injektion — als
> **tatsächlich gebildeter Schlüssel** auf. Es sind I07–I09 (`FORBIDDEN_RELATION`), I17–I20,
> I21–I24 und I29–I32.
>
> **Aufschlüsselung nach semantischer Familie**, weil die Bilanz sonst falsch gelesen wird:
>
> | Familie | Injektionen | erwarteter Schlüssel im Ruhezustand gebildet |
> |---|---|---|
> | `ABSENCE_REQUIRED` (`R-PORT-1…4`) | I17–I20 | **4 / 4**, je 3× in K2 |
> | `FORBIDDEN_SIGNATURE_TYPE` (`R-FRAMEWORK-1`) | I21–I24 | **4 / 4** in K2 (3× / 15× / 12× / 3×) |
> | `API_CONTRACT` (`R-SIG-1…4`) | I29–I32 | **4 / 4**, je 3× in K2; zwei davon auch in K3 |
> | `STRUCTURAL_PLACEMENT` (`R-PLACE-1`) | I25–I28 | **0 / 4** |
> | `FORBIDDEN_RELATION` | I07–I09 | **3 / 12** |
>
> **Drei** der vier semantischen Familien sind vollständig (je 4/4), die vierte —
> `STRUCTURAL_PLACEMENT` — trägt **0/4**, und das ist **strukturell zwingend**: die
> `INCORRECT_LOCATION`-Injektion **verschiebt** das Modul, der Manifestschlüssel nennt den Pfad
> **nach** der Verschiebung, den es auf der Baseline noch nicht gibt (D2N §1(d),
> Gegenprobe 2). 3 × 4 + 3 = **15** — die Rechnung geht nur mit drei vollständigen Familien
> auf. (Die Formulierung „alle vier semantischen Familien vollständig" in D2N §6 ist an dieser
> Stelle **ungenau**; verbindlich ist die Tabelle oben, deren Einzelwerte D2N §1(d), §2(d),
> §3(d) und §4(d) wörtlich tragen.)
>
> **Zwei Beobachtungen, die die Auflage unten tragen:**
>
> - **I17–I20 (`ABSENCE_REQUIRED`):** die Injektion **entfernt** einen Portbezug, die saubere
>   Baseline **erfüllt** die Regel — und das Modell meldet den Verstoss dort **trotzdem**, mit
>   **exakt dem Schlüssel**, den das Manifest für den injizierten Fall erwartet, in **jeder**
>   der drei Repetitionen. Derselbe Schlüssel entsteht hier also **ohne** Verstoss.
> - **I25–I28 (`STRUCTURAL_PLACEMENT`):** drei der vier Trägermodule (`legacy_order_index`,
>   `legacy_invoice_index`, `legacy_token_index`) werden im Ruhezustand **je 3×** als
>   fehlplatziert gemeldet — **bevor** irgendetwas verschoben wurde; das vierte,
>   `depot.billing.models.legacy_tax_models`, wird geprüft, aber **nie** gemeldet. Bei I25–I27
>   wird also auf Modulen gemessen, die schon im Ruhezustand Meldungen **derselben Kategorie**
>   ziehen, bei I28 nicht.
>
> **Auflage.** Zu **jedem** Kampagnenergebnis wird die **Ruhezustandszahl desselben Moduls in
> derselben Kategorie** aus C3b mitberichtet (`data/c3b-k2/` bzw. `data/c3b-k3/`, gleiche
> Konfiguration wie das Kampagnenergebnis). **Ein `strict`-Treffer, der die Ruhezustandsrate
> nicht übersteigt, wird nicht als Erkennungsnachweis geführt** — er ist dann mit „das Modell
> meldet dieses Modul ohnehin" vollständig erklärbar, und die Injektion hat nichts
> hinzugefügt, was die Zahl belegt.
>
> **Einordnung.** Diese Auflage ist die **injektionsscharfe Fassung** der bestehenden Regel
> „`localized` nie ohne die Falsch-Positiv-Rate" (§5 Amendment 11.08.). Dort wirkt die
> Kontrolle **global** über das Clean-Control-Set; hier wirkt sie **je Injektion**, weil die
> Vorbelastung nachweislich **ungleich verteilt** ist — 4/4 in einer Familie, 0/4 in der
> nächsten. Eine globale FP-Rate mittelt genau die Ungleichheit weg, auf die es bei der
> Einzelinjektion ankommt. **Keine Metrikänderung:** Precision, Recall und F1 werden
> unverändert nach §5 gebildet; die Ruhezustandszahl tritt **neben** sie, nie an ihre Stelle,
> und es wird **nichts subtrahiert**.

> **Nachtrag (26.08.2026, Rev. 31) — PAARWEISE AUSLESART JE INJEKTION, VORREGISTRIERT.**
> Begründung: derselbe Befund wie im Nachtrag oben; Berichtsform nach §5 Amendment 12.08.
>
> **Zusätzlich zu den bestehenden Kennzahlen, nicht statt ihnen** — Precision, Recall, F1,
> Median über drei Läufe, Spannweite und die FP-Rate bleiben unverändert bestehen (§5 oben):
> je **Injektion** und je **Konfiguration** wird die **Differenz zwischen injiziertem Zustand
> und Ruhezustand desselben Moduls** berichtet.
>
> **Bildungsvorschrift.**
>
> - **Zählgrösse:** Findings desselben Moduls in derselben Kategorie, wie in der Auflage oben.
> - **Ruhezustandsseite:** aus `data/c3b-k2/` bzw. `data/c3b-k3/`, **konfigurationsgleich** zum
>   Kampagnenergebnis.
> - **Gleiche Repetitionszahl auf beiden Seiten.** Beide Bestände tragen **drei** Läufe je
>   Modul; wird auf einer Seite anders aggregiert als auf der anderen, ist die Differenz eine
>   Zahl ohne Gegenstand.
> - **Für K1, K4 und K5** ist die Differenz mangels LLM-Streuung trivial, aber aus Symmetrie
>   der Tabelle **ebenfalls auszuweisen**.
>
> **Deskriptiv, ohne inferenzstatistische Deutung.** Es wird **kein** Test gerechnet, **kein**
> Konfidenzintervall und **keine** Signifikanz behauptet; bei 3 Läufen und 3–4 Injektionen je
> Szenario (Amendment 12.08., Threat T4) trüge nichts davon. Berichtsform: **Grössenordnungen**,
> ohne Interpretation von Nachkommastellen.
>
> **Bindend: die Differenz wird auch berichtet, wenn sie null oder negativ ist.** Eine
> Injektion, nach der das Modell **weniger** meldet als im Ruhezustand, ist ein Ergebnis
> dieser Arbeit und keine Störung — sie fällt nicht heraus, wird nicht gerundet und wird nicht
> kommentarlos durch die Aggregatzahl ersetzt. Dieselbe Disziplin wie bei der Auflage in §9
> zur B36a-Gegenprobe: **nicht nachbessern, nur berichten.**

---

## 6. Ablauf

1. Clean-State-Audit (§2) bestanden, Known-Deviations-Liste eingefroren.
2. Injektions-Commits einspielen (Reihenfolge im Manifest).
3. Pro Konfiguration ein Skriptaufruf über alle Injektions-Commits (diff-aware,
   ~~`HEAD~1`~~ — **korrigiert am 12.08.2026 auf `--base <Baseline-SHA>`**; relative Referenzen
   sind seit Rev. 4 ausgeschlossen, siehe Amendment (11.08.2026) unten);
   ~~K1/K4/K5 zusätzlich einmal auf dem Endzustand (Gesamtsicht)~~ — **ersetzt am 12.08.2026
   durch den deskriptiven Vollbild-Lauf, siehe Amendment unten.**
4. Rohlogs unverändert archivieren (gleiche Disziplin wie `scale-probe/`: Manifest mit
   Repo-Commit, Checker-Commit, Prompt-Hash, Regel-Hash, Modellnamen, Datum).
5. Auswertung strikt nach §4/§5; Klassifikation ambiger Fälle zuletzt, dokumentiert.

> **Amendment (11.08.2026) — Begründung: B33.**
>
> **Diff-Erzeugung.** Jede Injektion ist ein eigener Commit über einer Clean-Baseline; die
> Historie ist **linear, ohne Merges** (`git diff <parent>` sieht bei einem Merge-Commit nur
> einen Elternteil). Je Messlauf: `git checkout <Injektions-SHA>`, Working Tree clean,
> `--base <Base-SHA>`. **Der Base-Wert ist immer ein SHA, nie eine relative Referenz** wie
> `HEAD~1`: `base_ref` wird wörtlich geloggt und nicht aufgelöst, ein Lauf mit relativer
> Referenz ist nur zusammen mit der Repo-Historie interpretierbar. Mit SHA ist er
> selbstbezeugend, und zusammen mit `target_repo_git_head` steht das gemessene Delta
> vollständig im Artefakt.
> **Working Tree clean ist Vorbedingung, nicht Empfehlung:** der Diff vergleicht `<base>`
> gegen den Working Tree, nicht `<base>..HEAD`. Bei verschmutztem Tree mischt der Diff
> Commit- und uncommittete Änderungen, und **kein Log-Feld unterscheidet das** — ein solcher
> Lauf ist nachträglich nicht von einem sauberen zu trennen.
> Verworfen: Injektion im Working Tree (der geprüfte Zustand wäre nicht versioniert, alle
> Läufe trügen denselben `target_repo_git_head`) sowie ein Branch je Injektion statt einer
> Historie (kein Zusatznutzen, mehr Verwaltung).
>
> **Ergänzung der Lauf-Akzeptanzregel.** Ein Lauf ist ungültig, wenn `changed_files_count: 0`
> ist — das ist kein „sauberer" Lauf, sondern ein nicht gemessener. Ein Lauf **ohne
> `run_header`** gilt als **nicht durchgeführt**, nicht als Lauf mit null Findings: bei
> unauflösbarer Base wirft `git`, bevor der Header geschrieben wird (Exit 2, Logdatei 0 Bytes,
> kein Artefakt). Beides prüft die Harness bzw. der Runner je Lauf, nicht der Mensch.

> **Amendment (12.08.2026) — Begründung: Revision von B33,
> `c1b_bericht_komponentenschnitt.md`, Decision Record M.**
>
> **Historie sternförmig statt linear.** Ein Clean-Baseline-Commit **B**; darüber **32
> Commits mit B als einzigem Elternteil**, je eine Injektion, jeder unter **eigenem Ref**
> (`inj/01` … `inj/32`). **Kein Merge.** Begründung: eine **lineare Kette ist kumulativ** —
> Commit *n* enthält die Injektionen 1..*n*, und K4, K5 sowie K1 im Full-Modus lesen den
> **Gesamtzustand** und würden alle vorherigen Injektionen mitmelden. Bei `acyclic_siblings`
> kommt hinzu, dass die ausgegebene **minimale** Kantenmenge eine globale Optimierung über alle
> Zyklen ist und die injizierte Kante bei mehreren gleichzeitigen Zyklen **nicht enthalten
> muss**. „Linear" war in B33 **Begründung, nicht Zweck**; die dort tragende Anforderung „genau
> ein Elternteil, kein Merge" ist von der Sternform erfüllt.
>
> - **`--base` ist für alle Läufe derselbe Baseline-SHA**, nie eine relative Referenz.
> - **Jede Injektion braucht ein Ref**, und das `git bundle` des Testrepos umfasst `--all`:
>   unreferenzierte Commits werden von `git gc` entfernt.
>
> **Deskriptiver Vollbild-Lauf.** Es gibt **einen zusätzlichen Commit mit allen 32
> Injektionen** (Elternteil B, kein Merge) für einen Lauf von K1, K4 und K5. Er wird
> **nicht gegen das Manifest gejoint** und geht **in keine Metrik** ein; er dient allein der
> Beobachtung des Werkzeugverhaltens unter Mehrfachverletzung (UF4, Ausgabegranularität).
> Ausdrücklich so vorregistriert.
>
> **Graphmodus je Kategorie für K1, vor der Messung festgeschrieben.**
> `--rule-graph diff` für `FORBIDDEN_RELATION`, `--rule-graph full` für `CYCLE`. Begründung: im
> Diff-Modus sieht die Rule-Engine nur die Importe der geänderten Datei, ein Zyklus braucht
> aber **beide** Kanten; umgekehrt entsteht im Diff-Modus **keine** `cycle`-Begleitmeldung zu
> einer `FORBIDDEN_RELATION`-Injektion (§4, `expected_co_findings`).
> **Die daraus folgende Asymmetrie ist zu benennen:** K1 erhält bei `CYCLE` den vollen
> Importgraphen, K2/K3 sehen eine einzelne Datei. Das ist **keine Bevorteilung von K1**,
> sondern die Kehrseite der in Decision Record P begründet verworfenen Option „Importgraph im
> Prompt" (§9); die `CYCLE`-Nullzeile für K2/K3 ist konstruktionsbedingt.
>
> **Lauf-Akzeptanzregel, Ergänzung zu B14 und B33.** Ein LLM-Lauf der Kampagne ist nur gültig,
> wenn **`changed_files_count == 1` UND `calls_total == 1`**. Begründung: der Diff ist je
> Injektionslauf konstruktionsbedingt genau **eine** Datei, und die **Differenz dieser beiden
> Zahlen ist das einzige Signal** für ein nicht gemapptes Modul — ein solches Modul erzeugt
> **keinen** `llm_call`, **keinen** `checks_performed`-Eintrag und **keine** Fehlermeldung
> (`c1b_bericht_komponentenschnitt.md`, Punkte 6 und 8, beide ausgeführt). Für den
> **Vollbild-Lauf gilt die Regel nicht**.
>
> **Messstand.** Der Freeze-Tag ist **über seinen SHA** zu führen, nicht nur über den Namen:
> die Push-Rechte auf `origin` umfassen das **Löschen von Tags**
> (`b20_bericht_push_rechte.md` plus manuelle Verifikation vom 12.08.2026), ein Tagname ist
> damit **kein unveränderlicher Anker**. `phase04-freeze = <SHA>` gehört ins Messmanifest.

> **Amendment (13.08.2026) — Begründung: Decision Record M.2, Festlegung 2 und Begründung 3;
> `c1b_bericht_ruleengine_verifikation.md` Punkt 7, Kontrolllauf.** Der Absatz „Graphmodus je
> Kategorie" oben bleibt unverändert stehen; seine **Begründung** wird ersetzt, seine
> **Festlegung** bleibt richtig.
>
> **Ersetzte Begründung für den Ausschluss der Begleitmeldung im Diff-Modus.** Tragend ist
> nicht „ein Zyklus braucht **beide** Kanten" — das legt nahe, es hinge davon ab, wo die zweite
> Kante liegt. Tragend ist: **ein Ein-Datei-Diff erzeugt genau einen Adjazenz-Knoten.** Alle
> beobachteten Importe stammen aus einem Modul, also tragen alle Komponentenkanten dieselbe
> Quellkomponente, `adjacency` hat einen Schlüssel, die DFS besucht einen Knoten, und
> `childState === VISITING` (`ruleEngine.ts:120`) tritt nie ein. Der Ausschluss ist damit eine
> Eigenschaft des Diffs, nicht des Repos, und gilt unbedingt.
>
> **Der deskriptive Vollbild-Lauf bekommt eine positive Messaufgabe.** Er war bisher nur von
> der Vorhersagepflicht freigestellt. Er ist ab jetzt die Beobachtung, an der die **Grenze der
> Handableitbarkeit zu zeigen ist**: bei einem Zyklus über **mehr als zwei** Komponenten
> benennt K1 einen Träger, der mit der Ursache nichts zu tun hat. Gemessen im Kontrolllauf zu
> Punkt 7: bei `presentation → application → persistence → presentation` trägt der
> `cycle`-Record die Kante **`presentation -> application`** mit `location.module`
> `shop.presentation.web` — die Rückkante auf die kleinste DFS-Wurzel —, während die injizierte
> Kante `persistence -> presentation` war. Der Vollbild-Lauf trägt alle 32 Injektionen
> gleichzeitig, Z1 (genau zwei beteiligte Komponenten) gilt dort nicht, und genau solche
> längeren Zyklen können entstehen. **Das ist der Beobachtungsgegenstand, nicht ein Mangel des
> Laufs.** Er bleibt ungejoint und metrikfrei; berichtet wird qualitativ, mit dem Kontrolllauf
> als vorab bekanntem Erwartungsbild (UF4, Ausgabegranularität).

> **Nachtrag (14.08.2026, Rev. 17) — VORBEDINGUNG FÜR C3: DER LEER-PROMPT WIRD EINMAL GERENDERT
> UND GEPRÜFT.** Begründung: B27 / `b1_bericht_matchkey.md` E3 (`promptCanary.ts:11-39`);
> `c1_modulliste.md` §4, Bedingung 8; Protokoll §3, Amendment (e).
>
> **Vorbedingung, vor dem Start der Kampagne und als Schritt des Clean-State-Audits (C3):** Der
> Prompt für **ein importfreies Modul** wird **einmal gerendert** und **manuell geprüft** —
> Vorlage, Abschnittsköpfe, leere `## Imports`-Liste, `## Rules to check`. Das Ergebnis wird
> festgehalten; ein Defekt ist vor dem Freeze zu beheben, danach nur noch als Amendment mit
> vollständigem Re-Run.
>
> **Grund, in drei Schritten:**
>
> 1. Die vier `INCORRECT_LOCATION`-Träger **I25–I28 sind import- und referenzfrei** — das ist
>    keine Zufälligkeit des Baus, sondern **gefordert** (Abnahmebedingung 8, Amendment (e); ohne
>    sie wäre die vorregistrierte Zelle K5 = nein falsch). Im Diff eines
>    `INCORRECT_LOCATION`-Commits erscheint also eine **hinzugefügte Datei ohne Importe**.
> 2. Der **Canary-Hash deckt genau diesen Rendering-Zweig nicht ab**: `CANARY_CONTEXT` hat eine
>    Regel, **einen Import**, eine Signatur, eine Kante und nicht-null `component`. Ein Prompt
>    **ohne** Importe wurde damit **nie gerendert**; `user_prompt_render_sha256` bezeugt für
>    diesen Zweig nichts.
> 3. Ein Defekt dort — eine fehlende Überschrift, ein leerer Block, eine abgeschnittene
>    Regelliste — erschiene in der Auswertung als **vier Modellfehler** in genau der Kategorie,
>    in der **K2/K3 als einzige „ja" tragen** (`STRUCTURAL_PLACEMENT`; K1 = Nicht-Abdeckung, K4
>    = teilweise und namensblind, K5 = nein). Der teuerste denkbare Ort für einen stillen
>    Renderfehler, und der einzige, an dem er als Modellbefund durchginge.
>
> **Abgrenzung:** das ist **keine** Messung und **kein** Modell-Call — gerendert wird der
> Prompttext, geprüft wird er mit dem Auge. Die Prüfung gehört in **C3** und ist in **B27**
> vermerkt.

> **Nachtrag (23.08.2026, Rev. 22) — LAUF-AKZEPTANZREGEL FÜR DEN KONTROLLLAUF.** Begründung:
> `increment7_bericht_control_set.md` §1b, §2b, §6 und §8.1 (Increment 7 / B5, Checker-Commit
> `348ca9d`, **kein Modell-Call**); `c2a_bericht_regeldatei.md` §5 (Validatorpunkt (3b));
> `4c_bericht_soll_und_validator.md` §5 (Ladetest).
>
> **REGEL: ein Kontrolllauf ist nur gültig, wenn `control_files_count == calls_total`.** Die
> bestehende Regel **`changed_files_count == 1 ∧ calls_total == 1`** (Amendment 12.08.) gilt
> **nur für Injektionsläufe** — dort ist der Diff konstruktionsbedingt genau eine Datei. Im
> Kontrolllauf trägt der Diff nichts bei, und die Zahl der Calls ist die Zahl der
> Kontrolldateien. Die beiden Regeln stehen **nebeneinander**; keine ersetzt die andere, und für
> den **Vollbild-Lauf** gilt wie bisher keine von beiden.
>
> **DIE VORBEDINGUNG IST BEREITS GARANTIERT — EIN WEITERER LAUF WAR NICHT NÖTIG.** Increment 7
> führt die Regel unter **Vorbehalt** (§8.1): `checkFactWithLlm` überspringt den Modell-Call,
> wenn für die Komponente einer Datei **keine Regel im Scope** liegt (`llmChecker.ts:96`); dann
> wäre `calls_total < control_files_count`, **ohne dass etwas kaputt ist** — die Datei erschiene
> als Abdeckungslücke mit leerem `checks_performed`. Für das **52er-Control-Set** ist der
> Vorbehalt aus **bereits vorliegenden** Messungen aufgelöst, in drei Schritten:
>
> 1. **Regel-Scopes sind KOMPONENTENWEIT, nicht modulweit.** `contextBuilder.ts:19` filtert über
>    `component != null && r.scope.components.includes(component)`. Ob eine Datei einen Call
>    erzeugt, hängt damit **allein an ihrer Komponente** — nicht an ihrem Modulnamen, nicht an
>    ihrem Inhalt.
> 2. **Jede Komponente ist von mindestens einer Regel gescopt.** Validatorpunkt **(3b)** stand in
>    C2a auf **`components scoped by no rule = 0`**, über **19 von 19** Komponenten
>    (`c2a_bericht_regeldatei.md` §5, wörtliche Validatorausgabe).
> 3. **Jedes Modul hat eine Komponente.** Der 4c-Ladetest über `resolveTopology`/`componentOf`
>    ergab **77 gelistete Module, 0 Fehltreffer**, und gegen den Dateibaum **73 Module, 0
>    unmapped** (`4c_bericht_soll_und_validator.md` §5).
>
> Aus (1)–(3) folgt für **alle 52 Kontrollmodule** mindestens eine Regel im Scope, also
> `control_files_count == calls_total`. **Der Nachweis ist eine Ableitung aus gemessenen Größen,
> kein neuer Lauf** — und er ist an seine Voraussetzungen gebunden: er fällt, sobald sich
> Regeldatei oder Soll ändern. Beide sind bis **C5** änderbar, und (3b) läuft nach §2 (Rev. 11)
> **je Injektionscommit** ohnehin mit; die Bedingung wird damit fortlaufend nachgeprüft, nicht
> einmalig behauptet.
>
> **MESSPFAD.** `--control-files <pfad>` und das `run_header`-Feld **`control_files_count`** sind
> ab hier **Bestandteil des Messpfads**. `control_files_count` zählt **nach** Abzug der
> Überschneidung mit dem Diff (`run.ts:161`) — anders gerechnet wäre die Akzeptanzregel nicht
> stimmig, weil eine Datei in beiden Mengen sonst zweimal zählte —, und `--json-out` übernimmt
> beide Zahlen **ohne Neuberechnung** aus dem Header (`jsonOut.ts:43-46`), sodass die zwei
> Dokumente nicht auseinanderlaufen können. Der Prompt ist **unberührt**: `diff_kind` ist
> Log-Metadatum und erreicht `buildUserPrompt` nicht; eine Kontrolldatei rendert **zeichengleich**
> wie dieselbe Datei als `modified` (§4 des Berichts, als Zeichenvergleich gepinnt).
>
> **Der zugehörige `checker_git_head` ist `348ca9d`** — der dritte Stand nach `c493daf` und
> `fe66357`. Die **vier Inhaltshashes sind byte-identisch geblieben**, `promptFreeze.spec.ts` ist
> unverändert und grün; bewegt hat sich allein `checker_git_head`.

> **Nachtrag (23.08.2026, Rev. 24) — AUFRUFSPEZIFIKATION.** Die folgenden Zeilen sind die
> verbindlichen Aufrufe. Ausgangspunkt sind die in C3a tatsächlich ausgeführten Zeilen
> (`c3a_bericht_clean_state_audit.md` §2–§4); die LLM- und Kampagnenparameter sind hier vor
> ihrer Ausführung vervollständigt. Dabei bedeuten `<checker>`, `<testrepo>`, `<ma>`, `<venv>`,
> `<out>`, `<baseline-sha>` und `<injection-sha>` die im Laufmanifest aufgelösten absoluten
> Pfade beziehungsweise SHAs. Jeder Lauf erfolgt mit Arbeitsverzeichnis `<testrepo>` und nach
> Checkout von `<injection-sha>`; der Kontrolllauf erfolgt auf `<baseline-sha>`.
>
> **K1, Diff-Graph (je Injektion):**
>
> ```sh
> node <checker>/packages/triton-conformance/dist/cli.js \
>   --topology <ma>/data/soll/depot_soll.ilograph.yaml \
>   --rules <ma>/data/soll/architecture-rules.yaml \
>   --src-root src --rule-graph diff --base <baseline-sha> \
>   --runs 1 --timeout-ms 120000 \
>   --run-log <out>/k1_diff_<injection-sha>.jsonl \
>   --json-out <out>/k1_diff_<injection-sha>.json
> ```
>
> **K1, Full-Graph (je `CYCLE`-Injektion sowie mit entsprechendem Ausgabenamen für den
> deskriptiven Vollbild-Lauf):**
>
> ```sh
> node <checker>/packages/triton-conformance/dist/cli.js \
>   --topology <ma>/data/soll/depot_soll.ilograph.yaml \
>   --rules <ma>/data/soll/architecture-rules.yaml \
>   --src-root src --rule-graph full --base <baseline-sha> \
>   --runs 1 --timeout-ms 120000 \
>   --run-log <out>/k1_full_<injection-sha>.jsonl \
>   --json-out <out>/k1_full_<injection-sha>.json
> ```
>
> **K2, Ollama (je Injektion):**
>
> ```sh
> CONFORMANCE_API_KEY=<ollama-dummy-key> \
> CONFORMANCE_BASE_URL=http://localhost:11434/v1 \
> CONFORMANCE_MODEL=qwen2.5-coder:7b \
> node <checker>/packages/triton-conformance/dist/cli.js \
>   --topology <ma>/data/soll/depot_soll.ilograph.yaml \
>   --rules <ma>/data/soll/architecture-rules.yaml \
>   --src-root src --rule-graph diff --base <baseline-sha> \
>   --runs 3 --timeout-ms 240000 \
>   --run-log <out>/k2_<injection-sha>.jsonl \
>   --json-out <out>/k2_<injection-sha>.json
> ```
>
> **~~K3, OpenRouter/DigitalOcean (je Injektion):~~** — **ÜBERHOLT mit Rev. 32.** Der folgende
> Block bleibt als Revisionsnachweis **unverändert** stehen; verbindlich ist die korrigierte
> Fassung darunter (Nachtrag Rev. 32, §6).
>
> ```sh
> CONFORMANCE_API_KEY=<openrouter-api-key> \
> CONFORMANCE_BASE_URL=https://openrouter.ai/api/v1 \
> CONFORMANCE_MODEL=nvidia/nemotron-3-super-120b-a12b \
> CONFORMANCE_PROVIDER_PIN=digitalocean \
> node <checker>/packages/triton-conformance/dist/cli.js \
>   --topology <ma>/data/soll/depot_soll.ilograph.yaml \
>   --rules <ma>/data/soll/architecture-rules.yaml \
>   --src-root src --rule-graph diff --base <baseline-sha> \
>   --runs 3 --timeout-ms 600000 \
>   --run-log <out>/k3_<injection-sha>.jsonl \
>   --json-out <out>/k3_<injection-sha>.json
> ```
>
> **K3, DigitalOcean-Direktzugang (je Injektion) — KORRIGIERTE FASSUNG, Rev. 32, verbindlich:**
>
> ```sh
> CONFORMANCE_API_KEY=<DO_MODEL_ACCESS_KEY aus ~/ma/.secrets/do.env> \
> CONFORMANCE_BASE_URL=https://inference.do-ai.run/v1 \
> CONFORMANCE_MODEL=nvidia-nemotron-3-super-120b \
> node <checker>/packages/triton-conformance/dist/cli.js \
>   --topology <ma>/data/soll/depot_soll.ilograph.yaml \
>   --rules <ma>/data/soll/architecture-rules.yaml \
>   --src-root src --rule-graph diff --base <baseline-sha> \
>   --runs 3 --timeout-ms 600000 \
>   --run-log <out>/k3_<injection-sha>.jsonl \
>   --json-out <out>/k3_<injection-sha>.json
> ```
>
> **`CONFORMANCE_PROVIDER_PIN` steht unter dieser Zeile NICHT** und ist damit `undefined`
> (`cli.ts:50`: `process.env.CONFORMANCE_PROVIDER_PIN || undefined`) — keine Auslassung, sondern
> die Konsequenz aus B32: ohne Router gibt es nichts zu pinnen. `provider_pin` im `run_header`
> bleibt `null`, `provider_served` je Call `null` (§1 Nachtrag Rev. 30).
>
> **K4, import-linter (je ausgechecktem Zustand):**
>
> ```sh
> PYTHONPATH=src <venv>/bin/lint-imports \
>   --config <ma>/data/soll/importlinter.ini --no-cache
> ```
>
> **~~K5, PyTestArch (je ausgechecktem Zustand):~~** — **ÜBERHOLT mit Rev. 32: die Zeile ist
> NICHT AUSFÜHRBAR, ihr fehlt `DEPOT_SRC`.** Der folgende Block bleibt als Revisionsnachweis
> **unverändert** stehen; verbindlich ist die korrigierte Fassung darunter (Nachtrag Rev. 32, §6).
>
> ```sh
> <venv>/bin/python -m pytest -p no:cacheprovider \
>   <ma>/data/soll/test_architecture.py
> ```
>
> **K5, PyTestArch (je ausgechecktem Zustand) — KORRIGIERTE FASSUNG, Rev. 32, verbindlich:**
>
> ```sh
> DEPOT_SRC=<testrepo>/src <venv>/bin/python -m pytest -p no:cacheprovider -q \
>   <ma>/data/soll/test_architecture.py
> ```
>
> **Kontrolllauf K2 und K3 auf B, jeweils eine eigene vollständige Invocation:**
>
> ```sh
> CONFORMANCE_API_KEY=<ollama-dummy-key> \
> CONFORMANCE_BASE_URL=http://localhost:11434/v1 \
> CONFORMANCE_MODEL=qwen2.5-coder:7b \
> node <checker>/packages/triton-conformance/dist/cli.js \
>   --topology <ma>/data/soll/depot_soll.ilograph.yaml \
>   --rules <ma>/data/soll/architecture-rules.yaml \
>   --src-root src --rule-graph diff --base <baseline-sha> \
>   --runs 3 --timeout-ms 240000 \
>   --control-files <ma>/data/soll/control_files.txt \
>   --run-log <out>/control_k2.jsonl --json-out <out>/control_k2.json
> ```
>
> **~~Zweite Zeile (K3):~~ ÜBERHOLT mit Rev. 32**, aus demselben Grund wie die
> K3-Injektionszeile oben. Der Block bleibt als Revisionsnachweis **unverändert** stehen.
>
> ```sh
> CONFORMANCE_API_KEY=<openrouter-api-key> \
> CONFORMANCE_BASE_URL=https://openrouter.ai/api/v1 \
> CONFORMANCE_MODEL=nvidia/nemotron-3-super-120b-a12b \
> CONFORMANCE_PROVIDER_PIN=digitalocean \
> node <checker>/packages/triton-conformance/dist/cli.js \
>   --topology <ma>/data/soll/depot_soll.ilograph.yaml \
>   --rules <ma>/data/soll/architecture-rules.yaml \
>   --src-root src --rule-graph diff --base <baseline-sha> \
>   --runs 3 --timeout-ms 600000 \
>   --control-files <ma>/data/soll/control_files.txt \
>   --run-log <out>/control_k3.jsonl --json-out <out>/control_k3.json
> ```
>
> **Kontrolllauf K3 auf B — KORRIGIERTE FASSUNG, Rev. 32, verbindlich:**
>
> ```sh
> CONFORMANCE_API_KEY=<DO_MODEL_ACCESS_KEY aus ~/ma/.secrets/do.env> \
> CONFORMANCE_BASE_URL=https://inference.do-ai.run/v1 \
> CONFORMANCE_MODEL=nvidia-nemotron-3-super-120b \
> node <checker>/packages/triton-conformance/dist/cli.js \
>   --topology <ma>/data/soll/depot_soll.ilograph.yaml \
>   --rules <ma>/data/soll/architecture-rules.yaml \
>   --src-root src --rule-graph diff --base <baseline-sha> \
>   --runs 3 --timeout-ms 600000 \
>   --control-files <ma>/data/soll/control_files.txt \
>   --run-log <out>/control_k3.jsonl --json-out <out>/control_k3.json
> ```
>
> **Dieser Kontrolllauf ist bereits so ausgeführt worden.** Der archivierte Bestand
> `data/c3b-k3/` ist über den Direktzugang erhoben (`c3b_k3_bericht_kontrolllauf.md` §2,
> Base-URL und Modell wörtlich; `model_version` zeichengleich `nvidia-nemotron-3-super-120b` in
> **156 von 156** Calls, D2 M2). Die überholte Zeile darüber bezeichnet damit einen Lauf, den es
> nie gegeben hat — der Nachzug stellt den Aufschrieb auf das her, was gemessen wurde.
>
> **Codebeleg der Checker-Argumente:** `cliArgs.ts:33-34` führt genau `--topology`, `--rules`,
> `--base`, `--src-root`, `--rule-graph`, `--run-log`, `--runs`, `--timeout-ms`, `--json-out`
> und `--control-files`; `cliArgs.ts:48-57` parst sie, `cli.ts:78-91` reicht sie an den Lauf
> weiter. `cli.ts:42-67` belegt die vier `CONFORMANCE_*`-Variablen sowie Temperatur 0 und Seed
> 42 (`cli.ts:37-39`). `run.ts:115-120`, `run.ts:124-153` und `run.ts:168-208` belegen
> Kontrollliste, Base/Diff, Graphmodus, Ausgabepfade und Wiederholungen;
> `cliExtractor.ts:100-127` belegt die Semantik von `--control-files`. Damit ist keine
> nicht existierende Checker-Option vorregistriert.
>
> **Notwendigkeit von `--src-root src`, vor C4 festgelegt:**
> `relativeFilePathToModulePath` ist eine Funktion von **(Pfad, argv)**
> (`b1_bericht_matchkey.md` D1). Der daraus entstehende Modulname ist das **dritte Segment**
> jedes `match_key`; alle 32 erwarteten Schlüssel hängen daran. Ohne festes `--src-root src`
> wäre die Übereinstimmung zwischen Messlauf und Manifest Zufall statt Registrierung. Diese
> Festlegung muss deshalb vor C4 gelten, weil C4 die Schlüssel berechnet.
>
> **Bewusste Lücken/Nichtanwendbarkeit:** K4 und K5 besitzen keine Checker-Optionen für
> Soll-Pfad, `--src-root`, Graphmodus, `--base`, `--runs`, Timeout, JSON/JSONL-Ausgaben oder
> `--control-files`; ihre Regelpfade sind stattdessen `--config` beziehungsweise der
> pytest-Dateipfad. Für K4/K5 muss die Harness Ausgabe und Exit-Code selbst archivieren; eine
> native strukturierte Ausgabepfad-Option ist im festgelegten Aufrufweg nicht vorhanden.
> `--control-files` steht absichtlich nur im K2/K3-Kontrolllauf und nicht in Injektionsläufen
> oder K1: es speist unveränderte Dateien in den LLM-Pfad (`cli.ts:26-29`), nicht in die
> statischen Baselines. Die CLI hat ferner keine Optionen für Modell, Endpoint, Provider-Pin,
> Temperatur oder Seed; diese Werte kommen ausschließlich aus der Umgebung beziehungsweise
> sind im Code fest (`cli.ts:37-67`).
>
> **Nachtrag (23.08.2026, Rev. 24) — VOLLSTRECKER DER AKZEPTANZREGELN.** Der bisherige Satz
> „Beides prüft die Harness ~~bzw. der Runner~~ je Lauf, nicht der Mensch" wird präzisiert:
> Der Checker-Runner vollstreckt diese Regeln **nicht**. `invalidReasons` kennt nur
> `invalid_final_response`, `transport_failure`, `incomplete_runs` und `skipped_files`
> (`reporter.ts:59-64`); `changed_files_count` fehlt. C3a-Lauf 1b endete deshalb bei
> `changed_files_count: 0` mit Exit 0 und leerem `invalid_reasons`
> (`c3a_bericht_clean_state_audit.md` §2b).
>
> Ab C3b läuft nach **jedem** Aufruf ein Nachlaufskript. Es prüft für Injektionsläufe
> `changed_files_count == 1 ∧ calls_total == 1` und für Kontrollläufe
> `control_files_count == calls_total`. Nur dieses Nachlaufskript vollstreckt beide Regeln;
> die Harness C6 übernimmt dieselbe Prüfung. Ohne bestandene Nachprüfung ist ein Lauf ungültig,
> wird wiederholt und nicht ausgewertet. Der Alttext oben bleibt gestrichen als
> Revisionsnachweis stehen.

> **Nachtrag (23.08.2026, Rev. 23) — C3 ZERFÄLLT IN C3a UND C3b, WEIL DAS BESTEHENSKRITERIUM
> NICHT FÜR ALLE FÜNF KONFIGURATIONEN GELTEN KANN.** Begründung:
> `c3a_bericht_clean_state_audit.md` (Audit vom 23.08.2026, Testrepo `0d65104`, Checker
> `348ca9d`, **kein Modell-Call**); §5 Nachträge Rev. 16 und Rev. 18; §2 Schritt 3.
>
> **C3a — AUDIT, hartes Gate.** K1, K4 und K5 auf der Clean-Baseline `B`. Sollwert **0 Findings**,
> und zwar als Bestehenskriterium: die drei Konfigurationen sind **deterministisch** — dieselbe
> Eingabe liefert dieselbe Ausgabe —, ein Finding auf `B` ist also entweder eine echte Altlast
> oder eine Werkzeugeigenheit, und beide Wege sind in §2 Schritt 3 schon beschrieben (Repo fixen
> bzw. Known Deviation). **Bestanden am 23.08.2026 in EINEM Durchgang:** K1 `--rule-graph full`
> 0 Findings / Exit 0 (`graph_files_count: 73`), K1 `--rule-graph diff` am Leerfall 0 Findings /
> Exit 0, K4 `13 kept, 0 broken`, K5 `24 passed`, Soll-Validator `RESULT: OK` / Exit 0 mit allen
> acht Punkten und (3a)–(3d) eingeschaltet. **Known-Deviations-Liste: leer.**
>
> **C3b — KONTROLLLAUF, Messgröße.** K2 und K3 über die 52 Kontrollmodule
> (`data/soll/control_files.txt`, `--control-files`, `--runs 3`). Das Ergebnis ist die
> **Falsch-Positiv-Rate**, **kein Bestehenskriterium**. Ein 0-Findings-Kriterium wäre hier durch
> die **eigene Vorregistrierung ausgeschlossen**: §5 sagt zwei Meldungen **vorher** an — die
> Adapterfassade (Nachtrag Rev. 16) und die beiden Portregeln auf `orders_services` (Nachtrag
> Rev. 18) —, beide getrennt zu führen. Es gälte sonst als durchgefallen, was das Protokoll
> vorausgesagt hat. Gültigkeitsbedingung des Laufs bleibt allein
> **`control_files_count == calls_total`** (Nachtrag Rev. 22 oben).
>
> **Folge für §2 Schritt 3.** Der dortige Satz „alle fünf Konfigurationen … Sollwert: 0 Findings"
> **bleibt wörtlich stehen** und liest sich ab hier so: **Sollwert für K1/K4/K5**, **Messgröße für
> K2/K3**. Dieselbe Präzisierung trifft Fußnote 4 in §3 (dortiger Nachtrag Rev. 23). Es ist keine
> Absenkung des Anspruchs — der teure Teil des Audits, die Prüfung gegen einen unabhängig
> gemessenen Nullwert, liegt gerade bei den drei deterministischen Konfigurationen, und dort gilt
> er ungemildert.
>
> **DIE LEER-PROMPT-VORBEDINGUNG AUS DEM NACHTRAG REV. 17 IST ERFÜLLT.** Gerendert wurde der
> User-Prompt von `src/depot/orders/repository/legacy_order_index.py`
> (`depot.orders.repository.legacy_order_index`, Komponente `orders_repository`, I25-Träger,
> importfrei), aus `buildPromptContext`/`buildUserPrompt` des Checkerstands `348ca9d`, **ohne
> jeden Client** — es gibt also nicht nur keinen Modell-Call, sondern nichts, was einen führen
> könnte. **Sichtprüfung, wie das Protokoll sie verlangt:** alle fünf Abschnitte stehen
> (`# Changed file`, `## Imports`, `## Signatures`,
> `## Allowed dependency edges touching this component`,
> `## Rules to check (scope includes this component)`), der Importblock ist **leer statt fehlend**
> — die Überschrift steht, es folgt keine Zeile —, die Regelliste trägt alle vier gescopten Regeln
> vollständig bis zum letzten Zeichen von R-SIG-2. Der wörtliche Prompt steht in
> `c3a_bericht_clean_state_audit.md` §5. Als **zusätzlicher** Beleg, nicht als Ersatz: Increment 7
> hat denselben Zweig als Zeichenvergleich gepinnt (`increment7_bericht_control_set.md` §5, Fixture
> und Gegenprobe an echten Daten). Das Protokoll verlangt die **Sichtprüfung**; sie ist hiermit
> durchgeführt und liegt wörtlich vor.

> **Nachtrag (23.08.2026, Rev. 25) — DAS NACHLAUFSKRIPT WEIST JE LAUF BEIDE ZAHLEN GETRENNT AUS.**
> Begründung: §4 Nachtrag Rev. 25. Weil `--rule-graph diff` in den K2/K3-Aufrufzeilen steht, ist
> die Gesamtzahl der Records eines Laufs eine **Summe über zwei Mechanismen**. Das Nachlaufskript
> (Nachtrag Rev. 24) protokolliert deshalb je Lauf **zwei** Zahlen:
>
> - die Zahl der Records mit `rule_id`-Präfix `DERIVED:` — der deterministische Pfad,
> - die Zahl der Records mit jedem anderen `rule_id` — der LLM-Pfad.
>
> **Eine Auswertung, die nur die Gesamtzahl führt, ist ungültig.** Der Filter aus §4 Nachtrag
> Rev. 25 ist damit die **erste Stufe** des Joins, vor jeder Metrikberechnung; die Harness C6
> übernimmt dieselbe Trennung. Die beiden Lauf-Akzeptanzregeln (`changed_files_count == 1 ∧
> calls_total == 1` für Injektionsläufe, `control_files_count == calls_total` für Kontrollläufe)
> bleiben unverändert — sie zählen Dateien und Calls, nicht Records.

> **Nachtrag (24.08.2026, Rev. 26) — BEIDE LAUF-AKZEPTANZREGELN TRAGEN DEN
> WIEDERHOLUNGSFAKTOR.** Begründung: `k2_machbarkeitslauf_bericht.md` §4, §10.
>
> `calls_total` (`reporter.ts`, `CallTally.total`) akkumuliert **über alle Repetitionen** eines
> Laufs (`run.ts:169-206`) und zählt **jeden** Modellaufruf **jeder** Repetition, nicht nur den
> ersten. Die beiden bisher registrierten Fassungen der Akzeptanzregeln —
> `changed_files_count == 1 ∧ calls_total == 1` (Amendment 12.08.2026) und
> `control_files_count == calls_total` (Nachtrag Rev. 22) — gelten **nur für `--runs 1`**; die
> registrierten Aufrufzeilen selbst (Nachtrag Rev. 24) schreiben **`--runs 3`** vor. **Korrigierte
> Fassung:**
>
> - **Injektionslauf:** `changed_files_count == 1 ∧ calls_total == 1 * runs`
> - **Kontrolllauf:** `calls_total == control_files_count * runs`
>
> Der alte Wortlaut bleibt an beiden Stellen gestrichen stehen, als Revisionsnachweis. **Gemessen**
> in allen fünf Läufen des Machbarkeitslaufs: `calls_total: 3` bei `control_files_count: 1` und
> `--runs 3` (`k2_machbarkeitslauf_bericht.md` §4, alle fünf `run_footer`-Records).
>
> **Was die alte Fassung gekostet hätte:** Bei `--runs 3` ist `calls_total` für **jeden**
> Injektionslauf gleich **3**, nie **1** — die alte Injektionsregel `calls_total == 1` hätte damit
> **jeden der 32 Injektionsläufe** als ungültig verworfen und nach dem Nachtrag Rev. 24 zur
> Wiederholung geschickt, mit einer Wiederholung, die am selben Rechenfehler erneut gescheitert
> wäre. Die Meldung des Nachlaufskripts hätte dabei auf ein **Datenproblem** hingedeutet (ein
> vermeintlich fehlgeschlagener oder unvollständiger Lauf), nicht auf einen **Rechenfehler in der
> Regel** selbst.
>
> **Codebefund zu `runLog.ts:85-86`:** Die dortige Formulierung der Kontrolllauf-Invariante
> (`control_files_count == calls_total`) steht im **JSDoc-Kommentar** des Felds
> `control_files_count`, nicht in ausführbarem Code — sie wird an dieser Stelle **nur
> dokumentiert, nicht geprüft**. Ein Vermerk genügt; es ist **kein** getrennt zu meldender
> Codebefund.

> **Nachtrag (24.08.2026, Rev. 26) — EXIT-CODE IST KEIN GÜLTIGKEITSKRITERIUM.** Begründung:
> `k2_machbarkeitslauf_bericht.md` §4.
>
> Gemessen im Machbarkeitslauf: Lauf 2 (0 Findings) endet mit **Exit 0**, die vier Läufe mit
> Befund (Lauf 1, 3, 4, 5) mit **Exit 1**. Der Exit-Code kodiert **„Findings vorhanden"**, nicht
> **„Lauf fehlgeschlagen"**. Das Nachlaufskript (Nachtrag Rev. 24) darf ihn **nicht** als
> Gültigkeitskriterium verwenden — sonst gälte in der Kampagne **jeder** Lauf mit Treffer als
> fehlgeschlagen, und mit ihm alle Injektionsläufe der Kategorien, die K2/K3 gerade finden sollen.
> Gültigkeit bemisst sich stattdessen an `invalid_reasons`, `calls_invalid`,
> `calls_transport_failed` und den beiden Zählregeln aus dem Nachtrag oben.

> **Nachtrag (24.08.2026, Rev. 27) — POOLBEFUND UNTER DEM K3-MACHBARKEITSLASTPROFIL.**
> Begründung: `k3_machbarkeitslauf_bericht.md` §4, §5, §15.
>
> Fünf getrennte Einzeldatei-Invocationen (je drei Repetitionen, 30 s Pause dazwischen — ein
> Fünfzehntel der C3b-Last, vollständig entkoppelt) gegen den gepinnten Provider
> `digitalocean`: **drei von fünf** brechen mit `invalid_reasons: ["transport_failure"]` ab
> (Lauf 3, 4, 5), **6 von 15** angeforderten Calls erreichen das Modell nie. Alle drei Abbrüche
> sind nach §7 (Stop-Regeln, API-Fehler) **gültige Ergebnisse**, keine Fehlschläge der
> Durchführung. `--control-files`/`control_files_count` bleiben unverändert Bestandteil des
> Messpfads; die Akzeptanzregel des Kontrolllaufs (`control_files_count == calls_total * runs`,
> Nachtrag Rev. 26) ist von diesem Befund **nicht** berührt — sie bemisst Gültigkeit je
> Invocation, nicht die Ausfallursache. Vollständige Umgebungs- und Ursachenanalyse in §1,
> Nachtrag Rev. 27 (Poolbefund K3).

> **Nachtrag (25.08.2026, Rev. 29) — DER DESKRIPTIVE VOLLBILD-COMMIT FEHLT NOCH; ER IST OFFEN.**
> Begründung: `repo-kontext/c4b_bericht_injektionen.md` §11 Punkt 4.
>
> Das Amendment vom 12.08.2026 oben registriert **einen zusätzlichen Commit mit allen 32
> Injektionen** (Elternteil `B`, **kein Merge**) für einen **deskriptiven Vollbild-Lauf** von K1,
> K4 und K5. **C4b hat ihn nicht gebaut**: sein Auftrag war ausdrücklich auf „32 Commits und 32
> Refs" begrenzt und nennt den Vollbild-Commit nicht. Gebaut sind daher **32**, nicht 33.
>
> **Als OFFEN geführt, mit drei Vermerken:**
>
> - **Er geht in KEINE Metrik ein.** Er wird nicht gegen das Manifest gejoint, die
>   Lauf-Akzeptanzregel `changed_files_count == 1 ∧ calls_total == 1 * runs` gilt für ihn nicht
>   (Amendment 12.08., Nachtrag Rev. 26); berichtet wird qualitativ (UF4,
>   Ausgabegranularität; Amendment 13.08.).
> - **Er blockiert weder C4c noch die Kampagne.** C4c trägt die SHAs der **32** Injektionen ins
>   Manifest und prüft je Injektionscommit vor; die Messläufe K1–K5 fahren über dieselben 32.
>   Der Vollbild-Lauf ist ein **zusätzlicher** Beobachtungsgegenstand, keine Voraussetzung.
> - **Er ist mechanisch aus den 32 Tags herstellbar**, weil die Injektionen **verschiedene
>   Dateien** betreffen: 32 paarweise verschiedene Trägermodule, kein Modul zweimal
>   (`c4b_bericht_injektionen.md` §8.2). Die 32 Änderungen sind damit konfliktfrei auf `B`
>   zusammenzulegen; es entsteht **ein** Commit mit `B` als einzigem Elternteil, kein Merge.
>
> **Eigener Auftrag.** Er wird nicht in C4c mitgeführt und nicht stillschweigend nachgeholt.

> **Nachtrag (26.08.2026, Rev. 30) — AUFZEICHNUNGSAUFLAGEN FÜR C7.** Begründung:
> `d2_bericht_vormessungen.md` M5 und M6 (Trockenlauf der Auswertungsspezifikation gegen die
> beiden archivierten Bestände); `c6_auswertungsspezifikation.md` §8 Punkte 4 und 6, §10.3,
> §10.4; §5 Nachtrag Rev. 30.
>
> **Zusätzlich** zu den bestehenden Auflagen dieses Abschnitts — die unverändert fortgelten —
> schreibt C7 je Kampagnenlauf auf:
>
> **(1) Externe Wanduhrzeit je Invocation, für alle fünf Konfigurationen.** Monotone Uhr,
> Subprozess-Start bis -Ende, in dasselbe Laufmanifest wie die übrigen Invocationsdaten
> (Feldform analog `duration_s` der C3b-Kontrollläufe). Ohne sie ist die Kostentabelle nach §5
> Nachtrag Rev. 30 nicht bildbar; für K4 und K5 existiert **keine** andere Quelle.
>
> **(2) stdout UND stderr jedes K4- und jedes K5-Aufrufs, wörtlich und vollständig, neben das
> Laufmanifest.** Nicht gekürzt, nicht als `stdout_tail`, nicht vorverarbeitet. Begründung:
> K4 und K5 kennen keinen `match_key`; ihre Trefferkriterien sind Vergleichsvorschriften auf
> der **Textausgabe** (Mengenregel für K4/`CYCLE`, Test-ID plus `AssertionError`-Text für K5,
> §6.1/§6.2 der Auswertungsspezifikation). Liegt die Ausgabe wörtlich vor, ist die
> K4/K5-Matchregel **nachträglich beliebig oft anwendbar** — auch mit einer später
> präzisierten Regel, ohne Neumessung. Damit ist **Punkt 4 der Auswertungsspezifikation**
> (§10.4: die Matchregeln liegen im Manifest nur als Prosa je Injektion vor, nicht als
> generische Vergleichsfunktion) **nicht kampagnenblockierend** — er wird zu einer Frage der
> Auswertung, nicht der Messung. Der Punkt selbst bleibt offen und wird hier **nicht**
> entschieden.
>
> **(3) Absoluter Pfad des Testrepositoriums, `cwd` der Invocation und Maschinenkennung ins
> Laufmanifest.** Begründung: der `match_key` ist Funktion von (Pfad, argv)
> (`pythonCodeModel.ts:56-79`), und die K5-Modulnamen hängen am `root_path` (V17). In den
> C3b-Läufen ist **keines** dieser drei Felder aufgezeichnet — belegt im Trockenlauf über beide
> `run_manifest.json`. Als **Referenzwerte** gelten die in `d2_bericht_vormessungen.md` M5(d)
> protokollierten Angaben:
>
> ```
> abs_repo_path : /home/haasentimo/ma/ma-conformance-testrepo
> cwd           : /home/haasentimo/ma/ma-conformance-testrepo
> uname -a      : Linux DESKTOP-PJA89CF 5.15.153.1-microsoft-standard-WSL2 #1 SMP
>                 Fri Mar 29 23:14:13 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
> python3       : Python 3.12.3
> node          : v22.23.2
> dist/cli.js   : c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95
> ```
>
> **(4) Alles aus der Liste NICHT AUFZEICHNUNGSGEDECKT** der Feldabdeckungsprüfung
> (`d2_bericht_vormessungen.md` M6), soweit dort nach Anwendung der Punkte (1) bis (3) noch
> etwas steht. **Stand 26.08.2026: nach (1) bis (3) leer** — die drei Lücken, die der
> Trockenlauf gefunden hat, sind genau die Punkte (1), (2) und (3) oben.
>
> **Was der Trockenlauf ausdrücklich bestätigt hat** und was C7 deshalb **nicht** zusätzlich
> aufzeichnen muss: der Mechanismusfilter (`rule_id`), `strict` (`match_key`), `localized`
> (`component`/`module`/`category`), Median und Spannweite (`run_index` 0/1/2 in allen 52
> Dateien beider Bestände), die FP-Rate mit Nenner 52, die beiden vorregistrierten Meldungen
> (über `rule_id` identifizierbar), beide Lauf-Akzeptanzregeln (52/52 erfüllt in beiden
> Beständen) und die Liste ungültiger Läufe (`invalid_reasons`, `calls_*`, `attempt`) sind in
> der bestehenden Aufzeichnung **vollständig gedeckt**.

> **Nachtrag (26.08.2026, Rev. 31) — DER GRAPHMODUS WIRD AUS DER KATEGORIE ABGELEITET UND JE
> LAUF INS LAUFMANIFEST GESCHRIEBEN.** Begründung: `c4c_bericht_vorabpruefung.md` Teil B (B2);
> Absatz „Graphmodus je Kategorie für K1" oben (Rev. 7), Begründung ersetzt durch das
> Amendment 13.08.
>
> **Der Bestand.** Die C4c-Gegenprobe hat die Zuordnung **wortgleich zum Protokoll** gefahren:
> I01–I12 (`FORBIDDEN_RELATION`) mit `--rule-graph diff`, I13–I16 (`CYCLE`) mit
> `--rule-graph full`, `--base` in beiden Fällen der Baseline-SHA. Ihr Ergebnis — **16 von 16**
> erwarteten `match_key` zeichengleich gemessen — attestiert die Kampagne **nur unter genau
> dieser Zuordnung**.
>
> **Auflage für C7.** Der Graphmodus wird **aus der Kategorie des Injektionseintrags
> abgeleitet** (`category_l1` des Manifesteintrags → `full` bei `CYCLE`, sonst `diff`),
> **nicht per Aufrufzeile gesetzt**. Der abgeleitete Wert wird **je Lauf ins Laufmanifest
> geschrieben**, neben den bereits registrierten Aufzeichnungsauflagen (Nachtrag Rev. 30).
>
> **Warum das eine Auflage und keine Stilfrage ist.** Ein per Hand gesetzter Modus ist eine
> Aufrufzeile, die von der Kategorie abweichen **kann**; ein abgeleiteter ist eine, die es
> **nicht kann**. Für die vier `CYCLE`-Injektionen verschiebt ein abweichender Modus die
> **Records-Menge** — im Diff-Modus sieht die Rule-Engine nur die Importe der geänderten Datei,
> ein Ein-Datei-Diff erzeugt genau **einen** Adjazenz-Knoten, und `childState === VISITING`
> tritt nie ein (Amendment 13.08.): I13–I16 fielen dort **stumm** auf null, ohne Fehlermeldung
> und ohne dass die Lauf-Akzeptanzregel anschlüge. Die Aufzeichnung im Laufmanifest macht die
> Zuordnung **nachträglich prüfbar**, statt sie dem Runner-Code zu glauben.
>
> **Keine Änderung** an der Zuordnung selbst, an der Erwartungsmatrix (§3) oder an einer
> Metrik — nur an der Art, wie sie hergestellt und bezeugt wird.

> **Nachtrag (27.08.2026, Rev. 33, C5b) — DER GRAPHMODUS-NACHTRAG REV. 31 GILT FÜR K1;
> WORTLAUT PRÄZISIERT.** Begründung: C5-Planausgabe (`c5_bericht_freeze.md` §8);
> `c4c_bericht_vorabpruefung.md` Teil B; §6 Rev. 7 („Graphmodus je Kategorie **für K1**");
> §4 Nachtrag Rev. 25.
>
> **Was präzisiert wird.** Der Nachtrag Rev. 31 schreibt die Ableitungsregel **generisch**:
> „`category_l1` des Manifesteintrags → `full` bei `CYCLE`, sonst `diff`", ohne die
> Konfiguration zu nennen. Wörtlich gelesen deckte er **12** Full-Läufe — K1, K2 **und** K3 auf
> I13–I16. Gemeint und festgelegt waren immer **4**.
>
> **Der präzisierte Wortlaut, verbindlich:**
>
> - **K1** — `--rule-graph full` bei `category_l1 == CYCLE`, sonst `--rule-graph diff`,
>   abgeleitet aus dem Manifesteintrag und je Lauf ins Laufmanifest geschrieben (Rev. 31,
>   unverändert).
> - **K2/K3** — **immer** `--rule-graph diff`, für **alle 32** Injektionen, ohne Ableitung aus
>   der Kategorie. Das steht seit §6 Rev. 24 in beiden Aufrufzeilen und ist die Grundlage von
>   §4 Nachtrag Rev. 25 (der deterministische Pfad läuft in K2/K3-Läufen mit, weil dort `diff`
>   steht) sowie der konstruktionsbedingten `CYCLE`-Nullzeile für K2/K3 (§6 Rev. 7, Absatz
>   „Asymmetrie").
> - **K4/K5** — die Werkzeuge **kennen den Schalter nicht**; der Modus ist dort `n/a` und wird
>   im Laufmanifest auch so geführt.
>
> **Beleg, nachgezählt statt behauptet.** Die C5-Planausgabe über alle 160 Invocations zählt
> **4 × `--rule-graph full`** (K1 auf I13–I16, den vier `CYCLE`-Injektionen) und
> **92 × `--rule-graph diff`** (K1 auf den übrigen 28, K2 und K3 auf allen 32) —
> 4 + 92 = 96, die drei LLM-fähigen Konfigurationen × 32; die 64 K4/K5-Invocations tragen
> keinen Modus. Dazu C4c Teil B, das I01–I12 mit `diff` und I13–I16 mit `full` gefahren hat
> und dessen 16-von-16-Gegenprobe die Kampagne **nur unter genau dieser Zuordnung** attestiert.
>
> **Die Festlegung ändert sich nicht.** Sie stand so in §6 Rev. 7, ist so gegengeprüft (C4c),
> so geplant (C5) und so implementiert (`campaign_spec.graph_mode` liefert den Modus, und
> `run_campaign.build_matrix` setzt ihn **nur für K1**, für K2/K3 fest auf `diff`, für K4/K5
> auf `None`). Präzisiert ist der **Protokolltext**, der als einziger der vier Stellen
> generisch formuliert war. **Keine Metrikänderung, keine Manifeständerung, keine Matrixzelle
> bewegt sich, kein Messergebnis betroffen.**

> **Nachtrag (26.08.2026, Rev. 32) — (1) DIE K5-AUFRUFZEILE WAR UNVOLLSTÄNDIG REGISTRIERT.**
> Begründung: `c7_abbruch_bericht_aufrufspezifikation.md` A1; `data/soll/test_architecture.py`;
> `c2c_bericht_k5_konfiguration.md` §B4; `c3a_bericht_clean_state_audit.md` §3b;
> `d2_bericht_vormessungen.md` M5(c); `data/soll/MANIFEST.md`.
>
> **Der Befund.** Die in §6 Nachtrag Rev. 24 registrierte K5-Zeile trägt die Umgebungsvariable
> **`DEPOT_SRC` nicht**. Die eingefrorene K5-Konfiguration leitet aus ihr `root_path` **und**
> `module` ab und bricht ohne sie ab — `data/soll/test_architecture.py`, wörtlich:
>
> ```python
> _SRC = os.environ.get("DEPOT_SRC")
> if not _SRC:
>     raise RuntimeError(
>         "DEPOT_SRC must point at the source root <testrepo>/src; "
>         "root_path and module are derived from it as <DEPOT_SRC>/depot."
>     )
> ROOT_PACKAGE = os.path.join(_SRC, "depot")
> ```
>
> **Die Anweisung steht auf Modulebene, nicht in einem Test.** Sie läuft damit in der
> **Sammelphase**: pytest bricht beim Einlesen der Datei ab, und **0 von 23**
> Architekturregeln werden ausgewertet. Die registrierte Zeile ist mithin **nicht
> ausführbar** — kein Grenzfall, sondern ein Lauf, der nie stattfindet.
>
> **Warum das ohne diese Korrektur still bliebe.** K5 schreibt **keinen `run_header`**; die
> beiden bestehenden Lauf-Akzeptanzregeln (`changed_files_count`, `calls_total`) zählen Felder
> des Checker-Laufprotokolls und greifen für K5 **strukturell nicht**. Es gäbe damit **kein**
> Kriterium, das den Abbruch von einem sauberen Lauf trennt. Punkt (3) unten schliesst diese
> Lücke generisch.
>
> **RICHTUNG DER KORREKTUR, ausdrücklich benannt: korrigiert wird der AUFSCHRIEB, nicht die
> Konfiguration.** `DEPOT_SRC=<testrepo>/src` ist in **drei gemessenen Läufen** belegt, alle
> vor dem 26.08.2026, alle **mit** der Variablen:
>
> | Fundstelle | Zeile | Ergebnis |
> |---|---|---|
> | `c2c_bericht_k5_konfiguration.md` §B4 | `DEPOT_SRC=<testrepo>/src python -m pytest -p no:cacheprovider -q data/soll/test_architecture.py` | `24 passed`, Exit 0 |
> | `c3a_bericht_clean_state_audit.md` §3b | `DEPOT_SRC=<baseline>/src venv/bin/python -m pytest -p no:cacheprovider -q data/soll/test_architecture.py` | `24 passed`, Exit 0 |
> | `d2_bericht_vormessungen.md` M5(c) | `DEPOT_SRC=… <venv>/bin/python -m pytest -p no:cacheprovider <ma>/data/soll/test_architecture.py` | `collected 24 items`, `24 passed`, Exit 0 |
>
> `data/soll/MANIFEST.md` führt die Zeile ebenfalls mit der Variablen. **Gemessen wurde immer
> so; unvollständig war allein die Protokollzeile.** **Kein Messergebnis ist betroffen, keine
> Matrixzelle bewegt sich, die K5-Testdatei wird nicht angefasst** — ihr SHA256 bleibt der
> registrierte (§1 Amendment 12.08.).
>
> **`-q` BLEIBT — entschieden, nicht offengelassen.** Grund: der **Schärfenachweis** in
> `c2c_bericht_k5_konfiguration.md` §B5, die empirische Grundlage der K4/K5-Matchregel, ist
> **mit `-q`** gemessen; die dort dokumentierten Ausgabeformen sind die **Referenz** für die
> Rohtextauflage aus §6 Nachtrag Rev. 30 (2). Ein Wechsel der Schalterstellung änderte den
> wörtlich zu archivierenden Rohtext gegenüber genau der Quelle, gegen die er verglichen wird.
> **Für die Auswertung geht nichts verloren:** die `FAILURES`-Sektion mit Test-ID,
> `AssertionError`-Text und dem **schuldigen Modul** erscheint mit und ohne `-q` vollständig;
> `-q` kürzt die Fortschrittsanzeige und den Kopf, nicht den Befund. **Vermerkt:** D2 M5(c) lief
> **ohne** `-q` und lieferte dasselbe Verdikt (`24 passed`, Exit 0) — die Schalterstellung ist
> ergebnisneutral und wird hier allein wegen der Rohtext-Referenz festgelegt.

> **Nachtrag (26.08.2026, Rev. 32) — (2) DIE K3-AUFRUFZEILEN SIND AUF DEN DIREKTZUGANG
> GEZOGEN.** Begründung: §1 Nachtrag Rev. 30 (K3-Zugangsweg registriert);
> `k3_machbarkeitslauf_direktzugang_bericht.md` §3; `c3b_k3_bericht_kontrolllauf.md` §2;
> `c7_abbruch_bericht_aufrufspezifikation.md` A2; B32.
>
> **Der Befund.** §6 Nachtrag Rev. 24 registriert für K3 — sowohl in der Injektions- als auch in
> der Kontrolllaufzeile — `CONFORMANCE_BASE_URL=https://openrouter.ai/api/v1`,
> `CONFORMANCE_MODEL=nvidia/nemotron-3-super-120b-a12b` und
> `CONFORMANCE_PROVIDER_PIN=digitalocean`. §1 Nachtrag **Rev. 30** erklärt demgegenüber
> `https://inference.do-ai.run/v1`, `nvidia-nemotron-3-super-120b` und **keinen** Pin für
> **verbindlich**. Rev. 30 hat dabei nur die **Matrixzeile** in §1 gestrichen; die
> **Aufrufzeilen** in §6 blieben stehen. **Das Protokoll trug seither zwei verbindliche
> K3-Zeilen.**
>
> **Sachlich war der Widerspruch durch Revisionsvorrang aufgelöst, dokumentarisch nicht** — und
> ein Runner, der die vorregistrierten Zeilen wörtlich übernimmt, hätte zwischen ihnen **wählen**
> müssen. Genau diese Wahl darf er nicht haben: sie ist der Unterschied zwischen einem Messpfad,
> der auf **Vorregistrierung** ruht, und einem, der auf der **Auslegung** des Ausführenden ruht
> (dieselbe Lückenklasse wie im Amendment 12.08. zum Konfigurations-Freeze).
>
> **Beide Blöcke oben sind entsprechend nachgezogen**, Alttext je gestrichen und unverändert
> stehen gelassen. **Der Kontrolllauf ist bereits über den Direktzugang gefahren worden:**
> `data/c3b-k3/` ist mit Base-URL und Modell des Direktzugangs erhoben
> (`c3b_k3_bericht_kontrolllauf.md` §2, Aufrufzeile wörtlich), und `model_version` steht in
> **156 von 156** Calls zeichengleich auf `nvidia-nemotron-3-super-120b` (D2 M2). Die überholte
> Zeile bezeichnete damit einen Lauf, den es **nie gegeben hat**.
>
> **Kein `CONFORMANCE_PROVIDER_PIN`, und das ist keine Auslassung.** Ohne Router gibt es nichts
> zu pinnen (B32); `cli.ts:50` liest `process.env.CONFORMANCE_PROVIDER_PIN || undefined`,
> `provider_pin` im `run_header` bleibt `null` und `provider_served` je Call `null` — **Datenlage,
> kein Ausfall** (§1 Nachtrag Rev. 30). **Keine Metrik, keine Matrixzelle und kein archiviertes
> Ergebnis bewegt sich**; T14 (§9) bleibt in vollem Umfang bestehen.

> **Nachtrag (26.08.2026, Rev. 32) — (3) POSITIVE LAUF-AKZEPTANZREGEL FÜR K4 UND K5.**
> Begründung: `c7_abbruch_bericht_aufrufspezifikation.md`; Nachtrag Rev. 31 (Graphmodus) und
> Nachtrag Rev. 32 (1) oben; `c3a_bericht_clean_state_audit.md` §3a und §3b;
> `d2_bericht_vormessungen.md` M5(c); `data/soll/importlinter.ini`;
> `data/soll/test_architecture.py`.
>
> **Warum eine neue Regel nötig ist.** Die beiden bestehenden Lauf-Akzeptanzregeln —
> `changed_files_count == 1 ∧ calls_total == 1 * runs` (Injektionslauf) und
> `calls_total == control_files_count * runs` (Kontrolllauf) — zählen Felder des
> **Checker-Laufprotokolls**. **K4 und K5 schreiben keines davon**; sie hatten damit bisher
> **kein positives Gültigkeitskriterium** überhaupt. Der Graphmodus (Rev. 31) und `DEPOT_SRC`
> (Punkt (1) oben) sind zwei Instanzen **derselben Ausfallklasse**: eine Fehlkonfiguration, die
> **null Findings ohne Fehlermeldung** erzeugt. Für K1/K2/K3 fängt die Zählregel diese Klasse ab,
> für K4/K5 fing sie bisher **nichts**.
>
> **FESTLEGUNG, je Invocation, vor der Auswertung:**
>
> - **K5 — die Anzahl GESAMMELTER Tests muss 24 betragen, und die Sammelphase muss fehlerfrei
>   abgeschlossen sein.** Der Sollwert ist aus `data/soll/test_architecture.py` bestimmt:
>   **19** Erlaubnislistenregeln (`ALLOW_LIST_RULES`, parametrisiert über die 19 Schlüssel von
>   `COMPONENTS`) **+ 4** Portregeln (`PORT_RULES`, parametrisiert über `PORT_CARRIERS`)
>   **+ 1** Wächtertest (`test_k5_1_no_rule_names_a_locked_module`, prüft Bauvorschrift K5-1 und
>   ist **keine** Architekturregel) = **24**. Gegengeprüft: C3a §3b `24 passed`, D2 M5(c)
>   `collected 24 items` / `24 passed`, C2c §B4 `24 passed`.
> - **K4 — die Anzahl AUSGEWERTETER Contracts (`kept + broken`) muss 13 betragen.** Der Sollwert
>   ist aus `data/soll/importlinter.ini` bestimmt: **13** `[importlinter:contract:*]`-Abschnitte
>   (`spine`; `skip-{identity,orders,billing}-{api,services}`, sechs, mechanisch aus der
>   Schichtliste abgeleitet nach §1 Rev. 13; `adapters-internal`;
>   `orders-billing-independent`; `acyclic`; `exhaustive-{identity,orders,billing}`).
>   Gegengeprüft: C3a §3a `Contracts: 13 kept, 0 broken`, zeichengleich mit
>   `c2b_bericht_k4_konfiguration.md` §B3/§B11.
>
> **AUSDRÜCKLICH: geprüft wird, dass das Werkzeug seine REGELMENGE gelesen hat — nicht, wie viele
> Verstösse es gefunden hat.** Die Trefferzahl ist die **Messung** und bleibt **unangetastet**;
> `broken` darf jeden Wert von 0 bis 13 annehmen, `failed` jeden von 0 bis 24, ohne dass die Regel
> anschlägt. Geprüft wird allein die **Summe**, also die Vollzähligkeit der ausgewerteten Regeln.
> Eine Regel, die auf die Trefferzahl zielte, wäre ein Bestehenskriterium und stünde im
> Widerspruch zu §5 und zum Nachtrag Rev. 23 (C3b als Messgrösse).
>
> **Rechtsfolge, analog zu den bestehenden Regeln:** eine Verletzung macht den Lauf **ungültig**,
> er wird **wiederholt und nicht ausgewertet**. Vollstreckt wird die Regel vom Nachlaufskript
> (Nachtrag Rev. 24), das dazu die nach Rev. 30 (2) ohnehin wörtlich abgelegten stdout/stderr
> liest — **keine zusätzliche Aufzeichnungsauflage**. **Der Exit-Code bleibt kein Kriterium**
> (Nachtrag Rev. 26): K4 endet bei gebrochenem Contract mit Exit 1, K5 bei fehlgeschlagenem
> Assert ebenso, und beides ist gemessenes Normalverhalten.
>
> **Für den deskriptiven Vollbild-Lauf gilt auch diese Regel nicht** — wie schon für die beiden
> bestehenden (Amendment 12.08., Nachtrag Rev. 29). Die Regelmenge ist dort zwar dieselbe, aber
> der Lauf geht in keine Metrik ein und wird nicht gejoint.

> **Nachtrag (26.08.2026, Rev. 32) — SCHREIBFORM DES K4-AUFRUFS, FESTGELEGT.** Begründung:
> `c7_abbruch_bericht_aufrufspezifikation.md`, Abschnitt „K4-Pfadform".
>
> Für K4 stehen zwei wirkungsgleiche Schreibformen nebeneinander: §6 Nachtrag Rev. 24 registriert
> `PYTHONPATH=src` mit **absolutem** `--config` bei `cwd = <testrepo>`, während
> `c2b_bericht_k4_konfiguration.md` §B3/§B11 und `c3a_bericht_clean_state_audit.md` §3a
> `PYTHONPATH=<baseline>/src` mit **relativem** `--config` bei `cwd = <ma>` protokollieren. Unter
> dem in §6 festgelegten Arbeitsverzeichnis `<testrepo>` lösen beide auf **dieselben absoluten
> Pfade** auf (`PYTHONPATH=src` → `<testrepo>/src`, relative `PYTHONPATH`-Einträge werden beim
> Start des Interpreters gegen das `cwd` aufgelöst).
>
> **Festgelegt wird allein die Schreibform, nicht die Konfiguration:** der Runner verwendet die
> **in §6 Rev. 24 registrierte Form** — `PYTHONPATH=src`, absolutes `--config`, `cwd = <testrepo>`,
> `--no-cache`. Damit muss C7 nicht wählen, und die Zeile im Laufmanifest ist zeichengleich mit
> der Registrierung. **Keine Revision der K4-Konfiguration**, kein bewegter Hash, kein bewegtes
> Ergebnis; `data/soll/importlinter.ini` bleibt unberührt.

---

## 7. Entscheidungs- & Stop-Regeln

- **Eine-Iteration-Regel:** kein Prompt-Tuning nach Sichtung von Evaluationsdaten
  (Fortsetzung der Disziplin aus Befund 04, Konsequenz 1).
- **Validitäts-Gate:** liegt `valid_final` einer LLM-Konfiguration unter 0.9, wird das als
  Befund dokumentiert und die Konfiguration mit den vorhandenen validen Läufen ausgewertet —
  nicht nachgebessert. Operationalisierung: `valid_final=false`-Läufe sind über Exit-Code 3
  bzw. das persistierte Run-Log (CLI-Inkremente 2 und 4) identifizierbar; stille Zählung
  invalider Läufe als „0 Findings" ist damit ausgeschlossen.
- **API-Fehler** (Timeout, 429): betroffenen Call wiederholen, im Log kennzeichnen;
  systematischer Ausfall → Lauf abbrechen, neu starten, beides protokollieren.
- **Ergebnis widerspricht Erwartungsmatrix:** dokumentieren und diskutieren. Die Matrix wird
  nicht rückwirkend angepasst.
- **Scope-Gate (Variante C → A, festgelegt 18.07.):** Stichtag **31.08.2026**. Sind die
  K1–K5-Läufe abgeschlossen und ausgewertet (oder Verzug ≤ 1 Woche), bleibt Variante C
  (Z2-Regelableitungsstudie nach `z2_protokoll_regelableitung.md` wird ausgeführt). Andernfalls
  automatischer Rückfall auf Variante A — ohne neue Diskussion; die Z2-Studie wandert nach
  Future Work, der Kapitel-1-Präzisierungsabschnitt adressiert die Titellücke aktiv.
  ~~Kürzungsreihenfolge bei Verzug: zuerst Z4 (Transfer-Demonstration), dann erst Z2.~~
  — **gestrichen am 31.08.2026 (Auftrag G1, Rev. 46).** Die Reihenfolge konnte nie zur
  Anwendung kommen: der Gate ist ein binärer Kalendermechanismus zum Stichtag 31.08. und
  liegt konstruktiv **vor** Z4s Slot (Arbeitsplan Rev. 1, Block 6: 11.09.); am Stichtag ist
  Z4 noch nicht gelaufen, und ein negativer Ausgang streicht unmittelbar Z2. **Z4 wird
  eigenständig entschieden, nicht über den Gate.** Damit ist die seit dem 04.08.2026 in
  `00_stand_und_entscheidungen.md` §3 offene Inkonsistenz aufgelöst.

> **ENTSCHIEDEN AM TERMIN — 31.08.2026 (Auftrag G1, Rev. 46).** Der Gate ist am Stichtag
> geprüft und entschieden: **das Kriterium ist erfüllt, Variante C bleibt, Z2 fällt
> nicht.** Belege je mit Fundstelle in `docs/planung/gate_notiz_2026-08-31.md` — die
> Kampagne K1–K5 ist am 27./28.08.2026 gefahren, **32 von 32 gültige Injektionen je
> Konfiguration** (`c10_bericht_kampagne.md` §2.1 und §4.1), in **vier** Läufen ausgewertet,
> **kanonisch `c14_eval_full`** (`data/campaign/eval/README.md`), und in **Befund 08**
> berichtet (`docs/befunde_log.md`, 28.08.2026). Der Rückfall auf Variante A **tritt nicht
> ein**; die drei dafür vorgesehenen Folgeposten bleiben als Vorsorge benannt (Gate-Notiz
> §7). **Zur Ehrlichkeit des Mechanismus gehört der Vorlauf:** am 26.08.2026 war das
> Kriterium **nicht** erfüllt — kein Kampagnenlauf existierte, das Protokoll stand als
> **Rev. 32** noch im Entwurf —, und die Kampagne wurde erst am 28.08. abgeschlossen, drei
> Tage vor dem Termin. **Die zweite Bedingung aus `00_stand_und_entscheidungen.md` §4 ist
> NICHT erfüllt** — Anhang A des Z2-Protokolls ist ein Platzhalter; daraus folgt keine
> Streichung, sondern eine gestufte Bedingung mit vorab gesetzter Schwelle und den Terminen
> **07.09.2026** (Anhang A und Freeze) und **13.09.2026** (zweite und letzte Entscheidung
> über den Umfang von Z2), Gate-Notiz §5. **Dieses Protokoll ist davon nicht berührt:**
> Z2 hat sein eigenes Protokoll, und Z3 ist abgeschlossen.

> **Nachtrag (24.08.2026, Rev. 27) — SCHLÜSSELVORFALL.** Am 24.08.2026 ist der
> OpenRouter-API-Schlüssel während eines Werkzeuglaufs **einmalig im Klartext** in einer
> Fehlermeldung der Sitzungsausgabe erschienen. Geprüft (`grep -rI` über `docs/`, `data/`,
> `tools/` nach dem Präfix `sk-or-`, 25.08.2026): **kein Treffer** — kein archiviertes Artefakt
> und keine Datei des Repositoriums enthält ihn. Der Schlüssel wurde danach beim Anbieter
> **gelöscht und ersetzt**; die Ablage des neuen Schlüssels liegt außerhalb aller Repositorien
> (§0, `.env`, gitignored). Der Vorfall wird dokumentiert, nicht verschwiegen: ein benannter und
> behobener Zwischenfall ist belegbar, eine Lücke nicht.

---

## 8. Bezug zu Forschungsfragen

> **Korrigiert (Rev. 2, 18.07.):** Die frühere Zuordnung der Kategorie-Ausfälle zu UF2 war
> eine Umdeutung — UF2 ist die Regel-**Ableitungs**-Frage und wird durch die eigenständige
> Z2-Studie (`z2_protokoll_regelableitung.md`) beantwortet, nicht durch dieses Protokoll.
> Kanonische UF-Fassungen: `00_stand_und_entscheidungen.md` §2.

- **UF3:** Overlap-Analyse K1/K4/K5 vs. K2/K3, P/R/F1 pro Kategorie; Kategorie-Ausfälle und
  Falsche-Regel-Fälle aus §4 als Fähigkeitsprofil des LLM-Pfads. Framing: Für die
  **Kantenkategorien** gilt der Non-Inferiority-Vergleich. Bei den übrigen Kategorien ist die
  Lage nach den Messungen aus B9+ **kategorienspezifisch** und nicht mehr entlang
  „strukturell gegen semantisch" zu beschreiben:
  - **Echte Nullzeile** und damit Ausdrucksmächtigkeits-Feststellung, kein Messbefund:
    ~~`CYCLE` bei K5,~~ `SIGNATURE_DEVIATION` bei K4 und K5, `MISSING_PORT_REFERENCE` bei K4,
    `INCORRECT_LOCATION` bei K5, **und `FRAMEWORK_TYPE_IN_SIGNATURE` bei K4 und K5**.
    **Ergänzt Rev. 22 (B40), Nachzug zu Rev. 20:** beide Werkzeuge werten ausschließlich
    Importkanten, und die Injektion lässt die Importmenge unverändert — vor und nach der
    Injektion sehen K4 und K5 dasselbe (Fußnote 4). Ein **Import-Proxy** als Ersatz käme nicht in
    Frage: er widerspräche **R-FRAMEWORK-1**, das den Import ausdrücklich erlaubt (§3 Amendment
    (d)), und erzeugte auf der **sauberen** Baseline **acht Findings** — vier Träger und vier
    Zwillinge, je Werkzeug (K4: `c2b_bericht_k4_konfiguration.md` §B6; K5:
    `c2c_bericht_k5_konfiguration.md` §B6) —, während C3 über alle fünf Konfigurationen **null**
    fordert. Damit ist `FORBIDDEN_SIGNATURE_TYPE` die **einzige** Kategorie, in der allein K2/K3
    etwas finden können: strukturelle Nicht-Abdeckung beider Baselines, kein Werkzeugversagen.
    **`CYCLE` bei K5 ist mit Rev. 22 (B39) aus dieser Aufzählung genommen** — siehe die eigene
    Zeile unten.
  - ~~**Kein** Nullzeilen-Fall, sondern **messbarer False Positive**:
    `FRAMEWORK_TYPE_IN_SIGNATURE` bei K4 und K5 — beide melden das konforme Zwillingsmodul
    mit, weil sie nur den Import sehen.~~ **Mit Rev. 20 zurückgezogen** (Fußnote 4: „keine
    verminderte Precision, sondern **gar keine Messung**") und **mit Rev. 22 (B40) ersetzt**; die
    Kategorie steht jetzt eine Zeile höher. Rev. 20 hatte Komponentenschnitt, B38 und
    Standdokument nachgezogen, **§8 aber nicht** — der Alttext bleibt gestrichen stehen, damit
    der Nachzug sichtbar bleibt.
  - **Ausdrucksmächtigkeitsbefund EIGENER ART (neu Rev. 22, B39):** `CYCLE_SIBLING` und
    `CYCLE_PARENT_CHILD` bei **K5**. K5 meldet `CYCLE_*` an der **richtigen Stelle** unter
    **falscher Kategorie** — die **Erlaubnisliste erreicht die Stelle, das Vokabular erreicht die
    Kategorie nicht**: gemeldet wird die injizierte Rückkante als **nicht gelistete Kante**, nicht
    als Zyklus, weil PyTestArch keine Zyklenregel hat (§3, Fußnote 7;
    `c2c_bericht_k5_konfiguration.md` §B5). Weder Nullzeile noch Treffer — in `strict` kein
    Treffer, in `localized` „richtige Stelle, falsche Kategorie". Für UF3 ist das die
    interessantere Aussage als beide Randfälle: eine **Regelform** kann eine Stelle erreichen,
    die ihr **Vokabular** nicht benennen kann.
  - **Teiltreffer:** `INCORRECT_LOCATION` bei K4 — die Stelle wird gefunden, die Art nicht;
    in `localized` anders bewertet als in `strict`.
  - **Von der Baseline erkannt:** `MISSING_PORT_REFERENCE` bei K5.
  - **Vorab benannter Vergleichsgegenstand (ergänzt 13.08.2026, Rev. 13; präzisiert
    Rev. 14):** die Asymmetrie zwischen der **Erlaubnisliste** des Soll-Modells, aus der K1
    jede nicht gelistete Kante ableitet, und dem **Contract-Vokabular** von K4, das die
    verbotenen Paare nicht vollständig ausdrücken kann (§1, Nachtrag Rev. 13).
    Ausdrucksmächtigkeits-Aussage, kein Messbefund.
    **Präzisierung (Rev. 14, `c2b_bericht_erlaubnislisten.md` §1):** Die Überlegenheit gilt
    gegenüber dem **Contract-Vokabular von import-linter**, **nicht** gegenüber dem
    **Regel-DSL von PyTestArch**. K5 **kann** die Whitelist je Komponente als Erlaubnisliste
    ausdrücken — gemessen mit
    `should_not().import_modules_except_modules_that().are_named([…])`, die je Import und je
    Modul wertet und das schuldige Modul benennt; K4 kann es nicht. Der Befund ist damit
    **kein** Gegensatz „Erlaubnisliste gegen statische Werkzeuge", sondern eine Asymmetrie
    **zwischen den beiden Baselines**, und das ist die genauere und für UF3 interessantere
    Aussage. Dazu die zweite, gegenläufige Asymmetrie aus c2b §2b/§3d: bei **externen**
    Paketen ist K5 feiner (drei adressierbare Knoten aus `sqlalchemy.ext.asyncio`), K4 kennt
    nur die Paketwurzel. Beide Richtungen gehören in die UF3-Auswertung.

  Das G2-Reframing bleibt gültig, gilt aber **je Kategorie und Konfiguration**. Der
  Messbefund ist Existenz und Verlässlichkeit des LLM-Pfads.
- **UF4:** Kosten/Latenz pro Check und Modell; Run-Varianz; roh-vs-final-Validität;
  Grenze „nur Imports + Signaturen sichtbar".
- **UF2:** nicht Gegenstand dieses Protokolls (siehe oben).

---

## 9. Threats to Validity (vorregistriert)

- **T1 Synthetischer Datensatz:** Injektionen sind konstruiert; Übertragbarkeit auf
  gewachsene Verletzungen begrenzt. Gegenposition: nur so existiert Ground Truth — und nur so
  ist Kontaminationsfreiheit garantiert (§2): bei öffentlichen Repos wäre Erkennung aus
  Pretraining-Memorierung nicht von Inferenz unterscheidbar.
- **T2 Autor-Zirkularität:** Dieselbe Person schreibt Regeln und Injektionen. Mitigation:
  Reihenfolge Soll → Regeln → Injektionen (§2), mechanische Injektionsrezepte (§3),
  Erwartungsmatrix vor der Messung fixiert.
- **T3 Selektionsbias der semantischen Kategorien:** `FORBIDDEN_SIGNATURE_TYPE`,
  `STRUCTURAL_PLACEMENT` und `API_CONTRACT` sind so gewählt, dass sie im Extractor-Output
  sichtbar sind. Framing in der Arbeit: Existenznachweis des Mehrwerts unter günstigen
  Bedingungen, keine Aussage über beliebige semantische Regeln. **Mitigation (Decision
  Record P):** Die Auswahl ist literaturgestützt — Abweichungstypen nach Murphy et al.,
  dependency rules gegenüber property rules nach Pruijt et al., DCL und DCL 2.0 —, zwei
  ursprüngliche Kategorien wurden wegen fehlenden Belegs ersetzt, und die Baseline-Zellen
  der Erwartungsmatrix (§3) sind **gemessen** statt aus Dokumentation abgeleitet.
  **Verbleibendes Risiko:** Die Auswahl bleibt eine Auswahl, und `API_CONTRACT` ist die
  einzige Kategorie ohne gemessene Baseline-Zelle.
- **T4 Kleines n:** 32 Injektionen nach der Verteilung in §3 → P/R pro Szenario grobkörnig.
  Bei 3–4 Injektionen je Szenario entspricht eine einzelne Verfehlung 25–33 Prozentpunkten
  (Vermerk in §5). Aussagen entsprechend vorsichtig formulieren; Gesamtzahlen (n=32) und
  Aggregate auf Ebene 1 tragen mehr.
- **T5 Tokenizer-/Kosten-Proxy:** Token-Zahlen je nach Provider-Reporting; `cl100k` nur als
  Proxy, wo der Provider nichts liefert (Kennzeichnung wie in Befund 05).

> **Amendment (12.08.2026) — Begründung: Decision Record P.** **Verworfene Option: Importgraph
> im Prompt.** Ein Prompt mit vollständigem Importgraphen — um `CYCLE` für K2/K3 erkennbar zu
> machen — wurde erwogen und verworfen. Erstens würde der LLM-Pfad **dieselbe Eingabe erhalten
> wie die Rule-Engine**; gemessen würde dann, wie gut ein Sprachmodell eine Tiefensuche
> nachrechnet, die ein DFS in Millisekunden vollständig und korrekt ausführt — eine andere
> Frage, deren Antwort nicht bestritten wird. Zweitens bricht es mit dem diff-basierten Entwurf
> und berührt die Skalierungsaussage aus Befund 05, weil ein vollständiger Graph mit dem Repo
> wächst, ein Diff nicht. Drittens ist die Nullzeile bei `CYCLE` **der Befund, nicht die
> Lücke**. **Vermerk:** Die Kombination aus deterministischer Graphanalyse und LLM-Prüfung in
> einer Pipeline gehört in den **Ausblick**.

> **Amendment (12.08.2026) — Begründung: Decision Record M, c1a, B24, B20.** Fünf Einträge
> ergänzt:
>
> - **T6 Werkzeuginformierte Bauentscheidung (Z2).** Die Benennung der `CYCLE`-Paare richtet
>   sich nach der **Sortierordnung der Rule-Engine** (§3, Z2). Sie verzerrt keine Messung,
>   sondern macht den Ground Truth **benennbar**; die Alternative wäre ein vorregistrierter
>   False Positive in einem sauberen Modul. **Deklariert, nicht verschwiegen.**
> - **T7 Importsyntax.** Das Testrepo schreibt durchgehend `import pkg.modul`, das
>   Vorbildsystem durchgehend `from x import Y`. Grund ist ein **Auflösungsartefakt von
>   PyTestArch 4.0.1** (B9+ B17c), nicht Nachbildungstreue.
> - **T8 Top-Level-Importe.** Das häufigste Zyklusmotiv des Vorbildsystems — gegenseitig
>   verwiesene Mapper-Paare — ist dort über **Funktionsrumpf-Importe** realisiert
>   (`c1a_nachtrag` §4.3) und für den Extractor unsichtbar; das Testrepo verwendet
>   ausschließlich **Top-Level-Importe**.
> - **T9 Messstand nach B4 noch einmal geändert.** Der Messstand wurde nach dem
>   Verifikationslauf B4 erneut geändert (Commit `fe66357`, Decision Record M). Die Änderung
>   berührt `subject`, `match_key` und den LLM-Pfad nicht und ist deterministisch verifiziert;
>   **Befund 06.7 bezeugt jedoch `c493daf`, nicht den gemessenen Stand.**
> - **T10 E2E-Suite nicht vollständig grün.** Zum Freeze-Zeitpunkt fallen **9 Tests** in
>   `tests/e2e/dojo.spec.ts` durch (Diagramm-Layout im Editor). Die Fehlermenge ist am
>   unveränderten Stand identisch (B24-Bericht §5), sie hat **keine Berührung mit dem
>   Messpfad**. Der Messpfad ist die CLI.

> **Amendment (13.08.2026) — Begründung: `planung/c1_komponentenschnitt.md` §2 und §6;
> `c2a_bericht_contract_semantik.md`.** Zwei Einträge ergänzt:
>
> - **T11 Werkzeuginformierte Trägerwahl (Z2′).** Die Wahl der
>   `CYCLE_SIBLING`-Träger — `api ↔ mappers` statt `models ↔ mappers` — folgt **Z2′** und
>   damit dem **Sortierverhalten der Rule-Engine**. Sie verzerrt **keine Messung**, sondern
>   macht den Ground Truth **benennbar**; die Abweichung vom realen Zyklusmotiv (4 von 5
>   realen Zyklen liegen paketintern und sind für K1 unsichtbar, der fünfte auf
>   `models ↔ repository`) ist in §3 benannt. Verschärfung von T6, nicht Ersatz.
> - **T12 Zwei Konfigurationseinstellungen tragen den Clean-State-Audit.** Die K4- und
>   K5-Konfiguration enthält zwei Einstellungen, **ohne die der Clean-State-Audit aus
>   Konfigurationsgründen durchfiele**: `allow_indirect_imports = True` auf den
>   `LAYER_SKIP_CALL`-Contracts und **kein** `exhaustive` auf dem Spine-`layers`-Contract
>   (§1, Amendment 13.08.). Beide sind **vorregistriert** und in der **B38-Prüfliste** mit
>   **Positiv- und Negativfall** zu belegen; die zweite ist **ungemessen** und als Annahme
>   gekennzeichnet.

> **Amendment (24.08.2026) — Begründung: `k2_machbarkeitslauf_bericht.md` §1, §9.** Ein Eintrag
> ergänzt:
>
> - **T13 Maschinenwechsel für K2.** Die Messungen von K2 (Machbarkeitslauf, 24.08.2026)
>   entstehen auf einer **anderen** Maschine als die Vorarbeiten bis C3a (§1 Nachtrag Rev. 26:
>   Ryzen 5 5600X unter WSL2 statt der C3a-Umgebung). **Belegt, nicht angenommen, dass der Wechsel
>   folgenlos ist:** Alle Messeingänge sind per SHA256 gegengeprüft — acht von acht Vergleichen
>   `OK` (`k2_machbarkeitslauf_bericht.md` §1: Build-Hash `c0bbdfeb…d95`, Baseline-SHA
>   `0d65104…` gegen `HEAD`, Checker-`HEAD` `348ca9d` gegen den registrierten Stand, fünf
>   `data/soll`-Dateien gegen `SHA256SUMS`) —, der Checker-Build ist **bitgleich** mit den vier auf
>   dem Notebook gebauten Fassungen trotz anderem Betriebssystem und anderer Node-Version, und die
>   vor dem Wechsel zuletzt gemessenen K4-/K5-Ergebnisse (`13 kept, 0 broken`, 75 Dateien, 90
>   Abhängigkeiten; `24 passed`, C3a) beruhen auf denselben, jetzt erneut hashgeprüften
>   Eingangsdateien und bleiben damit als Referenz gültig. Die einzige inhaltliche Messung dieser
>   Maschine — der K2-Machbarkeitslauf selbst — lief fehlerfrei (§11 des Berichts).

> **Amendment (26.08.2026, Rev. 30) — Begründung: `d2_bericht_vormessungen.md` M1–M4;
> `k3_machbarkeitslauf_bericht.md`; `b36a_bericht_k3_varianzlauf.md`; `befunde_log.md`
> Befund 06.5/06.6.** Ein Eintrag ergänzt:
>
> - **T14 Anbieter- und Endpunktwechsel bei K3.** Die Vormessungen, auf denen die
>   K3-Erwartungen dieses Protokolls ruhen, sind über einen **anderen Zugangsweg** erhoben als
>   den, der gemessen wird. **Befund 06.5/06.6** (Schema-Fähigkeit; kein honorierter `seed`)
>   und **B36a** (Aufspaltung in **zwei** Findings je Verstoss, wechselnder Schema-Zweig — die
>   **empirische Grundlage von Decision Record O**) liefen über **OpenRouter** mit dem Slug
>   `nvidia/nemotron-3-super-120b-a12b`, gepinnt auf `digitalocean`. Gemessen wird der
>   **DigitalOcean-Direktzugang** `https://inference.do-ai.run/v1` mit der Katalog-`id`
>   `nvidia-nemotron-3-super-120b` (§1 Nachtrag Rev. 30).
>
>   **Belegstand.** Der Katalog kennt die angeforderte `id` zeichengleich; das geloggte
>   `model_version` weicht in **156 von 156** C3b-K3-Calls **nicht** vom angeforderten Namen
>   ab (`runLog.ts:270` schreibt dort `model_version_reported` — den Wert, den der Anbieter
>   selbst meldet, **nie** aus dem Anforderungsnamen zurückgefüllt); eine stille Substitution
>   wäre genau hier sichtbar und ist **nicht beobachtet**. Der Slug unterscheidet sich
>   (`nvidia/nemotron-3-super-120b-a12b` gegen `nvidia-nemotron-3-super-120b`), `provider_served`
>   ist auf dem Direktweg durchgehend `null` gegen `DigitalOcean` bei OpenRouter, und
>   `context_length` ist auf beiden Seiten mit 1 000 000 ausgewiesen.
>
>   **Was NICHT belegbar ist und hier auch nicht behauptet wird:** Quantisierung, Präzision,
>   Gewichts-Revision und Serving-Stack-Version sind über die API-Metadaten **nicht
>   ausgewiesen** (die Feldmenge des Katalogs ist erschöpfend `id`, `object`, `owned_by`,
>   `created`, `context_length`, `max_output_tokens`). Ein Tokenizer- oder Verhaltensvergleich
>   über **identische Prompts** ist nicht möglich, weil die OpenRouter-Vormessungen auf
>   **anderen Eingaben** liefen (anderes Wegwerf-Repo, anderer `checker_git_head` `e52ddbe`
>   bzw. `c493daf`, andere `topology_sha256`/`rules_sha256`). **Die Identität der Gewichte ist
>   nicht verifiziert.**
>
>   **Auflage.** Die **B36a-Charakteristik** — Aufspaltung eines Verstosses in zwei Findings,
>   wechselnder Schema-Zweig — ist an den **ERSTEN K3-Kampagnenläufen gegenzuprüfen** und das
>   Ergebnis zu **berichten, gleich in welche Richtung es ausfällt**. Bestätigt sie sich nicht,
>   ist das ein Befund über die Vormessung, kein Anlass nachzubessern: **nicht nachbessern, nur
>   berichten** (Eine-Iteration-Regel, §7).
>
>   **Strukturell dieselbe Lage** wie der bereits geführte Risikoeintrag „Befund 06.7 bezeugt
>   `c493daf`, gemessen wird `348ca9d`": **eine Vormessung bezeugt nicht den Messstand.**
>   T14 ist eine Verschärfung von T13 (Maschinenwechsel), nicht dessen Ersatz — dort war der
>   Wechsel per SHA256-Gegenprobe als folgenlos **belegbar**, hier ist er es **nicht**.

> **Amendment (26.08.2026, Rev. 31) — ZWEI ERGÄNZUNGEN AN BESTEHENDEN THREATS. Begründung:
> `d2_bericht_vormessungen.md` M5(d) und M1; `befunde_log.md` Befund 05.3;
> `c3a_bericht_clean_state_audit.md` §1; `c1b_bericht_ruleengine_verifikation.md`.** Kein neuer
> Eintrag; T13 und T14 oben bleiben unverändert stehen und werden ergänzt:
>
> - **Zu T13 — Node-Version auf dem Messrechner.** Auf dem Messrechner läuft **Node v22.23.2**,
>   in C3a protokolliert war **v22.22.2** (C3a §1; `c1b_bericht_ruleengine_verifikation.md`).
>   Das ist eine **Umgebungsdifferenz zwischen Vorarbeit und Messstand** und wird hier als
>   solche **benannt, nicht verschwiegen**. **Folgenlos**, und zwar belegt statt angenommen:
>   der Gatterbeleg dieses Protokolls ist nicht die Node-Version, sondern der **Build-Hash des
>   gebauten `dist/cli.js`**, und der stimmt **zeichengleich**
>   (`c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95`) — dieselbe Beobachtung,
>   die der Reproduzierbarkeitsbefund in §1 Nachtrag Rev. 26 bereits für einen **grösseren**
>   Toolchain-Unterschied festhält (anderes Betriebssystem, andere Node-Version, bitgleicher
>   Build). Die übrigen Werkzeugstände sind gegen C3a §1 geprüft und **alle identisch**
>   (`import-linter==2.13`, `grimp==3.15`, `PyTestArch==4.0.1`, `pytest==9.0.1`,
>   `networkx==3.6.1`, `PyYAML==6.0.2`, `SQLAlchemy==2.0.52`, Python 3.12.3); die
>   Node-Differenz ist der **einzige** Unterschied.
>
> - **Zu T14 — eine schwache, indirekte Stütze der Gewichtsidentität, mehr nicht.** Der
>   DigitalOcean-Katalog weist für `nvidia-nemotron-3-super-120b` `context_length`
>   **1 000 000** aus (§1 Nachtrag Rev. 30, wörtlich aus `GET /v1/models`). Derselbe Wert steht
>   in **Befund 05.3** für den **bezahlten** OpenRouter-Slug `nvidia/nemotron-3-super-120b-a12b`
>   als Registry-Angabe (dort gegen den `:free`-Slug mit 262 144 abgegrenzt). Zwei
>   **unabhängig erhobene Anbieterangaben** nennen also dieselbe, für dieses Modell
>   ungewöhnliche Fenstergrösse. Das ist eine **SCHWACHE, INDIREKTE** Stütze der
>   Gewichtsidentität und wird ausdrücklich nur als solche geführt: `context_length` ist eine
>   **Serving-Konfiguration**, keine Eigenschaft der Gewichte, sie ist von jedem Betreiber frei
>   setzbar, und beide Angaben stammen aus **Selbstauskünften der Anbieter**, nicht aus einer
>   Messung. **Der Satz aus T14 bleibt unangetastet: die Identität der Gewichte ist nicht
>   verifiziert.** Quantisierung, Präzision, Revision und Serving-Stack bleiben **FEHLT**; die
>   Auflage zur B36a-Gegenprobe an den ersten K3-Kampagnenläufen bleibt in vollem Umfang
>   bestehen.

> **Amendment (26.08.2026, Rev. 32) — EINE ERGÄNZUNG AN T12, KEIN NEUER EINTRAG. Begründung:**
> `c7_abbruch_bericht_aufrufspezifikation.md`; §6 Nachtrag Rev. 31 (Graphmodus) und §6 Nachtrag
> Rev. 32 (1) und (3). T12 oben bleibt unverändert stehen und wird ergänzt:
>
> - **Zu T12 — STILLE NULL DURCH FEHLKONFIGURATION BEI DEN KONFIGURATIONEN OHNE LAUFPROTOKOLL.**
>   T12 benennt bisher zwei Einstellungen, ohne die der Clean-State-Audit **durchfiele** — ein
>   **lauter** Ausfall. Ergänzt wird hier die **gefährlichere Schwester**: eine Fehlkonfiguration,
>   die den Lauf **nicht** durchfallen lässt, sondern **null Findings ohne Fehlermeldung**
>   erzeugt. Zwei Instanzen sind inzwischen belegt, beide **vor** der Kampagne gefunden:
>
>   1. **Graphmodus (Rev. 31).** Ein per Aufrufzeile gesetzter `--rule-graph diff` statt `full`
>      liesse die vier `CYCLE`-Injektionen I13–I16 **stumm** auf null fallen: ein Ein-Datei-Diff
>      erzeugt genau einen Adjazenz-Knoten, `childState === VISITING` tritt nie ein
>      (Amendment 13.08.). Kein Fehler, kein Exit-Code, keine anschlagende Akzeptanzregel.
>   2. **`DEPOT_SRC` (Rev. 32).** Die bis dahin registrierte K5-Zeile ist ohne die Variable
>      **nicht ausführbar**; pytest bricht in der **Sammelphase** ab, **0 von 23** Regeln laufen,
>      und weder Exit-Code noch Ausgabe trennen diesen Fall von einem sauberen Lauf.
>
>   **Das gemeinsame Merkmal ist nicht die Einstellung, sondern die FEHLENDE GEGENINSTANZ.** Für
>   K1/K2/K3 fängt die Zählregel über `changed_files_count`/`calls_total` diese Klasse ab, weil
>   sie eine **positive** Aussage über den Lauf verlangt. **K4 und K5 schreiben kein
>   Laufprotokoll** und hatten deshalb überhaupt **kein** positives Kriterium — dort war jede
>   Fehlkonfiguration dieser Art unsichtbar, nicht nur diese beiden.
>
>   **Ab Rev. 32 generisch abgedeckt:** die positive Lauf-Akzeptanzregel für K4 und K5 (§6
>   Nachtrag Rev. 32 (3)) prüft je Invocation, dass das Werkzeug seine **Regelmenge vollzählig
>   gelesen** hat — K5 **24** gesammelte Tests bei fehlerfreier Sammelphase, K4 **13**
>   ausgewertete Contracts (`kept + broken`). Sie greift damit **unabhängig davon**, welche
>   Fehlkonfiguration die Regelmenge verkürzt hat, und ist keine Reaktion allein auf die beiden
>   bekannten Fälle. **Als Restrisiko benannt:** eine Fehlkonfiguration, welche die Regelmenge
>   **vollzählig** lässt und dennoch das Ergebnis verschiebt, fängt auch diese Regel nicht — dafür
>   bleiben der Konfigurations-Freeze über SHA256 (§1 Amendment 12.08.) und die B38-Prüfliste
>   zuständig.

> **Amendment (01.09.2026, Rev. 48) — NEUER EINTRAG T15. Begründung:**
> `z1_s_bericht_diagnoselauf.md` §6–§8; Archiv `data/z1_s_diagnose/` (51 Dateien,
> `sha256sum -c` Exit 0); `befunde_log.md` Befund 07.3, Nachtrag vom 01.09.2026. T1 bis T14
> bleiben **unverändert stehen**.
>
> - **T15 Ausführungsgeometrie des Inferenzservers — ein Umgebungsparameter, der die Ausgabe
>   bewegt und in keinem Laufrecord bezeugt ist.** Gemeint sind drei Grössen, die der Server
>   beim Laden des Modells festlegt: **`n_ctx`** (`-c`), die daraus **abgeleitete
>   Batchgrösse** (`-b`/`-ub`) und die **KV-Cache-Geometrie**.
>
>   **Belegt, nicht vermutet.** Zwei Diagnoseläufe auf **derselben Maschine**, derselben
>   Ollama-Fassung **0.30.10**, demselben Modell-Blob `sha256:60e05f21…bfc2463`, demselben
>   Chat-Template und mit **token-für-token demselben Erstprompt** (4 095 IDs) haben
>   **verschieden geantwortet** — **1 517 gegen 2 261 Zeichen** —, bei `temperature=0` und
>   `seed=0`. Der eine Lauf war gültig mit **0** Fehlern, der andere ungültig mit **14**
>   Fehlern derselben Klasse in allen drei Versuchen. Verändert war **allein `-c 4096` gegen
>   `-c 16384`** und was der Server daraus ableitet: `-b`/`-ub` **512 gegen 1024**, KV-Cache
>   **224 gegen 896 MiB**. Die Läufe liegen ausserhalb dieses Protokolls und ausserhalb des
>   Z3-Messstands; sie tragen **diesen Threat**, **keine Kennzahl dieser Kampagne**.
>
>   **ABGRENZUNG — DIE VERGLEICHBARKEIT INNERHALB DER Z3-KAMPAGNE IST UNBERÜHRT.** Vier
>   Stücke, jedes einzeln nachprüfbar:
>
>   1. **Alle K2-Läufe liefen auf demselben Fenster**, und es ist **gemessen, nicht
>      angenommen**: `CONTEXT 4096` (**§1 Nachtrag Rev. 26** — kein `num_ctx` gesetzt, Ollama
>      fällt auf sein Default zurück).
>   2. Das **Nachlaufskript prüfte je Call**, dass `tokens_in + tokens_out` unter dem
>      tatsächlich geladenen Fenster bleibt (ebenda) — ohne Eingriff in den Messpfad.
>   3. Die Prompts lagen **weit darunter**: Median **1 346** Token je Check bei Maximum
>      **1 948** (`c14_eval_full.md`, K2-Zeile `1346 (767–1948)`). Keine Annäherung an die
>      Fenstergrenze, keine Kürzung.
>   4. **Kein Messergebnis ist betroffen, keine Metrik, keine Zelle der Erwartungsmatrix.**
>
>   **Was nach dieser Messung NICHT mehr behauptet werden kann:** **Reproduzierbarkeit auf
>   einer anders konfigurierten Serverinstanz.** Gleiche Gewichte, gleiche Binärversion und
>   gleicher Prompt genügen dafür nicht — die Serverkonfiguration gehört zur Bedingung. Für
>   künftige Läufe **ausserhalb** dieses eingefrorenen Messstands ist die Geometrie samt
>   Serverversion und Startparametern aufzuzeichnen; im Z1-Protokoll ist das als
>   **T-Z1-11 (Rev. 6)** registriert.
>
>   **Die Entscheidung aus Rev. 26, `num_ctx` NICHT zu setzen, war richtig und bleibt
>   unangetastet.** Ein Eingriff hätte den **eingefrorenen Messpfad bewegt** — `checker_git_head`
>   ein weiteres Mal — und die effektive Modellkonfiguration geändert; genau das hält Rev. 26
>   fest. Das Fenster als **gemessenen** Umgebungsparameter zu führen statt es zu setzen, ist
>   derselbe Weg, den dieser Threat für die übrigen Geometriegrössen fortschreibt.
>
>   **AUSDRÜCKLICH: dieses Amendment BESCHREIBT, es legt nichts fest** — zulässig nach §0.1
>   Punkt 2 auch nach Messbeginn. Es hält fest, was beobachtet wurde und wie es zu lesen ist,
>   und verschiebt nicht, wogegen gemessen wird. Berührt sind **weder Metrikdefinition noch
>   Injektionsmanifest, Regeldatei, Prompt oder Schema** — die fünf Gegenstände der Sperre.
>
>   **Strukturell dieselbe Lage** wie T13 (Maschinenwechsel) und T14 (Anbieter- und
>   Endpunktwechsel): **eine Umgebungsgrösse, die kein registrierter Anker bezeugt.** Anders
>   als bei T13 ist die Folgenlosigkeit hier nicht über einen Bytevergleich belegbar, sondern
>   über die **Distanz zur Fenstergrenze** (Punkt 3) — und anders als bei T14 ist die
>   bewegliche Grösse **gemessen** statt bloss unbelegt.

---

## 10. Amendments

**Revisionshistorie vor Freeze** (Änderungen am Entwurf, solange keine Messung läuft):

| Rev | Datum | Änderung | Begründung |
|---|---|---|---|
| 2 | 18.07.2026 | Matching auf Manifest-`expected_match_key` (§3, §4); Freeze umfasst Prompt- UND Regel-Hash (§1); Kontaminationsfreiheit als Validitäts-Stärke (§2, T1); Scope-Gate 31.08. (§7); UF-Zuordnung §8 korrigiert (UF2 → Z2-Protokoll); §0 offene Punkte expliziert | Abgleich mit implementiertem Checker (Repo-Analyse 17.07., `matchKey.ts`/`ruleEngine.ts`); Beschlüsse der Review-Session 17./18.07. (`00_stand_und_entscheidungen.md`) |
| 3 | 11.08.2026 | §3 — Vermerk: die Vorhersagen der Erwartungsmatrix gelten für `localized`, für `strict` besteht keine Vorhersage. Die Matrix selbst bleibt unverändert | Decision Record O, Anlass B36a |
| 3 | 11.08.2026 | §4 — zweite Metrik `localized` neben der unverändert fortbestehenden Regel `strict`, mit Deduplizierungsregel und pfadabhängiger Kategorie | Decision Record O, Anlass B36a |
| 3 | 11.08.2026 | §5 — `localized` ist nur zusammen mit der Falsch-Positiv-Messreihe interpretierbar | Decision Record O, Anlass B36a |
| 4 | 11.08.2026 | §6 — Diff-Erzeugung der Kampagne festgelegt (Injektions-Commits, `--base` mit SHA, Working Tree clean als Vorbedingung); Lauf-Akzeptanzregel um `changed_files_count: 0` und fehlenden `run_header` erweitert | B33 |
| 5 | 11.08.2026 | §1 — Versionen der Baseline-Werkzeuge in den eingefrorenen Messstand aufgenommen, `--no-cache` als Ablaufregel | B9+ |
| 6 | 12.08.2026 | §3 Erwartungsmatrix und §3 Kategorientabelle ersetzt (sechs Abweichungstypen, zehn Szenarien, zweistufige Kodierung); Abbildung der alten Kürzel ergänzt; verworfene Importgraph-Option und Aussagekraft bei kleinem n dokumentiert. **Umfang der Ersetzung:** vorher standen dort sechs gleichrangige Kategorien S1 (Schichtüberquerung), S2 (Zirkuläre Abhängigkeit), S3 (Kapselungsbruch), S4 (Unabhängigkeitsverletzung), M1 (Framework-Leakage), M2 (Naming-/Verantwortungskonvention) mit je Definition und Injektionsrezept, **5 Injektionen pro Kategorie = 30**, sowie eine sechszeilige Erwartungsmatrix über dieselben Kürzel mit einer Fußnote (import-linter-Zyklenfähigkeit, vor dem Freeze zu verifizieren). Die Matching-Regeln in §4 sind davon **nicht** berührt. §8 UF3 auf die gemessene, kategorienspezifische Lage umgestellt; §4 Kategorienbezeichner nachgezogen (Regeln unverändert); Träger für `ABSENCE_REQUIRED` in Decision Record P nachgetragen | Decision Record P |
| 7 | 12.08.2026 | §2 — Ähnlichkeit zu `nova-modulith` auf die c1a-Messung gestützt (6 Top-Level-Pakete, Schichtung innerhalb der Kontexte, 15 Kanten mit 190/220 Gewicht auf `core`), Größenordnung 407/349/299 am Commit `559491b`, `alembic` als bewusste Auslassung · §3 — CYCLE-Verteilung auf 3 + 1 geändert, Bauvorschriften **Z1–Z4** für CYCLE-Injektionen, Top-Level-Import-Regel, Regelwortlaut `FORBIDDEN_SIGNATURE_TYPE` auf den Persistenz-/Session-Typ präzisiert · §4 — Matchregel für `CYCLE` (exakter Vergleich für K1, Mengenregel für K4), `expected_co_findings` vorregistriert; **schließt B28** · §6 — **Sternhistorie** statt linearer Kette, deskriptiver Vollbild-Lauf ersetzt den Endzustands-Lauf, **Graphmodus je Kategorie**, Lauf-Akzeptanzregel `changed_files_count == 1 UND calls_total == 1`, Freeze-Tag über SHA · §9 — fünf Threat-Einträge T6–T10 | Decision Record M; Decision Record P, Nachtrag; c1a und c1a-Nachtrag; `c1b_bericht_komponentenschnitt.md`; B20; Revision von B33 |
| 8 | 12.08.2026 | §2 — **Option B ausgeführt**: das Soll deckt den gesamten Messraum ab und listet die **vier Zielorte der `INCORRECT_LOCATION`-Injektionen** (`componentOf` ist ein exakter Lookup, ein Modul an nicht gelistetem Ort ist unmapped und erzeugt keinen LLM-Call); Modulliste **maschinell** aus dem Dateibaum erzeugt plus explizite Phantomliste; **Soll-Validator je Injektionscommit** mit commit-abhängiger erwarteter Differenz, gehört in C3 und als Vorbedingung in C7 · §3 — zwei Rezeptpräzisierungen: **(e)** `INCORRECT_LOCATION` mit vorab gelistetem Zielort und **ohne Importkanten** (sonst wäre die vorregistrierte Zelle K5 = nein falsch), **(f)** `MISSING_PORT_REFERENCE` entfernt Annotation **und Import**, K5 braucht **vier Einzelregeln** wegen der Aggregatsemantik von `should()`; Rezepttabelle entsprechend ergänzt · §6 — `HEAD~1` in Ablaufpunkt 3 auf `--base <Baseline-SHA>` korrigiert · §0 — Punkt 3 (FP-Messreihe) von „entscheiden, ob" auf **Pflicht** umgestellt, Punkt 4 (import-linter-Zyklenfähigkeit) als **erledigt** markiert | Ausführung der Entscheidung Option B; `c1b_bericht_komponentenschnitt.md` Punkte 6 und 7; B9+ Fragen 1, 4 und 5; B33 |
| 9 | 12.08.2026 | §3 — zwei weitere Rezeptpräzisierungen: **(g)** die `layers`-Liste des K4-`exhaustive`-Contracts wird aus dem **Dateibaum der Clean-Baseline** erzeugt, nicht aus der Soll-Modulliste — sonst ist der Zielort deklariert, der Contract läuft KEPT durch und die vorregistrierte Zelle K4 = „teilweise" ist unerfüllbar (gemessen belegt, B9+ Nachtrag Abschnitt 3); Zielort muss **direktes Kind** eines Container-Pakets sein. **(h)** `SIGNATURE_DEVIATION` **ändert die Importmenge nicht** (Builtin oder bereits importierter Typ) — sonst könnten K4/K5 aus dem falschen Grund melden, und die einzige nicht gemessene Matrixzeile ruhte auf einer Annahme. Rezepttabelle entsprechend ergänzt · §0 — toter Verweis „Fußnote ¹ (§3)" in Punkt 4 korrigiert (seit Rev. 6 ist Fußnote ¹ die zu `LAYER_SKIP_CALL`; der Punkt betrifft `CYCLE_SIBLING`/`CYCLE_PARENT_CHILD`) | B9+ Nachtrag Abschnitt 3; B9+ Frage 1; B38; Decision Record P |
| 10 | 12.08.2026 | §1 — der Freeze umfasst zusätzlich die **K4-Contract-Datei** und die **K5-Testdatei**, je mit eigenem SHA256 im Messmanifest; die Änderungssperre ab der ersten Messung gilt auch für sie. Begründung: für K4/K5 **ist** die Konfigurationsdatei die vollständige Regelmenge, und die vier B38-Formulierungsfallen laufen still grün durch — dieselbe Lückenklasse wie bei B27 · §3 — **Contract-Typ je Szenario vorregistriert** (Typebene, Namen erst in C2), mit ausdrücklichem „nicht ausdrückbar" bei `CYCLE_PARENT_CHILD`/K4, `MISSING_PORT_REFERENCE`/K4, `INCORRECT_LOCATION`/K5 und `SIGNATURE_DEVIATION`/K4+K5; K5-Regeln für `MISSING_PORT_REFERENCE` auf **Untermodulebene** (`are_named`), Risikorichtung als fehlgeschlagener Clean-State-Audit benannt · §3 — die drei an Bauvorschriften gebundenen Matrixzellen mit **ᴱ/ᴳ/ᴴ annotiert**, Fußnoten 5 und 6 entsprechend ergänzt; **Matrixwerte unverändert** | B38; B9+ Fragen 1–5 und Nachtrag Abschnitte 1 und 3; Analogie zum Regel-Freeze |
| 11 | 13.08.2026 | §4 — die beiden offenen Amendments aus **Decision Record M.2** eingesetzt: die im Messpfad auftretende Begleitmeldung ist die **`layer-violation` zu einer `CYCLE`-Injektion** (nicht umgekehrt), `expected_co_findings` für `FORBIDDEN_RELATION` **konstruktionsbedingt leer** (Ein-Datei-Diff → ein Adjazenz-Knoten), „identische `location`/`subject`" nur **unter Z2** (Gegenbeispiel 5b), Fundstelle `subject` auf `ruleEngine.ts:155` korrigiert, Bildungsregel als Präfixersetzung auf dem handabgeleiteten Schlüssel (kein Engine-Aufruf), Vorabprüfung zusätzlich auf die Record-**Zahl** 2; **neu, nicht aus M.2:** ein `FORBIDDEN_RELATION`-Finding von K2/K3 auf dem Trägermodul einer `CYCLE`-Injektion ist eine **vorregistrierte Kategorieverwechslung** — kein `CYCLE`-Treffer, kein False Positive, in `localized` als „richtige Stelle, falsche Kategorie" · §6 — Begründung des Diff-Modus-Ausschlusses **ersetzt** (ein Ein-Datei-Diff erzeugt genau einen Adjazenz-Knoten, nicht „ein Zyklus braucht beide Kanten"), der deskriptive Vollbild-Lauf als **positive Messaufgabe** formuliert (Grenze der Handableitbarkeit bei Zyklen über mehr als zwei Komponenten, Erwartungsbild aus dem Kontrolllauf zu Punkt 7) · §2 — **dritter stiller Ausfall**: Soll-Validator prüft `rules[].scope.components` ⊆ `topology.components` (Abbruch) und meldet ungescopte Komponenten (Warnung); `__init__.py` bildet in der maschinell erzeugten Modulliste auf den **Paketnamen** ab · §5 — **`__init__.py`-Module nicht im Clean-Control-Set**, bei Ausnahme getrennt auszuweisen · dokumentweit: `c1b`-Zitate auf den vollen Dateinamen gebracht (zwei gleichnamig präfixierte Berichte) | Decision Record M.2; `c1b_bericht_ruleengine_verifikation.md` Punkte 2, 3, 4, 5, 7 und §8.3; `c1a_bericht_nova_modulith_struktur.md` C2; `b1_bericht_matchkey.md` C3 und E3; B27 |

| 12 | 13.08.2026 | §1 — **K4/K5-Konfiguration auf Contract-Typ- und Einstellungsebene vorregistriert**: `layers` für `LAYER_BACK_CALL` **ohne** `exhaustive` (ungemessene Annahme, sonst bräche der Contract auf der sauberen Baseline an `mappers` als nicht deklariertem Kind), `forbidden` **mit `allow_indirect_imports = True`** für `LAYER_SKIP_CALL` (`forbidden` wertet transitiv, `api → services → repository` ist die legitime Kette), **`protected`** statt `forbidden` für `PROTECTED_MODULE` (direkt-only, sonst ist ein Paket mit privatem Innenleben unkonfigurierbar), `independence` ohne Einstellmöglichkeit (Bedingung liegt im Schnitt, I1), **ein** `acyclic_siblings` mit `ancestors` = Wurzelpaket (`ancestor` je Contract ins Messmanifest), `layers` mit `exhaustive = True` für `INCORRECT_LOCATION`; **K5 `root_path` und `module` auf das Wurzelpaket-Verzeichnis**, sonst ist K5 nicht joinbar · §2 — **vierter Ausfallmodus**, ausdrücklich **nicht still**: `NetworkXError` ist in pytest ein **Error**, kein Failure — laut, aber ergebnislos; **Richtwert korrigiert** auf **19 Pakete, ~70 Dateien, ~50 inhaltstragend** (Tokenrechnung aus Befund 05 **nicht** neu gerechnet, sie galt der verworfenen Ein-Prompt-je-Paket-Variante); **drei Fidelitätsverzichte** vermerkt (kein kontexteigener Verdrahtungs-`core`, keine Kompositionswurzel, `services → models` ausgelassen); **Korrektur** am eigenen Amendment vom 13.08., Punkt (6): Träger der `CYCLE_PARENT_CHILD`-Injektion ist das **Kindmodul**, nicht die `__init__.py` · §3 — **Z2′** als **Verschärfung** von Z2 mit Beweisskizze (Eigenschaft des Algorithmus, keine Fixture-Beobachtung; die Vorabprüfung aus DDR M wird von der Ableitungsstütze zur **Kontrolle**), `CYCLE_SIBLING`-Träger auf **`api ↔ mappers`** (Preis als Abweichung deklariert: nachgebildet wird die **Lage** des Motivs, nicht das Schichtenpaar), Bauvorschrift **I1** (`independence` wertet transitiv und hat keinen Abschalter) und Bauvorschrift **K5-1** (keine K5-Regel nennt ein Modul, das eine Injektion verschiebt oder entfernt); Matrixzelle K4/`PROTECTED_MODULE` als **ᴾ** an den Contract-Typ annotiert, **Matrixwerte unverändert** · §4 — **vorregistrierte K4-Begleitmeldung**: `LAYER_BACK_CALL` wird **zweifach** gemeldet (`layers` **und** `acyclic_siblings`), nicht wegkonfigurierbar, kein False Positive; Form der K4-Zyklusmeldung präzisiert (minimale Entfernungsmenge auf Paketebene, relativ zum `ancestor`, mit Importzähler, ohne Modulnamen; **Liste von Blöcken**, nicht ein Block je Contract) · §5 — Ausnahmeklausel zum Clean-Control-Set **gegenstandslos** (sie ruhte auf dem korrigierten Träger), Auflage bleibt als allgemeine Regel · §9 — **T11** (werkzeuginformierte Trägerwahl nach Z2′) und **T12** (zwei Konfigurationseinstellungen, ohne die C3 aus Konfigurationsgründen durchfiele) | `c2a_bericht_contract_semantik.md`; `planung/c1_komponentenschnitt.md` §2, §3, §4.6, §6, §7 und §9; Decision Record M.2 |

| 13 | 13.08.2026 | §1 — **Nachtrag zum Amendment vom 13.08.: Ableitungsregel der K4-Konfiguration.** Die Zeile zu `LAYER_SKIP_CALL` wird **korrigiert** (sie war mit Fußnote ¹ in §3 nicht deckungsgleich; die Fußnote hat recht): die `forbidden`-Contracts für Schichtsprünge werden **mechanisch aus der Schichtliste** abgeleitet, **nicht aus dem Injektionsplan** — je Container ein Contract für jede Quellschicht mit nicht-benachbarten Schichten unterhalb, mit allen diesen Schichten in `forbidden_modules`; bei vier Schichten **zwei je Kontext**, bei drei Kontexten **sechs** statt drei (= n−2 je Kontext). `allow_indirect_imports = True` gilt für **alle sechs**, sonst brechen sie auf der sauberen Baseline an `api → services → repository → models` und `api → mappers → models`. Begründung über die Arithmetik hinaus: eine Konfiguration, die nur die injizierte Grenze kennt, misst **gegen den Testfall statt gegen die Zielarchitektur** — ohne Wirkung auf den Recall, aber auf die **Vergleichbarkeit mit K1** und die **Falsch-Positiv-Reihe**; die vollständigere Konfiguration ist der **härtere** Test für K4. Dazu das **Prinzip für alle K4/K5-Regeln** (Konfiguration aus Whitelist bzw. Schichtliste, Lücken als Nicht-Abdeckung dokumentieren statt durch engere Konfiguration verdecken) und die **Nicht-Abdeckung**: eine vollständige Spiegelung der Whitelist ist nicht schreibbar (19 Komponenten, dreistellige Menge verbotener Paare gegen eine kleine Zahl von Contract-Typen); nicht ausgedrückt sind insbesondere die `mappers`-Paare außer dem Zyklus-Contract und die kontextübergreifenden Paare jenseits von `independence` · §8 — die Asymmetrie **Erlaubnisliste ↔ Contract-Vokabular** als vorab benannter Vergleichsgegenstand unter UF3, mit Verweis auf §1 Rev. 13 | Deckungsgleichheit mit §3 Fußnote ¹; `c2a_bericht_contract_semantik.md` §1.1c; `planung/c1_komponentenschnitt.md` §3 und §4 |

| 14 | 13.08.2026 | §1 — **Nachtrag: K5 wird als ERLAUBNISLISTE gebaut.** Je Komponente eine Regel `should_not().import_modules_except_modules_that().are_named([Whitelist-Nachbarn])` unter `exclude_external_libraries = True` (**19 Regeln**), die Framework-Regeln über ein **zweites Architekturobjekt in derselben Testdatei** unter `False`; die Zuordnung Regel → Objekt gehört ins Messmanifest. **`should_only` ist ausgeschlossen** — es ist eine **Mengengleichheit** und bräche auf der **sauberen** Baseline, weil es auch die **Benutzung** jedes gelisteten Ziels verlangt (dieselbe Falle wie `exhaustive` auf dem Spine-Contract, auf der K5-Seite). Die gewählte Form wertet **je Import** (vollständige Aufzählung, keine Abschneidung) und **je Modul** (nennt das schuldige Modul) und ist damit auf **Kantenebene** joinbar. **Die Konsequenz ist nicht wählbar:** sie folgt aus dem in Rev. 13 vorregistrierten PRINZIP. **Keine vorregistrierte Matrixzelle verschiebt sich** — die K5-Spalte steht bei allen `FORBIDDEN_RELATION`-Szenarien bereits auf „ja". Ferner: **`include_external_packages = True`** als **erforderliche** K4-Einstellung (die Zelle FP⁴ setzt voraus, dass beide Werkzeuge den Framework-Import sehen), mit drei gemessenen Randbedingungen — externe Importe erscheinen als Kante, aber **auf die Paketwurzel zusammengefasst** (Unterpaket als Contract-Ziel wird abgelehnt); externe Knoten sind **`squashed` ohne ausgehende Kanten** und können daher **keine indirekte Kette** schließen; **keiner** der sechs Skip-Contracts und auch `independence` bricht unter dem Schalter auf der sauberen Menge (`7 kept, 0 broken`, mit und ohne Schalter, beide Regelarten mit Positivkontrolle scharf) · §2 — **Nachtrag:** Zuordnungsregel für die **vier Phantomeinträge** (der Zielort **erbt die Komponente des sauberen Orts**; erst damit ist der `component`-Anteil des `match_key` für I25–I28 berechenbar, und R-PLACE-1 ist für genau diese Komponenten gescopt); Zuordnungsregel für die **fünf Paketmodule** `depot`, `depot.core`, `depot.identity`, `depot.orders`, `depot.billing` an die Komponente **`core`**, nachdem **alle** Pakete eine `__init__.py` erhalten (**keine PEP-420-Namensraumpakete** — Vermeidungsentscheidung gegen ungemessenes grimp-Verhalten an `containers`/`modules`/`ancestors`, deren Ausfall erst **nach** dem Freeze sichtbar würde); Richtwert auf **72–75 Dateien / 50–52 inhaltstragend / 23 Pakete** korrigiert (ausgeführt: 73/50/23); **fünfter Ausfallmodus** — eine K5-Regel auf ein **externes** Modul bricht das Werkzeug ab, sobald der Import verschwindet, weil externe Knoten nur existieren, solange sie importiert werden (K4 hat das Problem nicht) · §3 — **(vi)** R-PLACE-1 ist als **Namensregel** zu formulieren: eine reine Platzierungsregel verschöbe die vorregistrierte Zelle `INCORRECT_LOCATION`/K4 von „teilweise" auf „ja", also eine Matrixzelle durch eine **Regelformulierung** statt durch eine Messung · §8 — UF3-Zeile **präzisiert**: die Erlaubnisliste ist dem **Contract-Vokabular von import-linter** überlegen, **nicht** dem **Regel-DSL von PyTestArch**, das die Whitelist je Komponente ausdrücken kann; dazu die gegenläufige Asymmetrie bei externen Paketen | `c2b_bericht_erlaubnislisten.md` §1, §2, §3; `planung/c1_komponentenschnitt.md` §3.1 und §4.1 Rev. 2; `planung/c1_modulliste.md` Rev. 2; `c1a_bericht_nova_modulith_struktur.md` C2 |
| 15 | **14.08.2026** — bis Rev. 15 mit dem 13.08. datiert; das Datum war im auslösenden Auftrag falsch vorgegeben und ist mit Rev. 16 in §2, §3 und §5 korrigiert, ältere Nachträge bleiben unberührt | §3 — **Nachtrag zu (vi): R-PLACE-1 hat ZWEI Klauseln.** Beide **suffixbasiert**, beide **einseitig** formuliert („Name impliziert Ort", nicht umgekehrt — Paketmodule und suffixlose Module sind unbetroffen). **Klausel 1:** Module auf `_repo`/`_query`/`_index` liegen im `repository`-Paket ihres Kontextes. **Klausel 2 (neu):** Module auf `_models` liegen im `models`-Paket ihres Kontextes. Vorregistriert wird die **FORM**, der Regeltext bleibt C2. Die Endung ist **gemessen**: fünf der sechs inhaltstragenden Module in `iam/models` heißen `*_models.py`, darunter `permission_models.py`; das Testrepo verengt die im Vorbild vorhandenen zwei Endungen (`_models`, `_schemas`) auf eine. Die **beiden Kandidaten aus `c1_modulliste.md` §D.9 sind ausdrücklich verworfen** — eine reine **Ortsklausel** für `models` ist keine Namensregel und verschöbe die vorregistrierte Zelle K4/`INCORRECT_LOCATION` von „teilweise" auf „ja" (eine Matrixzelle durch Regelformulierung statt durch Messung); ein Verbot des Präfix `legacy_` in `models` würde von der **CLEAN-Baseline selbst** verletzt und ließe den Clean-State-Audit durchfallen (C3 fordert 0 Findings) — derselbe Fehler, den die Umbenennung von `legacy_token` vermieden hat. **Folge:** I28 ist geschlossen, alle vier `INCORRECT_LOCATION`-Injektionen haben eine verletzte Regel und einen besetzbaren `rule_id`-Eintrag im Manifest. **Keine Matrixzelle bewegt sich.** Ausführung: `c1_modulliste.md` Rev. 3 benennt alle zwölf `models`-Module auf `*_models` um (inkl. der vier Zwillinge und des I28-Trägers), maschinell geprüft mit 0 Verstößen im Clean-Zustand und genau einem verletzenden Phantom je Klauselgruppe; die zehn Ist-Zahlen bleiben unverändert · §2 — **Phantomzeile zu I28 nachgezogen** (`depot.billing.models.legacy_tax_models` → `depot.billing.legacy_tax_models`); die Namen dieser Tabelle gehen in den `expected_match_key` ein und müssen mit `c1_modulliste.md` zeichengleich sein · §5 — **Zahl der `__init__.py` korrigiert**: „rund elf" → **23 von 73 Dateien**; die alte Zahl stammte aus dem entfallenen Richtwert „eine je Komponente". Das Argument gegen Init-Module im Clean-Control-Set wird dadurch **stärker**: eine über alle 73 Dateien gerechnete Falsch-Positiv-Rate läge bei 50/73 = 0,685 der korrekten, also um rund ein Drittel zu niedrig | `c1a_nachtrag_framework_importe.md` §2/§3.2; `planung/c1_modulliste.md` Rev. 3 §3, §4 und §D.9; §3 (vi) Rev. 14; `planung/c1_komponentenschnitt.md` §3.1 Rev. 2 |
| 16 | 14.08.2026 | §3 — **Nachtrag: drei Bauentscheidungen des ersten Baucommits vorregistriert.** **(A) Reservierungsregel für Ports:** die vier Ports der `MISSING_PORT_REFERENCE`-Träger I17–I20 (`TokenSigner`, `RateProvider`, `PaymentGateway`, `Clock`) erscheinen in der Clean-Baseline in **genau einem** Modul — ihrem Träger — und dort in einer **öffentlichen Methodensignatur**; alle übrigen Importeure von `depot.core.ports` verwenden andere Ports, und `ports.py` darf dafür in **4b-2 bis 4b-4 erweitert** werden. Grund: `R-PORT-1…4` sind vier **Einzelregeln**, je auf ein Trägermodul mit `are_named` gebunden (Komponentenschnitt §6.3) — ein mehrfach verwendeter Port machte die Zuordnung **Befund → Regel mehrdeutig**, und dieselbe Schnittstelle in fachlich unverwandten Modulen wäre bei der Sichtprüfung als **konstruiert** erkennbar. Dass `ports.py` in mehreren Commits wächst, ist unerheblich: `B` ist der **letzte** der vier Baucommits, für den Messpfad zählt allein sein Zustand. Die Alternative „Wiederverwendung der sieben vorhandenen Ports" ist damit verworfen. **(B) Alle vier `API_CONTRACT`-Regeln (R-SIG-1…4) prüfen einheitlich über den `statement`-Wortlaut**, nicht über ein Protocol im Repo: `depot.orders.mappers.order_line_mapper` (**I32**) importiert `depot.core.ports` nach der Modulliste **nicht** und kann kein Protocol referenzieren; eine Ungleichbehandlung der vier Regeln derselben Kategorie wäre nicht begründbar. Die drei Ports aus 4b-1 §3.2 bleiben als **Implementierungsvorlage** im Repo, der `statement`-Wortlaut bleibt C2. **(C) Fassadenform:** `core/adapters/__init__.py` löst die re-exportierten Namen über ein **Modul-`__getattr__` (PEP 562)** auf — `import depot.x.y` plus eager Zuweisung bricht in CPython mit `AttributeError: cannot access submodule 'adapters' of module 'depot.core'`, weil die Importmaschinerie das Attribut erst **nach** `exec_module` setzt; **V12 bleibt damit ohne Ausnahme**. Gegen die geprüfte V12-Ausnahme für Re-Export-`__init__.py` sprechen zwei Gründe: die Auflösung von `from <vollqualifiziertes modul> import <symbol>` ist für dieses Werkzeugpaar **ungemessen** (B9+/B17c betreffen `from <paket> import <modul>`, eine andere Form), und die Fassade ist für **keines** der zehn Szenarien Messobjekt — die Aufweichung wäre ein **Tausch ohne Messgewinn**. Statisch folgenlos: drei Top-Level-Importe im Modulkopf, Kante `core_adapters → core_adapters_internal` sichtbar, `core_adapters` bleibt ihr einziger Importeur. Die Abweichung vom gemessenen Vorbild (c1a C2: 9 von 9 realen Fassaden schreiben `from .x import Y`) gehört zu **T6** (§9) · §5 — **vorhergesagter Falsch-Positiv auf der Fassade:** `depot.core.adapters` ist das **einzige** Modul der Clean-Baseline, das das geschützte Internum importiert; im Clean-Control-Lauf hat es **R-PROTECT-1 im Scope** und zeigt genau die Importe, die die Regel verbietet — sie erlaubt sie nur ihm. Ein K2/K3-Finding dort ist **vorregistrierte Beobachtung**, kein unerwarteter FP, und **getrennt zu führen**; es prüft, ob das Modell die `allowed_importers`-Hälfte des `statement` liest oder nur die Verbotshälfte · **Datumskorrektur:** die Nachträge der Rev. 15 in §2, §3 und §5 sind auf den **14.08.2026** datiert (der auslösende Auftrag hatte 13.08. vorgegeben, das war ein Fehler im Auftrag); ältere Nachträge unverändert | `4b1_bericht_baseline_kern.md` §2, §3.1–§3.4, §5.1, §6.3; `planung/c1_komponentenschnitt.md` §6.3; `planung/c1_modulliste.md` §1 und §D.6/§D.8; c1a C2 |

| 17 | 14.08.2026 | §5 — **Ausschlusskriterium des Clean-Control-Sets präzisiert:** ausgeschlossen sind nur **LEERE** `__init__.py` (kein Import, kein `def`, kein `class`, kein `__all__`), **nicht Paketmodule als Gattung**. Der tragende Grund war „keine leeren Module im Falsch-Positiv-Nenner", nicht „keine Paketmodule"; „Paketmodul" war die Abkürzung für „leer", solange alle Paketmodule leer waren. Die gebaute Baseline widerlegt die Gleichsetzung: **zwei der 23** sind inhaltstragend — `depot.core.adapters` (Fassade: drei Top-Level-Importe, `__all__`, PEP-562-Auflösung) und `depot.orders.services` (trägt die Eltern/Kind-Kante des `CYCLE_PARENT_CHILD`-Paares plus zwei Funktionen). **Zwingend**, weil die Amendments vom 13.08. und 14.08. sich sonst widersprechen: unter dem alten Wortlaut liefe `depot.core.adapters` nie durch den LLM-Pfad, und der in Rev. 16 **vorregistrierte Falsch-Positiv auf der Fassade** wäre nicht messbar. **Wirkung: 21 leere Paketmodule bleiben draußen, das Control-Set umfasst 52 statt 50 Module**; die Auflage zur getrennten Ausweisung leerer Init-Module bleibt unberührt · §1 — **Framework-Pin `sqlalchemy` 2.0.52** in den eingefrorenen Messstand: (a) es ist die Umgebung, in der K4 unter `include_external_packages = True` und K5 unter `exclude_external_libraries = False` externe Importe auflösen — davon hängt die vorregistrierte Zelle `FORBIDDEN_SIGNATURE_TYPE`/K4 = FP⁴ ab; (b) c2b hat unter genau dieser Version gemessen und führt sie als „Fixture-Requisite, nicht registriert" — richtig, solange es Fixture-Requisite war, überholt seit acht Module der Baseline sie führen; (c) die `README.md` des Baseline-Commits **behauptet den Pin bereits** („All modules import cleanly under the framework version the specification pins"), und `B` wird nicht geändert, also ist der Pin nachzuliefern. Gemessen ergänzt: Smoke-Test unter 2.0.52 importiert **alle 73 Module fehlerfrei**. **Ungemessen** und neu in der B38-Prüfliste: Auflösung externer Importe bei **fehlendem** Paket · §2 — **Kontaminationsfreiheit datiert:** „nie öffentlich zugänglich" gilt für den **Evaluationszeitraum** (bis zur letzten Messung), weil das Testrepo nach **Block 8** des Arbeitsplans Teil des Reproduzierbarkeits-Anhangs wird. Die `README.md` in `B` formuliert weiter absolut und wird **NICHT** geändert; die Präzisierung erfolgt hier und in Kapitel 4 · §3 — **Singular-Regel für Injektionen:** jede Injektion benennt im Manifest die betroffene **Methode oder Signatur namentlich**, auch wo der `match_key` sie nicht führt. Anlass gemessen: `ledger_service` führte im ersten Entwurf `Clock` in **zwei** Signaturen, während I20 „die Annotation" im Singular entfernt — die Injektion wäre unbestimmt gewesen. Betroffen `FORBIDDEN_SIGNATURE_TYPE` (I21–I24; der Schlüssel hängt nicht daran, die Reproduzierbarkeit schon) und `SIGNATURE_DEVIATION` (I29–I32; dort trägt `offending_type` nach DDR L/P den Symbolnamen, der Schlüssel hängt also daran); für I17–I20 und I29–I32 ist die Signatur durch die Bauberichte bereits wörtlich festgelegt · §6 — **Vorbedingung für C3, Leer-Prompt:** vor dem Start der Kampagne wird der Prompt für **ein importfreies Modul** einmal gerendert und manuell geprüft. Die vier `INCORRECT_LOCATION`-Träger I25–I28 sind import- und referenzfrei (Bedingung 8, gefordert), im Diff erscheint eine hinzugefügte Datei ohne Importe, und der **Canary-Hash deckt den Rendering-Zweig eines Prompts ohne Importe nicht ab** (B27) — er wurde nie gerendert. Ein Defekt dort erschiene als **vier Modellfehler** in genau der Kategorie, in der K2/K3 als einzige „ja" tragen | `4b1_bericht_baseline_kern.md` §5.1; `4b3_bericht_baseline_orders.md` §7.1; `4b4_bericht_baseline_billing.md` §2, §7 und §8; `c2b_bericht_erlaubnislisten.md` §0/§2b/§3d; `planung/c1_modulliste.md` §1 und §4 Bedingung 8/9; `planung/arbeitsplan_bis_abgabe.md` Block 8; B27 / `b1_bericht_matchkey.md` E3 |
| 18 | 23.08.2026 | §3 — **Nachtrag: die drei schlüsselbildenden Schreibweisen vorregistriert, verbindlich für C4.** `ABSENCE_REQUIRED` trägt in `offending_type` den **Porttyp in der Schreibweise des `statement`** (`depot.core.ports.TokenSigner`, `…RateProvider`, `…PaymentGateway`, `…Clock`); `API_CONTRACT` den **Symbolnamen als `Class.method`** (`SessionRepository.touch`, `OrderQuery.percent_for`, `InvoiceQuery.settled_cents`) bzw. bei einer Top-Level-Funktion den bloßen Namen (`to_payload`); `STRUCTURAL_PLACEMENT` die **volle Punktkette des fehlplatzierten Moduls**. Alle drei bilden das **vierte Segment** des `match_key` (`matchKey.ts:26`); ohne sie ist `expected_match_key` für zwölf der 32 Injektionen nicht berechenbar, und sie standen bisher nur in einem Bericht. Ergänzt Decision Record L/P, der zwischen voller Kette und letztem Segment bzw. zwischen `method` und `Class.method` nicht entschied; Kriterium für beide Wahlen ist **die im Prompt wörtlich vorkommende Form** (`contextBuilder.ts:58-59`) · §3 — **Nachtrag: die vier R-PORT-Statements sind gekürzt**, die **wörtliche Soll-Signatur entfällt**. Trägermodul, Methode als `Class.method` und Porttyp bleiben. Grund: Komponentenschnitt §8 verlangt für diese Regeln die **Typschreibweise**, nicht die Signatur — die ist Regelinhalt bei `API_CONTRACT` und dort allein; mit der vollen Signatur würde die Prüfung zum **Zeichenkettenvergleich** und `ABSENCE_REQUIRED` gegenüber K1/K4/K5 **inflationiert**, in genau der Kategorie, in der K2/K3 als Mehrwert ausgewiesen werden (UF3). **Rückkehr zum vorregistrierten Wortlaut, vor jeder Messung.** Wirkung: Statements 651/678/690/757 → 480/487/488/596 Zeichen, dichtester Prompt 4 920 → 4 527 Zeichen, `rules_sha256` nachgezogen; **keine Matrixzelle und kein `expected_match_key` bewegt sich** · §5 — **Nachtrag: zweite vorhergesagte Falschmeldung.** `orders_services` trägt **zwei** `ABSENCE_REQUIRED`-Regeln im Scope (R-PORT-2 für `catalog_service`, R-PORT-3 für `refund_service`); da Regel-Scopes **komponentenweit** sind (`contextBuilder.ts:19`), sieht das Modell bei jedem Modul dieser Komponente eine Regel, die ein anderes Modul betrifft. Ein Finding auf der Nicht-Träger-Regel ist **vorregistriert und getrennt zu führen** — strukturell derselbe Fall wie die Adapterfassade (Rev. 16) und dieselbe Messfrage: liest das Modell die einschränkende Hälfte des `statement`. Betroffen ist **nur** `orders_services`; Ursache ist die Injektionsverteilung (Komponentenschnitt §5, `orders_services` 2×), nicht die Regelformulierung · **Werkzeug:** `tools/validate_soll.py` Punkt (3) um **(3c)** — `category` zeichengleich mit den sechs Ebene-1-Strings, Exit ≠ 0 bei Abweichung — und **(3d)** — jede Kategorie von mindestens einer Regel getragen, Warnung — erweitert. Der Validator läuft in C3 und in C7 je Commit; dort muss die Prüfung sitzen, nicht in der C5-Freeze-Liste | `c2a_bericht_regeldatei.md` §4, §7.1, §8 und Nachtrag §N1–§N5; `planung/c1_komponentenschnitt.md` §5, §6.3, §8; Decision Record L/P |
| 19 | 23.08.2026 | §4 — **Nachtrag: die sechzehn Regelstatements benennen einheitlich die erwartete Subjektform.** Strukturelle Kategorien (`FORBIDDEN_RELATION`, `CYCLE`) schließen mit `subject.from`/`subject.to`, die vier Elementkategorien (`ABSENCE_REQUIRED`, `FORBIDDEN_SIGNATURE_TYPE`, `STRUCTURAL_PLACEMENT`, `API_CONTRACT`) mit `subject.offending_type` in der Schreibweise aus §3 Rev. 18 — in den **Feldnamen des Antwortschemas** (`llmClient.ts:200-214`, `validate.ts:56-58`). Grund: `subjectKey` ist das vierte Segment des `match_key` und wird aus `offending_type` **oder** aus `from->to` gebaut (`matchKey.ts:23-26`); beide Formen sind für dieselbe Beobachtung zulässig, und die falsche Wahl lässt den Schlüssel **nie** treffen — `strict` misst dann die Formatwahl statt der Erkennung. `localized` (Decision Record O) fängt alles Übrige ab, die Subjektform aber nicht, weil sie in **beide** Metriken durchschlägt. **Einheitlich**, weil eine ungleiche Belegung den Vergleich ZWISCHEN den Kategorien aus einem regeltextlichen statt einem modellbezogenen Grund verzerrte — dieselbe Erwägung wie bei der einheitlichen `severity`. Als **Instrumenteneigenschaft** vorregistriert und in Kapitel 4 als Konstruktionsbedingung zu benennen. Befund vorab: **alle sechzehn Statements nannten bereits eine Subjektform, aber in vier verschiedenen Diktionen und keines im Feldnamen** (c2b Teil A, A1). Wirkung: Statements 9 814 → 10 211 Zeichen, dichtester Prompt 4 527 → 4 747 Zeichen, `rules_sha256` nachgezogen; **keine Matrixzelle und kein `expected_match_key` bewegt sich** | `c2b_bericht_k4_konfiguration.md` Teil A; Decision Record L und O; §3 Nachtrag Rev. 18 |
| 20 | 23.08.2026 | §3 — **Matrixzellen `FRAMEWORK_TYPE_IN_SIGNATURE`/K4 und /K5: FP⁴ → „nein".** Beide Baselines werten ausschließlich Importkanten aus, die Injektion ändert diese nicht; ein Importverbot widerspricht R-FRAMEWORK-1 und erzeugt auf der sauberen Baseline acht Findings, obwohl C3 über K1–K5 null fordert. Fußnote 4 bewahrt den alten Wortlaut gestrichen; B9+ F1 war richtig gemessen, aber falsch in eine C3-taugliche Konfiguration übertragen. Die hypothesenkonforme Richtung ist offengelegt; zulässig ist die Änderung nur, weil die Messung sie erzwingt. `FORBIDDEN_SIGNATURE_TYPE` ist damit die einzige Kategorie, in der allein K2/K3 etwas finden können — strukturelle Nicht-Abdeckung beider Baselines, kein Werkzeugversagen. Der Zwilling misst nun direkt, ob K2/K3 lexikalisch vom Import auf einen Verstoß schließen oder die erlaubte Import-/verbotene Signatur-Differenz lesen; er bleibt getrennt im Clean-Control-Set. §3/§6.1 und §9 des Komponentenschnitts sowie B38 und der zentrale Stand sind auf die gemessenen K4-Konfigurationsbefunde nachgezogen. | `c2b_bericht_k4_konfiguration.md` §B2.1, §B4, §B5 (g)/(i), §B6; B9+ Frage 1 |
| 21 | 23.08.2026 | §1 — **Nachtrag: drei Folgen aus Rev. 20, alle Festlegungen bleiben, zwei Begründungen werden ersetzt.** **(C1)** `include_external_packages = True` **bleibt**; die alte Begründung („beide Werkzeuge müssen den Framework-Import sehen") **war** die FP⁴-Zelle und fällt mit Rev. 20. Neu und tragend: die externen Importe bleiben im Graphen **sichtbar**, und dass K4 dennoch nichts meldet, ist damit eine **inspizierbare Nicht-Abdeckung** statt eines Artefakts der Unsichtbarkeit — der Unterschied zwischen „nicht gefunden" und „nicht gesucht". Gemessen **wirkungslos** für alle dreizehn Contracts (`13 kept, 0 broken` mit **und** ohne Schalter); die Kosten der Festlegung sind null. **(C2)** Der `sqlalchemy`-Pin **2.0.52 bleibt**, ruht aber ab hier **allein auf Grund (c)** — die `README.md` des Baseline-Commits behauptet den Pin bereits, und `B` wird nicht geändert — sowie auf dem **Smoke-Test** (73 importiert, 0 gebrochen). Grund (a) fällt mit der Zelle weg, Grund (b) ist eine Provenienzangabe und kein Grund zur Festschreibung. Ausdrücklich vermerkt, weil die **Zahl** der Gründe sich geändert hat. Ergänzend **schließt das B38 (l) auf beiden Seiten**: beide Werkzeuge lösen externe Importe **auch bei fehlendem Paket** auf — K4 `13 kept, 0 broken` und identische Sondenbefunde, K5 mit unveränderten Knoten `sqlalchemy`/`sqlalchemy.orm` und **denselben acht Modulen**; beide lesen den Importgraphen aus dem **Quelltext**, nicht aus der Installation. **(C3)** K5 verwendet **EIN** Architekturobjekt (`exclude_external_libraries = True`); das zweite Objekt aus Rev. 14 trug allein die Framework-Regel, die mit Rev. 20 entfällt, und ein ungenutztes Objekt in einer einzufrierenden Datei ist totes Gewicht. **Alle 23 Regeln** laufen gegen dieses eine Objekt; die in Rev. 14 verlangte Zuordnung Regel → Objekt wird dadurch trivial und ist in `data/soll/MANIFEST.md` festgehalten · §3 — **Nachtrag: zwei Nachzüge aus Rev. 20.** **(1)** Die Begründung der Annotation **ᴾ** („mit `forbidden` in Vorgabestellung nicht erfüllbar") gilt für den **allgemeinen Fall** (c2a §1.1c), **nicht für das Testrepo**: die Kette `services → storage → internal` ist dort **nicht realisiert** — `storage.py` importiert nur `depot.core.ports`, die Internum-Importe liegen in der **Fassade**. Am Testrepo hielten **beide** Contract-Typen auf clean und **beide** meldeten die Injektion. **`protected` bleibt die Wahl** (die Zelle ist an den Typ vorregistriert, und die Falle ist real, sobald die Kette entsteht), aber ᴾ beschreibt **am Messgegenstand** eine Lage, die dort nicht vorliegt: als **DEKLARIERTE GRENZE** geführt, nicht als Befund. Alttext steht; die Parallelstelle im Komponentenschnitt **Rev. 3** ist bereits nachgezogen, die Baseline wird dafür **nicht** neu gebaut. **(2)** Die **Belegquellenspalte** der Zeile `FRAMEWORK_TYPE_IN_SIGNATURE` ist **je Zelle aufgespalten**: **K4 gemessen** (`c2b…` §B6, acht Findings auf der sauberen Baseline, wörtliche Ausgabe), **K5** war zum Zeitpunkt von Rev. 20 **abgeleitet** (B9+ F1 + `converter.py:78,89`) und ist mit der **C2c-Sonde gemessen** (`c2c…` §B6: dieselben acht Module, Befundmenge **vor und nach** der Injektion identisch). Grund für die Aufspaltung: die Unterscheidung Belegt/Abgeleitet trägt in dieser Arbeit überall, und die Zelle ist soeben **in Richtung der Hypothese** bewegt worden. **Kein Matrixwert bewegt sich.** | `c2c_bericht_k5_konfiguration.md`; `c2b_bericht_k4_konfiguration.md` §B5 (g)/(k)/(l), §B6; `planung/c1_komponentenschnitt.md` Rev. 3 §3.1 (4)/§6.1; B9+ Frage 1 |
| 22 | 23.08.2026 | §3 — **B39 ENTSCHIEDEN, zwei Matrixzellen bewegen sich:** `CYCLE_SIBLING`/**K5** und `CYCLE_PARENT_CHILD`/**K5** von **„nein"** auf **„teilweise⁷"**, die alten Werte gestrichen sichtbar. K5 meldet beide Injektionen, aber **nicht als Zyklus** — PyTestArch hat keine Zyklenregel (B9+ F5, unverändert richtig) —, sondern als **nicht gelistete Kante der Erlaubnisliste**, je `1 failed, 23 passed`, Exit 1, wörtliche Ausgabe. **Die Ursache ist nicht wählbar:** die Whitelist ist einseitig (DDR M.2 Festlegung 4), eine aus ihr abgeleitete Erlaubnisliste **muss** die Rückkante melden, und die Kante aufzunehmen hieße, eine **andere Zielarchitektur** auszudrücken (§1 Rev. 13); die K5-Konfiguration wird **nicht** geändert. **Beide Alternativen erwogen und verworfen:** `expected_co_findings` setzt einen Treffer voraus, den die Begleitmeldung begleitet — bei K1 der `cycle`-Record, bei K5 gibt es keinen; die Meldung dort zu parken zählte vier Injektionen als „nichts" und untertriebe K5 systematisch. „ja" behauptete Zyklenerkennung, die B9+ F5 widerlegt — dieselbe Regel feuert bei jeder nicht gelisteten Kante, auch ohne Gegenkante. **Buchung ohne neue Regel:** in `strict` kein Treffer (abweichendes Kategoriesegment), in `localized` die bestehende Klasse **„richtige Stelle, falsche Kategorie"** (§4, Amendment 13.08. (f)) — genau der Fall, für den DDR O `localized` eingeführt hat. **Richtung offengelegt:** die Änderung macht eine **Baseline besser** und liegt damit **gegen** die Hypothese; zulässig, weil gemessen erzwungen. Bei **Rev. 20** lag die Richtung umgekehrt — **die Symmetrie ist der Beleg**, dass beide Änderungen der Messung folgen und nicht der These. Vollständige Begründung in der **neuen Fußnote 7**, in der Form von Fußnote 5 · §8 — **B40:** die mit Rev. 20 zurückgezogene Zeile „Kein Nullzeilen-Fall, sondern messbarer False Positive: `FRAMEWORK_TYPE_IN_SIGNATURE` bei K4 und K5 …" ist **ersetzt**; die Kategorie steht jetzt in **„Echte Nullzeile und damit Ausdrucksmächtigkeits-Feststellung"**, mit dem Zusatz, dass ein **Import-Proxy** R-FRAMEWORK-1 widerspräche und auf der sauberen Baseline **acht Findings** erzeugte (K4 `c2b…` §B6, K5 `c2c…` §B6). Alttext gestrichen stehen gelassen. Dazu die **B39-Zeile**: K5 meldet `CYCLE_*` an der richtigen Stelle unter falscher Kategorie — ein **Ausdrucksmächtigkeitsbefund eigener Art** (die Erlaubnisliste erreicht die Stelle, das Vokabular die Kategorie nicht); `CYCLE` bei K5 verlässt dafür die Nullzeilen-Aufzählung · §6 — **Lauf-Akzeptanzregel für den Kontrolllauf: `control_files_count == calls_total`**; die bestehende Regel `changed_files_count == 1 ∧ calls_total == 1` gilt **nur für Injektionsläufe**. Der Vorbehalt aus Increment 7 §8.1 ist **ohne weiteren Lauf** aufgelöst: `llmChecker.ts:96` überspringt den Call nur bei leerem Regel-Scope, Regel-Scopes sind **komponentenweit** (`contextBuilder.ts:19`), Validatorpunkt (3b) stand in C2a auf **0 von 19 ungescopten Komponenten**, und der 4c-Ladetest auf **77 gelistete Module, 0 Fehltreffer** (73 Dateibaum-Module, 0 unmapped) — daraus folgt für alle **52** Kontrollmodule mindestens eine Regel im Scope. Ferner: **`--control-files` und `control_files_count` als Bestandteil des Messpfads**, mit dem neuen **`checker_git_head` = `348ca9d`** (vier Inhaltshashes byte-identisch, `promptFreeze.spec.ts` grün) · **Mitkorrektur außerhalb des Protokolls:** der **Kopfkommentar** von `data/soll/importlinter.ini` trug noch die FP⁴-Begründung für `include_external_packages = True`, die §1 Rev. 21 (Teil C1) ersetzt hat — korrigiert **vor** jeder Messung, weil die Datei gehashter Messeingang ist; neuer SHA256 `0c9a1e0e…` statt `652b2352…`, `SHA256SUMS`/`MANIFEST.md` nachgezogen, Nachlauf gegen `baseline` **`13 kept, 0 broken`, Exit 0** | `c2c_bericht_k5_konfiguration.md` §B5; `increment7_bericht_control_set.md` §1b/§2b/§6/§8.1; `c2a_bericht_regeldatei.md` §5; `4c_bericht_soll_und_validator.md` §5; `c2b_bericht_k4_konfiguration.md` §B6/§B11; DDR M.2 Festlegung 4; DDR O |

| 24 | 23.08.2026 | Kopf auf Rev. 24 · §1 — Build-Provenienz des ausgeführten `dist/cli.js`: Neubau vor jedem Lauf, SHA256, Bauzeitpunkt und Checker-`git status --porcelain` neben `checker_git_head`; Rollen-Pins `networkx==3.6.1` (Messpfad) und `PyYAML==6.0.2` (Soll-Validator) · §6 — vollständige Aufrufzeilen für K1 (diff/full), K2, K3, K4, K5 und beide Kontrollläufe, `--src-root src` vor C4 festgelegt, nicht vorhandene Optionen als Lücken markiert; Nachlaufskript als alleiniger Vollstrecker beider Akzeptanzregeln, ungültige Läufe werden wiederholt und nicht ausgewertet | `c3a_bericht_clean_state_audit.md`; `b1_bericht_matchkey.md` D1; tatsächliche CLI in `cli.ts`, `cliArgs.ts`, `run.ts`, `cliExtractor.ts`; `reporter.ts:59-64`; C2a/C2b |
| 25 | 23.08.2026 | Kopf auf Rev. 25 · §4 — **Nachtrag: Recordmenge je Konfiguration.** Die K2/K3-Aufrufzeilen (§6 Rev. 24) tragen `--rule-graph diff`, der deterministische Pfad läuft mit, seine Records landen im **selben** `--run-log`/`--json-out`; ein K2/K3-Lauf erzeugt die **Vereinigung** aus LLM-Findings und `DERIVED:forbidden-edge`/`DERIVED:cycle`. **Festlegung: die Konfiguration ist der Mechanismus, nicht der Aufruf** — **K1** := `rule_id`-Präfix `DERIVED:`, **K2/K3** := jedes andere `rule_id`. Filter **vor** der Berechnung **beider** Metriken, in der Harness (C6) und im Nachlaufskript; **keine** Checker-Änderung, die bewegte `checker_git_head` ein viertes Mal ohne Beweiskraft. **Beide Metriken getrennt begründet:** `strict` ist ohne Filter **unbetroffen** (differierende Kategoriesegmente, ein DERIVED-Record trifft den erwarteten K2/K3-Schlüssel nie); `localized` wäre ohne Filter **konfundiert** — es trifft auf **Stelle**, nicht Kategorie (DDR O, B39 baut darauf auf), und ein DERIVED-Record liegt bei **jeder der sechzehn strukturellen Injektionen** am richtigen Modul: K2/K3 bekämen dort einen Treffer **ohne Modellmeldung**, in genau den Kategorien, in denen **K1 der Vergleichsmaßstab** ist. Für den Kontrolllauf auf `B` ist die Menge **leer** (C3a: K1 mit 0 Findings) — ohne Wirkung, aber unverändert gültig · §6 — **Nachtrag: das Nachlaufskript weist je Lauf BEIDE Zahlen getrennt aus** (`DERIVED:`-Records und LLM-Records); eine Auswertung, die nur die Gesamtzahl führt, ist **ungültig**. Der Filter ist die **erste Stufe** des Joins; die beiden Lauf-Akzeptanzregeln bleiben unverändert, sie zählen Dateien und Calls, nicht Records | §6 Nachtrag Rev. 24 (Aufrufzeilen mit `--rule-graph diff`); DDR O; B39/§3 Fußnote 7; `ruleEngine.ts` (`DERIVED:forbidden-edge`, `DERIVED:cycle`); `c3a_bericht_clean_state_audit.md` |
| 26 | 24.08.2026 | Kopf auf Rev. 26 · §6 — **Nachtrag: beide Lauf-Akzeptanzregeln tragen den Wiederholungsfaktor.** `calls_total` akkumuliert über alle Repetitionen (`reporter.ts` `CallTally.total`, `run.ts:169-206`); die registrierten Regeln galten nur für `--runs 1`. Korrigiert: `changed_files_count == 1 ∧ calls_total == 1 * runs` (Injektionslauf), `calls_total == control_files_count * runs` (Kontrolllauf); gemessen `calls_total: 3` bei `control_files_count: 1` und `--runs 3` in allen fünf K2-Läufen. Die alte Fassung hätte bei der registrierten Aufrufzeile jeden der 32 Injektionsläufe als ungültig verworfen. `runLog.ts:85-86` **kommentiert** die Invariante nur, prüft sie nicht — kein getrennter Codebefund · §6 — **Nachtrag: Exit-Code ist kein Gültigkeitskriterium.** Gemessen Exit 0 bei 0 Findings, Exit 1 bei ≥ 1 Finding; Gültigkeit bemisst sich an `invalid_reasons`, `calls_invalid`, `calls_transport_failed` und den beiden Zählregeln oben · §1 — **Nachtrag: Kontextfenster als gemessener Umgebungsparameter.** Kein `num_ctx` gesetzt (`llmClient.ts:114-124`, `llmClient.ts:37-53`), Ollama lädt gemessen `CONTEXT 4096` statt der Modellgrenze 32768; Nachlaufskript prüft je Call `tokens_in + tokens_out` gegen das Fenster, ohne Eingriff in den Messpfad · §1 — **Nachtrag: Messumgebung K2 und Reproduzierbarkeitsbefund.** Vollständige Umgebung (Maschine, Ollama, Modell) aus dem Machbarkeitslauf übernommen; `dist/cli.js` auf der neuen Maschine SHA256-identisch mit den vier Notebook-Bauten trotz anderem Betriebssystem und anderer Node-Version · §9 — **T13**: Maschinenwechsel für K2, belegt folgenlos (SHA256-Gegenprobe, bitgleicher Build, unveränderte K4-/K5-Referenzergebnisse) | `k2_machbarkeitslauf_bericht.md` |
| 27 | 25.08.2026 | Kopf auf Rev. 27 · §4 — **Lesekorrektur: `localized` misst auf dem LLM-Pfad die Meldequote auf der geprüften Datei, nicht die Lokalisationsgenauigkeit** (`location.module`/`location.component` werden vom Checker aus dem `ChangedFact` gesetzt, nie aus der Modellantwort, `llmChecker.ts:282-305`); Berichtspflicht gemeinsam mit der Falsch-Positiv-Rate bekräftigt, Basisrate 49/52 = 0,9423 gemessen. **Keine Änderung an Metrik, Regeldatei, Prompt oder Schema** · §3 — deskriptiver Nachtrag zu den 461 Findings des K2-Kontrolllaufs: 71,4 % Selbstbezug/7,8 % Fremdbezug/2,6 % Zielbezug/18,2 % nicht zuordenbar, `R-CORE-1` als 153 identische Findings über alle drei Repetitionen, 9 `sqlalchemy`-Halluzinationen (Prompt enthält den Begriff nirgends), beide vorregistrierten Meldungen (Rev. 16, Rev. 18) im unabhängigen Prompt-Abgleich bestätigt, 51 von 52 Modulen über drei Repetitionen reproduzierbar · §1 — **K2-Kontrolllauf auf voller Skala bestätigt** (52/52 Invocationen, 33 min 2 s, 0 Wiederholungen, 156/156 Calls, Token-Maximum 2356/4096, 57–60 °C ohne thermischen Drift über Invocation 1/26/52), Kontextfenster-Frage aus Rev. 26 empirisch geschlossen; **Poolbefund K3**: unter einem gegenüber C3b um Faktor 15 reduzierten, über fünf entkoppelte Invocationen verteilten Lastprofil brechen 3 von 5 mit `http_429`/`limit_source: upstream_provider_shared_pool` ab, 6 von 15 Calls verloren — die Ausfallursache liegt am geteilten Anbieterkontingent, nicht am Burst, unabhängig vom eigenen Guthaben; Nebenbefund positiv (Abbruchgrund erstmals im `llm_call`-Record sichtbar), Nebenbefund offen (zwei negative `latency_ms`-Werte, ungeprüft) · §6 — operative Buchung des Poolbefunds unter der bestehenden Kontrolllauf-Akzeptanzregel, unberührt · §7 — **Schlüsselvorfall dokumentiert**: einmaliges Klartext-Erscheinen des OpenRouter-Schlüssels in der Sitzungsausgabe, `grep -rI` über `docs/`/`data/`/`tools/` nach `sk-or-` ohne Treffer, Schlüssel beim Anbieter gelöscht und ersetzt | `c3b_k2_nachtrag_findingbezug.md`; `c3b_k2_bericht_kontrolllauf.md`; `k3_machbarkeitslauf_bericht.md`; Decision Record O, Konsequenz 2; B37 |
| 28 | 25.08.2026 | Kopf auf Rev. 28 · §3 — **Nachtrag: I16-Zielkante klargestellt.** Die in Fußnote 7 zitierte K5-Ausgabe zu I16 (`"…pricing.engine" imports "…order_service"`) stammt aus der C2c-Prüfsonde gegen zehn Baseline-Kopien mit je einer nachgebauten Injektion, nicht aus der I16-Injektion dieses Testrepositoriums — der alte Wortlaut bleibt gestrichen stehen. **Verbindlich für C4b:** I16 ergänzt den Import des **Paketmoduls** `depot.orders.services`, nicht eines Submoduls; Begründung über den Blindfleck von `acyclic_siblings` bei Paket **und** eigenem Untermodul (Decision Record P) — ein Import auf `order_service` wäre auf Modulebene eine Kante zwischen Cousins und zerstörte den Gegenstand der Kategorie. `match_key` unberührt (`location.module`/`subject` identisch in beiden Lesarten); nur der K5-Meldetext unterscheidet sich. Zusatz: der I16-Commit erzeugt einen echten Laufzeit-Zirkelimport (`c1_modulliste.md` §D.6) — für die statische Messung folgenlos, aber der Commit darf keinem Laufzeit-Smoke-Test unterworfen werden, `python -m compileall` bleibt anwendbar · §3 — **Nachtrag: Typwahl für I21–I24 festgelegt.** Injiziert wird `sqlalchemy.orm.Session` als Parameter- oder Rückgabetypannotation einer öffentlichen Methode der Trägerklasse — kanonischer Typ des `R-FRAMEWORK-1`-Beispiels, `Mapped` ungeeignet, weil in Klassenattributen erlaubt. Drei Auflagen für C4b: (a) öffentliche, vom Extractor erfasste Methode, (b) kein neuer Import (`sqlalchemy.orm` in allen vier Trägern bereits importiert, Importmenge identisch zum Zwilling), (c) kein gebrochener Aufrufer. Genau ein Vorkommen je Träger (Singular-Regel, §3 Nachtrag Rev. 17); `offending_type` wörtlich aus dem Code, von C4b zu melden und von C4c ins Manifest zu übernehmen | `c2c_bericht_k5_konfiguration.md` §B5; `c1_modulliste.md` §D.6; Decision Record P; `architecture-rules.yaml` R-FRAMEWORK-1; `b1_bericht_matchkey.md` C4; §3 Nachtrag Rev. 17 |
| 29 | 25.08.2026 | Kopf auf Rev. 29 · §3 — **Nachtrag: Klarstellung zu den Zyklen der `LAYER_BACK_CALL`-Injektionen.** Gemessen (`c4b_bericht_injektionen.md` §8.5): **I01–I03 tragen je einen Komponentenzyklus `<k>_repository ↔ <k>_services`**, auf Modul- wie auf Komponentenebene; die übrigen Nicht-`CYCLE`-Injektionen je 0. Der Zyklus ist **konstruktionsnotwendig** — die Spine-Kante `<k>_services → <k>_repository` steht in der Whitelist und ist in der Baseline realisiert, `LAYER_BACK_CALL` injiziert die Gegenrichtung; ihn zu vermeiden hieße, die Spine-Kante zu entfernen oder dem Szenario seinen Gegenstand zu nehmen. Er ist **vorregistriert als K4-Doppelmeldung** (Komponentenschnitt §6.2, §4 Amendment 13.08.: der einzige `acyclic_siblings`-Contract meldet denselben Verstoß ein zweites Mal als Geschwisterzyklus) — **kein False Positive, getrennt zu führen** (Manifest §5.1). **Auf K1 wirkt er NICHT:** `FORBIDDEN_RELATION` läuft in `--rule-graph diff`, dort ist eine `cycle`-Begleitmeldung **strukturell unmöglich** (ein Ein-Datei-Diff erzeugt genau einen Adjazenz-Knoten, `childState === VISITING` tritt nie ein), `expected_co_findings` bleibt für alle zwölf `FORBIDDEN_RELATION`-Injektionen leer. **Z1 und Z3 unberührt** — sie gelten laut §3 nur für die `CYCLE`-Injektionen. **Keine Matrixzelle bewegt sich.** · §6 — **Nachtrag: der deskriptive Vollbild-Commit fehlt noch und ist OFFEN.** Das Amendment 12.08. registriert einen zusätzlichen Commit mit allen 32 Injektionen (Elternteil `B`, kein Merge); **C4b hat ihn nicht gebaut**, weil sein Auftrag auf 32 Commits und 32 Refs begrenzt war. Vermerkt: er geht in **keine Metrik** ein, blockiert **weder C4c noch die Kampagne**, und ist **mechanisch aus den 32 Tags herstellbar**, weil die Injektionen verschiedene Dateien betreffen (32 paarweise verschiedene Trägermodule, §8.2). **Eigener Auftrag** | `c4b_bericht_injektionen.md` §7.1, §8.2, §8.5, §11 Punkte 3 und 4; Decision Record M.2 Festlegung 2; Komponentenschnitt §6.2 |
| 30 | 26.08.2026 | Kopf auf Rev. 30 · **§4 — Nachtrag: `localized` ist für K4/`CYCLE` NICHT DEFINIERT.** Die `acyclic_siblings`-Ausgabe trägt strukturell keinen Modulnamen — gemeldet wird eine minimale Entfernungsmenge auf **Paketebene**, je gebrochenem Contract in mehreren Blöcken (V16, `c2a_bericht_contract_semantik.md` §2); ein Modul-Match nach Decision Record O ist daraus nicht bildbar. Festgelegt: die Zellen `CYCLE_SIBLING`/K4 und `CYCLE_PARENT_CHILD`/K4 tragen `localized` als **„n. b."**, **nicht als 0** — eine 0 behauptete eine Messung, die nicht stattgefunden hat. `strict` unberührt (§4 Rev. 7: exakter Vergleich für K1, **Mengenregel** für K4); die Matrixzelle `CYCLE_SIBLING`/K4 = „ja" ruht auf der Mengenregel und bewegt sich nicht. **Erwogen und verworfen:** die Paketebene als Modul-Match zu zählen — sie hätte die Metrikdefinition in genau einer Zelle verschoben und K4 dort besser gemacht, gewählt statt gemessen; Offenlegung nach der Praxis der Rev. 20 und Rev. 22 · **§5 — Nachtrag: Wanduhrzeit einheitlich extern.** Für K4/K5 existiert kein Äquivalent zu `run_footer.wall_clock_ms`; Innen- und Aussenmessung zu mischen macht die Kostentabelle konfigurationsübergreifend unvergleichbar. Festgelegt: die berichtete Wanduhrzeit ist für **alle fünf** Konfigurationen **extern je Invocation** gemessen (monotone Uhr, vom Runner geschrieben); `run_footer.wall_clock_ms` bleibt für K1/K2/K3 Innenwert im Anhang und weist die Differenz Prozessstart/Nutzarbeit aus (gemessen an C3b: Median aussen/innen 8,4/8,3 s bei K2, 97,8/96,3 s bei K3). Zwei Randbedingungen aufgenommen: `--no-cache` ist je import-linter-Lauf Ablaufregel (B9+ (b)), K4 baut den Graphen jedes Mal neu — das ist die ehrliche Laufkost; K5 bricht beim ersten fehlgeschlagenen Assert ab (B9+ (a)), die Laufzeit hängt am Trefferzeitpunkt. Berichtsform: **Grössenordnungen**, ohne Nachkommastellen-Interpretation (§5 Amendment 12.08.) · **§1 — Nachtrag: K3-Zugangsweg registriert.** Base-URL `https://inference.do-ai.run/v1`, Modell `nvidia-nemotron-3-super-120b`, **kein** `CONFORMANCE_PROVIDER_PIN` (ohne Router gibt es nichts zu pinnen, B32); die Matrixzeile „nemotron-120B (OpenRouter)" bleibt gestrichen stehen. Katalogangaben wörtlich aus `GET /v1/models` (26.08.2026, HTTP 200, 72 Einträge): `id` zeichengleich, `owned_by: digitalocean`, `created: 1773783814`, `context_length: 1000000`, `max_output_tokens: 32768`. Das **Kontextfenster wird als gemessener Umgebungsparameter** geführt, parallel zur Führung des Ollama-Fensters (`CONTEXT 4096` statt 32768, Rev. 26); Gegenprobe an 156 archivierten C3b-K3-Calls: Maximum `tokens_in + tokens_out` = 3136 (0,31 %), keine Annäherung an eine der beiden Grenzen. **Als nicht belegbar benannt:** Quantisierung, Präzision, Revision und Serving-Stack sind im Katalog **nicht ausgewiesen** (FEHLT), werden nicht geschätzt und nicht aus fremden Modellkarten ergänzt · **§1 — Nachtrag: Auswertungseingang gehasht.** `docs/protokolle/c6_auswertungsspezifikation.md` mit SHA256 `dc1d17f8…4d1d7785` als registrierter Auswertungseingang, analog zu den gehashten Messeingängen in `data/soll/`; bekannter Stand-Unterschied (§1.6/§10.1 der Spezifikation führen I21–I24 noch als Platzhalter, seit D1 erledigt) benannt, nicht stillschweigend aufgelöst · **§6 — Nachtrag: vier Aufzeichnungsauflagen für C7.** (1) externe Wanduhrzeit je Invocation für alle fünf Konfigurationen; (2) stdout **und** stderr jedes K4/K5-Aufrufs wörtlich und vollständig neben das Laufmanifest — damit ist die K4/K5-Matchregel nachträglich beliebig oft anwendbar und **Punkt 4 der Auswertungsspezifikation nicht kampagnenblockierend** (der Punkt selbst bleibt offen); (3) absoluter Testrepo-Pfad, `cwd` und Maschinenkennung ins Laufmanifest, mit den in D2 M5(d) protokollierten Referenzwerten — in beiden C3b-`run_manifest.json` ist keines der drei Felder aufgezeichnet; (4) alles aus der Liste NICHT AUFZEICHNUNGSGEDECKT, nach (1)–(3) **leer** · **§9 — T14: Anbieter- und Endpunktwechsel bei K3.** Befund 06.5/06.6 und B36a (die empirische Grundlage von Decision Record O) sind über **OpenRouter** mit dem Slug `nvidia/nemotron-3-super-120b-a12b` erhoben; gemessen wird der **DigitalOcean-Direktzugang**. Belegt: `id` zeichengleich im Katalog, `model_version` in 156/156 Calls ohne Abweichung (`runLog.ts:270` schreibt den vom Anbieter gemeldeten Wert, nie zurückgefüllt) — keine stille Substitution beobachtet. Nicht belegbar: Quantisierung, Serving-Stack, Tokenizer-/Verhaltensvergleich über identische Prompts (die Vormessungen liefen auf anderen Eingaben); **die Identität der Gewichte ist nicht verifiziert.** Auflage: die B36a-Charakteristik (Aufspaltung in zwei Findings je Verstoss, wechselnder Schema-Zweig) ist an den **ersten** K3-Kampagnenläufen gegenzuprüfen und zu berichten, gleich in welche Richtung — **nicht nachbessern, nur berichten**. Strukturell dieselbe Lage wie „Befund 06.7 bezeugt `c493daf`, gemessen wird `348ca9d`": eine Vormessung bezeugt nicht den Messstand | `d2_bericht_vormessungen.md` M0–M6; `c6_auswertungsspezifikation.md` §8 Punkt 6, §10.2, §10.3, §10.4; `c2a_bericht_contract_semantik.md` §2; V16; B9+ (a)/(b); B32; `k3_machbarkeitslauf_bericht.md`; `b36a_bericht_k3_varianzlauf.md`; `d1_bericht_matchkey_eintrag.md`; Decision Record O |
| 31 | 26.08.2026 | Kopf auf Rev. 31 · **§4 — Nachtrag: Schreibvarianz bei `FORBIDDEN_SIGNATURE_TYPE` als vorhergesagter `strict`-Ausfall, DEKLARIERT.** Gemessen im K2-Ruhezustand: von 63 `R-FRAMEWORK-1`-Findings schreiben **57** `sqlalchemy.orm.Session`, **6** die gekürzte Form `sqlalchemy.orm` — zwei Module × drei Run-Indizes, also je Modul über **alle drei Repetitionen reproduzierbar**; beide Abweichungsmodule sind `*_view_models`-**Zwillinge**, auf **keinem** der vier Träger von I21–I24 tritt die Kurzform auf. **Vorhergesagte Folge:** verkürzt ein Träger in der Kampagne ebenso, ist `strict` für diese Injektion **0** bei gleichzeitigem `localized`-**Treffer**. Ab jetzt **deklarierter** Ausfallmodus, kein nachträglich erklärter. **Ausdrücklich nicht normalisiert und der Manifestwert nicht angepasst** — konsistent zu Decision Record O, wo H3b an genau diesem Argument verworfen wurde. Der Vorbehalt gilt **allein** für diese Familie: die drei übrigen semantischen Familien treffen die vorregistrierte Form in **92 von 92** Findings · **§4 — Nachtrag: `strict` ist für `STRUCTURAL_PLACEMENT` nicht unabhängig von `localized`.** In **54 von 54** `R-PLACE-1`-Findings ist Segment 4 zeichengleich mit Segment 3 — das Modell nennt als fehlplatziertes Modul **stets das geprüfte**. Segment 3 setzt der Checker ohnehin aus dem `ChangedFact` (§4 Nachtrag Rev. 27); der Subjektwert trägt dort **keine unabhängige Information**, `strict` ist nicht schärfer als „`localized` + Kategorie". Festlegung: die Zelle wird **weiterhin berichtet**, aber mit dieser Einschränkung als **Fussnote**, damit die Ergebnistabelle nicht **zwei unabhängige Metriken suggeriert, wo eine steht**. **Keine Metrikänderung** — Lesehilfe, keine Rechenvorschrift, anders als die „n. b."-Festlegung für K4/`CYCLE` (Rev. 30) · **§5 — Nachtrag: Vorbelastung je Injektion ist berichtspflichtig.** Für **15 der 32** Injektionen tritt der erwartete `match_key` bereits im K2-Ruhezustand als tatsächlich gebildeter Schlüssel auf — I07–I09, I17–I24, I29–I32; **drei** der vier semantischen Familien vollständig (je 4/4), `STRUCTURAL_PLACEMENT` **0/4** (strukturell zwingend: die Injektion verschiebt das Modul erst). Besonders: bei **I17–I20** (`ABSENCE_REQUIRED`) meldet das Modell den Verstoss auf der **sauberen** Baseline mit exakt dem erwarteten Schlüssel, obwohl die Baseline die Regel **erfüllt**; bei **I25–I27** zieht das Trägermodul im Ruhezustand je **3** Meldungen derselben Kategorie, bei **I28 nie**. **Auflage:** zu jedem Kampagnenergebnis wird die Ruhezustandszahl **desselben Moduls in derselben Kategorie** aus C3b mitberichtet; ein `strict`-Treffer, der die Ruhezustandsrate **nicht übersteigt**, wird **nicht als Erkennungsnachweis** geführt. Injektionsscharfe Fassung der Regel „`localized` nie ohne die Falsch-Positiv-Rate" (§5 Amendment 11.08.), weil die Vorbelastung nachweislich **ungleich verteilt** ist und eine globale FP-Rate genau das wegmittelt · **§5 — Nachtrag: paarweise Auslesart je Injektion.** **Zusätzlich** zu den bestehenden Kennzahlen, nicht statt ihnen: je Injektion und je Konfiguration die **Differenz zwischen injiziertem Zustand und Ruhezustand desselben Moduls**, gleiche Repetitionszahl, Ruhezustandsseite konfigurationsgleich aus `data/c3b-k2/` bzw. `data/c3b-k3/`. **Deskriptiv, ohne inferenzstatistische Deutung**, Berichtsform **Grössenordnungen** (§5 Amendment 12.08.). **Bindend: die Differenz wird auch berichtet, wenn sie null oder negativ ist** — nicht nachbessern, nur berichten · **§6 — Nachtrag: Graphmodus je Kategorie ins Laufmanifest.** C4c Teil B hat I01–I12 in `--rule-graph diff` und I13–I16 in `--rule-graph full` gefahren, wortgleich zu §6 Rev. 7; die **16-von-16-Gegenprobe attestiert die Kampagne nur bei identischer Zuordnung**. Auflage für C7: der Modus wird aus `category_l1` des Injektionseintrags **abgeleitet** (`full` bei `CYCLE`, sonst `diff`), **nicht per Aufrufzeile gesetzt**, und je Lauf **ins Laufmanifest geschrieben**. Ein abweichender Modus verschiebt für die vier `CYCLE`-Injektionen die **Records-Menge** und liesse sie **stumm** auf null fallen — ohne Fehlermeldung und ohne dass die Lauf-Akzeptanzregel anschlüge · **§9 — zwei Ergänzungen an bestehenden Threats, kein neuer Eintrag.** **T13:** auf dem Messrechner läuft **Node v22.23.2**, in C3a protokolliert war **v22.22.2** — als Umgebungsdifferenz **benannt, nicht verschwiegen**, und **folgenlos**, weil der Gatterbeleg der Build-Hash `dist/cli.js` ist und der zeichengleich stimmt (`c0bbdfeb…d95`); alle übrigen Werkzeugstände gegen C3a §1 identisch. **T14:** der DO-Katalog nennt `context_length` **1 000 000**, was sich mit der in **Befund 05.3** festgehaltenen Registry-Angabe zum **bezahlten** OpenRouter-Slug deckt — eine **SCHWACHE, INDIREKTE** Stütze der Gewichtsidentität, ausdrücklich nur als solche geführt (`context_length` ist Serving-Konfiguration, keine Eigenschaft der Gewichte, beides Selbstauskunft). **Der Satz „die Identität der Gewichte ist nicht verifiziert" bleibt unangetastet** · **§1 — Hash-Nachzug am registrierten Auswertungseingang.** `docs/protokolle/c6_auswertungsspezifikation.md` ist in **D3a** auf den D1-Stand gezogen: die vier `expected_match_key.K2_K3` für I21–I24 **wörtlich aus `data/soll/injection_manifest.json`** in §1.6 eingetragen (Alttext durchgestrichen stehen gelassen, Verweis auf D1 Commit `40bf33a`), §10.1 als **ERLEDIGT** gekennzeichnet mit auflösendem Nachtrag, und die vier oben registrierten Punkte als **Anforderungen an C6b** aufgenommen (§3.4 (1) Schreibweisen-Flag für `FORBIDDEN_SIGNATURE_TYPE`, §3.4 (2) `STRUCTURAL_PLACEMENT`-Fussnote, §7.5 (3) Ruhezustandszahl je Injektion, §7.5 (4) paarweise Differenzspalte, Pflichtbestandteile §8 Punkte 7 und 8). Der **SHA256 in §1 Nachtrag Rev. 30 ist nachgezogen**: ~~`dc1d17f8…4d1d7785`~~ → **`2f1354bb…f6608f97`**, alter Wert gestrichen sichtbar, neuer daneben; der Absatz „Bekannter Stand-Unterschied" steht **gestrichen**, weil sein Gegenstand entfallen ist. Nachzug **im selben Commit** wie die Spezifikationsänderung, damit Spezifikation und registrierter Hash nie auseinanderfallen | `d2_bericht_vormessungen.md` M0(c), M0(d), M1, M5(d); D2N `~/scratch/d2n/schluesselform_semantische_familien.md` §0–§6 (Bericht folgt in D3b); `c4c_bericht_vorabpruefung.md` Teil B (B2); `c3a_bericht_clean_state_audit.md` §1; `c1b_bericht_ruleengine_verifikation.md`; `befunde_log.md` Befund 05.3; Decision Record O (H3b verworfen); Protokoll §4 Nachtrag Rev. 27, §5 Amendment 11.08. und 12.08., §6 Rev. 7, §1 Nachtrag Rev. 26 und Rev. 30 |
| 32 | 26.08.2026 | Kopf auf Rev. 32 · **§6 — Nachtrag: die K5-Aufrufzeile war UNVOLLSTÄNDIG REGISTRIERT, korrigiert.** Die in §6 Rev. 24 registrierte Zeile trägt `DEPOT_SRC` nicht. Die eingefrorene K5-Konfiguration leitet `root_path` **und** `module` aus der Variablen ab (`data/soll/test_architecture.py`, `_SRC = os.environ.get("DEPOT_SRC")` … `ROOT_PACKAGE = os.path.join(_SRC, "depot")`); die Anweisung steht auf **Modulebene**, läuft also in der **Sammelphase** — ohne die Variable bricht pytest beim Einlesen ab und **0 von 23** Architekturregeln werden ausgewertet, ohne dass Exit-Code oder Ausgabe diesen Fall von einem sauberen Lauf trennen. Die bestehenden Lauf-Akzeptanzregeln greifen dort **strukturell nicht**, weil K5 keinen `run_header` schreibt. **RICHTUNG DER KORREKTUR: korrigiert wird der AUFSCHRIEB, nicht die Konfiguration** — `DEPOT_SRC=<testrepo>/src` steht in `c2c_bericht_k5_konfiguration.md` §B4, `c3a_bericht_clean_state_audit.md` §3b, `d2_bericht_vormessungen.md` M5(c) und `data/soll/MANIFEST.md`; **drei gemessene Läufe, alle vor dem 26.08., alle mit der Variablen** (je `24 passed`, Exit 0). Gemessen wurde immer so; unvollständig war die Protokollzeile. **Kein Messergebnis betroffen, keine Matrixzelle bewegt, K5-Testdatei und ihr SHA256 unangetastet.** Alte Zeile gestrichen stehen gelassen, korrigierte daneben. **`-q` BLEIBT**, entschieden und begründet: der Schärfenachweis in c2c §B5 — die empirische Grundlage der K4/K5-Matchregel — ist **mit** `-q` gemessen und ist die Referenz für die Rohtextauflage aus §6 Nachtrag Rev. 30 (2); die `FAILURES`-Sektion mit Test-ID, `AssertionError`-Text und schuldigem Modul erscheint mit und ohne `-q` vollständig. Vermerkt: D2 M5(c) lief **ohne** `-q` und lieferte dasselbe Verdikt · **§6 — Nachtrag: die K3-Aufrufzeilen sind auf den Direktzugang gezogen.** §6 Rev. 24 trug in **beiden** K3-Blöcken (Injektion und Kontrolllauf) `openrouter.ai/api/v1`, `nvidia/nemotron-3-super-120b-a12b` und `CONFORMANCE_PROVIDER_PIN=digitalocean`; §1 Nachtrag Rev. 30 erklärt `https://inference.do-ai.run/v1`, `nvidia-nemotron-3-super-120b` und **keinen** Pin für verbindlich, hat aber nur die **Matrixzeile** in §1 gestrichen. **Das Protokoll trug seither zwei verbindliche K3-Zeilen** — sachlich durch Revisionsvorrang aufgelöst, dokumentarisch nicht; ein Runner, der die Zeilen wörtlich übernimmt, hätte **wählen** müssen. Beide Blöcke nachgezogen, Alttext gestrichen stehen gelassen. **Der Kontrolllauf ist bereits über den Direktzugang gefahren** (`c3b_k3_bericht_kontrolllauf.md` §2, Aufrufzeile wörtlich; `model_version` zeichengleich in **156/156** Calls, D2 M2) — die überholte Zeile bezeichnete einen Lauf, den es nie gegeben hat. Kein Pin ist **keine Auslassung**, sondern B32 (`cli.ts:50`, `provider_pin: null`) · **§6 — Nachtrag: POSITIVE LAUF-AKZEPTANZREGEL FÜR K4 UND K5 (NEU).** Die bestehenden Regeln zählen `changed_files_count` und `calls_total`, beides Felder des Checker-Laufprotokolls; **K4 und K5 schreiben keines davon** und hatten bisher **kein positives Gültigkeitskriterium**. Graphmodus (Rev. 31) und `DEPOT_SRC` (hier) sind zwei Instanzen derselben Ausfallklasse: eine Fehlkonfiguration, die **null Findings ohne Fehlermeldung** erzeugt. Festgelegt, je Invocation, vor der Auswertung: **K5 — 24 gesammelte Tests** bei fehlerfrei abgeschlossener Sammelphase (Sollwert aus `data/soll/test_architecture.py`: 19 Erlaubnislistenregeln + 4 Portregeln + 1 Wächtertest; gegengeprüft C3a §3b, D2 M5(c) `collected 24 items`, C2c §B4); **K4 — 13 ausgewertete Contracts** als `kept + broken` (Sollwert aus `data/soll/importlinter.ini`: 13 `[importlinter:contract:*]`-Abschnitte; gegengeprüft C3a §3a `13 kept, 0 broken`). **AUSDRÜCKLICH: geprüft wird, dass das Werkzeug seine REGELMENGE gelesen hat, nicht wie viele Verstösse es gefunden hat** — die Trefferzahl ist die Messung und bleibt unangetastet, `broken` darf 0–13 und `failed` 0–24 sein. Verletzung macht den Lauf **ungültig** und erzwingt Wiederholung, analog zu den bestehenden Regeln; vollstreckt vom Nachlaufskript aus dem nach Rev. 30 (2) ohnehin abgelegten stdout/stderr, **keine zusätzliche Aufzeichnungsauflage**; **der Exit-Code bleibt kein Kriterium** (Rev. 26). Für den deskriptiven Vollbild-Lauf gilt auch diese Regel nicht · **§6 — Nachtrag: Schreibform des K4-Aufrufs festgelegt.** `PYTHONPATH=src` + absolutes `--config` bei `cwd = <testrepo>` (Rev. 24) gegen `PYTHONPATH=<baseline>/src` + relatives `--config` bei `cwd = <ma>` (c2b §B3/§B11, C3a §3a) lösen unter dem in §6 festgelegten `cwd` auf **dieselben absoluten Pfade** auf. Der Runner verwendet die in Rev. 24 registrierte Form; **Festlegung der Schreibform, keine Revision der Konfiguration** · **§9 — eine Ergänzung an T12, kein neuer Eintrag.** Ausfallklasse **stille Null durch Fehlkonfiguration bei den Konfigurationen ohne Laufprotokoll**, mit beiden belegten Instanzen (Graphmodus Rev. 31, `DEPOT_SRC` Rev. 32); T12 benannte bisher nur den **lauten** Fall. Gemeinsames Merkmal ist die **fehlende Gegeninstanz**, nicht die einzelne Einstellung. **Ab Rev. 32 generisch abgedeckt** durch die positive Akzeptanzregel oben; als Restrisiko benannt bleibt eine Fehlkonfiguration, welche die Regelmenge **vollzählig** lässt und dennoch das Ergebnis verschiebt — dafür bleiben Konfigurations-Freeze und B38-Prüfliste zuständig. **Keine Metrikänderung, keine Manifeständerung, keine Matrixzelle bewegt sich, kein Messergebnis betroffen.** | `c7_abbruch_bericht_aufrufspezifikation.md`; `data/soll/test_architecture.py`; `data/soll/importlinter.ini`; `data/soll/MANIFEST.md`; `c2c_bericht_k5_konfiguration.md` §B4/§B5; `c2b_bericht_k4_konfiguration.md` §B3/§B11; `c3a_bericht_clean_state_audit.md` §3a/§3b; `d2_bericht_vormessungen.md` M2/M5(c); `c3b_k3_bericht_kontrolllauf.md` §2; `k3_machbarkeitslauf_direktzugang_bericht.md` §3; B32; Protokoll §1 Nachtrag Rev. 30, §6 Nachtrag Rev. 24, Rev. 26, Rev. 29, Rev. 30 und Rev. 31 |

| 33 | 27.08.2026 | Kopf auf **Rev. 33** und Status auf **EINGEFROREN zur Vorregistrierung** (Alttext gestrichen sichtbar) · **§0 Punkt 2 — ENTSCHIEDEN: das Validitäts-Gate 0.9 aus §7 ist BESTÄTIGT, unverändert.** (a) Die technische Vorbedingung ist erfüllt — `valid_final=false`-Läufe sind über **Exit-Code 3** bzw. das **persistierte Run-Log** identifizierbar (CLI-Inkremente 2 und 4; der Messstand enthält Increment 7); stille Zählung invalider Läufe als „0 Findings" ist damit ausgeschlossen. (b) Beobachtungsstand, am 27.08.2026 aus den `llm_call`-Records ausgezählt, **nicht** aus Berichten übernommen: K2 (`data/c3b-k2/runs/`) **156/156 = 1.0**, K3 (`data/c3b-k3/runs/`) **156/156 = 1.0**, je 52 Invocations, `valid_raw` ebenfalls 156/156, `attempts_used` durchweg 1, `outcome` durchweg `measured` — **kein** Fall, in dem erst ein Repair-Versuch die Gültigkeit hergestellt hat; deckungsgleich mit `run_footer.calls_invalid: 0` / `invalid_reasons: []`. (c) Die Richtung der Regel ist **konservativ**: Unterschreitung führt zu **Dokumentation als Befund** und **Auswertung mit den vorhandenen validen Läufen**, ausdrücklich **OHNE Nachbesserung** — kein Prompt-Tuning (Eine-Iteration-Regel), kein selektives Nachmessen, keine Anpassung des Gates; die Regel kann ein Ergebnis nur verschlechtern oder unangetastet lassen. (d) **Der Zeitpunkt ist der Punkt:** die Bestätigung erfolgt **VOR dem ersten Kampagnenlauf**, die Anteile stammen ausschliesslich aus den Kontrollläufen auf der sauberen Baseline (C3b); eine Bestätigung **nach** Sichtung der Kampagnen-`valid_final`-Werte wäre **nicht mehr vorregistriert**, sondern an den Daten gewählt · **§0.1 NEU — Messstand (eingefroren).** Protokoll (Rev. 33; sein SHA256 wird im Freeze-Bericht geführt, weil ein Selbstbezug im gehashten Dokument unmöglich ist), Auswertungsspezifikation `2f1354bb…f6608f97`, die **sieben** Messeingänge aus `data/soll/SHA256SUMS` vollständig, Checker `phase04-freeze = 348ca9da…35297e` (Tag-Objekt `19e7a7a5…dfcac4`) mit Messpfad `~/ma/tritongraph-measure`, Checker-Artefakt `dist/cli.js` = `c0bbdfeb…d35d95`, Runner-Commit `70a2dd87…6fa9e95`, Testrepo `baseline = 0d651041…c0a66` mit 32 Tags `inj/01`–`inj/32` und Bundle `1b9f8b58…be508b`, Archivwurzel `/home/haasentimo/scratch/c7/out`. **Jeder Wert am 27.08.2026 aus Datei bzw. Repo gelesen**, keiner aus einem Bericht übernommen · **§0.1 — Regel für die Zeit nach dem Freeze.** Änderungen nur als **datierte Amendments mit Begründung**, geführt in Revisionshistorie **und** §10; **ab dem ersten Kampagnenlauf ändert KEIN Amendment mehr** Metrikdefinition, Injektionsmanifest, Regeldatei, Prompt oder Schema — Amendments danach dürfen **nur beschreiben, nicht festlegen**; die Defekt-Ausnahme aus §1 (ein Amendment, vollständiger Re-Run aller Konfigurationen) bleibt unverändert · **§6 — Klarstellung: der Graphmodus-Nachtrag Rev. 31 gilt für K1.** Der generische Wortlaut („`category_l1` → `full` bei `CYCLE`, sonst `diff`") deckte wörtlich gelesen **12** statt **4** Full-Läufe. Präzisiert: **K1** leitet den Modus aus der Kategorie ab, **K2/K3** tragen nach §6 Rev. 25/Rev. 24 **immer** `--rule-graph diff` für alle 32 Injektionen, **K4/K5** kennen den Schalter nicht (`n/a`). Belegt mit der C5-Planausgabe über 160 Invocations — **4 × `full`** (K1 auf I13–I16), **92 × `diff`** (K1 auf den übrigen 28, K2/K3 auf allen 32), 4 + 92 = 96 — und mit C4c Teil B (16 von 16 unter genau dieser Zuordnung). **Die Festlegung ändert sich nicht**, sie stand so in §6 Rev. 7, ist so gegengeprüft, so geplant und so implementiert (`run_campaign.build_matrix` setzt `full` nur für K1); präzisiert ist der **Protokolltext** · **§1 — Nachzug: die K3-Matrixzeile ist jetzt tatsächlich gestrichen.** Nachtrag Rev. 30 erklärte die Zeile „nemotron-120B (OpenRouter)" für überholt und schrieb, sie „bleibt gestrichen stehen" — **gestrichen war sie nicht**; Rev. 32 löste denselben Widerspruch für die **Aufrufzeilen** auf, nicht für die Matrix. Alte Zeile jetzt gestrichen, **Direktzugangszeile daneben** (`nvidia-nemotron-3-super-120b`, `https://inference.do-ai.run/v1`, kein Pin). **Keine Festlegung geändert** — verbindlich war der Direktzugang seit Rev. 30, der Kontrolllauf ist bereits über ihn gefahren; korrigiert ist allein der Aufschrieb. **Insgesamt: keine Metrikänderung, keine Manifeständerung, keine Zelle der Erwartungsmatrix bewegt sich, kein Messergebnis betroffen.** | `data/c3b-k2/runs/*.jsonl`; `data/c3b-k3/runs/*.jsonl`; `c3b_k2_bericht_kontrolllauf.md`; `c3b_k3_bericht_kontrolllauf.md`; `c5_bericht_freeze.md` §8 (Planausgabe) und §3 (Freeze-Tag, Worktree); `c4c_bericht_vorabpruefung.md` Teil B; `c5b_bericht_protokoll_freeze.md`; `data/soll/SHA256SUMS`; `data/testrepo/SHA256SUMS`; `tools/run_campaign.py`, `tools/campaign_spec.py` (Commit `70a2dd8`); Protokoll §1 Nachtrag Rev. 30, §4 Nachtrag Rev. 25, §6 Rev. 7, Rev. 24 und Nachtrag Rev. 31, §7 Validitäts-Gate |
| 34 | 27.08.2026 | Kopf auf **Rev. 34** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **§0.1 — Amendment: die Archivwurzel der Kampagne wandert von ~~`/home/haasentimo/scratch/c7/out`~~ nach `~/ma/masterarbeit/data/campaign/`**, einen **versionierten** Pfad im Thesis-Repo neben `data/c3b-k2/`, mit unveränderter Unterordnerstruktur `k1/`…`k5/` und `manifests/`. Der Pfad ist **nicht hart verdrahtet**, sondern Vorgabe des CLI-Parameters `--out` (`CAMPAIGN_OUT` in `tools/run_campaign.py`), damit ein Rauchtest weiterhin an der Kampagne vorbei ablegen kann · **Mitgezogen: die Zeile Runner in §0.1** — sie bezeichnet „den letzten Commit, der eine dieser drei Dateien berührt", und `tools/run_campaign.py` ist berührt: ~~`70a2dd8`~~ → **`b6f9972`** (`b6f9972067f6c7b4288c14bb52723f5c8a4a7a82`); `campaign_spec.py` und `postrun_check.py` sind unverändert · **Was sich NICHT ändert, ausdrücklich:** keine **Messgrösse**, kein **Messeingang** (die sieben `data/soll/`-Hashes stehen zeichengleich), keine **Metrik**, keine Zelle der Erwartungsmatrix, keine Aufrufsemantik, kein Checker-Tag, kein Build-Hash, keine Testrepo-Baseline. **Belegt:** erneuter `--plan`-Lauf, **Exit 0**, **160 Invocations / 192 Model-Calls / 480 Zielpfade, alle eindeutig** — gegen die C5-Planausgabe nach Normalisierung des Pfadpräfixes **zeichengleich bis auf den Erzeugungszeitstempel**; das Präfix trägt in beiden Ausgaben genau **577** Zeilen · **Zeitpunkt:** die Änderung erfolgt **VOR dem ersten Kampagnenlauf**; es existiert kein Messbestand, der umzuziehen wäre, und keine Auswertung, an der sie gewählt sein könnte | **§6 Punkt 4 verlangt, die Rohlogs unverändert zu archivieren; ein Scratchpad-Verzeichnis ist flüchtig und trägt sie nicht.** Der **C4c-Verlustfall** ist der Beleg: die sechzehn `--run-log`/`--json-out`-Dateien der Vorabprüfung liegen laut `c4c_bericht_vorabpruefung.md` Teil C „im flüchtigen Arbeitsverzeichnis dieses Auftrags" und sind **bewusst nicht abgelegt** — bei einer Kontrolle vertretbar, bei der Kampagne ein Verstoss gegen §6 Punkt 4. Ein versionierter Pfad unter `data/` macht die Rohlogs hashbar (`SHA256SUMS`/`MANIFEST.md` nach der Kampagne) und damit bezeugbar. Belege: `c5c_bericht_archivwurzel.md`; `c5_bericht_freeze.md` Anhang A (Vergleichsausgabe); `c4c_bericht_vorabpruefung.md` Teil C; Protokoll §6 Punkt 4, §0.1 |
| 35 | 27.08.2026 | Kopf auf **Rev. 35** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **DEFEKT: Validator-Punkt (6), Z2′ (ii) „sole importer per component“, wurde als commit-invariant geführt und ist es nicht.** Der Punkt zählt Kanten des **Codegraphen**, nicht Eigenschaften des **Soll-Modells**; unter einer `FORBIDDEN_RELATION`-Injektion auf ein Ziel mit genau einem Ruhezustands-Importeur ist er **zwangsläufig** verletzt. Betroffen **I07, I08, I09**, Ziel `core_adapters_internal`. Der Kampagnenlauf C10 brach an I07 ab, bevor ein Call entstand · **KLASSIFIKATION der acht Validator-Punkte** in commit-invariante Soll-Eigenschaften **(1)–(5)** und commit-variante Codegraph-Eigenschaften **(6)–(8)**, je mit einem Satz Begründung (Tabelle in der Revisionshistorie im Kopf) — der eigentliche Ertrag: die nächste Injektionsmenge läuft nicht mehr blind in dieselbe Wand · **NEUE REGEL für (6):** erwartet wird die **exakte Importeursmenge** je geschützter Komponente, **berechnet** aus dem whitelisted Importeur in `depot_soll.ilograph.yaml` plus der Quellkomponente der in `expected_edge_boundary` registrierten Kante — dieselbe Quelle, gegen die (7) und (8) geführt werden. Abbruch weiterhin bei mehr als einem zusätzlichen Importeur, einem anderen als dem registrierten, fehlendem Ruhezustands-Importeur und jeder Abweichung an einer unberührten Komponente. `--plan` gibt die erwarteten (6)-Werte je Injektion aus, wie schon (7)/(8) · **SCHÄRFEND, nicht lockernd:** Rev. 34 verglich eine **Zahl** (`len(importers) == 1`) und sah nie nach, **welche** Komponente importiert; Rev. 35 vergleicht die **Menge** — ein Lauf mit fremdem statt eigenem Importeur bei unveränderter Anzahl bricht jetzt ab und wäre vorher durchgelaufen · **KEINE gesperrte Änderung**, vier Punkte: **(a)** der registrierte Entwurf verlangt die Commit-Schärfe ausdrücklich (`docs/planung/offene_punkte.md` C7, Zusatz 12.08.: Soll-Validator je Lauf „mit der für den **jeweiligen Commit** erwarteten“ Phantommenge); **(b)** berührt sind **weder Metrik noch Manifest, Regeldatei, Prompt oder Schema** — die fünf Gegenstände der Sperre aus §0.1 Punkt 2 —, sondern allein eine **Vorbedingung des Runners**; **(c)** die Erwartung ist aus den Messeingängen **berechnet**, nicht gewählt, nichts hart verdrahtet, nichts aus einem Bericht abgetippt; **(d)** ein schärferes Gatter kann ein Ergebnis nur verwerfen, nie herbeiführen · **ZEITPUNKT UNGESCHMINKT — dieses Amendment steht NACH dem ersten Kampagnenlauf.** Am 27.08.2026 um 08:25 liefen **sechs K2-Invocationen** (I01–I06, 18 Calls, `valid_final` 18/18, Fenster 4096, max `tokens_in_total + tokens_out_total` 1599). Sie sind **verworfen**: nicht ausgewertet, nicht committet, aus `data/campaign/` entfernt und nach `~/scratch/c10a/abgebrochener_k2_teilbestand/` abgelegt, SHA256 je Datei im C10a-Bericht. **K2 wird vollständig neu gefahren**, damit der Block unter **einem** Runner-Commit steht. Die Eine-Iteration-Regel (§7) galt durchgehend: an dem Teilbestand wurde keine Metrik berechnet und kein Finding beurteilt · **Mitgezogen: die Zeile Runner in §0.1** — ~~`b6f9972`~~ → **`4caf083`** (`4caf083d5e21f36440579af6888513ca897f1dd4`); `campaign_spec.py` und `postrun_check.py` sind unverändert · **Belegt:** Gegenprobe über alle 32 Tags mit der neuen Logik, **32 von 32 passieren**, I07/I08/I09 mit exakt der registrierten Importeursmenge; Schärfeprobe gegen vier falsche Mengen bricht in allen vier Fällen ab; `--plan` Exit 0, **160 Invocations / 192 Model-Calls / 480 Zielpfade, alle eindeutig**, gegen die C5c-Ausgabe zeichengleich bis auf den (6)-Block und den Zeitstempel | **Der Abbruch war das Kriterium, nicht die Injektion.** Punkt (6) prüft eine Eigenschaft des Codegraphen mit dem Anspruch einer Soll-Eigenschaft; das ist genau der Fehler, den die Klassifikation oben ausräumt. Belege: `c10a_bericht_validator_punkt6.md`; `c10_bericht_kampagne.md` (Abbruchbefund); `docs/planung/offene_punkte.md` C7 Zusatz 12.08.; `data/soll/depot_soll.ilograph.yaml` (whitelisted Importeure); `data/soll/injection_manifest.json` (`expected_edge_boundary`); `tools/validate_soll.py` `SOLE_IMPORTER`; `tools/run_campaign.py` Commit `4caf083`; Protokoll §0.1, §3 Nachtrag Rev. 29, §7 |
| 36 | 27.08.2026 | Kopf auf **Rev. 36** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **NACHREGISTRIERUNG eines bereits vollzogenen Bytewechsels — dieses Amendment BESCHREIBT nur, es legt nichts fest** · **Was C6b-2b geändert hat, und zwar richtig:** die Auswertungsspezifikation `docs/protokolle/c6_auswertungsspezifikation.md` ist an drei Stellen **ergänzt** — §10.4 (offener Punkt 4, K4/K5-Matchregel, ERLEDIGT), §6.2 (korrigiert: Parameter der Test-ID der vier Portregeln ist die `rule_id`, nicht der Modulname, belegt an `data/soll/test_architecture.py:309-310`), §1.4 (erweitert um die **Terminalbreite** der K4-Messung, `console.width = 80`, `is_terminal = False`). Der SHA des **registrierten Auswertungseingangs** ändert sich damit notwendig: ~~`2f1354bb…f6608f97`~~ → **`8f6d3580…82c37749`**, in `0c1cc34` an **beiden** vorgeschriebenen Stellen nachgezogen — §1 (Nachtrag Rev. 30) **und** §0.1 (Messstand) —, im **selben Commit** wie die Spezifikationsänderung. **Dieser Nachzug war richtig und von der Repo-Regel verlangt**; er wird hier nicht revidiert, sondern registriert · **WAS DABEI UNTERBLIEB, ungeschminkt:** der Nachzug wurde **ohne Kopf-Revision, ohne Historieneintrag und ohne §10-Zeile** vollzogen. Das Protokoll trug danach unverändert „Rev. 35“ im Kopf, während seine Bytes nicht mehr die von Rev. 35 waren; sein SHA wechselte von `876680b13c568312059d9143b146617b3be6887e5e89a2badfd05c5361f3b910` auf `620f11739d65ba759ea8b78eb2d710be684c40fb4c52e9e3d74a7464283d80d3` — und **dieser Bytestand war in keinem Dokument bezeugt**. Er ist jetzt in `c5b_bericht_protokoll_freeze.md` §3 als Zwischenstand nachgetragen, **nie als Revision geführt** · **WIE ES AUFFIEL:** an der **Bewegungsprüfung** von C6b, die den Protokoll-SHA gegen den in `c5b_bericht_protokoll_freeze.md` §3 geführten Wert vergleicht. Sie schlug an, der Auftrag brach ab, bevor eine Zeile Harness geschrieben war — **die Prüfung hat funktioniert, ihr fehlte der Vergleichswert** · **DIE LESART, ab jetzt verbindlich (§0.1 Punkt 5): JEDE Änderung am Protokoll ist eine Revision, auch ein reiner Hash-Nachzug.** Zwei unabhängig tragende Gründe: **(a)** eine Ausnahme für „inhaltsneutrale“ Bytewechsel verlangte ein **Urteil darüber, welche Änderung substanziell ist**, und genau dieses Urteil nimmt der Freeze aus dem Verkehr; **(b)** der Protokoll-SHA ist der **Anker der Bewegungsprüfung** und als Detektor nur brauchbar, wenn **kein** Bytewechsel unregistriert bleibt — ein einziger geduldeter Wechsel macht jede spätere Abweichung mehrdeutig · **DER RIEGEL:** `tools/check_doc_invariants.py`, **ausschliesslich lesend**, Exit 0/1, prüft (a) Protokoll-SHA gegen c5b §3, (b) Kopf-Revision = höchste §10-Zeile = oberster Historieneintrag, (c) Spezifikations-SHA gegen §1 **und** §0.1 getrennt, (d) `sha256sum -c` in `data/soll` und jedem `data/campaign`-Unterordner mit `SHA256SUMS`; läuft als Vorbedingung jedes schreibenden Auftrags (`CLAUDE.md`) · **AUSDRÜCKLICH:** **keine** Metrikdefinition, **kein** Injektionsmanifest, **keine** Regeldatei, **kein** Prompt, **kein** Schema berührt — die fünf Gegenstände der Sperre aus §0.1 Punkt 2; **keine Zelle der Erwartungsmatrix bewegt sich, kein Messergebnis betroffen**, kein Wert der §0.1-Tabelle ändert sich. Die Sperre ist gewahrt, weil dieses Amendment **ausschliesslich beschreibt**, was bereits geschehen ist | **Ein Bytewechsel am eingefrorenen Protokoll, der in keinem Dokument bezeugt ist, macht den Anker der Bewegungsprüfung unbrauchbar** — nicht die Änderung war der Fehler, sondern ihre fehlende Registrierung. Belege: `c6b0a_bericht_invarianten.md`; `c6b2_bericht_matchregel.md` (die Spezifikationsänderung und ihre Vorbedingungstabelle mit dem damals korrekten Ausgangswert `876680b1…61f3b910`); Commit `0c1cc34`; `c5b_bericht_protokoll_freeze.md` §3 (die drei bezeugten Stände plus der nachgetragene Zwischenstand); Protokoll §0.1 Regel für die Zeit nach dem Freeze, Punkt 1 und neuer Punkt 5; `tools/check_doc_invariants.py` |
| 37 | 28.08.2026 | Kopf auf **Rev. 37** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **ENTSCHEIDUNG einer Zweideutigkeit, gesetzt VOR ihrer ersten wirksamen Anwendung** · §7.2 der Auswertungsspezifikation verlangte, die beiden vorregistrierten Meldungen des Clean-Control-Sets (§5 Fälle 4 und 5) „aus dem Zähler der Headline-Rate **herauszurechnen** und separat auszuweisen“; die Ergebniszeile des K2-Berichts führt dieselben Meldungen „getrennt **darin** enthalten“ (`c3b_k2_bericht_kontrolllauf.md` §4.2). **Entschieden: sie BLEIBEN im Zähler und werden GETRENNT AUSGEWIESEN — NICHT herausgerechnet.** Die Headline-Rate zählt die Kontrollmodule mit ≥ 1 Finding, **alle Findings**; die zweite Lesart wird mitgeführt, ist aber nicht die Headline. §7.2 der Auswertungsspezifikation entsprechend geändert (Alttext gestrichen), SHA256 des Auswertungseingangs an **beiden** Stellen nachgezogen — §0.1 und §1 Nachtrag Rev. 30 —, im **selben Commit**; `tools/evaluate_campaign.py` rechnet die entschiedene Lesart. | **(a)** Die Herausrechnung **verbesserte** die K2-Falsch-Positiv-Rate, also die gemessene Grösse, und wäre **gewählt** statt von der Messung erzwungen — von einer an den Daten gewählten Festlegung nachträglich nicht zu unterscheiden (§0.1 Punkt 4). **(b)** Sie widerspräche der Auflage aus §5 Amendment 11.08.: `localized` nie ohne die **vollständige** FP-Rate. **(c)** Eine vorhergesagte Meldung ist auf sauberem Code trotzdem eine Meldung — **Vorhersagbarkeit ist ein Zusatz, kein Abzug**. **Zeitpunkt:** auf dem Kontrollbestand ergeben beide Lesarten **49**, im Fixture **3/6 gegen 4/6** — die Entscheidung fällt **vor** ihrer ersten wirksamen Anwendung, der Auswertungslauf über `data/campaign/k*` hat nicht stattgefunden. **Keine Metrikdefinition geändert:** der Zähler ist seit Rev. 3 „Zahl der Kontrollmodule mit ≥ 1 Finding“, und die entschiedene Lesart ist dessen **wörtliche** Anwendung; verworfen ist der Zusatz, der ihn einschränkte. Kein Injektionsmanifest, keine Regeldatei, kein Prompt, kein Schema, keine Matrixzelle berührt. Anlass: C6c, `c6c_bericht_selbsttest_freeze.md`. |
| 38 | 28.08.2026 | Kopf auf **Rev. 38** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **§0.1 — Amendment: die drei AUSWERTUNGSINSTRUMENTE sind mit SHA256 in den Messstand aufgenommen**, gesetzt **VOR** dem ersten Auswertungslauf über `data/campaign/k*`: `tools/evaluate_campaign.py`, `tools/match_k4k5.py` und `tools/check_doc_invariants.py` — der Prüfer **registriert sich selbst mit**. Dazu **Punkt 6** der Amendment-Regel unter §0.1: ab dem ersten Auswertungslauf ist jede Änderung an diesen drei Dateien eine **datierte Revision mit Begründung**, **keine** darf eine **Rechenregel** oder einen **Marker** verschieben, zulässig ist allein die **Behebung eines Defekts** — mit **vollständiger Neuauswertung** und **Ausweis beider Ergebnisse**, nebeneinander und nicht ersetzend. Maschinell geprüft durch `tools/check_doc_invariants.py` **Invariante (E)**. | Der Messstand bezeugte den **Eingang** und — über die Bewegungsprüfung — Protokoll und Auswertungsspezifikation, **nicht** den Weg dazwischen. Eine stille Änderung an `false_positive_rates()`, an `NB_CELLS` oder an einer Zellenregel in `tools/match_k4k5.py` verschöbe **jede** Tabelle des Kapitels 7, **ohne** dass ein einziger registrierter Wert sich bewegte — die Bewegungsprüfung über die Eingangshashes bliebe **grün**. Dieselbe Begründung, mit der C6b-0a den Protokoll-SHA als Anker eingesetzt hat (Rev. 36): ein Detektor taugt nur, wenn **kein** Bytewechsel unregistriert bleibt. **Keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein Prompt, kein Schema berührt** — dieses Amendment **beschreibt** einen Bytestand und legt eine **Änderungssperre** darauf. Anlass: C6c, `c6c_bericht_selbsttest_freeze.md`. |

| 39 | 28.08.2026 | Kopf auf **Rev. 39** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **(1) §0.1 / T7 — die QUELLE von T7 wechselt auf die GEHASHTEN LAUFMANIFESTE** unter `data/campaign/manifests/`, ein Manifest je Invocation, jedes von einem Block-`SHA256SUMS` bezeugt. Gelesen werden `postrun.verdict`, `invalid_reasons`, `calls_total`, `calls_invalid`, `calls_transport_failed`, `changed_files_count`, die K4/K5-Akzeptanzzähler und `external_wall_clock_ms`; **`valid_final` ist kein Feld, sondern eine Ableitung** und wird als solche ausgewiesen. `journal.jsonl` und die Prosa-`MANIFEST.md` sind seither **GEGENPROBE, nicht Quelle**; eine Abweichung ist ein **Befund** (`ABWEICHUNG` in T7, Banner im Kopf der Ausgabe, `stderr`), **keine Seite wird an die andere angeglichen** · **(2) Ausnahmeregel für LEBENDE DOKUMENTE — entschieden, nicht offen.** Die sieben ungelisteten Dateien (`data/soll/MANIFEST.md`, `data/campaign/MANIFEST.md`, `data/campaign/README.md`, `data/campaign/journal.jsonl`, `data/campaign/control/journal.jsonl`, `data/campaign/k2/MANIFEST.md`, `data/campaign/k3/MANIFEST.md`) werden **NICHT** in ein `SHA256SUMS` aufgenommen; sie werden weiterhin bei jedem Prüferlauf gemeldet, aber als **bekannte, entschiedene Ausnahme**, nicht als Fehlschlag. Die Liste steht **namentlich im Code** (`KNOWN_UNLISTED`), damit eine **achte** ungelistete Datei als **Fehlschlag** auffällt · **(3) PRÄZISIERUNG der Blindheitsauflage:** Funde bleiben gesperrt (`--json-out`, Run-Log-Records, stdout/stderr der Kampagne), die **Laufmanifeste sind ausdrücklich erlaubt** — Verdikte, Zähler, Provenienz, **keine Funde**. Die Selbstauditierung der Harness ist **angepasst, nicht ausgeschaltet**, und dabei **schärfer** geworden: positive Erlaubnisliste statt Aufzählung der Blockordner, jeder andere Pfad unter der Kampagnenwurzel **Exit 3**, `data/campaign/control/` eingeschlossen — das die alte Prüfung gar nicht sah · **Mitgezogen:** Auswertungsspezifikation (neues §1.8, §7.4 lebende Dokumente, §8 Punkt 9) mit SHA an **beiden** Stellen (§0.1 und §1 Nachtrag Rev. 30), und die drei Instrumentenhashes in §0.1 (§0.1 Punkt 6), weil `tools/evaluate_campaign.py` und `tools/check_doc_invariants.py` geändert sind · **Gemessen, alle drei Lesungen deckungsgleich:** K1/K2/K4/K5 je 32 Invocationen, K3 61 (29 INVALID, durchgehend `transport_failure`); **32 von 32 Injektionen gültig in jeder Konfiguration**, keine `n. e.`-Zelle; `valid_final` K2 96/96, K3 133/133, je 1,000, Gate 0,9 nirgends unterschritten | **T7 ist die Tabelle, die den Messbestand bezeugt; sie darf nicht auf ungehashten Dateien ruhen.** Journal und Prosa-Manifeste sind planmäßig ungehasht — append-only bzw. fortzuschreibend —, und ein Hash wäre für sie das falsche Instrument: er risse bei jeder legitimen Fortschreibung und erzöge dazu, ihn nachzuziehen, was den Detektor zerstört (dieselbe Detektorlogik wie Rev. 36 für den Protokoll-SHA). Die Laufmanifeste tragen **dieselben Zahlen** und sind gehasht; die Umstellung bewegt **keinen Messwert**, nur die Datei, aus der er gelesen wird. **Keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein Prompt, kein Schema berührt**, keine Zelle der Erwartungsmatrix. Anlass: C6c-a, `c6ca_bericht_t7_quellen.md`; Belege: `data/campaign/manifests/*.json`, `data/campaign/MANIFEST.md`, `data/campaign/k3/MANIFEST.md`, `data/campaign/journal.jsonl`, `tools/evaluate_campaign.py`, `tools/check_doc_invariants.py`, `docs/kapitel/kapitel7_tabellenskelette.md` T7. |



**Amendments nach Messbeginn:**

| Nr | Datum | Änderung | Begründung | Re-Run |
|---|---|---|---|---|
| 40 | 28.08.2026 | Kopf auf **Rev. 40** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **(a) §5 Rev. 31 / §7.5 (3) — kein-EN WIRD AUF EINER AGGREGATIONSSTUFE GEBILDET: der EXISTENZSTUFE.** Der Wortlaut aus Rev. 31 bleibt **wörtlich stehen**; gebildet wird kein-EN jetzt als `strict` (Existenz über die drei Repetitionen, §4, unverändert) gegen die **Existenz** derselben Zählgrösse im Ruhezustand — statt bisher `strict` (Existenz) gegen einen **Median**. Begründung: der Wortlaut macht **den `strict`-Treffer zum Subjekt**, `strict` ist nach §4 ein Existenzquantor und als **Metrikdefinition** nach §0.1 Punkt 2 gesperrt; die Stufe des Subjekts ist damit die zu wählende, und die Ruhezustandsseite folgt ihr. **Beide Kandidaten gegenübergestellt** (Revisionshistorie Rev. 40, Tabelle): **Kandidat A (Existenzstufe, gewählt)** bewegt **2 von 32** kein-EN-Zeilen bei K2 (I10, I12: `nein`→`ja`) und **4 von 32** bei K3 (I06, I20, I21: `ja`→`nein`; I30: `nein`→`ja`) — **in beide Richtungen**, drei je Seite, und bewegt **keine** vorregistrierte Zelle. **Kandidat B (Medianstufe, verworfen)** bewegt 1 bzw. 3 Zeilen, aber **nur in eine Richtung** und verschöbe **vier vorregistrierte `strict`-Zellen** (I06/K3, I19/K2, I20/K3, I21/K3 von 1 auf 0) und mit ihnen T1, T2, T4 und T5 — eine Metrikdefinition nach Sicht auf die Daten, ausgeschlossen durch §0.1 Punkt 2. **Kein Ergebnis wird verbessert:** bei K2 steigt die Zahl der Zeilen ohne Erkennungsnachweis von 20 auf 22, bei K3 sinkt sie von 4 auf 2. **NICHT geändert:** die Spalten `Ruhe`, `Kampagne`, `Δ` bleiben auf dem Median (eigenständige paarweise Auslesart nach §7.5 (4), beide Seiten dort bereits gleich aggregiert; kein-EN liest sie seither nicht mehr) · der **Filterunterschied** `match_key` gegen Trägermodul+Kategorie bleibt bestehen, beide Filter sind vorregistriert, dieses Amendment betrifft die **Stufe**, nicht den Filter · `strict` selbst · Precision, Recall, F1, Median, Spannweite, FP-Rate · **(b) T4 — NEUE SPALTE „Läufe (Ruhe · Kampagne)“ je Konfiguration**: die drei Repetitionszählwerte **einzeln** (`[0,0,0] · [0,0,1]`) statt zweier gedruckter Mediane `0`. **Rein deskriptiv**, keine Wertung, keine Aggregation, kein Eingang in eine Rechnung — sie macht die Aggregationsstufe an der Tabelle **lesbar** · **(c) ABGELEHNT, ausdrücklich registriert: kein-EN wird NICHT nach Ursache aufgespalten.** Eine Spalte „Rauschen gegen Instabilität“ wäre eine **neue, nach Sicht auf die Daten gebildete Klassifikation** — die Klassen existierten vor dem ersten Lauf nicht, ihre Grenze läge an genau den Zeilen, die sie sortieren soll (§0.1 Punkt 4). Der Ursachenunterschied (C11a §3.6) gehört in die **Prosa von Kapitel 7**, belegt aus der neuen Läufespalte | **ZEITPUNKT UNGESCHMINKT: NACH dem ersten Auswertungslauf und NACH der Diagnose C11a.** Zulässig als **Metrikbildung, nicht Metrikdefinition**: die Regel aus Rev. 31 bleibt wörtlich, ihre Umsetzung wird auf **eine** Stufe gebracht — eine Frage, die Rev. 31 offengelassen und die die C6b-Umsetzung stillschweigend in zwei Richtungen beantwortet hat (C11a §3.5, Arbeitslistenpunkt 11 „OFFEN — benannt, nicht entschieden“). Belege: `c11a_bericht_diagnose.md` §3, `c11b_bericht_zweiter_lauf.md` | **JA — vollständige Neuauswertung** über den gesamten Bestand als `data/campaign/eval/c12_eval_full.*`; der erste Lauf `c11_eval_full.*` bleibt **archiviert, gehasht und unverändert daneben** und wird Zelle für Zelle gegenübergestellt (§0.1 Punkt 6) |
| 41 | 28.08.2026 | Kopf auf **Rev. 41** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **§0.1 — HASH-NACHZUG DER AUSWERTUNGSINSTRUMENTE nach der Reparatur R1–R9.** `tools/evaluate_campaign.py` ~~`5125cd59…0528eed`~~ → **`20bcdae0…23d306`**, `tools/match_k4k5.py` ~~`ad3edcb1…fc060022`~~ → **`c16e7c43…799f4ca6`**; `tools/check_doc_invariants.py` **unverändert**. **Eine eigene Revision, obwohl reiner Bytestandsnachzug** — §0.1 Punkt 5: jede Änderung am Protokoll ist eine Revision, auch eine, die inhaltlich nichts verschiebt. Rev. 40 hatte den Nachzug angekündigt; unter derselben Nummer vollzogen, stünde der Bytestand von Rev. 40 in keinem Dokument mehr | **Defektklausel §0.1 Punkt 6.** Behoben sind die Punkte aus `c11a_bericht_diagnose.md` §7: **R8/R7** Buchung der vorregistrierten Sonderklasse T9 Fall 7 (der Join verwarf sie an zwei Zeichenkettenvergleichen, der T9-Zähler las aus dem falschen Eimer) — repariert **über die Klassifikation des Parsers**, nicht am Literal · **R2** gerechnete Nullen wurden als leere Zelle gedruckt · **R1** neue Zusicherung „keine markerfreie Leerzelle“, geprüft am gerenderten Text, Exit 2 · **R3/R4** T5 und T6 waren nicht implementiert bzw. nicht gerendert (165 + 31 Zellen) · **R5** T4-Symmetrieteil, dabei ein Defekt der Zählgrösse behoben, die auf dem K1-Pfad nie traf · **R6** T1-Abweichungsspalte · **R9** T9 in Skelettform · die laufweise Bildung der `strict`-FP nach §3.2 · die Umsetzung von Rev. 40. **KEINE Rechenregel und KEIN Marker verschoben**, wie §0.1 Punkt 6 verlangt; belegt durch die **vor** der Reparatur allein committete Handrechnung (`tests/fixtures/harness/EXPECTED.md` §11–§15) und durch Selbsttest B, der K2 49/52 und 461, K3 1/52 und 3 unverändert reproduziert | **JA — derselbe Re-Run wie Rev. 40**, ein Lauf für beide Revisionen: `c12_eval_full.*`. Der erste Lauf `c11_eval_full.*` bleibt archiviert, gehasht und unverändert daneben |
| 42 | 28.08.2026 | Kopf auf **Rev. 42** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **§7.5 Punkt 1 der Auswertungsspezifikation und Skelett T5 (ii) — DIE FORDERUNG NACH MEDIAN UND SPANNWEITE ÜBER DREI LÄUFE IST FÜR DIE P/R/F1-TABELLE GEGENSTANDSLOS UND DAMIT ERLEDIGT; sie wird NICHT abgewiesen.** Median und Spannweite setzen eine **laufweise** Grösse voraus. Precision, Recall und F1 dieser Tabelle stehen auf `strict` und `localized`; `strict` ist nach Spezifikation **§3** ein **Existenzquantor über die Repetitionen** und hat konstruktiv **keine Verteilung über Läufe**, über die ein Median zu bilden wäre. Eine laufweise Fassung wäre keine zweite Auslesart derselben Metrik, sondern eine **neue Metrikdefinition** — gesperrt nach §0.1 Punkt 2. Die Anforderung zu erfüllen hiesse also, die Sperre zu brechen; sie offen stehen zu lassen hiesse, eine konstruktiv unerfüllbare Forderung als Lücke zu führen · **Die Laufstreuung wird an der dafür vorregistrierten Stelle ausgewiesen, und feiner:** die mit **Rev. 40** eingeführte T4-Spalte **Läufe (Ruhe · Kampagne)** trägt die Zählgrösse **je Repetition einzeln** (`[0,0,1]`, Spezifikation §7.5 (5)) — nicht zu einem Median zusammengezogen · **NICHT BERÜHRT: §7.5 Punkt 2.** Die Falsch-Positiv-Raten-Tabelle führt Median **und** Spannweite über drei Läufe für K2/K3 **unverändert** weiter; dort ist die Headline-Rate eine **je Lauf** gebildete Grösse (§7.1). T3 druckt sie wie bisher · **AUSDRÜCKLICH: keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein Prompt, kein Schema berührt** — die fünf Gegenstände der Sperre. `strict`, `localized`, Precision, Recall, F1, Median, Spannweite, FP-Rate und die vier Marker stehen unverändert; **keine Zelle der Erwartungsmatrix bewegt sich, kein Messergebnis ist betroffen**. Dieses Amendment **beschreibt** eine Eigenschaft, die `strict` seit §3 hat, und zieht die Folge daraus — es legt nichts fest, was nicht schon galt · **Mitgezogen:** der SHA der Auswertungsspezifikation an **beiden** Stellen (§1 Nachtrag Rev. 30 und §0.1 Messstand), ~~`be3491e2…acb21d6e1`~~ → **`fe991be6…092c20d1`**, im **selben Commit** wie die Spezifikationsänderung · **Der Aufschrieb aus Phase 1 desselben Auftrags berührt keinen gehashten Wert:** die korrigierte Zeilenbeschriftung der T5-Gesamtzeilen steht im **Tabellenskelett**, das weder in §0.1 noch in einer `SHA256SUMS` geführt wird und keines der drei Auswertungsinstrumente ist — es gibt dort nichts nachzuziehen | Eine vorregistrierte Anforderung, die aus der **Konstruktion der Metrik** heraus leerläuft, darf weder stillschweigend gestrichen noch als dauerhaft offene Lücke geführt werden: das erste verwischt die Vorregistrierung, das zweite behauptet einen Mangel, wo eine definitorische Eigenschaft steht. Belege: `c6_auswertungsspezifikation.md` §3 (Existenzquantor), §7.1, §7.5 Punkte 1, 2 und 5; Protokoll §0.1 Punkt 2 (Sperre) und Revisionshistorie Rev. 40 (T4-Läufespalte); `c11b_bericht_zweiter_lauf.md` §8 (die Lücke benannt und nicht gefüllt); `kapitel7_tabellenskelette.md` T5 (ii) | **nein** — keine Rechenvorschrift bewegt, keine Zelle rechnet anders |
| 43 | 28.08.2026 | Kopf auf **Rev. 43** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **§0.1 — HASH-NACHZUG DER AUSWERTUNGSINSTRUMENTE nach der Darstellungsreparatur D1–D3, gesetzt NACH dem zweiten Auswertungslauf und VOR dem dritten.** Ein reiner Bytestandsnachzug und deshalb nach §0.1 Punkt 5 **eine eigene Revision**, **nicht** unter Rev. 42 mitvollzogen: dort stünde der in `c5b_bericht_protokoll_freeze.md` §3 bezeugte Bytestand von Rev. 42 in keinem Dokument mehr — der Ausfall aus C6b-2b, aus dem Rev. 36 diese Regel gemacht hat (dieselbe Trennung wie Rev. 40/41) · **Ein Instrument geändert:** `tools/evaluate_campaign.py` ~~`20bcdae0…23d306`~~ → **`eb206a6f…b520653`**; `tools/match_k4k5.py` und `tools/check_doc_invariants.py` **unverändert** · **Anlass: die Defektklausel §0.1 Punkt 6, und die Defekte sind AUSSCHLIESSLICH DARSTELLEND.** **D1** T5 druckte seine Marker **ohne Code-Auszeichnung** (72 Zellen im zweiten Lauf) — `Score.cells()` gab den rohen Markerstring zurück, jede andere Tabelle lief über `Cell.text`; ein Marker ohne Auszeichnung ist von Prosa nicht zu unterscheiden, und die drei Marker tragen drei verschiedene Aussagen (Skelett §1.1). `marker_text()` ist jetzt die **einzige** rendernde Stelle · **D2** T6 druckte zwei K3-Millisekundensummen in **Exponentialschreibweise** (`9.19054e+06 ms`), der `%g`-Rückfall oberhalb sechs signifikanter Stellen; `plain()` rendert denselben Wert ohne Exponent, alle übrigen `%g`-Aufrufstellen laufen darüber · **D3** Nachschau über **alle** Tabellen nach beiden Klassen: **zwei** weitere Zellen — die Headline-Zellen der findingweisen T3-Zeilen trugen einen **blossen Gedankenstrich**; **nur die Auszeichnung** ist ergänzt. Gedankenstriche **in Fliesstext** sind Interpunktion, keine Marker, und bleiben unangetastet · **R10 neu**, geprüft am **fertig gerenderten** Text wie R1: kein Marker ohne Code-Auszeichnung, keine Zahl in Exponentialform, Exit 2 · **AUSDRÜCKLICH: KEINE Rechenregel, KEIN Filter, KEIN Nenner, KEINE Aggregationsstufe berührt.** `strict`, `localized`, Precision, Recall, F1, Median, Spannweite, FP-Rate und die vier Marker stehen unverändert; verschoben ist allein die **Notation** auf bereits gerechnetem Text. **Keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein Prompt, kein Schema** ist berührt · **Belegt, nicht behauptet:** `match_k4k5.py --selftest` **34/34**, Selbsttest B unverändert (K2 **49/52** und **461**, K3 **1/52** und **3**), Fixture-Lauf **60** geänderte Zellen — **50** reine Auszeichnung, **10** die Zeilenbeschriftung aus Rev. 42 —, jede Zusicherung negativ probiert, R10 in **beiden** Hälften · **Der erste und der zweite Auswertungslauf bleiben archiviert, gehasht und unverändert**; der dritte tritt **daneben** | Ein Bytewechsel an einem Auswertungsinstrument, der unter der Nummer einer bereits bezeugten Revision vollzogen wird, macht deren Bytestand unbezeugt (§0.1 Punkt 5, Präzedenz Rev. 36 und Rev. 41). Belege: `c11b_bericht_zweiter_lauf.md` §7 (die beiden Darstellungsabweichungen, ausgewiesen und nicht behoben), `c11c_bericht_dritter_lauf.md` §3 und §5, Protokoll §0.1 Zeile Auswertungsinstrumente und Punkt 6, `c5b_bericht_protokoll_freeze.md` §3 | **ja** — vollständige Neuauswertung über den **unveränderten** Kampagnenbestand, keine Neumessung; der dritte Lauf muss nach Normalisierung zum zweiten zeichengleich sein |
| 44 | 28.08.2026 | Kopf auf **Rev. 44** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **(a) ARTEFAKTAUSWAHL — Auswertungsspezifikation §1.9 NEU.** Welches Laufartefakt je Paar (Konfiguration, Injektion) gelesen wird, entscheidet **`postrun.verdict` des gehashten Laufmanifests**; bei mehreren gültigen Versuchen der **früheste** (kleinster `attempt`), bei keinem **`n. e.`** mit Eintrag in T7.3. **Nicht** aus dem Dateinamen, **nicht** aus der Zahl der Records. Der bisherige Glob `<cfg>_*<injection_sha256>.json` traf den **ersten** Versuch; für **elf** K3-Injektionen (I05, I06, I07, I09, I11, I13, I16, I20, I21, I22, I23) trägt dieses Artefakt das Verdikt **INVALID**, Grund `transport_failure` (C11d §A6b). **Verletzt ist §7 wörtlich:** „stille Zählung invalider Läufe als ‚0 Findings‘ ist damit ausgeschlossen“ — genau das ist geschehen, **während T7 die Gültigkeit korrekt auswies**. **Z3 ist als kontrolliertes Experiment registriert** (`00_stand` §5, `methodik_begruendung` §6), und die Stufe toleriert diesen Defekt nicht. **RICHTUNG BENANNT, NICHT UMSCHRIEBEN: die Reparatur wird die K3-Zahlen voraussichtlich VERBESSERN.** Tragend sind vier Gründe, jeder für sich: die verletzte Regel war **vorregistriert** (§7, seit Rev. 33); der Defekt fiel durch eine **vor dem Befund beauftragte mechanische Auszählung** auf (C11d A6b); es ist eine **Artefaktauswahl, KEINE Metrikänderung**; **C11–C13 bleiben archiviert** und werden gegenübergestellt. Die in C13 gedruckte T1-Abweichung **„K3: Soll ja / Ist teilweise“** ist nach derzeitigem Stand ein **Artefakt der Dateiauswahl** (C11d §A6.1: das gelesene Artefakt von I23 trägt `calls_transport_failed: 3`, Exit 3, null Records) — **ob sie bestehen bleibt, zeigt der vierte Lauf; hier nicht vorweggenommen** · **Zusicherung R12, Exit 2:** der Lauf bricht ab, wenn ein Artefakt gelesen wird, dessen Laufmanifest ein Verdikt ≠ `VALID` trägt; **unabhängig vom Auswähler formuliert**, deshalb der Riegel gegen die Wiederholung. Ausgenommen und benannt: die Run-Logs `*.jsonl` für **T6** (Kosten über **alle** Invocationen) — **T6 bewegt sich nicht** · **(b) OVERLAP-TABELLE T10 NEU** — §8 verlangt für UF3 eine „Overlap-Analyse K1/K4/K5 vs. K2/K3“, die registrierte Ausgabe enthielt keine (C11d §B5). Registriert in `kapitel7_tabellenskelette.md` (Abschnitt T10, Druckreihenfolge Position 10, §0.3-Zuordnung, Anhangzeile A-39) und in der Auswertungsspezifikation (§8 Punkt 10). **Basis: die BEREITS GERECHNETEN Trefferzellen — keine neue Metrik, keine neue Schwelle, kein neuer Nenner.** `localized` und `strict` in **getrennten** Teiltabellen T10a/T10b · **K2 und K3 werden NICHT zu „dem LLM-Pfad“ vereinigt**, je Konfiguration eine eigene Zeilengruppe · die **Baselineseite ist eine Vereinigung** K1 ∪ K4 ∪ K5 und wird als solche **benannt** · vier Zustände je Injektion (**nur Baseline · nur die LLM-Konfiguration · beide · keiner**) · **MARKERDISZIPLIN:** eine Seite, die eine Injektion nach **T8** nicht ausdrücken kann, ist dort **nicht verfehlt** — eigene Klasse, **nie** in „nur die andere Seite“ umgedeutet (sonst würde Ausdrucksmächtigkeit zu Leistung, **B17**); `n. b.`, `n. e.` und T9 Fall 6/7 gehen **weder als Treffer noch als Verfehlung** ein · **Aggregatzeile je Gruppe mit ausgewiesenem Nenner, wie in T5** · nach Skelett §0.3 eine **gerechnete** Tabelle, **kein Aufschrieb** · **(c) DER ÜBERHOLTE T5-VERMERK (R14).** Die Ausgabe druckte an T5 weiter „LÜCKE, benannt und nicht gefüllt“, während Skelett, Spezifikation und Protokoll die Anforderung T5 (ii) seit **Rev. 42** als **gegenstandslos erledigt** führen (C11c §2); der Renderertext ist mit der Rev.-42-Begründung nachgezogen, **keine Zelle bewegt sich** · **Hash-Nachzug der Auswertungsspezifikation** in §0.1 und §1: ~~`fe991be6…092c20d1`~~ → **`39822edc…d2cd71c7`** · **AUSDRÜCKLICH: keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein Prompt, kein Schema** — die fünf Gegenstände der Sperre aus §0.1 Punkt 2 sind unangetastet; `strict`, `localized`, Precision, Recall, F1, Median, Spannweite, FP-Rate und die vier Marker stehen zeichengleich · **Die Instrumenten-Hashes werden NICHT unter dieser Nummer nachgezogen** — das ist nach §0.1 Punkt 5 eine eigene Revision (Präzedenz Rev. 36, 41, 43) | Ein vorregistrierter Ausschluss („stille Zählung invalider Läufe als ‚0 Findings‘ ist damit ausgeschlossen“, §7) war in der Auswertung nicht wirksam, obwohl T7 die Gültigkeit korrekt auswies; und eine von §8 UF3 ausdrücklich verlangte Analyse fehlte in der Ausgabe. Beides ist ein **Defekt der Auswertung**, kein Messergebnis — Defektklausel §0.1 Punkt 6. Belege: `c11d_bericht_befund08_grundlagen.md` §A6b (die elf Injektionen, ausgezählt), §A6.1 (I23: null Records, Exit 3), §B5 (die fehlende Overlap-Analyse), §B1 (Z3 als kontrolliertes Experiment), Protokoll §7 und §8 UF3 | **ja** — vollständige Neuauswertung über den **unveränderten** Kampagnenbestand, keine Neumessung; C11, C12 und C13 bleiben archiviert und werden dem vierten Lauf **gegenübergestellt**, nicht ersetzt |
| 45 | 28.08.2026 | Kopf auf **Rev. 45** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **§0.1 — HASH-NACHZUG DER AUSWERTUNGSINSTRUMENTE nach der Umsetzung von R11–R14, gesetzt NACH dem dritten Auswertungslauf und VOR dem vierten.** Ein reiner Bytestandsnachzug und deshalb nach §0.1 Punkt 5 **eine eigene Revision**, **nicht** unter Rev. 44 mitvollzogen: dort stünde der in `c5b_bericht_protokoll_freeze.md` §3 bezeugte Bytestand von Rev. 44 in keinem Dokument mehr (Präzedenz Rev. 36, und dieselbe Trennung wie Rev. 40/41 und Rev. 42/43) · **Ein Instrument geändert:** `tools/evaluate_campaign.py` ~~`eb206a6f…b520653`~~ → **`b66be750…9a93428`**; `tools/match_k4k5.py` und `tools/check_doc_invariants.py` **unverändert** · **Umgesetzt sind die vier in Rev. 44 registrierten Punkte:** **R11** Artefaktauswahl aus dem gehashten Laufmanifest (`postrun.verdict == VALID`, bei mehreren der früheste `attempt`; Pfad aus dem Manifestnamen, nicht aus einem Glob; die Injektions-SHA bleibt als **Gegenprobe** in Gebrauch) · **R12** Zusicherung **Exit 2** gegen das Lesen eines Artefakts ohne gültiges Laufmanifest, **unabhängig vom Auswähler formuliert** — sie fragt die gelesenen Dateien; ausgenommen und benannt die Run-Logs `*.jsonl`, die **T6** über alle Invocationen liest · **R13** **T10** gerendert: T10a/T10b, je Zeilengruppe K2 und K3 **getrennt**, Baselineseite als **benannte Vereinigung** K1 ∪ K4 ∪ K5, Aggregat mit ausgewiesenem Nenner, Buchungsprobe als Exit 2 · **R14** der T5-Vermerk druckt die Rev.-42-Begründung statt „LÜCKE, benannt und nicht gefüllt“ · **AUSDRÜCKLICH: KEINE Rechenregel, KEIN Filter, KEIN Nenner, KEINE Aggregationsstufe berührt** — `strict`, `localized`, Precision, Recall, F1, Median, Spannweite, FP-Rate und die vier Marker stehen zeichengleich · **Belegt, nicht behauptet:** `match_k4k5.py --selftest` **34/34**, Selbsttest B unverändert (K2 **49/52** und **461**, K3 **1/52** und **3**), der Fixture-Lauf reproduziert **jede** Metrikzelle von T1–T5, T8 und T9 **zeichengleich** gegen den Stand vor C14, die Zustandszuordnung ist gegen alle **16** Paare der handgerechneten Tabelle geprüft, jede Zusicherung negativ probiert und **R12 gegen den echten Bestand mit elf Verstössen, Exit 2** · **C11, C12 und C13 bleiben archiviert, gehasht und unverändert**; der vierte Lauf tritt daneben | Ein Bytewechsel an einem Auswertungsinstrument, der unter der Nummer einer bereits bezeugten Revision vollzogen wird, macht deren Bytestand unbezeugt (§0.1 Punkt 5, Präzedenz Rev. 36, 41 und 43). Belege: `c11d_bericht_befund08_grundlagen.md` §A6b und §B5, Protokoll §0.1 Zeile Auswertungsinstrumente und Punkt 6, Revisionshistorie Rev. 45, `tests/fixtures/harness/EXPECTED.md` §16 (**vor** der Umsetzung allein committet), `c14_bericht_vierter_lauf.md` §3 und §5 | **ja** — vollständige Neuauswertung über den **unveränderten** Kampagnenbestand, keine Neumessung; erwartet sind Änderungen ausschliesslich in den K3-Spalten von T1, T2, T4, T5 und T7.4 sowie die neue T10 |
| 46 | 31.08.2026 | Kopf auf **Rev. 46** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **§7 — DIE KÜRZUNGSREIHENFOLGE „ZUERST Z4 (TRANSFER-DEMONSTRATION), DANN ERST Z2" IST ALS ÜBERHOLT GESTRICHEN**, Alttext durchgestrichen sichtbar stehengelassen. Grund: der Gate ist ein binärer Kalendermechanismus zum Stichtag 31.08.2026 und liegt konstruktiv **vor** Z4s Slot (Arbeitsplan Rev. 1, Block 6: Z4 am 11.09.); am Stichtag ist Z4 noch nicht gelaufen, ein negativer Ausgang streicht unmittelbar Z2 — die Reihenfolge **konnte nie zur Anwendung kommen**. **Z4 wird eigenständig entschieden, nicht über den Gate.** Dazu aufgenommen: der **Ausgang des Gates selbst**, als Vermerk unter der Regel — geprüft und entschieden am Termin, **Kriterium erfüllt, Variante C bleibt, Z2 fällt nicht** | **Auftrag G1, Gate-Notiz vom 31.08.2026** (`docs/planung/gate_notiz_2026-08-31.md`). Die Reihenfolge war die seit dem 04.08.2026 in `00_stand_und_entscheidungen.md` §3 als **offen** geführte Inkonsistenz; ihre Auflösung war dort ausdrücklich der Gate-Notiz zugewiesen (Vermerk Rev. 11, 29.08.2026). Eine Regel, die konstruktiv nie greifen kann, als geltend stehenzulassen, macht das Protokoll an dieser Stelle unwahr | **nein** — **keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein Prompt und kein Schema ist berührt**; §7 ist die Entscheidungs- und Stop-Regel-Sektion, bewegt hat sich eine **Scope-Klausel**, keine Rechenvorschrift. Messstand §0.1, Matching-Regel §4, Metriken §5 und Ablauf §6 unberührt; die drei Instrumentenhashes stehen unverändert auf den Werten von Rev. 45 |
| 47 | 31.08.2026 | Kopf auf **Rev. 47** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **§0.1 — HASH-NACHZUG AN EINEM AUSWERTUNGSINSTRUMENT.** der SHA256 von `tools/check_doc_invariants.py` steht jetzt auf ~~`6cc16ef9…1e52b7018`~~ → **`c351a137…2b8707fdf`**; `tools/evaluate_campaign.py` und `tools/match_k4k5.py` stehen **zeichengleich**. Der Prüfer hat die **Invariante (F)** aufgenommen: SHA256 des Z1-Protokolls `docs/protokolle/z1_protokoll_extraktionsvergleich.md` gegen den in `z1_p_bericht_freeze.md` §3 als aktuell geführten Wert — dieselbe Bewegungsprüfung, die (A) für dieses Protokoll leistet, für das zweite vorregistrierte Protokoll der Arbeit. Die Leseroutine der §3-Tabelle ist um zwei Parameter erweitert und wird von (A) und (F) geteilt; **(A) liest dieselbe Tabelle mit demselben Ergebnis** | **Auftrag Z1-P, 31.08.2026** (`z1_p_bericht_freeze.md`). Das Z1-Protokoll ist an diesem Tag zur Vorregistrierung geschrieben und eingefroren worden; sein Bytestand kann — wie der dieses Protokolls — nicht im Dokument selbst bezeugt werden und steht deshalb in einem eigenen Bericht. Ohne maschinelle Prüfung driften die beiden Stellen auseinander; genau dieser Ausfall ist der Anlass, aus dem der Prüfer mit Rev. 36 überhaupt entstanden ist. **Eigene Revision und nicht unter Rev. 46 mitvollzogen** (§0.1 Punkt 5): läge der Nachzug dort, stünde der in `c5b_bericht_protokoll_freeze.md` §3 bezeugte Bytestand von Rev. 46 in keinem Dokument mehr — Präzedenz Rev. 41, Rev. 43, Rev. 45 | **nein** — **keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein Prompt und kein Schema ist berührt**; die Invarianten (A)–(E) stehen wörtlich unverändert und liefern zeichengleiche Ausgaben, der Prüfer ist ausschliesslich lesend und rechnet keine Kennzahl. Kein Artefakt unter `data/campaign/k*` und kein Messeingang unter `data/soll/` bewegt sich |


| 48 | 01.09.2026 | Kopf auf **Rev. 48** (Alttext gestrichen sichtbar; die **Freeze-Aussage bleibt Rev. 33, 27.08.2026**) · **§9 — T15 NEU: DIE AUSFÜHRUNGSGEOMETRIE DES INFERENZSERVERS** (`n_ctx` / `-c`, die daraus **abgeleitete Batchgrösse** `-b`/`-ub`, die **KV-Cache-Geometrie**) **ist ein Umgebungsparameter, der die Ausgabe bewegt und in keinem Laufrecord bezeugt ist.** T1 bis T14 stehen **unverändert**. Belegt aus zwei Diagnoseläufen ausserhalb dieses Messstands: dieselbe Maschine, dieselbe Ollama-Fassung **0.30.10**, derselbe Modell-Blob, **token-für-token derselbe Erstprompt** (4 095 IDs), `temperature=0` und `seed=0` — und **verschiedene Ausgabe**, 1 517 gegen 2 261 Zeichen; der eine Lauf gültig mit 0 Fehlern, der andere ungültig mit 14. Verändert war allein `-c 4096` gegen `-c 16384` samt `-b`/`-ub` 512 gegen 1024 und 224 gegen 896 MiB KV-Cache · **MIT DER ABGRENZUNG, die zum Eintrag gehört: die Vergleichbarkeit innerhalb dieser Kampagne ist UNBERÜHRT** — alle K2-Läufe auf demselben **gemessenen** Fenster `CONTEXT 4096` (§1 Nachtrag Rev. 26), das Nachlaufskript prüfte es **je Call**, die Prompts lagen mit Median **1 346** und Maximum **1 948** Token weit darunter, **kein Messergebnis, keine Metrik, keine Zelle der Erwartungsmatrix ist betroffen**. **Nicht mehr behauptbar** ist allein die **Reproduzierbarkeit auf einer anders konfigurierten Serverinstanz** · **Die Entscheidung aus Rev. 26, `num_ctx` NICHT zu setzen, war richtig und bleibt unangetastet**: ein Eingriff hätte den eingefrorenen Messpfad bewegt | **Ein Amendment, das BESCHREIBT und nicht festlegt** — nach §0.1 Punkt 2 auch nach Messbeginn zulässig: es hält fest, was beobachtet wurde und wie es zu lesen ist, und verschiebt nicht, wogegen gemessen wird. Der Anlass liegt **ausserhalb** dieses Protokolls (Aufträge Z1-S/Z1-S2 zum Extraktionsvergleich), die Folge für Z3 ist eine **Geltungsgrenze**, keine Korrektur. Belege: `z1_s_bericht_diagnoselauf.md` §6–§8; `data/z1_s_diagnose/` (51 Dateien, `sha256sum -c` Exit 0); `befunde_log.md` Befund 07.3, Nachtrag 01.09.2026; Protokoll §1 Nachtrag Rev. 26 (Fenster als gemessener Umgebungsparameter); `c14_eval_full.md` (K2-Zeile `1346 (767–1948)`); Z1-Protokoll §9 T-Z1-11 (Rev. 6), wo dieselbe Grösse für **künftige** Läufe als bezeugungspflichtig registriert ist | **nein** — **keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, kein Prompt und kein Schema ist berührt**; die drei Instrumentenhashes stehen zeichengleich auf den Werten von Rev. 47, kein Artefakt unter `data/campaign/k*` und kein Messeingang unter `data/soll/` bewegt sich, keine Zelle rechnet anders |

~~*Leer bei Vorregistrierung. Jede Änderung nach Messbeginn wird hier eingetragen.*~~
(überholt am 28.08.2026 durch C11b: **die Tabelle trägt ihre erste Zeile.**)

> **Zur Einordnung der Zeile 40, damit die Reihenfolge nicht verwischt.** Die Amendments
> **Rev. 34 bis Rev. 39** stehen oben in der Revisionshistorie-Tabelle, obwohl Rev. 35, 38
> und 39 zeitlich **nach** dem ersten Kampagnenlauf gesetzt sind: keines von ihnen berührte
> eine Metrikbildung, jedes war Ablage, Vorbedingung, Registrierung eines Bytestandes oder
> Quellenwechsel bei unbewegtem Wert. **Rev. 40 ist der erste Eintrag, der eine
> Rechenvorschrift bewegt**, und der erste, der einen **Re-Run** nach sich zieht — deshalb
> steht er hier und nicht oben. Der Re-Run ist eine **vollständige Neuauswertung** über den
> **unveränderten** Kampagnenbestand, **keine** Neumessung: die Kampagne selbst wird nicht
> wiederholt, kein Artefakt unter `data/campaign/k*` bewegt sich.

> **Sperre ab dem ersten Kampagnenlauf (Rev. 33, §0.1).** Einträge in dieser Tabelle dürfen
> **keine Metrikdefinition, kein Injektionsmanifest, keine Regeldatei, keinen Prompt und kein
> Schema ändern** — sie dürfen **nur beschreiben, nicht festlegen**. Einzige Ausnahme bleibt die
> Defektklausel aus §1: **höchstens ein** Amendment, mit **vollständigem Re-Run aller**
> Konfigurationen, kein selektives Nachmessen.
