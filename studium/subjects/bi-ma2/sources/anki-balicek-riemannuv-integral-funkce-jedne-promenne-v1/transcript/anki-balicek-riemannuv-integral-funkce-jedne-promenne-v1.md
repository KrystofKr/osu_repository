# BI-MA2 – Riemannův integrál funkce jedné proměnné

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2::Riemannův integrál funkce jedné proměnné
Rozsah: 18 poznámek, 18 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Původní definice matematických maker

```tex
\def\AAA{\mathcal{A}}
\def\BB{\mathcal{B}}
\def\CC{\mathbb{C}}
\def\DD{\mathcal{D}}
\def\EE{\mathcal{E}}
\def\FF{\mathcal{F}}
\def\GG{\mathcal{G}}
\def\HH{\mathcal{H}}
\def\II{\mathcal{I}}
\def\Im{\mathrm{Im}\,}
\def\JJ{\mathcal{J}}
\def\KK{\mathcal{K}}
\def\LL{\mathcal{L}}
\def\MM{\mathcal{M}}
\def\NN{\mathcal{N}}
\def\N{\mathbb{N}}
\def\OO{\mathcal{O}}
\def\PP{\mathcal{P}}
\def\QQ{\mathcal{Q}}
\def\Q{\mathbb{Q}}
\def\RR{\mathcal{R}}
\def\Re{\mathrm{Re}\,}
\def\R{\mathbb{R}}
\def\SSS{\mathcal{S}}
\def\TT{\mathcal{T}}
\def\UU{\mathcal{U}}
\def\VV{\mathcal{V}}
\def\WW{\mathcal{W}}
\def\XX{\mathcal{X}}
\def\YY{\mathcal{Y}}
\def\ZZ{\mathcal{Z}}
\def\Z{\mathbb{Z}}
\def\arcctg{arccotg}
\def\arctg{arctg}
\def\ceq{\mathrel{\mathop:}=}
\def\cotg{cotg}
\def\ctg{cotg}
\def\dt{\mathrm{d}t}
\def\dx{\mathrm{d}x}
\def\dy{\mathrm{d}y}
\def\dz{\mathrm{d}z}
\def\eR{\overline{\R}}
\def\ee{\mathrm{e}}
\def\fl{f \kern 0.04em l}
\def\ii{\mathrm{i}}
\def\lanO{\mathcal{O}}
\def\lano{o}
\def\lcm{lcm}
\def\mA{\mathbf{A}}
\def\mB{\mathbf{B}}
\def\mC{\mathbf{C}}
\def\mD{\mathbf{D}}
\def\mE{\mathbf{E}}
\def\mF{\mathbf{F}}
\def\mG{\mathbf{G}}
\def\mH{\mathbf{H}}
\def\mI{\mathbf{I}}
\def\mJ{\mathbf{J}}
\def\mK{\mathbf{K}}
\def\mL{\mathbf{L}}
\def\mM{\mathbf{M}}
\def\mN{\mathbf{N}}
\def\mO{\mathbf{O}}
\def\mP{\mathbf{P}}
\def\mQ{\mathbf{Q}}
\def\mR{\mathbf{R}}
\def\mSigma{\boldsymbol{\Sigma}}
\def\mS{\mathbf{S}}
\def\mT{\mathbf{T}}
\def\mU{\mathbf{U}}
\def\mV{\mathbf{V}}
\def\mW{\mathbf{W}}
\def\mX{\mathbf{X}}
\def\mY{\mathbf{Y}}
\def\mZ{\mathbf{Z}}
\def\sgn{\mathrm{sgn}}
\def\ssubset{\subset\subset}
\def\tg{tg}
\def\tr{tr}
\def\va{\mathbf{a}}
\def\vb{\mathbf{b}}
\def\vc{\mathbf{c}}
\def\vd{\mathbf{d}}
\def\vell{\boldsymbol{\ell}}
\def\veps{\varepsilon}
\def\ve{\mathbf{e}}
\def\vf{\mathbf{f}}
\def\vg{\mathbf{g}}
\def\vh{\mathbf{h}}
\def\vi{\mathbf{i}}
\def\vj{\mathbf{j}}
\def\vk{\mathbf{k}}
\def\vl{\mathbf{l}}
\def\vm{\mathbf{m}}
\def\vn{\mathbf{n}}
\def\vo{\mathbf{o}}
\def\vp{\mathbf{p}}
\def\vq{\mathbf{q}}
\def\vr{\mathbf{r}}
\def\vs{\mathbf{s}}
\def\vt{\mathbf{t}}
\def\vu{\mathbf{u}}
\def\vv{\mathbf{v}}
\def\vw{\mathbf{w}}
\def\vx{\mathbf{x}}
\def\vy{\mathbf{y}}
\def\vz{\mathbf{z}}
```

## Poznámka Anki 1672329270444

Karty Anki: 1672329270444
GUID: Jk:Pwn};kM; štítky: BI-MA2::chap_riemannuv_integral Definition.

### Otázka (Front)

Definice 3.1: Dělení intervalu

### Odpověď (Back)

Buď dán interval \(\langle a,b \rangle\).
  Konečnou množinu\[ \sigma = \{x_0,x_1,\ldots,x_n\} \]takovou, že\[ a = x_0 < x_1 < \cdots < x_n = b \]nazýváme **dělením intervalu**  \(\langle a,b \rangle\). Bodům \(x_k\), \(k=1,2,\ldots,n-1\), říkáme **dělící body intervalu**  \(\langle a,b \rangle\).
  Intervalu \(\langle x_{k-1},x_k \rangle\) říkáme **částečný interval** intervalu \(\langle a,b \rangle\) při dělení \(\sigma\).
  Číslo\[ \nu(\sigma) := \max \{ \Delta_k \mid k = 1,2,\ldots,n \},
    \quad \text{kde} \quad \Delta_k := x_k - x_{k-1}, \ k = 1,2,\ldots,n, \]nazýváme **normou dělení**  \(\sigma\).

## Poznámka Anki 1672329270445

Karty Anki: 1672329270445
GUID: tM8l:1(Zuc; štítky: BI-MA2::chap_riemannuv_integral Definition.

### Otázka (Front)

Definice 3.2: Ekvidistantní dělení

### Odpověď (Back)

Pro interval \(\langle a,b \rangle\) a \(n\in\mathbb{N}\) položme \(\Delta := \frac{b-a}{n}\) a\[ x_i := a + i\cdot\Delta, \quad i = 0,1,\ldots,n. \]Tedy\[ \sigma = \big\{ a, \, a + \Delta, \, a + 2 \Delta, \ldots, \, a + (n-1)\Delta, \, b \big\}. \]

## Poznámka Anki 1672329270446

Karty Anki: 1672329270446
GUID: Q;,}7p`&wP; štítky: BI-MA2::chap_riemannuv_integral Definition.

### Otázka (Front)

Definice 3.3: Dolní a horní součet funkce při dělení \(\sigma\)

### Odpověď (Back)

Buďte funkce \(f\) definovaná a omezená na intervalu \(J =\langle a,b \rangle\) a \(\sigma = \{x_0,x_1,\ldots,x_n\}\)  dělení intervalu \(J\).
  Součty\[\begin{aligned} S(\sigma,f) &:= \sum_{i=1}^n \Delta_i \sup_{\langle x_{i-1},x_i\rangle} f, \\
    s(\sigma,f) &:= \sum_{i=1}^n \Delta_i \inf_{\langle x_{i-1},x_i\rangle} f \end{aligned} \]nazýváme **horním součtem funkce** a **dolním součtem funkce**  **\(f\) při dělení \(\sigma\)**.

## Poznámka Anki 1672329270447

Karty Anki: 1672329270447
GUID: l2bMVQr4wu; štítky: BI-MA2::chap_riemannuv_integral Definition.

### Otázka (Front)

Definice 3.4: Dolní a horní integrál

### Odpověď (Back)

Pro funkci \(f\) definovanou a omezenou na uzavřeném intervalu \(J=\langle a,b \rangle\) pomocí dolních a horních součtů definujeme čísla\[\begin{aligned} \overline{\int_a^b} f(x) \,\,\mathrm{d}x &:= \inf\{ S(\sigma, f) \mid \sigma \ \text{dělení} \ J \}, \\
    \underline{\int_a^b} f(x) \,\,\mathrm{d}x &:= \sup\{ s(\sigma, f) \mid \sigma \ \text{dělení} \ J \}. \end{aligned} \]a nazýváme je **horním integrálem**, resp. **dolním integrálem**, **funkce \(f\) na intervalu \(J\)**.

## Poznámka Anki 1672329270448

Karty Anki: 1672329270448
GUID: ,r>^j_VFC; štítky: BI-MA2::chap_riemannuv_integral Definition.

### Otázka (Front)

Definice 3.5: Riemannův určitý integrál

### Odpověď (Back)

Mějme funkci \(f\) definovanou a omezenou na uzavřeném intervalu \(J\).
  Pokud pro její dolní a horní integrál na intervalu  \(J\) platí\[ \overline{\int_a^b} f(x)\,\,\mathrm{d}x = \underline{\int_a^b} f(x) \,\,\mathrm{d}x \in \mathbb{R}, \]pak jejich společnou hodnotu nazýváme **Riemannovým integrálem funkce \(f\) na intervalu \(J\)** a toto číslo značíme symboly\[ \int_a^b f, \quad \text{případně} \quad \int_a^b f(x)\,\,\mathrm{d}x. \]

## Poznámka Anki 1672329270449

Karty Anki: 1672329270449
GUID: QV(UhPsZ!Q; štítky: BI-MA2::chap_riemannuv_integral Definition.

### Otázka (Front)

Definice 3.6: Normální posloupnost dělení

### Odpověď (Back)

Posloupnost dělení  \(\sigma_n\) nazveme **normální**, pokud pro její normy platí\[ \lim_{n\to\infty} \nu(\sigma_n) = 0. \]

## Poznámka Anki 1672329270450

Karty Anki: 1672329270450
GUID: mHS!FQ|pRe; štítky: BI-MA2::chap_riemannuv_integral Theorem.

### Otázka (Front)

Věta 3.1: Postačující podmínka pro existenci Riemannova integrálu

### Odpověď (Back)

Buď \(f\) spojitá funkce na intervalu \(\langle a,b \rangle\).
  Potom existuje její Riemannův integrál na intervalu \(\langle a,b\rangle\).

Pokud je navíc \((\sigma_n)\)  normální posloupnost dělení intervalu \(\langle a,b \rangle\), potom limity\[ \lim_{n\to\infty} s(\sigma_n, f) \quad \text{a} \quad \lim_{n\to\infty} S(\sigma_n,f) \]existují, a jsou rovny Riemannově integrálu funkce \(f\) na intervalu \(\langle a,b \rangle\).

## Poznámka Anki 1672329270451

Karty Anki: 1672329270451
GUID: zw{&~.lDkP; štítky: BI-MA2::chap_riemannuv_integral Definition.

### Otázka (Front)

Definice 3.7: Integrální součet

### Odpověď (Back)

Pro funkci \(f\) spojitou na uzavřeném intervalu \(\langle a,b \rangle\) a dělení  \(\sigma = \{x_0,\,x_1,\ldots,\,x_n\}\), kde \(x_0 = a\) a \(x_n = b\), tohoto intervalu definujeme **integrální součet funkce \(f\) při dělení \(\sigma\)** předpisem\[ \mathcal{J}(\sigma,f) = \sum_{i=1}^n f(\alpha_i) \Delta_i, \]kde \(\alpha_i\) patří do intervalu \(\langle x_{i-1}, x_i \rangle\), \(i=1,2,\ldots,n\).

## Poznámka Anki 1672329270452

Karty Anki: 1672329270452
GUID: xv0em_cIxi; štítky: BI-MA2::chap_riemannuv_integral Theorem.

### Otázka (Front)

Věta 3.2: Aditivita integrálu

### Odpověď (Back)

Nechť \(f\) a \(g\) jsou spojité funkce na intervalu \(\langle a,b \rangle\).
  Potom pro Riemannův integrál funkce \(f+g\), která je také automaticky spojitá na intervalu \(\langle a,b \rangle\), platí\[ \int_a^b (f+g)(x)\,\,\mathrm{d}x = \int_a^b f(x)\,\,\mathrm{d}x + \int_a^b g(x)\,\,\mathrm{d}x. \]

## Poznámka Anki 1672329270453

Karty Anki: 1672329270453
GUID: B4-2b!Mc]W; štítky: BI-MA2::chap_riemannuv_integral Theorem.

### Otázka (Front)

Věta 3.3: Multiplikativita integrálu

### Odpověď (Back)

Nechť \(f\) je spojitá na intervalu \(\langle a,b \rangle\) a \(c\in\mathbb{R}\) je konstanta.
  Potom pro Riemannův integrál funkce \(cf\) platí\[ \int_a^b (cf)(x)\,\,\mathrm{d}x = c \int_a^b f(x)\,\,\mathrm{d}x. \]

## Poznámka Anki 1672329270454

Karty Anki: 1672329270454
GUID: ~mQ.Vj|S1; štítky: BI-MA2::chap_riemannuv_integral Theorem.

### Otázka (Front)

Věta 3.4: Aditivita integrálu v mezích

### Odpověď (Back)

Riemannův integrál funkce \(f\) na intervalu \(\langle a, b \rangle\) existuje, právě když pro každé \(c \in (a,b)\) existují Riemannovy integrály funkce \(f\) na intervalech \(\langle a, c \rangle\) a \(\langle c, b \rangle\).
  V takovém případě navíc platí\[ \int_a^b f(x)\,\,\mathrm{d}x  = \int_a^c f(x)\,\,\mathrm{d}x + \int_c^b f(x)\,\,\mathrm{d}x. \]

## Poznámka Anki 1672329270455

Karty Anki: 1672329270455
GUID: f6!l11h3-$; štítky: BI-MA2::chap_riemannuv_integral Theorem.

### Otázka (Front)

Věta 3.5: Nerovnosti mezi integrály

### Odpověď (Back)

Nechť jsou \(f\) a \(g\) spojité funkce na intervalu \(\langle a,b \rangle\) a nechť platí nerovnost \(f(x) \leq g(x)\) pro všechna \(x\in\langle a,b \rangle\).
  Potom pro jejich Riemannovy integrály platí\[ \int_a^b f(x)\,\,\mathrm{d}x \leq \int_a^b g(x)\,\,\mathrm{d}x. \]

## Poznámka Anki 1672329270456

Karty Anki: 1672329270456
GUID: O@3$-46:mY; štítky: BI-MA2::chap_riemannuv_integral Theorem.

### Otázka (Front)

Věta 3.6: Newtonova formule

### Odpověď (Back)

Nechť \(f\) je funkce spojitá na intervalu \(\langle a,b \rangle\) s primitivní funkcí  \(F\).
  Pak pro Riemannův integrál funkce \(f\) na intervalu \(\langle a,b \rangle\) platí rovnost\[ \int_a^b f(x) \,\,\mathrm{d}x = F(b) - F(a) =: \Big[ F(x) \Big]_a^b. \]

## Poznámka Anki 1672329270457

Karty Anki: 1672329270457
GUID: Ba6`E8xg[&; štítky: BI-MA2::chap_riemannuv_integral Theorem.

### Otázka (Front)

Věta 3.7: Metoda per partes (určitý integrál)

### Odpověď (Back)

Nechť \(f\) a \(g\) jsou funkce spojité na \(\langle a,b \rangle\), \(f\) má spojitou derivaci na intervalu \(\langle a,b \rangle\) a nechť \(G\) je primitivní funkce k funkci \(g\) na intervalu \(\langle a,b \rangle\).
  Potom\[ \int_a^b f(x) g(x) \,\,\mathrm{d}x = \big[ f(x) G(x) \big]_a^b - \int_a^b f'(x) G(x) \,\mathrm{d}x. \]

## Poznámka Anki 1672329270458

Karty Anki: 1672329270458
GUID: B=w[EDT`t1; štítky: BI-MA2::chap_riemannuv_integral Theorem.

### Otázka (Front)

Věta 3.8: O substituci (určitý integrál)

### Odpověď (Back)

Nechť pro funkce \(f\) a \(\varphi\) platí

1. 

\(\varphi\) a její derivace \(\varphi'\) jsou spojité na \(\langle \alpha,\beta \rangle\),

2. 

\(f\) je spojitá na \(\varphi\big(\langle\alpha,\beta\rangle\big)\).

Potom pro Riemannův integrál platí\[ \int_\alpha^\beta f\big(\varphi(t)\big)\cdot\varphi'(t) \,\mathrm{d}t = \int_{\varphi(\alpha)}^{\varphi(\beta)}
    f(x)\,\,\mathrm{d}x. \]

## Poznámka Anki 1672329270459

Karty Anki: 1672329270459
GUID: zA{Lw;O#UZ; štítky: BI-MA2::chap_riemannuv_integral Theorem.

### Otázka (Front)

Věta 3.9: Integrace na symetrickém intervalu

### Odpověď (Back)

Nechť \(f\) je funkce spojitá na uvažovaných intervalech.

1. 

Je-li \(f\) sudá funkce na \(\langle -a,a \rangle\), pak \(\displaystyle\int_{-a}^a f(x) \,\mathrm{d}x = 2 \int_0^a f(x) \,\mathrm{d}x\).

2. 

Je-li \(f\) lichá funkce na \(\langle -a,a \rangle\), pak \(\displaystyle\int_{-a}^a f(x) \,\mathrm{d}x = 0\).

3. 

Je-li \(f\) periodická na \(\mathbb{R}\) s periodou \(T\), pak pro každé \(a,b\in\mathbb{R}\) platí \(\displaystyle\int_a^{a+T} f(x)\,\mathrm{d}x = \int_b^{b+T} f(x) \,\mathrm{d}x\).

## Poznámka Anki 1672329270460

Karty Anki: 1672329270460
GUID: Eo~K;V6`aP; štítky: BI-MA2::chap_riemannuv_integral Definition.

### Otázka (Front)

Definice 3.8: Zobecněný Riemannův integrál

### Odpověď (Back)

Nechť \(f\) je funkce definovaná na intervalu \(\langle a, b)\) pro nějaké \(a \in \mathbb{R}\) a \(b \in (a, +\infty) \cup \{+\infty\}\), která má Riemannův integrál na intervalu \(\langle a, c \rangle\) pro každé \(c \in (a,b)\).
  Pokud existuje konečná limita\[ \lim_{c \to b_-} \int_a^c f(x)\, \,\mathrm{d}x, \]pak její hodnotu značíme\[ \int_a^b f(x)\, \,\mathrm{d}x, \]nazýváme **zobecněným Riemannovým integrálem** funkce \(f\) na intervalu \(\langle a, b)\) a říkáme, že integrál \(\int_a^b f(x)\, \,\mathrm{d}x\) konverguje.

## Poznámka Anki 1672329270461

Karty Anki: 1672329270461
GUID: oLA~kO2gC*; štítky: BI-MA2::chap_riemannuv_integral Definition.

### Otázka (Front)

Definice 3.9: Absolutně konvergentní zobecněný Riemannův integrál na \(\mathbb{R}\)

### Odpověď (Back)

Buď \(f\) spojitá funkce definovaná na \(\mathbb{R}\).
  Pokud existuje konečná limita\[ \lim_{c\to+\infty} \int_{-c}^{c} |f(x)| \,\,\mathrm{d}x, \]pak tuto její hodnotu značíme\[ \int_{-\infty}^{+\infty} |f(x)| \,\,\mathrm{d}x \]a o \(f\) říkáme, že má **absolutně konvergentní zobecněný Riemannův integrál na**  \(\mathbb{R}\).
  Pokud má funkce absolutně konvergentní zobecněný Riemannův integrál na \(\mathbb{R}\), pak i limita\[ \lim_{c\to+\infty} \int_{-c}^{c} f(x) \,\,\mathrm{d}x \]existuje a značíme ji\[ \int_{-\infty}^{+\infty} f(x)\,\,\mathrm{d}x. \]Tuto hodnotu pak nazýváme **zobecněným Riemannovým integrálem \(f\) na \(\mathbb{R}\)**.

