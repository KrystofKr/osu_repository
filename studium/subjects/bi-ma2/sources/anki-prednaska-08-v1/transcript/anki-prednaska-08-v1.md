# BI-MA2 – Přednáška 08

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1665425228426

Karty Anki: 1665425228426
GUID: PRGdI*D~I+; štítky: bi-ma2::p08.

### Otázka (Front)

Definujte exponenciální funkci.

### Odpověď (Back)

Zobrazení, které každému \(x \in \mathbb{R}\) přiřadí součet absolutně konvergentní řady
\[\sum \limits_{k=0}^\infty \frac{x^k}{k!}\]nazýváme exponenciální funkcí. Její funkční hodnotu pro zadaná \(x \in \mathbb{R}\) značíme symbolem \(e^x\).

## Poznámka Anki 1665425388129

Karty Anki: 1665425388129
GUID: bdeUs/i}V!; štítky: bi-ma2::p08.

### Otázka (Front)

Dokažte, že \(e^0 = 1\).

### Odpověď (Back)

Přímo z dosazení \(x = 0\) do definičního vztahu
\[e^0 = \sum \limits_{k=0}^\infty \frac{0^k}{k!} = 1 + 0 + 0 + \cdots = 1.\]

## Poznámka Anki 1666011557816

Karty Anki: 1666011557816
GUID: e~n|IhMH)M; štítky: bi-ma2::p08 bi-spol::15.

### Otázka (Front)

Definujte mocninnou řadu.

### Odpověď (Back)

Nechť je dána posloupnost \((a_k)_{k=0}^\infty\) a číslo \(c \in \mathbb{R}\). Číselnou řadu
\[\sum \limits_{k=0}^\infty a_k(x-c)^k\]závisející na reálném parametru \(x\) nazýváme mocninnou řadou se středem v bodě \(c\).

## Poznámka Anki 1666011657283

Karty Anki: 1666011657283
GUID: DL0Wq3eHa@; štítky: bi-ma2::p08 bi-spol::15.

### Otázka (Front)

Definujte obor konvergence.

### Odpověď (Back)

Množinu všech hodnot \(x \in \mathbb{R}\), pro které mocninná řada \(\sum \limits_{k=0}^{+\infty} a_k(x-c)^k\) konverguje nazýváme oborem konvergence mocninné řady.

## Poznámka Anki 1666012624991

Karty Anki: 1666012624992
GUID: k.(^u-^<~#; štítky: bi-ma2::p08 bi-spol::15.

### Otázka (Front)

Vyslovte větu o poloměru konvergence.

### Odpověď (Back)

Pokud existuje limita
\[L := \lim \limits_{k \to \infty} \bigg| \frac{a_{k+1}}{a_k} \bigg|,\]potom klademe
\[R:=
\begin{cases}
\frac{1}{L}, && L \in \mathbb{R}, \\
+ \infty, && L = 0, \\
0, && L = +\infty
\end{cases}\]a tvrdíme, že mocninná řada
\[\sum \limits_{k=0}^\infty a_k(x-c)^k\]konverguje absolutně pro \(x \in (c-R, c+R)\) a diverguje pro \(|x-c| > R\).

## Poznámka Anki 1666012926641

Karty Anki: 1666012926642
GUID: uh/;(8qq@V; štítky: bi-ma2::p08 bi-spol::15.

### Otázka (Front)

Dokažte větu o poloměru konvergence.

### Odpověď (Back)

BÚNO \(c=0\). Pro libovolné \(x \in \mathbb{R}\) dostáváme
\[\lim \limits_{k \to \infty} \bigg| \frac{a_{k+1}x^{k+1}}{a_k x^k} \bigg| = \lim \limits_{k \to \infty} |x| \cdot \bigg| \frac{a_{k+1}}{a_k} \bigg| = |x| \cdot L.\]Shrnujeme, že pokud

- \(|x| \cdot L < 1\), tedy \(|x| < R\), pak podle d'Alembertova kritéria zkoumaná řada konverguje **absolutně**,

- \(|x| \cdot L > 1\), tedy \(|x| > R\), pak podle podílového kritéria je \(\lim \limits_{k \to \infty} |a_kx^k| = +\infty\). Tudíž nemůže být splněna nutná podmínka konvergence zkoumané řady (tj. neplatí \(\lim \limits_{k \to \infty} a_k x^k = 0\)).

## Poznámka Anki 1672960267150

Karty Anki: 1672960267150
GUID: IdZlbF]jOp; štítky: bi-ma2::p08.

### Otázka (Front)

Definujte obecnou mocninu.

### Odpověď (Back)

Pro \(a \in (0, +\infty)\) a \(x \in \mathbb R\) definujeme
\[a^x:= e^{x \ln a}.\]

