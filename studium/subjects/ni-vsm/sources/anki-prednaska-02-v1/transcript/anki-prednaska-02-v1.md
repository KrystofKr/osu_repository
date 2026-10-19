# NI-VSM – Přednáška 02

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-VSM
Rozsah: 31 poznámek, 31 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1739870571747

Karty Anki: 1739870571747
GUID: r9v)>1nrKY; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte náhodnou veličinu.

### Odpověď (Back)

Náhodná veličina \(X\) na pravděpodobnostním prostoru \((\Omega, \mathcal F, \operatorname P)\) je zobrazení \(X : \Omega \to \mathbb R\), které každému výsledku experimentu \(\omega \in \Omega\) přiřadí hodnotu \(X(\omega) \in \mathbb R\) a pro které platí podmínka měritelnosti:\[\{ X \leq x \} = \{ \omega \in \Omega \mid X(\omega) \in (-\infty, x \rangle \}\in \mathcal F, \quad \forall x \in \mathbb R.\]-----------------
Náhodná veličina převádí výsledek náhodného pokusu na čísla

## Poznámka Anki 1739870738642

Karty Anki: 1739870738642
GUID: H6HR..)J*-; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte distribuční funkci.

### Odpověď (Back)

Distribuční funkce náhodné veličiny \(X\) je funkce \(F_X: \mathbb R \to \langle 0, 1 \rangle\) definovaná vztahem\[F_X(x) = \operatorname P(X \leq x), \quad \forall x \in \mathbb R.\]Distribuční funkce jednoznačně určuje pravděpodobnostní rozdělení náhodné veličiny.

## Poznámka Anki 1739871235588

Karty Anki: 1739871235589
GUID: xW<@,b5TN^; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Vyslovte větu o vlastnostech distribuční funkce.

### Odpověď (Back)

Distribuční funkce \(F\) náhodné veličiny \(X\) má následující vlastnosti:

- **je neklesající** - když \(x < y\), pak \(F(x) \leq F(y)\);
- **„začíná v **\(0\)** a končí v **\(1\)**“** - \(\displaystyle \lim_{x \to -\infty} F(x) = 0\) a \(\displaystyle \lim_{x \to +\infty} F(y) = 1\),
- **je spojitá zprava** - \(\displaystyle \lim_{y \to x+} = F(x)\).

## Poznámka Anki 1739871330596

Karty Anki: 1739871330596
GUID: j52p@z5iDo; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Vyslovte lemma o použití distribuční funkce.

### Odpověď (Back)

Pomocí distribuční funkce \(F\) náhodné veličiny \(X\) můžeme vyjádřit:

- \(\operatorname P(X > x) = 1 - F(x)\),

- \(\operatorname P(X \in (x, y \rangle) = \operatorname P(x < X \leq y) = F(y) - F(x)\),

- \(\operatorname P(X < x) = \displaystyle \lim_{y \to x-} F(y)\),

- \(\operatorname P(X = x) = F(x) - \displaystyle \lim_{y \to x-} F(y)\).

## Poznámka Anki 1739872659236

Karty Anki: 1739872659236
GUID: e}tdmBH,9T; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte diskrétní náhodnou veličinu.

### Odpověď (Back)

Náhodná veličina \(X\) se nazývá diskrétní, jesliže nabývá pouze hodnot z nějaké nejvýše spočetné množiny \(\mathcal X = \{ x_1, x_2, \dots \}\) takové, že platí\[\displaystyle \sum_{x \in \mathcal X} \operatorname P(X = x) = 1.\]Pravděpodobnosti možných hodnot náhodné veličiny \(X\) potom jsou\[\operatorname P(X = x_k), \quad k = 1, 2, \dots.\]

## Poznámka Anki 1739872685161

Karty Anki: 1739872685162
GUID: I_)&~rWsS?; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte spojitou náhodnou veličinu.

### Odpověď (Back)

Náhodná veličina \(X\) se nazývá (absolutně) spojitá, jestliže existuje nezáporná funkce \(f_X\) taková, že pro každé \(x \in \mathbb R\) můžeme distribuční funkci \(F_X\) vyjádřit jako
\[F_X(x) = \int_{-\infty}^x f_X(t) \, \text dt.\]Funkci \(f_X\) v takovém případě nazýváme hustotou pravděpodobnosti náhodné veličiny \(X\).
 [Obrázek: paste-bfdc2232ca8783563dd94887ac525202d2874b73.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1740488655802

Karty Anki: 1740488655802
GUID: IpzWm#)U6b; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Vyslovte větu o vlastnostech spojitých náhodných veličin.

### Odpověď (Back)

Pro hustotu \(f_X\) spojité náhodné veličiny \(X\) platí:

- \(\displaystyle \int_{-\infty}^{+\infty} f_X(x) \, \text dx = 1\);

- \(\operatorname P(X = x) = 0\) pro všechna \(x \in \mathbb R\),

- \(f_X(x) = \frac {\text d F_X}{\text dx}(x)\) v bodech, kde \(F_X\) má derivaci,

- \(\operatorname P(a < X \leq b) = \displaystyle \int_a^b f_X(x) \, \text dx = F_X(b) - F_X(a)\),

- \(\operatorname P(X \in B) = \displaystyle  \int_B f_X(x) \, \text dx\) pro všechny \(B\) v Borelovské \(\sigma\)-algebře na \(\mathbb R\).

## Poznámka Anki 1740488727671

Karty Anki: 1740488727672
GUID: zEWExq+jCs; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte střední hodnotu spojité náhodné veličiny.

### Odpověď (Back)

Střední hodnota spojité náhodné veličiny \(X\) s hustotou \(f\) je určena vztahem\[\operatorname E \, X = \displaystyle \int_{-\infty}^{+\infty} x \cdot f(x) \, \text dx.\]Nutnou podmínkou je, že tento integrál absolutně konverguje. Jinak říkáme, že střední hodnota náhodné veličiny \(X\) neexistuje.

## Poznámka Anki 1740488781733

Karty Anki: 1740488781733
GUID: AI`kA?ps][; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte střední hodnotu diskrétní náhodné veličiny.

### Odpověď (Back)

Střední hodnota diskrétní náhodné veličiny \(X\), nabývající hodnot \(x_1, x_2, \dots\), je průměr všech hodnot veličiny \(X\) vážený pravděpodobnostmi příslušných elementárních jevů, tedy\[\operatorname E \, X = \displaystyle \sum_{x \in \mathcal X} x \cdot \text P(X = x_k).\]Nutnou podmínkou je, že uvedená suma konverguje. Jinak říkáme, že střední hodnota náhodné veličiny \(X\) neexistuje.

## Poznámka Anki 1740488811028

Karty Anki: 1740488811029
GUID: hI_u#^gm:9; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Vyslovte větu o střední hodnotě funkce diskrétních náhodných veličin.

### Odpověď (Back)

Mějme diskrétní náhodné veličiny \(X\) a \(Y\). Pak platí\[\operatorname E h(X, Y) = \displaystyle \sum_{x \in \mathcal X, \, y \in \mathcal Y} h(x, y) \cdot \operatorname P(X = x \cap Y = y),\]pokud řada absolutně konverguje.

## Poznámka Anki 1740488818898

Karty Anki: 1740488818898
GUID: bZ(/:R28-9; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Vyslovte větu o střední hodnotě funkce spojitých náhodných veličin.

### Odpověď (Back)

Mějme spojitné náhodné veličiny \(X\) a \(Y\). Pak platí\[\operatorname E h(X, Y) = \displaystyle \int_{-\infty}^\infty \displaystyle \int_{-\infty}^\infty h(x, y) \cdot f_{X, Y}(x, y) \, \text dx \, \text dy,\]pokud integrál absolutně konverguje.

## Poznámka Anki 1740488860721

Karty Anki: 1740488860721
GUID: tmD^;aF2uW; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Vyslovte větu o vlastnostech střední hodnoty.

### Odpověď (Back)

Střední hodnota náhodné veličiny \(X\) splňuje následující vlastnosti:

- Je-li \(X \geq 0\), pak \(\operatorname E(X) \geq 0\).
- Je-li \(a, b \in \mathbb R\), pak \(\operatorname E(a X + b) = a \operatorname E(X) + b\).
- Je-li \(X = c \in \mathbb R\), pak \(\operatorname E(X) = c\).

## Poznámka Anki 1740488888364

Karty Anki: 1740488888364
GUID: K/eJkiMV-1; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte rozptyl (varianci) náhodné veličiny.

### Odpověď (Back)

Rozptyl (variance) náhodné veličiny \(X\) je definován vztahem\[\operatorname{var} X = \operatorname  E \big((X - \operatorname E X)^2 \big) = \operatorname E X^2 - (\operatorname E X)^2. \]

## Poznámka Anki 1740488910772

Karty Anki: 1740488910772
GUID: lsbmJc<yN&; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte směrodatnou odchylku náhodné veličiny.

### Odpověď (Back)

Směrodatná odchylka náhodné veličiny \(X\) je definována jako\[\operatorname{sd} X = \sqrt{\operatorname{var} X}.\]

## Poznámka Anki 1740488970702

Karty Anki: 1740488970702
GUID: KW}*?qppf#; štítky: duplicate ni-vsm::p02.

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

## Poznámka Anki 1740488984496

Karty Anki: 1740488984496
GUID: Olg7D_rWnj; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte kvantil a kvantilovou funkci.

### Odpověď (Back)

Nechť \(X\) je náhodná veličina s distribuční funkcí \(F_X\). Nechť \(\alpha \in (0, 1)\). Hodnota \(q_\alpha\) se nazývá \(\alpha\)-kvantil náhodné veličiny \(X\) právě tehdy, když
\[q_\alpha = \inf \{x \mid F_X(x) \geq \alpha \}.\]Kvantil uvažovaný jako funkce \(\alpha\) se nazývá kvantilová funkce a značí se \(F_X^{-1}(\alpha)\).

## Poznámka Anki 1740489005364

Karty Anki: 1740489005364
GUID: pj&&5^eDNb; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte \(\alpha\)-kritickou hodnotu.

### Odpověď (Back)

\(\alpha\)-kritickou \(c_\alpha\) hodnotou nazýváme \((1 - \alpha)\)-kvantil, tedy\[c_\alpha = q_{1 - \alpha}.\]

## Poznámka Anki 1740489035392

Karty Anki: 1740489035392
GUID: j/C[=4Fmk-; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte Bernoulliho (alternativní) rozdělení.

### Odpověď (Back)

Diskrétní náhodná veličina \(X\) má Bernoulliho (alternativní) rozdělení s parametrem \(p \in \langle 0, 1 \rangle\), jestliže\[\operatorname P(X = 1) = p, \quad \operatorname P(X = 0) = 1 - p.\]Značíme \(X \sim \operatorname{Be}(p)\) či \(X \sim \operatorname{Bernoulli}(p)\) nebo také \(X \sim \operatorname{Alt}(p)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = p, \\
\operatorname{var}(X) = p(1-p).
\end{matrix}\]

### Doplňující pole (Extra)

Bernoulliho (alternativní) rozdělení využijeme, pokud máme náhodný experiment se dvěma možnými výsledky a úspěch nastává s pravděpodobností \(p\).

## Poznámka Anki 1740489057484

Karty Anki: 1740489057484
GUID: Brdima`N_u; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte binomické rozdělení.

### Odpověď (Back)

Diskrétní náhodná veličina \(X\) má binomické rozdělení s parametry \(n \in \mathbb N\) a \(p \in \langle 0, 1 \rangle\), jestliže\[\operatorname P(X = k) = {n \choose k} p^k (1 - p)^{n - k}, \quad k = 0, 1, \dots, n.\]Značíme \(X \sim \operatorname{Binom}(n,p)\) nebo \(X \sim \operatorname{Bin}(n, p)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = np, \\
\operatorname{var}(X) = np(1-p).
\end{matrix}\]

### Doplňující pole (Extra)

Binomické rozdělení využijeme, pokud uvažujeme \(n\) nezávislých pokusů se dvěma možnými výsledky, předpokládáme, že pravděpodobnost úspěchu je \(p\) a úspěch nastává právě \(k\)-krát.

## Poznámka Anki 1740489086256

Karty Anki: 1740489086256
GUID: kX*y$|U#V<; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte geometrické rozdělení.

### Odpověď (Back)

Diskrétní náhodná veličina \(X\) má geometrické rozdělení s parametrem \(p \in (0, 1)\), jestliže\[\operatorname P(X = k) = (1 - p)^{k - 1} p, \quad k = 1, 2, \dots\]Značíme \(X \sim \operatorname{Geom}(p)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = \displaystyle \frac 1 p, \\
\operatorname{var}(X) = \displaystyle  \frac {1 - p} {p^2}.
\end{matrix}\]

### Doplňující pole (Extra)

Geometrické rozdělení využijeme v případě, že uvažujeme posloupnost nezávislých pokusů se dvěma možnými výsledky. Předpokládáme, že pravděpodobnost úspěchu je \(p\) a zajímá nás pravděpodobnost, že první úspěšný pokus je \(k\)-tý pokus v pořadí.

## Poznámka Anki 1740489109510

Karty Anki: 1740489109511
GUID: b;`5^YbX*|; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte Poissonovo rozdělení.

### Odpověď (Back)

Diskrétní náhodná veličina \(X\) má Poissonovo rozdělení s parametrem \(\lambda > 0\), jestliže\[\operatorname P(X = k) = \frac {\lambda^k} {k!} e^{- \lambda}, \quad k = 0, 1, \dots.\]Značíme \(X \sim \operatorname{Poisson}(\lambda)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = \lambda, \\
\operatorname{var}(X)= \lambda.
\end{matrix}\]

### Doplňující pole (Extra)

Poissonovo rozdělení využijeme, pokud zkoumáme počet realizací náhodných údálostí řídkého jevu během určité doby. Počítá s výrazně vyšším počtem pokusů než realizací.

## Poznámka Anki 1740489140945

Karty Anki: 1740489140945
GUID: plW{wz,4v?; štítky: duplicate ni-vsm::p02.

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

## Poznámka Anki 1740489172443

Karty Anki: 1740489172443
GUID: t,GhHcW#-!; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte exponenciální rozdělení.

### Odpověď (Back)

Spojitá náhodná veličina \(X\) má exponenciální rozdělení s parametrem \(\lambda >0\), jestliže\[f_X(x) = \begin{cases}
\lambda e^{- \lambda x} && \text{pro } x \in \langle 0, +\infty), \\
0 && \text{jinde}.
\end{cases}\]Značíme \(X \sim \operatorname{Exp}(\lambda)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = \displaystyle \frac 1 \lambda, \\
\operatorname{var}(X) = \displaystyle \frac 1 {\lambda^2}.
\end{matrix}\]

### Doplňující pole (Extra)

Exponenciální rozdělení využijeme, pokud modelujeme čas mezi dvěma událostmi s Poissonovským rozdělením.

## Poznámka Anki 1740489194824

Karty Anki: 1740489194824
GUID: Oq6h2nzkoF; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte normální (Gaussovo) rozdělení.

### Odpověď (Back)

Spojitá náhodná veličina \(X\) má normální (Gaussovo) rozdělení s parametry \(\mu \in \mathbb R\) a \(\sigma^2 > 0\), jestliže\[f_X(x) = \frac 1 {\sqrt{2 \pi \sigma^2}} e^{- \frac {(x - \mu)^2} {2 \sigma^2}}, \quad x \in (- \infty, +\infty).\]Značíme \(X \sim \operatorname N(\mu, \sigma^2)\) a \(\operatorname N(0, 1) \) nazýváme standardním normálním rozdělením. Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E(X) = \mu, \\
\operatorname{var}(X) = \sigma^2.
\end{matrix}\]

### Doplňující pole (Extra)

Normální (Gaussovo) rozdělení využijeme, pokud modelujeme veličiny pozorovatelné v přírodě jako např. výška nebo váha.

## Poznámka Anki 1740490305434

Karty Anki: 1740490305434
GUID: Q`~N/:1_Ad; štítky: ni-vsm::p02.

### Otázka (Front)

Definujte gamma funkci.

### Odpověď (Back)

Gamma funkce \(\Gamma\) je pro \(p > 0\) definována vztahem\[\operatorname \Gamma(p) = \displaystyle \int_0^{+\infty} x^{p - 1} e^{-x} \, \mathrm dx.\]

## Poznámka Anki 1740490728467

Karty Anki: 1740490728468
GUID: ra/2g8Sr-Q; štítky: ni-vsm::p02.

### Otázka (Front)

Definujte gamma rozdělení.

### Odpověď (Back)

Spojitá náhodná veličina \(X\) má gamma rozdělení s parametry \(a > 0\) a \(p > 0\), jestliže\[f_X(x) = \begin{cases}
\displaystyle \frac{a^p}{\operatorname \Gamma(p)} e^{-ax} x^{p - 1} && x \in (0, +\infty),\\
0 && \text{jinde}.
\end{cases}\]Značíme \(X \sim \operatorname{Ga}(a, p)\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E X =  \displaystyle \frac p a,\\
\operatorname{var} X = \displaystyle \frac p {a^2}.
\end{matrix}\]

### Doplňující pole (Extra)

Z gamma rozdělení vychází:

- **exponenciální rozdělení** - pro \(a = \lambda\) a \(p = 1\),

- \(\chi^2\) **rozdělení** s \(n\) stupni volnosti - pro \(a = \frac 1 2\) a \(p = \frac n 2\).

## Poznámka Anki 1740490948025

Karty Anki: 1740490948025
GUID: t*h}iAR.Fm; štítky: ni-vsm::p02.

### Otázka (Front)

Definujte \(\chi^2\) rozdělení.

### Odpověď (Back)

Spojitá náhodná veličina \(X\) má \(\chi^2\) rozdělení s \(n \in \mathbb N\) stupni volnosti, jestliže\[f_X(x) = \begin{cases}
\displaystyle \frac 1 {2^\frac n 2 \operatorname \Gamma(\frac n 2)} x^{\frac n 2 - 1} e ^{- \frac x 2} && x \in (0, +\infty),\\
0 && \text{jinde}.
\end{cases}\]Značíme \(X \sim \chi^2_n\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname E X = n,\\
\operatorname{var} X = 2n.
\end{matrix}\]

### Doplňující pole (Extra)

\(\chi^2\) rozdělení se nejčastěji objevuje jako součet kvadrátů nezávislých standardních normálních rozdělení.

## Poznámka Anki 1740491409623

Karty Anki: 1740491409623
GUID: m*^Jt!%9+^; štítky: ni-vsm::p02.

### Otázka (Front)

Definujte Studentovo \(t\)-rozdělení

### Odpověď (Back)

Spojitá náhodná veličina \(X\) má Studentovo \(\operatorname t\)-rozdělení s \(n \in \mathbb N\) stupni volnosti, jestliže\[f_X(x) = \frac{\operatorname \Gamma(\frac{n + 1} 2)}{\operatorname \Gamma(\frac n 2) \sqrt{\pi n}} \bigg( 1 + \frac {x^2} n \bigg)^{- \frac{n + 1} 2}, \quad x \in (-\infty, +\infty).\]Značíme \(X \sim \operatorname{t}_n\). Pro střední hodnotu a rozptyl platí:\[\begin{matrix}
\operatorname EX = 0, && n > 1 \\
\operatorname{var}X = \displaystyle \frac n {n - 2} && n > 2.
\end{matrix}\]

### Doplňující pole (Extra)

Studentovo \(\operatorname t\)-rozdělení se nejčasteji objevuje jako podíl standardního normálního rozdělení a \(\chi^2\) rozdělení.

## Poznámka Anki 1740492472452

Karty Anki: 1740492472453
GUID: A0&Hx2p>}+; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte sdružené rozdělení (náhodný vektor a sdruženou distribuční funkci).

### Odpověď (Back)

Mějme \(n \in \mathbb N\) a náhodné veličiny \(X_1, \dots X_n\) na stejném pravděpodobnostním prostoru \((\Omega, \mathcal F, \operatorname P)\). Vektor \(\mathbf X = (X_1, \dots, X_n)^T\) nazýváme **náhodným vektorem** na \((\Omega, \mathcal F, \operatorname P)\). Pravděpodobnostní rozělení vektoru \(\mathbf X\) je popsáno **sdruženou distribuční funkcí** \(F_\mathbf X : \mathbb R^n \to \langle 0, 1 \rangle\) definovanou vztahem\[F_{\mathbf X}(\mathbf x) = \operatorname P(\mathbf X \leq \mathbf x) = \operatorname P(X_1 \leq x_1 \cap \dots \cap X_n \leq x_n)\]pro každé \(\mathbf x = (x_1, \dots, x_n)^T \in \mathbb R^n\).

## Poznámka Anki 1740493083537

Karty Anki: 1740493083538
GUID: PbR~B#}#wy; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte sdružené diskrétní rozdělení.

### Odpověď (Back)

Náhodný vektor \(\mathbf X = (X_1, \dots, X_n)^T\) má sdružené diskrétní rozdělení, jestliže nabývá hodnot z nejvýše spočetné množiny \(\mathcal X = \{ \mathbf x_1, \mathbf x_2, \dots \} \subset \mathbb R^n\) takové, že platí\[\displaystyle \sum_{\mathbf x \in \mathcal X} \operatorname P(\mathbf X = \mathbf x) = \displaystyle \sum_{\mathbf x \in \mathcal X} \operatorname P(X_1 = x_1 \cap \dots \cap X_n = x_n ) = 1.\]Pravděpodobnosti možných hodnot náhodného vektoru \(\mathbf X\) potom jsou\[\operatorname P(\mathbf X = \mathbf x) = \operatorname P(X_1 = x_1 \cap \dots \cap X_n = x_n) = \operatorname P(\{ X_1 = x_1 \} \cap \dots \cap \{ X_n = x_n \}).\]

## Poznámka Anki 1740493315830

Karty Anki: 1740493315830
GUID: c${lB(|B*`; štítky: duplicate ni-vsm::p02.

### Otázka (Front)

Definujte sdružené spojité rozdělení.

### Odpověď (Back)

Náhodný vektor \(\mathbf X = (X_1, \dots, X_n)^T\) má sdružené (absolutně) spojité rozdělení, jestliže nezáporná funkce \(f_\mathbf X : \mathbb R^n \to \mathbb R\) taková, že pro každé \(\mathbf x \in \mathbb R^n\) platí\[F_\mathbf X(\mathbf x) = \displaystyle \int_{-\infty}^{x_n} \dots \displaystyle \int_{-\infty}^{x_1} f_\mathbf X(u) \, \mathrm d u_1 \dots \, \mathrm d u_n.\]Funkce \(f_\mathbf X\) se pak nazývá sdruženou hustotou pravděpodobnosti náhodného vektoru \(\mathbf X\).

