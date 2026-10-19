# NI-KOP – Přednáška 11

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1733774137464

Karty Anki: 1733774137464
GUID: C~:KJ9Kt3j; štítky: ni-kop::p11 ni-spol::14.

### Otázka (Front)

Popište schéma, jeho řád a délku.

### Odpověď (Back)

**Schéma **je kódování jedince (chromozom), v němž mají některé proměnné (geny) neurčenou hodnotu. **Řádem schématu** je počet určených proměnných a jeho **délkou** je maximální vzdálenost mezi určenými proměnnými.

## Poznámka Anki 1733774578626

Karty Anki: 1733774578626
GUID: K,O!W$>Ei<; štítky: ni-kop::p11.

### Otázka (Front)

Popište vliv křížení a mutace životnost schémat v genetickém algoritmu.

### Odpověď (Back)

Vliv křížení a mutace na životnost schémat v genetickém algoritmu závisí na následujících parametrech:

- **délka** - delší schémata mají vyšší pravděpodobnost narušení křížením,
- **řád** - schémata vyššího řádu mají vyšší pravděpodobnost narušení mutací.

Z toho vyplývá, že krátká schémata nízkých řádů mají nejvyšší životnost.

## Poznámka Anki 1733774978240

Karty Anki: 1733774978241
GUID: uK^fI4OHwa; štítky: ni-kop::p11 ni-spol::14.

### Otázka (Front)

Popište hypotézu stavebních bloků.

### Odpověď (Back)

Hypotéza stavebních bloků popisuje princip fungování evolučních algoritmů. Podle ní fungují evoluční algoritmy proto, že výsledné kvalitní řešení úlohy skládají z kvalitních řešení menších podúloh (stavebních bloků). V případě evolučních algoritmů je stavební blok definován množinou proměnných kódování jedince (genů), tedy schématem.

## Poznámka Anki 1733775732949

Karty Anki: 1733775732949
GUID: m%lj+-)QBd; štítky: ni-kop::p11 ni-spol::14.

### Otázka (Front)

Popište kompetentní genetický algoritmus. Uveďte příklady.

### Odpověď (Back)

Kompetentní genetický algoritmus je genetický algoritmus, který zachází optimálně i se schématy vyšších řádů. Mezi kompetentní genetické algoritmy patří fast messy genetický algoritmus a vychází z nich Bayesovská optimalizace.

## Poznámka Anki 1733776866525

Karty Anki: 1733776866525
GUID: PF1UHe2f}$; štítky: ni-kop::p11 ni-spol::14.

### Otázka (Front)

Popište fast messy genetický algoritmus.

### Odpověď (Back)

Fast messy genetický algoritmus je kompetentní genetický algoritmus, který namísto jedinců explicitně pracuje se stavebními bloky ve formě schémat. V případě fast messy genetického algoritmu jsou schémata reprezentována seznamem dvojic identifikace proměnné (genu) a hodnota proměnné. Z toho důvodu mohou nastat následující situace:

- **schéma proměnnou nespecifikuje** - proměnná je převzata z nejzdatnějšího (referenčního) jedince,

- **schéma proměnnou specifikuje vícekrát** - použije se první výskyt proměnné ve schématu.
Fast messy genetický algoritmus probíhá tak, že v cyklu iteruje následující kroky, přičemž v každé iteraci je zvýšen řád schémat:

- **primordiální fáze** - generování, filtrace a krácení schémat,

- **juxtapoziční fáze** - spojování, rozdělování a mutace schémat.

## Poznámka Anki 1733778136851

Karty Anki: 1733778136851
GUID: HuxS,,-L:C; štítky: ni-kop::p11 ni-spol::14.

### Otázka (Front)

Popište Bayesovskou optimalizaci.

### Odpověď (Back)

Bayesovská optimalizace vychází z kompetentních genetických algoritmů. Schémata vyšších řádů zohledňuje tak, že pracuje se stochastickým modelem vazeb mezi hodnotami proměnných schémat. Bayesovská optimalizace je nejprve inicializována s náhodnou populací a poté v cyklu iteruje následující kroky:

- je zkonstruován stochastický model závislosti zdatnosti na hodnotách proměnných v aktuální populaci,
- podle tohoto modelu je vygenerována nová populace,
- výsledná populace je sestavena výběrem nejzdatnějších jedinců z obou populací.

