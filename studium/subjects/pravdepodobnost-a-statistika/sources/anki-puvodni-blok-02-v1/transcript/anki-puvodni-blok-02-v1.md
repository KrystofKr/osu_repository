# Pravděpodobnost a statistika – Původní blok 02

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::Pravděpodobnost a statistika
Rozsah: 34 poznámek, 34 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783851674866

Karty Anki: 1783851674866
GUID: vMCEsDXJf>; štítky: konsolidace::blok_2 nahodne_veliciny::zaklady.

### Otázka (Front)

Co je náhodná veličina, proč ji zavádíme a jak zní podmínka její měřitelnosti?

### Odpověď (Back)

Náhodná veličina je číselná funkce **X: Ω→ℝ**, která každému výsledku ω přiřadí sledovanou číselnou charakteristiku. Zavádíme ji, abychom z výsledku experimentu vybrali relevantní informaci a mohli ji matematicky zpracovat.

Formálně musí pro každé x∈ℝ platit **{ω∈Ω: X(ω)≤x}∈F**. Tato měřitelnost zajišťuje, že výroky typu X≤x, X=x nebo X∈(a,b) jsou jevy, jimž lze přiřadit pravděpodobnost.

## Poznámka Anki 1783851674867

Karty Anki: 1783851674867
GUID: lsrkH!dj!U; štítky: konsolidace::blok_2 nahodne_veliciny::zaklady.

### Otázka (Front)

Jaké jsou základní typy náhodných veličin a jaké nástroje popisují jejich rozdělení?

### Odpověď (Back)

**Diskrétní** veličina nabývá nejvýše spočetně mnoha izolovaných hodnot a popisujeme ji bodovými pravděpodobnostmi. **Absolutně spojitá** veličina se popisuje hustotou a pravděpodobnostmi intervalů. Univerzálním popisem obou typů je distribuční funkce F_X(x)=P(X≤x).

Typický tok látky je: náhodná veličina → distribuční funkce → diskrétní pravděpodobnostní funkce nebo spojitá hustota → transformace → kvantily a simulace → charakteristiky polohy a šířky, zejména střední hodnota a rozptyl.

## Poznámka Anki 1783851674868

Karty Anki: 1783851674868
GUID: Hf+k&R9Rq@; štítky: konsolidace::blok_2 nahodne_veliciny::distribucni_funkce.

### Otázka (Front)

Jaké vlastnosti má distribuční funkce a jak z ní získáme základní pravděpodobnosti?

### Odpověď (Back)

[Obrázek: paste-1cfd4c1b9732eaab8afae355e4288ea8663f571f.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1783851674869

Karty Anki: 1783851674869
GUID: H1hWY_X([); štítky: konsolidace::blok_2 nahodne_veliciny::priklady.

### Otázka (Front)

Jaké je rozdělení minima dvou nezávislých hodů férovou čtyřstěnnou kostkou?

### Odpověď (Back)

[Obrázek: paste-57ef9bee5acf51a54eeafa74fb044e383351df34.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1783851674870

Karty Anki: 1783851674870
GUID: Be<PAQrWP|; štítky: konsolidace::blok_2 nahodne_veliciny::diskretni.

### Otázka (Front)

Jak se popisuje rozdělení diskrétní náhodné veličiny a jak souvisí její pravděpodobnostní a distribuční funkce?

### Odpověď (Back)

[Obrázek: paste-e7bdf177d797dbd9e0822f439a758ce89835618f.jpg; soubor je v media/ v doprovodném ZIP]  diskrétní rozdělené = možné hodnoty + jejich pravděpodobnosti

## Poznámka Anki 1783851674871

Karty Anki: 1783851674871
GUID: hRFg+z!.r^; štítky: konsolidace::blok_2 nahodne_veliciny::diskretni.

### Otázka (Front)

Jak vypadá rozdělení počtu hlav při dvou hodech mincí a proč diskretnost nezávisí na povaze Ω?

### Odpověď (Back)

Je-li X počet hlav při dvou hodech férovou mincí, pak P(X=0)=1/4, P(X=1)=1/2, P(X=2)=1/4. Jeho CDF je 0 pro x<0; 1/4 pro 0≤x<1; 3/4 pro 1≤x<2; 1 pro x≥2.

Diskretnost se týká **hodnot X**, ne celého prostoru Ω. I na spojitém prostoru může být X diskrétní, například bodové skóre při zásahu šipkou do různých pásem terče.

## Poznámka Anki 1783851674872

Karty Anki: 1783851674872
GUID: BBX:TPmWA~; štítky: konsolidace::blok_2 rozdeleni::diskretni_prehled.

### Otázka (Front)

Co modelují Bernoulliho, binomické, geometrické a Poissonovo rozdělení?

### Odpověď (Back)

• **Bernoulli Be(p)**: jeden pokus, P(X=1)=p, P(X=0)=1−p.
• **Binom(n,p)**: počet úspěchů v n nezávislých Bernoulliho pokusech; P(X=k)=C(n,k)p^k(1−p)^{n−k}.
• **Geom(p)**: počet pokusů do prvního úspěchu; P(X=k)=(1−p)^{k−1}p, k=1,2,…
• **Poisson(λ)**: počet výskytů událostí v daném rámci; P(X=k)=e^{−λ}λ^k/k!, k=0,1,…

## Poznámka Anki 1783851674873

Karty Anki: 1783851674873
GUID: F~AbzWZffn; štítky: konsolidace::blok_2 nahodne_veliciny::spojite.

### Otázka (Front)

Co je absolutně spojitá náhodná veličina a jak spolu souvisejí její hustota a distribuční funkce?

### Odpověď (Back)

Absolutně spojitá X má nezápornou hustotu f_X takovou, že **F_X(x)=∫_{−∞}^{x}f_X(t)dt**. Hustota splňuje ∫_{−∞}^{∞}f_X(x)dx=1 a v bodech diferencovatelnosti F_X platí f_X(x)=F′_X(x). Distribuční funkce je proto spojitá.

Spojitý model je vhodný pro veličiny jako čas, vzdálenost či souřadnice. Jednotlivým bodům nelze přidělit kladné pravděpodobnosti tak, aby se nesčetně mnoho hodnot normalizovalo na 1; pravděpodobnost se proto rozděluje pomocí plochy pod hustotou.

## Poznámka Anki 1783851674874

Karty Anki: 1783851674874
GUID: k*#AO][]95; štítky: konsolidace::blok_2 nahodne_veliciny::spojite.

### Otázka (Front)

Jak se u spojité náhodné veličiny počítají pravděpodobnosti a jak se interpretuje hustota?

### Odpověď (Back)

Pro absolutně spojitou X platí P(X=x)=0 pro každý bod x a pro borelovskou množinu B:
**P(X∈B)=∫_B f_X(t)dt.**
Zvlášť P(a<X≤b)=∫_a^b f_X(t)dt=F_X(b)−F_X(a). Proto nezáleží na ostrých či neostrých krajích intervalu: všechny čtyři varianty mají stejnou pravděpodobnost.

Hustota f_X(x) není bodová pravděpodobnost. Pro malé Δx platí P(x<X<x+Δx)≈f_X(x)Δx; vyjadřuje tedy lokální koncentraci pravděpodobnosti.

## Poznámka Anki 1783851674875

Karty Anki: 1783851674875
GUID: v_lX40kb!b; štítky: konsolidace::blok_2 nahodne_veliciny::srovnani.

### Otázka (Front)

Jak se liší diskrétní pravděpodobnostní funkce od spojité hustoty a co mají oba případy společné?

### Odpověď (Back)

U diskrétní veličiny je p_X(x)=P(X=x) skutečná pravděpodobnost bodu a CDF je schodovitá; její skoky jsou bodové pravděpodobnosti. U absolutně spojité veličiny je P(X=x)=0 a f_X(x) je hustota, jejíž integrál přes oblast dává pravděpodobnost; CDF je spojitá.

V obou případech platí **F_X(x)=P(X≤x)** a distribuční funkce úplně určuje rozdělení.

## Poznámka Anki 1783851674876

Karty Anki: 1783851674876
GUID: v}4Po)7KA;; štítky: konsolidace::blok_2 nahodne_veliciny::spojite_priklady.

### Otázka (Front)

Jaké jsou základní příklady rovnoměrné a trojúhelníkové hustoty na [0,1] a co ukazují?

### Odpověď (Back)

Pro Romeův rovnoměrný příchod je f_X(x)=1 na [0,1] a 0 jinde; konstanta je 1, protože celková plocha musí být 1. Proto P(1/4≤X≤3/4)=1/2.

Pro Julii je trojúhelníková hustota f_Y(y)=4y na [0,1/2] a 4−4y na [1/2,1]. Pak P(1/4≤Y≤3/4)=3/4.

Čistý geometrický poměr ploch funguje jen při rovnoměrném rozdělení. U nerovnoměrné hustoty se oblasti musí vážit integrálem hustoty.

## Poznámka Anki 1783851674877

Karty Anki: 1783851674877
GUID: ADq_[O~H=<; štítky: konsolidace::blok_2 nahodne_veliciny::transformace.

### Otázka (Front)

Co znamená transformace Y=g(X), kdy je opět náhodnou veličinou a jak se obecně hledá její rozdělení?

### Odpověď (Back)

Transformace je veličina **Y(ω)=g(X(ω))**; používá se například pro převod jednotek, např. Y=1.8X+32 při převodu °C na °F, nebo pro nelineární odvozené veličiny.

Je-li g borelovsky měřitelná, pak Y je náhodná veličina a **F_Y(y)=P(g(X)≤y)**. Pro diskrétní X je Y vždy diskrétní. Pro spojité X může být Y diskrétní, spojitá nebo smíšená podle funkce g.

## Poznámka Anki 1783851674878

Karty Anki: 1783851674878
GUID: H6>d=Lgc&r; štítky: konsolidace::blok_2 nahodne_veliciny::transformace.

### Otázka (Front)

Jak se počítá rozdělení diskrétní transformace Y=g(X)?

### Odpověď (Back)

Pro každou hodnotu y se sečtou pravděpodobnosti všech hodnot x_k, které se na y zobrazí:
**P(Y=y)=Σ_{k:g(x_k)=y}P(X=x_k).**
Důvodem je, že {Y=y} je disjunktní sjednocení jevů {X=x_k} se stejným obrazem.

Příklad: X nabývá −3,−1,0,1,3 s pravděpodobnostmi 0.2,0.2,0.45,0.05,0.1 a Y=X². Potom P(Y=0)=0.45, P(Y=1)=0.2+0.05=0.25 a P(Y=9)=0.2+0.1=0.30.

## Poznámka Anki 1783851674879

Karty Anki: 1783851674879
GUID: tPeQ4/QLFL; štítky: konsolidace::blok_2 nahodne_veliciny::transformace.

### Otázka (Front)

Jak se transformuje distribuční funkce a hustota při ryze monotónní transformaci Y=g(X)?

### Odpověď (Back)

Je-li g rostoucí a invertibilní, pak **F_Y(y)=F_X(g^{-1}(y))**. Je-li navíc X absolutně spojitá a g diferencovatelná a ryze monotónní, pak
**f_Y(y)=f_X(g^{-1}(y))·|(g^{-1})′(y)|**
na obrazu podpory X. Absolutní hodnota je nutná i pro klesající transformace.

## Poznámka Anki 1783851674880

Karty Anki: 1783851674880
GUID: z^mlwg42Y!; štítky: konsolidace::blok_2 nahodne_veliciny::kvantily.

### Otázka (Front)

Co je α-kvantil a kdy je kvantilová funkce klasickou inverzí distribuční funkce?

### Odpověď (Back)

Pro α∈(0,1) je **q_α=inf{x:F_X(x)≥α}**. Je to nejmenší hodnota, pod níž leží alespoň podíl α rozdělení. Kvantilová funkce α↦F_X^{-1}(α) převádí pravděpodobnostní hladinu na hodnotu veličiny.

Je-li F_X spojitá a ryze rostoucí, je kvantilová funkce její běžnou inverzí a platí F_X(q_α)=P(X≤q_α)=α.

## Poznámka Anki 1783851674881

Karty Anki: 1783851674881
GUID: u#._~932}h; štítky: konsolidace::blok_2 simulace::inverzni_transformace.

### Otázka (Front)

Jak funguje metoda inverzní transformace pro simulaci rozdělení?

### Odpověď (Back)

Vygenerujeme U∼Unif(0,1) a položíme **X=F_X^{-1}(U)**. Potom X má distribuční funkci F_X, protože při spojité rostoucí F_X:
P(F_X^{-1}(U)≤x)=P(U≤F_X(x))=F_X(x).

Tím se propojí hustota → distribuční funkce → kvantilová funkce → simulace. Pro férovou šestistěnnou kostku lze použít X=⌊6U⌋+1 pro U∈[0,1); ekvivalentně X=⌈6U⌉ téměř jistě. Interval [0,1] se rozdělí na šest stejně dlouhých částí.

## Poznámka Anki 1783851674882

Karty Anki: 1783851674882
GUID: yEF)-!oV5P; štítky: konsolidace::blok_2 simulace::generator.

### Otázka (Front)

Co jsou pseudonáhodná čísla a jak funguje lineární kongruentní generátor?

### Odpověď (Back)

Pseudonáhodná čísla vytváří deterministický algoritmus tak, aby jejich posloupnost statisticky připomínala náhodné hodnoty. Lineární kongruentní generátor volí a,b,m a seed X₀ a iteruje
**X_{n+1}=(aX_n+b) mod m**;
dělením m získá hodnoty v [0,1). Sofistikovanější zmíněné generátory jsou Mersenne Twister a Wichmann–Hill.

## Poznámka Anki 1783851674883

Karty Anki: 1783851674883
GUID: M>40_2alp~; štítky: charakteristiky::stredni_hodnota konsolidace::blok_2.

### Otázka (Front)

Jak se definuje a interpretuje střední hodnota diskrétní a spojité náhodné veličiny?

### Odpověď (Back)

Střední hodnota je charakteristika polohy: vážený průměr možných hodnot a rovnovážný bod rozdělení.

Diskrétní případ: **E[X]=Σ_k x_kP(X=x_k)**.
Spojitý případ: **E[X]=∫_{−∞}^{∞}x f_X(x)dx**.
Konečná střední hodnota existuje, když příslušná suma či integrál absolutně konverguje, tj. E[|X|]<∞; jinak nemusí být konečná nebo dobře definovaná.

## Poznámka Anki 1783851674884

Karty Anki: 1783851674884
GUID: x@?/5fOAEz; štítky: charakteristiky::stredni_hodnota konsolidace::blok_2.

### Otázka (Front)

Jaké jsou základní příklady střední hodnoty a proč ji nelze zaměňovat s modem?

### Odpověď (Back)

• počet hlav ve dvou férových hodech: E[X]=0·1/4+1·1/2+2·1/4=1;
• férová šestistěnná kostka: E[X]=(1+⋯+6)/6=3.5;
• maximum dvou férových šestistěnných kostek: E[X]=161/36≈4.47.

Střední hodnota je vážený průměr celého rozdělení; **modus** je nejpravděpodobnější hodnota. Obecně se nemusí shodovat a střední hodnota ani nemusí být možnou realizací.

## Poznámka Anki 1783851674885

Karty Anki: 1783851674885
GUID: n$=[7M.Xv}; štítky: charakteristiky::stredni_hodnota konsolidace::blok_2.

### Otázka (Front)

Jak se počítá E[g(X)] bez určování celého rozdělení Y=g(X)?

### Odpověď (Back)

Použije se zákon nevědomého statistika (LOTUS):
• diskrétní X: **E[g(X)]=Σ_k g(x_k)P(X=x_k)**;
• absolutně spojitá X: **E[g(X)]=∫_{−∞}^{∞}g(x)f_X(x)dx**.

Transformace může výrazně změnit rozdělení Y, ale pro její očekávání často stačí přímo rozdělení X; není nutné nejprve hledat p_Y nebo f_Y.

## Poznámka Anki 1783851674886

Karty Anki: 1783851674886
GUID: oH;$>H8)`<; štítky: charakteristiky::stredni_hodnota konsolidace::blok_2.

### Otázka (Front)

Jak lze vyjádřit střední hodnotu nezáporné veličiny pomocí funkce přežívání?

### Odpověď (Back)

Pro X≥0 platí **E[X]=∫_0^∞P(X>t)dt=∫_0^∞[1−F_X(t)]dt**, případně v rozšířeném smyslu i s hodnotou ∞. Střední hodnota je tedy plocha pod funkcí přežívání t↦P(X>t): sčítá příspěvky pravděpodobností, že X překročí jednotlivé prahy.

## Poznámka Anki 1783851674887

Karty Anki: 1783851674887
GUID: JT#BMVeiRK; štítky: charakteristiky::stredni_hodnota konsolidace::blok_2.

### Otázka (Front)

Jaké základní algebraické a pořádkové vlastnosti má střední hodnota?

### Odpověď (Back)

Pro veličiny s konečnými středními hodnotami platí:
• E[c]=c pro konstantu c;
• X≥0 ⇒ E[X]≥0;
• **E[aX+bY]=aE[X]+bE[Y]**, a to bez požadavku nezávislosti;
• zvlášť E[aX+b]=aE[X]+b.

## Poznámka Anki 1783851674888

Karty Anki: 1783851674888
GUID: iM}l]`aaI); štítky: charakteristiky::rozptyl konsolidace::blok_2.

### Otázka (Front)

Co jsou rozptyl a směrodatná odchylka a jak se interpretují?

### Odpověď (Back)

**var(X)=E[(X−E[X])²]** měří průměrnou čtvercovou vzdálenost hodnot od střední hodnoty, tedy šířku rozdělení. **sd(X)=√var(X)**.

Rozptyl má jednotky původní veličiny na druhou; směrodatná odchylka má stejné jednotky jako X, a proto se interpretuje přirozeněji.

## Poznámka Anki 1783851674889

Karty Anki: 1783851674889
GUID: m0I4<T87g%; štítky: charakteristiky::rozptyl konsolidace::blok_2.

### Otázka (Front)

Jak se rozptyl prakticky počítá a jak se chová při afinní transformaci?

### Odpověď (Back)

Výpočetní vzorec je **var(X)=E[X²]−(E[X])²**; bývá jednodušší než přímé E[(X−E[X])²]. Rozptyl je vždy nezáporný, a proto (E[X])²≤E[X²].

Pro a,b∈ℝ platí **var(aX+b)=a²var(X)**. Posun b rozptyl nemění, násobení a jej násobí a² a var(c)=0 pro konstantu.

## Poznámka Anki 1783851674890

Karty Anki: 1783851674890
GUID: N2f/De_<T9; štítky: charakteristiky::rozptyl konsolidace::blok_2.

### Otázka (Front)

Jaké jsou střední hodnoty a rozptyly rovnoměrného a trojúhelníkového rozdělení na [0,1]?

### Odpověď (Back)

Pro X∼Unif(0,1): **E[X]=1/2, var(X)=1/12**.
Pro symetrické trojúhelníkové rozdělení Julie s hustotou 4y na [0,1/2] a 4−4y na [1/2,1]: **E[Y]=1/2, var(Y)=1/24**.

Obě rozdělení mají stejnou polohu, ale Julie má poloviční rozptyl, takže její příchody jsou více soustředěné kolem středu.

## Poznámka Anki 1783851674891

Karty Anki: 1783851674891
GUID: d)oF@s5Bmg; štítky: charakteristiky::momenty konsolidace::blok_2.

### Otázka (Front)

Co jsou momenty a centrální momenty a jak souvisejí se střední hodnotou, rozptylem a směrodatnou odchylkou?

### Odpověď (Back)

k-tý moment je **μ_k=E[X^k]**; k-tý centrální moment je **σ_k=E[(X−E[X])^k]**. Platí μ₁=E[X] a σ₂=var(X); směrodatná odchylka je √σ₂ a má stejné jednotky jako X.

Momenty nemusí existovat: příslušná suma nebo integrál může divergovat či být nekonečná.

## Poznámka Anki 1783851674892

Karty Anki: 1783851674892
GUID: F.5!:5~-0^; štítky: charakteristiky::momenty konsolidace::blok_2.

### Otázka (Front)

Jak se definují a interpretují koeficient šikmosti a excess kurtosis?

### Odpověď (Back)

Šikmost je **γ₁=E[(X−E[X])³]/var(X)^{3/2}**. γ₁>0 značí delší či těžší pravý chvost, γ₁<0 levý chvost.

Excess kurtosis je **γ₂=E[(X−E[X])⁴]/var(X)²−3**. Normální rozdělení má γ₂=0; kladná hodnota obvykle souvisí s těžšími chvosty a větším výskytem extrémů, záporná s lehčími chvosty. Tradiční název „špičatost“ je zjednodušující.

## Poznámka Anki 1783851674893

Karty Anki: 1783851674893
GUID: rSqTB|/Wzq; štítky: charakteristiky::mgf konsolidace::blok_2.

### Otázka (Front)

Co je momentová vytvořující funkce a jak z ní získáme momenty?

### Odpověď (Back)

Momentová vytvořující funkce je **M_X(s)=E[e^{sX}]**. Diskrétně M_X(s)=Σ_k e^{sx_k}P(X=x_k), spojitě M_X(s)=∫e^{sx}f_X(x)dx.

Existuje-li v okolí s=0, jednoznačně určuje rozdělení a **M_X^{(k)}(0)=E[X^k]**. Tedy E[X]=M′_X(0), E[X²]=M″_X(0) a var(X)=M″_X(0)−(M′_X(0))². MGF tak sjednocuje výpočet momentů; rozptyl je druhý centrální moment.

## Poznámka Anki 1783851674894

Karty Anki: 1783851674894
GUID: jrv0G^Ati(; štítky: charakteristiky::mgf konsolidace::blok_2.

### Otázka (Front)

Jaké jsou MGF, střední hodnota a rozptyl Poissonova a exponenciálního rozdělení?

### Odpověď (Back)

Pro X∼Poisson(λ): **M_X(s)=exp(λ(e^s−1))**, E[X]=λ, var(X)=λ.

Pro X∼Exp(λ): **M_X(s)=λ/(λ−s)** pro s<λ, E[X]=1/λ, var(X)=1/λ².

## Poznámka Anki 1783851674895

Karty Anki: 1783851674895
GUID: yV*kcUf)dv; štítky: charakteristiky::kvantily konsolidace::blok_2.

### Otázka (Front)

Jak souvisejí kvantily, kritické hodnoty, kvartily a kvantilová funkce rovnoměrného rozdělení?

### Odpověď (Back)

α-kvantil je q_α=inf{x:F_X(x)≥α}. **α-kritická hodnota** je c_α=q_{1−α}. Speciálně q_{0.25} je dolní kvartil, q_{0.5} medián a q_{0.75} horní kvartil.

Při spojité ryze rostoucí F je q_α=F^{-1}(α). Pro Unif(0,1) platí jednoduše **q_α=α**.

## Poznámka Anki 1783851674896

Karty Anki: 1783851674896
GUID: NC7rcvHI?(; štítky: charakteristiky::kvantily konsolidace::blok_2.

### Otázka (Front)

Co ukazují 5% a 95% kvantily v příkladu příchodů Romea a Julie?

### Odpověď (Back)

Romeo má Unif(0,1): q_{0.05}=0.05=3 minuty a q_{0.95}=0.95=57 minut. Julie má trojúhelníkové rozdělení: přibližně q_{0.05}=0.16=9.5 minuty a q_{0.95}=0.84=50.5 minuty.

Juliin centrální 90% interval je užší, což odpovídá jejímu menšímu rozptylu a větší koncentraci kolem středu.

## Poznámka Anki 1783851674897

Karty Anki: 1783851674897
GUID: L.^M:GTni|; štítky: charakteristiky::kvantily konsolidace::blok_2.

### Otázka (Front)

Jak se liší střední hodnota, medián a interkvartilové rozpětí a kdy jsou kvantilové charakteristiky užitečnější?

### Odpověď (Back)

Střední hodnota je vážený průměr a je citlivá na asymetrii a extrémy. Medián q_{0.5} dělí rozdělení na dvě poloviny a je robustnější. **IQR=q_{0.75}−q_{0.25}** měří šířku prostředních 50 % a je robustnější alternativou k rozptylu.

U pravostranně asymetrických příjmů několik velmi vysokých hodnot zvyšuje průměr nad medián; proto může mít většina populace příjem pod průměrem. Kvantily tak doplňují momentové charakteristiky polohy a disperze.

## Poznámka Anki 1783851674898

Karty Anki: 1783851674898
GUID: DBt{.TQVen; štítky: konsolidace::blok_2 rozdeleni::konstantni.

### Otázka (Front)

Jaké rozdělení, distribuční funkci, střední hodnotu a rozptyl má konstantní náhodná veličina?

### Odpověď (Back)

Je-li X(ω)=c pro všechna ω, jde o degenerované rozdělení: P(X=c)=1 a P(X=x)=0 pro x≠c. Distribuční funkce je F_X(x)=0 pro x<c a F_X(x)=1 pro x≥c. Platí **E[X]=c** a **var(X)=0**.

## Poznámka Anki 1783851674899

Karty Anki: 1783851674899
GUID: C1l{~rFX6C; štítky: konsolidace::blok_2 rozdeleni::bernoulli.

### Otázka (Front)

Jak je definováno Bernoulliho rozdělení a jaké má střední hodnotu a rozptyl?

### Odpověď (Back)

Bernoulliho veličina modeluje jeden pokus se dvěma výsledky, obvykle úspěch 1 a neúspěch 0. Značí se X∼Be(p), Bernoulli(p) nebo Alt(p) a platí P(X=1)=p, P(X=0)=1−p, p∈[0,1]. U mince lze hlavě přiřadit 1 a orlu 0.

Protože X²=X, je E[X]=E[X²]=p a **var(X)=p−p²=p(1−p)**. Jde o výchozí model pro další důležitá diskrétní rozdělení.

