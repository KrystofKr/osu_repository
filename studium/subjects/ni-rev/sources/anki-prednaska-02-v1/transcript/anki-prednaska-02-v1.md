# NI-REV – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-rev/NI-REV.apkg; APKG SHA-256 9670f49b042e57cbd1c6d96f27c545d7e3e73f639dfdfaa5254dbc7ff55faa9f. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7fc653b9bed751e297f56e0ab41b46bdc555bbf2270d66a69096723b55136e70.
Původní balíčky: NI-REV
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1728218050820

Karty Anki: 1728218050820
GUID: E)mJ|?=y,_; štítky: ni-pb::13 ni-rev::p02.

### Otázka (Front)

Definujte základní blok (basic block) kódu a control-flow graf (CFG).

### Odpověď (Back)

**Základní blok** (basic block) je maximální posloupnost po sobě jdoucích instrukcí, do které lze vstoupit jedině první instrukcí posloupnosti a opustit ji lze jedině poslední instrukcí. Základní bloky jakožto vrcholy spojené orientovanými hranami tvoří **control-flow graf** (CFG).

## Poznámka Anki 1728221053072

Karty Anki: 1728221053072
GUID: L[YzLW(C7u; štítky: ni-pb::13 ni-rev::p02.

### Otázka (Front)

Popište vstupní bod (entry point) programu.

### Odpověď (Back)

Vstupní bod (entry point) programu je bod programu, ve kterém je spuštěno jeho vykonávání. Na Windows je jedná o funkci \(\texttt{mainCRTStartup}\) (nebo její variantu) volanou z \(\texttt{kernel32.dll}\). Před spuštěním funkce \(\texttt{main}\) provede funkce \(\texttt{_initterm}\) (nebo její varianta) spuštění inicializačních funkcí, jejichž ukazatele jsou uloženy v sekci \(\texttt{.rdata}\). Mezi tyto funkce patří:

- \(\texttt{pre_c_init}\) nebo \(\texttt{pre_cpp_init}\),

- konstruktory globálních instancí tříd a registrace volání jejich destruktorů,
- další programátorem registrované funkce.

## Poznámka Anki 1728221459192

Karty Anki: 1728221459192
GUID: qB3;o)%8hu; štítky: ni-pb::12 ni-rev::p02.

### Otázka (Front)

Popište specifika programů v debugovací verzi.

### Odpověď (Back)

Při analýze programů v debugovací verzi se můžeme setkat s:

- **hot patching** - před prolog funkce je vloženo několik instrukcí \(\texttt{nop}\), které rezervují místo pro případné úpravy funkce za běhu programu;

- \(\texttt{call}\) **to **\(\texttt{jmp}\) - funkce jsou volány přes další úroveň nepřímého skoku, což umožňuje nahrazení libovolné funkce za běhu programu.

## Poznámka Anki 1728223142131

Karty Anki: 1728223142131
GUID: k6ri>?qe]Y; štítky: ni-rev::p02.

### Otázka (Front)

Popište Import Address Table (IAT) a princip jejího zneužití.

### Odpověď (Back)

Import Address Table (IAT) se nachází v sekci \(\texttt{.rdata}\) a ukazatel na ni je součástí každého záznamu v importním adresáři (import directory table). Z počátku obsahuje jména funkcí nebo jejich pořadová čísla (ordinal), která jsou při zavádění do paměti loaderem přepsána na skutečné adresy daných funkcí. Volání importovaných funkcí za běhu programu pak probíhá skokem na adresu uloženou v IAT, což znamená, že přepsáním záznamu v IAT lze přesměrovat volání dané funkce napříč celým programem.

