# BI-PST – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1700042916811

Karty Anki: 1700042916811
GUID: i)cJ9SkhGJ; štítky: bi-pst::p08 bi-spol::26.

### Otázka (Front)

Vyslovte větu o Markovově nerovnosti.

### Odpověď (Back)

Nechť \(X\) je náhodná veličina s konečnou střední hodnotou. Potom pro každé \(a > 0\) platí
\[\operatorname P(|X| \geq a) \leq \frac{\operatorname E|X|} a.\]

## Poznámka Anki 1700043016158

Karty Anki: 1700043016158
GUID: Rd1s=1KB.}; štítky: bi-pst::p08 bi-spol::26.

### Otázka (Front)

Vyslovte větu o Čebyševově nerovnosti.

### Odpověď (Back)

Nechť \(X\) je náhodná veličina s konečnou střední hodnotou a konečným rozptylem. Potom pro každé \(\varepsilon > 0\) platí
\[\operatorname P(|X - \operatorname EX| \geq \varepsilon) \leq \frac{\operatorname{var} X} {\varepsilon^2}.\]

## Poznámka Anki 1700044796361

Karty Anki: 1700044796361
GUID: F*-*qnT[qw; štítky: bi-pst::p08 bi-spol::26.

### Otázka (Front)

Vyslovte větu o slabém zákonu velkých čísel.

### Odpověď (Back)

Nechť \(X_1, X_2, \dots\) jsou i.i.d. náhodné veličiny s konečnou střední hodnotou \(\operatorname E X_i = \mu\) a konečným rozptylem \(\operatorname{var} X_i = \sigma^2\). Potom\[\bar X_n \xrightarrow{\operatorname P} \mu \quad \text{pro} \quad n \to +\infty.\]To znamená, že pro každé \(\varepsilon > 0\) platí\[\displaystyle \lim_{n \to \infty} \operatorname P(|\bar X_n - \mu| \geq \varepsilon) = 0.\]

## Poznámka Anki 1700044994935

Karty Anki: 1700044994935
GUID: oXU*kiT*T7; štítky: bi-pst::p08 bi-spol::26.

### Otázka (Front)

Vyslovte větu o silném zákonu velkých čísel.

### Odpověď (Back)

Nechť \(X_1, X_2, \dots\) jsou i.i.d. náhodné veličiny s ne nutně konečnou střední hodnotou \(\operatorname E X_i = \mu\). Potom \(\bar X_n\) konverguje k \(\mu\) skoro jistě (almost surely):\[\bar X_n \xrightarrow {\text{a.s.}} \mu \quad \text{pro} \quad n \to +\infty.\]To znamená, že množina \(\omega \in \Omega\), kde \(\bar X_n(\omega)\) konverguje jako číselná posloupnost, má pravděpodobnost \(1\):\[\operatorname P(\{ \omega \in \Omega : \bar X_n(\omega) \to \mu \text{ při } n \to +\infty \}) = 1.\]

## Poznámka Anki 1700045763217

Karty Anki: 1700045763217
GUID: lD3F0ME0QP; štítky: bi-pst::p08 bi-spol::26.

Metadata původního zdroje pro kartu 1700045763217: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte konvergenci v distribuci.

### Odpověď (Back)

Nechť \(X_1, X_2, \dots\) je posloupnost náhodných veličin s distribučními funkcemi \(F_{X_1}, F_{X_2}, \dots\) a \(X\) je náhodná veličina s distribuční funkcí \(F_X\). Říkáme, že veličiny \(X_i\) konvergují k \(X\) v distribuci,\[X_n \xrightarrow{\mathcal D} X \quad \text{pro } n \to +\infty,\]jestliže\[\displaystyle \lim_{n \to \infty} F_{X_n}(x) = F_X(x)\]ve všech bodech spojitosti distribuční funkce \(F_X\).

## Poznámka Anki 1700046005844

Karty Anki: 1700046005844
GUID: QTUnh}w+R8; štítky: bi-pst::p08 bi-spol::26.

Metadata původního zdroje pro kartu 1700046005844: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte centrální limitní větu.

### Odpověď (Back)

Nechť \(X_1, X_2, \dots\) je posloupnost i.i.d náhodných veličin s konečnou střední hodnotou \(\operatorname E X_i = \mu\) a konečným rozptylem \(\operatorname{var} X_i = \sigma^2 > 0\). Potom\[\frac{\bar X_n - \mu} {\frac {\sigma} {\sqrt n}} \xrightarrow {\mathcal D} \operatorname N(0, 1) \quad \text{pro} \quad n \to +\infty,\]a podobně\[\frac{S_n - n\mu} {\sigma \sqrt n} \xrightarrow {\mathcal D} \operatorname N(0, 1) \quad \text{pro} \quad n \to +\infty.\]

## Poznámka Anki 1700046820023

Karty Anki: 1700046820023
GUID: IVUI@biX6G; štítky: bi-pst::p08 bi-spol::26.

Metadata původního zdroje pro kartu 1700046820023: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte větu o charakteristikách průměru náhodných veličin.

### Odpověď (Back)

Mějme \(X_1, X_2, \dots\) náhodné i.i.d. veličiny s \(\operatorname E X_i = \mu\) a \(\operatorname{var} X_i = \sigma^2\) potom pro průměr\[\bar X_n = \frac 1 n \displaystyle \sum_{i = 1}^n X_i\]platí\[\begin{matrix}
\operatorname E \bar X_n = \mu, \\
\operatorname{var} \bar X_n = \displaystyle \frac {\sigma^2} n.
\end{matrix}\]

## Poznámka Anki 1700046893953

Karty Anki: 1700046893954
GUID: nx}a[EC:Pg; štítky: bi-pst::p08 bi-spol::26.

Metadata původního zdroje pro kartu 1700046893954: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte větu o charakteristikách součtu náhodných veličin.

### Odpověď (Back)

Mějme \(X_1, X_2, \dots\) náhodné i.i.d. veličiny s \(\operatorname E X_i = \mu\) a \(\operatorname{var} X_i = \sigma^2\) potom pro součet\[S_n = \displaystyle \sum_{i = 1}^n X_i\]platí\[\begin{matrix}
\operatorname E S_n = n \mu, \\
\operatorname{var} S_n = n \sigma^2.
\end{matrix}\]

