# BI-MA2 – Přednáška 18

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1671463505605

Karty Anki: 1671463505605
GUID: yVSdj37OIl; štítky: bi-ma2::p18 duplicate ni-spol::04.

### Otázka (Front)

Zkonstruujte Riemannův integrál pro funkce dvou proměnných.

### Odpověď (Back)

Mějme obdélník \(D:= \langle a_1, b_1 \rangle \times \langle a_2, b_2 \rangle\) a funkci \(f\) definovanou a omezenou na \(D\). Zkonstruujme nejprve **dělení obdélníku** \(D\) pomocí dílčích dělení\[\sigma_x = \set{x_0 = a_1 < x_1 < \cdots < x_n = b_1}\]intervalu \(\langle a_1, b_1 \rangle\) a\[\sigma_y = \set{y_0 = a_2 < y_1 < \cdots < y_m = b_2}\]intervalu \(\langle a_2, b_2 \rangle\). Dělením obdélníku \(D\) pak nazveme\[\sigma = \sigma_x \times \sigma_y.\]Zadefinujme nyní pomocné symboly\[\begin{matrix}
M_{i,j} := \sup \set{f(x, y) | (x, y) \in \langle x_{i-1}, x_i \rangle \times \langle y_{j-1}, y_j \rangle},\\
m_{i,j} := \inf \set{f(x, y) | (x, y) \in \langle x_{i-1}, x_i \rangle \times \langle y_{j-1}, y_j \rangle}.
\end{matrix}\]pro \(i \in \hat n\) a \(j \in \hat m\). Dále definujme **horní a dolní součet funkce **\(f\)** na obdélníku **\(D\)** při dělení** \(\sigma\) předpisy\[\begin{matrix}
S(f, \sigma) := \sum \limits_{i=1}^n \sum \limits_{j=1}^m M_{i,j} (x_i - x_{i-1} )(y_j - y_{j-1}),\\
s(f, \sigma) := \sum \limits_{i=1}^n \sum \limits_{j=1}^m m_{i,j} (x_i - x_{i-1} )(y_j - y_{j-1}).
\end{matrix}\]Nyní pro funkci \(f\) a obdélník \(D\) **definujeme horní a dolní integrál funkce **\(f\)** na obélníku **\(D\)** **následujícími předpisy\[\begin{matrix}
\overline\int_D f(x, y) \, \text{d}x\text{d}y := \inf \set{S(f, \sigma) \, | \, \sigma \text{ dělení obdélníku } D},\\
\underline\int_D f(x, y) \, \text{d}x\text{d}y := \sup \set{s(f, \sigma) \, | \, \sigma \text{ dělení obdélníku } D}.
\end{matrix}\]Omezenou funkci \(f\) nazveme **Riemannovsky integrabilní na obdélníku **\(D\), právě když\[\overline\int_D f(x, y) \, \text dx \text dy = \underline\int_D f(x, y) \, \text dx \text dy.\]Tuto společnou hodnotu nazveme **Riemannovým integrálem funkce **\(f\)** na obdélníku **\(D\) a značíme ji \(\int _D f(x, y) \, \mathrm dx \mathrm dy\) nebo \(\int_D f\).

## Poznámka Anki 1671464420943

Karty Anki: 1671464420943
GUID: n=IO;Y0Fjy; štítky: bi-ma2::p18 duplicate ni-spol::04.

### Otázka (Front)

Definujte množinu typu 1 a množinu typu 2.

### Odpověď (Back)

Omezíme se na dvourozměrný případ \(D \subset \mathbb R^2\) a zavedeme dva typy množiny:

- **Typ 1**: existuje interval \(J = \langle a, b \rangle\) a dvě spojité funkce \(\varphi_1\) a \(\varphi_2\) definované na \(J\) a splňující \(\varphi_1(x) \leq \varphi_2(x)\) pro všechna \(x \in J\) tak, že

\[D = \set{(x, y) \in \mathbb R^2 \, | \, x \in J \land \varphi_1(x) \leq  y \leq \varphi_2(x)}.\]

- **Typ 2**: existuje interval \(J = \langle a, b\rangle\) a dvě spojité funkce \(\psi_1 \) a \(\psi_2\) definované na \(J\) a splňující \(\psi_1(y) \leq \psi_2(y)\) pro všechna \(y \in J\) tak, že

\[D = \set{(x, y) \in \mathbb R^2 \, | \, y \in J \land \psi_1(y) \leq x \leq \psi_2(y)}.\]

 [Obrázek: paste-45e96d5cd8bda19486c7d7b4ee4968e28c0e5e3e.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1671464742193

Karty Anki: 1671464742193
GUID: hIgmY4H^E0; štítky: bi-ma2::p18 duplicate ni-spol::04.

### Otázka (Front)

Jak integrujeme přes množiny typu 1 a typu 2?

### Odpověď (Back)

- Máme-li množinu \(D \subset \mathbb R^2\) typu 1 nebo 2, pak Riemannův integrál definujeme takto: množinu \(D\) vnoříme do vhodného obdélníku \(K\), tj. \(D \subset K\), a funkce vně \(D\) dodefinujeme/předefinujeme nulou.
- Na obdélníku \(K \supset D\) definujeme funkci

\[g(x, y) = \begin{cases}
f(x, y), && (x, y) \in D, \\
0, && (x, y) \notin D.
\end{cases}\]

- A klademe

\[\int_D f(x, y) \, \text dx \text dy := \int_K g(x, y) \, \text dx \text dy.\]

 [Obrázek: paste-e9afeb440bcdc1c0f2dd2f82932d141e4f2f4edd.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1671718879725

Karty Anki: 1671718879762
GUID: CRW7w?vTN:; štítky: bi-ma2::p18.

### Otázka (Front)

Vyslovte větu o postačující podmínce existence vícerozměrného integrálu.

### Odpověď (Back)

Nechť \(D\) je hyperkvádr nebo množina typu 1 nebo 2 a \(f\) spojitá funkce na \(D\). Potom je funkce \(f\) Riemannovsky integrabilní na množině \(D\).

## Poznámka Anki 1671719308902

Karty Anki: 1671719308902
GUID: FYVa&|8P_D; štítky: bi-ma2::p18 duplicate ni-spol::04.

### Otázka (Front)

Popište vlastnosti vícerozměrného Riemannova integrálu.

### Odpověď (Back)

Mějme \(D \subset \mathbb R^2\) množinu typu 1 nebo typu 2 (zahrnuje případ obdélníku) a funkce \(f\) a \(g\) na ní spojité. Potom platí:

- **linearita** - máme-li konstantu \(c \in \mathbb R\), pak

\[\int_D (f + cg) = \int_D f + c \int_D g;\]

- **nerovnosti **- pokud \(f(x,y) \leq g(x,y)\) pro každé \((x, y)^T \in D\), pak

\[\int_D f \leq \int_D g;\]

- **obsah množiny **- obsah \(\operatorname{Vol}_2(D)\)** **množiny** **\(D\) lze spočítat jako

\[\operatorname{Vol}_2(D) = \int_D \, 1;\]

- **chování v „mezích“ **- je-li \(C\) další množina typu 1 nebo typu 2 mající s množinou \(D\) v průniku pouze část „hranice“, pak\[\int_{C \cup D} f = \int_C f + \int_D f.\]

Analogická tvrzení platí i pro hyperkvádry \(K \subset \mathbb R^n\) a funkce na nich spojité.

### Doplňující pole (Extra)

Přepoklady vlasnosti chování v „mezích“ mezích lze také formulovat tak, že platí, pokud jsou \(C\) a \(D\) uzavřené omezené množiny a jejich průnik je množina míry nula.

## Poznámka Anki 1671719877866

Karty Anki: 1671719877866
GUID: Ei5@HR/fzM; štítky: bi-ma2::p18 duplicate ni-spol::04.

### Otázka (Front)

Vyslovte Fubiniho větu pro hyperkvádr.

### Odpověď (Back)

Buď \(f\) Riemannovsky integrabilní na obdélníku \(D = \langle a_1, b_1 \rangle \times \langle a_2, b_2 \rangle\). Pokud existuje jeden z integrálů
\[\int_{a_1}^{b_1} \bigg( \int_{a_2}^{b_2} f(x, y) \, \text dy \bigg) \, \text dx \quad \text{nebo} \quad \int_{a_2}^{b_2} \bigg( \int_{a_1}^{b_1} f(x, y) \, \text dx \bigg) \, \text dy,\]potom je roven Riemannově integrálu
\[\int_D f(x, y) \, \text dx \text dy.\]

## Poznámka Anki 1671720218314

Karty Anki: 1671720218314
GUID: H>V(]KSX5c; štítky: bi-ma2::p18.

### Otázka (Front)

Vyslovte větu integraci funkcí se separovanými proměnnými. Z čeho tato věta plyne?

### Odpověď (Back)

Důsledkem Fubiniho věty je, že pokud integrujeme funkci tvaru \(f(x, y) = g(x)h(y)\) na obdélníku \(D = \langle a_1, b_1 \rangle \times \langle a_2, b_2 \rangle\), pak
\[\int_D f(x, y) \, \text dx \text dy = \int_{a_1}^{b_1} g(x) \, \text dx \cdot \int_{a_2}^{b_2} h(y) \, \text dy.\]

## Poznámka Anki 1671720880726

Karty Anki: 1671720880726
GUID: sp{iuYW#Sa; štítky: bi-ma2::p18 duplicate ni-spol::04.

### Otázka (Front)

Vyslovte Fubiniho větu pro množiny typu 1 nebo 2.

### Odpověď (Back)

Buď \(f\) spojitá na množině \(D\) typu 1 nebo 2. Potom pro množinu typu 1 platí\[\int _D f(x, y) \, \mathrm dx \mathrm dy = \int_a^b \bigg( \int_{\varphi_1(x)}^{\varphi_2(x)} f(x, y) \, \mathrm dy \bigg) \, \mathrm dx\]a obdobně pro množinu typu 2\[\int _D f(x, y) \, \mathrm dx \mathrm dy = \int_a^b \bigg( \int_{\psi_1(y)}^{\psi_2(y)} f(x, y) \, \mathrm dx \bigg) \, \mathrm dy.\]

