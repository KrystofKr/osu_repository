# BI-BEK – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1681310174964

Karty Anki: 1681310174964
GUID: lWhxbH$V$4; štítky: bi-bek::p07 bi-ib::09.

### Otázka (Front)

Popište důvody, proč mohou aplikace vyžadovat zvýšená oprávnění a jejich řešení.

### Odpověď (Back)

Aplikace mohou vyžadovat zvýšená oprávnění zaprvé **kvůli ACL**:

- zápis do umístění, kam smí zapisovat pouze administrátor;
- otevírání prostředků s úrovní přístupu \(\texttt{GENERIC_ALL}\);
- zápis do registrového stromu \(\texttt{HKEY_LOCAL_MACHINE}\).

Tyto problémy lze vyřešit:

- ukládáním dat do umístění, kam může aplikace zapsat;
- otevíráním prostředků s minimální úrovní přístupu;
- rozvolněním ACL.

Dalším důvodem mohou být **problémy s oprávněními**. V takovém případě se doporučuje přidat uživatele do skupiny s požadovaným oprávněním. Posledním důvodem může být **přístup k LSA secrets**, které však lze často nahradit pomocí Data Protection API (DPAPI).

## Poznámka Anki 1681310232211

Karty Anki: 1681310232211
GUID: hf`Y>a`A:w; štítky: bi-bek::p07 bi-ib::09.

### Otázka (Front)

Co je to Local Security Authority (LSA)?

### Odpověď (Back)

Local Security Authority (LSA) je bezpečnostní prvek Windows systémů. Má na starosti správu a vymáhání bezpečnostních zásad, autentizaci uživatelů, auditování a poskytuje API pro přístup k LSA Secrets.

## Poznámka Anki 1681311922558

Karty Anki: 1681311922558
GUID: I5|w^`s5yj; štítky: bi-bek::p07 bi-ib::09.

### Otázka (Front)

Popište proces zjištění minimálních práv.

### Odpověď (Back)

Proces zjištění minimálních práv je následující:

- Zjištění všech prostředků (SO), které aplikace používá.
- Zjištění všech privilegovaných API, které aplikace používá.
- Posouzení uživatelského účtu, pod kterým má aplikace běžet.
- Zjištění všech SID, které jsou v tokenu.
- Určení všech SID, které jsou pro aplikaci nezbytné.
- Změna tokenu aplikace tak, aby vyhovoval předešlým krokům.

## Poznámka Anki 1681313132770

Karty Anki: 1681313132770
GUID: IRBE}mMp:{; štítky: bi-bek::p07 bi-ib::09 bi-ib::25.

### Otázka (Front)

Co je to User Account Control (UAC)?

### Odpověď (Back)

User Account Control je bezpečnostní prvek Windows systémů, který omezuje oprávnění běžících aplikací na úroveň uživatele, dokud administrátor nepotvrdí zvýšení práv. Snaží se zpětně kompatibilním způsobem eliminovat hrozby plynoucí z toho, že uživatelé jsou zvyklí pracovat pod administrátorským účtem.

## Poznámka Anki 1681313319564

Karty Anki: 1681313319564
GUID: Lt%2qHa!Ub; štítky: bi-bek::p07 bi-ib::09 bi-ib::25.

### Otázka (Front)

Z jakých komponent sestává User Account Control?

### Odpověď (Back)

UAC sestává z následujících komponent:

- **Application Information Service** - zajišťuje spouštení aplikací s dalšími právy,

- \(\mathtt{consent\text.exe}\) - prezentuje uživateli okno UAC a výsledky poskytuje AIS,
- **virtualizační ovladač** - provádí virtualizaci pro aplikace nekompatibilní s UAC.

## Poznámka Anki 1681314055823

Karty Anki: 1681314055823
GUID: cH@|7)01qz; štítky: bi-bek::p07 bi-ib::09 bi-ib::25.

### Otázka (Front)

Popište User Interface Privilege Isolation (UIPI)?

### Odpověď (Back)

User Interface Privilege Isolation (UIPI) je bezpečnostní prvek Windows systémů, který každému procesu přiřazuje integrity level. Následně zamezuje procesům s nižší hodnotou integrity level ovlivňovat procesy s vyšší hodnotou integrity level.

## Poznámka Anki 1717617949963

Karty Anki: 1717617949963
GUID: gT$MCSj9^]; štítky: bi-bek::p07 bi-ib::09 bi-ib::25.

### Otázka (Front)

Popište Linux capabilities.

### Odpověď (Back)

Capabilities jsou bezpečnostní komponenta Linuxových systémů. Jejich účlem je rozdělit monolitická privilegia uživatele \(\texttt{root}\) na menší části, které lze selektivně vypínat a zapínat. Dělí se do tří základních skupin:

- **permitted** - capabilities, které vlákno může získat;

- **inheritable** - capabilities děděné do permitted capabilities spouštěných vláken;

- **effective **- capabilities používané pro testování autorizace kernelem.

