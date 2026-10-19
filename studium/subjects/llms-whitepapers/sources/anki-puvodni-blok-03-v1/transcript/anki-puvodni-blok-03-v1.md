# LLMs whitepapers – Původní blok 03

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::2 LLMs whitepapers
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783852352324

Karty Anki: 1783852352325
GUID: 69f382a6f7; štítky: AI_whitepapers B3_001 konsolidace.

### Otázka (Front)

Jak se liší training a inference transformeru a jak context length ovlivňuje jejich náklady?

### Odpověď (Back)

- **Training:** model počítá loss, backpropagací získává gradienty a aktualizuje parametry.
- **Inference:** parametry jsou fixní a model pouze počítá výstup nebo autoregresivně generuje tokeny.
- **Context length** je počet předchozích tokenů dostupných modelu. Delší kontext může přinést více relevantních informací a lepší zachycení vzdálených vztahů, ale zvyšuje paměť, čas a cenu tréninku i inference.

## Poznámka Anki 1783852352326

Karty Anki: 1783852352327
GUID: f0b1dbc27e; štítky: AI_whitepapers B3_002 konsolidace.

### Otázka (Front)

Jak fungují temperature, top-K a top-P a jak se navzájem ovlivňují?

### Odpověď (Back)

LLM v každém kroku vytváří pravděpodobnostní distribuci nad slovníkem; decoding z ní teprve vybere token. 

- **Greedy / temperature 0:** vybere nejpravděpodobnější token; je prakticky deterministický, ale shoda pravděpodobností může záviset na implementaci tiebreakingu.
- **Temperature:** nízká distribuci zostří a zvýší konzistenci, vysoká ji zploští a zvýší diverzitu až náhodnost.
- **Top-K:** ponechá K nejpravděpodobnějších tokenů; K=1 je greedy.
- **Top-P:** ponechá nejmenší množinu nejpravděpodobnějších tokenů, jejíž kumulativní pravděpodobnost dosáhne prahu P.
Při kombinaci se nejprve vytvoří kandidáti podle top-K/top-P a z nich se sampleuje s temperature; bez temperature se vzorkuje z filtrované množiny. Extrémy mohou ostatní parametry anulovat: temperature=0, K=1 nebo P≈0 vedou téměř ke greedy; K blízké slovníku a P=1 téměř nefiltrují. Neexistuje univerzální optimum: whitepaper uvádí startovní příklady `T=.2, P=.95, K=30` pro koherentní mírně kreativní výstup, `.9/.99/40` pro kreativní a `.1/.9/20` pro konzervativní; pro jedinou správnou odpověď doporučuje začít s T=0. Větší volnost zvyšuje variabilitu, ale také odbočky, nerelevanci a halucinace.

## Poznámka Anki 1783852352328

Karty Anki: 1783852352329
GUID: f8ab8e544f; štítky: AI_whitepapers B3_003 konsolidace.

### Otázka (Front)

Jaké pilíře a strategie podporují reasoning LLM?

### Odpověď (Back)

Robustní reasoning stojí na třech vrstvách: **architektuře** a jejích inductive biases, **tréninkových metodách** jako instruction tuning, RLHF či distilace a **inference/prompting strategiích**. 

- **Chain-of-Thought:** model vytvoří mezikroky před finální odpovědí.
- **Tree-of-Thoughts:** rozvětví více cest uvažování a pomocí search vybere slibnou větev; hodí se pro kombinatorické a game-tree úlohy.
- **Least-to-Most:** rozloží problém na postupně obtížnější subproblémy a výsledky jednodušších kroků předává dál.
- **Další postupy:** beam search, best-of-N, kalibrace temperature/samplingu, externí znalosti a ReAct.
- **FunSearch:** propojí předtrénovaný LLM se systematickým evaluátorem v evoluční smyčce a vyhledává nové programy, řešení či heuristiky.
Kvalita závisí na společné kalibraci promptu, vyhledávání, decoding strategie a hodnoticího signálu.

## Poznámka Anki 1783852352330

Karty Anki: 1783852352331
GUID: a84c667f91; štítky: AI_whitepapers B3_004 konsolidace.

### Otázka (Front)

Jak se má hodnotit a optimalizovat LLM při přechodu z MVP do produkce?

### Odpověď (Back)

Veřejný leaderboard nestačí. Je potřeba **task-based evaluation** nad vlastními eval daty, v konkrétním vývojovém kontextu a s explicitní definicí dobrého výstupu. Optimalizace pak vyvažuje: 

- **kvalitu vs. latenci a cenu** — menší či komprimovaný model může být pro jednoduchou úlohu výhodnější;
- **latenci vs. throughput** — větší batching snižuje cenu na požadavek, ale může zvýšit čekání;
- funkčnost, UX a provozní monitoring.
Inference bývá dominantní zdroj nákladů i latence, takže toto měření musí odpovídat skutečnému produktu.

## Poznámka Anki 1783852352332

Karty Anki: 1783852352333
GUID: e3febaaf91; štítky: AI_whitepapers B3_005 konsolidace.

### Otázka (Front)

Jak se dělí metody akcelerace inference podle toho, zda mění výstup modelu?

### Odpověď (Back)

- **Output-approximating:** zrychlení či zlevnění může změnit pravděpodobnosti nebo konkrétní výstup; patří sem například kvantizace a použití destilovaného menšího modelu.
- **Output-preserving:** stejnou matematickou funkci nebo rozhodovací pravidlo počítají efektivněji, takže zachovávají výstup; příklady jsou FlashAttention, caching a správně provedené speculative decoding.

## Poznámka Anki 1783852352334

Karty Anki: 1783852352335
GUID: d61e14eb86; štítky: AI_whitepapers B3_006 konsolidace.

### Otázka (Front)

Co je kvantizace LLM, jaké má přínosy a proč může pomoci QAT?

### Odpověď (Back)

**Kvantizace** snižuje numerickou přesnost vah a případně aktivací, například z FP32/BF16 na INT8 nebo INT4. Přináší menší paměťový footprint, menší datové přenosy na čipu i mezi zařízeními a na podporovaném hardwaru rychlejší maticové násobení. Dopad na kvalitu může být malý až nulový, ale závisí na modelu a úloze. **Post-training/inference-only quantization** se aplikuje až na hotový model; při **Quantization-Aware Training** model během tréninku simuluje nízkou přesnost a může se kvantizační chybě přizpůsobit, proto bývá odolnější.

## Poznámka Anki 1783852352336

Karty Anki: 1783852352337
GUID: da6262316b; štítky: AI_whitepapers B3_007 konsolidace.

### Otázka (Front)

Jak funguje distilace modelu a jak se liší data, knowledge a on-policy distillation?

### Odpověď (Back)

Distilace přenáší schopnosti velkého **teacher** modelu do menšího **student** modelu, aby byl levnější při inference. Funguje i nad stejnými základními daty, protože teacher má větší kapacitu a poskytuje bohatší tréninkový signál. 

- **Data distillation:** teacher generuje syntetická tréninková data; nekvalitní syntetika však může studentovi uškodit.
- **Knowledge distillation:** student napodobuje teacherovu distribuci tokenů nebo jiné jemné signály a bývá sample-efficient.
- **On-policy distillation:** student generuje vlastní sekvence a teacher hodnotí právě stavy a chyby, do nichž se student reálně dostává.
Teacher může přenášet i vzory vícekrokového uvažování.

## Poznámka Anki 1783852352338

Karty Anki: 1783852352339
GUID: d4d0b0e805; štítky: AI_whitepapers B3_008 konsolidace.

### Otázka (Front)

Jak FlashAttention zrychluje attention a proč je output-preserving?

### Odpověď (Back)

[Obrázek: paste-096f12e1648dd32212db3f45b273e8675952b183.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1783852352340

Karty Anki: 1783852352341
GUID: 5e676fa61a; štítky: AI_whitepapers B3_009 konsolidace.

### Otázka (Front)

Co jsou prefill, decode a KV cache při autoregresivní inference?

### Odpověď (Back)

- **Prefill:** model paralelně zpracuje celý vstupní prompt a pro každou vrstvu vytvoří Key/Value reprezentace; jde o velké maticové operace nad mnoha tokeny.
- **KV cache:** uloží K/V předchozích tokenů, aby se při každém novém tokenu nemusely znovu počítat pro celý kontext.
- **Decode:** nové tokeny vznikají autoregresivně po jednom a KV cache se postupně rozšiřuje. Fáze je inherentně sériová a často memory-bound, proto bývá hlavním latency bottleneckem.

## Poznámka Anki 1783852352342

Karty Anki: 1783852352343
GUID: 91842243d4; štítky: AI_whitepapers B3_010 konsolidace.

### Otázka (Front)

Jak funguje prefix/context caching a co může zničit jeho účinnost?

### Odpověď (Back)

Prefix caching uchovává **KV cache mezi požadavky**, které sdílejí stejný dlouhý začátek, například system prompt, dokument nebo historii chatu. Tím šetří opakovaný prefill, latenci i cenu. Cache může být v paměti nebo na disku a načítat se podle potřeby. Jakákoli změna na začátku promptu invaliduje všechny následující cache pozice; typický anti-pattern je vložit dynamický timestamp úplně na začátek.

## Poznámka Anki 1783852352344

Karty Anki: 1783852352345
GUID: 47e961b511; štítky: AI_whitepapers B3_011 konsolidace.

### Otázka (Front)

Jak funguje speculative decoding a kdy skutečně zrychluje generování?

### Odpověď (Back)

Malý rychlý **drafter** navrhne několik tokenů dopředu a hlavní model je ověří paralelně. Přijme se nejdelší prefix, který odpovídá rozhodnutí hlavního modelu; ostatní návrhy se zahodí. Proto je metoda quality-neutral/output-preserving vůči main modelu a zrychluje hlavně sériovou decode fázi. Přínos závisí na vysoké míře akceptace: drafter musí být dostatečně levný a dobře sladěný s hlavním modelem.

## Poznámka Anki 1783852352346

Karty Anki: 1783852352347
GUID: 6eee5aae2c; štítky: AI_whitepapers B3_012 konsolidace.

### Otázka (Front)

Proč batching zvyšuje throughput LLM inference a jaké má omezení?

### Odpověď (Back)

Batching zpracovává více požadavků současně na stejném hardwaru a lépe využívá výpočetní kapacitu. Je zvlášť užitečný při decode, který často není compute-bound, takže volnou kapacitu lze využít pro další sekvence. Hlavní omezení je paměť: každá aktivní sekvence potřebuje vlastní stav a KV cache. Větší batch proto obvykle zlepšuje throughput a cenu na request, ale může zvýšit latenci a vyčerpat dostupnou paměť.

## Poznámka Anki 1783852352348

Karty Anki: 1783852352349
GUID: 5250e0eb1b; štítky: AI_whitepapers B3_013 konsolidace.

### Otázka (Front)

Jaké typy paralelizace se používají u transformerů a jaký je jejich hlavní trade-off?

### Odpověď (Back)

- **Sequence parallelism:** rozdělí tokeny či části vstupní sekvence mezi zařízení.
- **Pipeline parallelism:** různé skupiny vrstev běží na různých zařízeních a mezivýsledky se předávají mezi stupni.
- **Tensor parallelism:** rozdělí jednu velkou maticovou či tensorovou operaci napříč zařízeními.
Přínos může zničit komunikační a synchronizační overhead mezi shardy. Správná strategie proto závisí na tom, zda je bottleneck v délce sekvence, vrstvách modelu, výpočtu uvnitř vrstvy nebo v propojení zařízení.

