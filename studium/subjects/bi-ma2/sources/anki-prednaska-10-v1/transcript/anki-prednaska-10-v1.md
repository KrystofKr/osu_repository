# BI-MA2 – Přednáška 10

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1666106190172

Karty Anki: 1666106190172
GUID: FsgtZHS%kO; štítky: bi-ma2::p10 bi-spol::15.

### Otázka (Front)

Definujte Taylorův vzorec a zbytek v Taylorově vzorci.

### Odpověď (Back)

Nechť funkce \(f\) má v bodě \(a\) konečnou \(n\)-tou derivaci. Pro všechna přípustná \(x\) položme \(R_{n,a}(x) := f(x) - T_{n,a}(x)\). Potom vztah
\[f(x) = T_{n,a}(x) + R_{n,a}(x)\]nazýváme Taylorovým vzorcem a \(R_{n,a}\) nazýváme \(n\)-tým zbytkem v Taylorově vzorci.

## Poznámka Anki 1666106559907

Karty Anki: 1666106559907
GUID: OE4qubdh)I; štítky: bi-ma2::p10 bi-spol::15.

### Otázka (Front)

Vyslovte větu o chování zbytku.

### Odpověď (Back)

Nechť funkce \(f\) má v jistém okolí \(H_a\) bodu \(a\) spojitou \(n\)-tou derivaci. Pak pro zbytek v Taylorově vzorci platí
\[\lim \limits_{x \to a} \frac{R_{n,a}(x)}{(x-a)^n} = 0.\]

## Poznámka Anki 1666106858723

Karty Anki: 1666106858723
GUID: xGY}nq7bjp; štítky: bi-ma2::p10 bi-spol::15.

### Otázka (Front)

Dokažte větu o chování zbytku.

### Odpověď (Back)

BÚNO předpokládejme, že \(a=0\). Z definice zbytku a vlastností Taylorova polynomu plyne
\[R_n(0) = R'_n(0) = \cdots = R^{(n-1)}_n(0) = R^{(n)}_n(0) = 0.\]Pro výpočet limity lze použít l'Hospitalovo pravidlo. Potom
\[\lim \limits_{x \to 0} \frac{R_n(x)}{x^n} = \lim \limits_{x \to 0} \frac{R_n'(x)}{nx^{n-1}} = \cdots = \lim \limits_{x \to 0} \frac{R_n^{(n-1)}(x)}{n! \cdot x} = \lim \limits_{x \to 0} \frac{R_n^{(n)}(x)}{n!} = 0.\]Poslední rovnost platí, protože \(R_n^{(n)} = f^{(n)} - T_n^{(n)}\) je podle předpokladu spojitá funkce na \(H_a\) a \(R_n^{(n)}(0) = 0.\)

## Poznámka Anki 1666107422481

Karty Anki: 1666107422481
GUID: va2r<^M`,Z; štítky: bi-ma2::p10 bi-spol::15.

### Otázka (Front)

Vyslovte Taylorovu větu.

### Odpověď (Back)

Nechť existuje okolí \(H_a\) bodu \(a\) takové, že funkce \(f\) v něm má konečnou \((n+1)\)-ní derivaci. Pak zbytek v Taylorově vzorci \(f(x) = T_{n,a}(x) + R_{n,a}(x)\) lze pro každé \(x \in H_a\) zapsat ve tvaru
\[R_{n,a}(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1},\]kde číslo \(\xi\) závisí na \(x\) a \(n\) a leží uvnitř intervalu s krajními body \(x\) a \(a\). Tento tvar zbytku nazýváme Lagrangeův.

