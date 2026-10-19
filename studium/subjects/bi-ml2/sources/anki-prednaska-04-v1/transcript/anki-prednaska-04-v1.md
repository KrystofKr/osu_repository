# BI-ML2 – Přednáška 04

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291445

Karty Anki: 1785306291446
GUID: <yzH`r68nN; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Jak se pomocí matic V a U rozloží prostor, bod a jeho energie na ortogonální podprostory?

### Odpověď (Back)

V∈ℝ<sup>p×q</sup> obsahuje ortonormální bázi podprostoru V a U∈ℝ<sup>p×(p−q)</sup> ortonormální bázi V<sup>⊥</sup>. Projekční matice jsou VVᵀ a UUᵀ a splňují VVᵀ+UUᵀ=I<sub>p</sub>.

Každý bod se rozloží jako x=VVᵀx+UUᵀx=vₓ+uₓ, kde vₓ∈V a uₓ∈V<sup>⊥</sup>. Proto ‖x‖²=‖vₓ‖²+‖uₓ‖². Pro souřadnice tₓ=Vᵀx platí vₓ=Vtₓ a ‖vₓ‖=‖tₓ‖, protože VᵀV=I<sub>q</sub>.

## Poznámka Anki 1785306291447

Karty Anki: 1785306291448
GUID: blRx8%F6hK; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Proč PCA data středuje a jak souvisejí rekonstrukční chyba a zachycený rozptyl?

### Odpověď (Back)

Středovaný bod je xᵢ′=xᵢ−x̄, kde x̄=(1/N)Σᵢxᵢ; X′ vznikne odečtením x̄ᵀ od každého řádku X. PCA hledá lineární podprostor pro X′, což v původních souřadnicích znamená afinní podprostor procházející průměrem. Rekonstrukce je x̂=x̄+VVᵀ(x−x̄).

PCA volí q-rozměrný V minimalizující Σᵢ‖xᵢ′−VVᵀxᵢ′‖² = Σᵢ‖UUᵀxᵢ′‖². Průměr je optimální poloha afinního podprostoru, protože minimalizuje součet čtvercových vzdáleností k centru; po středování mají průměr i průměr kolmých reziduí hodnotu 0.

Z Pythagorovy věty
Σᵢ‖xᵢ′‖² = Σᵢ‖VVᵀxᵢ′‖² + Σᵢ‖(I−VVᵀ)xᵢ′‖².
Celková energie dat je konstantní, proto minimalizace rekonstrukční chyby přesně odpovídá maximalizaci energie neboli rozptylu projekcí.

## Poznámka Anki 1785306291449

Karty Anki: 1785306291450
GUID: f*GfVRrsRD; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Jaké vlastnosti má kovarianční matice a jak z ní PCA získá optimální podprostor?

### Odpověď (Back)

Výběrová kovarianční matice středovaných dat je S=X′ᵀX′/(N−1). Prvek Sᵢⱼ je kovariance příznaků i,j a diagonála obsahuje jejich rozptyly.

S je symetrická a pozitivně semidefinitní, protože aᵀSa=‖X′a‖²/(N−1)≥0. Má proto reálná nezáporná vlastní čísla a ortonormální bázi vlastních vektorů. Seřadíme λ₁≥λ₂≥…≥λ<sub>p</sub>≥0; optimální q-rozměrný PCA podprostor má v matici V vlastní vektory b₁,…,b<sub>q</sub> odpovídající q největším vlastním číslům.

## Poznámka Anki 1785306291451

Karty Anki: 1785306291452
GUID: v9p~?-F/fb; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Jaký optimalizační význam mají hlavní směry, vlastní čísla a spektrální mezera v PCA?

### Odpověď (Back)

První hlavní směr b₁ je jednotkový vektor maximalizující výběrový rozptyl projekce bᵀX′. Pro jednotkový b je tento rozptyl bᵀSb a Rayleighův podíl dosahuje maxima λ₁ ve vlastním směru největšího vlastního čísla. Každý další směr maximalizuje rozptyl při jednotkové normě a ortogonalitě k předchozím.

Prvních q komponent zachytí rozptyl Σᵢ₌₁<sup>q</sup>λᵢ, respektive součet čtverců (N−1)Σᵢ₌₁<sup>q</sup>λᵢ. Minimální celková rekonstrukční chyba je (N−1)Σᵢ₌q₊₁<sup>p</sup>λᵢ. Výběr největších vlastních čísel tedy současně maximalizuje zachycený rozptyl a minimalizuje zahozený.

Hlavní q-rozměrný podprostor je jednoznačný, pokud λ<sub>q</sub>>λ<sub>q+1</sub>. Při shodných vlastních číslech lze v odpovídajícím vlastním podprostoru volit různé ortonormální báze.

## Poznámka Anki 1785306291453

Karty Anki: 1785306291454
GUID: SH?.Ds,G<d; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Co jsou hlavní komponenty, loadings a skóre a jaké mají statistické vlastnosti?

### Odpověď (Back)

i-tá hlavní komponenta jako náhodná veličina je Tᵢ=bᵢᵀX′. Pro dataset je skórová matice T<sub>q</sub>=X′V: její řádky jsou souřadnice pozorování a sloupce hodnoty jednotlivých komponent. **Loadings/směry** jsou sloupce V v původním příznakovém prostoru; **skóre** jsou souřadnice v T<sub>q</sub>.

Po středování má každá komponenta nulový výběrový průměr. Pro všech p komponent platí cov(T<sub>p</sub>)=T<sub>p</sub>ᵀT<sub>p</sub>/(N−1)=Λ. Rozptyl i-té komponenty je λᵢ a kovariance různých komponent je 0, takže jsou výběrově nekorelované.

Nekorelovanost obecně neznamená statistickou nezávislost; ta z nulové kovariance plyne jen pro zvláštní případy, například společně normální rozdělení.

## Poznámka Anki 1785306291455

Karty Anki: 1785306291456
GUID: rnl.+WEDzG; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Jak PCA měří vysvětlený rozptyl a co platí při zachování všech komponent?

### Odpověď (Back)

Podíl rozptylu vysvětlený komponentou i je λᵢ/Σⱼλⱼ a kumulativní podíl prvních q komponent je (Σᵢ₌₁<sup>q</sup>λᵢ)/(Σⱼ₌₁<sup>p</sup>λⱼ). Celkový rozptyl je trace(S)=Σⱼλⱼ, tedy součet rozptylů původních příznaků i hlavních komponent. Nevysvětlený podíl a rekonstrukční chyba jsou určeny zahozenými λ<sub>q+1</sub>,…,λ<sub>p</sub>.

Pro q=p nedochází k redukci ani ztrátě informace; data se jen vyjádří v nové ortonormální bázi. Sloupce T<sub>p</sub> jsou navzájem ortogonální, protože T<sub>p</sub>ᵀT<sub>p</sub>=(N−1)Λ je diagonální. Znaménko směru není jednoznačné: bᵢ a −bᵢ určují stejný směr a pouze obrátí znaménko skóre.

## Poznámka Anki 1785306291457

Karty Anki: 1785306291458
GUID: Qgt`~Q)__x; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Jak se volí počet komponent PCA a jak se PCA počítá spektrálním rozkladem nebo SVD?

### Odpověď (Back)

**Volba q:** v elbow grafu kumulativně vysvětleného rozptylu se hledá bod, za nímž další komponenty přidávají málo; alternativně se vezme nejmenší q dosahující předem stanoveného podílu rozptylu.

**Spektrální výpočet:** vytvořit S=X′ᵀX′/(N−1), rozložit ji a vlastní vektory seřadit podle vlastních čísel.
**SVD:** pro X′=UΣVᵀ jsou pravé singulární vektory ve V hlavní směry, λᵢ=σᵢ²/(N−1) a skóre všech komponent X′V=UΣ. SVD se vyhne explicitnímu součinu X′ᵀX′ a bývá numericky stabilnější.

Středovaný dataset má nejvýše min(p,N−1) nenulových hlavních komponent, protože středování sníží hodnost X′ alespoň o jedna.

## Poznámka Anki 1785306291459

Karty Anki: 1785306291460
GUID: D=[D@bAOZo; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Co mohou ukázat první komponenty PCA a jaká jsou hlavní omezení PCA?

### Odpověď (Back)

Promítnutí MNIST do prvních dvou komponent může odhalit část shlukové struktury a překryvů tříd, ale třídy nemusí dokonale oddělit. Interpretace obrazových komponent je obtížná, protože každá je globální lineární kombinací mnoha pixelů a maximální rozptyl nemusí odpovídat pojmenovatelnému sémantickému faktoru.

PCA zachycuje jen globální lineární směry. Švýcarskou rolku proto správně nerozvine do jejích dvou vnitřních souřadnic a jediným nízkodimenzionálním podprostorem obecně nevystihne silně nelineární závislosti ani zakřivené variety.

## Poznámka Anki 1785306291461

Karty Anki: 1785306291462
GUID: 2:vc@kkgOM; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Jak probíhá první fáze LLE a jaké vlastnosti mají její lokální rekonstrukční váhy?

### Odpověď (Back)

LLE předpokládá, že varietu lze v malém okolí aproximovat lineárním či afinním prostorem. Pro každý xᵢ najde k nejbližších sousedů (bez xᵢ) a hledá váhy wᵢⱼ minimalizující Σᵢ‖xᵢ−Σⱼwᵢⱼxⱼ‖².

Platí wᵢⱼ=0 mimo sousedy a Σⱼwᵢⱼ=1; váhy nemusejí být nezáporné. Maticově se minimalizuje ‖X−WX‖<sub>F</sub>²=‖(I−W)X‖<sub>F</sub>² při W1=1. W je řídká, protože každý řádek má nenulové prvky jen u k sousedů.

Afinní podmínka zajišťuje invarianci vůči společnému posunu: po xⱼ→xⱼ+c se bod i jeho rekonstrukce posunou o stejné c, takže reziduum zůstane.

## Poznámka Anki 1785306291463

Karty Anki: 1785306291464
GUID: K$71QiUVkA; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Jak probíhá druhá fáze LLE a proč se vnoření získává z netriviálních vlastních vektorů?

### Odpověď (Back)

LLE při přechodu do nižší dimenze zachovává optimální lokální váhy W*, nikoli nutně globální eukleidovské vzdálenosti. Hledá body zᵢ minimalizující Σᵢ‖zᵢ−Σⱼw*ᵢⱼzⱼ‖², maticově ‖(I−W*)Z‖<sub>F</sub>².

Bez omezení je úloha degenerovaná: konstantní Z, například 0, má nulovou chybu, protože W*1=1. Proto se vnoření centruje a normalizuje, typicky Zᵀ1=0 a ZᵀZ=I. Souřadnice pak tvoří vlastní vektory (I−W)ᵀ(I−W) s nejmenšími netriviálními vlastními čísly; konstantní vlastní vektor s nulovým číslem se vynechá, neboť (I−W)1=0.

První fáze tedy odhaduje lokální geometrii vahami W, druhá hledá souřadnice Z, které ji reprodukují.

## Poznámka Anki 1785306291465

Karty Anki: 1785306291466
GUID: l@3KHk!6!z; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Jak volba počtu sousedů k ovlivňuje LLE a jak se řeší singulární lokální úlohy?

### Odpověď (Back)

Příliš malé k může dát nestabilní okolí nebo nesouvislý sousednostní graf, takže se globální vnoření rozpadne. Příliš velké k poruší lokální linearitu a může spojovat vzdálené části variety.

Je-li k větší než dimenze původního prostoru, sousedé mohou být lineárně závislí a lokální rekonstrukční úloha singulární či nejednoznačná. Použije se modifikované LLE nebo vhodná regularizace lokální úlohy.

## Poznámka Anki 1785306291467

Karty Anki: 1785306291468
GUID: 3G0wd%|)9s; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Co ukazují příklady standardního a modifikovaného LLE a proč se vnoření nemá hodnotit jen esteticky?

### Odpověď (Back)

Na švýcarské rolce standardní LLE s k=15 zachová postupné lokální uspořádání barev, ale může plochu zdeformovat do klínovitého tvaru. Modifikované LLE ji rozvine do pravidelnější, přibližně obdélníkové 2D reprezentace.

Další uvedené metody jsou MDS, Isomap, t-SNE a UMAP. Na stejných datech mohou vytvořit výrazně odlišná vnoření, protože zachovávají různé aspekty geometrie a optimalizují jiné cíle. Vizuálně přitažlivý graf proto nemusí věrně zachovávat vztahy důležité pro konkrétní úlohu.

## Poznámka Anki 1785306291469

Karty Anki: 1785306291470
GUID: j[}Kdc/aWv; štítky: BI-ML2 iterace_04 Konsolidovano Prednaska_04.

### Otázka (Front)

Jaký je hlavní rozdíl a koncepční návaznost mezi ortogonální projekcí, PCA a LLE?

### Odpověď (Back)

Ortogonální projekce rozkládá data na zachovanou a zahozenou složku. PCA zvolí jeden globální lineární podprostor, který maximalizuje rozptyl a minimalizuje rekonstrukční chybu. Manifold learning hledá nelineární strukturu pomocí lokálních vztahů; LLE konkrétně nahrazuje globální linearitu zachováním lokálních afinních rekonstrukčních vah.

