# BI-BEK – Přednáška 11

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1683126016980

Karty Anki: 1683126016980
GUID: B{#(0`?myj; štítky: bi-bek::p11 bi-ib::14.

### Otázka (Front)

Co je to nesprávné řízení přístupů (OWASP Top Ten)? Uveďte typické chyby.

### Odpověď (Back)

Aplikace by měla zajistit, že uživatelé nebudou moci provádět operace, ke kterým nemají oprávnění. Mezi typické chyby patří:

- nedodržení principu nejmenších oprávnění,
- nezabezpečené přímé odkazy na objekty,
- přístup k API z neautorizovaných míst.

## Poznámka Anki 1683126139252

Karty Anki: 1683126139252
GUID: f45]g~H#IY; štítky: bi-bek::p11 bi-ib::14.

### Otázka (Front)

Co je to selhání v kryptografii (OWASP Top Ten)? Uveďte typické chyby.

### Odpověď (Back)

Jedná se buď o nesprávné použití kryptografických technik, nebo přímo jejich absence. Týká se zejména dat, jejichž ochrana je dána legislativou (např. GDPR). Mezi typické chyby patří:

- přenos dat pomocí nezabezpečených protokolů (HTTP, FTP, SMTP),
- použití slabých kryptografických algoritmů,
- nesprávná kontrola ověřovacích informací.

## Poznámka Anki 1683126314827

Karty Anki: 1683126314827
GUID: GPbJh&d&So; štítky: bi-bek::p11 bi-ib::10 bi-ib::14 bi-ib::16.

### Otázka (Front)

Co je to injekce (OWASP Top Ten)? Uveďte běžné typy injekce na webu.

### Odpověď (Back)

Injekce je souhrnný název pro situace, kdy v důsledku nesprávného ošetření vstupu dojde k tomu, že uživatelský vstup, který by z principu měl být interpretován jako data, získá charakter spustitelného kódu. Mezi běžné typy injekcí na webu patří:

- SQL injection,
- file inclusion,
- cross-site scripting.

## Poznámka Anki 1683126523483

Karty Anki: 1683126523483
GUID: r{(3)%&7[2; štítky: bi-bek::p11 bi-ib::14.

### Otázka (Front)

Co je to nezabezpečený návrh (OWASP Top Ten)? Uveďte některá doporučení.

### Odpověď (Back)

Jde o souhrnou kategorii problémů vyplývajících z nedostatečného respektování principů bezpečného návrhu aplikací. Mezi základní doporučení patří:

- postupovat podle principů bezpečného vývoje,
- zahrnout bezpečnost do procesu návrhu,
- důkladně oddělovat vrstvy aplikace podle bezpečnostních charakteristik.

## Poznámka Anki 1683126832178

Karty Anki: 1683126832178
GUID: g4~>J6remg; štítky: bi-bek::p11 bi-ib::14 bi-ib::16.

### Otázka (Front)

Co je to nesprávná konfigurace (OWASP Top Ten)? Uveďte typické chyby.

### Odpověď (Back)

Jde o špatné nastavení aplikace, webového serveru, aplikačního serveru, knihovny, firewallu, OS nebo dalších. Mezi typické chyby patří:

- příliš detailní výpis chyby,
- nezabezpečené externí XML entity,
- použití výchozích uživatelů s výchozími hesly.

## Poznámka Anki 1683127328999

Karty Anki: 1683127328999
GUID: ITKW|}0w}b; štítky: bi-bek::p11 bi-ib::14.

### Otázka (Front)

Co jsou to zranitelné nebo zastaralé komponenty (OWASP Top Ten)?

### Odpověď (Back)

Jde o důsledek nečinnosti administrátora, který by měl sledovat databáze CVE, NVD a další, které popisují zranitelnosti produktů.

## Poznámka Anki 1683127677160

Karty Anki: 1683127677161
GUID: oHm)$+}lP_; štítky: bi-bek::p11 bi-ib::10 bi-ib::14 bi-ib::16.

### Otázka (Front)

Co jsou to chyby v identifikaci a autentizaci (OWASP Top Ten)? Co je to session hijacking a session fixation?

### Odpověď (Back)

Jde o chyby v autentizaci, kontrole identity uživatele a session managementu. Mezi typické projevy patří:

- **session hijacking** - útočník zcizí session ID a může se vydávat za jiného uživatele,
- **session fixation** - serveru je vnuceno session ID a nedochází k jeho validaci.

## Poznámka Anki 1683128283764

Karty Anki: 1683128283765
GUID: J~u%c~sCXy; štítky: bi-bek::p11 bi-ib::14.

### Otázka (Front)

Co je to selhání integrity software a dat (OWASP Top Ten)? Uveďte typické chyby.

### Odpověď (Back)

Jde o zranitelnosti vznikající z důvodu nesplněných očekávání o obsahu dat získaných z externích zdrojů, případně selháními v komponentách sestavovacího systému. Chyby mohou nastávat v následujících případech:

- aplikace závisí na kódu třetích stran (knihovny, CDN),
- aplikace používá komponenty s automatickou aktualizací,
- nezabezpečená deserializace dat.

## Poznámka Anki 1683128569580

Karty Anki: 1683128569580
GUID: kFk:ZrSs@y; štítky: bi-bek::p11 bi-ib::14.

### Otázka (Front)

Co je to selhání v logování a monitorování (OWASP Top Ten)? Uveďte typické chyby.

### Odpověď (Back)

Nedostatečné logování dovolí útočníkům provádět jejich činnost po delší dobu bez toho, aby byli detekováni. Mezi typické chyby patří:

- dlouhý interval kontroly logu,
- logování nedostatečné množiny typů operací,
- nesrozumitelné nebo málo podrobné logy.

## Poznámka Anki 1683800378536

Karty Anki: 1683800378536
GUID: v_A`t#P+j_; štítky: bi-bek::p11 bi-ib::10 bi-ib::16.

### Otázka (Front)

Popište zranitelnost file inclusion (injekce souboru). Jak se proti ní lze bránit?

### Odpověď (Back)

File inclusion je zranitelnost, která je způsobena nedostatečnou validací vstupu. Spočívá v tom, že zranitelná aplikace vnitřně pracuje se souborem, který je určen na základě uživatelského vstupu. Rozlišujeme:

- **local file inclusion **(LFI) - útočník zobrazí či spustí soubor na zranitelném stroji (typicky vede k information disclosure);
- **remote file inclusion **(RFI) - útočník zobrazí či spustí soubor, který se na zranitelném stroji nenachází, ale může být poskytován externě útočníkem (typicky vede k remote code execution nebo information disclosure).

Proti file inclusion zranitelnostem se lze bránit následujícími způsoby:

- vyhnout se přímým použitím jmen souborů a URL,
- zvážit použití \(\mathtt{chroot}\) jailu,
- použít allow-list pro aplikaci dostupných souborů.

## Poznámka Anki 1717685888120

Karty Anki: 1717685888120
GUID: hKxkmWSrUI; štítky: bi-bek::p11.

Metadata původního zdroje pro kartu 1717685888120: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište cross-site scripting (XSS). Jaké existují typy. Jak jej lze mitigovat?

### Odpověď (Back)

Cross-site scripting (XSS) je typ injection útoku, který spočívá ve vložení škodlivého kódu do jinak důvěryhodné webové aplikace. Rolzišujeme:

- reflected XSS,
- stored XSS,
- DOM-based XSS.

XSS lze mitigovat následujícími metodami:

- escapování nebezpečných znaků,

- enkódování zobrazovaných dat,
- allow-list vybraných HTML tagů a atributů,

- použití Content Security Policy (CSP) a dalších HTTP hlaviček.

