# BI-AG1 – Přednáška 09

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1668421609914

Karty Anki: 1668421609914
GUID: gO`POY?/H_; štítky: bi-ag1::p09 bi-spol::20.

### Otázka (Front)

Naznačte důkaz věty o časové složitosti algoritmu \(\mathtt{QuickSort}\) s náhodnou volbou pivota.

### Odpověď (Back)

- Označme \(X = x_1, x_2, \dots, x_n\) vstupní posloupnost a \(Y = y_1, y_2, \dots, y_n\) seřazenou výstupní posloupnost.
- Budeme určovat střední počet porovnání v průběhu algoritmu \(\mathtt{QuickSort}\).
- Protože pivota volíme náhodně, je porovnání \(y_i\) s \(y_j\) náhodný jev.
- Pro \(1 \leq i < j \leq n\) zavedeme náhodné veličiny \(C_{ij}\) takto:

\[C_{ij} = \begin{cases}
1 & \text{pokud během řažení došlo k porovnání } y_i \text{ s } y_j, \\
0 & \text{jinak.}
\end{cases}\]

- Poté určíme, že \(\boldsymbol{P}[C_{ij} = 1] = \frac{2}{j-i+1}\) a

\[\boldsymbol{E}[C] = \boldsymbol{E}[ \sum \limits_{1 \leq i < j \leq n} C_{ij}] = \mathcal{O}(n \log n).\]

## Poznámka Anki 1668421974527

Karty Anki: 1668421974527
GUID: EGF$<G/AbX; štítky: bi-ag1::p09 bi-spol::20.

### Otázka (Front)

Vyslovte a dokažte větu o časové složitosti algoritmu \(\mathtt{QuickSort}\) s deterministickou volbou pivotu a náhodnými vstupy.

### Odpověď (Back)

Uvažujme na vstupu rovnoměrně náhodné permutace \(\set{1, \dots, n}\). Jako pivota volíme vždy prvek např. na prostřední pozici. Potom střední hodnota počtu operací vykonaných při jednom běhu algoritmu \(\mathtt{QuickSort}\) je \(\mathcal{O}(n \log n)\).

**Důkaz**

- Vzhledem k náhodnosti vstupu je prostřední prvek rovnoměrně náhodně vybrané číslo z množiny \(\set{1, 2, \dots, n}\).

- Po rozdělení vstupu na levou a pravou část budou obě části opět náhodné permutace, na nichž se algoritmus chová stejně.
- Lze tedy použít stejnou analýzu jako ve Větě o složitosti algoritmu \(\mathtt{QuickSort}\) s náhodnou volbou pivotu.

## Poznámka Anki 1668422268906

Karty Anki: 1668422268906
GUID: NTd%q==KyI; štítky: bi-ag1::p09 bi-spol::20.

### Otázka (Front)

Definujte porovnávací model RAM.

### Odpověď (Back)

Porovnávací model RAM má stejné vlastnosti jako obecný model RAM, ale navíc platí, že prvky zadané posloupnosti můžou být pouze vzájemně porovnávány operací \(\mathtt{cmp}(a_i, a_j)\) nebo přesouvány (či kopírovány) v paměti, kde operace \(\mathtt{cmp}(a_i, a_j)\) je binární operace, která v konstantním čase rozhodne, která z nerovností (\(<\), \(>\), \(=\)) mezi prvky \(a_i\), \(a_j\) platí.

## Poznámka Anki 1668422449791

Karty Anki: 1668422449791
GUID: xVUu<KK7]Y; štítky: bi-ag1::p09 bi-spol::20.

### Otázka (Front)

Definujte problém vyhledávání.

### Odpověď (Back)

**Vstup**
Číslo \(n\), vzestupně seřazená posloupnost \(A\) o \(n\) číslech \(a_1, \dots, a_n\) a hledané číslo \(x\).

**Výstup
**Odpověď na otázku, zda se \(x\) vyskytuje v \(A\).

## Poznámka Anki 1668422953139

Karty Anki: 1668422953139
GUID: Naytm0>Fm*; štítky: bi-ag1::p09 bi-spol::20.

### Otázka (Front)

Vyslovte a dokažte větu o dolní mezi časové složitosti problému vyhledávání.

### Odpověď (Back)

Dolní mez složitosti problému vyhledávání je \(\Omega(\log n)\) operací porovnávání.

**Důkaz**

- Dokážeme, že pro libovolný deterministický vyhledávací algoritmus \(S\) a pro libovolné \(n\) a pro libovolnou vstupní vzestupně seřazenou posloupnost \(A = a_1 < a_2 < \cdots < a_n\) existuje \(x\) takové, že algoritmus \(S\) při hledání \(x\) v posloupnosti \(A\) provede \(\Omega(\log n)\) porovnání.
- První porovnání, které algoritmus \(S\) se vstupem \(A\) provede, bude vždy stejné, neboť je deterministický.
- Porovnání typu \(\mathtt{cmp}(a_i, a_j)\) dopadne také vždy stejně.
- Až první porovnání typu \(\mathtt{cmp}(x, a_i)\) může pro různá vstupní \(x\) dopadnout různě.
- Pro každý z možných výsledků tohoto porovnání pokračuje \(S\) deterministicky, takže algoritmem \(S\) je pevně dáno, které další porovnání se provede.
- A tak dále, až se \(S\) zastaví s výsledkem buď \(x \in A\) nebo \(x \notin A\).
- Protože \(S\) je deterministický algoritmus, můžeme jeho provedení se vstupem \(A\) pro všechna možná \(x\) popsat takzvaným rozhodovacím stromem \(T_{S,A}\).

- Každý vnitřní vrchol rozhodovacího stromu \(T_{S,A}\) je porovnání typu \(\mathtt{cmp}(x, a_i)\) a má tedy obecně tři syny, kteří odpovídají možným výsledkům tohoto porovnání (\(<\), \(=\), \(>\)).
- Může se stát, že některý z výsledků nemůže vzniknout, protože by byl ve sporu s dříve provedenými porovnáními. V takovém případě příslušný syn neexistuje (je prázdný).
- V listech \(T_{S,A}\) jsou jednotlivé výsledky hledání: buď pozice v \(A\), na které se \(x\) vyskytuje, nebo odpověď, že \(x\) v \(A\) neexistuje.

- Každé možné provedení algoritmu \(S\) se vstupem \(A\) pro nějaké \(x\) odpovídá nějaké cestě z kořene \(T_{S,A}\) do listu.
- Rozhodovací strom \(T_{S,A}\) je tedy ternární (vrcholy mají nejvýše 3 syny) s nejméně \(n + 2\) listy a s nejvýše \(2n + 1\) listy.

- Protože každý ternární strom hloubky \(h\) má nejvýše \(3^h\) listů, má \(T_{S,A}\) hloubku nejméně \(\log_3 n\).

- V \(T_{S,A}\) tedy existuje cesta délky nejméně \(\log_3 n\) a proto existuje \(x\), které této cestě odpovídá.

- \(A\) takové \(x\) „donutí“ \(S\) vykonat nejméně \(\log_3 n\) porovnání.

 [Obrázek: paste-6df519621c1d2dc1f6a2997adacfedd633ce1dce.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1668423515320

Karty Anki: 1668423515320
GUID: s.+za_jH;#; štítky: bi-ag1::p09 bi-spol::20.

### Otázka (Front)

Vyslovte a dokažte větu o dolní mezi časové složitosti problému řazení.

### Odpověď (Back)

Každý deterministický algoritmus v porovnávacím modelu, který seřadí \(n\)-prvkovou posloupnost, použije v nejhorším případě \(\Omega(n \log n)\) porovnání.

**Důkaz**

- Zvolme pevné \(n\) a uvažujme vstupy \(A = a_1, \dots, a_n\), které jsou permutacemi množiny \(\set{1, \dots, n}\).
- Ukážeme, že pro libovolný řadicí algoritmus \(S\) v porovnávacím modelu existuje „těžký“ vstup \(A\), který „donutí“ \(S\) provést \(\Omega(n \log n)\) porovnání.
- Upravíme \(S\) tak, aby nejprve prováděl všechna porovnání a teprve na konec prvky přeindexoval.

- Každý prvek si tedy pouze pamatuje průběžně novou pozici a na výslednou pozici se přesune až nakonec.

- Sestrojíme rozhodovací strom \(T_S\) popisující všechny možné průběhy algoritmu \(S\), tedy běhy pro všechny možné permutace.
- Vnitřní vrcholy \(T_S\) jsou porovnání \(\mathtt{cmp}(a_i, a_j)\) se dvěma možnými výsledky (rovnost tentokrát nenastane díky volbě vstupní posloupnosti).
- Vynecháme výsledky, které jsou ve sporu s předchozími porovnáními.
- V listu stromu algoritmus \(S\) provede napočítané prohození a zastaví se.
- Pro různé vstupní permutace \(A\) musí algoritmus \(S\) skončit v různých listech \(T_S\) (dvě různé permutace nelze seřadit toutéž posloupností přesunů prvků).

- \(T_S\) je tedy binární kořenový strom s \(n!\) listy, takže musí mít hloubku nejméně \(\log(n!)\), tedy \(\Omega(n \log n)\).

- Proto musí existovat vstupní permutace \(A\), pro kterou \(S\) provede \(\Omega(n \log n)\) porovnání.

 [Obrázek: paste-8619fc8c01ca2f24dd6dbefc3c7a5d878f3cd37a.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1668423878990

Karty Anki: 1668423878991
GUID: nBeZ}n6&g<; štítky: bi-ag1::p09 bi-spol::20.

### Otázka (Front)

Popište algoritmus \(\mathtt{CountingSort}\) a uveďte jeho časovou a paměťovou složitost.

### Odpověď (Back)

\(\texttt{CountingSort}\) je speciální algoritmus řazení, který je out-of-place, stabilní a datově necitlivý.

**Vstup** 

- neseřazené pole \(X = x_1, \dots x_n\) celých čísel z množiny \(\{ 1, \dots, r \}\)

**Výstup** 

- seřazené pole \(Y = y_1, \dots, y_n\)

**Postup** 

- V prvním průchodu \(X\) je pro každé číslo z množiny \(\{ 1, \dots, r \}\) spočteno, kolikrát se v \(X\) vyskytuje.
- Pomocí prefixového součtu jsou poté za pomocí počtů výskytů spočteny pozice v \(Y\), na kterých se budou po seřazení pole nacházet začátky oblastí tvořených stejnými čísly z množiny \(\{ 1, \dots, r \}\).
- V druhém průchodu \(X\) je pro každý jeho prvek určena pozice, na které má ležet v \(Y\), a na tuto pozici je přesunut.

**Složitost** 

- Časová i paměťová složitost algoritmu je \(\Theta (n + r)\).

## Poznámka Anki 1669019181775

Karty Anki: 1669019181775
GUID: J@G7=F<PmI; štítky: bi-ag1::p09.

### Otázka (Front)

Popište algoritmus \(\mathtt{LexCountingSort}\).

### Odpověď (Back)

- Mějme \(n\) uspořádaných \(k\)-tic \(X_1, \dots, X_n\) prvků z množiny \(\set{1, \dots, r}\) (čili \(X_i \in \set{1, \dots, r}^k\)).
- Souřadnice \(k\)-tic číslujeme zleva doprava od jedné: \(X_i = (x_{i,1}, x_{i,2}, \dots, x_{i,k})\).
- Využijeme toho, že \(\mathtt{CountingSort}\) je stabilní, a řadíme takto:

- \(\mathtt{LexCountingSort}(k\)-tice \(X_1, \dots, X_n)\)

- \(S := X_1, \dots, X_n\)

- Pro \(i:= x, \dots, 1:\)

- \(S:= \mathtt{CountingSort}(S)\) podle souřadnice \(i\)

- Vrať \(S\)

## Poznámka Anki 1669019424686

Karty Anki: 1669019424686
GUID: q(@PDo<2ms; štítky: bi-ag1::p09.

### Otázka (Front)

Vyslovte a dokažte větu o korektnosti algoritmu \(\mathtt{LexCountingSort}\).

### Odpověď (Back)

Algoritmus \(\mathtt{LexCountingSort}\) řadí vstupní \(k\)-tice správně lexikograficky a je stabilní.

**Důkaz**

- Dokážeme indukcí přes číslo souřadnice následující invariant:

- Po provedení iterace cyklu s číslem \(i\) platí, že vstupní pole \(k\)-tic ořezaných na \(i\)-tou až \(k\)-tou souřadnici je lexikograficky seřazené.

- **IZ**: Platí evidentně pro první iteraci s \(i = k\), kdy v \(S\) jsou hodnoty seřazeny podle poslední souřadnice.
- **IK**: Předpokládejme, že invariant platí pro všechna \(j\), \(i < j \leq k\).
- Řazení v iteraci s číslem \(i\) posouvá dopředu v pořadí nejprve \(k\)-tice mající na souřadnici \(i\) hodnotu \(1\), pokud existují.
- Protože tyto \(k\)-tice oříznuté na (\(i + 1\))-tou až \(k\)-tou souřadnici byly v předchozích iteracích seřazeny správně a \(\mathtt{CountingSort}\) je stabilní, bude tato skupina \(k\)-tic oříznutých na \(i\)-tou až \(k\)-tou souřadnici také seřazena správně.

- Pak bude podobným způsobem případně následovat skupina \(k\)-tic, majících na souřadnici \(i\) hodnotu \(2\), pak \(3\), atd.

- Po skončení iterace cyklu s číslem \(i\) budou tedy \(k\)-tice oříznuté na \(i\)-tou až \(k\)-tou souřadnici seřazeny správně.

## Poznámka Anki 1669019498142

Karty Anki: 1669019498143
GUID: v;p_/CXi:*; štítky: bi-ag1::p09.

### Otázka (Front)

Jaká je časová a paměťová složitost algoritmu \(\mathtt{LexCountingSort}\).

### Odpověď (Back)

Časová složitost \(\mathtt{LexCountingSort}\) je \(\Theta(k \cdot (n + r))\), což je lineární s délkou vstupu \((k \cdot n)\) pro pevné \(k\) a \(r\). Paměťová složitost činí \(\Theta(kn + r)\).

## Poznámka Anki 1672052090692

Karty Anki: 1672052090692
GUID: yk:7R%|T)o; štítky: bi-ag1::p09 bi-spol::20.

### Otázka (Front)

Zařaďte algoritmy \(\mathtt{SelectSort}\), \(\mathtt{BubbleSort}\), \(\mathtt{InsertSort}\), \(\mathtt{MergeSort}\) a \(\mathtt{CountingSort}\).

### Odpověď (Back)

| 
      \(\mathtt{BubbleSort}\)
 | 
      \(\mathtt{InsertSort}\)
 | 
      \(\mathtt{SelectSort}\)
 | 
      \(\mathtt{CountingSort}\)
 | 
      \(\mathtt{MergeSort}\)
 | 

| 
      in-place | 
      in-place | 
      in-place | 
      out-of-place | 
      out-of-place | 

| 
      stabilní | 
      stabilní | 
      nestabilní | 
      stabilní | 
      stabilní | 

| 
      datově citlivý | 
      datově citlivý | 
      datově necitlivý | 
      datově necitlivý | 
      datově necitlivý | 

| 
      \(\mathcal O(n^2)\)
 | 
      \(\mathcal O(n^2)\)
 | 
      \(\Theta(n^2)\)
 | 
      \(\Theta(n + r)\)
 | 
      \(\mathcal O(n \log n)\)
 |

## Poznámka Anki 1674083648443

Karty Anki: 1674083648444
GUID: o|a9Dk1l*C; štítky: bi-ag1::p09 bi-spol::20.

### Otázka (Front)

Dokažte časovou složitost algoritmu \(\mathtt{QuickSort}\).

### Odpověď (Back)

Nejprve dokažme, že pro \(1 \leq i < j \leq n\) platí \(\mathbf E[C_{ij}] = \mathbf P[C_{ij} = 1] = \frac 2 {j - i + 1}\). Určeme tedy **pravděpodobnost porovnání **\(y_i\) s \(y_j\), čili \(\mathbf P[C_{ij} = 1]\).

- \(\mathtt{QuickSort}\) porovnává prvky pouze s pivotem, takže jeden z prvků \(y_i\), \(y_j\) se těsně před porovnáním musí stát pivotem.

- Současně ale žádný prvek z \(y_{i + 1}, \dots, y_{j - 1}\) ještě pivotem být nemohl, jinak by \(y_i\) a \(y_j\) patřily do různých částí posloupnosti a nemohly by být porovnány.
- Jinými slovy \(C_{ij} = 1\) právě tehdy, když se z prvků \(y_i, y_{i + 1}, \dots, y_j\) stane pivotem jako první buď \(y_i\) nebo \(y_j\).
- Protože pivota vybíráme náhodně, může být každý z prvků \(y_i, \dots, y_j\) vybrán se stejnou pravděpodobností \(\frac 1 {j - i + 1}\).
- Proto \(\mathbf P[C_{ij} = 1] = \frac 2 {j - i + 1}\).

Nyní dokažme platnost našeho tvrzení o střední hodnotě celkového počtu porovnání, tedy \(\mathbf E[C] = \mathcal O(n \log n)\).

- Definujme náhodnou veličinu \(C\) jako celkový počet všech porovnání provedených během běhu algoritmu \(\mathtt{QuickSort}\).
- Pak \(C = \sum \limits_{1 \leq i < j \leq n} C_{ij}\).
- Pro střední hodnotu celkového počtu provedených porovnání během běhu algoritmu \(\mathtt{QuickSort}\) tak dostaneme

\[\mathbf E[C] = \sum \limits_{1 \leq i < j \leq n} \frac 2 {j - i + 1} = 2 \sum \limits_{d = 1}^{n - 1} \sum \limits_{i = 1}^{n - d} \frac 1 {d + 1}.\]

- Použili jsme substituci \(j - i = d\), čili \(1 \leq d \leq n - 1\) a \(1 \leq i \leq n - d\), a tedy

\[\mathbf E[C] < 2 \sum \limits_{d = 1}^{n - 1} \sum \limits_{i = 1}^{n - 1} \frac 1 {d + 1} = 2(n - 1) \cdot \sum \limits_{d = 1}^{n - 1} \frac 1 {d + 1} < 2n \cdot \sum \limits_{d' = 2}^n \frac 1 {d'}.\]

- Na odhad poslední sumy nyní použijeme lemma o součtu harmonické řady, tedy \(\mathbf E[C] < 2n \cdot \Theta(\log n) = \mathcal O(n \log n)\).

