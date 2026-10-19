# Goodfellow – Blok 05 – karty 401–500

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001406318

Karty Anki: 1790001406318
GUID: JF+`sClH`L; štítky: (žádné).

### Otázka (Front)

Jaký vliv má minibatch size na gradient estimate?

### Odpověď (Back)

Větší batch snižuje variance estimate, ale zvyšuje computation jednoho update a má diminishing returns.

## Poznámka Anki 1790001406319

Karty Anki: 1790001406319
GUID: h)S<H5`,Od; štítky: (žádné).

### Otázka (Front)

Proč se examples v minibatchi typicky sampleují i.i.d. nebo po shuffle?

### Odpověď (Back)

Aby minibatch gradient co nejlépe aproximoval expectation pod empirical data distribution a nevnášel systematické ordering bias.

## Poznámka Anki 1790001406320

Karty Anki: 1790001406320
GUID: xZ<c,0|iK#; štítky: (žádné).

### Otázka (Front)

Jaký obecný recept knihy popisuje pro konstrukci ML algoritmu?

### Odpověď (Back)

Zvolit dataset, model, cost function a optimization procedure.

## Poznámka Anki 1790001406321

Karty Anki: 1790001406321
GUID: M)k@jGy*uv; štítky: (žádné).

### Otázka (Front)

Jak lze změnou modelu při stejném costu a optimizeru vytvořit jiný learning algorithm?

### Odpověď (Back)

Model určuje function family a probability assumptions; například lineární mapping lze nahradit neural networkou.

## Poznámka Anki 1790001406322

Karty Anki: 1790001406322
GUID: rEK0y^&pbU; štítky: (žádné).

### Otázka (Front)

Jak lze změnou cost function změnit behavior stejného modelu?

### Odpověď (Back)

Cost určuje statistický cíl a regularization, takže stejný model může být optimalizován pro různé desired properties.

## Poznámka Anki 1790001406323

Karty Anki: 1790001406323
GUID: Gm0NzR&RsI; štítky: (žádné).

### Otázka (Front)

Proč některé ML algorithms potřebují special-purpose optimization?

### Odpověď (Back)

Jejich objectives mohou být discrete, non-differentiable nebo mít flat regions, například decision trees či k-means.

## Poznámka Anki 1790001406324

Karty Anki: 1790001406324
GUID: xMT2znma!9; štítky: (žádné).

### Otázka (Front)

Co je curse of dimensionality?

### Odpověď (Back)

Počet konfigurací nebo regions potřebných k pokrytí prostoru roste exponenciálně s dimensionality.

## Poznámka Anki 1790001406325

Karty Anki: 1790001406325
GUID: Fg_PCz&X?U; štítky: (žádné).

### Otázka (Front)

Jak curse of dimensionality poškozuje local generalization?

### Odpověď (Back)

V high-dimensional space mohou být training examples daleko od většiny test points, takže smoothness založená jen na nearest neighbors poskytuje málo informace.

## Poznámka Anki 1790001406326

Karty Anki: 1790001406326
GUID: HWJ/S&*{20; štítky: (žádné).

### Otázka (Front)

Jaký structural assumption pomáhá deep learningu čelit curse of dimensionality?

### Odpověď (Back)

Data a target functions mají structure, například compositionality, distributed factors nebo concentration near lower-dimensional manifolds.

## Poznámka Anki 1790001406327

Karty Anki: 1790001406327
GUID: M1pd9kCD)?; štítky: (žádné).

### Otázka (Front)

Co je manifold hypothesis?

### Odpověď (Back)

Real-world data v high-dimensional ambient space mají probability mass soustředěnou poblíž low-dimensional manifolds.

## Poznámka Anki 1790001406328

Karty Anki: 1790001406328
GUID: txGtw=}@Bm; štítky: (žádné).

### Otázka (Front)

Jak manifold hypothesis snižuje effective dimensionality?

### Odpověď (Back)

Relevantní variations dat lze popsat menším počtem local coordinates než počtem raw input dimensions.

## Poznámka Anki 1790001406329

Karty Anki: 1790001406329
GUID: OM#E6Y(@T$; štítky: (žádné).

### Otázka (Front)

Proč samotná low-dimensional manifold nestačí pro snadné learning?

### Odpověď (Back)

Manifold může být velmi zakřivená a složitá; learner potřebuje reprezentaci, která její strukturu rozvine nebo sdílí napříč regions.

## Poznámka Anki 1790001406330

Karty Anki: 1790001406330
GUID: KSJm<xkYM$; štítky: (žádné).

### Otázka (Front)

Co znamená disentangling manifold coordinates?

### Odpověď (Back)

Naučit reprezentaci, v níž jednotlivé coordinates odpovídají relativně nezávislým factors variability dat.

## Poznámka Anki 1790001406331

Karty Anki: 1790001406331
GUID: c8@Ydq(tI`; štítky: (žádné).

### Otázka (Front)

Jaký vztah mají traditional ML a deep learning podle kapitoly 5?

### Odpověď (Back)

Deep learning používá stejné principy generalization, estimation, optimization a probabilistic modeling, ale aplikuje je na high-capacity multi-layer representations.

## Poznámka Anki 1790001406332

Karty Anki: 1790001406332
GUID: vkJl<LZ7tY; štítky: (žádné).

### Otázka (Front)

Co je deep feedforward network?

### Odpověď (Back)

Parametrized function y=f(x;θ) tvořená acyclic composition více vrstev, která aproximuje target function f*(x).

## Poznámka Anki 1790001406333

Karty Anki: 1790001406333
GUID: W*AOnEN{[; štítky: (žádné).

### Otázka (Front)

Proč se feedforward network nazývá feedforward?

### Odpověď (Back)

Information flows od inputu přes intermediate hidden computations k outputu bez feedback connections.

## Poznámka Anki 1790001406334

Karty Anki: 1790001406334
GUID: KF:bX(yKQ[; štítky: (žádné).

### Otázka (Front)

Jak se feedforward network liší od recurrent network?

### Odpověď (Back)

Feedforward graph je acyclic; recurrent network obsahuje feedback connections, které po unfolding vytvářejí opakované výpočty přes čas nebo steps.

## Poznámka Anki 1790001406335

Karty Anki: 1790001406335
GUID: mxC2Akv:XU; štítky: (žádné).

### Otázka (Front)

Co znamená depth feedforward network?

### Odpověď (Back)

Počet postupných computational layers nebo transformations na nejdelší path od inputu k outputu.

## Poznámka Anki 1790001406336

Karty Anki: 1790001406336
GUID: Hik.{/%^$.; štítky: (žádné).

### Otázka (Front)

Co je hidden layer?

### Odpověď (Back)

Intermediate layer, jejíž activations nejsou přímo specifikovány training targets a jsou learned jako internal representation.

## Poznámka Anki 1790001406337

Karty Anki: 1790001406337
GUID: v_4^tXA1;?; štítky: (žádné).

### Otázka (Front)

Jaký základní computational pattern má fully connected hidden layer?

### Odpověď (Back)

h=g(Wᵀx+b) nebo ekvivalentní affine transformace následovaná element-wise nonlinearity.

## Poznámka Anki 1790001406338

Karty Anki: 1790001406338
GUID: B!<5I0}MnA; štítky: (žádné).

### Otázka (Front)

Proč nelze hlubokou network vytvořit pouze skládáním lineárních vrstev bez nonlinearities?

### Odpověď (Back)

Composition lineárních/affine transforms je stále jediná affine transformace, takže depth by nepřidala representational power.

## Poznámka Anki 1790001406339

Karty Anki: 1790001406339
GUID: u+Z{uQtF#-; štítky: (žádné).

### Otázka (Front)

Jak XOR ilustruje potřebu hidden features?

### Odpověď (Back)

XOR není linearly separable v původním input space, ale hidden layer může transformovat vstupy do representation, kde je output linearly separable.

## Poznámka Anki 1790001406340

Karty Anki: 1790001406340
GUID: idKs/{SO{Q; štítky: (žádné).

### Otázka (Front)

Jaký princip se používá při designu hidden representation pro XOR?

### Odpověď (Back)

Network se naučí nonlinear features, které vytvoří nový space vhodný pro jednoduchou output rule.

## Poznámka Anki 1790001406341

Karty Anki: 1790001406341
GUID: Q.Q8^%d4^r; štítky: (žádné).

### Otázka (Front)

Co je gradient-based learning neural network?

### Odpověď (Back)

Optimization parameters θ pomocí gradients cost function J(θ), obvykle minibatch SGD nebo jeho variant.

## Poznámka Anki 1790001406342

Karty Anki: 1790001406342
GUID: hL<v?%esE>; štítky: (žádné).

### Otázka (Front)

Proč se output-unit design váže na cost function?

### Odpověď (Back)

Output activation přirozeně parametrizuje určitou probability distribution a maximum-likelihood cost z ní určuje vhodný loss.

## Poznámka Anki 1790001406343

Karty Anki: 1790001406343
GUID: cTyD.?0N!J; štítky: (žádné).

### Otázka (Front)

Jaký output je přirozený pro Gaussian regression s fixed variance?

### Odpověď (Back)

Linear output parametrizující conditional mean.

## Poznámka Anki 1790001406344

Karty Anki: 1790001406344
GUID: OS22fr!tz5; štítky: (žádné).

### Otázka (Front)

Proč se při Gaussian regression často používá MSE?

### Odpověď (Back)

Negative log-likelihood Gaussian s fixed variance je až na konstantu úměrná squared error.

## Poznámka Anki 1790001406345

Karty Anki: 1790001406345
GUID: M`U23n1+U/; štítky: (žádné).

### Otázka (Front)

Jaký output je přirozený pro binary classification?

### Odpověď (Back)

Sigmoid unit parametrizující Bernoulli probability.

## Poznámka Anki 1790001406346

Karty Anki: 1790001406346
GUID: L>]Z{Bh|v#; štítky: (žádné).

### Otázka (Front)

Jaký loss je přirozený pro sigmoid binary classifier?

### Odpověď (Back)

Binary cross-entropy neboli Bernoulli negative log-likelihood.

## Poznámka Anki 1790001406347

Karty Anki: 1790001406347
GUID: o!<v+,@{.}; štítky: (žádné).

### Otázka (Front)

Jaký output je přirozený pro mutually exclusive k-class classification?

### Odpověď (Back)

Softmax distribution nad k classes.

## Poznámka Anki 1790001406348

Karty Anki: 1790001406348
GUID: Q>qq3Am*<{; štítky: (žádné).

### Otázka (Front)

Jak se definuje softmax output?

### Odpověď (Back)

softmax(z)_i=exp(z_i)/Σ_j exp(z_j).

## Poznámka Anki 1790001406349

Karty Anki: 1790001406349
GUID: KN36NYD><C; štítky: (žádné).

### Otázka (Front)

Jaký loss je přirozený pro softmax classifier?

### Odpověď (Back)

Categorical cross-entropy neboli negative log-likelihood správné class.

## Poznámka Anki 1790001406350

Karty Anki: 1790001406350
GUID: L5:Uef&Y{#; štítky: (žádné).

### Otázka (Front)

Proč se maximum likelihood často preferuje před MSE u saturating output units?

### Odpověď (Back)

Správně spárovaný log-likelihood může poskytovat silnější gradient i v regimes, kde by squared error s sigmoid outputem silně saturoval.

## Poznámka Anki 1790001406351

Karty Anki: 1790001406351
GUID: FN{bGVu1(.; štítky: (žádné).

### Otázka (Front)

Co je hidden unit?

### Odpověď (Back)

Learned nonlinear feature vypočtená z předchozí layer.

## Poznámka Anki 1790001406352

Karty Anki: 1790001406352
GUID: s[C+~s-Gw(; štítky: (žádné).

### Otázka (Front)

Co je rectified linear unit (ReLU)?

### Odpověď (Back)

g(z)=max(0,z).

## Poznámka Anki 1790001406353

Karty Anki: 1790001406353
GUID: PXVJP<O+>J; štítky: (žádné).

### Otázka (Front)

Proč jsou ReLU computationally jednoduché?

### Odpověď (Back)

Používají pouze thresholding a lineární přenos v positive region.

## Poznámka Anki 1790001406354

Karty Anki: 1790001406354
GUID: OefZpIBUj&; štítky: (žádné).

### Otázka (Front)

Proč ReLU mohou usnadnit optimization oproti sigmoid/tanh?

### Odpověď (Back)

V positive region mají konstantní derivative 1 a netrpí two-sided saturation.

## Poznámka Anki 1790001406355

Karty Anki: 1790001406355
GUID: vkl3)x}Z4^; štítky: (žádné).

### Otázka (Front)

Jaký sparsity effect mají ReLU?

### Odpověď (Back)

Pro záporný pre-activation dávají přesně nulovou activation.

## Poznámka Anki 1790001406356

Karty Anki: 1790001406356
GUID: vf.$@7s;P6; štítky: (žádné).

### Otázka (Front)

Co je leaky ReLU?

### Odpověď (Back)

Rectifier s malým nenulovým slope α pro z<0, typicky g(z)=max(z,αz).

## Poznámka Anki 1790001406357

Karty Anki: 1790001406357
GUID: tcgat:G3N`; štítky: (žádné).

### Otázka (Front)

Co je parametric ReLU (PReLU)?

### Odpověď (Back)

Leaky ReLU, jejíž negative slope α je learned parameter.

## Poznámka Anki 1790001406358

Karty Anki: 1790001406358
GUID: rwLNmPVa[J; štítky: (žádné).

### Otázka (Front)

Co je maxout unit?

### Odpověď (Back)

Unit vracející maximum z několika learned affine functions.

## Poznámka Anki 1790001406359

Karty Anki: 1790001406359
GUID: N+*}vgZtHk; štítky: (žádné).

### Otázka (Front)

Jaká je hlavní representational výhoda maxout?

### Odpověď (Back)

Může aproximovat obecné convex piecewise-linear functions a dobře spolupracuje s dropout.

## Poznámka Anki 1790001406360

Karty Anki: 1790001406360
GUID: K2<SlYFxB`; štítky: (žádné).

### Otázka (Front)

Jaká je hlavní nevýhoda maxout?

### Odpověď (Back)

Vyšší počet parameters a computation než jednoduchá ReLU.

## Poznámka Anki 1790001406361

Karty Anki: 1790001406361
GUID: co9nX>V`iB; štítky: (žádné).

### Otázka (Front)

Co je sigmoid hidden unit?

### Odpověď (Back)

g(z)=σ(z), saturating nonlinearity mapující real input do (0,1).

## Poznámka Anki 1790001406362

Karty Anki: 1790001406362
GUID: oL=$^I{rUC; štítky: (žádné).

### Otázka (Front)

Proč sigmoid hidden units mohou trpět vanishing gradients?

### Odpověď (Back)

Pro velké |z| derivative σ(z)(1−σ(z)) směřuje k nule.

## Poznámka Anki 1790001406363

Karty Anki: 1790001406363
GUID: iVw?H>/vCu; štítky: (žádné).

### Otázka (Front)

Co je tanh hidden unit?

### Odpověď (Back)

g(z)=tanh(z), zero-centered saturating nonlinearity s outputs v (−1,1).

## Poznámka Anki 1790001406364

Karty Anki: 1790001406364
GUID: q/e1|:xrJ); štítky: (žádné).

### Otázka (Front)

Proč bývá tanh preferována před sigmoid v hidden layers, pokud se používají saturating nonlinearities?

### Odpověď (Back)

Je zero-centered, takže activations mají často příznivější optimization geometry.

## Poznámka Anki 1790001406365

Karty Anki: 1790001406365
GUID: DiDCdqpc%]; štítky: (žádné).

### Otázka (Front)

Jaký princip může pomoci navrhovat nové hidden units?

### Odpověď (Back)

Začít z jednoduchého linear modelu a přidat nelinearitu, která nezhoršuje gradient-based optimization více, než je nutné.

## Poznámka Anki 1790001406366

Karty Anki: 1790001406366
GUID: t[SF)k+F0r; štítky: (žádné).

### Otázka (Front)

Co je universal approximation theorem pro feedforward networks?

### Odpověď (Back)

Feedforward network s alespoň jednou hidden layer a dostatečným počtem units může aproximovat širokou třídu continuous functions na compact domain.

## Poznámka Anki 1790001406367

Karty Anki: 1790001406367
GUID: t?-MITkz$~; štítky: (žádné).

### Otázka (Front)

Znamená universal approximation theorem, že jedna hidden layer je vždy prakticky nejlepší?

### Odpověď (Back)

Ne; potřebná width může být obrovská a theorem nic negarantuje o learnability, generalization ani computational efficiency.

## Poznámka Anki 1790001406368

Karty Anki: 1790001406368
GUID: k]D:N1!APE; štítky: (žádné).

### Otázka (Front)

Jak depth může zvýšit representational efficiency?

### Odpověď (Back)

Některé compositional functions lze reprezentovat polynomial-size deep networkou, ale shallow network může vyžadovat exponenciálně mnoho units.

## Poznámka Anki 1790001406369

Karty Anki: 1790001406369
GUID: dHqL,Q7:4|; štítky: (žádné).

### Otázka (Front)

Jaký inductive bias vyjadřuje použití deep architecture?

### Odpověď (Back)

Preference funkcí tvořených composition mnoha jednodušších transformations.

## Poznámka Anki 1790001406370

Karty Anki: 1790001406370
GUID: r[H?7-oQ]G; štítky: (žádné).

### Otázka (Front)

Proč pouhé zvýšení počtu parametrů v mělké síti nemusí nahradit větší depth?

### Odpověď (Back)

Depth omezuje function family jiným způsobem než size; experimenty ukazují, že deep architecture může generalizovat lépe než stejně či více parametrická shallow architecture.

## Poznámka Anki 1790001406371

Karty Anki: 1790001406371
GUID: dcI*dYdx[}; štítky: (žádné).

### Otázka (Front)

Co je architecture neural network?

### Odpověď (Back)

Specifikace počtu vrstev, jejich widths, typů units a connectivity pattern.

## Poznámka Anki 1790001406372

Karty Anki: 1790001406372
GUID: xo<%,uh`7r; štítky: (žádné).

### Otázka (Front)

Jak width ovlivňuje model capacity?

### Odpověď (Back)

Více hidden units obvykle zvyšuje representational capacity i computational a memory cost.

## Poznámka Anki 1790001406373

Karty Anki: 1790001406373
GUID: my]vofgIb4; štítky: (žádné).

### Otázka (Front)

Jak depth ovlivňuje computation?

### Odpověď (Back)

Přidává sequentially dependent transformations a může vytvářet hierarchické representations.

## Poznámka Anki 1790001406374

Karty Anki: 1790001406374
GUID: m^|~%tm7?j; štítky: (žádné).

### Otázka (Front)

Proč specialized sparse connectivity může být výhodná?

### Odpověď (Back)

Snižuje počet parameters a computation a vkládá domain-relevant structural prior, například locality v CNN.

## Poznámka Anki 1790001406375

Karty Anki: 1790001406375
GUID: vwk!r8rhp5; štítky: (žádné).

### Otázka (Front)

Co je computational graph?

### Odpověď (Back)

Graph reprezentující computation jako nodes operations/variables a directed edges závislosti.

## Poznámka Anki 1790001406376

Karty Anki: 1790001406376
GUID: n>P@~RZKx#; štítky: (žádné).

### Otázka (Front)

Proč jsou computational graphs užitečné?

### Odpověď (Back)

Umožňují systematicky aplikovat chain rule, automatickou diferenciaci a sdílet subcomputations.

## Poznámka Anki 1790001406377

Karty Anki: 1790001406377
GUID: pH}fFsL[Eb; štítky: (žádné).

### Otázka (Front)

Co je forward propagation?

### Odpověď (Back)

Vyhodnocení computational graphu od inputs k outputs a scalar costu.

## Poznámka Anki 1790001406378

Karty Anki: 1790001406378
GUID: ci9c*wFjq0; štítky: (žádné).

### Otázka (Front)

Co je back-propagation?

### Odpověď (Back)

Efektivní algorithm pro výpočet gradientu scalar outputu computational graphu vzhledem k jeho inputs/parameters pomocí chain rule v reverse topological order.

## Poznámka Anki 1790001406379

Karty Anki: 1790001406379
GUID: x8)HvP^h&7; štítky: (žádné).

### Otázka (Front)

Je back-propagation totéž co gradient descent?

### Odpověď (Back)

Ne. Backprop počítá gradient; gradient descent nebo jiný optimizer tento gradient používá k update parameters.

## Poznámka Anki 1790001406380

Karty Anki: 1790001406380
GUID: gZ).o>j?s0; štítky: (žádné).

### Otázka (Front)

Co je automatic differentiation?

### Odpověď (Back)

Programatický výpočet exact derivatives složených elementary operations pomocí chain rule, nikoli symbolic algebra ani finite differences.

## Poznámka Anki 1790001406381

Karty Anki: 1790001406381
GUID: l0`6>]n#?<; štítky: (žádné).

### Otázka (Front)

Jaký typ automatic differentiation odpovídá backpropagation?

### Odpověď (Back)

Reverse-mode automatic differentiation.

## Poznámka Anki 1790001406382

Karty Anki: 1790001406382
GUID: zJb{V:b8`W; štítky: (žádné).

### Otázka (Front)

Proč je reverse-mode AD vhodná pro neural-network training?

### Odpověď (Back)

Máme mnoho parameters/inputs a jeden scalar cost; gradient všech inputs lze získat s costem stejného řádu jako několik forward evaluations.

## Poznámka Anki 1790001406383

Karty Anki: 1790001406383
GUID: h:T/WTLLit; štítky: (žádné).

### Otázka (Front)

Co je forward-mode automatic differentiation?

### Odpověď (Back)

Propaguje derivatives od inputs směrem k outputs a je výhodnější, když je málo inputs a mnoho outputs.

## Poznámka Anki 1790001406384

Karty Anki: 1790001406384
GUID: M]X_VD:K?z; štítky: (žádné).

### Otázka (Front)

Jak chain rule funguje v computational graphu s více cestami?

### Odpověď (Back)

Derivative node vůči ancestoru je součet contributions přes všechny directed paths spojující ancestor s node.

## Poznámka Anki 1790001406385

Karty Anki: 1790001406385
GUID: M-W0Jr*be%; štítky: (žádné).

### Otázka (Front)

Co jsou backprop messages?

### Odpověď (Back)

Intermediate partial derivatives propagované backward, které lze znovu použít pro všechny upstream parameters.

## Poznámka Anki 1790001406386

Karty Anki: 1790001406386
GUID: NV0&6,}?WX; štítky: (žádné).

### Otázka (Front)

Proč naivní symbolic differentiation může opakovat výpočty?

### Odpověď (Back)

Stejné subexpressions derivatives se mohou objevit mnohokrát, zatímco backprop je ukládá a reuseuje.

## Poznámka Anki 1790001406387

Karty Anki: 1790001406387
GUID: r*8T,uhG?Y; štítky: (žádné).

### Otázka (Front)

Jaký memory trade-off má backprop?

### Odpověď (Back)

Pro rychlý backward pass obvykle ukládá forward activations; lze šetřit memory recomputation za cenu dalšího computation.

## Poznámka Anki 1790001406388

Karty Anki: 1790001406388
GUID: FJ7CVHgkrc; štítky: (žádné).

### Otázka (Front)

Co je gradient of tensor output vzhledem k tensor input?

### Odpověď (Back)

Obecně Jacobian s potenciálně velmi vysokým řádem, ale v trainingu se díky scalar costu typicky potřebují jen vector-Jacobian products.

## Poznámka Anki 1790001406389

Karty Anki: 1790001406389
GUID: gb+5[84#~C; štítky: (žádné).

### Otázka (Front)

Co je vector-Jacobian product v backprop?

### Odpověď (Back)

Násobení upstream gradientu Jacobianem local operation bez explicitního sestavení celé Jacobian matrix.

## Poznámka Anki 1790001406390

Karty Anki: 1790001406390
GUID: t==.RUcUn]; štítky: (žádné).

### Otázka (Front)

Proč se Jacobian matrices obvykle explicitně nevytvářejí?

### Odpověď (Back)

Byly by velké; local derivative rules umožňují potřebné products počítat mnohem levněji.

## Poznámka Anki 1790001406391

Karty Anki: 1790001406391
GUID: D-f[V/t+XT; štítky: (žádné).

### Otázka (Front)

Jak se backpropaguje přes addition z=x+y?

### Odpověď (Back)

Upstream gradient se beze změny předá do x i y.

## Poznámka Anki 1790001406392

Karty Anki: 1790001406392
GUID: ED#8RN$3g[; štítky: (žádné).

### Otázka (Front)

Jak se backpropaguje přes multiplication z=xy scalarů?

### Odpověď (Back)

∂J/∂x=(∂J/∂z)y a ∂J/∂y=(∂J/∂z)x.

## Poznámka Anki 1790001406393

Karty Anki: 1790001406393
GUID: DAyq)v~Z55; štítky: (žádné).

### Otázka (Front)

Jak se backpropaguje přes matrix multiplication?

### Odpověď (Back)

Použijí se odpovídající transpose multiplications, například pro C=AB: ∂J/∂A=(∂J/∂C)Bᵀ a ∂J/∂B=Aᵀ(∂J/∂C).

## Poznámka Anki 1790001406394

Karty Anki: 1790001406394
GUID: oqct<g4Ab8; štítky: (žádné).

### Otázka (Front)

Co je differentiation through a graph with shared parameters?

### Odpověď (Back)

Gradient shared parameteru je součet contributions ze všech míst, kde byl parameter použit.

## Poznámka Anki 1790001406395

Karty Anki: 1790001406395
GUID: ebw/In&qxJ; štítky: (žádné).

### Otázka (Front)

Proč parameter sharing dobře spolupracuje s backprop?

### Odpověď (Back)

Reverse-mode AD automaticky akumuluje gradient contributions ze všech usages stejného parameteru.

## Poznámka Anki 1790001406396

Karty Anki: 1790001406396
GUID: ge)1z5K7r!; štítky: (žádné).

### Otázka (Front)

Co je gradient checking?

### Odpověď (Back)

Numerické porovnání analytického/backprop gradientu s finite-difference approximation pro odhalení implementation errors.

## Poznámka Anki 1790001406397

Karty Anki: 1790001406397
GUID: HiX`]un-P,; štítky: (žádné).

### Otázka (Front)

Proč se finite-difference gradient checking nepoužívá jako training algorithm?

### Odpověď (Back)

Je mnohem pomalejší a numericky méně stabilní než backprop.

## Poznámka Anki 1790001406398

Karty Anki: 1790001406398
GUID: yixT`3Oql-; štítky: (žádné).

### Otázka (Front)

Jak lze počítat higher-order derivatives?

### Odpověď (Back)

Aplikovat automatic differentiation na program, který sám počítá derivatives, například backpropagovat skrz gradient computation.

## Poznámka Anki 1790001406399

Karty Anki: 1790001406399
GUID: t?(^(7&Dr]; štítky: (žádné).

### Otázka (Front)

Proč mohou higher-order derivatives být memory/computation náročné?

### Odpověď (Back)

Graph derivative computation je sám rozsáhlý a opakované differentiation může výrazně zvětšit intermediate state.

## Poznámka Anki 1790001406400

Karty Anki: 1790001406400
GUID: q@922t(<u7; štítky: (žádné).

### Otázka (Front)

Co je Hessian-vector product?

### Odpověď (Back)

Součin H v vypočitatelný bez explicitního Hessianu pomocí automatic differentiation, užitečný pro second-order methods.

## Poznámka Anki 1790001406401

Karty Anki: 1790001406401
GUID: nG43<`3=>l; štítky: (žádné).

### Otázka (Front)

Jaký historický význam má backpropagation?

### Odpověď (Back)

Umožnil prakticky trénovat vícevrstvé differentiable networks end-to-end pomocí gradient methods.

## Poznámka Anki 1790001406402

Karty Anki: 1790001406402
GUID: qz=G33STXS; štítky: (žádné).

### Otázka (Front)

Proč feedforward networks tvoří základ mnoha jiných deep models?

### Odpověď (Back)

CNNs, mnoho sequence architectures, VAEs i GAN components používají stejné principy differentiable feedforward computation a backpropagation.

## Poznámka Anki 1790001406403

Karty Anki: 1790001406403
GUID: G4#.[9@DQ@; štítky: (žádné).

### Otázka (Front)

Co je regularization v deep learningu?

### Odpověď (Back)

Jakákoli strategie určená ke snížení test/generalization error, i kdyby zvýšila training error.

## Poznámka Anki 1790001406404

Karty Anki: 1790001406404
GUID: yKa#rVuYi^; štítky: (žádné).

### Otázka (Front)

Jak se regularization liší od optimization?

### Odpověď (Back)

Optimization se snaží minimalizovat training objective; regularization mění objective, model nebo learning procedure tak, aby zlepšila generalization.

## Poznámka Anki 1790001406405

Karty Anki: 1790001406405
GUID: D8m/%t#J!s; štítky: (žádné).

### Otázka (Front)

Co je parameter norm penalty?

### Odpověď (Back)

Regularizer přidávající k objective term Ω(θ), který penalizuje velikost parameters.

## Poznámka Anki 1790001406406

Karty Anki: 1790001406406
GUID: QV/_kq0|Q~; štítky: (žádné).

### Otázka (Front)

Proč se norm penalties často aplikují na weights, ale ne na biases?

### Odpověď (Back)

Bias parameters obvykle ovlivňují pouze jednu output dimension a jejich overfitting přispívá méně; jejich regularizace navíc může zbytečně omezit baseline offsets.

## Poznámka Anki 1790001406407

Karty Anki: 1790001406407
GUID: caUxcOLgsA; štítky: (žádné).

### Otázka (Front)

Jak vypadá L² parameter penalty?

### Odpověď (Back)

Ω(w)=½||w||₂², takže regularized objective je J̃=J+αΩ.

## Poznámka Anki 1790001406408

Karty Anki: 1790001406408
GUID: E3}=xRjw/-; štítky: (žádné).

### Otázka (Front)

Jaký gradient přidává L² penalty?

### Odpověď (Back)

αw.

## Poznámka Anki 1790001406409

Karty Anki: 1790001406409
GUID: L&LznZ]LiL; štítky: (žádné).

### Otázka (Front)

Jaký update vznikne pro SGD s L² weight decay?

### Odpověď (Back)

w←(1−εα)w−ε∇_w J, tedy weights se při každém kroku multiplikativně zmenší.

## Poznámka Anki 1790001406410

Karty Anki: 1790001406410
GUID: wRQ_U#~Q)H; štítky: (žádné).

### Otázka (Front)

Proč se L² regularization nazývá weight decay?

### Odpověď (Back)

V simple gradient update každý weight decayuje faktorem 1−εα kromě data-driven gradient contribution.

## Poznámka Anki 1790001406411

Karty Anki: 1790001406411
GUID: Av#Hb[626R; štítky: (žádné).

### Otázka (Front)

Jak L² penalty působí v eigenbasis Hessianu unregularized objective?

### Odpověď (Back)

Silně potlačuje directions s malou curvature a méně mění directions, které data určují silně.

## Poznámka Anki 1790001406412

Karty Anki: 1790001406412
GUID: J]VC-IDd6f; štítky: (žádné).

### Otázka (Front)

Jaký Bayesian prior odpovídá L² penalty?

### Odpověď (Back)

Zero-mean isotropic Gaussian prior nad weights v MAP estimation.

## Poznámka Anki 1790001406413

Karty Anki: 1790001406413
GUID: fwoy>/ay2#; štítky: (žádné).

### Otázka (Front)

Jak vypadá L¹ penalty?

### Odpověď (Back)

Ω(w)=||w||₁=Σ_i|w_i|.

## Poznámka Anki 1790001406414

Karty Anki: 1790001406414
GUID: zfQc?FVHxJ; štítky: (žádné).

### Otázka (Front)

Jaký gradient/subgradient přidává L¹ penalty pro nenulový weight?

### Odpověď (Back)

α sign(w_i).

## Poznámka Anki 1790001406415

Karty Anki: 1790001406415
GUID: c[27>!OnAU; štítky: (žádné).

### Otázka (Front)

Proč L¹ regularization podporuje sparsity?

### Odpověď (Back)

Penalty působí konstantní silou směrem k nule a optimum některých coordinates může ležet přesně v nule.

## Poznámka Anki 1790001406416

Karty Anki: 1790001406416
GUID: t$)L9(EV32; štítky: (žádné).

### Otázka (Front)

Jaký Bayesian prior odpovídá L¹ penalty?

### Odpověď (Back)

Factorized Laplace prior nad weights.

## Poznámka Anki 1790001406417

Karty Anki: 1790001406417
GUID: F)?W1cl`<Q; štítky: (žádné).

### Otázka (Front)

Jak se L¹ a L² liší v zacházení s velkými a malými weights?

### Odpověď (Back)

L² shrinkage je úměrné magnitude weightu; L¹ působí téměř konstantní silou a snáze vynuluje malé weights.

