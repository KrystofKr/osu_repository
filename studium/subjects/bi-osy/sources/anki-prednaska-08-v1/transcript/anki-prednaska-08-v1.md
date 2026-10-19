# BI-OSY – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-osy/BI-OSY.apkg; APKG SHA-256 e601d54cae58e1923ab743a64796ef89ec49f6bcd52ac062288890242af207fc. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b95b42cacacaa5de70f8162d09b00582086c2fd5b59f3a299e3fc9531a688ab6.
Původní balíčky: BI-OSY
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1681306029946

Karty Anki: 1681306029946
GUID: h]@(NiX,(I; štítky: bi-ib::06 bi-osy::p08 bi-spol::18.

Metadata původního zdroje pro kartu 1681306029946: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište strukturu jednoho řádku v invertované tabulce stránek.

### Odpověď (Back)

Pro každý rámec obsahuje invertovaná tabulka stránek jeden řádek s následujícími informacemi:

- **číslo stránky** - číslo stránky, která je do rámce nahrána;
- **číslo procesu **- číslo procesu, do jehož virtuálního adresního prostoru stránka patří;

- ****řídící **bity:**

- presence (\(\mathtt P\)) - nastaven, pokud je stránka v hlavní paměti;

- reference nebo také acessed (\(\mathtt R\) nebo \(\mathtt A\)) - nastaven, při každém přístupu ke stránce;

- modified nebo také dirty (\(\mathtt M\) nebo \(\mathtt D\)) - nastaven, při změně obsahu stránky;
- cache enabled nebo cache disabled - nastaven na disabled při paměťově mapovaném I/O;

- user nebo supervisor - určuje úrovně přístupu;

- a další.

- **index zřetězení **(chain index).

## Poznámka Anki 1681306186744

Karty Anki: 1681306186744
GUID: t/SbELzGVX; štítky: bi-ib::06 bi-osy::p08 bi-spol::18.

### Otázka (Front)

Popište fungování invertované tabulky stránek.

### Odpověď (Back)

OS si uchovává pouze jednu tabulku pro celý systém. Číslo stránky (z virtuální adresy) se přepočte pomocí hashovací funkce na index do tabulky stránek. Protože je počet stránek větší než počet rámců, může se několik různých stránek mapovat na jednu řádku v tabulce stránek. Proto proběhne kontrola, zda sedí číslo procesu, a pokud ne, je přistoupeno na další řádku, na kterou odkazuje index zřetězení.

## Poznámka Anki 1687711483395

Karty Anki: 1687711483396
GUID: fw^B[7Wni[; štítky: bi-osy::p08.

Metadata původního zdroje pro kartu 1687711483396: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište virtualizaci hlavní paměti stránkováním.

### Odpověď (Back)

Každému procesu je přidělen virtuální adresní prostor (VAS), v rámci kterého používá proces virtuální adresy. VAS je dělen na stejně velké **stránky** (pages). Hlavní paměť je dělena na stejně velké **stránkové rámce** (frames), přičemž velikost stránky a rámce je také stejná. Běžící procesy pak do hlavní paměti umisťují pouze aktuálně využívané stránky svého VAS (tzv. working set) a zbytek stránek je odložen na disku.

## Poznámka Anki 1687711674406

Karty Anki: 1687711674407
GUID: G7`v)wb^NL; štítky: bi-osy::p08.

Metadata původního zdroje pro kartu 1687711674407: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to memory management unit (MMU)?

### Odpověď (Back)

Memory management unit je část procesoru, která zajišťuje překlad virtuálních adres na fyzické adresy, tedy realizuje page walk.

## Poznámka Anki 1687712026523

Karty Anki: 1687712026524
GUID: PS{p_Suz)!; štítky: bi-osy::p08 bi-spol::18.

Metadata původního zdroje pro kartu 1687712026524: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte výpadek stránky (page fault). Jaké rozeznávámy typy?

### Odpověď (Back)

Výpadek stránky je situace, kdy procesor vygeneruje výjimku v reakci na přístup k virtuální adrese, kterou není memory management unit schopna přeložit. Existují dva typy výpadků stránky:

- **invalid page fault **- virtuální adresa není součásti virtuálního adresního prostoru (obvykle generuje segmentation fault);

- **valid page fault **- virtuální adresa je součástí virtuálního adresního prostoru, ale nelze provézt její překlad (např. stránka je odložena na disku a OS musí zajistit její přesun do hlavní paměti a nastavení tabulky stránek).

## Poznámka Anki 1687712317482

Karty Anki: 1687712317482
GUID: hRpg2=v.(h; štítky: bi-osy::p08.

Metadata původního zdroje pro kartu 1687712317482: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké existují struktury pro překlad a mapování virtuálních adres?

### Odpověď (Back)

Moderní operační systémy využívají jednu z následujících struktur:

- **konvenční (víceúrovňová) stránkovací tabulka** - každý proces má vlastní stránkovací tabulku, resp. strom stránkovacích tabulek, jejíž počáteční adresa je uložena v \(\mathtt{mm\_struct}\) v ukazateli \(\mathtt{*pgd}\);

- **inverzní stránkovací tabulka** - všechny procesy sdílejí jedinou stránkovací tabulku.

## Poznámka Anki 1687808795146

Karty Anki: 1687808795146
GUID: Lw(461t,V; štítky: bi-osy::p08.

Metadata původního zdroje pro kartu 1687808795146: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište strukturu virtuální a fyzické adresy.

### Odpověď (Back)

**Virtuální adresa** se skládá následujících položek:

- číslo stránky,
- offset.

**Fyzická adresa **se skládá z následujících částí:

- číslo rámce,
- offset.

## Poznámka Anki 1687808916580

Karty Anki: 1687808916580
GUID: QrrY&g13TQ; štítky: bi-osy::p08.

Metadata původního zdroje pro kartu 1687808916580: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište translation lookaside buffer (TLB) a zakreslete její strukturu.

### Odpověď (Back)

Translation lookaside buffer obsahuje překlady nejčastěji používaných virtuálních adres, čímž minimalizuje pamětovou latenci spojenou s překladem virtuální adresy na fyzickou adresu. Pro jednoduchost je TLB znázorněna jako přímo mapovaná cache. Ve skutečnosti se však používá stupěň asociativity 4-64.

 [Obrázek: paste-96bca2bc47bbe6f04adbfe3b2dd0de20326598a5.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1687809598304

Karty Anki: 1687809598304
GUID: u@Io(s4SGy; štítky: bi-osy::p08.

Metadata původního zdroje pro kartu 1687809598304: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

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

## Poznámka Anki 1687810228554

Karty Anki: 1687810228554
GUID: m9(MPNtgu!; štítky: bi-osy::p08.

Metadata původního zdroje pro kartu 1687810228554: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

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

