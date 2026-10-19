# NI-MKY – Přednáška 04

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MKY
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1741200057148

Karty Anki: 1741200057149
GUID: IWIV)jT28*; štítky: ni-mky::c02 ni-mky::p04.

### Otázka (Front)

Definujte faktorokruh a dokažte, že se jedná o okruh.

### Odpověď (Back)

Mějme okruh \(R\) a jeho ideál \(J\). Faktorokruhem \(R\) vzhledem k ideálu \(J\) nazýváme okruh tvořený třídami rozkladu \(R\) vzhledem k \(H\) společně s operacemi\[\begin{align}
(a + J) + (b + J) &= (a + b) + J,\\
(a + J) \cdot (b + J) &= ab + J
\end{align}\]pro \(a, b \in R\) a značíme jej \(R/J\).

**Důkaz** 
Nejprve dokážeme, že operace výše je dobře definovaná. Vlastnost operace \(+\) jsou již známé z věty o faktorgrupě a víme, že operace \(+\) společně s třídami rozkladu tvoří abelovskou grupu. Korektnost operace ověříme obdobně. Mějme třídy rozkladu \([a]\) a \([b]\) a jejich další reprezentanty \(a' \in [a]\) a \(b' \in [b]\). Z toho plyne, že existují \(j_1, j_2 \in J\) taková, že\[\begin{align}
a' &= a + j_1,\\
b' &= b + j_2.
\end{align}\]a dohromady\[a'b' = (a + j_1)(b + j_2) = \underbrace{ab}_{\in R} + \underbrace{aj_2 + j_1b + j_1 j_2}_{\in J} \in [ab],\]kde \(aj_2 \in J\) a \(j_1 b \in J\), protože \(J\) je ideál, a \(j_1 j_2 \in J\), protože \(J\) je okruh. Nyní dokážeme, že třídy rozkladu společně s operací \(\cdot\) tvoří pologrupu:

- **uzavřenost** - plyne z předchozí části důkazu,

- **asociativita** - plyne z asociativity operace \(\cdot\) na \(R\).

Posledním poznatkem je, že distributivita plyne z distributivity na \(R\).

### Doplňující pole (Extra)

Výraz \(a + J\) v tomto kontextu značí třídu rozkladu prvku \(a\) tedy \([a]\).

## Poznámka Anki 1741201930906

Karty Anki: 1741201930906
GUID: nPyXaWD0!o; štítky: ni-mky::p04.

### Otázka (Front)

Vyslovte a dokažte větu o faktorokruhu vzhledem k hlavnímu ideálu generovanému prvočíslem.

### Odpověď (Back)

Faktorokruh \(\mathbb Z/(p)\), kde \(p\) je prvočíslo, je těleso.

**Důkaz** 
Víme, že faktorokruh \(\mathbb Z/(p)\) je konečným komutativním okruhem s jedničkou \([1]\). Díky větě o vztahu těles a oborů integrity stačí dokázat, že \(\mathbb Z/(p)\) nemá triviální dělitele nuly. Pro spor předpokládejme, že existují \([a], [b] \in \mathbb Z/(p)\) taková, že\[[a] \cdot [b] = [ab] = 0.\]To může nastat pouze v případě, že existuje \(k \in \mathbb Z\) takové,  že\[ab = k \cdot p.\]Protože \(p\) je prvočíslo a \(p | ab\), tak musí \(p\) dělit aspoň jedno z \(a\) a \(b\), tedy buď \([a] = 0\) nebo \([b] = 0\).

## Poznámka Anki 1741202162033

Karty Anki: 1741202162033
GUID: O:>6oj>Y3u; štítky: ni-mky::c02 ni-mky::p04.

### Otázka (Front)

Definujte prvoideál.

### Odpověď (Back)

Mějme ideál \(J\) komutativního okruhu \(R\) takový, že \(J \neq R\). Ideál \(J\) je prvoideálem \(R\) právě tehdy, když pro všechna \(a, b \in R\) platí\[ab \in J \Rightarrow a \in J \lor b \in J.\]

## Poznámka Anki 1741202319548

Karty Anki: 1741202319548
GUID: i+KKpw[Fj,; štítky: ni-mky::c02 ni-mky::p04.

### Otázka (Front)

Definujte maximální ideál.

### Odpověď (Back)

Mějme ideál \(J\) okruhu \(R\) takový, že \(J \neq R\). Ideál \(J\) je maximálním ideálem \(R\), pokud každý ideál \(I\) splňující \(J \subset I\) je roven buď \(J\) nebo \(R\).

## Poznámka Anki 1741202353006

Karty Anki: 1741202353006
GUID: h*VMcccDg]; štítky: ni-mky::c02 ni-mky::p04.

### Otázka (Front)

Definujte obor hlavních ideálů.

### Odpověď (Back)

Okruh \(R\) nazvýváme oborem hlavních ideálů, pokud \(R\) je oborem integrity a každý ideál \(J\) okruhu \(R\) je hlavní.

## Poznámka Anki 1741202595577

Karty Anki: 1741202595577
GUID: Jr/1[U|E9_; štítky: ni-mky::p04.

### Otázka (Front)

Vyslovte větu o provideálech a maximálních ideálech.

### Odpověď (Back)

Mějme komutativní okruh s jedničkou \(R\). Potom: 

- ideál \(J\) okruhu \(R\) je jeho prvoideálem právě tehdy, když je faktorokruh \(R/P\) oborem integrity;
- ideál \(J\) okruhu \(R\) je jeho maximálním ideálem právě tehdy, když je faktorokruh \(R/J\) tělesem;
- každý maximální ideál okruhu \(R\) je prvoideál.

## Poznámka Anki 1741202708108

Karty Anki: 1741202708108
GUID: g^$Fix0|X%; štítky: ni-mky::p04.

### Otázka (Front)

Vyslovte větu o oborech hlavních ideálů.

### Odpověď (Back)

Mějme komutativní okruh s jedničkou \(R\), který je oborem hlavních ideálů. Potom \(R/(c)\) je těleso právě tehdy, když \(c\) je prvoelement okruhu \(R\).

## Poznámka Anki 1741206184598

Karty Anki: 1741206184598
GUID: t/+m^}$WBy; štítky: duplicate ni-mky::p04.

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

## Poznámka Anki 1741207092210

Karty Anki: 1741207092210
GUID: hn!.pn%q1%; štítky: ni-mky::c02 ni-mky::p04.

### Otázka (Front)

Vyslovte větu o homomorfismu pro okruhy.

### Odpověď (Back)

Mějme epimorfismus \(f : R \to R'\) okruhu \(R\) na okruh \(R'\). Potom \(\ker f\) je ideál \(R\) a \(R'\) je izomorfní faktorokruhu \(R/\ker f\). Naopak, je-li \(J\) ideál okruhu \(R\), pak zobrazení \(\psi : R \to R/J\) definované předpisem\[\psi(a) = a + J\]pro \(a \in R\) je homomorfismem \(R\) a \(R/J\), přičemž \(\ker \psi = J\).

### Doplňující pole (Extra)

Epimorfismus je homomorfismus, který je surjektivní.

## Poznámka Anki 1741207594082

Karty Anki: 1741207594082
GUID: D=KSXuH6Pg; štítky: ni-mky::p04.

### Otázka (Front)

Vyslovte větu o izomorfismu mezi faktorokruhem vzhledem k hlavnímu ideálu generovanému prvočíslem a Galoisovým tělesm.

### Odpověď (Back)

Tělese \(\mathbb Z/(p)\), kde \(p\) je prvočíslo, je izomorfní Galoisovu tělesu \(GF(p)\).

## Poznámka Anki 1741207729449

Karty Anki: 1741207729449
GUID: fZG+d#]JJ4; štítky: ni-mky::p04.

### Otázka (Front)

Definujte charakteristiku okruhu.

### Odpověď (Back)

Mějme okruh \(R\) a \(a \in R\). Pokud existuje \(n \in \mathbb N\) splňující\[na = 0,\]pak nejmenší takové \(n\) nazýváme charakteristikou okruhu \(R\) a říkáme, že \(R \) má kladnou charakteristiku. Pokud takové \(n\) neexistuje, je charakteristika okruhu \(R\) rovna \(0\).

## Poznámka Anki 1741210605565

Karty Anki: 1741210605565
GUID: t(<IHvTJl7; štítky: ni-mky::p04.

### Otázka (Front)

Vyslovte a dokažte větu o charakteristice okruhu.

### Odpověď (Back)

Charakteristika okruhu s jedničkou \(R \neq \{ 0 \}\), který má kladnou charakteristiku a neobsahuje netriviální dělitele nuly, je prvočíslo.

**Důkaz** 
Z předpokladu víme, že \(R\) obsahuje nenulové prvky a pro jeho charakteristiku \(n\) musí tedy platit \(n \geq 2\). Pro spor předpokládejme, že \(n\) není prvočíslo, tedy že existuje \(m \in \mathbb Z\) takové, že\[n = km,\]kde \(1 < k < n\) a \(1 < m < n\). Potom platí\[0 = n \cdot 1 = (k \cdot m) \cdot 1 = (k \cdot 1)(m \cdot 1).\]Protože dle předpokladu neexistují v \(R\) netriviální dělitelé nuly, musí \(k \cdot 1 = 0\) nebo \(m \cdot 1 = 0\). Pro libovolné \(b \in R\) pak ale máme\[k \cdot r = (k \cdot 1) \cdot r = 0\]nebo případně obdobně pro \(m\). Protože však \(k < n\) resp. \(m < n\) dostáváme spor s definicí charakteristiky, která má být nejmenším přirozeným číslem s touto vlastností.

## Poznámka Anki 1741211949590

Karty Anki: 1741211949590
GUID: M-K28NH(nw; štítky: ni-mky::p04.

### Otázka (Front)

Vyslovte a dokažte větu o charakteristice konečného tělesa.

### Odpověď (Back)

Konečné těleso má prvočíselnou charakteristiku.

**Důkaz** 
Důkaz plyne z věty o charakterstice okruhu. Pro její použití však musíme dokázat, že je charakteristika tělesa nenulová. Mějme tedy těleso \(T = (M, +, \cdot)\). Podle věty o vztahu řádu grupy a neutrálního prvku (zde akorát v aditivní notaci) v \((M, +)\) platí\[\#T \cdot 1 = 0\]a \(T\) má proto konečnou charakteristiku.

### Doplňující pole (Extra)

Neplatí však, že \(\#T\) je nutně charakteristikou \(T\), ta totiž může být menší. S jistotou však víme, že musí být konečná.

