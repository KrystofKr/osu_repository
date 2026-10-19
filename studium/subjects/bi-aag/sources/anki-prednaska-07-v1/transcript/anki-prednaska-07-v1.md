# BI-AAG – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aag/BI-AAG.apkg; APKG SHA-256 0383847389324f3b83b349363b7ad16a6bf91673c90b7a96ed1a57b25a85f8af. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b9cda20d5a5a9d1ff47d4e1fc58b10ed3ac7a37c72c6c1431cc7cb67e2ca10c.
Původní balíčky: BI-AAG
Rozsah: 35 poznámek, 35 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1667557529417

Karty Anki: 1667557529420
GUID: fzv:rEJm@k; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557529420: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **normální tvar podle Chomského** pro bezkontextovou gramatiku.

### Odpověď (Back)

Bezkontextová gramatika \(G = (N, \Sigma, P, S)\) je v **normálním tvaru podle Chomského** právě tehdy, když každé pravidlo v \(P\) má jeden z následujících tvarů: 

- \(A \rightarrow BC\), 
- \(A \rightarrow a\), 
- \(S \rightarrow \varepsilon\),
kde \(A, B, C \in N\) a \(a \in \Sigma\) a zároveň platí, že pokud se v \(P\) vyskytuje třetí pravidlo, pak \(S\) není na pravé straně žádného z pravidel.

## Poznámka Anki 1667557604968

Karty Anki: 1667557604968
GUID: kP7xRgb+Xo; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557604968: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadanou bezkontextovou gramatiku vrátí ekvivalentní bezkontextovou gramatiku v **normálním tvaru podle Chomského**.

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Bezkontextová gramatika \(G^\prime = (N^\prime, \Sigma^\prime, P^\prime, S^\prime)\) v normálním tvaru podle Chomského taková, že \(L(G^\prime) = L(G)\).

**Postup:**

1. Gramatiku \(G\) převedeme dle algoritmu na gramatiku \(G_1 = (N_1, \Sigma_1, P_1, S_1)\), která je vlastní a bez jednoduchých pravidel. 
2. Inicializujeme \(N^\prime = N_1\).
3. \(\Sigma^\prime = \Sigma_1\).
4. \(S^\prime = S_1\).
5. Víme, že všechna pravidla v \(P_1\) mají jeden z následujících tvarů:

1. \(A \rightarrow a\), kde \(A \in N_1, a \in \Sigma_1\),
2. \(S_1 \rightarrow \varepsilon\), kde \(S_1\) je počáteční neterminál, který se nevyskytuje na pravé straně žádného pravidla,
3. \(A \rightarrow \alpha\), kde \(|\alpha| \geq 2, \alpha \in (N_1 \cup \Sigma_1)^*\).

6. V případě (5.1) a (5.2) mají pravidla tvar, který splňuje požadavky normálního tvaru podle Chomského, proto všechna pravidla z \(P_1\) tohoto tvaru přesuneme do \(P^\prime\). Ve případě (5.3) je počet symbolů na pravé straně větší nebo roven dvěma, přičemž se může jednat o libovolnou posloupnost terminálů i neterminálů. Naším úkolem tedy pro pravidla v případě (5.3) bude:

1. Zajistit, že všechna tato pravidla mají na pravé straně pouze neterminální symboly. To lze provést tak, že pro každý terminál \(a \in \Sigma_1\) vyskytující se na pravé straně těchto pravidel vytvoříme nový neterminál \(a^\prime\) (předpokládáme, že původně \(a^\prime \notin N_1\)) a do gramatiky \(G^\prime\) přidáme pravidlo \(a^\prime \rightarrow a\). Neterminálem \(a^\prime\) poté nahradíme každý výskyt terminálu \(a\) ve všech pravých stranách pravidel v \(G_1\) s délkou větší nebo rovnou dvěma. Zároveň aktualizujeme množinu neterminálních symbolů: \(N^\prime = N^\prime \cup \{ a^\prime \}\).

2. Každé pravidlo ve tvaru \(A \to BC\), kde \(B,C \in N^\prime\), z \(P_1\) přesuneme do \(P^\prime\).
3. Dále musíme rozdělit pravé strany z \(P_1\) s délkou větší nebo rovnou třem do více pravidel tak, aby každé pravidlo mělo na pravé straně přesně dva neterminální symboly: Pro každé pravidlo ve tvaru \(A \rightarrow B_1 B_2 \dots B_k\), kde \(k \geq 3\), z \(P_1\) přidáme do \(P^\prime\)  následující pravidla:

- \(A \to B_1C_1\), 
- \(C_1 \to B_2C_2\), 
- \(\dots\) 
- \(C_{k-3} \to B_{k-2}C_{k-2}\), 
- \(C_{k-2} \to B_{k-1}B_k\),

- kde \(C_1, \dots, C_{k-2}\) jsou nové neterminální symboly (tedy \(C_1, \dots, C_{k-2} \notin N_1\)) a tyto neterminály přidáme do množiny \(N^\prime\).

### Doplňující pole (Extra)

Každou bezkontextovou gramatiku můžeme převést do normálního tvaru podle Chomského

## Poznámka Anki 1667557695083

Karty Anki: 1667557695083
GUID: A)!_i$Z7LL; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557695083: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište vstup, výstup a postup algoritmu **CYK**.

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\) v normálním tvaru podle Chomského a řetězec \(x = x_1x_2\dots x_k\) nad abecedou \(\Sigma\) délky \(k\).

**Výstup:** true právě tehdy, když \(x \in L(G)\), jinak false.

**Postup:**

1. Vytvoříme dvourozměrnou tabulku \(T\) velikosti \(k \times k\). Pomocí \(T(r,c)\) budeme značit buňku, která je v řádku \(r\) a sloupci \(c\). Tato buňka bude po vyplnění obsahovat množinu neterminálů z \(G\), které v rámci řetězce \(x\) generují jeho podřetězec začínající na pozici \(r\) (odpovídá číslu řádku) s délkou \(c\) (odpovídá číslu sloupce).
2. (první sloupec) Pro každé \(i \in \{ 1, 2, \dots, k \}\) vyplníme buňku \(T[i, 1]\): \(T[i, 1] = \{ A : A \in N \wedge (A \to x_i) \in P \}\).
3. (\(j\)-tý sloupec) Pro každé \(i \in \{ 1, 2, \dots, (k - j + 1) \}\) vyplníme buňku \(T[i, j]\): \(T[i, j] = \{ A : A \in N \wedge \exists(A \Rightarrow^* x_i\dots x_{j}) \}\).
4. Jak zjistíme, zdali \(A \Rightarrow^* x_i\dots x_{j}\)? Využijeme předchozí vypočítané buňky. Neboť \(A \Rightarrow^* x_i\dots x_{j}\) právě tehdy, když \(P\) obsahuje pravidlo \(A \to BC\), kde \(B \Rightarrow^* x_i\dots x_{r}\) a \(C \Rightarrow^* x_r\dots x_{j}\). 
5. Pokud \(T[1,k]\) obsahuje \(S\), vrať true, jinak vrať false.

### Doplňující pole (Extra)

Algoritmus využívá technicky dynamického programování

## Poznámka Anki 1667557717858

Karty Anki: 1667557717858
GUID: FyjpbT{mrv; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557717858: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaká je **časová složitost** algoritmu **CYK**?

### Odpověď (Back)

Časová složitost algoritmu CYK je \(\mathcal{O}(|x|^3)\), kde \(x\) je vstupní řetězec (považujeme-li velikost gramatiky za konstantu).

## Poznámka Anki 1667557788412

Karty Anki: 1667557788412
GUID: LZs|Gy:XMu; štítky: bi-aag::p07.

Metadata původního zdroje pro kartu 1667557788412: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadanou bezkontextovou gramatiku rozhodne, zdali **(ne)generuje prázdný jazyk**.

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup: **true právě tehdy, když \(L(G) = \emptyset\), jinak false.

**Postup:**

1. V gramatice \(G\) nalezneme množinu \(N_R\) obsahující všechny generující symboly:

1. Inicializujeme \(N_R = \{ a : a \in \Sigma\}\).

2. \(N_R = N_R \cup \{ A : (A \to \varepsilon) \in P \}\).
3. Projdeme všechna pravidla v \(P\) a pokud je zkoumané pravidlo ve tvaru \(A \to \alpha\), kde \(\alpha \in (N \cup \Sigma)^+\) a každý symbol v \(\alpha\) je generující, pak \(N_R = N_R \cup \{A\}\).
4. Předchozí krok opakujeme, dokud se množina \(N_R\) mění.

2. Pokud \(S \notin N_R\), vrať true, jinak vrať false.

## Poznámka Anki 1667557817883

Karty Anki: 1667557817883
GUID: pKZF{aHCr+; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557817883: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **rekurzivní neterminální symbol**.

### Odpověď (Back)

Mějme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\). Neterminální symbol \(A \in N\) nazveme **rekurzivní** právě tehdy, když existuje derivace \(A \Rightarrow^+ \alpha A\beta\), kde \(\alpha, \beta \in (N \cup \Sigma)^*\).

## Poznámka Anki 1667557836385

Karty Anki: 1667557836385
GUID: umEGEghhW|; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557836385: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **rekurzivní bezkontextovou gramatiku**.

### Odpověď (Back)

Bezkontextovou gramatiku nazveme **rekurzivní** právě tehdy, když obsahuje alespoň jeden rekurzivní neterminální symbol.

## Poznámka Anki 1667557879220

Karty Anki: 1667557879220
GUID: lT?xbos^!c; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557879220: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **neterminální symbol rekurzivní zleva**.

### Odpověď (Back)

Mějme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\). Neterminální symbol \(A \in N\) nazveme **rekurzivní zleva** právě tehdy, když existuje derivace \(A \Rightarrow^+ A\alpha\), kde \(\alpha \in (N \cup \Sigma)^*\).

### Doplňující pole (Extra)

Neterminální symbol \(A\) je tedy rekurzivní zleva, pokud v gramatice existuje derivace, která z \(A\) po jednom či více krocích generuje řetězec nad abecedou \(N \cup \Sigma\) začínající symbolem \(A\).

## Poznámka Anki 1667557904122

Karty Anki: 1667557904122
GUID: Dx<QN3A~MG; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557904122: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **neterminální symbol přímo rekurzivní zleva**.

### Odpověď (Back)

Mějme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\). Neterminální symbol \(A \in N\) nazveme **přímo rekurzivní zleva** právě tehdy, když \((A \rightarrow A\alpha) \in P\), kde \(\alpha \in (N \cup \Sigma)^*\).

### Doplňující pole (Extra)

Neterminální symbol \(A\) je tedy přímo rekurzivní zleva, pokud v gramatice pro \(A\) existuje alespoň jedno pravidlo, které na pravé straně začíná symbolem \(A\).

## Poznámka Anki 1667557926423

Karty Anki: 1667557926423
GUID: O]UHaD~f;.; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557926423: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **bezkontextovou gramatiku rekurzivní zleva**.

### Odpověď (Back)

Bezkontextovou gramatiku nazveme **rekurzivní zleva** právě tehdy, když obsahuje alespoň jeden neterminální symbol rekurzivní zleva.

## Poznámka Anki 1667557949742

Karty Anki: 1667557949742
GUID: EhK];(TD#i; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557949742: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **neterminální symbol rekurzivní zprava**.

### Odpověď (Back)

Mějme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\). Neterminální symbol \(A \in N\) nazveme **rekurzivní zprava** právě tehdy, když existuje derivace \(A \Rightarrow^+ \alpha A\), kde \(\alpha \in (N \cup \Sigma)^*\).

## Poznámka Anki 1667557962627

Karty Anki: 1667557962627
GUID: Pj)L~[E6~m; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667557962627: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **bezkontextovou gramatiku rekurzivní zprava**.

### Odpověď (Back)

Bezkontextovou gramatiku nazveme **rekurzivní zprava** právě tehdy, když obsahuje alespoň jeden neterminální symbol rekurzivní zprava.

## Poznámka Anki 1667558061612

Karty Anki: 1667558061612
GUID: NL[bQ%|eo+; štítky: bi-aag::p07.

Metadata původního zdroje pro kartu 1667558061612: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadanou bezkontextovou gramatiku vrátí ekvivalentní bezkontextovou gramatiku obsahující pouze **neterminály, které nejsou přímo rekurzivní zleva.**

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Bezkontextová gramatika \(G^\prime = (N^\prime, \Sigma, P^\prime, S)\), kde \(L(G^\prime) = L(G)\), obsahující pouze neterminály, které nejsou přímo rekurzivní zleva. 

**Postup:**

1. Inicializujeme \(N^\prime = N\).
2. V pravidlech \(P\) gramatiky \(G\) nalezneme postupně pro každý neterminál \(A \in N\) všechna pravidla s \(A\) na levé straně:

1. Pokud jsou tato pravidla následujícího tvaru: \(A \rightarrow A\alpha_1 \mid A\alpha_2 \mid \dots \mid A\alpha_m \mid \beta_1 \mid \beta_2 \mid \dots \mid \beta_n\), kde \(m \in \mathbb{N}\) je počet pravých stran pro \(A\) začínající neterminálem \(A\) a \(n \in \mathbb{N}\) je počet pravých stran pro \(A\) nezačínajících symbolem \(A\), pak do pravidel \(P^\prime\) gramatiky \(G^\prime\) přidáme následující pravidla:

- \(A \to \beta_1 A^\prime \mid \beta_2 A^\prime \mid \dots \mid \beta_n A^\prime \mid \beta_1 \mid \beta_2 \mid \dots \mid \beta_n\),
- \(A^\prime \to \alpha_1 A^\prime \mid \alpha_2 A^\prime \mid \dots \mid \alpha_m A^\prime \mid \alpha_1 \mid \alpha_2 \mid \dots \mid \alpha_m\),
- kde \(A^\prime\) je nový neterminál (tedy \(A^\prime \notin N\)). Zároveň \(A^\prime\) přidáme do \(N^\prime\).

2. Pro pravidla ostatního tvaru (tj. pokud \(A\) není neterminál přímo rekurzivní zleva), tyto pravidla pouze překopírujeme do \(P^\prime\).

### Doplňující pole (Extra)

Pomocí tohoto algoritmu zvládneme z libovolné bezkontextové gramatiky vyloučit přímou rekurzivitu zleva. Postup ovšem neodhalí neterminální symboly rekurzivní zleva, u nichž se rekurze objeví až po dvou čí více krocích v derivaci.

## Poznámka Anki 1667558111088

Karty Anki: 1667558111088
GUID: k_]@36z-M;; štítky: bi-aag::p07.

Metadata původního zdroje pro kartu 1667558111088: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro bezkontextovou gramatiku vrátí ekvivalentní bezkontextovou gramatiku, která **není rekurzivní zleva**.

### Odpověď (Back)

**Vstup:** **Vlastní** bezkontextová gramatika bez jednoduchých pravidel \(G = (N, \Sigma, P, S)\).

**Výstup:** Bezkontextová gramatika \(G^\prime = (N^\prime, \Sigma, P^\prime, S)\), kde \(L(G^\prime) = L(G)\), která není rekurzivní zleva. 

**Postup:**

1. Inicializujeme \(N^\prime = N\).
2. Zvolíme libovolné uspořádání všech neterminálních symbolů z \(N\): \(A_1, A_2, \dots, A_n\).
3. Postupně pro všechna \(i \in \{ 1, \dots, n \}\):

1. Postupně pro všechna \(j \in \{ 1, \dots, i-1 \}\):

1. Všechna pravidla z \(P\) tvaru \(A_i \to A_j \alpha\) nahradíme pravidly \(A_i \to \beta_1 \alpha \mid \beta_2 \alpha \mid \dots \mid \beta_k \alpha\), kde \(A_j \to \beta_1 \mid \beta_2 \mid \dots \beta_k\) jsou pravidla pro neterminál \(A_j\) z \(P^\prime\).
2. Pokud neterminál \(A_i\) v \(P\) není přímo rekurzivní zleva, pak všechna pravidla obsahující \(A_i\) na levé straně pravidel překopírujeme z \(P\) do \(P^\prime\). Jinak platí, že pravidla pro \(A_i\) jsou následujícího tvaru: \(A_i \rightarrow A_i\alpha_1 \mid A_i\alpha_2 \mid \dots \mid A_i\alpha_m \mid \beta_1 \mid \beta_2 \mid \dots \mid \beta_n\), kde \(m \in \mathbb{N}\) je počet pravých stran pro \(A_i\) začínající neterminálem \(A_i\) a \(n \in \mathbb{N}\) je počet pravých stran pro \(A_i\) nezačínajících symbolem \(A_i\). Pak do pravidel \(P^\prime\) gramatiky \(G^\prime\) přidáme následující pravidla:

- \(A_i \to \beta_1 A_i^\prime \mid \beta_2 A_i^\prime \mid \dots \mid \beta_n A_i^\prime \mid \beta_1 \mid \beta_2 \mid \dots \mid \beta_n\), 
- \(A_i^\prime \to \alpha_1 A_i^\prime \mid \alpha_2 A_i^\prime \mid \dots \mid \alpha_m A_i^\prime \mid \alpha_1 \mid \alpha_2 \mid \dots \mid \alpha_m\),
- kde \(A_i^\prime\) je nový neterminál (tedy \(A_i^\prime \notin N\)). Zároveň \(A_i^\prime\) přidáme do \(N^\prime\).

## Poznámka Anki 1667558175644

Karty Anki: 1667558175644
GUID: n(QPvq;%:D; štítky: bi-aag::p07.

Metadata původního zdroje pro kartu 1667558175644: v původním balíčku pozastavená karta.

### Otázka (Front)

Je algoritmicky řešitelný **problém ekvivalence dvou bezkontextových gramatik**?

### Odpověď (Back)

Není. Neexistuje algoritmus, který by pro dvě libovolné bezkontextové gramatiky vždy správně rozhodl, zdali jsou ekvivalentní.

## Poznámka Anki 1667558238218

Karty Anki: 1667558238218
GUID: jb,rNP*2-m; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558238218: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **nejednoznačnou** a **jednoznačnou bezkontextovou gramatiku**.

### Odpověď (Back)

Bezkontextovou gramatiku \(G\) nazveme **nejednoznačnou** právě tehdy, když existuje věta \(w\) generovaná gramatikou \(G\), která je výsledkem alespoň dvou různých derivačních stromů. V opačném případě je gramatika \(G\) **jednoznačná**.

## Poznámka Anki 1667558278413

Karty Anki: 1667558278414
GUID: v/lJUiU({x; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558278414: v původním balíčku pozastavená karta.

### Otázka (Front)

Existuje **algoritmus**, který by pro libovolnou zadanou bezkontextovou gramatiku vždy správně rozhodl, zda-li je **nejednoznačná**?

### Odpověď (Back)

Ne. Jedná se o tzv. nerozhodnutelný problém.

## Poznámka Anki 1667558321880

Karty Anki: 1667558321880
GUID: m=gP{U)cW|; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558321880: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **inherentně nejednoznačný** bezkontextový jazyk a **jednoznačný** bezkontextový jazyk.

### Odpověď (Back)

Bezkontextový jazyk \(L\) nazveme **inherentně nejednoznačný** právě tehdy, když neexistuje jednoznačná bezkontextová gramatika taková, že \(L(G) = L\). V opačném případě (tj. existuje-li jednoznačná bezkontextová gramatika generující jazyk \(L\)) nazveme jazyk \(L\) **jednoznačný**.

## Poznámka Anki 1667558354438

Karty Anki: 1667558354438
GUID: kLmic:t#T^; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558354438: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **bezkontextovou gramatiku bez **\(\varepsilon\)**-pravidel**.

### Odpověď (Back)

Bezkontextová gramatika \(G = (N, \Sigma, P, S)\) je **bez **\(\varepsilon\)**-pravidel** právě tehdy, když obsahuje nejvýše jedno \(\varepsilon\)-pravidlo, které je tvaru \(S \rightarrow \varepsilon\), přičemž \(S\) se nevyskytuje na pravé straně žádného pravidla z \(P\).

### Doplňující pole (Extra)

Můžeme si všimnout, že pokud bezkontextová gramatika není bez \(\varepsilon\)-pravidel, pak zároveň není kontextová. Zatímco každá bezkontextová gramatika bez \(\varepsilon\)-pravidel je zároveň kontextová.

## Poznámka Anki 1667558376858

Karty Anki: 1667558376858
GUID: LgD_(Yr}2}; štítky: bi-aag::p07.

Metadata původního zdroje pro kartu 1667558376858: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **zkracující neterminální symbol**.

### Odpověď (Back)

Uvažujme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\). Neterminální symbol \(A \in N\) nazveme **zkracující**, pokud v \(G\) existuje derivace \(A \Rightarrow^+ \varepsilon\).

### Doplňující pole (Extra)

Výskyt \(\varepsilon\)-pravidel v bezkontextové gramatice jinde než u počátečního neterminálu, který se nevyskytuje na pravé straně žádného z pravidel, tedy způsobuje, že je daná gramatika zkracující (délka následující větné formy může být kratší).

## Poznámka Anki 1667558504343

Karty Anki: 1667558504344
GUID: v8(3Gc3Q2q; štítky: bi-aag::p07.

Metadata původního zdroje pro kartu 1667558504344: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadanou bezkontextovou gramatiku vrátí ekvivalentní bezkontextovou gramatiku **bez **\(\varepsilon\)**-pravidel**.

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Bezkontextová gramatika bez \(\varepsilon\)-pravidel \(G^\prime = (N^\prime, \Sigma, P^\prime, S^\prime)\) taková, že \(L(G^\prime) = L(G)\).

**Postup:**

1. V gramatice \(G\) nalezneme množinu \(N_\varepsilon\) obsahující všechny zkracující neterminály:

1. Inicializujeme \(N_\varepsilon = \{ A : (A \to \varepsilon) \in P \}\).

2. Projdeme všechna pravidla v \(P\) a pokud je zkoumané pravidlo ve tvaru \(B \rightarrow C_1C_2\dots{}C_k\), kde \(k\) je počet symbolů na pravé straně pravidla a \(\forall C_i: C_i \in N_\varepsilon\), pak \(N_\varepsilon = N_\varepsilon \cup \{B\}\) (všimněte si, že každé \(C_i\) musí být neterminál). 
3. Předchozí krok opakujeme, dokud se množina \(N_\varepsilon\) mění.

2. \(N^\prime = N \cup \{S^\prime\}\), kde \(S^\prime \notin N\). Neterminál \(S^\prime\) bude zároveň počátečním neterminálem gramatiky \(G^\prime\). 
3. Do pravidel \(P^\prime\) gramatiky \(G^\prime\) přidáme všechna pravidla \(P\) z gramatiky \(G\) (kromě \(\varepsilon\)-pravidel): \(P' = P \setminus \{A \rightarrow \varepsilon : (A \rightarrow \varepsilon) \in P\}\).
4. Nyní v \(P^\prime\) projdeme každé pravidlo, které na pravé straně obsahuje alespoň jeden neterminální symbol z \(N_\varepsilon\) a do \(P^\prime\) přidáme jeho upravené „kopie“ — pro každou možnost zkrácení jednu (kromě čistě \(\varepsilon\)-pravidel): \(P' = P' \cup \{A \rightarrow \alpha_1 \alpha_2 : (A \rightarrow \alpha_1 X \alpha_2) \in P' \wedge X \in N_{\varepsilon} \wedge \alpha_1 \alpha_2 \in (N \cup \Sigma)^* \wedge \alpha_1 \alpha_2 \neq \varepsilon\}\).  
5. Pokud \(S \in N_\varepsilon\), pak \(\varepsilon \in L(G)\). V tom případě musíme \(\varepsilon\)-pravidlo přidat i k počátečnímu neterminálu gramatiky \(G^\prime\):

1. Pokud v \(P^\prime\) neexistuje pravidlo, které by na pravé straně obsahovalo neterminál \(S\), pak do \(P^\prime\) přidáme pravidlo \(S \to \varepsilon\) a nastavíme \(S^\prime = S\).
2. Jinak (tedy pokud \(P^\prime\) obsahuje pravidlo, který by na pravé straně obsahovalo \(S\)) přidáme do \(P^\prime\) pravidlo \(S^\prime \to S \mid \varepsilon\).

### Doplňující pole (Extra)

Intuitivně nám pravidlo \(A \rightarrow \varepsilon\) říká, že neterminál \(A\) může v průběhu derivace kdykoli „zmizet“. Pokud tedy chceme \(\varepsilon\)-pravidla odstranit, musíme tuto jejich schopnost nahradit jinak — vyhledáme všechny pravé strany pravidel, která \(A\) obsahují, a vytvoříme jejich „kopie“, kde zvážíme všechny možnosti, jak každý jednotlivý výskyt \(A\) může „zmizet“. Kromě „klasických“ \(\varepsilon\)-pravidel, musíme ovšem také pohlídat případy, kdy daný neterminál generuje \(\varepsilon\) po \(k \geq 2\) krocích — například pokud bezkontextová gramatika obsahuje pravidla, která jsou tvaru: \(A \rightarrow BC, B \rightarrow \varepsilon, C \rightarrow \varepsilon\), pak \(A\) obsahuje vlastně „skryté“ \(\varepsilon\)-pravidlo, neboť \(A \Rightarrow^3 \varepsilon\).

V prvním kroku algoritmu pro danou bezkontextovou gramatiku nalezneme všechny zkracující neterminály — množina \(N_\varepsilon\). Tato množina obsahuje tedy i neterminály se „skrytým“ \(\varepsilon\)-pravidlem. Ve třetím kroku odstraníme z gramatiky všechna \(\varepsilon\)-pravidla a ve čtvrtém vyhledáme všechny pravé strany pravidel obsahující některý z neterminálů z množiny \(N_\varepsilon\). Pro tyto pravé strany vytvoříme výše zmíněné „kopie“ se všemi možnými kombinacemi „zmizení“.

## Poznámka Anki 1667558527925

Karty Anki: 1667558527925
GUID: x[/VtAZbAX; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558527925: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **jednoduché pravidlo** v bezkontextové gramatice.

### Odpověď (Back)

Uvažujme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\). Pravidlo tvaru \(A \rightarrow B\), kde \(A,B \in N\), nazveme **jednoduché**.

### Doplňující pole (Extra)

Jednoduchá pravidla usnadňují v mnoha případech návrh bezkontextové gramatiky. Stejně jako \(\varepsilon\)-pravidla ale ani jednoduchá pravidla nejsou pro návrh bezkontextové gramatiky nezbytná.

## Poznámka Anki 1667558554822

Karty Anki: 1667558554822
GUID: rZ`1aW`Js0; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558554822: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **bezkontextovou gramatiku bez jednoduchých pravidel**.

### Odpověď (Back)

Bezkontextová gramatika \(G = (N, \Sigma, P, S)\) je bez jednoduchých pravidel právě tehdy, když \(P\) neobsahuje žádné jednoduché pravidlo.

## Poznámka Anki 1667558632661

Karty Anki: 1667558632661
GUID: H%IV/uQep0; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558632661: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadanou bezkontextovou gramatiku vrátí ekvivalentní bezkontextovou gramatiku **bez jednoduchých pravidel**.

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Bezkontextová gramatika bez jednoduchých pravidel \(G^\prime = (N, \Sigma, P^\prime, S)\) taková, že \(L(G^\prime) = L(G)\).

**Postup:**

1. V gramatice \(G\) nalezneme pro každý neterminál \(A \in N\) jeho množinu \(N_A = \{ B : B \in N \wedge \text{v gramatice } G \text{ existuje derivace ve tvaru } (A \Rightarrow^* B) \}\):

1. Inicializujeme \(N_A = \{A\}\) (neboť \(A \Rightarrow^0 A\)).

2. Projdeme všechna pravidla v \(P\) a pokud je zkoumané pravidlo ve tvaru \(B \rightarrow C\), kde \(B \in N_A \land C \in N\), pak \(N_A = N_A \cup \{C\}\).
3. Předchozí krok opakujeme, dokud se množina \(N_A\) mění.

2. Do pravidel \(P^\prime\) gramatiky \(G^\prime\) přidáme všechna pravidla z gramatiky \(G\) (kromě jednoduchých pravidel): \(P^\prime = P \setminus \{ A \to B : (A \to B) \in P \}\).   
3. Pro každý neterminál \(A\) dále přidáme do gramatiky \(G^\prime\) všechna pravidla ve tvaru \(A \rightarrow \alpha\), kde \(\alpha\) je pravá strana pravidla v \(G\) pro některý z neterminálů v \(N_A\), která není rovna samotnému neterminálu: \(\forall A \in N: P^\prime = P^\prime \cup \{A \rightarrow \alpha : (B \rightarrow \alpha) \in P \wedge B \in N_A \wedge \alpha \in (N \cup \Sigma)^* \setminus N\}\).

### Doplňující pole (Extra)

Základní myšlenka algoritmu vyloučení jednoduchých pravidel je, že jednoduchá pravidla můžeme vyloučit pomocí dosazování.

## Poznámka Anki 1667558666831

Karty Anki: 1667558666831
GUID: ERta*yM=`6; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558666831: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **bezkontextovou gramatiku bez cyklů**.

### Odpověď (Back)

Řekneme, že bezkontextová gramatika \(G = (N, \Sigma, P, S)\) je **bez cyklů** právě tehdy, když pro žádný neterminál \(A \in N\) neexistuje derivace \(A \Rightarrow^+ A\).

## Poznámka Anki 1667558688405

Karty Anki: 1667558688405
GUID: ihSM9k/l;5; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558688405: v původním balíčku pozastavená karta.

### Otázka (Front)

V jakých případech máme u bezkontextové gramatiky zaručeno, že je **bez cyklů**?

### Odpověď (Back)

Pokud je bezkontextová gramatika bez jednoduchých a \(\varepsilon\)-pravidel, poté je bez cyklů.

## Poznámka Anki 1667558738847

Karty Anki: 1667558738847
GUID: z{B<&#}$W=; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558738847: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **generující** a **negenerující** symbol v bezkontextové gramatice.

### Odpověď (Back)

Nechť \(G = (N, \Sigma, P, S)\) je bezkontextová gramatika. Symbol \(X \in (N \cup \Sigma)\) je **generující** v \(G\) právě tehdy, když existuje derivace \(X \Rightarrow^* w\), kde \(w \in \Sigma^*\). V opačném případě je symbol \(X\) **negenerující**.

### Doplňující pole (Extra)

Tato definice tedy říká, že symbol \(X\) je generující právě tehdy, když z něj lze generovat řetězec nad abecedou terminálních symbolů (třeba i prázdný). Můžeme si všimnout, že každý terminální symbol je z definice generující.

Evidentně platí, že odstraníme-li z bezkontextové gramatiky \(G\) všechny její negenerující symboly a všechna pravidla \(A \rightarrow \alpha\), kde \(\alpha\) obsahuje některý z negenerujících symbolů, \(L(G)\) se nezmění — tj. vzniklá gramatika bude ekvivalentní.

## Poznámka Anki 1667558774845

Karty Anki: 1667558774845
GUID: hfg;PQ<<KT; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558774845: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadanou bezkontextovou gramatiku vrátí ekvivalentní bezkontextovou gramatiku **bez negenerujících symbolů**.

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Bezkontextová gramatika \(G^\prime = (N^\prime, \Sigma, P^\prime, S)\) taková, že neobsahuje žádný negenerující symbol a \(L(G^\prime) = L(G)\).

**Postup:**

1. V gramatice \(G\) nalezneme množinu \(N_R\) obsahující všechny generující symboly:

1. Inicializujeme \(N_R = \{ a : a \in \Sigma\}\).\(N_R = N_R \cup \{ A : (A \to \varepsilon) \in P \}\).
2. Projdeme všechna pravidla v \(P\) a pokud je zkoumané pravidlo ve tvaru \(A \to \alpha\), kde \(\alpha \in (N \cup \Sigma)^+\) a každý symbol v \(\alpha\) je generující, pak \(N_R = N_R \cup \{A\}\).
3. Předchozí krok opakujeme, dokud se množina \(N_R\) mění.\(N^\prime = N_R \cap N\).

2. Do pravidel \(P^\prime\) gramatiky \(G^\prime\) přidáme všechna pravidla z \(P\), které obsahují pouze a jenom generující symboly: \(P^\prime = \{ A \to \varepsilon : (A \to \varepsilon)\in P \}\).

3. \(P^\prime = P^\prime \cup \{ A \to \alpha : A \in N_R \wedge \alpha = a_1a_2\dots a_{|\alpha|}  \wedge a_1,a_2,\dots,a_{|\alpha|} \in N_R \}\).

### Doplňující pole (Extra)

Algoritmicky tuto úlohu vyřešíme tak, že nejprve nalezneme množinu všech symbolů, které jsou generující. Negenerujícími symboly budou poté všechny ty, které v naší množině nebudou.

## Poznámka Anki 1667558803549

Karty Anki: 1667558803549
GUID: ks=buCMC-z; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558803549: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **dostupný** a **nedostupný** symbol v bezkontextové gramatice.

### Odpověď (Back)

Uvažujme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\). Symbol \(X \in (N \cup \Sigma)\) je **nedostupný** v \(G\) pravě tehdy, když neexistuje derivace \(S \Rightarrow^* \alpha X \beta\), kde \(\alpha, \beta \in (N \cup \Sigma)^*\). V opačném případě je symbol \(X\) **dostupný**.

### Doplňující pole (Extra)

Symbol \(X\) (ať už terminál či neterminál) je tedy nedostupný, když se neobjeví v žádné větné formě — tj. žádná derivace začínající počátečním neterminálem negeneruje větnou formu takovou, že by obsahovala symbol \(X\).

Evidentně opět platí, že odstraníme-li z bezkontextové gramatiky \(G\) všechny její nedostupné symboly a jejich pravidla, \(L(G)\) se nezmění — tj. vzniklá gramatika bude ekvivalentní.

## Poznámka Anki 1667558839822

Karty Anki: 1667558839822
GUID: Cz)i/*1~6-; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558839822: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadanou bezkontextovou gramatiku vrátí ekvivalentní bezkontextovou gramatiku **bez nedostupných symbolů**.

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Bezkontextová gramatika \(G^\prime = (N^\prime, \Sigma^\prime, P^\prime, S)\) taková, že neobsahuje žádný nedostupný symbol a \(L(G^\prime) = L(G)\).

**Postup:**

1. V gramatice \(G\) nalezneme množinu \(D\) obsahující všechny dostupné symboly:

1. Inicializujeme \(D = \{ S \}\).

2. Projdeme všechna pravidla v \(P\) a pokud je zkoumané pravidlo ve tvaru \(A \to \alpha\), kde \(\alpha \in (N \cup \Sigma)^+\) a \(A \in D\), pak do \(D\) přidáme všechny symboly obsažené v \(\alpha\).
3. Předchozí krok opakujeme, dokud se množina \(D\) mění.

2. \(N^\prime = N \cap D\).

3. \(\Sigma^\prime = \Sigma \cap D\).
4. Do pravidel \(P^\prime\) gramatiky \(G^\prime\) přidáme všechna pravidla z \(P\), které obsahují pouze a jenom dostupné symboly: \(P^\prime = \{ A \to \alpha : (A \to \alpha)\in P \wedge A \in N^\prime \wedge \alpha \in D^* \}\).

### Doplňující pole (Extra)

Algoritmicky tuto úlohu vyřešíme tak, že nalezneme množinu všech symbolů, které jsou dostupné. Nedostupnými symboly budou poté všechny ty, které v naší množině nebudou.

## Poznámka Anki 1667558863240

Karty Anki: 1667558863240
GUID: KER9rwWbuM; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558863240: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **zbytečný** a **užitečný** **symbol** v bezkontextové gramatice.

### Odpověď (Back)

Nechť \(G = (N, \Sigma, P, S)\) je bezkontextová gramatika. Symbol \(X \in (N \cup \Sigma)\) je **zbytečný** v \(G\) právě tehdy, když neexistuje derivace \(S \Rightarrow^* \alpha X \beta \Rightarrow^* w\), kde \(\alpha, \beta \in (N \cup \Sigma)^*\) a \(w \in \Sigma^*\). V opačném případě je symbol \(X\) **užitečný**.

## Poznámka Anki 1667558904853

Karty Anki: 1667558904853
GUID: pNJ9=qHW^Y; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558904853: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **redukovanou bezkontextovou gramatiku**.

### Odpověď (Back)

Danou bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\) nazveme **redukovanou** právě tehdy, když neobsahuje zbytečné symboly.

## Poznámka Anki 1667558960899

Karty Anki: 1667558960899
GUID: HM-]!uc,}T; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558960899: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadanou bezkontextovou gramatiku vrátí ekvivalentní bezkontextovou gramatiku **bez zbytečných symbolů**.

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Redukovaná bezkontextová gramatika \(G^\prime = (N^\prime, \Sigma, P^\prime, S)\) taková, že \(L(G^\prime) = L(G)\).

**Postup:**

1. Převedeme \(G\) na bezkontextovou gramatiku \(G_1\), která neobsahuje negenerující symboly.
2. Převedeme \(G_1\) na bezkontextovou gramatiku \(G_2\), která neobsahuje nedostupné symboly.
3. \(G^\prime = G_2\).

### Doplňující pole (Extra)

Rozmyslete si, že kroky v algoritmu musíme provést právě v tomto pořadí (nelze je prohodit).

## Poznámka Anki 1667558987074

Karty Anki: 1667558987074
GUID: y34=E-QdE|; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667558987074: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **vlastní** bezkontextovou gramatiku.

### Odpověď (Back)

Bezkontextová gramatika \(G = (N, \Sigma, P, S)\) je **vlastní** právě tehdy, když je bez cyklů, bez \(\varepsilon\)-pravidel a nemá zbytečné symboly.

### Doplňující pole (Extra)

Každou bezkontextovou gramatiku můžeme převést na vlastní.

## Poznámka Anki 1667559041434

Karty Anki: 1667559041435
GUID: GZ=b(4pq_:; štítky: bi-aag::p07 bi-spol::02.

Metadata původního zdroje pro kartu 1667559041435: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadanou bezkontextovou gramatiku vrátí ekvivalentní bezkontextovou gramatiku, která je **vlastní**.

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Vlastní bezkontextová gramatika \(G^\prime\) taková, že \(L(G^\prime) = L(G)\).

**Postup:**

1. Převedeme \(G\) na ekvivalentní bezkontextovou gramatiku \(G_1\) bez \(\varepsilon\)-pravidel.
2. Převedeme \(G_1\) na ekvivalentní bezkontextovou gramatiku \(G_2\) bez jednoduchých pravidel.
3. Převedeme \(G_2\) na ekvivalentní redukovanou bezkontextovou gramatiku \(G_3\).
4. \(G^\prime = G_3\).

### Doplňující pole (Extra)

Rozmyslete si, že kroky v algoritmu je nutné provést v tomto pořadí (nelze je prohodit).

