# LLMs whitepapers – Původní blok 06

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::2 LLMs whitepapers
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783852352376

Karty Anki: 1783852352377
GUID: 2406f1f126; štítky: AI_whitepapers B6_001 konsolidace.

### Otázka (Front)

Co je embedding, jakou informaci nese jeho geometrie a proč je závislý na modelu a úloze?

### Odpověď (Back)

**Embedding** je hustý numerický vektor, který mapuje objekt — text, obraz, zvuk, video či jiná data — do latentního prostoru. Jde o **ztrátovou kompresi**: detaily se zahodí, ale model se snaží zachovat vlastnosti důležité pro cílovou úlohu. Vzdálenost nebo úhel mezi vektory pak aproximuje vztah objektů: blízké vektory mají být podle naučeného kritéria podobné. Embeddingy lze použít nejen pro search, ale jako feature vektory pro klasifikaci, clustering, doporučování či detekci anomálií. Podobnost je však **task-specific**: retrieval, klasifikace a jiné úlohy mohou vyžadovat jinou geometrii. Vektory vytvořené různými modely či verzemi obvykle neleží v kompatibilním prostoru a nesmějí se bez explicitního mapování porovnávat.

## Poznámka Anki 1783852352378

Karty Anki: 1783852352379
GUID: 2bf07f84bb; štítky: AI_whitepapers B6_002 konsolidace.

### Otázka (Front)

Jak se vyhodnocuje retrieval pomocí precision@k, recall@k a nDCG?

### Odpověď (Back)

Evaluace vyžaduje pro každý dotaz **gold relevance** dokumentů a metriku odpovídající produktu. 

- **Precision@k** = relevantní položky v top-k / k; měří čistotu vrácené špičky.
- **Recall@k** = relevantní položky v top-k / všechny relevantní položky; měří jejich pokrytí.
- **nDCG** používá odstupňovanou relevanci, zvýhodňuje správné položky nahoře a DCG normalizuje ideálním pořadím do rozsahu 0–1.
Precision a recall často zacházejí s relevancí binárně a samy nemusí postihnout kvalitu pořadí. Model s vyšším recall@k proto může působit hůře, jsou-li nejlepší výsledky umístěny níže. Retrieval, ranking, klasifikace a další použití embeddingů je nutné hodnotit jejich vlastními cílovými metrikami.

## Poznámka Anki 1783852352380

Karty Anki: 1783852352381
GUID: f07aa45ea3; štítky: AI_whitepapers B6_003 konsolidace.

### Otázka (Front)

Jak se volí embeddingový režim, encoderová architektura a task type pro různé aplikace?

### Odpověď (Back)

Hlavní aplikace zahrnují **retrieval** (Q&A a recommendations), semantic similarity (parafráze, duplicate detection, bitext mining), klasifikaci, clustering a reranking. 

- **Siamese/single encoder** používá stejnou síť pro oba vstupy.
- **Dual encoder/two-tower** má samostatnou query a document věž; hodí se, když dotazy a dokumenty mají jinou délku, styl a distribuci.
- Stejnou asymetrii mohou vyjádřit task types jako `RETRIEVAL_QUERY` a `RETRIEVAL_DOCUMENT`; další režimy jsou například `SEMANTIC_SIMILARITY`, `CLASSIFICATION` a `CLUSTERING`.
- Pro downstream klasifikaci nebo NER se na embedding přidá predikční vrstva; backbone lze zmrazit, fine-tunovat nebo trénovat spolu s headem podle množství dat a požadované kvality.
Předtrénovaný embedding model lze použít jako přenositelný feature extractor a případně dále dolaďovat.

## Poznámka Anki 1783852352382

Karty Anki: 1783852352383
GUID: b4dbb1f2db; štítky: AI_whitepapers B6_004 konsolidace.

### Otázka (Front)

Jak se vyvinuly tokenové a slovní embeddingy od one-hot reprezentace k Word2Vec, GloVe a SWIVEL?

### Odpověď (Back)

Text se nejprve **tokenizuje** na slova, subwordy, znaky, čísla či interpunkci a každý token dostane ID z vocabulary. ID ani one-hot vektor nemají přirozenou sémantiku; one-hot je navíc řídký a má dimenzi velikosti slovníku. Husté word embeddingy se učí z distribuce kontextů. 

- **Word2Vec CBOW** predikuje středové slovo z okolí; je rychlý a bývá silný pro častá slova.
- **Skip-gram** predikuje okolní slova ze středového; je pomalejší, ale pomáhá u menších dat a vzácných slov.
- **GloVe** využívá globální ko-výskytovou matici a zachycuje širší korpusové statistiky.
- **SWIVEL** faktoruje části ko-výskytové matice distribuovaně a speciální loss zohledňuje i nepozorované dvojice, což pomáhá rare words.
Tyto historické word embeddingy jsou obvykle kontextově nezávislé: jedno slovo má jeden vektor bez ohledu na větu.

## Poznámka Anki 1783852352384

Karty Anki: 1783852352385
GUID: 7c9c258f60; štítky: AI_whitepapers B6_005 konsolidace.

### Otázka (Front)

Jaké jsou klasické document representations: BoW, LSA, LDA, TF-IDF/BM25 a Doc2Vec?

### Odpověď (Back)

**Bag-of-Words** chápe dokument jako neuspořádaný multiset termů; ignoruje slovosled a bez dalších mechanismů i významové vztahy. 

- **LSA** redukuje word–document ko-výskytovou matici do latentního prostoru.
- **LDA** je generativní bayesovský model dokumentů jako směsí latentních témat.
- **TF-IDF** váží term podle četnosti v dokumentu a vzácnosti v korpusu; vzniká sparse vektor nebo váha pro agregaci word embeddingů.
- **BM25** je stále silný lexikální retrieval baseline.
- **Doc2Vec** přidává dokumentový/paragraph vektor k word embeddingům a učí jej při predikci slov. Pro známý dokument je vektor uložený, pro nový je nutná dodatečná inference/optimalizace.
Klasické metody jsou levné a silné pro přesné termy, ale hůře zachycují pořadí, kontext a parafráze než hluboké transformery.

## Poznámka Anki 1783852352386

Karty Anki: 1783852352387
GUID: 582178ef61; štítky: AI_whitepapers B6_006 konsolidace.

### Otázka (Front)

Jak vznikají moderní transformerové document embeddingy a jaké jsou jejich hlavní varianty a trade-offy?

### Odpověď (Back)

Transformery vytvářejí **kontextualizované tokenové reprezentace**: stejné slovo má podle okolí jiný vektor. Reprezentace sekvence může vzniknout poolingem nebo embeddingem speciálního tokenu `[CLS]`; samotný [CLS] však bez specializovaného fine-tuningu nemusí být optimální pro semantic similarity. Proto vznikly modely jako Sentence-BERT, SimCSE, E5, GTR nebo Sentence-T5, optimalizované pro retrieval či větnou podobnost. 

- **Single-vector**: jeden vektor na objekt; jednoduché, rychlé a úsporné indexování.
- **Multi-vector** (např. ColBERT, XTR): více reprezentací na objekt; lepší jemný matching, ale více storage a výpočtu.
- **Matryoshka embeddings**: model je učen tak, aby bylo možné použít zkrácený prefix dimenzí a řídit kompromis kvalita × storage × latence.
Hluboké modely vyžadují více dat a compute než BoW, ale lépe zachycují sekvenci a význam a lze je využít pro search, topic discovery, clustering i klasifikaci.

## Poznámka Anki 1783852352388

Karty Anki: 1783852352389
GUID: 3c46fb4c28; štítky: AI_whitepapers B6_007 konsolidace.

### Otázka (Front)

Jak se vytvářejí image a multimodální joint embeddings a co přinášejí modely typu ColPali?

### Odpověď (Back)

Unimodální image embedding lze získat například z předposlední vrstvy klasifikačního CNN nebo Vision Transformeru; ta nese přenositelné diskriminační features. **Multimodální/joint embedding** mapuje text a obraz do společného latentního prostoru, typicky pomocí dvou věží a kontrastivního tréninku. Umožňuje cross-modal retrieval, například textový dotaz → relevantní obrázek či produkt, i když se popis a vizuální obsah lexikálně neshodují. **ColPali** používá multi-vector reprezentace multimodálních dokumentů a vyhledává přímo nad renderovanými stránkami; tím může obejít složité OCR a layout preprocessing a zachovat textové i vizuální informace dokumentu.

## Poznámka Anki 1783852352390

Karty Anki: 1783852352391
GUID: 927b68ad27; štítky: AI_whitepapers B6_008 konsolidace.

### Otázka (Front)

Jak se liší embeddingy obecných strukturovaných dat a user/item embeddingy v doporučování?

### Odpověď (Back)

Strukturovaná data mají schéma a význam sloupců specifický pro doménu, proto pro ně často neexistuje univerzální předtrénovaný model. 

- **General structured embeddings** komprimují řádek tabulky například pomocí PCA nebo aplikací naučeného encoderu; používají se pro anomaly detection, klasifikaci a další downstream úlohy. Informativní nízkodimenzionální reprezentace může snížit množství labelovaných dat potřebných pro supervised model.
- **User/item embeddings** se učí z interakcí, například kliknutí či ratingů, aby latentní vzdálenost nebo dot product odpovídaly preferenci uživatele k produktu. Atributy, texty a obrázky itemů lze s interakčními embeddingy kombinovat.
Rozdíl je tedy mezi obecnou kompresí tabulkových features a společným latentním prostorem optimalizovaným na vztah uživatel–item.

## Poznámka Anki 1783852352392

Karty Anki: 1783852352393
GUID: 650b627158; štítky: AI_whitepapers B6_009 konsolidace.

### Otázka (Front)

Co zachycují graph embeddings a pro jaké úlohy se používají?

### Odpověď (Back)

**Graph embedding** reprezentuje uzel nebo celý graf tak, aby vektor nesl nejen atributy, ale i sousedství a relační strukturu. Propojené či strukturálně podobné uzly mají získat podobné reprezentace; proto jsou graph embeddings přirozenou volbou, když význam vzniká ze sítě vztahů. Použití zahrnuje node/graph classification, link prediction, community clustering, search a recommendations. Mezi klasické algoritmy patří DeepWalk, Node2vec, LINE a GraphSAGE. Oproti „plochému“ tabulkovému embeddingu explicitně využívají topologii grafu a mohou být výrazně lepší tam, kde sousedé a hrany nesou klíčový signál.

## Poznámka Anki 1783852352394

Karty Anki: 1783852352395
GUID: 733dca954f; štítky: AI_whitepapers B6_010 konsolidace.

### Otázka (Front)

Kdy použít lexikální, vektorové nebo hybridní vyhledávání a jak vypadá základní vector-search pipeline?

### Odpověď (Back)

**Lexikální search** (TF-IDF/BM25) skóruje shodu termů a je silný pro přesné názvy, ID, kódy a doménové tokeny. **Vector search** embeduje položky i dotaz stejným kompatibilním modelem a hledá nejbližší vektory; funguje pro parafráze, překlepy a sémantické shody i napříč modalitami. Minimální pipeline: offline spočítat a uložit embeddingy korpusu → online embedovat dotaz → nearest-neighbor search. **Hybrid search** kombinuje oba signály s metadata filtry, pre/post-filteringem a případným rerankingem. Rychlé pravidlo: přesné termy/ID → lexikálně; význam/parafráze → vektorově; obojí nebo tvrdé filtry → hybridně. Vector DB zajišťuje nízkolatenční hledání ve velkých kolekcích.

## Poznámka Anki 1783852352396

Karty Anki: 1783852352397
GUID: d79a2b138e; štítky: AI_whitepapers B6_011 konsolidace.

### Otázka (Front)

Proč se používá ANN a jak fungují LSH a HNSW?

### Odpověď (Back)

Přesný brute-force nearest-neighbor porovná dotaz se všemi n vektory a ve velkém měřítku je příliš pomalý. **Approximate Nearest Neighbor (ANN)** obětuje část recall za výrazně nižší latenci a lepší škálování. Klasické rodiny zahrnují stromy (KD/Ball tree), hashing a grafové indexy; jejich kombinací lze ladit speed–accuracy trade-off. 

- **LSH** používá hash funkce, u nichž podobné vektory s vyšší pravděpodobností skončí ve stejném bucketu, a omezuje tak kandidáty.
- **HNSW** je hierarchický proximity graf. Greedy navigace začíná v řídkých horních vrstvách s dlouhými hranami a sestupuje k jemnějším sousedům; typicky nabízí sublineární chování kolem O(log n). Paměť a rychlost lze dále optimalizovat kvantizací.
ANN řeší výpočet nejbližších sousedů; vector DB nad ním řeší provozní správu.

## Poznámka Anki 1783852352398

Karty Anki: 1783852352399
GUID: bb1d39db72; štítky: AI_whitepapers B6_012 konsolidace.

### Otázka (Front)

Jak funguje ScaNN od partitioningu přes scoring po rescoring?

### Odpověď (Back)

**ScaNN** je škálovatelná ANN pipeline se třemi vrstvami: 

1. **Partitioning/pruning:** prostor se rozdělí do clusterů a pro dotaz se prohledá jen několik nejbližších. U velkých datasetů je klíčový; orientační počet partitionů může být přibližně √n. Vyšší počet partitionů či `partitions_to_search` obvykle zvyšuje recall i cenu.
2. **Scoring:** v kandidátních partitions se vybere top K′ pomocí přesné nebo aproximované vzdálenosti; aproximace může používat product nebo anisotropic quantization.
3. **Rescoring:** malá kandidátní množina se volitelně přepočítá přesněji, čímž se vrátí část kvality za malou dodatečnou latenci.
ScaNN tak kombinuje pruning, levný scoring a přesnější finální výběr; je základem Vertex AI Vector Search.

## Poznámka Anki 1783852352400

Karty Anki: 1783852352401
GUID: 3f5c1ec34d; štítky: AI_whitepapers B6_013 konsolidace.

### Otázka (Front)

Co přidává vector database nad ANN index a podle čeho se vybírá?

### Odpověď (Back)

**Vector database** spojuje ukládání embeddingů a ANN dotazy s databázovými vlastnostmi: horizontální/vertikální škálování, dostupnost a konzistenci, realtime updates, backupy, access control, compliance, filtry a správu indexů. Managed příklady zahrnují Vertex AI Vector Search, Pinecone, Elasticsearch a vector funkce v AlloyDB/Cloud SQL; Postgres přes `pgvector` kombinuje vektorové dotazy se SQL predikáty a transakcemi. OSS příklady jsou Weaviate a ChromaDB. Při výběru zvaž velikost a typ vektorů, latency/throughput, rozpočet, security/privacy, hybridní search a integraci se stávajícími systémy. Pro OLTP a časté zápisy se hodí operational DB; pro velký OLAP/batch může být vhodnější analytické řešení typu BigQuery vector search.

## Poznámka Anki 1783852352402

Karty Anki: 1783852352403
GUID: cb1ef632b1; štítky: AI_whitepapers B6_014 konsolidace.

### Otázka (Front)

Jak řídit produkční lifecycle embeddingů: volbu modelu, dimenzi, náklady, verze a migrace?

### Odpověď (Back)

Produkční volba není jen benchmark kvality. Sleduj velikost modelu, dimenzi vektoru, latenci, compute pro offline/online embedding, storage/index, query serving a náklady na caching či rescoring. Vyšší dimenze a větší model mohou zachovat jemnější význam, ale zvyšují cenu; Matryoshka nebo kvantizace mohou kompromis zmírnit. Ověř **distribution shift** mezi tréninkovými a reálnými daty a podle potřeby fine-tunuj. Při upgradu se geometrie změní, takže staré a nové vektory nejsou kompatibilní. Udržuj model/version metadata, automatizovaný refresh a purge a možnost rollbacku. Migrační strategie: 

1. full re-embed + reindex — čisté, ale drahé;
2. dual index — paralelní A/B test a postupný rollout;
3. postupný refresh hot položek — levnější, ale dočasně nekonzistentní.

## Poznámka Anki 1783852352404

Karty Anki: 1783852352405
GUID: 0d6ea12554; štítky: AI_whitepapers B6_015 konsolidace.

### Otázka (Front)

Jak se liší tradiční RAG a agentic RAG a co máš optimalizovat dříve, než přidáš agentní orchestraci?

### Odpověď (Back)

**Tradiční RAG** obvykle jednorázově retrievuje několik chunků z jednoho indexu a předá je modelu. To často nestačí pro nejasné, multi-step nebo multi-perspective dotazy. **Agentic RAG** přidává retrieval agenta, který dotaz dekomponuje, iterativně jej rozšiřuje a zpřesňuje, provádí více searchů, dynamicky volí zdroje, filtruje a rerankuje výsledky a pomocí evaluatorů ověřuje rozpory či nedostatečné důkazy před finální syntézou. Tím může zlepšit accuracy, explainability a adaptabilitu, zejména v právu, vědě, business intelligence a rychle se měnících doménách. Agent ale neopraví špatný základ: nejprve maximalizuj **retrieval recall**, kvalitně parsuj a chunkuj podle struktury a přidej metadata — klíčová slova, synonyma, autora, datum, tagy a kategorie — pro boost, bury a filtering. RAG stále neodstraňuje halucinace; chraň oprávnění, měř relevanci a faithfulness, uváděj citace a při nedostatku podkladů odpověď raději odmítni.

## Poznámka Anki 1783852352406

Karty Anki: 1783852352407
GUID: a45a268e52; štítky: AI_whitepapers B6_016 konsolidace.

### Otázka (Front)

Jak funguje dvoufázová retrieval/ranking pipeline s candidate generation a rerankingem?

### Odpověď (Back)

Moderní search a recommender systémy oddělují rychlost a přesnost: 

1. **Candidate retrieval:** embeddingy + ANN rychle zúží miliony až miliardy položek na malou množinu s vysokým recallem.
2. **Reranking:** dražší a přesnější model znovu seřadí desítky či stovky kandidátů s využitím více features nebo cross-interakcí.
První fáze musí být velmi rychlá a nesmí zahodit dobré kandidáty; druhá optimalizuje pořadí viditelné uživateli. Tato architektura umožňuje škálovat ranking, protože komplexní model se nepouští nad celým korpusem.

