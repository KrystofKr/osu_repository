# NI-KOP – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1731965706813

Karty Anki: 1731965706813
GUID: zJf9J4DZ!e; štítky: ni-kop::p08 ni-spol::13.

### Otázka (Front)

Popište metodu úniku z lokálních optim lokálních heuristik a konkrétní metody jejich implementace.

### Odpověď (Back)

Metoda úniku z lokálních optim lokálních heuristik stojí na řízení ochoty algoritmu připustit akci, která vede k horšímu řešení. Podle této ochoty rozlišujeme dvě fáze výpočtu heuristiky:

- **diverzifikace **- vysoká ochota, vede k rovnoměrnému průzkumu stavového prostoru;

- **intenzifikace **- nízká ochota, vede ke konvergenci k finálnímu řešení.

Diverzifikace lokální heuristiky lze dosáhnout:

- **zvětšením okolí** - exponenciální velikost, Kernighan-Lin okolí;

- **prací s více stavy** - heuristika najednou používá vícero stavů.

## Poznámka Anki 1732037110503

Karty Anki: 1732037110503
GUID: kMJtpI$tfC; štítky: ni-kop::p08 ni-spol::15.

### Otázka (Front)

Popište obecnou strukturu simulovaného ochlazování.

### Odpověď (Back)

Simulované ochlazování se inicializuje s následujícími hodnotami:\[\begin{matrix}
s = s_0,\\
s_\text{best} = \emptyset,\\
T = T_0,
\end{matrix}\]kde \(s\) je aktuální stav, \(s_0\) je počáteční stav, \(s_\text{best}\) je nelepší nalezený stav, \(T\) je aktuální teplota a \(T_0\) je počáteční teplota. Dokud platí \(!\operatorname{\texttt{frozen}}(T, \dots)\), jsou iterovány následující kroky:

- dokud platí \(! \operatorname{\texttt{equilibrium}}(\dots)\) jsou iterovány následující kroky:

- na základě funkce \(\texttt{try}\) je z aktuálního stavu odvozen další stav

\[s = \operatorname{\texttt{try}}(s, T),\]

- pokud je nový stav lepší než nejlepší nalezený stav, je nejlepší nalezený stav aktualizován

\[s_\text{best} = s,\]

- na základě funkce \(\operatorname{\texttt{cool}}\) je aktualizována teplota

\[T = \operatorname{\texttt{cool}}(T, \dots).\]Po skončení hlavního cyklu vrací heuristika \(s_\text{best}\).

## Poznámka Anki 1732037532806

Karty Anki: 1732037532806
GUID: GaHf|BEdRL; štítky: ni-kop::p08 ni-spol::15.

### Otázka (Front)

Popište funkci \(\texttt{try}\) simulovaného ochlazování a způsob, kterým je řešena diverzifikace a intenzifikace.

### Odpověď (Back)

Funkce \(\texttt{try}\) simulovaného ochlazování dostává na vstupu aktuální stav \(s\) a aktuální teplotu \(T\). Její vyhodnocení probíhá následovně:

- z okolí \(s\) je náhodně vybrán sousední stav \(s'\);
- pokud je \(s'\) lepší než \(s\) je vrácen \(s'\) a funkce končí;
- v opačném případě je spočteno, o kolik je \(s'\) horší než \(s\) a tato hodnota je označena \(\delta\);
- z intervalu \(\langle 0, 1 \rangle\) je náhodně zvoleno číslo \(r\) a pokud je následující výraz pravdivý, je vráceno \(s'\), v opačném případě je vráceno \(s\)

\[r < e^{-\frac{\delta}{T}}.\]Můžeme pozorovat, že při vysoké teplotě se přijmou i velká zhoršení (diverzifikace) a naopak při nízké teplotě se zhoršení přijímají jen s nízkou pravděpodobností (intenzifikace).

## Poznámka Anki 1732043452114

Karty Anki: 1732043452114
GUID: PqvQt,Ob<V; štítky: ni-kop::p08 ni-spol::15.

### Otázka (Front)

Popište rozvrh ochlazování simulovaného ochlazování.

### Odpověď (Back)

Rozvrh ochlazování popisuje parametry simulovaného ochlazování. Bývá buď nastaven předem, nebo řízen zpětnou vazbou. Skládá se z následujících parametrů:

- **funkce **\(\texttt{cool}\) - řídí krok ochlazování, volena následovně:

\[\operatorname{\texttt{cool}}(T) = \alpha T, \quad  \alpha \in (0.8, 0.999);\]

- **funkce **\(\texttt{equilibrium}\) - řídí rychlost ochlazování, volena v závislosti na přijatých stavech nebo velikosti instance;

- **funkce **\(\texttt{frozen}\) - řídí zastavení heuristiky, typicky jakmile klesne četnost změn obecně nebo četnost změn k lepšímu pod nastavenou mez,

- **počáteční teplota **\(T_0\) - volena tak, aby přijetí zhoršující akce bylo pravděpodobné.

## Poznámka Anki 1732043664419

Karty Anki: 1732043664419
GUID: HX]O2Yzq(y; štítky: ni-kop::p08 ni-spol::15.

### Otázka (Front)

Popište způsoby nastavení počáteční teploty simulovaného ochlazování.

### Odpověď (Back)

Počáteční teplota simulovaného ochlazování je nastavována tak, aby přijetí zhoršující akce bylo pravděpodobné. Toho lze dosáhnout následujícími způsoby:

- pokud známe hloubku lokálních optim, vypočteme teplotu tak, aby pravděpodobnost úniku z optima měla požadovanou hodnotu;
- nasbíráme vzorky zhoršujících akcí a vypočteme teplotu,
- rychle zvyšujeme teplotu, sledujeme četnost přijatých zhoršujících akcí, zaznamenáme teplotu pro požadovanou pravděpodobnost úniku z lokálního optima a restartujeme algoritmus s novou počáteční teplotou.

