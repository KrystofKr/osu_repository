# Goodfellow – Blok 08 – karty 701–800

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001406618

Karty Anki: 1790001406618
GUID: KrKdkc=$UF; štítky: (žádné).

### Otázka (Front)

Co jsou simple cells v klasickém neuroscience modelu V1?

### Odpověď (Back)

Neurony citlivé na local oriented patterns na konkrétní position a phase, podobné convolutional linear filters.

## Poznámka Anki 1790001406619

Karty Anki: 1790001406619
GUID: xJ|Amu|dz}; štítky: (žádné).

### Otázka (Front)

Co jsou complex cells v klasickém modelu?

### Odpověď (Back)

Neurony méně citlivé na exact position/phase a více invariantní, analogicky pooling přes responses related simple cells.

## Poznámka Anki 1790001406620

Karty Anki: 1790001406620
GUID: qH/7oNcK?U; štítky: (žádné).

### Otázka (Front)

Jaký význam měl neocognitron pro historii CNN?

### Odpověď (Back)

Používal hierarchické local feature extraction a pooling-like mechanisms inspirované visual cortex, před moderním backprop-trained CNN.

## Poznámka Anki 1790001406621

Karty Anki: 1790001406621
GUID: BEB.Z)c%oe; štítky: (žádné).

### Otázka (Front)

Jaký historický model popularizoval gradient-trained CNN pro handwriting?

### Odpověď (Back)

LeNet family convolutional networks.

## Poznámka Anki 1790001406622

Karty Anki: 1790001406622
GUID: vWP%Al_g[q; štítky: (žádné).

### Otázka (Front)

Proč CNN sehrály zásadní roli v moderním deep learningu?

### Odpověď (Back)

Ukázaly, že architecture s vhodným structural prior a scalable gradient trainingem může dosáhnout vysokého výkonu na large-scale vision tasks.

## Poznámka Anki 1790001406623

Karty Anki: 1790001406623
GUID: nK-(~IBe:C; štítky: (žádné).

### Otázka (Front)

Jaký meta-princip shrnuje convolutional networks?

### Odpověď (Back)

Místo učení všech interactions nezávisle architecture explicitně využívá locality, stationarity a hierarchical composition k efektivnímu sdílení statistical strength.

## Poznámka Anki 1790001406624

Karty Anki: 1790001406624
GUID: Ob4?-U_dM3; štítky: (žádné).

### Otázka (Front)

Co je recurrent neural network (RNN)?

### Odpověď (Back)

Neural network obsahující recurrent connections, které umožňují sdílet parameters napříč různými positions v sequence a udržovat state závislý na minulosti.

## Poznámka Anki 1790001406625

Karty Anki: 1790001406625
GUID: BY@okf2p`y; štítky: (žádné).

### Otázka (Front)

Co znamená unfolding recurrent computational graphu?

### Odpověď (Back)

Nahrazení cyclic recurrent definition acyclic graph representation s kopií stejné computation pro každý time step a sdílenými parameters.

## Poznámka Anki 1790001406626

Karty Anki: 1790001406626
GUID: EFV]xpcH;F; štítky: (žádné).

### Otázka (Front)

Proč je unfolding důležitý?

### Odpověď (Back)

Umožňuje aplikovat běžný forward propagation a back-propagation na recurrent computation přes konečnou sequence.

## Poznámka Anki 1790001406627

Karty Anki: 1790001406627
GUID: nZNLFCzn:H; štítky: (žádné).

### Otázka (Front)

Jaký základní recurrent update má simple RNN?

### Odpověď (Back)

h^(t)=f(h^(t−1),x^(t);θ), často h^(t)=tanh(Wh^(t−1)+Ux^(t)+b).

## Poznámka Anki 1790001406628

Karty Anki: 1790001406628
GUID: glY?2Qk[vL; štítky: (žádné).

### Otázka (Front)

Jaký základní output může mít RNN?

### Odpověď (Back)

o^(t)=Vh^(t)+c a následná output distribution, například softmax y^(t)=softmax(o^(t)).

## Poznámka Anki 1790001406629

Karty Anki: 1790001406629
GUID: vS%[`9vB(S; štítky: (žádné).

### Otázka (Front)

Jak RNN sdílí statistical strength mezi sequence positions?

### Odpověď (Back)

Stejné recurrent, input a output parameters se používají v každém time step.

## Poznámka Anki 1790001406630

Karty Anki: 1790001406630
GUID: r5Cd&Dl@a^; štítky: (žádné).

### Otázka (Front)

Proč parameter sharing napříč časem umožňuje zpracovat variable-length sequences?

### Odpověď (Back)

Model definition nezávisí na konkrétní délce; recurrent transition lze aplikovat libovolný počet steps.

## Poznámka Anki 1790001406631

Karty Anki: 1790001406631
GUID: O7ncMleXLl; štítky: (žádné).

### Otázka (Front)

Jak RNN reprezentuje history sequence?

### Odpověď (Back)

Current hidden state h^(t) je learned summary předchozích inputs a states.

## Poznámka Anki 1790001406632

Karty Anki: 1790001406632
GUID: JNU7FzZ-%); štítky: (žádné).

### Otázka (Front)

Jaký rozdíl je mezi feedforward temporal window modelem a RNN?

### Odpověď (Back)

Feedforward model má fixed-size context, zatímco recurrent state může teoreticky přenášet information přes arbitrarily dlouhou minulost.

## Poznámka Anki 1790001406633

Karty Anki: 1790001406633
GUID: O!_XDI`h(~; štítky: (žádné).

### Otázka (Front)

Co je sequence-to-sequence RNN v širokém smyslu?

### Odpověď (Back)

Model mapující input sequence na output sequence, případně různé délky.

## Poznámka Anki 1790001406634

Karty Anki: 1790001406634
GUID: e[Eyv9RfVA; štítky: (žádné).

### Otázka (Front)

Jaký task odpovídá RNN s outputem v každém time step?

### Odpověď (Back)

Například sequence labeling nebo next-token prediction.

## Poznámka Anki 1790001406635

Karty Anki: 1790001406635
GUID: b>q%/kk9b%; štítky: (žádné).

### Otázka (Front)

Jaký task odpovídá RNN s jediným outputem po posledním step?

### Odpověď (Back)

Sequence classification, kde final hidden state shrnuje celý input.

## Poznámka Anki 1790001406636

Karty Anki: 1790001406636
GUID: k3}7)2(9<&; štítky: (žádné).

### Otázka (Front)

Jak lze generative RNN modelovat joint probability sequence?

### Odpověď (Back)

Pomocí chain rule p(x^(1),…,x^(τ))=∏_t p(x^(t)|x^(1),…,x^(t−1)), přičemž RNN parametrizuje jednotlivé conditionals.

## Poznámka Anki 1790001406637

Karty Anki: 1790001406637
GUID: k-T*9]lVKE; štítky: (žádné).

### Otázka (Front)

Jak se recurrent network trénuje pomocí maximum likelihood?

### Odpověď (Back)

Součet negative log-likelihood jednotlivých conditional outputs se backpropaguje přes unfolded graph.

## Poznámka Anki 1790001406638

Karty Anki: 1790001406638
GUID: CvK`|^YG:m; štítky: (žádné).

### Otázka (Front)

Co je back-propagation through time (BPTT)?

### Odpověď (Back)

Aplikace backpropagation na unfolded recurrent computational graph, která akumuluje gradient contributions přes time steps.

## Poznámka Anki 1790001406639

Karty Anki: 1790001406639
GUID: yb!%F<LabH; štítky: (žádné).

### Otázka (Front)

Proč gradients shared recurrent parameters sčítají contributions ze všech time steps?

### Odpověď (Back)

Stejný parameter se v unfolded graphu používá opakovaně, takže chain rule vyžaduje součet derivatives všech jeho usages.

## Poznámka Anki 1790001406640

Karty Anki: 1790001406640
GUID: wAsVkKKjPN; štítky: (žádné).

### Otázka (Front)

Co je truncated BPTT?

### Odpověď (Back)

Approximation BPTT, která propaguje gradients pouze omezený počet time steps zpět místo přes celou history.

## Poznámka Anki 1790001406641

Karty Anki: 1790001406641
GUID: qlziTPa2dm; štítky: (žádné).

### Otázka (Front)

Jaký computational benefit má truncated BPTT?

### Odpověď (Back)

Snižuje memory a runtime pro dlouhé sequences.

## Poznámka Anki 1790001406642

Karty Anki: 1790001406642
GUID: G0`L&i!0FX; štítky: (žádné).

### Otázka (Front)

Jaký statistical/optimization cost má truncated BPTT?

### Odpověď (Back)

Omezuje direct gradient signal pro dependencies delší než truncation horizon a vytváří biased gradient.

## Poznámka Anki 1790001406643

Karty Anki: 1790001406643
GUID: LEKpsMpxk]; štítky: (žádné).

### Otázka (Front)

Co je teacher forcing?

### Odpověď (Back)

Při trainingu sequence generatoru se jako input pro další time step používá skutečný předchozí target místo modelovy vlastní sampled prediction.

## Poznámka Anki 1790001406644

Karty Anki: 1790001406644
GUID: I#>P5bH?&o; štítky: (žádné).

### Otázka (Front)

Proč teacher forcing usnadňuje training?

### Odpověď (Back)

Model se učí conditionals pod correct histories a errors se během trainingu nekumulují přes sampled outputs.

## Poznámka Anki 1790001406645

Karty Anki: 1790001406645
GUID: sS1}:!5RV*; štítky: (žádné).

### Otázka (Front)

Jaký mismatch vytváří teacher forcing mezi trainingem a generation?

### Odpověď (Back)

Při generation model musí podmiňovat na vlastní předchozí predictions, které mohou obsahovat errors a posouvat state mimo training histories.

## Poznámka Anki 1790001406646

Karty Anki: 1790001406646
GUID: imn|[QoT4q; štítky: (žádné).

### Otázka (Front)

Co je computational graph RNN bez output-to-hidden recurrence?

### Odpověď (Back)

Hidden recurrence přenáší state, zatímco outputs jsou pouze readout z hidden state a nejsou explicitně vraceny jako recurrent inputs.

## Poznámka Anki 1790001406647

Karty Anki: 1790001406647
GUID: zI)8}QT}by; štítky: (žádné).

### Otázka (Front)

Proč může být RNN output conditional distribution multimodální i s deterministic hidden state?

### Odpověď (Back)

Output layer může parametrizovat categorical nebo jinou stochastic distribution, takže randomness je v output sampling.

## Poznámka Anki 1790001406648

Karty Anki: 1790001406648
GUID: eOz,{,e_AZ; štítky: (žádné).

### Otázka (Front)

Co je bidirectional RNN?

### Odpověď (Back)

Architecture se dvěma recurrent chains, jednou zpracovávající sequence forward a druhou backward; output v čase t využívá past i future context.

## Poznámka Anki 1790001406649

Karty Anki: 1790001406649
GUID: q(6VK}1X}d; štítky: (žádné).

### Otázka (Front)

Kdy bidirectional RNN nelze použít?

### Odpověď (Back)

V online causal prediction, kde future inputs ještě nejsou dostupné.

## Poznámka Anki 1790001406650

Karty Anki: 1790001406650
GUID: G_z[,UW:70; štítky: (žádné).

### Otázka (Front)

Jaký benefit má bidirectional RNN pro offline sequence labeling?

### Odpověď (Back)

Prediction každé position může využít kontext z obou stran sequence.

## Poznámka Anki 1790001406651

Karty Anki: 1790001406651
GUID: fsH5)6`eri; štítky: (žádné).

### Otázka (Front)

Co je encoder–decoder sequence-to-sequence architecture?

### Odpověď (Back)

Encoder přečte input sequence do representation/context a decoder conditioned na ní generuje output sequence.

## Poznámka Anki 1790001406652

Karty Anki: 1790001406652
GUID: J(dDE2-t};; štítky: (žádné).

### Otázka (Front)

Proč encoder–decoder umožňuje input a output sequences různých délek?

### Odpověď (Back)

Encoder a decoder mají oddělené recurrent computations a nejsou svázány one-to-one time alignmentem.

## Poznámka Anki 1790001406653

Karty Anki: 1790001406653
GUID: hLZ:3X,_fs; štítky: (žádné).

### Otázka (Front)

Jaký bottleneck má simple fixed-vector encoder–decoder?

### Odpověď (Back)

Veškerou informaci o dlouhém inputu musí komprimovat do jediného fixed-dimensional context vectoru.

## Poznámka Anki 1790001406654

Karty Anki: 1790001406654
GUID: zec9b(r7K]; štítky: (žádné).

### Otázka (Front)

Jak attention později zmírňuje fixed-context bottleneck?

### Odpověď (Back)

Decoder může v každém output step přistupovat k různým encoder states místo jediného summary vectoru.

## Poznámka Anki 1790001406655

Karty Anki: 1790001406655
GUID: vpiK2OjK@C; štítky: (žádné).

### Otázka (Front)

Co je deep recurrent network?

### Odpověď (Back)

RNN s depth v recurrent state transition, mezi recurrent layers, v input-to-hidden mapping nebo hidden-to-output mapping.

## Poznámka Anki 1790001406656

Karty Anki: 1790001406656
GUID: P/nD=Y(CYg; štítky: (žádné).

### Otázka (Front)

Jak lze depth vytvořit stackingem recurrent layers?

### Odpověď (Back)

Hidden sequence jedné RNN layer slouží jako input sequence další recurrent layer.

## Poznámka Anki 1790001406657

Karty Anki: 1790001406657
GUID: hNxTOx_`n-; štítky: (žádné).

### Otázka (Front)

Jak se temporal depth liší od architectural depth stacked RNN?

### Odpověď (Back)

Temporal depth vzniká opakováním transition přes time, zatímco architectural depth počtem distinct transformations v jednom time step.

## Poznámka Anki 1790001406658

Karty Anki: 1790001406658
GUID: O:3QFkK$eA; štítky: (žádné).

### Otázka (Front)

Co je recursive neural network?

### Odpověď (Back)

Network aplikující stejnou composition function rekurzivně na hierarchical/tree structure místo lineární time sequence.

## Poznámka Anki 1790001406659

Karty Anki: 1790001406659
GUID: E.LznN:UD@; štítky: (žádné).

### Otázka (Front)

Jaký typ dat přirozeně zpracovává recursive network?

### Odpověď (Back)

Trees, například parse trees v natural language.

## Poznámka Anki 1790001406660

Karty Anki: 1790001406660
GUID: bSdjky$kYU; štítky: (žádné).

### Otázka (Front)

Jak recursive network vytváří parent representation?

### Odpověď (Back)

Sdílená function kombinuje representations children do representation parent node.

## Poznámka Anki 1790001406661

Karty Anki: 1790001406661
GUID: E5jPzYm{qm; štítky: (žádné).

### Otázka (Front)

Jaký rozdíl je mezi recurrent a recursive network?

### Odpověď (Back)

Recurrent network sdílí parameters podél sequence/time; recursive network podél obecné hierarchical structure.

## Poznámka Anki 1790001406662

Karty Anki: 1790001406662
GUID: zfzB<6XY(P; štítky: (žádné).

### Otázka (Front)

Co je long-term dependency?

### Odpověď (Back)

Relationship mezi events oddělenými mnoha computational steps, pro kterou musí model uchovat a využít information přes dlouhý interval.

## Poznámka Anki 1790001406663

Karty Anki: 1790001406663
GUID: p#t%bD&v~+; štítky: (žádné).

### Otázka (Front)

Proč jsou long-term dependencies obtížné pro gradient-based RNN learning?

### Odpověď (Back)

Backpropagated derivatives obsahují products mnoha recurrent Jacobians, jejichž norms typicky exponenciálně rostou nebo klesají.

## Poznámka Anki 1790001406664

Karty Anki: 1790001406664
GUID: o@uv^b-vme; štítky: (žádné).

### Otázka (Front)

Jak eigenvalues recurrent Jacobian souvisejí s long-term gradientem v jednoduchém lineárním případě?

### Odpověď (Back)

Opakované násobení W vede k W^k; eigencomponents s |λ|<1 mizí a s |λ|>1 explodují.

## Poznámka Anki 1790001406665

Karty Anki: 1790001406665
GUID: B,0>Fu{`2<; štítky: (žádné).

### Otázka (Front)

Co je vanishing-gradient problem v RNN?

### Odpověď (Back)

Gradient signal z vzdálených time steps se exponenciálně zmenší, takže parameters nedostanou informace k učení dlouhodobých dependencies.

## Poznámka Anki 1790001406666

Karty Anki: 1790001406666
GUID: L4.d_{;PCP; štítky: (žádné).

### Otázka (Front)

Co je exploding-gradient problem v RNN?

### Odpověď (Back)

Gradient přes dlouhé dependencies exponenciálně naroste a způsobí extrémně velké, nestabilní updates.

## Poznámka Anki 1790001406667

Karty Anki: 1790001406667
GUID: O}IxVFYk-%; štítky: (žádné).

### Otázka (Front)

Proč může RNN teoreticky uchovat informaci dlouho, ale přesto ji neumět naučit?

### Odpověď (Back)

Representational existence long-memory solution neznamená, že gradient poskytne dostatečný signal k jejímu nalezení.

## Poznámka Anki 1790001406668

Karty Anki: 1790001406668
GUID: t:W`JFa>!u; štítky: (žádné).

### Otázka (Front)

Co je echo state network (ESN)?

### Odpověď (Back)

Recurrent model, jehož recurrent hidden dynamics jsou typicky random a fixed a učí se hlavně output weights.

## Poznámka Anki 1790001406669

Karty Anki: 1790001406669
GUID: bj/YUQIWmz; štítky: (žádné).

### Otázka (Front)

Co je reservoir v echo state network?

### Odpověď (Back)

Velká fixed recurrent hidden network transformující input history do high-dimensional dynamic representation.

## Poznámka Anki 1790001406670

Karty Anki: 1790001406670
GUID: ueTZFRZP(L; štítky: (žádné).

### Otázka (Front)

Jaký training benefit má ESN?

### Odpověď (Back)

Vyhne se obtížné optimization recurrent weights; output readout lze často učit jednoduchou regression.

## Poznámka Anki 1790001406671

Karty Anki: 1790001406671
GUID: o$ei~l^[g}; štítky: (žádné).

### Otázka (Front)

Co je spectral radius recurrent matrix?

### Odpověď (Back)

Maximum absolute eigenvalue matrix; v ESN se používá jako heuristic k řízení stability a memory dynamics.

## Poznámka Anki 1790001406672

Karty Anki: 1790001406672
GUID: c[(f|;Fcn?; štítky: (žádné).

### Otázka (Front)

Co je echo state property?

### Odpověď (Back)

Asymptotic state reservoiru má být primárně určován input history, nikoli arbitrary initial hidden state.

## Poznámka Anki 1790001406673

Karty Anki: 1790001406673
GUID: wxP}UYNwx`; štítky: (žádné).

### Otázka (Front)

Proč spectral radius <1 není univerzálně přesnou podmínkou echo state property?

### Odpověď (Back)

Nonlinear dynamics a input scaling mohou měnit stability; jde spíše o běžnou heuristic než úplnou characterization.

## Poznámka Anki 1790001406674

Karty Anki: 1790001406674
GUID: tg<g_3=z>1; štítky: (žádné).

### Otázka (Front)

Co jsou leaky units?

### Odpověď (Back)

Recurrent units, které kombinují nový candidate state s částí previous state a tím vytvářejí pomalejší time scale.

## Poznámka Anki 1790001406675

Karty Anki: 1790001406675
GUID: lmi(mh|lw#; štítky: (žádné).

### Otázka (Front)

Jaký jednoduchý leaky update lze použít?

### Odpověď (Back)

h^(t)=αh^(t−1)+(1−α)f(...), kde α určuje persistence.

## Poznámka Anki 1790001406676

Karty Anki: 1790001406676
GUID: N]1]X6%F+y; štítky: (žádné).

### Otázka (Front)

Jak α ovlivňuje time scale leaky unit?

### Odpověď (Back)

Vyšší α zachovává větší část minulého state a vytváří pomalejší dynamics.

## Poznámka Anki 1790001406677

Karty Anki: 1790001406677
GUID: u+,tTi]t~3; štítky: (žádné).

### Otázka (Front)

Proč je užitečné mít units s různými time scales?

### Odpověď (Back)

Různé latent factors sequence se mění různou rychlostí; model může současně sledovat rychlé i pomalé dependencies.

## Poznámka Anki 1790001406678

Karty Anki: 1790001406678
GUID: GMQGP}EyGR; štítky: (žádné).

### Otázka (Front)

Jak lze multiple time scales vytvořit kromě leaky integration?

### Odpověď (Back)

Například skip connections v čase, hierarchickými recurrent layers nebo gated mechanisms.

## Poznámka Anki 1790001406679

Karty Anki: 1790001406679
GUID: I.yyNaRdU; štítky: (žádné).

### Otázka (Front)

Co je LSTM?

### Odpověď (Back)

Gated recurrent architecture navržená tak, aby pomocí self-loop memory cell s řízeným gating usnadnila učení long-term dependencies.

## Poznámka Anki 1790001406680

Karty Anki: 1790001406680
GUID: HNNY0>8(~=; štítky: (žádné).

### Otázka (Front)

Co je LSTM cell state?

### Odpověď (Back)

Internal memory variable s téměř lineární self-connection, jejíž update je řízen gates.

## Poznámka Anki 1790001406681

Karty Anki: 1790001406681
GUID: bQem<czP52; štítky: (žádné).

### Otázka (Front)

Jakou roli má forget gate v LSTM?

### Odpověď (Back)

Určuje, jak velká část předchozího cell state se zachová.

## Poznámka Anki 1790001406682

Karty Anki: 1790001406682
GUID: F%{r:=EAU1; štítky: (žádné).

### Otázka (Front)

Jakou roli má input gate v LSTM?

### Odpověď (Back)

Určuje, kolik nového candidate contentu se zapíše do cell state.

## Poznámka Anki 1790001406683

Karty Anki: 1790001406683
GUID: ldO0290HcE; štítky: (žádné).

### Otázka (Front)

Jakou roli má output gate v LSTM?

### Odpověď (Back)

Řídí, kolik cell state se projeví v exposed hidden outputu.

## Poznámka Anki 1790001406684

Karty Anki: 1790001406684
GUID: MX5}),@T5S; štítky: (žádné).

### Otázka (Front)

Jaký typ functions gates typicky používají?

### Odpověď (Back)

Sigmoid outputs v (0,1), interpretovatelné jako soft multiplicative controls.

## Poznámka Anki 1790001406685

Karty Anki: 1790001406685
GUID: P0nd;ojVb%; štítky: (žádné).

### Otázka (Front)

Proč LSTM pomáhá proti vanishing gradients?

### Odpověď (Back)

Cell state má gated additive/near-linear path přes čas, po níž může gradient proudit bez opakovaného násobení saturating nonlinear Jacobians.

## Poznámka Anki 1790001406686

Karty Anki: 1790001406686
GUID: gh+M-?[miT; štítky: (žádné).

### Otázka (Front)

Je gradient přes LSTM cell vždy perfektně zachován?

### Odpověď (Back)

Ne; forget gates a další paths mohou gradient tlumit nebo měnit, ale architecture umožňuje naučit dlouhodobější preservation.

## Poznámka Anki 1790001406687

Karty Anki: 1790001406687
GUID: j(pY>DNj,B; štítky: (žádné).

### Otázka (Front)

Co je constant error carousel v historické LSTM terminologii?

### Odpověď (Back)

Self-loop cell s derivative blízkou 1, navržený k dlouhodobému zachování error signal.

## Poznámka Anki 1790001406688

Karty Anki: 1790001406688
GUID: L~:#eplBLP; štítky: (žádné).

### Otázka (Front)

Co je GRU?

### Odpověď (Back)

Gated recurrent unit, jednodušší gated architecture kombinující některé funkce LSTM gates a nemající oddělený cell/output state ve stejné podobě.

## Poznámka Anki 1790001406689

Karty Anki: 1790001406689
GUID: H;<wri<&rJ; štítky: (žádné).

### Otázka (Front)

Jakou roli má update gate v GRU?

### Odpověď (Back)

Řídí interpolation mezi previous hidden state a novým candidate state.

## Poznámka Anki 1790001406690

Karty Anki: 1790001406690
GUID: pO3c+%*G8P; štítky: (žádné).

### Otázka (Front)

Jakou roli má reset gate v GRU?

### Odpověď (Back)

Řídí, kolik previous state se používá při výpočtu candidate state.

## Poznámka Anki 1790001406691

Karty Anki: 1790001406691
GUID: tz1Hq$zm#1; štítky: (žádné).

### Otázka (Front)

Jak se GRU liší od LSTM?

### Odpověď (Back)

Má jednodušší gating a typicky méně parameters; LSTM používá oddělený cell state a explicitní input/forget/output gates.

## Poznámka Anki 1790001406692

Karty Anki: 1790001406692
GUID: r3aVV1u*)n; štítky: (žádné).

### Otázka (Front)

Je jedna z LSTM a GRU univerzálně lepší?

### Odpověď (Back)

Ne; performance závisí na tasku, data a tuning.

## Poznámka Anki 1790001406693

Karty Anki: 1790001406693
GUID: rz6zEYJROi; štítky: (žádné).

### Otázka (Front)

Co je gradient clipping?

### Odpověď (Back)

Nahrazení gradientu příliš velké normy rescaled gradientem s maximální povolenou normou.

## Poznámka Anki 1790001406694

Karty Anki: 1790001406694
GUID: obnpFems$X; štítky: (žádné).

### Otázka (Front)

Jak vypadá norm-based gradient clipping?

### Odpověď (Back)

Pokud ||g||>v, použije se g←v g/||g||.

## Poznámka Anki 1790001406695

Karty Anki: 1790001406695
GUID: hF!BPUc3aP; štítky: (žádné).

### Otázka (Front)

Proč gradient clipping řeší exploding gradients?

### Odpověď (Back)

Omezuje magnitude parameter update, i když backpropagated derivative exploduje.

## Poznámka Anki 1790001406696

Karty Anki: 1790001406696
GUID: e*gX*d^(c/; štítky: (žádné).

### Otázka (Front)

Řeší gradient clipping vanishing gradients?

### Odpověď (Back)

Ne; pouze zabraňuje extrémně velkým gradientům.

## Poznámka Anki 1790001406697

Karty Anki: 1790001406697
GUID: raT!EL%h5G; štítky: (žádné).

### Otázka (Front)

Proč je clipping podle global norm lepší než component-wise clipping pro zachování směru?

### Odpověď (Back)

Global rescaling zachová direction gradient vectoru, zatímco ořez jednotlivých components ji může změnit.

## Poznámka Anki 1790001406698

Karty Anki: 1790001406698
GUID: o$M]Qcrk_B; štítky: (žádné).

### Otázka (Front)

Co je regularization gradientu pro long-term dependencies popsaná v kapitole?

### Odpověď (Back)

Přidání objective podporující, aby gradient norm přes recurrent transition zůstávala blízko konstantní místo vanishing/exploding.

## Poznámka Anki 1790001406699

Karty Anki: 1790001406699
GUID: pE=.w%%Qp@; štítky: (žádné).

### Otázka (Front)

Jaký conflict může mít gradient-flow regularizer s hidden-state dynamics?

### Odpověď (Back)

Dynamics vhodná pro forward computation nemusí současně optimalizovat backward gradient norm; obě goals mohou vyžadovat kompromis.

## Poznámka Anki 1790001406700

Karty Anki: 1790001406700
GUID: g*YM|hF6I4; štítky: (žádné).

### Otázka (Front)

Co jsou explicit memory mechanisms?

### Odpověď (Back)

Architectures přidávající adresovatelnou memory oddělenou od fixed-dimensional recurrent hidden state.

## Poznámka Anki 1790001406701

Karty Anki: 1790001406701
GUID: sEKc%b2Eg5; štítky: (žádné).

### Otázka (Front)

Proč explicit memory může pomoci sequence models?

### Odpověď (Back)

Model nemusí komprimovat veškerou dlouhodobou informaci do jednoho fixed-size vectoru a může selektivně číst/zapisovat uložené položky.

## Poznámka Anki 1790001406702

Karty Anki: 1790001406702
GUID: q+w;$AN$H; štítky: (žádné).

### Otázka (Front)

Jaký klíčový operation potřebuje differentiable explicit memory?

### Odpověď (Back)

Differentiable nebo approximate-differentiable addressing/read-write mechanism, často pomocí soft attention.

## Poznámka Anki 1790001406703

Karty Anki: 1790001406703
GUID: jJ~9L`xz4V; štítky: (žádné).

### Otázka (Front)

Jak attention souvisí s explicit memory?

### Odpověď (Back)

Attention vytváří weighted read z několika memory entries podle jejich relevance k current query.

## Poznámka Anki 1790001406704

Karty Anki: 1790001406704
GUID: u=#s`S%2]k; štítky: (žádné).

### Otázka (Front)

Jaký meta-princip shrnuje gated RNNs a explicit memory?

### Odpověď (Back)

Long-term learning se usnadní vytvořením computational paths, po nichž lze information a gradient přenášet s menší ztrátou než přes opakovanou generic nonlinear transition.

## Poznámka Anki 1790001406705

Karty Anki: 1790001406705
GUID: xp@{^kc77]; štítky: (žádné).

### Otázka (Front)

Jaký rozdíl je mezi bidirectional RNN a encoder–decoder?

### Odpověď (Back)

Bidirectional RNN používá future i past context pro aligned outputs; encoder–decoder mapuje jednu celou sequence na jinou, často bez one-to-one alignmentu.

## Poznámka Anki 1790001406706

Karty Anki: 1790001406706
GUID: C/art3tQAe; štítky: (žádné).

### Otázka (Front)

Jaký rozdíl je mezi deep recurrent network a long unrolled RNN?

### Odpověď (Back)

Unrolling vytváří depth se shared parameters přes čas; deep recurrent architecture navíc používá více distinct transformations/layers v každém nebo mezi time steps.

## Poznámka Anki 1790001406707

Karty Anki: 1790001406707
GUID: eDQ;b%R,a*; štítky: (žádné).

### Otázka (Front)

Jaký relationship spojuje teacher forcing a probabilistic chain rule?

### Odpověď (Back)

Při maximum-likelihood trainingu každého conditional p(x_t|x_<t) jsou skutečné předchozí tokens známé, takže teacher forcing přesně odpovídá conditioning na observed history.

## Poznámka Anki 1790001406708

Karty Anki: 1790001406708
GUID: osRbuy8x6f; štítky: (žádné).

### Otázka (Front)

Proč sequence generation může akumulovat errors?

### Odpověď (Back)

Každá sampled prediction se stává contextem dalších predictions, takže chyba změní budoucí input distribution modelu.

## Poznámka Anki 1790001406709

Karty Anki: 1790001406709
GUID: NY]9nf=lU[; štítky: (žádné).

### Otázka (Front)

Jaký sjednocující problém řeší leaky units, LSTM a GRU?

### Odpověď (Back)

Umožňují naučit více časových měřítek a uchovávat information přes delší intervals než simple RNN.

## Poznámka Anki 1790001406710

Karty Anki: 1790001406710
GUID: EzoSg:)~c2; štítky: (žádné).

### Otázka (Front)

Jaký sjednocující problém řeší gradient clipping a gated memory jinými způsoby?

### Odpověď (Back)

Clipping stabilizuje optimization při exploding gradientu, zatímco gating mění architecture tak, aby gradient i state mohly být dlouhodoběji zachovány.

## Poznámka Anki 1790001406711

Karty Anki: 1790001406711
GUID: iNeRz&3]<=; štítky: (žádné).

### Otázka (Front)

Jaká meta-struktura shrnuje kapitolu 10?

### Odpověď (Back)

RNN sdílejí transition přes sequence, BPTT učí jejich dynamiku, long-term dependencies vytvářejí gradient instability a gated či explicit-memory architectures zavádějí lépe kontrolované paths pro uchování informace.

## Poznámka Anki 1790001406712

Karty Anki: 1790001406712
GUID: mM2}i5XS%!; štítky: (žádné).

### Otázka (Front)

Jaké čtyři kroky tvoří praktický deep-learning design process podle kapitoly 11?

### Odpověď (Back)

Stanovit cíle a performance metric; rychle vytvořit end-to-end baseline; instrumentovat systém a určit bottlenecks; iterativně provádět evidence-based změny.

## Poznámka Anki 1790001406713

Karty Anki: 1790001406713
GUID: wG$`FFL8OS; štítky: (žádné).

### Otázka (Front)

Proč se performance metric volí před konkrétním modelem?

### Odpověď (Back)

Určuje, co bude považováno za zlepšení, a tím řídí všechny další design decisions.

## Poznámka Anki 1790001406714

Karty Anki: 1790001406714
GUID: L~_decm.d(; štítky: (žádné).

### Otázka (Front)

Proč training cost nemusí být stejný jako application performance metric?

### Odpověď (Back)

Training cost se volí také podle optimization properties, zatímco application metric má odrážet skutečnou hodnotu nebo cenu chyb.

## Poznámka Anki 1790001406715

Karty Anki: 1790001406715
GUID: d9IG^~s>^G; štítky: (žádné).

### Otázka (Front)

Proč accuracy selhává u silně imbalanced classes?

### Odpověď (Back)

Model může dosáhnout vysoké accuracy pouhou predikcí majority class a přitom vůbec nedetekovat vzácnou positive class.

## Poznámka Anki 1790001406716

Karty Anki: 1790001406716
GUID: zU{_ki!`X~; štítky: (žádné).

### Otázka (Front)

Co je precision?

### Odpověď (Back)

Podíl predicted positives, které jsou skutečně positive: TP/(TP+FP).

## Poznámka Anki 1790001406717

Karty Anki: 1790001406717
GUID: d;7ZT:fwia; štítky: (žádné).

### Otázka (Front)

Co je recall?

### Odpověď (Back)

Podíl skutečných positives, které model detekuje: TP/(TP+FN).

