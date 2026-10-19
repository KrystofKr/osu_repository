# BI-MA1 – Přednáška 11

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA1
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1650900176070

Karty Anki: 1650900176070
GUID: k6-ea3K``D; štítky: bi-ma1::p11 bi-spol::14.

### Otázka (Front)

Definujte inflexní bod.

### Odpověď (Back)

Nechť \(f\) je spojitá v bodě \(c\). Bod \(c\) nazveme inflexním bodem funkce \(f\), právě když existuje \(\delta > 0\) takové, že \(f\) je ryze konvexní na intervalu \((c-\delta, c)\) a ryze konkávní na intervalu \((c, c + \delta)\), nebo naopak.

## Poznámka Anki 1650900356449

Karty Anki: 1650900356449
GUID: JN9lfT?kgP; štítky: bi-ma1::p11 bi-spol::14.

### Otázka (Front)

Definujte asymptotu.

### Odpověď (Back)

- Řekneme, že funkce \(f\) má v bodě \(a \in \mathbb{R}\) asymptotu \(x = a\), právě když \(\lim \limits_{x \to a +} f(x)\) nebo \(\lim \limits_{x \to a -} f(x)\) existuje a je rovna \(+ \infty\) a \(- \infty\).
- Řekneme, že přímka \(y = kx + q \) je asymptotou funkce \(f\) v \(+ \infty\) resp. v \(- \infty\) když \(\lim \limits_{x \to +\infty}(f(x) - kx - q) = 0\) resp. \(\lim \limits_{x \to -\infty}(f(x) - kx - q) = 0\).

## Poznámka Anki 1654290951868

Karty Anki: 1654290951868
GUID: gz~(q.XNbk; štítky: bi-ma1::p11 bi-spol::14.

### Otázka (Front)

Vyslovte tři postačující podmínky pro existenci lokálního extrému funkce.

### Odpověď (Back)

Mějme funkci \(f\) a bod \(a \in D_f\) takové, že \(f\) je spojitá v bodě \(a\). Potom pokud:

- \(f\) je (ostře) rostoucí na nějakém levém okolí bodu \(a\) a (ostře) klesající na nějakém pravém okolí bodu \(a\), potom má \(f\) v bodě \(a\) (ostré) lokální maximum.

- \(f\) je (ostře) klesající na nějakém levém okolí bodu \(a\) a (ostře) rostoucí na nějakém pravém okolí bodu \(a\), potom má \(f\) v bodě \(a\) (ostré) lokální minimum.

Nechť pro funkci \(f\) platí \(f'(c) = 0\).

- Pokud je \(f\) (ryze) konvexní v bodě \(c\), pak má funkce \(f\) v bodě \(c\) (ostré) lokální minimum.
- Pokud je \(f\) (ryze) konkávní v bodě \(c\), pak má funkce \(f\) v bodě \(c\) (ostré) lokální maximum.
Mějme funkci \(f\) diferencovatelnou na okolí bodu \(a \in D_f\). Pokud první derivace funkce \(f\) v bodě \(a\) mění znaménko, potom má \(f\) v bodě \(a\) ostrý lokální extrém.

## Poznámka Anki 1654291750015

Karty Anki: 1654291750015
GUID: DMlOK&Kbe9; štítky: bi-ma1::p11 bi-spol::14.

### Otázka (Front)

Vyslovte větu o postačující podmínce existence globálního extrému.

### Odpověď (Back)

Funkce \(f\) spojitá a definovaná právě na uzavřeném intervalu \(\langle a, b \rangle\) nabývá globálního minima a maxima na tomto intervalu. Tyto extrémy mohou být nabyty pouze v krajních bodech tohoto intervalu a v bodech, kde je první derivace \(f\) nulová nebo neexistuje.

## Poznámka Anki 1654506676508

Karty Anki: 1654506676509
GUID: uY~lDTrpo(; štítky: bi-ma1::p11 bi-spol::14.

### Otázka (Front)

Vyslovte větu o vztahu první derivace a monotonie funkce a dokažte ji.

### Odpověď (Back)

Nechť \(f\) je spojitá na intervalu \(J\) a pro každé \(x \in J^{ \circ }\) existuje derivace \(f'(x)\). Potom platí následující tvrzení:

1. \((\forall x \in J^{ \circ })(f'(x) \geq 0) \Rightarrow\) \(f\) je rostoucí na \(J\),

2. \((\forall x \in J^{ \circ })(f'(x) \leq0) \Rightarrow\) \(f\) je klesající na \(J\),

3. \((\forall x \in J^{ \circ })(f'(x) > 0) \Rightarrow\) \(f\) je ostře rostoucí na \(J\),

4. \((\forall x \in J^{ \circ })(f'(x) < 0) \Rightarrow\) \(f\) je ostře klesající na \(J\),

5. \((\forall x \in J^{ \circ })(f'(x) = 0) \Rightarrow\) \(f\) je konstantní na \(J\).

**Důkaz pro 1. bod:**
Buďte \(x_1, x_2 \in J\) taková, že \(x_1 < x_2\). Podle Lagrangeovy věty o přírůstku funkce aplikované na interval \(\langle x_1, x_2 \rangle\) existuje \(c \in (x_1, x_2)\) takové, že
 \[f'(c) = \frac{ f(x_2) - f(x_1) }{ x_2 - x_1 }\]
Protože \(c \in J^{ \circ}\), je \(f'(x) \geq 0\). Tudíž
\[\frac{ f(x_2) - f(x_1) }{ x_2 - x_1 } \geq 0 \Rightarrow f(x_2) - f(x_1) \geq 0 \Rightarrow f(x_1) \leq f(x_2)\]

## Poznámka Anki 1655200493098

Karty Anki: 1655200493098
GUID: j?xv42#&*?; štítky: bi-ma1::p11 bi-spol::14.

### Otázka (Front)

Vyslovte zobecněnou definici (ryze) konvexní (resp. (ryze) konkávní) funkce na intervalu.

### Odpověď (Back)

Funkci \(f\) definovanou na intervalu \(J\) nazveme konvexní (resp. konkávní) na intervalu \(J\), právě když pro každé \(x_1, x_2, x_3 \in J\) splňující \(x_1 < x_2 < x_3\), leží bod \((x_2, f(x_2))\) buďto pod (resp. nad) přímkou spojující body \((x_1, f(x_1))\) a \((x_3, f(x_3))\), nebo na ní.
Pokud bychom nepřipustili možnost bodů ležet na této spojnici, definovali bychom ryze konvexní (resp. ryze konkávní) funkci na intervalu \(J\).

