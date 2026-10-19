# BI-HWB – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-hwb/BI-HWB.apkg; APKG SHA-256 0303626d2408f7eee1801e17ecb475633a60c42f914f37290ffd8c479013ce2b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b861d2e855c5070244800c22d62092a09b22aee0ded024030525b06a7d18285e.
Původní balíčky: BI-HWB
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1695646793553

Karty Anki: 1695646793553
GUID: kJx`a[zWam; štítky: bi-hwb::p01.

### Otázka (Front)

Porovnejte implementaci kryptografických funkcí jako softwarový modul a hardwarový modul.

### Odpověď (Back)

|       **softwarový modul** |       **hardwarový modul** |         
|       jednoduchá implementace a vývoj |       náročná implementace a vývoj |         
|       vysoká flexibilita (možnost aktualizace) |       velmi nízká flexibilita |         
|       otevřenost (možnost auditu kódu)
 |       uzavřenost (utajené detaily specifikace) |         
|       horší bezpečnost tajných dat (lze je vyčíst z RAM)
 |       vysoká bezpečnost tajných dat (tamper resistance) |          
|       težko prokazatelné prolomení
 |       lehce prokazatelné prolomení (tamper evidence) |           
|       zranitelnost chybami OS, útoky nebo malware |       
 |

## Poznámka Anki 1695647050071

Karty Anki: 1695647050071
GUID: Di$Dm7X62r; štítky: bi-hwb::p01 ni-pb::21.

### Otázka (Front)

Popište hardwarový bezpečnostní modul (HSM).

### Odpověď (Back)

Hardwarový bezpečnostní modul nebo také hardware security module (HSM) je fyzické výpočetní zařízení, které poskytuje následující funkce:

- bezpečné generování klíčů,
- bezpečné ukládání klíčů,
- šifrování a dešifrování,
- podepisování a ověřování,
- bezpečná autentizace,
- odlehčení CPU stroje (offloading),
- akcelerace SSL/TLS.

## Poznámka Anki 1695648025685

Karty Anki: 1695648025686
GUID: cvYDd5,4qa; štítky: bi-hwb::p01.

### Otázka (Front)

Uveďte některé normy bezpečnostních požadavků na hardwarové bezpečnostní moduly.

### Odpověď (Back)

Mezi normy bezpečnostních požadavků na HSM patří:

- FIPS 140 (NIST),
- Common Criteria for Information Technology Security Evaluation,
- FIPS 140-2.

## Poznámka Anki 1695648128332

Karty Anki: 1695648128333
GUID: kIrC!VGou@; štítky: bi-hwb::p01.

Metadata původního zdroje pro kartu 1695648128333: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to čipová karta? Jaký autentizační faktor představuje?

### Odpověď (Back)

Čipová karta je obvykle plastová kartička, které obsahuje integrovaný obvod. Představuje autentizační faktor vlastnictví.

## Poznámka Anki 1695648177195

Karty Anki: 1695648177195
GUID: LL0QG8Tjbb; štítky: bi-hwb::p01.

Metadata původního zdroje pro kartu 1695648177195: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište vnitřní složení čipové karty.

### Odpověď (Back)

Základní čipové karty si vystačí pouze s propojenými kontakty, rezonančními obvody a podobně. O něco pokročilejší karty obsahují paměť a to buď ve formě ROM, EEPROM nebo zabezpečené paměti (např. MIFARE Classic). Moderní čipové karty potom obsahují počítač, který je konfigurovatelný a programovatelný (např. Java Cards). Vnitřní struktura tohoto počítače je následující:

- **výpočetní jednotky** - CPU, kryptografický koprocesor;
- **paměti** - RAM, ROM, EEPROM;

- ****napájecí a **komunikační rozhraní**;
- **senzory**.

## Poznámka Anki 1695649573936

Karty Anki: 1695649573936
GUID: ARFU*h|a[1; štítky: bi-hwb::p01 bi-ib::18.

### Otázka (Front)

Popište application protocol data unit (APDU) podle ISO 7816.

### Odpověď (Back)

APDU je komunikační jednotka používaná mezi smart card a čtečkou. Její struktura je následující:

 [Obrázek: paste-ae65b14bea9d5f93000cdaae3eacde1819e077f1.jpg; soubor je v media/ v doprovodném ZIP] 

Jednotlivá pole představují:

- \(\mathtt{CLA}\) - třída instrukce (instruction class),

- \(\mathtt{INS}\) - kód instrukce (instruction code),

- \(\mathtt{P1}\) a \(\mathtt{P2}\) - parametry instrukce,

- \(\mathtt{L_c}\) - délka pole \(\mathtt{Data}\),

- \(\mathtt{Data}\) - data instrukce nebo odpovědi,

- \(\mathtt{L_e}\)- očekávaná délka odpovědi.

- \(\mathtt{SW1}\) a \(\mathtt{SW2}\) - návratová hodnota instrukce.

## Poznámka Anki 1695650736593

Karty Anki: 1695650736594
GUID: z?D]&VzOvv; štítky: bi-hwb::p01 bi-ib::18.

### Otázka (Front)

Popište typy pamětí na Java Card.

### Odpověď (Back)

| 
      **persistentní úložiště** | 
      **transientní úložiště** | 

| 
      realizována EEPROM | 
      realizována RAM | 

| 
      kapacita ~64 KB | 
      kapacita ~1 KB | 

| 
      obsah vydrží po vysunutí karty | 
      obsah je po vysunutí karty ztracen | 

| 
      pomalejší | 
      rychlejší | 

| 
      opakované použití ji opotřebuje | 
      
 |

## Poznámka Anki 1702815228120

Karty Anki: 1702815228120
GUID: p`>sfb&@a2; štítky: bi-hwb::p01 ni-pb::21.

### Otázka (Front)

Popište jednotlivé úrovně požadavků na bezpečnost hardwarových bezpečnostních modulů (HSM) podle FIPS 140-2.

### Odpověď (Back)

FIPS 140-2 stanovuje následující úrovně podle požadavků na bezpečnost hardwarových bezpečnostních modulů (HSM):

- **level 1** - alespoň jeden schválený šifrovací algoritmus nebo jedna schválená bezpečnostní funkce,

- **level 2** - prokazatelnost ovlivnění či průniku (tamper evidence),

- **level 3** - odolnost proti ovlivnění či průniku (tamper resistance),

- **level 4** - vyšší odolnost proti ovlivnění či průniku (tamper resistance) a odolnost proti vlivům prostředí.

