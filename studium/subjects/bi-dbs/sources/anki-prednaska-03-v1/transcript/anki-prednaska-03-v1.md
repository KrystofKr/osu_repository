# BI-DBS – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-dbs/BI-DBS.apkg; APKG SHA-256 2adef415f377fbe4eac7b4dd1e452577d8eedea5e207be2be6c2aeb0e90cf4eb. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7f054157e2673745662b1c45d22f99de1a01232f0420fd85b7b7f7c2b095d969.
Původní balíčky: BI-DBS
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1646073860619

Karty Anki: 1646073860619
GUID: c-eW6G1nku; štítky: bi-dbs::p03 bi-spol::05.

Metadata původního zdroje pro kartu 1646073860619: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište podobnosti a odlišnosti tabulek a relací.

### Odpověď (Back)

Tabulky a relace si jsou podobné 1:1 v následujích aspektech:

| 
      **tabulky** | 
      **relace** | 

| 
      schéma | 
      záhlaví | 

| 
      atribut | sloupec | 

| 
      jméno atributu | 
      jméno sloupce | 

| 
      \(n\)-tice
 | 
      řádek | 

Liší se však v následujících bodech:

- v relacích nezáleží na pořadí \(n\)-tic,
- relace neobsahují duplicitní \(n\)-tice.

## Poznámka Anki 1646073946842

Karty Anki: 1646073946842
GUID: f5ELC+7QEx; štítky: bi-dbs::p03 bi-spol::05.

### Otázka (Front)

Definujte schéma relační databáze.

### Odpověď (Back)

Schéma relační databáze je dvojice \((R, I)\), kde

- \(R = \{R_1, R_2, \dots, R_n\}\) je množina relací,

- \(I\) je množina integritních omezení.

## Poznámka Anki 1646074049858

Karty Anki: 1646074049858
GUID: yunqQBt,oT; štítky: bi-dbs::p03 bi-spol::05.

Metadata původního zdroje pro kartu 1646074049858: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte přípustnou relační databázi.

### Odpověď (Back)

Relační databázi se schématem \((R, I)\) nazveme přípustnou, právě když \(n\)-tice jejích relací \(\{ R_1, R_2, \dots, R_n \}\) vyhovují integritním omezením z \(I\).

## Poznámka Anki 1646074160584

Karty Anki: 1646074160584
GUID: IEdYF*Z9qh; štítky: bi-dbs::p03 bi-spol::05.

### Otázka (Front)

Definujte klíč schématu.

### Odpověď (Back)

Klíč \(K\) schématu \(R(A)\) je taková minimální podmnožina atributů z \(A\), která jednoznačně určí každou \(n\)-tici relace \(R\).

## Poznámka Anki 1646074227358

Karty Anki: 1646074227358
GUID: d$kB%/.b|J; štítky: bi-dbs::p03 bi-spol::05.

Metadata původního zdroje pro kartu 1646074227358: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte minimalitu klíče.

### Odpověď (Back)

Neexistuje takové \(K' \subset K\), které jednoznačně určuje každou \(n\)-tici \(R(A)\).

## Poznámka Anki 1646074360884

Karty Anki: 1646074360885
GUID: E:n&F&{M:~; štítky: bi-dbs::p03 bi-spol::05.

Metadata původního zdroje pro kartu 1646074360885: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte databázový dotaz, jeho definiční obor a obor hodnot.

### Odpověď (Back)

Databázový dotaz nad schématem \(S\) je výraz, který vrací odpověď se schématem \(T\), přičemž:

- definičním oborem jsou všechna úložiště se schématem \(S\),
- oborem hodnot jsou všechny relace se schématem \(T\),
- data v odpovědi pocházejí z databáze,
- odpověď nezávisí na fyzickém uložení dat.

## Poznámka Anki 1646074389658

Karty Anki: 1646074389659
GUID: x+*Z{SEiSv; štítky: bi-dbs::p03 bi-spol::05.

Metadata původního zdroje pro kartu 1646074389659: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte dotazovací jazyk.

### Odpověď (Back)

Dotazovací jazyk je množina všech použitelných výrazů pro konstrukci dotazu.

## Poznámka Anki 1646074617633

Karty Anki: 1646074617633
GUID: Cws7>]qw~Q; štítky: bi-dbs::p03 bi-spol::05.

### Otázka (Front)

Popište selekci v relační algebře.

### Odpověď (Back)

Selekce je operace relační algebry, která omezuje výslednou relaci na \(n\)-tice splňující danou podmínku, např.
\[\texttt{teachers}(\texttt{id}=\texttt{1}).\]

## Poznámka Anki 1646074755963

Karty Anki: 1646074755964
GUID: u%DOHAZL3V; štítky: bi-dbs::p03 bi-spol::05.

### Otázka (Front)

Popište projekci a přejmenování v relační algebře.

### Odpověď (Back)

**Projekce** je operace relační algebry, která omezuje atributy \(n\)-tic výsledné relace na dané atributy, např.
\[\texttt{teachers}[\texttt{id}, \texttt{name}].\]Projekci lze kombinovat s **přejmenováním**, které umožňuje změnit název atributu ve výsledné relaci, např.
\[\texttt{teachers}[\texttt{id}, \texttt{name} \to \texttt{jmeno}].\]

## Poznámka Anki 1716475109414

Karty Anki: 1716475109414
GUID: z::ZCuTv=/; štítky: bi-dbs::p03 bi-spol::05.

### Otázka (Front)

Popište relační algebru a operace, které poskytuje.

### Odpověď (Back)

Relační algebra je jazyk vyšší úrovně používaný pro dotazování databází. Namísto způsobu provedení dotazu specifikuje pouze požadované výsledky. Byla vzorem při návrhu příkazu \(\mathtt{SELECT}\) ve Structured Query Language (SQL), který na rozdíl od relační algebry umožňuje i vytváření nových objektů databáze (DDL) a jejich úpravu (DML). Relační algebra poskytuje následující operace:

- selekce, projekce a přejmenování;
- množinové operace;
- spojení (přirozené, obecné, anti-join);
- relační dělení.

## Poznámka Anki 1716476396548

Karty Anki: 1716476396548
GUID: P0RvY)>>cP; štítky: bi-dbs::p03 bi-spol::05.

### Otázka (Front)

Popište spojení v relační algebře.

### Odpověď (Back)

Relační algebra umožňuje následující typy spojení:

- **přirozené **- výsledkem je množina kombinací \(n\)-tic shodujících se ve společném atributu\[R_1 * R_2\]

- **obecné** (\(\Theta\)) - výsledkem je množina kombinací \(n\)-tic spojených na základě podmínky

\[R_1 [R_1.a < R_2.b] R_2,\]Dále lze libovolný typ spojení zkombinovat s projekcí, čímž vzniká **levé **nebo **pravé** spojení, např.

\[\begin{matrix}
R_1 < \kern-0.3em * \kern0.4em R_2,\\
R_1[R_1.a < R_2.b \kern-0.2em > \kern-0.2em R_2.
\end{matrix}\]Speciálním případem spojení je **anti-join**, jehož výsledkem je množina všech \(n\)-tic z jedné relace, které nejsou spojitelné s žádnou \(n\)-ticí z druhé relace

\[\begin{matrix}
R_1 \overline{< \kern-0.3em *} R_2,\\
R_1 \overline{* \kern-0.3em >} R_2.
\end{matrix}\]

## Poznámka Anki 1716476680994

Karty Anki: 1716476680994
GUID: c6F1+:f,4); štítky: bi-dbs::p03 bi-spol::05.

### Otázka (Front)

Popište relační dělení v relační algebře.

### Odpověď (Back)

Relační dělení je operace relační algebry, jejímž výsledkem je množina všech \(n\)-tic z první relace, které jsou spojitelné s každou \(n\)-ticí druhé relace
\[R_1 \div R_2.\]

## Poznámka Anki 1716478457124

Karty Anki: 1716478457124
GUID: q>00.5vq=L; štítky: bi-dbs::p03 bi-spol::05.

### Otázka (Front)

Popište integritní omezení.

### Odpověď (Back)

Integritní omezení jsou pravidla omezující procesy v databázi (např. vkládání a upravování) tak, aby byla zajištěna integrita a kvalita dat. Existují následující možnosti vyjádření a kontroly integritních omezení:

- **deklarativní** - stanoveny při vytvoření relace, automaticky kontrolované DBMS;

- **procedurální** - na straně klienta nebo serveru.

## Poznámka Anki 1716478982610

Karty Anki: 1716478982610
GUID: qr,iE.,?;[; štítky: bi-dbs::p03 bi-spol::05.

Metadata původního zdroje pro kartu 1716478982610: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište možnosti vyjádření integritních omezení pomocí Structured Query Language (SQL).

### Odpověď (Back)

Structured Query Language (SQL) umožňuje definovat integritní omezení pro sloupce i tabulky. Využívá k tomu specifikátory \(\texttt{NOT NULL}\), \(\texttt{DEFAULT}\), \(\texttt{UNIQUE}\), \(\texttt{PRIMARY KEY}\), \(\texttt{REFERENCES}\) a \(\texttt{CHECK}\), např.
\[\texttt{CREATE TABLE cars (name varchar(255) NOT NULL, CONSTRAINT CAR_PK PRIMARY_KEY (name));}\]SQL navíc umožňuje specifikovat čas provedení kontroly nebo ji dočasně vypnout.

