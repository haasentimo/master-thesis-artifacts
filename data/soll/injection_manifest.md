# Injektionsmanifest — Erwartungswerte vor dem Bau der Injektionen

**Masterarbeit Timo Haas · HTWG Konstanz · Phase 04 · Schritt C4a**
Stand: 25. August 2026 · Status: **abgeleitet, ungebaut** — die 32 Injektions-Commits existieren
noch nicht.

**Quellen, ausschließlich:** `docs/planung/c1_modulliste.md` Rev. 5 · `docs/planung/c1_komponentenschnitt.md`
Rev. 3 · `docs/protokolle/eval_protokoll_phase04.md` Rev. 28 · `data/soll/architecture-rules.yaml`
· `docs/ddr/checker_entscheidungen_l_m.md` §M/§M.2 · die vier Bauberichte 4b-1…4b-4 (wörtliche
Signaturen). Zur reinen Nachsicht von Modulnamen und Signaturen wurde zusätzlich der Tag
`baseline` (`0d651041ed87dd03f2f78359713633fac01c0a66`) im Testrepo `~/ma/ma-conformance-testrepo`
gelesen (`git show baseline:<pfad>`), **kein Checkout, keine Änderung** — `git status --porcelain`
dort vor und nach dieser Arbeit leer.

**Kein Modell-Call. Kein Aufruf des Checkers, der Rule-Engine, von import-linter oder PyTestArch —
auch nicht probeweise.** Alle Schlüssel unten sind von Hand aus der Spezifikation gebildet.

## Warum der Injektions-SHA hier leer bleibt

`injection_sha256` (in `injection_manifest.json`) ist **absichtlich leer** und wird erst in C4c
gefüllt, nachdem die 32 Injektions-Commits gebaut sind. Grund ist die **Anti-Tautologie-Regel**
aus Decision Record M (`docs/ddr/checker_entscheidungen_l_m.md`, §M): `expected_match_key` muss
von Hand nach der dokumentierten Handregel gebildet werden — wären erwarteter und gemessener Wert
aus derselben Funktion (bzw. am selben Bauzustand) entstanden, entstünde dieselbe Tautologie wie
bei `matchKeyOf` in `validate.ts` (`b1_bericht_matchkey.md` Abschnitt A2), und die `strict`-Zahl
prüfte nichts. Dieses Manifest wird deshalb erzeugt und im Repository committet, **bevor** die
Injektions-Commits existieren: die Unabhängigkeit der Ableitung ist damit durch die Commit-Historie
belegt, nicht nur behauptet. Der Injektions-SHA kommt als zusätzliches, nachträglich ergänztes Feld
in C4c hinzu, ohne dass eine der hier festgehaltenen Erwartungen rückwirkend geändert wird.

## Nachtrag (25.08.2026, Auftrag C4B-0) — zwei offene Punkte aufgelöst, vor dem Bau der Commits

Die beiden in §6 als **OFFEN** geführten Punkte sind **vor dem Bau der 32 Injektions-Commits**
aufgelöst — genau wie das übrige Manifest, ausschließlich aus der Spezifikation
(`docs/protokolle/eval_protokoll_phase04.md` §3 Nachtrag Rev. 28, 25.08.2026), **kein** Modell-
Call, **kein** Werkzeuglauf, **kein** Blick auf einen bestehenden Commit. Die
**Anti-Tautologie-Regel** aus Decision Record M (siehe oben) bleibt damit gewahrt: die Auflösung
liegt zeitlich und sachlich vor jedem gebauten Commit, nicht danach.

- **I16 (`CYCLE_PARENT_CHILD`):** der Widerspruch aus §5.6/dem C4a-Bericht §5.2 ist **zugunsten
  des Rezepts** entschieden — I16 ergänzt den Import des **Paketmoduls**
  `depot.orders.services`, nicht des Submoduls `order_service`. Die zitierte K5-Ausgabe stammte
  aus der C2c-Prüfsonde gegen zehn Baseline-Kopien, nicht aus dieser Injektion. Siehe §5.6.
- **I21–I24 (`FRAMEWORK_TYPE_IN_SIGNATURE`):** der injizierte Typ ist **`sqlalchemy.orm.Session`**.
  Die tragende Methode/Signatur bleibt bis C4b **OFFEN** — „von C4b zu benennen" —, ebenso die
  wörtliche Schreibweise in der Signatur, die `offending_type` bildet. Siehe §6.

Der alte **OFFEN**-Vermerk bleibt an beiden Stellen unten sichtbar stehen, ergänzt statt ersetzt.

## Nachtrag (25.08.2026, Auftrag C4C) — die 32 Injektions-SHA und die Methodennamen

**Die erwarteten Schlüssel sind vor dem Bau der Injektions-Commits abgeleitet.** Dieses Manifest
wurde als Commit `56055de` („feat: derive the injection manifest before the injections exist",
25.08.2026 11:03:51 +02:00) im Repository `masterarbeit` festgeschrieben; die 32 Injektions-Commits
im Testrepo tragen den Zeitstempel 25.08.2026 18:32:22 +02:00. Auch der C4B-0-Nachtrag oben
(`9bd6014`, 18:21:05) liegt **vor** ihnen. Die Unabhängigkeit der Ableitung ist damit durch zwei
Commit-Historien belegt, nicht behauptet — genau das, was die Anti-Tautologie-Regel aus Decision
Record M verlangt.

**Dieser Auftrag trägt ausschließlich nach:**

1. die **32 `injection_sha256`** (§2.1 unten sowie `injection_sha256` je Eintrag in
   [`injection_manifest.json`](injection_manifest.json)), Quelle
   [`data/testrepo/MANIFEST.md`](../testrepo/MANIFEST.md) (Nachtrag 25.08.2026, lokal aus
   `git bundle verify` gelesen und gegen `git ls-remote --tags origin` abgeglichen), in C4c
   zusätzlich Eintrag für Eintrag gegen `git rev-parse inj/NN` gestellt — **32/32 zeichengleich,
   0 Abweichungen**;
2. die **tragende Methode bzw. den tragenden Modulpfad je Injektion**, wörtlich aus
   [`c4b_bericht_injektionen.md`](../../docs/repo-kontext/c4b_bericht_injektionen.md) §3–§6 (§2.2
   unten).

**Kein `expected_match_key` ist geändert** — weder einer der 28 abgeleiteten noch die vier bei
I21–I24 weiterhin **OFFEN** geführten. Maschinell gegengeprüft: die Menge aller
`expected_match_key`-Werte in `injection_manifest.json` ist vor und nach diesem Auftrag
zeichengleich. Änderte sich doch einer, wäre das ein **Befund** und getrennt zu melden.

---

## 1. Ableitungsregeln je Segment des `match_key`

Format (`matchKey.ts:26`): `category|component|module|subjectKey`.

### 1a. `category`

- **K1 (deterministische Rule-Engine).** Für die vier `FORBIDDEN_RELATION`-Szenarien
  (`LAYER_BACK_CALL`, `LAYER_SKIP_CALL`, `PROTECTED_MODULE`, `INDEPENDENCE`) emittiert die
  Engine einheitlich `layer-violation` mit `rule_id = DERIVED:forbidden-edge`
  (`ruleEngine.ts:77`, Protokoll §4 „Geändert vor Freeze", `rule_id` diskriminiert nicht). Für
  `CYCLE` (`CYCLE_SIBLING`, `CYCLE_PARENT_CHILD`) emittiert sie `cycle` mit
  `rule_id = DERIVED:cycle` (`ruleEngine.ts:132`). Die vier übrigen Ebene-1-Kategorien sind auf
  dem K1-Pfad **nicht ausdrückbar** — die Rule-Engine kennt nur diese zwei `DERIVED:`-Werte
  (Protokoll §3 Fußnote 3; Komponentenschnitt §1 V-Tabelle).
- **K2/K3 (LLM-Pfad).** `category` stammt aus `rule.category` der Regeldatei
  (`llmChecker.ts:288`) — eine der sechs Ebene-1-Kategorien aus `architecture-rules.yaml`,
  zeichengleich mit der Kodierung in Protokoll §3 (validiert dort unter (3c)).
- **K4/K5.** Keine `match_key`-Bildung; die Baselines kennen den Schlüssel nicht (Protokoll §4
  „Baselines (K4/K5)"). Statt eines Schlüssels führt dieses Manifest je Injektion die
  **Matchregel** aus §4/§6 des Protokolls (Kantenmenge bei `acyclic_siblings`, Regelname bei den
  Erlaubnislistenregeln).

### 1b. `component` und `module`

Aus `docs/planung/c1_modulliste.md` §1/§2 (Rev. 5) — Trägerspalte „erwarteter Träger des
Findings" bzw. `Komponente`-Spalte. Für die vier `INCORRECT_LOCATION`-Injektionen gilt die
**Phantom-Erbregel**: der Zielort erbt die Komponente seines sauberen Ursprungsorts
(`c1_modulliste.md` §D.1, Protokoll §2 Nachtrag Rev. 14 (a)); `component` und `module` sind dann
die des **Zielorts** (Phantom), nicht des Herkunftsorts.

### 1c. `subjectKey`

Nach den bindenden Schreibweisen aus Protokoll §3 Nachtrag Rev. 18/19 und Decision Record L/P:

| Kategorie | Form | Schreibweise |
|---|---|---|
| `FORBIDDEN_RELATION`, `CYCLE` | Kantenpaar `from->to` | Komponentennamen, `subject.from`/`subject.to` |
| `ABSENCE_REQUIRED` | `offending_type` | Porttyp voll qualifiziert, Schreibweise des `statement` (z. B. `depot.core.ports.TokenSigner`) |
| `FORBIDDEN_SIGNATURE_TYPE` | `offending_type` | Framework-Typname, verbatim wie in der Signatur |
| `STRUCTURAL_PLACEMENT` | `offending_type` | volle Punktkette des fehlplatzierten Moduls |
| `API_CONTRACT` | `offending_type` | Symbolname als `Class.method`, bei Top-Level-Funktion der bloße Name |

### 1d. Handregel für die vier `CYCLE`-Injektionen (§M/§M.2)

Für ein Paar mit Clean-Kante S→T und injizierter Kante T→S gilt: ist **(i)** S in
Code-Unit-Ordnung vor T sortiert **und (ii)** S im Komponentengraphen des Injektionscommits der
**einzige** Importeur von T (Z2′, Komponentenschnitt §2.2, bewiesen §2.3), dann trägt der Record
die injizierte Kante T→S, `location.component = T`, `location.module` = importierender Modul in
T = der Injektionsträger. Die Ordnung jedes Paares ist unten **maschinell** nachgerechnet — nicht
neu gemessen, sondern **wiederverwendet** aus dem bereits eingefrorenen Prüfskript in
`c1_modulliste.md` §3 (dort für Rev. 3 ausgeführt und committet, vor diesem Auftrag):

| Paar | S | T | S<T? | Beleg |
|---|---|---|---|---|
| `CYCLE_SIBLING` 1 (I13) | `identity_api` | `identity_mappers` | ✓ | Pos 9: `a`(0x61) < `m`(0x6D) |
| `CYCLE_SIBLING` 2 (I14) | `orders_api` | `orders_mappers` | ✓ | Pos 7: `a` < `m` |
| `CYCLE_SIBLING` 3 (I15) | `billing_api` | `billing_mappers` | ✓ | Pos 8: `a` < `m` |
| `CYCLE_PARENT_CHILD` (I16) | `orders_services` | `orders_services_pricing` | ✓ | Präfix, S um 8 Zeichen kürzer |

Für alle vier Paare ist die Kandidatenmenge **einelementig** (Bedingung (ii) — S ist alleiniger
Importeur von T, per Bauvorschrift/Whitelist erzwungen, Komponentenschnitt §4.1/§4.4) — es gibt
keinen zweiten Kandidaten einzutragen.

---

## 2. Manifest-Tabelle

Alle Angaben je Injektion — sortiert nach ID, lückenlos I01–I32. `match_key` und Matchregeln
stehen, sofern nicht trivial, in den Detailblöcken §3–§5. Maschinenlesbare Fassung:
[`injection_manifest.json`](injection_manifest.json).

| ID | Szenario (Ebene 2) | Kategorie (Ebene 1) | Trägermodul | Komponente | Methode/Signatur | `rule_id` | Kantengrenze |
|---|---|---|---|---|---|---|---|
| I01 | LAYER_BACK_CALL | FORBIDDEN_RELATION | `depot.identity.repository.customer_repo` | identity_repository | — | R-LAYER-1 | identity_repository → identity_services |
| I02 | LAYER_BACK_CALL | FORBIDDEN_RELATION | `depot.orders.repository.order_repo` | orders_repository | — | R-LAYER-1 | orders_repository → orders_services |
| I03 | LAYER_BACK_CALL | FORBIDDEN_RELATION | `depot.billing.repository.invoice_repo` | billing_repository | — | R-LAYER-1 | billing_repository → billing_services |
| I04 | LAYER_SKIP_CALL | FORBIDDEN_RELATION | `depot.identity.api.routes` | identity_api | — | R-LAYER-1 | identity_api → identity_repository |
| I05 | LAYER_SKIP_CALL | FORBIDDEN_RELATION | `depot.orders.api.routes` | orders_api | — | R-LAYER-1 | orders_api → orders_repository |
| I06 | LAYER_SKIP_CALL | FORBIDDEN_RELATION | `depot.billing.api.routes` | billing_api | — | R-LAYER-1 | billing_api → billing_repository |
| I07 | PROTECTED_MODULE | FORBIDDEN_RELATION | `depot.identity.services.customer_service` | identity_services | — | R-PROTECT-1 | identity_services → core_adapters_internal |
| I08 | PROTECTED_MODULE | FORBIDDEN_RELATION | `depot.orders.services.order_service` | orders_services | — | R-PROTECT-1 | orders_services → core_adapters_internal |
| I09 | PROTECTED_MODULE | FORBIDDEN_RELATION | `depot.billing.services.invoice_service` | billing_services | — | R-PROTECT-1 | billing_services → core_adapters_internal |
| I10 | INDEPENDENCE | FORBIDDEN_RELATION | `depot.orders.services.checkout_service` | orders_services | — | R-INDEP-1 | orders_services → billing_services |
| I11 | INDEPENDENCE | FORBIDDEN_RELATION | `depot.billing.services.dunning_service` | billing_services | — | R-INDEP-1 | billing_services → orders_models |
| I12 | INDEPENDENCE | FORBIDDEN_RELATION | `depot.orders.repository.order_line_repo` | orders_repository | — | R-INDEP-1 | orders_repository → billing_repository |
| I13 | CYCLE_SIBLING | CYCLE | `depot.identity.mappers.customer_mapper` | identity_mappers | — | R-CYCLE-1 | identity_mappers → identity_api (injiziert) |
| I14 | CYCLE_SIBLING | CYCLE | `depot.orders.mappers.order_mapper` | orders_mappers | — | R-CYCLE-1 | orders_mappers → orders_api (injiziert) |
| I15 | CYCLE_SIBLING | CYCLE | `depot.billing.mappers.invoice_mapper` | billing_mappers | — | R-CYCLE-1 | billing_mappers → billing_api (injiziert) |
| I16 | CYCLE_PARENT_CHILD | CYCLE | `depot.orders.services.pricing.engine` | orders_services_pricing | — | R-CYCLE-2 | orders_services_pricing → orders_services (injiziert) |
| I17 | MISSING_PORT_REFERENCE | ABSENCE_REQUIRED | `depot.identity.services.token_service` | identity_services | `TokenService.issue` | R-PORT-1 | keine Kante — semantisch |
| I18 | MISSING_PORT_REFERENCE | ABSENCE_REQUIRED | `depot.orders.services.catalog_service` | orders_services | `CatalogService.quote_cents` | R-PORT-2 | keine Kante — semantisch |
| I19 | MISSING_PORT_REFERENCE | ABSENCE_REQUIRED | `depot.orders.services.refund_service` | orders_services | `RefundService.refund` | R-PORT-3 | keine Kante — semantisch |
| I20 | MISSING_PORT_REFERENCE | ABSENCE_REQUIRED | `depot.billing.services.ledger_service` | billing_services | `LedgerService.post_invoice` | R-PORT-4 | keine Kante — semantisch |
| I21 | FRAMEWORK_TYPE_IN_SIGNATURE | FORBIDDEN_SIGNATURE_TYPE | `depot.identity.models.customer_models` | identity_models | ~~Typ `sqlalchemy.orm.Session` festgelegt, Methode **OFFEN** (§6)~~ `Customer.reload`, `def reload(self, session: sqlalchemy.orm.Session) -> None:` (C4c, §2.2) | R-FRAMEWORK-1 | keine Kante — Import bleibt erlaubt |
| I22 | FRAMEWORK_TYPE_IN_SIGNATURE | FORBIDDEN_SIGNATURE_TYPE | `depot.orders.models.order_models` | orders_models | ~~Typ `sqlalchemy.orm.Session` festgelegt, Methode **OFFEN** (§6)~~ `Order.reload`, `def reload(self, session: sqlalchemy.orm.Session) -> None:` (C4c, §2.2) | R-FRAMEWORK-1 | keine Kante — Import bleibt erlaubt |
| I23 | FRAMEWORK_TYPE_IN_SIGNATURE | FORBIDDEN_SIGNATURE_TYPE | `depot.orders.models.order_line_models` | orders_models | ~~Typ `sqlalchemy.orm.Session` festgelegt, Methode **OFFEN** (§6)~~ `OrderLine.reload`, `def reload(self, session: sqlalchemy.orm.Session) -> None:` (C4c, §2.2) | R-FRAMEWORK-1 | keine Kante — Import bleibt erlaubt |
| I24 | FRAMEWORK_TYPE_IN_SIGNATURE | FORBIDDEN_SIGNATURE_TYPE | `depot.billing.models.invoice_models` | billing_models | ~~Typ `sqlalchemy.orm.Session` festgelegt, Methode **OFFEN** (§6)~~ `Invoice.reload`, `def reload(self, session: sqlalchemy.orm.Session) -> None:` (C4c, §2.2) | R-FRAMEWORK-1 | keine Kante — Import bleibt erlaubt |
| I25 | INCORRECT_LOCATION | STRUCTURAL_PLACEMENT | `depot.orders.legacy_order_index` (Herkunft: `…repository.legacy_order_index`) | orders_repository | — | R-PLACE-1 (Klausel 1) | keine Kante — Platzierung |
| I26 | INCORRECT_LOCATION | STRUCTURAL_PLACEMENT | `depot.billing.legacy_invoice_index` (Herkunft: `…repository.legacy_invoice_index`) | billing_repository | — | R-PLACE-1 (Klausel 1) | keine Kante — Platzierung |
| I27 | INCORRECT_LOCATION | STRUCTURAL_PLACEMENT | `depot.identity.legacy_token_index` (Herkunft: `…repository.legacy_token_index`) | identity_repository | — | R-PLACE-1 (Klausel 1) | keine Kante — Platzierung |
| I28 | INCORRECT_LOCATION | STRUCTURAL_PLACEMENT | `depot.billing.legacy_tax_models` (Herkunft: `…models.legacy_tax_models`) | billing_models | — | R-PLACE-1 (Klausel 2) | keine Kante — Platzierung |
| I29 | SIGNATURE_DEVIATION | API_CONTRACT | `depot.identity.repository.session_repo` | identity_repository | `SessionRepository.touch` | R-SIG-1 | keine Kante |
| I30 | SIGNATURE_DEVIATION | API_CONTRACT | `depot.orders.repository.order_query` | orders_repository | `OrderQuery.percent_for` | R-SIG-2 | keine Kante |
| I31 | SIGNATURE_DEVIATION | API_CONTRACT | `depot.billing.repository.invoice_query` | billing_repository | `InvoiceQuery.settled_cents` | R-SIG-3 | keine Kante |
| I32 | SIGNATURE_DEVIATION | API_CONTRACT | `depot.orders.mappers.order_line_mapper` | orders_mappers | `to_payload` | R-SIG-4 | keine Kante |

Die vier `INCORRECT_LOCATION`-Zielorte sind je **direktes Kind** ihres Kontextpakets:
`depot.orders.legacy_order_index` < `depot.orders`, `depot.billing.legacy_invoice_index` <
`depot.billing`, `depot.identity.legacy_token_index` < `depot.identity`,
`depot.billing.legacy_tax_models` < `depot.billing`.

---

## 2.1 `injection_sha256` je Injektion (nachgetragen in C4c, 25.08.2026)

Quelle: [`data/testrepo/MANIFEST.md`](../testrepo/MANIFEST.md), Nachtrag 25.08.2026, Tabelle
„Die 32 Injektions-Commits" — dort lokal aus `git bundle verify` gelesen und gegen
`git ls-remote --tags origin` abgeglichen. **Gegenprobe in C4c:** je Eintrag `git rev-parse inj/NN`
im Testrepo (rein lesend, kein Checkout) gegen den Manifestwert gestellt — **32 von 32
zeichengleich, 0 Abweichungen** (Beleg: `c4c_bericht_vorabpruefung.md` §A1).

Der Tagname ist **nicht** der Anker, der SHA ist es: die Push-Rechte auf `origin` umfassen das
Löschen von Tags (`b20_bericht_push_rechte.md`).

| ID | Ref | `injection_sha256` |
|---|---|---|
| I01 | `inj/01` | `439125ece20060321bff983d7b8295f1b33dda50` |
| I02 | `inj/02` | `4165fab5c82b1194572461fdb232c1af264e66f5` |
| I03 | `inj/03` | `b3fb12905f7f3becc803d1915af5654da35643bb` |
| I04 | `inj/04` | `3de8357bc191821fe60922022be257c47959d35d` |
| I05 | `inj/05` | `dbcd05b8935ac3d007464f2e0d72c08ef0a9931e` |
| I06 | `inj/06` | `531a1ff2616aaa13f8c317fe7d40f56135caacaf` |
| I07 | `inj/07` | `0993e01b26b7cc91bb70840207860fcc15dba286` |
| I08 | `inj/08` | `792cb6867f55634bc3f8bfac321b392ea5507a48` |
| I09 | `inj/09` | `06e052e19c153503f751611d7f813f18f204d8f0` |
| I10 | `inj/10` | `e1829642b304a016d0b2f11087c2b215f8368942` |
| I11 | `inj/11` | `5601a944ea1da65b1e2b03c5e74a8237336a2e85` |
| I12 | `inj/12` | `cb1fb228ff6021071a8c6b2a88506a80f138eafb` |
| I13 | `inj/13` | `3be646fed3bdb2449b153f912d42fbb63b719776` |
| I14 | `inj/14` | `a9d644515812b98877af4e63e0f9a3f119ee7e88` |
| I15 | `inj/15` | `616cb02982e634670c4dbaa84d5efbf4df63c61a` |
| I16 | `inj/16` | `43f9fa5ec1b6fbf4aaae26296a41b752c2e3f9cf` |
| I17 | `inj/17` | `c5faa0a65f0a85e9bb1a1ecac950806650449ec1` |
| I18 | `inj/18` | `ad210637f542736323c4d2f5da4254c4c4e60bad` |
| I19 | `inj/19` | `864da9678e6a10137a2fd2d4b1a7d73082db403f` |
| I20 | `inj/20` | `35061d852631049ff74f65451368d7e85fd733bd` |
| I21 | `inj/21` | `dd414657d12197a1ca79152d401f75eb4b5f5f57` |
| I22 | `inj/22` | `08a622b024e9174d7ce62863f385b369c8c27b12` |
| I23 | `inj/23` | `28a75749496229bb1db37d85f68347572bd84c49` |
| I24 | `inj/24` | `91ed6a80d415c68eed7661a21ea554ba32da9c83` |
| I25 | `inj/25` | `ef114806ec2360f19eb9dc9425d79ed153b9a769` |
| I26 | `inj/26` | `efe5c81f526d183fcb6634e65df00e7f90b0dbc3` |
| I27 | `inj/27` | `33ad86a07dd626c59541c91334d33f3e1e76bc04` |
| I28 | `inj/28` | `72dc7461f9ecb5cdd53293f1f94d7418e98a3401` |
| I29 | `inj/29` | `5e685cff9559cfbff8935162405cd98c5c10932e` |
| I30 | `inj/30` | `604d30460ce9a602b7b635f8f6de08c113acf9bf` |
| I31 | `inj/31` | `3d3374571153656f012a15d01df7f5e8dcb88c8e` |
| I32 | `inj/32` | `307e57327a81d94dea84614d9fc9d8d82b839f97` |

`--base` ist für **jeden** dieser Stände derselbe Baseline-SHA
`0d651041ed87dd03f2f78359713633fac01c0a66` (Sternform, Protokoll §6 Amendment 12.08.2026).

---

## 2.2 Die tragende Methode bzw. der tragende Modulpfad je Injektion (C4b, nachgetragen in C4c)

Wörtlich aus [`c4b_bericht_injektionen.md`](../../docs/repo-kontext/c4b_bericht_injektionen.md)
§3–§6. **Singular-Regel** (Protokoll §3 Nachtrag Rev. 17/Rev. 22): je Träger genau ein Vorkommen.

### `ABSENCE_REQUIRED` — I17–I20 (C4b §5)

Entfernt wurden Annotation **und** Import (Protokoll §3 Amendment (f)); `object` statt ersatzlos,
weil Prüfpunkt 3e die vollständige Typannotation verlangt.

| ID | Methode | Annotation vorher | Annotation nachher | `offending_type` (= `subjectKey`) |
|---|---|---|---|---|
| I17 | `TokenService.issue` | `signer: depot.core.ports.TokenSigner` | `signer: object` | `depot.core.ports.TokenSigner` |
| I18 | `CatalogService.quote_cents` | `rates: depot.core.ports.RateProvider` | `rates: object` | `depot.core.ports.RateProvider` |
| I19 | `RefundService.refund` | `gateway: depot.core.ports.PaymentGateway` | `gateway: object` | `depot.core.ports.PaymentGateway` |
| I20 | `LedgerService.post_invoice` | `clock: depot.core.ports.Clock` | `clock: object` | `depot.core.ports.Clock` |

### `FORBIDDEN_SIGNATURE_TYPE` — I21–I24 (C4b §3)

| ID | Träger | Klasse | Methode | Signatur **wörtlich aus dem Code** | `offending_type` **wörtlich** |
|---|---|---|---|---|---|
| I21 | `depot.identity.models.customer_models` | `Customer` | `Customer.reload` | `def reload(self, session: sqlalchemy.orm.Session) -> None:` | `sqlalchemy.orm.Session` |
| I22 | `depot.orders.models.order_models` | `Order` | `Order.reload` | `def reload(self, session: sqlalchemy.orm.Session) -> None:` | `sqlalchemy.orm.Session` |
| I23 | `depot.orders.models.order_line_models` | `OrderLine` | `OrderLine.reload` | `def reload(self, session: sqlalchemy.orm.Session) -> None:` | `sqlalchemy.orm.Session` |
| I24 | `depot.billing.models.invoice_models` | `Invoice` | `Invoice.reload` | `def reload(self, session: sqlalchemy.orm.Session) -> None:` | `sqlalchemy.orm.Session` |

**Die qualifizierte Schreibweise `sqlalchemy.orm.Session` ist ERZWUNGEN, nicht gewählt.** Die
Bauvorschrift lässt nur `import pkg.modul` zu, nie `from pkg import modul` (B9+, Protokoll §3
Amendment (c)); die unqualifizierte Form `Session` wäre ohne `from sqlalchemy.orm import Session`
ein `NameError`, und genau dieser Import ist verboten. Es gibt an dieser Stelle also keine
Stilentscheidung, die anders hätte ausfallen können — das ist beim Lesen von §1c mitzudenken, wo
`offending_type` „verbatim wie in der Signatur" verlangt wird.

Der Rumpf ist je `session.refresh(self)`; `reload` ist **neu**, keine bestehende Signatur ist
verändert (Auflage (c)), und `import sqlalchemy.orm` stand bereits in allen vier Trägern
(Auflage (b), Importmenge unverändert und weiterhin zeichengleich mit der des Zwillings).

### `STRUCTURAL_PLACEMENT` — I25–I28 (C4b §6)

Reiner `git mv`, **Inhalt unverändert** (Blob-Hashes identisch, `R100`); nach dem Umzug 0
ausgehende Importe und 0 eingehende Referenzen (Abnahmebedingung 8).

| ID | Modulpfad vorher | Modulpfad nachher (= Phantom-Zielort) | Klausel |
|---|---|---|---|
| I25 | `src/depot/orders/repository/legacy_order_index.py` | `src/depot/orders/legacy_order_index.py` | R-PLACE-1 Klausel 1 (`_index`) |
| I26 | `src/depot/billing/repository/legacy_invoice_index.py` | `src/depot/billing/legacy_invoice_index.py` | R-PLACE-1 Klausel 1 (`_index`) |
| I27 | `src/depot/identity/repository/legacy_token_index.py` | `src/depot/identity/legacy_token_index.py` | R-PLACE-1 Klausel 1 (`_index`) |
| I28 | `src/depot/billing/models/legacy_tax_models.py` | `src/depot/billing/legacy_tax_models.py` | R-PLACE-1 Klausel 2 (`_models`) |

### `API_CONTRACT` — I29–I32 (C4b §4)

`offending_type` ist der Symbolname als `Class.method` (Protokoll §3 Nachtrag Rev. 18); bei der
Top-Level-Funktion `to_payload` der bloße Name.

| ID | Symbol (= `subjectKey`) | Signatur vorher (= Soll, R-SIG-n) | Signatur nachher | Abweichung |
|---|---|---|---|---|
| I29 | `SessionRepository.touch` | `def touch(self, session_id: str, ttl_seconds: int) -> bool:` | `def touch(self, session_id: str, ttl_seconds: float) -> bool:` | Parametertyp `int` → `float` |
| I30 | `OrderQuery.percent_for` | `def percent_for(self, code: str, subtotal_cents: int) -> int:` | `def percent_for(self, code: str, subtotal_cents: int) -> float:` | Rückgabetyp `int` → `float` |
| I31 | `InvoiceQuery.settled_cents` | `def settled_cents(self, invoice_number: str) -> int:` | `def settled_cents(self, invoice_number: str) -> float:` | Rückgabetyp `int` → `float` |
| I32 | `to_payload` | `def to_payload(line: depot.orders.models.order_line_models.OrderLine) -> dict[str, object]:` | `def to_payload(line: depot.orders.models.order_line_models.OrderLine) -> dict[str, str]:` | Rückgabetyp `dict[str, object]` → `dict[str, str]` |

Zu I32: die Signatur ist in der Datei über drei Zeilen umbrochen (black) und trägt dort ein Magic
Trailing Comma; oben — wie in `architecture-rules.yaml` — auf **einer** logischen Zeile **ohne**
dieses Komma wiedergegeben, Tokenfolge im Übrigen identisch. Geändert wurde ausschließlich die
Zeile `) -> dict[str, object]:` → `) -> dict[str, str]:`.

**Kein Import kommt in I29–I32 hinzu und keiner fällt weg** (`int`, `float`, `bool`, `str`, `dict`,
`object` sind Builtins) — die Bauvorschrift (h), auf der die Zeilen K4 = K5 = `nein` in §5.9 ruhen.

---

## 3. `expected_match_key` je Pfad, an dem die Erwartungsmatrix einen Treffer vorhersagt

Nur Pfade mit vorhergesagtem `ja`/`teilweise` in Protokoll §3 tragen einen `match_key`; `nein`
und die auf dem jeweiligen Pfad nicht ausdrückbaren Kategorien bleiben ohne Eintrag (K4/K5 haben
grundsätzlich keinen `match_key`, siehe §4/§5).

| ID | K1 (`match_key`) | K2/K3 (`match_key`) |
|---|---|---|
| I01 | `layer-violation\|identity_repository\|depot.identity.repository.customer_repo\|identity_repository->identity_services` | `FORBIDDEN_RELATION\|identity_repository\|depot.identity.repository.customer_repo\|identity_repository->identity_services` |
| I02 | `layer-violation\|orders_repository\|depot.orders.repository.order_repo\|orders_repository->orders_services` | `FORBIDDEN_RELATION\|orders_repository\|depot.orders.repository.order_repo\|orders_repository->orders_services` |
| I03 | `layer-violation\|billing_repository\|depot.billing.repository.invoice_repo\|billing_repository->billing_services` | `FORBIDDEN_RELATION\|billing_repository\|depot.billing.repository.invoice_repo\|billing_repository->billing_services` |
| I04 | `layer-violation\|identity_api\|depot.identity.api.routes\|identity_api->identity_repository` | `FORBIDDEN_RELATION\|identity_api\|depot.identity.api.routes\|identity_api->identity_repository` |
| I05 | `layer-violation\|orders_api\|depot.orders.api.routes\|orders_api->orders_repository` | `FORBIDDEN_RELATION\|orders_api\|depot.orders.api.routes\|orders_api->orders_repository` |
| I06 | `layer-violation\|billing_api\|depot.billing.api.routes\|billing_api->billing_repository` | `FORBIDDEN_RELATION\|billing_api\|depot.billing.api.routes\|billing_api->billing_repository` |
| I07 | `layer-violation\|identity_services\|depot.identity.services.customer_service\|identity_services->core_adapters_internal` | `FORBIDDEN_RELATION\|identity_services\|depot.identity.services.customer_service\|identity_services->core_adapters_internal` |
| I08 | `layer-violation\|orders_services\|depot.orders.services.order_service\|orders_services->core_adapters_internal` | `FORBIDDEN_RELATION\|orders_services\|depot.orders.services.order_service\|orders_services->core_adapters_internal` |
| I09 | `layer-violation\|billing_services\|depot.billing.services.invoice_service\|billing_services->core_adapters_internal` | `FORBIDDEN_RELATION\|billing_services\|depot.billing.services.invoice_service\|billing_services->core_adapters_internal` |
| I10 | `layer-violation\|orders_services\|depot.orders.services.checkout_service\|orders_services->billing_services` | `FORBIDDEN_RELATION\|orders_services\|depot.orders.services.checkout_service\|orders_services->billing_services` |
| I11 | `layer-violation\|billing_services\|depot.billing.services.dunning_service\|billing_services->orders_models` | `FORBIDDEN_RELATION\|billing_services\|depot.billing.services.dunning_service\|billing_services->orders_models` |
| I12 | `layer-violation\|orders_repository\|depot.orders.repository.order_line_repo\|orders_repository->billing_repository` | `FORBIDDEN_RELATION\|orders_repository\|depot.orders.repository.order_line_repo\|orders_repository->billing_repository` |
| I13 | `cycle\|identity_mappers\|depot.identity.mappers.customer_mapper\|identity_mappers->identity_api` | — (K2/K3 = nein², konstruktionsbedingt) |
| I14 | `cycle\|orders_mappers\|depot.orders.mappers.order_mapper\|orders_mappers->orders_api` | — (nein²) |
| I15 | `cycle\|billing_mappers\|depot.billing.mappers.invoice_mapper\|billing_mappers->billing_api` | — (nein²) |
| I16 | `cycle\|orders_services_pricing\|depot.orders.services.pricing.engine\|orders_services_pricing->orders_services` | — (nein²) |
| I17 | — (K1 = nein³, strukturell nicht ausdrückbar) | `ABSENCE_REQUIRED\|identity_services\|depot.identity.services.token_service\|depot.core.ports.TokenSigner` |
| I18 | — (nein³) | `ABSENCE_REQUIRED\|orders_services\|depot.orders.services.catalog_service\|depot.core.ports.RateProvider` |
| I19 | — (nein³) | `ABSENCE_REQUIRED\|orders_services\|depot.orders.services.refund_service\|depot.core.ports.PaymentGateway` |
| I20 | — (nein³) | `ABSENCE_REQUIRED\|billing_services\|depot.billing.services.ledger_service\|depot.core.ports.Clock` |
| I21 | — (K1 nein) | ~~**OFFEN** — `offending_type` (Framework-Typname) erst in C4b entschieden, §6~~ ~~Typ `sqlalchemy.orm.Session` (25.08.2026); wörtliche Schreibweise und Methode bleiben **OFFEN**, §6~~ ~~Typ, Schreibweise und Methode liegen seit C4b vor (§2.2); die **Bildung des Schlüssels bleibt OFFEN** — sie fällt nicht unter C4c, siehe §6~~ `FORBIDDEN_SIGNATURE_TYPE\|identity_models\|depot.identity.models.customer_models\|sqlalchemy.orm.Session` (eingetragen 26.08.2026, Auftrag D1 — Vermerk unter dieser Tabelle) |
| I22 | — | ~~**OFFEN**, §6~~ ~~wie I21 (Methode `Order.reload`, §2.2); Schlüsselbildung weiterhin OFFEN, §6~~ `FORBIDDEN_SIGNATURE_TYPE\|orders_models\|depot.orders.models.order_models\|sqlalchemy.orm.Session` (26.08.2026, D1) |
| I23 | — | ~~**OFFEN**, §6~~ ~~wie I21 (Methode `OrderLine.reload`, §2.2); Schlüsselbildung weiterhin OFFEN, §6~~ `FORBIDDEN_SIGNATURE_TYPE\|orders_models\|depot.orders.models.order_line_models\|sqlalchemy.orm.Session` (26.08.2026, D1) |
| I24 | — | ~~**OFFEN**, §6~~ ~~wie I21 (Methode `Invoice.reload`, §2.2); Schlüsselbildung weiterhin OFFEN, §6~~ `FORBIDDEN_SIGNATURE_TYPE\|billing_models\|depot.billing.models.invoice_models\|sqlalchemy.orm.Session` (26.08.2026, D1) |
| I25 | — (K1 nein) | `STRUCTURAL_PLACEMENT\|orders_repository\|depot.orders.legacy_order_index\|depot.orders.legacy_order_index` |
| I26 | — | `STRUCTURAL_PLACEMENT\|billing_repository\|depot.billing.legacy_invoice_index\|depot.billing.legacy_invoice_index` |
| I27 | — | `STRUCTURAL_PLACEMENT\|identity_repository\|depot.identity.legacy_token_index\|depot.identity.legacy_token_index` |
| I28 | — | `STRUCTURAL_PLACEMENT\|billing_models\|depot.billing.legacy_tax_models\|depot.billing.legacy_tax_models` |
| I29 | — (K1 nein, strukturell) | `API_CONTRACT\|identity_repository\|depot.identity.repository.session_repo\|SessionRepository.touch` |
| I30 | — | `API_CONTRACT\|orders_repository\|depot.orders.repository.order_query\|OrderQuery.percent_for` |
| I31 | — | `API_CONTRACT\|billing_repository\|depot.billing.repository.invoice_query\|InvoiceQuery.settled_cents` |
| I32 | — | `API_CONTRACT\|orders_mappers\|depot.orders.mappers.order_line_mapper\|to_payload` |

### Ableitungsvermerk zum K2/K3-`match_key` von I21–I24 (eingetragen 26.08.2026, Auftrag D1)

Der Schlüssel ist **nicht abgetippt**, sondern maschinell aus den Feldern dieses Manifests und aus
dem Soll gebildet: Segment 1 `category_l1`, Segment 2 die Komponente des `carrier_module`,
aufgelöst über [`depot_soll.ilograph.yaml`](depot_soll.ilograph.yaml) mit derselben
Modul→Komponente-Abbildung wie `load_soll` in
[`tools/evaluate_control_run.py`](../../tools/evaluate_control_run.py), Segment 3 `carrier_module`,
Segment 4 `offending_type_verbatim_c4b`. Trennzeichen `|` und Segmentreihenfolge sind an
`matchKey.ts:26` verifiziert (`[category, location.component ?? '', location.module,
subjectKey].join('|')`), nicht aus dem Auftrag übernommen. Die vier gebildeten Zeichenketten sind
**zeichengleich (4 von 4, 0 Abweichungen)** mit den in
[`c4c_bericht_vorabpruefung.md`](../../docs/repo-kontext/c4c_bericht_vorabpruefung.md) §A2 als
Beobachtung ausgewiesenen.

Jedes Glied der Kette mit Datum und Fundstelle:

| Glied | Datum | Beleg |
|---|---|---|
| `R-FRAMEWORK-1` im Wortlaut, gehashter Messeingang | 23.08.2026 | [`architecture-rules.yaml`](architecture-rules.yaml), [`SHA256SUMS`](SHA256SUMS), C2a |
| Schreibweise des vierten Segments: „die im Prompt wörtlich vorkommende Form" | 23.08.2026 | Protokoll §3 Nachtrag Rev. 18 |
| Typwahl `sqlalchemy.orm.Session` als kanonischer Typ des Regelbeispiels | 25.08.2026 | Protokoll §3 Nachtrag Rev. 28 |
| Qualifizierte Schreibweise **erzwungen, nicht gewählt**: V12 verbietet `from … import`, unqualifiziert wäre `NameError` | 25.08.2026 | `c4c_bericht_vorabpruefung.md` §A2 |
| Trägermethode `<Klasse>.reload` je Modul | 25.08.2026 | `c4b_bericht_injektionen.md` §3–§6, in C4c übernommen |
| Eintrag dieses Schlüssels | 26.08.2026 | dieser Commit |

**Offenlegung, ohne Beschönigung.** Der K2-Kontrolllauf vom 24.08.2026 hat `R-FRAMEWORK-1`
**63-mal** gesehen, davon **neun Findings auf Dateien, deren gerenderter Prompt `sqlalchemy` an
keiner Stelle enthält** (`c3b_k2_nachtrag_findingbezug.md` §B5) — die Schreibpräferenz des Modells
für genau diesen Typ und genau diese qualifizierte Schreibweise ist also **bekannt**, und der
Verdacht, der Erwartungswert sei auf das Modellverhalten hin gewählt, liegt nahe genug, um ihn hier
auszusprechen statt zu übergehen. Der Anker dagegen ist die **Regeldatei vom 23.08.2026**, die
**vor** diesem Kontrolllauf gehasht wurde (`SHA256SUMS`, C2a): Typ, Schreibweise und
Segmentordnung folgen aus ihr und aus `matchKey.ts:26`, nicht aus der Beobachtung vom 24.08. Der
Zeitstempel dieses Commits ist der Beleg der Anti-Tautologie-Regel aus Decision Record M — er liegt
**vor** dem ersten K2/K3-Lauf der Kampagne.

Die früheren **OFFEN**-Vermerke zu I21–I24 bleiben in der Tabelle oben, in §2 und in §6 sichtbar
durchgestrichen stehen — **ergänzt statt ersetzt**, dieselbe Praxis wie bei C4B-0 und C4c. In der
JSON-Fassung tragen sie die Felder `expected_match_key_k2_k3_open_superseded_2026_08_26` und
`expected_match_key_k2_k3_entered_2026_08_26`.

---

## 4. `expected_co_findings`

- **I01–I12 (`FORBIDDEN_RELATION`): leer, konstruktionsbedingt.** `--rule-graph diff` +
  `changed_files_count == 1` bedeutet: alle beobachteten Importe stammen aus einem Modul, die
  Adjazenz hat genau einen Knoten, `childState === VISITING` (`ruleEngine.ts:120`) kann nie
  eintreten — ein Ein-Datei-Diff kann keinen `cycle`-Record erzeugen (Protokoll §4 Amendment
  13.08. (b)). Keine dieser zwölf Zeilen trägt einen K1-Begleitfund.
- **I13–I16 (`CYCLE`): je ein Eintrag**, gebildet als reine Zeichenkettenoperation auf dem
  handabgeleiteten `expected_match_key` (Präfix `cycle|` → `layer-violation|`, `rule_id =
  DERIVED:forbidden-edge`, `location`/`subject` unverändert) — DDR M.2 Festlegung 1(e). Gültig
  unter Z2 (Ziel sortiert vor Quelle, hier für alle vier Paare erfüllt, siehe §1d):

| ID | `expected_co_findings[0].match_key` |
|---|---|
| I13 | `layer-violation\|identity_mappers\|depot.identity.mappers.customer_mapper\|identity_mappers->identity_api` |
| I14 | `layer-violation\|orders_mappers\|depot.orders.mappers.order_mapper\|orders_mappers->orders_api` |
| I15 | `layer-violation\|billing_mappers\|depot.billing.mappers.invoice_mapper\|billing_mappers->billing_api` |
| I16 | `layer-violation\|orders_services_pricing\|depot.orders.services.pricing.engine\|orders_services_pricing->orders_services` |

- **I17–I32: leer**, keine Vorschrift für Begleitmeldungen außerhalb von `FORBIDDEN_RELATION`/`CYCLE`.
- **I21–I24, Sonderfall Zwilling:** kein `expected_co_findings`-Eintrag im engeren Sinn, aber ein
  vorregistrierter **Begleit-Testfall** — der jeweilige Zwilling (`customer_view_models`,
  `order_view_models`, `order_line_view_models`, `invoice_view_models`) trägt dieselbe
  Importmenge und ist historisch als FP⁴ geführt worden; seit Protokoll §3 Rev. 20/21 ist das
  **keine Messung** für K4/K5 (beide sehen vor und nach der Injektion dieselbe Importmenge),
  sondern ein Präzisions-Testfall für K2/K3 (UF1/UF2). Kein vorregistrierter Treffer, getrennt zu
  führen.

---

## 5. Matchregel für K4 und K5 (wo die Erwartungsmatrix `ja`/`teilweise` trägt)

### 5.1 `LAYER_BACK_CALL` (I01–I03)

- **K4 (ja):** Spine-`layers`-Contract (`containers` = die drei Kontextpakete, `layers =
  api/services/repository/models`) meldet `BROKEN` für die Rückkante `repository → services`.
  **Zusätzlich, vorregistrierte K4-Doppelmeldung** (Komponentenschnitt §6.2; Protokoll §4
  Amendment 13.08. (a)): der einzige `acyclic_siblings`-Contract (`ancestors = depot`) meldet
  **denselben** Verstoß als Geschwisterzyklus `services ↔ repository` unter dem betroffenen
  Kontextpaket — kein False Positive, getrennt zu führen.
- **K5 (ja):** die Erlaubnislistenregel der jeweiligen `…_repository`-Komponente
  (`should_not().import_modules_except_modules_that().are_named([…])`) meldet
  `"<Trägermodul>" imports "<Modul in …_services>".`

### 5.2 `LAYER_SKIP_CALL` (I04–I06)

- **K4 (ja¹):** einer der sechs mechanisch aus der Schichtliste abgeleiteten `forbidden`-Contracts
  (`source_modules = <k>.api`, `<k>.repository` ∈ `forbidden_modules`, `allow_indirect_imports =
  True`) meldet `BROKEN`. Fußnote ¹: die Zelle misst Konfigurationsaufwand (UF4), nicht
  Erkennungsfähigkeit.
- **K5 (ja):** Erlaubnislistenregel der `…_api`-Komponente meldet
  `"<Trägermodul>" imports "<Modul in …_repository>".`

### 5.3 `PROTECTED_MODULE` (I07–I09)

- **K4 (ja ᴾ):** `protected`-Contract (`protected_modules = depot.core.adapters.internal`,
  `allowed_importers = depot.core.adapters`) meldet `BROKEN`. Annotation ᴾ: die Zelle ist an den
  Contract-**Typ** `protected` gebunden; am Testrepo ist sie nicht tragend, weil die Kette
  `services → storage → internal` hier nicht gebaut ist (Protokoll §3 Rev. 21 Nachtrag 1) — mit
  `forbidden` in Vorgabestellung hielte die Zelle hier ebenfalls (deklarierte Grenze, keine
  Messung dieses Unterschieds am Testrepo).
- **K5 (ja):** Erlaubnislistenregel der jeweiligen `…_services`-Komponente meldet
  `"<Trägermodul>" imports "depot.core.adapters.internal…".`

### 5.4 `INDEPENDENCE` (I10–I12)

- **K4 (ja):** `independence`-Contract (`modules = depot.orders, depot.billing`) meldet `BROKEN`.
  Keine K4-Doppelmeldung (Einzelkante zwischen Wurzelgeschwistern, Protokoll §4 Amendment
  13.08. (b)).
- **K5 (ja):** Erlaubnislistenregel der Quellkomponente meldet
  `"<Trägermodul>" imports "<Modul in Zielkomponente>".`

### 5.5 `CYCLE_SIBLING` (I13–I15)

- **K4 (ja):** der einzige `acyclic_siblings`-Contract meldet einen `No cycles are allowed in
  …`-Block, dessen **minimale, paketrelative Entfernungsmenge** (ohne Modulnamen, mit
  Importzähler) die injizierte Kante enthält, Form `- .mappers -> .api (1 import)`
  (Komponentenschnitt §6.1; Protokoll §4 Amendment 13.08. (c)).
- **K5 (teilweise⁷):** dieselbe Erlaubnislistenregel wie bei den vier `FORBIDDEN_RELATION`-Typen
  (**keine** Zyklenregel — B9+ F5 bleibt richtig) meldet die injizierte Rückkante als **nicht
  gelistete Kante**. Gemessenes Beispiel (orders, Protokoll §3 Fußnote 7 / Rev. 22, Beleg
  `c2c_bericht_k5_konfiguration.md` §B5, wörtliche Ausgabe):
  `"depot.orders.mappers.order_mapper" imports "depot.orders.api.routes".` Buchung ohne neue
  Regel: `strict` kein Treffer (Kategoriesegment weicht ab), `localized` Treffer als „richtige
  Stelle, falsche Kategorie" (Decision B39).

### 5.6 `CYCLE_PARENT_CHILD` (I16)

- **K4 (nein):** `acyclic_siblings` vergleicht ausschließlich Geschwister und erkennt
  Eltern/Kind-Zyklen nicht (B9+ F5, auch am externen Kontrollfall mit `ancestors = shop.audit`
  gemessen) — keine Matchregel.
- **K5 (teilweise⁷):** dieselbe Erlaubnislistenregel (für `orders_services_pricing`) meldet die
  Rückkante als nicht gelistete Kante. ~~Zitiertes Beispiel aus Protokoll §3 Fußnote 7 / Rev. 22:
  `"depot.orders.services.pricing.engine" imports "depot.orders.services.order_service".` **Diese
  Ausgabe wird hier zitiert, aber nicht ungeprüft übernommen** — siehe Widerspruch in §8 des
  Berichts: das Injektionsrezept beschreibt eine Rückkante auf das **Paket**
  `depot.orders.services`, nicht auf `order_service`.~~
  **Aufgelöst 25.08.2026 (Protokoll §3 Nachtrag Rev. 28):** die zitierte Zeile stammte aus der
  C2c-Prüfsonde gegen zehn Baseline-Kopien mit je einer nachgebauten Injektion, nicht aus der
  I16-Injektion dieses Testrepositoriums, die zum Zeitpunkt jener Messung noch nicht existierte.
  Verbindlich ist die Rückkante auf das **Paketmodul** `depot.orders.services` — die erwartete
  K5-Meldung lautet `"depot.orders.services.pricing.engine" imports "depot.orders.services".`
  Begründung: `CYCLE_PARENT_CHILD` prüft den Blindfleck von `acyclic_siblings` bei Paket **und**
  eigenem Untermodul (Decision Record P); ein Import auf `order_service` wäre auf Modulebene eine
  Kante zwischen Cousins und zerstörte den Gegenstand der Kategorie. Der `match_key` (§3, K1) ist
  davon unberührt — er stand bereits auf Komponentenebene (`orders_services_pricing->orders_services`).

### 5.7 `MISSING_PORT_REFERENCE` (I17–I20)

- **K4 (nein):** kein Contract-Typ erreicht eine erforderliche Referenz (`type = required`
  existiert nicht); keine Matchregel.
- **K5 (ja):** eine der vier dedizierten Portregeln
  (`are_named(<Trägermodul>).should().import_modules_that()…`, Untermodulebene) meldet, dass das
  benannte Modul den erforderlichen Import `depot.core.ports` **nicht** führt.

### 5.8 `INCORRECT_LOCATION` (I25–I28)

- **K4 (teilweise⁵ᴳ):** `layers`-Contract mit `exhaustive = True` auf dem Zielpaket (Layerliste
  aus dem **Dateibaum** der Clean-Baseline, Protokoll §3 Amendment (g)) meldet den verschobenen
  Träger als **nicht deklariertes Kind** — richtige Stelle, falsche Art (Fußnote 5); zählt in
  `localized`, nie in `strict`.
- **K5 (nein⁶ᴱ):** keine Matchregel — das Modul ist bauvorschriftsgemäß import- und referenzfrei
  (Abnahmebedingung 8, Protokoll §3 Amendment (e)), PyTestArch erreicht ein falsch platziertes
  Modul nur als Import-Proxy und damit hier gar nicht.

### 5.9 `FRAMEWORK_TYPE_IN_SIGNATURE` (I21–I24) und `SIGNATURE_DEVIATION` (I29–I32)

K4 = K5 = `nein` in beiden Zeilen; keine Matchregel. Für `FRAMEWORK_TYPE_IN_SIGNATURE` gemessen
(Protokoll §3 Rev. 20/21, Fußnote 4, c2b §B6/c2c §B6): beide Werkzeuge werten ausschließlich
Importkanten aus, und die Injektion ändert die Importmenge nicht. Für `SIGNATURE_DEVIATION`
bauvorschriftsgebunden (ᴴ, Amendment (h)): dieselbe Importmenge-invariante gilt hier per Bauregel.

---

## 6. Offene Punkte

~~**I21–I24 (`FRAMEWORK_TYPE_IN_SIGNATURE`): `offending_type` und die tragende Methode/Signatur
sind aus der Spezifikation nicht ableitbar.**~~ `R-FRAMEWORK-1` verlangt nur, dass der injizierte
Typ aus dem Namensraum `sqlalchemy.orm` stammt („Report the persistence type that appears in the
signature … verbatim"); welcher Typ (`Session` oder ein anderer) und welche öffentliche
Methode/Rückgabeposition ihn trägt, entscheidet laut Regelkommentar in
`architecture-rules.yaml` und Protokoll §3 („Zwingende Präzisierung zu `API_CONTRACT`" gilt hier
nicht, aber die Injektionsrezepttabelle nennt nur „einen Parameter- oder Rückgabetyp einer
öffentlichen Funktion") **erst der Bauauftrag C4b**. Eine Rückfrage am Testrepo (`git show
baseline:src/depot/identity/models/customer_models.py`, rein lesend, siehe Kopf dieser Datei)
bestätigt, dass die Baseline noch keine solche Signatur trägt — der Punkt ist nicht aus einer
vergessenen Angabe offen, sondern weil er zeitlich erst nach diesem Manifest entschieden wird.
~~Geführt als **OFFEN**, nicht durch Wahl einer plausiblen Annahme geschlossen.~~

**Aufgelöst 25.08.2026 (Auftrag C4B-0, Protokoll §3 Nachtrag Rev. 28), teilweise:** der injizierte
Typ ist **`sqlalchemy.orm.Session`** — der kanonische Typ des Namensraums, im `statement` von
R-FRAMEWORK-1 selbst als Beispiel genannt; `Mapped` ist ungeeignet, weil in Klassenattributen
erlaubt. Drei Auflagen für C4b: (a) öffentliche, vom Extractor erfasste Methode
(`b1_bericht_matchkey.md` C4), (b) kein neuer Import (`sqlalchemy.orm` in allen vier Trägern
bereits importiert, Importmenge identisch zum Zwilling), (c) kein gebrochener Aufrufer. Genau ein
Vorkommen je Träger (Singular-Regel, Protokoll §3 Nachtrag Rev. 17). **Weiterhin OFFEN** bleiben
die tragende Methode/Signatur und die wörtliche Schreibweise in der Signatur (unqualifiziert
`Session` oder qualifiziert `sqlalchemy.orm.Session`) — beide entscheidet erst der Bauauftrag C4b
und bildet `offending_type`; C4b meldet die Schreibweise wörtlich, C4c übernimmt sie ins Manifest.

**Nachtrag 25.08.2026 (Auftrag C4C), Rest von I21–I24 aufgelöst — bis auf die Schlüsselbildung:**
die tragende Methode ist je `Customer.reload` / `Order.reload` / `OrderLine.reload` /
`Invoice.reload`, die Signatur `def reload(self, session: sqlalchemy.orm.Session) -> None:`, und
die wörtliche Schreibweise in der Signatur ist `sqlalchemy.orm.Session` — **erzwungen** durch die
Top-Level-Import-Regel, nicht gewählt (§2.2). Damit ist alles beisammen, was §1c für den
`subjectKey` dieser Kategorie verlangt.

~~**Weiterhin OFFEN bleibt allein der Eintrag des `expected_match_key` selbst.** Auftrag C4C trägt
ausdrücklich **nur SHAs und Methodennamen** nach und ändert keinen `expected_match_key`; den
Schlüssel aus §1c zusammenzusetzen, wäre eine darüber hinausgehende Manifeständerung. Der aus §1c
mechanisch folgende Wert ist im Bericht `c4c_bericht_vorabpruefung.md` §A2 als **Beobachtung**
ausgewiesen und dort als eigener Punkt zur Entscheidung gestellt — **hier absichtlich nicht
eingetragen**. Er berührt K1 nicht: für I21–I24 ist die K1-Spalte `nein`, und die Vorabprüfung in
§B dieses Auftrags betrifft ausschließlich die sechzehn strukturellen Injektionen.~~

**Aufgelöst 26.08.2026 (Auftrag D1) — der letzte Punkt zu I21–I24 ist geschlossen.** Der
K2/K3-`expected_match_key` ist in beiden Manifestfassungen eingetragen; die vier Werte stehen in
der §3-Tabelle, die vollständige Ableitungskette mit Datum und Fundstelle je Glied im
**Ableitungsvermerk unter der §3-Tabelle**. Gebildet wurde er mechanisch aus den Feldern dieses
Manifests und aus `depot_soll.ilograph.yaml`, mit an `matchKey.ts:26` verifizierter
Segmentordnung, und zeichengleich (4 von 4) gegen `c4c_bericht_vorabpruefung.md` §A2 gestellt.
`FORBIDDEN_SIGNATURE_TYPE` ist nach Protokoll §8 (Rev. 22) die einzige Kategorie, in der allein
K2/K3 etwas finden können — ohne diesen Join-Schlüssel fiele die `strict`-Metrik dort aus, und
`localized` ist kein Ersatz, weil sie auf dem LLM-Pfad die Meldequote misst (Protokoll §4 Nachtrag
Rev. 27). Der Eintrag erfolgt **vor** dem ersten K2/K3-Lauf der Kampagne; der Commit-Zeitstempel
ist der Beleg der Anti-Tautologie-Regel aus Decision Record M. Die im Ableitungsvermerk
ausgesprochene Offenlegung zum K2-Kontrolllauf vom 24.08.2026 (63 `R-FRAMEWORK-1`-Findings, neun
davon auf Dateien ohne `sqlalchemy` im gerenderten Prompt) gehört ausdrücklich zu diesem Punkt.

**§6 führt zu I21–I24 damit keinen offenen Punkt mehr.**

~~**I16 (`CYCLE_PARENT_CHILD`), K5-Matchregel: Widerspruch zwischen Rezept und zitierter
Messausgabe.** Siehe §5.6 und den ausführlichen Bericht (`docs/repo-kontext/c4a_bericht_injektionsmanifest.md`
§8) — nicht durch einen eigenen Werkzeuglauf aufgelöst, wie es dieser Auftrag ausdrücklich
untersagt.~~

**Aufgelöst 25.08.2026 (Auftrag C4B-0, Protokoll §3 Nachtrag Rev. 28):** zugunsten des Rezepts —
die zitierte Messausgabe stammte aus der C2c-Prüfsonde gegen zehn Baseline-Kopien mit je einer
nachgebauten Injektion, nicht aus der I16-Injektion dieses Testrepositoriums. I16 ergänzt den
Import des **Paketmoduls** `depot.orders.services`. Siehe §5.6. Weiterhin **nicht** durch einen
eigenen Werkzeuglauf aufgelöst, wie es dieser Auftrag ausdrücklich untersagt — die Auflösung
stützt sich ausschließlich auf die Spezifikation (Protokoll §3 Nachtrag Rev. 28).

---

## 7. Vollständigkeitsprüfung

| # | Bedingung | Ist |
|---|---|---|
| 1 | 32 Zeilen, IDs I01–I32 lückenlos | ✔ 32 Zeilen, keine Lücke |
| 2 | Verteilung 3/3/3/3/3/1/4/4/4/4 (Protokoll §3) | ✔ LAYER_BACK_CALL 3, LAYER_SKIP_CALL 3, PROTECTED_MODULE 3, INDEPENDENCE 3, CYCLE_SIBLING 3, CYCLE_PARENT_CHILD 1, MISSING_PORT_REFERENCE 4, FRAMEWORK_TYPE_IN_SIGNATURE 4, INCORRECT_LOCATION 4, SIGNATURE_DEVIATION 4 — Summe 32 |
| 3 | jedes Trägermodul kommt genau einmal vor | ✔ 32 paarweise verschiedene Trägermodule (Abgleich gegen `c1_modulliste.md` §1, Rolle „Injektionsträger" = 32) |
| 4 | jede zitierte `rule_id` existiert in `architecture-rules.yaml` und ihr Scope enthält die Komponente des Trägers | ✔ alle 16 Regeln zitiert (R-LAYER-1, R-PROTECT-1, R-INDEP-1, R-CYCLE-1, R-CYCLE-2, R-PORT-1…4, R-FRAMEWORK-1, R-PLACE-1, R-SIG-1…4); Scope-Abgleich je Zeile in §2/§5 geprüft, keine Abweichung |
| 5 | jede der sechs Ebene-1-Kategorien ist besetzt, zeichengleich mit §3-Kodierung | ✔ FORBIDDEN_RELATION (12), CYCLE (4), ABSENCE_REQUIRED (4), FORBIDDEN_SIGNATURE_TYPE (4), STRUCTURAL_PLACEMENT (4), API_CONTRACT (4) — Strings identisch mit `architecture-rules.yaml`-Kopfkommentar |
| 6 | die vier `CYCLE`-Zeilen erfüllen Z1–Z4 und Z2′ (i)+(ii); Ordnungsvergleich maschinell | ✔ siehe §1d; Z1 (je 2 Komponenten/2 Kanten) und Z3 (keine parallele Zeugenkante) aus Komponentenschnitt §3/§4.5 übernommen, nicht neu geprüft — bereits dort maschinell verifiziert |
| 7 | die vier `INCORRECT_LOCATION`-Zeilen nennen Herkunft und Phantom-Zielort, Zielort ist direktes Kind eines Kontextpakets | ✔ siehe §2-Tabellenfußnote |
| 8 | die drei `LAYER_BACK_CALL`-Zeilen tragen die vorregistrierte K4-Doppelmeldung | ✔ §5.1 |
| 9 | keine `FORBIDDEN_RELATION`-Zeile trägt eine K1-Begleitmeldung (Graphmodus `diff`) | ✔ §4, erster Punkt |
| 10 | 32 `injection_sha256` eingetragen, je gegen `git rev-parse inj/NN` gestellt (C4c) | ✔ 32/32 zeichengleich, 0 Abweichungen — §2.1 |
| 11 | je Injektion die tragende Methode bzw. der tragende Modulpfad namentlich eingetragen (C4c) | ✔ I17–I20, I21–I24, I25–I28, I29–I32 in §2.2; I01–I16 tragen konstruktionsgemäß keine Methode (Kanteninjektion) |
| 12 | kein `expected_match_key` geändert (C4c) | ✔ maschinell gegengeprüft, Wertemenge vor/nach zeichengleich |

~~**Offene Punkte insgesamt:** 2 (I21–I24 `offending_type`/Methode; I16 K5-Zitat-Widerspruch) — beide
in §6 benannt, keiner durch Annahme oder Werkzeuglauf geschlossen.~~

**Stand 25.08.2026 (Auftrag C4B-0):** I16 ist **aufgelöst** (§5.6/§6). Bei I21–I24 ist der
injizierte **Typ** aufgelöst (`sqlalchemy.orm.Session`, §6); **weiterhin offen** bleiben die
tragende Methode/Signatur und deren wörtliche Schreibweise — beide entscheidet erst C4b. Keiner
der beiden Punkte wurde durch Annahme oder Werkzeuglauf geschlossen; beide Auflösungen stützen
sich ausschließlich auf Protokoll §3 Nachtrag Rev. 28 und liegen vor dem Bau der Commits.

**Stand 25.08.2026 (Auftrag C4C):** die 32 `injection_sha256` (§2.1) und die tragenden
Methoden/Modulpfade (§2.2) sind nachgetragen. Von den beiden ursprünglichen offenen Punkten ist
I16 seit C4B-0 erledigt; bei I21–I24 ist alles erledigt **außer** dem Eintrag des
`expected_match_key` selbst, der außerhalb dieses Auftrags liegt (§6). **Kein**
`expected_match_key` wurde geändert.

**SHA256 dieser beiden Dateien:** siehe `data/soll/SHA256SUMS`.
