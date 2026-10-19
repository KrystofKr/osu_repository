# BI-PA2

ID předmětu: `bi-pa2`. Knihovna: `/home/grogy/osu_repository/studium`.
Rozsah importu: 46 karet, 4 tematických sad.

Materiály jsou exportem obsahu Anki kartiček. U každé otázky je zachovaná odpověď, případná doplňující pole, původní ID a štítky.
Každý čitelný přepis je zaregistrován s doprovodným ZIP, který uchovává přesná pole HTML, šablony, matematická makra a použitá média.
Všechny sady jsou přiřazené ke stejnojmenným tématům. Import nevytvořil žádné výsledky učení; témata začínají jako `unseen`.

## Materiály a témata

| Téma | Karty | Čitelný přepis | Původní export |
|---|---:|---|---|
| Přednáška 02 | 1 | [Markdown](sources/anki-prednaska-02-v1/transcript/anki-prednaska-02-v1.md) | [ZIP](sources/anki-prednaska-02-v1/anki-prednaska-02-v1.zip) |
| Přednáška 03 | 1 | [Markdown](sources/anki-prednaska-03-v1/transcript/anki-prednaska-03-v1.md) | [ZIP](sources/anki-prednaska-03-v1/anki-prednaska-03-v1.zip) |
| Přednáška 10 | 2 | [Markdown](sources/anki-prednaska-10-v1/transcript/anki-prednaska-10-v1.md) | [ZIP](sources/anki-prednaska-10-v1/anki-prednaska-10-v1.zip) |
| Základní sada otázek | 42 | [Markdown](sources/anki-zakladni-sada-v1/transcript/anki-zakladni-sada-v1.md) | [ZIP](sources/anki-zakladni-sada-v1/anki-zakladni-sada-v1.zip) |

## Použití ve výuce

Například: „Uč mě BI-PA2 z knihovny `/home/grogy/osu_repository/studium` a nejprve ověř moje základy.“

`study-library` dohledává text a vrací citace `transcript-line:N`. `study-tutor` vede výuku nad těmito pasážemi. `study-progress` zapisuje až skutečně provedené výklady a vyhodnocená cvičení.
Před výukou zkontrolovat vizuálně příslušný vzorec, tabulku nebo obrázek. Média jsou uvnitř ZIP v `media/`, původní texty v `original-notes.json` a původní šablony v `note-types.json`.
Kartičky jsou studijní podklad, nikoli doklad znalostí uživatele. Případné nepřesnosti v původních odpovědích nebyly automaticky opravovány; doplňující výklad musí být označený.

[Zpět na přehled knihovny](../../README.md)
