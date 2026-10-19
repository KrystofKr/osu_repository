# BI-KAB – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-kab/BI-KAB.apkg; APKG SHA-256 080060aa53ee5f63eca18237eef611a0bfca99908f9ab640e349ebadb96964ec. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8571882594c00598a0b5a029eed57cadb06fe0563741a3f883a87eacef0c1588.
Původní balíčky: BI-KAB
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1681216974175

Karty Anki: 1681216974175
GUID: kC+s.Ak%M%; štítky: bi-ib::18 bi-kab::p07.

### Otázka (Front)

Co je to čipová karta? Jaký autentizační faktor představuje?

### Odpověď (Back)

Čipová karta je obvykle plastová kartička, které obsahuje integrovaný obvod. Představuje autentizační faktor vlastnictví.

## Poznámka Anki 1681217449023

Karty Anki: 1681217449023
GUID: Ga/Sp/(zX(; štítky: bi-ib::18 bi-kab::p07.

### Otázka (Front)

Jaké jsou typy napájecích a komunikačních rozhraní čipové karty?

### Odpověď (Back)

Rozlišujeme zejména následující typy:

- **kontaktní** (např. USB),

- **bezkontaktní** (RFID a NFC).

Případně pokud karta kombinuje kontaktní a bezkontaktní rozhraní, rozlišujeme dále

- **hybridní** - karta má pro každé rozhraní jiný čip,

- **duální** - obě rozhraní jsou napojena na stejný čip.

## Poznámka Anki 1681218061883

Karty Anki: 1681218061883
GUID: eM6Y`|Rr?6; štítky: bi-ib::18 bi-kab::p07.

### Otázka (Front)

Co je to ISO 14443?

### Odpověď (Back)

ISO 14443 je norma, která popisuje bezkontaktní rozhraní čipových karet s kryptografickými funkcemi. Jde o vysokofrekvenční rozhraní s vazbou na blízko (proximity coupling) na 13.56 MHz.

## Poznámka Anki 1681220085681

Karty Anki: 1681220085681
GUID: RhXSEQ~@q;; štítky: bi-ib::18 bi-kab::p07.

### Otázka (Front)

Jaká kryptografická schémata mohou čipové karty používat?

### Odpověď (Back)

Používá se:

- **symetrická kryptografie** - klíč je tajný a sdílený mezi kartou a terminálem,

- **asymetrická kryptografie ** - karta má vlastní soukromý a veřejný klíč.

## Poznámka Anki 1681220230210

Karty Anki: 1681220230211
GUID: E^{}@#[{a6; štítky: bi-ib::18 bi-kab::p07.

### Otázka (Front)

Popište symetrickou kryptografii na čipových kartách.

### Odpověď (Back)

Karta obvykle obsahuje tajný klíč, který je odvozený od nějakého hlavního klíče (master key) pomocí jednosměrné funkce (diverzifikace klíčů). Terminálu se karta prokáže pomocí svého sériového čísla a tajného klíče. Terminál disponuje hlavním klíčem a pomocí sériového čísla si odvodí správný tajný klíč karty a porovná jej s tím, kterým se karta prezentovala.

## Poznámka Anki 1685209015408

Karty Anki: 1685209015408
GUID: JrA5k1)6dQ; štítky: bi-ib::18 bi-kab::p07.

### Otázka (Front)

Popište vnitřní složení čipové karty.

### Odpověď (Back)

Základní čipové karty si vystačí pouze s propojenými kontakty, rezonančními obvody a podobně. O něco pokročilejší karty obsahují paměť a to buď ve formě ROM, EEPROM nebo zabezpečené paměti (např. MIFARE Classic). Moderní čipové karty potom obsahují počítač, který je konfigurovatelný a programovatelný (např. Java Cards). Vnitřní struktura tohoto počítače je následující:

- **výpočetní jednotky** - CPU, kryptografický koprocesor;
- **paměti** - RAM, ROM, EEPROM;

- ****napájecí a **komunikační rozhraní**;
- **senzory**.

## Poznámka Anki 1685209126652

Karty Anki: 1685209126652
GUID: rU$%~_5<#_; štítky: bi-ib::18 bi-kab::p07.

### Otázka (Front)

Popište diverzifikaci klíčů.

### Odpověď (Back)

Diverzifikace klíčů se používá např. na čipových kartách. Na vstupu obdrží hlavní klíč (master key) a diverzifikační data (např. číslo karty) a na výstupu vrací odvozený klíč (diversified key). Požadujeme, aby tento proces byl jednosměrný, tedy aby z odvozeného klíče bylo výpočetně nemožné získat hlavní klíč.

## Poznámka Anki 1685209330896

Karty Anki: 1685209330896
GUID: dP`S@W/n|K; štítky: bi-ib::18 bi-kab::p07.

### Otázka (Front)

Jakými způsoby se provádí zabezpečení komunikace (secure messaging) čipových karet?

### Odpověď (Back)

Zabezpečení komunikace čipových karet (secure messaging) lze implementovat následujícími způsoby:

- **bez zabezpečení integrity a šifrování **- některé čipové karty nepoužívají autentizaci ani šifrování;
- **zabezpečení integrity** - např. pomocí MAC;
- **zabezpečení integrity a šifrování** - např. pomocí 3DES nebo AES;
- **princip zabalení do struktur typu TLV** (tag, length, value).

