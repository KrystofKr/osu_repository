# BI-ML1 – 06 Logisticka regrese

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::3 BI-ML1::06 Logisticka regrese
Rozsah: 18 poznámek, 18 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785269100119

Karty Anki: 1785269200119
GUID: 19e0b41c6704; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Co základní **binární logistická regrese** modeluje a proč nemůže použít lineární prediktor přímo jako pravděpodobnost?

### Odpověď (Back)

Navzdory názvu jde o klasifikační metodu pro **Y∈{0,1}**. Místo diskrétní třídy modeluje spojitou pravděpodobnost **P(Y=1|x,w)∈(0,1)**; P(Y=0)=1−P(Y=1), takže stačí jedna.

Základem je lineární prediktor **z=wᵀx=w<sub>0</sub>+⋯+w<sub>p</sub>x<sub>p</sub>**. Ten může být libovolné reálné číslo, a proto jej nelze přímo interpretovat jako pravděpodobnost.

## Poznámka Anki 1785269100120

Karty Anki: 1785269200120
GUID: 511d3b395f45; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jak je definována **sigmoida** a jaké má hlavní vlastnosti?

### Odpověď (Back)

**σ(z)=e<sup>z</sup>/(1+e<sup>z</sup>)=1/(1+e<sup>−z</sup>)**.

- Definiční obor R, obor hodnot (0,1).
- Pro konečné z nikdy není přesně 0 ani 1.
- σ(0)=1/2; je ostře rostoucí.
- lim<sub>z→−∞</sub>σ(z)=0, lim<sub>z→+∞</sub>σ(z)=1.
- **σ(−z)=1−σ(z)**; σ(z)−1/2 je lichá.

## Poznámka Anki 1785269100121

Karty Anki: 1785269200121
GUID: 4e2708cde0c0; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Co je **logit** a jak logistická regrese modeluje pravděpodobnost a logaritmus šancí?

### Odpověď (Back)

Inverzí sigmoidy je **logit(p)=ln[p/(1−p)]**. Logistická regrese předpokládá:

**ln[P(Y=1|x,w)/P(Y=0|x,w)]=wᵀx**.

Proto:

- **P(Y=1|x,w)=σ(wᵀx)=e<sup>wᵀx</sup>/(1+e<sup>wᵀx</sup>)**;
- **P(Y=0|x,w)=1−σ(wᵀx)=1/(1+e<sup>wᵀx</sup>)**.

## Poznámka Anki 1785269100122

Karty Anki: 1785269200122
GUID: 94c5ccafa8a4; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jak intercept a práh 0,5 určují **rozhodovací hranici** logistické regrese?

### Odpověď (Back)

Konstantní x<sub>0</sub>=1 zahrne intercept w<sub>0</sub>, který posouvá hranici a mění základní pravděpodobnost při nulových ostatních příznacích.

Standardně Ŷ=1 pro p̂>0,5. Protože σ je rostoucí a σ(0)=0,5, je to ekvivalentní **wᵀx>0**. Hranice je:

**wᵀx=w<sub>0</sub>+w<sub>1</sub>x<sub>1</sub>+⋯+w<sub>p</sub>x<sub>p</sub>=0**,

tedy (p−1)-rozměrná nadrovina. Sigmoida je sice nelineární, ale její monotónnost zachová lineární hranici pro práh 0,5.

## Poznámka Anki 1785269100123

Karty Anki: 1785269200123
GUID: dc83c1f13834; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jak se interpretuje koeficient w<sub>j</sub> logistické regrese v **logitu, šancích a pravděpodobnosti**?

### Odpověď (Back)

Pravděpodobnost σ(wᵀx) není lineární v příznacích; lineární je **logit**. Při zvýšení x<sub>j</sub> o 1 a fixních ostatních:

- logaritmus šancí se změní o **w<sub>j</sub>**;
- šance se násobí **e<sup>w<sub>j</sub></sup>**;
- w<sub>j</sub>>0 zvyšuje a w<sub>j</sub><0 snižuje šance i pravděpodobnost třídy 1.

Změna pravděpodobnosti není konstantní; závisí na aktuální hodnotě wᵀx.

## Poznámka Anki 1785269100124

Karty Anki: 1785269200124
GUID: cf7399b132fb; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Co je **MLE** a jak funguje na příkladu 7 hlav z 10 hodů?

### Odpověď (Back)

**MLE = Maximum Likelihood Estimation**: volí parametry, při nichž jsou pozorovaná data podle modelu nejpravděpodobnější.

Pro konkrétní posloupnost se 7 hlavami a 3 orly je **L(p)=p<sup>7</sup>(1−p)<sup>3</sup>**. Kombinační číslo není potřeba pro konkrétní pořadí; při modelování jen počtu by se objevilo, ale nezávisí na p, takže MLE nezmění. Maximum je **p̂=7/10=0,7**. Obecně je Bernoulliho MLE výběrový průměr, tedy podíl jedniček.

## Poznámka Anki 1785269100125

Karty Anki: 1785269200125
GUID: 38dbdcfff8f9; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Proč se v MLE používá **log-věrohodnost** a jak se z ní odvodí p̂=0,7 pro 7 hlav a 3 orly?

### Odpověď (Back)

Logaritmus je ostře rostoucí, takže L a ℓ=ln L mají stejné maximalizátory, a převádí součiny na součty.

**ℓ(p)=7 ln p+3 ln(1−p)**. Položíme **ℓ′(p)=7/p−3/(1−p)=0** a vyřešíme p=0,7.

## Poznámka Anki 1785269100126

Karty Anki: 1785269200126
GUID: 4778c84a5067; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jak se sestaví **věrohodnost logistické regrese** pro N binárních pozorování?

### Odpověď (Back)

Označme **p<sub>1</sub>(x,w)=σ(wᵀx)** a **p<sub>0</sub>(x,w)=1−σ(wᵀx)**. Pravděpodobnost jednoho cíle zapíšeme jednotně:

**p<sub>1</sub>(x<sub>i</sub>,w)<sup>Y<sub>i</sub></sup> p<sub>0</sub>(x<sub>i</sub>,w)<sup>1−Y<sub>i</sub></sup>**,

což vybere p<sub>1</sub> pro Y=1 a p<sub>0</sub> pro Y=0. Při podmíněné nezávislosti pozorování:

**L(w)=∏<sub>i=1</sub><sup>N</sup>p<sub>1</sub>(x<sub>i</sub>,w)<sup>Y<sub>i</sub></sup>p<sub>0</sub>(x<sub>i</sub>,w)<sup>1−Y<sub>i</sub></sup>**.

Data jsou zafixována; L je funkce kandidátních parametrů w a vyjadřuje pravděpodobnost pozorovaných cílů.

## Poznámka Anki 1785269100127

Karty Anki: 1785269200127
GUID: 04518e4810ab; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jak vypadá **log-věrohodnost logistické regrese** a jak souvisí s binární cross-entropy?

### Odpověď (Back)

Pro p<sub>i</sub>=σ(wᵀx<sub>i</sub>):

**ℓ(w)=Σ[Y<sub>i</sub>ln p<sub>i</sub>+(1−Y<sub>i</sub>)ln(1−p<sub>i</sub>)]**
**=Σ[Y<sub>i</sub>wᵀx<sub>i</sub>−ln(1+e<sup>wᵀx<sub>i</sub></sup>)]**.

Učení maximalizuje ℓ (ekvivalentně L). Minimalizace −ℓ je součet binárních cross-entropií, které vznikají přímo jako záporné log-pravděpodobnosti skutečných tříd. Správná sebejistá predikce přispívá k ℓ hodnotou blízkou 0; sebejistá chyba žene ℓ k −∞ a −ℓ k +∞.

## Poznámka Anki 1785269100128

Karty Anki: 1785269200128
GUID: 13d791dbf831; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jak vypadá **gradient log-věrohodnosti** logistické regrese a jak se interpretuje?

### Odpověď (Back)

X má v řádcích x<sub>i</sub>ᵀ (obvykle s prvními jedničkami), Y=(Y<sub>1</sub>,…,Y<sub>N</sub>)ᵀ a P(w)=(p<sub>1</sub>(x<sub>1</sub>,w),…,p<sub>1</sub>(x<sub>N</sub>,w))ᵀ.

- **∂ℓ/∂w<sub>j</sub>=Σx<sub>ij</sub>(Y<sub>i</sub>−p<sub>i</sub>)**.
- **∇ℓ(w)=Xᵀ[Y−P(w)]**.

Y<sub>i</sub>−p<sub>i</sub> je pravděpodobnostní reziduum; gradient je agreguje s vahami příznaků. Vnitřní maximum splňuje **Xᵀ[Y−P(w)]=0**.

## Poznámka Anki 1785269100129

Karty Anki: 1785269200129
GUID: 385cf4b34a36; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Proč logistická regrese nemá obecně uzavřený odhad a jak funguje **gradientní vzestup**?

### Odpověď (Back)

Rovnice Xᵀ[Y−P(w)]=0 je nelineární, protože P(w) obsahuje sigmoidy. Na rozdíl od OLS proto obvykle potřebujeme numerickou iteraci, např. gradientní vzestup nebo vícerozměrnou Newtonovu metodu.

Vzniká posloupnost w<sup>(0)</sup>,w<sup>(1)</sup>,… a gradientní vzestup aktualizuje:

**w<sup>(t+1)</sup>=w<sup>(t)</sup>+αXᵀ[Y−P(w<sup>(t)</sup>)]**.

Gradient se přičítá, protože maximalizujeme pohybem ve směru nejrychlejšího růstu; sestup by jej při minimalizaci odečítal.

## Poznámka Anki 1785269100130

Karty Anki: 1785269200130
GUID: c2f3ef7a270b; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jak learning rate a numerická konvergence ovlivňují učení logistické regrese?

### Odpověď (Back)

**Learning rate α** je hyperparametr délky kroku. Příliš velký může maximum přeskakovat, oscilovat či způsobit nekonvergenci; příliš malý vede k pomalému učení. Adaptivní α<sub>t</sub> se mezi iteracemi mění.

Výsledkem není přesné algebraické řešení, ale aproximace závislá na algoritmu, toleranci a konvergenci. Algoritmus může selhat kvůli nekonvergenci, numerickým problémům nebo úloze bez konečného maxima.

## Poznámka Anki 1785269100131

Karty Anki: 1785269200131
GUID: 7bcf75d5ba54; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jak **konkávnost log-věrohodnosti** zjednodušuje optimalizaci standardní logistické regrese?

### Odpověď (Back)

Existuje-li konečné lokální maximum, je díky konkávnosti zároveň globální. Nemohou tedy existovat různá izolovaná neglobální lokální maxima, na nichž by optimalizace uvízla.

## Poznámka Anki 1785269100132

Karty Anki: 1785269200132
GUID: dfca310acdd0; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Co je **lineární separabilita** a proč při ní nemusí existovat konečné nepenalizované MLE?

### Odpověď (Back)

Data jsou separabilní, existuje-li w s wᵀx<sub>i</sub>>0 pro všechny Y=1 a wᵀx<sub>i</sub><0 pro všechny Y=0. Násobením separujícího w rostoucí konstantou posouváme pravděpodobnosti správných tříd blíž k 1 a stále zvyšujeme věrohodnost. Sigmoida však pro konečné koeficienty nikdy nedá přesně 0/1, takže koeficienty mohou růst bez omezení a konečné maximum neexistuje.

Prakticky: obrovské koeficienty, nestabilita, varování o nekonvergenci či limit iterací. **Regularizace** penalizuje velké koeficienty a stabilizuje separabilitu i kolinearitu.

## Poznámka Anki 1785269100133

Karty Anki: 1785269200133
GUID: e6edd44cc44a; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jak odvozené příznaky mění **flexibilitu a rozhodovací hranici** logistické regrese?

### Odpověď (Back)

Přidáme mocniny, součiny či jiné bázové funkce bez změny základního algoritmu. Model zůstane lineární v transformovaných příznacích, ale v původním prostoru může mít nelineární hranici. Příznaky x<sub>1</sub>,x<sub>2</sub>,x<sub>1</sub>²,x<sub>2</sub>² mohou vytvořit kvadratickou hranici, např. elipsu či jinou kuželosečku.

Mnoho odvozených příznaků však zvyšuje riziko přeučení, kolinearity a numerické nestability.

## Poznámka Anki 1785269100134

Karty Anki: 1785269200134
GUID: 3d5ff08cb992; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jaký je hlavní **modelový předpoklad** logistické regrese a jak se liší model, jeho učení, parametry a hyperparametry?

### Odpověď (Back)

Jádrem je předpoklad, že **logit podmíněné pravděpodobnosti je lineární v zvolených příznacích**. Pokud skutečný vztah sigmoida lineárního prediktoru nevystihne, je model podspecifikovaný a ani optimální w nemusí dávat dobré pravděpodobnosti.

- **Model:** P(Y=1|x,w)=σ(wᵀx).
- **Učení:** volba w maximalizací věrohodnosti.
- **w:** parametry odhadované z dat.
- **α:** hyperparametr numerického algoritmu.

## Poznámka Anki 1785269100135

Karty Anki: 1785269200135
GUID: acfd7cd239b1; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jaký řetězec vede v logistické regresi **od vstupu k rozhodnutí** a jak se liší její predikční cíl od lineární regrese?

### Odpověď (Back)

**x → lineární prediktor wᵀx → sigmoida → pravděpodobnost → rozhodovací práh → třída.**

Lineární regrese přímo modeluje podmíněnou střední hodnotu spojitého Y; logistická regrese modeluje pravděpodobnost binární události Y=1.

## Poznámka Anki 1785269100136

Karty Anki: 1785269200136
GUID: 4196f20aba4e; štítky: 06_Logisticka_regrese BI-ML1 konsolidace.

### Otázka (Front)

Jaký řetězec popisuje **učení logistické regrese** a jak se liší od OLS?

### Odpověď (Back)

Model přiřadí trénovacím třídám pravděpodobnosti → sestaví se věrohodnost → zlogaritmuje se → maximum se hledá gradientem či jinou numerickou metodou.

**OLS** minimalizuje součet čtverců reziduí a často má uzavřený vzorec. **Logistické MLE** maximalizuje Bernoulliho věrohodnost a obecně vyžaduje numerickou optimalizaci.

