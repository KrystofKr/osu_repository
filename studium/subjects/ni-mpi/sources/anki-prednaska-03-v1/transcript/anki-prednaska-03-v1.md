# NI-MPI – Přednáška 03

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1728315940643

Karty Anki: 1728315940643
GUID: bk:s;q$%AW; štítky: ni-mpi::p03 ni-spol::03.

### Otázka (Front)

Vyslovte větu o implicitní funkci pro funkce dvou proměnných.

### Odpověď (Back)

Mějmě funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^2\). Nechť má spojité všechny parciální derivace na okolí bodu \((a, b) \in D_f\) a platí
\[f(a, b) = 0 \quad \text a \quad \frac {\partial f}{\partial x_2}(a, b) \neq 0.\]Potom existuje \(\varepsilon > 0\) a čtvercové okolí
\[R := \{ (x_1, x_2) : |x_1 - a| < \varepsilon, |x_2 - b| < \varepsilon \}\]bodu \((a, b)\) takové, že pro každé \(x_1 \in (a - \varepsilon, a + \varepsilon)\) existuje právě jedno \(x_2 \in (b - \varepsilon, b + \varepsilon)\) takové, že platí
\[f(x_1, x_2) = 0.\]Proměnná \(x_2\) je tedy funkcí proměnné \(x_1\), neboli
\[x_2 = \varphi(x_1), \quad x_1 \in (a - \varepsilon, a + \varepsilon).\]Pro funkci \(\varphi\) navíc platí, že je spojitá pro \(x \in (a - \varepsilon, a + \varepsilon)\) a
\[\varphi'(x) = - \frac{\frac{\partial f}{\partial x_1} \big(x, \varphi(x) \big)}{\frac{\partial f}{\partial x_2} \big( x, \varphi(x) \big)}, \quad x \in (a - \varepsilon, a + \varepsilon).\]

## Poznámka Anki 1728337034935

Karty Anki: 1728337034935
GUID: D].(A+wh~; štítky: ni-mpi::p03 ni-spol::03.

### Otázka (Front)

Definujte množinu přípustných řešení, rovnostní vazby a nerovnostní vazby.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a \(m, p \in \mathbb N\). **Množinu přípustných řešení** \(\mathcal M\) definujeme následovně:
\[\mathcal M = \{ \mathbf x \in D_f : (\forall j \in \hat m) \big( g_j(\mathbf x) = 0 \big) \land (\forall k \in \hat p) \big (h_k (\mathbf x) \leq 0 \big).\]Funkce \(g_j : D_{g_j} \to \mathbb R\), \(D_{g_j} \subset \mathbb R^n\) pak nazýváme **rovnostními vazbami **(podmínkami) a funkce \(h_k : D_{h_k} \to \mathbb R\), \(D_{h_k} \subset \mathbb R^n\) **nerovnostními vazbami **(podmínkami).

## Poznámka Anki 1728337395457

Karty Anki: 1728337395457
GUID: t$tUWzS^k+; štítky: ni-mpi::p03 ni-spol::03.

### Otázka (Front)

Definujte lokální extrémy funkce více proměnných na množině přípustných řešení.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a množinu přípustných řešení \(\mathcal M \subset \mathbb R^n\). Funkce \(f\) má v bodě \(\mathbf a \in \mathcal M \cap D_f\):

- **ostré lokální minimum vzhledem k množině **\(\mathcal M\), právě když existuje okolí \(H(\mathbf x^*)\) bodu \(\mathbf x^*\) takové, že pro všechna \(\mathbf x \in \big (H(a) \cap \mathcal M \big) \smallsetminus \{ \mathbf a \}\) platí \(f(\mathbf x) > f(\mathbf a)\);

- **ostré lokální maximum**** vzhledem k množině **\(\mathcal M\), právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in \big (H(a) \cap \mathcal M \big) \smallsetminus \{ \mathbf a \}\) platí \(f(\mathbf x) < f(\mathbf a)\);
- **lokální minimum**** vzhledem k množině **\(\mathcal M\), právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in H(a) \cap \mathcal M\) platí \(f(\mathbf x) \geq f(\mathbf a)\);
- **lokální maximum**** vzhledem k množině **\(\mathcal M\), právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in H(a) \cap \mathcal M\) platí \(f(\mathbf x) \leq f(\mathbf a)\).

### Doplňující pole (Extra)

V krajních bodech množiny přípustných řešení uvažujeme jednostranné okolí \(U_\mathbf a\) bodu \(\mathbf a\).

## Poznámka Anki 1728404010784

Karty Anki: 1728404010784
GUID: n{R2sjTA@2; štítky: ni-mpi::p03 ni-spol::03.

### Otázka (Front)

Definujte Lagrangeovu funkci a Lagrangeovy multiplikátory při rovnostních vazbách.

### Odpověď (Back)

Funkci \(L : \mathcal M \times \mathbb R^m \to \mathbb R\) definovanou jako
\[L(\mathbf x; \lambda) = f(\mathbf x) + \displaystyle \sum_{j = 1}^m \lambda_j g_j (\mathbf x)\]nazýváme **Lagrangeovou funkcí** pro úlohu při rovnostních vazbách. Koeficienty
\[\lambda = (\lambda_1, \dots, \lambda_m)\]nazýváme **Lagrangeovy multiplikátory**.

## Poznámka Anki 1728406122274

Karty Anki: 1728406122274
GUID: Mwu9_I@A!7; štítky: ni-mpi::p03 ni-spol::03.

### Otázka (Front)

Vyslovte větu o postačující podmínce existence ostrého lokálního minima a maxima při rovnostních vazbách.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a rovnostní vazby \(g_j\), \(j \in \hat m\) a nechť mají spojité všechny druhé parciální derivace na nějaké otevřené nadmnožině \(\tilde{\mathcal M} \supset \mathcal M\). Pokud dvojice \((\mathbf x^*; \lambda^*) \in \mathbb R^n \times \mathbb R^m\) splňuje podmínky:

- **0. derivace** - \(\mathbf x^*\) je z množiny přípustných řešení

\[\mathbf x^* \in \mathcal M;\]

- **1. derivace **- všechny parciální derivace Largrangeovy funkce podle proměnných \(x_i\), \(i \in \hat n\) jsou v bodě \((\mathbf x^*; \lambda^*)\) nulové

\[\frac{\partial L}{\partial x_i}(\mathbf x^*; \lambda^*) = 0, \quad i \in \hat n; \]

- **2. derivace** - pro každý nenulový sloupcový vektor \(v \in \mathbb R^n\) splňující 

\[\nabla g_j(\mathbf x^*) \cdot v = 0, \quad j \in \hat m\]platí

\[v^T \cdot \nabla^2_\mathbf x L(\mathbf x^*; \lambda^*) \cdot v > 0 \quad \text{resp.} \quad v^T \cdot \nabla^2_\mathbf x L(\mathbf x^*; \lambda^*) \cdot v < 0,\]kde \(\nabla^2_\mathbf x L\) je Hessova matice funkce \(L\) vzhledem k proměnným \(\mathbf x = (x_1, \dots, x_n)\);

potom je \(\mathbf x^*\) bodem ostrého lokálního minima resp. maxima.

### Doplňující pole (Extra)

Podmínky 0. a 1. derivace zajišťují, že \(\nabla L(\mathbf x^*; \lambda^*) = \theta\), tedy že \(\nabla f\) a \(\nabla g_j\) mají stejné směry a vazby v daném bodě neprotínají vrstevnici. Jedině v takových bodech se může nacházet lokální extrém.
Podmínka 2. derivace omezuje vyhodnocení definitnosti \(\nabla^2_\mathbf x L\) pouze na vektory \(v\) kolmé na gradienty rovnostních vazeb \(g_j\), tedy na vektory v jejich směru.

## Poznámka Anki 1728406580331

Karty Anki: 1728406580331
GUID: pL-MZtDT*K; štítky: ni-mpi::p03 ni-spol::03.

### Otázka (Front)

Definujte Lagrangeovu funkci a Lagrangeovy multiplikátory při rovnostních i nerovnostních vazbách.

### Odpověď (Back)

Funkci \(L : \mathcal M \times \mathbb R^m \times \mathbb R^p \to \mathbb R\) definovanou jako
\[L(\mathbf x; \lambda; \mu) = f(\mathbf x) + \displaystyle \sum_{j = 1}^m \lambda_j g_j (\mathbf x) + \displaystyle \sum_{k = 1}^p \mu_k h_k (\mathbf x)\]nazýváme **Lagrangeovou funkcí** pro úlohu při rovnostních i nerovnostních vazbách. Koeficienty
\[\lambda = (\lambda_1, \dots, \lambda_m) \quad \text a \quad \mu = (\mu_1, \dots, \mu_p)\]nazýváme **Lagrangeovy multiplikátory**.

## Poznámka Anki 1728410421855

Karty Anki: 1728410421855
GUID: q)!&^6<`]q; štítky: ni-mpi::p03 ni-spol::03.

### Otázka (Front)

Definujte množinu aktivních omezení.

### Odpověď (Back)

Mějme bod \(\mathbf x \in \mathcal M\) a nerovnostní vazby \(h_k\), \(k \in \hat p\). Množinu aktivních omezení definujeme jako
\[\mathcal B(\mathbf x) = \{ k \in \hat p : h_k(\mathbf x) = 0 \}.\]

### Doplňující pole (Extra)

Množina aktivních omezení udává indexy nerovnostních vazeb, na jejichž hranici leží bod \(\mathbf x\).

## Poznámka Anki 1728411906519

Karty Anki: 1728411906519
GUID: C_~;g*w<oM; štítky: ni-mpi::p03 ni-spol::03.

### Otázka (Front)

Vyslovte větu o postačující podmínce existence ostrého lokálního minima a maxima při rovnostních i nerovnostních vazbách.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\), rovnostní vazby \(g_j\), \(j \in \hat m\) a nerovnostní vazby \(h_k\), \(k \in \hat p\) a nechť mají spojité všechny druhé parciální derivace na nějaké otevřené nadmnožině \(\tilde{\mathcal M} \supset \mathcal M\). Pokud trojice \((\mathbf x^*; \lambda^*; \mu^*) \in \mathbb R^n \times \mathbb R^m \times \mathbb R^p\) splňuje podmínky:

- **0. derivace** - \(\mathbf x^*\) je z množiny přípustných řešení

\[\mathbf x^* \in \mathcal M\]

-  **1. derivace** - všechny parciální derivace Lagrangeovy funkce podle proměnných \(x_i\), \(i \in \hat n\) jsou v bodě \((\mathbf x^*; \lambda^*; \mu^*)\) nulové

\[\frac{\partial L}{\partial x_i}(\mathbf x^*; \lambda^*; \mu^*) = 0, \quad i \in \hat n; \]

- **aktivní a neaktivní vazby** - buď \(\mu_k^* = 0\) nebo \(h_k(\mathbf x^*) = 0\) pro \(k \in \hat p\);

- **2. derivace** - pro každý nenulový sloupcový vektor \(v \in \mathbb R^n\) splňující

\[\begin{matrix}
\nabla g_j(\mathbf x^*) \cdot v = 0, \quad j \in \hat m,\\
\nabla h_k(\mathbf x^*) \cdot v = 0, \quad k \in \hat p, \mu_k^* \neq 0;
\end{matrix}\]platí

\[v^T \cdot \nabla^2_\mathbf x L(\mathbf x^*; \lambda^*; \mu^*) \cdot v > 0 \quad \text{resp.} \quad v^T \cdot \nabla^2_\mathbf x L(\mathbf x^*; \lambda^*; \mu^*) \cdot v < 0,\]kde \(\nabla^2_x L\) je Hessova matice funkce \(L\) vzhledem k proměnným \(\mathbf x = (x_1, \dots, x_n)\);

- **správný „směr“ od hranice **\(\mathcal M\) - \(\mu_k^* \geq 0\) resp. \(\mu_k^* \leq 0\) pro \(k \in \hat p\);

potom je \(\mathbf x^*\) bodem ostrého lokálního minima resp. maxima.

### Doplňující pole (Extra)

Podmínky 0. a 1. derivace zajišťují, že \(\nabla L(\mathbf x^*; \lambda^*, \mu^*) = \theta\), tedy že \(\nabla f\), \(\nabla g_k\) a \(\nabla h_k\) mají stejný směr a vazby v daném bodě neprotínají vrstevnici. Jedině v takových bodech se může nacházet lokální extrém. 
Podmínka 2. derivace omezuje vyhodnocení definitnosti \(\nabla^2_\mathbf x L\) pouze na vektory \(v\) kolmé na gradienty rovnostních vazeb \(g_k\) a nerovnostních vazeb \(h_k\), tedy na vektory v jejich směru, a případně na vektory s nulovými Lagrangeovými multiplikátory \(\mu_k^*\), protože ty se nachází uvnitř nerovnostních vazeb.

