"""K5 — PyTestArch configuration of the target model ("Soll") of the conformance test
repository `ma-conformance-testrepo`. Baseline tool K5 of the campaign.

Pinned measurement state (protocol §1): PyTestArch 4.0.1, networkx 3.6.1, pytest 9.0.1,
Python 3.12.3, SQLAlchemy 2.0.52.

    DEPOT_SRC=<testrepo>/src python -m pytest -p no:cacheprovider -q data/soll/test_architecture.py

THIS FILE EXPRESSES THE TARGET ARCHITECTURE, NOT THE INJECTION PLAN (protocol §1
Rev. 13). `COMPONENTS` and `WHITELIST` below are generated from the frozen Soll
(`depot_soll.ilograph.yaml`, 19 components / 77 modules / 39 relations), not curated by
hand; see `MANIFEST.md` for the derivation. A rule without a matching injection is
correct — it contributes to the false-positive measurement.

Twenty-three rules:
   19  allow-list      one per component: everything not on the whitelist is forbidden
    4  port rules      one per MISSING_PORT_REFERENCE carrier, on the SUBMODULE level

ONE architecture object, `exclude_external_libraries = True` (protocol §1 Rev. 20 / C2c).
The second object of Rev. 14 carried the framework rule only; with the FP⁴ cell withdrawn
in Rev. 20 that rule is gone, and an unused object in a file that is about to be frozen is
dead weight.

`root_path` AND `module` point at the ROOT PACKAGE directory `<repo>/src/depot`, not at
the source root. Only then are the node names `depot.core.ports` rather than
`src.depot.core.ports` (c2a §5.2) and only then do they coincide with the module names of
the checker and with the `match_key` of the manifest. Without this choice K5 is not
joinable.

The SHA256 of this file is a hashed measurement input and falls under the change freeze of
protocol §1 Rev. 10; see `MANIFEST.md`.
"""

from __future__ import annotations

import os

import pytest
from pytestarch import Rule, get_evaluable_architecture

# ── the architecture object ───────────────────────────────────────────────────────────
#
# Built once, before the first test (c2b §2c). `exclude_external_libraries = True` keeps
# every foreign node out of the graph: an allow-list that had to enumerate `typing` and
# `sqlalchemy` would be a list taken FROM THE REPO instead of from the target
# architecture, and would break on `typing` alone (c2b §2b).

_SRC = os.environ.get("DEPOT_SRC")
if not _SRC:
    raise RuntimeError(
        "DEPOT_SRC must point at the source root <testrepo>/src; "
        "root_path and module are derived from it as <DEPOT_SRC>/depot."
    )
ROOT_PACKAGE = os.path.join(_SRC, "depot")

ARCH = get_evaluable_architecture(
    ROOT_PACKAGE,
    ROOT_PACKAGE,
    exclude_external_libraries=True,
)

# ── the modules of every component ────────────────────────────────────────────────────
#
# Generated from the `resources` block of `depot_soll.ilograph.yaml`, with two mechanical
# conversions:
#
#   (1) the Soll writes an `__init__.py` under its PACKAGE name (protocol §2, point (6));
#       PyTestArch keeps `<package>` and `<package>.__init__` as SEPARATE nodes and
#       attributes an import in an `__init__.py` to the latter (c2a §5.3). Every Soll
#       module that is a package of the clean baseline is therefore rewritten to
#       `...__init__`. The package nodes themselves are never named: their only outgoing
#       edges are containment edges, which are not imports.
#
#   (2) BAUVORSCHRIFT K5-1 — the four `INCORRECT_LOCATION` carriers and their four
#       phantom target locations are dropped. A rule target that is not in the graph
#       raises `NetworkXError`, i.e. an ERROR instead of a FAILURE (c2a §5.1). The eight
#       names are import- and reference-free (`c1_modulliste.md` §4, condition 8), so
#       dropping them removes no edge from the measurement. Guarded by
#       `test_k5_1_no_rule_names_a_locked_module` below.
#
# 77 Soll modules − 4 phantoms − 4 carriers = 69.

COMPONENTS = {
    "billing_api": [
        "depot.billing.api.__init__",
        "depot.billing.api.routes",
        "depot.billing.api.schemas",
    ],
    "billing_mappers": [
        "depot.billing.mappers.__init__",
        "depot.billing.mappers.invoice_mapper",
        "depot.billing.mappers.payment_mapper",
    ],
    "billing_models": [
        "depot.billing.models.__init__",
        "depot.billing.models.invoice_models",
        "depot.billing.models.invoice_view_models",
        "depot.billing.models.payment_models",
    ],
    "billing_repository": [
        "depot.billing.repository.__init__",
        "depot.billing.repository.invoice_query",
        "depot.billing.repository.invoice_repo",
    ],
    "billing_services": [
        "depot.billing.services.__init__",
        "depot.billing.services.dunning_service",
        "depot.billing.services.invoice_service",
        "depot.billing.services.ledger_service",
    ],
    "core": [
        "depot.__init__",
        "depot.billing.__init__",
        "depot.core.__init__",
        "depot.core.config",
        "depot.core.errors",
        "depot.core.ports",
        "depot.identity.__init__",
        "depot.orders.__init__",
    ],
    "core_adapters": [
        "depot.core.adapters.__init__",
        "depot.core.adapters.storage",
    ],
    "core_adapters_internal": [
        "depot.core.adapters.internal.__init__",
        "depot.core.adapters.internal.cache",
        "depot.core.adapters.internal.session",
    ],
    "identity_api": [
        "depot.identity.api.__init__",
        "depot.identity.api.routes",
        "depot.identity.api.schemas",
    ],
    "identity_mappers": [
        "depot.identity.mappers.__init__",
        "depot.identity.mappers.customer_mapper",
        "depot.identity.mappers.role_mapper",
    ],
    "identity_models": [
        "depot.identity.models.__init__",
        "depot.identity.models.customer_models",
        "depot.identity.models.customer_view_models",
        "depot.identity.models.role_models",
    ],
    "identity_repository": [
        "depot.identity.repository.__init__",
        "depot.identity.repository.customer_repo",
        "depot.identity.repository.session_repo",
    ],
    "identity_services": [
        "depot.identity.services.__init__",
        "depot.identity.services.customer_service",
        "depot.identity.services.token_service",
    ],
    "orders_api": [
        "depot.orders.api.__init__",
        "depot.orders.api.routes",
        "depot.orders.api.schemas",
    ],
    "orders_mappers": [
        "depot.orders.mappers.__init__",
        "depot.orders.mappers.order_line_mapper",
        "depot.orders.mappers.order_mapper",
    ],
    "orders_models": [
        "depot.orders.models.__init__",
        "depot.orders.models.discount_models",
        "depot.orders.models.order_line_models",
        "depot.orders.models.order_line_view_models",
        "depot.orders.models.order_models",
        "depot.orders.models.order_view_models",
    ],
    "orders_repository": [
        "depot.orders.repository.__init__",
        "depot.orders.repository.order_line_repo",
        "depot.orders.repository.order_query",
        "depot.orders.repository.order_repo",
    ],
    "orders_services": [
        "depot.orders.services.__init__",
        "depot.orders.services.catalog_service",
        "depot.orders.services.checkout_service",
        "depot.orders.services.order_service",
        "depot.orders.services.refund_service",
    ],
    "orders_services_pricing": [
        "depot.orders.services.pricing.__init__",
        "depot.orders.services.pricing.engine",
    ],
}

# ── the whitelist ─────────────────────────────────────────────────────────────────────
#
# The 39 relations of the `dependencies` perspective, grouped by source component
# (`c1_komponentenschnitt.md` §4). Only listed edges are allowed; anything else is
# forbidden. `core` and `core_adapters_internal` have no outgoing relation at all.

WHITELIST = {
    "billing_api": ["billing_mappers", "billing_services", "core"],
    "billing_mappers": ["billing_models", "core"],
    "billing_models": ["core"],
    "billing_repository": ["billing_models", "core"],
    "billing_services": ["billing_repository", "core", "core_adapters", "identity_services"],
    "core": [],
    "core_adapters": ["core", "core_adapters_internal"],
    "core_adapters_internal": [],
    "identity_api": ["core", "identity_mappers", "identity_services"],
    "identity_mappers": ["core", "identity_models"],
    "identity_models": ["core"],
    "identity_repository": ["core", "identity_models"],
    "identity_services": ["core", "core_adapters", "identity_repository"],
    "orders_api": ["core", "orders_mappers", "orders_services"],
    "orders_mappers": ["core", "orders_models"],
    "orders_models": ["core"],
    "orders_repository": ["core", "orders_models"],
    "orders_services": ["core", "core_adapters", "identity_services", "orders_repository", "orders_services_pricing"],
    "orders_services_pricing": ["core"],
}


# ── 19 × allow-list — one rule per component ──────────────────────────────────────────
#
# The allowed targets of a component are the modules of its whitelist neighbours PLUS its
# own modules. The second half is not a relaxation: the whitelist is a graph over
# COMPONENTS, an edge inside a component is `from === to` and invisible to K1
# (`ruleEngine.ts:47`, V4). A rule that forbade those edges would express a STRICTER
# architecture than the frozen target model and would violate the principle of protocol §1
# Rev. 13. Under `are_named([...])` each subject module is evaluated on its own, so
# without the self-entry an import between two modules of one component would be reported.
#
# NOT `should_only()`. That is a SET EQUALITY, not an allow-list: its positive half also
# demands that every listed target actually IS imported, so a module using a SUBSET of its
# allowed neighbours breaks the rule on the CLEAN baseline (c2b §1c-Zusatz). Derived from
# the whitelist — as the principle requires — `should_only` would be the same trap as
# `exhaustive` on the spine contract, only on the K5 side: C3 would fail on a
# configuration error that looks like a repo error. The chosen form has no positive half;
# it holds on a subset and on an empty import set and breaks on every unlisted import.
#
# The forbidding half evaluates PER IMPORT and names the offending module (c2b §1c/§1d),
# so a broken rule yields n findings on module level and is joinable on edge level.
#
# Targets are always named on MODULE level, never on package level. A package name as an
# allowed target pulls in its whole subtree (`get_all_submodules_of`,
# `breadth_first_searches.py`): `depot.core.adapters` as an allowed target for the three
# `...services` components would silently allow `depot.core.adapters.internal` as well and
# the `PROTECTED_MODULE` injections would go unreported.


def _subject(component: str) -> list[str]:
    return COMPONENTS[component]


def _allowed(component: str) -> list[str]:
    names = [component] + WHITELIST[component]
    return sorted(m for name in names for m in COMPONENTS[name])


ALLOW_LIST_RULES = {
    component: (
        Rule()
        .modules_that()
        .are_named(_subject(component))
        .should_not()
        .import_modules_except_modules_that()
        .are_named(_allowed(component))
    )
    for component in sorted(COMPONENTS)
}


@pytest.mark.parametrize("component", sorted(ALLOW_LIST_RULES))
def test_component_imports_only_whitelisted_modules(component: str) -> None:
    ALLOW_LIST_RULES[component].assert_applies(ARCH)


# ── 4 × port rule — one per MISSING_PORT_REFERENCE carrier ────────────────────────────
#
# Four SEPARATE rules, each naming ONE carrier module — not one rule over
# `are_sub_modules_of`. `should()` has AGGREGATE semantics and holds as soon as ANY module
# of the subject set imports the target (B9+ question 4, restriction 1; c2b §1d). The
# submodule level is measured, not assumed: `import depot.x.y` resolves to the imported
# SUBMODULE and `should()` checks on exactly that level, so the target does not have to be
# lifted to `depot.core` (c2a §4).
#
# Unaffected by K5-1: the `MISSING_PORT_REFERENCE` injection removes the IMPORT, the
# module `depot.core.ports` stays (protocol §3, amendment (f)).

PORT_CARRIERS = {
    "R-PORT-1": "depot.identity.services.token_service",    # I17, TokenSigner
    "R-PORT-2": "depot.orders.services.catalog_service",    # I18, RateProvider
    "R-PORT-3": "depot.orders.services.refund_service",     # I19, PaymentGateway
    "R-PORT-4": "depot.billing.services.ledger_service",    # I20, Clock
}

PORT_RULES = {
    rule_id: (
        Rule()
        .modules_that()
        .are_named(carrier)
        .should()
        .import_modules_that()
        .are_named("depot.core.ports")
    )
    for rule_id, carrier in PORT_CARRIERS.items()
}


@pytest.mark.parametrize("rule_id", sorted(PORT_RULES))
def test_carrier_references_the_core_ports(rule_id: str) -> None:
    PORT_RULES[rule_id].assert_applies(ARCH)


# ── guard, not an architecture rule ───────────────────────────────────────────────────
#
# Bauvorschrift K5-1, checked instead of asserted in prose. Runs on the clean baseline and
# on every injection commit; after I25–I28 the carrier has moved and the phantom exists,
# and either name inside a rule would turn a FAILURE into a tool ERROR.

K5_1_LOCKED = (
    "depot.orders.repository.legacy_order_index",     # I25 carrier
    "depot.billing.repository.legacy_invoice_index",  # I26 carrier
    "depot.identity.repository.legacy_token_index",   # I27 carrier
    "depot.billing.models.legacy_tax_models",         # I28 carrier
    "depot.orders.legacy_order_index",                # I25 phantom target
    "depot.billing.legacy_invoice_index",             # I26 phantom target
    "depot.identity.legacy_token_index",              # I27 phantom target
    "depot.billing.legacy_tax_models",                # I28 phantom target
)


def test_k5_1_no_rule_names_a_locked_module() -> None:
    named = {m for c in COMPONENTS for m in COMPONENTS[c]}
    named.update(PORT_CARRIERS.values())
    named.add("depot.core.ports")
    assert named.isdisjoint(K5_1_LOCKED)
    assert len(ALLOW_LIST_RULES) + len(PORT_RULES) == 23
