# BI-DBS – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-dbs/BI-DBS.apkg; APKG SHA-256 2adef415f377fbe4eac7b4dd1e452577d8eedea5e207be2be6c2aeb0e90cf4eb. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7f054157e2673745662b1c45d22f99de1a01232f0420fd85b7b7f7c2b095d969.
Původní balíčky: BI-DBS
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1649694980833

Karty Anki: 1649694980834
GUID: l6uCR2R~=Q; štítky: bi-dbs::p09.

Metadata původního zdroje pro kartu 1649694980834: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to funkční závislost?

### Odpověď (Back)

Funkční závislost nastává, když hodnoty některých atributů funkčně závisí na hodnotách jiných atributů. Lze pomocí nich vyjadřovat IO. Zapisujeme
\(\mathtt{NAZEV\_K} \to \mathtt{ADRESA}\)

## Poznámka Anki 1649695491210

Karty Anki: 1649695491210
GUID: OKP(^}b^hI; štítky: bi-dbs::p09.

Metadata původního zdroje pro kartu 1649695491210: v původním balíčku pozastavená karta.

### Otázka (Front)

Vyjmenujte Armstrongova pravidla.

### Odpověď (Back)

Mějme \(R(A)\) a nechť \(X \subseteq A, Y \subseteq A, Z \subseteq A\).

1. triviální funkční závislosti - jestliže \(Y \subseteq X\), pak \(X \to Y\)
2. tranzitivita - jestliže \(X \to Y\) a \(Y \to Z\), tak \(X \to Z\)
3. kompozice pravé strany - jestliže \(X \to Y\) a \(X \to Z\), pak \(X \to YZ\)
4. dekompozice pravé strany - jestliže \(X \to YZ\), pak \(X \to Y\) a \(X \to Z\)

## Poznámka Anki 1649695676264

Karty Anki: 1649695676265
GUID: GTh1;a1Xxz; štítky: bi-dbs::p09.

Metadata původního zdroje pro kartu 1649695676265: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to tranzitivní uzávěr množiny atributů \(X\) a jaký je jeho postup výpočtu?

### Odpověď (Back)

Je to množina všech atributů funkčně závislých na \(X\). Značíme \(X^+\).
Postup výpočtu:

1. do \(X^+\) přidáme \(X\)
2. procházíme funkční závislosti, je-li levá strana už v \(X^+\), přidáme pravou stranu
3. opakujeme dokud do \(X^+\) něco přibývá

## Poznámka Anki 1649695755697

Karty Anki: 1649695755697
GUID: EPwJXG/w-{; štítky: bi-dbs::p09.

Metadata původního zdroje pro kartu 1649695755697: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to klíč relace?

### Odpověď (Back)

Mějme \(R(A)\) a nechť \(K \subseteq A\). \(K\) je klíčem schématu, jestliže splňuje

- \(K \to A\)

- neexistuje \(K' \subset K\) taková, že \(K' \to A\).

## Poznámka Anki 1649695939482

Karty Anki: 1649695939482
GUID: P-C&eVAL`J; štítky: bi-dbs::p09.

Metadata původního zdroje pro kartu 1649695939482: v původním balíčku pozastavená karta.

### Otázka (Front)

Kdy je schéma v třetí normální formě (3NF)?

### Odpověď (Back)

Řekneme, že schéma relace \(R\) je v 3. normální formě, jestliže žádný neklíčový atribut schématu \(R\) není tranzitivně závislý na žádném klíči schématu.

**Jinými slovy**: Každý neklíčový atribut je na (každém) klíči schématu závislý přímo, nikoliv tranzitivně.

## Poznámka Anki 1649695997081

Karty Anki: 1649695997081
GUID: Gf_lrOPgg:; štítky: bi-dbs::p09.

Metadata původního zdroje pro kartu 1649695997081: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte BCNF.

### Odpověď (Back)

Řekneme, že schéma relace \(R\) je v Boyce-Coddově normální formě (BCNF), jesliže pro každou netriviální závislost \(X \to Y\) platí, že \(X\) obsahuje klíč schématu \(R\).

