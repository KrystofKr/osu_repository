# BI-ML2 – Přednáška 05

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291471

Karty Anki: 1785306291472
GUID: F?IaAJ4f7P; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Jak funguje Bayesova MAP klasifikace a které veličiny v ní vystupují?

### Odpověď (Back)

Pro diskrétní Y se odhadnou posteriorní pravděpodobnosti a použije se pravidlo Ŷ(x)=arg max<sub>y∈𝒴</sub>P(Y=y|X=x). MAP znamená maximum a posteriori.

Bayesova věta:
P(Y=y|X=x)=P(X=x|Y=y)P(Y=y)/P(X=x).
• P(X=x|Y=y) je třídně podmíněná věrohodnost vstupu.
• P(Y=y) je prior třídy před pozorováním x.
• P(X=x) je evidence normalizující posteriory, přičemž P(X=x)=Σ<sub>y</sub>P(X=x|Y=y)P(Y=y).

Pro pevné x je evidence stejná pro všechny třídy, proto při MAP stačí porovnat neznormalizovaná skóre P(X=x|Y=y)P(Y=y), tj. posterior je k nim jako funkce y proporcionální. Prior lze odhadnout relativní četností π̂<sub>y</sub>=N<sub>y</sub>/N.

## Poznámka Anki 1785306291473

Karty Anki: 1785306291474
GUID: aXww/6x2gx; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Jaký předpoklad používá naivní Bayes a jak zjednoduší MAP pravidlo?

### Odpověď (Back)

Naivní Bayes předpokládá, že X₁,…,X<sub>p</sub> jsou navzájem nezávislé podmíněně na třídě Y=y. Proto pro diskrétní příznaky
P(X=x|Y=y)=∏ᵢP(Xᵢ=xᵢ|Y=y)
a Ŷ=arg max<sub>y</sub>P(Y=y)∏ᵢP(Xᵢ=xᵢ|Y=y).

„Naivní“ je tento předpoklad proto, že v reálných datech bývá porušen. Jde o nezávislost **uvnitř každé třídy**, nikoli nutně v celé populaci: příznaky mohou být marginálně závislé přes společnou vazbu na Y. Formálně znalost ostatních příznaků při známém Y nemění rozdělení Xᵢ:
P(Xᵢ=xᵢ|Y=y,X<sub>−i</sub>=x<sub>−i</sub>)=P(Xᵢ=xᵢ|Y=y).

## Poznámka Anki 1785306291475

Karty Anki: 1785306291476
GUID: VK!*Mn2#La; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Proč může naivní Bayes dobře klasifikovat i při porušené nezávislosti a jaký kompromis přináší?

### Odpověď (Back)

Porušená nezávislost zkreslí součin marginálních pravděpodobností, může vícenásobně započítat korelovanou informaci a dát špatně kalibrované posteriory. Pro správnou MAP klasifikaci však stačí správné pořadí třídních skóre: skutečná třída musí mít vyšší skóre než konkurenti, i když absolutní pravděpodobnosti nejsou přesné.

Podmíněná nezávislost dovolí pro každou třídu odhadnout každý příznak samostatně. Místo jednoho p-rozměrného sdruženého rozdělení se odhaduje p jednorozměrných modelů. Přímá tabulka všech diskrétních kombinací by rostla exponenciálně a většina kombinací by nebyla pozorována. Naivní Bayes tak snižuje datovou náročnost a rozptyl odhadu za cenu systematického zkreslení a je relativně odolný vůči prokletí dimenzionality.

## Poznámka Anki 1785306291477

Karty Anki: 1785306291478
GUID: Dk4N6P(~|H; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Co ukazuje příklad naivního Bayese se třemi binárními příznaky a v čem spočívá problém nulové četnosti?

### Odpověď (Back)

Pro x=(0,1,1) byla třídní skóre 1/9 a 1/27, proto model predikoval Ŷ=1. V příkladu s většinovou funkcí Y klasifikoval téměř všechny vstupy správně navzdory porušené podmíněné nezávislosti.

Bod x=(1,0,1) však byl chybný, protože odhad P(X₂=0|Y=1)=0 vynuloval celé skóre správné třídy. To je problém nulové četnosti: nepozorovaná hodnota ve třídě dostane MLE pravděpodobnost 0. Jelikož třídní skóre násobí příspěvky všech příznaků, jediná nula přebije veškeré ostatní důkazy.

## Poznámka Anki 1785306291479

Karty Anki: 1785306291480
GUID: {UVP.h9.-I; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Jak se v naivním Bayesovi modeluje binární příznak Bernoulliho rozdělením a odhaduje pomocí MLE?

### Odpověď (Back)

Pro (X|Y=y)∼Be(p<sub>y</sub>) je p<sub>y</sub>=P(X=1|Y=y) a pro x∈{0,1}
P(X=x|Y=y)=p<sub>y</sub><sup>x</sup>(1−p<sub>y</sub>)<sup>1−x</sup>.

Označme N<sub>1,y</sub> počet bodů s X=1,Y=y a N<sub>0,y</sub> počet s X=0,Y=y. MLE je relativní četnost
p̂<sub>y</sub>=N<sub>1,y</sub>/(N<sub>1,y</sub>+N<sub>0,y</sub>),
protože maximalizuje věrohodnost pozorovaných nul a jedniček.

Pokud N<sub>1,y</sub>=0, dostaneme p̂=0; pokud N<sub>0,y</sub>=0, p̂=1. U malého vzorku tyto extrémy nerozumně vyjadřují absolutní jistotu a nepozorované hodnotě přiřazují nulovou pravděpodobnost.

## Poznámka Anki 1785306291481

Karty Anki: 1785306291482
GUID: -X|<X=MaIo; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Jak probíhá obecný bayesovský odhad parametru a jak se liší posteriorní průměr od MAP?

### Odpověď (Back)

Frekventistický přístup chápe parametr jako pevný a odhaduje jej z dat; bayesovský přístup popisuje nejistotu o parametru priorem f(p) a aktualizuje ji daty.

• **Prior f(p):** znalost či očekávání před daty.
• **Věrohodnost P(X=x|p):** pravděpodobnost dat jako funkce p.
• **Posterior:** f(p|x)=P(X=x|p)f(p)/P(X=x) ∝ P(X=x|p)f(p).
• **Evidence:** P(X=x)=∫P(X=x|p)f(p)dp; normalizuje posterior na integrál 1.

Materiál používá jako bodový odhad Bernoulliho parametru posteriorní střední hodnotu E[p|x]=∫p f(p|x)dp. Není totožná s MAP odhadem parametru: průměr integruje celý posterior, MAP hledá jeho maximum.

## Poznámka Anki 1785306291483

Karty Anki: 1785306291484
GUID: @va~cF~$at; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Jak Beta prior vede k add-one vyhlazení Bernoulliho pravděpodobnosti?

### Odpověď (Back)

Beta rozdělení je vhodný prior pro p∈(0,1) a je konjugované k Bernoulliho datům. Rovnoměrný prior Beta(1,1) po N₁ jedničkách a N₀ nulách dává posterior Beta(N₁+1,N₀+1) a posteriorní průměr
p̂=(N₁+1)/(N₁+N₀+2).

Jde o **add-one smoothing** neboli Laplaceovo pravidlo následnosti: přidá jeden pseudočet hodnotě 1 a jeden hodnotě 0. Odhad proto při konečných datech není přesně 0 ani 1. S rostoucím vzorkem relativní vliv dvou pseudočetů klesá a odhad se blíží empirické četnosti.

Příklady: N₁=1,N₀=4 → posterior Beta(2,5), p̂=2/7. N₁=7,N₀=13 → posterior Beta(8,14), p̂=8/22.

## Poznámka Anki 1785306291485

Karty Anki: 1785306291486
GUID: 1Xb(^o0]7I; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Jak se modeluje a vyhlazuje diskrétní příznak s k kategoriemi?

### Odpověď (Back)

Pro hodnoty c₁,…,c<sub>k</sub> se používá Cat(p<sub>y</sub>), kde p<sub>j,y</sub>=P(X=cⱼ|Y=y) a Σⱼp<sub>j,y</sub>=1. Je-li N<sub>j,y</sub> počet bodů třídy y s kategorií cⱼ, MLE je
p̂<sub>j,y</sub>=N<sub>j,y</sub>/ΣᵣN<sub>r,y</sub>.

Nepozorovaná kategorie dostane nulu a může vynulovat třídní skóre. Add-one odhad je
p̂<sub>j,y</sub>=(N<sub>j,y</sub>+1)/(ΣᵣN<sub>r,y</sub>+k).
Ve jmenovateli je +k, protože se přidává jeden pseudočet každé z k kategorií; součet čitatelů se rovná jmenovateli, takže pravděpodobnosti zůstanou normalizované. Bernoulliho rozdělení je speciální kategorický model se dvěma hodnotami.

## Poznámka Anki 1785306291487

Karty Anki: 1785306291488
GUID: /)QxHWo?^N; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Jak naivní Bayes pracuje se spojitými příznaky a se směsí diskrétních a spojitých příznaků?

### Odpověď (Back)

U spojité veličiny je P(X=x|Y=y)=0 pro každou přesnou hodnotu, proto se používá podmíněná hustota f<sub>X|Y=y</sub>(x). Podmíněná distribuční funkce je F<sub>X|y</sub>(x)=P(X≤x|Y=y) a hustota je její derivací, existuje-li.

Pro ℓ diskrétních a p−ℓ spojitých příznaků:
Ŷ=arg max<sub>y</sub>P(Y=y)∏ᵢ₌₁<sup>ℓ</sup>P(Xᵢ=xᵢ|Y=y)∏ᵢ₌ℓ₊₁<sup>p</sup>f<sub>Xᵢ|y</sub>(xᵢ).
Skóre tedy kombinuje prior, pravděpodobnostní hmotnosti diskrétních příznaků a hustoty spojitých příznaků.

## Poznámka Anki 1785306291489

Karty Anki: 1785306291490
GUID: ]$_:C8P_$q; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Jak funguje Gaussian Naive Bayes a jak se odhadují jeho parametry?

### Odpověď (Back)

Pro spojitý příznak se často předpokládá (X|Y=y)∼N(μ<sub>y</sub>,σ<sub>y</sub>²) s hustotou
f<sub>X|y</sub>(x)=1/√(2πσ<sub>y</sub>²) · exp[−(x−μ<sub>y</sub>)²/(2σ<sub>y</sub>²)].

MLE ve třídě y jsou
μ̂<sub>y</sub>=(1/N<sub>y</sub>)Σ<sub>i:Yᵢ=y</sub>xᵢ,
σ̂<sub>y</sub>²=(1/N<sub>y</sub>)Σ<sub>i:Yᵢ=y</sub>(xᵢ−μ̂<sub>y</sub>)².
Jmenovatel N<sub>y</sub> maximalizuje věrohodnost; N<sub>y</sub>−1 patří k nestrannému odhadu, což je jiný cíl.

Pro více spojitých příznaků Gaussian NB odhaduje pro každý příznak i a třídu y vlastní μ<sub>i,y</sub>,σ<sub>i,y</sub>² a předpokládá podmíněnou nezávislost jednorozměrných normálních modelů.

## Poznámka Anki 1785306291491

Karty Anki: 1785306291492
GUID: :faNE[*dxf; štítky: BI-ML2 iterace_05 Konsolidovano Prednaska_05.

### Otázka (Front)

Jak se vybírají varianty naivního Bayese, jak se model trénuje a jaké má silné a slabé stránky?

### Odpověď (Back)

Bernoulli, kategorický a Gaussovský NB používají stejný Bayesův a nezávislostní rámec, ale pro příznak volí podle jeho typu binární, konečně kategoriální nebo spojitý normální třídně podmíněný model.

**Trénování:** odhadnout priory tříd a pro každý příznak zvlášť parametry jeho rozdělení v každé třídě.
**Predikce:** pro každou třídu zkombinovat prior s příspěvky všech příznaků a vybrat nejvyšší skóre.

**Výhody:** jednoduchost, malá datová náročnost, přirozeně vícetřídní model a relativní odolnost ve vysoké dimenzi.
**Omezení:** často nerealistická podmíněná nezávislost, špatná kalibrace, nulové četnosti bez vyhlazení a závislost na vhodnosti jednorozměrných modelů.

Konstrukce postupuje: MAP → Bayesova věta rozloží posterior na prior a věrohodnost → podmíněná nezávislost rozloží věrohodnost na jednorozměrné faktory.

