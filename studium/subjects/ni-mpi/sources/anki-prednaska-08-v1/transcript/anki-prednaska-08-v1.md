# NI-MPI – Přednáška 08

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1731440900908

Karty Anki: 1731440900908
GUID: e%OekmRp8P; štítky: ni-mpi::p08 ni-spol::05.

### Otázka (Front)

Popište přímou numerickou metodu. Uveďte příklad.

### Odpověď (Back)

Přímá numerická metoda je numerická metoda, která počítá řešení matematického problému v konečném počtu kroků a v teoretické absolutní přesnosti dává přesné řešení. Příkladem takové metody je Gaussova eliminační metoda (GEM).

## Poznámka Anki 1731441107848

Karty Anki: 1731441107848
GUID: A^ZwJvM4Cr; štítky: ni-mpi::p08 ni-spol::05.

### Otázka (Front)

Popište iterační numerickou metodu. Uveďte příklad.

### Odpověď (Back)

Iterační numerická metoda je numerická metoda, která počítá řešení matematického problému tak, že konstruuje posloupnost přibližných „řešení“ \(x_0, x_1, x_2, \dots\), přičemž každé další přibližné „řešení“ je odvozeno od toho předchozího:
\[x_k = T(x_{k - 1}), \quad k = 1, 2, \dots. \]Zobrazení \(T\) je voleno tak, aby posloupnost \((x_k)_{k = 0}^\infty\) měla za limitu skutečné řešení daného matematického problému. Příkladem takové metody je mocninná metoda.

## Poznámka Anki 1731444373276

Karty Anki: 1731444373277
GUID: c63RQI51>A; štítky: ni-mpi::p08 ni-spol::05.

### Otázka (Front)

Porovnejte výhody a nevýhody přímých a iteračních numerických metod.

### Odpověď (Back)

Přímé a iterační numerické metody mají následující výhody a nevýhody:

| 
      **přímé metody** | 
      **iterační metody** | 

| 
      poskytují přesné řešení (v teoretické absolutní přesnosti) | 
      poskytují přibližné „řešení“ | 

| 
      více výpočetně náročné | méně výpočetně náročné | 

| 
      trpí zaokrouhlovacími chybami | 
      dobře nastavné zobrazení \(T\) dokáže zaokrouhlovací chyby mezi iteracemi opravovat | 

| 
      kvalitu řešení nelze řídit | 
      kvalitu řešení lze řídit pomocí kritéria zastavení |

## Poznámka Anki 1731445858060

Karty Anki: 1731445858060
GUID: oR]2OuR=]B; štítky: ni-mpi::p08 ni-spol::05.

### Otázka (Front)

Popište mocninnou metodu a její předpoklady.

### Odpověď (Back)

Mocninná metoda je iterační numerická metoda, která slouží k nalezení v absolutní hodnotě největšího vlastního čísla a příslušného vlastního vektoru. Mějme matici \(\mathbf M \in \mathbb C^{n, n}\) splňující následující předpoklady:

- \(\mathbf M\) je diagonalizovatelná, tedy existuje \(\mathbf P \in \mathbb C^{n, n}\) splňující

\[\mathbf M = \mathbf{PDP}^{-1},\]kde \(\mathbf D = \operatorname{diag}(\lambda_1, \dots, \lambda_n),\)

- vlastní čísla \(\mathbf M\) můžeme označit jako

\[|\lambda_1| > |\lambda_2| \geq \dots \geq |\lambda_n|.\]Zvolme nyní \(\mathbf x_0 \in \mathbb C^n\) a konstruujme posloupnost \((\mathbf x_k)_{k = 0}^\infty\) pomocí rekurentního nebo explicitního vztahu

\[\mathbf x_{k + 1} = \mathbf M \mathbf x_k \quad \text{nebo} \quad \mathbf x_k = \mathbf M^k \mathbf x_0, \quad k \in \mathbb N.\]Pokud vektor \(\mathbf x_k\) normalizujeme tak, aby jeho první složka byla \(1\), bude mít pro \(k \to \infty\) za limitu vlastní vektor příslušející vlastnímu číslu \(\lambda_1\).

### Doplňující pole (Extra)

Od předpokladu diagonalizovatelnosti lze upustit při využití Jordanova normálního tvaru.

## Poznámka Anki 1731447323754

Karty Anki: 1731447323754
GUID: qb}FDUj90T; štítky: ni-mpi::p08.

### Otázka (Front)

Popište princip fungování mocninné metody.

### Odpověď (Back)

Mějme \(\mathbf M \in \mathbb C^{n, n}\) splňující předpoklady mocninné metody a konstruovanou posloupnost \((\mathbf x_k)_{k = 0}^\infty\) získanou pomocí explicitního vztahu
\[\mathbf x_k = \mathbf M^k \mathbf x_0, \quad k \in \mathbb N.\]Vektor \(\mathbf x_0 \in \mathbb C^n\) můžeme vyjádřit jako lineární kombinaci vlastních vektorů \(\mathbf M\):
\[\mathbf x_0 = \mathbf P \alpha,\]kde \(\alpha \in \mathbb C^n\) je vektor koeficientů dané lineární kombinace (předpokládáme \(\alpha_1 \neq 0\)). Pro \(k\)-tý člen konstruované posloupnosti pak platí
\[\mathbf x_k = \mathbf M^k \mathbf x_0 \stackrel{1.}{=} (\mathbf{PDP}^{-1})^k \mathbf x_0 \stackrel{2.}{=} \mathbf{PD}^k \alpha \stackrel{3.}{=} \mathbf P \operatorname{diag}(\lambda_1^k, \dots, \lambda_n^k) \alpha \stackrel{4.}{=} \lambda_1^k \mathbf P \operatorname{diag} \Bigg( 1, \bigg( \frac{\lambda_2}{\lambda_1} \bigg)^k, \dots, \bigg( \frac{\lambda_n}{\lambda_1} \bigg)^k \Bigg) \alpha,\]Vektor \(\mathbf x_k\) nyní normalizujeme tak, aby jeho první složka byla rovna \(1\), tedy
\[\mathbf y_k := \frac{\mathbf x_k}{(\mathbf x_k)_1} = \frac{\mathbf P \operatorname{diag} \bigg( 1, \Big( \frac{\lambda_2}{\lambda_1} \Big)^k, \dots, \Big( \frac{\lambda_n}{\lambda_1} \Big)^k \bigg) \alpha}{\Bigg( \mathbf P \operatorname{diag} \bigg( 1, \Big( \frac{\lambda_2}{\lambda_1} \Big)^k, \dots, \Big( \frac{\lambda_n}{\lambda_1} \Big)^k \bigg) \alpha \Bigg)_1} \stackrel{k \to \infty}{=} \frac{\mathbf P \operatorname{diag}(1, 0, \dots, 0) \alpha}{ \big( \mathbf P \operatorname{diag}(1, 0, \dots, 0) \alpha \big)_1} = \frac{\alpha_1 \cdot \mathbf u_1}{\alpha_1} =: \mathbf y_\infty \in \operatorname{ker}(\mathbf M - \lambda_1 \mathbf E), \]díky předpokladu o vlastních číslech platí
\[\displaystyle \lim_{k \to \infty} \Big( \frac{\lambda_i}{\lambda_1} \Big) = 0, \quad i = 2, 3, \dots, n\]a skutečně v \(\mathbf y_\infty\) dostáváme vlastní vektor příslušející vlastnímu číslu \(\lambda_1\).

### Doplňující pole (Extra)

V rovnostech využíváme:

1. diagonalizovatelnost \(\mathbf M = (\mathbf{PDP}^{-1})\),
2. vyjádření \(\mathbf x_0 = \mathbf P \alpha\),
3. definici matice \(\mathbf D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)\),
4. vytknutí \(\lambda_1^k\).

## Poznámka Anki 1731447994074

Karty Anki: 1731447994074
GUID: yD5v]^GarQ; štítky: ni-mpi::p08.

### Otázka (Front)

Popište způsob získání vlastního čísla z vlastního vektoru v mocninné metodě.

### Odpověď (Back)

Mějme \(\mathbf M \in \mathbb C^{n, n}\) splňující předpoklady mocninné metody a poslední iteraci aproximace vlastního vektoru \(\mathbf y_k\) (normalizované \(\mathbf x_k\)). Aproximaci vlastního čísla \(\lambda_1\) získáme následovně
\[\frac{\langle \mathbf y_k, \mathbf {My}_k \rangle}{\| \mathbf y_k \|^2} \stackrel{k \to \infty}{=} \frac{\langle \mathbf y_\infty, \mathbf {My}_\infty \rangle}{\| \mathbf y_\infty \|^2} \stackrel{1.}{=} \frac{\langle \mathbf y_\infty, \lambda_1 \mathbf y_\infty \rangle}{\| \mathbf y_\infty \|^2} \stackrel{2.}{=} \frac{\lambda_1 \| \mathbf y_\infty \|^2}{\| \mathbf y_\infty \|^2} = \lambda_1.\]

### Doplňující pole (Extra)

V rovnostech využíváme:

1. definici vlastního čísla a vztahu \(\mathbf M \mathbf u_1 = \lambda_1 \mathbf u_1\), kde \(\mathbf u_1\) je vlastní vektor a \(\mathbf y_\infty\) jeho aproximace;
2. vytknutí \(\lambda_1\) a vztahu \(\langle \mathbf y_\infty, \mathbf y_\infty \rangle = \| \mathbf y_\infty \|^2\).

## Poznámka Anki 1731448643893

Karty Anki: 1731448643893
GUID: hax/eY,YCZ; štítky: ni-mpi::p08.

### Otázka (Front)

Popište kritérium zastavení a rychlost konvergence mocninné metody.

### Odpověď (Back)

Mějme \(\mathbf M \in \mathbb C^{n, n}\) splňující předpoklady mocninné metody, poslední iteraci aproximace vlastního vektoru \(\mathbf y_k\) (normalizované \(\mathbf x_k\)) a vlastního čísla \(\lambda_1^{(k)}\) a \(\varepsilon > 0\). **Kritérium zastavení** mocninné metody definujeme jako
\[\| \mathbf {My}_k - \lambda_1^{(k)} \mathbf y_k \| < \varepsilon.\]Pro **rychlost konvergence** aproximace vlastního vektoru \(\mathbf y_k\) platí
\[\| \mathbf y_k - \mathbf y_\infty \| = \mathcal O \bigg( \bigg| \frac{\lambda_2}{\lambda_1} \bigg|^k \bigg)\]a obdobně pro aproximaci vlastního čísla \(\lambda_1^{(k)}\)
\[\| \lambda_1^{(k)} - \lambda_1 \| = \mathcal O \bigg( \bigg| \frac{\lambda_2}{\lambda_1} \bigg|^{2k} \bigg).\]

