# BI-BEK – Cvičení 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 2 poznámek, 2 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1717600472811

Karty Anki: 1717600472811
GUID: Kp0&}wI^7g; štítky: bi-bek::c02 bi-ib::08.

### Otázka (Front)

Popište DLL hijacking.

### Odpověď (Back)

DLL hijacking je útok na operační systém Windows. Pokud aplikace nespecifikuje přesnou cestu načítaného DLL, bude se jej Windows snažit dohledat na základě definovaných pravidel, jejichž součástí je i procházení několika adresářů. Pokud útočník smí do některého z těchto adresářů zapisovat, může do něj vložit škodlivou verzi hledaného DLL. V případě, že se škodlivé DLL nachází v prohledávaném pořadí adresářů dříve než legitimní DLL, dojde k jeho načtení do programu a spuštění útočníkova kódu. Mezi tyto adresáře patří:

- složka, ze které byla aplikace spuštěna;
- \(\texttt{C:\Windows\System32}\);

- \(\texttt{C:\Windows\System}\);

- \(\texttt{C:\Windows} \);
- aktuální pracovní adresář,
- složky v proměnné \(\texttt{PATH}\).

## Poznámka Anki 1717600711509

Karty Anki: 1717600711509
GUID: z;h@C3D/pm; štítky: bi-bek::c02 bi-ib::08.

### Otázka (Front)

Popište indirect DLL hijacking.

### Odpověď (Back)

Indirect DLL hijacking je typ DLL hijackingu. Stojí na stejném principu, ale v tomto případě proces hledání DLL neiniciuje program jako takový, ale některá z jeho závislostí (např. knihovna).

