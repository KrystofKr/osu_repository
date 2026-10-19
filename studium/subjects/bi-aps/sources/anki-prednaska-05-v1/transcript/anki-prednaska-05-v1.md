# BI-APS – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1666016842088

Karty Anki: 1666016842089
GUID: ybS)$3>>l2; štítky: bi-aps::p05 bi-ib::04 bi-spol::29.

### Otázka (Front)

Definujte přerušení.

### Odpověď (Back)

Přerušení (interrupt) je asynchronní nebo synchronní událost či požadavek na CPU jádro, aby přerušilo právě vykonávaný program a promptně reagovalo na příčinu této události.

## Poznámka Anki 1666016883831

Karty Anki: 1666016883831
GUID: uP;.K3Wm8y; štítky: bi-aps::p05 bi-ib::04 bi-spol::29.

### Otázka (Front)

Definujte asynchronní přerušení.

### Odpověď (Back)

Asynchronní přerušení je přerušení s vnější příčinou, která nesouvisí s právě vykonávanou instrukcí a ta může být dokončena. Rozlišujeme:

- **maskovatelná** - nemusí být nutně obsloužena,

- **nemaskovatelná** - musí být obsloužena.

Zdroji maskovatelných asynchronních přerušení mohou být:

- periferie (např. myš, joystick),
- časovač preemptivního multitaskingu,
- jiný program (externí softwarové přerušení).

Zrdoji nemaskovatelných asynchronních přerušení mohou být:

- chyby hardware (např. vybitá baterie),
- stisknutí tlačítka reset.

## Poznámka Anki 1666016931445

Karty Anki: 1666016931445
GUID: bg=w3#T?`b; štítky: bi-aps::p05 bi-ib::04 bi-spol::29.

### Otázka (Front)

Definujte synchronní přerušení.

### Odpověď (Back)

Příčina přerušení je vnitřní a je důsledkem právě vykonávané instrukce. Tato instrukce nebude dokončena.

## Poznámka Anki 1666017280985

Karty Anki: 1666017280985
GUID: LrTb@<Lv#>; štítky: bi-aps::p05 bi-ib::04.

Metadata původního zdroje pro kartu 1666017280985: v původním balíčku pozastavená karta.

### Otázka (Front)

Čemu odpovídá výjimka (exception) a přerušení (interrupt) v terminologii RISC-V.

### Odpověď (Back)

- výjimka (exception) - (vnitřní) synchronní přerušení
- přerušení (interrupt) - (vnější) asynchronní přerušení

## Poznámka Anki 1666017504708

Karty Anki: 1666017504708
GUID: lW8NLY>],p; štítky: bi-aps::p05 bi-ib::04.

### Otázka (Front)

Jak rozlišujeme výjimky? Uveďte příklady.

### Odpověď (Back)

Výjimky vznikají z dvou důvodů:

- chyby při provádění instrukcí

- přetečení, dělení nulou
- přístup na neplatnou adresu
- neoprávněný přístup do paměti

- instrukce explicitně vyvolávající výjimku:

- instrukce \(\mathtt{int}\) (x86)
- instrukce \(\mathtt{syscall}\)
- instrukce \(\mathtt{breakpoint}\)

## Poznámka Anki 1666022480893

Karty Anki: 1666022480893
GUID: o@hpBq$EGs; štítky: bi-aps::p05 bi-ib::04 bi-spol::29.

Metadata původního zdroje pro kartu 1666022480893: v původním balíčku pozastavená karta.

### Otázka (Front)

Kde se najde obslužná rutina přerušení?

### Odpověď (Back)

V jednoduchých **vestavných systémech** způsobí všechna přerušení skok na jedinou předdefinovanou adresu. **Standartní systémy** používají tabulku vektorů přerušení, která obsahuje buď adresy jednotlivých obslužných rutin (x86, ARM), nebo skokové instrukce na ně vedoucí (RISC-V, AVR).

## Poznámka Anki 1666022706681

Karty Anki: 1666022706681
GUID: NaiJ[<iY/u; štítky: bi-aps::p05.

### Otázka (Front)

Jaké bezpečnostní režimy OS rozlišujeme? Jak se mezi nimi lze přesouvat?

### Odpověď (Back)

- **privilegovaný režim** (OS) - smí vykonávat všechny instrukce a přistupovat ke všem registrům
- **uživatelský režim** (uživatelské programy) - nemůže vykonávat privilegované instrukce a přistupovat k privilegovaným registrům (musí zažádat použitím **systémového volání**)

## Poznámka Anki 1666022952374

Karty Anki: 1666022952374
GUID: gH*ZO1]iUt; štítky: bi-aps::p05.

Metadata původního zdroje pro kartu 1666022952374: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké úrovně zabezpečení definuje RISC-V? Co platí pro jejich implementaci a vidielnost?

### Odpověď (Back)

- User/Application (U-mode)
- Supervisor (S-mode)
- Machine (M-mode)

Podle potřeby může být v zařízení **implementována libovolná podmnožina** těchto úrovní, vždy ale musí obsahovat M-mode.

Úroveň zabezpečení je programátorovi **neviditelná**, tzn. RISC-V nedefinuje místo, kde se tato informace nachází.

## Poznámka Anki 1666023303067

Karty Anki: 1666023303067
GUID: B<Kiz=0,1+; štítky: bi-aps::p05 bi-ib::04 bi-spol::29.

Metadata původního zdroje pro kartu 1666023303067: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak zajistíme podporu přerušení od více periferií?

### Odpověď (Back)

- softwarově - při přerušení se projdou stavové registry jednotlivých periferií
- hardwarově - do návrhu se přidá speciální registr uchovávající informaci o tom, která periferie přerušení vykonává

## Poznámka Anki 1666023466124

Karty Anki: 1666023466124
GUID: Dv]#*=m>)$; štítky: bi-aps::p05 bi-ib::04.

Metadata původního zdroje pro kartu 1666023466124: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak se řeší výjimky u zřetězeného zpracování?

### Odpověď (Back)

Aby byla zachována sekvenční sémantika programu, použijeme **přesné výjimky**. To znamená, že výjimky budeme volat z jediného stupně zřetězení, který bude poslední stupeň, ve kterém ješte může nějaká výjimka nastat.

## Poznámka Anki 1687705015661

Karty Anki: 1687705015661
GUID: Q@zl|2}N&x; štítky: bi-aps::p05.

### Otázka (Front)

Co je to systémové volání?

### Odpověď (Back)

Systémové volání je způsob, kterým si neprivilegovaný program běžící v user mode může požádat o poskytnutí služby od operačního systému. Systémové volání probíhá stejně jako běžné volání rutiny.

