# BI-PSI – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 22 poznámek, 22 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1646655767666

Karty Anki: 1646655767667
GUID: C{P?Inx<,=; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Které druhy komunikačních operací jsou a nejsou podporovány u IPv6?

### Odpověď (Back)

Podporovány jsou unicast, multicast, anycast, ale broadcast nikoliv.

## Poznámka Anki 1646656097511

Karty Anki: 1646656097511
GUID: qxZ/wf0)0c; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Popište složení IPv6 paketu a jeho složky.

### Odpověď (Back)

**Základní hlavička **obsahující informace nutné pro doručení paketu (zdrojová a cílová adresa, TTL, velikost dat) je přítomna vždy.
**Rozšiřující hlavička** obsahující informace pro doručení konkrétního paketu nemusí být vždy přítomna. Vícero rozšiřujících hlaviček se spojuje za sebe.
**Data** obsahující hlavičky a data protoklů vyšších vrstev.

## Poznámka Anki 1646656182031

Karty Anki: 1646656182031
GUID: g[N~36S+J`; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Jaké jsou rozdíly u fragmentace paketů IPv6 oproti IPv4?

### Odpověď (Back)

Velikost paketu určuje narozdíl od IPv4 zdrojová stanice a po celou dobu doručování se velikost nemění. U IPv4 mohla být velikost měněna na každém směrovači.

## Poznámka Anki 1646656347686

Karty Anki: 1646656347686
GUID: hTRK;v}hH;; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Popište řetězení hlaviček u IPv6 paketů.

### Odpověď (Back)

Rozšiřující hlavičky s řetězí v definovaném pořadí a každá má specifickou funkci (směrování, fragmentace, ...) rozlišenou kódem. K samotnému řetězení se využívá speciální položka v každé hlavičce (další hlavička). 
Oproti IPv4 se tedy přenáší jen nutné hlavičky. Každý paket může mít individuální počet hlaviček.

## Poznámka Anki 1646656706022

Karty Anki: 1646656706022
GUID: emv(pUNW@-; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Popište strukturu IPv6 adres a princip jejich zkracování.

### Odpověď (Back)

IPv6 adresa obsahuje \(8 \times 16\) bitů v hexadecimálním zápisu oddělených dvojtečkami:
\[\texttt{1234:1234:1234:0000:1234:0000:0000:1234}.\]V zápisu lze sloučit nuly na jednu:
\[\texttt{1234:1234:1234:0:1234:0:0:1234}.\]Nebo je lze vynechat úplně. Takový zápis potom znamená vložení co možná největšího počtu nul:
\[\texttt{1234:1234:1234:0:1234::1234}.\]

## Poznámka Anki 1646657009874

Karty Anki: 1646657009874
GUID: AxX;(Zc)`l; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Jaké jsou druhy adres IPv6?

### Odpověď (Back)

- **lokální linkové** (LL)
- **skupinové** (multicastové)
- **unikátní lokální **(UL)
- **loopback **(smyčka)
- **přechodové** - slouží k doručení dat do IPv4 sítí
- **individuální globální** - obdoba veřejných IPv4 adres

## Poznámka Anki 1646657271856

Karty Anki: 1646657271856
GUID: H2Mx-o.B`H; štítky: bi-psi::p04.

### Otázka (Front)

Popište individuální globální adresu (IGA).

### Odpověď (Back)

Po bitech se skládá z: 001 + globální směrovací prefix + identifikátor podsítě + identifikátor rozhraní
**Globální směrovací prefix** označuje konkrétní síť, která je dosažitelná po internetu.
**Identifikátor podsítě** se využívá pro směrování do konkrétní podsítě v rámci sítě určené GSP.
**Identifikátor rozhraní** určuje konkrétní síťové rozhraní, odvozuje se z MAC adresy a označuje se také jako **EUI-64 **(Extended Unique Identifier).

## Poznámka Anki 1646657347783

Karty Anki: 1646657347783
GUID: v6ejYpk9+9; štítky: bi-psi::p04.

### Otázka (Front)

Jak se odvodí EUI-64 z MAC adresy rozhraní.

### Odpověď (Back)

Mezi 3. a 4. bajt MAC adresy se vloží bajty FF a FE a 7. bit zleva se invertuje.
 [Obrázek: paste-e9b331eaa9f21e93512a6bd7b7e0b7f0a0e58c8e.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1646658035255

Karty Anki: 1646658035256
GUID: i2S+$TGyUD; štítky: bi-psi::p04.

### Otázka (Front)

Popište lokální linkové (LL) a unikátní lokální (UL) adresy.

### Odpověď (Back)

Oba druhy jsou zakončeny EUI-64 dle rozhraní stejně jako IGA.
**LL** adresa se používá pro adresaci konkrétního síťového rozhraní v lokální síti, nastavuje se automaticky dle MAC adresy daného síťového rozhraní.
**UL** se používá pro směrování ve stejné síti a musí se ručně konfigurovat.

## Poznámka Anki 1646658143262

Karty Anki: 1646658143262
GUID: fr!wdx5)P:; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Jak probíhá řízení provozu v IPv6?

### Odpověď (Back)

IPv6 dokáže zabezpečit svou činnost pouze s využitím protokolu Internet Control Protocol for IPv6 (ICMPv6), který je přenášen uvnitř IPv6 jako data. Zahrnuje řadu funkcí označovanou jako Neighbor Discovery (ND).

## Poznámka Anki 1646658810572

Karty Anki: 1646658810573
GUID: p*7*Pe:.j$; štítky: bi-psi::p04.

### Otázka (Front)

Jaké funkce nabízí objevování sousedů (Neighbor Discovery)?

### Odpověď (Back)

- **automatická konfigurace koncových stanic** (obdoba DHCP u IPv4)
- **zjišťování linkových adres v lokální síti** (náhrada ARP u IPv4)
- aktualizace neplatných složek
- detekce duplicitních adres
- hledání směrovačů
- ověřování sousedů

## Poznámka Anki 1646659123881

Karty Anki: 1646659123881
GUID: JbO7X^*a13; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Co to je automatická konfigurace koncové stanice u IPv6?

### Odpověď (Back)

Metoda, jejímž účelem je získání globální adresy IPv6 a dalších parametrů, které umožní stanici komunikoat uvnitř sítě i internetu.
Druhy:

- **bezestavová** - existují směrovače, které mají kompletní informace o provzu a dokáží je předat
- **stavová** - v síti existuje server přidělující adresy přes protokol DHCPv6.

## Poznámka Anki 1646659756552

Karty Anki: 1646659756553
GUID: pxbDzk=d>%; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Jak funguje bezestavová automatická konfigurace?

### Odpověď (Back)

Směrovač periodicky posílá do sítě zprávu ohlášení směrovače (Router Advertisement - RA) obsahující 64bitový prefix, který stanice zkombinuje s EUI-64 odvozeného od MAC adresy svého rozhraní a získá tak použitelou individuální globální IPv6 adresu. Směrovač se zároveň automaticky stává bránou.

Případně stanice požádá o konfiguraci pomocí zprávy vývzva směrovači (Router Solicitation - RS).

RA i RS jsou doručovány pomocí ICMPv6 a zasílány pomocí linkové vrstvy.

## Poznámka Anki 1646660009049

Karty Anki: 1646660009049
GUID: GHnq}q>cF}; štítky: bi-psi::p04.

### Otázka (Front)

Popište mapování skupinové IPv6 adresy na MAC adresu.

### Odpověď (Back)

Skupinové IPv6 adresy se na MAC adresy mapují následujícím způsobem:

- MAC adresa se odvodí z posledních 32 bitů IPv6 adresy,
- před ni se vloží 16bitový hexadecimální prefix \(\texttt{33:33}\).

Toto mapování předpokládá podporu na úrovni zařízení linkové vrstvy.

 [Obrázek: paste-c9487a1c3dc7ed4e534c71259ac5a14f23193718.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1646678222878

Karty Anki: 1646678222878
GUID: sl4L,$}~$2; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Popište algoritmus zjištění linkové adresy na základě známé IPv6 adresy.

### Odpověď (Back)

1. sestavení adresy vyzývané cílové stanice (Solicitation Address - SA)
2. poslání zprávy výzva sousedovi (Neighbor Solicitation - NS) skupinově na SA pomocí linkové vrstvy
3. přijetí zprávy NS cílovou stanicí a zaslání odpovědi zpráva ohlášení souseda (Neighbor Advertisement - NA)
4. načtení MAC adresy souseda zdrojovu stanicí a uložení této adresy do tabulky sousedů

## Poznámka Anki 1646684794375

Karty Anki: 1646684794375
GUID: G_k66x#:]D; štítky: bi-psi::p04.

### Otázka (Front)

Jaké jsou stavy adres v tabulce sousedů?

### Odpověď (Back)

- nekompletní
- dosažitelná
- prošlá
- odložená
- testovaná
 [Obrázek: paste-6f0a72f3ea8682f34df80d5c91d5012d84883b7a.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1646685346368

Karty Anki: 1646685346368
GUID: paX-+_PpYO; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Co je to inverzní objevování sousedů?

### Odpověď (Back)

Metoda mapující známou linkovou adresu rozhraní na odpovídající adresu IPv6.
Probíhá pomocí zpráv inverzní výzva sousedovi a inverzní ohlášení souseda.

## Poznámka Anki 1646685458311

Karty Anki: 1646685458311
GUID: r)G}$0oZ)[; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Jak probíhá směrování v IPv6 sítích?

### Odpověď (Back)

- stanice jsou schopné zjistit dostupné směrovače pomocí ND
- stanice si udržují směrovací tabulky
- pro neznámé cíle je implicitní směrovač (obdoba brány v IPv4), o kterém se dozví z ohlášení směrovače (Router Advertisement) nebo od DHCPv6 serveru

## Poznámka Anki 1646685603564

Karty Anki: 1646685603564
GUID: cJ@DxFW-rj; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Co je to stavová konfigurace koncové stanice a DHCPv6?

### Odpověď (Back)

Algoritmus přidělení adresy je shodný s klasickým DHCP s tím rozdílem, že DHCPv6 přiděluje pouze adresu a ostatní zařizuje metoda ND.

## Poznámka Anki 1646685756109

Karty Anki: 1646685756109
GUID: DPhp|1/oY[; štítky: bi-psi::p04 bi-spol::24.

### Otázka (Front)

Jak funguje přechodový mechanizmus IPv6 pro přístup do IPv4?

### Odpověď (Back)

Pokud existuje směrovač, na kterém běží současně IPv4 a IPv6 protokol, využije se řešení NAT64.
Přechodová IPv6 adresa (IPP) pro dosažení IPv4 adresy se sestaví jako prefix **64:FF9B::/96 **+ 32 bitů IPv4 adresy.

## Poznámka Anki 1646685944882

Karty Anki: 1646685944882
GUID: u[]3/pl|5H; štítky: bi-psi::p04.

### Otázka (Front)

Co je to TEREDO?

### Odpověď (Back)

TEREDO umožňuje stanici komunikovat přes IPv6, anižby se nacházela v síti podporující tento protokol.
Mezi stanicí a TEREDO relayem se pomocí IPv4 komunikace vytvoří tunel, kterým jsou posílány IPv6 pakety. TEREDO relay je pomocí své nativní IPv6 sítě směruje do internetu a tunelem zpět přeposílá zprávy stanici.

## Poznámka Anki 1646686292754

Karty Anki: 1646686292754
GUID: obonqow4T^; štítky: bi-psi::p04.

### Otázka (Front)

Jak funguje mobilita u IPv6?

### Odpověď (Back)

Stanice má přidělenou konrétní adresu ve své domácí síti. Když se stanice připojí v cizí síti pod jinou adresou, tak kontaktuje svůj domácí směrovač a ohlásí mu svou novou adresu. Jakmile jiná stanice chce mobilní stanici kontaktovat, zařídí domácí směrovač preposlání požadavku na její novou adresu a optimalizaci cesty.

