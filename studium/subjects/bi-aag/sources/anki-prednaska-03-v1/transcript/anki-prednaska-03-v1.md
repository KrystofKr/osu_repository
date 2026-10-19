# BI-AAG – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aag/BI-AAG.apkg; APKG SHA-256 0383847389324f3b83b349363b7ad16a6bf91673c90b7a96ed1a57b25a85f8af. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b9cda20d5a5a9d1ff47d4e1fc58b10ed3ac7a37c72c6c1431cc7cb67e2ca10c.
Původní balíčky: BI-AAG
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1665133629176

Karty Anki: 1665133629177
GUID: yJwd81?4HH; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665133629177: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **ekvivalentní** konečné automaty.

### Odpověď (Back)

Konečné automaty \(M_1\) a \(M_2\) nazýváme **ekvivalentní**, jestliže přijímají stejný jazyk, tj. \(L(M_1) = L(M_2)\).

### Doplňující pole (Extra)

Ekvivalentní automaty nemusí vypadat (například po zakreslení obrázkem) úplně stejně.

## Poznámka Anki 1665133757542

Karty Anki: 1665133757542
GUID: f5wBO/}BqI; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665133757542: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **minimální DKA**.

### Odpověď (Back)

Nechť \(M = (Q, \Sigma, \delta, q_0, F)\) je DKA. Automat \(M\) nazveme (stavově) **minimální DKA**, pokud neexistuje \(M' = (Q', \Sigma, \delta ', q_0', F')\) takový, že \(L(M) = L(M')\) a \(|Q'| < |Q|\).

### Doplňující pole (Extra)

DKA je minimální, pokud neexistuje ekvivalentní DKA s menším množstvím stavů.

Minimální DKA přijímající prázdný jazyk má pouze jeden stav, který je počáteční a zároveň nekoncový. Ačkoliv je tento stav z definice zbytečný, v automatu jej ponecháváme, neboť každý KA musí mít definován počáteční stav.

## Poznámka Anki 1665133843537

Karty Anki: 1665133843537
GUID: yL<96H-gCy; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665133843537: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **ekvivalentní stavy** DKA.

### Odpověď (Back)

Nechť \(M = (Q, \Sigma, \delta, q_0, F)\) je deterministický konečný automat. Stavy \(p, q \in Q\) nazveme **ekvivalentní, **značíme \(p \sim q\), právě tehdy, když pro všechny řetězce \(w \in \Sigma^*\) platí, že \(\hat{\delta}(p,w) \in F \iff \hat{\delta}(q,w) \in F\).

### Doplňující pole (Extra)

Symbolem \(\hat{\delta}\) značíme **zobecněnou přechodovou funkci DKA. **Předpis této funkce je \(\hat{\delta}: Q \times \Sigma^* \to Q\)  a definovaná je pro \(q_1, q_2 \in Q\) a \(w \in \Sigma^*\) následovně: \(\hat{\delta}(q_1,w) = q_2 \) právě tehdy, když \((q_1,w) \vdash^* (q_2,\varepsilon)\).

Platí, že pokud u DKA sloučíme stavy, které jsou spolu ekvivalentní, pak jazyk, který daný automat přijímá, se nezmění.

## Poznámka Anki 1665133988363

Karty Anki: 1665133988363
GUID: Iqw9@&;U^_; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665133988363: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadaný DKA \(M\), vrátí DKA \(M^\prime\) takový, že v \(M^\prime\) žádné dva **stavy nejsou ekvivalentní** a** **\(L(M) = L(M^\prime)\).

### Odpověď (Back)

**Vstup:** DKA \(M = (Q, \Sigma, \delta, q_0, F)\).

**Výstup:** DKA \(M^\prime = (Q^\prime, \Sigma, \delta^\prime, q_0^\prime, F^\prime)\), kde žádné dva **stavy nejsou ekvivalentní** a** **\(L(M^\prime) = L(M)\).

**Postup:**

1. Pro \(M\) nalezneme vzájemně ekvivalentní stavy (třídy ekvivalence) pomocí následujícího iterativního předpisu:

1. Vyrobíme třídy ekvivalence určující, které stavy z \(Q\) jsou ekvivalentní pro řetězce délky \(0\): Stavy \(p\) a \(q\) jsou v tomto případě ekvivalentní právě tehdy, když jsou oba koncové, nebo oba nekoncové. 
2. Vyrobíme třídy ekvivalence určující, které stavy z \(Q\) jsou ekvivalentní pro řetězce délky \(1\): Platí, že dva stavy \(p\) a \(q\) jsou ekvivalentní pro řetězce délky \(1\), pokud jsou ekvivalentní pro řetězce délky \(0\) a pro každý symbol \(a \in \Sigma\) platí, že \(\delta(p,a) \sim_0 \delta(q,a)\).
3. \(\dots\)
4. Vyrobíme třídy ekvivalence určující, které stavy z \(Q\) jsou ekvivalentní pro řetězce délky \(i+1\): Platí, že dva stavy \(p\) a \(q\) jsou ekvivalentní pro řetězce délky \(i+1\), pokud jsou ekvivalentní pro řetězce délky \(i\) a pro každý symbol \(a \in \Sigma\) platí, že \(\delta(p,a) \sim_i \delta(q,a)\).
5. S výrobou tříd ekvivalence pokračujeme do té doby, dokud poprvé pro nějaké \(i\) nenastane, že \(\sim_{i+1}\) je stejná jako \(\sim_i\). Pak totiž už i pro všechna vyšší \(i\) musí být relace ekvivalence stejné. Jakmile toto nastane, pak každá třída ekvivalence (pro řetězce délky \(i+1\)), obsahuje vzájemně ekvivalentní stavy automatu \(M\).

2. Výsledné třídy ekvivalence prohlásíme za stavy automatu \(M^\prime\).

3. Třída ekvivalence obsahující počáteční stav automatu \(M\) bude počátečním stavem u \(M^\prime\).

4. Třída ekvivalence bude v množině koncových stavů automatu \(M^\prime\) právě tehdy, když obsahuje některý z koncových stavů automatu \(M\).

5. Přechodová funkce automatu \(M^\prime\) vznikne z přechodové funkce automatu \(M\) tak, že stavy \(q \in Q\) nahradíme odpovídající třídou ekvivalence, která tento stav obsahuje.

### Doplňující pole (Extra)

V tomto algoritmu se využívá pozorování, že stavy \(p, q \in Q\) jsou ekvivalentní, \(p \sim q \), právě tehdy, když \(p \sim_k q\) pro každé \(k \geq 0\). Přičemž \(p \sim_0 q\) je pravdivé, pokud vztah \(p \in F \iff q \in F\) je pravdivý. Vztah \(p \sim_{i+1} q\) je pravdivý, pokud \(p \sim_i q\) a zároveň \(\delta(p,a) \sim_i \delta(q,a)\) pro každý symbol \(a \in \Sigma\).

Algoritmus hledání ekvivalentních stavů na začátku předpokládá optimistický případ, že všechny koncové stavy jsou vzájemně ekvivalentní a všechny nekoncové stavy taktéž. Následně zkontroluje, zdali tento předpoklad byl pravdivý — vyrobí třídy ekvivalence pro řetězce o jedna delší. Pokud se rozklad ekvivalence pro řetězce této větší délky liší, pokračujeme a vyrobíme opět třídy ekvivalence pro řetězce o jedna delší. Takto pokračujeme, dokud se poprvé nestane, že dva následující rozklady ekvivalence jsou stejné.

## Poznámka Anki 1665134049441

Karty Anki: 1665134049442
GUID: QGB%h}>H^G; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665134049442: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadaný DKA, vrátí ekvivalentní **minimální DKA**.

### Odpověď (Back)

**Vstup:** DKA \(M\).

**Výstup:** Minimální DKA \(M_{\mathrm{min}}\) ekvivalentní automatu \(M\).

**Postup:**

1. Převedeme \(M\) na ekvivalentní DKA \(M_1\) bez nedosažitelných stavů.
2. Převedeme \(M_1\) na ekvivalentní DKA \(M_2\) bez zbytečných stavů.
3. V automatu \(M_2\) najdeme a sloučíme ekvivalentní stavy a výsledný automat označíme \(M_{\mathrm{min}}\).

### Doplňující pole (Extra)

U algoritmu lze prohodit kroky 1 a 2.

## Poznámka Anki 1665134185782

Karty Anki: 1665134185782
GUID: Lw/<]&nf:3; štítky: bi-aag::p03.

Metadata původního zdroje pro kartu 1665134185782: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **automatový izomorfismus**.

### Odpověď (Back)

Nechť \(M_1 = (Q_1, \Sigma, \delta_1, q_{01}, F_1)\) a \(M_2 = (Q_2, \Sigma, \delta_2, q_{02}, F_2)\) jsou konečné automaty. Zobrazení \(f: Q_1 \to Q_2\) je **automatový izomorfismus** \(M_1\) a \(M_2\), pokud

- \(f\) je bijekce,
- \(f(q_{01}) = q_{02}\),
- \(q \in F_1 \iff f(q) \in F_2\),
- \(f\left(\delta_1(q, a)\right)=\delta_2(f(q), a)\) pro všechna \(q \in Q_1\) a \(a \in \Sigma\).

### Doplňující pole (Extra)

Pokud mezi \(M_1\) a \(M_2\) existuje automatový izomorfismus, pak automaty \(M_1\) a \(M_2\) nazveme **izomorfní**.

## Poznámka Anki 1665134264987

Karty Anki: 1665134264987
GUID: NMmv<@.R;h; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665134264987: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak **algoritmicky** rozpoznat, že dva **konečné automaty** \(M_1\) a \(M_2\) jsou **ekvivalentní**?

### Odpověď (Back)

Využijeme skutečnosti, že pokud pro jazyk \(L\) lze sestrojit konečný automat, pak pro \(L\) existuje právě jeden unikátní minimální DKA (až na případné pojmenování stavů neboli až na automatový izomorfismus).

Uvažujme tedy dva konečné automaty \(M_1\) a \(M_2\) a předpokládejme, že se jedná o minimální DKA (pokud tomu tak není, umíme je na minimální DKA převést). Platí, že pokud jsou \(M_1\) a \(M_2\) izomorfní, pak jsou také ekvivalentní.

## Poznámka Anki 1665142955907

Karty Anki: 1665142955907
GUID: N!vS>[T.|w; štítky: bi-aag::p03 bi-spol::02.

Metadata původního zdroje pro kartu 1665142955907: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadaný **NKA**, vrátí ekvivalentní **DKA**.

### Odpověď (Back)

**Vstup:** NKA \(N = (Q_N, \Sigma, \delta_N, q_{0N}, F_N)\).

**Výstup:** DKA \(D = (Q_D, \Sigma, \delta_D, q_{0D}, F_D)\) takový, že \(L(N) = L(D)\).

**Postup:**

1. Automat \(D\) má stejnou abecedu vstupních symbolů jako automat \(N\).   
2. Počátečním stavem automatu \(D\) je jednoprvková podmnožina množiny \(Q_N\) obsahující pouze počáteční stav automatu \(N\). Tedy platí, že \(q_{0D} = \{ q_{0N} \}\).  
3. Množinu \(Q_D\) budeme budovat postupně. Nejprve přidáme pouze počáteční stav. Tedy nastavíme \(Q_D = \{ q_{0D} \}\).
4. Pro každý vstupní symbol \(a \in \Sigma\) najdeme podmnožinu \(S\) stavů z \(Q_N\), do kterých se z \(q_{0D}\) na tento symbol dostaneme. Pokud \(S \notin Q_D\), pak \(S\) přidáme do \(Q_D\) a tuto množinu označíme jako nezpracovanou. Zároveň nastavíme \(\delta_D(q_{0D},a)=S\).  
5. Postupně procházíme všechny nezpracované množiny \(S\) z \(Q_D\) a pro každý symbol \(a \in \Sigma\):   

1. Nastavíme \(\delta_D(S,a) = \bigcup\limits_{p \in S} \delta_N(p,a)\). 
2. Pokud je výsledkem \(\delta_D(S,a)\) množina, která ještě není v \(Q_D\), pak ji tam přidáme a označíme jako nezpracovanou. 
3. Aktuální množinu \(S\) označíme za zpracovanou.

6. Stav \(q \in Q_D\) je koncový právě tehdy, když \(q \cap F_N \neq \emptyset\). Množina \(F_D\) tedy obsahuje takové podmnožiny stavů z \(Q_N\), které obsahují alespoň jeden z koncových stavů vstupního NKA \(N\).

### Doplňující pole (Extra)

Tento algoritmus (také často nazývaný determinizace) je založen na principu podmnožinové kostrukce — konstruujeme všechny možné podmnožiny stavů, ve kterých se daný NKA může v jednu chvíli během svého výpočtu nacházet. Tyto podmnožiny následně prohlásíme za stavy ekvivalentního DKA. 

V nejhorším možném případě se může NKA během výpočtu postupně vyskytnout ve všech možných podmnožinách svých \(n\) stavů — příslušný DKA by tak měl \(2^n\) stavů. Odtud plyne časová složitost tohoto algoritmu, která je \(\mathcal{O}(2^n)\), kde \(n\) je počet stavů NKA.

## Poznámka Anki 1665142996690

Karty Anki: 1665142996690
GUID: pS]X2J(hN@; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665142996690: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **homogenní** NKA.

### Odpověď (Back)

Nechť \(M = (Q, \Sigma, \delta, q_0, F)\) je NKA. Pro \(a \in \Sigma\) definujeme \(Q(a) = \{q : q \in \delta(p,a) \wedge p,q \in Q\}\). Jestliže pro všechny dvojice různých symbolů \(a,b \in \Sigma\), platí \(Q(a) \cap Q(b) = \emptyset\), pak se automat \(M\) nazývá **homogenní**.

### Doplňující pole (Extra)

Množinu \(Q(a)\) nazýváme **množinou cílových stavů** pro symbol \(a\). Tuto množinu tvoří všechny stavy, do kterých se lze dostat přechodem na symbol \(a\). 

Pokud pro každý stav platí, že do něj vedoucí hrany jsou všechny ohodnoceny stejným symbolem, pak je automat homogenní. 

Pokud algoritmus determinizace dostane na vstupu homogenní NKA, pak je počet stavů výsledného DKA omezen následovně: \(|Q_D| \leq \sum_{a \in \Sigma} (2^{|Q_N(a)|}) - |\Sigma| + 1\), kde \(Q_D\) je množina stavů DKA a \(Q_N\) je množina stavů NKA.

## Poznámka Anki 1665143151322

Karty Anki: 1665143151322
GUID: C{GuZ%I(UA; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665143151322: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro dva konečné automaty \(M_1\) a \(M_2\), vrátí konečný automat \(M\) takový, že \(L(M) = L(M_1) \cdot L(M_2)\).

### Odpověď (Back)

**Vstup:** Konečný automat \(M_1 = (Q_1, \Sigma, \delta_1, q_1, F_1)\) a konečný automat \(M_2 = (Q_2, \Sigma, \delta_2, q_2, F_2)\), přičemž \(Q_1 \cap Q_2 = \emptyset\).

**Výstup:** NKA s \(\varepsilon\)-přechody \(M = (Q, \Sigma, \delta, q_1, F_2)\) takový, že \(L(M) = L(M_1) \cdot L(M_2)\).

**Postup:**

1. \(Q = Q_1 \cup Q_2\).
2. Všechny přechody v \(\delta_1\) a \(\delta_2\) jsou také součástí \(\delta\).
3. Počáteční stav automatu \(M\) odpovídá počátečnímu stavu automatu \(M_1\).
4. Pro všechny stavy \(q_F \in F_1\) přídáme přechody \(\delta(q_F, \varepsilon) = \{q_2\}\). Jinými slovy, ze všech stavů v \(M\), které odpovídají koncovým stavům v \(M_1\), vedeme \(\varepsilon\)-přechod do stavu, který odpovídá počátečnímu stavu automatu \(M_2\).
5. Množina koncových stavů automatu \(M\) odpovídá množině koncových stavů automatu \(M_2\).

## Poznámka Anki 1665143196782

Karty Anki: 1665143196782
GUID: bkr,H$fwgd; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665143196782: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro konečný automat \(M_1\), vrátí konečný automat \(M\) takový, že \(L(M) = (L(M_1))^*\).

### Odpověď (Back)

**Vstup:** Konečný automat \(M_1 = (Q_1, \Sigma, \delta_1, q_1, F_1)\).

**Výstup:** NKA s \(\varepsilon\)-přechody \(M = (Q, \Sigma, \delta, q_0, F)\) takový, že \(L(M) = (L(M_1))^*\).

**Postup:**

1. \(Q = Q_1 \cup \{q_0\}\), kde \(q_0 \notin Q_1\). 
2. Počátečním stavem automatu\(M\) je stav \(q_0\).
3. Všechny přechody z \(\delta_1\) budou také součástí \(\delta\).
4. Z počátečního stavu \(q_0\) automatu \(M\) vedeme \(\varepsilon\)-přechod do stavu, který odpovídá počátečnímu stavu automatu \(M_1\). Tedy nastavíme \(\delta(q_0, \varepsilon) = \{q_1\}\).
5. Pro každý stav \(q_F \in F_1\) přidáme přechod \(\delta(q_F, \varepsilon) = \{q_1\}\). Jinými slovy, ze všech stavů, které odpovídají koncovým stavům v \(M_1\), vedeme v \(M\) \(\varepsilon\)-přechod do stavu, který odpovídá počáteční stavu v \(M_1\).
6. \(F = F_1 \cup \{q_0\}\).

## Poznámka Anki 1665143284060

Karty Anki: 1665143284061
GUID: I{}~V40!j^; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665143284061: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadaný konečný automat \(M_1\), vrátí konečný automat \(M\) takový, že \(L(M) = \overline{L(M_1)}\).

### Odpověď (Back)

**Vstup:** Úplně určený DKA \(M_1 = (Q, \Sigma, \delta, q_0, F_1)\).

**Výstup:** Úplně určený DKA \(M = (Q, \Sigma, \delta, q_0, F)\) takový, že \(L(M) = \overline{L(M_1)}\).

**Postup:**

1. \(F = Q \setminus F_1\).

## Poznámka Anki 1665143400091

Karty Anki: 1665143400092
GUID: 1fM08Aqx0; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665143400092: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro konečné automaty \(M_1\) a \(M_2\), vrátí NKA s \(\varepsilon\)-přechody \(M\) takový, že \(L(M) = L(M_1) \cup L(M_2)\).

### Odpověď (Back)

**Vstup:** Konečný automat \(M_1 = (Q_1, \Sigma, \delta_1, q_1, F_1)\) a konečný automat \(M_2 = (Q_2, \Sigma, \delta_2, q_2, F_2)\), přičemž \(Q_1 \cap Q_2 = \emptyset\).

**Výstup:** NKA s \(\varepsilon\)-přechody \(M = (Q, \Sigma, \delta, q_0, F)\) takový, že \(L(M) = L(M_1) \cup L(M_2)\).

**Postup:**

1. \(Q = Q_1 \cup Q_2 \cup \{q_0\}\), kde \(q_0 \notin (Q_1 \cup Q_2)\). 
2. Počátečním stavem automatu \(M\) je stav \(q_0\).
3. Všechny přechody z \(\delta_1\) a \(\delta_2\) budou také součástí \(\delta\).
4. Z počátečního stavu \(q_0\) automatu \(M\) vedeme \(\varepsilon\)-přechody do stavů, které odpovídají počátečním stavům automatu \(M_1\) a \(M_2\). Tedy nastavíme \(\delta(q_0, \varepsilon) = \{q_1, q_2\}\).
5. \(F = F_1 \cup F_2\).

## Poznámka Anki 1665143420953

Karty Anki: 1665143420953
GUID: foFya($f@B; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665143420953: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro konečné automaty \(M_1\) a \(M_2\), vrátí NKA s více počátečními stavy \(M\) takový, že \(L(M) = L(M_1) \cup L(M_2)\).

### Odpověď (Back)

**Vstup:** Konečný automat \(M_1 = (Q_1, \Sigma, \delta_1, q_1, F_1)\) a konečný automat \(M_2 = (Q_2, \Sigma, \delta_2, q_2, F_2)\), přičemž \(Q_1 \cap Q_2 = \emptyset\).

**Výstup:** NKA s více počátečními stavy \(M = (Q, \Sigma, \delta, I, F)\) takový, že \(L(M) = L(M_1) \cup L(M_2)\).

**Postup:**

1. \(Q = Q_1 \cup Q_2\).
2. Všechny přechody z \(\delta_1\) a \(\delta_2\) jsou také součástí \(\delta\).
3. \(I = \{q_1, q_2\}\).
4. \(F = F_1 \cup F_2\).

## Poznámka Anki 1665143478710

Karty Anki: 1665143478710
GUID: z`}+<JaS+8; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665143478710: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus** založený na **paralelní činnosti**, který pro konečné automaty \(M_1\) a \(M_2\), vrátí konečný automat \(M\) takový, že \(L(M) = L(M_1) \cup L(M_2)\).

### Odpověď (Back)

**Vstup:** Úplně určený NKA nebo DKA \(M_1 = (Q_1, \Sigma, \delta_1, q_1, F_1)\) a úplně určený NKA nebo DKA \(M_2 = (Q_2, \Sigma, \delta_2, q_2, F_2)\), přičemž \(Q_1 \cap Q_2 = \emptyset\).

**Výstup:** Úplně určený KA \(M = (Q, \Sigma, \delta, q_0, F)\) takový, že \(L(M) = L(M_1) \cup L(M_2)\). Pokud \(M_1\) i \(M_2\) jsou DKA, pak \(M\) bude DKA, jinak \(M\) bude NKA.

Postup:

1. Stavy automatu \(M\) budou tvořit uspořádané dvojice stavů \(M_1\) a \(M_2\), tedy \(Q = Q_1 \times Q_2\). 
2. Pokud \(M_1\) i \(M_2\) jsou DKA, pak pro všechny stavy \((p_1, p_2) \in Q\) a symboly \(a \in \Sigma\) nastavíme \(\delta\big( (p_1, p_2), a \big) = \big( \delta_1(p_1, a), \delta_2(p_2, a) \big)\). Jinak pro všechny stavy \((p_1, p_2) \in Q\) a symboly \(a \in \Sigma\) nastavíme \(\delta\big( (p_1, p_2), a \big) = \{ (r_1, r_2) : r_1 \in \delta_1(p_1, a) \wedge r_2 \in \delta_2(p_2, a) \}\).
3. Počáteční stav automatu \(M\) tvoří dvojice složená z počátečních stavů \(M_1\) a \(M_2\). Tedy platí, že \(q_0 = (q_1, q_2)\).
4. Koncové stavy automatu \(M\) jsou dvojice, ve kterých je alespoň jeden koncový stav z \(M_1\) nebo \(M_2\). Tedy platí, že \(F = (F_1 \times Q_2) \cup (Q_1 \times F_2)\).

### Doplňující pole (Extra)

Tento algoritmus může vyrobit i nedosažitelné stavy. Je možné jej však upravit a budovat pouze stavy dosažitelné, počínaje stavem \((q_1, q_2)\).

## Poznámka Anki 1665143511162

Karty Anki: 1665143511162
GUID: JD/H6Q=aZ<; štítky: bi-aag::p03 bi-spol::01.

Metadata původního zdroje pro kartu 1665143511162: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro konečné automaty \(M_1\) a \(M_2\), vrátí konečný automat \(M\) takový, že \(L(M) = L(M_1) \cap L(M_2)\).

### Odpověď (Back)

**Vstup:** NKA nebo DKA \(M_1 = (Q_1, \Sigma, \delta_1, q_1, F_1)\) a NKA nebo DKA \(M_2 = (Q_2, \Sigma, \delta_2, q_2, F_2)\), přičemž \(Q_1 \cap Q_2 = \emptyset\).

**Výstup:** KA \(M = (Q, \Sigma, \delta, q_0, F)\) takový, že \(L(M) = L(M_1) \cap L(M_2)\). Pokud \(M_1\) i \(M_2\) jsou DKA, pak \(M\) bude DKA, jinak \(M\) bude NKA.
**
Postup:**

1. Stavy automatu \(M\) budou tvořit uspořádané dvojice stavů \(M_1\) a \(M_2\), tedy \(Q = Q_1 \times Q_2\).

2. Pokud \(M_1\) i \(M_2\) jsou DKA, pak pro všechny stavy \((p_1, p_2) \in Q\) a symboly \(a \in \Sigma\) nastavíme \(\delta\big( (p_1, p_2), a \big) = \big( \delta_1(p_1, a), \delta_2(p_2, a) \big)\). Pokud ovšem výsledek \(\delta_1(p_1,a)\) nebo \(\delta_2(p_2,a)\) není definován, poté nebude definován ani přechod \(\delta\big( (p_1, p_2), a \big)\).
3. Pokud \(M_1\) nebo \(M_2\) není deterministický KA, pak pro všechny stavy \((p_1, p_2) \in Q\) a symboly \(a \in \Sigma\) nastavíme \(\delta\big( (p_1, p_2), a \big) = \{ (r_1, r_2) : r_1 \in \delta_1(p_1, a) \wedge r_2 \in \delta_2(p_2, a) \}\). Pokud ovšem výsledek \(\delta_1(p_1,a)\) nebo \(\delta_2(p_2,a)\) není definován nebo je výsledkem prázdná množina stavů, poté nebude definován ani přechod \(\delta\big( (p_1, p_2), a \big)\).
4. Počáteční stav automatu \(M\) tvoří dvojice složená z počátečních stavů \(M_1\) a \(M_2\). Tedy platí, že \(q_0 = (q_1, q_2)\).
5. Koncové stavy automatu \(M\) jsou dvojice, ve kterých jsou oba koncové z \(M_1\) a \(M_2\). Tedy platí, že \(F = F_1 \times F_2\).

### Doplňující pole (Extra)

Pro paralelní činnost za účelem sestrojení KA pro průnik vstupní automaty nemusí být úplně určené.

Tento algoritmus může vyrobit i nedosažitelné stavy. Je možné jej však upravit a budovat pouze stavy dosažitelné, počínaje stavem \((q_1, q_2)\).

