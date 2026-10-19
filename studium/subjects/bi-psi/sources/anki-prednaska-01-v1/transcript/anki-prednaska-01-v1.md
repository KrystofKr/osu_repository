# BI-PSI – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 15 poznámek, 15 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1644841701678

Karty Anki: 1644841701679
GUID: k?j>g`8SI]; štítky: bi-ib::11 bi-psi::p01.

### Otázka (Front)

Jak rozdělujeme počítačové sítě?

### Odpověď (Back)

Přepojování:

- okruhů (connection-oriented, circuit switching) - ATM, FrameRelay

- **okruh** = sestavená trasa, inspirace analog. ústřednami

- paketů (connectionless, packet switching) - Ethernet

- **paket** = balíček odesílaných dat

Architektura:

- peer-to-peer
- client-server
Použítí:

- veřejná
- privátní
- hybridní
Dle rozlehlosti:

- osobní (1 m) - Personal Area Network (PAN)
- místní (100 m) - Local Area Network (LAN)
- městské (10 km) - Metropolitan Area Network (MAN)
- rozlehlé (1000 km) - Wide Area Network (WAN)

## Poznámka Anki 1644841761650

Karty Anki: 1644841761650
GUID: o3v-Z@PFc.; štítky: bi-psi::p01.

### Otázka (Front)

Co je to topologie sítě?

### Odpověď (Back)

Topologie je způsob uspořádání propojení linek mezi stanicemi (uzly) v síti. Volba topologie souvisí s konkrétním využítím sítě a lze kombinovat (vznikají hybridní topologie).

## Poznámka Anki 1644841916928

Karty Anki: 1644841916928
GUID: PWUHb~1+<~; štítky: bi-psi::p01.

### Otázka (Front)

Uveďte příklady topologií sítí a zakreslete je.

### Odpověď (Back)

Příklady síťových topologií jsou: kruh, hvězda, plně propojená, přímá, strom, sběrnice.
 [Obrázek: paste-90fbc9a706133d8358679284ab2e59020ffde53a.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1644842021349

Karty Anki: 1644842021349
GUID: t/HJ&:6`7/; štítky: bi-psi::p01.

### Otázka (Front)

Jaké rozlišujeme druhy linek dle možnosti vysílání a příjmu?

### Odpověď (Back)

Rozlišujeme následující typy linek:

- **simplex **- komunikace probíhá pouze jedním směrem;
- **duplex **- komunikace probíhá obousměrně;
- **half-duplex** - komunikace může probíhat oběma směry, ale najednou lze komunikovat pouze jednosměrně.
 [Obrázek: paste-20229215ee6af9c4f418904d4787afcd7edc3cbe.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1644842459581

Karty Anki: 1644842459581
GUID: Pi9_)U+_&$; štítky: bi-psi::p01.

### Otázka (Front)

Jaké rozlišujeme druhy komunikačních operací v počítačových sítích?

### Odpověď (Back)

- unicast - zúčastněný je pouze jeden vysílač a jeden přijímač
- multicast - zúčastněný je jeden vysílač a několik přijímačů
- broadcast - zúčastněný je jeden vysílač a všechny přijímače
- anycast - zúčastněný je jeden vysílač a jeden z několika možných přijímačů

## Poznámka Anki 1644844513155

Karty Anki: 1644844513155
GUID: e%Hp/V;r!f; štítky: bi-psi::p01.

### Otázka (Front)

Jaká zařízení typicky v síti pracují a na jakých vrstvách?

### Odpověď (Back)

- hub a repeater - fyzická vrstva
- switch - linková vrstva
- router - síťová vrstva

## Poznámka Anki 1644844662225

Karty Anki: 1644844662225
GUID: zrDX@E|0,=; štítky: bi-psi::p01.

### Otázka (Front)

Co je to IP?

### Odpověď (Back)

Internet Protocol (IP) je základní komunikační protokol, který umožňuje doručování dat mezi stanicemi (uzly). Každé konkrétní stanici přiřazuje jednu konkrétní IP adresu. Je hierarchický, tedy má logickou strukturu a umožňuje tak vytvářet topologie a spojovat adresy ve větší celky.

## Poznámka Anki 1644865385809

Karty Anki: 1644865385810
GUID: G{dng*3/<=; štítky: bi-psi::p01 bi-spol::24.

Metadata původního zdroje pro kartu 1644865385810: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolik adres lze přiřadit pomocí IPv4 a kolik pomocí IPv6?

### Odpověď (Back)

- IPv4: \(2^{32}\)
- IPv6: \(2^{128}\)

## Poznámka Anki 1644865508066

Karty Anki: 1644865508066
GUID: b?4`/:Dx;m; štítky: bi-psi::p01.

### Otázka (Front)

Co určuje síťová maska?

### Odpověď (Back)

Maska určuje, jakou část IP adresy mají všichni členové dané sítě (segmentu) společnou.

## Poznámka Anki 1644865584717

Karty Anki: 1644865584717
GUID: d!ZFvEU$;t; štítky: bi-psi::p01.

### Otázka (Front)

Co určuje prefix?

### Odpověď (Back)

Prefix určuje počet bitů IP adresy, které jsou společné pro všechny členy sítě (segmentu).

## Poznámka Anki 1644865777976

Karty Anki: 1644865777977
GUID: NHFM-*`=0~; štítky: bi-psi::p01.

### Otázka (Front)

Jak odvodíme z prefixu masku sítě?

### Odpověď (Back)

Hodnota prefixu odpovídá počtu jedniček (zleva) v masce a zbytek doplníme nulami.
Tedy prefix IP/30 odpovídá:
11111111 11111111 11111111 11111100
255.255.255.252

## Poznámka Anki 1644865859808

Karty Anki: 1644865859808
GUID: DnA^K?9S#H; štítky: bi-psi::p01.

### Otázka (Front)

Co je to adresa sítě, jak ji lze získat a jaká je její obecná hodnota?

### Odpověď (Back)

Adresa sítě označuje všechny IP adresy patřící do daného adresního rozsahu.
Lze získat skrze bitový AND masky a libovolné adresy z dané sítě. Obecně jde o nejnižší adresu daného rozsahu.

## Poznámka Anki 1644865942327

Karty Anki: 1644865942327
GUID: {y)h+]UAo; štítky: bi-psi::p01.

### Otázka (Front)

Co je to brána a jaká adresa se jí přiřazuje?

### Odpověď (Back)

Brána je implicitní směrovač pro komunikaci mimo lokální síť.
Přiřazujeme jí (typicky) druhou nejvyšší nebo druhou nejnižší adresu v daném rozsahu.

## Poznámka Anki 1644866043945

Karty Anki: 1644866043945
GUID: Qb(uh|X/_7; štítky: bi-psi::p01.

### Otázka (Front)

Co je to broadcast (všesměr) a jakou adresu mu přiřazujeme?

### Odpověď (Back)

Broadcast je zpráva, kterou obdrží všechny stanice v síti. Přiřazujeme mu nejvyšší adresu v daném rozsahu.

## Poznámka Anki 1696237632225

Karty Anki: 1696237632225
GUID: gpqt6lm7oM; štítky: bi-ib::11 bi-ib::21 bi-psi::p01.

### Otázka (Front)

Popište Open Systems Interconnection (OSI) model včetně protokolů a datových jednotek používaných na jednotlivých vrstvách.

### Odpověď (Back)

Open Systems Interconnection (OSI) model je konceptuální model vyvinutý ISO, který rozděluje komunikaci mezi počítačovými systémy do následujících abstraktních vrstev:

|       
      **vrstva** | 
      **protokoly** |       
      **datová jednotka** | 

| 
      aplikační | 
      HTTP, FTP, DNS | 
      vlastní data | 

|       
      prezentační | 
      SSL/TLS, Tox | 
      vlastní data | 

|       
      relační | 
      SIP, NFS, SMB | 
      vlastní data | 

|       
      transportní | 
      TCP, UDP | 
      segmenty a datagramy | 

|       
      síťová | 
      IP, ICMP | 
      pakety | 

|       
      linková | 
      Ethernet, ARP | 
      rámce | 

|       
      fyzická | 
      metalické či optické kabely | 
      bity |

