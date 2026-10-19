# BI-UKB – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-ukb/BI-UKB.apkg; APKG SHA-256 fb963722a1039499908d9a37b947a0f774fd26b951b463a4c2349468681bec67. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8d39d92d14a3cb34c1c177ef00602d3767837744484a3254d799cb18f10b34a9.
Původní balíčky: BI-UKB
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1665555908109

Karty Anki: 1665555908109
GUID: PfF7_^0-RC; štítky: bi-ukb::p03.

Metadata původního zdroje pro kartu 1665555908109: původní příznak autora 5; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte protokol.

### Odpověď (Back)

Série kroků, navržených za účelem dosažení cíle, která zahrnuje dvě nebo více stran. Každá strana musí kroky protokolu znát předem a musí souhlasit s jejich dodržováním. Protokol musí být jednoznačný a kompletní.

## Poznámka Anki 1665556061815

Karty Anki: 1665556061815
GUID: ztz@%^2E:0; štítky: bi-ukb::p03.

Metadata původního zdroje pro kartu 1665556061815: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké role má kryptografie v bezpečnostních protokolech? Uveďte kryptografické primitivy spjaté s každým bodem.

### Odpověď (Back)

- **důvěrnost** - utajení informací (šifrování)

- **integrita **- přesnost informací, tedy zda nedošlo ke změně při přenosu (hashovací funkce)

- **autentizace** - ověření odesílatele a původu informací (Message Authentication Code)

## Poznámka Anki 1665557778183

Karty Anki: 1665557778183
GUID: QuR_V6+lAq; štítky: bi-ukb::p03.

Metadata původního zdroje pro kartu 1665557778183: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Co to znamená diverzifikace klíčů?

### Odpověď (Back)

Kompromitace jednoho uživatelského klíče nesmí ovlivnit bezpečnost ostatních klíčů v systému.

## Poznámka Anki 1665558680552

Karty Anki: 1665558680552
GUID: kIciX9;xa|; štítky: bi-ib::19 bi-ukb::p03.

Metadata původního zdroje pro kartu 1665558680552: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Jak lze generovat skutečně náhodné hodnoty? Jaké jsou nevýhody těchto metod?

### Odpověď (Back)

Zdrojem může být:

- **uživatel** - údery kláves, pohyby myši, přistupové časy k disku

- **fyzikální jevy** - Zenerova dioda, termální šum rezistorů

Jeližkož jde o fyzické komponenty, může se u nich projevit stárnutí. Často jsou pomalé, proto se většinou používají jako seed (iniciální hodnota) pro generování pseudonáhodných hodnot.

## Poznámka Anki 1665558743058

Karty Anki: 1665558743058
GUID: hIkzmMY){|; štítky: bi-ib::19 bi-ukb::p03.

Metadata původního zdroje pro kartu 1665558743058: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Jak se generují pseudonáhodné hodnoty?

### Odpověď (Back)

Pro jejich generování se používá deterministický algoritmus, který potřebuje seed (iniciální hodnotu).

## Poznámka Anki 1665559251778

Karty Anki: 1665559251779
GUID: v:1^=4Qnuq; štítky: bi-ukb::p03.

Metadata původního zdroje pro kartu 1665559251779: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Transport Layer Security (TLS) protokol.

### Odpověď (Back)

Transport Layer Security (TLS) je protokol, který má za cíl zajistit důvěrnost a integritu dat mezi dvěma komunikujicími aplikacemi na transportní vrstvě. Sestává ze dvou vrstev:

- **nižší** - TLS Record Protocol,

- **vyšší** - čtyři TLS protokoly: Handshake, Alert, Change Cipher Spec a Application Data.

## Poznámka Anki 1665559397450

Karty Anki: 1665559397451
GUID: fJt?>e2c!m; štítky: bi-ukb::p03.

Metadata původního zdroje pro kartu 1665559397451: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to Request for Comments (RFC)?

### Odpověď (Back)

Jde o dokumenty popisující internetové protokoly v kompletním detailu pro implementaci a umožňují jejich analýzu.

## Poznámka Anki 1665559688674

Karty Anki: 1665559688674
GUID: u~I(nt~N_*; štítky: bi-ib::12 bi-ukb::p03.

### Otázka (Front)

Popište TLS Handshake protokol.

### Odpověď (Back)

Handshake protokol je vysokoúrovňový TLS protokol, který zodpovídá za zřízení zabezpečené relace, což zahrnuje:

- sjednání verze TLS protokolu a sady kryptografických algoritmů,
- autentizace serveru, případně i klienta, pomocí digitálního certifikátu,
- sjednání tajného klíče.

## Poznámka Anki 1665559761623

Karty Anki: 1665559761623
GUID: e(n(.|y,>,; štítky: bi-ukb::p03.

Metadata původního zdroje pro kartu 1665559761623: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište TLS Record protokol.

### Odpověď (Back)

Jde o nízkoúrovňový protokol, který má na starosti rozklad a skládání paketů vyšší vrstvy TLS protokolu do rámců. Volitelně ješte poskytuje:

- **šifrování **- pomocí proudové šifry (ChaCha20) nebo blokové šifry (AES či mód AEAD),

- **kompresi **- pomocí Deflate,

- **integritu** - pomocí MAC s klíčovaným hashem nebo AEAD.

