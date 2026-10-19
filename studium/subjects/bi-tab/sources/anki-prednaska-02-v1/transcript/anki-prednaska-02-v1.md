# BI-TAB – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-tab/BI-TAB.apkg; APKG SHA-256 aad5d9418346792a97b103483c6a92411d60f79d52fd5a423fd0fc14dffe748b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 53183dd48468239630c7cf283347984511ecad52b3dee78ea36f4c1d42180eeb.
Původní balíčky: BI-TAB
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1709144245446

Karty Anki: 1709144245446
GUID: H*&frEOX6!; štítky: bi-tab::p02.

### Otázka (Front)

Popište základní vrstvy přenosu dat v bezdrátových sítích.

### Odpověď (Back)

Mezi základní vrstvy přenosu dat v bezdrátových sítích patří:

- **data a protokol**;
- **kódování** - úprava dat pro přenos na médiu, kontrola a oprava chyb;
- **modulace**.

## Poznámka Anki 1709144555354

Karty Anki: 1709144555354
GUID: sJR0G;Zhsx; štítky: bi-tab::p02.

### Otázka (Front)

Popište return-to-zero a non-return-to-zero kódování.

### Odpověď (Back)

Return-to-zero a non-return-to-zero jsou typy kódování, v jejichž nejjednodušším případě jsou nuly a jedničky reprezentovány zápornými a kladnými pulzy. U return-to-zero kódování se po odvysílání každého pulzu vrátí signál do neutrální hodnoty, což u non-return-to-zero kódování nenastává. Vložené návraty do neutrální hodnoty umožňují synchronizaci hodin příjemce a odesílatele, ale vyžadují větší šířku frekvenčního pásma.

| 
       [Obrázek: RZcode.png; soubor je v media/ v doprovodném ZIP] (původní alt: undefined)  | 
       [Obrázek: NRZcode.png; soubor je v media/ v doprovodném ZIP] (původní alt: undefined)  | 

| 
      return-to-zero | 
      non-return-to-zero |

## Poznámka Anki 1709149962182

Karty Anki: 1709149962182
GUID: OO5&gT^dsR; štítky: bi-tab::p02.

### Otázka (Front)

Popište kódování Manchester.

### Odpověď (Back)

Kódování Manchester je typ kódování, ve kterém nese informaci vždy hrana v polovině bitového intervalu. Ve verzi podle IEEE 802.3 reprezentuje hrana z nízké do vysoké úrovně jedničku a hrana opačným směrem nulu (v původní verzi kódování je tomu přesně naopak). Hrany, které se nachází na krajích bitového intervalu žádnou informaci nenesou a pouze uvádějí signál do potřebné úrovně.

 [Obrázek: 1920px-Manchester_encoding_both_conventions.svg.png; soubor je v media/ v doprovodném ZIP] (původní alt: undefined)

## Poznámka Anki 1709150297861

Karty Anki: 1709150297861
GUID: eQ%YUvV(]z; štítky: bi-tab::p02.

### Otázka (Front)

Uveďte základní typy útoků na bezdrátové síti.

### Odpověď (Back)

Mezi základní typy útoků na síti patří:

- **odposlouchávání **(eavesdropping),

- **modifikace dat **(tampering),
- **rušení **(jamming),

- **replay a relay útoky**.

## Poznámka Anki 1709150551825

Karty Anki: 1709150551825
GUID: t<SNS+tSg{; štítky: bi-ib::11 bi-ib::12 bi-ib::21 bi-tab::p02.

### Otázka (Front)

Popište replay útok.

### Odpověď (Back)

Replay útok je typ útoku, který typicky zahrnuje nahrání autentizačních nebo přístupových informací přenášených po síti a jejich pozdější přehrání za účelem získání neoprávněného přístupu nebo jiného efektu.

## Poznámka Anki 1709151016907

Karty Anki: 1709151016907
GUID: tW&z@g}g_}; štítky: bi-tab::p02.

### Otázka (Front)

Popište rolling code.

### Odpověď (Back)

Rolling code je metoda předcházení replay útokům, která se používá v některých keyless entry systémech. Funguje tak, že vysílač i přijímač obsahují generátory pseudonáhodných čísel, které jsou na začátku nastaveny na stejný seed. Když je vysílač spuštěn, odešle kód, který je další v pořadí generovaném jeho PRNG. Přijímač tuto hodnotu porovná s několika dalšími možnými kódy z pořadí generovaného jeho vlastním PRNG a pokud nalezne shodu, zajistí odemčení.

## Poznámka Anki 1709151438508

Karty Anki: 1709151438508
GUID: yfbLx(k2m@; štítky: bi-tab::p02.

### Otázka (Front)

Popište zranitelnost rolljam.

### Odpověď (Back)

Rolljam je zranitelnost keyless entry systémů, které používají rolling code. Její zneužití probíhá následovně:

- Zařízení útočníka generuje rušící signál, který blokuje signál z vysílače právoplatného vlastníka, a zároveň nahrává kódy z pokusů o odemčení.
- Při prvním pokusu o odemčení je použitý kód uložen.
- Při následujícím pokusu je přehrán kód z prvního pokusu a kód z druhého pokusu je uložen.

Tímto způsobem má útočník uložen funkční kód pro odemčení a zároveň snižuje riziko detekce.

## Poznámka Anki 1709153280258

Karty Anki: 1709153280258
GUID: OD{E0d_t{|; štítky: bi-tab::p02.

### Otázka (Front)

Popište relay útok na vozidlo.

### Odpověď (Back)

Relay útok na vozidlo může probíhat následujícím způsobem:

- Útočník umístí do blízkosti vozidla anténu, kterou zaznamená jím generované elektromagnetické pole. To se typicky využívá pro odemčení vozidla v případě, že se klíč nachází v jeho bezprostřední blízkosti.
- Útočník následně pomocí vysílače replikuje elektromagnetické pole v blízkosti klíče.
- Klíč na elektromagnetické pole zareaguje odesláním odemykacího kódu, který útočník zaznamená.
- Útočník kód přehraje v blízkosti vozidla, čímž dojde k jeho odemčení.

