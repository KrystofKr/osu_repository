# LLMs whitepapers – Původní blok 02

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::2 LLMs whitepapers
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783852352298

Karty Anki: 1783852352299
GUID: d99cb81b6d; štítky: AI_whitepapers B2_001 konsolidace.

### Otázka (Front)

Jak vypadá typická vícefázová cesta k užitečnému LLM modelu?

### Odpověď (Back)

1. **Pre-training:** model se na velmi velkém a různorodém nelabelovaném korpusu učí obecnou distribuci jazyka; decoder-only LLM typicky predikuje další token.
2. **Supervised fine-tuning / instruction tuning:** na menším, kvalitním a kurátorovaném datasetu instrukcí, demonstrací či cílových úloh se učí následovat zadání a požadovaný styl chování.
3. **Preference alignment:** následné metody jako RLHF nebo DPO posouvají chování směrem k lidským preferencím.
Fine-tuning je proti pre-trainingu levnější díky menšímu datasetu a počtu kroků a může měnit nejen výkon, ale také bezpečnost, toxicitu, konverzačnost a poslušnost instrukcím.

## Poznámka Anki 1783852352300

Karty Anki: 1783852352301
GUID: 083b40bbab; štítky: AI_whitepapers B2_002 konsolidace.

### Otázka (Front)

Jak se liší pretraining cíle decoder-only, encoder-only a encoder–decoder transformerů?

### Odpověď (Back)

- **Decoder-only:** autoregresivní next-token prediction; target je vstup posunutý o jeden token a model predikuje pokračování z prefixu.
- **Encoder-only:** rekonstrukce poškozeného vstupu, typicky Masked Language Modeling, kde se token odhaduje z levého i pravého kontextu.
- **Encoder–decoder:** mapování vstupní sekvence na cílovou sekvenci. Typické supervised seq2seq úlohy jsou překlad, sumarizace a otázka–odpověď; i nelabelované cíle lze převést do text-to-text podoby.

## Poznámka Anki 1783852352302

Karty Anki: 1783852352303
GUID: 554cff8003; štítky: AI_whitepapers B2_003 konsolidace.

### Otázka (Front)

Jak se liší SFT a RLHF a proč se obvykle používají za sebou?

### Odpověď (Back)

**SFT** učí model z kvalitních pozitivních demonstrací prompt–odpověď a vytváří základní instruction-following policy. **RLHF** pak využívá hodnocení či porovnání více výstupů, takže může posilovat preferované odpovědi a penalizovat nežádoucí. Cílem je posunout model k užitečnějším, pravdivějším, bezpečnějším a koherentnějším výstupům, nejen napodobit demonstrace.

## Poznámka Anki 1783852352304

Karty Anki: 1783852352305
GUID: b545a5dd62; štítky: AI_whitepapers B2_004 konsolidace.

### Otázka (Front)

Jak probíhá klasická RLHF pipeline a v jakých formách se sbírají preference?

### Odpověď (Back)

1. Po SFT model vygeneruje kandidátní odpovědi na prompty.
2. Hodnotitelé dodají preference: například **single-sided skóre**, **pairwise volbu** lepší odpovědi, binary good/bad, Likertovu škálu nebo pořadí více kandidátů.
3. Z těchto dat se natrénuje **reward model**, často inicializovaný z předtrénovaného či SFT transformeru.
4. Policy se dále optimalizuje RL algoritmem, typicky policy-gradient metodou jako PPO, aby zvyšovala odměnu a přitom se příliš nevzdálila výchozímu modelu.

## Poznámka Anki 1783852352306

Karty Anki: 1783852352307
GUID: bc7e1be68a; štítky: AI_whitepapers B2_005 konsolidace.

### Otázka (Front)

Jak se RLAIF a DPO liší od klasického RLHF?

### Odpověď (Back)

- **RLAIF** nahrazuje část lidského označování feedbackem generovaným AI, aby tvorba preferenčních dat lépe škálovala; následná optimalizace může stále používat reward model a RL.
- **DPO (Direct Preference Optimization)** učí policy přímo z dvojic preferovaná vs. odmítnutá odpověď. Dosahuje alignmentu bez samostatně trénovaného reward modelu a bez klasického PPO/RL kroku.

## Poznámka Anki 1783852352308

Karty Anki: 1783852352309
GUID: 5f6f2eb2f5; štítky: AI_whitepapers B2_006 konsolidace.

### Otázka (Front)

Jak funguje GRPO a čím se liší od PPO s critic/value modelem?

### Odpověď (Back)

Pro jeden prompt model vygeneruje **skupinu odpovědí**, každá dostane reward a její výhoda se určí relativně vůči průměru skupiny. Nadprůměrné výstupy se posilují a podprůměrné potlačují. Skupinová relativní baseline nahrazuje samostatný **critic/value model**, čímž snižuje výpočetní náklady a může stabilizovat trénink. „Self-play“ zde neznamená dva soupeřící agenty, ale porovnávání několika vlastních výstupů modelu. PPO naproti tomu typicky optimalizuje policy s reward signálem a naučeným value/critic odhadem.

## Poznámka Anki 1783852352310

Karty Anki: 1783852352311
GUID: e561d073a0; štítky: AI_whitepapers B2_007 konsolidace.

### Otázka (Front)

Co je PEFT a jak se liší adaptéry a soft prompting?

### Odpověď (Back)

**Parameter-Efficient Fine-Tuning** zmrazí většinu parametrů základního modelu a učí jen malou přídavnou část, například adaptéry, LoRA matice nebo soft prompty. 

- **Adapter-based fine-tuning:** do vrstev se vloží malé trénovatelné moduly a aktualizují se pouze jejich váhy.
- **Soft prompting:** optimalizují se naučené embeddingové vektory vložené jako prefix ke vstupu; na rozdíl od ručně psaného textového promptu nejsou lidsky čitelné.
Výsledkem jsou nižší paměťové a výpočetní náklady, rychlejší specializace a snadněji přenosné moduly; full fine-tuning však může u některých úloh dosáhnout vyššího maxima.

## Poznámka Anki 1783852352312

Karty Anki: 1783852352313
GUID: 88d076a19b; štítky: AI_whitepapers B2_008 konsolidace.

### Otázka (Front)

Jak fungují LoRA a QLoRA a proč jsou praktické při nasazení?

### Odpověď (Back)

**LoRA** ponechá původní váhovou matici zmrazenou a její změnu aproximuje součinem dvou malých low-rank matic. Trénuje se tedy jen zlomek parametrů. Malé LoRA moduly lze sdílet a přepínat mezi úlohami nad stejným base modelem. **QLoRA** navíc drží základní model v kvantizované podobě a trénuje LoRA adaptéry, čímž dále snižuje paměťové nároky.

## Poznámka Anki 1783852352314

Karty Anki: 1783852352315
GUID: 3233fbf034; štítky: AI_whitepapers B2_009 konsolidace.

### Otázka (Front)

Jak se trénuje, vyhodnocuje a doménově dolaďuje embedding model?

### Odpověď (Back)

Moderní embedding model se obvykle inicializuje z foundation modelu a dolaďuje tak, aby změnil **geometrii prostoru** pro cílovou úlohu. U retrievalu se často používá kontrastivní loss nad dvojicemi či trojicemi query–positive–negative: relevantní páry se přibližují, nerelevantní oddalují. **Hard negatives** jsou nerelevantní položky, které model zaměňuje s pozitivy; učí jemnější hranice relevance. Data mohou vzniknout lidským labelováním, syntetickou generací LLM, distilací nebo miningem. Evaluace potřebuje qrels/gold relevanci a metriky jako precision@k, recall@k či nDCG. Předtrénovaný model je baseline; fine-tuning či search adaptor pomáhá při doménovém rozdílu a distribution shiftu, ale musí být ověřen proti latenci a nákladům.
-------------------
 [Obrázek: paste-bbcd6c85585e551004d8c282099b641f3b464197.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1783852352316

Karty Anki: 1783852352317
GUID: 519387557f; štítky: AI_whitepapers B2_010 konsolidace.

### Otázka (Front)

Proč doménový LLM vyžaduje opatrnou specializaci a jaké trade-offy je nutné hlídat?

### Odpověď (Back)

General-purpose model může selhávat kvůli nedostatku veřejných doménových dat, neznalosti hlubokého a rychle se měnícího odborného jazyka nebo bezpečnostním omezením citlivých úloh. Větší model může nabídnout lepší reasoning, ale být nevhodný pro nízkolatenční a vysokoobjemové použití. Příliš úzký či špatně kurátorovaný fine-tuning zase může poškodit generalizaci na nové produkty, platformy a úlohy. Design proto vyvažuje doménový výkon, generalizaci, latenci, náklady a oddělení citlivých dat.

## Poznámka Anki 1783852352318

Karty Anki: 1783852352319
GUID: efd5406f72; štítky: AI_whitepapers B2_011 konsolidace.

### Otázka (Front)

Jak vypadá doménová adaptační pipeline SecLM a proč se používají specializované deriváty?

### Odpověď (Back)

1. Začít robustním, ideálně vícejazyčným **foundation modelem** znalým textu, kódu a strukturovaných dat.
2. Provést **continued pre-training** na otevřených či licencovaných security zdrojích, aby model získal doménový jazyk.
3. Provést **SFT** na konkrétních úlohách, například analýze škodlivých skriptů, vysvětlování příkazů a událostí, sumarizaci threat-intel reportů nebo generování SIEM dotazů.
4. Citlivé či proprietární znalosti podle potřeby oddělit do lehkých **PET derivátů** místo jejich vmíchání do core modelu; tím se chrání data a omezuje degradace obecné schopnosti.
Vícejazyčný základ je důležitý pro globální threat intelligence i uživatele.

## Poznámka Anki 1783852352320

Karty Anki: 1783852352321
GUID: 3599246d2c; štítky: AI_whitepapers B2_012 konsolidace.

### Otázka (Front)

Kdy po fine-tuningu použít ICL, RAG nebo PET?

### Odpověď (Back)

- **ICL:** když je potřeba rychle naučit model nový formát, platformu či query jazyk pomocí několika příkladů bez změny vah.
- **RAG:** když je klíčová čerstvá a autoritativní znalost; informace se doplní za běhu bez změny parametrů.
- **PET/PEFT adaptér:** když je třeba trvaleji přidat specializované chování nebo environment-specific znalost, často z citlivých dat, aniž by se přetrénoval celý core model.
Tyto mechanismy řeší jiné potřeby a mohou se kombinovat.

## Poznámka Anki 1783852352322

Karty Anki: 1783852352323
GUID: 399734f6e6; štítky: AI_whitepapers B2_013 konsolidace.

### Otázka (Front)

Jaké tři formy targeted learningu může agent využít a jaké mají trade-offy?

### Odpověď (Back)

- **In-context learning:** model při inference dostane instrukce, definice nástrojů a několik příkladů; učí se „za běhu“ bez změny vah.
- **Retrieval-based ICL:** relevantní informace, nástroje či demonstrace se dynamicky vybírají z externí paměti a vkládají do kontextu.
- **Fine-tuning-based learning:** model se před nasazením trénuje na specifickém datasetu a získá hlubší, trvalejší specializaci pro budoucí neviděné případy.
Přístupy se liší rychlostí změny, cenou, latencí a hloubkou specializace; produkční systém je může kombinovat.

