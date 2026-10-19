# BI-MA2 – Přednáška 06

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 2 poznámek, 2 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1664839197380

Karty Anki: 1664839197380
GUID: P6C]}nr-G/; štítky: bi-ma2::p06.

### Otázka (Front)

Popište lichoběžníkové pravidlo.

### Odpověď (Back)

Na dílčích intervalech se můžeme pokusit integrovanou funkci aproximovat lineární funkcí, která prochází body \((x_{i-1}, f(x_{i-1}))\) a \((x_i, f(x_i))\). "Obsah" plochy pod grafem funkce, resp. \(\int_{x_{i-1}}^{x_i} f(x) \, \text dx\), pak lze aproximovat obsahem lichoběžníku
\[S = \frac{f(x_{x-1}) + f(x_i)}{2} \cdot (x_i - x_{i-1}).\]
Buď tedy \(f\) spojitá na intervalu \(\langle a, b \rangle\). Pro \(n \in \mathbb N\) a \(\Delta := \frac{b-a}n\) použijeme ekvidistantní dělení \(x_i := a + i \cdot \Delta\), \(i = 0, 1, \dots, n\), tedy
\[\sigma = \set{a, a + \Delta, a + 2\Delta, \dots, a + (n-1)\Delta, a + n\Delta = b}.\]Hodnotu integrálu \(\int_a^b f(x) \, \text dx\) aproximujeme pomocí součtu obsahů lichoběžníků
\[\sum \limits_{i=1}^n \frac{f(x_{i-1}) + f(x_i)}2 \cdot \Delta = \frac{b-a}{2n} \cdot \Big( f(a) + 2 \sum \limits_{i=1}^{n-1} f(x_i) + f(b) \Big).\]Pro dané \(a,b \in \mathbb R\) a \(n \in \mathbb N\) označme aproximaci integrálu \(\int_a^b f(x) \, \text dx\) jako
\[\mathcal J_\text{trapezoid} = \frac{b-a}{2n} \cdot \Big( f(a) + 2 \sum \limits_{i=1}^{n-1} f(x_i) + f(b) \Big).\]

## Poznámka Anki 1672940354763

Karty Anki: 1672940354764
GUID: hO|!/;B|e7; štítky: bi-ma2::p06.

### Otázka (Front)

Vyslovte větu o odhadu chyby v lichoběžníkovém pravidlu.

### Odpověď (Back)

Nechť funkce \(f\) má na intervalu \(\langle a, b \rangle\) druhou derivaci a existuje \(M \in \mathbb R\) takové, že \(| f''(x) | \leq M\) pro všechna \(x \in \langle a, b \rangle\). Potom
\[\bigg| \int_a^b f(x) \, \text dx - \mathcal J_\text{trapeziod} \bigg| \leq \frac{M(b-a)^3}{12n^2}.\]

