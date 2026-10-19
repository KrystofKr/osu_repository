# Goodfellow – Blok 06 – karty 501–600

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001406418

Karty Anki: 1790001406418
GUID: g.C<h!y?r; štítky: (žádné).

### Otázka (Front)

Jak lze norm penalty interpretovat jako constrained optimization?

### Odpověď (Back)

Místo J+αΩ lze minimalizovat J subject to Ω(θ)≤k; pro vhodné α a k mohou obě formulace mít stejné optimum.

## Poznámka Anki 1790001406419

Karty Anki: 1790001406419
GUID: Cl[;jT*Qmy; štítky: (žádné).

### Otázka (Front)

Co určuje Lagrange multiplier α v constrained interpretation regularization?

### Odpověď (Back)

Sílu constraintu na parameter norm a tedy trade-off mezi data fit a preferred complexity.

## Poznámka Anki 1790001406420

Karty Anki: 1790001406420
GUID: JOcH[u5e`6; štítky: (žádné).

### Otázka (Front)

Proč může explicit constraint být užitečný oproti penalty?

### Odpověď (Back)

Projection může zabránit parameters opustit povolenou oblast i při velkých gradient steps.

## Poznámka Anki 1790001406421

Karty Anki: 1790001406421
GUID: Pnx$uP-rv*; štítky: (žádné).

### Otázka (Front)

Co je projected gradient descent?

### Odpověď (Back)

Po gradient update se parameters promítnou zpět do feasible set daného constraintem.

## Poznámka Anki 1790001406422

Karty Anki: 1790001406422
GUID: y;k3ls9tAu; štítky: (žádné).

### Otázka (Front)

Co je under-constrained problem?

### Odpověď (Back)

Problem, kde training objective nedokáže jednoznačně určit všechny parameters, například protože design matrix nemá full rank.

## Poznámka Anki 1790001406423

Karty Anki: 1790001406423
GUID: y,/Z;GA(NP; štítky: (žádné).

### Otázka (Front)

Jak regularization řeší under-constrained linear problem?

### Odpověď (Back)

Vybere preferované řešení mezi mnoha ekvivalentními fits, například minimum-norm solution.

## Poznámka Anki 1790001406424

Karty Anki: 1790001406424
GUID: HXZRY{YxLR; štítky: (žádné).

### Otázka (Front)

Co je dataset augmentation?

### Odpověď (Back)

Generování dalších training examples aplikací transformations, o nichž předpokládáme, že nemění správný label.

## Poznámka Anki 1790001406425

Karty Anki: 1790001406425
GUID: FR++py(EH@; štítky: (žádné).

### Otázka (Front)

Jaký typ invariance vkládá image translation augmentation?

### Odpověď (Back)

Předpoklad, že malé posuny objektu nemění jeho category.

## Poznámka Anki 1790001406426

Karty Anki: 1790001406426
GUID: OK87%pv64p; štítky: (žádné).

### Otázka (Front)

Proč dataset augmentation často funguje lépe než explicitní generic regularization?

### Odpověď (Back)

Vkládá konkrétní domain knowledge o transformacích, vůči nimž má být predictor invariantní.

## Poznámka Anki 1790001406427

Karty Anki: 1790001406427
GUID: GQyGN3:`nn; štítky: (žádné).

### Otázka (Front)

Jaký benefit má augmentation kromě regularization?

### Odpověď (Back)

Efektivně zvyšuje množství distinct training inputs bez nového ručního labeling.

## Poznámka Anki 1790001406428

Karty Anki: 1790001406428
GUID: g+Co*QWtYN; štítky: (žádné).

### Otázka (Front)

Kdy může augmentation škodit?

### Odpověď (Back)

Když použitá transformation ve skutečnosti může změnit target nebo vytváří unrealistic examples.

## Poznámka Anki 1790001406429

Karty Anki: 1790001406429
GUID: x>Ut`D$}{D; štítky: (žádné).

### Otázka (Front)

Co je noise injection do inputs?

### Odpověď (Back)

Přidávání náhodného noise k training inputs jako forma augmentation a regularization.

## Poznámka Anki 1790001406430

Karty Anki: 1790001406430
GUID: l,MGHf`3r*; štítky: (žádné).

### Otázka (Front)

Jak lze input noise interpretovat u některých modelů?

### Odpověď (Back)

Může aproximovat určité smoothness nebo derivative penalties a podporovat robustní predictions.

## Poznámka Anki 1790001406431

Karty Anki: 1790001406431
GUID: Ab<i*E6Coh; štítky: (žádné).

### Otázka (Front)

Co je weight noise?

### Odpověď (Back)

Přidávání noise přímo k parameters během trainingu.

## Poznámka Anki 1790001406432

Karty Anki: 1790001406432
GUID: bHRmc_LGEE; štítky: (žádné).

### Otázka (Front)

Jak lze weight noise interpretovat Bayesian způsobem?

### Odpověď (Back)

Jako stochastic uncertainty nad parameters; u některých settings odpovídá regularization preferující flat robust solutions.

## Poznámka Anki 1790001406433

Karty Anki: 1790001406433
GUID: n&A(t^O5Mv; štítky: (žádné).

### Otázka (Front)

Co je label smoothing?

### Odpověď (Back)

Nahrazení hard one-hot targets distribution, která dává většinu mass správné class a malou mass ostatním classes.

## Poznámka Anki 1790001406434

Karty Anki: 1790001406434
GUID: JnVz2iO?:o; štítky: (žádné).

### Otázka (Front)

Proč label smoothing regularizuje classifier?

### Odpověď (Back)

Brání modelu tlačit logit differences k extrémním hodnotám a penalizuje overconfident predictions.

## Poznámka Anki 1790001406435

Karty Anki: 1790001406435
GUID: =Glq<&fX#; štítky: (žádné).

### Otázka (Front)

Jaký vztah má label smoothing k prioru nad labels?

### Odpověď (Back)

Target lze chápat jako mixture empirical hard labelu a simple prior distribution, často uniformní.

## Poznámka Anki 1790001406436

Karty Anki: 1790001406436
GUID: NN6aNo90F.; štítky: (žádné).

### Otázka (Front)

Co je semi-supervised learning?

### Odpověď (Back)

Learning využívající labeled i unlabeled data.

## Poznámka Anki 1790001406437

Karty Anki: 1790001406437
GUID: I*%,Dy:}Q{; štítky: (žádné).

### Otázka (Front)

Jak unlabeled data mohou regularizovat supervised model?

### Odpověď (Back)

Pomáhají odhalit structure p(x) nebo representation, která omezuje plausibilní decision functions.

## Poznámka Anki 1790001406438

Karty Anki: 1790001406438
GUID: g{Ba$N1$G(; štítky: (žádné).

### Otázka (Front)

Kdy unlabeled data nemusí pomoci supervised tasku?

### Odpověď (Back)

Když structure p(x) nesouvisí s conditional p(y|x) nebo když unsupervised objective zdůrazňuje task-irrelevant factors.

## Poznámka Anki 1790001406439

Karty Anki: 1790001406439
GUID: xK?{Nsx!p$; štítky: (žádné).

### Otázka (Front)

Co je multi-task learning?

### Odpověď (Back)

Společné učení více related tasks se sdílenou representation nebo parameters.

## Poznámka Anki 1790001406440

Karty Anki: 1790001406440
GUID: sJZhP8j5F1; štítky: (žádné).

### Otázka (Front)

Jak multi-task learning regularizuje?

### Odpověď (Back)

Shared parameters musí vysvětlit více tasks, takže se méně přizpůsobují noise jednoho tasku.

## Poznámka Anki 1790001406441

Karty Anki: 1790001406441
GUID: dK~<Uun#1; štítky: (žádné).

### Otázka (Front)

Kdy může multi-task learning škodit?

### Odpověď (Back)

Když tasks nesdílejí užitečné underlying factors nebo jejich gradients si systematicky odporují.

## Poznámka Anki 1790001406442

Karty Anki: 1790001406442
GUID: h^(ZB%>jOI; štítky: (žádné).

### Otázka (Front)

Co je early stopping?

### Odpověď (Back)

Během tréninku se sleduje validation loss a uchovají se parametry z epochy, kde byl minimální. Tím se zastaví trénink dříve, než se model začne příliš přizpůsobovat trénovacímu šumu.

## Poznámka Anki 1790001406443

Karty Anki: 1790001406443
GUID: J`m`clmktG; štítky: (žádné).

### Otázka (Front)

Proč early stopping funguje jako regularizer?

### Odpověď (Back)

Omezuje effective optimization time a tím, jak daleko se parameters mohou přizpůsobit training data.

## Poznámka Anki 1790001406444

Karty Anki: 1790001406444
GUID: JPL1~{BK>z; štítky: (žádné).

### Otázka (Front)

Co se při early stopping typicky sleduje?

### Odpověď (Back)

Validation error nebo jiná validation performance metric.

## Poznámka Anki 1790001406445

Karty Anki: 1790001406445
GUID: l1_&![PT!/; štítky: (žádné).

### Otázka (Front)

Proč se nejlepší model při early stopping obvykle checkpointuje?

### Odpověď (Back)

Validation metric může po dosažení nejlepší hodnoty zhoršit; final parameters nemusí být nejlepší.

## Poznámka Anki 1790001406446

Karty Anki: 1790001406446
GUID: sW9}IN^J7%; štítky: (žádné).

### Otázka (Front)

Jaký computational benefit může mít early stopping?

### Odpověď (Back)

Současně regularizuje a zkracuje training oproti metodám vyžadujícím plnou convergence.

## Poznámka Anki 1790001406447

Karty Anki: 1790001406447
GUID: d^KQHs)BP;; štítky: (žádné).

### Otázka (Front)

Jak early stopping souvisí s L² regularization v simple linear/quadratic settings?

### Odpověď (Back)

Omezený počet gradient steps může preferovat podobně low-norm solutions jako explicitní weight decay.

## Poznámka Anki 1790001406448

Karty Anki: 1790001406448
GUID: OkeY|rL5F3; štítky: (žádné).

### Otázka (Front)

Co je parameter tying?

### Odpověď (Back)

Constraint, že více model parameters sdílí stejnou hodnotu.

## Poznámka Anki 1790001406449

Karty Anki: 1790001406449
GUID: v`TZD=|o0<; štítky: (žádné).

### Otázka (Front)

Co je parameter sharing?

### Odpověď (Back)

Používání stejného parameteru v několika částech modelu, například convolution kernel na různých spatial positions.

## Poznámka Anki 1790001406450

Karty Anki: 1790001406450
GUID: rbp8YgGK$r; štítky: (žádné).

### Otázka (Front)

Jak parameter sharing regularizuje?

### Odpověď (Back)

Snižuje počet independent degrees of freedom a vkládá assumption, že stejná feature má být užitečná v různých contexts.

## Poznámka Anki 1790001406451

Karty Anki: 1790001406451
GUID: KEQVZMVad(; štítky: (žádné).

### Otázka (Front)

Co je sparse representation?

### Odpověď (Back)

Representation, v níž je pro typický input aktivní jen malá část units.

## Poznámka Anki 1790001406452

Karty Anki: 1790001406452
GUID: j.lU@HwKY@; štítky: (žádné).

### Otázka (Front)

Jaký rozdíl je mezi sparse parameters a sparse representation?

### Odpověď (Back)

Sparse parameters znamenají mnoho nulových weights; sparse representation znamená mnoho nulových activations.

## Poznámka Anki 1790001406453

Karty Anki: 1790001406453
GUID: j*w|BJ$g%m; štítky: (žádné).

### Otázka (Front)

Jak lze podporovat sparse activations?

### Odpověď (Back)

Přidat penalty na hidden activations, například L¹ term nebo KL penalty k nízké target activation rate.

## Poznámka Anki 1790001406454

Karty Anki: 1790001406454
GUID: GRkbS4{)10; štítky: (žádné).

### Otázka (Front)

Co je bagging?

### Odpověď (Back)

Ensemble metoda trénující více models na bootstrapped datasets a kombinující jejich predictions.

## Poznámka Anki 1790001406455

Karty Anki: 1790001406455
GUID: j@(#|l^;r`; štítky: (žádné).

### Otázka (Front)

Jaký hlavní statistical effect má bagging?

### Odpověď (Back)

Snižuje variance predictorů, pokud jejich errors nejsou dokonale korelované.

## Poznámka Anki 1790001406456

Karty Anki: 1790001406456
GUID: LBPbVxv80I; štítky: (žádné).

### Otázka (Front)

Jak se kombinuje regression ensemble v baggingu?

### Odpověď (Back)

Průměrováním predictions.

## Poznámka Anki 1790001406457

Karty Anki: 1790001406457
GUID: B`YJHpimYu; štítky: (žádné).

### Otázka (Front)

Jak se kombinuje classification ensemble?

### Odpověď (Back)

Votingem nebo průměrováním predictive probabilities.

## Poznámka Anki 1790001406458

Karty Anki: 1790001406458
GUID: f@pT,v!e_,; štítky: (žádné).

### Otázka (Front)

Proč ensemble může zlepšit generalization?

### Odpověď (Back)

Nezávislé nebo částečně nekorelované errors jednotlivých models se při averagingu částečně vyruší.

## Poznámka Anki 1790001406459

Karty Anki: 1790001406459
GUID: blNIn&;TTr; štítky: (žádné).

### Otázka (Front)

Co je bootstrap sample?

### Odpověď (Back)

Dataset stejné velikosti jako původní training set vytvořený samplingem examples s replacement.

## Poznámka Anki 1790001406460

Karty Anki: 1790001406460
GUID: xp:Aa8KB#[; štítky: (žádné).

### Otázka (Front)

Co je dropout?

### Odpověď (Back)

Regularization technique, která během trainingu náhodně násobí activations binary maskou a tím trénuje mnoho subnetworks sdílejících parameters.

## Poznámka Anki 1790001406461

Karty Anki: 1790001406461
GUID: Oxzev3G4Qg; štítky: (žádné).

### Otázka (Front)

Jaký typ noise používá standardní dropout?

### Odpověď (Back)

Multiplicative Bernoulli noise, který jednotlivé units nebo inputs náhodně nastaví na nulu.

## Poznámka Anki 1790001406462

Karty Anki: 1790001406462
GUID: hdG[m{cwM^; štítky: (žádné).

### Otázka (Front)

Jak lze dropout interpretovat jako ensemble?

### Odpověď (Back)

Každá maska definuje jinou subnetwork; training sdílí weights mezi exponenciálně mnoha subnetworks.

## Poznámka Anki 1790001406463

Karty Anki: 1790001406463
GUID: zE/N|S7Hdy; štítky: (žádné).

### Otázka (Front)

Proč není možné explicitně average predictions všech dropout subnetworks?

### Odpověď (Back)

Je jich exponenciálně mnoho.

## Poznámka Anki 1790001406464

Karty Anki: 1790001406464
GUID: Pj95Pq@ZST; štítky: (žádné).

### Otázka (Front)

Jak se dropout typicky aproximuje při testu?

### Odpověď (Back)

Použije se full network s deterministically škálovanými activations nebo inverted-dropout convention, takže test network aproximuje ensemble average.

## Poznámka Anki 1790001406465

Karty Anki: 1790001406465
GUID: Lq+VrrqNGZ; štítky: (žádné).

### Otázka (Front)

Co je inverted dropout?

### Odpověď (Back)

Během trainingu se zachované activations dělí keep probability, takže při testu není potřeba další scaling.

## Poznámka Anki 1790001406466

Karty Anki: 1790001406466
GUID: LXCDC?vS}S; štítky: (žádné).

### Otázka (Front)

Proč dropout omezuje co-adaptation features?

### Odpověď (Back)

Unit nemůže spoléhat na přítomnost konkrétních ostatních units, protože jejich dropout maska se náhodně mění.

## Poznámka Anki 1790001406467

Karty Anki: 1790001406467
GUID: l.vP1)G/C6; štítky: (žádné).

### Otázka (Front)

Kdy může dropout potřebovat méně benefitovat?

### Odpověď (Back)

Při extrémně velkých datasets, silné jiné regularization nebo architectures s již výrazným parameter sharing.

## Poznámka Anki 1790001406468

Karty Anki: 1790001406468
GUID: lD!LFfq!dD; štítky: (žádné).

### Otázka (Front)

Co je adversarial example?

### Odpověď (Back)

Input vzniklý malou, často perceptuálně zanedbatelnou perturbací, která způsobí výrazně chybnou prediction modelu.

## Poznámka Anki 1790001406469

Karty Anki: 1790001406469
GUID: db]oT.)IIf; štítky: (žádné).

### Otázka (Front)

Co je adversarial training?

### Odpověď (Back)

Regularization, která do trainingu přidává adversarially perturbed examples a učí model správně je klasifikovat.

## Poznámka Anki 1790001406470

Karty Anki: 1790001406470
GUID: eq:_ofx35V; štítky: (žádné).

### Otázka (Front)

Jak se typicky vytváří jednoduchá adversarial perturbation podle fast gradient sign method?

### Odpověď (Back)

η=ε sign(∇_x J(θ,x,y)).

## Poznámka Anki 1790001406471

Karty Anki: 1790001406471
GUID: I0Tdw;+`>Q; štítky: (žádné).

### Otázka (Front)

Proč adversarial examples zpochybňují čistě local smoothness intuition?

### Odpověď (Back)

Velmi malý krok v high-dimensional prostoru může kumulativně změnit linear response o velkou hodnotu.

## Poznámka Anki 1790001406472

Karty Anki: 1790001406472
GUID: so7+rMQiue; štítky: (žádné).

### Otázka (Front)

Jaký mechanismus knihy navrhuje jako vysvětlení adversarial vulnerability mnoha networks?

### Odpověď (Back)

Především high-dimensional linear behavior, nikoli nutně extrémní nelinearita.

## Poznámka Anki 1790001406473

Karty Anki: 1790001406473
GUID: t9n&r?E&@3; štítky: (žádné).

### Otázka (Front)

Jak adversarial training funguje jako local smoothness regularizer?

### Odpověď (Back)

Nutí predictor dávat správné výsledky i v nejproblematičtějších směrech malého okolí training examples.

## Poznámka Anki 1790001406474

Karty Anki: 1790001406474
GUID: B0;p8_4m)C; štítky: (žádné).

### Otázka (Front)

Co je tangent propagation?

### Odpověď (Back)

Regularization penalizující sensitivity model outputu ve známých tangent directions transformací, vůči nimž má být invariantní.

## Poznámka Anki 1790001406475

Karty Anki: 1790001406475
GUID: q0Kg3!1ed&; štítky: (žádné).

### Otázka (Front)

Co je tangent distance?

### Odpověď (Back)

Distance measure, která zohledňuje local manifold transformations a považuje examples spojené tangent direction za podobnější.

## Poznámka Anki 1790001406476

Karty Anki: 1790001406476
GUID: bfO|X/gpKE; štítky: (žádné).

### Otázka (Front)

Co je manifold tangent classifier?

### Odpověď (Back)

Classifier kombinující unsupervised manifold tangent estimation s tangent-propagation-like supervised regularization.

## Poznámka Anki 1790001406477

Karty Anki: 1790001406477
GUID: tbEp,X*D$I; štítky: (žádné).

### Otázka (Front)

Jaký sjednocující princip mají augmentation a tangent methods?

### Odpověď (Back)

Vkládají prior knowledge o transformations, které by neměly měnit prediction.

## Poznámka Anki 1790001406478

Karty Anki: 1790001406478
GUID: d$4)UGUk/%; štítky: (žádné).

### Otázka (Front)

Jaký sjednocující princip mají weight decay, dropout a early stopping?

### Odpověď (Back)

Omezují effective capacity nebo způsob, jakým se model může přizpůsobit finite training sample.

## Poznámka Anki 1790001406479

Karty Anki: 1790001406479
GUID: x41}F#6g`v; štítky: (žádné).

### Otázka (Front)

Proč není nejlepší regularizer univerzální?

### Odpověď (Back)

Úspěch závisí na modelu, dataset size, architecture a správnosti domain assumptions vložených regularizerem.

## Poznámka Anki 1790001406480

Karty Anki: 1790001406480
GUID: OI6j}FPyX*; štítky: (žádné).

### Otázka (Front)

Jak se optimization pro training neural networks liší od čisté mathematical optimization?

### Odpověď (Back)

Cílem není minimalizovat training objective samo o sobě, ale dosáhnout nízkého expected generalization error.

## Poznámka Anki 1790001406481

Karty Anki: 1790001406481
GUID: b=:curS$I/; štítky: (žádné).

### Otázka (Front)

Jaký objective se při supervised trainingu typicky skutečně optimalizuje?

### Odpověď (Back)

Empirical risk neboli sample average loss přes training data, často s regularization.

## Poznámka Anki 1790001406482

Karty Anki: 1790001406482
GUID: wQ#ZICz;Pc; štítky: (žádné).

### Otázka (Front)

Proč minibatch stochastic optimization nahrazuje full objective?

### Odpověď (Back)

Exact expectation pod data distribution není známá a full empirical average může být příliš drahá na každý update.

## Poznámka Anki 1790001406483

Karty Anki: 1790001406483
GUID: k5r6^M1g*%; štítky: (žádné).

### Otázka (Front)

Jaký benefit má minibatch kromě nižší computational cost?

### Odpověď (Back)

Využívá vectorized hardware a stochasticity gradientu může pomáhat exploration.

## Poznámka Anki 1790001406484

Karty Anki: 1790001406484
GUID: E^T0=(-!$g; štítky: (žádné).

### Otázka (Front)

Jak se variance minibatch gradientu mění s batch size?

### Odpověď (Back)

Obecně klesá, ale s diminishing returns a bez lineárního zlepšení optimization progress.

## Poznámka Anki 1790001406485

Karty Anki: 1790001406485
GUID: Gnej{nLU#K; štítky: (žádné).

### Otázka (Front)

Proč může být velmi velký batch computationally neefektivní?

### Odpověď (Back)

Další examples snižují variance méně, než kolik stojí computation, a poskytují méně parameter updates na jednotku dat.

## Poznámka Anki 1790001406486

Karty Anki: 1790001406486
GUID: M/O%gxYvoY; štítky: (žádné).

### Otázka (Front)

Co je non-convexity neural-network optimization?

### Odpověď (Back)

Training objective má komplexní landscape s mnoha critical points a symmetries místo jediného convex basin.

## Poznámka Anki 1790001406487

Karty Anki: 1790001406487
GUID: lgT!d{7|B; štítky: (žádné).

### Otázka (Front)

Proč local minima nejsou jedinou nebo hlavní obtíží deep optimization?

### Odpověď (Back)

High-dimensional objectives obsahují mnoho saddle points, plateaus, ill-conditioning a gradient instability.

## Poznámka Anki 1790001406488

Karty Anki: 1790001406488
GUID: vR};~kfx3{; štítky: (žádné).

### Otázka (Front)

Proč jsou saddle points časté v high-dimensional spaces?

### Odpověď (Back)

Je statisticky nepravděpodobné, aby všechny Hessian eigenvalues měly stejné znaménko; kombinace positive a negative curvature je častější.

## Poznámka Anki 1790001406489

Karty Anki: 1790001406489
GUID: iO(|hL1;<-; štítky: (žádné).

### Otázka (Front)

Co je ill-conditioning v neural-network trainingu?

### Odpověď (Back)

Hessian má eigenvalues velmi odlišných magnitudes, takže vhodný step size pro jeden směr je nevhodný pro jiný.

## Poznámka Anki 1790001406490

Karty Anki: 1790001406490
GUID: G_4~i_W|VS; štítky: (žádné).

### Otázka (Front)

Jak ill-conditioning ovlivňuje SGD trajectory?

### Odpověď (Back)

Gradient může oscilovat napříč steep direction a postupovat pomalu podél shallow direction.

## Poznámka Anki 1790001406491

Karty Anki: 1790001406491
GUID: z>|FGWBc1X; štítky: (žádné).

### Otázka (Front)

Co jsou cliffs and exploding gradients?

### Odpověď (Back)

Regions, kde opakované transformations vytvářejí velmi velké derivatives, takže gradient norm náhle exploduje.

## Poznámka Anki 1790001406492

Karty Anki: 1790001406492
GUID: I!f2:Q`*ye; štítky: (žádné).

### Otázka (Front)

Co je vanishing gradient?

### Odpověď (Back)

Gradient se při backpropagation přes mnoho transformations násobením malých Jacobian factors zmenší téměř k nule.

## Poznámka Anki 1790001406493

Karty Anki: 1790001406493
GUID: id[Ff^{W![; štítky: (žádné).

### Otázka (Front)

Proč jsou long-term dependencies v recurrent networks zvlášť citlivé na exploding/vanishing gradients?

### Odpověď (Back)

Stejná recurrent Jacobian se násobí napříč mnoha time steps.

## Poznámka Anki 1790001406494

Karty Anki: 1790001406494
GUID: e`vF#jfa3k; štítky: (žádné).

### Otázka (Front)

Co znamená poor correspondence between local and global structure objective?

### Odpověď (Back)

Local gradient může směřovat k okamžitému zlepšení, ale nepřenáší informaci o vzdálenější, výrazně lepší region landscape.

## Poznámka Anki 1790001406495

Karty Anki: 1790001406495
GUID: LHl%A;0^;+; štítky: (žádné).

### Otázka (Front)

Jaký optimization problém mohou způsobovat saturating nonlinearities?

### Odpověď (Back)

Malé derivatives vytvářejí flat regions s velmi slabým gradient signalem.

## Poznámka Anki 1790001406496

Karty Anki: 1790001406496
GUID: D:lB*oH>Q); štítky: (žádné).

### Otázka (Front)

Proč stochastic gradients nejsou přesným gradientem empirical objective?

### Odpověď (Back)

Minibatch obsahuje pouze náhodný subset data, takže vzniká sampling noise.

## Poznámka Anki 1790001406497

Karty Anki: 1790001406497
GUID: t<u|5^P@2G; štítky: (žádné).

### Otázka (Front)

Jaký základní SGD update používá learning rate ε?

### Odpověď (Back)

θ←θ−ε ĝ.

## Poznámka Anki 1790001406498

Karty Anki: 1790001406498
GUID: e*X~U,Ap@B; štítky: (žádné).

### Otázka (Front)

Proč se learning rate často během trainingu snižuje?

### Odpověď (Back)

Na začátku jsou vhodné velké kroky pro rychlý progress, později menší kroky snižují oscillation a stochastic noise kolem optimum.

## Poznámka Anki 1790001406499

Karty Anki: 1790001406499
GUID: JPUIFR}&~F; štítky: (žádné).

### Otázka (Front)

Jaká theoretical condition pro convergence stochastic approximation často vyžaduje learning-rate schedule?

### Odpověď (Back)

Σ_t ε_t=∞, ale Σ_t ε_t²<∞.

## Poznámka Anki 1790001406500

Karty Anki: 1790001406500
GUID: EyUpCW+o,1; štítky: (žádné).

### Otázka (Front)

Proč konstantní learning rate obvykle nekonverguje přesně v stochastic settingu?

### Odpověď (Back)

Gradient noise udržuje parameters v neighborhood optimum místo asymptotického zániku step sizes.

## Poznámka Anki 1790001406501

Karty Anki: 1790001406501
GUID: J92v&[GaQS; štítky: (žádné).

### Otázka (Front)

Co je momentum?

### Odpověď (Back)

Optimizer akumulující exponentially decayed moving average minulých gradients do velocity, která určuje parameter update.

## Poznámka Anki 1790001406502

Karty Anki: 1790001406502
GUID: t>9`K3z2xs; štítky: (žádné).

### Otázka (Front)

Jaký standardní momentum update uvádí kniha?

### Odpověď (Back)

v←αv−ε∇J(θ), θ←θ+v.

## Poznámka Anki 1790001406503

Karty Anki: 1790001406503
GUID: n,uL#L{dTc; štítky: (žádné).

### Otázka (Front)

Jak momentum pomáhá v ill-conditioned valley?

### Odpověď (Back)

Akumuluje consistent gradient component podél valley a ruší oscilující components napříč steep direction.

## Poznámka Anki 1790001406504

Karty Anki: 1790001406504
GUID: vana<.Nte>; štítky: (žádné).

### Otázka (Front)

Jaký význam má momentum coefficient α?

### Odpověď (Back)

Určuje, jak dlouho minulá velocity přetrvává; vyšší α prodlužuje effective averaging horizon.

## Poznámka Anki 1790001406505

Karty Anki: 1790001406505
GUID: IZHn#}3Z77; štítky: (žádné).

### Otázka (Front)

Jak momentum mění effective step při konstantním gradientu?

### Odpověď (Back)

Po ustálení může velocity být přibližně ε/(1−α) násobkem gradientu oproti jednomu raw step.

## Poznámka Anki 1790001406506

Karty Anki: 1790001406506
GUID: q#$k)_f_0i; štítky: (žádné).

### Otázka (Front)

Co je Nesterov momentum?

### Odpověď (Back)

Varianta, která vyhodnotí gradient po částečném posunu ve směru current velocity.

## Poznámka Anki 1790001406507

Karty Anki: 1790001406507
GUID: f76j+Nh{m+; štítky: (žádné).

### Otázka (Front)

Jaká je intuition Nesterov momentum?

### Odpověď (Back)

Gradient 'vidí dopředu' do místa, kam momentum míří, a může začít korigovat směr dříve.

## Poznámka Anki 1790001406508

Karty Anki: 1790001406508
GUID: f|C$[KKgf!; štítky: (žádné).

### Otázka (Front)

Proč initialization neural network není pouze arbitrary detail?

### Odpověď (Back)

Určuje počáteční scale activations, gradient propagation, symmetry breaking a region objective landscape navštívený optimizerem.

## Poznámka Anki 1790001406509

Karty Anki: 1790001406509
GUID: BBE&*!Z/X&; štítky: (žádné).

### Otázka (Front)

Proč se weights nemají všechny inicializovat stejnou hodnotou?

### Odpověď (Back)

Symmetric units by dostávaly stejné gradients a zůstaly identické, takže layer by nevyužila více features.

## Poznámka Anki 1790001406510

Karty Anki: 1790001406510
GUID: E~=|xL-Y]5; štítky: (žádné).

### Otázka (Front)

Jak se biases často inicializují?

### Odpověď (Back)

Na nulu nebo malé constants, pokud architecture nevyžaduje jiný prior.

## Poznámka Anki 1790001406511

Karty Anki: 1790001406511
GUID: uKnK[aQr:<; štítky: (žádné).

### Otázka (Front)

Jaký problém způsobí příliš malé initial weights?

### Odpověď (Back)

Signal a gradients mohou postupně mizet nebo jednotlivé units zůstat téměř lineární a nerozlišitelné.

## Poznámka Anki 1790001406512

Karty Anki: 1790001406512
GUID: iz#8$D`(<(; štítky: (žádné).

### Otázka (Front)

Jaký problém způsobí příliš velké initial weights?

### Odpověď (Back)

Activations a gradients mohou explodovat nebo saturovat nonlinearities.

## Poznámka Anki 1790001406513

Karty Anki: 1790001406513
GUID: oW{taplW.*; štítky: (žádné).

### Otázka (Front)

Jaký princip mají Xavier/Glorot-like initializations?

### Odpověď (Back)

Volí variance weights podle fan-in a fan-out tak, aby variance activations a gradients zůstávala napříč layers přibližně stabilní.

## Poznámka Anki 1790001406514

Karty Anki: 1790001406514
GUID: O.:;D@wINC; štítky: (žádné).

### Otázka (Front)

Proč lze orthogonal initialization použít v recurrent networks?

### Odpověď (Back)

Orthogonal recurrent matrix má singular values 1 a zpočátku lépe zachovává normy přes opakované multiplications.

## Poznámka Anki 1790001406515

Karty Anki: 1790001406515
GUID: lkHZzT#4;d; štítky: (žádné).

### Otázka (Front)

Co je adaptive learning-rate algorithm?

### Odpověď (Back)

Optimizer mění effective step size jednotlivých parameters podle historie jejich gradients.

## Poznámka Anki 1790001406516

Karty Anki: 1790001406516
GUID: oy+w}<LCJ0; štítky: (žádné).

### Otázka (Front)

Co je AdaGrad?

### Odpověď (Back)

Algorithm akumulující sum squared gradients pro každý parameter a dělící current gradient odmocninou této akumulace.

## Poznámka Anki 1790001406517

Karty Anki: 1790001406517
GUID: nc.a(ngoyJ; štítky: (žádné).

### Otázka (Front)

Jaký benefit má AdaGrad pro sparse features?

### Odpověď (Back)

Rarely updated parameters mají menší accumulated squared gradient a dostávají relativně větší effective learning rate.

