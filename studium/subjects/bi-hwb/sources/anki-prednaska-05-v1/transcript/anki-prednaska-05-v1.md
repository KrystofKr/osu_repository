# BI-HWB – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-hwb/BI-HWB.apkg; APKG SHA-256 0303626d2408f7eee1801e17ecb475633a60c42f914f37290ffd8c479013ce2b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b861d2e855c5070244800c22d62092a09b22aee0ded024030525b06a7d18285e.
Původní balíčky: BI-HWB
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1698071738269

Karty Anki: 1698071738269
GUID: t*&5fE&{r6; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Popište proces inicializace kontaktní čipové karty.

### Odpověď (Back)

Inicializace kontaktní čipové karty probíhá v následujících krocích:

- terminál indikuje přítomnost karty,
- terminál spouští napájení,
- terminál spouští signál hodin a signál reset,
- karta odesílá answer to reset,
- terminál dekóduje answer to reset,
- proběhne volba parametrů protokolu.

## Poznámka Anki 1698071942808

Karty Anki: 1698071942808
GUID: po52/%ofj_; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Uveďte příklady komunikačních protokolů kontaktních karet. Jak jsou přenášena jejich data?

### Odpověď (Back)

Data komunikančích protokolů kontaktních karet jsou přenášena uvnitř struktur transmission protocol data unit (TPDU). Nejčastěji se používají následující protokoly:

- \(\mathtt{T = 0}\) protokol - bytově orientovaný,

- \(\mathtt{T = 1}\) protokol - blokově orientovaný.

## Poznámka Anki 1698072969284

Karty Anki: 1698072969284
GUID: L8SmvE)2x$; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Popište radio-frequency identification (RFID).

### Odpověď (Back)

Radio-frequency identification (RFID) používá elektromagnetické pole k automatické identifikaci a sledování transponderů připevněných k objektům. RFID systém se skládá ze dvou zařízení:

- **transponder** (tag, karta) - nosič dat připevněný ke sledovanému objektu,

- **čtečka **(interrogator, terminál) - napájí, detekuje a komunikuje s transpondery.

## Poznámka Anki 1698079797785

Karty Anki: 1698079797786
GUID: 7_X70Q2AV; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Popište near-field communication (NFC).

### Odpověď (Back)

Near-field communication (NFC) je sada komunikačních protokolů pro přenos dat mezi dvěma zařízeními na krátkou vzdálenost (cca 4 cm), která rozšiřuje radio-frequency identification (RFID). Používá se v platebních systémech, pro sdílení dat nebo bootstrapping dalších protokolů jako např. Bluetooth. Umožňuje dva operační módy:

- **active** - obě zařízení střídavě indukují elektromagnetické pole a komunikují,

- **passive** - jedno zařízení indukuje elektromagnetické pole a vysílá a druhé pouze přijímá.

U zařízení, která jsou schopna plnit jak funkci čtečky, tak čipové karty rozlišujeme operační mód passive ještě na:

- reader emulation,

- card emulation.

## Poznámka Anki 1698080007569

Karty Anki: 1698080007569
GUID: wHq0r:D[B9; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Jaký je rozdíl mezi pasivním a aktivním transponderem?

### Odpověď (Back)

Pasivní transponder neobsahuje baterii a veškeré napájení získává z elektromagnetického pole čtečky. Aktivní transponder baterii obsahuje, což mu dovoluje vysílat s větším dosahem.

## Poznámka Anki 1698085373075

Karty Anki: 1698085373075
GUID: IDz7=-i5M-; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Jaká se používají bezpečnostní opatření na čipových kartách?

### Odpověď (Back)

Na čipových kartách se používají následující bezpečnostní opatření:

- **basic access control** (BAC) - používá strojově čitelnou zónu (machine-readable zone),

- **supplemental access control** (SAC) - používá strojově čitelnou zónu a card access number či PIN.

Tato opatření zabraňují útokům skimmingem (čtení karty bez fyzického přístupu) a odposlechu, čehož dosahují pomocí secure messaging. Doplňkově se pak mohou používat:

- **active authentication **- autentizace čipové karty,

- **extended access control **(EAC) - autentizace čipové karty i terminálu,

a to k tomu, aby bylo zabráněno podvržení čipové karty.

## Poznámka Anki 1698086434649

Karty Anki: 1698086434649
GUID: OL^S7fJ#J<; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Popište zákadní kategorie útoků na čipové karty.

### Odpověď (Back)

Mezi základní kategorie útoků na čipové karty patří:

- **útoky na komunikaci **- odposlech, MITM, replay, relay;

- **invazivní útoky** - vyčtení klíče z paměti;

- **semi-invazivní útoky**,

- **neinvazivní útoky** - postranní kanál, injekce poruch.

## Poznámka Anki 1718035891527

Karty Anki: 1718035891528
GUID: f#$Cwb|K5b; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Uveďte příklady čipových karet s bezkontaktním rozhraním.

### Odpověď (Back)

Mezi příklady čipových karet s bezkontaktním rozhraním patří:

- **MIFARE DESFire EV1** - studentská karta ČVUT, Lítačka;
- **MIFARE 1K (Classic)** - předchůdce DESFire EV1;
- **ICAO MRTD ePassport** - evropský pas,
- **Visa payWave** a **MasterCard PayPass** - platební karty.

## Poznámka Anki 1718036088826

Karty Anki: 1718036088826
GUID: Q{#`|#g!Ai; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Uveďte příklady typů bezkontaktních komunikačních rozhraní čipových karet.

### Odpověď (Back)

Mezi příklady typů bezkontaktních komunikačních rozhraní čipových karet patří:

- **low frequency** - 125 kHZ, 135 kHZ;

- **high frequency with proximity coupling** (vazba na blízko) - 13.56 MHz (ISO 14443);

- **high frequency with vicinity coupling **(vazba na dálku) - 13.56 MHz;

- **ultra-high frequency** - 868-928 MHz.

## Poznámka Anki 1718037860853

Karty Anki: 1718037860853
GUID: xt^r=STeq_; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Popište složení radio-frequency identification (RFID) transponderu a uveďte jeho příklady.

### Odpověď (Back)

Radio-frequency identification (RFID) transponder se skládá z:

- antény (spojovacího prvku),
- mikročipu.

Mezi příklady RFID transponderů patří sledovací nálepky na zboží, implantovaný čip pro značení zvířat nebo mobilní telefon.

## Poznámka Anki 1718037972818

Karty Anki: 1718037972819
GUID: r:|rC,nv.M; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Popište složení radio-frequency identification (RFID) čtečky a uveďte její příklady.

### Odpověď (Back)

Radio-frequency identification (RFID) čtečka se skládá z:

- antény (spojovacího prvku),
- radio-frequency (RF) modulu (přijímač, vysílač),

- řídící jednotky.

Mezi příklady RFID čteček patří zámek dveří, imobilizér auta nebo mobilní telefon.

## Poznámka Anki 1718039201828

Karty Anki: 1718039201828
GUID: xe:#t]9fn$; štítky: bi-hwb::p05.

Metadata původního zdroje pro kartu 1718039201828: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Jakými způsoby se provádí zabezpečení komunikace (secure messaging) čipových karet?

### Odpověď (Back)

Zabezpečení komunikace čipových karet (secure messaging) lze implementovat následujícími způsoby:

- **bez zabezpečení integrity a šifrování **- některé čipové karty nepoužívají autentizaci ani šifrování;
- **zabezpečení integrity** - např. pomocí MAC;
- **zabezpečení integrity a šifrování** - např. pomocí 3DES nebo AES;
- **princip zabalení do struktur typu TLV** (tag, length, value).

## Poznámka Anki 1718040130194

Karty Anki: 1718040130195
GUID: pk2)^7xEHj; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Popište implementaci zabezpečení komunikace (secure messaging) čipových karet se zabezpečením integrity a šifrováním.

### Odpověď (Back)

Při implementaci zabezpečení komunikace (secure messaging) čipových karet se zabezpečením integrity a šifrováním se nejprve provádí zabezpečení integrity:

- data původního APDU jsou zabalena do struktury TLV (tag, length, value);
- z této struktury je vypočten cryptographic checksum (např. MAC);
- vypočtený cryptographic checksum (CCS) je zabalen do struktury TLV a připojen za původní TLV strukturu;
- \(\texttt{CLA}\) byte APDU je upraven tak, aby signalizoval použití cryptographic checksum.

Výsledkem je APDU s původní hlavičkou a upraveným \(\texttt{CLA}\) bytem, které v těle obsahuje TLV struktury pro data a cryptographic checksum. Následně se použije obdobný proces pro šifrování:

- TLV struktury z předchozího kroku jsou zašifrovány (např. pomocí 3DES);
- výsledný ŠT je zabalen do struktury TLV a připojen za původní hlavičku;
- \(\texttt{CLA}\) byte APDU je upraven tak, aby signalizoval použití cryptographic checksum a šifrování.

Výsledkem je APDU s původní hlavičkou a upraveným \(\texttt{CLA}\) bytem, které v těle obsahuje TLV strukturu se zašifrovanými daty z předchozího kroku.

## Poznámka Anki 1718040634368

Karty Anki: 1718040634368
GUID: cCfJ+k,p6P; štítky: bi-hwb::p05 bi-ib::18.

### Otázka (Front)

Popište souborový systém čipových karet podle normy ISO 7816-4.

### Odpověď (Back)

V souborovém systému čipových karet podle normy ISO 7816-4 rozlišujeme tři typy souborů:

- **master file** - kořenový adresář,

- **dedicated file **- adresář,

- **elementary file **- soubor.

Soubory (elementary files) dále dělíme podle struktury na:

- **transparent structure **- bez vnitřní struktury,

- **record structure** - strukturované do záznamů.

Se soubory lze provádět operace:

- \(\texttt{SELECT}\) - výběr souboru,

- \(\texttt{READ BINARY}\), \(\texttt{UPDATE BINARY}\) - čtení a zápis transparent souborů,

- \(\texttt{READ RECORD}\), \(\texttt{UPDATE RECORD}\) - čtení a zápis record souborů.

Souborový systém dále podporuje přístupová oprávnění.

