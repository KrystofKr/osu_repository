# LLMs whitepapers – Původní blok 04

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::2 LLMs whitepapers
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783852352350

Karty Anki: 1783852352351
GUID: b6faf63a0c; štítky: AI_whitepapers B4_001 konsolidace.

### Otázka (Front)

Jak se připravují data a jak probíhá základní training loop transformeru?

### Odpověď (Back)

1. **Příprava dat:** filtrace a čištění, normalizace a deduplikace; deduplikace omezuje opakování a leakage, zvyšuje efektivní diverzitu a zpřesňuje evaluaci.
2. **Tokenizace:** text se rozloží například pomocí BPE nebo Unigramu na tokeny a převede přes **vocabulary** — množinu tokenů mapovaných na ID.
3. **Rozdělení dat:** vytvoří se train a oddělený eval/test split.
4. **Trénink:** vzorkuje se batch vstupů a targetů → forward pass → výpočet loss, často cross-entropy → backpropagation gradientů → update parametrů optimizerem; cyklus se opakuje do konvergence nebo stanoveného počtu tokenů/kroků.

## Poznámka Anki 1783852352352

Karty Anki: 1783852352353
GUID: 5085cf174c; štítky: AI_whitepapers B4_002 konsolidace.

### Otázka (Front)

Co je prompt engineering a kdy použít zero-shot, one-shot nebo few-shot?

### Odpověď (Back)

**Prompt engineering** je iterativní návrh vstupu tak, aby model vytvořil relevantní, přesný a správně formátovaný výstup. 

- **Zero-shot:** pouze instrukce bez ukázky; hodí se pro jednoduché nebo standardní úlohy. U klasifikace se obvykle volí nízká temperature pro stabilitu.
- **One-shot:** jedna demonstrace požadovaného mapování vstup → výstup.
- **Few-shot:** více demonstrací, které učí obsah, strukturu, styl a tón. Obecný start je přibližně 3–5 příkladů, u klasifikace lze začít kolem šesti a dále měřit.
Potřebný počet závisí na složitosti, modelu, kvalitě příkladů a context window. Příklady mají být přesné, relevantní, různorodé a zahrnovat edge cases; u klasifikace promíchej pořadí tříd, aby se model neučil sekvenci labelů. System prompt a příklady jsou komplementární: system prompt stanoví globální pravidla a formát, demonstrace ukazují konkrétní pattern.

## Poznámka Anki 1783852352354

Karty Anki: 1783852352355
GUID: 0fd7c937c5; štítky: AI_whitepapers B4_003 konsolidace.

### Otázka (Front)

Jaké hlavní trendy, možnosti a rizika charakterizují moderní LLM?

### Odpověď (Back)

- **Evoluce:** pole se posunulo od menších encoder–decoder modelů ke škálovaným decoder-only LLM s miliardami parametrů a tréninkem na velmi rozsáhlých korpusech; růst dat a parametrů přinesl lepší výkon, emergentní schopnosti a zero/few-shot generalizaci.
- **Open models:** veřejně dostupný kód a předtrénované váhy usnadňují lokální nasazení a úpravy, ale vždy je nutné ověřit licenci a podmínky konkrétního použití.
- **Multimodalita:** moderní modely mohou zpracovávat či generovat více modalit, například text, obrázky, audio a video.
- **Limity:** dokument upozorňuje na nedokonalou konverzační přirozenost, omezené matematické schopnosti a neúplný alignment s lidskými hodnotami, včetně biasu a toxicity.

## Poznámka Anki 1783852352356

Karty Anki: 1783852352357
GUID: 7eadc9a439; štítky: AI_whitepapers B4_004 konsolidace.

### Otázka (Front)

Jaké text-understanding úlohy dokument spojuje s LLM a proč v nich LLM pomáhají?

### Odpověď (Back)

- **Natural Language Inference (NLI):** model posuzuje, zda lze hypotézu logicky odvodit z premisy; například z „Všichni psi jsou savci“ plyne „Tento pes je savec“.
- **Text classification:** přiřazuje text do předem definovaných kategorií, i když jsou hranice subtilní, nejasné nebo se překrývají.
- **Text analysis:** z rozsáhlých korpusů získává vzory, témata a hlubší insighty místo pouze povrchových znaků.
Podle dokumentu LLM těží z jemnějšího sémantického a kontextového porozumění, díky němuž lépe zachycují nuance a v NLI mohou dosahovat výkonu blízkého člověku.

