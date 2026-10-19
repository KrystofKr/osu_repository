# NI-VSM – Přednáška 06

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-VSM
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1741213611827

Karty Anki: 1741213611827
GUID: L(WaH?|Ud; štítky: ni-vsm::p06.

### Otázka (Front)

Definujte kód a kódové slovo.

### Odpověď (Back)

Mějme \(D\)-ární abecedu \(\mathcal D\). Zobrazení \(C : \mathcal X \to \mathcal D^*\), kde \(\mathcal D^*\) je množina konečných řetězců symbolů \(\mathcal D\), tedy\[\mathcal D^* = \displaystyle \bigcup_{n \in \mathbb N} \mathcal D^n,\]nazýváme \(D\)**-árním kódem diskrétní náhodné veličiny**. Obraz \(C(x)\) prvku \(x \in \mathcal X\) nazýváme **kódové slovo** příslušející prvku \(x\) a jeho délku značíme \(\ell(x)\).

## Poznámka Anki 1741213808508

Karty Anki: 1741213808508
GUID: O}tF(bLcID; štítky: ni-vsm::p06.

### Otázka (Front)

Definujte střední délku kódu.

### Odpověď (Back)

Střední délka kódu \(C\) náhodné veličiny \(X\) s rozdělením \(p(x)\) je definována vztahem\[L(C) = \displaystyle \sum_{x \in \mathcal X} \ell(x) p(x),\]

## Poznámka Anki 1741214327909

Karty Anki: 1741214327909
GUID: i`RKkPuv[B; štítky: ni-vsm::p06.

### Otázka (Front)

Definujte nesingulární kód.

### Odpověď (Back)

Kód diskrétní náhodné veličiny je nesingulární, pokud je prostým zobrazenín.

## Poznámka Anki 1741214600742

Karty Anki: 1741214600742
GUID: c8=Q`%TcMs; štítky: ni-vsm::p06.

### Otázka (Front)

Definujte rozšíření kódu a jednoznačně (unikátně) dekódovatelný kód.

### Odpověď (Back)

**Rozšíření **\(C^*\)** kódu **\(C \) je zobrazení množiny \(\mathcal X^*\) do množiny \(\mathcal D^*\) definované jako\[C^*(x_1 x_2 \cdots x_n) = C(x_1) C(x_2) \cdots C(x_n),\]kde \(C(x_1) C(x_2) \cdots C(x_n)\) znamená zápis jednotlivých kódových slov za sebe a \(\mathcal X^*\) značí množinu všech konečných řetězců symbolů z \(\mathcal X\). Kód \(C\) je **jednoznačně** (unikátně) **dekódovatelný**, pokud je \(C^*\) nesingulární.

### Doplňující pole (Extra)

Každý jednoznačně (unikátně) dekódovatelný kód je nesingulární.

## Poznámka Anki 1741264094102

Karty Anki: 1741264094102
GUID: g_nA7wh(.E; štítky: ni-vsm::p06.

### Otázka (Front)

Definujte instantní (prefixový) kód.

### Odpověď (Back)

Kód diskrétní náhodné veličiny je instantní (prefixový), pokud žádné kódové slovo není prefixem jiného kódového slova.

### Doplňující pole (Extra)

Každý instantní (prefixový) kód je jednoznačně dekódovatelný.

## Poznámka Anki 1741267190737

Karty Anki: 1741267190737
GUID: Bbxb/LqfL@; štítky: ni-vsm::p06.

### Otázka (Front)

Vyslovte větu o Kraftově nerovnosti.

### Odpověď (Back)

Pro libovolný instantní kód nad \(D\)-ární abecedou musí délky kódových slov \(\ell_1, \ell_2, \dots, \ell_n\) splnit nerovnost\[\displaystyle \sum_i D^{-\ell_i} \leq 1.\]Navíc platí, že ke každé \(n\)-tici délek, které splní tuto nerovnost, existuje instantní kód s kódovými slovy těchto délek.

## Poznámka Anki 1741277803041

Karty Anki: 1741277803041
GUID: wR~`9c%v1S; štítky: ni-vsm::p06.

### Otázka (Front)

Vyslovte McMillanovu větu.

### Odpověď (Back)

Podle McMillanovy věty platí Kraftova nerovnost i pro jednoznačně dekódovatelné kódy. Z toho plyne, že ke každému jednoznačně dekódovatelnému kódu lze sestrojit instantní kód, který má stejně dlouhá kódová slova a tedy i stejnou střední délku kódu.

## Poznámka Anki 1741278175382

Karty Anki: 1741278175383
GUID: Eoi[cTC4CM; štítky: ni-vsm::p06.

### Otázka (Front)

Vyslovte větu o dolní mezi střední délky instantního kódu.

### Odpověď (Back)

Střední dílka instantního \(D\)-ářního kódu \(C\) diskrétní náhodné veličiny \(X\) je\[L(C) \geq H_D(X),\]přičemž rovnost nastává právě tehdy, když\[D^{-\ell_i} = p_i\]pro všechna \(i = 1, \dots, | \mathcal X |\).

## Poznámka Anki 1741278477229

Karty Anki: 1741278477229
GUID: mnfl9&,yK[; štítky: ni-vsm::p06.

### Otázka (Front)

Vyslovte větu o entropii náhodné veličiny a střední délce jejího optimálního instantního kódu.

### Odpověď (Back)

Pro optimální instantní \(D\)-ární kód \(C^*\) diskrétní náhodné veličiny \(X\) platí\[H_D(X) \leq L(C^*) < H_D(X) + 1.\]

## Poznámka Anki 1742152543495

Karty Anki: 1742152543495
GUID: pMe-=8FCme; štítky: ni-vsm::p06.

### Otázka (Front)

Vyslovte větu o optimalitě Huffmanova kódu.

### Odpověď (Back)

Huffmanův kód je optimální, tedy je-li \(C^*\) Huffmanův od a \(C'\) libovolný jednoznačně dekódovatelný kód, potom\[L(C^*) \leq L(C').\]

