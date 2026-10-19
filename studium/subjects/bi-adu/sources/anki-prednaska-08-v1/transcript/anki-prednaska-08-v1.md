# BI-ADU – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-adu/BI-ADU.apkg; APKG SHA-256 82e24d30673cd0e7a3a5aa4e190d583b7bbdacb9961363822343a47e911816b0. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e4dcf13ba19280a57f78abe30db474a9b8da6ee148ccef4aa2c510acfc892435.
Původní balíčky: BI-ADU
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1681284468406

Karty Anki: 1681284468406
GUID: qw~X9W:cSe; štítky: bi-adu::p08 bi-ib::02.

Metadata původního zdroje pro kartu 1681284468406: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaká existují řešení sdílení filesystémů?

### Odpověď (Back)

Existují následující řešení, která jsou založena na modelu klient-server:

- **NFS** - Unixové řešení, později i Windows;

- **SMB/CIFS** (Samba) - novější, snazší Unix-Windows vazba.

## Poznámka Anki 1681285494437

Karty Anki: 1681285494437
GUID: DAIJwO_rR$; štítky: bi-adu::p08 bi-ib::02.

Metadata původního zdroje pro kartu 1681285494437: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké daemony používá NFS3 na serveru a jaké u klienta? Jaké jsou jejich funkce?

### Odpověď (Back)

Na serveru běží

- \(\mathtt{mountd}\) - mount požadavky (nfs request), vrací file handle;

- \(\mathtt{nfsd}\) - operace se soubory (data request), vrací data;

- \(\mathtt{statd}\) - spolupracuje s \(\mathtt{lockd}\), obnovuje spojení po výpadku;

- \(\mathtt{lockd}\) - zamykání NFS souborů;

- \(\mathtt{nfslogd}\) - logování přístupů.

Na klientu se používá pouze \(\mathtt{statd}\) a \(\mathtt{lockd}\).

## Poznámka Anki 1681286838373

Karty Anki: 1681286838374
GUID: O&L+kD}w)%; štítky: bi-adu::p08.

Metadata původního zdroje pro kartu 1681286838374: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký je rozdíl mezi idempotentním a neidempotentním požadavkem?

### Odpověď (Back)

**Idempotentní **požadavek je bezestavový (např. ze souboru \(S\) načti \(B\) bytů z pozice \(P\)), kdežto **neidempotentní** požadavek je stavový (např. ze souboru \(S\) načti dalších \(B\) bytů).

## Poznámka Anki 1681287160845

Karty Anki: 1681287160845
GUID: i/(QoWrp?c; štítky: bi-adu::p08 bi-ib::02.

Metadata původního zdroje pro kartu 1681287160845: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké výhody poskytuje NFS4 oproti NFS3?

### Odpověď (Back)

NFS4 obsahuje následující vylepšení:

- je stavový,
- sjednocuje funkce všech daemonů do \(\mathtt{nfsd}\),
- používá well-known port \(2049\),
- umí delegovat cache,
- používá pseudo-filesystem (pseudo-mountpoints),
- používá volatile file handles,
- poskytuje vyšší bezpečnost.

## Poznámka Anki 1681287603893

Karty Anki: 1681287603893
GUID: r#%>1RHeu5; štítky: bi-adu::p08 bi-ib::02.

Metadata původního zdroje pro kartu 1681287603893: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to delegace cache u NFS4?

### Odpověď (Back)

Delegace cache znamená přesunutí cache a tedy i operací blíže ke klientům. NFS4 umí delegovat

- **read cache** - lze pro více klientů najednou,

- **write cache** - lze nejvýše pro jednoho klienta.

Tím se snižuje množství síťových operací a zrychluje se běh filesystému.

## Poznámka Anki 1681287777945

Karty Anki: 1681287777945
GUID: D]BthMS7$c; štítky: bi-adu::p08 bi-ib::02.

Metadata původního zdroje pro kartu 1681287777945: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to pseudo-filesystem (pseudo-mountpoint) u NFS4?

### Odpověď (Back)

Pseudo-filesystem (pseudo-mountpoint) je optimalizace, která funguje tak, že namísto vyššího počtu sdílených adresářů se připojí méně jim nadřazených adresářů, které nutně nemusí být sdílené. Přístup do těchto adresářů je potom řízen tak, aby byly viditelné pouze sdílené adresáře. Omezuje se tím počet spojení.

 [Obrázek: paste-b66d3d67ca0b4b8574a5d15068180d1166042318.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1681287949500

Karty Anki: 1681287949500
GUID: xBf:W]=N|A; štítky: bi-adu::p08 bi-ib::02.

Metadata původního zdroje pro kartu 1681287949500: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké bezpečnostní prvky poskytuje NFS4?

### Odpověď (Back)

NFS4 umožňuje konzistenci a případně mapování \(\mathtt{UID}\) podle uživatelského jména. Dovoluje také mapovat vzdáleného \(\mathtt{root}\) uživatele na uživatele \(\mathtt{nobody}\). Umí použít i Kerberos autentizaci nebo Diffie-Hellmanův mechanismus zřízení společného klíče.

## Poznámka Anki 1681288088929

Karty Anki: 1681288088929
GUID: zLoSnHjZhl; štítky: bi-adu::p08 bi-ib::02.

Metadata původního zdroje pro kartu 1681288088929: v původním balíčku pozastavená karta.

### Otázka (Front)

Co jsou to volatile file handles u NFS4?

### Odpověď (Back)

Volatile file handles umožňují automatické obnovení file handle. Řeší se tím například problém přesunutí sdíleného adresáře.

## Poznámka Anki 1681288281389

Karty Anki: 1681288281389
GUID: Gd>{>w[=E.; štítky: bi-adu::p08 bi-ib::02.

Metadata původního zdroje pro kartu 1681288281389: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to automounter?

### Odpověď (Back)

Automounter připojuje filesystém pouze pokud jsou používány a po určité době je v případě neaktivity odpojí. Tím se redukuje počet aktivních spojení.

