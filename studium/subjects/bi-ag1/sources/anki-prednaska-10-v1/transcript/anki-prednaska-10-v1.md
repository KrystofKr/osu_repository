# BI-AG1 – Přednáška 10

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1669020455724

Karty Anki: 1669020455724
GUID: M5}Z]CnbcB; štítky: bi-ag1::p10.

### Otázka (Front)

Popište problém hledání nejdelší rostoucí posloupnosti.

### Odpověď (Back)

- Vstupem je posloupnost \(n\) celých čísel \(x_1, \dots, x_n\).
- Úkolem je vyškrtnout z ní co nejméně prvků tak, aby zbývající prvky tvořily rostoucí posloupnost.

## Poznámka Anki 1669020945547

Karty Anki: 1669020945547
GUID: Di<(pXx?<R; štítky: bi-ag1::p10 bi-spol::21.

### Otázka (Front)

Popište algoritmus hledání délky nejdelší rostoucí posloupnosti \(\mathtt{DelkaNrpRec}(i)\). Jak ho lze memoizovat? Ueďte časové složitosti.

### Odpověď (Back)

- Algoritmus pro dané \(i\) vrátí délku NRP začínající přávě prvkem \(x_i\).
- Postupně projdeme všechna \(x_j\) potenciálně navazující na \(x_i\).

- Pro každé takové \(x_j\) zavoláme rekurzivně totéž (čímž vypočítáme délku NRP začínající prvkem \(x_j\)).
- Ze všech potenciálně navazujících prvků \(x_j\) si pak vybereme ten, který má svou NRP nejdelší a k délce jeho NRP přičteme jedničku.

**Memoizace**

- Zavedeme z počátku prázdnou tabulku \(T[0, \dots, n]\).
- Na konci bude na pozici \(T[i]\) uložena délka nejdelší ze všech rostoucích posloupností začínající prvkem \(x_i\).
- Původní časovou složitost \(\mathcal O(2^n)\) tak vylepšíme na \(\mathcal O(n^2)\).

## Poznámka Anki 1669021947402

Karty Anki: 1669021947402
GUID: IN7<STR{a>; štítky: bi-ag1::p10 bi-spol::21.

### Otázka (Front)

Vyslovte a dokažte větu o korektnosti iterativního řešení hledání délky nejdelší rostoucí posloupnosti.

### Odpověď (Back)

NRP je po skončení výpočtu \(\mathtt{NrpIter}\) podposloupnost s indexy \(N[0], N[N[0]], N[N[N[0]]], \dots\).

**Důkaz**

- Kdykoliv se našlo větší \(T[i]\), uložil se do \(N[i]\) index druhého prvku příslušné delší rostoucí podposloupnosti začínající prvkem \(x_i\).
- Po skončení proto \(N[0]\) říká, jaký prvek je v optimálním řešení celé úlohy první, \(N[N[0]]\) udává druhý a tak dále.
- Pokud \(N[i] = \bot\) (\(\mathtt{nil}\)), pak \(x_i\) je maximem v \(x_i, \dots, x_n\) a každá případná rostoucí podposloupnost zde končí.
- Pokud existuje více řešení, \(\mathtt{NrpIter}\) vrátí to, které začíná nejvíce vlevo.

## Poznámka Anki 1669022062254

Karty Anki: 1669022062254
GUID: PK/eRX3/1#; štítky: bi-ag1::p10 bi-spol::21.

### Otázka (Front)

Jak z algoritmu hledání délky nejdelší rostoucí posloupnosti zkonstruujeme nejdelší rostoucí posloupnost?

### Odpověď (Back)

Během výpočtu délky NRP si stačí při každém nalezení lepšího řešení zapamatovat i příslušný navazující prvek.

## Poznámka Anki 1669027665702

Karty Anki: 1669027665702
GUID: MOtZf%o}z9; štítky: bi-ag1::p10 bi-spol::21.

### Otázka (Front)

Popište rekurzivní algoritmus hledání editační vzdálenosti řetězců. Jak lze memoizovat? Uveďte časové složitosti.

### Odpověď (Back)

- V nejkratší posloupnosti editačních operací se každého znaku týká nejvýše jedna editační operace (vložení, smazání nebo záměna znaku), takže editační operace lze vždy uspořádat zleva doprava.
- Můžeme si tedy představit, že procházíme \(x = x_1, \dots, x_m\) zleva doprava a postupně ho přetváříme na \(y = y_1, \dots, y_n\) a hledáme nejmenší počet editačních operací, kterými to dokážeme.

- Pokud \(x_1 = y_1\), můžeme první znak ponechat beze změny a rekurzivně pak tudíž platí \(L(x, y) = L(x_2 \dots x_m, y_2 \dots y_n)\).
- Jinak máme \(3\) možnosti, z nichž volíme tu, která dá nejmenší řešení:

- Znak \(x_1\) zaměníme za \(y_1\). Pak \(L(x, y) = 1 + L(x_2 \dots x_m, y_2 \dots y_n)\).
- Znak \(x_1\) smažeme. Pak \(L(x, y) = 1 + L(x_2 \dots x_m, y_1 \dots y_n)\).
- Před řetězec \(x\) vložíme znak \(y_1\). Pak \(L(x, y) = 1 + L(x_1 \dots x_m, y_2 \dots y_n)\).

- Editační vzdálenost \(2\) řetězců lze tedy vypočítat rekurzivně z editačních vzdálenosti jejich podřetězců, přesněji jejich suffixů.

**Memoizace**

- Hodnotu, kterou vrátí první zavolání \(\mathtt{EvrMem}(i, j)\) ukládáme do políčka \(M[i, j]\).

- Na konci bude \(M[i, j] = L(x_i \dots x_m, y_j \dots y_n)\).
- Řešení najdeme v \(M[1,1]\).
- Původní časovou složitost \(\mathcal O(3^{m + n - 1})\) tak vylepšíme na \(\mathcal O(m \cdot n)\).

