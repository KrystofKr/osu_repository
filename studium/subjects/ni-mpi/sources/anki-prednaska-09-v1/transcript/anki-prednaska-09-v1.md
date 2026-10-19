# NI-MPI – Přednáška 09

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1731499301073

Karty Anki: 1731499301073
GUID: O&.D6bG$,S; štítky: ni-mpi::p09 ni-spol::01.

### Otázka (Front)

Definujte grupoid (magma).

### Odpověď (Back)

Grupoid (magma) je uspořádaná dvojice \((M, \circ)\), kde \(M\) je neprázdná množina a \(\circ : M \times M \to M\) binární operace.

### Doplňující pole (Extra)

Z definice vyplývá, že množina \(M\) je uzavřená vůči operaci \(\circ\). Množinu \(M\) nazýváme nosič (carrier).

## Poznámka Anki 1731499423809

Karty Anki: 1731499423809
GUID: hWh^~JX#d]; štítky: ni-mpi::p09 ni-spol::01.

### Otázka (Front)

Definujte pologrupu (semigroup).

### Odpověď (Back)

Pologrupa (semigroup) je grupoid \((M, \circ)\), pro který je \(\circ\) asociativní operace:
\[(\forall a,b,c \in M) \big(a \circ (b \circ c) = (a \circ b) \circ c \big).\]

## Poznámka Anki 1731499507944

Karty Anki: 1731499507944
GUID: oBLEY1|6pH; štítky: ni-mpi::p09 ni-spol::01.

### Otázka (Front)

Definujte monoid.

### Odpověď (Back)

Monoid je pologrupa \((M, \circ)\), ve které existuje neutrální prvek tak, že
\[(\exists e \in M)(\forall a \in M) \big( a \circ e = e \circ a = a \big).\]

## Poznámka Anki 1731499587451

Karty Anki: 1731499587451
GUID: spH{EkmhmG; štítky: duplicate ni-mpi::p09.

### Otázka (Front)

Definujte grupu (group) a abelovskou (komutativní) grupu.

### Odpověď (Back)

Nechť \(M\) je neprázdná množina a \(\circ : M \times M \to M\) binární operace (vlastnosti grupoidu). Pokud

- platí asociativní zákon (vlastnost pologrupy):

\[(\forall a,b,c \in M) \big(a \circ (b \circ c) = (a \circ b) \circ c \big),\]

- existuje neutrální prvek (vlastnost monoidu) tak, že

\[(\exists e \in M)(\forall a \in M) \big( a \circ e = e \circ a = a \big),\]

- existuje inverzní prvek tak, že

\[(\forall a \in M)(\exists a^{-1}\in M) \big(a \circ a^{-1} = a^{-1} \circ a = e\big),\]říkáme, že uspořádaná dvojice \(G = (M, \circ)\) je **grupa**. Pokud navíc pro \(\circ\) platí komutativní zákon:

\[(\forall a,b \in M) \big(a \circ b = b \circ a\big),\]mluvíme o** abelovské **(komutativní)** grupě**.

### Doplňující pole (Extra)

Grupa je tedy monoid \((M, \circ)\), ve kterém existuje ke každému prvku inverzní prvek, a abelovská (komutativní) grupa je grupa, kde \(\circ\) je komutativní operace.

## Poznámka Anki 1731500082629

Karty Anki: 1731500082629
GUID: L1:#.0Yp`|; štítky: ni-mpi::p09.

### Otázka (Front)

Popište dědičnost algebraických vlastností.

### Odpověď (Back)

Dedičnost algebraických vlastností zajišťuje, že pokud lze dokázat nějaké tvrzení pro obecnou strukturu, např. grupu \((M, \circ)\), bude toto tvrzení platit pro všechny konkrétní struktury splňující definici dané obecné struktury, např. \((\mathbb R, +)\).

## Poznámka Anki 1731508397690

Karty Anki: 1731508397691
GUID: hFliss-Z$l; štítky: duplicate ni-mpi::p09 ni-spol::01.

### Otázka (Front)

Vyslovte a dokažte větu o jednoznačnosti neutrálního prvku v monoidu.

### Odpověď (Back)

Mějme monoid \((M, \circ)\). Pak v tomto monoidu existuje právě jeden neutrální prvek.

**Důkaz** 
Důkaz provedeme sporem. Z definice monoidu víme, že existuje neutrální prvek \(e \in M\). Pro spor budeme nyní předpokládat, že existuje další neutrální prvek \(\overline e \in M\) takový, že \(e \neq \overline e\). Potom z definice neutrálního prvku platí
\[\overline e = \overline e \circ e = e,\]čímž dostáváme spor s tím, že \(e\) a \(\overline e\) jsou různé.

## Poznámka Anki 1731959395044

Karty Anki: 1731959395044
GUID: gYUgb^)d[5; štítky: duplicate ni-mpi::p09 ni-spol::01.

### Otázka (Front)

Vyslovte a dokažte větu o jednoznačnosti inverzního prvku v grupě.

### Odpověď (Back)

Mějme grupu \((M, \circ)\). Pak pro každé \(a \in M\) existuje právě jeden inverzní prvek.

**Důkaz** 
Důkaz provedeme sporem. Z definice grupy víme, že pro každý prvek \(a \in M\) existuje alespoň jeden inverzní prvek \(a^{-1} \in M\). Pro spor budeme nyní předpokládat, že existuje další inverzní prvek \(\overline{a^{-1}} \in M\) takový, že \(a \neq \overline{a^{-1}}\). Potom platí
\[\overline{a^{-1}} = \overline{a^{-1}} \circ e = \overline{a^{-1}} \circ (a \circ a^{-1}) = (\overline{a^{-1}} \circ a) \circ a^{-1} = e \circ a^{-1} = a^{-1},\]čímž dostáváme spor s tím, že \(a^{-1}\) a \(\overline{a^{-1}}\) jsou různé.

## Poznámka Anki 1731960978307

Karty Anki: 1731960978308
GUID: o~*Wit7K~^; štítky: ni-mpi::p09 ni-spol::01.

### Otázka (Front)

Vyslovte a dokažte větu o vztahu Cayleyho tabulky grupy a latinského čtverce.

### Odpověď (Back)

Cayleyho tabulka každé grupy tvoří latinský čtverec, což je pro \(n\) prvkovou množinu \(M\) matice \(n \times n\) taková, že v každém řádku i sloupci jsou vždy všechny prvky množiny \(M\).

**Důkaz** 
Důkaz provedeme sporem. Předpokládejme, že tabulka nějaké grupy \((M, \circ)\) není latinský čtverec. To znamená, že v nějakém řádku nebo sloupci Cayleyho tabulky se jeden prvek, označme ho \(b\), opakuje dvakrát. Předpokládejme, že se tak děje v řádku \(n\) a sloupcích \(m_1\) a \(m_2\). Z toho vyplývá, že rovnice
\[n \circ x = b\]má dvě různá řešení, \(m_1\) a \(m_2\), což je spor s větou o jednoznačnosti dělení v grupě.

## Poznámka Anki 1731961226181

Karty Anki: 1731961226181
GUID: zoo0#eUVF:; štítky: ni-mpi::p09 ni-spol::01.

### Otázka (Front)

Vyslovte a dokažte větu o jednoznačnosti dělení v grupě.

### Odpověď (Back)

Mějme grupu \((M, \circ)\). Pak v této grupě lze jednoznačně dělit, tzn. pro libovolné \(a, b \in M\) mají rovnice
\[a \circ x = b \quad \text{resp.} \quad y \circ a = b\]právě jedno řešení.

**Důkaz** 
Důkaz provedeme sporem. Z věty o jednoznačnosti inverzního prvku v grupě víme, že pro každý prvek \(a \in M\) existuje právě jeden inverzní prvek a řešení daných rovnic tedy je
\[a^{-1} \circ b \quad \text{resp.} \quad b \circ a^{-1}.\]Pro spor budeme nyní předpokládat, že existuje další řešení \(x_1\) takové, že \(x_1 \neq a^{-1} \circ b\). Potom platí
\[x_1 = e \circ x_1 = (a^{-1} \circ a) \circ x_1 = a^{-1} \circ (a \circ x_1) = a^{-1} \circ b,\]čímž dostáváme spor s tím, že \(x_1\) a \(a^{-1} \circ b\) jsou různé.

