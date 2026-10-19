# BI-UKB – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-ukb/BI-UKB.apkg; APKG SHA-256 fb963722a1039499908d9a37b947a0f774fd26b951b463a4c2349468681bec67. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8d39d92d14a3cb34c1c177ef00602d3767837744484a3254d799cb18f10b34a9.
Původní balíčky: BI-UKB
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1666765833210

Karty Anki: 1666765833210
GUID: Dc`QT8D.{}; štítky: bi-ib::11 bi-ib::21 bi-ukb::p05.

### Otázka (Front)

Rozdělte útoky na síťové vrstvě.

### Odpověď (Back)

Útoky na síťové vrstvě dělíme do dvou kategorií:

- **pasivní **- útočník negeneruje síťový provoz (eavesdropping, analýza provozu),

- **aktivní **- útočník generuje síťový provoz (replay, DoS).

## Poznámka Anki 1666767116442

Karty Anki: 1666767116442
GUID: Gd|2K4~Jo&; štítky: bi-ukb::p05.

Metadata původního zdroje pro kartu 1666767116442: v původním balíčku pozastavená karta.

### Otázka (Front)

Co jsou to služby bezpečnosti?

### Odpověď (Back)

Služby bezpečnosti jsou definované postupy zvyšující bezpečnost IS a realizující ochranu proti útokům na tyto systémy. Jsou zajištěny prostřednictvím bezpečnostních mechanizmů.

## Poznámka Anki 1666767205238

Karty Anki: 1666767205238
GUID: x8Q>77&6i{; štítky: bi-ukb::p05.

Metadata původního zdroje pro kartu 1666767205238: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište model perimetru.

### Odpověď (Back)

- všechna zařízení mimo perimetr jsou nedůvěryhodná, zařízení uvnitř jsou důvěryhodná
- chybí inspekce provozu uvnitř perimetru
- spoléhá na jednotlivé izolované kontrolní body (single point of failure)

## Poznámka Anki 1666769409421

Karty Anki: 1666769409421
GUID: P*Hnl#bG(<; štítky: bi-ukb::p05.

Metadata původního zdroje pro kartu 1666769409421: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište různé přístupy k Zero Trust.

### Odpověď (Back)

- **rozšířené řízení identit** - tvorba politik se odvíjí od definovaných identit

- **mikro segmentace **- spoléhá na síťové segmenty seskupující skupiny zdrojů se stejnými požadavky na bezpečnost

- **softwarově definovaný perimetr** - souvislost se softwarově definovanými sítěmi

## Poznámka Anki 1666770335877

Karty Anki: 1666770335877
GUID: gK,MqDL;nm; štítky: bi-ib::21 bi-ukb::p05.

Metadata původního zdroje pro kartu 1666770335877: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké existují zdroje dat sloužící k bezpečnostnímu monitoringu sítí?

### Odpověď (Back)

- **sběr paketů **(Packet Capture) - zachytí přesnou kopii paketu tak, jak byl přenesen v stíti

- **NetFlows **- metadata paketů se společnými vlastnostmi

- **logy** - logy ze routerů, switchů, firewallů, IPS, IDS a podobně

## Poznámka Anki 1666770651434

Karty Anki: 1666770651434
GUID: qsrAI4?Woh; štítky: bi-ukb::p05.

Metadata původního zdroje pro kartu 1666770651434: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakým způsobem může probíhat paketová analýza?

### Odpověď (Back)

- **hledání vzorů **(Pattern Matching)

- **parsování specifických příznaků **(Parsing Protocol Field)

- **filtrování paketů** (Packet Filtering)

## Poznámka Anki 1666772124910

Karty Anki: 1666772124910
GUID: qC/k3Rf,|6; štítky: bi-ukb::p05.

### Otázka (Front)

Jaké prostředky se používají k zabezpečení emailu?

### Odpověď (Back)

- **Sender Permitted From **(SPF) - na úrovni DNS záznamu je dán seznam serverů, které mohou posílat emaily jménem dané domény
- **Domain Keys Identified Mail **(DKIM) - emailový server kryptograficky podepíše zprávu a odpovádající klíč je pak dostupný na úrovni DNS

- **Domain-based Message Authentication, Reporting and Conformance **(DMARC) - protokol obsluhující SPF a DKIM

