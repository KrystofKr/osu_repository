# BI-OSY – Přednáška 12

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-osy/BI-OSY.apkg; APKG SHA-256 e601d54cae58e1923ab743a64796ef89ec49f6bcd52ac062288890242af207fc. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b95b42cacacaa5de70f8162d09b00582086c2fd5b59f3a299e3fc9531a688ab6.
Původní balíčky: BI-OSY
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1684327166976

Karty Anki: 1684327166976
GUID: Aqh1Jh3z,n; štítky: bi-osy::p12.

Metadata původního zdroje pro kartu 1684327166976: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to virtual file system (VFS)?

### Odpověď (Back)

Virtual file system je vrstva jádra OS, která je nezávislá na konkrétní implementaci filesystému a poskytuje rozhraní mezi ním a procesy, které v OS běží.

 [Obrázek: paste-fdad8894ea21fd08db4d51838f8aecd9bfa552d9.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1684327464728

Karty Anki: 1684327464728
GUID: HEaEM_8y9]; štítky: bi-ib::02 bi-osy::p12.

Metadata původního zdroje pro kartu 1684327464728: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to Filesystem in Userspace (FUSE)?

### Odpověď (Back)

Filesystem in Userspace (FUSE) je rozhraní, které umožňuje neprivilegovaným uživatelům vytvářet své vlastní filesystémy bez nutnosti modifikovat jádro OS. Skládá se ze dvou částí:

- **modul jádra OS** - samotná implementace FUSE,

- **knihovna **- rozhraní modulu.

## Poznámka Anki 1684328465862

Karty Anki: 1684328465862
GUID: q44PRAI$$&; štítky: bi-osy::p12.

Metadata původního zdroje pro kartu 1684328465862: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakými způsoby se optimalizuje přístup do filesystému?

### Odpověď (Back)

Přístup do filesystému lze optimalizovat následujícími způsoby:

- **block cache nebo page cache** - skrytá paměť nedávno používaných datových bloků,
- **Directory Name Look-up Cache** - skrytá paměť nedávno používaných souborů a adresářů,

- **Block Read Ahead** - přednačítání datových bloků podle principu prostorové lokality.

## Poznámka Anki 1684329139360

Karty Anki: 1684329139361
GUID: G%^)gNW|SD; štítky: bi-ib::02 bi-osy::p12.

### Otázka (Front)

Co je to journaling filesystem?

### Odpověď (Back)

Journaling filesystem je filesystém, který do speciální oblasti journal zapisuje záznamy o plánovaných transakcích. Poté co dojde k jejich úspěšnému provedení, jsou z journalu zase odebrány. Pokud se filesystém dostane do nekonzistentního stavu, stačí přehrát operace z journalu.

## Poznámka Anki 1684330393615

Karty Anki: 1684330393615
GUID: O+3u=v8OYS; štítky: bi-osy::p12.

Metadata původního zdroje pro kartu 1684330393615: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište B-strom řádu \(n\).

### Odpověď (Back)

B-strom řádu \(n\) se skládá z uzlů, které jsou tvořeny posloupností \([p_0, k_1, d_1], [p_1, k_2, d_2], \dots [p_{n - 1}, k_n, d_n] \), kde

- \(p_i\) odkazuje na podstrom uzlů, pro jejichž klíče \(c\) platí, že \(k_i < c < k_{i + 1}\);

- \(k_i\) je klíč ukládaných dat,

- \(d_i\) jsou ukládaná data.

 [Obrázek: paste-70952a536dfd7efdf58c847170b90a022df901b1.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1684330451332

Karty Anki: 1684330451332
GUID: Kz@VF2<9(J; štítky: bi-osy::p12.

Metadata původního zdroje pro kartu 1684330451332: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište B+ strom.

### Odpověď (Back)

B+ strom má stejnou strukturu jako B strom s tím rozdílem, že vnitřní uzly ukladají pouze klíče a odkazy na podstromy a data najdeme až v listech.

