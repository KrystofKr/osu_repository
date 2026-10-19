# BI-MA1 – Přednáška 13

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA1
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1652130655183

Karty Anki: 1652130655184
GUID: K~wx>NbkgE; štítky: bi-ma1::p13 bi-spol::13 bi-spol::20.

### Otázka (Front)

Definujte asymptotickou dolní mez \(\Omega\) pro posloupnosti.

### Odpověď (Back)

Mějme dvě posloupnosti \((a_n)_{n=1}^{\infty}\) a \((b_n)_{n=1}^{\infty}\). Řekneme, že posloupnost \((a_n)_{n=1}^{\infty}\) je asymptoticky zdola omezená posloupností \((b_n)_{n=1}^{\infty}\), symbolicky \(a_n = \Omega (b_n)\) pro \(n \to \infty\), právě když **existuje **kladná konstanta \(c \in \mathbb{R}\) a přirozené \(N \in \mathbb{N}\) tak, že pro všechna \(n \geq N\) platí 
\[| a_n | \geq c \cdot | b_n |.\]

## Poznámka Anki 1652130738519

Karty Anki: 1652130738519
GUID: P-z_^4IM7S; štítky: bi-ma1::p13 bi-spol::13.

### Otázka (Front)

Definujte striktně menší dolní mez \(\omega\) pro posloupnosti.

### Odpověď (Back)

Mějme dvě posloupnosti \((a_n)_{n=1}^{\infty}\) a \((b_n)_{n=1}^{\infty}\). Řekneme, že posloupnost \((a_n)_{n=1}^{\infty}\) je asymptoticky zdola striktně omezená posloupností \((b_n)_{n=1}^{\infty}\), symbolicky \(a_n = \omega (b_n)\) pro \(n \to \infty\), právě když pro **každé **kladné \(c \in \mathbb{R}\) existuje \(N \in \mathbb{N}\) tak, že pro všechna \(n \geq N\) platí 
\[| a_n | > c \cdot | b_n |.\]

## Poznámka Anki 1652130780404

Karty Anki: 1652130780404
GUID: Gs$Q4RvFs#; štítky: bi-ma1::p13 bi-spol::13 bi-spol::20.

### Otázka (Front)

Definujte těsnou asymptotickou mez \(\Theta\) pro posloupnosti

### Odpověď (Back)

Mějme dvě posloupnosti \((a_n)_{n=1}^{\infty}\) a \((b_n)_{n=1}^{\infty}\). Řekneme, že posloupnost \((a_n)_{n=1}^{\infty}\) je téhož řádu jako posloupnost \((b_n)_{n=1}^{\infty}\), symbolicky \(a_n = \Theta(b_n)\) pro \(n \to \infty\), právě když **existují **kladné konstanty \(c_1, c_2 \in \mathbb{R}\) a přirozené \(N \in \mathbb{N}\) tak, že pro všechna \(n \geq N\) platí 
\[c_1 \cdot | b_n | \leq | a_n |\leq c_2 \cdot | b_n |.\]

## Poznámka Anki 1652131157751

Karty Anki: 1652131157751
GUID: z;vOnY|0;(; štítky: bi-ma1::p13 bi-spol::13.

### Otázka (Front)

Definujte asymptotickou ekvivalenci \(\sim\) pro funkce.

### Odpověď (Back)

Mějme dvě funkce \(f\), \(g\) a bod \(a \in \overline{\mathbb{R}}\) takový, že \(a\) je hromadým bodem množiny \(D_f \cap D_g\) a existuje okolí \(V_a\) splňující \(V_a \cap D_f = V_a \cap D_g\).
Řekneme, že funkce \(f\) je asymptoticky ekvivalentní funkci \(g\) pro \(x\) jdoucí k \(a\), symbolicky \(f(x) \sim g(x)\) pro \(x \to a\), právě když existuje okolí \(U_a\) bodu \(a\) a funkce \(u\) definovaná na \(U_a\) splňující \(\lim \limits_{x \to a} u(x) = 1\) tak, že pro všechna \(x \in U_a \cap D_f \cap D_g\) platí
\[f(x) = u(x) g(x).\]

## Poznámka Anki 1652131614031

Karty Anki: 1652131614031
GUID: m2ef0<=2#v; štítky: bi-ma1::p13.

### Otázka (Front)

Popište algoritmus square and multiply (binární umocňování).

### Odpověď (Back)

- převedeme exponent do binární soustavy
- při každém kroku algoritmu umocníme číslo na druhou
- začínáme s číslem x, které je rovno mocněnému číslu
- pokud je v exponentu 1, pak číslo nejen mocníme na druhou, ale i násobíme původním mocněným číslem

