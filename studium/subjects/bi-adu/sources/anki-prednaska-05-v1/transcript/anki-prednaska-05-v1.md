# BI-ADU – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-adu/BI-ADU.apkg; APKG SHA-256 82e24d30673cd0e7a3a5aa4e190d583b7bbdacb9961363822343a47e911816b0. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e4dcf13ba19280a57f78abe30db474a9b8da6ee148ccef4aa2c510acfc892435.
Původní balíčky: BI-ADU
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1679473238246

Karty Anki: 1679473238246
GUID: B3]-V6kI6e; štítky: bi-adu::p05 bi-ib::02.

Metadata původního zdroje pro kartu 1679473238246: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké informace ukládají metadata ve filesystému?

### Odpověď (Back)

Informace popisující umístění dat na disku a atributy souboru (práva, vlastník, časy).

## Poznámka Anki 1679473719226

Karty Anki: 1679473719226
GUID: M:hX{_:(h(; štítky: bi-adu::p05 bi-ib::02.

Metadata původního zdroje pro kartu 1679473719226: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou možné způsoby implementace filesystému?

### Odpověď (Back)

Existují následující způsoby implementace filesystému podle metod alokace datových bloků:

- **alokace souboru pomocí souvislých oblastí datových bloků** (VxFS),
- **alokace souboru po jednotlivých datových blocích**:

- pomocí tabulky (FAT),
- pomocí i-nodů (UFS).

## Poznámka Anki 1679474490623

Karty Anki: 1679474490623
GUID: Es~I!LiAiI; štítky: bi-adu::p05 bi-ib::02.

Metadata původního zdroje pro kartu 1679474490623: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište strukturu filesystému Unix filesystem (UFS).

### Odpověď (Back)

Unix filesystem má následující strukturu:

 [Obrázek: paste-3c0ff7d70da276a9dd7608335430107e390133ab.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1679475434338

Karty Anki: 1679475434338
GUID: l8,DwD4n;O; štítky: bi-adu::p05 bi-ib::02.

Metadata původního zdroje pro kartu 1679475434338: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakými příkazy lze vytvářet nový filesystém?

### Odpověď (Back)

Nový filesystém lze vytvořit pomocí příkadu \(\mathtt{newfs}\) na Solarisu a pomocí \(\mathtt{mkfs}\) na Linuxu.

## Poznámka Anki 1679475765552

Karty Anki: 1679475765552
GUID: O#Vil!M2<f; štítky: bi-adu::p05 bi-ib::02.

Metadata původního zdroje pro kartu 1679475765552: v původním balíčku pozastavená karta.

### Otázka (Front)

Kde najdeme záznamy o připojených discích?

### Odpověď (Back)

Záznamy o připojených discích najdeme v souboru \(\mathtt{/etc/mnttab}\) na Solarisu a \(\mathtt{/etc/mtab}\) na Linuxu.

## Poznámka Anki 1679476411270

Karty Anki: 1679476411270
GUID: s=o!J]L(3&; štítky: bi-adu::p05 bi-ib::02.

Metadata původního zdroje pro kartu 1679476411270: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to \(\mathtt{fsck}\)?

### Odpověď (Back)

Utilita \(\mathtt{fsck}\) (file system consistency check) v několika průchodech opravuje nekonzistence filesystému. Umí nahradit superblock záložní verzí nebo obnovit soubory po chybě i-node tabulky. Spouští se automaticky, pokud je disk při bootu dirty.

## Poznámka Anki 1679477191099

Karty Anki: 1679477191099
GUID: u{|e(/-^d?; štítky: bi-adu::p05 bi-ib::02.

Metadata původního zdroje pro kartu 1679477191099: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak funguje UFS snapshot?

### Odpověď (Back)

Snapshot slouží k zapamatování stavu filesystému. Pomocí příkazu \(\mathtt{fssnap}\) lze definovat "děravý" soubor (ideálně na jiném filesystému), kam se kopíruje původní stav. Vytvoří se tím i speciální soubor, který lze připojit příkazem \(\mathtt{mount}\).

## Poznámka Anki 1679482894329

Karty Anki: 1679482894329
GUID: c_:/FzETol; štítky: bi-adu::p05 bi-ib::02.

### Otázka (Front)

Popište redundant array of independent disks (RAID) a jeho verze.

### Odpověď (Back)

RAID (redundant array of independent disks) je řešení, které kombinuje vícero disků do jednoho virtuálního a poskytuje výhody jako zvýšení kapacity, bezpečnosti nebo výkonu. Existují následující verze RAID:

- **RAID 0** (skládání):

- concatenation - disky jsou řazeny za sebe,

- striping - disky jsou řazeny vedle sebe,

- **RAID 1** (zrcadlení);

- **RAID 0+1 **a **RAID 1+0 **(kombinace stripe a mirror nebo mirror a stripe);

- **RAID 2** (stripe po bitech, Hammingův kód);

- **RAID 3 **(stripe po bytech, dedikovaný paritní disk);

- **RAID 4 **(stripe po blocích, dedikovaný paritní disk);

- **RAID 5 **(stripe po blocích, distribuovaná parita);

- **RAID 6** (stripe po blocích, dvě distribuované parity).

## Poznámka Anki 1683798432109

Karty Anki: 1683798432109
GUID: D$q,2VO}4x; štítky: bi-adu::p05 bi-ib::02.

Metadata původního zdroje pro kartu 1683798432109: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to loop file interface (LOFI)? Jaká jsou jeho využití?

### Odpověď (Back)

Loop file interface (LOFI), někdy pouze loop device, je pseudo zařízení, které umožní interpretovat obyčejný soubor jako blokové zařízení. Na tomto zařízení pak můžeme např. vytvořit filesystém, případně jej využijeme u ISO souborů.

## Poznámka Anki 1683798570915

Karty Anki: 1683798570915
GUID: pJxu?N<#0O; štítky: bi-adu::p05 bi-ib::02.

Metadata původního zdroje pro kartu 1683798570915: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to Loopback File System (LOFS)? Kde se využívá?

### Odpověď (Back)

Loopback File System (LOFS) je technologie operačních systémů Solaris, která umožňuje vytvořit virtuální filesystém. Tento filesystém potom funguje jako odkaz na jiný již existující filesystém a umožňuje k němu přistupovat alternativní cestou. Využíván je např. u neglobální sparse Solaris zóny, která implicitně mountuje některé systémové adresáře globální zóny jako read-only LOFS.

## Poznámka Anki 1683808392995

Karty Anki: 1683808392996
GUID: f<xkpa+~3`; štítky: bi-adu::p05 bi-ib::03.

Metadata původního zdroje pro kartu 1683808392996: v původním balíčku pozastavená karta.

### Otázka (Front)

Z jakých částí se skládá logovací systém?

### Odpověď (Back)

Logovací systém se typicky skládá z následujících částí:

- **logovací daemon **- proces, který sbírá zprávy od ostatních běžících programů a zapisuje je do logu (nejčastěji \(\mathtt{syslogd}\), který lze konfigurovat v \(\mathtt{/etc/syslog\text.conf}\));
- **logovací soubory** - soubory, do kterých jsou zapisovány logovací zprávy (nejčastěji v adresáři \(\mathtt{/var}\));

- **systém rotace logů** - periodicky odstraňuje či přesouvá staré logovací soubory (zabraňuje se tak čerpání přiliš velké diskové kapacity).

## Poznámka Anki 1684006110871

Karty Anki: 1684006110871
GUID: P81xi/,V-J; štítky: bi-adu::p05 bi-ib::02.

Metadata původního zdroje pro kartu 1684006110871: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to write hole?

### Odpověď (Back)

Write hole je typ chyby, která může nastat na RAID discích při náhlém výpadku napájení. Způsobí, že nedojde k dokončení zápisu celého stripe a následně není možné určit, které bloky byly zapsány a které ne. Navíc pravděpodobně dojde k nekonzistenci parity a nelze určit, který blok paritu narušuje, či jestli je samotná parita špatně.

## Poznámka Anki 1687875421751

Karty Anki: 1687875421751
GUID: C>Z>?,c,U:; štítky: bi-adu::p05.

Metadata původního zdroje pro kartu 1687875421751: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to journaling filesystem?

### Odpověď (Back)

Journaling filesystem je filesystém, který do speciální oblasti journal zapisuje záznamy o plánovaných transakcích. Poté co dojde k jejich úspěšnému provedení, jsou z journalu zase odebrány. Pokud se filesystém dostane do nekonzistentního stavu, stačí přehrát operace z journalu.

