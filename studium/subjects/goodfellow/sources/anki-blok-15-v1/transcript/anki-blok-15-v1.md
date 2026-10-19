# Goodfellow – Blok 15 – karty 1401–1495

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 95 poznámek, 95 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001407318

Karty Anki: 1790001407318
GUID: h|_T?7cC/2; štítky: (žádné).

### Otázka (Front)

Co je Gaussian-Bernoulli RBM?

### Odpověď (Back)

RBM s real-valued Gaussian visible units a binary hidden units.

## Poznámka Anki 1790001407319

Karty Anki: 1790001407319
GUID: v_k/91N06F; štítky: (žádné).

### Otázka (Front)

Jaký conditional distribution má Gaussian visible layer given h?

### Odpověď (Back)

Gaussian s mean závislou na Wh+b a obvykle diagonal/isotropic covariance.

## Poznámka Anki 1790001407320

Karty Anki: 1790001407320
GUID: B)+HkBChY.; štítky: (žádné).

### Otázka (Front)

Proč diagonal covariance usnadňuje Gaussian RBM?

### Odpověď (Back)

Visible units zůstávají conditionally independent a sampling/inference nevyžaduje full matrix inversion.

## Poznámka Anki 1790001407321

Karty Anki: 1790001407321
GUID: ps2N&?MS9;; štítky: (žádné).

### Otázka (Front)

Co motivuje mean-and-covariance RBM?

### Odpověď (Back)

Natural images mají důležitou conditional covariance structure, kterou modelující pouze hidden-dependent mean nemusí zachytit.

## Poznámka Anki 1790001407322

Karty Anki: 1790001407322
GUID: i<A{YMI&ly; štítky: (žádné).

### Otázka (Front)

Co je spike-and-slab RBM?

### Odpověď (Back)

Model s binary spike variables určujícími aktivaci features a continuous slab variables určujícími jejich amplitudu.

## Poznámka Anki 1790001407323

Karty Anki: 1790001407323
GUID: O9_3{:8C5?; štítky: (žádné).

### Otázka (Front)

Jak spike-and-slab representation vytváří exact sparsity?

### Odpověď (Back)

Když spike=0, corresponding feature contribution je přesně nulová.

## Poznámka Anki 1790001407324

Karty Anki: 1790001407324
GUID: xf1gV:&b{w; štítky: (žádné).

### Otázka (Front)

Jaká validity podmínka je kritická u covariance-modulating models?

### Odpověď (Back)

Effective precision/covariance musí zůstat positive definite, jinak density nemusí být normalizovatelná.

## Poznámka Anki 1790001407325

Karty Anki: 1790001407325
GUID: wP8J*u*OZ@; štítky: (žádné).

### Otázka (Front)

Co je convolutional Boltzmann machine?

### Odpověď (Back)

Boltzmann model používající local connectivity a shared convolutional weights pro grid-structured data.

## Poznámka Anki 1790001407326

Karty Anki: 1790001407326
GUID: CoBgx)xvcT; štítky: (žádné).

### Otázka (Front)

Co je probabilistic max pooling?

### Odpověď (Back)

Stochastic pooling constraint, který v pool region dovoluje aktivaci nejvýše jednoho detector unit plus all-off state.

## Poznámka Anki 1790001407327

Karty Anki: 1790001407327
GUID: ufm6vtz!B[; štítky: (žádné).

### Otázka (Front)

Proč probabilistic max pooling snižuje počet local configurations?

### Odpověď (Back)

Místo 2^n binary detector patterns připouští pouze n+1 states.

## Poznámka Anki 1790001407328

Karty Anki: 1790001407328
GUID: Ej#k%-u9`H; štítky: (žádné).

### Otázka (Front)

Jaká nevýhoda má mutually exclusive probabilistic pooling?

### Odpověď (Back)

Zakazuje současný výskyt více features ve stejné pool region.

## Poznámka Anki 1790001407329

Karty Anki: 1790001407329
GUID: gn#)ggZ[~[; štítky: (žádné).

### Otázka (Front)

Co je conditional RBM pro sequences?

### Odpověď (Back)

RBM, jehož parameters, často biases, jsou functions previous time steps a parametrizují p(x_t|history).

## Poznámka Anki 1790001407330

Karty Anki: 1790001407330
GUID: d2SlVV@ZUF; štítky: (žádné).

### Otázka (Front)

Co je RNN-RBM?

### Odpověď (Back)

RNN vytváří time-dependent parameters RBM, která modeluje distribution current frame.

## Poznámka Anki 1790001407331

Karty Anki: 1790001407331
GUID: HH0R7}C?]9; štítky: (žádné).

### Otázka (Front)

Jak se RNN-RBM trénuje?

### Odpověď (Back)

RBM poskytne approximate gradients svých parameters a ty se backpropagují přes RNN pomocí BPTT.

## Poznámka Anki 1790001407332

Karty Anki: 1790001407332
GUID: L/?[`pb[P_; štítky: (žádné).

### Otázka (Front)

Co jsou higher-order Boltzmann machines?

### Odpověď (Back)

Energy models s multiplicative interactions tří nebo více variables.

## Poznámka Anki 1790001407333

Karty Anki: 1790001407333
GUID: MjaejKyW[!; štítky: (žádné).

### Otázka (Front)

Jaký benefit mohou mít three-way interactions?

### Odpověď (Back)

Mohou modelovat transformations, například vztah mezi dvěma video frames conditional na latent motion feature.

## Poznámka Anki 1790001407334

Karty Anki: 1790001407334
GUID: K1b}as^O)g; štítky: (žádné).

### Otázka (Front)

Co je reparameterization trick?

### Odpověď (Back)

Přepis stochastic sample y~p(y|ω) jako deterministic differentiable y=f(z;ω) s parameter-independent noise z.

## Poznámka Anki 1790001407335

Karty Anki: 1790001407335
GUID: h?na1(i5J5; štítky: (žádné).

### Otázka (Front)

Jak Gaussian reparameterization vypadá?

### Odpověď (Back)

z~N(0,I), y=μ+Lz nebo v diagonal case y=μ+σ⊙z.

## Poznámka Anki 1790001407336

Karty Anki: 1790001407336
GUID: iodQQ<:+zv; štítky: (žádné).

### Otázka (Front)

Proč reparameterization umožňuje low-variance pathwise gradients?

### Odpověď (Back)

Gradient prochází přímo differentiable function f při fixním sampled noise z.

## Poznámka Anki 1790001407337

Karty Anki: 1790001407337
GUID: wv#2V;7^lt; štítky: (žádné).

### Otázka (Front)

Proč standardní reparameterization nefunguje přímo pro discrete variables?

### Odpověď (Back)

Discrete sample vzniká discontinuous mappingem, jehož derivative je nulová nebo nedefinovaná téměř všude.

## Poznámka Anki 1790001407338

Karty Anki: 1790001407338
GUID: mx4irBBB4<; štítky: (žádné).

### Otázka (Front)

Co je REINFORCE estimator?

### Odpověď (Back)

Score-function gradient identity ∇θE[J(y)]=E[J(y)∇θlog p(y;θ)].

## Poznámka Anki 1790001407339

Karty Anki: 1790001407339
GUID: xQ<@pP|VT[; štítky: (žádné).

### Otázka (Front)

Jaká výhoda má REINFORCE?

### Odpověď (Back)

Funguje i pro discrete stochastic variables a je unbiased.

## Poznámka Anki 1790001407340

Karty Anki: 1790001407340
GUID: A_NErJ,~?J; štítky: (žádné).

### Otázka (Front)

Jaká hlavní nevýhoda REINFORCE?

### Odpověď (Back)

Typicky velmi vysoká variance gradient estimates.

## Poznámka Anki 1790001407341

Karty Anki: 1790001407341
GUID: s#31;p9aRO; štítky: (žádné).

### Otázka (Front)

Jak baseline snižuje REINFORCE variance?

### Odpověď (Back)

Nahradí J(y) termem J(y)−b, kde b nezávisí na sampled y a aproximuje expected cost.

## Poznámka Anki 1790001407342

Karty Anki: 1790001407342
GUID: CzBwuh?yVG; štítky: (žádné).

### Otázka (Front)

Proč baseline nemění expected gradient?

### Odpověď (Back)

E[∇θlog p(y;θ)]=0.

## Poznámka Anki 1790001407343

Karty Anki: 1790001407343
GUID: GJh9)0diCN; štítky: (žádné).

### Otázka (Front)

Co je sigmoid belief network?

### Odpověď (Back)

Directed generative model s binary units, jejichž conditional Bernoulli probabilities jsou sigmoid functions parents.

## Poznámka Anki 1790001407344

Karty Anki: 1790001407344
GUID: k({|DZVxe>; štítky: (žádné).

### Otázka (Front)

Proč sigmoid belief network snadno generuje samples?

### Odpověď (Back)

DAG dovoluje ancestral sampling od top latent variables k visibles.

## Poznámka Anki 1790001407345

Karty Anki: 1790001407345
GUID: fCZ(%4f:zs; štítky: (žádné).

### Otázka (Front)

Proč je posterior sigmoid belief network obtížný?

### Odpověď (Back)

Conditioning na descendants indukuje explaining-away dependencies mezi latent parents.

## Poznámka Anki 1790001407346

Karty Anki: 1790001407346
GUID: fhDq>x&/]:; štítky: (žádné).

### Otázka (Front)

Co je Helmholtz machine?

### Odpověď (Back)

Directed generative network doplněná recognition/inference network pro approximate posterior inference.

## Poznámka Anki 1790001407347

Karty Anki: 1790001407347
GUID: Oeemx$Qk?|; štítky: (žádné).

### Otázka (Front)

Co je differentiable generator network?

### Odpověď (Back)

Neural network transformující simple latent noise z na generated sample x nebo parameters p(x|z).

## Poznámka Anki 1790001407348

Karty Anki: 1790001407348
GUID: pwTu2I+%v+; štítky: (žádné).

### Otázka (Front)

Jak invertible differentiable generator umožňuje exact density?

### Odpověď (Back)

Change-of-variables formula používá base density a determinant Jacobianu transformation.

## Poznámka Anki 1790001407349

Karty Anki: 1790001407349
GUID: sFEH;_~&@W; štítky: (žádné).

### Otázka (Front)

Co je variational autoencoder (VAE)?

### Odpověď (Back)

Directed latent-variable model s generative decoderem p(x|z) a amortized inference network q(z|x), trénovaný maximalizací ELBO.

## Poznámka Anki 1790001407350

Karty Anki: 1790001407350
GUID: QE_2](G|hc; štítky: (žádné).

### Otázka (Front)

Jaká je standardní VAE ELBO?

### Odpověď (Back)

E_{q(z|x)}[log p(x|z)]−D_KL(q(z|x)||p(z)).

## Poznámka Anki 1790001407351

Karty Anki: 1790001407351
GUID: n-~MmH#.P$; štítky: (žádné).

### Otázka (Front)

Jak se interpretuje reconstruction term VAE?

### Odpověď (Back)

Latent sample musí umožnit decoderu přiřadit observed x vysokou conditional likelihood.

## Poznámka Anki 1790001407352

Karty Anki: 1790001407352
GUID: jHWS,=7wWe; štítky: (žádné).

### Otázka (Front)

Jak se interpretuje KL term VAE?

### Odpověď (Back)

Approximate posterior codes mají zůstat kompatibilní s generative prior p(z).

## Poznámka Anki 1790001407353

Karty Anki: 1790001407353
GUID: xqVUIfW9u/; štítky: (žádné).

### Otázka (Front)

Proč je VAE encoder stochastic?

### Odpověď (Back)

Produkuje parameters distribution q(z|x), ze které se během trainingu sampleuje latent z.

## Poznámka Anki 1790001407354

Karty Anki: 1790001407354
GUID: e{].i7|K)0; štítky: (žádné).

### Otázka (Front)

Jak se gradient propaguje přes VAE latent sample?

### Odpověď (Back)

Pomocí reparameterization tricku.

## Poznámka Anki 1790001407355

Karty Anki: 1790001407355
GUID: FC::0-fj0}; štítky: (žádné).

### Otázka (Front)

Co znamená amortized inference ve VAE?

### Odpověď (Back)

Shared encoder network nahradí samostatnou iterative variational optimization pro každý example.

## Poznámka Anki 1790001407356

Karty Anki: 1790001407356
GUID: Q?([`j5r%Z; štítky: (žádné).

### Otázka (Front)

Proč mohou Gaussian-decoder VAE samples působit blurry?

### Odpověď (Back)

Pixel-wise Gaussian/MSE likelihood může odměňovat averaging několika plausible fine-detail outcomes.

## Poznámka Anki 1790001407357

Karty Anki: 1790001407357
GUID: cvf=/~uz2b; štítky: (žádné).

### Otázka (Front)

Co je posterior collapse/use of few latent dimensions v VAE?

### Odpověď (Back)

Decoder může ignorovat část z a q(z|x) pro tyto dimensions zůstává blízko prioru.

## Poznámka Anki 1790001407358

Karty Anki: 1790001407358
GUID: sXi(=dH)UY; štítky: (žádné).

### Otázka (Front)

Co je importance-weighted autoencoder (IWAE)?

### Odpověď (Back)

Variational objective používající více importance samples k vytvoření tighter lower bound na log p(x).

## Poznámka Anki 1790001407359

Karty Anki: 1790001407359
GUID: OIP%-0s@.e; štítky: (žádné).

### Otázka (Front)

Jak se IWAE bound mění s počtem samples k?

### Odpověď (Back)

Typicky se s větším k ztěsňuje a k=1 odpovídá standardní VAE ELBO.

## Poznámka Anki 1790001407360

Karty Anki: 1790001407360
GUID: Q>LX^(QdJF; štítky: (žádné).

### Otázka (Front)

Co je generative adversarial network (GAN)?

### Odpověď (Back)

Implicit generative model s generator networkou a discriminator classifierem trénovanými v adversarial game.

## Poznámka Anki 1790001407361

Karty Anki: 1790001407361
GUID: G=GgqsJY28; štítky: (žádné).

### Otázka (Front)

Jaký objective má základní GAN?

### Odpověď (Back)

min_G max_D E_{data}log D(x)+E_z log(1−D(G(z))).

## Poznámka Anki 1790001407362

Karty Anki: 1790001407362
GUID: rKh?r%&AB(; štítky: (žádné).

### Otázka (Front)

Co se discriminator učí?

### Odpověď (Back)

Rozlišovat real data od generated samples.

## Poznámka Anki 1790001407363

Karty Anki: 1790001407363
GUID: K(dMF4Iru*; štítky: (žádné).

### Otázka (Front)

Co se generator učí?

### Odpověď (Back)

Měnit generated distribution tak, aby discriminator fake samples považoval za real.

## Poznámka Anki 1790001407364

Karty Anki: 1790001407364
GUID: Nui*5r@CQ#; štítky: (žádné).

### Otázka (Front)

Jak vypadá idealizované GAN equilibrium?

### Odpověď (Back)

p_model=p_data a optimal discriminator vrací 1/2 pro oba zdroje.

## Poznámka Anki 1790001407365

Karty Anki: 1790001407365
GUID: sQ8T^#.Yx|; štítky: (žádné).

### Otázka (Front)

Jakou computational výhodu má GAN training?

### Odpověď (Back)

Nepotřebuje explicitní posterior inference ani partition-function gradient.

## Poznámka Anki 1790001407366

Karty Anki: 1790001407366
GUID: AQm}J3d[C:; štítky: (žádné).

### Otázka (Front)

Proč GAN optimization není obyčejná minimization?

### Odpověď (Back)

Jde o two-player nonconvex game, kde současné gradient dynamics mohou oscilovat.

## Poznámka Anki 1790001407367

Karty Anki: 1790001407367
GUID: g<}AfD{h`C; štítky: (žádné).

### Otázka (Front)

Proč good GAN samples neimplikují high likelihood?

### Odpověď (Back)

Implicit generator může pokrývat jen low-dimensional manifold, dropovat modes nebo nemít tractable density.

## Poznámka Anki 1790001407368

Karty Anki: 1790001407368
GUID: R^e=un9xj; štítky: (žádné).

### Otázka (Front)

Co je mode dropping?

### Odpověď (Back)

Generator reprezentuje jen subset data modes a jiné plausible regions téměř nikdy negeneruje.

## Poznámka Anki 1790001407369

Karty Anki: 1790001407369
GUID: 8_)fQz1jh; štítky: (žádné).

### Otázka (Front)

Co jsou generative moment matching networks?

### Odpověď (Back)

Generators trained tak, aby statistics generated samples odpovídaly data statistics bez discriminatoru nebo explicitní likelihood.

## Poznámka Anki 1790001407370

Karty Anki: 1790001407370
GUID: f)JxsgRQ(k; štítky: (žádné).

### Otázka (Front)

Co je maximum mean discrepancy (MMD)?

### Odpověď (Back)

Kernel-based distance mezi distributions porovnávající jejich mean embeddings ve feature space.

## Poznámka Anki 1790001407371

Karty Anki: 1790001407371
GUID: N~^M4ryLLb; štítky: (žádné).

### Otázka (Front)

Kdy je MMD při characteristic kernelu nulová?

### Odpověď (Back)

Právě když jsou distributions stejné.

## Poznámka Anki 1790001407372

Karty Anki: 1790001407372
GUID: wd(/5nLYNf; štítky: (žádné).

### Otázka (Front)

Proč lze MMD počítat z minibatches?

### Odpověď (Back)

Mean embeddings se aproximují empirical averages samples z dat a generatoru.

## Poznámka Anki 1790001407373

Karty Anki: 1790001407373
GUID: k8Ldk*T]F@; štítky: (žádné).

### Otázka (Front)

Proč lze moment matching provádět v autoencoder feature space?

### Odpověď (Back)

Learned representation může zdůraznit semantic structure a učinit distribution snáze matchovatelnou než raw pixels.

## Poznámka Anki 1790001407374

Karty Anki: 1790001407374
GUID: kysX2L~iy<; štítky: (žádné).

### Otázka (Front)

Co je autoregressive generative model?

### Odpověď (Back)

Model factorující joint p(x)=∏_i p(x_i|x_<i) podle zvoleného ordering.

## Poznámka Anki 1790001407375

Karty Anki: 1790001407375
GUID: wlo?R8kLG|; štítky: (žádné).

### Otázka (Front)

Proč má autoregressive model tractable normalized likelihood?

### Odpověď (Back)

Každý factor je normalizovaná conditional distribution a nejsou zde latent variables k marginalizaci.

## Poznámka Anki 1790001407376

Karty Anki: 1790001407376
GUID: rb.5X8%$hr; štítky: (žádné).

### Otázka (Front)

Jaká nevýhoda autoregressive sampling?

### Odpověď (Back)

Variables se často generují sekvenčně, takže sampling je pomalejší než parallel one-shot generator.

## Poznámka Anki 1790001407377

Karty Anki: 1790001407377
GUID: NEpT9,LM[); štítky: (žádné).

### Otázka (Front)

Jaký design choice ovlivňuje autoregressive model?

### Odpověď (Back)

Ordering variables.

## Poznámka Anki 1790001407378

Karty Anki: 1790001407378
GUID: 3{OG04tOo; štítky: (žádné).

### Otázka (Front)

Co je NADE?

### Odpověď (Back)

Neural autoregressive density estimator se shared hidden computations napříč conditional predictions.

## Poznámka Anki 1790001407379

Karty Anki: 1790001407379
GUID: unUU{Gx_wj; štítky: (žádné).

### Otázka (Front)

Jaký benefit má NADE oproti naive independent neural conditional networks?

### Odpověď (Back)

Parameter a computation sharing snižují cost a zlepšují statistical efficiency.

## Poznámka Anki 1790001407380

Karty Anki: 1790001407380
GUID: qil>Gp~35A; štítky: (žádné).

### Otázka (Front)

Jak NADE historicky souvisí s RBM inference?

### Odpověď (Back)

Jeho weight-sharing a forward computation byly motivovány approximate mean-field-like inference v RBM.

## Poznámka Anki 1790001407381

Karty Anki: 1790001407381
GUID: qq%7]-8u(4; štítky: (žádné).

### Otázka (Front)

Co je NADE-k?

### Odpověď (Back)

Extension napodobující více recurrent inference iterations před jednotlivými autoregressive predictions.

## Poznámka Anki 1790001407382

Karty Anki: 1790001407382
GUID: zf@kJ3jf~s; štítky: (žádné).

### Otázka (Front)

Co je RNADE?

### Odpověď (Back)

Continuous NADE, kde jednotlivé conditionals mohou být například mixtures of Gaussians.

## Poznámka Anki 1790001407383

Karty Anki: 1790001407383
GUID: m#0p(KVX~%; štítky: (žádné).

### Otázka (Front)

Jak lze autoregressive model učit bez fixed ordering?

### Odpověď (Back)

Randomizovat orderings během trainingu a informovat model, které variables jsou observed.

## Poznámka Anki 1790001407384

Karty Anki: 1790001407384
GUID: CImkx](C/k; štítky: (žádné).

### Otázka (Front)

Jaký benefit má order-agnostic training?

### Odpověď (Back)

Jeden model může odpovídat na různé conditional/missing-data queries.

## Poznámka Anki 1790001407385

Karty Anki: 1790001407385
GUID: FT;S,S=nog; štítky: (žádné).

### Otázka (Front)

Jak lze denoising autoencoder použít jako generative model?

### Odpověď (Back)

Definovat Markov chain, která střídá corruption x→x̃ a stochastic reconstruction x̃→x.

## Poznámka Anki 1790001407386

Karty Anki: 1790001407386
GUID: yDl1RHYX:I; štítky: (žádné).

### Otázka (Front)

Proč corruption potřebuje stochasticity?

### Odpověď (Back)

Umožňuje chain procházet state space místo deterministického zacyklení v jednom reconstruction pointu.

## Poznámka Anki 1790001407387

Karty Anki: 1790001407387
GUID: Q0JDP5<nPw; štítky: (žádné).

### Otázka (Front)

Co je walk-back training?

### Odpověď (Back)

Trénink DAE na states navštívených několika kroky jeho vlastní generative Markov chain, aby se naučil opravovat i vzdálenější errors/spurious regions.

## Poznámka Anki 1790001407388

Karty Anki: 1790001407388
GUID: hg:pA~e,Ff; štítky: (žádné).

### Otázka (Front)

Jak walk-back připomíná contrastive divergence?

### Odpověď (Back)

Obě metody spouštějí krátkou chain z data points a používají states, do nichž model od dat odchází, k learningu.

## Poznámka Anki 1790001407389

Karty Anki: 1790001407389
GUID: FtOA#+$7RD; štítky: (žádné).

### Otázka (Front)

Co je generative stochastic network (GSN)?

### Odpověď (Back)

Model parametrizující stochastic transition process nad visible a latent states, jehož stationary distribution má odpovídat datům.

## Poznámka Anki 1790001407390

Karty Anki: 1790001407390
GUID: Nr.u*Hrcps; štítky: (žádné).

### Otázka (Front)

Jak se GSN liší od explicit-density modelu?

### Odpověď (Back)

Joint density může být implicitně definována dlouhodobým behavior transition operatoru místo explicitního p(x) vzorce.

## Poznámka Anki 1790001407391

Karty Anki: 1790001407391
GUID: r!,-|8I*#8; štítky: (žádné).

### Otázka (Front)

Jak lze GSN použít pro structured conditional prediction?

### Odpověď (Back)

Clampnout observed inputs a nechat Markov chain resamplovat dependent output variables a hidden states.

## Poznámka Anki 1790001407392

Karty Anki: 1790001407392
GUID: MGQWCu;=+k; štítky: (žádné).

### Otázka (Front)

Jaký princip používá diffusion inversion model popsaný v knize?

### Odpověď (Back)

Forward process postupně přidává noise a reverse learned process se učí malé denoising steps zpět k data distribution.

## Poznámka Anki 1790001407393

Karty Anki: 1790001407393
GUID: lIKnG)FAi,; štítky: (žádné).

### Otázka (Front)

Proč multiple small denoising steps mohou být snazší než jeden velký?

### Odpověď (Back)

Každý local reverse conditional je jednodušší než rekonstrukce clean data z velmi silně corrupted inputu jedním skokem.

## Poznámka Anki 1790001407394

Karty Anki: 1790001407394
GUID: Bw89`-?8)z; štítky: (žádné).

### Otázka (Front)

Jak se diffusion-like reverse chain liší od MCMC inference pro fixed EBM?

### Odpověď (Back)

Reverse transitions samy definují generative model distribution; nejsou jen approximate samplerem jiné explicitně definované density.

## Poznámka Anki 1790001407395

Karty Anki: 1790001407395
GUID: jBs:;pLbpA; štítky: (žádné).

### Otázka (Front)

Co je approximate Bayesian computation (ABC) v broad sampling contextu?

### Odpověď (Back)

Likelihood-free approach používající generated samples a summary statistics k přijímání nebo modifikaci simulations.

## Poznámka Anki 1790001407396

Karty Anki: 1790001407396
GUID: d{Lm*eW7#*; štítky: (žádné).

### Otázka (Front)

Proč je evaluation generative models obtížná?

### Odpověď (Back)

Likelihood může být intractable nebo zavádějící, sample quality subjektivní a různé models mohou optimalizovat odlišné vlastnosti distribution.

## Poznámka Anki 1790001407397

Karty Anki: 1790001407397
GUID: AV%3S8zJ2*; štítky: (žádné).

### Otázka (Front)

Proč nelze přímo srovnávat exact-ish likelihood jednoho modelu s loose lower boundem jiného?

### Odpověď (Back)

Rozdíl může pocházet z approximation gapu místo skutečného rozdílu true likelihood.

## Poznámka Anki 1790001407398

Karty Anki: 1790001407398
GUID: wnwGwq958#; štítky: (žádné).

### Otázka (Front)

Jak špatný partition-function estimate může zkreslit likelihood?

### Odpověď (Back)

Podhodnocené Z uměle nadhodnotí normalized log p(x).

## Poznámka Anki 1790001407399

Karty Anki: 1790001407399
GUID: tR(N|abYhz; štítky: (žádné).

### Otázka (Front)

Proč preprocessing musí být při likelihood comparison stejný?

### Odpověď (Back)

Transformace, discretization a noise mění samotnou probability space a numerical scale density.

## Poznámka Anki 1790001407400

Karty Anki: 1790001407400
GUID: h1->[U3I[1; štítky: (žádné).

### Otázka (Front)

Proč nelze přímo porovnávat discrete probability mass a continuous density hodnoty?

### Odpověď (Back)

Mají odlišné measure a units; změna bin width nebo coordinate scale mění continuous density.

## Poznámka Anki 1790001407401

Karty Anki: 1790001407401
GUID: flj6?v0BVz; štítky: (žádné).

### Otázka (Front)

Jaký benefit má visual inspection samples?

### Odpověď (Back)

Odhaluje perceptual artifacts a zda generator vytváří plausibilní examples.

## Poznámka Anki 1790001407402

Karty Anki: 1790001407402
GUID: czo^~6nj!k; štítky: (žádné).

### Otázka (Front)

Proč visual inspection sama nestačí?

### Odpověď (Back)

Neodhalí spolehlivě memorization, mode dropping ani nesprávné relative mode probabilities.

## Poznámka Anki 1790001407403

Karty Anki: 1790001407403
GUID: wC.@{pztvA; štítky: (žádné).

### Otázka (Front)

Jak nearest-neighbor analysis pomáhá evaluation generatoru?

### Odpověď (Back)

Porovnáním generated samples s training examples lze odhalit zjevné copying/memorization.

## Poznámka Anki 1790001407404

Karty Anki: 1790001407404
GUID: u:Zq[`XMn); štítky: (žádné).

### Otázka (Front)

Jak může model současně overfit i underfit?

### Odpověď (Back)

Může memorovat subset training modes a současně ignorovat jiné modes data distribution.

## Poznámka Anki 1790001407405

Karty Anki: 1790001407405
GUID: PvXuc-tOm.; štítky: (žádné).

### Otázka (Front)

Proč vysoká likelihood nemusí znamenat perceptuálně lepší samples?

### Odpověď (Back)

Model může získat likelihood modelováním statistically easy low-level details, které málo souvisejí s human perceptual quality.

## Poznámka Anki 1790001407406

Karty Anki: 1790001407406
GUID: ONIk^/DbOD; štítky: (žádné).

### Otázka (Front)

Jak forward KL D_KL(p_data||p_model) penalizuje mode dropping?

### Odpověď (Back)

Silně penalizuje data-supported regions, kde p_model přiděluje malou nebo nulovou probability.

## Poznámka Anki 1790001407407

Karty Anki: 1790001407407
GUID: y0(Eil*M#b; štítky: (žádné).

### Otázka (Front)

Jak reverse KL D_KL(p_model||p_data) penalizuje unrealistic samples?

### Odpověď (Back)

Silně penalizuje regions, kam model dává mass, ale data distribution tam má nízkou probability.

## Poznámka Anki 1790001407408

Karty Anki: 1790001407408
GUID: B&BM~m<ihL; štítky: (žádné).

### Otázka (Front)

Jaký sjednocující problém řeší VAE, GAN a MMD generator?

### Odpověď (Back)

Jak naučit mapping z latent noise k data-like samples, když observed data neposkytují corresponding latent z.

## Poznámka Anki 1790001407409

Karty Anki: 1790001407409
GUID: wmX!.k#[)d; štítky: (žádné).

### Otázka (Front)

Jak se learning signal liší mezi VAE, GAN a MMD?

### Odpověď (Back)

VAE používá likelihood lower bound a inference network; GAN discriminator; MMD sample-statistic discrepancy.

## Poznámka Anki 1790001407410

Karty Anki: 1790001407410
GUID: t3:g:a$9v7; štítky: (žádné).

### Otázka (Front)

Jaký trade-off je mezi autoregressive modely a one-shot implicit generators?

### Odpověď (Back)

Autoregressive models mají tractable likelihood, ale sequential sampling; implicit generators sampleují rychle, ale density nemusí být dostupná.

## Poznámka Anki 1790001407411

Karty Anki: 1790001407411
GUID: H/|m;ueEO^; štítky: (žádné).

### Otázka (Front)

Jaký sjednocující princip spojuje DAE chains, GSN a diffusion inversion?

### Odpověď (Back)

Generování lze realizovat jako learned stochastic dynamiku, která opakovaně transformuje noisy/partial states směrem k data-like configurations.

## Poznámka Anki 1790001407412

Karty Anki: 1790001407412
GUID: qWxg=suz~a; štítky: (žádné).

### Otázka (Front)

Jaký širší cíl mají deep generative models?

### Odpověď (Back)

Současně modelovat komplexní distribution dat, generovat samples a poskytovat latent distributed representations pro inference a reasoning under uncertainty.

