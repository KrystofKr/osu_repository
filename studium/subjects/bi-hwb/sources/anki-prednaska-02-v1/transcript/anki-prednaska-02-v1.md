# BI-HWB – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-hwb/BI-HWB.apkg; APKG SHA-256 0303626d2408f7eee1801e17ecb475633a60c42f914f37290ffd8c479013ce2b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b861d2e855c5070244800c22d62092a09b22aee0ded024030525b06a7d18285e.
Původní balíčky: BI-HWB
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1696251173878

Karty Anki: 1696251173879
GUID: xRs,DfR5`!; štítky: bi-hwb::p02.

Metadata původního zdroje pro kartu 1696251173879: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Trusted Platform Module (TPM).

### Odpověď (Back)

Trusted Platform Module je standard bezpečného kryptoprocesoru, který umožňuje využívání dalších bezpečnostních mechanik (např. Secure Boot, šifrování disku, key wrapping nebo key sealing).

## Poznámka Anki 1696252079479

Karty Anki: 1696252079479
GUID: c1eWYiD^;Y; štítky: bi-hwb::p02.

### Otázka (Front)

Popište Intel Trusted Execution Technology (Intel TXT).

### Odpověď (Back)

Intel Trusted Execution Technology (Intel TXT) je hardwarová technologie, která využívá TPM. Zajišťuje důvěryhodnost OS a prostředí a poskytuje další bezpečnostní služby jako:

- **měření **(measurements) - kód, data či konfigurace jsou hashovány a kontrolovány před tím, než jsou spouštěny či čteny;

- **chain of trust** - Static/Dynamic Root of Trust for Measurements.

## Poznámka Anki 1696253540146

Karty Anki: 1696253540146
GUID: vo6Vg-1_!.; štítky: bi-hwb::p02.

### Otázka (Front)

Popište System Management Mode (SMM).

### Odpověď (Back)

System Management Mode (SMM), někdy také označován jako ring -2, je operační mód procesorů, který se nachází pod kernel mode (ring 0). Umožňuje obsluhu System Management Interrupts (SMI), které slouží k hlášení HW poruch, řízení teploty a podobně. Pro OS je neviditelný, proto není vhodný pro systémy reálného času.

## Poznámka Anki 1696253795879

Karty Anki: 1696253795879
GUID: v%m1+g*g.S; štítky: bi-hwb::p02.

### Otázka (Front)

Popište direct memory access (DMA) útok. Uveďte typy portů, které mohou DMA povolovat.

### Odpověď (Back)

Direct memory access (DMA) útok je typ útoku postranním kanálem, kdy útočník získá přímý přístup do paměti skrze hardwarové porty. Mezi porty, které mohou dovolovat DMA patří FireWire, ExpressCard nebo Thunderbolt.

## Poznámka Anki 1696254385267

Karty Anki: 1696254385267
GUID: uk1I[vFZ%&; štítky: bi-hwb::p02.

### Otázka (Front)

Popište input-output memory management unit (IOMMU).

### Odpověď (Back)

Input-output memory management unit je memory management unit (MMU), která překládá adresy přidělené pomocí paměťově mapovaného I/O na fyzické adresy. IOMMU podporují virtualizaci paměti a její ochranu (např. před DMA útoky).

## Poznámka Anki 1696254839840

Karty Anki: 1696254839840
GUID: soPiPA!#ot; štítky: bi-hwb::p02.

### Otázka (Front)

Popište kryptografický hardware? Jak je lze realizovat?

### Odpověď (Back)

Kryptografický hardware je hardware, který je specializován na provádění kryptografických operací, které jsou zpravidla náročné a mohou zatěžovat procesor stroje. Poskytuje podporu pro symetrické šifry (posuvy, S-Box, operace v \(GF(2^8)\) apod.) a asymetrické šifry (operace v \(GF(p)\), operace nad eliptickými křivkami, modulární umocňování apod.). Realizovat je lze následujícími způsoby:

- speciální vykonávací jednotka unitř CPU,
- dedikované kryptografické jádro CPU,
- kryptografický koprocesor připojený přes sběrnici.

## Poznámka Anki 1696271210111

Karty Anki: 1696271210111
GUID: y){Xf96ldy; štítky: bi-hwb::p02.

### Otázka (Front)

Popište šifrování paměti.

### Odpověď (Back)

Protože jsou externí paměti náchylné na cold boot útoky, používá se šifrování obsahu paměti. Toto šifrování je zcela transparentní pro uživatele a procesor. Existují následující realizace:

- AMD Memory Encryption,

- Intel Software Guard Extensions,

- trusted enclaves - aplikace mohou obsahovat části, které jsou spouštěny v chráněné paměti.

## Poznámka Anki 1696271643857

Karty Anki: 1696271643857
GUID: bZByzi-|G!; štítky: bi-hwb::p02.

### Otázka (Front)

Popište Intel Management Engine a AMD Platform Security Processor.

### Odpověď (Back)

Intel Management Engine a AMD Platform Security Processor jsou autonomní mikrokontrolery zahrnuté do čipové sady většiny současných procesorů. Dle jejich výrobců poskytují podporu TPM, zajištění bezpečného prostředí a procesu bootu systému. Jejich přesné funkce nejsou dokumentovány a jejich kód je utajen.

## Poznámka Anki 1700642724273

Karty Anki: 1700642724273
GUID: d1lG7zC0$e; štítky: bi-hwb::p02.

### Otázka (Front)

Jakými způsoby lze realizovat Trusted Platform Module (TPM)?

### Odpověď (Back)

Trusted Platform Module (TPM) lze realizovat následujícími způsoby:

- diskrétní čip,
- integrovaný v čipsetu,
- integrovaný ve firmware,
- softwarově emulovaný.

