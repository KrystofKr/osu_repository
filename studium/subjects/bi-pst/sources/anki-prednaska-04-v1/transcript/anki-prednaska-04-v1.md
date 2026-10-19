# BI-PST – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1697620198189

Karty Anki: 1697620198189
GUID: n;Du`z_?S|; štítky: bi-pst::p04 bi-spol::26.

Metadata původního zdroje pro kartu 1697620198189: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte střední hodnotu spojité náhodné veličiny.

### Odpověď (Back)

Střední hodnota spojité náhodné veličiny \(X\) s hustotou \(f\) je určena vztahem\[\operatorname E \, X = \displaystyle \int_{-\infty}^{+\infty} x \cdot f(x) \, \text dx.\]Nutnou podmínkou je, že tento integrál absolutně konverguje. Jinak říkáme, že střední hodnota náhodné veličiny \(X\) neexistuje.

## Poznámka Anki 1697620507996

Karty Anki: 1697620507997
GUID: EW`V^H)LK8; štítky: bi-pst::p04.

Metadata původního zdroje pro kartu 1697620507997: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte střední hodnotu diskrétní náhodné veličiny.

### Odpověď (Back)

Střední hodnota diskrétní náhodné veličiny \(X\), nabývající hodnot \(x_1, x_2, \dots\), je průměr všech hodnot veličiny \(X\) vážený pravděpodobnostmi příslušných elementárních jevů, tedy\[\operatorname E \, X = \displaystyle \sum_{x \in \mathcal X} x \cdot \text P(X = x_k).\]Nutnou podmínkou je, že uvedená suma konverguje. Jinak říkáme, že střední hodnota náhodné veličiny \(X\) neexistuje.

## Poznámka Anki 1697621034020

Karty Anki: 1697621034020
GUID: TwvP~MxhT; štítky: bi-pst::p04 bi-spol::26.

### Otázka (Front)

Vyslovte větu o vlastnostech střední hodnoty.

### Odpověď (Back)

Střední hodnota náhodné veličiny \(X\) splňuje následující vlastnosti:

- Je-li \(X \geq 0\), pak \(\operatorname E(X) \geq 0\).
- Je-li \(a, b \in \mathbb R\), pak \(\operatorname E(a X + b) = a \operatorname E(X) + b\).
- Je-li \(X = c \in \mathbb R\), pak \(\operatorname E(X) = c\).

## Poznámka Anki 1697621501160

Karty Anki: 1697621501160
GUID: yKqfPItx@6; štítky: bi-pst::p04 bi-spol::26.

Metadata původního zdroje pro kartu 1697621501160: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte rozptyl (varianci) náhodné veličiny.

### Odpověď (Back)

Rozptyl (variance) náhodné veličiny \(X\) je definován vztahem\[\operatorname{var} X = \operatorname  E \big((X - \operatorname E X)^2 \big) = \operatorname E X^2 - (\operatorname E X)^2. \]

## Poznámka Anki 1697621568161

Karty Anki: 1697621568161
GUID: H3`?T]gF$u; štítky: bi-pst::p04 bi-spol::26.

Metadata původního zdroje pro kartu 1697621568161: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte směrodatnou odchylku náhodné veličiny.

### Odpověď (Back)

Směrodatná odchylka náhodné veličiny \(X\) je definována jako\[\operatorname{sd} X = \sqrt{\operatorname{var} X}.\]

## Poznámka Anki 1697623697021

Karty Anki: 1697623697021
GUID: y|#X6hPRJ5; štítky: bi-pst::p04.

Metadata původního zdroje pro kartu 1697623697021: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte \(\alpha\)-kritickou hodnotu.

### Odpověď (Back)

\(\alpha\)-kritickou \(c_\alpha\) hodnotou nazýváme \((1 - \alpha)\)-kvantil, tedy\[c_\alpha = q_{1 - \alpha}.\]

## Poznámka Anki 1716216154129

Karty Anki: 1716216154130
GUID: owbn/?xu7[; štítky: bi-pst::p04 bi-spol::27.

Metadata původního zdroje pro kartu 1716216154130: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte obecné momenty.

### Odpověď (Back)

Pro \(k \in \mathbb N\), přirozené číslo, definujeme \(k\)-tý moment náhodné veličiny jako\[\mu_k = \operatorname E(X^k) = \begin{cases}
\displaystyle \sum_{x \in \mathcal X} x^k \operatorname P(X = x) && \text{pro } X \text{ diskrétní},\\
\displaystyle \int_{-\infty}^{\infty} x^k f_X(x) \, \mathrm dx && \text{pro } X \text{ spojitou}.
\end{cases}\]Podobně, \(k\)-tý centrální moment je\[\sigma_k = \operatorname E(X - \operatorname EX)^k = \begin{cases}
\displaystyle \sum_{x \in \mathcal X} (x - \mu_1)^k \operatorname P(X = x) && \text{pro } X \text{ diskrétní},\\
\displaystyle \int_{-\infty}^{\infty} (x - \mu_1)^k f_X(x) \, \mathrm dx && \text{pro } X \text{ spojitou}.
\end{cases}\]

