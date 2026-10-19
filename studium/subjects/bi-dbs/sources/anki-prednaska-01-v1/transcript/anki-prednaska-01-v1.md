# BI-DBS – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-dbs/BI-DBS.apkg; APKG SHA-256 2adef415f377fbe4eac7b4dd1e452577d8eedea5e207be2be6c2aeb0e90cf4eb. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7f054157e2673745662b1c45d22f99de1a01232f0420fd85b7b7f7c2b095d969.
Původní balíčky: BI-DBS
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1644910440738

Karty Anki: 1644910440739
GUID: qOmFvx%eeH; štítky: bi-dbs::p01 bi-spol::05.

### Otázka (Front)

Popište databázi.

### Odpověď (Back)

Databáze je soubor záznamů (zpráv), jako jsou znaky, čísla, diagramy, jejichž systematická struktura umožňuje, aby tyto zprávy mohly být vyhledávány pomocí počítače.

## Poznámka Anki 1644910503179

Karty Anki: 1644910503179
GUID: oW3T)m#cy$; štítky: bi-dbs::p01 bi-spol::05.

### Otázka (Front)

Popište databázový systém (DBS).

### Odpověď (Back)

Databázový systém (DBS) se skládá z:

- databáze (DB),
- database management system (DBMS).

## Poznámka Anki 1644910724329

Karty Anki: 1644910724330
GUID: s7%q[HW^8h; štítky: bi-dbs::p01 bi-spol::05.

### Otázka (Front)

Popište vlastnosti databázové technologie.

### Odpověď (Back)

Databázová technologie se zabývá řízením **velkého množství**, **perzistentních**, **spolehlivých** a **sdílených **dat. Přičemž jednotlivá slovní spojení znamenají:

- „**velkého množství**“ - pro data nestačí operační paměť;
- „**perzistentních**“ - data přetrvávají od zpracování ke zpracování;
- „**spolehlivých**“ - data lze rekonstruovat po chybě;
- „**sdílených**“ - data jsou přístupná více uživatelům.

## Poznámka Anki 1644911076957

Karty Anki: 1644911076957
GUID: Qe%R&V=Q9B; štítky: bi-dbs::p01 bi-spol::05.

### Otázka (Front)

Popište Structured Query Language (SQL) a rozdělení jeho příkazů.

### Odpověď (Back)

Structured Query Language (SQL) je jazyk vyšší úrovně používaný pro dotazování databází. Na místo způsobu provedení dotazu specifikuje pouze požadované výsledky. Některé jeho části byly inspirovány relační algebrou a na rozdíl od ní je standardizován. Jeho příkazy se dělí do následujících skupin:

- Data Definition Language (DDL),
- Data Manipulation Language (DML),
- Transaction Control Language (TCL),
- Data Control Language (DCL).

## Poznámka Anki 1716470848732

Karty Anki: 1716470848732
GUID: hbqct|R~8G; štítky: bi-dbs::p01 bi-spol::05.

### Otázka (Front)

Popište Data Definition Language (DDL).

### Odpověď (Back)

Data Definition Language (DDL) je skupina příkazů Structured Query Language (SQL), která slouží pro vytváření a úpravu databázových objektů, jako jsou tabulky, pohledy a integritní omezení. Typickými příkazy DDL jsou \(\texttt{CREATE}\), \(\texttt{ALTER}\) nebo \(\texttt{DROP}\), např.
\[\texttt{CREATE TABLE teachers (id int, name varchar(255));}.\]

## Poznámka Anki 1716471044171

Karty Anki: 1716471044171
GUID: O*57:=a:K&; štítky: bi-dbs::p01 bi-spol::05.

### Otázka (Front)

Popište Data Manipulation Language (DML).

### Odpověď (Back)

Data Manipulation Language (DML) je skupina příkazů Structured Query Language (SQL), která slouží pro dotazování a úpravu dat. Typickými příkazy DML jsou \(\mathtt{SELECT}\), \(\mathtt{INSERT}\) nebo \(\mathtt{UPDATE}\) např.
\[\texttt{SELECT name FROM teachers WHERE id = 1;}.\]

## Poznámka Anki 1716471272885

Karty Anki: 1716471272885
GUID: GP(z6YJHGQ; štítky: bi-dbs::p01 bi-spol::05.

### Otázka (Front)

Popište Transaction Control Language (TCL).

### Odpověď (Back)

Transaction Control Language (TCL) je skupina příkazů Structured Query Language (SQL), která slouží pro řízení transakcí. Typickými příkazy TCL jsou \(\texttt{COMMIT}\), \(\mathtt{ROLLBACK}\) a \(\mathtt{SAVEPOINT}\).

## Poznámka Anki 1716471550215

Karty Anki: 1716471550215
GUID: ns/f(^s[HN; štítky: bi-dbs::p01 bi-spol::05.

### Otázka (Front)

Popište Data Control Language (DCL).

### Odpověď (Back)

Data Control Language (DCL) je skupina příkazů Structured Query Language (SQL), která slouží pro řízení přístupových práv. Typickými příkazy DCL jsou \(\mathtt{GRANT}\), \(\texttt{REVOKE}\) a \(\mathtt{ROLE}\) např.
\[\texttt{GRANT INSERT,UPDATE ON teachers TO 'user';}.\]

## Poznámka Anki 1716472883485

Karty Anki: 1716472883485
GUID: J(;7r[dv61; štítky: bi-dbs::p01 bi-spol::05.

Metadata původního zdroje pro kartu 1716472883485: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte relaci a schéma relace.

### Odpověď (Back)

Mějme \(n \in \mathbb N\) a \(i \in \hat n\). Relace \(R\) je množina \(n\)-tic tvaru \[(a_1, a_2, \dots, a_n) \in D_1 \times D_2 \times \dots \times D_n,\]kde \(a_i\) nazýváme hodnotami atributu a \(D_i\) doménami atributu. Schéma relace zapisujeme
\[R(A_1 : D_1, A_2 : D_2, \dots, A_n : D_n),\]kde \(R\) je jméno relace a \(A_i\) jsou jména atributů. Zápis schématu relace můžeme zkrátit na \(R(A)\).

## Poznámka Anki 1716472993613

Karty Anki: 1716472993613
GUID: Dv|L(Xk!H#; štítky: bi-dbs::p01 bi-spol::05.

Metadata původního zdroje pro kartu 1716472993613: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište základní paradigma databázových systémů (DBS).

### Odpověď (Back)

Základním paradigmatem databázových systémů (DBS) je, že existence dat v databázi je nezávislá na aplikačních programech.

