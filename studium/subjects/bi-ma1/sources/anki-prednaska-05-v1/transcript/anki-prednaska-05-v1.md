# BI-MA1 – Přednáška 05

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA1
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1647363804702

Karty Anki: 1647363804702
GUID: IHa,3Hs,LY; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte větu o vztahu hromadných bodů množin a posloupností.

### Odpověď (Back)

Mějme množinu \(M \subset \mathbb{R}\).
Bod \(b \in \overline{\mathbb{R}}\) je hromadným bodem množiny \(M\), právě když existuje posloupnost \((a_{n})_{n=1}^{\infty}\) jejíž členy všechny leží v \(M\) a jsou různé od \(b\) a \(\lim a_n = b\).

## Poznámka Anki 1647363950427

Karty Anki: 1647363950427
GUID: r[uPT}vkO]; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte větu o limitě vybrané posloupnosti.

### Odpověď (Back)

Nechť posloupnost \((a_{n})_{n=1}^{\infty}\) má limitu \(\alpha \in \overline{\mathbb R}\). Pak každá podposloupnost vybraná z \((a_n)_{n=1}^{\infty}\) má také limitu \(\alpha\).

Tedy platí, že pokud lze z posloupnosti vybrat dvě podposloupnosti s různými limitami, pak limita původní posloupnosti neexistuje.

## Poznámka Anki 1647364121582

Karty Anki: 1647364121582
GUID: l$R?Cd3Q+~; štítky: bi-ma1::p05.

### Otázka (Front)

Jaké platí vztahy limity a \(\mathcal{O}\), \(o\)?

### Odpověď (Back)

Pokud \(\displaystyle \lim_{x \to a} \bigg| \frac{f(x)}{g(x)} \bigg| \in \mathbb{R}\), pak \(f(x) = \mathcal{O}(g(x))\) pro \(x \to a\).
Pokud \(\displaystyle \lim_{x \to a} \bigg| \frac{f(x)}{g(x)} \bigg| = 0\), pak \(f(x) = o(g(x))\) pro \(x \to a\).

## Poznámka Anki 1647364262656

Karty Anki: 1647364262656
GUID: l)!<W.D0*7; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Definujte konvergentní a divergentní posloupnosti.

### Odpověď (Back)

Posloupnost \((a_{n})_{n=1}^{\infty}\) se nazývá konvergentní, právě když její limita existuje a je prvkem \(\mathbb{R}\). V ostatních případech ji nazýváme divergentní.

## Poznámka Anki 1647364305721

Karty Anki: 1647364305721
GUID: yne{+YGljh; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte Bolzano-Weierstrassovu větu.

### Odpověď (Back)

Každá omezená číselná posloupnost má hromadný bod ležící v \(\mathbb{R}\).

## Poznámka Anki 1647364344768

Karty Anki: 1647364344768
GUID: MK}wE8cqe=; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte větu o limitě monotonní posloupnosti.

### Odpověď (Back)

Každá reálná monotonní posloupnost má limitu. Tato limita je konečná, právě když je daná posloupnost omezená.

## Poznámka Anki 1647364463566

Karty Anki: 1647364463567
GUID: bvkTK;,X.z; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte Bolzano-Cauchyho větu.

### Odpověď (Back)

Posloupnost \((a_{n})_{n=1}^{\infty}\) je konvergentní, právě když pro každé \(\varepsilon > 0\) existuje \(N \in \mathbb{N}\) takové, že pro každé \(n, m > N\) je \(| a_n - a_m | < \varepsilon\).

## Poznámka Anki 1647365288019

Karty Anki: 1647365288019
GUID: Q<P^*n0mP}; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte větu o limitě sevřené posloupnosti.

### Odpověď (Back)

Mějme tři posloupnosti \((a_{n})_{n=1}^{\infty}\), \((b_{n})_{n=1}^{\infty}\), \((c_{n})_{n=1}^{\infty}\) a nechť platí

- exsistuje \(N \in \mathbb{N}\) takové, že pro všechna \(n \geq N\) platí nerovnosti \(a_n \leq b_n \leq c_n\)
- exsitují limity posloupností , \((a_{n})_{n=1}^{\infty}\) a \((c_{n})_{n=1}^{\infty}\) a jsou rovné \(b \in \overline{\mathbb{R}}\).
Potom existuje i limita posloupnosti \((b_n)_{n=1}^{\infty}\) a je také rovna \(b\).

## Poznámka Anki 1647365516375

Karty Anki: 1647365516375
GUID: t}OKy:u@Sq; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte větu o limitě složené funkce.

### Odpověď (Back)

Nechť \(f\) a \(g\) jsou funkce, \(a\), \(b\), \(c\) jsou prvky \(\overline{\mathbb{R}}\) a platí čtyři podmínky

- \(\lim \limits_{x \to a} g(x) = b\),

- \(\lim \limits_{x \to b} f(x) = c\),

- bod \(a\) je hromadným bodem množiny \(D_{f \circ g}\),
- buď \((\exists U_a)(\forall x \in U_a \cap D_g \smallsetminus \{a\})(g(x) \neq b)\) nebo \(b \in D_f\) a \(f(b) = c\).
Potom \(\lim \limits_{x \to a}(f \circ g)(x) = c\).

## Poznámka Anki 1647365742599

Karty Anki: 1647365742600
GUID: Q[g4ckv#!+; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte větu o podílovém kritériu posloupnosti.

### Odpověď (Back)

Buď \((a_{n})_{n=1}^{\infty}\) posloupnost kladných čísel a nechť existuje limita
\[\lim \limits_{n \to \infty} \frac{a_{n + 1}}{a_n},\]označme její hodnotu symbolem \(q\). Potom

- pokud \(q < 1\), pak \(\lim \limits_{n \to \infty} a_n = 0\)
- pokud \(q > 1\), pak \(\lim \limits_{n \to \infty} a_n = + \infty\).

## Poznámka Anki 1654419249512

Karty Anki: 1654419249512
GUID: b:[&#sh/7,; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte a dokažte větu o vytlačení do nekonečna.

### Odpověď (Back)

Mějme dvě funkce \(f\), \(g\) a bod \(a \in \overline{\mathbb{R}}\), Nechť existuje okolí \(U_a\) bodu \(a\) splňující

1. \(D_f \cap U_a = D_g \cap U_a\), tuto množinu označme \(M\),

2. \(a\) je hromadným bodem množiny \(M\),

3. pro všechna \(x \in M \smallsetminus \{a\}\) platí \(f(x) \leq g(x)\).
Potom platí následující dvě tvrzení:

- Pokud \(\lim_a f = +\infty\), potom i \(\lim_a g = +\infty\).
- Pokud \(\lim_a g = -\infty\), potom i \(\lim_a f = -\infty\).
**Důkaz v připadě \(+\infty\):**
Vezměme okolí \(U_{+\infty} = (c, +\infty)\). Protože \(\lim_a f = +\infty\), máme pro toto \(c\) k dispozici jisté okolí \(U_a\) takové, že pro všechna \(x \in (U_a \cap M) \smallsetminus \{a\}\) platí \(f(x) > c\). Vezmeme-li proto nyní libovolné \(x \in (U_a \cap M) \smallsetminus \{a\}\), pak platí i \(c < f(x) \leq g(x)\) a \(g(x) \in (c, +\infty)\). Tudíž \(\lim_a g = +\infty\).

## Poznámka Anki 1654436832246

Karty Anki: 1654436832247
GUID: xH-r?2,l0x; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte větu o limitě součtu, součinu a podílu funkcí.

### Odpověď (Back)

Mějme funkce \(f : A \to \mathbb R\), \(g : B \to \mathbb R\) a hromadný bod \(a\) množiny \(A \cap B\). Pokud existují \(\displaystyle \lim_{x \to a} f(x)\) a \(\displaystyle \lim_{x \to a} g(x)\), platí\[\begin{matrix}
\displaystyle \lim_{x \to a} \big( f(x) + g(x) \big) = \displaystyle \lim_{x \to a} f(x) + \displaystyle \lim_{x \to a} g(x), \\
\displaystyle \lim_{x \to a} \big( f(x) \cdot g(x) \big) = \displaystyle \lim_{x \to a} f(x) \cdot \displaystyle \lim_{x \to a} g(x), \\
\displaystyle \lim_{x \to a} \frac{f(x)}{g(x)} = \frac {\displaystyle \lim_{x \to a} f(x)}{\displaystyle \lim_{x \to a} g(x)},
\end{matrix}\]jsou-li algebraické operace na pravých stranách definovány v \(\overline{\mathbb R}\).

### Doplňující pole (Extra)

Ze vztahu pro limitu součinu funkcí plyne vztah pro limitu konstantního násobku funkce. Pro \(c \in \mathbb R\) platí\[\displaystyle \lim_{x \to a} c \cdot f(x) = c \cdot \displaystyle \lim_{x \to a} f(x).\]

## Poznámka Anki 1655159842697

Karty Anki: 1655159842697
GUID: p!Ff!BoTe=; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte větu o vztahu podposloupností a hromadných bodů posloupnosti.

### Odpověď (Back)

Bod \(\alpha \in \overline{ \mathbb{ R } }\) je hromadným bodem posloupnosti \(( a_n )_{ n = 1 }^{ \infty }\), právě když existuje vybraná posloupnost \(( a_{ k_n } )_{ n = 1 }^{ \infty }\) mající limitu \(\alpha \in \overline{ \mathbb{ R } }\).

## Poznámka Anki 1716131223675

Karty Anki: 1716131223675
GUID: u<xwd82Ew!; štítky: bi-ma1::p05 bi-spol::13.

### Otázka (Front)

Vyslovte větu o limitě sevřené funkce.

### Odpověď (Back)

Mějme tři funkce \(f\), \(g\) a \(h\) a bod \(a \in \overline{\mathbb R}\). Nechť existuje okolí \(U_a\) bodu \(a\) splňující

- \(D_f \cap U_a = D_g \cap U_a = D_h \cap U_a\), označme tuto množinu \(M\),

- \(a\) je hromadným bodem množiny \(M\),

- pro všechna \(x \in M \smallsetminus \{ a \}\) platí nerovnosti \(f(x) \leq g(x) \leq h(x)\).

Nechť dále existují limity funkcí \(f\) a \(h\) v bodě \(a\) mající společnou hodnotu \(b \in \overline{\mathbb R}\), tj.

\[\displaystyle \lim_{x \to a} f(x) = \displaystyle \lim_{x \to a} h(x) = b.\]Potom existuje i limita \(g\) v bodě \(a\) a je rovna \(b\), tj. \(\displaystyle \lim_{x \to a} g(x) = b\).

