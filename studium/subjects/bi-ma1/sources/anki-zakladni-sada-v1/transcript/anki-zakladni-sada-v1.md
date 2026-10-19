# BI-MA1 – Základní sada otázek

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA1
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1654290153916

Karty Anki: 1654290153916
GUID: r:C]:~W#cl; štítky: bi-ma1::ustni bi-spol::13.

### Otázka (Front)

Uveďte příklad nekonstantní posloupnosti, jejíž limita je rovna \(0\) a určí se pomocí věty o sevřené posloupnosti.

### Odpověď (Back)

\[\lim \limits_{ n \to \infty } \frac{ \sin n }{ n }\]
Platí totiž následující nerovnost.
\[-\frac{ 1 }{ n } \leq \frac{ \sin n }{ n } \leq \frac{ 1 }{ n }\]

## Poznámka Anki 1654292826661

Karty Anki: 1654292826661
GUID: AocVuyR1I%; štítky: bi-ma1::ustni.

### Otázka (Front)

Uveďte rovnici, na kterou lze s výhodou uplatnit metodu půlení intervalu nebo Newtonovou metodou.

### Odpověď (Back)

\(0 = x^2 - 2\) nebo \(0 = x^3 - 11\)

## Poznámka Anki 1654346597602

Karty Anki: 1654346597603
GUID: iJv&UDOWG]; štítky: bi-ma1::ustni bi-spol::13.

### Otázka (Front)

Jaká vlastnost zobrazení platí na všechny ryze monotónní funkce?

### Odpověď (Back)

Každá ryze monotónní funkce je injektivní (prostá).

## Poznámka Anki 1654348149555

Karty Anki: 1654348149556
GUID: A0(P0]Xzo2; štítky: bi-ma1::ustni.

### Otázka (Front)

Uveďte příklad dvou různých funkcí \(f\) a \(g\), pro které platí \(f(x) = \mathcal{O}(g(x))\), ale neplatí \(f(x) = \mathcal{o}(g(x))\) pro \(x \to a\).

### Odpověď (Back)

\(f(x) = \sqrt{ x }\)
\(g(x) = x\)
pro \(x \to +\infty\)

## Poznámka Anki 1654351948380

Karty Anki: 1654351948380
GUID: Ft:Wy.&;2L; štítky: bi-ma1::ustni bi-spol::13.

### Otázka (Front)

Jaká je souvislost vztahů \(\Omega\) a \(\mathcal{O}\)?

### Odpověď (Back)

Mějme posloupnost \((a_n)_{n=1}^{\infty}\) a \((b_n)_{n=1}^{\infty}\). Pak \(a_n = \Omega (b_n)\), právě když \(b_n = \mathcal{O}(a_n)\).

## Poznámka Anki 1654352040622

Karty Anki: 1654352040622
GUID: N{n}*7^rj/; štítky: bi-ma1::ustni bi-spol::13.

### Otázka (Front)

Jaká je souvislost vztahů \(\omega\) a \(\mathcal{o}\)?

### Odpověď (Back)

Mějme posloupnost \((a_n)_{n=1}^{\infty}\) a \((b_n)_{n=1}^{\infty}\). Pak \(a_n = \omega (b_n)\), právě když \(b_n = \mathcal{o}(b_n)\).

## Poznámka Anki 1654357267863

Karty Anki: 1654357267863
GUID: hNeot?=h>G; štítky: bi-ma1::ustni bi-spol::13.

### Otázka (Front)

Jaká je souvislost vztahů \(\Theta\), \(\mathcal{O}\) a \(\Omega\)?

### Odpověď (Back)

Mějme posloupnost \((a_n)_{n=1}^{\infty}\) a \((b_n)_{n=1}^{\infty}\). Pak \(a_n = \Theta (b_n)\), právě když \(a_n = \mathcal{O}(b_n)\) a zároveň \(a_n = \Omega (b_n)\).

## Poznámka Anki 1654377834212

Karty Anki: 1654377834212
GUID: KDKlts%P8V; štítky: bi-ma1::ustni.

### Otázka (Front)

Dokažte, že platí \((e^x)' = e^x\).

### Odpověď (Back)

Z definice derivace víme:\[f'(e^x) = \lim \limits_{x \to a} \frac{e^x - e^a}{x - a}.\]Máme také zavedenou známou limitu:\[\lim \limits_{x \to a} \frac{e^x - 1}{x} = 1.\]Potom podle věty o limitě složené funkce a limitě součinu platí:\[\lim \limits_{x \to a} \frac{e^x - e^a}{x - a} = \lim \limits_{x \to a} e^a \cdot \frac{e^{x - a} - 1}{x - a} = e^a \cdot 1 = e^a.\]

## Poznámka Anki 1654378801332

Karty Anki: 1654378801332
GUID: 7{r#o+om-; štítky: bi-ma1::ustni.

### Otázka (Front)

Dokažte, že platí \((\ln(x))' = \frac{1}{x}\).

### Odpověď (Back)

Z definice derivace víme:
\[\lim \limits_{x \to a} \frac{\ln (x) - \ln (a)}{x - a}\]
Máme také zavedenou známou limitu:
\[\lim \limits_{x \to 0} \frac{ \ln (1 + x)}{x} = 1\]
Podle známých vztahů limit:
\[\lim \limits_{x \to a} \frac{ \ln (x) - \ln (a)}{x - a} = \lim \limits_{x \to a} \frac{\ln (\frac{x}{a})}{x - a} = \lim \limits_{x \to a} \frac{ \ln (1 + \frac{x}{a} - 1)}{a ( \frac{x}{a} - 1)} = \frac{1}{a} \cdot 1 = \frac{1}{a}\]

## Poznámka Anki 1654422516396

Karty Anki: 1654422516396
GUID: i$`j|_~O4=; štítky: bi-ma1::ustni.

### Otázka (Front)

Najdtěte funkci, která je spojitá v bodě \(1\), ale nemá v něm tečnu.

### Odpověď (Back)

\[f(x) = | x - 1 |\]

## Poznámka Anki 1654433696556

Karty Anki: 1654433696556
GUID: tvtuL%Rlo$; štítky: bi-ma1::ustni bi-spol::14.

### Otázka (Front)

Dokažte větu o derivaci součtu a součinu.

### Odpověď (Back)

\[( f + g )' (a) = \lim \limits_{ x \to a } \frac{ f(x) - f(a) + g(x) - g(a) }{ x - a } = \lim \limits_{ x \to a } \frac{ f(x) - f(a) }{ x - a } + \frac{ g(x) - g(a) }{ x - a} = f'(a) + g'(a)\]
\[( f \cdot g )' (a) = \lim \limits_{ x \to a } \frac{ f(x)g(x) - f(a)g(a) }{ x - a } = \lim \limits_{ x \to a } \frac{ f(x) \cdot ( g(x) - g(a) ) + g(a) \cdot ( f(x) - f(a) ) }{ x - a } = f(a)g'(a) + f'(a)g(a)\]

## Poznámka Anki 1654434042761

Karty Anki: 1654434042761
GUID: F3Q@u@8jI.; štítky: bi-ma1::ustni bi-spol::13.

### Otázka (Front)

Uveďte příklad posloupnosti, jejíž limita se dá spočítat pomocí podílového kritéria, a posloupnosti, jejíž limita se pomocí podílového kritéria spočítat nedá.

### Odpověď (Back)

Lze:
\[a_n = \frac{ n }{ 2^n }\]
Nelze:
\[a_n = \frac { n + 1 }{ n }\]

## Poznámka Anki 1654435154369

Karty Anki: 1654435154369
GUID: qnwq[_@ib&; štítky: bi-ma1::ustni bi-spol::13.

### Otázka (Front)

Najděte posloupnosti \((a_n)_{ n = 1 }^{ \infty }\) a \((b_n)_{ n = 1 }^{ \infty }\) takové, že platí \(a_n = \Theta (b_n)\).

### Odpověď (Back)

\(a_n = n + \sin n\)
\(b_n = n\)

## Poznámka Anki 1654459713549

Karty Anki: 1654459713549
GUID: p~TiTPAp+v; štítky: bi-ma1::ustni.

### Otázka (Front)

Najděte funkci, která je spojitá na \(\langle 0, 1 \rangle\), ale ne v \(0\).

### Odpověď (Back)

\(f(x) = \operatorname{ sgn } (x)\)
\(f(x) = \lfloor x \rfloor\)
\(f(x) = \lceil x \rceil\)

