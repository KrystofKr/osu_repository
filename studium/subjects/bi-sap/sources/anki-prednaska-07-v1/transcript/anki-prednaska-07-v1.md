# BI-SAP – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-sap/BI-SAP.apkg; APKG SHA-256 1f67b9282d55c6e8fb096f86041a008a959b3ade7ab78b051bce1ceb2cf0a3bd. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 624f9e0b4061e0e62a0e80089c16bfc9c700ec35ffa2dae8f3cc15f23be9a383.
Původní balíčky: BI-SAP
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1648555459528

Karty Anki: 1648555459528
GUID: g,R9?1V%1z; štítky: bi-sap::otazky07 bi-sap::p07.

Metadata původního zdroje pro kartu 1648555459528: v původním balíčku pozastavená karta.

### Otázka (Front)

Zakreslete schéma pro rozšíření řádové mřížky pro doplňkový kód.

### Odpověď (Back)

[Obrázek: paste-14c40d9f2179fcca9a76b6c11b9960e259a84056.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1648555604664

Karty Anki: 1648555604665
GUID: fQ2#S5viu?; štítky: bi-sap::otazky07 bi-sap::p07.

Metadata původního zdroje pro kartu 1648555604665: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak se rozšiřuje řádová mřížka pro čísla bez znaménka?

### Odpověď (Back)

Zleva se doplní nulami.

## Poznámka Anki 1648555639227

Karty Anki: 1648555639227
GUID: k)@To&Lm]h; štítky: bi-sap::otazky07 bi-sap::p07.

Metadata původního zdroje pro kartu 1648555639227: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak se rozšiřuje řádová mřížka pro přímý kód.

### Odpověď (Back)

Znaménko (první bit) se zkopíruje a doplňují se nuly.

## Poznámka Anki 1648560409575

Karty Anki: 1648560409577
GUID: ijcE>JK2lG; štítky: bi-sap::otazky07 bi-sap::p07 bi-spol::30 ni-spol::05.

### Otázka (Front)

Popište reprezentaci čísel v pohyblivé řádové čárce (floating point) podle IEEE 754.

### Odpověď (Back)

Podle IEEE 754 jsou čísla s pohyblivou řádovou čárkou (floating point) reprezentována v podobě:
\[(-1)^s \cdot m \cdot 2^{e - b}, \]kde:

- \(s \in \{ 0, 1 \}\) je znaménko (signum),

- \(m\) je mantisa (signifikant) v přímém kódu,

- \(2\) je základ (base),

- \(e\) je exponent v aditivním kódu s konstantou \(b\) (bias).

### Doplňující pole (Extra)

Délka exponentu \(e\) jakožto binárního řetězce je značena \(d\).

## Poznámka Anki 1648560531966

Karty Anki: 1648560531966
GUID: A`T.CkR/o*; štítky: bi-sap::otazky07 bi-sap::p07 bi-spol::30 ni-spol::05.

### Otázka (Front)

Popište normalizovaná a subnormální čísla v pohyblivé řádové čárce (floating point) a princip skryté jedničky podle IEEE 754.

### Odpověď (Back)

Číslo v pohyblivé řádové čárce (floating point) nazveme **normalizované**, jestliže \(e \in (0, 2^d - 1)\). Jeho hodnotu pak získáme jako\[(-1)^s \cdot (1.m_2)_2 \cdot 2^{e - b}.\]V tomto tvaru bude první bit mantisy vždy jednička, proto není nutné tuto jedničku ukládat, čímž vzniká tzv. **skrytá jednička**. **Subnormální** číslo v pohyblivé řádové čárce je číslo, pro které platí \(e = 0\) a \(m \neq 0\). Jeho hodnotu získáme jako\[(-1)^s \cdot (0.m_2)_2 \cdot 2^{1 - b}.\]

### Doplňující pole (Extra)

Číslo v pohyblivé řádové čárce je v normalizovaném tvaru, pokud mantisu již nelze posunout více doleva. Symbol \(m_2\) značí binární reprezentaci mantisy (signifikantu) a \(.\) je zde chápána jako binární tečka.

## Poznámka Anki 1648560995034

Karty Anki: 1648560995035
GUID: Fu3k:u2$Ik; štítky: bi-sap::otazky07 bi-sap::p07 bi-spol::30 ni-spol::05.

### Otázka (Front)

Popište mezní případy čísel v pohyblivé řádové čárce (floating point) podle IEEE 754.

### Odpověď (Back)

Norma IEEE 754 definuje následující mezní případy čísel v pohyblivé řádové čárce (floating point):

| 
      **exponent** | 
      **mantisa** | 
      **hodnota** | 

| 
      \(e = 2^d - 1\)
 | 
      \(m \neq 0\)
 | 
      \(x = \texttt{NaN}\)
 | 

| 
      \(e = 2^d - 1\) | 
      \(m = 0\)
 | 
      \(x = (-1)^s \cdot \infty\)
 | 

| 
      \(e = 0\) | 
      \(m = 0\)
 | 
      \(x = (-1)^s \cdot 0\)
 |

## Poznámka Anki 1717260602280

Karty Anki: 1717260602280
GUID: tarS]PCe<E; štítky: bi-sap::p07 bi-spol::30.

Metadata původního zdroje pro kartu 1717260602280: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište artimetické operace s čísly v pohyblivé řádové čárce (floating point).

### Odpověď (Back)

Aritmetické operace s čísly v pohyblivé řádové čárce (floating point) probíhají následovně:

- **sčítání a odčítání** - srovnání exponentu a sčítání nebo odečítání mantis,
- **násobení** - sečtení exponentů a násobení mantis,

- **dělení** - odečtení exponentů a dělení mantis,

- **porovnání **- srovnání exponentů a porovnání mantis,

- **posuv** - posuv mantisy nebo zvětšení či zmenšení exponentu.

