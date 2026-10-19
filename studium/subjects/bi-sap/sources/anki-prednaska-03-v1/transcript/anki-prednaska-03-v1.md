# BI-SAP – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-sap/BI-SAP.apkg; APKG SHA-256 1f67b9282d55c6e8fb096f86041a008a959b3ade7ab78b051bce1ceb2cf0a3bd. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 624f9e0b4061e0e62a0e80089c16bfc9c700ec35ffa2dae8f3cc15f23be9a383.
Původní balíčky: BI-SAP
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1646137007349

Karty Anki: 1646137007350
GUID: mq[=^?6HyZ; štítky: bi-sap::p03 bi-spol::28.

### Otázka (Front)

Definujte sekvenční obvod. Co je jeho matematickým modelem?

### Odpověď (Back)

Sekvenční obvod je logický obvod, jehož výstpy zavísí nejen na kombinaci vstupů, ale i na jejich posloupnosti (sekvenci). Pro implementaci „paměti,“ která slouží pro „uložení“ historie vstupů, se používá zpětná vazba, typicky za pomocí klopného obvodu typu D. Matematickým modelem sekvenčního obvodu je konenčný automat.

## Poznámka Anki 1646137098405

Karty Anki: 1646137098405
GUID: ME51BclXIG; štítky: bi-sap::p03 bi-spol::28.

### Otázka (Front)

Popište rozdíly mezi Mealyho a Mooreovým automatem.

### Odpověď (Back)

Mealyho a Mooreův automat se liší v následujících bodech:      
|       **Mealyho automat** |       **Mooreův automat** |         
|       input-based | state-based
 |         
|         
|       \(\lambda : Q \times X \to Y\)
 |       \(\lambda : Q \to Y\)
 |     
| má přímou vazbu vstupu na výstup | nemá přímou vazbu vstupu na výstup |

## Poznámka Anki 1646137453718

Karty Anki: 1646137453718
GUID: BZ1iOoHKj&; štítky: bi-sap::p03.

Metadata původního zdroje pro kartu 1646137453718: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte předstih, přesah a zpoždění u časování klopného obvodu.

### Odpověď (Back)

[Obrázek: paste-368b0e79b71a28ff551b7aa22ec2f1ecd964b80a.jpg; soubor je v media/ v doprovodném ZIP] 

- **předstih** (setup time) - vstup musí být stabilní před hodinovou hranou
- **přesah **(hold time) - vstup musí zůstat stabilní po hodinové hraně
- **zpoždění** klopného obvodu (clock-to-Q time) - doba mezi přechodem aktuálních dat z D na Q odvozená od aktivní hrany hodin

## Poznámka Anki 1716984980103

Karty Anki: 1716984980104
GUID: D<wNjDNEp&; štítky: bi-sap::p03 bi-spol::28.

### Otázka (Front)

Popište klopný obvod typu D (D flip-flop).

### Odpověď (Back)

Klopný obvod typu D (D flip-flop), je klopný obvod, který realizuje jednobitovou paměť. Funguje tak, že hodnota na vstupu \(D\) je s hodinovým pulzem přenesena na výstup \(Q\).

 [Obrázek: paste-09c5b1c60ac95c57b2489bf08cb01e908cb2a34b.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1717016443450

Karty Anki: 1717016443450
GUID: l-M>>W3B.3; štítky: bi-sap::p03 bi-spol::28.

Metadata původního zdroje pro kartu 1717016443450: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište postup návrhu sekvenčního obvodu.

### Odpověď (Back)

Postup návrhu sekvenčního obvodu je následující:

- původní popis obvodu převedeme na graf přechodů,
- zkonstruujeme pravdivostní tabulky přechodových a výstupních funkcí,
- zvolíme kódování vstupů, výstupů a vnitřních stavů,
- tabulky zakódujeme,
- zakódované tabulky převedeme do Karnaughových map,
- pomocí dvouúrovňové minimalizace nalezneme minimální disjunktivní normální tvar přechodových a výstupních funkcí,

- obvod realizujeme pomocí vybraných hradel,
- vypočteme hodinovou frekvenci.

