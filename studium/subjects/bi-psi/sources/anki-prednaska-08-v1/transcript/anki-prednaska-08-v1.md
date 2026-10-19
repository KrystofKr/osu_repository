# BI-PSI – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 19 poznámek, 19 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1649071492527

Karty Anki: 1649071492529
GUID: s;A`nR>@=n; štítky: bi-ib::11 bi-ib::21 bi-psi::p08.

### Otázka (Front)

Popište firewall.

### Odpověď (Back)

Firewall je síťové zařízení nebo aplikace, která monitoruje příchozí a odchozí provoz a na základě definovaných pravidel určuje, zda bude provoz povolen nebo blokován.

## Poznámka Anki 1649071548627

Karty Anki: 1649071548627
GUID: C;9LnP+vw~; štítky: bi-ib::21 bi-psi::p08.

### Otázka (Front)

Definujte DMZ.

### Odpověď (Back)

Demilitarizovaná zóna je část počítačové sítě, která je plně nebo částečně přístupná z vnější sítě. Umisťují se do ní servery zpřístupňující služby libovolným uživatelům.

## Poznámka Anki 1649071576421

Karty Anki: 1649071576421
GUID: i.u-kMrZ)Y; štítky: bi-psi::p08.

### Otázka (Front)

Definujte intranet.

### Odpověď (Back)

Intranet je vnitřní část sítě, která je přístupná pouze oprávněným uživatelům.

## Poznámka Anki 1649071771097

Karty Anki: 1649071771097
GUID: pZ#@7[]c_-; štítky: bi-ib::11 bi-ib::21 bi-psi::p08 bi-spol::25.

### Otázka (Front)

Popište druhy firewallů.

### Odpověď (Back)

Rozlišujeme následující tři základní druhy firewallů:

| **síťový firewall **(packet filtering firewall) | **stavový firewall **(stateful firewall) | **aplikační firewall **(application firewall) | 
| pracuje na síťové vrstvě | pracuje na transportní vrstvě | pracuje na aplikační vrstvě | 
| filtruje provoz na základě IP adres | filtruje provoz na základě TCP/UDP relací | filtruje provoz na základě heuristik, signatur a detekce anomálií | 
| ochrana před port scanningem a útoky ze zón s nižší ochranou | ochrana před port scanningem, DoS a session hijackingem | ochrana před XSS, injection útoky a DoS |

## Poznámka Anki 1649071860254

Karty Anki: 1649071860255
GUID: Ox+<@0l>M$; štítky: bi-psi::p08.

### Otázka (Front)

Jaký linuxový paketový firewall se běžně využívá?

### Odpověď (Back)

iptables / nftables

## Poznámka Anki 1649072000603

Karty Anki: 1649072000603
GUID: OBk25;IX1<; štítky: bi-psi::p08.

### Otázka (Front)

Popište úrovně pravidel práce s pakety u iptables.

### Odpověď (Back)

- **prerouting** - týká se všech paketů před provedením směrovacího rozhodnutí
- **postrouting** - týká se všech paketů po provedení směrovacího rozhodnutí
- **forward** - týká se pouze přeposílaných paketů
- **input** - týká se pouze paketů určených místním aplikacím
- **output** - týká se pouze paketů generovaných místními aplikacemi

 [Obrázek: paste-91fa23be806b8e06b5077567967ba77e2a1fd1d4.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1649072079152

Karty Anki: 1649072079152
GUID: tB<@2?+VI; štítky: bi-psi::p08.

### Otázka (Front)

Jaké tabulky pravidel rozlišuje iptables?

### Odpověď (Back)

- **filter** - povolení či zakázání doručení paketu
- **nat** - překlad IP adres či portů v hlavičce paketu
- **mangle** - úpravy položek v hlavičce paketu

## Poznámka Anki 1649072242507

Karty Anki: 1649072242507
GUID: kM+Ep!!n`<; štítky: bi-psi::p08.

### Otázka (Front)

Popište Deep Packet Inspection (DPI).

### Odpověď (Back)

Díky **signatuře** (specifickému jednoznačnému řetězci/otisku) lze s vysokou pravděpodobností identifikovat hlavičky konkrétních paketů a na základě toho provést další akce.

## Poznámka Anki 1649072448592

Karty Anki: 1649072448592
GUID: KY4cXpCl^{; štítky: bi-psi::p08.

### Otázka (Front)

Popište fungování aplikačního firewallu a důvod jeho použití.

### Odpověď (Back)

Aplikační firewall funguje v několika fázích:

1. zdrojová stanice (ZS) se obrací prostředníctvím aplikačního protokolu na aplikační firewall (AF)
2. AF zkopíruje požadavek, nastaví sebe jako původce požadavku a kontaktuje cílový server (CS)
3. CS vrátí odpověd AF
4. AF přepošle odpověd ZS
Díky AF můžeme skrýt zdrojové IP adresy a snížit množství odchozího provozu pomocí kešování.

## Poznámka Anki 1649072537716

Karty Anki: 1649072537717
GUID: F-ZHA~e$Rr; štítky: bi-ib::11 bi-ib::21 bi-psi::p08 bi-spol::25.

### Otázka (Front)

Popište činnost IDS.

### Odpověď (Back)

Intrusion Detection System průběžně provádí kontrolu příchozího provozu a detekci hrozeb. Pokud je hrozba detekována, upozorní administrátora, který provede adekvátní opatření.

## Poznámka Anki 1649072623722

Karty Anki: 1649072623732
GUID: y6c*o?VP7w; štítky: bi-ib::11 bi-psi::p08 bi-spol::25.

### Otázka (Front)

Popište činnost IPS.

### Odpověď (Back)

Intrusion Prevention System provádí analýzu příchozího i odchozího provozu a detekci hrozeb. Pokud je zjištěna hrozba,  zašle pokyn k vygenerování či aktivaci pravidla, kterým se např. provoz odfiltruje.

## Poznámka Anki 1649072728975

Karty Anki: 1649072728976
GUID: jgka^zoM]1; štítky: bi-ib::21 bi-psi::p08.

### Otázka (Front)

Popište fungování honeypotu.

### Odpověď (Back)

Do DMZ se umístí honeypot, který vytváří dojem zranitelné síťové služby. Pokud útočník tuto službu napadne, zaznamenají se o něm informace, které jsou poté využity pro vytvoření firewall pravidel, která zamezí dalším útokům.

## Poznámka Anki 1649073267706

Karty Anki: 1649073267706
GUID: E?~1.LfWoz; štítky: bi-ib::21 bi-psi::p08.

Metadata původního zdroje pro kartu 1649073267706: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište skenování portů (port scanning).

### Odpověď (Back)

Skenování portů (port scanning) je technika používáná k detekci otevřených portů na vzdáleném zařízení. Jejím cílem je identifikovat služby, které na zařízení běží a přijímají spojení. Podle formátu skenu rozlišujeme dva typy skenování portů:

- **horizontální** - skenování konkrétního portu napříč vícero zařízeními,

- **vertikální** - skenování vícero portů na konkrétním zařízení.

Podle použitého protokolu rozlišujeme:

- TCP sken,
- UDP sken.

Mezi účinné obrani proti skenování portů patří firewall, IDS nebo IPS.

## Poznámka Anki 1649073419616

Karty Anki: 1649073419616
GUID: e2.Gq<Q/^m; štítky: bi-ib::21 bi-psi::p08.

Metadata původního zdroje pro kartu 1649073419616: původní příznak autora 6.

### Otázka (Front)

Popište útok prolamováním hesel.

### Odpověď (Back)

Útok často probíhá prostřednictvím terminálových služeb (SSH, RDP, Telnet). Rozlišujeme dva typy:

- **útok hrubou silou** (brute-force attack) - útočník zkouší všechny možné kombinace znaků nad danou abecedou
- **slovníkový útok** (dictionary attack) - útočník používá předem definovaný seznam často používaných hesel
Účinnou obranou je firewall, IDS či IPS.

## Poznámka Anki 1649073582384

Karty Anki: 1649073582384
GUID: jef]VRLxXU; štítky: bi-psi::p08.

Metadata původního zdroje pro kartu 1649073582384: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to denial-of-service (DoS) útok.

### Odpověď (Back)

Denial-of-service (DoS) útok je útok z jednoho zdroje na počítač, aplikaci, sdílený prostředek nebo službu, jehož účelem je učinit cíl částečně nebo úplně nedostupným pro legitimní uživatele.

## Poznámka Anki 1649073714929

Karty Anki: 1649073714929
GUID: km*TuF3|iS; štítky: bi-psi::p08.

### Otázka (Front)

Jak se nazývají aplikace zneužívající specifické bezpečnostní chyby v konkrétním systému a jak se lze proti nim bránit?

### Odpověď (Back)

Takové aplikace se označují jako červi (worms). Účinnou obranou jsou pravidelné bezpečnostní záplaty systému.

## Poznámka Anki 1649074200460

Karty Anki: 1649074200460
GUID: f>pUr4F#tE; štítky: bi-psi::p08.

### Otázka (Front)

Popište malware a uveďte jeho příklady.

### Odpověď (Back)

Malware je program, který je většinou skrytě umístěn do systému, s cílem narušit důvěrnost, integritu nebo dostupnost dat, aplikací nebo operačního systému oběti. Mezi příklady malware patří ransomware, spyware nebo adware.

## Poznámka Anki 1649074735622

Karty Anki: 1649074735622
GUID: E4xGB.JW{h; štítky: bi-psi::p08.

Metadata původního zdroje pro kartu 1649074735622: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to distributed denial-of-service (DDoS) útok.

### Odpověď (Back)

Distributed denial-of-service (DDoS) útok je typ denial-of-service (DoS) útoku, při kterém je na jednu oběť útočeno současně z několika různých zdrojů.

## Poznámka Anki 1649075141608

Karty Anki: 1649075141608
GUID: bq8;D.uJF?; štítky: bi-ib::11 bi-ib::21 bi-psi::p08.

### Otázka (Front)

Popište smurf attack.

### Odpověď (Back)

Smurf attack je typ distributed denial-of-service útoku (DDoS), který zneužívá protokol ICMP. Útok probíhá tak, že útočník broadcastuje ICMP echo request paket s podvrženou zdrojovou IP adresou v lokální síti. Zařízení, která paket obdrží, odešlou na podvrženou adresu paket ICMP echo reply, čímž způsobí zahlcení oběti, jejíž IP adresa byla podvržena v původním ICMP echo request paketu.

