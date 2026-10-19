# NI-MKY – Přednáška 05

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MKY
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1741292993090

Karty Anki: 1741292993090
GUID: m->flTBN}n; štítky: ni-mky::p05.

### Otázka (Front)

Definujte vedoucí koeficient, konstantní člen a stupeň polynomu nad okruhem.

### Odpověď (Back)

Mějme okruh \(R\) a polynom \(p(x) \in R[x]\) takový, že\[p(x) = \displaystyle \sum_{k = 0}^n a_k x^k.\]Předpokládejme, že \(a_n \neq 0\). Potom \(a_n\) nazýváme **vedoucím koeficientem** polynumu \(p(x)\) a \(a_0\) jeho **konstantním členem**. Číslo \(n\) se nazývá stupněm polynomu a značí \(\deg p(x)\). Je-li \(p(x)\) nulový polynom, klademe \(\deg p(x) = - \infty\).

## Poznámka Anki 1741293138563

Karty Anki: 1741293138564
GUID: vC[WB@B=gd; štítky: ni-mky::p05.

### Otázka (Front)

Definujte monický a konstantní polynom.

### Odpověď (Back)

Mějme okruh s jedničkou \(R\) a polynom \(p(x) \in R[x]\). Pokud je jeho vedoucí koeficient \(a_n = 1\), pak \(p(x) \) nazýváme **monickým polynomem**. Pokud platí \(\deg p(x) \leq 0\), nazýváme jej **konstantním polynomem**.

## Poznámka Anki 1741293535304

Karty Anki: 1741293535304
GUID: A>$QO}FC?t; štítky: ni-mky::p05.

### Otázka (Front)

Vyslovte větu o vlivu operací na stupně polynomů nad okruhem.

### Odpověď (Back)

Mějme okruh \(R\) a polynomy \(p(x), q(x) \in R[x]\). Potom\[\begin{align}
\deg \big( p(x) + q(x) \big) &\leq \max \{ \deg p(x), \deg q(x) \},\\
\deg \big( p(x) \cdot q(x) \big) &\leq \deg p(x) + \deg q(x).
\end{align}\]Je-li navíc \(R\) oborem integrity, pak\[\deg \big( p(x) \cdot q(x) \big) = \deg p(x) + \deg q(x).\]

## Poznámka Anki 1741293629517

Karty Anki: 1741293629517
GUID: GGIOZyTdWB; štítky: ni-mky::p05.

### Otázka (Front)

Vyslovte větu o vlastnostech okruhu polynomů.

### Odpověď (Back)

Mějme okruh \(R\). Potom:

- \(R[x]\) je komutativní právě tehdy, když \(R\) je komutativní;

- \(R[x]\) je okruhem s jedničkou právě tehdy, když \(R\) je okruhem s jedničkou;

- \(R[x]\) je oborem integrity právě tehdy, když \(R\) je oborem integrity.

## Poznámka Anki 1741293842404

Karty Anki: 1741293842404
GUID: vQ#&!eCAW-; štítky: ni-mky::p05.

### Otázka (Front)

Vyslovte větu o zbytcích po dělení polynomů nad tělesem.

### Odpověď (Back)

Mějme těleso \(T\) a polynomy \(p(x), g(x) \in T[x]\) takové, že \(g(x) \neq 0\). Potom pro každý \(p(x)\) existují jednoznačně určené polynomy \(q(x), r(x) \in T[x]\) splňující\[p(x) = q(x)g(x) + r(x),\]přičemž \(\deg r(x) < \deg g(x)\).

## Poznámka Anki 1741294017789

Karty Anki: 1741294017789
GUID: Qf`qcp^#n`; štítky: ni-mky::p05.

### Otázka (Front)

Vyslovte větu o největším společném děliteli polynomů nad tělesem.

### Odpověď (Back)

Mějme těleso \(T\) a polynomy \(p_1(x), \dots, p_n(x) \in T[x]\), z nichž je aspoň jeden nenulový. Potom existuje právě jeden monický polynom \(q(x) \in T[x]\) takový, že \(q(x) = \gcd \big( p_1(x), \dots, p_n(x) \big)\) a lze jej vyjádřit ve tvaru\[d = a_1 p_1(x) + \dots + a_n p_n(x),\]kde \(a_1, \dots, a_n \in T[x]\).

## Poznámka Anki 1741294030360

Karty Anki: 1741294030360
GUID: y>@ByGJZdz; štítky: duplicate ni-mky::p05.

### Otázka (Front)

Definujte největší společný dělitel polynomů.

### Odpověď (Back)

Mějme dva polynomy \(f(x), g(x) \in T[x]\). Potom polynom \(h(x) \in T[x]\) nazveme největším společným dělitelem polynomů \(f(x)\) a \(g(x)\), značeno \(\gcd \big( f(x), g(x) \big)\), jestliže:

- \(h(x)\) dělí \(f(x)\);

- \(h(x)\) dělí \(g(x)\);

- každý polynom, který dělí \(f(x)\) i \(g(x)\), dělí také \(h(x)\).

### Doplňující pole (Extra)

To, že \(h(x)\) dělí \(f(x)\), znamená, že existuje \(q(x) \in T[x]\) takové, že\[f(x) = q(x)h(x).\]

## Poznámka Anki 1741294222059

Karty Anki: 1741294222059
GUID: ms9z=?*MCl; štítky: duplicate ni-mky::p05.

### Otázka (Front)

Definujte ireducibilní polynom nad okruhem.

### Odpověď (Back)

Mějme polynom \(p(x) \in R[x]\) stupně aspoň \(1\). Řekneme, že \(p(x)\) je ireducibilní nad okruhem \(R\), jestliže pro každé dva polynomy \(u(x), v(x) \in R[x]\) platí\[ p(x) = u(x)v(x) \Rightarrow \deg \big( u(x) \big) = 0 \lor \deg \big( v(x) \big) = 0.\]

### Doplňující pole (Extra)

**V předmětu NI-MKY** je požadováno, aby buď \(u(x)\) nebo \(v(x)\) byl konstantní polynom, tedy\[\deg \big( u(x) \big) \leq 0 \lor \deg \big( v(x) \big) \leq 0.\]

## Poznámka Anki 1741294407464

Karty Anki: 1741294407464
GUID: g>|X|e90)); štítky: ni-mky::p05.

### Otázka (Front)

Vyslovte větu o rozkladu na ireducibilní polynomy.

### Odpověď (Back)

Mějme těleso \(T\). Každý polynom \(p(x) \in T[x]\) kladného stupně lze vyjádřit ne vtavu\[p(x) = \alpha p_1^{k_1} \cdots p_n^{k_n},\]kde \(\alpha \in T\), \(p_1, \dots, p_n \in T[x]\) jsou různé monické ireducibilní polynomy a \(k_1, \dots, k_n \in \mathbb N\). Tento rozklad je určen jednoznačně až na pořadí členů.

## Poznámka Anki 1741294638884

Karty Anki: 1741294638884
GUID: iR:EXZT*d:; štítky: ni-mky::p05.

### Otázka (Front)

Vyslovte větu o vztahu faktorokruhu a ireducibilního polynomu.

### Odpověď (Back)

Mějme těleso \(T\) a polynom \(p(x) \in T[x]\). Potom faktorokruh \(T[x]/ \big(p(x)\big)\) je tělesem právě tehdy, když je \(p(x)\) ireducibilní.

## Poznámka Anki 1741294735604

Karty Anki: 1741294735605
GUID: ii5/4^`R?e; štítky: ni-mky::p05.

### Otázka (Front)

Definujte kořen polynomu nad tělesem.

### Odpověď (Back)

Mějme těleso \(T\) a polynom \(p(x) \in T[x]\). Prvek \(a \in T\) nazýváme kořenem polynomu \(p(x) \in T[x]\), pokud \[p(a) = 0.\]

## Poznámka Anki 1741294792626

Karty Anki: 1741294792626
GUID: AjaAIY^)Y/; štítky: duplicate ni-mky::p05.

### Otázka (Front)

Vyslovte větu o faktorech polynomu (polynomial factor theorem).

### Odpověď (Back)

Mějme těleso \(T\) a polynom \(p(x) \in T[x]\) stupně \(n\). Prvek \(\xi \in T\) je kořen polynomu \(p(x)\) právě tehdy, když\[p(x) = (x - \xi)g(x),\]kde \(g(x) \in T[x]\) je polynom stupně \(n - 1\).

## Poznámka Anki 1741295083493

Karty Anki: 1741295083493
GUID: wI+}(fM~:6; štítky: ni-mky::p05.

### Otázka (Front)

Definujte násobnost kořene a jednoduchý kořen polynomu nad tělesem.

### Odpověď (Back)

Mějme těleso \(T\), \(a \in T\) a polynom \(p(x) \in T[x]\) takové, že \(a\) je kořenem \(p(x)\). **Násobností kořene** \(a\) pak nazýváme \(n \in \mathbb N\) takové, že \(p(x)\) je dělitelný polynomem \((x - a)^k\), ale už není dělitelný poylnomem \((x - a)^{k + 1}\). Pro \(n = 1\) nazýváme \(a\) **jednoduchým kořenem** \(p(x)\).

## Poznámka Anki 1741295320423

Karty Anki: 1741295320423
GUID: L:m.s*IpNI; štítky: ni-mky::p05.

### Otázka (Front)

Vyslovte větu o počtu kořenů polynomu nad tělesem.

### Odpověď (Back)

Mějme těleso \(T\), polynom \(p(x) \in T[x]\) kladného stupně a \(a_1, \dots, a_n \in T\) různé kořeny \(p(x)\) s násobnostmi \(k_1, \dots, k_n\). Potom polynom\[(x - a_1)^{k_1} \cdots (x - a_n)^{k_n}\]dělí polynom \(p(x)\). Z toho plyne, že\[k_1 + \cdots + k_n \leq n\]a \(p(x)\) tedy můze mít nejvýše \(n\) různých kořenů v \(T\).

## Poznámka Anki 1741295381649

Karty Anki: 1741295381649
GUID: z$B@:7yT2p; štítky: ni-mky::p05.

### Otázka (Front)

Vyslovte větu o vztahu kořene a derivace polynomu nad tělesem.

### Odpověď (Back)

Mějme těleso \(T\) a polynom \(p(x) \in T[x]\). Potom \(a \in T\) je vícenásobným kořenem polynomu \(p(x)\) právě tehdy, když je kořenem jak \(p(x)\), tak \(p'(x)\).

## Poznámka Anki 1741296081267

Karty Anki: 1741296081267
GUID: de^_@=3a.u; štítky: ni-mky::p05.

### Otázka (Front)

Vyslovte a dokažte větu o ireducibilních polynomech nízkých stupňů.

### Odpověď (Back)

Mějme těleso \(T\) a polynom \(p(x) \in T[x]\) stupně \(2\) nebo \(3\). Pak \(p(x)\) je ireducibilní právě tehdy, když nemá kořeny \(T\).

**Důkaz pro** „\(\Rightarrow\)“
Mějme ireducibilní polynom \(p(x) \in T[x]\) stupně \(n \geq 2\). Potom z věty o faktorech polynomu plyne, že nemá kořen. V opačném případě by totiž byl dělitelný nějakým polynomem stupně \(n -1\).

**Důkaz pro** „\(\Leftarrow\)“
Pro spor předpokládejme, že \(p(x) \in T[x]\) je reducibilní polynom stupně \(2\) nebo \(3\), který nemá žádné kořeny. Potom existují \(q(x), r(x) \in T[x]\) splňující\[p(x) = q(x) r(x),\]kde ale \(\deg q(x) > 0\) a \(\deg r(x) > 0\), jinak by \(p(x) \) byl ireducibilní. Protože však platí\[\deg q(x) + \deg r(x) = \deg f(x) \leq 3,\]musí být buď \(\deg q(x) = 1\) nebo \(\deg r(x) = 1\). Tedy alespoň jeden z těchto polynomů má kořen \(a \in T\). Protože \(p(x)\) je součinem \(q(x)\) a \(r(x)\), bude \(a\) i kořenem polynomu \(p(x)\), což je spor.

