# BI-ML1 – 09 Nesupervizovane uceni

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::3 BI-ML1::09 Nesupervizovane uceni
Rozsah: 39 poznámek, 39 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785269100176

Karty Anki: 1785269200176
GUID: 3f43bb3947db; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co je **nesupervizované učení**, jaký má geometrický cíl a proč je jeho evaluace obtížná?

### Odpověď (Back)

Jde o učení z příznaků **bez známé cílové proměnné**, proto „bez učitele“. Hledá vnitřní strukturu: reálná data obvykle nejsou rovnoměrně v celém prostoru, ale soustřeďují se do shluků či nízkodimenzionálních oblastí s vysokou četností.

Leží-li data poblíž objektu nižší dimenze, lze je popsat méně souřadnicemi; např. povrch koule v ℝ³ je dvourozměrný a stačí dvě sférické souřadnice.

Evaluace je obtížná, protože chybí správné cíle a nemusí existovat jediné správné řešení: různé definice podobnosti, kompaktnosti a struktury mohou být legitimní.

## Poznámka Anki 1785269100177

Karty Anki: 1785269200177
GUID: c7054d802fed; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jaký je **pravděpodobnostní pohled** na nesupervizované učení u spojitých a diskrétních příznaků?

### Odpověď (Back)

Data chápeme jako realizace náhodného vektoru **X=(X₁,…,Xₚ)ᵀ**. Pro p binárních příznaků je prostor typicky {0,1}ᵖ, pro spojité ℝᵖ.

Porozumět rozdělení X znamená odhadovat P(X∈O) pro relevantní oblasti O. U spojitých znaků odhadujeme sdruženou hustotu f<sub>X</sub>(x₁,…,xₚ) nebo její strukturální vlastnosti; u diskrétních sdruženou pravděpodobnostní funkci p<sub>X</sub>(x)=P(X₁=x₁,…,Xₚ=xₚ).

## Poznámka Anki 1785269100178

Karty Anki: 1785269200178
GUID: db2868c5643f; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co je **shlukování** a proč mohou různé algoritmy rozdělit stejná data odlišně?

### Odpověď (Back)

Clustering je nesupervizované rozdělení dat do shluků podle zvolené podobnosti či vzdálenosti. Intuitivně mají být blízké body spolu a vzdálené odděleně.

To však neurčuje přesnou míru blízkosti, přípustnou velikost a tvar shluků ani řešení konfliktu lokální blízkosti s globální kompaktností. Algoritmy proto optimalizují různá kritéria a předpokládají jiný tvar, hustotu či hierarchii shluků.

## Poznámka Anki 1785269100179

Karty Anki: 1785269200179
GUID: eb2bb4681830; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co je **metrika a metrický prostor** a jaké axiomy musí vzdálenost splňovat?

### Odpověď (Back)

Metrika je funkce d:X×X→[0,∞); dvojice (X,d) je **metrický prostor**. Pro všechna x,y,z musí platit:

- **pozitivní definitnost:** d(x,y)≥0 a d(x,y)=0 právě když x=y,
- **symetrie:** d(x,y)=d(y,x),
- **trojúhelníková nerovnost:** d(x,y)≤d(x,z)+d(z,y).

## Poznámka Anki 1785269100180

Karty Anki: 1785269200180
GUID: 372c7c7c1079; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Porovnej **L1, L2, L∞ a Levenštejnovu vzdálenost**. Proč volba vzdálenosti mění shlukování?

### Odpověď (Back)

| L2 / eukleidovská | d₂(x,y)=√Σᵢ(xᵢ−yᵢ)² | 
| L1 / manhattanská | d₁(x,y)=Σᵢ|xᵢ−yᵢ| | 
| L∞ / Čebyševova | d∞(x,y)=maxᵢ|xᵢ−yᵢ| | 
| Levenštejnova | Minimální počet vložení, odstranění a nahrazení znaků pro převod jednoho řetězce na druhý. | 

Vzdálenost určuje, které objekty algoritmus považuje za podobné, a proto může zásadně změnit výsledné shluky.

## Poznámka Anki 1785269100181

Karty Anki: 1785269200181
GUID: 26a13e3634ac; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jaké jsou obecné **vstupy a výstupy úlohy shlukování** a jak se liší DBSCAN?

### Odpověď (Back)

Vstupem je metrický prostor (X,d), dataset D⊂X a často požadovaný počet shluků k. Standardním výstupem je rozklad D=C₁∪…∪C<sub>k</sub>: shluky jsou po dvojicích disjunktní a každý bod patří právě do jednoho.

**DBSCAN** může část bodů označit jako šum, takže jeho výstup nemusí být úplným rozkladem D.

## Poznámka Anki 1785269100182

Karty Anki: 1785269200182
GUID: c252261f785b; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jak funguje **aglomerativní a divizní hierarchické shlukování**?

### Odpověď (Back)

- **Aglomerativní (zdola nahoru):** začíná N jednoprvkovými shluky; opakovaně spojí dva nejbližší podle zvoleného linkage. K jedinému shluku potřebuje N−1 spojení. Zastavit lze při požadovaném k nebo maximální vzdálenosti spojení.
- **Divizní (shora dolů):** začíná jedním shlukem všech dat a shluky opakovaně rozděluje.

Aglomerativní metoda tedy spojuje, divizní rozděluje.

## Poznámka Anki 1785269100183

Karty Anki: 1785269200183
GUID: 305d951cf785; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Porovnej **single, complete a average linkage** v hierarchickém shlukování.

### Odpověď (Back)

| Single | D(A,B)=min<sub>x∈A,y∈B</sub>d(x,y). Tvoří i dlouhé řetězcovité shluky; chaining effect může spojit vzdálené útvary řadou lokálně blízkých bodů. | 
| Complete | D(A,B)=max<sub>x∈A,y∈B</sub>d(x,y). Preferuje kompaktní shluky s omezenou vzdáleností všech bodů. | 
| Average | D(A,B)=[1/(|A||B|)]Σ<sub>x∈A,y∈B</sub>d(x,y). Agreguje všechny páry, a je tak kompromisem mezi extrémy single a complete. |

## Poznámka Anki 1785269100184

Karty Anki: 1785269200184
GUID: a283bc97c53b; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co je **Wardovo linkage kritérium** a jak se linkage liší od metriky bodů?

### Odpověď (Back)

Metrika d měří vzdálenost jednotlivých bodů; linkage D z ní či z variability odvozuje vzdálenost celých shluků.

**Wardova metoda** v eukleidovském prostoru ℝᵖ spojuje dvojici, která způsobí nejmenší nárůst celkového součtu čtverců vzdáleností bodů od centroidů, tedy nejmenší nárůst vnitroshlukové kvadratické variability.

## Poznámka Anki 1785269100185

Karty Anki: 1785269200185
GUID: 9b90d0f50d23; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co zobrazuje **dendrogram** a jak z něj získat k shluků?

### Odpověď (Back)

Dendrogram je strom celého hierarchického spojování:

- listy = jednotlivé body / počáteční jednoprvkové shluky,
- vnitřní vrchol = spojení dvou podřazených shluků, jeho výška = jejich vzdálenost při spojení,
- kořen = shluk všech bodů.

Vodorovný řez protínající k větví určí k shluků. Řez lze umístit do výrazné mezery mezi výškami spojení; výhodou je možnost zvolit k až po prohlédnutí celé hierarchie.

## Poznámka Anki 1785269100186

Karty Anki: 1785269200186
GUID: cbc756eaac83; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jakou vlastnost má **hierarchie shluků** při změně k a co měří cophenetic correlation?

### Odpověď (Back)

Při zvýšení počtu shluků o jedna se v hierarchickém řešení rozdělí právě jeden existující shluk; ostatní zůstávají stejné.

**Cophenetic correlation** měří, jak dobře cophenetické vzdálenosti dané výškami společných spojení v dendrogramu zachovávají původní párové vzdálenosti dat.

## Poznámka Anki 1785269100187

Karty Anki: 1785269200187
GUID: 784f76e63ea7; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jaké jsou **výpočetní náklady hierarchického shlukování**?

### Odpověď (Back)

Aglomerativní metoda je na velkých datech náročná kvůli opakovanému vyhodnocování a aktualizaci vzdáleností shluků. Naivně má časovou složitost O(N³); single či complete linkage lze podle materiálu zlepšit na O(N²).

Naivní divizní postup je ještě horší: při dělení shluku velikosti m může porovnávat přibližně 2<sup>m−1</sup> rozdělení, tedy exponenciálně mnoho.

## Poznámka Anki 1785269100188

Karty Anki: 1785269200188
GUID: 559fe107bd27; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jakou **účelovou funkci minimalizuje k-means** a proč je reprezentantem shluku centroid?

### Odpověď (Back)

Pro rozklad C=(C₁,…,C<sub>k</sub>) minimalizuje vnitroshlukový součet čtverců:

**G(C)=ΣᵢΣ<sub>x∈Cᵢ</sub>‖x−x̄ᵢ‖²**, kde x̄ᵢ=(1/|Cᵢ|)Σ<sub>x∈Cᵢ</sub>x.

Centroid je bod μ minimalizující Σ<sub>x∈A</sub>‖x−μ‖². Platí také identita

[1/(2|A|)]Σ<sub>x,y∈A</sub>‖x−y‖² = Σ<sub>x∈A</sub>‖x−x̄‖²,

takže kriterium lze chápat i přes párové vzdálenosti uvnitř shluku.

## Poznámka Anki 1785269100189

Karty Anki: 1785269200189
GUID: 1550f4aef497; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jak probíhá **algoritmus k-means**, proč účelová funkce monotónně klesá a co to nezaručuje?

### Odpověď (Back)

Globální optimalizace je NP-těžká, proto standardní k-means střídá:

1. **Přiřazení:** každý bod k nejbližšímu centroidu; při fixních centroidech to minimalizuje jeho příspěvek.
2. **Aktualizaci:** centroid nahradí průměr bodů shluku; při fixním členství ten minimalizuje součet čtverců.

Každý krok G zachová nebo sníží, ale nezaručí globální minimum: algoritmus může skončit v lokálním minimu. Zastaví se např. při dostatečně malé změně G či centroidů.

## Poznámka Anki 1785269100190

Karty Anki: 1785269200190
GUID: 12fa6c7212af; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Proč k-means závisí na **inicializaci** a jak se tento problém omezuje?

### Odpověď (Back)

Různé počáteční centroidy mohou vést do různých lokálních minim. Lze náhodně vybrat k datových bodů, lépe však použít **k-means++**, který centroidy rozmísťuje prostorově.

K-means se obvykle spustí vícekrát s různými inicializacemi a ponechá se běh s nejnižší konečnou hodnotou účelové funkce.

## Poznámka Anki 1785269100191

Karty Anki: 1785269200191
GUID: 1b6c5f0c3fd6; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jak zvolit **počet shluků k** pro k-means metodou lokte a silhouette skórem?

### Odpověď (Back)

Standardní k-means vyžaduje k předem. Samotné minimum G jej neurčí: s rostoucím k se G nemůže zvýšit a při k=N je 0.

- **Loket:** hledá přechod z prudkého na pozvolný pokles G. Je subjektivní, nemusí být zřetelný a nemusí odpovídat skutečnému počtu skupin.
- **Silhouette:** porovná kompaktnost a oddělení pro různá k; obvykle volíme vyšší průměrné skóre.

## Poznámka Anki 1785269100192

Karty Anki: 1785269200192
GUID: 34378afe3619; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jaké **geometrické předpoklady** má k-means, proč je citlivý na škálování a jaký je jeho meta-princip?

### Odpověď (Back)

K-means preferuje shluky s malým součtem čtverců eukleidovských vzdáleností od centroidu, tedy spíše kompaktní centroidové útvary. Příznaky s velkým číselným rozsahem mohou vzdálenosti dominovat, proto je obvykle nutné vhodné škálování.

Meta-principem je **střídavá optimalizace**: při fixních centroidech optimalizuje přiřazení a při fixním přiřazení centroidy.

## Poznámka Anki 1785269100193

Karty Anki: 1785269200193
GUID: ed9f468ea881; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jaká je myšlenka **hustotního shlukování a DBSCAN** a co znamenají ε a MinPts?

### Odpověď (Back)

Hustotní shlukování hledá souvislé oblasti, kde odhad hustoty překračuje zvolenou úroveň; body mimo ně mohou být šum. **DBSCAN = Density-Based Spatial Clustering of Applications with Noise** a hustotu odhaduje počtem datových bodů v okolí.

V metrickém prostoru (X,d) používá:

- **ε:** poloměr okolí N<sub>ε</sub>(x)={y∈D | d(x,y)≤ε},
- **MinPts:** minimální počet bodů pro hustou oblast.

Okolí zahrnuje i x, protože d(x,x)=0.

## Poznámka Anki 1785269100194

Karty Anki: 1785269200194
GUID: 34ce70c8f57c; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co jsou v DBSCAN **core a border body** a co znamená přímá hustotní dosažitelnost?

### Odpověď (Back)

- **Core bod x:** |N<sub>ε</sub>(x)|≥MinPts.
- **y přímo hustotně dosažitelné z x:** x je core a y∈N<sub>ε</sub>(x).
- **Border bod:** není core, ale je přímo dosažitelný alespoň z jednoho core bodu.

Přímá dosažitelnost je obecně nesymetrická: z core x lze dojít k neklíčovému y, ale ne opačně. Je symetrická, jsou-li oba body core a do vzdálenosti ε.

## Poznámka Anki 1785269100195

Karty Anki: 1785269200195
GUID: 8f039292c3d4; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co znamená v DBSCAN **hustotní dosažitelnost a hustotní spojenost**?

### Odpověď (Back)

**y je hustotně dosažitelné z x**, existuje-li řetězec od x k y, kde je každý další bod přímo dosažitelný z předchozího. Všechny body řetězce kromě případného posledního musí být core. Relace obecně není symetrická.

**x a y jsou hustotně spojené**, existuje-li core bod p, z něhož jsou oba dosažitelné. Spojenost je symetrická. Je-li jeden ze spojených bodů core, druhý je z něj dosažitelný.

## Poznámka Anki 1785269100196

Karty Anki: 1785269200196
GUID: d22513923378; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jak je formálně definován **shluk a šum v DBSCAN**?

### Odpověď (Back)

Shluk je maximální hustotně spojená množina s alespoň jedním core bodem:

- **souvislost:** každé dva body shluku jsou hustotně spojené,
- **maximalita:** každý bod dosažitelný z bodu shluku patří také do shluku.

Obsahuje nejméně MinPts bodů, protože zahrne core bod i celé jeho ε-okolí. Lze jej vytvořit jako všechny body dosažitelné z jednoho core bodu.

**Šum** jsou body mimo všechny shluky; označení během průchodu nemusí být definitivní, protože bod se později může stát border bodem.

## Poznámka Anki 1785269100197

Karty Anki: 1785269200197
GUID: 01ca34b99f74; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jak prakticky probíhá **DBSCAN** a která část výsledku může záviset na pořadí?

### Odpověď (Back)

1. Určí ε-okolí a core body.
2. Spojí sousední core body do zárodků shluků a rozšíří je o dosažitelné body.
3. Neklíčový bod sousedící s core bodem přiřadí jako border; bez core souseda jej označí za šum.

Border bod může sousedit s core body různých shluků a praktická implementace jej přiřadí prvnímu navštívenému. Proto mohou **hraniční body** záviset na pořadí, zatímco klíčové části shluků tuto nejednoznačnost nemají.

## Poznámka Anki 1785269100198

Karty Anki: 1785269200198
GUID: c0f6f7553e4d; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jaká je **časová složitost DBSCAN**?

### Odpověď (Back)

V nejhorším případě O(n²), typicky při naivním hledání okolí. S vhodným prostorovým indexováním lze v mnoha praktických situacích dosáhnout přibližně O(n log n).

## Poznámka Anki 1785269100199

Karty Anki: 1785269200199
GUID: 28ae9de748c1; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jak ladit **ε a MinPts** v DBSCAN a jak se projeví nevhodné hodnoty?

### Odpověď (Back)

- **Malé ε:** více malých shluků a více šumu.
- **Velké ε:** oddělené oblasti se mohou slít do jednoho shluku.
- **Vyšší MinPts:** bod potřebuje hustší okolí, aby byl core; ε bývá citlivější parametr.

MinPts se orientačně volí např. 4–6 či podle dimenze p; ε lze hledat z grafu vzdáleností ke zvolenému pořadovému sousedovi. Orientační podíl šumu může být 1–30 %. Obsahuje-li největší shluk přes polovinu dat, ε může být příliš velké; lze je zmenšit nebo použít např. HDBSCAN.

## Poznámka Anki 1785269100200

Karty Anki: 1785269200200
GUID: 8e5c866fa175; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jaké výhody má **DBSCAN** a jak se principiálně liší od k-means a hierarchického shlukování?

### Odpověď (Back)

- Najde i nekonvexní a nepravidelné shluky.
- Odlehlé body může označit jako šum.
- Nevyžaduje k; počet shluků plyne z ε a MinPts.

**k-means** přiřadí všechny body do předem daného počtu centroidových shluků. **Hierarchické shlukování** tvoří vnořenou strukturu spojování či dělení. **DBSCAN** vytváří shluky z lokální hustotní dosažitelnosti.

## Poznámka Anki 1785269100201

Karty Anki: 1785269200201
GUID: bd4d47dfd027; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jak se definuje **silhouette skóre bodu** pomocí a(x) a b(x)?

### Odpověď (Back)

Pro bod x ve shluku C<sub>j(x)</sub>:

- **a(x)** = průměrná vzdálenost od ostatních bodů vlastního shluku:
a(x)=[1/(|C<sub>j(x)</sub>|−1)]Σ<sub>y∈Cj(x), y≠x</sub>d(x,y).
- d(x,Cᵢ)=(1/|Cᵢ|)Σ<sub>y∈Cᵢ</sub>d(x,y).
- **b(x)**=min<sub>i≠j(x)</sub>d(x,Cᵢ), tedy vzdálenost k nejbližšímu konkurenčnímu shluku.

**s(x)=[b(x)−a(x)]/max{a(x),b(x)}**.

## Poznámka Anki 1785269100202

Karty Anki: 1785269200202
GUID: f37a55cf14ed; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

V jakém intervalu leží **silhouette skóre** a jak se interpretuje?

### Odpověď (Back)

s(x)∈[−1,1]:

- **blízko 1:** a(x)≪b(x), bod je dobře uvnitř vlastního shluku,
- **blízko 0:** bod leží přibližně na hranici shluků,
- **blízko −1:** a(x)>b(x), bod je blíže jinému shluku a patrně špatně zařazen.

Obecně a(x)<b(x) dává kladné a a(x)>b(x) záporné skóre.

## Poznámka Anki 1785269100203

Karty Anki: 1785269200203
GUID: 87b1710e16a9; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jak se **silhouette skóre agreguje a používá** k hodnocení shlukování?

### Odpověď (Back)

Skóre shluku je průměr s(x) jeho bodů; celkové skóre je průměr přes celý dataset. Vyšší hodnota znamená v průměru kompaktnější a lépe oddělené shluky. Pro výběr k lze porovnat řešení a zvolit nejvyšší průměr.

Proti samotné účelové funkci k-means hodnotí i oddělení od konkurentů. Vyžaduje definovanou vzdálenost mezi body; při jediném shluku se v materiálu definuje jako 0.

## Poznámka Anki 1785269100204

Karty Anki: 1785269200204
GUID: 7d898afe6a20; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co je **analýza asociačních pravidel**, analýza nákupního košíku a itemset?

### Odpověď (Back)

Asociační analýza hledá kombinace hodnot příznaků, které se často vyskytují spolu, tedy oblasti prostoru s vysokou pravděpodobností. Obecné konjunktivní pravidlo je průnik podmínek ∩<sub>j=1</sub><sup>p</sup>(Xⱼ∈sⱼ).

V **market-basket analýze** je Xⱼ∈{0,1} přítomnost položky j. **Itemset K** je množina položek a odpovídá události ∩<sub>j∈K</sub>(Xⱼ=1), že jsou všechny současně v transakci.

## Poznámka Anki 1785269100205

Karty Anki: 1785269200205
GUID: 9924014819b3; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co je **podpora itemsetu**, častý itemset a princip Apriori?

### Odpověď (Back)

Podpora je podíl N transakcí obsahujících celý K:

**T(K)=(1/N)Σᵢ∏<sub>j∈K</sub>xᵢⱼ** ≈ P(∩<sub>j∈K</sub>(Xⱼ=1)).

Itemset je častý, překročí-li T(K) minimální mez t. **Apriori** využívá antimonotónnost podpory: přidáním položky podpora nemůže vzrůst, protože každá transakce s nadmnožinou obsahuje i podmnožinu. Není-li podmnožina častá, žádná její nadmnožina nemůže být častá, a větev se prořeže.

## Poznámka Anki 1785269100206

Karty Anki: 1785269200206
GUID: cfd4cac154a3; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co je **asociační pravidlo A⇒B**, antecedent, consequent a jeho support?

### Odpověď (Back)

A a B jsou disjunktní části itemsetu K, A∪B=K. **A** je antecedent/předpoklad a **B** consequent/závěr.

Podpora pravidla je **T(A∪B)**, tedy odhad pravděpodobnosti, že se A a B vyskytnou současně.

## Poznámka Anki 1785269100207

Karty Anki: 1785269200207
GUID: 9bc19874db29; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co je **confidence asociačního pravidla** a proč sama nestačí?

### Odpověď (Back)

**C(A⇒B)=T(A∪B)/T(A)≈P(B|A)**. Confidence 0,75 znamená, že 75 % transakcí obsahujících A obsahuje i B. Pravidla se typicky filtrují minimální podporou t a confidence c.

Vysoká confidence nemusí být zajímavá, je-li B běžné i bez A; může pouze odrážet vysokou základní četnost B.

## Poznámka Anki 1785269100208

Karty Anki: 1785269200208
GUID: 22b606d4cc34; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co je **lift asociačního pravidla** a jak se interpretuje?

### Odpověď (Back)

**L(A⇒B)=C(A⇒B)/T(B)≈P(B|A)/P(B)**. Koriguje confidence o běžnou četnost závěru B:

- L>1: A je spojeno s vyšší pravděpodobností B,
- L≈1: A pravděpodobnost B přibližně nemění, což odpovídá nezávislosti,
- L<1: A je spojeno s nižší pravděpodobností B.

## Poznámka Anki 1785269100209

Karty Anki: 1785269200209
GUID: 52701a422070; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Co je v materiálu **coverage pravidla** a jak se liší support, confidence, coverage a lift?

### Odpověď (Back)

**Coverage(A⇒B)=T(A∪B)/T(B)≈P(A|B)**: jaká část případů se závěrem B obsahuje i A.

| Support | P(A∩B): společná četnost v celých datech. | 
| Confidence | P(B|A): četnost B mezi případy s A. | 
| Coverage | P(A|B): četnost A mezi případy s B. | 
| Lift | P(B|A)/P(B): relativní zesílení B podmínkou A. |

## Poznámka Anki 1785269100210

Karty Anki: 1785269200210
GUID: 6d9a5c318f86; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Spočítej **support, confidence, lift a coverage** pravidla {párky}⇒{hořčice,chléb}.

### Odpověď (Back)

Je-li T(A∪B)=0,06, T(A)=0,08 a T(B)=0,15:

- **support**=0,06,
- **confidence**=0,06/0,08=0,75,
- **lift**=0,75/0,15=5: B se po A vyskytuje pětkrát častěji než běžně,
- **coverage**=0,06/0,15=0,4: ve 40 % transakcí s B se vyskytuje A.

## Poznámka Anki 1785269100211

Karty Anki: 1785269200211
GUID: 2f91ac994c9f; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jaká jsou hlavní **omezení a kroky analýzy nákupního košíku**?

### Odpověď (Back)

Postup: binárně zakódovat transakce → najít časté itemsety → rozdělit je na pravidla A⇒B → filtrovat podle podpory a confidence a posoudit např. lift.

- Vysoká minimální podpora může skrýt vzácné, ale velmi silné vztahy (např. doutník⇒rum).
- Asociace není kauzalita: společný výskyt může způsobit třetí proměnná, výběr dat či náhoda.

## Poznámka Anki 1785269100212

Karty Anki: 1785269200212
GUID: 24a38735ad9f; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jaký společný pravděpodobnostní rámec spojuje **shlukování a asociační pravidla**?

### Odpověď (Back)

Obě metody hledají oblasti prostoru příznaků s vysokou koncentrací pravděpodobnosti. **Shlukování** je popisuje geometricky pomocí vzdálenosti, kompaktnosti či hustotní souvislosti; **asociační pravidla** je popisují konjunkcemi konkrétních hodnot příznaků.

## Poznámka Anki 1785269100213

Karty Anki: 1785269200213
GUID: 5c4da421b46f; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Souhrnně porovnej **hierarchické shlukování, k-means a DBSCAN**.

### Odpověď (Back)

| Hierarchické | Vnořená struktura spojování/dělení; shluk určuje linkage vůči jiným shlukům; k lze zvolit až řezem dendrogramu. | 
| k-means | Centroidové kompaktní shluky; k předem; každý bod musí patřit do shluku. | 
| DBSCAN | Hustotně propojené oblasti; počet shluků plyne z ε a MinPts; odlehlé body mohou být šum. | 

Žádný algoritmus není univerzálně nejlepší: každý formalizuje shluk jinak a vyhovuje jiné geometrii, hustotě a výpočetním podmínkám.

## Poznámka Anki 1785269100214

Karty Anki: 1785269200214
GUID: 1bea14297163; štítky: 09_Nesupervizovane_uceni BI-ML1 konsolidace.

### Otázka (Front)

Jaký je celkový proces **nesupervizované analýzy dat**?

### Odpověď (Back)

1. Zvolit reprezentaci dat a smysluplnou míru podobnosti.
2. Vybrat model hledané struktury.
3. Naladit jeho hyperparametry.
4. Výsledek interně evaluovat.
5. Interpretovat jej vzhledem k doméně.

Protože neexistuje cílová proměnná, jsou volba reprezentace, kritéria a doménová interpretace podstatnou součástí výsledku.

