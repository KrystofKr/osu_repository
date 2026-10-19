# BI-UKB – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-ukb/BI-UKB.apkg; APKG SHA-256 fb963722a1039499908d9a37b947a0f774fd26b951b463a4c2349468681bec67. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8d39d92d14a3cb34c1c177ef00602d3767837744484a3254d799cb18f10b34a9.
Původní balíčky: BI-UKB
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1667377054902

Karty Anki: 1667377054902
GUID: Q94(jsgG+F; štítky: bi-ib::25 bi-ukb::p06.

### Otázka (Front)

Popište secure boot.

### Odpověď (Back)

Secure boot je bezpečnostní mechanismus využívající Trusted Platform Module (TPM), který zajišťuje, že je při procesu bootování systému načten pouze důvěryhodný podepsaný software.

## Poznámka Anki 1667377148431

Karty Anki: 1667377148431
GUID: rJ#Z%+qcOu; štítky: bi-ib::25 bi-ukb::p06.

### Otázka (Front)

Popište Trusted Platform Module (TPM).

### Odpověď (Back)

Trusted Platform Module (TPM) je standard bezpečného kryptoprocesoru, který umožňuje využívání dalších bezpečnostních mechanik (např. Secure Boot, šifrování disku, key wrapping nebo key sealing).

## Poznámka Anki 1667377260130

Karty Anki: 1667377260130
GUID: uom]{|D;7T; štítky: bi-ukb::p06.

Metadata původního zdroje pro kartu 1667377260130: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište přetečení bufferu (buffer overflow). Kde k němu může docházet?

### Odpověď (Back)

Přetečení bufferu (buffer overflow) je typ zranitelnosti, kdy dojde k přepsání obsahu paměti za koncem bufferu. Typicky vzniká jako důsledek neodstatečného ošetření vstupu, které umožní, aby do bufferu bylo zapsáno více dat, než je jeho kapacita. K přetečení bufferu může dojít na:

- **zásobníku** - zneužívá toho, že na zásobníku jsou uloženy jak lokální proměnné, argumenty funkcí a uložené hodnoty registrů, tak návratové adresy;

- **haldě** - zneužívá toho, že na haldě jsou uložena jak uživatelská data, tak alokační struktury správce paměti (na jeho implementaci je zneužití přetečení na haldě silně závislé).

## Poznámka Anki 1667377862936

Karty Anki: 1667377862937
GUID: B%LAOk4*7D; štítky: bi-ukb::p06.

### Otázka (Front)

Co je to OS Hardening?

### Odpověď (Back)

Hardening je bezpečné nastavení operačních systémů tak, aby se snížil Attack Surface (povrchová zranitelnost).

## Poznámka Anki 1667380484736

Karty Anki: 1667380484736
GUID: P}K683knn); štítky: bi-ukb::p06.

Metadata původního zdroje pro kartu 1667380484736: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to Container Escape?

### Odpověď (Back)

Container Escape je technika, kdy se útočník snaží uniknout z kontejneru dané aplikace.

## Poznámka Anki 1667396914951

Karty Anki: 1667396914954
GUID: MBSWGWOXVo; štítky: bi-ukb::p06.

### Otázka (Front)

Co je to firmware?

### Odpověď (Back)

Firmware je program pro provádění základních nízkoúrovňových operací. Jde o integrační vrstvu mezi hardware a software.

## Poznámka Anki 1667397013858

Karty Anki: 1667397013858
GUID: c}M@.Kap0%; štítky: bi-ukb::p06.

Metadata původního zdroje pro kartu 1667397013858: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to Privilege Escalation?

### Odpověď (Back)

Je to typ útoku, kdy útočník zneužitím nějaké zranitelnosti získá vyšší oprávnění.

## Poznámka Anki 1667397219889

Karty Anki: 1667397219890
GUID: E9%omkPI,{; štítky: bi-ukb::p06.

Metadata původního zdroje pro kartu 1667397219890: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakými bezpečnostními prvky disponuje Windows?

### Odpověď (Back)

- **User Account Control **(UAC) - aplikace sama nemůže eskalovat oprávnění

- **Smart App Control** - kontrola spouštěných aplikací

- **Virtualization-based Security** - spouštění aplikací v separátních virtualizovaných prostředích

- **Kernel DMA Protection** - ochrana před přímým přístupem do paměti přes PCIe porty

## Poznámka Anki 1667397367674

Karty Anki: 1667397367674
GUID: KzKuOpUb#W; štítky: bi-ukb::p06.

Metadata původního zdroje pro kartu 1667397367674: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak lze zvýšit bezpečnost Linuxu?

### Odpověď (Back)

- používat účet s minimálními oprávěními (Least Privilege) a pro privilegované operace používat **sudo**

- **SELinux** (Secure Enhanced Linux) - lze nastavovat bezpečnostní pravidla s vysokou granularitou
- **chroot** - umožňuje posunout kořen souborového systému

- **Fail2Ban** - v případě opakovaných pokusů o přihlášení dojde k zablokování síťového prostupu

## Poznámka Anki 1667397617771

Karty Anki: 1667397617771
GUID: Pi*647S]hz; štítky: bi-ukb::p06.

Metadata původního zdroje pro kartu 1667397617771: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký je rozdíl mezi hardwarovým hypervisorem, softwarovým hypervisorem a kontejnerem?

### Odpověď (Back)

- **hardwarový hypervisor **- hypervisor je instalován přímo na hardware

- **softwarový hypervisor** - hypervisor je instalován na operačním systému hosta

- **kontejner** - je instalován na operačním systému hosta a slouží k emulaci OS pro potřebu konkrétní aplikace

## Poznámka Anki 1667397734800

Karty Anki: 1667397734800
GUID: L%ErK(w<D1; štítky: bi-ukb::p06.

Metadata původního zdroje pro kartu 1667397734800: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakým způsobem jsou kontejnery podporovány v Linuxu?

### Odpověď (Back)

- **namespaces** - funkce kernelu, která umožňuje spouštět jednotlivé procesy odděleně a přiřazovat jim prostředky

- **cgroups** - funkce kernelu, která umožňuje řízení hardwarových zdrojů pro jednotlivé procesy

