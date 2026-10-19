# NI-MPI – Přednáška 15

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 2 poznámek, 2 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1734631976007

Karty Anki: 1734631976007
GUID: i#Q#(tuQa(; štítky: ni-mpi::p15 ni-spol::05.

### Otázka (Front)

Vyslovte lemma o načítání chyb.

### Odpověď (Back)

Mějme \(| \delta_i | \leq \mathbf u\) a \(| \rho_i| = 1\) pro všechna \(i \in \hat n\), \(n \in \mathbb N\) a nechť \(n \mathbf u < 1\). Potom\[\prod_{i = 1}^n (1 + \delta_i)^{\rho_i} = 1 + \Theta_n,\]kde\[| \Theta_n| \leq \frac{n \mathbf u}{1 - n \mathbf u}.\]

## Poznámka Anki 1734632178666

Karty Anki: 1734632178666
GUID: J>Fy5Ry|lV; štítky: ni-mpi::p15 ni-spol::05.

### Otázka (Front)

Popište značení počtu nakumulovaných chyb.

### Odpověď (Back)

Počet nakumulovaných chyb se značí\[\langle n \rangle = \prod_{i = 1}^n(1 + \delta_i)^{\rho_i},\]kde \(n \in \mathbb N\) je počet chyb a platí
\[\begin{matrix}
\langle j \rangle \cdot \langle k \rangle = \langle j + k \rangle,\\
\displaystyle \frac{\langle j \rangle}{\langle k \rangle} = \langle j + k \rangle.
\end{matrix}\]

### Doplňující pole (Extra)

Jedná se o velmi volné značení, tedy nemusí nutně platit\[\langle n \rangle \stackrel{?}{=} \langle n \rangle.\]

