# BI-TAB – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-tab/BI-TAB.apkg; APKG SHA-256 aad5d9418346792a97b103483c6a92411d60f79d52fd5a423fd0fc14dffe748b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 53183dd48468239630c7cf283347984511ecad52b3dee78ea36f4c1d42180eeb.
Původní balíčky: BI-TAB
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1709751019484

Karty Anki: 1709751019485
GUID: K2j>Nh6eHC; štítky: bi-tab::p03.

### Otázka (Front)

Jaké existují časové stupnice (standary času)?

### Odpověď (Back)

Existují následující časové stupnice (standardy času):

- **Universal Time **(UT0, UT1, UT2) - čas založený na rozaci Země;

- **International Atomic Time **(TAI) - vážený průměr časů 450 atomových hodin;

- **Coordinated Universal Time **(UTC) - založen na TAI, používá přestupné sekundy.

## Poznámka Anki 1709751305597

Karty Anki: 1709751305597
GUID: m_`8O/-5=1; štítky: bi-tab::p03.

### Otázka (Front)

Popište přestupnou sekundu.

### Odpověď (Back)

Přestupná sekunda je jednosekundová oprava, která se nepravidelně aplikuje na Coordinated Universal Time (UTC). Jejím cílem je vyrovnat rozdíl mezi časem měřeným atomovými hodinami (International Atomic Time) a časem odvozeným od rotace Země (Universal Time). Tento rozdíl vzniká vlivem zpomalující se zemské rotace.

## Poznámka Anki 1709751545973

Karty Anki: 1709751545973
GUID: CZ%qQ9QJIZ; štítky: bi-tab::p03.

### Otázka (Front)

Jaké existují metody synchronizace času?

### Odpověď (Back)

Existují následující metody synchronizace času:

- **pomocí satelitních systémů** (common-view),
- **pomocí optického vlákna **(ELSTAB),

- **pomocí sítě **(NTP, PTP, White Rabbit),

- **pomocí rádia **(eLoran).

## Poznámka Anki 1709751669972

Karty Anki: 1709751669972
GUID: xN[JgDu2?u; štítky: bi-tab::p03.

### Otázka (Front)

Popište stabilitu a přesnost hodin.

### Odpověď (Back)

**Stabilitou **hodin se rozumí maximální změna relativní frekvence v daném časovém úseku. **Přesnost** hodin vyjadřuje absolutní odchylku od správného času.

## Poznámka Anki 1709754996844

Karty Anki: 1709754996845
GUID: rFi1/!Ev2a; štítky: bi-tab::p03.

### Otázka (Front)

Popište signál pulse-per-second.

### Odpověď (Back)

Pulse-per-second je signál, jehož začátek přesně reprezentuje začátek sekundy. Bývá jedním z výstupů atomových hodin.

## Poznámka Anki 1709755049857

Karty Anki: 1709755049857
GUID: u6A*.C#>TW; štítky: bi-tab::p03.

### Otázka (Front)

Popište synchronizaci a syntonizaci hodin.

### Odpověď (Back)

**Synchronizace **hodin je sjednocení časového údaje dvou hodin, kdežto **syntonizace** je sjednocení jejich frekvence.

## Poznámka Anki 1709755914593

Karty Anki: 1709755914593
GUID: G=gF`Lja&K; štítky: bi-tab::p03.

Metadata původního zdroje pro kartu 1709755914593: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Network Time Protocol (NTP).

### Odpověď (Back)

Network Time Protocol (NTP) je protokol aplikační vrstvy používaný pro synchronizaci hodin. Typicky je implementován pomocí protokolu UDP a používá port 123. Servery provozující NTP se nazývají strata a jsou řazeny hierarchicky dle vzálenosti od atomových hodin. Komunikace protokolu NTP vypadá následovně:

- klient odešle žádost na NTP server,
- NTP server přijme klientovu žádost a začne ji zpracovávat,
- NTP server dokončí zpracování žádosti a odešle odpověď,
- klient přijme odpověď NTP serveru.

V každém z těchto kroků jsou vytvořeny timestampy, z nichž klient následně dokáže spočítat správný způsob úpravy svých hodin.

 [Obrázek: paste-ad778c42e383998a38865147bea05789e8a92fd5.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1709756970567

Karty Anki: 1709756970567
GUID: rEe8ls/}eb; štítky: bi-tab::p03.

### Otázka (Front)

Popište Precision Time Protocol (PTP).

### Odpověď (Back)

Precision Time Protocol (PTP), někdy označován také IEEE 1588, je protokol, který se používá k synchronizaci hodin. Může být implementován na transportní vrstvě pomocí protokolu UDP, ale typicky se využívá na linkové vrstvě, kde dosahuje mnohem vyšší přesnosti. Zakládá se na hardwarové podpoře síťové infrastruktury a používá follow-up paket, který obsahuje data o předchozím paketu. Je postaven na architektuře master/slave, přičemž hodiny slave jsou synchronizovány k hodinám master.

