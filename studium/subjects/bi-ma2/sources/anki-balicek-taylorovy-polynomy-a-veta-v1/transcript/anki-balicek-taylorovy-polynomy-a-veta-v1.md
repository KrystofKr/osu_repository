# BI-MA2 – Taylorovy polynomy a věta

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2::Taylorovy polynomy a věta
Rozsah: 11 poznámek, 11 karet.
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

## Poznámka Anki 1672329315945

Karty Anki: 1672329315945
GUID: d~7DtX~Tf9; štítky: BI-MA2::chap_taylor Definition.

### Otázka (Front)

Definice 5.1: Polynom

### Odpověď (Back)

Reálnou funkci reálné proměnné \(p: \mathbb{R} \to \mathbb{R}\) nazveme **polynomem**, právě když existuje nezáporné celé číslo \(n\in\mathbb{N}_0\) a reálná čísla \(a_0, \ldots, a_n \in \mathbb{R}\) taková,
  že rovnost\[ p(x) = \sum_{k=0}^n a_k x^k \]platí pro všechna reálná \(x\in\mathbb{R}\).

## Poznámka Anki 1672329315946

Karty Anki: 1672329315946
GUID: nds/ZBuV&Q; štítky: BI-MA2::chap_taylor Definition.

### Otázka (Front)

Definice 5.2: Taylorův polynom

### Odpověď (Back)

Nechť reálná funkce reálné proměnné \(f\) má v bodě \(a\in\mathbb{R}\) konečnou \(n\)-tou derivaci.
  Polynom\[ T_{n,a}(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x-a)^k \]nazýváme **\(n\)-tým Taylorovým polynomem funkce \(f\) v bodě \(a\)**

## Poznámka Anki 1672329315947

Karty Anki: 1672329315947
GUID: w#{wLb1gN+; štítky: BI-MA2::chap_taylor Theorem.

### Otázka (Front)

Věta 5.1: O vlastnostech Taylorova polynomu

### Odpověď (Back)

Nechť reálná funkce reálné proměnné \(f\) má v bodě \(a\in\mathbb{R}\) konečnou \(n\)-tou derivaci.
  Potom Taylorův polynom \(T_{n,a}\) existuje a je to jediný polynom stupně nejvýše \(n\) takový, že\[ T_{n,a}^{(k)}(a) = f^{(k)}(a) \ \text{pro každé} \ k=0,1,\ldots,n. \]

## Poznámka Anki 1672329315948

Karty Anki: 1672329315948
GUID: Pv!.q{WC-Z; štítky: BI-MA2::chap_taylor Definition.

### Otázka (Front)

Definice 5.3: Taylorův vzorec a Taylorův zbytek

### Odpověď (Back)

Nechť funkce \(f\) má v bodě \(a\) konečnou \(n\)-tou derivaci.
  Pro všechna přípustná \(x\) položme \(R_{n,a}(x) := f(x) - T_{n,a}(x)\).
  Potom vztah\[ f(x) = T_{n,a}(x) + R_{n,a}(x) \]nazýváme **Taylorovým vzorcem** a \(R_{n,a}\) nazýváme **\(n\)-tým zbytkem** v Taylorově vzorci.

## Poznámka Anki 1672329315949

Karty Anki: 1672329315949
GUID: mXoa&xy_!2; štítky: BI-MA2::chap_taylor Theorem.

### Otázka (Front)

Věta 5.2: O zbytku v Taylorově vzorci

### Odpověď (Back)

Nechť funkce \(f\) má v jistém okolí \(H_a\) bodu \(a\) spojitou \(n\)-tou derivaci.
  Pak pro zbytek v Taylorově vzorci platí\[ \lim_{x\to a} \frac{R_{n,a}(x)}{(x-a)^n} = 0. \]

## Poznámka Anki 1672329315950

Karty Anki: 1672329315950
GUID: vkTCo<ni3D; štítky: BI-MA2::chap_taylor Theorem.

### Otázka (Front)

Věta 5.3: O nejlepší aproximaci

### Odpověď (Back)

Nechť funkce \(f\) má v jistém okolí bodu \(0\) konečnou \(n\)-tou derivaci a nechť \(Q\) je polynom stupně nejvýše \(n\), různý od Taylorova polynomu \(T_n\) funkce \(f\) v bodě \(0\).
  Potom existuje okolí \(H_0\) bodu \(0\) takové, že\[ |f(x) - T_n(x)| < |f(x) - Q(x)| \quad \textrm{pro každé} \ x\in H_0 \smallsetminus \{0\}. \]

## Poznámka Anki 1672329315951

Karty Anki: 1672329315951
GUID: pw_y`{+u^L; štítky: BI-MA2::chap_taylor Theorem.

### Otázka (Front)

Věta 5.4: Taylorova

### Odpověď (Back)

Nechť existuje okolí \(H_a\) bodu \(a\) takové, že funkce \(f\) v něm má konečnou \((n+1)\)-ní derivaci.
  Pak zbytek v Taylorově vzorci \(f(x) = T_{n,a}(x) + R_{n,a}(x)\) lze pro každé \(x\in H_{a}\) zapsat ve tvaru\[ R_{n,a}(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} (x-a)^{n+1}, \]kde číslo \(\xi\) závisí na \(x\) a \(n\) a leží uvnitř intervalu s krajními body \(x\) a \(a\).
  Tento tvar zbytku nazýváme **Lagrangeův**.

## Poznámka Anki 1672329315952

Karty Anki: 1672329315952
GUID: v7~Ujnfii:; štítky: BI-MA2::chap_taylor Definition.

### Otázka (Front)

Definice 5.4: Mocninná řada

### Odpověď (Back)

Nechť je dána posloupnost \((a_k)_{k=0}^\infty\) a číslo \(c\in\mathbb{R}\).
  Číselnou řadu\[ \sum_{k=0}^\infty a_k (x-c)^k, \]závisející na reálném parametru \(x\), nazýváme **mocninnou řadou se středem v bodě \(c\)**.

## Poznámka Anki 1672329315953

Karty Anki: 1672329315953
GUID: E:1kqN>oLA; štítky: BI-MA2::chap_taylor Definition.

### Otázka (Front)

Definice 5.5: Taylorova řada

### Odpověď (Back)

Nechť reálná funkce reálné proměnné \(f\) má v bodě \(c \in \mathbb{R}\) konečné derivace všech řádů.
  Mocninnou řadu\[ \sum_{k=0}^\infty \frac{f^{(k)}(c)}{k!} (x-c)^k \]potom nazýváme **Taylorovou řadou funkce \(f\) v bodě \(c\)**.

## Poznámka Anki 1672329315954

Karty Anki: 1672329315954
GUID: jVU5WXhyn9; štítky: BI-MA2::chap_taylor Theorem.

### Otázka (Front)

Věta 5.5: O poloměru konvergence

### Odpověď (Back)

Pokud existuje limita\[ L := \lim_{k\to\infty} \bigg|\frac{a_{k+1}}{a_k}\bigg|, \]potom klademe\[ R := \begin{cases} \frac{1}{L}, & L > 0, \\ +\infty, & L = 0, \\ 0, & L = +\infty \end{cases} \]a tvrdíme, že mocninná řada\[ \sum_{k = 0}^\infty a_k (x-c)^k \] konverguje absolutně pro \(x\in(c-R,c+R)\) a diverguje pro \(|c-x| > R\).

## Poznámka Anki 1672329315955

Karty Anki: 1672329315955
GUID: j18`jLbB&H; štítky: BI-MA2::chap_taylor Theorem.

### Otázka (Front)

Věta 5.6: Cauchy–Hadamard

### Odpověď (Back)

Ke každé mocninné řadě tvaru\[ \sum_{k=0}^\infty a_k x^k. \]existuje \(R\in\langle 0,+\infty\rangle\) takové, že řada absolutně konverguje pro \(|x| < R\) a diverguje pro \(|x| > R\).

