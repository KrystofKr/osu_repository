# BI-PST – Cvičení 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 2 poznámek, 2 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1698856642248

Karty Anki: 1698856642248
GUID: hJeN0C8Z~?; štítky: bi-pst::c06.

### Otázka (Front)

Vyslovte větu o transformaci diskrétní náhodné veličiny.

### Odpověď (Back)

Mějme diskrétní náhodnou veličinu \(X\). Pro pravděpodobnostní funkci \(Y = t(X)\) platí
\[\operatorname P(Y = y_k) = \displaystyle \sum_{x_k \in t^{-1}(y_k)} \operatorname P(X = x_k).\]Tedy pravděpodobnost \(y_k\) získáme jako součet pravděpodobností \(x_k\), které se zobrazí na \(y_k\).

## Poznámka Anki 1698857205389

Karty Anki: 1698857205389
GUID: O8IzO8tk79; štítky: bi-pst::c06.

### Otázka (Front)

Vyslovte větu o transformaci spojité náhodné veličiny.

### Odpověď (Back)

Mějme spojitou náhodnou veličinu \(X\) se spojitou distribuční funkcí \(F\) a nechť pro každé \(x \in \mathbb R\) s výjimkou nanejvýše konečně mnoha bodů existuje její derivace \(F'(x)\). Dále mějme spojitou ryze monotonní funkci \(t\), která má derivaci \(t'(x)\) pro všechna \(x \in \mathbb R\). Pak pro pravděpodobnostní funkci \(Y = t(X)\) platí
\[f_Y(y) = f_X\big(t^{-1}(y)\big)\cdot \big|(t^{-1})'(y)\big|\]a navíc
\[F_Y(y) = \begin{cases}
F_X \big(t^{-1}(y) \big), && \text{pro } t \text{ rostoucí}, \\
1 - F_X \big(t^{-1}(y)\big), && \text{pro } t \text{ klesající}.
\end{cases}\]

