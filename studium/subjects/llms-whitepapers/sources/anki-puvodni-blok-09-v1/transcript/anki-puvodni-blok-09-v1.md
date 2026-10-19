# LLMs whitepapers – Původní blok 09

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::2 LLMs whitepapers
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783852352452

Karty Anki: 1783852352453
GUID: 73c826e4c8; štítky: AI_whitepapers B9_001 konsolidace.

### Otázka (Front)

Proč nestačí general-purpose LLM pro složité doménové problémy a jaký obecný návrhový vzor ukazují SecLM a MedLM?

### Odpověď (Back)

Domény mají vlastní terminologii, citlivá či proprietární data, rychle se měnící znalosti, specifická rizika a úlohy, které nelze spolehlivě vyřešit samotným obecným modelem. Úspěšný vzor je **doménově přizpůsobený model + podpůrná infrastruktura**: autoritativní data a RAG pro grounding a aktuálnost, specializované deriváty modelu, plánování, nástroje a bezpečné napojení na reálné systémy. Whitepaper to ukazuje na **SecLM** pro kyberbezpečnost a **MedLM** pro zdravotnictví. Vertikální nebo aplikačně specifické modely mohou dosahovat lepších výsledků, ale technologie sama nestačí: rozhodující jsou lidská expertíza, pečlivá implementace, doménová spolupráce a víceúrovňová evaluace. Citované práce o foundation modelech a používání GenAI threat aktéry připomínají, že příležitosti musí být posuzovány společně s riziky a reálným kontextem.

## Poznámka Anki 1783852352454

Karty Anki: 1783852352455
GUID: 0116d08891; štítky: AI_whitepapers B9_002 konsolidace.

### Otázka (Front)

Jaké zvláštní výzvy má kyberbezpečnost a jaké požadavky z nich plynou pro security LLM platformu?

### Odpověď (Back)

Security kombinuje čtyři těžkosti: málo veřejných dat kvůli citlivosti, velkou šíři technických konceptů, hrozby měnící se téměř denně a abuse scénáře jako malware či phishing. Prakticky se to shrnuje jako **3T**: **Threats** (rychle se vyvíjející útoky), **Toil** (repetitivní triage a vyšetřování) a **Talent** (nedostatek zkušených lidí). Platforma proto musí poskytovat: 

- **freshness** bez každodenního retrainingu, typicky přes retrieval z aktuálních autoritativních zdrojů;
- práci s **uživatelskými daty** v jejich prostředí bez úniku a bez centralizovaného tréninku na customer datech;
- **security expertise** — znalost terminologie a rozklad abstraktních konceptů na akční kroky;
- syntézu heterogenních sil: logů, threat intelligence, pravidel, konfigurací a reportů;
- **kompartmentalizaci proprietárních dat** do konkrétních taskových schopností, aby se citlivé znalosti nešířily do obecného core modelu.

## Poznámka Anki 1783852352456

Karty Anki: 1783852352457
GUID: 55d706074d; štítky: AI_whitepapers B9_003 konsolidace.

### Otázka (Front)

Jak je navržena SecLM platforma a co v jejím případě znamená „one-stop API“?

### Odpověď (Back)

SecLM je API platforma, nikoli samotný model. Má tři vrstvy: **autoritatívní datastores** s threat intelligence a operational expertise; **security-specialized model API** s dalšími ML modely, RAG, plánováním a reasoningem; a **existující security tools**, které znají lokální kontext a umějí provádět lookupy či akce. Uživatel položí zero-shot dotaz přirozeným jazykem a planner jej rozloží, vybere vhodné zdroje, specializované modely, nástroje nebo agenty a agreguje výsledek. Plán může být statický od expertů nebo vytvořen dynamicky s expert guidance; platforma může používat také tool execution a dlouhodobou paměť preferencí. **RAG** zajišťuje aktuálnost a grounding, nástroje přístup k reálným systémům a plánování koordinaci více kroků. „One-stop“ tedy znamená, že API skrývá tuto orchestraci — ne že jeden nekontextový LLM vždy poskytne bezpečně správnou odpověď. V security je přesnost kritická, proto musí systém spojovat modely, data, nástroje a lidskou expertízu.

## Poznámka Anki 1783852352458

Karty Anki: 1783852352459
GUID: d799d37367; štítky: AI_whitepapers B9_004 konsolidace.

### Otázka (Front)

Jak SecLM řeší multi-step security úlohu na příkladech APT41 a obfuskovaného PowerShellu?

### Odpověď (Back)

U otázky „Jaké jsou TTP APT41 a jsou přítomné v mém prostředí?“ planner provede řetězec: **(1)** retrievuje nejnovější threat intelligence, **(2)** extrahuje a syntetizuje TTP a indikátory, **(3)** specializovaný — často parameter-efficient fine-tuned — model je přeloží do správné syntaxe a schématu SIEM, **(4)** dotazy spustí nad uživatelským prostředím a výsledky agreguje. Plán může být předem sestaven experty nebo vznikat dynamicky. Automatizace může analytikovi ušetřit hodiny mechanické práce, zatímco interpretace a rozhodnutí zůstávají na něm. U obfuskovaného PowerShellu platforma kombinuje nástroj, například base64 decoder, se SecLM: skript deobfuskuje, vysvětlí jeho kroky a klasifikuje škodlivost. Oba příklady ukazují, že hodnotu přináší **model + tool use + orchestrace**, ne samotné generování textu.

## Poznámka Anki 1783852352460

Karty Anki: 1783852352461
GUID: b64ed5d064; štítky: AI_whitepapers B9_005 konsolidace.

### Otázka (Front)

Jaké hlavní praktické security use-cases může doménová GenAI platforma pokrýt?

### Odpověď (Back)

- **Security analytik:** překlad přirozeného jazyka do event query language a pravidel; autonomní triage přes investigation → grouping/clustering → classification; case-specific plán remediace.
- **Threat researcher / administrátor:** reverse engineering, deobfuskace či dekompilace neznámého artefaktu a následné vysvětlení a klasifikace.
- **CISO tým:** organizaci přizpůsobený report nebo slide deck spojující aktuální threat intelligence s interními nálezy.
- **IT a identity týmy:** hledání attack paths k citlivým zdrojům, návrhy remediace a úprava access policies podle historických patternů směrem k least privilege.
- **Vývojáři:** určení vhodných míst pro fuzz testing a generování fuzz testů.
Společný princip je využít kontext konkrétní organizace a nástroje, ne pouze poskytovat obecnou radu.

## Poznámka Anki 1783852352462

Karty Anki: 1783852352463
GUID: 9ad901a622; štítky: AI_whitepapers B9_006 konsolidace.

### Otázka (Front)

Jak se má evaluovat SecLM a co znamenají classification metrics, ROUGE, BLEU, BERTScore a preference win rate?

### Odpověď (Back)

Security úlohy jsou heterogenní, proto jedna metrika nestačí. 

- Pro klasifikaci, například malware classification, použij standardní **classification metrics**.
- Pro generativní výstupy lze porovnat golden odpovědi: **ROUGE** měří zejména n-gram overlap používaný u sumarizace; **BLEU** vychází z n-gram precision vůči referenci; **BERTScore** porovnává kontextové embeddingy a zachytí více semantické podobnosti než čistý doslovný overlap.
- Dále použij automatické **side-by-side preference** s odděleným hodnotícím LLM a **human expert** hodnocení přes Likert škály či párové porovnání.
Metody je nutné kombinovat, protože mezi kategoriemi existují trade-offy a vysoká přesnost je kritická. „Platform preference win rate“ přibližně 53–79 % znamená, že experti ve srovnání častěji preferovali SecLM než general LLM; není to absolutní míra pravdivosti ani záruka výkonu mimo testované úlohy.

## Poznámka Anki 1783852352464

Karty Anki: 1783852352465
GUID: 1393304463; štítky: AI_whitepapers B9_007 konsolidace.

### Otázka (Front)

Co je MedLM a jaká ponaučení dává healthcare část pro vývoj a evaluaci doménových LLM?

### Odpověď (Back)

**MedLM** navazuje na Med-PaLM, který ukázal expert-level výkon v medicínském question answering, a má zpřístupňovat znalosti v prostředí s rychle rostoucím množstvím a komplexitou zdravotních dat. Samotný benchmark však nestačí: zdravotnické nasazení vyžaduje úzkou spolupráci s klinickou komunitou, pečlivou vícefázovou evaluaci a testování ve skutečném workflow. MedQA ilustruje rozsáhlé QA datasety z medicínských zkoušek, ale každá další úloha — například hodnocení psychiatrického fungování — potřebuje vlastní validaci. Medicína je inherentně **multimodální**; citované směry kombinují text s obrazovými či dalšími zdravotními daty, včetně X-ray systémů. Případ diabetické retinopatie zdůrazňuje human-centered evaluaci a redesign klinických postupů, nikoli jen přesnost modelu. Doménové LLM mohou pomáhat i mimo přímou péči, například při genetickém objevu. Základní výzkumné práce a projektová homepage slouží jako zdroje pro sledování vývoje, ne jako náhrada lokální klinické validace.

