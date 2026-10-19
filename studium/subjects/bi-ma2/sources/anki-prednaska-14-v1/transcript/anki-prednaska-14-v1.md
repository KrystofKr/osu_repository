# BI-MA2 – Přednáška 14

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 29 poznámek, 29 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1668435508485

Karty Anki: 1668435508486
GUID: B|^1yT)4Ye; štítky: bi-ma2::p14 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Definujte okolí bodu \(\mathbf a \in \mathbb{R}^n\).

### Odpověď (Back)

Mějme bod \(\mathbf a \in \mathbb{R}^n\) a \(\varepsilon > 0\). Potom okolím bodu \(\mathbf a\) o poloměru \(\varepsilon\) nazýváme množinu všech bodů \(\mathbf x \in \mathbb{R}^n\), jejichž vzdálenost od bodu \(\mathbf a\) je menší než \(\varepsilon\) a značíme ho \(U_\mathbf a(\varepsilon)\).
\[U_\mathbf a(\varepsilon) = \set{\mathbf a \in \mathbb{R}^n \mid d(\mathbf x, \mathbf a) < \varepsilon} \subset \mathbb{R}^n\]

## Poznámka Anki 1668435580405

Karty Anki: 1668435580405
GUID: Q9fY*K.Z3>; štítky: bi-ma2::p14 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Definujte hromadný bod množiny \(M \subset R^n\).

### Odpověď (Back)

Bod \(\mathbf a \in \mathbb{R}^n\) nazýváme hromadným bodem množiny \(M \subset R^n\), právě když v každém okolí bodu \(\mathbf a\) leží bod množiny \(M\) různý od \(\mathbf{a}\), neboli
\[(\forall \varepsilon > 0)(U_{\mathbf a}(\varepsilon) \smallsetminus \{ \mathbf x \} \cap M \neq \emptyset )\]

## Poznámka Anki 1668435699020

Karty Anki: 1668435699020
GUID: QzGY/t2Lsu; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Definujte Euklidovskou normu vektoru \(\mathbf{x} \in \mathbb{R}^n\) (\(||\mathbf{x}||\)).

### Odpověď (Back)

\[||\mathbf x|| := \sqrt{\sum \limits_{j=1}^n x_j^2}\]

## Poznámka Anki 1668435793144

Karty Anki: 1668435793144
GUID: soC+O_1:43; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Definujte standardní skalární součin dvou vektorů \(\mathbf{x}, \mathbf{y} \in \mathbb R^n\).

### Odpověď (Back)

\[\langle \mathbf{x} \mid \mathbf{y} \rangle := \sum \limits_{j=1}^n x_j y_j = \mathbf{x}^T \mathbf{y}\]

## Poznámka Anki 1668435881971

Karty Anki: 1668435881971
GUID: N7e&.@c}GG; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Definujte euklidovskou vzdálenost dvou bodů \(\mathbf{x}, \mathbf{y} \in \mathbb R^n\) (\(d(\mathbf{x}, \mathbf{y})\)).

### Odpověď (Back)

\[d(\mathbf{x}, \mathbf{y}) := ||\mathbf{x} - \mathbf{y}|| = \sqrt{\sum  \limits_{j=1}^n (x_j - y_j)^2}\]

## Poznámka Anki 1668435988893

Karty Anki: 1668435988893
GUID: xNOJk5KjiW; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Definujte vnitřní bod množiny.

### Odpověď (Back)

O bodu \(\mathbf{a} \in M \subset \mathbb{R}^n\) řekneme, že je vnitřním bodem množiny \(M\), právě když existuje okolí \(U_\mathbf{a}\) bodu \(\mathbf{a}\) takové, že \(U_\mathbf{a} \subset M\).

## Poznámka Anki 1668436100934

Karty Anki: 1668436100935
GUID: E6FQ#UsEQj; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Definujte otevřenou množinu.

### Odpověď (Back)

O množině \(M \subset \mathbb{R}^n\) řekneme, že je otevřená, právě když pro každý bod \(\mathbf{a} \in M\) existuje okolí \(U_\mathbf{a}\) bodu \(\mathbf{a}\) takové, že \(U_\mathbf{a} \subset M\).

## Poznámka Anki 1668436339404

Karty Anki: 1668436339404
GUID: n|<eJtT@H7; štítky: bi-ma2::p14 duplicate.

### Otázka (Front)

Definujte limitu vektorové posloupnosti.

### Odpověď (Back)

Posloupnost \((\mathbf{x}_k)_{k=1}^\infty\) vektorů \(\mathbf{x}_k \in \mathbb{R}^n\) má limitu \(\mathbf b \in \mathbb R^n\), právě když pro každé okolí \(U_\mathbf b\) bodu \(\mathbf b\) existuje \(N \in \mathbb{N}\) takové, že pokud pro \(k \in \mathbb N\) platí \(k \geq N\), pak \(\mathbf{x}_k \in U_\mathbf b\). Symbolicky lze limitu vektorové posloupnosti definovat následovně:\[(\forall U_\mathbf b)(\exists N \in \mathbb N)(\forall k \in \mathbb N)(k \geq N \Rightarrow \mathbf x_k \in U_\mathbf b).\]Tuto skutečnost značíme\[\displaystyle \lim_{k \to \infty} \mathbf{x}_k = \mathbf{a}.\]

## Poznámka Anki 1668436471296

Karty Anki: 1668436471296
GUID: F6KHK{~IL?; štítky: bi-ma2::p14.

### Otázka (Front)

Vyslovte větu o konvergenici a vzdálenosti (vztahu limity vektorové posloupnosti a "obyčejné" limity).

### Odpověď (Back)

Pro vektorovou posloupnost \((\mathbf{x}_k)_{k=1}^\infty\) platí \(\lim \limits_{k \to \infty} \mathbf{x}_k = \mathbf{a}\), právě když \(\displaystyle \lim_{k \to \infty} \| \mathbf{x}_k - \mathbf{a} \| = 0\) (tato druhá limita je "obyčejná" limita z BI-MA1).

## Poznámka Anki 1668436671306

Karty Anki: 1668436671306
GUID: f;Z;VT?T--; štítky: bi-ma2::p14.

### Otázka (Front)

Vyslovte větu o konvergenci posloupnosti po složkách.

### Odpověď (Back)

Uvažme posloupnost \((\mathbf{x}_k)_{k=1}^\infty\). Potom platí následující ekvivalence \(\displaystyle \lim_{k \to \infty} \mathbf{x}_k = \mathbf{a}\), právě když pro každé \(j \in \hat{n}\) platí \(\displaystyle \lim_{k \to \infty} (\mathbf{x}_k)_j = \mathbf{a}_j\).

## Poznámka Anki 1668436954709

Karty Anki: 1668436954709
GUID: FW!GZ/wP7/; štítky: bi-ma2::p14.

### Otázka (Front)

Vyslovte větu o limitě součtu a skalárního násobku posloupností.

### Odpověď (Back)

Mějme dvě vektorové posloupnosti \((\mathbf{x}_k)_{k=1}^\infty\) a \((\mathbf{y}_k)_{k=1}^\infty\) splňující \(\displaystyle \lim_{k \to \infty} \mathbf{x}_k = \mathbf{a}\) a \(\displaystyle \lim_{k \to \infty} \mathbf{y}_k = \mathbf{b}\) a \(\alpha \in \mathbb{R}\). Potom:
\[\displaystyle \lim_{k \to \infty} (\mathbf{x}_k + \mathbf{y}_k) = \mathbf{a} + \mathbf{b},\]\[\displaystyle \lim_{k \to \infty} (\alpha \mathbf{x}_k) = \alpha \mathbf{a}.\]

## Poznámka Anki 1668437810830

Karty Anki: 1668437810830
GUID: zvS`t-lw{8; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Definujte limitu vektorové funkce.

### Odpověď (Back)

Mějme funkci \(F: D_F \to \mathbb R^m\), \(D_F \subset \mathbb R^n\) a hromadný bod \(\mathbf a\) množiny \(D_F\). Funkce \(F\) má v bodě \(\mathbf a\) limitu \(\mathbf{b} \in \mathbb{R}^m\), právě když pro každé okolí \(U_\mathbf{b}\) bodu \(\mathbf{b}\) existuje okolí \(U_\mathbf{a}\) bodu \(\mathbf{a}\) takové, že pokud pro \(\mathbf x \in \mathbb R^n\) platí \(\mathbf x \in (U_\mathbf a \cap D_F) \smallsetminus \{ \mathbf a \}\), pak \(F(\mathbf x) \in U_\mathbf b\). Symbolicky lze limitu vektorové funkce definovat následovně:\[(\forall U_\mathbf b)(\exists U_\mathbf a)(\forall \mathbf x \in \mathbb R^n)(\mathbf x \in (U_\mathbf a \cap D_F) \smallsetminus \{ \mathbf a \} \Rightarrow F(\mathbf x) \in U_\mathbf b).\]Tuto skutečnost značíme\[\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} F(\mathbf{x}) = \mathbf{b}.\]Pokud je navíc \(m = 1\), pak povolujeme i situaci, kdy \(\mathbf b \in \{ +\infty, -\infty \}\), tedy \(\mathbf b \in \overline{\mathbb R}\).

## Poznámka Anki 1668458400229

Karty Anki: 1668458400229
GUID: y.4ZJR5xGU; štítky: bi-ma2::p14 bi-spol::16 duplicate.

### Otázka (Front)

Vyslovte větu o limitě zúžení vektorové funkce. Co platí o posloupnosti bodů z jejího definičního oboru?

### Odpověď (Back)

Mějme vektorovou funkci \(F : D_F \to \mathbb{R}^m\), \(D_F \subset \mathbb{R}^n\) a hromadný bod \(\mathbf{a}\) definičního oboru funkce \(F\), v němž existuje limita
\[\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} F(\mathbf{x}) = \mathbf{b} \in \mathbb{R}^m.\]Potom i pro \(F|_M\) zúžení funkce \(F\) na množinu \(M\), která má \(\mathbf{a}\) jako hromadný bod, platí
\[\displaystyle \lim_{\mathbf{x} \to \mathbf{a}}(F|_M)(\mathbf{x}) = \mathbf{b}.\]Speciálně, je-li \((\mathbf{x}_k)_{k=1}^\infty\) posloupnost bodů z \(D_F\) různých od \(\mathbf{a}\), ale s limitou rovnou \(\mathbf{a}\), pak
\[\displaystyle \lim_{k \to \infty} F(\mathbf{x}_k) = \mathbf{b}.\]

## Poznámka Anki 1668458671528

Karty Anki: 1668458671528
GUID: hu=HB^q5c(; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Vyslovte větu o limitě součtu, násobku, součinu a podílu vektorových funkcí.

### Odpověď (Back)

Mějme funkce \(F : D_F \to \mathbb{R}^m\), \(D_F \subset \mathbb{R}^n\), \(G: D_G \to \mathbb{R}^m\), \(D_G \subset \mathbb{R}^n\), bod \(\mathbf{a} \in \mathbb{R}^n\), který je hromadným bodem množiny \(D_F \cap D_G\) a \(c \in \mathbb{R}\). Pokud existují limity \(\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} F(\mathbf{x})\) a \(\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} G(\mathbf{x})\), platí\[\begin{matrix}
\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} \big(F(\mathbf{x}) + G(\mathbf{x}) \big) = \displaystyle \lim_{\mathbf{x} \to \mathbf{a}} F(\mathbf{x}) + \displaystyle \lim_{\mathbf{x} \to \mathbf{a}} G(\mathbf{x}), \\ \displaystyle \lim_{\mathbf{x} \to \mathbf{a}} c \cdot F(\mathbf{x}) = c \cdot \displaystyle \lim_{\mathbf{x} \to \mathbf{a}} F(\mathbf{x}).
\end{matrix}\]Pokud je navíc \(m = 1\), platí\[\begin{matrix}
\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} \big( f(\mathbf{x}) \cdot g(\mathbf{x}) \big) = \displaystyle \lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) \cdot \displaystyle \lim_{\mathbf{x} \to \mathbf{a}} g(\mathbf{x}),\\\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} \frac{f(\mathbf{x})}{g(\mathbf{x})} = \frac{\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x})}{\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} g(\mathbf{x})},
\end{matrix}\]pro podíl za předpokladu \(\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} g(\mathbf{x}) \neq 0\).

## Poznámka Anki 1669038585890

Karty Anki: 1669038585890
GUID: n`H,v2>wiM; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Definujte spojitou vektorovou funkci v bodě a na definičním oboru (resp.  množině).

### Odpověď (Back)

Mějme vektorovou funkci \(F: A \to \mathbb{R}^m\), \(A \subset \mathbb{R}^n\), a bod \(\mathbf{a} \in D_F\), který je hromadným bodem množiny \(D_F\). Funkce \(F\) je spojitá v bodě \(\mathbf{a}\), právě když
\[\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} F(\mathbf{x}) = F(\mathbf{a}).\]Funkci \(F\) nazveme spojitou (resp. spojitou na množině \(M\)), právě když je spojitá v každém bodě svého definičního oboru (resp. v každém bodě množiny \(M\)).

## Poznámka Anki 1669038845770

Karty Anki: 1669038845770
GUID: D3W[fAAOG2; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Vyslovte a dokažte větu o spojitosti součtu, násobku, součinu a podílu vektorových funkcí.

### Odpověď (Back)

Mějme dvě vektorové funkce \(F : D_F \to \mathbb{R}^m\), \(D_F \subset \mathbb{R}^n\), \(G: D_G \to \mathbb{R}^m\), \(D_G \subset \mathbb{R}^n\), bod \(\mathbf{a} \in \mathbb{R}^n\), který je hromadným bodem množiny \(D_F \cap D_G\) a \(\alpha \in \mathbb{R}\). Předpokládejme, že \(F\) i \(G\) jsou spojité v bodě \(\mathbf{a}\). Potom

- \(F + G\) je spojitá v \(\mathbf{a}\),

- \(\alpha F\) je spojitá v \(\mathbf{a}\).

Pokud je \(m = 1\), pak

- \(F \cdot G\) je spojitá v \(\mathbf{a}\),

- \(\frac{F}{G}\) je spojitá v \(\mathbf{a}\) v případě, kdy \(G(\mathbf{a}) \neq 0.\)

**Důkaz** 

Věta vychází z definice spojitosti a věty o limitě součtu, násobku, součinu a podílu.

## Poznámka Anki 1669040339656

Karty Anki: 1669040339656
GUID: O7#:%p)eng; štítky: bi-ma2::p14 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Definujte parciální derivaci funkce v bodě.

### Odpověď (Back)

Mějme funkci \(f: D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) definovanou na okolí bodu \(\mathbf a \in D_f\) a \(j \in \hat n\). Parciální derivace funkce \(f\) v bodě** **\(\mathbf a\)** **podle \(j\)-té proměnné je limita\[\displaystyle \lim_{h \to 0} \frac{f(\mathbf a + h \mathbf e_j) - f(\mathbf a)}{h},\]existuje-li. Značíme ji \(\frac{\partial f}{\partial x_j}(\mathbf{a})\) nebo \(\partial_{x_j} f(\mathbf{a})\).

### Doplňující pole (Extra)

**V předmětu NI-MPI **se používá alternativní ekvivalentní definice:\[\displaystyle \lim_{h \to 0} \frac { f(a_1, a_2, \dots, a_j  + h, \dots, a_n ) - f(a_1, a_2, \dots,  a_j, \dots, a_n) } h,\]kde \(\mathbf a = (a_1, a_2, \dots a_n)\) a nazývá se také parciální derivací funkce \(f\) v bodě \(\mathbf a\) ve směru \(x_j\).

## Poznámka Anki 1669040471896

Karty Anki: 1669040471896
GUID: g1Fz&Z/lNk; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Vyslovte větu o spojitosti složené vektorové funkce.

### Odpověď (Back)

Mějme vektorové funkce \(g: D_g \to \mathbb{R}^m\), \(D_g \subset \mathbb{R}^n\) a \(f: D_f \to \mathbb{R}^k\), \(D_f \subset \mathbb{R}^m\). Dále předpokládejme, že \(g\) je spojitá v \(\mathbf{a} \in D_g\) a \(f\) je spojitá a definovaná na okolí \(g(\mathbf{a})\). Potom je \(f \circ g\) spojitá v bodě \(\mathbf{a}\).

## Poznámka Anki 1669040984802

Karty Anki: 1669040984802
GUID: Lv?]VE+?ul; štítky: bi-ma2::p14 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Definujte gradient funkce v bodě a popište jeho význam.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(\mathbf a \in D_f\) takový, že \(f\) má na okolí bodu \(\mathbf a\) spojité všechny parciální derivace. Gradient funkce \(f\) v bodě je vektor typu \(\mathbb R^{1, n}\)\[\bigg(\frac{\partial f}{\partial x_1}(\mathbf{a}), \frac{\partial f}{\partial x_2}(\mathbf{a}), \cdots, \frac{\partial f}{\partial x_n}(\mathbf{a}) \bigg)\]a značíme jej \(\nabla f(\mathbf{a})\) nebo \(\operatorname{grad} f(\mathbf{a})\). Gradient udává směr největšího růstu funkce v bodě. To znamená, že směrnice tečny udaná derivací funkce v tomto směru bude největší.

### Doplňující pole (Extra)

Tato definice je zjednodušená, z čehož plyne i předpoklad spojitosti parciálních derivací. Obecná definice požaduje vnitřní bod \(\mathbf a \in D_f\) a gradient funkce \(f\) v bodě \(\mathbf a\) pak definuje jako vektor \(v \in \mathbb R^{1, n}\) splňující\[\displaystyle \lim_{\mathbf x \to \mathbf a} \frac{\| f(\mathbf x) - f(\mathbf a) - \mathbf v \cdot (\mathbf x - \mathbf a) \|}{\| \mathbf x - \mathbf a \|} = 0.\]

## Poznámka Anki 1669041299704

Karty Anki: 1669041299704
GUID: iuWzcV6Hp@; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Definujte derivaci vektorové funkce.

### Odpověď (Back)

Mějme funkci \(F : D_F \to \mathbb R^m\), \(D_F \subset \mathbb R^n\) definovanou na okolí bodu \(\mathbf a\). Derivace vektorové funkce \(F\) v bodě \(\mathbf a\) je matice \(DF(\mathbf a) \in \mathbb R^{m, n}\) splňující\[\displaystyle \lim_{\mathbf x \to \mathbf a} \frac{\| F(\mathbf x) - F(\mathbf a) - DF(\mathbf a) \cdot (\mathbf x - \mathbf a) \|}{\| \mathbf x - \mathbf a \|} = 0.\]

## Poznámka Anki 1669043359654

Karty Anki: 1669043359654
GUID: JEUQR[-(%x; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Vyslovte a dokažte větu o složkách matice \(DF(\mathbf{a})\) a její jednoznačnosti.

### Odpověď (Back)

Pokud má zobrazení \(F: D_F \to \mathbb{R}^m\), \(D_F \subset \mathbb{R}^n\), definované na okolí bodu \(\mathbf{a}\), derivaci \(DF(\mathbf{a}) \in \mathbb{R}^{m,n}\) v bodě \(\mathbf{a}\), potom
\[      DF(\mathbf{a}) = \begin{pmatrix}

        \frac{\partial F_1}{\partial x_1}(\mathbf{a}) & \frac{\partial F_1}{\partial x_2}(\mathbf{a}) & \cdots & \frac{\partial F_1}{\partial x_n}(\mathbf{a}) \\

        \frac{\partial F_2}{\partial x_1}(\mathbf{a}) & \frac{\partial F_2}{\partial x_2}(\mathbf{a}) & \cdots & \frac{\partial F_2}{\partial x_n}(\mathbf{a}) \\

        \vdots & \vdots & \ddots & \vdots \\

        \frac{\partial F_m}{\partial x_1}(\mathbf{a}) & \frac{\partial F_m}{\partial x_2}(\mathbf{a}) & \cdots & \frac{\partial F_m}{\partial x_n}(\mathbf{a})

      \end{pmatrix}.\]
**Důkaz
**Určíme prvek matice \(DF(\mathbf{a})\) v \(i\)-tém řádku a \(j\)-tém sloupci. Z předpokladu a obecné nerovnosti \(|\mathbf z_i| \leq \| \mathbf z \|\), \(i \in \hat m\) a \(\mathbf z \in \mathbb R^m\), dostáváme
\[\lim \limits_{\mathbf x \to \mathbf a} \frac{|F_i(\mathbf x) - F_i(\mathbf a) - \big( DF(\mathbf a) \cdot (\mathbf x - \mathbf a) \big)_i |}{\| \mathbf x - \mathbf a \|} = 0.\]Nyní použijeme větu o zúžení a budeme k \(\mathbf a\) přistupovat po přímce \(\mathbf x = \mathbf a + h \mathbf e_j\), kde \(h \to 0\). Odtud pomocí jednoduchých úprav plyne
\[ 0 = \lim_{h \to 0} \frac{\big|F_i(\mathbf{a} + h\mathbf{e}_j) - F_i(\mathbf{a}) - DF(\mathbf{a})_{i,j} h\big|}{|h|} = \Bigg| \lim_{h \to 0} \frac{F_i(\mathbf{a} + h\mathbf{e}_j) - F_i(\mathbf{a})}{h} - DF(\mathbf{a})_{i,j} \Bigg|.\]V tomto výrazu již vidíme parciální derivaci funkce \(F_i\) podle \(j\)-té proměnné v bodě \(\mathbf a\), která má nutně hodnotu \(DF(\mathbf a)_{i, j}\).

## Poznámka Anki 1669050220731

Karty Anki: 1669050220731
GUID: CP`Vp[|y)i; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Vyslovte větu spojitosti vektorové funkce zadané pomcí spojitých elementárních funkcí jedné proměnné.

### Odpověď (Back)

Buďte \(f: D_f \to \mathbb{R}\), \(D_f \subset \mathbb{R}\), reálná funkce jedné reálné proměnné, \(n \in \mathbb{N}\) a \(k \in \hat{n}\). Definujme funkci (\(D_f\) v \(k\)-tém faktoru)
\[g(\mathbf{x}) := f(x_k), \text{ pro } \mathbf{x} \in D_g := \mathbb{R} \times \cdots \times \mathbb{R} \times D_f \times \mathbb{R} \cdots \times \mathbb{R}.\]Je-li \(f\) spojitá, pak i \(g\) je spojitá.

## Poznámka Anki 1669050477174

Karty Anki: 1669050477174
GUID: hx=>J[{epk; štítky: bi-ma2::p14 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Definujte Hessovu matici funkce v bodě.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(\mathbf a \in A \subset D_f\) takový, že \(f\) má v bodě \(\mathbf a\) všechny druhé parciální derivace. Hessova matice funkce \(f\) v bodě \(\mathbf a\) je matice typu \(\mathbb R^{n, n}\)\[\begin{pmatrix}

        \frac{\partial^2 f}{\partial x_1^2}(\mathbf a) & \frac{\partial^2 f}{\partial x_2 \partial x_1}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_n \partial x_1}(\mathbf a) \\

        \frac{\partial^2 f}{\partial x_1 \partial x_2}(\mathbf a) & \frac{\partial^2 f}{\partial x_2^2}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_n \partial x_2}(\mathbf a) \\

        \vdots & \vdots & \cdots & \vdots \\

        \frac{\partial^2 f}{\partial x_1 \partial x_n}(\mathbf a) & \frac{\partial^2 f}{\partial x_2 \partial x_n}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_n^2}(\mathbf a)

      \end{pmatrix}\]a značíme ji \(\nabla^2 f(\mathbf a).\)

### Doplňující pole (Extra)

Pokud na gradient („derivaci“) funkce \(f\) nahlédneme jako na zobrazení \(Df : A \to \mathbb R^n\), \(A \subset D_f\), pak je Hessova matice derivací tohoto zobrazení v bodě \(\mathbf a \in A\).
**V předmětu NI-MPI **je pořadí parciálních derivací prohozeno** **a Hessova matice je tedy definována jako\[      \nabla^2 f(\mathbf a) = \begin{pmatrix}

        \frac{\partial^2 f}{\partial x_1^2}(\mathbf a) & \frac{\partial^2 f}{\partial x_1 \partial x_2}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n}(\mathbf a) \\

        \frac{\partial^2 f}{\partial x_2 \partial x_1}(\mathbf a) & \frac{\partial^2 f}{\partial x_2^2}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n}(\mathbf a) \\

        \vdots & \vdots & \cdots & \vdots \\

        \frac{\partial^2 f}{\partial x_n \partial x_1}(\mathbf a) & \frac{\partial^2 f}{\partial x_n \partial x_2}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_n^2}(\mathbf a)

      \end{pmatrix}.\]

## Poznámka Anki 1669050694532

Karty Anki: 1669050694532
GUID: sR5j1Ylz{q; štítky: bi-ma2::p14.

### Otázka (Front)

Vyslovte větu o derivaci složené vektorové funkce.

### Odpověď (Back)

Mějme zobrazení \(F: D_F \to \mathbb{R}^k, D_F \subset \mathbb{R}^m\) a \(G : D_G \to \mathbb{R}^m\), \(D_G \subset \mathbb{R}^n\) a bod \(\mathbf{a} \in D_G\) takové, že existují \(DG(\mathbf{a})\) a \(DF(G(\mathbf{a}))\). Potom existuje i derivace složeného zobrazení \(F \circ G\) v bodě \(\mathbf{a}\) a platí
\[D(F \circ G)(\mathbf{a}) = DF(G(\mathbf{a})) \cdot DG(\mathbf{a}).\]

## Poznámka Anki 1669050866276

Karty Anki: 1669050866276
GUID: Gx#G[yzk4p; štítky: bi-ma2::p14 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Definujte derivaci funkce ve směru v bodě a popište její vztah s gradientem funkce.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\), bod \(\mathbf a \in D_f \) takový, že \(f\) má v bodě \(\mathbf a\) derivaci, a vektor \(\mathbf s \in \mathbb R^{n, 1}\) takový, že \(\| \mathbf s \| = 1\). Derivace funkce \(f\) v bodě \(\mathbf a\) ve směru \(\mathbf s\) je limita\[\displaystyle \lim_{h \to 0} \frac{f(\mathbf a + h \mathbf s) - f(\mathbf a)}{h}\]a značíme ji \(\frac{\partial f}{\partial \mathbf s}(\mathbf{a})\) nebo \(\partial_{\mathbf s} f(\mathbf a)\). Pokud má funkce v bodě \(\mathbf a\) gradient, pak\[\partial_{\mathbf s} f(\mathbf a) = \langle \nabla f(\mathbf a) \mid \mathbf s \rangle.\]

### Doplňující pole (Extra)

**V předmětu NI-MPI **je po bodu \(a \in D_f\) požadováno pouze, aby funkce \(f\) byla definována na nějakém jeho okolí, a pro derivaci funkce \(f\) v bodě \(\mathbf a\) ve směru \(\mathbf s\) se také používá značení \(\nabla_\mathbf s f(\mathbf a)\).

## Poznámka Anki 1673178897985

Karty Anki: 1673178897985
GUID: K#=HB0mCyO; štítky: bi-ma2::p14.

### Otázka (Front)

Vyslovte a dokažte tvrzení o Schwarzově nerovnosti.

### Odpověď (Back)

Pro každé \(\mathbf x, \mathbf y \in \mathbb R^n\) platí nerovnost
\[| \langle \mathbf x \mid \mathbf y \rangle  | \leq \| \mathbf x \| \cdot \| \mathbf y \|.\]Navíc rovnost nastává právě tehdy, když jeden z vektorů je násobkem druhého.

**Důkaz**
Pro každé \(\alpha \in \mathbb R\) a \(\mathbf x, \mathbf y \in \mathbb R^n\) platí
\[0 \leq \| \mathbf x + \alpha \mathbf y \|^2 = \langle \mathbf x + \alpha \mathbf y \mid \mathbf x + \alpha \mathbf y \rangle = \| \mathbf x \|^2 + 2 \alpha \langle \mathbf x \mid \mathbf y \rangle + \alpha^2 \| \mathbf y \|^2.\]A pro diskriminant \(D\) tohoto kvadratického polynomu (v \(\alpha\)) pak nutně platí
\[0 \geq D = \big( 2 \langle \mathbf x \mid \mathbf y \rangle \big)^2 - 4 \| \mathbf x \|^2 \| \mathbf y \|^2.\]Což po jednoduchých úpravách dává přesně Schwarzovu nerovnost. Konečně pak také vidíme, že rovnost nastává právě tehdy, když \(D =0\), čili když uvedený polynom má dvojnásobný kořen \(\alpha\) a tedy \(\| \mathbf x + \alpha \mathbf y \| = 0\), neboli \(\mathbf x + \alpha \mathbf  y = 0\).

## Poznámka Anki 1673179136036

Karty Anki: 1673179136036
GUID: Pv>l=S8ysw; štítky: bi-ma2::p14.

### Otázka (Front)

Vyslovte a dokažte tvrzení o trojůhelníhové nerovnosti.

### Odpověď (Back)

Pro každé \(\mathbf x, \mathbf y \in \mathbb R^n\) platí
\[\| \mathbf x + \mathbf y \| \leq \| \mathbf x \| + \| \mathbf y \|.\]
**Důkaz
**Tvrzení plyne z Schwarzovy nerovnosti:
\[\| \mathbf x + \mathbf y \|^2 = \| \mathbf x \|^2 + 2 \langle \mathbf x \mid \mathbf y \rangle + \| \mathbf  y \|^2 \leq \| \mathbf x \|^2 + 2 \| \mathbf x \| \| \mathbf y \| + \| \mathbf y \|^2 = \big( \| \mathbf x \| + \| \mathbf y \| \big)^2.\]Nyní stačí odmocnit.

## Poznámka Anki 1673180863915

Karty Anki: 1673180863915
GUID: Gq3LRzPG0g; štítky: bi-ma2::p14 bi-spol::16.

### Otázka (Front)

Vyslovte větu o vztahu limity vektorové funkce a limity jejích složek.

### Odpověď (Back)

Mějme funkci \(F: D_F \to \mathbb R^m\), \(D_F \subset \mathbb R^n\), hromadný bod \(\mathbf a \in \mathbb R^n\) množiny \(D_F\) a bod \(\mathbf b \in \mathbb R^m\). Potom platí\[\displaystyle \lim_{\mathbf x \to \mathbf a} F(\mathbf x) = \mathbf b \Leftrightarrow \displaystyle \lim_{\mathbf x \to \mathbf a} \| F(\mathbf x) - \mathbf b \| = 0.\]Označíme-li složky \(F\) jako \(F(\mathbf x) = \big( F_1(\mathbf x), \dots, F_m(\mathbf x) \big)^T\), kde \(\mathbf x \in D_F\), pak platí\[\displaystyle \lim_{\mathbf x \to \mathbf a} F(\mathbf x) = \mathbf b \Leftrightarrow \displaystyle \lim_{\mathbf x \to \mathbf a} F_j(\mathbf x) = b_j,\]kde \(j \in \hat m\).

## Poznámka Anki 1673368773481

Karty Anki: 1673368773482
GUID: z6##$2^,|G; štítky: bi-ma2::p14.

### Otázka (Front)

Definujte vektorovou posloupnost.

### Odpověď (Back)

Zobrazení \(\mathbb N \to \mathbb R^n\), které značíme \((\mathbf x_k)_{k=1}^\infty\), nazveme vektorovou posloupností.

