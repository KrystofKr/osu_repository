# BI-ASB – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-asb/BI-ASB.apkg; APKG SHA-256 7a0706fba841a39fa40ea1e5439c99f14f59930aaa7f6d5620a33590d53350fa. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: eea4a1b952e7287bc51501f27ae2f5ec76f032fca049ee9ef600d2729e12ef40.
Původní balíčky: BI-ASB
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1701694302954

Karty Anki: 1701694302954
GUID: FIw9Rr$%;E; štítky: bi-asb::p09.

Metadata původního zdroje pro kartu 1701694302954: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište a porovnejte protokoly Secure Shell Protocol (SSH) a Telnet.

### Odpověď (Back)

Protokoly Secure Shell Protocol (SSH) a Telnet (teletype network) jsou protokoly aplikační vrstvy, které se používají pro vzdálený přístup. Postaveny jsou na architektuře klient/server a pro přenos dat používají protokol TCP. Odlišují je následující rozdíly:

| 
      **Secure Shell Protocol (SSH)** | **Telnet** | 

| 
      používá port 22 | 
      používá port 23 | 

| 
      šifruje přenášená data
 | 
      nešifruje přenášená data |

## Poznámka Anki 1701698293340

Karty Anki: 1701698293340
GUID: t7I*C@&W~N; štítky: bi-asb::p09 bi-ib::12.

### Otázka (Front)

Popište architekturu protokolu Secure Shell Protocol (SSH).

### Odpověď (Back)

Architektura Secure Shell Protocolu (SSH) se skládá ze tří vrstev:

- **transport layer **- provádí výměnu klíčů, autentizaci serveru, šifrování;

- **authentication layer **- provádí autentizaci klienta (password, public key, keyboard interactive);

- **connection layer** - umožňuje používání kanálů (channels) a na nich běžících služeb (services), které dovolují několik paralelních relací se serverem.

## Poznámka Anki 1701700822739

Karty Anki: 1701700822739
GUID: A9$L7]{L{>; štítky: bi-asb::p09 bi-ib::12.

### Otázka (Front)

Popište Secure Shell Protocol (SSH) handshake s použitím Diffie-Hellmanova algoritmu nad eliptickou křivkou.

### Odpověď (Back)

Handshake Secure Shell Protocolu (SSH) s použitím Diffie-Hellmanova algoritmu nad eliptickou křivkou (ECDH) probíhá následovně:

- Klient a server si sdělí verzi protokolu a podporované kryptografické metody.
- Klient posílá serveru svůj věřejný klíč ECDH algoritmu.
- Server si spočte společný klíč a exchange hash, kterou podepíše svým soukromým klíčem, čímž vzniká signed hash. Klientovi pak zpátky posílá svůj veřejný ECDH klíč, veřejný klíč ke klíči, který byl použit pro podepsání exchange hash, a signed hash.
- Klient si spočte společný klíč a ověří podpis na exchange hash.
- Ze společného klíče si následně klient i server vygenerují MAC klíč serveru a klienta, šifrovací klíč serveru a klienta a případné inicializační vektory.

## Poznámka Anki 1701702569467

Karty Anki: 1701702569467
GUID: fE#N7B23.n; štítky: bi-asb::p09.

Metadata původního zdroje pro kartu 1701702569467: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište virutal private network (VPN) a jeho využití.

### Odpověď (Back)

Virtual private network (VPN) je technologie využívající tunelování (tunelling) k sestavení spojení mezi zařízením a vzdálenou sítí. Toto spojení bývá zpravidla šifrované, ale existují i VPN protokoly, které šifrování nepodporují. Mezi využití VPN patří:

- zpřístupnění lokální sítě uživateli, který je od ní geograficky nebo síťově oddělen;
- anonymizace;
- zpřístupnění geograficky omezeného obsahu.

## Poznámka Anki 1701704849448

Karty Anki: 1701704849448
GUID: v^E*zqv4f3; štítky: bi-asb::p09.

Metadata původního zdroje pro kartu 1701704849448: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Layer 2 Tunneling Protocol (L2TP).

### Odpověď (Back)

Layer 2 Tunneling Protocol (L2TP) je virtual private network (VPN) protokol linkové vrstvy, který se používá pro tunelování rámců. Data přenášená pomocí L2TP jsou nešifrovaná, proto se často kombinuje s protokolem Internet Protocol Security (IPSec).

## Poznámka Anki 1701706808943

Karty Anki: 1701706808943
GUID: J5>?[3-=[h; štítky: bi-asb::p09.

Metadata původního zdroje pro kartu 1701706808943: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište protokol Internet Protocol Security (IPSec).

### Odpověď (Back)

Internet Protocol Security (IPSec) protokol je virtual private network (VPN) protokol síťové vrstvy, který se používá pro šifrování spojení mezi zařízeními komunikujícími pomocí Internet Protocolu (IP). IPSec používá následující podprotokoly:

- **Internet Key Exchange **(IKE) - sjednání společného klíče,

- **Authentication Header **(AH) - autentizace původu a kontrola integrity dat,

- **Encapsulating Security Payload **(ESP) - šifrování a autentizace původu dat.

Komunikace pomocí IPSec může probíhat buď v transportním (transport) nebo tunelovacím (tunnel) módu.

## Poznámka Anki 1701707353650

Karty Anki: 1701707353650
GUID: JBU,v)1v=~; štítky: bi-asb::p09.

Metadata původního zdroje pro kartu 1701707353650: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Porovnejte módy protokolu Internet Protocol Secured (IPSec).

### Odpověď (Back)

Komunikace pomocí Internet Protocol Secured (IPSec) může probíhat buď v transporním nebo tunelovacím módu. V **transportním **módu se šifrují pouze data IP paketu a hlavička zůstává původní. Tento mód je méně náročný na přenosovou rychlost. Naproti tomu **tunelovací mód** funguje tak, že celý původní paket zapouzdří a zašifruje. Vzniká tak nová hlavička paketu, která neobsahuje informace o komunikujících koncových zařízeních. Tento mód je náročnější na přenosovou rychlost.

## Poznámka Anki 1701707847337

Karty Anki: 1701707847337
GUID: giIe+j!zW4; štítky: bi-asb::p09.

### Otázka (Front)

Jakým způsobem nakládá Authentication Header (AH) protokol s proměnlivými položkami paketu.

### Odpověď (Back)

Vzhledem k tomu, že některé položky (např. TTL či ToS) IP paketu se mohou při jeho směrování měnit, nejsou při kontrole integrity pomocí Authentication Header (AH) protokolu používány.

