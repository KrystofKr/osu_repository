# BI-AAG – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aag/BI-AAG.apkg; APKG SHA-256 0383847389324f3b83b349363b7ad16a6bf91673c90b7a96ed1a57b25a85f8af. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b9cda20d5a5a9d1ff47d4e1fc58b10ed3ac7a37c72c6c1431cc7cb67e2ca10c.
Původní balíčky: BI-AAG
Rozsah: 33 poznámek, 33 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1670947786874

Karty Anki: 1670947786876
GUID: mKkASF&ZZ2; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670947786876: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **formální překlad**.

### Odpověď (Back)

Uvažujme formální jazyky \(L\) a \(V\). **Formální překlad** (značíme \(Z\)) z jazyka \(L\) do jazyka \(V\) definujeme jako binární relaci \(Z \subseteq L \times V\).

### Doplňující pole (Extra)

Obecně tedy relace \(Z\) každému prvku \(w \in L\) přiřazuje množinu jeho překladů \(Z(w) \in V\).

## Poznámka Anki 1670947815458

Karty Anki: 1670947815458
GUID: L,tpUdH*d*; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670947815458: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **jednoznačný formální překlad**.

### Odpověď (Back)

Formální překlad \(Z\) nazveme **jednoznačným**, pokud relace \(Z\) je funkcí (případně parciální).

### Doplňující pole (Extra)

U jednoznačného překladu platí, že \(Z(w)\) pro každé \(w \in L\) obsahuje právě jeden prvek (případně nejvýše jeden prvek v případě parciální funkce).

## Poznámka Anki 1670947838251

Karty Anki: 1670947838251
GUID: J7g90G#wo[; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670947838251: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **překladovou gramatiku**.

### Odpověď (Back)

**Překladová gramatika** (PG) je definována jako uspořádaná pětice \(\mathit{PG} = (N, \Sigma, D, P, S)\), kde

- \(N\) je konečná neprázdná množina neterminálních symbolů,
- \(\Sigma\) je konečná množina **vstupních** symbolů,
- \(D\) je konečná množina **výstupních** symbolů,
- \(P\) je konečná množina přepisovacích pravidel ve tvaru:
- \(A \rightarrow \alpha\), kde \(A \in N\) a \(\alpha \in (N \cup \Sigma \cup D)^*\),
- \(S\) je počáteční neterminální symbol.
Zároveň platí, že množiny \(N, \Sigma, D\) jsou po dvojicích navzájem disjunktní (tj. \(\Sigma \cap D = \emptyset, (\Sigma \cup D) \cap N = \emptyset\)).

## Poznámka Anki 1670947848625

Karty Anki: 1670947848625
GUID: ve%c)i)6KS; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670947848625: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **regulární překladovou gramatiku**.

### Odpověď (Back)

Překladovou gramatiku \((N, \Sigma, D, P, S)\) nazveme **regulární**, pokud každé pravidlo z \(P\) má jeden z následujících tvarů:

- \(A \rightarrow ax\), kde \(A \in N \land a \in \Sigma \land x \in D^*\),
- \(A \rightarrow axB\), kde \(A,B \in N \land a \in \Sigma \land x \in D^*\),
- \(S \rightarrow \varepsilon\).
Pokud ovšem \(P\) obsahuje pravidlo \(S \to \varepsilon\), pak se \(S\) nesmí vyskytovat na pravé straně žádného z pravidel.

## Poznámka Anki 1670947873972

Karty Anki: 1670947873972
GUID: v3m&ns$kHF; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670947873972: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **homomorfismus**.

### Odpověď (Back)

Uvažujme abecedy \(\Sigma\) a \(D\). Pak **homomorfismem** nazýváme každé zobrazení \(h : \Sigma \to D^*\). Definiční obor homomorfismu rozšíříme na \(\Sigma^*\) následovně:
\(h(w) = \begin{cases}\varepsilon & \text{ pokud } w = \varepsilon, \\h(a_1)h(a_2)\dots h(a_n) & \text{ pokud } w = a_1a_2\dots a_n \wedge a_1,a_2,\dots , a_n \in \Sigma \wedge |w| = n \wedge n \geq 2.\end{cases}\)

## Poznámka Anki 1670947897278

Karty Anki: 1670947897278
GUID: qF>J0lo;~|; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670947897278: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **vstupní homomorfismus překladové gramatiky**.

### Odpověď (Back)

Nechť \(\mathit{PG} = (N, \Sigma, D, P, S)\) je překladová gramatika. **Vstupní homomorfismus** překladové gramatiky \(\mathit{PG}\) je homorfismus \(h_i^\mathit{PG} : (\Sigma \cup N \cup D) \to (\Sigma \cup N \cup D)^*\) takový, že \(h_i^\mathit{PG}(a) = \begin{cases}a & \text{ pokud } a \in N \cup \Sigma, \\\varepsilon & \text{ pokud } a \in D.\end{cases}\)

### Doplňující pole (Extra)

Vstupní homomorfismus je tedy zobrazení, které z řetězce nad abecedou \(\Sigma \cup D \cup N\) odebere výstupní symboly (ponechá tam pouze neterminální a vstupní symboly).

## Poznámka Anki 1670947919347

Karty Anki: 1670947919348
GUID: D6^>qd$$C1; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670947919348: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **výstupní homomorfismus překladové gramatiky**.

### Odpověď (Back)

Nechť \(\mathit{PG} = (N, \Sigma, D, P, S)\) je překladová gramatika. **Výstupní homomorfismus** překladové gramatiky \(\mathit{PG}\) je homorfismus \(h_o^\mathit{PG} : (\Sigma \cup N \cup D) \to (\Sigma \cup N \cup D)^*\) takový, že \(h_o^\mathit{PG}(a) = \begin{cases}a & \text{ pokud } a \in N \cup D, \\\varepsilon & \text{ pokud } a \in \Sigma.\end{cases}\)

### Doplňující pole (Extra)

Výstupní homomorfismus je tedy zobrazení, které z řetězce nad abecedou \(\Sigma \cup D \cup N\) odebere vstupní symboly (ponechá tam pouze neterminální a výstupní symboly).

## Poznámka Anki 1670947942830

Karty Anki: 1670947942830
GUID: cM~3HX?@Oi; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670947942830: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **překlad definovaný překladovou gramatikou**.

### Odpověď (Back)

Nechť \(\mathit{PG} = (N, \Sigma, D, P, S)\) je překladová gramatika. Pak **překlad definovaný překladovou gramatikou** \(\mathit{PG}\) definujeme následovně: 
\(Z(\mathit{PG}) = \Big\{ \big(h_i(w), h_o(w)\big) : w \in (\Sigma \cup D)^* \wedge S \Rightarrow^* w\Big\}\).

## Poznámka Anki 1670947958978

Karty Anki: 1670947958978
GUID: D>c4o0fGQZ; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670947958978: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **vstupní gramatiku překladové gramatiky**.

### Odpověď (Back)

Nechť \(\mathit{PG} = (N, \Sigma, D, P, S)\) je překladová gramatika. **Vstupní gramatiku** \(G_i\) překladové gramatiky \(\mathit{PG}\) definujeme následovně: \(G_i = (N, \Sigma, P_i, S)\), kde \(P_i = \{A \rightarrow h_i(\alpha) : (A \rightarrow \alpha) \in P\}\).

### Doplňující pole (Extra)

Vstupní (popřípadě výstupní) gramatika tedy vznikne z překladové gramatiky tak, že odebereme výstupní (popřípadě vstupní) symboly. Z pětice se tak stane čtveřice a ve všech pravidlech budou ponechány pouze vstupní (popřípadě výstupní) symboly a neterminály.

## Poznámka Anki 1670947986502

Karty Anki: 1670947986502
GUID: G,)10vu{Y+; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670947986502: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **výstupní gramatiku překladové gramatiky**.

### Odpověď (Back)

Nechť \(\mathit{PG} = (N, \Sigma, D, P, S)\) je překladová gramatika. **Výstupní gramatiku** \(G_o\) překladové gramatiky \(\mathit{PG}\) definujeme následovně: 
\(G_o = (N, D, P_o, S)\), kde \(P_o = \{A \rightarrow h_o(\alpha) : (A \rightarrow \alpha) \in P\}\).

### Doplňující pole (Extra)

Vstupní (popřípadě výstupní) gramatika tedy vznikne z překladové gramatiky tak, že odebereme výstupní (popřípadě vstupní) symboly. Z pětice se tak stane čtveřice a ve všech pravidlech budou ponechány pouze vstupní (popřípadě výstupní) symboly a neterminály.

## Poznámka Anki 1670948014140

Karty Anki: 1670948014140
GUID: hZ:onUF84t; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948014140: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **charakteristickou gramatiku** překladové gramatiky.

### Odpověď (Back)

Nechť \(\mathit{PG} = (N, \Sigma, D, P, S)\) je překladová gramatika. **Charakteristickou gramatiku** \(G\) překladové gramatiky \(\mathit{PG}\) definujeme následovně: \(G = (N, \Sigma \cup D, P, S)\).

## Poznámka Anki 1670948035799

Karty Anki: 1670948035799
GUID: k(,TiO$ok@; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948035799: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **charakteristický jazyk** překladové gramatiky.

### Odpověď (Back)

Nechť \(\mathit{PG} = (N, \Sigma, D, P, S)\) je překladová gramatika a \(G = (N, \Sigma \cup D, P, S)\) její charakteristická gramatika. Jazyk \(L(G)\) nazýváme **charakteristický jazyk** překladu \(Z(\mathit{PG})\).

## Poznámka Anki 1670948084380

Karty Anki: 1670948084380
GUID: E!=eKb>44l; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948084380: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **charakteristickou větu** překladové gramatiky.

### Odpověď (Back)

Nechť \(\mathit{PG} = (N, \Sigma, D, P, S)\) je překladová gramatika a \(G = (N, \Sigma \cup D, P, S)\) její charakteristická gramatika. Řetězec \(w \in L(G)\) nazýváme **charakteristickou větou** dvojice \((u,v) \in Z(\mathit{PG})\), kde \(u = h_i(w)\) a \(v = h_o(w)\).

## Poznámka Anki 1670948121904

Karty Anki: 1670948121904
GUID: P$[|iQTM9E; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948121904: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **konečný překladový automat**.

### Odpověď (Back)

**Konečný překladový automat** je uspořádaná šestice \(\mathit{KPA} = (Q, \Sigma, D, \delta, q_0, F)\), kde

- \(Q\) je konečná neprázdná množina stavů,
- \(\Sigma\) je konečná množina vstupních symbolů,
- \(D\) je konečná množina výstupních symbolů,
- \(\delta : Q \times (\Sigma \cup \{\varepsilon\}) \to \mathcal{P}(Q \times D^*)\), kde \(\mathcal{P}(Q \times D^*)\) reprezentuje množinu všech konečných podmnožin množiny \(Q \times D^*\), je přechodová funkce,
- \(q_0 \in Q\) je počáteční stav,
- \(F \subseteq Q\) je množina koncových stavů.

### Doplňující pole (Extra)

(prázdné pole)

## Poznámka Anki 1670948139320

Karty Anki: 1670948139321
GUID: v43~+L.B@G; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948139321: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **deterministický konečný překladový automat**.

### Odpověď (Back)

Konečný překladový automat \(\mathit{KPA} = (Q, \Sigma, D, \delta, q_0, F)\) nazveme **deterministický** (DKPA), pokud pro všechny dvojice stavů \(q \in Q\) a symbolů \(a \in \Sigma\) platí jedna z následujících podmínek:

- přechod \(\delta(q, a)\) není definován, nebo
- \(|\delta(q,a)| \leq 1 \wedge \delta(q,\varepsilon) = \emptyset\), nebo
- \(\delta(q,a) = \emptyset \wedge |\delta(q,\varepsilon)| \leq 1\).

## Poznámka Anki 1670948154527

Karty Anki: 1670948154527
GUID: srDNRg/:+.; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948154527: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **konfiguraci konečného překladového automatu**.

### Odpověď (Back)

Uvažujme konečný překladový automat \(\mathit{KPA} = (Q, \Sigma, D, \delta, q_0, F)\). **Konfigurací** konečného překladového automatu \(\mathit{KPA}\) je trojice \((q, x, y) \in Q \times \Sigma^* \times D^*\).

## Poznámka Anki 1670948183543

Karty Anki: 1670948183543
GUID: B0hQa;blv?; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948183543: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **počáteční konfiguraci konečného překladového automatu**.

### Odpověď (Back)

Uvažujme konečný překladový automat \(\mathit{KPA} = (Q, \Sigma, D, \delta, q_0, F)\) a vstupní řetězec \(u \in \Sigma^*\). Pak konfigurace \((q_0, u, \varepsilon)\) je **počáteční konfigurace** konečného překladového automatu \(\mathit{KPA}\).

### Doplňující pole (Extra)

Počáteční konfigurace KPA je tedy taková konfigurace, ve které se KPA nachází na začátku svého výpočtu (tj. je v počátečním stavu, zpracovat mu zbývá celý vstupní řetězec \(w\) a výstupní páska je zatím zcela prázdná).

## Poznámka Anki 1670948207042

Karty Anki: 1670948207042
GUID: F^p!_J,_ST; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948207042: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **přijímací konfiguraci konečného překladového automatu**.

### Odpověď (Back)

Uvažujme konečný překladový automat \(\mathit{KPA} = (Q, \Sigma, D, \delta, q_0, F)\). Pak konfigurace \((q, \varepsilon, v)\), kde \(q \in F\) a \(v \in D^*\), je **přijímací konfigurace **konečného překladového automatu \(\mathit{KPA}\).

### Doplňující pole (Extra)

Přijímací konfigurace KPA je tedy tedy taková konfigurace, ve které se KPA nachází na konci svého přijímacího výpočtu (tj. je v nějakém koncovém stavu, celý vstup byl zpracován a na výstupu je řetězec \(v\) reprezentující výsledný překlad).

## Poznámka Anki 1670948236371

Karty Anki: 1670948236371
GUID: F4/}p$6Zsw; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948236371: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **přechod konečného překladového automatu**.

### Odpověď (Back)

Mějme konečný překladový automat \(\mathit{KPA} = (Q, \Sigma, D, \delta, q_0, F)\). **Přechodem** v automatu \(\mathit{KPA}\) nazveme prvek relace \(\vdash_{\mathit{KPA}}\) nad \(\left(Q \times \Sigma^{*} \times D^* \right) \times \left(Q \times \Sigma^{*} \times D^* \right)\) s touto vlastností:\((q, aw, y) \vdash_{\mathit{KPA}} (p, w, yz) \iff (p,z) \in \delta(q, a)\), kde \(a\in (\Sigma \cup \{\varepsilon\})\), \(w \in \Sigma^*\) a \(y,z \in D^*\).

\(k\)-tá mocnina relace \(\vdash_{\mathit{KPA}}\), kde \(k \in \mathbb{N}_{0}\), se značí \(\vdash_{\mathit{KPA}}^{k}\) a je definovaná takto:
\((p_0, w_0, y_0) \vdash_{\textit{KPA}}^k (p_k, w_k, y_k)\): \(\forall i \in \{0, \dots, k-1\} : \exists (p_i, w_i, y_i): (p_i, w_i, y_i) \vdash_{\mathit{KPA}} (p_{i+1}, w_{i+1}, y_{i+1})\).

Tranzitivní uzávěr relace \(\vdash_{\mathit{KPA}}\) značíme \(\vdash_{\mathit{KPA}}^+\). Tranzitivní a reflexivní uzávěr relace \(\vdash_{\mathit{KPA}}\) značíme \(\vdash_{\mathit{KPA}}^*\).

### Doplňující pole (Extra)

Relace \(\vdash_{\textit{KPA}}\) nám tedy říká, mezi kterými dvěma konfiguracemi můžeme přejít. To souvisí s přechody, které dovoluje zobrazení \(\delta\). Tato relace představuje jeden krok, který je v daném KPA možný, zatímco \(k\)-tá mocnina představuje několik kroků (do jaké konfigurace se můžeme dostat po \(k\) krocích z konfigurace výchozí). Tranzitivní a reflexivní uzávěr pak říká, do jakých možných konfigurací se lze z té výchozí dostat po libovolném počtu kroků (včetně nulového), zatímco tranzitivní uzávěr říká, do jakých konfigurací se lze dostat z té výchozí po alespoň jednom kroku. Značení \(\vdash_{\textit{KPA}}\) budeme zjednodušovat jen na \(\vdash\), pokud je z kontextu KPA jasný.

## Poznámka Anki 1670948259204

Karty Anki: 1670948259204
GUID: x:6hq+*rW0; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948259204: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **překlad definovaný konečným překladovým automatem**.

### Odpověď (Back)

Mějme konečný překladový automat \(\mathit{KPA} = (Q, \Sigma, D, \delta, q_0, F)\). Pak překlad definovaný konečným překladovým automatem \(\mathit{KPA}\) definujeme následovně: 
\(Z(\mathit{KPA}) = \{(u,v) : (q_0, u, \varepsilon) \vdash^* (q, \varepsilon, v) \land u \in \Sigma^* \land v \in D^* \land q \in F\}\).

### Doplňující pole (Extra)

Vstupní řetězce, které KPA přijme, tvoří definiční obor překladu definovaného daným KPA. Naopak výstupní řetězce, které KPA pošle na výstup při přijímání nějakého řetězce z definičního oboru, tvoří obor hodnot. Řetězec \(v\) z oboru hodnot je překladem řetězce \(u\) z definičního oboru, pokud v automatu existuje posloupnost přechodů vedoucí k přijetí \(u\) a zároveň vypsání řetězce \(v\) na výstup.

## Poznámka Anki 1670948272557

Karty Anki: 1670948272557
GUID: NXm^,$jSDr; štítky: bi-aag::p09.

### Otázka (Front)

Definujte **Mealyho automat**.

### Odpověď (Back)

**Mealyho automat **definujeme jako šestici \(M = (Q, \Sigma, D, \delta, \lambda, q_0)\), kde

- \(Q\) je konečná neprázdná množina stavů,
- \(\Sigma\) je konečná množina vstupních symbolů,
- \(D\) je konečná množina výstupních symbolů,
- \(\delta : Q \times \Sigma \to Q\) je přechodová funkce, 
- \(\lambda : Q \times \Sigma \to D\) je výstupní funkce (parciální funkci zde nepřipouštíme),
- \(q_0 \in Q\) je počáteční stav.

## Poznámka Anki 1670948295077

Karty Anki: 1670948295077
GUID: sC9I_TAi5/; štítky: bi-aag::p09.

### Otázka (Front)

Definujte **Mooreův automat**.

### Odpověď (Back)

**Mooreův automat** definujeme jako šestici \(M = (Q, \Sigma, D, \delta, \lambda, q_0)\), kde

- \(Q\) je konečná neprázdná množina stavů,
- \(\Sigma\) je konečná množina vstupních symbolů,
- \(D\) je konečná množina výstupních symbolů,
- \(\delta : Q \times \Sigma \to Q\) je přechodová funkce,
- \(\lambda : Q \to D\) je výstupní funkce (parciální funkci zde nepřipouštíme),
- \(q_0 \in Q\) je počáteční stav.

## Poznámka Anki 1670948322077

Karty Anki: 1670948322077
GUID: dEctA*Hp5}; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948322077: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **zásobníkový překladový automat**.

### Odpověď (Back)

**Zásobníkový překladový automat** definujeme jako uspořádanou osmici \(\mathit{ZPA} = (Q, \Sigma, G, D, \delta, q_0, Z_0, F)\), kde

- \(Q\) je konečná neprázdná množina stavů,
- \(\Sigma\) je konečná množina vstupních symbolů,
- \(G\) je konečná neprázdná množina zásobníkových symbolů,
- \(D\) je konečná množina výstupních symbolů,
- \(\delta : Q \times (\Sigma \cup \{\varepsilon\}) \times G^* \to \mathcal{P}(Q \times G^* \times D^*)\), kde \(\mathcal{P}(Q \times G^* \times D^*)\) reprezentuje množinu všech konečných podmnožin množiny \(Q \times G^* \times D^*\), je přechodová funkce,
- \(q_0 \in Q\) je počáteční stav,
- \(Z_0 \in G\) je počáteční symbol na zásobníku,
- \(F \subseteq Q\) je množina koncových stavů.

## Poznámka Anki 1670948347306

Karty Anki: 1670948347306
GUID: ibgetq#l>a; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948347306: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **deterministický překladový zásobníkový automat**.

### Odpověď (Back)

Zásobníkový překladový automat \(\mathit{ZPA} = (Q, \Sigma, G, D, \delta, q_0, Z_0, F)\) je **deterministický** (DZPA), jestliže \(\forall q\in Q \land \forall a \in \Sigma\cup\{\varepsilon\} \land \forall \alpha, \beta \in G^*\):

- \(|\delta(q, a, \alpha)| \leq 1\) a současně
- jestliže \(\delta(q, a, \alpha) \neq \emptyset \land \delta(q, a, \beta) \neq \emptyset\), pak \(\alpha\) není předponou \(\beta\) (ani opačně) a současně
- jestliže \(\delta(q, a, \alpha) \neq \emptyset \land \delta(q, \varepsilon, \beta) \neq \emptyset\), pak \(\alpha\) není předponou \(\beta\) (ani opačně).

### Doplňující pole (Extra)

Zásobníkový překladový automat je tedy deterministický, pokud je deterministický zásobníkový automat, který vznikne po vynechání výstupních symbolů.

## Poznámka Anki 1670948369183

Karty Anki: 1670948369183
GUID: k$g7J)],lE; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948369183: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **konfiguraci zásobníkového překladového automatu**.

### Odpověď (Back)

Nechť \(\mathit{ZPA} = (Q, \Sigma, G, D, \delta, q_0, Z_0, F)\) je zásobníkový překladový automat. **Konfigurace** zásobníkového překladového automatu \(\mathit{ZPA}\) je čtveřice
\((q, x, \alpha, y) \in Q \times \Sigma^* \times G^* \times D^*\).

### Doplňující pole (Extra)

Obdobně jako u ostatních automatů, konfiguraci zásobníkového překladového automatu získáme, když během výpočtu automatu provedeme snapshot, tj. zastavíme výpočet a podíváme se, v jakém stavu \(q\) se automat nachází, jaký řetězec \(x\) mu ještě zbývá na vstupu zpracovat, jaký řetězec \(\alpha\) má na zásobníku (tedy celý obsah zásobníku) a jaký řetězec \(y\) se aktuálně nachází na výstupu.

## Poznámka Anki 1670948392812

Karty Anki: 1670948392812
GUID: EXJ-FV,BYf; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948392812: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **počáteční konfiguraci zásobníkového překladového automatu**.

### Odpověď (Back)

Nechť \(\mathit{ZPA} = (Q, \Sigma, G, D, \delta, q_0, Z_0, F)\) je zásobníkový překladový automat a \(u \in \Sigma^*\) je vstupní řetězec. Pak konfigurace \((q_0, u, Z_0, \varepsilon)\) je **počáteční konfigurací** zásobníkového překladového automatu \(\mathit{ZPA}\).

## Poznámka Anki 1670948413929

Karty Anki: 1670948413929
GUID: K&D8&vH43c; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948413929: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **přechod zásobníkového překladového automatu**.

### Odpověď (Back)

Nechť \(\mathit{ZPA} = (Q, \Sigma, G, D, \delta, q_0, Z_0, F)\) je zásobníkový překladový automat. **Přechodem** v zásobníkovém překladovém automatu \(\mathit{ZPA}\) nazveme prvek relace \(\vdash_{\mathit{ZPA}}\) nad \((Q \times \Sigma^* \times G^* \times D^*) \times (Q \times \Sigma^* \times G^* \times D^*)\) s touto vlastností: \((q, aw, \alpha\gamma, x) \vdash_{\mathit{ZPA}} (p, w, \beta \gamma, xy) \iff (p, \beta, y) \in \delta(q, a ,\alpha)\), kde \(a \in (\Sigma\cup\{\varepsilon\}) \land w \in \Sigma^* \land \alpha,\beta,\gamma \in G^* \land x,y \in D^*\) (vrchol zásobníku uvažujeme vlevo).

\(k\)-tá mocnina relace \(\vdash_{\textit{ZPA}}\), její tranzitivní i tranzitivní a reflexivní uzávěr jsou definovány obdobně jako v případě přechodu konečného překladového automatu.

## Poznámka Anki 1670948439299

Karty Anki: 1670948439299
GUID: Cr#tvI1CL0; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948439299: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **překlad definovaný zásobníkovým překladovým automatem přechodem do koncového stavu**.

### Odpověď (Back)

Uvažujme zásobníkový překladový automat \(\mathit{ZPA} = (Q, \Sigma, G, D, \delta, q_0, Z_0, F)\). **Překlad definovaný** zásobníkovým překladovým automatem \(\mathit{ZPA}\) **přechodem do koncového stavu** definujeme takto: \(Z(\mathit{ZPA}) = \big\{(u,v) : (q_0, u, Z_0, \varepsilon) \vdash^* (q, \varepsilon, \alpha, v) \land u \in \Sigma^* \land v \in D^* \land \alpha \in G^* \land q \in F\big\}\).

## Poznámka Anki 1670948480772

Karty Anki: 1670948480772
GUID: u./j(d1T!]; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948480772: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **překlad definovaný zásobníkovým překladovým automatem přechodem do konfigurace s prázdným zásobníkem**.

### Odpověď (Back)

Uvažujme zásobníkový překladový automat \(\mathit{ZPA} = (Q, \Sigma, G, D, \delta, q_0, Z_0, F)\). **Překlad definovaný** zásobníkovým překladovým automatem \(\mathit{ZPA}\) **přechodem do konfigurace s prázdným zásobníkem** definujeme takto: \(Z_\varepsilon(\mathit{ZPA}) = \big\{(u,v) : (q_0, u, Z_0, \varepsilon) \vdash^* (q, \varepsilon, \varepsilon, v) \land u \in \Sigma^* \land v \in D^* \land q \in Q\big\}\).

### Doplňující pole (Extra)

Konvence: U ZPA, jenž překlad definuje přechodem do konfigurace s prázdným zásobníkem, budeme množinu koncových stavů definovat jako prázdnou.

## Poznámka Anki 1670948505898

Karty Anki: 1670948505898
GUID: L<{k:w|+2a; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948505898: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus pro převod RPG na KPA**.

### Odpověď (Back)

**Vstup:** Regulární překladová gramatika \(\mathit{RPG} = (N, \Sigma, D, P, S)\).

**Výstup:** Konečný překladový automat \(\mathit{KPA} = (Q, \Sigma, D, \delta, S, F)\) takový, že \(Z(\mathit{KPA}) = Z(\mathit{RPG})\).

**Postup:**

1. Pro každý neterminál \(A \in N\) vytvoříme nekoncový stav v automatu \(\mathit{KPA}\).
2. Stav odpovídající počátečnímu neterminálu bude počátečním stavem automatu \(\mathit{KPA}\).
3. Pokud \(G\) neobsahuje pravidlo \(S \to \varepsilon\), pak \(\mathit{KPA}\) bude mít pouze jeden koncový stav \(K\) takový, že \(K\) neodpovídá žádnému neterminálnímu symbolu, tedy \(K \notin N\). V opačném případě bude koncový navíc i stav \(S\).
4. Pro každé pravidlo tvaru \(A \to axB\), kde \(a \in \Sigma\), \(x \in D^*\) a \(A, B \in N\) přidáme přechod ze stavu \(A\) do \(B\) ohodnocený \(a / x\). Například:

 [Obrázek: paste-86da25a0a9c7b11a0885dec7d1c5003060267eac.jpg; soubor je v media/ v doprovodném ZIP] 

5. Pro každé pravidlo tvaru \(A \to ax\), kde \(a \in \Sigma\), \(x \in D^*\) a \(A \in N\) přidáme přechod ze stavu \(A\) do koncového stavu \(K\) ohodnocený \(a / x\). Například:

 [Obrázek: paste-caaf147402e6a137bf431076be5c871c90686b50.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1670948528818

Karty Anki: 1670948528818
GUID: Cerpy@QzU`; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948528818: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus pro převod KPA na RPG**.

### Odpověď (Back)

**Vstup:** Konečný překladový automat \(\mathit{KPA} = (Q, \Sigma, D, \delta, S, F)\), kde \(\Sigma \cap D = \emptyset\) a \((\Sigma \cup D) \cap Q = \emptyset\). Zároveň předpokládáme, že \(\mathit{KPA}\) neobsahuje \(\varepsilon\)-přechody.

**Výstup:** Regulární překladová gramatika \(\mathit{RPG} = (N, \Sigma, D, P, S)\)  taková, že \(Z(\mathit{RPG}) = Z(\mathit{KPA})\).

**Postup:**

1. Pro každý stav vytvoříme v gramatice \(\mathit{RPG}\) jeden neterminál.
2. Neterminál odpovídající počátečnímu stavu bude startovacím neterminálem gramatiky \(\mathit{RPG}\).
3. Pro přechody typu \((B,x) \in \delta(A,a)\), kde \(B\) je nekoncový stav, přidáme do gramatiky pravidlo \(A \rightarrow axB\). Například:

 [Obrázek: paste-250692413c107ecec28c7648421f25231523acf6.jpg; soubor je v media/ v doprovodném ZIP] 

4. Pro přechody typu \((B,x) \in \delta(A,a)\), kde \(B\) je koncový stav, přidáme do gramatiky pravidlo \(A \rightarrow axB \mid ax\). Například:

 [Obrázek: paste-69a97071a2be42991992df3ef0d79c00c3c7073d.jpg; soubor je v media/ v doprovodném ZIP] 

5. Pokud je počáteční stav \(S\) zároveň koncový, pak do gramatiky přidáme pravidlo \(S \to \varepsilon\). Dále zkontrolujeme, zdali se startovací neterminál nevyskytuje též na pravé straně pravidel. Pokud ano musíme gramatiku následovně upravit: Vytvoříme nový startovací neterminál \(S^\prime\) s pravidlem \(S^\prime \rightarrow \varepsilon\). U původního startovacího neterminálu \(\varepsilon\)-pravidlo odstraníme. Všechny pravé strany pravidel pro původní startovací neterminál přidáme též k neterminálu \(S^\prime\).

## Poznámka Anki 1670948558447

Karty Anki: 1670948558447
GUID: HquxcKKyP_; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1670948558447: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus pro převod PG na ZPA**.

### Odpověď (Back)

**Vstup:** Překladová gramatika \(\mathit{PG} = (N, \Sigma, D, P, S)\).

**Výstup:** Zásobníkový překladový automat \(\mathit{ZPA} = (Q, \Sigma, G, D, \delta, q_0, Z_0, F)\) s vrcholem zásobníku vlevo takový, že \(Z_\varepsilon(\mathit{ZPA}) = Z(\mathit{PG})\).  

**Postup:**

1. \(Q = \{q_0\}\).
2. \(G = N \cup \Sigma \cup D\).
3. (srovnání) \(\forall a \in \Sigma : \delta(q_0, a, a) = \{ (q_0, \varepsilon, \varepsilon) \}\).
4. (expanze) \(\forall (A \to \alpha) \in P\), kde \(\alpha \in (N \cup \Sigma \cup D)^*\), přidáme přechod \(\delta(q_0, \varepsilon, A) = \{ (q_0, \alpha, \varepsilon) \}\).
5. (výstup) \(\forall x \in D : \delta(q_0, \varepsilon, x) = \{ (q_0, \varepsilon, x) \}\).
6. \(Z_0 = S\) (tj. počáteční zásobníkový symbol odpovídá počátečnímu neterminálu).
7. \(F = \emptyset\).

### Doplňující pole (Extra)

Graficky si zásobníkový překladový automat, který je výstupem algoritmu, můžeme zakreslit následovně:

 [Obrázek: paste-fa149ef6f1bccda9d4d0a71e98cedb886c6de9fa.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1672755356020

Karty Anki: 1672755356020
GUID: wa?8mJ:5NE; štítky: bi-aag::p09.

Metadata původního zdroje pro kartu 1672755356020: v původním balíčku pozastavená karta.

### Otázka (Front)

Mějme vstupní řetězec \(w \in \Sigma^*\) délky \(n\). Jak dlouhý výstup vyprodukují pro tento řetězec **Mealyho **a **Mooreův **automat?

### Odpověď (Back)

**Mealyho **automat vygeneruje výstup délky \(n\), kdežto **Mooreův** automat vygeneruje výstup délky \(n + 1\).

