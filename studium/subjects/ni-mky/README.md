# NI-MKY

ID předmětu: `ni-mky`. Knihovna: `/home/grogy/osu_repository/studium`.
Rozsah importu: 91 karet, 6 tematických sad.

Materiály jsou exportem obsahu Anki kartiček. U každé otázky je zachovaná odpověď, případná doplňující pole, původní ID a štítky.
Každý čitelný přepis je zaregistrován s doprovodným ZIP, který uchovává přesná pole HTML, šablony, matematická makra a použitá média.
Všechny sady jsou přiřazené ke stejnojmenným tématům. Import nevytvořil žádné výsledky učení; témata začínají jako `unseen`.

## Materiály a témata

| Téma | Karty | Čitelný přepis | Původní export |
|---|---:|---|---|
| Přednáška 01 | 18 | [Markdown](sources/anki-prednaska-01-v1/transcript/anki-prednaska-01-v1.md) | [ZIP](sources/anki-prednaska-01-v1/anki-prednaska-01-v1.zip) |
| Přednáška 02 | 7 | [Markdown](sources/anki-prednaska-02-v1/transcript/anki-prednaska-02-v1.md) | [ZIP](sources/anki-prednaska-02-v1/anki-prednaska-02-v1.zip) |
| Přednáška 03 | 14 | [Markdown](sources/anki-prednaska-03-v1/transcript/anki-prednaska-03-v1.md) | [ZIP](sources/anki-prednaska-03-v1/anki-prednaska-03-v1.zip) |
| Přednáška 04 | 13 | [Markdown](sources/anki-prednaska-04-v1/transcript/anki-prednaska-04-v1.md) | [ZIP](sources/anki-prednaska-04-v1/anki-prednaska-04-v1.zip) |
| Přednáška 05 | 16 | [Markdown](sources/anki-prednaska-05-v1/transcript/anki-prednaska-05-v1.md) | [ZIP](sources/anki-prednaska-05-v1/anki-prednaska-05-v1.zip) |
| Přednáška 06 | 23 | [Markdown](sources/anki-prednaska-06-v1/transcript/anki-prednaska-06-v1.md) | [ZIP](sources/anki-prednaska-06-v1/anki-prednaska-06-v1.zip) |

## Použití ve výuce

Například: „Uč mě NI-MKY z knihovny `/home/grogy/osu_repository/studium` a nejprve ověř moje základy.“

`study-library` dohledává text a vrací citace `transcript-line:N`. `study-tutor` vede výuku nad těmito pasážemi. `study-progress` zapisuje až skutečně provedené výklady a vyhodnocená cvičení.
Před výukou zkontrolovat vizuálně příslušný vzorec, tabulku nebo obrázek. Média jsou uvnitř ZIP v `media/`, původní texty v `original-notes.json` a původní šablony v `note-types.json`.
Kartičky jsou studijní podklad, nikoli doklad znalostí uživatele. Případné nepřesnosti v původních odpovědích nebyly automaticky opravovány; doplňující výklad musí být označený.

[Zpět na přehled knihovny](../../README.md)
