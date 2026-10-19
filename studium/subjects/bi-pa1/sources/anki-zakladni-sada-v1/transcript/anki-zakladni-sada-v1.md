# BI-PA1 – Základní sada otázek

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-PA1
Rozsah: 87 poznámek, 87 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1641426159931

Karty Anki: 1641426159932
GUID: HE<I&`nmc$; štítky: bi-pa1::ustni.

### Otázka (Front)

ADT Set (množina) vs ADT List (seznam)

### Odpověď (Back)

Množina by měla být bez duplicit a je neuspořádaná, je často reprezentována jako binární vyhledávací strom.

V seznamu se mohou objevit duplicity a má pořadí. Ve spojovém seznamu na sebe prvky navzájem odkazují.

## Poznámka Anki 1641426366384

Karty Anki: 1641426366394
GUID: DcOdxM9X,p; štítky: bi-pa1::ustni bi-spol::19.

### Otázka (Front)

Popište endianitu (little endian a big endian).

### Odpověď (Back)

Endianita označuje pořadí, ve kterém jsou jednotlivé byty vícebytových dat adresovány v paměti nebo přenášeny po komunikačním médiu. Rozlišujeme:

- **little endian **- nejméně významný byte leží na nejnižší adrese (je přenášen jako první),
- **big endian** - nejvíce významný byte leží na nejnižší adrese (je přenášen jako první).

## Poznámka Anki 1641461296909

Karty Anki: 1641461296910
GUID: dsRQ]+!wl=; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je medián a jak souvisí s pojmem pivot? Kde se používají a jak se dají určit?

### Odpověď (Back)

Medián je střední hodnota dané množiny a dělí ji tak na dvě poloviny.
Pivot je kandidátem na střední hodnotu. Využívá se např. v Quicksortu. Zde ale není množina předem seřazena, a tak se vybírá ze tří náhodných prvků. Čím bíže je pivot ke skutečnému mediánu, tím rychlejší Quicksort je.

## Poznámka Anki 1641461515192

Karty Anki: 1641461515193
GUID: wy/J8d1X}2; štítky: bi-pa1::ustni.

### Otázka (Front)

Co vyjadřuje asymptotická složitost algoritmu, proč bychom se jí měli zabývat?

### Odpověď (Back)

Asymptotická složitost vyjadřuje nejhorší možnou složitost programu vzhledem k velikosti vstupních dat.
Zanedbává aditivní a multiplikativní konstanty.
Vyjadřuje se jako: \(O(f(n))\)

## Poznámka Anki 1641461996320

Karty Anki: 1641461996320
GUID: jE&pJxAbBp; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak je definována množina funkcí omikron \(O(f(n))\) pro nějakou funkci \(f(n)\)?

### Odpověď (Back)

Množina omikron \(O(f(n))\) je množina všech funkcí, které rostou pomaleji nebo stejně ryhle jako \(f(n)\). Jde tedy o nejhorší možnost složitosti algoritmu, která může pro libovolná vstupní data nastat.

## Poznámka Anki 1641462055831

Karty Anki: 1641462055831
GUID: IEVG>{Z]GN; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaké chyby mohou nastat při kopírování jednoho souboru do druhého a jak tyto chyby ošetříme?

### Odpověď (Back)

rozdílný typ souborů, soubor neexistuje, nemáme dostatečná práva, není dostatek místa na disku

## Poznámka Anki 1641462256882

Karty Anki: 1641462256883
GUID: dg%HEWEo{I; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaké jsou typické operace pro ADT množinu?

### Odpověď (Back)

vložení prvku do množiny, odebrání prvku z množiny, dotaz na existenci prvku v množině, dotaz na počet prvků v množině, dotaz na shodnost dvou množin, typické množinové operace \(\cup, \cap, \backslash, \times, \subset, ...\)

## Poznámka Anki 1641462862432

Karty Anki: 1641462862432
GUID: uB|TJiJG%_; štítky: bi-pa1::ustni.

### Otázka (Front)

K čemu slouží Eratosthénovo síto, jak se používá a jaká je jeho složitost ?

### Odpověď (Back)

Slouží k nalezení všech prvočísel menších než je zadaná horní mez. Na počátku máme seznam od 2 do zadané meze. Odebereme první číslo seznamu (uložíme jej jako pročíslo) a odstraníme všechny jeho násobky. Opakujeme dokud neodstraníme poslední číslo nebo dokud není za prvočíslo označeno číslo vyšší než odmocnina horní meze.
\(O(n \cdot \log(\log(n))\)

## Poznámka Anki 1641463104744

Karty Anki: 1641463104744
GUID: K=lq1U;EBU; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je to symetrická diference?

### Odpověď (Back)

[Obrázek: paste-6de5b89e4bcc221d15ed1d8f8000dc34e936a9ef.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1641463445788

Karty Anki: 1641463445788
GUID: QNTsfcus,9; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je a k čemu slouží abstraktní datový typ a jaké jsou jeho příklady?

### Odpověď (Back)

Abstraktní datový typ (**ADT**) je **datová struktura**, která je definována **svým chováním** (jaká operace se s ní dá provádět), ale **ne způsobem její implementace**.
Příklady: queue (fronta), stack (zásobník), array (pole), table/map (tabulka), list (seznam), tree (strom), set (množina), ...

## Poznámka Anki 1641463523091

Karty Anki: 1641463523092
GUID: GcgbXRM8L7; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je a k čemu slouží binární strom?

### Odpověď (Back)

Binární vyhledávací strom je příklad ADT. Slouží např. pro reprezentaci množiny. Umožňuje efektivní vyhledávání.

## Poznámka Anki 1641463626653

Karty Anki: 1641463626653
GUID: n-NvXFLIn!; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je EOF a k čemu lze použít?

### Odpověď (Back)

EOF (End Of File) je příznak označující konec datového zdroje (běžně soubor nebo např. stdin). Lze použít jako ověření konce vstupu od uživatele programu.

## Poznámka Anki 1641463717410

Karty Anki: 1641463717410
GUID: L&zEP#V.P:; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je lineární spojová struktura? Ukažte její vytvoření pro hodnoty typu int.

### Odpověď (Back)

Spojový seznam je příklad ADT. Skládá se ze struktur (node), které obsahují vždy vlastní hodnotu prvku v seznamu a podle toho, zda je seznam jednosměrně nebo obousměrně zřetězený, odkazy na následující a předcházející prvek.

## Poznámka Anki 1641463874632

Karty Anki: 1641463874632
GUID: bJL}219{oO; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je makro v C jak funguje? Uveďte příklad.

### Odpověď (Back)

Makro je textová náhrada definovaná direktivou `#define`. Zpracuje ji preprocesor před samotnou kompilací. Ne každá direktiva preprocesoru je makro.

## Poznámka Anki 1641464061668

Karty Anki: 1641464061668
GUID: xx*}F}GBQ;; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je podmíněný překlad v C? Uveďte příklad.

### Odpověď (Back)

Podmíněný překlad je řízen direktivami pro preprocesor, který zpracovává zdrojový kód před kompilací. Na základě zadané podmínky, kterou vyhodnotí, zpracuje kód v podmíněném překladu. Direktivy začínají **# **a příkladem je: **#ifdef** a **#endif**, **#ifndef**, **#endif**, **#if**, **#elif** a **#else**, ...

## Poznámka Anki 1641464345933

Karty Anki: 1641464345933
GUID: z]riPX76IP; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je rekurze?

### Odpověď (Back)

Rekurzivní funkce je taková funkce, která volá sama sebe.

## Poznámka Anki 1641464402669

Karty Anki: 1641464402669
GUID: H.Pp@gQCBV; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je sekvenční přístup k souboru? Jaký by mohl být jiný a jak se liší?

### Odpověď (Back)

Sekvenční přístup přistupuje k záznamům popořadě (k jednomu za druhým) zatímco přímý přístup přistupuje zcela libovolně podle potřeby zpracování.

## Poznámka Anki 1641464493263

Karty Anki: 1641464493263
GUID: c])9R$Z}:U; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je sestavovač (linker) jazyka C a k čemu slouží.

### Odpověď (Back)

Linker je program, který sestaví finální spustitelný soubor z více objektových souborů generovaných překladačem (připojí do něj knihovny atd.).

## Poznámka Anki 1641464886731

Karty Anki: 1641464886731
GUID: kBy?Z6ZBIO; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je v C enum? Uveďte příklad.

### Odpověď (Back)

Výčtový typ (enum) je datový typ, který vrací hodnoty konstant definovaných programátorem.

\(\mathtt{ enum\ week\{mon, tue, wed, thu, fri, sat, sun\};}\)
\(\mathtt{ enum\ week\ day;}\)
\(\mathtt{ day = wed};\)
\(\mathtt{ printf (\ ' \%d',\ day\ );}\)
\(>2\)

## Poznámka Anki 1641465245447

Karty Anki: 1641465245447
GUID: jvMKK<dap.; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je v C union a k čemu slouží. Uveďte příklad.

### Odpověď (Back)

V jazyce C `union` (sjednocení) je speciální datová struktura, která umožňuje uložit **různé typy dat na stejném místě v paměti**.

- Na rozdíl od `struct`, kde **každá proměnná zabírá vlastní paměť**, v `union` všechny členy **sdílejí stejný paměťový prostor**.
- Velikost `union` je **dána největším členem** (ten s největší velikostí v bajtech).
- V daném čase může být **aktivní pouze jedna hodnota**.

- #include <stdio.h>
- 

- union Data {
-     int i;
-     float f;
-     char str[20];
- };
- 

- int main() {
-     union Data data;
- 

-     data.i = 10;
-     printf("data.i: %d\n", data.i);
- 

-     data.f = 3.14;
-     printf("data.f: %f\n", data.f);
- 

-     // Přepisuje předchozí hodnoty
-     snprintf(data.str, sizeof(data.str), "Hello");
-     printf("data.str: %s\n", data.str);
- 

-     // data.i i data.f jsou nyní neplatná, protože `data.str` přepsalo paměť
-     return 0;
- }
-

## Poznámka Anki 1641465402256

Karty Anki: 1641465402256
GUID: J*1[PJ5!q9; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je to bitový XOR?

### Odpověď (Back)

XOR je logická operace, která vrací 1 právě tehdy když pouze jeden ze vstupů je 1 a druhý 0. V ostatních případech vrací 0.

## Poznámka Anki 1641465489202

Karty Anki: 1641465489202
GUID: FbDe?t,eMa; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaké operace jsou v C povoleny s ukazateli a jaký mají význam?

### Odpověď (Back)

přičítání celých čísel k ukazateli (pohyb v poli), rozdíl dvou ukazatelů (počet prvků pole mezi nimi), porovnání ukazatelů, dereference

## Poznámka Anki 1641465637737

Karty Anki: 1641465637737
GUID: G(t_6}/6Rx; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaký je rozdíl mezi interpretovanými a kompilovanými programovacími jazyky. Uveďte příklady těchto jazyků.

### Odpověď (Back)

Kompilované jazyky jsou celé najednou přeloženy kompilátorem do spustielného souboru (C, C++, Pascal).
Interpretované jazyky jsou překládány interpreterem až za běhu programu (Python).

## Poznámka Anki 1641465806454

Karty Anki: 1641465806454
GUID: C/Ze~d8rJ,; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaký je rozdíl mezi syntaxí a sémantikou v programovacím jazyce.

### Odpověď (Back)

Sémantika ve světě programování se týká významu kódu – to, co kód skutečně dělá, když je proveden. Na rozdíl od **syntaktické správnosti**, která zajišťuje, že kód je napsaný podle pravidel jazyka (např. správně napsané závorky, středníky atd.), **sémantika** se soustředí na to, zda kód skutečně provádí to, co je zamýšleno a zda chování odpovídá očekáváním.

## Poznámka Anki 1641465829571

Karty Anki: 1641465829571
GUID: G`<mgzA!-:; štítky: bi-pa1::ustni.

### Otázka (Front)

Jakým způsobem měříme efektivitu algoritmu?

### Odpověď (Back)

Skrze jeho časovou a paměťovou složitost.

## Poznámka Anki 1641465920048

Karty Anki: 1641465920048
GUID: pWag_iVjD8; štítky: bi-pa1::ustni.

### Otázka (Front)

Popište podmínky použití binárního vyhledávání a určete jeho složitost.

### Odpověď (Back)

Vstup musí být setřízený a prvky musí být porovnatelné.
\(O(\log_{2}(n)\)

## Poznámka Anki 1641466063366

Karty Anki: 1641466063366
GUID: n!@EIS?_wc; štítky: bi-pa1::ustni.

### Otázka (Front)

Co dělá funkce \(\mathtt{free()}\)? Jaké má parametry?

### Odpověď (Back)

Funkce \(\mathtt{free()}\) označuje dynamicky alokovanou paměť za uvolněnou. Má jeden vstupní parametr - ukazatel na paměť.

## Poznámka Anki 1641466220807

Karty Anki: 1641466220807
GUID: u4)hi8q&xf; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je Fibonacciho posloupnost?

### Odpověď (Back)

Fibonacciho posloupnost je posloupnost definována následujícímí pravidly:
\(F_{1}=0\)
\(F_{2}=1\)
\(F_{n}=F_{n-1} + F_{n-2}\)

## Poznámka Anki 1641466303511

Karty Anki: 1641466303511
GUID: fxm6@h#?{; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je \(\mathtt{NULL}\) v C?

### Odpověď (Back)

\(\mathtt{NULL}\) se používá jako hodnota 'prázdného' ukazatele, který neukazuje na žádnou paměť.

## Poznámka Anki 1641466396805

Karty Anki: 1641466396805
GUID: zda@kfNI=]; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je předpřekladač (preprocessor) jazyka C a k čemu slouží.

### Odpověď (Back)

Zpracovává zdrojový kód před vlastní kompilací. Používá se pro připojení hlavičkových souborů a interpretaci maker.

## Poznámka Anki 1641466509725

Karty Anki: 1641466509725
GUID: LW}1F5Pr=`; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je překladač (compiler) jazyka C a k čemu slouží.

### Odpověď (Back)

Kompilátor překládá zdrojový kód C (vyššího programovacího jazyka) na spustitelný strojový kód (nižžší programovací jazyk).

## Poznámka Anki 1641466674629

Karty Anki: 1641466674630
GUID: yb>Z@dBGY`; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je soubor v C a jaký je rozdíl mezi textovým a binárním souborem?

### Odpověď (Back)

Soubor v C, typicky s příponou \(\mathtt{.c}\) je zdrojový kód, který je později kompilátorem přeložen na spustitelný strojový kód uložený v binárním souboru.
Textový soubor (potažmo soubor v C) je soubor obsahující bílé znaky a je lehce čitelný pro člověka.
Binární soubor je zcela nečitelný a to proto, že obsahuje pouze bity a bajty.

## Poznámka Anki 1641466930201

Karty Anki: 1641466930201
GUID: E4jM(*NuGu; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je přetypování (cast)?

### Odpověď (Back)

Typecast změní datový typ dané proměnné.

## Poznámka Anki 1641466987400

Karty Anki: 1641466987400
GUID: rm6G;vdp9<; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je v C řetězec?

### Odpověď (Back)

String je pole charů (znaků), které může být ukončeno terminačním znakem \(\mathtt{\backslash0}\).

## Poznámka Anki 1641467209882

Karty Anki: 1641467209882
GUID: b$A|L*7&:); štítky: bi-pa1::ustni.

### Otázka (Front)

Co je to algoritmus a jaké jsou jeho vlastnosti?

### Odpověď (Back)

Algoritmus je konečná posloupnost operací sloužící k řešení daného druhu problémů.

- hromadnost - řeší celou třídu problémů
- determinovanost - stejná vstupní data vedou ke stejným výsledkům
- resultativnost - každá vstupní data vedou k výsledku
- konečnost - konečný počet kroků vede k výsledku

## Poznámka Anki 1641467276808

Karty Anki: 1641467276808
GUID: K;ZzMTQFr4; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je v C ukazatel?

### Odpověď (Back)

Pointer je datový typ držící adresu paměti počítače.

## Poznámka Anki 1641467344407

Karty Anki: 1641467344407
GUID: uV$z31*h/9; štítky: bi-pa1::ustni.

### Otázka (Front)

Co jsou .h soubory a k čemu slouží?

### Odpověď (Back)

Hlavičkové soubory slouží jako direktiva pro preprocesor pro zařazení již napsaných funkcí funkcí do programu.

## Poznámka Anki 1641467448224

Karty Anki: 1641467448224
GUID: k3z=KBNvD,; štítky: bi-pa1::ustni.

### Otázka (Front)

Co znamená konstrukce \(\mathtt{p\to a}\) a jak ji lze nahradit?

### Odpověď (Back)

Jedná se o dereferenci ukazatele na strukturu \(\mathtt p\) a přístupu k jejímu členu \(\mathtt a\).
Lze nahradit jako: \(\mathtt{(*p).a}\).

## Poznámka Anki 1641467607584

Karty Anki: 1641467607584
GUID: bnDh4?-Qa9; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaký je rozdíl mezi definicí a deklarací funkce, uveďte příklad.

### Odpověď (Back)

Deklarace pouze udívá, že funkce existuje a bude někde definována. Defince potom určuje posloupnost kroků, kterou funkce vykonává.

## Poznámka Anki 1641467770282

Karty Anki: 1641467770282
GUID: DBN]Hp]bU;; štítky: bi-pa1::ustni.

### Otázka (Front)

Popište rozsah platnosti identifikátorů v C.

### Odpověď (Back)

Identifikátory smí obsahovat písmena (velká i malá), čísla a podtržítka. Prvním znakem identifikátoru smí být pouze písmeno nebo podtržítko. Identifikátory se nesmí shodovat s klíčovými slovy jako \(\mathtt{if}\), \(\mathtt{char}\), ...

## Poznámka Anki 1641467885698

Karty Anki: 1641467885698
GUID: J+~)6r<?pp; štítky: bi-pa1::ustni.

### Otázka (Front)

Proč je třeba nepoužívané dynamické proměnné uvolnit? Jak se to provede?

### Odpověď (Back)

Mohlo by se stát, že se by při delším běhu programu zabralo příliš mnoho paměti a program by byl ukončen. Uvolňujeme pomocí funkce \(\mathtt{free()}\).

## Poznámka Anki 1641468045644

Karty Anki: 1641468045644
GUID: OO#Qv*2j&S; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je bit, byte, kilobyte, kilobit?

### Odpověď (Back)

- **bit **- nejmenší paměťová jednotka, nabývá hodnot 1 nebo 0
- **byte **- nejmenší jednotka, se kterou pracuje procesor
\(1\ byte = 8\ bit\)
\(1\ kilobit = 1000\ bit\)
\(1\ kilobyte = 1024\ byte\)

## Poznámka Anki 1641468164685

Karty Anki: 1641468164685
GUID: QeI*[RbM1X; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je globální proměnná, jak ji v programu poznám a na jakou hodnotu je nastavena?

### Odpověď (Back)

Globální proměnná je každá proměnná deklarovaná mimo funkci \(\mathtt{main()}\) a je automaticky inicializována na 0.

## Poznámka Anki 1641468207652

Karty Anki: 1641468207652
GUID: `:+gr<H}^; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je lokální proměnná, jak ji v programu poznám a na jakou hodnotu je nastavena?

### Odpověď (Back)

Lokální proměnná je každá proměnná deklarovaná uvnitř funkce \(\mathtt{main()}\) a její počáteční hodnota je nedefinována.

## Poznámka Anki 1641468289588

Karty Anki: 1641468289588
GUID: uHPv=e<zdm; štítky: bi-pa1::ustni.

### Otázka (Front)

Co znamená zápis \(\mathtt{*(p+i)}\) ? Jak ho nahradit?

### Odpověď (Back)

K pointeru \(\mathtt p\) přičítáme index \(\mathtt i\) a dereferencujeme, posouváme tedy pointer a přistupujeme k hodnotě paměti, na kterou ukazuje. Můžeme nahradit zápisem \(\mathtt{p[i]}\).

## Poznámka Anki 1641468451605

Karty Anki: 1641468451605
GUID: Q(3v$!Y=lu; štítky: bi-pa1::ustni.

### Otázka (Front)

Vysvětlete k čemu slouží dynamické proměnné?

### Odpověď (Back)

Dynamická proměnná je taková proměnná, která zvládne přizpůsobit svou velikost podle potřeby. Využijeme ji v případě, kdy nevíme, jaká bude velikost dat v ní uložená.

## Poznámka Anki 1641468618306

Karty Anki: 1641468618306
GUID: PRuRGC(0.*; štítky: bi-pa1::ustni.

### Otázka (Front)

Co to je \(\mathtt {NaN}\) u desetinných čísel?

### Odpověď (Back)

\(\mathtt{NaN}\) (Not A Number) je nečíselná hodnota.
Např. \(x \div 0 \), \(\sqrt[2]{-x}\), ...

## Poznámka Anki 1641468766464

Karty Anki: 1641468766464
GUID: FTE!|nU7aL; štítky: bi-pa1::ustni.

### Otázka (Front)

Chceme ukládat texty s českou diakritikou. Naším cílem je co nejkompaktnější uložení (z hlediska nároků na paměť). Které kódování je nejvýhodnější: utf-8, utf-16, utf-32, iso-8859-2 nebo windows-1250?

### Odpověď (Back)

ISO-8859-2 nebo Windows-1250, obě jsou schopné zakódovat jeden znat jako jeden byte.

## Poznámka Anki 1641473515841

Karty Anki: 1641473515841
GUID: FlvF8&kEHY; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost a rozpětí \(\mathtt{char}\)?

### Odpověď (Back)

- **Velikost:** 1 byte
- **Rozpětí:** -128-127 nebo 0-255

## Poznámka Anki 1641473564993

Karty Anki: 1641473564993
GUID: M0-Y$^LxhY; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost a rozpětí \(\mathtt{unisgned\ char}\)?

### Odpověď (Back)

- **Velikost: **1 byte
- **Rozpětí:** 0-255

## Poznámka Anki 1641473617903

Karty Anki: 1641473617903
GUID: oKo-Ttbh(}; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost a rozpětí \(\mathtt{signed\ char}\)?

### Odpověď (Back)

- **Velikost:** 1 byte
- **Rozpětí:** -128-127

## Poznámka Anki 1641473737570

Karty Anki: 1641473737570
GUID: u`zEIo/,MP; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost a rozpětí \(\mathtt{int}\)?

### Odpověď (Back)

- **Velikost:** 2 nebo 4 byte
- **Rozpětí:** -32,768-32,767 nebo -2,147,483,648-2,147,483,647

## Poznámka Anki 1641473806342

Karty Anki: 1641473806342
GUID: m$d)^q/2L>; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost a rozpětí \(\mathtt{unisgned\ int}\)?

### Odpověď (Back)

- **Velikost:** 2 nebo 4 byte
- **Rozpětí:** 0-65,535 nebo 0-4,294,967,295

## Poznámka Anki 1641473956511

Karty Anki: 1641473956511
GUID: m.d>#|p}LN; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost a rozpětí \(\mathtt{short}\)?

### Odpověď (Back)

- **Velikost:** 2 byte
- **Rozpětí:** -32,768-32,767

## Poznámka Anki 1641473981726

Karty Anki: 1641473981726
GUID: LcB03Fk!nl; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost a rozpětí \(\mathtt{unisgned\ short}\)?

### Odpověď (Back)

- **Velikost:** 2 byte
- **Rozpětí:** 0-65,535

## Poznámka Anki 1641474044895

Karty Anki: 1641474044895
GUID: J8Bb5i(@Ja; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost \(\mathtt{long}\)?

### Odpověď (Back)

8 byte (4 byte na 32-bit OS)

## Poznámka Anki 1641474069103

Karty Anki: 1641474069103
GUID: M-i_HU<%y/; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost \(\mathtt{unisgned\ long}\)?

### Odpověď (Back)

8 bytes

## Poznámka Anki 1641474129838

Karty Anki: 1641474129838
GUID: q%M_w##vDP; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost, rozpětí a přesnost \(\mathtt{float}\)?

### Odpověď (Back)

- **Velikost:** 4 byte
- **Rozpětí:** 1.2E-38-3.4E+38
- **Přesnost:** 6 desetinných míst

## Poznámka Anki 1641474185521

Karty Anki: 1641474185521
GUID: F=$WCFI_qo; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost, rozpětí a přesnost \(\mathtt{double}\)?

### Odpověď (Back)

- **Velikost:** 8 byte
- **Rozpětí:** 2.3E-308-1.7E+308
- **Přesnost:** 15 desetinných míst

## Poznámka Anki 1641474214651

Karty Anki: 1641474214651
GUID: O^jb=GHA,[; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost, rozpětí a přesnost \(\mathtt{long\ double}\)?

### Odpověď (Back)

- **Velikost:** 16 byte
- **Rozpětí:** 3.4E-4932-1.1E+4932
- **Přesnost:** 19 desetinných míst

## Poznámka Anki 1641474386018

Karty Anki: 1641474386018
GUID: z&=n<:-)FV; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaká je velikost pointeru?

### Odpověď (Back)

4 bytes na 32-bit OS a 8 bytes na 64-bit OS

## Poznámka Anki 1641475089014

Karty Anki: 1641475089014
GUID: f7KH_WUHd2; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak funguje interní reprezentace floating point čísel?

### Odpověď (Back)

\(x=(-1)^s \cdot m \cdot b^e\)

- báze \(b\), typicky \(b=2\)
- mantisa \(m\), \(1 \leq m < b\)
- exponent \(e\)
- znaménko \(s\), \(s \in \{0, 1\}\)

## Poznámka Anki 1641475261446

Karty Anki: 1641475261446
GUID: O%dU}P+01Q; štítky: bi-pa1::ustni.

### Otázka (Front)

Co je to skrytý bit u floating point čísel?

### Odpověď (Back)

Jedná se o první bit mantisy. Pokud je roven 1 je číslo normalizované.

## Poznámka Anki 1641476573965

Karty Anki: 1641476573965
GUID: K[P`pD)7Jj; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak funguje Bubble Sort a jaká je jeho složitost?

### Odpověď (Back)

Bubble Sort porovnává každé dva sousední prvky pole, když nejsou ve správném pořadí, tak je prohodí.

- nejhorší: \(O(n^2)\)
- nejlepší: \(O(n)\)

## Poznámka Anki 1641476727836

Karty Anki: 1641476727836
GUID: Ob%krc)A|Y; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak funguje Select Sort a jaká je jeho složitost?

### Odpověď (Back)

Najde nejmenší prvek ve zbytku pole a zamění jej s prvním prvkem. Poté pokračuje s polem o prvek menším.

- nejhorší \(O(n^2)\)
- nejlepší \(O(n^2)\)

## Poznámka Anki 1641476954689

Karty Anki: 1641476954690
GUID: lrw+%hWj3D; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak funguje Insert Sort a jaká je jeho složitost?

### Odpověď (Back)

Záčátkem je první prvek pole. Pokud uvažujeme jediný prvek jako samostatné pole, tak víme, že je vždy seřazeno. Poté vezme první prvek zbytku pole a zařadí jej do již seřazeného pole. Opakujeme dokud pole není seřazeno.

- nejhorší \(O(n^2)\)
- nejlepší \(O(n)\)

## Poznámka Anki 1641477281278

Karty Anki: 1641477281278
GUID: yEAGfkL^h8; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak funguje Merge Sort a jaká je jeho složitost?

### Odpověď (Back)

Pole o velikosti jednoho prvku je již seřazené. Pokud má pole více prvků, rozdělí se na dvě části. Rekurzivně zavoláme Merge Sort na obě poloviny a poté je sloučíme do jednoho seřazeného pole tak, že postupně vybíráme menší prvek z obou částí.
\(O(n \cdot \log(n))\)

## Poznámka Anki 1641477659097

Karty Anki: 1641477659098
GUID: Jb5gD8OY.D; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak funguje Quick Sort a jaká je jeho složitost?

### Odpověď (Back)

Určí se pivot, ideálně na hodnotu mediánu, ten ale není znám, a tak je často určován jako medián ze tří náhodných prvků. Pak je pole rozděleno na dvě části (ideálně dvě poloviny) a prvky se prohazují tak, aby dolní část obsahovala prvky menší než pivot a horní část prvky větší než pivot. Na obě poloviny se volá rekurzivě algorimus znovu.

- nejhorší - špatný výběr pivota, pole se zmenší pouze o jeden prvek: \(O(n^2)\)
- nejlepší \(O(n \cdot \log(n)\)

## Poznámka Anki 1641478642801

Karty Anki: 1641478642802
GUID: I]{qb,*xC_; štítky: bi-pa1::ustni.

### Otázka (Front)

Na co přepíšeme \(O(\log(n!))\)?

### Odpověď (Back)

\(O(n \cdot log(n))\)

## Poznámka Anki 1641564863288

Karty Anki: 1641564863298
GUID: CV^_#irB9W; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaký je výsledek operace \(\mathtt{-12\ \%\ 5}\)

### Odpověď (Back)

\(-2\)

## Poznámka Anki 1641564964624

Karty Anki: 1641564964624
GUID: dVzw3hF~L]; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaký je výsledek operace \(\mathtt{!\ x}\), \(\forall x \neq 0\)

### Odpověď (Back)

\(0\)

## Poznámka Anki 1641571520927

Karty Anki: 1641571520927
GUID: zlBBR40XAg; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak jdou po sobě řády růstu funkcí v \(O\)?

### Odpověď (Back)

\(O(1)\)
\(O(\log{\log{n}})\)
\(O(log{\ n})\)
\(O((\log n )^c) = O(\log^c n) \)
\(O(\sqrt{n})\)
\(O(n)\)
\(O(n \cdot log\ n) = O( \log\ n!)\)
\(O(n^2)\)
\(O(n^3)\)
\(O(2^n)\)
\(O(n!)\)
\(O(n^n)\)

## Poznámka Anki 1641601381079

Karty Anki: 1641601381080
GUID: I<0wq0|IQm; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak vyjádříme \(\log_n{(x)}\) pomocí \(\ln\)?

### Odpověď (Back)

\(\log_n{(x)} = \frac{\ln(x)}{\ln(n)}\)

## Poznámka Anki 1641601448101

Karty Anki: 1641601448101
GUID: j:Fpn[`%e6; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak zjednodušíme \(a^{\log_a{(b)}}\) ?

### Odpověď (Back)

\(a^{\log_a{(b)}} = b\)

## Poznámka Anki 1641765749453

Karty Anki: 1641765749453
GUID: exX6_Txr,3; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak přetypujeme porovnávací funkci při volání qsortu?

### Odpověď (Back)

\(\mathtt{(int(*)(const\ void\ *, const\ void\ *))}\)

## Poznámka Anki 1642017631554

Karty Anki: 1642017631564
GUID: iVZU&:T-uE; štítky: bi-pa1::ustni.

### Otázka (Front)

Jaký je doporučený komparátor pro qsort?

### Odpověď (Back)

\(\mathtt{(*b < *a) - (*a < *b)} \)

## Poznámka Anki 1642017757774

Karty Anki: 1642017757774
GUID: qM[,&DR|pa; štítky: bi-pa1::ustni.

### Otázka (Front)

Jak ideálně přiřadit \(\mathtt{mid}\) v binárním vyhledávání?

### Odpověď (Back)

\(\mathtt{mid = lo + ( hi - lo ) / 2}\)

## Poznámka Anki 1716737711213

Karty Anki: 1716737711213
GUID: lPVTym2xMe; štítky: bi-pa1 bi-spol::19.

### Otázka (Front)

Popište datový typ.

### Odpověď (Back)

Datový typ je vlastnost objektů, funkcí a výrazů programovacího jazyka, která definuje:

- interpretaci binární hodnoty objektu nebo výsledku výrazu,
- množinu možných hodnot,
- množinu použitelných operací.

Datové typy dělíme do následujících kategorií:

- **primitivní typy** - \(\mathtt{int}\), \(\mathtt{float}\), \(\mathtt{char}\);

- **strukturované typy** - pole, struktury;

- **ukazatele**,

- **jiné** - např. funkce.

## Poznámka Anki 1716737798173

Karty Anki: 1716737798173
GUID: joXJa5;+l1; štítky: bi-pa1 bi-spol::19.

### Otázka (Front)

Popište proměnnou.

### Odpověď (Back)

Proměnná je pojmenovaný objekt daného datového typu, jehož hodnota se může měnit.

## Poznámka Anki 1716738316053

Karty Anki: 1716738316053
GUID: GH^<%KG^gL; štítky: bi-pa1 bi-spol::19.

### Otázka (Front)

Popište statický a dynamický typový systém.

### Odpověď (Back)

V programovacím jazyku se **statickým typovým systémem** mají při kompilaci všechny proměnné známý typ. Příkladem takového jazyka je Rust, C nebo C++. Naopak v programovacích jazycích s **dynamickým typovým systémem** jsou typy přiřazovány až konkrétním hodnotám za běhu programu. Mezi takové jazyky patří Python, JavaScript nebo Perl.

## Poznámka Anki 1716739058447

Karty Anki: 1716739058448
GUID: edC3=ux$NC; štítky: bi-pa1 bi-spol::19.

### Otázka (Front)

Popište celočíselné datové typy.

### Odpověď (Back)

Celočíselné datové typy se používají pro reprezentaci celých čísel (\(\mathbb Z\)). Typicky je rozlišujeme dle rozsahu jejich hodnot:

- **znaménkové** - \(\texttt{short}\), \(\mathtt{int}\), \(\mathtt{long}\), \(\texttt{long long}\);

- **neznaménkové** - \(\texttt{unsigned short}\), \(\texttt{unsigned int}\), \(\texttt{unsigned long}\), \(\texttt{unsigned long long}\).

Mezi celočíselné datové typy patří také typy \(\texttt{bool} \) a \(\texttt{char}\). Pro reprezentaci záporných hodnot je běžně používán doplňkový kód.

## Poznámka Anki 1716739107268

Karty Anki: 1716739107268
GUID: hyY-`Cf|Tk; štítky: bi-pa1 bi-spol::19.

### Otázka (Front)

Popište datový typ \(\mathtt{char}\).

### Odpověď (Back)

Datový typ \(\mathtt{char}\) se používá pro reprezentaci znaků ASCII tabulky, které jsou kódovány jako celá čísla.

## Poznámka Anki 1716739986117

Karty Anki: 1716739986117
GUID: P5#TaWdNY@; štítky: bi-pa1 bi-spol::19.

### Otázka (Front)

Popište datové typy pohyblivé řádové čárky (floating point).

### Odpověď (Back)

Datové typy pohyblivé řádové čárky (floating point) se používají pro aproximaci reálných čísel (\(\mathbb R\)). Mají však omezenou přesnost a omezený rozsah. Na základě nich rozlišujeme datové typy \(\texttt{float}\), \(\texttt{double}\) a \(\texttt{long double}\). Reprezentované jsou typicky pomocí následujících složek:

- základ (base) \(b\),
- mantisa \(m\),
- exponent \(e\),
- znaménko (signum) \(s\).

Číslo \(x\) pak vyjádříme jako

\[x = (-1)^s \cdot m \cdot b^e,\]kde \(s \in \{ 0, 1 \}\) a běžně \(b = 2\).

## Poznámka Anki 1716740551495

Karty Anki: 1716740551495
GUID: u})sVOcP#w; štítky: bi-pa1 bi-spol::19.

### Otázka (Front)

Popište rozdíl mezi staticky a dynamicky alokovaným objektem.

### Odpověď (Back)

Mezi staticky a dynamicky alokovaným objektem jsou následující rozdíly:

| 
      **staticky alokovaný objekt** | 
      **dynamicky alokovaný objekt** | 

| 
      vzniká deklarací | 
      vzniká voláním specializované funkce (např. \(\texttt{malloc}\)) nebo operátoru (např. \(\texttt{new}\)) | 

| 
      známá velikost při kompilaci | neznámá velikost při kompilaci | 

| 
      alokován na zásobníku | 
      alokován na haldě | 

| 
      rychlejší správa paměti | 
      pomalejší správa paměti | 

| 
      automatické uvolnění paměti | 
      manuální uvolnění paměti (např. \(\texttt{free}\) a \(\texttt{delete}\)) |

## Poznámka Anki 1716740708209

Karty Anki: 1716740708209
GUID: sueg#vbSR8; štítky: bi-pa1 bi-spol::19.

### Otázka (Front)

Popište modul.

### Odpověď (Back)

Modul je část programu, která poskytuje funkcionalitu pro zbytek programu. Skládá se ze dvou částí:

- **specifikace** - objekty poskytované modulem (datové typy, funkce, třídy);
- **implementace** - implementace poskytovaných objektů.

V C a C++ jsou moduly definovány pomocí dvou typů souborů:

- **hlavičkové **(\(\texttt{.h}\) a \(\texttt{.hpp}\)) - specifikační část modulu;

- **implementační **(\(\texttt{.c}\) a \(\texttt{.cpp}\)) - implementační část modulu.

## Poznámka Anki 1716741654709

Karty Anki: 1716741654709
GUID: qF8mMRDBji; štítky: bi-pa1 bi-spol::19.

### Otázka (Front)

Popište funkci a proceduru.

### Odpověď (Back)

**Funkce **je podprogram řešící dílčí problém, který má definované rozhraní a lze jej volat opakovaně. Definována je zápisem
\[\texttt{type name (parameter list)}.\]**Procedura** je podprogram, který nevrací žádnou hodnotu. V C a C++ jsou procedury definovány stejně jako funkce s použitím datového typu \(\texttt{void}\).

## Poznámka Anki 1739041014075

Karty Anki: 1739041014075
GUID: A.hZs,GfcM; štítky: (žádné).

### Otázka (Front)

Regression to the mean

### Odpověď (Back)

Extrémní pozorování je následováno pozorováním bliže k průměru. Dávání přílišné váhy extrémnímu pozorování vede k selection bias.

