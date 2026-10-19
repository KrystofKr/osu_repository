# BI-ASB – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-asb/BI-ASB.apkg; APKG SHA-256 7a0706fba841a39fa40ea1e5439c99f14f59930aaa7f6d5620a33590d53350fa. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: eea4a1b952e7287bc51501f27ae2f5ec76f032fca049ee9ef600d2729e12ef40.
Původní balíčky: BI-ASB
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1699870213505

Karty Anki: 1699870213505
GUID: tARG!SO4#n; štítky: bi-asb::p06 bi-ib::13.

### Otázka (Front)

Popište technologii Wi-Fi.

### Odpověď (Back)

Wi-Fi je rodina protokolů vycházející ze 802.11 standardu, které se používají pro bezdrátové síťové přípojení. Používá CSMA/CA (carrier-sense multiple access with collision avoidance) a mechanismus RTS/CTS (request to send and clear to send). Komunikace Wi-Fi sítí probíhá buď v infrastrukturním nebo ad-hoc módu.

## Poznámka Anki 1699870730191

Karty Anki: 1699870730192
GUID: diW#!7z,H*; štítky: bi-asb::p06 bi-ib::13.

### Otázka (Front)

Popište strukturu Wi-Fi rámce.

### Odpověď (Back)

Struktura Wi-Fi rámce je následující:

 [Obrázek: paste-bd40143b68be310a4cdb1b37581f0622626303d1.jpg; soubor je v media/ v doprovodném ZIP] 

Důležité prvky:

- **frame control **- nese řídící informace, např. rozlišuje management, control a data rámce;

- 4 pole pro MAC adresy - jejich význam vyplývá z frame control.

## Poznámka Anki 1699871469696

Karty Anki: 1699871469696
GUID: t5&gA:x[26; štítky: bi-asb::p06.

Metadata původního zdroje pro kartu 1699871469696: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Wired Equivalent Privacy (WEP).

### Odpověď (Back)

Wired Equivalent Policy (WEP) je prolomený bezpečnostní algoritmus používaný ve Wi-Fi sítích. Používá šifru RC4 a CRC32. Autentizační proces probíhá následovně:

- Stanice pošle access pointu žádost o autentizaci.
- Access point odpoví zprávou, která obsahuje nešifrovanou challenge.

- Stanice zašifruje challenge s použítím předsdíleného klíče a pošle ji zpět.
- Access point dešifruje odpověď stanice a pokud odpovídá původní challenge zprávě, je stanice připojena k síti.

## Poznámka Anki 1699871479934

Karty Anki: 1699871479934
GUID: FQ%m9jyKc3; štítky: bi-asb::p06.

Metadata původního zdroje pro kartu 1699871479934: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Jakým způsobem lze prolomit Wired Equivalent Privacy (WEP)?

### Odpověď (Back)

Protože WEP používá proudovou šifru RC4, nesmí být stejný keystream použit více než jedenkrát. Proto se používá 24b inicializační vektor, který je přednášek v otevřeném textu. Kvůli malé délce inicializačního vektoru jsou ale inicializační vektory často opakovaně použity. Proto je možné během několika málo minut (na síti s vysokou aktivitou) zachytit kolize inicializačních vektorů a pomocí statistické analýzy následně zrekonstruovat klíč.

## Poznámka Anki 1699873700121

Karty Anki: 1699873700125
GUID: o&Yb@I#&QW; štítky: bi-asb::p06 bi-ib::12 bi-ib::13 bi-ib::21.

### Otázka (Front)

Popište 802.1X.

### Odpověď (Back)

IEEE 802.1X je standard pro port-based access control, který používá Extensible Authentication Protocol (EAP) pro řízení přístupu k síti. Používá následující infrastrukturu:

- **supplicant** - zařízení žádající o přístup k síti,

- **authenticator** - zařízení spravující spojení mezi supplicantem a sítí,

- **authentication server** - komunikuje s authenticatorem a rozhoduje o připojení supplicantů k síti.

## Poznámka Anki 1699873757623

Karty Anki: 1699873757623
GUID: EkaV5QLO_~; štítky: bi-asb::p06.

Metadata původního zdroje pro kartu 1699873757623: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Wi-Fi Protected Access (WPA).

### Odpověď (Back)

Wi-Fi Protected Access (WPA) je bezpečnostní algoritmus používaný ve Wi-Fi sítích. Používá šifru AES v CTR a CBC-MAC módech. Před tím, než začne autentizace, musí mít stanice i access point k dispozici **pairwise master key **(PMK), což je v kontextu WPA-Personal předsdílené heslo. Poté autentizační proces probíhá následovně:

- Access point posílá hodnotu **ANONCE** (náhodná hodnota generovaná access pointem).

- Stanice vygeneruje svou náhodnou hodnotu **SNONCE** a odvodí si **pairwise transit key** (PTK).
- Stanice pošle access pointu svou hodnotu **SNONCE **společně s **MIC **(Message Integrity Code) (od této zprávy obsahuje každá zápráva MIC).
- Access point si odvodí svůj PTK.

- Access point pošle stanici zašifrovaný **group transit key **(GTK) a nařídí stanici nainstalovat smluvené klíče.

- Stanice nainstaluje klíče a pošle access pointu potvrzení.

## Poznámka Anki 1699878335655

Karty Anki: 1699878335655
GUID: DDJ#<}N&6Q; štítky: bi-asb::p06 bi-ib::13.

### Otázka (Front)

Popište verze Wi-Fi Protected Access (WPA). Jak se liší?

### Odpověď (Back)

Existují následující tři verze WPA:

- **WPA1** - používá Temporal Key Integrity Protocol (TKIP),

- **WPA2** - používá šifru AES v CTR a CBC-MAC módu,

- **WPA3** - používá Simultaneous Authentication of Equals (SAE).

## Poznámka Anki 1699878593321

Karty Anki: 1699878593321
GUID: zzB*<P.KI5; štítky: bi-asb::p06 bi-ib::13.

### Otázka (Front)

Popište Temporal Key Integrity Protocol (TKIP).

### Odpověď (Back)

Temporal Key Integrity Protocol (TKIP) je protokol využívaný ve WPA1. Měl za úkol nahradit prolomený Wired Equivalent Privacy (WEP) protokol, ale zároveň měl být realizovatelný na stejném hardware jako WEP. Proto je konstruován jako nadstavba WEP, tedy je stále založen na šifře RC4. Vyřešil některé z hlavních problémů WEP jako:

- chyby v generování inicializačního vektoru,
- příliš krátké klíče,
- použití CRC32 pro kontrolu integrity.

## Poznámka Anki 1699881728108

Karty Anki: 1699881728108
GUID: N|Hl@l,sR}; štítky: bi-asb::p06 bi-ib::13.

### Otázka (Front)

Popište Wi-Fi Protected Access 3 (WPA3) handshake.

### Odpověď (Back)

WPA3 handshake probíhá podobně jako WPA2 handshake, ale je předcházen výměnou dvou zpráv protokolu Simultaneous Authentication of Equals (SAE), který vnitřně používá Dragonfly algoritmus, což je typ Simple Password Exponential Key Exchange (SPEKE) algoritmu. Průběh je tedy následující:

- Stanice a access point si vymění zprávy authentication commit, které obsahují parametry scalar a element algoritmu Dragonfly.
- Stanice a access point si vymění zprávy authentication confirm, které slouží k ověření, že oba došli ke stejnému shared secret v algoritmu Dragonfly.
- Dojde k vygenerování společného klíče podle algoritmu Dragonfly a ten se použije jako pairwise master key.

Zbytek probíhá totožně s WPA2 handshakem:

- Access point posílá hodnotu **ANONCE** (náhodná hodnota generovaná access pointem).

- Stanice vygeneruje svou náhodnou hodnotu **SNONCE** a odvodí si **pairwise transit key** (PTK).
- Stanice pošle access pointu svou hodnotu **SNONCE **společně s **MIC **(Message Integrity Code) (od této zprávy obsahuje každá zápráva MIC).
- Access point si odvodí svůj PTK.

- Access point pošle stanici zašifrovaný **group transit key **(GTK) a nařídí stanici nainstalovat smluvené klíče.

- Stanice nainstaluje klíče a pošle access pointu potvrzení.

## Poznámka Anki 1699883501613

Karty Anki: 1699883501614
GUID: deki-O#6hl; štítky: bi-asb::p06 bi-ib::12 bi-ib::13.

### Otázka (Front)

Popište Simple Password Exponential Key Exchange (SPEKE) nad eliptickou křivkou.

### Odpověď (Back)

Simple Password Exponential Key Echange (SPEKE) algoritmus nad eliptickou křivkou je algoritmus výměny klíče založený na Diffie-Hellmanově algoritmu nad eliptickou křivkou. Mějme tedy dva subjekty \(A\) a \(B\) a předpokládejme, že mají sjednanou eliptickou křivku \(E\), hashovací funkci \(h\), sdílené heslo \(p\) a každý svůj tajný klíč \(k\). Potom alogritmus SPEKE nad eliptikou křivkou probíhá následovně:

- Oba subjekty spočítají počáteční bod \(P\) pomocí hashovací funkce \(h\) a sdíleného hesla \(p\).

\[P = h(p)\]Dále algoritmus pokračuje stejně jako Diffie-Hellmanův algoritmus nad eliptickou křivkou:

- Subjekt A spočte a pošle druhému subjektu bod \(Q_\text A \in E\), pro který platí

\[Q_\text A = k_\text A \cdot P.\]

- Subjekt B spočte společný bod \(X \in E\) pomocí vztahu

\[X = k_\text B \cdot Q_\text A = k_\text A \cdot k_\text B \cdot P.\]

- Subjekt B spočte a pošle prvnímu subjektu bod \(Q_\text B \in E\), pro který platí

\[Q_\text B = k_\text B \cdot P.\]

- Subjekt A spočte společný bod \(X\) pomocí vztahu

\[X = k_\text A \cdot Q_\text B = k_\text A \cdot k_\text B \cdot P.\]Podle smluveného algoritmu se ze společného bodu \(X\) spočte společný klíč  \(K\). SPEKE lze však použít i k autentizaci, a to tak že si \(A\) a \(B\) po skončení algoritmu sdělí výsledné \(K\). V případě, že jsou stejná, museli na začátku oba vyjít ze stejného sdíleného hesla \(p\).

## Poznámka Anki 1699883561853

Karty Anki: 1699883561853
GUID: ElbgK1^A,*; štítky: bi-asb::p06.

Metadata původního zdroje pro kartu 1699883561853: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište slabiny Wi-Fi Protected Access (WPA).

### Odpověď (Back)

Wi-Fi Protected Access má následující slabiny:

- slabě předsdílené klíče jsou náchylné k slovníkovým útokům,
- existují rainbow tables pro často používaná SSID,
- Wi-Fi Protected Setup (WPS) používá slabé PINy a starší verze obsahovaly implementační chyby,

- Dragonblood útok - kombinace downgrade útoku a útoku postranním kanálem,

- Key Reinstallation Attack (KRACK).

## Poznámka Anki 1717793518463

Karty Anki: 1717793518463
GUID: j!jjuR%UoS; štítky: bi-asb::p06 bi-ib::13.

### Otázka (Front)

Popište brute-force útok na Wi-Fi Protected Access 2 (WPA2).

### Odpověď (Back)

Brute-force útok na Wi-Fi Protected Access 2 (WPA2) je možný z toho důvodu, že data vyměňovaná ve WPA2 handshaku jsou závislá na pairwise master key (PMK). Předpokladem je, že útočník dříve zachytil WPA2 handshake se všemi parametry, které potřebuje pro odvození pairwise transit key (PTK) (kromě PMK). Následně může spustit offline brute-force útok, ve kterém iteruje následující postup:

- odhadne pre-shared key,
- spočte pairwise master key,
- spočte pairwise transit key,
- spočte message integrity code (MIC) a porovná jej s MIC použitým v zachyceném handshaku.
Pokud nastane shoda, byl nalezen správný pre-shared key.

## Poznámka Anki 1717793999982

Karty Anki: 1717793999982
GUID: f-^,![((3D; štítky: bi-asb::p06 bi-ib::13.

### Otázka (Front)

Popište Wi-Fi Protected Access 3 (WPA3).

### Odpověď (Back)

Wi-Fi Protected Access 3 (WPA3) je bezpečnostní algoritmus používaný ve Wi-Fi sítích navržený jako nástupce algoritmu WPA2. Oproti WPA2 poskytuje perfect forward secrecy (PFS) a používá Simultaneous Authentication of Equals (SAE). Díky SAE je odstraněna vazba mezi pairwise master key (PMK) a pre-shared key, čímž je zamezeno offline brute-force útokům na pre-shared key, které jsou u WPA2 možné.

