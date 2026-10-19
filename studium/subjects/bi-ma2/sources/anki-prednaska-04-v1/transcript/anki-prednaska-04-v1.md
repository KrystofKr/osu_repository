# BI-MA2 – Přednáška 04

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1663703106971

Karty Anki: 1663703106971
GUID: Q97S1)4_I;; štítky: bi-ma2::p04 bi-spol::15 duplicate ni-spol::04.

### Otázka (Front)

Definujte dělení, dělící body, částečné intervaly intervalu \(\langle a, b \rangle\) a normu dělení.

### Odpověď (Back)

Mějme interval \(\langle a, b \rangle\). **Dělením **tohoto **intervalu **nazveme konečnou množinu\[\sigma = \set{x_0, x_1, \dots, x_n}\]takovou, že\[a = x_0 < x_1 < \cdots < x_n = b.\]Body \(x_k\), \(k = 1, 2, \dots, n - 1\) nazýváme **dělícími body intervalu** \(\langle a, b \rangle\) a interval \(\langle x_{k-1}, x_k \rangle\) \(k\)-tým **částečným intervalem** **intervalu **\(\langle a, b \rangle\). Číslo\[\nu(\sigma)  := \max \set{\Delta_k \mid k \in \hat n},\]kde\[\Delta_k := x_k - x_{k-1}, \quad k \in \hat n\]nazáváme **normou dělení** \(\sigma\).

## Poznámka Anki 1663703446387

Karty Anki: 1663703446387
GUID: Lp;e%i4hl/; štítky: bi-ma2::p04 bi-spol::15 duplicate ni-spol::04.

### Otázka (Front)

Definujte horní a dolní součet.

### Odpověď (Back)

Buďte funkce \(f\) definovaná a omezená na intervalu \(J = \langle a, b \rangle\) a \(\sigma = \set{x_0, x_1, \dots, x_n}\) dělení intervalu \(J\). Označme \(M_i(\sigma, f) := \sup \limits_{\langle x_{i-1}, x_i \rangle} f\) a \( m_i(\sigma, f) := \inf \limits_{\langle x_{i-1}, x_i \rangle} f\) pro každé \(i = 1, 2, \dots, n\). Potom součty \(S(\sigma, f) := \sum \limits_{i = 1} ^{n} M_i(\sigma, f) \Delta_i\) a \(s(\sigma, f) := \sum \limits_{i = 1} ^{n} m_i(\sigma, f) \Delta_i\) nazýváme **horním**, resp. **dolním**, **součtem funkce **\(f\) při dělení \(\sigma\).

## Poznámka Anki 1664195644619

Karty Anki: 1664195644629
GUID: u)IWydxSO6; štítky: bi-ma2::p04 bi-spol::15.

### Otázka (Front)

Definujte horní a dolní integrál.

### Odpověď (Back)

Pro funkci \(f\) definovanou a omezenou na uzavřeném intervalu \(J = \langle a, b \rangle\) definujme čísla
\[\overline{\int_a^b} f(x) \, \mathrm dx := \inf \set{S(\sigma) \mid \sigma \text{ dělení } J}\]\[\underline{\int_a^b} f(x) \, \mathrm dx := \sup \set{s(\sigma) \mid \sigma \text{ dělení } J}\]a nazýváme horním, resp. dolním, integrálem funkce \(f\) na intervalu \(J.\)

## Poznámka Anki 1664196025849

Karty Anki: 1664196025849
GUID: blyg^}T?=o; štítky: bi-ma2::p04 ni-spol::04.

### Otázka (Front)

Definujte Riemannův integrál funkce.

### Odpověď (Back)

Pokud pro funkci \(f\) definovanou a omezenou na uzavřeném intervalu \(J = \langle a, b \rangle\) platí 
\[\overline{\int_a^b} f(x) \, \mathrm dx = \underline{\int_a^b} f(x) \, \mathrm dx \in \mathbb{R},\]pak jejich společnou hodnotu nazýváme Riemannovým integrálem funkce \(f\) na intervalu \(J\) a toto číslo zančíme symboly \(\int_a^b f\), případně \(\int_a^b f(x) \, \mathrm dx\).

## Poznámka Anki 1664196265345

Karty Anki: 1664196265345
GUID: w![?DJ~lc5; štítky: bi-ma2::p04 bi-spol::15.

### Otázka (Front)

Definujte normální dělení.

### Odpověď (Back)

Posloupnost dělení \(\sigma_n\) nazveme normální, pokud pro její normy platí
\[\lim \limits_{n \to \infty} \nu(\sigma_n) = 0\]

## Poznámka Anki 1664196423566

Karty Anki: 1664196423566
GUID: vjZ.;s(X%,; štítky: bi-ma2::p04 bi-spol::15 ni-spol::04.

### Otázka (Front)

Vyslovte větu o postačující podmínce pro existenci Riemannova integrálu. Popište souvislost s horním a dolním součtem.

### Odpověď (Back)

Mějme funkci \(f\) spojitou na intervalu \(\langle a, b \rangle\). Pak na intervalu \(\langle a, b \rangle\) existuje její Riemannův integrál. Pokud navíc máme normální posloupnost dělení \((\sigma_n)_{n=1}^\infty\), pak existují limity\[\begin{matrix}
\displaystyle \lim_{n \to \infty} s(\sigma_n, f),\\
\displaystyle \lim_{n \to \infty} S(\sigma_n, f),\\
\end{matrix}\]a platí, že jsou rovny Riemannově integrálu funkce \(f\) na intervalu \(\langle a, b \rangle\).

## Poznámka Anki 1664198070787

Karty Anki: 1664198070788
GUID: m%XnpUaZ>R; štítky: bi-ma2::p04 bi-spol::15 ni-spol::04.

### Otázka (Front)

Vyslovte větu o aditivitě Riemannova integrálu.

### Odpověď (Back)

Nechť \(f\) a \(g\) jsou spojité funkce na intervalu \(\langle a, b \rangle\). Potom pro Riemannův integrál funkce \(f + g\) (která je také automaticky spojitá na \(\langle a, b \rangle\)) platí\[\int_a^b(f+g)(x) \, \mathrm dx = \int_a^bf(x) \, \mathrm dx + \int_a^bg(x) \, \mathrm dx.\]

## Poznámka Anki 1664198170300

Karty Anki: 1664198170300
GUID: xHUr$&)Buu; štítky: bi-ma2::p04 ni-spol::04.

### Otázka (Front)

Vyslovte větu o multiplikativitě Riemannova integrálu.

### Odpověď (Back)

Nechť \(f\) je spojitá na intervalu \(\langle a, b \rangle\) a \(c \in \mathbb{R}\) je konstanta. Potom pro Riemannův integrál funkce \(cf\) platí\[\int_a^b(cf)(x) \, \text dx = c\int_a^bf(x) \, \text dx.\]

## Poznámka Anki 1664198291993

Karty Anki: 1664198291993
GUID: wun5=FA;&6; štítky: bi-ma2::p04 bi-spol::15 ni-spol::04.

### Otázka (Front)

Vyslovte větu o aditivitě integrálu v mezích.

### Odpověď (Back)

Riemannův integrál funkce \(f\) na intervalu \(\langle a, b \rangle\) existuje, právě když pro každé \(c \in (a, b)\) existují Riemannovy integrály funkce \(f\) na intervalech \(\langle a, c \rangle\) a \(\langle c,  b \rangle\). V takovém případě platí\[\int_a^bf(x) \, dx = \int_a^cf(x) \, dx + \int_c^bf(x) \, dx.\]

## Poznámka Anki 1664208517991

Karty Anki: 1664208517991
GUID: xY=)+JyEQq; štítky: bi-ma2::p04 bi-spol::15.

### Otázka (Front)

Vyslovte větu o nerovnosti mezi integrály.

### Odpověď (Back)

Nechť jsou \(f\) a \(g\) spojité funkce na intervalu \(\langle a, b \rangle\) a nechť platí nerovnost \(f(x) \leq g(x)\) pro všechna \(x \in \langle a, b \rangle\). Potom pro jejich Riemannovy integrály platí:
\[\int_a^b f(x) \, \text dx \leq \int_a^b g(x) \,  \text dx.\]

## Poznámka Anki 1664208907218

Karty Anki: 1664208907219
GUID: i10P&=GcXb; štítky: bi-ma2::p04 bi-spol::15.

### Otázka (Front)

Definujte integrální součet.

### Odpověď (Back)

Pro funkci \(f\) spojitou na uzavřeném intervalu \(\langle a, b \rangle\) a dělení \(\sigma = \set{x_0 = a, x_1, \dots, x_n = b}\) tohoto intervalu definujeme integrální součet funkce \(f\) při dělení \(\sigma\) předpisem
\[\mathcal{J}(\sigma) \equiv \mathcal{J}(\sigma, \alpha) = \sum \limits_{i=1}^n f(\alpha_i) \Delta_i,\]kde \(\alpha_i\) patří do intervalu \(\langle x_{i-1}, x_i \rangle\), \(i = 1, 2, \dots, n\).

## Poznámka Anki 1664209087559

Karty Anki: 1664209087559
GUID: x)6w=vAUY7; štítky: bi-ma2::p04 bi-spol::15 duplicate ni-spol::04.

### Otázka (Front)

Vyslovte větu o Newtonově formuli.

### Odpověď (Back)

Nechť \(f\) je funkce spojitá na intervalu \(\langle a, b \rangle\) s primitivní funkcí \(F\). Pak platí rovnost
\[\int_a^b f(x) \, \mathrm  dx = F(b) - F(a) =: \Big[ F(x) \Big]_a^b.\]

### Doplňující pole (Extra)

Ve skutečnosti nemusí být funkce \(f\) v bodech \(a\) a \(b\) spojitá a platí obecnější vztah:
\[\int_a^b f(x) \, \mathrm  dx = \displaystyle \lim_{x \to b_-} F(x) - \displaystyle \lim_{x \to a_+} F(x) =: \Big[ F(x) \Big]_a^b.\]

## Poznámka Anki 1664209370988

Karty Anki: 1664209370988
GUID: M>C#nqHT1C; štítky: bi-ma2::p04 bi-spol::15.

### Otázka (Front)

Dokažte větu o Newtonově formuli.

### Odpověď (Back)

Uvažme \(\sigma = \set{x_0, x_1, \dots, x_n}\) dělení intervalu \(\langle a, b \rangle\). Použijeme Lagrangeovu větu o přírůstku funkce na funkci \(F\) a intervaly \(\langle x_{i-1}, x_i \rangle\) postupně pro \(i = 1, 2, \dots, n\),
\[F(b) - F(a) = \sum \limits_{i=1}^n \big( F(x_i) - F(x_{i-1}) \big) = \sum \limits_{i=1}^n F'(\alpha_i)(x_i - x_{i-1}) = \sum \limits_{i=1}^n f(\alpha_i) \Delta_i,\]kde \(a_i \in (x_{i-1}, x_i)\), \(i = 1, 2, \dots, n\). Takže
\[F(b) - F(a) = \mathcal{J}(\sigma).\]Uvážíme-li nyní libovolnou normální posloupnost dělení \((\sigma_n)\), pak
\[F(b) - F(a) = \displaystyle \lim_{n \to \infty} \mathcal J(\sigma_n) = \int_a^b f(x) \, \text dx.\]

## Poznámka Anki 1717504422192

Karty Anki: 1717504422192
GUID: Bk!4/K{kOP; štítky: bi-ma2::p04 bi-spol::15.

### Otázka (Front)

Zakreslete geometrický význam integrálu.

### Odpověď (Back)

Geometrický význam integrálu lze znázornit následujícím způsobem:

| 
     [Obrázek: paste-82bb2f349a60472ddc8ea3df83d566cbcc1bbce3.jpg; soubor je v media/ v doprovodném ZIP]  |  [Obrázek: paste-7a61567a6560fdfebd7471fb266716c16d7584c8.jpg; soubor je v media/ v doprovodném ZIP]  |

