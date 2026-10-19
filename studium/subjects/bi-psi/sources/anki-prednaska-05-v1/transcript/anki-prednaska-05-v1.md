# BI-PSI – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 15 poznámek, 15 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1647259565002

Karty Anki: 1647259565002
GUID: Mt,c.6fn2M; štítky: bi-psi::p05.

### Otázka (Front)

Definujte cestu (ve směrování).

### Odpověď (Back)

Cesta je posloupnost směrovačů, kterou musí paket projít mezi zdrojovou a cílovou adresou.

## Poznámka Anki 1647259718751

Karty Anki: 1647259718751
GUID: Q!^xCC(x!A; štítky: bi-psi::p05.

### Otázka (Front)

Vyjmenujte druhy směrování.

### Odpověď (Back)

- optimální

- nejkratší
- nejlevnější

- redundantní (multipath)
- dle symetrie

- symetrické
- asymetrické

- dle způsobu hledání cesty

- záplavové
- proaktivní
- reaktivní

- dle oblasti výpočtu trasy

- vnitřní
- vnější

## Poznámka Anki 1647259921771

Karty Anki: 1647259921771
GUID: Gt4j+NJ/>G; štítky: bi-psi::p05.

### Otázka (Front)

Popište redundantní (multipath) směrování.

### Odpověď (Back)

Směrování k cílové stanici je možné několika disjunktními cestami, ze kterých je vybíráno na základě nějakého kritéria.

## Poznámka Anki 1647259964872

Karty Anki: 1647259964872
GUID: k=8<KYht/@; štítky: bi-psi::p05.

### Otázka (Front)

Popište asymetrické směrování.

### Odpověď (Back)

Asymetrické směrování znaměná, že dopředná (forward) a zpětná (reverse) cesta nejsou shodné.

## Poznámka Anki 1647260105339

Karty Anki: 1647260105339
GUID: G#Ujas]-K-; štítky: bi-psi::p05.

### Otázka (Front)

Popište záplavové směrování.

### Odpověď (Back)

Počáteční uzel osloví své sousedy zprávou (je opatřena ID) a ti oslovují zase své sousedy. Při příjmu stanice nejdříve zkontroluje, jestli zprávu už dříve neobdržela, pokud ano, tak ji zahodí, jinak s ní osloví své sousedy.
 [Obrázek: paste-127410e406692eec1fdb4b0a33aa3e797ab24d11.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1647260301119

Karty Anki: 1647260301119
GUID: Fm2[6c_!oK; štítky: bi-psi::p05.

### Otázka (Front)

Popište rozdíly mezi proaktivním a reaktivním směrováním.

### Odpověď (Back)

**Proaktivní směrování** využívá směrovací tabulky, používá se běžně a hlavně u málo proměnlivých sítí. Před odesláním zprávy je už cesta známá.
**Reaktivní směrování** směrovací tabulky nevyužívá. Setkáme se s ním hlavně v mobilních sítích. Před odesláním zprávy se většinou záplavovým směrováním najde cesta, která je po dokončení vysílání zapomenuta.

## Poznámka Anki 1647260565255

Karty Anki: 1647260565255
GUID: osibm,qep?; štítky: bi-psi::p05.

### Otázka (Front)

Popište rozdíly mezi statickou a dynamickou konfigurací směrovacích tabulek.

### Odpověď (Back)

**Statická konfigurace** probíhá z pravidla ve třech operacích: přidání, odebrání nebo změna záznamu. Probíhá manuálně, funguje okamžitě po zapnutí směrovače, ale neumí reagovat na změny.
U **dynamické konfigurace** si směrovače nastavují tabulky samy pomocí směrovacích protokolů, a díky tomu jsou schopné reagovat na změny. Využívá směrovací algoritmy.

## Poznámka Anki 1647260603904

Karty Anki: 1647260603904
GUID: xZAn)MHjr]; štítky: bi-psi::p05.

### Otázka (Front)

Vyjmenujte typy směrovacích protokolů.

### Odpověď (Back)

Směrovací protokoly lze rozdělit do následujících kategorií:

- distance-vector protokoly,

- link-state protokoly,

- path-vector protokoly.

## Poznámka Anki 1647260780217

Karty Anki: 1647260780217
GUID: j(?pf$-))>; štítky: bi-psi::p05.

### Otázka (Front)

Popište distance-vector směrovací protokoly.

### Odpověď (Back)

Distance-vector směrovací protokoly fungují tak, že si každý směrovač pro všechny své sousedy udržuje informaci o vzdálenosti (např. hop count). Sousední směrovače si tyto informace vyměňují a každý směrovač si pak sestavuje vlastní směrovací tabulku pomocí modifikovaného Bellman-Fordova algoritmu. Do této kategorie směrovacích protokolů patří např. Routing Information Protocol (RIP).

## Poznámka Anki 1647261006205

Karty Anki: 1647261006205
GUID: Hx,H`;^fGI; štítky: bi-psi::p05.

### Otázka (Front)

Popište link-state směrovací protokoly.

### Odpověď (Back)

Link-state směrovací protokoly fungují tak, že si směrovače vyměňují informace o stavu a ohodnocení linek. Z nich konstruují ohodnocený graf sítě a pomocí Dijkstrova algoritmu hledají nejkratší cesty ke všem ostatním směrovačům. Do této kategorie směrovacích protokolů patří např. Open Shortest Path First (OSPF) nebo Intermediate System to Intermediate System (IS-IS).

## Poznámka Anki 1647261375312

Karty Anki: 1647261375312
GUID: y23*$H1j&&; štítky: bi-psi::p05.

### Otázka (Front)

Co je to autonomní systém?

### Odpověď (Back)

Autonomní systém je skupina všech IP adresních rozsahů konkrétního ISP. Každý AS má svůj identifikátor, který se využívá při vnějším směrování.

## Poznámka Anki 1647261443369

Karty Anki: 1647261443369
GUID: idY10ydYUp; štítky: bi-psi::p05.

### Otázka (Front)

Co je to vnitřní a vnější směrování? Jaké používají protokoly?

### Odpověď (Back)

Vnitřní směrování probíhá uvnitř sítě jednoho ISP, používá protokoly OSPF a RIP.
Vnější směrování je směrování mezi sítěmi různých ISP, používá např. protokol BGP.

## Poznámka Anki 1647261543003

Karty Anki: 1647261543003
GUID: A7&b~U6CeT; štítky: bi-psi::p05.

### Otázka (Front)

Popište path-vector směrovací protokoly.

### Odpověď (Back)

Path-vector směrovací protokoly fungují tak, že si kromě vzdáleností vyměňují i kompletní cesty (posloupnosti směrovačů) ke konkrétním cílům. Do této kategorie směrovacích protokolů patří Border Gateway Protocol (BGP).

## Poznámka Anki 1647261787221

Karty Anki: 1647261787221
GUID: e!9z]D=Bu@; štítky: bi-psi::p05.

### Otázka (Front)

Jak se propojují autonomní systémy?

### Odpověď (Back)

Autonomní systémy se propojují pomocí hraničních směrovačů, které používají protokol BGP pro dynamickou konfiguraci směrovacích tabulek pro adresní rozsahy jiných AS.

## Poznámka Anki 1647261854427

Karty Anki: 1647261854427
GUID: ubS>[a=TXZ; štítky: bi-psi::p05.

### Otázka (Front)

Co je to transistentní a netransistentní autonomní systém?

### Odpověď (Back)

Transistentní AS je takový AS, který přeposílá provoz jinému AS prostřednictvím své vnitřní sítě. Netransistentní AS přijímá provoz pouze pro své vnitřní stanice.

