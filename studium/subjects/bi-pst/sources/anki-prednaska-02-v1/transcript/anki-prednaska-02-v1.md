# BI-PST – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1696412367186

Karty Anki: 1696412367186
GUID: sKBHQa+L0_; štítky: bi-pst::p02 bi-spol::26.

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
\[\operatorname P(A) = \operatorname P(A|B_1) \operatorname P(B_1) + \operatorname P(A|B_2) \operatorname P(B_2) + \operatorname P(A|B_3) \operatorname P(B_3).\]

## Poznámka Anki 1696412524277

Karty Anki: 1696412524277
GUID: f9{CRa!s6*; štítky: bi-pst::p02 bi-spol::26.

### Otázka (Front)

Popište Bayesovu větu.

### Odpověď (Back)

Mějme prostor elementárních jevů \(\Omega\) takový, že \(\Omega = B_1 \cup B_2 \cup B_3\), kde \(B_1\), \(B_2\) a \(B_3\) jsou vzájemně disjunktní, a pozorujme jev \(A\).

 [Obrázek: paste-ed3ca23e1b8baf4283e302da627cdadb7f415a9c.jpg; soubor je v media/ v doprovodném ZIP] 

Potom s použitím úplného rozkladu pravděpodobnosti
\[\operatorname P(A) = \operatorname P(A|B_1) \operatorname P(B_1) + \operatorname P(A|B_2) \operatorname P(B_2) + \operatorname P(A|B_3) \operatorname P(B_3)\]dostaneme, že
\[\text P(B_j|A) = \frac {\text P(A|B_j) \text P(B_j)} {\text P(A|B_1) \text P(B_1) + \text P(A|B_2) \text P(B_2) + \text P(A|B_3) \text P(B_3)}.\]

## Poznámka Anki 1696413261956

Karty Anki: 1696413261957
GUID: vAt}?:{&09; štítky: bi-pst::p02 bi-spol::26.

Metadata původního zdroje pro kartu 1696413261957: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte lemma o multiplikativním zákonu (řetězovém pravidle).

### Odpověď (Back)

Pro jevy \(A_1, \dots , A_n\) splňující \(\operatorname P(A_1 \cap \dots \cap A_n ) > 0\) platí
\[\operatorname P(A_1 \cap \dots \cap A_n) = \operatorname P(A_1) \cdot \operatorname P(A_2|A_1) \cdot \operatorname P(A_3|A_1 \cap A_2) \cdots \operatorname P(A_n|A_1 \cap \dots \cap A_{n - 1}). \]

## Poznámka Anki 1696414152452

Karty Anki: 1696414152452
GUID: AuE;>ebx|?; štítky: bi-pst::p02 bi-spol::26.

Metadata původního zdroje pro kartu 1696414152452: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte nezávislost náhodných jevů.

### Odpověď (Back)

Náhodné jevy \(A\) a \(B\) se nazývají nezávislé, pokud\[\operatorname P(A \cap B) = \operatorname P(A) \cdot \operatorname P(B).\]Obecně, soubor jevů \(\{ A_i : i \in I \}\) se nazývá nezávislý, jestliže\[\operatorname P \Big( \displaystyle \bigcap_{i \in J} A_i \Big) = \displaystyle \prod_{i \in J} \operatorname P(A_i)\]pro všechny neprázdné konečné podmnožiny \(J\) indexové množiny \(I\).

## Poznámka Anki 1696414922391

Karty Anki: 1696414922391
GUID: M=Nmsru#t;; štítky: bi-pst::p02 bi-spol::26.

Metadata původního zdroje pro kartu 1696414922391: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte podmíněnou nezávislost.

### Odpověď (Back)

Nechť \((\Omega, \mathcal F, \operatorname P)\) je pravděpodobnostní prostor a \(C\) je náhodný jev s \(\operatorname P(C) > 0\). Náhodné jevy \(A\) a \(B\) se nazývají podmíněně nezávislé za podmínky \(C\), pokud\[\operatorname P(A \cap B | C) = \operatorname P(A|C) \cdot \operatorname P(B|C).\]

## Poznámka Anki 1696417650274

Karty Anki: 1696417650274
GUID: hfEi-!BlWw; štítky: bi-pst::p02 bi-spol::26.

Metadata původního zdroje pro kartu 1696417650274: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte podmíněnou pravděpodobnost.

### Odpověď (Back)

Mějme \(A\) a \(B\) náhodné jevy, kde \(\operatorname P(B) > 0\). Podmíněnou pravděpodobnost jevu \(A\) za podmínky, že nastal jev \(B\) definujeme jako
\[\operatorname P(A|B) = \frac {\operatorname P(A \cap B)} {\operatorname P(B)}.\]Takto definovaná podmíněná pravděpodobnost \(\operatorname P( \cdot | B)\) je pravděpodobnostní mírou.

## Poznámka Anki 1740063548121

Karty Anki: 1740063548121
GUID: c8m%}z57O); štítky: bi-pst::p02.

Metadata původního zdroje pro kartu 1740063548121: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte větu o doplňcích nezávislých jevů.

### Odpověď (Back)

Jsou-li jevy \(A\) a \(B\) nezávislé, pak jsou nezávislé i jevy \(A\) a \(B^c\).

### Doplňující pole (Extra)

Obdobně věta platí i pro \(A^c\) a \(B\) či \(A^c\) a \(B^c\).

