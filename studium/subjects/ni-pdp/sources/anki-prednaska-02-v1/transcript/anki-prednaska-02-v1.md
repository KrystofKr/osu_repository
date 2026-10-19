# NI-PDP – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-pdp/NI-PDP.apkg; APKG SHA-256 b38783778a590460b03050d14b21f60017ff90d9b0abe806748521d92454df28. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: da16e1b818a2fcaa42e78195ece6396a24afd5754b63362dce0d5df6925e0f3f.
Původní balíčky: NI-PDP
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1740495235418

Karty Anki: 1740495235418
GUID: fLo/hz;7Nb; štítky: ni-pdp::p02.

### Otázka (Front)

Popište progamový model OpenMP a paralelní oblasti.

### Odpověď (Back)

**Programový model OpenMP **stojí na programovací šabloně fork-join. Program vytvořený pomocí OpenMP je tedy zprvu prováděn sekvenčně počáteční vláknem, které postupně vytváří tým paralelních vláken. Místa v kódu, ve kterých dochází k vytvoření paralelních vláken, jsou explicitně označena a nazývají se **paralelní oblasti** (parallel regions). Mimo ně běží pouze počáteční vlákno a program je prováděn sekvenčně.

 [Obrázek: Screenshot 2025-02-25 155118-f65a3b9f690cc2dcdc18f5bad0a16e7016ce7c4f.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1740496732602

Karty Anki: 1740496732602
GUID: c#4@CmYU=`; štítky: ni-pdp::p02.

### Otázka (Front)

Popište vlastnosti proměnných v paralelních oblastech OpenMP.

### Odpověď (Back)

Vlastnosti proměnných v paralelních oblastech OpenMP se definují pomocí následujících klauzulí:

- \(\texttt{shared}\) - všechna vlákna sdílí stejnou instanci proměnné, programátor musí zajistit správný paralelní přístup;

- \(\texttt{private}\) - každé vlákno má vlastní instanci proměnné, její počáteční hodnota není definovaná a po opuštění paralelní oblasti je obnovena její původní hodnota;

- \(\texttt{firstprivate}\) - \(\texttt{private}\) proměnná jejíž instance jsou inicializovány hodnotou, kterou měla před vstupem do paralelní oblasti;

- \(\texttt{reduction}\) - každé vlákno má vlastní instanci proměnné inicializovanou na nulu, při opouštění paralelní oblasti jsou veškeré instance zkombinovány s původní hodnotou pomocí daného operátoru a zapsány do původní proměnné;
- \(\texttt{threadprivate}\) - \(\texttt{private}\) proměnná s životností napříč všemi paralelními oblastmi.

Dále existuje klauzule \(\texttt{default}\), která umožňuje specifikovat vlastnost všech proměnných, jejichž vlasnosti nebyly explicitně uvedeny. Podobně jako v běžných programovacích jazycích se vlastnosti ukazatelů aplikují pouze na ně jako takové, nikoliv na odkazované proměnné.

## Poznámka Anki 1740497131621

Karty Anki: 1740497131622
GUID: Lod;slO*+%; štítky: ni-pdp::p02.

### Otázka (Front)

Popište OpenMP direktivu \(\texttt{parallel}\).

### Odpověď (Back)

OpenMP direktiva \(\texttt{parallel}\) se používá pro vytváření paralelních oblastí. Vlákno, které na direktivu narazí se stává master vláknem a je mu přiřazen identifikátor 0. Na konci každé paralelní oblasti je umístěna implicitní bariéra. Vlákna, která dosáhnou konce paralelní oblasti nejsou typicky ničena, ale odkládána do thread poolu a později recyklována.

## Poznámka Anki 1740498679241

Karty Anki: 1740498679241
GUID: s%s]e%))x@; štítky: ni-pdp::p02.

### Otázka (Front)

Popište OpenMP direktivu \(\texttt{for}\).

### Odpověď (Back)

OpenMP direktiva \(\texttt{for}\) implementuje datový (iterační) paralelismus. Podobně jako v direktivě \(\texttt{parallel}\) je i zde na konci cyklu umístěna implicitní bariéra. Mezi časté klauzule direktivy \(\texttt{for}\) patří:

- \(\texttt{schedule}\) - strategie přiřazení iterací cyklu vláknům,

- \(\texttt{collapse}\) - počet úrovní víceúrovňového cyklu, které má být spojeno do jednoho iterátoru;

- \(\texttt{ordered}\) - specifikuje, že iterace musí být vykonány v sekvenčním pořadí;

- \(\texttt{nowait}\) - specifikuje, ža vlákna nemusí čekat na bariéře.

Direktiva \(\texttt{for}\) navíc definuje klauzuli \(\texttt{lastpriate}\) pro vlastnosti proměnných, která specifikuje, že po opuštění paralelní oblasti je do proměnné uložena hodnota vypočtená v syntakticky poslední iteraci cyklu.

## Poznámka Anki 1740499163443

Karty Anki: 1740499163443
GUID: mFXguYa%se; štítky: ni-pdp::p02.

### Otázka (Front)

Popište typy klauzule \(\texttt{schedule}\) v OpenMP direktivě \(\texttt{for}\).

### Odpověď (Back)

Klauzule \(\texttt{schedule}\) v OpenMP direktivě \(\texttt{schedule}\) může být následujících typů:

- \(\texttt{static}\) - vláknu je přidělen chunk po sobě jdoucích iterací cyklu specifikované velikosti (implicitně \(\frac n p\)) a všechny iterace jsou přiděleny ihned;

- \(\texttt{dynamic}\) - vláknu je přidělen chunk po sobě jdoucích iterací cyklu specifikované velikosti (implicitně 1) a pokud tím nejsou přiděleny všechny iterace, jsou postupně další chunky přidělovány vláknům, které skončily výpočet;

- \(\texttt{guided}\) - vláknu je přidělen chunk stejným způsobem jako v \(\texttt{dynamic}\) velikosti \(x\), kde\[x = \max \Big( \frac {\text{remaining iterations}}{p}, \text{size} \Big)\]a implicitně je \(\text{size}\) bráno jako 1;

- \(\texttt{runtime}\) - strategie je zvolena za běhu podle systémových proměnných;

- \(\texttt{auto}\) - strategie je zvolena kompilátorem nebo béhovým prostředím.

## Poznámka Anki 1740501941724

Karty Anki: 1740501941725
GUID: M[)80DryM;; štítky: ni-pdp::p02.

### Otázka (Front)

Popište OpenMP direktivu \(\texttt{task}\).

### Odpověď (Back)

OpenMP direktiva \(\texttt{task}\) implementuje funkční paralelismus (task parallelism). Používá se zejména pro paralelní provádění algoritmů typu divide-and-conquer a mechanismus přidělování úloh vláknům je postaven na principu producent-konzument s tím, že každé vlákno může být současně producentem i konzumentem. Úloha se v OpenMP skládá z:

- ukazatele na začátek kódu,
- vstupních dat,
- datové struktury, do které konzumentské vlákno provádějící úlohu vloží svůj identifikátor.

Mezi časté klauzule direktivy \(\texttt{task}\) patří:

- \(\texttt{if}\) - podmínka, která musí být splněna pro vytvoření úlohy, v opačném případě je úloha provedena sekvenčně;

- \(\texttt{final}\) - udává podmínku a pokud je platná, nebude daná úloha generovat další úlohy;

- \(\texttt{priority}\) - přiřadí úloze prioritu.

## Poznámka Anki 1740502620189

Karty Anki: 1740502620189
GUID: tv|K&E5#38; štítky: ni-pdp::p02.

### Otázka (Front)

Popište synchornizační direktivy OpenMP.

### Odpověď (Back)

Mezi synchorizační direktivy OpenMP patří:

- \(\texttt{barrier}\) - všechna vlákna z týmu musejí počat na poslední příchozí vlákno,

- \(\texttt{master}\) - blok kódu provede pouze master vlákno a ostatní vlákna jej přeskočí,

- \(\texttt{single}\) - blok kódu provede jedno libovolné vlákno a ostatní vlákna čekají na jeho dokončení,

- \(\texttt{critical}\) - blok kódu smí být v každém časovém okamžiku prováděn pouze jedním vláknem (kritická sekce),

- \(\texttt{atomic}\) - atomická operace nad proměnnou,

- \(\texttt{flush}\) - uložení aktuálních hodnot sdílených proměnných do sdílené paměti,

- \(\texttt{taskwait}\) - čekání rodičovské úlohy na dokončení všech potomků.

## Poznámka Anki 1740503276425

Karty Anki: 1740503276425
GUID: QP24+gjHC!; štítky: ni-pdp::p02.

### Otázka (Front)

Popište OpenMP direktivu \(\texttt{atomic}\).

### Odpověď (Back)

OpenMP direktiva \(\texttt{atomic}\) je synchronizační direktiva, která se používá pro zajištění atomicity operací nad skalární proměnnou. Lze ji aplikovat v následujících podobách:

- \(\texttt{read}\) - čtení;
- \(\texttt{write}\) - zápis;
- \(\texttt{update}\) - čtení, modifikace a zápis;
- \(\texttt{capture}\) - čtení, modifikace, zápis a získání hodnoty před nebo po provedení modifikace.

### Doplňující pole (Extra)

Varianty \(\texttt{read}\) a \(\texttt{update}\) se používají z toho důvodu, že na některých architekturách nejsou operace čtení a zápisu paměti atomické operace.

