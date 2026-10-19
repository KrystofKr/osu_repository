# BI-PSI – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 15 poznámek, 15 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1646051061287

Karty Anki: 1646051061288
GUID: JO/d<aXteg; štítky: bi-ib::11 bi-ib::21 bi-psi::p03.

### Otázka (Front)

Jaké jsou důvody pro využití virtual local area network (VLAN)?

### Odpověď (Back)

Virtual local area network (VLAN) dokáže zajistit:

- **přehlednost **- provoz je rozdělen na základě definovaných skupin,
- **bezpečnost **- jednotlivé skupiny se nemohou navzájem ovlivňovat,
- **efektivita **- každá VLAN odbavuje jen provoz své skupiny uzlů,
- **jednoduchost **- administrátor může skupiny spravovat separátně.

## Poznámka Anki 1646051103076

Karty Anki: 1646051103076
GUID: CJJPvgT$Y0; štítky: bi-ib::11 bi-ib::21 bi-psi::p03.

### Otázka (Front)

Co je to trunk port?

### Odpověď (Back)

Trunk port je port, který přenáší provoz několika různých VLAN.

## Poznámka Anki 1646051279208

Karty Anki: 1646051279208
GUID: m^|E+uA|Ju; štítky: bi-ib::11 bi-ib::21 bi-psi::p03.

### Otázka (Front)

Podle čeho se provoz dělí mezi VLAN sítě?

### Odpověď (Back)

- dle rozhraní (VLAN se vybere podle konkrétního rozhraní na přepínači)
- dle adres (rámec je zařazen do VLAN skupiny dle MAC adresy)
- dle protokolu (rámec je zařazen podle protokolu vyšší vrstvy, který přenáší)
- dle značky (rámec se zařadí podle tagu, který je připojen v hlavičce rámce)

## Poznámka Anki 1646051580642

Karty Anki: 1646051580643
GUID: b~&u+a$Bjr; štítky: bi-ib::11 bi-ib::21 bi-psi::p03.

### Otázka (Front)

Popište 802.1q hlavičku tagovaného rámce.

### Odpověď (Back)

Hlavička 802.1q tagovaného rámce má následující strukturu:

 [Obrázek: paste-e9b0b3d462cc64e0cf50d07af8e3cf0bc6243eb8.jpg; soubor je v media/ v doprovodném ZIP] 

Důležité prvky:

- **tag protocol identifier **(TPI) - identifikuje tagovaný rámec, stojí na místě length or type (Ethertype) parametru běžného rámce;

- **tag control information **(TCI):

- **priority code point **(PCP) - určuje prioritu;

- **drop eligible indicator **(DEI) - označuje rámec, který lze zahodit při přetížení linky;

- **VLAN identifier **(VID) - určuje VLAN, do které rámec patří.

## Poznámka Anki 1646051947029

Karty Anki: 1646051947029
GUID: e@Y]5Cmo6{; štítky: bi-ib::11 bi-psi::p03.

### Otázka (Front)

Co je primárním úkolem síťové vrstvy, jaké využívá protokoly, v jaké podobě doručuje data a jaký je její rozdíl oproti linkové vrstvě.

### Odpověď (Back)

Primárním úkolem síťové vrstvy je doručování dat mezi stanicemi, které se nacházejí v různých sítích, definuje IP adresy. Využívá IP (Internet Protocol) a ICMP (Internet Control Message Protocol). Data jsou doručována po paketech (až 64 KB). Adresace síťové vrstvy je hierarchická, je tedy vhodná pro směrování.

## Poznámka Anki 1646052477305

Karty Anki: 1646052477305
GUID: ErB+vHeqO3; štítky: bi-psi::p03.

### Otázka (Front)

Vyjmenujte speciální adresní rozsahy u IPv4.

### Odpověď (Back)

- privátní adresy (pouze místní sítě)

- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

- link-local (lokální, mohou se přiřadit automaticky)

- 169.254.0.0/16

- loop-back (provoz sám sobě)

- 127.0.0.0/24

- multicast (doručování dat skupině)

- 224.0.0.0/24

## Poznámka Anki 1646052689412

Karty Anki: 1646052689412
GUID: PM7e0l`Fdi; štítky: bi-ib::11 bi-psi::p03.

Metadata původního zdroje pro kartu 1646052689412: původní příznak autora 7.

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

## Poznámka Anki 1646052729796

Karty Anki: 1646052729797
GUID: gU>`[l#P`; štítky: bi-psi::p03.

### Otázka (Front)

Co je to hop a jak souvísí s TTL?

### Odpověď (Back)

Hop je průchod paketu směrovačem. Každý takový průchod sníží hodnotu TTL o jedna.

## Poznámka Anki 1646053150731

Karty Anki: 1646053150732
GUID: PhIBzJ9msJ; štítky: bi-psi::p03.

### Otázka (Front)

Co je to směrování?

### Odpověď (Back)

Je to mechanizmus hledání cesty mezi zdrojovou a cílovu adresou,tedy odeslání konkrétního paketu prostředníctvním zvoleného odchozího síťového rozhraní na základě cílové adresy uvedené v hlavičce paketu. Pro určení odchozího rozhraní směrovače slouží směrovací tabulka, která obsahuje směrovací záznamy.

## Poznámka Anki 1646053376501

Karty Anki: 1646053376502
GUID: QSnayj+3L~; štítky: bi-psi::p03.

### Otázka (Front)

Co je to fragmentace IP paketů.

### Odpověď (Back)

Pokud je velikost IP paketu větší než maximální velikost části rámce linkové vrstvy určené pro data, musí se paket přenášet po částech (fragmentech).

## Poznámka Anki 1646053522305

Karty Anki: 1646053522306
GUID: l*$@;L0M8_; štítky: bi-psi::p03.

### Otázka (Front)

Co je to NAT?

### Odpověď (Back)

Network Address Translation funguje tak, že privátní adresy se při průchodu směrovačem nahradí veřejnou (směrovatelnou) adresou směrovače.

## Poznámka Anki 1646053631713

Karty Anki: 1646053631713
GUID: J]IYe;1M%b; štítky: bi-ib::11 bi-psi::p03.

### Otázka (Front)

Co je to Internet Control Message Protocol (ICMP)? Kde se používá?

### Odpověď (Back)

ICMP je podpůrný protokol, který není určen k přenosu dat. Používá se k diagnostice spojení mezi zařízeními v síti provozující IP. Využívá se v utilizách \(\mathtt{ping}\) a \(\mathtt{traceroute}\) či \(\mathtt{tracert}\).

## Poznámka Anki 1646053681523

Karty Anki: 1646053681523
GUID: owgwx@CPIi; štítky: bi-psi::p03.

### Otázka (Front)

Co je to ARP?

### Odpověď (Back)

Adress Resolution Protocol je schopen namapovat konkrétní síťovou adresu (IP) na linkovou adresu (MAC).

## Poznámka Anki 1646053934815

Karty Anki: 1646053934815
GUID: oST}Ow^]Hf; štítky: bi-ib::11 bi-psi::p03.

### Otázka (Front)

Co je to DHCP?

### Odpověď (Back)

Dynamic Host Configuration Protocol slouží k automatické nastavení IP adresy na klientské stanici. Komunikace probíhá ve čtyřech fázích:

- DHPC Discover
- DHPC Offer
- DHPC Request
- DHPC ACK

## Poznámka Anki 1696851468514

Karty Anki: 1696851468515
GUID: O=wMJ.b|)(; štítky: bi-ib::11 bi-ib::21 bi-psi::p03.

Metadata původního zdroje pro kartu 1696851468515: původní příznak autora 7.

### Otázka (Front)

Co je to virtual local area network (VLAN)?

### Odpověď (Back)

Virtual local area network (VLAN) je logicky izolovaná část Ethernetové sítě, která odděluje toky dat na linkové vrstvě. Používá k tomu tagované 802.1q rámce. Používají se zejména za účelem:

- **kompartmentalizace** - rozdělení síťových uzlů do skupin podle prostředků, ke kterým přistupují;

- **segregace** - oddělení toků dat jednotlivých skupin uzlů.

Navíc odděluje broadcastové domény, tedy funguje jako ochrana proti broadcastovým bouřím (broadcast storms).

