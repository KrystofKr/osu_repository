# BI-ASB – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-asb/BI-ASB.apkg; APKG SHA-256 7a0706fba841a39fa40ea1e5439c99f14f59930aaa7f6d5620a33590d53350fa. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: eea4a1b952e7287bc51501f27ae2f5ec76f032fca049ee9ef600d2729e12ef40.
Původní balíčky: BI-ASB
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1700475489460

Karty Anki: 1700475489460
GUID: tQv?U`+;Gd; štítky: bi-asb::p07.

Metadata původního zdroje pro kartu 1700475489460: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Internet of Things (IoT).

### Odpověď (Back)

Internet of Things (IoT) jsou zařízení vybavená senzory a softwarem pro zpracování jejich výstupů, která si prostřednictvím internetu nebo jiných sítí vyměnují data s dalšími zařízeními za účelem poskytování služeb nebo informací.

## Poznámka Anki 1700476042218

Karty Anki: 1700476042219
GUID: ru-^l4/<dR; štítky: bi-asb::p07 bi-ib::22.

### Otázka (Front)

Popište vrstvy Internet of Things (IoT) ekosystému.

### Odpověď (Back)

Ekosystém Internet of Things (IoT) se dělí do následujících vrstev:

- **coding layer** - identifikace zařízení,

- **perception layer** - přenos signálů mezi senzory a akčními členy,

- **network layer** - přenos dat po síti,

- **middleware layer** - zpracování dat ze zařízení,

- **application layer** - aplikace používající zařízení.

## Poznámka Anki 1700476629431

Karty Anki: 1700476629431
GUID: EZnxE<Q/XN; štítky: bi-asb::p07 bi-ib::22.

### Otázka (Front)

Uveďte příklady protokolů fyzické a linkové vrstvy, které se používají v Internet of Things (IoT).

### Odpověď (Back)

Mezi protokoly fyzické a linkové vrstvy využívané v Internet of Things (IoT) patří:

- Bluetooth,
- Bluetooth Low Energy (BLE),
- ZigBee,
- Wi-Fi,
- LoRaWAN,
- a další.

## Poznámka Anki 1700477104715

Karty Anki: 1700477104715
GUID: lMqPnm5/du; štítky: bi-asb::p07 bi-ib::22.

### Otázka (Front)

Popište Bluetooth Low Energy (BLE).

### Odpověď (Back)

Bluetooth Low Energy (BLE) je komunikační protokol postavený na protokolu Bluetooth. Na rozdíl od předchozích verzí neudržuje Bluetooth Low Energy konstantní spojení, ale po většinu času setrvává v úsporném módu a data vyměňuje jen když je to nutné.

## Poznámka Anki 1700477772606

Karty Anki: 1700477772606
GUID: zmH^5NW<[E; štítky: bi-asb::p07.

### Otázka (Front)

Popište role zařízení v Bluetooth Low Energy (BLE).

### Odpověď (Back)

Zařízení používající Bluetooth Low Energy (BLE) mohou mít jednu z následujících dvou rolí:

- **central device **(centrální zařízení) - zahajuje párování, přijímá data, vydává příkazy;

- **peripheral device **(periferní zařízení) - posílá advertising packets, poskytuje data.

## Poznámka Anki 1700478079546

Karty Anki: 1700478079546
GUID: Ov%n7}5Sf]; štítky: bi-asb::p07.

### Otázka (Front)

Popište topologie Bluetooth Low Energy (BLE) sítí.

### Odpověď (Back)

Bluetooth Low Energy (BLE) sítě mohou používat jednu z následujících topologií:

- **broadcast topology** - centrální zařízení poslouchají advertising packets od periferních zařízení,

- **connected topology** - centrální zařízení obousměrně komunikuje s jedním nebo více periferními zařízeními.

## Poznámka Anki 1700478588759

Karty Anki: 1700478588759
GUID: D:BP<<Jrax; štítky: bi-asb::p07.

### Otázka (Front)

Popište Generic Attribute Profile (GATT).

### Odpověď (Back)

Generic Attribute Profile (GATT) určuje způsob, kterým si zařízení v Bluetooth Low Energy (BLE) sítích vyměňují data. GATT umožňuje data rozdělit do services (služeb), které mohou definovat characteristics (vlastnosti) ukládající konkrétní data.

## Poznámka Anki 1700479639305

Karty Anki: 1700479639305
GUID: r;og`@an@z; štítky: bi-asb::p07.

### Otázka (Front)

Popište proces párování v Bluetooth Low Energy (BLE).

### Odpověď (Back)

Proces párování v Bluetooth Low Energy (BLE) probíhá následujícím způsobem:

- zařízení si vymění informace o podporovaných technologiích a metodách;
- zařízení se domluví na temporary key, který se použije k vygenerování short term key pomocí Diffie-Hellmanova algoritmu nad eliptickou křivkou;
- zařízení si spočtou long term key (šifrování a autentizace), connection signature resolving key (podepisování dat) a identity resolving key (generování soukromé adresy);
- spustí se šifrování přenosu pomocí AES-CCM (kombinace CTR a CBC-MAC módů).

## Poznámka Anki 1700480050598

Karty Anki: 1700480050598
GUID: v.aus^E)xT; štítky: bi-asb::p07.

### Otázka (Front)

Popište metody sjednání klíče u Bluetooth Low Energy (BLE).

### Odpověď (Back)

Bluetooth Low Energy (BLE) definuje následující metody sjednání klíče:

- **numeric comparison** - zařízení vygenerují náhodnou sekvenci čísel, kterou je potřeba potvrdit na obou zařízeních;

- **passkey entry **- jedno zařízení vygeneruje náhodnou sekvenci čísel, kterou je potřeba zadat na druhém zařízení;

- **just works** - temporary key je nastaven na samé nuly;
- **out-of-band **- výměna náhodné sekvence čísel se provede jiným kanálem jako např. NFC.

## Poznámka Anki 1700480225292

Karty Anki: 1700480225292
GUID: qb`]BfWfF9; štítky: bi-asb::p07 bi-ib::22.

Metadata původního zdroje pro kartu 1700480225292: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Uveďte příklady protokolů aplikační vrstvy, které se používají v Internet of Things (IoT).

### Odpověď (Back)

Mezi protokoly aplikační vrstvy využívané v Internet of Things (IoT) patří:

- Hypertext Transfer Protocol (HTTP),

- Message Queing Telemetry Transport (MQTT),

- Constrained Application Protocol (CoAP)
a další.

## Poznámka Anki 1700481039544

Karty Anki: 1700481039544
GUID: vm?:2,PQmI; štítky: bi-asb::p07 bi-ib::22.

### Otázka (Front)

Popište Message Queuing Telemetry Transport (MQTT) protokol.

### Odpověď (Back)

Message Queuing Telemetry Transport (MQTT) protokol je protokol aplikační vrstvy postavený na architektuře publish/subscribe specializovaný pro zažízení s omezenými zdroji, jako např. Internet of Things (IoT) zařízení. MQTT rozlišuje dva typy zařízení:

- **client** - zařízení, které buď odebírá (subscribes) nebo vydává (publishes) zprávy;
- **message broker** - přijímá veškeré zprávy a přeposílá je klientům, kteří je odebírají.

Zprávy v rámci MQTT protokolu jsou děleny do témat (topics). Pro každé téma se klient může rozhodnout jestli jej bude odebírat, nebo ne a podle toho mu pak bude message broker doručovat relevantní zprávy.

