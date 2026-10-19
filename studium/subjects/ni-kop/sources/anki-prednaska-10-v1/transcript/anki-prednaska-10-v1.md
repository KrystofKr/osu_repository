# NI-KOP – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1733094684947

Karty Anki: 1733094684947
GUID: JK)Wk7zS-@; štítky: ni-kop::p10 ni-spol::14.

### Otázka (Front)

Popište evoluční strategii a její obecnou strukturu.

### Odpověď (Back)

Evoluční strategie patří mezi evoluční algoritmy. Vyznačuje se následujícími vlastnostmi:

- **kódování jedince** - vektor reálných čísel a endogenní parametry (velikost a směr kroku, standardní odchylky);

- **křížení **- diskrétní, střední, vážené;

- **mutace **- přičtení náhodné veličiny (vektoru) s rozdělením \(\operatorname N(0, \sigma^2)\) nebo podobným,

- **řízení populace** - soutěž \((\mu + \lambda)\) nebo \((\mu, \lambda)\) s rankingem.

Obecná struktura evoluční strategie se liší v tom, že před křížením probíhá ještě výběr pro křížení. Fáze tedy jsou:

- selekce,
- výběr pro křížení a křížení,
- mutace
- řízení populace.

### Doplňující pole (Extra)

V kontextu evoluční strategie se křížení někdy nazývá rekombinace.

## Poznámka Anki 1733316534301

Karty Anki: 1733316534302
GUID: F|E<++#8m; štítky: ni-kop::p10 ni-spol::14.

### Otázka (Front)

Popište metody křížení v evoluční strategii.

### Odpověď (Back)

V evoluční strategii vstupuje do křížení pouze \(\rho\) vybraných rodičů a mezi metody jejich křížení patří:

- **diskrétní** - potomek dědí každou svou složku z náhodně zvoleného rodiče,

- **střední** - potomek vzniká jako průměr (po složkách) rodičů,

- **vážená** - potomek vzniká jako vážený průměr (po složkách) rodičů,

## Poznámka Anki 1733317643547

Karty Anki: 1733317643547
GUID: A0hSl$Qo34; štítky: ni-kop::p10 ni-spol::14.

### Otázka (Front)

Popište genetické programování a jeho obecnou strukturu. Jaký má v genetickém programování význam zdatnost?

### Odpověď (Back)

Genetické programování patří mezi evoluční algoritmy. Vyznačuje se následujícími vlastnostmi:

- **kódování jedince** - strom výrazu nebo výpočtu programu,

- **křížení **- dominující operátor (výměna podstromů),

- **mutace **- upozaděný operátor (nahrazení podstromu náhodně vygenerovaným podstromem),

- **řízení populace** - náhrada (en bloc, s elitismem nebo jiná).

Obecná struktura genetického programování se liší v tom, že před křížením probíhá výběr pro křížení a před selekcí testování jedinců. V tomto kontextu vyjadřuje zdatnost jedince funkčnost programu, který kóduje, a právě funkčnost je předmětem testů předcházejícím selekci. Fáze tedy jsou:

- testy a selekce,
- výběr pro křížení a křížení,
- mutace,
- řízení populace.

### Doplňující pole (Extra)

V kontextu genetického programování se křížení někdy nazývá rekombinace.

## Poznámka Anki 1733318418130

Karty Anki: 1733318418130
GUID: yQfv1$6/_L; štítky: ni-kop::p10 ni-spol::14.

### Otázka (Front)

Popište evoluční programování a jeho obecnou strukturu.

### Odpověď (Back)

Evoluční programování patří mezi evoluční algoritmy. Vyznačuje se následujícími vlastnostmi:

- **kódování jedince** - stavový stroj (např. automat, neuronová síť nebo program s pevnou strukturou);

- **křížení **- nepoužívá se, jedinec je chápán jako vlastní druh a vyvíjí se samostatně;

- **mutace **- změna počátečního stavu, změna výstupního symbolu, změna přechodu, přidání nebo odebrání stavu;

- **řízení populace** - soutěž \((\mu + \lambda)\) nebo turnajový výběr.

Obecná struktura evoluční strategie se liší v tom, že nepoužívá křížení. Fáze tedy jsou:

- selekce,
- mutace,
- řízení populace.

