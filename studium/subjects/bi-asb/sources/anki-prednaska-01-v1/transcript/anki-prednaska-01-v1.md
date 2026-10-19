# BI-ASB – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-asb/BI-ASB.apkg; APKG SHA-256 7a0706fba841a39fa40ea1e5439c99f14f59930aaa7f6d5620a33590d53350fa. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: eea4a1b952e7287bc51501f27ae2f5ec76f032fca049ee9ef600d2729e12ef40.
Původní balíčky: BI-ASB
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1695629554915

Karty Anki: 1695629554915
GUID: f>^HHRq0=u; štítky: bi-asb::p01.

### Otázka (Front)

Popište Transmission Control Program.

### Odpověď (Back)

Transmission Control Program je předchůdce Transmission Control Protocolu, který se zrodil z jeho 4. verze. Při tom došlo k rozdělení síťové a transportní vrstvy.

## Poznámka Anki 1695629768138

Karty Anki: 1695629768138
GUID: u%Ha^#6(C;; štítky: bi-asb::p01.

### Otázka (Front)

Popište Advanced Research Projects Agency Network (ARPANET).

### Odpověď (Back)

ARPANET je předchůdce internetu. Jde o jednu z prvních sítí, která stojí na přepínání paketů a implementuje sadu protokolů TCP/IP. Jako transportní protokol používal Network Control Program (NCP).

## Poznámka Anki 1695633045230

Karty Anki: 1695633045230
GUID: Fgw~A-r%g`; štítky: bi-asb::p01.

Metadata původního zdroje pro kartu 1695633045230: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište strukturu Ethernet rámce.

### Odpověď (Back)

Struktura Ethernet rámce je následující:

 [Obrázek: figure_3-3_600.png; soubor je v media/ v doprovodném ZIP] (původní alt: The Ethernet (IEEE 802.3) frame format contains source and destination addresses, an overloaded Length/Type field, a field for data, and a frame check sequence (a CRC32). Additions to the basic frame format provide for a tag containing a VLAN ID and priority information (802.1p/q) and more recently for an extensible number of tags. The preamble and SFD are used for synchronizing receivers. When half-duplex operation is used with Ethernet running at 100Mb/s or more, additional bits may be appended to short frames as a carrier extension to ensure that the collision detection circuitry operates properly. ) 

Důležité prvky:

- **preamble** - úvodní hlavička pro identifikaci rámce,

- **SFD** (start frame delimiter),

- **DST** - cílová MAC adresa,

- **SRC** - zdrojová MAC adresa,
- **P/Q tag** - obsažen v tagovaných 802.1q/p rámcích (VLAN),

- **length or type** - délka nebo Ethertype rámce,

- **FCS** (frame check sequence) - kontrola chyb pomocí CRC-32.

## Poznámka Anki 1695633340457

Karty Anki: 1695633340457
GUID: Eo&7AeV~UQ; štítky: bi-asb::p01 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište Ethernet z hlediska bezpečnosti.

### Odpověď (Back)

Ethernet trpí následujícímí bezpečnostními nedostatky:

- Ethernetová komunikace je otevřená;
- CRC-32 nezajistí obranu proti úpravě dat, protože lze jednoduše přepočítat;
- metodu CSMA/CD, lze zneužít pro DoS útoky.

## Poznámka Anki 1695633993305

Karty Anki: 1695633993305
GUID: L+4<QT-Y9<; štítky: bi-asb::p01.

Metadata původního zdroje pro kartu 1695633993305: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište strukturu IPv4 paketu.

### Odpověď (Back)

Struktura IP paketu je následující:

 [Obrázek: paste-b25065a2028e716c292e3849b1ba5de6ed8fd340.jpg; soubor je v media/ v doprovodném ZIP] 

Důležité prvky:

- **ToS** (type of service) - prioritizace paketů, nepoužívá se;

- **flags **- řídí fragmentaci;

- **TTL** (time to live) - prevence zacyklení;

- **header checksum** - kontrola proti chybám, jedničkový doplněk v inverzním kódu;

- **source address **- zdrojová IPv4 adresa;

- **destination address **- cílová IPv4 adresa.

## Poznámka Anki 1695634166248

Karty Anki: 1695634166248
GUID: AQTJyJ|[<T; štítky: bi-asb::p01 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište IPv4 z hlediska bezpečnosti.

### Odpověď (Back)

IPv4 trpí následujícími bezpečnostními nedostatky:

- IPv4 komunikace je otevřená;
- kontrolní součet nezajistí obranu proti úpravě dat, protože lze jednoduše přepočítat;
- zdrojová adresa není ověřována, což lze zneužít v DoS útocích.

## Poznámka Anki 1695635121249

Karty Anki: 1695635121249
GUID: sFS!>z%:Y#; štítky: bi-asb::p01 bi-ib::11 bi-ib::21 bi-spol::25.

### Otázka (Front)

Popište TCP a UDP z hlediska bezpečnosti.

### Odpověď (Back)

TCP a UDP trpí následujícími bezpečnostními nedostatky:

- TCP a UDP komunikace je otevřená;
- kontrolní součet nezajistí obranu proti úpravě dat, protože lze jednoduše přepočítat;
- TCP lze využít v SYN flood útocích.

## Poznámka Anki 1695635659093

Karty Anki: 1695635659093
GUID: kTM^eTl9kb; štítky: bi-asb::p01 bi-ib::11 bi-spol::25.

### Otázka (Front)

Popište strukturu TCP segmentu a UDP datagramu.

### Odpověď (Back)

Struktura TCP segmentu je následující:

 [Obrázek: paste-73e1cf9e6757371018492be37d15525c10e2e002.jpg; soubor je v media/ v doprovodném ZIP] 

Struktura UDP datagramu je následující:

 [Obrázek: paste-a30443d3d97f45e5718e2712f967f837d2773adb.jpg; soubor je v media/ v doprovodném ZIP] 

Důležité prvky:

- **pseudo-header** (červeně) - není reálnou součásti TCP/UDP hlaviček, používá se k výpočtu checksum;

- **source port **- zdrojový port;

- **destination port **- cílový port;

- **checksum** - kontrola proti chybám, jedničkový doplněk v inverzním kódu.

## Poznámka Anki 1695636531857

Karty Anki: 1695636531857
GUID: 6zk5rpJy<; štítky: bi-asb::p01 bi-ib::11.

### Otázka (Front)

Popište strukturu ARP paketu.

### Odpověď (Back)

Struktura ARP paketu je následující:

 [Obrázek: paste-b13de0c39b0e2dea56c8d9e4b3b672616764201f.jpg; soubor je v media/ v doprovodném ZIP] 

Důležité prvky:

- **hardware type **(\(\mathtt{HTYPE}\)) - typ adresy linkové vrstvy (např. Ethernet),

- **protocol type **(\(\mathtt{PTYPE}\)) - typ adresy síťové vrstvy (např. IPv4),
- **hardware address length **(\(\mathtt{HLEN}\)), **protocol address length **(\(\mathtt{PLEN}\))** **- délka adresy linkové/síťové vrstvy,
- **operation **(\(\mathtt{OPER}\)) - typ operace (request nebo reply),
- **sender hardware/protocol address **(\(\mathtt{SHA}\)/\(\mathtt{SPA}\)), **target hardware/protocol address **(\(\mathtt{THA}\)/\(\mathtt{TPA}\)) - adresa linkové/síťové vrstvy odesílatele/příjemce.

## Poznámka Anki 1695636909108

Karty Anki: 1695636909109
GUID: eyyo2w2uVG; štítky: bi-asb::p01 bi-ib::11 bi-ib::21.

### Otázka (Front)

Co je to rouge DHCP server? Jak se proti němu lze bránit?

### Odpověď (Back)

Rouge DHCP server je DHCP server, který není pod správou administrátora sítě. Vzniknout může nedbalou konfigurací nebo záměrně jako forma útoku. Obranou může být DHCP snooping - kontrola a filtrování DHCP komunikace.

## Poznámka Anki 1695637423137

Karty Anki: 1695637423137
GUID: l(18iGP8eY; štítky: bi-asb::p01 bi-ib::11.

### Otázka (Front)

Popište strukturu ICMP paketu.

### Odpověď (Back)

Struktura ICMP paketu je následující:

 [Obrázek: paste-9221e6b88e059b833e9a8783b2603874ae14e86d.jpg; soubor je v media/ v doprovodném ZIP] 

Důležité prvky:

- **type** - specifikuje ICMP type zprávy,

- **code **- specifikuje ICMP subtype zprávy.

## Poznámka Anki 1695644273339

Karty Anki: 1695644273339
GUID: r$p{?4*K&B; štítky: bi-asb::p01 bi-ib::11 bi-ib::21.

Metadata původního zdroje pro kartu 1695644273339: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište ping of death.

### Odpověď (Back)

Ping of death je typ denial-of-service (DoS) útoku, který využívá ICMP protokol (lze ale využít i další protokoly). Útočník pošle oběti fragmentovaný paket, který po zpětném sestavení překročí maximální délku IP paketu, což může způsobit buffer overflow.

