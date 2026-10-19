# BI-AG1 – Přednáška 03

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 20 poznámek, 20 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1664783197739

Karty Anki: 1664783197739
GUID: E(l>X[+iuE; štítky: bi-ag1::p03 bi-spol::03.

### Otázka (Front)

Dokažte část věty o charakterizaci stromů: \(G\) je strom \(\Longleftrightarrow\) \(G\) je souvislý a vynecháním libovolné hrany vznikne nesouvislý graf.

### Odpověď (Back)

** **\(G\)** je strom **\(\Longrightarrow\) \(G\)** je souvislý a vynecháním libovolné hrany vzniknce nesouvislý graf:**

- Souvislost je splněna triviálně.
- Předpokládejme pro spor, že existuje hrana \(e = \set{u, v} \in E\) taková, že graf \(G - e = (V, E \setminus \set{e})\) je souvislý.
- Pak v \(G - e\) musí existovat \(u\text{-}v\text{-}\)cesta, která se ale po přidání hrany \(e\) stane v grafu \(G\) kružnicí, což je spor s předpokladem, že \(G\) je strom.

 [Obrázek: paste-5dc89aae02a28185c97171bf4d812a7339355191.jpg; soubor je v media/ v doprovodném ZIP] 

\(G\)** je souvislý a vynecháním libovolné hrany vzniknce nesouvislý graf **

\(\Longrightarrow\) \(G\)** je strom:**

- Souvislost je splněna, stačí ukázat neexistenci kružnic v \(G\).
- Předpokládejme pro spor, že (1) vynecháním libovolné hrany v \(G\) vznikne nesouvislý graf a současně že (2) \(G\) obsahuje kružnici \(C\).
- Vyjmeme-li z \(G\) ale libovolnou hranu \(e = \set{x, y} \in C\), pak se \(G\) nerozpadne na dvě komponenty, protože jakékoliv cestě mezi libovolnými \(2\) vrcholy \(u\) a \(v\), která před tím obsahovala \(e\), poskytne \(C\) alternativní spojení.
- Pro hrany kružnice \(C\) tudíž předpoklad (1) neplatí – dostali jsme spor.

 [Obrázek: paste-14dafa5a30c0b081b7df0946e4891c3e32df39d5.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1664783326814

Karty Anki: 1664783326814
GUID: zlPFrelW(P; štítky: bi-ag1::p03 bi-spol::03.

### Otázka (Front)

Definujte kostru grafu.

### Odpověď (Back)

Nechť \(G = (V, E)\) je souvislý graf. Podgraf \(K\) grafu \(G\) nazveme kostrou grafu \(G\), pokud \(V(K) = V\) a \(K\) je strom.

### Doplňující pole (Extra)

- Nesouvislé grafy nemají kostru, kostru má každá souvislá komponenta.
- Kostra souvislého grafu je tedy souvislý podgraf nad stejnou množinou vrcholů s nejmenším počtem hran.
- Souvislý graf s kružnicemi má více různých koster.

## Poznámka Anki 1664783618460

Karty Anki: 1664783618460
GUID: jrRnBJ^2,(; štítky: bi-ag1::p03 bi-spol::03.

### Otázka (Front)

Popište algoritmus pro hledání kostry souvislého grafu.

### Odpověď (Back)

**Vstup**
Souvislý graf \(G\)

**Výstup**
Seznam hran nějaké kostry grafu \(G\)

**Postup**
Spustíme algoritmus \(\text{BFS}(G, s)\), kde \(s \in V(G)\). Hrany do předchůdců pak tvoří kostru.

 [Obrázek: paste-e3868d08ad0f20c4597c388f6a2dbccd16abae8a.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1664783780168

Karty Anki: 1664783780168
GUID: ot^S}$$!mT; štítky: bi-ag1::p03 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o správnosti modifikace algoritmu \(\text{BFS}\) pro hledání kostry souvislého grafu.

### Odpověď (Back)

Nechť \(G = (V, E)\) je souvislý graf. Potom hrany do předchůdců v \(\text{BFS}\) tvoří nějakou kostru grafu \(G\).

**Důkaz**

- Označme \(H\) graf na množině vrcholů \(V\) s hranami do předchůdců (podle pole vyplněného algoritmem \(\text{BFS}\)).
- Víme, že každý vrchol kromě počátečního vrcholu má právě jednoho předchůdce. Tedy \(H\) má právě \(n - 1\) hran.
- Protože po hranách do předchůdců je možné se z každého vrcholu dostat do \(s\) (tedy pro každý vrchol \(v\) existuje v \(H\) sled z \(v\) do \(s\)), a protože složením sledů vznikne sled, je graf \(H\) souvislý.

## Poznámka Anki 1664785012100

Karty Anki: 1664785012100
GUID: v2{*?mWgPZ; štítky: bi-ag1::p03 bi-spol::03.

### Otázka (Front)

Definujte topologické uspořádání grafu.

### Odpověď (Back)

Topologické uspořádání (TU) orientovaného grafu \(G = (V, E)\) je takové seřazení vrcholů \(V = \set{v_1, \dots, v_n}\), že pro každou orientovanou hranu \((v_i, v_j) \in E\) platí \(i < j\).

### Doplňující pole (Extra)

- Pokud graf obsahuje cyklus, nelze topologicky uspořádat.
- Jinými slovy, pokud vrcholy zakreslíme horizontálně v pořadí topologického uspořádání, budou všechny orientované hrany směřovat zleva doprava.

## Poznámka Anki 1664785063294

Karty Anki: 1664785063294
GUID: olBZ=0S{l5; štítky: bi-ag1::p03 bi-spol::03 bi-spol::04.

### Otázka (Front)

Definujte acyklický graf.

### Odpověď (Back)

Orientovaný graf \(G\) je acyklický, pokud neobsahuje jako podgraf orientovanou kružnici.

## Poznámka Anki 1664785096026

Karty Anki: 1664785096026
GUID: mA!4g)RRD!; štítky: bi-ag1::p03 bi-spol::03.

### Otázka (Front)

Definujte zdroj.

### Odpověď (Back)

Zdroj je takový vrchol orientovaného grafu, do kterého nevede žádná hrana.

## Poznámka Anki 1664785277832

Karty Anki: 1664785277832
GUID: orz$Ej)d}w; štítky: bi-ag1::p03.

### Otázka (Front)

Vyslovte a dokažte větu o existenci zdroje a stoku v orientovaném acyklickém grafu.

### Odpověď (Back)

Nechť \(G = (V, E)\) je orientovaný acyklický graf. Potom \(G\) obsahuje aspoň jeden zdroj a aspoň jeden stok.

**Důkaz**

- Sporem pro existenci zdroje (pro stok analogické).
- Předpokládejme, že v \(G\) neexistuje zdroj.
- Zvolme libovolný vrchol \(v_1 \in V\). Do něj, dle předchozího předpokladu, vede alespoň jedna orientovaná hrana z nějakého vrcholu \(v_2\).
- Do \(v_2\) také musí vést orientovaná hrana z nějakého vrcholu \(v_3\), a tak dále.
- Nejpozději po \(n\) krocích se však musí nějaký vrchol zopakovat.
- To ale znamená existenci cyklu v \(G\), čímž dostáváme spor.

## Poznámka Anki 1664785293751

Karty Anki: 1664785293751
GUID: Bow7tGroNL; štítky: bi-ag1::p03 bi-spol::03.

### Otázka (Front)

Definujte stok.

### Odpověď (Back)

Stok je takový vrchol orientovaného grafu, ze kterého nevede žádná hrana.

## Poznámka Anki 1664788057739

Karty Anki: 1664788057739
GUID: Fld!kc+v<_; štítky: bi-ag1::p03 bi-spol::03.

### Otázka (Front)

Popište algoritmus \(\text{TopSort}\).

### Odpověď (Back)

**Vstup**

- orientovaný graf \(G = (V, E)\)
**Výstup**

- nějaké topologické uspořádání \(G\), pokud je acyklický a detekce cykličnosti v opačném případě

**Postup**

- Spočteme pole vstupních stupňů vrcholů \(\delta\).
- Zinicializujeme frontu \(Q\) se všemi vrcholy \(v \in V\), které jsou zdroji, tedy platí pro ně \(\delta[v] = 0\).
- Dokud je fronta \(Q\) neprázdná, iterujeme:

- vybereme první vrchol z \(Q\) a označíme jej \(v\);
- vrchol \(v\) zařadíme do výstupního pořadí;
- vrchol \(v\) odebereme z grafu, tedy každému jeho následníkovi snížíme hodnotu v \(\delta\);
- pokud tímto vznikne nový zdroj, tj. vrchol \(w \in V\), pro který platí \(\delta[w] = 0\), přidáme jej do \(Q\).

- Pokud došlo k vyprázdnění \(Q\) a jsou zpracovány všechny vrcholy, je výstupem nějaké topologické uspořádání \(G\). V opačném případě obsahuje gram orientovaný cyklus.

**Složitost**

- Časová složitost algoritmu je \(\mathcal O(n + m)\).

## Poznámka Anki 1664788465996

Karty Anki: 1664788465996
GUID: hLa2b5`d:J; štítky: bi-ag1::p03 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o správnosti algoritmu \(\text{TopSort}\).

### Odpověď (Back)

Algoritmus \(\text{TopSort}(G)\) spuštěný na orientovaný graf \(G\) doběhne v konečném čase a buď vygeneruje korektní topologické uspořádání acyklického grafu, nebo detekuje existenci orientovaného cyklu.

**Důkaz**

- Předpokládejme, že \(G\) je orientovaný graf a předpokládejme, že před tím, než začneme vkládat zdroje do \(Q\), existuje aspoň jeden zdroj \(z\) a že všechny zdroje zařadíme do fronty \(Q\).
- Vnitřek hlavního cyklu realizuje odebrání jednoho zdroje z fronty \(Q\), jeho vyjmutí z grafu \(G\), jeho vložení do výsledného uspořádání a identifikaci případných nových zdrojů a jejich zařazení do \(Q\).
- Existence hrany \((v_i, v_j)\) znemožňuje vložit vrchol \(v_j\) do fronty \(Q\) před vrcholem \(v_i\), protože \(v_j\) by v takovém okamžiku mělo \(\delta(v_j) \geq 1\) a podmínkou vložení do \(Q\) je \(\delta(v_j) = 0\).
- Pokud jsou v okamžiku vyprázdnění fronty zpracovány všechny vrcholy grafu \(G\), našli jsme TU orientovaného acyklického grafu.

- Pokud je fronta prázdná a přesto zbývají nějaké nezpracované vrcholy ve zbytku \(G\), pak ve zbytku \(G\) nejsou žádné zdroje, čili každý vrchol má vstupní hranu/-y a musí existovat orientovaný cyklus, plus případně z něj dostupné podgrafy. Vrcholy tohoto zbytkového grafu nelze topologicky uspořádat.

- Algoritmus tedy správně detekuje existenci cyklu a skončí v konečném čase.
- V obou případech algoritmus pracuje korektně a zastaví se.

## Poznámka Anki 1664789243075

Karty Anki: 1664789243075
GUID: dY=ff6)BXU; štítky: bi-ag1::p03 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o složitosti algoritmu \(\text{TopSort}\).

### Odpověď (Back)

Algoritmus 

\(\text{TopSort}(G)\), kde \(G = (V,E)\) je orientovaný graf reprezentovaný pomocí pole následníků, má časovou i paměťovou složitost \(\mathcal{O}(|V| + |E|)\).

**Důkaz**

- Výpočet pole vstupních stupňů trvá \(\Theta(|E|)\).
- Počáteční vložení zdrojů do \(Q\) trvá \(\mathcal{O}(|V |)\).
- Každý vrchol je vložen do \(Q\) nejvýše \(1 \times\), proto vybírání z \(Q\) a výpis na výstup trvá \(\mathcal{O}(|V|)\).
- Každá hrana může být odebrána z grafu nejvýše \(1 \times\), proto snížení stupňů následníků trvá \(\mathcal{O}(|E|)\).
- Celková časová složitost je tedy \(\mathcal{O}(|V| + |E|)\).
- Graf \(G\), pole \(\delta\), fronta \(Q\), to vše zabere \(\mathcal{O}(|V| + |E|)\) paměti.

## Poznámka Anki 1664789549904

Karty Anki: 1664789549904
GUID: nq{62-gh`<; štítky: bi-ag1::p03 bi-spol::20.

### Otázka (Front)

Popište problém řazení.

### Odpověď (Back)

**Vstup**
Posloupnost čísel \(A = a_1, a_2, \dots, a_n\)

**Výstup
**Permutace \(A' = a_1', a_2', \dots, a_n'\) vstupní posloupnosti \(A\), že platí \(a_1' \leq a_2' \leq \dots \leq a_n' \)

## Poznámka Anki 1664791860506

Karty Anki: 1664791860506
GUID: Q|)cU.7}#q; štítky: bi-ag1::p03 bi-spol::20.

### Otázka (Front)

Popište taxonomii algoritmů pro řazení.

### Odpověď (Back)

- **základní operace**:

- řazení založené pouze na binární operaci porovnání-a-prohození (Compare-and-Exchange)
- řazení založené na jiné operaci

- **paměťová náročnost**:

- in-place algoritmy (potřebují \(n + \text{polylog}(n)\) paměti)
- out-of-place algoritmy

- **stabilita**:

- stabilní algoritmy (pořadí stejně velkých prvků je zachováno)
- nestabilní algoritmy (pořadí stejně velkých prvků se může změnit)

- **citlivost na hodnoty prvků vstupní posloupnosti**:

- datově citlivé algoritmy (časová složitost závisí na hodnotách prvků)
- datově necitlivé algoritmy (časová složitost nezávisí na hodnotách prvků)

## Poznámka Anki 1664792196290

Karty Anki: 1664792196290
GUID: rEj~*/pA0]; štítky: bi-ag1::p03 bi-spol::20.

### Otázka (Front)

Popište princip algoritmů \(\text{SelectSort}\) a \(\text{InsertSort}\).

### Odpověď (Back)

Algoritmy \(\texttt{SelectSort}\) a \(\texttt{InsertSort}\) jsou řadící algoritmy, které fungují na podobném principu. Vstupní posloupnost je rozdělena na levou seřazenou část, která je zpočátku prázdná, a pravou neseřazenou část, která zpočátku obsahuje celou vstupní posloupnost. S každou iterací se hranice mezi seřazenou na neseřazenou částí posune o jednu pozici doprava. Liší se však v postupu řazení:

- \(\texttt{SelectSort}\) - z neseřazené části je vybráno minimum, které je prohozeno s prvním prvkem této části (tj. přesune se přímo za sežazenou část);

- \(\texttt{InsertSort}\) - z neseřazené části je vybrán první prvek, který je vložen zprava na správnou pozici v seřazené části.

## Poznámka Anki 1664792346947

Karty Anki: 1664792346947
GUID: y1xR7Dbvov; štítky: bi-ag1::p03 bi-spol::20.

### Otázka (Front)

Zařaďte algoritmus \(\text{SelectSort}\), uveďte jeho časovou složitost a invariant.

### Odpověď (Back)

Algoritmus \(\text{SelectSort}\) seřadí \(n\)-prvkové pole v čase \(\Theta(n^2)\) a je in-place, nestabilní a datově necitlivý.

**Invariant**: Po \(i\)-té iteraci je vlevo seřazená posloupnost délky \(i\) a vpravo zbývá \(n - i\) neseřazených prvků, které jsou \(\geq\) než čísla v levé části.

## Poznámka Anki 1664792466287

Karty Anki: 1664792466288
GUID: ChGHd)6e4=; štítky: bi-ag1::p03 bi-spol::20.

### Otázka (Front)

Zařaďte algoritmus \(\text{InsertSort}\), uveďte jeho časovou složitost a invariant.

### Odpověď (Back)

Algoritmus \(\text{InsertSort}\) seřadí \(n\)-prvkové pole v čase \(\mathcal{O}(n^2)\) a je in-place, stabilní, datově citlivý.

**Invariant**: Po \(i\)-té iteraci je vlevo seřazená posloupnost délky \(i + 1\) a vpravo zbývá \(n - 1 - i\) neseřazených prvků.

## Poznámka Anki 1664792643406

Karty Anki: 1664792643406
GUID: hq-a=J}V%8; štítky: bi-ag1::p03 bi-spol::20.

### Otázka (Front)

Popište algoritmus \(\text{BubbleSort}\).

### Odpověď (Back)

\(\texttt{BubbleSort}\) je in-place, stabilní a datově citlivý řadící algoritmus s časovou složitostí \(\mathcal O(n^2)\).

**Vstup** 

- neseřazené pole \(X = x_1, \dots, x_n\)

**Výstup** 

- seřazené pole \(Y = y_1, \dots, y_n\)

**Postup** 

- Pro všechna \(i := 1, \dots, n -1\) iterujeme:

- postupně zleva doprava porovnáváme dvojice sousedních prvků a pokud jsou v nesprávném pořadí, prohodíme je.

- Vrátíme \(Y := X\).

**Složitost** 

- Časová složitost algoritmu je \(\mathcal O(n^2)\).

### Doplňující pole (Extra)

Po první iteraci algoritmu je největší prvek posloupnosti přesunut na poslední místo, po druhé druhý největší a tak dále. Iterací se provede nejvýše \(n - 1\) a pokud se během průchodu neprohodí žádná dvojice prvků, je řazení u konce. \(\texttt{BubbleSort}\) je vhodný zejména v případě, kdy je vstupní posloupnost již z velké části seřazená.

## Poznámka Anki 1664792845251

Karty Anki: 1664792845251
GUID: MPI]{M9j<x; štítky: bi-ag1::p03 bi-spol::20.

### Otázka (Front)

Vyslovte a dokažte větu o korektnosti algoritmu \(\text{BubbleSort}\).

### Odpověď (Back)

Algoritmus \(\text{BubbleSort}\) korektně seřadí \(n\)-prvkové pole.

**Důkaz**

- Korektnost dokážeme indukčním důkazem následujícího invariantu.
- **Invariant**: nejpozději po \(i\)-té iteraci hlavního cyklu se \(i\) největších prvků pole nachází seřazeno na \(i\) posledních pozicích zprava.
- IZ: Invariant platí pro \(i = 1\). Po \(1.\) iteraci je největší prvek celé posloupnosti zaručeně na poslední pozici.
- IK: Předpokládejme, že invariant platí pro všechna \(j < i\)  a tedy \(i - 1\) největších prvků se nachází seřazeno na posledních \(i - 1\) pozicích vpravo. Proveďme \(i\)-tou iteraci.
- Tím probublá největší hodnota levého zbytku doprava, levá část se zkrátí o jedna a pravá seřazená část se zvětší o jeden prvek, a invariant platí.

## Poznámka Anki 1664793097297

Karty Anki: 1664793097297
GUID: QrPP0WI+!?; štítky: bi-ag1::p03 bi-spol::20.

### Otázka (Front)

Vyslovte a dokažte větu o složitosti a vlastnostech algoritmu \(\text{BubbleSort}\).

### Odpověď (Back)

\(\text{BubbleSort}\) seřadí \(n\)-prvkové pole v čase \(\mathcal{O}(n^2)\) a je in-place, stabilní a datově citlivý.

**Důkaz**

- Iterací je nejvýše \(n - 1\), \(i\)-tá iterace trvá \(\Theta(n - i)\) kroků, což dává časovou složitost \(\mathcal{O}(n^2)\).
- Kromě vstupního pole potřebuje pouze \(\mathcal{O}(1)\) paměti.
- Je stabilní, neboť v hlavním cyklu se prvky prohazují pouze při ostré nerovnosti.
- Je datově citlivý, neboť končí, jakmile nedošlo během některé iterace ke změně.
- V nejlepším případě již seřazeného pole má složitost \(\Theta(n)\).

