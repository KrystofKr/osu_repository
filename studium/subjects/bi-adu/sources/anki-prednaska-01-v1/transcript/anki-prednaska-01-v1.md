# BI-ADU – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-adu/BI-ADU.apkg; APKG SHA-256 82e24d30673cd0e7a3a5aa4e190d583b7bbdacb9961363822343a47e911816b0. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e4dcf13ba19280a57f78abe30db474a9b8da6ee148ccef4aa2c510acfc892435.
Původní balíčky: BI-ADU
Rozsah: 15 poznámek, 15 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1677062946999

Karty Anki: 1677062946999
GUID: b$[zWZh$3|; štítky: bi-adu::p01.

Metadata původního zdroje pro kartu 1677062946999: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou kategorie administrátorských nástrojů?

### Odpověď (Back)

Administrátorské nástroje dělíme do těchto kategorií:

- **GUI** (graphical user interface) administrátorské příkazy (např. Control Panel ve Windows),

- **CLI** (command line interface) administrátorské příkazy (např. \(\mathtt{useradd}\), \(\mathtt{ifconfig}\)),

- základní Unixové příkazy (\(\mathtt{vi}\), \(\mathtt{mkdir}\)).

## Poznámka Anki 1677063112684

Karty Anki: 1677063112684
GUID: db-|;4`T96; štítky: bi-adu::p01 bi-ib::01.

### Otázka (Front)

Kam se ukládají hashovaná hesla?

### Odpověď (Back)

Hashovaná hesla se ukládají do \(\mathtt{/etc/shadow}\).

## Poznámka Anki 1677067117054

Karty Anki: 1677067117054
GUID: uJ5bKS`W2R; štítky: bi-adu::p01 bi-ib::01.

Metadata původního zdroje pro kartu 1677067117054: v původním balíčku pozastavená karta.

### Otázka (Front)

V jakém konfiguračním souboru se nastavují parametry hesel? Jaké parametry lze nastavovat?

### Odpověď (Back)

Parametry hesel jako password aging, požadavky na sílu nebo zákaz opakování lze nastavovat v souboru \(\mathtt{/etc/default/passwd}\) na Solarisu a \(\mathtt{/etc/security/pwquality\text.conf}\) na Linuxu.

## Poznámka Anki 1677067495217

Karty Anki: 1677067495217
GUID: Ic<X%u84Cu; štítky: bi-adu::p01 bi-ib::01.

Metadata původního zdroje pro kartu 1677067495217: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak lze provést změnu hashovacího algoritmu hesel?

### Odpověď (Back)

Změnu hashovacího algoritmu hesel lze provést pomocí souborů \(\mathtt{/etc/security/crypt\text.conf}\) a 
\(\mathtt{/etc/security/policy\text.conf}\) na Solarisu a na Linuxu pomocí příkazu \(\mathtt{authconfig}.\)

## Poznámka Anki 1677067727003

Karty Anki: 1677067727003
GUID: xP?Th~EpT/; štítky: bi-adu::p01 bi-ib::01.

### Otázka (Front)

V jakém formátu jsou ukládána hesla v \(\mathtt{/etc/shadow}\)?

### Odpověď (Back)

Hesla v souboru \(\mathtt{/etc/shadow}\) mají následující formát:
\[\mathtt{\$<algoritmus>\$<sul>\$<hash>}.\]

## Poznámka Anki 1677067861440

Karty Anki: 1677067861440
GUID: c}^[nRUi]O; štítky: bi-adu::p01 bi-ib::01.

### Otázka (Front)

V jakém konfiguračním souboru najdeme přířazení primárních skupin a v jakém přiřazení sekundárních skupin?

### Odpověď (Back)

Přiřazení **primárních **skupin nalezneme v \(\mathtt{/etc/passwd}\) a **sekundárních **v \(\mathtt{/etc/group}\).

## Poznámka Anki 1677067922509

Karty Anki: 1677067922509
GUID: d:dEF^;3/$; štítky: bi-adu::p01 bi-ib::01.

### Otázka (Front)

Jakými příkazy můžeme změnit vlastnictví či skupinové vlastnictví souboru?

### Odpověď (Back)

Vlastnictví souboru lze měnit příkazm \(\mathtt{chown}\) a skupinové vlastnictví příkazem \(\mathtt{chgrp}\).

## Poznámka Anki 1677067944382

Karty Anki: 1677067944382
GUID: wOeH#F:)AQ; štítky: bi-adu::p01 bi-ib::01.

### Otázka (Front)

Jakým příkazem provedeme změnu aktuální skupiny?

### Odpověď (Back)

Změnu aktuální skupiny lze provést příkazem \(\mathtt{newgrp}\).

## Poznámka Anki 1677068435581

Karty Anki: 1677068435581
GUID: nWB~w>#wVR; štítky: bi-adu::p01 bi-ib::01.

Metadata původního zdroje pro kartu 1677068435581: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište princip jmenných služeb (name services).

### Odpověď (Back)

Běžné uživatelské účty jsou sdíleny v rámci domény serverem nebo servery pomocí protokolů jako LDAP, NIS nebo NIS+. Systémoví uživatelé jako \(\mathtt{root}\) či \(\mathtt{bin}\) by měli být dostupní lokálně pro případ výpadku sítě. Pomocí souboru \(\mathtt{/etc/nsswitch\text.conf}\) lze definovat prioritu hledání informace o uživateli.

## Poznámka Anki 1677068728930

Karty Anki: 1677068728930
GUID: B_0G+X#kQC; štítky: bi-adu::p01.

Metadata původního zdroje pro kartu 1677068728930: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište pořadí vykonávaných souborů po přihlášení uživatele.

### Odpověď (Back)

1. Pro všechny uživatele se vykoná \(\mathtt{/etc/profile}\).
2. Pro potřeby GUI se může vykonat \(\mathtt{$HOME/\text.dtprofile}\).
3. V závislosti na shellu se vykoná \(\mathtt{$HOME/\text.profile}\), \(\mathtt{$HOME/\text.bash\_profile}\) nebo jiné.
4. Při spuštění shellu se potom v závislosti na shellu vykoná \(\mathtt{$HOME/\text.kshrc}\), \(\mathtt{$HOME/\text.bashrc}\) nebo jiné.

## Poznámka Anki 1677068994173

Karty Anki: 1677068994173
GUID: Oi.an5yD8x; štítky: bi-adu::p01 bi-ib::01.

Metadata původního zdroje pro kartu 1677068994173: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to vnější a vnitřní identita?

### Odpověď (Back)

Vnější identitou se rozumí \(\mathtt{username}\) a \(\mathtt{groupname}\), kdežto vnitřní \(\mathtt{UID}\) a \(\mathtt{GID}\).

## Poznámka Anki 1677069157731

Karty Anki: 1677069157731
GUID: BjlZZ`Xf]O; štítky: bi-adu::p01 bi-ib::01 bi-ib::25.

Metadata původního zdroje pro kartu 1677069157731: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou tři druhy vnitřní identity procesu?

### Odpověď (Back)

Rozlišujeme následující vnitřní identity procesu:

- **reálná **(\(\mathtt{RUID}\), \(\mathtt{RGID}\)) - využívaná při akceptaci signálů,

- **efektivní **(\(\mathtt{EUID}\), \(\mathtt{EGID}\)) - při práci se soubory (práva, vlastnictví),

- **uložená **(\(\mathtt{SUID}, \mathtt{SGID}\)) - uchování identity při změně \(\mathtt{EUID}\).

## Poznámka Anki 1677069311832

Karty Anki: 1677069311833
GUID: hC#9`Y~Vip; štítky: bi-adu::p01 bi-ib::01.

Metadata původního zdroje pro kartu 1677069311833: v původním balíčku pozastavená karta.

### Otázka (Front)

Co jsou to \(\mathtt{SUID}\) a \(\mathtt{SGID}\) programy? Uveďte příklad.

### Odpověď (Back)

\(\mathtt{SUID}\), resp. \(\mathtt{SGID}\), programy jsou programy, u kterých při spuštění proces získává \(\mathtt{EUID}\) a \(\mathtt{SUID}\) od **vlastníka **programu, resp. \(\mathtt{EGID}\) a \(\mathtt{SGID}\) od **skupinového vlastníka **programu. Příkladem je příkaz \(\mathtt{su}\).

## Poznámka Anki 1677069447533

Karty Anki: 1677069447534
GUID: Ni6U@5pZ:A; štítky: bi-adu::p01 bi-ib::01.

Metadata původního zdroje pro kartu 1677069447534: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak provedeme změnu všech tří druhů identity na identitu \(\mathtt{username}\)?

### Odpověď (Back)

Změnu všech tří druhů identity provedeme pomocí volání \(\mathtt{su\ [\text{-}]\ username}\). Při volání bez \(\text-\) se neprovedou volání \(\mathtt{/etc/profile}\) apod., jen dojde ke změně identity.

## Poznámka Anki 1683995891549

Karty Anki: 1683995891550
GUID: dGxj(./T}d; štítky: bi-adu::p01.

Metadata původního zdroje pro kartu 1683995891550: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište kategorie subsystémů, které administrátor spravuje.

### Odpověď (Back)

Administrátor obvykle spravuje následující kategorie subsystémů:

- **********uživatelé********** - práva, autentizace, autorizace;

- **********zařízení********** - disky, tiskárny, síťové karty;

- ******síťová administrace****** - NFS, Samba, LDAP, NIS;

- ****************************************virtuální subsystémy**************************************** - domény, zóny, clustery.

