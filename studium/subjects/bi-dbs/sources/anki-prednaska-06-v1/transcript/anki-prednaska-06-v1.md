# BI-DBS – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-dbs/BI-DBS.apkg; APKG SHA-256 2adef415f377fbe4eac7b4dd1e452577d8eedea5e207be2be6c2aeb0e90cf4eb. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7f054157e2673745662b1c45d22f99de1a01232f0420fd85b7b7f7c2b095d969.
Původní balíčky: BI-DBS
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1718384237426

Karty Anki: 1718384237426
GUID: m1P?npy=n*; štítky: bi-dbs::p06 bi-spol::09.

### Otázka (Front)

Popište základní syntaxi příkazu \(\texttt{SELECT}\) v Structured Query Language (SQL).

### Odpověď (Back)

Základní syntaxe příkazu \(\texttt{SELECT}\) je:
\[\begin{matrix}
\texttt{SELECT} \text{ columns}\\
\texttt{FROM} \text{ source}\\
\texttt{[WHERE} \text{ condition} \texttt ]\\
\texttt{[ORDER BY} \text{ ordering} \texttt {];}
\end{matrix}\]kde:

- \(\texttt{SELECT}\) určuje sloupce výstupu;

- \(\texttt{FROM}\) určuje zdrojovu tabulku, pohled nebo dotaz;
- \(\texttt{WHERE}\) klade podmínku na \(n\)-tice výstupu a může obsahovat porovnávací, Booleovské a další (např. \(\texttt{BETWEEN}\), \(\texttt{LIKE}\), \(\texttt{IN}\)) operátory;

- \(\texttt{ORDER BY}\) určuje řazení výstupu.

Tedy na příklad:

\[\begin{matrix}
\texttt{SELECT} \text{ *}\\
\texttt{FROM} \text{ films}\\
\texttt{WHERE} \text{ year} \geq 2000 \texttt{ AND } \texttt{year} \leq 2020 \\
\texttt{ORDER BY} \text{ name } \texttt {ASC;}
\end{matrix}\]

## Poznámka Anki 1718385550300

Karty Anki: 1718385550300
GUID: mlPH)Hy6P|; štítky: bi-dbs::p06 bi-spol::09.

### Otázka (Front)

Popište spojení v Structured Query Language (SQL).

### Odpověď (Back)

Structured Query Language (SQL) umožňuje následující typy spojení:

- \(\texttt{NATURAL JOIN}\) (**přirozené**) - výsledkem je množina kombinací  \(n\)-tic shodujících se ve společném atributu

\[\dots \texttt{FROM } T_1 \texttt{ NATURAL JOIN } T_2 \texttt ; \]

- \(\texttt{INNER JOIN}\) (**vnitřní**) - výsledkem je množina kombinací  \(n\)-tic spojených na základě podmínky

\[\dots \texttt{FROM } T_1 \texttt{ [INNER] JOIN } T_2 \texttt{ ON (} T_1.a < T_2.b \texttt{);}\]

- \(\texttt{OUTER JOIN}\) (**vnější**) - výsledkem je množina kombinací \(n\)-tic spojených na základě podmínky, která navíc obsahuje i \(n\)-tice z levé, pravé nebo obou tabulek, které nejsou spojitelné s žádnou \(n\)-ticí z protější tabulky

\[\dots \texttt{FROM } T_1 \texttt{ LEFT/RIGHT/FULL [OUTER] JOIN } T_2 \texttt{ ON (} T_1.a < T_2.b \texttt{);}\]

- \(\texttt{CROSS JOIN}\) (**kartézský součin**) - výsledkem je množina všech kombinací \(n\)-tic obou tabulek

\[\begin{matrix}
\dots \texttt{FROM } T_1 \texttt{ CROSS JOIN } T_2 \texttt ;\\
\dots \texttt{FROM } T_1, T_2 \texttt ;
\end{matrix}\]V případě, že ve spojení používáme podmínku rovnosti, může být tato podmínka nahrazena klíčovým slovem \(\texttt{USING}\), na příklad:

\[\dots \texttt{FROM } T_1 \texttt{ [INNER] JOIN } T_2 \texttt{ USING } \texttt( \text{name} \texttt{);}\]

## Poznámka Anki 1718388440255

Karty Anki: 1718388440255
GUID: HD-$xYIwHg; štítky: bi-dbs::p06 bi-spol::09.

### Otázka (Front)

Popište agregační funkce a klauzule \(\texttt{HAVING}\) a \(\texttt{GROUP BY}\) v Structured Query Language (SQL).

### Odpověď (Back)

**Agregační funkce** umožňují dále zpracovávat sloupce klauzule \(\texttt{SELECT}\). Mezi příklady agregačních funkcí patří \(\texttt{AVG}\), \(\texttt{COUNT}\) nebo \(\texttt{SUM}\). **Klauzule **\(\texttt{GROUP BY}\) seskupuje \(n\)-tice na základě společné hodnoty atributu a **klauzule **\(\texttt{HAVING}\) na seskupené a případně agregované \(n\)-tice aplikuje podmínku. Na příklad
\[\begin{matrix}
\texttt{SELECT} \text{ film}, \texttt{COUNT(} \text{actor} \texttt )\\
\texttt{FROM} \text{ films}\\
\texttt{GROUP BY} \text{ film}\\
\texttt{HAVING COUNT(} \text{actor} \texttt ) > 2 \texttt;
\end{matrix}\]zobrazí jména filmů a počty jejich herců, pokud mají více než dva.

## Poznámka Anki 1718540552561

Karty Anki: 1718540552561
GUID: sNx^eV~bKx; štítky: bi-dbs::p06 bi-spol::05.

Metadata původního zdroje pro kartu 1718540552561: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište pořadí vyhodnocování příkazu \(\texttt{SELECT}\) s klauzulemi \(\texttt{WHERE}\), \(\texttt{GROUP BY}\), \(\texttt{HAVING}\) a \(\texttt{ORDER BY}\) a agregační funkcí v Structured Query Language (SQL).

### Odpověď (Back)

Příkaz \(\texttt{SELECT}\) s klauzulemi \(\texttt{WHERE}\), \(\texttt{GROUP BY}\), \(\texttt{HAVING}\) a \(\texttt{ORDER BY}\) a agregační funkcí se vyhodnocuje v následujícím pořadí:

- klauzule \(\texttt{FROM}\),
- klauzule \(\texttt{WHERE}\),
- klauzule \(\texttt{GROUP BY}\),

- klauzule \(\texttt{SELECT}\) společně s agregační funkcí,
- klauzule \(\texttt{HAVING}\),
- klauzule \(\texttt{ORDER BY}\).

