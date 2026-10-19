# BI-APS – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1666696728950

Karty Anki: 1666696728950
GUID: v]~UD,,)bp; štítky: bi-aps::p06.

Metadata původního zdroje pro kartu 1666696728950: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Rozdělte pamět podle použítí v počítači.

### Odpověď (Back)

Podle využití v počítači rozlišujeme následující typy paměti:

- **primární **(hlavní, operační) - spuštěné programy a data operačního systému nebo uživatele, realizována DRAM;

- **sekundární **(vedlejší, vnější, odkládací) - trvalé uchování dat a programů operačního systému nebo uživatele, permanentní, realizována HDD nebo SSD.

Pro akceleraci přístupu k primární paměti se používá **skrytá paměť** (cache memory).

## Poznámka Anki 1666696924643

Karty Anki: 1666696924643
GUID: B;?[bpT`zd; štítky: bi-aps::p06 bi-ib::06.

Metadata původního zdroje pro kartu 1666696924643: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište hierarchickou paměť.

### Odpověď (Back)

Hierarchická paměť je způsob uspořádání paměti s cílem dosažení ideálního poměru ceny, rychlosti a kapacity, které stojí na principech prostorové a časové lokality. Nejrychlejší, ale zároveň nejmenší paměti jsou umístěny poblíž procesoru a se vzrůstající vzdáleností od procesoru se zvyšuje kapacita, ale snižuje rychlost. Tímto způsobem se minimalizuje latence spojená s přístupem do hlavní paměti, protože procesor pracuje primárně s rychlou skrytou pamětí. Bězně se používá následující uspořádání:

 [Obrázek: paste-3c52523c6d1d0e0356e9d0c758c3293d06872b2f.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1666697246535

Karty Anki: 1666697246535
GUID: x-<QLt+I;A; štítky: bi-aps::p06 bi-ib::05 bi-ib::06 bi-spol::18.

### Otázka (Front)

Popište princip časové a prostorové lokality.

### Odpověď (Back)

**Princip časové lokality** říká, že data, ke kterým bylo přistupováno nedávno, budou opět brzy používána. **Princip prostorové lokality **tvrdí, že k datům v okolí těch dat, která jsou aktuálně používána, bude brzy také přistupováno.

## Poznámka Anki 1666697407183

Karty Anki: 1666697407183
GUID: r/[@*.:?%/; štítky: bi-aps::p06 bi-ib::05 bi-ib::06.

### Otázka (Front)

Definujte skrytou paměť (cache).

### Odpověď (Back)

Skrytá paměť (cache) je uživatelskému programu neviditelná paměť, kterou používá runtime systém pro ukládání opakovaně použtých dat nebo instrukcí blíže procesoru. Bývá integrována uvnitř procesoru a realizována pomocí SRAM.

## Poznámka Anki 1666697504172

Karty Anki: 1666697504172
GUID: r5s1Zcuj{7; štítky: bi-aps::p06 bi-ib::05.

### Otázka (Front)

Definujte cache block.

### Odpověď (Back)

Cache block je souvislý a nedělitelný úsek hlavní paměti, který lze přenést do cache během jedné paměťové transakce.

## Poznámka Anki 1666699370977

Karty Anki: 1666699370977
GUID: g{5qC/Cnl7; štítky: bi-aps::p06 bi-ib::05.

Metadata původního zdroje pro kartu 1666699370977: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište přímo mapovanou skrytou paměť (cache) a zakreslete její schéma.

### Odpověď (Back)

Přímo mapovaná skrytá paměť (cache) je typ cache, který obsahuje pouze jednu cestu. Pro každý blok hlavní paměti tedy existuje právě jeden blok cache, do kterého se může mapovat. Z tohoto důvodu není přímo mapovaná cache odolná proti kolizím.

 [Obrázek: paste-7bc030b40e4984c2dfc3d3f03dce3aa4118f698a.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1666699727502

Karty Anki: 1666699727502
GUID: G>k|9Q/5q/; štítky: bi-aps::p06 bi-ib::05.

Metadata původního zdroje pro kartu 1666699727502: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište částečně asociativní skrytou paměť (cache) a zakreslete její schéma.

### Odpověď (Back)

Částečně asociativní skrytá paměť (cache) je typ cache, která obsahuje \(A\) cest ( \(A\) instancí přímo mapované cache). Pro každý blok hlavní paměti tedy existuje právě \(A\) bloků cache v rámci jednoho setu, do kterého se může mapovat. Z tohoto důvodu dokáže cache odolat \(A\) kolízím. Schéma částečně asociativní dvoucestné cache je následující:

 [Obrázek: paste-7605158601f6dd606e728ab7bb9445c3faf7d9ca.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1666699906241

Karty Anki: 1666699906241
GUID: JoT0vW//,H; štítky: bi-aps::p06 bi-ib::05.

Metadata původního zdroje pro kartu 1666699906241: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište plně asociativní skrytou paměť (cache) a zakreslete její schéma.

### Odpověď (Back)

Plně asociativní skrytá paměť (cache) je typ cache, která obsahuje stejný počet cest jako bloků. Skládá se tedy z jediného setu, a proto je nutné si jako tag ukládat celou adresu bloku z hlavní paměti. Plně asociativní cache poskytuje maximální možnou odolnost proti kolizím.

 [Obrázek: paste-94564e1f94419ea67c6be4ac9b9896f72e1201ab.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1666700006921

Karty Anki: 1666700006921
GUID: zU#gbsKU}:; štítky: bi-aps::p06 bi-ib::05.

### Otázka (Front)

Popište obecnou strukturu skryté paměti (cache) a zakreslete její schéma.

### Odpověď (Back)

Skrytá paměť (cache) se skládá z následujících složek:

- **cesta** (way) - instance cache, jejich počet značíme \(A\) a nazýváme stupněm asociativity;

- **řádek** (set) - sada \(A\) bloků, do kterých se může mapovat konkrétní blok hlavní paměti;
- **blok **(block) - obsahuje zkopírovaný blok hlavní paměti, dělí se na slova (words).

Pro mapování konkrétního bloku paměti do cache se použije výraz

\[\texttt{set} = \frac {\texttt{main memory address}} {\texttt{cache block size}} \pmod {\texttt{count of sets}}\]O tom, do které cesty bude blok namapován se rozhodne na základě obsazenosti a algoritmů pro nahrazování bloků cache. Tímto způsobem vzniká rozklad hlavní paměti do tříd ekvivalence na základě toho, do jakého setu se mapují. Nicméně protože je velikost hlavní paměti podstatně větší než velikost cache může se několik bloků mapovat do stejného setu. Proto je nutné pro identifikaci každého bloku ukládat část jeho adresy v hlavní paměti (**tag**).

 [Obrázek: paste-e4970463e18e07c85cb76cc6ae3b9f1fe52cb4fb.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1666707680634

Karty Anki: 1666707680644
GUID: jY[W#L~L$k; štítky: bi-aps::p06 bi-ib::05.

### Otázka (Front)

Popište obsah řádku skryté paměti (cache).

### Odpověď (Back)

Řádek skryté paměti (cache) obsahuje:

- **data** - slovně dělený blok hlavní paměti;

- **tag** - část adresy dat z hlavní paměti;

- **řídící bity**:

- dirty (\(\mathtt D\)) - nastaven, pokud se data v cache liší od dat v hlavní paměti;

- validity** **(\(\texttt V\)) - nastaven, pokud jsou data platná.

## Poznámka Anki 1666707850569

Karty Anki: 1666707850569
GUID: m5*<7|Hi}6; štítky: bi-aps::p06 bi-ib::05.

Metadata původního zdroje pro kartu 1666707850569: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište vliv stupně asociativity, velikosti bloku a velikosti skryté paměti na skrytou paměť (cache).

### Odpověď (Back)

Uvedené parametry mají následující vliv na skrytou paměť (cache):

- **stupeň asociativity** - počet kolizí, kterým je cache schopna odolat;

- **velikost bloku** - míra podpory principu prostorové lokality;

- **velikost cache** - je přímo úměrná hit rate, ale negativně ovlivňuje hit time.

## Poznámka Anki 1666708114082

Karty Anki: 1666708114083
GUID: bEy$}]ow+c; štítky: bi-aps::p06 bi-ib::05.

Metadata původního zdroje pro kartu 1666708114083: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište strategie odstraňování bloků skryté paměti (cache).

### Odpověď (Back)

Existují následující strategie ostraňování bloků skryté paměti (cache):

- **pseudonáhodná**:

- odstraní náhodný blok;
- jednoduchá implementace;

- **least recently used **(LRU):

- odstraní nejdéle nepoužitý blok;
- implementace je náročná na hardware, používá se jednodušší **pseudo-LRU**;

- **least frequently used **(LFU):

- odstraní nejméně používaný blok;
- u každého bloku je nutné ukládat informaci o četnosti jeho použití;
- samotná se nepoužívá;

- **adaptive replacement cache **(ARC):

- typicky kombinace LRU, LFU.

## Poznámka Anki 1666708263214

Karty Anki: 1666708263214
GUID: pkj1r,F/&%; štítky: bi-aps::p06 bi-ib::05.

Metadata původního zdroje pro kartu 1666708263214: v původním balíčku pozastavená karta.

### Otázka (Front)

Rozdělte skrytou paměť (cache) podle způsobu zápisu dat do hlavní paměti.

### Odpověď (Back)

Podle způsobu zápisu dat do hlavní paměti rozlišujeme:

- **write-through cache** - všechny zápisy do cache se současně zapisují do hlavní paměti,

- **write-back cache** - zápisy do cache nastavují příznak dirty (\(\texttt D\)) a k zápisu do hlavní paměti dochází až v okamžiku odstraňování dirty bloku z cache.

## Poznámka Anki 1666710184710

Karty Anki: 1666710184710
GUID: x]_$j3JlmZ; štítky: bi-aps::p06 bi-ib::05.

Metadata původního zdroje pro kartu 1666710184710: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište zápisovou frontu (write buffer) skryté paměti (cache).

### Odpověď (Back)

Zápisová fronta (write buffer) skryté paměti (cache) snižuje zátěž sběrnice pro write-through cache a pro write-back cache snižuje dobu jejího výpadku, protože:

- **write-through cache** - zápisy jsou ve write bufferu seskupeny a zapisovány hromadně,

- **write-back cache **- při výpadku lze zápis odstraňovaného bloku přenechat na write bufferu a ihned začít číst z hlavní paměti.

