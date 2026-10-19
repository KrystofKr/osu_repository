# NI-VSM – Přednáška 05

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-VSM
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1741179539855

Karty Anki: 1741179539855
GUID: o,8B5fFKeh; štítky: duplicate ni-vsm::p05.

### Otázka (Front)

Definujte entropii diskrétní náhodné veličiny.

### Odpověď (Back)

Entropie diskrétní náhodné veličiny \(X\) je definována vztahem\[H(X) = - \displaystyle \sum_{x \in \mathcal X} p(x) \log p(x),\]kde \(\mathcal X\) je množina všech hodnot, kterých může \(X\) nabývat.

### Doplňující pole (Extra)

V kontextu teorie informace značí \(p(x)\) pravděpodobní funkci veličiny \(X\) v bodě \(x\), tedy\[p(x) = \operatorname P(X = x).\]Entropie bývá nejčastěji definována s logaritmem při základu \(2\). Měřenou jednotkou je potom bit. Pro potřebu této definice dále klademe\[0 \cdot \log 0 = 0.\]

## Poznámka Anki 1741180683802

Karty Anki: 1741180683802
GUID: lLkh7maUTS; štítky: ni-vsm::p05.

### Otázka (Front)

Definujte sdruženou entropii náhodného vektoru.

### Odpověď (Back)

Sdužená entropie diskrétního náhodného vektoru \(\mathbf X\) se sdruženým rozdělením \(p(\mathbf x)\) je definována vztahem\[H(\mathbf X) = - \displaystyle \sum_{\mathbf x \in \mathcal X} p(\mathbf x) \log p(\mathbf x).\]

## Poznámka Anki 1741181786730

Karty Anki: 1741181786730
GUID: EtGINR#HtR; štítky: ni-vsm::p05.

### Otázka (Front)

Definujte podmíněnou entropii.

### Odpověď (Back)

Podmíněná entropie diskrétních náhodných veličin \(X\), \(Y\) se sdruženým rozdělením \(p(x, y)\) je definována vztahem\[H(Y|X) = - \displaystyle \sum_{x \in \mathcal X} \displaystyle \sum_{y \in \mathcal Y} p(x, y) \log p(y|x),\]kde\[p(y|x) = \frac{p(x, y)}{(x)}.\]

## Poznámka Anki 1741182337752

Karty Anki: 1741182337752
GUID: u^V^-CA~Cv; štítky: ni-vsm::p05.

### Otázka (Front)

Vyslovte větu o řetězovém pravidlu pro sdruženou entropii.

### Odpověď (Back)

Podle řetězového pravidla pro sdruženou entropii platí\[H(X, Y) = H(X) + H(Y|X).\]

## Poznámka Anki 1741195915447

Karty Anki: 1741195915448
GUID: PKh%6*Nye%; štítky: ni-vsm::p05.

### Otázka (Front)

Definujte relativní entropii (Kullback-Leiblerovu vzdálenost).

### Odpověď (Back)

Relativní entropie (Kullback-Leiblerova vzdálenost) mezi diskrétním rozdělením \(p\) a diskréním rozdělením \(q\) na množině \(\mathcal X\) je definována vztahem\[D(p \| q) = \displaystyle \sum_{x \in \mathcal X} p(x) \log \frac{p(x)}{q(x)}.\]

### Doplňující pole (Extra)

Pro potřebu této definice klademe\[0 \cdot \log \frac 0 0 = 0\]a pro \(p \neq 0\), \(q \neq 0\) dále\[\begin{align}
0 \cdot \log \frac 0 q &= 0,\\
p \cdot \log \frac p 0 &= + \infty.
\end{align}\]Důležité je poznamenat, že obecně není \(D(p \| q) \) rovno \(D(q \| p)\).

## Poznámka Anki 1741196179990

Karty Anki: 1741196179990
GUID: eCN*qi@;H6; štítky: ni-vsm::p05.

### Otázka (Front)

Definujte vzájemnou informaci.

### Odpověď (Back)

Vzájemná informace diskrétních náhodných veličin \(X\) a \(Y\) je definována vztahem\[I(X; Y) = \displaystyle \sum_{x \in \mathcal X} \displaystyle \sum_{y \in \mathcal Y} p(x, y) \log \frac {p(x, y)}{p(x), p(y)}.\]Jedná se tedy o relativní entropii skutečného sdruženého rozdělení a rozdělení nezávislých náhodných veličin se stejnými marginálami\[I(X; Y) = D \big( p(x, y) \| p(x) p(y) \big).\]

## Poznámka Anki 1741196502674

Karty Anki: 1741196502674
GUID: ur2=`8eaH5; štítky: ni-vsm::p05.

### Otázka (Front)

Vyslovte větu o vlastnostech vzájemné informace a entropie.

### Odpověď (Back)

Mějme diskrétní náhodné veličiny \(X\) a \(Y\). Pak platí\[\begin{align}
I(X; Y) &= I(Y; X),\\
I(X, Y) &= H(X) - H(X | Y),\\
I(X, Y) &= H(Y) - H(Y | X),\\
I(X, Y) &= H(S) + H(Y) - H(X, Y),\\
I(X, X) &= H(X).
\end{align}\]

 [Obrázek: paste-93830389266b6087dd06af7287249cf0e2fe3658.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1741196798109

Karty Anki: 1741196798109
GUID: FSH,8o#ftK; štítky: ni-vsm::p05.

### Otázka (Front)

Vyslovte větu o informační nerovnosti.

### Odpověď (Back)

Mějme \(p(x)\) a \(q(x)\) dvě možná rozdělení diskrétní náhodné veličiny \(X\) pro \(x \in \mathcal X\). Potom\[D(p \| q) \geq 0,\]přičemž rovnost nastává pouze pokud \(p(x) = q(x)\) pro všechna \(x \in \mathcal X\).

## Poznámka Anki 1741213207683

Karty Anki: 1741213207683
GUID: E3hkc;C(#$; štítky: ni-vsm::p05.

### Otázka (Front)

Vyslovte větu o nezápornosti vzájemné informace. Z čeho plyne?

### Odpověď (Back)

Pro diskrétní náhodné veličiny \(X\) a \(Y\) platí\[I(X; Y) \geq 0,\]přičemž rovnost nastává právě tehdy, když jsou \(X\) a \(Y\) nezávislé. Tato věta plyne z věty o informační nerovnosti.

## Poznámka Anki 1741213299585

Karty Anki: 1741213299585
GUID: j%5UEl-+}<; štítky: ni-vsm::p05.

### Otázka (Front)

Vyslovte větu o maximalizaci entropie. Z čeho plyne?

### Odpověď (Back)

Pro diskrétní náhodnou veličinu \(X\) nabývajcí hodnot konečné množiny \(\mathcal X\) platí\[H(X) \leq \log | \mathcal X |,\]přičemž rovnost nastává právě tehdy, když \(X\) má rovnoměrné rozdělení na \(\mathcal X\). Tato věta plyne z informační nerovnosti.

## Poznámka Anki 1741213369376

Karty Anki: 1741213369376
GUID: dIbR<4QQi@; štítky: ni-vsm::p05.

### Otázka (Front)

Vyslovte větu o redukci entropie podmíěním.

### Odpověď (Back)

Pro diskrétní náhodné veličiny \(X\) a \(Y\) platí\[H(X|Y) \leq H(X),\]přičemž rovnost nastává, pouze pokud jsou \(X\) a \(Y\) nezávislé.

