# BI-PSI – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1647881260104

Karty Anki: 1647881260106
GUID: w6V>S}h?)]; štítky: bi-psi::p06 bi-spol::25.

### Otázka (Front)

Popište port a dělení portů.

### Odpověď (Back)

Port je 16bitový identifikátor, který se používá jako další adresační stupeň na transportní vrstvě. Typicky identifikuje proces nebo službu, která je cílem komunikace. Porty rozdělujeme na:      
|       well-known
 |       0-1023 |         
|       registered
 |       1024-49151 |         
|         
|       dynamic
 |       49152-65535 |

## Poznámka Anki 1647881444198

Karty Anki: 1647881444199
GUID: PAnP{RWUGe; štítky: bi-psi::p06 bi-spol::25.

### Otázka (Front)

Uveďte parametry přenosu dat transportní vrstvy.

### Odpověď (Back)

- ztrátovost (packet loss) - procento paktetů, které je ztraceno v přenosu
- zpoždění (delay) - průměrná doba doručení paketů mezi zdrojem a cílem v ms
- obousměrné zpoždění (Round Trip Time) - průměrná doba doručení paketů mezi zdrojem, cílem a zpět v ms
- nestabilita, variabilní zpoždění (Jitter) - kolísání zpoždění

## Poznámka Anki 1647881538472

Karty Anki: 1647881538472
GUID: k+(-XWF21Q; štítky: bi-psi::p06.

### Otázka (Front)

Popište algoritmus Stop & Go.

### Odpověď (Back)

Vysílač posílá přijímači posloupnost paketů. Jakmile vysílač obdrží zprávu STOP, vysílání ukončí a čeká, dokud nedostane zprávu GO.

## Poznámka Anki 1647881685815

Karty Anki: 1647881685815
GUID: tDfU+[:e^5; štítky: bi-ib::11 bi-psi::p06 bi-spol::25.

### Otázka (Front)

Jak dělíme protokoly transportní vrstvy? Na co jsou orientované?

### Odpověď (Back)

- spolehlivé - pokud je to možné, data jsou vždy doručena

- spojově orientované - mezi směrovači se sestavuje a drží virtuální spojení
- typicky protokol TCP

- nespolehlivé - data se mohou během přenosu ztratit

- paketově orientované - data se odesílají po částech a spojení se nevytváří
- implementačně jednodušší
- typicky protokol UDP

## Poznámka Anki 1647881830901

Karty Anki: 1647881830902
GUID: JZTuL{l8MG; štítky: bi-psi::p06 bi-spol::25.

### Otázka (Front)

Popište Transmission Control Protocol (TCP).

### Odpověď (Back)

- umožňuje řízení toku (klouzavé okénko) i eliminaci zahlcení (Congestion Window)
- zabezpečený proti chybám, garantuje i pořadí doručených paketů
- je duplexní (každá strana otevírá vlastní spojení)

## Poznámka Anki 1647882116502

Karty Anki: 1647882116502
GUID: f=D8s8N0~.; štítky: bi-psi::p06 bi-spol::25.

### Otázka (Front)

Popište životní cyklus TCP spojení.

### Odpověď (Back)

1. sestavení spojení

- příznak SYN v hlavičce TCP paketu znamená otevření spojení ze strany A
- příznak SYN ACK potvrzuje doručení SYN ze strany A a otevírá spojení ze strany B
- strana A potvrzuje paketem s příznakem ACK

2. přenos dat

- posílání dat z A, příjem ACK od B

3. ukončení spojení

- FIN od A uzavírá spojení ze strany A
- FIN ACK od B potvrzuje uzavření spojení ze strany A
- FIN od B uzavírá spojení ze strany B
- ACK od A potvrzuje uzavření spojení ze strany B

 [Obrázek: paste-679eb0f853a78aba47284c5e169b1a9c173e6449.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1647882181422

Karty Anki: 1647882181422
GUID: F}h&$e&UMC; štítky: bi-psi::p06 bi-spol::25.

### Otázka (Front)

Co je to sekvenční číslo u TCP paketů?

### Odpověď (Back)

Sekvenční číslo udává aktuální pořadové číslo paketu v rámci spojení. Počáteční hodnota je typicky náhodná, je domluvena při zahájení spojení a postupně se inkrementuje.

## Poznámka Anki 1647882737101

Karty Anki: 1647882737101
GUID: uXP:8dZBoF; štítky: bi-psi::p06 bi-spol::25.

### Otázka (Front)

Popište délku sliding window a congestion window a principy jejich nastavení.

### Odpověď (Back)

Délka sliding window i congestion window je nastavována dynamicky v závislosti na stavu sítě. Protože TCP je duplexní, jsou délky pro každý směr komunikace řízeny separátně. Mezi délkou sliding window a congestion window jsou následující rozdíly:      
|       **délka sliding window**
 |       **délka congestion window**
 |         
|       počet segmentů, které je možné odeslat najednou bez potvrzení |       počet segmentů, které je možné odeslat najednou, anižby došlo k zahlcení |         
|         
|       nastavuje přijímač |       nastavuje vysílač |       Navíc platí, že congestion window má prioritu nad sliding window. To znamená, že v případě, že je délka congestion window nižší než délka sliding window, bude posíláno pouze tolik segmentů, kolik určuje délka congestion window.

## Poznámka Anki 1647882836867

Karty Anki: 1647882836867
GUID: k&6d*J>&vr; štítky: bi-psi::p06 bi-spol::25.

### Otázka (Front)

Co je to Fast Retransmit u TCP?

### Odpověď (Back)

Při komunikaci podle klouzavého okénka si vysílač navíc pamatuje dobu, po kterou mu určitý paket nebyl potvrzen. Jakmile doba překročí nastavený timeout, sám bez výzvy daný paket odešle znovu. Důvodem je zvýšení efektivity přenosu.

## Poznámka Anki 1647893826012

Karty Anki: 1647893826013
GUID: bQT_?_`CIm; štítky: bi-psi::p06 bi-spol::25.

### Otázka (Front)

Popište User Datagram Protocol (UDP).

### Odpověď (Back)

UDP má lepší propustnost než TCP kvůli nižší režii a využívá se zejména pro real time přenosy. Je nezabezpečený a negarantuje doručení ani pořadí paketů.

## Poznámka Anki 1647893991113

Karty Anki: 1647893991113
GUID: I1F4+:T.#M; štítky: bi-psi::p06 bi-spol::25.

### Otázka (Front)

Popište překlad adres (NAT) na transportní vrstvě.

### Odpověď (Back)

Díky portům je možné odlišit různá současná spojení jdoucí od více stanic ke stejnému cíli přes stejnou veřejnou IP adresu. Směrovač provádí mapování vnitřní zdrojové IP a vnitřního zdrojového portu na vnější zdrojovou IP a vnější zdrojový port a naopak.

