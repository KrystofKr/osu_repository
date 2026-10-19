# Goodfellow – Blok 13 – karty 1201–1300

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001407118

Karty Anki: 1790001407118
GUID: dh:7qX>ZZe; štítky: (žádné).

### Otázka (Front)

Jaký meta-princip shrnuje structured probabilistic models?

### Odpověď (Back)

Explicitně reprezentovat pouze nezbytné direct interactions a využít graph-induced independences k redukci parameter, data a computational complexity.

## Poznámka Anki 1790001407119

Karty Anki: 1790001407119
GUID: f<mKv{<M&2; štítky: (žádné).

### Otázka (Front)

Co je Monte Carlo method?

### Odpověď (Back)

Randomized numerical method odhadující quantities pomocí samples a dovolující snižovat error větším computational budgetem.

## Poznámka Anki 1790001407120

Karty Anki: 1790001407120
GUID: fp,_L)*a;U; štítky: (žádné).

### Otázka (Front)

Jak se Monte Carlo algorithm liší od Las Vegas algorithmu?

### Odpověď (Back)

Monte Carlo vrací aproximaci s náhodnou chybou při omezeném budgetu; Las Vegas vrací správnou odpověď, ale používá náhodné množství resources nebo může opakovat práci.

## Poznámka Anki 1790001407121

Karty Anki: 1790001407121
GUID: t|ASxTMV&E; štítky: (žádné).

### Otázka (Front)

Jak se expectation E_p[f(x)] odhaduje ordinary Monte Carlo?

### Odpověď (Back)

ŝ=(1/n)Σ_i f(x^(i)) pro i.i.d. samples x^(i)~p.

## Poznámka Anki 1790001407122

Karty Anki: 1790001407122
GUID: ojzsb_B:{>; štítky: (žádné).

### Otázka (Front)

Je ordinary Monte Carlo sample average unbiased?

### Odpověď (Back)

Ano: E[ŝ]=E_p[f(x)].

## Poznámka Anki 1790001407123

Karty Anki: 1790001407123
GUID: x}&4=3?SHt; štítky: (žádné).

### Otázka (Front)

Jaká je variance average z n i.i.d. samples?

### Odpověď (Back)

Var(ŝ)=Var(f(x))/n.

## Poznámka Anki 1790001407124

Karty Anki: 1790001407124
GUID: &jn+1/s-L; štítky: (žádné).

### Otázka (Front)

Jak se standard error mění s počtem samples n?

### Odpověď (Back)

Klesá jako 1/√n.

## Poznámka Anki 1790001407125

Karty Anki: 1790001407125
GUID: KF/6$R5GJg; štítky: (žádné).

### Otázka (Front)

Jaký praktický důsledek má 1/√n scaling?

### Odpověď (Back)

Desetinásobné snížení standard error vyžaduje přibližně stonásobek samples.

## Poznámka Anki 1790001407126

Karty Anki: 1790001407126
GUID: At:xnyBH-`; štítky: (žádné).

### Otázka (Front)

Co zaručuje law of large numbers?

### Odpověď (Back)

Při vhodných podmínkách sample average konverguje k true expectation s rostoucím n.

## Poznámka Anki 1790001407127

Karty Anki: 1790001407127
GUID: x%{9qVv87W; štítky: (žádné).

### Otázka (Front)

Co poskytuje central limit theorem pro Monte Carlo?

### Odpověď (Back)

Pro velké n je sampling distribution average přibližně Gaussian, což umožňuje approximate confidence intervals.

## Poznámka Anki 1790001407128

Karty Anki: 1790001407128
GUID: c`6x(85}{d; štítky: (žádné).

### Otázka (Front)

Co je importance sampling?

### Odpověď (Back)

Monte Carlo metoda sampleující z proposal q místo target p a korigující rozdíl pomocí importance weights.

## Poznámka Anki 1790001407129

Karty Anki: 1790001407129
GUID: pR{T7OJhRJ; štítky: (žádné).

### Otázka (Front)

Jaký importance weight se používá?

### Odpověď (Back)

w(x)=p(x)/q(x).

## Poznámka Anki 1790001407130

Karty Anki: 1790001407130
GUID: t<qBS,W^.T; štítky: (žádné).

### Otázka (Front)

Jak vypadá importance-sampling estimator E_p[f]?

### Odpověď (Back)

(1/n)Σ_i [p(x_i)/q(x_i)]f(x_i), kde x_i~q.

## Poznámka Anki 1790001407131

Karty Anki: 1790001407131
GUID: zw:SYqd&A[; štítky: (žádné).

### Otázka (Front)

Kdy je importance sampling validní?

### Odpověď (Back)

Proposal q musí mít nonzero probability všude, kde integrand pod p může významně přispívat.

## Poznámka Anki 1790001407132

Karty Anki: 1790001407132
GUID: P(km(}>dX~; štítky: (žádné).

### Otázka (Front)

Jaká proposal minimalizuje variance v ideálním importance samplingu?

### Odpověď (Back)

q*(x)∝p(x)|f(x)|.

## Poznámka Anki 1790001407133

Karty Anki: 1790001407133
GUID: fSXGHdV+F#; štítky: (žádné).

### Otázka (Front)

Proč q* není obvykle prakticky dostupná?

### Odpověď (Back)

Její normalizace a konstrukce vyžaduje znalost quantity/integrandu, jehož obtížný výpočet právě řešíme.

## Poznámka Anki 1790001407134

Karty Anki: 1790001407134
GUID: r!6)HkipM/; štítky: (žádné).

### Otázka (Front)

Co se stane, když q špatně překrývá důležité regions p?

### Odpověď (Back)

Importance weights budou extrémně variabilní a estimator může mít obrovskou variance.

## Poznámka Anki 1790001407135

Karty Anki: 1790001407135
GUID: fd<e?5wRRH; štítky: (žádné).

### Otázka (Front)

Proč high-dimensional importance sampling často selhává?

### Odpověď (Back)

Overlap jednoduché proposal s komplexní target distribution se s dimensionality dramaticky zhoršuje.

## Poznámka Anki 1790001407136

Karty Anki: 1790001407136
GUID: qJ7);d}QbY; štítky: (žádné).

### Otázka (Front)

Co je self-normalized neboli biased importance sampling?

### Odpověď (Back)

Estimator používající normalizované weights w_i/Σ_jw_j místo známé normalizační konstanty.

## Poznámka Anki 1790001407137

Karty Anki: 1790001407137
GUID: Rid;L|QLF~; štítky: (žádné).

### Otázka (Front)

Jaká je výhoda self-normalized importance sampling?

### Odpověď (Back)

Může pracovat s unnormalized target density, protože neznámý common normalizer se zkrátí.

## Poznámka Anki 1790001407138

Karty Anki: 1790001407138
GUID: J~,y9]SB$K; štítky: (žádné).

### Otázka (Front)

Je self-normalized importance estimator unbiased?

### Odpověď (Back)

Ne pro finite sample, ale za běžných podmínek je consistent.

## Poznámka Anki 1790001407139

Karty Anki: 1790001407139
GUID: P0NCo?I-dc; štítky: (žádné).

### Otázka (Front)

Co je Markov chain Monte Carlo (MCMC)?

### Odpověď (Back)

Sampling methods používající Markov chain s target distribution jako stationary distribution.

## Poznámka Anki 1790001407140

Karty Anki: 1790001407140
GUID: jg<:RI_b<; štítky: (žádné).

### Otázka (Front)

Co je Markov property?

### Odpověď (Back)

Next state distribution závisí na current state, ne na celé explicitní historii chainu.

## Poznámka Anki 1790001407141

Karty Anki: 1790001407141
GUID: Ptu4cEZZB?; štítky: (žádné).

### Otázka (Front)

Co je transition distribution T(x'|x)?

### Odpověď (Back)

Probability law určující next state x' given current x.

## Poznámka Anki 1790001407142

Karty Anki: 1790001407142
GUID: sS;.U5KEPp; štítky: (žádné).

### Otázka (Front)

Co je stationary distribution q chainu?

### Odpověď (Back)

Distribution, která se transition operatoru nemění.

## Poznámka Anki 1790001407143

Karty Anki: 1790001407143
GUID: uI<-Onr8MB; štítky: (žádné).

### Otázka (Front)

Jak se stationary condition zapisuje?

### Odpověď (Back)

q(x')=Σ_x q(x)T(x'|x), případně integrálem.

## Poznámka Anki 1790001407144

Karty Anki: 1790001407144
GUID: c~X(m&Y#!T; štítky: (žádné).

### Otázka (Front)

Jaký cíl má MCMC design?

### Odpověď (Back)

Zvolit transition operator, jehož stationary distribution je požadované p(x), a který k ní rychle konverguje.

## Poznámka Anki 1790001407145

Karty Anki: 1790001407145
GUID: w|lxW&-pk0; štítky: (žádné).

### Otázka (Front)

Co je burn-in?

### Odpověď (Back)

Initial transitions zahazované před sběrem samples, aby se oslabil vliv arbitrary initialization.

## Poznámka Anki 1790001407146

Karty Anki: 1790001407146
GUID: jWq0C](0q@; štítky: (žádné).

### Otázka (Front)

Proč MCMC samples nejsou i.i.d.?

### Odpověď (Back)

Successive states vznikají local transition z previous state a jsou proto correlated.

## Poznámka Anki 1790001407147

Karty Anki: 1790001407147
GUID: eeUX0WA?FL; štítky: (žádné).

### Otázka (Front)

Jak correlation ovlivňuje effective sample size?

### Odpověď (Back)

n correlated samples obsahuje méně information než n independent samples.

## Poznámka Anki 1790001407148

Karty Anki: 1790001407148
GUID: FTic&^|/^g; štítky: (žádné).

### Otázka (Front)

Co je mixing time?

### Odpověď (Back)

Doba/transitions potřebné, aby distribution chainu byla dostatečně blízko stationary target distribution.

## Poznámka Anki 1790001407149

Karty Anki: 1790001407149
GUID: PRPq1OOiIn; štítky: (žádné).

### Otázka (Front)

Proč je mixing time obtížné v praxi ověřit?

### Odpověď (Back)

Target high-dimensional distribution i transition matrix nejsou explicitně dostupné a finite chain může vypadat stabilně, i když neprozkoumala jiné modes.

## Poznámka Anki 1790001407150

Karty Anki: 1790001407150
GUID: u+[ty1Ae:7; štítky: (žádné).

### Otázka (Front)

Jak second-largest eigenvalue souvisí s mixing v finite-state idealizaci?

### Odpověď (Back)

Její magnitude určuje, jak rychle zanikají dominantní nonstationary components distribution.

## Poznámka Anki 1790001407151

Karty Anki: 1790001407151
GUID: n@QY6Y~wDe; štítky: (žádné).

### Otázka (Front)

Proč graphical-model structure usnadňuje Gibbs sampling?

### Odpověď (Back)

Conditional jednoho node typicky závisí jen na jeho Markov blanket/neighbors.

## Poznámka Anki 1790001407152

Karty Anki: 1790001407152
GUID: MaB$&m-vaE; štítky: (žádné).

### Otázka (Front)

Proč block Gibbs může mixovat lépe než single-site Gibbs?

### Odpověď (Back)

Coordinovaně změní correlated variables bez průchodu low-probability intermediate states.

## Poznámka Anki 1790001407153

Karty Anki: 1790001407153
GUID: kH2Ewqr>~P; štítky: (žádné).

### Otázka (Front)

Jak RBM využívá block Gibbs?

### Odpověď (Back)

Alternativně sampleuje celou hidden layer given visible a celou visible layer given hidden.

## Poznámka Anki 1790001407154

Karty Anki: 1790001407154
GUID: bXE)Z5)&*2; štítky: (žádné).

### Otázka (Front)

Co je hlavní praktický problém MCMC v multimodal distributions?

### Odpověď (Back)

Chain může zůstat dlouho uvězněný v jednom mode a velmi zřídka překoná low-probability barriers.

## Poznámka Anki 1790001407155

Karty Anki: 1790001407155
GUID: LIC3suBBwa; štítky: (žádné).

### Otázka (Front)

Co je energy barrier?

### Odpověď (Back)

High-energy/low-probability region oddělující dva high-probability modes.

## Poznámka Anki 1790001407156

Karty Anki: 1790001407156
GUID: yr!beum3oN; štítky: (žádné).

### Otázka (Front)

Proč local transitions obtížně překonávají energy barrier?

### Odpověď (Back)

Musí postupně navštívit velmi nepravděpodobné intermediate states.

## Poznámka Anki 1790001407157

Karty Anki: 1790001407157
GUID: kAS/U!d0!); štítky: (žádné).

### Otázka (Front)

Jak jednoduchý strongly correlated binary pair ilustruje slow mixing?

### Odpověď (Back)

Pokud jsou high-probability pouze (+,+) a (−,−), single-bit Gibbs musí přes low-probability mismatched state, takže změna mode je vzácná.

## Poznámka Anki 1790001407158

Karty Anki: 1790001407158
GUID: h@)vP84!Su; štítky: (žádné).

### Otázka (Front)

Jaký conflict může existovat mezi informative latent representation a Gibbs mixing?

### Odpověď (Back)

Pokud h téměř deterministicky určuje x a naopak, alternating Gibbs se může vracet k téměř stejnému state a mixovat pomalu.

## Poznámka Anki 1790001407159

Karty Anki: 1790001407159
GUID: hWjo1z9k(/; štítky: (žádné).

### Otázka (Front)

Co je tempering?

### Odpověď (Back)

Sampling strategy využívající flatter high-temperature versions target distribution ke snazším přechodům mezi modes.

## Poznámka Anki 1790001407160

Karty Anki: 1790001407160
GUID: rCdGEvL4{9; štítky: (žádné).

### Otázka (Front)

Jak se temperature zavádí do EBM?

### Odpověď (Back)

p_β(x)∝exp(−βE(x)), kde β je inverse temperature.

## Poznámka Anki 1790001407161

Karty Anki: 1790001407161
GUID: Lr;]-{n|(L; štítky: (žádné).

### Otázka (Front)

Co způsobí β<1?

### Odpověď (Back)

Zploští distribution a sníží relativní energy barriers.

## Poznámka Anki 1790001407162

Karty Anki: 1790001407162
GUID: h(RT2#uJu|; štítky: (žádné).

### Otázka (Front)

Co způsobí β→0 v finite discrete space?

### Odpověď (Back)

Distribution se blíží uniformní.

## Poznámka Anki 1790001407163

Karty Anki: 1790001407163
GUID: G,m:1h0WLk; štítky: (žádné).

### Otázka (Front)

Co je parallel tempering?

### Odpověď (Back)

Současný běh chains při více temperatures s občasnými swaps states mezi sousedními temperatures.

## Poznámka Anki 1790001407164

Karty Anki: 1790001407164
GUID: e*^)|QvjP+; štítky: (žádné).

### Otázka (Front)

Jak parallel tempering pomáhá target-temperature chain?

### Odpověď (Back)

High-temperature chain snáze změní mode a swap může tuto configuration přenést k β=1.

## Poznámka Anki 1790001407165

Karty Anki: 1790001407165
GUID: G<{9`wnqO&; štítky: (žádné).

### Otázka (Front)

Co jsou tempered transitions?

### Odpověď (Back)

Jedna chain dočasně projde sérií vyšších temperatures a vrátí se k target temperature, aby mohla změnit mode.

## Poznámka Anki 1790001407166

Karty Anki: 1790001407166
GUID: w@d*xbu7SB; štítky: (žádné).

### Otázka (Front)

Proč tempering není univerzální řešení?

### Odpověď (Back)

Může vyžadovat velmi jemné temperature schedules, zvlášť kolem critical temperatures, a zůstává computationally nákladné.

## Poznámka Anki 1790001407167

Karty Anki: 1790001407167
GUID: n{}biiLMg>; štítky: (žádné).

### Otázka (Front)

Jak depth může hypoteticky pomáhat mixing?

### Odpověď (Back)

Higher-level representation může data distribution 'rozvinout' tak, že modes jsou v latent space méně oddělené.

## Poznámka Anki 1790001407168

Karty Anki: 1790001407168
GUID: gw53E;]lMY; štítky: (žádné).

### Otázka (Front)

Co bylo empiricky pozorováno u hlubších RBM/autoencoder representations?

### Odpověď (Back)

Top-level distributions mohly být více spread out a Gibbs sampling mezi semantic modes rychlejší.

## Poznámka Anki 1790001407169

Karty Anki: 1790001407169
GUID: ek,0+%!m:U; štítky: (žádné).

### Otázka (Front)

Jaký meta-princip shrnuje Monte Carlo chapter?

### Odpověď (Back)

Intractable expectations lze aproximovat samplingem, ale kvalita závisí nejen na počtu samples, nýbrž i na tom, zda sampling mechanism skutečně pokrývá target distribution.

## Poznámka Anki 1790001407170

Karty Anki: 1790001407170
GUID: f6,{Sq-Ybc; štítky: (žádné).

### Otázka (Front)

Proč maximum-likelihood training undirected modelu obsahuje obtížný term?

### Odpověď (Back)

Log-likelihood log p(x)=log p̃(x)−log Z a partition function Z závisí na model parameters.

## Poznámka Anki 1790001407171

Karty Anki: 1790001407171
GUID: D1M-VM<Io^; štítky: (žádné).

### Otázka (Front)

Jak se rozkládá gradient log-likelihood undirected modelu?

### Odpověď (Back)

∇θlog p(x)=∇θlog p̃(x)−∇θlog Z.

## Poznámka Anki 1790001407172

Karty Anki: 1790001407172
GUID: H9]n`9=!j<; štítky: (žádné).

### Otázka (Front)

Co je positive phase?

### Odpověď (Back)

Term zvyšující unnormalized probability training examples.

## Poznámka Anki 1790001407173

Karty Anki: 1790001407173
GUID: c*dCY|F*+g; štítky: (žádné).

### Otázka (Front)

Co je negative phase?

### Odpověď (Back)

Term snižující relative probability states, kterým current model přiděluje vysokou probability, a tím kontrolující normalization.

## Poznámka Anki 1790001407174

Karty Anki: 1790001407174
GUID: qlxz8W6elY; štítky: (žádné).

### Otázka (Front)

Jak lze gradient log Z vyjádřit?

### Odpověď (Back)

∇θ log Z=E_{x~p_model}[∇θ log p̃(x)].

## Poznámka Anki 1790001407175

Karty Anki: 1790001407175
GUID: kbp[|%TW6z; štítky: (žádné).

### Otázka (Front)

Proč je negative phase obtížná?

### Odpověď (Back)

Vyžaduje expectation/samples z current model distribution, která sama může být obtížně sampleovatelná.

## Poznámka Anki 1790001407176

Karty Anki: 1790001407176
GUID: n5FwWn:iv_; štítky: (žádné).

### Otázka (Front)

Jak se positive a negative phase interpretují v EBM?

### Odpověď (Back)

Positive phase snižuje energy dat, negative phase zvyšuje energy modelových fantasy states.

## Poznámka Anki 1790001407177

Karty Anki: 1790001407177
GUID: eJp:u_l#!n; štítky: (žádné).

### Otázka (Front)

Proč samotná positive phase nestačí?

### Odpověď (Back)

Model by mohl zvyšovat p̃ téměř všude bez správné redistribuce normalized probability mass.

## Poznámka Anki 1790001407178

Karty Anki: 1790001407178
GUID: p5|GT0]L8s; štítky: (žádné).

### Otázka (Front)

Co jsou fantasy particles?

### Odpověď (Back)

Samples z model distribution používané k aproximaci negative phase.

## Poznámka Anki 1790001407179

Karty Anki: 1790001407179
GUID: z_}vsLFD73; štítky: (žádné).

### Otázka (Front)

Co je contrastive divergence (CD)?

### Odpověď (Back)

Approximate training metoda spouštějící krátké MCMC chains z training examples místo z random initialization/equilibrium.

## Poznámka Anki 1790001407180

Karty Anki: 1790001407180
GUID: O)leM0j]`[; štítky: (žádné).

### Otázka (Front)

Co znamená CD-k?

### Odpověď (Back)

Každá negative-phase chain provede k MCMC transitions od data pointu.

## Poznámka Anki 1790001407181

Karty Anki: 1790001407181
GUID: eG[R-0LLIw; štítky: (žádné).

### Otázka (Front)

Proč CD může být levnější než exact/long-run MCMC maximum likelihood?

### Odpověď (Back)

Data initialization omezuje burn-in a používá jen několik transitions.

## Poznámka Anki 1790001407182

Karty Anki: 1790001407182
GUID: m^L5TGk9&I; štítky: (žádné).

### Otázka (Front)

Proč je CD biased?

### Odpověď (Back)

Distribution po krátké chain z data obecně není current model distribution.

## Poznámka Anki 1790001407183

Karty Anki: 1790001407183
GUID: KF;_]&sX>W; štítky: (žádné).

### Otázka (Front)

Co je spurious mode?

### Odpověď (Back)

High-probability region modelu, který neodpovídá data distribution.

## Poznámka Anki 1790001407184

Karty Anki: 1790001407184
GUID: i)j^)pQT8h; štítky: (žádné).

### Otázka (Front)

Proč CD může spurious mode přehlédnout?

### Odpověď (Back)

Short chains začínající na datech jej nemusí nikdy navštívit, takže negative phase jej nepotlačí.

## Poznámka Anki 1790001407185

Karty Anki: 1790001407185
GUID: k`]--ZC63,; štítky: (žádné).

### Otázka (Front)

Je CD update obecně gradientem fixed scalar objective?

### Odpověď (Back)

Ne; jeho vector field nemusí být integrable jako gradient jediné objective.

## Poznámka Anki 1790001407186

Karty Anki: 1790001407186
GUID: F2)Gx@w3v%; štítky: (žádné).

### Otázka (Front)

Co je stochastic maximum likelihood (SML)?

### Odpověď (Back)

Training udržující persistent MCMC chains napříč parameter updates pro approximation negative phase.

## Poznámka Anki 1790001407187

Karty Anki: 1790001407187
GUID: iw?,:SjP=2; štítky: (žádné).

### Otázka (Front)

Jaký jiný název má SML?

### Odpověď (Back)

Persistent contrastive divergence (PCD).

## Poznámka Anki 1790001407188

Karty Anki: 1790001407188
GUID: oHA7zY{d1P; štítky: (žádné).

### Otázka (Front)

Jaký je hlavní rozdíl mezi CD a PCD?

### Odpověď (Back)

CD restartuje chains na datech; PCD pokračuje z previous fantasy states.

## Poznámka Anki 1790001407189

Karty Anki: 1790001407189
GUID: g`IP:#~uyT; štítky: (žádné).

### Otázka (Front)

Proč persistence šetří burn-in?

### Odpověď (Back)

Pokud se parameters mezi updates mění jen málo, previous samples jsou stále blízko nové model distribution.

## Poznámka Anki 1790001407190

Karty Anki: 1790001407190
GUID: i>XL!<1)1h; štítky: (žádné).

### Otázka (Front)

Jaký klíčový assumption PCD vyžaduje?

### Odpověď (Back)

Model se musí měnit pomaleji, než chains stíhají mixovat.

## Poznámka Anki 1790001407191

Karty Anki: 1790001407191
GUID: Kb$2W_EcB6; štítky: (žádné).

### Otázka (Front)

Jak může příliš velký learning rate poškodit PCD?

### Odpověď (Back)

Target distribution se mezi steps změní příliš výrazně a persistent particles ji nestihnou sledovat.

## Poznámka Anki 1790001407192

Karty Anki: 1790001407192
GUID: sur`/A#({W; štítky: (žádné).

### Otázka (Front)

Proč PCD lépe odhaluje vzdálené spurious modes než CD?

### Odpověď (Back)

Chains nejsou po každém update resetovány k data manifold a mohou dlouhodobě prozkoumávat model space.

## Poznámka Anki 1790001407193

Karty Anki: 1790001407193
GUID: Ey<aW6b!9[; štítky: (žádné).

### Otázka (Front)

Co je fast persistent contrastive divergence (FPCD)?

### Odpověď (Back)

PCD varianta s additional fast parameters, které se rychle mění a pomáhají particles opouštět current modes.

## Poznámka Anki 1790001407194

Karty Anki: 1790001407194
GUID: gwGcJZe<%/; štítky: (žádné).

### Otázka (Front)

Proč fast parameters silně decayují?

### Odpověď (Back)

Mají být transient mechanism pro mixing, nikoli dlouhodobá reprezentace target distribution.

## Poznámka Anki 1790001407195

Karty Anki: 1790001407195
GUID: vt!zovyltR; štítky: (žádné).

### Otázka (Front)

Co je pseudolikelihood?

### Odpověď (Back)

Objective Σ_i log p(x_i|x_−i), který nahrazuje full joint likelihood local conditional likelihoods.

## Poznámka Anki 1790001407196

Karty Anki: 1790001407196
GUID: s/oA-AJ@R#; štítky: (žádné).

### Otázka (Front)

Proč pseudolikelihood nepotřebuje globální Z?

### Odpověď (Back)

Partition function se v conditional ratio numerator/denominator zruší.

## Poznámka Anki 1790001407197

Karty Anki: 1790001407197
GUID: f_~Qge~8u?; štítky: (žádné).

### Otázka (Front)

Jaký computational scaling má discrete pseudolikelihood oproti full table?

### Odpověď (Back)

Místo k^n global configurations často vyžaduje zhruba O(nk) local evaluations.

## Poznámka Anki 1790001407198

Karty Anki: 1790001407198
GUID: Jdzu0cTC:^; štítky: (žádné).

### Otázka (Front)

Je pseudolikelihood asymptotically consistent?

### Odpověď (Back)

Za vhodných conditions ano, přesto může mít finite-sample behavior odlišné od MLE.

## Poznámka Anki 1790001407199

Karty Anki: 1790001407199
GUID: x_ei(T`(};; štítky: (žádné).

### Otázka (Front)

Co je generalized pseudolikelihood?

### Odpověď (Back)

Objective používající conditionals p(x_S|x_−S) pro subsets S místo singleton variables.

## Poznámka Anki 1790001407200

Karty Anki: 1790001407200
GUID: LnuA9C9ylK; štítky: (žádné).

### Otázka (Front)

Jak generalized pseudolikelihood interpoluje mezi local a full likelihood?

### Odpověď (Back)

Malé subsets dávají levné local objectives; S obsahující všechny variables odpovídá full likelihood.

## Poznámka Anki 1790001407201

Karty Anki: 1790001407201
GUID: FOJQpBoOQl; štítky: (žádné).

### Otázka (Front)

Pro jaký task může pseudolikelihood přirozeně fungovat dobře?

### Odpověď (Back)

Prediction malého počtu missing variables given většiny observed variables.

## Poznámka Anki 1790001407202

Karty Anki: 1790001407202
GUID: ArM|ZyhS.U; štítky: (žádné).

### Otázka (Front)

Proč pseudolikelihood nemusí vytvořit nejlepší unconstrained sampler?

### Odpověď (Back)

Optimalizuje local conditionals a finite-sample optimum nemusí dobře odpovídat global joint distribution.

## Poznámka Anki 1790001407203

Karty Anki: 1790001407203
GUID: hLXg<KXV_`; štítky: (žádné).

### Otázka (Front)

Co je score matching?

### Odpověď (Back)

Training criterion porovnávající score ∇_x log p_model(x) se score data distribution.

## Poznámka Anki 1790001407204

Karty Anki: 1790001407204
GUID: Q~pJ7+VvVI; štítky: (žádné).

### Otázka (Front)

Proč score matching odstraňuje partition function?

### Odpověď (Back)

log Z nezávisí na x, takže jeho derivative podle x je nulová.

## Poznámka Anki 1790001407205

Karty Anki: 1790001407205
GUID: QR0S5crAz|; štítky: (žádné).

### Otázka (Front)

Jaký problém má naive score-matching objective?

### Odpověď (Back)

Obsahuje neznámé ∇_x log p_data(x).

## Poznámka Anki 1790001407206

Karty Anki: 1790001407206
GUID: e+nOr6$2>C; štítky: (žádné).

### Otázka (Front)

Jak se score matching přepíše do tractable formy?

### Odpověď (Back)

Integration by parts převede objective na expectation přes data obsahující first a second derivatives log p_model.

## Poznámka Anki 1790001407207

Karty Anki: 1790001407207
GUID: hj?G)BX)QD; štítky: (žádné).

### Otázka (Front)

Pro jaké observed variables je standardní score matching vhodný?

### Odpověď (Back)

Continuous variables, protože vyžaduje derivatives podle x.

## Poznámka Anki 1790001407208

Karty Anki: 1790001407208
GUID: Q%}|*5ss|F; štítky: (žádné).

### Otázka (Front)

Co je ratio matching?

### Odpověď (Back)

Discrete analog založený na ratios probabilities neighboring states, ve kterých se partition function zruší.

## Poznámka Anki 1790001407209

Karty Anki: 1790001407209
GUID: bY}&;W><tf; štítky: (žádné).

### Otázka (Front)

Jaký neighborhood se typicky používá u binary ratio matching?

### Odpověď (Back)

States lišící se od training example flipnutím jednoho bitu.

## Poznámka Anki 1790001407210

Karty Anki: 1790001407210
GUID: kIqhUiMiy8; štítky: (žádné).

### Otázka (Front)

Jaký local-negative-phase pohled mají pseudolikelihood, score a ratio matching?

### Odpověď (Back)

Místo global model samples porovnávají data s nearby alternative configurations.

## Poznámka Anki 1790001407211

Karty Anki: 1790001407211
GUID: CGk+`os6J,; štítky: (žádné).

### Otázka (Front)

Co je denoising score matching?

### Odpověď (Back)

Score matching na smoothed data distribution vzniklé corruption/noise procesem.

## Poznámka Anki 1790001407212

Karty Anki: 1790001407212
GUID: hvvuCyg(b9; štítky: (žádné).

### Otázka (Front)

Proč smoothing regularizuje density estimation?

### Odpověď (Back)

Brání estimatoru vytvořit extrémně ostré peaks přes finite training examples.

## Poznámka Anki 1790001407213

Karty Anki: 1790001407213
GUID: G#qYZ&5D7a; štítky: (žádné).

### Otázka (Front)

Jak denoising score matching souvisí s denoising autoencoders?

### Odpověď (Back)

Některé DAE reconstruction objectives jsou ekvivalentní odhadu score smoothed data density.

## Poznámka Anki 1790001407214

Karty Anki: 1790001407214
GUID: s[IljpN!iU; štítky: (žádné).

### Otázka (Front)

Co je noise-contrastive estimation (NCE)?

### Odpověď (Back)

Metoda převádějící density estimation na binary classification mezi data samples a samples z known noise distribution.

## Poznámka Anki 1790001407215

Karty Anki: 1790001407215
GUID: G~eW6=@GBN; štítky: (žádné).

### Otázka (Front)

Jak NCE zachází s neznámým log Z?

### Odpověď (Back)

Zavede samostatný parameter c≈−log Z a učí jej spolu s model parameters.

## Poznámka Anki 1790001407216

Karty Anki: 1790001407216
GUID: w%Lhjz,Fj3; štítky: (žádné).

### Otázka (Front)

Jaký classifier používá NCE?

### Odpověď (Back)

Logistic classifier založený na rozdílu log p_model(x)−log p_noise(x), případně s class-prior correction.

## Poznámka Anki 1790001407217

Karty Anki: 1790001407217
GUID: erA_:_j]FH; štítky: (žádné).

### Otázka (Front)

Proč NCE může být consistent estimator?

### Odpověď (Back)

Classification problem je zkonstruován tak, že jeho population optimum obnovuje true data/model density ratio a normalization.

