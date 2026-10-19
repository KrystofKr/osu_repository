# BI-APS – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1667834898258

Karty Anki: 1667834898258
GUID: pGZH1Bj5l>; štítky: bi-aps::p08.

### Otázka (Front)

Rozdělte multiprocesorové systémy.

### Odpověď (Back)

- **systémy se sdílenou pamětí **(Shared Memory Systems)

- běží jedna instance OS (společné plánování)
- výhody: snazší programování

- **systémy s oddělenou pamětí **(Distributed Memory Systems)

- na každém uzlu běží jiná instance OS
- komunikace mezi uzly je podpořena sítěmi s nízkou latencí a probíhá pomocí knihoven jako MPI (Message Passing Interface)
- výhody: méně náročné na HW, snazší škálování

## Poznámka Anki 1667835335354

Karty Anki: 1667835335354
GUID: OlI[NCipOr; štítky: bi-aps::p08.

### Otázka (Front)

Rozdělte multiprocesorové systémy se sdílenou pamětí (shared memory systems).

### Odpověď (Back)

Multiprocesorové systémy se sdílenou pamětí (shared memory systems) se dělí na:

- **systémy se sdílenou fyzickou pamětí** - centralizovaná paměť;

- **systémy s oddělenou fyzickou pamětí** - každý uzel má vlastní paměť, ale může přistupovat i do paměti ostatních uzlů.

Proto se časy přístupu do paměti mohou lišit. Z tohoto hlediska dělíme systémy se sdílenou pamětí dále na:

- **uniform memory access **(UMA) **systémy **- čas přístupu je stejný pro všechny procesory a všechny adresy;

- **non-uniform memory access (NUMA) systémy** - čas přístupu se odvíjí od procesoru a adresy.

## Poznámka Anki 1667835410042

Karty Anki: 1667835410042
GUID: k{ck,ZE1g!; štítky: bi-aps::p08.

### Otázka (Front)

Definujte symetrický multiprocesor (SMP).

### Odpověď (Back)

Symetrický multiprocesor je multiprocesorový výpočetní systém, který používá identické procesory a jedinou centrální sdílenou paměť. SMP je tedy zároveň UMA SMS.

## Poznámka Anki 1667836238927

Karty Anki: 1667836238927
GUID: Dr|JwU,H1E; štítky: bi-aps::p08.

### Otázka (Front)

Definujte kohererentní paměťový systém.

### Odpověď (Back)

Řekneme, že multiprocesorový paměťový systém je koherentní, jestliže výsledek jakéhokoli provádění programu je takový, že pro každé paměťové místo (přesněji adresu) je možné sestavit myšlené sériové pořadí operací \(\mathtt{Read}\) a \(\mathtt{Write}\) nad tímto paměťovým místem a platí, že

- paměťové operace nad daným paměťovým místem spuštěné daným procesorem se v paměti provedou v pořadí, ve kterém byly tímto procesorem spuštěny.
- hodnoty vrácené každou operací \(\mathtt{Read}\) jsou hodnotami v tomto sériovém pořadí naposledy provedené operace \(\mathtt{Write}\) do daného paměťového místa.

## Poznámka Anki 1667837199764

Karty Anki: 1667837199764
GUID: Cby=yyW.2m; štítky: bi-aps::p08.

### Otázka (Front)

Jak se implementují koherenční porotokoly založené na odposlechu (snooping) (KPO)?

### Odpověď (Back)

- Jádra jsou se sdílenou pamětí propojena sdílenou sběrnící.
- Řadiče SP jader jsou doplněny o HW, který sleduje dění a sběrnici a

- deketuje relevantní transakce (s bloky, jejichž kopie daná SP obsahuje),
- akutalizuje stavové příznaky relevantních bloků dat,
- pro ostatní řadiče generuje transakce na sběrnici.

## Poznámka Anki 1667837261054

Karty Anki: 1667837261054
GUID: cSrw!u<sBl; štítky: bi-aps::p08.

### Otázka (Front)

Jaké existují přístupy k zajištění koherence paměti?

### Odpověď (Back)

- koherence založená na odposlechu/slídění na sdílené sběrnici (snooping)
- koherence založená na adresářích (directory based)

## Poznámka Anki 1667838666531

Karty Anki: 1667838666531
GUID: mwqco$r.71; štítky: bi-aps::p08.

Metadata původního zdroje pro kartu 1667838666531: v původním balíčku pozastavená karta.

### Otázka (Front)

Rozdělte koherenční protokoly založené na odposlechu (KPO).

### Odpověď (Back)

Z pohledu shody obsahu hlavní paměti a SP dělíme KPO na:

- **write-through **(WT) - zatěžuje sběrnici, nepoužívá se
- **write-back **(WB)

Z pohledu reakce ostatních SP na zápis do lokální SP dělíme KPO na:

- **invalidační **(invalidate)

- **aktualizační **(update) - zatěžuje sběrnici, nepoužívá se

## Poznámka Anki 1667839373119

Karty Anki: 1667839373119
GUID: PPQMnSGe7W; štítky: bi-aps::p08.

### Otázka (Front)

Popište MESI protokol.

### Odpověď (Back)

- MESI protokol je nejrozšířenější WB invalidační KPO:

- Modifikovaný (dirty) blok se do hlavní paměti zapíše pouze, pokud má být z SP odstraněn.
- Při zápisu do lokální SP provedou všechny dotčené řadiče SP ostatních procesorů zneplatnění relevantního bloku ve svých SP (nepřenášejí se
data).

- Každý blok v SP může být v jednom z 4 stavů:

- **modified **(\(\mathtt M\)) - Obsah bloku v této SP se liší od obsahu hlavní paměti.
- **exclusive **(\(\mathtt E\)) - Daný blok je jedině v této SP a je stejný jako v hlavní paměti.
- **shared **(\(\mathtt S\)) - Blok je stejný jako v hlavní paměti, ale nemusí být jen v této SP.
- **invalid **(\(\mathtt I\)) - Obsah bloku v této SP je neplatný.

## Poznámka Anki 1667847042909

Karty Anki: 1667847042919
GUID: Iy>7B7r^wT; štítky: bi-aps::p08.

Metadata původního zdroje pro kartu 1667847042919: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké vylepšení poskytuje MESIF oproti MESI?

### Odpověď (Back)

- Pokud výpočetní jádro požaduje blok, který je ve stavu \(\mathtt S\) a je uložen v několika SP, může každá SP reagovat a vydat tento blok.
- MESIF definuje nový stav **forwarding** (\(\mathtt F\)).
- Jenom jeden blok SP může být ve stavu \(\mathtt F\) (ten bude reagovat na sběrnici) ostatní jádra mohou mít blok ve stavu \(\mathtt S\).

## Poznámka Anki 1667847183614

Karty Anki: 1667847183614
GUID: pP:6Hjs+Hb; štítky: bi-aps::p08.

Metadata původního zdroje pro kartu 1667847183614: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké vylepšení poskytuje MOESI oproti MESI?

### Odpověď (Back)

- Pokud má být modifikovaný (dirty) block sdílen (\(\mathtt M \to \mathtt S \)), pak musí být tento blok nejdříve zapsán do paměti.
- MOESI definuje nový stav **owner** (\(\mathtt O\)).
- V tomto případě se stav modifikovaného bloku změní na \(\mathtt O\) a jeho kopie v jiných jádrech se označí \(\mathtt S\) (\(\mathtt S\) už neindikuje shodu s hlavní pamětí).
- Blok ve stavu \(\mathtt O\) se zapisuje do paměti až tehdy, kdy má být vyhozen ze SP.

## Poznámka Anki 1667851024166

Karty Anki: 1667851024166
GUID: oaAIBR!o=x; štítky: bi-aps::p08.

Metadata původního zdroje pro kartu 1667851024166: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakou roli má adresář při dodržování paměťové koherence? Jaké druhy rozeznáváme?

### Odpověď (Back)

Díky adresáři se v některých případech můžeme vyhnout broadcastu (dotazování na všechny ostatní uzly).

- **plný adresář** - binární vektor délky \(N + 1\), kde \(N\) je počet uzlů (určuje v jakém uzlu je kopie daného bloku, poslední bit je indikátor dirty/clean)

- **minimální adresář** - obsahuje pouze informaci, zda je daný blok domovského uzlu sdílen; nevýhodou je posílání **probe requestu **každému ulzu v případě, že blok je sdílen

## Poznámka Anki 1667851267936

Karty Anki: 1667851267936
GUID: rt{U:u?0}R; štítky: bi-aps::p08.

Metadata původního zdroje pro kartu 1667851267936: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak fungují ccNUMA systémy?

### Odpověď (Back)

Cache-Coherent NUMA systémy implementují adresáře uvnitř procesoru jako skrytou paměť (použitím SRAM). Adresáře jsou však omezené velikosti a nemusí pojmout všechna metadata o všech sdílených blocích v systému. Proto v případě **directory miss **budeme broadcastovat všem uzlům.

