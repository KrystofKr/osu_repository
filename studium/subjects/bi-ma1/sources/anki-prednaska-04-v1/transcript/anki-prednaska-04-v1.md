# BI-MA1 – Přednáška 04

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA1
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1646686891695

Karty Anki: 1646686891695
GUID: G=SM/Ou?6?; štítky: bi-ma1::p04 bi-spol::13 bi-spol::14.

### Otázka (Front)

Definujte limitu funkce.

### Odpověď (Back)

Mějme funkci \(f : A \to \mathbb R\) a hromadný bod \(a \in \overline{\mathbb R}\) množiny \(A\). Funkce \(f\) má v bodě \(a\) limitu \(b \in \overline{\mathbb R}\), právě když pro každé okolí \(U_b\) bodu \(b\) existuje okolí \(U_a\) bodu \(a\) takové, že pokud pro \(x \in \mathbb R\) platí\(x \in (U_a \cap A) \smallsetminus \{ a \}\), pak \(f(x) \in U_b\). Symbolicky lze limitu funkce definovat následovně:\[(\forall U_b)(\exists U_a)(\forall x \in \mathbb R)(x \in (U_a \cap A) \setminus \{a\} \Rightarrow f(x) \in U_b).\]Tuto skutečnost značíme\[\displaystyle \lim_{x \to a} f(x) = b.\]

## Poznámka Anki 1646687018784

Karty Anki: 1646687018784
GUID: t;T^*:8>pl; štítky: bi-ma1::p04.

### Otázka (Front)

Čemu je rovno \(\lim \limits_{x \to 0} \frac{1}{x^2}\)?

### Odpověď (Back)

\(+ \infty\)

## Poznámka Anki 1646687078918

Karty Anki: 1646687078918
GUID: Lcbw!X5/b&; štítky: bi-ma1::p04.

### Otázka (Front)

Čemu je rovno \(\lim \limits_{x \to a} | x |\)?

### Odpověď (Back)

\(| a |\)

## Poznámka Anki 1646687494964

Karty Anki: 1646687494964
GUID: g8]oe_?7]U; štítky: bi-ma1::p04 bi-spol::13 bi-spol::14.

### Otázka (Front)

Definujte jednostanné limity.

### Odpověď (Back)

Mějme funkci \(f : A \to \mathbb R\) a bod \(a \in \mathbb R\). Označme\[\begin{matrix}
M_- := A \cap (-\infty, a),\\
M_+ := A \cap (a, +\infty)
\end{matrix}.\]Potom limitu funkce \(f\) v bodě \(a\) zleva definujeme jako limitu zúžení funkce \(f\) na množinu \(M_{\_}\) a značíme ji\[\displaystyle \lim_{x \to a-} f(x) := \displaystyle \lim_{x \to a} (f |_{M_-})(x).\]Obdobně limitu funkce \(f\) v bodě \(a\) zprava definujeme jako limitu zúžení funkce \(f\) na množinu \(M_+\) a značíme ji\[\displaystyle \lim_{x \to a+}f(x) := \displaystyle \lim_ {x \to a}(f|_{M_+})(x).\]

## Poznámka Anki 1646687713595

Karty Anki: 1646687713595
GUID: y@N*(k2],g; štítky: bi-ma1::p04 bi-spol::13 bi-spol::14.

### Otázka (Front)

Vyslovte větu o vztahu limity funkce a jednostanných limit funkce.

### Odpověď (Back)

Mějme funkci \(f: D_f \to \mathbb{R}\) a nechť \(a \in \mathbb{R}\) je hromadným bodem množiny \(D_f \cap (a, + \infty)\) i \(D_f \cap (- \infty, a)\).
Potom limita \(\lim \limits_{x \to a} f(x)\) existuje a je rovna \(b \in \overline{\mathbb{R}}\), právě když existují obě jednostranné limity \(\lim \limits_{x \to a_+}f(x)\) a \(\lim \limits_{x \to a_-}f(x)\) a obě jsou rovny \(b\).

## Poznámka Anki 1646687758349

Karty Anki: 1646687758349
GUID: mP_uK7}@-H; štítky: bi-ma1::p04 bi-spol::13.

### Otázka (Front)

Vyslovte větu o jednoznačnosti limit.

### Odpověď (Back)

Funkce \(f\) má v bodě \(a\) nejvýše jednu limitu.

## Poznámka Anki 1646687917264

Karty Anki: 1646687917264
GUID: z4sgXv/=L=; štítky: bi-ma1::p04 bi-spol::13.

### Otázka (Front)

Vyslovte větu o limitě zúžení.

### Odpověď (Back)

Mějme funkci \(f\) a bod \(a \in \overline{\mathbb{R}}\), který je hromadným bodem definičního oboru \(D_f\) funkce \(f\). Dále uvažme množinu \(M \subset D_f\) takovou, že bod \(a\) je stále jejím hromadným bodem.
Potom pokud \(\lim \limits_{x \to a}f(x) = b \in \overline{\mathbb{R}}\), pak i pro \(g := f|_M\), zúžení funkce \(f\) na množinu \(M\), platí  \(\lim \limits_{x \to a}g(x) = b \).

## Poznámka Anki 1646688262535

Karty Anki: 1646688262535
GUID: ECi*7mC+0^; štítky: bi-ma1::p04 bi-spol::13.

### Otázka (Front)

Vyslovte Heineho větu.

### Odpověď (Back)

Platí\[\displaystyle \lim_{x \to a} f(x) = b,\]právě když \(a\) je hromadným bodem \(D_f\) a pro každou posloupnost \((x_n)_{n = 1}^\infty\) s limitou \(a\) splňující\[\{ x_n \mid n\in \mathbb N \} \subset D_f \smallsetminus \{ a \}\]platí\[\displaystyle \lim_{n \to \infty} f(x_n) = b.\]

## Poznámka Anki 1718719205506

Karty Anki: 1718719205506
GUID: gPoj)_wj}@; štítky: bi-ma1::p04 bi-spol::13.

### Otázka (Front)

Jak lze pomocí Heineho věty vyvrátit existenci limity funkce?

### Odpověď (Back)

Chceme rozhodout o existenci limity
\[\displaystyle \lim_{x \to a} f(x).\]Zvolme proto dvě posloupnosti \((a_n)_{n = 1}^\infty\) a \((b_n)_{n = 1}^\infty\) mající za limitu bod \(a\) a splňující, že všechny jejich členy pro \(n \in \mathbb N\) náleží \(D_f \smallsetminus \{ a \}\). Pokud nastane situace, že
\[\displaystyle \lim_{n \to \infty} f(a_n) \neq \displaystyle \lim_{n \to \infty} f(b_n),\]pak
\[\displaystyle \lim_{x \to a} f(x)\]neexistuje.

