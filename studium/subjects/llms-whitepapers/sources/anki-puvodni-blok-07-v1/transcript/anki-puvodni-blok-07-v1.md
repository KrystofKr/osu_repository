# LLMs whitepapers – Původní blok 07

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::2 LLMs whitepapers
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783852352408

Karty Anki: 1783852352409
GUID: 005073e2eb; štítky: AI_whitepapers B7_001 konsolidace.

### Otázka (Front)

Co je AI agent, z jakých komponent se skládá a jak se liší od samotného foundation modelu?

### Odpověď (Back)

**Agent** je aplikace navržená k dosažení cíle tím, že vnímá prostředí a strategicky v něm jedná. Používá jazykový model jako rozhodovací jádro, ale doplňuje jej o **orchestration layer** a **tools**. Samotný model obvykle provede jednu inferenci, má znalosti omezené tréninkovými daty a sám neudržuje dlouhodobý stav ani nevykonává externí akce. Agent naproti tomu spravuje historii a paměť, plánuje více kroků, volá API či datové zdroje, získává grounded aktuální informace a podle observations mění další postup. Jeden turn tvoří příchozí událost a jedna odpověď; více turnů vytváří session history. Model může být general-purpose, multimodální nebo fine-tuned a používání konkrétních nástrojů se řídí instrukcemi a in-context příklady. Praktická architektura stojí na trojici **model + nástroje + orchestrace**.

## Poznámka Anki 1783852352410

Karty Anki: 1783852352411
GUID: ad4f56bbf5; štítky: AI_whitepapers B7_002 konsolidace.

### Otázka (Front)

Jak orchestration layer řídí agentní smyčku a jakou roli v ní hrají ReAct, CoT a Tree-of-Thoughts?

### Odpověď (Back)

**Orchestration layer** udržuje stav, historii, paměť a plán a opakovaně řídí cyklus **Think → Act → Observe**: zavolá model, interpretuje jeho rozhodnutí, vykoná nástroj, vrátí výsledek do kontextu a rozhodne, zda pokračovat, přeplánovat nebo skončit. Je to podobné kuchaři, který zjistí objednávku a dostupné suroviny, naplánuje postup, vaří a podle průběžného výsledku plán upravuje. **ReAct** propojuje reasoning a acting ve struktuře Question → Thought → Action → Action input → Observation, která se může několikrát opakovat před Final answer. Action určuje nástroj a jeho vstup; Observation dodává výsledek akce pro další rozhodování a grounding. **CoT** vytváří jednu posloupnost mezikroků, zatímco **Tree-of-Thoughts** zkoumá více větví a strategický lookahead. Kvalita závisí nejen na modelu, ale i na řízení smyčky, nástrojích, zastavovacích podmínkách a zpracování chyb.

## Poznámka Anki 1783852352412

Karty Anki: 1783852352413
GUID: 204b93ec7f; štítky: AI_whitepapers B7_003 konsolidace.

### Otázka (Front)

Co jsou agentní tools, jak souvisejí s API a co rozhoduje o kvalitě jejich používání?

### Odpověď (Back)

**Tools** jsou rozhraní, přes která agent čte externí data nebo provádí akce — například vyhledává, pracuje s databází, kalendářem, e-mailem či smart-home službou. Často odpovídají operacím webových API typu GET, POST, PATCH a DELETE. Model obvykle neimplementuje službu; vybírá vhodný nástroj a vytváří jeho argumenty, zatímco orchestrace zajišťuje provedení a návrat výsledku. Kvalitu zásadně ovlivňuje definice nástroje: jednoznačný název a účel, přesné schéma argumentů, povinné parametry, příklady, omezení a srozumitelné chyby. Špatně popsané nebo překrývající se nástroje vedou k nesprávné volbě a argumentům. Dobře navržené tools rozšiřují model z generátoru obsahu na systém schopný pracovat s aktuálním světem a vykonávat kontrolované operace.

## Poznámka Anki 1783852352414

Karty Anki: 1783852352415
GUID: c1b0ffb3dd; štítky: AI_whitepapers B7_004 konsolidace.

### Otázka (Front)

Co jsou Extensions a jak řeší agent-side přístup k API?

### Odpověď (Back)

**Extensions** jsou standardizovaná agent-side vrstva mezi agentem a API. Konfigurace popisuje endpointy, jejich účel, parametry a příklady, takže agent nemusí spoléhat na křehký ručně napsaný parser entit a může za běhu vybrat vhodnou extension. Příklady učí nejen kdy endpoint použít, ale také které argumenty jsou nutné a jak reagovat na chybějící údaje. Jeden agent může mít více extensions a každá může zpřístupnit více API endpointů. Whitepaper uvádí například Code Interpreter, který z přirozeného jazyka generuje a spouští Python, a možnost zkoušet dostupné extensions v nastavení aplikace Gemini. Extensions se hodí, když má agent přímo řídit API interakce a výsledky okamžitě využívat v dalších krocích.

## Poznámka Anki 1783852352416

Karty Anki: 1783852352417
GUID: d46c5f9878; štítky: AI_whitepapers B7_005 konsolidace.

### Otázka (Front)

Jak funguje function calling a kdy je vhodnější než agent-side Extensions?

### Odpověď (Back)

Při **function callingu** model funkci sám nespustí. Ze specifikace vybere název funkce a vrátí strukturovaný payload — typicky JSON s argumenty — který interpretuje klient, middleware nebo backend. Tok je: dotaz + definice/příklady → modelový `function_call` → client-side validace a provedení API → volitelný návrat výsledku modelu → sestavení odpovědi nebo UI. Tento přístup je vhodný, když přímému volání brání autentizace či bezpečnost, operace musí proběhnout v jiné vrstvě stacku, záleží na pořadí, batchování nebo human-in-the-loop, je třeba transformovat odpověď nebo rychle stubovat API. Vývojář má jemnou kontrolu nad tím, zda a kolik externích dat se vrátí do další reasoning smyčky. Příkladem je travel concierge, kde model pouze strukturuje města a preference a klient následně volá Places API.

## Poznámka Anki 1783852352418

Karty Anki: 1783852352419
GUID: 3256d516be; štítky: AI_whitepapers B7_006 konsolidace.

### Otázka (Front)

Jak se liší Extensions, Function Calling a Data Stores podle provedení, účelu a míry kontroly?

### Odpověď (Back)

- **Extensions:** agent-side provedení API; agent vybírá endpoint, volá jej a výsledek používá v další smyčce. Hodí se pro přímé akce a multi-hop workflow.
- **Function Calling:** model vrátí název a argumenty, ale provedení je client-side. Hodí se pro bezpečnostní, autentizační, infrastrukturní a pořadové požadavky a dává vývojáři největší kontrolu nad tokem dat.
- **Data Stores:** agent-side retrieval z předindexovaných webů, dokumentů či databází. Rozšiřují primárně znalosti pomocí RAG, zatímco Extensions a Functions rozšiřují hlavně schopnost provádět operace.
Volba tedy není jen technická: závisí na tom, zda agent potřebuje informaci, akci, nebo obojí, kde smí běžet citlivý kód a zda má výsledek automaticky vstupovat do dalšího rozhodování.

## Poznámka Anki 1783852352420

Karty Anki: 1783852352421
GUID: 6889a92e9a; štítky: AI_whitepapers B7_007 konsolidace.

### Otázka (Front)

Jak se agentní systém prototypuje a převádí do produkce a co znamenají multi-hop a multi-agent architektury?

### Odpověď (Back)

Agentní frameworky jako **LangChain/LangGraph** skládají model, stavovou logiku a nástroje do grafu či smyčky. Whitepaper demonstruje multi-hop dotaz, kde agent nejprve přes SerpAPI zjistí sportovního soupeře a teprve z tohoto výsledku vytvoří dotaz do Google Places na adresu stadionu; druhý krok tedy závisí na observation z prvního. Produkční systém potřebuje vedle promptu a tool definitions také UI, autentizaci, monitoring, evaluaci, debugging, bezpečnostní omezení a kontinuální zlepšování. Managed platforma může organizovat cíle, instrukce, příklady, nástroje, vector search a sub-agenty. Vývoj musí být iterativní, protože chování je generativní a konfigurace se liší podle úlohy. **Agent chaining** nebo **mixture of agent experts** rozděluje problém mezi specializované agenty; orchestrace pak musí řídit delegování, sdílení stavu, slučování výsledků a ukončení.

