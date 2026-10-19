# BI-MA1 – Přednáška 12

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA1
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1652128408801

Karty Anki: 1652128408801
GUID: c^!k3%fOKl; štítky: bi-ma1::p12.

### Otázka (Front)

Popište Newtonovu metodu.

### Odpověď (Back)

Newtonova metoda je iterační numerická metoda, která spočívá v konstrukci posloupnosti \((x_n)_{n=1}^{\infty}\) aproximující řešení rovnice \(f(x)=0\). Probíhá v následujících krocích:

- je dáno \(x_n\),
- sestroj tečnu funkce \(f\) v bodě \(x_n\),
- průsečík tečny s osou \(x\) nechť je další člen posloupnosti\[x_{n+1} := x_n - \frac{f(x_n)}{f'(x_n)},\]

- opakuj s \(x_{n+1}\) místo \(x_n\).

 [Obrázek: paste-edb643d855ea256bfd4feea10d30d0b3bd151e94.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1652129001827

Karty Anki: 1652129001827
GUID: G()u}gbnCD; štítky: bi-ma1::p12.

### Otázka (Front)

Popište lineární interpolaci.

### Odpověď (Back)

Postup:

- zvolíme vzorkovací body
- vypočteme vzorky
- spojíme sousední body úsečkou
Pro dobrý výsledek je nutno zvolit vzorkovací mřížku dostatečně hustou.

## Poznámka Anki 1652129175337

Karty Anki: 1652129175337
GUID: KA7aH.?~W<; štítky: bi-ma1::p12.

### Otázka (Front)

Popište kubickou interpolaci (spline).

### Odpověď (Back)

Místo linárních funkcí se používají polynomy třetího stupně, \(y = ax^3 + bx^2 + cx + d\). Jde o polynomy nejnižšího stupně mající inflexní body.
Jelikož je tento polynom zadán čtyřmi parametry, využijeme je pro nakladení dalších podnínek. Budeme chtít, aby "švy" byly nejen spojité, ale aby na sebe jednotlivé interpolační funkce navazovaly se stejnou derivací (tedy sklonem).

## Poznámka Anki 1652129427263

Karty Anki: 1652129427264
GUID: g`-6:&kNa5; štítky: bi-ma1::p12.

### Otázka (Front)

Definujte křivku.

### Odpověď (Back)

Buďte \(f\) a \(g\) dvě spojité funkce na intervalu \(\langle a, b \rangle\). Potom zobrazení \(F: \langle a, b \rangle \to \mathbb{R}^2\) definované předpisem
\[F(t) = ( f(t), g(t) ), t \in \langle a, b \rangle,\]nazveme křivkou v \(\mathbb{R}^2\).

## Poznámka Anki 1652129552534

Karty Anki: 1652129552534
GUID: E/$|_*YdCw; štítky: bi-ma1::p12.

### Otázka (Front)

Definujte tečný vektor.

### Odpověď (Back)

Máme-li křivku \(F(t) = ( f(t), g(t) ), t \in \langle a, b \rangle\) a jsou-li \(f\) a \(g\) na intervalu \(\langle a, b \rangle\) diferencovatelné (v krajích bereme jednostranné derivace), pak pokud je vektor
\(F'(t) := ( f'(t), g'(t) ), \,t \in \langle a, b \rangle \)
nenulový, tak ho nazveme tečným vektorem křivky \(F\) v bodě \(F(t)\).

## Poznámka Anki 1652129778255

Karty Anki: 1652129778255
GUID: rnIeg{;w/q; štítky: bi-ma1::p12.

### Otázka (Front)

Popište jednoduše Bézierovu křivku.

### Odpověď (Back)

Jsou zadány dva body \(A\) a \(B\) v rovině, které chceme spojit křivkou, a další dva body \(C\) a \(D\), které udávají tečný vektor, s kterým bod \(A\) opouštíme (\(C\)) a pod kterým do \(B\) vstupujeme (\(D\)).

 [Obrázek: paste-7c429c1a7021fa2691732009ab1b6f60911bcb79.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1652130096670

Karty Anki: 1652130096670
GUID: lIZz}C7A5~; štítky: bi-ma1::p12.

### Otázka (Front)

Definujte Bernsteinův polynom.

### Odpověď (Back)

Pro \(n \in \mathbb{N}_0\) a celočíselné \(i\) splňující \(0 \leq i \leq n\) definujeme Bernsteinův polynom \(B_{i,n}\) předpisem
\(B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}, t \in \mathbb{R}\).

## Poznámka Anki 1652130267462

Karty Anki: 1652130267462
GUID: Iq.A)!xm>!; štítky: bi-ma1::p12.

### Otázka (Front)

Definujte Bézierovu křivku.

### Odpověď (Back)

Pro \(n+1\) kontrolních bodů \(P_0, P_1, \dots, P_n \in \mathbb{R}^2\) definujeme křivku \(C\) předpisem
\[C(t) = \sum_{i=0}^{n} P_i B_{i,n}(t), t \in \langle 0, 1 \rangle,\]
a nazýváme ji Bézierovou křivkou s kontrolními body \(P_0, P_1, \dots, P_n\).

## Poznámka Anki 1654292576552

Karty Anki: 1654292576552
GUID: PQya0^i&0P; štítky: bi-ma1::p12.

### Otázka (Front)

Podrobně popište metodu půlení. Jakou rovnici řeší?

### Odpověď (Back)

Metoda půlení řeší rovnici \(f(c) = 0\).
Mějme funkci \(f\) spojitou na intervalu \(\langle a, b \rangle\) a nechť \(f(a) \cdot f(b) < 0\).
Položme \(a_1 := a\) a \(b_1 = b\). Protože znaménka \(f(a_1)\) a \(f(b_1)\) jsou různá, nastane jedna ze tří možností:

1. \(f(\frac{a_1 + b_1}{2}) = 0\),

2. znaménka \(f(a_1)\) a \(f(\frac{a_1 + b_1}{2})\) jsou různá,
3. znaménka \(f(\frac{a_1 + b_1}{2})\) a  \(f(b_1)\) jsou různá.
Dále postupujeme podle toho, která z možností nastala:

1. Hledaným bodem \(c\) je \(\frac{a_1 + b_1}{2}\).
2. Položme \(a_2 := a_1\) a \(b_2 := \frac{a_1 + b_1}{2}\).
3. Položme \(a_2 := \frac{a_1 + b_1}{2}\) a \(b_2 = b_1\).
Postup opakujeme s novými hodnotami.

## Poznámka Anki 1654375348279

Karty Anki: 1654375348279
GUID: N?/?2|S/cV; štítky: bi-ma1::p12.

### Otázka (Front)

Jaké jsou problémy Newtonovy metody?

### Odpověď (Back)

Pro špatně zvolený výchozí bod \(x_1\) může posloupnost oscilovat nebo divergovat do nekonečna.
Případně může nastat situace, kdy \(f'(x_n) = 0\).

## Poznámka Anki 1654375443541

Karty Anki: 1654375443541
GUID: v<QHs;@;~3; štítky: bi-ma1::p12.

### Otázka (Front)

Jaké jsou výhody Newtonovy metody?

### Odpověď (Back)

Oproti metodě půlení intervalu konverguje Newtonova metoda výrazně rychleji, a to s kvadratickou konvergencí.

