# LLMs whitepapers – Původní blok 01

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::2 LLMs whitepapers
Rozsah: 15 poznámek, 15 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783852352268

Karty Anki: 1783852352269
GUID: f5e7de8371; štítky: AI_whitepapers B1_001 konsolidace.

### Otázka (Front)

Co je jazykový model a jak se moderní neurální LM liší od n-gramového modelu?

### Odpověď (Back)

- **Jazykový model** přiřazuje pravděpodobnost sekvencím tokenů; prakticky z prefixu odhaduje pravděpodobnosti následujícího tokenu.
- **LLM** je velký neurální jazykový model trénovaný na rozsáhlých textových datech, který se učí statistické vzory jazyka a používá je k porozumění či generování textu.
- **n-gram** ukládá frekvence lokálních kontextů pevné délky; moderní neurální LM se učí distribuované reprezentace a umí zachytit širší a delší závislosti.

## Poznámka Anki 1783852352270

Karty Anki: 1783852352271
GUID: d32ce2f074; štítky: AI_whitepapers B1_002 konsolidace.

### Otázka (Front)

Jaké výhody a omezení mají RNN a transformery při modelování sekvencí?

### Odpověď (Back)

- **RNN/LSTM/GRU** zpracovávají tokeny postupně. Teoreticky mohou nést stav libovolně dlouho, ale v praxi dlouhé závislosti oslabují vanishing gradient, kumulace chyb a obtížná paralelizace.
- **Transformer** zpracovává tokeny přes self-attention paralelně a dlouhé vztahy modeluje přímo, takže se obvykle lépe trénuje.
- Hlavní nevýhoda původního self-attention je časová i paměťová složitost přibližně **O(L²)** v délce sekvence.

## Poznámka Anki 1783852352272

Karty Anki: 1783852352273
GUID: 94fe78c4e8; štítky: AI_whitepapers B1_003 konsolidace.

### Otázka (Front)

Jak funguje původní encoder–decoder transformer a co znamená autoregresivní generování?

### Odpověď (Back)

Původní transformer je sekvence-na-sekvenci architektura navržená pro překlad. **Encoder** převede vstup na kontextové reprezentace a **decoder** z nich generuje výstup. Autoregresivně znamená, že decoder vytváří token po tokenu a každý nový token podmiňuje již vygenerovaným prefixem a případně reprezentací encoderu.

## Poznámka Anki 1783852352274

Karty Anki: 1783852352275
GUID: ab188b061f; štítky: AI_whitepapers B1_004 konsolidace.

### Otázka (Front)

Jaké úrovně vrstev má transformer od vstupu po výstup?

### Odpověď (Back)

- **Vstupní vrstva:** token ID → embedding; přidá se poziční informace.
- **Skryté vrstvy:** opakované transformer bloky se self-attention, position-wise feed-forward sítí, reziduálními spoji a layer normalization. Každý blok převádí sekvenci vektorů na sekvenci stejného tvaru.
- **Výstupní vrstva:** lineární projekce posledních reprezentací do slovníku a softmax pravděpodobností tokenů. Výstupní embeddingy mohou být svázané se vstupní embeddingovou maticí.

## Poznámka Anki 1783852352276

Karty Anki: 1783852352277
GUID: 1d7e617dce; štítky: AI_whitepapers B1_005 konsolidace.

### Otázka (Front)

Jaká je vstupní pipeline textu pro transformer a proč potřebuje poziční informaci?

### Odpověď (Back)

Typická pipeline je: **volitelná normalizace** textu → **tokenizace** na slova/subslova a token ID → **embedding lookup** do naučených vektorů → přidání **positional encoding/embedding**. Poziční signál je nutný, protože samotný self-attention neobsahuje pořadí tokenů a bez něj nerozlišuje slovosled.

## Poznámka Anki 1783852352278

Karty Anki: 1783852352279
GUID: 2fe3cebc16; štítky: AI_whitepapers B1_006 konsolidace.

### Otázka (Front)

Co dělá self-attention a jaké role mají Query, Key a Value?

### Odpověď (Back)

Self-attention dovoluje každému tokenu váženě čerpat informace z ostatních tokenů, takže zachytí například dlouhé závislosti či koreferenci zájmena s referentem. Z reprezentace každého tokenu se naučenými lineárními projekcemi vytvoří: **Query** („co hledám“), **Key** („podle čeho mě lze najít“) a **Value** („jakou obsahovou informaci předám“).

## Poznámka Anki 1783852352280

Karty Anki: 1783852352281
GUID: 3495234ab7; štítky: AI_whitepapers B1_007 konsolidace.

### Otázka (Front)

Jak se matematicky vypočítá scaled dot-product attention?

### Odpověď (Back)

Pro celou sekvenci se sestaví matice Q, K a V a počítá se `Attention(Q,K,V) = softmax(QKᵀ / √d_k) V`. Skalár Q·K měří relevanci; dělení `√d_k` brání příliš ostrému softmaxu a stabilizuje trénink; softmax vytvoří nezáporné váhy se součtem 1; jejich vážený součet Value vektorů dává kontextovou reprezentaci. Maticová forma umožňuje paralelní výpočet všech tokenů.

## Poznámka Anki 1783852352282

Karty Anki: 1783852352283
GUID: 1d59dc91b6; štítky: AI_whitepapers B1_008 konsolidace.

### Otázka (Front)

Co je multi-head attention a proč je expresivnější než jedna attention hlava?

### Odpověď (Back)

Multi-head attention používá několik paralelních sad projekcí Q/K/V. Jednotlivé hlavy se mohou současně specializovat na jiné vztahy, například syntaxi, koreferenci, lokální či vzdálené závislosti. Výstupy hlav se zřetězí a lineárně transformují, čímž model získá bohatší reprezentaci než z jediné hlavy.

## Poznámka Anki 1783852352284

Karty Anki: 1783852352285
GUID: 17b036b65c; štítky: AI_whitepapers B1_009 konsolidace.

### Otázka (Front)

Co znamená Add & Norm a proč transformer používá reziduální spojení a layer normalization?

### Odpověď (Back)

**Add** je reziduální/skip spojení: ke vstupu subvrstvy se přičte její výstup, což usnadňuje průchod informace a gradientu hlubokou sítí a omezuje vanishing/exploding gradients. **Norm** je layer normalization, která stabilizuje rozsah aktivací, tok gradientu a konvergenci. Společně usnadňují trénink hlubokého stacku.

## Poznámka Anki 1783852352286

Karty Anki: 1783852352287
GUID: da31f28342; štítky: AI_whitepapers B1_010 konsolidace.

### Otázka (Front)

Co je position-wise feed-forward síť v transformeru a co přidává oproti attention?

### Odpověď (Back)

Je to stejná MLP aplikovaná nezávisle na reprezentaci každého tokenu, typicky `Linear → aktivace (např. GELU) → Linear` s dočasným rozšířením dimenze. Self-attention míchá informace mezi tokeny; feed-forward síť pak každý token nelineárně přepracuje. Dodává modelu nelinearitu, kapacitu a schopnost vytvářet nové rysy.

## Poznámka Anki 1783852352288

Karty Anki: 1783852352289
GUID: 7fafba241d; štítky: AI_whitepapers B1_011 konsolidace.

### Otázka (Front)

Jak je sestaven encoder transformeru a jakou má funkci?

### Odpověď (Back)

Encoder opakuje bloky obsahující self-attention, position-wise feed-forward síť, reziduální spojení a normalizaci. Na vstupu používá tokenové a poziční embeddingy. Výsledkem jsou kontextové reprezentace vstupních tokenů, v nichž je každý token obohacen informací o vztazích v celé vstupní sekvenci.

## Poznámka Anki 1783852352290

Karty Anki: 1783852352291
GUID: 20959d1fc8; štítky: AI_whitepapers B1_012 konsolidace.

### Otázka (Front)

Jak se liší decoder, cross-attention a decoder-only transformer?

### Odpověď (Back)

- **Decoder** generuje sekvenci autoregresivně. Jeho masked/causal self-attention dovolí každé pozici vidět jen dřívější tokeny, ne budoucnost.
- V encoder–decoder modelu následuje **cross-attention**, kde decoder vybírá relevantní reprezentace z encoderu.
- **Decoder-only** nemá samostatný encoder ani cross-attention; celý vstup i dosavadní výstup zpracovává jedním kauzálním stackem a predikuje další token.

## Poznámka Anki 1783852352292

Karty Anki: 1783852352293
GUID: fb40f3f1b8; štítky: AI_whitepapers B1_013 konsolidace.

### Otázka (Front)

Jak funguje Mixture of Experts (MoE) a čím se liší od ensemble?

### Odpověď (Back)

MoE obsahuje více specializovaných **expertů**, naučený **router/gating network** a mechanismus spojení jejich výstupů. Router pro každý vstup či token vybere a zváží jen malou podmnožinu expertů; jejich výstupy se podle vah zkombinují. Tato **sparse activation** dovoluje velkou celkovou kapacitu při menším výpočtu. Na rozdíl od prostého ensemble se neaktivují a neprůměrují všichni členové stejně pro každý vstup.

## Poznámka Anki 1783852352294

Karty Anki: 1783852352295
GUID: c763eceb78; štítky: AI_whitepapers B1_014 konsolidace.

### Otázka (Front)

Jak je BERT postaven, jaké pretraining cíle používá a co vrací jako embedding?

### Odpověď (Back)

BERT (**Bidirectional Encoder Representations from Transformers**) je encoder-only transformer pro obousměrné porozumění textu, nikoli primárně pro autoregresivní generování. Při **Masked Language Modeling** se vybrané tokeny maskují či korumpují a model rekonstruuje jejich ID z levého i pravého kontextu; tím vznikají hluboké kontextualizované reprezentace, takže vektor tokenu závisí na celé větě. Původní BERT navíc používá **Next Sentence Prediction**, které rozpoznává, zda druhá věta navazuje na první. Výstupem encoderu je embedding pro každý token; reprezentace celé sekvence se často získává poolingem nebo tokenem `[CLS]`, ale pro semantic similarity bývá vhodné specializované dolaďování.

## Poznámka Anki 1783852352296

Karty Anki: 1783852352297
GUID: 14f9c751ae; štítky: AI_whitepapers B1_015 konsolidace.

### Otázka (Front)

Proč je unsupervised pre-training užitečný oproti čistě supervised tréninku?

### Odpověď (Back)

Pre-training využívá velké množství levně dostupných nelabelovaných dat, z nichž model získá obecné jazykové reprezentace a vzory. Tím snižuje závislost na drahých labelech a zlepšuje přenos a generalizaci na úlohy, které nebyly přímo obsažené v dohlíženém tréninku.

