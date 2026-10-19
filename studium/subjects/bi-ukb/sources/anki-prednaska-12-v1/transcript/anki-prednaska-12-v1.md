# BI-UKB – Přednáška 12

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-ukb/BI-UKB.apkg; APKG SHA-256 fb963722a1039499908d9a37b947a0f774fd26b951b463a4c2349468681bec67. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8d39d92d14a3cb34c1c177ef00602d3767837744484a3254d799cb18f10b34a9.
Původní balíčky: BI-UKB
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1671274012391

Karty Anki: 1671274012391
GUID: QnOypp#*Z$; štítky: bi-ib::22 bi-ukb::p12.

Metadata původního zdroje pro kartu 1671274012391: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Purdue model pro průmyslové sítě.

### Odpověď (Back)

Podle Purdue modelu se průmyslová síť skládá z následujících částí:

| 
      úroveň (level) | 
      název | 
      účel | 
      komponenty | 

| 
      5, 4 | 
      enterprise zone | 
      plánování, logistika | 
      enterprise resource planning (ERP) | 

| 
      - | 
      demilitarized zone | 
      ochrana sítě | 
      firewall, proxy | 

| 
      3 | 
      manufacturing operations systems zone | 
      monitorování a řízení výrobního procesu | 
      automatizační nástroje, vzdálený přístup | 

| 
      2 | 
      control systems zone | 
      monitorování a řízení fyzického procesu | 
      HMI, SCADA | 

| 
      1 | 
      intelligent devices zone | 
      řízení level 0 zařízení | 
      PLC | 

| 
      0 | 
      physical process zone | 
      průběh fyzického procesu | 
      senzory, akční členy |

## Poznámka Anki 1671274086911

Karty Anki: 1671274086911
GUID: qdBn)i+OoB; štítky: bi-ib::22 bi-ukb::p12.

### Otázka (Front)

Popište industrial control system (ICS).

### Odpověď (Back)

Industrial control system (ICS) je cyber-physical system (CPS), který se používá pro řízení průmyslových procesů. Typicky se skládá z následujících částí:

- **senzory **(sensors), **akční členy **(actuators) - komponenty CPS,
- **programmable logic controllers** (PLC),

- **human-machine interfaces** (HMI),

- **supervisory control and data acquisition** (SCADA) **systém**.

## Poznámka Anki 1671274163791

Karty Anki: 1671274163792
GUID: d#J]uk;-m(; štítky: bi-ib::22 bi-ukb::p12.

### Otázka (Front)

Popište supervisory control and data acquisition (SCADA) systém.

### Odpověď (Back)

Supervisory control and data acquisition (SCADA) systém je systém používaný pro high-level dohled nad průmyslovými procesy a zařízeními, který se typicky nachází v control systems zone průmyslové sítě. Provádí monitorování průmyslových procesů a zařízení (PLC, senzory) a umožňuje jejich řízení.

## Poznámka Anki 1671275834510

Karty Anki: 1671275834510
GUID: N$=;A.x=$); štítky: bi-ib::22 bi-ukb::p12.

Metadata původního zdroje pro kartu 1671275834510: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište programmable logic controller (PLC).

### Odpověď (Back)

Programmable logic controller (PLC) je typ počítače přizpůsobeného pro použití v průmyslovém prostředí, který se typicky nachází v intelligent devices zone průmyslové sítě. Přímo řídí připojená průmyslová zařízení, monitoruje je a komunikuje skrze human-machine interface (HMI).

## Poznámka Anki 1671275921452

Karty Anki: 1671275921452
GUID: JJGys>_zP@; štítky: bi-ib::22 bi-ukb::p12.

Metadata původního zdroje pro kartu 1671275921452: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište human-machine interface (HMI).

### Odpověď (Back)

Human-machine interface (HMI) je hardwarové nebo softwarové rozhraní, které se používá pro monitorování a řízení PLC a dalších průmyslových zařízení (např. pomocí protokolů Modbus, ICCP a DNP3). Typicky se nachází v control systems zone průmyslové sítě.

## Poznámka Anki 1671276487461

Karty Anki: 1671276487461
GUID: dSjB-GSY[M; štítky: bi-ib::22 bi-ukb::p12.

Metadata původního zdroje pro kartu 1671276487461: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište specifika zabezpečení industrial control systems (ICS) a průmyslových sítí.

### Odpověď (Back)

Protože industrial control systems (ICS) jsou typem cyber-physical systems (CPS), jsou na ICS aplikovatelná specifika zabezpečení CPS. Krom nich dále platí:

- **komunikační protokoly** - ICS často používají nezabezpečené komunikační protokoly (Modbus, ICCP, DNP3),

- **komplikovaný ****patch management** - aplikace patchů vyžaduje pozastavení průmyslových procesů a může způsobit nestabilitu systému;

- **kritická infrastruktura **- ICS jsou často součástí kritické infrastruktury a jejich výpadky mohou mít rozsáhlé následky.

## Poznámka Anki 1671277118820

Karty Anki: 1671277118821
GUID: L8,%w$g)lc; štítky: bi-ib::22 bi-ukb::p12.

Metadata původního zdroje pro kartu 1671277118821: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište protokol Modbus a jeho bezpečnostní nedostatky.

### Odpověď (Back)

Modbus je protokol aplikační vrstvy postavený na modelu client/server, který se používá pro komunikaci s průmyslovými zařízeními. Mezi jeho bezpečnostní nedostatky patří:

- chybějící ochrana důvěrnosti a integrity,
- chybějící autentizace,
- chybějící ochrana proti denial-of-service (DoS) útokům.

## Poznámka Anki 1671277723320

Karty Anki: 1671277723320
GUID: EsaM1I30Gz; štítky: bi-ib::22 bi-ukb::p12.

Metadata původního zdroje pro kartu 1671277723320: v původním balíčku pozastavená karta.

### Otázka (Front)

Popišt Inter-Control Center Communications Protocol (ICCP) a jeho bezpečnostní nedotatky.

### Odpověď (Back)

Inter-Control Center Communications Protocol (ICCP) je protokol aplikační vrstvy postavený na modelu client/server, který se používá pro komunikaci mezi řídícími centry industrial control systems (ICS), zejména elektráren. Na rozdíl od protokolu Modbus podporuje obousměrnou komunikaci a implementuje řízení přístupů v podobě bilateral table, která určuje úrovně přístupu pro konkrétní spojení. Mezi jeho bezpečnostní nedostatky patří:

- chybějící ochrana důvěrnosti,
- chybějící autentizace,
- chybějící ochrana proti denial-of-service (DoS) útokům.

## Poznámka Anki 1671278480383

Karty Anki: 1671278480383
GUID: IrGu&ekvv}; štítky: bi-ib::22 bi-ukb::p12.

Metadata původního zdroje pro kartu 1671278480383: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Distributed Network Protocol 3 (DNP3).

### Odpověď (Back)

Distributed Network Protocol 3 (DNP3) je protokol linkové, transportní a aplikační vrstvy, který se používá pro komunikaci s průmyslovými zařízeními, zejména mezi SCADA systémy a zařízeními nižších vrstev průmyslové sítě. Narozdíl od protokolů Modbus a ICCP podporuje autentizaci a kontrolu integrity.

