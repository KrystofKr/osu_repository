# BI-ML2 – Přednáška 08

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 17 poznámek, 17 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291545

Karty Anki: 1785306291546
GUID: +[vIa^&:Ss; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Co je dopředná neuronová síť a jak se matematicky popisuje její vrstvená architektura?

### Odpověď (Back)

Dopředná síť šíří informaci bez zpětných cyklů od vstupu přes skryté vrstvy k výstupu. Vícevrstvý perceptron (MLP) je obvykle taková síť z plně propojených vrstev: každý neuron přijímá výstupy všech neuronů předchozí vrstvy. Skryté vrstvy leží mezi vstupem a výstupem; hloubka je počet postupně skládaných výpočetních vrstev (konvence může počítat výstupní vrstvu různě) a šířka vrstvy je počet jejích neuronů.

Vrstva s n<sub>i−1</sub> vstupy a n<sub>i</sub> neurony je f<sup>(i)</sup>:ℝ<sup>n<sub>i−1</sub></sup>→ℝ<sup>n<sub>i</sub></sup>. Jeden neuron počítá z=wᵀx+w₀ a g(z); celá vrstva f<sup>(i)</sup>(x)=(f₁<sup>(i)</sup>(x),…,f<sub>nᵢ</sub><sup>(i)</sup>(x))ᵀ, maticově z=Wᵀx+w₀, h=g(z), kde W∈ℝ<sup>n<sub>i−1</sub>×n<sub>i</sub></sup>, w₀∈ℝ<sup>n<sub>i</sub></sup> a j-tý sloupec W obsahuje váhy do j-tého neuronu. Celá l-vrstvá síť je f=f<sup>(l)</sup>∘…∘f<sup>(1)</sup>; vyhodnocuje se od f<sup>(1)</sup> po f<sup>(l)</sup>.

## Poznámka Anki 1785306291547

Karty Anki: 1785306291548
GUID: 3y5UKd8r0N; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jak skryté vrstvy provádějí representation learning a proč potřebují nelineární aktivace?

### Odpověď (Back)

Aktivace skryté vrstvy je naučená reprezentace vstupu a sada příznaků pro další vrstvy; poslední výstupní vrstva je afinně kombinuje a vhodnou aktivací vytvoří predikci. Na rozdíl od předem zvolených bázových funkcí se tyto příznaky učí současně s predikčním pravidlem. Dataset poskytuje jen cílový výstup celé sítě, nikoli správné hodnoty skrytých neuronů, takže mezilehlé reprezentace vznikají nepřímo minimalizací výsledné ztráty. To je representation learning.

Více vrstev skládá afinní transformace a nelinearity do hierarchie stále složitějších příznaků. Bez nelineárních aktivací by se síť zhroutila na jedinou afinní vrstvu, protože složení lineárních či afinních zobrazení je opět lineární či afinní.

## Poznámka Anki 1785306291549

Karty Anki: 1785306291550
GUID: )U;M`o5i{r; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Co říká univerzální aproximace a jaké praktické limity mají expresivní hluboké sítě?

### Odpověď (Back)

V základní podobě věta říká, že síť s jednou dostatečně širokou skrytou vrstvou a vhodnou nelineární aktivací umí na omezené oblasti s libovolnou přesností aproximovat každou spojitou funkci. Neříká však potřebný počet neuronů, jak parametry efektivně nalézt ani zda model bude generalizovat. Jednovrstvá síť může být extrémně široká a optimalizace ji z konečných dat nemusí najít; hlubší síť může jednodušší příznaky opakovaně používat a některé funkce reprezentovat mnohem úsporněji.

Velká kapacita současně zvyšuje riziko přeučení bez dostatku dat či regularizace. Trénování je obecně nekonvexní, protože parametry různých vrstev se vzájemně násobí a procházejí nelinearitami; výsledek proto závisí na inicializaci a trajektorii a globální minimum není zaručeno.

Perceptronový update se na více vrstev se skokovými aktivacemi nerozšíří: skok nemá použitelnou derivaci a není jasné, jak rozdělit výstupní chybu mezi skryté neurony. Řešením jsou spojité, téměř všude diferencovatelné aktivace a zpětné šíření derivací.

## Poznámka Anki 1785306291551

Karty Anki: 1785306291552
GUID: _&ab(lBFbb; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jak výstupní vrstva používá poslední skrytou reprezentaci a jak vypadá výstup pro regresi?

### Odpověď (Back)

Poslední skrytá reprezentace je h=f<sup>(l−1)</sup>∘…∘f<sup>(1)</sup>(x). Jeden výstupní neuron má preaktivaci z=wᵀh+w₀, více výstupů z=Wᵀh+w₀. Výstupní aktivace se volí podle požadovaného oboru a interpretace predikce.

Pro neomezenou regresi se používá identita g(z)=z, takže při jednom výstupu Ŷ=wᵀh+w₀. Pokud musí být výstup například kladný nebo omezený na interval, lineární výstup není vhodný a použije se odpovídající transformace.

## Poznámka Anki 1785306291553

Karty Anki: 1785306291554
GUID: e$[*wM~f8D; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jak funguje sigmoidální výstup pro binární klasifikaci?

### Odpověď (Back)

Používá se logistická sigmoida σ(z)=1/(1+e<sup>−z</sup>) s oborem (0,1); její výstup se interpretuje jako odhad P(Y=1|X=x). Při běžném prahu 0,5 se predikuje třída 1, když σ(z)>0,5, jinak 0. Protože σ je rostoucí a σ(0)=0,5, rozhodovací hranice odpovídá logitu z=0.

## Poznámka Anki 1785306291555

Karty Anki: 1785306291556
GUID: iX<8DKtx5g; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jak softmax převádí logity na vícetřídní predikci a jak se počítá stabilně?

### Odpověď (Back)

Pro c vzájemně se vylučujících tříd síť vytvoří nenormalizované reálné logity z₁,…,z<sub>c</sub> a použije
softmax<sub>i</sub>(z)=e<sup>zᵢ</sup>/Σ<sub>j=1</sub><sup>c</sup>e<sup>zⱼ</sup>.
Každá složka leží v (0,1), součet je 1 a i-tá složka se interpretuje jako P(Y=i|X=x). Třídní predikce je arg max<sub>i</sub> softmax<sub>i</sub>(z), což je stejné jako arg max logitů: exponenciála je rostoucí a jmenovatel společný. Softmax je hladká diferencovatelná obdoba one-hot arg maxu.

Přičtení stejné konstanty ke všem logitům výsledek nezmění, protože společný faktor se vykrátí. Proto se před exponenciálou odečítá max<sub>j</sub>z<sub>j</sub>; tím se zabrání přetečení bez změny pravděpodobností.

## Poznámka Anki 1785306291557

Karty Anki: 1785306291558
GUID: x*/4^|sZHx; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Co jsou preaktivace a aktivace skryté vrstvy a jaké vlastnosti mají ReLU a Leaky ReLU?

### Odpověď (Back)

Aktivační funkce převádí preaktivaci na výstup neuronu a určuje jeho nelinearitu i rozsah. Preaktivace z=Wᵀx+w₀ je afinní kombinace; aktivace h=g(z) se obvykle počítá stejnou funkcí po složkách, h<sub>j</sub>=g(z<sub>j</sub>).

**ReLU:** g(z)=max(0,z), derivace je 0 pro z<0 a 1 pro z>0. Nediferencovatelnost v jediném bodě z=0 prakticky nevadí; implementace zvolí subderivaci, typicky 0. ReLU je jednoduchá, v kladné oblasti nesaturuje a obvykle šíří gradient lépe než sigmoid či tanh. Neuron však může kvůli nevhodné inicializaci nebo škálování zůstat převážně v z<0, kde má nulový výstup i gradient: jde o umírající ReLU.

**Leaky ReLU:** g(z)=z pro z≥0 a 0,01z pro z<0. Pro záporné vstupy zachovává malou zápornou hodnotu a nenulový gradient, čímž umírání neuronů zmírňuje.

## Poznámka Anki 1785306291559

Karty Anki: 1785306291560
GUID: @O@@pc#70H; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jak fungují SELU a tanh a jaké mají výhody a omezení?

### Odpověď (Back)

**SELU:** g(z)=λz pro z≥0 a λα(e<sup>z</sup>−1) pro z<0, kde λ≈1,0507 a α≈1,6733. Za vhodných podmínek pomáhá udržovat přibližně stabilní střední hodnotu a rozptyl aktivací mezi vrstvami. Samonormalizaci však nelze automaticky čekat při nevhodné inicializaci, architektuře, normalizaci či operacích porušujících její předpoklady.

**tanh:** tanh(z)=(e<sup>z</sup>−e<sup>−z</sup>)/(e<sup>z</sup>+e<sup>−z</sup>), obor (−1,1), derivace 1−tanh²(z). Přibližné centrování kolem nuly předává následující vrstvě kladné i záporné aktivace. Pro velké |z| však saturuje u −1 nebo 1, derivace se blíží nule a může vznikat mizející gradient.

## Poznámka Anki 1785306291561

Karty Anki: 1785306291562
GUID: 1kL/oFKFSz; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jaký je rozdíl mezi ztrátovou a účelovou funkcí při trénování sítě?

### Odpověď (Back)

Ztrátová funkce L hodnotí chybu jednoho pozorování porovnáním skutečné hodnoty Y s predikcí. Účelová funkce J závisí na všech parametrech a agreguje ztráty používané k optimalizaci, případně přidává regularizaci. Bez regularizace typicky
J(w)=(1/N)Σ<sub>i=1</sub><sup>N</sup>L(Y<sub>i</sub>,f(x<sub>i</sub>;w)).

## Poznámka Anki 1785306291563

Karty Anki: 1785306291564
GUID: B`{Ou{$#Ws; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jak se pro regresi porovnávají MSE a MAE?

### Odpověď (Back)

**Kvadratická ztráta:** L(Y,Ŷ)=(Y−Ŷ)² a MSE=(1/N)Σᵢ(Yᵢ−f(xᵢ;w))². Druhá mocnina silně penalizuje velké a odlehlé chyby.

**Absolutní ztráta:** L(Y,Ŷ)=|Y−Ŷ| a MAE=(1/N)Σᵢ|Yᵢ−f(xᵢ;w)|. Roste lineárně, proto je vůči odlehlým chybám robustnější. V nulové chybě není diferencovatelná, ale lze použít subgradient.

## Poznámka Anki 1785306291565

Karty Anki: 1785306291566
GUID: Dth)pc3F%I; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jak funguje binární křížová entropie a jak souvisí s maximální věrohodností?

### Odpověď (Back)

Pro p̂=P(Y=1|X=x) je
L(Y,p̂)=−Y log p̂−(1−Y)log(1−p̂).
Pro Y=1 se zjednoduší na −log p̂, pro Y=0 na −log(1−p̂). Pokud model přiřadí skutečné třídě pravděpodobnost blížící se nule, sebejistá chybná predikce má ztrátu rostoucí bez omezení.

Účelová funkce je průměr:
J(w)=−(1/N)Σᵢ[Yᵢlog f(xᵢ;w)+(1−Yᵢ)log(1−f(xᵢ;w))].
Jde o zápornou logaritmickou Bernoulliho věrohodnost, takže minimalizace křížové entropie odpovídá maximalizaci podmíněné věrohodnosti tříd.

## Poznámka Anki 1785306291567

Karty Anki: 1785306291568
GUID: 4L9]43+U*l; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jak funguje kategorická křížová entropie a které dvojice výstupu a ztráty jsou standardní?

### Odpověď (Back)

Pro softmaxovou klasifikaci do c tříd je
L(Y,p̂)=−Σ<sub>j=1</sub><sup>c</sup>1<sub>Y=j</sub>log p̂<sub>j</sub>=−log p̂<sub>Y</sub>.
Přispívá jen pravděpodobnost skutečné třídy, protože one-hot indikátor je nenulový pouze u ní. Účelová funkce je J(w)=−(1/N)Σᵢlog f<sub>Yᵢ</sub>(xᵢ;w). Jde o zápornou log-věrohodnost kategorického modelu; minimalizace tedy maximalizuje pravděpodobnost pozorovaných tříd.

Výstup musí být kompatibilní se ztrátou: identita + MSE/MAE pro regresi, sigmoida + binární křížová entropie a softmax + kategorická křížová entropie.

## Poznámka Anki 1785306291569

Karty Anki: 1785306291570
GUID: k7lQ`(g%@M; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jak gradientní sestup a řetězové pravidlo umožňují trénovat složenou neuronovou síť?

### Odpověď (Back)

Gradient ∇<sub>w</sub>J je vektor všech parciálních derivací a ukazuje směr nejrychlejšího růstu; gradientní sestup aktualizuje proti němu: w←w−η∇<sub>w</sub>J(w). Protože ztráta je složením mnoha vrstev, derivace podle raných parametrů musí projít všemi následujícími operacemi.

Pro skalární funkce d[f(g(x))]/dx=f′(g(x))g′(x). Pro f:ℝⁿ→ℝ a g:ℝᵐ→ℝⁿ platí
∂(f∘g)/∂x<sub>j</sub>=Σ<sub>i=1</sub><sup>n</sup>(∂f/∂g<sub>i</sub>)(g(x))·∂g<sub>i</sub>/∂x<sub>j</sub>.
Součet agreguje všechny cesty, jimiž změna x<sub>j</sub> ovlivní složky mezivrstvy a přes ně výslednou ztrátu.

## Poznámka Anki 1785306291571

Karty Anki: 1785306291572
GUID: ;rhev]`<3f; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Co přesně dělají dopředný chod, backpropagation a gradientní sestup?

### Odpověď (Back)

Dopředný chod počítá od vstupu preaktivace, aktivace, predikci a ztrátu; ukládá vstupy vrstev a mezivýsledky potřebné pro lokální derivace. Zpětný chod jde od ztráty přes výstupní a skryté vrstvy ke všem parametrům. Backpropagation je efektivní aplikace řetězového pravidla, která znovu používá mezivýsledky a **vypočítá gradient**; gradientní sestup jej teprve **použije k aktualizaci**.

Pro průměrnou ztrátu ∂J/∂w<sub>j</sub>=(1/N)Σᵢ∂Lᵢ/∂w<sub>j</sub> a přes více výstupů ∂L/∂w<sub>j</sub>=Σ<sub>ℓ</sub>(∂L/∂f<sub>ℓ</sub>)(∂f<sub>ℓ</sub>/∂w<sub>j</sub>). Podél jedné cesty se lokální derivace násobí; příspěvky více cest se sčítají.

Upstream gradient je derivace konečné ztráty podle výstupu aktuálního uzlu. Gradient podle jeho vstupu získáme vynásobením upstream gradientu lokální derivací výstupu uzlu podle tohoto vstupu.

## Poznámka Anki 1785306291573

Karty Anki: 1785306291574
GUID: lL$:eK],`b; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Co je výpočetní graf a jak se přes něj odvodí gradienty jednoduchého neuronu?

### Odpověď (Back)

Výpočetní graf je orientovaný rozklad výpočtu na vstupy, parametry, mezilehlé hodnoty, predikci a ztrátu; hrany/operace vyjadřují závislosti a elementární transformace. Umožňuje systematickou automatickou diferenciaci složených funkcí.

Pro neuron s jedním vstupem: u=w₁x, z=u+w₀, f=g(z). Lokální derivace jsou ∂u/∂w₁=x, ∂u/∂x=w₁, ∂z/∂u=1, ∂z/∂w₀=1 a ∂f/∂z=g′(z). Z upstream ∂J/∂f tedy:
∂J/∂z=(∂J/∂f)g′(z),
∂J/∂w₀=∂J/∂z,
∂J/∂w₁=(∂J/∂z)x,
∂J/∂x=(∂J/∂z)w₁.

## Poznámka Anki 1785306291575

Karty Anki: 1785306291576
GUID: Uj@FwZaOir; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Jak vypadá backpropagation v regresní síti se dvěma skrytými neurony?

### Odpověď (Back)

Model s lineárním výstupem je
f(x;w)=w₁<sup>(2)</sup>g(xᵀw₁<sup>(1)</sup>+w<sub>0,1</sub><sup>(1)</sup>)+w₂<sup>(2)</sup>g(xᵀw₂<sup>(1)</sup>+w<sub>0,2</sub><sup>(1)</sup>)+w₀<sup>(2)</sup>.
Skryté výstupy jsou dvě naučené nelineární bázové funkce, které výstupní neuron lineárně kombinuje.

Pro MSE:
∂J/∂w₁<sup>(2)</sup>=(1/N)Σᵢ2(f(xᵢ;w)−Yᵢ)g(xᵢᵀw₁<sup>(1)</sup>+w<sub>0,1</sub><sup>(1)</sup>),
∂J/∂w<sub>1,1</sub><sup>(1)</sup>=(1/N)Σᵢ2(f(xᵢ;w)−Yᵢ)w₁<sup>(2)</sup>g′(xᵢᵀw₁<sup>(1)</sup>+w<sub>0,1</sub><sup>(1)</sup>)x<sub>i,1</sub>.

Skrytý gradient tedy násobí výstupní chybu, váhu navazujícího spojení, derivaci aktivace a vstup daného spojení. Následující váha určuje sílu vlivu skrytého neuronu, g′ převádí změnu preaktivace na změnu aktivace a x<sub>j</sub> plyne z ∂z/∂w<sub>j</sub>=x<sub>j</sub>. Je-li g′(z)=0, gradient přes neuron zanikne a jeho vstupní váhy se daným příkladem nezmění.

## Poznámka Anki 1785306291577

Karty Anki: 1785306291578
GUID: :x$g1Mktow; štítky: BI-ML2 iterace_08 Konsolidovano Prednaska_08.

### Otázka (Front)

Co jsou mizející a explodující gradienty, proč je backpropagation efektivní a jak vypadá jeden trénovací krok?

### Odpověď (Back)

V hluboké síti se lokální derivace a váhy podél cest násobí. Mnoho malých faktorů může zmenšit gradient raných vrstev téměř k nule (mizející gradient); velké faktory jej mohou zvětšit do nestabilních hodnot (explodující gradient). Derivace aktivační funkce proto přímo rozhoduje, zda se gradient zachová, zmizí či exploduje.

Backpropagation sdílí mezivýsledky a každou lokální derivaci zpracuje jen omezeněkrát; zpětný chod má řádově cenu několika dopředných vyhodnocení, nikoli násobek počtu parametrů. Jde o reverse-mode automatickou diferenciaci: pro jediný skalární výstup J efektivně získá derivace podle milionů parametrů jedním zpětným průchodem.

Jeden základní krok: (1) dopředně spočítat predikce, (2) spočítat ztrátu, (3) backpropagation získat gradienty, (4) optimalizátorem aktualizovat parametry. Skryté vrstvy tvoří naučené příznaky, nelineární aktivace dávají expresivitu a backpropagation určuje, jak všechny transformace upravit podle výstupní chyby.

