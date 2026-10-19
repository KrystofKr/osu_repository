# BI-APS – Přednáška 11

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1669650001117

Karty Anki: 1669650001117
GUID: Fy=nr$i!:K; štítky: bi-aps::p11 bi-ib::04.

Metadata původního zdroje pro kartu 1669650001117: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to Load Bypassing?

### Odpověď (Back)

- Umožňuje vykonat instrukci \(\mathtt{Load}\) před předchozí instrukcí \(\mathtt{Store}\), pokud jsou paměťově nezávislé. 
- V opačném případě se použije (pokud existuje) **Load** **Forwarding**.
- Pokud neexistuje, vykonat instrukci \(\mathtt{Load}\) mimo pořadí nelze.

## Poznámka Anki 1669650108494

Karty Anki: 1669650108494
GUID: h~D4um7]]U; štítky: bi-aps::p11 bi-ib::04.

Metadata původního zdroje pro kartu 1669650108494: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to Load Forwarding?

### Odpověď (Back)

- Předpokládejme vydávaní \(\mathtt{Load}\) a \(\mathtt{Store}\) instrukcí z rezervační stanice v programovém pořadí.
- Load Forwarding (nebo též Store-to-Load Forwarding) přeposílá data z instrukce \(\mathtt{Store}\) do instrukce \(\mathtt{Load}\), aby bylo zaručeno dodržení RAW závislosti.

 [Obrázek: paste-8b92f70425882c956f0b20813f3c495b171508c6.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1669656083673

Karty Anki: 1669656083673
GUID: ot5y/Kazn6; štítky: bi-aps::p11 bi-ib::04.

Metadata původního zdroje pro kartu 1669656083673: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak probíhá spekulativní vykonávání \(\mathtt{Load}\) instrukcí.

### Odpověď (Back)

- Pokud povolíme vydávání (issuing) instrukcí z rezervační stanice mimo programové pořadí, může se stát, že instrukce \(\mathtt{Load}\) bude vykonána dříve, než jí předcházející instrukce \(\mathtt{Store}\), se kterou má (monžá) RAW hazard, bude umístěna ve Store Bufferu.
- Budeme předpokládat, že neexistuje závislost a tento předpoklad validujeme později.
- Spekulativní vykonávání využívá podpory **FLB** (Finished Load Buffer) a ROB.
- Vykonané ale ješte nedokončené \(\mathtt{Load}\) instrukce budeme umisťovat do FLB.

- Kdykoliv instrukce \(\mathtt{Store}\) přechází k dokončení, vykoná kontrolu s položkami ve FLB:

- nenalezne konflikt: \(\mathtt{Store}\) je dokončena
- nalezne konflikt: zrušení spekulativně rozpracované instrukce \(\mathtt{Load}\) a instrukcí jí následujících

 [Obrázek: paste-b3de428c430f7bc96410a78582a1ffcb522643a0.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1669741467735

Karty Anki: 1669741467735
GUID: o]g[n-e28E; štítky: bi-aps::p11.

Metadata původního zdroje pro kartu 1669741467735: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký má Load Bypassing a Load Forwarding důsledek na konzistenci vícejádrového procesoru.

### Odpověď (Back)

Vícejádrový procesor, který podporuje **Load Bypassing** nebo **Load Forwarding** není sekvenčně konzistentní.

## Poznámka Anki 1669741860363

Karty Anki: 1669741860363
GUID: t=eP+K$gwd; štítky: bi-aps::p11.

Metadata původního zdroje pro kartu 1669741860363: v původním balíčku pozastavená karta.

### Otázka (Front)

Porovnejte model vícejádrového CPU, který dodržuje sekvenční konzistenci a vícejádrového CPU, které používá Load Bypassing a/nebo Load Forwarding.

### Odpověď (Back)

- CPU **je **sekvenčně konzistentní a **nepoužívá **Load Bypassing a Load Forwarding

- výhody: sekvenčně konzistentní paměť

- nevýhody: dramatická ztráta výkonnosti

- CPU **není **sekvenčně konzistentní, tedy **používá **Load Bypassing a/nebo Load Forwarding

- výhody: zachování výkonnosti

- nevýhody: programátor musí pracovat s jiným modelem konzistence
- Tento přístup je používán v praxi.

## Poznámka Anki 1669742123913

Karty Anki: 1669742123913
GUID: D)]>B($POY; štítky: bi-aps::p11.

Metadata původního zdroje pro kartu 1669742123913: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte uvolněnou konzistenci.

### Odpověď (Back)

Uvolněná konzistence ulevuje na některých z požadavků stanovených sekvenční konzistencí (\(\text{W} \to \text{R}\), \(\text{R} \to \text{R}\), \(\text{R} \to \text{W}\), \(\text{W} \to \text{W}\)).

## Poznámka Anki 1669742239542

Karty Anki: 1669742239542
GUID: qA7xTCn)yi; štítky: bi-aps::p11.

Metadata původního zdroje pro kartu 1669742239542: v původním balíčku pozastavená karta.

### Otázka (Front)

Co jsou to instrukce paměťové bariéry?

### Odpověď (Back)

Instrukce paměťové bariéry zabezpečuje uspořádání paměťových přístupů před a za touto bariérou, což typicky znamená, že paměťové operace nacházející se před bariérou jsou zaručeně dokončeny a globálně viditelné před paměťovými operacemi nacházejícími se za touto bariérou.

