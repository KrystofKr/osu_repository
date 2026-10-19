# BI-PSI – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 20 poznámek, 20 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1648467498092

Karty Anki: 1648467498092
GUID: nKRP~vFs7!; štítky: bi-ib::11 bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co je to resolver, name server a DNS server?

### Odpověď (Back)

**Resolver** je server, který provádí překlad doménových jmen. Podle metody, kterou používá se rozlišujeme rekurzivní a iterativní resolvery. 
**Name server** je počítač, který se stará o překlad doménových jmen na IP adresy.
**DNS server** je NS pracující v systému DNS.

## Poznámka Anki 1648467886746

Karty Anki: 1648467886746
GUID: IaRbJK,DuY; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co je to DZZ a DNS?

### Odpověď (Back)

**Doménový zdrojový záznam **(DZZ) je konkrétní typ záznamů pro danou doménu.
**Domain Name System **(DSS) je systém pro správu domén a doménových záznamů.

## Poznámka Anki 1648467967946

Karty Anki: 1648467967946
GUID: gc$U&yhXGe; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co je to autoritativní DNS server?

### Odpověď (Back)

Pro konkrétní domény je to DNS server, který spravuje DZZ těchto domén.

## Poznámka Anki 1648468021240

Karty Anki: 1648468021240
GUID: O|es7e!ly}; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Jak může DNS provádět překlad doménových jmen?

### Odpověď (Back)

- **přímo** - doménovému jménu se přiřadí IP adresa
- **reverzně** - IP adrese se přiřadí doménové jméno

## Poznámka Anki 1648468216536

Karty Anki: 1648468216536
GUID: O9/XZd1@:; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co je to doménové jméno, doména (subdoména) a hloubka?

### Odpověď (Back)

**Doménové jméno** je posloupnost jmen od listu ke kořenu.
**Doména** je libovolný podstrom daného stromu.
**Hloubka** je počet zanoření ve stromu doménových jmen.
 [Obrázek: paste-8c325a4663d4fc9a3693c839562b9778b3de20cc.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1648468404175

Karty Anki: 1648468404175
GUID: luMW-l>)5l; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co jsou to kořenové DNS servery a k čemu slouží? Jak se dělí a jak jsou jim doručovány dotazy?

### Odpověď (Back)

Jsou to DNS servery 0. úrovně, tedy udržují informace o DNS serverech 1. úrovně. Dělí se do 13 skupin (A-M). Dotazy jsou jim doručovány pomocí anycastu (IPv6 nativně, IPv4 pomocí BGP).

## Poznámka Anki 1648468525325

Karty Anki: 1648468525325
GUID: xq/(O{t(l^; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co je to TLD? Jaké rozlišujeme typy?

### Odpověď (Back)

Top-Level Domain

- generic (gTLD) - .gov, .com, .net
- country code (ccTLD) - .cz, .us, .de
- new generic (ngTLD) - libovolné řetězce

## Poznámka Anki 1648468636500

Karty Anki: 1648468636500
GUID: eXoW05k$s|; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co je to FQDN?

### Odpověď (Back)

Fully Qualified Domain Name je zřetězení doménových jmen v jeden řetězec s použitím teček jako oddělovačů. Jeho maximální délka je 255 znaků.

## Poznámka Anki 1648468929330

Karty Anki: 1648468929331
GUID: A6jSw];)-#; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co je to zóna v DNS?

### Odpověď (Back)

Zóna je konrétní podmnožina množiny doménových jmen. DNS server starající se o překlad doménových jmen dané zóny je pro danou zónu autoritativní. Autoritativní DNS server může správu doménových jmen zóny (nebo subzóny) delegovat na jiný DNS server.

## Poznámka Anki 1648469301953

Karty Anki: 1648469301953
GUID: H=ZS5I(S3.; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Popište strukturu záznamu zóny.

### Odpověď (Back)

- úvodní záznam - všeobecné informace o zóně (vyskytuje se jednou)
- doménový zdrojový záznam (DZZ) - konkrétní informace pro konkrétní doménové jméno (běžně se vyskytuje vícekrát)

 [Obrázek: paste-e1d2883f5f22c278f45b31006b7a2cb533dacd8b.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1648469542320

Karty Anki: 1648469542320
GUID: H{9r`UFF}a; štítky: bi-ib::11 bi-psi::p07 bi-spol::25.

Metadata původního zdroje pro kartu 1648469542320: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište Domain Name System (DNS) a jeho protokol.

### Odpověď (Back)

**Domain Name System** (DNS) je systém poskytující schéma pro pojmenovávání počítačů, služeb a dalších zdrojů v internetu. Známý je zejména pro poskytování vzájemného překladu doménových jmen a IP adres. **DNS protokol** je pak protokol aplikační vrstvy používaný pro komunikaci v rámci DNS. Typicky je implementován pomocí UDP a používá port 53.

## Poznámka Anki 1648469720851

Karty Anki: 1648469720851
GUID: xHZ$;os_-F; štítky: bi-ib::11 bi-psi::p07 bi-spol::25.

### Otázka (Front)

Popište obecný formát DNS dotazu/odpovědi.

### Odpověď (Back)

[Obrázek: paste-66aa1cd854ea2b5cfc8322052103530d49ebe40b.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1648470213594

Karty Anki: 1648470213594
GUID: H~2XY7~meO; štítky: bi-psi::p07 bi-spol::25.

Metadata původního zdroje pro kartu 1648470213594: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište iterativní dotazování v Domain Name Systému (DNS).

### Odpověď (Back)

Iterativní dotazování v Domain Name Systému (DNS) je způsob dotazování, při kterém resolver obdrží buď odpověď na svůj dotaz, nebo odkaz na DNS server, kterého se má dále dotázat. Probíhá v následujících krocích:

- resolver dotáže svůj iterativní lokální DNS server;

- lokální DNS server prohledá svou cache a pokud nenalezne odpověď, odpoví resolveru odkazem na kořenové DNS servery;
- resolver dotáže kořenový DNS server;

- kořenový DNS server odpoví odkazem na DNS servery 1. úrovně

a tak dále dokud resolver neobdrží odpověď od autoritativního serveru dotazované domény.

## Poznámka Anki 1648474958184

Karty Anki: 1648474958184
GUID: c7<;3hm~^!; štítky: bi-psi::p07 bi-spol::25.

Metadata původního zdroje pro kartu 1648474958184: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište rekurzivní dotazování v Domain Name Systému (DNS).

### Odpověď (Back)

Rekurzivní dotazování v Domain Name Systému (DNS) je způsob dotazování, při kterém resolver obdrží buď odpověď na svůj dotaz, nebo definitivní rozhodnutí, že doménu nelze přeložit. Probíhá v následujících krocích:

- resolver dotáže svůj rekurzivní lokální DNS server;
- lokální DNS server prohledá svou cache a pokud nenalezne odpověď, dotáže kořenový DNS server;
- kořenový DNS server odpoví lokálnímu DNS serveru odkazem na DNS servery 1. úrovně;
- lokální DNS server dotáže DNS server 1. úrovně

a tak dále dokud lokální DNS server neobdrží odpověď od autoritativního DNS serveru dorazované domény. V ten moment odpověď předává resolveru.

### Doplňující pole (Extra)

Kořenové DNS servery a DNS servery 1. úrovně jsou typicky konfigurovány jako iterativní DNS servery. Pokud by tomu tak nebylo, tak namísto toho, aby odpověděly odkazem, by samy provedly rekurzivní dotaz na server úrovně o jedna níže.

## Poznámka Anki 1648475141971

Karty Anki: 1648475141971
GUID: xaof:BinyI; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Popište reverzní DNS dotaz.

### Odpověď (Back)

Reverzní dotaz zjišťuje doménové jméno pro zadanou IP. Pro IP AA.BB.CC.DD se vytvoří doménové jméno DD.CC.BB.AA.in-addr.arpa. 
Samotné provedení probíhá stejně jako u přímého dotazu s tím rozdílem, že finální překlad provádí DNS server organizace, který má daný adresní rozsah na starosti. Počet DNS dotazů tedy nemusí odpovídat počtu řetězců doménového jména.

## Poznámka Anki 1648475222471

Karty Anki: 1648475222471
GUID: MPh,/si:48; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co je to DynDNS?

### Odpověď (Back)

Dynamický DNS server je DNS server, který dokáže za běhu měnit záznamy pro doménová jména podle pokynů stanic.

## Poznámka Anki 1648475261302

Karty Anki: 1648475261303
GUID: hjq1%8_qn]; štítky: bi-ib::11 bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co je to DNSSEC?

### Odpověď (Back)

Jde o zabezpečenou verzi DNS, která ověřuje pravost odpovědí. Je založena na asymetrické kryptografii.

## Poznámka Anki 1648475327926

Karty Anki: 1648475327926
GUID: dc0pfR5e?@; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Co je to Load Balancing na úrovni DNS?

### Odpověď (Back)

Rozdělování zátěže spočívá v tom, že autoritativní DNS server vrací při opakovaném dotazu na stejné doménové jméno pokaždé jinou IP.

## Poznámka Anki 1648475416768

Karty Anki: 1648475416768
GUID: vA2[UU+:*x; štítky: bi-psi::p07.

Metadata původního zdroje pro kartu 1648475416768: původní příznak autora 6.

### Otázka (Front)

Co je to DNS Cache Poisoning?

### Odpověď (Back)

Je to typ útoku na DNS, kdy útočník odposlouchává síť a je schopen generovat falešné odpovědi DNS serveru, které stanice přijme za pravé, jelikož k ní dorazí dříve než ty správné.

## Poznámka Anki 1648502623513

Karty Anki: 1648502623513
GUID: sN]!C9iu`u; štítky: bi-psi::p07 bi-spol::25.

### Otázka (Front)

Vyjmenujte několik typů DZZ.

### Odpověď (Back)

Příklady DNS záznamů jsou:

- **A** - IPv4 adresa pro doménové jméno,
- **AAAA** - IPv6 adresa pro doménové jméno,
- **MX** - emailový server domény,
- **NS** - autoritativní DNS server domény.

