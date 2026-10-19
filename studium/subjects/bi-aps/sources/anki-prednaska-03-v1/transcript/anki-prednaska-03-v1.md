# BI-APS – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1664839432763

Karty Anki: 1664839432763
GUID: Fx9C`q[bem; štítky: bi-aps::p03 bi-spol::29.

### Otázka (Front)

Co je funkce řadiče?

### Odpověď (Back)

Funkcí řadiče je generovat sekvenci řídicích signálu různým subsystémům počítače ve správném pořadí tak, aby byly vykonány požadované operace (aritmetické, změny toku programu aj.).

## Poznámka Anki 1664839630314

Karty Anki: 1664839630314
GUID: HqnmcSndOv; štítky: bi-aps::p03.

### Otázka (Front)

Jakými způsoby je možné realizovat řadič?

### Odpověď (Back)

**Obvodový řadič**

- kombinační nebo sekvenční obvod
**Mikroprogramový řadič**

- mikroprogram je uložen v paměti řadiče a skládá se z mikroinstrukcí

- každá instrukce ISA je provedena pomocí jedné nebo více mikroinstrukcí

- výhodou je flexibilita

- nevýhodou je složitost a nevhodnost pro zřetězené procesory

## Poznámka Anki 1664839905129

Karty Anki: 1664839905129
GUID: GXfKX/X+]/; štítky: bi-aps::p03 bi-spol::18.

### Otázka (Front)

Jaké existují přístupy pro komunikaci mezi CPU a periferiemi?

### Odpověď (Back)

- paměťově mapované I/O
- izolované (portově mapované) I/O

## Poznámka Anki 1664840034261

Karty Anki: 1664840034261
GUID: g}gs1+#tw,; štítky: bi-aps::p03 bi-spol::18.

### Otázka (Front)

Popište paměťově mapované I/O.

### Odpověď (Back)

- část adresního prostoru je vyhrazena I/O zařízením

- čtení/zápisy na vyhrazené adresy jsou interpretovány jako příkazy nebo přenosy dat pro dané I/O zařízení
- druhy přístupů:

- **centralizovaný přístup** - adresní dekodér řídí přístup k I/O zařízením a paměti

- **autonomní přístup** - při startu počítače jsou inicializovány speciální registry s adresami pro každé I/O zařízení, které reaguje, pouze pokud detekuje shodu adresy na sběrnici a jí přiřazené adresy

## Poznámka Anki 1664840099829

Karty Anki: 1664840099829
GUID: xLTv.S1[lH; štítky: bi-aps::p03 bi-spol::18.

### Otázka (Front)

Popište izolované (portově mapované I/O).

### Odpověď (Back)

- pro komunikaci s I/O zařízeními se využívá separátní adresní prostor
- používá speciální instrukce (např. \(\mathtt{in}\) a \(\mathtt{out}\) pro x86)

