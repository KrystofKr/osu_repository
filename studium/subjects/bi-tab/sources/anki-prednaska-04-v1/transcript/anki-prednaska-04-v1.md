# BI-TAB – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-tab/BI-TAB.apkg; APKG SHA-256 aad5d9418346792a97b103483c6a92411d60f79d52fd5a423fd0fc14dffe748b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 53183dd48468239630c7cf283347984511ecad52b3dee78ea36f4c1d42180eeb.
Původní balíčky: BI-TAB
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1710353345539

Karty Anki: 1710353345539
GUID: hx{#&?#(=]; štítky: bi-tab::p04.

### Otázka (Front)

Popište rozdíly mezi circuit switching a packet switching.

### Odpověď (Back)

Circuit switching je komunikační metoda, při které je před zahájením přenosu dat vytvořeno spojení (circuit) mezi komunikujícími zařízeními. Toto spojení je po dobu komunikace neměnné a používané linky jsou obsazené. Naproti tomu packet switching data před přenosem rozdělí na menší části (packets), které jsou poté nezávisle směrovány. Circuit switching a packet switching mají následující výhody a nevýhody:      
|       **circuit switching** |       **packet switching** |         
|       nížší latence |       vyšší latence |         
|       garantovaná rychlost přenosu |       variabilní rychlost přenosu |          
|       dražší |       levnější |

## Poznámka Anki 1710354104730

Karty Anki: 1710354104730
GUID: m8RH8HY|&B; štítky: bi-tab::p04.

### Otázka (Front)

Popište autentizaci v Global System for Mobile Communication (GSM/2G) síti.

### Odpověď (Back)

Předpokládejme, že existuje společný symetrický klíč \(K_i\), který je uložen jak v mobile station (MS), tak v domovském mobile switching center (MSC). Autentizace v 2G síti probíhá následovně:

- MS posílá svou international mobile subscriber identity (IMSI) MSC.

- MSC si na základě IMSI z databáze zjistí odpovídající hodnotu \(K_i\) a vygeneruje náhodné číslo \(\text{RAND}\). Pomocí \(\text{RAND}\) a \(K_i\) získá signed response \(\text{SRES}\) za pomocí algoritmu A3 a \(K_c\) za pomocí algoritmu A8. Hodnotu \(\text{RAND}\) odešle MS.
- Pomocí \(\text{RAND}\) si MS stejným způsobem vygeneruje \(K_c\) a \(\text{SRES}'\). \(\text{SRES}'\) následně pošle MSC.
- MSC porovná \(\text{SRES}\) s \(\text{SRES}'\) a pokud se shodují, je zařízení úspěšně autentizováno a spouští se šifrování pomocí A5/3. Jako šifrovací klíč se použije \(K_c\).

## Poznámka Anki 1710362116600

Karty Anki: 1710362116600
GUID: H[|4@W%63t; štítky: bi-tab::p04.

### Otázka (Front)

Popište popiště vývoj napříč 1G, 2G, 3G, 4G a 5G sítěmi.

### Odpověď (Back)

Vývoj napříč 1G, 2G, 3G, 4G a 5G sítěmi je následující:

| 
      **různé technologie
(1G)** | 
      **Global System for Mobile Communications
(GSM/2G)** | 
      **Universal Mobile Telecommunications System
(UMTS/3G)** | 
      **4G** | 
      **5G** | 

| 
      zavislé na analogových technologiích | 
      první plně digitální generace | 
      hlas, SMS, circuit switching, packet switching | 
      vylepšení technologií 3G a podpora VoIP | 
      nižší latence | 

| 
       | 
      hlas, SMS, circuit switching | 
      rychlejší datový přenos | 
      rychlejší datový přenos | 
      rychlejší datový přenos | 

| 
       | 
      později přidán i packet switching a přenos dat | 
       | 
      standardizace 3rd Generation Partnership Project (3GPP) |

## Poznámka Anki 1710362600483

Karty Anki: 1710362600483
GUID: O-6`Ob6iba; štítky: bi-tab::p04.

### Otázka (Front)

Popište rozdíl mezi standalone (SA) a non-standalone (NSA) 5G sítěmi.

### Odpověď (Back)

Standalone (SA) 5G síť je 5G síť, která používá 5G jádro a může tak využívat výhody 5G, jako jsou nízká latence a rychlý datový přenos. Oproti tomu non-standalone (NSA) 5G sítě stále operují na 4G LTE jádru.

## Poznámka Anki 1710362765261

Karty Anki: 1710362765261
GUID: sH>6_`YDM4; štítky: bi-tab::p04.

### Otázka (Front)

Popište 3rd Generation Partnership Project (3GPP).

### Odpověď (Back)

3rd Generation Partnership Project (3GPP) je pojem zaštiťující celou řadu standardizačních organizací, které se zabývají vývojem mobilních telekomunikačních sítí (2G, 3G, 4G, 5G).

## Poznámka Anki 1710363924172

Karty Anki: 1710363924173
GUID: K^>JXAEN#}; štítky: bi-tab::p04.

### Otázka (Front)

Popište Subscriber Identity Module (SIM) kartu.

### Odpověď (Back)

Subscriber Identity Module (SIM) karta je forma smart card se standardním ISO 7816-4 souborovým systémem, která se využívá v mobilních telekomunikačních sítích. Běžně ukládá následující data:

- international mobile subscriber identity (IMSI),

- autentizační klíč \(K_i\),
- Integrated Circuit Card Identifier (ICCID).

## Poznámka Anki 1710364388053

Karty Anki: 1710364388053
GUID: utfUB`DCz]; štítky: bi-tab::p04.

### Otázka (Front)

Popište international mobile subscriber identity (IMSI) catcher.

### Odpověď (Back)

International mobile subscriber identity (IMSI) catcher je forma man-in-the-middle útoku na mobilní telekomunikační sítě, zjeména na 2G síť. Funguje tak, že útočník předstírá falešnou telekomunikační věž a zachytí IMSI konkrétní mobile station. Z pozice man-in-the-middle pak může projít celým autentizačním algoritmem pro 2G a následně odposlouchávat telefonní komunikaci. Síť 3G zavádí proti tomuto útoku obranu v podobě mutual authentication.

