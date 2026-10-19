# BI-PA1

ID předmětu: `bi-pa1`. Knihovna: `/home/grogy/osu_repository/studium`.
Rozsah importu: 90 karet, 4 tematických sad.

Materiály jsou exportem obsahu Anki kartiček. U každé otázky je zachovaná odpověď, případná doplňující pole, původní ID a štítky.
Každý čitelný přepis je zaregistrován s doprovodným ZIP, který uchovává přesná pole HTML, šablony, matematická makra a použitá média.
Všechny sady jsou přiřazené ke stejnojmenným tématům. Import nevytvořil žádné výsledky učení; témata začínají jako `unseen`.

## Materiály a témata

| Téma | Karty | Čitelný přepis | Původní export |
|---|---:|---|---|
| Přednáška 07 | 1 | [Markdown](sources/anki-prednaska-07-v1/transcript/anki-prednaska-07-v1.md) | [ZIP](sources/anki-prednaska-07-v1/anki-prednaska-07-v1.zip) |
| Přednáška 08 | 1 | [Markdown](sources/anki-prednaska-08-v1/transcript/anki-prednaska-08-v1.md) | [ZIP](sources/anki-prednaska-08-v1/anki-prednaska-08-v1.zip) |
| Přednáška 09 | 1 | [Markdown](sources/anki-prednaska-09-v1/transcript/anki-prednaska-09-v1.md) | [ZIP](sources/anki-prednaska-09-v1/anki-prednaska-09-v1.zip) |
| Základní sada otázek | 87 | [Markdown](sources/anki-zakladni-sada-v1/transcript/anki-zakladni-sada-v1.md) | [ZIP](sources/anki-zakladni-sada-v1/anki-zakladni-sada-v1.zip) |

## Použití ve výuce

Například: „Uč mě BI-PA1 z knihovny `/home/grogy/osu_repository/studium` a nejprve ověř moje základy.“

`study-library` dohledává text a vrací citace `transcript-line:N`. `study-tutor` vede výuku nad těmito pasážemi. `study-progress` zapisuje až skutečně provedené výklady a vyhodnocená cvičení.
Před výukou zkontrolovat vizuálně příslušný vzorec, tabulku nebo obrázek. Média jsou uvnitř ZIP v `media/`, původní texty v `original-notes.json` a původní šablony v `note-types.json`.
Kartičky jsou studijní podklad, nikoli doklad znalostí uživatele. Případné nepřesnosti v původních odpovědích nebyly automaticky opravovány; doplňující výklad musí být označený.

[Zpět na přehled knihovny](../../README.md)
