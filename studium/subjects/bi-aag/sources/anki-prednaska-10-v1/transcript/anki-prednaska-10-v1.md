# BI-AAG – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aag/BI-AAG.apkg; APKG SHA-256 0383847389324f3b83b349363b7ad16a6bf91673c90b7a96ed1a57b25a85f8af. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b9cda20d5a5a9d1ff47d4e1fc58b10ed3ac7a37c72c6c1431cc7cb67e2ca10c.
Původní balíčky: BI-AAG
Rozsah: 20 poznámek, 20 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1670952307017

Karty Anki: 1670952307017
GUID: E{cJymNuDW; štítky: bi-aag::p10 ni-spol::11.

### Otázka (Front)

Definujte **deterministický Turingův stroj**.

### Odpověď (Back)

**Deterministický Turingův stroj** (DTS) definujeme jako uspořádanou sedmici
\(R = (Q, \Sigma, G, \delta, q_0, \mathtt{B}, F)\), kde

- \(Q\) je konečná neprázdná množina stavů,
- \(\Sigma\) je konečná vstupní abeceda,
- \(G\) je konečná neprázdná pracovní abeceda taková, že \(\Sigma \subsetneq G\)
- \(\delta : (Q \setminus F) \times G \to Q \times G \times \{-1,0,1\}\) je přechodová funkce,
- \(q_0 \in Q\) je počáteční stav,
- \(\mathtt{B} \in (G \setminus \Sigma)\) je **prázdný/blank symbol**,
- \(F \subseteq Q\) je množina koncových stavů.

### Doplňující pole (Extra)

Na začátku výpočtu se Turingův stroj nachází v počátečním stavu \(q_0\), na pásce je zapsán vstupní řetězec \(w\) a ostatní buňky jsou vyplněny symbolem \(\mathtt{B}\) a čtecí hlava ukazuje na buňku obsahující první symbol vstupního řetězce \(w\). Pokud \(w = \varepsilon\), pak je celá páska vyplněna symboly \(\mathtt{B}\) a čtecí hlava ukazuje na jeden z nich.

Definice přechodové funkce \(\delta\) nám říká, že DTS má vždy jasně dáno, jak ve výpočtu pokračovat (nemůže si vybrat z více možností). Rozhodnutí probíhá na základě aktuálního stavu a aktuálně čteného symbolu, na základě čehož DTS přejde do dalšího stavu, aktuálně čtený symbol přepíše nějakým symbolem z pracovní abecedy a čtecí hlavu posune vlevo (-1), vpravo (1), nebo neposune vůbec (0). Všimněte si, že dle definice může DTS mít přechody pouze z nekoncových stavů.

Obdobně jako u DKA i zde zobrazení \(\delta\) nemusí být definováno pro všechny dvojice stavů \(q \in (Q \setminus F)\) a symbolů z pracovní abecedy \(a \in G\). Deterministický Turingův stroj, jenž má zobrazení \(\delta\) definováno pro všechny dvojice stavů \(q \in (Q \setminus F)\) a symbolů z pracovní abecedy \(a \in G\), nazveme **úplně určeným DTS**.

## Poznámka Anki 1670952346142

Karty Anki: 1670952346142
GUID: I+O64km~b[; štítky: bi-aag::p10.

Metadata původního zdroje pro kartu 1670952346142: v původním balíčku pozastavená karta.

### Otázka (Front)

Kdy dva **Turingovy stroje** nazveme **ekvivalentní**?

### Odpověď (Back)

Turingovy stroje \(R_1\) a \(R_2\) nazýváme ekvivalentní, jestliže přijímají stejný jazyk, tj. \(L(R_1) = L(R_2)\).

## Poznámka Anki 1670952384848

Karty Anki: 1670952384848
GUID: Qbw|[UL@w}; štítky: bi-aag::p10.

### Otázka (Front)

Definujte **konfiguraci Turingova stroje**.

### Odpověď (Back)

Konfigurace Turingova stroje \(R = (Q, \Sigma, G, \delta, q_0, \mathtt{B}, F)\) je trojice \((\alpha, q, \beta) \in G^* \times Q \times G^*\), kde \(q\) je aktuální stav, \(\alpha\) je řetězec od pozice hlavy vlevo (včetně symbolu, který vidí hlava) a \(\beta\) je řetězec od čtecí hlavy vpravo. Poslední symbol \(\alpha\) obsahuje symbol, na který aktuálně ukazuje čtecí hlava. Řetězce \(\alpha\) a \(\beta\) neobsahují krajní prázdné symboly \(\mathtt{B}\). Pokud hlava ukazuje na symbol \(a \in G\), kde vlevo od něj jsou již pouze symboly \(\mathtt{B}\), pak \(\alpha = a\). Pokud hlava ukazuje na symbol \(b \in G\), kde vpravo od něj jsou již pouze symboly \(\mathtt{B}\), pak \(\beta = \varepsilon\).

### Doplňující pole (Extra)

Z definice konfigurace vyplývá, že pokud je Turingův stroj ve stavu \(q\) a celá páska je vyplněna pouze prázdnými symboly \(\mathtt{B}\), pak konfiguraci zapíšeme jako \((\mathtt{B}, q, \varepsilon)\). Pokud je páska vyplněná pouze prázdnými symboly, budeme říkat, že je páska prázdná.

## Poznámka Anki 1670952405132

Karty Anki: 1670952405132
GUID: LqO@h2kMCY; štítky: bi-aag::p10.

### Otázka (Front)

Definujte **počáteční konfiguraci Turingova stroje**.

### Odpověď (Back)

Uvažujme Turingův stroj \(R = (Q, \Sigma, G, \delta, q_0, \mathtt{B}, F)\) a vstupní řetězec \(w \in \Sigma^*\). **Počáteční konfiguraci** TS \(R\) definujeme jako

- \((a, q_0, u)\), pokud \(w = au \wedge a \in \Sigma \wedge u \in \Sigma^*\),
- \((\mathtt{B}, q_0, \varepsilon)\), pokud \(w = \varepsilon\).

## Poznámka Anki 1670952424016

Karty Anki: 1670952424016
GUID: s)kL,whg[T; štítky: bi-aag::p10.

### Otázka (Front)

Definujte **přijímací konfiguraci Turingova stroje**.

### Odpověď (Back)

Uvažujme Turingův stroj \(R = (Q, \Sigma, G, \delta, q_0, \mathtt{B}, F)\), pak konfiguraci \((\mathtt{B}, q, \varepsilon)\), kde \(q\in F\), nazveme přijímající konfigurací.

### Doplňující pole (Extra)

Přijímající konfigurace TS je tedy taková konfigurace, kdy se Turingův stroj nachází v některém z koncových stavů a zároveň páska je prázdná.

## Poznámka Anki 1670952505134

Karty Anki: 1670952505134
GUID: l88*@l7!!n; štítky: bi-aag::p10.

### Otázka (Front)

Definujte **řetězec přijímaný deterministickým Turingovým strojem**.

### Odpověď (Back)

Uvažujme DTS \(R = (Q, \Sigma, G, \delta, q_0, \mathtt{B}, F)\). Řekneme, že řetězec \(w = a\alpha\), kde \(a \in \Sigma, \alpha \in \Sigma^*\), je **přijímaný** \(R\) právě tehdy, když \(\exists (a, q_0, \alpha) \vdash^* (\mathtt{B}, q, \varepsilon)\), kde \(q \in F\). Prázdný řetězec je přijímaný \(R\) právě tehdy, když \(\exists (\mathtt{B}, q_0, \varepsilon) \vdash^* (\mathtt{B}, q, \varepsilon)\) kde \(q \in F\).

### Doplňující pole (Extra)

Řetězec je tedy přijímaný deterministických Turingovým strojem, existuje-li pro něj posloupnost přechodů taková, že daný DTS dojde do koncového stavu a má prázdnou pásku. Ve všech ostatních případech DTS řetězec nepřijme. DTS tedy nepřijme řetězec, pokud nastane jedna z následujících situací:

- Turingův stroj přejde do koncového stavu, ale páska není po ukončení výpočtu prázdná (tj. existuje buňka pásky, která není vyplněna symbolem \(\mathtt{B}\)).
- Během výpočtu se dostaneme do konfigurace, ze které již nelze dále pokračovat, neboť pro aktuální nekoncový stav a aktuální symbol, není definován přechod. Takové situaci často říkáme, že Turingův stroj skončí výpočet s chybou. (Poznámka: pokud je DTS zároveň úplně určený, pak tato situace nikdy nenastane.)
- Výpočet pro daný řetězec na vstupu neskončí. Této situaci říkáme, že se DTS zacyklí.

## Poznámka Anki 1670952527013

Karty Anki: 1670952527013
GUID: gCGd|e58YP; štítky: bi-aag::p10.

### Otázka (Front)

Definujte **jazyk přijímaný deterministickým Turingovým strojem**.

### Odpověď (Back)

Uvažujme DTS \(R = (Q, \Sigma, G, \delta, q_0, \mathtt{B}, F)\). Jazyk \(L\) přijímaný strojem \(R\), značíme \(L(R)\), jsou všechny řetězce nad abecedou \(\Sigma\), které \(R\) přijímá.

## Poznámka Anki 1670952559405

Karty Anki: 1670952559405
GUID: HSRWm1!0{{; štítky: bi-aag::p10 ni-spol::11.

### Otázka (Front)

Definujte **nedeterministický Turingův stroj**.

### Odpověď (Back)

**Nedeterministický Turingův stroj** (NTS) definujeme jako uspořádanou sedmici \(R = (Q, \Sigma, G, \delta, q_0, \mathtt{B}, F)\), kde

- \(Q, \Sigma, G, q_0, \mathtt{B}, F\) jsou definovány stejně jako u DTS,
- přechodová funkce je definována jako \(\delta : (Q \setminus F) \times G \to \mathcal{P}(Q \times G \times \{-1,0,1\})\).

### Doplňující pole (Extra)

Výsledkem přechodové funkce \(\delta\) u NTS je tedy množina trojic \((p,a,d)\), kde \(p \in Q, a \in G, d \in \{-1,0,1\}\). Tato množina může být i prázdná. Stejně tak zobrazení \(\delta\) pro nějaký stav a symbol nemusí být definováno vůbec, v praktické rovině se však tento případ neliší od předchozího. 

NTS jenž má zobrazení \(\delta\) definované pro všechny dvojice nekoncových stavů a symbolů z pracovní abecedy, kde zároveň platí, že výsledkem je vždy neprázdná množina, nazveme **úplně určený NTS**.

## Poznámka Anki 1670952589690

Karty Anki: 1670952589690
GUID: QiFOupQJz=; štítky: bi-aag::p10.

### Otázka (Front)

Definujte **lineárně omezený Turingův stroj**.

### Odpověď (Back)

Mějme TS \(R = (Q, \Sigma, G, \delta, q_0, \mathtt{B}, F)\). Řekneme, že \(R\) je **lineárně omezený**, jestliže existuje nějaké \(k \geq 1\) takové, že \(\forall w \in \Sigma^*\), které \(R\) dostane na vstupu, využije \(R\) nejvýše \(k \cdot |w|\) buněk na pásce.

## Poznámka Anki 1670952706996

Karty Anki: 1670952706996
GUID: KM9{,/[5b2; štítky: bi-aag::p10.

Metadata původního zdroje pro kartu 1670952706996: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **univerzální Turingův stroj**.

### Odpověď (Back)

**Univerzální Turingův stroj**, značíme \(R_U\), je takový Turingův stroj, který přijímá univerzální jazyk \(L_U = \{([R], w) : \text{Turingův stroj } R \text{ přijímá řetězec } w\}\).

### Doplňující pole (Extra)

Stroj \(R_U\) simuluje výpočet Turingova stroje \(R\) nad řetězcem \(w\). \(R_U\) tak vstup přijme právě tehdy, když jej přijme \(R\) a zároveň se zacyklí právě tehdy, když se zacyklí \(R\).

## Poznámka Anki 1670952757300

Karty Anki: 1670952757300
GUID: q+9PJ(kf9r; štítky: bi-aag::p10.

Metadata původního zdroje pro kartu 1670952757300: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte, kdy **Turingův stroj rozhoduje jazyk**.

### Odpověď (Back)

Turingův stroj \(R\) **rozhoduje** jazyk \(L\) právě tehdy, když jej přijímá (tj. \(L(R) = L\)) a výpočet se pro každý řetězec zastaví (tj. TS se nezacyklí).

## Poznámka Anki 1670952772098

Karty Anki: 1670952772098
GUID: Pe8~.|vQJ=; štítky: bi-aag::p10.

Metadata původního zdroje pro kartu 1670952772098: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **rekurzivní jazyk**.

### Odpověď (Back)

Jazyk je **rekurzivní** právě tehdy, když jej lze rozhodovat nějakým Turingovým strojem.

## Poznámka Anki 1670952849682

Karty Anki: 1670952849683
GUID: G/pD+KfXpw; štítky: bi-aag::p10.

### Otázka (Front)

Vysvětlete, co znamená **redukce problémů**.

### Odpověď (Back)

Uvažujme dva rozhodovací problémy \(A\) a \(B\). Redukcí problému \(B\) na problém \(A\), rozumíme transformaci \(f\), která každou instanci \(I_B\) problému \(B\) převede na ekvivalentní instanci \(I_A = f(I_B)\) problému \(A\). Ekvivalentní zde znamená, že řešení případu \(I_A = f(I_B)\) problému \(A\) je ano právě tehdy, když řešení případu \(I_B\) problému \(B\) je ano.

Existuje-li redukce problému \(B\) na problém \(A\), značíme \(B \leq A\), pak řekneme, že problém \(A\) je aspoň tak těžký (složitý) jako problém \(B\).

### Doplňující pole (Extra)

Redukci můžeme využít, chceme-li o nějakém problému \(X\) dokázat, že je nerozhodnutelný. Budeme přitom potřebovat nějaký známý nerozhodnutelný problém, říkejme mu \(Z\). Pokud nalezneme redukci problému \(Z\) na problém \(X\), pak problém \(X\) je aspoň tak těžký, jako \(Z\) — neboli \(X\) je také nerozhodnutelný problém. Kdyby nebyl, pak bychom problém \(Z\) mohli řešit tak, že jeho instance vždy převedeme na instance problému \(X\).

## Poznámka Anki 1670952904602

Karty Anki: 1670952904603
GUID: KJ{Qh$6GL@; štítky: bi-aag::p10.

### Otázka (Front)

Definujte **halting problem**.

### Odpověď (Back)

**Vstup:** Turingův stroj \(R\) a řetězec \(w\).
**Výstup:** true, pokud se výpočet \(R\) pro \(w\) zastaví. Jinak false.

Tomuto problému se říká problém zastavení Turingova stroje (halting problem). V řeči formálních jazyků jej můžeme formulovat následovně:
\(L_H = \{ ([R],w) : \text{Turingův stroj } R \text{ se pro vstup } w \text{ zastaví}\}\)

### Doplňující pole (Extra)

Jazyk \(L_H\) není rekurzivní / Halting problem je nerozhodnutelný.

## Poznámka Anki 1670952922965

Karty Anki: 1670952922965
GUID: v&]ey|v=AK; štítky: bi-aag::p10.

Metadata původního zdroje pro kartu 1670952922965: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **třídu P**.

### Odpověď (Back)

**Třída P** je taková třída rozhodovacích problémů, které lze řešit v polynomiálně omezeném čase na deterministickém Turingově stroji.

### Doplňující pole (Extra)

Do třídy P patří například rozhodovací verze problému nalezení minimální kostry grafu nebo problému počítání největšího společného dělitele.

## Poznámka Anki 1670952988528

Karty Anki: 1670952988528
GUID: JU`gNc]OQ7; štítky: bi-aag::p10.

Metadata původního zdroje pro kartu 1670952988528: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **třídu NP**.

### Odpověď (Back)

**Třída NP** je taková třída rozhodovacích problémů, které lze řešit v polynomiálně omezeném čase na nedeterministickém Turingově stroji.

### Doplňující pole (Extra)

Protože deterministický TS je speciálním případem nedeterministického TS, tak všechny problémy z třídy P patří též do třídy NP.

Do třídy NP patří například rozhodovací verze problému obchodního cestujícího či izomorfismus grafů.

## Poznámka Anki 1670953014548

Karty Anki: 1670953014549
GUID: G;j-GTlXde; štítky: bi-aag::p10.

### Otázka (Front)

Vysvětlete, co znamená **polynomiální redukce problémů**.

### Odpověď (Back)

Polynomiální redukce je taková redukce problému, která má polynomiální časovou složitost. Máme-li tedy dva rozhodovací problémy \(A\) a \(B\), pak polynomiální redukcí problému \(B\) na problém \(A\) rozumíme transformaci \(f\), která každou instanci \(I_B\) problému \(B\) převede v polynomiálním čase ve velikosti instance \(I_B\) na ekvivalentní instanci \(I_A = f(I_B)\) problému \(A\). Ekvivalentní zde opět znamená, že řešení případu \(I_A = f(I_B)\) problému \(A\) je ano právě tehdy, když řešení případu \(I_B\) problému \(B\) je ano.

Existuje-li polynomiální redukce problému \(B\) na problém \(A\), značíme \(B \leq_p A\), pak řekneme, že problém \(A\) je aspoň tak těžký (složitý) jako problém \(B\).

### Doplňující pole (Extra)

Polynomiální redukci můžeme využít, chceme-li o nějakém problému \(X\) dokázat, že je NP-úplný. Budeme přitom potřebovat nějaký známý NP-úplný problém, říkejme mu \(Z\). Pokud nalezneme polynomiální redukci problému \(Z\) na problém \(X\), pak jsme ukázali, že všechny NP-problémy lze převést na \(X\) (s využitím \(Z\)). Tedy \(X\) je NP-těžký. Pokud ukážeme, že \(X\) je zároveň v NP (tedy, že jej lze řešit polynomiálním čase na nedeterministickém TS), pak jsme ukázali, že \(X\) je NP-úplný.

## Poznámka Anki 1670953027846

Karty Anki: 1670953027846
GUID: z[MD<[ChPY; štítky: bi-aag::p10.

### Otázka (Front)

Definujte **NP-těžký problém**.

### Odpověď (Back)

**NP-těžký problém** (NP-hard) je takový problém, na nějž lze polynomiálně redukovat všechny problémy z třídy NP.

## Poznámka Anki 1670953039999

Karty Anki: 1670953039999
GUID: nvH0}#o#S|; štítky: bi-aag::p10.

### Otázka (Front)

Definujte **NP-úplný problém**.

### Odpověď (Back)

**NP-úplný problém** (NP-complete) je takový problém, který je NP-těžký a sám patří do třídy NP.

## Poznámka Anki 1672757965938

Karty Anki: 1672757965939
GUID: xS{GlKrj*W; štítky: bi-aag::p10 bi-spol::02.

Metadata původního zdroje pro kartu 1672757965939: v původním balíčku pozastavená karta.

### Otázka (Front)

Pro jaké operace jsou jednotlivé třídy Chomského hierarchie jazyků uzavřené?

### Odpověď (Back)

| 
       | 
      **regulární jazyky** | 
      **bezkontextové jazyky** | 
      **kontextové jazyky** | 
      **rekurzivně spočetné jazky** | 

| 
      **sjednocení** | 
      \(\checkmark\)
 | 
      \(\checkmark\)
 | 
      \(\checkmark\)
 | 
      \(\checkmark\) | 

| 
      **průnik** | 
      \(\checkmark\)
 | 
      ✗ | 
      \(\checkmark\)
 | 
      \(\checkmark\) | 

| 
      **doplněk** | 
      \(\checkmark\)
 | 
      ✗
 | 
      \(\checkmark\) | 
      ✗
 | 

| 
      **rozdíl** | 
      \(\checkmark\)
 | 
      ✗
 | 
      \(\checkmark\) | 
      ✗
 | 

| 
      **zřetězení** | 
      \(\checkmark\)
 | 
      \(\checkmark\)
 | 
      \(\checkmark\) | 
      \(\checkmark\) | 

| 
      **iterace** | 
      \(\checkmark\)
 | 
      \(\checkmark\)
 | 
      \(\checkmark\) | 
      \(\checkmark\) |

