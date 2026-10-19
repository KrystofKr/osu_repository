# NI-KOP – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1727632032964

Karty Anki: 1727632032964
GUID: tU$kDxMPBp; štítky: ni-kop::p02 ni-spol::12.

### Otázka (Front)

Popište experimentální vyhodnocení algoritmů.

### Odpověď (Back)

Experimentální vyhodnocení algoritmů spočívá v analýze algoritmů za účelem srovnání algoritmu s dosud známými algoritmy, porozumění nebo určení vhodnosti pro konkrétní nasazení. Typicky je předmětem analýzy:

- složitost,
- kvalita,
- závislost mezi vstupními a výstupními metrikami.

## Poznámka Anki 1727632149999

Karty Anki: 1727632149999
GUID: M%wX;eAT2D; štítky: ni-kop::p02 ni-spol::12.

### Otázka (Front)

Popište kroky experimentálního vyhodnocení algoritmu.

### Odpověď (Back)

Experimentální vyhodnocení algoritmu začíná u stanovení otázky. Samotný experiment pak probíhá následovně:

- plánování experimentu,
- provedení experimentu,
- sběr dat,
- interpretace výsledku.

Výstupem by měla být odpověď na otázkou stanovenou na začátku experimentálního vyhodnocení.

## Poznámka Anki 1727632690784

Karty Anki: 1727632690784
GUID: b9CAB*CDvX; štítky: ni-kop::p02 ni-spol::12.

### Otázka (Front)

Popište metriky experimentálního vyhodnocení algoritmů.

### Odpověď (Back)

Metriky experimentálního vyhodnocení algoritmů jsou kvantitativní veličiny, které vznikají abstrakcí vstupů a výstupů algoritmu. Používají se k interpretaci a zobecnění jednotlivých běhů algoritmu, protože cílem je nalézt závislost metrik, která se týká algoritmu obecně, nikoliv jeho konkrétních běhů s konkrétními daty. Rozlišujeme:

- **primární metriky** - měřené hodnoty,

- **sekundární metriky** - kvantitativní srovnání (průměr, medián, distribuční funkce).

## Poznámka Anki 1727635725262

Karty Anki: 1727635725262
GUID: PYYytew=}V; štítky: ni-kop::p02 ni-spol::12.

### Otázka (Front)

Popište obecné experimentální vyhodnocení algoritmu.

### Odpověď (Back)

Obecné experimentální vyhodnocení algoritmu sestává z následujících komponent:

- **generátor instancí** - generuje instance se zadanou vstupní metrikou (všechny instance by měly být stejně pravděpodobné), je zdrojem variance;

- **algoritmus** - řeší zadané instance, je měřena jeho výstupní metrika;

- **statistika a interpretace** - zkoumá výstupní metriku, potlačuje varianci v instancích.

 [Obrázek: Screenshot 2024-09-29 205343.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1727636416839

Karty Anki: 1727636416839
GUID: LJN$W`[0X@; štítky: ni-kop::p02 ni-spol::12.

### Otázka (Front)

Popište experimentální vyhodnocení randomizovaného algoritmu.

### Odpověď (Back)

Experimentální vyhodnocení randomizovaného algoritmu probíhá podobně jako obecné experimentální vyhodnocení algoritmu s tím rozdílem, že vlivem randomizace se zdrojem variance stává i samotný algoritmus. Může probíhat dvěma způsoby s následujícími specifiky:

- **na jedné instanci** - bez generátoru instancí, statistika potlačuje varianci způsobenou randomizací;

- **na sadě instancí** - s generátorem instancí, statistika potlačuje varianci způsobenou randomizací a varianci v instancích.

|  [Obrázek: paste-d82dfe6e029df62d43b40c4eb0216122f210e70c.jpg; soubor je v media/ v doprovodném ZIP] 
 |  [Obrázek: paste-40536d693e2cb21925634f409ef310a737728a1f.jpg; soubor je v media/ v doprovodném ZIP] 
 |

## Poznámka Anki 1727636718945

Karty Anki: 1727636718945
GUID: xe:H6KIj4~; štítky: ni-kop::p02 ni-spol::12.

### Otázka (Front)

Popište metriky experimentálního vyhodnocení randomizovaných algoritmů.

### Odpověď (Back)

Metriky experimentálního vyhodnocení randomizovaných algoritmů dělíme na:

- **metriky 1. fáze** - používají se pro potlačení variance způsobené randomizací,

- **metriky 2. fáze** - používají se pro potlačení variance v instancích.

### Doplňující pole (Extra)

Na metriky experimentálního vyhodnocení randomizovaných algoritmů se také aplikuje obecné dělení na primární a sekundární.

## Poznámka Anki 1727637671858

Karty Anki: 1727637671859
GUID: O%=h;e-Qq]; štítky: ni-kop::p02 ni-spol::12.

### Otázka (Front)

Popište robustní algoritmus a metodu měření robustnosti.

### Odpověď (Back)

Robustní algoritmus je algoritmus, který je konzistentní a efektivní napříč různými vstupy, a to i v případech, kdy nejsou vstupy nebo podmínky jeho běhu ideální. Měření robustnosti algoritmu sestává z následujících komponent:

- **instance** - vstupuje pouze jediná instance se zadanou vstupní metrikou,

- **náhodná perturbace **- do instance je zanesena variance (všechny perturbace by měly být stejně pravděpodobné),

- **algoritmus** - řeší zadanou instanci, je měřena jeho výstupní metrika;

- **statistika a interpretace** - zkoumá varianci vyvolanou perturbací.

 [Obrázek: paste-edaf6206b36b7f9cb88317b1a161528b142dcf14.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1727638465327

Karty Anki: 1727638465327
GUID: N,O-&%5X]-; štítky: ni-kop::p02 ni-spol::12.

### Otázka (Front)

Popište metodu Introduction, Methods, Results, and Discussion (IMRaD).

### Odpověď (Back)

Introduction, Methods, Results, and Discussion (IMRaD) je metoda udávající obecnou strukturu článku pojednávajícího o výzkumné činnosti. Používá se také při prezentaci výsledků experimentálního vyhodnocení algoritmů. Podle ní by článek měl obsahovat následující části:

- **introduction** - účel výzkumu, výzkumná otázka;

- **methods** - použité metody a důvod jejich použití, ověření korektnosti;

- **results** - výsledky výzkumu, odpověď na výzkumnou otázku;

- **discussion** - interpretace odpovědi, prostor pro budoucí výzkum.

## Poznámka Anki 1727643292619

Karty Anki: 1727643292619
GUID: D7Fn$A;f|*; štítky: ni-kop::p02 ni-spol::12.

### Otázka (Front)

Popište srovnání algoritmů na základě experimentálního vyhodnocení.

### Odpověď (Back)

Srovnání algoritmů \(A\) a \(B\) na základě experimentálního vyhodnocení můžeme provést podle:

- **parametrů statistického rozdělení** - \(A\) má všechny parametry lepší než \(B\),

- **dominance** - \(A\) je v každé instanci zadané vstupní metriky stejně dobrý nebo lepší než \(B\).

