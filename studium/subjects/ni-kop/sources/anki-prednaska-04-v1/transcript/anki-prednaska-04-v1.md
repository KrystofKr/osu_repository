# NI-KOP – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1728911735329

Karty Anki: 1728911735329
GUID: h{Z4JB]d(X; štítky: ni-kop::p04 ni-spol::11.

### Otázka (Front)

Popište \(\text X\)-těžký (\(\text X\)-hard) problém.

### Odpověď (Back)

Problém \(\Pi\) je \(\text X\)-těžký (\(\text X\)-hard), jestliže se efektivní řešení všech problémů třídy \(\text X\) dá polynomiálně redukovat na efektivní řešení problému \(\Pi\).

### Doplňující pole (Extra)

Efektivním řešením se rozumí řešení s omezenou chybou nebo polynomiální časovou složitostí.

## Poznámka Anki 1728911861145

Karty Anki: 1728911861145
GUID: Ee(]$jUxnG; štítky: ni-kop::p04 ni-spol::11.

### Otázka (Front)

Popište \(\text X\)-úplný (\(\text X\)-complete) problém.

### Odpověď (Back)

Problém \(\Pi\) je \(\text X\)-úplný (\(\text X\)-complete), jestliže je \(\text X\)-těžký a sám patří do třídy \(\text X\).

## Poznámka Anki 1728912360166

Karty Anki: 1728912360166
GUID: BsfCqAyWV=; štítky: ni-kop::p04 ni-spol::11.

### Otázka (Front)

Definujte Karpovu redukci (many-one reduction) a Karp-redukovatelný problém.

### Odpověď (Back)

**Karpova redukce** (many-one reduction) je typ polynomiální redukce, která je speciálním případem Turingovy redukce v polynomiálním čase. Rozhodovací problém \(\Pi_1\) je **Karp-redukovatelný** na \(\Pi_2\), jestliže existuje polynomiální program pro deterministický Turingův stroj, který převede každou instanci \(I_1\) problému \(\Pi_1\) na instanci \(I_2\) problému \(\Pi_2\) tak, že výstup obou instancí je shodný. Tuto skutečnost značíme \(\Pi_1 \propto \Pi_2\).

## Poznámka Anki 1728912505465

Karty Anki: 1728912505465
GUID: j*D,+4MOj4; štítky: ni-kop::p04.

### Otázka (Front)

Definujte polynomiálně ekvivalentní rozhodovací problémy.

### Odpověď (Back)

Rozhodovací problémy \(\Pi_1\) a \(\Pi_2\) nazveme polynomiálně ekvivalentní, jestliže platí\[\Pi_1 \propto \Pi_2 \quad \land \quad \Pi_2 \propto \Pi_1.\]

## Poznámka Anki 1728912651717

Karty Anki: 1728912651717
GUID: nmsGnDeck:; štítky: ni-kop::p04 ni-spol::11.

### Otázka (Front)

Vyslovte Cookovu větu.

### Odpověď (Back)

Problém splnitelnosti Booleovy formule (SAT) je \(\text{NP}\)-úplný.

## Poznámka Anki 1728913341147

Karty Anki: 1728913341148
GUID: pyM>y]:ApU; štítky: ni-kop::p04.

### Otázka (Front)

Definujte řešení optimalizačního problému deterministickým Turingovým strojem.

### Odpověď (Back)

Program \(M\) pro deterministický Turingův stroj řeší optimalizační problém \(\Pi\) resp. počítá optimalizační kritérium problému \(\Pi\) v čase \(t\), jestliže se výpočet zastaví po nejvýše \(t\) krocích pro každou instanci problému \(\Pi\), která má řešení, a na pásce Turingova stroje je zapsán výstup instance resp. hodnota optimalizačního kritéria.

## Poznámka Anki 1728913725351

Karty Anki: 1728913725351
GUID: OV;pq3,`pg; štítky: ni-kop::p04.

### Otázka (Front)

Definujte třídu \(\text{NPO}\). Jaký je její vztah k třídě \(\text{APX}\)?

### Odpověď (Back)

Optimalizační problém \(\Pi\) patří do třídy \(\text{NPO}\), jestliže splňuje následující podmínky:

- velikost výstupu instance je omezena polynomem závislým na velikosti instance;
- problém kontroly, že daná konfigurace je řešením instance, patří do \(\text P\);
- existuje program pro Turingův stroj, který spočte hodnotu optimalizačního kritéria pro každé řešení každé instance v polynomiálním čase.

Platí, že \(\text{NPO} \supset \text{APX}\).

### Doplňující pole (Extra)

Jinými slovy:

- výstup lze zapsat v polynomiálním čase,
- omezení lze vyhodnotit v polynomiálním čase,
- optimalizační kritérium lze vyhodnotit v polynomiálním čase.

## Poznámka Anki 1728913810343

Karty Anki: 1728913810343
GUID: cL0H/n<F&Z; štítky: ni-kop::p04.

### Otázka (Front)

Definujte třídu \(\text{PO}\). Jaký je její vztah k třídě \(\text{FPTAS}\)?

### Odpověď (Back)

Optimalizační problém \(\Pi\) patří do třídy \(\text{PO}\), jestliže splňuje následující podmínky:

- patří do \(\text{NPO}\),
- existuje program pro Turingův stroj, který každou jeho instanci vyřeší v polynomiálním čase.

Platí, že \(\text{PO} \subset \text{FPTAS}\).

## Poznámka Anki 1728914413681

Karty Anki: 1728914413681
GUID: QNRc*)Su=O; štítky: ni-kop::p04 ni-spol::11.

### Otázka (Front)

Definujte Turingovu redukci a Turing-redukovatelný problém.

### Odpověď (Back)

**Turingova redukce** je typ redukce problémů. Problém \(\Pi_1\) je **Turing-redukovatelný na **\(\Pi_2\), jestliže existuje program pro deterministický Turingův stroj, který řeší každou instanci \(I_1\) problému \(\Pi_1\) tak, že používá program \(M_2\) pro problém \(\Pi_2\) jako podprogram. Tuto skutečnost značíme \(\Pi_1 \underline \propto \Pi_2\)

### Doplňující pole (Extra)

Turingova redukce nemusí probíhat v polynomiálním čase. Takovou redukci pak nazveme Cookovou redukcí.

## Poznámka Anki 1728916035550

Karty Anki: 1728916035550
GUID: uLIDQtG+N5; štítky: ni-kop::p04.

### Otázka (Front)

Definujte optimalizační problém obchodního cestujícího (TSO).

### Odpověď (Back)

Optimalizační problém obchodního cestujícího (TSO) je kombinatorický problém. Na vstupu je dána množina \(n \) měst \(C = \{ c_1, \dots, c_n \}\) a pro každé dvě města je dána jejich vzdálenost \(d(c_i, c_j)\). Cílem je nalézt uzavřenou túru, která prochází každým městem právě jednou a má nejmenší možnou délku. Optimalizační problém obchodního cestujícího patří do třídy \(\text{NPO}\).

## Poznámka Anki 1728916300519

Karty Anki: 1728916300519
GUID: pw3+AnM@z8; štítky: ni-kop::p04 ni-spol::11.

### Otázka (Front)

Definujte \(\text{NP}\)-těžký (\(\text{NP}\)-hard) problém pomocí Turingovy redukce.

### Odpověď (Back)

Problém \(\Pi\) je \(\text{NP}\)-těžký (\(\text{NP}\)-hard), jesltiže pro všechny problémy \(\Pi' \in \text{NP}\) platí
\[\Pi' \underline \propto \Pi\]v polynomiálním čase.

### Doplňující pole (Extra)

Definici lze postavit i na Karpově redukci, ta je však omezena pouze na rozhodovací problémy.

## Poznámka Anki 1728916943667

Karty Anki: 1728916943667
GUID: jna{U^&V];; štítky: ni-kop::p04 ni-spol::11.

### Otázka (Front)

Definujte třídu \(\text{NP}\)-intermediate (NPI).

### Odpověď (Back)

Problém \(\Pi\) patří do třídy \(\text{NP}\)-intermediate** **(NPI), jestliže splňuje následující podmínky:

- patří do třídy \(\text{NP}\),
- nepatří do třídy \(\text P\),
- není \(\text{NP}\)-úplný.

## Poznámka Anki 1728922533142

Karty Anki: 1728922533142
GUID: G:#rGll}iu; štítky: ni-kop::p04 ni-spol::11.

### Otázka (Front)

Definujte \(\text{NP}\)-úplný (\(\text{NP}\)-complete) pomocí Karpovy redukce.

### Odpověď (Back)

Problém \(\Pi\) je \(\text{NP}\)-úplný (\(\text{NP}\)-complete), jestliže:

- patří do třídy \(\text{NP}\),
- pro všechny problémy \(\Pi' \in \text{NP}\) platí \(\Pi' \propto \Pi\).

