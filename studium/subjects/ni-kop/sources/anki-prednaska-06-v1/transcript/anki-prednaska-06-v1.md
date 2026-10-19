# NI-KOP – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1730847008951

Karty Anki: 1730847008951
GUID: uxJ~[b8tPn; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Popište princip globálních a lokálních heuristických metod.

### Odpověď (Back)

Heuristické metody stojí na následujících principech:

- **globální metody** - dekomponují instanci na vícero menších instancí a z jejich řešení skládají výsledné řešení, někdy označovány jako metody divide-and-conquer (rozděl a panuj);
- **lokální metody** - stojí na prohledávání stavového prostoru, zaměřují se na aktuální konfiguraci a příští konfiguraci vybírají z jejích sousedů.

## Poznámka Anki 1730895917648

Karty Anki: 1730895917661
GUID: w2lJz&;q.{; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Definujte stav algoritmu.

### Odpověď (Back)

Mějme vnitřní proměnné \(Z\) algoritmu \(A\) řešícího problém \(\Pi\) s konfiguračními proměnnými \(Y\). Každé ohodnocení \(s\) proměnných \(Z \cup Y\) nazýváme stavem algoritmu \(A\) řešícího \(I\).

## Poznámka Anki 1730897613135

Karty Anki: 1730897613135
GUID: uf15@T9P-R; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Definujte stavový prostor a akci.

### Odpověď (Back)

Mějme množinu všech stavů \(S = \{ s_i \}\) algoritmu \(A\) řešícího instanci \(I\). Nechť \(Q = \{ q_j \}\) je množina operátorů takových, že
\[q_j : S \to S, \quad q_j(s_i) \neq s_i, \quad \forall q_j, \forall s_i.\]Dvojici \((S, Q)\) pak nazýváme **statovým prostorem** algoritmu \(A\) řešícího \(I\). Aplikace \(q_j\) na \(s_i\) se nazývá **akce**.

## Poznámka Anki 1730897740568

Karty Anki: 1730897740568
GUID: AO`M#s&6=>; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Popište vlastnosti grafu stavového prostoru lokální heuristiky.

### Odpověď (Back)

Graf stavového prostoru lokální heuristiky může mít v závislosti na typu heuristiky následující vlastnosti:

- **acykličnost** - jednodušší heuristiky, typicky hladové algoritmy;
- **cykličnost** - složitější heuristiky.

## Poznámka Anki 1730898925137

Karty Anki: 1730898925137
GUID: x5exz(Vh,k; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Popište relaxaci ve stavovém prostoru.

### Odpověď (Back)

Relaxací** **ve stavovém prostoru nazýváme převedení omezení kombinatorického problému na pokutu v jeho optimalizačním kritériu. Výpočet relaxace probíhá z:

- optimalizačního kritéria,
- pokuty (odhadu vzdálenosti od řešení),
- experimentálně nastaveného numerického parametru.
Upuštení od omezení umožňuje operátorům přejít do stavů, které nejsou řešením, což zlepšuje dosažitelnost stavového prostoru, zatímco pokuta algoritmus od vstupu do takových stavů odrazuje.

## Poznámka Anki 1730918164873

Karty Anki: 1730918164873
GUID: dKiPG!1Pk?; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Definujte úplnou strategii prohledávání stavového prostoru.

### Odpověď (Back)

Úplná strategie** **prohledávání stavového prostoru je strategie, která navštíví všechny stavy kromě těch, o kterých je známo, že nedávají řešení (nebo optimální řešení).

## Poznámka Anki 1730919334237

Karty Anki: 1730919334238
GUID: jxBn+E<%_%; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Definujte systematickou strategii prohledávání stavového prostoru a popište její vlastnosti.

### Odpověď (Back)

Systematická strategie prohledávání stavového prostoru je úplná strategie, která každý stav navštíví nejvýše jednou. Pro systematické strategie platí:

- bez prořezávání je složitost nejhoršího případu rovna řešení hrubou silou;
- pokud řešení (nebo optimální řešení) existuje, pak jej systematická strategie nalezne.

## Poznámka Anki 1730919427958

Karty Anki: 1730919427958
GUID: f0<@{VSq]7; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Popište realizace systematických strategií prohledávání stavového prostoru.

### Odpověď (Back)

Systematické strategie prohledávání stavového prostoru lze realizovat v následujících podobách:

- **prohledávání do šířky** (BFS) - pomocí fronty,
- **prohledávání do hloubky **(DFS) - pomocí zásobníku,
- **prohledávání metodou „nejlepší nejdříve“ **(best first) - pomocí prioritní fronty.

## Poznámka Anki 1730921761116

Karty Anki: 1730921761116
GUID: Ik*F#/_SU^; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Popište metody lokálních heuristik.

### Odpověď (Back)

Metody lokálních heuristik se liší ve způsobu výběru příštího stavu (implementaci funkce \(\texttt{try}\)):

- **metoda „pouze nejlepší“ **(best-only) - vybere stav, který je řešením, je lepší než aktuální stav a je nejlepší ze všech sousedů aktuálního stavu;
- **metoda „první zlepšení“** (first improvement) - vybere stav, který je řešením a je prvním lepším sousedním stavem aktuálního stavu (ostatní sousedy už neposuzuje);

- **metoda Kernighan-Lin** - okolí stavu zkonstruuje opakovanou aplikací jednoho operátoru (Kernighan-Lin okolí) a následně vybere stav metodou „pouze nejlepší.“

### Doplňující pole (Extra)

Mezi pokročilé lokální heuristiky dále patří simulované ochlazování a simulovaná evoluce, které se však svou strukturou od základních lokálních heuristik liší.

## Poznámka Anki 1731967479899

Karty Anki: 1731967479899
GUID: br{DPf97--; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Popište obecnou strukturu lokální heuristiky.

### Odpověď (Back)

Lokální heuristika se inicializuje s následujícími hodnotami:\[\begin{matrix}
s = s_0,\\
s_\text{best} = \emptyset,
\end{matrix}\]kde \(s\) je aktuální stav, \(s_0\) je počáteční stav a \(s_\text{best}\) je nejlepší nalezený stav. Dokud platí \(s \neq \emptyset\), jsou iterovány následující kroky:

- pokud je aktuální stav řešením a je lepší než nejlepší nalezený stav, je nejlepší nalezený stav aktualizován

\[s_\text{best} = s;\]

- na základě funkce \(\texttt{try}\) je z aktuálního stavu odvozen další stav

\[s = \operatorname{\texttt{try}}(s).\]Jakmile funkce \(\texttt{try}\) vrátí prázdný stav, je heuristika ukončena a vrací \(s_\text{best}\).

## Poznámka Anki 1737638829300

Karty Anki: 1737638829300
GUID: trWb}buMNr; štítky: ni-kop::p06 ni-spol::13.

### Otázka (Front)

Popište prostor prohledávání.

### Odpověď (Back)

Prostor prohledávání se od stavového prostoru liší tím, že ohodnocení proměnných jeho prvků může být nedefinované. Dosazením všech možných hodnot za nedefinované proměnné vzniká podmnožina stavového prostoru.

### Doplňující pole (Extra)

Předpokládejme stav kódovaný pomocí binárního řetězce \(\texttt{011}\) (např. pro rozhodovací 0/1 problém batohu). V prostoru prohledávání by pak byl přípustný např. prvek \(\texttt{0?1}\) a dosazením všech možných hodnot za nedefinovanou proměnnou lze získat stavy \(\texttt{011}\) a \(\texttt{001}\), které tvoří podmnožinu stavového prostoru.

