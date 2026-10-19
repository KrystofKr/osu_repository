# NI-VSM – Přednáška 09

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-VSM
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1742155300390

Karty Anki: 1742155300390
GUID: j3R]s+a35h; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Definujte náhodný výběr.

### Odpověď (Back)

Náhodným výběrem z rozdělení \(F\) nazveme \(n\)-tici i.i.d. náhodných veličin \(X_1, \dots, X_n\) s distribuční funkcí \(F\).

## Poznámka Anki 1742155523612

Karty Anki: 1742155523612
GUID: HeHGJe#G.~; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Popište typy hypotéz.

### Odpověď (Back)

Hypotézy rozdělujeme na dva druhy:

- **neparametrické** - tvrzení týkající se vlastností rozdělení nebo jeho tvaru (testy dobré shody), používají výběr z obecného rozdělení;

- **parametrické** - tvrzení týkající se hodnoty parametru \(\theta \in \mathbb R^d\), používají náhodný výběr z rozdělení s parametrem \(\theta\).

## Poznámka Anki 1742155559669

Karty Anki: 1742155559669
GUID: AEr.}rEQ0+; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Definujte bodový odhad.

### Odpověď (Back)

Bodový odhad parametru \(\theta\) je funkce \(\hat \theta_n(X_1, \dots X_n)\) náhodného výběru, která nezávisí na hodnotách \(\theta\).

## Poznámka Anki 1742155646398

Karty Anki: 1742155646398
GUID: n~Pa_B$KGT; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Popište výběrový průměr.

### Odpověď (Back)

Výběrový průměr se používá jako bodový odhad střední hodnoty \(\operatorname E X\). Spočíst lze pomocí následujícího vzorce:\[\bar X_n = \frac 1 n \displaystyle \sum_{i = 1}^n X_i.\]

## Poznámka Anki 1742155663591

Karty Anki: 1742155663591
GUID: z1rn!NTbj(; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Popište výběrový rozptyl.

### Odpověď (Back)

Výběrový rozptyl se používá jako bodový odhad rozptylu \(\operatorname{var} X\). Spočíst lze pomocí následujícího vzorce:\[s_n^2 = s_X^2 = \frac 1 {n - 1} \displaystyle \sum_{i = 1}^n(X_i - \bar X_n)^2 = \frac 1 {n - 1} \Big( \displaystyle \sum_{i = 1}^n X_i^2 - n\bar X_n^2 \Big).\]

## Poznámka Anki 1742155688128

Karty Anki: 1742155688128
GUID: Q~7;(Z]6$H; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Popište výběrovou kovarianci.

### Odpověď (Back)

Výběrová kovariance se používá jako bodový odhad kovariance \(\operatorname{cov}(X, Y)\). Spočíst ji lze pomocí následujícího vzorce:\[s_{X, Y} = \frac 1 {n - 1} \displaystyle \sum_{i = 1}^n (X_i - \bar X_n)(Y_i - \bar Y_n) = \frac 1 {n - 1} \Big( \displaystyle \sum_{i  =1}^n X_i Y_i - n \bar X_n \bar Y_n \Big).\]

## Poznámka Anki 1742155710657

Karty Anki: 1742155710657
GUID: z,!>?Bw/2;; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Popište výběrový korelační koeficient.

### Odpověď (Back)

Výběrový korelační koeficient se používá jako bodový odhad korelačního koeficientu \(\operatorname \rho(X, Y)\). Spočíst ho lze pomocí následujícího vzorce:\[r_{X, Y} = \frac {s_{X, Y}} {s_X s_Y}.\]

## Poznámka Anki 1742155789626

Karty Anki: 1742155789626
GUID: lqxt]JF5b; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Definujte nestranný (nevychýlený) odhad.

### Odpověď (Back)

Odhad \(\hat \theta_n\) parametru \(\theta\) nazveme nestranný (nevychýlený), jestliže pro všechna \(\theta \in \Theta\) platí\[\operatorname E \hat \theta_n = \theta.\]

## Poznámka Anki 1742155873024

Karty Anki: 1742155873024
GUID: NGwY;b(l9g; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Definujte konzistentní odhad.

### Odpověď (Back)

Odhad \(\hat \theta_n\) parametru \(\theta\) se nazývá konzistentní, jestliže pro každé \(\theta \in \Theta\) platí\[\hat \theta_n \xrightarrow{\operatorname P} \theta \quad \text{pro} \quad n \to +\infty.\]To znamená, že pro každé \(\varepsilon > 0\) a \(\theta \in \Theta\) platí\[\displaystyle \lim_{n \to +\infty} \operatorname P(|\hat \theta_n(X_1, \dots, X_n) - \theta| \geq \varepsilon) = 0.\]

## Poznámka Anki 1742156152535

Karty Anki: 1742156152535
GUID: CbCf3Dl260; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Definujte nejlepší nestranný odhad.

### Odpověď (Back)

Odhad \(\hat \theta_n^*(X_1, \dots, X_n)\) se nazývá nejlepší nestranný odhad parametru \(\theta\), pokud je nestranný a pro každý jiný nestranný odhad \(\hat \theta_n\) platí, že pro všechna \(\theta \in \Theta\)\[\operatorname{var}(\hat \theta_n) \geq \operatorname{var}(\hat \theta_n^*).\]

## Poznámka Anki 1742156356359

Karty Anki: 1742156356359
GUID: Itb^HW0.o`; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Definujte interval spolehlivosti, jeho dolní a horní meze a hladinu spolehlivosti.

### Odpověď (Back)

Nechť \(X_1, \dots, X_n\) je náhodný výběr z rozdělení určeného parametrem \(\theta\). Interval \((L, U)\) s krajními body určenými statistikami\[\begin{matrix}
L \equiv L(\mathbf X) \equiv L(X_1, \dots, X_n), \\
U \equiv U(\mathbf X) \equiv U(X_1, \dots, X_n) \\
\end{matrix}\]splňující\[\operatorname P(L < \theta < U) = 1 - \alpha\]se nazývá \(100 \cdot (1 - \alpha)\%\) **interval spolehlivosti** (připadně konfidenční interval). Statistika \(L\) resp. \(U\) se nazývá **dolní** resp. **horní mez intervalu spolehlivosti**. Číslo \((1 - \alpha)\) se nazývá **hladina spolehlivosti**.

## Poznámka Anki 1742156581228

Karty Anki: 1742156581229
GUID: kcbQN&igO[; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Vyslovte větu o oboustranném a jednostranném intervalu spolehlivosti pro střední hodnotu při známém rozptylu.

### Odpověď (Back)

Mějme náhodný výběr \(X_1, \dots X_n\) z normálního rozdělení \(\operatorname N(\mu, \sigma^2)\) a předpokládejme, že známe rozptyl \(\sigma^2\). **Oboustranný** \(100 \cdot (1 - \alpha)\%\) **interval spolehlivosti** pro \(\mu\) je\[\Big( \bar X_n - z_{\frac \alpha 2} \frac \sigma {\sqrt n}, \bar X_n + z_{\frac \alpha 2} \frac \sigma {\sqrt n} \Big),\]kde \(z_{\frac \alpha 2} = \Phi^{-1} \big( 1 - \frac \alpha 2 \big)\) je kritická hodnota standardního normálního rozdělení, tj. číslo, pro které platí\[\operatorname P(Z > z_{\frac \alpha 2}) = \frac \alpha 2\]pro \(Z \sim \operatorname N(0, 1)\). **Jednostranné **\(100 \cdot (1 - \alpha)\%\) **intervaly spolehlivosti** pro \(\mu\) jsou pak\[\begin{matrix}
\Big( \bar X_n - z_\alpha \frac \sigma {\sqrt n}, +\infty \Big), \\
\Big( -\infty, \bar X_n + z_\alpha \frac \sigma {\sqrt n} \Big)
\end{matrix}\]při stejném značení.

## Poznámka Anki 1742156625021

Karty Anki: 1742156625021
GUID: gBu^^&e&^{; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Vyslovte větu o oboustranném a jednostranném intervalu spolehlivosti pro střední hodnotu při neznámém rozptylu.

### Odpověď (Back)

Mějme náhodný výběr \(X_1, \dots X_n\) z normálního rozdělení \(\operatorname N(\mu, \sigma^2)\). **Oboustranný** \(100 \cdot (1 - \alpha)\%\) **interval spolehlivosti** pro \(\mu\) je
\[\Big( \bar X_n - t_{\frac \alpha 2, n - 1} \frac {s_n} {\sqrt n}, \bar X_n + t_{\frac \alpha 2, n - 1} \frac {s_n} {\sqrt n} \Big),\]kde \(t_{\frac \alpha 2, n - 1} \) je kritická hodnota Studentova \(\operatorname t\)-rozdělení s \(n - 1\) stupni volnosti, tj. číslo, pro které platí
\[\operatorname P(X > t_{\frac \alpha 2, n - 1}) = \frac \alpha 2\]
pro \(X\) se Studentovým \(\operatorname t\)-rozdělením s \(n - 1\) stupni volnosti. **Jednostranné **\(100 \cdot (1 - \alpha)\%\) **intervaly spolehlivosti** pro \(\mu\) jsou pak\[\begin{matrix}
\Big( \bar X_n - t_{\alpha, n - 1} \frac {s_n} {\sqrt n}, +\infty \Big), \\
\Big( -\infty, \bar X_n + t_{\alpha, n - 1} \frac {s_n} {\sqrt n} \Big)
\end{matrix}\]při stejném značení.

## Poznámka Anki 1742156805631

Karty Anki: 1742156805631
GUID: jL(ofqopw:; štítky: duplicate ni-vsm::p09.

### Otázka (Front)

Vyslovte větu o oboustranném a jednostranném intervalu spolehlivosti pro rozptyl.

### Odpověď (Back)

Mějme náhodný výběr \(X_1, \dots X_n\) z normálního rozdělení \(\operatorname N(\mu, \sigma^2)\). **Oboustranný** \(100 \cdot (1 - \alpha)\%\) **interval spolehlivosti** pro \(\sigma^2\) je\[\bigg( \frac {(n - 1)s_n^2} {\chi_{\frac \alpha 2, n - 1}^2 }, \frac {(n - 1)s_n^2} {\chi_{1 - \frac \alpha 2, n - 1}^2,  } \bigg),\]kde \(\chi_{\frac \alpha 2, n - 1}^2\) je kritická hodnota rozdělení \(\chi^2\) s \(n - 1\) stupni volnosti, tj. číslo, pro které platí\[\operatorname P(X > \chi_{\frac \alpha 2, n - 1}^2) = \frac \alpha 2\]pro \(X \sim \chi_{n - 1}^2\). **Jednostranné **\(100 \cdot (1 - \alpha)\%\) **intervaly spolehlivosti** pro \(\sigma^2\) jsou pak\[\begin{matrix}
\Big( \frac {(n - 1)s_n^2} {\chi_{\alpha, n - 1}^2 }, +\infty \Big), \\
\Big( 0, \frac {(n - 1)s_n^2} {\chi_{1 - \alpha, n - 1}^2,  } \Big)
\end{matrix}\]při stejném značení.

