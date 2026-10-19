# Goodfellow – Blok 10 – karty 901–1000

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001406818

Karty Anki: 1790001406818
GUID: l}53+&4G#F; štítky: (žádné).

### Otázka (Front)

Jaký hlavní problém mají n-gram models?

### Odpověď (Back)

Combinatorial sparsity: většina možných n-grams není ani ve velkém corpus pozorována.

## Poznámka Anki 1790001406819

Karty Anki: 1790001406819
GUID: OVzrm}5&=u; štítky: (žádné).

### Otázka (Front)

Co je smoothing n-gram modelu?

### Odpověď (Back)

Redistribution probability mass k unseen nebo rare n-grams, aby nedostaly nulovou probability.

## Poznámka Anki 1790001406820

Karty Anki: 1790001406820
GUID: vZ!TmXO!g~; štítky: (žádné).

### Otázka (Front)

Co je back-off?

### Odpověď (Back)

Použití shorter context modelu, když delší n-gram nemá dost statistik.

## Poznámka Anki 1790001406821

Karty Anki: 1790001406821
GUID: C1rMg?={CF; štítky: (žádné).

### Otázka (Front)

Proč one-hot word representation omezuje generalization?

### Odpověď (Back)

Všechna různá words jsou geometricky stejně odlišná a representation nevyjadřuje semantic similarity.

## Poznámka Anki 1790001406822

Karty Anki: 1790001406822
GUID: o)daP}X`z.; štítky: (žádné).

### Otázka (Front)

Co je word embedding?

### Odpověď (Back)

Learned dense low-dimensional vector representation wordu.

## Poznámka Anki 1790001406823

Karty Anki: 1790001406823
GUID: C5^nixX-Pn; štítky: (žádné).

### Otázka (Front)

Jak neural language model využívá embeddings proti curse of dimensionality?

### Odpověď (Back)

Sdílí statistical strength mezi words a contexts s podobnými learned features.

## Poznámka Anki 1790001406824

Karty Anki: 1790001406824
GUID: n4SHF1Ip-=; štítky: (žádné).

### Otázka (Front)

Jaký computational problém má flat softmax s velmi velkým vocabulary?

### Odpověď (Back)

Výpočet normalizeru a gradientu scales jako O(|V|) na prediction.

## Poznámka Anki 1790001406825

Karty Anki: 1790001406825
GUID: K78h*jN9&-; štítky: (žádné).

### Otázka (Front)

Co je hierarchical softmax?

### Odpověď (Back)

Tree factorization word probability do sequence local decisions, která může snížit cost probability jednoho wordu na O(log|V|).

## Poznámka Anki 1790001406826

Karty Anki: 1790001406826
GUID: rU&,A8.d/V; štítky: (žádné).

### Otázka (Front)

Jak se probability leaf wordu počítá v hierarchical softmax?

### Odpověď (Back)

Jako součin probabilities branch decisions podél path od rootu k leaf.

## Poznámka Anki 1790001406827

Karty Anki: 1790001406827
GUID: flcSzclU$L; štítky: (žádné).

### Otázka (Front)

Jaký design problem má hierarchical softmax?

### Odpověď (Back)

Volba nebo learning vhodné word hierarchy.

## Poznámka Anki 1790001406828

Karty Anki: 1790001406828
GUID: pG6IbBPh/e; štítky: (žádné).

### Otázka (Front)

Jak importance sampling zrychluje large-vocabulary training?

### Odpověď (Back)

Approximuje contribution většiny negative words malým samplem z proposal distribution.

## Poznámka Anki 1790001406829

Karty Anki: 1790001406829
GUID: Lk=POQ23}<; štítky: (žádné).

### Otázka (Front)

Co je ranking loss pro language modeling?

### Odpověď (Back)

Objective vyžadující, aby score correct wordu převyšovalo sampled incorrect words o margin.

## Poznámka Anki 1790001406830

Karty Anki: 1790001406830
GUID: wQ)hJy%/~?; štítky: (žádné).

### Otázka (Front)

Jaká nevýhoda ranking loss omezuje probabilistic use?

### Odpověď (Back)

Nevytváří přímo normalized conditional probabilities.

## Poznámka Anki 1790001406831

Karty Anki: 1790001406831
GUID: m9TlQ5k6f6; štítky: (žádné).

### Otázka (Front)

Jaký complementary benefit mají n-gram a neural language models?

### Odpověď (Back)

N-gram poskytuje velmi high-capacity sparse lookup; neural model poskytuje distributed generalization.

## Poznámka Anki 1790001406832

Karty Anki: 1790001406832
GUID: u#b})P-{65; štítky: (žádné).

### Otázka (Front)

Co je encoder–decoder model pro translation?

### Odpověď (Back)

Encoder vytvoří representation source sentence a decoder conditioned na ní generuje target sentence.

## Poznámka Anki 1790001406833

Karty Anki: 1790001406833
GUID: Kir*H%4>1h; štítky: (žádné).

### Otázka (Front)

Jaký bottleneck má jediný fixed context vector v translation?

### Odpověď (Back)

Dlouhá source sentence musí být kompletně komprimována do fixed-dimensional representation.

## Poznámka Anki 1790001406834

Karty Anki: 1790001406834
GUID: m)+2sTejpz; štítky: (žádné).

### Otázka (Front)

Co je attention?

### Odpověď (Back)

Mechanismus tvořící context jako learned weighted combination encoder representations podle relevance pro current decoder state.

## Poznámka Anki 1790001406835

Karty Anki: 1790001406835
GUID: rNc:lv/CNK; štítky: (žádné).

### Otázka (Front)

Jak se attention weights typicky normalizují?

### Odpověď (Back)

Softmaxem přes relevance scores.

## Poznámka Anki 1790001406836

Karty Anki: 1790001406836
GUID: Hyi=$tRHZ-; štítky: (žádné).

### Otázka (Front)

Jak attention pomáhá alignmentu v translation?

### Odpověď (Back)

Decoder může při generování každého target tokenu zdůraznit odpovídající source positions.

## Poznámka Anki 1790001406837

Karty Anki: 1790001406837
GUID: Q/YeAU0tD{; štítky: (žádné).

### Otázka (Front)

Co je recommender-system task?

### Odpověď (Back)

Predikce preference, probability action nebo expected utility user-item interaction.

## Poznámka Anki 1790001406838

Karty Anki: 1790001406838
GUID: cz#&_aX7`6; štítky: (žádné).

### Otázka (Front)

Co je collaborative filtering?

### Odpověď (Back)

Recommendation z patternů user-item interactions bez nutnosti rich content features.

## Poznámka Anki 1790001406839

Karty Anki: 1790001406839
GUID: lx:[:o^@e^; štítky: (žádné).

### Otázka (Front)

Jaký latent model se často používá pro collaborative filtering?

### Odpověď (Back)

User a item embeddings, jejichž dot product approximuje affinity.

## Poznámka Anki 1790001406840

Karty Anki: 1790001406840
GUID: nCL-s&-9ll; štítky: (žádné).

### Otázka (Front)

Jak lze rating predikovat bilinear modellem?

### Odpověď (Back)

R̂_ui=b_u+c_i+u_uᵀv_i.

## Poznámka Anki 1790001406841

Karty Anki: 1790001406841
GUID: CRz[cWtR+-; štítky: (žádné).

### Otázka (Front)

Co je cold-start problem?

### Odpověď (Back)

Nový user nebo item nemá dost interaction history pro collaborative filtering.

## Poznámka Anki 1790001406842

Karty Anki: 1790001406842
GUID: G@IFO!J5xN; štítky: (žádné).

### Otázka (Front)

Jak lze cold start řešit?

### Odpověď (Back)

Použít content features usera/itemu a naučit mapping těchto features do shared embedding space.

## Poznámka Anki 1790001406843

Karty Anki: 1790001406843
GUID: gCJsc7;MEY; štítky: (žádné).

### Otázka (Front)

Co je content-based recommendation?

### Odpověď (Back)

Recommendation využívající explicitní properties items/users místo pouze interaction matrix.

## Poznámka Anki 1790001406844

Karty Anki: 1790001406844
GUID: gEM$&N>6/4; štítky: (žádné).

### Otázka (Front)

Proč recommender data vytvářejí exploration problem?

### Odpověď (Back)

Systém pozoruje response pouze na actions/items, které sám zvolil.

## Poznámka Anki 1790001406845

Karty Anki: 1790001406845
GUID: I|sLLj>DQ^; štítky: (žádné).

### Otázka (Front)

Co je contextual bandit?

### Odpověď (Back)

Setting, kde agent pozoruje context, vybere jednu action a obdrží immediate reward bez dlouhodobé state transition sekvence.

## Poznámka Anki 1790001406846

Karty Anki: 1790001406846
GUID: u~r=1)AN@p; štítky: (žádné).

### Otázka (Front)

Co je exploitation?

### Odpověď (Back)

Volba action s nejvyšším current estimated reward.

## Poznámka Anki 1790001406847

Karty Anki: 1790001406847
GUID: bb&B?9boJ&; štítky: (žádné).

### Otázka (Front)

Co je exploration?

### Odpověď (Back)

Volba uncertain action za účelem získání informace, která může zlepšit future policy.

## Poznámka Anki 1790001406848

Karty Anki: 1790001406848
GUID: cdu]{R:&T%; štítky: (žádné).

### Otázka (Front)

Jak time horizon ovlivňuje exploration?

### Odpověď (Back)

Delší horizon zvyšuje hodnotu early exploration, protože knowledge lze využít v mnoha budoucích decisions.

## Poznámka Anki 1790001406849

Karty Anki: 1790001406849
GUID: reDCQ}of|N; štítky: (žádné).

### Otázka (Front)

Co je knowledge base?

### Odpověď (Back)

Structured collection facts o entities, attributes a relations používaná pro machine reasoning.

## Poznámka Anki 1790001406850

Karty Anki: 1790001406850
GUID: IP_U_]@X,%; štítky: (žádné).

### Otázka (Front)

Jak se binary relation reprezentuje?

### Odpověď (Back)

Jako triples (subject, relation, object).

## Poznámka Anki 1790001406851

Karty Anki: 1790001406851
GUID: GzsGU7u/n`; štítky: (žádné).

### Otázka (Front)

Co je knowledge graph?

### Odpověď (Back)

Graph s entities jako nodes a relations jako labeled edges.

## Poznámka Anki 1790001406852

Karty Anki: 1790001406852
GUID: vADgLI}u8s; štítky: (žádné).

### Otázka (Front)

Co je link prediction?

### Odpověď (Back)

Predikce chybějících relations v knowledge graphu.

## Poznámka Anki 1790001406853

Karty Anki: 1790001406853
GUID: EQ.bqU[h]T; štítky: (žádné).

### Otázka (Front)

Jak embeddings pomáhají knowledge representation?

### Odpověď (Back)

Entities a relations získají distributed vectors/operators, které umožňují generalizovat patterns na unseen facts.

## Poznámka Anki 1790001406854

Karty Anki: 1790001406854
GUID: tPjhpgsvtq; štítky: (žádné).

### Otázka (Front)

Proč evaluation link prediction potřebuje opatrnost u negative examples?

### Odpověď (Back)

Missing fact nemusí být false; knowledge base může být jen neúplná.

## Poznámka Anki 1790001406855

Karty Anki: 1790001406855
GUID: iutv6N%>Y.; štítky: (žádné).

### Otázka (Front)

Jak se approximate negatives často vytvářejí?

### Odpověď (Back)

Corrupting known true triples nahrazením jedné entity náhodnou jinou.

## Poznámka Anki 1790001406856

Karty Anki: 1790001406856
GUID: GK%gAuN:dY; štítky: (žádné).

### Otázka (Front)

Jaké schopnosti potřebuje general question-answering system?

### Odpověď (Back)

Reprezentovat input, uložit relevantní facts, retrievalnout je a provést reasoning.

## Poznámka Anki 1790001406857

Karty Anki: 1790001406857
GUID: n[j|q.n95U; štítky: (žádné).

### Otázka (Front)

Jak explicit memory pomáhá question answering?

### Odpověď (Back)

Umožňuje uchovat jednotlivé facts a dynamicky vybírat ty relevantní k query.

## Poznámka Anki 1790001406858

Karty Anki: 1790001406858
GUID: N*jAI6#^z5; štítky: (žádné).

### Otázka (Front)

Jaký meta-princip propojuje embeddings v language, recommendation a knowledge graphs?

### Odpověď (Back)

Discrete identities se mapují do continuous spaces, kde shared geometry podporuje similarity a statistical sharing.

## Poznámka Anki 1790001406859

Karty Anki: 1790001406859
GUID: J-}_4/aIoL; štítky: (žádné).

### Otázka (Front)

Jaký meta-princip propojuje scale engineering a model quality?

### Odpověď (Back)

Hardware/software efficiency určuje, jak velké models a datasety lze použít, a tím přímo omezuje dosažitelnou accuracy.

## Poznámka Anki 1790001406860

Karty Anki: 1790001406860
GUID: f[4KlsUK:&; štítky: (žádné).

### Otázka (Front)

Co je linear factor model?

### Odpověď (Back)

Latent-variable model generující observed x jako lineární transformaci latent factors h plus bias a noise.

## Poznámka Anki 1790001406861

Karty Anki: 1790001406861
GUID: mPs5/##:R7; štítky: (žádné).

### Otázka (Front)

Jaký generative equation má základní linear factor model?

### Odpověď (Back)

x=Wh+b+noise.

## Poznámka Anki 1790001406862

Karty Anki: 1790001406862
GUID: bhwuxN=5*r; štítky: (žádné).

### Otázka (Front)

Jaký prior se často předpokládá nad latent factors?

### Odpověď (Back)

Factorial prior p(h)=∏_i p(h_i).

## Poznámka Anki 1790001406863

Karty Anki: 1790001406863
GUID: tM=2F{2}aT; štítky: (žádné).

### Otázka (Front)

Co představují columns W?

### Odpověď (Back)

Latent directions/features, jejichž lineární kombinace generuje observed x.

## Poznámka Anki 1790001406864

Karty Anki: 1790001406864
GUID: mO|YZ,>|Ek; štítky: (žádné).

### Otázka (Front)

Co je factor analysis?

### Odpověď (Back)

Linear Gaussian latent-variable model s h~N(0,I) a independent Gaussian observation noise s diagonal covariance.

## Poznámka Anki 1790001406865

Karty Anki: 1790001406865
GUID: vB,9t;?7@2; štítky: (žádné).

### Otázka (Front)

Jaká je marginal covariance x ve factor analysis?

### Odpověď (Back)

WWᵀ+Ψ, kde Ψ je diagonal covariance residual noise.

## Poznámka Anki 1790001406866

Karty Anki: 1790001406866
GUID: hA~k.f%E+/; štítky: (žádné).

### Otázka (Front)

Jakou roli má WWᵀ ve factor analysis?

### Odpověď (Back)

Zachycuje dependencies observed variables vysvětlené shared latent factors.

## Poznámka Anki 1790001406867

Karty Anki: 1790001406867
GUID: nF&LB?wNZ#; štítky: (žádné).

### Otázka (Front)

Jakou roli má Ψ?

### Odpověď (Back)

Zachycuje residual per-variable noise, který shared factors nevysvětlují.

## Poznámka Anki 1790001406868

Karty Anki: 1790001406868
GUID: i8UIuM;m%p; štítky: (žádné).

### Otázka (Front)

Co je probabilistic PCA?

### Odpověď (Back)

Special case factor analysis s isotropic residual noise Ψ=σ²I.

## Poznámka Anki 1790001406869

Karty Anki: 1790001406869
GUID: Ch8{6_oAVM; štítky: (žádné).

### Otázka (Front)

Jaká je covariance x v probabilistic PCA?

### Odpověď (Back)

WWᵀ+σ²I.

## Poznámka Anki 1790001406870

Karty Anki: 1790001406870
GUID: bmLv}zR6Bj; štítky: (žádné).

### Otázka (Front)

Jak probabilistic PCA souvisí s classical PCA při σ→0?

### Odpověď (Back)

Probability mass se koncentruje kolem linear principal subspace a posterior mean code odpovídá projekci do tohoto subspace.

## Poznámka Anki 1790001406871

Karty Anki: 1790001406871
GUID: KAt!5GIpw.; štítky: (žádné).

### Otázka (Front)

Proč může příliš malé σ v probabilistic PCA být problematické?

### Odpověď (Back)

Data mimo learned subspace dostanou extrémně nízkou likelihood.

## Poznámka Anki 1790001406872

Karty Anki: 1790001406872
GUID: vbKzQ<i_8d; štítky: (žádné).

### Otázka (Front)

Co je independent component analysis (ICA)?

### Odpověď (Back)

Linear latent-factor method hledající components, které jsou statisticky independent a typicky non-Gaussian.

## Poznámka Anki 1790001406873

Karty Anki: 1790001406873
GUID: w8;pK$e#!?; štítky: (žádné).

### Otázka (Front)

Jaký základní generative ICA model lze zapsat?

### Odpověď (Back)

x=Wh s independent prior nad components h.

## Poznámka Anki 1790001406874

Karty Anki: 1790001406874
GUID: Pfz-D;B(Av; štítky: (žádné).

### Otázka (Front)

Proč ICA potřebuje non-Gaussian components pro identifiability?

### Odpověď (Back)

Gaussian independent sources lze po orthogonal rotations stále popsat stejnou joint Gaussian distribution, takže jejich směry nelze určit.

## Poznámka Anki 1790001406875

Karty Anki: 1790001406875
GUID: zc49}+k_7$; štítky: (žádné).

### Otázka (Front)

Jak se ICA liší od PCA?

### Odpověď (Back)

PCA decorreluje a řadí podle variance; ICA hledá silnější statistical independence pomocí higher-order structure.

## Poznámka Anki 1790001406876

Karty Anki: 1790001406876
GUID: F]DI_/7+NV; štítky: (žádné).

### Otázka (Front)

Co je blind source separation?

### Odpověď (Back)

Rozložení observed mixtures na underlying source signals bez přímého pozorování sources.

## Poznámka Anki 1790001406877

Karty Anki: 1790001406877
GUID: EC4h0p,kQA; štítky: (žádné).

### Otázka (Front)

Proč jsou některé ICA representations sparse?

### Odpověď (Back)

Používané super-Gaussian priors mají silný peak u nuly a těžší tails.

## Poznámka Anki 1790001406878

Karty Anki: 1790001406878
GUID: u@vq/mCSFH; štítky: (žádné).

### Otázka (Front)

Co je independent subspace analysis?

### Odpověď (Back)

Model dovolující dependence uvnitř groups components, ale podporující independence mezi groups.

## Poznámka Anki 1790001406879

Karty Anki: 1790001406879
GUID: eEi^~S&wR8; štítky: (žádné).

### Otázka (Front)

Co je topographic ICA?

### Odpověď (Back)

ICA-like model organizující related features do spatial neighborhoods, v nichž sousední features mají podobné properties.

## Poznámka Anki 1790001406880

Karty Anki: 1790001406880
GUID: I3kT.vfJbD; štítky: (žádné).

### Otázka (Front)

Jak topographic ICA může vést k phase/translation invariance?

### Odpověď (Back)

Pooling related filters s různými phases může reprezentovat pattern nezávisleji na exact local shift.

## Poznámka Anki 1790001406881

Karty Anki: 1790001406881
GUID: P[tED8f<|I; štítky: (žádné).

### Otázka (Front)

Co je slow feature analysis (SFA)?

### Odpověď (Back)

Representation-learning method hledající features, které se mění v čase co nejpomaleji při normalizačních a decorrelation constraints.

## Poznámka Anki 1790001406882

Karty Anki: 1790001406882
GUID: xkn:aQzbm); štítky: (žádné).

### Otázka (Front)

Co je slowness principle?

### Odpověď (Back)

Semantically významné latent factors se často mění pomaleji než raw sensory observations.

## Poznámka Anki 1790001406883

Karty Anki: 1790001406883
GUID: bb9/hZOy`J; štítky: (žádné).

### Otázka (Front)

Jaký objective minimalizuje SFA feature?

### Odpověď (Back)

Expected squared temporal difference E[(f(x_{t+1})−f(x_t))²].

## Poznámka Anki 1790001406884

Karty Anki: 1790001406884
GUID: L9iXs(ZWg,; štítky: (žádné).

### Otázka (Front)

Proč SFA potřebuje zero-mean constraint?

### Odpověď (Back)

Odstraňuje arbitrary constant offset a pomáhá identifikaci features.

## Poznámka Anki 1790001406885

Karty Anki: 1790001406885
GUID: wNRo6K0Iwo; štítky: (žádné).

### Otázka (Front)

Proč SFA potřebuje unit-variance constraint?

### Odpověď (Back)

Bez něj by trivial constant/zero feature minimalizovala slowness objective.

## Poznámka Anki 1790001406886

Karty Anki: 1790001406886
GUID: xD>0,^Y-@H; štítky: (žádné).

### Otázka (Front)

Proč SFA potřebuje decorrelation mezi více features?

### Odpověď (Back)

Aby všechny features nekopírovaly stejný nejpomalejší signal.

## Poznámka Anki 1790001406887

Karty Anki: 1790001406887
GUID: m3Jq0Y=#!7; štítky: (žádné).

### Otázka (Front)

Jak lze linear SFA rozšířit nelineárně?

### Odpověď (Back)

Nejprve použít nonlinear basis expansion a potom aplikovat linear SFA.

## Poznámka Anki 1790001406888

Karty Anki: 1790001406888
GUID: r[t{aZh+yt; štítky: (žádné).

### Otázka (Front)

Jak lze vytvořit deep SFA?

### Odpověď (Back)

Skládat více SFA stages s nonlinear expansions mezi nimi.

## Poznámka Anki 1790001406889

Karty Anki: 1790001406889
GUID: B2Sg>^<#;O; štítky: (žádné).

### Otázka (Front)

Jaké omezení má strict slowness prior?

### Odpověď (Back)

Useful factor se může měnit rychle, například position rychle se pohybujícího objektu; predictability může být vhodnější než absolutní pomalost.

## Poznámka Anki 1790001406890

Karty Anki: 1790001406890
GUID: EX_}Y*kU:u; štítky: (žádné).

### Otázka (Front)

Co je sparse coding?

### Odpověď (Back)

Model/reprezentace hledající latent code h, který rekonstruuje x pomocí dictionary W a současně má mnoho nulových nebo téměř nulových components.

## Poznámka Anki 1790001406891

Karty Anki: 1790001406891
GUID: cNpNS~H#]d; štítky: (žádné).

### Otázka (Front)

Jaký typ observation modelu používá basic sparse coding?

### Odpověď (Back)

Gaussian p(x|h) kolem Wh+b.

## Poznámka Anki 1790001406892

Karty Anki: 1790001406892
GUID: ur7A|:{ho); štítky: (žádné).

### Otázka (Front)

Jaký prior typicky podporuje sparsity h?

### Odpověď (Back)

Laplace, Student-t nebo jiný sharply peaked/heavy-tailed prior.

## Poznámka Anki 1790001406893

Karty Anki: 1790001406893
GUID: bYHbL~C[?H; štítky: (žádné).

### Otázka (Front)

Jaký MAP objective vzniká s Laplace prior?

### Odpověď (Back)

λ||h||₁+β||x−Wh||₂².

## Poznámka Anki 1790001406894

Karty Anki: 1790001406894
GUID: u9XW}-<=,X; štítky: (žádné).

### Otázka (Front)

Co vyjadřuje reconstruction term ve sparse codingu?

### Odpověď (Back)

Požadavek, aby aktivní dictionary atoms dobře vysvětlily observed input.

## Poznámka Anki 1790001406895

Karty Anki: 1790001406895
GUID: E:Ro{Q}F3r; štítky: (žádné).

### Otázka (Front)

Co vyjadřuje L¹ term?

### Odpověď (Back)

Preference code s malým počtem aktivních components.

## Poznámka Anki 1790001406896

Karty Anki: 1790001406896
GUID: n3y%onkb)!; štítky: (žádné).

### Otázka (Front)

Jak se sparse-coding inference liší od parametric encoderu?

### Odpověď (Back)

Code se pro každý input hledá iterative optimization místo jednoho learned forward mappingu.

## Poznámka Anki 1790001406897

Karty Anki: 1790001406897
GUID: q>oHbc_83L; štítky: (žádné).

### Otázka (Front)

Jaká výhoda má optimization-based encoder sparse codingu?

### Odpověď (Back)

Může přímo optimalizovat definovaný inference objective a není omezen approximation error konkrétní encoder network.

## Poznámka Anki 1790001406898

Karty Anki: 1790001406898
GUID: GGv>MEYFb#; štítky: (žádné).

### Otázka (Front)

Jaká nevýhoda má optimization-based encoder?

### Odpověď (Back)

Je pomalý při deploymentu a hůře se integruje do end-to-end differentiable pipeline.

## Poznámka Anki 1790001406899

Karty Anki: 1790001406899
GUID: JI[jyg:[>#; štítky: (žádné).

### Otázka (Front)

Jak se sparse coding typicky trénuje?

### Odpověď (Back)

Alternuje se inference codes H při fixed dictionary W a update W při fixed codes.

## Poznámka Anki 1790001406900

Karty Anki: 1790001406900
GUID: s3r._Qb]o7; štítky: (žádné).

### Otázka (Front)

Proč continuous Laplace generative prior nevytváří doslova exact-zero samples?

### Odpověď (Back)

Jednotlivý exact point má v continuous distribution probability zero; exact zeros vznikají spíše z MAP L¹ optimization.

## Poznámka Anki 1790001406901

Karty Anki: 1790001406901
GUID: F-$8`NCg[?; štítky: (žádné).

### Otázka (Front)

Co je dictionary ve sparse codingu?

### Odpověď (Back)

Sada learned basis vectors, typicky columns W, jejichž sparse kombinace rekonstruuje input.

## Poznámka Anki 1790001406902

Karty Anki: 1790001406902
GUID: bb;xY^lF>;; štítky: (žádné).

### Otázka (Front)

Proč factorial latent prior linear factor modelu může generovat špatné samples i při useful features?

### Odpověď (Back)

Neumí modelovat dependencies mezi activations, takže kombinuje features v configurations, které se v reálných datech nevyskytují.

## Poznámka Anki 1790001406903

Karty Anki: 1790001406903
GUID: iBFKF.dFyk; štítky: (žádné).

### Otázka (Front)

Jak hlubší generative model může zlepšit linear factor prior?

### Odpověď (Back)

Vyšší latent layers mohou modelovat dependencies určující, které lower-level features mají být aktivní společně.

## Poznámka Anki 1790001406904

Karty Anki: 1790001406904
GUID: M.vIDm<uIZ; štítky: (žádné).

### Otázka (Front)

Jak lze PCA interpretovat jako manifold model?

### Odpověď (Back)

Probability mass leží poblíž low-dimensional linear subspace vloženého do high-dimensional ambient space.

## Poznámka Anki 1790001406905

Karty Anki: 1790001406905
GUID: Gf!R^?oiM=; štítky: (žádné).

### Otázka (Front)

Jaká geometrická analogie popisuje probabilistic PCA?

### Odpověď (Back)

Tenký 'pancake': velká variance podél principal subspace a malá variance kolmo na něj.

## Poznámka Anki 1790001406906

Karty Anki: 1790001406906
GUID: Nj5rRc!/d]; štítky: (žádné).

### Otázka (Front)

Jaký reconstruction encoder-decoder odpovídá PCA?

### Odpověď (Back)

Encoder projektuje x−μ na principal directions a decoder jej projektuje zpět do ambient space.

## Poznámka Anki 1790001406907

Karty Anki: 1790001406907
GUID: cuRNF@RLo3; štítky: (žádné).

### Otázka (Front)

Jaký error minimalizuje d-dimensional PCA?

### Odpověď (Back)

Squared reconstruction error.

## Poznámka Anki 1790001406908

Karty Anki: 1790001406908
GUID: f_tb#F$Jn7; štítky: (žádné).

### Otázka (Front)

Čemu se rovná minimální PCA reconstruction error v eigenvalue decomposition covariance?

### Odpověď (Back)

Součtu eigenvalues odpovídajících vynechaným dimensions.

## Poznámka Anki 1790001406909

Karty Anki: 1790001406909
GUID: c-j+!T0**^; štítky: (žádné).

### Otázka (Front)

Proč je PCA omezená z manifold perspective?

### Odpověď (Back)

Reprezentuje pouze jediný linear subspace a nedokáže zachytit silně curved manifolds.

## Poznámka Anki 1790001406910

Karty Anki: 1790001406910
GUID: A}hm=dB2>+; štítky: (žádné).

### Otázka (Front)

Jaký common principle sdílejí PCA, ICA, SFA a sparse coding?

### Odpověď (Back)

Všechny hledají lineární latent representation, ale používají jiné criterion: variance/reconstruction, independence, temporal slowness nebo sparsity.

## Poznámka Anki 1790001406911

Karty Anki: 1790001406911
GUID: uD}NnZt<$-; štítky: (žádné).

### Otázka (Front)

Co je autoencoder?

### Odpověď (Back)

Neural network s encoderem h=f(x) a decoderem r=g(h), trénovaná tak, aby reconstruction r byla blízká inputu x.

## Poznámka Anki 1790001406912

Karty Anki: 1790001406912
GUID: oL)(O2I-4*; štítky: (žádné).

### Otázka (Front)

Proč perfektní identity function není useful autoencoder objective sama o sobě?

### Odpověď (Back)

Model by mohl pouze kopírovat input bez naučení struktury data distribution.

## Poznámka Anki 1790001406913

Karty Anki: 1790001406913
GUID: Ct5t-@bNxU; štítky: (žádné).

### Otázka (Front)

Jak autoencoder zabrání trivial identity solution?

### Odpověď (Back)

Omezí bottleneck/capacity nebo použije regularization jako sparsity, corruption či contraction.

## Poznámka Anki 1790001406914

Karty Anki: 1790001406914
GUID: z~2eO::sK[; štítky: (žádné).

### Otázka (Front)

Co je undercomplete autoencoder?

### Odpověď (Back)

Autoencoder s code dimensionality menší než input dimensionality.

## Poznámka Anki 1790001406915

Karty Anki: 1790001406915
GUID: NW&OM__2.s; štítky: (žádné).

### Otázka (Front)

Proč undercomplete bottleneck podporuje useful representation?

### Odpověď (Back)

Model musí komprimovat input a zachovat pouze information nejdůležitější pro reconstruction.

## Poznámka Anki 1790001406916

Karty Anki: 1790001406916
GUID: JhsZgFoy,~; štítky: (žádné).

### Otázka (Front)

Jaký vztah má linear undercomplete autoencoder s MSE k PCA?

### Odpověď (Back)

Naučí span stejného principal subspace jako PCA.

## Poznámka Anki 1790001406917

Karty Anki: 1790001406917
GUID: g+Ejilo2ht; štítky: (žádné).

### Otázka (Front)

Proč nonlinear undercomplete autoencoder může být výrazně silnější než PCA?

### Odpověď (Back)

Encoder a decoder mohou zachytit nonlinear manifold structure místo jediného linear subspace.

