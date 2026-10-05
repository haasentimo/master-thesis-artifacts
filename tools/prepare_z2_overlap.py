#!/usr/bin/env python3
"""Build the overlap matrix for Z2 protocol §7 point 5 (task S12).

WHAT THIS TOOL IS
-----------------
§7 point 5 asks for a secondary, descriptive figure: "n von 16
autorenformulierten Statements wurden sinngemäß vorgeschlagen". This tool
produces the SHEET on which that figure is later established: one section per
authored rule statement of the frozen `data/soll/architecture-rules.yaml`, a
lookup part with the sixteen assessed proposal classes (Z2-R), a MACHINE
PRE-FINDING per statement, and three EMPTY author fields.

TWO STAGES, AND WHY
-------------------
"Sinngemäss" is the same kind of judgement as the Z2-R criterion (category,
scope and core assertion agree). Z2-R was expressly NOT mechanised in S10 --
the merge was limited to character equality so that no tool would take an
substantive decision. Both figures are therefore treated alike: the tool does
the LOOKUP WORK (which proposals speak about the subject matter of a statement
at all) and lays its audit trail open; the DECISION on every one of the sixteen
rows belongs to the author.

The pre-finding is a PROPOSAL, not a determination. It lives in its own fields,
marked MASCHINELL, visibly separated from the three author fields, which stay
EMPTY. Nothing is pre-filled there, and the sum field stays empty as well: the
tool computes NO subtotal of its own pre-findings, because a subtotal would be
read as the result.

THE STANDARD, AND WHAT IS NOT USED
----------------------------------
A candidate is recorded when THE SAME SUBJECT MATTER IS FORBIDDEN OR REQUIRED
-- irrespective of wording, category label and scope granularity. There is NO
similarity measure, no ratio, no ranking and no ordering by proximity anywhere
in this tool: the pre-finding is a subject-matter check, not a text comparison.
The pre-findings are DATA CONSTANTS (`VORBEFUNDE`); the tool does not compute
them, it renders them and checks their shape.

Order is fixed and carries no information: the target statements appear in FILE
order (not grouped by category), the proposals in LABEL order `P-01` ... `P-17`,
and candidates and audit-trail entries in label order too.

WORDING IS EXTRACTED, NEVER RETYPED
-----------------------------------
§7 point 5, §7 point 3 and T-Z2-8 are cut out of the FROZEN protocol at runtime,
between the anchors in `SECTIONS`. The file is pinned by SHA256 (`PROTO_SHA`);
a mismatch aborts. `data/soll/architecture-rules.yaml` is pinned the same way
(`RULES_SHA`), and its category distribution is COUNTED from the file, not
copied from the protocol.

DETERMINISM
-----------
Standard library only; PyYAML is used when the system provides it, otherwise a
minimal reader for this one file takes over and the choice is reported. No
clock, no environment, no network. Run twice, the output is byte-identical.
`--check` re-runs the generation into a temporary directory and compares.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

PROTO_PATH = REPO / "docs/protokolle/z2_protokoll_regelableitung.md"
PROTO_SHA = "862fdc3b7cfb264482db155575437edb25b1b436f92b5444b2137f1e332d9dde"

RULES_PATH = REPO / "data/soll/architecture-rules.yaml"
RULES_SHA = "72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95"

OUT_DIR = REPO / "data/z2/bewertung"
MATRIX_NAME = "ueberlappmatrix.md"
SUMS_NAME = "SHA256SUMS"

TALLY_PATH = OUT_DIR / "auswertung.json"
KEY_PATH = OUT_DIR / "zuordnungsschluessel.json"

# Registered denominator of §7 point 5. A different count is an ABORT: the
# registered denominator would then be wrong.
EXPECTED_RULES = 16
# Registered class count of the assessment (S11): sixteen Z2-R classes out of
# seventeen labels.
EXPECTED_CLASSES = 16

# Execution day of task S12, written into the sheet as a constant so that the
# output does not depend on a clock.
RUN_DATE = "04.09.2026"

# Anchors of the verbatim cut-outs: (first line prefix, stop line prefix).
SECTIONS = {
    "p5": ("5. **Sekundär, klar gelabelt:**", "6. ~~**B1-vs-B2-Kontrast:**"),
    "p3": ("3. **Abdeckungsmatrix:**", "4. **Stabilität:**"),
    "tz28": ("| **T-Z2-8** |", "| **T-Z2-9** |"),
}

# Fence for the `statement` texts: four tildes, because proposal and rule texts
# carry backticks (precedent S10).
FENCE = "~~~~"

# The two verdict words of the machine pre-finding. Nothing else is admissible.
KANDIDAT = "Kandidat vorhanden"
KEIN_KANDIDAT = "kein Kandidat"

# --------------------------------------------------------------------------
# The machine pre-finding -- DATA, not a computation
# --------------------------------------------------------------------------
# One entry per authored rule statement, keyed by its `id`. The tool does not
# derive these; it renders them, and `check_vorbefunde` checks their shape
# against the classes actually read from `auswertung.json`.
#
# `kandidaten` and the labels of `pruefspur` name Z2-R CLASSES by the label
# form used in the lookup part ("P-01 + P-11" for the one non-trivial class).
# Both lists are RENDERED IN LABEL ORDER, whatever order they are written in
# here: the order in the sheet must not express proximity, and there is no
# ranking anywhere.
#
# Standard applied throughout: THE SAME SUBJECT MATTER IS FORBIDDEN OR REQUIRED
# -- irrespective of wording, category label and scope granularity. The wording
# stays in the register of a proposal ("spricht über denselben Sachverhalt",
# "Kandidat", "zu prüfen"), never in that of a determination.
VORBEFUNDE: dict[str, dict] = {
    "R-LAYER-1": {
        "befund": KANDIDAT,
        "kandidaten": ["P-07", "P-14"],
        "begruendung": (
            "`P-14` spricht über denselben Sachverhalt wie die Sprungklausel des "
            "Statements: „must not import repository, model, or adapter modules "
            "directly“ ist der Schichtsprung `api` → `repository`, den R-LAYER-1 "
            "verbietet. Der Vorschlag ist **enger** — er trifft nur die api-Schicht "
            "(drei `routes`-Module) und spricht den Rückruf aus einer unteren Schicht "
            "nicht aus. `P-07` beschränkt die Importe eines repository-Moduls auf die "
            "eigenen Models und `depot.core.ports`; liest man diese Erlaubnisliste "
            "abschliessend, ist der Rückruf `repository` → `services` mitverboten — "
            "als Nebenfolge und nur für eine Schicht. **Beides ist zu prüfen.**"
        ),
        "pruefspur": [
            ("P-01 + P-11", "verbietet den Services die Abhängigkeit von konkreten "
                            "Repositories, also gerade die Kante `services` → "
                            "`repository`, die R-LAYER-1 als Schritt in die "
                            "nächsttiefere Schicht erlaubt — gegenläufig"),
            ("P-02", "zieht eine Grenze zwischen den Kontexten, nicht zwischen den "
                     "Schichten eines Kontexts"),
            ("P-16", "betrifft die mappers-Pakete, die in der Schichtordnung des "
                     "Statements nicht vorkommen"),
            ("P-03", "regelt den Definitionsort einer Fehlerfunktion, keine "
                     "Schichtrichtung"),
            ("P-09", "desgleichen, Definitionsort statt Importrichtung"),
            ("P-10", "desgleichen"),
            ("P-04", "Importverbot gegen `logging`, keine Aussage über Schichten"),
            ("P-05", "Stil- und Dokumentationsaussage ohne Importrichtung"),
            ("P-06", "Duplikationsverbot ohne Importrichtung"),
            ("P-12", "Organisationsaussage ohne Importrichtung"),
            ("P-15", "Fehlerbehandlungsaussage ohne Importrichtung"),
            ("P-08", "Definitionsort der Protokolle"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-17", "Duplikationsverbot für zwei benannte Funktionen"),
        ],
    },
    "R-PROTECT-1": {
        "befund": KANDIDAT,
        "kandidaten": ["P-01 + P-11", "P-14"],
        "begruendung": (
            "Beide sprechen über denselben Sachverhalt — das Verbot, aus einer höheren "
            "Schicht heraus konkrete Adaptermodule zu importieren: `P-01 + P-11` für "
            "die drei Servicepakete („must not directly instantiate or depend on "
            "concrete adapter … classes“), `P-14` für die api-Routen. Beide fassen "
            "**breiter**, weil sie den Adapterzugriff insgesamt verbieten, während "
            "R-PROTECT-1 die Fassade `depot.core.adapters` ausdrücklich **erlaubt** und "
            "nur `depot.core.adapters.internal` sperrt; die Fassaden-Ausnahme steht in "
            "keinem der beiden. **Zu prüfen ist**, ob ein breiteres Verbot als "
            "Entsprechung zu einem Fassadenverbot gelten soll."
        ),
        "pruefspur": [
            ("P-02", "Kontextgrenze zwischen `orders` und `billing`, keine "
                     "Fassadengrenze"),
            ("P-07", "beschränkt die repository-Schicht auf eigene Models und Ports, "
                     "nennt die Adapter nicht"),
            ("P-08", "regelt, wo Protokolle definiert werden, nicht wer Adapter "
                     "importieren darf"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-16", "Importverbot für mappers, aber gegen `depot.core.errors`, nicht "
                     "gegen die Adapter-Internals"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
            ("P-17", "Duplikationsverbot für zwei benannte Funktionen"),
            ("P-04", "Importverbot gegen `logging`, ein anderes Modul"),
            ("P-05", "Stil und Dokumentation"),
            ("P-06", "Duplikation"),
            ("P-12", "Organisation"),
            ("P-15", "Fehlerbehandlung"),
        ],
    },
    "R-INDEP-1": {
        "befund": KANDIDAT,
        "kandidaten": ["P-02", "P-07"],
        "begruendung": (
            "`P-02` spricht über dieselbe Kontextgrenze zwischen `orders` und "
            "`billing`, fasst sie aber **enger**: nur die services-Pakete, während "
            "R-INDEP-1 alle Schichten beider Kontexte erfasst (`api`, `services`, "
            "`repository`, `models`, `mappers`). `P-07` verbietet einem "
            "repository-Modul Models fremder Pakete und trifft damit die Kante "
            "`billing.repository` → `orders.models` mit — **nur teilweise**, auf der "
            "models-Achse und ohne die Kontextgrenze als solche zu benennen."
        ),
        "pruefspur": [
            ("P-01 + P-11", "bindet die Services an die Ports, zieht keine Grenze "
                            "zwischen zwei Kontexten"),
            ("P-14", "Schichtgrenze innerhalb eines Kontexts"),
            ("P-16", "Importverbot für mappers gegen `depot.core.errors`, keine "
                     "Kontextgrenze"),
            ("P-04", "spricht über die billing-Komponenten, aber über `logging`"),
            ("P-05", "desgleichen, über Stil und Dokumentation"),
            ("P-06", "desgleichen, über Duplikation"),
            ("P-12", "desgleichen, über Organisation"),
            ("P-15", "desgleichen, über Fehlerbehandlung"),
            ("P-08", "Definitionsort der Protokolle im Kern"),
            ("P-13", "Definitionsort der Fehlerklassen im Kern"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
            ("P-17", "Duplikationsverbot für zwei benannte Funktionen"),
        ],
    },
    "R-CORE-1": {
        "befund": KEIN_KANDIDAT,
        "kandidaten": [],
        "begruendung": (
            "Der Sachverhalt des Statements ist die **Abhängigkeitsrichtung DES "
            "KERNS**: `core`, `core_adapters` und `core_adapters_internal` dürfen "
            "keinen Businesskontext importieren, und `core` trägt überhaupt keine "
            "ausgehende Kante. Dieser Sachverhalt kommt in **keinem** der 16 "
            "Vorschläge vor. Die Vorschläge, die den Kern nennen, sprechen sämtlich "
            "über Kanten, die **auf ihn zulaufen**, oder über den **Ort**, an dem "
            "etwas im Kern zu definieren ist — nie über das, was der Kern seinerseits "
            "importieren darf."
        ),
        "pruefspur": [
            ("P-01 + P-11", "richtet die Services auf `depot.core.ports` aus, also "
                            "eine eingehende Kante — die Gegenrichtung"),
            ("P-07", "erlaubt der repository-Schicht `depot.core.ports`, wieder eine "
                     "eingehende Kante"),
            ("P-08", "verlangt Protokolle in `depot.core.ports`: ein Definitionsort im "
                     "Kern, keine Aussage über dessen Abhängigkeiten"),
            ("P-13", "dasselbe für Fehlerklassen in `depot.core.errors`"),
            ("P-09", "verlangt die Fehler-Mappingfunktionen in `depot.core.errors` — "
                     "Definitionsort"),
            ("P-17", "verlangt `status_for` und `error_body` in einem gemeinsamen "
                     "Modul — Definitionsort"),
            ("P-16", "verbietet den mappers den Import von `depot.core.errors`, erneut "
                     "eine eingehende Kante"),
            ("P-03", "verbietet den schemas-Modulen eine eigene `error_body` — "
                     "eingehende Kante"),
            ("P-10", "desgleichen für `status_for`"),
            ("P-02", "Kontextgrenze zwischen zwei Businesskontexten"),
            ("P-14", "Schichtgrenze innerhalb eines Kontexts"),
            ("P-04", "Importverbot gegen `logging` in den billing-Komponenten"),
            ("P-05", "Stil und Dokumentation"),
            ("P-06", "Duplikation"),
            ("P-12", "Organisation"),
            ("P-15", "Fehlerbehandlung"),
        ],
    },
    "R-CYCLE-1": {
        "befund": KEIN_KANDIDAT,
        "kandidaten": [],
        "begruendung": (
            "Der Sachverhalt des Statements ist der **Importzyklus zwischen den "
            "Geschwisterpaketen** `<context>.api` und `<context>.mappers` und das "
            "Verbot der Rückkante `mappers` → `api`. Kein Vorschlag verbietet diese "
            "Rückkante, und **keiner der 16 verwendet den Zyklusbegriff überhaupt**."
        ),
        "pruefspur": [
            ("P-14", "nennt die mappers als für die api-Routen zulässige Abhängigkeit, "
                     "spricht also über die von R-CYCLE-1 **erlaubte** Richtung, nicht "
                     "über die verbotene Rückkante"),
            ("P-16", "betrifft die mappers, verbietet ihnen aber den Import von "
                     "`depot.core.errors`, nicht den der api"),
            ("P-01 + P-11", "Kanten zwischen Services und Konkreta, kein "
                            "Geschwisterpaar eines Kontexts"),
            ("P-02", "Kanten zwischen zwei Kontexten"),
            ("P-07", "Kanten der repository-Schicht"),
            ("P-03", "Definitionsort von `error_body` in den schemas-Modulen"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for` in den routes-Modulen"),
            ("P-17", "Duplikationsverbot für zwei benannte Funktionen"),
            ("P-08", "Definitionsort der Protokolle"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-04", "Importverbot gegen `logging`"),
            ("P-05", "Stil und Dokumentation"),
            ("P-06", "Duplikation"),
            ("P-12", "Organisation"),
            ("P-15", "Fehlerbehandlung"),
        ],
    },
    "R-CYCLE-2": {
        "befund": KEIN_KANDIDAT,
        "kandidaten": [],
        "begruendung": (
            "Der Sachverhalt des Statements ist die **Rückkante eines Unterpakets auf "
            "sein Elternpaket** — `depot.orders.services.pricing` → "
            "`depot.orders.services`. Kein Vorschlag nennt dieses Unterpaket, und "
            "**keiner spricht über das Verhältnis eines Pakets zu seinem eigenen "
            "Elternpaket**; die Vorschläge behandeln die services-Pakete durchweg als "
            "ungeteilte Einheiten."
        ),
        "pruefspur": [
            ("P-01 + P-11", "spricht über die drei services-Pakete als Ganzes, ohne "
                            "deren innere Paketstruktur"),
            ("P-02", "desgleichen, und zieht die Grenze zwischen zwei Kontexten"),
            ("P-14", "Schichtgrenze zwischen api und den darunterliegenden Schichten"),
            ("P-12", "verlangt logische Modul- und Paketorganisation, aber ohne "
                     "Richtung und ohne Zyklusbegriff, und mit Scope nur auf den "
                     "billing-Komponenten"),
            ("P-07", "repository-Pakete"),
            ("P-16", "mappers-Pakete"),
            ("P-08", "Definitionsort der Protokolle"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
            ("P-17", "Duplikationsverbot für zwei benannte Funktionen"),
            ("P-04", "Importverbot gegen `logging`"),
            ("P-05", "Stil und Dokumentation"),
            ("P-06", "Duplikation"),
            ("P-15", "Fehlerbehandlung"),
        ],
    },
    "R-PORT-1": {
        "befund": KANDIDAT,
        "kandidaten": ["P-01 + P-11"],
        "begruendung": (
            "Der Vorschlag bindet die Serviceklassen der drei Kontexte an die "
            "Schnittstellen aus `depot.core.ports` und verbietet ihnen den Griff auf "
            "Konkreta — **derselbe Sachverhalt**, den R-PORT-1 für "
            "`depot.identity.services.token_service` und den Port `TokenSigner` "
            "fordert. Der Vorschlag fasst **breiter** (alle drei Servicepakete, alle "
            "Ports) und formuliert ein **Abhängigkeitsverbot**, wo das Statement die "
            "**Anwesenheit** des Porttyps in einer benannten öffentlichen Signatur "
            "verlangt; die Signaturebene fehlt ihm. **Zu prüfen.**"
        ),
        "pruefspur": [
            ("P-08", "verlangt, dass Protokolle in `depot.core.ports` definiert "
                     "werden, sagt aber nichts darüber, welcher Service welchen Port "
                     "zu führen hat"),
            ("P-14", "betrifft die Konstruktorabhängigkeiten der api-Routen, nicht die "
                     "Signatur eines Services"),
            ("P-02", "Kontextgrenze ohne Portbezug"),
            ("P-07", "Repositorygrenze ohne Portbezug — nennt `depot.core.ports` nur "
                     "als erlaubte Importquelle"),
            ("P-17", "nennt Signaturen, aber die zweier Fehler-Hilfsfunktionen"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-16", "Importverbot für mappers"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
            ("P-04", "Importverbot gegen `logging`, Scope billing"),
            ("P-05", "Stil und Dokumentation, Scope billing"),
            ("P-06", "Duplikation, Scope billing"),
            ("P-12", "Organisation, Scope billing"),
            ("P-15", "Fehlerbehandlung, Scope billing"),
        ],
    },
    "R-PORT-2": {
        "befund": KANDIDAT,
        "kandidaten": ["P-01 + P-11"],
        "begruendung": (
            "Wie bei R-PORT-1: der Vorschlag bindet die Serviceklassen — darunter die "
            "des Pakets `depot.orders.services` — an die Schnittstellen aus "
            "`depot.core.ports`, und das ist **derselbe Sachverhalt**, den R-PORT-2 "
            "für `depot.orders.services.catalog_service` und den Port `RateProvider` "
            "fordert. **Breiter** in der Reichweite (alle Servicepakete, alle Ports), "
            "und als Abhängigkeitsverbot statt als Anwesenheitsforderung in der "
            "Signatur `CatalogService.quote_cents`. **Zu prüfen.**"
        ),
        "pruefspur": [
            ("P-02", "nennt `depot.orders.services` im Scope, spricht aber über die "
                     "Grenze zum billing-Kontext, nicht über einen Port"),
            ("P-08", "Definitionsort der Protokolle, keine Zuweisung Port ↔ Service"),
            ("P-14", "Konstruktorabhängigkeiten der api-Routen"),
            ("P-07", "nennt `depot.core.ports` nur als erlaubte Importquelle der "
                     "repository-Schicht"),
            ("P-17", "nennt Signaturen, aber die zweier Fehler-Hilfsfunktionen"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-16", "Importverbot für mappers"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
            ("P-04", "Importverbot gegen `logging`, Scope billing"),
            ("P-05", "Stil und Dokumentation, Scope billing"),
            ("P-06", "Duplikation, Scope billing"),
            ("P-12", "Organisation, Scope billing"),
            ("P-15", "Fehlerbehandlung, Scope billing"),
        ],
    },
    "R-PORT-3": {
        "befund": KANDIDAT,
        "kandidaten": ["P-01 + P-11"],
        "begruendung": (
            "Wie bei R-PORT-1 und R-PORT-2: die Bindung der Serviceklassen an "
            "`depot.core.ports` ist **derselbe Sachverhalt**, den R-PORT-3 für "
            "`depot.orders.services.refund_service` und den Port `PaymentGateway` "
            "fordert; `depot.orders.services` liegt im Scope des Vorschlags. "
            "**Breiter** in der Reichweite und ohne die Signaturebene, die das "
            "Statement mit `RefundService.refund` benennt. **Zu prüfen.**"
        ),
        "pruefspur": [
            ("P-02", "nennt `depot.orders.services` im Scope, spricht aber über die "
                     "Kontextgrenze, nicht über einen Port"),
            ("P-08", "Definitionsort der Protokolle"),
            ("P-14", "Konstruktorabhängigkeiten der api-Routen"),
            ("P-07", "`depot.core.ports` nur als erlaubte Importquelle der "
                     "repository-Schicht"),
            ("P-17", "Signaturen zweier Fehler-Hilfsfunktionen"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-16", "Importverbot für mappers"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
            ("P-04", "Importverbot gegen `logging`, Scope billing"),
            ("P-05", "Stil und Dokumentation, Scope billing"),
            ("P-06", "Duplikation, Scope billing"),
            ("P-12", "Organisation, Scope billing"),
            ("P-15", "Fehlerbehandlung, Scope billing"),
        ],
    },
    "R-PORT-4": {
        "befund": KANDIDAT,
        "kandidaten": ["P-01 + P-11"],
        "begruendung": (
            "Wie bei den drei übrigen Portregeln: die Bindung der Serviceklassen an "
            "`depot.core.ports` ist **derselbe Sachverhalt**, den R-PORT-4 für "
            "`depot.billing.services.ledger_service` und den Port `Clock` fordert; "
            "`depot.billing.services` liegt im Scope des Vorschlags. **Breiter** in "
            "der Reichweite, ohne die Signaturebene `LedgerService.post_invoice` und "
            "ohne die Ausnahme, die das Statement für `post_settlement` ausdrücklich "
            "macht. **Zu prüfen.**"
        ),
        "pruefspur": [
            ("P-02", "nennt `depot.billing.services` im Scope, spricht aber über die "
                     "Kontextgrenze, nicht über einen Port"),
            ("P-04", "Scope sind die billing-Komponenten, der Sachverhalt ist aber der "
                     "Import von `logging`, nicht die Portbindung"),
            ("P-05", "Scope billing, Sachverhalt Stil und Dokumentation"),
            ("P-06", "Scope billing, Sachverhalt Duplikation"),
            ("P-12", "Scope billing, Sachverhalt Organisation"),
            ("P-15", "Scope billing, Sachverhalt Fehlerbehandlung"),
            ("P-08", "Definitionsort der Protokolle"),
            ("P-14", "Konstruktorabhängigkeiten der api-Routen"),
            ("P-07", "`depot.core.ports` nur als erlaubte Importquelle"),
            ("P-17", "Signaturen zweier Fehler-Hilfsfunktionen"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-16", "Importverbot für mappers"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
        ],
    },
    "R-FRAMEWORK-1": {
        "befund": KEIN_KANDIDAT,
        "kandidaten": [],
        "begruendung": (
            "Der Sachverhalt des Statements ist der **Persistenztyp aus "
            "`sqlalchemy.orm` in einer öffentlichen Signatur der models-Schicht** — "
            "samt der Unterscheidung, die das Statement trägt: der **Import ist "
            "erlaubt**, der **Typ in der Signatur nicht**. Weder `sqlalchemy` noch ein "
            "Persistenzframework noch die Signaturen der models-Schicht kommen in "
            "**einem** der 16 Vorschläge vor."
        ),
        "pruefspur": [
            ("P-04", "verbietet den direkten Import einer Fremdbibliothek "
                     "(`logging`) — dieselbe Bauart, aber ein anderes Modul, und ein "
                     "Importverbot, das die Signaturebene gerade nicht trifft"),
            ("P-07", "spricht über Importe **von** Models durch die repository-Schicht, "
                     "nicht über Typen **in** deren Signaturen"),
            ("P-17", "nennt Signaturen, aber die von `status_for` und `error_body`"),
            ("P-08", "Definitionsort der Protokolle"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-05", "Stil und Dokumentation der billing-Komponenten, ohne Typaussage"),
            ("P-12", "Organisation der billing-Komponenten, ohne Typaussage"),
            ("P-06", "Duplikation"),
            ("P-15", "Fehlerbehandlung"),
            ("P-01 + P-11", "Portbindung der Services, nicht die models-Schicht"),
            ("P-02", "Kontextgrenze"),
            ("P-14", "Schichtgrenze der api-Routen"),
            ("P-16", "Importverbot für mappers"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
        ],
    },
    "R-PLACE-1": {
        "befund": KEIN_KANDIDAT,
        "kandidaten": [],
        "begruendung": (
            "Der Sachverhalt des Statements ist die **Ortsimplikation eines "
            "Modulnamens**: ein Modul auf `_repo`, `_query` oder `_index` gehört ins "
            "repository-Paket seines Kontexts, eines auf `_models` ins models-Paket. "
            "**Kein** Vorschlag leitet aus einem Modulnamen ab, in welchem Paket das "
            "Modul zu liegen hat, und die vier Suffixe kommen in keinem der 16 vor."
        ),
        "pruefspur": [
            ("P-03", "spricht über einen Namen, aber über den **Funktions**namen "
                     "`error_body` und dessen Definitionsort, nicht über Modulnamen "
                     "und deren Paket"),
            ("P-10", "desgleichen für `status_for`"),
            ("P-12", "verlangt logische Modul- und Paketorganisation, benennt aber kein "
                     "Namensmerkmal, aus dem sich ein Ort ergäbe, und liegt mit seinem "
                     "Scope nur auf den billing-Komponenten"),
            ("P-07", "betrifft die repository-Pakete, aber deren Importe, nicht die "
                     "Platzierung von Modulen nach ihrem Namen"),
            ("P-17", "Duplikationsverbot für zwei benannte Funktionen"),
            ("P-08", "Definitionsort der Protokolle, an einem Paket festgemacht, nicht "
                     "an einem Namensmerkmal des Moduls"),
            ("P-13", "dasselbe für Fehlerklassen"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-01 + P-11", "Portbindung der Services"),
            ("P-02", "Kontextgrenze"),
            ("P-14", "Schichtgrenze der api-Routen"),
            ("P-16", "Importverbot für mappers"),
            ("P-04", "Importverbot gegen `logging`"),
            ("P-05", "Stil und Dokumentation"),
            ("P-06", "Duplikation"),
            ("P-15", "Fehlerbehandlung"),
        ],
    },
    "R-SIG-1": {
        "befund": KEIN_KANDIDAT,
        "kandidaten": [],
        "begruendung": (
            "Der Sachverhalt des Statements ist die **zeichengenaue Vertragstreue "
            "einer Portimplementierung**: `SessionRepository.touch` muss die "
            "Zielsignatur des Ports `depot.core.ports.SessionStore` exakt tragen, "
            "Parameternamen und Rückgabetyp eingeschlossen. **Kein** Vorschlag "
            "verlangt, dass eine Implementierung eine vorgegebene Zielsignatur "
            "einhält; weder das Symbol noch der Port kommt in einem der 16 vor."
        ),
        "pruefspur": [
            ("P-17", "führt Signaturen mit, aber als Duplikationsverbot für "
                     "`status_for` und `error_body`, nicht als Vertragstreue gegenüber "
                     "einem Port"),
            ("P-08", "regelt, **wo** Protokolle definiert werden; über die Signatur "
                     "ihrer Implementierungen sagt es nichts"),
            ("P-01 + P-11", "verlangt die Bindung an Ports, nicht die Form der "
                            "implementierenden Methode"),
            ("P-07", "Importgrenze der repository-Schicht, keine Signaturaussage"),
            ("P-14", "Importgrenze der api-Schicht"),
            ("P-02", "Kontextgrenze"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-16", "Importverbot für mappers"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
            ("P-04", "Importverbot gegen `logging`"),
            ("P-05", "Stil und Dokumentation"),
            ("P-06", "Duplikation"),
            ("P-12", "Organisation"),
            ("P-15", "Fehlerbehandlung"),
        ],
    },
    "R-SIG-2": {
        "befund": KEIN_KANDIDAT,
        "kandidaten": [],
        "begruendung": (
            "Wie bei R-SIG-1: der Sachverhalt ist die zeichengenaue Zielsignatur von "
            "`OrderQuery.percent_for` gegenüber dem Port "
            "`depot.core.ports.DiscountCatalog`. **Kein** Vorschlag der 16 fordert "
            "Signaturtreue einer Portimplementierung, und weder das Symbol noch der "
            "Port wird genannt."
        ),
        "pruefspur": [
            ("P-17", "nennt zwei Signaturen, aber als Duplikationsverbot für "
                     "Fehler-Hilfsfunktionen"),
            ("P-08", "Definitionsort der Protokolle, nicht die Form ihrer "
                     "Implementierungen"),
            ("P-07", "spricht über `depot.orders.repository`, aber über dessen "
                     "Importe, nicht über eine Methodensignatur"),
            ("P-01 + P-11", "Portbindung der Services, nicht der repository-Schicht"),
            ("P-14", "Importgrenze der api-Schicht"),
            ("P-02", "Kontextgrenze"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-16", "Importverbot für mappers"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
            ("P-04", "Importverbot gegen `logging`"),
            ("P-05", "Stil und Dokumentation"),
            ("P-06", "Duplikation"),
            ("P-12", "Organisation"),
            ("P-15", "Fehlerbehandlung"),
        ],
    },
    "R-SIG-3": {
        "befund": KEIN_KANDIDAT,
        "kandidaten": [],
        "begruendung": (
            "Wie bei R-SIG-1 und R-SIG-2: der Sachverhalt ist die zeichengenaue "
            "Zielsignatur von `InvoiceQuery.settled_cents` gegenüber dem Port "
            "`depot.core.ports.PaymentLedger`. **Kein** Vorschlag der 16 fordert "
            "Signaturtreue einer Portimplementierung."
        ),
        "pruefspur": [
            ("P-17", "nennt zwei Signaturen, aber als Duplikationsverbot"),
            ("P-08", "Definitionsort der Protokolle"),
            ("P-07", "spricht über `depot.billing.repository`, aber über dessen "
                     "Importe, nicht über eine Methodensignatur"),
            ("P-01 + P-11", "Portbindung der Services"),
            ("P-14", "Importgrenze der api-Schicht"),
            ("P-02", "Kontextgrenze"),
            ("P-04", "Scope billing, aber Importverbot gegen `logging`"),
            ("P-05", "Scope billing, aber Stil und Dokumentation"),
            ("P-06", "Scope billing, aber Duplikation"),
            ("P-12", "Scope billing, aber Organisation"),
            ("P-15", "Scope billing, aber Fehlerbehandlung"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-16", "Importverbot für mappers"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
        ],
    },
    "R-SIG-4": {
        "befund": KEIN_KANDIDAT,
        "kandidaten": [],
        "begruendung": (
            "Der Sachverhalt des Statements ist die zeichengenaue Zielsignatur der "
            "öffentlichen Funktion `to_payload` in "
            "`depot.orders.mappers.order_line_mapper` — hier ohne Port, weil das "
            "Statement selbst der ganze Vertrag ist. **Kein** Vorschlag der 16 spricht "
            "über die Signatur einer Mapperfunktion."
        ),
        "pruefspur": [
            ("P-16", "spricht über die mappers-Pakete, aber über deren Fehlerimporte, "
                     "nicht über die Signatur einer Mapperfunktion"),
            ("P-14", "nennt die mappers als zulässige Abhängigkeit der api-Routen, "
                     "ohne Aussage über deren Schnittstelle"),
            ("P-17", "nennt zwei Signaturen, aber die von `status_for` und "
                     "`error_body`"),
            ("P-08", "Definitionsort der Protokolle; das Statement nennt ausdrücklich "
                     "keines"),
            ("P-07", "Importgrenze der repository-Schicht"),
            ("P-01 + P-11", "Portbindung der Services"),
            ("P-02", "Kontextgrenze"),
            ("P-13", "Definitionsort der Fehlerklassen"),
            ("P-03", "Definitionsort von `error_body`"),
            ("P-09", "Definitionsort der Fehler-Mappingfunktionen"),
            ("P-10", "Definitionsort von `status_for`"),
            ("P-04", "Importverbot gegen `logging`"),
            ("P-05", "Stil und Dokumentation"),
            ("P-06", "Duplikation"),
            ("P-12", "Organisation"),
            ("P-15", "Fehlerbehandlung"),
        ],
    },
}


def die(msg: str) -> None:
    print(f"ABBRUCH: {msg}", file=sys.stderr)
    raise SystemExit(1)


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# --------------------------------------------------------------------------
# Reading the authored rule statements
# --------------------------------------------------------------------------

def load_rules_pyyaml(text: str):
    import yaml  # noqa: PLC0415 -- optional, probed by the caller
    return yaml.safe_load(text)["rules"]


def load_rules_minimal(text: str):
    """Fallback reader for exactly this file: a `rules:` list of mappings with
    scalar fields, a `scope.components` sequence, a folded `statement: >-` block
    and an optional `predicate` with `type` and `allowed_importers`."""
    rules: list[dict] = []
    cur: dict | None = None
    stack: list[str] = []          # nesting path below the rule, e.g. ["scope"]
    folded_key: tuple | None = None
    folded_indent = 0
    folded: list[str] = []

    def flush_folded() -> None:
        nonlocal folded_key, folded
        if folded_key is None:
            return
        # `>-`: lines joined by a single space, trailing newlines stripped.
        target, key = folded_key
        target[key] = " ".join(folded).strip()
        folded_key, folded = None, []

    in_rules = False
    for raw in text.splitlines():
        if not in_rules:
            if raw.rstrip() == "rules:":
                in_rules = True
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw.strip()

        if folded_key is not None:
            if stripped and indent >= folded_indent and not stripped.startswith("#"):
                folded.append(stripped)
                continue
            if not stripped:
                continue
            flush_folded()

        if not stripped or stripped.startswith("#"):
            continue

        if stripped.startswith("- id:"):
            cur = {"id": stripped[len("- id:"):].strip()}
            rules.append(cur)
            stack = []
            continue
        if cur is None:
            continue

        if stripped.startswith("- "):
            value = stripped[2:].strip()
            if stack == ["scope", "components"]:
                cur["scope"]["components"].append(value)
            elif stack == ["predicate", "allowed_importers"]:
                cur["predicate"]["allowed_importers"].append(value)
            else:
                die(f"minimaler Leser: unerwarteter Listeneintrag {stripped!r}")
            continue

        if ":" not in stripped:
            die(f"minimaler Leser: unerwartete Zeile {stripped!r}")
        key, _, value = stripped.partition(":")
        key, value = key.strip(), value.strip()

        # Depth 4 = a rule field, 6 = inside scope/predicate, 8 = a sequence key.
        if indent <= 4:
            stack = []
        elif indent <= 6:
            stack = stack[:1]

        if value == ">-":
            folded_key = (cur if not stack else _descend(cur, stack), key)
            folded_indent = indent + 2
            folded = []
            continue
        if value == "":
            target = cur if not stack else _descend(cur, stack)
            target[key] = [] if key in ("components", "allowed_importers") else {}
            stack = stack + [key]
            continue
        target = cur if not stack else _descend(cur, stack)
        target[key] = value

    flush_folded()
    return rules


def _descend(rule: dict, stack: list[str]):
    node = rule
    for part in stack:
        node = node[part]
    return node


def load_rules() -> tuple[list[dict], str]:
    text = RULES_PATH.read_text(encoding="utf-8")
    try:
        import yaml  # noqa: F401
    except ImportError:
        return load_rules_minimal(text), "minimaler eigener Leser (PyYAML nicht vorhanden)"
    return load_rules_pyyaml(text), "PyYAML"


# --------------------------------------------------------------------------
# Reading the assessed proposals
# --------------------------------------------------------------------------

def load_proposal_texts() -> dict[str, dict]:
    """`P-xx` -> the proposal fields, character-identical from `raw_response.json`.

    The label's origin is taken from the assignment key; the fields are read
    back out of the archived raw artefact, not out of the review sheet, so the
    text passes through no markdown round-trip.
    """
    key = json.loads(KEY_PATH.read_text(encoding="utf-8"))
    cache: dict[tuple[str, str], list] = {}
    out: dict[str, dict] = {}
    for entry in key["eintraege"]:
        first = entry["herkunft"][0]
        cell, slot = first["bedingung"], first["slot"]
        if (cell, slot) not in cache:
            raw_path = REPO / "data/z2" / cell / slot / "raw_response.json"
            raw = json.loads(raw_path.read_text(encoding="utf-8"))
            cache[(cell, slot)] = json.loads(
                raw["choices"][0]["message"]["content"])["rules"]
        rule = cache[(cell, slot)][first["position"]]
        if rule["id"] != first["id"]:
            die(f"{entry['etikett']}: id {rule['id']!r} != Schlüssel {first['id']!r}")
        out[entry["etikett"]] = {
            "category": rule["category"],
            "severity": rule["severity"],
            "components": list(rule["scope"]["components"]),
            "statement": rule["statement"],
            "herkunft": entry["herkunft"],
        }
    return out


def load_classes() -> list[dict]:
    tally = json.loads(TALLY_PATH.read_text(encoding="utf-8"))
    block = tally["z2r_klassen"]
    classes = block["klassen"]
    if len(classes) != EXPECTED_CLASSES:
        die(f"{len(classes)} Z2-R-Klassen statt {EXPECTED_CLASSES}")
    # Label order `P-01` ... `P-17`: a class is placed at its smallest label.
    return sorted(classes, key=lambda c: sorted(c["mitglieder"])[0])


# --------------------------------------------------------------------------
# Verbatim cut-outs from the frozen protocol
# --------------------------------------------------------------------------

def cut(name: str) -> str:
    lines = PROTO_PATH.read_text(encoding="utf-8").splitlines()
    start_pat, stop_pat = SECTIONS[name]
    starts = [i for i, line in enumerate(lines) if line.startswith(start_pat)]
    if len(starts) != 1:
        die(f"Anker {start_pat!r}: {len(starts)} Treffer, genau 1 erwartet")
    stops = [i for i in range(starts[0] + 1, len(lines))
             if lines[i].startswith(stop_pat)]
    if not stops:
        die(f"Endanker {stop_pat!r} nach {start_pat!r} nicht gefunden")
    return "\n".join(lines[starts[0]:stops[0]]).rstrip()


# --------------------------------------------------------------------------
# Shape check of the pre-finding constants
# --------------------------------------------------------------------------

def class_label(cls: dict) -> str:
    """Plain-text label of a Z2-R class, e.g. "P-01 + P-11"."""
    return " + ".join(sorted(cls["mitglieder"]))


def check_vorbefunde(rules: list[dict], classes: list[dict]) -> None:
    """Abort unless every pre-finding is complete and well formed.

    The tool renders the pre-findings; it does not compute them. This is what
    keeps the constants honest: every rule carries exactly one entry, every
    label names a class that was actually read from `auswertung.json`, no label
    is both candidate and discarded, and NO ROW IS WITHOUT AN AUDIT TRAIL --
    an empty trail would make the row unusable (task S12, step 3(d)).
    """
    labels = {class_label(c) for c in classes}

    ids = [r["id"] for r in rules]
    missing = [i for i in ids if i not in VORBEFUNDE]
    if missing:
        die(f"ohne Vorbefund: {', '.join(missing)}")
    extra = [k for k in VORBEFUNDE if k not in ids]
    if extra:
        die(f"Vorbefund ohne Soll-Statement: {', '.join(sorted(extra))}")

    for rid in ids:
        v = VORBEFUNDE[rid]
        if v["befund"] not in (KANDIDAT, KEIN_KANDIDAT):
            die(f"{rid}: Vorbefund {v['befund']!r} ist keines der zwei Verdikte")

        cands = v["kandidaten"]
        if v["befund"] == KANDIDAT and not cands:
            die(f"{rid}: „{KANDIDAT}“ ohne Etikett")
        if v["befund"] == KEIN_KANDIDAT and cands:
            die(f"{rid}: „{KEIN_KANDIDAT}“, aber Etiketten genannt")

        trail = [lab for lab, _ in v["pruefspur"]]
        if not trail:
            die(f"{rid}: leere Prüfspur — die Zeile wäre unbrauchbar")
        for lab in cands + trail:
            if lab not in labels:
                die(f"{rid}: Etikett {lab!r} ist keine gelesene Z2-R-Klasse")
        both = sorted(set(cands) & set(trail))
        if both:
            die(f"{rid}: {', '.join(both)} steht als Kandidat UND als verworfen")
        for seq, what in ((cands, "Kandidaten"), (trail, "Prüfspur")):
            if len(set(seq)) != len(seq):
                die(f"{rid}: {what} nennt ein Etikett doppelt")
        if not v["begruendung"].strip():
            die(f"{rid}: Begründung des Vorbefunds fehlt")
        for lab, grund in v["pruefspur"]:
            if not grund.strip():
                die(f"{rid}: Prüfspureintrag {lab} ohne Grund")


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

def fence(text: str) -> str:
    fen = FENCE
    while re.search(rf"^{fen}", text, re.MULTILINE):
        fen += "~"
    return f"{fen}text\n{text}\n{fen}"


def render(rules: list[dict], classes: list[dict], texts: dict[str, dict],
           counts: list[tuple[str, int]], reader: str) -> str:
    o: list[str] = []
    w = o.append

    w("# Z2 — Überlappmatrix zu §7 Punkt 5 "
      "(Vorbefund maschinell · ENTSCHEIDUNG durch den Autor)")
    w("**Auftrag S12 · Repo `masterarbeit` · Werkzeug `tools/prepare_z2_overlap.py` · "
      f"{RUN_DATE}**")
    w(f"**Protokollstand:** `z2_protokoll_regelableitung.md`, SHA256 `{PROTO_SHA}`. "
      "Die Abschnitte (a) und (d) unten sind **wörtlich aus diesem Stand "
      "ausgeschnitten**, nicht nacherzählt.")
    w(f"**Regeldatei:** `data/soll/architecture-rules.yaml`, SHA256 `{RULES_SHA}` — "
      "eingefroren, hier nur gelesen.")
    w(f"**Nenner:** {len(rules)} autorenformulierte Statements, aus der Datei gezählt "
      "(Verteilung unten).")
    w(f"**Nachschlageteil:** {len(classes)} bewertete Vorschläge (Z2-R-Klassen aus "
      "17 Etiketten).")
    w(f"**Gelesen mit:** {reader}.")
    w("")
    w("**Dieses Blatt trifft die Entscheidung nicht.** Je Statement steht ein "
      "ausdrücklich als **MASCHINELL** gekennzeichneter **Vorbefund** — die "
      "Nachschlagearbeit, welche Vorschläge über den Sachverhalt des Statements "
      "überhaupt sprechen, samt **Begründung** und offengelegter **Prüfspur**. Die drei "
      "Felder der **ENTSCHEIDUNG DES AUTORS** sind **leer** und bleiben es, bis der "
      "Autor sie ausfüllt; sie sind **nicht vorbelegt**. Der Vorbefund ist ein "
      "**Vorschlag, keine Feststellung**.")
    w("")
    w("Es steht hier **keine Ähnlichkeitszahl**, **kein `ratio`**, **kein Ranking** und "
      "**keine Sortierung nach Nähe** — der Vorbefund ist eine **Sachverhaltsprüfung, "
      "kein Textvergleich**. Kandidaten und Prüfspur stehen in **Etikettreihenfolge**.")
    w("")
    w("**Es steht hier auch keine Summe.** Das Feld „n von 16“ in Teil 4 ist **leer**, "
      "und das Blatt bildet **keine Summe** über seine Vorbefunde: eine solche Zahl "
      "würde als Ergebnis gelesen.")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- (a)
    w("## 1. Was zu erheben ist")
    w("")
    w("### 1a (a) §7 Punkt 5 — wörtlich aus dem eingefrorenen Protokoll")
    w("")
    w("> Ausgeschnitten zwischen den Ankern `5. **Sekundär, klar gelabelt:**` und "
      "`6. ~~**B1-vs-B2-Kontrast:**`, samt durchgestrichenem Alttext und "
      "Nennerkorrektur.")
    w("")
    w(fence(cut("p5")))
    w("")

    # ---------------------------------------------------------------- (b)
    w("### 1b (b) Die Auslegung von „sinngemäss“ — Anleitung, keine Vorbelegung")
    w("")
    w("**Derselbe Sachverhalt wird verboten oder gefordert — unabhängig von Wortlaut, "
      "Kategorielabel und Scope-Granularität.** NICHT verlangt sind derselbe Wortlaut, "
      "dieselbe Kategorie oder dieselbe Präzision. Fasst ein Vorschlag den Sachverhalt "
      "**BREITER** als das Soll-Statement, zählt er **MIT VERMERK**; fasst er ihn enger "
      "oder trifft er nur einen Teil, ist das in der Begründung auszuweisen. "
      "**Mehrfachnennung ist zulässig:** ein Vorschlag kann mehreren Statements "
      "entsprechen und umgekehrt.")
    w("")
    w("Diese Auslegung sagt, **woran** zu messen ist. Sie sagt **nicht**, wie eine "
      "einzelne Zeile ausfällt — das entscheidet der Autor am Wortlaut, der unten in "
      "beiden Teilen zeichengleich steht.")
    w("")
    w("**Nach demselben Maßstab ist der maschinelle Vorbefund gebildet:** ein Etikett "
      "steht als **Kandidat**, wenn der Vorschlag über **denselben Sachverhalt** "
      "spricht — unabhängig von Wortlaut, Kategorielabel und Scope-Granularität —, und "
      "die Begründung weist aus, **wo Reichweite oder Granularität abweichen**.")
    w("")

    # ---------------------------------------------------------------- (c)
    w("### 1c (c) Das zweistufige Verfahren — Vorbefund maschinell, "
      "ENTSCHEIDUNG durch den Autor")
    w("")
    w("**Stufe 1 — maschinell, in diesem Blatt bereits ausgeführt.** Je Soll-Statement "
      "steht ein **VORBEFUND (MASCHINELL, kein Ergebnis)** mit vier Feldern: dem "
      "Verdikt „Kandidat vorhanden“ oder „kein Kandidat“, den **Etiketten** der "
      "Vorschläge, die über denselben Sachverhalt sprechen, einer **Begründung** und "
      "einer **PRÜFSPUR**, die die erwogenen und ausgeschlossenen Etiketten je mit "
      "einem Grund nennt. Die Prüfspur ist **Pflicht** — auch und besonders bei „kein "
      "Kandidat“: sie macht die Nachschlagearbeit **gegenlesbar**, statt nur ein "
      "Ergebnis zu behaupten.")
    w("")
    w("**Stufe 2 — der Autor, je Zeile.** Die drei Felder unter **ENTSCHEIDUNG DES "
      "AUTORS** sind **leer**. **Der Autor bestätigt oder überstimmt JEDE der sechzehn "
      "Zeilen; eine unbestätigte Zeile gilt nicht als entschieden.** Der Vorbefund "
      "bindet ihn nicht: er ist ein **Vorschlag, keine Feststellung**, und in seinen "
      "Formulierungen bewusst im Konjunktiv gehalten — „spricht über denselben "
      "Sachverhalt“, „Kandidat“, „zu prüfen“, nicht „entspricht“ oder „ist erfüllt“.")
    w("")
    w("**Warum zweistufig.** „Sinngemäss“ ist **dieselbe Urteilsart wie das "
      "Z2-R-Kriterium** (§6: Duplikate bei Übereinstimmung in **Kategorie, Scope und "
      "Kernaussage**). **Z2-R wurde in S10 ausdrücklich NICHT maschinisiert** — die "
      "Zusammenführung war dort auf **Zeichengleichheit** beschränkt, damit das "
      "Werkzeug **keine inhaltliche Entscheidung abnimmt**. Damit **beide Größen "
      "konsistent behandelt** werden, entscheidet der Autor auch hier je Zeile; das "
      "Werkzeug leistet die **Nachschlagearbeit** und legt seine **Prüfspur offen**.")
    w("")
    w("**Und deshalb keine Summe.** Das Blatt bildet **keine Summe** über die "
      "Vorbefunde — sie würde als Ergebnis gelesen, obwohl **keine einzige Zeile "
      "entschieden** ist. Das Summenfeld in Teil 4 bleibt **leer**.")
    w("")

    # ---------------------------------------------------------------- (d)
    w("### 1d (d) Die Einhegung — was diese Zahl NICHT ist")
    w("")
    w("Wörtlich aus §7 Punkt 5: **„Der Charakter der Größe bleibt unverändert:** "
      "sekundär, deskriptiv. Ausdrücklich KEIN Korrektheits- oder Recall-Maß (Autor "
      "beider Seiten; gleiche Logik wie Gold-Degradierung in Befund 01).“")
    w("")
    w("Ausdrücklich, und beim Ausfüllen mitzulesen:")
    w("")
    w("1. **Die Größe ist sekundär und deskriptiv** — sie steht neben den Punkten 1–4 "
      "des §7, nicht über ihnen.")
    w("2. **KEIN Korrektheitsmaß und KEIN Recall-Maß.** **Der Autor hat beide Seiten "
      "formuliert** — die sechzehn Soll-Statements **und** das Messobjekt, auf das sie "
      "passen. Die Zahl darf **NIE** als „das Modell hat n von 16 Regeln gefunden“ "
      "gelesen werden, sondern **nur** als „n Statements haben eine Entsprechung unter "
      "den Vorschlägen“.")
    w("3. **Analogie im Protokoll:** die **Gold-Degradierung aus Befund 01** — dieselbe "
      "Logik, dieselbe Grenze.")
    w("4. **T-Z2-8:** die **Affordanzen der sechs Kategorien stecken strukturell im "
      "Testrepo**. Eine hohe Überschneidung wäre **insoweit Eigenschaft des "
      "Messobjekts**, nicht Leistung des Modells. Der Wortlaut des Threats steht unter "
      "1e.")
    w("")

    # ---------------------------------------------------------------- (e)
    w("### 1e (e) Abgrenzung zu §7 Punkt 3 — verschiedene Größen, verschiedene Nenner")
    w("")
    w("| | §7 Punkt 3 — Abdeckungsmatrix | §7 Punkt 5 — Überlapp (dieses Blatt) |")
    w("|---|---|---|")
    w("| Frage | Welche der **sechs KATEGORIEN** sind durch **mindestens einen "
      "normativen, prüfbaren Vorschlag** belegt? | Welche der **sechzehn EINZELNEN "
      "Statements** haben eine Entsprechung unter den Vorschlägen? |")
    w("| Nenner | **6** Kategorien | **16** Statements |")
    w("| Status | in `auswertung.json` bereits ausgezählt (S11) | **steht aus** |")
    w("")
    w("**Nicht zu verwechseln und nicht gegeneinander zu rechnen.** Die beiden Zahlen "
      "haben verschiedene Bezugsmengen; ein Verhältnis zwischen ihnen ist ohne Bedeutung.")
    w("")
    w("> §7 Punkt 3, wörtlich:")
    w("")
    w(fence(cut("p3")))
    w("")
    w("> T-Z2-8 (§10), wörtlich:")
    w("")
    w(fence(cut("tz28")))
    w("")

    # ---------------------------------------------------------------- counts
    w("### 1f Der Nenner, aus der Datei gezählt")
    w("")
    w(f"`data/soll/architecture-rules.yaml` (SHA256 `{RULES_SHA}`) führt "
      f"**{len(rules)} Regelstatements** über **{len(counts)} Kategorien**:")
    w("")
    w("| `category` | Zahl |")
    w("|---|---|")
    for cat, n in counts:
        w(f"| `{cat}` | {n} |")
    w(f"| **Summe** | **{len(rules)}** |")
    w("")
    w("Die Reihenfolge der Statements in Teil 3 ist die **Dateireihenfolge**. Sie ist "
      "**nicht nach Kategorie gruppiert** — eine Gruppierung wäre bereits eine "
      "Lesehilfe in eine Richtung.")
    w("")

    # ---------------------------------------------------------------- blinding
    w("### 1g Vermerk zur aufgehobenen Verblindung")
    w("")
    w("Die **Herkunft je Vorschlagsklasse (K2 × B1 / K3 × B1) ist unten angegeben**. "
      "Der Zuordnungsschlüssel ist mit **S11** aufgelöst; die Bewertung war zu diesem "
      "Zeitpunkt abgeschlossen, die Verblindung ist beendet.")
    w("")
    w("**Die Größe des §7 Punkt 5 ist sekundär und deskriptiv, nicht "
      "bedingungsvergleichend.** Wird sie je Zelle aufgeschlüsselt, geschieht das "
      "**nach Aufhebung der Verblindung** — und das ist **zu berichten**.")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- lookup
    w("## 2. Nachschlageteil — die 16 bewerteten Vorschläge")
    w("")
    w("**Reihenfolge:** die Etikettreihenfolge `P-01` … `P-17`. **Nicht** nach "
      "Ähnlichkeit, Kategorie oder Herkunft sortiert — die Reihenfolge trägt keine "
      "Information über die Zuordnung.")
    w("")
    w("Die vier Dimensionen (`kind`, Z2-P, Z2-G, Z2-Z) sind **vom Bewerter gesetzt und "
      "bereits entschieden** (§6, ausgezählt in `auswertung.json`); sie stehen hier als "
      "Lesehilfe für „sinngemäss“ und sind **keine Vorbelegung** der drei leeren Felder.")
    w("")
    for cls in classes:
        members = sorted(cls["mitglieder"])
        head = members[0]
        src = texts[head]
        label = " + ".join(f"`{m}`" for m in members)
        assert class_label(cls) == " + ".join(members)
        w("---")
        w("")
        w(f"### {label}")
        w("")
        w("| Feld | Wert |")
        w("|---|---|")
        w(f"| Etikett(en) | {label} |")
        w(f"| `category` | `{src['category']}` |")
        w(f"| `severity` | `{src['severity']}` |")
        w("| `scope.components` | "
          + " · ".join(f"`{c}`" for c in src["components"]) + " |")
        w("| Herkunft (Bedingung) | "
          + " · ".join(f"`{b}`" for b in cls["bedingungen"]) + " |")
        w("| Herkunft (Läufe) | "
          + " · ".join(f"`{r}`" for r in cls["laeufe"]) + " |")
        w("")
        w("**`statement`** — zeichengleich wie im Rohartefakt:")
        w("")
        w(fence(src["statement"]))
        w("")
        w("**Vom Bewerter gesetzt (§6, bereits entschieden):**")
        w("")
        w("| Dimension | Eintrag |")
        w("|---|---|")
        dim = cls["dimensionen"]
        w(f"| `kind` | `{dim['kind']}` |")
        w(f"| **Z2-P** Prüfbarkeit | {dim['z2p']} |")
        w(f"| **Z2-G** Gehalt | {dim['z2g']} |")
        w(f"| **Z2-Z** Zuordnung | {dim['z2z']} |")
        w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- matrix
    w("## 3. Die Matrix — ein Abschnitt je Soll-Statement")
    w("")
    w("**Reihenfolge:** Dateireihenfolge von `architecture-rules.yaml`. Je Abschnitt "
      "stehen zuerst die Angaben des Statements, dann der **maschinelle Vorbefund** "
      "mit vier Feldern, dann die **drei leeren Felder der ENTSCHEIDUNG DES AUTORS**. "
      "Die beiden Blöcke sind **sichtbar getrennt**; nichts aus dem Vorbefund ist in "
      "die Entscheidungsfelder übernommen.")
    w("")
    for rule in rules:
        w("---")
        w("")
        w(f"### {rule['id']}")
        w("")
        w("| Feld | Wert |")
        w("|---|---|")
        w(f"| Soll-ID | `{rule['id']}` |")
        w(f"| `category` | `{rule['category']}` |")
        w(f"| `kind` | `{rule['kind']}` |")
        w(f"| `severity` | `{rule['severity']}` |")
        w("| `scope.components` | "
          + " · ".join(f"`{c}`" for c in rule["scope"]["components"]) + " |")
        w("")
        w("**`statement`** — zeichengleich wie in `architecture-rules.yaml`:")
        w("")
        w(fence(rule["statement"]))
        w("")
        pred = rule.get("predicate")
        if pred:
            w("**`predicate`** — zeichengleich:")
            w("")
            w("| Feld | Wert |")
            w("|---|---|")
            w(f"| `predicate.type` | `{pred['type']}` |")
            w("| `predicate.allowed_importers` | "
              + " · ".join(f"`{c}`" for c in pred["allowed_importers"]) + " |")
            w("")
        v = VORBEFUNDE[rule["id"]]
        # Label order, never proximity: both lists are sorted here so that the
        # order in the sheet carries no information about the decision.
        kand = sorted(v["kandidaten"])
        spur = sorted(v["pruefspur"], key=lambda e: e[0])
        cands = " · ".join(f"`{c}`" for c in kand) if kand else "—"
        w("#### VORBEFUND (MASCHINELL, kein Ergebnis)")
        w("")
        w("> **Maschinell erzeugte Nachschlagearbeit — ein VORSCHLAG, keine "
          "Feststellung.** Der Vorbefund nimmt die Entscheidung nicht vorweg und "
          "bindet den Autor nicht.")
        w("")
        w("| Feld | Eintrag |")
        w("|---|---|")
        w(f"| **(a) VORBEFUND (maschinell)** | **{v['befund']}** |")
        w(f"| **(b) Kandidat(en)** | {cands} |")
        w(f"| **(c) Begründung des Vorbefunds** | {v['begruendung']} |")
        w("")
        w("**(d) PRÜFSPUR — geprüft und verworfen:**")
        w("")
        w("| Etikett | Grund des Ausschlusses |")
        w("|---|---|")
        for lab, grund in spur:
            w(f"| `{lab}` | {grund} |")
        w("")
        w("#### ENTSCHEIDUNG DES AUTORS")
        w("")
        w("> **Vom Autor auszufüllen. Hier leer und nicht vorbelegt.** Der Autor "
          "**bestätigt oder überstimmt** den Vorbefund; eine unbestätigte Zeile gilt "
          "**nicht als entschieden**.")
        w("")
        w("| Feld | Eintrag |")
        w("|---|---|")
        w("| **ENTSCHEIDUNG (ja \\| nein)** | |")
        w("| **durch welche(s) P-xx** | |")
        w("| **Begründung des Autors** | |")
        w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- sum
    w("## 4. Summenfeld — leer")
    w("")
    w(f"**n von {len(rules)} = ___**")
    w("")
    w("| Größe | Eintrag |")
    w("|---|---|")
    w(f"| **n von {len(rules)}** | ___ |")
    w("")
    w("**Die Zahl wird erst nach dem Ausfüllen der Matrix gebildet** — aus den Feldern "
      "**ENTSCHEIDUNG DES AUTORS**, nicht aus den Vorbefunden und nicht daneben. In "
      "**S13** wird sie **mechanisch nachgerechnet**: gezählt werden die Abschnitte mit "
      f"„ja“, der Nenner bleibt {len(rules)}.")
    w("")
    w("**Die Vorbefunde ergeben diese Zahl NICHT.** Sie sind Nachschlagearbeit, nicht "
      "Entscheidung; das Blatt weist deshalb **keine Summe** über sie aus. Wer "
      "die Kandidatenzeilen zählt, hat **nicht** „n von "
      f"{len(rules)}“ gebildet, sondern eine **Arbeitsangabe** über den Stand der "
      "Nachschlagearbeit.")
    w("")
    w("**Beim Eintragen gilt die Einhegung aus 1d:** die Zahl heisst „n Statements haben "
      "eine Entsprechung unter den Vorschlägen“ — nie „das Modell hat n von "
      f"{len(rules)} Regeln gefunden“.")
    w("")
    return "\n".join(o) + "\n"


def write_sums(out_dir: Path) -> str:
    names = sorted(p.name for p in out_dir.iterdir()
                   if p.is_file() and p.name != SUMS_NAME)
    body = "".join(f"{sha256_of(out_dir / n)}  {n}\n" for n in names)
    (out_dir / SUMS_NAME).write_text(body, encoding="utf-8")
    return body


def build(out_dir: Path) -> str:
    for path, want, what in ((PROTO_PATH, PROTO_SHA, "Protokoll"),
                             (RULES_PATH, RULES_SHA, "Regeldatei")):
        got = sha256_of(path)
        if got != want:
            die(f"{what} {path.name}: SHA256 {got} != gepinnt {want}")

    rules, reader = load_rules()
    if len(rules) != EXPECTED_RULES:
        die(f"{len(rules)} Regelstatements statt {EXPECTED_RULES} — der registrierte "
            "Nenner des §7 Punkt 5 stimmt dann nicht")

    counts: list[tuple[str, int]] = []
    for rule in rules:
        for i, (cat, n) in enumerate(counts):
            if cat == rule["category"]:
                counts[i] = (cat, n + 1)
                break
        else:
            counts.append((rule["category"], 1))
    counts.sort(key=lambda cn: (-cn[1], cn[0]))

    classes = load_classes()
    texts = load_proposal_texts()
    check_vorbefunde(rules, classes)
    body = render(rules, classes, texts, counts, reader)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / MATRIX_NAME).write_text(body, encoding="utf-8")
    return body


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="regenerate into a temporary directory and compare bytes")
    args = ap.parse_args()

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            fresh = build(Path(tmp))
            have = (OUT_DIR / MATRIX_NAME).read_bytes()
            if fresh.encode("utf-8") != have:
                die(f"{MATRIX_NAME} weicht von der Neuerzeugung ab")
        print(f"DETERMINISMUS OK: {MATRIX_NAME} bytegleich "
              f"({sha256_of(OUT_DIR / MATRIX_NAME)})")
        return 0

    build(OUT_DIR)
    sums = write_sums(OUT_DIR)
    print(f"geschrieben: {OUT_DIR / MATRIX_NAME}")
    print(f"SHA256 {sha256_of(OUT_DIR / MATRIX_NAME)}")
    print(f"--- {SUMS_NAME}\n{sums}", end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
