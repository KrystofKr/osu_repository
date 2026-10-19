# NI-MKY – Přednáška 02

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MKY
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1739966066753

Karty Anki: 1739966066753
GUID: Eh+Tt_)m@9; štítky: duplicate ni-mky::p02.

### Otázka (Front)

Definujte homomorfismus, monomorfismus, epiformismus a izomorfismus grupoidů.

### Odpověď (Back)

Mějme dva grupoidy \(G = (M, \circ_G)\) a \(H = (N, \circ_H)\). Zobrazení \(h: M \to N\) nazveme **homomorfismem **\(G\) do \(H\), jestliže pro všechna \(x, y \in M\) platí\[h(x \circ_G y) = h(x) \circ_H h(y).\]Je-li navíc \(h\) injektivní resp. surjektivní resp. bijektivní, nazveme \(h\) **monomorfismem **resp. **epimorfismem **resp. **izomorfismem**.

## Poznámka Anki 1739966887694

Karty Anki: 1739966887694
GUID: b4jx#*|RWO; štítky: ni-mky::c01 ni-mky::p02.

### Otázka (Front)

Definujte jádro homomorfismu.

### Odpověď (Back)

Jádro homomorfismu \(f : G \to H\) je množina\[\ker f = \{ a \in G \mid f(a) = e_H \},\]kde \(e_H\) je neutrální prvek \(H\).

## Poznámka Anki 1739968752066

Karty Anki: 1739968752067
GUID: togPOGiKB1; štítky: ni-mky::p02.

### Otázka (Front)

Vyslovte a dokažte lemma o vztahu jádra homomorfismu a normální podgrupy.

### Odpověď (Back)

Mějme homomorfismus \(f : G \to H\). Jádro \(\ker f\) homomorfismu \(f\) je normální podgrupa grupy \(G\).

**Důkaz** 
Postupně dokážeme vlastnosti grupy:

- **uzavřenost **- mějme \(a, b \in \ker f\), potom\[f(a b) = f(a) f(b) = e_H  e_H = e_H,\]z čehož plyne, že \(a b \in \ker f\);
- **asociativita** - plyne z asociativity operace na \(G\);
- **existence neutrálního prvku** - mějme \(e_G  \in G\), potom\[f(e_G) = e_H,\]z čehož plyne, že \(e_G \in \ker f\);
- **existence inverzních prvků** - mějme \(a \in \ker f\) a \(a^{-1} \in G\), potom platí\[f(a^{-1}) = f(a^{-1}) e_H = f(a^{-1}) f(a) = f(a^{-1} a) = f(e_G) = e_H\]z čehož plyne, že \(a^{-1} \in \ker f\).

Zbývá dokázat, že \(\ker f\) je normální podgrupa grupy \(G\). Mějme \(a \in G\) a \(h \in \ker f\). Potom

\[f(aha^{-1}) = f(a) f(h) f(a^{-1}) = f(a) e_H f(a^{-1}) = f(a a^{-1}) = f(e_G) = e_H,\]z čehož plyne, že \(aha^{-1} \in \ker f\), a proto je \(\ker f\) normální.

## Poznámka Anki 1739977977275

Karty Anki: 1739977977276
GUID: vYtj^)a!k$; štítky: ni-mky::c01 ni-mky::p02.

### Otázka (Front)

Definujte faktorgrupu a dokažte, že se jedná o grupu.

### Odpověď (Back)

Mějme normální podgrupu \(H\) grupy \(G = (M, \circ)\). Faktorgrupou \(G\) vzhledem k \(H\) nazýváme grupu tvořenou třídami rozkladu \(G\) vzhledem k \(H\) společně s operací\[[a] \cdot [b] = [a \circ b]\]a značíme ji \(G/H\).

**Důkaz** 
Nejprve dokážeme, že operace výše je dobře definovaná. Mějme třídy rozkladu \([a]\) a \([b]\) a jejich další reprezentanty \(a' \in [a]\) a \(b' \in [b]\). Z toho plyne, že existují \(h_1, h_2 \in H\) taková, že\[\begin{matrix}
a' = ah_1,\\
b' = bh_2
\end{matrix}\]a dohromady\[a'b' = ah_1bh_2.\]Protože \(H\) je dle předpokladu normální, tak platí, že \(aH = Ha\), proto existuje \(h_3 \in H\) takové, že\[h_1b = bh_3,\]tedy\[a'b' = a b h_3 h_2.\]Protože \(H\) je grupa, tak \(h_3h_2 \in H\) a\[a'b' \in [ab].\]Nyní postupně dokážeme vlastnosti grupy:

- **uzavřenost **- plyne z předchozí části důkazu,

- **asociativita** - díky asociativitě operace na \(G\) platí:\[([a] \cdot [b]) \cdot [c] = [a \circ b] \cdot [c] = [(a \circ b) \circ c] = [a \circ (b \circ c)] = [a] \cdot [b \circ c] = [a] \cdot ([b] \cdot [c]),\]

- **existence neutrálního prvku** - neutrálním prvkem je \([e_G]\),
- **existence inverzního prvku** - inverzním prvkem k \([a] \) je \([a^{-1}]\).

## Poznámka Anki 1739981880187

Karty Anki: 1739981880187
GUID: M:lJNV.T4V; štítky: ni-mky::c01 ni-mky::p02.

### Otázka (Front)

Vyslovte větu o homomorfismu pro grupy.

### Odpověď (Back)

Mějme epimorfismus \(f : G \to G'\) grupy \(G\) na grupu \(G'\). Potom \(\ker f\) je normální podgrupa \(G\) a \(G'\) je izomorfní faktorgrupě \(G / \ker f\). Naopak, je-li \(H\) normální podgrupa grupy \(G\), pak zobrazení \(\psi : G \to G/H\) definované předpisem\[\psi(a) = aH\]pro \(a \in G\) je homomorfismem \(G\) a \(G/H\), přičemž \(\ker \psi = H\).

### Doplňující pole (Extra)

Epimorfismus je homomorfismus, který je surjektivní.

## Poznámka Anki 1739982191778

Karty Anki: 1739982191779
GUID: b6M3Cg9R|2; štítky: duplicate ni-mky::p02.

### Otázka (Front)

Vyslovte a dokažte větu o vztahu řádu grupy a neutrálního prvku.

### Odpověď (Back)

Mějme grupu \(G = (M, \circ)\) řádu \(n\). Pro všechny prvky \(a \in M\) platí, že
\[a^n = e,\]kde \(e \) je neutrální prvek.

**Důkaz** 
Víme, že grupa \(\langle a \rangle \) je podgrupou grupy \(G\). Dle Lagrangeovy věty o řádu grupy platí, že \(\# \langle a \rangle\) dělí \(n\) a dostáváme
\[a^n = a^{k \cdot \# \langle a \rangle} = (a^{\# \langle a \rangle})^k = (a^{\operatorname{ord} a})^k = e^k = e.\]

### Doplňující pole (Extra)

Z této věty vyplývá Malá Fermatova věta a Eulerova věta.

## Poznámka Anki 1739982314320

Karty Anki: 1739982314320
GUID: g$pJI:b`]F; štítky: duplicate ni-mky::p02.

### Otázka (Front)

Definujte cyklickou grupu (cyclic group) a generátor cyklické grupy.

### Odpověď (Back)

Grupa \(G = (M, \circ)\) se nazývá **cyklická**, pokud existuje prvek \(a \in M\) takový, že \(\langle a \rangle = G\). Tomuto prvku říkáme **generátor cyklické grupy** \(G\).

### Doplňující pole (Extra)

Všechny prvky patřící do \(\langle a \rangle\) získáme pomocí „grupového obalu:“\[\langle a \rangle = \{ a \circ a \circ \cdots \circ a = a^k : k \in \mathbb Z \}.\]

