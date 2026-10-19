# BI-HWB – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-hwb/BI-HWB.apkg; APKG SHA-256 0303626d2408f7eee1801e17ecb475633a60c42f914f37290ffd8c479013ce2b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b861d2e855c5070244800c22d62092a09b22aee0ded024030525b06a7d18285e.
Původní balíčky: BI-HWB
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1699285611153

Karty Anki: 1699285611154
GUID: H=-!Y}~{YY; štítky: bi-hwb::p07 bi-ib::17.

### Otázka (Front)

Popište útok postranním kanálem (side-channel attack).

### Odpověď (Back)

Útok postranním kanálem (side-channel attack) je často pasivní neinvazivní typ útoku. Zneužívá informací, které jsou uvolňovány cílem do jeho okolí, ale nejsou přímo součástí jeho normální funkce. Využívá slabin v implementaci:

- **algoritmu** - zpřístupňuje informace ve vhodné formě (square-and-multiply),

- **architektury** - ovlivňuje časování a pořadí operací (Meltdown, Spectre),

- **technologie** - určuje spotřebu nebo množství elektromagnetického záření.

## Poznámka Anki 1699297494277

Karty Anki: 1699297494277
GUID: i-,3?}~UhG; štítky: bi-hwb::p07 bi-ib::17.

### Otázka (Front)

Popište odběrový postranní kanál na příkladu algoritmu square and multiply.

### Odpověď (Back)

Odběrový postranní kanál využvá měření spotřeby energie monitorovaného zařízení. Protože square and multiply provede operaci násobení pouze tehdy, když je v exponentu na dané pozici jednička, lze pomocí zákmitů v napájení způsobených operací násobení vyčíst hodnotu exponentu.

## Poznámka Anki 1699297940344

Karty Anki: 1699297940345
GUID: tSht)}/|X%; štítky: bi-hwb::p07 bi-ib::17.

### Otázka (Front)

Popište důvod vzniku odběrového postranního kanálu.

### Odpověď (Back)

Spotřeba zařízení se odvíjí od množství aktivity na jeho logických obvodech, které jsou zpravidla tvořeny CMOS transistory. Přechody mezi jednotlivými stavy CMOS transistoru způsobují vyšší odběr, a protože aktivita na logických obvodech tyto přechody vyvolává, vzniká závislost spotřeby na operacích a hodnotách, které jsou na logickém obvodu zpracovávány.

## Poznámka Anki 1699298288114

Karty Anki: 1699298288115
GUID: ut`#MK;?o$; štítky: bi-hwb::p07 bi-ib::17.

### Otázka (Front)

Jaké existují typy útoků odběrovým postranním kanálem?

### Odpověď (Back)

Existují následující dva typy útoků odběrovým postranním kanálem:

- **simple power analysis** (jednoduchá odběrová analýza) - analýza spotřeby v čase během jednoho průběhu,

- **differential power analysis **(diferenciální odběrová analýza) - analýza spotřeby ve stejných okamžicích v čase napříč vícero průběhy.

## Poznámka Anki 1699299796241

Karty Anki: 1699299796241
GUID: o,6`9X_N&); štítky: bi-hwb::p07 bi-ib::17.

### Otázka (Front)

Popište průběh diferenciální odběrové analýzy (differential power analysis).

### Odpověď (Back)

Diferenciální odběrová analýza probíhá v následujících fázích:

- Zvolíme vnitřní hodnotu \(v = f(d, k)\), která je funkcí známých vstupních dat \(d\) a neznámého částečného klíče \(k\) (musí být tak krátký, aby šel odhadovat).
- Změříme průběh spotřeby \(t_i\) (traces) pro šifrování různých dat \(d_i\).
- Sestavíme matici hypotetických vnitřních hodnot \(v_{i, j}\) pro všechny možné klíče \(k\) a použitá data \(d\).
- Sestavíme matici hypotetické spotřeby \(h_{i, j}\) z hypotetických vnitřních hodnot a modelu spotřeby.
- Statisticky vyhodnotíme, která hypotéza o klíči nejlépe odpovídá změřené spotřebě.

## Poznámka Anki 1699303212048

Karty Anki: 1699303212049
GUID: l1V)<xr]-6; štítky: bi-hwb::p07 bi-ib::17.

### Otázka (Front)

Jaké existují modely spotřeby v diferenciální odběrové analýze?

### Odpověď (Back)

Diferenciální odběrová analýza využívá následující modely spotřeby:

- **single bit model** - spotřeba je závislá na konkrétním bitu vnitřní hodnoty,

- **hammingova váha **- spotřeba je závislá na počtu jedniček vnitřní hodnoty,

- **hammingova vzdálenost **- spotřeba je závislá na počtu změněných bitů oproti předchozímu stavu vnitřní hodnoty.

## Poznámka Anki 1717955199241

Karty Anki: 1717955199241
GUID: c6]f._s5I6; štítky: bi-hwb::p07 bi-ib::17.

### Otázka (Front)

Popište typy útoků postranním kanálem (side-channel attacks).

### Odpověď (Back)

Mezi typy útoků postranním kanálem (side-channel attacks) patří:

- **časový** - doba provedení operace závisí na utajovaných datech (útok na porovnání polí),

- **chybový** - chybový kód zavisí na utajovaných datech (padding oracle),

- **odběrový** - spotřeba závisí na utajovaných datech (simple power analysis, differential power analysis),

- **elektromagnetický** - množství elektromagnetického záření závisí na utajovaných datech (TEMPEST).

## Poznámka Anki 1717955667097

Karty Anki: 1717955667097
GUID: v9|9lMdpvW; štítky: bi-hwb::p07 bi-ib::17.

### Otázka (Front)

Popište útok časovým postranním kanálem na porovnání polí.

### Odpověď (Back)

Útok časovým postranním kanálem na porovnání polí lze zneužít v situacích, kdy je hodnota \(a\) zadaná uživatelem (např. heslo, hash nebo session key) porovnávána se správnou referenční hodnotou \(b\). Pokud je při porovnání obou polí použit typický přístup s podmínkou a operátorem nerovnosti,

 [Obrázek: paste-decd2bb80a2e5de1e82ace9cbe9e3344fd50f594.jpg; soubor je v media/ v doprovodném ZIP] 

je možné na základě času do odezvy programu odhadovat jednotlivé byty referenční hodnoty, protože každý shodný byte prodlouží dobu jeho běhu. Správný způsob porovnání polí spočívá v odstranění podmínky a použití logických operátorů OR, XOR a NOT:

 [Obrázek: paste-7ddc0d530070902668c13396e7ab38310f97a605.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1717956122689

Karty Anki: 1717956122690
GUID: sTWqv-6Th+; štítky: bi-hwb::p07 bi-ib::17.

### Otázka (Front)

Popište obecný postup při útoku odběrovým postranním kanálem.

### Odpověď (Back)

Při útoku odběrovým postranním kanálem se typicky využívá následující infrastruktura:

- **kryptografické zařízení** - provádí výpočty,

- **osciloskop** - měří spotřebu kryptografického zařízení a data předává do počítače,

- **počítač** - řídí výpočty kryptografického zařízení a analyzuje data z osciloskopu.

