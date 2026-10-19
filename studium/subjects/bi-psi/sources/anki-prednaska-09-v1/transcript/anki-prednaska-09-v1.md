# BI-PSI – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1649675713351

Karty Anki: 1649675713351
GUID: s|-+Y*)|wV; štítky: bi-ib::11 bi-ib::12 bi-ib::21 bi-psi::p09 bi-spol::25.

### Otázka (Front)

Popište virutal private network (VPN) a jeho využití.

### Odpověď (Back)

Virtual private network (VPN) je technologie využívající tunelování (tunelling) k sestavení spojení mezi zařízením a vzdálenou lokální sítí. Toto spojení bývá zpravidla šifrované, ale existují i VPN protokoly, které šifrování nepodporují. Mezi využití VPN patří:

- zpřístupnění lokální sítě uživateli, který je od ní geograficky nebo síťově oddělen;
- anonymizace;
- zpřístupnění geograficky omezeného obsahu.

## Poznámka Anki 1649675922257

Karty Anki: 1649675922257
GUID: v4$470^Qwm; štítky: bi-ib::12 bi-psi::p09 bi-spol::25.

Metadata původního zdroje pro kartu 1649675922257: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište dělení virtual private network (VPN).

### Odpověď (Back)

Virtual private network (VPN) můžeme rozdělit do následujících kategorií dle způsobu jejich využití:

- **remote access **- dočasné připojení konkrétního zařízení do vzdálené lokální sítě,

- **site-to-site** - permanentní propojení dvou různých sítí.

Site-to-site VPN pak ještě dělíme na dva typy:

- **intranet-based **- propojené sítě patří pod stejnou organizaci,

- **extranet-based **- propojené sítě patří různým organizacím.

## Poznámka Anki 1649676089465

Karty Anki: 1649676089466
GUID: kz!UafFivx; štítky: bi-ib::12 bi-psi::p09 bi-spol::25.

### Otázka (Front)

Popište virtual private network (VPN) infrastrukturu a její prvky.

### Odpověď (Back)

Virtual private network (VPN) infrastruktura se skládá ze tří částí:

- **VPN server** - zprostředkovává přístup do lokální sítě;
- **VPN device** - zařízení propojující lokální síť ostatními sítěmi, může být realizováno hardwarově nebo softwarově;

- **VPN tunnel** - virtuální spojení mezi VPN zařízeními (devices).

## Poznámka Anki 1649676192734

Karty Anki: 1649676192734
GUID: bi6<)NDQ<<; štítky: bi-ib::11 bi-ib::12 bi-ib::21 bi-psi::p09 bi-spol::25.

### Otázka (Front)

Popište tunelování (tunneling) a enkapsulaci (encapsulation) a jejich využití.

### Odpověď (Back)

Tunelování (tunelling) je metoda přenosu dat, při které jsou data nejprve zapouzdřena do paketů tunelovacího protokolu a až poté přenášena po síti. Tomuto principu zapouzdření se říká enkapsulace (encapsulation). Mezi jejich využití patří:

- technologie virtual private network (VPN),
- zabezpečení protokolů, které samy o sobě zabezpečení nepodporují.

## Poznámka Anki 1649676299020

Karty Anki: 1649676299020
GUID: BarGcHPQ:b; štítky: bi-ib::11 bi-ib::12 bi-ib::21 bi-psi::p09 bi-spol::25.

### Otázka (Front)

Popište princip anonymizace pomocí virtual private network (VPN).

### Odpověď (Back)

Při běžné komunikaci vidí externí pozorovatel v síťovém provozu uživatele IP adresu zdrojového routeru a cílového serveru. V případě, že uživatel použije virtual private network (VPN) spojení, přeposílá router pakety na VPN server, čímž dochází k utajení cílového serveru před pozorovatelem.

## Poznámka Anki 1649676390230

Karty Anki: 1649676390230
GUID: x02tkvR-`X; štítky: bi-psi::p09.

### Otázka (Front)

Popište Point-to-Point protokol (PPP).

### Odpověď (Back)

- pracuje na linkové vrstvě
- propojuje vždy právě 2 strany
- je jednoduchý, používá se pro vzdálený přístup
- podporuje kompresi, šifrování i autentizaci

## Poznámka Anki 1649676871063

Karty Anki: 1649676871063
GUID: s<3/.p=u[t; štítky: bi-ib::11 bi-ib::12 bi-psi::p09.

### Otázka (Front)

Popište protokol Internet Protocol Security (IPSec).

### Odpověď (Back)

Internet Protocol Security (IPSec) protokol je virtual private network (VPN) protokol síťové vrstvy, který se používá pro šifrování spojení mezi zařízeními komunikujícími pomocí Internet Protocolu (IP). IPSec používá následující podprotokoly:

- **Internet Key Exchange **(IKE) - sjednání společného klíče,

- **Authentication Header **(AH) - autentizace původu a kontrola integrity dat,

- **Encapsulating Security Payload **(ESP) - šifrování a autentizace původu dat.

Komunikace pomocí IPSec může probíhat buď v transportním (transport) nebo tunelovacím (tunnel) módu.

## Poznámka Anki 1649677027324

Karty Anki: 1649677027324
GUID: oS^{sLPE;w; štítky: bi-ib::11 bi-psi::p09.

### Otázka (Front)

Porovnejte módy protokolu Internet Protocol Secured (IPSec).

### Odpověď (Back)

Komunikace pomocí Internet Protocol Secured (IPSec) může probíhat buď v transporním nebo tunelovacím módu. V **transportním **módu se šifrují pouze data IP paketu a hlavička zůstává původní. Tento mód je méně náročný na přenosovou rychlost. Naproti tomu **tunelovací mód** funguje tak, že celý původní paket zapouzdří a zašifruje. Vzniká tak nová hlavička paketu, která neobsahuje informace o komunikujících koncových zařízeních. Tento mód je náročnější na přenosovou rychlost.

## Poznámka Anki 1649677128842

Karty Anki: 1649677128842
GUID: KP:_N[Cv-h; štítky: bi-psi::p09.

### Otázka (Front)

Popište protokol IP over IP.

### Odpověď (Back)

- pracuje na síťově vrstvě
- původní IP pakety jsou přenášeny v položce DATA nových IP paketů
- přeposílají se pouze celé pakety, fragmentace není povolena
- neobsahuje šifrovací ani bezpečnostní mechanismy

## Poznámka Anki 1649677206073

Karty Anki: 1649677206073
GUID: m-R_ois4?N; štítky: bi-ib::11 bi-psi::p09 bi-spol::25.

### Otázka (Front)

Popište Generic Routing Encapsulation (GRE).

### Odpověď (Back)

- pracuje na transportní vrstvě
- je využíván dalšími VPN protokoly
- jeho hlavička neobsahuje porty (narozdíl od TCP/UDP), je tedy špatně průchozí pro NAT

## Poznámka Anki 1649677382572

Karty Anki: 1649677382572
GUID: y;zVAlNB|P; štítky: bi-psi::p09.

Metadata původního zdroje pro kartu 1649677382572: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Point-to-Point Tunneling Protokol (PPTP).

### Odpověď (Back)

- využívá GRE a PPP
- je postaven na modelu client-server
- vytvářené spojení je obousměrné

## Poznámka Anki 1649677445704

Karty Anki: 1649677445704
GUID: cr#(}qGdEh; štítky: bi-ib::11 bi-ib::12 bi-psi::p09.

### Otázka (Front)

Popište Layer 2 Tunneling Protocol (L2TP).

### Odpověď (Back)

Layer 2 Tunneling Protocol (L2TP) je virtual private network (VPN) protokol linkové vrstvy, který se používá pro tunelování rámců. Data přenášená pomocí L2TP jsou nešifrovaná, proto se často kombinuje s protokolem Internet Protocol Security (IPSec).

## Poznámka Anki 1649677615948

Karty Anki: 1649677615948
GUID: DRs[*!E,Qi; štítky: bi-psi::p09.

### Otázka (Front)

Popište Secure Socket Tunelling Protocol (SSTP).

### Odpověď (Back)

- pracuje na aplikační vrstvě
- je přenášen v protokolu HTTPS
- pro zapouzdření dat využívá PPP
- vytváření spojení probíhá ve třech fázích:

- sestavení TCP spojení
- spuštění šifrování přes SSL
- přenos přes HTTPS

## Poznámka Anki 1649677726938

Karty Anki: 1649677726939
GUID: illnday~wa; štítky: bi-psi::p09.

### Otázka (Front)

Popište protokol Open VPN.

### Odpověď (Back)

- pracuje na aplikační vrstvě
- v OS je implementován jako virtuální síťové rozhraní

- TAP pro linkovou vrstvu
- TUN pro síťovou vrstvu

- OVPN pakety jsou přenášeny jako data protokolu TCP nebo UDP

## Poznámka Anki 1649678105804

Karty Anki: 1649678105804
GUID: tpbwNf47vz; štítky: bi-psi::p09.

### Otázka (Front)

Co je to otisk prohlížeče?

### Odpověď (Back)

Je to množina specifických atributů zasílaných v rámci HTTP, které lze využít pro identifikaci uživatele.

## Poznámka Anki 1649678241916

Karty Anki: 1649678241917
GUID: Ot<?{RJz5B; štítky: bi-psi::p09.

### Otázka (Front)

Co je to Tor, Onion Routing a Onion Service?

### Odpověď (Back)

**Tor **je síť, která si klade za cíl znemožnit sledování uživatelů.
**Onion Routing** je anonymní směrování, které je proměnné a nelze tak odhadnout ani vzdálenost zdroje.
**Onion Service** je anonymní obdoba DNS, je však založna na odlišném principu.

