# Goodfellow – Blok 14 – karty 1301–1400

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001407218

Karty Anki: 1790001407218
GUID: FiiuEW~n{$; štítky: (žádné).

### Otázka (Front)

Jaký property musí mít noise distribution NCE?

### Odpověď (Back)

Musí být snadno sampleovatelná a evaluovatelná a mít dostatečný overlap s data distribution.

## Poznámka Anki 1790001407219

Karty Anki: 1790001407219
GUID: u&D~MC:>;|; štítky: (žádné).

### Otázka (Front)

Co se stane, když noise je od dat příliš snadno odlišitelný?

### Odpověď (Back)

Classifier task je triviální a poskytuje málo signalu pro jemné modelování data density.

## Poznámka Anki 1790001407220

Karty Anki: 1790001407220
GUID: mbJrR9J<wg; štítky: (žádné).

### Otázka (Front)

Co je self-contrastive estimation?

### Odpověď (Back)

Varianta NCE používající current model jako noise distribution pro daný update.

## Poznámka Anki 1790001407221

Karty Anki: 1790001407221
GUID: L)MDcwd,;U; štítky: (žádné).

### Otázka (Front)

Jaký gradient má self-contrastive estimation v expectation?

### Odpověď (Back)

Stejný jako maximum-likelihood gradient.

## Poznámka Anki 1790001407222

Karty Anki: 1790001407222
GUID: t^R*]xO-46; štítky: (žádné).

### Otázka (Front)

Jak self-contrastive view interpretuje MLE?

### Odpověď (Back)

Model se učí rozlišovat skutečná data od samples svých vlastních současných beliefs.

## Poznámka Anki 1790001407223

Karty Anki: 1790001407223
GUID: f:hH|)7<O8; štítky: (žádné).

### Otázka (Front)

Proč je i po partition-function-free trainingu někdy nutné Z odhadnout?

### Odpověď (Back)

Pro normalized likelihood evaluation, model comparison a monitoring.

## Poznámka Anki 1790001407224

Karty Anki: 1790001407224
GUID: Lo>0].ii}-; štítky: (žádné).

### Otázka (Front)

Jak simple importance sampling odhadne ratio Z1/Z0?

### Odpověď (Back)

Sample x~p0 a průměruje p̃1(x)/p̃0(x), pokud Z0 je známé.

## Poznámka Anki 1790001407225

Karty Anki: 1790001407225
GUID: I-F):w,*:F; štítky: (žádné).

### Otázka (Front)

Kdy simple importance estimate Z funguje dobře?

### Odpověď (Back)

Když p0 a p1 mají silný overlap a importance weights nejsou extrémně variabilní.

## Poznámka Anki 1790001407226

Karty Anki: 1790001407226
GUID: pjZ|zL+=oy; štítky: (žádné).

### Otázka (Front)

Proč simple importance sampling Z selhává ve high-dimensional multimodal case?

### Odpověď (Back)

Tractable p0 obvykle nepokrývá všechny modes p1, takže estimate dominují extrémně vzácné samples.

## Poznámka Anki 1790001407227

Karty Anki: 1790001407227
GUID: PrQmKSJJ_.; štítky: (žádné).

### Otázka (Front)

Co je annealed importance sampling (AIS)?

### Odpověď (Back)

Metoda propojující tractable p0 a target p1 sérií intermediate distributions a násobící odhady jejich successive normalization ratios.

## Poznámka Anki 1790001407228

Karty Anki: 1790001407228
GUID: O>_AUE_-;+; štítky: (žádné).

### Otázka (Front)

Proč AIS používá intermediate distributions?

### Odpověď (Back)

Každý malý distribution shift má lepší overlap než jeden přímý skok p0→p1.

## Poznámka Anki 1790001407229

Karty Anki: 1790001407229
GUID: yCnL3uwLiv; štítky: (žádné).

### Otázka (Front)

Jaká common AIS interpolation je geometric path?

### Odpověď (Back)

p_η(x)∝p1(x)^η p0(x)^{1−η}, kde η postupuje od 0 k 1.

## Poznámka Anki 1790001407230

Karty Anki: 1790001407230
GUID: AO-Drh]WWm; štítky: (žádné).

### Otázka (Front)

Jakou roli mají MCMC transitions v AIS?

### Odpověď (Back)

Přesouvají trajectory tak, aby successive states odpovídaly intermediate distributions a každý transition zachovával příslušnou p_η invariantní.

## Poznámka Anki 1790001407231

Karty Anki: 1790001407231
GUID: pLqT:@0V[9; štítky: (žádné).

### Otázka (Front)

Jak vzniká AIS weight?

### Odpověď (Back)

Jako product ratios unnormalized intermediate densities podél trajectory.

## Poznámka Anki 1790001407232

Karty Anki: 1790001407232
GUID: pgyMr~t-KJ; štítky: (žádné).

### Otázka (Front)

Proč se AIS weights počítají v log-space?

### Odpověď (Back)

Product mnoha ratios může numericky underflowovat/overflowovat; log transformuje product na stabilnější sum.

## Poznámka Anki 1790001407233

Karty Anki: 1790001407233
GUID: r7`{m(,WD+; štítky: (žádné).

### Otázka (Front)

K čemu se AIS často používá u RBMs?

### Odpověď (Back)

K approximate evaluation partition function a test log-likelihood po trainingu.

## Poznámka Anki 1790001407234

Karty Anki: 1790001407234
GUID: I#|xdj?9z^; štítky: (žádné).

### Otázka (Front)

Co je bridge sampling?

### Odpověď (Back)

Odhad ratio normalizers dvou distributions pomocí intermediate bridge distribution s dobrým overlapem s oběma.

## Poznámka Anki 1790001407235

Karty Anki: 1790001407235
GUID: G`0Unk@L41; štítky: (žádné).

### Otázka (Front)

Jak se bridge sampling liší od AIS?

### Odpověď (Back)

Bridge sampling typicky používá jednu nebo několik bridge relationships; AIS používá explicitní dlouhou annealing path.

## Poznámka Anki 1790001407236

Karty Anki: 1790001407236
GUID: C+p1sAGbh8; štítky: (žádné).

### Otázka (Front)

Co je linked importance sampling?

### Odpověď (Back)

Metoda kombinující sequence intermediate distributions s bridge-like estimates mezi sousedními stages.

## Poznámka Anki 1790001407237

Karty Anki: 1790001407237
GUID: GZU#?|OX26; štítky: (žádné).

### Otázka (Front)

Jaké tři strategie proti partition function shrnuje kapitola?

### Odpověď (Back)

Approximovat negative-phase gradient samplingem; použít alternative objective, kde Z algebraicky/derivačně zmizí; nebo Z explicitně odhadnout.

## Poznámka Anki 1790001407238

Karty Anki: 1790001407238
GUID: c/r{|K~>|{; štítky: (žádné).

### Otázka (Front)

Co je approximate inference?

### Odpověď (Back)

Výpočetně tractable approximation intractable posterior distribution nebo jejích expectations.

## Poznámka Anki 1790001407239

Karty Anki: 1790001407239
GUID: uG?EbN(%%=; štítky: (žádné).

### Otázka (Front)

Proč posterior latent variables bývá intractable?

### Odpověď (Back)

Conditioning na observations může vytvořit silné dependencies a marginalization přes latent configurations může růst exponenciálně.

## Poznámka Anki 1790001407240

Karty Anki: 1790001407240
GUID: Rf%y[5V`+h; štítky: (žádné).

### Otázka (Front)

Jak explaining away vytváří posterior dependencies?

### Odpověď (Back)

Latent co-causes shared observed effectu se po jeho pozorování stanou dependent.

## Poznámka Anki 1790001407241

Karty Anki: 1790001407241
GUID: G`?c=~()VC; štítky: (žádné).

### Otázka (Front)

Co je evidence lower bound (ELBO)?

### Odpověď (Back)

L(v,θ,q)=log p(v;θ)−D_KL(q(h|v)||p(h|v;θ)), dolní mez log evidence.

## Poznámka Anki 1790001407242

Karty Anki: 1790001407242
GUID: qth<6,l+6e; štítky: (žádné).

### Otázka (Front)

Proč je ELBO skutečně lower bound?

### Odpověď (Back)

KL divergence je vždy nezáporná.

## Poznámka Anki 1790001407243

Karty Anki: 1790001407243
GUID: mro,!B&#;]; štítky: (žádné).

### Otázka (Front)

Kdy je ELBO tight?

### Odpověď (Back)

Když q(h|v)=p(h|v;θ) almost everywhere.

## Poznámka Anki 1790001407244

Karty Anki: 1790001407244
GUID: D:#01R@>S^; štítky: (žádné).

### Otázka (Front)

Jaká expectation forma ELBO se běžně používá?

### Odpověď (Back)

L=E_q[log p(v,h;θ)]+H(q).

## Poznámka Anki 1790001407245

Karty Anki: 1790001407245
GUID: A6?_r~dta9; štítky: (žádné).

### Otázka (Front)

Jak exact inference souvisí s ELBO optimization?

### Odpověď (Back)

Maximalizace ELBO přes unrestricted q dosáhne true posterioru a log p(v).

## Poznámka Anki 1790001407246

Karty Anki: 1790001407246
GUID: qZ?CNdB0&6; štítky: (žádné).

### Otázka (Front)

Jak approximate inference vznikne omezením q family?

### Odpověď (Back)

True posterior nemusí být representable, takže optimum q zůstane s nonzero KL gap.

## Poznámka Anki 1790001407247

Karty Anki: 1790001407247
GUID: qMEK:tL?`p; štítky: (žádné).

### Otázka (Front)

Jaké dva zdroje inference error lze rozlišit?

### Odpověď (Back)

Approximation/representation error variational family a optimization error při hledání jejího nejlepšího memberu.

## Poznámka Anki 1790001407248

Karty Anki: 1790001407248
GUID: GI_i}=h5Lr; štítky: (žádné).

### Otázka (Front)

Co je variational inference?

### Odpověď (Back)

Maximalizace ELBO nad computationally tractable family q.

## Poznámka Anki 1790001407249

Karty Anki: 1790001407249
GUID: eT/l$xe8;e; štítky: (žádné).

### Otázka (Front)

Jaký KL směr variational inference používá?

### Odpověď (Back)

D_KL(q||p_posterior).

## Poznámka Anki 1790001407250

Karty Anki: 1790001407250
GUID: D0,/6Bb(:y; štítky: (žádné).

### Otázka (Front)

Proč je tento KL směr convenient?

### Odpověď (Back)

Expectations se počítají pod tractable q místo intractable posterioru.

## Poznámka Anki 1790001407251

Karty Anki: 1790001407251
GUID: oSKu%FigwB; štítky: (žádné).

### Otázka (Front)

Jaký qualitative mode-seeking behavior má D_KL(q||p)?

### Odpověď (Back)

Silně penalizuje q mass v low-p regions, takže restricted q může raději pokrýt jeden posterior mode než průměrovat mezi separated modes.

## Poznámka Anki 1790001407252

Karty Anki: 1790001407252
GUID: Eqt^|f~4h8; štítky: (žádné).

### Otázka (Front)

Co je expectation maximization (EM)?

### Odpověď (Back)

Coordinate-ascent procedure střídající posterior inference E-step a parameter optimization M-step.

## Poznámka Anki 1790001407253

Karty Anki: 1790001407253
GUID: v0D:X`:z]j; štítky: (žádné).

### Otázka (Front)

Co dělá exact E-step?

### Odpověď (Back)

Nastaví q(h)=p(h|v;θ_current), čímž ELBO ztěsní na log likelihood.

## Poznámka Anki 1790001407254

Karty Anki: 1790001407254
GUID: dSAHU;qJwJ; štítky: (žádné).

### Otázka (Front)

Co dělá M-step?

### Odpověď (Back)

Maximalizuje ELBO vzhledem k θ při fixním q.

## Poznámka Anki 1790001407255

Karty Anki: 1790001407255
GUID: f>6H3*C4$j; štítky: (žádné).

### Otázka (Front)

Proč se gap během M-stepu může otevřít?

### Odpověď (Back)

True posterior se s novými θ mění, zatímco q odpovídá starým parameters.

## Poznámka Anki 1790001407256

Karty Anki: 1790001407256
GUID: mp*ZLP:CGs; štítky: (žádné).

### Otázka (Front)

Jak lze jeden gradient step θ chápat v EM frameworku?

### Odpověď (Back)

Jako partial M-step místo exact maximization.

## Poznámka Anki 1790001407257

Karty Anki: 1790001407257
GUID: L]GsyX2XJq; štítky: (žádné).

### Otázka (Front)

Co je MAP inference?

### Odpověď (Back)

Hledání jediného latent state h*=argmax_h p(h|v).

## Poznámka Anki 1790001407258

Karty Anki: 1790001407258
GUID: mYV@~hnzzI; štítky: (žádné).

### Otázka (Front)

Jak se MAP liší od full posterior inference?

### Odpověď (Back)

Ignoruje uncertainty a ostatní posterior states.

## Poznámka Anki 1790001407259

Karty Anki: 1790001407259
GUID: F+#0_v(m(o; štítky: (žádné).

### Otázka (Front)

Jak lze MAP variationally interpretovat?

### Odpověď (Back)

Jako extrémně restricted q soustředěnou v jediném pointu, i když continuous Dirac má formální entropy complications.

## Poznámka Anki 1790001407260

Karty Anki: 1790001407260
GUID: iy0Q}bDs86; štítky: (žádné).

### Otázka (Front)

Proč sparse coding používá MAP inference?

### Odpověď (Back)

Full posterior latent causes je intractable, ale mode lze najít convex nebo tractable optimization pro fixed dictionary.

## Poznámka Anki 1790001407261

Karty Anki: 1790001407261
GUID: gptysH4)ni; štítky: (žádné).

### Otázka (Front)

Jaký MAP sparse-coding objective vzniká s Laplace prior?

### Odpověď (Back)

Reconstruction squared error plus L¹ sparsity penalty.

## Poznámka Anki 1790001407262

Karty Anki: 1790001407262
GUID: KBpf$XR,ZD; štítky: (žádné).

### Otázka (Front)

Proč se sparse coding střídavě optimalizuje v h a W?

### Odpověď (Back)

Joint problem není convex, ale každý block subproblem může být výrazně jednodušší.

## Poznámka Anki 1790001407263

Karty Anki: 1790001407263
GUID: d|JK9?1E5w; štítky: (žádné).

### Otázka (Front)

Co je mean-field approximation?

### Odpověď (Back)

Variational family factorující q(h|v)=∏_i q(h_i|v).

## Poznámka Anki 1790001407264

Karty Anki: 1790001407264
GUID: IX&Ej)]7UW; štítky: (žádné).

### Otázka (Front)

Jaký benefit má mean field?

### Odpověď (Back)

Dramaticky zjednodušuje storage, expectations a updates.

## Poznámka Anki 1790001407265

Karty Anki: 1790001407265
GUID: pV{iL7:VZK; štítky: (žádné).

### Otázka (Front)

Jaký cost má mean field?

### Odpověď (Back)

Nemůže explicitně reprezentovat posterior correlations a některé multimodal dependencies.

## Poznámka Anki 1790001407266

Karty Anki: 1790001407266
GUID: gxSYw,=Q(d; štítky: (žádné).

### Otázka (Front)

Co je structured variational inference?

### Odpověď (Back)

Variational family q zachovávající vybrané dependencies místo plné factorization.

## Poznámka Anki 1790001407267

Karty Anki: 1790001407267
GUID: j,Q|rw&S)K; štítky: (žádné).

### Otázka (Front)

Jaký trade-off má structured q?

### Odpověď (Back)

Tighter approximation za vyšší computational cost.

## Poznámka Anki 1790001407268

Karty Anki: 1790001407268
GUID: Ir{6qN{I,a; štítky: (žádné).

### Otázka (Front)

Jak se mean-field parameters pro binary h_i reprezentují?

### Odpověď (Back)

Bernoulli means ĥ_i=q(h_i=1|v).

## Poznámka Anki 1790001407269

Karty Anki: 1790001407269
GUID: c@r=LhJY#j; štítky: (žádné).

### Otázka (Front)

Co jsou fixed-point mean-field equations?

### Odpověď (Back)

Coordinate-optimal update rules získané nastavením derivative ELBO podle jednoho variational factoru na nulu při fixních ostatních.

## Poznámka Anki 1790001407270

Karty Anki: 1790001407270
GUID: FT2PC)G?Lo; štítky: (žádné).

### Otázka (Front)

Proč se fixed-point updates často používají místo generic gradient descent?

### Odpověď (Back)

Jsou specializované na inference objective a mohou rychleji dosáhnout dobrého q v inner loop.

## Poznámka Anki 1790001407271

Karty Anki: 1790001407271
GUID: d(]:mw^rxQ; štítky: (žádné).

### Otázka (Front)

Jak mean-field sparse coding realizuje explaining-away competition?

### Odpověď (Back)

Activation jednoho latent cause zmenšuje residual a inhibuje redundantní causes prostřednictvím coupling terms.

## Poznámka Anki 1790001407272

Karty Anki: 1790001407272
GUID: pjFsFdR_HR; štítky: (žádné).

### Otázka (Front)

Jak residual interpretation vysvětluje iterative inference?

### Odpověď (Back)

Každá hidden unit reaguje na část inputu, kterou ostatní latent units ještě nevysvětlily.

## Poznámka Anki 1790001407273

Karty Anki: 1790001407273
GUID: x@;L<&o&&!; štítky: (žádné).

### Otázka (Front)

Co je damping variational updates?

### Odpověď (Back)

Nové factor values se posunou jen částečně směrem k coordinate optimum, aby se zlepšila stability synchronous updates.

## Poznámka Anki 1790001407274

Karty Anki: 1790001407274
GUID: e:!oJLm>ZD; štítky: (žádné).

### Otázka (Front)

Co je calculus of variations?

### Odpověď (Back)

Optimization over functions, používaná k odvození optimal functional form continuous q factors.

## Poznámka Anki 1790001407275

Karty Anki: 1790001407275
GUID: f[1VOT6lXH; štítky: (žádné).

### Otázka (Front)

Co je functional derivative?

### Odpověď (Back)

Analog gradientu pro objective, jehož argumentem je celá funkce.

## Poznámka Anki 1790001407276

Karty Anki: 1790001407276
GUID: eRP2v;bJ1T; štítky: (žádné).

### Otázka (Front)

Jaký general continuous mean-field update platí?

### Odpověď (Back)

q_i(h_i)∝exp(E_{q_{−i}}[log p(v,h)]).

## Poznámka Anki 1790001407277

Karty Anki: 1790001407277
GUID: Ca`]s]ZOgq; štítky: (žádné).

### Otázka (Front)

Co tento update říká intuitivně?

### Odpověď (Back)

Optimal factor je exponential očekávaného log joint modelu po averaging ostatních latent variables.

## Poznámka Anki 1790001407278

Karty Anki: 1790001407278
GUID: f86$PrZ@`); štítky: (žádné).

### Otázka (Front)

Proč approximation může ovlivnit learned generative model samotný?

### Odpověď (Back)

Maximalizujeme ELBO, ne exact likelihood, takže θ může preferovat model s posterior structure, kterou zvolená q family snáze aproximuje.

## Poznámka Anki 1790001407279

Karty Anki: 1790001407279
GUID: dOKGs|<!tV; štítky: (žádné).

### Otázka (Front)

Co znamená self-fulfilling prophecy variational inference?

### Odpověď (Back)

Restricted q může během learningu tlačit model k posteriorům, které vypadají podobně jako její vlastní assumptions.

## Poznámka Anki 1790001407280

Karty Anki: 1790001407280
GUID: EZfp[wk3_~; štítky: (žádné).

### Otázka (Front)

Proč tight ELBO u final modelu nedokazuje, že variational training našel nejlepší likelihood model?

### Odpověď (Back)

Bound může být tight pro suboptimal θ, zatímco lepší likelihood θ* má posterior příliš složitý pro q a byl trainingem penalizován.

## Poznámka Anki 1790001407281

Karty Anki: 1790001407281
GUID: DS[yzR*[qM; štítky: (žádné).

### Otázka (Front)

Co je learned approximate inference?

### Odpověď (Back)

Parametric network předpovídá parameters approximate posterioru z observation místo nové iterative optimization pro každý example.

## Poznámka Anki 1790001407282

Karty Anki: 1790001407282
GUID: Ou,1F?.x?5; štítky: (žádné).

### Otázka (Front)

Co znamená amortized inference?

### Odpověď (Back)

Cost learning inference mapping je sdílen přes mnoho examples; každý nový input pak potřebuje levný forward pass.

## Poznámka Anki 1790001407283

Karty Anki: 1790001407283
GUID: w`wJy,ER]/; štítky: (žádné).

### Otázka (Front)

Jaký trade-off má amortized inference?

### Odpověď (Back)

Je rychlá, ale přidává approximation/generalization error inference networku.

## Poznámka Anki 1790001407284

Karty Anki: 1790001407284
GUID: f|.HWDxSZB; štítky: (žádné).

### Otázka (Front)

Co je wake-sleep algorithm?

### Odpověď (Back)

Generative/inference-network training procedure používající samples z generative modelu k učení reverse recognition mappingu.

## Poznámka Anki 1790001407285

Karty Anki: 1790001407285
GUID: ms=FJ+b.FO; štítky: (žádné).

### Otázka (Front)

Co se děje v sleep phase?

### Odpověď (Back)

Generative model vytvoří synthetic (h,v) pairs a recognition network se učí inferovat h z v.

## Poznámka Anki 1790001407286

Karty Anki: 1790001407286
GUID: b3uVYqo|(8; štítky: (žádné).

### Otázka (Front)

Jaká slabina má sleep-phase training?

### Odpověď (Back)

Recognition network se učí na model-generated v, které zejména na začátku nemusí odpovídat real data distribution.

## Poznámka Anki 1790001407287

Karty Anki: 1790001407287
GUID: t<1iSP;Jc<; štítky: (žádné).

### Otázka (Front)

Jak predictive sparse decomposition ilustruje learned inference?

### Odpověď (Back)

Parametric encoder se učí approximovat výsledky pomalejší MAP sparse-coding optimization.

## Poznámka Anki 1790001407288

Karty Anki: 1790001407288
GUID: Dpjz.oSo.4; štítky: (žádné).

### Otázka (Front)

Jak lze iterative inference spojit s recurrent networks?

### Odpověď (Back)

Unrolled optimization steps tvoří recurrent computational graph, jehož update rules mohou být learned nebo differentiated.

## Poznámka Anki 1790001407289

Karty Anki: 1790001407289
GUID: PqXD}-1.uK; štítky: (žádné).

### Otázka (Front)

Jak VAE používá learned inference?

### Odpověď (Back)

Encoder network parametrizuje q(z|x) a je trénována přímo přes differentiable ELBO.

## Poznámka Anki 1790001407290

Karty Anki: 1790001407290
GUID: Qt<ZIrR)R2; štítky: (žádné).

### Otázka (Front)

Proč VAE nepotřebuje posterior target labels?

### Odpověď (Back)

Inference-network parameters dostávají gradient z variational objective společně s generative parameters.

## Poznámka Anki 1790001407291

Karty Anki: 1790001407291
GUID: Oy$r)MRPx&; štítky: (žádné).

### Otázka (Front)

Jaký sjednocující pohled spojuje exact inference, variational inference, MAP a amortized inference?

### Odpověď (Back)

Jde o různé kompromisy mezi representational richness posterior approximation, optimization effort a computation per example.

## Poznámka Anki 1790001407292

Karty Anki: 1790001407292
GUID: u~$jXFYKwf; štítky: (žádné).

### Otázka (Front)

Co je hlavní téma kapitoly 20?

### Odpověď (Back)

Deep generative models: modely učící složité data distributions a latent representations pomocí deep, probabilistic nebo implicit generative mechanisms.

## Poznámka Anki 1790001407293

Karty Anki: 1790001407293
GUID: N=?0C!`F@U; štítky: (žádné).

### Otázka (Front)

Co je Boltzmann machine?

### Odpověď (Back)

Undirected energy-based model s binary nebo jinými random units a energy function definující p(x)∝exp(−E(x)).

## Poznámka Anki 1790001407294

Karty Anki: 1790001407294
GUID: iGVB,4Oc{8; štítky: (žádné).

### Otázka (Front)

Jak hidden units zvyšují expressive power Boltzmann machine?

### Odpověď (Back)

Zprostředkují higher-order dependencies mezi visibles bez explicitních high-order visible factors.

## Poznámka Anki 1790001407295

Karty Anki: 1790001407295
GUID: iLnVlz$[~d; štítky: (žádné).

### Otázka (Front)

Proč maximum-likelihood training Boltzmann machine potřebuje positive a negative phase?

### Odpověď (Back)

Positive phase podporuje configurations kompatibilní s daty, negative phase potlačuje probability modelových states přes gradient partition function.

## Poznámka Anki 1790001407296

Karty Anki: 1790001407296
GUID: g.3w9g[1Cf; štítky: (žádné).

### Otázka (Front)

Co je local Hebbian-like interpretation positive phase?

### Odpověď (Back)

Connections posilují, když jejich endpoint units jsou v data-driven posterioru často aktivní společně.

## Poznámka Anki 1790001407297

Karty Anki: 1790001407297
GUID: QH+t)2nqMM; štítky: (žádné).

### Otázka (Front)

Jaká je energy binary RBM?

### Odpověď (Back)

E(v,h)=−bᵀv−cᵀh−vᵀWh.

## Poznámka Anki 1790001407298

Karty Anki: 1790001407298
GUID: [PX-Qc3/5; štítky: (žádné).

### Otázka (Front)

Jak se hidden activation probability RBM počítá?

### Odpověď (Back)

P(h_j=1|v)=σ(c_j+vᵀW_:,j).

## Poznámka Anki 1790001407299

Karty Anki: 1790001407299
GUID: K3rQ|~yh`!; štítky: (žádné).

### Otázka (Front)

Jak se visible activation probability počítá?

### Odpověď (Back)

P(v_i=1|h)=σ(b_i+W_i,:h).

## Poznámka Anki 1790001407300

Karty Anki: 1790001407300
GUID: Q&+brD.__(; štítky: (žádné).

### Otázka (Front)

Proč je block Gibbs v RBM efektivní?

### Odpověď (Back)

Všechny units stejné layer jsou conditionally independent given protější layer a lze je sampleovat paralelně.

## Poznámka Anki 1790001407301

Karty Anki: 1790001407301
GUID: OdS1N|G0;2; štítky: (žádné).

### Otázka (Front)

Co je deep belief network (DBN)?

### Odpověď (Back)

Hybridní deep generative model s undirected top RBM a directed generative connections v nižších layers.

## Poznámka Anki 1790001407302

Karty Anki: 1790001407302
GUID: jP+_FfbzcE; štítky: (žádné).

### Otázka (Front)

Jak se vzorkuje z DBN?

### Odpověď (Back)

Nejprve se MCMC sampleuje top-level RBM a pak se provede ancestral downward sampling nižšími directed layers.

## Poznámka Anki 1790001407303

Karty Anki: 1790001407303
GUID: B|Pez4gxB&; štítky: (žádné).

### Otázka (Front)

Proč je posterior DBN intractable?

### Odpověď (Back)

Directed latent causes vytvářejí explaining away a top RBM přidává undirected dependency.

## Poznámka Anki 1790001407304

Karty Anki: 1790001407304
GUID: pW+bHxL}5_; štítky: (žádné).

### Otázka (Front)

Co je greedy layer-wise DBN pretraining?

### Odpověď (Back)

Každá další RBM modeluje hidden representations vytvořené předchozí pretrained layer.

## Poznámka Anki 1790001407305

Karty Anki: 1790001407305
GUID: i:Yv`ZM:nR; štítky: (žádné).

### Otázka (Front)

Jaký historický význam mají DBNs?

### Odpověď (Back)

Ukázaly kolem roku 2006, že hluboké fully connected networks lze prakticky trénovat, a pomohly obnovit zájem o deep learning.

## Poznámka Anki 1790001407306

Karty Anki: 1790001407306
GUID: Fo;g*XUHfp; štítky: (žádné).

### Otázka (Front)

Co je deep Boltzmann machine (DBM)?

### Odpověď (Back)

Entirely undirected generative model s visible layer a více hidden layers, typicky bez intra-layer connections.

## Poznámka Anki 1790001407307

Karty Anki: 1790001407307
GUID: O.vSZ+V+$4; štítky: (žádné).

### Otázka (Front)

Jak se DBM liší od DBN?

### Odpověď (Back)

DBM má undirected interactions mezi všemi sousedními layers; DBN je undirected pouze nahoře a níže directed.

## Poznámka Anki 1790001407308

Karty Anki: 1790001407308
GUID: P&X=~G[D42; štítky: (žádné).

### Otázka (Front)

Jak se DBM liší od RBM?

### Odpověď (Back)

Má více než jednu hidden layer a posterior přes layers je obecně intractable.

## Poznámka Anki 1790001407309

Karty Anki: 1790001407309
GUID: jyBZ.]#6d=; štítky: (žádné).

### Otázka (Front)

Jaký structural property DBM umožňuje efficient Gibbs transitions?

### Odpověď (Back)

Layers lze rozdělit na odd/even blocks; units v jednom blocku jsou conditionally independent given druhý block.

## Poznámka Anki 1790001407310

Karty Anki: 1790001407310
GUID: Ra#[!J!L0B; štítky: (žádné).

### Otázka (Front)

Jak se posterior DBM typicky aproximuje?

### Odpověď (Back)

Factorial mean-field variational inference s iterative bottom-up a top-down updates.

## Poznámka Anki 1790001407311

Karty Anki: 1790001407311
GUID: EP,co6ZERr; štítky: (žádné).

### Otázka (Front)

Proč top-down signal v DBM inference matters?

### Odpověď (Back)

Higher-level explanation může změnit interpretation lower-level features a vice versa.

## Poznámka Anki 1790001407312

Karty Anki: 1790001407312
GUID: HgyaR;_/QF; štítky: (žádné).

### Otázka (Front)

Jak se trénuje negative phase DBM?

### Odpověď (Back)

Typicky persistent MCMC/SML.

## Poznámka Anki 1790001407313

Karty Anki: 1790001407313
GUID: h%]b@PLP2%; štítky: (žádné).

### Otázka (Front)

Jak se trénuje positive phase DBM?

### Odpověď (Back)

Approximate posterior expectations z mean-field inference.

## Poznámka Anki 1790001407314

Karty Anki: 1790001407314
GUID: bKm^!cYx7!; štítky: (žádné).

### Otázka (Front)

Proč greedy pretraining historically pomáhal DBM?

### Odpověď (Back)

Random joint training mohl uváznout v poor solution; layer-wise RBM initialization vytvořila užitečné feature structure.

## Poznámka Anki 1790001407315

Karty Anki: 1790001407315
GUID: wP|s}WTtA6; štítky: (žádné).

### Otázka (Front)

Co je centering trick v Boltzmann machines?

### Odpověď (Back)

Reparametrizace activations kolem learned/fixed offsets, která zlepšuje conditioning optimization bez změny model family.

## Poznámka Anki 1790001407316

Karty Anki: 1790001407316
GUID: rI8;_dTL)%; štítky: (žádné).

### Otázka (Front)

Co je multi-prediction DBM (MP-DBM)?

### Odpověď (Back)

DBM trained by unrolling approximate inference a backpropagating prediction loss pro random subsets missing variables.

## Poznámka Anki 1790001407317

Karty Anki: 1790001407317
GUID: i-=7$H83rs; štítky: (žádné).

### Otázka (Front)

Jak MP-DBM souvisí s generalized pseudolikelihood?

### Odpověď (Back)

Učí model predikovat různé subsets variables conditioned na ostatních, nikoli přímo maximalizovat exact joint likelihood.

