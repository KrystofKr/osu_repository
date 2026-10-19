# BI-KAB – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-kab/BI-KAB.apkg; APKG SHA-256 080060aa53ee5f63eca18237eef611a0bfca99908f9ab640e349ebadb96964ec. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8571882594c00598a0b5a029eed57cadb06fe0563741a3f883a87eacef0c1588.
Původní balíčky: BI-KAB
Rozsah: 29 poznámek, 29 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1676987016773

Karty Anki: 1676987016774
GUID: ld%:l4r8RS; štítky: bi-kab::p01.

### Otázka (Front)

Co je to kryptologie, kryptografie a kryptoanalýza.

### Odpověď (Back)

**Kryptologie** je věda o tvorbě a luštění šifer. **Kryptografie **je věda o tvorbě šifer a **kryptoanalýza** je věda o luštění šifer. Kryptografie a kryptoanalýza spadají pod kryptologii.

## Poznámka Anki 1676987037980

Karty Anki: 1676987037980
GUID: y9Vn]$60_!; štítky: bi-kab::p01 bi-spol::09 bi-spol::10.

### Otázka (Front)

Co je to otevřený text (OT)?

### Odpověď (Back)

Otevřený text (OT) je text, který je určen k šifrování, tedy transformaci na šifrový text (ŠT).

## Poznámka Anki 1676987056806

Karty Anki: 1676987056806
GUID: Ov_{t=$o`S; štítky: bi-kab::p01 bi-spol::09 bi-spol::10.

### Otázka (Front)

Co je to šifrování?

### Odpověď (Back)

Šifrování je proces převodu otevřeného textu na šifrový text, ideálně takovým způsobem, aby byl čitelný pouze pro autorizované subjekty.

## Poznámka Anki 1676987080353

Karty Anki: 1676987080353
GUID: vzZr;?6$`F; štítky: bi-kab::p01 bi-spol::09 bi-spol::10.

### Otázka (Front)

Co je to šifra?

### Odpověď (Back)

Šifra je algoritmus, který udává způsob šifrování (převod OT na ŠT) a dešifrování (převod ŠT na OT).

## Poznámka Anki 1676987136847

Karty Anki: 1676987136847
GUID: r/@=2iJm0u; štítky: bi-kab::p01 bi-spol::09 bi-spol::10.

### Otázka (Front)

Co je to dešifrování? Co je k němu nutné?

### Odpověď (Back)

Dešifrování je proces opačný k šifrování, tedy převádí šifrový text zpět na otevřený text. Pro dešifrování je nutná znalost šifry.

## Poznámka Anki 1676987327507

Karty Anki: 1676987327507
GUID: r4nfEf#L_5; štítky: bi-kab::p01.

### Otázka (Front)

Z jakých fází se skládá proces kryptoanalýzy?

### Odpověď (Back)

Proces kryptoanalýzy se skládá z následujících částí:

- **identifikace** - určení použitého šifrovacího systému,

- **prolomení** - určení neměnných částí způsobu šifrování zprávy,

- **nastavení** - určení způsobu proměny proměnlivé části kryptosystému.

## Poznámka Anki 1676987435479

Karty Anki: 1676987435479
GUID: q9%LHrLpv{; štítky: bi-kab::p01.

### Otázka (Front)

Jaký je rozdíl mezi šifrováním a kódováním?

### Odpověď (Back)

**Šifrování** má za úkol utajit zprávu před nepovolanou osobou. **Kódování** zprávu neutajuje, ale pouze upravuje za účelem přenosu pomocí nějakého kanálu (např. detekce poruchy zprávy pomocí Hammingova kódu).

## Poznámka Anki 1676987506694

Karty Anki: 1676987506694
GUID: imxmMi{zW$; štítky: bi-kab::p01 bi-spol::09 bi-spol::10.

### Otázka (Front)

Co je to šifrovací systém (kryptosystém)?

### Odpověď (Back)

Šifrovací systém je sada kryptografických algoritmů a k nim přidružené infrastruktury, která se používá pro poskytování ochrany informace. Formálně je kryptosystém definován jako uspořádaná pětice \((\mathcal P, \mathcal C, \mathcal K, \mathcal E, \mathcal D)\), kde

- \(\mathcal P\) je prostor OT,

- \(\mathcal C\) je prostor ŠT,
- \(\mathcal K\) je prostor klíčů,

- \(\mathcal E = \{ E_k : k \in \mathcal K \}\) je množina šifrovacích funkcí \(E_k : \mathcal P \to \mathcal C\),

- \(\mathcal D = \{ D_k : k \in \mathcal K \}\) je množina dešifrovacích funkcí \(D_k : \mathcal C \to \mathcal P\).

## Poznámka Anki 1676987544188

Karty Anki: 1676987544188
GUID: KfW!+zbDGn; štítky: bi-kab::p01.

### Otázka (Front)

Jaké metody šifrování dominovaly do nástupu počítačů?

### Odpověď (Back)

Do nástupu počítačů dominovala substituční, transpoziční a metoda kódové knihy.

## Poznámka Anki 1676987730993

Karty Anki: 1676987730993
GUID: E$H{^#P)S(; štítky: bi-kab::p01.

### Otázka (Front)

Popište šifrování pomocí kódové knihy.

### Odpověď (Back)

Kódová kniha představuje slovník s běžnými frázemi tvořenými jedním nebo více symboly či slovy. Pomocí kódové knihy je potom každý symbol či slovo OT nahrazeno za **kódovou skupinu**, která je typicky tvořena čtyřmi až pěti písmeny nebo čísly.

## Poznámka Anki 1676988082680

Karty Anki: 1676988082680
GUID: diLn9@;T9b; štítky: bi-kab::p01.

### Otázka (Front)

Jak lze posuzovat odolnost šifrovacích systémů?

### Odpověď (Back)

Rozlišujeme pět způsobů testování šifry podle toho, jakou část šifry kryptoanalytik zná:

1. **ciphertext-only attack** - pouze ŠT (šifra prolomitelná tímto způsobem není vhodná pro praktické využití),

2. **known-plaintext attack** - ŠT a jeden nebo více OT,

3. **chosen-plaintext attack** - vybraný (na základě požadované vlasnosti) OT a k němu odpovídající ŠT,
4. **chosen-ciphertext attack** - vybraný (na základě požadované vlasnosti) ŠT a k němu odpovídající OT,

5. **chosen-text** **attack** - kombinace 3. a 4. metody.

## Poznámka Anki 1676991430189

Karty Anki: 1676991430189
GUID: e4z(H/tlif; štítky: bi-kab::p01 bi-spol::10.

### Otázka (Front)

Co je to substituční šifra? Jaké substituční šifry rozlišujeme?

### Odpověď (Back)

Substituční šifra patří mezi klasické šifry. Šifrování spočívá v tom, že pro každé písmeno OT se provede záměna. Cílem substituce je **konfúze**.
Podle způsobu substituce rozlišujeme šifry využívající:

- **monoalfabetickou substituci** - používá stejnou záměnu pro celý OT (např. Caesarova šifra),

- **polyalfabetickou substituci** - pro každou část OT může provést jinou záměnu (např. Vigenèrova šifra).

Podle množství substituovaných znaků rozlišujeme:

- **monografické šifry** - substituují za jeden znak OT (např. Caesarova šifra),

- **polygrafické šifry** - substituují za vícero znaků OT (např. Hillova šifra).

## Poznámka Anki 1677016456779

Karty Anki: 1677016456779
GUID: A^,A?C7puT; štítky: bi-kab::p01 bi-spol::10.

### Otázka (Front)

Co je to transpoziční šifra?

### Odpověď (Back)

Transpoziční šifra (někdy také permutační šifra) patří mezi klasické šifry. Šifrování spočívá ve změně uspořádání symbolů OT, tedy nedochází k jejich záměně jako u substituční šifry. Cílem transpoziční šifry je **difúze**.

## Poznámka Anki 1677016511950

Karty Anki: 1677016511950
GUID: G(v2Cubzu!; štítky: bi-kab::p01 bi-spol::10.

### Otázka (Front)

Co je to symetrická šifra? Uveďte příklady.

### Odpověď (Back)

Symetrická je taková šifra, která pro šifrování a dešifrování používá stejný klíč. Substituční a transpoziční šifry jsou symetrické.

## Poznámka Anki 1677016732370

Karty Anki: 1677016732371
GUID: x[EeIzSI&+; štítky: bi-kab::p01.

### Otázka (Front)

Co je to \(n\)-gram?

### Odpověď (Back)

\(n\)-gram (monogram, bigram, polygram) označuje posloupnost po sobě jdoucích symbolů abecedy délky \(n\).

## Poznámka Anki 1677016783718

Karty Anki: 1677016783718
GUID: I{tPjz??EL; štítky: bi-kab::p01.

### Otázka (Front)

Co je to symbol a řetězec?

### Odpověď (Back)

**Řetězec **je posloupnost po sobě jdoucích symbolů, kde **symbol **označuje libovolný prvek abecedy (písmeno, číslíci, interpunkční znaménko, a podobně).

## Poznámka Anki 1677017620152

Karty Anki: 1677017620152
GUID: g`bqtC.9;w; štítky: bi-kab::p01.

### Otázka (Front)

Popište afinní šifru. Jaké výhody nabízí oproti Caesarově šifře?

### Odpověď (Back)

Afinní šifra je monoalfabetická a monografická substituční šifra. Za předpokladu, že \(\gcd(a, m) = 1\), je šifrovací zobrazení definováno jako
\[c = | ap + b |_m\]a dešifrovací zobrazení jako
\[p = | a^{-1}(c - b) |_m.\]Oproti Caesarově šifře nabízí větší prostor klíčů, neboli větší množství možných transformací.

## Poznámka Anki 1677017711880

Karty Anki: 1677017711880
GUID: M]%Q[2[_mx; štítky: bi-kab::p01.

### Otázka (Front)

Jak lze prolamovat monoalfabetické monografické substituční šifry? Jak lze tento problém vyřešit?

### Odpověď (Back)

Monoalfabetické substituční šifry jsou zranitelné kryptoanalýzou založenou na frekvenční analýze ŠT. To proto, že četnosti monogramů ŠT jsou odrazem četnosti monogramů OT. Tento nedostatek řeší polyalfabetické šifry (Vigenérova šifra) a polygrafické šifry (Hillova šifra).

## Poznámka Anki 1677019702580

Karty Anki: 1677019702581
GUID: h|!4g@ekLP; štítky: bi-kab::p01 bi-spol::10.

### Otázka (Front)

Popište Hillovu šifru.

### Odpověď (Back)

Hillova šifra je monoalfabetická polygrafická substituční šifra (řadit by se dala i mezi blokové šifry) založená na lineární algebře. BÚNO uvažme délku bloku jeden bigram OT. Pak je šifrovací zobrazení definováno dvěma kongurencemi
\[\begin{matrix}
c_1 = | a_1 p_1 + b_1 p_2 |_m, \\
c_2 = | a_2 p_1 + b_2 p_2 |_m.
\end{matrix}\]Pro Hillovu šifru však použijeme maticový zápis
\[\Bigg| 
\begin{pmatrix}
c_1 \\
c_2
\end{pmatrix}
\Bigg|_m = \Bigg|
\begin{pmatrix}
a_1 & b_1 \\
a_1 & b_2 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
p_1 \\
p_2
\end{pmatrix}
\Bigg|_m\]nebo obecněji
\[\mathbf c = | \mathbf{Ap} |_m,\]přičemž předpokládáme, že \(\gcd \big(\det(\mathbf A), m \big) = 1\). Dešifrovací zobrazní potom definujeme jako
\[\mathbf p = | \mathbf{A^{-1}c} |_m.\]

## Poznámka Anki 1677020733005

Karty Anki: 1677020733006
GUID: JuS;!V}?/w; štítky: bi-kab::p01 bi-spol::10.

### Otázka (Front)

Jak lze prolamovat Hillovu šifru?

### Odpověď (Back)

Hillovu šifru lze prolamovat následujícími způsoby:

- **frekvenční analýza** - má smysl pro malé velikosti bloku,

- **known-plaintext** **kryptoanalýza** (2. typ) - lze využít lineární závislosti ŠT na OT k získání klíče (matice \(\mathbf A\)),

- **chosen-plaintext kryptoanalýza** (3. typ) - matici \(\mathbf p\) zvolíme jako jednotkovou a získáme klíč šifry (matici \(\mathbf A\)).

## Poznámka Anki 1677070843906

Karty Anki: 1677070843907
GUID: hOCAB1Z>rc; štítky: bi-kab::p01.

### Otázka (Front)

Popište Vigenèrovu šifru.

### Odpověď (Back)

Vigenèrova šifra je monografická polyalfabetická substituční šifra, která je tvořena konečnou posloupností Caesarovských transformací. Šifrovací a dešifrovací zobrazení definujeme jako
\[\begin{matrix}
c_i = | p_i + k_{|i|_n} |_m, \\
p_i = | c_i - k_{|i|_n} |_m,
\end{matrix}\]kde \(n\) se nazývá periodou Vigenèrovy šifry (nebo také délkou klíče) a \(m\) označuje velikost abecedy.

## Poznámka Anki 1677071519497

Karty Anki: 1677071519498
GUID: eYCxN^GtNm; štítky: bi-kab::p01 bi-spol::10.

### Otázka (Front)

Co je to konfúze a difúze?

### Odpověď (Back)

**Konfúze **se snaží skrýt vztah ŠT a klíče, tedy ztížit určení způsobu transformace OT a klíče na ŠT. Konfúze je dosahováno v substitučních šifrách. **Difúze** se snaží narušit systematické struktury v OT, tedy rozptýlit informace o OT po celé šíři ŠT. Difúze dosahují transpoziční šifry.

## Poznámka Anki 1677071765636

Karty Anki: 1677071765636
GUID: f[w$O$Q^>h; štítky: bi-kab::p01 bi-spol::10.

### Otázka (Front)

Popište sloupcovou transpoziční šifru.

### Odpověď (Back)

BÚNO předpokládejme pětisloupcovou transpozici. OT rozdělíme do bloků po pěti symbolech a vepíšeme je do matice jako
\[\begin{matrix}
p_1 & p_2, & p_3 & p_4 & p_5 \\
p_6 & p_7 & p_8 & p_9 & p_{10} \\
p_{11} & p_{12} & p_{13} & \dots \\
\dots
\end{matrix}\]Výsledný ŠT potom přečteme ze sloupců matice jako
\[p_1 p_6 p_{11} \dots p_2 p_7 p_{12} \dots p_3 p_8 p_{13} \dots\]

## Poznámka Anki 1677105189530

Karty Anki: 1677105189530
GUID: L/;mkt1K!1; štítky: bi-kab::p01 bi-spol::08.

### Otázka (Front)

Vyslovte Malou Fermatovu větu.

### Odpověď (Back)

Mějme prvočíslo \(p\) a \(a \in \mathbb Z\) takové, že \(\gcd (a, p) = 1\). Potom platí
\[a^{p - 1} \equiv 1 \pmod p.\]

## Poznámka Anki 1677105237715

Karty Anki: 1677105237715
GUID: o,V^ym`K|O; štítky: bi-kab::p01 bi-spol::08.

### Otázka (Front)

Definujte Eulerovu funkci \(\varphi\).

### Odpověď (Back)

Eulerova funkce \(\varphi(n): \mathbb N \to \mathbb N\) je zobrazení, které každému \(n \in \mathbb N\) přiřadí počet přirozených čísel menších nebo rovných \(n\), která jsou s \(n\) nesoudělná.

## Poznámka Anki 1677105654895

Karty Anki: 1677105654895
GUID: N)&6@zUNAt; štítky: bi-kab::p01 bi-spol::08.

### Otázka (Front)

Uveďte metody výpočtu Eulerovy funkce.

### Odpověď (Back)

Nechť \(p\) je prvočíslo a \(\alpha \in \mathbb N\). Potom
\[\varphi(p^\alpha) = p^\alpha - p^{\alpha - 1}.\]Nechť \(m\), \(n \in \mathbb N\) a \(\gcd(m, n) = 1.\) Potom
\[\varphi(m \cdot n) = \varphi(m) \cdot \varphi(n).\]Nechť \(m = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots  p_k^{\alpha_k}\) je kanonický (prvočíselný) rozklad složeného čísla \(m \in \mathbb N\). Potom
\[\varphi(m) = m \cdot \Big(1 - \frac 1 {p_1}\Big) \cdot \Big(1 - \frac 1 {p_2}\Big) \cdots \Big(1 - \frac 1 {p_k}\Big).\]

## Poznámka Anki 1677105831453

Karty Anki: 1677105831453
GUID: c5~QB89=5O; štítky: bi-kab::p01.

### Otázka (Front)

Vyslovte Eulerovu větu.

### Odpověď (Back)

Nechť \(a \in \mathbb Z\), \(m \in \mathbb N\) a \(\gcd(a, m) = 1\). Potom platí
\[a^{\varphi(m)} \equiv 1 \pmod m,\]kde \(\varphi\) označuje Eulerovu funkci.

## Poznámka Anki 1677106128493

Karty Anki: 1677106128493
GUID: sUOJMnEIrp; štítky: bi-kab::p01.

### Otázka (Front)

Jak převedeme hledání multiplikativní inverze na Bezoutovu rovnost?

### Odpověď (Back)

Mějme \(m \in \mathbb Z\), \(a \in \mathbb Z\) a předpokládejme \(\gcd(a, m) = 1\). Potom existuje právě jedno číslo \(b \in \mathbb Z_m\) takové, že
\[a \cdot b \equiv 1 \pmod m.\]Bezoutovu rovnost dostáváme ve tvaru
\[b \cdot a + k \cdot m = 1,\]kde \(k \in \mathbb Z\).

## Poznámka Anki 1678183685698

Karty Anki: 1678183685698
GUID: y(VkP8rF&N; štítky: bi-kab::p01.

### Otázka (Front)

Popište Caesarovu šifru.

### Odpověď (Back)

Caesarova šifra spadá mezi monoalfabetické a monografické substituční šifry. Šifrovací a dešifrovací zobrazení definujeme následovně
\[\begin{matrix}
c = | p + b |_m, \\
p = | c - b |_m.
\end{matrix}\]

