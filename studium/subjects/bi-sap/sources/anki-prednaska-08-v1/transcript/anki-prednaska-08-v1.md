# BI-SAP – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-sap/BI-SAP.apkg; APKG SHA-256 1f67b9282d55c6e8fb096f86041a008a959b3ade7ab78b051bce1ceb2cf0a3bd. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 624f9e0b4061e0e62a0e80089c16bfc9c700ec35ffa2dae8f3cc15f23be9a383.
Původní balíčky: BI-SAP
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1649750963704

Karty Anki: 1649750963705
GUID: Ou_C(~go!P; štítky: bi-sap::otazky08 bi-sap::p08.

Metadata původního zdroje pro kartu 1649750963705: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište instrukční cyklus.

### Odpověď (Back)

[Obrázek: paste-2e9e3ade353241cca7e77380b5f5f5b7c97236a3.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1649751095153

Karty Anki: 1649751095153
GUID: hBLwG?86VG; štítky: bi-ib::04 bi-sap::otazky08 bi-sap::p08 bi-spol::29.

### Otázka (Front)

Co je to instrukce a co musí obsahovat.

### Odpověď (Back)

Instrukce je příkaz zakódovaný jako číslo.
Musí obsahovat:

- co se má provést
- s čím se to má provést (operandy)
- kam se má uložit výsledek
- kde se má pokračovat
Tyto informace mohou být obsaženy explicitně nebo implicitně (pokračuje se instrukcí na další adrese).

## Poznámka Anki 1649751175236

Karty Anki: 1649751175236
GUID: kiSq+#Ri`U; štítky: bi-sap::otazky08 bi-sap::p08.

Metadata původního zdroje pro kartu 1649751175236: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to střadač?

### Odpověď (Back)

Je to registr procesoru určený k obecnému použití.

## Poznámka Anki 1649751348446

Karty Anki: 1649751348446
GUID: Fo9*)aXdsM; štítky: bi-ib::04 bi-sap::otazky08 bi-sap::p08 bi-spol::29.

### Otázka (Front)

Z čeho se skládá instrukce?

### Odpověď (Back)

Z operačního znaku a operandů.

 [Obrázek: paste-9cebf6c6281f11defe44bb11e395b9a8ea870171.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1649751593850

Karty Anki: 1649751593851
GUID: w=8)M4FRrF; štítky: bi-ib::04 bi-sap::otazky08 bi-sap::p08 bi-spol::29.

Metadata původního zdroje pro kartu 1649751593851: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou druhy adresace operandů v ISA? Zakreslete ilustrace.

### Odpověď (Back)

- implicitní - v instrukci je jen operační znak
- bezprostřední - v instrukci je konstanta
- přímá - v instrukci je adresa paměti (nebo číslo registru), na které je operand
- nepřímá - v instrukci je adresa paměti (nebo číslo registru), na které je adresa paměti, na které je operand
- relativní - adresa operandu se získá součtem obsahu registru a offsetu (registr je buď implicitní (PC) nebo je určen v instrukci)
- indexová - adresa operandu se získá součtem obsahu dvou registrů (báze a indexu)
- autoinkrementace a autodekrementace - operand se získá na adrese, která je obsahem registru a je navíc inkrementována nebo dekrementována
Ukázka ilustrace pro indexovou adresaci:

 [Obrázek: paste-5d2866ac0391f8c2fe6515f652cb65faa6c22e2e.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1649751853098

Karty Anki: 1649751853098
GUID: H.s;1JZIzo; štítky: bi-sap::otazky08 bi-sap::p08 bi-spol::29.

Metadata původního zdroje pro kartu 1649751853098: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište střadačově orientovanou (accumulator-oriented) ISA.

### Odpověď (Back)

Střadačově orientovaná (accumulator-oriented) ISA je jedna z nejstarších ISA. Její instrukce typicky povolují jeden operand a druhým operandem je implicitně střadač (accumulator). Mezi její výhody a nevýhody patří:
| **výhody** | **nevýhody** |         
|       jednoduchý hardware |       časté přístupy do paměti |         
|       krátké instrukce
 |       omezený paralelismus |

## Poznámka Anki 1649752034934

Karty Anki: 1649752034934
GUID: JEtCYG47oj; štítky: bi-sap::otazky08 bi-sap::p08 bi-spol::29.

Metadata původního zdroje pro kartu 1649752034934: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište zásobníkově orientovanou (stack-oriented) ISA.

### Odpověď (Back)

Zásobníkově orientovaná (stack-oriented) ISA je ISA, která typicky používá instrukce bez operandů. Všechny instrukce pracují implicitně se svrchní nebo svrchními dvěma pozicemi na zásobníku. Mezi její výhody a nevýhody patří:

| **výhody** | **nevýhody** |         
|       vysoká hustota kódu |       neumožňuje náhodný přístup k datům |         
|       krátké instrukce
 |       omezený paralelismus |

## Poznámka Anki 1649752168460

Karty Anki: 1649752168460
GUID: L^4`f?W.kJ; štítky: bi-sap::otazky08 bi-sap::p08 bi-spol::29.

### Otázka (Front)

Popište general purpose register (GPR) orientovanou ISA.

### Odpověď (Back)

General purpose reigster (GPR) orientovaná ISA je ISA, která typicky používá instrukce se dvěma nebo třemi operandy, ve kterých se vyskytují GPR. Mezi její výhody a nevýhody patří:

| **výhody** | **nevýhody** | 

| 
      minimalizace přístupů do paměti (vyšší rychlost) | 
      složitější překladač | 

| 
      podporuje náhodný přístup k datům | 
      omezený počet registrů |

