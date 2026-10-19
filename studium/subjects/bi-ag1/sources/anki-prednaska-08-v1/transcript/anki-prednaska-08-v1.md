# BI-AG1 – Přednáška 08

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 19 poznámek, 19 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1667810174541

Karty Anki: 1667810174541
GUID: _B8as#cS;; štítky: bi-ag1::p08 bi-spol::20.

### Otázka (Front)

Zařaďte algoritmus \(\mathtt{MergeSort}\).

### Odpověď (Back)

\(\mathtt{MergeSort}\) je out-of-place, stabilní a datově necitlivý.

## Poznámka Anki 1667810612725

Karty Anki: 1667810612725
GUID: ds>tu7@g7}; štítky: bi-ag1::p08 bi-spol::20.

### Otázka (Front)

Vyslovte a dokažte větu o časové složitosti algoritmu \(\mathtt{MergeSort}\).

### Odpověď (Back)

Časová složitost algoritmu \(\mathtt{MergeSort}\) je \(\Theta(n \log n)\).

**Důkaz**

- Rozdělení posloupností a slití seřazených kusů trvá čas \(c \cdot n\).

- Algotitmus volá \(2 \times\) sebe sama na vstupy velikosti \(\frac{n}{2}\). Proto

\[T(1) = 1,\]\[T(n) = 2 \cdot T(\frac{n}{2}) + cn.\]

- Po rozvinutí dostaneme:

\[T(n)= 2 \cdot (2 \cdot T(\frac{n}{4}) + \frac{cn}{2}) + cn = 4 \cdot T(\frac{n}{4}) + 2cn = 8 \cdot T(\frac{n}{8}) + 3cn = \dots = 2^k \cdot T(\frac{n}{2^k}) + kcn.\]

- Rekurze skončí, když \(\frac{n}{2^k} = 1\) čili \(k = \log n\). Tím dostaneme \(T(n) = 2^{\log n} \cdot T(1) + \log n \cdot cn = \Theta(n) + cn \log n = \Theta(n \log n)\).

## Poznámka Anki 1667810892487

Karty Anki: 1667810892487
GUID: Q3PO{7Osb?; štítky: bi-ag1::p08 bi-spol::20.

### Otázka (Front)

Vyslovte a dokažte větu o paměťové složitosti algoritmu \(\mathtt{MergeSort}\).

### Odpověď (Back)

- \(\mathtt{MergeSort}\) si pamatuje lokální proměnné: vstup a jejich setříděné poloviny, dohromady \(\Theta(n)\) paměti. Plus kontext pro návrat z rekurzivního zanoření (\(\mathcal{O}(1)\) paměti).
- Mimo to obě rekurzivní volání spotřebují další paměť, ale jelikož vždy běží pouze jedno z nich, stačí započítat pouze jedno.
- Dostaneme tuto rekurentní rovnici (pro kladnou konstantu \(d\)):
\[M(1) = 1,\]\[M(n) = dn + M (\frac{n}{2})\]

- To nám pro \(M(n)\) dává geometrickou řadu \(dn + \frac{dn}{2} + \frac{dn}{4} + \dots\) , která má součet \(\Theta(n)\).

## Poznámka Anki 1667815680566

Karty Anki: 1667815680566
GUID: M;Yz,2*8Yz; štítky: bi-ag1::p08 bi-spol::21.

### Otázka (Front)

Formulujte problém rekurzivního násobení dvou celých čísel.

### Odpověď (Back)

- Mějme dvě \(n\)-ciferná čísla \(x\) a \(y\), která chceme vynásobit (pro jednoduchost nechť je \(n\) mocina dvou).
- Obě čísla rozdělíme na \(\frac{n}{2}\) horních a \(\frac{n}{2}\) dolních cifer (\(x_U, x_L, y_U, y_L\) jsou \(\frac{n}{2}\)-ciferná čísla):

\[x = x_U \cdot 10^{\frac{n}{2}} + x_L,\]\[y = y_U \cdot 10^{\frac{n}{2}} + y_L.\]

- Výsledný součin dvou \(n\)-ciferných čísel \(xy\) pak můžeme poskládat ze \(4\) součinů \(\frac{n}{2}\)-ciferných čísel:

\[xy = x_U \cdot y_U \cdot 10^n + (x_U \cdot y_L + x_L \cdot y_U) \cdot 10^{\frac{n}{2}} + x_L \cdot y_L.\]

## Poznámka Anki 1667816895540

Karty Anki: 1667816895540
GUID: FVi+bIN]bI; štítky: bi-ag1::p08 bi-spol::21.

### Otázka (Front)

Vyslovte a dokažte větu o časové složitosti Karacubova algoritmu rekurzivního násobení dvou celých čísel.

### Odpověď (Back)

- Karacubův algoritmus proádí pouze \(3\) násobení čísel poloviční délky, kde základní algoritmus provádí \(4\).
- Formuli násobení dvou čísel jde totiž zapsat také jako:

\[x_U \cdot y_U \cdot 10^n + \big((x_U + x_L) \cdot (y_U + y_L) - x_U \cdot y_U - x_L \cdot y_L \big) \cdot 10^{\frac{n}{2}} + x_L \cdot y_L.\]

- Počet násobení se tedy snížil a přibily \(2\) operace sčítání, ale ty mají pouze lineární složitost.
- **Časová složitost Karacubova algoritmu tedy je **\(\Theta(n^{\log 3}) \approx \Theta(n^{1,59})\).

**Důkaz**

- Počet operací je:

\[T(1) = 1,\]\[T(n) = 3 \cdot T(\frac{n}{2}) + \Theta(n).\]

- Strom rekurzivních volání vypadá takto:

- Na \(i\)-té hladině je \(3^i\) vrcholů s \(\frac{n}{2^i}\)-cifernými problémy.
- Na \(i\)-té hladině nyní dohromady trávíme čas \(\Theta\bigg(n \cdot \Big(\frac{3}{2}\Big)^i\bigg)\).
- Hloubka stromu je \(\log n\).
- V součtu přes všechny hladiny dostaneme:

\[T(n) = \Theta \Bigg( n \cdot \bigg( \Big(\frac{3}{2}\Big)^0 + \Big(\frac{3}{2}\Big)^1 + \cdots + \Big(\frac{3}{2}\Big)^{\log n} \bigg) \Bigg) \]

- Člen \(n\) se násobí s gemetrickou řadou s koeficientem \(\frac{3}{2}\), která se (pokud zanedbáme konstanty) sečte na \(\Big( \frac{3}{2} \Big)^{\log n}\), což lze upravit na \(n^{\log(3) - 1}\).
- Časová složitost tedy činí \(\Theta(n \cdot n^{\log(3) - 1}) = \Theta(n^{\log 3}) \approx \Theta(n^{1,59})\).

## Poznámka Anki 1667817265245

Karty Anki: 1667817265245
GUID: mWs&q~o9e!; štítky: bi-ag1::p08 bi-spol::20.

### Otázka (Front)

Popište algoritmus \(\mathtt{QuickSelect}\).

### Odpověď (Back)

**Vstup**
Neseřazená posloupnost \(X\) o velikosti \(n\) prvků a číslo \(k\), \(k \leq n\).

**Výstup**
\(k\)-tý nejmenší prvek v \(X\).

**Postup**

- Ze vstupní posloupnosti \(X\) vybereme **pivot **a posloupnost rozdělíme na tři části:

- **levou** (\(L\)) - prvky menší než pivot,

- **prostřední **(\(S\)) - prvky rovné pivotu,

- **pravou** (\(P\)) - prvky větší než pivot.

- Pak platí:

- Je-li \(k \leq |L|\), pak je hledaný prvek \(k\)-tý nejmenší prvek v části \(L\).
- Je-li \(|L| < k \leq |L| + |S|\), je hledaný prvek roven pivotu.
- Je-li \(k > |L| + |S|\), je hledaný prvek \((k - |L| - |S|)\)-tý nejmenší prvek v části \(P\).

- Rekurzivně opakujeme volání na část, která podle vztahů výše prvek obsahuje.

## Poznámka Anki 1667818555044

Karty Anki: 1667818555044
GUID: Mjx.i5VQS%; štítky: bi-ag1::p08 bi-spol::20.

### Otázka (Front)

Analyzujte časovou složitost algoritmu \(\mathtt{QuickSelect}\) a popište vliv volby pivotu.

### Odpověď (Back)

- Rozdělení vstupní posloupnosti na \(L\), \(S\) a \(P\) trvá lineární čas.
- Pak se \(\mathtt{QuickSelect}\) rekurzivně volá na část \(L\) nebo \(P\).
- Pivot ovlivňuje **o kolik bude tato část menší než **\(n\).

**Nejhorší případ**

- Hledejme \(k=1\) a za pivot zvolme největší prvek vstupu.
- \(\mathtt{QuickSelect}\) budeme rekurzivně volat na \(L\), kde ale \(|L| = n-1\) (vyloučili jsme pouze jeden prvek).

- Pokud se pivot bude volit tímto způsobem nadále získáme složitost

\[\Theta(n) + \Theta(n-1) + \cdots + \Theta(1) = \Theta(n^2).\]

**Nejlepší případ**

- Ideální volbou pivota by byl medián, pak by \(|L|\) i \(|P|\) byla nejvýše \(\lfloor \frac{n}{2} \rfloor\).
- Pokud bychom mediáln byli schopni nalézt v lineárním čase, získali bychom složitost

\[\Theta(n) + \Theta \Big(\frac{n}{2}\Big) + \Theta \Big(\frac{n}{4}\Big) + \cdots + \Theta(1) = \Theta(n).\]

**Skutečný případ**

- K nejlepšímu případu se můžeme přiblížit tak, že místo mediánu použijeme skoromedián (prvek, který je kdekoli v prostředních dvou čtvrtinách seřazené posloupnosti).
- Skoromedián má nalevo i napravo vždy nejvýše \(\frac{3}{4} \cdot n\) prvků.
- Skoromedián vybíráme náhodně. Pravděpodobnost, že se strefíme je \(\frac{1}{2}\), ve střední hodnotě tedy \(2\) pokusy. Pak ješte musíme ověřit, je jde skutečne o skoromedián, což zabere \(\Theta(n)\). Případně volbu opakujeme.
- Získáváme tedy složitost

\[\mathcal{O}(n) + \mathcal{O}\Big(\frac{3}{4} \cdot n\Big) + \mathcal{O}\Big(\Big(\frac{3}{4}\Big)^2 \cdot n\Big) + \cdots + \mathcal{O}(1) = \mathcal{O}(n).\]

## Poznámka Anki 1667818689315

Karty Anki: 1667818689315
GUID: NNF$=mL{?_; štítky: bi-ag1::p08.

### Otázka (Front)

Co když nemůžeme v algoritmu \(\mathtt{QuickSelect}\) ovlivňit strategii volby pivota, ale stále požadujeme časovou složitost \(\mathcal{O}(n)\)?

### Odpověď (Back)

- Předpokládejme, že je volba pivota vždy deterministická a fixní.
- Pak postačí dokonale přepermutovat vstupní posloupnost.

## Poznámka Anki 1674082069934

Karty Anki: 1674082069935
GUID: w?tI:cgkot; štítky: bi-ag1::p08.

### Otázka (Front)

Vyslovte a dokažte větu o časové složitosti algoritmu \(\mathtt{QuickSelect}\) s náhodnou volbou pivota.

### Odpověď (Back)

Střední hodnota počtu výpočetních operací vykonaných algoritmem \(\mathtt{RandomPivotQuickSelect}(x_1, \dots, x_n; k)\) s náhodným výběrem pivota je \(O(n)\).

**Důkaz**

- Rozdělíme běh algoritmu \(\mathtt{RandomPivotQuickSelect}\) na fáze podle hloubky rekurze.

- V každé fázi zvolíme náhodně pivota, což zahrnuje ověření v lineárním čase, že se jedná o skoromedián. Pak provedeme v lineárním čase rozdělení na \(L\), \(S\), \(P\) a pokud neskončíme, půjdeme do další rekurzivní fáze s \(L\) nebo \(P\) na vstupu.
- Během každé fáze se vstup zmenší nejméně o čtvrtinu.
- V \(i\)-té fázi je tedy na vstupu nejvýše \(\Big(\frac 3 4 \Big)^i \cdot n\) prvků.
- Definujeme náhodnou veličinu \(T_i\) jako počet výpočetních operací (přesunů, porovnání, atd.) \(i\)-té fáze.
- Pak platí

\[\mathbf E[T_i] \leq \Big(\frac 3 4\Big)^{i - 1} \cdot \Theta(n) \cdot \mathbf E[\text{\# pokusů k nalezení skoromediánu}] \leq \Big(\frac 3 4\Big)^{i - 1} \cdot \Theta(n) \cdot 2.\]

- Náhodná veličina celkového počtu operací algoritmu \(T\) je tedy \(T = T_1 + T_2 + \dots + T_l\), kde \(l = \Theta(\log n)\).
- Využitím linearity střední hodnoty dostaneme

\[\mathbf E[T] = \mathbf E[T_1 + \dots + T_l] = \mathbf E[T_1] + \dots + \mathbf E[T_l] \leq \sum \limits_{i = 1}^l \Big( \frac 3 4 \Big)^{i - 1} \cdot \Theta(n) = \Theta(n).\]

- Tedy i v nejhorším případě skoromediánu na hranicích vnitřních dvou čtvrtin vstupní posloupnosti je střední hodnota počtu výpočetních operací \(\mathcal O(n)\), což je optimální složitost.

## Poznámka Anki 1716397268311

Karty Anki: 1716397268312
GUID: xv(|uwecH); štítky: bi-ag1::p08 bi-spol::20 bi-spol::21.

### Otázka (Front)

Popište algoritmus \(\mathtt{QuickSort}\).

### Odpověď (Back)

**Vstup** 

- neseřazené pole \(X = x_1, \dots, x_n\)

**Výstup** 

- seřazené pole \(Y = y_1, \dots, y_n\)

**Postup** 

- Pokud \(n \leq 1\), vrátíme \(X\).
- Zvolíme pivot \(p\) a rozdělíme \(X\) na tři části:

- levou (\(L\)) - prvky menší než \(p\);
- střední (\(S\)) - prvky rovné \(p\);
- pravou (\(P\)) - prvky větší než \(p\).

- Rekurzivním voláním seřadíme \(L\) a \(P\):

\[\begin{matrix}
L := \texttt{QuickSort}(L),\\
P := \texttt{QuickSort}(P).
\end{matrix}\]

- Části spojíme za sebe a vrátíme:

\[Y = L, S, P.\]

**Složitost** 

- Časová složitost algoritmu je \(\mathcal O(n \log n)\).

## Poznámka Anki 1716404968652

Karty Anki: 1716404968652
GUID: g@}M3tI,i,; štítky: bi-ag1::p08 bi-spol::21.

### Otázka (Front)

Popište metodu divide-and-conquer (rozděl a panuj). Uveďte příklady jejího využití.

### Odpověď (Back)

Divide-and-conquer je metoda návrhu algoritmů, při které je zadaný problém rekurzivně dělen na podproblémy řešitelné stejným nebo podobným způsobem, dokud není dosaženo triviální instance problému, kterou je možné vyřešit přímo. Řešení zadaného problému je následně složeno z řešení jeho podproblémů. Tuto metodu lze využít v řadících algoritmech (\(\mathtt{MergeSort}\), \(\mathtt{QuickSort}\)) nebo při rychlém násobení celých čísel (Karacubův algoritmus).

## Poznámka Anki 1716405349463

Karty Anki: 1716405349463
GUID: Lx_p4J$c6Q; štítky: bi-ag1::p08 bi-spol::04 bi-spol::21.

### Otázka (Front)

Popište rekurzi. Uveďte příklady jejího využití.

### Odpověď (Back)

Rekurze je metoda řešení problémů, jejichž řešení závisí na řešeních menších podproblémů řešitelných stejným nebo podobným způsobem. Vyznačuje se tím, že používá rekurzivní funkce, což jsou funkce, které ve svém kódu volají sebe samy. Pro použití rekurze musí být splněny dvě podmínky:

- rekurzivní volání řeší menší instanci původního problému;
- existuje triviální instance problému, u které rekurze skončí.

Rekurzi lze využít při výpočtu faktoriálu, Fibonacciho posloupnosti nebo v operacích nad binárními vyhledávacími stromy.

## Poznámka Anki 1716406137954

Karty Anki: 1716406137954
GUID: y)Pu&;40oA; štítky: bi-ag1::p08 bi-spol::21 duplicate.

### Otázka (Front)

Popište dynamické programování. Uveďte příklady jeho využití.

### Odpověď (Back)

Dynamické programování je metoda návrhu algoritmů, která se stejně jako divide-and-conquer zakládá na rekurzivním rozkladu problému na podproblémy řešitelné stejným nebo podobným způsobem. Na rozdíl od divide-and-conquer však předpokládá a využívá toho, že se podproblémy v rekurzivním rozkladu opakují. Za použití memoizace lze pomocí dynamického programování dosáhnout výrazného zrychlení algoritmů. Dynamické programování lze využít při výpočtu faktoriálu, Fibonacciho posloupnosti nebo při konstrukci nejdelší rostoucí podposloupnosti.

## Poznámka Anki 1716406702289

Karty Anki: 1716406702289
GUID: OAGO(@zw|D; štítky: bi-ag1::p08 bi-spol::21.

### Otázka (Front)

Popište memoizaci.

### Odpověď (Back)

Memoizace je optimizační technika, která dosahuje zrychlení algoritmů ukládáním výsledků náročných operací. Namísto toho, aby byla náročná operace prováděna opakovaně, jsou použity uložené výsledky. Memoizace je využívána zejména v dynamickém programování, které předpokládá, že se v rekurzivním rozkladu problému na podproblémy jednotlivé podproblémy opakují.

## Poznámka Anki 1716406827506

Karty Anki: 1716406827506
GUID: b*dvEGR42_; štítky: bi-ag1::p08 bi-spol::21.

### Otázka (Front)

Popište postup dynamického programování a memoizace algoritmu.

### Odpověď (Back)

Postup memoizace algoritmu je následující:

- formulujeme řešení pomocí rekurzivního rozkladu na podproblémy;
- navrhneme rekurzivní algoritmus;
- identifikujeme opakované podproblémy;
- vytvoříme prázdnou tabulku ukládající řešení podproblémů;
- do tabulky vložíme řešení triviálních instancí problému;
- před výpočtem každého podproblému zkontrolujeme odpovídající políčko tabulky:

- pokud je již vypočtené, použijeme jeho hodnotu;
- v opačném případě vyřešíme podproblém pomocí rekurze a zapíšeme výsledek do políčka.

## Poznámka Anki 1716407134236

Karty Anki: 1716407134236
GUID: b8n[hBq)Ys; štítky: bi-ag1::p08 bi-spol::21.

### Otázka (Front)

Porovnejte rekurzivní a iterativní řešení problémů.

### Odpověď (Back)

Rekurzivní řešení problémů vede na výpočet „shora dolů,“ při kterém řešení problémů vyvolává řešní podproblémů a vyplňování jejich políček v memoizační tabulce. Iterativní řešení probíhá „zdola nahoru,“ tedy začíná u triviálních instancí a postupně přechází k složitějším.** **

## Poznámka Anki 1716407691239

Karty Anki: 1716407691239
GUID: qABz:vG_h&; štítky: bi-ag1::p08 bi-spol::21.

### Otázka (Front)

Popište výhody a nevýhody rekurzivních algoritmů.

### Odpověď (Back)

Mezi výhody rekurzivních algoritmů patří:

- **úspornost** - kratší zdrojový kód,

- **přirozenost **a **intuitivnost** - využívá přirozeného opakování podproblémů,
- **expresivnost** - složitost lze vyjádřit pomocí rekurentních rovnic a analyzovat.

Mezi jejich nevýhody patří:

- **prostor na zásobníku** - hluboká rekurze může být násilně ukončena kvůli stack overflow,

- **výkon** - volání funkcí s sebou nese výkonnostní overhead.

## Poznámka Anki 1716564347431

Karty Anki: 1716564347432
GUID: tnjGC2K({i; štítky: bi-ag1::p08 bi-spol::20 bi-spol::21.

### Otázka (Front)

Popište algoritmus \(\mathtt{MergeSort}\).

### Odpověď (Back)

**Vstup** 

- neseřazené pole \(X = x_1, \dots, x_n\)

**Výstup** 

- seřazené pole \(Y = y_1, \dots, y_n\)

**Postup** 

- Pokud \(n \leq 1\), vrátíme \(X\).
- Posloupnost rozdělíme na levou a pravou polovinu a rekurzivním voláním seřadíme:

\[\begin{matrix}
l_1, \dots, l_{\lfloor \frac n 2 \rfloor} := \mathtt{MergeSort}(x_1, \dots, x_{\lfloor \frac n 2 \rfloor}),\\
r_1, \dots, r_{\lceil \frac n 2 \rceil} := \mathtt{MergeSort}(x_{\lfloor \frac n 2 \rfloor + 1}, \dots, x_n).
\end{matrix}\]

- Poloviny spojíme do jedné seřazené posloupnosti a vrátíme:

\[Y = y_1, \dots, y_n := \mathtt{Merge}(l_1, \dots, l_{\lfloor \frac n 2 \rfloor}; r_1, \dots, r_{\lceil \frac n 2 \rceil})\]**Složitost**

- Časová složitost algoritmu je \(\Theta (n \log n)\).
- Paměťová složitost algoritmu je \(\Theta (n)\).

### Doplňující pole (Extra)

Funkce \(\mathtt{Merge}\) na vstupu dostává dvě seřazené posloupnosti délek \(m\) a \(n\), které spojí do jedné seřazené posloupnosti s časovou a paměťovou složitostí \(\Theta ( m + n)\).

## Poznámka Anki 1718546238955

Karty Anki: 1718546238955
GUID: o;/Vmb*`;%; štítky: bi-ag1::p08 bi-spol::21.

### Otázka (Front)

Popište koncovou rekurzi (tail recursion).

### Odpověď (Back)

Koncová rekurze (tail recursion) je typ rekurze, ve které je posledním příkazem rekurzivní funkce rekurzivní volání sebe sama. Tyto funkce tedy neprovádí žádné odložené operace po návratu z rekurzivního volání. Pokud to překladač umožňuje, dokáže koncová rekurze šetřit místo na zásobníku a navíc ji vždy lze převést na iteraci.

