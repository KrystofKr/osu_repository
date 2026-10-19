# NI-MPI – Přednáška 02

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1727626942515

Karty Anki: 1727626942515
GUID: B?nhG)Y}E7; štítky: duplicate ni-mpi::p02.

### Otázka (Front)

Definujte Hessovu matici funkce v bodě.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(\mathbf a \in A \subset D_f\) takový, že \(f\) má v bodě \(\mathbf a\) všechny druhé parciální derivace. Hessova matice funkce \(f \) v bodě \(\mathbf a\) je matice typu \(\mathbb R^{n, n}\)\[      \begin{pmatrix}

        \frac{\partial^2 f}{\partial x_1^2}(\mathbf a) & \frac{\partial^2 f}{\partial x_2 \partial x_1}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_n \partial x_1}(\mathbf a) \\

        \frac{\partial^2 f}{\partial x_1 \partial x_2}(\mathbf a) & \frac{\partial^2 f}{\partial x_2^2}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_n \partial x_2}(\mathbf a) \\

        \vdots & \vdots & \cdots & \vdots \\

        \frac{\partial^2 f}{\partial x_1 \partial x_n}(\mathbf a) & \frac{\partial^2 f}{\partial x_2 \partial x_n}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_n^2}(\mathbf a)

      \end{pmatrix}\]a značíme ji \(\nabla^2 f(\mathbf a).\)

### Doplňující pole (Extra)

Pokud na gradient („derivaci“) funkce \(f\) nahlédneme jako na zobrazení \(Df : A \to \mathbb R^n\), \(A \subset D_f\), pak je Hessova matice derivací tohoto zobrazení v bodě \(\mathbf a \in A\).
**V předmětu NI-MPI **je pořadí parciálních derivací prohozeno a Hessova matice je tedy definována jako\[      \nabla^2 f(\mathbf a) = \begin{pmatrix}

        \frac{\partial^2 f}{\partial x_1^2}(\mathbf a) & \frac{\partial^2 f}{\partial x_1 \partial x_2}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n}(\mathbf a) \\

        \frac{\partial^2 f}{\partial x_2 \partial x_1}(\mathbf a) & \frac{\partial^2 f}{\partial x_2^2}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n}(\mathbf a) \\

        \vdots & \vdots & \cdots & \vdots \\

        \frac{\partial^2 f}{\partial x_n \partial x_1}(\mathbf a) & \frac{\partial^2 f}{\partial x_n \partial x_2}(\mathbf a) & \cdots & \frac{\partial^2 f}{\partial x_n^2}(\mathbf a)

      \end{pmatrix}.\]

## Poznámka Anki 1727627136929

Karty Anki: 1727627136930
GUID: i@_OXm>ef$; štítky: ni-mpi::p02 ni-spol::03.

### Otázka (Front)

Vyslovte větu o zaměnitelnosti druhých parciálních derivací.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(\mathbf a \in D_f\). Pokud existuje \(\frac {\partial^2 f}{\partial x \partial y}(\mathbf a)\) a je v bodě \(\mathbf a\) spojitá, pak existuje i \(\frac {\partial^2 f}{\partial y \partial x}(\mathbf a)\) a platí
\[\frac {\partial^2 f}{\partial x \partial y}(\mathbf a) = \frac {\partial^2 f}{\partial y \partial x}(\mathbf a).\]

## Poznámka Anki 1727627587580

Karty Anki: 1727627587580
GUID: K1{l<uvyP/; štítky: ni-mpi::p02 ni-spol::03.

### Otázka (Front)

Definujte druhou derivaci funkce ve směru v bodě a vyslovte větu o jejím výpočtu.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\), bod \(\mathbf a \in D_f\) takový, že \(f\) je definovaná na nějakém jeho okolí \(H(a)\) a vektor \(\mathbf s \in \mathbb R^{n, 1}\) takový, že \(\| \mathbf s \| = 1\). Druhá paricální derivace funkce \(f\) ve směru \(\mathbf s\) v bodě \(\mathbf a\) je\[\nabla_\mathbf s (\nabla_\mathbf s f)(\mathbf a).\]Pokud navíc platí, že má \(f\) na \(H(\mathbf a)\) spojité všechny druhé parciální derivace, pak\[\nabla_\mathbf s (\nabla_\mathbf s f)(\mathbf a) = \mathbf s^T \cdot \nabla^2 f(\mathbf a) \cdot \mathbf s.\]

## Poznámka Anki 1727627689297

Karty Anki: 1727627689297
GUID: Rb.efwBbdE; štítky: duplicate ni-mpi::p02.

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

## Poznámka Anki 1727627709365

Karty Anki: 1727627709365
GUID: H`SyDtzy)L; štítky: duplicate ni-mpi::p02.

### Otázka (Front)

Jaký je vztah mezi vlastními čísly matice \(\mathbf M\) a definitností příslušné kvadratické formy?

### Odpověď (Back)

Kvadratická forma \(q(\mathbf x) = \mathbf x^T \mathbf{Mx}\) je

- **PD**, právě když všechna vlastní čísla matice \(\mathbf M\) jsou kladná.
- **PSD**, právě když všechna vlastní čísla matice \(\mathbf M\) jsou nezáporná.
- **ID**, právě když má matice \(\mathbf M\) kladné i záporné vlastní číslo.
- **NSD**, právě když všechna vlastní čísla matice \(\mathbf M\) jsou nekladná.
- **ND**, právě když všechna vlastní čísla matice \(\mathbf M\) jsou záporná.

## Poznámka Anki 1727627850006

Karty Anki: 1727627850006
GUID: MK-%m>+~3u; štítky: duplicate ni-mpi::p02.

### Otázka (Front)

Vyslovte větu o Sylvestrově kritériu.

### Odpověď (Back)

Kvadratická forma \(q(\mathbf x) = \mathbf x^T \mathbf M \mathbf x\), kde \(\mathbf M \in \mathbb R^{n,n}\) je symetrická matice, je

- PD, právě když pro každé \(k \in \hat n\) platí \(\det \mathbf M_k > 0\).
- ND, právě když pro každé \(k \in \hat n\) platí \((-1)^k \det \mathbf M_k > 0\).

### Doplňující pole (Extra)

Matici \(\mathbf M_k\) definujeme pro všechna \(k \in \hat n\) jako matici typu \(\mathbb R^{k, k}\) v horním lelém rohu matice \(\mathbf M\).

## Poznámka Anki 1727627876872

Karty Anki: 1727627876872
GUID: qN>txX2QXO; štítky: duplicate ni-mpi::p02.

### Otázka (Front)

Vyslovte a dokažte pozorování o postačující podmínce pro indefinitnost.

### Odpověď (Back)

Mějme kvadratickou formu \(q(\mathbf x) = \mathbf x^T \mathbf M \mathbf x\), kde \(\mathbf M \in \mathbb R^{n,n}\) je symetrická matice. Pokud má \(\mathbf M\) na diagonále prvky s různým znaménkem (aspoň jeden kladný a aspoň jeden záporný), potom je \(q\) indefinitní.

**Důkaz** 
Dosazením \(j\)-tého standardního bazického vektoru \(\mathbf e_j\) do \(q\) dostaneme \(j\)-tý prvek na diagonále matice \(\mathbf M\), tedy
\[\mathbf M: q(\mathbf e_j) = \mathbf M_{jj}.\]Pokud má tedy \(\mathbf M\) na diagonále prvky s různým znaménkem, pak pro důkaz indefinitnosti volíme vektory \(\mathbf x, \mathbf y \in \mathbb R^n\) jako bazické vektory, které tyto prvky z diagonály „vyberou“.

## Poznámka Anki 1727627977071

Karty Anki: 1727627977071
GUID: Ibvbz57^qm; štítky: duplicate ni-mpi::p02.

### Otázka (Front)

Vyslovte větu o postačující podmínce existence lokálního extrému.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(\mathbf a \in D_f\) takový, že \(f\) má na okolí bodu \(\mathbf a\) spojité všechny třetí parciální derivace. Pokud jsou splněny následující podmínky:

- \(\nabla f(\mathbf a) = \theta\) (\(\mathbf a\) je stacionární bod),

- \(\nabla^2f(\mathbf a)\) je pozitivně definitní (PD) resp. negativně definitní (ND),

pak má  \(f\) v bodě  \(\mathbf a\) ostré lokální minimum resp. ostré lokální maximum. Pokud je Hessova matice \(\nabla^2f(\mathbf a)\) indefinitní (ID), pak se v bodě \(\mathbf a\) nachází sedlový bod a funkce \(f\) v něm lokální extrém nemá.

### Doplňující pole (Extra)

**V předmětu NI-MPI je požadována spojitost pouze druhých parciálních derivací.**

## Poznámka Anki 1727628082650

Karty Anki: 1727628082650
GUID: dtH6nV5^$m; štítky: duplicate ni-mpi::p02.

### Otázka (Front)

Vyslovte větu o nutné podmínce existence lokálního extrému funkce II.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(\mathbf a \in D_f\) takový, že \(f \) má v bodě \(\mathbf a\) lokální minimum resp. maximum a spojité všechny druhé parciální derivace na jeho okolí. Potom je \(\nabla^2 f(\mathbf a)\) Hessova matice funkce \(f\) v bodě \(\mathbf a\) pozitivně semidefinitní (PSD) resp. negativně semidefinitní (NSD).

### Doplňující pole (Extra)

**V předmětu NI-MPI **je požadován bod \(a \in D_f\) takový, že je stacionárním bodem \(f\).

## Poznámka Anki 1727628361539

Karty Anki: 1727628361539
GUID: wp5i{>sxIT; štítky: ni-mpi::p02.

### Otázka (Front)

Definujte konvexnost a konkávnost pro funkci více proměnných.

### Odpověď (Back)

Funkce \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) je **konvexní**, pokud je \(D_f\) konvexní množina a 
\[\forall \mathbf a_1, \mathbf a_2 \in D_f, \forall t \in \langle 0, 1 \rangle : f(t \mathbf a_1 + (1 - t) \mathbf a_2) \leq tf(\mathbf a_1) + (1 - t)f(\mathbf a_2).\]Funkci \(f\) nazveme **konkávní**, pokud je \(-f\) konvexní.

## Poznámka Anki 1727628613560

Karty Anki: 1727628613560
GUID: He=GJ{3x[e; štítky: ni-mpi::p02 ni-spol::03.

### Otázka (Front)

Vyslovte větu o vztahu definitnosti Hessovy matice a konvexity.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R^n\), \(D_f \subset \mathbb R\) a nechť má spojité všechny druhé parciální derivace. Funkce \(f\) je konvexní právě tehdy, když je její Hessova matice pozitivně semidefinitní (PSD) ve všech bodech vnitřku \(D_f\).

### Doplňující pole (Extra)

Vnitřkem množiny rozumíme všechny její body, které v ní leží s nějakým okolím.

