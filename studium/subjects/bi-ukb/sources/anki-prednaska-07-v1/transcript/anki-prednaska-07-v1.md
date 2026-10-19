# BI-UKB – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-ukb/BI-UKB.apkg; APKG SHA-256 fb963722a1039499908d9a37b947a0f774fd26b951b463a4c2349468681bec67. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8d39d92d14a3cb34c1c177ef00602d3767837744484a3254d799cb18f10b34a9.
Původní balíčky: BI-UKB
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1667978710632

Karty Anki: 1667978710632
GUID: xB{jd]@AFc; štítky: bi-ukb::p07.

### Otázka (Front)

Co je to front-end a back-end webové aplikace?

### Odpověď (Back)

|       **front-end** |       **back-end** |         
|       kód vykonaný na straně prohlížeče |       kód vykonaný na straně serveru |         
|       využívá výpočetní výkon koncové stanice |       využívá výpočetní výkon serveru |         
|       uživatel vidí zdrojový kód |       uživatel nevidí zdrojový kód |

## Poznámka Anki 1667979152742

Karty Anki: 1667979152742
GUID: MT!vxTPobM; štítky: bi-ukb::p07.

Metadata původního zdroje pro kartu 1667979152742: v původním balíčku pozastavená karta.

### Otázka (Front)

Co jsou to statické a dynamické stránky?

### Odpověď (Back)

| 
      **statické stránky** | 
      **dynamické stránky** | 

| 
      mají pouze front-end | 
      mají front-end i back-end | 

| 
      nemají logiku na straně serveru | 
      mají logiku na straně serveru | 

| 
      nemají vstup od uživatele | 
      často používají vstup od uživatele |

## Poznámka Anki 1667980013925

Karty Anki: 1667980013925
GUID: iWg%YXnkdu; štítky: bi-ukb::p07.

Metadata původního zdroje pro kartu 1667980013925: původní příznak autora 5; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to SSI (Server Side Includes)?

### Odpověď (Back)

Server Side Includes umožňují při načítání HTML stránky do ní vložit další kód.

## Poznámka Anki 1667982324457

Karty Anki: 1667982324457
GUID: tu@mf*Wa=%; štítky: bi-ib::16 bi-ukb::p07.

### Otázka (Front)

Popište HTTP hlavičku \(\texttt{Content-Security-Policy}\) (CSP).

### Odpověď (Back)

HTTP hlavička \(\texttt{Content-Security-Policy}\) (CSP) definuje jaké zdroje mohou být na dané stránce načítány a odkud. Používá se jako ochrana před cross-site scripting (XSS) útoky a nahrazuje tak hlavičku \(\texttt{X-XSS-Protection}\). Mezi možné atributy patří např. \(\texttt{script-src}\), \(\texttt{img-src}\) nebo \(\texttt{font-src}\).

## Poznámka Anki 1667982758214

Karty Anki: 1667982758214
GUID: iI%SYZ5$cM; štítky: bi-ib::16 bi-ukb::p07.

### Otázka (Front)

Popište HTTP hlavičku \(\texttt{Strict-Transport-Security}\) (HSTS).

### Odpověď (Back)

HTTP hlavička \(\texttt{Strict-Transport-Security}\) (HSTS) indikuje, že by k dané stránce mělo být přistupováno pouze skrze protokol HTTPS a všechny další přístupy skrze HTTP by měly být konvertovány na HTTPS.

## Poznámka Anki 1667982896772

Karty Anki: 1667982896772
GUID: fSdZn<s;T+; štítky: bi-ib::16 bi-ukb::p07.

Metadata původního zdroje pro kartu 1667982896772: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište HTTP public key pinning (HPKP) a HTTP hlavičku \(\texttt{Public-Key-Pins}\).

### Odpověď (Back)

HTTP public key pinning (HPKP) byl bezpečnostní mechanismus zajišťovaný HTTP hlavičkou \(\texttt{Public-Key-Pins}\), který umožňoval webovým stránkám specifikovat seznam hashů veřejných klíčů, jež se musí objevit v řetezci certifikátů všech budoucích spojení s danou stránkou. Dnes se tento mechanismus už nepoužívá kvůli možným lidským chybám a denial-of-service útokům.

## Poznámka Anki 1667983087617

Karty Anki: 1667983087617
GUID: BT3%oU-`_Y; štítky: bi-ukb::p07.

Metadata původního zdroje pro kartu 1667983087617: původní příznak autora 5; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to Downgrade Attack?

### Odpověď (Back)

Downgrade Attack je typ útoku, kdy útočník např. donutí server používat starší verzi šifrovacího protokolu, který umí napadnout.

## Poznámka Anki 1667983809475

Karty Anki: 1667983809475
GUID: NXcl6Mz,/E; štítky: bi-ukb::p07.

Metadata původního zdroje pro kartu 1667983809475: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

V čem spočívá zranitelnost Security Misconfiguration?

### Odpověď (Back)

Jde o špatnou konfiguraci prostředí, ve kterém je webová aplikace provozována, např. špatný error handling, zapomenuté konfigurační skripty, výchozí hesla.

## Poznámka Anki 1667984091750

Karty Anki: 1667984091750
GUID: Eu~;@6VF=m; štítky: bi-ib::07 bi-ukb::p07.

### Otázka (Front)

Popište security through obscurity.

### Odpověď (Back)

Security through obscurity spoléhá na utajení a nestandartní postupy či konstrukce pro zajištení bezpečnosti. Jejím hlavním cílem je zmatení útočníka, neposkytuje ale žádnou formu zabezpečení.

## Poznámka Anki 1667984366204

Karty Anki: 1667984366204
GUID: Af)oC1p!{R; štítky: bi-ukb::p07.

### Otázka (Front)

Co je to Security Information and Event Management (SIEM)?

### Odpověď (Back)

Security Information and Event Management se zabývá dlouhodobým ukládáním událostí jejich analýzou a hlášením problémů.

## Poznámka Anki 1667986873992

Karty Anki: 1667986873992
GUID: nQZy:EixYx; štítky: bi-ukb::p07.

Metadata původního zdroje pro kartu 1667986873992: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to Mobile Device Management (MDM)?

### Odpověď (Back)

Mobile Device Management je nástroj pro zajištění kontroly nad mobilními zařízeními a vymáhání firemních politik.

## Poznámka Anki 1667987721911

Karty Anki: 1667987721911
GUID: IO$8vgQchf; štítky: bi-ukb::p07.

### Otázka (Front)

Porovnejte Static Aplication Security Testing (SAST) a Dynamic Aplication Security Testing (DAST).

### Odpověď (Back)

| 
      **Static Aplication Security Testing** | 
      **Dynamic Aplication Security Testing** | 

| 
      testuje aplikaci bez jejího spuštení | 
      testuje aplikaci za jejího běhu | 

| 
      testuje zdrojový kód aplikace (inside-out) | 
      testuje aplikaci skrze API nebo front-end (outside-in) | 

| 
      rychlé testování | 
      pomalé testování | 

| 
      vyžaduje přístup ke zdrojovému kódu | 
      nevyžaduje přístup ke zdrojovému kódu | 

| 
      dokáže nalézt konkrétní řádku s chybou | 
      nedokáže nalézt konkrétní řádku s chybou | 

| 
      vysoký počet false-positives | 
      nízký počet false-positives |

