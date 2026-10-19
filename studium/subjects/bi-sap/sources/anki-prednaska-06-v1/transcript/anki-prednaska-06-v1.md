# BI-SAP – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-sap/BI-SAP.apkg; APKG SHA-256 1f67b9282d55c6e8fb096f86041a008a959b3ade7ab78b051bce1ceb2cf0a3bd. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 624f9e0b4061e0e62a0e80089c16bfc9c700ec35ffa2dae8f3cc15f23be9a383.
Původní balíčky: BI-SAP
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1648935307924

Karty Anki: 1648935307924
GUID: xB>a/ox~.q; štítky: bi-sap::otazky06 bi-sap::p06.

Metadata původního zdroje pro kartu 1648935307924: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to výpujčka, jaký má vztah k přenosu a kdy se používá?

### Odpověď (Back)

Mezi přenosem a výpůjčkou platí vztah negace. Uplatní se při odečítání větších čísel než je šířka aritmetické jednotky procesoru.

## Poznámka Anki 1651350604952

Karty Anki: 1651350604952
GUID: DaV$djQA,*; štítky: bi-sap::otazky06 bi-sap::p06 bi-sap::test02.

Metadata původního zdroje pro kartu 1651350604952: v původním balíčku pozastavená karta.

### Otázka (Front)

Co znamená predikce přenosu? Uveďte vzorce.

### Odpověď (Back)

Pomocí kombinační logiky lze předvídat, kdy přenos na sčítačce vzniká (generate - \(G\)) a kdy se šíří (propagate - \(P\)).
\(G = ab\) a \(P = a \oplus b\), kde \(a\) a \(b\) jsou vstupy sčítačky.

## Poznámka Anki 1717253793263

Karty Anki: 1717253793263
GUID: unj`(H>XW/; štítky: bi-sap::p06 bi-spol::30.

Metadata původního zdroje pro kartu 1717253793263: v původním balíčku pozastavená karta.

### Otázka (Front)

Zakreslete schéma paralelní sčítačky a odčítačky v doplňkovém kódu.

### Odpověď (Back)

Schéma paralelní sčítačky a odčítačky v doplňkovém kódu je následující:

 [Obrázek: paste-5305ed38de7595a15b176b32d5258a3ea5b1eb7d.jpg; soubor je v media/ v doprovodném ZIP] 

Přičemž:

- \(a_i\) a \(b_i\) jsou vstupy sčítačky a odčítačky,

- \(s\) je \(\texttt 0\) pokud se má sčítat a \(\texttt 1\) pokud se má odečítat,

- \(\textstyle \sum\) označuje jednobitovou sčítačku,

- \(c\) je výstupní přenos (carry),

- \(o\) je přeplnění (overflow),

- \(f_i\) jsou výstupy čítačky.

## Poznámka Anki 1717254005790

Karty Anki: 1717254005790
GUID: jp,i0`nE$P; štítky: bi-sap::p06 bi-spol::30.

### Otázka (Front)

Popište typy posuvů v řádové mřížce.

### Odpověď (Back)

Rozlišujeme následující typy posuvů v řádové mřížce:

- **logický** - přeplnění se ignoruje, na uvolněná místa se vkládají nuly;

- **cyklický** - na uvolněná místa se vkládá přeplnění;
- **aritmetický** - operace odpovídající dělení a násobení, detekce přeplnění a ztráty přesnosti.

## Poznámka Anki 1717255213950

Karty Anki: 1717255213950
GUID: v2[l$+g]t?; štítky: bi-sap::p06 bi-spol::30.

Metadata původního zdroje pro kartu 1717255213950: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište realizaci aritmetického posuvu v doplňkovém kódu.

### Odpověď (Back)

**Posuv vlevo v doplňkovém kódu** realizujeme následovně:

 [Obrázek: paste-7df9e50d4a8f728f84921afadb3bf1a98448dada.jpg; soubor je v media/ v doprovodném ZIP] 

Přičemž \(o\) označuje přeplnění (overflow). **Posuv vpravo v doplňkovém kódu** realizujeme následovně:

 [Obrázek: paste-9d2d1c0cfb92b08a78913b4212b2b44c9c78811e.jpg; soubor je v media/ v doprovodném ZIP] 

Přičemž \(z\) označuje ztrátu přesnosti.

## Poznámka Anki 1717255446750

Karty Anki: 1717255446750
GUID: PB$F>el%pg; štítky: bi-sap::p06 bi-spol::30.

Metadata původního zdroje pro kartu 1717255446750: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište realizaci aritmetického posuvu v přímém kódu.

### Odpověď (Back)

**Posuv vlevo v přímém kódu** realizujeme následovně:

 [Obrázek: paste-ad4ef2740a18a8e347f60354e8538d72f4dc64a5.jpg; soubor je v media/ v doprovodném ZIP] 

Přičemž \(o\) označuje přeplnění (overflow). **Posuv vpravo v přímém kódu** realizujeme následovně:

 [Obrázek: paste-59f01416d6f6894cca5dfe125b0d5c99a8df297b.jpg; soubor je v media/ v doprovodném ZIP] 

Přičemž \(z\) označuje ztrátu přesnosti.

