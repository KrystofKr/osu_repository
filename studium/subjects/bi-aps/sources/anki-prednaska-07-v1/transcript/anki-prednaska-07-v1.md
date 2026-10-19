# BI-APS – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1667229929142

Karty Anki: 1667229929142
GUID: k2]3oY>Lrn; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

Metadata původního zdroje pro kartu 1667229929142: v původním balíčku pozastavená karta.

### Otázka (Front)

S jakými problémy se můžeme setkat u hlavní paměti bez virtualizace?

### Odpověď (Back)

- **nedostatek paměti **- velikost instalované paměti nemusí být dostačující pro spouštění dalších procesů

- **fragmentace **- při ukončování procesů vznikají v paměťovém prostoru volné oblasti různých velikostí

- **dynamická alokace** - nelze měnit rozsah adres přidelený běžícím procesům

- **bezpečnost** - jak zajistit, aby procesy nemohly vzájemně číst obsah hlavní paměti

## Poznámka Anki 1667230066514

Karty Anki: 1667230066514
GUID: m{UETJvVew; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

### Otázka (Front)

Popište virtualizaci hlavní paměti stránkováním.

### Odpověď (Back)

Každému procesu je přidělen virtuální adresní prostor (VAS), v rámci kterého používá proces virtuální adresy. VAS je dělen na stejně velké **stránky** (pages). Hlavní paměť je dělena na stejně velké **stránkové rámce** (frames), přičemž velikost stránky a rámce je také stejná. Běžící procesy pak do hlavní paměti umisťují pouze aktuálně využívané stránky svého VAS (tzv. working set) a zbytek stránek je odložen na disku.

## Poznámka Anki 1667235696425

Karty Anki: 1667235696425
GUID: g$h[*@cWp]; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

Metadata původního zdroje pro kartu 1667235696425: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to demand paging (lazy loading)?

### Odpověď (Back)

Demand paging je strategie nahrávání stránek, při které je stránka nahrána do hlavní paměti až tehdy, když je k ní přistupováno. Toto mapování zajišťuje OS.

## Poznámka Anki 1667235878687

Karty Anki: 1667235878687
GUID: roRopBisJ/; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

### Otázka (Front)

Jaké existují struktury pro překlad a mapování virtuálních adres?

### Odpověď (Back)

Moderní operační systémy využívají jednu z následujících struktur:

- **konvenční (víceúrovňová) stránkovací tabulka** - každý proces má vlastní stránkovací tabulku, resp. strom stránkovacích tabulek, jejíž počáteční adresa je uložena v \(\mathtt{mm\_struct}\) v ukazateli \(\mathtt{*pgd}\);

- **inverzní stránkovací tabulka** - všechny procesy sdílejí jedinou stránkovací tabulku.

## Poznámka Anki 1667236244000

Karty Anki: 1667236244000
GUID: fEH&4[KO;W; štítky: bi-aps::p07 bi-spol::18.

### Otázka (Front)

Popište strukturu virtuální a fyzické adresy.

### Odpověď (Back)

**Virtuální adresa** se skládá následujících položek:

- číslo stránky,
- offset.

**Fyzická adresa **se skládá z následujících částí:

- číslo rámce,
- offset.

## Poznámka Anki 1667236494728

Karty Anki: 1667236494728
GUID: s,eU6@32s5; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

Metadata původního zdroje pro kartu 1667236494728: v původním balíčku pozastavená karta.

### Otázka (Front)

Zakreslete dvouúrovňový systém tabulek stránek.

### Odpověď (Back)

[Obrázek: paste-c39af8f2a90d39405ef6d47b7456bae357d6bb30.jpg; soubor je v media/ v doprovodném ZIP] 

- **AR** - access rights

- **P** - presence (bit platnosti)

- **pgd** - ukazatel na začátek tabulky stránek

## Poznámka Anki 1667236786615

Karty Anki: 1667236786615
GUID: o^6MV}U*#s; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

### Otázka (Front)

Popište strukturu jednoho řádku tabulky stránek.

### Odpověď (Back)

Jeden řádek tabulky stránkek obsahuje následující položky:

- **číslo rámce** - číslo rámce nebo adresy následující stránkovací tabulky,

- ****řídící **bity:**

- presence (\(\mathtt P\)) - nastaven, pokud je stránka v hlavní paměti;

- reference nebo také acessed (\(\mathtt R\) nebo \(\mathtt A\)) - nastaven, při každém přístupu ke stránce;

- modified nebo také dirty (\(\mathtt M\) nebo \(\mathtt D\)) - nastaven, při změně obsahu stránky;
- cache enabled nebo cache disabled - nastaven na disabled při paměťově mapovaném I/O;

- user nebo supervisor - určuje úrovně přístupu;

- a další.

## Poznámka Anki 1667236884738

Karty Anki: 1667236884738
GUID: fku/FstJ^j; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

### Otázka (Front)

Popište page walk.

### Odpověď (Back)

Page walk je proces překladu virtuální adresy na fyzickou adresu, kdy se prochází všechny úrovně stránkovacích tabulek. Typicky je prováděn memory management unit (MMU), která je součástí procesoru. Protože se stránkování aplikuje i na stránkovací tabulky, může se stát, že některé tabulky budou odloženy (swapped) na disku. Proto se page walk často urychluje pomocí translation lookaside buffer (TLB).

## Poznámka Anki 1667243480719

Karty Anki: 1667243480719
GUID: Aw(=)bf^WN; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

### Otázka (Front)

Co je to memory management unit (MMU)?

### Odpověď (Back)

Memory management unit je část procesoru, která zajišťuje překlad virtuálních adres na fyzické adresy, tedy realizuje page walk.

## Poznámka Anki 1667243512997

Karty Anki: 1667243512997
GUID: m^:(P@x3%9; štítky: bi-aps::p07 bi-ib::06 bi-spol::18 bi-spol::19.

### Otázka (Front)

Definujte výpadek stránky (page fault). Jaké rozeznávámy typy?

### Odpověď (Back)

Výpadek stránky je situace, kdy procesor vygeneruje výjimku v reakci na přístup k virtuální adrese, kterou není memory management unit schopna přeložit. Existují dva typy výpadků stránky:

- **invalid page fault **- virtuální adresa není součásti virtuálního adresního prostoru (obvykle generuje segmentation fault);

- **valid page fault **- virtuální adresa je součástí virtuálního adresního prostoru, ale nelze provést její překlad (např. stránka je odložena na disku a OS musí zajistit její přesun do hlavní paměti a nastavení tabulky stránek).

## Poznámka Anki 1667244640202

Karty Anki: 1667244640202
GUID: H&V!Q#0_>>; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

### Otázka (Front)

Popište translation lookaside buffer (TLB) a zakreslete její strukturu.

### Odpověď (Back)

Translation lookaside buffer (TLB) obsahuje překlady nejčastěji používaných virtuálních adres, čímž minimalizuje pamětovou latenci spojenou s překladem virtuální adresy na fyzickou adresu. Pro jednoduchost je TLB znázorněna jako přímo mapovaná cache, ve skutečnosti se však používá stupeň asociativity 4-64.

 [Obrázek: paste-96bca2bc47bbe6f04adbfe3b2dd0de20326598a5.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1667244766818

Karty Anki: 1667244766819
GUID: w;A|RalST(; štítky: bi-aps::p07 bi-ib::06.

### Otázka (Front)

Popište strukturu jednoho řádku v translation lookaside buffer.

### Odpověď (Back)

Jeden řádek v translation lookaside buffer obsahuje následující položky:

- **validity bit** (\(\mathtt V\)) - nastaven, pokud je řádek platný;

- **číslo stránky** (tag);
- **číslo rámce**;
- **address space identifier** (ASID) - identifikátor adresního prostoru;
- ****řídící **bity**:

- global flag (\(\mathtt G\)) - pokud je nastaven, ignoruje se ASID;

- cache policy (\(\mathtt C\));

- přístupová práva.

## Poznámka Anki 1667244943005

Karty Anki: 1667244943005
GUID: Q_Vvts9nWb; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

Metadata původního zdroje pro kartu 1667244943005: v původním balíčku pozastavená karta.

### Otázka (Front)

K čemu slouží ASID (Address Space ID) neboli identifikátor adresního prostoru?

### Odpověď (Back)

- Každý proces používá vlastní adresní prostor, ale vlákna vrámci jednoho procesu tento prostor sdílí.
- Během přepínání kontextu z jednoho procesu na druhý, dochází i ke změně adresního prostoru.
- Aby se TLB při každém přepnutí kontextu nemusel vyprázdnit, je součástí každé jeho položky ASID, který určí, zda je záznam pro aktuální kontext platný.

## Poznámka Anki 1667244999649

Karty Anki: 1667244999649
GUID: fO3:j>^c{=; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

Metadata původního zdroje pro kartu 1667244999649: v původním balíčku pozastavená karta.

### Otázka (Front)

Zakreslete schéma HW podpory stránkování.

### Odpověď (Back)

[Obrázek: paste-a1303d16b4cd3ffa88c95f8c52afc3425b348e46.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1667245131721

Karty Anki: 1667245131721
GUID: EeFqJX^fy[; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

Metadata původního zdroje pro kartu 1667245131721: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké rozlišujeme TLB a jak jsou uspořádány?

### Odpověď (Back)

Dnešní CPU implementují dvě nezávislé TLB:

- **iTLB** - instrukční TLB,

- **dTLB** - datovou TLB.

TLB jsou uspořádány hierarchicky pro minimalizaci jejich latence a maximalizaci jejich velikosti.

## Poznámka Anki 1717513949156

Karty Anki: 1717513949156
GUID: v&%0uBs&=c; štítky: bi-aps::p07 bi-ib::06 bi-spol::18.

### Otázka (Front)

Porovnejte jednoúrovňové stránkování s víceúrovňovým stránkováním.

### Odpověď (Back)

Při **jednoúrovňovém stránkování** bude operační systém pro každý proces uchovávat rozsáhlou stránkovací tabulku. Navíc protože tabulky nelze fragmentovat, není možné je stránkovat. **Víceúrovňové stránkování** sníží velikost jednotlivých tabulek a umožní pro ně použít stránkování. Navíc dovoluje snížit paměťové požadavky, protože pro některé procesy může být postačující pouze první úroveň stránkovacích tabulek a další lze alokovat dynamicky.

