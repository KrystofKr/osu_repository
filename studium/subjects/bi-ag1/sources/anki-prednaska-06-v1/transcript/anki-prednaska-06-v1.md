# BI-AG1 – Přednáška 06

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1666596208461

Karty Anki: 1666596208461
GUID: b2tE,kqU[K; štítky: bi-ag1::p06 bi-spol::04 bi-spol::23.

### Otázka (Front)

Definujte binární vyhledávací strom.

### Odpověď (Back)

Binární vyhledávací strom (BVS) je binární strom, v jehož každém vrcholu \(v\) je uložen unikátní klíč \(k(v)\) a pro jehož vrchol \(v\) platí:

- Pokud \(a \in L(v)\), pak \(k(a) < k(v)\).
- Pokud \(b \in R(v)\), pak \(k(b) > k(v)\).

\(L(v)\) představuje levý podstrom vrcholu \(v\) a \(R(v)\) představuje pravý podstrom vrcholu.

## Poznámka Anki 1666596859364

Karty Anki: 1666596859365
GUID: tylP7/$fwG; štítky: bi-ag1::p06 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište algoritmus výpisu vzestupně uspořádaných klíčů BVS (\(\mathtt{BVSShow}(v)\)) a uveďte jeho časovou složitost.

### Odpověď (Back)

**Vstup**
Ukazatel na kořen \(v\) nějakého BVS \(T(v)\), kde \(T(v)\) označuje podstrom tvořený kořenem \(v\) a všechny jeho potomky.

**Výstup**
Vzestupně uspořádáná posloupnost klíčů všech vtcholů v \(T(v)\).

**Postup**

- pokud \(v = \emptyset\), konec

- zavoláme \(\mathtt{BVSShow}(l(v))\)
- vypíšeme \(k(v)\)
- zavoláme \(\mathtt{BVSShow}(r(v))\)

**Složitost**

\(\mathtt{BVSShow}(v)\) vypíše klíče v čase \(\mathcal{O}(|T(v)|)\).

## Poznámka Anki 1666597065383

Karty Anki: 1666597065384
GUID: P<[M6<{Vw8; štítky: bi-ag1::p06 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište algoritmus nalezení minima BVS (\(\mathtt{BVSMin}(v)\)) a uveďte jeho časovou složitost.

### Odpověď (Back)

Nejmenší klíč se bude nacházet nejvíce vlevo v BVS. Algoritmus implementujeme rekurzivně a má časovou složitost \(\mathcal{O}(h(T(v)))\).

## Poznámka Anki 1666603261180

Karty Anki: 1666603261180
GUID: O-=n/(E4}~; štítky: bi-ag1::p06 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište algoritmus nalezení předchůdce vrcholu v BVS (\(\mathtt{BVSPred}(v, w)\)) a uveďte jeho složitost.

### Odpověď (Back)

**Vstup**
Ukazatel na kořen \(v\) nějakého BVS \(T(v)\) a na nějaký jeho vrchol \(w\).

**Výstup**
Ukazatel na předchůdce \(w\) v \(T(v)\).

**Postup**

- Klíč předchůdce prvku \(w\) v \(T(v)\) je ve vzestupném výpisu klíčů algoritmem \(\mathtt{BVSShow}\) levým sousedem \(k(w)\).
- Pokud má \(w\) v \(T(v)\) levý podstrom \(L(w)\), pak je předchůdce \(w\) jeho maximem.
- V opačném případě je předchůdcem \(w\) první předek, do kterého vstoupíme zprava při průchodu nahoru.
- Evidentně, prvek s nejmenším klíčem předchůdce nemá, neboť nesplňuje ani jednu podmínku.

**Složitost**

\(\mathtt{BVSPred}(v, w)\) má složitost \(\mathcal{O}(h(T(v)))\).

## Poznámka Anki 1666603512785

Karty Anki: 1666603512785
GUID: x4>fcZT7na; štítky: bi-ag1::p06 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište algoritmus nalezení vrcholu s daným klíčem v BVS (\(\mathtt{BVSFind}(v,x)\)) a uveďte jeho časovou složitost.

### Odpověď (Back)

**Vstup**
Ukazatel na kořen nějakého BVS \(T(v)\) a klíč \(x\).

**Výstup**
Ukazatel na vrchol s klíčem \(x\), pokud takový v \(T(v)\) existuje, jinak \(\emptyset\).

**Postup**

- pokud \(v = \emptyset\): vrať \(\emptyset\)

- pokud \(x = k(v)\): vrať ukazatel na \(v\)
- pokud \(x < k(v)\): vrať \(\mathtt{BVSFind}(l(v), x)\)
- pokud \(x > k(v)\): vrať \(\mathtt{BVSFind}(r(v), x)\)

**Složitost**

\(\mathtt{BVSFind}(v,x)\) má časovou složitost \(\mathcal{O}(h(T(v)))\).

## Poznámka Anki 1666604111487

Karty Anki: 1666604111487
GUID: o3D-Fw?et%; štítky: bi-ag1::p06 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište algoritmus odstranění vrcholu s daným klíčem z BVS (\(\mathtt{BVSDelete}(v, x)\)) a uveďte jeho časovou složitost.

### Odpověď (Back)

**Vstup**

Ukazatel na kořen \(v\) nějakého BVS a klíč \(x\).

**Výstup**

Ukazatel na kořen BVS, ze kterého byl odstraněn vrchol s klíčem \(x\), pokud takový vrchol existoval.

**Postup**

- Nejdříve nalezneme vrchol, který obsahuje klíč, který chceme smazat.
- Při mazání vrcholu může nastat několik různých případů.

1. Pokud takový vrchol neexistuje, strom necháme beze změny.
2. Pokud je vrchol listem, odtrhneme jej od stromu.
3. Má-li vrchol právě jednoho syna, nahradíme ho tímto synem.
4. Má-li nalezený vrchol \(u\) dva syny, pak jej nemůžeme odstranit přímo.

- Využijeme toho, že vrchol \(u\) má v BVS následníka \(w = \mathtt{BVSMin}(r(u))\) a ten má nejvýše jednoho syna.
- Klíč vrcholu \(u\) nahradíme klíčem vrcholu \(w\).
- Aplikací případu 2 nebo 3 pak odstraníme vrchol \(w\) z BVS.

**Složitost**

\(\mathtt{BVSDelete}(v, x)\) má časovou složitost \(\mathcal{O}(h(T(v)))\).

## Poznámka Anki 1666604460149

Karty Anki: 1666604460149
GUID: yhX%z-)1NF; štítky: bi-ag1::p06 bi-spol::04.

### Otázka (Front)

Definujte dokonale vyvážený BVS. Co platí pro počet jeho hladin a jaký to má důsledek na operace s ním spjaté?

### Odpověď (Back)

BVS \(T\) je dokonale vyvážený, pokud pro každý jeho vrchol \(v \in V(T)\) platí
\[\big| |L(v)| - |R(v)| \big| \leq 1,\]kde \(L(v)\) resp. \(R(v)\) označují levý resp. pravý podstrom vrcholu \(v\). Dokonale vyvážený BVS o \(n\) vrcholech má právě
\[\lfloor \log_2 n \rfloor + 1\]hladin, a proto mají operace nad ním (\(\mathtt{BVSFind}\), \(\mathtt{BVSMin}\), \(\mathtt{BVSInsert}\), \(\mathtt{BVSDelete}\)) časovou složitost \(\mathcal O(\log n)\).

## Poznámka Anki 1666604726197

Karty Anki: 1666604726197
GUID: dqKXAa`YO=; štítky: bi-ag1::p06 bi-spol::04 bi-spol::23.

### Otázka (Front)

Definujte AVL strom.

### Odpověď (Back)

BVS je AVL stromem, pokud pro každý jeho vrchol \(v\) platí \(|h(L(v)) - h(R(v))| \leq 1\).

## Poznámka Anki 1666604981439

Karty Anki: 1666604981439
GUID: Kk3TgfQy;:; štítky: bi-ag1::p06 bi-spol::04 bi-spol::23.

### Otázka (Front)

Definujte zaneménko vrcholu AVL stromu. Jakých hodnot může v korektním AVL stormu nabývat?

### Odpověď (Back)

Znaménko vrcholu definujeme pro vrchol \(v\) jako \[\delta(v) = h \big( R(v) \big) - h \big( L(v) \big).\]V korektním AVL stromu může nabývat pouze hodnot:

- \(\delta(v) = +1\) - pravý podstrom je hlubší,

- \(\delta(v) = -1\) - levý podstrom je hlubší,

- \(\delta(v) = 0\) - oba podstromy jsou stejně hluboké.

## Poznámka Anki 1666605331553

Karty Anki: 1666605331553
GUID: z7^L~7S[/e; štítky: bi-ag1::p06 bi-spol::04.

### Otázka (Front)

Popište jednoduchou rotaci doprava (R) AVL stromu.

### Odpověď (Back)

[Obrázek: paste-e1374eb97b97044e49f203ddf1f01a8eb0b89768.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1666605386507

Karty Anki: 1666605386507
GUID: F-7ekd*[iN; štítky: bi-ag1::p06 bi-spol::04.

### Otázka (Front)

Popište jednoduchou rotaci doleva (L) AVL stromu.

### Odpověď (Back)

[Obrázek: paste-8597dcb9ef900a4f77294e09acf03ade83bfc05c.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1666609217699

Karty Anki: 1666609217699
GUID: j7P>&lP3]d; štítky: bi-ag1::p06 bi-spol::04.

### Otázka (Front)

Popište dvojitou rotaci LR AVL stromu.

### Odpověď (Back)

[Obrázek: paste-40d27a3ab691132c8efcc9ea85f3034b8ba6fb1e.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1666609299945

Karty Anki: 1666609299946
GUID: cUEuHz?Sn>; štítky: bi-ag1::p06 bi-spol::04.

### Otázka (Front)

Popište dvojitou rotaci RL AVL stromu.

### Odpověď (Back)

[Obrázek: paste-c57f3f19b2c5e2db4b11745a5e8cf9b6750e66e0.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1666645957318

Karty Anki: 1666645957318
GUID: xsUD?AIPq0; štítky: bi-ag1::p06 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište aloritmus přidání prvku do AVL stromu (\(\mathtt{AVLInsert}\)).

### Odpověď (Back)

- Nový vrchol vložíme standardně jako list se znaménkem \(0\).
- Z prázdného podstromu hloubky \(0\) se tak stal jednovrcholový podstrom hloubky \(1\).
- Potom je třeba přepočítat hloubky stromů na cestě z jeho rodiče do kořene.
- Proto budeme propagovat nahoru informaci o tom, že se zvětšila hloubka podstromu.
- Popíšeme propagaci pro vrchol \(x\), do kterého přišla z jeho levého syna informace o propagaci
**Vrchol **\(x\)** měl znaménko **\(+1\)**.**

- Hloubka levého podstromu se právě vyrovnala s hloubkou pravého, čili znaménko \(x\) se změní na \(0\).

- Hloubka podstromu \(T(x)\) se ale nezměnila, takže propagování informace zastavíme.

**Vrchol **\(x\)** měl znaménko **\(0\)**.**

- Znaménko \(x\) se změní na \(-1\).
- Hloubka podstromu \(T (x)\) se zvětšila o jedna, takže musíme pokračovat v propagování.

**Vrchol ** \(x\)  **měl znaménko **\(-1\).

- \(\delta(x)\) tedy bude \(-2\) a je potřeba vyvažovat.

- Označme \(y\) vrchol, z nějž přišla informace o prohloubení, čili levého syna vrcholu \(x\).

1. Vrchol \(y\) má znaménko \(-1\) - provedeme jednoduchou rotaci R hrany \(\set{x,y}\) a propagování zastavíme.
2. Vrchol \(y\) má znaménko \(+1\) - provedeme dvojitou LR rotaci, která celou konfiguraci překoření za pravého syna \(z\) vrcholu \(y\) a propagování zastavíme.
3. Vrchol \(y\) má znaménko \(0\) - tato situace nemůže nastat.

## Poznámka Anki 1666646902297

Karty Anki: 1666646902297
GUID: oXb7e;<[y6; štítky: bi-ag1::p06 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište algoritmus odstranění prvku z AVL stromu (\(\mathtt{AVLDelete}\)).

### Odpověď (Back)

- Vrchol smažeme podle \(\mathtt{BVSDelete}\) a po cestě zpět do kořene propagujeme informaci o snížení hloubky podstromu.
- Pokaždé mažeme list nebo vrchol s jediným synem, takže stačí propagovat od místa smazaného vrcholu nahoru.
- Popíšeme propagaci pro vrchol \(x\), do kterého přišla z levého syna informace o snížení hloubky podstromu.

**Vrchol **\(x\) **má znaménko **\(-1\)**.**

- Hloubka levého podstromu se právě vyrovnala s hloubkou pravého, znaménko vrcholu \(x\) se mění na \(0\).
- Hloubka podstromu \(T(x)\) se snížila, takže pokračujeme v propagování.

**Vrchol **\(x\) **má znaménko **\(0\)**.**

- Znaménko \(x\) se změní na \(+1\).
- Hloubka podstromu \(T(x)\) se nezměnila, takže propagování zastavíme.

**Vrchol **\(x\)** má znaménko **\(+1\)**.**

- Tehdy se jeho znaménko změní na \(+2\) a musíme vyvažovat.

- Označme \(y\) pravého syna vrcholu \(x\).

1. Vrchol \(y\) má znaménko \(+1\) - provedeme jednoduchou rotaci L hrany \(\set{x,y}\) a pokračujeme v propagování.
2. Vrchol \(y\) má znaménko \(0\) - provedeme jednoduchou rotaci L hrany \(\set{x,y}\) a zastavíme propagování.
3. Vrchol \(y\) má znaménko \(-1\) - provedeme dvojitou RL rotaci, která celou konfiguraci překoření za levého syna vrcholu \(y\) a pokračujeme v propagování.

## Poznámka Anki 1673959998919

Karty Anki: 1673959998919
GUID: F9PM&OgoBn; štítky: bi-ag1::p06 bi-spol::04.

### Otázka (Front)

Vyslovte a dokažte větu o hloubce AVL stromu.

### Odpověď (Back)

AVL strom o \(n\) vrcholech má hloubku \(\Theta(\log n)\).

**Důkaz**

- Definujme \(A_h\) jako minimální počet vrcholů AVL stromu hloubky \(h\).

- Ukážeme, že \(A_h\) roste exponenciálně s \(h\).
- Nejmenší AVL stromy dané hloubky jsou maximálně "hloubkově rozvážené" v mezích definice, čili v každém vnitřním vrchol \(v\) platí \(|h(l(v))| - h(r(v))| = 1\).
- Pro \(h \leq 4\) lze nejmenší AVL stromy hloubky \(h\) nalézt přímo:

 [Obrázek: paste-7c641c045da9b33b3b4007d65dc8c0d2659b9069.jpg; soubor je v media/ v doprovodném ZIP] 

- Obecně pak minimální AVL strom hloubky \(h\) musí mít jako podstromy minimální AVL stromy hloubky \(h - 1\) a \(h - 2\).
- Musí tedy platit \(A_h = A_{h - 1} + A_{h - 2} + 1\).
- Dokážeme indukcí, že \(A_{h + 1} \geq 2^{\frac h 2} \dot = 1,41^h\).

\[\text{ZK:} \qquad A_1 = 1 \geq 2^{\frac 0 2} = 1 \qquad \text{a} \qquad A_2 = 2 \geq 2^{\frac 1 2} \dot = 1,414.\]\[\text{IK:} \qquad A_{h + 1} = 1 + A_h + A_{ h - 1} > 2^{\frac{h - 1}2} + 2^{\frac{h - 2}2} = 2^{\frac h 2} \cdot (2^{-\frac 1 2} + 2^{-1}) > 2^{\frac h 2} \cdot (\frac 1 2 + \frac 1 2) = 2^{\frac h 2}.\]

- AVL strom hloubky \(h + 1\) má tedy nejméně \(\sqrt 2^h\) vrcholů.
- Proto AVL strom o \(n\) vrcholech má hloubku nejvýše \(\log_{\sqrt 2}(n) + 1\).
- A protože je binární, nemůže mít hloubku menší než \(\lfloor \log_2 n \rfloor\).
- Tedy hloubka AVL stromu o \(n\) vrcholech je \(\Theta(\log n)\).

