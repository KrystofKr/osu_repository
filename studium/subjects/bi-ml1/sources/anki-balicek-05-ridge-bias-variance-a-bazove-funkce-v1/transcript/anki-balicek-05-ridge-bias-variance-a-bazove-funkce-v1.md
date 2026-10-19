# BI-ML1 – 05 Ridge, bias-variance a bazove funkce

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::3 BI-ML1::05 Ridge, bias-variance a bazove funkce
Rozsah: 29 poznámek, 29 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785269100090

Karty Anki: 1785269200090
GUID: fb7a03c26665; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jaká je **geometrická interpretace OLS** a co je sloupcový prostor matice X?

### Odpověď (Back)

**Sloupcový prostor** je množina všech lineárních kombinací sloupců X: **{Xw | w∈R<sup>p+1</sup>}**. Xw v něm vždy leží, protože je lineární kombinací sloupců s vahami w.

OLS hledá Xw s nejmenší eukleidovskou vzdáleností od Y; minimalizace ‖Y−Xw‖ a její druhé mocniny RSS je ekvivalentní. Výsledné **Xŵ je ortogonální projekce Y do sloupcového prostoru X**.

## Poznámka Anki 1785269100091

Karty Anki: 1785269200091
GUID: 9ab24525f308; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak **ortogonalita rezidua** vede k normální rovnici a proč zaručuje globální minimum OLS?

### Odpověď (Back)

Nejbližší bod Xŵ splňuje, že reziduum **r=Y−Xŵ** je kolmé na celý sloupcový prostor. Stačí kolmost ke každému sloupci, protože sloupce prostor generují:

**Xᵀr=Xᵀ(Y−Xŵ)=0 ⇒ XᵀXŵ=XᵀY**.

Normální rovnice tedy říká, že reziduum je kolmé na každý směr možných změn predikce Xw. Xŵ je proto nejbližší bod/projekce a každé řešení rovnice globálně minimalizuje RSS.

## Poznámka Anki 1785269100092

Karty Anki: 1785269200092
GUID: 7614507fb589; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Co plyne z ortogonality OLS reziduí při **interceptu** a jak se liší jednoznačnost koeficientů a trénovacích predikcí?

### Odpověď (Back)

Obsahuje-li X sloupec jedniček, z Xᵀr=0 plyne **Σr<sub>i</sub>=0**.

Koeficienty jsou jednoznačné jen při lineární nezávislosti sloupců X (regularitě XᵀX). I když jednoznačné nejsou, **trénovací predikce Xŵ jsou jednoznačné**: všechna OLS řešení představují stejnou projekci Y.

## Poznámka Anki 1785269100093

Karty Anki: 1785269200093
GUID: 5c0438d35142; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak spolu souvisejí **lineární nezávislost sloupců X, nulový prostor, hodnost a regularita XᵀX**?

### Odpověď (Back)

- Sloupce X jsou nezávislé právě tehdy, když **Xs=0 ⇒ s=0**.
- **ker(XᵀX)=ker(X)**, protože sᵀXᵀXs=‖Xs‖²; z XᵀXs=0 tedy plyne Xs=0.
- XᵀX je regulární právě tehdy, když má X plnou sloupcovou hodnost p+1.
- Je nutné N≥p+1, protože v R<sup>N</sup> nemůže být více než N nezávislých sloupců; podmínka však není dostačující, příznakové sloupce mohou být závislé i při mnoha řádcích.

## Poznámka Anki 1785269100094

Karty Anki: 1785269200094
GUID: 16ca7af287ca; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak vzniká přesná lineární závislost příznaků a kolik řešení má OLS při regulární a singulární XᵀX?

### Odpověď (Back)

Závislost vznikne např. duplicitním příznakem nebo příznakem, který je přesnou lineární kombinací jiných; více pozorování strukturální algebraickou závislost neodstraní.

- **Regulární XᵀX:** právě jedno řešení (XᵀX)<sup>−1</sup>XᵀY.
- **Singulární XᵀX:** nekonečně mnoho řešení minimalizujících RSS. Neexistence řešení nehrozí, protože XᵀY vždy leží v obrazu XᵀX.

## Poznámka Anki 1785269100095

Karty Anki: 1785269200095
GUID: 026509a26724; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak spolu souvisejí dvě různá OLS řešení při singulární XᵀX a proč dávají stejné predikce i RSS?

### Odpověď (Back)

Pro dvě řešení w,w′ platí **X(w−w′)=0**, tedy jejich rozdíl leží v ker(X). Proto **Xw=Xw′**, mají stejné reziduum Y−Xw i stejnou hodnotu RSS. Minimum je neostré: tvoří je celá afinní množina koeficientů.

## Poznámka Anki 1785269100096

Karty Anki: 1785269200096
GUID: 33e806490f1e; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak získat OLS řešení bez inverze XᵀX a jaké řešení vybírá **Moorova–Penroseova pseudoinverze**?

### Odpověď (Back)

Lze použít pseudoinverzi nebo numerický algoritmus založený na rozkladu matice. Zápis pomocí pseudoinverze XᵀX:

**ŵ=(XᵀX)<sup>+</sup>XᵀY**.

Mezi všemi řešeními nejmenších čtverců vybere řešení s nejmenší eukleidovskou normou koeficientů.

## Poznámka Anki 1785269100097

Karty Anki: 1785269200097
GUID: 99acb32042c3; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Co je **kolinearita**, jak se liší přesná a přibližná a proč je problémem i téměř závislá matice?

### Odpověď (Back)

Kolinearita znamená přesnou nebo téměř lineární závislost sloupců X.

- **Přesná:** existuje nenulové v s Xv=0.
- **Přibližná:** pro jednotkové v je ‖Xv‖ velmi malé, zatímco v jiných jednotkových směrech může být ‖Xu‖ velké.

Při přibližné kolinearitě může být XᵀX formálně invertibilní, ale inverze a koeficienty jsou extrémně citlivé na malé změny dat.

## Poznámka Anki 1785269100098

Karty Anki: 1785269200098
GUID: f09d45a7cc9c; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak kolinearita ovlivňuje **rozptyl koeficientů, predikce a interpretaci**?

### Odpověď (Back)

- Mezi mírně odlišnými trénovacími výběry se koeficienty mohou silně měnit; ve špatně identifikovaných směrech mají vysoký rozptyl.
- V některých vstupech se vysoký rozptyl přenese i na predikce.
- Na oblasti pokryté daty však mohou být predikce stabilnější než koeficienty, protože různé velké koeficienty vytvoří podobné Xw.
- Jednotlivé koeficienty se špatně interpretují: data nedokážou oddělit příspěvky závislých příznaků.

## Poznámka Anki 1785269100099

Karty Anki: 1785269200099
GUID: 90818f1431af; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jaké jsou tři základní strategie řešení **kolinearity** a kdy pomohou další data?

### Odpověď (Back)

1. **Vhodnější nebo další data:** pomohou, je-li téměř závislá struktura jen důsledkem omezeného výběru; nepomohou při strukturální vazbě příznaků.
2. **Redukce/transformace příznaků:** odstranit redundantní sloupce nebo je nahradit menším počtem nezávislejších.
3. **Regularizace:** změnit účelovou funkci, omezit nestabilní velké koeficienty a získat stabilnější, jednoznačnější řešení.

## Poznámka Anki 1785269100100

Karty Anki: 1785269200100
GUID: f376291c3410; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Co je **hřebenová (Ridge) regrese**, jakou má účelovou funkci a jak působí λ?

### Odpověď (Back)

Ridge je lineární regrese s L2 penalizací neinterceptových koeficientů:

**RSS<sub>λ</sub>(w)=‖Y−Xw‖²+λΣ<sub>j=1</sub><sup>p</sup>w<sub>j</sub>²**, λ≥0.

- λ=0 dává OLS.
- Rostoucí λ silněji stahuje koeficienty k nule a řídí kompromis přizpůsobení/stabilita.
- Intercept se obvykle nepenalizuje, aby se průměrná úroveň predikcí zbytečně nestahovala k nule.

## Poznámka Anki 1785269100101

Karty Anki: 1785269200101
GUID: 4159f4ee9382; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak se Ridge zapíše pomocí matice I′ a jak vypadají jeho **gradient, normální rovnice a uzavřený odhad**?

### Odpověď (Back)

Pro nepenalizovaný intercept použijeme **I′=diag(0,1,…,1)**, takže Σ<sub>j=1</sub><sup>p</sup>w<sub>j</sub>²=wᵀI′w.

- **Gradient:** −2Xᵀ(Y−Xw)+2λI′w.
- **Normální rovnice:** (XᵀX+λI′)w=XᵀY.
- **Odhad:** ŵ<sub>λ</sub>=(XᵀX+λI′)<sup>−1</sup>XᵀY.

## Poznámka Anki 1785269100102

Karty Anki: 1785269200102
GUID: c2625139c170; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Proč má Ridge pro λ>0 **jediné stabilní řešení** i při kolinearitě?

### Odpověď (Back)

Hessián je **2(XᵀX+λI′)**. Pro nenulové s:

**sᵀ(XᵀX+λI′)s=‖Xs‖²+λΣ<sub>j=1</sub><sup>p</sup>s<sub>j</sub>²>0**.

Penalizace pokryje všechny neinterceptové směry a čistý interceptový směr není v ker(X), protože interceptový sloupec tvoří jedničky. Matice je tedy pozitivně definitní, účelová funkce ostře konvexní a má jediné globální minimum. λI′ odstraní ploché směry a penalizací velkých norem stabilizuje špatně identifikované koeficienty.

## Poznámka Anki 1785269100103

Karty Anki: 1785269200103
GUID: 5f0cd22296ac; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak se liší **Ridge a Lasso** z hlediska penalizace a nulových koeficientů?

### Odpověď (Back)

| Ridge | Lasso | 
| L2: λΣw<sub>j</sub>². Koeficienty zmenšuje, ale při konečném λ je obvykle nenuluje přesně. | L1: λΣ|w<sub>j</sub>|. Může vytvářet přesně nulové koeficienty, a tím vybírat příznaky. |

## Poznámka Anki 1785269100104

Karty Anki: 1785269200104
GUID: 512b6203b3a2; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Proč před Ridge obvykle **standardizovat příznaky** a jak korektně vybrat λ?

### Odpověď (Back)

Bez standardizace má stejná penalizace koeficientů jiný praktický účinek pro různé jednotky a měřítka. Od příznaku odečteme **trénovací průměr** a vydělíme **trénovací směrodatnou odchylkou**; stejné hodnoty použijeme na validaci, test a budoucí data.

λ vybíráme validační chybou nebo cross-validation. Trénovací MSE by typicky preferovala λ=0 či příliš slabou regularizaci a nehodnotí generalizační kompromis.

## Poznámka Anki 1785269100105

Karty Anki: 1785269200105
GUID: ad7bcdc59180; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak se rozkládá **očekávaná kvadratická predikční chyba** a co znamená neodstranitelný šum?

### Odpověď (Back)

V pevném bodě x a při nezávislosti trénovacích dat a nového testovacího pozorování:

**E[(Y−Ŷ)²]=σ²+bias(Ŷ)²+Var(Ŷ)**.

**σ²** je variabilita nového Y kolem E[Y|x]. Je neodstranitelná: ani znalost skutečné podmíněné střední hodnoty nepředpoví konkrétní náhodnou realizaci ε.

## Poznámka Anki 1785269100106

Karty Anki: 1785269200106
GUID: 049c69e67cc5; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Co v bias–variance rozkladu znamenají **bias a variance** a jak se liší chyba odhadu střední hodnoty od chyby nového Y?

### Odpověď (Back)

- **bias(Ŷ)=E[Ŷ]−E[Y|x]**: systematická odchylka průměrné predikce procedury od skutečného podmíněného průměru.
- **Var(Ŷ)**: citlivost predikce na konkrétní náhodnou trénovací množinu.

Pro odhad podmíněné střední hodnoty platí **E[(Ŷ−E[Y|x])²]=bias²+variance**. Celková chyba predikce nového Y navíc obsahuje σ².

## Poznámka Anki 1785269100107

Karty Anki: 1785269200107
GUID: bb1d29b8e7c9; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Co je **bias–variance trade-off** a jak jej Ridge využívá při kolinearitě?

### Odpověď (Back)

Snižování systematického biasu často zvyšuje variance a naopak. S rostoucím λ Ridge typicky **zvyšuje bias** stahováním od OLS, ale **snižuje variance** omezením citlivosti na trénovací výběr. Malý nárůst bias² může být více než vyvážen poklesem variance, takže Ridge překoná nestranný OLS.

Optimální λ minimalizuje bias²+variance, ne samotný bias ani samotnou variance: nulový bias může být nestabilní a minimální variance silně vychýlená. Kolinearita právě vytváří vysoko-rozptylové směry OLS, které Ridge penalizuje.

## Poznámka Anki 1785269100108

Karty Anki: 1785269200108
GUID: a1929dc27d40; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Co je **model bázových funkcí** a proč může být nelineární ve vstupu, ale stále lineární regresí?

### Odpověď (Back)

Bázová funkce φ<sub>j</sub>:R<sup>p</sup>→R je předem zvolená transformace vstupu použitá jako nový příznak. Definujeme:

**φ(x)=(1,φ<sub>1</sub>(x),…,φ<sub>M</sub>(x))ᵀ**,
**Y=φ(x)ᵀw+ε=Σ<sub>j=0</sub><sup>M</sup>w<sub>j</sub>φ<sub>j</sub>(x)+ε**.

φ<sub>j</sub> mohou být nelineární v x, ale neznámé koeficienty w vstupují lineárně, proto jde stále o lineární regresi v parametrech.

## Poznámka Anki 1785269100109

Karty Anki: 1785269200109
GUID: 27988285bc1e; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak se model bázových funkcí zapíše pro trénovací data a jak vypadá jeho **regularizovaný odhad a predikce**?

### Odpověď (Back)

Matice Φ má v i-tém řádku φ(x<sub>i</sub>)ᵀ a model je **Y=Φw+ε**. Minimalizujeme:

**‖Y−Φw‖²+λwᵀI′w**,

odkud **ŵ<sub>λ</sub>=(ΦᵀΦ+λI′)<sup>−1</sup>ΦᵀY**. Pro nový vstup nejprve vypočteme φ(x) a poté **Ŷ=φ(x)ᵀŵ<sub>λ</sub>**.

## Poznámka Anki 1785269100110

Karty Anki: 1785269200110
GUID: 7a812f833dba; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jaké bázové funkce používá **polynomiální regrese** a co umožňují kvadratické a interakční členy?

### Odpověď (Back)

Polynomiální regrese používá mocniny příznaků a jejich součiny.

- **x<sub>j</sub>²:** zachytí kvadratickou závislost.
- **x<sub>k</sub>x<sub>l</sub>:** interakce — účinek jednoho příznaku závisí na druhém.

Model s x² je nelineární v původním x, ale lineární v koeficientech. Použít lze i log(x<sub>j</sub>), √x<sub>j</sub>, sin(x<sub>j</sub>) a jiné věcně vhodné transformace.

## Poznámka Anki 1785269100111

Karty Anki: 1785269200111
GUID: 4d26f407c174; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Co je **indikátorová bázová funkce** a jaký model vytvářejí indikátory oblastí či intervalů?

### Odpověď (Back)

**1<sub>A</sub>(x)=1**, pokud x∈A, jinak 0. Indikátory rozdělí vstupní prostor na oblasti a dovolí v nich různé konstantní nebo lineární komponenty. Indikátory disjunktních intervalů vytvářejí po částech konstantní či obecně po částech definovaný regresní model.

## Poznámka Anki 1785269100112

Karty Anki: 1785269200112
GUID: 184f1632c68b; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Co je **radiální bázová funkce** a jak modeluje lokální strukturu?

### Odpověď (Back)

Má tvar **φ(x)=h(‖x−c‖)** a závisí pouze na vzdálenosti od centra c. Centra mohou být v trénovacích bodech nebo reprezentativních centrech získaných z dat. Každá funkce reaguje nejsilněji v okolí svého centra a její vliv se mění se vzdáleností.

## Poznámka Anki 1785269100113

Karty Anki: 1785269200113
GUID: e9c5d0459472; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Proč používat mnoho bázových funkcí, jaká to má rizika a co je u nich **parametr vs. hyperparametr**?

### Odpověď (Back)

Mnoho bází rozšíří tvary závislostí, které lze aproximovat, ale přináší vysokou dimenzi, kolinearitu, nestabilní koeficienty a přeučení. Regularizace dovolí flexibilní reprezentaci s menší nestabilitou.

- **Hyperparametry reprezentace:** tvary a množina φ<sub>j</sub>, např. stupeň polynomu.
- **Parametry:** koeficienty w<sub>j</sub> odhadované z dat.

Složitost bází i sílu regularizace ladíme validací nebo cross-validation.

## Poznámka Anki 1785269100114

Karty Anki: 1785269200114
GUID: 23ebe4b3dc25; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Co je **statistika**, proč je OLS odhad náhodný a za jakého předpokladu je nestranný?

### Odpověď (Back)

Statistika je funkce náhodného výběru, takže se mění mezi realizacemi dat. OLS ŵ je náhodný vektor, protože závisí na náhodných Y a případně X.

Při správně specifikovaném lineárním modelu a **E[ε|X]=0** je OLS podmíněně nestranný: **E[ŵ<sub>OLS</sub>|X]=w**. Průměr odhadů přes opakované výběry se rovná skutečným koeficientům.

## Poznámka Anki 1785269100115

Karty Anki: 1785269200115
GUID: 7cb50a688931; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jak se dokáže **nestrannost OLS koeficientů**?

### Odpověď (Back)

Do vzorce dosadíme Y=Xw+ε:

**ŵ=(XᵀX)<sup>−1</sup>XᵀY
=w+(XᵀX)<sup>−1</sup>Xᵀε**.

Při E[ε|X]=0 má druhý člen podmíněnou střední hodnotu nula, a proto E[ŵ|X]=w.

## Poznámka Anki 1785269100116

Karty Anki: 1785269200116
GUID: de89abb921bb; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Co přesně odhaduje OLS predikce a co znamená její **nestrannost**?

### Odpověď (Back)

**Ŷ=xᵀŵ** odhaduje podmíněnou střední hodnotu E[Y|X=x]=xᵀw. Za standardních předpokladů:

**E[Ŷ|X]=xᵀE[ŵ|X]=xᵀw**,

takže bias odhadu střední hodnoty je nulový. Neznamená to přesnou predikci každého budoucího Y, které stále obsahuje náhodnou chybu ε.

## Poznámka Anki 1785269100117

Karty Anki: 1785269200117
GUID: eb0121b94b0a; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jaký je rozdíl mezi **nestranností a stabilitou** a proč může být vychýlený Ridge výhodnější než OLS?

### Odpověď (Back)

Nestrannost se týká průměru odhadu přes opakované výběry; stabilita velikosti jeho rozptylu mezi výběry. Ridge je pro λ>0 obecně vychýlený, protože koeficienty stahuje k nule, ale může mít výrazně menší rozptyl a tím nižší celkovou MSE než nestranný OLS.

## Poznámka Anki 1785269100118

Karty Anki: 1785269200118
GUID: 15449ecc7310; štítky: 05_Ridge_bias_variance_a_bazove_funkce BI-ML1 konsolidace.

### Otázka (Front)

Jaký rámec propojuje **OLS, kolinearitu, Ridge a bázové funkce**?

### Odpověď (Back)

**OLS** odhaduje lineární koeficienty ortogonální projekcí. **Kolinearita** vytváří ploché či téměř ploché směry a nestabilní koeficienty. **Ridge** je stabilizuje L2 penalizací za cenu biasu. **Bázové funkce** rozšíří lineární model na nelineární vztahy ve vstupu, přičemž zachovají linearitu v odhadovaných parametrech.

