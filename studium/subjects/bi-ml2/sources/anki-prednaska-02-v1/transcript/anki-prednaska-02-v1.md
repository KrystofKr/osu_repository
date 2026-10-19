# BI-ML2 – Přednáška 02

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291401

Karty Anki: 1785306291402
GUID: $R)hL_DU9y; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Jak se binární lineární klasifikátor interpretuje geometricky v prostoru bázových příznaků?

### Odpověď (Back)

Pro Y ∈ {−1, 1} se používá diskriminační funkce f(x) = wᵀϕ(x) + w₀ a predikce Ŷ(x) = 1 pro f(x) ≥ 0, jinak −1 (tj. sgn(f(x)) s konvencí pro nulu).

Rozhodovací hranice je množina bodů u splňujících wᵀu + w₀ = 0: jde o nadrovinu s normálovým vektorem w. Její orientovaná vzdálenost od počátku ve směru w je −w₀/‖w‖. Orientovaná vzdálenost bodu u od nadroviny je r = (wᵀu + w₀)/‖w‖, takže pro transformovaný vstup r(x) = f(x)/‖w‖.

Znaménko f(x) určuje poloprostor, a tedy třídu. Absolutní hodnota f(x) sama není geometrickou vzdáleností: platí |f(x)| = ‖w‖·|r(x)|, proto je nutná normalizace normou ‖w‖.

## Poznámka Anki 1785306291403

Karty Anki: 1785306291404
GUID: PcV*119Zjc; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Jak se od lineární separability odvodí princip největšího odstupu a kanonická škála SVM?

### Odpověď (Back)

Data jsou lineárně separabilní v prostoru ϕ(x), existují-li w, w₀ takové, že Yᵢf(xᵢ) > 0 pro všechna i. Separujících nadrovin bývá mnoho a liší se robustností. Geometrický odstup klasifikátoru je minimální vzdálenost trénovacího bodu od hranice; odstup bodu i se štítkem je Yᵢf(xᵢ)/‖w‖. Násobení Yᵢ zajistí kladnou hodnotu právě při správné klasifikaci.

Princip největšího odstupu maximalizuje minᵢ Yᵢ(wᵀϕ(xᵢ)+w₀)/‖w‖. Funkční odstup Yᵢf(xᵢ) závisí na škále parametrů, geometrický odstup Yᵢf(xᵢ)/‖w‖ nikoli: přeškálování w,w₀ kladným κ nemění hranici, znaménka ani geometrické vzdálenosti.

Proto lze zavést kanonickou škálu, v níž nejbližší body splňují Yᵢf(xᵢ)=1 a všechny body Yᵢf(xᵢ) ≥ 1. Jednostranný odstup je pak 1/‖w‖ a šířka pásu mezi f(x)=−1 a f(x)=1 je 2/‖w‖. Maximalizace 1/‖w‖ je ekvivalentní minimalizaci ½‖w‖².

## Poznámka Anki 1785306291405

Karty Anki: 1785306291406
GUID: $_EX$a.e!L; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Jak zní primární úloha hard-margin SVM a co v ní určují podpůrné vektory?

### Odpověď (Back)

Hard-margin SVM řeší

min<sub>w,w₀</sub> ½‖w‖²
za podmínek Yᵢ(wᵀϕ(xᵢ)+w₀) ≥ 1 pro všechna i.

Jde o kvadratické programování: účelová funkce je kvadratická ve w a omezení jsou lineární nerovnosti ve w,w₀. Podpůrný vektor má aktivní vazbu Yᵢf(xᵢ)=1; tyto body určují polohu a orientaci optimální nadroviny, zatímco body dále od pásu ji přímo neovlivňují. Pro lineárně neseparabilní data je úloha neproveditelná, protože nelze splnit všechna omezení.

## Poznámka Anki 1785306291407

Karty Anki: 1785306291408
GUID: n}l=8=HL%c; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Jak soft-margin SVM zavádí slack proměnné ξᵢ a co znamenají jejich různé hodnoty?

### Odpověď (Back)

Soft-margin SVM dovoluje porušit požadovaný odstup pomocí ξᵢ ≥ 0 a vazby Yᵢf(xᵢ) ≥ 1 − ξᵢ. Nejmenší přípustná hodnota je ξᵢ = max(0, 1 − Yᵢf(xᵢ)), tedy hinge loss daného bodu.

**Geometrický význam:**
• ξᵢ = 0: správná klasifikace na hranici pásu nebo vně něj, Yᵢf(xᵢ) ≥ 1.
• 0 < ξᵢ < 1: správná klasifikace uvnitř pásu, 0 < Yᵢf(xᵢ) < 1.
• ξᵢ = 1: bod přesně na rozhodovací hranici, Yᵢf(xᵢ)=0.
• ξᵢ > 1: bod na nesprávné straně hranice, tedy chybná klasifikace.

## Poznámka Anki 1785306291409

Karty Anki: 1785306291410
GUID: q|(h:){]Yq; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Jaká je primární úloha soft-margin SVM a jak parametr C řídí regularizaci a robustnost?

### Odpověď (Back)

Soft-margin SVM minimalizuje ½‖w‖² + CΣᵢξᵢ za podmínek ξᵢ ≥ 0 a Yᵢ(wᵀϕ(xᵢ)+w₀) ≥ 1−ξᵢ. Vyvažuje široký geometrický odstup (malé ‖w‖) proti porušením odstupu a chybám (malé Σξᵢ).

**Velké C:** porušení jsou drahá, model se těsněji přizpůsobuje trénovacím datům i za cenu užšího odstupu; jde o slabší regularizaci.
**Malé C:** model toleruje více bodů uvnitř pásu či chyb, aby zmenšil ‖w‖ a získal širší odstup; jde o silnější regularizaci.

Hard-margin vyžaduje bezchybnou separaci s odstupem, soft-margin připouští porušení penalizovaná C. Malá norma w zvětšuje odstup a snižuje citlivost rozhodnutí na malé perturbace vstupu; C současně řídí toleranci k porušením v trénovacích datech.

## Poznámka Anki 1785306291411

Karty Anki: 1785306291412
GUID: HK_!b+Mc]v; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Jak souvisejí slack proměnné, hinge loss, počet chyb a parametrizace ν-SVM?

### Odpověď (Back)

Po eliminaci ξᵢ je soft-margin úloha ekvivalentní minimalizaci
½‖w‖² + CΣᵢ max(0, 1 − Yᵢf(xᵢ)).

Hinge loss L(y,f(x)) = max(0,1−yf(x)) je nulová jen při správné klasifikaci s funkčním odstupem alespoň 1. Není diferencovatelná v yf(x)=1, ale je konvexní a lze použít subgradientní či specializované konvexní metody.

Každá trénovací chyba má ξᵢ > 1, proto počet chyb ≤ Σξᵢ. Rovnost obecně neplatí: přispívají i správně klasifikované body uvnitř pásu a chybný bod může přispět více než 1.

Někdy se volí C = 1/(νN), kde 0 < ν ≤ 1; odpovídající varianta se označuje ν-SVM.

## Poznámka Anki 1785306291413

Karty Anki: 1785306291414
GUID: ^Xg[4#T(Yt; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Jak vypadá duální úloha soft-margin SVM a výsledná jádrová rozhodovací funkce?

### Odpověď (Back)

Duál maximalizuje
Σᵢaᵢ − ½ΣᵢΣⱼaᵢaⱼYᵢYⱼk(xᵢ,xⱼ)
za podmínek 0 ≤ aᵢ ≤ C a ΣᵢaᵢYᵢ = 0. Koeficient aᵢ měří příspěvek trénovacího bodu; rovnost ΣaᵢYᵢ=0 vzniká stacionaritou Lagrangeovy funkce podle nepenalizovaného interceptu w₀.

Protože transformované body vystupují pouze ve skalárních součinech ϕ(xᵢ)ᵀϕ(xⱼ), lze je nahradit jádrem. Primární vektor je w = ΣᵢaᵢYᵢϕ(xᵢ) a diskriminační funkce
f(x) = ΣᵢaᵢYᵢk(xᵢ,x) + w₀,
takže Ŷ(x)=sgn(f(x)). Jde o jádrový model centrovaný v trénovacích bodech; jeho obecný koeficient αᵢ = aᵢYᵢ.

## Poznámka Anki 1785306291415

Karty Anki: 1785306291416
GUID: L?qph(XA}A; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Jak KKT podmínky vysvětlují podpůrné vektory, řídkost SVM a výpočet interceptu?

### Odpověď (Back)

Řešení je obvykle řídké: podpůrné vektory jsou právě body s aᵢ > 0 a jen ty přispívají do predikce.

**KKT rozdělení:**
• aᵢ = 0: bod je správně klasifikován vně pásu a lokálně neovlivňuje funkci.
• 0 < aᵢ < C: bod leží na hranici pásu a Yᵢf(xᵢ)=1.
• aᵢ = C: bod leží uvnitř pásu nebo je chybně klasifikován; vazba na slack je nasycena.

Proto při predikci stačí jádro vyhodnocovat vůči podpůrným vektorům. Intercept lze určit z libovolného bodu s 0<aᵢ<C:
w₀ = Yᵢ − ΣⱼaⱼYⱼk(xⱼ,xᵢ),
případně hodnoty zprůměrovat přes více takových bodů.

## Poznámka Anki 1785306291417

Karty Anki: 1785306291418
GUID: &5tc0([#5y; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Jak počet podpůrných vektorů ovlivňuje cenu predikce a jak s ním typicky souvisí C?

### Odpověď (Back)

Jedna predikce vyžaduje vyhodnocení jádra vůči každému podpůrnému vektoru, takže více podpůrných vektorů znamená dražší inferenci.

Malé C (silnější regularizace) obvykle vytváří širší pás s více body uvnitř, a tedy více podpůrných vektorů. Velké C (slabší regularizace) obvykle vede k užšímu pásu a menšímu počtu podpůrných vektorů. Jde o typickou tendenci; přesný vztah závisí na datech a jádru.

## Poznámka Anki 1785306291419

Karty Anki: 1785306291420
GUID: i`#`i#rh6K; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Proč lineární SVM neřeší XOR a jak jej řeší nelineární jádro včetně vlivu C?

### Odpověď (Back)

Ideální XOR nelze v původním prostoru oddělit jedinou přímkou či nadrovinou. Nelineární jádro data implicitně zobrazí do prostoru, kde mohou být lineárně separovatelná; zpět v původním prostoru to odpovídá nelineární rozhodovací hranici. Gaussovské jádro vytváří lokální nelineární hranice podle vzdálenostní podobnosti bodů.

V příkladech XOR malé C (např. 0,1) dává silně regularizovaný model s mnoha podpůrnými vektory. Velká C (např. 10 až 1000) kladou větší důraz na přesné přizpůsobení trénovacím datům a typicky používají méně podpůrných vektorů.

## Poznámka Anki 1785306291421

Karty Anki: 1785306291422
GUID: O)oS9LeCaM; štítky: BI-ML2 iterace_02 Konsolidovano Prednaska_02.

### Otázka (Front)

Jaké jsou hlavní konstrukční kroky SVM a jak propojuje bázové funkce, dualitu a jádrový trik?

### Odpověď (Back)

Postup je: (1) definovat lineární diskriminační funkci, (2) geometricky ji interpretovat jako nadrovinu, (3) maximalizovat minimální odstup, (4) pro neseparabilní data zavést slack proměnné a (5) převést úlohu do jádrového duálu.

Klasifikátor zůstává lineární v transformovaném prostoru ϕ(x). Duální řešení závisí jen na skalárních součinech transformovaných bodů, které lze nahradit jádrem k(x,y); tím vznikne nelineární klasifikátor v původním prostoru bez explicitní konstrukce ϕ(x).

