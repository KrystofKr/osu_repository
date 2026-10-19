# BI-BEK – Přednáška 12

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1683718366365

Karty Anki: 1683718366365
GUID: eR0!gSWK)H; štítky: bi-bek::p12 bi-ib::12.

### Otázka (Front)

Popište Transport Layer Security (TLS) protokol.

### Odpověď (Back)

Transport Layer Security (TLS) je protokol, který má za cíl zajistit důvěrnost a integritu dat mezi dvěma komunikujicími aplikacemi na transportní vrstvě. Sestává ze dvou vrstev:

- **nižší** - TLS Record Protocol,

- **vyšší** - čtyři TLS protokoly: Handshake, Alert, Change Cipher Spec a Application Data.

## Poznámka Anki 1683718715849

Karty Anki: 1683718715849
GUID: HLD5xIAwW#; štítky: bi-bek::p12 bi-ib::12.

### Otázka (Front)

Popište TLS Record protokol.

### Odpověď (Back)

Record protokol je nízkoúrovňový TLS protokol, který má na starosti rozklad a skládání paketů vyšší vrstvy TLS protokolu do rámců. Volitelně ještě poskytuje:

- **šifrování **- pomocí proudové šifry (ChaCha20) nebo blokové šifry (AES či mód AEAD),

- **kompresi **- pomocí Deflate,

- **integritu** - pomocí HMAC nebo AEAD.

## Poznámka Anki 1683718756292

Karty Anki: 1683718756292
GUID: Bx.eO12yG/; štítky: bi-bek::p12 bi-spol::10.

### Otázka (Front)

Co je to AEAD?

### Odpověď (Back)

Authenticated Encryption with Associated Data (AEAD) je speciální mód blokových šifer, který nejen zprávu šifruje, ale zárověň ji i autentizuje.

## Poznámka Anki 1683718803790

Karty Anki: 1683718803790
GUID: sE?/;A;XKq; štítky: bi-bek::p12 bi-ib::12.

### Otázka (Front)

Popište TLS Change Cipher Spec protokol.

### Odpověď (Back)

Change Cipher Spec protokol je vysokoúrovňový TLS protokol slouží k signalizaci změny v šifrování.

## Poznámka Anki 1683720202575

Karty Anki: 1683720202575
GUID: dp_q$;?PV}; štítky: bi-bek::p12 bi-ib::12.

### Otázka (Front)

Popište TLS Alert protokol.

### Odpověď (Back)

Alert protokol je vysokoúrovňový TLS protokol sloužící pro posílání informací o varováních a chybách. V případě fatální chyby uzavřou obě strany spojení, v případě varování může spojení pokračovat dále.

## Poznámka Anki 1683720686837

Karty Anki: 1683720686837
GUID: z/H3fKT1O6; štítky: bi-bek::p12.

### Otázka (Front)

Jaký je rozdíl mezi self-signed certifikátem a certifikátem vystaveným důvěryhodnou CA?

### Odpověď (Back)

| 
      **self-signed certifikát** | 
      **certifikát vystavený důvěryhodnou CA** | 

| 
      levný | 
      drahý | 

| 
      poskytuje šifrování, ale ne autentizaci | poskytuje šifrování i autentizaci | 

| 
      kořenový certifikát není předinstalován v běžných OS
 | 
      kořenový certifikát je předinstalován v běžných OS | 
Protože kořenový certifikát pro self-signed certifikát není nainstalován v běžných OS, je vhodný zejména pro subjekty, které mají možnost do OS nainstalovat svůj vlastní kořenový certifikát. V případě, že to není možné, bude uživatel neustále varován před nedůvěryhodnou CA.

## Poznámka Anki 1683818516237

Karty Anki: 1683818516237
GUID: rB@.g<*G^?; štítky: bi-bek::p12 bi-ib::12.

### Otázka (Front)

Jak se TLS chrání proti man-in-the-middle útokům?

### Odpověď (Back)

TLS používá certifikáty, které by měl klient ověřovat. Pokud tak však neučiní, může útočník odposlouchávat a ovlivňovat komunikaci mezi klientem a serverem.

## Poznámka Anki 1687444453933

Karty Anki: 1687444453933
GUID: F2JS*Z*8^B; štítky: bi-bek::p12.

Metadata původního zdroje pro kartu 1687444453933: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište TLS Handshake protokol.

### Odpověď (Back)

Handshake protokol je vysokoúrovňový TLS protokol, který zodpovídá za zřízení zabezpečené relace, což zahrnuje:

- sjednání verze TLS protokolu a sady kryptografických algoritmů,
- autentizace serveru, případně i klienta, pomocí digitálního certifikátu,
- sjednání tajného klíče.

