# BI-MA2 – Přednáška 11

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1666618595351

Karty Anki: 1666618595352
GUID: I)kg9,K-FS; štítky: bi-ma2::p11.

### Otázka (Front)

Definujte linární rekurentní rovnici.

### Odpověď (Back)

Lineární rekurentní rovnice řádu \(k \in \mathbb{N}\) je rovnice tvaru
\[x_{n+k} + c_{k-1,n} \cdot x_{n+k-1} + \cdots + c_{1,n} \cdot x_{n+1} + c_{0,n} \cdot x_n = b_n, \quad n\in \mathbb{Z}, n \geq n_0 \quad (\star)\]kde \(n_0 \in \mathbb{Z}\) a \((c_{i,n})_{n=n_0}^\infty\), \(i = 0, 1, \dots, k-1\), (tzv. **koeficienty rovnice**) a \((b_n)_{n=n_0}^\infty\) (tzn. **pravá strana rovnice**) jsou zadané posloupnosti a posloupnost \((c_{0,n})_{n=n_0}^\infty\) není nulová posloupnost.

Jestliže \(b_n = 0\) pro každé \(n \geq n_0\), pak se příslušná rovnice nazývá **homogenní**.

Jako **neznámou **v této rovnici chápeme posloupnost \((x_n)_{n=n_0}^\infty\).

**Přidruženou homogenní rovnici** k rovnici \((\star)\) nazýváme LRR se stejnými koeficienty a nulovou pravou stranou (\(b_n = 0\) pro každé \(n \geq n_0\)).

## Poznámka Anki 1666618744340

Karty Anki: 1666618744340
GUID: U#vLAGXA?; štítky: bi-ma2::p11.

### Otázka (Front)

Definujte řešení LRR.

### Odpověď (Back)

Nechť je dána lineární rekurentní rovnice řádu \(k \in \mathbb{N}\)
\[x_{n+k} + c_{k-1,n} \cdot x_{n+k-1} + \cdots + c_{1,n} \cdot x_{n+1} + c_{0,n} \cdot x_n = b_n, \quad n\in \mathbb{Z}, n \geq n_0. \quad (\star)\]Jejím **řešením** nazveme libovolnou posloupnost \((x_n)_{n=n_0}^\infty\) takovou, že dosazením jejích členů do \((\star)\) dostaneme pravdivé rovnosti pro každé celočíselné \(n \geq n_0\).

## Poznámka Anki 1666619055220

Karty Anki: 1666619055220
GUID: CvkFgCfi@; štítky: bi-ma2::p11.

### Otázka (Front)

Definujte počáteční podmínky LRR.

### Odpověď (Back)

Nechť je dána lineární rekurentní rovnice řádu \(k \in \mathbb{N}\),
\[x_{n+k} + c_{k-1,n} \cdot x_{n+k-1} + \cdots + c_{1,n} \cdot x_{n+1} + c_{0,n} \cdot x_n = b_n, \quad n\in \mathbb{Z}, n \geq n_0.\]**Počátečními podmínkami** pro tuto rovnici nazveme libovolnou soustavu rovností \(x_{n_0} = A_0, \ x_{n_0+1} = A_1, \dots,\ x_{n_0 + k-1} = A_{k-1} \), pro zadané hodnoty \(A_0, \dots, A_{k-1} \in \mathbb{R}\).

## Poznámka Anki 1666619181957

Karty Anki: 1666619181957
GUID: *E(Y3eOK&; štítky: bi-ma2::p11.

### Otázka (Front)

Vyslovte a dokažte větu o existenci a jednoznačnosti řešení LRR.

### Odpověď (Back)

Podle věty o existenci a jednoznačnosti řešení LRR platí následující tvrzení:

- Každá lineární rekurentní rovnice má nějaké řešení.
- Je-li dána lineární rekurentní rovnice řádu \(k \in \mathbb{N}\) s předepsanými \(k\) počátečními podmínkami, pak existuje právě jedno řešení této rovnice spojující tyto počáteční podmínky.

**Důkaz** 

Nejprve dokažme první bod. Mějme LRR řádu \(k \in \mathbb{N}\) tvaru
\[x_{n+k} + \sum_{i=0}^{k-1} c_{i,n}x_{n+i} = b_n, \quad n \in \mathbb{Z}, n \geq n_0.\]Zvolme \(A_0, \dots, A_{k-1}\) libovolně a položme \(X_{n_0} := A_0, \dots, X_{n_0 + k-1} := A_{k-1}\). Poté postupně vypočtěme \(X_{n_0+k}\), \(X_{n_0 + k + 1}, \dots\) pomocí předpisu
\[X_{n+k} := b_n - \sum_{i=0}^{k-1} c_{i,n}X_{n+i}, \quad n \in \mathbb{Z}, n \geq n_0.\]Takto zkonstruovaná posloupnost \((X_n)_{n=n_0}^\infty\) je řešením naší LRR. Jsou-li počáteční podmínky \(A_0, \dots, A_{k-1}\) předepsány, pak z předchozího bodu vidíme, že už jednoznačně udávají hodnoty řešení \(X_n\) pro \(n \geq n_0 + k\) a tedy jednoznačně udávají i celé řešení (jakožto posloupnost) a tím je dokázán druhý bod.

## Poznámka Anki 1667223730264

Karty Anki: 1667223730264
GUID: cpmh)1B:r%; štítky: bi-ma2::p11.

### Otázka (Front)

Vyslovte větu o principu superpozice.

### Odpověď (Back)

Uvažme dvě LRR \(k\)-tého řádu s ne nutně shodnými pravými stranami,
\[x_{n+k}+ \sum \limits_{i=0}^{k-1} c_{i,n} x_{n+i} = b_n, \quad (1)\]\[x_{n+k}+ \sum \limits_{i=0}^{k-1} c_{i,n} x_{n+i} = \tilde{b}_n, \quad (2)\]pro \(n \in \mathbb{Z}, n \geq n_0\).
Je-li \((X_n)_{n=n_0}^\infty\) řešení \((1)\) a \((Y_n)_{n=n_0}^\infty\) řešení \((2)\), potom pro libovolnou konstantu \(\alpha\) je posloupnost \((X_n + \alpha Y_n)_{n=n_0}^\infty\) řešením LRR
\[x_{n+k}+ \sum \limits_{i=0}^{k-1} c_{i,n} x_{n+i} = b_n + \alpha \tilde{b}_n, \quad n \geq n_0.\]

## Poznámka Anki 1667224097785

Karty Anki: 1667224097785
GUID: ra/)=Yi/.&; štítky: bi-ma2::p11.

### Otázka (Front)

Vyslovte větu o struktuře množiny řešení LRR.

### Odpověď (Back)

Mějme LRR řádu \(k \in \mathbb{N}\) tvaru
\[x_{n+k}+ \sum \limits_{i=0}^{k-1} c_{i,n} x_{n+i} = b_n, \quad n \in \mathbb{Z}, n \geq n_0, \quad (\star)\]a označme množinu všech jejích řešení symbolem \(S\) a množinu všech řešení přidružené homogenní rovnice symbolem \(S_0\).
Potom platí následující tvrzení:

- Množina \(S_0\) je vektorový prostor dimenze \(k\).
- Množina \(S\) je tvaru \(S = (\tilde{x}_n)_{n=n_0}^\infty + S_0\), kde \((\tilde{x}_n)_{n=n_0}^\infty\) je (partikulární) řešení rovnice \((\star)\).

