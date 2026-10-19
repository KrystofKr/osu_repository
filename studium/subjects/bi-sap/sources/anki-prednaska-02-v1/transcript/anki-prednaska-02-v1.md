# BI-SAP – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-sap/BI-SAP.apkg; APKG SHA-256 1f67b9282d55c6e8fb096f86041a008a959b3ade7ab78b051bce1ceb2cf0a3bd. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 624f9e0b4061e0e62a0e80089c16bfc9c700ec35ffa2dae8f3cc15f23be9a383.
Původní balíčky: BI-SAP
Rozsah: 19 poznámek, 19 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1645569579859

Karty Anki: 1645569579860
GUID: Gz2U6+dFH_; štítky: bi-sap::p02 bi-spol::28.

### Otázka (Front)

Definujte kombinační obvod. Co je jeho matematickým modelem?

### Odpověď (Back)

Kombinační obvod je logický obvod, jehož výstupy jsou určeny kombinací vstupů. Jeho matematickým modelem je Booleova algebra, konkrétně logická funkce.

## Poznámka Anki 1645569643863

Karty Anki: 1645569643863
GUID: I,+v~}1q>;; štítky: bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1645569643863: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte Booleovskou krychli, onset a offset.

### Odpověď (Back)

**Booleovská krychle** se používá pro vyjádření Booleovských funkcí. Rozumí se jí literál nebo logický součin literálů. To znamená, že krychle může být množinou právě \(2^k\), \(k \in \mathbb N_0\) vrcholů jednotkové krychle. Konkrétně funkci
\[f(z, y, x) = z \overline y x + \overline z \overline y x = \overline y x(z + \overline z) = \overline y  x\]vyjádříme v \(B^3\) jako

 [Obrázek: paste-3aef244c23f766e4b065f39a30d35fda9b54daa0.jpg; soubor je v media/ v doprovodném ZIP] 

Každý vrchol, pro který je \(f\) pravdivá a v \(B^3\) je značen pomocí \(\bullet\), nazýváme **onset**. Ostatní vrcholy nazýváme **offsety**. Nicméně v obecném případě může být pro vyjádření Booleovské funkce potřeba kombinace vícero Booleovských krychlí.

## Poznámka Anki 1645569887916

Karty Anki: 1645569887916
GUID: hd-oI:.M0*; štítky: bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1645569887916: v původním balíčku pozastavená karta.

### Otázka (Front)

Kdy je Booleovská krychle implikantem a mintermem Booleovské funkce?

### Odpověď (Back)

Booleovská krychle \(C\) je **implikantem **Booleovské funkce \(f\), je-li podmnožinou množiny jejích onsetů. **Mintermem** funkce \(f\) je \(C\) tehdy, pokud je jejím implikantem a obsahuje všechny proměnné, které se v \(f\) vyskytují. Konkrétně pro funkci
\[f(z, y, x) = z \overline y x + \overline z \overline y x = \overline y x(z + \overline z) = \overline y  x\]kterou lze vyjádřit v \(B^3\) jako

 [Obrázek: paste-3aef244c23f766e4b065f39a30d35fda9b54daa0.jpg; soubor je v media/ v doprovodném ZIP] 

platí, že:

- krychle \(z \overline y x\) a \(\overline z \overline y x\) (tedy oba onsety zvlášť) jsou mintermy (a zároveň implikanty) \(f\),
- krychle \(\overline y x\) (tedy kombinace obou onsetů) je implikant \(f\).

## Poznámka Anki 1645570178807

Karty Anki: 1645570178807
GUID: j+_SjSaS=a; štítky: bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1645570178807: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte pokrytí.

### Odpověď (Back)

Pokrytí je množina Booleovských krychlí, které popisují konkrétní Booleovskou funkci.

## Poznámka Anki 1645570253952

Karty Anki: 1645570253952
GUID: L81S1V_?n~; štítky: bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1645570253952: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte neredundantní Booleovskou krychli.

### Odpověď (Back)

Booleovská krychle je neredundantní, jestliže po jejím odstranění z množiny krychlí popisujících konkrétní Booleovskou funkci nebudou pokryty všechny onsety.

## Poznámka Anki 1645570315838

Karty Anki: 1645570315838
GUID: F/1|K[3$2I; štítky: bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1645570315838: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte přímý literál a přímou Booleovskou krychli.

### Odpověď (Back)

**Literál** Booleovské krychle \(C\) je přímý, jestliže jeho odstraněním z \(C\) vznikne krychle \(C'\) pokrývající nějaký offset. V důsledku toho nejsou funkce pokrývané \(C\) a \(C'\) logicky ekvivalentní. **Booleovskou krychli** nazveme přímou, jestliže jsou všechny její literály přímé.

## Poznámka Anki 1645570344895

Karty Anki: 1645570344895
GUID: g=?H~F2~?(; štítky: bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1645570344895: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte podstatnou Booleovskou krychli.

### Odpověď (Back)

Booleovská krychle je podstatná, jestliže obsahuje onset (minterm), který není obsažen v jiné přímé krychli.

## Poznámka Anki 1647968926529

Karty Anki: 1647968926530
GUID: lGhx?8-dv/; štítky: bi-sap::otazky02 bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1647968926530: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaká existují kanonická vyjádření Booleovských funkcí?

### Odpověď (Back)

Existují následující kanonická vyjádření Booleovských funkcí:

- pravdivostní tabulka,
- úplný DNT a KNT,
- Karnaughova mapa,
- Booleovská krychle.

## Poznámka Anki 1647969495636

Karty Anki: 1647969495637
GUID: x_H5-J@0.n; štítky: bi-sap::otazky02 bi-sap::p02 bi-spol::28.

### Otázka (Front)

Definujte Booleovu algebru.

### Odpověď (Back)

Booleova algebra je struktura \(\{ B, +, \cdot, \neg, 0, 1 \}\), kde

- \(B\) je neprázdná množina (nosič algebry),

- \(+\), \(\cdot\) jsou binární operace na \(B\),

- \(\neg\) je unární operace na \(B\),

- \(0\), \(1\) jsou nulární operace na \(B\)

a kde dále platí základní axiomy (komutativita, distributivita, zákon vyloučeného třetího a další).

## Poznámka Anki 1648815799070

Karty Anki: 1648815799070
GUID: NJ*@WW6G0{; štítky: bi-sap::otazky02 bi-sap::p02.

Metadata původního zdroje pro kartu 1648815799070: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to onset, resp. offset?

### Odpověď (Back)

Je to množina vrcholů nabývající hodnoty 1, resp. 0.

## Poznámka Anki 1648815997401

Karty Anki: 1648815997401
GUID: u@#&Br)hxB; štítky: bi-sap::otazky02 bi-sap::p02.

Metadata původního zdroje pro kartu 1648815997401: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký je rozdíl mezi proměnnou a literálem?

### Odpověď (Back)

Proměnná může měnit svou hodnotu, kdežto hodnota literálu je pevně dána.

## Poznámka Anki 1648816795666

Karty Anki: 1648816795666
GUID: g?zvF4D@Bj; štítky: bi-sap::otazky02 bi-sap::p02.

Metadata původního zdroje pro kartu 1648816795666: v původním balíčku pozastavená karta.

### Otázka (Front)

Mějme booleovskou \(n\)-krychli.

- Kolik má vrcholů?
- Kolik má proměnných?
- Kolik je literálů?
- Kolik je všech logických formulí?

### Odpověď (Back)

Booleovská \(n\)-krychle má:

- \(2^n\) vrcholů,

- \(n\) proměnných,

- \(2n\) literálů,

- \(\infty\) logických formulí.

## Poznámka Anki 1648818016763

Karty Anki: 1648818016764
GUID: G=N@fenz:^; štítky: bi-sap::otazky02 bi-sap::p02.

Metadata původního zdroje pro kartu 1648818016764: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolik existuje různých logických funkcí pro \(n\) proměnných?

### Odpověď (Back)

\(2^{2^n}\)

## Poznámka Anki 1648818831138

Karty Anki: 1648818831138
GUID: C2]<DTk0MP; štítky: bi-sap::otazky02 bi-sap::p02.

Metadata původního zdroje pro kartu 1648818831138: v původním balíčku pozastavená karta.

### Otázka (Front)

Zapište zákony absorpce a absorpce negace.

### Odpověď (Back)

\(x+x\cdot y=x\)
\(x\cdot(x+y)=x\)
\(x+\overline x\cdot y = x+y\)
\(x\cdot(\overline x+y)=x\cdot y\)

## Poznámka Anki 1648819722245

Karty Anki: 1648819722245
GUID: {ff^+yuqA; štítky: bi-sap::otazky02 bi-sap::p02.

Metadata původního zdroje pro kartu 1648819722245: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to přímý implikant funkce \(f\)?

### Odpověď (Back)

Je to takový implikant logické funkce \(f\), který již nelze zjednodušit.

## Poznámka Anki 1717000504208

Karty Anki: 1717000504209
GUID: v/.wDc&BAO; štítky: bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1717000504209: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište dvouúrovňovou minimalizaci.

### Odpověď (Back)

**Dvouúrovňová minimalizace** je proces hledání minimálního pokrytí Booleovské funkce. Takové pokrytí je tvořeno co nejmenším počtem Booleovských krychlí co největších velikostí. Čím menší bude pokrytí dané funkce, tím úspornější bude fyzická realizace obvodu pomocí hradel.

## Poznámka Anki 1717000952057

Karty Anki: 1717000952057
GUID: HE|3t[;@Af; štítky: bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1717000952057: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište realizaci kombinačních a sekvenčních obvodů.

### Odpověď (Back)

Realizace kombinačních a sekvenčních obvodů spočívá v minimalizaci Booleovské funkce, která daný obvod popisuje, a její následné konstrukci pomocí hradel. Z Shannonova expanzního teorému víme, že \(\{ \land, \lor, \neg \}\) tvoří univerzální systém logických spojek, nicméně samostatné systémy tvoří také spojky NAND a NOR. Ty se při realizaci obvodů používají nejčastěji, neboť hradla, která je implementují, využívají nejmenší počet tranzistorů a zabírají tak nejmenší plochu. Cílová realizace se však může odvíjet od dalších parametrů jako je rychlost obvodu, rychlost návrhu a realizace nebo testovatelnost.

## Poznámka Anki 1717016225507

Karty Anki: 1717016225507
GUID: f]M~+1//}d; štítky: bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1717016225507: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište postup návrhu kombinačního obvodu.

### Odpověď (Back)

Postup návrhu kombinačního obvodu je následující:

- původní popis obvodu převedeme do Karnaughovy mapy,
- pomocí dvouúrovňové minimalizace nalezneme minimální disjunktivní normální tvar Booleovské funkce popisující obvod,
- obvod realizujeme pomocí vybraných hradel.

## Poznámka Anki 1718103650691

Karty Anki: 1718103650691
GUID: A[(qNEB!~i; štítky: bi-sap::p02 bi-spol::28.

Metadata původního zdroje pro kartu 1718103650691: v původním balíčku pozastavená karta.

### Otázka (Front)

Zakreslete Karnaughovu mapu pro tři a čtyři proměnné.

### Odpověď (Back)

Karnaughova mapa pro **tři **proměnné vypadá následovně:

 [Obrázek: paste-4cffab2dd204ef0e34a7d97f9560606942cb2d21.jpg; soubor je v media/ v doprovodném ZIP] 

Karnaughova mapa pro **čtyři **proměnné vypadá následovně:

 [Obrázek: paste-68a0d7ff9719d86eaf2ace8a26852260dd864331.jpg; soubor je v media/ v doprovodném ZIP]

