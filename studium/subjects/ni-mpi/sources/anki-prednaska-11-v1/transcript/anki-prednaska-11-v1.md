# NI-MPI – Přednáška 11

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1732568380853

Karty Anki: 1732568380853
GUID: f8oUYlV7Rh; štítky: duplicate ni-mpi::p11 ni-spol::01.

### Otázka (Front)

Definujte homomorfismus, monomorfismus, epiformismus a izomorfismus grupoidů.

### Odpověď (Back)

Mějme dva grupoidy \(G = (M, \circ_G)\) a \(H = (N, \circ_H)\). Zobrazení \(h: M \to N\) nazveme **homomorfismem **\(G\) do \(H\), jestliže pro všechna \(x, y \in M\) platí\[h(x \circ_G y) = h(x) \circ_H h(y).\]Je-li navíc \(h\) injektivní resp. surjektivní resp. bijektivní, nazveme \(h\) **monomorfismem **resp. **epimorfismem **resp. **izomorfismem**.

## Poznámka Anki 1732568437499

Karty Anki: 1732568437499
GUID: x1pBP91Dco; štítky: ni-mpi::p11 ni-spol::01.

### Otázka (Front)

Definujte izomorfní grupy a tělesa.

### Odpověď (Back)

Grupy resp. tělesa \(G\) a \(H\) nazýváme izomorfní, právě když existuje izomorfismus \(G \to H\).

## Poznámka Anki 1732708235106

Karty Anki: 1732708235106
GUID: k<YX$jJxZ*; štítky: ni-mpi::p11 ni-spol::01.

### Otázka (Front)

Vyslovte větu o vlastnostech homomorfismu.

### Odpověď (Back)

Mějme homomorfismus \(h\) grupy \(G = (M, \circ _G)\) do grupoidu \(H = (N, \circ_H)\). Potom
\[h(G) := \big( h(M), \circ_H  \big)\]je grupa.

## Poznámka Anki 1732709010461

Karty Anki: 1732709010461
GUID: Kp!7.u{}AT; štítky: ni-mpi::p11 ni-spol::01.

### Otázka (Front)

Vyslovte větu o izomorfismu cyklických grup.

### Odpověď (Back)

Libovolné dvě cyklické grupy stejného řádu jsou izomorfní. Libovolná nekonečná grupa je izomorfní s \((\mathbb Z, +)\) a konečná grupa s \((\mathbb Z_n, +_n)\). Máme-li grupu \(G = \langle a \rangle\) s generátorem \(a\), pak hledaný izomorfismus je bijekce ze \(\mathbb Z\) resp. \(\mathbb Z_n\) na \(G\) definovaná jako\[h(k) = a^k.\]

### Doplňující pole (Extra)

Z toho vyplývá, že \((\mathbb Z, +)\) a \((\mathbb Z_n, +_n)\) jsou jediné cyklické grupy až na izomorfismus.

## Poznámka Anki 1732709659895

Karty Anki: 1732709659895
GUID: J5`79dbn1z; štítky: ni-mpi::p11 ni-spol::01.

### Otázka (Front)

Vyslovte Cayleyovu větu.

### Odpověď (Back)

Libovolná konečná grupa je izomorfní s nějakou grupou permutací.

## Poznámka Anki 1732710347370

Karty Anki: 1732710347370
GUID: e/abO/{!M?; štítky: duplicate ni-mpi::p11.

### Otázka (Front)

Definujte diskrétní logaritmus. Kdy je jeho existence zaručena?

### Odpověď (Back)

Nechť \((M, \circ)\) je grupa a \(a\), \(b\) a \(x\) jsou její prvky. Potom \(x\) nazveme diskrétním logaritmem \(a\) při základu \(b\), když platí
\[\log_b(a) = x \Leftrightarrow \underbrace {b \circ b \circ \dots \circ b}_{x\text{-krát}} = a.\]Tedy v multiplikativní grupě \((M, \times)\) platí
\[\log_b(a) = x \Leftrightarrow b^x = a,\]a v aditivní grupě \((M, +)\) platí
\[\log_b(a) = x \Leftrightarrow x \cdot b = a.\]Existence diskrétního logaritmu je zaručena v případě, že \((M, \circ)\) je cyklická grupa a \(b\) je její generátor.

