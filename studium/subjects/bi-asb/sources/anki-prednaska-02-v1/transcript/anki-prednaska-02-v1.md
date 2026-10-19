# BI-ASB – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-asb/BI-ASB.apkg; APKG SHA-256 7a0706fba841a39fa40ea1e5439c99f14f59930aaa7f6d5620a33590d53350fa. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: eea4a1b952e7287bc51501f27ae2f5ec76f032fca049ee9ef600d2729e12ef40.
Původní balíčky: BI-ASB
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1696234681813

Karty Anki: 1696234681813
GUID: h8QHDj)$b5; štítky: bi-asb::p02 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište hub (opakovač).

### Odpověď (Back)

Hub (opakovač) je síťový prvek fyzické vrstvy. Funguje tak, že data přijímaná na vstupním portu jsou replikována na všechny výstupní porty. V dnešní době jde o překonané zařízení.

## Poznámka Anki 1696234816177

Karty Anki: 1696234816177
GUID: wdz&PK<#8h; štítky: bi-asb::p02 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište hub (opakovač) z hlediska bezpečnosti.

### Odpověď (Back)

Hub (opakovač) trpí následujícími bezpečnostními nedostatky:

- v síti, které je postavená na hubech může kdokoliv odposlouchávat veškerá přenášená data,
- jakákoliv stanice může způsobovat neustálé kolize, čímž může docílit DoS.
- dovoluje velmi omezené možnosti nastavení.

## Poznámka Anki 1696236116354

Karty Anki: 1696236116354
GUID: d%iPo%+g6h; štítky: bi-asb::p02 bi-ib::21.

Metadata původního zdroje pro kartu 1696236116354: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište switch (přepínač).

### Odpověď (Back)

Switch (přepínač) je síťový prvek linkové vrstvy, který přeposílá rámce na základě MAC adresy. Pro výběr portu, na který bude rámec přesměrován, se používá switching table (CAM table), která obsahuje asociace portů a MAC adres. Switch také odděluje kolizní domény, broadcastové však ne.

## Poznámka Anki 1696236215861

Karty Anki: 1696236215861
GUID: LOWR2Y|7zi; štítky: bi-asb::p02 bi-ib::21.

Metadata původního zdroje pro kartu 1696236215861: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište MAC flooding. Jak jej lze mitigovat?

### Odpověď (Back)

MAC flooding je útok cílený na switche (přepínače), který běžně probíhá následujícím způsobem:

- Útočník zaplní MAC tabulku switche pomocí velkého množství rámců s podvrženými MAC adresami, čímž vytlačí používané záznamy.
- Aby se switch znovu naučil vytlačené záznamy musí broadcastovat rámce na všechny své porty.
- Útočník využije packet analyzer k zachycení přenášených rámců.
MAC flooding lze mitigovat pomocí port-based network access control (802.1x).

## Poznámka Anki 1696237793792

Karty Anki: 1696237793792
GUID: f]3lGZ_X7-; štítky: bi-asb::p02 bi-spol::25.

Metadata původního zdroje pro kartu 1696237793792: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

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

## Poznámka Anki 1696238351993

Karty Anki: 1696238351993
GUID: P)(g0uC`Dp; štítky: bi-asb::p02 bi-ib::11.

Metadata původního zdroje pro kartu 1696238351993: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište TCP/IP model.

### Odpověď (Back)

TCP/IP model je konceptuální model vyvinutý DARPA, který rozděluje komunikaci mezi počítačovými systémy do několika abstraktních vrstev, které korespondují s vrstvami z OSI modelu násldujícím způsobem:

| 
      **vrstva OSI modelu** | **vrstva TCP/IP modelu** | 

| 
      aplikační
prezentační
relační | 
      aplikační | 

| 
      transportní
 | 
      transportní | 

| 
      síťová | 
      internetová | 

| 
      linková
fyzická | 
      linková |

## Poznámka Anki 1696239001205

Karty Anki: 1696239001206
GUID: BuUS,&vM:=; štítky: bi-asb::p02 bi-ib::11.

### Otázka (Front)

Popište three-layer hierarchical model včetně možných bezpečnostních opatření.

### Odpověď (Back)

Three-layer hierarchical model je konceptuální model vyvinutý společností Cisco, který dělí sítě do následujících vrstev:           
|             **vrstva** |       **využití** |             **opatření** |         
|       core |       velkokapacitní přenos s nízkou latencí a připojení k internetu |       problematická aplikace bezpečnosti |             
|             distribution |       propojení jednotlivých access zón
 |       filtrování paketů, firewall, oddělení
broadcastových a multicastových domén |         
|             access |       připojení koncových zařízení
 |       VLAN, ochrana proti základním
útokům (ARP, DHCP apod.) |

## Poznámka Anki 1696239662002

Karty Anki: 1696239662002
GUID: CFh9~_=EnO; štítky: bi-asb::p02.

### Otázka (Front)

Popište IOS planes model.

### Odpověď (Back)

IOS planes model je konceptuální model vyvinutý společností Cisco, který rozšiřuje OSI model o nový rozměr. Síť dělí na následující vrstvy (planes):

- **data plane** - přenos uživatelských dat;

- **control plane **- řízení síťových prvků data plane;

- **management plane** - správa, konfigurace a monitoring.

## Poznámka Anki 1696240250210

Karty Anki: 1696240250210
GUID: vz6TVV`aBx; štítky: bi-asb::p02 bi-ib::11.

### Otázka (Front)

Popište service-oriented network architecture (SONA).

### Odpověď (Back)

Service-oriented network architecture je konceptuální model vyvinutý společností Cisco. Jeho hlavní myšlenkou je oddělit aplikace od obecně použitelných síťových služeb a fyzické infrastruktury. Síť dělí na následující vrstvy:

- **application layer **- aplikace využívající síťové služby,

- **network/interactive services layer **- obecné síťové služby (security, management, storage a další),

- **physical/networked infrastructure layer** - fyzická síťová infrastruktura (WAN, MAN, data centra a další).

## Poznámka Anki 1696240441514

Karty Anki: 1696240441514
GUID: FS=V3+-x4i; štítky: bi-asb::p02 bi-ib::11 bi-ib::21.

Metadata původního zdroje pro kartu 1696240441514: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Uveďte základní typy útoků na síti.

### Odpověď (Back)

Mezi základní typy útoků na síti patří:

- odposlouchávání (eavesdropping),

- modifikace dat** **(tampering),

- podvržení (spoofing),

- útoky na hesla,

- denial of service útoky (DoS),

- man-in-the-middle útoky (MITM),

- hijacking

a další.

## Poznámka Anki 1696240655671

Karty Anki: 1696240655671
GUID: LY{wF$I#v!; štítky: bi-asb::p02 bi-asb::p08 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište AAA framework.

### Odpověď (Back)

AAA framework je framework sloužící k řízení a sledování přístupů v počítačové síti. Skládá se ze tří složek:

- **authentication** - prokázání identity,

- **authorization** - kontrola oprávnění,

- **accounting** - logování a monitorování.

## Poznámka Anki 1696241316282

Karty Anki: 1696241316282
GUID: QNkG8Gv%W; štítky: bi-asb::p02 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište rozdíl mezi segmentací a segregací počítačových sítí.

### Odpověď (Back)

**Segmentace** označuje rozdělování síťě na menší podsíťě, zatímco **segregace **označuje oddělení přístupů a vymáhání různých přistupových oprávnění pro jednotlivé koncové uživatele sítě (např. pomocí VLAN, firewallů, VPN a podobně).

