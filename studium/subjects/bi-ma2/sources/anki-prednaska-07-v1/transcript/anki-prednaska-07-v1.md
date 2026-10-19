# BI-MA2 – Přednáška 07

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1664893914510

Karty Anki: 1664893914510
GUID: jiEY&BMX,@; štítky: bi-ma2::p07 bi-spol::15.

### Otázka (Front)

Definujte číselnou řadu.

### Odpověď (Back)

Uvažme číselnou posloupnost \((a_k)_{k=0}^\infty\). Formální výraz tvaru
\[\sum \limits_{k=0}^\infty a_k = a_0 + a_1 + a_2 + \cdots\]nazýváme číselnou řadou. Pokud je posloupnost částečných součtů \((s_n)_{n=0}^\infty\),
\[s_n := \sum \limits_{k=0}^n a_k, \quad n \in \mathbb{N}_0\]konvergentní, nazýváme příslušnou řadu také konvergentní. V opačném případě mluvíme o divergentní číselné řadě. Součtem konvergetní řady \(\sum \limits_{k=0}^\infty a_k\) nazýváme hodontu limity \(\lim \limits_{n \to \infty} s_n\).

## Poznámka Anki 1664895145565

Karty Anki: 1664895145565
GUID: H&1?O/lMb;; štítky: bi-ma2::p07 bi-spol::15.

### Otázka (Front)

Vyslovte a dokažte větu o nutné podmínce konvergence řady.

### Odpověď (Back)

Pokud řada \(\sum \limits_{k=0}^\infty a_k\) konverguje, potom pro limitu sčítanců platí \(\lim \limits_{k \to \infty} a_k = 0\).

**Důkaz
**Označme \(S \in \mathbb{R}\) součet naší konvergentní řady. Pro libovolné kladné celé \(n\) platí
\[0 \leq |a_n| = |s_n - s_{n-1}| = |s_n - S + S - s_{n-1}| \leq |s_n - S| + |S - s_{n-1}|\]Protože \(S = \lim \limits_{n \to \infty} s_n\) dostáváme z věty o limitě sevřené posloupnosti, že \(\lim \limits_{n \to \infty} |a_n| = 0\), což implikuje \(\lim \limits_{n \to \infty} a_n = 0\).

## Poznámka Anki 1664895561228

Karty Anki: 1664895561228
GUID: t6Qrr^Q[D2; štítky: bi-ma2::p07 bi-spol::15.

### Otázka (Front)

Vyslovte větu o Bolzano-Cauchyovu kritériu pro řady.

### Odpověď (Back)

Řada \(\sum \limits_{k=0}^\infty a_k\) konverguje právě tehdy, když pro každé \(\varepsilon > 0\) existuje \(n_0 \in \mathbb{R}\) tak, že pro každé \(n \geq n_0\) a \(p \in \mathbb{N}\) platí
\[|a_n + a_{n+1} + \cdots + a_{n+p}| < \varepsilon.\]

## Poznámka Anki 1664895710832

Karty Anki: 1664895710832
GUID: GI)XSUZSLp; štítky: bi-ma2::p07.

### Otázka (Front)

Definujte absolutně konvergetní řadu.

### Odpověď (Back)

Řadu \(\sum \limits_{k=0}^\infty a_k\) nazýváme absolutně konvergentní, pokud řada \(\sum \limits_{k=0}^\infty |a_k|\) konverguje.

## Poznámka Anki 1664895899319

Karty Anki: 1664895899319
GUID: n1BG`G@ixT; štítky: bi-ma2::p07.

### Otázka (Front)

Vyslovte a dokažte větu o vztahu absolutní konvergence a konvergence řady.

### Odpověď (Back)

Pokud řada absolutně konverguje, pak konverguje.

**Důkaz**
Použijeme Bolzanova-Cauchyova kritéria pro konvergenci řady. Buď \(\sum \limits_{k=0}^\infty a_k\) absolutně konvergentní řada. Potom pro \(\varepsilon > 0\) existuje \(n_0 \in \mathbb{N}\) tak, že pro každé \(n \geq n_0\) a \(p \in \mathbb{N}\) je podle trojúhelníkové nerovnosti
\[|a_n + a_{n+1} + \cdots+ a_{n+p}| \leq | a_n| + |a_{n+1}| + \cdots + |a_{n+p}| < \varepsilon.\]Řada \(\sum \limits_{k=0}^\infty a_k\) tedy konverguje.

## Poznámka Anki 1664896396372

Karty Anki: 1664896396373
GUID: uKO}`4>DYx; štítky: bi-ma2::p07 bi-spol::15.

### Otázka (Front)

Vyslovte větu o Leibnizově kritériu.

### Odpověď (Back)

Buď \((a_k)_{k=1}^\infty\) monotónní posloupnost konvergující k nule. Potom řada
\[\sum \limits_{k=1}^\infty (-1)^k a_k\]konverguje.

## Poznámka Anki 1664896917278

Karty Anki: 1664896917278
GUID: fw{y;~G|;H; štítky: bi-ma2::p07 bi-spol::15.

### Otázka (Front)

Vyslovte větu o srovnávacím kritériu.

### Odpověď (Back)

Buďte \(\sum \limits_{k=1}^\infty a_k\) a \(\sum \limits_{k=1}^\infty b_k\) číselné řady. Potom platí následující tvrzení.

- Nechť existuje \(k_0 \in \mathbb{N}\) takové, že pro každé \(k \in \mathbb{N}\) větší než \(k_0\) platí \(0 \leq | a_k| \leq b_k\) a nechť řada \(\sum \limits_{k=1}^\infty b_k\) konverguje. Potom řada \(\sum \limits_{k=1}^\infty a_k\) absolutně konverguje.
- Nechť existuje \(k_0 \in \mathbb{N}\) takové, že pro každé \(k \in \mathbb{N}\) větší než \(k_0\) platí \(0 \leq a_k \leq b_k\) a \(\sum \limits_{k=1}^\infty a_k\) diverguje. Potom i řada \(\sum \limits_{k=1}^\infty b_k\) diverguje.

## Poznámka Anki 1664897324252

Karty Anki: 1664897324253
GUID: Pl+>q)0C*D; štítky: bi-ma2::p07 bi-spol::15.

### Otázka (Front)

Dokažte větu o srovnávacím kritériu.

### Odpověď (Back)

**První bod**
Použijeme Bolzanova–Cauchyova kritéria. Tvrzení plyne z následujícího odhadu,
\[\big| |a_n| + | a_{n+1}| + \cdots + |a_{n+p}| \big| = |a_n| + |a_{n+1}| + \cdots + |a_{n+p}| \leq b_n + b_{n+1} + \cdots + b_{n+p}.\]
**Druhý bod** 
Dle předpokladů víme, že platí
\[0 \leq \sum \limits_{k=k_0}^n a_k \leq \sum \limits_{k=k_0}^n b_k,\]kde limita levé stany je \(+ \infty\). Odtud plyne, že i posloupnost částečných součtů řady \(\sum \limits_{k=0}^\infty b_k\) diverguje.

## Poznámka Anki 1664897835502

Karty Anki: 1664897835502
GUID: fV@e~0L-Jd; štítky: bi-ma2::p07 bi-spol::15.

### Otázka (Front)

Vyslovte větu o d'Alembertovu kritériu.

### Odpověď (Back)

Nechť \(a_k > 0\) pro každé \(k \in \mathbb{N}\). Potom platí dvě následující tvrzení:

- Pokud \(\lim \limits_{k \to \infty} \frac{a_{k+1}}{a_k} >1\), pak řada \(\sum \limits_{k=0}^\infty a_k\) diverguje.
- Pokud \(\lim \limits_{k \to \infty} \frac{a_{k+1}}{a_k} < 1\), pak řada \(\sum \limits_{k=0}^\infty a_k\) (absolutně) konverguje.

## Poznámka Anki 1664898609044

Karty Anki: 1664898609044
GUID: n4SlzVOiIJ; štítky: bi-ma2::p07 bi-spol::15.

### Otázka (Front)

Dokažte větu o d'Alembertově kritériu.

### Odpověď (Back)

**První bod**: Z podílového kritéria aplikovaného na posloupnost \((a_k)_{k=1}^\infty\) plyne\[\lim \limits_{k \to \infty} a_k = +\infty.\]Není proto splněna nutná podmínka konvergence a řada \(\sum \limits_{k=1}^\infty a_k\) proto diverguje.
**Druhý bod**: Dle předpokladu existuje \(r < 1\) a \(k_0 \in \mathbb{N}\) pro něž platí
\[\frac{a_{k+1}}{a_k} \leq r < 1, k \geq k_0.\]Odtud nahlédneme, že pro každé \(k \geq k_0\) platí
\[a_k \leq r^{k-k_0} a_{k_0}.\]Už ale víme, že řada \(\sum \limits_{k=0}^\infty r^k\) konverguje pro \(|r| < 1\). Podle srovnávacího kritéria tedy konverguje i řada \(\sum \limits_{k=0}^\infty a_k\).

## Poznámka Anki 1665424627479

Karty Anki: 1665424627479
GUID: d]|~V}j*EP; štítky: bi-ma2::p07.

### Otázka (Front)

Uveďte vzorce pro známé součty.

### Odpověď (Back)

- **aritmetická posloupnost** \((a_n)_{n=1}^\infty\) tj \(a_n = a_1 + (n-1)d\)

\[\sum \limits_{k=1}^n a_k = \frac{n}{2}(a_1+a_n)\]

- **geometrická posloupnost** \((a_n)_{n=1}^\infty\) tj. \(a_n = a_1q^{n-1}\)

\[\sum \limits_{k=1}^n a_k = a_1 \frac{q^n-1}{q-1}, \quad q \neq 1\]

- **geometrická řada**

\[\sum \limits_{k=0}^\infty q^k = \frac{1}{1-q}, \quad |q| < 1\]

- **exponenciála**

\[\sum \limits_{k=0}^\infty \frac{x^k}{k!} = e^x, \quad x \in \mathbb{R}\]**
**

## Poznámka Anki 1665424825155

Karty Anki: 1665424825155
GUID: Pa}+@Z,J45; štítky: bi-ma2::p07 bi-spol::15.

### Otázka (Front)

Vyslovte větu o odhadu růstu součtů.

### Odpověď (Back)

Nechť \(f\) je spojitá funkce na \(\langle1, + \infty )\) a \(n \in \mathbb{N}\).

- Je-li \(f\) klesající, pak

\[f(n) + \int_1^n f(x) \, \text dx \leq \displaystyle \sum_{k = 1}^n f(k) \leq f(1) + \int_1^n f(x) \, \text dx.\]

- Je-li \(f\) rostoucí, pak

\[f(1) + \int_1^n f(x) \, \text dx \leq \displaystyle \sum_{k = 1}^n f(k) \leq f(n) + \int_1^n f(x) \, \text dx.\]

## Poznámka Anki 1665425031761

Karty Anki: 1665425031761
GUID: M&=y/:!HGv; štítky: bi-ma2::p07 bi-spol::15.

### Otázka (Front)

Vyslovte větu o integrálním kritériu.

### Odpověď (Back)

Buď \(\sum \limits_{n=1}^\infty a_n\) číselná řada s kladnými členy. Nechť existuje spojitá monotónní funkce definovaná na \(\langle 1, + \infty)\) taková, že \(f(n) = a_n\) pro každé \(n\). Potom:

- Pokud integrál \(\int_1^\infty f(x) \, \text dx\) konverguje, pak číselná řada \(\sum \limits_{n=1}^\infty a_n\) konverguje.
- Pokud integrál \(\int_1^\infty f(x) \, \text dx\) diverguje, pak číselná řada \(\sum \limits_{n=1}^\infty a_n\) diverguje.

