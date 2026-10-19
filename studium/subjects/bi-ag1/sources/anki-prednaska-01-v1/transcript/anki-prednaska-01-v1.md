# BI-AG1 – Přednáška 01

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 22 poznámek, 22 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1663579316367

Karty Anki: 1663579316367
GUID: dC+EcdO[ll; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Definujte neorientovaný graf a hranu.

### Odpověď (Back)

**Neorientovaný graf** je uspořádaná dvojice \((V, E)\), kde

- \(V\) je neprázdná konečná množina vrcholů,
- \(E\) je množina hran.
**Hrana** je dvouprvková podmnožina \(V\) (neuspořádaná dvojice vrcholů) a značíme ji \(\{u, v\}\). Množinu všech dvouprvkových podmnožin množiny \(V\) (všech možných hran) značíme \(V \choose 2\).

### Doplňující pole (Extra)

Počet vrcholů neorientovaného grafu \(| V(G) |\) značíme \(n\) a počet jeho hran \(| E(G) |\) značíme \(m\).

## Poznámka Anki 1663579454327

Karty Anki: 1663579454327
GUID: i&Or%>b4=(; štítky: bi-ag1::p01.

### Otázka (Front)

Nechť \(G\) je graf. Jak označujeme množinu vrcholů, množinu hran, počet vrcholů a počet hran?

### Odpověď (Back)

- množina vrcholů grafu \(G\): \(V(G)\)
- množina hran grafu \(G\): \(E(G)\)
- počet vrcholů grafu \(G\): \(n = |V(G)|\)
- počet hran grafu \(G\): \(m = |E(G)|\)

## Poznámka Anki 1663579629080

Karty Anki: 1663579629081
GUID: ea<J:yDeL.; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Definujte koncový vrchol, sousední vrchol a incidentní vrcholy.

### Odpověď (Back)

Nechť \(e = \set{u, v}\) je hrana v grafu \(G\). Pak řekneme, že:

- vrcholy \(u\) a \(v\) jsou **koncové vrcholy** hrany \(e\),
- \(u\) je **sousedem** \(v\) v \(G\) (a naopak),

- \(u\) i \(v\) jsou **incidentní** s hranou \(e\).

## Poznámka Anki 1663579978008

Karty Anki: 1663579978009
GUID: h5UbW,Fq#?; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Definujte sled, cestu a délku cesty v grafu.

### Odpověď (Back)

- **Sled délky **\(k\) **v grafu **\(G\) je sekvence \(v_0, e_1, v_1, e_2, \dots, e_k v_k\) taková, že \(e_i = \set{v_{i - 1}, v_i}\) a \(e_i \in E(G)\) pro všechna \(i = 1, \dots, k\).

- **Cesta v grafu **\(G\) je sled, ve kterém se neopakují vrcholy (a tedy ani hrany).

- Má-li cesta \(P\) v grafu \(G\) koncové vrcholy \(s = v_0\) a \(t = v_k\), mluvíme o cestě z \(s\) do \(t\), nebo o \(s \text{-} t \text{-}\)cestě (připouštíme i cestu nulové délky).
- **Délka **\(s \text{-} t \text{-}\)cesty \(d(s, t)\) je počet hran v této cestě v grafu \(G\).

## Poznámka Anki 1663580707580

Karty Anki: 1663580707581
GUID: mHa:@}WxH.; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Popište algoritmus breadth-first search (\(\texttt{BFS}\)).

### Odpověď (Back)

[Obrázek: paste-5f5c1be7fdb300b30db2072d2bf8ec852ad4ba03.jpg; soubor je v media/ v doprovodném ZIP]  [Obrázek: paste-c0df01e4dd201dbbaf77c4fda8c6dec6fedf55c9.jpg; soubor je v media/ v doprovodném ZIP]  [Obrázek: paste-2c30104b272112d5f9e3df3dfb0085399210d0d2.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1663580769177

Karty Anki: 1663580769177
GUID: pgT]SAb:,w; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o konečnosti algoritmu \(\text{BFS}\).

### Odpověď (Back)

Algoritmus \(\text{BFS(G, s)}\) se vždy zastaví.

**Důkaz**

- Každý vrchol je přidán do fronty \(Q\) nejvýše jednou, neboť je předtím otevřen a nemůže už tedy vícekrát splnit podmínku, že je nenalezený.

- V každé iteraci vnějšího cyklu je jeden vrchol odebrán z fronty.
- Algoritmus se zastaví nejvýše po \(|V(G)|\) iteracích vnějšího cyklu.

## Poznámka Anki 1663581249100

Karty Anki: 1663581249100
GUID: vhgpt2*3^o; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Vyslovte větu o správnosti algoritmu \(\text{BFS}\).

### Odpověď (Back)

[Obrázek: paste-5a491c043b92836adbbbde74d78b2d5d4c6ecae7.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1663603626622

Karty Anki: 1663603626622
GUID: e)wek>p1y9; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Definujte \(\text{BFS}\) fáze a hladiny.

### Odpověď (Back)

[Obrázek: paste-db2b001367be8c69343204057e643fdc5989ea84.jpg; soubor je v media/ v doprovodném ZIP]  [Obrázek: paste-a4540bf7eb366d282af8a1afcdac8cbc729dd103.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1663603798343

Karty Anki: 1663603798343
GUID: K2vIYX29+~; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte první vlastnost algoritmu \(\text{BFS}\).

### Odpověď (Back)

Po skončení \(\text{BFS}(G, s)\) jsou uzavřeny právě ty vrcholy, do kterých vede cesta ze startu \(s\) a ostatní vrcholy zůstanou nenalezené.

**Důkaz**

- Prvním otevřeným a následně uzavřeným vrcholem je start \(s\).
- \(\text{BFS}\) otvírá **všechny **nové sousedy dříve otevřených vrcholů.
- (\(\supseteq\)) Vrchol tedy bude otevřen (a později i uzavřen) pouze tehdy, když do něho ze startu \(s\) vede posloupnost sousedních hran.
- \((\subseteq\)) Naopak, existuje-li do vrcholu nějaká posloupnost sousedních hran z \(s\), bude v průběhu algoritmu někdy otevřen.

## Poznámka Anki 1663604211968

Karty Anki: 1663604211968
GUID: hE}CQe(p]a; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte druhou vlastnost algoritmu \(\text{BFS}\).

### Odpověď (Back)

Pro všechny uzavřené vrcholy \(v\) platí \( D(v) = d(s, v) =\) vzdálenost nejkratší cesty ze startu \(s\) do vrcholu \(v\).

**Důkaz**

- Triviálně platí ve fázi \(F_0\). Uvažujme fázi \(F_i\), \(i > 0\).
- Pokud \(v \in H_i\), pak \(D[v] = i\) a tedy z \(s\) do \(v\) musí existovat cesta o \(i\) hranách. Proto je vzdálenost \(d(s, v) \leq i\).
- Ukážme, že nemůže existovat \(s\text{-}v\text{-cesta}\) kratší než \(i\). Pro spor, nechť existuje cesta \(P\) z \(s\) do \(v\) délky \(j\), kde \(j < i\).
- Protože \(j < i\), musí dle holubníkového principu na \(P\) existovat dva sousední vrcholy \(w\) a \(w'\) a dvě nesousední hladiny \(H_k\) a \(H_l\) (tedy \(|k - l| > 1\)) tak, že \(w \in H_k\) a \(w' \in H_l\).
- To však není možné, neboť dva sousední vrcholy na \(P\) musí nutně ležet ve dvou sousedních hladinách. Máme spor.
- Proto \(d(s, v) = i = D(v)\).

## Poznámka Anki 1663604324521

Karty Anki: 1663604324522
GUID: fK(N=>OgWo; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Definujte úplný graf \(K_n\) ("klika").

### Odpověď (Back)

Nechť \(n \geq 1\).
**Úplný graf na **\(n\) vrcholech \(K_n\) je graf \((V, {V \choose 2})\), kde \(|V| = n\).
 [Obrázek: paste-189e8c1c316b1134eced834f44c777888547a8a9.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1663604504954

Karty Anki: 1663604504954
GUID: uH</JLg>NB; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Definujte úplný bipartitní graf \(K_{n_1, n_2}\).

### Odpověď (Back)

[Obrázek: paste-70228fc9675338d51fe2340c14cb16248fc165f0.jpg; soubor je v media/ v doprovodném ZIP] 
 [Obrázek: paste-d8360c6f85399c1ac5a4da9ca1dee5078acd872b.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1663609644858

Karty Anki: 1663609644858
GUID: IvB=6Ds.21; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Definujte cestu \(P_m\).

### Odpověď (Back)

[Obrázek: paste-fb34fd8144795d7d17a6b0ece0903e3e4447a59b.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1663609787885

Karty Anki: 1663609787885
GUID: z?57CEhbfb; štítky: bi-ag1::p01.

### Otázka (Front)

Definujte kružnici \(C_n\).

### Odpověď (Back)

[Obrázek: paste-e92a3a947031ea8ec1bd5cf6108c11d58515c6a5.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1663609884903

Karty Anki: 1663609884903
GUID: CTpj|u-Gce; štítky: bi-ag1::p01.

### Otázka (Front)

Definujte doplněk grafu.

### Odpověď (Back)

Doplněk \(\overline{G}\) grafu \(G = (V, E)\) je graf \((V, {V \choose 2} \setminus E)\).

## Poznámka Anki 1663610121755

Karty Anki: 1663610121756
GUID: K)a`3v+,`1; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Definujte okolí a stupeň vrcholu.

### Odpověď (Back)

Nechť \(G = (V, E)\) je graf a \(v \in V\) jeho vrchol.

- Symbolem \(\deg_G(v)\) označme počet hran grafu \(G\) obsahujících vrchol \(v\). Toto číslo nazveme **stupněm vrcholu**.
- Symbolem \(N_G(v)\) označme množinu všech sousedů vrcholu \(v\) v grafu \(G\). Tuto množinu nazveme **(otevřené) okolí **vrcholu \(v\) v grafu \(G\).
- Množinu \(N_G[v] = N_G(v) \cup \set{v}\) nazveme **uzavřené okolí** vrcholu \(v\) v grafu \(G\).

Platí tedy \(\deg_G(v) = |N_G(v)|\).

## Poznámka Anki 1663610208871

Karty Anki: 1663610208871
GUID: cyl-D$gYW^; štítky: bi-ag1::p01.

### Otázka (Front)

Definujte regulární graf.

### Odpověď (Back)

- Graf je \(r\text{-}\)regulární, pokud stupeň každého jeho vrcholu je \(r\).
- Graf je regulární, pokud je \(r\text{-}\)regulární pro nějaké \(r\).

Každý vrchol má stejně hran.

## Poznámka Anki 1663623635720

Karty Anki: 1663623635720
GUID: jmBT=2.7Vp; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o principu sudosti.

### Odpověď (Back)

Pro každý graf \(G = (V, E)\) platí
\[\displaystyle \sum_{v \in V} \deg_G(v) = 2|E|.\]
**Důkaz
**Posčítame-li stupně všech vrcholů, započítáme každou hranu přesně dvakrát, což dává součet \(2|E|\).
\[\displaystyle \sum_{v \in V} \deg_G(v) = \displaystyle \sum_{v \in V} |N_G(v)| = \displaystyle \sum_{v \in V} |\set{u \in V \mid \set{u, v} \in E}| = \displaystyle \sum_{v \in V} | \set{e \in E \mid v \in e}| = \displaystyle \sum_{v \in V} \displaystyle \sum_{e \in E \mid v \in e} 1 = \displaystyle \sum_{e \in E} \displaystyle \sum_{v \in e} 1 = \displaystyle \sum_{e \in E} 2 = 2|E|\] [Obrázek: paste-1dfbfbd8f7505fd1a04d3b38a7c9b57a55705360.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1663628065375

Karty Anki: 1663628065375
GUID: CrjBV[9`IX; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Definujte podgraf, indukovaný podgraf a podgraf indukovaný množinou vrcholů.

### Odpověď (Back)

- Graf \(H\) je **podgrafem** grafu \(G\), když \(V(H) \subseteq V(G)\) a \(E(H) \subseteq E(G)\).
- Graf \(H\) je **indukovaným podgrafem **grafu \(G\), když \(V(H) \subseteq V(G)\) a \(E(H) = E(G) \cap {V(H) \choose 2}\).
- Je-li \(G = (V, E)\) a \(V' \subseteq V\), pak \(G[V']\) označuje graf s množinou vrcholů \(V'\) a množinou hran \(E(G) \cap {V' \choose 2}\). Říkáme, že \(G[V']\) je **podgraf indukovaný množinou vrcholů **\(V'\).

  [Obrázek: paste-7c854c05070524120d9982d3983442f30e1a6a98.jpg; soubor je v media/ v doprovodném ZIP] 

 [Obrázek: paste-4697edee2f43cb2cc96c98a94a81f3fe9c5570b2.jpg; soubor je v media/ v doprovodném ZIP] 

 [Obrázek: paste-f24f281a638ceed8fd0f84ab7a5ab8814c68a3b7.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1663628099559

Karty Anki: 1663628099559
GUID: c>|^5/)=,L; štítky: bi-ag1::p01.

### Otázka (Front)

Definujte kliku.

### Odpověď (Back)

Klika v grafu \(G\) je podmnožina vrcholů, z nichž každé dva jsou sousední (čili spojeny hranou).

## Poznámka Anki 1664176130600

Karty Anki: 1664176130600
GUID: esq~jA=i.,; štítky: bi-ag1::p01.

### Otázka (Front)

Definujte izolovaný vrchol.

### Odpověď (Back)

Vrchol stupně \(0\) nazveme izolovaný.

## Poznámka Anki 1664176740580

Karty Anki: 1664176740580
GUID: Mrk!DU$dpL; štítky: bi-ag1::p01 bi-spol::03.

### Otázka (Front)

Definujte orientovaný graf, předchůdce, následníka a smyčku.

### Odpověď (Back)

Orientovaný graf \(G\) je uspořádaná dvojice \((V, E)\), kde

- \(V\) je neprázdná konečná množina vrcholů,

- \(E\) je množina orientovaných hran (zobrazujeme jako šipky).

Orientovaná hrana \((u, v) \in E\) je uspořádaná dvojice vrcholů \(u, v \in V\).

Říkáme, že \(u\) je **předchůdce** \(v\) a \(v\) je **následník** \(u\). Orientovaná hrana \((u, u)\) je **smyčka**.

