# BI-MA2 – Přednáška 03

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1663662529397

Karty Anki: 1663662529397
GUID: fynj!qtp8F; štítky: bi-ma2::p03 bi-spol::15.

### Otázka (Front)

Vyslovte a dokažte větu o integraci per partes.

### Odpověď (Back)

Nechť funkce \(f\) je diferencovatelná v intervalu \((a, b)\) a \(G\) je primitivní funkce k funkci \(g\) na intervalu \((a, b)\) a konečně nechť existuje primitivní funkce k funkci \(f'G\). Potom existuje primitivní funkce k funkci \(f g\) a platí
\[\int fg = fG - \int f'G.\]
**Důkaz
**Větu lze přímo ověřit pomocí derivace.
\[(fG - \int f'G)' = (fG)' - f'G = f'G + fG' - f'G = fG' = fg\]

## Poznámka Anki 1663684348881

Karty Anki: 1663684348881
GUID: N}D=(J5PjK; štítky: bi-ma2::p03 bi-spol::15.

### Otázka (Front)

Vyslovte větu o substituci v neurčitém integrálu (I).

### Odpověď (Back)

Nechť pro funkce \(f\) a \(\varphi\) platí

- \(f\) má primitivní funkci \(F\) na intervalu \((a, b)\),

- \(\varphi\) je na intervalu \((\alpha, \beta)\) diferencovatelná,

- \(\varphi \bigl((\alpha, \beta)\bigr) \subset (a, b)\).

Pak funkce \(f(\varphi(x)) \cdot \varphi'(x)\) má primitivní funkci na intervalu \((\alpha, \beta)\) a platí
\[\int f \big( \varphi(x) \big) \cdot \varphi'(x) \, \text dx = F \big( \varphi(x) \big) + C.\]

## Poznámka Anki 1663690300932

Karty Anki: 1663690300932
GUID: j|WrVH51v;; štítky: bi-ma2::p03 bi-spol::15.

### Otázka (Front)

Dokažte větu o substituci v neurčitém integrálu (I).

### Odpověď (Back)

\(F\) je primitivní funkcí k funkci \(f\), tj. \(F'(x) = f(x)\) pro každé \(x \in (a, b)\). Podle věty o derivaci složené funkce dostaneme
\[(F \circ \varphi)'(x) = F'\bigl(\varphi(x)\bigr) \cdot \varphi'(x) = f\bigl(\varphi(x)\bigr) \cdot \varphi'(x)\]pro každé \(x \in (\alpha, \beta)\).

## Poznámka Anki 1663690530922

Karty Anki: 1663690530923
GUID: g)m+BED||}; štítky: bi-ma2::p03 bi-spol::15.

### Otázka (Front)

Vyslovte větu o substituci v neurčitém integrálu (II).

### Odpověď (Back)

Nechť \(f\) je definována na intervalu \((a, b)\) a nechť \(\varphi\) je bijekce intervalu \((\alpha, \beta)\) na \((a, b)\) s nenulovou konečnou derivací v každém bodě intervalu \((\alpha, \beta)\). Pak platí
\[\int f \big( \varphi(t) \big) \cdot \varphi'(t) \, \text dt = G(t) + C \implies \int f(x) \, \text dx = G \big( \varphi^{-1}(x) \big) + C.\]

## Poznámka Anki 1663690806164

Karty Anki: 1663690806164
GUID: ATqQ+Fz8Sm; štítky: bi-ma2::p03 bi-spol::15.

### Otázka (Front)

Dokažte větu o substituci v neurčitém integrálu (II).

### Odpověď (Back)

Pomocí věty o derivaci inverzní funkce odvodíme, že
\[\Big(G\big(\varphi^{-1}(x)\big)\Big)' = G'\big(\varphi^{-1}(x)\big) \cdot \frac{1}{\varphi' \big(\varphi^{-1}(x)\big)} = f\big(\varphi\big(\varphi^{-1}(x)\big)\big) \cdot \varphi'\big(\varphi^{-1}(x)\big) \cdot \frac{1}{\varphi'\big(\varphi^{-1}(x)\big)} = f(x).\]

