# NI-MPI – Přednáška 12

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 19 poznámek, 19 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1732710933552

Karty Anki: 1732710933552
GUID: M;o]L3/FAn; štítky: duplicate ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Definujte okruh (ring) a komutativní okruh.

### Odpověď (Back)

Nechť \(M\) je neprázdná množina a \(+ : M \times M \to M\), \(\cdot : M \times M \to M\) dvě binární operace. Pokud:

- \((M, +) \) je abelovská grupa,

- \((M , \cdot)\) je monoid,

- platí levý a pravý distributivní zákon:

\[(\forall a,b,c \in M) \big( a(b + c) = ab + ac \wedge (b+c)a = ba + ca\big),\]nazýváme uspořádanou trojici \(R = (M, +, \cdot)\) okruhem (ring). Je-li navíc \((M, \cdot)\) komutativní monoid, je \(R\) komutativním okruhem.

### Doplňující pole (Extra)

**V předmětu NI-MKY** je okruh definován tak, že \((M, +)\) je pouze pologrupa. Objekt, který je definován výše se pak nazývá okruhem s jedničkou.

## Poznámka Anki 1732711216169

Karty Anki: 1732711216169
GUID: rmY=z)$cJ$; štítky: duplicate ni-mpi::p12.

### Otázka (Front)

Definujte těleso (field) a komutativní těleso.

### Odpověď (Back)

Nechť \(M\) je neprázdná množina a \(+ : M \times M \to M\), \(\cdot : M \times M \to M\) dvě binární operace. Pokud:

- \((M, +) \) je abelovská grupa,

- \((M \smallsetminus \{ 0 \}, \cdot)\) je grupa,

- platí levý a pravý distributivní zákon:

\[(\forall a,b,c \in M) \big( a(b + c) = ab + ac \wedge (b+c)a = ba + ca\big),\]nazýváme uspořádanou trojici \(T = (M, +, \cdot)\) tělesem (field). Je-li navíc \((M \smallsetminus \{ 0 \}, \cdot)\) abelovská grupa, je \(T\) komutativní těleso.

### Doplňující pole (Extra)

**V předmětech NI-MPI a NI-MKY **je těleso vždy definováno jako komutativní těleso, tedy okruh \(T = (M, + , \cdot)\), pro který platí, že \((M \smallsetminus \{ 0 \}, \cdot)\) je abelovksá grupa, případně komutativní okruh s dělením.

## Poznámka Anki 1732712162985

Karty Anki: 1732712162985
GUID: s3-,n$;TB:; štítky: duplicate ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Definujte dělitele nuly a obor integrity (integral domain).

### Odpověď (Back)

Mějme okruh \((M, +, \cdot)\). Nenulové prvky \(a, b \in M\) nazýváme **dělitelé nuly**, právě když\[a \cdot b = b \cdot a = 0.\]**Obor integrity **(integral domain) je potom komutativní okruh, ve kterém neexistují dělitelé nuly.

### Doplňující pole (Extra)

**V předmětu NI-MKY** je obor integrity definován jako komutativní okruh s jedničkou, kde \(1 \neq 0\) a neexistují dělitelé nuly. To vychází z toho, že NI-MKY definuje okruh tak, že \((M, \cdot)\) je pologrupa. V případě, že \(a \neq 0\) a \(b \neq 0\), se pro \(a\) a \(b\) v NI-MKY používá označení netriviální dělitelé nuly, což odpovídá dělitelům nuly z NI-MPI.

## Poznámka Anki 1732712753086

Karty Anki: 1732712753087
GUID: LJD)gzJ,pg; štítky: duplicate ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Definujte homomorfismus okruhů a těles.

### Odpověď (Back)

Zobrazení \(h \) z okruhu \(R\) do okruhu \(S\) je **homomorfismus těchto okruhů**, jestliže: 

- \(h\) je homomorfismem z aditivní grupy \(R\) do aditivní grupy \(S\),
- \(h\) je homomorfismem z multiplikativního monoidu \(R\) do multiplikativního monoidu \(S\) a platí \(h(1_R) = 1_S\).

Zobrazení \(h \) z tělesa \(R\) do tělesa \(S\) je **homomorfismus těchto těles**, jestliže: 

- \(h\) je homomorfismem z aditivní grupy \(R\) do aditivní grupy \(S\),
- \(h\) je homomorfismem z multiplikativní grupy \(R\) do multiplikativní grupy \(S\).

### Doplňující pole (Extra)

Monomorfismus, epimorfismus a izomorfimus definujeme podobně jako u grupoidů.
**V přemetu NI-MKY **je okruh definován tak, že \((M, +)\) je pouze pologrupa. Druhá podmínka definice homomorfismu okruhů tak bude požadovat, aby \(h\) byl homomorfismem multiplikativní pologrupy \(R\) do multiplikativní pologrupy \(S\). Podmínka na zobrazení neutrálního prvku vzhledem k násobení může být vypuštěna.

## Poznámka Anki 1732713138423

Karty Anki: 1732713138423
GUID: I9h5OM2(wO; štítky: duplicate ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Definujte polynom nad okruhem.

### Odpověď (Back)

Mějme okruh \(R\) a \(a_i \in R\) pro \(i = 0, 1, \dots n\). Polynomem nad okruhem \(R\) s formální proměnnou \(x\) nazýváme formální výraz\[P(x) = \displaystyle \sum_{i = 0}^n a_i x^i.\]

## Poznámka Anki 1732713465975

Karty Anki: 1732713465975
GUID: f:iaMEgjo|; štítky: duplicate ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Definujte okruh polynomů (polynomial ring).

### Odpověď (Back)

Mějme okruh \(R\). Potom množina všech polynomů nad okruhem \(R\) spolu s operacemi sčítání a násobení polynomů definovanými předpisy\[\begin{matrix}
\displaystyle \sum_{i = 0}^n a_i x^i + \displaystyle \sum_{i = 0}^n b_i x^i := \displaystyle \sum_{i = 0}^n (a_i + b_i) x^i,\\
\bigg( \displaystyle \sum_{i = 0}^n a_i x^i  \bigg) \cdot \bigg( \displaystyle \sum_{i = 0}^m b_i x^i \bigg) := \displaystyle \sum_{i = 0}^{n + m} \bigg( \displaystyle \sum_{j + k = i} a_j b_k \bigg) x^i,
\end{matrix}\]kde \(a_i, b_i \in R\) pro všechna \(i\), tvoří okruh polynomů nad okruhem \(R\), který značíme \(R[x]\).

## Poznámka Anki 1733343991395

Karty Anki: 1733343991395
GUID: c#mR+s%H(@; štítky: duplicate ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Definujte největší společný dělitel polynomů.

### Odpověď (Back)

Mějme dva polynomy \(f(x), g(x) \in T[x]\). Potom polynom \(h(x) \in T[x]\) nazveme největším společným dělitelem polynomů \(f(x)\) a \(g(x)\), značeno \(\gcd \big( f(x), g(x) \big)\), jestliže:

- \(h(x)\) dělí \(f(x)\);

- \(h(x)\) dělí \(g(x)\);

- každý polynom, který dělí \(f(x)\) i \(g(x)\), dělí také \(h(x)\).

### Doplňující pole (Extra)

To, že \(h(x)\) dělí \(f(x)\), znamená, že existuje \(q(x) \in T[x]\) takové, že\[f(x) = q(x)h(x).\]

## Poznámka Anki 1733344082567

Karty Anki: 1733344082567
GUID: IC#pjVb;}0; štítky: ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Vyslovte větu o Bézoutově rovnosti pro polynomy.

### Odpověď (Back)

Mějme nenulové polynomy \(f(x), g(x) \in T[x]\). Pak existují polynomy \(u(x), v(x) \in T[x]\) takové, že\[u(x)f(x) + v(x)g(x) = \gcd \big( f(x), g(x) \big).\]

## Poznámka Anki 1733344754285

Karty Anki: 1733344754285
GUID: Ng/XDqSPkj; štítky: duplicate ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Vyslovte větu o faktorech polynomu (polynomial factor theorem).

### Odpověď (Back)

Mějme těleso \(T\) a polynom \(p(x) \in T[x]\) stupně \(n\). Prvek \(\xi \in T\) je kořen polynomu \(p(x)\) právě tehdy, když\[p(x) = (x - \xi)g(x),\]kde \(g(x) \in T[x]\) je polynom stupně \(n - 1\).

## Poznámka Anki 1733345220656

Karty Anki: 1733345220656
GUID: Lza%C4*I}z; štítky: duplicate ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Definujte ireducibilní polynom nad okruhem.

### Odpověď (Back)

Mějme polynom \(p(x) \in R[x]\) stupně aspoň \(1\). Řekneme, že \(p(x)\) je ireducibilní nad okruhem \(R\), jestliže pro každé dva polynomy \(u(x), v(x) \in R[x]\) platí\[ p(x) = u(x)v(x) \Rightarrow \deg \big( u(x) \big) = 0 \lor \deg \big( v(x) \big) = 0.\]

### Doplňující pole (Extra)

**V předmětu NI-MKY** je požadováno, aby buď \(u(x)\) nebo \(v(x)\) byl konstantní polynom, tedy\[\deg \big( u(x) \big) \leq 0 \lor \deg \big( v(x) \big) \leq 0.\]

## Poznámka Anki 1733345255250

Karty Anki: 1733345255250
GUID: eesM!_h>iu; štítky: ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Definujte konečné těleso (finite field).

### Odpověď (Back)

Konečně těleso je takové těleso, které má konečný počet prvků.

## Poznámka Anki 1733346743964

Karty Anki: 1733346743964
GUID: cR|Qap!!A_; štítky: ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Vyslovte větu o řádu konečného tělesa.

### Odpověď (Back)

Řád konečného tělesa je vždy mocnina provčísla, tedy \(p^n\), kde \(p\) je prvočíslo a \(n \in \mathbb Z^+\). Navíc platí, že všechna tělesa řádu \(p^n\) jsou vzájemně izomorfní.

## Poznámka Anki 1733346833557

Karty Anki: 1733346833558
GUID: A+#sUiQ/Q#; štítky: ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Definujte Galoisovo těleso (Galois field) a jeho charakteristiku.

### Odpověď (Back)

**Galoisovo těleso** (Galois field) \(GF(p^n)\) je konečné těleso s \(p^n\) prvky, kde \(p\) je prvočíslo a \(n \in \mathbb Z^+\). Číslo \(p\) se nazývá **charakteristika** tělesa \(GF(p^n)\).

## Poznámka Anki 1733669322142

Karty Anki: 1733669322142
GUID: PwrJ&XN/T9; štítky: ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Popište vlastnosti aditivní grupy tělěsa \((\mathbb Z_p, +, \cdot)\).

### Odpověď (Back)

Aditivní grupa \((\mathbb Z_p, +)\) tělesa \((\mathbb Z_p, +, \cdot)\) má následující vlastnosti:

- její řád je \(p\),
- je cyklická,
- každý její nenulový prvek je jejím generátorem,
- je grupou i pro neprvočíselná \(p\).

## Poznámka Anki 1733669658799

Karty Anki: 1733669658800
GUID: C49pJt><-p; štítky: ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Popište vlastnosti multiplikativní grupy tělesa \((\mathbb Z_p, +,\cdot)\).

### Odpověď (Back)

Multiplikativní grupa \((\mathbb Z_p \smallsetminus \{ 0 \}, \cdot)\) tělesa \((\mathbb Z_p, +, \cdot)\) má následující vlastnosti:

- její řád je \(p - 1\),
- je cyklická,
- počet jejích generátorů je roven počtu čísel nesoudělných s \(p - 1\),
- je grupou pouze pro prvočíselná \(p\) (jinak obsahuje dělitele nuly).

## Poznámka Anki 1733670011146

Karty Anki: 1733670011146
GUID: G{>S_w!5H#; štítky: ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Popište konstrukci konečného tělesa neprvočíselného řádu.

### Odpověď (Back)

Mějme prvočíslo \(p\) a \(n \in \mathbb Z\) takové, že \(n \geq 2\). Postup konstrukce konečného tělesa neprvočíselného řádu je následující:

- uvažme těleso \(T\) s \(p\) prvky (např. \((\mathbb Z_p, +, \cdot)\)),
- sestrojme okruh \(T[x]\) všech polynomů nad tělesem \(T\),
- nalezněme ireducibilní polynom \(p(x) \in T[x]\) stupně \(n\),
- sestrojme množinu \(F\) všech polynomů z \(T[x]\) stupně nejvýše \(n - 1\) včetně nulového polynomu,
- vybavme \(F\) operacemi sčítání polynomů v \(T[x]\) a násobení polynomů v \(T[x]\) modulo \(p(x)\).

Potom \(F\) s takto zavedenými operacemi tvoří konečné těleso řádu \(p^n\).

## Poznámka Anki 1733670394180

Karty Anki: 1733670394180
GUID: pn5nF=3,~f; štítky: ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Popište vlastnosti aditivní grupy tělesa \(GF(p^n)\).

### Odpověď (Back)

Aditivní grupa tělesa \(GF(p^n)\) má následující vlastnosti:

- její řád je \(p^n\),
- její neutrální prvek je:

\[0 = 00 \dots 0 = 0^n,\]

- inverze k prvku \(b_1b_2 \dots b_n\) je:

\[(p - b_1)(p - b_2) \dots (p - b_n),\]

- pro \(n > 1\) není cyklická.

### Doplňující pole (Extra)

Řetězec \(b_1b_2 \dots b_n\) označuje zápis koeficientů polynomu od členu s nejvyšší mocninou po člen s nejnižší mocninou.
Je však „cyklická“ v každém koeficientu členu polynomu.

## Poznámka Anki 1733670665988

Karty Anki: 1733670665988
GUID: xuaQ-yy|`=; štítky: duplicate ni-mpi::p12 ni-spol::02.

### Otázka (Front)

Popište vlastnosti multiplikativní grupy tělesa \(GF(p^n)\).

### Odpověď (Back)

Multiplikativní grupa tělesa \(GF(p^n)\) má následující vlastnosti:

- její řád je \(p^n - 1\),
- její neutrální prvek je:

\[0 = 00 \dots 1 = 0^{n - 1}1,\]

- inverzi ke každému prvku nalezneme pomocí EEA,
- je cyklická.

### Doplňující pole (Extra)

Řetězec \(b_1b_2 \dots b_n\) označuje zápis koeficientů polynomu od členu s nejvyšší mocninou po člen s nejnižší mocninou.

## Poznámka Anki 1733671025127

Karty Anki: 1733671025127
GUID: F^r[p#_ISS; štítky: ni-mpi::p12.

### Otázka (Front)

Vyslovte větu o podgrupách multiplikativní grupy tělesa \((\mathbb Z_p, +, \cdot)\).

### Odpověď (Back)

Mějme multiplikativní grupu \((\mathbb Z_p \smallsetminus \{ 0 \}, \cdot)\) tělesa \((\mathbb Z_p, +, \cdot)\), kde \(p\) je prvočíslo, a \(k \in \mathbb Z^+\). Pokud \(k \, | \, p - 1\), pak v \((\mathbb Z_p \smallsetminus \{ 0 \}, \cdot)\) existuje podgrupa řádu \(k\) a obsahuje právě ty prvky \(a \in \mathbb Z_p \smallsetminus \{ 0 \}\), pro které platí\[a^k = 1.\]

