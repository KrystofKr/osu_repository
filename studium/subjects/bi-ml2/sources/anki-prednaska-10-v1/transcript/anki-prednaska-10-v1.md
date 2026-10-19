# BI-ML2 – Přednáška 10

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 17 poznámek, 17 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291613

Karty Anki: 1785306291614
GUID: 66*_H>5s?O; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Co je CNN a jaké základní vlastnosti spojité konvoluce využívá?

### Odpověď (Back)

Konvoluční neuronová síť je dopředná síť pro data s pravidelnou tenzorovou strukturou—např. 1D časové řady, 2D obrazy a vícerozměrná pole—která alespoň v jedné vrstvě používá konvoluci nebo příbuznou křížovou korelaci. U obrazů využívá lokalitu, sdílí detektor přes pozice a má méně parametrů než plně propojená vrstva.

Spojitá konvoluce je (f∗g)(t)=∫f(τ)g(t−τ)dτ a je komutativní: f∗g=g∗f. Konvoluce s hladkým jádrem g, např. rovnoměrným na [−w,w] či Gaussovským, vytvoří lokálně vážené vyhlazení; jádro určuje váhy okolních hodnot. Za vhodných podmínek (f∗g)′=f∗g′, takže derivaci vyhlazené funkce získáme konvolucí původní funkce s derivací jádra.

## Poznámka Anki 1785306291615

Karty Anki: 1785306291616
GUID: qlw4]3P2PD; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Co je translační ekvivariance konvoluce a co umí diskrétní konvoluční filtry?

### Odpověď (Back)

Konvoluce je translačně **ekvivariantní**: posun vstupu o a způsobí stejný posun výstupní mapy. Není sama invariantní; invariance by znamenala nezměněný výstup. Díky ekvivarianci se odezva detektoru přesune spolu se vzorem.

Pro oboustranné posloupnosti je (x∗w)(t)=Σ<sub>i=−∞</sub><sup>∞</sup>x(i)w(t−i). Jádro s podobnými kladnými vahami vytvoří lokální vážený průměr a potlačí krátkodobé výkyvy. Jádro s kladnou a zápornou částí aproximuje lokální diferenci, takže prudká změna či hrana vyvolá velkou odezvu.

## Poznámka Anki 1785306291617

Karty Anki: 1785306291618
GUID: YJ=A~OXv9g; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jak se v CNN liší matematická konvoluce od křížové korelace a proč rozdíl neomezuje expresivitu?

### Odpověď (Back)

Konvoluční jádro CNN je malý tenzor vah učený gradientním sestupem a aplikovaný na různé lokální oblasti. Pravá 2D konvoluce může být zapsána S(i,j)=ΣₘΣₙI(m,n)K(i−m,j−n); jádro se při posouvání obrací, což souvisí mimo jiné s komutativitou.

Knihovny pod názvem „konvoluce“ obvykle počítají křížovou korelaci bez obrácení:
(I⋆K)(i,j)=Σ<sub>m=1</sub><sup>k₁</sup>Σ<sub>n=1</sub><sup>k₂</sup>I(i+m−1,j+n−1)K(m,n).
Expresivitu to neomezuje, protože trénovatelné jádro se naučí potřebnou orientaci hodnot bez ohledu na konvenci.

## Poznámka Anki 1785306291619

Karty Anki: 1785306291620
GUID: -DhuL)[?>O; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jaké rozměry mají validní konvoluce a vícekanálové vstupy v channel-first notaci?

### Odpověď (Back)

Validní konvoluce nepřidává padding a jádro vyhodnocuje jen tam, kde celé leží uvnitř vstupu. Pro 2D vstup p₁×p₂, jádro k₁×k₂ a stride 1 má výstup (p₁−k₁+1)×(p₂−k₂+1); zmenšení vzniká ztrátou okrajových umístění.

Kanál je paralelní složka tenzoru, např. R/G/B. Jeden vstup v channel-first notaci má (c<sub>in</sub>,p₁,…,p<sub>d</sub>), barevný obraz 28×28 tedy (3,28,28), a minibatch m vstupů (m,c<sub>in</sub>,p₁,…,p<sub>d</sub>).

## Poznámka Anki 1785306291621

Karty Anki: 1785306291622
GUID: =rw&FTLF+i; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jak vícekanálová konvoluce kombinuje vstupy a kolik má parametrů?

### Odpověď (Back)

J-tý výstupní kanál má pro každý z c<sub>in</sub> vstupních kanálů vlastní jádro, korelace se sečtou a přičte se jeden bias:
O<sub>j</sub>=b<sub>j</sub>+Σ<sub>ℓ=1</sub><sup>c<sub>in</sub></sup>I<sub>ℓ</sub>⋆K<sub>j,ℓ</sub>.
Pro d-rozměrné jádro k₁×…×k<sub>d</sub> má jeden výstupní kanál c<sub>in</sub>k₁…k<sub>d</sub> vah + bias; celá vrstva c<sub>out</sub>(c<sub>in</sub>k₁…k<sub>d</sub>+1). Počet parametrů nezávisí na prostorové velikosti, protože se váhy sdílejí.

Validní výstup se stride 1 má tvar (c<sub>out</sub>,p₁−k₁+1,…,p<sub>d</sub>−k<sub>d</sub>+1).

## Poznámka Anki 1785306291623

Karty Anki: 1785306291624
GUID: |Fc(;GE&/m; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Co je omezené lokální spojení a jak s hloubkou roste receptive field CNN?

### Odpověď (Back)

Výstupní neuron CNN je propojen jen s malou lokální oblastí předchozí vrstvy. Jeho receptive field je oblast předchozí vrstvy či původního vstupu, která jej může ovlivnit; větší jádro zvětší přímé pole. Skládáním vrstev se překrývající lokální pole spojují, takže vyšší neuron vidí velkou část obrazu i při malých jádrech.

Lokalita snižuje počet parametrů, protože nevzniká váha mezi každým vstupním a výstupním prvkem. Biologickou analogií jsou neurony primární vizuální kůry reagující na lokální části zorného pole, z nichž se skládá globální obraz.

## Poznámka Anki 1785306291625

Karty Anki: 1785306291626
GUID: {ljJVJ*ARF; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Co je sdílení parametrů CNN a jak spolu s lokalitou vytváří konvoluční blok?

### Odpověď (Back)

Stejné jádro se používá na všech pozicích výstupního kanálu. Konvoluční vrstvu lze chápat jako plně propojenou vrstvu s vynucenou lokalitou a svázanými vahami. Jeden filtr proto hledá tentýž vzor všude místo zvláštního detektoru pro každou pozici; při posunu vzoru se posune i aktivace, což podporuje translační ekvivarianci.

Dva určující principy jsou omezené lokální spojení a sdílení parametrů. Po lineární konvoluci následuje nelinearita, např. ReLU; typický blok je konvoluce → aktivace → případně lokální pooling.

## Poznámka Anki 1785306291627

Karty Anki: 1785306291628
GUID: ggG}}S_9XN; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jak funguje pooling a jak ovlivňuje rozměr a odolnost vůči posunům?

### Odpověď (Back)

Pooling je pevná lokální agregace, která obvykle zmenšuje prostorové mapy. Max pooling zachová nejsilnější odezvu oblasti; average pooling její průměrnou intenzitu. Následující vrstvy tak pracují s hrubší reprezentací.

Malý posun aktivního vzoru uvnitř stejné poolingové oblasti může vytvořit stejný či podobný agregát, takže pooling zlepšuje lokální odolnost. Nezajišťuje však dokonalou invarianci vůči libovolnému posunu; výsledek závisí na velikosti okna a stride.

## Poznámka Anki 1785306291629

Karty Anki: 1785306291630
GUID: h%h@JHP8Sx; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jak padding, stride a dilatace řídí rozměry a receptive field konvoluce?

### Odpověď (Back)

**Padding** rozšíří okraje, nejčastěji nulami, alternativně replikací či zrcadlením. Umožní zpracovat okraje a řídit rozměr; same padding při vhodném stride zachová prostorovou velikost, takže lze skládat více vrstev bez rychlého zmenšování.

**Stride** je posun jádra mezi vyhodnoceními; základ je 1. Větší stride podvzorkuje výstup a lze jej chápat jako konvoluci následovanou vynecháním hodnot. Pro validní konvoluci je rozměr r
⌊(p<sub>r</sub>−k<sub>r</sub>)/s<sub>r</sub>⌋+1,
celkově (c<sub>out</sub>,⌊(p₁−k₁)/s₁⌋+1,…). Pooling používá pevnou agregaci, strided convolution trénovatelné jádro a současně podvzorkuje.

**Dilatovaná konvoluce** vkládá mezi prvky jádra rozestupy, a zvětšuje tak receptive field bez úměrného růstu parametrů.

## Poznámka Anki 1785306291631

Karty Anki: 1785306291632
GUID: }ncxg2L4pG; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jak vypadá klasifikační CNN a kdy lze 1D CNN použít na sekvence?

### Odpověď (Back)

Klasifikační CNN obvykle skládá několik konvolučních bloků do hierarchických příznaků a zakončí je malým počtem plně propojených vrstev. Lokalita a sdílení drží počet parametrů nízko i ve velmi hluboké síti; GPU efektivně paralelizují její pravidelné tenzorové operace.

CNN není jen pro obrazy. Časovou řadu pevné délky lze zapsat přibližně jako (p,τ), kde p složek tvoří kanály a čas jednu osu. U různě dlouhých posloupností však základní dávkový tenzor vyžaduje padding, ořezání nebo jinou architekturu.

## Poznámka Anki 1785306291633

Karty Anki: 1785306291634
GUID: .oTq@KG(fL; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jak základní RNN aktualizuje skrytý stav, výstup a sdílené parametry?

### Odpověď (Back)

RNN pro sekvenční data kombinuje aktuální x<sup>(t)</sup> s předchozím stavem h<sup>(t−1)</sup>; obecně h<sup>(t)</sup>=f(h<sup>(t−1)</sup>,x<sup>(t)</sup>;w). Stav je naučený souhrn dosavadní posloupnosti. Základní buňka:
h<sup>(t)</sup>=g₁(Uᵀx<sup>(t)</sup>+Wᵀh<sup>(t−1)</sup>+w₀),
o<sup>(t)</sup>=g₂(Vᵀh<sup>(t)</sup>+v₀).
U vede vstup→stav, W stav→nový stav, V stav→výstup. Pro vstup p, stav n₁ a výstup n₂: U∈ℝ<sup>p×n₁</sup>, W∈ℝ<sup>n₁×n₁</sup>, V∈ℝ<sup>n₁×n₂</sup>.

Stejné U,W,V se sdílejí ve všech časech. Přechod lze proto opakovat libovolně dlouho bez nových parametrů a zpracovat proměnnou délku.

## Poznámka Anki 1785306291635

Karty Anki: 1785306291636
GUID: ;Fb}{vL>cP; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jaké výstupy může RNN tvořit a proč při BPTT vznikají mizející a explodující gradienty?

### Odpověď (Back)

Sequence-to-sequence vytváří o<sup>(1)</sup>,…,o<sup>(τ)</sup>; sequence-to-one používá např. poslední o<sup>(τ)</sup> nebo reprezentaci z posledního stavu. Unfolding znázorní opakovanou buňku jako časový řetězec zdánlivých kopií; všechny sdílejí parametry a liší se vstupy a stavy. Délka sekvence se tak podobá hloubce dopředné sítě.

Backpropagation through time je backpropagation přes tento rozbalený graf se sečtením příspěvků ke sdíleným parametrům. Přes mnoho kroků se opakovaně násobí rekurentní matice a lokální derivace. Faktory s normou pod 1 gradient tlumí, velké jej exponenciálně zvětšují; RNN proto sdílí problémy velmi hlubokých sítí.

## Poznámka Anki 1785306291637

Karty Anki: 1785306291638
GUID: 9>:{;|Sr0N; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Proč jednoduchá RNN obtížně zachycuje dlouhodobé závislosti a jak se liší LSTM od transformeru?

### Odpověď (Back)

Dlouhodobá závislost znamená, že výstup závisí na časově vzdálené informaci. V jednoduché RNN musí informace i gradient projít mnoha přechody, takže mohou zmizet nebo explodovat.

LSTM (long short-term memory) je složitější rekurentní jednotka navržená pro lépe řízené uchování informace a toku gradientu přes dlouhé úseky; problém základní RNN zmírňuje, ne zcela ruší.

Transformer místo rekurentního předávání jediného stavu používá hlavně self-attention k přímému modelování vztahů mezi pozicemi. Je zvlášť úspěšný v přirozeném jazyce a dalších sekvenčních úlohách.

## Poznámka Anki 1785306291639

Karty Anki: 1785306291640
GUID: w=bta17)gm; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Co je autoenkodér a jak souvisí latentní prostor s generativním modelováním?

### Odpověď (Back)

Autoenkodér se učí rekonstruovat vstup přes mezilehlý kód. Úzký latentní kód poskytuje nelineární redukci dimenzionality; denoising autoenkodér dostane poškozený vstup a rekonstruuje čistou podobu.

Latentní prostor generativního modelu je jednodušší prostor skrytých náhodných proměnných. Síť se učí transformovat jednoduché vícerozměrné rozdělení, např. normální, na složité rozdělení datových vzorků.

## Poznámka Anki 1785306291641

Karty Anki: 1785306291642
GUID: Mt)b(7sc0q; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jak se liší augmentace dat, adversariální příklady a adversariální trénování?

### Odpověď (Back)

**Augmentace** vytváří nové příklady transformacemi, u obrazů např. otočením, posunem či změnou měřítka. Transformace musí zachovat štítek nebo jej správně změnit. Model vidí více variant a méně se váže na náhodné detaily; volbou transformací vkládáme apriorní předpoklad invariance či ekvivariance.

**Adversariální příklad** je malá, často téměř neviditelná, ale cíleně optimalizovaná perturbace využívající citlivost konkrétního modelu k vyvolání chybné nebo zvolené predikce—na rozdíl od náhodného šumu. **Adversariální trénování** zahrnuje takové nejnepříznivější vstupy do učení a hledá kompromis mezi běžnou přesností a robustností.

## Poznámka Anki 1785306291643

Karty Anki: 1785306291644
GUID: C4OdcBq1NB; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jak funguje transfer learning a jak se liší od augmentace a adversariálního trénování?

### Odpověď (Back)

Transfer learning přenese parametry či reprezentace modelu předtrénovaného na velké související úloze do cílové úlohy. Síť poskytne výchozí bod s obecnými příznaky, což pomáhá při nedostatku štítků. Fine-tuning dále trénuje část nebo celou síť; alternativně se většina vrstev zmrazí jako extraktor a učí se jen nový výstup či několik posledních vrstev.

Augmentace rozšiřuje cílový dataset transformacemi jeho vzorků, transfer learning přenáší znalost z jiného trénování. Běžná augmentace používá realistické předvolené transformace, adversariální trénování cíleně hledá perturbace maximalizující chybu.

## Poznámka Anki 1785306291645

Karty Anki: 1785306291646
GUID: =D7NN`mIWF; štítky: BI-ML2 iterace_10 Konsolidovano Prednaska_10.

### Otázka (Front)

Jaké strukturální předpoklady používají CNN, RNN a transformer a jak vypadá celkový tok zpracování CNN?

### Odpověď (Back)

CNN spojuje lokalitu, sdílení filtru přes prostor a pooling: lokální filtry vytvoří mapy, nelinearity jejich odezvy kombinují, pooling/stride sníží rozlišení a hlubší vrstvy skládají lokální vzory do globálních struktur. RNN sdílí přechod přes čas a minulost shrnuje skrytým stavem; transformer modeluje vztahy attention mechanismem.

CNN je praktická pro pevnou délku a lokální vzory díky paralelnímu zpracování; RNN přirozeně postupuje proměnlivě dlouhou sekvencí. CNN sdílí váhy přes pozice, RNN přes čas. Přednáška dále zlepšuje praktické použití sítí augmentací, adversariálním trénováním a transfer learningem.

