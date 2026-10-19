# BI-MA2 – Přednáška 05

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1664209568299

Karty Anki: 1664209568299
GUID: Rbs:Ado)t:; štítky: bi-ma2::p05 bi-spol::15 duplicate ni-spol::04.

### Otázka (Front)

Vyslovte větu o per partes pro určitý integrál.

### Odpověď (Back)

Nechť \(f\) a \(g\) jsou funkce spojité na \( \langle a, b \rangle\), \(f\) má spojitou derivaci na intervalu \(\langle a, b \rangle\) a nechť \(G\) je primitivní funkce k funkci \(g\) na intervalu \(\langle a, b \rangle\). Potom
\[\int_a^b f(x)g(x) \, \text dx = \big[ f(x)G(x) \big]_a^b - \int_a^b f'(x)G(x) \, \text dx.\]

## Poznámka Anki 1664209743877

Karty Anki: 1664209743877
GUID: Ju)gzGU}pr; štítky: bi-ma2::p05 bi-spol::15.

### Otázka (Front)

Dokažte větu o per partes pro určitý integrál.

### Odpověď (Back)

Funkce \(fG\) je primitivní funkcí k funkci \(f'G + fg\) na intervalu \((a, b)\) a spojitá na \(\langle a, b \rangle\). Předpoklady spojitosti na intervalu \(\langle a, b \rangle\) zaručují existenci integrálů \(\int_a^b f'G\) a \(\int_a^b fg\). Použijeme-li linearitu integrálu a Newtonovu fomuli, dostáváme
\[\int_a^b f'(x)G(x) \, \text dx + \int_a^b f(x)g(x) \, \text dx = \int_a^b (fG)'(x) \, \text dx = \big[ f(x)G(x) \big]_a^b.\]

## Poznámka Anki 1664216368133

Karty Anki: 1664216368133
GUID: u<n8$1*%a&; štítky: bi-ma2::p05 bi-spol::15 duplicate ni-spol::04.

### Otázka (Front)

Vyslovte větu o substituci (I) v určitém integrálu.

### Odpověď (Back)

Nechť pro funkce \(f\) a \(\varphi\) platí

- \(\varphi\) a její derivace \(\varphi'\) jsou spojité na \(\langle \alpha, \beta \rangle\),

- \(f\) je spojitá na \(\varphi(\langle \alpha, \beta \rangle)\).

Potom

\[\int_\alpha^\beta f\big(\varphi(t)\big) \cdot \varphi'(t) \, \text dt = \int_{\varphi(\alpha)}^{\varphi(\beta)} f(x) \, \text dx.\]

## Poznámka Anki 1664800766465

Karty Anki: 1664800766465
GUID: tVNt@;t;G_; štítky: bi-ma2::p05.

### Otázka (Front)

Jak spočteme Riemannův integrál nespojité funkce.

### Odpověď (Back)

Předpokládejme, že pro funkci \(f\) na intervalu \(\langle a, b \rangle\) platí

- existuje \(c \in (a, b)\) tak, že \(f\) je spojitá na \(\langle a, c)\) i \((c, b \rangle\),
- existují jednostranné limity funkce \(f\) v bodě \(c\).

Potom můžeme počítat její Riemannův integrál jako

\[\int_a^b f(x) \, \text dx = \int_a^c f(x) \, \text dx + \int_c^b f(x) \, \text dx.\]

## Poznámka Anki 1664802326629

Karty Anki: 1664802326629
GUID: f=|nZUuQq`; štítky: bi-ma2::p05 bi-spol::15.

### Otázka (Front)

Definujte zobecněný Riemannův integrál.

### Odpověď (Back)

Nechť \(f\) je funkce definovaná na intervalu \(\langle a, b)\) pro nějaké \(a \in \mathbb{R}\) a \(b \in (a, +\infty \rangle\), která je Riemannovsky integrabilní na intervalu \(\langle a, c \rangle\) pro každé \(c \in (a, b)\). Pokud existuje konečná limita
\[\displaystyle \lim_{c \to b_-} \int_a^c f(x) \, \text dx,\]pak její hodnotu značíme
\[\int_a^b f(x) \, \text dx\]a nazýváme zobecněným Riemannovým integrálem funkce \(f\) na intervalu \(\langle a, b)\) a říkáme, že integrál \(\int_a^b f(x) \, \text dx\) konverguje.

## Poznámka Anki 1664802934880

Karty Anki: 1664802934880
GUID: s$G3Jgqxo~; štítky: bi-ma2::p05 bi-spol::15.

### Otázka (Front)

Definujte absolutně konvergentní zobecněný Riemannův integrál na \(\mathbb{R}\).

### Odpověď (Back)

Buď \(f\) spojitá funkce definovaná na \(\mathbb{R}\). Pokud existuje konečná limita
\[\displaystyle \lim_{c \to +\infty} \int_{-c}^c |f(x)| \, \text dx,\]pak tuto její hodnotu značíme 
\[\int_{-\infty}^{+\infty} \, |f(x)| \, \text dx\]a o \(f\) říkáme, že má absolutně konvergentní zobecněný Riemannův integrál na \(\mathbb{R}\).

## Poznámka Anki 1664803405754

Karty Anki: 1664803405755
GUID: g@fK(s>oEn; štítky: bi-ma2::p05.

### Otázka (Front)

Jak lze využít symetrie funkcí při integraci?

### Odpověď (Back)

Nechť je funkce \(f\) spojitá na uvažovaných intervalech.

- Je-li \(f\) sudá funkce na \(\langle -a, a \rangle\), pak

\[\int_{-a}^a f(x) \, \mathrm dx = 2 \int_0^a f(x) \, \mathrm dx.\]

- Je-li \(f\) lichá funkce na \(\langle -a, a \rangle\), pak

\[\int_{-a}^a f(x) \, \mathrm dx = 0.\]

- Je-li \(f\) periodická na \(\mathbb{R}\) s periodou \(T\), pak pro každé \(a, b \in \mathbb{R}\), platí

\[\int_a^{a+T} f(x) \, \mathrm dx = \int_b^{b+T} f(x) \, \mathrm dx.\]

