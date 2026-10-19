# NI-MPI – Přednáška 05

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 31 poznámek, 31 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1729075996602

Karty Anki: 1729075996602
GUID: k|f$Qh@g5,; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Definujte dělení, dělící body, částečné intervaly intervalu \(\langle a, b \rangle\) a normu dělení.

### Odpověď (Back)

Mějme interval \(\langle a, b \rangle\). **Dělením **tohoto **intervalu **nazveme konečnou množinu\[\sigma = \set{x_0, x_1, \dots, x_n}\]takovou, že\[a = x_0 < x_1 < \cdots < x_n = b.\]Body \(x_k\), \(k = 1, 2, \dots, n - 1\) nazýváme **dělícími body intervalu** \(\langle a, b \rangle\) a interval \(\langle x_{k-1}, x_k \rangle\) \(k\)-tým **částečným intervalem** **intervalu **\(\langle a, b \rangle\). Číslo\[\nu(\sigma)  := \max \set{\Delta_k \mid k \in \hat n},\]kde\[\Delta_k := x_k - x_{k-1}, \quad k \in \hat n\]nazáváme **normou dělení** \(\sigma\).

## Poznámka Anki 1729076103751

Karty Anki: 1729076103752
GUID: dQu>%v^VXa; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Definujte horní a dolní součet.

### Odpověď (Back)

Buďte funkce \(f\) definovaná a omezená na intervalu \(J = \langle a, b \rangle\) a \(\sigma = \set{x_0, x_1, \dots, x_n}\) dělení intervalu \(J\). Označme \(M_i(\sigma, f) := \sup \limits_{\langle x_{i-1}, x_i \rangle} f\) a \( m_i(\sigma, f) := \inf \limits_{\langle x_{i-1}, x_i \rangle} f\) pro každé \(i = 1, 2, \dots, n\). Potom součty \(S(\sigma, f) := \sum \limits_{i = 1} ^{n} M_i(\sigma, f) \Delta_i\) a \(s(\sigma, f) := \sum \limits_{i = 1} ^{n} m_i(\sigma, f) \Delta_i\) nazýváme **horním**, resp. **dolním**, **součtem funkce **\(f\) při dělení \(\sigma\).

## Poznámka Anki 1729076529443

Karty Anki: 1729076529443
GUID: BUc]XHbeMd; štítky: ni-mpi::p05.

### Otázka (Front)

Definujte Darbouxův integrál funkce.

### Odpověď (Back)

Pokud pro funkci \(f\) definovanou a omezenou na uzavřeném intervalu \(J = \langle a, b \rangle\) platí 
\[\overline{\int_a^b} f(x) \, \mathrm dx = \underline{\int_a^b} f(x) \, \mathrm dx \in \mathbb{R},\]pak jejich společnou hodnotu nazýváme Darbouxovým integrálem funkce \(f\) na intervalu \(J\) a toto číslo zančíme symboly \(\int_a^b f\), případně \(\int_a^b f(x) \, \mathrm dx\).

## Poznámka Anki 1729076608895

Karty Anki: 1729076608895
GUID: iv[_?ZQ8l&; štítky: ni-mpi::p05.

### Otázka (Front)

Vyslovte větu o postačující podmínce pro existenci Darbouxova integrálu. Popište souvislost s horním a dolním součtem.

### Odpověď (Back)

Buď \(f\) spojitá funkce na intervalu \(\langle a, b \rangle\). Potom existuje její Darbouxův integrál na intervalu \(\langle a, b \rangle\).
Pokud je navíc \((\sigma_n)_{n=1}^\infty\) normální posloupnost dělení intervalu \(\langle a, b \rangle\) potom limity \(\lim \limits_{n \to \infty} s(\sigma_n, f)\) a \(\lim \limits_{n \to \infty} S(\sigma_n, f)\) existují, a jsou rovny Darbouxově integrálu funkce \(f\) na intervalu \(\langle a, b \rangle\).

## Poznámka Anki 1729076992572

Karty Anki: 1729076992572
GUID: tN$@wuswJ; štítky: ni-mpi::p05.

### Otázka (Front)

Vyslovte větu o aditivitě Darbouxova integrálu.

### Odpověď (Back)

Nechť \(f\) a \(g\) jsou spojité funkce na intervalu \(\langle a, b \rangle\). Potom pro Darbouxův integrál funkce \(f + g\) (která je také automaticky spojitá na \(\langle a, b \rangle\)) platí\[\int_a^b(f+g)(x) \, \mathrm dx = \int_a^bf(x) \, \mathrm dx + \int_a^bg(x) \, \mathrm dx.\]

## Poznámka Anki 1729077005739

Karty Anki: 1729077005739
GUID: xPDE}]BOg(; štítky: ni-mpi::p05.

### Otázka (Front)

Vyslovte větu o multiplikativitě Darbouxova integrálu.

### Odpověď (Back)

Nechť \(f\) je spojitá na intervalu \(\langle a, b \rangle\) a \(c \in \mathbb{R}\) je konstanta. Potom pro Darbouxův integrál funkce \(cf\) platí\[\int_a^b(cf)(x) \, \text dx = c\int_a^bf(x) \, \text dx.\]

## Poznámka Anki 1729077061853

Karty Anki: 1729077061854
GUID: imP5a*d]wa; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Definujte primitivní funkci.

### Odpověď (Back)

Mějme funkci \(f\) definovanou na intervalu \((a, b)\), kde\[−\infty \leq a < b \leq +\infty.\]Funkci \(F\) splňující podmínku\[F'(x) = f(x), \quad \forall x \in (a, b)\]nazýváme primitivní funkcí k funkci \(f\) na intervalu \((a, b)\).

### Doplňující pole (Extra)

Z definice plyne, že \(F\) je diferencovatelná a tedy i spojitá v každém bodě intervalu \((a, b)\).

## Poznámka Anki 1729077143901

Karty Anki: 1729077143901
GUID: v#kHTXN>@%; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int \frac{1}{\sin^2(x)} \, \mathrm dx\), když \(x \in (k\pi, \pi + k\pi), k \in \mathbb{Z}\).

### Odpověď (Back)

\[\int \frac{1}{\sin^2(x)} \, \mathrm dx = -\operatorname{cotg}(x) + C\]

## Poznámka Anki 1729077159370

Karty Anki: 1729077159370
GUID: yE@zoBERqL; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int x^n \, \mathrm dx\), když \(x \in \mathbb{R}, n\in N_0\).

### Odpověď (Back)

\[\int x^n \, \mathrm dx = \frac{x^{n+1}}{n+1} + C\]

## Poznámka Anki 1729077176465

Karty Anki: 1729077176465
GUID: QCZXHRomD#; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int x^n \, \mathrm dx\), když \(x \in \mathbb{R} \smallsetminus \{0\}, n \in \mathbb{Z}, n \leq -2\).

### Odpověď (Back)

\[\int x^n \, \mathrm dx = \frac{x^{n+1}}{n+1} + C\]

## Poznámka Anki 1729077195864

Karty Anki: 1729077195864
GUID: uL)E/w?39d; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int x^\alpha \, \mathrm dx\), když \(x \in (0, +\infty), a \notin \mathbb{Z}\).

### Odpověď (Back)

\[\int x^\alpha \, \mathrm dx = \frac{x^{\alpha+1}}{\alpha+1} + C\]

## Poznámka Anki 1729077208709

Karty Anki: 1729077208709
GUID: CjH$/X3MDc; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int \frac{1}{x} \, \mathrm dx\), když \(x \in \mathbb{R} \smallsetminus \{0\}\).

### Odpověď (Back)

\[\int \frac 1 x \, \text dx = \ln |x| + C\]

## Poznámka Anki 1729077220869

Karty Anki: 1729077220869
GUID: tHGjV#pW&O; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int a^x \, \mathrm dx\), když \(x \in \mathbb{R}, a > 0\) a \(a \neq 1\).

### Odpověď (Back)

\[\int a^x \, \mathrm dx = \frac{a^x}{\ln a} + C\]

## Poznámka Anki 1729077230302

Karty Anki: 1729077230302
GUID: NVUD{%g;@*; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int \sin(x) \, \mathrm dx\), když \(x \in \mathbb{R}\).

### Odpověď (Back)

\[\int \sin(x) \, \mathrm dx = -\cos(x) + C\]

## Poznámka Anki 1729077239662

Karty Anki: 1729077239662
GUID: v8qWfIC)md; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int \cos(x) \, \mathrm dx\), když \(x \in \mathbb{R}\).

### Odpověď (Back)

\[\int \cos(x) \, \mathrm dx = \sin(x) + C\]

## Poznámka Anki 1729077248900

Karty Anki: 1729077248900
GUID: PK,w@BV;G; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int \frac{1}{\cos^2(x)} \, \text dx\), když \(x \in (-\frac{\pi}{2} + k\pi, \frac{\pi}{2} + k\pi), k \in \mathbb{Z}\).

### Odpověď (Back)

\[\int \frac{1}{\cos^2(x)} \, \text dx = \operatorname{tg}(x) + C\]

## Poznámka Anki 1729077268112

Karty Anki: 1729077268113
GUID: o=d;TF6}-s; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int \frac{1}{\sqrt{1-x^2}} \, \mathrm dx\), když \(x \in (-1, 1)\).

### Odpověď (Back)

\[\int \frac 1 {\sqrt{1 - x^2}} \, \mathrm dx = \arcsin(x) + C\]

## Poznámka Anki 1729077275894

Karty Anki: 1729077275894
GUID: k|A2Qi<uo_; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vypočtěte \(\int \frac{1}{1+x^2} \, \mathrm dx\), když \(x \in \mathbb{R}\).

### Odpověď (Back)

\[\int \frac{1}{1+x^2} \, \mathrm dx= \operatorname{arctg}(x) + C\]

## Poznámka Anki 1729077565289

Karty Anki: 1729077565289
GUID: IeKj,E5l@; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vyslovte větu o Newtonově formuli.

### Odpověď (Back)

Nechť \(f\) je funkce spojitá na intervalu \(\langle a, b \rangle\) s primitivní funkcí \(F\). Pak platí rovnost
\[\int_a^b f(x) \, \mathrm  dx = \displaystyle \lim_{x \to b_-} F(x) - \displaystyle \lim_{x \to a_+} F(x) =: \Big[ F(x) \Big]_a^b.\]

### Doplňující pole (Extra)

Ve skutečnosti nemusí být funkce \(f\) v bodech \(a\) a \(b\) spojitá a platí obecnější vztah:
\[\int_a^b f(x) \, \mathrm  dx = \displaystyle \lim_{x \to b_-} F(x) - \displaystyle \lim_{x \to a_+} F(x) =: \Big[ F(x) \Big]_a^b.\]

## Poznámka Anki 1729077664990

Karty Anki: 1729077664990
GUID: xGkCK:b3td; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vyslovte větu o per partes pro určitý integrál.

### Odpověď (Back)

Nechť \(f\) a \(g\) jsou funkce spojité na \( \langle a, b \rangle\), \(f\) má spojitou derivaci na intervalu \(\langle a, b \rangle\) a nechť \(G\) je primitivní funkce k funkci \(g\) na intervalu \(\langle a, b \rangle\). Potom
\[\int_a^b f(x)g(x) \, \text dx = \big[ f(x)G(x) \big]_a^b - \int_a^b f'(x)G(x) \, \text dx.\]

## Poznámka Anki 1729077716875

Karty Anki: 1729077716875
GUID: kv}?~@ov2[; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vyslovte větu o substituci (I) v určitém integrálu.

### Odpověď (Back)

Nechť pro funkce \(f\) a \(\varphi\) platí

- \(\varphi\) a její derivace \(\varphi'\) jsou spojité na \(\langle \alpha, \beta \rangle\),

- \(f\) je spojitá na \(\varphi(\langle \alpha, \beta \rangle)\).

Potom

\[\int_\alpha^\beta f\big(\varphi(t)\big) \cdot \varphi'(t) \, \text dt = \int_{\varphi(\alpha)}^{\varphi(\beta)} f(x) \, \text dx.\]

## Poznámka Anki 1729078032048

Karty Anki: 1729078032048
GUID: N.iYZ~6z2!; štítky: duplicate ni-mpi::p05.

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

## Poznámka Anki 1729078341958

Karty Anki: 1729078341958
GUID: Qt)jg3/9Rw; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vyslovte Fubiniho větu pro hyperkvádr.

### Odpověď (Back)

Buď \(f\) Riemannovsky integrabilní na obdélníku \(D = \langle a_1, b_1 \rangle \times \langle a_2, b_2 \rangle\). Pokud existuje jeden z integrálů
\[\int_{a_1}^{b_1} \bigg( \int_{a_2}^{b_2} f(x, y) \, \text dy \bigg) \, \text dx \quad \text{nebo} \quad \int_{a_2}^{b_2} \bigg( \int_{a_1}^{b_1} f(x, y) \, \text dx \bigg) \, \text dy,\]potom je roven Riemannově integrálu
\[\int_D f(x, y) \, \text dx \text dy.\]

## Poznámka Anki 1729078403051

Karty Anki: 1729078403052
GUID: K^#6{i]TR.; štítky: duplicate ni-mpi::p05.

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

## Poznámka Anki 1729079775068

Karty Anki: 1729079775069
GUID: u^QP%}5l[U; štítky: ni-mpi::p05 ni-spol::04.

### Otázka (Front)

Definujte množinu míry nula.

### Odpověď (Back)

Množina \(Z \subset \mathbb R^2\) má míru nula, pokud pro každé \(\varepsilon > 0\) existují obdélníky\[R_i = \langle a_i, b_i \rangle \times \langle c_i, d_i \rangle, \quad i = 1, \dots, n\]tak, že\[Z \subset \bigcup_{i = 1}^n R_i \quad \text a \quad \displaystyle \sum_{i = 1}^n |b_i - a_i| \cdot |d_i - c_i| < \varepsilon.\]Množiny míry nula jsou pro hodnotu integrálu „zanedbatelné.“

## Poznámka Anki 1729080394349

Karty Anki: 1729080394349
GUID: E*#Zh.C$59; štítky: ni-mpi::p05 ni-spol::04.

### Otázka (Front)

Vyslovte větu o vztahu integrability a nespojitosti na množině míry nula.

### Odpověď (Back)

Omezená funkce \(f : D_f \to \mathbb R\), \(D_f = \langle a, b \rangle \times \langle c, d \rangle\), je integrabilní, pokud množina
\[\{ \mathbf x \in D_f : f \text{ není spojitá v } \mathbf x \}\]má míru nula. Z toho vyplývá, že spojitá funkce \(f : D_f \to \mathbb R\), která má na omezené množině \(D_f\) hranici míry nula, je integrabilní.

## Poznámka Anki 1729080540801

Karty Anki: 1729080540801
GUID: D[`IwS31[B; štítky: duplicate ni-mpi::p05.

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

- **chování v „mezích“ **- je-li \(C\) další množina typu 1 nebo typu 2 mající s množinou \(D\) v průniku pouze část „hranice“, pak

\[\int_{C \cup D} f = \int_C f + \int_D f.\]Analogická tvrzení platí i pro hyperkvádry \(K \subset \mathbb R^n\) a funkce na nich spojité.

### Doplňující pole (Extra)

Přepoklady vlasnosti chování v „mezích“ mezích lze také formulovat tak, že platí, pokud jsou \(C\) a \(D\) uzavřené omezené množiny a jejich průnik je množina míry nula.

## Poznámka Anki 1729080617196

Karty Anki: 1729080617196
GUID: H<^=]gqn_]; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Definujte množinu typu 1 a množinu typu 2.

### Odpověď (Back)

Omezíme se na dvourozměrný případ \(D \subset \mathbb R^2\) a zavedeme dva typy množiny:

- **Typ 1**: existuje interval \(J = \langle a, b \rangle\) a dvě spojité funkce \(\varphi_1\) a \(\varphi_2\) definované na \(J\) a splňující \(\varphi_1(x) \leq \varphi_2(x)\) pro všechna \(x \in J\) tak, že

\[D = \set{(x, y) \in \mathbb R^2 \, | \, x \in J \land \varphi_1(x) \leq  y \leq \varphi_2(x)}.\]

- **Typ 2**: existuje interval \(J = \langle a, b\rangle\) a dvě spojité funkce \(\psi_1 \) a \(\psi_2\) definované na \(J\) a splňující \(\psi_1(y) \leq \psi_2(y)\) pro všechna \(y \in J\) tak, že

\[D = \set{(x, y) \in \mathbb R^2 \, | \, y \in J \land \psi_1(y) \leq x \leq \psi_2(y)}.\]

 [Obrázek: paste-45e96d5cd8bda19486c7d7b4ee4968e28c0e5e3e.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1729081976743

Karty Anki: 1729081976743
GUID: ma~Q)+5TsY; štítky: ni-mpi::p05 ni-spol::04.

### Otázka (Front)

Definujte Jacobiho matici.

### Odpověď (Back)

Mějme \(\Psi : \mathbb R^n \to \mathbb R^n\), \(\Psi( \mathbf v) = \big (\Psi_1(\mathbf v), \dots, \Psi_n(\mathbf v) \big)\). Jacobiho matice zobrazení \(\Psi\) je následující zobrazení \(\mathbb R^n \to \mathbb R^{n, n}\) (pro \(\mathbf v = (v_1, \dots, v_n)\))
\[J_\Psi = \begin{pmatrix}
\frac{\partial \Psi_1}{\partial v_1} & \cdots & \frac{\partial \Psi_1}{\partial v_n}\\
\vdots & \ddots & \vdots\\
\frac{\partial \Psi_n}{\partial v_1} & \cdots & \frac{\partial \Psi_n}{\partial v_n}
\end{pmatrix},\]pokud všechny parciální derivace existují.

## Poznámka Anki 1729086570495

Karty Anki: 1729086570495
GUID: yLu-fvd2n); štítky: ni-mpi::p05 ni-spol::04.

### Otázka (Front)

Vyslovte větu o substituci v integrálu funkce více proměnných.

### Odpověď (Back)

Mějme spojitou funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\). Nechť je \(D \subset D_f\) omezená uzavřená množina, nechť má zobrazení \(\Psi : \mathbb R^n \to \mathbb R^n\) spojité všechny parciální derivace na nějaké otevřené nadmnožině množiny \(D\) a skoro všude na \(D\) platí, že:

- \(\Psi\) je bijekce,

- \(\det J_\Psi\) je nenulový.

Potom pro funkci \(f\) platí

\[\int_{\Psi(D)} f( \mathbf x) \, \mathrm d \mathbf x = \int_{D} f \big( \Psi(\mathbf v) \big) \cdot | \det J_\Psi(\mathbf v) | \, \mathrm d \mathbf v,\]kde \(\mathbf x = (x_1, \dots, x_n)\).

### Doplňující pole (Extra)

„Skoro všude“ zde znamená, že množina, na níž tvrzení neplatí, má míru nula.

## Poznámka Anki 1729524349248

Karty Anki: 1729524349248
GUID: x;*b{E*saI; štítky: duplicate ni-mpi::p05.

### Otázka (Front)

Vyslovte Fubiniho větu pro množiny typu 1 nebo 2.

### Odpověď (Back)

Buď \(f\) spojitá na množině \(D\) typu 1 nebo 2. Potom pro množinu typu 1 platí
\[\int _D f(x, y) \, \mathrm dx \mathrm dy = \int_a^b \bigg( \int_{\varphi_1(x)}^{\varphi_2(x)} f(x, y) \, \mathrm dy \bigg) \, \mathrm dx\]a obdobně pro množinu typu 2
\[\int _D f(x, y) \, \mathrm dx \mathrm dy = \int_a^b \bigg( \int_{\psi_1(y)}^{\psi_2(y)} f(x, y) \, \mathrm dx \bigg) \, \mathrm dy.\]

