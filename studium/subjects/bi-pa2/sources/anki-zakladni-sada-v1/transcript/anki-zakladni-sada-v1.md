# BI-PA2 – Základní sada otázek

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-PA2
Rozsah: 42 poznámek, 42 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1655282850885

Karty Anki: 1655282850885
GUID: G?m;WSz(S]; štítky: bi-pa2::ustni.

### Otázka (Front)

Popište standardní datové proudy.

### Odpověď (Back)

**Datový proud** (\(\mathtt{ stream }\)) je tok dat od zdroje k cíli s možnou konverzí.
Dělíme je na:

- vstupní proud (\(\mathtt{ istream }\)) - data jsou čtena ze zdroje a ukládána do paměti (např. \(\mathtt{ cin }\) - std. vstup, \(\mathtt{ ifstream }\) - soubor, \(\mathtt { istringstream }\) - paměťový prostor)
- výstupní proud (\(\mathtt { ostream }\)) - data jsou čtena z paměti a posílána na výstup (např. \(\mathtt{ cout }\) - std. výstup, \(\mathtt{ cerr }\) - std. chybový výstup, \(\mathtt{ ofstream }\) - soubor, \(\mathtt{ ostringstream }\) - paměťový prostor)

## Poznámka Anki 1655283096988

Karty Anki: 1655283096988
GUID: nTY.h1[%{h; štítky: bi-pa2::ustni.

### Otázka (Front)

Popište konverze u standartních datových proudů.

### Odpověď (Back)

- na různých OS se používají různé konce řádků (\(\mathtt{ LF }\) - UNIX, \(\mathtt{ CR\ LF }\) - Windows, DOS, \(\mathtt{ CR }\) - Mac (old))
- v paměti je konec řádku vždy \(\mathtt { LF }\)
- na Mac/Windows provádí C/C++ standartní knihovna konverze při čtení a zápisu
- u binárních souborů může kvůli konverzi dojít k poškození obsahu, konvezi je proto nutné vypnout

## Poznámka Anki 1655283246778

Karty Anki: 1655283246778
GUID: yxe5tr&5Y:; štítky: bi-pa2::ustni.

### Otázka (Front)

Popište IO manipulátory.

### Odpověď (Back)

Jde o sadu nástrojů pro řízení vzhledu formátovaného výstupu. Posílají se do proudu před proměnnou a ovlivňují její zobrazení. Jsou deklarovány v \(\mathtt { \text{<}iomanip\text{>} }\). Např. \(\mathtt{ hex }, \mathtt { setw (x) }, \mathtt { setfill (c) }\) a další.

## Poznámka Anki 1655283528864

Karty Anki: 1655283528864
GUID: %U;;q3O3L; štítky: bi-pa2::ustni.

### Otázka (Front)

Jak fungují implicitní hodnoty parametrů?

### Odpověď (Back)

Implicitní hodnoty parametrů se uvádí v definici funkcí a určují hodnotu parametru v případě, že je vynechán. Z toho důvodu se musí řadit až na konec seznamu parametrů.

## Poznámka Anki 1655283736306

Karty Anki: 1655283736306
GUID: tD:8O[kYI8; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Co je to přetěžování funkcí?

### Odpověď (Back)

V C++ lze deklarovat funkce se stejným jménem, ale s různými typy či počtem parametrů. Takovým to funkcím se říká přetížené funkce. Funkce však nelze odlišit pouze návratovým typem. Jde o typ compile-time polymorfismu, jelikož o tom, jaká funkce se ve výsledku zavolá je rozhodnuto už při kompilaci programu.

## Poznámka Anki 1655284142989

Karty Anki: 1655284142989
GUID: GE^j=qS{1U; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište inline funkce.

### Odpověď (Back)

U inline funcí se místo zavolání funkce provede její vyexpandování do zdrojového kódu při kompilaci. Tím se vyhneme overheadu, který obnáší zavolání funkce.
Funkce deklarované a definované v těle třídy jsou implicitně inline. Dále můžeme inline funkce deklarovat pomocí klíčového slova \(\mathtt{ inline }\), které je však pro kompilátor nezávazné.

## Poznámka Anki 1655284506141

Karty Anki: 1655284506141
GUID: K@mc?;Wmoq; štítky: bi-pa2::ustni.

### Otázka (Front)

Definujte konstanty.

### Odpověď (Back)

Konstanta je proměnná, která nemůže být upravena po tom, co je definována. Můžeme je vytvářet pomocí maker preprocesoru (\(\mathtt { \#define }\)), klíčového slova \(\mathtt{ const }\) či \(\mathtt { constexpr }\).

## Poznámka Anki 1655284714847

Karty Anki: 1655284714847
GUID: BPp!wx{INE; štítky: bi-pa2::ustni.

### Otázka (Front)

Popište reference.

### Odpověď (Back)

Proměnná deklarovaná s operátorem \(\mathtt { \& }\) se nazývá referencí a funguje jako alternativní identifikátor dané proměnné. Pokud deklarujeme parametr funkce jako referenci, tak je nám umožněno modifikovat hodnotu tohoto parametru nebo vyhnout se kopírování velkých objektů. Reference může být vnitřně reprezentována jako ukazatel.

## Poznámka Anki 1655284944054

Karty Anki: 1655284944054
GUID: bdMA7HV0k; štítky: bi-pa2::ustni bi-spol::19.

### Otázka (Front)

Popište operátory \(\mathtt { new }\) a \(\mathtt { delete }\).

### Odpověď (Back)

Operátor \(\mathtt { new }\) slouží k alokaci prostoru pro proměnnou na haldě. Takto alokovaná paměť musí být uvolněna pomocí operátoru \(\mathtt { delete }\).
Pomocí operátoru \(\mathtt{ new [] }\) můžeme alokovat paměť pro pole. Tuto paměť však uvolňujeme pomocí operátoru \(\mathtt { delete [] }\).

## Poznámka Anki 1655285245137

Karty Anki: 1655285245137
GUID: jUM8ot2c!0; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište třídu.

### Odpověď (Back)

Třída je datový typ sloužící jako vzor pro vytváření objektů, které se poté nazývají instance třídy. Definuje:

- **data** - atributy (členské proměnné),

- **rozhraní** - metody (členské funkce).

## Poznámka Anki 1655285358365

Karty Anki: 1655285358365
GUID: p8zYWE@uvi; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište objekt a operátor \(\mathtt{ this }\).

### Odpověď (Back)

Objekt je konkrétní instancí třídy, tedy prvek modelované reality. Jeho typem je třída. Operátor \(\mathtt{ this }\) je ukazatel na tuto konkrétní instanci a umožnuje přístup k jejím metodám a členským proměnným.

## Poznámka Anki 1655285417730

Karty Anki: 1655285417730
GUID: D^{^rA{y)y; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište konstantní metodu třídy.

### Odpověď (Back)

Konstantní metoda třídy je metoda, která nemění stav daného objektu, tedy nemění členské proměnné a nesmí ani volat nekonstantní metody třídy.

## Poznámka Anki 1655386061586

Karty Anki: 1655386061589
GUID: J&sX#6@?]K; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište statické položky a metody tříd.

### Odpověď (Back)

Není-li určeno jinak, jsou položky a metody třídy součástí každého objektu (instance). Pokud je položka nebo metoda deklarována jako statická, je součastí dané třídy nikoliv konkrétního objektu. Nemůže tedy přistupovat k ne-statickým položkám a metodám.

## Poznámka Anki 1655386439460

Karty Anki: 1655386439460
GUID: KY_DVB6@6[; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište přetěžování operátorů.

### Odpověď (Back)

Stejně jako je možné přetěžovat funkce, je možné přetížit operátory tak, aby fungovaly s uživatelskými třídami. Deklarují se jako funkce či metody pomocí klíčového slova \(\mathtt{ operator }\).

## Poznámka Anki 1655386809678

Karty Anki: 1655386809678
GUID: h=%%I`lKQe; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište uživatelskou konverzi.

### Odpověď (Back)

Už v C se provádí automatická konverze operandů pokud je třeba. Např. výraz \(4.7 + 3\) se automaticky zkonvertuje na \(4.7 + \mathtt{ (double) } 3\), protože operand \(4.7\) je právě typu \(\mathtt{ double }\). Stejně tak se v C++ mohou konvertovat operandy přetížených operátorů, a to pomocí konstruktorů uživatelské konverze.
Konstruktorem uživatelské konverze typu \(\mathtt{ T1 }\) na typ \(\mathtt{ T2 }\) rozumíme takový konstruktor třídy \(\mathtt{ T2 }\), který lze zavolat s jediným parametrem typu \(\mathtt { T1 }\).
Tuto implicitní konverzi lze zakázat deklarováním takového konstruktoru jako explicitního pomocí klíčového slova \(\mathtt{ explicit }\).

## Poznámka Anki 1655387531836

Karty Anki: 1655387531836
GUID: yel!)qUKu*; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Porovnejte kopírující konstruktor a operátor přiřazení.

### Odpověď (Back)

**Kopírující konstruktor** je členská funkce, která má za úkol inicializovat nový objekt kopií již existujícího objektu.
**Operátor přiřazení** se používá k přiřazení obsahu již exsitující proměnné do jiné již existující proměnné.

## Poznámka Anki 1655387835216

Karty Anki: 1655387835216
GUID: nC?aJfB6wZ; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Porovnejte mělkou a hlubokou kopii.

### Odpověď (Back)

**Mělká kopie** se vytvoří jednoduše zkopírováním obsahu všech proměnných. To je postačující pouze v případě, že objekt neobsahuje dynamicky alokované proměnné. Mělká kopie objektů, které mají zdroje alokované na haldě může způsobovat chyby jako double-free, memory leaks a další.
**Hluboká kopie** překopíruje obsah všech proměnných vzorového objektu a zároveň vytvoří separátní a nezávislou kopii dynamicky alokovaných zdrojů.

## Poznámka Anki 1655388223088

Karty Anki: 1655388223088
GUID: o.wMOAi)g!; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Jak fungují počítané reference a copy-on-write?

### Odpověď (Back)

Ne vždy je potřeba ihned vytvářet hlubokou kopii objektu. Do objektu stačí přidat počítadlo, které se inkrementuje s každým "kopírováním" objektu (vytvořením nové reference) a dekrementuje s každým zavoláním destruktoru, přičemž pokud je po této dekrementaci nulové, dojde ke skutečné dealokaci prostředů.
Pokud pak dojde k zavolání metody, která by měnila obsah tohoto objektu, provede se skutečná hluboká kopie, korespondující úprava objektu a dekrementace počítadla.

## Poznámka Anki 1655388903433

Karty Anki: 1655388903433
GUID: t=);JVH_`4; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište výjimky.

### Odpověď (Back)

Výjimky jsou vylepšení C++ oproti C. Kde v C se informace o chybě předávala nejčastěji pomocí návratové hodnoty funkce, můžeme v C++ využít výjimky. Ty nám umožňují oddělit error-handling od ostatního kódu. Zároveň při jejich prostupování call-stackem výše zajišťují úklid ve všech blocích, které jsou opouštěny. Výjimky jsou vytvářeny pomocí klíčového slova \(\mathtt{ throw }\) a lze je zpracovávat pomocí \(\mathtt{ try }\)-\(\mathtt{ catch }\) bloku. Pokud výjimka zpracována není, způsobí ukončení programu.

## Poznámka Anki 1655390232328

Karty Anki: 1655390232328
GUID: xbyL>.QsoU; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište šablony funkcí a tříd.

### Odpověď (Back)

**Šablona funkce** (generická funkce) je parametrizovaná deklarace (definice), ze které kompilátor dosazením za parametry vytvoří instanci šablony, tj. deklaraci (definici) konkrétní funkce. Parametrem šablony může být typ parametru, návratové hodnoty nebo lokálních proměnných funkce.
**Šablona třídy **(generická třída) je parametrizovatelná deklarace třídy, ze které kompilátor dosazením za generické parametry vytvoří instanci konkrétní třídy.

## Poznámka Anki 1655390425471

Karty Anki: 1655390425471
GUID: GGGF[7J0?e; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište dědičnost.

### Odpověď (Back)

Mějme bázovou třídu \(\mathtt { B }\). Pokud deklarujeme odvozenou třídu \(\mathtt{ D }\) jako potomka třídy \(\mathtt{ B }\) pomocí dvojtečkové notace, pak třída \(\mathtt{ D }\) dědí všechny atributy a metody z třídy \(\mathtt{ B }\), přičemž může přidávat vlastní. Odvozené třídy jsou jistou konkretizací abstraktnější bázové třídy.

## Poznámka Anki 1655391001672

Karty Anki: 1655391001672
GUID: j2JxoDdKwW; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište statickou vazbu.

### Odpověď (Back)

Mějme bázovou třídu \(\mathtt{ B }\) a zní odvozenou třídu \(\mathtt{ D }\).
Přiřadíme-li ukazatel na \(\mathtt{ D }\) do ukazatele na \(\mathtt{ B }\) (např. pro heterogenní kontejner) a potom na tomto objektu zavoláme zastíněnou metodu (definovanou jak na \(\mathtt{ B }\), tak na \(\mathtt{ D }\)), pak vždy dojde k zavolání metody na bázové třídě \(\mathtt{ B }\). Jde o **statickou **(brzkou) **vazbu**. Vybraná operace je totiž vždy určena typem stojícím nalevo od operátoru a rozhoduje se o ní již v době kompilace.

## Poznámka Anki 1655391284451

Karty Anki: 1655391284451
GUID: y@nS[i*@o*; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište dynamickou vazbu.

### Odpověď (Back)

Mějme bázovou třídu \(\mathtt{ B }\) a zní odvozenou třídu \(\mathtt{ D }\).
Zastíněné metody nyní deklarujme společně s klíčovým slovem \(\mathtt{ virtual }\). Tím dojde ke vzniku VMT (Virtual Method Table). Pokud pak přiřadíme instanci \(\mathtt{ D }\) do ukazatele na třídu \(\mathtt{ B }\) a zavoláme na tomto ukazateli zastíněnou metodu, bude se volaná metoda vybírat z VMT podle typu objektu, na který tento ukazatel ukazuje. Jde o **dynamickou** (pozdní) **vazbu**, která probíhá až při runtime.

## Poznámka Anki 1655391441141

Karty Anki: 1655391441141
GUID: O<XZ>aP!b9; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Definujte polymorfismus.

### Odpověď (Back)

Polymorfismus znamená, že určitá entita se může v různých situacích chovat různě. Rozlišujeme compile-time polymorfismus a run-time polymorfismus. Compile-time polymorfismu dosahujeme pomocí přetěžování funkcí a operátorů, zatímco run-time polymorfismu pomocí virtuálních metod.

## Poznámka Anki 1655391593143

Karty Anki: 1655391593143
GUID: P(.kWq0>eG; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Definujte abstraktní metodu a abstraktní třídu.

### Odpověď (Back)

**Abstraktní metoda** je metoda, která je deklarovaná, ale není definovaná a na místo její implementace je umístěna konstrukce \(\texttt{= 0}\). **Abstraktní třída** je pak třída s alespoň jednou abstraktní metodou. Používají se pro definování rozhraní, které následně odvozené třídy implmementují. Abstraktní třídy nelze instancovat.

## Poznámka Anki 1655392245875

Karty Anki: 1655392245875
GUID: K)9ULWO}b#; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Definuje polymorfní datovou strukturu.

### Odpověď (Back)

Polymorfní datová struktura obsahuje prvky různých typů, operace s prvky se mohou provádět různě v závislosti na typu prvku. Implementujeme je pomocí abstraktních tříd.

## Poznámka Anki 1655392454476

Karty Anki: 1655392454476
GUID: oapzd,pDqZ; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište dynamické přetypování.

### Odpověď (Back)

Dynamické přetypování (\(\mathtt{ dynamic\_cast }\)) lze využít pro tzv. downcast, neboli převod ukazatele z bázové třídy na odvozenou třídu. Pokud je tato operace úspěšná je výsledkem této operace ukazatel na objekt odvozené třídy, pokud ne, je výsledekm \(\mathtt{ nullptr }\).

## Poznámka Anki 1655392585413

Karty Anki: 1655392585413
GUID: G!Eq;|<f).; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Popište RTTI a operátor \(\mathtt{ typeid }\).

### Odpověď (Back)

Run-Time Type Information (RTTI) nám umožňuje zjistit typ objektu za běhu programu. Slouží k tomu např. operátor \(\mathtt{ typeid }\), který vrací objekt typu \(\mathtt{ std::type\_info }\) vybavený mimo jiné operátory \(\mathtt{ == }\), \(\mathtt{ != }\) či metodou \(\mathtt{ name () }\).

## Poznámka Anki 1655393320383

Karty Anki: 1655393320383
GUID: gO7SMNFPxo; štítky: bi-pa2::ustni bi-spol::22.

### Otázka (Front)

Vyjmenujte a vysvětlete operátory přetypování.

### Odpověď (Back)

- \(\mathtt{ (T)x }\) - přetypování z C

- \(\mathtt{ const\_cast<T>(x) }\) - přidává či odebírá modifikátory \(\mathtt{ const }\) a \(\mathtt{ volatile }\)

- \(\mathtt{ static\_cast<T>(x) }\) - běžná přetypování, v rámci hierarchie tříd pouze se statickou kontrolou (za běhu může vést k chybám)

- \(\mathtt{ dynamic\_cast (x) }\) - přetypování ukazatelů nebo referencí v rámci hierarchie tříd s dynamickou kontrolou typů
- \(\mathtt{ reinterpret\_cast (x) }\) - přetypování bez kontrol; implementačně závislé a nepřenositelné

## Poznámka Anki 1655394551999

Karty Anki: 1655394551999
GUID: snb7JK~@Q^; štítky: bi-pa2::ustni bi-spol::19 bi-spol::23.

### Otázka (Front)

Popište abstraktní datový typ (ADT).

### Odpověď (Back)

Abstraktní datový typ (ADT) je datový typ, který je definován svým chováním, konkrétně množinou možných hodnot a množinou možných operací. Interní implementace ADT je pro uživatele nepodstatná a chování ADT je na ní nezávislé.

## Poznámka Anki 1655395148941

Karty Anki: 1655395148941
GUID: M?M[d[BS]o; štítky: bi-pa2::ustni bi-spol::23.

### Otázka (Front)

Popište zásobník (stack).

### Odpověď (Back)

Zásobník (stack) je sekvenční abstraktní datový typ, který organizuje prvky na principu LIFO. Měl by podporovat následující operace:

- \(\texttt{push}\) - vloží prvek na vrchol zásobníku,

- \(\texttt{pop}\) - odebere prvek z vrcholu zásobníku.

Očekávané časové složitosti těchto operací jsou \(\mathcal O(1)\) případně \(\mathcal O^*(1)\). Zásobník lze implementovat pomocí:

- statické pole pevné délky,
- dynamické pole pevné délky,
- dynamické pole proměnlivé délky,
- spojový seznam.

## Poznámka Anki 1655395454108

Karty Anki: 1655395454108
GUID: D5tVu(f:rq; štítky: bi-pa2::ustni bi-spol::23.

### Otázka (Front)

Popište frontu (queue).

### Odpověď (Back)

Fronta (queue) je sekvenční abstraktní datový typ, který organizuje prvky na principu FIFO. Měla by podporovat následující operace:

- \(\mathtt{enqueue}\) - vloží prvek na konec fronty,

- \(\texttt{dequeue}\) - odebere prvek ze začátku fronty.

Očekávané časové složitosti těchto operací jsou \(\mathcal O(1)\) případně \(\mathcal O^*(1)\). Frontu lze implementovat pomocí:

- statické pole pevné délky,
- dynamické pole pevné délky,
- dynamické pole proměnlivé délky,
- spojový seznam.

### Doplňující pole (Extra)

V implementacích pomocí pole se postupuje, tak že při vkládání prvku proběhne kontrola, zda je „prázdný“ prostor před prvky větší než počet prvků. Pokud ano, jsou prvky přesunuty na začátek pole. Lze dokázat, že vkládání má v takovém případě časovou složitost \(\mathcal O^*(1)\).

## Poznámka Anki 1655395574633

Karty Anki: 1655395574633
GUID: Dydt(ks5&|; štítky: bi-pa2::ustni bi-spol::23.

### Otázka (Front)

Popište seznam (list)

### Odpověď (Back)

Seznam (list) je sekvenční abstraktní datový typ. Měl by podporovat následující operace, přičemž operace jsou určeny pozicí v seznamu:

- \(\texttt{insert}\) - vloží prvek před pozici v seznamu,

- \(\texttt{remove}\) - odstraní prvek za pozicí v seznamu,

- \(\texttt{read}\) - přečte hodnotu prvku na aktuální pozici,

- \(\texttt{next}\), \(\texttt{prev}\) - posune pozici v seznamu.

Očekávané časové složitosti těchto operací jsou \(\mathcal O(1)\), proto se ADT seznam implementuje pomocí obousměrně zřetězeného spojového seznamu.

## Poznámka Anki 1655396870856

Karty Anki: 1655396870856
GUID: fYl|q*c#Ak; štítky: bi-pa2::ustni bi-spol::23.

### Otázka (Front)

Popište pole (array), mapovací funkci a reprezentaci vícerozměrného pole.

### Odpověď (Back)

**Pole** (array) je sekvenční abstraktní datový typ, který organizuje prvky v \(n\) dimenzionálním prostoru, přičemž každý prvek je identifikován \(n\)-ticí indexů. Mělo by podporovat přístup k prvkům s časovou složitostí \(\mathcal O(1)\). Pro přístup k prvkům se používá **mapovací funkce**. **Vícerozměrná pole **lze reprezentovat jako:

- kontinuální blok serializovaný po řádcích,
- kontinuální blok serializovaný po sloupcích,
- přístupové vektory (Ilifeho vektory).

 [Obrázek: paste-e768fd980bb1358128ab1d37683d96555ec2c575.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1655397506135

Karty Anki: 1655397506135
GUID: w-P-;-@s#g; štítky: bi-pa2::ustni bi-spol::23.

### Otázka (Front)

Popište množinu (set) a tabulku (map).

### Odpověď (Back)

**Množina **(set) je asociativní abstraktní datový typ, který uchovává klíče bez duplicit. Měla by podporovat operace:

- \(\texttt{insert}\) - vloží prvek do množiny;

- \(\texttt{delete}\) - odstraní prvek z množiny;

- \(\texttt{contains}\) - zjistí, zda je prvek v množině obsažen.

**Tabulka** (map) je asociativní abstraktní datový typ podobný množině, který společně s každým klíčem uchovává navíc ještě další libovolná data. Měla by podporovat stejné opreace jako množina a navíc:

- \(\texttt{find}\) - nalezne data asociovaná s daným klíčem.

Množinu a tabulku lze implementovat pomocí:

- charakteristického (indikátorového) vektoru;
- seřazeného pole libovolného typu,
- neseřazeného pole libovolného typu,
- spojového seznamu,
- vyhledávacího stromu,
- hashovací tabulky.

Časové složitosti jednotlivých implementací se mohu lišit:

 [Obrázek: paste-507201b60b3c53ed7c5658f2d583776018e84321.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1655399532619

Karty Anki: 1655399532619
GUID: pU|)k?]=KO; štítky: bi-pa2::ustni.

### Otázka (Front)

Popište binární vyhledávací strom.

### Odpověď (Back)

Binární vyhledávací strom je asociativní kontejner obsahující hodnoty identifikované klíči. Jeho požadavkem je, aby byly každé dva klíče nazvájem porovnatelné. Potom pro uzel stromu s hodnotou \(x\) platí, že v jeho levém podstromu jsou uzly s hodnotou menší než \(x\) a v jeho pravém podstromu se nachází klíče s vyšší hodnotou než \(x\).

## Poznámka Anki 1655399615732

Karty Anki: 1655399615732
GUID: OzV>P`ciz<; štítky: bi-pa2::ustni.

### Otázka (Front)

Jaké existují algoritmy pro průchod stromem?

### Odpověď (Back)

- DFS (Depth-First Search)
- BFS (Breadth-First Search)

## Poznámka Anki 1655561841792

Karty Anki: 1655561841803
GUID: xS-RoBnISn; štítky: bi-pa2::ustni.

### Otázka (Front)

Co je to rozptylovací funkce?

### Odpověď (Back)

Rozptylovací funkce je funkce, která pro každý vstup vrátí celé číslo z určitého rozsahu. Kolize jsou připuštěny.

## Poznámka Anki 1655561865513

Karty Anki: 1655561865513
GUID: s/MJgPRojQ; štítky: bi-pa2::ustni bi-spol::23.

### Otázka (Front)

Popište otevřené rozptylování.

### Odpověď (Back)

U otevřeného rozptylování umisťujeme na pozici \(i\) takové klíče, pro které vrátila hashovací funkce hodnotu \(i\). Kolize více prvků na stejné pozici zařadíme do spojového seznamu, rozšiřitelného pole nebo podobně.

## Poznámka Anki 1655561887219

Karty Anki: 1655561887219
GUID: JJm>RG)5+c; štítky: bi-pa2::ustni bi-spol::23.

### Otázka (Front)

Popište uzavřené rozptylování.

### Odpověď (Back)

U uzavřeného rozptylování se klíče ukládají do pole jehož velikost omezuje počet prvků tabulky. Kolizní řádky se ukládají na další pozice v poli. Sekvence kolizních řádku je zakončena "prázdným" řádkem, který musí v poli být alespoň jeden. 
Vyhledávání začíná na indexu daném hashovací funkcí až po další "prázdný" řádek. Při mazání nelze nahrazovat "prázdným" řádkem, ale musí se provést re-hash.

## Poznámka Anki 1718543643173

Karty Anki: 1718543643173
GUID: Et&O3eUa6w; štítky: bi-pa2 bi-spol::23.

### Otázka (Front)

Popište rozdíl mezi sekvenčními a asociativními kontejnery.

### Odpověď (Back)

**Sekvenční **kontejnery jsou takové kontejnery, které umožňují sekvenční přístup k prvkům. **Asociativní **kontejnery naopak umožňují rychlé vyhledávání, typicky v čase \(\mathcal O(\log n)\) u seřazených kontejnerů a v čase \(\mathcal O(1)\) (průměrně) u neseřazených kontejnerů.

## Poznámka Anki 1718560991021

Karty Anki: 1718560991021
GUID: uKA-lQ9T7o; štítky: bi-pa2 bi-spol::22.

### Otázka (Front)

Popište koncept abstrakce (abstraction).

### Odpověď (Back)

Abstrakce (abstraction) je koncept programovacích jazyků, který spočívá v generalizaci konkrétních případů na obecné koncepty. Formou abstakce jsou:

- generalizace konkrétních tříd na společnou rodičovskou třídu a zní dědící odvozené třídy,
- abstraktní třídy a metody,
- funkce,
- moduly,
- šablony

a další.

