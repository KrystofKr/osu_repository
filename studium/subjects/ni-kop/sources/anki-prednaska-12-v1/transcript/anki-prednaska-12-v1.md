# NI-KOP – Přednáška 12

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1734633929065

Karty Anki: 1734633929066
GUID: D)IJLF),O$; štítky: ni-kop::p12.

### Otázka (Front)

Popište řešitelnost instance komponované globální heuristickou metodou.

### Odpověď (Back)

Mějme instanci \(I\) problému \(\Pi\) dekomponovanou pomocí globální heuristické metody na instance \(I_1\) a \(I_2\). Potom:

- některé kompozice fungují, i když \(I_1\) nebo \(I_2\) nemá řešení (0/1 problém batohu);
- některé kompozice fungují, pouze když \(I_1\) a \(I_2\) mají řešení (problém diskrétního rozmístění).

## Poznámka Anki 1734634537069

Karty Anki: 1734634537069
GUID: i5!p,.2L0Z; štítky: ni-kop::p12.

### Otázka (Front)

Popište přibližnou dekompozici (approximate decomposition), čistou dekompozici (pure decomposition) a přesnou dekompozici (proper decomposition) globální heuristické metody. Jakou dekompozici využívá dynamické programování?

### Odpověď (Back)

Mějme instanci \(I\) problému \(\Pi\) dekomponovanou pomocí globální heuristické metody na instance \(I_1\), \(I_2\) a \(Y_1\), \(Y_2\) jejich optimální řešení. Pro **přibližnou dekompozici** (approximate decomposition) platí, že:

- kompozicí \(Y_1\) a \(Y_2\) vzniká nějaké řešení \(Y\) instance \(I\);
- pokud \(Y_1\) a/nebo \(Y_2\) neexistuje, nedokážeme o existenci \(Y\) rozhodnout.

Pro **čistou dekompozici** (pure decomposition) platí, že:

- kompozicí \(Y_1\) a \(Y_2\) vzniká optimální řešení \(Y\) instance \(I\);
- pokud \(Y_1\) a/nebo \(Y_2\) neexistuje, neexistuje ani \(Y\).

Čistou dekompozici využívá dynamické programování.** Přesná dekompozice** (proper decomposition) má stejné vlastnosti jako čistá dekompozice a navíc platí, že všechna optimální řešení \(Y\) lze složit z nějakých optimálních řešení \(Y_1\) a \(Y_2\).

### Doplňující pole (Extra)

Zda závisí na neexistenci \(Y_1\) a/nebo \(Y_2\) vyplývá z vlastností kompozice dané globální heuristické metody.

## Poznámka Anki 1734635703476

Karty Anki: 1734635703476
GUID: H1hOpxcOc}; štítky: ni-kop::p12.

Metadata původního zdroje pro kartu 1734635703476: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište dynamické programování. Uveďte příklady jeho využití.

### Odpověď (Back)

Dynamické programování je metoda návrhu algoritmů, která se stejně jako divide-and-conquer zakládá na rekurzivním rozkladu problému na podproblémy řešitelné stejným nebo podobným způsobem. Na rozdíl od divide-and-conquer však předpokládá a využívá toho, že se podproblémy v rekurzivním rozkladu opakují. Za použití memoizace lze pomocí dynamického programování dosáhnout výrazného zrychlení algoritmů. Dynamické programování lze využít při výpočtu faktoriálu, Fibonacciho posloupnosti nebo při konstrukci nejdelší rostoucí podposloupnosti.

## Poznámka Anki 1734636323111

Karty Anki: 1734636323111
GUID: v6WPxqK}Zp; štítky: ni-kop::p12.

### Otázka (Front)

Popište stupně dynamického programování.

### Odpověď (Back)

Dynamické programování lze rozdělit do stupňů, které při rekurzivní formulaci odpovídají stupňům rekurze, pokud platí aspoň jedno z následujících:

- pro výpočet instance jsou k dispozici řešení všech jejích podinstancí,
- pro výpočet instance daného stupně jsou potřeba pouze instance právě jednoho jiného stupně.

## Poznámka Anki 1734636458179

Karty Anki: 1734636458179
GUID: u#SG_^ChtL; štítky: ni-kop::p12.

### Otázka (Front)

Popište formulace dynamického programování.

### Odpověď (Back)

Dynamické programování lze formulovat dvěma způsoby:

- **rekurzivně **(zpětně)** **- vychází ze vstupní instance a dekomponuje ji až na triviální instance,

- **iterativně **(dopředně) - vychází z triviálních instancí a komponuje je až na vstupní instanci.

