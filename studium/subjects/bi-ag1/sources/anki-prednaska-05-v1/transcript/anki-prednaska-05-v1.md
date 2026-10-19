# BI-AG1 – Přednáška 05

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1665992332944

Karty Anki: 1665992332944
GUID: IMH,GT9$-o; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Definujte binomiální strom.

### Odpověď (Back)

Binomiální strom řádu \(k\) (značíme \(B'_k\)) je uspořádaný zakořeněný strom, pro který platí:

- \(B'_0\) je tvořen pouze kořenem.

- Pro \(k \geq 1\) se \(B'_k\) skládá ze stromu \(B'_{k-1}\), pod jehož kořenem je jako nejpravější syn napojený další strom \(B'_{k-1}\).

## Poznámka Anki 1665993580930

Karty Anki: 1665993580930
GUID: lD)!<O-XAJ; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Definujte binomiální haldu.

### Odpověď (Back)

Binomiální halda (BH) obsahující \(n\) prvků je uspořádaná množina binomiálních stromů \(\mathcal{T} = T_1, \dots, T_l\), kde platí:

- Stromy \(T_i\) jsou v \(\mathcal{T}\) uspořádány vzestupně podle svých řádů.
- \(n = |V(T_1)| + \dots + |V(T_l)|\).
- Pro každé nezáporné \(k\) se v množině \(\mathcal{T}\) vyskytuje nejvýše jeden binomiální strom řádu \(k\).
- Každý vrchol \(v\) v každém stromu obsahuje klíč \(k(v)\).
- Pro každý strom \(T_i\) platí haldové uspořádání klíčů, čili \(\forall v \in V(T_i)\) a pro všechny jeho syny \(s_j, j = 1, 2,\dots , m\), platí \(k(v) \leq k(s_j)\).

## Poznámka Anki 1665997554894

Karty Anki: 1665997554894
GUID: B0i)_S]D9d; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Kdy se vyskytuje binomiální strom \(B_i\) v seznamu \(\mathcal{T}\) \(n\)-prvkové binomiální haldy? Uveďte důsledek.

### Odpověď (Back)

Binomiální strom \(B_i\) se vyskytuje v seznamu \(\mathcal{T}\) \(n\)-prvkové BH právě tehdy, když ve dvojkovém zápisu \(b_k b_{k-1} \dots b_0\) čísla \(n\) je \(b_i = 1\).

Důsledkem je, že \(n\)-prvková BH má až \(\mathcal{O}(\log n)\) binomiálních stromů.

## Poznámka Anki 1665997653112

Karty Anki: 1665997653112
GUID: F::|nT5yYa; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Popište algoritmus nalezení minima binomiální haldy (\(\mathtt{BHFindMin}(H)\)).

### Odpověď (Back)

- Minimum celé BH se musí nacházet v jednom z kořenů stromů \(T_i\).
- Stačí projít seznam \(\mathcal{T}\), což bude trvat čas \(\mathcal{O}(\log n)\).
- Používáme-li tuto funkci často, vyplatí se udržovat ukazatel na tento globálně nejmenší kořen. Operaci \(\mathtt{BHFindMin}\) lze pak provést v konstantním čase.

## Poznámka Anki 1665998049342

Karty Anki: 1665998049342
GUID: oG1VNUI~jg; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Popište algoritmus sloučení dvou binomiálních stromů (\(\mathtt{BHMergeTree}\)) a uveďte jeho složitost.

### Odpověď (Back)

**Vstup**
Binomiální stromy \(T_1\), \(T_2\) stejných řádů.

**Výstup**
Výsledný binomiální strom řádu o jedna větší.

**Postup**
Porovnáme kořeny. Pokud je kořen \(T_1\) menší nebo roven kořenu \(T_2\) připojíme \(T_2\) jako nejpravějšího syna pod kořen \(T_1\). Jinak připojíme \(T_1\) jako nejpravějšího syna pod kořen \(T_2\).

**Složitost
**Algoritmus lze naimplementovat s časovou složitostí \(\mathcal{O}(1)\).

## Poznámka Anki 1665998606191

Karty Anki: 1665998606191
GUID: vB/+S;wuXy; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Popište algoritmus sloučení dvou binomiálních hald (\(\mathtt{BHMerge}(A, B)\)).

### Odpověď (Back)

- Procházíme obě BH pomocí dvou ukazatelů.
- Pokud ukazatel v jedné haldě narazí na binomiální strom řádu \(i\), který se v druhé haldě nevyskytuje, stačí tento strom překopírovat do výsledku. Takto udržujeme ukazatele na binomiálních stromech stejného řádu.
- Jsou-li všechny tři stromy \(A_i\), \(B_i\) a \(\operatorname{carry}_i\) neprázdné, sloučíme \(A_i\) a \(B_i\) pomocí \(\mathtt{BHMergeTree}(A_i, B_i)\) a výsledek se stane přenosem do dalšího řádu \(\operatorname{carry}_{i+1}\) a do výsledku přiřadíme \(\operatorname{carry}_i\).

## Poznámka Anki 1665998845759

Karty Anki: 1665998845759
GUID: p^K_7|7sLP; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Vyslovte a dokažte větu o správnosti a časové složitosti algoritmu sloučení dvou binomiálních hald (\(\mathtt{BHMerge}\)).

### Odpověď (Back)

- V každé iteraci se zpracují všechny stromy řádu \(i\).
- Následně se řád \(i\) zvýší o jedna.
- Všechny operace v rámci jednoho řádu trvají \(\mathcal{O}(1)\).
- Nejvyšší řád je \(\mathcal{O}(\log n)\), celkový čas je tedy \(\mathcal{O}(\log n)\).

## Poznámka Anki 1665998905189

Karty Anki: 1665998905189
GUID: q}PoQ,(F19; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Popište algoritmus vložení prvku do binomiální haldy (\(\mathtt{BHInsert}(H,x)\)).

### Odpověď (Back)

- Vytvoříme BH \(H'\) s jediným prvkem \(x\).
- Zavoláme \(\mathtt{BHMerge}(H, H')\).

## Poznámka Anki 1665999263556

Karty Anki: 1665999263556
GUID: tJ;TL9{+x; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Vyslovte a dokažte tvrzení o časové složitosti vložení prvku do binomiální haldy (\(\mathtt{BHInsert}\)).

### Odpověď (Back)

Operace \(\mathtt{BHInsert}\) má v nejhorším případě složitost \(\mathcal{O}(\log n)\). Pro na počátku prázdnou BH trvá posloupnost \(n\) volání operace \(\mathtt{BHInsert}\) čas \(\mathcal{O}(n)\). \(\mathtt{BHInsert}\) má tedy amortizovanou časovou složitost \(\mathcal{O}^*(1)\).

**Důkaz**

- Víme, že binomiální stromy tvořící \(n\)-prvkovou BH přesně odpovídají jedničkovým bitům v dvojkovém zápisu čísla \(n\).
- Operace \(\mathtt{BHInsert}\) je sloučení s jednoprvkovou BH a to odpovídá operaci \(\mathtt{Inc}\) binární sčítačky.
- Provedení operace \(\mathtt{BHMergeTree}\) s \(\mathcal{O}(1)\) složitostí během \(\mathtt{BHInsert}\) odpovídá bitové inverzi v operaci \(\mathtt{Inc}\).
- Dle analýzy binární sčítačky má tedy operace \(\mathtt{BHInsert}\) amortizovanou složitost \(O^*(1)\).

 (https://courses.fit.cvut.cz/BI-AG1/media/lectures/bi-ag1-p5-handout.pdf#Navigation1)

## Poznámka Anki 1665999362621

Karty Anki: 1665999362621
GUID: y[o1#|^C-=; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Popište algoritmus vytvoření \(n\)-prvkové binomiální haldy (\(\mathtt{BHBuild}\)) a uveďte jeho časovou složitost.

### Odpověď (Back)

- Voláním \(\mathtt{BHInsert}\) \(n\)-krát po sobě vytvoříme BH o velikosti \(n\).
- Podle analýzy \(\mathtt{BHInsert}\) bude trvat vytvoření \(n\)-prvkové BH čas \(\mathcal{O}(n)\).

## Poznámka Anki 1665999872565

Karty Anki: 1665999872566
GUID: vSdpq-AP+&; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Popište algoritmus odstranění minima z binomiální haldy (\(\mathtt{BHExtractMin}\)).

### Odpověď (Back)

- V BH \(H\) najdeme strom \(T\), jehož kořen je minimem.
- Tento strom odpojíme z \(H\).
- Z \(T\) odtrhneme kořen a vytvoříme z něj novou BH \(H'\).
- Provedeme \(\mathtt{BHMerge}(H, H')\).

## Poznámka Anki 1666000137670

Karty Anki: 1666000137670
GUID: z.t[6!*cB3; štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Vyslovte a dokažte tvrzení o časové složitosti algoritmu odstranění minima z binomiální haldy (\(\mathtt{BHExtractMin}\)).

### Odpověď (Back)

Časová složitost operace \(\mathtt{BHExtractMin}\) je \(\mathcal{O}(\log n)\).

**Důkaz**

- Nalezení stromu \(T\), jehož kořen je minimem, v BH \(H\) trvá \(\mathcal{O}(1)\). Stačí si udržovat minimový ukazatel na strom a vypojit ho ze seznamu.

- Odpojení stromu \(T\) a odtrhnutí jeho kořene trvá \(\mathcal{O}(\log n)\), protože kořen binomiálního stromu má nejvýše \(\mathcal{O}(\log n)\) synů.
- Sloučení hald trvá \(\mathcal{O}(\log n)\), včetně rekonstrukce minimového ukazatele.

## Poznámka Anki 1669495703641

Karty Anki: 1669495703641
GUID: gA-ppA`PY); štítky: bi-ag1::p05 bi-spol::04.

### Otázka (Front)

Určete počet vrcholů, počet hladin, počet vrcholů v \(i\)-té hladině a stupeň kořene binomiálního stromu řádu \(k\).

### Odpověď (Back)

- počet vrcholů: \(2^k\)
- počet hladin: \(k + 1\)
- počet vrcholů v \(i\)-té hladině: \(k \choose i\)
- stupeň kořene: \(k\)

