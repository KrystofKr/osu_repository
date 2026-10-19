# BI-MA2 – Přednáška 12

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1667226179795

Karty Anki: 1667226179795
GUID: n_j)5CB$xY; štítky: bi-ma2::p12.

### Otázka (Front)

Definujte LRR s konstantními koeficienty.

### Odpověď (Back)

Lineární rekurentní rovnice řádu \(k \in \mathbb{N}\) s konstantními koeficienty je rovnice tvaru
\[x_{n+k} + c_{k-1} \cdot x_{n+k-1} + \cdots + c_1 \cdot x_{n+1} + c_0 \cdot x_n = b_n, \quad n \in \mathbb{Z}, n \geq n_0, \quad (\dagger)\]kde \(n_0 \in \mathbb{Z}\) a \(c_i \in \mathbb{R}\), \(i = 0, 1, \dots, k-1\), (tzv. **koeficienty rovnice**), \(c_0 \neq 0\), jsou zadané konstanty a \((b_n)_{n=n_0}^\infty\) je zadaná posloupnost (tzv. **pravá strana rovnice**).

Jestliže \(b_n = 0\) pro kažé \(n \geq n_0\), pak se příslušná rovnice nazývá **homogenní**.

Jako **neznámou **v této rovnici chápeme posloupnost \((x_n)_{n=n_0}^\infty\).

Přidruženou homogenní rovnicí k rovnici \((\dagger)\) nazýváme LRR se stejnými koeficienty a nulovou pravou stranou \((b_n = 0\) pro každé \(n > n_0\)).

## Poznámka Anki 1667226401990

Karty Anki: 1667226401991
GUID: L$gZ)OkvT,; štítky: bi-ma2::p12.

### Otázka (Front)

Definujte charakteristický polynom a charakteristická čísla LRR s konstantními koeficienty.

### Odpověď (Back)

Nechť je dána lineární rekurentní rovnice řádu \(k \in \mathbb N\) s konstantními koeficienty
\[x_{n+k} + c_{k-1} \cdot x_{n+k-1} + \cdots + c_1 \cdot x_{n+1} + c_0 \cdot x_n = b_n, \quad n \in \mathbb{Z}, n \geq n_0.\]Charakteristickým polynomem této rovnice nazýváme polynom stupně \(k\) tvaru
\[p(\lambda) = \lambda^k + c_{k-1} \lambda^{k-1} + \cdots + c_1 \lambda + c_0.\]Kořeny (obecně komplexní čísla) tohoto polynomu se nazývají charakteristická (nebo vlastní) čísla zadané LRR.

## Poznámka Anki 1667226683489

Karty Anki: 1667226683489
GUID: e*hn_q4yfN; štítky: bi-ma2::p12.

### Otázka (Front)

Vyslovte a dokažte větu o konstrukci řešení homogenní LRR s konstantními koeficienty pomocí charakteristického čísla.

### Odpověď (Back)

Jestliže \(\lambda\) je charakteristickým číslem homogenní LRR řádu \(k \in \mathbb{N}\) s konstantními koeficienty
\[x_{n+k} + c_{k-1} \cdot x_{n+k-1} + \cdots + c_1 \cdot x_{n+1} + c_0 \cdot x_n = 0, \quad n \geq n_0,\]pak posloupnost \((\lambda^n)_{n=n_0}^\infty\) je jejím řešením.

**Důkaz
**Číslo \(\lambda\) splňuje \(p(\lambda) = \lambda^k + c_{k-1}\lambda^{k-1} + \cdots + c_1 \lambda + c_0 = 0\), a proto
\[\lambda^{n+k} + \sum \limits_{i=0}^{k-1}c_i \lambda^{n+i} = \lambda^n \cdot p(\lambda) = \lambda^n \cdot 0 = 0\]pro každé \(n \geq n_0\).

## Poznámka Anki 1667228521059

Karty Anki: 1667228521059
GUID: kb+#gY;]cF; štítky: bi-ma2::p12.

### Otázka (Front)

Vyslovte větu o konstrukci báze řešení homogenní LRR s konstantními koeficienty pomocí charakteristických čísel vyšší násobnosti.

### Odpověď (Back)

Jestliže \(\lambda\) je charakteristickým číslem homogenní LRR řádu \(k \in \mathbb{N}\) s konstantními koeficienty
\[x_{n+k} + c_{k-1} \cdot x_{n+k-1} + \cdots + c_1 \cdot x_{n+1} + c_0 \cdot x_n = 0, \quad n \geq n_0,\]a jeho násobnost je \(m\), pak posloupnosti \((\lambda^n)_{n=n_0}^\infty\), \((n\lambda^n)_{n=n_0}^\infty, \dots, (n^{m-1}\lambda^n)_{n=n_0}^\infty\) jsou jejím řešením a tvoří LN soubor.

## Poznámka Anki 1667316638431

Karty Anki: 1667316638431
GUID: Xp1km>c^;; štítky: bi-ma2::p12.

### Otázka (Front)

Vyslovte větu o konstrukci báze řešení homogenní LRR s konstantními koeficienty pomocí charakteristických čísel násobnosti \(1\).

### Odpověď (Back)

Uvažme homogenní LRR řádu \(k \in \mathbb{N}\) s konstantními koeficienty
\[x_{n+k} + c_{k-1} \cdot x_{n+k-1} + \cdots + c_1 \cdot x_{n+1} + c_0 \cdot x_n = 0, \quad n \geq n_0.\]Jestliže má \(k\) vzájemně různých charakteristických čísel \(\lambda_i\), \(i \in \hat{k}\), pak soubor posloupností \((\lambda_i^n)_{n=n_0}^\infty\), \(i \in \hat{k}\), tvoří bázi \(S_0\), tedy libovolné řešení \((x_n)_{n=n_0}^\infty \in S_0\) je tvaru
\[x_n = \alpha_1 \lambda_1^n + \cdots + \alpha_k \lambda_k^n, \quad n \geq n_0,\]pro nějaké konstanty \(\alpha_1, \dots, \alpha_k\).

## Poznámka Anki 1667316955478

Karty Anki: 1667316955478
GUID: w%mIX5lf^R; štítky: bi-ma2::p12.

### Otázka (Front)

Vyslovte obecnou větu o bázi prostoru \(S_0\) LRR s konstantními koeficienty.

### Odpověď (Back)

Uvažme homogenní LRR řádu \(k \in \mathbb{N}\) s konstantními koeficienty
\[x_{n+k} + c_{k-1} \cdot x_{n+k-1} + \cdots + c_1 \cdot x_{n+1} + c_0 \cdot x_n = 0, \quad n \geq n_0.\]Jestliže má \(K\) vzájemně různých charakteristických čísel \(\lambda_i\), \(i \in \hat{K}\), každé s násobností \(m_i \in \hat{k}\), pak soubor posloupností
\[\bigg( (\lambda_1^n)_{n=n_0}^\infty, (n \lambda_1^n)_{n=n_0}^\infty, \dots, (n^{m_1 - 1}\lambda_1^n)_{n=n_0}^\infty, \dots, (\lambda_K^n)_{n=n_0}^\infty, (n \lambda_K^n)_{n=n_0}^\infty, \dots, (n^{m_K-1}\lambda_K^n)_{n=n_0}^\infty \bigg)\]tvoří bázi \(S_0\).

## Poznámka Anki 1667319284421

Karty Anki: 1667319284421
GUID: C-sUkG5o5O; štítky: bi-ma2::p12.

### Otázka (Front)

Definujte kvazipolynom.

### Odpověď (Back)

Řekneme, že posloupnost je \((b_n)_{n=n_0}^\infty\) je kvazipolynom, jestliže existuje \(\lambda \in \mathbb{R}\) a polynom \(P(x)\) takový, že \(b_n = P(n) \lambda^n\) pro všechna přirozená \(n \geq n_0\).

## Poznámka Anki 1667319544329

Karty Anki: 1667319544329
GUID: zk6^-?StEU; štítky: bi-ma2::p12.

### Otázka (Front)

Vyslovte větu o partikulárním řešení LRR s konstantními koeficienty a kvazipolynomiální pravou stranou.

### Odpověď (Back)

Uvažujme homogenní LRR řádu \(k \in \mathbb{N}\) s konstantními koeficienty
\[x_{n+k} + c_{k-1} \cdot x_{n+k-1} + \cdots + c_1 \cdot x_{n+1} + c_0 \cdot x_n = b_n, \quad n \geq n_0,\]a nechť \((b_n)_{n=n_0}^\infty\) je kvazipolynom, tj. \(b_n = P(n) \lambda^n\), \(n \geq n_0\), pro nějaký polynom \(P(x)\) a číslo \(\lambda \in \mathbb{R}\).
Defiunjme \(m \in \mathbb{N}_0\) následujícím způsobem:

- pokud je \(\lambda\) charakteristické číslo uvažované LRR, pak nechť je \(m\) je jeho násobnost,
- jinak nechť \(m\) je nula.

Potom existuje polynom \(Q(x)\) stupně stejného jako \(P(x)\) takový, že posloupnost

\[\bigg(n^mQ(n)\lambda^n\bigg)_{n=n_0}^\infty\]je řešením uvažované LRR.

