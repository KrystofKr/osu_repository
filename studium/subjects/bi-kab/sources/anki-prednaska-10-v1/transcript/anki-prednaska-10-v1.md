# BI-KAB – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-kab/BI-KAB.apkg; APKG SHA-256 080060aa53ee5f63eca18237eef611a0bfca99908f9ab640e349ebadb96964ec. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8571882594c00598a0b5a029eed57cadb06fe0563741a3f883a87eacef0c1588.
Původní balíčky: BI-KAB
Rozsah: 19 poznámek, 19 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1683637462961

Karty Anki: 1683637462962
GUID: Nj@t@d-7Lv; štítky: bi-kab::p10 bi-spol::08 bi-spol::09.

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

## Poznámka Anki 1683637694530

Karty Anki: 1683637694530
GUID: E6hX]*Ri$S; štítky: bi-kab::p10.

### Otázka (Front)

Definujte kvadratické residuum a nonresiduum.

### Odpověď (Back)

Mějme kladné celé číslo \(m\). Řekneme, že \(a\) je **kvadratické residuum** modulo \(m\), pokud \(\gcd(a, m) = 1\) a kongruence
\[x^2 \equiv a \pmod m\]má nějaké řešení pro \(x\). Pokud řešení neexistuje, nazveme \(a\) **kvadratickým nonresiduem**.

## Poznámka Anki 1683637834850

Karty Anki: 1683637834850
GUID: Megr/&Q?5p; štítky: bi-kab::p10.

### Otázka (Front)

Vyslovte větu o kvadratickém residuu v prvočíselném modulu.

### Odpověď (Back)

Mějme prvočíslo \(p\) a \(a\) takové, že \(\gcd(a, p) = 1\). Potom kongruence
\[x^2 \equiv a \pmod p\]má buď právě dvě vzájemně nekongruentní řešení modulo \(p\), nebo nemá řešení žádné.

## Poznámka Anki 1683638018799

Karty Anki: 1683638018799
GUID: biAu^}>cD{; štítky: bi-kab::p10.

### Otázka (Front)

Vyslovte větu o kvadratickém residuu ve složeném modulu. Z čeho tato věta vyplývá?

### Odpověď (Back)

Nechť \(n = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots p_k^{\alpha_k}\) je kanonický rozklad čísla \(n\). Potom platí, že \(a\) je kvadratickým residuem modulo \(n\), právě když je kvadratickým residuem v modulech \(p_1^{\alpha_1}, p_2^{\alpha_2}, \dots p_k^{\alpha_k}\). To vyplývá z Čínské věty o zbytcích.

## Poznámka Anki 1683638965911

Karty Anki: 1683638965911
GUID: bMR@1y?%!Z; štítky: bi-kab::p10.

### Otázka (Front)

Vyslovte větu o hledání generátorů.

### Odpověď (Back)

Nechť \(p\) je prvočíslo a \(p - 1 = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots p_k^{\alpha_k}\) je kanonický rozklad čísla \(p - 1\). Číslo \(g\) je generátorem modulo \(p\), pokud pro všechny hodnoty \(p_1^{\alpha_1}, p_2^{\alpha_2}, \dots p_k^{\alpha_k}\) platí
\[| g^{ \frac {p - 1}{p_i^{\alpha_i}} } |_p \neq 1.\]

## Poznámka Anki 1683639599943

Karty Anki: 1683639599944
GUID: Cs[c0qd?lD; štítky: bi-kab::p10.

### Otázka (Front)

Uveďte rady pro generování prvočísel.

### Odpověď (Back)

Chceme vygenerovat náhodné prvočíslo \(p\). Potom je doporučeno:

- \(\text{MSB} = 1 \) - zaručí požadovanou délku čísla;

- \(\text{LSB} = 1\) - zaručí, že číslo je liché;

- testovat prvočíselnost pomocí malých prvočísel (menších než \(1000\));
- provést Rabin-Millerův test s náhodně generovanými bázemi alespoň 5-krát.

V případě, že \(p\) v nějakém bodu selže, je potřeba vygenerovat nové.

## Poznámka Anki 1683640769136

Karty Anki: 1683640769136
GUID: nfzLQ5,uW}; štítky: bi-kab::p10.

### Otázka (Front)

Co je to silné prvočíslo?

### Odpověď (Back)

Silné prvočíslo \(p\) musí splňovat následující vlastnosti:

- musí být dostatečně dlouhé,
- číslo \(p - 1\) musí mít velké prvočinitele (např. \(p'\)),
- čísla \(p' - 1\) a \(p' + 1\) musí mít velké prvočinitele,
- číslo \(\frac{p - 1}2\) musí být prvočíslo.

## Poznámka Anki 1683654089492

Karty Anki: 1683654089492
GUID: bvLB5G3hCS; štítky: bi-kab::p10.

### Otázka (Front)

Popište Rabin-Millerův test prvočíselnosti.

### Odpověď (Back)

Mějme prvočíslo \(p\), které chceme testovat a zvolme náhodně bázi \(a\) takovou, že \(\gcd(a, p) = 1\). Pokud by bylo \(p\) prvočíslem, tak by mělo podle Malé Fermatovy věty platit
\[a^{p - 1} - 1 \equiv 0 \pmod p.\]Protože prvočísla jsou vždy lichá (sudé číslo tedy nedává smysl ani testovat), můžeme výraz rozepsat na
\[(a^\frac{p - 1}2 - 1)(a^\frac{p - 1}2 + 1) \equiv 0 \pmod p.\]V tomto rozkladu pokračujeme, dokud je to možné, tedy dokud je exponent sudé číslo. Následně vyhodnotíme postupně zleva všechny závorky, přičemž mohou nastat následující situace:

- některá ze závorek vyjde nula - v takovém případě výraz platí a \(p\) může být prvočíslo;
- všechny závorky jsou různé od nuly - v takovém případě výraz neplatí a báze \(a\) je **svědkem **toho, že \(p\) je složené číslo.

V případě, že test provedeme úspěšně (nenalezneme svědka) pro \(n\) bází, pak je pravděpodobnost toho, že \(p\) je prvočíslo rovna

\[1 - \Big( \frac 1 4 \Big)^n.\]

## Poznámka Anki 1683656852707

Karty Anki: 1683656852707
GUID: qA{Jbb*=9r; štítky: bi-ib::19 bi-kab::p10.

### Otázka (Front)

Co je to náhodné číslo a generátor náhodných čísel (RNG)?

### Odpověď (Back)

**Náhodné číslo** je číslo vygenerované procesem, který má nepředvídatelný výsledek a jehož průběh nelze přesně reprodukovat. Tomuto procesu říkáme **generátor náhodných čísel **(RNG).

## Poznámka Anki 1683657095815

Karty Anki: 1683657095815
GUID: bY2h9T.gAX; štítky: bi-kab::p10.

### Otázka (Front)

Co je to generátor pseudonáhodných čísel (PRNG)?

### Odpověď (Back)

Generátor pseudonáhodných čísel (PRNG) je deterministrický algoritmus, jehož výstup je posloupnost, která sice ve skutečnosti není náhodná, ale útočníkovi se jako náhodná jeví, pokud mu nejsou známy některé parametry generátoru.

## Poznámka Anki 1683657370779

Karty Anki: 1683657370779
GUID: dB7&H(&?8a; štítky: bi-ib::19 bi-kab::p10.

Metadata původního zdroje pro kartu 1683657370779: původní příznak autora 7.

### Otázka (Front)

Popište lineární kongruentní generátor.

### Odpověď (Back)

Jde o jeden z nejstarších a nejznámějších PRNG, který však není kryptograficky bezpečný. Používá vztah
\[X_{n + 1} = a \cdot X_n + c \pmod m,\]kde \(m\) je modul (často mocnina dvou), \(a\) je násobitel, \(c\) je inkrement, \(X_0\) je počáteční hodnota (seed) a 
\((X)_{n = 1}^\infty\) je posloupnost pseudonáhodných čísel. Platí, že posloupnost pseudonáhodných čísel se začne opakovat nejvýše po \(m\) iteracích.

## Poznámka Anki 1683657589810

Karty Anki: 1683657589810
GUID: KS*$*7Zo|R; štítky: bi-ib::19 bi-kab::p10.

### Otázka (Front)

Co je to next-bit test pseudonáhodného generátoru?

### Odpověď (Back)

Řekneme, že PRNG je odolný proti next-bit test v případě, že i přestože je známo prvních \(k\) bitů náhodné posloupnosti, neexistuje algoritmus s polynomiální složitostí, který by dokázal předpovědět \(k + 1\) bit s pravděpodobností úspěchu vyšší než \(\frac 1 2\).

## Poznámka Anki 1683657796145

Karty Anki: 1683657796145
GUID: k$u.h-2wtN; štítky: bi-ib::19 bi-kab::p10.

### Otázka (Front)

Co je to state compromise pseudonáhodného generátoru?

### Odpověď (Back)

Řekneme, že PRNG je odolný proti state compromise v případě, že i přestože je zjištěn vnitřní stav generátoru, nelze zpětně zrekonstruovat dosavadní vygenerovanou náhodnou posloupnost. Navíc pokud do generátoru vstupuje další entropie, nemělo by být možné předpovědět ani jeho stav v další iteraci.

## Poznámka Anki 1683658040142

Karty Anki: 1683658040142
GUID: G~Kg&G@o7V; štítky: bi-ib::19 bi-kab::p10.

### Otázka (Front)

Uveďte způsoby, kterými lze realizovat PRNG.

### Odpověď (Back)

Kryptograficky bezpečné PRNG lze realizovat následujícími způsoby:

- **bezpečná bloková šifra v režimu CTR** - náhodně se zvolí klíč (seed) a počáteční hodnota čítače \(i\) a pomocí těchto parametrů se šifrují postupně hodnoty \(i, i + 1, \dots\);

- **kryptograficky bezpečná hashovací funkce aplikovaná na čítač** - náhodně se zvolí počáteční hodnota čítače \(i\) a následně hashuje posloupnost \(i, i + 1, \dots\);

- **proudové šifry** - proudová šifra je v zásadě PRNG, jehož výstup se kombinuje s plaintextem;

- **algoritmy založené na teorii čísel** - musí u nich být proveden důkaz bezpečnosti.

## Poznámka Anki 1683658550645

Karty Anki: 1683658550645
GUID: oDrdNol8Av; štítky: bi-ib::19 bi-kab::p10.

### Otázka (Front)

Popište pseudonáhodný generátor Blum-Blum-Shub.

### Odpověď (Back)

Blum-Blum-Shub je PRNG, který je považován za kryptograficky bezpečný. Používá vztah
\[X_{n + 1} = X_n^2 \bmod m,\]kde modul \(m\) je součinem dvou velkých prvočísel \(p\) a \(q\), pro něž platí:

- \(p \equiv 3 \pmod 4\) a \(q \equiv 3 \pmod 4\),
- \(\gcd \big(\varphi(p - 1), \varphi(q - 1) \big)\) je malé.

\(X_0\) je potom počáteční prvek (seed) a \((X_n)_{n = 1}^\infty\) je posloupnost pseudonáhodných čísel. Výstupem generátoru však nebývá samotné \(X_n\), ale spíše jeho parita či několik nejméně významných bitů.

## Poznámka Anki 1683658791342

Karty Anki: 1683658791343
GUID: ty^Lkgeqq,; štítky: bi-ib::19 bi-kab::p10.

Metadata původního zdroje pro kartu 1683658791343: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište generátory skutečně náhodných čísel (TRNG)?

### Odpověď (Back)

Generátory skutečně náhodných čísel (TRNG) jsou nedeterministrické a využívají zdroje entropie, kterými jsou zpravidla fyzikální nebo vnější jevy. Příkladem může být:

- radioaktivní rozpad,
- atomosférický šum,
- teplotní šum,
- chování uživatele.

Oproti generátorům pseudonáhodných čísel (PRNG) ale často mívají horší statistické vlastnosti, a proto se u nich používá post-processing.

## Poznámka Anki 1683659004868

Karty Anki: 1683659004868
GUID: AmIg/@v*XF; štítky: bi-ib::19 bi-kab::p10.

### Otázka (Front)

Co je to post-processing u TRNG? Uveďte příklady.

### Odpověď (Back)

Protože výstupy TRNG mají zpravidla horší statistické vlastnosti, je nutné je dále zpracovávat. Post-processing se provádí zejména za cílem:

- ostranění nevyváženosti jedniček a nul a zajištění rovnoměrného rozdělení,
- zhuštení entropie výstupních bitů za cenu snížení rychlosti jejich generování.

Způsoby, kterými lze zajistit lepší statistické vlastnosti TRNG jsou:

- XOR výstupu TRNG s výstupem kryptograficky silného PRNG,
- XOR výstupů dvou nebo více různých TRNG,
- hashování výstupu TRNG kryptograficky silnou hashovací funkcí,
- použití John von Neumannova dekorelátoru nebo XOR korektoru.

## Poznámka Anki 1683659861776

Karty Anki: 1683659861776
GUID: nY|@B{XnkI; štítky: bi-ib::19 bi-kab::p10.

### Otázka (Front)

Popište John von Neumannův dekorelátor.

### Odpověď (Back)

John von Neumannův dekorelátor se používá v post-processingu TRNG, kde je schopen eliminovat nevyváženost a snížit korelaci výstupu. Bity se ze vstupu odebírají po dvojicích a výstup je následující:

| 
      **vstup** | 
      **výstup** | 

| 
      \(\mathtt{00}\) nebo \(\mathtt{11}\) | 
       vstup je zahozen | 

| 
      \(\mathtt{01}\)
 | 
      \(\mathtt 0\)
 | 

| 
      \(\mathtt{10}\)
 | 
      \(\mathtt 1\)
 |

## Poznámka Anki 1683661065699

Karty Anki: 1683661065699
GUID: eb#&;kF|yJ; štítky: bi-ib::19 bi-kab::p10.

### Otázka (Front)

Jak lze testovat náhodné generátory? Uveďte příklady.

### Odpověď (Back)

K testování RNG se používají statistické testy, které mohou odhalit nekvalitní generátory. Nedokáží však dokázat, že generátor kvalitní je. Jsou založeny na testování statistických hypotéz. Mezi příklady testů náhodných generátorů patří:

- **frekvenční test** - testuje podíl jedniček a nul;

- **runs test** - testuje, zda počet a délka řetězců po sobě jdoucích stejných bitů odpovídá náhodné posloupnosti;
- **test hodností matic** - testuje na lineární závistlosti podposloupností;

- **spektrální test** - testuje na periodicitu;

- **Mauerův univerzální statistický test** - testuje, zda lze posloupnost bezeztrátově komprimovat (výrazně komprimovatelná posloupnost nemá dostatečnou entropii).

