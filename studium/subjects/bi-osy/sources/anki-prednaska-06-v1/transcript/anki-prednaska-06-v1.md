# BI-OSY – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-osy/BI-OSY.apkg; APKG SHA-256 e601d54cae58e1923ab743a64796ef89ec49f6bcd52ac062288890242af207fc. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b95b42cacacaa5de70f8162d09b00582086c2fd5b59f3a299e3fc9531a688ab6.
Původní balíčky: BI-OSY
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1680093668967

Karty Anki: 1680093668967
GUID: tlfQFxvRf9; štítky: bi-osy::p06 bi-spol::17.

### Otázka (Front)

Co je to tabulka procesů, process control block a thread control block?

### Odpověď (Back)

Tabulka procesů je struktura (nejčastěji zřetězený seznam), ve které si OS udržuje informace o procesech. Process control block je potom jedna položka této tabulky, která obsahuje všechny nezbytné informace pro jeden proces. Thread control block je obdoba process control blocku ale pro vlákna, nicméně některé OS (jako Linux) používají stejnou strukturu pro vlákna i procesy.

## Poznámka Anki 1680094888258

Karty Anki: 1680094888258
GUID: B*)iW`ltqO; štítky: bi-osy::p06 bi-spol::17.

### Otázka (Front)

Popište způsoby implementace vláken.

### Odpověď (Back)

Rozlišujeme následující způsoby implementace vláken:

- user-level vlákna (model many-to-one),

- kernel-level vlákna (model one-to-one),

- hybridní vlákna (model many-to-many).

## Poznámka Anki 1680095106378

Karty Anki: 1680095106378
GUID: rxvHe$V2=r; štítky: bi-osy::p06 bi-spol::17.

Metadata původního zdroje pro kartu 1680095106378: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište user-level implementaci vláken (model many-to-one).

### Odpověď (Back)

User-level implementace vláken (model many-to-one) stojí na kooperativním plánování a run-time systému v podobě user-level knihovny. Její výhodou je velmi rychlá správa vláken. Nevýhodou však je, že se vícero user-level vláken mapuje na jedno kernel-level vlákno, z čehož vyplývá, že blokující volání jednoho user-level vlákna zablokuje i všechna ostatní.

## Poznámka Anki 1680095231766

Karty Anki: 1680095231766
GUID: xVa%>DZ7L+; štítky: bi-osy::p06 bi-spol::17.

Metadata původního zdroje pro kartu 1680095231766: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište kernel-level implementaci vláken (model one-to-one).

### Odpověď (Back)

Kernel-level implementace vláken (model one-to-one) je dnes nejpoužívanější model implementace vláken, při kterém se každé user-level vlákno mapuje na vlastní kernel-level vlákno. Jeho výhodou je, že blokující volání ovlivňuje pouze vlákno, které jej provádí. Nevýhodou však je pomalejší správa vláken kvůli přepínání z user mode do kernel mode.

## Poznámka Anki 1680096387193

Karty Anki: 1680096387193
GUID: lw|1L:c8w%; štítky: bi-osy::p06 bi-spol::17.

Metadata původního zdroje pro kartu 1680096387193: v původním balíčku pozastavená karta.

### Otázka (Front)

V jakých momentech dochází k plánování vláken?

### Odpověď (Back)

K plánování dochází když

- **běžící vlákno se vzdá jádra** - dokončí výpočet, dobrovolně se vzdá jádra nebo provádí blokující volání,
- **nastane nějaká událost** - přerušení od I/O zařízení nebo časovače.

## Poznámka Anki 1680096457547

Karty Anki: 1680096457547
GUID: lrMUMHwvJ,; štítky: bi-osy::p06 bi-spol::17.

### Otázka (Front)

Jaké existují strategie plánování vláken?

### Odpověď (Back)

Rozlišujeme:

- **plánování s odnímáním** - OS přidělí vláknu jádro CPU pouze na určitou dobu a poté mu ho odebere,

- **kooperativní plánování** - OS přidělí vláknu jádro CPU a to ho používá, dokud ho samo neuvolní.

## Poznámka Anki 1680098323480

Karty Anki: 1680098323480
GUID: Em$oaHH!=x; štítky: bi-osy::p06 bi-spol::17.

Metadata původního zdroje pro kartu 1680098323480: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište round-robin plánování vláken s prioritou.

### Odpověď (Back)

Round-robin plánování je typ plánování s odnímáním. Vlákna ve stavu ready čekají v několika frontách (FIFO) podle jejich priority. Volné jádro CPU je přiděleno vláknu s nejvyšší prioritou, které je první ve frontě. Po opuštění jádra je vlákno řazeno na konec příslušné fronty. Pokud vlákno provede blokující volání, je zařazeno do speciální fronty, kde čeká na příslušnou událost. Prioritu a časové kvantum můžeme dynamicky měnit.

 [Obrázek: paste-ad551e2c164c00ea1132fa4ee8d6578384cdc4b5.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1680099068211

Karty Anki: 1680099068211
GUID: AW{#vFLdEm; štítky: bi-osy::p06 bi-spol::17.

Metadata původního zdroje pro kartu 1680099068211: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakým způsobem můžeme měnit prioritu a časové kvantum u round-robin plánování?

### Odpověď (Back)

Strategie mohou být následující:

- **priorita se zvýší a časové kvantum se sníží** - to se děje v případech, kdy

- vlákno nevyužilo celé kvantum (I/O orientované vlákno),
- vlákno dlouho čeká na CPU (hrozí hladovění);

- **priorita se sníží a časové kvantum se zvýší** - to se děje pokud vlákno využilo celé kvantum (CPU orientované vlákno).

## Poznámka Anki 1680099583969

Karty Anki: 1680099583969
GUID: yQiYtggq_(; štítky: bi-osy::p06 bi-spol::17.

Metadata původního zdroje pro kartu 1680099583969: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište first-come-first-served plánování vláken.

### Odpověď (Back)

First-come-first-served je typ kooperativního plánování. Používá totožný princip jako round-robin plánování.

## Poznámka Anki 1716659915355

Karty Anki: 1716659915355
GUID: zNFRF@$O3$; štítky: bi-ib::03 bi-osy::p06 bi-spol::17.

Metadata původního zdroje pro kartu 1716659915355: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište obsah process control block (PCB).

### Odpověď (Back)

Process control block (TCB) obsahuje:

- **informace pro identifikaci procesu **- číslo procesu (PID), číslo rodičovského procesu (PPID);

- **informace související s identitou procesu a bezpečností** - vlastník procesu (UID, GID), přístupová oprávnění;
- **informace o alokovaných prostředcích** - paměť, soubory.

## Poznámka Anki 1716660011452

Karty Anki: 1716660011453
GUID: IFz$8Yj4i-; štítky: bi-ib::03 bi-osy::p06 bi-spol::17.

Metadata původního zdroje pro kartu 1716660011453: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište obsah thread control block (TCB).

### Odpověď (Back)

Thread control block (TCB) obsahuje:

- **informace pro identifikaci vlákna** - číslo vlákna (TID);
- **informace pro přepínání kontextu **- ukazatel na zásobník, hodnoty registrů procesoru;

- **informace pro plánování vláken** - priorita a stav vlákna.

## Poznámka Anki 1716660874608

Karty Anki: 1716660874608
GUID: I]3[I7:1Ol; štítky: bi-osy::p06 bi-spol::17.

Metadata původního zdroje pro kartu 1716660874608: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište hybridní implementaci vláken (model many-to-many).

### Odpověď (Back)

Hybridní implementace vláken (model many-to-many) je model implementace vláken, který kombinuje principy user-level a kernel-level implementací. Vyznačuje se tím, že \(m\) user-level vláken se mapuje na \(n\) kernel-level vláken.

