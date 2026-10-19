# BI-APS – Přednáška 12

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 17 poznámek, 17 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1670260126295

Karty Anki: 1670260126295
GUID: i#r?(oreI,; štítky: bi-aps::p12 bi-ib::04.

Metadata původního zdroje pro kartu 1670260126295: v původním balíčku pozastavená karta.

### Otázka (Front)

K čemu slouží prediktor skoků?

### Odpověď (Back)

Prediktory skoků umožňují

- odhadnout chování skokové instrukce,
- odhadnout cíl skoku.

## Poznámka Anki 1670260217504

Karty Anki: 1670260217504
GUID: uv1%@4oHOB; štítky: bi-aps::p12 bi-ib::04.

Metadata původního zdroje pro kartu 1670260217504: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak rozdělujeme činnosti související se spekulativním vykonáváním skokových instrukcí?

### Odpověď (Back)

- **spekulativní provádění instrukcí** (Branch Speculation) - predikce chování skokové instrukce a následné provádění spekulativně vybrané větve.
- **validace spekulativního provádění/zotavení** (Branch Validation/Recovery) - ověření správnosti predikce a případné ukončení nesprávné větve a zahájení výběru instrukcí z té správné

## Poznámka Anki 1670260347305

Karty Anki: 1670260347305
GUID: L(+,>jooT/; štítky: bi-aps::p12.

Metadata původního zdroje pro kartu 1670260347305: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak jsou odlišeny instrukce spekulativně prováděného bloku?

### Odpověď (Back)

Každá spekulativně prováděná instrukce je označena unikátním identifikátorem (tag).

## Poznámka Anki 1670260387608

Karty Anki: 1670260387608
GUID: t9~Yv5RDZ|; štítky: bi-aps::p12 bi-ib::04.

Metadata původního zdroje pro kartu 1670260387608: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak probíhá validace spekulativního provádění?

### Odpověď (Back)

V případě, že predikce skoku byla správná, identifikátor patřící danému bloku je zrušen a všechny instrukce jím označené se stávají nespekulativní (mohou být dokončeny).

## Poznámka Anki 1670260525945

Karty Anki: 1670260525945
GUID: b^).ICA5a9; štítky: bi-aps::p12 bi-ib::04.

Metadata původního zdroje pro kartu 1670260525945: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak probíhá zotavení z chybné predikce skoku?

### Odpověď (Back)

- Spekulativní větev se ukončí, tedy identifikují se všechny nesprávné instrukce (identifikátory všech bloků nesprávných větví) a zneplatní se instrukce ve frontě instrukcí, v rezervačních stanicích a v ROBu.
- Zahájí se vykonávání ze správné větve, tedy PC se aktualizuje na nově vypočtenou adresu nebo adresu uloženou během předchozího spekulativního vykonávání.

## Poznámka Anki 1670260589205

Karty Anki: 1670260589205
GUID: mIn}wA9J-i; štítky: bi-aps::p12 bi-ib::04.

### Otázka (Front)

Na jaké podúkoly se dělí predikce skoků?

### Odpověď (Back)

-  predikce cíle větvení (branch target prediction/speculation)

- predikce hodnoty podmínky větvení (branch condition prediction/speculation)

## Poznámka Anki 1670261273361

Karty Anki: 1670261273361
GUID: Xi|sRgc[b; štítky: bi-aps::p12 bi-ib::04.

### Otázka (Front)

Jak probíhá predikce cíle větvení?

### Odpověď (Back)

Predikce větvení probíhá za pomoci BTB (Branch Target Buffer), GHR (Global History Register) a RAS (Return Address Stack).

## Poznámka Anki 1670261304638

Karty Anki: 1670261304638
GUID: MFq3n%6%m6; štítky: bi-aps::p12 bi-ib::04.

### Otázka (Front)

Co je to Branch Target Buffer (BTB) u predikce cíle větvení?

### Odpověď (Back)

- Jedná se o plně nebo částečně asociativní SP, jejíž řádky jsou dvojice **Branch Instruction Address** (BIA) (klíč) a **Branch Target Address** (BTA) (hodnota).

- Pokud se skoková instrukce vykonává po několikáté, nemusí se vypočítávat cíl skoku, ale jen se přečte BTB.

## Poznámka Anki 1670261345798

Karty Anki: 1670261345798
GUID: H3AxLdhRgn; štítky: bi-aps::p12 bi-ib::04.

### Otázka (Front)

Co je to Global History Register (GHR) u predikce cíle větvení?

### Odpověď (Back)

- Obvykle posuvný registr uchovávající několik posledních bitů Taken nebo Not-Taken.

- Používá se společně s PC jako parametr pro hashovací funkci do BTB.

## Poznámka Anki 1670269987745

Karty Anki: 1670269987746
GUID: D2-@?}H@`t; štítky: bi-aps::p12 bi-ib::04.

### Otázka (Front)

Co je to Return Address Stack (RAS) u predikce cíle větvení?

### Odpověď (Back)

- Protože volání podprogramů a návraty z nich jsou velmi časté, rozšiřuje se prediktor cíle skoku o zásobník návratových adres.
- Tím se integruje predikce větvení s řízením toku instrukcemi volání podprogramů.
- Počet položek RAS je 8 až 32 (typicky 16).

## Poznámka Anki 1670270368070

Karty Anki: 1670270368070
GUID: Af2:#PU$o?; štítky: bi-aps::p12 bi-ib::04.

### Otázka (Front)

Jaké rozlišujeme typy predikcí splnění podmínky větvení?

### Odpověď (Back)

- **statická predikce **(úspěšnost 70 % - 80 %) - pro danou skokovou instrukci je výsledek predikce vždy stejný

- **BTFNT** (Backwards Taken, Forwards Not-Taken) - předpovídáme, že dopředný skok (relativně k PC) neskočí a zpětný ano

- **heuristiky** analyzující program - výsledky heuristik se předávají jako **branch hints** zakódované ve skokových instrukcích

- **profilace** - vykonávání programu s různými vstupy

- **dynamická predikce **(úspěšnost 80 % - 98 %) - pro danou skokovou instrukci se může výsledek v čase měnit

- **hybridní predikce** - predikuje dynamicky, pokud však není dostupná stavová informace o predikci, použije se statická predikce

## Poznámka Anki 1670270737846

Karty Anki: 1670270737846
GUID: HpIKX~=/sR; štítky: bi-aps::p12 bi-ib::04.

### Otázka (Front)

Popište Smithův prediktor. Co je to interference?

### Odpověď (Back)

- Smithův prediktor obsahuje několik \(k\)-bitových čítačů.

- Popisuje se množinou konečných automatů, kde stavy automatů představují predikce a mezi stavy se přechází dle skutečného chování dané skokové instrukce.

- Jestliže je Smithův prediktor tvořen \(2^m\) automaty, pak \(m\) LSBs PC se používá pro jejich indexaci.
- Tedy různé skokové instrukce se mohou mapovat do jednoho automatu a vzniká interference. Rozlišujeme:

- **neutrální interferenci** - úspěšnost predikcí tohoto automatu nedegraduje,

- **negativní interferenci** - instrukce vzájemně negativně ovlivňují predikce automatu.

- Implementace \(1\)-bitového Smithova prediktoru (\(k=1\)):

 [Obrázek: paste-e97110281c3755cc9ce9334b66605a69fc9f5885.jpg; soubor je v media/ v doprovodném ZIP] 

- Implementace \(2\)-bitového Smithova prediktoru (\(k=2\)):

 [Obrázek: paste-fd61202c0ed26f7b80489f6de2f006ced0209720.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1670271228341

Karty Anki: 1670271228341
GUID: >6,H7b:T8; štítky: bi-aps::p12 bi-ib::04.

Metadata původního zdroje pro kartu 1670271228341: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou výhody a nevýhody Smithova prediktoru? Jak se jeho nevýhody dají zmírnit?

### Odpověď (Back)

- Smithův prediktor se hodí pro skokové instrukce, které mají v sérii opakující se chování jednoho typu (např. \(\text{TTT}\dots\text{TNNN}\dots\text{N}\)).

- Prediktor se zasaturuje v jednom z krajních stavů, případně se přeučí na novou hodnotu.

- Naopak nevhodný je pro predikci vzorů, kde dochází k častému střídání chování instrukce (např. \(\text{TNTN}\dots\text{TN}\)).
- Proto Smithův prediktor doplňujeme o **lokální **nebo **globání** **historii**, která se potom podílí na indexaci konkrétního automatu Smithova prediktoru.

## Poznámka Anki 1670272135119

Karty Anki: 1670272135119
GUID: y8?N%kh}hJ; štítky: bi-aps::p12 bi-ib::04.

### Otázka (Front)

Popište dvouúrovňový prediktor s lokální historií větvení.

### Odpověď (Back)

- Vychází ze **Smithova prediktoru**, který je obohacen o **Branch History Table** (BHT).

- BHT je množina posuvných registrů, kde každý z nich uchovává několikabitovou historii daného skoku.

- Lokální historie přináší možnost sledovat **autokorelaci **skokových instrukcí.

 [Obrázek: paste-6c7f91ada7d99b5bdc128b970fbae1da23be2c7d.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1670272257413

Karty Anki: 1670272257413
GUID: s-,IT^|)K{; štítky: bi-aps::p12 bi-ib::04.

### Otázka (Front)

Popište dvouúrovňový prediktor s globální historií větvení.

### Odpověď (Back)

- Vychází ze **Smithova prediktoru**, který je obohacen o **Branch History Register **(BHR).

- BHR je několikabitový posuvný registr, který ukládá globální historii skoků.

- Globální historie přináší možnost sledovat vzájemnou **korelaci** skokových instrukcí.

 [Obrázek: paste-1a41d9d084dd948a1565752f7b0f250c81cc0868.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1670273298249

Karty Anki: 1670273298250
GUID: n>ie!bGe^a; štítky: bi-aps::p12 bi-ib::04.

Metadata původního zdroje pro kartu 1670273298250: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište TAGE (Tagged Geometric History Length) prediktor.

### Odpověď (Back)

- Prediktor vhodný pro detekci krátkých i velmi dlouhých vzorů.

- Základní prediktor \(T_0\) je doplněn o několik dalších prediktorů \(T_i\), které pro indexaci využívají \(L(i)\) bitů globální historie a několik nejnižších bitů PC.
- Prediktory \(T_i\) používají dvě hashovací funkce (a eliminují tak interference):

- \(\mathtt{Hash1}\) pro indexaci položky

- \(\mathtt{Hash2}\) pro Tag - ověření, že daná položka skutečně odpovídá dané skokové instrukci s danou historií

- Nejvyšší prioritu dostává ten prediktor \(T_i\), který detekuje shodu tagu a má nejdelší historii.
- Položka \(\text{U}\) (Useful Counter) je typicky \(2\)-bitový saturovaný čítač úšpešnosti predikcí (potlačuje predikce v období učení prediktoru).
- Prediktory \(T_i\) s delší historií jsou obvykle menší než ty předešlé (mají menší pravděpodobnost zaplnění).

 [Obrázek: paste-c0154463806107d82dab188da7634fd8cbb24102.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1670406983914

Karty Anki: 1670406983914
GUID: GG_Fl%Ae@3; štítky: bi-aps::p12 bi-ib::04.

### Otázka (Front)

Co je to Pattern History Table (PHT) u predikce chování skokové instrukce?

### Odpověď (Back)

PHT je označení pro reprezentaci Smithova prediktoru, tedy množinu několika konečných automatů (\(k\)-bitových čítačů) sloužících pro predikci chování skokové instrukce.

