# BI-PST – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1701252760047

Karty Anki: 1701252760047
GUID: BZ+@t_0r|!; štítky: bi-pst::p10 bi-spol::27.

Metadata původního zdroje pro kartu 1701252760047: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte interval spolehlivosti, jeho dolní a horní meze a hladinu spolehlivosti.

### Odpověď (Back)

Nechť \(X_1, \dots, X_n\) je náhodný výběr z rozdělení určeného parametrem \(\theta\). Interval \((L, U)\) s krajními body určenými statistikami\[\begin{matrix}
L \equiv L(\mathbf X) \equiv L(X_1, \dots, X_n), \\
U \equiv U(\mathbf X) \equiv U(X_1, \dots, X_n) \\
\end{matrix}\]splňující\[\operatorname P(L < \theta < U) = 1 - \alpha\]se nazývá \(100 \cdot (1 - \alpha)\%\) **interval spolehlivosti** (připadně konfidenční interval). Statistika \(L\) resp. \(U\) se nazývá **dolní** resp. **horní mez intervalu spolehlivosti**. Číslo \((1 - \alpha)\) se nazývá **hladina spolehlivosti**.

## Poznámka Anki 1701253229252

Karty Anki: 1701253229252
GUID: w.2m6Uvdjw; štítky: bi-pst::p10 bi-spol::27.

### Otázka (Front)

Vyslovte větu o oboustranném a jednostranném intervalu spolehlivosti pro střední hodnotu při známém rozptylu.

### Odpověď (Back)

Mějme náhodný výběr \(X_1, \dots X_n\) z normálního rozdělení \(\operatorname N(\mu, \sigma^2)\) a předpokládejme, že známe rozptyl \(\sigma^2\). **Oboustranný** \(100 \cdot (1 - \alpha)\%\) **interval spolehlivosti** pro \(\mu\) je\[\Big( \bar X_n - z_{\frac \alpha 2} \frac \sigma {\sqrt n}, \bar X_n + z_{\frac \alpha 2} \frac \sigma {\sqrt n} \Big),\]kde \(z_{\frac \alpha 2} = \Phi^{-1} \big( 1 - \frac \alpha 2 \big)\) je kritická hodnota standardního normálního rozdělení, tj. číslo, pro které platí\[\operatorname P(Z > z_{\frac \alpha 2}) = \frac \alpha 2\]pro \(Z \sim \operatorname N(0, 1)\). **Jednostranné **\(100 \cdot (1 - \alpha)\%\) **intervaly spolehlivosti** pro \(\mu\) jsou pak\[\begin{matrix}
\Big( \bar X_n - z_\alpha \frac \sigma {\sqrt n}, +\infty \Big), \\
\Big( -\infty, \bar X_n + z_\alpha \frac \sigma {\sqrt n} \Big)
\end{matrix}\]při stejném značení.

## Poznámka Anki 1701255557356

Karty Anki: 1701255557357
GUID: M*iJ>)x}k.; štítky: bi-pst::p10 bi-spol::27.

Metadata původního zdroje pro kartu 1701255557357: modrý příznak autora: v poslední verzi upraveno.

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

## Poznámka Anki 1701256764794

Karty Anki: 1701256764794
GUID: QF++B!<bQK; štítky: bi-pst::p10 bi-spol::27.

### Otázka (Front)

Vyslovte větu o oboustranném a jednostranném intervalu spolehlivosti pro rozptyl.

### Odpověď (Back)

Mějme náhodný výběr \(X_1, \dots X_n\) z normálního rozdělení \(\operatorname N(\mu, \sigma^2)\). **Oboustranný** \(100 \cdot (1 - \alpha)\%\) **interval spolehlivosti** pro \(\sigma^2\) je\[\bigg( \frac {(n - 1)s_n^2} {\chi_{\frac \alpha 2, n - 1}^2 }, \frac {(n - 1)s_n^2} {\chi_{1 - \frac \alpha 2, n - 1}^2,  } \bigg),\]kde \(\chi_{\frac \alpha 2, n - 1}^2\) je kritická hodnota rozdělení \(\chi^2\) s \(n - 1\) stupni volnosti, tj. číslo, pro které platí\[\operatorname P(X > \chi_{\frac \alpha 2, n - 1}^2) = \frac \alpha 2\]pro \(X \sim \chi_{n - 1}^2\). **Jednostranné **\(100 \cdot (1 - \alpha)\%\) **intervaly spolehlivosti** pro \(\sigma^2\) jsou pak\[\begin{matrix}
\Big( \frac {(n - 1)s_n^2} {\chi_{\alpha, n - 1}^2 }, +\infty \Big), \\
\Big( 0, \frac {(n - 1)s_n^2} {\chi_{1 - \alpha, n - 1}^2,  } \Big)
\end{matrix}\]při stejném značení.

