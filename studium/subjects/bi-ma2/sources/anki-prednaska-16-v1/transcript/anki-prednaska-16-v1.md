# BI-MA2 – Přednáška 16

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1669738080260

Karty Anki: 1669738080260
GUID: xA+vx1MdD`; štítky: bi-ma2::p16 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Definujte lokální extrémy funkce více proměnných.

### Odpověď (Back)

Funkce \(f: D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) má v bodě \(\mathbf a \in D_f\):

- **ostré lokální minimum**, právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in (U_{\mathbf a} \cap D_f) \smallsetminus \{ \mathbf a \}\) platí \(f(\mathbf x) > f(\mathbf a)\);

- **ostré lokální maximum**, právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in (U_{\mathbf a} \cap D_f) \smallsetminus \{ \mathbf a \}\) platí \(f(\mathbf x) < f(\mathbf a)\);
- **lokální minimum**, právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in U_{\mathbf a} \cap D_f\) platí \(f(\mathbf x) \geq f(\mathbf a)\);
- **lokální maximum**, právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in U_{\mathbf a} \cap D_f\) platí \(f(\mathbf x) \leq f(\mathbf a)\).

### Doplňující pole (Extra)

V krajních bodech definičního oboru uvažujeme jednostranné okolí \(U_{\mathbf a}\) bodu \(\mathbf a\).

## Poznámka Anki 1669738478290

Karty Anki: 1669738478290
GUID: O)N+a!Q7!#; štítky: bi-ma2::p16 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o nutné podmínce existence lokálního extrému funkce I.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\), bod \(\mathbf a \in D_f\) takový, že \(f\) má v bodě \(\mathbf a\) lokální extrém, a \(j \in \hat n\). Potom je parciální derivace funkce \(f\) v bodě \(\mathbf a\) podle \(j\)-té proměnné nulová, nebo neexistuje.

**Důkaz
**Definujme funkci\[g(x) = f(\mathbf a + x \mathbf e_j).\]Tato funkce má podle předpokladů jistě lokální extrém v bodě \(x = 0\). Víme, že pokud má reálná funkce jedné reálně proměnné lokální extrém v bodě \(x\), pak je její derivace v tomto bodě nulová nebo neexistuje. Z toho plyne, že \(g'(0)\) je buď nulová, nebo neexistuje. Věta výše plyne ze vztahu\[\partial_jf(\mathbf a) = g'(0).\]

## Poznámka Anki 1669738543503

Karty Anki: 1669738543503
GUID: K7v%6CA`8Z; štítky: bi-ma2::p16 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Jaký důsledek má věta o nutné podmínce existence lokálního extrému I?

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(a \in D_f\) takový, že \(f\) má v bodě \(a \) lokální extrém a parciální derivace podle všech poměnných. Potom je gradient funkce \(f\) v bodě \(a \) nulový vektor\[\nabla f(\mathbf a) = \theta.\]

## Poznámka Anki 1669738662053

Karty Anki: 1669738662053
GUID: e,`J7SFCmA; štítky: bi-ma2::p16 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Definujte stacionární bod a kritický bod.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n \). Bod \(\mathbf a \in D_f\) splňující \(\nabla f(\mathbf a) = \theta\) nazýváme **stacionárním bodem**. **Kritickým bodem** nazveme bod, kde neexistuje gradient nebo je stacionární.

## Poznámka Anki 1669738932270

Karty Anki: 1669738932270
GUID: qgB!t+5#q5; štítky: bi-ma2::p16 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Vyslovte větu o nutné podmínce existence lokálního extrému funkce II.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(\mathbf a \in D_f\) takový, že \(f \) má v bodě \(\mathbf a\) lokální minimum resp. maximum a spojité všechny druhé parciální derivace na jeho okolí. Potom je \(\nabla^2 f(\mathbf a)\) Hessova matice funkce \(f\) v bodě \(\mathbf a\) pozitivně semidefinitní (PSD) resp. negativně semidefinitní (NSD).

### Doplňující pole (Extra)

**V předmětu NI-MPI **je požadován bod \(a \in D_f\) takový, že je stacionárním bodem \(f\).

## Poznámka Anki 1670247799832

Karty Anki: 1670247799832
GUID: q}y=#]Wl}Y; štítky: bi-ma2::p16 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Vyslovte větu o postačující podmínce existence lokálního extrému.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(\mathbf a \in D_f\) takový, že \(f\) má na okolí bodu \(\mathbf a\) spojité všechny třetí parciální derivace. Pokud jsou splněny následující podmínky:

- \(\nabla f(\mathbf a) = \theta\) (\(\mathbf a\) je stacionární bod),

- \(\nabla^2f(\mathbf a)\) je pozitivně definitní (PD) resp. negativně definitní (ND),

pak má  \(f\) v bodě  \(\mathbf a\) ostré lokální minimum resp. ostré lokální maximum. Pokud je Hessova matice \(\nabla^2f(\mathbf a)\) indefinitní (ID), pak se v bodě \(\mathbf a\) nachází sedlový bod a funkce \(f\) v něm lokální extrém nemá.

### Doplňující pole (Extra)

**V předmětu NI-MPI **je požadována spojitost pouze druhých parciálních derivací.

## Poznámka Anki 1673186319045

Karty Anki: 1673186319045
GUID: vSKXS}R?Ey; štítky: bi-ma2::p16 bi-spol::16.

### Otázka (Front)

Vyslovte lemma o Taylorově větě (do kvadratických členů) s odhadem chyby pro funkce více proměnných.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\), mající spojité všechny parciální derivace do třetího řádu včetně na okolí \(U_\mathbf a\) bodu \(\mathbf a \in D_f\). Potom existuje konstanta \(M > 0\) taková, že pro každé \(\mathbf x \in U_\mathbf a\) platí\[f(\mathbf x) = f(\mathbf a) + \nabla f(\mathbf a) \cdot (\mathbf x - \mathbf a) + \frac 1 2 (\mathbf x - \mathbf a)^T \cdot \nabla^2 f(\mathbf a) \cdot (\mathbf x - \mathbf a) + R_2(\mathbf x),\]kde \(|R_2(\mathbf x)| \leq M \| \mathbf x - \mathbf a \|^3.\)

## Poznámka Anki 1673187227411

Karty Anki: 1673187227411
GUID: fc[>_<p+-1; štítky: bi-ma2::p16.

### Otázka (Front)

Popište problém, který řeší lineární regrese.

### Odpověď (Back)

Předpokládejme, že máme k dispozici sadu dat \(\set{(x_i, y_i)}_{i = 1}^n\) a chceme nalézt lineární kombinaci daných funkcí \(f_1, f_2, \dots, f_m\), tj. funkci
\[f_c = \sum \limits_{i = 1}^m c_i f_i,\]tak, aby funkční hodnoty funkce \(f\) v bodech \(x_i\) co nejlépe odpovídaly hodnotám \(y_i\) pro každé \(i \in \hat n\). Alternativně řečeno, snažíme se dobře vystihnout hypotetickou závislost \(y \approx f(x)\). Úkolem je tedy určit neznámé koeficienty lineární kombinace \(c_1, c_2, \dots, c_m\).

## Poznámka Anki 1673187754054

Karty Anki: 1673187754054
GUID: E(aUn,1B1Z; štítky: bi-ma2::p16.

### Otázka (Front)

Popište metodu nejmenších čtverců.

### Odpověď (Back)

Metoda nejmenších čtverců spočívá v myšlence minimalizovat kvadrát celkové chyby mezi \(y_i\) a \(f(x_i)\). Přesněji, hledáme hodnoty \(c_1, c_2, \dots, c_m\) tak, aby hodnota
\[F(\mathbf c) := \sum \limits_{i = 1}^n \big( y_i - f_\mathbf c(x_i) \big)^2 = \sum \limits_{i = 1}^n \big( y_i - (\mathbf{Ac})_i  \big)^2 = \| \mathbf y - \mathbf{Ac} \|_2^2\]byla co nejmenší, kde
\[(\mathbf{Ac})_i = \sum \limits_{j = 1}^m f_j(x_i)c_j.\]Tedy metodu nejmenších čtverců můžeme shrnout jako **minimalizuj **\(\| \mathbf y - \mathbf{Ac} \|_2^2\), **vůči **\(\mathbf c = (c_1, c_2, \dots, c_m)^T \in \mathbb R^m\), **kde **\(\mathbf y = (y_1, y_2, \dots, y_n)^T \in \mathbb R^n\) a \(\mathbf A_{ij} = f_j(x_i)\) **jsou dány**. Což provedeme pomocí hledání extrémů funkcí více proměnných.

