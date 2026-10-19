# BI-ML1 – 02 Hyperparametry, regresni stromy a kNN

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::3 BI-ML1::02 Hyperparametry, regresni stromy a kNN
Rozsah: 23 poznámek, 23 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785269100017

Karty Anki: 1785269200017
GUID: 9c5e080b0ae8; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak správně rozdělit data na **trénovací, validační a testovací** část a k čemu slouží křížová validace?

### Odpověď (Back)

- **Trénovací data:** odhad parametrů.
- **Validační data:** výběr modelu a hyperparametrů.
- **Testovací data:** až závěrečný nezávislý odhad generalizační chyby; ani nepřímé ladění podle testu není dovoleno.

Rozdělení bývá náhodné, protože pořadí řádků může odrážet čas, skupiny, cíl či jinou strukturu; prosté „první řádky train, poslední test“ tak může vytvořit nereprezentativní části. Univerzální poměr neexistuje. Příklad heuristiky: 20 % všech dat test, 20 % ze zbytku validace a zbytek trénink.

**Křížová validace** opakovaně střídá trénovací a validační části netestovacích dat, takže ladění méně závisí na jediném náhodném rozdělení.

## Poznámka Anki 1785269100018

Karty Anki: 1785269200018
GUID: f2426d0338ce; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Co je **one-hot encoding**, jak vypadá pro kategorie A/B/C a jaké má výhody a nevýhody u binárně větveného stromu?

### Odpověď (Back)

Kategorii s n hodnotami nahradí n **dummy** indikátory (1 = objekt patří do kategorie, jinak 0). Pro A/B/C: A=(1,0,0), B=(0,1,0), C=(0,0,1).

- **Výhoda:** vícehodnotový příznak převede na binární otázky použitelné binárně větveným stromem a nezavádí pořadí kategorií.
- **Nevýhoda:** vysoká kardinalita výrazně zvýší dimenzi, výpočetní nároky a riziko přeučení.
- I bez ztráty informace může zhoršit hladový strom: informace se rozdělí mezi více indikátorů a algoritmus každý posuzuje pouze lokálně.

## Poznámka Anki 1785269100019

Karty Anki: 1785269200019
GUID: 3920bf930390; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Porovnej **nominální** a **ordinální** příznaky a jejich vhodné kódování.

### Odpověď (Back)

| Typ | Význam | Vhodná reprezentace | 
| Nominální | Kategorie bez přirozeného pořadí, např. místo narození či fakulta. | Typicky one-hot. Prosté číselné kódy by uměle zavedly pořadí a vzdálenosti. | 
| Ordinální | Kategorie s přirozeným pořadím, např. vzdělání či spokojenost. | Lze číselně seřadit a ve stromu používat prahové splity. |

## Poznámka Anki 1785269100020

Karty Anki: 1785269200020
GUID: 1ccc095fa44e; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak rozhodovací strom hledá a používá split **spojitého příznaku**?

### Odpověď (Back)

1. Spojitý příznak modelujeme jako hodnotu z intervalu a dělíme pravidlem např. **X ≤ d**.
2. Unikátní pozorované hodnoty se seřadí; stačí zkoušet středy mezi sousedními hodnotami, protože jiné prahy ve stejném intervalu rozdělí trénovací data totožně.
3. Pro každý příznak a kandidátní práh se spočítá zlepšení kritéria a vybere se nejlepší dvojice.

Stejný spojitý příznak se může na jedné větvi opakovat s různými prahy a vymezit intervaly. Binární příznak se tam obvykle neopakuje, protože po prvním testu je konstantní. Při mnoha hodnotách lze zkoušet jen podmnožinu prahů. Shodně kvalitní splity mohou být rozhodnuty náhodně, takže konstrukce nemusí být deterministická.

## Poznámka Anki 1785269100021

Karty Anki: 1785269200021
GUID: acd25d789829; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak se klasifikační strom převádí na **regresní strom** a jakou predikci dává jeho list?

### Odpověď (Back)

Je nutné (1) určit číselnou predikci listu a (2) nahradit třídní nečistotu kritériem pro spojitý cíl. List obvykle predikuje **aritmetický průměr** cílových hodnot, které do něj dopadly; hodnoty proto chceme soustředit těsně kolem průměru. Např. průměr 10, 15, 20, 25, 30, 35 je **22,5**.

Entropie tříd se nehodí, protože spojitý cíl zpravidla nemá malou konečnou množinu třídních podílů.

## Poznámka Anki 1785269100022

Karty Anki: 1785269200022
GUID: 596a28f370a5; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak regresní strom používá **MSE** k hodnocení uzlu a splitu?

### Odpověď (Back)

Pro uzel s N cíli a jejich průměrem Ȳ:

**MSE(D) = (1/N) Σ<sub>i</sub>(Y<sub>i</sub>−Ȳ)<sup>2</sup>**.

Měří průměrnou kvadratickou odchylku od predikce uzlu. Zlepšení splitu:

**MSE(D) − t<sub>L</sub>MSE(D<sub>L</sub>) − t<sub>R</sub>MSE(D<sub>R</sub>)**,

kde t<sub>L</sub>, t<sub>R</sub> jsou podíly vzorků v potomcích. Váhy jsou nutné, protože velký potomek ovlivňuje očekávanou chybu více. Strom preferuje největší snížení.

## Poznámka Anki 1785269100023

Karty Anki: 1785269200023
GUID: 6f4565ab6780; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak je definována **MAE** a jak se liší od MSE?

### Odpověď (Back)

**MAE = (1/N) Σ<sub>i</sub>|Y<sub>i</sub>−ŷ<sub>i</sub>|**; při měření variability uzlu se ŷ volí jako jeho reprezentativní hodnota.

- **MSE** chyby umocňuje, takže velké odchylky penalizuje výrazněji.
- **MAE** roste s velikostí chyby lineárně.

## Poznámka Anki 1785269100024

Karty Anki: 1785269200024
GUID: e1162e6632e7; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jaké jsou hlavní výhody a nevýhody rozhodovacích stromů, co je **prořezávání** a co znamená CART?

### Odpověď (Back)

**Výhody:** predikci lze vysvětlit pravidly na cestě kořen→list; numerické škálování není obvykle nutné, protože splity závisí na pořadí a prazích, nikoli vzdálenostech. Přímá práce s kategoriemi či chybějícími hodnotami závisí na konkrétní implementaci.

**Nevýhody:** jsou nerobustní (malá změna dat může změnit časný split i celý strom) a bez omezení se snadno přeučí malými specifickými listy.

**Prořezávání** odstraňuje větve s malým přínosem ke generalizaci. **CART** = Classification and Regression Trees, rodina metod pro klasifikační i regresní stromy, typicky s binárním větvením.

## Poznámka Anki 1785269100025

Karty Anki: 1785269200025
GUID: fa7b3143cbd1; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Na jakém principu funguje **kNN**, jaká má trénovací data a jak predikuje klasifikaci či regresi?

### Odpověď (Back)

Z dvojic **(x<sub>i</sub>,Y<sub>i</sub>)** vyhledá podle zvolené metriky k trénovacích bodů nejbližších novému vstupu.

- **Klasifikace, uniformní váhy:** nejčetnější třída sousedů.
- **Regrese, uniformní váhy:** aritmetický průměr jejich cílů.

Hlavní hyperparametry jsou **počet k, metrika vzdálenosti a způsob vážení sousedů**.

## Poznámka Anki 1785269100026

Karty Anki: 1785269200026
GUID: 03149118ffaa; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Co je **metrika** a jaké tři vlastnosti musí splňovat?

### Odpověď (Back)

Metrika je funkce **d:X×X→[0,∞)** splňující:

1. **pozitivní definitnost:** d(x,y)≥0 a d(x,y)=0 právě tehdy, když x=y;
2. **symetrii:** d(x,y)=d(y,x);
3. **trojúhelníkovou nerovnost:** d(x,y)≤d(x,z)+d(z,y).

## Poznámka Anki 1785269100027

Karty Anki: 1785269200027
GUID: 9cb23b62d033; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak jsou definovány **Minkowského, eukleidovská a manhattanská** vzdálenost?

### Odpověď (Back)

**Minkowského L<sub>q</sub>:** d<sub>q</sub>(x,y)=(Σ<sub>i</sub>|x<sub>i</sub>−y<sub>i</sub>|<sup>q</sup>)<sup>1/q</sup>, q≥1.

- **Eukleidovská L2:** q=2, tedy √(Σ<sub>i</sub>(x<sub>i</sub>−y<sub>i</sub>)²).
- **Manhattanská L1:** q=1, tedy Σ<sub>i</sub>|x<sub>i</sub>−y<sub>i</sub>|.

## Poznámka Anki 1785269100028

Karty Anki: 1785269200028
GUID: 52189a390326; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Proč je kNN **lazy learning** a jaký má výpočetní profil oproti rozhodovacímu stromu?

### Odpověď (Back)

Základní kNN při „tréninku“ hlavně uloží data; většina práce nastane až při predikci. Naivně počítá vzdálenost ke všem n trénovacím bodům, takže práce jedné predikce roste přibližně lineárně s n.

Rozhodovací strom má naopak náročnější konstrukci, ale rychlou predikci. kNN lze urychlit prostorovým indexem či vyhledávací strukturou: více práce při přípravě výměnou za levnější některé predikce.

## Poznámka Anki 1785269100029

Karty Anki: 1785269200029
GUID: dbd93d4963d4; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak hyperparametr **k** řídí složitost, přeučení a kompromis bias–variance v kNN?

### Odpověď (Back)

- **Malé k:** velmi lokální, nepravidelná hranice; vysoká variabilita a citlivost na šum. Při k=1 může každý bod vytvořit izolovanou oblast a model se přeučí.
- **Velké k:** vyhlazuje lokální variace a snižuje citlivost na jednotlivé body, ale může potlačit skutečnou jemnou strukturu a mít vysoké systematické zkreslení.

k tedy řídí kompromis **lokální flexibilita / vyhlazení**, resp. variance / bias.

## Poznámka Anki 1785269100030

Karty Anki: 1785269200030
GUID: d79ec3658e52; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Proč volba **metriky** zásadně mění kNN a jak lze pracovat se smíšenými typy příznaků?

### Odpověď (Back)

Metrika určuje geometrii podobnosti, tedy kteří body jsou sousedé a jaká bude predikce. Pro numerické, textové a kategorické části lze použít vhodné dílčí míry nepodobnosti a zkombinovat je vahami.

Tím však vznikají další strukturální volby a váhy, tedy nové hyperparametry, které je nutné věcně navrhnout nebo naladit.

## Poznámka Anki 1785269100031

Karty Anki: 1785269200031
GUID: 742ce715e5d7; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak funguje **vzdálenostně vážená** regrese kNN a jaký problém má váha 1/d?

### Odpověď (Back)

**ŷ = (Σ<sub>i</sub>w<sub>i</sub>y<sub>i</sub>)/(Σ<sub>i</sub>w<sub>i</sub>)**, w<sub>i</sub>≥0.

Váhy často klesají se vzdáleností, protože bližší sousedé jsou pro lokální predikci relevantnější; např. **w<sub>i</sub>=1/d(x,x<sub>i</sub>)**. Je-li d=0, výraz 1/0 není definován a implementace musí shodný bod ošetřit zvláštním pravidlem.

## Poznámka Anki 1785269100032

Karty Anki: 1785269200032
GUID: 4dfb3127a9b1; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Proč je kNN citlivé na **měřítko numerických příznaků** a proč problém nevyřeší vždy jen sjednocení fyzikálních jednotek?

### Odpověď (Back)

Příznak s větším číselným rozsahem může ovládnout vzdálenost bez ohledu na věcnou důležitost. Např. stejná změna vyjádřená jako 500 cm má číselně stokrát větší rozdíl než 5 m.

Příznaky navíc často měří nesouměřitelné věci (plocha, počet oken, velikost obrazovky), pro které společná fyzikální jednotka vůbec neexistuje; potřebujeme vhodné škálování a metriku.

## Poznámka Anki 1785269100033

Karty Anki: 1785269200033
GUID: cc23aeb24ebf; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak funguje **min–max normalizace** a jak se má korektně použít na train/validation/test?

### Odpověď (Back)

**x ← (x−min<sub>train</sub>)/(max<sub>train</sub>−min<sub>train</sub>)**; trénovací minimum převede na 0 a maximum na 1. Omezuje dominanci příznaků s velkým rozsahem.

Minimum a maximum se odhadnou **jen na trénovacích datech**; stejnými hodnotami se transformují validace, test i budoucí vstupy. Jinak vzniká datový únik. U konstantního trénovacího příznaku je jmenovatel nulový; příznak nemá variabilitu a musí se odstranit či zvlášť ošetřit.

## Poznámka Anki 1785269100034

Karty Anki: 1785269200034
GUID: 4df08c41e643; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Co je **standardizace** a proč není škálování každého příznaku samostatně univerzálně správné? Uveď příklad MNIST.

### Odpověď (Back)

**x ← (x−x̄<sub>train</sub>)/s<sub>train</sub>**; trénovací hodnoty pak mají přibližně průměr 0 a směrodatnou odchylku 1.

Vhodná transformace závisí na významu, datovém typu a metrice. U MNIST mají všechny pixely stejné jednotky i rozsah. Samostatný min–max pro téměř vždy černý pixel by mohl neúměrně zesílit nepatrné odchylky; přirozenější je všechny intenzity 0–255 společně dělit 255 a převést je do [0,1].

## Poznámka Anki 1785269100035

Karty Anki: 1785269200035
GUID: 08ce4aadcb82; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak měřit nepodobnost **nominálního příznaku** v kNN a jak se liší jednoduchá neshoda od one-hot vzdálenosti?

### Odpověď (Back)

Běžná číselná vzdálenost mezi kódy kategorií nedává smysl: kód 2 nemusí být podobnější 3 než 20. Jednoduchá míra je **0 při shodě, 1 při neshodě**.

One-hot převádí kategorie na binární rozměry, takže je lze zahrnout do číselné vzdálenosti. Není však bez úpravy totožný s 0/1 neshodou: dvě různé one-hot kategorie se např. v eukleidovské vzdálenosti liší ve dvou souřadnicích, takže příspěvek závisí na metrice a škálování.

## Poznámka Anki 1785269100036

Karty Anki: 1785269200036
GUID: e30f49308ea9; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Co je **prokletí dimenzionality** a proč zvlášť poškozuje kNN?

### Odpověď (Back)

Ve vysoké dimenzi při pevném počtu vzorků:

- objem prostoru rychle roste, data řídnou a typické vzdálenosti se zvětšují;
- relativní rozdíl mezi blízkými a vzdálenými body se zmenšuje (koncentrace vzdáleností).

„Nejbližší“ soused je proto méně lokální, méně reprezentativní a méně odlišitelný od ostatních, právě přitom kNN stojí na blízkých reprezentativních sousedech.

## Poznámka Anki 1785269100037

Karty Anki: 1785269200037
GUID: 29af8d95e346; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak příklad podkrychle ilustruje ztrátu lokálnosti ve vysoké dimenzi?

### Odpověď (Back)

Má-li d-rozměrná podkrychle jednotkové hyperkrychle zabírat podíl objemu r, její strana musí splňovat **a<sup>d</sup>=r**, tedy **a=r<sup>1/d</sup>**.

Pro r=0,01 je a=(0,01)<sup>1/d</sup> a s dimenzí se blíží 1. V 50 dimenzích je a≈0,91: oblast obsahující jen 1 % objemu už zasahuje asi 91 % rozsahu každé osy. „Lokální“ okolí tak přestává být lokální v běžném smyslu.

## Poznámka Anki 1785269100038

Karty Anki: 1785269200038
GUID: 2d3c80f33733; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jak lze zmírnit prokletí dimenzionality a proč je nevyřeší samotná normalizace ani snadno více dat?

### Odpověď (Back)

- **Výběr příznaků** odstraní nepotřebné či redundantní rozměry.
- **Redukce dimenzionality** data popíše menším počtem rozměrů.

Pro zachování stejné lokální hustoty roste potřebný počet vzorků s dimenzí velmi rychle, typicky exponenciálně vzhledem k požadovanému rozlišení. Normalizace opraví nepoměr měřítek, ale nikoli řídnutí dat ani koncentraci vzdáleností způsobenou samotným počtem rozměrů.

## Poznámka Anki 1785269100039

Karty Anki: 1785269200039
GUID: f9f58daefc3b; štítky: 02_Hyperparametry_regresni_stromy_a_kNN BI-ML1 konsolidace.

### Otázka (Front)

Jaké stavební prvky tvoří kNN a jak přesně probíhá jeho predikce? Proč kvalitu nelze oddělit od reprezentace dat?

### Odpověď (Back)

**Prvky:** reprezentace příznaků, metrika podobnosti, počet sousedů k, pravidlo vah a agregace pro klasifikaci či regresi.

1. Transformovat vstup stejně jako trénovací data.
2. Spočítat vzdálenosti.
3. Vybrat k nejbližších bodů.
4. Určit jejich váhy.
5. Agregovat cíle.

kNN nemá vlastní parametrickou strukturu, která by napravila nevhodné příznaky; jeho chování přímo určuje geometrie zvolené reprezentace a metriky.

