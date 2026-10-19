# NI-VSM – Přednáška 01

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-VSM
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1739868108721

Karty Anki: 1739868108721
GUID: LFrh?EO+R8; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Vyslovte klasickou definici pravděpodobnosti.

### Odpověď (Back)

Mějme konečný počet \(n\) vzájemně různých výsledků nějakého pokusu a předpokládejme, že jsou všechny stejně pravděpodobné. Jestliže \(m\) těchto výsledků odpovídá realizaci jevu \(A\), potom definujeme pravděpodobnost jevu \(A\) jako\[\operatorname P(A) = \frac m n = \frac {\text{počet příznivých výsledků}} {\text{počet všech možných výsledků}}.\]

## Poznámka Anki 1739868154312

Karty Anki: 1739868154313
GUID: g6m1D3L[`o; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Vyslovte geometrickou definici pravděpodobnosti.

### Odpověď (Back)

Pokud výsledky nastávají v nějakém geometrickém objektu či množině \(\Omega\) konečné „velikosti“ a každý výsledek je stejně pravděpodobný, pak pravděpodobnost jevu \(A\) definujeme jako „relativní velikost“ množiny \(A\):\[\operatorname P(A) = \frac {\text{"velikost" množiny příznivých výsledků}} {\text{"velikost" množiny všech výsledků}} = \frac {\text{"velikost" } A} {\text{"velikost" } \Omega}.\]a mluvíme o rovnoměrném rozložení výsledků experimentu.

## Poznámka Anki 1739868520339

Karty Anki: 1739868520339
GUID: e*X:|_y)2~; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Definuje pravděpodobnostní prostor (experiment).

### Odpověď (Back)

Pravděpodobnostní prostor (experiment) je trojice \(\mathcal E = (\Omega, \mathcal F, \operatorname P)\), kde

- \(\Omega\) je prostor elementárních jevů (výběrový prostor),

- \(\mathcal F\) je kolekce podmnožin \(\Omega\) nazývaných náhodné jevy, kterým lze přiřadit pravděpodobnost \(\text P\);
- \(\operatorname P\) je pravděpodobnostní míra.

## Poznámka Anki 1739868680514

Karty Anki: 1739868680514
GUID: I<iM,!FHh>; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Definujte \(\sigma\)-algebru.

### Odpověď (Back)

Kolekci \(\mathcal F\) podmnožin prostoru elementárních jevů \(\Omega\) nazýváme \(\sigma\)-algebrou, jestliže jsou splněny následující podmínky:

- **obsahuje nemožný jev **- \(\emptyset \in \mathcal F\);

- **obsahuje opačný jev** - když \(A \in \mathcal F\), tak \(A^c \in \mathcal F\);
- **obsahuje spočetné sjednocení **- když \(A_1, A_2, \dots \in \mathcal F\), tak \(\displaystyle \bigcup_{i = 1}^\infty A_i \in \mathcal F\).

## Poznámka Anki 1739868894588

Karty Anki: 1739868894588
GUID: i/fv85>kiC; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Definujte pravděpodobnostní míru.

### Odpověď (Back)

Pravděpodobnostní míra na \((\Omega, \mathcal F)\) je funkce \(\operatorname P : \mathcal F \to \mathbb R\) splňující:

- **nezápornost** - pro každé \(A \in \mathcal F\) platí \(\operatorname P(A) \geq 0\),

- **normalizace **- \(\operatorname P(\Omega) = 1\),

- \(\sigma\)**-aditivita** - když jsou \(A_1, A_2, \dots \in \mathcal F\) vzájemně disjunktní jevy, tak

\[\operatorname P \Bigg( \displaystyle \bigcup_{i = 1}^\infty A_i \Bigg) = \displaystyle \sum_{i = 1}^\infty \operatorname P(A_i).\]

## Poznámka Anki 1739868977908

Karty Anki: 1739868977908
GUID: Is8n6gt<KN; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Vyslovte větu o vlastnostech pravděpodobnosti.

### Odpověď (Back)

Nechť \(A\) a \(B\) jsou náhodné jevy na pravděpodobnostním prostoru s mírou \(\operatorname P\). Pak platí:

- \(\operatorname P(\emptyset) = 0\),

- jestliže \(A\) a \(B\) jsou vzájemně disjunktní, pak \(\operatorname P(A \cup B) = \operatorname P(A) + \operatorname P(B)\),
- \(\operatorname P(A^c) = 1 - \operatorname P(A)\),

- jestliže \(A\) a \(B\) nejsou vzájmně disjunktní, pak \(\operatorname P(A \cup B) = \operatorname P(A) + \operatorname P(B) - \operatorname P(A \cap B)\),

- pokud \(A \subset B\), tak \(\operatorname P(A) \leq \operatorname P(B)\).

## Poznámka Anki 1739869010400

Karty Anki: 1739869010400
GUID: r342]_C]M9; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Definujte podmíněnou pravděpodobnost.

### Odpověď (Back)

Mějme \(A\) a \(B\) náhodné jevy, kde \(\operatorname P(B) > 0\). Podmíněnou pravděpodobnost jevu \(A\) za podmínky, že nastal jev \(B\) definujeme jako
\[\operatorname P(A|B) = \frac {\operatorname P(A \cap B)} {\operatorname P(B)}.\]Takto definovaná podmíněná pravděpodobnost \(\operatorname P( \cdot | B)\) je pravděpodobnostní mírou.

## Poznámka Anki 1739869437274

Karty Anki: 1739869437274
GUID: qrsrDjM/Hb; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Vyslovte lemma o multiplikativním zákonu (řetězovém pravidle).

### Odpověď (Back)

Pro jevy \(A_1, \dots , A_n\) splňující \(\operatorname P(A_1 \cap \dots \cap A_n ) > 0\) platí
\[\operatorname P(A_1 \cap \dots \cap A_n) = \operatorname P(A_1) \cdot \operatorname P(A_2|A_1) \cdot \operatorname P(A_3|A_1 \cap A_2) \cdots \operatorname P(A_n|A_1 \cap \dots \cap A_{n - 1}). \]

## Poznámka Anki 1739869549887

Karty Anki: 1739869549887
GUID: iG&KQ!IQVS; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Popište úplný rozklad pravděpodobnosti.

### Odpověď (Back)

Mějme prostor elementárních jevů \(\Omega\) takový, že \(\Omega = B_1 \cup B_2 \cup B_3\), kde \(B_1\), \(B_2\) a \(B_3\) jsou vzájemně disjunktní, a pozorujme jev \(A\).

 [Obrázek: paste-ed3ca23e1b8baf4283e302da627cdadb7f415a9c.jpg; soubor je v media/ v doprovodném ZIP] 

Potom s použitím podmíněné pravděpodobnosti
\[\begin{matrix}
\operatorname P(A|B_i) = \displaystyle \frac {\operatorname P(A \cap B_i)} {\operatorname P(B_i)} \\
\operatorname P(A \cap B_i) = \operatorname P(A|B_i) \cdot \operatorname P(B_i)
\end{matrix}\]dostaneme, že
\[\operatorname P(A) = \operatorname P(A|B_1) \operatorname P(B_1) + \operatorname P(A|B_2) \operatorname P(B_2) + \operatorname P(A|B_3) \operatorname P(B_3).\]Obecně:
 [Obrázek: paste-368a512c32c838133da84bba9e24c1638e35bb18.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1739869562658

Karty Anki: 1739869562658
GUID: b}]Tbp0~rT; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Popište Bayesovu větu.

### Odpověď (Back)

Mějme prostor elementárních jevů \(\Omega\) takový, že \(\Omega = B_1 \cup B_2 \cup B_3\), kde \(B_1\), \(B_2\) a \(B_3\) jsou vzájemně disjunktní, a pozorujme jev \(A\).

 [Obrázek: paste-ed3ca23e1b8baf4283e302da627cdadb7f415a9c.jpg; soubor je v media/ v doprovodném ZIP] 

Potom s použitím úplného rozkladu pravděpodobnosti
\[\operatorname P(A) = \operatorname P(A|B_1) \operatorname P(B_1) + \operatorname P(A|B_2) \operatorname P(B_2) + \operatorname P(A|B_3) \operatorname P(B_3)\]dostaneme, že
\[\text P(B_j|A) = \frac {\text P(A|B_j) \text P(B_j)} {\text P(A|B_1) \text P(B_1) + \text P(A|B_2) \text P(B_2) + \text P(A|B_3) \text P(B_3)}.\]

## Poznámka Anki 1739869963444

Karty Anki: 1739869963445
GUID: bal.5NhHZL; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Definujte nezávislost náhodných jevů.

### Odpověď (Back)

Náhodné jevy \(A\) a \(B\) se nazývají nezávislé, pokud\[\operatorname P(A \cap B) = \operatorname P(A) \cdot \operatorname P(B).\]Obecně, soubor jevů \(\{ A_i : i \in I \}\) se nazývá nezávislý, jestliže\[\operatorname P \Big( \displaystyle \bigcap_{i \in J} A_i \Big) = \displaystyle \prod_{i \in J} \operatorname P(A_i)\]pro všechny neprázdné konečné podmnožiny \(J\) indexové množiny \(I\).

## Poznámka Anki 1740063561866

Karty Anki: 1740063561866
GUID: bb~JU>${$~; štítky: duplicate ni-vsm::p01.

### Otázka (Front)

Vyslovte větu o doplňcích nezávislých jevů.

### Odpověď (Back)

Jsou-li jevy \(A\) a \(B\) nezávislé, pak jsou nezávislé i jevy \(A\) a \(B^c\).

### Doplňující pole (Extra)

Obdobně věta platí i pro \(A\) a \(B^c\) či \(A^c\) a \(B^c\).

