# BI-PST – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1697015398933

Karty Anki: 1697015398933
GUID: uINi7=URJ~; štítky: bi-pst::p03 bi-spol::26.

Metadata původního zdroje pro kartu 1697015398933: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte náhodnou veličinu.

### Odpověď (Back)

Náhodná veličina \(X\) na pravděpodobnostním prostoru \((\Omega, \mathcal F, \operatorname P)\) je zobrazení \(X : \Omega \to \mathbb R\), které každému výsledku experimentu \(\omega \in \Omega\) přiřadí hodnotu \(X(\omega) \in \mathbb R\) a pro které platí podmínka měritelnosti:\[\{ X \leq x \} = \{ \omega \in \Omega \mid X(\omega) \in (-\infty, x \rangle \}\in \mathcal F, \quad \forall x \in \mathbb R.\]

## Poznámka Anki 1697015642841

Karty Anki: 1697015642842
GUID: zJ(H_4WKkM; štítky: bi-pst::p03 bi-spol::26.

Metadata původního zdroje pro kartu 1697015642842: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte distribuční funkci.

### Odpověď (Back)

Distribuční funkce náhodné veličiny \(X\) je funkce \(F_X: \mathbb R \to \langle 0, 1 \rangle\) definovaná vztahem\[F_X(x) = \operatorname P(X \leq x), \quad \forall x \in \mathbb R.\]Distribuční funkce jednoznačně určuje pravděpodobnostní rozdělení náhodné veličiny.

## Poznámka Anki 1697017283252

Karty Anki: 1697017283252
GUID: k?!X1VS?,#; štítky: bi-pst::p03.

### Otázka (Front)

Vyslovte lemma o použití distribuční funkce.

### Odpověď (Back)

Pomocí distribuční funkce \(F\) náhodné veličiny \(X\) můžeme vyjádřit:

- \(\operatorname P(X > x) = 1 - F(x)\),

- \(\operatorname P(X \in (x, y \rangle) = \operatorname P(x < X \leq y) = F(y) - F(x)\),

- \(\operatorname P(X < x) = \displaystyle \lim_{y \to x-} F(y)\),

- \(\operatorname P(X = x) = F(x) - \displaystyle \lim_{y \to x-} F(y)\).

## Poznámka Anki 1697017653149

Karty Anki: 1697017653149
GUID: Lcy{vr)|,*; štítky: bi-pst::p03.

Metadata původního zdroje pro kartu 1697017653149: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte diskrétní náhodnou veličinu.

### Odpověď (Back)

Náhodná veličina \(X\) se nazývá diskrétní, jesliže nabývá pouze hodnot z nejvýše spočetné množiny \(\mathcal X = \{ x_1, x_2, \dots \}\) takové, že platí\[\displaystyle \sum_{x \in \mathcal X} \operatorname P(X = x) = 1.\]Pravděpodobnosti možných hodnot náhodné veličiny \(X\) potom jsou\[\operatorname P(X = x_k), \quad k = 1, 2, \dots.\]

## Poznámka Anki 1697018082071

Karty Anki: 1697018082071
GUID: w2oVqv`Tow; štítky: bi-pst::p03 bi-spol::26.

### Otázka (Front)

Definujte spojitou náhodnou veličinu.

### Odpověď (Back)

Náhodná veličina \(X\) se nazývá (absolutně) spojitá, jestliže existuje nezáporná funkce \(f_X\) taková, že pro každé \(x \in \mathbb R\) můžeme distribuční funkci \(F_X\) vyjádřit jako
\[F_X(x) = \int_{-\infty}^x f_X(t) \, \text dt.\]Funkci \(f_X\) v takovém případě nazýváme hustotou pravděpodobnosti náhodné veličiny \(X\).

## Poznámka Anki 1697018799880

Karty Anki: 1697018799880
GUID: iQ^0hG%lK&; štítky: bi-pst::p03 bi-spol::26.

### Otázka (Front)

Vyslovte větu o vlastnostech spojitých náhodných veličin.

### Odpověď (Back)

Pro hustotu \(f_X\) spojité náhodné veličiny \(X\) platí:

- \(\displaystyle \int_{-\infty}^{+\infty} f_X(x) \, \text dx = 1\);

- \(\operatorname P(X = x) = 0\) pro všechna \(x \in \mathbb R\),

- \(f_X(x) = \frac {\text d F_X}{\text dx}(x)\) v bodech, kde \(F_X\) má derivaci,

- \(\operatorname P(a < X \leq b) = \displaystyle \int_a^b f_X(x) \, \text dx = F_X(b) - F_X(a)\),

- \(\operatorname P(X \in B) = \displaystyle  \int_B f_X(x) \, \text dx\) pro všechny \(B\) v Borelovské \(\sigma\)-algebře na \(\mathbb R\).

## Poznámka Anki 1697020158420

Karty Anki: 1697020158420
GUID: s{g5g6;+gr; štítky: bi-pst::p03.

Metadata původního zdroje pro kartu 1697020158420: původní příznak autora 7.

### Otázka (Front)

Definujte kvantil a kvantilovou funkci.

### Odpověď (Back)

Nechť \(X\) je náhodná veličina s distribuční funkcí \(F_X\). Nechť \(\alpha \in (0, 1)\). Hodnota \(q_\alpha\) se nazývá \(\alpha\)-kvantil náhodné veličiny \(X\) právě tehdy, když
\[q_\alpha = \inf \{x \mid F_X(x) \geq \alpha \}.\]Kvantil uvažovaný jako funkce \(\alpha\) se nazývá kvantilová funkce a značí se \(F_X^{-1}(\alpha)\).

## Poznámka Anki 1697638916042

Karty Anki: 1697638916043
GUID: w23q_Mkq:b; štítky: bi-pst::p03 bi-spol::26.

### Otázka (Front)

Vyslovte větu o vlastnostech distribuční funkce.

### Odpověď (Back)

Distribuční funkce \(F\) náhodné veličiny \(X\) má následující vlastnosti:

- **je neklesající** - když \(x < y\), pak \(F(x) \leq F(y)\);
- **„začíná v **\(0\)** a končí v **\(1\)**“** - \(\displaystyle \lim_{x \to -\infty} F(x) = 0\) a \(\displaystyle \lim_{x \to +\infty} F(y) = 1\),
- **je spojitá zprava** - \(\displaystyle \lim_{y \to x+} = F(x)\).

