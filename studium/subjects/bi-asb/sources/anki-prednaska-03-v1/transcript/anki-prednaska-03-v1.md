# BI-ASB – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-asb/BI-ASB.apkg; APKG SHA-256 7a0706fba841a39fa40ea1e5439c99f14f59930aaa7f6d5620a33590d53350fa. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: eea4a1b952e7287bc51501f27ae2f5ec76f032fca049ee9ef600d2729e12ef40.
Původní balíčky: BI-ASB
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1696849628885

Karty Anki: 1696849628885
GUID: sm7.Lo_Cjk; štítky: bi-asb::p03 bi-ib::11 bi-ib::21.

### Otázka (Front)

Uveďte možnosti zabezpečení na úrovni switchů.

### Odpověď (Back)

Na úrovni switchů můžeme zavést následující bezpečnostní opatření:

- vypnutí nepoužívaných portů,

- omezení počtu MAC adres na port** **(Cisco Switchport Security),

- použití VLAN.

## Poznámka Anki 1696850116442

Karty Anki: 1696850116442
GUID: z&h5n!ZJ}/; štítky: bi-asb::p03 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište omezení počtu MAC adres na port** **(Cisco Switchport Security).

### Odpověď (Back)

Cisco Switchport Security je bezpečnostní opatření na úrovni switchů. Působí jako efektivní obrana proti MAC flooding útokům. Pro každý port umožňuje nastavit seznam či počet povolených MAC adres a to následujícími způsoby:

- **static **- pevně daný seznam;

- **dynamic** - naučený seznam na základě provozu na portu;

- **sticky** - statický či dynamický seznam, který je permanentně uložen.

V případě, že je počet překročen, nebo je připojena MAC adresa, která se na seznamu nenachází, umožňuje Switchport Security provést následující akce:

- **protect** - switch zahazuje rámce od adresy, která porušuje konfiguraci;

- **restrict** - switch zahazuje rámce od adresy, která porušuje konfiguraci, a dojde k vytvoření události a logování;

- **shutdown** - switch úplně vypne port.

## Poznámka Anki 1696851448166

Karty Anki: 1696851448166
GUID: yMotE~hg-V; štítky: bi-asb::p03.

Metadata původního zdroje pro kartu 1696851448166: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to virtual local area network (VLAN)?

### Odpověď (Back)

Virtual local area network (VLAN) je logicky izolovaná část Ethernetové sítě, která odděluje toky dat na linkové vrstvě. Používá k tomu tagované 802.1q rámce. Používají se zejména za účelem:

- **kompartmentalizace** - rozdělení síťových uzlů do skupin podle prostředků, ke kterým přistupují;

- **segregace** - oddělení toků dat jednotlivých skupin uzlů.

Navíc odděluje broadcastové domény, tedy funguje jako ochrana proti broadcastovým bouřím (broadcast storms).

## Poznámka Anki 1696852167102

Karty Anki: 1696852167102
GUID: Cbl=RUp_Zb; štítky: bi-asb::p03.

Metadata původního zdroje pro kartu 1696852167102: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

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

## Poznámka Anki 1696852852123

Karty Anki: 1696852852123
GUID: LA~pc0#!8=; štítky: bi-asb::p03 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište VLAN hopping.

### Odpověď (Back)

VLAN hopping je typ útoku na switche s cílem získat přístup do VLAN, které by za normálních okolností němely být přístupné. VLAN hoppingu lze dosáhnout dvěma strategiemi:

- double tagging,

- switch spoofing.

## Poznámka Anki 1696853142842

Karty Anki: 1696853142842
GUID: zF+J)`_;Bk; štítky: bi-asb::p03 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište VLAN hopping přístupem double tagging. Jak jej lze mitigovat?

### Odpověď (Back)

VLAN hopping útok použitím přístupu double tagging vypadá následovně:

- Útočník do hlavičky Ethernet rámce zařadí dva 802.1q tagy za sebe.
- První switch na access portu odebere první tag a přepošle rámec na trunk port.
- Druhý switch vidí pouze druhý tag a zařadí rámec do odpovídající VLAN.

 [Obrázek: paste-386a48bced480c972a18f90c2693267778b97b94.jpg; soubor je v media/ v doprovodném ZIP] 

Mitigací je nepoužívat VLAN 1 pro access porty.

## Poznámka Anki 1696853352580

Karty Anki: 1696853352580
GUID: KsMvv;z6r6; štítky: bi-asb::p03 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište VLAN hopping přístupem switch spoofing. Jak jej lze mitigovat?

### Odpověď (Back)

VLAN hopping útok použitím přístupu switch spoofing vypadá následovně:

- Útočník se připojí na port switche a imituje chování trunking switche pomocí protokolů jako Multiple VLAN Registration Protocol nebo Dynamic Trunking Protocol.
- Na připojeném portu vznikne trunk, čímž útočník získá přístup k provozu všech VLAN.

Útok lze mitigovat následujícími způsoby:

- explicitně na portu nastavit, že se jedná o access port;
- vypnout na portu trunking protokoly.

## Poznámka Anki 1696854120388

Karty Anki: 1696854120388
GUID: bU/vBid3c3; štítky: bi-asb::p03 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište Spanning Tree Protocol (STP).

### Odpověď (Back)

Spanning Tree Protocol je protokol používaný k sestavení kostry topologie Ethernetové sítě. Tím se snaží předějít vzniku smyček (switching loops), které mohou zavinit broadcastové bouře (broadcast storms). Jeden ze switchů je na základě definované priority (a sekundárně dle nižší MAC adresy) zvolen za kořen (root) a od něj je poté dle rychlosti linek budována kostra.

## Poznámka Anki 1696854420702

Karty Anki: 1696854420702
GUID: d0Np#j}^uF; štítky: bi-asb::p03 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište útok na Spanning Tree Protocol (STP). Jak jej lze mitigovat?

### Odpověď (Back)

Útok na Spanning Tree Protocol (STP) probíhá následovně:

- Útočník připojí do sítě switch či zařzení, které funkci switche napodobuje, s vysokou STP prioritou (případně ještě nízkou MAC adresou).
- Toto zařízení se stane kořenovým (root) switchem kostry topologie, což zapříčiní, že je přes něj posílán provoz ostatních switchů.

Útok lze mitigovat následujícími způsoby:

- zakázat zvolení nově přidaných switchů jako kořenové (Root Guard),
- zahazování Bridge Protocol Data Unit (BPDU) na access portech (BPDU Guard).

## Poznámka Anki 1696855384433

Karty Anki: 1696855384433
GUID: C7UlR(YtR4; štítky: bi-asb::p03 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište DHCP spoofing. Jak jej lze mitigovat?

### Odpověď (Back)

DHCP spoofing je útok zaměřený na protokol DHCP s cílem asociovat útočníkovu IP adresu jako výchozí bránu a případně DNS server na straně oběti. Útočník může postupovat následovně:

- Nejdříve může útočník vykonat DHCP starvation útok, kterým vyčerpá adresy legitimního DHCP serveru.
- Následně útočník spustí svůj vlastní DHCP server a začne obětem poskytovat síťovou konfiguraci, ve které nastaví svou IP adresu jako výchozí bránu a případně DNS server.
- Tímto způsoběm na sebe přesměruje veškerou komunikaci a získává man-in-the-middle pozici.

Útok lze mitigovat následujícími způsoby:

- definováním portů, na kterých leží důvěryhodné DHCP servery,
- kombinací DHCP snooping a Dynamic ARP Inspection (DAI) - zahazování paketů s neplatnou kombinací MAC a IP adresy.

## Poznámka Anki 1697461537751

Karty Anki: 1697461537751
GUID: qOs7}HxxQ&; štítky: bi-asb::p03 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište access control list (ACL) na úrovni síťových prvků. Jaké jsou jeho výhody a nevýhody?

### Odpověď (Back)

Access control list (ACL) je bezpečnostní opatření na úrovni routerů. Jde o seznam access control entries (ACE), které filtrují síťový provoz. Rozlišujeme:

- standard ACL - podporuje filtrování na základě zdrojové IP adresy,

- extended ACL - podporuje filtrování na základě zdrojových a cílových IP adres, portů či protokolu.

Mezi výhody ACL patří rychlost a jednoduchost. Naopak nevýhodou je, že záznamy jsou statické a jsou vyhodnocovány bezestavově.

## Poznámka Anki 1697463954568

Karty Anki: 1697463954569
GUID: B9fR3#Fdn7; štítky: bi-asb::p03.

Metadata původního zdroje pro kartu 1697463954569: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište firewall.

### Odpověď (Back)

Firewall je síťové zařízení nebo aplikace, která monitoruje příchozí a odchozí provoz a na základě definovaných pravidel určuje, zda bude provoz povolen nebo blokován.

## Poznámka Anki 1697463971566

Karty Anki: 1697463971566
GUID: FOK]4g-.s^; štítky: bi-asb::p03.

Metadata původního zdroje pro kartu 1697463971566: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište druhy firewallů.

### Odpověď (Back)

Rozlišujeme následující tři základní druhy firewallů:

| **síťový firewall **(packet filtering firewall) | **stavový firewall **(stateful firewall) | **aplikační firewall **(application firewall) | 
| pracuje na síťové vrstvě | pracuje na transportní vrstvě | pracuje na aplikační vrstvě | 
| filtruje provoz na základě IP adres | filtruje provoz na základě TCP/UDP relací | filtruje provoz na základě heuristik, signatur a detekce anomálií | 
| ochrana před port scanningem a útoky ze zón s nižší ochranou | ochrana před port scanningem, DoS a session hijackingem | ochrana před XSS, injection útoky a DoS |

