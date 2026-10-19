# NI-MKY – Přednáška 01

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MKY
Rozsah: 18 poznámek, 18 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1739873844914

Karty Anki: 1739873844914
GUID: c&q]gl>_o{; štítky: duplicate ni-mky::p01.

### Otázka (Front)

Definujte grupu (group) a abelovskou (komutativní) grupu.

### Odpověď (Back)

Nechť \(M\) je neprázdná množina a \(\circ : M \times M \to M\) binární operace (vlastnosti grupoidu). Pokud

- platí asociativní zákon (vlastnost pologrupy):

\[(\forall a,b,c \in M) \big(a \circ (b \circ c) = (a \circ b) \circ c \big),\]

- existuje neutrální prvek (vlastnost monoidu) tak, že

\[(\exists e \in M)(\forall a \in M) \big( a \circ e = e \circ a = a \big),\]

- existuje inverzní prvek tak, že

\[(\forall a \in M)(\exists a^{-1}\in M) \big(a \circ a^{-1} = a^{-1} \circ a = e\big),\]říkáme, že uspořádaná dvojice \(G = (M, \circ)\) je **grupa**. Pokud navíc pro \(\circ\) platí komutativní zákon:

\[(\forall a,b \in M) \big(a \circ b = b \circ a\big),\]mluvíme o** abelovské **(komutativní)** grupě**.

 [Obrázek: paste-1d997f3379632d352e95389c9e16ecc09f6e5eee.jpg; soubor je v media/ v doprovodném ZIP]

### Doplňující pole (Extra)

Grupa je tedy monoid \((M, \circ)\), ve kterém existuje ke každému prvku inverzní prvek, a abelovská (komutativní) grupa je grupa, kde \(\circ\) je komutativní operace.

## Poznámka Anki 1739873882550

Karty Anki: 1739873882551
GUID: Nb?f3[+pMV; štítky: duplicate ni-mky::p01.

### Otázka (Front)

Vyslovte a dokažte větu o jednoznačnosti neutrálního prvku v monoidu.

### Odpověď (Back)

Mějme monoid \((M, \circ)\). Pak v tomto monoidu existuje právě jeden neutrální prvek.

**Důkaz** 
Důkaz provedeme sporem. Z definice monoidu víme, že existuje neutrální prvek \(e \in M\). Pro spor budeme nyní předpokládat, že existuje další neutrální prvek \(\overline e \in M\) takový, že \(e \neq \overline e\). Potom z definice neutrálního prvku platí
\[\overline e = \overline e \circ e = e,\]čímž dostáváme spor s tím, že \(e\) a \(\overline e\) jsou různé.

## Poznámka Anki 1739873901738

Karty Anki: 1739873901739
GUID: P$#haL}W8G; štítky: duplicate ni-mky::p01.

### Otázka (Front)

Vyslovte a dokažte větu o jednoznačnosti inverzního prvku v grupě.

### Odpověď (Back)

Mějme grupu \((M, \circ)\). Pak pro každé \(a \in M\) existuje právě jeden inverzní prvek.

**Důkaz** 
Důkaz provedeme sporem. Z definice grupy víme, že pro každý prvek \(a \in M\) existuje alespoň jeden inverzní prvek \(a^{-1} \in M\). Pro spor budeme nyní předpokládat, že existuje další inverzní prvek \(\overline{a^{-1}} \in M\) takový, že \(a \neq \overline{a^{-1}}\). Potom platí
\[\overline{a^{-1}} = \overline{a^{-1}} \circ e = \overline{a^{-1}} \circ (a \circ a^{-1}) = (\overline{a^{-1}} \circ a) \circ a^{-1} = e \circ a^{-1} = a^{-1},\]čímž dostáváme spor s tím, že \(a^{-1}\) a \(\overline{a^{-1}}\) jsou různé.

## Poznámka Anki 1739874750295

Karty Anki: 1739874750295
GUID: oL%*mg-`mB; štítky: ni-mky::p01.

### Otázka (Front)

Vyslovte a dokažte větu o inverzním prkvu složení dvou prvků grupy.

### Odpověď (Back)

Mějme grupu \(G\) a dva prvky \(a, b \in G\). Pak platí\[(a \circ b )^{-1} = b^{-1} \circ a ^{-1}.\]**Důkaz** 
Postupně ověříme obě rovnosti, které musí inverzní prvek splňovat. Díky asociativitě operace v \(G\) platí:\[\begin{matrix}
(a \circ b) \circ (b^{-1} \circ a^{-1}) = a \circ (b \circ b^{-1}) \circ a^{-1} = a \circ e \circ a^{-1} = a \circ a^{-1} = e,\\
(b^{-1} \circ a^{-1}) \circ (a \circ b) = b^{-1} \circ (a^{-1} \circ a) \circ b = b^{-1} \circ e \circ b = b^{-1} \circ b = e.
\end{matrix}\]

## Poznámka Anki 1739874793734

Karty Anki: 1739874793735
GUID: QiFaOnKL>k; štítky: duplicate ni-mky::p01.

### Otázka (Front)

Definujte řád (order) grupy, konečnou a nekonečnou grupu.

### Odpověď (Back)

**Řádem grupy** \(G = (M, \circ)\) nazýváme počet prvků množiny \(M\) a značíme \(\#G\). Je-li \(M\) nekonečná množina, je její řád nekonečno a o \(G\) říkáme, že je **nekonečná**. V opačném případě nazýváme \(G\) **konečnou grupou**.

## Poznámka Anki 1739874847930

Karty Anki: 1739874847930
GUID: fP]e[-,e1:; štítky: duplicate ni-mky::p01.

### Otázka (Front)

Definujte řád prvku grupy a popište jeho vztah k řádu grupy.

### Odpověď (Back)

Mějme grupu \(G = (M, \circ)\) a \(a \in M\). Pokud existuje \(m \in \mathbb Z^+\) splňující\[a^m = e,\]pak nejmenší takové \(m\) nazýváme řádem prvku** **\(a\) a značíme jej \(\operatorname{ord} a\). Pokud takové \(m\) neexistuje, je řád prvku \(a\) nekonečno. Pro grupu \(\langle a \rangle\) platí, že\[\operatorname{ord} a = \# \langle a \rangle.\]

## Poznámka Anki 1739874898857

Karty Anki: 1739874898857
GUID: y3>+.P8##z; štítky: duplicate ni-mky::p01.

### Otázka (Front)

Definujte podgrupu (subgroup).

### Odpověď (Back)

Mějme grupu \(G = (M, \circ)\). Podgrupou (subgroup) grupy \(G\) nazveme libovolnou dvojici \(H = (N, \circ)\) takovou, že

- \(N \subseteq M\) je neprázdná množina,

- \((N, \circ)\) je grupa.

## Poznámka Anki 1739876006621

Karty Anki: 1739876006621
GUID: FW6rYU[eVv; štítky: ni-mky::p01.

### Otázka (Front)

Definujte relaci ekvivalence a třídu prvku v ekvivalenci.

### Odpověď (Back)

Relaci \(R\) na množině \(M\) nazýváme **relací ekvivalence** na množině \(M\) právě tehdy, když splňuje následující vlastnosti:

- **reflexivita** - pro každé \(x \in M\) platí \((x, x) \in R\);

- **symetrie** - pokud \((x, y) \in R\), pak \((y, x) \in R\);

- **tranzitivita** - pokud \((x, y) \in R\) a \((y, z) \in R\), potom \((x, z) \in R\).

**Třídou prvku ** \(x \in M\)** v ekvivalenci **nazýváme množinu všech prvků, které s ním jsou ekvivalentní a značíme ji \[[x] = \{ y \in M \mid (x, y) \in R \}.\]

## Poznámka Anki 1739876622269

Karty Anki: 1739876622269
GUID: lUqV2a+jKj; štítky: ni-mky::p01.

### Otázka (Front)

Definujte rozklad množiny

### Odpověď (Back)

Mějme neprázdnou množinu \(X\). Rozkladem množiny \(X\) je množina \(\mathcal X\) neprázdných podmnožin množiny \(X\), která splňuje:

- **podmínku pokrytí **- \(X\) je sjednocením množin z množiny \(\mathcal X\):

\[(\forall x \in X)(\exists M \in \mathcal X)(x \in M),\]

- **podmínku disjunkce **- množiny z \(\mathcal X\) jsou vzájemně disjunktní:\[(\forall M, N \in \mathcal X)(M \neq N \Rightarrow M \cap N = \emptyset).\]

## Poznámka Anki 1739883449263

Karty Anki: 1739883449263
GUID: QpiEH2.>hl; štítky: ni-mky::p01.

### Otázka (Front)

Vyslovte a dokažte větu o vztahu relace ekvivalence a rozkladu množiny.

### Odpověď (Back)

Třídy ekvivalence relace ekvivalence \(R\) na množině \(M\) tvoří její rozklad a opačně z rozkladu \(M\) lze zkonstruovat relaci ekvivalence.

**Důkaz pro „**\(\Rightarrow\)**“
**Postupně dokážeme vlastnosti rozkladu množiny:

- **podmínka pokrytí** - díky reflexivitě relace ekvivalence \(R\) je každá třída ekvivalene neprázdná a navíc víme, že \(M\) je jejich sjednocením;

- **podmínka disjunkce** - mějme dvě třídy rozkladu \([x]\) a \([y]\) takové, že \([x] \neq [y]\) a pro spor předpokládejme, že existuje\[z \in [x] \cap [y],\]potom z definice\[\begin{matrix}
x \sim z,\\
y \sim z,
\end{matrix}\]pomocí symetrie dostaneme\[y \sim z \Rightarrow z \sim y\]a pomocí tranzitivity potom\[x \sim z \land z \sim y \Rightarrow x \sim y,\]z čehož plyne\[[x] = [y],\]což je spor.

**Důkaz pro „**\(\Leftarrow\)**“**
Je-li dán nějaký rozklad množiny \(M\), položme \(x \sim y\), právě když \(x\) a \(y\) leží ve stejné části rozkladu. Takto definovaná relace je relací ekvivalence na \(M\).

## Poznámka Anki 1739885400578

Karty Anki: 1739885400578
GUID: ZeCmq|Xwo; štítky: ni-mky::c01 ni-mky::p01.

### Otázka (Front)

Definujte relace ekvivalence \(\mathcal L_H\) a \(\mathcal R_H\) a levou a pravou třídu rozkladu.

### Odpověď (Back)

Mějme podgrupu \(H\) grupy \(G\). Potom **relace ekvivalence** \(\mathcal L_H\) resp. \(\mathcal R_H\) na \(G\) je definována jako:\[\begin{matrix}
(a, b) \in \mathcal L_H \stackrel{\text{def}}\Leftrightarrow (\exists h \in H)(a = bh)\\
\text{resp.}\\
(a, b) \in \mathcal R_H \stackrel{\text{def}}\Leftrightarrow (\exists h \in H)(a = hb).
\end{matrix}\]Relace ekvivalence \(\mathcal L_H\) resp. \(\mathcal R_H\) rozkládá nosnou množinu grupy \(G\) na třídy ekvivalence\[\begin{matrix}
[a]_{\mathcal L_H} = \{ ah \mid h \in H \}\\
\text{resp.}\\
[a]_{\mathcal R_H} = \{ ha \mid h \in H \},
\end{matrix}\]kde \(a \in G\). Tyto třídy ekvivalence se nazývají **levé** resp. **pravé třídy rozkladu** \(G\) vzhledem k \(H\) a často se pro ně používá značení \(aH\) resp. \(Ha\).

## Poznámka Anki 1739886331303

Karty Anki: 1739886331303
GUID: mZNURM;N^2; štítky: ni-mky::p01.

### Otázka (Front)

Dokažte, že \(\mathcal L_H\) a \(\mathcal R_H\) jsou relace ekvivalence.

### Odpověď (Back)

Důkaz provedeme pro \(\mathcal L_H\) tak, že postupně ověříme vlastnosti relace ekvivalence:

- **reflexivita** - pro libovolné \(a \in G\) platí\[a = ae,\]z čehož plyne\[(a, a) \in \mathcal L_H;\]
- **symetrie** - je-li \((a, b) \in \mathcal L_H\), pak existuje \(h \in H\) tak, že\[a = bh,\]z čehož plyne\[b = ah^{-1},\]a protože je \(H\) grupa, tak \(h^{-1} \in H\) a platí\[(b, a) \in \mathcal L_H;\]
- **tranzitivita** - je-li \((a, b) \in \mathcal L_H\) a \((b, c) \in \mathcal L_H\), pak existují \(h_1, h_2 \in H\) tak, že\[\begin{matrix}
a = bh_1,\\
b = ch_2,
\end{matrix}\]z čehož plyne\[a = (c h_2) h_1 = c (h_2 h_1)\]a protože je \(H \) grupa, tak \(h_2 h_1 \in H\) a platí\[(a, c) \in \mathcal L_H.\]

### Doplňující pole (Extra)

Důkaz pro \(\mathcal R_H\) je obdobný.

## Poznámka Anki 1739887214626

Karty Anki: 1739887214626
GUID: g.gdy}71ql; štítky: ni-mky::p01.

### Otázka (Front)

Vyslovte a dokažte lemma o počtu prvků levé a pravé třídy rozkladu grupy.

### Odpověď (Back)

Mějme konečnou podgrupu \(H\) grupy \(G\). Potom každá levá i pravá třída rozkladu \(G\) vzhledem k \(H \) má stejný počet prvků jako \(H\).

**Důkaz**
Ze vztahu\[[a]_{\mathcal L_H} = \{ ah \mid h \in H \}\]plyne, že počet prvků \([a]_{\mathcal L_H}\) je menší nebo roven \(\#H\). Sporem ukážeme, že musí platit rovnost. Předpokládejme, že velikost \([a]_{\mathcal L_H}\) je menší než \(\#H\). Pak musí existovat \(h_1, h_2 \in H\) taková, že \(h_1 \neq h_2\) a\[ah_1 = ah_2.\]To by však znamenalo, že \(h_1 = h_2\), což je spor.

### Doplňující pole (Extra)

Důkaz pro \(\mathcal R_H\) je obdobný.

## Poznámka Anki 1739887407523

Karty Anki: 1739887407523
GUID: Kdk]LN@`pG; štítky: ni-mky::p01.

### Otázka (Front)

Definujte index podgrupy.

### Odpověď (Back)

Mějme podgrupu \(H\) grupy \(G\) a nechť je počet různých tříd rozkladu \(G\) vzhledem k \(H\) konečný. Pak jej nazýváme indexgem podgrupy \(H\) v grupě \(G\) a značíme \([G : H]\).

## Poznámka Anki 1739888206675

Karty Anki: 1739888206675
GUID: HHRT;T$@IW; štítky: ni-mky::c01 ni-mky::p01.

### Otázka (Front)

Vyslovte a dokažte Lagrangeovu větu (větu o řádu grupy) pomocí indexu podgrupy.

### Odpověď (Back)

Mějme podgrupu \(H\) konečné grupy \(G\). Potom řád \(G\) je součinem řádu \(H\) a indexu \(H \) v \(G\), neboli řád \(H\) je dělitelem řádu \(G\):\[\#G = \#H \cdot [ G : H ].\]
**Důkaz** 
Důkaz plyne z lemmatu o počtu prvků levé a pravé třídy rozkladu grupy, které tvrdí, že všechny třídy rozkladu grupy \(G\) vzhledem k \(H\) mají stejný počet prvků jako \(H\). Navíc víme, že index \(H\) v \(G\) je definován jako počet různých tříd rozkladu a že jednotlivé třídy rozkladu jsou vzájemně disjunktní.

### Doplňující pole (Extra)

Rovnost výše lze formulovat ještě názorněji jako\[[G : H] = \frac{\#G}{\#H}.\]

## Poznámka Anki 1739888324183

Karty Anki: 1739888324183
GUID: F#+FvFqHQ_; štítky: ni-mky::p01.

### Otázka (Front)

Vyslovte redukovanou Sylwovovu větu.

### Odpověď (Back)

Mějme konečnou grupu \(G\) řádu \(p^nm\), kde \(p\) je prvočíslo takové, že \(p \nmid m\) a \(n \in \mathbb N\). Potom v \(G\) existují podgrupy řádu \(p \) a \(p^n\).

## Poznámka Anki 1739888388149

Karty Anki: 1739888388149
GUID: J&;E>jn+J5; štítky: ni-mky::c01 ni-mky::p01.

### Otázka (Front)

Definujte normální podgrupu. Co platí pro abelovské grupy?

### Odpověď (Back)

Podgrupu \(H\) grupy \(G\) nazýváme normální podgrupou, jestliže platí\[aha^{-1} \in H\]pro každé \(a \in G\) a \(h \in H\). Z předpisu výše plyne, že každá podgrupa \(H\) abelovské grupy \(G\) je normální podgrupou.

 [Obrázek: paste-1f7bb7206e16c347d6cb3431fcf9244e8d227526.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1739889354435

Karty Anki: 1739889354435
GUID: c%)<*]>V^8; štítky: ni-mky::p01.

### Otázka (Front)

Vyslovte a dokažte větu o vztahu normální podgrupy s třídami rozkladu grupy.

### Odpověď (Back)

Podgrupa \(H \) grupy \(G\) je normální, právě když je každá levá třída rozkladu \(aH\) totožná s pravou třídou rozkladu \(Ha\) pro každé \(a \in G\).

**Důkaz pro „**\(\Rightarrow\)**“**
Nejprve dokážeme inkluzi \(aH \subset Ha\). Mějme \(b \in aH\), potom existuje \(h \in H\) tak, že\[b = ah = ahe = aha^{-1}a.\]Protože \(H\) je podle předpokladu normální, tak platí \(\tilde h = aha^{-1} \in H\). Z toho plyne, že\[b = \tilde ha \in Ha.\]Analogicky lze ukázat i inkluzi \(Ha \subset aH\), z čehož plyne \(aH = Ha\).

**Důkaz pro „**\(\Leftarrow\)**“
**Mějme \(a \in G\) a \(h \in H\). Potom\[aha^{-1} = \tilde h a a^{-1} = \tilde h \in H,\]kde\[ah = \tilde ha,\]protože \(ah \in aH\) a zároveň podle předpokladu \(aH = Ha\), musí existovat \(\tilde h \in H\) tak, aby \(\tilde ha \in Ha\).

