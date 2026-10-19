# BI-ADU – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-adu/BI-ADU.apkg; APKG SHA-256 82e24d30673cd0e7a3a5aa4e190d583b7bbdacb9961363822343a47e911816b0. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e4dcf13ba19280a57f78abe30db474a9b8da6ee148ccef4aa2c510acfc892435.
Původní balíčky: BI-ADU
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1681889705128

Karty Anki: 1681889705128
GUID: NxM{M.!}G8; štítky: bi-adu::p09 bi-ib::03.

### Otázka (Front)

Co je to daemon?

### Odpověď (Back)

Daemon je proces, který běží na pozadí operačního systému, a poskytuje funkcionalitu jiným běžícím procesům.

## Poznámka Anki 1681890690860

Karty Anki: 1681890690860
GUID: dNg/UiJ-B$; štítky: bi-adu::p09 bi-ib::02 bi-ib::03.

Metadata původního zdroje pro kartu 1681890690860: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký je rozdíl mezi hard limitem a soft limitem? Jak je lze nastavit?

### Odpověď (Back)

**Hard limit** je nastavován uživatelem \(\mathtt{root}\) a nelze jej přesáhnout. **Soft limit** může běžný uživatel nastavovat jak chce v rozpětí do hard limitu. Nastavovat je můžeme pomocí příkazu \(\mathtt{ulimit}\).

## Poznámka Anki 1681891486559

Karty Anki: 1681891486559
GUID: tHW;bJH={4; štítky: bi-adu::p09 bi-ib::03.

Metadata původního zdroje pro kartu 1681891486559: v původním balíčku pozastavená karta.

### Otázka (Front)

K čemu slouží příkaz \(\mathtt{at}\)?

### Odpověď (Back)

Příkaz \(\mathtt{at}\) slouží k naplánování jednorázového spuštění příkazu ve specifikovaný čas. Naplnánované příkazy najdeme v \(\mathtt{/var/spool/cron/atjobs/\text<jobname\text>}\) na Solarisu a v \(\mathtt{/var/spool/at/\text<jobname\text>}\) na Linuxu a vydrží přes reboot.

## Poznámka Anki 1681892061158

Karty Anki: 1681892061158
GUID: u9n3%=Bdr_; štítky: bi-adu::p09 bi-ib::03.

Metadata původního zdroje pro kartu 1681892061158: v původním balíčku pozastavená karta.

### Otázka (Front)

K čemu slouží příkaz \(\mathtt{crontab}\)?

### Odpověď (Back)

Příkaz \(\mathtt{crontab}\) slouží k plánování periodického spouštění příkazů. Naplánované události se spravují v \(\mathtt{crontab}\) tabulce (na Solarisu \(\mathtt{/var/spool/cron/crontabs/\text<username\text>}\), na Linuxu \(\mathtt{/var/spool/crontab/\text<username\text>}\)) a vydrží přes reboot.

## Poznámka Anki 1681893047434

Karty Anki: 1681893047434
GUID: N_ZLp3qj2h; štítky: bi-adu::p09 bi-ib::02 bi-ib::03.

Metadata původního zdroje pro kartu 1681893047434: v původním balíčku pozastavená karta.

### Otázka (Front)

K čemu slouží diskové kvóty? Jak probíhá jejích konfigurace?

### Odpověď (Back)

Diskové kvóty umožňují nastavit limit na diskový prostor případně počet souborů pro uživatele nebo skupiny. Na tradičních filesystémech se konfigurují ve speciálních konfiguračních souborech, na Zettabyte File System je tato funkcionalita integrovaná.

## Poznámka Anki 1681893292125

Karty Anki: 1681893292125
GUID: fe6x$%<$1b; štítky: bi-adu::p09 bi-ib::10 bi-ib::16.

Metadata původního zdroje pro kartu 1681893292125: v původním balíčku pozastavená karta.

### Otázka (Front)

K čemu slouží příkaz \(\mathtt{chroot}\)?

### Odpověď (Back)

Příkaz \(\mathtt{chroot}\) nastaví kořenový adresář daného programu na určený adresář. Program se tak dá oddělit do separovaného prostředí (sandboxing).

## Poznámka Anki 1682497746163

Karty Anki: 1682497746163
GUID: Ae{098|h3!; štítky: bi-adu::p09.

Metadata původního zdroje pro kartu 1682497746163: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište životní cyklus procesu.

### Odpověď (Back)

[Obrázek: paste-8d9f1633ae129b366752fd6ff571a40d9cdb5b26.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1683797627979

Karty Anki: 1683797628006
GUID: gQDq3M`<y]; štítky: bi-adu::p09 bi-ib::02 bi-ib::03.

Metadata původního zdroje pro kartu 1683797628006: v původním balíčku pozastavená karta.

### Otázka (Front)

Kde najdeme konfiguraci resource limitů?

### Odpověď (Back)

V Solarisu jde o soubor \(\mathtt{/etc/system}\) na Linuxu ji najdeme v \(\mathtt{/etc/security/limits\text.conf}\).

