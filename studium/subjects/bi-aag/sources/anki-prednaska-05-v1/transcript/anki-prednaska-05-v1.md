# BI-AAG – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aag/BI-AAG.apkg; APKG SHA-256 0383847389324f3b83b349363b7ad16a6bf91673c90b7a96ed1a57b25a85f8af. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b9cda20d5a5a9d1ff47d4e1fc58b10ed3ac7a37c72c6c1431cc7cb67e2ca10c.
Původní balíčky: BI-AAG
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1666535082553

Karty Anki: 1666535082556
GUID: J&`Xn2Oqme; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666535082556: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus zvaný **metoda derivací**, který pro regulární výraz \(V\) vrátí konečný automat \(M\) tak, že \(L(M) = h(V)\).

### Odpověď (Back)

**Vstup:** Regulární výraz \(V\) nad abecedou \(\Sigma\).

**Výstup:** Úplně určený DKA \(M\) takový, že \(L(M) = h(V)\).

**Postup:**

1. Původní regulární výraz označíme \(V_0\) a prohlásíme jej za počáteční stav.
2. Výraz \(V_0\) zderivujeme postupně dle všech symbolů abecedy \(\Sigma\), čímž mohou vzniknout nové výrazy (tj. nové stavy). Pokud například \(\frac{\mathrm{d}V_0}{\mathrm{d}\mathtt{a}} = V_1\), poté: 

1. pokud mezi aktuálními stavy neexistuje regulární výraz \(V_i\) podobný regulárnímu výrazu \(V_1\), vytvoříme nový stav \(V_1\) a v automatu přidáme přechod ze stavu \(V_0\) na symbol \(\mathtt{a}\) do stavu \(V_1\).

2. pokud mezi aktuálními stavy existuje regulární výraz \(V_i\) podobný regulárnímu výrazu \(V_1\), nový stav nevytváříme a v automatu přidáme přechod ze stavu \(V_0\) na symbol \(\mathtt{a}\) do stavu \(V_i\).

3. Pokud v automatu existuje stav, který nemá definován přechody pro všechny symboly abecedy, poté pro odpovídající regulární výraz aplikujeme stejný postup jako pro regulární výraz \(V_0\) ve druhém kroku.
4. Pokud \(\varepsilon \in h(V)\) pro nějaký regulární výraz \(V\), pak tomuto výrazu odpovídající stav je vždy koncový.

### Doplňující pole (Extra)

Výstupem metody derivací je tedy vždy úplně určený DKA. Tento automat však nemusí být nutně minimální. Automat by byl minimální v případě, pokud bychom místo podobných výrazů hledali ekvivalentní. Problém však je, že existují regulární výrazy, jejichž ekvivalenci nejde rozhodnout na základě algebraických úprav. Proto se v metodě derivací využívá podobnost.

## Poznámka Anki 1666535114922

Karty Anki: 1666535114922
GUID: kNIqe)Wc0; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666535114922: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus zvaný **metoda sousedů**, který pro regulární výraz \(V\) vrátí konečný automat \(M\) tak, že \(L(M) = h(V)\).

### Odpověď (Back)

**Vstup:** Regulární výraz \(V\) nad abecedou \(\Sigma\).

**Výstup:** Homogenní konečný automat \(M\) takový, že \(L(M) = h(V)\).

**Postup:**

1. Pro regulární výraz \(V\) vytvoříme očíslovaný regulární výraz \(V'\), kde jednotlivé symboly z abecedy \(\Sigma\) ve \(V\) zleva doprava unikátně očíslujeme — např. pro \(V = \mathtt{aab} + \varepsilon + \emptyset\) vytvoříme \(V^\prime = \mathtt{a}_1\mathtt{a}_2\mathtt{b}_3 + \varepsilon + \emptyset\).
2. Vytvoříme následující množiny:

- \(Z\) (množina počátečních symbolů), která obsahuje všechny očíslované symboly, jimiž mohou očíslované řetězce z jazyka \(h(V')\) začínat.
- \(F\) (množina koncových symbolů), která obsahuje všechny očíslované symboly, jimiž mohou očíslované řetězce z jazyka \(h(V')\) končit.
- \(P\) (množina sousedů), která obsahuje všechny dvojice očíslovaných symbolů, jež se mohou v očíslovaných řetězcích z jazyka \(h(V')\) vyskytnout vedle sebe.

3. Zkonstruujeme KA pro daný regulární výraz:

1. Každý očíslovaný symbol v regulárním výrazu \(V'\) představuje jeden stav automatu. Navíc do automatu přidáme nový stav \(q_0\), který bude počáteční a který neodpovídá žádnému očíslovanému symbolu.

2. Jednotlivé symboly v rámci množiny \(F\) reprezentují koncové stavy. A pokud platí, že \(\varepsilon \in h(V)\), pak \(q_0\) bude též koncovým stavem.
3. Z počátečního stavu \(q_0\) vedeme přechody do stavů, které reprezentují očíslované symboly v množině \(Z\). Tyto přechody ohodnotíme symbolem, který vznikne po odstranění číselného indexu z názvu cílového stavu. Například pro \(Z = \{\mathtt{a}_1, \mathtt{b}_3\}\) povedeme přechody z \(q_0\) na symbol \(\mathtt{a}\) do stavu \(\mathtt{a}_1\) a na symbol \(\mathtt{b}\) do stavu \(\mathtt{b}_3\).
4. Pomocí množiny sousedů přidáme zbylé přechody. Pro danou dvojici sousedů vytvoříme přechod tak, že jej vedeme ze stavu, jenž reprezentuje levý symbol dvojice, do stavu, jenž reprezentuje pravý symbol dvojice. Tento přechod označíme symbolem, který vznikne po odstranění číselného indexu z názvu cílového stavu. Například pro \(\mathtt{b}_1\mathtt{a}_3\) přidáme přechod ze stavu \(\mathtt{b}_1\) na symbol \(\mathtt{a}\) do stavu \(\mathtt{a}_3\).

### Doplňující pole (Extra)

Výsledkem metody sousedů je nedeterministický konečný automat, má tedy vždy pouze jeden počáteční stav a nemá \(\varepsilon\)-přechody. Tento automat je navíc homogenní. V ojedinělých případech může být výsledný automat i deterministický, například pokud bychom převáděli regulární výraz \(V = \mathtt{a}\).

Pozor! Všimněte si, že u metody sousedů číslujeme pouze symboly abecedy, tedy \(\varepsilon\) ani \(\emptyset\) nečíslujeme.

## Poznámka Anki 1666535308734

Karty Anki: 1666535308734
GUID: if,(5jOFR*; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666535308734: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus zvaný **metoda postupnou konstrukcí**, který pro regulární výraz \(V\) vrátí konečný automat \(M\) tak, že \(L(M) = h(V)\).

### Odpověď (Back)

**Vstup:** Regulární výraz \(V\) nad abecedou \(\Sigma\).

**Výstup:** Konečný automat \(M\) takový, že \(L(M) = h(V)\).

**Postup:**

1. Sestavíme konečné automaty přijímající jednotlivé elementární regulární výrazy vyskytující se v daném výrazu
 [Obrázek: paste-67195ab21a0d6043116b2cde9ce19419df5e32b0.jpg; soubor je v media/ v doprovodném ZIP] 
2. Tyto elementární automaty skládáme do větších celků tvořících daný regulární výraz, a to dle následujícího principu

 [Obrázek: paste-88d1b58c5bce14063af754ef6b0463795a71b68b.jpg; soubor je v media/ v doprovodném ZIP]

### Doplňující pole (Extra)

Výsledkem metody postupnou konstrukcí je v obecném případě nedeterministický konečný automat s \(\varepsilon\)-přechody. Tento automat má tedy vždy pouze jeden počáteční stav. Všimněte si, že každý výsledný automat má navíc také právě jeden koncový stav. Zároveň z koncového stavu nevychází žádná hrana, stejně tak jako žádná hrana nevstupuje do počátečního stavu.

V ojedinělých případech může být výsledkem metody postupnou konstrukcí i NKA (tj. bez \(\varepsilon\)-přechodů) nebo dokonce DKA.

## Poznámka Anki 1666535386075

Karty Anki: 1666535386075
GUID: Kbv]qRi+7>; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666535386075: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus zvaný **metoda pravých regulárních rovnic (odchozí přechody)**, který pro NKA \(M\) vrátí regulární výraz \(V\) takový, že \(h(V) = L(M)\).

### Odpověď (Back)

**Vstup:** Nedeterministický konečný automat \(M = (Q, \Sigma, \delta, q_0, F)\).

**Výstup:** Regulární výraz \(V\) takový, že \(h(V)= L(M)\).

**Postup:**

1. Každý stav \(q \in Q\) prohlásíme za neznámou v soustavě regulárních rovnic. 
2. Pro každou neznámou sestavíme odpovídající pravou regulární rovnici tím, že sledujeme odchozí přechody z příslušného stavu. Každá odchozí hrana znamená jeden separátní výraz na pravé straně rovnice. Například pokud ze stavu \(A\) vede odchozí hrana označená symbolem \(\mathtt{0}\) do stavu \(B\), pak do rovnice pro neznámou \(A\) přidáme na pravou stranu výraz \(\mathtt{0}B\). Všechny takto vzniklé výrazy na pravé straně rovnice sjednotíme (operace +). [Obrázek: paste-27b8d7976c450bc7a4fdc43e9812d6131aa6da79.jpg; soubor je v media/ v doprovodném ZIP] 
3. Do všech rovnic pro neznámé reprezentující koncové stavy přidáme na pravou stranu „\(+\varepsilon\)“.
4. Soustavu rovnic vyřešíme pro neznámou reprezentující počáteční stav \(q_0\).

## Poznámka Anki 1666535421544

Karty Anki: 1666535421544
GUID: O5[.%z%qSC; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666535421544: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus zvaný **metoda levých regulárních rovnic (příchozí přechody)**, který pro NKA \(M\) vrátí regulární výraz \(V\) takový, že \(h(V) = L(M)\).

### Odpověď (Back)

**Vstup:** Nedeterministický konečný automat \(M = (Q, \Sigma, \delta, q_0, F)\).

**Výstup:** Regulární výraz \(V\) takový, že \(h(V)= L(M)\).

**Postup:**

1. Každý stav \(q \in Q\) prohlásíme za neznámou v soustavě regulárních rovnic. 
2. Pro každou neznámou sestavíme odpovídající levou regulární rovnici tím, že sledujeme příchozí přechody do příslušného stavu. Každá příchozí hrana znamená jeden separátní výraz na pravé straně rovnice. Například pokud do stavu \(A\) vede příchozí hrana označená symbolem \(\mathtt{0}\) ze stavu \(B\), pak do rovnice pro neznámou \(A\) přidáme na pravou stranu výraz \(B\mathtt{0}\). Všechny takto vzniklé výrazy na pravé straně rovnice sjednotíme (operace +).     [Obrázek: paste-9e9308aab4f8bce74dc347c59f27972c37fa61b5.jpg; soubor je v media/ v doprovodném ZIP] 
3. Do rovnice pro neznámou reprezentující počáteční stav přidáme na pravou stranu „\(+\varepsilon\)“.
4. Tuto soustavu rovnic standardně vyřešíme. Výsledný regulární výraz \(V\) je poté alternativou regulárních výrazů, které jsou řešením všech neznámých, jež odpovídají koncovým stavům automatu \(M\).

## Poznámka Anki 1666535545730

Karty Anki: 1666535545731
GUID: EHw^hzSb~(; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666535545731: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus zvaný **metoda eliminací stavů**, který pro konečný automat \(M\) vrátí regulární výraz \(V\) takový, že \(h(V) = L(M)\).

### Odpověď (Back)

**Vstup:** Konečný automat \(M = (Q, \Sigma, \delta, q_0, F)\).

**Výstup:** Regulární výraz \(V\) takový, že \(h(V)= L(M)\).

**Postup:**

1. (počáteční stav) Pokud \(q_0\) není koncový stav a zároveň do něj nevedou žádné příchozí přechody, poté jej přejmenujeme na \(q_s\) (předpokládáme, že \(q_s \notin Q\)). V opačném případě (tedy pokud je počáteční stav \(q_0\) zároveň koncový nebo do něj vedou nějaké příchozí příchody), do automatu přidáme nový počáteční stav \(q_s\) (předpokládáme, že původně \(q_s \notin Q\)). Zároveň přidáme \(\varepsilon\)-přechod z \(q_s\) do \(q_0\) a \(q_0\) již nebude počátečním stavem.   
2. (koncový stav) Pokud existuje právě jeden koncový stav \(q \in F\), pak jej přejmenujeme na \(q_f\). V opačném případě (tedy pokud existuje více než jeden koncový stav), do automatu přidáme nový koncový stav \(q_f\) (předpokládáme, že původně \(q_f \notin Q\)). Původní koncové stavy již koncové nebudou a z každého z nich povedeme \(\varepsilon\)-přechod do \(q_f\).
3. (sloučení multihran) Zajistíme, že pro všechny stavy \(p,q \in Q\) (přičemž může platit \(p = q\)) existuje nejvýše jeden přechod vedoucí z \(p\) do \(q\). Tohoto stavu docílíme následovně:
 [Obrázek: paste-52baff071fd47daf8ee5ab051eb01c02b06a8b73.jpg; soubor je v media/ v doprovodném ZIP]    
4. (eliminace stavů) Nyní budeme v libovolném pořadí eliminovat stavy, dokud v \(M\) nezbudou pouze stavy \(q_s\) a \(q_f\). V průběhu eliminace průběžně slučujeme multihrany — tj. zajišťujeme, že pro všechny stavy \(p,q \in Q\) (přičemž může platit \(p = q\)) existuje nejvýše jeden přechod vedoucí z \(p\) do \(q\). Stav \(v \in Q\) eliminujeme za pomoci následujícího principu:   
   [Obrázek: paste-cf973b50850d126ca54c29f85449a37a42c96f43.jpg; soubor je v media/ v doprovodném ZIP]    
5. Tímto způsobem zpracujeme všechny možné dvojice stavů \(u, w \in Q\) (kde \(u,w \neq v\)). Přičemž se může stát, že \(u = w\). Jinými slovy, pokud má eliminovaný stav \(v\) více příchozích/odchozích přechodů, pak při eliminaci musíme zvážit kombinaci každého příchozího přechodu do \(v\) s každým odchozím přechodem z \(v\).
6. (výsledný regulární výraz) Jakmile v automatu zbyly pouze stavy \(q_s\) a \(q_f\) výsledný regulární výraz \(V\) získáme následovně:

 [Obrázek: paste-65e090808cbf0b3cf364dd436d7a6be7221c9394.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1666535693719

Karty Anki: 1666535693719
GUID: rEGaSQC,#=; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666535693719: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus zvaný **metoda pravých regulárních rovnic**, který regulární gramatiku \(G\) vrátí regulární výraz \(V\) takový, že \(L(G) = h(V)\).

### Odpověď (Back)

**Vstup:** Regulární gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Regulární výraz \(V\) takový, že \(h(V)= L(G)\).

**Postup:**

1. Z gramatiky \(G\) vytvoříme soustavu pravých regulárních rovnic. Neformálně řečeno v pravidlech gramatiky zaměníme „|“ za „+“ a „\(\to\)“ za „=“.   
 [Obrázek: paste-04462a8442ae9e813a36af3da5ebfbe7937b3816.jpg; soubor je v media/ v doprovodném ZIP]   
2. Soustavu rovnic vyřešíme pro neznámou reprezentující počáteční neterminál \(S\). Toto řešení poté odpovídá hledanému regulárnímu výrazu \(V\).

## Poznámka Anki 1666535732801

Karty Anki: 1666535732801
GUID: xC`%NfVrNp; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666535732801: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus zvaný **metoda eliminací neterminálních symbolů**, který regulární gramatiku \(G\) vrátí regulární výraz \(V\) takový, že \(L(G) = h(V)\).

### Odpověď (Back)

**Vstup:** Regulární gramatika \(G = (N, \Sigma, P, S)\).

**Výstup:** Regulární výraz \(V\) takový, že \(h(V) = L(G)\).  

**Postup:**

1. (nové neterminální symboly) Do gramatiky přidáme nové neterminály \(S^\prime\) a \(F^\prime\) (předpokládáme, že původně \(S^\prime, F^\prime \notin N\)). Dále přidáme pravidla \(S^\prime \to \varepsilon S\) a \(F^\prime \to \varepsilon\). Neterminál \(S^\prime\) je nový počáteční neterminál a \(S\) je původní počáteční neterminál.
2. (nová pravidla) Všechny pravé strany pravidel, které neobsahují neterminální symboly, zřetězíme zprava s neterminálem \(F^\prime\) (kromě pravidla \(F^\prime \to \varepsilon\)). Například \(S \to \mathtt{1}\) zaměníme za \(S \to \mathtt{1}F^\prime\).
3. (sloučení pravidel) Zajistíme, že pro všechny neterminály \(A,B \in N\) (přičemž může platit \(A = B\)) existuje nejvýše jedno pravidlo \(A \to \alpha B\), kde \(\alpha\) je RV nad abecedou \(\Sigma\). Jinými slovy, \(n\)-tice pravidel \(A \to \alpha_1 B\), \(A \to \alpha_2 B\), \(\dots\), \(A \to \alpha_n B\) (kde \(A,B \in N\) a \(\alpha_1, \alpha_2, \dots, \alpha_n\) jsou RV) nahradíme pravidlem \(A \to (\alpha_1 + \alpha_2 + \dots + \alpha_n)B\). Například \(S \to \mathtt{1}B \mid \mathtt{2}B \mid \mathtt{0}B\) nahradíme za \(S \to (\mathtt{1} + \mathtt{2} + \mathtt{0})B\).
4. (eliminace neterminálů) Nyní budeme v libovolném pořadí eliminovat neterminály, dokud v \(G\) nezbudou pouze neterminály \(S^\prime\) a \(F^\prime\). V průběhu eliminace průběžně slučujeme pravidla dle principu uvedeného v předchozím kroku. Neterminál \(A \in N\) eliminujeme za pomoci následujícího principu:

1. Vyřešíme regulární rovnici odpovídající odstraňovanému neterminálu. Například pokud \(A \to (\mathtt{1} + \mathtt{21}^*)B \mid \mathtt{1}F'\), pak \(A = (\mathtt{1} + \mathtt{21}^*)B + \mathtt{1}F'\). 

2. Ve zbývajících pravidlech vyhledáme ta, která náš odstraňovaný neterminál na pravé straně používají. Tento neterminál nahradíme příslušným regulárním výrazem. Pokud ovšem pro eliminovaný neterminál \(A\) platí, že \(A = \emptyset\), poté \(A\) v pravidlech nenahrazujeme, ale všechna pravidla obsahující \(A\) z gramatiky odstraníme.

5. (výsledný regulární výraz) Jakmile v gramatice zbyly pouze neterminály \(S^\prime\) a \(F^\prime\) s pravidly \(S \to \alpha F^\prime\) a \(F^\prime \to \varepsilon\), poté \(V = \alpha\).

### Doplňující pole (Extra)

Tato metoda je podobná metodě eliminací stavů. Postupujeme tak, že z gramatiky postupně vylučujeme neterminální symboly a nahrazujeme je regulárními výrazy.

## Poznámka Anki 1666535791812

Karty Anki: 1666535791812
GUID: v_J)x`,gx+; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666535791812: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus zvaný **metoda derivací**, který pro regulární výraz \(V\) vrátí regulární gramatiku \(G\) tak, že \(L(G) = h(V)\).

### Odpověď (Back)

**Vstup:** Regulární výraz \(V\).

**Výstup:** Regulární gramatika \(G\) taková, že \(L(G) = h(V)\).

**Postup:**

1. Původní regulární výraz označíme \(V_0\) a prohlásíme jej za počáteční neterminál gramatiky.
2. Výraz \(V_0\) zderivujeme postupně dle všech symbolů abecedy, čímž mohou vzniknout nové výrazy (tj. nové neterminální symboly). Pokud například \(\frac{\mathrm{d}V_0}{\mathrm{d}\mathtt{a}} = V_1\), poté: 

1. pokud mezi aktuálními neterminály neexistuje regulární výraz \(V_i\) podobný regulárnímu výrazu \(V_1\), vytvoříme nový neterminál \(V_1\) a v gramatice přidáme pravidlo \(V_0 \to \mathtt{a}V_1\). Pokud navíc \(\varepsilon \in h(V_1)\), přidáme též pravidlo \(V_0 \to \mathtt{a}\).

2. pokud mezi aktuálními neterminály existuje regulární výraz \(V_i\) podobný regulárnímu výrazu \(V_1\), nový neterminál nevytváříme a v gramatice přidáme pravidlo \(V_0 \to \mathtt{a}V_i\). Pokud navíc \(\varepsilon \in h(V_i)\), přidáme též pravidlo \(V_0 \to \mathtt{a}\).

3. Pokud v gramatice existuje neterminální symbol, kde odpovídající regulární výraz nebyl zderivován postupně pro všechny symboly abecedy, aplikujeme pro tento výraz stejný postup jako pro regulární výraz \(V_0\) v předchozím kroku.
4. Pokud \(\varepsilon \in h(V_0)\), k počátečnímu neterminálu \(V_0\) přidáme \(\varepsilon\)-pravidlo a zkontrolujeme, zdali se počáteční neterminál nevyskytuje též na pravé straně. Pokud ano, musíme gramatiku následovně upravit: Vytvoříme nový startovací neterminál \(S'\) s pravidlem \(S' \to \varepsilon\). U původního startovacího neterminálu \(\varepsilon\)-pravidlo odstraníme. Všechny pravé strany pravidel pro původní startovací neterminál přidáme též k neterminálu \(S'\).

## Poznámka Anki 1666535839358

Karty Anki: 1666535839358
GUID: fV:>q[j%r9; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666535839358: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus zvaný **metoda postupnou konstrukcí**, který pro regulární výraz \(V\) vrátí regulární gramatiku \(G\) tak, že \(L(G) = h(V)\).

### Odpověď (Back)

**Vstup:** Regulární výraz \(V\) nad abecedou \(\Sigma\).

**Výstup:** Regulární gramatika \(G\) taková, že \(L(G) = h(V)\).

**Postup:**

1. Sestavíme gramatiky generující jednotlivé elementární regulární výrazy vyskytující se ve \(V\):

- \(G_\varepsilon = (\{S\},\Sigma,\{S \to \varepsilon\}, S)\), tedy \(L(G) = \{\varepsilon\}\). 
- \(G_\emptyset = (\{S\},\Sigma,\emptyset, S)\), tedy \(L(G) = \emptyset\).
- \(G_\mathtt{a} = (\{S\},\Sigma,\{S \to \mathtt{a}\}, S)\), tedy \(L(G) = \{\mathtt{a}\}\).

2. Postupně tyto elementární gramatiky skládáme do větších celků, které jsou součástí \(V\), a to dle algoritmů pro skládání regulárních gramatik.

## Poznámka Anki 1666538383548

Karty Anki: 1666538383549
GUID: I5JO$ug^$%; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666538383549: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus **sjednocení** **regulárních** gramatik.

### Odpověď (Back)

**Vstup: **Regulární gramatiky** **\(G_1 = (N_1, \Sigma, P_1, S_1)\) a \(G_2 = (N_2, \Sigma, P_2, S_2)\) tak, že \(N_1 \cap N_2 = \emptyset\).**

Výstup: **Regulární gramatika \(G = (N, \Sigma, P, S)\) generující jazyk \(L = L(G_1) \cup L(G_2)\).**

Postup:**

1. \(N = N_1 \cup N_2 \cup \{S\}\), předpokládáme, že původně \(S \notin (N_1 \cup N_2)\).

2. \(P = P_1 \cup P_2 \cup \{S \to X_1 \mid X_2 \mid \dots \mid X_n\} \setminus \{S_1 \to \varepsilon, S_2 \to \varepsilon\}\), kde \(X_1, X_2, \dots, X_n\) jsou všechny pravé strany pravidel pro neterminály \(S_1\) a \(S_2\).

## Poznámka Anki 1666538449744

Karty Anki: 1666538449744
GUID: ha*Wv1eHdZ; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666538449744: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus **iterace regulární** gramatiky.

### Odpověď (Back)

**Vstup: **Regulární gramatika** **\(G_1 = (N_1, \Sigma, P_1, S_1)\) 

**Výstup: **Regulární gramatika \(G = (N, \Sigma, P, S)\) generující jazyk \(L = L(G_1)^*\)**

Postup:**

1. \(N = N_1 \cup \{S\}\), předpokládáme, že původně \(S \notin N\).

2. Do množiny přepisovacích pravidel \(P\) přidáme:

1. Všechna pravidla z množiny \(P_1\) ve tvaru \(A \to a\) nebo \(A \to aB\) (\(A,B \in N\), \(a \in \Sigma\)),
2. Všechna pravidla ve tvaru \(A \to aS_1\) (\(A \in N, a \in \Sigma\)), kde pravidlo \((A \to a) \in P_1\).
3. Pravidla \(S \to \varepsilon \mid X_1 \mid \dots \mid X_n\), kde \(X_1, \dots, X_n\) jsou všechny pravé strany neterminálu \(S_1\) v gramatice \(G_1\).
4. Pro všechna pravidla v \(G_1\) tvaru \(S_1 \to a\), kde \(a \in \Sigma\), přidáme do \(G\) pravidlo \(S \to a S_1\).

## Poznámka Anki 1666538464732

Karty Anki: 1666538464732
GUID: wtXK+f%)|c; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1666538464732: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus **zřetězení (součin) regulárních** gramatik.

### Odpověď (Back)

**Vstup: **Regulární gramatiky** **\(G_1 = (N_1, \Sigma, P_1, S_1)\) a \(G_2 = (N_2, \Sigma, P_2, S_2)\) tak, že \(N_1 \cap N_2 = \emptyset\).**

Výstup: **Regulární gramatika \(G = (N, \Sigma, P, S)\) generující jazyk \(L = L(G_1) \cdot L(G_2)\).

**Postup:**

1. \(N = N_1 \cup N_2\).
2. Počáteční neterminál gramatiky \(G\) bude \(S_1\).
3. Do množiny přepisovacích pravidel \(P\) přidáme:

1. Všechna pravidla z množin \(P_1, P_2\) ve tvaru \(A \to aB\) (\(A,B \in N\), \(a \in \Sigma\)).
2. Všechna pravidla z množiny \(P_2\) ve tvaru \(A \to a\) (\(A \in N_2\), \(a \in \Sigma\)).
3. Všechna pravidla ve tvaru \(A \to aS_2\) (\(A \in N_1\), \(a \in \Sigma\)), kde pravidlo \((A \to a) \in P_1\).
4. Pokud gramatika \(G_2\) obsahuje pravidlo \(S_2 \to \varepsilon\), pak přidáme všechna pravidla ve tvaru \(A \to a\) (\(A \in N_1, a \in \Sigma\)), kde pravidlo \((A \to a) \in P_1\).
5. Pokud gramatika \(G_1\) obsahuje pravidlo \(S_1 \to \varepsilon\), pak do gramatiky \(G\) přidáme navíc k počátečnímu neterminálu \(S\) všechny pravé strany neterminálu \(S_2\) z gramatiky \(G_2\).

## Poznámka Anki 1672759664963

Karty Anki: 1672759664963
GUID: k#`}e`0d`f; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1672759664963: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je výsledkem **metody sousedů** (Glushkov)?

### Odpověď (Back)

Výsledkem metody sousedů je homogenní NKA bez \(\varepsilon\)-přechodů, v ojedinělých případech DKA.

## Poznámka Anki 1672759824313

Karty Anki: 1672759824313
GUID: tb>+KR/(>h; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1672759824313: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je výsledkem **metody postupnou konstrukcí** (Thompson)?

### Odpověď (Back)

Výsledkem metody postupnou konstrukcí je NKA s \(\varepsilon\)-přechody. Má právě jeden koncový stav, ze kterého nevychází ani jedna hrana. Nápodobně do počátečního stavu žádné hrany nevstupují. V ojedinělých případech může být výsledkem NKA bez \(\varepsilon\)-přechodů nebo DKA.

## Poznámka Anki 1672759922474

Karty Anki: 1672759922474
GUID: lYI{n>1mY@; štítky: bi-aag::p05.

Metadata původního zdroje pro kartu 1672759922474: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je výsledkem **metody derivací** převodu regulárního výrazu na KA (Brzozowski)?

### Odpověď (Back)

Výsledkem metody derivací je vždy úplně určený DKA.

