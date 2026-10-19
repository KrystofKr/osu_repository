# Goodfellow – Blok 09 – karty 801–900

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001406718

Karty Anki: 1790001406718
GUID: tq[hV:8/Ds; štítky: (žádné).

### Otázka (Front)

Jak threshold classifieru typicky mění precision–recall trade-off?

### Odpověď (Back)

Nižší threshold zvyšuje recall, ale často snižuje precision; vyšší threshold obvykle dělá opak.

## Poznámka Anki 1790001406719

Karty Anki: 1790001406719
GUID: KvH~}+L=Q_; štítky: (žádné).

### Otázka (Front)

Co je F1 score?

### Odpověď (Back)

Harmonický průměr precision a recall: F1=2PR/(P+R).

## Poznámka Anki 1790001406720

Karty Anki: 1790001406720
GUID: jUa`7)-NrC; štítky: (žádné).

### Otázka (Front)

Proč se používá harmonický průměr v F1?

### Odpověď (Back)

Silně penalizuje situaci, kdy je jedna z precision nebo recall velmi nízká.

## Poznámka Anki 1790001406721

Karty Anki: 1790001406721
GUID: tw*f[x|J80; štítky: (žádné).

### Otázka (Front)

Co je coverage systému, který může abstainovat?

### Odpověď (Back)

Podíl examples, na nichž systém skutečně vydá automatickou prediction.

## Poznámka Anki 1790001406722

Karty Anki: 1790001406722
GUID: yTRig57~27; štítky: (žádné).

### Otázka (Front)

Jaký trade-off vzniká mezi coverage a accuracy při možnosti abstention?

### Odpověď (Back)

Přísnější confidence threshold může zvýšit accuracy přijatých predictions, ale sníží coverage.

## Poznámka Anki 1790001406723

Karty Anki: 1790001406723
GUID: y^AZ<qprV3; štítky: (žádné).

### Otázka (Front)

Proč lze mít 100% accuracy s nulovou coverage?

### Odpověď (Back)

Systém může odmítnout odpovědět na každý example a tím neudělat žádnou automatickou chybu.

## Poznámka Anki 1790001406724

Karty Anki: 1790001406724
GUID: H/^MiNQM&V; štítky: (žádné).

### Otázka (Front)

Proč je rychlý end-to-end baseline zásadní?

### Odpověď (Back)

Poskytne reálná measurements celého pipeline a odhalí skutečné bottlenecks místo spekulativního optimalizování jednotlivých komponent.

## Poznámka Anki 1790001406725

Karty Anki: 1790001406725
GUID: B*sh}R.PJ_; štítky: (žádné).

### Otázka (Front)

Jaký baseline je rozumný pro fixed-size vector inputs?

### Odpověď (Back)

Fully connected feedforward network.

## Poznámka Anki 1790001406726

Karty Anki: 1790001406726
GUID: C>q~9RlIi~; štítky: (žádné).

### Otázka (Front)

Jaký baseline je rozumný pro images?

### Odpověď (Back)

Convolutional network.

## Poznámka Anki 1790001406727

Karty Anki: 1790001406727
GUID: cF-)_m#<C9; štítky: (žádné).

### Otázka (Front)

Jaký baseline je rozumný pro sequences?

### Odpověď (Back)

Gated recurrent network, například LSTM nebo GRU.

## Poznámka Anki 1790001406728

Karty Anki: 1790001406728
GUID: MoG!I@P-&8; štítky: (žádné).

### Otázka (Front)

Jaké activation functions kapitola doporučuje jako běžný baseline pro feedforward/CNN hidden layers?

### Odpověď (Back)

Piecewise-linear units, například ReLU nebo příbuzné rectifiers.

## Poznámka Anki 1790001406729

Karty Anki: 1790001406729
GUID: h`%<kb@]!z; štítky: (žádné).

### Otázka (Front)

Jaký optimizer je rozumný baseline podle knihy?

### Odpověď (Back)

SGD s momentum a decaying learning rate; Adam je další běžná alternativa.

## Poznámka Anki 1790001406730

Karty Anki: 1790001406730
GUID: E?fcb`2}xL; štítky: (žádné).

### Otázka (Front)

Jaký regularizer je téměř univerzálně vhodný baseline?

### Odpověď (Back)

Early stopping.

## Poznámka Anki 1790001406731

Karty Anki: 1790001406731
GUID: 9,8gNMKA4; štítky: (žádné).

### Otázka (Front)

Jakou další jednoduchou regularization kapitola doporučuje?

### Odpověď (Back)

Dropout, pokud dataset a architecture vyžadují další regularization.

## Poznámka Anki 1790001406732

Karty Anki: 1790001406732
GUID: B~>5fm;4*Y; štítky: (žádné).

### Otázka (Front)

Kdy je batch normalization vhodné rychle vyzkoušet?

### Odpověď (Back)

Když se objeví optimization difficulties nebo u architectures, kde empiricky výrazně stabilizuje training.

## Poznámka Anki 1790001406733

Karty Anki: 1790001406733
GUID: BB,Bk4@43O; štítky: (žádné).

### Otázka (Front)

Jak se rozhodnout, zda sbírat více dat?

### Odpověď (Back)

Nejprve porovnat training a validation/test performance a zjistit, zda problém vypadá jako underfitting nebo overfitting.

## Poznámka Anki 1790001406734

Karty Anki: 1790001406734
GUID: Cj:@@cnoHw; štítky: (žádné).

### Otázka (Front)

Co naznačuje vysoký training error?

### Odpověď (Back)

Nedostatečnou capacity, optimization problem, software bug nebo nedostatek predictive information v inputu; více stejných dat obvykle není první řešení.

## Poznámka Anki 1790001406735

Karty Anki: 1790001406735
GUID: DQ~uwMd3D*; štítky: (žádné).

### Otázka (Front)

Co naznačuje nízký training error a vysoký validation/test error?

### Odpověď (Back)

Velký generalization gap neboli overfitting.

## Poznámka Anki 1790001406736

Karty Anki: 1790001406736
GUID: e7LIbkBI3y; štítky: (žádné).

### Otázka (Front)

Kdy více dat typicky pomáhá nejvíce?

### Odpověď (Back)

Když je training performance dobrá, ale generalization výrazně horší.

## Poznámka Anki 1790001406737

Karty Anki: 1790001406737
GUID: D0ZhToI)2<; štítky: (žádné).

### Otázka (Front)

Co dělat, pokud training error zůstává vysoký?

### Odpověď (Back)

Zvýšit capacity, zlepšit optimization, zkontrolovat implementation a kvalitu/features dat.

## Poznámka Anki 1790001406738

Karty Anki: 1790001406738
GUID: -#gW,_Ti-; štítky: (žádné).

### Otázka (Front)

Jak learning curve pomáhá rozhodnout o dalším sběru dat?

### Odpověď (Back)

Ukazuje, jak se training a validation error mění s training-set size a zda další data stále přinášejí zlepšení.

## Poznámka Anki 1790001406739

Karty Anki: 1790001406739
GUID: ozNSRCH}|0; štítky: (žádné).

### Otázka (Front)

Co znamená, když train a validation curves konvergují k vysokému error?

### Odpověď (Back)

Přidávání podobných dat pravděpodobně nepomůže; limituje model capacity, features nebo optimization.

## Poznámka Anki 1790001406740

Karty Anki: 1790001406740
GUID: FE[FDDqL;m; štítky: (žádné).

### Otázka (Front)

Co znamená persistentní velký train–validation gap?

### Odpověď (Back)

Model má dost capacity fitovat data, ale nedostatečně generalizuje; více dat nebo silnější regularization mohou pomoci.

## Poznámka Anki 1790001406741

Karty Anki: 1790001406741
GUID: zHIg|T&Dc#; štítky: (žádné).

### Otázka (Front)

Jaký hyperparameter považuje kapitola za nejdůležitější k tuningu?

### Odpověď (Back)

Learning rate.

## Poznámka Anki 1790001406742

Karty Anki: 1790001406742
GUID: H]$kv%%T5f; štítky: (žádné).

### Otázka (Front)

Proč learning rate nemá monotonic relationship k capacity/performance?

### Odpověď (Back)

Příliš malý i příliš velký learning rate mohou training zhoršit; nejlepší výkon vzniká v intermediate range.

## Poznámka Anki 1790001406743

Karty Anki: 1790001406743
GUID: r:-nfyDepC; štítky: (žádné).

### Otázka (Front)

Jak capacity-controlling hyperparameter často ovlivňuje generalization error?

### Odpověď (Back)

Vytváří přibližně U-shaped curve: nízká capacity underfituje, příliš vysoká overfituje.

## Poznámka Anki 1790001406744

Karty Anki: 1790001406744
GUID: E*~E.D95|O; štítky: (žádné).

### Otázka (Front)

Co je manual hyperparameter tuning?

### Odpověď (Back)

Iterativní volba hyperparameters člověkem na základě understanding learning dynamics a výsledků předchozích experiments.

## Poznámka Anki 1790001406745

Karty Anki: 1790001406745
GUID: fY;G]KcS=}; štítky: (žádné).

### Otázka (Front)

Jaká je výhoda manual tuning?

### Odpověď (Back)

Expert může využít mechanism-level knowledge a brzy ukončit zjevně špatné experiments.

## Poznámka Anki 1790001406746

Karty Anki: 1790001406746
GUID: w|z;,6kL.|; štítky: (žádné).

### Otázka (Front)

Jaká je nevýhoda manual tuning?

### Odpověď (Back)

Je časově náročný, závisí na zkušenosti a obtížně škáluje na mnoho interacting hyperparameters.

## Poznámka Anki 1790001406747

Karty Anki: 1790001406747
GUID: ynqM4]1%-); štítky: (žádné).

### Otázka (Front)

Co je grid search?

### Odpověď (Back)

Vyhodnocení Cartesian productu předem zvolených values jednotlivých hyperparameters.

## Poznámka Anki 1790001406748

Karty Anki: 1790001406748
GUID: y+(>3i-*c^; štítky: (žádné).

### Otázka (Front)

Proč grid search špatně škáluje s dimensionality hyperparameter space?

### Odpověď (Back)

Počet trials roste exponenciálně jako přibližně n^m pro n values a m hyperparameters.

## Poznámka Anki 1790001406749

Karty Anki: 1790001406749
GUID: HZY73.p^W~; štítky: (žádné).

### Otázka (Front)

Proč se learning rate a podobné scale parameters hledají na log scale?

### Odpověď (Back)

Relevantní differences jsou multiplicative a optimum může ležet v několika orders of magnitude.

## Poznámka Anki 1790001406750

Karty Anki: 1790001406750
GUID: o9Ps/m6eal; štítky: (žádné).

### Otázka (Front)

Co signalizuje nejlepší grid-search value na hranici search range?

### Odpověď (Back)

Range pravděpodobně nepokrývá optimum a je vhodné jej rozšířit nebo posunout.

## Poznámka Anki 1790001406751

Karty Anki: 1790001406751
GUID: J&bh=,o<wb; štítky: (žádné).

### Otázka (Front)

Co je random search?

### Odpověď (Back)

Hyperparameter configurations se sampleují z předem definovaných distributions místo exhaustive Cartesian gridu.

## Poznámka Anki 1790001406752

Karty Anki: 1790001406752
GUID: knRrJQ2T=-; štítky: (žádné).

### Otázka (Front)

Proč random search často překoná grid search při stejném trial budgetu?

### Odpověď (Back)

Každý trial zkouší novou hodnotu každého hyperparameteru a neplýtvá kombinacemi podél dimensions, které jsou málo důležité.

## Poznámka Anki 1790001406753

Karty Anki: 1790001406753
GUID: lcqT){k&K-; štítky: (žádné).

### Otázka (Front)

Proč je random search zvlášť výhodný, když výkon závisí hlavně na několika hyperparameters?

### Odpověď (Back)

Pro důležité dimensions získá mnohem více unikátních values než grid se stejným počtem trials.

## Poznámka Anki 1790001406754

Karty Anki: 1790001406754
GUID: zvM^Ok%K^r; štítky: (žádné).

### Otázka (Front)

Jaká distribution je často vhodná pro positive scale hyperparameters v random search?

### Odpověď (Back)

Log-uniform distribution.

## Poznámka Anki 1790001406755

Karty Anki: 1790001406755
GUID: qk?}4r+XBY; štítky: (žádné).

### Otázka (Front)

Co je model-based hyperparameter optimization?

### Odpověď (Back)

Metoda budující surrogate model vztahu mezi hyperparameters a validation performance a používající jej k volbě dalších trials.

## Poznámka Anki 1790001406756

Karty Anki: 1790001406756
GUID: NCZ.`2dD=b; štítky: (žádné).

### Otázka (Front)

Jaký trade-off řeší Bayesian/model-based hyperparameter optimization?

### Odpověď (Back)

Exploration nejistých regions versus exploitation regions, kde surrogate očekává dobrý výkon.

## Poznámka Anki 1790001406757

Karty Anki: 1790001406757
GUID: A`Kdsi1)DP; štítky: (žádné).

### Otázka (Front)

Jaké constraints lze zahrnout do hyperparameter optimization?

### Odpověď (Back)

Runtime, memory, inference latency nebo jiné resource budgets vedle validation error.

## Poznámka Anki 1790001406758

Karty Anki: 1790001406758
GUID: h;_q5bLPl%; štítky: (žádné).

### Otázka (Front)

Jak nadměrný hyperparameter search může overfitovat validation set?

### Odpověď (Back)

Čím více configurations porovnáváme na stejné validation sample, tím větší je šance vybrat model těžící z validation noise.

## Poznámka Anki 1790001406759

Karty Anki: 1790001406759
GUID: iMXQ@f_]<D; štítky: (žádné).

### Otázka (Front)

Proč je debugging machine-learning systemu obtížný?

### Odpověď (Back)

Neznáme předem přesný správný output a adaptivní components mohou některé implementation errors částečně kompenzovat.

## Poznámka Anki 1790001406760

Karty Anki: 1790001406760
GUID: Q6s8|cwjBo; štítky: (žádné).

### Otázka (Front)

Jaký základní debugging princip kapitola doporučuje?

### Odpověď (Back)

Vytvořit jednoduché případy s předvídatelným správným behavior a izolovaně testovat components.

## Poznámka Anki 1790001406761

Karty Anki: 1790001406761
GUID: mz%BCg,NV6; štítky: (žádné).

### Otázka (Front)

Proč je vhodné přímo vizualizovat predictions modelu?

### Odpověď (Back)

Scalar metric může skrývat systematic errors nebo sama obsahovat bug; inspection často rychle odhalí nesmyslné behavior.

## Poznámka Anki 1790001406762

Karty Anki: 1790001406762
GUID: qn?c}pS[)z; štítky: (žádné).

### Otázka (Front)

Co znamená vizualizovat worst mistakes?

### Odpověď (Back)

Prohlížet examples, na nichž je model sebevědomě chybný nebo dává správnému targetu extrémně nízkou probability.

## Poznámka Anki 1790001406763

Karty Anki: 1790001406763
GUID: j&OR@iG#AH; štítky: (žádné).

### Otázka (Front)

Proč jsou worst-confidence errors diagnosticky výnosné?

### Odpověď (Back)

Často odhalí systematic preprocessing, labeling nebo modeling problem místo běžné ambiguity.

## Poznámka Anki 1790001406764

Karty Anki: 1790001406764
GUID: CH9DX]T2Lr; štítky: (žádné).

### Otázka (Front)

Co znamená test „fit a tiny dataset“?

### Odpověď (Back)

Ověřit, zda model dokáže téměř dokonale overfitnout jeden nebo několik training examples.

## Poznámka Anki 1790001406765

Karty Anki: 1790001406765
GUID: qZ7HRujx<r; štítky: (žádné).

### Otázka (Front)

Co signalizuje neschopnost classifieru fitnout jediný example?

### Odpověď (Back)

Silný důkaz implementation, optimization nebo capacity problému.

## Poznámka Anki 1790001406766

Karty Anki: 1790001406766
GUID: bg{H>5IfUV; štítky: (žádné).

### Otázka (Front)

Proč tiny-dataset test rozlišuje software bug od generalization problému?

### Odpověď (Back)

Na jediném example není generalization relevantní a dostatečně expressive model by jej měl snadno memorovat.

## Poznámka Anki 1790001406767

Karty Anki: 1790001406767
GUID: tG>CN0zlsc; štítky: (žádné).

### Otázka (Front)

Proč finite-difference ε nemá být ani příliš velké, ani příliš malé?

### Odpověď (Back)

Velké ε způsobuje truncation error, příliš malé ε cancellation a floating-point rounding error.

## Poznámka Anki 1790001406768

Karty Anki: 1790001406768
GUID: x4`Z-Pm+`7; štítky: (žádné).

### Otázka (Front)

Co lze zjistit z histogramů activations?

### Odpověď (Back)

Saturation, dead ReLUs, příliš velké nebo malé activation scales a další patologické regimes.

## Poznámka Anki 1790001406769

Karty Anki: 1790001406769
GUID: e8cyp.-7?*; štítky: (žádné).

### Otázka (Front)

Co lze zjistit z histogramů gradients?

### Odpověď (Back)

Vanishing/exploding gradients nebo vrstvy s výrazně odlišnou optimization scale.

## Poznámka Anki 1790001406770

Karty Anki: 1790001406770
GUID: JOL@s1fY3H; štítky: (žádné).

### Otázka (Front)

Proč sledovat ratio parameter update magnitude ku parameter magnitude?

### Odpověď (Back)

Pomáhá odhalit téměř frozen parameters nebo naopak příliš agresivní updates.

## Poznámka Anki 1790001406771

Karty Anki: 1790001406771
GUID: ze7]#CR|E1; štítky: (žádné).

### Otázka (Front)

Jaká diagnostika pomohla Street View house-number systemu?

### Odpověď (Back)

Vizualizace sebevědomých chyb odhalila, že detector cropoval images příliš těsně a někdy odřezával digits.

## Poznámka Anki 1790001406772

Karty Anki: 1790001406772
GUID: B4a?APhW&(; štítky: (žádné).

### Otázka (Front)

Jak byl cropping problem Street View systému pragmaticky opraven?

### Odpověď (Back)

Rozšířením crop regions místo komplikovaného redesignu detectoru.

## Poznámka Anki 1790001406773

Karty Anki: 1790001406773
GUID: Cid6wU5c][; štítky: (žádné).

### Otázka (Front)

Jaký obecný metodologický princip ilustruje Street View příklad?

### Odpověď (Back)

Největší improvement může přijít z odstranění skutečného measured bottlenecku, nikoli ze sofistikovanějšího learning algorithmu.

## Poznámka Anki 1790001406774

Karty Anki: 1790001406774
GUID: k&dx3xx/{A; štítky: (žádné).

### Otázka (Front)

Jaký generalization diagnosis měl Street View model po zlepšení output likelihood?

### Odpověď (Back)

Training a test error byly podobné, takže dominantní problém byl underfitting/data pipeline, nikoli overfitting.

## Poznámka Anki 1790001406775

Karty Anki: 1790001406775
GUID: dC<b(fK!W%; štítky: (žádné).

### Otázka (Front)

Proč pak dávalo smysl zvětšovat Street View model?

### Odpověď (Back)

Malý train–test gap znamenal, že zvýšení capacity mohlo snížit oba errors bez výrazného nárůstu overfittingu.

## Poznámka Anki 1790001406776

Karty Anki: 1790001406776
GUID: dQS(_/-:^!; štítky: (žádné).

### Otázka (Front)

Jaká meta-struktura shrnuje praktickou metodologii?

### Odpověď (Back)

Definuj metric → postav baseline → měř train/validation behavior a pipeline → diagnostikuj bottleneck → proveď cílenou změnu → opakuj.

## Poznámka Anki 1790001406777

Karty Anki: 1790001406777
GUID: cXv;sej:ol; štítky: (žádné).

### Otázka (Front)

Jaký hlavní princip kapitoly 12 spojuje různé deep-learning applications?

### Odpověď (Back)

Stejné základní learning principles se specializují podle structure modality, computational constraints a typu desired output.

## Poznámka Anki 1790001406778

Karty Anki: 1790001406778
GUID: BmSN3p<sLV; štítky: (žádné).

### Otázka (Front)

Proč je scale důležitý pro deep-learning applications?

### Odpověď (Back)

Větší models a datasets často zvyšují accuracy, ale vyžadují hardware a software schopné efektivně provádět masivní computation.

## Poznámka Anki 1790001406779

Karty Anki: 1790001406779
GUID: C1<^)c^|$k; štítky: (žádné).

### Otázka (Front)

Proč jsou GPUs vhodné pro neural networks?

### Odpověď (Back)

Poskytují vysoký parallelism a memory bandwidth pro regular matrix, convolution a element-wise operations.

## Poznámka Anki 1790001406780

Karty Anki: 1790001406780
GUID: Q!InbY#51p; štítky: (žádné).

### Otázka (Front)

Jaký trade-off mají GPUs oproti CPUs?

### Odpověď (Back)

Vyšší throughput na uniform parallel computation, ale menší flexibilitu pro branching-heavy serial workloads.

## Poznámka Anki 1790001406781

Karty Anki: 1790001406781
GUID: O!==SDQeNF; štítky: (žádné).

### Otázka (Front)

Co je data parallelism?

### Odpověď (Back)

Různé workers zpracovávají různé examples pomocí kopií stejného modelu.

## Poznámka Anki 1790001406782

Karty Anki: 1790001406782
GUID: o*CyGoYib7; štítky: (žádné).

### Otázka (Front)

Co je model parallelism?

### Odpověď (Back)

Jednotlivé části jednoho modelu/computation jsou rozděleny mezi více devices nebo machines.

## Poznámka Anki 1790001406783

Karty Anki: 1790001406783
GUID: bTh(2EQur); štítky: (žádné).

### Otázka (Front)

Proč je distributed training složitější než distributed inference?

### Odpověď (Back)

Workers musí koordinovat parameter updates a gradients, které jsou sekvenčně závislé.

## Poznámka Anki 1790001406784

Karty Anki: 1790001406784
GUID: fGTKilNM!b; štítky: (žádné).

### Otázka (Front)

Co je asynchronous SGD?

### Odpověď (Back)

Workers počítají gradients nezávisle a aplikují je na shared parameters bez úplné synchronizace po každém minibatchi.

## Poznámka Anki 1790001406785

Karty Anki: 1790001406785
GUID: zeYPup77}T; štítky: (žádné).

### Otázka (Front)

Jaký trade-off má asynchronous SGD?

### Odpověď (Back)

Stale gradients mohou být méně přesné, ale vyšší update throughput může training výrazně urychlit.

## Poznámka Anki 1790001406786

Karty Anki: 1790001406786
GUID: O8I9s%#)WH; štítky: (žádné).

### Otázka (Front)

Co je parameter server?

### Odpověď (Back)

Distributed service nebo architecture spravující shared parameters pro více training workers.

## Poznámka Anki 1790001406787

Karty Anki: 1790001406787
GUID: ByPlf0.,Xr; štítky: (žádné).

### Otázka (Front)

Co je model compression?

### Odpověď (Back)

Přenos learned function velkého modelu do menšího modelu s levnější inference.

## Poznámka Anki 1790001406788

Karty Anki: 1790001406788
GUID: NwHueT=uH1; štítky: (žádné).

### Otázka (Front)

Proč lze velký teacher model použít k trainingu menšího student modelu?

### Odpověď (Back)

Teacher poskytuje pseudo-targets na velkém množství inputs a jeho soft outputs nesou více information než hard labels.

## Poznámka Anki 1790001406789

Karty Anki: 1790001406789
GUID: syF/Cm6+|u; štítky: (žádné).

### Otázka (Front)

Co jsou soft targets v model compression?

### Odpověď (Back)

Celá predictive probability distribution teacheru, včetně probabilities incorrect classes.

## Poznámka Anki 1790001406790

Karty Anki: 1790001406790
GUID: b`hMOOmIOP; štítky: (žádné).

### Otázka (Front)

Proč jsou soft targets informativní?

### Odpověď (Back)

Odhalují similarity a uncertainty strukturu mezi classes, která se v one-hot labelu ztrácí.

## Poznámka Anki 1790001406791

Karty Anki: 1790001406791
GUID: D<Bp[4U;^-; štítky: (žádné).

### Otázka (Front)

Co je conditional computation?

### Odpověď (Back)

Model podle inputu aktivuje pouze subset units, experts nebo branches místo vyhodnocení celé network.

## Poznámka Anki 1790001406792

Karty Anki: 1790001406792
GUID: j*hFnL5,QK; štítky: (žádné).

### Otázka (Front)

Jaký benefit má conditional computation?

### Odpověď (Back)

Může výrazně zvýšit model capacity bez proporcionálního zvýšení computation per example.

## Poznámka Anki 1790001406793

Karty Anki: 1790001406793
GUID: w0G0T?yE#`; štítky: (žádné).

### Otázka (Front)

Co je classifier cascade?

### Odpověď (Back)

Sekvence classifiers, kde levné stages rychle odmítají easy negatives a expensive stages zpracují jen obtížné examples.

## Poznámka Anki 1790001406794

Karty Anki: 1790001406794
GUID: E`S:6=*4y^; štítky: (žádné).

### Otázka (Front)

Proč mají early cascade stages mít vysoký recall?

### Odpověď (Back)

Chybným odmítnutím positive example by jej pozdější, přesnější stages již nemohly zachránit.

## Poznámka Anki 1790001406795

Karty Anki: 1790001406795
GUID: Dm49K5&!1s; štítky: (žádné).

### Otázka (Front)

Co je mixture of experts?

### Odpověď (Back)

Architecture s několika expert subnetworks a gating mechanismem určujícím, jak se jejich outputs kombinují.

## Poznámka Anki 1790001406796

Karty Anki: 1790001406796
GUID: qkii5FBWu; štítky: (žádné).

### Otázka (Front)

Jak se soft a hard mixture of experts liší?

### Odpověď (Back)

Soft gating kombinuje více experts differentiable weights; hard gating vybírá jen jeden nebo několik experts.

## Poznámka Anki 1790001406797

Karty Anki: 1790001406797
GUID: E5.|JWF5$`; štítky: (žádné).

### Otázka (Front)

Proč hard gating může šetřit computation?

### Odpověď (Back)

Nevybrané experts není nutné vůbec vyhodnotit.

## Poznámka Anki 1790001406798

Karty Anki: 1790001406798
GUID: B5kTf8ktR(; štítky: (žádné).

### Otázka (Front)

Proč je hard gating obtížnější trénovat gradient descentem?

### Odpověď (Back)

Discrete selection není standardně differentiable.

## Poznámka Anki 1790001406799

Karty Anki: 1790001406799
GUID: L1(1e;KjEr; štítky: (žádné).

### Otázka (Front)

Jak attention souvisí s conditional computation?

### Odpověď (Back)

Soft attention je differentiable weighted selection information; hard attention je discrete conditional routing.

## Poznámka Anki 1790001406800

Karty Anki: 1790001406800
GUID: pkw2s#)}a!; štítky: (žádné).

### Otázka (Front)

Co je ASIC?

### Odpověď (Back)

Application-specific integrated circuit optimalizovaný pro konkrétní workload.

## Poznámka Anki 1790001406801

Karty Anki: 1790001406801
GUID: in^T1z=(.1; štítky: (žádné).

### Otázka (Front)

Co je FPGA?

### Odpověď (Back)

Reprogramovatelný hardware umožňující implementovat specialized circuits po výrobě.

## Poznámka Anki 1790001406802

Karty Anki: 1790001406802
GUID: jaTOiN%:};; štítky: (žádné).

### Otázka (Front)

Proč low-precision arithmetic může urychlit neural networks?

### Odpověď (Back)

Méně bitů snižuje memory bandwidth, storage, power a cost arithmetic operations.

## Poznámka Anki 1790001406803

Karty Anki: 1790001406803
GUID: fL[)$sv=Kv; štítky: (žádné).

### Otázka (Front)

Která fáze obvykle snese nižší precision lépe: training nebo inference?

### Odpověď (Back)

Inference; training je citlivější kvůli gradient accumulation a malým updates.

## Poznámka Anki 1790001406804

Karty Anki: 1790001406804
GUID: EAiRr{lTL:; štítky: (žádné).

### Otázka (Front)

Jaké základní computer-vision tasks kapitola zmiňuje?

### Odpověď (Back)

Classification, localization/detection, transcription a dense/pixel-wise labeling.

## Poznámka Anki 1790001406805

Karty Anki: 1790001406805
GUID: mmu$)L!^!Z; štítky: (žádné).

### Otázka (Front)

Proč CNN vyhovují vision?

### Odpověď (Back)

Images mají local grid structure a approximately translation-stationary features, které convolution efektivně sdílí.

## Poznámka Anki 1790001406806

Karty Anki: 1790001406806
GUID: FAkV-{|bFP; štítky: (žádné).

### Otázka (Front)

Jaký preprocessing images je skutečně zásadní?

### Odpověď (Back)

Konzistentní numerical scaling a základní normalization input values.

## Poznámka Anki 1790001406807

Karty Anki: 1790001406807
GUID: Bm8XYQ>%ut; štítky: (žádné).

### Otázka (Front)

Co je global contrast normalization?

### Odpověď (Back)

Centering a rescaling celého image podle jeho global mean a contrast.

## Poznámka Anki 1790001406808

Karty Anki: 1790001406808
GUID: bca]$;`KV!; štítky: (žádné).

### Otázka (Front)

Co je local contrast normalization?

### Odpověď (Back)

Normalization každého local region podle local mean a local standard deviation.

## Poznámka Anki 1790001406809

Karty Anki: 1790001406809
GUID: E|ia-E<`yx; štítky: (žádné).

### Otázka (Front)

Proč musí být contrast normalization regularizována?

### Odpověď (Back)

Téměř konstantní region může mít variance blízkou nule a division by tiny number by byla nestabilní.

## Poznámka Anki 1790001406810

Karty Anki: 1790001406810
GUID: JCfV57Q/i#; štítky: (žádné).

### Otázka (Front)

Jak dataset augmentation pomáhá computer vision?

### Odpověď (Back)

Vytváří label-preserving transformations jako translations, rotations, flips nebo color perturbations a vkládá desired invariances.

## Poznámka Anki 1790001406811

Karty Anki: 1790001406811
GUID: DI,8,E_Fty; štítky: (žádné).

### Otázka (Front)

Co je automatic speech recognition (ASR)?

### Odpověď (Back)

Mapping acoustic sequence na linguistic sequence words, characters nebo phonetic symbols.

## Poznámka Anki 1790001406812

Karty Anki: 1790001406812
GUID: gJe/-X:2P!; štítky: (žádné).

### Otázka (Front)

Jak tradiční GMM-HMM ASR rozdělilo modeling problem?

### Odpověď (Back)

HMM modelovalo sekvenční latent states a GMM modelovalo acoustic observations conditioned on states.

## Poznámka Anki 1790001406813

Karty Anki: 1790001406813
GUID: ka_nU26>(#; štítky: (žádné).

### Otázka (Front)

Jak deep networks změnily GMM-HMM speech recognition?

### Odpověď (Back)

DNN nahradily GMM jako silnější acoustic model pro posterior/likelihood HMM states.

## Poznámka Anki 1790001406814

Karty Anki: 1790001406814
GUID: p&y=Y(lK+9; štítky: (žádné).

### Otázka (Front)

Proč jsou RNN/LSTM vhodné pro speech?

### Odpověď (Back)

Acoustic evidence a linguistic context mají temporal dependencies přes různě dlouhé intervals.

## Poznámka Anki 1790001406815

Karty Anki: 1790001406815
GUID: AJ*5?H_6$u; štítky: (žádné).

### Otázka (Front)

Co znamená end-to-end speech recognition?

### Odpověď (Back)

Učit přímější mapping z acoustic inputu na output sequence s menším množstvím ručně navržených intermediate states.

## Poznámka Anki 1790001406816

Karty Anki: 1790001406816
GUID: PC[|/z8W}=; štítky: (žádné).

### Otázka (Front)

Co je language model?

### Odpověď (Back)

Probability distribution nad sequences tokens, typicky vyjádřená chain rule podmíněných next-token probabilities.

## Poznámka Anki 1790001406817

Karty Anki: 1790001406817
GUID: Fq(q9IPA`U; štítky: (žádné).

### Otázka (Front)

Co je n-gram language model?

### Odpověď (Back)

Model aproximující next-token probability pouze pomocí posledních n−1 tokens.

