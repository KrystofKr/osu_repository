# BI-DML – Základní sada otázek

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-DML
Rozsah: 43 poznámek, 43 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1715524560457

Karty Anki: 1715524560457
GUID: qRu+JC>|4Y; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte prvotní výrok a prvotní formuli.

### Odpověď (Back)

**Prvotní výrok** je jednoduchá oznamovací věta, u které má smysl se ptát, zda je či není pravdivá.
  Prvotní výroky označujeme velkými tiskacími písmeny \(A, B, C, \dots\), kterým říkáme **prvotní formule**.

## Poznámka Anki 1715524642903

Karty Anki: 1715524642903
GUID: z8lR6x?,EC; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte pravdivostní ohodnocení.

### Odpověď (Back)

Pravdivostní ohodnocení množiny prvotních výroků je zobrazení \(v\), které každé prvotní formuli přiřadí \(0\) nebo \(1\) tak, že

- je-li \(v(A) = 1\), řekneme, že \(A\) je pravdivý při ohodnocení \(v\);
- je-li \(v(A) = 0\), řekneme, že \(A\) je nepravdivý při ohodnocení \(v\).

## Poznámka Anki 1715524987281

Karty Anki: 1715524987281
GUID: HH#Wm0IAd{; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte jazyk výrokové logiky.

### Odpověď (Back)

Jazyk výrokové logiky obsahuje:

- symboly pro prvotní formule \(A, B, \dots\);
- logické spojky \(\lnot, \land,\) \(\lor\), \(\Rightarrow\), \(\Leftrightarrow\);
- závorky \((\), \()\).

## Poznámka Anki 1715525198633

Karty Anki: 1715525198633
GUID: b2M-)re=-[; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte formuli výrokové logiky.

### Odpověď (Back)

Formule výrokové logiky je každá posloupnost symbolů z jazyka výrokové logiky, která vznikne aplikací následujících pravidel:

- každá prvotní formule je výroková formule;
- jsou-li \(E\) a \(F\) výrokové formule, pak jsou i \(\lnot E\), \((E \land F)\), \((E \lor F)\), \((E \Rightarrow F)\) a \((E \Leftrightarrow F)\) výrokové formule;
- každá posloupnost symbolů vzniklá aplikací předcházejících pravidel v konečně mnoha krocích je výroková formule.

## Poznámka Anki 1715525396698

Karty Anki: 1715525396698
GUID: Mz)ayg.nww; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte tautologii, splnitelnost a kontradikci.

### Odpověď (Back)

Nechť \(F\) je výroková formule. Řekneme, že \(F\) je:

- **tautologie **(\(\top\)), právě když pro každé ohodnocení \(v\) platí \(v(F) = 1\);

- **splnitelná**, existuje-li ohodnocení \(v\) takové, že \(v(F) = 1\);

- **kontradikce **(\(\bot\)), právě když pro každé ohodnocení \(v\) platí \(v(F) = 0\).

## Poznámka Anki 1715528550145

Karty Anki: 1715528550145
GUID: DsGlM:M^Ky; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte logickou ekvivalenci a logický důsledek.

### Odpověď (Back)

Nechť \(E\) a \(F\) jsou výrokové formule. Řekneme, že

- \(E\) a \(F\) jsou **logicky ekvivalentní**, právě když pro každé ohodnocení \(v\) je \(v(E) = v(F)\) neboli \(E \Leftrightarrow F \) je tautologie. Značíme

\[\newcommand{\logi}{{\mkern4mu\textcolor{white}{\rule{0.4pt}{1.5ex}}\mkern-1mu{=}\mkern-1mu\textcolor{white}{\rule{0.4pt}{1.5ex}}\mkern3mu}}
E \logi F.\]

- \(F\) je **logickým důsledkem** \(E\), právě když pro každé ohodnocení \(v\), pro které \(v(E) = 1\), je i \(v(F) = 1\) neboli \(E \Rightarrow F\) je tautologie. Značíme

\[E \models F.\]

## Poznámka Anki 1715529843749

Karty Anki: 1715529843749
GUID: uG887)33+,; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte univerzální systém logických spojek. Uveďte příklady.

### Odpověď (Back)

Množina logických spojek tvoří univerzální systém, právě když ke každé formuli existuje logicky ekvivalentní formule, která obsahuje pouze tyto spojky. Příkladem může být:

- \(\{ \neg, \wedge, \vee, \Rightarrow, \Leftrightarrow \}\), \(\{ \neg, \wedge, \vee, \Rightarrow \}\), \(\{ \neg, \wedge, \vee \}\);

- \(\{ \neg, \vee \}\), \(\{ \neg, \wedge \}\), \(\{ \neg, \Rightarrow \}\);

- \(\{ \uparrow \}\), \(\{ \downarrow \}\).

## Poznámka Anki 1715530006108

Karty Anki: 1715530006108
GUID: Am&q6?_[4:; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte Shefferův symbol (NAND) a Peircovu šipku (NOR).

### Odpověď (Back)

Nechť \(A\) a \(B\) jsou výrokové formule. Definujme spojky:

- **Shefferův symbol **(NAND) značený \(\uparrow\) vztahem

\[\newcommand{\logi}{{\mkern4mu\textcolor{white}{\rule{0.4pt}{1.5ex}}\mkern-1mu{=}\mkern-1mu\textcolor{white}{\rule{0.4pt}{1.5ex}}\mkern3mu}}
A \uparrow B \logi \lnot (A \land B).\]

- **Peircova šipka **(NOR) značená \(\downarrow\) vztahem

\[A \downarrow B \logi \lnot (A \lor B).\]

## Poznámka Anki 1715530366582

Karty Anki: 1715530366582
GUID: P=v*pXYrSe; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte logickou spojku negace.

### Odpověď (Back)

Negace \(\lnot A\) výroku \(A\) je je pravdivá pro všechna ohodnocení, při kterých je \(A\) nepravdivý. Pro ostatní ohodnocení je nepravdivá. V přirozeném jazyce odpovídá tvrzením typu „Neplatí, že \(A\).“
\[\begin{array}{c||c}
    A & \neg A \\
    \hline
    1 & 0\\
    0 & 1
    \end{array}\]

## Poznámka Anki 1715530427576

Karty Anki: 1715530427576
GUID: q}*NA(6$(R; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte logickou spojku konjunkce.

### Odpověď (Back)

Konjunkce \(A \land B\) výroků \(A\) a \(B\) je pravdivá pro všechna ohodnocení, při kterých jsou \(A\) i \(B\) současně pravdivé. Pro ostatní ohodnocení je nepravdivá. V přirozeném jazyce odpovídá tvrzením typu „Platí \(A \) a současně \(B\).“
\[\begin{array}{c|c||c}
    A & B & A \wedge B \\
    \hline
    1 & 1 & 1\\
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & 0
    \end{array}\]

## Poznámka Anki 1715530484381

Karty Anki: 1715530484381
GUID: o:5!F]BG{R; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte logickou spojku disjunkce.

### Odpověď (Back)

Disjunkce \(A \lor B\) výroků \(A\) a \(B\) je pravdivá pro všechna ohodnocení, při kterých je alespoň jeden z výroků \(A\) a \(B\) pravdivý. Pro ostatní ohodnocení je nepravdivá. V přirozeném jazyce odpovídá tvrzením typu „Platí \(A \) nebo \(B\).“
\[\begin{array}{c|c||c}
    A & B & A \vee B \\
    \hline
    1 & 1 & 1\\
    1 & 0 & 1\\
    0 & 1 & 1\\
    0 & 0 & 0
    \end{array}\]

## Poznámka Anki 1715530574039

Karty Anki: 1715530574039
GUID: vX,12Y:n&f; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte logickou spojku implikace.

### Odpověď (Back)

Implikace \(A \Rightarrow B\) mezi výroky \(A\) a \(B\) je nepravdivá pro všechna ohodnocení, při kterých je předpoklad \(A\) pravdivý a závěr \(B\) nepravdivý. Pro ostatní ohodnocení je pravdivá. V přirozeném jazyce odpovídá tvrzením typu „Jestliže \(A\), pak \(B\).“
\[\begin{array}{c|c||c}
    A & B & A \Rightarrow B \\
    \hline
    1 & 1 & 1\\
    1 & 0 & 0\\
    0 & 1 & 1\\
    0 & 0 & 1
    \end{array}\]

## Poznámka Anki 1715530727988

Karty Anki: 1715530727988
GUID: M{[caq]jIf; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte logickou spojku ekvivalence.

### Odpověď (Back)

Ekvivalence \(A \Leftrightarrow B\) mezi výroky \(A\) a \(B\) je pravdivá pro všechna ohodnocení, při kterých mají výroky \(A\) a \(B\) stejnou pravdivostní hodnotu. Pro ostatní ohodnocení je nepravdivá. V přirozeném jazyce odpovídá tvrzením typu „\(A\) právě tehdy, když \(B\).“
\[\begin{array}{c|c||c}
    A & B & A \Leftrightarrow B \\
    \hline
    1 & 1 & 1\\
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & 1
    \end{array}\]

## Poznámka Anki 1715530879844

Karty Anki: 1715530879845
GUID: ZdwOp]+0_; štítky: bi-dml bi-spol::07 duplicate.

### Otázka (Front)

Definujte literál.

### Odpověď (Back)

Výroková formule je literál, je-li prvotní formulí nebo negací prvotní formule.

## Poznámka Anki 1715531006287

Karty Anki: 1715531006287
GUID: NEr./`6?Qb; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte implikant a disjunktivní normální tvar (DNT).

### Odpověď (Back)

Výroková formule je **implikant**, je-li literálem nebo konjunkcí několika literálů. V **disjunktivním normálním tvaru** (DNT) je tehdy, je-li implikantem nebo disjunkcí několika implikantů.

## Poznámka Anki 1715531082450

Karty Anki: 1715531082450
GUID: q?ANuPz|b0; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte klausuli a konjunktivní normální tvar (KNT).

### Odpověď (Back)

Výroková formule je **klausule**, je-li literálem nebo disjunkcí několika literálů. V **konjunktivním normálním tvaru** (KNT) je tehdy, je-li klausulí nebo konjunkcí několika klausulí.

## Poznámka Anki 1715531248445

Karty Anki: 1715531248445
GUID: ge^vYf.)!>; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte minterm a úplný disjunktivní normální tvar (ÚDNT).

### Odpověď (Back)

Výroková formule je **minterm **formule \(F\), pokud je to takový její implikant, který obsahuje všechny prvotní formule vyskytující se v \(F\), každou právě jednou. V **úplném disjunktivním normálním tvaru** (ÚDNT) je tehdy, je-li mintermem nebo disjunkcí různých (logicky neekvivalentních) mintermů.

## Poznámka Anki 1715531316198

Karty Anki: 1715531316198
GUID: P<-@f6ZA<!; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Definujte maxterm a úplný konjunktivní normální tvar (ÚKNT).

### Odpověď (Back)

Výroková formule je **maxterm **formule \(F\), pokud je to taková její klausule, která obsahuje všechny prvotní formule vyskytující se v \(F\), každou právě jednou. V **úplném konjunktivním normálním tvaru** (ÚKNT) je tehdy, je-li maxtermem nebo konjunkcí různých (logicky neekvivalentních) maxtermů.

## Poznámka Anki 1715535106392

Karty Anki: 1715535106392
GUID: KiFI+bOkB[; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Popište souvislost mezi úplnými normálními tvary a pravdivostní tabulkou.

### Odpověď (Back)

Označme jako \(A_k\) a \(A_d\) úplný KNT a úplný DNT formule \(A\) o \(n\) prvotních formulích. Pak platí:

-  Počet ohodnocení prvotních formulí, pro která je formule \(A\) pravdivá, je roven počtu mintermů \(A_d\).
-  Počet ohodnocení prvotních formulí, pro která je formule \(A\) nepravdivá, je roven počtu maxtermů \(A_k\).
-  Součet počtu mintermů \(A_d\) a počtu maxtermů \(A_k\) je \(2^n\).

## Poznámka Anki 1715535368158

Karty Anki: 1715535368158
GUID: gY-p#@Kg<t; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Popište souvislost mezi úplnými normálními tvary a logickou ekvivalencí a logickým důsledkem.

### Odpověď (Back)

Mějme výrokové formule \(A\) a \(B\) obsahující stejné prvotní formule, označme jejich úplné DNT jako \(A_d\) a \(B_d\) a jejich úplné KNT jako \(A_k\)  a \(B_k\). Pak platí:

- \(\newcommand{\logi}{{\mkern4mu\textcolor{white}{\rule{0.4pt}{1.5ex}}\mkern-1mu{=}\mkern-1mu\textcolor{white}{\rule{0.4pt}{1.5ex}}\mkern3mu}}
A \logi B\) právě tehdy, když \(A_d\) a \(B_d\) obsahují stejné mintermy.
- \(A \logi B\) právě tehdy, když \(A_k\) a \(B_k\) obsahují stejné maxtermy.
- \(A \models B\) právě tehdy, když všechny mintermy \(A_d\) jsou obsaženy i v \(B_d\).
- \(A \models B\) právě tehdy, když všechny maxtermy \(B_k\) jsou obsaženy i v \(A_k\).

## Poznámka Anki 1715538621337

Karty Anki: 1715538621337
GUID: rbX.x)kpic; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Definujte dělitelnost.

### Odpověď (Back)

Nechť \(a, b \in \mathbb Z\). Řekneme, že \(a\) dělí \(b\), značíme \(a | b\), jestliže existuje \(k \in \mathbb Z\) takové, že
\[a \cdot k = b.\]Pokud \(a\) nedělí \(b\), píšeme \(a \!\nmid\! b\). Samotné \(\mid\) nazýváme relací dělitelnosti.

## Poznámka Anki 1715539146482

Karty Anki: 1715539146482
GUID: f/RES45NAK; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Definujte Bézoutovu rovnost a Bézoutovy koeficienty.

### Odpověď (Back)

Mějme \(a, b \in \mathbb Z\). Pak existují \(m, n \in \mathbb Z\) taková, že vztah
\[\gcd(a, b) = m \cdot a + n \cdot b\]nazveme **Bézoutovou rovností**. Dvojici koeficientů \(m\), \(n\) nazýváme **Bézoutovými koeficienty**.

## Poznámka Anki 1715539372888

Karty Anki: 1715539372889
GUID: o5:=^Rg;69; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Definujte lineární diofantickou rovnici.

### Odpověď (Back)

Lineární diofantická rovnice (pro dvě neznámé) je libovolná rovnice typu
\[ax + by = c,\]kde \(a, b, c \in \mathbb Z\) pro dvě neznámé \(x, y \in \mathbb Z\).

## Poznámka Anki 1715539614410

Karty Anki: 1715539614410
GUID: MCA-cs/K;w; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Vyslovte větu o řešitelnosti lineární diofantické rovnice.

### Odpověď (Back)

Lineární diofantická rovnice
\[ax + by = c\]má alespoň jedno řešení právě tehdy, když \(\gcd(a, b) \ | \ c\).

## Poznámka Anki 1715540005156

Karty Anki: 1715540005156
GUID: mai#~phG^/; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Popište postup řešení lineární diofantické rovnice.

### Odpověď (Back)

Pro nalezení partikulárního řešení lineární diofantické rovnice
\[ax + by = c\]je postup následující:

- Určíme \(\gcd(a, b)\). Pokud \(\gcd(a, b) \!\nmid\!c\), řešení neexistuje.
- Pomocí REA nalezneme dvojici Bézoutových koeficientů \(\alpha, \beta \in \mathbb Z\) splňujících

\[\gcd(a, b) = \alpha \cdot a + \beta \cdot b.\]

- Obě strany Bézoutovy rovnosti vynásobíme celým číslem \(\frac c {\gcd(a, b)}\) a dostaneme, že

\[x = \alpha \cdot \frac c {\gcd(a, b)}, \quad y = \beta \cdot \frac c {\gcd(a, b)}.\]REA:
 [Obrázek: paste-f9c581ce0782436e618b300274166191cfdf231d.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1715540515258

Karty Anki: 1715540515258
GUID: EWEq9|rf2p; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Vyslovte větu o množině všech řešení lineární diofantické rovnice.

### Odpověď (Back)

Nechť \(a, b \in \mathbb Z \smallsetminus \{ 0 \}\) a dvojice \((x_0, y_0) \in \mathbb Z^2\) je řešením lineární diofantické rovnice
\[ax + by = c.\]Potom množina všech celočíselných řešení této rovnice je
\[\bigg\{ \bigg( x_0 + \frac b {\gcd(a, b)} \cdot k, y_0 - \frac a {\gcd(a, b)} \cdot k \ \bigg| \ k \in \mathbb Z \bigg) \bigg\},\]což lze ekvivalentně zapsat jako
\[\bigg\{(x_0,y_0) + k \cdot \bigg(\frac{b}{\gcd(a,b)}, \frac{-a}{\gcd(a,b)}\bigg) \ \bigg|\ k\in \mathbb Z\bigg\}.\]

### Doplňující pole (Extra)

Druhý z ekvivalentních zápisů připomíná zápis řešení soustavy lineárních rovnic, kde se k partikulárnímu řešení rovnice přičítá množina řešení přidružené homogenní soustavy rovnic.

## Poznámka Anki 1715540737846

Karty Anki: 1715540737846
GUID: jK,]Cs-/V,; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Definujte partikulární řešení a přidruženou homogenní rovnici lineární diofantické rovnice.

### Odpověď (Back)

Mějme lineární diofantickou rovnici
\[ax + by = c.\]Potom **partikulárním řešením **nazveme libovolné řešení \((x_0, y_0)\) této rovnice. **Přidruženou homogenní rovnicí** pak nazýváme lineární diofantickou rovnici
\[ax + by = 0.\]

## Poznámka Anki 1715540933175

Karty Anki: 1715540933175
GUID: f<w`st2f-B; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Popište rozdělení přirozených čísel a definujte prvočísla a čísla složená.

### Odpověď (Back)

Přirozená čísla \(\mathbb N\) rozdělujeme podle počtu dělitelů do tří tříd:

- číslo \(1\), které má jediného dělitele, sebe sama;
- **prvočísla**, která mají právě dva dělitele, sebe sama a číslo \(1\);

- všechna ostatní čísla, která se nazývají **složená čísla**.

## Poznámka Anki 1715541141184

Karty Anki: 1715541141184
GUID: v|z3I=xZO@; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Vyslovte základní větu aritmetiky.

### Odpověď (Back)

Každé \(n \in \mathbb N\), \(n \geq 2\) se dá jednoznačně vyjádřit součinem
\[n = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots p_k^{\alpha_k} = \displaystyle \prod_{i = 1}^k p_i^{\alpha_i},\]kde \(k \in \mathbb N\), \(p_1 < p_2 < \cdots p_k\) jsou prvočísla a \(\alpha_1, \alpha_2 \dots \alpha_k \in \mathbb N\). Tento zápis se nazývá kanonickým (prvočíselným) rozkladem čísla \(n\) nebo také (prvočíselnou) faktorizací čísla \(n\).

## Poznámka Anki 1715541514118

Karty Anki: 1715541514118
GUID: e(_94Ty!|;; štítky: bi-dml.

### Otázka (Front)

Definujte kongruenci modulo \(m\).

### Odpověď (Back)

Nechť \(a, b \in \mathbb Z\) a \(m \in \mathbb N\). Pokud \(m \ | \ (a - b)\), říkáme, že \(a\) je kongruentní s \(b\) modulo \(m\) a píšeme
\[a \equiv b \pmod m.\]Samotné \(\equiv (\bmod m)\) nazýváme relací kongurence modulo \(m\).

## Poznámka Anki 1715542412056

Karty Anki: 1715542412056
GUID: p<Jh>5>Kbf; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Definujte množinu zbytků \(\mathbb Z_m\) a operace na ní.

### Odpověď (Back)

Nechť \(m \geq 2\). Jako \(\mathbb Z_m\) označíme množinu všech zbytků modulo \(m\),
\[\mathbb Z_m = \{ 0, 1, \dots m - 1 \}.\]Na \(\mathbb Z\) zavádíme operace sčítání a násobení modulo \(m\):
\[\begin{matrix}
+_m : \mathbb Z \times \mathbb Z \to \mathbb Z_m, & a +_m b := (a + b) \bmod m,\\
\cdot_m : \mathbb Z \times \mathbb Z \to \mathbb Z_m, & a \cdot_m  b := (a \cdot b) \bmod m.
\end{matrix}\]

## Poznámka Anki 1715542540552

Karty Anki: 1715542540552
GUID: eOl.zDrR(=; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Definujte inverze v \(\mathbb Z_m\).

### Odpověď (Back)

Mějme \(m \geq 2\) a \(a \in \mathbb Z_m\). Číslo \(x \in \mathbb Z_m\) nazveme:

- **aditivní inverzí **k \(a\) (značíme \(-a\)), právě když platí

\[x +_m a= a +_m x = 0.\]

- **multiplikativní inverzí **k \(a\) (značíme \(a^{-1}\)), právě když platí

\[x \cdot_m a = a \cdot_m x = 1.\]

## Poznámka Anki 1715542609245

Karty Anki: 1715542609245
GUID: G/FanxM#2m; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Vyslovte větu o existenci multiplikativní inverze.

### Odpověď (Back)

Mějme \(m \geq 2\) a \(a \in \mathbb Z_m\). V \(\mathbb Z_m\) existuje multiplikativní inverze k \(a\) právě tehdy, když \(\gcd(a, m) = 1\). Pokud tato inverze existuje, pak je jediná.

## Poznámka Anki 1715542669978

Karty Anki: 1715542669978
GUID: N:j,<A=Y}F; štítky: bi-dml duplicate.

### Otázka (Front)

Vyslovte Malou Fermatovu větu.

### Odpověď (Back)

Mějme prvočíslo \(p\) a \(a \in \mathbb Z\) takové, že \(\gcd (a, p) = 1\). Potom platí
\[a^{p - 1} \equiv 1 \pmod p.\]

## Poznámka Anki 1715542793676

Karty Anki: 1715542793676
GUID: xf;#2!6W{<; štítky: bi-dml duplicate.

### Otázka (Front)

Definujte Eulerovu funkci \(\varphi\).

### Odpověď (Back)

Eulerova funkce \(\varphi(n): \mathbb N \to \mathbb N\) je zobrazení, které každému \(n \in \mathbb N\) přiřadí počet přirozených čísel menších nebo rovných \(n\), která jsou s \(n\) nesoudělná.

## Poznámka Anki 1715542846531

Karty Anki: 1715542846531
GUID: i;!e*CWz]J; štítky: bi-dml duplicate.

### Otázka (Front)

Vyslovte Eulerovu větu.

### Odpověď (Back)

Nechť \(a \in \mathbb Z\), \(m \in \mathbb N\) a \(\gcd(a, m) = 1\). Potom platí
\[a^{\varphi(m)} \equiv 1 \pmod m,\]kde \(\varphi\) označuje Eulerovu funkci.

## Poznámka Anki 1715542884991

Karty Anki: 1715542884992
GUID: xeBc=r.RG]; štítky: bi-dml duplicate.

### Otázka (Front)

Uveďte metody výpočtu Eulerovy funkce.

### Odpověď (Back)

Nechť \(p\) je prvočíslo a \(\alpha \in \mathbb N\). Potom
\[\varphi(p^\alpha) = p^\alpha - p^{\alpha - 1}.\]Nechť \(m\), \(n \in \mathbb N\) a \(\gcd(m, n) = 1.\) Potom
\[\varphi(m \cdot n) = \varphi(m) \cdot \varphi(n).\]Nechť \(m = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots  p_k^{\alpha_k}\) je kanonický (prvočíselný) rozklad složeného čísla \(m \in \mathbb N\). Potom
\[\varphi(m) = m \cdot \Big(1 - \frac 1 {p_1}\Big) \cdot \Big(1 - \frac 1 {p_2}\Big) \cdots \Big(1 - \frac 1 {p_k}\Big).\]

## Poznámka Anki 1715543436550

Karty Anki: 1715543436550
GUID: f4{^G<h~E!; štítky: bi-dml.

### Otázka (Front)

Vyslovte větu o řešení lineární kongruence modulo \(\mathbb Z_m\).

### Odpověď (Back)

Jestliže \(\gcd(a, m) \ | \ b\), potom lineární kongruence
\[ax \equiv b \pmod m\]má v \(\mathbb Z_m\) přesně \(\gcd(a, m)\) řešení. Množinu řešení získáme jako
\[\begin{equation*}
\left\{\left(x_0 + k \cdot \frac{m}{\gcd(a,m)}\right) \bmod m \ \bigg|\ k\in\big\{0,1,\dots,\gcd(a,m)-1 \big\}\right\}\,,
\end{equation*}\]kde \(x_0\) je z dvojice \((x_0, y_0)\), která je nějakým řešením lineární diofantické rovnice
\[a \cdot x + m \cdot y = b.\]

## Poznámka Anki 1715543834574

Karty Anki: 1715543834574
GUID: c~>m#%P%d+; štítky: bi-dml duplicate.

### Otázka (Front)

Vyslovte větu o Čínské větě o zbytcích.

### Odpověď (Back)

Uvažujme soustavu lineárních kongurencí
\[\begin{matrix}
x \equiv a_1 \pmod {m_1},\\
x \equiv a_2 \pmod {m_2},\\
\vdots\\
x \equiv a_N \pmod {m_N},\\
\end{matrix}\]kde \(m_1, m_2, \dots, m_N \geq 2\) jsou vzájemně nesoudělná. Řešení této soustavy existuje a je jednoznačně určeno v \(\mathbb Z_M\), kde
\[M = \displaystyle \prod_{i = 1}^N m_i.\]

## Poznámka Anki 1715544086630

Karty Anki: 1715544086630
GUID: Ob)&%*i;DZ; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Vyslovte větu o zobecněné Čínské větě o zbytcích.

### Odpověď (Back)

Uvažujme soustavu lineárních kongurencí
\[\begin{matrix}
x \equiv a_1 \pmod {m_1},\\
x \equiv a_2 \pmod {m_2},\\
\vdots\\
x \equiv a_N \pmod {m_N},\\
\end{matrix}\]kde \(m_1, m_2, \dots, m_N \geq 2\). Tato soustava má řešení právě tehdy, když \(\gcd(m_i, m_j)\) dělí \(a_i - a_j\) pro všechna \(i \neq j\). Pokud řešení existuje, je jednoznačně určeno modulo \(\operatorname{lcm}(m_1, m_2, \dots, m_N)\).

## Poznámka Anki 1715598898565

Karty Anki: 1715598898565
GUID: J,cFI5MRSG; štítky: bi-dml bi-spol::08.

### Otázka (Front)

Vyslovte větu o vztahu \(\gcd\) a \(\operatorname{lcm}\).

### Odpověď (Back)

Nechť \(a, b \in \mathbb Z\). Pak platí
\[\gcd(a, b) \cdot \operatorname{lcm}(a, b) = |a| \cdot |b|.\]

## Poznámka Anki 1718389066877

Karty Anki: 1718389066877
GUID: k||1uX;)>P; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Popište logické zákony výrokové logiky.

### Odpověď (Back)

Mezi základní logické zákony patří:

- zákon vyloučení sporu

\[\newcommand{\logi}{{\mkern4mu\textcolor{white}{\rule{0.4pt}{1.5ex}}\mkern-1mu{=}\mkern-1mu\textcolor{white}{\rule{0.4pt}{1.5ex}}\mkern3mu}}
A \land \lnot A \logi \bot,\]

- zákon vyloučeného třetího

\[A \lor \lnot A \logi \top\]

- zákon dvojí negace

\[\lnot \lnot A \Leftrightarrow A \logi \top.\]Dále platí

- komutativní, distributivní a asociativní zákony pro konjunkci a disjunkci,
- De Morganovy zákony

\[\lnot (A  \land B) \logi \lnot A \lor \lnot B \quad \text{a} \quad \lnot (A \lor B) \logi \lnot A \land \lnot B\]a další.

## Poznámka Anki 1718788519221

Karty Anki: 1718788519221
GUID: zsnux>ud55; štítky: bi-dml bi-spol::07.

### Otázka (Front)

Popište logické zákony vztahující se k implikaci.

### Odpověď (Back)

Mějme dvě výrokové formule \(A\) a \(B\). Pak platí následující logické ekvivalence:

- zákon kontrapozice

\[\newcommand{\logi}{{\mkern4mu\textcolor{white}{\rule{0.4pt}{1.5ex}}\mkern-1mu{=}\mkern-1mu\textcolor{white}{\rule{0.4pt}{1.5ex}}\mkern3mu}}
A \Rightarrow B \logi \lnot B \Rightarrow \lnot A,\]

- převod na disjunkci

\[A \Rightarrow B \logi \lnot A \lor B,\]

- převod na konjunkci

\[\lnot(A \Rightarrow B) \logi A \land \lnot B.\]

