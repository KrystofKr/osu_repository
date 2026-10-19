# NI-MPI – Přednáška 01

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 19 poznámek, 19 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1727091315606

Karty Anki: 1727091315606
GUID: s&SK?#hnDx; štítky: ni-mpi::p01 ni-spol::03 ni-spol::05.

### Otázka (Front)

Definujte normu.

### Odpověď (Back)

Norma na vektorovém prostoru \(V\) (nad \(\mathbb R\) nebo \(\mathbb C\)) je zobrazení \(\| \cdot \| : V \to \mathbb R^+_0\) splňující:

- **pozitivní definitnost** - \(\| \mathbf x \| = 0 \Rightarrow \mathbf x = \theta\),

- **konzistenci **- \(\| \alpha \mathbf x \| = |\alpha| \cdot \| \mathbf x \|\),

- **submultiplikativitu **- \(\| \mathbf x + \mathbf y \| \leq \| \mathbf x \| + \| \mathbf y \|\) (trojúhelníková nerovnost).

## Poznámka Anki 1727091414725

Karty Anki: 1727091414725
GUID: psIOl2MV?Q; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Definujte okolí bodu \(\mathbf a \in \mathbb{R}^n\).

### Odpověď (Back)

Mějme \(\mathbf x \in \mathbb R^n\) a \(\delta \in \mathbb R^+\). \(\delta\)-okolí bodu (otevřená koule o poloměru \(\delta\)) \(\mathbf x\) je množina
\[H_\delta(\mathbf x) = \{ \mathbf b \in \mathbb R^n : \| \mathbf x - \mathbb b \| < \delta \}.\]

## Poznámka Anki 1727091973376

Karty Anki: 1727091973376
GUID: *=-M~:N;?; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Definujte hromadný bod množiny \(M \subset R^n\).

### Odpověď (Back)

Řekneme, že \(\mathbf x \in \mathbb R^n\) je hromadným bodem množiny \(M \subset \mathbb R^n\), pokud pro všechna \(\varepsilon > 0\) platí
\[H_\varepsilon(\mathbf x) \smallsetminus \{ \mathbf x \} \cap M \neq \emptyset.\]Bod, který není hromadný, se nazývá izolovaný.

## Poznámka Anki 1727092015193

Karty Anki: 1727092015193
GUID: rLo8~D7U!j; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Definujte limitu vektorové posloupnosti.

### Odpověď (Back)

Posloupnost \((\mathbf{x}_k)_{k=1}^\infty\) vektorů \(\mathbf{x}_k \in \mathbb{R}^n\) má limitu \(\mathbf b \in \mathbb R^n\), právě když pro každé okolí \(U_\mathbf b\) bodu \(\mathbf b\) existuje \(N \in \mathbb{N}\) takové, že pokud pro \(k \in \mathbb N\) platí \(k \geq N\), pak \(\mathbf{x}_k \in U_\mathbf b\). Symbolicky lze limitu vektorové posloupnosti definovat následovně:\[(\forall U_\mathbf b)(\exists N \in \mathbb N)(\forall k \in \mathbb N)(k \geq N \Rightarrow \mathbf x_k \in U_\mathbf b).\]Tuto skutečnost značíme\[\displaystyle \lim_{k \to \infty} \mathbf{x}_k = \mathbf{a}.\]

## Poznámka Anki 1727092692263

Karty Anki: 1727092692263
GUID: P]]:8nx<px; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Vyslovte větu o limitě zúžení vektorové funkce. Co platí o posloupnosti bodů z jejího definičního oboru?

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb{R}^n\) a hromadný bod \(\mathbf{a}\) množiny \(D_f\), v němž existuje limita
\[\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = b.\]Potom i pro \(f|_M\) zúžení funkce \(f\) na množinu \(M\), která má \(\mathbf{a}\) jako hromadný bod, platí
\[\displaystyle \lim_{\mathbf{x} \to \mathbf{a}}(f|_M)(\mathbf{x}) = b.\]Speciálně, je-li \((\mathbf{x}_k)_{k=1}^\infty\) posloupnost bodů z \(D_f\) různých od \(\mathbf{a}\), ale s limitou rovnou \(\mathbf{a}\), pak
\[\displaystyle \lim_{k \to \infty} f(\mathbf{x}_k) = b.\]

## Poznámka Anki 1727093414209

Karty Anki: 1727093414209
GUID: z}k:[+R=-+; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Definujte lokální extrémy funkce více proměnných.

### Odpověď (Back)

Funkce \(f: D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) má v bodě \(\mathbf a \in D_f\):

- **ostré lokální minimum**, právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in (U_{\mathbf a} \cap D_f) \smallsetminus \{ \mathbf a \}\) platí \(f(\mathbf x) > f(\mathbf a)\);

- **ostré lokální maximum**, právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in (U_{\mathbf a} \cap D_f) \smallsetminus \{ \mathbf a \}\) platí \(f(\mathbf x) < f(\mathbf a)\);
- **lokální minimum**, právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in U_{\mathbf a} \cap D_f\) platí \(f(\mathbf x) \geq f(\mathbf a)\);
- **lokální maximum**, právě když existuje okolí \(U_{\mathbf a}\) bodu \(\mathbf a\) takové, že pro všechna \(\mathbf x \in U_{\mathbf a} \cap D_f\) platí \(f(\mathbf x) \leq f(\mathbf a)\).

### Doplňující pole (Extra)

V krajních bodech definičního oboru uvažujeme jednostranné okolí \(U_{\mathbf a}\) bodu \(\mathbf a\).

## Poznámka Anki 1727095871699

Karty Anki: 1727095871700
GUID: h5sswmquz0; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Definujte reálnou funkci.

### Odpověď (Back)

Mějme \(n \in \mathbb{N}\) a \(A \subset \mathbb{R}^n\) neprázdnou množinu. Zobrazení \(f\) množiny \(A\) do množiny \(\mathbb{R}\), tj. symbolicky \(f: A \rightarrow \mathbb{R}\), nazýváme reálnou funkcí.

## Poznámka Anki 1727096287528

Karty Anki: 1727096287528
GUID: tl0I`a`;uh; štítky: ni-mpi::p01 ni-spol::03.

### Otázka (Front)

Definujte limitu funkce více proměnných.

### Odpověď (Back)

Řekneme, že funkce \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\), má limitu \(b \in \mathbb R\) v hromadném bodě \(\mathbf a\) množiny \(D_f\), pokud\[\big( \forall H(b) \big) \big( \exists H(\mathbf a) \big) \Big( \mathbf x \in \big( D_f \cap H(\mathbf a) \big) \smallsetminus \{ \mathbf a \} \Rightarrow f(\mathbf x) \in H(b) \Big).\]Tuto skutečnost značíme\[\displaystyle \lim_{\mathbf x \to \mathbf a} f( \mathbf x) = b.\]

## Poznámka Anki 1727096981456

Karty Anki: 1727096981456
GUID: rsg19nl^YH; štítky: ni-mpi::p01 ni-spol::03.

### Otázka (Front)

Vyslovte obě formulace spojitosti funkce více proměnných v bodě.

### Odpověď (Back)

Řekneme, že funkce \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\), je spojitá v bodě \(\mathbf a \in D_f\), pokud
\[(\forall \varepsilon > 0) (\exists \delta > 0) \big( \forall \mathbf x \in D_f : d(\mathbf x, \mathbf a) < \delta \big) \Big( d \big(f(\mathbf x), f(\mathbf a) \big) < \varepsilon \Big).\]Spojitost lze formulovat i pomocí limity. Funkce \(f\) je spojitá v bodě \(\mathbf a\), pokud
\[\displaystyle \lim_{ \mathbf x \to \mathbf a } f(\mathbf x) = f(\mathbf a).\]

## Poznámka Anki 1727097327054

Karty Anki: 1727097327054
GUID: O%Xt9g~LiU; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Definujte globální extrémy funkce.

### Odpověď (Back)

Mějme funkci \(f\) a množinu \(M \subset D_{f}\). Globálním minimem resp. maximem funkce \(f\) na množině \(M\) nazýváme hodnotu\[\displaystyle \min_M f  = a \in M : (\forall x \in M) \big(f(a) \leq f(x) \big)\]resp.\[\displaystyle \max_M f  = a \in M : (\forall x \in M) \big(f(a) \geq f(x) \big)\]existují-li.

### Doplňující pole (Extra)

Pokud vynecháme specifikaci množiny \(M\), pak máme na mysli případ \(M = D_{f}\).

## Poznámka Anki 1727097533049

Karty Anki: 1727097533050
GUID: jT,J`%/|{/; štítky: ni-mpi::p01 ni-spol::03.

### Otázka (Front)

Definujte omezenou, otevřenou a uzavřenou množinu.

### Odpověď (Back)

Množina \(M \subset \mathbb R^n\) se nazývá:

- **omezená**, pokud je podmnožinou nějaké otevřené koule (otevřeného okolí);

- **otevřená**, pokud s každým svým bodem obsahuje i nějaké jeho okolí,

- **uzavřená**, pokud je její doplněk (\(\mathbb R^n \smallsetminus M\)) otevřený (obsahuje svou hranici).

### Doplňující pole (Extra)

Hranicí množiny \(M\) rozumíme množinu bodů, v jejichž každém okolí leží bod z \(M\) a bod mimo \(M\).

## Poznámka Anki 1727097725449

Karty Anki: 1727097725449
GUID: f,eQ3<O.Z;; štítky: ni-mpi::p01 ni-spol::03.

### Otázka (Front)

Vyslovte větu o postačující podmínce existence globálního extrému funkce více proměnných.

### Odpověď (Back)

Mějme spojitou funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\). Je-li \(D_f\) uzavřená a omezená množina, pak na ní \(f\) nabývá globálního maxima i minima.

## Poznámka Anki 1727098297236

Karty Anki: 1727098297236
GUID: NH|vfp(#ro; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Definujte parciální derivaci funkce v bodě.

### Odpověď (Back)

Mějme funkci \(f: D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) definovanou na okolí bodu \(\mathbf a \in D_f\) a \(j \in \hat n\). Parciální derivace funkce \(f\) v bodě** **\(\mathbf a\)** **podle \(j\)-té proměnné je limita\[\displaystyle \lim_{h \to 0} \frac{f(\mathbf a + h \mathbf e_j) - f(\mathbf a)}{h},\]existuje-li. Značíme ji \(\frac{\partial f}{\partial x_j}(\mathbf{a})\) nebo \(\partial_{x_j} f(\mathbf{a})\).

### Doplňující pole (Extra)

**V předmětu NI-MPI **se používá alternativní ekvivalentní definice:\[\displaystyle \lim_{h \to 0} \frac { f(a_1, a_2, \dots, a_j  + h, \dots, a_n ) - f(a_1, a_2, \dots,  a_j, \dots, a_n) } h,\]kde \(\mathbf a = (a_1, a_2, \dots a_n)\) a nazývá se také parciální derivací funkce \(f\) v bodě \(\mathbf a\) ve směru \(x_j\).

## Poznámka Anki 1727098435421

Karty Anki: 1727098435421
GUID: j,c-^v}5}; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Definujte gradient funkce v bodě a popište jeho význam.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(\mathbf a \in D_f\) takový, že \(f\) má na okolí bodu \(\mathbf a\) spojité všechny parciální derivace. Gradient funkce \(f\) v bodě je vektor typu \(\mathbb R^{1, n}\)\[\bigg(\frac{\partial f}{\partial x_1}(\mathbf{a}), \frac{\partial f}{\partial x_2}(\mathbf{a}), \cdots, \frac{\partial f}{\partial x_n}(\mathbf{a}) \bigg)\]a značíme jej \(\nabla f(\mathbf{a})\) nebo \(\operatorname{grad} f(\mathbf{a})\). Gradient udává směr největšího růstu funkce v bodě. To znamená, že směrnice tečny udaná derivací funkce v tomto směru bude největší.

### Doplňující pole (Extra)

Tato definice je zjednodušená, z čehož plyne i předpoklad spojitosti parciálních derivací. Obecná definice požaduje vnitřní bod \(\mathbf a \in D_f\) a gradient funkce \(f\) v bodě \(\mathbf a\) pak definuje jako vektor \(v \in \mathbb R^{1, n}\) splňující\[\displaystyle \lim_{\mathbf x \to \mathbf a} \frac{\| f(\mathbf x) - f(\mathbf a) - \mathbf v \cdot (\mathbf x - \mathbf a) \|}{\| \mathbf x - \mathbf a \|} = 0.\]

## Poznámka Anki 1727098699846

Karty Anki: 1727098699846
GUID: G3VjLPH<h#; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Definujte derivaci funkce ve směru v bodě a popište její vztah s gradientem funkce.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\), bod \(\mathbf a \in D_f \) takový, že \(f\) má v bodě \(\mathbf a\) derivaci, a vektor \(\mathbf s \in \mathbb R^{n, 1}\) takový, že \(\| \mathbf s \| = 1\). Parciální derivace funkce \(f\) v bodě \(\mathbf a\) ve směru \(\mathbf s\) je limita\[\displaystyle \lim_{h \to 0} \frac{f(\mathbf a + h \mathbf s) - f(\mathbf a)}{h}\]a značíme ji \(\frac{\partial f}{\partial \mathbf s}(\mathbf{a})\) nebo \(\partial_{\mathbf s} f(\mathbf a)\). Pokud má funkce v bodě \(\mathbf a\) gradient, pak\[\partial_{\mathbf s} f(\mathbf a) = \langle \nabla f(\mathbf a) \mid \mathbf s \rangle.\]

### Doplňující pole (Extra)

**V předmětu NI-MPI **je po bodu \(a \in D_f\) požadováno pouze, aby funkce \(f\) byla definována na nějakém jeho okolí.

## Poznámka Anki 1727098825548

Karty Anki: 1727098825549
GUID: H6HvvJC*g^; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Vyslovte a dokažte větu o nutné podmínce existence lokálního extrému funkce I.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\), bod \(\mathbf a \in D_f\) takový, že \(f\) má v bodě \(\mathbf a\) lokální extrém, a \(j \in \hat n\). Potom je parciální derivace funkce \(f\) v bodě \(\mathbf a\) podle \(j\)-té proměnné nulová, nebo neexistuje.

**Důkaz
**Definujme funkci\[g(x) = f(\mathbf a + x \mathbf e_j).\]Tato funkce má podle předpokladů jistě lokální extrém v bodě \(x = 0\). Víme, že pokud má reálná funkce jedné reálně proměnné lokální extrém v bodě \(x\), pak je její derivace v tomto bodě nulová nebo neexistuje. Z toho plyne, že \(g'(0)\) je buď nulová, nebo neexistuje. Věta výše plyne ze vztahu\[\partial_jf(\mathbf a) = g'(0).\]

## Poznámka Anki 1727098906709

Karty Anki: 1727098906709
GUID: nN_Idk6MBw; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Definujte stacionární bod a kritický bod.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n \). Bod \(\mathbf a \in D_f\) splňující \(\nabla f(\mathbf a) = \theta\) nazýváme **stacionárním bodem**. **Kritickým bodem** nazveme bod, kde neexistuje gradient nebo je stacionární.

## Poznámka Anki 1727098955122

Karty Anki: 1727098955123
GUID: L4S^{y>Z-^; štítky: duplicate ni-mpi::p01.

### Otázka (Front)

Jaký důsledek má věta o nutné podmínce existence lokálního extrému I?

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R\), \(D_f \subset \mathbb R^n\) a bod \(a \in D_f\) takový, že \(f\) má v bodě \(a \) lokální extrém a parciální derivace podle všech poměnných. Potom je gradient funkce \(f\) v bodě \(a \) nulový vektor\[\nabla f(\mathbf a) = \theta.\]

## Poznámka Anki 1735473195554

Karty Anki: 1735473195554
GUID: j<4/NOx,z*; štítky: ni-mpi::p01 ni-spol::03.

### Otázka (Front)

Popište tečnou nadrovinu funkce a její normálový vektor.

### Odpověď (Back)

Mějme funkci \(f : D_f \to \mathbb R, D_f \subset \mathbb R^n\) a bod \(\mathbf a \in D_f\) takový, že \(f\) má v bodě \(\mathbf a\) gradient. Tečná nadrovina funkce \(f\) v bodě \(\mathbf a\) je sjednocením tečen ve všech směrech v bodě \(\mathbf a\), tedy množina bodů \((x_1, x_2, \dots, x_n, z) \in \mathbb R^{n + 1}\) vyhovujících rovnici\[z = \frac{\partial f}{\partial x_1}(\mathbf a)(x_1 - a_1) + \frac{\partial f}{\partial x_2}(\mathbf a)(x_2 - a_2) + \dots + \frac{\partial f}{\partial x_n}(\mathbf a)(x_n - a_n) + f(\mathbf a).\]Jejím normálovým vektorem je vektor\[\Big( \frac{\partial f}{\partial x_1}(\mathbf a), \frac{\partial f}{\partial x_2}(\mathbf a), \dots, \frac{\partial f}{\partial x_n}(\mathbf a), -1 \Big).\]

