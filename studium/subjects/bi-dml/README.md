# BI-DML

ID předmětu: `bi-dml`. Knihovna: `/home/grogy/osu_repository/studium`.
Rozsah importu: 43 karet, 1 tematických sad.

Materiály jsou exportem obsahu Anki kartiček. U každé otázky je zachovaná odpověď, případná doplňující pole, původní ID a štítky.
Každý čitelný přepis je zaregistrován s doprovodným ZIP, který uchovává přesná pole HTML, šablony, matematická makra a použitá média.
Všechny sady jsou přiřazené ke stejnojmenným tématům. Import nevytvořil žádné výsledky učení; témata začínají jako `unseen`.

## Materiály a témata

| Téma | Karty | Čitelný přepis | Původní export |
|---|---:|---|---|
| Základní sada otázek | 43 | [Markdown](sources/anki-zakladni-sada-v1/transcript/anki-zakladni-sada-v1.md) | [ZIP](sources/anki-zakladni-sada-v1/anki-zakladni-sada-v1.zip) |

## Použití ve výuce

Například: „Uč mě BI-DML z knihovny `/home/grogy/osu_repository/studium` a nejprve ověř moje základy.“

`study-library` dohledává text a vrací citace `transcript-line:N`. `study-tutor` vede výuku nad těmito pasážemi. `study-progress` zapisuje až skutečně provedené výklady a vyhodnocená cvičení.
Před výukou zkontrolovat vizuálně příslušný vzorec, tabulku nebo obrázek. Média jsou uvnitř ZIP v `media/`, původní texty v `original-notes.json` a původní šablony v `note-types.json`.
Kartičky jsou studijní podklad, nikoli doklad znalostí uživatele. Případné nepřesnosti v původních odpovědích nebyly automaticky opravovány; doplňující výklad musí být označený.

[Zpět na přehled knihovny](../../README.md)
