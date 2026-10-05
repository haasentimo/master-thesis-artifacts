# MANIFEST — Sicherung der Clean-Baseline `B` des Testrepos

**Datum der Ablage:** 14. August 2026
**Bezug:** Phase 04, Schritt 4 (Bau der Clean-Baseline), Bauauftrag 4b-4
**Bericht:** [docs/repo-kontext/4b4_bericht_baseline_billing.md](../../docs/repo-kontext/4b4_bericht_baseline_billing.md)

## Zweck

Sicherung des **Evaluationsdatensatzes der Phase 04**. Das Testrepo ist das
Messobjekt der gesamten Kampagne; ohne die Clean-Baseline `B` ist kein Messlauf
und keine Auswertung reproduzierbar.

Das Testrepo liegt zugleich auf einem **privaten Remote unter eigener Kontrolle**
(`origin/main` gleichauf mit `0d65104`). Das Bundle sichert daher gegen
**Zugriffsverlust**, nicht gegen Datenverlust, und dient als Grundlage des
**Reproduzierbarkeits-Anhangs** der Arbeit.

## Inhalt

| Datei | Beschreibung |
|---|---|
| `ma-conformance-testrepo-baseline.bundle` | Git-Bundle des gesamten Testrepos, 52 KB, `--all` |
| `SHA256SUMS` | Prüfsumme des Bundles |

**SHA256:** `597fa466c5ff4e05ab5c1f3550fb88e0407c3968fae8fafd420166324d4a7b18`

## Herkunft

- **Quellrepo:** `ma-conformance-testrepo` (`~/Schreibtisch/ma-conformance-testrepo`)
- **Remote:** `origin` = `git@github.com:haasentimo/ma-conformance-testrepo.git`
  — **privat, im Eigentum des Autors**
- **Branch:** `main`, gleichauf mit `origin/main`
- **Datum der Sicherung:** 14. August 2026
- **Arbeitsverzeichnis zum Zeitpunkt der Sicherung:** sauber (`git status --porcelain`
  vor und nach dem Lauf leer). Am Testrepo wurde nichts geändert — kein Commit,
  kein Tag, kein Push, keine Änderung der Remote-Konfiguration.

## Die Clean-Baseline `B`

> ```
> B = Tag `baseline` = 0d651041ed87dd03f2f78359713633fac01c0a66
> ```
>
> **Dieser SHA ist `--base` für JEDEN Messlauf der Kampagne.**

Der Tag `baseline` ist der einzige eindeutige benannte Zeiger auf `B` und liegt
im Bundle (siehe `verify`-Ausgabe unten).

## Umfang

Erzeugt mit `git bundle create ... --all`, also die **komplette Historie**: die
**fünf Baucommits** und der Tag.

| Commit | Inhalt |
|---|---|
| `f3870da` | Kerngruppe — core, adapters, geschützte Internals |
| `6b224c9` | Kontext `identity` |
| `1b165f2` | Teil A der Clock-Korrektur (Document Store implementiert einen Port, statt eine Clock zu halten) |
| `9869340` | Kontext `orders` |
| `0d65104` | Kontext `billing` und Abschluss — **= `B`**, Tag `baseline` |

Die **32 Injektions-Commits (I01–I32) existieren noch nicht.** Sie hängen später
**sternförmig** an `B`. Sobald sie stehen, ist ein **zweites, vollständiges
Bundle** zu erzeugen; dieses hier bleibt als Stand der reinen Baseline bestehen.

### `git bundle verify` — wörtlich

```
$ git bundle verify data/testrepo/ma-conformance-testrepo-baseline.bundle
/home/timohaas/Schreibtisch/masterarbeit/data/testrepo/ma-conformance-testrepo-baseline.bundle ist in Ordnung
Das Paket enthält diese 4 Referenzen:
0d651041ed87dd03f2f78359713633fac01c0a66 refs/heads/main
0d651041ed87dd03f2f78359713633fac01c0a66 refs/remotes/origin/main
0d651041ed87dd03f2f78359713633fac01c0a66 refs/tags/baseline
0d651041ed87dd03f2f78359713633fac01c0a66 HEAD
Das Paket speichert eine komplette Historie.
The bundle uses this hash algorithm: sha1
```

Alle vier Referenzen zeigen auf denselben Commit; `refs/heads/main` **und**
`refs/tags/baseline` sind enthalten.

## Vermerk zum Amend — der unerreichbare SHA `6aea3df`

Während des Baus wurde der letzte Commit einmal per `git commit --amend`
korrigiert (die zweite `Clock`-Signatur); der Tag wurde vorher gelöscht und
danach neu gesetzt. Der kurzzeitig vergebene SHA **`6aea3df` ist dadurch
unerreichbar**, liegt **nicht** im Bundle und **darf nirgends als `--base`
auftauchen**. Gültig ist allein `0d65104…`.

Der Sprung in der Reflog-Historie ist damit erklärt und **kein Verlust** — es war
nichts gepusht, der Amend ist folgenlos.
Quelle: `4b4_bericht_baseline_billing.md` §5 (Ursache in §2).

## Geheimnis-Kontrolle

Vor der Ablage geprüft, wie bei `data/checker/`. Weil das Bundle `--all` umfasst,
zusätzlich auf Stashes geprüft.

| Prüfung | Ergebnis |
|---|---|
| `git ls-files \| grep -Ei '(^\|/)\.env\|secret\|credential\|\.pem$'` | **kein Treffer** |
| `git log --diff-filter=A --name-only --pretty=format: \| sort -u \| grep -Ei '(^\|/)\.env\|secret\|credential\|\.pem$'` | **kein Treffer** |
| `git stash list` | **leer — kein Stash vorhanden** |

Kein Treffer in der gesamten Historie und keine Stashes. Das Repo enthält
ausschließlich generierten Python-Quelltext der Clean-Baseline, `.gitignore` und
`README.md`.

## Wiederherstellung

```
git clone ma-conformance-testrepo-baseline.bundle ma-conformance-testrepo
cd ma-conformance-testrepo && git checkout baseline
```

## Abgrenzung — dies ist NICHT der Freeze-Stand des Checkers

Diese Ablage sichert das **Testrepo** (Messobjekt). Der Freeze-Stand des
**Conformance-Checkers** ist ein anderer Gegenstand und liegt in
[`data/checker/`](../checker/MANIFEST.md), Commit `fe66357`. Die beiden dürfen
nicht verwechselt werden: `--base` der Messläufe ist `0d65104` (dieses Bundle),
`checker_git_head` der Logzeilen verweist auf `fe66357`.

---

# Nachtrag 25. August 2026 — zweites Bundle, der **vollständige Evaluationsdatensatz**

**Datum der Ablage:** 25. August 2026
**Bezug:** Phase 04, Schritt C4b (Bau der 32 Injektions-Commits)
**Bericht:** [docs/repo-kontext/c4b_bericht_injektionen.md](../../docs/repo-kontext/c4b_bericht_injektionen.md)

Damit ist eingelöst, was der Abschnitt „Umfang" oben angekündigt hat: die 32
Injektions-Commits stehen, und das zweite, vollständige Bundle liegt ab.

## Rollentrennung — die beiden Bundles sichern zwei verschiedene Rollen

Ausdrücklich, wie bei [`data/checker/`](../checker/MANIFEST.md):

- **`ma-conformance-testrepo-baseline.bundle`** sichert den Zustand **VOR** den
  Injektionen — die reine Clean-Baseline `B`. Das ist der **Messgegenstand der
  Clean-State- und Kontrollläufe**: C3a (K1/K4/K5 auf `B`, 0 Findings) und C3b
  (K2/K3 über die 52 Kontrollmodule) messen genau diesen Stand und keinen anderen.
- **`ma-conformance-testrepo-injections.bundle`** ist der **VOLLSTÄNDIGE
  Evaluationsdatensatz**: dieselbe Clean-Baseline **plus die 32 Injektions-Commits**
  mit ihren 32 Tags. Aus ihm läuft die Kampagne.

**Beide bleiben liegen; keines ersetzt das andere.** Das erste ist der Beleg dafür,
dass der Kontrollstand vor den Injektionen unberührt war; das zweite ist der Stand,
gegen den gemessen wird. `--base` ist in beiden Fällen derselbe SHA `0d65104`.

## Inhalt

| Datei | Beschreibung |
|---|---|
| `ma-conformance-testrepo-injections.bundle` | Git-Bundle des gesamten Testrepos, 71 KB (71.767 Bytes), `--all` |

**SHA256:** `1b9f8b58f271332e2d66ead83a3858271a04f3aebce95b7927977d9fa1be508b`

Die Prüfsumme steht in `SHA256SUMS`. `sha256sum -c SHA256SUMS` ist am 25.08.2026 für
**beide** Bundles grün:

```
$ cd data/testrepo && sha256sum -c SHA256SUMS
ma-conformance-testrepo-baseline.bundle: OK
ma-conformance-testrepo-injections.bundle: OK
```

## Herkunft

- **Quellrepo:** `ma-conformance-testrepo` (`~/ma/ma-conformance-testrepo` — der Pfad
  hat sich mit dem Maschinenwechsel geändert, das Repo nicht)
- **Remote:** `origin` = `git@github.com:haasentimo/ma-conformance-testrepo.git`
  — **privat, im Eigentum des Autors**
- **Arbeitsverzeichnis zum Zeitpunkt der Sicherung:** sauber (`git status --porcelain`
  leer, vor dem Bau, zwischen allen 32 Commits und danach —
  `c4b_bericht_injektionen.md` §8.9)
- **`baseline` unverändert** auf `0d651041ed87dd03f2f78359713633fac01c0a66`, **`main`
  ebenso**

## Die 32 Injektions-Commits

Gelesen aus der `git bundle verify`-Ausgabe unten und gegen `git ls-remote --tags origin`
abgeglichen — **die 32 SHAs sind lokal und auf `origin` zeichengleich**.

**Diese Tabelle ist die Quelle, aus der C4c das Injektionsmanifest füllt**
(`injection_sha256`, bis dahin absichtlich leer — Anti-Tautologie-Regel). Die Zuordnung
Injektions-ID → Szenario stammt aus `c4b_bericht_injektionen.md` §2.

| ID | Ref | Commit-SHA | Szenario |
|---|---|---|---|
| I01 | `inj/01` | `439125ece20060321bff983d7b8295f1b33dda50` | `LAYER_BACK_CALL` |
| I02 | `inj/02` | `4165fab5c82b1194572461fdb232c1af264e66f5` | `LAYER_BACK_CALL` |
| I03 | `inj/03` | `b3fb12905f7f3becc803d1915af5654da35643bb` | `LAYER_BACK_CALL` |
| I04 | `inj/04` | `3de8357bc191821fe60922022be257c47959d35d` | `LAYER_SKIP_CALL` |
| I05 | `inj/05` | `dbcd05b8935ac3d007464f2e0d72c08ef0a9931e` | `LAYER_SKIP_CALL` |
| I06 | `inj/06` | `531a1ff2616aaa13f8c317fe7d40f56135caacaf` | `LAYER_SKIP_CALL` |
| I07 | `inj/07` | `0993e01b26b7cc91bb70840207860fcc15dba286` | `PROTECTED_MODULE` |
| I08 | `inj/08` | `792cb6867f55634bc3f8bfac321b392ea5507a48` | `PROTECTED_MODULE` |
| I09 | `inj/09` | `06e052e19c153503f751611d7f813f18f204d8f0` | `PROTECTED_MODULE` |
| I10 | `inj/10` | `e1829642b304a016d0b2f11087c2b215f8368942` | `INDEPENDENCE` |
| I11 | `inj/11` | `5601a944ea1da65b1e2b03c5e74a8237336a2e85` | `INDEPENDENCE` |
| I12 | `inj/12` | `cb1fb228ff6021071a8c6b2a88506a80f138eafb` | `INDEPENDENCE` |
| I13 | `inj/13` | `3be646fed3bdb2449b153f912d42fbb63b719776` | `CYCLE_SIBLING` |
| I14 | `inj/14` | `a9d644515812b98877af4e63e0f9a3f119ee7e88` | `CYCLE_SIBLING` |
| I15 | `inj/15` | `616cb02982e634670c4dbaa84d5efbf4df63c61a` | `CYCLE_SIBLING` |
| I16 | `inj/16` | `43f9fa5ec1b6fbf4aaae26296a41b752c2e3f9cf` | `CYCLE_PARENT_CHILD` |
| I17 | `inj/17` | `c5faa0a65f0a85e9bb1a1ecac950806650449ec1` | `MISSING_PORT_REFERENCE` |
| I18 | `inj/18` | `ad210637f542736323c4d2f5da4254c4c4e60bad` | `MISSING_PORT_REFERENCE` |
| I19 | `inj/19` | `864da9678e6a10137a2fd2d4b1a7d73082db403f` | `MISSING_PORT_REFERENCE` |
| I20 | `inj/20` | `35061d852631049ff74f65451368d7e85fd733bd` | `MISSING_PORT_REFERENCE` |
| I21 | `inj/21` | `dd414657d12197a1ca79152d401f75eb4b5f5f57` | `FRAMEWORK_TYPE_IN_SIGNATURE` |
| I22 | `inj/22` | `08a622b024e9174d7ce62863f385b369c8c27b12` | `FRAMEWORK_TYPE_IN_SIGNATURE` |
| I23 | `inj/23` | `28a75749496229bb1db37d85f68347572bd84c49` | `FRAMEWORK_TYPE_IN_SIGNATURE` |
| I24 | `inj/24` | `91ed6a80d415c68eed7661a21ea554ba32da9c83` | `FRAMEWORK_TYPE_IN_SIGNATURE` |
| I25 | `inj/25` | `ef114806ec2360f19eb9dc9425d79ed153b9a769` | `INCORRECT_LOCATION` |
| I26 | `inj/26` | `efe5c81f526d183fcb6634e65df00e7f90b0dbc3` | `INCORRECT_LOCATION` |
| I27 | `inj/27` | `33ad86a07dd626c59541c91334d33f3e1e76bc04` | `INCORRECT_LOCATION` |
| I28 | `inj/28` | `72dc7461f9ecb5cdd53293f1f94d7418e98a3401` | `INCORRECT_LOCATION` |
| I29 | `inj/29` | `5e685cff9559cfbff8935162405cd98c5c10932e` | `SIGNATURE_DEVIATION` |
| I30 | `inj/30` | `604d30460ce9a602b7b635f8f6de08c113acf9bf` | `SIGNATURE_DEVIATION` |
| I31 | `inj/31` | `3d3374571153656f012a15d01df7f5e8dcb88c8e` | `SIGNATURE_DEVIATION` |
| I32 | `inj/32` | `307e57327a81d94dea84614d9fc9d8d82b839f97` | `SIGNATURE_DEVIATION` |

## HINWEIS — die 32 Injektions-Commits liegen NICHT auf `main`

Dieser Punkt darf beim Lesen des Bundles nicht fehlen:

> **`main` und `baseline` zeigen beide auf `0d651041ed87dd03f2f78359713633fac01c0a66`.**
> Die 32 Injektions-Commits hängen als **Blätter** daran — **Sternform**, so
> vorgeschrieben in Protokoll §6 (Amendment 12.08.2026): 32 Commits mit `B` als
> **einzigem** Elternteil, kein Merge, keine kumulative Kette.

Daraus folgt unmittelbar: **die 32 Commits sind ausschließlich über ihre Tags
erreichbar.** Ein `git log main` zeigt sie nicht, ein Klon ohne Tags enthält sie nicht.

- **Ein gelöschtes Tag entfernt faktisch einen Messpunkt.** Der Commit wird damit
  unreferenziert, und `git gc` sammelt ihn anschließend ein — dann ist der Messstand
  weg, obwohl `main` unversehrt aussieht.
- **Die Tags sind deshalb nicht zu löschen und nicht zu verschieben.** Das gilt lokal
  wie auf `origin`; die Push-Rechte dort umfassen ausdrücklich auch das Löschen von
  Tags (`b20_bericht_push_rechte.md`). Genau darum werden die Messstände **zusätzlich
  über ihre SHAs** geführt — die Tabelle oben ist der Anker, nicht der Tagname.

## `git bundle verify` — wörtlich

```
$ git bundle verify data/testrepo/ma-conformance-testrepo-injections.bundle
data/testrepo/ma-conformance-testrepo-injections.bundle is okay
The bundle contains these 37 refs:
0d651041ed87dd03f2f78359713633fac01c0a66 refs/heads/main
0d651041ed87dd03f2f78359713633fac01c0a66 refs/remotes/origin/HEAD
0d651041ed87dd03f2f78359713633fac01c0a66 refs/remotes/origin/main
0d651041ed87dd03f2f78359713633fac01c0a66 refs/tags/baseline
439125ece20060321bff983d7b8295f1b33dda50 refs/tags/inj/01
…
307e57327a81d94dea84614d9fc9d8d82b839f97 refs/tags/inj/32
0d651041ed87dd03f2f78359713633fac01c0a66 HEAD
The bundle records a complete history.
The bundle uses this hash algorithm: sha1
```

**Vermerk zu den 37 Refs — es sind keine zusätzlichen Commits darin.** Die Zahl setzt
sich abschließend so zusammen:

| Ref | Anzahl | zeigt auf |
|---|---|---|
| `refs/heads/main` | 1 | `0d65104` |
| `refs/tags/baseline` | 1 | `0d65104` |
| `refs/tags/inj/NN` | 32 | die 32 Injektions-Commits |
| `HEAD` | 1 | `0d65104` |
| `refs/remotes/origin/HEAD`, `refs/remotes/origin/main` | 2 | `0d65104` |
| **Summe** | **37** | — |

Vier der 37 Refs (`main`, `baseline`, `HEAD` und die zwei `origin/*`) zeigen auf
**denselben** Commit `0d65104`. Die Gesamtmenge der Commits im Bundle ist damit
**5 Baucommits + 32 Injektions-Commits = 37 Commits**; **kein Commit ohne Ref, kein Ref
ohne Zweck**.

## Push-Stand am 25.08.2026 — Tags und `main` liegen auf `origin`

```
$ git ls-remote --tags origin | grep -c 'inj/'
32

$ git ls-remote origin refs/heads/main
0d651041ed87dd03f2f78359713633fac01c0a66	refs/heads/main
```

**32 von 32 Tags sind auf `origin` bestätigt**, und `main` steht dort auf demselben SHA
wie lokal. Die 32 lokalen Tag-SHAs sind mit den 32 entfernten zeichengleich (Abgleich
über die sortierten SHA-Listen, kein Unterschied).

Dies zieht den Vermerk „**Nicht gepusht**" nach, den `c4b_bericht_injektionen.md` (Kopf
und §8.9) führt: der Push ist **nach** Abschluss jenes Berichts erfolgt. Damit gilt für
das Testrepo dasselbe wie für den Checker — das Bundle sichert gegen **Zugriffsverlust**,
nicht gegen Datenverlust.

## Geheimnis-Kontrolle

Die 32 Commits berühren **ausschließlich `.py`-Dateien** unterhalb `src/depot`; `README.md`
und `.gitignore` stehen in keinem der 32 Diffs (`c4b_bericht_injektionen.md` §8.9).
Gegenprobe über die Bäume aller 32 Injektions-Commits:

| Prüfung | Ergebnis |
|---|---|
| Dateiendungen aller 32 Diffs | **ausschließlich `.py`** |
| `grep -Ei '(^\|/)\.env\|secret\|credential\|\.pem$'` über alle 32 Bäume | **kein Treffer** |

Der Befund der Baseline-Sicherung oben gilt damit unverändert fort.

## Wiederherstellung

```
git clone ma-conformance-testrepo-injections.bundle ma-conformance-testrepo
cd ma-conformance-testrepo && git checkout inj/16     # oder baseline, oder inj/NN
```

`git clone` überträgt die Tags mit; nur so sind die 32 Injektionsstände erreichbar
(siehe HINWEIS oben).

## Abgrenzung — dies ist NICHT der Freeze-Stand

**C5 steht aus.** Auch dieses Bundle ist eine Vorsicherung; es ersetzt die zitierfähige
Freeze-Referenz nicht. Und wie oben: `data/testrepo/` sichert das **Testrepo**
(`--base 0d65104`), `data/checker/` den **Checker** (`checker_git_head`). Die beiden
dürfen nicht verwechselt werden.
