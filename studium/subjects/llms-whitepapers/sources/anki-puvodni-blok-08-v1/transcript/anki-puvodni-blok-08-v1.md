# LLMs whitepapers – Původní blok 08

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::2 LLMs whitepapers
Rozsah: 15 poznámek, 15 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783852352422

Karty Anki: 1783852352423
GUID: b08e2fa866; štítky: AI_whitepapers B8_001 konsolidace.

### Otázka (Front)

Jak na sebe navazují DevOps, MLOps, FMOps, PromptOps, RAGOps a AgentOps a proč je AgentOps nutný pro přechod z POC do produkce?

### Odpověď (Back)

- **DevOps** productionizuje převážně deterministický software pomocí version control, CI/CD, testů, logování, bezpečnosti a škálování.
- **MLOps** přidává nedeterministické modely a silnou závislost na kvalitě a driftu dat.
- **FMOps** řeší životní cyklus foundation modelů — pre-training i customization/fine-tuning.
- **PromptOps** spravuje prompt templates, registry, metadata, lineage, eval skóre a optimalizaci promptů.
- **RAGOps** operationalizuje cleaning, chunking, embeddingy, retrieval, reranking, augmentaci promptu a grounding.
- **AgentOps** nad tím přidává správu nástrojů, „agent brain“ prompt s cílem/profilem/instrukcemi, orchestraci, paměť a dekompozici úloh.
AgentOps předchozí vrstvy nenahrazuje: agenti stále potřebují CI/CD, testy, quotas, privacy, security, logging a scale. Demo lze postavit rychle, ale hlavní bariérou produkce je stabilní **kvalita a spolehlivost**; Agent Builder a AgentOps jsou most od POC k měřitelnému, opakovatelnému provozu.

## Poznámka Anki 1783852352424

Karty Anki: 1783852352425
GUID: 37086f7c8e; štítky: AI_whitepapers B8_002 konsolidace.

### Otázka (Front)

Jaká je minimální produkční observabilita agentního systému?

### Odpověď (Back)

Začni **business north-star metrikou** (např. revenue nebo engagement) a pod ní měř **goal completion rate**. Pokud se cíl skládá z více kroků, instrumentuj kritické tasky a user interactions samostatně. Přidej standardní telemetry — hlavně latenci, chyby, dostupnost a náklady — a jednoduchý kontextový human feedback, například 👍/👎 nebo krátký formulář od uživatelů, QA či expertů. Uchovávej **traces** všech důležitých interních kroků a tool calls; nemusíš každý krok převést na KPI, ale trace je zásadní pro debugging, když metriky nebo manuální testy odhalí problém. U agentů je observabilita důležitější než u deterministického kódu, protože mohou volit širší spektrum akcí a jejich chování není plně předvídatelné.

## Poznámka Anki 1783852352426

Karty Anki: 1783852352427
GUID: 6fc9719b3f; štítky: AI_whitepapers B8_003 konsolidace.

### Otázka (Front)

Jaké tři vrstvy má evaluace agentů a jakou roli mají veřejné benchmarky?

### Odpověď (Back)

Evaluace agentů musí pokrýt: **(1) schopnosti agenta**, například porozumění instrukcím, reasoning, planning a tool calling; **(2) trajektorii a použití nástrojů**, tedy jak agent postupoval; a **(3) finální odpověď**, tedy zda skutečně splnil cíl. Veřejné benchmarky a technical reports dávají před vlastním testováním orientační obraz limitů a failure modes: například **BFCL** a **τ-bench** pro function/tool calling, **PlanBench** pro planning a **AgentBench** pro holističtější scénáře. Benchmark ale není náhradou za use-case eval: musíš rozumět jeho metodice, pokrytým schopnostem a tomu, zda odpovídá reálným úlohám tvého agenta.

## Poznámka Anki 1783852352428

Karty Anki: 1783852352429
GUID: 1f72d6b4a9; štítky: AI_whitepapers B8_004 konsolidace.

### Otázka (Front)

Jak se hodnotí trajektorie agenta a co znamenají exact match, in-order, any-order, precision, recall a single-tool use?

### Odpověď (Back)

**Trajektorie** je sekvence interních kroků před odpovědí — například disambiguace, retrieval, volání API a další tool calls. Porovnání očekávané a skutečné trajektorie pomáhá lokalizovat chyby a neefektivitu. Ground-truth metriky jsou: 

- **Exact match:** celá sekvence musí být totožná.
- **In-order match:** povinné kroky jsou ve správném pořadí, extra kroky jsou tolerovány.
- **Any-order match:** všechny nutné kroky se objeví, pořadí nehraje roli.
- **Precision:** podíl predikovaných tool calls, které jsou relevantní.
- **Recall:** podíl povinných referenčních tool calls, které agent provedl.
- **Single-tool use:** zda se konkrétní nástroj vůbec objevil.
Rigidita musí odpovídat úloze; často neexistuje jediná správná cesta. Automatizované evaly vyžadují kurátorovaný dataset reprezentující reálné situace a bez ground truth lze použít autoratery. Trajektorie hodnotí jak agent pracoval, finální odpověď co dodal — obě perspektivy se doplňují.

## Poznámka Anki 1783852352430

Karty Anki: 1783852352431
GUID: 8b8b91d7c9; štítky: AI_whitepapers B8_005 konsolidace.

### Otázka (Front)

Jak hodnotit finální odpověď agenta pomocí LLM-as-a-Judge a human-in-the-loop a jaké jsou jejich limity?

### Odpověď (Back)

Finální odpověď hodnotíš proti explicitním success kritériím: splnění cíle, správnost, relevance, úplnost, bezpečnost a případně styl. **LLM-as-a-Judge** dostane vstup, odpověď a přesně formulovanou rubriku; vágní kritéria znamenají nespolehlivé skóre a knihovní rubriky je nutné přizpůsobit use case. **Human-in-the-loop** je zásadní pro subjektivitu, kreativitu, common sense, širší kontext a kalibraci automatických hodnotitelů. Lze použít přímé skórování experty, párové porovnání verzí nebo user studies. Slabiny: lidé jsou drazí, subjektivní a špatně škálují; LLM judge může preferovat outcome a přehlédnout reasoning; jednoduché metriky lze „gamingovat“ a nemusí pokrýt plné schopnosti. Obtížná jsou také chybějící eval data, syntetické datasety, multimodální výstupy a dynamické prostředí. Trend směřuje k process-based evaluaci, AI-assisted škálování, standardizovaným benchmarkům a větší explainability.

## Poznámka Anki 1783852352432

Karty Anki: 1783852352433
GUID: db8787de6a; štítky: AI_whitepapers B8_006 konsolidace.

### Otázka (Front)

Co je multi-agent systém, proč se používá a jaké základní role v něm agenti mívají?

### Odpověď (Back)

**Multi-agent systém** je tým autonomních, specializovaných agentů — případně s různými LLM — kteří si dělí úkol, komunikují a skládají společný výsledek. Oproti jednomu univerzálnímu agentovi přináší modularitu, spolupráci a často hierarchii. Výhody mohou být: vyšší přesnost díky cross-checku, nižší latence díky paralelní práci, snazší rozklad složitých úloh, škálování přidáním specialistů, fault tolerance a omezení jednostranných halucinací či biasu. Tyto přínosy nejsou automatické a závisejí na kvalitě orchestrace. Typické role jsou **planner** (rozklad cíle a plán), **retriever** (získání znalostí), **executor** (výpočty, tvorba výstupů a API akce) a **evaluator** (kontrola koherence, cíle, rozporů a halucinací). Role, validace a adaptivní workflow přesahují prosté promptování jednoho modelu.

## Poznámka Anki 1783852352434

Karty Anki: 1783852352435
GUID: 7d835d27d1; štítky: AI_whitepapers B8_007 konsolidace.

### Otázka (Front)

Jaké jsou hlavní multi-agentní design patterns a podle čeho se mezi nimi vybírá?

### Odpověď (Back)

- **Sequential:** výstup jednoho specialisty vstupuje do dalšího; podobá se montážní lince.
- **Hierarchical:** manager plánuje, routuje a deleguje workerům; podobá se týmu s vedoucím.
- **Collaborative:** peer agenti sdílejí informace a společně skládají řešení.
- **Competitive:** více agentů navrhuje nebo optimalizuje kandidáty a systém vybere nejlepší; soutěž může být spojena s koordinací.
Pattern vol podle závislostí mezi kroky, požadovaného paralelismu, potřeby centrální kontroly, množství komunikace a možnosti nezávislé validace. Správně zvolený pattern může omezit provozní bottlenecky, zlepšit retrieval a spolehlivost automatizace; špatně zvolený přidá jen režii a latenci.

## Poznámka Anki 1783852352436

Karty Anki: 1783852352437
GUID: d2b9db3202; štítky: AI_whitepapers B8_008 konsolidace.

### Otázka (Front)

Jaké runtime komponenty potřebuje škálovatelný multi-agent systém a jaké jsou jeho hlavní provozní výzvy?

### Odpověď (Back)

Runtime typicky zahrnuje: **interaction wrapper** pro komunikaci s prostředím a různé modality; short-term context, sessions a cache; long-term paměť pro epizody, preference, skills a reference data; **reflection**, která rozhoduje, co zapsat dlouhodobě; reasoning/planner subsystém pro dekompozici, self-correction a upřesnění záměru; tool integration s dynamickým registry a případně Tool RAG; routing a neighbor discovery; a strukturovaný **A2A protokol**. U vzdálených agentů musí komunikace podporovat durable asynchronous tasks, notifikace a návrat uživatele do sezení. Při větším počtu agentů a nástrojů je nutný registry/mesh s ontologií capabilities, requirements a performance metrikami. Hlavní problémy jsou message-based místo task-based komunikace, rozdělení úloh, feedback loops, koordinované reasoning, správa kontextu, vyšší čas a náklady a komplexita podobná distribuovaným mikroslužbám.

## Poznámka Anki 1783852352438

Karty Anki: 1783852352439
GUID: 782748b7f9; štítky: AI_whitepapers B8_009 konsolidace.

### Otázka (Front)

Jak se evaluuje multi-agent systém nad rámec evaluace jednoho agenta?

### Odpověď (Back)

North-star business metriky, goal completion, úspěch kritických tasků, latence, chyby a traces zůstávají stejné. Stále hodnotíš **trajektorii** i jednu výslednou odpověď, ale trajektorie nyní zahrnuje více agentů a je důležité provést drill-down na jednotlivé delegace a kroky. Navíc testuj čtyři specifické oblasti: **(1) cooperation & coordination** — zda agenti účelně spolupracují; **(2) planning & task assignment** — zda vznikl dobrý plán, úkol dostal správný specialista a child agent neodbočil do slepé uličky; **(3) agent utilization** — kdy má být agent použit jako tool, background worker nebo handoff pro uživatele; **(4) scalability** — zda přidání agentů skutečně zvyšuje kvalitu či snižuje latenci a náklady, místo aby systém zhoršilo.

## Poznámka Anki 1783852352440

Karty Anki: 1783852352441
GUID: 6d5b64c9a2; štítky: AI_whitepapers B8_010 konsolidace.

### Otázka (Front)

Jak se liší enterprise knowledge asistenti Agentspace a NotebookLM a jaké schopnosti vyžadují?

### Odpověď (Back)

Enterprise agenti řeší vyhledávání, agregaci a akce napříč mnoha interními systémy; „manager of agents“ routuje specialisty, priority a workflow a udržuje konzistentní UX, governance a SLA. **Agentspace** je organizací řízený multimodální search/answering agent nad strukturovanými i nestrukturovanými daty. Potřebuje předpřipravené konektory, průběžný refresh, překlady, blended RAG, semantic search, knowledge graphs a personalizaci podle role, oprávnění a historie. Enterprise trust zahrnuje SSO, permissions model, user-level access control, RBAC, IAM, VPC Service Controls, vysvětlitelnost a governance; systém musí škálovat přes regiony, jazyky a špičky. **NotebookLM** je uživatelem kurátorovaný research workspace nad nahranými zdroji: extrahuje koncepty, shrnuje, odpovídá a hledá vztahy mezi dokumenty; Plus přidává kapacitu a pokročilejší analýzu, Enterprise bezpečnost/privacy a další formy syntézy včetně audio summaries. Zásadní rozdíl je organizační federovaný přístup vs. konkrétní sada zdrojů v jednom výzkumném workspace.

## Poznámka Anki 1783852352442

Karty Anki: 1783852352443
GUID: 40bac75d7b; štítky: AI_whitepapers B8_011 konsolidace.

### Otázka (Front)

Co znamená paradigma „agent jako contractor“ a jak funguje kontrakt, jeho lifecycle, validace a subcontracts?

### Odpověď (Back)

Místo vágního promptu dostane agent-**contractor** formální kontrakt. Ten obsahuje popis projektu, **deliverables a jejich akceptační kritéria**, očekávané náklady, dobu trvání a reporting/feedback; volitelně scope a povolené input sources. Lifecycle je **Defining → Negotiating → Executing**. V negotiation se vyjasňuje underspecification, konfliktní požadavky, dodatečné vstupy, risk, cost a priority. Pojem cost umožňuje alokovat zdroje mezi konkurující kontrakty. Během execution se preferuje kvalita a úplnost nad minimální latencí: contractor může vytvořit více řešení, reviewovat a skórovat je a pomocí objektivních validators iterovat a self-correctovat, dokud nejsou kritéria splněna. Průběžný Contract Feedback zachycuje nejasnosti a změny. Složitý kontrakt lze dekomponovat na standardizované **subcontracts** v execution queue. Knowledge nástroje typu Agentspace/NotebookLM dodávají zdroje; contract model dodává přesnou odpovědnost, vyjednávání a ověřitelnost výsledku.

## Poznámka Anki 1783852352444

Karty Anki: 1783852352445
GUID: 0a83661787; štítky: AI_whitepapers B8_012 konsolidace.

### Otázka (Front)

Jak funguje multi-agentní systém AI Co-Scientist a co ukazuje jako obecný design pattern?

### Odpověď (Back)

Co-Scientist používá cyklus **generate → debate → evolve**: nejprve vytváří diverzní hypotézy, poté je kriticky porovnává a validuje a nakonec je iterativně zlepšuje podle feedbacku a nových důkazů. Více modelů či agentů může mít specializované role: data-processing agenti agregují a strukturují data, hypothesis generators navrhují vysvětlení, validation agents provádějí simulace či kontrolu a collaboration agents koordinují týmy. Příklad studie jaterní fibrózy ilustruje, že systém může nejen dohledat existující kandidáty, ale navrhnout nové mechanismy a slibné směry. Obecná lekce je kombinovat diverzitu návrhů, strukturovanou kritiku, validaci a iterativní evoluci místo jednorázové odpovědi jednoho modelu.

## Poznámka Anki 1783852352446

Karty Anki: 1783852352447
GUID: c73494e1ec; štítky: AI_whitepapers B8_013 konsolidace.

### Otázka (Front)

Jak vypadá základní automotive multi-agent architektura a jaké specialisty a orchestrace typicky obsahuje?

### Odpověď (Back)

Automotive assistant musí fungovat hands-free, s nízkou latencí, bezpečně a někdy bez konektivity, proto používá tým úzce zaměřených agentů. **Navigation agent** rozpozná intent, volá Maps/Places, rerankuje podle preferencí a předá navigační příkaz; **Media agent** hledá a ovládá obsah; **Message agent** bezpečně formuluje diktované zprávy; **Car Manual agent** odpovídá z dokumentace a interpretuje výstrahy; **General Knowledge agent** doplňuje obecná vysvětlení. V hierarchickém patternu centrální **Orchestrator** klasifikuje doménu a intent, routuje specialistu, udržuje multi-turn kontext a zajišťuje fallback. Tato specializace dovoluje optimalizovat každý subsystém podle jeho dat, rizik a integračních potřeb.

## Poznámka Anki 1783852352448

Karty Anki: 1783852352449
GUID: b469c0b383; štítky: AI_whitepapers B8_014 konsolidace.

### Otázka (Front)

Jaké koordinační patterns se hodí v automotive multi-agent systému a jaké failure modes řeší?

### Odpověď (Back)

- **Diamond:** odpověď specialisty prochází Rephraserem, který sjednotí tón, zkrátí ji, personalizuje a přizpůsobí bezpečnému in-car UX.
- **Peer-to-peer handoff:** omylem zvolený specialista předá dotaz správnému a opraví misrouting.
- **Collaborative:** více doménových agentů sdílí informace pro otázku vyžadující několik perspektiv.
- **Response Mixer / competitive best-of:** více agentů vytvoří kandidáty a mixer vybere přesné a relevantní části, odstraní chyby a složí jednu odpověď; hodí se pro více interpretací.
- **Adaptive Loop:** agent iterativně uvolňuje či mění kritéria, dokud nenajde užitečnou aproximaci — například vegan+Italian → širší varianty — a transparentně vysvětlí kompromis.
Hierarchie řeší routing, diamond prezentaci, peer-to-peer self-healing, collaboration multi-domain dotazy, mixer konkurující kandidáty a adaptive loop neúspěšný search místo prostého „no results“.

## Poznámka Anki 1783852352450

Karty Anki: 1783852352451
GUID: 901bf0927b; štítky: AI_whitepapers B8_015 konsolidace.

### Otázka (Front)

Jaké jsou hlavní deploymentové výhody automotive multi-agent architektury?

### Odpověď (Back)

Úzká specializace umožňuje hlubší doménovou kvalitu a efektivně přiřadit správný výpočetní prostředek správnému dotazu: jednoduché požadavky používají levný a rychlý agent, složité eskalují na silnější model nebo více specialistů. **On-device** agenti obsluhují kritické a latency-sensitive funkce, například ovládání vozidla, klima nebo základní média; **cloud** poskytuje širší znalosti a méně urgentní doporučení. Při ztrátě internetu tak základní schopnosti zůstanou funkční a pouze komfortní cloudové funkce degradují. Správný split zlepšuje bezpečnost, odezvu, cenu i resilience, ale vyžaduje jasné fallbacky a konzistentní stav mezi zařízeními a cloudem.

