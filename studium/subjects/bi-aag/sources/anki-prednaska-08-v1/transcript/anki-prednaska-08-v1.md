# BI-AAG – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aag/BI-AAG.apkg; APKG SHA-256 0383847389324f3b83b349363b7ad16a6bf91673c90b7a96ed1a57b25a85f8af. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b9cda20d5a5a9d1ff47d4e1fc58b10ed3ac7a37c72c6c1431cc7cb67e2ca10c.
Původní balíčky: BI-AAG
Rozsah: 19 poznámek, 19 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1669379556828

Karty Anki: 1669379556830
GUID: Oy0N`DdcRB; štítky: bi-aag::p08 bi-spol::02.

### Otázka (Front)

Definujte **zásobníkový automat**.

### Odpověď (Back)

**Zásobníkový automat** definujeme jako uspořádanou sedmici
\(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\), kde

- \(Q\) je konečná neprázdná množina stavů,
- \(\Sigma\) je konečná vstupní abeceda,
- \(G\) je konečná neprázdná abeceda zásobníku,
- \(\delta : Q \times (\Sigma \cup \{\varepsilon\}) \times G^* \to \mathcal{P}(Q \times G^*)\), kde \(\mathcal{P}(Q \times G^*)\) zde reprezentuje množinu všech konečných podmnožin množiny \(Q \times G^*\), je přechodová funkce,
- \(q_0 \in Q\) je počáteční stav,
- \(Z_0 \in G\) je počáteční symbol na zásobníku,
- \(F \subseteq Q\) je množina koncových stavů.

### Doplňující pole (Extra)

Zásobníkový automat (ZA) si můžeme intuitivně představit jako konečný automat se zásobníkem. Konečný automat si informace pamatuje pouze za pomoci stavů (těch může být jen konečný počet), zatímco zásobníkový automat může k ukládání informací využít jak stavy, tak zásobník. 

Oproti definici konečného automatu nám přibyla abeceda zásobníku a počáteční symbol na zásobníku. Zásobníkový automat tedy pracuje se dvěma abecedami. Vstupní abeceda \(\Sigma\) obsahuje všechny symboly, které se mohou vyskytnout v řetězcích na vstupu (stejně jako u konečného automatu). Zásobníková abeceda \(G\) obsahuje všechny symboly, které se mohou v průběhu výpočtu objevit na zásobníku. Na počátku výpočtu není zásobník prázdný, ale je na něm symbol \(Z_0\).  

Definice přechodové funkce \(\delta\) nám říká, že se na základě aktuálního stavu, symbolu na vstupu (případně v rámci \(\varepsilon\)-přechodu symbol na vstupu neřešíme a nečteme nic) a řetězce na vrcholu zásobníku rozhodneme, do kterých stavů půjdeme a jaký řetězec zapíšeme na vrchol zásobníku. Po provedení přechodu se stejně jako u konečného automatu čtecí hlava posune o jednu pozici vpravo na následující symbol (pokud se nejednalo o \(\varepsilon\)-přechod). Z vrcholu zásobníku odstraníme čtený řetězec a následně vložíme nový řetězec.

## Poznámka Anki 1669379583154

Karty Anki: 1669379583155
GUID: l2Or8gJtq+; štítky: bi-aag::p08 bi-spol::02.

### Otázka (Front)

Definujte **konfiguraci zásobníkového automatu**.

### Odpověď (Back)

Nechť \(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\) je zásobníkový automat. **Konfigurace zásobníkového automatu** \(R\) je trojice \((q, w, \alpha) \in Q \times \Sigma^* \times G^*\).

### Doplňující pole (Extra)

Podobně jako u konečného automatu, konfiguraci ZA získáme, když během výpočtu automatu provedeme „snapshot“ — tj. zastavíme výpočet a podíváme se, v jakém stavu \(q\) se automat nachází, jaká nepřečtená část řetězce \(w\) mu ještě zbývá na vstupu a jaký řetězec \(\alpha\) má na zásobníku (tedy celý obsah zásobníku). Konfiguraci ZA budeme  používat k tomu, abychom mohli popsat průběh zpracování vstupního řetězce.

## Poznámka Anki 1669379604951

Karty Anki: 1669379604951
GUID: FW=2-mt<w}; štítky: bi-aag::p08 bi-spol::02.

### Otázka (Front)

Definujte **počáteční konfiguraci zásobníkového automatu**.

### Odpověď (Back)

Uvažujme zásobníkový automat \(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\) a vstupní řetězec \(w \in \Sigma^*\). Pak konfigurace \((q_0, w, Z_0)\) je **počáteční konfigurace** zásobníkového automatu \(R\).

## Poznámka Anki 1669379628493

Karty Anki: 1669379628493
GUID: eGnsTLBRVp; štítky: bi-aag::p08 bi-spol::02.

### Otázka (Front)

Definujte **přechod v zásobníkovém automatu**.

### Odpověď (Back)

Mějme ZA \(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\). **Přechodem** v zásobníkovém automatu \(R\) nazveme prvek relace \(\vdash_R\) nad \((Q \times \Sigma^* \times G^*) \times (Q \times \Sigma^* \times G^*)\) s touto vlastností: \((p, aw, \beta \gamma) \vdash_R (q, w, \alpha \gamma) \iff (q, \alpha) \in \delta(p, a, \beta)\), kde \(a \in \Sigma\cup\{\varepsilon\} \land w \in \Sigma^* \land \alpha, \beta, \gamma \in G^*\) (vrchol zásobníku uvažujeme vlevo).

### Doplňující pole (Extra)

\(k\)-tá mocnina relace \(\vdash_R\), její tranzitivní i tranzitivní a reflexivní uzávěr jsou definovány obdobně jako v případě přechodu konečného automatu.

## Poznámka Anki 1669379667928

Karty Anki: 1669379667929
GUID: jMEI~30mz+; štítky: bi-aag::p08 bi-spol::02.

### Otázka (Front)

Kdy zásobníkový automat **přijme** řetězec **přechodem do koncového stavu**?

### Odpověď (Back)

Mějme ZA \(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\). Řekneme, že řetězec \(w\) je přijímaný automatem \(R\) **přechodem do koncového stavu** právě tehdy, když
\(\exists (q_0, w, Z_0) \vdash^* (q, \varepsilon, \alpha) \text{ kde } q \in F \land \alpha \in G^*\).

### Doplňující pole (Extra)

Řetězec \(w\) je tedy přijímaný ZA \(R\) přechodem do koncového stavu, existuje-li posloupnost přechodů, která z počáteční konfigurace \((q_0, w, Z_0)\) vede do  konfigurace \((q, \varepsilon, \alpha)\), kde \(q\) je koncový stav (na obsahu zásobníku nezáleží).

## Poznámka Anki 1669379702101

Karty Anki: 1669379702102
GUID: z$$/E}/s]y; štítky: bi-aag::p08 bi-spol::02.

### Otázka (Front)

Kdy zásobníkový automat **přijme** řetězec **prázdným zásobníkem**?

### Odpověď (Back)

Mějme ZA \(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\). Řekneme, že řetězec \(w\) je přijímaný automatem \(R\) **prázdným zásobníkem** právě tehdy, když
\(\exists (q_0, w, Z_0) \vdash^* (q, \varepsilon, \varepsilon) \text{ kde } q \in Q\).

### Doplňující pole (Extra)

Řetězec \(w\) je tedy přijímaný ZA \(R\) prázdným zásobníkem, pokud existuje posloupnost přechodů taková, která z počáteční konfigurace \((q_0, w, Z_0)\) vede do  konfigurace \((q, \varepsilon, \varepsilon)\), kde \(q\) je libovolný stav a zásobník je prázdný (neobsahuje ani \(Z_0\)).

Konvence: U ZA přijímajícího řetězce prázdným zásobníkem budeme množinu koncových stavů definovat jako prázdnou.

## Poznámka Anki 1669379769356

Karty Anki: 1669379769356
GUID: v=]+P`.oy-; štítky: bi-aag::p08 bi-spol::02.

### Otázka (Front)

Definujte **jazyk definovaný zásobníkovým automatem přechodem do koncového stavu**.

### Odpověď (Back)

Mějme zásobníkový automat \(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\). Jazyk definovaný automatem \(R\) metodou přijímání přechodem do koncového stavu (zapisujeme jako \(L(R)\)) definujeme takto: \(L(R) = \{w : w \in \Sigma^* \wedge \exists q \in F, \alpha \in G^*: (q_0, w, Z_0) \vdash^* (q, \varepsilon, \alpha)\}\).

## Poznámka Anki 1669379794163

Karty Anki: 1669379794163
GUID: Lv&&cD~i%i; štítky: bi-aag::p08 bi-spol::02.

### Otázka (Front)

Definujte **jazyk přijímaný zásobníkovým automatem prázdným zásobníkem**.

### Odpověď (Back)

Mějme zásobníkový automatu \(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\). Jazyk definovaný automatem \(R\) metodou přijímání prázdným zásobníkem (zapisujeme jako \(L_\varepsilon(R)\)) definujeme takto: \(L_\varepsilon(R) = \{w : w \in \Sigma^* \wedge \exists q \in Q : (q_0, w, Z_0) \vdash^* (q, \varepsilon, \varepsilon)\}\).

## Poznámka Anki 1669379851531

Karty Anki: 1669379851531
GUID: f%WCSK_0c@; štítky: bi-aag::p08.

Metadata původního zdroje pro kartu 1669379851531: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus, který pro zásobníkový automat \(R_f\) přijímající přechodem do koncového stavu vrátí zásobníkový automat \(R_\varepsilon\) přijímající prázdným zásobníkem tak, že \(L_\varepsilon(R_\varepsilon) = L(R_f)\).

### Odpověď (Back)

**Vstup:** Zásobníkový automat \(R_f = (Q_f, \Sigma, G_f, \delta_f, q_f, Z_f, F_f)\).

**Výstup:** Zásobníkový automat \(R_\varepsilon = (Q, \Sigma, G, \delta, q_0, Z_0, F)\), kde \(Z_0 \notin G_f\), takový, že \(L_\varepsilon = L(R)\).

**Postup:**

1. \(Q = Q_f \cup \{q_0, q_\varepsilon\}\), kde \(q_0, q_\varepsilon \notin Q_f\).
2. \(G = G_f \cup\{Z_0\}\).
3. Zobrazení \(\delta\) bude obsahovat všechny přechody \(\delta_f\). Navíc přidáme následující přechody:

1. \(\delta(q_0, \varepsilon, Z_0) = \{(q_f, Z_f Z_0)\}\),
2. \(\forall q \in F : \delta(q, \varepsilon, \varepsilon) = \delta_f(q, \varepsilon, \varepsilon) \cup \{(q_\varepsilon, \varepsilon)\}\),
3. \(\forall \alpha \in G : \delta(q_\varepsilon, \varepsilon, \alpha) = \{(q_\varepsilon, \varepsilon)\}\). 

4. \(F = \emptyset\).

### Doplňující pole (Extra)

Ilustrace algoritmu: Černě jsou označené stavy pocházející z automatu \(R_f\), kde \(q_f\) je v \(R_f\) počátečním stavem. Předpokládejme dále, že \(q_2, q_3\) jsou jediné koncové stavy automatu \(R_f\). Pak \(R_\varepsilon\) bude navíc obsahovat červené stavy a přechody (vrchol zásobníku uvažujeme vlevo).

 [Obrázek: paste-83399c618ce38e86cd9b6215c1b710bc6bbe4705.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1669379876034

Karty Anki: 1669379876034
GUID: dB$u]:`lSj; štítky: bi-aag::p08.

Metadata původního zdroje pro kartu 1669379876034: původní příznak autora 7; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus, který pro zásobníkový automat \(R_\varepsilon\) přijímající prázdným zásobníkem vrátí zásobníkový automat \(R_f\) přijímající přechodem do koncového stavu tak, že \(L(R_f) = L_\varepsilon(R_\varepsilon)\).

### Odpověď (Back)

**Vstup:** Zásobníkový automat \(R_\varepsilon = (Q_\varepsilon, \Sigma, G_\varepsilon, \delta_\varepsilon, q_\varepsilon, Z_\varepsilon, F_\varepsilon)\).

**Výstup:** Zásobníkový automat \(R_f = (Q, \Sigma, G, \delta, q_0, Z_0, F)\), kde \(Z_0 \notin G_\varepsilon\), takový, že \(L(R_f) = L_\varepsilon(R_\varepsilon)\).

**Postup:**

1. \(Q = Q_\varepsilon \cup \{q_0, q_f\}\), kde \(q_0, q_f \notin Q_\varepsilon\). 
2. \(G = G_\varepsilon \cup\{Z_0\}\).
3. Zobrazení \(\delta\) bude obsahovat všechny přechody \(\delta_\varepsilon\). Navíc přidáme následující přechody:

1. \(\delta(q_0, \varepsilon, Z_0) = \{(q_\varepsilon, Z_\varepsilon Z_0)\}\),
2. \(\forall q \in Q_\varepsilon : \delta(q, \varepsilon, Z_0) = \{(q_f, \varepsilon)\}\).     

4. \(F = \{ q_f \}\).

### Doplňující pole (Extra)

Ilustrace algoritmu: Černě jsou označené stavy pocházející z automatu \(R_\varepsilon\), kde \(q_\varepsilon\) je v \(R_\varepsilon\) počátečním stavem. Pak \(R_f\) bude navíc obsahovat červené stavy a přechody (vrchol zásobníku uvažujeme vlevo).

 [Obrázek: paste-6c9963ddc03de1b8e6fc08af46ee018e1715471c.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1669380102451

Karty Anki: 1669380102452
GUID: K_[O4iEz}k; štítky: bi-aag::p08 bi-spol::02.

Metadata původního zdroje pro kartu 1669380102452: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus pro metodu **shora dolů**, která pro bezkontextovou gramatiku \(G\) vrátí zásobníkový automat \(R\) takový, že \(L_\varepsilon(R) = L(G)\).

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Zásobníkový automat \(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\) s vrcholem zásobníku **vlevo** takový, že \(L_\varepsilon(R) = L(G)\).

**Postup:**

1. \(Q = \{ q_0 \}\).
2. \(G = N \cup \Sigma\).
3. (srovnání) \(\forall a \in \Sigma : \delta(q_0, a, a) = \{ (q_0, \varepsilon) \}\).
4. (expanze) \(\forall (A \to \alpha) \in P\), kde \(\alpha \in (N \cup \Sigma)^*\), přidáme přechod \(\delta(q_0, \varepsilon, A) = \{ (q_0, \alpha) \}\).
5. \(Z_0 = S\) (tj. počáteční zásobníkový symbol odpovídá počátečnímu neterminálu).
6. \(F = \emptyset\).

### Doplňující pole (Extra)

[Obrázek: paste-4cee369a694056329c3525bf297f263534fac257.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1669380127131

Karty Anki: 1669380127131
GUID: qMfP:ZQnEF; štítky: bi-aag::p08 bi-spol::02.

Metadata původního zdroje pro kartu 1669380127131: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus pro metodu **zdola nahoru**, která pro bezkontextovou gramatiku \(G\) vrátí zásobníkový automat \(R\) takový, že \(L(G) = L(R)\).

### Odpověď (Back)

**Vstup:** Bezkontextová gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Zásobníkový automat \(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\) s vrcholem zásobníku **vpravo** takový, že \(L(R) = L(G)\).

**Postup:**

1. \(Q = \{ q_0, q_f \}\).
2. \(G = N \cup \Sigma \cup \{Z_0\}\).
3. (přesun) \(\forall a \in \Sigma : \delta(q_0, a, \varepsilon) = \{ (q_0, a) \}\).
4. (redukce) \(\forall (A \to \alpha) \in P\), kde \(\alpha \in (N \cup \Sigma)^*\), přidáme přechod \(\delta(q_0, \varepsilon, \alpha) = \{ (q_0, A) \}\).
5. (přijetí) \(\delta(q_0, \varepsilon, Z_0S) = \{(q_f, \varepsilon)\}\)
6. \(F = \{q_f\}\).

### Doplňující pole (Extra)

[Obrázek: paste-3a8fea0afdcf074a74d5cf0128f58a381a7f8ebf.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1669380156742

Karty Anki: 1669380156742
GUID: y_f|drk;er; štítky: bi-aag::p08 bi-spol::02.

Metadata původního zdroje pro kartu 1669380156742: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **levou derivaci**.

### Odpověď (Back)

Mějme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\). Derivaci \(S \Rightarrow^* \alpha\), kde \(\alpha \in (N \cup \Sigma)^*\), nazveme **levou derivací** právě tehdy, když v každém kroku byl vždy nahrazován neterminál, který byl v dané větné formě nejvíce vlevo.

## Poznámka Anki 1669380167516

Karty Anki: 1669380167516
GUID: NBn319-Y;+; štítky: bi-aag::p08 bi-spol::02.

Metadata původního zdroje pro kartu 1669380167516: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **pravou derivaci**.

### Odpověď (Back)

Mějme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\). Derivaci \(S \Rightarrow^* \alpha\), kde \(\alpha \in (N \cup \Sigma)^*\), nazveme **pravou derivací** právě tehdy, když v každém kroku byl vždy nahrazován neterminál, který byl v dané větné formě nejvíce vpravo.

## Poznámka Anki 1669380187218

Karty Anki: 1669380187218
GUID: iZ)+l2gp:0; štítky: bi-aag::p08 bi-spol::02.

Metadata původního zdroje pro kartu 1669380187218: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **rozklad** větné formy.

### Odpověď (Back)

Mějme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\), kde jsou jednotlivým pravidlům přiřazená čísla \(1, 2, \dots, |P|\). **Rozkladem** větné formy \(\alpha\) v \(G\) nazveme posloupnost čísel pravidel použitých v derivaci \(S \Rightarrow^* \alpha\).

## Poznámka Anki 1669380199597

Karty Anki: 1669380199597
GUID: m0{(Q9ECmk; štítky: bi-aag::p08 bi-spol::02.

Metadata původního zdroje pro kartu 1669380199597: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **levý rozklad** větné formy.

### Odpověď (Back)

Mějme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\), kde jsou jednotlivým pravidlům přiřazená čísla \(1, 2, \dots, |P|\). **Levým rozkladem** větné formy \(\alpha\) v \(G\) nazveme posloupnost čísel pravidel použitých v levé derivaci \(S \Rightarrow^* \alpha\).

## Poznámka Anki 1669380211733

Karty Anki: 1669380211733
GUID: lLy5[,Wr}a; štítky: bi-aag::p08 bi-spol::02.

Metadata původního zdroje pro kartu 1669380211733: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **pravý rozklad** větné formy.

### Odpověď (Back)

Mějme bezkontextovou gramatiku \(G = (N, \Sigma, P, S)\), kde jsou jednotlivým pravidlům přiřazená čísla \(1, 2, \dots, |P|\). **Pravým rozkladem** větné formy \(\alpha\) v \(G\) nazveme **obrácenou** posloupnost čísel pravidel použitých v pravé derivaci \(S \Rightarrow^* \alpha\).

## Poznámka Anki 1669380275279

Karty Anki: 1669380275279
GUID: Ls>:xVYRoO; štítky: bi-aag::p08 bi-spol::02.

Metadata původního zdroje pro kartu 1669380275279: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **deterministický zásobníkový automat**.

### Odpověď (Back)

Zásobníkový automat \(R = (Q, \Sigma, G, \delta, q_0, Z_0, F)\) je **deterministický**, jestliže \(\forall q\in Q \land \forall a \in \Sigma\cup\{\varepsilon\} \land \forall \alpha, \beta \in G^*\):

- \(|\delta(q, a, \alpha)| \leq 1\) a současně 
- jestliže \(\delta(q, a, \alpha) \neq \emptyset \land \delta(q, a, \beta) \neq \emptyset\) a \(\alpha \neq \beta\), pak \(\alpha\) není předponou \(\beta\) (ani opačně) a současně
- jestliže \(\delta(q, a, \alpha) \neq \emptyset \land \delta(q, \varepsilon, \beta) \neq \emptyset\), pak \(\alpha\) není předponou \(\beta\) (ani opačně).

### Doplňující pole (Extra)

První podmínka v definici nám říká, že pro každou kombinaci čteného symbolu vstupu i řetězce na vrcholu zásobníku má každý stav nejvýše jeden odchozí přechod. Druhá podmínka popisuje případ, kdy přechody nevyžadují stejný řetězec na vrcholu zásobníku, ale přesto bychom si mezi nimi mohli vybrat, pokud by jeden byl předponou druhého — například pokud by na vrcholu zásobníku byla \(\beta\) a \(\alpha\) by byla předponou \(\beta\), pak lze použít oba odchozí přechody. Třetí podmínka je obdobná té druhé, akorát popisuje situaci s \(\varepsilon\)-přechody. Platí tedy, že deterministický zásobníkový automat (DZA) má pro každý stav, symbol na vstupu a řetězec na zásobníku jasně dáno, jak pokračovat (nemůže si vybrat z více možností).

## Poznámka Anki 1717622139484

Karty Anki: 1717622139485
GUID: CyNnTZWgqY; štítky: bi-aag::p08 bi-spol::02.

### Otázka (Front)

Popište syntaktickou analýzu.

### Odpověď (Back)

Syntaktická analýza je proces, který pro bezkontextovou gramatiku \(G\) a řetězec \(w \in \Sigma^*\) určí, zdali \(w \in L(G)\). Probíhá tak, že gramatiku \(G\) převedeme na zásobníkový automat \(R\), pak platí, že \(R\) přijímá \(w\), právě když \(w \in L(G)\). Během výpočtu \(R\) si budeme zaznamenávat, které expanze či redukce automat použil a tím získáme syntaktickou strukturu řetězce \(w\) v gramatice \(G\).

