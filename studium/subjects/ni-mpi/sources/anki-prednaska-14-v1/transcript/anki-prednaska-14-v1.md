# NI-MPI – Přednáška 14

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1733918243990

Karty Anki: 1733918243994
GUID: f!+wH?lXFU; štítky: ni-mpi::p14 ni-spol::05.

### Otázka (Front)

Definujte dopřednou chybu (forward error) a zpětnou chybu (backward error).

### Odpověď (Back)

Mějme numerický algoritmus \(V\) a vstupní data \(d\). **Dopřednou chybou **(forward error) \(\Delta v\) rozumíme odchylku spočítaného řešení \(V(d)\) od teoretického přesného řešení \(V^*(d)\), tedy\[\Delta v = V^*(d) - V(d).\]**Zpětnou chybou **(backward error) je promítnutí chyby algoritmu \(V\) do jeho vstupu, tedy nejmenší \(\Delta d\) takové, že\[V^*(d + \Delta d) = V(d).\]

## Poznámka Anki 1733918322744

Karty Anki: 1733918322744
GUID: oC)MK,KE35; štítky: ni-mpi::p14 ni-spol::05.

### Otázka (Front)

Definujte zpětně stabilní (backward stable) numerický algoritmus.

### Odpověď (Back)

Numerický algoritmus je zpětně stabilní (backward stable), jestliže je jeho zpětná chyba (backward error) malá pro všechny vstupy.

## Poznámka Anki 1733918507616

Karty Anki: 1733918507616
GUID: KGtlH=47zs; štítky: ni-mpi::p14 ni-spol::05.

### Otázka (Front)

Definujte podmíněnost numerické úlohy, dobře podmíněnou (well-conditioned) a špatně podmíněnou (ill-conditioned) numerickou úlohu.

### Odpověď (Back)

**Podmíněnost** úlohy vyjadřuje závislost změny výstupu na změně (malé perturbaci) vstupních dat. Úlohu nazveme **dobře podmíněnou **(well-conditioned), je-li relativní číslo podmíněnosti (relative condition number) \(C_r \approx 1\). Je-li naopak velké, řekneme, že úloha je **špatně podmíněná** (ill-conditioned).

## Poznámka Anki 1733937457351

Karty Anki: 1733937457351
GUID: Jzj(~hzO<e; štítky: ni-mpi::p14 ni-spol::05.

### Otázka (Front)

Definujte přidruženou maticovou normu.

### Odpověď (Back)

Přidruženou maticovou normu pro nějakou vektorovou normu \(\| \cdot \| \) na \(\mathbb R^n\) definujeme jako
\[\| \mathbf A \| := \sup \{ \| \mathbf{Ax} \| : \mathbf x \in \mathbb R^{n, 1} \land \| \mathbf x \| = 1 \}.\]Takto definovaná norma tedy splňuje vlastnosti normy, jako je konzistence a submultiplikativita.

## Poznámka Anki 1733938877627

Karty Anki: 1733938877627
GUID: v4m[BqkA27; štítky: ni-mpi::p14 ni-spol::05.

### Otázka (Front)

Popište úlohu řešení soustavy lineárních rovnic a její podmíněnost.

### Odpověď (Back)

Mějme soustavu \(n \in \mathbb N\) lineárních rovnic pro \(n\) neznámých v maticovém tvaru\[\mathbf{Ax} = \mathbf b,\]kde \(\mathbf A \in \mathbb R^{n, n}\) je regulární matice soustavy, \(\mathbf b \in \mathbb R^{n, 1}\) je vektor pravých stran a \(\mathbf x \in \mathbb R^{n, 1}\) je hledané řešení. Předpokládejme nyní, že \(\mathbf b \neq 0\), a proveďme změnu (perturbaci) \(\mathbf b\) o \(\delta \mathbf b\). Označíme-li změnu v řešení \(\mathbf x\) symbolem \(\delta \mathbf x\), pak\[\mathbf A(\mathbf x + \delta \mathbf x) = \mathbf{Ax} + \mathbf A \delta \mathbf x = \mathbf b + \delta \mathbf b.\]Nyní odhadneme \(\| \delta \mathbf x \|\) vztahem\[\| \delta \mathbf x \| = \| \mathbf A^{-1} \delta \mathbf b \| \stackrel{1.}{\leq} \| \mathbf A^{-1} \| \cdot \| \delta b\|\]a \(\frac 1 {\| \mathbf x \|}\) vztahem\[\| \mathbf b \| = \| \mathbf{Ax} \| \stackrel{1.}{\leq} \| \mathbf A \| \cdot \| \mathbf x \| \Rightarrow \frac 1 {\| \mathbf x \|} \leq \frac{\| \mathbf A \|}{\| \mathbf b \|}.\]Pokud oba odhady složíme, získáme\[\frac{\| \delta \mathbf x \|}{\| \mathbf x \|} \leq \underbrace{\| \mathbf A \| \cdot \| \mathbf A^{-1} \|}_{\kappa(\mathbf A)} \cdot \frac{\| \delta \mathbf b \|}{\| \mathbf b \|},\]kde \(\kappa(\mathbf A)\) nazýváme číslem podmíněnosti matice \(\mathbf A\). Z této nerovnosti vyplývá, že relativní chyba v řešení \(\mathbf x\) soustavy je menší než relativní chyba pravé strany \(\mathbf b\) vynásobená číslem podmíněnosti. Čím je \(\operatorname \kappa(\mathbf A)\) větší, tím je úloha hůře podmíněná.

### Doplňující pole (Extra)

V rovnostech využíváme:

1. submultiplikativitu přidružené maticové normy.

## Poznámka Anki 1733939961311

Karty Anki: 1733939961311
GUID: w<MX3C5lAm; štítky: ni-mpi::p14.

### Otázka (Front)

Popište iterační metodu řešení soustavy lineárních rovnic.

### Odpověď (Back)

Iterační metoda řešení soustavy lineárních rovnic spočívá v tom, že je nejprve zvolen náhodný počáteční vektor \(\mathbf x_0 \in \mathbb R^n\) a regulární matice \(\mathbf Q \in \mathbb R^{n, n}\). Následně je konstruována posloupnost \((\mathbf x_k)_{k = 0}^\infty\) pomocí rekurentního předpisu\[\mathbf x_k = \mathbf Q^{-1} \big( (\mathbf Q - \mathbf A) \mathbf x_{k - 1} + \mathbf b \big)\]Provedeme-li ekvivalentní úpravu, bude mít posloupnost pro \(k \to \infty\) a vhodnou volbu \(\mathbf Q\) za limitu hledané řešení soustavy:\[\begin{matrix}
\mathbf Q \mathbf x_\infty = (\mathbf Q - \mathbf A) \mathbf x_\infty + \mathbf b,\\
\mathbf{Ax}_\infty = \mathbf b.
\end{matrix}\]

## Poznámka Anki 1733940891157

Karty Anki: 1733940891158
GUID: MOQ9gi8qBL; štítky: ni-mpi::p14.

### Otázka (Front)

Definujte vektor chyby a popište požadavky na volbu matice \(\mathbf Q\) v iterační metodě řešení soustavy lineárních rovnic.

### Odpověď (Back)

**Vektor chyby** v \(k\)-té iteraci iterační metody řešení soustavy lineárních rovnic definujeme vztahem\[\begin{matrix}
\mathbf e_k = \mathbf x_k - \mathbf x_\infty = \mathbf Q^{-1} \big( (\mathbf Q - \mathbf A) \mathbf x_{k - 1} + \mathbf b \big) - \mathbf x_\infty = (\mathbf E - \mathbf Q^{-1} \mathbf A)(\mathbf x_{k - 1} - \mathbf x_\infty) = (\mathbf E - \mathbf Q^{-1} \mathbf A) \mathbf e_{k - 1}.
\end{matrix}\]Označíme-li \(\mathbf W := \mathbf E - \mathbf Q^{-1} \mathbf A\), pak\[\mathbf e_k = \mathbf{We}_{k - 1} = \mathbf W^2 \mathbf e_{k - 2} = \dots = \mathbf W^k \mathbf e_0.\]**Matici** \(\mathbf Q\) volíme tedy tak, aby\[\displaystyle \lim_{k \to \infty} \mathbf W^k = 0,\]což platí právě tehdy, když \(\operatorname \rho(\mathbf W) < 1\), kde \(\rho\) je spektrální poloměr.

## Poznámka Anki 1733941128521

Karty Anki: 1733941128521
GUID: x7rET;*X%@; štítky: ni-mpi::p14.

### Otázka (Front)

Definujte spektrální poloměr matice.

### Odpověď (Back)

Spektrální poloměr \(\operatorname \rho(\mathbf M)\) matice \(\mathbf M \in \mathbb C^{n, n}\) je maximum absolutních hodnot vlastních čísel matice \(\mathbf M\):\[\operatorname \rho(\mathbf M) := \max \{ |\lambda| : \lambda \in \operatorname \sigma(\mathbf M) \},\]kde \(\operatorname \sigma(\mathbf M)\) je spektrum matice \(\mathbf M\).

## Poznámka Anki 1733942074175

Karty Anki: 1733942074175
GUID: K/WI37|B]j; štítky: ni-mpi::p14.

### Otázka (Front)

Popište rychlost konvergence iterační metody řešení soustavy lineárních rovnic.

### Odpověď (Back)

Mějme vektor chyby \(\mathbf e_k\) v \(k\)-té iteraci iterační metody řešení soustavy lineárních rovnic a matici \(\mathbf W := (\mathbf E - \mathbf Q^{-1} \mathbf A)\). Z odhadu\[\| \mathbf e_k \| = \| \mathbf W^k \mathbf e_0\| \stackrel{1.}{\leq} \| \mathbf W^k \| \cdot \| \mathbf e_0\| \stackrel{1.}{\leq} \| \mathbf W \|^k \cdot \| \mathbf e_0 \|\]plyne, že metoda konverguje, neboli \(\mathbf e_k\) jde k nule, pro \(\| \mathbf W \| < 1\). Pro symetrické matice je chování \(\mathbf W^k\) závislé na \(\operatorname \rho(\mathbf W)\) a obecně platí, že čím je menší \(\| \mathbf W \|\), tím rychlejší bude konvergence.

### Doplňující pole (Extra)

V rovnostech využíváme:

1. submultiplikativitu přidružené maticové normy.

## Poznámka Anki 1733942486463

Karty Anki: 1733942486463
GUID: t%TXL.}5~d; štítky: ni-mpi::p14.

### Otázka (Front)

Popište kritérium zastavení iterační metody řešení soustavy lineárních rovnic.

### Odpověď (Back)

Kritérium zastavení iterační metody řešení soustavy lineárních rovnic je pro \(\varepsilon > 0\) definováno jako\[\| \mathbf{Ax}_k - \mathbf b \| < \varepsilon,\]případně se za předpokladu \(\| \mathbf W \| < 1\) používá\[\| \mathbf e_k \| < \frac \varepsilon {1 - \| \mathbf W \|}.\]V nepřesné aritmetice metoda ale nemusí konvergovat ani v případě, že není špatně podmíněná. Proto je často jejím dalším parametrem maximální počet iterací, po kterém je metoda ukončena a prohlášena za neúspěšnou.

### Doplňující pole (Extra)

Platí, že \(\mathbf W = \mathbf E - \mathbf Q^{-1} \mathbf A\).

## Poznámka Anki 1733942819280

Karty Anki: 1733942819280
GUID: I[_U.??Jbr; štítky: ni-mpi::p14.

### Otázka (Front)

Popište Richardsonovu iterační metodu řešení soustavy lineárních rovnic.

### Odpověď (Back)

Richardsonova iterační metoda řešení soustavy lineárních rovnic je varianta iterační metody řešení soustavy lineárních rovnic, kde\[\mathbf Q = \mathbf E.\]Konvergence je kontrolována maticí\[\mathbf W = \mathbf E - \mathbf Q^{-1} \mathbf A = \mathbf E - \mathbf A\]a je splněna pouze pro matice \(\mathbf A\) dostatečně blízko \(\mathbf E\), tedy např. pro matice splňující\[\| \mathbf E - \mathbf A \| < 1.\]

## Poznámka Anki 1733943021630

Karty Anki: 1733943021630
GUID: AiFU*IST/5; štítky: ni-mpi::p14.

### Otázka (Front)

Popište Jacobiho iterační metodu řešení soustavy lineárních rovnic.

### Odpověď (Back)

Jacobiho iterační metoda řešení soustavy lineárních rovnic je varianta iterační metody řešení soustavy lineárních rovnic, kde\[\mathbf Q = \mathbf D,\]přičemž matice \(\mathbf D\) označuje diagonální matici kopírující prvky z diagonály \(\mathbf A\). Konvergence je kontrolována maticí
\[\mathbf W = \mathbf E - \mathbf Q^{-1} \mathbf A = \mathbf E - \mathbf D^{-1} \mathbf A\]a je splněna pouze pro ostře diagonálně dominantní matice \(\mathbf A\), tedy matice pro jejichž všechny řádky platí, že součet absolutních hodnot prvků vyjma diagonálního je menší než absolutní hodnota diagonálního prvku.

## Poznámka Anki 1733943297207

Karty Anki: 1733943297207
GUID: v?;0%*9YKJ; štítky: ni-mpi::p14.

### Otázka (Front)

Popište successive overrelaxation (SOR) a Gauss-Seidlovu iterační metodu řešení soustavy lineárních rovnic.

### Odpověď (Back)

**Successive overrelaxation** (SOR) iterační metoda řešení soustavy lineárních rovnic je varianta iterační metody řešení soustavy lineárních rovnic, kde\[\mathbf Q = \frac 1 \omega \mathbf D + \mathbf L,\]přičemž matice \(\mathbf D\) označuje diagonální matici kopírující prvky z diagonály \(\mathbf A\) a \(\mathbf L\) označuje matici \(\mathbf A\), jejíž diagonála a horní trojúhelníková část je vynulována. Konvergence je splněna, pokud \(\omega \in (0, 2)\) a \(\mathbf A\) je symetrická pozitivně definitní matice s kladnými prvky na diagonále. Speciálním případem successive overrelaxation (SOR) metody, kdy \(\omega = 1\), je **Gauss-Seidlova** metoda.

