# BI-ADU – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-adu/BI-ADU.apkg; APKG SHA-256 82e24d30673cd0e7a3a5aa4e190d583b7bbdacb9961363822343a47e911816b0. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e4dcf13ba19280a57f78abe30db474a9b8da6ee148ccef4aa2c510acfc892435.
Původní balíčky: BI-ADU
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1682494580793

Karty Anki: 1682494580793
GUID: sAMy{RE@He; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1682494580793: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište proces bootu systému.

### Odpověď (Back)

Boot systému (bootstrapping) se skládá z několika dílčích fází:

1. firmware fáze,
2. bootloader (GRUB) fáze,
3. načtení kernelu a konfigurace,
4. spuštění procesu \(\mathtt{init}\),
5. spouštění služeb a konfigurace systému.

## Poznámka Anki 1682494760548

Karty Anki: 1682494760548
GUID: b5r&X(~mJS; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1682494760548: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište firmware fázi bootu systému.

### Odpověď (Back)

Ve firmware fázi proběhne:

- power-on self-test (POST),
- inicializace hardware a driverů,
- výběr boot zařízení,
- načtení a spuštění boot kódu.

## Poznámka Anki 1682494836575

Karty Anki: 1682494836575
GUID: Pt}?sBd_TW; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1682494836575: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište bootloader fázi bootu systému.

### Odpověď (Back)

V bootloader fázi se vyhledá, načte a spustí boot program, který se vyskytuje na specifikované adrese v paměti.

## Poznámka Anki 1682494932666

Karty Anki: 1682494932666
GUID: qp_Kf@I!OD; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1682494932666: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Grand Unified Bootloader (GRUB).

### Odpověď (Back)

Grand Unified Bootloader (GRUB) začíná u **filesystem readeru**, který načte jeho konfiguraci. Následně je uživatel prezentován s možností výběru, odkud začít bootovat. Poté dojde k načtení a spuštění patřičného kernelu.

## Poznámka Anki 1682495142707

Karty Anki: 1682495142708
GUID: cxDGyvB4)/; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1682495142708: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište fázi načtení kernelu a konfigurace bootu systému.

### Odpověď (Back)

Ve fázi načtení a kernelu a konfigurace dojde k:

- inicializaci datových struktur kernelu,
- načtení driverů a inicializaci hardware,
- mountu root filesystému,
- přečtení konfigurace kernelu,
- načtení kernel modulů,
- spuštění prvního procesu \(\mathtt{init}\).

## Poznámka Anki 1682495437740

Karty Anki: 1682495437740
GUID: pjpY#dkcz-; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1682495437740: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište \(\mathtt{init}\) fázi bootu systému.

### Odpověď (Back)

Operace prováděné v \(\texttt{init}\) fázi bootu systému závisí na jeho typu a verzi. Dříve se používaly následující přístupy:

- **System V** - několik inicializačních skriptů v adresářích \(\texttt{/etc/rc<milestone>.d}\),
- **BSD** - jeden inicializační skript \(\texttt{/etc/rc}\).

Dnes se používají zejména:

- **Linux** - proces \(\texttt{init}\) nebo \(\texttt{systemd}\),

- **Solaris** - Solaris Service Management Facility.

## Poznámka Anki 1682495649991

Karty Anki: 1682495649991
GUID: vOv,]p:FG+; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1682495649991: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište runlevels (milestones) systému.

### Odpověď (Back)

Runlevel (na Solarisu milestone) je operační mód systému, který definuje, jaké zdroje jsou uživatelům přístupné. Jsou definovány následující runlevels (milestones):

| 
      **runlevel / milestone** | 
      **typ (Unix)** | 
      **typ (Solaris)** | 

| 
      \(\mathtt 0\)
 | 
      off | 
      power-down
 | 

| 
      \(\mathtt 1\) / \(\mathtt S\) / \(\mathtt s\)
 | 
      single-user mode | single-user | 
       | 

| 
      \(\mathtt 2\)
 | 
      multi-user mode | 
      mutli-user | 

| 
      \(\mathtt 3\)
 | 
      multi-user mode with networking | 
      **multi-user-server** | 
       | 

| 
      \(\mathtt 4\)
 | 
      user-defined multi-user (nepoužívá se)
 | 
      user-defined multi-user (nepoužívá se) | 

| 
      \(\mathtt 5\)
 | 
      **full mode (**\(\mathtt 3\)** s display managerem)** | 
      power-down (s automatickým vypnutím napájení) | 

| 
      \(\mathtt 6\)
 | 
       reboot | 
       reboot
 |

### Doplňující pole (Extra)

Tučně je vždy označen hlavní runlevel (milestone) pro daný systém.

## Poznámka Anki 1682496993280

Karty Anki: 1682496993280
GUID: wkkQ*.7Vp1; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1682496993280: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Solaris Service Management Facility (SMF).

### Odpověď (Back)

Solaris Service Management Facility (SMF) je komponenta operačního systému Solaris, která poskytuje jednotné rozhraní pro správu služeb a spouštění systému. Je založena na SMF databází, která obsahuje XML popis služeb,  jejich závislostí a skriptů pro start a zastavení nebo monitorování. Místo runlevels používá milestones. Stojí na \(\mathtt{svc\text.startd}\) a \(\mathtt{svc\text.configd}\) daemonech.

## Poznámka Anki 1682504683207

Karty Anki: 1682504683207
GUID: ev/}U-Kd`x; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1682504683207: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké existují metody vypnutí systému a jak moc jsou korektní?

### Odpověď (Back)

Existují následující metody vypnutí systému:

| 
       | 
      uživatelé | 
      aplikace | 
      systém | 

| 
      \(\mathtt{shutdown \text{ -}i \text{ <}level \text >}\)
 | 
      \(\checkmark\) | 
      \(\checkmark\) | 
      \(\checkmark\) | 

| 
      \(\mathtt{init \text{ <}level \text >}\)
 | 
      ✗ | 
      \(\checkmark\) | 
      \(\checkmark\) | 

| 
      \(\mathtt{poweroff}\), \(\mathtt{restart}\)
 | 
      ✗ | 
      ✗ | 
      \(\checkmark\) | 

| 
      power button
 | 
      ✗ | 
      ✗ | 
      ✗ |

## Poznámka Anki 1684007547145

Karty Anki: 1684007547146
GUID: tY-(W#X]:r; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1684007547146: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište System V typ startu systému.

### Odpověď (Back)

System V typ startu systému stojí na skriptech v adresářích \(\texttt{/etc/rc<milestone>.d}\). V těchto adresářích najdeme dva typy skriptů, které jsou spouštěny při přechodu mezi milestones:

- **start skripty** (jejich jméno začíná na \(\mathtt S\)) - spouští služby,

- **kill skripty** (jejich jméno začíná na \(\mathtt K\)) - ukončují služby.

## Poznámka Anki 1717364979629

Karty Anki: 1717364979629
GUID: P(>R)#WnwT; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1717364979629: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište proces \(\texttt{init}\). Jaký používá konfigurační soubor?

### Odpověď (Back)

Proces \(\texttt{init} \) je prvním spouštěným procesem operačního systému, a je mu tak přířazen process identifier (PID) 1. Jeho hlavním úkolem je pomocí volání funkce \(\texttt{fork}\) při bootu systému spouštět další procesy, proto je také předkem všech procesů, které v operačním systému běží. Navíc se stává přímým rodičem každého orphan procesu, což je proces, jehož rodič skončil dříve než on samotný. Proces \(\texttt{init}\) lze konfigurovat v \(\texttt{/etc/inittab}\).

## Poznámka Anki 1717365332936

Karty Anki: 1717365332936
GUID: PJ3b$3k.1s; štítky: bi-adu::p10 bi-ib::03.

Metadata původního zdroje pro kartu 1717365332936: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište \(\texttt{systemd}\).

### Odpověď (Back)

Programová sada \(\texttt{systemd}\) poskytuje řadu komponent operačních systémů Linux pro bootstrapping, zejména pak obdobu procesu \(\texttt{init}\) v podobě daemonu. Kromě něj umožňuje další funkcionality jako správu přihlašování, síťových spojení nebo logování.

