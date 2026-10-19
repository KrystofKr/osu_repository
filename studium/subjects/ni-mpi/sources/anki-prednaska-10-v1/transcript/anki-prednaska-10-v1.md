# NI-MPI – Přednáška 10

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1731961747759

Karty Anki: 1731961747759
GUID: A9L|>ja+*r; štítky: duplicate ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Definujte podgrupu (subgroup).

### Odpověď (Back)

Mějme grupu \(G = (M, \circ)\). Podgrupou (subgroup) grupy \(G\) nazveme libovolnou dvojici \(H = (N, \circ)\) takovou, že

- \(N \subseteq M\) je neprázdná množina,

- \((N, \circ)\) je grupa.

## Poznámka Anki 1731962728397

Karty Anki: 1731962728397
GUID: t|A24uZ+$]; štítky: ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Vyslovte větu o kritériu pro podgrupy.

### Odpověď (Back)

Mějme grupu \(G = (M, \circ)\) a neprázdnou množinu \(N \subseteq M\). Dvojice \(H = (N, \circ)\) je podgrupa \(G\), právě když pro každé \(a, b \in N\) platí
\[a \circ b^{-1} \in N.\]

## Poznámka Anki 1731962879840

Karty Anki: 1731962879840
GUID: yBchdla>P.; štítky: duplicate ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Definujte řád (order) grupy, konečnou a nekonečnou grupu.

### Odpověď (Back)

**Řádem grupy** \(G = (M, \circ)\) nazýváme počet prvků množiny \(M\) a značíme \(\#G\). Je-li \(M\) nekonečná množina, je její řád nekonečno a o \(G\) říkáme, že je **nekonečná**. V opačném případě nazýváme \(G\) **konečnou grupou**.

## Poznámka Anki 1731963162209

Karty Anki: 1731963162209
GUID: u,@Q&-^IjH; štítky: ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Vyslovte Lagrangeovu větu (větu o řádu grupy).

### Odpověď (Back)

Mějme podgrupu \(H\) konečné grupy \(G\). Potom řád \(H\) je dělitelem řádu \(G\).

## Poznámka Anki 1731964272182

Karty Anki: 1731964272182
GUID: bJ4m_[.5GJ; štítky: ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Vyslovte větu o podgrupě generované množinou.

### Odpověď (Back)

Mějme grupu \(G = (M, \circ)\) a neprázdnou množinu \(N \subseteq M\). Pak platí, že množina\[\langle N \rangle := \bigcap \{ H : H \text{ je podgrupa grupy } G \text{ obsahující } N \}\]je podgrupa grupy \(G\) obsahující \(N\).

## Poznámka Anki 1731964543820

Karty Anki: 1731964543820
GUID: 1Miyi,ZsJ; štítky: ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Definujte podgrupu generovanou množinou, generující množinu a generátor.

### Odpověď (Back)

Mějme grupu \(G = (M, \circ)\) a neprázdnou množinu \(N \subseteq M\). Podgrupu \(\langle N \rangle\) grupy \(G\) nazýváme **podgrupou generovanou množinou** \(N\) a \(N\) **generující množinou** grupy \(\langle N \rangle\). Je-li \(N\) jednoprvková množina obsahující prvek \(a\), pak o \(a\) mluvíme jako o **generátoru grupy **\(\langle \{ a \} \rangle := \langle a \rangle\).

## Poznámka Anki 1731964740310

Karty Anki: 1731964740310
GUID: d[0]i+e$S#; štítky: ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Vyslovte větu o „grupovém obalu.“

### Odpověď (Back)

Mějme grupu \(G = (M, \circ)\) a neprázdnou množinu \(N \subseteq M\). Potom všechny prvky patřící do \(\langle N \rangle\) lze získat pomocí „grupového obalu“
\[\langle N \rangle = \big \{ a_1^{k_1} \circ a_2^{k_2} \circ \dots \circ a_n^{k_n} : n \in \mathbb N, k_i \in \mathbb Z, a_i \in N \big \}.\]

### Doplňující pole (Extra)

Pro jednoprvkovou \(N\) se „grupový obal“ zredukuje na
\[\langle a \rangle = \big \{ a^k : k \in \mathbb Z \big \}.\]

## Poznámka Anki 1732564063282

Karty Anki: 1732564063282
GUID: l:yvXvS.DF; štítky: duplicate ni-mpi::p10.

### Otázka (Front)

Definujte cyklickou grupu (cyclic group) a generátor cyklické grupy.

### Odpověď (Back)

Grupa \(G = (M, \circ)\) se nazývá **cyklická**, pokud existuje prvek \(a \in M\) takový, že \(\langle a \rangle = G\). Tomuto prvku říkáme **generátor cyklické grupy** \(G\).

### Doplňující pole (Extra)

Všechny prvky patřící do \(\langle a \rangle\) získáme pomocí „grupového obalu:“\[\langle a \rangle = \{ a \circ a \circ \cdots \circ a = a^k : k \in \mathbb Z \}.\]

## Poznámka Anki 1732565192862

Karty Anki: 1732565192862
GUID: ipRf:q/FnQ; štítky: duplicate ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Definujte řád prvku grupy a popište jeho vztah k řádu grupy.

### Odpověď (Back)

Mějme grupu \(G = (M, \circ)\) a \(a \in M\). Pokud existuje \(m \in \mathbb Z^+\) splňující\[a^m = e,\]pak nejmenší takové \(m\) nazýváme řádem prvku** **\(a\) a značíme jej \(\operatorname{ord} a\). Pokud takové \(m\) neexistuje, je řád prvku \(a\) nekonečno. Pro grupu \(\langle a \rangle\) platí, že\[\operatorname{ord} a = \# \langle a \rangle.\]

## Poznámka Anki 1732565478764

Karty Anki: 1732565478764
GUID: u[4/x,f~tp; štítky: ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Vyslovte větu o cykličnosti grupy \(\mathbb Z_n^\times\).

### Odpověď (Back)

Grupa \(\mathbb Z_n^\times\) je cyklická, právě když \(n\) je \(2\), \(4\), \(p^k\) nebo \(2p^k\), kde \(p\) je liché prvočíslo a \(k \in \mathbb Z^+\).

## Poznámka Anki 1732566138953

Karty Anki: 1732566138953
GUID: zOtfGio<0p; štítky: ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Vyslovte větu o mocnině generátoru grupy.

### Odpověď (Back)

Mějme cyklickou grupu \(G = (M, \circ)\) řádu \(n\) a \(a \in M\) nějaký její generátor. Potom \(a^k\) je také generátor \(G\) právě tehdy, když \(\gcd(k, n) = 1\).

## Poznámka Anki 1732566179196

Karty Anki: 1732566179196
GUID: ihL]F`n:Fa; štítky: ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Vyslovte větu o počtu generátorů cyklické grupy.

### Odpověď (Back)

Počet generátorů cyklické grupy řádu \(n\) je roven \(\varphi(n)\).

## Poznámka Anki 1732566683673

Karty Anki: 1732566683673
GUID: k}U&BPfhhM; štítky: ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Vyslovte větu o podgrupě cyklické grupy.

### Odpověď (Back)

Libovolná podgrupa cyklické grupy je opět cyklická grupa.

## Poznámka Anki 1732567055466

Karty Anki: 1732567055466
GUID: hdyVXKjDF;; štítky: duplicate ni-mpi::p10 ni-spol::01.

### Otázka (Front)

Vyslovte a dokažte větu o vztahu řádu grupy a neutrálního prvku.

### Odpověď (Back)

Mějme grupu \(G = (M, \circ)\) řádu \(n\). Pro všechny prvky \(a \in M\) platí, že
\[a^n = e,\]kde \(e \) je neutrální prvek.

**Důkaz** 
Víme, že grupa \(\langle a \rangle \) je podgrupou grupy \(G\). Dle Lagrangeovy věty o řádu grupy platí, že \(\# \langle a \rangle\) dělí \(n\) a dostáváme
\[a^n = a^{k \cdot \# \langle a \rangle} = (a^{\# \langle a \rangle})^k = (a^{\operatorname{ord} a})^k = e^k = e.\]

### Doplňující pole (Extra)

Z této věty vyplývá Malá Fermatova věta a Eulerova věta.

