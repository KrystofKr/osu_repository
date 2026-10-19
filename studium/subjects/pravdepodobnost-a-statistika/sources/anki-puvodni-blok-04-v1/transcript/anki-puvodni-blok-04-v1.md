# Pravděpodobnost a statistika – Původní blok 04

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::Pravděpodobnost a statistika
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783851674922

Karty Anki: 1783851674922
GUID: iHGzZ7p;:,; štítky: konsolidace::blok_4 nahodny_vektor sdruzene_rozdeleni.

### Otázka (Front)

Co je náhodný vektor a jak jej popisuje sdružená distribuční funkce?

### Odpověď (Back)

Náhodný vektor je **n-tice náhodných veličin definovaných na stejném pravděpodobnostním prostoru**, například (X,Y). Používá se, když na jednom výsledku experimentu sledujeme více veličin a jejich závislost.

Pro X=(X<sub>1</sub>,…,X<sub>n</sub>) je sdružená distribuční funkce
**F<sub>X</sub>(x<sub>1</sub>,…,x<sub>n</sub>)=P(X<sub>1</sub>≤x<sub>1</sub>,…,X<sub>n</sub>≤x<sub>n</sub>)**.
Ve dvou rozměrech F<sub>X,Y</sub>(x,y)=P(X≤x,Y≤y). Zachycuje celé společné rozdělení a je neklesající v každé souřadnici. Jde k 0, pošleme-li některý práh do −∞; po poslání jedné souřadnice do +∞ dostaneme marginální CDF druhé veličiny:
**F<sub>X</sub>(x)=lim<sub>y→∞</sub>F<sub>X,Y</sub>(x,y)**, **F<sub>Y</sub>(y)=lim<sub>x→∞</sub>F<sub>X,Y</sub>(x,y)**.

## Poznámka Anki 1783851674923

Karty Anki: 1783851674923
GUID: PZVDWzEG]y; štítky: hustota konsolidace::blok_4 sdruzene_rozdeleni.

### Otázka (Front)

Co je sdružená hustota a jak souvisí se sdruženou distribuční funkcí?

### Odpověď (Back)

Pro spojitý pár (X,Y) je sdružená hustota **f<sub>X,Y</sub>(x,y)≥0** a musí splňovat
**∫<sub>−∞</sub><sup>∞</sup>∫<sub>−∞</sub><sup>∞</sup>f<sub>X,Y</sub>(x,y) dx dy=1**.

Sdružená distribuční funkce vznikne integrací přes levý dolní obdélník:
**F<sub>X,Y</sub>(x,y)=∫<sub>−∞</sub><sup>y</sup>∫<sub>−∞</sub><sup>x</sup>f<sub>X,Y</sub>(u,v) du dv**.
V bodech, kde příslušné derivace existují, platí
**f<sub>X,Y</sub>(x,y)=∂²F<sub>X,Y</sub>(x,y)/(∂x∂y)**.

## Poznámka Anki 1783851674924

Karty Anki: 1783851674924
GUID: QnPOg-;0L^; štítky: konsolidace::blok_4 pravdepodobnost_oblasti sdruzene_rozdeleni.

### Otázka (Front)

Jak se ze sdružené hustoty počítá pravděpodobnost oblasti a které množiny mají pravděpodobnost nula?

### Odpověď (Back)

Pro borelovskou oblast B⊂ℝ² platí
**P((X,Y)∈B)=∬<sub>B</sub>f<sub>X,Y</sub>(x,y) dx dy**.

Pro obdélník je
**P(a<X≤b, c<Y≤d)=∫<sub>c</sub><sup>d</sup>∫<sub>a</sub><sup>b</sup>f<sub>X,Y</sub>(x,y) dx dy**.

U absolutně spojitého sdruženého rozdělení mají jednotlivé body i svislé či vodorovné čáry nulovou pravděpodobnost: P(X=x,Y=y)=0, P(X=x,Y∈B)=0 a P(X∈A,Y=y)=0. Pravděpodobnost vzniká až integrací přes oblast s kladnou plochou.

## Poznámka Anki 1783851674925

Karty Anki: 1783851674925
GUID: JDzJ;(?UU-; štítky: konsolidace::blok_4 marginalni_rozdeleni.

### Otázka (Front)

Co je marginální rozdělení a jak se získá ze sdruženého rozdělení?

### Odpověď (Back)

Marginální rozdělení popisuje **jednu složku náhodného vektoru bez ohledu na ostatní složky**.

Diskrétně se druhá proměnná vysčítá:
**P(X=x)=Σ<sub>y</sub>P(X=x,Y=y)**.

Spojitě se druhá proměnná odintegruje:
**f<sub>X</sub>(x)=∫<sub>−∞</sub><sup>∞</sup>f<sub>X,Y</sub>(x,y)dy**,
**f<sub>Y</sub>(y)=∫<sub>−∞</sub><sup>∞</sup>f<sub>X,Y</sub>(x,y)dx**.

Marginály tedy zachovají chování jednotlivých veličin, ale samy o sobě mohou ztratit informaci o jejich vzájemné závislosti.

## Poznámka Anki 1783851674926

Karty Anki: 1783851674926
GUID: F?3=f/8LmG; štítky: faktorovani konsolidace::blok_4 nezavislost.

### Otázka (Front)

Jak se pomocí hustot pozná nezávislost náhodných veličin?

### Odpověď (Back)

Spojité veličiny X a Y jsou nezávislé právě tehdy, když se **celá sdružená hustota včetně svého oboru** rozloží jako
**f<sub>X,Y</sub>(x,y)=f<sub>X</sub>(x)f<sub>Y</sub>(y)** pro všechna x,y.
Pro n veličin obdobně f<sub>X</sub>(x<sub>1</sub>,…,x<sub>n</sub>)=∏f<sub>Xᵢ</sub>(x<sub>i</sub>).

Stačí-li hustotu napsat jako g(x)h(y) na kartézském součinovém nosiči, normalizace z g a h vytvoří marginální hustoty, a tedy prokáže nezávislost.

Příklad: f<sub>X,Y</sub>(x,y)=ye<sup>−2x</sup> pro x≥0 a 0≤y≤2 (jinak 0). Pak f<sub>X</sub>(x)=2e<sup>−2x</sup> a f<sub>Y</sub>(y)=y/2, takže jejich součin je původní sdružená hustota.

## Poznámka Anki 1783851674927

Karty Anki: 1783851674927
GUID: eR2;L.5b)!; štítky: diskretni konsolidace::blok_4 podminene_rozdeleni.

### Otázka (Front)

Jak se definuje diskrétní podmíněné rozdělení a podmíněná střední hodnota?

### Odpověď (Back)

Je-li P(Y=y)>0, pak
**P(X=x|Y=y)=P(X=x,Y=y)/P(Y=y)**.
Podmíněné rozdělení popisuje X poté, co jsme získali informaci Y=y.

Podmíněná střední hodnota je
**E[X|Y=y]=Σ<sub>x</sub>x·P(X=x|Y=y)**.

Rozdíl mezi E[X|Y=y] a nepodmíněnou E[X] ukazuje, jak informace o Y mění očekávání X. Při nezávislosti podmínění rozdělení X nemění.

## Poznámka Anki 1783851674928

Karty Anki: 1783851674928
GUID: xOYup1gds6; štítky: konsolidace::blok_4 podminene_rozdeleni spojite.

### Otázka (Front)

Jak se definuje podmíněné rozdělení spojitých veličin, když P(Y=y)=0?

### Odpověď (Back)

U spojité veličiny nelze použít běžný podíl P(A∩{Y=y})/P(Y=y), protože **P(Y=y)=0**. Definice se motivuje podmíněním na stále menší interval kolem y a limitním přechodem.

Pro f<sub>Y</sub>(y)>0 je podmíněná hustota
**f<sub>X|Y</sub>(x|y)=f<sub>X,Y</sub>(x,y)/f<sub>Y</sub>(y)**.
Podmíněná CDF je
**F<sub>X|Y</sub>(x|y)=∫<sub>−∞</sub><sup>x</sup>f<sub>X,Y</sub>(u,y)/f<sub>Y</sub>(y) du**
a podmíněná střední hodnota
**E[X|Y=y]=∫<sub>−∞</sub><sup>∞</sup>x f<sub>X|Y</sub>(x|y)dx**.

Zápis P(X≤x|Y=y) je zde standardní značení objektu definovaného přes hustoty, nikoli doslovné použití elementárního vzorce pro podmíněnou pravděpodobnost.

## Poznámka Anki 1783851674929

Karty Anki: 1783851674929
GUID: k4a(J.11+H; štítky: konsolidace::blok_4 nahodny_vektor transformace.

### Otázka (Front)

Jak se určuje rozdělení funkce náhodného vektoru Y=h(X₁,…,Xₙ)?

### Odpověď (Back)

Funkce náhodného vektoru vytváří novou veličinu **Y=h(X<sub>1</sub>,…,X<sub>n</sub>)**.

Diskrétně:
**F<sub>Y</sub>(y)=Σ<sub>h(x₁,…,xₙ)≤y</sub>P(X<sub>1</sub>=x<sub>1</sub>,…,X<sub>n</sub>=x<sub>n</sub>)**.

Spojitě:
**F<sub>Y</sub>(y)=∫…∫<sub>{x:h(x)≤y}</sub>f<sub>X</sub>(x)dx<sub>1</sub>…dx<sub>n</sub>**.

V obou případech tedy sečteme nebo zintegrujeme sdružené rozdělení přes množinu vstupů, pro něž h≤y. Zvlášť důležitým případem je součet Z=X<sub>1</sub>+…+X<sub>n</sub>.

## Poznámka Anki 1783851674930

Karty Anki: 1783851674930
GUID: k9f>?,/|$C; štítky: konsolidace::blok_4 konvoluce nezavislost soucet.

### Otázka (Front)

Co je konvoluce a jak dává rozdělení součtu nezávislých veličin?

### Odpověď (Back)

Pro **Z=X+Y** a nezávislé veličiny se sdružené rozdělení rozpadá na součin marginál, což vede ke konvoluci.

Diskrétně:
**P(Z=z)=Σ<sub>x</sub>P(X=x)P(Y=z−x)**.
Sečtou se příspěvky všech dvojic (x,z−x), které dávají součet z.

Spojitě:
**f<sub>Z</sub>(z)=∫<sub>−∞</sub><sup>∞</sup>f<sub>X</sub>(x)f<sub>Y</sub>(z−x)dx**.
Integruje se přes všechny rozklady z=x+(z−x). Bez nezávislosti je nutné použít přímo sdruženou PMF či hustotu; jednoduchý součin marginál obecně neplatí.

## Poznámka Anki 1783851674931

Karty Anki: 1783851674931
GUID: baJ~|vtiZE; štítky: konsolidace::blok_4 normalni poissonovo soucet.

### Otázka (Front)

Které běžné rodiny rozdělení jsou uzavřené na sčítání nezávislých veličin?

### Odpověď (Back)

Pro nezávislé normální veličiny platí
**X∼N(μ<sub>X</sub>,σ<sub>X</sub>²), Y∼N(μ<sub>Y</sub>,σ<sub>Y</sub>²) ⇒ X+Y∼N(μ<sub>X</sub>+μ<sub>Y</sub>,σ<sub>X</sub>²+σ<sub>Y</sub>²)**.
Proto součet n nezávislých N(μ,σ²) má N(nμ,nσ²); zvlášť dvě N(μ,1) dávají N(2μ,2).

Pro nezávislé Poissonovy veličiny platí
**X∼Poisson(λ), Y∼Poisson(μ) ⇒ X+Y∼Poisson(λ+μ)**.

Uzavřenost lze dokázat konvolucí nebo identifikací součinu momentových vytvořujících funkcí.

## Poznámka Anki 1783851674932

Karty Anki: 1783851674932
GUID: I2|cX)*b*R; štítky: konsolidace::blok_4 mgf nezavislost soucet.

### Otázka (Front)

Jak momentová vytvořující funkce určuje součet nezávislých veličin?

### Odpověď (Back)

Momentová vytvořující funkce je M<sub>X</sub>(s)=E[e<sup>sX</sup>]. Pro nezávislé veličiny platí
**M<sub>X+Y</sub>(s)=M<sub>X</sub>(s)M<sub>Y</sub>(s)**, obecně M<sub>ΣXᵢ</sub>(s)=∏M<sub>Xᵢ</sub>(s). To často identifikuje rozdělení součtu snáze než přímá konvoluce.

Pro nezávislé Bernoulli(p): M(s)=1−p+pe<sup>s</sup>, takže součet n veličin má M(s)=(1−p+pe<sup>s</sup>)<sup>n</sup>, tedy **Binom(n,p)**.

Pro Poisson(λ): M(s)=e<sup>λ(eˢ−1)</sup>. Součin pro parametry λ a μ je e<sup>(λ+μ)(eˢ−1)</sup>, tedy MGF **Poisson(λ+μ)**.

## Poznámka Anki 1783851674933

Karty Anki: 1783851674933
GUID: khpR!/]S%B; štítky: funkce konsolidace::blok_4 linearita stredni_hodnota.

### Otázka (Front)

Jak se počítá E[h(X,Y)] a vyžaduje linearita střední hodnoty nezávislost?

### Odpověď (Back)

Očekávání funkce lze spočítat přímo ze sdruženého rozdělení, aniž bychom nejprve hledali rozdělení h(X,Y).

Diskrétně:
**E[h(X,Y)]=Σ<sub>i,j</sub>h(x<sub>i</sub>,y<sub>j</sub>)P(X=x<sub>i</sub>,Y=y<sub>j</sub>)**.
Spojitě:
**E[h(X,Y)]=∫∫h(x,y)f<sub>X,Y</sub>(x,y)dxdy**.
Požaduje se příslušná absolutní konvergence či integrabilita.

Pro h(x,y)=ax+by dostáváme **E[aX+bY]=aE[X]+bE[Y]**. Linearita střední hodnoty **nevyžaduje nezávislost**; stačí existence očekávání.

## Poznámka Anki 1783851674934

Karty Anki: 1783851674934
GUID: FlU9+L3h!0; štítky: konsolidace::blok_4 kovariance nekorelovanost nezavislost.

### Otázka (Front)

Co je kovariance a jaký je vztah mezi nezávislostí a nekorelovaností?

### Odpověď (Back)

Kovariance je
**cov(X,Y)=E[(X−E[X])(Y−E[Y])]=E[XY]−E[X]E[Y]**.
Měří společné **lineární** kolísání kolem středních hodnot.

Veličiny jsou nekorelované, když cov(X,Y)=0, ekvivalentně E[XY]=E[X]E[Y]. **Nezávislost implikuje nekorelovanost**, protože faktorování sdruženého rozdělení dává E[XY]=E[X]E[Y]. Opačná implikace obecně neplatí: nulová kovariance vylučuje jen lineární vztah, nikoli všechny formy závislosti.

## Poznámka Anki 1783851674935

Karty Anki: 1783851674935
GUID: cKJ_N;cA;E; štítky: konsolidace::blok_4 korelace.

### Otázka (Front)

Co je korelační koeficient a jak se interpretuje?

### Odpověď (Back)

Mají-li X a Y kladné konečné rozptyly, pak
**ρ(X,Y)=cov(X,Y)/(σ<sub>X</sub>σ<sub>Y</sub>)** a **−1≤ρ≤1**.

ρ je bezrozměrná míra lineární závislosti: kladné znaménko značí společný růst, záporné růst jedné při poklesu druhé a ρ=0 absenci lineární korelace, nikoli nutně nezávislost.

Posuny a kladné změny měřítka korelaci nemění: pro a,c>0 platí ρ(aX+b,cY+d)=ρ(X,Y). Hodnota |ρ|=1 nastává právě při přesném afinním vztahu Y=aX+b téměř jistě; znaménko ρ odpovídá znaménku a.

## Poznámka Anki 1783851674936

Karty Anki: 1783851674936
GUID: jN1s$kHhKu; štítky: konsolidace::blok_4 kovariance linearni_kombinace rozptyl.

### Otázka (Front)

Jak kovariance vstupuje do rozptylu součtu a obecné lineární kombinace?

### Odpověď (Back)

Rozptyl je speciální kovariance: **cov(X,X)=var(X)**.

Pro dvě veličiny platí
**var(X±Y)=var(X)+var(Y)±2cov(X,Y)**
a obecně
**var(aX+bY)=a²var(X)+b²var(Y)+2ab·cov(X,Y)**.

Jsou-li veličiny nekorelované — zejména nezávislé — kovarianční člen zmizí a rozptyly se sčítají. Střední hodnota je vždy lineární, ale rozptyl nikoli. Kladná kovariance zvětšuje rozptyl součtu, protože odchylky bývají stejného směru; záporná jej zmenšuje, protože se odchylky částečně kompenzují.

## Poznámka Anki 1783851674937

Karty Anki: 1783851674937
GUID: Ce}$iT4Z<B; štítky: konsolidace::blok_4 nahodny_vektor shrnuti.

### Otázka (Front)

Jaký je celkový postup práce s více náhodnými veličinami?

### Odpověď (Back)

**1. Sdružené rozdělení** popíše veličiny současně a zachová jejich závislost.
**2. Marginální rozdělení** získáme sečtením nebo integrací přes ostatní složky.
**3. Podmíněné rozdělení** vznikne normalizací sdruženého rozdělení vzhledem k dané hodnotě druhé veličiny.
**4. Funkce vektoru**, zejména součet, se řeší integrací přes vhodnou oblast; při nezávislosti součet dává konvoluci a MGF se násobí.
**5. Závislost** kvantifikují kovariance a korelace; při rozptylu součtu se projeví kovarianční člen.

Tento rámec rozšiřuje teorii jedné náhodné veličiny na společné chování více veličin.

