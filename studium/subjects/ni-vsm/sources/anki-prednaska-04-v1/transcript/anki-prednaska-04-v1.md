# NI-VSM – Přednáška 04

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-VSM
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1740676873513

Karty Anki: 1740676873513
GUID: or|I9VJV9_; štítky: ni-vsm::p04.

### Otázka (Front)

Definujte střední hodnotu náhodného vektoru.

### Odpověď (Back)

Mějme náhodný vektor \(\mathbf X = (X_1, \dots, X_n)^T\). Pokud existují střední hodnoty náhodných veličin \(X_1, \dots, X_n\), pak vektor\[\operatorname E \mathbf X = (\operatorname E X_1, \dots, \operatorname E X_n)^T \]nazýváme střední hodnotou náhodného vektoru \(\mathbf X\).

## Poznámka Anki 1740677511774

Karty Anki: 1740677511774
GUID: vZ_Q}x.VCb; štítky: ni-vsm::p04.

### Otázka (Front)

Popište důsledek věty o linearitě střední hodnoty pro náhodné vektory.

### Odpověď (Back)

Mějme náhodný vektor \(\mathbf X\), vektor \(\mathbf a \in \mathbb R^p\) a matici \(\mathbf B \in \mathbb R^{p, n}\). Potom\[\operatorname E(\mathbf a + \mathbf{BX}) = \mathbf a + \mathbf B \operatorname E \mathbf X.\]

## Poznámka Anki 1740678255885

Karty Anki: 1740678255885
GUID: A3bPsty}eB; štítky: ni-vsm::p04.

### Otázka (Front)

Definujte varianční matici náhodného vektoru a vyslovte větu o jejím výpočtu.

### Odpověď (Back)

Mějme náhodný vektor \(\mathbf X = (X_1, \dots, X_n)^T\) s konečnými druhými momenty. Varianční matice vektoru \(\mathbf X\) je matice\[\operatorname{var} \mathbf X = \big( \operatorname{cov}(X_i, X_j) \big) = \begin{pmatrix}
\operatorname{var} X_1 && \operatorname{cov}(X_1, X_2) && \cdots && \operatorname{cov(X_1, X_n}\\
\operatorname{cov}(X_2, X_1) && \operatorname{var} X_2 && \cdots && \operatorname{cov}(X_2, X_n)\\
\vdots && \vdots && \ddots && \vdots\\
\operatorname{cov}(X_n, X_1) && \operatorname{cov}(X_n, X_2) && \cdots && \operatorname{var} X_n
\end{pmatrix}.\]Pro výpočet varianční matice vektoru \(\mathbf X\) lze použít vzorec\[\operatorname{var} \mathbf X = \operatorname E(\mathbf X - \operatorname E \mathbf X)(\mathbf X - \operatorname E \mathbf X)^T = \operatorname E \mathbf X \mathbf X^T - \operatorname E \mathbf X \operatorname E \mathbf X^T.\]

## Poznámka Anki 1740678736203

Karty Anki: 1740678736203
GUID: qET%6)drB2; štítky: ni-vsm::p04.

### Otázka (Front)

Vyslovte větu o varianční matici lineární transformace.

### Odpověď (Back)

Mějme náhodný vektor \(\mathbf X\), vektor \(\mathbf a \in \mathbb R^p\) a matici \(\mathbf B \in \mathbb R^{p, n}\). Potom\[\operatorname{var}(\mathbf a + \mathbf{BX}) = \mathbf B (\operatorname{var}X) \mathbf B^T.\]

## Poznámka Anki 1740678905682

Karty Anki: 1740678905682
GUID: gbu4obFP}W; štítky: ni-vsm::p04.

### Otázka (Front)

Vyslovte větu o vlastnostech varianční matice náhodného vektoru.

### Odpověď (Back)

Varianční matice \(\operatorname{var} \mathbf X\) náhodného vektoru \(\mathbf X\) je symetrická a pozitivně semidefinitní. Pokud navíc žádná složka \(\mathbf X\) není lineární kombinací ostatních složek a konstanty, je \(\operatorname{var} \mathbf X\) pozitivně definitní.

### Doplňující pole (Extra)

Náhodná veličina \(Y\) je kombinacní náhodných veličin \(Y_1, \dots, Y_n\) a konstanty, právě když existují koeficienty \(c_1, \dots, c_n \in \mathbb R\) takové, že\[\operatorname P(Y = c_1 Y_1 + \dots + c_n Y_n + c) = 1.\]

## Poznámka Anki 1740681396507

Karty Anki: 1740681396507
GUID: J}!sXntbN3; štítky: ni-vsm::p04.

### Otázka (Front)

Definujte vícerozměrné normální rozdělení a vyslovte větu o jeho hustotě.

### Odpověď (Back)

Náhodný vektor \(\mathbf X = (X_1, \dots, X_n)^T\) má \(n\)-rozměrné normální rozdělení s parametry \(\boldsymbol \mu \in \mathbb R^n\) a \(\boldsymbol \Sigma \in \mathbb R^{n, n}\), kde \(\boldsymbol \Sigma\) je symetrická pozitivně semidefinitní matice, jestliže pro každé \(\mathbf c \in \mathbb R^n\) platí\[\mathbf c^T \mathbf X \sim \operatorname N(\mathbf c^T \boldsymbol \mu, \mathbf c^T \boldsymbol \Sigma \mathbf c).\]Značíme \(\mathbf X \sim \operatorname N(\boldsymbol \mu, \boldsymbol \Sigma)\). Pokud je navíc \(\boldsymbol \Sigma\) pozitivně definitní, pak \(\mathbf X \sim \operatorname N(\boldsymbol \mu, \boldsymbol \Sigma)\) právě tehdy, když má \(\mathbf X\) spojité sdružené rozdělení s hustotou\[f_\mathbf X(\mathbf x) = \frac{1}{(2 \pi)^{\frac n 2} |\boldsymbol \Sigma|^{\frac 1 2}} e ^{- \frac 1 2 (\mathbf x - \boldsymbol \mu)^T \boldsymbol \Sigma^{-1} (\mathbf x - \boldsymbol \mu)}.\]

## Poznámka Anki 1740681544419

Karty Anki: 1740681544419
GUID: xeV1dab9lZ; štítky: ni-vsm::p04.

### Otázka (Front)

Vyslovte větu o vlivu lineární transformace na normální rozdělení.

### Odpověď (Back)

Mějme \(X \sim \operatorname N(\mu, \sigma^2)\), kde \(\mu \in \mathbb R\) a \(\sigma \geq 0\) a \(a, b \in \mathbb R\). Potom\[a + bX \sim \operatorname N(a + b \mu, b^2 \sigma^2),\]tedy normální rozdělení je invariantní vůči lineární transformaci.

### Doplňující pole (Extra)

V tomto případě připouštíme i \(\sigma = 0\), tedy singulární normální rozdělení.

## Poznámka Anki 1740682445378

Karty Anki: 1740682445378
GUID: xqU)[.AJK/; štítky: ni-vsm::p04.

### Otázka (Front)

Vyslovte větu o vlivu lineární transformace na vícerozměrné normální rozdělení.

### Odpověď (Back)

Mějme \(\mathbf X \sim \operatorname N(\boldsymbol \mu, \boldsymbol \Sigma)\), \(\mathbf a \in \mathbb R^m\) a \(\mathbf B \in \mathbb R^{m, n}.\) Potěom\[\mathbf a + \mathbf{BX} \sim \operatorname N(\mathbf a + \mathbf B \boldsymbol \mu, \mathbf B \boldsymbol \Sigma \mathbf B^T),\]tedy vícerozměrné normální rozdělení je invariantní vůči lineární transformaci.

## Poznámka Anki 1740682967327

Karty Anki: 1740682967327
GUID: zk_3PCYI)y; štítky: ni-vsm::p04.

### Otázka (Front)

Vyslovte větu o marginálním rozdělení vícerozměrného normálního rozdělení.

### Odpověď (Back)

Mějme \(\mathbf X = (X_1, \dots, X_m) \sim \operatorname N(\boldsymbol \mu, \boldsymbol \Sigma)\), \(k < n\) a \(k\)-tice přirozených čísel \(1 \leq i_1 < \dots < i_k \leq n\). Pro marginální rozdělení náhodného vektoru \(\mathbf X' = (X_{i_1}, \dots, X_{i_k})^T\) platí\[\mathbf X' \sim \operatorname N(\boldsymbol \mu', \boldsymbol \Sigma'),\]kde\[\begin{matrix}
\boldsymbol \mu' = (\mu_{i_1}, \dots, \mu_{i_k})^T,\\
\boldsymbol \Sigma' = \begin{pmatrix} \boldsymbol \Sigma_{i_j, i_\ell} \end{pmatrix}.
\end{matrix}\]

## Poznámka Anki 1740683160795

Karty Anki: 1740683160795
GUID: x[Y&*+t:qZ; štítky: ni-vsm::p04.

### Otázka (Front)

Vyslovte větu o vztahu nezávislosti a nekoerlovanosti ve vícerozměrném normálním rozdělení a uveďte její důsledek.

### Odpověď (Back)

Mějme náhodný vektor \(\mathbf X = (X_1, \dots, X_n)^T\). Náhodné veličiny \(X_1, \dots, X_n\) jsou nezávislé a \(X_1 \sim \operatorname N(\mu_1, \sigma_1^2), \dots, X_n \sim \operatorname N(\mu_n, \sigma_n^2)\) právě tehdy, když \(\mathbf X \sim \operatorname N(\boldsymbol \mu, \boldsymbol \Sigma)\), kde \(\boldsymbol \mu = (\mu_1, \dots, \mu_n)^T\) a \(\boldsymbol \Sigma\) je diagonální s \(\boldsymbol \Sigma_{i, i} = \sigma_i^2\). Z toho plyne, že máme-li \(\mathbf X \sim \operatorname N(\boldsymbol \mu, \boldsymbol \Sigma)\), pak pro \(i \neq j\) platí, že \(X_i\) a \(X_j\) jsou nezávislé právě tehdy, když jsou nekorelované.

## Poznámka Anki 1740683752657

Karty Anki: 1740683752657
GUID: u:%LGTtQFU; štítky: ni-vsm::p04.

### Otázka (Front)

Vyslovte větu o analýze hlavních komponent.

### Odpověď (Back)

Mějme \(\mathbf X \sim \operatorname N(\boldsymbol \mu, \boldsymbol \Sigma)\) a ortonormální bázi \(\{ \mathbf v_1, \dots, \mathbf v_n \}\) tvořenou vlastními vektory matice \(\boldsymbol \Sigma\) přislušejícím vlastním číslum \(\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_n\) matice \(\boldsymbol \Sigma\). Potom platí, že\[Y_i = \mathbf v_i^T \mathbf X\]jsou nezávislé náhodné veličiny a\[Y_i \sim \operatorname N(\mathbf v_i^T \boldsymbol \mu, \lambda_i).\]

### Doplňující pole (Extra)

Ortonormální vektory jsou vektory, které jsou na sebe kolmé a mají normu rovnou jedné.

