# BI-BEK – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1679500091133

Karty Anki: 1679500091133
GUID: jIA+DDQ>$q; štítky: bi-bek::p04 bi-ib::08.

### Otázka (Front)

Popište možné cíle útoku přetečení bufferu (buffer overflow) na haldě.

### Odpověď (Back)

Mezi možné cíle přetečení bufferu (buffer overflow) na haldě patří přepsání:

- ukazatele na tabulku virtuálních metod (VMT) instance třídy,
- alokační struktury tak, že správce paměti přepíše paměť procesu předvídatelným způsobem, který umožní spustit kód útočníka.

## Poznámka Anki 1679501623316

Karty Anki: 1679501623316
GUID: o?B8ALK^,7; štítky: bi-bek::p04 bi-ib::08 bi-spol::19.

### Otázka (Front)

Zjednodušeně popište proces alokace paměti.

### Odpověď (Back)

1. Alokační velikost je zaokrouhlena na nejbližší vyšší násobek 8 bytů.
2. Pokud jde o první volání alokačních funkci, inicializuje se halda.
3. Je zvolena aréna alokace. Pokud neexisuje, je vytvořena.
4. S ohledem na příznaky arény je vybrán rychlý nebo normální bin.
5. Bin je prohledán na uvolněný chunk odpovídající velikosti.
6. Pokud je nalezen, je vyjmut z koše, jinak se oddělí z kusu \(\mathtt{top}\).
7. Chunk je označen jako používaný a adresa je vrácena uživateli.

## Poznámka Anki 1679502155130

Karty Anki: 1679502155130
GUID: eQ$p@BlFxC; štítky: bi-bek::p04 bi-ib::08 bi-spol::19.

### Otázka (Front)

Zjednodušeně popište proces dealokace paměti.

### Odpověď (Back)

1. Vybere se aréna, do které blok paměti patří.
2. Určí se lokace chunku v aréně.
3. Pokud jde o poslední chunk, který je následován \(\mathtt{top}\), je chunk přidán k \(\mathtt{top}\) a funkce končí.
4. Jinak se vybere odpovídající bin.
5. Chunk je označen jako uvolněný a je zařazen do binu.
6. Pokud se jedná o normální bin, proběhně kontrola, zda některý ze sousedů chunku není uvolněn. Pokud ano, jsou spojeny do většího chunku.

## Poznámka Anki 1679502413732

Karty Anki: 1679502413732
GUID: jCq23rD8TA; štítky: bi-bek::p04 bi-ib::08 bi-spol::19.

### Otázka (Front)

Co je to aréna, chunk (kus), bin (koš) a \(\mathtt{top}\)?

### Odpověď (Back)

**Aréna **je souvislý blok lineární paměti, na které se dělí halda. Aréna se dále dělí na chunky. Jeden **chunk **reprezentuje jeden paměťový blok alokovaný aplikací. **Bins** jsou pole spojových seznamů chunků, které poskytují úložiště pro v minulosti alokované a uvolněné kusy. Ukazatel \(\mathtt{top}\) ukazuje na blok nealokované paměti arény, která neleží v žádném binu.

## Poznámka Anki 1679525026588

Karty Anki: 1679525026588
GUID: j43ht]^ifR; štítky: bi-bek::p04 bi-ib::08.

### Otázka (Front)

Popište přetečení bufferu (buffer overflow). Kde k němu může docházet?

### Odpověď (Back)

Přetečení bufferu (buffer overflow) je typ zranitelnosti, kdy dojde k přepsání obsahu paměti za koncem bufferu. Typicky vzniká jako důsledek neodstatečného ošetření vstupu, které umožní, aby do bufferu bylo zapsáno více dat, než je jeho kapacita. K přetečení bufferu může dojít na:

- **zásobníku** - zneužívá toho, že na zásobníku jsou uloženy jak lokální proměnné, argumenty funkcí a uložené hodnoty registrů, tak návratové adresy;

- **haldě** - zneužívá toho, že na haldě jsou uložena jak uživatelská data, tak alokační struktury správce paměti (na jeho implementaci je zneužití přetečení na haldě silně závislé).

## Poznámka Anki 1679525204798

Karty Anki: 1679525204798
GUID: Cp0J3F6tno; štítky: bi-bek::p04 bi-ib::08 bi-spol::19.

### Otázka (Front)

Jaké je riziko double-free?

### Odpověď (Back)

Chování po double-free není sice definované, ale v praxi se stane, že je stejný chunk umístěn do jednoho binu dvakrát. V takovém případě lze první kopii chunku alokovat, vhodně ji upravit pro exploit a následně alokovat kopii druhou. To vede ke spuštění chyby v makru \(\mathtt{unlink}\) bez nutnosti přetečení na haldě.

## Poznámka Anki 1718540152526

Karty Anki: 1718540152526
GUID: ij]4Y(/o-d; štítky: bi-bek::p04 bi-ib::08.

### Otázka (Front)

Popište chybu v makru \(\texttt{unlink}\).

### Odpověď (Back)

Makro \(\texttt{unlink}\) se používá pro vyjímání chunků z binu. Chyba spočívala v tom, že \(\texttt{unlink}\) předpokládal, že stav binu (jakožto spojového seznamu) je korektní, a neověřoval jeho obsah. V případě, že se útočníkovi podařilo strukturu binu narušit, např. pomocí buffer overflow, a následně \(\texttt{unlink}\) spustit, došlo k zápisu na libovolnou adresu v paměti. V současnoti je chyba již opravena.

