# BI-PST – Přednáška 12

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1702462740630

Karty Anki: 1702462740631
GUID: P@.RaLBWh@; štítky: bi-pst::p12 bi-spol::27.

### Otázka (Front)

Popište výběrovou kovarianci.

### Odpověď (Back)

Výběrová kovariance se používá jako bodový odhad kovariance \(\operatorname{cov}(X, Y)\). Spočíst ji lze pomocí následujícího vzorce:\[s_{X, Y} = \frac 1 {n - 1} \displaystyle \sum_{i = 1}^n (X_i - \bar X_n)(Y_i - \bar Y_n) = \frac 1 {n - 1} \Big( \displaystyle \sum_{i  =1}^n X_i Y_i - n \bar X_n \bar Y_n \Big).\]

## Poznámka Anki 1702464147224

Karty Anki: 1702464147224
GUID: F^lR|Sc/@W; štítky: bi-pst::p12.

### Otázka (Front)

Popište lineární regresní model.

### Odpověď (Back)

Lineární regresní model se používá pro popis lineární závislosti. Je dán vztahem
\[Y_i = \alpha + \beta x_i + \varepsilon_i, \quad i = 1, \dots, n.\]Předpokládáme, že

- \(x_i\) jsou dané hodnoty,

- \(\varepsilon_i\) jsou i.i.d. náhodné veličiny s nulovou střední hodnotu (experimentální chyby) často s \(\operatorname N(0, \sigma^2)\),

- \(\alpha\) a \(\beta\) jsou neznámé parametry.

## Poznámka Anki 1702464396020

Karty Anki: 1702464396020
GUID: OmIr!I^gQL; štítky: bi-pst::p12.

### Otázka (Front)

Popište, jak odhadnout parametry \(\alpha\) a \(\beta\) lineárního regresního modelu.

### Odpověď (Back)

Odhady \(a\) a \(b\) parametrů \(\alpha\) a \(\beta\) lineárního regresního modelu získáme metodou nejmenších čtverců jako
\[\begin{matrix}
b = \displaystyle \frac{ \sum_{i = 1}^n X_i Y_i - n \bar X_n \bar Y_n}{ \sum_{i = 1}^n X_i^2 - n \bar X_n^2} = \frac {s_{X, Y}} {s_X^2} = r_{X, Y} \frac {s_Y}{s_X}, \\
a = \bar Y_n - b \bar X_n.
\end{matrix}\]Potom jsou hodnoty
\[\hat Y_i = a + b \cdot x_i\]nejlepšími aproximacemi lineárního regresního modelu.

## Poznámka Anki 1702480539877

Karty Anki: 1702480539883
GUID: LbCun8I+o/; štítky: bi-pst::p12 bi-spol::27.

### Otázka (Front)

Popište výběrový korelační koeficient.

### Odpověď (Back)

Výběrový korelační koeficient se používá jako bodový odhad korelačního koeficientu \(\operatorname \rho(X, Y)\). Spočíst ho lze pomocí následujícího vzorce:\[r_{X, Y} = \frac {s_{X, Y}} {s_X s_Y}.\]

