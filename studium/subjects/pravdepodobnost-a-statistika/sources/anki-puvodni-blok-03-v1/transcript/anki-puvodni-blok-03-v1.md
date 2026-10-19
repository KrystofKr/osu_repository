# Pravděpodobnost a statistika – Původní blok 03

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::Pravděpodobnost a statistika
Rozsah: 22 poznámek, 22 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783851674900

Karty Anki: 1783851674900
GUID: b8P}_/OmJ0; štítky: konsolidace::blok_3 rozdeleni::binomicke.

### Otázka (Front)

Co modeluje binomické rozdělení, jaká je jeho pravděpodobnostní funkce a odkud vzorec pochází?

### Odpověď (Back)

Binomické rozdělení modeluje **počet úspěchů v n nezávislých Bernoulliho pokusech**, v nichž má každý pokus stejnou pravděpodobnost úspěchu p. Značí se **X∼Binom(n,p)** nebo Bin(n,p) a pro k=0,…,n platí:

**P(X=k)=C(n,k)p<sup>k</sup>(1−p)<sup>n−k</sup>.**

Každá konkrétní posloupnost s k úspěchy má pravděpodobnost p<sup>k</sup>(1−p)<sup>n−k</sup> a C(n,k) vybírá pozice k úspěchů. Normalizace plyne z binomické věty: Σ C(n,k)p<sup>k</sup>(1−p)<sup>n−k</sup>=(p+1−p)<sup>n</sup>=1. Bernoulliho rozdělení je speciální případ n=1.

## Poznámka Anki 1783851674901

Karty Anki: 1783851674901
GUID: K9rtB5yS@*; štítky: indikatory konsolidace::blok_3 rozdeleni::binomicke.

### Otázka (Front)

Jaké jsou střední hodnota a rozptyl binomické veličiny a jak je lze chápat přes součet indikátorů?

### Odpověď (Back)

Je-li **X∼Binom(n,p)**, pak
**E[X]=np** a **var(X)=np(1−p)**.

Binomickou veličinu lze psát jako **X=Σ<sub>i=1</sub><sup>n</sup>I<sub>i</sub>**, kde I<sub>i</sub> je indikátor úspěchu v i-tém pokusu. Linearita střední hodnoty dává E[X]=Σp=np; při nezávislosti se rozptyly sčítají, takže var(X)=Σp(1−p)=np(1−p). Průměr np je očekávaný počet úspěchů. Rozptyl je největší kolem p=1/2 a mizí pro p=0 nebo p=1.

## Poznámka Anki 1783851674902

Karty Anki: 1783851674902
GUID: dQJ7tSvj1s; štítky: bernoulli indikatory konsolidace::blok_3.

### Otázka (Front)

Co je indikátor jevu, jaké má rozdělení a proč je užitečný?

### Odpověď (Back)

Indikátor jevu A je náhodná veličina
**1<sub>A</sub>=1**, nastane-li A, a **1<sub>A</sub>=0**, nenastane-li A.

Má Bernoulliho rozdělení s parametrem p=P(A): P(1<sub>A</sub>=1)=P(A), P(1<sub>A</sub>=0)=1−P(A). Bernoulliho veličinu lze tedy chápat jako indikátor jevu „úspěch“. Indikátory převádějí jevy na čísla, takže lze počty událostí vyjádřit součtem a snadno počítat jejich střední hodnoty či rozptyly.

## Poznámka Anki 1783851674903

Karty Anki: 1783851674903
GUID: uYEd_POSB7; štítky: konsolidace::blok_3 priklady rozdeleni::binomicke.

### Otázka (Front)

Jak se řeší příklad s počtem šestek v 10 hodech kostkou?

### Odpověď (Back)

Je-li X počet šestek v 10 nezávislých hodech férovou kostkou, pak **X∼Binom(10,1/6)**.

Střední počet šestek je **E[X]=10/6≈1,67**.
Pravděpodobnost alespoň tří šestek lze počítat přímo
P(X≥3)=Σ<sub>k=3</sub><sup>10</sup>C(10,k)(1/6)<sup>k</sup>(5/6)<sup>10−k</sup>,
nebo efektivněji doplňkem
**P(X≥3)=1−P(X=0)−P(X=1)−P(X=2)≈0,224.**

## Poznámka Anki 1783851674904

Karty Anki: 1783851674904
GUID: EBq6b<(j=(; štítky: konsolidace::blok_3 rozdeleni::geometricke.

### Otázka (Front)

Co modeluje geometrické rozdělení a jaké jsou jeho PMF, CDF a funkce přežití?

### Odpověď (Back)

Geometrické rozdělení modeluje **počet pokusů do prvního úspěchu** v nezávislých Bernoulliho pokusech s pravděpodobností úspěchu p. Při konvenci X∈{1,2,…} značíme **X∼Geom(p)** a platí:

**P(X=k)=(1−p)<sup>k−1</sup>p**, k=1,2,…
**P(X>k)=(1−p)<sup>k</sup>**
**F<sub>X</sub>(k)=P(X≤k)=1−(1−p)<sup>k</sup>**.

Prvních k−1 pokusů musí být neúspěšných a k-tý úspěšný. Součet pravděpodobností je 1 díky geometrické řadě.

## Poznámka Anki 1783851674905

Karty Anki: 1783851674905
GUID: H0ro[rb`j%; štítky: konsolidace::blok_3 rozdeleni::geometricke.

### Otázka (Front)

Jaké jsou střední hodnota, rozptyl a interpretace geometrického rozdělení?

### Odpověď (Back)

Pro **X∼Geom(p)** na {1,2,…} platí:
**E[X]=1/p**, **var(X)=(1−p)/p²**.

Hodnota 1/p je průměrný počet pokusů do prvního úspěchu. Když p klesá, úspěch přichází v průměru později, rozptyl roste a pravý chvost se prodlužuje. Geometrické rozdělení je diskrétní model čekací doby do první události.

## Poznámka Anki 1783851674906

Karty Anki: 1783851674906
GUID: g$sR9of)mr; štítky: konsolidace::blok_3 rozdeleni::poissonovo.

### Otázka (Front)

Co modeluje Poissonovo rozdělení, jak je definováno a jak souvisí s binomickým?

### Odpověď (Back)

Poissonovo rozdělení modeluje **počet relativně vzácných událostí v daném časovém či prostorovém intervalu**, například požadavků na server, zákazníků nebo překlepů. Značí se **X∼Poisson(λ)**, λ>0, a platí:

**P(X=k)=e<sup>−λ</sup>λ<sup>k</sup>/k!**, k=0,1,2,…

Normalizace plyne z řady pro exponenciálu. Poissonovo rozdělení je limitou Binom(n,p), když n→∞, p→0 a np→λ: existuje mnoho příležitostí k události, každá má malou šanci, ale celková očekávaná četnost zůstává λ.

## Poznámka Anki 1783851674907

Karty Anki: 1783851674907
GUID: v+>5cT::J[; štítky: konsolidace::blok_3 rozdeleni::poissonovo.

### Otázka (Front)

Jaké jsou střední hodnota, rozptyl a interpretace parametru Poissonova rozdělení?

### Odpověď (Back)

Je-li **X∼Poisson(λ)**, pak
**E[X]=λ** a **var(X)=λ**.

Parametr λ je očekávaný počet událostí ve sledovaném intervalu a současně určuje variabilitu počtu. Rovnost průměru a rozptylu je charakteristickým rysem základního Poissonova modelu.

## Poznámka Anki 1783851674908

Karty Anki: 1783851674908
GUID: lO$:n7odrY; štítky: konsolidace::blok_3 priklady rozdeleni::poissonovo.

### Otázka (Front)

Jak se použije Poissonova aproximace v příkladu s překlepy?

### Odpověď (Back)

Autor dělá průměrně jeden překlep na 1000 znaků a normostrana má 1800 znaků. Při modelu mnoha znaků s malou pravděpodobností překlepu je
**λ=np=1800·(1/1000)=1,8**, takže X≈Poisson(1,8).

Střední počet překlepů je E[X]=1,8 a pravděpodobnost žádného překlepu je
**P(X=0)=e<sup>−1,8</sup>≈0,165.**

## Poznámka Anki 1783851674909

Karty Anki: 1783851674909
GUID: ib[BH;N[vU; štítky: konsolidace::blok_3 rozdeleni::diskretni srovnani.

### Otázka (Front)

Jak se porovnávají Bernoulliho, binomické, geometrické a Poissonovo rozdělení?

### Odpověď (Back)

**Bernoulli(p)**: jeden pokus; E=p, var=p(1−p).
**Binom(n,p)**: počet úspěchů v pevných n pokusech; E=np, var=np(1−p).
**Geom(p)**: počet pokusů do prvního úspěchu; E=1/p, var=(1−p)/p².
**Poisson(λ)**: počet vzácných událostí v intervalu; E=var=λ.

Poissonovo rozdělení aproximuje binomické při velkém n, malém p a λ=np. Strukturálně: binomické počítá v pevném počtu pokusů, geometrické čeká na první úspěch a Poissonovo počítá události v čase či prostoru.

## Poznámka Anki 1783851674910

Karty Anki: 1783851674910
GUID: ny7R3&c-uG; štítky: konsolidace::blok_3 rozdeleni::rovnomerne.

### Otázka (Front)

Jak je definováno rovnoměrné rozdělení na intervalu a jak vypadá jeho CDF?

### Odpověď (Back)

Pro **X∼Unif(a,b)**, a<b, je hustota konstantní:
**f<sub>X</sub>(x)=1/(b−a)** pro x∈(a,b) a 0 jinak. Výška je 1/(b−a), aby plocha obdélníku byla 1.

Distribuční funkce je
F<sub>X</sub>(x)=0 pro x<a,
**F<sub>X</sub>(x)=(x−a)/(b−a)** pro a≤x≤b,
F<sub>X</sub>(x)=1 pro x>b.

## Poznámka Anki 1783851674911

Karty Anki: 1783851674911
GUID: y6`|#G*bbN; štítky: konsolidace::blok_3 rozdeleni::rovnomerne.

### Otázka (Front)

Jaké jsou střední hodnota a rozptyl rovnoměrného rozdělení a jak se interpretují?

### Odpověď (Back)

Pro **X∼Unif(a,b)** platí
**E[X]=(a+b)/2** a **var(X)=(b−a)²/12**.

Střední hodnota je střed intervalu, což odpovídá symetrii. Rozptyl závisí na čtverci délky intervalu: zdvojnásobení šířky intervalu zvětší rozptyl čtyřikrát.

## Poznámka Anki 1783851674912

Karty Anki: 1783851674912
GUID: nApgiSZV|<; štítky: konsolidace::blok_3 rozdeleni::exponencialni.

### Otázka (Front)

Jak je definováno exponenciální rozdělení a jak souvisí s Poissonovým procesem?

### Odpověď (Back)

Exponenciální rozdělení modeluje **spojitou čekací dobu do další události**. Pro **X∼Exp(λ)**, λ>0, platí
**f<sub>X</sub>(x)=λe<sup>−λx</sup>** pro x≥0 a 0 jinak,
**F<sub>X</sub>(x)=1−e<sup>−λx</sup>** pro x≥0.

Hustota je normalizovaná, protože ∫₀∞λe<sup>−λx</sup>dx=1. V Poissonově procesu Poissonovo rozdělení popisuje počet událostí v intervalu, zatímco exponenciální rozdělení dobu mezi událostmi.

## Poznámka Anki 1783851674913

Karty Anki: 1783851674913
GUID: b7#=Kd~+J); štítky: konsolidace::blok_3 rozdeleni::exponencialni.

### Otázka (Front)

Jaké jsou momenty, funkce přežití a vliv parametru λ u exponenciálního rozdělení?

### Odpověď (Back)

Pro **X∼Exp(λ)** platí
**E[X]=1/λ**, **var(X)=1/λ²**,
**P(X>t)=e<sup>−λt</sup>** pro t≥0 a F(t)=1−e<sup>−λt</sup>.

Parametr λ je intenzita událostí. Větší λ znamená kratší typickou čekací dobu, strmější pokles hustoty a více hmoty blízko nuly. Funkce přežití je doplněk distribuční funkce.

## Poznámka Anki 1783851674914

Karty Anki: 1783851674914
GUID: rsX.#_+MIr; štítky: konsolidace::blok_3 priklady rozdeleni::exponencialni.

### Otázka (Front)

Jak se řeší příklad s exponenciální životností lampy?

### Odpověď (Back)

Je-li životnost lampy **X∼Exp(1/100)** hodin, pak λ=0,01 h⁻¹.

Střední životnost je **E[X]=1/λ=100 hodin**.
Pravděpodobnost, že vydrží déle než 50 hodin, je
**P(X>50)=e<sup>−λ·50</sup>=e<sup>−1/2</sup>≈0,606.**

## Poznámka Anki 1783851674915

Karty Anki: 1783851674915
GUID: D&?.gm_o-1; štítky: konsolidace::blok_3 rozdeleni::prechody.

### Otázka (Front)

Jak spolu souvisejí diskrétní a spojité modely čekání a proč se přechází k hustotám?

### Odpověď (Back)

**Geometrické rozdělení** modeluje diskrétní počet pokusů do prvního úspěchu; **exponenciální rozdělení** modeluje spojitý čas do první události. Diskrétní modely přiřazují pravděpodobnosti jednotlivým hodnotám, zatímco u spojitých veličin mají body pravděpodobnost nula a pravděpodobnosti intervalů se počítají integrací hustoty.

## Poznámka Anki 1783851674916

Karty Anki: 1783851674916
GUID: g@+sy2`Fdd; štítky: konsolidace::blok_3 rozdeleni::normalni.

### Otázka (Front)

Co modeluje normální rozdělení, jak je definováno a co je standardní normální rozdělení?

### Odpověď (Back)

Normální rozdělení modeluje spojité veličiny vznikající jako výsledek mnoha malých vlivů a často aproximuje součty či průměry. Pro **X∼N(μ,σ²)** má hustotu
**f<sub>X</sub>(x)=1/(σ√(2π))·exp(−(x−μ)²/(2σ²))**, x∈ℝ.

Je třeba ověřit konvenci zápisu: druhý parametr bývá rozptyl σ², někdy směrodatná odchylka σ. **Standardní normální rozdělení** je N(0,1) a jeho CDF se značí **Φ**. Φ nemá elementární uzavřený tvar, proto se počítá numericky či z tabulek.

## Poznámka Anki 1783851674917

Karty Anki: 1783851674917
GUID: v#]*RnTNq>; štítky: konsolidace::blok_3 rozdeleni::normalni.

### Otázka (Front)

Jaký je tvar normálního rozdělení a jak parametry μ a σ ovlivňují jeho polohu a šířku?

### Odpověď (Back)

Normální hustota je zvonovitá a symetrická kolem μ. Platí **E[X]=μ**, **var(X)=σ²**; díky symetrii splývá střední hodnota, medián a modus v μ.

Změna μ při pevném σ pouze posune křivku. Větší σ ji rozšíří a sníží, menší σ ji zúží a zvýší. Hodnoty stejně vzdálené od μ mají stejnou hustotu.

## Poznámka Anki 1783851674918

Karty Anki: 1783851674918
GUID: KZN]uH8Gbq; štítky: konsolidace::blok_3 standardizace.

### Otázka (Front)

Co je standardizace obecné náhodné veličiny a co zaručuje?

### Odpověď (Back)

Má-li X konečnou střední hodnotu μ a kladný konečný rozptyl σ², standardizujeme ji transformací
**Z=(X−μ)/σ**.

Odečtení μ vystředí veličinu a dělení σ ji přeškáluje, takže **E[Z]=0** a **var(Z)=1**. Standardizace není omezena na spojité veličiny; platí i pro diskrétní. U obecné veličiny však neurčuje konkrétní tvar výsledného rozdělení.

## Poznámka Anki 1783851674919

Karty Anki: 1783851674919
GUID: P2K%Pj$bZQ; štítky: konsolidace::blok_3 rozdeleni::normalni standardizace.

### Otázka (Front)

Jak se standardizuje normální veličina a jak se pomocí Φ počítají pravděpodobnosti?

### Odpověď (Back)

Je-li **X∼N(μ,σ²)**, pak
**Z=(X−μ)/σ∼N(0,1)**.

Z-skóre z=(x−μ)/σ říká, o kolik směrodatných odchylek je x od μ. Platí
**F<sub>X</sub>(x)=Φ((x−μ)/σ)**,
**P(X>x)=1−Φ((x−μ)/σ)**.

Postup: určit μ a σ, převést hranice na z-skóre, vyhledat Φ a podle intervalu použít rozdíl či doplněk. Obecná standardizace dává jen průměr 0 a rozptyl 1; u normální veličiny navíc přesně zachovává normální rodinu a vede k N(0,1).

## Poznámka Anki 1783851674920

Karty Anki: 1783851674920
GUID: uuR3+*jI{<; štítky: konsolidace::blok_3 priklady rozdeleni::normalni.

### Otázka (Front)

Jaká je pravděpodobnost, že kapr váží přes 3 kg, když X∼N(2,5;0,3²)?

### Odpověď (Back)

Standardizujeme hranici 3 kg:
**z=(3−2,5)/0,3≈1,67.**

Z tabulky nebo numericky Φ(1,67)≈0,9525, proto
**P(X>3)=1−Φ(1,67)≈0,0475**, tedy přibližně 4,75 %.

## Poznámka Anki 1783851674921

Karty Anki: 1783851674921
GUID: N9.CO|&dBl; štítky: konsolidace::blok_3 rozdeleni::spojita srovnani.

### Otázka (Front)

Jak se porovnávají rovnoměrné, exponenciální a normální rozdělení?

### Odpověď (Back)

**Unif(a,b)**: ploché na omezeném intervalu; f=1/(b−a), E=(a+b)/2, var=(b−a)²/12.
**Exp(λ)**: jednostranné na [0,∞), model čekací doby; f=λe<sup>−λx</sup>, E=1/λ, var=1/λ². Jeden parametr současně určuje polohu i rozptýlení.
**N(μ,σ²)**: symetrické na celé ℝ; f=exp(−(x−μ)²/(2σ²))/(σ√(2π)), E=μ, var=σ². Poloha a šířka jsou odděleny parametry μ a σ².

Normální rozdělení se standardizací převádí na univerzální N(0,1).

