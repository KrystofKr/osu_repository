# Goodfellow – Blok 04 – karty 301–400

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001406218

Karty Anki: 1790001406218
GUID: wAG#;1J1{); štítky: (žádné).

### Otázka (Front)

Co je constrained optimization?

### Odpověď (Back)

Optimalizace objective f(x) při požadavku, aby x splňovalo equality nebo inequality constraints.

## Poznámka Anki 1790001406219

Karty Anki: 1790001406219
GUID: HbT;^!}9~A; štítky: (žádné).

### Otázka (Front)

Co je Lagrangian pro equality-constrained problem?

### Odpověď (Back)

L(x,λ)=f(x)+Σ_i λ_i g_i(x), kde g_i(x)=0 jsou constraints.

## Poznámka Anki 1790001406220

Karty Anki: 1790001406220
GUID: j3HdS6wQ!I; štítky: (žádné).

### Otázka (Front)

Co je Lagrange multiplier?

### Odpověď (Back)

Proměnná λ_i vyjadřující citlivost optimum objective na příslušný constraint.

## Poznámka Anki 1790001406221

Karty Anki: 1790001406221
GUID: fPj/=SAG(!; štítky: (žádné).

### Otázka (Front)

Jak se do Lagrangianu přidávají inequality constraints h_j(x)≤0?

### Odpověď (Back)

Pomocí multipliers α_j≥0, tedy L=f+Σλ_i g_i+Σα_j h_j.

## Poznámka Anki 1790001406222

Karty Anki: 1790001406222
GUID: Gk`<`Bp}PW; štítky: (žádné).

### Otázka (Front)

Co jsou Karush–Kuhn–Tucker conditions?

### Odpověď (Back)

Nutné podmínky optimality zahrnující primal feasibility, dual feasibility, stationarity a complementary slackness; u vhodných convex problems jsou také sufficient.

## Poznámka Anki 1790001406223

Karty Anki: 1790001406223
GUID: qu7KH_Emi_; štítky: (žádné).

### Otázka (Front)

Co je complementary slackness?

### Odpověď (Back)

Pro inequality constraint h_i(x)≤0 a multiplier α_i≥0 platí α_i h_i(x)=0.

## Poznámka Anki 1790001406224

Karty Anki: 1790001406224
GUID: JpPH1WGV<O; štítky: (žádné).

### Otázka (Front)

Co znamená active inequality constraint?

### Odpověď (Back)

Constraint, který je v solution splněn s rovností h_i(x)=0.

## Poznámka Anki 1790001406225

Karty Anki: 1790001406225
GUID: rTRE[(a62$; štítky: (žádné).

### Otázka (Front)

Jaký vztah má least squares k numerical optimization?

### Odpověď (Back)

Minimization ||Ax−b||₂² vede k normal equations AᵀAx=Aᵀb, ale numericky jsou často vhodnější QR nebo SVD solvery.

## Poznámka Anki 1790001406226

Karty Anki: 1790001406226
GUID: k42R2`L<!e; štítky: (žádné).

### Otázka (Front)

Proč mohou normal equations zhoršit conditioning?

### Odpověď (Back)

Condition number AᵀA je přibližně čtvercem condition number A.

## Poznámka Anki 1790001406227

Karty Anki: 1790001406227
GUID: lOWy[IeikW; štítky: (žádné).

### Otázka (Front)

Jak kniha definuje machine learning podle Mitchella?

### Odpověď (Back)

Program se učí ze zkušenosti E vzhledem k třídě úloh T a performance measure P, pokud se jeho výkon na T měřený P se zkušeností E zlepšuje.

## Poznámka Anki 1790001406228

Karty Anki: 1790001406228
GUID: EBg_mE%86@; štítky: (žádné).

### Otázka (Front)

Co jsou tři prvky Mitchellovy definice learningu?

### Odpověď (Back)

Task T, performance measure P a experience E.

## Poznámka Anki 1790001406229

Karty Anki: 1790001406229
GUID: cE+UCyqdRt; štítky: (žádné).

### Otázka (Front)

Co je classification task?

### Odpověď (Back)

Model přiřazuje inputu x jednu z k categories.

## Poznámka Anki 1790001406230

Karty Anki: 1790001406230
GUID: L>,.*IJ!St; štítky: (žádné).

### Otázka (Front)

Co je classification with missing inputs?

### Odpověď (Back)

Classifier musí predikovat label i tehdy, když některé components input vectoru nejsou pozorovány.

## Poznámka Anki 1790001406231

Karty Anki: 1790001406231
GUID: LLYR_cgqZq; štítky: (žádné).

### Otázka (Front)

Co je regression task?

### Odpověď (Back)

Model má z inputu předpovědět jednu nebo více continuous values.

## Poznámka Anki 1790001406232

Karty Anki: 1790001406232
GUID: C8?TP@%iTc; štítky: (žádné).

### Otázka (Front)

Co je transcription task?

### Odpověď (Back)

Model převádí relativně nestrukturovaný vstup, například image nebo audio, na discrete textual či symbolic sequence.

## Poznámka Anki 1790001406233

Karty Anki: 1790001406233
GUID: KL/1NhC~LX; štítky: (žádné).

### Otázka (Front)

Co je machine translation?

### Odpověď (Back)

Převod sequence symbols v jednom natural language na ekvivalentní sequence v jiném jazyce.

## Poznámka Anki 1790001406234

Karty Anki: 1790001406234
GUID: gaY12c-5@|; štítky: (žádné).

### Otázka (Front)

Co je structured output task?

### Odpověď (Back)

Output obsahuje více vzájemně souvisejících values, jejichž dependencies je vhodné modelovat společně.

## Poznámka Anki 1790001406235

Karty Anki: 1790001406235
GUID: la01q(C.]C; štítky: (žádné).

### Otázka (Front)

Co je anomaly detection?

### Odpověď (Back)

Identifikace examples, které jsou nepravděpodobné vzhledem k normální data distribution.

## Poznámka Anki 1790001406236

Karty Anki: 1790001406236
GUID: F*pn&A&,jo; štítky: (žádné).

### Otázka (Front)

Co je synthesis and sampling task?

### Odpověď (Back)

Generování nových examples podobných samples z training distribution.

## Poznámka Anki 1790001406237

Karty Anki: 1790001406237
GUID: g{k>pqNKq4; štítky: (žádné).

### Otázka (Front)

Co je imputation of missing values?

### Odpověď (Back)

Predikce chybějících components inputu na základě observed components.

## Poznámka Anki 1790001406238

Karty Anki: 1790001406238
GUID: PVwEJYc>uL; štítky: (žádné).

### Otázka (Front)

Co je denoising?

### Odpověď (Back)

Rekonstrukce clean example x z corrupted observation x̃.

## Poznámka Anki 1790001406239

Karty Anki: 1790001406239
GUID: K;tP2r=H=W; štítky: (žádné).

### Otázka (Front)

Co je density estimation?

### Odpověď (Back)

Odhad probability mass nebo density function p_model(x) aproximující data-generating distribution.

## Poznámka Anki 1790001406240

Karty Anki: 1790001406240
GUID: k.S-:hKG|=; štítky: (žádné).

### Otázka (Front)

Co je supervised learning?

### Odpověď (Back)

Learning z labeled examples obsahujících input x a target y.

## Poznámka Anki 1790001406241

Karty Anki: 1790001406241
GUID: s3l>jX]zG#; štítky: (žádné).

### Otázka (Front)

Co je unsupervised learning?

### Odpověď (Back)

Learning struktury z examples x bez explicitního target y.

## Poznámka Anki 1790001406242

Karty Anki: 1790001406242
GUID: uqy&bd}+7D; štítky: (žádné).

### Otázka (Front)

Proč hranice mezi supervised a unsupervised learningem není absolutní?

### Odpověď (Back)

Mnoho algorithms kombinuje obě objectives nebo interpretuje různé subsets variables jako observed a target.

## Poznámka Anki 1790001406243

Karty Anki: 1790001406243
GUID: mWI01NIO~y; štítky: (žádné).

### Otázka (Front)

Co je design matrix X?

### Odpověď (Back)

Matrix training examples, kde řádek X_i,: obvykle představuje jeden example.

## Poznámka Anki 1790001406244

Karty Anki: 1790001406244
GUID: dY`-?)pp5}; štítky: (žádné).

### Otázka (Front)

Co je linear regression model?

### Odpověď (Back)

Model ŷ=wᵀx+b pro predikci continuous targetu.

## Poznámka Anki 1790001406245

Karty Anki: 1790001406245
GUID: F9Zg.:9S!{; štítky: (žádné).

### Otázka (Front)

Jak se linear regression typicky trénuje?

### Odpověď (Back)

Minimalizací mean squared error mezi predictions a targets, ekvivalentně maximum likelihood při Gaussian observation noise.

## Poznámka Anki 1790001406246

Karty Anki: 1790001406246
GUID: JVp0HZI4<n; štítky: (žádné).

### Otázka (Front)

Jaký je MSE objective linear regression?

### Odpověď (Back)

(1/m)Σ_i (ŷ_i−y_i)².

## Poznámka Anki 1790001406247

Karty Anki: 1790001406247
GUID: lL_,$GO7p<; štítky: (žádné).

### Otázka (Front)

Co je generalization?

### Odpověď (Back)

Schopnost modelu dosahovat dobrého výkonu na nových examples z data-generating distribution, nikoli jen na training setu.

## Poznámka Anki 1790001406248

Karty Anki: 1790001406248
GUID: o;THb8F=wt; štítky: (žádné).

### Otázka (Front)

Co je training error?

### Odpověď (Back)

Error měřený na examples použitých k fitování modelu.

## Poznámka Anki 1790001406249

Karty Anki: 1790001406249
GUID: n8SkIl&8Xo; štítky: (žádné).

### Otázka (Front)

Co je test error?

### Odpověď (Back)

Expected nebo empirical error na nových examples, které nebyly použity k trainingu ani model selection.

## Poznámka Anki 1790001406250

Karty Anki: 1790001406250
GUID: GHPp%@k3$L; štítky: (žádné).

### Otázka (Front)

Co je generalization gap?

### Odpověď (Back)

Rozdíl R(θ)−R̂(θ) mezi očekávanou ztrátou na nových datech a trénovacím empirickým riskem. Velký kladný gap signalizuje špatnou generalizaci.

## Poznámka Anki 1790001406251

Karty Anki: 1790001406251
GUID: oNZWE-t3Q@; štítky: (žádné).

### Otázka (Front)

Co je underfitting?

### Odpověď (Back)

Stav, kdy i trénovací empirický risk zůstává vysoký, protože modelová rodina nebo trénink nedokážou dostatečně vystihnout strukturu dat.

## Poznámka Anki 1790001406252

Karty Anki: 1790001406252
GUID: Gy[>pI6&?V; štítky: (žádné).

### Otázka (Front)

Co je overfitting?

### Odpověď (Back)

Stav, kdy je trénovací loss velmi malý, ale generalization gap velký: model se přizpůsobí specifikům a šumu trénovacích dat a na nových datech funguje hůře.

## Poznámka Anki 1790001406253

Karty Anki: 1790001406253
GUID: O^UQK8>zr~; štítky: (žádné).

### Otázka (Front)

Co je capacity modelu?

### Odpověď (Back)

Schopnost fitovat širokou třídu funkcí nebo distributions.

## Poznámka Anki 1790001406254

Karty Anki: 1790001406254
GUID: q8+6:bp:TT; štítky: (žádné).

### Otázka (Front)

Jak capacity ovlivňuje underfitting a overfitting?

### Odpověď (Back)

Příliš malá capacity vede k underfittingu; příliš velká může při omezených datech zvyšovat overfitting.

## Poznámka Anki 1790001406255

Karty Anki: 1790001406255
GUID: A$$yAGB<W7; štítky: (žádné).

### Otázka (Front)

Co je hypothesis space?

### Odpověď (Back)

Množina funkcí, ze které learning algorithm vybírá solution.

## Poznámka Anki 1790001406256

Karty Anki: 1790001406256
GUID: rk.z~<=y$Z; štítky: (žádné).

### Otázka (Front)

Jak linear model omezuje hypothesis space?

### Odpověď (Back)

Povoluje jen lineární nebo affine mappings dané jeho parametrizací.

## Poznámka Anki 1790001406257

Karty Anki: 1790001406257
GUID: Gs?!Yd}4Tp; štítky: (žádné).

### Otázka (Front)

Co je representational capacity?

### Odpověď (Back)

Množina funkcí, které model může teoreticky reprezentovat při nějakém nastavení parametrů.

## Poznámka Anki 1790001406258

Karty Anki: 1790001406258
GUID: Q:n:r*FiC!; štítky: (žádné).

### Otázka (Front)

Co je effective capacity?

### Odpověď (Back)

Subset funkcí, které learning algorithm prakticky může nebo preferuje nalézt po zohlednění optimization a regularization.

## Poznámka Anki 1790001406259

Karty Anki: 1790001406259
GUID: o<A=:J6?Ki; štítky: (žádné).

### Otázka (Front)

Proč effective capacity nemusí odpovídat počtu parameters?

### Odpověď (Back)

Optimization constraints, parameter sharing, regularization a architecture mohou dramaticky měnit, které functions jsou prakticky dostupné.

## Poznámka Anki 1790001406260

Karty Anki: 1790001406260
GUID: BwGSBh^W@); štítky: (žádné).

### Otázka (Front)

Co je Occam's razor v machine learningu?

### Odpověď (Back)

Preference jednodušší hypothesis, pokud vysvětluje data stejně dobře jako složitější.

## Poznámka Anki 1790001406261

Karty Anki: 1790001406261
GUID: sSfu6kt~IO; štítky: (žádné).

### Otázka (Front)

Co je Vapnik–Chervonenkis dimension?

### Odpověď (Back)

Measure capacity classifier family definovaná největším počtem points, které může family shatter ve všech možných labelings.

## Poznámka Anki 1790001406262

Karty Anki: 1790001406262
GUID: G%#t2CUsES; štítky: (žádné).

### Otázka (Front)

Co znamená shatter množinu points?

### Odpověď (Back)

Hypothesis class dokáže realizovat všechny možné binary labelings této množiny.

## Poznámka Anki 1790001406263

Karty Anki: 1790001406263
GUID: h#(JQ&KGiP; štítky: (žádné).

### Otázka (Front)

Jak VC dimension souvisí s generalization theory?

### Odpověď (Back)

Vyšší capacity vyžaduje více examples k zajištění malého generalization gap.

## Poznámka Anki 1790001406264

Karty Anki: 1790001406264
GUID: k|KL*knF_S; štítky: (žádné).

### Otázka (Front)

Co je non-parametric model v širším statistickém smyslu?

### Odpověď (Back)

Model, jehož effective complexity může růst s množstvím dat místo fixed finite parameter count.

## Poznámka Anki 1790001406265

Karty Anki: 1790001406265
GUID: eg<XJKmRrr; štítky: (žádné).

### Otázka (Front)

Co je no free lunch theorem pro machine learning?

### Odpověď (Back)

Při průměrování přes všechny možné data-generating distributions není žádný learning algorithm univerzálně lepší; úspěch vyžaduje assumptions o relevantních problems.

## Poznámka Anki 1790001406266

Karty Anki: 1790001406266
GUID: GWs7fGkA18; štítky: (žádné).

### Otázka (Front)

Jaký praktický závěr plyne z no free lunch theorem?

### Odpověď (Back)

Je nutné vložit inductive biases odpovídající struktuře reálných dat.

## Poznámka Anki 1790001406267

Karty Anki: 1790001406267
GUID: LWzDu?W&oK; štítky: (žádné).

### Otázka (Front)

Co je regularization?

### Odpověď (Back)

Jakákoli úprava learning algorithmu určená ke snížení generalization error, případně za cenu vyššího training error.

## Poznámka Anki 1790001406268

Karty Anki: 1790001406268
GUID: r,}[m{u1M8; štítky: (žádné).

### Otázka (Front)

Jak regularization souvisí s capacity?

### Odpověď (Back)

Obvykle omezuje nebo preferenčně směruje effective capacity k jednodušším či plausibilnějším solutions.

## Poznámka Anki 1790001406269

Karty Anki: 1790001406269
GUID: KC/*4+4Tz/; štítky: (žádné).

### Otázka (Front)

Co je hyperparameter?

### Odpověď (Back)

Nastavení learning algorithmu, které se neučí přímo standardním training objective, například learning rate nebo regularization strength.

## Poznámka Anki 1790001406270

Karty Anki: 1790001406270
GUID: ne6xYtjHB7; štítky: (žádné).

### Otázka (Front)

Proč se hyperparameters nesmějí volit podle test setu?

### Odpověď (Back)

Test set má odhadovat generalization po dokončení model selection; jeho používání k tuningu by vedlo k optimistickému biasu.

## Poznámka Anki 1790001406271

Karty Anki: 1790001406271
GUID: un*e}^cpR7; štítky: (žádné).

### Otázka (Front)

Co je validation set?

### Odpověď (Back)

Data oddělená od training setu, používaná k výběru hyperparameters a model variants.

## Poznámka Anki 1790001406272

Karty Anki: 1790001406272
GUID: N+aHtHC6aj; štítky: (žádné).

### Otázka (Front)

Jaký je rozdíl mezi validation a test setem?

### Odpověď (Back)

Validation řídí model selection, zatímco test se používá až pro finální nezávislý odhad výkonu.

## Poznámka Anki 1790001406273

Karty Anki: 1790001406273
GUID: N/A5zV@]iI; štítky: (žádné).

### Otázka (Front)

Co je k-fold cross-validation?

### Odpověď (Back)

Dataset se rozdělí do k folds; model se k-krát trénuje na k−1 folds a validuje na zbývajícím, poté se výsledky zprůměrují.

## Poznámka Anki 1790001406274

Karty Anki: 1790001406274
GUID: f}}-AK5g~A; štítky: (žádné).

### Otázka (Front)

Kdy je cross-validation zvlášť užitečná?

### Odpověď (Back)

Při malých datasets, kde je drahé vyčlenit velký fixed validation set.

## Poznámka Anki 1790001406275

Karty Anki: 1790001406275
GUID: OSrxuUe!eY; štítky: (žádné).

### Otázka (Front)

Co je estimator?

### Odpověď (Back)

Funkce training data používaná k odhadu neznámého parameteru nebo quantity.

## Poznámka Anki 1790001406276

Karty Anki: 1790001406276
GUID: yu7MpZX|?Q; štítky: (žádné).

### Otázka (Front)

Co je point estimator?

### Odpověď (Back)

Estimator vracející jedinou hodnotu nebo vector parametrů.

## Poznámka Anki 1790001406277

Karty Anki: 1790001406277
GUID: lC_>P#H3*t; štítky: (žádné).

### Otázka (Front)

Co je bias estimatoru θ̂?

### Odpověď (Back)

Bias(θ̂)=E[θ̂]−θ.

## Poznámka Anki 1790001406278

Karty Anki: 1790001406278
GUID: PZ0&g2`FQC; štítky: (žádné).

### Otázka (Front)

Co znamená unbiased estimator?

### Odpověď (Back)

Jeho expected value se rovná true parameteru.

## Poznámka Anki 1790001406279

Karty Anki: 1790001406279
GUID: PACd`_KrGg; štítky: (žádné).

### Otázka (Front)

Co je variance estimatoru?

### Odpověď (Back)

Míra variability θ̂ mezi různými training samples ze stejné data-generating distribution.

## Poznámka Anki 1790001406280

Karty Anki: 1790001406280
GUID: u(3EOZQ`q>; štítky: (žádné).

### Otázka (Front)

Co je standard error estimatoru?

### Odpověď (Back)

Standard deviation jeho sampling distribution.

## Poznámka Anki 1790001406281

Karty Anki: 1790001406281
GUID: se8N_T+0=>; štítky: (žádné).

### Otázka (Front)

Co je mean squared error estimatoru?

### Odpověď (Back)

E[(θ̂−θ)²]=Bias(θ̂)²+Var(θ̂) pro scalar parameter.

## Poznámka Anki 1790001406282

Karty Anki: 1790001406282
GUID: QD0VOWg&(H; štítky: (žádné).

### Otázka (Front)

Co vyjadřuje bias–variance trade-off?

### Odpověď (Back)

Snížení biasu pomocí flexibilnějšího modelu často zvyšuje variance a naopak; optimální generalization vyvažuje obě složky.

## Poznámka Anki 1790001406283

Karty Anki: 1790001406283
GUID: A>MMOZR4OX; štítky: (žádné).

### Otázka (Front)

Co je consistency estimatoru?

### Odpověď (Back)

Estimator je consistent, pokud θ̂_m konverguje k true θ při m→∞.

## Poznámka Anki 1790001406284

Karty Anki: 1790001406284
GUID: tEsENt%*/B; štítky: (žádné).

### Otázka (Front)

Znamená unbiasedness consistency?

### Odpověď (Back)

Ne; unbiased estimator může mít neklesající variance a být inconsistent, zatímco biased estimator může být consistent.

## Poznámka Anki 1790001406285

Karty Anki: 1790001406285
GUID: b3eJXlz%@>; štítky: (žádné).

### Otázka (Front)

Co je maximum likelihood estimation (MLE)?

### Odpověď (Back)

MLE volí θMLE ∈ arg maxθ L(θ), tedy parametry, pod nimiž jsou pozorovaná data nejpravděpodobnější.

## Poznámka Anki 1790001406286

Karty Anki: 1790001406286
GUID: Dku/=,|t/q; štítky: (žádné).

### Otázka (Front)

Jak se MLE zapisuje pro i.i.d. examples?

### Odpověď (Back)

θ_ML=argmax_θ ∏_i p_model(x^(i);θ).

## Poznámka Anki 1790001406287

Karty Anki: 1790001406287
GUID: Ay1tq=6Koy; štítky: (žádné).

### Otázka (Front)

Proč se MLE typicky maximalizuje v log-space?

### Odpověď (Back)

Log změní product na sum, zlepší numerical stability a nemění optimum, protože log je monotonic.

## Poznámka Anki 1790001406288

Karty Anki: 1790001406288
GUID: tR{>~zS1K%; štítky: (žádné).

### Otázka (Front)

Jaký je average negative log-likelihood objective?

### Odpověď (Back)

J(θ)=−E_{x~p̂_data} log p_model(x;θ).

## Poznámka Anki 1790001406289

Karty Anki: 1790001406289
GUID: kQaS#$&wpA; štítky: (žádné).

### Otázka (Front)

Jak MLE souvisí s cross-entropy?

### Odpověď (Back)

Minimalizuje cross-entropy mezi empirical data distribution a model distribution.

## Poznámka Anki 1790001406290

Karty Anki: 1790001406290
GUID: sF[@b@Am->; štítky: (žádné).

### Otázka (Front)

Jak MLE souvisí s D_KL(p_data||p_model)?

### Odpověď (Back)

V population limitu je maximalizace expected log-likelihood ekvivalentní minimalizaci této KL divergence.

## Poznámka Anki 1790001406291

Karty Anki: 1790001406291
GUID: DkS;)0Jv1(; štítky: (žádné).

### Otázka (Front)

Proč je MLE často preferován jako obecný estimator?

### Odpověď (Back)

Má dobré asymptotické properties a poskytuje jednotný princip pro mnoho model families.

## Poznámka Anki 1790001406292

Karty Anki: 1790001406292
GUID: G-6d9kL9,d; štítky: (žádné).

### Otázka (Front)

Co je conditional maximum likelihood?

### Odpověď (Back)

Maximalizace Σ_i log p(y^(i)|x^(i);θ) pro supervised prediction.

## Poznámka Anki 1790001406293

Karty Anki: 1790001406293
GUID: qF]?|X1di5; štítky: (žádné).

### Otázka (Front)

Jak MSE vzniká z maximum likelihood?

### Odpověď (Back)

Při Gaussian p(y|x) s fixed variance maximalizace likelihood odpovídá minimalizaci squared prediction error.

## Poznámka Anki 1790001406294

Karty Anki: 1790001406294
GUID: b@2}k1v*em; štítky: (žádné).

### Otázka (Front)

Jak cross-entropy classification loss vzniká z MLE?

### Odpověď (Back)

Použitím Bernoulli nebo categorical conditional distribution parametrizované neural networkou.

## Poznámka Anki 1790001406295

Karty Anki: 1790001406295
GUID: I@EHn$[B7Z; štítky: (žádné).

### Otázka (Front)

Co je Bayesian statistics?

### Odpověď (Back)

Přístup, který zachází s neznámými parameters jako s random variables a aktualizuje jejich distribution pomocí Bayes rule.

## Poznámka Anki 1790001406296

Karty Anki: 1790001406296
GUID: lshdFddFtB; štítky: (žádné).

### Otázka (Front)

Co je prior distribution p(θ)?

### Odpověď (Back)

Belief o parameters před pozorováním training data.

## Poznámka Anki 1790001406297

Karty Anki: 1790001406297
GUID: hkK}slUIh.; štítky: (žádné).

### Otázka (Front)

Co je posterior p(θ|D)?

### Odpověď (Back)

Distribution parameters po zohlednění data D: p(θ|D)∝p(D|θ)p(θ).

## Poznámka Anki 1790001406298

Karty Anki: 1790001406298
GUID: EP?/6{!#!O; štítky: (žádné).

### Otázka (Front)

Jak Bayesian prediction integruje uncertainty v parameters?

### Odpověď (Back)

p(y|x,D)=∫p(y|x,θ)p(θ|D)dθ.

## Poznámka Anki 1790001406299

Karty Anki: 1790001406299
GUID: A3z0|gSR)#; štítky: (žádné).

### Otázka (Front)

Jak se Bayesian inference liší od MLE?

### Odpověď (Back)

MLE vrací point estimate parameters; Bayesian approach udržuje posterior distribution a při prediction může přes parameters marginalizovat.

## Poznámka Anki 1790001406300

Karty Anki: 1790001406300
GUID: r@~l^JL~KS; štítky: (žádné).

### Otázka (Front)

Co je maximum a posteriori (MAP) estimation?

### Odpověď (Back)

Point estimate θ_MAP=argmax_θ p(θ|D)=argmax_θ [log p(D|θ)+log p(θ)].

## Poznámka Anki 1790001406301

Karty Anki: 1790001406301
GUID: rf>XE`se8w; štítky: (žádné).

### Otázka (Front)

Jak MAP souvisí s regularization?

### Odpověď (Back)

Negative log-prior působí jako regularization term v objective.

## Poznámka Anki 1790001406302

Karty Anki: 1790001406302
GUID: olY`FvCu<v; štítky: (žádné).

### Otázka (Front)

Jaký regularizer odpovídá isotropic Gaussian prioru nad weights?

### Odpověď (Back)

L² neboli weight decay penalty.

## Poznámka Anki 1790001406303

Karty Anki: 1790001406303
GUID: o{]nvs8#V~; štítky: (žádné).

### Otázka (Front)

Jaký regularizer odpovídá Laplace prioru?

### Odpověď (Back)

L¹ penalty.

## Poznámka Anki 1790001406304

Karty Anki: 1790001406304
GUID: e:AV8WKtG+; štítky: (žádné).

### Otázka (Front)

Jak se vliv prioru mění s rostoucím množstvím dat v MAP estimation?

### Odpověď (Back)

Likelihood term roste s počtem examples, zatímco prior ne, takže relativní vliv prioru typicky klesá.

## Poznámka Anki 1790001406305

Karty Anki: 1790001406305
GUID: EWy@_qj3Md; štítky: (žádné).

### Otázka (Front)

Co je supervised learning algorithm?

### Odpověď (Back)

Algorithm učící mapping nebo conditional distribution z labeled pairs (x,y).

## Poznámka Anki 1790001406306

Karty Anki: 1790001406306
GUID: sb_sLl&oha; štítky: (žádné).

### Otázka (Front)

Co je unsupervised learning algorithm?

### Odpověď (Back)

Algorithm učící distribution, representation nebo structure z unlabeled x.

## Poznámka Anki 1790001406307

Karty Anki: 1790001406307
GUID: Of;7=oKu^9; štítky: (žádné).

### Otázka (Front)

Co je logistic regression?

### Odpověď (Back)

Linear classifier modelující Bernoulli probability P(y=1|x)=σ(wᵀx+b).

## Poznámka Anki 1790001406308

Karty Anki: 1790001406308
GUID: cR5#SUiu9*; štítky: (žádné).

### Otázka (Front)

Proč se logistic regression trénuje cross-entropy místo MSE?

### Odpověď (Back)

Cross-entropy odpovídá Bernoulli maximum likelihood a poskytuje vhodnější gradient pro probabilistic classification.

## Poznámka Anki 1790001406309

Karty Anki: 1790001406309
GUID: cF3`8aDp[W; štítky: (žádné).

### Otázka (Front)

Co je support vector machine v základním pojetí knihy?

### Odpověď (Back)

Linear classifier maximalizující margin pomocí hinge loss a norm penalty.

## Poznámka Anki 1790001406310

Karty Anki: 1790001406310
GUID: i;h.zipM`M; štítky: (žádné).

### Otázka (Front)

Co je k-nearest neighbors?

### Odpověď (Back)

Non-parametric method predikující podle targets několika nejbližších training examples.

## Poznámka Anki 1790001406311

Karty Anki: 1790001406311
GUID: NqrTfgh#k7; štítky: (žádné).

### Otázka (Front)

Proč k-nearest neighbors trpí curse of dimensionality?

### Odpověď (Back)

V high dimensions jsou meaningful local neighborhoods velmi sparse a k pokrytí prostoru je potřeba exponenciálně mnoho examples.

## Poznámka Anki 1790001406312

Karty Anki: 1790001406312
GUID: JRNeL,05U,; štítky: (žádné).

### Otázka (Front)

Co je principal components analysis z ML pohledu?

### Odpověď (Back)

Unsupervised linear representation-learning method hledající low-dimensional subspace s minimálním squared reconstruction error.

## Poznámka Anki 1790001406313

Karty Anki: 1790001406313
GUID: J$ozQk+]WC; štítky: (žádné).

### Otázka (Front)

Co je k-means clustering?

### Odpověď (Back)

Unsupervised algorithm střídající přiřazení examples k nejbližším centroidům a update centroidů jako means jejich clusters.

## Poznámka Anki 1790001406314

Karty Anki: 1790001406314
GUID: qzi8;kE.x}; štítky: (žádné).

### Otázka (Front)

Jaký objective minimalizuje k-means?

### Odpověď (Back)

Součet squared Euclidean distances examples k centroidu jejich assigned clusteru.

## Poznámka Anki 1790001406315

Karty Anki: 1790001406315
GUID: PAd(Hj/q+5; štítky: (žádné).

### Otázka (Front)

Co je stochastic gradient descent (SGD)?

### Odpověď (Back)

Gradient-based optimization, která nahrazuje full-data gradient unbiased nebo approximate gradientem vypočteným z minibatch.

## Poznámka Anki 1790001406316

Karty Anki: 1790001406316
GUID: G>QnFBt9$*; štítky: (žádné).

### Otázka (Front)

Proč SGD škáluje lépe než full-batch gradient descent na velké datasety?

### Odpověď (Back)

Cost jednoho update nezávisí na celkovém počtu training examples, ale na minibatch size.

## Poznámka Anki 1790001406317

Karty Anki: 1790001406317
GUID: Ic99:{$6[}; štítky: (žádné).

### Otázka (Front)

Jaký je standardní SGD update?

### Odpověď (Back)

θ←θ−ε ĝ, kde ĝ je minibatch estimate gradientu objective.

