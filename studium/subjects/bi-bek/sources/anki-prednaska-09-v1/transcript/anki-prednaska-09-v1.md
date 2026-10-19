# BI-BEK – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1682520303971

Karty Anki: 1682520303971
GUID: K_%[N)IGx7; štítky: bi-bek::p09.

Metadata původního zdroje pro kartu 1682520303971: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište SQL injection.

### Odpověď (Back)

SQL injection je typ injection útoku, který spočívá v tom, že útočník do aplikace vloží škodlivé SQL dotazy skrze uživatelský vstup, které jsou následně vykonány na databázovém serveru aplikace v důsledku nedostatečné validace vstupů. Tento útok lze mitigovat následujícími metodami:

- princip nejmenších oprávnění (principle of least privilege);
- validace vstupů;
- escapování znaků, které mohou narušit formu SQL příkazu;
- parametrizované výrazy;
- specializované nástroje (\(\texttt{sqlmap}\), aplikační firewall).

## Poznámka Anki 1682521790692

Karty Anki: 1682521790693
GUID: N$],2sYgf/; štítky: bi-bek::p09 bi-ib::10 bi-ib::16.

### Otázka (Front)

Popište parametrizovaný SQL výraz.

### Odpověď (Back)

Parametrizovaný SQL výraz je výraz, který má na místě jednoho nebo více parametrů nevyplněné hodnoty (placeholdery). Jejich vyplnění je ponecháno na databázovém systému, čímž je odstraněno riziko, že by hodnoty mohly být interpretovány jako součást SQL výrazu.

## Poznámka Anki 1717683894767

Karty Anki: 1717683894767
GUID: sEaz&SfuN|; štítky: bi-bek::p09 bi-ib::10 bi-ib::16.

### Otázka (Front)

Popište způsoby aplikace principu nejmenších oprávnění (principle of least privilege) v databázích.

### Odpověď (Back)

Databáze podporují aplikaci principu nejmenších oprávnění (principle of least privilege) v následujících podobách:

- **pohledy** (views) - odstínění dostupných dat;

- **procedury** (procedures) - citlivá operace je prováděna procedurou a uživatel má pouze právo ji spustit;
- **Data Control Language **(DCL) - omezení oprávnění uživatelů, pohledů nebo procedur.

## Poznámka Anki 1717684560669

Karty Anki: 1717684560669
GUID: zO=8s8tey~; štítky: bi-bek::p09 bi-ib::10 bi-ib::16.

### Otázka (Front)

Popište blind SQL injection.

### Odpověď (Back)

Blind SQL injection je typ SQL injection, kdy je sice aplikace zranitelná, ale její odpovědi neobsahují výsledek dotazu. Zneužití blind SQL injection pak lze postavit např. na časové odezvě aplikace, chybových hláškách nebo out-of-band interakcích.

