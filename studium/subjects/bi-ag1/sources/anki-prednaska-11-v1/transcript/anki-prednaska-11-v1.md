# BI-AG1 – Přednáška 11

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 18 poznámek, 18 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1669624001026

Karty Anki: 1669624001027
GUID: KW7nj-0&.:; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Definujte hranově ohodnocený graf a váhu podgrafu.

### Odpověď (Back)

Mějme souvislý neorientovaný graf \(G = (V, E)\). Každé hraně \(e \in E\) přiřadíme číselnou váhu \(w(e)\), kde \(w : E \to \mathbb R\). Takový graf se nazývá **hranově ohodnocený**.
Váhovou funkci můžeme přirozeně rozšířit na podgrafy: **Váha** \(w(H)\) **podgrafu** \(H \subseteq G\) je součet vah jeho hran.

## Poznámka Anki 1669624027049

Karty Anki: 1669624027049
GUID: zx<>&tV=|f; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Definujte minimální kostru.

### Odpověď (Back)

Kostra hranově ohodnoceného grafu \(G\) je minimální, pokud má mezi všemi jeho kostrami nejmenší váhu.

## Poznámka Anki 1669624505506

Karty Anki: 1669624505506
GUID: g:0|^KiEI*; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Vyslovte lemma o konečnosti Jarníkova algoritmu. Po kolika iteracích se zastaví?

### Odpověď (Back)

Jarníkův algoritmus se po \(|V| - 1\) iteracích zastaví a vydá nějakou kostru zadaného grafu \(G = (V, E)\).

**Důkaz**

- Graf \(T\) konstruovaný algoritmem vzniká z jednoho vrcholu postupným přidáváním listů.
- Takže \(T\) je v každém okamžiku výpočtu strom.
- V každé iteraci se \(|V(T)|\) zvětší o \(1\).
- Dokud \(V(T) \neq V(G)\), musí díky souvislosti \(G\) existovat hrana mezi \(V(T)\) a \(V(G) \setminus V(T)\), kterou může algoritmus přidat do \(T\).
- To znamená, že algoritmus se zastaví, až když \(V(T) = V(G)\).
- Tehdy je ale \(T\) kostra.

## Poznámka Anki 1669624625215

Karty Anki: 1669624625215
GUID: xF,x,8pFz8; štítky: bi-ag1::p11.

### Otázka (Front)

Definujte řez grafu.

### Odpověď (Back)

Nechť \(A\) je nějaká podmnožina vrcholů grafu \(G = (V, E)\) a \(B\) její doplněk, tj. \(B = V \setminus A\).
Množině všech hran, které leží jedním vrcholem v \(A\) a druhým v \(B\), budeme říkat řez grafu \(G\) určený množinami \(A\) a \(B\).

## Poznámka Anki 1669625224972

Karty Anki: 1669625224972
GUID: J2igT,3`uk; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o minimální kostře grafu s unikátními vahami hran (o správnosti Jarníkova algoritmu).

### Odpověď (Back)

Souvislý graf s unikátními vahami má právě jednu minimální kostru a Jarníkův algoritmus tuto kostru vytvoří.

**Důkaz**

- Jarníkův algoritmus v každém kroku vybere jedinečnou nejlehčí hranu řezu mezi vrcholy dosud vytvořeného stromu a zbytkem grafu, která je vždy dle lemmatu o řezech v grafu s unikátními vahami obsažena v každé minimální kostře.
- To ale znamená, že kostra vytvořená Jarníkovým algoritmem je podgrafem každé minimální kostry.
- Protože ale všechny kostry daného grafu mají stejný počet hran, znamená to, že vytvořená kostra je všem minimálním kostrám rovna a je tudíž unikátní.

## Poznámka Anki 1669625892622

Karty Anki: 1669625892622
GUID: cq`>_#)//p; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte lemma o řezech v grafu s opakujícími se vahami hran.

### Odpověď (Back)

Nechť \(G\) je souvislý ohodnocený graf, \(R\) je řez v \(G\) a \(e\) je libovolná nejlehčí hrana v \(R\). Pro každou minimální kostru \(\hat T\) existuje minimální kostra \(T\) taková, že

- \(\hat T\) a \(T\) se liší pouze na hranách obsažených v \(R\) a
- \(T\) obsahuje \(e\).

**Důkaz**

- Označme \(A\) a \(B\) množiny vrcholů, kterými je určen řez \(R\).
- Nechť \(\hat T\) neobsahuje \(e\) a nechť \(e = \set{a, b}\).
- Buď \(P\) unikátní cesta mezi vrcholy \(a\) a \(b\) v \(\hat T\) .
- Cesta \(P\) prochází řezem \(R\).
- Nechť \(f\) je libovolná hrana v \(E(P) \cap E(R)\).
- Potom \(T := \hat T - f + e\) je kostra a platí, že \(w(T) \leq w(\hat T)\).

## Poznámka Anki 1669626157744

Karty Anki: 1669626157745
GUID: A;Gn.xFhT*; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o časové složitosti Jarníkova algoritmu s binární haldou.

### Odpověď (Back)

Časová složitost \(\mathtt{MinKostraJarník}\) při použití binární haldy je \(\mathcal O(|E| \log |V|)\).

**Důkaz**

- Inicializace zabere \(O(|V|)\).
- Operace s binární haldou:

- Provedeme \(|V | − 1\) krát operaci \(\mathtt{HeapExtractMin}\) – celkem \(\mathcal O(|V | \log |V |)\).
- Každá hrana může způsobit volání operace \(\mathtt{HeapDecreaseKey}\) – celkem \(\mathcal O(|E| \log |V |)\).

- Dohromady dostáváme \(\mathcal O(|V|) + \mathcal  O(|V| \log |V|) +  \mathcal  O(|E| \log |V|) = \mathcal  O(|E| \log |V|)\).

## Poznámka Anki 1669626711640

Karty Anki: 1669626711640
GUID: o6FcSmk~6r; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Dokažte lemma o správnosti Kruskalova algoritmu.

### Odpověď (Back)

Kruskalův algoritmus se zastaví a vydá minimální kostru.

**Důkaz**

- **Konečnost**: Cyklus se vykoná \(m\)-krát.
- **Správnost**: Ukážeme nejdříve, že pokud algoritmus přidá hranu \(e = \set{u, v}\) do \(T\), pak \(e\) leží v minimální kostře.
- Pokud algoritmus \(e\) přidá, stane se tak v okamžiku, kdy se vrcholy \(u\) a \(v\) nacházejí v nějakých dvou rozdílných stromech \(T_u\) a \(T_v\) lesa \(T\).
- Hrana \(e\) přitom leží v řezu oddělujícím strom \(T_u\) od zbytku grafu.
- Hrana \(e\) musí být nejlehčí hrana řezu oddělujícího strom \(T_u\) od zbytku grafu, neboť případnou lehčí hranu by algoritmus potkal dříve a přidal by ji do \(T\).

- Hrana \(e\) tedy leží v minimální kostře podle lemmatu o řezech.
- Nyní si ukážeme, že výsledný \(T\) je souvislý.

- Pokud by nebyl, uvažme dva rozdílné stromy \(T_u\) a \(T_v\) lesa \(T\) a řez oddělující strom \(T_u\) od zbytku grafu.

- Protože je graf \(G\) souvislý, je tento řez neprázdný a má nějakou hranu \(e\).

- Když algoritmus zkoumal hranu \(e\), nemohla tvořit cyklus (netvoří ho ani ve výsledném \(T\)), takže by ji algoritmus musel přidat, což je spor.

- Výstupem algoritmu je tedy kostra, která je podgrafem minimální kostry – tedy minimální kostra.

## Poznámka Anki 1669627516563

Karty Anki: 1669627516563
GUID: gvum~}[mz^; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Definujte strukturu Union-Find.

### Odpověď (Back)

Struktura Union-Find reprezentuje komponenty souvislosti grafu a umí na nich provádět následující operace:

- \(\mathtt{Find}(u)\) vrátí identifikátor komponenty, ve které leží vrchol \(u\).
- Pokud pro testovanou hranu \(\set{u, v}\) platí, že \(u\) a \(v\) patří do různých komponent, pak \(\mathtt{Union}(u, v)\) tyto komponenty spojí do jedné.

## Poznámka Anki 1669628388380

Karty Anki: 1669628388380
GUID: r9Mo9xJ|)!; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte lemma o hloubce keříků.

### Odpověď (Back)

Algoritmus \(\mathtt{Union}\) zachovává invariant, že keřík s \(h + 1\) hladinami obsahuje nejméně \(2^h\) vrcholů.

**Důkaz**

- Indukcí podle počtu operací \(\mathtt{Union}\).
- Na počátku algoritmu mají všechny keříky jednu hladinu a \(2^0 = 1\) vrchol.
- Nechť nyní provádíme \(\mathtt{Union}(u,v)\) a počet hladin obou keříků je různý.
- Připojením mělčího keříku pod kořen toho hlubšího se počet hladin nezmění a počet vrcholů neklesne, takže nerovnost stále platí.
- Pokud mají oba keříky \(h\) hladin, platí z indukčního předpokladu, že každý z nich obsahuje minimálně \(2^{h-  1}\) vrcholů.

- Jejich sloučením tudíž vznikne keřík s \(h + 1\) hladinami o alespoň \(2 \cdot 2^{h - 1} = 2^h\)  vrcholech.

## Poznámka Anki 1669628504010

Karty Anki: 1669628504010
GUID: e`7x>|f.oR; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Jaké jsou složitosti operací na struktuře Union-Find? Proč?

### Odpověď (Back)

Z lemmatu o hloubce keříků plyne:

- složitost \(\mathtt{Find}(u)\) je \(\mathcal{O}(\log n)\),
- složitost \(\mathtt{Union}(u,v)\) je \(\mathcal{O}(1)\).

## Poznámka Anki 1669628740111

Karty Anki: 1669628740111
GUID: 6U5sxgYrY; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o časové složitosti Kurskalova algoritmu.

### Odpověď (Back)

Kruskalův algoritmus vytvoří minimální kostru v čase \(\mathcal O(m \log n + m \cdot T_f(n) + n \cdot T_u(n))\), kde \(T_f(n)\) a \(T_u(n)\) jsou časové složitosti operací \(\mathtt{Find}\) a \(\mathtt{Union}\) na grafech s \(n\) vrcholy. Pokud použijeme strukturu Union-Find s keříky dostaneme složitost \(\mathcal O(m \log n)\).

**Důkaz
**Při testování hran se nejvýše \(m\)-krát zavolá \(\mathtt{Find}\) a \((n - 1)\)-krát se zavolá \(\mathtt{Union}\).

## Poznámka Anki 1716310454124

Karty Anki: 1716310454125
GUID: 7n(AigF,L; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Popište Kruskalův algoritmus (\(\mathtt{MinKostraKruskal}\)).

### Odpověď (Back)

**Vstup**

- hranově ohodnocený graf \(G = (V, E)\)

**Výstup** 

- minimální kostra \(T\) grafu \(G\)

**Postup**

- Uspořádáme hrany vzestupně dle jejich váhy \(w(e_1) \leq \dots \leq w(e_m)\).
- Zinicializujeme \(T := (V, \emptyset)\).
- Pro \(i := 1, \dots, m\) iterujeme:

- označíme \(u\), \(v\) krajní vrcholy hrany \(e_i\);
- pokud \(u\) a \(v\) leží v různých komponentách lesa \(T\), přidáme hranu \(e_i\) do \(T\), tj.

\[E(T) := E(T) \cup \{ e_i \}.\]

- Vrátíme \(T\).

**Složitost**

- Časová složitost je \(\mathcal O \big( m \log n + m \cdot T_f(n) + n \cdot T_u(n) \big)\), kde \(T_f(n)\) resp. \(T_u(n)\) jsou časové složitosti operací \(\texttt{Find}\) resp. \(\texttt{Union}\) na struktuře Union-Find s \(n\) prvky. Při implementaci Union-Find pomocí keříků má algoritmus časovou složitost \(\mathcal O(m \log n)\).

## Poznámka Anki 1716313030933

Karty Anki: 1716313030933
GUID: u[gY9=M-MY; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Popište Dijkstrův algoritmus (\(\texttt{Dijkstra}\)).

### Odpověď (Back)

**Vstup**

- hranově ohodnocený graf \(G = (V, E)\) s kladnými ohodnoceními hran
- počáteční vrchol \(v_0 \in V\)

**Výstup**

- pole vzdáleností \(h\)

- pole předchůdců \(P\)

**Postup**

- Všechny vrcholy \(v \in V\) zinicializujeme s
\[\begin{matrix}
\texttt{stav}[v] := \text{nenalezený},\\
h(v) := +\infty,\\
P(v) := \bot.
\end{matrix}\]

- Počáteční vrchol \(v_0\) nastavíme na

\[\begin{matrix}
\texttt{stav}[v_0] := \text{otevřený},\\
h(v_0) := 0.
\end{matrix}\]

- Dokud existují nějaké otevřené vrcholy, iterujeme:

- vybereme otevřený vrchol \(v\), jehož \(h(v)\) je nejmenší;
- pro všechny následníky \(w\) vrcholu \(v \) splňující \(h(w) > h(v) + \ell \big( (v, w) \big)\) nastavíme

\[\begin{matrix}
\texttt{stav}[w] := \text{otevřený},\\
h(w) := h(v) + \ell \big( (v, w) \big),\\
P(w) := v;
\end{matrix}\]

- uzavřeme vrchol \(v\).

- Vrátíme \((h, P)\).

**Složitost**

- Časová složitost je \(\mathcal O(n^2)\), ale s použitím minimové binární haldy lze dosáhnout složitosti \(\mathcal O(m \log n)\).

## Poznámka Anki 1716313138596

Karty Anki: 1716313138596
GUID: q])_N;m.x-; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Popište zobecněný Dijkstrův algoritmus (\(\mathtt{Relaxace}\)).

### Odpověď (Back)

**Vstup**

- hranově ohodnocený graf \(G = (V, E)\)
- počáteční vrchol \(v_0 \in V\)

**Výstup**

- pole vzdáleností \(h\)

- pole předchůdců \(P\)

**Postup**

- Všechny vrcholy \(v \in V\) zinicializujeme s

\[\begin{matrix}
\texttt{stav}[v] := \text{nenalezený},\\
h(v) := +\infty,\\
P(v) := \bot.
\end{matrix}\]

- Počáteční vrchol \(v_0\) nastavíme na

\[\begin{matrix}
\texttt{stav}[v_0] := \text{otevřený},\\
h(v_0) := 0.
\end{matrix}\]

- Dokud existují nějaké otevřené vrcholy, iterujeme:

- vybereme libovolný otevřený vrchol \(v\);
- pro všechny následníky \(w\) vrcholu \(v \) splňující \(h(w) > h(v) + \ell \big( (v, w) \big)\) nastavíme

\[\begin{matrix}
\texttt{stav}[w] := \text{otevřený},\\
h(w) := h(v) + \ell \big( (v, w) \big),\\
P(w) := v;
\end{matrix}\]

- uzavřeme vrchol \(v\).

- Vrátíme \((h, P)\).

## Poznámka Anki 1716313445318

Karty Anki: 1716313445318
GUID: mOeC*bzw`9; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Popište vlastnosti zobecněného Dijkstrova algoritmu (\(\texttt{Relaxace}\)).

### Odpověď (Back)

Zobecněný Dijkstrův algoritmus (\(\mathtt{Relaxace}\)) má podobné vlastnosti jako Dijkstrův algoritmus (\(\mathtt{Dijkstra}\)):

1. Ohodnocení \(h(v)\) v průběhu D.A. nikdy neroste a je-li konečné, rovná se délce **nějakého** \(v_0v\)**-sledu** zachyceného inverzí posloupnosti \(v\), \(P(v)\), \(P(P(v)), \dots, v_0\).
2. D.A. postupně otevírá všechny vrcholy dosažitelné z \(v_0\) (v případě \(\texttt{Relaxace}\) může být **uzavřený vrchol znovu otevřen**).
3. D.A. uzavírá všechny dosažitelné vrcholy v pořadí jejich neklesající vzdálenosti od \(v_0\) a **pokud se zastaví** je \(h(v) = d(v_0, v)\).

## Poznámka Anki 1716313809562

Karty Anki: 1716313809562
GUID: z1p,lWQ.S?; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Popište Bellman-Fordův algoritmus (\(\texttt{Bellman-Ford}\)).

### Odpověď (Back)

**Vstup**

- hranově ohodnocený graf \(G = (V, E)\) bez záporných cyklů
- počáteční vrchol \(v_0 \in V\)

**Výstup**

- pole vzdáleností \(h\)

- pole předchůdců \(P\)

**Postup**

- Všechny vrcholy \(v \in V\) zinicializujeme s

\[\begin{matrix}
\texttt{stav}[v] := \text{nenalezený},\\
h(v) := +\infty,\\
P(v) := \bot.
\end{matrix}\]

- Zinicializujeme frontu \(Q\) obsahující počáteční vrchol \(v_0\) a pro vrchol \(v_0\) nastavíme

\[\begin{matrix}
\texttt{stav}[v_0] := \text{otevřený},\\
h(v_0) := 0.
\end{matrix}\]

- Dokud je fronta \(Q\) neprázdná, iterujeme:

- vybereme první vrchol z \(Q\) a označíme jej \(v\);
- pro všechny následníky \(w\) vrcholu \(v \) splňující \(h(w) > h(v) + \ell \big( (v, w) \big)\) nastavíme

\[\begin{matrix}
\texttt{stav}[w] := \text{otevřený},\\
h(w) := h(v) + \ell \big( (v, w) \big),\\
P(w) := v;
\end{matrix}\]

- pokud navíc některý z následníků nebyl před naším zásahem otevřený, vložíme jej na konec \(Q\);
- uzavřeme vrchol \(v\).

- Vrátíme \((h, P)\).

**Složitost**

- Časová složitost je \(\mathcal O(n \cdot m)\).

## Poznámka Anki 1716314462756

Karty Anki: 1716314462756
GUID: IxU;.:UJjL; štítky: bi-ag1::p11 bi-spol::03.

### Otázka (Front)

Popište Jarníkův algoritmus (\(\mathtt{MinKostraJarník}\)).

### Odpověď (Back)

**Vstup**

- hranově ohodnocený graf \(G = (V, E)\)

**Výstup**

- minimální kostra \(T\) grafu \(G\)

**Postup** 

- Zvolíme libovolný vrchol \(v_0 \in V\) jako počáteční vrchol.
- Zinicializujeme \(T = (\{ v_0 \}, \emptyset)\).
- Dokud bude existovat hrana \(\{ u, v \} \in E\) taková, že \(u \in V(T)\) a \(v \notin V(T)\), přidáme nejlehčí takovou hranu spolu s \(v\) do \(T\).
- Vrátíme \(T\).

**Složitost** 

- Časová složitost je \(\mathcal O(n \cdot m)\), ale s použitím minimové binární haldy lze dosáhnout složitosti \(\mathcal O(m \log n)\).

