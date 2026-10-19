# BI-SAP – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-sap/BI-SAP.apkg; APKG SHA-256 1f67b9282d55c6e8fb096f86041a008a959b3ade7ab78b051bce1ceb2cf0a3bd. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 624f9e0b4061e0e62a0e80089c16bfc9c700ec35ffa2dae8f3cc15f23be9a383.
Původní balíčky: BI-SAP
Rozsah: 15 poznámek, 15 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1650356630610

Karty Anki: 1650356630611
GUID: f(nsjH]IdN; štítky: bi-sap::p10.

Metadata původního zdroje pro kartu 1650356630611: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to přerušení?

### Odpověď (Back)

- původně byla obsluha V/V zařízení řízena procesorem
- nyní je obsluha nezávislá na procesoru z důvodu rychlosti
- přerušení vzniká z nutnosti synchronizace, upozornění V/V zařízení na své požadavky

## Poznámka Anki 1650356715933

Karty Anki: 1650356715934
GUID: li!:D;el1$; štítky: bi-sap::p10 bi-spol::29.

Metadata původního zdroje pro kartu 1650356715934: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Jaká rozlišujeme přerušení?

### Odpověď (Back)

- **vnější** (periferie, uživatel)

- nemaskovatelná (NMI)
- maskovatelná (z řadicě přerušení)

- **vnitřní**

- chyby operandů, výsledků, krokování
- instrukce \(\mathtt{INT}\)

## Poznámka Anki 1650356903523

Karty Anki: 1650356903523
GUID: yU2|nwarMv; štítky: bi-ib::04 bi-sap::otazky10 bi-sap::p10 bi-spol::29.

Metadata původního zdroje pro kartu 1650356903523: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište postup při obsluze přerušení.

### Odpověď (Back)

1. na zásobník se uloží informace o probíhajícím programu (SREG, PC)
2. zakáží se další přerušení
3. PC se nastaví na začátek programu obsluhy přerušení
4. provede se přerušení
5. proběhne návrat z programu obsluhy přerušení k původnímu programu a obnova původního stavu (SREG, PC)

## Poznámka Anki 1650356977801

Karty Anki: 1650356977801
GUID: H;QR5B3i3U; štítky: bi-sap::p10.

Metadata původního zdroje pro kartu 1650356977801: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak funguje maskování přerušení?

### Odpověď (Back)

Probíhá pomocí nastavení příznaku I v SREG.

- polovení pomocí \(\mathtt{SEI}\)
- zakázání pomocí \(\mathtt{CLI}\)

## Poznámka Anki 1650357025745

Karty Anki: 1650357025745
GUID: O,O)#]>wPw; štítky: bi-sap::p10.

Metadata původního zdroje pro kartu 1650357025745: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to vektor přerušení?

### Odpověď (Back)

Vektor přerušení obsahuje adresu podprogramu obsluhy přerušení.

## Poznámka Anki 1650357080308

Karty Anki: 1650357080308
GUID: l+q~`:T|!s; štítky: bi-ib::04 bi-sap::otazky10 bi-sap::p10 bi-spol::29.

Metadata původního zdroje pro kartu 1650357080308: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to řadič přerušení? Má AVR takový řadič?

### Odpověď (Back)

Je to hardwarové zařízení přijímající signály z V/V zařízení, identifkuje IRQ (Interrupt Request) a generuje přerušovací signál.
AVR řadič přerušení neobsahuje.

## Poznámka Anki 1650357405808

Karty Anki: 1650357405808
GUID: hwQ9XUt6i`; štítky: bi-sap::p10.

Metadata původního zdroje pro kartu 1650357405808: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to hazard?

### Odpověď (Back)

Hazard je krátká neočekávaná změna výstupního signálu.

## Poznámka Anki 1650357494732

Karty Anki: 1650357494732
GUID: .$DF,n8>f; štítky: bi-sap::otazky10 bi-sap::p10.

Metadata původního zdroje pro kartu 1650357494732: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to statický hazard a čím je způsobený?

### Odpověď (Back)

Statický hazard nastává, když má výstup být trvale v \(0\) nebo \(1\), ale místo toho se objeví krátká změna do opačné úrovně.
Vzniká když se signál šíří různými, ale konvergujícími cestami.

## Poznámka Anki 1650357566090

Karty Anki: 1650357566090
GUID: I&pN1kV)wI; štítky: bi-sap::otazky10 bi-sap::p10.

Metadata původního zdroje pro kartu 1650357566090: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je statický hazard v jedničce a co v nule?

### Odpověď (Back)

Je to krátká změna do opačné úrovně.

 [Obrázek: paste-1aae5e4d997b3da89b0facc74b364a376a132306.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1650357929580

Karty Anki: 1650357929580
GUID: pXp-Ago_58; štítky: bi-sap::otazky10 bi-sap::p10.

Metadata původního zdroje pro kartu 1650357929580: v původním balíčku pozastavená karta.

### Otázka (Front)

Kdy statický hazard vadí a jak se ho vyvarovat?

### Odpověď (Back)

- v **kombinačních obvodech** nejsou hazardy kritické, po určité době se výstup vždy ustálí ve správných hodnotách
- v **sekvenčních obvodech** mohou přivést klopný obvod do nesprávného stavu; řešením je synchronní návrh a správný výpočet maximální hodinové frekvence

## Poznámka Anki 1650358984755

Karty Anki: 1650358984755
GUID: LLydjs:R=4; štítky: bi-sap::p10.

### Otázka (Front)

Co je to sběrnice (Bus)?

### Odpověď (Back)

Sběrnice je soubor vodičů a pravidel určených k propojení jednotek počítače a přenos signálů mezi nimi.

## Poznámka Anki 1650359448357

Karty Anki: 1650359448358
GUID: E.?<48m6{b; štítky: bi-sap::p10.

Metadata původního zdroje pro kartu 1650359448358: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké rozlišujeme typy sběrnic?

### Odpověď (Back)

- paralelní
- sériové (používají se pro systémové účely nebo jako záloha)

- jednosměrně řízené (řídící jednotka nečeká na potvrzení příkazu k provedení operace)
- obousměrně řízené

- synchronní (řízená hodinami)
  
- pseudosynchronní (obousměrné řízení, hodiny a speciální signály)
  
- asynchronní (obousměrné řízení)

## Poznámka Anki 1650359802007

Karty Anki: 1650359802007
GUID: NkR+;kdN>3; štítky: bi-sap::p10.

Metadata původního zdroje pro kartu 1650359802007: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to handshake?

### Odpověď (Back)

Je to způsob komunikace na asynchronní sběrnici (korespondenční režim).
Funguje ve dvou fázích:

- žádost (RQ)
- potvrzení (ACK)

## Poznámka Anki 1650359973692

Karty Anki: 1650359973693
GUID: p99ot[vE<}; štítky: bi-sap::otazky10 bi-sap::p10.

Metadata původního zdroje pro kartu 1650359973693: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou základní parametry sběrnic?

### Odpověď (Back)

- šířka přenosu - počet bitů, které lze po sběrnici přenést najednou [bit]
- frekvence - maximální frekvence, se kterou může sběrnice pracovat [Hz]
- rychlost přenosu - počet slabik přenesených za jednotku času [B/s]

## Poznámka Anki 1650360036414

Karty Anki: 1650360036414
GUID: oc>6I[]CwA; štítky: bi-sap::p10.

Metadata původního zdroje pro kartu 1650360036414: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké rozlišujeme způsoby přidělování sběrnic?

### Odpověď (Back)

- centralizované - pomocí přidělovače sběrnice (často procesor)
- distribuované - bez přidělovače

