# BI-ADU – Přednáška 11

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-adu/BI-ADU.apkg; APKG SHA-256 82e24d30673cd0e7a3a5aa4e190d583b7bbdacb9961363822343a47e911816b0. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e4dcf13ba19280a57f78abe30db474a9b8da6ee148ccef4aa2c510acfc892435.
Původní balíčky: BI-ADU
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1683098509487

Karty Anki: 1683098509488
GUID: z_o/.H3a}j; štítky: bi-adu::p11.

Metadata původního zdroje pro kartu 1683098509488: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to virtualizace? Uveďte příklady.

### Odpověď (Back)

Virtualizace je proces, při kterém se jeden fyzický prostředek (hostitel nebo host) se transformuje na několik virtuálních prostředků (host nebo guest). Mezi příklady virtualizace patří:

- **spooling **- tiskárny, faxy;
- **síťové karty** - virtuální interface;
- **disky **- partitions, RAID.

## Poznámka Anki 1683098951265

Karty Anki: 1683098951265
GUID: r>!:p7JC3f; štítky: bi-adu::p11.

Metadata původního zdroje pro kartu 1683098951265: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakým způsobem lze přidělovat prostředky virtualizovaným systémům?

### Odpověď (Back)

Prostředky lze přidělovat:

- **staticky** - virtualizované systémy mají zdroje přiděleny napevno,

- **dynamicky** - přidělené zdroje se mohou měnit na základě požadavků systému.

## Poznámka Anki 1683099214855

Karty Anki: 1683099214855
GUID: zSv]>rn!KK; štítky: bi-adu::p11 bi-ib::25.

### Otázka (Front)

Jaké existují úrovně virtualizace systému?

### Odpověď (Back)

Existují následující úrovně virtualizace:

- **hard partitioning **- dělení na úrovni hardware (Sun Dynamic System Domains),
- **emulation **(full virtualization) - virtuální počítač plně simuluje hardware (VirtualBox),
- **paravirtualization **- domény na úrovni firmware (Sun Logical Domains),
- **OS-level virtualization **- sdílené jádro OS (Solaris zóny, kontejnery),
- **application virtualization **- aplikace běží ve virtuálním prostředí oddělujícím ji od hardware a OS (Java Virtual Machine).

## Poznámka Anki 1683099854733

Karty Anki: 1683099854734
GUID: PoTV*UOyko; štítky: bi-adu::p11.

Metadata původního zdroje pro kartu 1683099854734: v původním balíčku pozastavená karta.

### Otázka (Front)

Uveďte možné využití virtualizace.

### Odpověď (Back)

Mezi možné využití virtualizace patří:

- sdružení různých serverů na jeden hardware,
- sdružení systémů s nízkými nároky na jeden hardware,
- izolace a bezpečnost aplikací,
- provoz starších aplikací na novějším hardware.

## Poznámka Anki 1683100105026

Karty Anki: 1683100105027
GUID: e@C~^I7t6t; štítky: bi-adu::p11.

Metadata původního zdroje pro kartu 1683100105027: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Solaris zóny.

### Odpověď (Back)

Solaris zóny spadají pod virtualizaci na úrovni OS, tedy používají sdílené jádro a jsou odděleny na úrovni filesystémů a procesů. Implicitně OS osbsahuje jednu **globální zónu** a v ní libovolný počet **neglobálních zón **(jednoúrovňová struktura).

## Poznámka Anki 1683100240171

Karty Anki: 1683100240171
GUID: wO?%vub:eA; štítky: bi-adu::p11.

Metadata původního zdroje pro kartu 1683100240171: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký je rozdíl mezi globální a neglobální Solaris zónou.

### Odpověď (Back)

V **globální zóně** běží daemoni, kteří řídí neglobální zóny, tedy chyba v této zóně může způsobit havárii neglobálních zón. Proto by se globální zóna měla používat pouze pro správu neglobálních zón. **Neglobální zóny** běží v globální zóně, nemohou se navzájem ovlivňovat a mají různé správce.

## Poznámka Anki 1683100286080

Karty Anki: 1683100286080
GUID: y_o,IX:p8e; štítky: bi-adu::p11.

Metadata původního zdroje pro kartu 1683100286080: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký je rozdíl mezi nativní a branded Solaris zónou.

### Odpověď (Back)

**Nativní zóna** používá stejnou verzi OS jako hostitel (globální zóna), kdežto **branded zóna** používá jinou (starší).

## Poznámka Anki 1683102633900

Karty Anki: 1683102633900
GUID: n~NZ-:J)6!; štítky: bi-adu::p11.

Metadata původního zdroje pro kartu 1683102633900: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké daemony použíavají Solaris zóny a jaké jsou jejich funkce?

### Odpověď (Back)

Solaris zóny používají dva daemony - \(\mathtt{zsched}\) a \(\mathtt{zoneadmd}\). \(\mathtt{zsched}\) je potomkem procesu \(\mathtt{init}\) globální zóny a otcem lokálního procesu \(\mathtt{init}\) každé zóny. \(\mathtt{zoneadmd}\) běží pro každou zónu zvlášť, spouští \(\mathtt{zsched}\), řídí boot a shutdown zóny, přiděluje prostředky a provádí akce zadané příkazem \(\mathtt{zoneadm}\).

## Poznámka Anki 1683102697094

Karty Anki: 1683102697095
GUID: v|2j>|W?e8; štítky: bi-adu::p11.

Metadata původního zdroje pro kartu 1683102697095: v původním balíčku pozastavená karta.

### Otázka (Front)

Co jsou to shares u Solaris zón?

### Odpověď (Back)

Shares umožňují každé zóně přidělit share (podíl) výkonu. V případě přetížení systému bude zónám přidělen právě tento podíl prostředků systému.

## Poznámka Anki 1683102835289

Karty Anki: 1683102835289
GUID: M8zX1@B-8#; štítky: bi-adu::p11.

Metadata původního zdroje pro kartu 1683102835289: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké existují modely Solaris zón?

### Odpověď (Back)

Existují následující modely zón:

- **sparse** - sdílení některých systémových částí filesystému jako read-only loopback filesystém (implicitně \(\mathtt{/usr}\), \(\mathtt{/lib}\), \(\mathtt{/sbin}\) a \(\mathtt{/platform}\));

- **full **- zóna má vlastní kopii celé systémové části filesystému;

- **custom** - kombinace sparse a full, definuje administrátor.

## Poznámka Anki 1683102977320

Karty Anki: 1683102977320
GUID: Q{1i|OJ4OQ; štítky: bi-adu::p11.

Metadata původního zdroje pro kartu 1683102977320: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to kontejner? Uveďte příklad kontejnerové virtualizační platformy.

### Odpověď (Back)

Kontejner je zapouzdření aplikace do prostředí. Jde v podstatě o spojení zóny, aplikace, konfigurace zóny a konfigurace aplikace do jednoho celku. Takto vytvořený celek je potom přenositelný a umí běžet bez ohledu na konfiguraci hostitelského systému. Příkladem je Docker.

