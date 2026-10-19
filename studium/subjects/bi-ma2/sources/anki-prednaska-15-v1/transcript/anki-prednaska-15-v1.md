# BI-MA2 – Přednáška 15

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1669644732543

Karty Anki: 1669644732543
GUID: e9r)?%_pZ5; štítky: bi-ma2::p15 bi-spol::16.

### Otázka (Front)

Definujte kvadratickou formu.

### Odpověď (Back)

Funkci \(q : \mathbb R ^n \to \mathbb R\) nazýváme kvadratickou formou, právě když existuje symetrická matice \(\mathbf M \in \mathbb R^{n,n}\) splňující
\[q(\mathbf x) = \sum \limits_{j,k = 1}^n \mathbf M_{j,k} \mathbf x_j \mathbf x_k, \quad \text{pro každé } \mathbf x = (x_1, \dots, x_n)^T \in \mathbb R^n.\]

## Poznámka Anki 1669645012205

Karty Anki: 1669645012205
GUID: dV:6Xxh.]_; štítky: bi-ma2::p15 bi-spol::16 duplicate.

### Otázka (Front)

Definujte typy definitnosti kvadratických forem.

### Odpověď (Back)

Kvadratickou formu \(q : \mathbb R^n \to \mathbb R\) nazveme:

- **pozitivně definitní **(PD), právě když \(q(\mathbf x) > 0\) pro každé nenulové \(\mathbf x \in \mathbb R^n\).

- **pozitivně semidefinitní **(PSD), právě když \(q(\mathbf x) \geq 0\) pro každé \(\mathbf x \in \mathbb R^n\).
- **indefinitní **(ID), právě když existují vektory \(\mathbf x, \mathbf y \in \mathbb R^n\) splňující \(q(\mathbf x) > 0\) a \(q(\mathbf y) < 0\).
- **negativně semidefinitní **(NSD), právě když \(q(\mathbf x) \leq 0\) pro každé \(\mathbf x \in \mathbb R^n\).
- **negativně definitní **(ND), právě když \(q(\mathbf x) < 0\) pro každé nenulové \(\mathbf x \in \mathbb R^n\).

Stejnou terminologii budeme používat i pro symetrické matice \(\mathbf M\text{:} \, \mathbf M\) je typu \(T\), právě když forma \(\mathbf x ^T \mathbf M \mathbf x\) je typu \(T\).

## Poznámka Anki 1669645921947

Karty Anki: 1669645921947
GUID: Odl6jhis)H; štítky: bi-ma2::p15 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Vyslovte a dokažte pozorování o postačující podmínce pro indefinitnost.

### Odpověď (Back)

Mějme kvadratickou formu \(q(\mathbf x) = \mathbf x^T \mathbf M \mathbf x\), kde \(\mathbf M \in \mathbb R^{n,n}\) je symetrická matice. Pokud má \(\mathbf M\) na diagonále prvky s různým znaménkem (aspoň jeden kladný a aspoň jeden záporný), potom je \(q\) indefinitní.

**Důkaz** 
Dosazením \(j\)-tého standardního bazického vektoru \(\mathbf e_j\) do \(q\) dostaneme \(j\)-tý prvek na diagonále matice \(\mathbf M\), tedy
\[\mathbf M: q(\mathbf e_j) = \mathbf M_{jj}.\]Pokud má tedy \(\mathbf M\) na diagonále prvky s různým znaménkem, pak pro důkaz indefinitnosti volíme vektory \(\mathbf x, \mathbf y \in \mathbb R^n\) jako bazické vektory, které tyto prvky z diagonály „vyberou“.

## Poznámka Anki 1669646018852

Karty Anki: 1669646018852
GUID: cwdR9~q^|&; štítky: bi-ma2::p15.

### Otázka (Front)

Vyslovte větu o diagonalizaci symetrické reálné matice.

### Odpověď (Back)

Symetrická reálná matice je diagonalizovatelná a všechna její vlastní čísla jsou reálná. Vlastní vektory příslušející různým vlastním číslům jsou vzájemně ortogonální.

## Poznámka Anki 1669646179290

Karty Anki: 1669646179290
GUID: MH,R}4:Mm*; štítky: bi-ma2::p15 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Jaký je vztah mezi vlastními čísly matice \(\mathbf M\) a definitností příslušné kvadratické formy?

### Odpověď (Back)

Kvadratická forma \(q(\mathbf x) = \mathbf x^T \mathbf{Mx}\) je

- **PD**, právě když všechna vlastní čísla matice \(\mathbf M\) jsou kladná.
- **PSD**, právě když všechna vlastní čísla matice \(\mathbf M\) jsou nezáporná.
- **ID**, právě když má matice \(\mathbf M\) kladné i záporné vlastní číslo.
- **NSD**, právě když všechna vlastní čísla matice \(\mathbf M\) jsou nekladná.
- **ND**, právě když všechna vlastní čísla matice \(\mathbf M\) jsou záporná.

## Poznámka Anki 1669735597299

Karty Anki: 1669735597299
GUID: QJkm2TOt`V; štítky: bi-ma2::p15 bi-spol::16 duplicate ni-spol::03.

### Otázka (Front)

Vyslovte větu o Sylvestrově kritériu.

### Odpověď (Back)

Kvadratická forma \(q(\mathbf x) = \mathbf x^T \mathbf M \mathbf x\), kde \(\mathbf M \in \mathbb R^{n,n}\) je symetrická matice, je

- PD, právě když pro každé \(k \in \hat n\) platí \(\det \mathbf M_k > 0\).
- ND, právě když pro každé \(k \in \hat n\) platí \((-1)^k \det \mathbf M_k > 0\).

### Doplňující pole (Extra)

Matici \(\mathbf M_k\) definujeme pro všechna \(k \in \hat n\) jako matici typu \(\mathbb R^{k, k}\) v horním levém rohu matice \(\mathbf M\).

