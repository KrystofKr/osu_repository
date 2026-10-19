# BI-MA2 – Přednáška 02

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1663656661691

Karty Anki: 1663656661691
GUID: yGF6ukjM8p; štítky: bi-ma2::p02 bi-spol::15 duplicate ni-spol::04.

### Otázka (Front)

Definujte primitivní funkci.

### Odpověď (Back)

Mějme funkci \(f\) definovanou na intervalu \((a, b)\), kde\[−\infty \leq a < b \leq +\infty.\]Funkci \(F\) splňující podmínku\[F'(x) = f(x), \quad \forall x \in (a, b)\]nazýváme primitivní funkcí k funkci \(f\) na intervalu \((a, b)\).

### Doplňující pole (Extra)

Z definice plyne, že \(F\) je diferencovatelná a tedy i spojitá v každém bodě intervalu \((a, b)\).

## Poznámka Anki 1663656817376

Karty Anki: 1663656817376
GUID: g<WmNF3joH; štítky: bi-ma2::p02 bi-spol::15.

### Otázka (Front)

Vyslovte a dokažte větu o jednoznačnosti primitivní funkce.

### Odpověď (Back)

Nechť \(F\) je primitivní funkcí k funkci \(f\) na intervalu \((a, b)\). Pak \(G\) je primitivní
funkcí k funkci \(f\) na intervalu \((a, b)\) právě tehdy, když existuje konstanta \(C \in \mathbb R\) taková, že
\[G(x) = F(x) + C\]pro každé \(x \in (a, b)\).

**Důkaz
**Pokud jsou funkce \(F\) a \(G\) primitivní k \(f\) na \((a, b)\), potom
\[(F - G)'(x) = F'(x) - G'(x) = f(x) - f(x) = 0,\]pro všechna \(x \in (a, b)\). Funkce \(F - G\) je tedy konstantní na intervalu \((a, b)\). Naopak je-li \(G(x) = F(x) + C\) pro libovolné \(x \in (a, b)\), pak \(G'(x) = F'(x)\).

## Poznámka Anki 1663657309820

Karty Anki: 1663657309820
GUID: KkD=EP+WDJ; štítky: bi-ma2::p02 bi-spol::15.

### Otázka (Front)

Definujte neurčitý integrál.

### Odpověď (Back)

Nechť k funkci \(f\) existuje primitivní funkce na intervalu \((a, b)\). Množinu všech
primitivních funkcí k funkci \(f\) na \((a, b)\) nazýváme neurčitým integrálem funkce \(f\) na intervalu \((a, b)\). Značíme jej \(\int f\) nebo \(\int f(x) \, \text dx.\)

## Poznámka Anki 1663657573836

Karty Anki: 1663657573836
GUID: F3VJAM.IGG; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int x^n \, \mathrm dx\), když \(x \in \mathbb{R}, n\in N_0\).

### Odpověď (Back)

\[\int x^n \, \mathrm dx = \frac{x^{n+1}}{n+1} + C\]

## Poznámka Anki 1663657649296

Karty Anki: 1663657649296
GUID: nVllKRzjV^; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int x^n \, \mathrm dx\), když \(x \in \mathbb{R} \smallsetminus \{0\}, n \in \mathbb{Z}, n \leq -2\).

### Odpověď (Back)

\[\int x^n \, \mathrm dx = \frac{x^{n+1}}{n+1} + C\]

## Poznámka Anki 1663657718099

Karty Anki: 1663657718099
GUID: blL$YWb_tk; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int x^\alpha \, \mathrm dx\), když \(x \in (0, +\infty), a \notin \mathbb{Z}\).

### Odpověď (Back)

\[\int x^\alpha \, \mathrm dx = \frac{x^{\alpha+1}}{\alpha+1} + C\]

## Poznámka Anki 1663657786536

Karty Anki: 1663657786537
GUID: m@E^0>i5rC; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int \frac{1}{x} \, \mathrm dx\), když \(x \in \mathbb{R} \smallsetminus \{0\}\).

### Odpověď (Back)

\[\int \frac 1 x \, \text dx = \ln |x| + C\]

## Poznámka Anki 1663657858928

Karty Anki: 1663657858928
GUID: gF)h;HnKL>; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int a^x \, \mathrm dx\), když \(x \in \mathbb{R}, a > 0\) a \(a \neq 1\).

### Odpověď (Back)

\[\int a^x \, \mathrm dx = \frac{a^x}{\ln a} + C\]

## Poznámka Anki 1663657897427

Karty Anki: 1663657897428
GUID: Ps?/DKmo6P; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int \sin(x) \, \mathrm dx\), když \(x \in \mathbb{R}\).

### Odpověď (Back)

\[\int \sin(x) \, \mathrm dx = -\cos(x) + C\]

## Poznámka Anki 1663657935515

Karty Anki: 1663657935515
GUID: qbH+@JsA9c; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int \cos(x) \, \mathrm dx\), když \(x \in \mathbb{R}\).

### Odpověď (Back)

\[\int \cos(x) \, \mathrm dx = \sin(x) + C\]

## Poznámka Anki 1663658186389

Karty Anki: 1663658186390
GUID: k,jTR7^j~3; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int \frac{1}{\cos^2(x)} \, \text dx\), když \(x \in (-\frac{\pi}{2} + k\pi, \frac{\pi}{2} + k\pi), k \in \mathbb{Z}\).

### Odpověď (Back)

\[\int \frac{1}{\cos^2(x)} \, \text dx = \operatorname{tg}(x) + C\]

## Poznámka Anki 1663658275722

Karty Anki: 1663658275722
GUID: u?/RZ47^LX; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int \frac{1}{\sin^2(x)} \, \mathrm dx\), když \(x \in (k\pi, \pi + k\pi), k \in \mathbb{Z}\).

### Odpověď (Back)

\[\int \frac{1}{\sin^2(x)} \, \mathrm dx = -\operatorname{cotg}(x) + C\]

## Poznámka Anki 1663659099477

Karty Anki: 1663659099477
GUID: N2:q.g*>bT; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int \frac{1}{\sqrt{1-x^2}} \, \mathrm dx\), když \(x \in (-1, 1)\).

### Odpověď (Back)

\[\int \frac 1 {\sqrt{1 - x^2}} \, \mathrm dx = \arcsin(x) + C\]

## Poznámka Anki 1663659159258

Karty Anki: 1663659159258
GUID: I`53V3Lf;b; štítky: bi-ma2::p02 duplicate.

### Otázka (Front)

Vypočtěte \(\int \frac{1}{1+x^2} \, \mathrm dx\), když \(x \in \mathbb{R}\).

### Odpověď (Back)

\[\int \frac{1}{1+x^2} \, \mathrm dx= \operatorname{arctg}(x) + C\]

## Poznámka Anki 1663659316448

Karty Anki: 1663659316448
GUID: Gl{>(LSlze; štítky: bi-ma2::p02 bi-spol::15.

### Otázka (Front)

Vyslovte a dokažte větu o linearitě neurčitého integrálu.

### Odpověď (Back)

[Obrázek: paste-07c9f96f27c5e79cb1a451dd0134a77eb35fdd2a.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1663659439068

Karty Anki: 1663659439068
GUID: ho09;JE0kP; štítky: bi-ma2::p02 bi-spol::15.

### Otázka (Front)

Vyslovte větu o postačující podmínce pro existenci primitivní funkce.

### Odpověď (Back)

Nechť funkce \(f\) je spojitá na intervalu \((a, b)\). Pak funkce \(f\) má na tomto intervalu
primitivní funkci.

