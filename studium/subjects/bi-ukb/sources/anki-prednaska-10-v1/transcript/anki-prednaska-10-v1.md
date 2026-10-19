# BI-UKB – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-ukb/BI-UKB.apkg; APKG SHA-256 fb963722a1039499908d9a37b947a0f774fd26b951b463a4c2349468681bec67. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8d39d92d14a3cb34c1c177ef00602d3767837744484a3254d799cb18f10b34a9.
Původní balíčky: BI-UKB
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1669817289168

Karty Anki: 1669817289168
GUID: i*PS@YDZ`(; štítky: bi-ib::07 bi-ukb::p10.

Metadata původního zdroje pro kartu 1669817289168: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to bezpečný software?

### Odpověď (Back)

Bezpečný software splňuje specifikované nebo implikované bezpečnostní cíle (obvykle důvěrnost, integrita, dostupnost). Je závislý na modelu hrozeb.

## Poznámka Anki 1669817797709

Karty Anki: 1669817797709
GUID: KpV_AgKp[+; štítky: bi-ib::08 bi-ukb::p10.

Metadata původního zdroje pro kartu 1669817797709: původní příznak autora 5; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Memory Management Vulnerabilities.

### Odpověď (Back)

- setkáváme se s nimi hlavně v programovacích jazycích, kde správa paměti spadá na programátora (C++, C)
- rozlišujeme:

- **spatial **zranitelnosti - buffer overflow
- **temporal **zranitelnosti - program přistupuje do paměti, která sice byla alokována, ale už doško k jejímu uvolnění

- **příklady útoků**: vstup exploitující zranitelnost, code corruption, control flow hijack

- **prevence**: validace vstupů, bounds checking, memory-safe jazyk

## Poznámka Anki 1669817966859

Karty Anki: 1669817966859
GUID: d{cKB_H+=@; štítky: bi-ib::10 bi-ib::16 bi-ukb::p10.

### Otázka (Front)

Popište structured output generation vulnerabilities.

### Odpověď (Back)

Structured output generation vulnerabilities je skupina zranitelností, která se týká zejména aplikací produkujících strukturovaný výstup, který je následně používán jako vstup pro další aplikaci. Mezi příklady těchto zranitelností patří:

- SQL injection,
- command injection,

- cross-site scripting (XSS).

Předcházet jim lze následujícími metodami:

- validace vstupů,
- použití předdefinovaných struktur nebo šablon pro výstup.

## Poznámka Anki 1669818875735

Karty Anki: 1669818875735
GUID: gL0T6#-Yz); štítky: bi-ukb::p10.

### Otázka (Front)

Popište Race Condition Vulnerabilities.

### Odpověď (Back)

- vznikají když jsou porušeny předpoklady aplikací přistupujících ke sdíleným zdrojům (pamět, soubory, databáze, ...)
- **Time of Check **vs. **Time of Use** (TOCTOU) - mezi kontrolou stavu objektu a samotným přístupem může dojít k jeho nečekané změně

- **příklady útoků**: souběh na filesystému, souběh vyhodnocovaní stavu relace ve webových aplikacích

- **prevence**: thread-safe design, mutex, atomické funkce, serializace

## Poznámka Anki 1669819090826

Karty Anki: 1669819090827
GUID: c<T(|1f13O; štítky: bi-ukb::p10.

### Otázka (Front)

Popište API Vulnerabilities.

### Odpověď (Back)

- vznikají když API není připravené na porušení specifikace použítí
- **příklady útoků**: chyby autentizace přístupů, chyby autorizace požadavků, přebytečná data ve výstupu, nedostatek zdrojů

- **prevence**: autentizace přístupů a autorizace požadavků, filtrování výstupu, rate limiting

## Poznámka Anki 1669820431605

Karty Anki: 1669820431605
GUID: j@pR!,|/@^; štítky: bi-ukb::p10.

Metadata původního zdroje pro kartu 1669820431605: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Side-Channel Vulnerabilities.

### Odpověď (Back)

- zneužívají toho, že digitální obvody mají spotřebu, vyzařují elektromagnetické záření a operace provádějí po určitou dobu
- **příklady útoků**: časový, cache a odběrový kanál

- **prevence**: hiding, masking, shielding, promíchání operací, vkladání prázdných operací, obfuskace

## Poznámka Anki 1669820573433

Karty Anki: 1669820573434
GUID: C0:61.ak4R; štítky: bi-ukb::p10.

Metadata původního zdroje pro kartu 1669820573434: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište kanárka na zásobníku (stack canary) a jeho implementace. Jak lze vypnout?

### Odpověď (Back)

Kanárek na zásobníku (stack canary) je obranný mechanismus proti buffer overflow. Funguje tak, že při vstupu do funkce je na zásobník vloženo náhodné slovo (kanárek) takovým způsobem, aby útočník nemohl přepsat návratovou adresu funkce bez jeho přepsání. V případě, že je detekována změna kanárka, je program ukončen. Mezi implementace kanárka na zásobníku patří:

- StackGuard,

- Stack Smashing Protector nebo někdy také ProPolice (GCC),

- Buffer Security Check (MSVC).

Na Linux je programy potřeba linkovat se speciálními přepínači, na Windows je ochrana automatická a naopak je potřeba použít speciální přepínače pro její vypnutí.

## Poznámka Anki 1669821089077

Karty Anki: 1669821089077
GUID: gnMg6H>(2y; štítky: bi-ukb::p10.

Metadata původního zdroje pro kartu 1669821089077: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

K čemu slouží segmenty s příznakem NX (non-execute)?

### Odpověď (Back)

Zabraňují zapsání spustitelného kódu mimo určené paměťové regiony.

## Poznámka Anki 1669821228604

Karty Anki: 1669821228605
GUID: h#kRn{_Cv=; štítky: bi-ib::08 bi-ukb::p10.

### Otázka (Front)

Popište control-flow integrity (CFI).

### Odpověď (Back)

Control-flow integrity (CFI) je bezpečnostní mechanismus, který se snaží předejít útokům, kdy útočník ovlivní tok programu (control-flow hijacking). Existují různé implementace, ale obecně je před každým nepřímým skokem prováděna kontrola cílové adresy.

## Poznámka Anki 1669822434216

Karty Anki: 1669822434217
GUID: pvL!!=YN%T; štítky: bi-ukb::p10.

Metadata původního zdroje pro kartu 1669822434217: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to Common Vulnerabilities and Exposures (CVE)?

### Odpověď (Back)

Jde o databázi, která obsahuje veřejně známé zranitelnosti. Spravuje ji organizace MITRE.

## Poznámka Anki 1669824117145

Karty Anki: 1669824117145
GUID: p|^uTUFS^e; štítky: bi-ukb::p10.

Metadata původního zdroje pro kartu 1669824117145: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké existují metody a přístupy k zajištění vývoje bezpečného software?

### Odpověď (Back)

Microsoft Security Development Lifecycle, Touchpoints a SAFECode

