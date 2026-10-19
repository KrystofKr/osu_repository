# LLMs whitepapers – Původní blok 05

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::2 LLMs whitepapers
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783852352358

Karty Anki: 1783852352359
GUID: a051024532; štítky: AI_whitepapers B5_001 konsolidace.

### Otázka (Front)

Jak má vypadat systematický prompt-engineering workflow od zadání po produkční prompt?

### Odpověď (Back)

**Prompt** je vstupní sekvence, z níž LLM autoregresivně vytváří odpověď; lze jím řídit sumarizaci, extrakci, Q&A, klasifikaci, překlad, práci s kódem i další úlohy. **Prompt engineering** je iterativní proces, ne jednorázové „hezky napsané zadání“: 

1. jasně definuj úkol, publikum, požadovaný obsah, délku, styl a formát;
2. piš jednoduše a odstraň nerelevantní šum;
3. používej proměnné/placeholders pro opakovatelné šablony;
4. experimentuj s formulací, strukturou vstupu, stylem, modelem a konfigurací generování;
5. měř výstupy na reprezentativních případech a porovnávej varianty;
6. veď verzovaný prompt log včetně modelu, sampling parametrů a výsledků;
7. po aktualizaci modelu prompty znovu ověř a uprav.
Nedostatečný nebo ambivalentní prompt vede k nepřesným, generickým či nerelevantním odpovědím. Výsledek je model-specific, protože modely se liší daty, instruction tuningem a implementací. Nástroje typu Vertex AI Studio pomáhají ukládat, testovat a dokumentovat varianty; paralelní práce více prompt engineerů může rychleji najít lepší řešení.

## Poznámka Anki 1783852352360

Karty Anki: 1783852352361
GUID: b257815eb8; štítky: AI_whitepapers B5_002 konsolidace.

### Otázka (Front)

Jak řídit délku a ukončení generování a jak předcházet repetition loops?

### Odpověď (Back)

- **Output configuration** zahrnuje zejména maximální počet tokenů a sampling parametry. Vyšší limit znamená více výpočtu, energie, latence a ceny.
- **Max tokens není instrukce ke stručnosti:** nízký limit pouze výstup uřízne. Pro krátkou odpověď je nutné současně explicitně zadat stručnost a formát.
- Limit je důležitý u agentních/ReAct smyček, které mohou pokračovat i po nalezení odpovědi, a u kódu či strukturovaného výstupu, kde truncation může zanechat neúplný artefakt.
- **Repetition loop** je cyklické opakování slov, frází nebo kroků až do vyčerpání okna. Může vzniknout při příliš nízké teplotě kvůli rigidní nejpravděpodobnější trajektorii i při příliš vysoké teplotě kvůli chaotickému návratu do předchozího stavu.
- Mitigace: společně ladit temperature/top-K/top-P, omezit délku, přesně definovat stop podmínku a testovat na reálných vstupech.

## Poznámka Anki 1783852352362

Karty Anki: 1783852352363
GUID: 0e5c277c4b; štítky: AI_whitepapers B5_003 konsolidace.

### Otázka (Front)

Jak se liší system, contextual a role/style prompting a jak je skládat?

### Odpověď (Back)

- **System prompt** stanovuje globální účel, chování, mantinely a formát, například „vrať pouze label velkými písmeny“ nebo „vrať validní JSON“. Jasné pravidlo může potlačit nadbytečný text i při kreativnějším samplingu.
- **Contextual prompt** přidává dynamické informace pro konkrétní úlohu: situaci, publikum, médium, lokální fakta, definice, rozsah či doménová omezení. Snižuje nejednoznačnost a nutnost, aby model hádal záměr.
- **Role prompt** určuje perspektivu a kompetenční rámec, například editor, učitel nebo travel guide; **style/tone** určuje způsob podání, například formální, přímý, humorný, přesvědčivý či inspirační. Změna role mění prioritizované detaily a terminologii, změna stylu hlavně způsob vyjádření.
Tyto vrstvy se mohou kombinovat a v praxi se překrývají. **Instruction** pozitivně říká, co má model vytvořit; **constraint** vymezuje hranice nebo zákazy. Preferuj konkrétní instrukce o obsahu, délce, struktuře a stylu a omezení používej jako doplněk, protože samotné zákazy modelu neukazují cílový výstup.

## Poznámka Anki 1783852352364

Karty Anki: 1783852352365
GUID: 192b55357f; štítky: AI_whitepapers B5_004 konsolidace.

### Otázka (Front)

Jak navrhovat strukturovaný vstup a výstup pomocí JSON a schémat?

### Odpověď (Back)

Pro extrakci, parsování, klasifikaci, ranking či katalogová data je často vhodný **strukturovaný výstup** (JSON/XML): je konzistentní, strojově parsovatelný, soustředí model na požadovaná pole, zachovává datové typy a vztahy a může omezit volné domýšlení. **JSON Schema** funguje jako blueprint názvů polí, typů, povolených hodnot, vztahů a časových formátů; například pro e-commerce popis produktu může definovat `name`, `category`, `price`, `features` a `release_date`. U structured input je lepší data předzpracovat a dodat schéma plus relevantní atributy než celý volný dokument. Nevýhody JSON: je tokenově verbose, zvyšuje čas a cenu a při truncation může být syntakticky nevalidní kvůli chybějícím závorkám. Proto nastav dostatečný output limit, validuj výstup a případně použij opravný nástroj, například knihovnu `json-repair`; oprava však nenahrazuje kontrolu věcné správnosti.

## Poznámka Anki 1783852352366

Karty Anki: 1783852352367
GUID: bca7816f2b; štítky: AI_whitepapers B5_005 konsolidace.

### Otázka (Front)

Co je step-back prompting, jaká je jeho šablona a kdy pomáhá?

### Odpověď (Back)

**Step-back prompting** je dvoukrokový postup: 

1. polož obecnější otázku, která vyvolá relevantní principy, heuristiky nebo stavební kameny;
2. předej tuto obecnou odpověď jako explicitní kontext do promptu pro konkrétní problém.
Abstrakce aktivuje širší background knowledge, omezuje ad-hoc rozhodování a může zlepšit přesnost, nápaditost i odolnost vůči některým biasům. Na rozdíl od běžného contextual promptingu není kontext dodán rovnou člověkem, ale nejprve jej vytvoří model. Whitepaper ilustruje postup tvorbou FPS storyline: přímý prompt při temperature 1 byl kreativní, ale náhodný a generický; step-back nejprve vyžádal pět atraktivních settingů, jeden (např. podmořskou výzkumnou stanici) pak použil pro finální příběh, který byl konkrétnější a lépe ukotvený.

## Poznámka Anki 1783852352368

Karty Anki: 1783852352369
GUID: c8950760d1; štítky: AI_whitepapers B5_006 konsolidace.

### Otázka (Front)

Jak funguje Chain-of-Thought prompting a jak ho použít prakticky?

### Odpověď (Back)

**Chain-of-Thought (CoT)** žádá model, aby před finální odpovědí vytvořil mezikroky a rozložil problém. 

- **Zero-shot CoT:** pouze instrukce typu „uvažuj krok za krokem“.
- **One/few-shot CoT:** prompt nejprve ukáže jednu či více vyřešených úloh ve formátu otázka → kroky → výsledek; u složitých úloh bývá spolehlivější než zero-shot.
- Hodí se pro problémy, které lze „odvyprávět“ po krocích: matematiku a logiku, plánování kódu nebo konzistentní generování syntetických dat.
- Přínosy podle whitepaperu: nízké implementační náklady bez fine-tuningu, vyšší přesnost, viditelné místo chyby a někdy větší robustnost mezi verzemi modelu.
Finální odpověď má následovat až po odvození, protože mezikroky mění kontext pro její predikci. Pro úlohy s jediným správným výsledkem whitepaper doporučuje nízkou teplotu, typicky 0. Základní CoT však sleduje jen jednu lineární trajektorii a může uvíznout v chybném postupu.

## Poznámka Anki 1783852352370

Karty Anki: 1783852352371
GUID: 74d48510ca; štítky: AI_whitepapers B5_007 konsolidace.

### Otázka (Front)

Co je self-consistency a jak rozšiřuje Chain-of-Thought?

### Odpověď (Back)

**Self-consistency** místo jediné greedy reasoning cesty nasampluje několik různých CoT trajektorií a jejich finální odpovědi agreguje majority vote nebo jiným měřítkem konzistence. Tím zvyšuje šanci, že se překoná chybná jednotlivá cesta a vybere se výsledek podporovaný více nezávislými odvozeními. Aby šla metoda automatizovat a vyhodnocovat, musí být finální odpověď ve stabilním, samostatně extrahovatelném poli nebo formátu odděleném od reasoning textu.

## Poznámka Anki 1783852352372

Karty Anki: 1783852352373
GUID: 3ccd9e2459; štítky: AI_whitepapers B5_008 konsolidace.

### Otázka (Front)

Jaké úlohy pokrývá code prompting a čím se liší od multimodal promptingu?

### Odpověď (Back)

**Code prompting** používá textové zadání k psaní, vysvětlování, dokumentaci, překladu, debugování a review kódu. Whitepaper ukazuje například Bash skript pro hromadné přejmenování stovek souborů s prefixem „draft“; nízká temperature kolem 0,1 podporuje konzistentní nekreativní výstup. Studio prostředí navíc dovoluje řídit konfiguraci generování a pracovat v cloudovém účtu. I dobře vypadající kód je nutné přečíst, otestovat a bezpečnostně zkontrolovat; review má hledat chyby, validaci vstupů, error handling, bezpečnou práci se soubory, robustnost a čitelnost. **Multimodal prompting** naproti tomu kombinuje více vstupních modalit, například text, obraz, audio a kód. Samotné promptování modelu, aby napsal kód, zůstává textovým promptingem, není automaticky multimodální.

## Poznámka Anki 1783852352374

Karty Anki: 1783852352375
GUID: cf6820fb3d; štítky: AI_whitepapers B5_009 konsolidace.

### Otázka (Front)

Jaký je obsahový rámec a zdrojová základna whitepaperu o prompt engineeringu?

### Odpověď (Back)

Whitepaper shrnuje zero-/one-/few-shot, system, role a contextual prompting, step-back, Chain-of-Thought, self-consistency, Tree-of-Thoughts a ReAct; vedle ručního ladění zmiňuje i **Automatic Prompt Engineering (APE)**, problémy nedostatečných promptů a praktické best practices. Endnotes propojují dvě skupiny primárních zdrojů: 

- oficiální dokumentaci Google/Google Cloud k Gemini, Vertex AI, modelům a sampling parametrům, včetně top-K/top-P;
- akademické práce, typicky arXiv, ke CoT, self-consistency, ToT, ReAct a APE.
Jejich praktický účel je umožnit ověření definic a implementačních detailů v původní dokumentaci a výzkumu, nikoli spoléhat jen na sekundární shrnutí.

