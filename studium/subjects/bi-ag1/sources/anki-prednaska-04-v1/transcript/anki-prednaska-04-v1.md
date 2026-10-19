# BI-AG1 – Přednáška 04

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1665386924560

Karty Anki: 1665386924560
GUID: HP9(S^%hl}; štítky: bi-ag1::p04 bi-spol::04.

### Otázka (Front)

Definujte zakořeněný strom a s ním spojené pojmy (předek, potomek, otec, syn, hladina a hloubka).

### Odpověď (Back)

- **Zakořeněný strom** je strom \(T\), ve kterém je jeden vrchol \(r \in V(T)\) označen jako **kořen**.
- Leží-li \(u\) na (jediné) cestě z \(v\) do kořene, pak \(u\) je **předek** \(v\) a \(v\) je **potomek** \(u\). Pokud je navíc \(\set{u, v} \in E(T)\) hrana, říkáme, že \(u\) je **otec** \(v\) a \(v\) je **syn** \(u\).
- Vrcholy rozdělíme podle vzdálenosti od kořene do **hladin**: v nulté leží kořen, v první jeho synové, atd.
- **Hloubka zakořeněného** stromu \(T\) je počet jeho hladin.

## Poznámka Anki 1665386963068

Karty Anki: 1665386963068
GUID: O.cJaNj7Vr; štítky: bi-ag1::p04 bi-spol::04.

### Otázka (Front)

Definujte binární strom.

### Odpověď (Back)

Strom nazveme binární, pokud

- je zakořeněný;
- každý vrchol má nejvýše dva syny;
- u synů rozlišujeme, který je levý a který pravý (je uspořádaný).

## Poznámka Anki 1665387170707

Karty Anki: 1665387170708
GUID: QIJ*xgn>(Q; štítky: bi-ag1::p04 bi-spol::04 bi-spol::23.

### Otázka (Front)

Definujte binární minimovou haldu a uveďte oprace, které podporuje s jejich časovými složitostmi.

### Odpověď (Back)

Binární minimová halda je datová struktura tvaru binárního stromu, v jehož každém vrcholu \(x\) je uložen jeden klíč \(k(x)\). Musí splňovat následující vlastnosti:

- **tvar haldy **- strom má všechny hladiny kromě poslední plně obsazené a poslední hladina je plněna od levého okraje směrem k pravému;
- **haldové uspořádání **- je-li \(v\) vrchol a \(s\) jeho syn, pak platí \(k(v) \leq k(s)\).

Binární minimová halda podporuje oprace:

- \(\mathtt{HeapInsert}\) - vložení klíče do haldy (\(\mathcal{O}(\log n)\)),

- \(\mathtt{HeapFindMin}\) - nalezení minima haldy (\(\mathcal{O}(1)\)),

- \(\mathtt{HeapExtract}\) - odstranění minima haldy (\(\mathcal{O}(\log n)\)).

### Doplňující pole (Extra)

Díky vlastnostem binární minimové haldy platí, že klíče na cestě z libovolného vrcholu do kořene tvoří nerostoucí posloupnost a v kořeni se tedy nachází globální minimum všech klíčů.

## Poznámka Anki 1665388041674

Karty Anki: 1665388041674
GUID: odsQI4^Yq{; štítky: bi-ag1::p04 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište algoritmus vložení prvku do binární haldy (\(\mathtt{HeapInsert}\)) a uveďte jeho časovou složitost.

### Odpověď (Back)

- Vlastnost Tvar haldy dovoluje přidat okamžitě nový prvek na konec nejspodnější hladiny.
- Pokud by již byla plná, založíme novou hladinu. Pokud je Haldové uspořádání mezi novým listem \(l\) a jeho otcem \(o\) v pořádku, můžeme skončit.
- Pokud ne, prohodíme \(k(l)\) a \(k(o)\).
- Tím se ale může porušit vlastnost Haldového uspořádání mezi vrcholem \(o\) a otcem vrcholu \(o\).
- Pokud pro ně Haldové uspořádání neplatí, opět jejich klíče prohodíme, jinak končíme.
- Toto opakujeme, nejdále však až do kořene.
- Na každé hladině strávíme \(\mathcal{O}(1)\) operací a procházených hladin je nejvýše logaritmicky mnoho, tedy celkem čas \(\mathcal{O}(\log n)\).

## Poznámka Anki 1665388817926

Karty Anki: 1665388817926
GUID: qa/ei-1I@!; štítky: bi-ag1::p04 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište algoritmus odebrání minima z binární minimové haldy (\(\mathtt{HeapExtractMin}(H)\)) a uveďte jeho časovou složitost.

### Odpověď (Back)

Triviálně je možné odstranit poslední list \(l\), čili list nejvíc vpravo v poslední hladině. Z toho plyne idea algoritmu odstranění minima:

- Prohoď \(k(r)\) a \(k(l)\).
- Odstraň vrchol \(l\) a zmenši tudíž haldu o \(1\) prvek.
- „Probublávej dolů“ z kořene klíč \(k(l)\) na jeho správné místo, aby opět platilo Haldové uspořádání.

Na každé hladině provedeme \(\mathcal{O}(1)\) operací a procházených hladin je nejvýše logaritmicky mnoho, tedy celkový čas je \(\mathcal{O}(\log n)\).

## Poznámka Anki 1665389903726

Karty Anki: 1665389903726
GUID: Nb}51B+WnO; štítky: bi-ag1::p04 bi-spol::04.

### Otázka (Front)

Popište algoritmus vytvoření binární haldy z \(n\)-prvkového pole (\(\mathtt{HeapBuild}\)).

### Odpověď (Back)

- Má-li prvek \(v\) dva syny \(l\) a \(r\), kteří jsou kořeny podstromů tvořících již korektní haldy, lze podstrom s kořenem ve \(v\) předělat na haldu „zabubláním“ klíče \(k(v)\) dolů.
- Všech \(\lceil n/2 \rceil\) listů jsou \(1\)prvkové haldy.

## Poznámka Anki 1665393886423

Karty Anki: 1665393886423
GUID: N5$M`ekDZ^; štítky: bi-ag1::p04 bi-spol::04.

### Otázka (Front)

Vyslovte a dokažte větu o časové složitosti algoritmu vytvoření binární haldy z \(n\)-prvkového pole (\(\mathtt{HeapBuild}\)).

### Odpověď (Back)

\(\mathtt{HeapBuild}\) má časovou složitost \(\mathcal{O}(n)\).

**Důkaz**

- Nechť strom haldy má \(h\) hladin (od \(0\) do \(h − 1\)).
- Platí tedy \(2^{h-1} \leq n \leq 2h^h - 1\).
- Pro účely analýzy si představíme, že i poslední hladina je zcela plná, například nějakými „dummy“ prvky většími než vše ostatní; tím jistě nesnížíme potřebný počet operací.
- Procedura \(\mathtt{BubbleDown}\) od \(j\)-té hladiny trvá čas \(\mathcal{O}(h - 1 - j)\).
- Pokud to sečteme přes všech \(2^j\) vrcholů hladiny \(j\) a poté přes všechny hladiny, dostaneme (až na konstantu)

\[\sum \limits_{j=0}^{h-1} 2^j(h-1-j) = \sum \limits_{q=0}^{h-1} 2^{h-1-q}q = \sum \limits_{q=0}^{h-1} \frac{2^{h-1}}{2^q}q \leq n\sum \limits_{q=0}^{h-1} \frac{q}{2^q}.\]

- Časovou složitost lze shora odhadnout \(\mathcal{O}(n\sum \limits_{q=0}^{h-1} \frac{q}{2^q}) = \mathcal{O}(n)\), protože s použitím d'Alembertova kritéria (\(\frac{k}{2^k} > 0)\) platí

\[\lim \limits_{k \to \infty} \Bigg( \frac{k+1}{2^{k+1}} \Bigg/ \frac{k}{k^2} \Bigg) = \lim \limits_{k \to \infty} \frac{(k+1) \cdot 2^k}{k \cdot 2^{k+1}} = \lim \limits_{k \to \infty} \frac{(k+1)}{k \cdot 2} = \frac{1}{2}.\]

- \(\frac{1}{2} < 1\), a tedy řada konverguje.

## Poznámka Anki 1665394046251

Karty Anki: 1665394046252
GUID: qMpJX$w.F!; štítky: bi-ag1::p04 bi-spol::04 bi-spol::20.

### Otázka (Front)

Popište algoritmus \(\mathtt{HeapSort}\) a jeho časovou složitost.

### Odpověď (Back)

- \(n\) prvků vstupní posloupnosti vložíme do pole
- na toto pole zavoláme \(\mathtt{HeapBuild}\)
- poté \(n\)-krát zavoláme \(\mathtt{HeapExtractMin}\) a vracené hodnoty vypíšeme do výstupního pole
- podle analýz k binární haldě má \(\mathtt{HeapSort}\) časovou složitost \(\mathcal{O}(n) + \mathcal{O}(n \log n) = \mathcal{O}(n \log n)\)

## Poznámka Anki 1665394335911

Karty Anki: 1665394335911
GUID: y*IL,>+GpT; štítky: bi-ag1::p04 bi-spol::04 bi-spol::20.

### Otázka (Front)

Definujte amortizovanou časovou složitost.

### Odpověď (Back)

Operace \(A\) nad dynamickou datovou strukturou má v daném kontextu svého provádění amortizovanou časovou složitost \(\mathcal{O}(f(n))\) (značíme \(\mathcal{O}^*(f (n))\)), pokud posloupnost \(k\) operací \(A\) má celkovou časovou složitost \(\mathcal{O}(k \cdot f(n))\). Parametr \(n\) je velikost dynamické datové struktury po provedení této posloupnosti operací.

## Poznámka Anki 1665395665580

Karty Anki: 1665395665580
GUID: nE0<L4_l98; štítky: bi-ag1::p04.

### Otázka (Front)

Vyslovte a dokažte větu o korektnosti algoritmu \(\mathtt{HeapInsert}\).

### Odpověď (Back)

Buď \(H\) minimová halda a \(k\) klíč. Potom struktura vzniklá voláním \(\mathtt{HeapInsert}(H, k)\) je opět minimová halda.

**Důkaz**

- Pokud je \(H\) prázdná, pak je výsledkem jednoprvková halda, tvrzení platí triviálně. Jinak označme \(\hat{H}\) výsledek volání \(\mathtt{HeapInsert}(H, k)\).
- \(\hat{H}\) má tvar haldy a zbývá ověřit, že splňuje podmínku haldového uspořádání.
- Po přidání hodnoty \(k\) do nového listu \(l\) může existovat jen jedna hrana s porušenou podmínkou.

- Tento problém pomocí funkce \(\mathtt{BubbleUp}\) posouváme směrem ke kořeni.

- Pozorujeme, že uspořádání mezi libovolným otcem \(o\) a jeho případným druhým synem na cestě z \(l\) do kořene neporušíme, neboť se hodnota \(k_o\) v \(o\) nemohla aplikováním \(\mathtt{BubbleUp}\) zvýšit (může pouze snížit nebo zůstat stejná).

## Poznámka Anki 1665395817261

Karty Anki: 1665395817261
GUID: Df^uCFFeqn; štítky: bi-ag1::p04.

### Otázka (Front)

Vyslovte a dokažte větu o korektnosti algoritmu \(\mathtt{HeapExtractMin}\).

### Odpověď (Back)

Buď \(H\) minimová halda a \(k\) klíč. Potom struktura vzniklá voláním \(\mathtt{HeapExtractMin}(H)\) je opět minimová halda.

**Důkaz**

- Tvar haldy je opět zachován triviálně.
- Pokud je výsledkem prázdná či jednoprvková halda, máme hotovo.
- Prohození extrahovaného prvku s listem mohlo porušit haldové uspořádání (mezi hladinami 0 a 1).
- Opět prohazujeme s menším ze synů, čímž posunujeme porušení na dvojici následujících hladin.
- Toto může pokračovat jen do poslední hladiny.

## Poznámka Anki 1669495513639

Karty Anki: 1669495513639
GUID: sq*PP9eafq; štítky: bi-ag1::p04 bi-spol::04.

### Otázka (Front)

Určete počet hladin, listů, vnitřních vrcholů a vrcholů v \(i\)-té hladině binárního stromu o \(n\) prvcích.

### Odpověď (Back)

- počet hladin: \(\lfloor \log_2 n \rfloor + 1\)
- počet listů: \(\lceil \frac n 2 \rceil\)
- počet vnitřních vrcholů: \(\lfloor \frac n 2 \rfloor\)
- počet vrcholů v \(i\)-té hladině: \(2^i\) (poslední hladina však nemusí být zcela zaplněná)

## Poznámka Anki 1670695895439

Karty Anki: 1670695895439
GUID: M20!(AITyu; štítky: bi-ag1::p04.

### Otázka (Front)

Je-li \(v\) vrchol binární minimové haldy s indexem \(i\), jaké budou indexy jeho levého syna, pravého syna a rodiče?

### Odpověď (Back)

- levý syn: \(2i\)
- pravý syn: \(2i + 1\)
- rodič: \(\lfloor \frac i 2 \rfloor\)

