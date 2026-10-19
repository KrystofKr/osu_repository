# BI-AAG – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aag/BI-AAG.apkg; APKG SHA-256 0383847389324f3b83b349363b7ad16a6bf91673c90b7a96ed1a57b25a85f8af. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b9cda20d5a5a9d1ff47d4e1fc58b10ed3ac7a37c72c6c1431cc7cb67e2ca10c.
Původní balíčky: BI-AAG
Rozsah: 24 poznámek, 24 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1664477798154

Karty Anki: 1664477798154
GUID: cL}H!1?P_t; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte **deterministický konečný automat**.

### Odpověď (Back)

**Deterministický konečný automat** (DKA) definujeme jako uspořádanou pětici \(M = (Q,\Sigma,\delta,q_0,F)\), kde

- \(Q\) je konečná neprázdná množina **stavů**,
- \(\Sigma\) je abeceda obsahující **vstupní symboly**,
- \(\delta : Q \times \Sigma \rightarrow Q\) je **přechodová funkce**,
- \(q_0 \in Q\) je **počáteční stav**,
- \(F \subseteq Q\) je množina **koncových stavů**.
Zobrazení \(\delta\) nemusí být u DKA definované pro všechny dvojice stavů \(q \in Q\) a vstupních symbolů \(a \in \Sigma\).

## Poznámka Anki 1664477881899

Karty Anki: 1664477881899
GUID: mQzAxXK{]x; štítky: bi-aag::p02 bi-spol::01.

Metadata původního zdroje pro kartu 1664477881899: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **úplně určený** deterministický konečný automat.

### Odpověď (Back)

Zobrazení \(\delta\) nemusí být obecně u DKA definované pro všechny dvojice stavů \(q \in Q\) a vstupních symbolů \(a \in \Sigma\). Deterministický konečný automat, jenž má zobrazení \(\delta\) definované pro všechny dvojice stavů \(q \in Q\) a vstupních symbolů \(a \in \Sigma\) nazveme **úplně určený DKA**.

## Poznámka Anki 1664478054698

Karty Anki: 1664478054698
GUID: fz?V.y{Jd-; štítky: bi-aag::p02.

Metadata původního zdroje pro kartu 1664478054698: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadaný deterministický konečný automat vrátí ekvivalentní** úplně určený** deterministický konečný automat.

### Odpověď (Back)

**Vstup:** DKA \(M = (Q, \Sigma, \delta, q_0, F)\). 

**Výstup:** Úplně určený DKA \(M^\prime = (Q^\prime, \Sigma, \delta^\prime, q_0, F)\) takový, že \(L(M) = L(M^\prime)\).

**Postup:**

1. \(Q^\prime = Q \cup \{q_\emptyset\}\), kde \(q_\emptyset \notin Q\). Jinými slovy, ke stávajícím stavům přidáme nový stav \(q_\emptyset\). Tento stav nazýváme nulový.
2. Do \(\delta^\prime\) přidáme všechny přechody, které obsahuje \(\delta\).
3. \(\forall a \in \Sigma: \delta^\prime(q_\emptyset,a) = q_\emptyset\). Jinými slovy, ke stavu \(q_\emptyset\) přidáme smyčku pro všechny symboly abecedy.
4. Ze všech stavů \(q \in Q\), které v \(M\) nemají definovaný přechod pro nějaký symbol abecedy \(a \in \Sigma\), přidáme v \(M^\prime\) přechod na tento symbol do stavu \(q_\emptyset\), tedy \(\delta^\prime(q, a) = q_\emptyset \iff \delta(q,a)\) není definováno.

## Poznámka Anki 1664478138159

Karty Anki: 1664478138159
GUID: J0TR.q0Yeg; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte **konfiguraci konečného automatu**.

### Odpověď (Back)

Uvažujme konečný automat \(M = (Q, \Sigma, \delta, q_0, F)\). **Konfigurace konečného automatu** \(M\) je dvojice \((q, w) \in Q \times \Sigma^*\).

### Doplňující pole (Extra)

Konfiguraci automatu získáme, když během výpočtu automatu provedeme jakýsi snapshot — tj. zastavíme výpočet a podíváme se, v jakém stavu \(q\) se automat nachází a jaká nepřečtená část \(w\) vstupního řetězce mu ještě zbývá zpracovat.

## Poznámka Anki 1664478177486

Karty Anki: 1664478177487
GUID: LQQY-fyc)D; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte **počáteční konfiguraci konečného automatu**.

### Odpověď (Back)

Uvažujme konečný automat \(M = (Q, \Sigma, \delta, q_0, F)\) a vstupní řetězec \(w \in \Sigma^*\). Pak konfigurace \((q_0, w)\) je **počáteční konfigurace** konečného automatu \(M\).

## Poznámka Anki 1664478240390

Karty Anki: 1664478240390
GUID: G>2euK(hI2; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte **přijímací konfiguraci konečného automatu**.

### Odpověď (Back)

Uvažujme konečný automat \(M = (Q, \Sigma, \delta, q_0, F)\). Pak konfigurace \((q, \varepsilon)\), kde \(q \in F\), je **přijímací konfigurace** konečného automatu \(M\).

## Poznámka Anki 1664478376179

Karty Anki: 1664478376179
GUID: Kk3#f32+*n; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte pojem **přechod deterministického konečného automatu**.

### Odpověď (Back)

Mějme DKA \(M = (Q, \Sigma, \delta, q_0, F)\). **Přechodem** v automatu \(M\) nazveme prvek relace \(\vdash_M\) nad \((Q \times \Sigma^*) \times (Q \times \Sigma^*)\) s touto vlastností:

\((p, au) \vdash_M (q, u) \iff \delta(p, a) = q\).

\(k\)-tá mocnina relace \(\vdash_M\), kde \(k \in \mathbb{N}_0\), se značí \(\vdash_M^k\) a je definovaná takto: \((p_0, w_0) \vdash_M^k (p_k, w_k)\) právě tehdy, když pro všechny \(i \in \{0, \dots, k-1\}\) existuje \((p_i, w_i)\) tak, že \((p_i, w_i) \vdash_M (p_{i+1}, w_{i+1})\).

Tranzitivní uzávěr relace \(\vdash_M\) značíme \(\vdash_M^+\). Tranzitivní a reflexivní uzávěr relace \(\vdash_M\) značíme \(\vdash_M^*\).

### Doplňující pole (Extra)

Značení \(\vdash_M\) zjednodušujeme jen na \(\vdash\), pokud je z kontextu automat jasný. 

Relace \(\vdash_M\) nám tedy říká, mezi kterými dvěma konfiguracemi můžeme v daném DKA \(M\) přejít. To souvisí s přechody, které definuje zobrazení \(\delta\). Tato relace představuje jeden krok, který je v daném DKA možný, zatímco \(k\)-tá mocnina představuje několik kroků (do jaké konfigurace se můžeme dostat po \(k\) krocích z konfigurace výchozí). Tranzitivní a reflexivní uzávěr pak říká, do jakých možných konfigurací se lze z té výchozí dostat po libovolném počtu kroků (včetně nulového), zatímco tranzitivní uzávěr říká, do jakých konfigurací se lze dostat z té výchozí po alespoň jednom kroku.

## Poznámka Anki 1664478442328

Karty Anki: 1664478442328
GUID: B~1.c6>p)|; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte pojem **řetězec přijímaný deterministickým konečným automatem**.

### Odpověď (Back)

Řekněme, že řetězec \(w\) je **přijímaný** deterministickým konečným automatem \(M = (Q, \Sigma, \delta, q_0, F)\) právě tehdy, když

\(\exists (q_0, w) \vdash^* (q, \varepsilon)\), kde \(q \in F\).

### Doplňující pole (Extra)

Řetězec \(w\) je tedy přijímaný DKA \(M\), existuje-li posloupnost přechodů taková, která z počáteční konfigurace \((q_0, w)\) vede do přijímací konfigurace \((q, \varepsilon)\), kde \(q \in F\). Taková posloupnost v deterministickém konečném automatu může existovat pouze jedna.

## Poznámka Anki 1664478525947

Karty Anki: 1664478525947
GUID: DHD8+Fy.Y9; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte pojem **jazyk přijímaný deterministickým konečným automatem**.

### Odpověď (Back)

Uvažujme DKA \(M = (Q, \Sigma, \delta, q_0, F)\). **Jazyk** přijímaný \(M\), zapisujeme jako \(L(M)\), definujeme následovně:

\(L(M) = \{w : w \in \Sigma^* \wedge (q_0, w) \vdash^* (q, \varepsilon) \wedge q \in F\}\).

### Doplňující pole (Extra)

Jazyk přijímaný DKA \(M\) je tedy tvořen všemi řetězci nad abecedou \(\Sigma\), které \(M\) přijímá.

## Poznámka Anki 1664478672297

Karty Anki: 1664478672297
GUID: bOm`lrVZx;; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte **nedeterministický konečný automat**.

### Odpověď (Back)

**Nedeterministický konečný automat** (NKA) definujeme jako uspořádanou pětici \(M = (Q,\Sigma,\delta,q_0,F)\), kde

- \(Q\), \(\Sigma\), \(q_0\), \(F\) jsou definovány stejně jako u DKA,
- přechodová funkce je definována jako \(\delta : Q \times \Sigma \rightarrow \mathcal{P}(Q)\).

### Doplňující pole (Extra)

Zobrazení \(\delta\) u NKA tedy povoluje, že se lze například ze stavu \(q_1\) na symbol \(\mathtt{a}\) vydat do dvou různých následujících stavů \(q_2\) a \(q_3\). Výsledkem zobrazení \(\delta\) u NKA může být pro nějaký stav a symbol též prázdná množina stavů. Stejně tak zobrazení \(\delta\) pro nějaký stav a symbol nemusí být definováno vůbec, v praktické rovině se však tento případ neliší od předchozího.

## Poznámka Anki 1664478733192

Karty Anki: 1664478733192
GUID: b`pDREzNt~; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte pojem **přechod nedeterministického konečného automatu**.

### Odpověď (Back)

Mějme NKA \(M = (Q, \Sigma, \delta, q_0, F)\). **Přechodem** v automatu \(M\) nazveme prvek relace \(\vdash_M\) nad \((Q \times \Sigma^*) \times (Q \times \Sigma^*)\) s touto vlastností: 

\((p, au) \vdash_M (q, u) \iff q\in\delta(p, a)\).

\(k\)-tá mocnina relace \(\vdash_M\), tranzitivní uzávěr relace \(\vdash_M\) i tranzitivní a reflexivní uzávěr relace \(\vdash_M\) jsou definovány obdobně jako v případě DKA.

## Poznámka Anki 1664478800514

Karty Anki: 1664478800514
GUID: z]7I$1#X%h; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte pojem **řetězec přijímaný nedeterministickým konečným automatem**.

### Odpověď (Back)

Řekněme, že řetězec \(w\) je **přijímaný** nedeterministickým konečným automatem \(M = (Q, \Sigma, \delta, q_0, F)\) právě tehdy, když

\(\exists (q_0, w) \vdash^* (q, \varepsilon) \), kde \(q \in F\).

### Doplňující pole (Extra)

Řetězec \(w\) je tedy přijímaný NKA \(M\), existuje-li posloupnost přechodů taková, která z počáteční konfigurace \((q_0, w)\) vede do přijímací konfigurace \((q, \varepsilon)\), kde \(q \in F\). Na rozdíl od DKA takových posloupností může v NKA existovat i více. 

NKA tedy přijme řetězec na vstupu, pokud v automatu existuje alespoň jedna posloupnost přechodů vedoucí k přijetí (tj. kdy je přečten celý řetězec a výpočet skončí v některém z koncových stavů). Ve všech ostatních případech NKA řetězec nepřijme.

## Poznámka Anki 1664478845381

Karty Anki: 1664478845381
GUID: oQi-tu~Tb7; štítky: bi-aag::p02 bi-spol::01.

### Otázka (Front)

Definujte **jazyk přijímaný nedeterministickým konečným automatem**.

### Odpověď (Back)

Uvažujme nedeterministický konečný automat \(M = (Q, \Sigma, \delta, q_0, F)\). **Jazyk** přijímaný \(M\), zapisujeme jako \(L(M)\), definujeme následovně:

\(L(M) = \{w : w \in \Sigma^* \wedge (q_0, w) \vdash^* (q, \varepsilon) \wedge q \in F\}\).

### Doplňující pole (Extra)

Jazyk přijímaný NKA \(M\) je tedy tvořen všemi řetězci nad abecedou \(\Sigma\), které \(M\) přijímá.

## Poznámka Anki 1664478957465

Karty Anki: 1664478957465
GUID: wG8:X5ZG.5; štítky: bi-aag::p02 bi-spol::01.

Metadata původního zdroje pro kartu 1664478957465: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **dosažitelný a nedosažitelný stav konečného automatu**.

### Odpověď (Back)

Nechť \(M = (Q, \Sigma, \delta, q_0, F)\) je konečný automat. Stav \(q \in Q\) nazveme **dosažitelný** právě tehdy, když 

\(\exists w \in \Sigma^*: (q_0, w) \vdash^* (q, \varepsilon)\).

Stav, který není dosažitelný, nazveme **nedosažitelný.**

### Doplňující pole (Extra)

Dosažitelný stav je tedy takový, pro který v automatu existuje posloupnost přechodů vedoucí z počátečního stavu právě do tohoto stavu.

## Poznámka Anki 1664479133478

Karty Anki: 1664479133478
GUID: G`ls+.@dhg; štítky: bi-aag::p02 bi-spol::01.

Metadata původního zdroje pro kartu 1664479133478: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadaný KA, vrátí ekvivalentní **KA bez nedosažitelných stavů**.

### Odpověď (Back)

**Vstup:** KA \(M = (Q, \Sigma, \delta, q_0, F)\).

**Výstup:** KA \(M^\prime = (Q^\prime, \Sigma, \delta^\prime, q_0, F^\prime)\) bez nedosažitelných stavů ekvivalentní automatu \(M\).

**Postup:**

1. Nalezneme množinu všech dosažitelných stavů pomocí následujícího induktivního předpisu:

1. \(q_0\) je dosažitelný stav.
2. Pokud je stav \(q \in Q\) dosažitelný, poté jsou dosažitelné i všechny stavy \(p\), pro které platí, že \(p \in \delta(q,a)\), kde \(a \in (\Sigma \cup \{\varepsilon\})\).

2. Množinu všech dosažitelných stavů poté prohlásíme za množinu \(Q^\prime\), tedy za množinu stavů automatu \(M^\prime\). 
3. Všechny přechody definované mezi stavy z množiny \(Q^\prime\) v automatu \(M\) překopírujeme do automatu \(M^\prime\). 
4. \(F^\prime = Q^\prime \cap F\).

### Doplňující pole (Extra)

Algoritmicky tuto úlohu vyřešíme tak, že nejprve nalezneme množinu všech dosažitelných stavů. Nedosažitelnými stavy budou poté všechny ty, které v naší množině nebudou. Algoritmus je založen na prohledávání grafu do šířky.

## Poznámka Anki 1664479211595

Karty Anki: 1664479211595
GUID: H3f)x=.^bG; štítky: bi-aag::p02 bi-spol::01.

Metadata původního zdroje pro kartu 1664479211595: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **užitečný a zbytečný stav konečného automatu**.

### Odpověď (Back)

Nechť \(M = (Q, \Sigma, \delta, q_0, F)\) je konečný automat. Stav \(q \in Q\) nazveme **užitečný** právě tehdy, když 

\(\exists w \in \Sigma^*: (q, w) \vdash^* (p, \varepsilon) \wedge p \in F\).

Stav, který není užitečný, nazveme **zbytečný**.

### Doplňující pole (Extra)

Stav nazveme užitečný tedy v případě, že z něj v automatu existuje  posloupnost přechodů vedoucí do některého koncového stavu.

## Poznámka Anki 1664626952943

Karty Anki: 1664626952943
GUID: C:Mj.j|3b*; štítky: bi-aag::p02 bi-spol::01.

Metadata původního zdroje pro kartu 1664626952943: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus odstranění zbytečných stavů z konečného automatu.

### Odpověď (Back)

**Vstup**: KA \(M = (Q, \Sigma, \delta, q_0, F)\).

**Výstup**: KA \(M^\prime = (Q^\prime, \Sigma, \delta^\prime, q_0, F^\prime)\)\) bez zbytečných stavů ekvivalentní automatu \(M\).

Postup:

1. Nalezneme množinu všech užitečných stavů pomocí následujícího induktivního předpisu:

1. \(q \in F\) jsou užitečné stavy.
2. Pokud je stav \(q \in Q\) užitečný, poté jsou užitečné i všechny stavy \(p \in Q\), kde \(q \in \delta(p,a)\) pro libovolný \(a \in (\Sigma \cup \{\varepsilon
\})\). 

2. Množinu všech užitečných stavů poté prohlásíme za množinu \(Q^\prime\), tedy za množinu stavů automatu \(M^\prime\). Pokud navíc \(q_0\) není v \(Q
^\prime\), pak jej tam dodáme.
3. Všechny přechody definované mezi stavy z množiny \(Q^\prime\) v automatu \(M\) překopírujeme do \(M^\prime\).
4. \(F^\prime =
Q^\prime \cap F\).

### Doplňující pole (Extra)

Algoritmicky tuto úlohu vyřešíme tak, že nejprve nalezneme množinu všech užitečných stavů. Zbytečnými stavy budou poté všechny ty, které v naší množině nebudou. Algoritmus je založen na prohledávání grafu do šířky, kdy začínáme ze všech koncových stavů a jdeme proti směru šipek.

## Poznámka Anki 1664627111057

Karty Anki: 1664627111057
GUID: NOs!#RET3E; štítky: bi-aag::p02 bi-spol::01.

Metadata původního zdroje pro kartu 1664627111057: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte nedeterministický konečný automat s \(\varepsilon\)-přechody.

### Odpověď (Back)

**Nedeterministický konečný automat s **\(\varepsilon\)-**přechody** je uspořádaná pětice \((Q, \Sigma, \delta, q_0, F)\), kde

- \(Q, \Sigma, q_0, F\) jsou stejné jako v definici nedeterministického konečného automatu a
- přechodová funkce je definována jako \(\delta : Q \times (\Sigma \cup \{\varepsilon\}) \to \mathcal{P}(Q)\).

### Doplňující pole (Extra)

Význam přechodu ohodnoceného \(\varepsilon\) (též nazývaného \(\varepsilon\)-přechod) je možnost přejít do následujícího stavu či stavů nezávisle na symbolu na vstupu, a tedy i bez jeho čtení. Neformálně si \(\varepsilon\)-přechody můžeme představit jako takové magické teleporty, díky kterým se v automatu můžeme pohybovat mezi stavy, aniž bychom zpracovávali vstup.

## Poznámka Anki 1664627126971

Karty Anki: 1664627126971
GUID: EIAz[Qk+wq; štítky: bi-aag::p02.

Metadata původního zdroje pro kartu 1664627126971: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **přechod** u NKA s \(\varepsilon\)-přechody.

### Odpověď (Back)

Pojem přechod je u NKA s \(\varepsilon\)-přechody definovaný obdobně jako pro NKA s tím rozdílem, že navíc platí, že z konfigurace \((p, u)\) lze přejít do konfigurace \((q, u)\), pokud \(q \in \delta(p, \varepsilon)\), kde \(p,q \in Q\) a \(u \in \Sigma^*\).

## Poznámka Anki 1664627163310

Karty Anki: 1664627163310
GUID: yc=;!)o`)l; štítky: bi-aag::p02 bi-spol::01.

Metadata původního zdroje pro kartu 1664627163310: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte funkci \(\varepsilon\)-closure.

### Odpověď (Back)

Funkce \(\varepsilon\operatorname{-closure}\) pro NKA s \(\varepsilon\)-přechody \(M=(Q,\Sigma,\delta,q_0,F)\) je pro stav \(q \in Q\) definována takto:

\(\varepsilon\operatorname{-closure}(q)=\{p:(q,\varepsilon)\vdash^*(p,\varepsilon)\}.\)

### Doplňující pole (Extra)

\(\varepsilon\operatorname{-closure}\) je funkce, která na vstupu vyžaduje stav automatu, pro nějž vrací množinu všech stavů, které jsou z daného stavu dosažitelné bez nutnosti čtení byť jen jediného vstupního symbolu. Do této množiny tak patří vždy sám stav, pro který \(\varepsilon\operatorname{-closure}\) počítáme, a všechny další, které jsou z tohoto stavu dosažitelné pouze a jenom pomocí \(\varepsilon\)-přechodů (jednoho i více).

## Poznámka Anki 1664627204949

Karty Anki: 1664627204949
GUID: vZRc(4AM=`; štítky: bi-aag::p02.

Metadata původního zdroje pro kartu 1664627204949: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus, který pro zadaný NKA s \(\varepsilon\)-přechody, vrátí ekvivalentní NKA.

### Odpověď (Back)

**Vstup:** NKA s \(\varepsilon\)-přechody \(M_\varepsilon=(Q, \Sigma, \delta_\varepsilon, q_0, F_\varepsilon)\).

**Výstup:** NKA \(M=(Q, \Sigma, \delta, q_0, F)\) tak, že \(L(M) = L(M_\varepsilon)\).

**Postup:**

1. Automat \(M\) má stejnou množinu stavů, stejnou abecedu vstupních symbolů i stejný počáteční stav jako automat \(M_\varepsilon\).
2. Vypočteme funkci \(\varepsilon\operatorname{-closure}\) pro všechny stavy \(q \in Q\).
3. Definujeme zobrazení \(\delta\) pro automat \(M\). Pro všechny \(q \in Q\) a \(a \in \Sigma\), nastavíme \(\delta(q, a) = \bigcup \limits_{p \in \varepsilon\operatorname{-closure}(q)} \delta_\varepsilon(p, a)\).
4. \(F = \{q : q \in Q \land \varepsilon\operatorname{-closure}(q) \cap F_\varepsilon \neq \emptyset\}\). Stav automatu \(M\) je tedy koncový právě tehdy, pokud ve svém \(\varepsilon\operatorname{-closure}\) obsahuje některý z koncových stavů automatu \(M_\varepsilon\).

### Doplňující pole (Extra)

Třetí krok algoritmu nám zjednodušeně říká, že pokud máme například \(\varepsilon\operatorname{-closure}(S) = \{S,A,B\}\), pak všechny přechody ohodnocené symboly abecedy, které vedou ze stavů \(S,A,B\) v automatu \(M_\varepsilon\), povedou také ze stavu \(S\) v automatu \(M\). 

Z čtvrtého kroku poté plyne, že \(F_\varepsilon \subseteq F\).

## Poznámka Anki 1664627253012

Karty Anki: 1664627253012
GUID: LC|(uQU>4G; štítky: bi-aag::p02 bi-spol::01.

Metadata původního zdroje pro kartu 1664627253012: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **nedeterministický konečný automat s více počátečními stavy**.

### Odpověď (Back)

**Nedeterministický konečný automat s více počátečními stavy** definujeme jako uspořádanou pětici \((Q, \Sigma, \delta, I, F)\) následovně:

- \(Q, \Sigma, \delta, F\) jsou stejné jako v definici nedeterministického konečného automatu,
- \(I \subseteq Q\) je konečná neprázdná množina počátečních stavů.

### Doplňující pole (Extra)

NKA s více počátečními stavy se od NKA tedy liší pouze tím, že může mít více počátečních konfigurací. Každá konfigurace \((q, w)\), kde \(q \in I\) a \(w \in \Sigma^*\) je vstupní řetězec, je počáteční konfigurací.

## Poznámka Anki 1664627304945

Karty Anki: 1664627304945
GUID: t=/<9g/?{f; štítky: bi-aag::p02.

Metadata původního zdroje pro kartu 1664627304945: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište **algoritmus**, který pro zadaný NKA s více počátečními stavy, vrátí ekvivalentní NKA s \(\varepsilon\)-přechody.

### Odpověď (Back)

**Vstup:** NKA s více počátečními stavy \(M = (Q, \Sigma, \delta, I, F)\).

**Výstup:** NKA s \(\varepsilon\)-přechody \(M^\prime = (Q^\prime, \Sigma, \delta^\prime, q_0, F)\) takový, že \(L(M) = L(M^\prime)\).

**Postup:**

1. \(Q^\prime = Q \cup \{q_0\}\), kde \(q_0 \notin Q\). Jinými slovy, přidáme nový stav, který bude v \(M^\prime\) počátečním stavem.
2. Všechny přechody definované v automatu \(M\) překopírujeme k odpovídajícím stavům i do automatu \(M^\prime\).

3. \(\delta^\prime(q_0, \varepsilon) = I\) (z \(q_0\) povedeme \(\varepsilon\)-přechody do všech stavů, které v \(M\) byly počáteční).

## Poznámka Anki 1664644329866

Karty Anki: 1664644329867
GUID: FEWfYwSR]R; štítky: bi-aag::p02.

Metadata původního zdroje pro kartu 1664644329867: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte řetězec přijímaný NKA s \(\varepsilon\)-přechody.

### Odpověď (Back)

Řetězec přijímaný NKA s \(\varepsilon\)-přechody definujeme stejně jako řetězec přijímaný NKA. Řetězec je tedy přijat NKA s \(\varepsilon\)-přechody, existuje-li posloupnost přechodů vedoucí z počáteční konfigurace do koncové. U NKA s \(\varepsilon\)-přechody může ale nastat situace, kdy se po přečtení řetězce ocitneme v nekoncovém stavu, ale z něj ještě vede posloupnost \(\varepsilon\)-přechodů do některého z koncových stavů. V takovém případě tedy existuje posloupnost přechodů vedoucí z počáteční konfigurace do koncové a takový řetězec je tedy přijat.

