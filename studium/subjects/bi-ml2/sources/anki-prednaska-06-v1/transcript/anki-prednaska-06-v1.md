# BI-ML2 – Přednáška 06

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291493

Karty Anki: 1785306291494
GUID: ,+3Ge>W#+a; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak se liší generativní a diskriminativní přístup ke klasifikaci?

### Odpověď (Back)

**Generativní model** odhaduje sdružené rozdělení P(X,Y)=P(X|Y)P(Y). Lze z něj generovat data: nejprve Y∼P(Y), potom X∼P(X|Y). Posterior získá Bayesovou větou P(Y=y|X=x)∝P(X=x|Y=y)P(Y=y). Protože modeluje i P(X), podporuje úlohy, které čistě diskriminativní model obecně neumí.

**Diskriminativní model** odhaduje přímo P(Y|X) nebo rozhodovací pravidlo Y=f(X), aniž modeluje vznik vstupů P(X). Příklady jsou logistická regrese a klasifikační neuronové sítě; v širším smyslu může být diskriminativní i model bez pravděpodobnostního výstupu, pokud přímo predikuje Y z X.

## Poznámka Anki 1785306291495

Karty Anki: 1785306291496
GUID: aj7ZWC<:FO; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak bag-of-words a multinomické rozdělení modelují dokument v Multinomial Naive Bayes?

### Odpověď (Back)

Bag-of-words reprezentuje dokument vektorem četností slov bez jejich pořadí. Slovník 𝒟 dává D=|𝒟| příznaků; xⱼ je počet výskytů slova j a n=Σⱼxⱼ počet zahrnutých tokenů.

Pro třídu y se používá
P(X=x|Y=y)=[n!/∏ⱼxⱼ!]∏ⱼp<sub>j,y</sub><sup>xⱼ</sup>,
kde p<sub>j,y</sub> je pravděpodobnost, že náhodný token dokumentu třídy y je slovo j; p<sub>j,y</sub>≥0 a Σⱼp<sub>j,y</sub>=1. Multinomický koeficient počítá pořadí tokenů vedoucí ke stejným četnostem. Při MAP jej lze vynechat, protože pro pevný dokument nezávisí na třídě.

## Poznámka Anki 1785306291497

Karty Anki: 1785306291498
GUID: =>vGV:(~Yh; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak se v Multinomial Naive Bayes odhadují a vyhlazují pravděpodobnosti slov?

### Odpověď (Back)

Označme N<sub>j,y</sub> počet výskytů slova j ve všech trénovacích dokumentech třídy y a T<sub>y</sub>=ΣⱼN<sub>j,y</sub> jejich celkový počet tokenů. MLE je p̂<sub>j,y</sub>=N<sub>j,y</sub>/T<sub>y</sub>.

Add-one smoothing používá p̂<sub>j,y</sub>=(N<sub>j,y</sub>+1)/(T<sub>y</sub>+D). Přičítá se D, protože jeden pseudočet dostane každé z D slov. Nepozorované slovo pak nemá pravděpodobnost nula a nevynuluje skóre třídy. Implementace ve scikit-learn se jmenuje `MultinomialNB`.

## Poznámka Anki 1785306291499

Karty Anki: 1785306291500
GUID: j@a[v;*{1E; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Proč se v Bayesově klasifikaci používají logaritmická skóre a jak vypadají v Multinomial NB?

### Odpověď (Back)

Součin mnoha pravděpodobností menších než 1 může numericky podtéct: matematicky nenulová hodnota se zaokrouhlí na 0. Proto se pracuje s logaritmy, které převádějí součiny na součty.

MAP maximalizuje log P(X=x|Y=y)+log P(Y=y); log je přísně rostoucí, takže zachová pořadí. V naivním Bayesovi se log-věrohodnost rozloží na součet příspěvků příznaků. Multinomial NB používá, až na člen nezávislý na třídě,
s<sub>y</sub>=log P(Y=y)+Σⱼxⱼlog p<sub>j,y</sub>.

Pro samotnou klasifikaci stačí porovnat tato neznormalizovaná log-skóre; pro posteriorní pravděpodobnosti je nutná normalizace přes třídy.

## Poznámka Anki 1785306291501

Karty Anki: 1785306291502
GUID: DU/DwB4Hny; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak log-sum-exp trik stabilně normalizuje třídní log-skóre?

### Odpověď (Back)

Log-sum-exp počítá log Σᵢexp(sᵢ). Pro m=maxᵢsᵢ platí
log Σᵢe<sup>sᵢ</sup>=m+log Σᵢe<sup>sᵢ−m</sup>.
Po posunu je největší exponent 0 a ostatní nekladné, takže nevznikají extrémně velké exponenciály a omezuje se podtečení.

Z log-skóre s<sub>y</sub> dostaneme
log P(Y=y|X=x)=s<sub>y</sub>−logsumexp(s₁,…,s<sub>C</sub>)
a P(Y=y|X=x)=exp[s<sub>y</sub>−logsumexp(s₁,…,s<sub>C</sub>)].

## Poznámka Anki 1785306291503

Karty Anki: 1785306291504
GUID: K0DWXNgaky; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak Gaussovská diskriminační analýza používá vícerozměrné normální rozdělení?

### Odpověď (Back)

Gaussovská diskriminační analýza je generativní model s X|Y=y∼N(μ<sub>y</sub>,Σ<sub>y</sub>), kde μ<sub>y</sub> je vektor středních hodnot a Σ<sub>y</sub> kovarianční matice. Vektor X∼N(μ,Σ) je charakterizován tím, že každá lineární kombinace cᵀX∼N(cᵀμ,cᵀΣc). Platí E[X]=μ, cov(X)=Σ a marginálně Xᵢ∼N(μᵢ,Σᵢᵢ).

Pro pozitivně definitní Σ je hustota
f(x)=(2π)<sup>−p/2</sup>|Σ|<sup>−1/2</sup>exp[−½(x−μ)ᵀΣ<sup>−1</sup>(x−μ)].
Definitnost zajišťuje inverzi a kladný determinant. Singulární pozitivně semidefinitní Σ dává degenerované rozdělení bez hustoty na celém ℝᵖ.

## Poznámka Anki 1785306291505

Karty Anki: 1785306291506
GUID: LMtW[8Uwfs; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak kovarianční matice určuje geometrii vícerozměrného normálního rozdělení a vztah ke Gaussian NB?

### Odpověď (Back)

Kvadratický člen (x−μ)ᵀΣ<sup>−1</sup>(x−μ) je čtverec Mahalanobisovy vzdálenosti. Zohledňuje měřítka a korelace: směry s velkým rozptylem váží méně. Množiny stejné hustoty jsou elipsoidy; mimodiagonální kovariance je mohou natáčet vůči osám.

U vícerozměrně normálního vektoru jsou složky nezávislé, je-li Σ diagonální. Gaussian Naive Bayes je proto speciální případ Gaussovské diskriminační analýzy s diagonální třídně podmíněnou kovarianční maticí v každé třídě.

## Poznámka Anki 1785306291507

Karty Anki: 1785306291508
GUID: qrxe|I)%MN; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak funguje QDA a proč má kvadratické rozhodovací hranice?

### Odpověď (Back)

Gaussovská diskriminační analýza predikuje Ŷ=arg max<sub>y</sub>f<sub>X|Y=y</sub>(x)P(Y=y). V QDA má každá třída vlastní Σ<sub>y</sub> a skóre
δ<sub>y</sub>(x)=−½log|Σ<sub>y</sub>|−½(x−μ<sub>y</sub>)ᵀΣ<sub>y</sub><sup>−1</sup>(x−μ<sub>y</sub>)+log π<sub>y</sub>,
po vypuštění společné konstanty.

Hranice tříd y,y′ vznikne z δ<sub>y</sub>(x)=δ<sub>y′</sub>(x). Pokud se kovariance liší, členy xᵀΣ<sub>y</sub><sup>−1</sup>x se nezruší, takže hranice je obecně kvadratická a zakřivená; právě to ukazuje vizualizace rozdílných kovariančních struktur.

## Poznámka Anki 1785306291509

Karty Anki: 1785306291510
GUID: R-83POYtgH; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak se metodou maximální věrohodnosti odhadují parametry QDA?

### Odpověď (Back)

Pro každou třídu y:
π̂<sub>y</sub>=N<sub>y</sub>/N,
μ̂<sub>y</sub>=(1/N<sub>y</sub>)Σ<sub>i:Yᵢ=y</sub>xᵢ,
Σ̂<sub>y</sub>=(1/N<sub>y</sub>)Σ<sub>i:Yᵢ=y</sub>(xᵢ−μ̂<sub>y</sub>)(xᵢ−μ̂<sub>y</sub>)ᵀ.

MLE kovariance používá N<sub>y</sub>, zatímco běžný nestranný odhad N<sub>y</sub>−1. Pro C tříd QDA odhaduje C samostatných kovariančních matic.

## Poznámka Anki 1785306291511

Karty Anki: 1785306291512
GUID: OB})/fEK>i; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak generativní LDA vzniká ze společné kovariance a jaká má skóre, posteriory a hranice?

### Odpověď (Back)

LDA předpokládá X|Y=y∼N(μ<sub>y</sub>,Σ) se stejnou Σ pro všechny třídy. Používá lineární skóre
δ<sub>y</sub>(x)=μ<sub>y</sub>ᵀΣ<sup>−1</sup>x−½μ<sub>y</sub>ᵀΣ<sup>−1</sup>μ<sub>y</sub>+log π<sub>y</sub>.
Kvadratický člen −½xᵀΣ<sup>−1</sup>x je pro třídy společný, a proto se zruší.

Posteriory jsou softmax: P(Y=y|X=x)=exp δ<sub>y</sub>(x)/Σ<sub>c</sub>exp δ<sub>c</sub>(x). Hranice dvou tříd je nadrovina
(β<sub>y</sub>−β<sub>y′</sub>)ᵀx=γ<sub>y′</sub>−γ<sub>y</sub>,
kde β<sub>y</sub>=Σ<sup>−1</sup>μ<sub>y</sub> a γ<sub>y</sub>=−½μ<sub>y</sub>ᵀΣ<sup>−1</sup>μ<sub>y</sub>+log π<sub>y</sub>. Ve 2D je to přímka.

## Poznámka Anki 1785306291513

Karty Anki: 1785306291514
GUID: yEVdo)d=4P; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak souvisí binární generativní LDA s logistickou regresí?

### Odpověď (Back)

Posterior binární LDA lze zapsat P(Y=1|X=x)=σ(wᵀx+w₀), kde
w=Σ<sup>−1</sup>(μ₁−μ₀),
w₀=−½wᵀ(μ₁+μ₀)+log(π₁/π₀).
Poměr priorů posouvá hranici ve prospěch apriorně pravděpodobnější třídy.

Funkční tvar je stejný jako u logistické regrese, ale trénování nikoli: LDA odhaduje generativní parametry π<sub>y</sub>,μ<sub>y</sub>,Σ a z nich w,w₀ odvodí; logistická regrese odhaduje w,w₀ přímo maximalizací podmíněné věrohodnosti P(Y|X).

## Poznámka Anki 1785306291515

Karty Anki: 1785306291516
GUID: J,FFTFRQ>L; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak LDA odhaduje společnou kovarianci a jaký je kompromis LDA oproti QDA?

### Odpověď (Back)

Pooled MLE je
Σ̂=(1/N)Σ<sub>y</sub>Σ<sub>i:Yᵢ=y</sub>(xᵢ−μ̂<sub>y</sub>)(xᵢ−μ̂<sub>y</sub>)ᵀ.
Body se centrují kolem průměru své třídy, protože Σ má popsat vnitrotřídní variabilitu, ne rozdíly mezi středy. LDA odhaduje jedinou společnou kovarianci bez ohledu na počet tříd.

QDA odhaduje plnou kovarianci pro každou třídu a nabízí flexibilní kvadratické hranice; LDA sdílí jednu kovarianci, má méně parametrů a pouze lineární nadroviny.

## Poznámka Anki 1785306291517

Karty Anki: 1785306291518
GUID: ees,tR)j8N; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Co je binární Fisherova LDA a jak se její kritérium zapíše pomocí scatter matic?

### Odpověď (Back)

FLDA je supervizovaná lineární projekce hledající velkou separaci třídních středů a malý rozptyl uvnitř tříd; explicitně nevyžaduje normální rozdělení ani společné kovariance.

Pro směr w je zᵢ=wᵀxᵢ/‖w‖ a projektovaný střed m<sub>y</sub>=wᵀμ̂<sub>y</sub>/‖w‖. Maximalizuje se
J(w)=(m₁−m₀)²/(s₀²+s₁²): čitatel je mezitřídní separace, jmenovatel vnitrotřídní rozptyl.

S<sub>B</sub>=(μ̂₁−μ̂₀)(μ̂₁−μ̂₀)ᵀ,
S<sub>W</sub>=Σ<sub>i:Yᵢ=0</sub>(xᵢ−μ̂₀)(xᵢ−μ̂₀)ᵀ+Σ<sub>i:Yᵢ=1</sub>(xᵢ−μ̂₁)(xᵢ−μ̂₁)ᵀ,
a J(w)=wᵀS<sub>B</sub>w/(wᵀS<sub>W</sub>w). Kritérium nezávisí na délce w, protože škálování násobí oba členy stejným čtvercem.

## Poznámka Anki 1785306291519

Karty Anki: 1785306291520
GUID: vO5_w^Bc#Q; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak se řeší binární FLDA a jak souvisí s generativní LDA?

### Odpověď (Back)

Stacionární směr splňuje zobecněnou vlastní úlohu S<sub>B</sub>w=λS<sub>W</sub>w, kde λ=J(w). Je-li S<sub>W</sub> regulární, pak až na nenulovou konstantu
w∝S<sub>W</sub><sup>−1</sup>(μ̂₁−μ̂₀).

Protože S<sub>W</sub>=NΣ̂, je směr ekvivalentní směru generativní LDA až na škálování. FLDA mu dává optimalizační interpretaci: maximalizuje poměr mezitřídní separace k vnitrotřídnímu rozptylu. Při přibližně normálních třídních rozděleních se společnou kovariancí získává také pravděpodobnostní interpretaci generativní LDA.

## Poznámka Anki 1785306291521

Karty Anki: 1785306291522
GUID: @S7Ryy-cgm; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak se Fisherova LDA zobecňuje na více tříd a kolik může vytvořit směrů?

### Odpověď (Back)

Pro C tříd hledá projekční matici W maximalizující mezitřídní rozptyl relativně k vnitrotřídnímu. Může vytvořit nejvýše C−1 netriviálních směrů, protože odchylky C třídních průměrů od společného středu jsou lineárně závislé.

S<sub>W</sub>=Σ<sub>y</sub>Σ<sub>i:Yᵢ=y</sub>(xᵢ−μ̂<sub>y</sub>)(xᵢ−μ̂<sub>y</sub>)ᵀ,
S<sub>B</sub>=Σ<sub>y</sub>(μ̂<sub>y</sub>−μ̂)(μ̂<sub>y</sub>−μ̂)ᵀ, kde μ̂ je průměr třídních průměrů.

Jedno kritérium je J(W)=det(WᵀS<sub>B</sub>W)/det(WᵀS<sub>W</sub>W). Směry se získají zobecněnými vlastními vektory dvojice (S<sub>B</sub>,S<sub>W</sub>) nebo vlastními vektory symetricky vybělené matice S<sub>W</sub><sup>−1/2</sup>S<sub>B</sub>S<sub>W</sub><sup>−1/2</sup>.

## Poznámka Anki 1785306291523

Karty Anki: 1785306291524
GUID: K2T3E;a#Qw; štítky: BI-ML2 iterace_06 Konsolidovano Prednaska_06.

### Otázka (Front)

Jak se liší PCA a FLDA a jaká je koncepční návaznost QDA, LDA a FLDA?

### Odpověď (Back)

PCA bez štítků maximalizuje celkový rozptyl; FLDA využívá třídy a maximalizuje jejich separaci vzhledem k vnitrotřídnímu rozptylu. Směr největšího rozptylu může zachycovat hlavně variabilitu uvnitř tříd, takže nemusí být klasifikačně vhodný; supervizovaná LDA může zvolit lépe separující směr s menším celkovým rozptylem.

**Generativní větev:** odhad priorů a normálních P(X|Y) → Bayesův posterior → třídní kovariance dávají QDA → společná kovariance ruší kvadratické členy a dává LDA.
**Fisherova větev:** projekce → změřit vzdálenost třídních středů a vnitrotřídní rozptyl → maximalizovat jejich poměr zobecněnou vlastní úlohou.

