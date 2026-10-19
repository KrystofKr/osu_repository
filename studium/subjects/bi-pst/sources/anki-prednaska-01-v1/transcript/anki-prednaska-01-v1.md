# BI-PST – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1695806941884

Karty Anki: 1695806941884
GUID: F3nN[)tsI!; štítky: bi-pst::p01 bi-spol::26.

Metadata původního zdroje pro kartu 1695806941884: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte klasickou definici pravděpodobnosti.

### Odpověď (Back)

Mějme konečný počet \(n\) vzájemně různých výsledků nějakého pokusu a předpokládejme, že jsou všechny stejně pravděpodobné. Jestliže \(m\) těchto výsledků odpovídá realizaci jevu \(A\), potom definujeme pravděpodobnost jevu \(A\) jako\[\operatorname P(A) = \frac m n = \frac {\text{počet příznivých výsledků}} {\text{počet všech možných výsledků}}.\]

## Poznámka Anki 1695808566114

Karty Anki: 1695808566115
GUID: P0GIM;OEm-; štítky: bi-pst::p01 bi-spol::26.

Metadata původního zdroje pro kartu 1695808566115: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Vyslovte geometrickou definici pravděpodobnosti.

### Odpověď (Back)

Pokud výsledky nastávají v nějakém geometrickém objektu či množině \(\Omega\) konečné „velikosti“ a každý výsledek je stejně pravděpodobný, pak pravděpodobnost jevu \(A\) definujeme jako „relativní velikost“ množiny \(A\):\[\operatorname P(A) = \frac {\text{"velikost" množiny příznivých výsledků}} {\text{"velikost" množiny všech výsledků}} = \frac {\text{"velikost" } A} {\text{"velikost" } \Omega}.\]a mluvíme o rovnoměrném rozložení výsledků experimentu.

## Poznámka Anki 1695809888478

Karty Anki: 1695809888478
GUID: oZ&4F<oEw); štítky: bi-pst::p01 bi-spol::26.

Metadata původního zdroje pro kartu 1695809888478: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definuje pravděpodobnostní prostor (experiment).

### Odpověď (Back)

Pravděpodobnostní prostor (experiment) je trojice \(\mathcal E = (\Omega, \mathcal F, \operatorname P)\), kde

- \(\Omega\) je prostor elementárních jevů (výběrový prostor),

- \(\mathcal F\) je kolekce podmnožin \(\Omega\) nazývaných náhodné jevy, kterým lze přiřadit pravděpodobnost \(\text P\);
- \(\operatorname P\) je pravděpodobnostní míra.

## Poznámka Anki 1695810450803

Karty Anki: 1695810450803
GUID: O*{Ur>^+{9; štítky: bi-pst::p01 bi-spol::26.

Metadata původního zdroje pro kartu 1695810450803: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte \(\sigma\)-algebru.

### Odpověď (Back)

Kolekci \(\mathcal F\) podmnožin prostoru elementárních jevů \(\Omega\) nazýváme \(\sigma\)-algebrou, jestliže jsou splněny následující podmínky:

- **obsahuje nemožný jev **- \(\emptyset \in \mathcal F\);

- **obsahuje opačný jev** - když \(A \in \mathcal F\), tak \(A^c \in \mathcal F\);
- **obsahuje spočetné sjednocení **- když \(A_1, A_2, \dots \in \mathcal F\), tak \(\displaystyle \bigcup_{i = 1}^\infty A_i \in \mathcal F\).

## Poznámka Anki 1695813009800

Karty Anki: 1695813009800
GUID: L~MCKHxVv_; štítky: bi-pst::p01 bi-spol::26.

### Otázka (Front)

Definujte pravděpodobnostní míru.

### Odpověď (Back)

Pravděpodobnostní míra na \((\Omega, \mathcal F)\) je funkce \(\operatorname P : \mathcal F \to \mathbb R\) splňující:

- **nezápornost** - pro každé \(A \in \mathcal F\) platí \(\operatorname P(A) \geq 0\),

- **normalizace **- \(\operatorname P(\Omega) = 1\),

- \(\sigma\)**-aditivita** - když jsou \(A_1, A_2, \dots \in \mathcal F\) vzájemně disjunktní jevy, tak

\[\operatorname P \Bigg( \displaystyle \bigcup_{i = 1}^\infty A_i \Bigg) = \displaystyle \sum_{i = 1}^\infty \operatorname P(A_i).\]

## Poznámka Anki 1695813164764

Karty Anki: 1695813164764
GUID: DEctbB=@#z; štítky: bi-pst::p01 bi-spol::26.

### Otázka (Front)

Vyslovte větu o vlastnostech pravděpodobnosti.

### Odpověď (Back)

Nechť \(A\) a \(B\) jsou náhodné jevy na pravděpodobnostním prostoru s mírou \(\operatorname P\). Pak platí:

- \(\operatorname P(\emptyset) = 0\),

- jestliže \(A\) a \(B\) jsou vzájemně disjunktní, pak \(\operatorname P(A \cup B) = \operatorname P(A) + \operatorname P(B)\),
- \(\operatorname P(A^c) = 1 - \operatorname P(A)\),

- jestliže \(A\) a \(B\) nejsou vzájmně disjunktní, pak \(\operatorname P(A \cup B) = \operatorname P(A) + \operatorname P(B) - \operatorname P(A \cap B)\),

- pokud \(A \subset B\), tak \(\operatorname P(A) \leq \operatorname P(B)\).

## Poznámka Anki 1695813364581

Karty Anki: 1695813364581
GUID: dw9JB_:MS-; štítky: bi-pst::p01 bi-spol::26.

### Otázka (Front)

Vyslovte větu o spojitosti pravděpodobnosti.

### Odpověď (Back)

Nechť \(A_1, A_2, \dots\) je posloupnost náhodných jevů rostoucí ve smyslu inkluze, tj. \(A_1 \subset A_2 \subset A_3 \subset \dots\), označme
\[A = \displaystyle \bigcup_{i = 1}^\infty A_i,\]pak platí \(\operatorname P(A) = \displaystyle \lim_{i \to \infty} \text P(A_i)\).
Obdobně nechť \(B_1, B_2 \dots\) je posloupnost náhodných jevů klesající ve smyslu inkluze, tj. \(B_1 \supset B_2 \supset B_3 \supset \dots\), označme
\[B = \displaystyle \bigcap_{i = 1}^\infty B_i,\]pak platí \(\operatorname P(B) = \displaystyle \lim_{i \to \infty} \operatorname P(B_i)\).

