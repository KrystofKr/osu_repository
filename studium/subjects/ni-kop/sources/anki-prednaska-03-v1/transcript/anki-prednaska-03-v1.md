# NI-KOP – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1728039785865

Karty Anki: 1728039785865
GUID: PU|-JF+=f>; štítky: ni-kop::p03.

Metadata původního zdroje pro kartu 1728039785865: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

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

## Poznámka Anki 1728039801302

Karty Anki: 1728039801302
GUID: vz5!DlDFLb; štítky: ni-kop::p03.

Metadata původního zdroje pro kartu 1728039801302: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **nedeterministický Turingův stroj**.

### Odpověď (Back)

**Nedeterministický Turingův stroj** (NTS) definujeme jako uspořádanou sedmici \(R = (Q, \Sigma, G, \delta, q_0, \mathtt{B}, F)\), kde

- \(Q, \Sigma, G, q_0, \mathtt{B}, F\) jsou definovány stejně jako u DTS,
- přechodová funkce je definována jako \(\delta : (Q \setminus F) \times G \to \mathcal{P}(Q \times G \times \{-1,0,1\})\).

### Doplňující pole (Extra)

Výsledkem přechodové funkce \(\delta\) u NTS je tedy množina trojic \((p,a,d)\), kde \(p \in Q, a \in G, d \in \{-1,0,1\}\). Tato množina může být i prázdná. Stejně tak zobrazení \(\delta\) pro nějaký stav a symbol nemusí být definováno vůbec, v praktické rovině se však tento případ neliší od předchozího. 

NTS jenž má zobrazení \(\delta\) definované pro všechny dvojice nekoncových stavů a symbolů z pracovní abecedy, kde zároveň platí, že výsledkem je vždy neprázdná množina, nazveme **úplně určený NTS**.

## Poznámka Anki 1728040061137

Karty Anki: 1728040061137
GUID: OSF|?HJ/)X; štítky: ni-kop::p03 ni-spol::11.

### Otázka (Front)

Definujte řešení rozhodovacího problému deterministickým Turingovým strojem.

### Odpověď (Back)

Program \(M\) pro deterministický Turingův stroj řeší rozhodovací problém \(\Pi\) v čase \(t\) s pamětí \(m\), jestliže se výpočet zastaví po nejvýše \(t\) krocích a počet použitých políček na pásce Turingova stroje je nejvýše \(m\) pro každou instanci problému \(\Pi\).

## Poznámka Anki 1728040328820

Karty Anki: 1728040328820
GUID: L9Kr#4-qNl; štítky: ni-kop::p03 ni-spol::11.

### Otázka (Front)

Definujte třídu \(\text P\). Jaký je její vztah k třídám \(\text{NP}\) a \(\text{co-NP}\)?

### Odpověď (Back)

Rozhodovací problém patří do třídy \(\text P\), jestliže pro něj existuje program pro deterministický Turingův stroj, který jej řeší v čase \(\mathcal O(n^k)\), kde \(n\) je velikost instance a \(k\) konečné číslo. Platí, že \(\text P \subseteq \text{NP}\) a \(\text P \subseteq \text{NP} \cap \text{co-NP}\).

## Poznámka Anki 1728040430132

Karty Anki: 1728040430132
GUID: FH6gV^SE}$; štítky: ni-kop::p03 ni-spol::11.

### Otázka (Front)

Definujte třídu \(\text{PSPACE}\). Jaký je její vztah k třídám \(\text{EXPTIME}\) a \(\text{NP}\)?

### Odpověď (Back)

Rozhodovací problém patří do třídy \(\text{PSPACE}\), jesliže pro něj existuje program pro deteriministický Turingův stroj, který jej řeší v paměti \(\mathcal O(n^k)\), kde \(n\) je velikost instance a \(k\) konečné číslo. Platí, že \(\text{NP} \subset \text{PSPACE} \subset \text{EXPTIME}\).

## Poznámka Anki 1728040521121

Karty Anki: 1728040521121
GUID: n[2S5EDao+; štítky: ni-kop::p03 ni-spol::11.

### Otázka (Front)

Definujte třídu \(\text{EXPTIME}\). Jaký je její vztah k třídě \(\text{PSPACE}\)?

### Odpověď (Back)

Rozhodovací problém patří do třídy \(\text{EXPTIME}\), jestliže pro něj existuje program pro deterministický Turingův stroj, který jej řeší v čase \(\mathcal O(2^{P(n)})\), kde \(P(n)\) je polynom závislý na velikosti instance \(n\). Platí, že \(\text{EXPTIME} \supset \text{PSPACE}\).

## Poznámka Anki 1728040809193

Karty Anki: 1728040809194
GUID: c61Ybz|i}.; štítky: ni-kop::p03 ni-spol::11.

### Otázka (Front)

Definujte řešení rozhodovacího problému nedeterministickým Turingovým strojem.

### Odpověď (Back)

Program \(M\) pro nedeterministický Turingův stroj řeší rozhodovací problém \(\Pi\) v čase \(t\), jestliže se výpočet zastaví nejvýše po \(t\) krocích pro každou instanci \(I \in \Pi_\mathtt{ano}\) problému \(\Pi\).

### Doplňující pole (Extra)

Množina \(\Pi_\texttt{ano}\) je množina všech instancí problému \(\Pi\), které mají výstup \(\texttt{ano}\). Podobně \(\Pi_\texttt{ne}\) je množina instancí problému \(\Pi\), jejichž výstup je \(\texttt{ne}\).

## Poznámka Anki 1728040894743

Karty Anki: 1728040894743
GUID: J/,+*c~eP_; štítky: ni-kop::p03.

### Otázka (Front)

Vyslovte větu o exponenciální mezeře (exponential gap).

### Odpověď (Back)

Jestliže nedeterministický Turingův stroj řeší problém \(\Pi\) v čase \(T(n)\), pak deterministický Turingův stroj řeší \(\Pi\) v čase \(2^{\mathcal O \big (T(n) \big)}\).

## Poznámka Anki 1728041011362

Karty Anki: 1728041011362
GUID: IDN!=rZLA!; štítky: ni-kop::p03 ni-spol::11.

### Otázka (Front)

Definujte třídu \(\text{NP}\) pomocí nedeterministického Turingova stroje. Jaký je její vztah k třídám \(\text{PSPACE}\) a \(\text P\)?

### Odpověď (Back)

Rozhodovací problém \(\Pi\) patří do třídy \(\text{NP}\), jestliže pro něj existuje program pro nedeterministický Turingův stroj, který každou instanci \(I \in \Pi_\texttt{ano}\) problému \(\Pi\) řeší v čase \(\mathcal O(n^k)\), kde \(n\) je velikost instance a \(k\) konečné číslo. Platí, že \(\text P \subseteq \text{NP} \subset \text{PSPACE}\).

### Doplňující pole (Extra)

Množina \(\Pi_\texttt{ano}\) je množina všech instancí problému \(\Pi\), které mají výstup \(\texttt{ano}\). Podobně \(\Pi_\texttt{ne}\) je množina instancí problému \(\Pi\), jejichž výstup je \(\texttt{ne}\).

## Poznámka Anki 1728041134476

Karty Anki: 1728041134476
GUID: yyY%on])>T; štítky: ni-kop::p03 ni-spol::11.

### Otázka (Front)

Definujte třídu \(\text{NP}\) pomocí svědka.

### Odpověď (Back)

Rozhodovací problém \(\Pi\) patří do třídy \(\text{NP}\), jestliže pro každou instanci \(I \in \Pi_\texttt{ano}\) problému \(\Pi\) existuje konfigurace \(Y\) taková, že kontrola, zda je \(Y\) řešením, patří do \(\text P\). Konfiguraci \(Y\) pak nazýváme svědkem (certifikátem).

### Doplňující pole (Extra)

Z této definice vyplývá, že omezení a optimalizační kritérium takového problému lze vyhodnotit v polynomiálním čase.
Množina \(\Pi_\texttt{ano}\) je množina všech instancí problému \(\Pi\), které mají výstup \(\texttt{ano}\). Podobně \(\Pi_\texttt{ne}\) je množina instancí problému \(\Pi\), jejichž výstup je \(\texttt{ne}\).

## Poznámka Anki 1728041555417

Karty Anki: 1728041555417
GUID: lKG7@H2Kn/; štítky: ni-kop::p03 ni-spol::11.

### Otázka (Front)

Popište problém Hamiltonovy kružnice (Hamiltonian cycle).

### Odpověď (Back)

Problém Hamiltonovy kružnice (Hamiltonian cycle) je kombinatorický problém. Na vstupu je dán graf \(G = (V, E)\) a cílem je rozhodnout, zda obsahuje Hamiltonovu kružnici, tedy kružnici, která každý vrchol navštíví právě jednou. Problém Hamiltonovy kružnice patří do třídy \(\text{NP}\).

## Poznámka Anki 1728062197045

Karty Anki: 1728062197045
GUID: xa@Gxvx|*0; štítky: ni-kop::p03.

### Otázka (Front)

Popište konstrukci komplementárních rozhodovacích problémů a typy svědků.

### Odpověď (Back)

Rozhodovací problémy typicky zadáváme „kladně,“ tedy \(\exists Y, R(I, Y)\). Konfiguraci \(Y\) pak nazýváme \(\exists\)**-svědkem**. Ke **komplementárnímu problému** přejdeme s pomocí „záporného“ zadání \(\forall Y, \lnot R(I, Y)\) a \(Y\) pak nazveme \(\forall\)**-svědkem**.

### Doplňující pole (Extra)

Komplementární třídy rozhodovacích problémů typicky označujeme předponou „\(\text{co-}\),“ tedy např. pro \(\text{NP}\) máme \(\text{co-NP}\).

## Poznámka Anki 1728062690083

Karty Anki: 1728062690083
GUID: uG$e+t-wd]; štítky: ni-kop::p03.

### Otázka (Front)

Definujte polynomiální hierarchii rozhodovacích problémů.

### Odpověď (Back)

Nechť \(\Sigma_0^\text P \equiv \Pi_0^\text P \equiv \text P\). Pak

- \(\Sigma_i^\text P\) je třída rozhodovacích problémů, pro něž existuje krátký \(\exists\)-svědek a problém jeho kontroly je třídy \(\Pi_{i - 1}^\text P\).

- \(\Pi_i^\text P\) je třída rozhodovacích problémů, pro něž existuje krátký \(\forall\)-svědek a problém jeho kontroly je třídy \(\Sigma_{i - 1}^\text P\).

Tedy platí, že \(\Sigma_1^\text P \equiv \text{NP}\) a \(\Pi_1^\text P \equiv \text{co-NP}\).

 [Obrázek: paste-2ba41707ef6a85ffc3760c5e6c19b1163e3e3b10.jpg; soubor je v media/ v doprovodném ZIP]

