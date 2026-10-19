# NI-KOP – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1727109952224

Karty Anki: 1727109952224
GUID: okZ]m.)*dt; štítky: ni-kop::p01 ni-spol::11.

### Otázka (Front)

Čím je charakterizován kombinatorický problém?

### Odpověď (Back)

Charakterizace kombinatorického problému jsou prvky:

- vstupní proměnné,
- výstupní proměnné,
- konfigurační proměnné,
- omezení,
- optimalizační kritérium (pokud je třeba).

## Poznámka Anki 1727109976088

Karty Anki: 1727109976088
GUID: tW)6<zrQSk; štítky: ni-kop::p01 ni-spol::11.

### Otázka (Front)

Čím je charakterizována instance kombinatorického problému?

### Odpověď (Back)

Charakterizace instance kombinatorického problému je dána ohodnocením vstupních proměnných.

## Poznámka Anki 1727115600386

Karty Anki: 1727115600396
GUID: uCeG;Wf!C7; štítky: ni-kop::p01 ni-spol::11.

Metadata původního zdroje pro kartu 1727115600396: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište konfigurační proměnné. Jaký mají vztah k výstupním proměnným?

### Odpověď (Back)

Konfigurační proměnné jsou proměnné, jejichž ohodnocení jsou procházena při řešení problému hrubou silou. Musí platit, že:

- konfiguračních proměnných je konečný počet,
- nabývají konečně mnoha ohodnocení.
V určitých třídách problémů mohou být shodné s výstupními proměnnými (konstruktivní problémy), avšak není tomu tak vždy (rozhodovací problémy). Společně s ohodnocením vstupních proměnných lze z jejich ohodnocení:

- zkonstruovat hledaný výstup,
- zkontrolovat omezení,
- vypočíst hodnotu optimalizačního kritéria.

## Poznámka Anki 1727115697308

Karty Anki: 1727115697308
GUID: o-.4]@}w=.; štítky: ni-kop::p01 ni-spol::11.

### Otázka (Front)

Definujte konfiguraci.

### Odpověď (Back)

Konfigurace je ohodnocení konfiguračních proměnných.

## Poznámka Anki 1727115740564

Karty Anki: 1727115740564
GUID: C4Y0/#RrE6; štítky: ni-kop::p01 ni-spol::11.

### Otázka (Front)

Definujte řešení a optimální řešení.

### Odpověď (Back)

**Řešení** je konfigurace, která vyhovuje omezujícím podmínkám. **Optimální řešení** je takové řešení, které má nejlepší hodnotu optimalizačního kritéria.

## Poznámka Anki 1727116161448

Karty Anki: 1727116161448
GUID: x>|yjpS/e*; štítky: ni-kop::p01 ni-spol::11.

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

## Poznámka Anki 1727120623700

Karty Anki: 1727120623700
GUID: Kcurss@&o}; štítky: ni-kop::p01 ni-spol::11.

### Otázka (Front)

Popište optimalizační problémy.

### Odpověď (Back)

Nechť \(I \) je instance, \(Y\) je konfigurace, \(C(Y)\) je optimalizační kritérium a \(R(I, Y)\) je omezení určující, zda je \(Y\) řešením \(I\). Rozlišujeme následující optimalizační problémy:

- **optimalizační rozhodovací problém** - výstupem je \(\texttt{ano}\) nebo \(\texttt{ne}\):

- Existuje \(Y\) takové, že \(R(I, Y)\) a \(C(Y)\) je aspoň tak dobré jako daná konstanta \(K\)?;

- **optimalizační konstruktuvní problém** - výstupem je \(Y\):

- Sestrojte nějaké \(Y\) takové, že \(R(I, Y)\) a \(C(Y)\) je nejlepší možné.;

- **optimalizační enumerační problém** - výstupem je \(\{ Y \}\):

- Sestrojte všechna \(Y\) taková, že \(R(I, Y)\) a \(C(Y)\) je nejlepší možné.;

- **optimalizační početní problém** - výstupem je \(m \in \mathbb N\):

- Kolik je \(Y\) takových, že \(R(I, Y)\) a \(C(Y)\) je aspoň tak dobré jako daná konstanta \(K\)?;

- **optimalizační evaluační problém** - výstupem je \(C(Y)\):

- Zjistěte nejlepší možné \(C(Y)\) takové, že \(R(I, Y)\).

## Poznámka Anki 1727121395190

Karty Anki: 1727121395190
GUID: yTuj^fnXW$; štítky: ni-kop::p01 ni-spol::11.

### Otázka (Front)

Definujte 0/1 problém batohu.

### Odpověď (Back)

0/1 problém batohu je kombinatorický problém. Je dána nosnost batohu \(M\), množina \(U\) a pro každý prvek \(u \in U\):

- váha \(w(u) \in \mathbb N\),
- cena \(c(u) \in \mathbb N\).

Cílem je sestrojit množinu \(U'\) tak, aby

\[\displaystyle \sum_{u \in U'} w(u) \leq M \quad \text a \quad \displaystyle \sum_{u \in U'} c(u) \max,\]tedy aby nebyl batoh přetížen a cena věcí byla maximální.

## Poznámka Anki 1727121738469

Karty Anki: 1727121738469
GUID: NUK0AQ0D+@; štítky: ni-kop::p01 ni-spol::11.

### Otázka (Front)

Definujte problém splnitelnosti Booleovy formule (SAT).

### Odpověď (Back)

Problém splnitelnosti Booleovy formule (SAT) je kombinatorický problém. Je dána množina \(n\) booleovských proměnných \(X = \{ x_1, x_2, \dots, x_n \}\) a Booleova formule \(F(X)\) v KNT. Cílem je rozhodnout, zda je tato formule splnitelná, tedy rozhodnout, zda existuje ohodnocení \(Y : X \to \{ 0, 1 \}\) proměnných \(x_1, x_2, \dots, x_n\) takové, že
\[F \big( Y(X) \big) = 1.\]

