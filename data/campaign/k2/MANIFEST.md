# MANIFEST — K2-Block der Konformitätskampagne (Ollama, alle 32 Injektionen)

**Datum des Laufs:** 27. August 2026, 08:46:01–08:50:18 CEST
**Auftrag:** C10 Phase 1, neu gefahren nach C10a
**Berichte:** [`docs/repo-kontext/c10_bericht_kampagne.md`](../../../docs/repo-kontext/c10_bericht_kampagne.md) ·
[`docs/repo-kontext/c10a_bericht_validator_punkt6.md`](../../../docs/repo-kontext/c10a_bericht_validator_punkt6.md)
**Protokollbezug:** §0.1 (Messstand, Amendments Rev. 34 und Rev. 35), §6 Rev. 24
(Aufrufspezifikation), Nachtrag Rev. 25 (getrennte Recordmengen), Rev. 26
(Wiederholungsfaktor, Exit-Code kein Gültigkeitskriterium), §1 Nachtrag Rev. 26
(Kontextfenster als gemessener Umgebungsparameter)

> **Nicht reproduzierbar. Niemals überschreiben.** LLM-Läufe gegen einen lokalen
> Ollama-Endpoint mit `temperature=0`/`seed=42` sind auch bei fixem Modellstand nicht
> bitgleich wiederholbar.

> **Keine Auswertung.** Dieses Verzeichnis enthält Rohbestand. Metriken, Findingbeurteilung
> und Vergleiche gehören nach C6b; die Eine-Iteration-Regel (§7) und die Amendment-Sperre
> aus §0.1 gelten.

## Messstand (§6 Punkt 4)

| Grösse | Wert |
|---|---|
| **Datum** | 27.08.2026, 08:46:01–08:50:18 CEST |
| **Repo-Commit (Messgegenstand)** | je Injektion `inj/01`…`inj/32`, sternförmig an `baseline` = `0d651041ed87dd03f2f78359713633fac01c0a66`; `--base` durchgehend dieser SHA |
| **Checker-Commit** | `checker_git_head` = `348ca9daa456af4954f11f7152fc45201035297e` (Tag `phase04-freeze`, Messpfad `~/ma/tritongraph-measure`) |
| **Checker-Artefakt** | `dist/cli.js` = `c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95` |
| **Prompt-Hash** | `prompt_template_sha256` = `65e78f38e7b1fee20000ea70c654df042f5e0831fc6a68ccb340f833bd915035` |
| **Regel-Hash** | `rules_sha256` = `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` |
| **Topologie-Hash** | `topology_sha256` = `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` |
| **Modell** | `qwen2.5-coder:7b` · Endpoint `http://localhost:11434/v1` · `seed=42`, `temperature=0` |
| **Kontextfenster** | **4096**, je Invocation **gemessen** (`window_source: MEASURED this campaign session`), = registrierter Wert; Modellgrenze laut `ollama show` 32768 |
| **Runner-Commit** | ~~`bd422b1bc9d6e9aa49a69779fc35a4fda12b6f41`~~ — **korrigiert am 27.08.2026 (C6b-1)**: jetzt **`4caf083d5e21f36440579af6888513ca897f1dd4`**, siehe Nachtrag am Ende |
| **Log-Schema** | `log_schema_version` = `2` |

Alle dreizehn Provenienzfelder stehen in **allen 32** Laufkopfzeilen zeichengleich.

## Aufrufzeile, wörtlich (Vorlage)

Aus Protokoll §6 Rev. 24, Abschnitt „K2, Ollama (je Injektion)". Je Invocation variiert **nur**
der Injektions-Checkout und die beiden Ausgabepfade (Repo-SHA im Dateinamen).

```sh
CONFORMANCE_API_KEY=ollama \
CONFORMANCE_BASE_URL=http://localhost:11434/v1 \
CONFORMANCE_MODEL=qwen2.5-coder:7b \
node ~/ma/tritongraph-measure/packages/triton-conformance/dist/cli.js \
  --topology ~/ma/masterarbeit/data/soll/depot_soll.ilograph.yaml \
  --rules ~/ma/masterarbeit/data/soll/architecture-rules.yaml \
  --src-root src --rule-graph diff --base 0d651041ed87dd03f2f78359713633fac01c0a66 \
  --runs 3 --timeout-ms 240000 \
  --run-log <out>/k2/k2_<repo-sha>.jsonl --json-out <out>/k2/k2_<repo-sha>.json
```

`--control-files` steht nur im Kontrolllauf und in **keinem** Injektionslauf (§6 Rev. 24).

## Gültigkeit

Entschieden allein von `tools/postrun_check.py` (§6 Nachtrag Rev. 24); der Exit-Code ist
**kein** Kriterium (Rev. 26).

| Grösse | Wert |
|---|---|
| Invocationen | **32** |
| Model-Calls | **96** (3 je Invocation, `--runs 3`) |
| VALID / INVALID | **32 / 0** |
| Wiederholungen | **keine** — alle Läufe `attempt 1` |
| `invalid_reasons` | durchgehend leer |
| `calls_invalid` / `calls_transport_failed` | **0** / **0** |
| `changed_files_count == 1` | in allen 32 |
| `valid_final` | **96 / 96 = 1,000** |
| max `tokens_in_total + tokens_out_total` je Call | **1948** (I08) gegen Fenster **4096** — **0** Überschreitungen |
| Records mit `rule_id`-Präfix `DERIVED:` | **16** |
| Records mit jedem anderen `rule_id` | **186** |
| externe Wanduhrzeit, Summe über 32 Invocationen | **252 155 ms** (252,2 s) |

Die beiden Recordzahlen stehen **getrennt** und werden **nie** summiert (§4/§6 Nachtrag
Rev. 25) — eine Auswertung, die nur die Gesamtzahl führt, ist ungültig.

## Inhalt

| Pfad | Inhalt |
|---|---|
| `data/campaign/k2/k2_<repo-sha>.jsonl` | Rohlauflog je Injektion, 32 Dateien |
| `data/campaign/k2/k2_<repo-sha>.json` | Findingausgabe je Injektion, 32 Dateien |
| `data/campaign/manifests/k2_<repo-sha>.json` | Laufmanifest je Injektion, 32 Dateien — Vorbedingungen, Soll-Validator-Ausgabe, Kontextfenstermessung, `postrun`-Verdikt |
| `data/campaign/k2/SHA256SUMS` | 96 Zeilen, mit `sha256sum -c` aus der Repowurzel prüfbar |

**`data/campaign/journal.jsonl` ist bewusst NICHT in `SHA256SUMS`.** Die Datei ist
append-only und wächst mit den Blöcken K3, K1, K4 und K5 weiter; ein Hash darauf wäre nach dem
nächsten Block falsch. Schnappschuss bei Abschluss des K2-Blocks, 32 Einträge, alle `VALID`,
alle `attempt 1`:

```
9fd6f2f2fa3a45af495a60983849b4e265a015ec0c9dfa2d11fbc77040914a6d  data/campaign/journal.jsonl
```

Der Gesamtstand über `data/campaign/` wird nach dem letzten Block geführt (C10 Phase 3).

## Vorgeschichte dieses Blocks

Ein erster K2-Anlauf am 27.08.2026 um 08:25 brach nach sechs Invocationen an I07 ab — der
Soll-Validator führte Punkt (6) als commit-invariant, was er nicht ist
(`c10a_bericht_validator_punkt6.md`). **Jene sechs Läufe sind verworfen**, nicht ausgewertet,
nicht committet und nach `~/scratch/c10a/abgebrochener_k2_teilbestand/` abgelegt; ihre SHA256
stehen im C10a-Bericht. **Der Block hier ist vollständig neu gefahren** und steht damit
geschlossen unter **einem** Runner-Commit (~~`bd422b1`~~ **`4caf083`**, Amendment Rev. 35; korrigiert am 27.08.2026, siehe Nachtrag unten).

---

## Nachtrag (27.08.2026, Auftrag C6b-1) — DIE ZEILE „RUNNER-COMMIT" WAR FALSCH BESETZT

**Der Alttext oben bleibt gestrichen sichtbar stehen**; korrigiert wird hier, nicht dort.

**Was falsch war.** Die Zeile trug `bd422b1bc9d6e9aa49a69779fc35a4fda12b6f41` — den
**Repo-HEAD zum Laufzeitpunkt**. Protokoll **§0.1** definiert die Grösse „Runner" aber anders:
als den **letzten Commit, der eine der drei Runner-Dateien berührt**
(`tools/run_campaign.py`, `tools/campaign_spec.py`, `tools/postrun_check.py`). Das ist
**`4caf083d5e21f36440579af6888513ca897f1dd4`** (`4caf083`, „fix: expect the injected importer
at soll validator point (6)"), und mit diesem Wert führen ihn auch
[`data/campaign/MANIFEST.md`](../MANIFEST.md) und [`k3/MANIFEST.md`](../k3/MANIFEST.md).

**`bd422b1` ist ein reiner Docs-Commit** („docs: amend rev 35 and report the aborted K2 partial
run") und berührt **keine** der drei Dateien; er ändert `eval_protokoll_phase04.md`,
`c10a_bericht_validator_punkt6.md` und `c5b_bericht_protokoll_freeze.md`. `git log` über die
drei Runner-Dateien nennt unverändert `4caf083` als letzten.

**Der Runner-Code war identisch — die Angabe war trotzdem falsch.** Gegengeprüft, Datei für
Datei, `git show <commit>:<datei> | sha256sum`:

| Datei | an `4caf083` | an `bd422b1` |
|---|---|---|
| `tools/run_campaign.py` | `eba3b95a0bfb2119…` | `eba3b95a0bfb2119…` |
| `tools/campaign_spec.py` | `c95d38140f00ee1d…` | `c95d38140f00ee1d…` |
| `tools/postrun_check.py` | `d179dcba0530c680…` | `d179dcba0530c680…` |

**Der K2-Block ist also unter demselben Runner-Code gelaufen wie K1, K3, K4 und K5.** Es
bewegt sich **keine Messung, kein Artefakt, kein Hash und keine Zahl** — korrigiert wird eine
**Provenienzangabe**, und zwar deshalb, weil das Gesamtmanifest **eine einzige** Runner-Zeile
führt und damit stillschweigend behauptete, alle fünf Blöcke stünden unter demselben Wert. Sie
tun es; die Zeile hier sagte es falsch.

**`SHA256SUMS` bleibt unberührt** — die Blockmanifeste stehen nicht darin (dokumentiert im
Abschnitt „Inhalt" oben: `SHA256SUMS` führt die 96 Lauf- und Findingdateien).

**Fundstelle des Befunds:** `c6b0_bericht_tabellenskelette.md` §8 (a), dort als Beobachtung aus
den erlaubten Metadaten notiert und nicht geändert; korrigiert mit diesem Auftrag.
