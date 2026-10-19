# NI-PDP – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-pdp/NI-PDP.apkg; APKG SHA-256 b38783778a590460b03050d14b21f60017ff90d9b0abe806748521d92454df28. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: da16e1b818a2fcaa42e78195ece6396a24afd5754b63362dce0d5df6925e0f3f.
Původní balíčky: NI-PDP
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1741171750951

Karty Anki: 1741171750951
GUID: qBKE$fi):K; štítky: ni-pdp::p03.

Metadata původního zdroje pro kartu 1741171750951: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Čím je charakterizován kombinatorický problém?

### Odpověď (Back)

Charakterizace kombinatorického problému jsou prvky:

- vstupní proměnné,
- výstupní proměnné,
- konfigurační proměnné,
- omezení,
- optimalizační kritérium (pokud je třeba).

## Poznámka Anki 1741171961867

Karty Anki: 1741171961867
GUID: qv(2Xo:v]+; štítky: ni-pdp::p03.

Metadata původního zdroje pro kartu 1741171961867: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište realizace systematických strategií prohledávání stavového prostoru.

### Odpověď (Back)

Systematické strategie prohledávání stavového prostoru lze realizovat v následujících podobách:

- **prohledávání do šířky** (BFS) - pomocí fronty,
- **prohledávání do hloubky **(DFS) - pomocí zásobníku,
- **prohledávání metodou „nejlepší nejdříve“ **(best first) - pomocí prioritní fronty.

## Poznámka Anki 1741171978538

Karty Anki: 1741171978538
GUID: oA>5)@v<A5; štítky: ni-pdp::p03.

Metadata původního zdroje pro kartu 1741171978538: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte stavový prostor a akci.

### Odpověď (Back)

Mějme množinu všech stavů \(S = \{ s_i \}\) algoritmu \(A\) řešícího instanci \(I\). Nechť \(Q = \{ q_j \}\) je množina operátorů takových, že
\[q_j : S \to S, \quad q_j(s_i) \neq s_i, \quad \forall q_j, \forall s_i.\]Dvojici \((S, Q)\) pak nazýváme **statovým prostorem** algoritmu \(A\) řešícího \(I\). Aplikace \(q_j\) na \(s_i\) se nazývá **akce**.

## Poznámka Anki 1741172015877

Karty Anki: 1741172015877
GUID: g^:z{+(3Rs; štítky: ni-pdp::p03.

Metadata původního zdroje pro kartu 1741172015877: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište problémy bez optimalizačního kritéria.

### Odpověď (Back)

Nechť \(I\) je instance, \(Y\) je konfigurace a \(R(I, Y)\) je omezení určující, zda je \(Y\) řešením \(I\). Rozlišujeme následující problémy bez optimalizačního kritéria:

- **rozhodovací problém** - výstupem je \(\texttt{ano}\) nebo \(\texttt{ne}\):

- Existuje \(Y\) takové, že \(R(I, Y)\)?,
- Platí pro všechna \(Y\), že \(R(I, Y)\)?;

- **konstruktivní problém** - výstupem je \(Y\):

- Sestrojte nějaké \(Y\) takové, že \(R(I, Y)\).;

- **enumerační problém** - výstupem je \(\{ Y \}\):

- Sestrojte všechna \(Y\) taková, že \(R(I, Y)\).;

- **početní problém** - výstupem je \(m \in \mathbb N\):

- Kolik je \(Y\) takových, že \(R(I, Y)\)?.

