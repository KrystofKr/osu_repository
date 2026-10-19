# BI-ML2 – Přednáška 03

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291423

Karty Anki: 1785306291424
GUID: ^q|[7RU^7L; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Co je prokletí dimenzionality a jak je ilustruje objem okrajové slupky hyperkrychle?

### Odpověď (Back)

Prokletí dimenzionality označuje jevy, kdy s počtem příznaků exponenciálně roste objem prostoru, data řídnou a lokální odhady či predikce ztrácejí spolehlivost.

V jednotkové d-rozměrné krychli má soustředná podkrychle s hranou 1−ε podíl objemu (1−ε)<sup>d</sup>; okrajová slupka tedy zabírá 1−(1−ε)<sup>d</sup>. Pro pevné ε>0 centrální podíl exponenciálně klesá k nule, takže většina objemu je ve vysoké dimenzi blízko hranice.

Příklad: ve 100 rozměrech a při slupce tloušťky 0,01 od každé stěny má centrální krychle hranu 0,98 a slupka obsahuje 1−0,98<sup>100</sup> ≈ 86,7 % objemu.

## Poznámka Anki 1785306291425

Karty Anki: 1785306291426
GUID: [6!23gohoG; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Jak vysoká dimenze ovlivňuje vzdálenosti, hustotu dat a potřebný počet pozorování?

### Odpověď (Back)

V omezeném vysokodimenzionálním prostoru bývají body relativně daleko, protože dostupný objem roste rychleji než počet pozorování. Při pevném N prudce klesá hustota dat a okolí nového bodu obsahuje stále méně trénovacích příkladů. Model proto predikuje daleko od pozorovaných bodů a musí více interpolovat či extrapolovat, což zvyšuje citlivost na chybu modelu.

Samotné přidávání dat problém obecně neřeší: počet bodů potřebný k zachování stejné hustoty roste exponenciálně s dimenzí. Například síť s rozestupem asi 0,1 v každé ze 100 souřadnic jednotkové krychle vyžaduje řádově 10<sup>100</sup> bodů.

## Poznámka Anki 1785306291427

Karty Anki: 1785306291428
GUID: @_%nLzjXCm; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Co říká hypotéza variet a jak rozlišuje ambientní a intrinsickou dimenzi?

### Odpověď (Back)

Reálná data obvykle nevyplňují celý vysokodimenzionální prostor rovnoměrně, ale leží v malé strukturované části. Hypotéza variet říká, že jsou přibližně soustředěna na varietě s mnohem nižší vnitřní dimenzí.

**Ambientní dimenze** je dimenze reprezentačního prostoru (např. počet pixelů či příznaků). **Intrinsická dimenze** je počet nezávislých souřadnic potřebných k popisu skutečné struktury dat; může být výrazně nižší.

**MNIST:** obraz má 28×28=784 příznaků, ale realistické číslice tvoří jen nepatrnou strukturovanou část všech pixelových kombinací; náhodný bod v ℝ⁷⁸⁴ proto téměř jistě nebude číslice.
**Švýcarská rolka:** data leží v trojrozměrném prostoru, ale na stočené dvourozměrné ploše.

## Poznámka Anki 1785306291429

Karty Anki: 1785306291430
GUID: oNYOI%z5Ta; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Co je cílem redukce dimenzionality a jak se liší lineární projekce od manifold learningu?

### Odpověď (Back)

Cílem je reprezentovat data v menším počtu rozměrů při zachování strukturálně důležité informace. Podle hypotézy variet obsahují původní příznaky redundantní stupně volnosti a strukturu lze popsat menším počtem latentních souřadnic.

**Lineární redukce** promítá data, obvykle ortogonálně, do jediného globálního nízkodimenzionálního lineárního podprostoru. **Manifold learning** používá nelineární metody k zachycení zakřivené nízkodimenzionální variety. Jediná lineární projekce nemusí rozvinout švýcarskou rolku: vzdálené části se mohou překrýt a vnitřní geometrie se zdeformuje.

Koncepční posloupnost je: vysoká dimenze → řídkost dat → hypotéza nízkodimenzionální variety → redukce dimenzionality; lineární přístup tuto strukturu aproximuje projekcí na podprostor.

## Poznámka Anki 1785306291431

Karty Anki: 1785306291432
GUID: x<?>,MN_|J; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Jak se definuje ortogonální projekce bodu na q-rozměrný podprostor a proč je jednoznačná?

### Odpověď (Back)

q-rozměrný podprostor V ⊆ ℝᵖ tvoří všechny lineární kombinace q lineárně nezávislých vektorů. Každý x∈ℝᵖ má vzhledem k V jednoznačný rozklad x = vₓ + uₓ, kde vₓ∈V a uₓ je kolmé na každý vektor z V.

Ortogonální projekce je složka vₓ; reziduum uₓ je část, kterou projekce nezachytí. Projekci lze také charakterizovat jako bod v∈V minimalizující ‖x−v‖. Jednoznačnost plyne z toho, že V∩V<sup>⊥</sup> obsahuje pouze nulový vektor.

## Poznámka Anki 1785306291433

Karty Anki: 1785306291434
GUID: dZGp/=(89C; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Jak se ortogonální projekce a reziduum zapisují pomocí ortonormální báze?

### Odpověď (Back)

Vektory b₁,…,b<sub>q</sub> tvoří ortonormální bázi V, jestliže mají normu 1, navzájem jsou kolmé a generují V. Souřadnice x ve směru bᵢ je τᵢ=xᵀbᵢ a projekce
vₓ = Σᵢ₌₁<sup>q</sup>(xᵀbᵢ)bᵢ.

Doplníme-li bázi na úplnou ortonormální bázi ℝᵖ, kolmá složka je
uₓ = Σᵢ₌q₊₁<sup>p</sup>(xᵀbᵢ)bᵢ.

## Poznámka Anki 1785306291435

Karty Anki: 1785306291436
GUID: c)O@{jTL:v; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Jak matice V kóduje ortonormální bázi a nízkodimenzionální souřadnice bodu?

### Odpověď (Back)

Matice V∈ℝ<sup>p×q</sup> má ve sloupcích ortonormální bázové vektory podprostoru, proto VᵀV=I<sub>q</sub>. Pro q<p obecně VVᵀ≠I<sub>p</sub>, protože sloupce nepokrývají celé ℝᵖ.

Nízkodimenzionální reprezentace sloupcového bodu je tₓ=Vᵀx∈ℝᵠ; obsahuje souřadnice projekce v dané bázi. Pro řádkový zápis platí tₓᵀ=xᵀV. Mapování x↦Vᵀx redukuje počet souřadnic z p na q<p.

## Poznámka Anki 1785306291437

Karty Anki: 1785306291438
GUID: mB(cSZ;rjv; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Jak se z nízkodimenzionálních souřadnic rekonstruuje projekce a jaké vlastnosti má projekční matice?

### Odpověď (Back)

Z tₓ se projekce rekonstruuje jako vₓ=Vtₓ=VVᵀx. Matice P<sub>V</sub>=VVᵀ∈ℝ<sup>p×p</sup> je matice ortogonální projekce.

Je **symetrická**: P<sub>V</sub>ᵀ=P<sub>V</sub>, a **idempotentní**: P<sub>V</sub>²=V(VᵀV)Vᵀ=P<sub>V</sub>. Idempotence znamená, že opakovaná projekce již promítnutý bod nezmění. Pro x∈V platí P<sub>V</sub>x=x, zatímco vektor kolmý k V zobrazí P<sub>V</sub> na nulu.

## Poznámka Anki 1785306291439

Karty Anki: 1785306291440
GUID: KWt>|?J!+t; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Jak se maticově vyjádří reziduum ortogonální projekce a jaké vztahy splňuje?

### Odpověď (Back)

Reziduum je uₓ=x−vₓ=(I<sub>p</sub>−VVᵀ)x. Je kolmé na V, protože Vᵀuₓ=Vᵀx−VᵀVVᵀx=0. Jelikož x=vₓ+uₓ a vₓ⊥uₓ, platí Pythagorův vztah ‖x‖²=‖vₓ‖²+‖uₓ‖².

## Poznámka Anki 1785306291441

Karty Anki: 1785306291442
GUID: ReC~6DJBKu; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Jak se ortogonální redukce a rekonstrukce zapisují pro celý dataset X?

### Odpověď (Back)

Pro X∈ℝ<sup>N×p</sup> je redukovaný dataset T<sub>q</sub>=XV∈ℝ<sup>N×q</sup>; každý řádek obsahuje q souřadnic příslušného bodu. Rekonstrukce projekcí v původních souřadnicích je X<sub>V</sub>=T<sub>q</sub>Vᵀ=XVVᵀ∈ℝ<sup>N×p</sup>.

T<sub>q</sub> tedy ukládá kompaktní q-rozměrnou reprezentaci, zatímco X<sub>V</sub> ukládá tytéž projekce znovu vyjádřené pomocí původních p příznaků.

## Poznámka Anki 1785306291443

Karty Anki: 1785306291444
GUID: ^bW+Z)FydN; štítky: BI-ML2 iterace_03 Konsolidovano Prednaska_03.

### Otázka (Front)

Co se při ortogonální redukci ztrácí, kdy je rekonstrukce přesná a co určuje její kvalitu?

### Odpověď (Back)

Ztrácejí se reziduální složky kolmé na V. Bod lze z tₓ=Vᵀx přesně rekonstruovat právě tehdy, když x∈V; potom x=VVᵀx.

Geometrická projekce nezávisí na konkrétní ortonormální bázi V: souřadnice tₓ se při změně báze ortogonálně pootočí či odrazí, ale VVᵀx zůstane stejné, protože závisí jen na podprostoru.

Redukci lze chápat jako kódování x↦tₓ=Vᵀx a dekódování tₓ↦vₓ=Vtₓ. Při pevné cílové dimenzi q určuje kvalitu volba podprostoru V: které směry variability zachová a které skončí v reziduu. Navazující otázkou je zvolit V tak, aby se zachovalo co nejvíce důležité informace a minimalizovala rekonstrukční chyba.

