# BI-AAG – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aag/BI-AAG.apkg; APKG SHA-256 0383847389324f3b83b349363b7ad16a6bf91673c90b7a96ed1a57b25a85f8af. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b9cda20d5a5a9d1ff47d4e1fc58b10ed3ac7a37c72c6c1431cc7cb67e2ca10c.
Původní balíčky: BI-AAG
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1667215355928

Karty Anki: 1667215355930
GUID: be!=5tDZ{A; štítky: bi-aag::p06.

Metadata původního zdroje pro kartu 1667215355930: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak zní **pumping lemma**?

### Odpověď (Back)

Nechť \(L\) je regulární jazyk. Pak pro jazyk \(L\) existuje konstanta \(p \in \mathbb{N}\) taková, že pro každý řetězec \(w \in L\), kde \(|w| \geq p\), platí, že \(w\) lze zapsat ve tvaru \(w=x y z\) tak, že \(|y| \geq 1\) a \(|xy| \leq p\) a \(\forall k \in \mathbb{N}_0\) platí, že \(xy^kz \in L\).

### Doplňující pole (Extra)

Té části, která začíná slovy „pro \(L\) existuje konstanta“, se říká „pumpovací vlastnost. Platí, že každý regulární jazyk tuto vlastnost má. Pumping lemma ovšem neříká, že tuto vlastnost nemohou mít i některé jazyky, které regulární nejsou.

## Poznámka Anki 1667215475423

Karty Anki: 1667215475423
GUID: CQR;@!9k^j; štítky: bi-aag::p06.

Metadata původního zdroje pro kartu 1667215475423: v původním balíčku pozastavená karta.

### Otázka (Front)

Mějme neregulární jazyk \(L\), který nemá pumpující vlastnost. Jak pomocí pumping lemma **dokážete**, že jazyk \(L\) **není regulární**?

### Odpověď (Back)

Důkaz provedeme sporem. Předpokládáme, že jazyk \(L\) je regulární. Pak na základě pumping lemmatu musí mít pumpovací vlastnost. Ukážeme však, že tuto vlastnost nemá (tím dostaneme spor s předpokladem, že jazyk \(L\) je regulární):

1. Pro všechny \(p \in \mathbb{N}\) zvolíme řetězec \(w\) tak, aby \(w \in L \land |w| \geq p\).
2. Najdeme všechny rozklady \(xyz\) pro zvolený řetězec \(w\) tak, aby \(w = xyz \land |xy| \leq p \land |y| \geq 1\).
3. Najdeme alespoň jedno \(k \in \mathbb{N}_0\) pro každý jednotlivý rozklad tak, aby \(xy^kz \notin L\).

## Poznámka Anki 1667506864536

Karty Anki: 1667506864536
GUID: eH~5k~(Hg+; štítky: bi-aag::p06.

Metadata původního zdroje pro kartu 1667506864536: v původním balíčku pozastavená karta.

### Otázka (Front)

Zapište pumping lemma jako formuli.

### Odpověď (Back)

\[L \text{ je regulární jazyk} \implies (\exists p \geq 1) (\forall w \in L) \Big[ |w| \geq p \implies (\exists x, y, z \in \Sigma^*) (w = xyz \ \land |xy| \leq p \ \land |y| \geq 1 \ \land (\forall k \geq 0) \ xy^kz \in L) \Big]\]

## Poznámka Anki 1672151459538

Karty Anki: 1672151459538
GUID: Hz,C^E@tF:; štítky: bi-aag::p06.

Metadata původního zdroje pro kartu 1672151459538: v původním balíčku pozastavená karta.

### Otázka (Front)

Vyslovte **Myhill-Nerodovu větu**.

### Odpověď (Back)

Nechť \(L\) je jazyk nad abecedou \(\Sigma\), pak následující tři tvrzení jsou ekvivalentní:

1. \(L\) je přijímaný deterministickým konečným automatem.

2. Existuje pravá kongruence \(\sim\) konečného indexu na \(\Sigma^*\) taková, že \(L\) je sjednocením některých jejích tříd rozkladu \(\Sigma^* / \sim\).
3. Relace prefixové ekvivalence \(\sim_L\) má konečný index.

## Poznámka Anki 1672151537098

Karty Anki: 1672151537098
GUID: xu<5^%.fo%; štítky: bi-aag::p06.

Metadata původního zdroje pro kartu 1672151537098: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **pravou kongruenci**.

### Odpověď (Back)

Nechť \(\Sigma\) je abeceda a \(\sim\) je relace ekvivalence na \(\Sigma^*\). Řekneme, že \(\sim\) je pravá kongruence, jestliže platí, že
\[\forall u, v, w \in \Sigma^* : u \sim v \implies uw \sim vw.\]

## Poznámka Anki 1672151714899

Karty Anki: 1672151714899
GUID: te|wzbMseG; štítky: bi-aag::p06.

Metadata původního zdroje pro kartu 1672151714899: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **prefixovou ekvivalenci**.

### Odpověď (Back)

Nechť \(L\) je libovolný jazyk nad abecedou \(\Sigma\). Prefixovou ekvivalenci \(\sim_L\) na \(\Sigma^*\) pro jazyk \(L\) a \(u, v \in \Sigma^*\) definujeme následovně:
\[u \sim_L v \iff (\forall w \in \Sigma^* : uw \in L \iff vw \in L).\]

### Doplňující pole (Extra)

Pro každý jazyk \(L\) je prefixová ekvivalence pravou kongruencí.

## Poznámka Anki 1672152218935

Karty Anki: 1672152218935
GUID: h0p~9X;Qa*; štítky: bi-aag::p06.

Metadata původního zdroje pro kartu 1672152218935: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak pomocí **Myhill-Nerodovy věty** dokážeme, že jazyk \(L\) není regulární?

### Odpověď (Back)

Důkaz provedeme sporem. Předpokládáme, že \(L\) je regulární (přesněji řečeno předpokládáme, že pro \(L\) existuje DKA, který ho přijímá). Pak podle Myhill-Nerodovy věty musí existovat pravá kongruence \(\sim\) konečného indexu \(k\) taková, že jazyk \(L\) je sjednocením některých jejích tříd rozkladu \(\Sigma^* / \sim\). Ukážeme však, že taková kongurence nemůže existovat (tím dostaneme spor s předpokladem, že jazyk \(L\) měl být regulární).

1. Zvolíme \(k + 1\) vhodných konkrétních řetězců \(w_1\), \(w_2\), \(\dots\), \(w_{k+1}\) nad abecedou \(\Sigma\).
2. Vzhledem k tomu, že těchto řetězců je \(k + 1\) a my máme pouze \(k\) tříd rozkladu, musí nutně minimálně dva řetězce být ve stejné třídě. Formálně zapsáno: \[\exists i,j \in \set{1, 2, \dots, k + 1} : i \neq j \land w_i \sim w_j.\]
3. Zvolíme vhodný řetězec \(u\), pro který ukážeme, že \(w_iu \in L \land w_ju \notin L\). Pokud totiž jazyk \(L\) má být sjednocením některých tříd rozkladu, otázka zní, jestli konkrétně třída \([w_iu] = [w_ju]\) v \(L\) je nebo není. Na jednu stranu tvrdíme, že by měla, na druhou současně že ne. To ale není možné. Tedy kdyby taková pravá kongruence \(\sim\) konečného indexu \(k\) existovala, pak jazyk \(L\) nemůže být sjednocením nějakých jejích tříd.
4. Dostali jsme spor s předpokladem, že jazyk \(L\) je regulární. Jazyk \(L\) tedy regulární není.

## Poznámka Anki 1672152287406

Karty Anki: 1672152287406
GUID: Gi&/|i7]nN; štítky: bi-aag::p06.

Metadata původního zdroje pro kartu 1672152287406: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **třídu ekvivalence**.

### Odpověď (Back)

Třída ekvivalence prvku \(a\) (značíme \([a]\)) na množině \(X\) je podmnožina \(X\) obsahující všechny prvky ekvivalentní s \(a\).

## Poznámka Anki 1672152431370

Karty Anki: 1672152431370
GUID: RhLK.R|.q>; štítky: bi-aag::p06.

Metadata původního zdroje pro kartu 1672152431370: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte **index ekvivalence**.

### Odpověď (Back)

Nechť \(\Sigma\) je abeceda a \(\sim\) je ekvivalence. Index ekvivalence \(\sim\) je počet tříd ekvivalence v \(\Sigma / \sim\). Jestliže existuje nekonečně mnoho tříd ekvivalence, definujeme index jako \(\infty\) a v takovém případě říkámě, že \(\sim\) má nekonečný index. Jinak má \(\sim\) konečný index.

## Poznámka Anki 1672152945143

Karty Anki: 1672152945144
GUID: PEr5Xkx?][; štítky: bi-aag::p06.

Metadata původního zdroje pro kartu 1672152945144: v původním balíčku pozastavená karta.

### Otázka (Front)

Vyslovte **2. variantu Myhill-Nerodovy věty**.

### Odpověď (Back)

Počet stavů libovolného minimálního DKA přijímajícího jazyk \(L\) je roven indexu \(\sim_L\). Takový DKA existuje právě tehdy, když je index \(\sim_L\) konečný.

