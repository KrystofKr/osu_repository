# BI-ZUM

ID předmětu: `bi-zum`. Knihovna: `/home/grogy/osu_repository/studium`.
Rozsah importu: 133 karet, 16 tematických sad.

Materiály jsou exportem obsahu Anki kartiček. U každé otázky je zachovaná odpověď, případná doplňující pole, původní ID a štítky.
Každý čitelný přepis je zaregistrován s doprovodným ZIP, který uchovává přesná pole HTML, šablony, matematická makra a použitá média.
Všechny sady jsou přiřazené ke stejnojmenným tématům. Import nevytvořil žádné výsledky učení; témata začínají jako `unseen`.

## Materiály a témata

| Téma | Karty | Čitelný přepis | Původní export |
|---|---:|---|---|
| 01 optimalizace | 8 | [Markdown](sources/anki-01-optimalizace-v1/transcript/anki-01-optimalizace-v1.md) | [ZIP](sources/anki-01-optimalizace-v1/anki-01-optimalizace-v1.zip) |
| 02 evolucni vypocty | 17 | [Markdown](sources/anki-02-evolucni-vypocty-v1/transcript/anki-02-evolucni-vypocty-v1.md) | [ZIP](sources/anki-02-evolucni-vypocty-v1/anki-02-evolucni-vypocty-v1.zip) |
| 03 planovani | 15 | [Markdown](sources/anki-03-planovani-v1/transcript/anki-03-planovani-v1.md) | [ZIP](sources/anki-03-planovani-v1/anki-03-planovani-v1.zip) |
| 04 multiagentni systemy | 8 | [Markdown](sources/anki-04-multiagentni-systemy-v1/transcript/anki-04-multiagentni-systemy-v1.md) | [ZIP](sources/anki-04-multiagentni-systemy-v1/anki-04-multiagentni-systemy-v1.zip) |
| 05 teorie her | 5 | [Markdown](sources/anki-05-teorie-her-v1/transcript/anki-05-teorie-her-v1.md) | [ZIP](sources/anki-05-teorie-her-v1/anki-05-teorie-her-v1.zip) |
| 06 neuronove site | 8 | [Markdown](sources/anki-06-neuronove-site-v1/transcript/anki-06-neuronove-site-v1.md) | [ZIP](sources/anki-06-neuronove-site-v1/anki-06-neuronove-site-v1.zip) |
| 07 herni stromy | 8 | [Markdown](sources/anki-07-herni-stromy-v1/transcript/anki-07-herni-stromy-v1.md) | [ZIP](sources/anki-07-herni-stromy-v1/anki-07-herni-stromy-v1.zip) |
| 08 robotika | 13 | [Markdown](sources/anki-08-robotika-v1/transcript/anki-08-robotika-v1.md) | [ZIP](sources/anki-08-robotika-v1/anki-08-robotika-v1.zip) |
| 09 uvod do AI | 8 | [Markdown](sources/anki-09-uvod-do-ai-v1/transcript/anki-09-uvod-do-ai-v1.md) | [ZIP](sources/anki-09-uvod-do-ai-v1/anki-09-uvod-do-ai-v1.zip) |
| 10 stavovy prostor | 9 | [Markdown](sources/anki-10-stavovy-prostor-v1/transcript/anki-10-stavovy-prostor-v1.md) | [ZIP](sources/anki-10-stavovy-prostor-v1/anki-10-stavovy-prostor-v1.zip) |
| 11 heuristicke prohledavani | 10 | [Markdown](sources/anki-11-heuristicke-prohledavani-v1/transcript/anki-11-heuristicke-prohledavani-v1.md) | [ZIP](sources/anki-11-heuristicke-prohledavani-v1/anki-11-heuristicke-prohledavani-v1.zip) |
| 12 agenti MDP POMDP | 8 | [Markdown](sources/anki-12-agenti-mdp-pomdp-v1/transcript/anki-12-agenti-mdp-pomdp-v1.md) | [ZIP](sources/anki-12-agenti-mdp-pomdp-v1/anki-12-agenti-mdp-pomdp-v1.zip) |
| 13 kvantove zihani QUBO | 3 | [Markdown](sources/anki-13-kvantove-zihani-qubo-v1/transcript/anki-13-kvantove-zihani-qubo-v1.md) | [ZIP](sources/anki-13-kvantove-zihani-qubo-v1/anki-13-kvantove-zihani-qubo-v1.zip) |
| 14 CSP | 3 | [Markdown](sources/anki-14-csp-v1/transcript/anki-14-csp-v1.md) | [ZIP](sources/anki-14-csp-v1/anki-14-csp-v1.zip) |
| 15 vyrokova logika SAT | 5 | [Markdown](sources/anki-15-vyrokova-logika-sat-v1/transcript/anki-15-vyrokova-logika-sat-v1.md) | [ZIP](sources/anki-15-vyrokova-logika-sat-v1/anki-15-vyrokova-logika-sat-v1.zip) |
| 16 BDD MDD | 5 | [Markdown](sources/anki-16-bdd-mdd-v1/transcript/anki-16-bdd-mdd-v1.md) | [ZIP](sources/anki-16-bdd-mdd-v1/anki-16-bdd-mdd-v1.zip) |

## Použití ve výuce

Například: „Uč mě BI-ZUM z knihovny `/home/grogy/osu_repository/studium` a nejprve ověř moje základy.“

`study-library` dohledává text a vrací citace `transcript-line:N`. `study-tutor` vede výuku nad těmito pasážemi. `study-progress` zapisuje až skutečně provedené výklady a vyhodnocená cvičení.
Před výukou zkontrolovat vizuálně příslušný vzorec, tabulku nebo obrázek. Média jsou uvnitř ZIP v `media/`, původní texty v `original-notes.json` a původní šablony v `note-types.json`.
Kartičky jsou studijní podklad, nikoli doklad znalostí uživatele. Případné nepřesnosti v původních odpovědích nebyly automaticky opravovány; doplňující výklad musí být označený.

[Zpět na přehled knihovny](../../README.md)
