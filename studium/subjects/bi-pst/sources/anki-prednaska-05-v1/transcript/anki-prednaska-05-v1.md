# BI-PST – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1698226140855

Karty Anki: 1698226140855
GUID: M0HgL;^SE6; štítky: bi-pst::p05 bi-spol::26.

Metadata původního zdroje pro kartu 1698226140855: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte Bernoulliho (alternativní) rozdělení.

### Odpověď (Back)

Diskrétní náhodná veličina \(X\) má Bernoulliho (alternativní) rozdělení s parametrem \(p \in \langle 0, 1 \rangle\), jestliže\[\operatorname P(X = 1) = p, \quad \operatorname P(X = 0) = 1 - p.\]Značíme \(X \sim \operatorname{Be}(p)\) či \(X \sim \operatorname{Bernoulli}(p)\) nebo také \(X \sim \operatorname{Alt}(p)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = p, \\
\operatorname{var}(X) = p(1-p).
\end{matrix}\]

### Doplňující pole (Extra)

Bernoulliho (alternativní) rozdělení využijeme, pokud máme náhodný experiment se dvěma možnými výsledky a úspěch nastává s pravděpodobností \(p\).

## Poznámka Anki 1698226631708

Karty Anki: 1698226631709
GUID: p};L6-ZY[2; štítky: bi-pst::p05 bi-spol::26.

Metadata původního zdroje pro kartu 1698226631709: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte binomické rozdělení.

### Odpověď (Back)

Diskrétní náhodná veličina \(X\) má binomické rozdělení s parametry \(n \in \mathbb N\) a \(p \in \langle 0, 1 \rangle\), jestliže\[\operatorname P(X = k) = {n \choose k} p^k (1 - p)^{n - k}, \quad k = 0, 1, \dots, n.\]Značíme \(X \sim \operatorname{Binom}(n,p)\) nebo \(X \sim \operatorname{Bin}(n, p)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = np, \\
\operatorname{var}(X) = np(1-p).
\end{matrix}\]

### Doplňující pole (Extra)

Binomické rozdělení využijeme, pokud uvažujeme \(n\) nezávislých pokusů se dvěma možnými výsledky, předpokládáme, že pravděpodobnost úspěchu je \(p\) a úspěch nastává právě \(k\)-krát.

## Poznámka Anki 1698226997267

Karty Anki: 1698226997268
GUID: J(H&Cmu>oy; štítky: bi-pst::p05 bi-spol::26.

Metadata původního zdroje pro kartu 1698226997268: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte geometrické rozdělení.

### Odpověď (Back)

Diskrétní náhodná veličina \(X\) má geometrické rozdělení s parametrem \(p \in (0, 1)\), jestliže\[\operatorname P(X = k) = (1 - p)^{k - 1} p, \quad k = 1, 2, \dots\]Značíme \(X \sim \operatorname{Geom}(p)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = \displaystyle \frac 1 p, \\
\operatorname{var}(X) = \displaystyle  \frac {1 - p} {p^2}.
\end{matrix}\]

### Doplňující pole (Extra)

Geometrické rozdělení využijeme v případě, že uvažujeme posloupnost nezávislých pokusů se dvěma možnými výsledky. Předpokládáme, že pravděpodobnost úspěchu je \(p\) a zajímá nás pravděpodobnost, že první úspěšný pokus je \(k\)-tý pokus v pořadí.

## Poznámka Anki 1698227544833

Karty Anki: 1698227544833
GUID: sFpcH)$V>I; štítky: bi-pst::p05 bi-spol::26.

Metadata původního zdroje pro kartu 1698227544833: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte Poissonovo rozdělení.

### Odpověď (Back)

Diskrétní náhodná veličina \(X\) má Poissonovo rozdělení s parametrem \(\lambda > 0\), jestliže\[\operatorname P(X = k) = \frac {\lambda^k} {k!} e^{- \lambda}, \quad k = 0, 1, \dots.\]Značíme \(X \sim \operatorname{Poisson}(\lambda)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = \lambda, \\
\operatorname{var}(X)= \lambda.
\end{matrix}\]

### Doplňující pole (Extra)

Poissonovo rozdělení využijeme, pokud zkoumáme počet realizací náhodných údálostí řídkého jevu během určité doby. Počítá s výrazně vyšším počtem pokusů než realizací.

## Poznámka Anki 1698228733343

Karty Anki: 1698228733344
GUID: GFx:BF2Z=c; štítky: bi-pst::p05 bi-spol::26.

Metadata původního zdroje pro kartu 1698228733344: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte rovnoměrné (uniformní) rozdělení.

### Odpověď (Back)

Spojitá náhodná veličina \(X\) má rovnoměrné (uniformní) rozdělení na intervalu \((a, b)\), kde \(a < b\), jestliže\[f_X(x) = \begin{cases}
\displaystyle \frac 1 {b - a} && \text{pro } x \in (a, b), \\
0 && \text{jinde}.
\end{cases}\]Značíme \(X \sim \operatorname{Unif}(a, b)\) nebo \(X \sim \operatorname U(a, b)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = \displaystyle  \frac {a + b} 2, \\
\operatorname{var}(X) = \displaystyle \frac{(b - a)^2} {12}.
\end{matrix}\]

### Doplňující pole (Extra)

Rovnoměrné rozdělení použijeme, pokud sledujeme jevy, jejichž pravděpodobnost je rovnoměrně rozdělena na intervalu \((a, b)\).

## Poznámka Anki 1698229103080

Karty Anki: 1698229103080
GUID: jK-W3L++;C; štítky: bi-pst::p05 bi-spol::26.

Metadata původního zdroje pro kartu 1698229103080: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte exponenciální rozdělení.

### Odpověď (Back)

Spojitá náhodná veličina \(X\) má exponenciální rozdělení s parametrem \(\lambda >0\), jestliže:\[f_X(x) = \begin{cases}
\lambda e^{- \lambda x} && \text{pro } x \in \langle 0, +\infty), \\
0 && \text{jinde}.
\end{cases}\]Značíme \(X \sim \operatorname{Exp}(\lambda)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = \displaystyle \frac 1 \lambda, \\
\operatorname{var}(X) = \displaystyle \frac 1 {\lambda^2}.
\end{matrix}\]

### Doplňující pole (Extra)

Exponenciální rozdělení využijeme, pokud modelujeme čas mezi dvěma událostmi s Poissonovským rozdělením.

## Poznámka Anki 1698229752926

Karty Anki: 1698229752927
GUID: h:;,#t`#6D; štítky: bi-pst::p05 bi-spol::26.

Metadata původního zdroje pro kartu 1698229752927: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte normální (Gaussovo) rozdělení.

### Odpověď (Back)

Spojitá náhodná veličina \(X\) má normální (Gaussovo) rozdělení s parametry \(\mu \in \mathbb R\) a \(\sigma^2 > 0\), jestliže\[f_X(x) = \frac 1 {\sqrt{2 \pi \sigma^2}} e^{- \frac {(x - \mu)^2} {2 \sigma^2}}, \quad x \in (- \infty, +\infty).\]Značíme \(X \sim \operatorname N(\mu, \sigma^2)\) a \(\operatorname N(0, 1) \) nazýváme standardním normálním rozdělením. Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = \mu, \\
\operatorname{var}(X) = \sigma^2.
\end{matrix}\]

### Doplňující pole (Extra)

Normální (Gaussovo) rozdělení využijeme, pokud modelujeme veličiny pozorovatelné v přírodě jako např. výška nebo váha.

## Poznámka Anki 1698833843557

Karty Anki: 1698833843557
GUID: p`4ASb,b?c; štítky: bi-pst::p05 bi-spol::26.

### Otázka (Front)

Vyslovte větu o standardizaci normální náhodné veličiny.

### Odpověď (Back)

Mějme náhodnou veličinu \(X\) s normálním rozdělením \(X \sim \operatorname N(\mu, \sigma^2)\). Pak náhodná veličina
\[Z = \frac {X - \mu} \sigma\]má standardní normální rozdělení, tedy \(Z \sim \operatorname N(0, 1)\) a platí
\[F_X(x) = \operatorname P\Big(Z \leq \frac {x - \mu} \sigma\Big) = \Phi\Big(\frac {x - \mu} \sigma\Big).\]

