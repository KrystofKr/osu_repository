# BI-KAB

ID předmětu: `bi-kab`. Knihovna: `/home/grogy/osu_repository/studium`.
Rozsah importu: 169 karet, 11 tematických sad.

Původem je balíček APKG z místní kopie repozitáře FIT ČVUT Anki. U každé otázky je zachovaná odpověď, případná doplňující pole, původní ID a štítky.
Každý přepis je zaregistrovaný s doprovodným ZIP obsahujícím přesná pole HTML, šablony, matematická makra, použitá média a metadata původních karet.

## Materiály a témata

| Téma | Karty | Čitelný přepis | Původní export |
|---|---:|---|---|
| Přednáška 01 | 29 | [Markdown](sources/anki-prednaska-01-v1/transcript/anki-prednaska-01-v1.md) | [ZIP](sources/anki-prednaska-01-v1/anki-prednaska-01-v1.zip) |
| Přednáška 02 | 6 | [Markdown](sources/anki-prednaska-02-v1/transcript/anki-prednaska-02-v1.md) | [ZIP](sources/anki-prednaska-02-v1/anki-prednaska-02-v1.zip) |
| Přednáška 03 | 13 | [Markdown](sources/anki-prednaska-03-v1/transcript/anki-prednaska-03-v1.md) | [ZIP](sources/anki-prednaska-03-v1/anki-prednaska-03-v1.zip) |
| Přednáška 04 | 12 | [Markdown](sources/anki-prednaska-04-v1/transcript/anki-prednaska-04-v1.md) | [ZIP](sources/anki-prednaska-04-v1/anki-prednaska-04-v1.zip) |
| Přednáška 05 | 22 | [Markdown](sources/anki-prednaska-05-v1/transcript/anki-prednaska-05-v1.md) | [ZIP](sources/anki-prednaska-05-v1/anki-prednaska-05-v1.zip) |
| Přednáška 06 | 12 | [Markdown](sources/anki-prednaska-06-v1/transcript/anki-prednaska-06-v1.md) | [ZIP](sources/anki-prednaska-06-v1/anki-prednaska-06-v1.zip) |
| Přednáška 07 | 8 | [Markdown](sources/anki-prednaska-07-v1/transcript/anki-prednaska-07-v1.md) | [ZIP](sources/anki-prednaska-07-v1/anki-prednaska-07-v1.zip) |
| Přednáška 08 | 14 | [Markdown](sources/anki-prednaska-08-v1/transcript/anki-prednaska-08-v1.md) | [ZIP](sources/anki-prednaska-08-v1/anki-prednaska-08-v1.zip) |
| Přednáška 09 | 18 | [Markdown](sources/anki-prednaska-09-v1/transcript/anki-prednaska-09-v1.md) | [ZIP](sources/anki-prednaska-09-v1/anki-prednaska-09-v1.zip) |
| Přednáška 10 | 19 | [Markdown](sources/anki-prednaska-10-v1/transcript/anki-prednaska-10-v1.md) | [ZIP](sources/anki-prednaska-10-v1/anki-prednaska-10-v1.zip) |
| Přednáška 11 | 16 | [Markdown](sources/anki-prednaska-11-v1/transcript/anki-prednaska-11-v1.md) | [ZIP](sources/anki-prednaska-11-v1/anki-prednaska-11-v1.zip) |

Členění vychází z předmětových štítků přednášek, cvičení a proseminářů. Pokud poznámka nese několik takových štítků, je zařazená jednou podle prvního hlavního štítku; ostatní štítky zůstávají uvedené u poznámky.

## Příznaky původního autora

Příznaky a pozastavení jsou vlastnostmi zdroje. Původní README uvádí: červená = chyba nebo určeno ke kontrole, oranžová = určeno k odstranění, zelená = duplicita, modrá = v poslední verzi upraveno. Ostatní příznaky nemají v README pevný význam.
V balíčku je 0 původně pozastavených karet. Karty zůstaly zachované včetně označení. Při výuce je třeba respektovat autorova upozornění a obsah případně ověřit.
Stejná kartička se může záměrně objevit ve více předmětech; její znalost ani výsledky se mezi předměty automaticky nepřenášejí.

## Použití ve výuce

Například: „Uč mě BI-KAB z knihovny `/home/grogy/osu_repository/studium` a nejprve ověř moje základy.“

`study-library` vyhledává původní pasáže s citacemi `transcript-line:N`. `study-tutor` vede výuku a `study-progress` zapisuje až skutečně provedené aktivity. Nová témata začínají jako `unseen`, bez převzatých výsledků autora.
Vzorce, tabulky a obrázky před použitím ve výuce vizuálně ověřit. Média jsou uvnitř ZIP v `media/`, přesné texty v `original-notes.json` a šablony v `note-types.json`. Věcná správnost původních odpovědí nebyla importem ověřena.

[Zpět na přehled knihovny](../../README.md)
