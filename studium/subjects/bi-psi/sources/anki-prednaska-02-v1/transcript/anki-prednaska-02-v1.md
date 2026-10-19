# BI-PSI – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 32 poznámek, 32 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1645445892280

Karty Anki: 1645445892280
GUID: Ou[U|&l3qU; štítky: bi-ib::11 bi-psi::p02.

### Otázka (Front)

Jaký je účel linkové vrstvy, co je základní přenášenou jednotkou a jaké má podvrstvy?

### Odpověď (Back)

Hlavním účelem linkové vrstvy je přenášení dat v rámci lokální sítě. Základní přenášenou jednotkou je rámec. Její podvrstvy jsou:

- Medium Access Control (MAC)
- Logical Link Control (LLC)

## Poznámka Anki 1645446117637

Karty Anki: 1645446117637
GUID: f}!n3M]@H:; štítky: bi-ib::11 bi-psi::p02.

### Otázka (Front)

Popište MAC.

### Odpověď (Back)

Medium Access Control je podvrstva linkové vrstvy.

- zajišťuje:

- předávání dat fyzické vrstvě
- sdílený přístup k médiu přes multiplex popř. přístupové metody
- přepínání, doručování rámců (také jejich ukládání do front a plánování odesílání)

- definuje linkové (MAC) adresy
- je hardwarově závislá

## Poznámka Anki 1645446331915

Karty Anki: 1645446331915
GUID: CXfwI-DwmU; štítky: bi-ib::11 bi-psi::p02.

### Otázka (Front)

Definujte multiplex a vyjmenujte jeho druhy. Co je to kolize?

### Odpověď (Back)

Multiplex je technika umožňující současné použítí stejného přenosového média více účastníky. Současný přístup k jednomu médiu se označuje jako **multiple access**. Pokud nastane současné a neoddělitelné použítí média více účastníky, dojde ke **kolizi **(ta může vznikat v kolizní doméně).
Mezi nejběžnější typy multiplexu patří:

- časový (Time Division Multiple Access)
- frekvenční (Frequency Division Multiple Access)
- kódový (Code Division Multiple Access)
- prostorový (Space Division Multiple Access)

## Poznámka Anki 1645446397172

Karty Anki: 1645446397172
GUID: T2O+p3`,I; štítky: bi-psi::p02.

### Otázka (Front)

Definujte kolizní doménu.

### Odpověď (Back)

Kolizní doména (Collision Domain) je množina stanic sdílících stejné médium. Současné vysílání více stanic způsobí kolizi.

## Poznámka Anki 1645446463891

Karty Anki: 1645446463891
GUID: C#P4xtp{M.; štítky: bi-psi::p02.

### Otázka (Front)

Definujte časový multiplex (TDMA).

### Odpověď (Back)

Médium je v konkrétním časovém okamžiku využíváno pouze jedním účastníkem. Účastníci se střídají ve vymezených časových intervalech.

## Poznámka Anki 1645446512382

Karty Anki: 1645446512382
GUID: E`_U$N~RGV; štítky: bi-psi::p02.

### Otázka (Front)

Definujte frekvenční multiplex (FDMA).

### Odpověď (Back)

Médium je současně využíváno vícero účastníky avšak na různých frekvenčních pásmech.

## Poznámka Anki 1645446677936

Karty Anki: 1645446677936
GUID: MAo#Ge`%M5; štítky: bi-psi::p02.

### Otázka (Front)

Popište způsob využití frekvenčního multiplexu v optických sítích (WDM).

### Odpověď (Back)

WDM (Wavelength Division Multiplex) spočívá v tom, že se do optického vláka vpouští více různěbarevných zdrojů (frekvence vlnění světla ovlivňuje jeho barvu). Na vstupu se barvy složí pomocí multiplexoru (MUX) a na výstupu opět rozdělí pomocí demultiplexoru (DEMUX).

## Poznámka Anki 1645446803356

Karty Anki: 1645446803356
GUID: kewv`CI2D); štítky: bi-psi::p02.

### Otázka (Front)

Definujte kódový multiplex (CDMA)

### Odpověď (Back)

Médium je v konkrétním časovém okamžiku využíváno více účastníky, kteří však zpracovávají pouze to, čemu rozumějí (svému kódu).

## Poznámka Anki 1645446882924

Karty Anki: 1645446882925
GUID: zfuOhA8Txt; štítky: bi-psi::p02.

### Otázka (Front)

Popište prostorový multiplex (SDMA).

### Odpověď (Back)

Médium je současně využíváno několika různými účastníky tak, že vysílání (může být i na stejné frekvenci) prochází různými vzájemně se nepřekrývajícími směry.

## Poznámka Anki 1645447069130

Karty Anki: 1645447069130
GUID: !/q2~<q&e; štítky: bi-ib::11 bi-ib::13 bi-psi::p02.

### Otázka (Front)

Definujte MA metody s příposlechem přenosového média a vyjmenujte varianty.

### Odpověď (Back)

Stejně jako multiplex, se snaží zabránit kolizím. Základem je naslouchání stavu přenosového média (Carrier Sense).
Existují dvě základní varianty:

- CSMA/CD - Collision Detection
- CSMA/CA - Collision Avoidance

## Poznámka Anki 1645447315065

Karty Anki: 1645447315065
GUID: zaRR,p8uy?; štítky: bi-ib::11 bi-psi::p02.

Metadata původního zdroje pro kartu 1645447315065: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište princip metody CSMA/CD.

### Odpověď (Back)

[Obrázek: paste-2709080292a73372bb63540b7bb81d7c9dc4f2ff.jpg; soubor je v media/ v doprovodném ZIP] 
**Jam** je signál informující všechny účastníky, že došlo ke kolizi.
**Náhodná doba čekání** snižuje pravděpodobnost opětovného přistupu více účastníků ve stejnou dobu.
Stále však může dojít ke kolizi a to v **kolizním okénku**, což je doba od začátku vysílání, během které se signál teprve šíří po médiu.

## Poznámka Anki 1645447967785

Karty Anki: 1645447967785
GUID: Lh1roq*a}=; štítky: bi-ib::13 bi-psi::p02.

### Otázka (Front)

Popište princip metody carrier-sense multiple access with collision avoidance (CSMA/CA). Kde se využívá a jaké jsou její problémy?

### Odpověď (Back)

Metoda carrier-sense multiple access with collision avoidance (CSMA/CA) se využívá zejména v bezdrátových sítích a funguje podle následujícího schématu:

 [Obrázek: paste-a2291ca14920f9f22a5163c338b536783eb5a352.jpg; soubor je v media/ v doprovodném ZIP] 

CSMA/CA nedokáže sama reagovat na kolize a opětovné odeslání dat tak musí vyžádat vyšší vrstva OSI modelu. Navíc neřeší problém skrytého uzlu v plném rozsahu a často se proto rozšiřuje o RTS/CTS mechanismus.

## Poznámka Anki 1645448289051

Karty Anki: 1645448289051
GUID: J0aC:4reDd; štítky: bi-ib::11 bi-psi::p02.

### Otázka (Front)

Popište LLC.

### Odpověď (Back)

Logial Link Control (LLC) je podvrstva linkové vrstvy.

- zajištuje:

- logické řízení toku a kontrolu chyb
- rozdělení toku dat z vyšších vrstev do rámců (framing)
- určování velikosti a konce rámce

- definuje potvrzovací schémata pro spolehlivé doručování rámců
- není hardwarově závislá

## Poznámka Anki 1645448359195

Karty Anki: 1645448359195
GUID: mSeL<D@2vK; štítky: bi-psi::p02 bi-spol::25.

### Otázka (Front)

Vyjmenujte potvrzovací schémata řízení toku dat.

### Odpověď (Back)

- jednotlivé potvrzování (Stop & Wait)
- kontinuální potvrzování se selektivním opakováním (Selective Repeat)
- kontinuální potvrzování s návratem (Go-Back-N)
- klouzavé okénko (Sliding Window)

## Poznámka Anki 1645448586732

Karty Anki: 1645448586732
GUID: s.IHSxDVV*; štítky: bi-psi::p02 bi-spol::25.

### Otázka (Front)

Popište princip jednotlivého potvrzování (Stop & Wait).

### Odpověď (Back)

[Obrázek: paste-04ab36bd50318820b28082632518c94dc587e0e7.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1645448647433

Karty Anki: 1645448647433
GUID: y93]P<uX&j; štítky: bi-psi::p02 bi-spol::25.

### Otázka (Front)

Popište princip kontinuálního potvrzování se selektivním opakováním (Selective Repeat).

### Odpověď (Back)

[Obrázek: paste-1d3d70f8f91c29d9f65b655e91df2063f7bd3d17.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1645448676940

Karty Anki: 1645448676940
GUID: xMV^iL%1(4; štítky: bi-psi::p02 bi-spol::25.

### Otázka (Front)

Popište princip kontinuálního potvrzování s návratem (Go-Back-N).

### Odpověď (Back)

[Obrázek: paste-e30154599024f00b540e66bd428240665318c792.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1645448788666

Karty Anki: 1645448788666
GUID: Q6)!/4Doc4; štítky: bi-psi::p02 bi-spol::25.

### Otázka (Front)

Popište princip klouzavého okénka (Sliding Window).

### Odpověď (Back)

[Obrázek: paste-5ac19799de83d3f021dd6d4e9c0ce4b4bfd46699.jpg; soubor je v media/ v doprovodném ZIP] 
Přijímač vždy potvrzuje nejvyšší čílo rámce, které tvoří souvislou ucelenou řadu od počátku vysílání. Vysílač posílá najednou souvislou řadu rámců (počet udává velikost okénka), která začíná rámcem o číslo vyšším, než byl poslední potvrzený.

## Poznámka Anki 1645449620273

Karty Anki: 1645449620273
GUID: JCr*z|^qqa; štítky: bi-psi::p02.

### Otázka (Front)

Jaká zařízení pracují na linkové vrstvě?

### Odpověď (Back)

přepínač (switch) a most (bridge)

## Poznámka Anki 1645449648715

Karty Anki: 1645449648715
GUID: Ea:o5Z]>SI; štítky: bi-psi::p02.

### Otázka (Front)

Co je to MTU?

### Odpověď (Back)

Maximum Transfer Unit označuje maximální možnou velikost přenášených dat.

## Poznámka Anki 1645449970868

Karty Anki: 1645449970868
GUID: L7PQ}{hcPQ; štítky: bi-ib::11 bi-psi::p02.

### Otázka (Front)

Popište princip přepínání přepínače.

### Odpověď (Back)

Přepínač obsahuje vstupně/výstupní porty, na kterých jsou připojeny komunikační linky. Porty obsahují buffery (vyrovnávací pamět), kde lze rámce při vstupu či výstupu zadržovat. Přepínání spočívá v obdržení rámce (frame in), jeho zpracování a odeslání portem směrem k příjemci (frame out), k výběru tohoto portu (dle MAC adresy příjemce) slouží **přepínací tabulka **(switching table). Záznamy v ní se aktualizují učením. Rámec s neznámou adresou příjemce se pošle na všechny porty krom portu, ze kterého přišel a zaznamená se, ze kterého portu přišla odpověď.

## Poznámka Anki 1645450124025

Karty Anki: 1645450124025
GUID: PdHjL%RE^u; štítky: bi-psi::p02.

### Otázka (Front)

Vyjmenujte a popište režimy práce přepínačů.

### Odpověď (Back)

**Store-And-Forward **(SF)

- přepínač přijme rámec, uloží jej a až pak ho pošle dál
**Cut-Through** (CT)

- přepínač načte jen cílovou adresu z hlavičky rámce, překontroluje ji a okamžitě přepošle data
**Fragment-Free **(FF)

- podobný jako cut-through
- načítáno a kontrolováno je více dat (typicky celá hlavička)
- dokáže odhalit větší množství chybných rámců

## Poznámka Anki 1645467361106

Karty Anki: 1645467361107
GUID: t|H6L1<9kX; štítky: bi-psi::p02.

### Otázka (Front)

K čemu slouží mosty (bridges)?

### Odpověď (Back)

Mosty propojují resp. oddělují provoz více částí sítě (jako přepínače obsahují přepínací tabulky). Mohou být realizovány softwarově nebo hardwarově.

## Poznámka Anki 1645468004581

Karty Anki: 1645468004582
GUID: Bj$FhFnzQm; štítky: bi-psi::p02.

### Otázka (Front)

Porovnejte mosty (bridges) a přepínače (switches).

### Odpověď (Back)

**Mosty**

- jednodušší, méně portů (2 až 4)
- propojují většinou jen dvě sítě
- nemají buffery (vyrovnávací paměť)
**Přepínače**

- složitější, více portů (až stovky)
- hardwarová podpora zpracování rámců na úrovni chipsetu (přepínání nezatěžuje procesor)
- mají buffery (vyrovnávací paměť), lze regulovat výstupní tok
- u dražších modelů možnost webového rozhraní, vzdáleného modelování, atd.

## Poznámka Anki 1645469116292

Karty Anki: 1645469116293
GUID: hFn&5=>I1^; štítky: bi-psi::p02.

### Otázka (Front)

Definujte broadcastovou doménu.

### Odpověď (Back)

Broadcastová doména je množina všech stanic dané sítě, kterým je doručen rámec s všesměrovou adresou. Jednotlivé broadcastové domény jsou od sebe oddělovány zařízeními síťové vrstvy (směrovači).

## Poznámka Anki 1645469237541

Karty Anki: 1645469237541
GUID: P?KGur]}s{; štítky: bi-ib::11 bi-psi::p02.

### Otázka (Front)

Definujte Ethernet.

### Odpověď (Back)

Jde o dnes nejběžnější technologii linkové vrstvy. Vyvíjí se podle standardu IEEE 802.3.

## Poznámka Anki 1645469387914

Karty Anki: 1645469387914
GUID: QL&X_,zBW^; štítky: bi-psi::p02.

### Otázka (Front)

Popište složení MAC adresy a její velikost.

### Odpověď (Back)

Standardní velikost MAC adresy je 48 bitů (6 bytů). První tři byty jsou OUI (Organization Unique Identifier) a označují výrobce. Zbylé tři byty označují sériové číslo daného zaříení.

## Poznámka Anki 1645469552868

Karty Anki: 1645469552868
GUID: xFy`x)!iC=; štítky: bi-ib::11 bi-ib::13 bi-ib::21 bi-psi::p02.

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
- **length or type** - délka nebo Ethertype rámce,

- **P/Q tag** - obsažen v tagovaných 802.1q/p rámcích (VLAN),
- **FCS** (frame check sequence) - kontrola chyb pomocí CRC-32.

## Poznámka Anki 1645469743412

Karty Anki: 1645469743412
GUID: v$*d<N(J5[; štítky: bi-psi::p02.

### Otázka (Front)

Popište způsob označování druhů Ethernetového média.

### Odpověď (Back)

[Obrázek: paste-7d21031dcdfd7aeb3de542bb97ad806e827d5e25.jpg; soubor je v media/ v doprovodném ZIP] 
**Specifikace média**: délka a typ (T - twisted pair, F - fiber)
**Směrovost média**: Full-Duplex (FD), Half-Duplex (HD)

## Poznámka Anki 1645469905144

Karty Anki: 1645469905144
GUID: GZcU;Bv<O6; štítky: bi-psi::p02.

### Otázka (Front)

Popište mechanismus řízení toku v Ethernetu.

### Odpověď (Back)

Příkazem **PAUSE** může přepínač požádat o zpomalení vysílání. Lze ho odvysílat všemi komunikačními operacemi (unicast, multicast, atd.). Ethernet však neobsahuje mechanismus garance spolehlivého doručení dat.

## Poznámka Anki 1645470043626

Karty Anki: 1645470043626
GUID: c/(=dd|oi,; štítky: bi-psi::p02.

### Otázka (Front)

Definujte autonegociaci.

### Odpověď (Back)

Autonegociace je metoda, kterou si vysílač a přijímač dohodnou parametry přenosu (max. průtok, modulaci, kódování). Konkrétním dojednaným parametrům se říká **slinkování**. Umožňuje zpětnou kompatibilitu zařízení.

## Poznámka Anki 1645470307361

Karty Anki: 1645470307362
GUID: w0xBn-p`]b; štítky: bi-psi::p02.

### Otázka (Front)

Jakým typem kabelu se připojují zařízení v Ethernetu.

### Odpověď (Back)

Počítače se mezi sebou bez přepínačů připojují kříženým kabelem (crossover).
Počítače s přepínači se běžně propojují přímým kabelem.

