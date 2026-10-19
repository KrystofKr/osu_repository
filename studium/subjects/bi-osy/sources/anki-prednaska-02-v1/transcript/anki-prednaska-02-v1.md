# BI-OSY – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-osy/BI-OSY.apkg; APKG SHA-256 e601d54cae58e1923ab743a64796ef89ec49f6bcd52ac062288890242af207fc. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b95b42cacacaa5de70f8162d09b00582086c2fd5b59f3a299e3fc9531a688ab6.
Původní balíčky: BI-OSY
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678181086913

Karty Anki: 1678181086913
GUID: y+]u_]iN9N; štítky: bi-ib::03 bi-osy::p02.

### Otázka (Front)

Co je to proces?

### Odpověď (Back)

Proces je instance spuštěného programu či aplikace, v rámci které jsou alokovány prostředky jako paměť, vlákna nebo soubory. Proces má vždy jedno implicitní hlavní vlákno a vlákna v rámci procesu sdílí většinu prostředků.

## Poznámka Anki 1678181169773

Karty Anki: 1678181169773
GUID: eaoaF=m24F; štítky: bi-ib::03 bi-osy::p02.

### Otázka (Front)

Co je to vlákno?

### Odpověď (Back)

Jde o výpočetní entitu (proud instrukcí), které je přidělováno jádro CPU.

## Poznámka Anki 1678181326340

Karty Anki: 1678181326341
GUID: HcSEnqb2ws; štítky: bi-ib::03 bi-osy::p02 bi-spol::17.

Metadata původního zdroje pro kartu 1678181326341: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakými způsoby můžeme vytvořit nový proces?

### Odpověď (Back)

Nový proces můžeme vytvářet jako:

- **kopii původního procesu** (např. voláním \(\mathtt{fork}\)),

- **úplně nový proces** (např. voláním \(\mathtt{fork}\) a následným \(\mathtt{execve}\)).

## Poznámka Anki 1678181419256

Karty Anki: 1678181419256
GUID: vv}_>$=[z,; štítky: bi-ib::03 bi-osy::p02.

Metadata původního zdroje pro kartu 1678181419256: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou návratové hodnoty funkce \(\mathtt{fork}\)?

### Odpověď (Back)

Funkce \(\mathtt{fork}\) vrací:

- v **rodičovském procesu** číslo potomka (případně \(\mathtt{\text-1}\) když dojde k chybě),
- v **potomkovi** vždy hodnotu \(\mathtt 0\).

## Poznámka Anki 1678181750577

Karty Anki: 1678181750577
GUID: caH{V1#WuV; štítky: bi-osy::p02 bi-spol::17.

### Otázka (Front)

Vyjmenujte a popište stavy vlákna.

### Odpověď (Back)

Vlákno se může nacházet v následujících stavech:

- **idle** - vlákno teprve vzniklo,

- **ready** - vlákno čeká na přidělení jádra CPU,

- **running** - vlákno je právě zpracováváno jádrem CPU,

- **blocked** - vlákno čeká na událost (signál, dokončení I/O operace),

- **zombie** - vlákno je v procesu ukončení,

- **free** - vlákno bylo kompletně zrušeno.

## Poznámka Anki 1678181825181

Karty Anki: 1678181825181
GUID: PnVzOQ(_lk; štítky: bi-osy::p02 bi-spol::17.

### Otázka (Front)

Co je to časově závislá chyba?

### Odpověď (Back)

Časově závislá chyba je situace, kdy několik vláken používá sdílené prostředky, a výsledek deterministického algoritmu je závislý na rychlosti jednotlivých vláken, které tyto prostředky využívají.

## Poznámka Anki 1678181842492

Karty Anki: 1678181842492
GUID: Ctjr)?=~)9; štítky: bi-osy::p02 bi-spol::17.

### Otázka (Front)

Co je to kritická sekce?

### Odpověď (Back)

Kritická sekce je část programu, kde vlákna používají sdílené prostředky.

