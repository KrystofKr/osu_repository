# Goodfellow – Blok 03 – karty 201–300

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001406118

Karty Anki: 1790001406118
GUID: P.]z)ZTU>i; štítky: (žádné).

### Otázka (Front)

Co je exponential distribution?

### Odpověď (Back)

Continuous distribution na x≥0 s density p(x;λ)=λe^{−λx}.

## Poznámka Anki 1790001406119

Karty Anki: 1790001406119
GUID: EQx22a4f>g; štítky: (žádné).

### Otázka (Front)

Kdy je exponential distribution užitečná?

### Odpověď (Back)

Pro variables, které mají být nezáporné a preferovat values blízko nule.

## Poznámka Anki 1790001406120

Karty Anki: 1790001406120
GUID: n/TPpwel#K; štítky: (žádné).

### Otázka (Front)

Co je Laplace distribution?

### Odpověď (Back)

Distribution s density p(x;μ,γ)=(1/(2γ))exp(−|x−μ|/γ), která má ostřejší peak a těžší tails než Gaussian.

## Poznámka Anki 1790001406121

Karty Anki: 1790001406121
GUID: K3hS~O#<)d; štítky: (žádné).

### Otázka (Front)

Proč Laplace prior podporuje sparsity v MAP inference?

### Odpověď (Back)

Jeho negative log-density je úměrná L¹ normě, která často dává přesně nulové optimum components.

## Poznámka Anki 1790001406122

Karty Anki: 1790001406122
GUID: rW1ZW$sS5@; štítky: (žádné).

### Otázka (Front)

Co je Dirac distribution δ(x−μ)?

### Odpověď (Back)

Generalized distribution soustřeďující veškerou probability mass v jediném bodě μ.

## Poznámka Anki 1790001406123

Karty Anki: 1790001406123
GUID: zn@JZ%Q^0x; štítky: (žádné).

### Otázka (Front)

Jak se Dirac delta používá k reprezentaci deterministic variable?

### Odpověď (Back)

p(x)=δ(x−f(z)) vyjadřuje, že x je přesně určeno funkcí f(z).

## Poznámka Anki 1790001406124

Karty Anki: 1790001406124
GUID: Q~afj*vr32; štítky: (žádné).

### Otázka (Front)

Co je empirical distribution p̂_data?

### Odpověď (Back)

Distribution, která přiřazuje stejnou probability training examples a nulu jiným discrete observations.

## Poznámka Anki 1790001406125

Karty Anki: 1790001406125
GUID: GQN{i-FYO,; štítky: (žádné).

### Otázka (Front)

Jak se sigmoid function definuje?

### Odpověď (Back)

σ(x)=1/(1+e^{−x}).

## Poznámka Anki 1790001406126

Karty Anki: 1790001406126
GUID: k3m2SEV]K*; štítky: (žádné).

### Otázka (Front)

Proč sigmoid přirozeně parametrizuje Bernoulli probability?

### Odpověď (Back)

Mapuje libovolné real číslo do intervalu (0,1).

## Poznámka Anki 1790001406127

Karty Anki: 1790001406127
GUID: DL[fOkzuxd; štítky: (žádné).

### Otázka (Front)

Co je logit function?

### Odpověď (Back)

Inverse sigmoid: logit(p)=log(p/(1−p)).

## Poznámka Anki 1790001406128

Karty Anki: 1790001406128
GUID: F)Sa=y*K6E; štítky: (žádné).

### Otázka (Front)

Co je softplus function?

### Odpověď (Back)

ζ(x)=log(1+e^x), smooth approximation max(0,x).

## Poznámka Anki 1790001406129

Karty Anki: 1790001406129
GUID: f7;kw;T]E|; štítky: (žádné).

### Otázka (Front)

Jaký vztah má derivative softplus k sigmoid?

### Odpověď (Back)

d/dx softplus(x)=σ(x).

## Poznámka Anki 1790001406130

Karty Anki: 1790001406130
GUID: q*/a];DQk:; štítky: (žádné).

### Otázka (Front)

Jak z joint distribution definujeme conditional distribution?

### Odpověď (Back)

p(x|y)=p(x,y)/p(y), pokud p(y)>0.

## Poznámka Anki 1790001406131

Karty Anki: 1790001406131
GUID: G7DK.C;#by; štítky: (žádné).

### Otázka (Front)

Co říká Bayes rule?

### Odpověď (Back)

P(x|y)=P(y|x)P(x)/P(y).

## Poznámka Anki 1790001406132

Karty Anki: 1790001406132
GUID: j_4I6a,#}H; štítky: (žádné).

### Otázka (Front)

Co v Bayes rule znamená prior P(x)?

### Odpověď (Back)

Belief o x před pozorováním y.

## Poznámka Anki 1790001406133

Karty Anki: 1790001406133
GUID: KFgs9fWej<; štítky: (žádné).

### Otázka (Front)

Co znamená likelihood P(y|x)?

### Odpověď (Back)

Jak pravděpodobné je pozorování y pro danou hypotézu x.

## Poznámka Anki 1790001406134

Karty Anki: 1790001406134
GUID: Rd&~(:Q45e; štítky: (žádné).

### Otázka (Front)

Co znamená posterior P(x|y)?

### Odpověď (Back)

Aktualizovaný belief o x po pozorování y.

## Poznámka Anki 1790001406135

Karty Anki: 1790001406135
GUID: m.D-91^G^*; štítky: (žádné).

### Otázka (Front)

Co znamená evidence P(y)?

### Odpověď (Back)

Normalizační term zajišťující, že posterior sumuje či integruje na 1.

## Poznámka Anki 1790001406136

Karty Anki: 1790001406136
GUID: PAic;4=p.<; štítky: (žádné).

### Otázka (Front)

Jak lze evidence P(y) vypočítat?

### Odpověď (Back)

Marginalizací hypotheses: P(y)=Σ_x P(y|x)P(x), případně integrálem.

## Poznámka Anki 1790001406137

Karty Anki: 1790001406137
GUID: u4HEue_mjZ; štítky: (žádné).

### Otázka (Front)

Proč se Bayes rule hodí při diagnosis?

### Odpověď (Back)

Umožňuje kombinovat prevalence hypothesis s citlivostí evidence a získat posterior probability po testu.

## Poznámka Anki 1790001406138

Karty Anki: 1790001406138
GUID: f,{<3<p;KP; štítky: (žádné).

### Otázka (Front)

Co znamená almost everywhere?

### Odpověď (Back)

Property platí všude kromě množiny measure zero.

## Poznámka Anki 1790001406139

Karty Anki: 1790001406139
GUID: rs/M)J:GUb; štítky: (žádné).

### Otázka (Front)

Proč může continuous density nabývat hodnot větších než 1?

### Odpověď (Back)

Density není probability bodu; pouze její integral přes region musí být nejvýše 1.

## Poznámka Anki 1790001406140

Karty Anki: 1790001406140
GUID: Fo]CtGU`HO; štítky: (žádné).

### Otázka (Front)

Co je self-information události x?

### Odpověď (Back)

I(x)=−log P(x); méně pravděpodobné události nesou více informace.

## Poznámka Anki 1790001406141

Karty Anki: 1790001406141
GUID: N:_1~kOf7+; štítky: (žádné).

### Otázka (Front)

Proč logarithm v self-information dává smysl?

### Odpověď (Back)

Information independent events se pak sčítá, protože −log P(x,y)=−log P(x)−log P(y) při independence.

## Poznámka Anki 1790001406142

Karty Anki: 1790001406142
GUID: BSZV9%}Lfv; štítky: (žádné).

### Otázka (Front)

Co je Shannon entropy H(P)?

### Odpověď (Back)

Expected self-information: H(P)=E_{x~P}[−log P(x)].

## Poznámka Anki 1790001406143

Karty Anki: 1790001406143
GUID: I;f|+-v6)D; štítky: (žádné).

### Otázka (Front)

Co entropy měří?

### Odpověď (Back)

Průměrnou uncertainty nebo information content random variable.

## Poznámka Anki 1790001406144

Karty Anki: 1790001406144
GUID: uQusJjE5`7; štítky: (žádné).

### Otázka (Front)

Kdy je entropy discrete distribution nulová?

### Odpověď (Back)

Když je distribution deterministic a jeden state má probability 1.

## Poznámka Anki 1790001406145

Karty Anki: 1790001406145
GUID: E-UirUOUGv; štítky: (žádné).

### Otázka (Front)

Kdy je entropy categorical distribution maximální?

### Odpověď (Back)

Při uniform distribution přes dostupné states.

## Poznámka Anki 1790001406146

Karty Anki: 1790001406146
GUID: p7PKWQUmFn; štítky: (žádné).

### Otázka (Front)

Co je differential entropy?

### Odpověď (Back)

Continuous analog entropy H(p)=−∫p(x)log p(x)dx; na rozdíl od discrete entropy může být záporná.

## Poznámka Anki 1790001406147

Karty Anki: 1790001406147
GUID: HC$X+I+U21; štítky: (žádné).

### Otázka (Front)

Co je Kullback–Leibler divergence D_KL(P||Q)?

### Odpověď (Back)

E_{x~P}[log(P(x)/Q(x))], míra rozdílu distribution Q od P z pohledu samples z P.

## Poznámka Anki 1790001406148

Karty Anki: 1790001406148
GUID: l>v{Q>bdi<; štítky: (žádné).

### Otázka (Front)

Je KL divergence symmetric?

### Odpověď (Back)

Ne; obecně D_KL(P||Q)≠D_KL(Q||P).

## Poznámka Anki 1790001406149

Karty Anki: 1790001406149
GUID: u%:De33-?]; štítky: (žádné).

### Otázka (Front)

Je KL divergence metrika?

### Odpověď (Back)

Ne, protože není symmetric a nesplňuje obecně triangle inequality.

## Poznámka Anki 1790001406150

Karty Anki: 1790001406150
GUID: vX$#)|V]ZX; štítky: (žádné).

### Otázka (Front)

Jaká základní non-negativity property platí pro KL divergence?

### Odpověď (Back)

D_KL(P||Q)≥0 a je 0 právě tehdy, když P=Q almost everywhere.

## Poznámka Anki 1790001406151

Karty Anki: 1790001406151
GUID: bYA[z8@ZQ*; štítky: (žádné).

### Otázka (Front)

Co je cross-entropy H(P,Q)?

### Odpověď (Back)

H(P,Q)=−E_{x~P}log Q(x).

## Poznámka Anki 1790001406152

Karty Anki: 1790001406152
GUID: Q~BugaWuVt; štítky: (žádné).

### Otázka (Front)

Jak souvisí cross-entropy, entropy a KL divergence?

### Odpověď (Back)

H(P,Q)=H(P)+D_KL(P||Q).

## Poznámka Anki 1790001406153

Karty Anki: 1790001406153
GUID: pwp09x]Giq; štítky: (žádné).

### Otázka (Front)

Proč minimalizace cross-entropy vzhledem k Q odpovídá minimalizaci KL divergence P||Q?

### Odpověď (Back)

H(P) je vzhledem k Q konstantní.

## Poznámka Anki 1790001406154

Karty Anki: 1790001406154
GUID: q}*c)k>S{|; štítky: (žádné).

### Otázka (Front)

Proč maximum likelihood souvisí s KL divergence?

### Odpověď (Back)

Maximalizace expected log p_model pod p_data je ekvivalentní minimalizaci D_KL(p_data||p_model).

## Poznámka Anki 1790001406155

Karty Anki: 1790001406155
GUID: wSK-Jeau:p; štítky: (žádné).

### Otázka (Front)

Co je structured probabilistic model?

### Odpověď (Back)

Probability distribution reprezentovaná grafem, který popisuje přímé interakce nebo conditional dependencies mezi random variables.

## Poznámka Anki 1790001406156

Karty Anki: 1790001406156
GUID: KIiczi7G)$; štítky: (žádné).

### Otázka (Front)

Co je directed graphical model?

### Odpověď (Back)

DAG, v němž joint distribution factorizes jako součin local conditionals každé variable given její parents.

## Poznámka Anki 1790001406157

Karty Anki: 1790001406157
GUID: PYRCM9^[Xy; štítky: (žádné).

### Otázka (Front)

Co je undirected graphical model?

### Odpověď (Back)

Graph, v němž joint distribution je úměrná součinu nonnegative factors nad cliques a vyžaduje globální normalization.

## Poznámka Anki 1790001406158

Karty Anki: 1790001406158
GUID: t0C9(:*Wwv; štítky: (žádné).

### Otázka (Front)

Proč graphical models pomáhají s high-dimensional distributions?

### Odpověď (Back)

Exploatují conditional independence a lokální factorization, takže není nutné explicitně parametrizovat probability každé kombinace variables.

## Poznámka Anki 1790001406159

Karty Anki: 1790001406159
GUID: B+]b_/1QRt; štítky: (žádné).

### Otázka (Front)

Co je latent variable?

### Odpověď (Back)

Random variable, která není přímo pozorována, ale pomáhá modelovat nebo vysvětlovat dependencies observed data.

## Poznámka Anki 1790001406160

Karty Anki: 1790001406160
GUID: pSW%i^6brq; štítky: (žádné).

### Otázka (Front)

Jaký rozdíl je mezi epistemic a aleatoric uncertainty v obecném smyslu?

### Odpověď (Back)

Epistemic uncertainty pochází z neznalosti modelu či parametrů a může klesat s daty; aleatoric uncertainty je inherentní stochasticity procesu.

## Poznámka Anki 1790001406161

Karty Anki: 1790001406161
GUID: Ifw`.jMmzG; štítky: (žádné).

### Otázka (Front)

Proč probability theory není pouze popis fyzické náhodnosti?

### Odpověď (Back)

Lze ji použít i k reprezentaci nedostatku znalostí o deterministickém systému.

## Poznámka Anki 1790001406162

Karty Anki: 1790001406162
GUID: m77<7v9NO7; štítky: (žádné).

### Otázka (Front)

Jaký princip vyjadřuje maximum entropy distribution?

### Odpověď (Back)

Při daných známých constraints má být zvolena distribution s nejvyšší entropy, aby nepřidávala nepodložené předpoklady.

## Poznámka Anki 1790001406163

Karty Anki: 1790001406163
GUID: w,B+fUP,3u; štítky: (žádné).

### Otázka (Front)

Proč je Gaussian maximum-entropy distribution při fixní mean a variance?

### Odpověď (Back)

Ze všech continuous distributions se stejnou mean a variance má nejvyšší differential entropy.

## Poznámka Anki 1790001406164

Karty Anki: 1790001406164
GUID: e/W7za.Oe+; štítky: (žádné).

### Otázka (Front)

Co znamená support probability distribution?

### Odpověď (Back)

Množina hodnot, kterým distribution přiřazuje nenulovou probability nebo density.

## Poznámka Anki 1790001406165

Karty Anki: 1790001406165
GUID: xCto9]D`Qy; štítky: (žádné).

### Otázka (Front)

Proč je support důležitý pro D_KL(P||Q)?

### Odpověď (Back)

Pokud P přiřazuje nenulovou probability regionu, kde Q=0, pak D_KL(P||Q)=∞.

## Poznámka Anki 1790001406166

Karty Anki: 1790001406166
GUID: w.6mT;On1H; štítky: (žádné).

### Otázka (Front)

Jak se independence promítá do expectation součinu?

### Odpověď (Back)

Pokud x a y jsou independent, E[xy]=E[x]E[y].

## Poznámka Anki 1790001406167

Karty Anki: 1790001406167
GUID: el-*[&zK|:; štítky: (žádné).

### Otázka (Front)

Co je conditional expectation E[x|y]?

### Odpověď (Back)

Expected value x podle conditional distribution p(x|y), tedy funkce pozorovaného y.

## Poznámka Anki 1790001406168

Karty Anki: 1790001406168
GUID: eVbBd,l^5!; štítky: (žádné).

### Otázka (Front)

Jak se law of total expectation vztahuje ke conditional expectation?

### Odpověď (Back)

E[x]=E_y[E[x|y]].

## Poznámka Anki 1790001406169

Karty Anki: 1790001406169
GUID: HjH]o%vMa<; štítky: (žádné).

### Otázka (Front)

Jak lze generative model interpretovat probabilisticky?

### Odpověď (Back)

Modeluje joint nebo marginal distribution dat a často umožňuje sampling nových observations.

## Poznámka Anki 1790001406170

Karty Anki: 1790001406170
GUID: HeEMOo*0JJ; štítky: (žádné).

### Otázka (Front)

Jak se discriminative model probabilisticky liší od generative modelu?

### Odpověď (Back)

Discriminative model typicky modeluje conditional p(y|x), zatímco generative model modeluje p(x,y) nebo p(x).

## Poznámka Anki 1790001406171

Karty Anki: 1790001406171
GUID: bMX&G$Z]Zt; štítky: (žádné).

### Otázka (Front)

Proč je numerical computation zásadní pro deep learning?

### Odpověď (Back)

Training a inference používají rozsáhlé numerical optimization a linear-algebra calculations, kde finite precision a computational cost zásadně ovlivňují výsledek.

## Poznámka Anki 1790001406172

Karty Anki: 1790001406172
GUID: E?xt50~(CV; štítky: (žádné).

### Otázka (Front)

Co je underflow ve floating-point arithmetic?

### Odpověď (Back)

Situace, kdy číslo s velmi malou absolutní hodnotou nelze reprezentovat a zaokrouhlí se typicky na 0.

## Poznámka Anki 1790001406173

Karty Anki: 1790001406173
GUID: eyQy;fT[bB; štítky: (žádné).

### Otázka (Front)

Proč je underflow problém při násobení probabilities?

### Odpověď (Back)

Součin mnoha malých probabilities může spadnout na 0, i když mathematically je nenulový.

## Poznámka Anki 1790001406174

Karty Anki: 1790001406174
GUID: bmp)#r]=c); štítky: (žádné).

### Otázka (Front)

Jak log-space computation zmírňuje underflow produktů probabilities?

### Odpověď (Back)

Produkty převede na součty logaritmů, které mají lépe reprezentovatelný numerical range.

## Poznámka Anki 1790001406175

Karty Anki: 1790001406175
GUID: m}EMz{V_=7; štítky: (žádné).

### Otázka (Front)

Co je overflow?

### Odpověď (Back)

Situace, kdy magnitude výsledku přesáhne největší reprezentovatelnou floating-point hodnotu a vznikne ±∞.

## Poznámka Anki 1790001406176

Karty Anki: 1790001406176
GUID: nsj?N8U|.p; štítky: (žádné).

### Otázka (Front)

Jaký numerical problém má naive softmax exp(z_i)/Σ_j exp(z_j)?

### Odpověď (Back)

Velké logits mohou způsobit overflow exponentials a velmi záporné logits underflow.

## Poznámka Anki 1790001406177

Karty Anki: 1790001406177
GUID: N#N_?-n}OA; štítky: (žádné).

### Otázka (Front)

Jak stabilizovat softmax vůči overflow?

### Odpověď (Back)

Odečíst od všech logits jejich maximum: softmax(z)=softmax(z−max_i z_i).

## Poznámka Anki 1790001406178

Karty Anki: 1790001406178
GUID: O_W$kCx<%(; štítky: (žádné).

### Otázka (Front)

Proč odečtení stejné konstanty od všech logits nemění softmax?

### Odpověď (Back)

Stejný multiplicative factor e^{-c} se objeví v numeratoru i denominatoru a zruší se.

## Poznámka Anki 1790001406179

Karty Anki: 1790001406179
GUID: hl(%%<Y/7o; štítky: (žádné).

### Otázka (Front)

Co je conditioning problemu?

### Odpověď (Back)

Citlivost výsledku matematické funkce na malé změny vstupu.

## Poznámka Anki 1790001406180

Karty Anki: 1790001406180
GUID: ja_=ZrpXNa; štítky: (žádné).

### Otázka (Front)

Co je condition number matrix vzhledem k inversion?

### Odpověď (Back)

Poměr největší a nejmenší singular value; velká hodnota znamená, že malé vstupní chyby mohou být silně zesíleny.

## Poznámka Anki 1790001406181

Karty Anki: 1790001406181
GUID: K=SCWH~bLY; štítky: (žádné).

### Otázka (Front)

Proč může být špatně podmíněný problém obtížný i s korektním algoritmem?

### Odpověď (Back)

Finite-precision perturbations vstupu se inherentně zesilují vlastností samotného problému.

## Poznámka Anki 1790001406182

Karty Anki: 1790001406182
GUID: w({_i$g>6}; štítky: (žádné).

### Otázka (Front)

Co je gradient scalar function f(x)?

### Odpověď (Back)

Vector partial derivatives ∇_x f, který ukazuje směr největšího lokálního růstu.

## Poznámka Anki 1790001406183

Karty Anki: 1790001406183
GUID: tq:AlGFnKU; štítky: (žádné).

### Otázka (Front)

Jaký směr nejrychleji lokálně snižuje differentiable function?

### Odpověď (Back)

Směr −∇f(x), tedy negative gradient.

## Poznámka Anki 1790001406184

Karty Anki: 1790001406184
GUID: E0At5|-KXa; štítky: (žádné).

### Otázka (Front)

Co je directional derivative ve směru unit vector u?

### Odpověď (Back)

uᵀ∇f(x).

## Poznámka Anki 1790001406185

Karty Anki: 1790001406185
GUID: DrmI0KJa}5; štítky: (žádné).

### Otázka (Front)

Proč negative gradient dává největší lokální pokles?

### Odpověď (Back)

Minimalizuje directional derivative mezi všemi unit directions.

## Poznámka Anki 1790001406186

Karty Anki: 1790001406186
GUID: Ol6$~IvX.Z; štítky: (žádné).

### Otázka (Front)

Co je critical point?

### Odpověď (Back)

Bod, kde gradient je nulový nebo nedefinovaný.

## Poznámka Anki 1790001406187

Karty Anki: 1790001406187
GUID: PdME$874{K; štítky: (žádné).

### Otázka (Front)

Jaké tři základní typy critical points rozlišujeme?

### Odpověď (Back)

Local minimum, local maximum a saddle point.

## Poznámka Anki 1790001406188

Karty Anki: 1790001406188
GUID: yAzl4{_.-a; štítky: (žádné).

### Otázka (Front)

Co je local minimum?

### Odpověď (Back)

Bod, jehož hodnota funkce není větší než hodnoty v dostatečně malém okolí.

## Poznámka Anki 1790001406189

Karty Anki: 1790001406189
GUID: H`3Cpk)8e_; štítky: (žádné).

### Otázka (Front)

Co je global minimum?

### Odpověď (Back)

Bod s nejmenší hodnotou funkce ze všech bodů v domain.

## Poznámka Anki 1790001406190

Karty Anki: 1790001406190
GUID: I%|ock:9aF; štítky: (žádné).

### Otázka (Front)

Co je saddle point?

### Odpověď (Back)

Critical point s nulovým gradientem a Hessianem obsahujícím kladné i záporné curvature directions.

## Poznámka Anki 1790001406191

Karty Anki: 1790001406191
GUID: kD7@p5m/I1; štítky: (žádné).

### Otázka (Front)

Jak funguje gradient descent?

### Odpověď (Back)

Iterativně aktualizuje x←x−ε∇f(x), kde ε je learning rate neboli step size.

## Poznámka Anki 1790001406192

Karty Anki: 1790001406192
GUID: mhKm53xk|@; štítky: (žádné).

### Otázka (Front)

Co určuje learning rate v gradient descent?

### Odpověď (Back)

Velikost kroku ve směru negative gradient.

## Poznámka Anki 1790001406193

Karty Anki: 1790001406193
GUID: FsS&DWigVR; štítky: (žádné).

### Otázka (Front)

Co se může stát při příliš velkém learning rate?

### Odpověď (Back)

Iterace mohou minimum přeskakovat, objective zvyšovat nebo divergovat.

## Poznámka Anki 1790001406194

Karty Anki: 1790001406194
GUID: brO3-EN[>e; štítky: (žádné).

### Otázka (Front)

Co se může stát při příliš malém learning rate?

### Odpověď (Back)

Convergence je velmi pomalá a optimization může během dostupného času zůstat daleko od dobrého řešení.

## Poznámka Anki 1790001406195

Karty Anki: 1790001406195
GUID: u=b4z%xxeu; štítky: (žádné).

### Otázka (Front)

Co je line search?

### Odpověď (Back)

Procedura volící step size podél zvoleného směru tak, aby dostatečně zlepšila objective.

## Poznámka Anki 1790001406196

Karty Anki: 1790001406196
GUID: PHs.kddILj; štítky: (žádné).

### Otázka (Front)

Co je Jacobian vector-valued function f:R^m→R^n?

### Odpověď (Back)

Matrix J_i,j=∂f_i/∂x_j.

## Poznámka Anki 1790001406197

Karty Anki: 1790001406197
GUID: AKf{f3zi/j; štítky: (žádné).

### Otázka (Front)

Jak gradient souvisí s Jacobianem?

### Odpověď (Back)

Gradient scalar-output function je zvláštní případ Jacobianu.

## Poznámka Anki 1790001406198

Karty Anki: 1790001406198
GUID: hE?O;PUnj>; štítky: (žádné).

### Otázka (Front)

Co je Hessian scalar function?

### Odpověď (Back)

Matrix druhých derivací H_i,j=∂²f/(∂x_i∂x_j).

## Poznámka Anki 1790001406199

Karty Anki: 1790001406199
GUID: sOWK4=9[bP; štítky: (žádné).

### Otázka (Front)

Kdy je Hessian symmetric?

### Odpověď (Back)

Když jsou příslušné druhé partial derivatives continuous, takže mixed derivatives lze zaměnit.

## Poznámka Anki 1790001406200

Karty Anki: 1790001406200
GUID: AjRjtQxOY!; štítky: (žádné).

### Otázka (Front)

Co vyjadřují eigenvalues Hessianu?

### Odpověď (Back)

Lokální curvature objective v příslušných eigenvector directions.

## Poznámka Anki 1790001406201

Karty Anki: 1790001406201
GUID: FCf}4Qm7=!; štítky: (žádné).

### Otázka (Front)

Co znamená positive Hessian eigenvalue v daném směru?

### Odpověď (Back)

Funkce má v tomto směru lokálně pozitivní curvature.

## Poznámka Anki 1790001406202

Karty Anki: 1790001406202
GUID: Qus~c{nHl^; štítky: (žádné).

### Otázka (Front)

Co znamená negative Hessian eigenvalue?

### Odpověď (Back)

Funkce má v daném směru negativní curvature.

## Poznámka Anki 1790001406203

Karty Anki: 1790001406203
GUID: h-q1Fln1O!; štítky: (žádné).

### Otázka (Front)

Jak Hessian charakterizuje strict local minimum v smooth critical pointu?

### Odpověď (Back)

Positive definite Hessian je sufficient condition pro strict local minimum.

## Poznámka Anki 1790001406204

Karty Anki: 1790001406204
GUID: P/qEjWa-Oq; štítky: (žádné).

### Otázka (Front)

Jak Hessian charakterizuje saddle point?

### Odpověď (Back)

Pokud má Hessian kladné i záporné eigenvalues, critical point je saddle.

## Poznámka Anki 1790001406205

Karty Anki: 1790001406205
GUID: j&e6Z_#!L#; štítky: (žádné).

### Otázka (Front)

Co je condition number Hessianu v positive-definite quadratic optimization?

### Odpověď (Back)

Poměr největší a nejmenší eigenvalue; velký poměr vede k obtížně optimalizovatelným protáhlým contours.

## Poznámka Anki 1790001406206

Karty Anki: 1790001406206
GUID: M*6_ug,72l; štítky: (žádné).

### Otázka (Front)

Proč špatně podmíněná curvature zpomaluje gradient descent?

### Odpověď (Back)

Step size dost malý pro steep direction vede k velmi malému progresu v shallow direction a trajectory zig-zaguje.

## Poznámka Anki 1790001406207

Karty Anki: 1790001406207
GUID: v`?WocS@|x; štítky: (žádné).

### Otázka (Front)

Co je second-order Taylor approximation f kolem x₀?

### Odpověď (Back)

f(x)≈f(x₀)+(x−x₀)ᵀ∇f(x₀)+½(x−x₀)ᵀH(x₀)(x−x₀).

## Poznámka Anki 1790001406208

Karty Anki: 1790001406208
GUID: NjtVQxPEtV; štítky: (žádné).

### Otázka (Front)

Jaký update používá Newton's method?

### Odpověď (Back)

x←x−H⁻¹∇f(x).

## Poznámka Anki 1790001406209

Karty Anki: 1790001406209
GUID: D?,B7BG>Hf; štítky: (žádné).

### Otázka (Front)

Proč Newton's method vyřeší positive-definite quadratic objective v jediném kroku?

### Odpověď (Back)

Second-order Taylor approximation je pro quadratic function přesná a její minimum lze analyticky nalézt pomocí H⁻¹∇f.

## Poznámka Anki 1790001406210

Karty Anki: 1790001406210
GUID: g[33h?,A}z; štítky: (žádné).

### Otázka (Front)

Proč Newton's method může být nebezpečný u saddle pointu?

### Odpověď (Back)

Hessian inverse může směrovat přímo ke critical pointu bez rozlišení, zda jde o minimum nebo saddle.

## Poznámka Anki 1790001406211

Karty Anki: 1790001406211
GUID: d^BjfxO<_5; štítky: (žádné).

### Otázka (Front)

Co je first-order optimization method?

### Odpověď (Back)

Metoda využívající hodnotu gradientu, ale ne Hessian; příkladem je gradient descent.

## Poznámka Anki 1790001406212

Karty Anki: 1790001406212
GUID: ej9Dl4:`oK; štítky: (žádné).

### Otázka (Front)

Co je second-order optimization method?

### Odpověď (Back)

Metoda využívající curvature informace z Hessianu nebo jeho aproximace; příkladem je Newton's method.

## Poznámka Anki 1790001406213

Karty Anki: 1790001406213
GUID: skE8Q,tQ3D; štítky: (žádné).

### Otázka (Front)

Co znamená Lipschitz continuity funkce f?

### Odpověď (Back)

Existuje L takové, že |f(x)−f(y)|≤L||x−y|| pro všechny x,y.

## Poznámka Anki 1790001406214

Karty Anki: 1790001406214
GUID: My@Jup-NZo; štítky: (žádné).

### Otázka (Front)

Proč je Lipschitz continuity užitečná v optimization?

### Odpověď (Back)

Omezuje rychlost změny funkce a poskytuje základ pro guarantees step sizes a convergence.

## Poznámka Anki 1790001406215

Karty Anki: 1790001406215
GUID: ge*&KYcjq}; štítky: (žádné).

### Otázka (Front)

Co je convex function?

### Odpověď (Back)

Funkce, jejíž epigraph je convex; ekvivalentně f(αx+(1−α)y)≤αf(x)+(1−α)f(y) pro α∈[0,1].

## Poznámka Anki 1790001406216

Karty Anki: 1790001406216
GUID: B5MvCzi=81; štítky: (žádné).

### Otázka (Front)

Jaký zásadní benefit má convex optimization?

### Odpověď (Back)

Každé local minimum je zároveň global minimum.

## Poznámka Anki 1790001406217

Karty Anki: 1790001406217
GUID: m{j#>bL_w@; štítky: (žádné).

### Otázka (Front)

Jak Hessian charakterizuje dvakrát diferencovatelnou convex function?

### Odpověď (Back)

Její Hessian je positive semidefinite v celé convex domain.

