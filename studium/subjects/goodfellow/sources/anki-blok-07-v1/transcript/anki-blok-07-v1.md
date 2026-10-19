# Goodfellow – Blok 07 – karty 601–700

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001406518

Karty Anki: 1790001406518
GUID: K+>eyz%~7^; štítky: (žádné).

### Otázka (Front)

Jaká hlavní slabina AdaGrad?

### Odpověď (Back)

Accumulated squared gradients pouze rostou, takže learning rates mohou předčasně klesnout téměř k nule.

## Poznámka Anki 1790001406519

Karty Anki: 1790001406519
GUID: I_/Qpeh%Ro; štítky: (žádné).

### Otázka (Front)

Co je RMSProp?

### Odpověď (Back)

Adaptive method používající exponentially decayed average squared gradients místo nekonečné kumulace AdaGrad.

## Poznámka Anki 1790001406520

Karty Anki: 1790001406520
GUID: J36Av}8w!3; štítky: (žádné).

### Otázka (Front)

Jaký problém AdaGrad RMSProp řeší?

### Odpověď (Back)

Zabraňuje monotonic decay effective learning rate způsobenému sumou všech historických squared gradients.

## Poznámka Anki 1790001406521

Karty Anki: 1790001406521
GUID: b#UBy0=wkK; štítky: (žádné).

### Otázka (Front)

Co je Adam?

### Odpověď (Back)

Optimizer kombinující exponentially decayed first-moment estimate gradientu a second-moment estimate squared gradientu s bias correction.

## Poznámka Anki 1790001406522

Karty Anki: 1790001406522
GUID: vd1T(WEEAT; štítky: (žádné).

### Otázka (Front)

Co v Adam představuje m?

### Odpověď (Back)

Exponential moving average gradientů, analog momentum.

## Poznámka Anki 1790001406523

Karty Anki: 1790001406523
GUID: n$E_%5@:%8; štítky: (žádné).

### Otázka (Front)

Co v Adam představuje v?

### Odpověď (Back)

Exponential moving average squared gradients, používaný k per-parameter normalization.

## Poznámka Anki 1790001406524

Karty Anki: 1790001406524
GUID: FaOixF$9,u; štítky: (žádné).

### Otázka (Front)

Proč Adam používá bias correction?

### Odpověď (Back)

Moving averages inicializované na nulu jsou v prvních steps biased směrem k nule.

## Poznámka Anki 1790001406525

Karty Anki: 1790001406525
GUID: OL^o>1,um`; štítky: (žádné).

### Otázka (Front)

Jaký typ second-order information používá Newton's method?

### Odpověď (Back)

Full Hessian inverse k rescaling gradientu podle curvature.

## Poznámka Anki 1790001406526

Karty Anki: 1790001406526
GUID: JiXtlZzPn@; štítky: (žádné).

### Otázka (Front)

Proč je exact Newton's method pro velké deep networks nepraktická?

### Odpověď (Back)

Hessian má počet prvků kvadratický v počtu parameters a jeho inversion je extrémně drahá.

## Poznámka Anki 1790001406527

Karty Anki: 1790001406527
GUID: t/`_}&1:[I; štítky: (žádné).

### Otázka (Front)

Co je conjugate gradient (CG)?

### Odpověď (Back)

Iterative algorithm pro řešení linear systems nebo quadratic optimization bez explicitního matrix inversion.

## Poznámka Anki 1790001406528

Karty Anki: 1790001406528
GUID: KkmiFc=GW3; štítky: (žádné).

### Otázka (Front)

Jak lze CG využít v second-order neural optimization?

### Odpověď (Back)

Řeší Hx=g pomocí Hessian-vector products bez explicitního sestavení H.

## Poznámka Anki 1790001406529

Karty Anki: 1790001406529
GUID: w1ypJ1I7=N; štítky: (žádné).

### Otázka (Front)

Co je BFGS?

### Odpověď (Back)

Quasi-Newton method, která iterativně buduje approximation inverse Hessianu z gradient a parameter differences.

## Poznámka Anki 1790001406530

Karty Anki: 1790001406530
GUID: u|<w~6WhTu; štítky: (žádné).

### Otázka (Front)

Co je L-BFGS?

### Odpověď (Back)

Limited-memory BFGS uchovávající pouze několik posledních update pairs místo full dense Hessian approximation.

## Poznámka Anki 1790001406531

Karty Anki: 1790001406531
GUID: EK*4^(k@|v; štítky: (žádné).

### Otázka (Front)

Proč jsou batch/quasi-Newton methods hůře škálovatelné na obrovské datasets než SGD?

### Odpověď (Back)

Typicky potřebují stabilnější full-batch nebo large-batch gradients a více computation per update.

## Poznámka Anki 1790001406532

Karty Anki: 1790001406532
GUID: L(B]AFL((]; štítky: (žádné).

### Otázka (Front)

Co je batch normalization?

### Odpověď (Back)

Reparameterization vrstvy normalizující minibatch activations pomocí sample mean a variance a následně aplikující learned scale γ a shift β.

## Poznámka Anki 1790001406533

Karty Anki: 1790001406533
GUID: AC)+^Qp<B`; štítky: (žádné).

### Otázka (Front)

Jaký původní motivation batch normalization uvádí kniha?

### Odpověď (Back)

Stabilizovat distributions intermediate activations během trainingu a usnadnit optimization.

## Poznámka Anki 1790001406534

Karty Anki: 1790001406534
GUID: ikDc96`^_c; štítky: (žádné).

### Otázka (Front)

Jaké trainable parameters má batch-normalized unit?

### Odpověď (Back)

Scale γ a shift β, které umožňují network znovu zvolit vhodnou mean a variance.

## Poznámka Anki 1790001406535

Karty Anki: 1790001406535
GUID: >8l/z>H@r; štítky: (žádné).

### Otázka (Front)

Proč BN může dovolit větší learning rates?

### Odpověď (Back)

Normalizace omezuje některé scale sensitivities a stabilizuje activations i gradients.

## Poznámka Anki 1790001406536

Karty Anki: 1790001406536
GUID: g/WcAcS<x!; štítky: (žádné).

### Otázka (Front)

Jak BN vytváří stochasticity?

### Odpověď (Back)

Mean a variance se odhadují z random minibatch, takže output jednoho example závisí na ostatních examples v batchi.

## Poznámka Anki 1790001406537

Karty Anki: 1790001406537
GUID: s{c:dXdq3a; štítky: (žádné).

### Otázka (Front)

Jak se BN používá při testu?

### Odpověď (Back)

Místo current minibatch statistics se používají running/population estimates mean a variance.

## Poznámka Anki 1790001406538

Karty Anki: 1790001406538
GUID: mRN0(,P{H|; štítky: (žádné).

### Otázka (Front)

Je batch normalization pouze regularizer?

### Odpověď (Back)

Ne; primárně mění parametrizaci a optimization, i když minibatch noise může mít regularizační efekt.

## Poznámka Anki 1790001406539

Karty Anki: 1790001406539
GUID: bf9cLW+.YA; štítky: (žádné).

### Otázka (Front)

Co je coordinate descent?

### Odpověď (Back)

Optimization aktualizující vždy jednu variable nebo block variables při fixaci ostatních.

## Poznámka Anki 1790001406540

Karty Anki: 1790001406540
GUID: d,50N1^1/p; štítky: (žádné).

### Otázka (Front)

Kdy je coordinate descent vhodný?

### Odpověď (Back)

Když lze jednotlivé coordinates optimalizovat snadno, ale není dobře kompatibilní s dense coupled neural parameters a GPU parallelismem.

## Poznámka Anki 1790001406541

Karty Anki: 1790001406541
GUID: gl.b[%=:tJ; štítky: (žádné).

### Otázka (Front)

Co je Polyak averaging?

### Odpověď (Back)

Průměrování parameter vectors navštívených během optimization k vytvoření final estimatoru.

## Poznámka Anki 1790001406542

Karty Anki: 1790001406542
GUID: d|oJ~-VT`;; štítky: (žádné).

### Otázka (Front)

Jaký benefit může mít parameter averaging?

### Odpověď (Back)

Snižuje variance stochastic trajectory a může zlepšit convergence/generalization.

## Poznámka Anki 1790001406543

Karty Anki: 1790001406543
GUID: iq+0w.&z!#; štítky: (žádné).

### Otázka (Front)

Co je pretraining jako optimization strategy?

### Odpověď (Back)

Inicializace parameters řešením jednoduššího nebo related tasku před hlavním trainingem.

## Poznámka Anki 1790001406544

Karty Anki: 1790001406544
GUID: mz84{V^;%B; štítky: (žádné).

### Otázka (Front)

Jak pretraining může pomoci optimization?

### Odpověď (Back)

Umístí parameters do regionu objective, ze kterého je hlavní task snazší optimalizovat.

## Poznámka Anki 1790001406545

Karty Anki: 1790001406545
GUID: A=P<R;Z_|A; štítky: (žádné).

### Otázka (Front)

Jak pretraining může pomoci generalization?

### Odpověď (Back)

Initialization může fungovat jako prior/regularizer preferující functions vhodné pro related data.

## Poznámka Anki 1790001406546

Karty Anki: 1790001406546
GUID: g3/qd<*,2]; štítky: (žádné).

### Otázka (Front)

Co je greedy layer-wise pretraining?

### Odpověď (Back)

Postupné trénování jednotlivých layers nebo shallow modules před joint fine-tuning celé deep network.

## Poznámka Anki 1790001406547

Karty Anki: 1790001406547
GUID: Btiv*B%gq-; štítky: (žádné).

### Otázka (Front)

Co je supervised pretraining?

### Odpověď (Back)

Initialization částí modelu pomocí jednodušších supervised tasks nebo shallow models.

## Poznámka Anki 1790001406548

Karty Anki: 1790001406548
GUID: LQ_cEos7.:; štítky: (žádné).

### Otázka (Front)

Jak architecture design může fungovat jako optimization strategy?

### Odpověď (Back)

Volba units a connectivity může výrazně měnit gradient flow a conditioning, například ReLU místo saturating nonlinearities.

## Poznámka Anki 1790001406549

Karty Anki: 1790001406549
GUID: A8<Nv+ZU:_; štítky: (žádné).

### Otázka (Front)

Co je continuation method?

### Odpověď (Back)

Optimization strategy, která nejprve řeší vyhlazenou nebo jednodušší verzi objective a postupně přechází k původní obtížnější objective.

## Poznámka Anki 1790001406550

Karty Anki: 1790001406550
GUID: IeBLzS{1_5; štítky: (žádné).

### Otázka (Front)

Co je curriculum learning?

### Odpověď (Back)

Continuation-like training, které nejprve používá jednodušší examples a postupně přidává obtížnější.

## Poznámka Anki 1790001406551

Karty Anki: 1790001406551
GUID: CddgdtZ3!6; štítky: (žádné).

### Otázka (Front)

Jaká je intuition curriculum learningu?

### Odpověď (Back)

Snazší examples nejprve odhalí základní structure a nasměrují parameters do regionu, kde lze efektivně zvládnout těžší examples.

## Poznámka Anki 1790001406552

Karty Anki: 1790001406552
GUID: N]hD%5.:|4; štítky: (žádné).

### Otázka (Front)

Je curriculum learning vždy výhodný?

### Odpověď (Back)

Ne; benefit závisí na tom, zda zvolená ordering skutečně vytváří užitečnou continuation path.

## Poznámka Anki 1790001406553

Karty Anki: 1790001406553
GUID: L%gkgN&wql; štítky: (žádné).

### Otázka (Front)

Jaký sjednocující princip mají initialization, normalization a momentum?

### Odpověď (Back)

Mění optimization geometry nebo trajectory, aniž by nutně měnily representational family modelu.

## Poznámka Anki 1790001406554

Karty Anki: 1790001406554
GUID: k1$,W>{Qob; štítky: (žádné).

### Otázka (Front)

Jaký sjednocující princip mají AdaGrad, RMSProp a Adam?

### Odpověď (Back)

Používají gradient history k adaptivnímu per-parameter škálování updates.

## Poznámka Anki 1790001406555

Karty Anki: 1790001406555
GUID: r1r}n(+kc_; štítky: (žádné).

### Otázka (Front)

Jaký rozdíl je mezi optimization failure a generalization failure?

### Odpověď (Back)

Optimization failure znamená vysoký training objective vzhledem k dostupné capacity; generalization failure znamená nízký training error, ale vysoký test error.

## Poznámka Anki 1790001406556

Karty Anki: 1790001406556
GUID: rN{Qq,^~H0; štítky: (žádné).

### Otázka (Front)

Co je convolution v kontextu convolutional networks?

### Odpověď (Back)

Operace kombinující input s kernel/filter weights sdílenými přes různé spatial nebo temporal positions.

## Poznámka Anki 1790001406557

Karty Anki: 1790001406557
GUID: iIwjV*=3T9; štítky: (žádné).

### Otázka (Front)

Jak se discrete 1D convolution formálně zapisuje?

### Odpověď (Back)

s(t)=(x*w)(t)=Σ_a x(a)w(t−a), přičemž v neural networks se často implementuje příbuzná cross-correlation bez otočení kernelu.

## Poznámka Anki 1790001406558

Karty Anki: 1790001406558
GUID: G4760ti6_c; štítky: (žádné).

### Otázka (Front)

Jaký rozdíl je mezi mathematical convolution a cross-correlation používanou v mnoha CNN knihovnách?

### Odpověď (Back)

Convolution kernel před násobením obrací, cross-correlation ne; při learned kernels je rozdíl obvykle jen v parametrizaci.

## Poznámka Anki 1790001406559

Karty Anki: 1790001406559
GUID: KV)~Q6eWlG; štítky: (žádné).

### Otázka (Front)

Proč neural networks běžně nazývají cross-correlation 'convolution'?

### Odpověď (Back)

Kernel se učí, takže jeho orientace není předem významná a obě operace mají stejné structural properties.

## Poznámka Anki 1790001406560

Karty Anki: 1790001406560
GUID: sf*D7ZJwx`; štítky: (žádné).

### Otázka (Front)

Jaké tři hlavní ideje dělají convolutional networks efektivní?

### Odpověď (Back)

Sparse interactions, parameter sharing a equivariant representations; pooling navíc může vytvářet invariance.

## Poznámka Anki 1790001406561

Karty Anki: 1790001406561
GUID: epvDR5YRp9; štítky: (žádné).

### Otázka (Front)

Co znamenají sparse interactions v CNN?

### Odpověď (Back)

Každý output unit interaguje jen s malou local subset inputu místo se všemi input units.

## Poznámka Anki 1790001406562

Karty Anki: 1790001406562
GUID: BOOP2_eGmy; štítky: (žádné).

### Otázka (Front)

Co je receptive field jednotky v convolutional layer?

### Odpověď (Back)

Subset původního nebo předchozího inputu, který může ovlivnit danou activation.

## Poznámka Anki 1790001406563

Karty Anki: 1790001406563
GUID: tIo8*NawYO; štítky: (žádné).

### Otázka (Front)

Jak se effective receptive field mění s hloubkou CNN?

### Odpověď (Back)

Skládáním local convolutions roste, takže deeper units mohou záviset na stále větší části původního inputu.

## Poznámka Anki 1790001406564

Karty Anki: 1790001406564
GUID: KR2piZ?(U%; štítky: (žádné).

### Otázka (Front)

Jak sparse connectivity snižuje computation oproti fully connected layer?

### Odpověď (Back)

Místo O(mn) connections může každý output používat jen k≪m inputs, tedy přibližně O(kn).

## Poznámka Anki 1790001406565

Karty Anki: 1790001406565
GUID: hY02GlW*R`; štítky: (žádné).

### Otázka (Front)

Co znamená parameter sharing v convolution?

### Odpověď (Back)

Stejný kernel parameter se používá na mnoha input locations.

## Poznámka Anki 1790001406566

Karty Anki: 1790001406566
GUID: AnPu-|&8u<; štítky: (žádné).

### Otázka (Front)

Jaký benefit má parameter sharing?

### Odpověď (Back)

Dramaticky snižuje počet parameters a umožňuje detekovat stejnou feature na různých positions.

## Poznámka Anki 1790001406567

Karty Anki: 1790001406567
GUID: P7RGiQBx!^; štítky: (žádné).

### Otázka (Front)

Jak se parameter sharing liší od sparse connectivity?

### Odpověď (Back)

Sparse connectivity omezuje, které input-output pairs interagují; sharing navíc nutí mnoho těchto interactions používat stejné weights.

## Poznámka Anki 1790001406568

Karty Anki: 1790001406568
GUID: I!]!BZg)R.; štítky: (žádné).

### Otázka (Front)

Co znamená equivariance funkce f vůči transformaci g?

### Odpověď (Back)

f(g(x))=g(f(x)); transformace inputu vyvolá odpovídající transformaci outputu.

## Poznámka Anki 1790001406569

Karty Anki: 1790001406569
GUID: KAnP8x>Zh?; štítky: (žádné).

### Otázka (Front)

Vůči jaké transformaci je standardní convolution přirozeně equivariantní?

### Odpověď (Back)

Vůči translation inputu, při odpovídajících boundary conventions.

## Poznámka Anki 1790001406570

Karty Anki: 1790001406570
GUID: M$z!S0Jr&6; štítky: (žádné).

### Otázka (Front)

Jak se translation equivariance liší od translation invariance?

### Odpověď (Back)

Equivariance posune feature map společně s inputem; invariance zachová output stejný bez ohledu na posun.

## Poznámka Anki 1790001406571

Karty Anki: 1790001406571
GUID: PJyiM}CW<:; štítky: (žádné).

### Otázka (Front)

Co je feature map?

### Odpověď (Back)

Spatial nebo temporal array activations vzniklá aplikací jednoho shared kernelu přes input.

## Poznámka Anki 1790001406572

Karty Anki: 1790001406572
GUID: tZmQtdB4r?; štítky: (žádné).

### Otázka (Front)

Proč CNN používá více kernels?

### Odpověď (Back)

Každý kernel se může naučit jiný typ local feature a vytváří vlastní feature map/channel.

## Poznámka Anki 1790001406573

Karty Anki: 1790001406573
GUID: rPiYlmJhU/; štítky: (žádné).

### Otázka (Front)

Co je pooling function?

### Odpověď (Back)

Operation nahrazující local neighborhood summary statistic, například maximum nebo average.

## Poznámka Anki 1790001406574

Karty Anki: 1790001406574
GUID: QnIf]X%pF]; štítky: (žádné).

### Otázka (Front)

Co je max pooling?

### Odpověď (Back)

Pooling vracející maximum activations v local region.

## Poznámka Anki 1790001406575

Karty Anki: 1790001406575
GUID: P,L&C+;7,q; štítky: (žádné).

### Otázka (Front)

Jak max pooling podporuje local translation invariance?

### Odpověď (Back)

Malý posun feature uvnitř pooling region často nezmění pooled maximum.

## Poznámka Anki 1790001406576

Karty Anki: 1790001406576
GUID: 2YS{YXkT5; štítky: (žádné).

### Otázka (Front)

Co je average pooling?

### Odpověď (Back)

Pooling vracející průměr activations local regionu.

## Poznámka Anki 1790001406577

Karty Anki: 1790001406577
GUID: PK>-%ZOrmv; štítky: (žádné).

### Otázka (Front)

Jaký trade-off vytváří pooling?

### Odpověď (Back)

Zvyšuje robustness/invariance a snižuje spatial resolution, ale může ztrácet přesnou location information.

## Poznámka Anki 1790001406578

Karty Anki: 1790001406578
GUID: Lm;Z8b{.5J; štítky: (žádné).

### Otázka (Front)

Proč pooling může snížit computational cost dalších vrstev?

### Odpověď (Back)

Downsampling feature maps zmenší počet spatial positions, které další layers zpracovávají.

## Poznámka Anki 1790001406579

Karty Anki: 1790001406579
GUID: u[lOos6jqb; štítky: (žádné).

### Otázka (Front)

Jak CNN vyjadřuje infinitely strong prior oproti fully connected layer?

### Odpověď (Back)

Architecture fixuje některé weights na nulu a jiné přesně svazuje, místo aby jen měkce preferovala locality a sharing.

## Poznámka Anki 1790001406580

Karty Anki: 1790001406580
GUID: l13@>gq)V3; štítky: (žádné).

### Otázka (Front)

Proč je convolution vhodná, když data mají grid topology?

### Odpověď (Back)

Lokální neighborhoods a stationarity patterns na gridu umožňují reuse stejné feature detector napříč positions.

## Poznámka Anki 1790001406581

Karty Anki: 1790001406581
GUID: t1y~4y=9z?; štítky: (žádné).

### Otázka (Front)

Jaké příklady grid-structured dat kniha uvádí?

### Odpověď (Back)

1D time-series data, 2D images a obecně arrays s pravidelným prostorovým nebo časovým uspořádáním.

## Poznámka Anki 1790001406582

Karty Anki: 1790001406582
GUID: o7*&&4T:Qe; štítky: (žádné).

### Otázka (Front)

Co je stride convolution?

### Odpověď (Back)

Posun kernelu o více než jeden input element mezi sousedními output positions.

## Poznámka Anki 1790001406583

Karty Anki: 1790001406583
GUID: JoO*>aX+wD; štítky: (žádné).

### Otázka (Front)

Jak větší stride ovlivňuje output?

### Odpověď (Back)

Snižuje spatial resolution a computation, protože convolution se vyhodnocuje na menším počtu positions.

## Poznámka Anki 1790001406584

Karty Anki: 1790001406584
GUID: g6G)O!qr1D; štítky: (žádné).

### Otázka (Front)

Co je zero padding?

### Odpověď (Back)

Rozšíření inputu nulami kolem boundary před convolution.

## Poznámka Anki 1790001406585

Karty Anki: 1790001406585
GUID: d%=u{-o/w.; štítky: (žádné).

### Otázka (Front)

Proč se používá padding?

### Odpověď (Back)

Řídí output size, umožňuje zachovat border information a dovoluje stackovat více convolutional layers bez rychlého zmenšení map.

## Poznámka Anki 1790001406586

Karty Anki: 1790001406586
GUID: Omyw)n,n#h; štítky: (žádné).

### Otázka (Front)

Co je valid convolution?

### Odpověď (Back)

Convolution bez paddingu; kernel se aplikuje jen tam, kde celý leží uvnitř inputu.

## Poznámka Anki 1790001406587

Karty Anki: 1790001406587
GUID: F#{:3H{jZ0; štítky: (žádné).

### Otázka (Front)

Co je same convolution v běžné terminologii?

### Odpověď (Back)

Padding zvolený tak, aby output měl při stride 1 přibližně stejný spatial size jako input.

## Poznámka Anki 1790001406588

Karty Anki: 1790001406588
GUID: sV];m:OVaK; štítky: (žádné).

### Otázka (Front)

Jaká nevýhoda má valid convolution ve velmi deep network?

### Odpověď (Back)

Spatial size se po každé vrstvě zmenšuje a boundary information rychle mizí.

## Poznámka Anki 1790001406589

Karty Anki: 1790001406589
GUID: cL=6(IgZxe; štítky: (žádné).

### Otázka (Front)

Jaká nevýhoda může mít extensive zero padding?

### Odpověď (Back)

Network může využívat umělé zeros jako location cue a boundary units mají odlišný effective context.

## Poznámka Anki 1790001406590

Karty Anki: 1790001406590
GUID: H!v;}0y:7K; štítky: (žádné).

### Otázka (Front)

Co je locally connected layer?

### Odpověď (Back)

Vrstva se sparse local connectivity jako convolution, ale bez parameter sharing mezi positions.

## Poznámka Anki 1790001406591

Karty Anki: 1790001406591
GUID: HU&1f1xSvo; štítky: (žádné).

### Otázka (Front)

Kdy může být locally connected layer vhodnější než convolution?

### Odpověď (Back)

Když stejné local features nemají být relevantní na různých locations a stationarity assumption neplatí.

## Poznámka Anki 1790001406592

Karty Anki: 1790001406592
GUID: s!ezex!eR7; štítky: (žádné).

### Otázka (Front)

Jaký cost má locally connected layer oproti convolution?

### Odpověď (Back)

Výrazně více parameters, protože každý spatial location má vlastní kernel.

## Poznámka Anki 1790001406593

Karty Anki: 1790001406593
GUID: m3D}UMk@;c; štítky: (žádné).

### Otázka (Front)

Co je tiled convolution?

### Odpověď (Back)

Kompromis mezi full sharing a locally connected layer, kde se opakuje menší sada kernels v periodickém patternu.

## Poznámka Anki 1790001406594

Karty Anki: 1790001406594
GUID: by{|nUjm|); štítky: (žádné).

### Otázka (Front)

Co je transposed convolution?

### Odpověď (Back)

Linear operation odpovídající transpose matrix representation convolution, často používaná k mapování menší feature map na větší.

## Poznámka Anki 1790001406595

Karty Anki: 1790001406595
GUID: eNo2<b1vpB; štítky: (žádné).

### Otázka (Front)

Je transposed convolution obecně inverse convolution?

### Odpověď (Back)

Ne; je to transpose lineárního operatoru, nikoli nutně jeho mathematical inverse.

## Poznámka Anki 1790001406596

Karty Anki: 1790001406596
GUID: rW1V&G5Pa+; štítky: (žádné).

### Otázka (Front)

Proč se transposed convolution někdy nepřesně nazývá deconvolution?

### Odpověď (Back)

Používá se pro upsampling-like generative transformations, ale neprovádí obecně skutečnou inversion původní convolution.

## Poznámka Anki 1790001406597

Karty Anki: 1790001406597
GUID: u,As;v8Wvj; štítky: (žádné).

### Otázka (Front)

Jak lze convolution reprezentovat jako matrix multiplication?

### Odpověď (Back)

Shared local kernel vytvoří sparse structured matrix, typicky Toeplitz-like; convolution je násobení touto maticí.

## Poznámka Anki 1790001406598

Karty Anki: 1790001406598
GUID: byhRroKHJI; štítky: (žádné).

### Otázka (Front)

Proč se convolution obvykle neimplementuje explicitním sparse matrix?

### Odpověď (Back)

Specialized convolution algorithms využívají regular structure rychleji a s menší memory.

## Poznámka Anki 1790001406599

Karty Anki: 1790001406599
GUID: fI{]9>sxsZ; štítky: (žádné).

### Otázka (Front)

Jak se gradient vůči inputu convolutional layer vztahuje k transposed convolution?

### Odpověď (Back)

Backpropagated gradient je násobení transpose convolution matrix, tedy právě transposed-convolution-like operation.

## Poznámka Anki 1790001406600

Karty Anki: 1790001406600
GUID: O]~yZq3yf); štítky: (žádné).

### Otázka (Front)

Co jsou outputs se structured spatial meaning v CNN?

### Odpověď (Back)

Predictions definované pro více input locations, například semantic segmentation nebo pixel labeling.

## Poznámka Anki 1790001406601

Karty Anki: 1790001406601
GUID: iju?O!d@q#; štítky: (žádné).

### Otázka (Front)

Jak lze CNN použít pro dense prediction?

### Odpověď (Back)

Nahradit fully connected layers convolutional layers a produkovat spatial map predictions.

## Poznámka Anki 1790001406602

Karty Anki: 1790001406602
GUID: uNhm|A)J/~; štítky: (žádné).

### Otázka (Front)

Proč je convolution efektivní pro dense sliding-window prediction?

### Odpověď (Back)

Sdílí intermediate computations překrývajících se windows místo opakovaného vyhodnocování celé network pro každý patch.

## Poznámka Anki 1790001406603

Karty Anki: 1790001406603
GUID: IvjQ3!x6pE; štítky: (žádné).

### Otázka (Front)

Co je downsampling?

### Odpověď (Back)

Snížení spatial nebo temporal resolution feature map například stride nebo poolingem.

## Poznámka Anki 1790001406604

Karty Anki: 1790001406604
GUID: K8|EN/TWNz; štítky: (žádné).

### Otázka (Front)

Co je upsampling?

### Odpověď (Back)

Zvýšení resolution representation pomocí interpolation, unpooling nebo transposed convolution.

## Poznámka Anki 1790001406605

Karty Anki: 1790001406605
GUID: Hw]oD@vfGP; štítky: (žádné).

### Otázka (Front)

Jak se liší convolution přes channels od spatial convolution?

### Odpověď (Back)

Kernel má weights pro všechny nebo subset input channels a lokální spatial extent; output channel kombinuje information přes channel dimension.

## Poznámka Anki 1790001406606

Karty Anki: 1790001406606
GUID: wlw4SKGWWo; štítky: (žádné).

### Otázka (Front)

Proč typical image convolution nesdílí weights přes channel index stejně jako přes spatial positions?

### Odpověď (Back)

Channel identity nese odlišný semantic význam, zatímco spatial position se předpokládá přibližně stationary.

## Poznámka Anki 1790001406607

Karty Anki: 1790001406607
GUID: N8M`9s[,SY; štítky: (žádné).

### Otázka (Front)

Jak lze convolution zobecnit na nepravidelné domains?

### Odpověď (Back)

Standardní convolution vyžaduje grid-like structure; jiné domains vyžadují specialized sharing, například graph convolutions, které však tato kapitola nerozvíjí.

## Poznámka Anki 1790001406608

Karty Anki: 1790001406608
GUID: h]r2m##1_{; štítky: (žádné).

### Otázka (Front)

Jaký relationship má convolution k probability priors?

### Odpověď (Back)

Architecture vyjadřuje prior, že relevantní interactions jsou local a stejné feature patterns se mohou objevovat na různých positions.

## Poznámka Anki 1790001406609

Karty Anki: 1790001406609
GUID: b.QfjH3B7q; štítky: (žádné).

### Otázka (Front)

Proč může být infinitely strong architectural prior nebezpečný?

### Odpověď (Back)

Pokud locality nebo translation-sharing assumption neplatí, model nemůže ani s mnoha daty reprezentovat některé useful interactions.

## Poznámka Anki 1790001406610

Karty Anki: 1790001406610
GUID: x42]JpU?6,; štítky: (žádné).

### Otázka (Front)

Jak CNN řeší velké input dimensionality images?

### Odpověď (Back)

Local connectivity a sharing udržují parameter count a computation manageable i při milionech pixels.

## Poznámka Anki 1790001406611

Karty Anki: 1790001406611
GUID: sfZEN/U5ws; štítky: (žádné).

### Otázka (Front)

Co je separable convolution v obecném computational smyslu?

### Odpověď (Back)

Kernel nebo operation lze rozložit na několik levnějších lower-dimensional operations.

## Poznámka Anki 1790001406612

Karty Anki: 1790001406612
GUID: b,wc2hBc(y; štítky: (žádné).

### Otázka (Front)

Jak FFT může zrychlit convolution?

### Odpověď (Back)

Convolution theorem převádí convolution ve spatial domain na element-wise multiplication ve frequency domain.

## Poznámka Anki 1790001406613

Karty Anki: 1790001406613
GUID: D<-_/[Ul>L; štítky: (žádné).

### Otázka (Front)

Kdy FFT-based convolution přináší největší benefit?

### Odpověď (Back)

Typicky pro velké kernels nebo velké feature maps; pro malé kernels může overhead převážit.

## Poznámka Anki 1790001406614

Karty Anki: 1790001406614
GUID: HKn:1;4MdE; štítky: (žádné).

### Otázka (Front)

Jaké další strategy lze použít k rychlé convolution?

### Odpověď (Back)

Specialized direct algorithms, matrix multiplication transformations a hardware-tuned implementations.

## Poznámka Anki 1790001406615

Karty Anki: 1790001406615
GUID: xxw1p9fzt#; štítky: (žádné).

### Otázka (Front)

Jak unsupervised feature learning souvisí s convolutional networks?

### Odpověď (Back)

Convolutional feature detectors lze naučit unsupervised methods a použít jako initialization nebo representations.

## Poznámka Anki 1790001406616

Karty Anki: 1790001406616
GUID: o1=ya]7Qv*; štítky: (žádné).

### Otázka (Front)

Co je random feature approach v CNN?

### Odpověď (Back)

Použití náhodně inicializovaných, někdy fixed convolutional filters a učení pouze pozdějších layers; může fungovat jako baseline, ale obvykle je horší než learned filters.

## Poznámka Anki 1790001406617

Karty Anki: 1790001406617
GUID: N(P4`-1D{=; štítky: (žádné).

### Otázka (Front)

Jaký neuroscience concept inspiroval convolutional architectures?

### Odpověď (Back)

Local receptive fields, retinotopic organization a hierarchical processing visual cortex.

