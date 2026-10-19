# BI-BEK – Přednáška 13

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1684497607909

Karty Anki: 1684497607909
GUID: Li8BfFO?sv; štítky: bi-bek::p13 bi-ib::07 bi-ib::11 bi-ib::21 bi-spol::25.

### Otázka (Front)

Co je to denial-of-service (DoS) útok.

### Odpověď (Back)

Denial-of-service (DoS) útok je útok z jednoho zdroje na počítač, aplikaci, sdílený prostředek nebo službu, jehož účelem je učinit cíl částečně nebo úplně nedostupným pro legitimní uživatele.

## Poznámka Anki 1684498664278

Karty Anki: 1684498664278
GUID: lf$^9+BG@J; štítky: bi-bek::p13 bi-ib::21 bi-spol::25.

### Otázka (Front)

Na co může útočník při denial-of-service útoku útočit?

### Odpověď (Back)

V rámci denial-of-service útoku lze útočit na:

- stabilitu aplikace či operačního systému (např. Ping of Death),
- na CPU či paměť s cílem jejich zahlcení (např. extrémně velký konfigurační soubor),
- na prostředky (např. vyčerpání pipes v OS).

## Poznámka Anki 1684499469830

Karty Anki: 1684499469830
GUID: D;^]9U$P;n; štítky: bi-bek::p13 bi-ib::11 bi-ib::21.

### Otázka (Front)

Co je to distributed denial-of-service (DDoS) útok.

### Odpověď (Back)

Distributed denial-of-service (DDoS) útok je typ denial-of-service (DoS) útoku, při kterém je na jednu oběť útočeno současně z několika různých zdrojů.

## Poznámka Anki 1684500496054

Karty Anki: 1684500496054
GUID: PD5I43iPX); štítky: bi-bek::p13 bi-ib::11 bi-ib::21 bi-spol::25.

Metadata původního zdroje pro kartu 1684500496054: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište SYN flood útok.

### Odpověď (Back)

SYN flood útok je typ denial-of-service (DoS) útoku, který cílí na implementaci TCP protokolu. Většina zařízení totiž při obdržení SYN paketu alokuje prostředky, které se dealokují až při naplnění timeoutu. Útok tedy spočívá v zahlcení serveru SYN pakety, čímž dojde k zaplnění jeho \(\mathtt{listen}\) fronty. Server je pak donucen odmítat nově příchozí požadavky.

## Poznámka Anki 1684501429713

Karty Anki: 1684501429713
GUID: rr;St|A1W0; štítky: bi-bek::p13 bi-ib::11 bi-ib::21 bi-spol::25.

Metadata původního zdroje pro kartu 1684501429713: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište obrany proti SYN flood útokům?

### Odpověď (Back)

Proti SYN flood útokům se lze chránit následujícími prostředky:

- **filtrování** - znemožní útočníkovi poslat paket z podvržené IP adresy;

- **zvětšení kapacity **\(\mathtt{listen}\) **fronty** - problematické, problémy se škálovatelností;

- **zmenšení timeoutu** - může odepřít legitimní požadavky;
- **recyklování nejstarších polootevřených spojení** - neefektivní při malé kapacitě fronty nebo vysoké frekvenci útoku;

- **SYN cache** - nahrazuje \(\texttt{listen}\) frontu hashovací tabulkou, čímž minimalizuje množství alokovaných prostředků;

- **SYN** **cookies** - stavová informace se ukládá do pořadového čísla v SYN ACK paketu a prostředky jsou alokovány až po dokončení celého handshaku.

## Poznámka Anki 1684501986559

Karty Anki: 1684501986559
GUID: c-SsFG/HWE; štítky: bi-bek::p13 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište útok Teardrop.

### Odpověď (Back)

Teardrop je historický typ denial-of-service útoku, který zneužívá fragmentaci IP paketů. Kód, který pakety rekonstruuje zpravidla předpokládá, že se fragmenty paketů vzájemně nepřekrývají. Pokud tato situace nastane, může dojít k pádu TCP stacku, který je typicky součástí OS.

## Poznámka Anki 1684502521651

Karty Anki: 1684502521651
GUID: o,|Q#@wfNW; štítky: bi-bek::p13 bi-ib::11 bi-ib::21.

### Otázka (Front)

Popište ICMP flood útok.

### Odpověď (Back)

ICMP flood je typ denial-of-service útoku, který spočívá v tom, že útočník pošle oběti záplavu ICMP Echo Request paketů o velkých velikostech s falešnou adresou odesílatele. Oběť bude odpovídat na adresu podvrženého odesílatele ICMP Echo Reply pakety, které budou kopírovat velikost původních ICMP Echo Request paketů. Tím může dojít k zahlcení síťového rozhraní či linky.

## Poznámka Anki 1684503220671

Karty Anki: 1684503220671
GUID: b78y]DfDoo; štítky: bi-bek::p13 bi-ib::11 bi-ib::21 bi-spol::25.

Metadata původního zdroje pro kartu 1684503220671: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište reflection (amplification) denial-of-service (RDoS) útok.

### Odpověď (Back)

Reflection (amplification) denial-of-service (RDoS) útok je typ denial-of-service (DoS) útoku, který zneužívá toho, že některé protokoly (např. DNS, NTP a SSDP) na relativně malý dotaz odpoví podstatně větší odpovědí. Útočník tedy zpravidla posílá dotazy s podvrženou zdrojovou adresou a dotazovaný server zahltí oběť svými odpověďmi na podvrženou adresu.

## Poznámka Anki 1684503500545

Karty Anki: 1684503500545
GUID: D!L!}SwdP; štítky: bi-bek::p13 bi-ib::11 bi-ib::21.

### Otázka (Front)

Co je to permanent denial-of-service (PDoS) útok?

### Odpověď (Back)

Permanent denial-of-service (PDoS) útok je typ denial-of-service útoku, jehož cílem je zničení zařízení oběti.

## Poznámka Anki 1684503796113

Karty Anki: 1684503796113
GUID: NAdvZ1v7zd; štítky: bi-bek::p13 bi-ib::11 bi-ib::21 bi-spol::25.

### Otázka (Front)

Jak se lze bránit proti denial-of-service útokům?

### Odpověď (Back)

Mezi metody ochrany proti denial-of-service útokům patří:

- filtrování provozu na routeru či firewallu,
- kontrola provozu pomocí IDS nebo IPS,
- použití kvót či historie spojení.

