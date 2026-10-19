# NI-MKY – Přednáška 03

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MKY
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1740523004825

Karty Anki: 1740523004825
GUID: Mxj1f1>{-C; štítky: duplicate ni-mky::p03.

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

## Poznámka Anki 1740523317898

Karty Anki: 1740523317898
GUID: u`i>=<3A94; štítky: duplicate ni-mky::p03 ni-mky::p05.

### Otázka (Front)

Definujte polynom nad okruhem.

### Odpověď (Back)

Mějme okruh \(R\) a \(a_i \in R\) pro \(i = 0, 1, \dots n\). Polynomem nad okruhem \(R\) s formální proměnnou \(x\) nazýváme formální výraz\[P(x) = \displaystyle \sum_{i = 0}^n a_i x^i.\]

## Poznámka Anki 1740523342713

Karty Anki: 1740523342713
GUID: I~dHT=j)pI; štítky: duplicate ni-mky::p03 ni-mky::p05.

### Otázka (Front)

Definujte okruh polynomů (polynomial ring).

### Odpověď (Back)

Mějme okruh \(R\). Potom množina všech polynomů nad okruhem \(R\) spolu s operacemi sčítání a násobení polynomů definovanými předpisy\[\begin{matrix}
\displaystyle \sum_{i = 0}^n a_i x^i + \displaystyle \sum_{i = 0}^n b_i x^i := \displaystyle \sum_{i = 0}^n (a_i + b_i) x^i,\\
\bigg( \displaystyle \sum_{i = 0}^n a_i x^i  \bigg) \cdot \bigg( \displaystyle \sum_{i = 0}^m b_i x^i \bigg) := \displaystyle \sum_{i = 0}^{n + m} \bigg( \displaystyle \sum_{j + k = i} a_j b_k \bigg) x^i,
\end{matrix}\]kde \(a_i, b_i \in R\) pro všechna \(i\), tvoří okruh polynomů nad okruhem \(R\), který značíme \(R[x]\).

## Poznámka Anki 1740523482848

Karty Anki: 1740523482848
GUID: Rh!whgukLO; štítky: ni-mky::p03.

### Otázka (Front)

Definujte okruh s jedničkou.

### Odpověď (Back)

Okruh \((M, +, \cdot)\) nazýváme okruhem s jedničkou, pokud v něm existuje neutrální prvek vůči operaci násobení , tedy  \((M, \cdot)\) je monoid. Takový prvek pak značíme \(1\).

## Poznámka Anki 1740523538950

Karty Anki: 1740523538950
GUID: tw_~Ni=plE; štítky: ni-mky::c02 ni-mky::p03.

### Otázka (Front)

Definujte okruh s dělením.

### Odpověď (Back)

Okruh \((M, +, \cdot)\) nazýváme okruhem s dělením, pokud \((M \smallsetminus \{ 0 \}, \cdot)\) je grupa.

## Poznámka Anki 1740523588676

Karty Anki: 1740523588676
GUID: r|#RNL[S-i; štítky: duplicate ni-mky::p03.

### Otázka (Front)

Definujte dělitele nuly a obor integrity (integral domain).

### Odpověď (Back)

Mějme okruh \((M, +, \cdot)\). Nenulové prvky \(a, b \in M\) nazýváme **dělitelé nuly**, právě když\[a \cdot b = b \cdot a = 0.\]**Obor integrity **(integral domain) je potom komutativní okruh, ve kterém neexistují dělitelé nuly.

### Doplňující pole (Extra)

**V předmětu NI-MKY** je obor integrity definován jako komutativní okruh s jedničkou, kde \(1 \neq 0\) a neexistují dělitelé nuly. To vychází z toho, že NI-MKY definuje okruh tak, že \((M, \cdot)\) je pologrupa. V případě, že \(a \neq 0\) a \(b \neq 0\), se pro \(a\) a \(b\) v NI-MKY používá označení netriviální dělitelé nuly, což odpovídá dělitelům nuly z NI-MPI.

## Poznámka Anki 1740561782139

Karty Anki: 1740561782139
GUID: ectf1p,|Ao; štítky: duplicate ni-mky::p03.

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

## Poznámka Anki 1740562362139

Karty Anki: 1740562362139
GUID: bX,XAM1jt1; štítky: ni-mky::p03.

### Otázka (Front)

Vyslovte a dokažte větu o vztahu těles a oborů integrity.

### Odpověď (Back)

Každé těleso je oborem integrity.

**Důkaz** 
Mějme těleso \(T = (M, +, \cdot)\) a  \(a, b \in M\) splňující\[a \cdot b = 0.\]Předpokládejme nyní, že \(a \neq 0\) (pro \(b \neq 0\) je důkaz obdobný). Potom existuje \(a^{-1} \neq 0 \in M\) a dostáváme\[\begin{align}
a^{-1} \cdot (a \cdot b) &= a^{-1} \cdot 0\\
(a^{-1} \cdot a) \cdot b &= 0\\
1 \cdot b &= 0\\
b &= 0
\end{align}\]Z toho plyne, že pokud je jeden z prvků \(a\) a \(b\) nenulový, tak druhý je nutně nulový. V \(T\) tedy neexistují netriviální dělitelé nuly a proto je \(T\) oborem integrity.

## Poznámka Anki 1740563022059

Karty Anki: 1740563022059
GUID: lm>C~tEgHb; štítky: ni-mky::p03.

### Otázka (Front)

Vyslovte a dokažte větu o konečných oborech integrity.

### Odpověď (Back)

Každý konečný obor integrity je tělesem.

**Důkaz** 
Mějme konečný obor integrity \(R = (M, +, \cdot)\). Ověříme, že \((M \smallsetminus \{ 0 \}, \cdot)\) je abelovská grupa. Uzavřenost, asociativita, existence neutrálního prvku a komutativita jsou splněny z definice oboru integrity. Zbývá tedy dokázat existenci inverzních prvků. Předpokládejme, \[R = \{ a_1, a_2, \dots, a_n \}.\]Dále mějme \(a \neq 0 \in M\) a množinu součinů\[R' = \{ a a_1, a a_2, \dots, a a_n \}.\]V této množině se žádné dva prvky nerovnají. Pokud by totiž platilo\[a a_i = a a_j, \quad i \neq j,\]pak\[\begin{align}
a a_i - a a_j &= 0\\
a (a_i - a_j) &= 0
\end{align}\]a protože \(a \neq 0\) a \(R\) je obor integrity, tak musí nutně platit \(a_i = a_j\). Z toho plyne, že \(R = R'\), tedy každý prvek \(R\) je součinem \(a a_i\). Speciálně pak\[1 = a a_j\]pro \(j \in \hat n\) a díky komutativitě\[1 = a_j a,\]což znamená, že \(a_j \) je inverzním prvkem k \(a\).

## Poznámka Anki 1740663987090

Karty Anki: 1740663987091
GUID: y!w;3z&?c{; štítky: ni-mky::c02 ni-mky::p03.

### Otázka (Front)

Definujte podokruh (subring).

### Odpověď (Back)

Podmnožinu \(S\) okruhu \(R = (M, +, \cdot)\) nazýváme podokruhem okruhu \(R\), pokud \(S\) společně s operacemi \(+\) a \(\cdot\) tvoří okruh.

## Poznámka Anki 1740664151613

Karty Anki: 1740664151613
GUID: A4H#_Q4PA*; štítky: ni-mky::c02 ni-mky::p03.

### Otázka (Front)

Definujte ideál (ideal).

### Odpověď (Back)

Podmnožinu \(J\) okruhu \(R\) nazýváme ideálem okruhu \(R\), pokud je \(J\) podokruhem okruhu \(R\)  a platí\[ab \in J \quad \text{a} \quad ba \in J\]pro kažadé \(a \in J\) a \(b \in R\).

## Poznámka Anki 1740664856007

Karty Anki: 1740664856007
GUID: M/P):syrfN; štítky: ni-mky::c02 ni-mky::p03.

### Otázka (Front)

Definujte hlavní ideál.

### Odpověď (Back)

Mějme komutativní okruh \(R\). Nejmenší ideál okruhu \(R\) obsahující prvek \(a \in R\) značíme \((a)\) a definujeme následovně:\[(a) = \displaystyle \bigcap \{ J : J \text{ je ideál okruhu R obsaující } a \}.\]Ideál \(J\) okruhu \(R\) se nazývá hlavním ideálem, pokud existuje \(a \in R\) splňující\[J = (a).\]Pak říkáme, že \(J\) je generovaný prvkem \(a\).

## Poznámka Anki 1740666728693

Karty Anki: 1740666728693
GUID: f+Py=q5LzI; štítky: ni-mky::p03.

### Otázka (Front)

Vyslovte a dokažte větu o hlavním ideálu komutativního okruhu.

### Odpověď (Back)

Mějme komutativní okruh \(R\) a \(a \in R\). Potom\[(a) = \{ ra + na \mid r \in R, n \in \mathbb Z \}.\]Pokud navíc \(R\) obsahuje jedničku, pak\[(a) = \{ ra \mid r \in R \}.\]
**Důkaz** 
Nejprve dokážeme, že \( M = \{ ra + na \mid r \in R, n \in \mathbb Z \}\) obsahuje \(a\). Stačí zvolit např. \(r = 0\) a \(n = 1\), čímž dostaneme\[0 \cdot a + 1 \cdot a = a \in M.\]Nyní dokažme, že \((M, +, \cdot)\) splňuje definici okruhu. \((M, +)\) tedy musí být abelovská grupa:

- **uzavřenost** - mějme \(r, s \in R\) a \(n, m \in \mathbb Z\):\[(r a + n a) + (s a + m a) = \underbrace{(r + s)}_{\in R}a + \underbrace{(n + m)}_{\in \mathbb Z}a;\]
- **asociativita** - plyne z asociativity operace \(+\) na \(R\);
- **existence neutrálního prvku** - mějme \(a \in R\):\[0 \cdot a + 0 \cdot a = 0 \in M\]

- **existence inverzních prvků** - inverzním prvkem k \(r a + n a \in R\) je\[(-r) a + (-n) a \in R,\]protože \(R\) je okruh a tedy \(-r \in R\);
- **komutativita** - plyne z komutativity operace \(+\) na \(R\).

Dále musí být \((M, \cdot)\) pologrupa:

- **uzavřenost** - mějme \(r, s \in R\) a \(n, m \in \mathbb Z\):\[(r a + n a) \cdot (s a + m a) = \underbrace{(ras + mra + nas + nma)}_{\in R}a + \underbrace{0}_{\in \mathbb Z} \cdot a \in M\]

- **asociativita** - plyne z asociativity operace \(\cdot\) na \(R\).

Pro splnění definice okruhu chybí už jen distributivní zákon, který plyne z platnosti distributivního zákonu na \(R\). Zbývá ověřit, že \((M, +, \cdot)\) je ideálem \(R\):

\[(r a + n a)s = s(r a + n a) = \underbrace{(sr + ns)}_{\in R}a + \underbrace{0}_{\in \mathbb Z} \cdot a \in M,\]kde \(s \in R\) a používáme komutativitu operací \(+\) i \(\cdot\) na \(R\). Z definice ideálu \((a)\) pak plyne inkluze \((a) \subset M\). Protože je ale \((a)\) ideál okruhu 

\(R\) obsahující \(a\), musí pro každé \(r a + n a \in M\) platit také\[r a + n a \in (a),\]z čehož plyne i inkluze \(M \subset (a)\) a tedy \((a) = M\). Pro okruh s jedničkou pak postačí\[r a + n a = r a + (n \cdot 1 ) a = \underbrace{(r + n \cdot 1)}_{\in R}a.\]

## Poznámka Anki 1741202902295

Karty Anki: 1741202902295
GUID: j-!f6n%+*z; štítky: ni-mky::p03.

### Otázka (Front)

Definujte dělitele, jednotku, přidružené prvky a prvoelement na oboru integrity.

### Odpověď (Back)

Mějme obor integrity \(R\). Prvek \(a \in R\) nazýváme **dělitelem **prvku \(b \in R\), pokud existuje \(c \in R\) splňující\[b = ac.\]Prvek \(a\) nazveme **jednotkou**, dělí-li jedničku. Dále nazveme prvky \(a\) a \(b\) přidružené, pokud existuje jednotka \(j \in R\) taková, že\[b = aj.\]Prvek \(a\) nazveme **prvoelementem**, pokud není jednotkou a mezi jeho dělitele patří pouze jednotky a prvky přidružené k \(a\).

