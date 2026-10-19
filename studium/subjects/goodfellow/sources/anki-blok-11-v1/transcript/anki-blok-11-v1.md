# Goodfellow – Blok 11 – karty 1001–1100

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001406918

Karty Anki: 1790001406918
GUID: o}%/j@Cb9d; štítky: (žádné).

### Otázka (Front)

Zaručuje malý code dimensionality dobrou representation?

### Odpověď (Back)

Ne; dostatečně high-capacity nonlinear functions mohou memorovat training set i přes úzký bottleneck.

## Poznámka Anki 1790001406919

Karty Anki: 1790001406919
GUID: f|44$|2$^S; štítky: (žádné).

### Otázka (Front)

Co je overcomplete autoencoder?

### Odpověď (Back)

Autoencoder s code dimensionality větší než input dimensionality.

## Poznámka Anki 1790001406920

Karty Anki: 1790001406920
GUID: mngO?;S,3M; štítky: (žádné).

### Otázka (Front)

Proč overcomplete autoencoder potřebuje regularization?

### Odpověď (Back)

Bez ní může velmi snadno realizovat identity mapping a nic užitečného se nenaučit.

## Poznámka Anki 1790001406921

Karty Anki: 1790001406921
GUID: mx.]%VW@8h; štítky: (žádné).

### Otázka (Front)

Co je regularized autoencoder?

### Odpověď (Back)

Autoencoder, jehož learning criterion omezuje representation nebo sensitivity jinak než samotnou code dimensionality.

## Poznámka Anki 1790001406922

Karty Anki: 1790001406922
GUID: qg7eB8@**|; štítky: (žádné).

### Otázka (Front)

Jaké regularization properties kapitola uvádí?

### Odpověď (Back)

Sparsity, robustness vůči noise a malou sensitivity representation vůči input perturbations.

## Poznámka Anki 1790001406923

Karty Anki: 1790001406923
GUID: AYxlbJU0tk; štítky: (žádné).

### Otázka (Front)

Co je sparse autoencoder?

### Odpověď (Back)

Autoencoder s penalty podporující sparse hidden activations.

## Poznámka Anki 1790001406924

Karty Anki: 1790001406924
GUID: IxjabQtV4); štítky: (žádné).

### Otázka (Front)

Jak vypadá generic sparse-autoencoder loss?

### Odpověď (Back)

L(x,g(f(x)))+Ω(f(x)), kde Ω penalizuje nežádoucí code pattern, například L¹ activations.

## Poznámka Anki 1790001406925

Karty Anki: 1790001406925
GUID: t!MW&$v+^@; štítky: (žádné).

### Otázka (Front)

Jak sparse autoencoder brání identity solution?

### Odpověď (Back)

Každý input smí efektivně využít jen subset available features.

## Poznámka Anki 1790001406926

Karty Anki: 1790001406926
GUID: p1?gt.oU3w; štítky: (žádné).

### Otázka (Front)

Jaký latent prior odpovídá L¹ activation penalty?

### Odpověď (Back)

Laplace-like prior nad latent representation.

## Poznámka Anki 1790001406927

Karty Anki: 1790001406927
GUID: w@sp~yNv_.; štítky: (žádné).

### Otázka (Front)

Jak se prior nad h liší od Bayesian prioru nad parameters θ?

### Odpověď (Back)

p(h) modeluje distribution latent variables pro examples; p(θ) vyjadřuje uncertainty nebo preference nad model parameters.

## Poznámka Anki 1790001406928

Karty Anki: 1790001406928
GUID: cM2tMT&-we; štítky: (žádné).

### Otázka (Front)

Jak lze autoencoder probabilisticky interpretovat?

### Odpověď (Back)

Encoder aproximuje inference latent code a decoder parametrizuje conditional distribution p(x|h).

## Poznámka Anki 1790001406929

Karty Anki: 1790001406929
GUID: qx?o(~Ud$B; štítky: (žádné).

### Otázka (Front)

Jaký decoder odpovídá MSE reconstruction u real-valued x?

### Odpověď (Back)

Gaussian decoder s mean g(h) a fixed variance.

## Poznámka Anki 1790001406930

Karty Anki: 1790001406930
GUID: k`gH=j(0[g; štítky: (žádné).

### Otázka (Front)

Jaký decoder odpovídá binary cross-entropy reconstruction?

### Odpověď (Back)

Bernoulli decoder se sigmoid probabilities.

## Poznámka Anki 1790001406931

Karty Anki: 1790001406931
GUID: ey.,lcsysv; štítky: (žádné).

### Otázka (Front)

Co je stochastic encoder?

### Odpověď (Back)

Conditional distribution p_encoder(h|x), z níž se latent code sampleuje.

## Poznámka Anki 1790001406932

Karty Anki: 1790001406932
GUID: Dh=m`9>OkO; štítky: (žádné).

### Otázka (Front)

Co je stochastic decoder?

### Odpověď (Back)

Conditional distribution p_decoder(x|h) namísto deterministic reconstruction pointu.

## Poznámka Anki 1790001406933

Karty Anki: 1790001406933
GUID: lGIG*}>}.); štítky: (žádné).

### Otázka (Front)

Co je denoising autoencoder (DAE)?

### Odpověď (Back)

Autoencoder trénovaný rekonstruovat clean x z corrupted inputu x̃ sampled z corruption process C(x̃|x).

## Poznámka Anki 1790001406934

Karty Anki: 1790001406934
GUID: o#)mdBMRnc; štítky: (žádné).

### Otázka (Front)

Jaký objective DAE minimalizuje?

### Odpověď (Back)

Expected reconstruction loss L(x,g(f(x̃))) přes data a corruption noise.

## Poznámka Anki 1790001406935

Karty Anki: 1790001406935
GUID: K:KQ[wZhIL; štítky: (žádné).

### Otázka (Front)

Proč corruption regularizuje autoencoder?

### Odpověď (Back)

Input a target nejsou totožné, takže model musí využít data structure k odstranění noise místo prostého kopírování.

## Poznámka Anki 1790001406936

Karty Anki: 1790001406936
GUID: oRd2AP&2f`; štítky: (žádné).

### Otázka (Front)

Může být DAE overcomplete?

### Odpověď (Back)

Ano; corruption sama může zabránit trivial identity learningu.

## Poznámka Anki 1790001406937

Karty Anki: 1790001406937
GUID: DWIcjd=e_Q; štítky: (žádné).

### Otázka (Front)

Jak DAE implicitně využívá p_data(x)?

### Odpověď (Back)

K úspěšnému denoisingu musí rozpoznat, které clean configurations jsou pravděpodobné vzhledem k training data.

## Poznámka Anki 1790001406938

Karty Anki: 1790001406938
GUID: f}tBYDZ2J&; štítky: (žádné).

### Otázka (Front)

Co je score probability density?

### Odpověď (Back)

∇_x log p(x), vector ukazující lokální směr růstu log density.

## Poznámka Anki 1790001406939

Karty Anki: 1790001406939
GUID: kN1~88C<Y|; štítky: (žádné).

### Otázka (Front)

Jak reconstruction vector field DAE souvisí se score?

### Odpověď (Back)

Při malém Gaussian corruption a squared loss může r(x)−x aproximovat scale-multiple score smoothed data density.

## Poznámka Anki 1790001406940

Karty Anki: 1790001406940
GUID: K7gKGn^uR2; štítky: (žádné).

### Otázka (Front)

Jak interpretovat r(x)−x mimo high-density manifold?

### Odpověď (Back)

Jako local direction směřující input k regionům vyšší learned probability.

## Poznámka Anki 1790001406941

Karty Anki: 1790001406941
GUID: l%0;aM!ut]; štítky: (žádné).

### Otázka (Front)

Proč jsou reconstruction vectors malé v high-density regions?

### Odpověď (Back)

Training data tam mají být přibližně fixed points reconstruction mappingu.

## Poznámka Anki 1790001406942

Karty Anki: 1790001406942
GUID: mTF`>emJ-l; štítky: (žádné).

### Otázka (Front)

Jaký limitation má score interpretation při fixed nonzero noise?

### Odpověď (Back)

Modeluje smoothed/blurred version data distribution místo přesného unsmoothed p_data.

## Poznámka Anki 1790001406943

Karty Anki: 1790001406943
GUID: tp_AHPn]#@; štítky: (žádné).

### Otázka (Front)

Co je manifold assumption?

### Odpověď (Back)

Data probability mass je soustředěna poblíž low-dimensional manifold v high-dimensional input space.

## Poznámka Anki 1790001406944

Karty Anki: 1790001406944
GUID: uD=GDNk7R<; štítky: (žádné).

### Otázka (Front)

Co je tangent plane manifoldu v bodě x?

### Odpověď (Back)

Local linear subspace directions, ve kterých se lze infinitesimálně pohybovat a zůstat přibližně na manifold.

## Poznámka Anki 1790001406945

Karty Anki: 1790001406945
GUID: IS~?U!X7G$; štítky: (žádné).

### Otázka (Front)

Jaké directions by měl manifold-learning autoencoder zachovávat?

### Odpověď (Back)

Variations tangent to the data manifold.

## Poznámka Anki 1790001406946

Karty Anki: 1790001406946
GUID: N(7`|>dZ_U; štítky: (žádné).

### Otázka (Front)

Vůči jakým directions by měl být regularized autoencoder insensitive?

### Odpověď (Back)

Perturbations orthogonal to manifold, které vedou do low-probability regions.

## Poznámka Anki 1790001406947

Karty Anki: 1790001406947
GUID: u9PlQ(yHKE; štítky: (žádné).

### Otázka (Front)

Proč kombinace reconstruction a insensitivity může odhalit manifold?

### Odpověď (Back)

Reconstruction nutí zachovat on-manifold information, zatímco regularization umožní kontrakci nepotřebných off-manifold directions.

## Poznámka Anki 1790001406948

Karty Anki: 1790001406948
GUID: I#~{HIkLnb; štítky: (žádné).

### Otázka (Front)

Co je contractive autoencoder (CAE)?

### Odpověď (Back)

Autoencoder s explicitní penalty na Jacobian encoderu vzhledem k inputu.

## Poznámka Anki 1790001406949

Karty Anki: 1790001406949
GUID: oZc$h~UM=J; štítky: (žádné).

### Otázka (Front)

Jak vypadá CAE penalty?

### Odpověď (Back)

λ||∂f(x)/∂x||_F².

## Poznámka Anki 1790001406950

Karty Anki: 1790001406950
GUID: em7&l$+P|n; štítky: (žádné).

### Otázka (Front)

Co CAE penalty podporuje?

### Odpověď (Back)

Local insensitivity latent representation vůči input perturbations kolem training examples.

## Poznámka Anki 1790001406951

Karty Anki: 1790001406951
GUID: z#UEN}I)cd; štítky: (žádné).

### Otázka (Front)

Proč CAE nemůže udělat encoder úplně konstantní?

### Odpověď (Back)

Reconstruction objective stále vyžaduje zachovat information potřebnou k rekonstrukci training data.

## Poznámka Anki 1790001406952

Karty Anki: 1790001406952
GUID: dD6]MPQ~WU; štítky: (žádné).

### Otázka (Front)

Jak lze z CAE Jacobianu odhadnout tangent directions?

### Odpověď (Back)

Directions s největšími singular values Jacobianu odpovídají input variations, na které representation zůstává citlivá.

## Poznámka Anki 1790001406953

Karty Anki: 1790001406953
GUID: t[ropD^3lt; štítky: (žádné).

### Otázka (Front)

Jaký scaling loophole může obejít CAE penalty?

### Odpověď (Back)

Encoder může svůj output škálovat malým ε a decoder opačně velkým faktorem, čímž se zmenší encoder Jacobian bez ztráty reconstruction.

## Poznámka Anki 1790001406954

Karty Anki: 1790001406954
GUID: GWzzhj[QoB; štítky: (žádné).

### Otázka (Front)

Jak tied weights pomáhají proti scaling degeneracy CAE?

### Odpověď (Back)

Svazují encoder a decoder scales, takže nelze libovolně zmenšit jeden a zvětšit druhý.

## Poznámka Anki 1790001406955

Karty Anki: 1790001406955
GUID: g+HwFCyeYi; štítky: (žádné).

### Otázka (Front)

Jak se DAE a CAE liší v regularization mechanismu?

### Odpověď (Back)

DAE trénuje robustness k finite sampled corruptions; CAE penalizuje infinitesimal sensitivity přes Jacobian.

## Poznámka Anki 1790001406956

Karty Anki: 1790001406956
GUID: P;~r*lH48/; štítky: (žádné).

### Otázka (Front)

Jaký limit vztahuje Gaussian DAE a contractive penalties?

### Odpověď (Back)

Pro malé Gaussian noise lze denoising objective rozvinout do reconstruction termu plus derivative-based regularization.

## Poznámka Anki 1790001406957

Karty Anki: 1790001406957
GUID: Aq6,dAbtP^; štítky: (žádné).

### Otázka (Front)

Co je predictive sparse decomposition (PSD)?

### Odpověď (Back)

Model kombinující sparse latent optimization s parametric encoderem, který se učí tuto inference rychle aproximovat.

## Poznámka Anki 1790001406958

Karty Anki: 1790001406958
GUID: IE_~}uUqp5; štítky: (žádné).

### Otázka (Front)

Jaký typický PSD objective používá kniha?

### Odpověď (Back)

||x−g(h)||²+λ||h||₁+γ||h−f(x)||².

## Poznámka Anki 1790001406959

Karty Anki: 1790001406959
GUID: [~aZ-#G+c; štítky: (žádné).

### Otázka (Front)

Co dělá termín ||x−g(h)||² v PSD?

### Odpověď (Back)

Nutí latent code rekonstruovat input.

## Poznámka Anki 1790001406960

Karty Anki: 1790001406960
GUID: Byd~vf_ZaY; štítky: (žádné).

### Otázka (Front)

Co dělá λ||h||₁?

### Odpověď (Back)

Podporuje sparsity code.

## Poznámka Anki 1790001406961

Karty Anki: 1790001406961
GUID: i&eMcaaS3; štítky: (žádné).

### Otázka (Front)

Co dělá γ||h−f(x)||²?

### Odpověď (Back)

Učí parametric encoder predikovat optimized sparse code.

## Poznámka Anki 1790001406962

Karty Anki: 1790001406962
GUID: PPC:V3^mW5; štítky: (žádné).

### Otázka (Front)

Jak probíhá PSD training?

### Odpověď (Back)

Alternuje se optimization h a model parameters; encoder poskytuje dobrou initialization latent inference.

## Poznámka Anki 1790001406963

Karty Anki: 1790001406963
GUID: H4t_W$3KX); štítky: (žádné).

### Otázka (Front)

Jaký benefit má PSD při deploymentu?

### Odpověď (Back)

Code lze získat rychlým forward passem f(x) místo iterative sparse-coding optimization.

## Poznámka Anki 1790001406964

Karty Anki: 1790001406964
GUID: nPd!h_OCz[; štítky: (žádné).

### Otázka (Front)

Jaký širší princip PSD ilustruje?

### Odpověď (Back)

Learned approximate inference může amortizovat computational cost náročného inference algorithmu.

## Poznámka Anki 1790001406965

Karty Anki: 1790001406965
GUID: L>zwifDC,@; štítky: (žádné).

### Otázka (Front)

Proč mohou deep autoencoders reprezentovat některé mappings efektivněji než shallow?

### Odpověď (Back)

Depth umožňuje compositional representations s nižší potřebnou width/computation pro některé function classes.

## Poznámka Anki 1790001406966

Karty Anki: 1790001406966
GUID: e,>b2WSEyR; štítky: (žádné).

### Otázka (Front)

Co je greedy layer-wise pretraining deep autoencoderu?

### Odpověď (Back)

Postupné training shallow encoder-decoder modules před joint fine-tuning celé hluboké architecture.

## Poznámka Anki 1790001406967

Karty Anki: 1790001406967
GUID: k,p[HAyHDb; štítky: (žádné).

### Otázka (Front)

Jaký historický benefit měly deep autoencoders pro dimensionality reduction?

### Odpověď (Back)

Dokázaly naučit nonlinear low-dimensional codes s lepší reconstruction a někdy lépe oddělenými semantic clusters než PCA.

## Poznámka Anki 1790001406968

Karty Anki: 1790001406968
GUID: cXN?}$vaIX; štítky: (žádné).

### Otázka (Front)

Jak lze binary low-dimensional autoencoder code použít pro information retrieval?

### Odpověď (Back)

Jako hash key: database examples se indexují podle compact binary code a podobné examples lze rychle lookupovat.

## Poznámka Anki 1790001406969

Karty Anki: 1790001406969
GUID: uuiY)OyDhF; štítky: (žádné).

### Otázka (Front)

Proč je dimensionality reduction computationally užitečná?

### Odpověď (Back)

Downstream algorithms pracují s kratšími vectors, takže spotřebují méně memory a computation.

## Poznámka Anki 1790001406970

Karty Anki: 1790001406970
GUID: DA`2Ofs.*6; štítky: (žádné).

### Otázka (Front)

Proč může learned low-dimensional space zlepšit statistical generalization?

### Odpověď (Back)

Semantic neighbors mohou být blíže než v raw space a local/statistical sharing pak funguje lépe.

## Poznámka Anki 1790001406971

Karty Anki: 1790001406971
GUID: KaD=UISE:O; štítky: (žádné).

### Otázka (Front)

Jaký rozdíl je mezi autoencoderem a generative modellem?

### Odpověď (Back)

Ordinary autoencoder nemusí definovat normalized p(x); generative model explicitně nebo implicitně definuje sampling/data distribution.

## Poznámka Anki 1790001406972

Karty Anki: 1790001406972
GUID: Knctf]Y3`{; štítky: (žádné).

### Otázka (Front)

Proč může autoencoder přesto obsahovat probabilistic information?

### Odpověď (Back)

Jeho reconstruction field a derivatives mohou zachycovat geometry a score data distribution.

## Poznámka Anki 1790001406973

Karty Anki: 1790001406973
GUID: g9SqYA)e&+; štítky: (žádné).

### Otázka (Front)

Jaký vztah má sparse coding z kapitoly 13 k autoencoderům?

### Odpověď (Back)

Oba rekonstruují input z latent code; sparse coding inferuje code optimization, autoencoder jej typicky získá parametric forward mappingem.

## Poznámka Anki 1790001406974

Karty Anki: 1790001406974
GUID: cg]_J@JxFO; štítky: (žádné).

### Otázka (Front)

Jaký meta-princip shrnuje autoencoders?

### Odpověď (Back)

Reconstruction se stává representation learningem teprve tehdy, když omezení nebo regularization donutí model zachytit strukturu dat místo identity mappingu.

## Poznámka Anki 1790001406975

Karty Anki: 1790001406975
GUID: G#3j]04P?l; štítky: (žádné).

### Otázka (Front)

Proč representation může změnit obtížnost stejného problému?

### Odpověď (Back)

Vhodné souřadnice mohou složitý mapping převést na jednoduchý, například linearly separable problem.

## Poznámka Anki 1790001406976

Karty Anki: 1790001406976
GUID: nBn<{:@Km(; štítky: (žádné).

### Otázka (Front)

Je nejlepší representation univerzální pro všechny tasks?

### Odpověď (Back)

Ne; usefulness závisí na tom, jaké properties potřebuje downstream task.

## Poznámka Anki 1790001406977

Karty Anki: 1790001406977
GUID: y/~>}o)rQ.; štítky: (žádné).

### Otázka (Front)

Jak supervised neural network provádí representation learning?

### Odpověď (Back)

Hidden layers se společně s outputem učí features, které snižují supervised loss.

## Poznámka Anki 1790001406978

Karty Anki: 1790001406978
GUID: gG,V#5XqT3; štítky: (žádné).

### Otázka (Front)

Jak unsupervised representation learning může být užitečný bez labels?

### Odpověď (Back)

Může odhalit structure p(x), latent factors nebo geometry, které jsou sdílené s pozdějšími supervised tasks.

## Poznámka Anki 1790001406979

Karty Anki: 1790001406979
GUID: oZ}}i|!e(u; štítky: (žádné).

### Otázka (Front)

Co je greedy layer-wise unsupervised pretraining?

### Odpověď (Back)

Postupné unsupervised učení jedné layer po druhé, poté často joint supervised nebo unsupervised fine-tuning.

## Poznámka Anki 1790001406980

Karty Anki: 1790001406980
GUID: H%4&r*sO3m; štítky: (žádné).

### Otázka (Front)

Proč se pretraining nazývá greedy?

### Odpověď (Back)

Každá layer se učí lokálně před znalostí finálního joint optimum.

## Poznámka Anki 1790001406981

Karty Anki: 1790001406981
GUID: yxEizP%^Fu; štítky: (žádné).

### Otázka (Front)

Jaké models lze použít pro layer-wise pretraining?

### Odpověď (Back)

Například RBMs, autoencoders nebo sparse-coding-like modules.

## Poznámka Anki 1790001406982

Karty Anki: 1790001406982
GUID: F0E,tfW[Q|; štítky: (žádné).

### Otázka (Front)

Jak pretraining může fungovat jako regularizer?

### Odpověď (Back)

Initialization omezuje region function space, do kterého subsequent supervised optimization prakticky dospěje.

## Poznámka Anki 1790001406983

Karty Anki: 1790001406983
GUID: Je=A(-kK:;; štítky: (žádné).

### Otázka (Front)

Jak pretraining může fungovat jako optimization aid?

### Odpověď (Back)

Může parameters umístit do regionu s nižším training objective, který random initialization obtížně dosahuje.

## Poznámka Anki 1790001406984

Karty Anki: 1790001406984
GUID: QsV!xA@`Bt; štítky: (žádné).

### Otázka (Front)

Proč zlepšení training error po pretrainingu dokládá optimization effect?

### Odpověď (Back)

Regularization sama by typicky nevyžadovala lepší fit training data; nižší training error ukazuje, že pretraining pomohl nalézt lepší optimum.

## Poznámka Anki 1790001406985

Karty Anki: 1790001406985
GUID: g1!nHk$^ve; štítky: (žádné).

### Otázka (Front)

Kdy unsupervised pretraining pravděpodobně pomáhá nejvíce?

### Odpověď (Back)

Při malém labeled datasetu, velkém unlabeled corpus a raw representation slabé pro target task.

## Poznámka Anki 1790001406986

Karty Anki: 1790001406986
GUID: N,i(f>7%br; štítky: (žádné).

### Otázka (Front)

Proč bylo pretraining historicky silné v NLP?

### Odpověď (Back)

One-hot word representations jsou chudé a současně je dostupné velmi mnoho unlabeled textu.

## Poznámka Anki 1790001406987

Karty Anki: 1790001406987
GUID: pl|pB27vw3; štítky: (žádné).

### Otázka (Front)

Proč moderní ReLU/dropout/batch-norm training snížil potřebu klasického layer-wise pretrainingu?

### Odpověď (Back)

Výrazně zlepšil přímou supervised optimization a regularization deep networks.

## Poznámka Anki 1790001406988

Karty Anki: 1790001406988
GUID: b[yOU5Y0fy; štítky: (žádné).

### Otázka (Front)

Co je transfer learning?

### Odpověď (Back)

Použití knowledge získané v source settingu P1 ke zlepšení learningu v target settingu P2.

## Poznámka Anki 1790001406989

Karty Anki: 1790001406989
GUID: j&`5lX!O&}; štítky: (žádné).

### Otázka (Front)

Jaký assumption umožňuje transfer learning?

### Odpověď (Back)

Source a target tasks/domains sdílejí relevantní factors nebo reusable representations.

## Poznámka Anki 1790001406990

Karty Anki: 1790001406990
GUID: rf9J((FvZ?; štítky: (žádné).

### Otázka (Front)

Co je domain adaptation?

### Odpověď (Back)

Transfer setting, kde task zůstává stejný, ale input distribution se mezi source a target domain změní.

## Poznámka Anki 1790001406991

Karty Anki: 1790001406991
GUID: uLWpuQ?+l^; štítky: (žádné).

### Otázka (Front)

Jak se domain adaptation liší od obecného transfer learningu?

### Odpověď (Back)

Domain adaptation zachovává target function/task v principu stejný; transfer learning může měnit i task a labels.

## Poznámka Anki 1790001406992

Karty Anki: 1790001406992
GUID: ytsG*xJ*uc; štítky: (žádné).

### Otázka (Front)

Co je concept drift?

### Odpověď (Back)

Změna data distribution v čase, kterou lze chápat jako průběžnou domain adaptation.

## Poznámka Anki 1790001406993

Karty Anki: 1790001406993
GUID: lLEB{m<B,i; štítky: (žádné).

### Otázka (Front)

Jak multi-task learning souvisí s transfer learningem?

### Odpověď (Back)

Oba sdílejí representations mezi tasks; multi-task learning je trénuje společně, transfer může probíhat sekvenčně.

## Poznámka Anki 1790001406994

Karty Anki: 1790001406994
GUID: r]U(o09m=<; štítky: (žádné).

### Otázka (Front)

Co je one-shot learning?

### Odpověď (Back)

Learning nové class/task z jediného labeled target example díky předchozí learned representation nebo knowledge.

## Poznámka Anki 1790001406995

Karty Anki: 1790001406995
GUID: q~.AGt:k4<; štítky: (žádné).

### Otázka (Front)

Jak dobrá representation umožňuje one-shot classification?

### Odpověď (Back)

Jeden example může jen pojmenovat již existující cluster nebo combination known attributes.

## Poznámka Anki 1790001406996

Karty Anki: 1790001406996
GUID: F@rpV*6lf^; štítky: (žádné).

### Otázka (Front)

Co je zero-shot learning?

### Odpověď (Back)

Prediction nové class/task bez labeled target examples díky structured representation target concepts.

## Poznámka Anki 1790001406997

Karty Anki: 1790001406997
GUID: BI/xZl^B!L; štítky: (žádné).

### Otázka (Front)

Proč one-hot class codes neumožňují smysluplný zero-shot transfer?

### Odpověď (Back)

Neobsahují similarity ani attributes vztahující unseen class ke známým classes.

## Poznámka Anki 1790001406998

Karty Anki: 1790001406998
GUID: K{%Sstna.u; štítky: (žádné).

### Otázka (Front)

Jak distributed semantic code umožňuje zero-shot learning?

### Odpověď (Back)

Unseen concept lze popsat kombinací attributes nebo embeddingem, jehož vztahy ke známým concepts jsou již naučeny.

## Poznámka Anki 1790001406999

Karty Anki: 1790001406999
GUID: CHY&9|~GcJ; štítky: (žádné).

### Otázka (Front)

Jak lze zero-shot learning realizovat mezi dvěma modalities?

### Odpověď (Back)

Naučit representation každé modality a mapping/alignment mezi jejich representation spaces z paired examples.

## Poznámka Anki 1790001407000

Karty Anki: 1790001407000
GUID: vA8s)5NLrC; štítky: (žádné).

### Otázka (Front)

Co je disentangling factors of variation?

### Odpověď (Back)

Representation odděluje různé underlying explanatory factors do různých features nebo directions.

## Poznámka Anki 1790001407001

Karty Anki: 1790001407001
GUID: AOryanw!W?; štítky: (žádné).

### Otázka (Front)

Proč je disentangled representation useful?

### Odpověď (Back)

Task může využít relevantní factor bez nutnosti znovu modelovat všechny ostatní nuisance variations.

## Poznámka Anki 1790001407002

Karty Anki: 1790001407002
GUID: QS@x1^A^V9; štítky: (žádné).

### Otázka (Front)

Zaručuje unsupervised density modeling automaticky disentanglement?

### Odpověď (Back)

Ne; stejná observed distribution může mít mnoho alternativních latent representations a jsou potřeba inductive clues.

## Poznámka Anki 1790001407003

Karty Anki: 1790001407003
GUID: HoPn`KXty@; štítky: (žádné).

### Otázka (Front)

Kdy může p(x) pomoci učit p(y|x)?

### Odpověď (Back)

Když y souvisí se salient underlying factors, které také významně strukturují p(x).

## Poznámka Anki 1790001407004

Karty Anki: 1790001407004
GUID: q}Ek*ESb![; štítky: (žádné).

### Otázka (Front)

Kdy unlabeled p(x) nemusí pomoci supervised y?

### Odpověď (Back)

Když target y nesouvisí s dominantní strukturou input distribution.

## Poznámka Anki 1790001407005

Karty Anki: 1790001407005
GUID: x1x*$-|G,V; štítky: (žádné).

### Otázka (Front)

Jak mixture-cluster example ilustruje semi-supervised learning?

### Odpověď (Back)

Unlabeled data odhalí dobře oddělené clusters a několik labels pak pouze přiřadí class names těmto clusters.

## Poznámka Anki 1790001407006

Karty Anki: 1790001407006
GUID: l8+,xz$.=l; štítky: (žádné).

### Otázka (Front)

Co je causal-factor view representation learningu?

### Odpověď (Back)

Latent h jsou chápány jako underlying causes generující observed x.

## Poznámka Anki 1790001407007

Karty Anki: 1790001407007
GUID: BKj*iAQ1Q;; štítky: (žádné).

### Otázka (Front)

Proč causal representations mohou být robustní vůči některým distribution shifts?

### Odpověď (Back)

Causal mechanism p(x|h) může zůstat invariantní, i když prevalence causes p(h) se změní.

## Poznámka Anki 1790001407008

Karty Anki: 1790001407008
GUID: c2&-FDIu.e; štítky: (žádné).

### Otázka (Front)

Proč není možné jednoduše reprezentovat všechny factors světa?

### Odpověď (Back)

Je jich obrovské množství a model musí rozhodnout, které jsou salient pro expected tasks.

## Poznámka Anki 1790001407009

Karty Anki: 1790001407009
GUID: ym8pkAWPHA; štítky: (žádné).

### Otázka (Front)

Jak supervised signal pomáhá určovat salience?

### Odpověď (Back)

Přímo ukazuje, které variations jsou relevantní pro target.

## Poznámka Anki 1790001407010

Karty Anki: 1790001407010
GUID: g?-)(y*nYv; štítky: (žádné).

### Otázka (Front)

Jak reconstruction loss určuje salience v autoencoderu?

### Odpověď (Back)

Factors způsobující velké reconstruction penalty dostávají větší learning pressure než numericky malé, i když mohou být semantically důležité.

## Poznámka Anki 1790001407011

Karty Anki: 1790001407011
GUID: FQO-]N+SI@; štítky: (žádné).

### Otázka (Front)

Proč pixel MSE může ignorovat malý, ale důležitý object?

### Odpověď (Back)

Jeho několik pixelů přispívá málo k celkovému squared error ve srovnání s velkými background structures.

## Poznámka Anki 1790001407012

Karty Anki: 1790001407012
GUID: db0&0sF?HB; štítky: (žádné).

### Otázka (Front)

Jak adversarial/perceptual-like criterion může změnit salience?

### Odpověď (Back)

Může penalizovat nerealistickou semantic structure i tehdy, když pixel-wise error je malý.

## Poznámka Anki 1790001407013

Karty Anki: 1790001407013
GUID: yHD%XL%,je; štítky: (žádné).

### Otázka (Front)

Kolik configurations může teoreticky reprezentovat n binary distributed features?

### Odpověď (Back)

2^n.

## Poznámka Anki 1790001407014

Karty Anki: 1790001407014
GUID: f)>OjX,!@Y; štítky: (žádné).

### Otázka (Front)

Kolik configurations reprezentuje n-dimensional one-hot code?

### Odpověď (Back)

Pouze n.

## Poznámka Anki 1790001407015

Karty Anki: 1790001407015
GUID: rEm`}fV.j|; štítky: (žádné).

### Otázka (Front)

Proč distributed representation podporuje combinatorial generalization?

### Odpověď (Back)

Nový concept může být unseen kombinací již známých feature values.

## Poznámka Anki 1790001407016

Karty Anki: 1790001407016
GUID: HRox~?-S9K; štítky: (žádné).

### Otázka (Front)

Jak one-hot representation omezuje semantic similarity?

### Odpověď (Back)

Různé symbols jsou navzájem equally distant a nesdílejí explicitní attributes.

## Poznámka Anki 1790001407017

Karty Anki: 1790001407017
GUID: B?Nf)g/8Cz; štítky: (žádné).

### Otázka (Front)

Jak embeddings vytvářejí similarity?

### Odpověď (Back)

Sdílené feature dimensions umístí concepts s podobnými properties blízko v vector space.

