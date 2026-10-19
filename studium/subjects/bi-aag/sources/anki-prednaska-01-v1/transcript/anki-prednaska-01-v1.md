# BI-AAG – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aag/BI-AAG.apkg; APKG SHA-256 0383847389324f3b83b349363b7ad16a6bf91673c90b7a96ed1a57b25a85f8af. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b9cda20d5a5a9d1ff47d4e1fc58b10ed3ac7a37c72c6c1431cc7cb67e2ca10c.
Původní balíčky: BI-AAG
Rozsah: 51 poznámek, 51 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1663830474636

Karty Anki: 1663830474636
GUID: F]mc{z?Wp!; štítky: bi-aag::p01.

### Otázka (Front)

Definujte pojem abeceda.

### Odpověď (Back)

Abeceda (obvykle značíme \(\Sigma\)) je konečná množina prvků, které nazýváme symboly abecedy.

## Poznámka Anki 1663830576483

Karty Anki: 1663830576483
GUID: md.<F;qe1Q; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663830576483: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte velikost abecedy.

### Odpověď (Back)

Velikost abecedy \(\Sigma\) značíme \(|\Sigma|\) a tato hodnota odpovídá počtu symbolů v \(\Sigma\).

## Poznámka Anki 1663830619581

Karty Anki: 1663830619582
GUID: mi4)uh(zZK; štítky: bi-aag::p01.

### Otázka (Front)

Definujte řetězec nad abecedou.

### Odpověď (Back)

Nechť \(\Sigma\) je abeceda. Pak řetězec nad abecedou \(\Sigma\) je konečná posloupnost symbolů ze \(\Sigma\).

## Poznámka Anki 1663830707542

Karty Anki: 1663830707542
GUID: pi7w+^V316; štítky: bi-aag::p01.

### Otázka (Front)

Co reprezentuje znak \(\varepsilon\)?

### Odpověď (Back)

Prázdnou posloupnost symbolů -prázdný řetězec.

### Doplňující pole (Extra)

Tento znak využíváme pouze k vyznačení prázdného řetězce. Tedy nikdy není součástí žádné abecedy. Jinými slovy vždy platí, že \(\varepsilon \notin \Sigma\).

## Poznámka Anki 1663830818681

Karty Anki: 1663830818682
GUID: d5zyJ7Y;UD; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663830818682: v původním balíčku pozastavená karta.

### Otázka (Front)

Nechť \(\Sigma\) je abeceda. Co značí \(\Sigma^*\) a \(\Sigma^+\)? Jaký vzájemný vztah mají \(\Sigma^*\) a \(\Sigma^+\)?

### Odpověď (Back)

- \(\Sigma^*\) - množina všech možných řetězců (včetně prázdného) nad \(\Sigma\)

- \(\Sigma^+\) - množina všech neprázdných řetězců nad \(\Sigma\)

### Doplňující pole (Extra)

Tedy platí, že \(\Sigma^* = \Sigma^+ \cup \{\varepsilon\}\).

## Poznámka Anki 1663831030681

Karty Anki: 1663831030681
GUID: yHg5(24O72; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663831030681: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte pojem délka řetězce.

### Odpověď (Back)

Délka řetězce \(x\), značíme \(|x|\), je počet symbolů řetězce. Délka prázdného řetězce se rovná nule, tj. \(|\varepsilon| = 0\).

## Poznámka Anki 1663831081631

Karty Anki: 1663831081631
GUID: fxLS((VNJ1; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663831081631: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci reverze řetězce.

### Odpověď (Back)

Mějme řetězec \(w = a_1 \dots a_n\), kde \(n \in \mathbb{N}\). Reverze řetězce \(w\) je řetězec \(w^\mathrm{R} = a_n \dots a_1\). Reverze prázdného řetězce je prázdný řetězec - tj. pokud \(w = \varepsilon\), pak \(w^\mathrm{R} = \varepsilon\).

### Doplňující pole (Extra)

Řetězec \(w^\mathrm{R}\) je tedy řetězec \(w\) zapsaný zprava doleva.

## Poznámka Anki 1663831337521

Karty Anki: 1663831337521
GUID: LzkPAPpK{2; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663831337521: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci zřetězení řetězců.

### Odpověď (Back)

Mějme řetězce \(x = x_1 x_2 \dots x_n\) a \(y = y_1 y_2 \dots y_m\). Výsledkem operace zřetězení řetězce \(x\) s řetězcem \(y\), značíme \(x \cdot y\) nebo \(xy\), je řetězec \(x_1 x_2 \dots x_n y_1 y_2 \dots y_m\).

### Doplňující pole (Extra)

Zřetězení je tedy operace spojující dva řetězce. Připojením řetězce \(y\) za řetězec \(x\) získáme řetězec \(xy\).

## Poznámka Anki 1663831384472

Karty Anki: 1663831384472
GUID: bL;xN~j1PG; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663831384472: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké vlastnosti má operace zřetězení řetězců?

### Odpověď (Back)

U operace zřetězení dvou řetězců nad abecedou \(\Sigma\) můžeme pozorovat následující vlastnosti:

- Neutrálním prvkem operace zřetězení je prázdný řetězec. Tedy \(\forall x \in \Sigma^*: x \varepsilon = \varepsilon x = x\). 
- Operace zřetězení je asociativní. Tedy \(\forall x,y,z \in \Sigma^*: x(yz) = (xy)z\). 
- Pro \(|\Sigma| \geq 2\) není operace zřetězení komutativní. Tedy \(\exists x,y \in \Sigma^*:xy \neq yx\).

## Poznámka Anki 1663831481265

Karty Anki: 1663831481265
GUID: t1F|]IJBpZ; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663831481265: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci mocnina řetězce.

### Odpověď (Back)

Mocnina řetězce \(w \in \Sigma^*\) je pro \(\forall n\in\mathbb{N}\) definovaná následovně:

- \(w^0  = \varepsilon\)
- \(w^n = w \cdot w^{n-1}\)
Mocnina řetězce je tedy opakované zřetězení.

### Doplňující pole (Extra)

Pokud \(|w| = 1\), pak \(w\) můžeme namísto řetězce interpretovat jako symbol a mocninu \(w^n\) chápat jako \(n\) výskytů daného symbolu. Ať už \(w\) budeme považovat za symbol nebo řetězec, v obou případech bude ale výsledek shodný.

## Poznámka Anki 1663841716221

Karty Anki: 1663841716221
GUID: KDU!8:&U#B; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663841716221: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte předponu (prefix) řetězce.

### Odpověď (Back)

Pokud \(w \in \Sigma^*\), pak řekneme, že \(p \in \Sigma^*\) je předponou \(w\) právě tehdy, když \(\exists x \in \Sigma^*\) tak, že \(w = px\).

### Doplňující pole (Extra)

Předpona řetězce \(w\) je tedy jeho libovolná úvodní souvislá posloupnost symbolů (včetně prázdné posloupnosti).

## Poznámka Anki 1663841779899

Karty Anki: 1663841779899
GUID: bL-/q&paZ/; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663841779899: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte příponu (suffix)** **řetězce.

### Odpověď (Back)

Pokud \(w \in \Sigma^*\), pak řekneme, že \(p \in \Sigma^*\) je příponou \(w\) právě tehdy, když \(\exists x \in \Sigma^*\) tak, že \(w = xp\).

### Doplňující pole (Extra)

Přípona řetězce \(w\) je tedy jeho libovolná závěrečná souvislá posloupnost symbolů (včetně prázdné posloupnosti).

## Poznámka Anki 1663841834295

Karty Anki: 1663841834296
GUID: bvd9a/{am1; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663841834296: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte podřetězec (substring) řetězce.

### Odpověď (Back)

Pokud \(w \in \Sigma^*\), pak řekneme, že \(x \in \Sigma^*\) je podřetězcem \(w\) právě tehdy, když \(\exists u,v \in \Sigma^*\) tak, že \(w = uxv\).

### Doplňující pole (Extra)

Podřetězec řetězce \(w\) je tedy nějaká souvislá posloupnost symbolů uvnitř \(w\) (včetně prázdné posloupnosti).

## Poznámka Anki 1663841876957

Karty Anki: 1663841876957
GUID: xu(7o7lb#P; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663841876957: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte podsekvenci (subsequence) řetězce.

### Odpověď (Back)

Podsekvence řetězce \(w\) je libovolný řetězec \(x\), který vznikne vynecháním \(0\) či více symbolů z \(w\). Prázdný řetězec (tj. vynechání všech symbolů z \(w\)) je též podsekvencí řetězce \(w\).

## Poznámka Anki 1663842003371

Karty Anki: 1663842003371
GUID: pBeu(E3n.9; štítky: bi-aag::p01.

### Otázka (Front)

Definujte formální jazyk nad abecedou.

### Odpověď (Back)

Formální jazyk nad abecedou \(\Sigma\) (obvykle značíme \(L\)) je libovolná podmnožina množiny všech možných řetězců nad \(\Sigma\) (tj. \(L \subseteq \Sigma^*\)).

### Doplňující pole (Extra)

Jednoduše řečeno tedy formální jazyk není nic jiného než množina řetězců.

## Poznámka Anki 1663842041338

Karty Anki: 1663842041338
GUID: v`4gbf#7^q; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842041338: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte velikost jazyka.

### Odpověď (Back)

Velikost jazyka je počet (různých) řetězců, které daný jazyk obsahuje.Velikost jazyka \(L \subseteq \Sigma^*\) značíme \(|L|\).

## Poznámka Anki 1663842106308

Karty Anki: 1663842106308
GUID: LLhv^{bEje; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842106308: v původním balíčku pozastavená karta.

### Otázka (Front)

Kdy o jazyce řekneme, že je (ne)konečný?

### Odpověď (Back)

Pokud jazyk obsahuje konečné množství řetězců, pak jej nazýváme konečným. V opačném případě jej nazýváme nekonečným.

### Doplňující pole (Extra)

Konečným jazykem je například i jazyk \(L = \emptyset\), který neobsahuje žádný řetězec. Nazýváme jej prázdným jazykem a jeho velikost je rovna nule.

## Poznámka Anki 1663842170278

Karty Anki: 1663842170279
GUID: l^D;YaJVJ$; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842170279: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci sjednocení jazyků.

### Odpověď (Back)

Mějme jazyky \(L_1\) a \(L_2\). Sjednocení jazyků \(L_1\) a \(L_2\) značíme jako \(L_1 \cup L_2\) a definujeme následovně:
\[L_1 \cup L_2 = \{w : w \in L_1 \vee w \in L_2\}\]

## Poznámka Anki 1663842194397

Karty Anki: 1663842194397
GUID: Ow=ZsAqJDE; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842194397: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci průnik jazyků.

### Odpověď (Back)

Mějme jazyky \(L_1\) a \(L_2\). Průnik jazyků \(L_1\) a \(L_2\) značíme jako \(L_1 \cap L_2\) a definujeme následovně:
\[L_1 \cap L_2 = \{w : w \in L_1 \wedge w \in L_2\}\]

## Poznámka Anki 1663842222093

Karty Anki: 1663842222093
GUID: r5+|k3e[<^; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842222093: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci rozdíl jazyků.

### Odpověď (Back)

Mějme abecedu \(\Sigma\) a jazyky \(L_1, L_2  \subseteq \Sigma^*\). Rozdíl jazyků \(L_1\) a \(L_2\) značíme jako \(L_1 \setminus L_2\) a definujeme následovně:
\[L_1 \setminus L_2 = \{w : w \in L_1 \land w \notin L_2\}\]

## Poznámka Anki 1663842245143

Karty Anki: 1663842245143
GUID: QylQ{9j2CO; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842245143: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci doplněk jazyka.

### Odpověď (Back)

Mějme abecedu \(\Sigma\) a jazyk \(L \subseteq \Sigma^*\).Doplněk jazyka \(L\) značíme \(\overline{L}\) a definujeme následovně: \[\overline{L} = \{w : w \in \Sigma^* \wedge w \notin L\} = \Sigma^* \setminus L\]

## Poznámka Anki 1663842294330

Karty Anki: 1663842294330
GUID: Cqee<)Mu%-; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842294330: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci zřetězení (součin) jazyků.

### Odpověď (Back)

Mějme abecedu \(\Sigma\) a jazyky \(L_1, L_2 \subseteq \Sigma^*\). Součin jazyků \(L_1\) a \(L_2\) značíme jako \(L_1 \cdot L_2\) a definujeme následovně:
\[L_1 \cdot L_2 = \{w : w = x \cdot y \land x \in L_1 \land y \in L_2\}\]

## Poznámka Anki 1663842328568

Karty Anki: 1663842328568
GUID: G:*EwSF|$2; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842328568: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci mocnina jazyka.

### Odpověď (Back)

Mějme abecedu \(\Sigma\) a jazyk \(L \subseteq \Sigma^*\), pak \(n\)-tou mocninu jazyka \(L\) značíme \(L^n\) a definujeme následovně:
\[L^n = 
\begin{cases}
\{ \varepsilon \} & \text{pokud } n = 0 \\
L \cdot L^{n-1} & \text{pokud } n \in \mathbb{N}
\end{cases}\]

### Doplňující pole (Extra)

Mocnina jazyka je tedy jeho opakované zřetězení sama se sebou. Tedy \(L^n = \underbrace{L \cdot L \cdot \dots \cdot L}_{n}\), přičemž \(L^0 = \{ \varepsilon \}\) pro libovolný jazyk \(L\).

## Poznámka Anki 1663842484450

Karty Anki: 1663842484451
GUID: H1VqaDu^zY; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842484451: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci iterace (Kleen star) jazyka.

### Odpověď (Back)

Mějme abecedu \(\Sigma\) a jazyk \(L \subseteq \Sigma^*\). Iteraci jazyka \(L\) značíme \(L^*\) a definujeme následovně:
\[L^* = \bigcup\limits_{n \in \mathbb{N}_0}{L^n}\]

## Poznámka Anki 1663842507446

Karty Anki: 1663842507446
GUID: n5-]/J1ej&; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842507446: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte operaci pozitivní iterace (Kleen plus) jazyka.

### Odpověď (Back)

Mějme abecedu \(\Sigma\) a jazyk \(L \subseteq \Sigma^*\). Pozitivní iteraci jazyka \(L\) značíme \(L^+\) a definujeme následovně:
\[L^+ = \bigcup\limits_{n \in \mathbb{N}}{L^n}\]

## Poznámka Anki 1663842560755

Karty Anki: 1663842560755
GUID: xe9Y$xtH[=; štítky: bi-aag::p01 bi-spol::01.

### Otázka (Front)

Definujte pojem gramatika.

### Odpověď (Back)

Gramatika \(G\) je uspořádaná čtveřice \(G = (N, \Sigma, P, S)\), kde

- \(N\) je konečná neprázdná množina neterminálních symbolů,
- \(\Sigma\) (nebo někdy \(T\)) je konečná množina terminálních symbolů (platí \(N \cap \Sigma = \emptyset\)),
- \(P\) je konečná množina přepisovacích pravidel ve tvaru \(\alpha A \beta \to \gamma\), kde \(\alpha, \beta, \gamma \in (N \cup \Sigma)^*\) a \(A \in N\),
- \(S\) je počáteční (startovací) neterminální symbol gramatiky (\(S \in N\)).

## Poznámka Anki 1663842613899

Karty Anki: 1663842613899
GUID: t98dq/Jo?L; štítky: bi-aag::p01 bi-spol::02.

### Otázka (Front)

Definujte pojem přímá derivace.

### Odpověď (Back)

Mějme gramatiku \(G = (N, \Sigma, P, S)\) obsahující pravidlo \(\alpha \to \beta\), kde \(\alpha, \beta \in (N \cup \Sigma)^*\) a \(\alpha\) obsahuje alespoň jeden neterminální symbol. Dále mějme \(\gamma, \delta \in (N \cup \Sigma)^*\), pak \(\gamma \alpha \delta \Rightarrow \gamma \beta \delta\) nazveme přímou derivací (\(\gamma \alpha \delta\) přímo derivuje \(\gamma \beta \delta\)).

### Doplňující pole (Extra)

Jedna posloupnost symbolů nad abecedou \((N \cup \Sigma)\) tedy v gramatice přímo derivuje druhou, pokud na přeměnu první na druhou bylo použito právě jedno pravidlo dané gramatiky.

## Poznámka Anki 1663842654075

Karty Anki: 1663842654075
GUID: q^jMPwFifj; štítky: bi-aag::p01 bi-spol::02.

Metadata původního zdroje pro kartu 1663842654075: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte pro gramatiky pojem derivace.

### Odpověď (Back)

Derivací nazveme libovolnou posloupnost přímých derivací.

- \(\alpha \Rightarrow^k \beta\) (posloupnost přímých derivací délky \(k \in \mathbb{N}_0\)) - \(\alpha\) generuje \(\beta\) po \(k\) krocích
- \(\alpha \Rightarrow^+ \beta\), tj. \(\alpha \Rightarrow^i \beta, i \in \mathbb{N}\) (tranzitivní uzávěr relace \(\Rightarrow\)) - \(\alpha\) generuje po nenulovém počtu kroků (po nenulovém počtu přímých derivací) \(\beta\)
- \(\alpha \Rightarrow^* \beta\), tj. \(\alpha \Rightarrow^i \beta, i \in \mathbb{N}_0\) (reflexivně tranzitivní uzávěr relace \(\Rightarrow\)) \(\alpha\) generuje po libovolném (i nulovém) počtu kroků (po libovolném i nulovém počtu přímých derivací) \(\beta\)

## Poznámka Anki 1663842834290

Karty Anki: 1663842834290
GUID: w-/vm9bXYu; štítky: bi-aag::p01 bi-spol::02.

### Otázka (Front)

Definujte pojem větná forma.

### Odpověď (Back)

Nechť \(G = (N, \Sigma, P, S)\), pak \(\alpha \in (N \cup \Sigma)^*\) nazveme větnou formou právě tehdy, když \(\exists (S \Rightarrow^* \alpha)\).

### Doplňující pole (Extra)

Větná forma je tedy libovolný řetězec nad abecedou \((N \cup \Sigma)\) takový, že jej lze získat nějakou derivací ze startovacího neterminálu gramatiky.

## Poznámka Anki 1663842879502

Karty Anki: 1663842879502
GUID: J8}=%8LjT!; štítky: bi-aag::p01 bi-spol::02.

### Otázka (Front)

Definujte pojem věta.

### Odpověď (Back)

Věta je taková větná forma, která neobsahuje neterminální symbol.

### Doplňující pole (Extra)

Věta je tedy vlastně konečným produktem derivace gramatiky a reprezentuje nějaký řetězec nad abecedou \(\Sigma\), jenž náleží do jazyka, který daná gramatika generuje.

## Poznámka Anki 1663842920510

Karty Anki: 1663842920510
GUID: FQkcnnVAL_; štítky: bi-aag::p01.

### Otázka (Front)

Definujte pojem jazyk generovaný gramatikou.

### Odpověď (Back)

Nechť \(G = (N, \Sigma, P, S)\), pak jazyk generovaný gramatikou \(G\) definujeme jako \(L(G) = \{ w : w \in \Sigma^* \land \exists (S \Rightarrow^* w ) \}\).

### Doplňující pole (Extra)

Jazyk \(L(G)\) je tedy množina všech vět generovaných gramatikou \(G\).

## Poznámka Anki 1663842949920

Karty Anki: 1663842949920
GUID: cTj`^q@sZt; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842949920: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte pojem ekvivalentní gramatiky.

### Odpověď (Back)

Dvě gramatiky \(G_1, G_2\) jsou ekvivalentní právě tehdy, když \(L(G_1) = L(G_2)\).

## Poznámka Anki 1663842980490

Karty Anki: 1663842980491
GUID: oA)nWj4.0,; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663842980491: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte pojem (ne)zkracující gramatika.

### Odpověď (Back)

Mějme gramatiku \(G = (N, \Sigma, P, S)\). Tuto gramatiku nazvemenezkracující právě tehdy, když \(\forall (\alpha \to \beta) \in P: |\alpha| \leq |\beta|\). Jediné pravidlo, které může tento předpis porušovat, je pravidlo \(S \to \varepsilon\), přičemž \(S\) se poté nesmí vyskytovat na pravé straně žádného pravidla z \(P\). V opačném případě nazveme gramatiku zkracující.

## Poznámka Anki 1663843070543

Karty Anki: 1663843070543
GUID: dE)gVfQEc8; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663843070543: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte pojem \(\varepsilon\)-pravidlo v gramatice.

### Odpověď (Back)

Mějme gramatiku \(G = (N, \Sigma, P, S)\), pak pravidlo tvaru \(A \rightarrow \varepsilon\), kde \(A \in N\) nazveme \(\varepsilon\)-pravidlem.

## Poznámka Anki 1663843112335

Karty Anki: 1663843112335
GUID: jsy1^1,O:x; štítky: bi-aag::p01 bi-spol::02.

### Otázka (Front)

Jaké typy gramatik vymezuje Chomského klasifikace?

### Odpověď (Back)

- regulární gramatika
- bezkontextová gramatika
- kontextová gramatika
- neomezená gramatika

## Poznámka Anki 1663843225658

Karty Anki: 1663843225658
GUID: O2E#ZH,#*B; štítky: bi-aag::p01 bi-spol::01.

### Otázka (Front)

Definujte regulární gramatiku.

### Odpověď (Back)

Regulární gramatika (RG, gramatika typu 3) je taková gramatika, která má pouze pravidla tvaru:

- \(A \to a\),
- \(A \to aB\),

- \(S \to \varepsilon\), pokud se počáteční neterminál \(S\) nevyskytuje na pravé straně žádného pravidla,
kde \(a \in \Sigma\) a \(A,B \in N\).

## Poznámka Anki 1663843270799

Karty Anki: 1663843270799
GUID: C[+v$LbG@6; štítky: bi-aag::p01 bi-spol::02.

### Otázka (Front)

Definujte bezkontextovou gramatiku.

### Odpověď (Back)

Bezkontextová gramatika (BG, gramatika typu 2) je taková gramatika, která má pouze pravidla tvaru:

- \(A \to \alpha\), kde \(\alpha \in (N \cup \Sigma)^*\) a \(A \in N\).

## Poznámka Anki 1663843295764

Karty Anki: 1663843295764
GUID: wgd.0P[Ah&; štítky: bi-aag::p01.

### Otázka (Front)

Definujte kontextovou gramatiku.

### Odpověď (Back)

Kontextová gramatika (KG, gramatika typu 1) je taková gramatika, která má pouze pravidla tvaru:

- \(\gamma A \delta \to \gamma \alpha \delta\), kde \(\gamma, \delta \in (N \cup \Sigma)^*\), \(A \in N\) a \(\alpha \in (N \cup \Sigma)^+\),
- \(S \to \varepsilon\), pokud se počáteční neterminál \(S\) nevyskytuje na pravé straně žádného pravidla

## Poznámka Anki 1663843341296

Karty Anki: 1663843341296
GUID: K2FDICjQ&j; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663843341296: v původním balíčku pozastavená karta.

### Otázka (Front)

Které typy gramatik z Chomského klasifikace jsou vždy nezkracující?

### Odpověď (Back)

Každá regulární a kontextová gramatika je nezkracující. Obráceně toto tvrzení neplatí - tedy ne každá nezkracující gramatika je regulární či kontextová.

## Poznámka Anki 1663843379514

Karty Anki: 1663843379514
GUID: s*I~m|C,+S; štítky: bi-aag::p01.

### Otázka (Front)

Definujte neomezenou gramatiku.

### Odpověď (Back)

Neomezená gramatika (NG, gramatika typu 0) je taková gramatika, která má pouze pravidla tvaru:

-  \(\alpha A \beta \to \gamma\), kde \(\alpha, \beta, \gamma \in (N \cup \Sigma)^*\) a \(A \in N\).

## Poznámka Anki 1663843522185

Karty Anki: 1663843522185
GUID: OoNM~dYV3`; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663843522185: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký je vzájemný vztah mezi jednotlivými typy gramatik, které definuje Chomského klasifikace?

### Odpověď (Back)

- Regulární gramatika je vždy zároveň bezkontextová, kontextová a neomezená.
- Bezkontextová gramatika je vždy neomezená, může ale nemusí být i kontextová.
- Kontextová gramatika je vždy zároveň neomezená.

## Poznámka Anki 1663843675178

Karty Anki: 1663843675178
GUID: e4Kk5TJ4K]; štítky: bi-aag::p01.

### Otázka (Front)

Který výpočetní model rozpoznává právě třídu rekurzivně spočetných jazyků?

### Odpověď (Back)

Turingův stroj

## Poznámka Anki 1663843690701

Karty Anki: 1663843690701
GUID: PJ!#di9{iG; štítky: bi-aag::p01.

### Otázka (Front)

Který výpočetní model rozpoznává právě třídu kontextových jazyků?

### Odpověď (Back)

lineárně omezený Turingův stroj

## Poznámka Anki 1663843703536

Karty Anki: 1663843703536
GUID: fH{@v0Bl,i; štítky: bi-aag::p01 bi-spol::02.

### Otázka (Front)

Který výpočetní model rozpoznává právě třídu bezkontextových jazyků?

### Odpověď (Back)

zásobníkový automat

## Poznámka Anki 1663843721758

Karty Anki: 1663843721758
GUID: umkyJm^2hv; štítky: bi-aag::p01 bi-spol::01.

### Otázka (Front)

Který výpočetní model rozpoznává právě třídu regulárních jazyků?

### Odpověď (Back)

konečný automat

## Poznámka Anki 1663843872124

Karty Anki: 1663843872124
GUID: oZO0CJ:T]a; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663843872124: v původním balíčku pozastavená karta.

### Otázka (Front)

Mějme nějakou jednu třídu jazyků Chomského hierarchie a jednu z operací pro jazyky. Kdy řekneme, že je daná třída pro danou operaci uzavřená?

### Odpověď (Back)

Provedeme-li se dvěma libovolnými jazyky z dané třídy danou operaci a výsledkem bude opět jazyk z této třídy, řekneme, že tato třída je pro danou operaci uzavřená.

## Poznámka Anki 1663844046226

Karty Anki: 1663844046226
GUID: bDgv%[7j1l; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663844046226: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus pro sjednocení bezkontextových gramatik.

### Odpověď (Back)

**Vstup: **Bezkontextová gramatika \(G_1 = (N_1, \Sigma, P_1, S_1)\) a \(G_2 = (N_2, \Sigma, P_2, S_2)\), přičemž \(N_1 \cap N_2 = \emptyset\).

**Výstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\) taková, že \(L(G) = L(G_1) \cup L(G_2)\).

**Postup:**

1. \(N = N_1 \cup N_2 \cup \set{S}\), kde \(S \notin (N_1 \cup N_2)\).

2. \(S\) je startovací neterminál výsledné bezkontextové gramatiky \(G\).
3. \(P = P_1 \cup P_2 \cup \set{S \to S_1 | S_2}\).

## Poznámka Anki 1663844089905

Karty Anki: 1663844089905
GUID: gJ@y8cVHNj; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663844089905: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus pro zřetězení (součin) bezkontextových gramatik.

### Odpověď (Back)

**Vstup: **bezkontextová gramatika \(G_1 = (N_1, \Sigma, P_1, S_1)\) a \(G_2 = (N_2, \Sigma, P_2, S_2)\), přičemž \(N_1 \cap N_2 = \emptyset\).

**Výstup:** bezkontextová gramatika \(G = (N, \Sigma, P, S)\) taková, že \(L(G) = L(G_1) \cdot L(G_2)\).

**Postup:**

1. \(N = N_1 \cup N_2 \cup \set{S}\), kde \(S \notin (N_1 \cup N_2)\).

2. \(S\) je startovací neterminál výsledné bezkontextové gramatiky \(G\).
3. \(P = P_1 \cup P_2 \cup \set{S \to S_1S_2}\).

## Poznámka Anki 1663844125391

Karty Anki: 1663844125391
GUID: tsC.a]m<3E; štítky: bi-aag::p01.

Metadata původního zdroje pro kartu 1663844125391: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus iterace bezkontextových gramatik.

### Odpověď (Back)

**Vstup: **bezkontextová gramatika \(G_1 = (N_1, \Sigma, P_1, S_1)\).

**Výstup:** bezkontextová gramatika \(G = (N, \Sigma, P, S)\) taková, že \(L(G) = L(G_1)^*\).

**Postup:**

1. \(N = N_1 \cup \set{S}\), kde \(S \notin N_1\).

2. \(S\) je startovací neterminál výsledné bezkontextové gramatiky \(G\).
3. \(P = P_1 \cup \set{S \to \varepsilon | S_1S}\).

## Poznámka Anki 1663844303990

Karty Anki: 1663844303990
GUID: E]F|b+$7X0; štítky: bi-aag::p01 bi-spol::02.

Metadata původního zdroje pro kartu 1663844303990: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte pojem derivační strom.

### Odpověď (Back)

Uvažujme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\). Derivační strom je zakořeněný uspořádaný strom (tj. strom, který má kořen a záleží na pořadí potomků) s následujícími vlastnostmi:

- Každý vrchol je ohodnocen právě jedním neterminálním/terminálním symbolem, nebo \(\varepsilon\).
- Kořen derivačního stromu je vždy ohodnocen počátečním neterminálem \(S\).
- Pokud má vrchol alespoň jednoho potomka, je ohodnocen neterminálním symbolem.
- Pokud je vrchol ohodnocen neterminálním symbolem \(A \in N\) a jeho první potomek je ohodnocen \(\alpha_1\), druhý potomek je ohodnocen \(\alpha_2\) až po \(n\)-tého potomka, který je ohodnocen \(\alpha_n\), pak v \(G\) existuje pravidlo \(A \to \alpha_1 \alpha_2 \dots \alpha_n\). 
- Listy derivačního stromu tvoří zleva doprava větnou formu (případně větu) v gramatice \(G\), o které řekneme, že je výsledkem tohoto derivačního stromu.

## Poznámka Anki 1664616350344

Karty Anki: 1664616350344
GUID: EZs(vqM6ju; štítky: bi-aag::p01 bi-spol::01.

Metadata původního zdroje pro kartu 1664616350344: v původním balíčku pozastavená karta.

### Otázka (Front)

Do jaké třídy můžeme s jistotou zařadit konečné jazyky?

### Odpověď (Back)

Konečné jazyky jsou vždy regulární.

