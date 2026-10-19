# BI-KAB – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-kab/BI-KAB.apkg; APKG SHA-256 080060aa53ee5f63eca18237eef611a0bfca99908f9ab640e349ebadb96964ec. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8571882594c00598a0b5a029eed57cadb06fe0563741a3f883a87eacef0c1588.
Původní balíčky: BI-KAB
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1677594040484

Karty Anki: 1677594040484
GUID: Fljj!{3<3I; štítky: bi-kab::p02.

### Otázka (Front)

Popište exponenciální šifru. Dokažte funkčnost dešifrovacího vztahu.

### Odpověď (Back)

Exponenciální šifra je symetrická šifra založená na modulárním umocňování. Mějme prvočíselný modul \(m\) a klíč \(e\) takový, že \(\gcd(e, m - 1) =1\). Symboly OT můžeme šifrovat zvlášť nebo po blocích. Šifrovací zobrazení potom definujeme jako
\[c = | p^e |_m.\]Před dešifrováním dopočteme dešifrovací klíč \(d\) pomocí vztahu
\[d = | e^{-1} |_{m - 1}\]a ŠT dešifrujeme pomocí zobrazení
\[p = | c^d |_m.\]V dešifrovacím zobrazení používáme Bézoutovu rovnost a Malou Fermatovu větu. Důkaz funkčnosti dešifrovacího vztahu je následující
\[| c^d |_m = | (p^e)^d |_m = | p^{e \cdot d} |_m \stackrel {\text{BR}}{=} | p^{1 + k(m - 1)} |_m = | p \cdot (p^{m - 1})^k |_m \stackrel {\text{MFV}}{=} | p |_m.\]

## Poznámka Anki 1677603322084

Karty Anki: 1677603322084
GUID: K>vsV=+kDE; štítky: bi-kab::p02.

### Otázka (Front)

Jaká je časová složitost šifrování pomocí exponenciální šifry?

### Odpověď (Back)

Modul \(m\) reprezentujeme pomocí \(k\) bitů, kde

\[k = \lceil\log_2(m) \rceil.\]Pro šifrování bloků OT budeme používat algoritmus square and multiply, který má časovou šložistost \(\mathcal O(k^3)\). Před dešifrováním si musíme zřídit dešifrovací klíč \(d\), což provedeme pomocí EEA/REA, který má časovou složitost \(\mathcal O \big(\log(2^k) \big)\), ale stačí ho provézt pouze jedenkrát. Při dešifrování jednoho bloku ŠT opět použijeme square and multiply algoritmus se složitostí \(\mathcal O(k^3)\).

## Poznámka Anki 1677603524988

Karty Anki: 1677603524989
GUID: DwGoBgXvX8; štítky: bi-kab::p02 bi-spol::09.

### Otázka (Front)

Jak by probíhalo prolamování exponenciální šifry?

### Odpověď (Back)

Předpokládejme, že známe modul \(m\) a délku použitého bloku. Pro prolomení šifry nám zbývá určit klíč \(e\). Zde vztahu
\[c = | p ^e |_m\]vyplývá, že
\[e = \log_p(c) \pmod m,\]což je ale problém diskrétního logaritmu.

## Poznámka Anki 1677603707425

Karty Anki: 1677603707425
GUID: r17aE^sJ.O; štítky: bi-kab::p02 bi-spol::09 ni-spol::01.

### Otázka (Front)

Definujte cyklickou grupu (cyclic group) a generátor cyklické grupy.

### Odpověď (Back)

Grupa \(G = (M, \circ)\) se nazývá **cyklická**, pokud existuje prvek \(a \in M\) takový, že \(\langle a \rangle = G\). Tomuto prvku říkáme **generátor cyklické grupy** \(G\).

### Doplňující pole (Extra)

Všechny prvky patřící do \(\langle a \rangle\) získáme pomocí „grupového obalu:“\[\langle a \rangle = \{ a \circ a \circ \cdots \circ a = a^k : k \in \mathbb Z \}.\]

## Poznámka Anki 1677604336021

Karty Anki: 1677604336021
GUID: sB+G;;U`KK; štítky: bi-ib::12 bi-ib::13 bi-kab::p02 bi-spol::09.

Metadata původního zdroje pro kartu 1677604336021: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište Diffie-Hellmanův algoritmus výměny klíče.

### Odpověď (Back)

Nechť \(m\) je velké prvočíslo a nechť \(g\) je generátorem grupy \(\mathbb Z_m^\times\). Každý subjekt nechť si náhodně zvolí svůj tajný klíč \(k_i\) tak, aby \(\gcd(k_i, m - 1) = 1\). Pro dva subjekty A a B s klíči \(k_A\) a \(k_B\) probíhá komunikace následovně:

- Subjekt A pošle subjektu B číslo \(y_A\), pro které platí
\[y_A = | g^{k_A} |_m.\]

- Subjekt B vypočítá společný klíč \(K\) na základě vztahu

\[K = | y_A^{k_B} |_m = | g^{k_A \cdot k_B} |_m.\]

- Subjekt B pošle subjektu A číslo \(y_B\), pro které platí

\[y_B = | g^{k_B} |_m.\]

- Subjekt A potom dopočítá společný klíč \(K\) vztahem

\[K = | y_B^{k_A} |_m = | g^{k_A \cdot k_B} |_m.\]Neautorizované subjekty odposlouchávající komunikaci nemohou \(K\) rekonstruovat v rozumném čase, neboť by byly nuceny řešit problém diskrétního logaritmu.

## Poznámka Anki 1677604600217

Karty Anki: 1677604600217
GUID: Rbxq3P_*;7; štítky: bi-ib::12 bi-kab::p02 bi-spol::09.

### Otázka (Front)

Definujte diskrétní logaritmus. Kdy je jeho existence zaručena?

### Odpověď (Back)

Nechť \((M, \circ)\) je grupa a \(a\), \(b\) a \(x\) jsou její prvky. Potom \(x\) nazveme diskrétním logaritmem \(a\) při základu \(b\), když platí
\[\log_b(a) = x \Leftrightarrow \underbrace {b \circ b \circ \dots \circ b}_{x\text{-krát}} = a.\]Tedy v multiplikativní grupě \((M, \times)\) platí
\[\log_b(a) = x \Leftrightarrow b^x = a,\]a v aditivní grupě \((M, +)\) platí
\[\log_b(a) = x \Leftrightarrow x \cdot b = a.\]Existence diskrétního logaritmu je zaručena v případě, že \((M, \circ)\) je cyklická grupa a \(b\) je její generátor.

