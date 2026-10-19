# BI-PST – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1698834501139

Karty Anki: 1698834501139
GUID: ne8c7tAzgd; štítky: bi-pst::p06 bi-spol::26.

Metadata původního zdroje pro kartu 1698834501139: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte sdružené rozdělení (náhodný vektor a sdruženou distribuční funkci).

### Odpověď (Back)

Mějme \(n \in \mathbb N\) a náhodné veličiny \(X_1, \dots X_n\) na stejném pravděpodobnostním prostoru \((\Omega, \mathcal F, \operatorname P)\). Vektor \(\mathbf X = (X_1, \dots, X_n)^T\) nazýváme **náhodným vektorem** na \((\Omega, \mathcal F, \operatorname P)\). Pravděpodobnostní rozělení vektoru \(\mathbf X\) je popsáno **sdruženou distribuční funkcí** \(F_\mathbf X : \mathbb R^n \to \langle 0, 1 \rangle\) definovanou vztahem\[F_{\mathbf X}(\mathbf x) = \operatorname P(\mathbf X \leq \mathbf x) = \operatorname P(X_1 \leq x_1 \cap \dots \cap X_n \leq x_n)\]pro každé \(\mathbf x = (x_1, \dots, x_n)^T \in \mathbb R^n\).

## Poznámka Anki 1698834928635

Karty Anki: 1698834928635
GUID: P-k$;^yH6L; štítky: bi-pst::p06 bi-spol::26.

### Otázka (Front)

Vyslovte větu o vlastnostech sdružené distribuční funkce.

### Odpověď (Back)

Distribuční funkce \(F_{X, Y}\) náhodných veličin \(X\) a \(Y\) má následující vlastnosti:

- pokud \(x_1 < x_2\) a \(y_1 < y_2\), tak \(F_{X, Y}(x_1, y_1) \leq F_{X, Y}(x_2, y_2)\);
- \(\forall y \in \mathbb R, \displaystyle \lim_{x \to -\infty} F_{X, Y}(x, y) = 0\) a \(\forall x \in \mathbb R, \displaystyle \lim_{y \to -\infty} F_{X, Y}(x, y) = 0\);

- \(\forall y \in \mathbb R, \displaystyle \lim_{x \to +\infty} F_{X, Y}(x, y) = F_Y(y)\) a \(\forall x \in \mathbb R, \displaystyle \lim_{y \to +\infty} F_{X, Y}(x, y) = F_X(x)\).

## Poznámka Anki 1698835242518

Karty Anki: 1698835242518
GUID: I>3$9he)q0; štítky: bi-pst::p06.

Metadata původního zdroje pro kartu 1698835242518: oranžový příznak autora: určeno k odstranění; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte sdruženou pravděpodobnost diskrétních náhodných veličin.

### Odpověď (Back)

Diskrétní náhodné veličiny \(X\) a \(Y\) mají sdružené pravděpodobnosti možných hodnot
\[\operatorname P(X = x \cap Y = y) = \operatorname P(\{ X = x \} \cap \{ Y = y \}).\]

## Poznámka Anki 1698835388149

Karty Anki: 1698835388149
GUID: m$/b|]Sau; štítky: bi-pst::p06.

Metadata původního zdroje pro kartu 1698835388149: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte větu o marginálním rozdělení diskrétní náhodné veličiny.

### Odpověď (Back)

Mějme náhodné veličiny \(X\) a \(Y\) se sdruženým diskrétním rozdělením. Marginální rozdělení veličin \(X\) a \(Y\) jsou potom také diskrétní a určená pravděpodobnostmi\[\begin{align}
\operatorname P(X = x) &= \displaystyle \sum_{y \in \mathcal Y} \operatorname P(X = x \cap Y = y),\\
\operatorname P(Y = y) &= \displaystyle \sum_{x \in \mathcal X} \operatorname P(X = x \cap Y = y).
\end{align}\]

## Poznámka Anki 1698835857877

Karty Anki: 1698835857877
GUID: H>zWh>rF}0; štítky: bi-pst::p06 bi-spol::26.

Metadata původního zdroje pro kartu 1698835857877: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte větu o nezávislosti diskrétních náhodných veličin.

### Odpověď (Back)

Diskrétní náhodné veličiny \(X_1, \dots, X_n\) jsou nezávislé právě tehdy, když pro každé \(\mathbf x \in \mathbb R^n\) platí\[\operatorname P(\mathbf X = \mathbf x) = \displaystyle \prod_{i = 1}^n \operatorname P(X_i = x_i).\]

## Poznámka Anki 1698836734885

Karty Anki: 1698836734885
GUID: m&~,{tZT<j; štítky: bi-pst::p06.

Metadata původního zdroje pro kartu 1698836734885: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte podmíněnou distribuční funkci a podmíněnou pravděpodobnost diskrétních veličin.

### Odpověď (Back)

Nechť \(\operatorname P(Y = y) > 0\). Potom je **podmíněná distribuční funkce** \(F_{X|Y}(\cdot |y)\) veličiny \(X\) dáno (za podmínky) \(Y = y\) určena vztahem\[F_{X|Y}(x|y) = \operatorname P(X \leq x | Y = y) = \frac{\operatorname P(X \leq x \cap Y = y)} {\operatorname P(Y = y)}.\]**Podmíněné pravděpodobnosti **hodnot \(X\) dáno (za podmínky) \(Y = y\) jsou analogicky\[\operatorname P(X = x | Y = y) = \frac{\operatorname P(X = x \cap Y = y)} {\operatorname P(Y = y)}.\]

## Poznámka Anki 1698836894978

Karty Anki: 1698836894978
GUID: G4wPb<mTt?; štítky: bi-pst::p06 bi-spol::26.

Metadata původního zdroje pro kartu 1698836894978: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte podmíněnou střední hodnotu diskrétní náhodné veličiny.

### Odpověď (Back)

Nechť \(\operatorname P(Y = y) > 0\). Podmíněnou střední hodnotu \(X\) dáno (za podmínky) \(\{Y = y\}\) definujeme jako\[\operatorname E(X | Y = y) = \displaystyle \sum_{x \in \mathcal X} x \cdot \operatorname P(X = x | Y = y).\]

## Poznámka Anki 1698837860743

Karty Anki: 1698837860743
GUID: P|Ff!Th{L); štítky: bi-pst::p06.

Metadata původního zdroje pro kartu 1698837860743: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte sdružené spojité rozdělení.

### Odpověď (Back)

Náhodný vektor \(\mathbf X = (X_1, \dots, X_n)^T\) má sdružené (absolutně) spojité rozdělení, jestliže nezáporná funkce \(f_\mathbf X : \mathbb R^n \to \mathbb R\) taková, že pro každé \(\mathbf x \in \mathbb R^n\) platí\[F_\mathbf X(\mathbf x) = \displaystyle \int_{-\infty}^{x_n} \dots \displaystyle \int_{-\infty}^{x_1} f_\mathbf X(u) \, \mathrm d u_1 \dots \, \mathrm d u_n.\]Funkce \(f_\mathbf X\) se pak nazývá sdruženou hustotou pravděpodobnosti náhodného vektoru \(\mathbf X\).

## Poznámka Anki 1698838030293

Karty Anki: 1698838030293
GUID: l#f[B|S_J-; štítky: bi-pst::p06.

Metadata původního zdroje pro kartu 1698838030293: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte větu o marginálním rozdělení spojité náhodné veličiny.

### Odpověď (Back)

Mějme náhodné veličiny \(X\) a \(Y\) se sdruženým spojitým rozdělením určeným hustotou \(f_{X, Y}\). Marginální rozdělení veličin \(X\) a \(Y\) jsou potom také spojitá a určená hustotami\[\begin{align}
f_X(x) = \displaystyle \int_{-\infty}^{+\infty} f_{X, Y}(x, y) \, \text dy, \\
f_Y(y) = \displaystyle \int_{-\infty}^{+\infty} f_{X, Y}(x, y) \, \text dx.
\end{align}\]

## Poznámka Anki 1698838155302

Karty Anki: 1698838155302
GUID: $&^J;bt/K; štítky: bi-pst::p06.

Metadata původního zdroje pro kartu 1698838155302: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte větu o nezávislosti spojitých náhodných veličin.

### Odpověď (Back)

Spojité náhodné veličiny \(X_1, \dots, X_n\) jsou nezávislé právě tehdy, když pro každé \(\mathbf x \in \mathbb R^n\) platí\[f_\mathbf X(\mathbf x) = \displaystyle \prod_{i = 1}^n f_{X_i}(x_i).\]

## Poznámka Anki 1698838385644

Karty Anki: 1698838385644
GUID: E`qQ8Yap?3; štítky: bi-pst::p06.

Metadata původního zdroje pro kartu 1698838385644: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte podmíněnou hustotu a podmíněnou distribuční funkci spojité náhodné veličiny.

### Odpověď (Back)

Nechť \(f_Y(y) > 0\). Potom je **podmíněná hustota** \(f_{X|Y}(\cdot|y)\) veličiny \(X\) dáno (za podmínky) \(Y = y\) určena vztahem\[f_{X|Y}(x|y) = \frac{f_{X, Y}(x, y)} {f_Y(y)}.\]**Podmíněná distribuční funkce **\(F_{X|Y}(\cdot|y)\) veličiny \(X\) dáno (za podmínky) \(Y = y\) je pak\[F_{X|Y}(x|y) = \displaystyle \int_{-\infty}^x f_{X|Y}(u|y) \, \text du.\]

## Poznámka Anki 1698838864684

Karty Anki: 1698838864684
GUID: fRMCwrUvC2; štítky: bi-pst::p06 bi-spol::26.

Metadata původního zdroje pro kartu 1698838864684: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte podmíněnou střední hodnotu spojité náhodné veličiny.

### Odpověď (Back)

Nechť \(f_Y(y) > 0\). Podmíněnou střední hodnotu \(X\) dáno (za podmínky) \(Y = y\) definujeme jako\[\operatorname E(X | Y = y) = \displaystyle \int_{-\infty}^{+\infty} x \cdot f_{X|Y}(x|y) \, \text dx.\]

## Poznámka Anki 1740493061652

Karty Anki: 1740493061652
GUID: v{.~i(AECA; štítky: bi-pst::p06.

Metadata původního zdroje pro kartu 1740493061652: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte sdružené diskrétní rozdělení.

### Odpověď (Back)

Náhodný vektor \(\mathbf X = (X_1, \dots, X_n)^T\) má sdružené diskrétní rozdělení, jestliže nabývá hodnot z nejvýše spočetné množiny \(\mathcal X = \{ \mathbf x_1, \mathbf x_2, \dots \} \subset \mathbb R^n\) takové, že platí\[\displaystyle \sum_{\mathbf x \in \mathcal X} \operatorname P(\mathbf X = \mathbf x) = 1.\]Pravděpodobnosti možných hodnot náhodného vektoru \(\mathbf X\) potom jsou\[\operatorname P(\mathbf X = \mathbf x) = \operatorname P(X_1 = x_1 \cap \dots \cap X_n = x_n) = \operatorname P(\{ X_1 = x_1 \} \cap \dots \cap \{ X_n = x_n \}).\]

