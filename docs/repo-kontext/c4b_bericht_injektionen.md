# C4b — Bau der 32 Injektions-Commits

**Masterarbeit Timo Haas · HTWG Konstanz**
**Datum:** 25. August 2026 · Phase 04, Schritt C4b
**Schreibend:** `~/ma/ma-conformance-testrepo` — 32 Commits, 32 Refs. **Nicht gepusht.**
**Lesend:** `~/ma/masterarbeit` (Spezifikation und Manifest). `~/ma/tritongraph` **nicht angefasst.**

**Kein Modell-Call. Kein Aufruf des Checkers, der Rule-Engine, von import-linter oder
PyTestArch — auch nicht probeweise.** Die Verifikation dieses Berichts ist rein strukturell:
`git`, das Standardmodul `ast` und `python -m compileall`. Kein Laufzeitimport des
Testrepositoriums.

**Quellen, verbindlich:** `data/soll/injection_manifest.md` (Fassung nach Rev. 28) ·
`docs/planung/c1_modulliste.md` Rev. 5 §1/§2/§D · `docs/planung/c1_komponentenschnitt.md`
Rev. 3 §4/§5 · `docs/protokolle/eval_protokoll_phase04.md` Rev. 28 §2/§3/§6 ·
`data/soll/architecture-rules.yaml` (R-PORT-1…4, R-FRAMEWORK-1, R-PLACE-1, R-SIG-1…4) ·
`data/soll/test_architecture.py` (K5-1-Sperrliste).

**Ergebnis:** 32 Commits, jeder mit `baseline` als einzigem Elternteil, jeder unter einem
leichtgewichtigen Tag `inj/01` … `inj/32`. `baseline` steht unverändert auf
`0d651041ed87dd03f2f78359713633fac01c0a66`, `main` ebenso, `git status --porcelain` leer.
Alle Prüfungen aus §3 und §4 des Auftrags mit **0 Verstößen** — mit **einer** benannten
Abweichung zu Prüfpunkt 4e, die aus der Spezifikation selbst folgt (§7.1 unten).

---

## 1. Refform: leichtgewichtige Tags, nicht Branches

Gewählt: **leichtgewichtige Tags** `refs/tags/inj/01` … `refs/tags/inj/32`, je direkt auf den
Injektionscommit zeigend (`git cat-file -t inj/01` → `commit`).

Begründung, drei Gründe:

1. **Konsistenz mit dem bestehenden Messstand.** Der Clean-Zustand ist bereits als **Tag**
   (`baseline`) geführt, und Protokoll §6 verlangt, den Freeze-Tag über seinen SHA zu führen.
   Die Injektionsstände sind Messstände derselben Art — ein fixierter Zeigepunkt, kein
   Entwicklungszweig.
2. **Ein Branch lädt zum Weiterschreiben ein.** `git commit` auf einem ausgecheckten Branch
   verschiebt ihn stillschweigend; ein Tag müsste dafür ausdrücklich mit `-f` überschrieben
   werden. Bei 32 Ständen, die über die ganze Kampagne unverändert bleiben müssen, ist die
   höhere Hürde der Zweck.
3. **`git gc`-Erreichbarkeit und `git bundle --all` sind für beide Formen gleich erfüllt**
   (Protokoll §6, Amendment 12.08.), die Form ist an dieser Stelle also frei — und damit
   entscheiden die beiden Gründe oben.

Einheitlich durchgehalten: **32 von 32** Refs sind Tags, keiner ist ein Branch
(`git branch -a` zeigt weiterhin nur `main` und `origin/main`).

**Bauweg je Injektion, unverändert für alle 32:** `git checkout --detach baseline` → Änderung →
`git add` bzw. `git mv` → `git commit -m "<eine Zeile>"` → `git tag inj/NN`. Danach zurück auf
`baseline` für die nächste. Zum Schluss `git checkout main`.

---

## 2. Die 32 Injektionen in Kurzform

Spalte „unerlaubte Kante" und „Komponentenzyklus" sind **Messwerte** aus der Prüfschrift
(§4 unten), nicht Absichtserklärungen.

| ID | Ref | Commit | Szenario | Diff (`--no-renames`) | Umfang | unerlaubte Komponentenkante | Komponentenzyklus |
|---|---|---|---|---|---|---|---|
| I01 | `inj/01` | 439125ece2 | LAYER_BACK_CALL | M `…/identity/repository/customer_repo.py` | 1 Datei, +5 | `identity_repository->identity_services` | `identity_repository->identity_services` |
| I02 | `inj/02` | 4165fab5c8 | LAYER_BACK_CALL | M `…/orders/repository/order_repo.py` | 1 Datei, +5 | `orders_repository->orders_services` | `orders_repository->orders_services` |
| I03 | `inj/03` | b3fb12905f | LAYER_BACK_CALL | M `…/billing/repository/invoice_repo.py` | 1 Datei, +5 | `billing_repository->billing_services` | `billing_repository->billing_services` |
| I04 | `inj/04` | 3de8357bc1 | LAYER_SKIP_CALL | M `…/identity/api/routes.py` | 1 Datei, +7 | `identity_api->identity_repository` | — |
| I05 | `inj/05` | dbcd05b893 | LAYER_SKIP_CALL | M `…/orders/api/routes.py` | 1 Datei, +7 | `orders_api->orders_repository` | — |
| I06 | `inj/06` | 531a1ff261 | LAYER_SKIP_CALL | M `…/billing/api/routes.py` | 1 Datei, +7 | `billing_api->billing_repository` | — |
| I07 | `inj/07` | 0993e01b26 | PROTECTED_MODULE | M `…/identity/services/customer_service.py` | 1 Datei, +8 | `identity_services->core_adapters_internal` | — |
| I08 | `inj/08` | 792cb6867f | PROTECTED_MODULE | M `…/orders/services/order_service.py` | 1 Datei, +8 | `orders_services->core_adapters_internal` | — |
| I09 | `inj/09` | 06e052e19c | PROTECTED_MODULE | M `…/billing/services/invoice_service.py` | 1 Datei, +8 | `billing_services->core_adapters_internal` | — |
| I10 | `inj/10` | e1829642b3 | INDEPENDENCE | M `…/orders/services/checkout_service.py` | 1 Datei, +15 | `orders_services->billing_services` | — |
| I11 | `inj/11` | 5601a944ea | INDEPENDENCE | M `…/billing/services/dunning_service.py` | 1 Datei, +5 | `billing_services->orders_models` | — |
| I12 | `inj/12` | cb1fb228ff | INDEPENDENCE | M `…/orders/repository/order_line_repo.py` | 1 Datei, +12 | `orders_repository->billing_repository` | — |
| I13 | `inj/13` | 3be646fed3 | CYCLE_SIBLING | M `…/identity/mappers/customer_mapper.py` | 1 Datei, +9 | `identity_mappers->identity_api` | `identity_api->identity_mappers` |
| I14 | `inj/14` | a9d6445158 | CYCLE_SIBLING | M `…/orders/mappers/order_mapper.py` | 1 Datei, +9 | `orders_mappers->orders_api` | `orders_api->orders_mappers` |
| I15 | `inj/15` | 616cb02982 | CYCLE_SIBLING | M `…/billing/mappers/invoice_mapper.py` | 1 Datei, +9 | `billing_mappers->billing_api` | `billing_api->billing_mappers` |
| I16 | `inj/16` | 43f9fa5ec1 | CYCLE_PARENT_CHILD | M `…/orders/services/pricing/engine.py` | 1 Datei, +5 | `orders_services_pricing->orders_services` | `orders_services->orders_services_pricing` |
| I17 | `inj/17` | c5faa0a65f | MISSING_PORT_REFERENCE | M `…/identity/services/token_service.py` | 1 Datei, +1/−2 | — | — |
| I18 | `inj/18` | ad210637f5 | MISSING_PORT_REFERENCE | M `…/orders/services/catalog_service.py` | 1 Datei, +1/−2 | — | — |
| I19 | `inj/19` | 864da9678e | MISSING_PORT_REFERENCE | M `…/orders/services/refund_service.py` | 1 Datei, +1/−2 | — | — |
| I20 | `inj/20` | 35061d8526 | MISSING_PORT_REFERENCE | M `…/billing/services/ledger_service.py` | 1 Datei, +1/−2 | — | — |
| I21 | `inj/21` | dd414657d1 | FRAMEWORK_TYPE_IN_SIGNATURE | M `…/identity/models/customer_models.py` | 1 Datei, +4 | — | — |
| I22 | `inj/22` | 08a622b024 | FRAMEWORK_TYPE_IN_SIGNATURE | M `…/orders/models/order_models.py` | 1 Datei, +4 | — | — |
| I23 | `inj/23` | 28a7574949 | FRAMEWORK_TYPE_IN_SIGNATURE | M `…/orders/models/order_line_models.py` | 1 Datei, +4 | — | — |
| I24 | `inj/24` | 91ed6a80d4 | FRAMEWORK_TYPE_IN_SIGNATURE | M `…/billing/models/invoice_models.py` | 1 Datei, +4 | — | — |
| I25 | `inj/25` | ef114806ec | INCORRECT_LOCATION | **A** `…/orders/legacy_order_index.py`, **D** `…/orders/repository/legacy_order_index.py` | 2 Dateien, +48/−48 | — | — |
| I26 | `inj/26` | efe5c81f52 | INCORRECT_LOCATION | **A** `…/billing/legacy_invoice_index.py`, **D** `…/billing/repository/legacy_invoice_index.py` | 2 Dateien, +48/−48 | — | — |
| I27 | `inj/27` | 33ad86a07d | INCORRECT_LOCATION | **A** `…/identity/legacy_token_index.py`, **D** `…/identity/repository/legacy_token_index.py` | 2 Dateien, +45/−45 | — | — |
| I28 | `inj/28` | 72dc7461f9 | INCORRECT_LOCATION | **A** `…/billing/legacy_tax_models.py`, **D** `…/billing/models/legacy_tax_models.py` | 2 Dateien, +68/−68 | — | — |
| I29 | `inj/29` | 5e685cff95 | SIGNATURE_DEVIATION | M `…/identity/repository/session_repo.py` | 1 Datei, +1/−1 | — | — |
| I30 | `inj/30` | 604d30460c | SIGNATURE_DEVIATION | M `…/orders/repository/order_query.py` | 1 Datei, +1/−1 | — | — |
| I31 | `inj/31` | 3d33745711 | SIGNATURE_DEVIATION | M `…/billing/repository/invoice_query.py` | 1 Datei, +1/−1 | — | — |
| I32 | `inj/32` | 307e57327a | SIGNATURE_DEVIATION | M `…/orders/mappers/order_line_mapper.py` | 1 Datei, +1/−1 | — | — |

**Zu I25–I28 ausdrücklich:** der Umzug erscheint mit `--no-renames` als **eine hinzugefügte und
eine gelöschte** Datei. Mit Vorgabestellung (Umbenennungserkennung an) meldet `git diff` je eine
Zeile `R100` — dieselbe Änderung, andere Darstellung. Für den Messpfad zählt die erste Lesart:
gelöschte Dateien fallen aus dem Diff heraus, der Umzug erreicht den LLM-Pfad als **hinzugefügte
Datei** (`b33_bericht_diff_erzeugung.md`, Schritt 1; Protokoll §3 Amendment (e)). Inhalt
unverändert — die Zeilenzahlen +48/−48, +45/−45, +68/−68 sind Datei für Datei identisch.

### 2.1 Die injizierte Kante je Commit, auf Modulebene

Je Commit **genau eine** neue Importkante; die Spalte ist der Zeuge der Komponentenkante oben.

| ID | injizierte Modulkante |
|---|---|
| I01 | `depot.identity.repository.customer_repo` → `depot.identity.services.customer_service` |
| I02 | `depot.orders.repository.order_repo` → `depot.orders.services.order_service` |
| I03 | `depot.billing.repository.invoice_repo` → `depot.billing.services.invoice_service` |
| I04 | `depot.identity.api.routes` → `depot.identity.repository.customer_repo` |
| I05 | `depot.orders.api.routes` → `depot.orders.repository.order_repo` |
| I06 | `depot.billing.api.routes` → `depot.billing.repository.invoice_repo` |
| I07 | `depot.identity.services.customer_service` → `depot.core.adapters.internal.session` |
| I08 | `depot.orders.services.order_service` → `depot.core.adapters.internal.session` |
| I09 | `depot.billing.services.invoice_service` → `depot.core.adapters.internal.session` |
| I10 | `depot.orders.services.checkout_service` → `depot.billing.services.invoice_service` |
| I11 | `depot.billing.services.dunning_service` → `depot.orders.models.order_models` |
| I12 | `depot.orders.repository.order_line_repo` → `depot.billing.repository.invoice_repo` |
| I13 | `depot.identity.mappers.customer_mapper` → `depot.identity.api.routes` |
| I14 | `depot.orders.mappers.order_mapper` → `depot.orders.api.routes` |
| I15 | `depot.billing.mappers.invoice_mapper` → `depot.billing.api.routes` |
| I16 | `depot.orders.services.pricing.engine` → **`depot.orders.services`** (Paketmodul) |

Jede dieser 16 Kanten ist zeichengleich die aus der Bemerkungsspalte von
`c1_modulliste.md` §1. I16 ergänzt das **Paketmodul**, wie mit Protokoll §3 Nachtrag Rev. 28
verbindlich festgelegt.

### 2.2 Wie der injizierte Import benutzt wird

Der Auftrag verlangt, dass der injizierte Import im Code **benutzt** wird, sonst ist die
Injektion bei einer Sichtprüfung als Attrappe erkennbar. Durchgehendes Muster: der Träger
bekommt **ein** kleines, vollständig annotiertes öffentliches Element, das das importierte
Modul konsumiert. Kein bestehender Aufrufer wird gebrochen, keine bestehende Signatur bewegt
sich, kein Import verschwindet.

| ID | Verwendung |
|---|---|
| I01–I03 | Methode, die eine Benachrichtigungsvorlage aus dem Service liest (`BLOCKED_TEMPLATE`, `PLACED_TEMPLATE`, `ISSUED_TEMPLATE`) |
| I04–I06 | Route-Methode, die das Repository als Parametertyp führt und direkt daraus liest (`count()`, `open_total_cents()`) |
| I07–I09 | Service-Methode, die eine `…internal.session.Session` als Parametertyp führt und darauf `execute`/`commit` ruft |
| I10 | `CheckoutService.bill_after_handover` mit `…billing.services.invoice_service.InvoiceService` als Parametertyp |
| I11 | `DunningService.is_dispatched` vergleicht gegen `…orders.models.order_models.STATUS_DISPATCHED` |
| I12 | `OrderLineRepository.billed_order_of` mit `…billing.repository.invoice_repo.InvoiceRepository` als Parametertyp |
| I13–I15 | Modulfunktion `to_error_payload`, die `…api.routes.status_for(error)` ruft |
| I16 | `PricingEngine.matches_context_handling` vergleicht gegen `depot.orders.services.HANDLING_PERCENT` |

Alle Importe stehen als `import depot.x.y` **auf Modulebene**; kein `from … import`, kein
`import … as`, nichts im Funktionsrumpf, nichts unter `if TYPE_CHECKING`. Maschinell geprüft,
§4.4.

---

## 3. `FORBIDDEN_SIGNATURE_TYPE` (I21–I24) — die vier Signaturen wörtlich

Festgelegt in Protokoll §3 Nachtrag Rev. 28: injiziert wird **`sqlalchemy.orm.Session`** als
Annotation eines Parameters oder des Rückgabewerts einer **öffentlichen** Methode der
Trägerklasse. Die tragende Methode und die **wörtliche Schreibweise** waren dort ausdrücklich
„von C4b zu benennen" — hier sind sie:

| ID | Träger | Klasse | Methode | Signatur **wörtlich aus dem Code** | `offending_type` **wörtlich** |
|---|---|---|---|---|---|
| I21 | `depot.identity.models.customer_models` | `Customer` | `Customer.reload` | `def reload(self, session: sqlalchemy.orm.Session) -> None:` | `sqlalchemy.orm.Session` |
| I22 | `depot.orders.models.order_models` | `Order` | `Order.reload` | `def reload(self, session: sqlalchemy.orm.Session) -> None:` | `sqlalchemy.orm.Session` |
| I23 | `depot.orders.models.order_line_models` | `OrderLine` | `OrderLine.reload` | `def reload(self, session: sqlalchemy.orm.Session) -> None:` | `sqlalchemy.orm.Session` |
| I24 | `depot.billing.models.invoice_models` | `Invoice` | `Invoice.reload` | `def reload(self, session: sqlalchemy.orm.Session) -> None:` | `sqlalchemy.orm.Session` |

Der Rumpf ist je `session.refresh(self)`, der Docstring nennt die Klasse.

**Die Schreibweise ist qualifiziert, `sqlalchemy.orm.Session`, nicht `Session`.** Das ist keine
Stilwahl: die Bauvorschrift „nur `import pkg.modul`, nie `from pkg import modul`" (B9+,
Protokoll §3 Amendment (c)) lässt die unqualifizierte Form gar nicht zu — `Session` wäre ohne
`from sqlalchemy.orm import Session` ein `NameError`, und dieser Import ist verboten. Die
qualifizierte Form ist damit **erzwungen**, nicht gewählt. **C4c übernimmt genau diese Kette
als `offending_type`.**

**Die drei Auflagen aus Rev. 28, je geprüft:**

- **(a) öffentliche, vom Extractor erfasste Methode.** `reload` ist eine Klassenmethode ohne
  führenden Unterstrich, also eine `Class.method`-Signatur im Sinne von
  `b1_bericht_matchkey.md` C4. Der Symbolname im `match_key` lautet entsprechend
  `Customer.reload` / `Order.reload` / `OrderLine.reload` / `Invoice.reload` — für
  `FORBIDDEN_SIGNATURE_TYPE` ist der `subjectKey` allerdings der `offending_type`, nicht das
  Symbol (Manifest §1c).
- **(b) kein neuer Import.** `import sqlalchemy.orm` steht in allen vier Trägern bereits in der
  Clean-Baseline; die Importmenge ist vor und nach der Injektion identisch und damit weiterhin
  **zeichengleich mit der des Zwillings**. Maschinell geprüft: die Komponentenkantenzahl bleibt
  bei allen vier Commits bei 39, `sqlalchemy.orm` ist unmapped und erzeugt keine Kante.
- **(c) kein gebrochener Aufrufer.** `reload` ist **neu**; keine bestehende Signatur ist
  verändert, kein bestehender Aufruf berührt. Der Diff ist je genau eine Datei.

**Genau ein Vorkommen je Träger** (Singular-Regel, Protokoll §3 Nachtrag Rev. 17): die
Zeichenkette `sqlalchemy.orm.Session` kommt in jeder der vier Dateien **einmal** vor. Die
`sqlalchemy.orm.Mapped[…]`-Klassenattribute und die `sqlalchemy.orm.mapped_column(…)`-Aufrufe
sind von R-FRAMEWORK-1 ausdrücklich erlaubt und unberührt geblieben.

**Der Zwilling bleibt unberührt.** `customer_view_models`, `order_view_models`,
`order_line_view_models` und `invoice_view_models` stehen in keinem der 32 Commits im Diff.

**Warum eine neue Methode und keine bestehende.** Alle vier Träger sind Datensatzklassen, deren
öffentliche Methoden von den Repositories aufgerufen werden (`customer.mark_verified(…)`,
`order.place(…)`, `line.check()`, `invoice.issue(…)`). Ein `sqlalchemy.orm.Session`-Parameter
an einer dieser Methoden hätte deren Aufrufer gebrochen und den Diff auf zwei Dateien
ausgedehnt — Auflage (c) verletzt. Eine Methode mit **Vorgabewert** hätte den Typ als
`sqlalchemy.orm.Session | None` schreiben müssen und damit den `offending_type` verunreinigt.
Die neue Methode ist der einzige Weg, der alle drei Auflagen zugleich hält.

---

## 4. `SIGNATURE_DEVIATION` (I29–I32) — vorher/nachher wörtlich

Bauvorschrift (Protokoll §3 Amendment (h)): der abweichende Typ ist ein **Builtin** oder ein
bereits importierter Typ; die Injektion **fügt keinen Import hinzu und entfernt keinen**. Die
Soll-Signaturen stehen wörtlich im `statement` von R-SIG-1…4.

| ID | Symbol | Soll-Signatur (R-SIG-n, = Clean-Baseline) | Signatur nach der Injektion | Abweichung |
|---|---|---|---|---|
| I29 | `SessionRepository.touch` | `def touch(self, session_id: str, ttl_seconds: int) -> bool:` | `def touch(self, session_id: str, ttl_seconds: float) -> bool:` | Parametertyp `int` → `float` |
| I30 | `OrderQuery.percent_for` | `def percent_for(self, code: str, subtotal_cents: int) -> int:` | `def percent_for(self, code: str, subtotal_cents: int) -> float:` | Rückgabetyp `int` → `float` |
| I31 | `InvoiceQuery.settled_cents` | `def settled_cents(self, invoice_number: str) -> int:` | `def settled_cents(self, invoice_number: str) -> float:` | Rückgabetyp `int` → `float` |
| I32 | `to_payload` | `def to_payload(line: depot.orders.models.order_line_models.OrderLine) -> dict[str, object]:` | `def to_payload(line: depot.orders.models.order_line_models.OrderLine) -> dict[str, str]:` | Rückgabetyp `dict[str, object]` → `dict[str, str]` |

Zu I32: die Signatur ist in der Datei über drei Zeilen umbrochen (black) und trägt dort ein
Magic Trailing Comma; oben ist sie — wie in `architecture-rules.yaml` — auf **einer** logischen
Zeile **ohne** dieses Komma wiedergegeben. Die Tokenfolge ist im Übrigen identisch. Geändert
wurde ausschließlich die Zeile `) -> dict[str, object]:` → `) -> dict[str, str]:`.

`int`, `float`, `bool`, `str`, `dict` und `object` sind Builtins — **kein Import kommt hinzu,
keiner fällt weg**, in keinem der vier Commits. Maschinell geprüft: 39 Komponentenkanten, wie in
der Baseline. Kein Parameter ist hinzugefügt oder entfernt, kein Parametername ist geändert; die
bestehenden Aufrufe (`self.sessions.touch(session_id, DEFAULT_TTL_SECONDS)`,
`self.payments.settled_cents(invoice_number)`) sind unberührt. Der Diff ist je **eine Zeile**.

---

## 5. `MISSING_PORT_REFERENCE` (I17–I20) — Annotation und Import entfernt

Protokoll §3 Amendment (f): Port-Typ-Referenz aus der öffentlichen Signatur **und** den
zugehörigen Import entfernen. In allen vier Trägern war `import depot.core.ports` **allein**
durch diese eine Annotation belegt — nach dem Entfernen der Annotation wäre er ein unbenutzter
Import gewesen; beides zusammen zu entfernen ist damit auch die einzige Form, die Prüfpunkt 3d
(kein unbenutzter Import) hält.

| ID | Methode | vorher | nachher |
|---|---|---|---|
| I17 | `TokenService.issue` | `signer: depot.core.ports.TokenSigner` | `signer: object` |
| I18 | `CatalogService.quote_cents` | `rates: depot.core.ports.RateProvider` | `rates: object` |
| I19 | `RefundService.refund` | `gateway: depot.core.ports.PaymentGateway` | `gateway: object` |
| I20 | `LedgerService.post_invoice` | `clock: depot.core.ports.Clock` | `clock: object` |

Der Porttyp verschwindet damit **vollständig** aus der Datei: die Zeichenketten
`depot.core.ports`, `TokenSigner`, `RateProvider`, `PaymentGateway` bzw. `Clock` kommen in
keiner der vier Dateien mehr vor.

**Warum `object` und nicht ersatzlos.** Prüfpunkt 3e verlangt, dass die vollständige
Typannotation aller Funktionen und Methoden der geänderten Datei **erhalten** bleibt; ein
Parameter ohne Annotation hätte sie verletzt. `object` ist ein Builtin und fügt keinen Import
hinzu — das Rezept sagt „Modul bleibt sonst unverändert", und `typing.Any` hätte einen neuen
(wenn auch unmapped) Import gebraucht. Die Parameter selbst bleiben stehen, damit kein Aufrufer
bricht und der Diff eine Datei bleibt.

---

## 6. `INCORRECT_LOCATION` (I25–I28) — Umzug, Inhalt unverändert

| ID | von | nach | Zielort ist direktes Kind von | verletzte Klausel |
|---|---|---|---|---|
| I25 | `src/depot/orders/repository/legacy_order_index.py` | `src/depot/orders/legacy_order_index.py` | `depot.orders` | R-PLACE-1 Klausel 1 (`_index`) |
| I26 | `src/depot/billing/repository/legacy_invoice_index.py` | `src/depot/billing/legacy_invoice_index.py` | `depot.billing` | R-PLACE-1 Klausel 1 (`_index`) |
| I27 | `src/depot/identity/repository/legacy_token_index.py` | `src/depot/identity/legacy_token_index.py` | `depot.identity` | R-PLACE-1 Klausel 1 (`_index`) |
| I28 | `src/depot/billing/models/legacy_tax_models.py` | `src/depot/billing/legacy_tax_models.py` | `depot.billing` | R-PLACE-1 Klausel 2 (`_models`) |

Die vier Zielorte sind zeichengleich die im Manifest §2 gelisteten Phantomeinträge. Der Umzug
ist ein reiner `git mv`; **der Inhalt ist unverändert** — die Blob-Hashes vor und nach dem Umzug
sind identisch, was `git diff` mit Umbenennungserkennung als `R100` ausweist.

**Import- und Referenzfreiheit nach dem Umzug, geprüft (Abnahmebedingung 8):** in allen vier
Commits hat das verschobene Modul **0 ausgehende Importe** (`ast`: keine `Import`- und keine
`ImportFrom`-Knoten) und **0 eingehende Referenzen** (kein anderes Modul des Commits nennt es in
einem Import). Damit bleibt die vorregistrierte Zelle K5/`INCORRECT_LOCATION` = nein tragfähig.

**Nichts sonst hat sich bewegt:** die verlassenen Pakete (`orders/repository`,
`billing/repository`, `identity/repository`, `billing/models`) behalten ihre `__init__.py` und
alle übrigen Module.

---

## 7. Verifikation je Commit (§3 des Auftrags) — Ist-Zahlen

Die Prüfschrift liest jeden Commit über `git ls-tree`/`git show`, parst mit `ast` und legt für
`compileall` einen Wegwerf-Baum in einem Temporärverzeichnis an. **Kein Werkzeug der Kampagne
läuft**, und das Arbeitsverzeichnis wird dabei nicht berührt.

| Prüfpunkt | Ist über alle 32 |
|---|---|
| **3a** genau eine Datei im Diff (`--no-renames`) | I01–I24, I29–I32: **1** Datei, Status `M`. I25–I28: **1 hinzugefügt (`A`), 1 gelöscht (`D`)** — ausgewiesen in §2 |
| **3b** `git rev-parse inj/NN^` == `0d651041…` | **32 von 32**; jeder Commit hat genau **einen** Elternteil, kein Merge |
| **3c** `python -m compileall src/depot` | **32 von 32** mit Rückgabewert **0**, keine Ausgabe. Bei I16 **kein** Laufzeitimport versucht (§D.6) |
| **3d** `ast`: kein `from … import`, kein `import … as`, kein Import außerhalb des Modulkopfs, kein unbenutzter Import | **0 Befunde** über alle geänderten Dateien |
| **3e** vollständige Typannotation aller Funktionen und Methoden der geänderten Datei | **0 Befunde**; jede `FunctionDef` hat `returns` und jeder Parameter außer `self` eine Annotation |

### 7.1 Zu 3c und I16 sowie I01–I03: die zirkulären Importe

`compileall` prüft die Syntax, nicht die Importierbarkeit — es ist deshalb auf **alle** Commits
anwendbar und läuft auf allen 32 fehlerfrei durch.

I16 erzeugt einen echten Laufzeit-Zirkelimport zwischen `depot.orders.services` und
`depot.orders.services.pricing.engine` (`c1_modulliste.md` §D.6, Protokoll §3 Nachtrag Rev. 28).
Kein Laufzeitimport wurde versucht.

**Neu und hier zu vermerken:** dasselbe gilt für **I01–I03**. Die `LAYER_BACK_CALL`-Injektion
ergänzt die Rückkante genau zwischen dem Modulpaar, dessen Vorwärtskante die Clean-Baseline
schon trägt (`customer_service` → `customer_repo`, `order_service` → `order_repo`,
`invoice_service` → `invoice_repo`) — der Modulname ist in
`c1_modulliste.md` §1 wörtlich vorgeschrieben und lässt keine andere Wahl. Auf **Modulebene**
entsteht damit in diesen drei Commits ebenfalls ein Zweierzyklus. Für die statische Messung
folgenlos (K1, K4 und K5 arbeiten rein statisch); die drei Commits sind wie I16 von einem
Laufzeit-Smoke-Test auszunehmen. Der Vermerk gehört sachlich zu §D.6 der Modulliste und ist dort
bisher nur für I16 geführt.

---

## 8. Verifikation über alle 32 (§4 des Auftrags) — Ist-Zahlen

### 8.1 (4a) Refs

32 Tags `inj/01` … `inj/32`, **lückenlos**, keiner fehlt, keiner zu viel
(`git tag -l 'inj/*'` → 32 Zeilen). Jeder zeigt auf einen Commit mit **genau einem** Elternteil,
und dieser ist `0d651041ed87dd03f2f78359713633fac01c0a66`. **Sternform bestätigt.**

### 8.2 (4b) Träger

**32 paarweise verschiedene Trägermodule**, kein Modul zweimal. Die vier Zwillinge
(`customer_view_models`, `order_view_models`, `order_line_view_models`, `invoice_view_models`)
sind in **keinem** der 32 Diffs enthalten. Die Trägerliste ist zeilengleich mit der Spalte
„Trägermodul" des Manifests §2 und mit der Rolle „Injektionsträger" in `c1_modulliste.md` §1.

### 8.3 (4c) Verteilung

| Szenario | Soll | Ist |
|---|---|---|
| `LAYER_BACK_CALL` | 3 | 3 (I01–I03) |
| `LAYER_SKIP_CALL` | 3 | 3 (I04–I06) |
| `PROTECTED_MODULE` | 3 | 3 (I07–I09) |
| `INDEPENDENCE` | 3 | 3 (I10–I12) |
| `CYCLE_SIBLING` | 3 | 3 (I13–I15) |
| `CYCLE_PARENT_CHILD` | 1 | 1 (I16) |
| `MISSING_PORT_REFERENCE` | 4 | 4 (I17–I20) |
| `FRAMEWORK_TYPE_IN_SIGNATURE` | 4 | 4 (I21–I24) |
| `INCORRECT_LOCATION` | 4 | 4 (I25–I28) |
| `SIGNATURE_DEVIATION` | 4 | 4 (I29–I32) |
| **Summe** | **32** | **32** |

**3/3/3/3/3/1/4/4/4/4 — erfüllt.**

### 8.4 (4d) Komponentengraph je Injektionscommit

Zuordnung Modul → Komponente aus `c1_modulliste.md` §1 (**nicht** aus dem Pfad — die fünf
leeren Paketmodule `depot`, `depot.core`, `depot.identity`, `depot.orders`, `depot.billing`
gehören zur Komponente `core`, §D.11). Whitelist aus Komponentenschnitt §4: **39 gerichtete
Komponentenpaare**, per Assertion nachgezählt. Intra-Komponenten-Kanten (`from === to`) sind
nicht gezählt (V4).

**Clean-Baseline zur Kontrolle:** 73 `.py`-Dateien, **39 Komponentenkanten**, **0 unerlaubt**,
**0 Zyklen**. Deckungsgleich mit `c1_modulliste.md` §4 Bedingung 6.

| Commits | Erwartung | Ist |
|---|---|---|
| I01–I16 | genau **eine** unerlaubte Kante, nämlich die injizierte | **je genau 1**, und je zeichengleich die aus dem Manifest §2 erwartete — Spalte in §2 oben, Zeuge in §2.1 |
| I17–I32 | **keine** unerlaubte Kante | **je 0** |

Kantenzahl je Commit: I01–I16 **40** (39 + 1 injizierte), I17–I32 **39**. Bei I17–I20 bleibt die
Kante `<k>_services → core` erhalten, weil andere Module derselben Komponente `depot.core.ports`
weiterhin importieren; die Injektion entfernt eine **Modul**kante, keine Komponentenkante.

### 8.5 (4e) Zyklen je Injektionscommit

| Commits | Erwartung des Auftrags | Ist (Komponentenebene) | Ist (Modulebene) |
|---|---|---|---|
| I13–I15 | genau 1 Zyklus über genau 2 Komponenten | **je 1**, `<k>_api ↔ <k>_mappers` | je 1, `<k>.api.routes ↔ <k>.mappers.<…>_mapper` |
| I16 | genau 1 Zyklus über genau 2 Komponenten | **1**, `orders_services ↔ orders_services_pricing` | 1, `depot.orders.services ↔ …pricing.engine` |
| I01–I03 | 0 | **je 1** (siehe unten) | je 1 |
| I04–I12, I17–I32 | 0 | **je 0** | je 0 |

Z1 ist bei I13–I16 erfüllt: **genau zwei** Komponenten und **genau zwei** Kanten je Zyklus, und
die Clean-Baseline ist zyklenfrei (0 Zyklen, oben gemessen). Z3 ist erfüllt: die injizierte
Kante ist in jedem der vier Commits die **einzige** Kante ihrer Richtung zwischen dem Paar —
`role_mapper`, `payment_mapper` und `order_line_mapper` importieren `api` nicht, und
`depot.orders.services.pricing` (das Paketmodul) ist importfrei.

**Abweichung zu 4e, benannt statt behoben — I01–I03 tragen einen Komponentenzyklus.** Die drei
`LAYER_BACK_CALL`-Injektionen ergänzen `<k>_repository → <k>_services`, während die Spine-Kante
`<k>_services → <k>_repository` in der Whitelist steht und in der Baseline realisiert ist. Der
Zweierzyklus ist damit **konstruktionsnotwendig**, nicht ein Baufehler:

- Er ist in der Spezifikation **vorregistriert**. Komponentenschnitt §6.2 und Protokoll §4
  Amendment 13.08. (a) führen ihn als **K4-Doppelmeldung**: der einzige
  `acyclic_siblings`-Contract meldet denselben Verstoß ein zweites Mal als Geschwisterzyklus
  `services ↔ repository`. Manifest §5.1 nennt das ausdrücklich „kein False Positive, getrennt
  zu führen".
- Ihn zu vermeiden hieße, entweder die Spine-Kante `services → repository` zu entfernen — sie
  ist der Rückgrat-Bestandteil des Modells — oder die Injektionsrichtung zu ändern, womit das
  Szenario `LAYER_BACK_CALL` seinen Gegenstand verlöre.

Der Auftragstext von 4e („bei allen anderen NULL") ist an dieser Stelle enger als die
Spezifikation, auf die er sich stützt. Gebaut ist nach der Spezifikation; die Zahl ist hier
ausgewiesen, damit sie nicht als unbemerkter Nebeneffekt durchgeht. **Auf Z1/Z3 wirkt das
nicht** — beide Vorschriften gelten laut Protokoll §3 nur für die `CYCLE`-Injektionen.

### 8.6 (4f) Z2′ (ii) je `CYCLE`-Commit

Geprüft im **Komponentengraphen des jeweiligen Injektionscommits**: ist die Quellkomponente S
der Clean-Kante S→T weiterhin der **einzige** Importeur der Zielkomponente T?

| ID | Clean-Kante S→T | Importeure von T im Injektionscommit | Z2′ (ii) |
|---|---|---|---|
| I13 | `identity_api` → `identity_mappers` | `{identity_api}` | ✔ einelementig |
| I14 | `orders_api` → `orders_mappers` | `{orders_api}` | ✔ |
| I15 | `billing_api` → `billing_mappers` | `{billing_api}` | ✔ |
| I16 | `orders_services` → `orders_services_pricing` | `{orders_services}` | ✔ |

**4 von 4 erfüllt.** Z2′ (i) — S sortiert in Code-Unit-Ordnung vor T — ist in
Komponentenschnitt §4.5 und Manifest §1d bereits maschinell nachgewiesen und wird hier nicht
neu gerechnet, sondern übernommen.

### 8.7 (4g) Bauvorschrift I1

Geprüft je Commit: trägt eine der Komponenten `core`, `core_adapters`,
`core_adapters_internal`, `identity_api`, `identity_mappers`, `identity_models`,
`identity_repository`, `identity_services` eine Kante nach `orders_*` oder `billing_*`?

**0 Verstöße in allen 32 Commits** und in der Clean-Baseline.

**Namentlich ausgewiesen, wie der Auftrag verlangt:** **I11** ist eine
`INDEPENDENCE`-Injektion mit der Kante `billing_services → orders_models`. Sie ist **kein**
I1-Fall — `billing_services` steht nicht in der Quellmenge von I1, die nur die geteilten
Komponenten und den gemeinsam genutzten Kontext `identity_*` umfasst (Komponentenschnitt §4.6).
Die Kante ist als `INDEPENDENCE`-Verstoß gewollt und in §8.4 als die eine unerlaubte Kante des
Commits gezählt. Dasselbe gilt für **I10** (`orders_services → billing_services`) und **I12**
(`orders_repository → billing_repository`): beide Quellen liegen außerhalb der I1-Quellmenge.
**Keine der 32 Injektionen legt eine Kante aus einer geteilten oder aus einer
`identity_*`-Komponente in einen der beiden unabhängigen Kontexte.**

### 8.8 (4h) Bauvorschrift K5-1

Die Modulmenge, die `data/soll/test_architecture.py` namentlich nennt — die 19
`COMPONENTS`-Listen der Erlaubnislistenregeln, die vier `PORT_CARRIERS` und `depot.core.ports` —
ist gegen jeden der 32 Commits geprüft: **kein** genanntes Modul ist in einem Commit
verschoben oder entfernt. **0 Befunde in 32 von 32.**

- Die vier `INCORRECT_LOCATION`-Träger und ihre vier Phantom-Zielorte stehen in `K5_1_LOCKED`
  und werden von **keiner** K5-Regel genannt; ihr Umzug in I25–I28 ist damit unschädlich.
- Die vier `MISSING_PORT_REFERENCE`-Träger **werden** von den vier Portregeln genannt — sie
  sind in I17–I20 aber weder verschoben noch entfernt; entfernt wird der **Import**, und
  `depot.core.ports` selbst bleibt in allen 32 Commits bestehen. Genau so vorgesehen
  (Protokoll §3 Amendment (f), Kommentar in `test_architecture.py`).

### 8.9 (4i) Arbeitsverzeichnis

- `git status --porcelain` → **leer** (vor dem Bau, zwischen allen 32 Commits und danach).
- `git rev-parse baseline` → `0d651041ed87dd03f2f78359713633fac01c0a66` — **unverändert**.
- `git rev-parse main` → `0d651041ed87dd03f2f78359713633fac01c0a66` — **unverändert**.
- `README.md` und `.gitignore` stehen in **keinem** der 32 Diffs; kein Commit berührt eine
  andere Datei als seine Zieldatei(en).
- **Nicht gepusht.** `git log origin/main..` ist für den Autor zu erledigen.

---

## 9. Commit-Hygiene

Alle 32 Commit-Messages sind englisch, imperativ, **eine Zeile**, mit Injektions-ID, und der
Body ist **leer**. Vollständige Liste in §2 über die SHAs erreichbar; Beispiele:

```
inject I07: open a session past the adapter facade in the customer service
inject I16: import the orders services package back from the pricing engine
inject I25: move the legacy order index out of the repository package
inject I30: deviate the percent_for signature of the order query
```

- **`Co-Authored-By`: 0.** **`Generated with`: 0.** Keine Signatur, kein Werkzeugname im Body.
- **Autor:** `Timo Haas <haasentimo@gmail.com>` in **32 von 32** — genau ein Autor.
  **Committer:** derselbe, in 32 von 32.
- **Nichtleere Bodies: 0.**

**Die im Auftrag vorgegebene Prüfzeile liefert 0 — misst aber nicht, was sie soll.** Ausgeführt:

```
$ git log --format='%H %s%n%b' inj/01..inj/32 --no-walk | grep -ic "co-authored-by"
0
```

`inj/01..inj/32` ist ein **Bereich**, kein Ref-Paar; mit `--no-walk` bleibt davon **ein**
Commit übrig (`git log --format='%H' inj/01..inj/32 --no-walk | wc -l` → **1**, nämlich
`inj/32`). Die Zeile prüft also einen von 32 Commits. Die tragende Prüfung ist deshalb die
Aufzählungsform, ebenfalls ausgeführt:

```
$ git log --format='%H %s%n%b' --no-walk inj/01 inj/02 … inj/32 | grep -ic "co-authored-by"
0
```

**0 über alle 32.** Kein Commit musste geamendet werden.

---

## 10. Was in der Spezifikation fehlte — und wie es geschlossen ist

Alle Punkte sind aus der Spezifikation heraus entschieden; nichts ist erfunden, kein Werkzeug
lief zur Klärung.

1. **Die tragende Methode der vier `FORBIDDEN_SIGNATURE_TYPE`-Injektionen** war laut Manifest §6
   und Protokoll §3 Nachtrag Rev. 28 ausdrücklich „von C4b zu benennen". Benannt in §3:
   `Customer.reload`, `Order.reload`, `OrderLine.reload`, `Invoice.reload`, je mit
   `sqlalchemy.orm.Session` als Parametertyp. Die **Schreibweise** war ebenfalls offen; sie ist
   durch die Top-Level-Import-Regel (B9+) auf die qualifizierte Form **erzwungen** und nicht
   frei gewählt.
2. **Welche Signatur der vier `SIGNATURE_DEVIATION`-Injektionen wie abweicht** nennt das
   Manifest nicht — nur das Symbol und die Auflage „Builtin oder bereits importiert,
   Importmenge unverändert". Entschieden in §4; die Soll-Signaturen stammen wörtlich aus
   R-SIG-1…4.
3. **Womit der entfernte Porttyp bei I17–I20 zu ersetzen ist,** sagt weder Rezept noch
   Amendment (f). Prüfpunkt 3e (vollständige Typannotation) schließt „ersatzlos" aus, das
   Rezept („Modul bleibt sonst unverändert") schließt einen neuen Import aus. Übrig bleibt ein
   Builtin; gewählt ist `object` (§5).
4. **Wie der injizierte Import zu benutzen ist,** sagt keine Quelle. Gewählt ist das in §2.2
   beschriebene Muster: ein neues, vollständig annotiertes öffentliches Element je Träger. Die
   Randbedingungen daraus — kein gebrochener Aufrufer, keine bewegte Bestandssignatur, ein
   Ein-Datei-Diff — folgen aus §3a des Auftrags und aus Auflage (c) von Rev. 28.
5. **Die Refform** war ausdrücklich freigestellt („Form wählen, im Bericht begründen"). Gewählt
   und begründet in §1.

---

## 11. Widersprüche

1. **4e des Auftrags gegen Komponentenschnitt §6.2 / Protokoll §4 / Manifest §5.1.** 4e verlangt
   „bei allen anderen NULL" Zyklen; die drei `LAYER_BACK_CALL`-Injektionen erzeugen jedoch
   konstruktionsnotwendig einen Komponentenzyklus `<k>_repository ↔ <k>_services`, der in der
   Spezifikation als K4-Doppelmeldung **vorregistriert** ist. Aufgelöst zugunsten der
   Spezifikation, Zahlen ausgewiesen (§8.5). **Nicht** durch einen Werkzeuglauf geklärt.
2. **Die Hygiene-Prüfzeile des Auftrags misst einen statt 32 Commits** (§9). Beide Formen
   ausgeführt, beide liefern 0.
3. **`c1_modulliste.md` §D.6 führt den Laufzeit-Zirkelimport nur für I16.** Er trifft ebenso auf
   I01–I03 zu (§7.1). Keine Änderung an der Modulliste vorgenommen — der Vermerk gehört in eine
   Revision dieser Datei und ist hier zur Übernahme festgehalten.
4. **Der deskriptive Vollbild-Commit aus Protokoll §6 ist nicht gebaut.** Protokoll §6
   (Amendment 12.08.) sieht **einen zusätzlichen Commit mit allen 32 Injektionen** vor, Elternteil
   `baseline`, kein Merge, ausdrücklich nicht gegen das Manifest gejoint und in keiner Metrik.
   Der Auftrag C4b nennt ihn nicht und begrenzt den Bau auf „32 Commits und 32 Refs". Gebaut
   sind daher **32**; der Vollbild-Commit steht **aus** und braucht einen eigenen Auftrag.

Kein weiterer Widerspruch aufgefallen. Insbesondere ist **kein Defekt in der Clean-Baseline**
aufgefallen: 73 Dateien, 39 Komponentenkanten, 0 unerlaubte Kanten, 0 Zyklen, alles
deckungsgleich mit `c1_modulliste.md` §4.

---

## 12. Bestätigungen

- **Kein Werkzeuglauf zur Kontrolle der Findings.** Der Checker, die Rule-Engine, import-linter
  und PyTestArch wurden **nicht** aufgerufen — auch nicht probeweise. Benutzt wurden
  ausschließlich `git`, das Python-Standardmodul `ast` und `python -m compileall` gegen eine
  Wegwerf-Kopie in einem Temporärverzeichnis.
- **Kein Modell-Call.**
- **`baseline` ist unverändert:** `0d651041ed87dd03f2f78359713633fac01c0a66`. **`main` ist
  unverändert.** Beide zeigen weiterhin auf denselben Commit wie vor diesem Auftrag.
- **Kein Push.** Weder Commits noch Tags sind auf `origin` übertragen.
- **Keine Änderung** am Manifest, an `data/soll/**`, am Checker oder an `control_files.txt`.
  Die 32 Injektions-SHAs trägt **C4c** nach.
- `~/ma/tritongraph` wurde **nicht angefasst**.
