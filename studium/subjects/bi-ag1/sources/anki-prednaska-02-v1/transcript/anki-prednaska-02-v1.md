# BI-AG1 – Přednáška 02

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 27 poznámek, 27 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1664178285275

Karty Anki: 1664178285275
GUID: Bmkw+QIS}N; štítky: bi-ag1::p02 bi-spol::03 bi-spol::04.

### Otázka (Front)

Definujte souvislý a nesouvislý neorientovaný graf.

### Odpověď (Back)

Graf \(G\) je souvislý, jestliže v něm pro každé jeho dva vrcholy \((u, v)\) existuje \(u\text{-}v\text{-}\)cesta. Jinak je \(G\) nesouvislý.

## Poznámka Anki 1664178440474

Karty Anki: 1664178440474
GUID: gdsNyMUqdu; štítky: bi-ag1::p02 bi-spol::03 bi-spol::04.

### Otázka (Front)

Definujte souvislou komponentu grafu.

### Odpověď (Back)

[Obrázek: paste-058a5b57f0bc98c08e0954292e77f2dfb1aabcef.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1664179327289

Karty Anki: 1664179327289
GUID: bq,v`vcVJ*; štítky: bi-ag1::p02 bi-spol::03.

### Otázka (Front)

Jak zjistíme, zda je graf \(G\) souvislý?

### Odpověď (Back)

Spustíme \(\text{BFS}(G, s)\), kde \(s \in V(G)\). Pokud na konci \(\text{BFS}(G, s)\) zbydou nějaké neobjevené vrcholy, není graf \(G\) souvislý. V opačném případě je \(G\) souvislý.

## Poznámka Anki 1664179414547

Karty Anki: 1664179414547
GUID: p9)mzGau?c; štítky: bi-ag1::p02 bi-spol::03.

### Otázka (Front)

Mějme graf \(G\) a vrchol \(s\). Jak identifikujeme souvislou komponentu, do které \(s\) patří?

### Odpověď (Back)

Spustíme \(\text{BFS}(G, s)\). Všechny uzavřené vrcholy jsou součástí souvislé komponenty grafu \(G\), do které náleží vrchol \(s\).

## Poznámka Anki 1664179556404

Karty Anki: 1664179556404
GUID: iWz3Nz,%pq; štítky: bi-ag1::p02 bi-spol::03.

### Otázka (Front)

Jak identifikujeme všechny souvislé komponenty grafu \(G\).

### Odpověď (Back)

Spustíme \(\text{BFS}(G, s)\), kde \(s \in V(G)\). Poté opakujeme s \(t \in V(G)\) nějakým dosud neobjeveným vrcholem grafu \(G\) dokud zbývají neobjevené vrcholy. Skupiny vrcholů uzavřených jednotlivými běhy \(\text{BFS}\) jsou všechny souvislé komponenty grafu \(G\).

## Poznámka Anki 1664179860868

Karty Anki: 1664179860868
GUID: ukDN1.PmI1; štítky: bi-ag1::p02 bi-spol::20.

### Otázka (Front)

Popište výpočetní model random-access machine (RAM).

### Odpověď (Back)

RAM je idealizovaný počítač s očíslovanými paměťovými buňkami, který vykonává instrukce jednu po druhé. Tento model umožňuje přesně počítat, kolik kroků algoritmus potřebuje, a tím určovat jeho časovou složitost.;

- **aritmeticko-logické** - mají obvykle dva vstupní a jeden výstupní argument, které mohou být zadány jako přímá konstanta, přímo adresovaná paměťová buňka nebo nepřímo adresovaná paměťová buňka;

- **řídící** - nepodmíněné skoky, podmíněné skoky a instrukce zastavení programu.

## Poznámka Anki 1664179911593

Karty Anki: 1664179911593
GUID: n^{Yx+?%HE; štítky: bi-ag1::p02 bi-spol::20.

### Otázka (Front)

Vyjmenujte vlastosti random-access machine (RAM) modelu.

### Odpověď (Back)

- Na začátku výpočtu obsahuje paměť v určených buňkách vstup a obsah ostatních buněk je nedefinován.
- Potom je program sekvenčně prováděn, instrukce za instrukcí.
- Procesor v každém kroku provede právě jednu instrukci.
- Po zastavení programu je obsah paměti v určených buňkách interpretován jako výstup programu.

## Poznámka Anki 1664179954150

Karty Anki: 1664179954150
GUID: B~HvipqTZF; štítky: bi-ag1::p02.

### Otázka (Front)

Definujte velikost vstupu RAM.

### Odpověď (Back)

Velikost vstupu je počet paměťových buněk, které vstup zabírá.

## Poznámka Anki 1664180011378

Karty Anki: 1664180011378
GUID: lH+GYFlyl{; štítky: bi-ag1::p02 bi-spol::20.

### Otázka (Front)

Definujte časovou složitost programu.

### Odpověď (Back)

Časová složitost programu (v nejhorším případě) pro vstup velikosti \(N\) je maximum z počtu vykonaných instrukcí přes všechny možné (povolené) vstupy velikosti nejvýše \(N\).

## Poznámka Anki 1664180052866

Karty Anki: 1664180052866
GUID: wy;woti@,a; štítky: bi-ag1::p02 bi-spol::20.

### Otázka (Front)

Definujte paměťovou složitost programu.

### Odpověď (Back)

Paměťová složitost programu (v nejhorším případě) pro vstup velikosti \(N\) je maximum z počtu použitých paměťových buněk přes všechny možné (povolené) vstupy velikosti nejvýše \(N\).

## Poznámka Anki 1664182848720

Karty Anki: 1664182848720
GUID: ktuA>_=f]|; štítky: bi-ag1::p02.

### Otázka (Front)

Definujte matici sousednosti. Jaká je její paměťová složitost?

### Odpověď (Back)

Nechť \(G = (V, E)\) je graf s \(V = \set{v_1, v_2, \dots, v_n}\). Matice sousednosti grafu \(G\) je čtvercová matice \(A_G = (a_{ij})_{i, j = 1}^n\) definovaná předpisem
\[a_{i, j} =
\begin{cases}
  1 & \text{když } \set{v_i, v_j} \in E, \\
  0 & \text{jinak}
\end{cases}\]Paměťová složitost: \(\mathcal{O}(n^2)\).

## Poznámka Anki 1664182960012

Karty Anki: 1664182960012
GUID: L_Ioxt=sSn; štítky: bi-ag1::p02.

### Otázka (Front)

Definujte seznam sousedů. Jaká je jeho paměťová složitost?

### Odpověď (Back)

Pro každý vrchol \(v\) grafu \(G = (V, E)\) uchováváme seznam jeho sousedů (např. spojový seznam).
Paměťová složitost: \(|V| + 2|E| = \mathcal{O}(n + m)\).

## Poznámka Anki 1664183269499

Karty Anki: 1664183269499
GUID: eaSzH!MEvV; štítky: bi-ag1::p02 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o časové složitosti algoritmu \(\text{BFS}\).

### Odpověď (Back)

Alogritmus \(\text{BFS}(G)\) má při reprezentaci grafu \(G\) seznamem sousedů časovou složitost \(\mathcal{O}(|V| + |E|)\).

**Důkaz**

- Každý vrchol je přidán do fronty \(Q\) nejvýše jednou, neboť je předtím otevřen a nemůže už tedy vícekrát splnit podmínku, že je nenalezený.

- V každé iteraci vnějšího cyklu je jeden vrchol odebrán z fronty, tento cyklus má tedy nejvýše \(|V|\) iterací.

- Celkový počet iterací vnitřního cyklu je nejvýše dvakrát tolik, kolik je v grafu hran (jednou „pohled“ hranou z jedné strany, podruhé z opačné).
- Celková časová složitost je tedy \(\mathcal{O}(|V | + |E|)\).

## Poznámka Anki 1664183392189

Karty Anki: 1664183392189
GUID: hw2(2~U!;X; štítky: bi-ag1::p02.

### Otázka (Front)

Definujte symetrizaci orientovaného grafu.

### Odpověď (Back)

Symetrizace orientovaného grafu \(G=(V,E)\) je neorientovaný graf \(\operatorname{sym}(G) = (V, E')\), kde \(\set{u, v} \in E'\) právě tehdy, když \((u, v) \in E\) nebo \((v, u) \in E\).

## Poznámka Anki 1664183472903

Karty Anki: 1664183472904
GUID: G4*p+-pEMu; štítky: bi-ag1::p02.

### Otázka (Front)

Definujte slabě souvislý graf.

### Odpověď (Back)

Orientovaný graf \(G = (V, E)\) nazveme slabě souvislý, pokud je souvislá jeho symetrizace \(\operatorname{sym}(G)\).

## Poznámka Anki 1664183544185

Karty Anki: 1664183544185
GUID: BK:y<:Z]jl; štítky: bi-ag1::p02.

### Otázka (Front)

Definujte silně souvislý graf.

### Odpověď (Back)

Orientovaný graf \(G = (V, E)\) nazveme silně souvislý, pokud pro každé dva vrcholy \(u, v \in V\) existuje v \(G\) orientovaná cesta z \(u\) do \(v\) a současně orientovaná cesta z \(v\) do \(u\).

## Poznámka Anki 1664183662618

Karty Anki: 1664183662618
GUID: mk+F4EL&W;; štítky: bi-ag1::p02.

### Otázka (Front)

Definujte izomorfismus grafů.

### Odpověď (Back)

Nechť \(G\) a \(H\) jsou dva grafy. Funkce \(f: V(G) \to V(H)\) je izomorfismus grafů \(G\) a \(H\), pokud

- \(f\) je bijekce a
- pro každou dvojici vrcholů \(u, v\) z \(V(G)\) platí \(\set{u, v} \in E(G)\) právě tehdy, když \(\set{f(u), f(v)} \in E(H)\).

## Poznámka Anki 1664183817236

Karty Anki: 1664183817236
GUID: AlRlt@!3PY; štítky: bi-ag1::p02.

### Otázka (Front)

Definujte izomorfní grafy.

### Odpověď (Back)

Dva grafy \(G\) a \(H\) jsou izomorfní, pokud existuje izomofismus grafů \(G\) a \(H\). Tento fakt značíme \(G \underline{\sim} H\).

## Poznámka Anki 1664183929817

Karty Anki: 1664183929817
GUID: F6f2ch3:>4; štítky: bi-ag1::p02.

### Otázka (Front)

Definujte automorfismus grafu.

### Odpověď (Back)

Automorfismus grafu \(G\) je izomorfismus se sebou samým, tedy funkce \(f: V(G) \to V(G)\) taková, že

- \(f\) je bijekce a

- pro každou dvojici vrcholů \(u, v \in V(G)\) platí \(\set{u, v} \in E(G)\) právě tehdy, když \(\set{f(u), f(v)} \in E(G)\).

## Poznámka Anki 1664184011228

Karty Anki: 1664184011228
GUID: NDOit_J3o3; štítky: bi-ag1::p02.

### Otázka (Front)

Kolik je v \(n\)-prvkové množině vrcholů \(V\) různých grafů?

### Odpověď (Back)

\[2^{n \choose 2}\]

## Poznámka Anki 1664184284536

Karty Anki: 1664184284536
GUID: CXyx/;m$n1; štítky: bi-ag1::p02 bi-spol::03 bi-spol::04.

### Otázka (Front)

Definujte strom, les a list.

### Odpověď (Back)

Graf \(G\) nazveme **stromem**, pokud je souvislý a neobsahuje žádnou kružnici (je acyklický).
Graf \(G\) nazveme **lesem**, pokud neobsahuje žádnou kružnici.
Vrchol \(v\) grafu \(G\) nazveme **listem**, pokud \(\deg_G(v) = 1\).

## Poznámka Anki 1664184480569

Karty Anki: 1664184480570
GUID: MXW4GK%Cln; štítky: bi-ag1::p02.

### Otázka (Front)

Vyslovte a dokažte větu o existenci listů.

### Odpověď (Back)

Každý strom \(T\) s aspoň dvěma vrcholy obsahuje aspoň dva listy.

**Důkaz**

- Nechť \(P\) je nejdelší cesta v \(T\).

- Nechť \(u\) a \(v\) jsou její koncové vrcholy.
- Sporem ukážeme, že \(u\) a \(v\) jsou listy.
- Kdyby z \(u\) vedly aspoň dvě hrany, jedna z nich bude patřit do \(u\text{-}v\text{-}\)cesty \(P\) a zbývat bude ještě aspoň jedna hrana \(e = \set{u, w}\).
- Kdyby \(w \in V(P)\), byla by v \(T\) kružnice.
- Kdyby \(w \notin V(P)\), cesta \(P\) by šla prodloužit a nebyla by tedy nejdelší.
- To samé platí pro koncový vrchol \(v\).

## Poznámka Anki 1664185131140

Karty Anki: 1664185131140
GUID: ju}D6Ds;H]; štítky: bi-ag1::p02.

### Otázka (Front)

Vyslovte a dokažte větu o trhání listů.

### Odpověď (Back)

Nechť \(G = (V,E)\) je graf na aspoň \(2\) vrcholech a nechť \(v \in V\) je jeho list. Pak \(G\) je strom, právě když \(G - v\) je strom.

**Důkaz **\(G - v\) **je strom:**

- \(G - v\) je souvislý:

- Zvol dva libovolné vrcholy \(x, y \in V \setminus \set{v}\) a cestu \(P\) mezi nimi v \(G\) (ta existuje, protože \(G\) je souvislý).
- \(P\) nemůže obsahovat jiné vrcholy stupně \(1\) než \(x, y\); tedy speciálně neobsahuje \(v\).

- Dostáváme tedy \(P \subseteq G - v\) a tedy \(G - v\) je souvislý.

- \(G - v\) je bez kružnic:

- \(G - v \) je podgraf \(G\), a tedy neobsahuje kružnici.

- Tedy \(G - v\) je strom.

**Důkaz **\(G\) **je strom:**

- \(G\)** **je bez kružnic:

- Vrácením listu \(v\) do grafu \(G\) (přidáním listu ke stromu \(G - v\)) zjevně nevytvoříme kružnici.

- \(G\) je souvislý:

- Mezi každými dvěma vrcholy \(x, y \in V \setminus \set{v}\) vede cesta v \(G - v\).
- Cesta v \(G\) z libovolného vrcholu \(x\) do \(v\) vznikne prodloužením cesty mezi \(x\) a \(w\) do vrcholu \(v\), kde \(w\) je jediný soused listu \(v\).

- Tedy \(G\) je strom.

## Poznámka Anki 1664185226260

Karty Anki: 1664185226260
GUID: w=/jQ&p,$-; štítky: bi-ag1::p02 bi-spol::03.

### Otázka (Front)

Vyslovte větu o charakterizaci stromů.

### Odpověď (Back)

Nechť \(G = (V,E)\) je graf. Pak následující tvrzení jsou ekvivalentní:

- \(G\) je strom.

- Pro každé dva vrcholy \(u, v \in V\) existuje právě jedna \(u\text{-}v\text{-}\)cesta.
- \(G\) je souvislý a vynecháním libovolné hrany vznikne nesouvislý graf.

- \(G\) je souvislý a \(|E| = |V| - 1\).

## Poznámka Anki 1669403864297

Karty Anki: 1669403864297
GUID: Hqc&?H`B#_; štítky: bi-ag1::p02.

### Otázka (Front)

Kolik automorfismů má \(P_m\)?

### Odpověď (Back)

\(2\)

## Poznámka Anki 1669403931440

Karty Anki: 1669403931440
GUID: dsIB:PIC$n; štítky: bi-ag1::p02.

### Otázka (Front)

Kolik automorfismů má \(C_n\)?

### Odpověď (Back)

\(2n\)

## Poznámka Anki 1669403971255

Karty Anki: 1669403971255
GUID: p$6Rxmk99W; štítky: bi-ag1::p02.

### Otázka (Front)

Kolik automorfismů má \(K_n\).

### Odpověď (Back)

\(n!\)

