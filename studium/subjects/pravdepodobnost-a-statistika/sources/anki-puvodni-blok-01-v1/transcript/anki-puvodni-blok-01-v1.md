# Pravděpodobnost a statistika – Původní blok 01

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::Pravděpodobnost a statistika
Rozsah: 22 poznámek, 22 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783851674841

Karty Anki: 1783851674841
GUID: iHV_c`y=DQ; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jak se liší teorie pravděpodobnosti od matematické statistiky a jaký mají společný cíl?

### Odpověď (Back)

**Teorie pravděpodobnosti** vychází ze zadaného modelu náhody a odvozuje pravděpodobnosti výsledků. **Matematická statistika** postupuje opačně: z pozorovaných dat odhaduje a ověřuje pravděpodobnostní model. Společným cílem je popsat situace, v nichž nelze konkrétní výsledek předem určit kvůli náhodě, složitosti nebo neúplné informaci.

## Poznámka Anki 1783851674842

Karty Anki: 1783851674842
GUID: ex(Pg(L=mJ; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jak funguje klasická definice pravděpodobnosti, kdy platí a jaké jsou typické příklady?

### Odpověď (Back)

Je-li konečný prostor tvořen **n stejně pravděpodobnými výsledky** a jev A obsahuje m z nich, pak P(A)=m/n. Vyžaduje konečný počet možností a jejich rovnoměrnost; selhává u nerovnoměrných, nekonečných či nespočetných prostorů.

Příklady: dvě férové mince → P(alespoň jedna hlava)=3/4; férová šestistěnná kostka → P(sudé číslo)=3/6=1/2.

## Poznámka Anki 1783851674843

Karty Anki: 1783851674843
GUID: tnl1nTjNbY; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jak se definuje geometrická pravděpodobnost a jaké má předpoklady a omezení?

### Odpověď (Back)

Má-li Ω konečnou geometrickou míru μ a výběr je rovnoměrný vzhledem k této míře, pak P(A)=μ(A)/μ(Ω). Stejně velké oblasti tedy musí být stejně pravděpodobné. Definice neřeší nerovnoměrné rozdělení ani prostor s nekonečnou celkovou mírou. Konečná rovnoměrná i geometrická konstrukce splňují nezápornost, normalizaci a aditivitu, a proto určují pravděpodobnostní míru.

## Poznámka Anki 1783851674844

Karty Anki: 1783851674844
GUID: uAp%cK1ik1; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Co je pravděpodobnostní prostor?

### Odpověď (Back)

Pravděpodobnostní prostor je trojice (Ω,F,P): Ω je prostor elementárních výsledků, F je σ-algebra měřitelných jevů a P:F→[0,1] je pravděpodobnostní míra.

## Poznámka Anki 1783851674845

Karty Anki: 1783851674845
GUID: k2Ah]rTb]Q; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Co je výběrový prostor Ω a jak se volí pro jednoduché, opakované a nekonečné experimenty?

### Odpověď (Back)

Ω je množina všech možných elementárních výsledků ω. Výsledky musí být **vzájemně exkluzivní** (jeden realizovaný výsledek nepatří dvěma elementárním jevům) a **vyčerpávající** (každý možný výsledek je zahrnut).

Příklady: mince {H,O}; kostka {1,…,6}; dva hody mincí {H,O}²; nekonečné hody {H,O}^N. U n hodů kostkou lze modelovat buď uspořádanou posloupnost v {1,…,6}^n, nebo jen vektor četností (n₁,…,n₆) se součtem n; druhý model ztrácí pořadí a jeho výsledky nejsou obecně stejně pravděpodobné.

## Poznámka Anki 1783851674846

Karty Anki: 1783851674846
GUID: l_-a^Ons{#; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jak se náhodné jevy vyjadřují množinově a co znamenají základní množinové operace?

### Odpověď (Back)

Jev A je měřitelná podmnožina Ω. A^c: A nenastane; A∩B: nastanou oba; A∪B: nastane alespoň jeden; A\B: nastane A, ale ne B; A⊂B: z A plyne B. ∅ je nemožný a Ω jistý jev.

Příklady: při dvou hodech mincí „alespoň jedna hlava“ = {(H,H),(H,O),(O,H)}; při hodu kostkou „sudé“ = {2,4,6}.

## Poznámka Anki 1783851674847

Karty Anki: 1783851674847
GUID: Q<cHrwzv^E; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Co je σ-algebra F, proč ji potřebujeme a co je borelovská σ-algebra?

### Odpověď (Back)

V obecném, zejména nespočetném prostoru nelze každé podmnožině konzistentně přiřadit pravděpodobnost. σ-algebra F proto určuje měřitelné jevy. Obsahuje ∅, je uzavřena na doplňky a spočetná sjednocení; z toho plyne, že obsahuje Ω, spočetné průniky a další kombinace jevů. Borelovská σ-algebra na R je nejmenší σ-algebra obsahující všechny otevřené intervaly; zahrnuje běžné „rozumné“ množiny používané v pravděpodobnosti.

## Poznámka Anki 1783851674848

Karty Anki: 1783851674848
GUID: fl!J8-?b(:; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jaké axiomy splňuje pravděpodobnostní míra a proč musí být přesně určen model náhody?

### Odpověď (Back)

P:F→R splňuje: (1) P(A)≥0; (2) P(Ω)=1; (3) pro disjunktní A_i platí P(⋃A_i)=ΣP(A_i). Z axiomů plyne 0≤P(A)≤1. Volba P určuje význam slova „náhodně“; stejný slovní problém může při různých mechanismech výběru vést k různým výsledkům. Bertrandův paradox proto ukazuje, že nestačí říci „vybereme náhodně“—musí se specifikovat postup výběru.

## Poznámka Anki 1783851674849

Karty Anki: 1783851674849
GUID: jQTWP[D>Hc; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jaké základní vztahy platí pro pravděpodobnost jevů?

### Odpověď (Back)

P(∅)=0. Pro disjunktní A,B: P(A∪B)=P(A)+P(B). Obecně P(A∪B)=P(A)+P(B)−P(A∩B), protože průnik by byl započten dvakrát. Dále P(A^c)=1−P(A) a z A⊂B plyne P(A)≤P(B). Pro libovolné A_i platí σ-subaditivita P(⋃A_i)≤ΣP(A_i).

## Poznámka Anki 1783851674850

Karty Anki: 1783851674850
GUID: B:/+AR})*X; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Co říká princip inkluze–exkluze a spojitost pravděpodobnosti?

### Odpověď (Back)

Inkluze–exkluze vyjadřuje pravděpodobnost sjednocení střídavým součtem pravděpodobností průniků. Pro tři jevy:
P(A∪B∪C)=P(A)+P(B)+P(C)−P(A∩B)−P(A∩C)−P(B∩C)+P(A∩B∩C).

Je-li A₁⊂A₂⊂… a A=⋃A_n, pak P(A_n)→P(A). Je-li B₁⊃B₂⊃… a B=⋂B_n, pak P(B_n)→P(B).

## Poznámka Anki 1783851674851

Karty Anki: 1783851674851
GUID: At[pg>ejZ2; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jak spravedlivě rozdělit sázku při vedení 5:3 ve hře do 6 vítězství?

### Odpověď (Back)

Hráč B vyhraje jen tehdy, vyhraje-li všechny tři následující férové hry: pravděpodobnost 1/8. Hráč A tedy vyhraje s pravděpodobností 7/8. Sázka se rozdělí v poměru **7:1 ve prospěch A**.

## Poznámka Anki 1783851674852

Karty Anki: 1783851674852
GUID: w>+I-&_!gY; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Co je podmíněná pravděpodobnost a jak souvisí s průnikem?

### Odpověď (Back)

Pro P(B)>0 je P(A|B)=P(A∩B)/P(B). Po informaci, že nastal B, zúžíme prostor možností na B. Ekvivalentně platí násobicí pravidlo P(A∩B)=P(A|B)P(B)=P(B|A)P(A).

Příklad: při prvním hodu kostkou 3 je součet dvou hodů >6 právě pro druhý hod 4,5,6, takže podmíněná pravděpodobnost je 3/6=1/2.

## Poznámka Anki 1783851674853

Karty Anki: 1783851674853
GUID: rkL@~U/uf{; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Je P(·|B) pravděpodobnostní míra a jaké vlastnosti po podmínění zachovává?

### Odpověď (Back)

Ano, pro P(B)>0 je P(·|B) nezáporná, normalizovaná a σ-aditivní. „Žije na B“: jevy disjunktní s B mají podmíněnou pravděpodobnost 0. Platí tedy běžná pravidla, např. P(A^c|B)=1−P(A|B) a P(A₁∪A₂|B)=P(A₁|B)+P(A₂|B)−P(A₁∩A₂|B).

## Poznámka Anki 1783851674856

Karty Anki: 1783851674856
GUID: w?:n6i{|]y; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jak zní Bayesova věta, jak se odvodí a co znamenají prior, likelihood a posterior?

### Odpověď (Back)

[Obrázek: paste-eed181bc7eb35d00f9cc386e0e513b8e76e7ebcf.jpg; soubor je v media/ v doprovodném ZIP] 
 [Obrázek: paste-045036f269d14ebb0276ff03bf2058ecd3e8fc48.jpg; soubor je v media/ v doprovodném ZIP]  [Obrázek: paste-908ace039ef0a770dd77d6f93af4b63efe8ff262.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1783851674858

Karty Anki: 1783851674858
GUID: Ay#pOuyu0K; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jaký je vztah mezi průnikem, podmíněním, úplným rozkladem pravděpodobnosti a Bayesovou větou?

### Odpověď (Back)

Základ je P(A∩B)=P(A|B)P(B). Úplná pravděpodobnost tyto společné pravděpodobnosti sčítá přes disjunktní scénáře. Bayesova věta vydělí příspěvek jednoho scénáře jejich celkovým součtem a obrátí směr podmínění. Obecně P(A|B)≠P(B|A), protože mají stejný čitatel P(A∩B), ale jiné jmenovatele. Prakticky: „pravděpodobnost vady“ je úplným rozkladem pravděpodobnosti ; „pravděpodobnost dovozu při zjištěné vadě“ je Bayesova inverzní úloha a aktualizace prioru na posterior.

## Poznámka Anki 1783851674859

Karty Anki: 1783851674859
GUID: bgD6a{#OWe; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Co je pravděpodobnostní strom a co v něm představují uzly, větve a cesty?

### Odpověď (Back)

Strom graficky popisuje vícekrokový experiment. Uzly jsou průběžné stavy nebo dostupná informace, větve jsou možné další výsledky s podmíněnými pravděpodobnostmi a cesta od kořene k listu představuje jeden úplný scénář—konkrétní posloupnost dílčích výsledků.

## Poznámka Anki 1783851674860

Karty Anki: 1783851674860
GUID: v:Jv`W[_`D; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jak se počítá s pravděpodobnostním stromem a jak souvisí s úplnou pravděpodobností a Bayesem?

### Odpověď (Back)

**Po jedné cestě násobíme** pravděpodobnosti větví; **přes alternativní disjunktní cesty sčítáme**. Strom je grafickým zápisem rozkladu prostoru a věty o úplné pravděpodobnosti. Po spočtení příspěvků všech cest k pozorování lze Bayesovou větou určit zpětnou pravděpodobnost příčiny. Strom tedy sjednocuje podmínění, součin po cestě, součet přes scénáře a Bayesovskou aktualizaci.

## Poznámka Anki 1783851674861

Karty Anki: 1783851674861
GUID: hQ!cGc,,+J; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Co znamená nezávislost dvou jevů a jaké jsou její ekvivalentní formulace?

### Odpověď (Back)

A a B jsou nezávislé, jestliže **P(A∩B)=P(A)P(B)**. To vyjadřuje absenci informační vazby. Při P(B)>0 je to ekvivalentní P(A|B)=P(A); při P(A)>0 také P(B|A)=P(B). Součinová definice je základní, protože je symetrická a funguje i při nulových pravděpodobnostech. Obecně P(A∩B)=P(A|B)P(B); nezávislost je právě případ, kdy podmínění nic nezmění.

## Poznámka Anki 1783851674862

Karty Anki: 1783851674862
GUID: P4Jo)V+JS[; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jak se liší průnik, disjunktnost a nezávislost a co platí pro doplňky nezávislých jevů?

### Odpověď (Back)

A∩B je jev současného nastání. Disjunktnost znamená A∩B=∅; jestliže mají oba jevy kladnou pravděpodobnost, jsou tím pádem závislé, ne nezávislé. Disjunktní jevy mohou být nezávislé jen tehdy, má-li alespoň jeden pravděpodobnost 0. Nezávislost znamená P(A∩B)=P(A)P(B). Jsou-li A,B nezávislé, jsou nezávislé i dvojice A,B^c; A^c,B; A^c,B^c.

## Poznámka Anki 1783851674863

Karty Anki: 1783851674863
GUID: FL]TSXaF6n; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jak se nezávislost používá v opakovaných experimentech a jak se projeví ve stromu?

### Odpověď (Back)

U nezávislých pokusů se pravděpodobnosti společného výsledku násobí. Dvě hlavy: (1/2)²=1/4. Nejprve sudé číslo a potom číslo >4 při dvou hodech kostkou: (1/2)·(2/6)=1/6. Ve stromu se nezávislost projeví tím, že pravděpodobnosti na další úrovni nezávisí na předchozí větvi—podmíněné pravděpodobnosti jsou stejné jako nepodmíněné.

## Poznámka Anki 1783851674864

Karty Anki: 1783851674864
GUID: ly<yAev0#%; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jaký je rozdíl mezi párovou a vzájemnou nezávislostí více jevů?

### Odpověď (Back)

Párová nezávislost vyžaduje nezávislost každé dvojice. Vzájemná nezávislost je silnější: pro každou neprázdnou množinu indexů I⊂{1,…,n} musí platit
**P(⋂_{i∈I} A_i)=∏_{i∈I}P(A_i).**
Párová nezávislost nekontroluje průniky tří a více jevů, a proto sama nestačí.

## Poznámka Anki 1783851674865

Karty Anki: 1783851674865
GUID: sxv4,uhu~T; štítky: konsolidace::blok_1 pravdepodobnost::zaklady.

### Otázka (Front)

Jak se ověřuje a interpretuje závislost jevů v konečném prostoru?

### Odpověď (Back)

Nezávislost generujících experimentů je vlastnost modelu; nezávislost konkrétních odvozených jevů je nutné ověřit. Spočítáme P(A), P(B), P(A∩B) a porovnáme průnik se součinem. Rovnost znamená nezávislost; P(A∩B)>P(A)P(B) pozitivní asociaci; P(A∩B)

