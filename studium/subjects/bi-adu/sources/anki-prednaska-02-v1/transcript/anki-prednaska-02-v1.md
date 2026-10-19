# BI-ADU – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-adu/BI-ADU.apkg; APKG SHA-256 82e24d30673cd0e7a3a5aa4e190d583b7bbdacb9961363822343a47e911816b0. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e4dcf13ba19280a57f78abe30db474a9b8da6ee148ccef4aa2c510acfc892435.
Původní balíčky: BI-ADU
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1677659356434

Karty Anki: 1677659356434
GUID: yUZs!zMJL8; štítky: bi-adu::p02 bi-ib::01 bi-ib::25 ni-pb::21.

### Otázka (Front)

Jaký je rozdíl mezi autentizací a autorizací?

### Odpověď (Back)

**Autentizace **je proces ověření identity uživatele (např. pomocí hesla, klíče, otisku prstu), kdežto **autorizace** je proces ověření, zda daný uživatel má právo na provedení operace (např. pomocí jeho identity, členství ve skupinách, RBAC).

## Poznámka Anki 1677659471626

Karty Anki: 1677659471626
GUID: c3`SsW:TCB; štítky: bi-adu::p02 bi-ib::01.

Metadata původního zdroje pro kartu 1677659471626: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakými způsoby lze obdržet práva administrátora?

### Odpověď (Back)

Existují tři způsoby, jak obdržet práva administrátora:

- přihlášení jako administrátor,
- \(\mathtt{su \ <command>}\) (switch user),

- \(\mathtt{sudo \ <command>}\) (substitute user do).

## Poznámka Anki 1677660232793

Karty Anki: 1677660232793
GUID: u]_5>^/ikg; štítky: bi-adu::p02 bi-ib::01.

Metadata původního zdroje pro kartu 1677660232793: v původním balíčku pozastavená karta.

### Otázka (Front)

K čemu slouží \(\mathtt{sudo}\)? Jaký konfigurační soubor používá?

### Odpověď (Back)

Utilita \(\mathtt{sudo}\) (substitue user do) slouží ke spouštění příkazů pod identitou (a s právy) jiného uživatele. Konfigurovat jej můžeme v \(\mathtt{/etc/sudoers}\).

## Poznámka Anki 1677660856668

Karty Anki: 1677660856668
GUID: G@z/U9TjUJ; štítky: bi-adu::p02 bi-ib::01.

### Otázka (Front)

Popište strukturu jednoho řádku v \(\mathtt{/etc/sudoers}\)?

### Odpověď (Back)

\[\mathtt{kdo\ kde=[(jako\ kdo)] [tag:]\ co}\]

## Poznámka Anki 1677662080849

Karty Anki: 1677662080849
GUID: fU[b~&csM#; štítky: bi-adu::p02 bi-ib::01.

Metadata původního zdroje pro kartu 1677662080849: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký význam má sticky bit (\(\mathtt t\)) na adresáři?

### Odpověď (Back)

Soubory v takovém adresáři mohou být mazány pouze jejich vlastníkem, vlastníkem adresáře nebo uživatelem \(\mathtt{root}\).

## Poznámka Anki 1677662498904

Karty Anki: 1677662498904
GUID: dNx[&*2K-0; štítky: bi-adu::p02 bi-ib::01.

Metadata původního zdroje pro kartu 1677662498904: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký význam má \(\mathtt{SGID}\) bit (\(\mathtt s\)) na adresáři?

### Odpověď (Back)

Všechny soubory vznikající v takovém adresáři dědí skupinové vlastnictví od skupinového vlastníka tohoto adresáře.

## Poznámka Anki 1677663144145

Karty Anki: 1677663144145
GUID: y}D:O~K:LN; štítky: bi-adu::p02 bi-ib::01 bi-ib::09 bi-ib::25.

Metadata původního zdroje pro kartu 1677663144145: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to access control list (ACL)? Jakými příkazy se konfiguruje? Jak jsou ACL implementovány?

### Odpověď (Back)

ACL umožňuje řídit oprávnění s vyšší granularitou než poskytují základní Unixová oprávnění, nad kterými má precedenci. Pro jejich konfiguraci používáme příkazy \(\mathtt{setfacl}\) a \(\mathtt{getfacl}\). Často se implementují jako přídavný i-node, který je nalinkován z toho původního.

## Poznámka Anki 1677663764188

Karty Anki: 1677663764188
GUID: oo#zNz$Q<m; štítky: bi-adu::p02 bi-ib::01 bi-ib::25.

Metadata původního zdroje pro kartu 1677663764188: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak funguje maska u access control lists (ACL)?

### Odpověď (Back)

Maska určuje nejvyšší možná oprávnění na souboru. Například pro
\[\mathtt{user\text:\ rwx} \quad \mathtt{mask\text:\ r\text-x}\]budou efektivní oprávnění pro uživatele \(\mathtt{user}\) pouze \(\mathtt{r\text-x}\).

