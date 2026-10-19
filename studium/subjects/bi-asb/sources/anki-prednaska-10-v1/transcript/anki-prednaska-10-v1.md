# BI-ASB – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-asb/BI-ASB.apkg; APKG SHA-256 7a0706fba841a39fa40ea1e5439c99f14f59930aaa7f6d5620a33590d53350fa. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: eea4a1b952e7287bc51501f27ae2f5ec76f032fca049ee9ef600d2729e12ef40.
Původní balíčky: BI-ASB
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1702293945095

Karty Anki: 1702293945095
GUID: M%#W(NC:hD; štítky: bi-asb::p10.

### Otázka (Front)

Popište rozdíl mezi layer a tier?

### Odpověď (Back)

**Layer **popisuje logickou organizaci a architekturu kódu aplikace. Jde o část kódu poskytující konkrétní funkcionalitu. Kdežto **tier** popisuje fyzickou infrastrukturu, na které je kód aplikace spouštěn.

## Poznámka Anki 1702294256433

Karty Anki: 1702294256433
GUID: t+,yPmlK&_; štítky: bi-asb::p10.

### Otázka (Front)

Popište n-tier (multitier) architecture.

### Odpověď (Back)

N-tier (multitier) architecture je typ architektury klient-server aplikací, která rozděluje prezentační, aplikační a datové funkcionality aplikace do logicky oddělených layerů a fyzicky oddělených tierů. Zásadní je, že vzájemně mohou komunikovat pouze sousední vrstvy. Nejčastěji se setkáváme s three-tier architecture.

## Poznámka Anki 1702294940403

Karty Anki: 1702294940403
GUID: GKEmZ@${c5; štítky: bi-asb::p10.

### Otázka (Front)

Popište three-tier architecture.

### Odpověď (Back)

Three-tier architecture je typ n-tier (multitier) architecture, která se skládá z následujících vrstev:

- **presentation tier **- poskytuje rozhraní uživateli;

- **application tier** - zpracovává požadavky, provádí rozhodování, realizuje business logic aplikace a zprostředkovává komunikaci mezi presentation tier a data tier;

- **data tier** - zapisuje a čte data z úložiště.

## Poznámka Anki 1702295494332

Karty Anki: 1702295494332
GUID: kwJPd:So*W; štítky: bi-asb::p10.

### Otázka (Front)

Popište škálování v three-tier architecture.

### Odpověď (Back)

Existují tři přístupy ke škálování v three-tier architecture:

- **vertikální **- každý layer má dedikovaný server, škáluje se alokací více prostředků konkrétnímu serveru;
- **horizontální **- tier se skládá z více serverů, škáluje se přídáním dalšího serveru;
- **diagonální** - kombinace vertikálního a horizontálního přístupu.

## Poznámka Anki 1702296538035

Karty Anki: 1702296538035
GUID: n_CiNr8/S(; štítky: bi-asb::p10.

### Otázka (Front)

Popište rozdíl mezi chatty a chunky interface.

### Odpověď (Back)

**Chatty interface **je založeno na častější výměně kratších zpráv (např. načtení jména uživatele). Při četném používání generuje vysoký komunikační overhead. Oproti tomu **chunky interface **je založeno na méně časté výměně delších zpráv (např. načtení celého profilu uživatele). Tím je docíleno efektivnějšího přenosu dat za cenu zvýšené latence.

## Poznámka Anki 1702297105851

Karty Anki: 1702297105851
GUID: Ivv-*GJ8nt; štítky: bi-asb::p10.

### Otázka (Front)

Popište five-tier architecture.

### Odpověď (Back)

Five-tier architecture je typ n-tier (multitier) architecture, která se skládá z následujících vrstev:

- **client tier **- poskytuje rozhraní uživateli;

- **presentation tier **- prezentuje uživateli data z business logic tieru;

- **business logic tier **(business tier)** **- provádí rozhodování, realizuje business logic aplikace;
- **data access tier **(integration tier)** **- poskytuje abstrakci nad data tierem;
- **data tier **(enterprise tier) - zapisuje a čte data z úložiště.

