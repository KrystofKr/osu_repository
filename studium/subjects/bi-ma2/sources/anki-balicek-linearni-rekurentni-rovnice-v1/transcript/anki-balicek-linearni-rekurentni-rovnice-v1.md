# BI-MA2 – Lineární rekurentní rovnice

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2::Lineární rekurentní rovnice
Rozsah: 17 poznámek, 17 karet.
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

## Poznámka Anki 1672329229380

Karty Anki: 1672329229380
GUID: NFip1Q/MQa; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Definition.

### Otázka (Front)

Definice 6.1: Lineární rekurentní rovnice

### Odpověď (Back)

**Lineární rekurentní rovnice řádu \(k \in \mathbb{N}\)** (zkráceně LRR) je rovnice tvaru\[ x_{n+k} + c_{k-1,n} \cdot x_{n+k-1} + \cdots + c_{1,n} \cdot x_{n+1} + c_{0,n} \cdot x_n = b_n, \quad n \in \mathbb{z}, \ n \geq n_0, \]kde \(n_0 \in \mathbb{z}\) a \((c_{i,n})_{n=n_0}^\infty\), \(i = 0,1,\ldots,k-1\), (tzv. **koeficienty rovnice**) a \((b_n)_{n=n_0}^\infty\) (tzv. **pravá strana rovnice**) jsou zadané posloupnosti a posloupnost \((c_{0,n})_{n=n_0}^\infty\) není nulová posloupnost.
  Jestliže \(b_n = 0\) pro každé \(n \geq n_0\), pak se příslušná rovnice nazývá **homogenní**. **Přidruženou homogenní rovnicí** k rovnici (6.2) nazýváme LRR se stejnými koeficienty a nulovou pravou stranou (\(b_n = 0\) pro každé \(n \geq n_0\)).

## Poznámka Anki 1672329229381

Karty Anki: 1672329229381
GUID: I##jsmwwEJ; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Definition.

### Otázka (Front)

Definice 6.2: Řešení LRR

### Odpověď (Back)

Nechť je dána lineární rekurentní rovnice řádu \(k \in \mathbb{N}\),\[ x_{n+k} + c_{k-1,n} x_{n+k-1} + \cdots + c_{1,n} x_{n+1} + c_{0,n} x_n = b_n, \quad n \in \mathbb{z}, \ n \geq n_0. \]Jejím **řešením** nazveme libovolnou posloupnost \((x_n)_{n=n_0}^\infty\) takovou, že dosazením jejích členů do (6.3) dostaneme pravdivé rovnosti pro každé celočíselné \(n \geq n_0\).

## Poznámka Anki 1672329229382

Karty Anki: 1672329229382
GUID: n;%(W5q1:&; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Definition.

### Otázka (Front)

Definice 6.3: Počáteční podmínky

### Odpověď (Back)

Nechť je dána lineární rekurentní rovnice řádu \(k \in \mathbb{N}\),\[ x_{n+k} + c_{k-1,n} x_{n+k-1} + \cdots + c_{1,n} x_{n+1} + c_{0,n} x_n = b_n, \quad n \in \mathbb{z}, \ n \geq n_0. \]**Počátečními podmínkami** pro tuto rovnici nazveme libovolnou soustavu rovností \(x_{n_0} = A_0\), \(x_{n_0 + 1} = A_1\), …, \(x_{n_0 + k - 1} = A_{k-1}\), pro zadané hodnoty \(A_0,\ldots,A_{k-1} \in \mathbb{R}\).

## Poznámka Anki 1672329229383

Karty Anki: 1672329229383
GUID: IlM/7)ca8*; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Question.

### Otázka (Front)

Otázka 6.1: 

Proč jsme nezavedli LRR nultého řádu?
  Je to vůbec možné?

### Odpověď (Back)

V definici LRR lze položit \(k = 0\), ale výslednou rovnici nelze považovat za rekurentní. Dostali bychom explicitní předpis \(x_n = b_n\), \(n \geq n_0\). V tomto případě není co řešit.

## Poznámka Anki 1672329229384

Karty Anki: 1672329229384
GUID: d-(Bf}fbv]; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Theorem.

### Otázka (Front)

Věta 6.1: O existenci a jednoznačnosti řešení LRR

### Odpověď (Back)

Platí dvě následující tvrzení.

1. 

Každá lineární rekurentní rovnice má nějaké řešení.

2. 

Je-li dána lineární rekurentní rovnice řádu \(k \in \mathbb{N}\) s předepsanými počátečními podmínkami, pak existuje právě jedno řešení této rovnice splňující tyto počáteční podmínky.

## Poznámka Anki 1672329229385

Karty Anki: 1672329229385
GUID: wXQ(O:SPQC; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Theorem.

### Otázka (Front)

Věta 6.2: Princip superpozice

### Odpověď (Back)

Uvažme dvě LRR \(k\)-tého řádu s ne nutně shodnými pravými stranami,\[ x_{n+k} + \sum_{i=0}^{k-1} c_{i,n} x_{n+i} = \clr{red}{b_n}, \]a\[ x_{n+k} + \sum_{i=0}^{k-1} c_{i,n} x_{n+i} = \clr{red}{\tilde{b}_n}, \]pro \(n \in \mathbb{z}\), \(n \geq n_0\).
  Je-li \((X_n)_{n = n_0}^\infty\) řešení rovnice (6.4) a \((Y_n)_{n = n_0}^\infty\) řešení rovnice (6.5), potom pro libovolnou konstantu \(\alpha\) je posloupnost \((X_n + \alpha Y_n)_{n = n_0}^\infty\) řešením LRR\[ x_{n+k} + \sum_{i=0}^{k-1} c_{i,n} x_{n+i} = \clr{red}{b_n + \alpha \tilde b_n}, \quad n \geq n_0. \]

## Poznámka Anki 1672329229386

Karty Anki: 1672329229386
GUID: g<eimzx*yg; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Theorem.

### Otázka (Front)

Věta 6.3: O struktuře množiny řešení LRR

### Odpověď (Back)

Mějme LRR řádu \(k \in \mathbb{N}\) tvaru\[ x_{n+k} + \sum_{i=0}^{k-1} c_{i,n} x_{n+i} = b_n, \quad n \in \mathbb{z}, \ n \geq n_0, \]a označme množinu všech jejích řešení symbolem \(S\) a množinu všech řešení přidružené homogenní rovnice symbolem \(S_0\).
  Potom platí následující tvrzení:

1. 

Množina \(S_0\) je vektorový prostor dimenze \(k\).

2. 

Množina \(S\) je tvaru \(S = (\tilde{x}_n)_{n=n_0}^\infty + S_0\), kde \((\tilde{x}_n)_{n=n_0}^\infty\) je (partikulární) řešení rovnice (6.6).

## Poznámka Anki 1672329229387

Karty Anki: 1672329229387
GUID: y>mq~D>I&l; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Definition.

### Otázka (Front)

Definice 6.4: LRR s konstantními koeficienty

### Odpověď (Back)

**Lineární rekurentní rovnice řádu \(k \in \mathbb{N}\) s konstantními koeficienty** je lineární rekurentní rovnice řádu \(k\) tvaru\[ x_{n+k} + c_{k-1} \cdot x_{n+k-1} + \cdots + c_{1} \cdot x_{n+1} + c_{0} \cdot x_n = b_n, \quad n \in \mathbb{z}, \ n \geq n_0, \]kde \(n_0 \in \mathbb{z}\) a \(c_{i} \in \mathbb{R}\), \(i = 0,1,\ldots,k-1\), \(c_0 \neq 0\), jsou zadané konstanty a \((b_n)_{n=n_0}^\infty\) je zadaná posloupnost.

## Poznámka Anki 1672329229388

Karty Anki: 1672329229388
GUID: nF~pV6:JPq; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Definition.

### Otázka (Front)

Definice 6.5: Charakteristický polynom LRR s konstantními koeficienty

### Odpověď (Back)

**Charakteristickým polynomem rovnice**  (6.8) nazýváme polynom stupně \(k\) tvaru\[ p(\lambda) = \lambda^k + c_{k-1} \lambda^{k - 1} + \cdots + c_1 \lambda + c_0. \]Kořeny tohoto polynomu se nazývají **charakteristická (nebo vlastní) čísla rovnice**  (6.8).

## Poznámka Anki 1672329229389

Karty Anki: 1672329229389
GUID: NxR^c>L%/.; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Theorem.

### Otázka (Front)

Věta 6.4: Konstrukce řešení homogenní LRR pomocí charakteristického čísla

### Odpověď (Back)

Jestliže \(\lambda\) je charakteristickým číslem homogenní LRR s konstantními koeficienty řádu \(k\in\mathbb{N}\)\[ x_{n+k} + c_{k-1} x_{n+k-1} + \cdots + c_1 x_{n+1} + c_0 x_{n} = 0, \quad n \geq n_0, \]pak posloupnost \((\lambda^n)_{n=n_0}^\infty\) je jejím řešením.

## Poznámka Anki 1672329229390

Karty Anki: 1672329229390
GUID: odOUupmbUu; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Theorem.

### Otázka (Front)

Věta 6.5: Řešení homogenní LRR s konstantními koeficienty, jednoduchá charakteristická čísla

### Odpověď (Back)

Uvažujme homogenní LRR s konstantními koeficienty řádu \(k \in \mathbb{N}\)\[ x_{n+k} + c_{k-1} x_{n+k-1} + \cdots + c_1 x_{n+1} + c_0 x_{n} = 0, \quad n \geq n_0. \]Jestliže má \(k\) vzájemně různých charakteristických čísel  \(\lambda_i\), \(i\in\hat{k}\), pak soubor posloupností \((\lambda_i^n)_{n=n_0}^\infty\), \(i\in\hat{k}\), tvoří bázi \(S_0\), tedy libovolné řešení \((x_n)_{n=n_0}^\infty \in S_0\) je tvaru\[ x_n = \alpha_1 \lambda_1^n + \cdots + \alpha_k \lambda_k^n, \quad n \geq n_0, \]pro nějaké konstanty \(\alpha_1, \ldots, \alpha_k\).

## Poznámka Anki 1672329229391

Karty Anki: 1672329229391
GUID: IFN!vG0Vyi; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Lemma.

### Otázka (Front)

Lemma 6.1: Determinant Vandermondovy matice

### Odpověď (Back)

Mějme vzájemně různá čísla \(\lambda_1,\ldots,\lambda_k\) a označme (tzv. **Vandermondův determinant**)\[ V(\lambda_1,\ldots,\lambda_k) :=
    \det \begin{pmatrix}
    1 & 1 & 1 & \cdots & 1 & 1 \\
    \lambda_1 & \lambda_2 & \lambda_3 & \cdots & \lambda_{k-1} & \lambda_{k} \\
    \lambda_1^2 & \lambda_2^2 & \lambda_3^2 & \cdots & \lambda_{k-1}^2 & \lambda_{k}^2 \\
    \lambda_1^3 & \lambda_2^3 & \lambda_3^3 & \cdots & \lambda_{k-1}^3 & \lambda_{k}^3 \\
    \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
    \lambda_1^{k-2} & \lambda_2^{k-2} & \lambda_3^{k-2} & \cdots & \lambda_{k-1}^{k-2} & \lambda_{k}^{k-2} \\
    \lambda_1^{k-1} & \lambda_2^{k-1} & \lambda_3^{k-1} & \cdots & \lambda_{k-1}^{k-1} & \lambda_{k}^{k-1}
    \end{pmatrix}. \]Potom \(\displaystyle V(\lambda_1,\ldots,\lambda_k) = \prod_{1 \leq i < j \leq k} (\lambda_j - \lambda_i) \neq 0\).

## Poznámka Anki 1672329229392

Karty Anki: 1672329229392
GUID: fvkojmv?jd; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Theorem.

### Otázka (Front)

Věta 6.6: Konstrukce řešení homogenní LRR pomocí charakteristického čísla vyšší násobnosti

### Odpověď (Back)

Jestliže \(\lambda\) je charakteristickým číslem  homogenní LRR řádu \(k\in\mathbb{N}\) s konstantními koeficienty\[ x_{n+k} + c_{k-1} x_{n+k-1} + \cdots + c_1 x_{n+1} + c_0 x_{n} = 0, \quad n \geq n_0, \]a jeho násobnost je \(m\), pak posloupnosti \((\lambda^n)_{n=n_0}^\infty\), \((n\lambda^n)_{n=n_0}^\infty\), …, \((n^{m-1}\lambda^n)_{n=n_0}^\infty\) jsou jejím řešením a tvoří LN soubor.

## Poznámka Anki 1672329229393

Karty Anki: 1672329229393
GUID: UR9,pLx)G; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Theorem.

### Otázka (Front)

Věta 6.7: Konstrukce prostoru všech řešení homogenní LRR

### Odpověď (Back)

Uvažujme homogenní LRR řádu \(k \in \mathbb{N}\) s konstantními koeficienty\[ x_{n+k} + c_{k-1} x_{n+k-1} + \cdots + c_1 x_{n+1} + c_0 x_{n} = 0, \quad n \geq n_0. \]Jestliže má \(K\) vzájemně různých charakteristických čísel  \(\lambda_i\), \(i\in\hat{K}\), každé s násobností \(m_i \in \hat{K}\), pak soubor posloupností\[ \begin{gathered} \Big( (\lambda_1^n)_{n=n_0}^\infty, \ (n\lambda_1^n)_{n=n_0}^\infty, \ \ldots, (n^{m_1-1} \lambda_1^n)_{n=n_0}^\infty, \ \ldots, \\  (\lambda_K^n)_{n=n_0}^\infty, \ (n\lambda_K^n)_{n=n_0}^\infty, \ \ldots, (n^{m_K-1} \lambda_K^n)_{n=n_0}^\infty \Big) \end{gathered} \]tvoří bázi \(S_0\)

## Poznámka Anki 1672329229394

Karty Anki: 1672329229394
GUID: gP8OfE/K(.; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Definition.

### Otázka (Front)

Definice 6.6: Kvazipolynom

### Odpověď (Back)

Řekneme, že posloupnost \((b_n)_{n=n_0}^\infty\) je **kvazipolynom**, jestliže existuje \(\lambda\in\mathbb{R}\) a polynom \(P(x)\) takový, že \(b_n = P(n) \lambda^n\) pro všechna přirozená \(n \geq n_0\).

## Poznámka Anki 1672329229395

Karty Anki: 1672329229395
GUID: m7p6Nli(O=; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Theorem.

### Otázka (Front)

Věta 6.8: Partikulární řešení LRR s kvazipolynomiální pravou stranou

### Odpověď (Back)

Uvažujme nehomogenní LRR řádu \(k \in \mathbb{N}\) s konstantními koeficienty\[ x_{n+k} + c_{k-1} x_{n+k-1} + \cdots + c_1 x_{n+1} + c_0 x_{n} = b_n, \quad n \geq n_0, \]a nechť \((b_n)_{n=n_0}^\infty\) je kvazipolynom, tj. \(b_n = P(n) \lambda^n\), \(n \geq n_0\), pro nějaký polynom \(P(x)\) a číslo \(\lambda\in\mathbb{R}\).
  Definujme \(m \in \N_0\) následujícím způsobem:

- 

pokud je \(\lambda\) charakteristické číslo uvažované LRR, pak nechť \(m\) je jeho násobnost,

- 

jinak nechť \(m\) je nula.

Potom existuje polynom \(Q(x)\) stupně stejného jako \(P(x)\) takový, že posloupnost\[ \Big( n^m Q(n) \lambda^n \Big)_{n = n_0}^\infty \]je řešením uvažované LRR.

## Poznámka Anki 1672329229396

Karty Anki: 1672329229396
GUID: zAl<KMG`J|; štítky: BI-MA2::chap_linearni_rekurentni_rovnice Theorem.

### Otázka (Front)

Věta 6.9: Mistrovská metoda

### Odpověď (Back)

Nechť \(a \geq 1\) a \(b > 1\) jsou reálné konstanty, \(f\) kladná funkce jedné proměnné.
  Uvažujme rekurentní rovnici\[ T(n) = a \cdot T\left( \frac{n}{b} \right) + f(n), \]kde \(\frac{n}{b}\) v argumentu může znamenat i \(\lceil \frac{n}{b} \rceil\) nebo \(\lfloor \frac{n}{b} \rfloor\).

Potom (všechny vztahy myšleny pro \(n \to \infty\)):

1. 

Pokud \(f(n) = \mathcal{O}(n^{\log_b(a) - \varepsilon})\) pro nějaké \(\varepsilon > 0\), potom \(T(n) = \Theta(n^{\log_b(a)})\).

2. 

Pokud \(f(n) = \Theta(n^{\log_b(a)})\), pak \(T(n) = \Theta\big(n^{\log_b(a)} \cdot \ln(n)\big)\).

3. 

Pokud \(f(n) = \Omega(n^{\log_b(a) + \varepsilon})\) pro nějaké \(\varepsilon > 0\) a pokud existuje \(d \in (0, 1)\) a \(n_0 \in \mathbb{N}\) takové, že\[ a f\left( \frac{n}{b} \right) \leq d \cdot f(n), \quad \text{pro každé} \ n \geq n_0, \]pak \(T(n) = \Theta(f(n))\).

