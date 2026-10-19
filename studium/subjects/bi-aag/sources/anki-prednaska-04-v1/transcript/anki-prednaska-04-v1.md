# BI-AAG – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aag/BI-AAG.apkg; APKG SHA-256 0383847389324f3b83b349363b7ad16a6bf91673c90b7a96ed1a57b25a85f8af. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b9cda20d5a5a9d1ff47d4e1fc58b10ed3ac7a37c72c6c1431cc7cb67e2ca10c.
Původní balíčky: BI-AAG
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1665829625218

Karty Anki: 1665829625219
GUID: i!e8o~>vF&; štítky: bi-aag::p04 bi-spol::01.

### Otázka (Front)

Definujte **regulární výraz**.

### Odpověď (Back)

Nechť** **\(\Sigma\) je abeceda.** Regulární výraz** (RV) nad \(\Sigma\) definujeme následovně:

- \(\emptyset,\varepsilon\) a \(a \in \Sigma\) jsou regulární výrazy nad \(\Sigma\).
- Jsou-li \(V\) a \(W\) regulární výrazy nad \(\Sigma\), pak

- \((V+W)\) (sjednocení, alternativa),
- \((V.W)\) (zřetězení),
- \((V)^*\) (iterace),

    jsou regulární výrazy nad \(\Sigma\).

### Doplňující pole (Extra)

Regulární výrazy \(\emptyset, \varepsilon\) a \(a \in \Sigma\) také nazýváme elementární regulární výrazy.

## Poznámka Anki 1665829653229

Karty Anki: 1665829653229
GUID: lrgpuEWP+z; štítky: bi-aag::p04 bi-spol::01.

Metadata původního zdroje pro kartu 1665829653229: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **hodnotu** regulárního výrazu.

### Odpověď (Back)

Hodnotu \(h(V)\) regulárního výrazu \(V\) definujeme následovně:

- \(h(\emptyset)= \emptyset\), 
- \(h(\varepsilon)=\{\varepsilon\}\), 
- \(h(a)=\{a\}\), kde \(a \in \Sigma\),
- \(h(V+W)=h(V) \cup h(W)\), kde \(V\) a \(W\) jsou regulární výrazy,
- \(h(V.W)=h(V).h(W)\), kde \(V\) a \(W\) jsou regulární výrazy,
- \(h(V^*)=(h(V))^*\), kde \(V\) je regulární výraz.

### Doplňující pole (Extra)

**Hodnota** regulární výrazu je jazyk, který daný regulární výraz reprezentuje.

## Poznámka Anki 1665829686898

Karty Anki: 1665829686898
GUID: tlLJ#^9|Cv; štítky: bi-aag::p04 bi-spol::01.

Metadata původního zdroje pro kartu 1665829686898: v původním balíčku pozastavená karta.

### Otázka (Front)

Kdy o dvou regulárních výrazech řekneme, že jsou **ekvivalentní**?

### Odpověď (Back)

Regulární výrazy \(V\) a \(W\) jsou **ekvivalentní** (značíme \(V = W\)), jestliže mají stejnou hodnotu, tj. \(h(V) = h(W)\).

## Poznámka Anki 1665829707164

Karty Anki: 1665829707164
GUID: vX&?FyW|~m; štítky: bi-aag::p04 bi-spol::01.

Metadata původního zdroje pro kartu 1665829707164: v původním balíčku pozastavená karta.

### Otázka (Front)

Kdy o dvou regulárních výrazech řekneme, že jsou **identické**?

### Odpověď (Back)

Regulární výrazy \(V\) a \(W\) jsou **identické** (značíme \(V \equiv W\)), jestliže se jedná o úplně stejné řetězce symbolů.

## Poznámka Anki 1665829729422

Karty Anki: 1665829729422
GUID: xqLy6e3I8U; štítky: bi-aag::p04 bi-spol::01.

Metadata původního zdroje pro kartu 1665829729422: v původním balíčku pozastavená karta.

### Otázka (Front)

Kdy o dvou regulárních výrazech řekneme, že jsou si **podobné**?

### Odpověď (Back)

Regulární výrazy \(V\) a \(W\) jsou si **podobné** (značíme \(V \cong W\)), dají-li se na sebe převést pomocí posloupnosti následujících operací:

- \(V + V = V\)

- \(V + \emptyset = V\)

- \((V + W) + Z = V + (W + Z)\)

- \(V + W = W + V\)

- \(V\emptyset = \emptyset V = \emptyset\)

- \(V \varepsilon = \varepsilon V = V\)

## Poznámka Anki 1665829816210

Karty Anki: 1665829816210
GUID: ekOL{A5rTR; štítky: bi-aag::p04 bi-spol::01.

Metadata původního zdroje pro kartu 1665829816210: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **derivaci** regulárního výrazu **dle symbolu**.

### Odpověď (Back)

Mějme regulární výraz \(V\) nad abecedou \(\Sigma\) a symboly \(a,b \in \Sigma\) takové, že \(a \neq b\). Derivaci regulárního výrazu \(V\) dle \(a\) zapisujme jako \(\frac{\mathrm{d}V}{\mathrm{d}a}\) a definujeme následovně:

Pokud \(V\) je elementární regulární výraz:

- \(\frac{\mathrm{d}V}{\mathrm{d}a} = 
\begin{cases}
\emptyset & \text{ pokud } V = \varepsilon, \\
        \emptyset & \text{ pokud } V = \emptyset, \\
        \varepsilon & \text{ pokud } V = a, \\
        \emptyset & \text{ pokud } V = b.
\end{cases}\)

Pokud \(V\) není elementární regulární výraz:

- (sjednocení) Pokud \(V = U + W\), pak \(\frac{\mathrm{d}V}{\mathrm{d}a} = \frac{\mathrm{d}(U + W)}{\mathrm{d}a} = \frac{\mathrm{d}U}{\mathrm{d}a} + \frac{\mathrm{d}W}{\mathrm{d}a}\).

- (zřetězení) Pokud \(V = UW\), pak \(\frac{\mathrm{d}V}{\mathrm{d}a} = \frac{\mathrm{d}(UW)}{\mathrm{d}a} =
\begin{cases}
 \frac{\mathrm{d}U}{\mathrm{d}a}W & \text{ pokud } \varepsilon \notin h(U), \\
        \frac{\mathrm{d}U}{\mathrm{d}a}W + \frac{\mathrm{d}W}{\mathrm{d}a} & \text{ pokud } \varepsilon \in h(U).
\end{cases}\)

- (iterace) Pokud \(V = U^*\), pak \(\frac{\mathrm{d}V}{\mathrm{d}a} = \frac{\mathrm{d}(U^*)}{\mathrm{d}a} = \frac{\mathrm{d}U}{\mathrm{d}a}U^*\).

### Doplňující pole (Extra)

Nechť \(V\) je regulární výraz nad abecedou \(\Sigma\). Výsledkem derivace regulárního výrazu \(V\) dle symbolu \(a\) je regulární výraz \(V^\prime\) takový, že platí \(h(V')=\{y : ay\in h(V)\}\). Pokud si tedy představíme všechny řetězce začínající symbolem \(a\), které popisuje výraz \(V\) a pokud těmto všem řetězcům odebereme předponu \(a\), získáme hodnotu regulárního výrazu \(V^\prime\), který je výsledkem derivace \(V\) dle \(a\).

## Poznámka Anki 1665829836981

Karty Anki: 1665829836981
GUID: AUu~{@sT!a; štítky: bi-aag::p04 bi-spol::01.

Metadata původního zdroje pro kartu 1665829836981: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **derivaci** regulárního výrazu **dle řetězce**.

### Odpověď (Back)

Mějme regulární výraz \(V\) nad abecedou \(\Sigma\) a řetězec \(x=a_1a_2\dots{}a_n\), kde \(a_1, \dots, a_n \in \Sigma\). Derivaci regulárního výrazu \(V\) dle řetězce \(x\) zapisujeme jako \(\frac{\mathrm{d}V}{\mathrm{d}x}\) a definujeme následovně: \(\frac{\mathrm{d}V}{\mathrm{d}x} = \frac{\mathrm{d}}{\mathrm{d}a_n} (\frac{\mathrm{d}}{\mathrm{d}a_{n-1}} (\dots\frac{\mathrm{d}}{\mathrm{d}a_2} (\frac{\mathrm{d}V}{\mathrm{d}a_1})))\).

## Poznámka Anki 1665829886179

Karty Anki: 1665829886179
GUID: ggE)>GZ)1X; štítky: bi-aag::p04 bi-spol::01.

Metadata původního zdroje pro kartu 1665829886179: v původním balíčku pozastavená karta.

### Otázka (Front)

Necť \(V, \alpha\) a \(\beta\) jsou regulární výrazy. Jaké je řešení **levé regulární rovnice** \(V=V\alpha+\beta\)?

### Odpověď (Back)

\(V=\beta\alpha^*\)

## Poznámka Anki 1665829914916

Karty Anki: 1665829914916
GUID: AE8n^BitG$; štítky: bi-aag::p04 bi-spol::01.

Metadata původního zdroje pro kartu 1665829914916: v původním balíčku pozastavená karta.

### Otázka (Front)

Necť \(V, \alpha\) a \(\beta\) jsou regulární výrazy. Jaké je řešení **pravé regulární rovnice** \(V=\alpha V+\beta\)?

### Odpověď (Back)

\(V=\alpha^*\beta\)

## Poznámka Anki 1665852076108

Karty Anki: 1665852076111
GUID: u-CYI|!8K1; štítky: bi-aag::p04.

Metadata původního zdroje pro kartu 1665852076111: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadanou regulární gramatiku \(G\), vrátí konečný automat \(M\) takový, že \(L(M) = L(G)\).

### Odpověď (Back)

**Vstup:** Regulární gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Konečný automat \(M = (Q, \Sigma, \delta, q_S, F)\) takový, že \(L(M) = L(G)\).

**Postup:**

1. Pro každý neterminál \(A \in N\) vytvoříme nekoncový stav \(q_A\) v automatu \(M\).
2. Stav \(q_S\) odpovídající počátečnímu neterminálu \(S\) bude počáteční stav automatu \(M\).
3. Pokud \(G\) neobsahuje pravidlo \(S \to \varepsilon\), pak \(M\) bude mít pouze jeden koncový stav \(q_K\) takový, že \(K\) neodpovídá žádnému neterminálnímu symbolu, tedy \(K \notin N\). V opačném případě bude koncový navíc i stav \(q_S\).
4. Pro každé pravidlo tvaru \(A \to aB\) přidáme přechod ze stavu \(q_A\) na symbol \(a\) do stavu \(q_B\).

5. Pro každé pravidlo tvaru  \(A \to a\) přidáme přechod ze stavu \(q_A\) na symbol \(a\) do koncového stavu \(q_K\).

### Doplňující pole (Extra)

Výstupem algoritmu je nedeterministický konečný automat s jedním počátečním stavem. V ojedinělých případech se může stát, že výsledný konečný automat bude deterministický.

## Poznámka Anki 1665852167316

Karty Anki: 1665852167316
GUID: CFKnZ]I/NK; štítky: bi-aag::p04.

Metadata původního zdroje pro kartu 1665852167316: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadaný NKA \(M\), vrátí regulární gramatiku \(G\) takovou, že \(L(G) = L(M)\).

### Odpověď (Back)

**Vstup:** Nedeterministický konečný automat \(M = (Q, \Sigma, \delta, q_S, F)\), kde \(Q \cap \Sigma = \emptyset\).

**Výstup:** Regulární gramatika \(G\) taková, že \(L(G) = L(M)\).

**Postup:**

1. Pro každý stav \(q_A\) vytvoříme v gramatice neterminál \(A\).
2. Pro přechody typu \(q_B \in \delta(q_A,a)\), kde \(q_B\) je nekoncový stav, přidáme do gramatiky pravidlo \(A \to aB\).

3. Pro přechody typu \(q_B \in \delta(q_A,a)\), kde \(q_B\) je koncový stav, přidáme do gramatiky pravidla \(A \to aB \mid a\).

4. Pokud je \(q_S\) nekoncový stav, pak neterminál \(S\) odpovídající počátečnímu stavu \(q_S\) je startovacím neterminálem gramatiky. Jinak do gramatiky přidáme pravidlo \(S \to \varepsilon\) a zkontrolujeme, zdali se neterminál \(S\) nevyskytuje na pravé straně pravidel: 

1. Pokud nevyskytuje, pak neterminál \(S\) odpovídající počátečnímu stavu \(q_S\) je startovacím neterminálem gramatiky. 
2. Pokud vyskytuje, pak vytvoříme nový neterminál \(S'\) s pravidlem \(S' \to \varepsilon\). Pravidlo \(S \to \varepsilon\) zrušíme. Všechny pravé strany pravidel pro neterminál \(S\) přidáme k neterminálu \(S'\). Neterminál \(S^\prime\) je startovacím neterminálem gramatiky.

