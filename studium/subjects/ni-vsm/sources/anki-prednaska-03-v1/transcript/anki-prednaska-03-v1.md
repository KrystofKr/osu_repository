# NI-VSM – Přednáška 03

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-VSM
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1740673338834

Karty Anki: 1740673338834
GUID: hqK`l3ia2r; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Vyslovte větu o marginálním rozdělení spojité náhodné veličiny.

### Odpověď (Back)

Mějme náhodné veličiny \(X\) a \(Y\) se sdruženým spojitým rozdělením určeným hustotou \(f_{X, Y}\). Marginální rozdělení veličin \(X\) a \(Y\) jsou potom také spojitá a určená hustotami\[\begin{align}
f_X(x) = \displaystyle \int_{-\infty}^{+\infty} f_{X, Y}(x, y) \, \text dy, \\
f_Y(y) = \displaystyle \int_{-\infty}^{+\infty} f_{X, Y}(x, y) \, \text dx.
\end{align}\]

## Poznámka Anki 1740673347384

Karty Anki: 1740673347384
GUID: D9sng=t&R$; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Vyslovte větu o marginálním rozdělení diskrétní náhodné veličiny.

### Odpověď (Back)

Mějme náhodné veličiny \(X\) a \(Y\) se sdruženým diskrétním rozdělením. Marginální rozdělení veličin \(X\) a \(Y\) jsou potom také diskrétní a určená pravděpodobnostmi\[\begin{align}
\operatorname P(X = x) &= \displaystyle \sum_{y \in \mathcal Y} \operatorname P(X = x \cap Y = y),\\
\operatorname P(Y = y) &= \displaystyle \sum_{x \in \mathcal X} \operatorname P(X = x \cap Y = y).
\end{align}\]

## Poznámka Anki 1740673946029

Karty Anki: 1740673946029
GUID: <7QwjaB-L; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Vyslovte větu o nezávislosti diskrétních náhodných veličin.

### Odpověď (Back)

Diskrétní náhodné veličiny \(X_1, \dots, X_n\) jsou nezávislé právě tehdy, když pro každé \(\mathbf x \in \mathbb R^n\) platí\[\operatorname P(\mathbf X = \mathbf x) = \displaystyle \prod_{i = 1}^n \operatorname P(X_i = x_i).\]

## Poznámka Anki 1740673956436

Karty Anki: 1740673956436
GUID: mTjaG?{Q{d; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Vyslovte větu o nezávislosti spojitých náhodných veličin.

### Odpověď (Back)

Spojité náhodné veličiny \(X_1, \dots, X_n\) jsou nezávislé právě tehdy, když pro každé \(\mathbf x \in \mathbb R^n\) platí\[f_\mathbf X(\mathbf x) = \displaystyle \prod_{i = 1}^n f_{X_i}(x_i).\]

## Poznámka Anki 1740674212164

Karty Anki: 1740674212164
GUID: of<:HTf9n*; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Vyslovte větu o součtu diskrétních náhodných veličin (diskrétní konvoluci).

### Odpověď (Back)

Mějme nezávislé diskrétní náhodné veličiny \(X \) a \(Y\). Pak pro \(Z = X + Y\) platí\[\operatorname P(Z = z) = \displaystyle \sum_{x \in \mathcal X} \operatorname P(X = x) \cdot \operatorname P(Y = z - x).\]

## Poznámka Anki 1740674221305

Karty Anki: 1740674221305
GUID: efb%SV8i<?; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Vyslovte větu o součtu spojitých náhodných veličin (konvoluci hustot).

### Odpověď (Back)

Mějme nezávislé spojité náhodné veličiny \(X\) a \(Y\). Pak pro \(Z = X + Y\) platí\[f_Z(z) = \displaystyle \int_{-\infty}^\infty f_X(x) \cdot f_Y(z - x) \, \text dx.\]

## Poznámka Anki 1740674711360

Karty Anki: 1740674711360
GUID: rj+I)68%d?; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Definujte kovarianci a korelační koeficient.

### Odpověď (Back)

Mějme náhodné veličiny \(X\) a \(Y\) s konečnými druhými momenty. Pak definujeme **kovarianci** náhodných veličin \(X\) a \(Y\) vztahem\[\operatorname{cov}(X, Y) = \operatorname E \big((X - \operatorname E X) \cdot (Y - \operatorname E Y) \big) = \operatorname E XY - \operatorname E X \cdot \operatorname E Y.\]Pokud mají \(X\) a \(Y\) kladné rozptyly, definujeme **korelační koeficient** jako\[\operatorname \rho (X, Y) = \frac {\operatorname{cov}(X, Y)} {\sigma_X \sigma_Y} = \frac {\operatorname{cov}(X, Y)} {\sqrt{\operatorname{var} X } \sqrt{\operatorname{var} Y}}.\]

## Poznámka Anki 1740674761145

Karty Anki: 1740674761145
GUID: Gjc{CEZYUU; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Definujte nekorelované náhodné veličiny.

### Odpověď (Back)

Náhodné veličiny \(X\) a \(Y\) nazýváme nekorelované, pokud platí\[\operatorname{cov}(X, Y) = 0\]nebo alternativně\[\operatorname E XY = \operatorname E X \operatorname E Y.\]

## Poznámka Anki 1740674878318

Karty Anki: 1740674878319
GUID: Ieo`f6P9)2; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Vyslovte větu o vlastnostech rozptylu (variance).

### Odpověď (Back)

Rozptyl splňuje následující vlastnosti:

- pro náhodnou veličinu \(X\) platí

\[\operatorname{cov}(X, X) = \operatorname{var} X,\]

- pro \(X\) a \(Y\) s konečnými druhými momenty platí

\[\operatorname{var}(X \pm Y) = \operatorname{var} X + \operatorname{var} Y \pm 2 \operatorname{cov}(X, Y),\]

- pro nekorelované náhodné veličiny platí

\[\operatorname{var}(X \pm Y) = \operatorname{var} X + \operatorname{var} Y,\]

- pro \(a, b \in \mathbb R\) platí

\[\operatorname{var}(aX + bY) = a^2 \operatorname{var} X + b^2 \operatorname{var} Y + 2ab \operatorname{cov}(X, Y).\]

## Poznámka Anki 1740674906068

Karty Anki: 1740674906068
GUID: jm#XwaBM}[; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Vyslovte větu o korelaci nezávislých náhodných veličin.

### Odpověď (Back)

Jestliže jsou náhodné veličiny \(X\) a \(Y\) nezávislé, pak jsou i nekorelované.

## Poznámka Anki 1740675782612

Karty Anki: 1740675782612
GUID: bVDs2XiQ15; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Definujte podmíněnou distribuční funkci a podmíněnou pravděpodobnost diskrétních veličin.

### Odpověď (Back)

Nechť \(\operatorname P(Y = y) > 0\). Potom je **podmíněná distribuční funkce** \(F_{X|Y}(\cdot |y)\) veličiny \(X\) dáno (za podmínky) \(Y = y\) určena vztahem\[F_{X|Y}(x|y) = \operatorname P(X \leq x | Y = y) = \frac{\operatorname P(X \leq x \cap Y = y)} {\operatorname P(Y = y)}.\]**Podmíněné pravděpodobnosti **hodnot \(X\) dáno (za podmínky) \(Y = y\) jsou analogicky\[\operatorname P(X = x | Y = y) = \frac{\operatorname P(X = x \cap Y = y)} {\operatorname P(Y = y)}.\]

## Poznámka Anki 1740675792660

Karty Anki: 1740675792660
GUID: b;2ZDgJj6p; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Definujte podmíněnou hustotu a podmíněnou distribuční funkci spojité náhodné veličiny.

### Odpověď (Back)

Nechť \(f_Y(y) > 0\). Potom je **podmíněná hustota** \(f_{X|Y}(\cdot|y)\) veličiny \(X\) dáno (za podmínky) \(Y = y\) určena vztahem\[f_{X|Y}(x|y) = \frac{f_{X, Y}(x, y)} {f_Y(y)}.\]**Podmíněná distribuční funkce **\(F_{X|Y}(\cdot|y)\) veličiny \(X\) dáno (za podmínky) \(Y = y\) je pak\[F_{X|Y}(x|y) = \displaystyle \int_{-\infty}^x f_{X|Y}(u|y) \, \text du.\]

## Poznámka Anki 1740676483092

Karty Anki: 1740676483092
GUID: QDz:,iR}rd; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Definujte podmíněnou střední hodnotu diskrétní náhodné veličiny.

### Odpověď (Back)

Nechť \(\operatorname P(Y = y) > 0\). Podmíněnou střední hodnotu \(X\) dáno (za podmínky) \(\{Y = y\}\) definujeme jako\[\operatorname E(X | Y = y) = \displaystyle \sum_{x \in \mathcal X} x \cdot \operatorname P(X = x | Y = y).\]

## Poznámka Anki 1740676492132

Karty Anki: 1740676492132
GUID: GI(reg5I?n; štítky: duplicate ni-vsm::p03.

### Otázka (Front)

Definujte podmíněnou střední hodnotu spojité náhodné veličiny.

### Odpověď (Back)

Nechť \(f_Y(y) > 0\). Podmíněnou střední hodnotu \(X\) dáno (za podmínky) \(Y = y\) definujeme jako\[\operatorname E(X | Y = y) = \displaystyle \int_{-\infty}^{+\infty} x \cdot f_{X|Y}(x|y) \, \text dx.\]

