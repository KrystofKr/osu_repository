# NI-VSM – Přednáška 08

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-VSM
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1742153430812

Karty Anki: 1742153430813
GUID: PMQH:Bz{U5; štítky: duplicate ni-vsm::p08.

### Otázka (Front)

Vyslovte větu o charakteristikách součtu náhodných veličin.

### Odpověď (Back)

Mějme \(X_1, X_2, \dots\) náhodné i.i.d. veličiny s \(\operatorname E X_i = \mu\) a \(\operatorname{var} X_i = \sigma^2\) potom pro součet\[S_n = \displaystyle \sum_{i = 1}^n X_i\]platí\[\begin{matrix}
\operatorname E S_n = n \mu, \\
\operatorname{var} S_n = n \sigma^2.
\end{matrix}\]

## Poznámka Anki 1742153466414

Karty Anki: 1742153466415
GUID: FQ2.xXbdhf; štítky: duplicate ni-vsm::p08.

### Otázka (Front)

Vyslovte větu o charakteristikách průměru náhodných veličin.

### Odpověď (Back)

Mějme \(X_1, X_2, \dots\) náhodné i.i.d. veličiny s \(\operatorname E X_i = \mu\) a \(\operatorname{var} X_i = \sigma^2\) potom pro průměr\[\bar X_n = \frac 1 n \displaystyle \sum_{i = 1}^n X_i\]platí\[\begin{matrix}
\operatorname E \bar X_n = \mu, \\
\operatorname{var} \bar X_n = \displaystyle \frac {\sigma^2} n.
\end{matrix}\]

## Poznámka Anki 1742153962068

Karty Anki: 1742153962069
GUID: Jc6mtXQ+?.; štítky: duplicate ni-vsm::p08.

### Otázka (Front)

Vyslovte větu o slabém zákonu velkých čísel.

### Odpověď (Back)

Nechť \(X_1, X_2, \dots\) jsou i.i.d. náhodné veličiny s konečnou střední hodnotou \(\operatorname E X_i = \mu\) a konečným rozptylem \(\operatorname{var} X_i = \sigma^2\). Potom\[\bar X_n \xrightarrow{\operatorname P} \mu \quad \text{pro} \quad n \to +\infty.\]To znamená, že pro každé \(\varepsilon > 0\) platí\[\displaystyle \lim_{n \to \infty} \operatorname P(|\bar X_n - \mu| \geq \varepsilon) = 0.\]

## Poznámka Anki 1742153971763

Karty Anki: 1742153971763
GUID: vi:[>IuC-$; štítky: duplicate ni-vsm::p08.

### Otázka (Front)

Vyslovte větu o silném zákonu velkých čísel.

### Odpověď (Back)

Nechť \(X_1, X_2, \dots\) jsou i.i.d. náhodné veličiny s ne nutně konečnou střední hodnotou \(\operatorname E X_i = \mu\). Potom \(\bar X_n\) konverguje k \(\mu\) skoro jistě (almost surely):\[\bar X_n \xrightarrow {\text{a.s.}} \mu \quad \text{pro} \quad n \to +\infty.\]To znamená, že množina \(\omega \in \Omega\), kde \(\bar X_n(\omega)\) konverguje jako číselná posloupnost, má pravděpodobnost \(1\):\[\operatorname P(\{ \omega \in \Omega : \bar X_n(\omega) \to \mu \text{ při } n \to +\infty \}) = 1.\]

## Poznámka Anki 1742154684153

Karty Anki: 1742154684153
GUID: MFY,A{WG,c; štítky: duplicate ni-vsm::p08.

### Otázka (Front)

Definujte konvergenci v distribuci.

### Odpověď (Back)

Nechť \(X_1, X_2, \dots\) je posloupnost náhodných veličin s distribučními funkcemi \(F_{X_1}, F_{X_2}, \dots\) a \(X\) je náhodná veličina s distribuční funkcí \(F_X\). Říkáme, že veličiny \(X_i\) konvergují k \(X\) v distribuci,\[X_n \xrightarrow{\mathcal D} X \quad \text{pro } n \to +\infty,\]jestliže\[\displaystyle \lim_{n \to \infty} F_{X_n}(x) = F_X(x)\]ve všech bodech spojitosti distribuční funkce \(F_X\).

## Poznámka Anki 1742154905728

Karty Anki: 1742154905728
GUID: HHr=X;(gDf; štítky: duplicate ni-vsm::p08.

### Otázka (Front)

Vyslovte centrální limitní větu.

### Odpověď (Back)

Nechť \(X_1, X_2, \dots\) je posloupnost i.i.d náhodných veličin s konečnou střední hodnotou \(\operatorname E X_i = \mu\) a konečným rozptylem \(\operatorname{var} X_i = \sigma^2 > 0\). Potom\[\frac{\bar X_n - \mu} {\frac {\sigma} {\sqrt n}} \xrightarrow {\mathcal D} \operatorname N(0, 1) \quad \text{pro} \quad n \to +\infty,\]a podobně\[\frac{S_n - n\mu} {\sigma \sqrt n} \xrightarrow {\mathcal D} \operatorname N(0, 1) \quad \text{pro} \quad n \to +\infty.\]

