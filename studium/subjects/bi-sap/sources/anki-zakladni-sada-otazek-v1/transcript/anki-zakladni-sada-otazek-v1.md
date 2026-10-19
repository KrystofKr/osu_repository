# BI-SAP – Základní sada otázek

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-sap/BI-SAP.apkg; APKG SHA-256 1f67b9282d55c6e8fb096f86041a008a959b3ade7ab78b051bce1ceb2cf0a3bd. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 624f9e0b4061e0e62a0e80089c16bfc9c700ec35ffa2dae8f3cc15f23be9a383.
Původní balíčky: BI-SAP
Rozsah: 37 poznámek, 37 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1647985913063

Karty Anki: 1647985913064
GUID: E7XC[o&vk:; štítky: bi-sap::otazky03 bi-spol::28.

Metadata původního zdroje pro kartu 1647985913064: v původním balíčku pozastavená karta.

### Otázka (Front)

Zakreslete obecný model sekvečního obvodu.

### Odpověď (Back)

Obecný model sekvenčního obvodu vypadá následovně:

 [Obrázek: paste-a2bc7e597a739241b4ad1f1317b65e4c56c3604b.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1647985962510

Karty Anki: 1647985962510
GUID: r3@UFGIxTF; štítky: bi-sap::otazky03 bi-spol::28.

### Otázka (Front)

Zakreslete blokovou strukturu obvodů typu Mealy a Moore.

### Odpověď (Back)

Obvody Mealy a Moore mají následující strukturu:

 [Obrázek: paste-b33c97645fb0a0c66a958dbe024512479b6ff31d.jpg; soubor je v media/ v doprovodném ZIP] 

Přičemž \(\texttt{Komb 1}\) realizuje přechodovou funkci \(\delta\), \(\texttt{Komb 2}\) realizuje výstupní funkci \(\lambda \) a \(\texttt{FF}\) označuje klopný obvod typu D.

## Poznámka Anki 1647986798005

Karty Anki: 1647986798005
GUID: u-O`;YJO}:; štítky: bi-sap::otazky03 bi-spol::28.

Metadata původního zdroje pro kartu 1647986798005: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus Quine-McCluskey.

### Odpověď (Back)

Algoritmus Quine-McCluskey slouží podobně jako Karnaughova mapa k minimalizaci Booleovských funkcí. Probíhá ve dvou krocích:

- nalezení všech přímých implikantů,
- nalezení minimálního normálního tvaru pomocí tabulky pokrytí, což zahrnuje nalezení podstatných implikantů a dalších přímých implikantů nutných pro pokrytí dané funkce.

## Poznámka Anki 1648822541057

Karty Anki: 1648822541057
GUID: ks=rOtDb|B; štítky: bi-sap::otazky03 bi-spol::28.

Metadata původního zdroje pro kartu 1648822541057: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte Mealyho a Mooreův automat.

### Odpověď (Back)

Mealyho resp. Mooreův automat je konečný automat, tedy uspořádaná pětice 

\(M = (Q, X, Y, \delta, \lambda)\), případně uspořádaná šestice \(M = (Q, X, Y, \delta, \lambda, q_0)\) je-li iniciální. Liší se v definici výstupní funkce \(\lambda\), kterou definujeme jako:

- \(\lambda: Q \times X \to Y\) pro **Mealyho automat**,
- \(\lambda : Q \to Y\) pro **Mooreův** **automat**.

## Poznámka Anki 1648822708477

Karty Anki: 1648822708477
GUID: bc_.B{@i};; štítky: bi-sap::otazky03 bi-spol::28.

Metadata původního zdroje pro kartu 1648822708477: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte konečný automat a iniciální konečný automat.

### Odpověď (Back)

**Konečný automat** je uspořádaná pětice \(M = (Q, X, Y, \delta, \lambda)\), kde

- \(Q\) je konečná neprázdná množina stavů,

- \(X\) je množina kombinací hodnot vstupních proměnných,

- \(Y\) je množina kombinací hodnot výstupních proměnných,

- \(\delta : Q \times X \to Q\) je přechodová funkce,

- \(\lambda\) je výstupní funkce.

V případě, že má konečný automat určen počáteční stav, nazýváme jej **iniciálním konečným automatem** a definujeme jej jako uspořádanou šestici 

\(M = (Q, X, Y, \delta, \lambda)\), kde

- \(q_0 \in Q\) je počáteční stav.

### Doplňující pole (Extra)

BI-SAP se v některých částech definic automatů Mealy a Moore rozchází s definicemi z BI-AAG. „Konečný automat“ je v BI-SAP používaný ve smylu „zobecněného Mealyho a Moorova automatu“. Podle BI-AAG by bylo možné „konečný automat“ definovat jako uspořádanou pětici \(M = (Q, \Sigma, D, \delta, \lambda, q_0)\), kde:

- \(Q\) je konečná neprázdná množina stavů,
- \(\Sigma\) je konečná množina vstupních symbolů,
- \(D\) je konečná množina výstupních symbolů,
- \(\delta : Q \times \Sigma \to Q\) je přechodová funkce, 
- \(\lambda\) je výstupní funkce (parciální funkci zde nepřipouštíme),
- \(q_0 \in Q\) je počáteční stav.

## Poznámka Anki 1648982950769

Karty Anki: 1648982950769
GUID: i?*!!Zd:zM; štítky: bi-sap::test01.

Metadata původního zdroje pro kartu 1648982950769: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolika transistory je realizován invertor?

### Odpověď (Back)

1

## Poznámka Anki 1648982965954

Karty Anki: 1648982965954
GUID: z%8B(0E[tY; štítky: bi-sap::test01.

Metadata původního zdroje pro kartu 1648982965954: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolika transistory je realizováno hradlo AND?

### Odpověď (Back)

6

## Poznámka Anki 1648982979782

Karty Anki: 1648982979783
GUID: tys%cQ?)lU; štítky: bi-sap::test01.

Metadata původního zdroje pro kartu 1648982979783: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolika transistory je realizováno hradlo OR?

### Odpověď (Back)

6

## Poznámka Anki 1648982987339

Karty Anki: 1648982987339
GUID: m4NTnNp[[l; štítky: bi-sap::test01.

Metadata původního zdroje pro kartu 1648982987339: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolika transistory je realizováno hradlo NOR?

### Odpověď (Back)

4

## Poznámka Anki 1648982992959

Karty Anki: 1648982992959
GUID: O>C]y[/fdu; štítky: bi-sap::test01.

Metadata původního zdroje pro kartu 1648982992959: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolika transistory je realizováno hradlo NAND?

### Odpověď (Back)

4

## Poznámka Anki 1648983016229

Karty Anki: 1648983016229
GUID: py*>;eP|%Y; štítky: bi-sap::test01.

Metadata původního zdroje pro kartu 1648983016229: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolika transistory je realizováno hradlo XOR?

### Odpověď (Back)

14

## Poznámka Anki 1648983026387

Karty Anki: 1648983026387
GUID: BV6J6FKqpI; štítky: bi-sap::test01.

Metadata původního zdroje pro kartu 1648983026387: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolika transistory je realizováno hradlo XNOR?

### Odpověď (Back)

12

## Poznámka Anki 1650361117646

Karty Anki: 1650361117647
GUID: oP)oqS7Q(Z; štítky: bi-sap::otazky10.

Metadata původního zdroje pro kartu 1650361117647: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký další vstup kromě datových musí mít registr s třístavovým výstupem?

### Odpověď (Back)

Ještě řídící vstup - output enable (\(\mathtt{\overline{OE}}\)).

## Poznámka Anki 1650361206534

Karty Anki: 1650361206534
GUID: ncrg`UAgU,; štítky: bi-sap::otazky10.

Metadata původního zdroje pro kartu 1650361206534: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak zakážete přerušení?

### Odpověď (Back)

Při obsluze přerušení je další přerušení zakázáno automaticky. Ručně lze pomocí \(\mathtt{CLI}\).

## Poznámka Anki 1650361232790

Karty Anki: 1650361232790
GUID: G@.XB|t?F7; štítky: bi-sap::otazky10.

Metadata původního zdroje pro kartu 1650361232790: v původním balíčku pozastavená karta.

### Otázka (Front)

Kdy se testuje zda nemá procesor přejít na obsluhu přerušení?

### Odpověď (Back)

Po execute fázi instrukčního cyklu.

## Poznámka Anki 1650361702464

Karty Anki: 1650361702464
GUID: Q8BEXpvRl/; štítky: bi-sap::otazky10.

Metadata původního zdroje pro kartu 1650361702464: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak se zajistí návrat z přerušení zpět do programu, který byl tímto přerušením přerušen? Kde je uložena adresa instrukce, kde se má pokračovat?

### Odpověď (Back)

Návrat z přerušení se realizuje jako běžný návrat z podprogramu (podprogramem je obsluha přerušení), adresa následující instrukce je tedy uložena na zásobníku.

## Poznámka Anki 1650361764348

Karty Anki: 1650361764348
GUID: kd=p0phOT:; štítky: bi-sap::otazky10.

Metadata původního zdroje pro kartu 1650361764348: v původním balíčku pozastavená karta.

### Otázka (Front)

Je možné v průběhu zpracování jednoho přerušení (tedy v podprogramu pro zpracování jednoho přerušení) povolit další přerušení? Jak?

### Odpověď (Back)

Další přerušení ve stávajícím přerušení povolíme pomocí \(\mathtt{SEI}\).

## Poznámka Anki 1650361811304

Karty Anki: 1650361811304
GUID: s-?SZ!D_k~; štítky: bi-sap::otazky10.

Metadata původního zdroje pro kartu 1650361811304: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké instrukce je možné použít, jestliže jsou vstupy a výstupy mapované do paměti (např. pro zjištění hodnoty některého vstupu)?

### Odpověď (Back)

Používají se instrukce \(\mathtt{IN}\) a \(\mathtt{OUT}\).

## Poznámka Anki 1650361944231

Karty Anki: 1650361944231
GUID: hoiUG/f)>i; štítky: bi-sap::otazky10.

Metadata původního zdroje pro kartu 1650361944231: v původním balíčku pozastavená karta.

### Otázka (Front)

Může v kombinačním obvodu realizovaném podle minimální normální formy nastat statický hazard? Proč?

### Odpověď (Back)

Může, protože i v MNDF se mohou vyskytnout nepodstatné implikanty, které zapříčiní větvení realizovaného obvodu.

 [Obrázek: paste-e4571ceecc8baff2c8a511048c95fd45f139f2f2.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1651350300244

Karty Anki: 1651350300244
GUID: d^aa]|{Ej.; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651350300244: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak se pozná správný výsledek při odečítání čísel bez znaménka?

### Odpověď (Back)

Vyjde carry.

## Poznámka Anki 1651350374660

Karty Anki: 1651350374660
GUID: f%Z<4k14X=; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651350374660: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak se získá z nesprávného výsledku správný při odečítání čísel bez znaménka?

### Odpověď (Back)

Výsledek odečteme od nuly, na první bit vložíme 1 a uložíme jej v přímém kódu.

## Poznámka Anki 1651350837747

Karty Anki: 1651350837748
GUID: hSXe17_ldz; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651350837748: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolik registrů a jak velkých a jakého typu potřebujete pro realizaci 6bitové násobičky
(násobenec i násobitel jsou 6bitová nezáporná čísla)?

### Odpověď (Back)

Potřebujeme dva 6bitové registry s paralelním vstupem a paralelním výstupem, 6bitovou sčítačku a jeden až dva posuvné 6bitové registry s možností paralelního zápisu.

## Poznámka Anki 1651351104251

Karty Anki: 1651351104251
GUID: nq)(h=l,&H; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651351104251: v původním balíčku pozastavená karta.

### Text

Řadič procesoru je {{c1::sekvenční}} obvod.

### Back Extra

(prázdné pole)

## Poznámka Anki 1651351207888

Karty Anki: 1651351207888
GUID: reajz4zQV; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651351207888: v původním balíčku pozastavená karta.

### Text

Barrel shifter je {{c1::kombinační}} obvod.

### Back Extra

(prázdné pole)

## Poznámka Anki 1651351237126

Karty Anki: 1651351237126
GUID: cAEf5}VfX{; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651351237126: v původním balíčku pozastavená karta.

### Text

Aritmeticko-logická jednotka (ALU) je {{c1::kombinační}} obvod.

### Back Extra

(prázdné pole)

## Poznámka Anki 1651351282201

Karty Anki: 1651351282201
GUID: xoMhE^!6(9; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651351282201: v původním balíčku pozastavená karta.

### Text

Multiplexor je {{c1::kombinační}} obvod.

### Back Extra

(prázdné pole)

## Poznámka Anki 1651351298145

Karty Anki: 1651351298145
GUID: kJE=qyZh~N; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651351298145: v původním balíčku pozastavená karta.

### Text

Adresový dekodér je {{c1::kombinační}} obvod.

### Back Extra

(prázdné pole)

## Poznámka Anki 1651351314991

Karty Anki: 1651351314991
GUID: Igz%JmRx>H; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651351314991: v původním balíčku pozastavená karta.

### Text

Sčítačka je {{c1::kombinační}} obvod.

### Back Extra

(prázdné pole)

## Poznámka Anki 1651351341497

Karty Anki: 1651351341497
GUID: PCa{J}=MHU; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651351341497: v původním balíčku pozastavená karta.

### Text

Obvod pro rozšíření řádové mřížky z 8 na 16 bitů je {{c1::kombinační}} obvod.

### Back Extra

(prázdné pole)

## Poznámka Anki 1651351361196

Karty Anki: 1651351361196
GUID: usa#lJEuN8; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651351361196: v původním balíčku pozastavená karta.

### Text

Programový čítač je {{c1::sekvenční}} obvod.

### Back Extra

(prázdné pole)

## Poznámka Anki 1651351973509

Karty Anki: 1651351973509
GUID: vb*c9:Z3;*; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651351973509: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakými instrukcemi v jazyce symbolických instrukcí (asembleru) můžete měnit pořadí provádění
instrukcí?

### Odpověď (Back)

\(\mathtt{JMP}\), \(\mathtt{BRxx}\), \(\mathtt{CALL}\), \(\mathtt{RET}\), \(\mathtt{SBxx}\) a další

## Poznámka Anki 1651353484879

Karty Anki: 1651353484879
GUID: bpI_wrH(dF; štítky: bi-sap::test02.

### Otázka (Front)

Jaké jsou základní třídy instruction set architecture (ISA)?

### Odpověď (Back)

Mezi základní třídy instruction set architecture (ISA) patří:

- střadačově orientovaná ISA,
- zásobníkově orientovaná ISA,
- general purpose register (GPR) orientovaná ISA.

## Poznámka Anki 1651353633718

Karty Anki: 1651353633718
GUID: D36P%~raP&; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651353633718: původní příznak autora 6; v původním balíčku pozastavená karta.

### Otázka (Front)

Vysvětlete pojem „registr“ a popište jeho možné funkce.

### Odpověď (Back)

Je to velmi rychlé úložiště dat, které je využíváno procesorem pro dočasné uchování dat, instrukcí a pomocných proměnných.

## Poznámka Anki 1651353930348

Karty Anki: 1651353930348
GUID: nS7^E(hWZR; štítky: bi-sap::test02.

### Otázka (Front)

Jaký je rozdíl mezi nepodmíněným a podmíněným skokem a skokem do podprogramu? Kdy, kam a
co se ukládá?

### Odpověď (Back)

- **nepodmíněný skok** se provede vždy, mění obsah PC
- **podmíněný skok** se provede pokud je splněna podmínka, mění obsah PC
- **skok do podprogramu **se provede vždy, mění obsah PC a na zásobník ukládá návratovou adresu

## Poznámka Anki 1651354033301

Karty Anki: 1651354033302
GUID: u/a&BL%@1L; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651354033302: v původním balíčku pozastavená karta.

### Otázka (Front)

Jsou nějaká omezení na délku skoku (je možné skákat v celém rozsahu paměti programu)? Čím
mohou být případná omezení způsobená?

### Odpověď (Back)

**Nepodmíněné skoky** zpravidla omezené nejsou. Délka **podmíněného skoku** je omezena kódováním instrukcí. Adresa paměti, na kterou se skáče tedy musí být z určitého intervalu.

## Poznámka Anki 1651354988480

Karty Anki: 1651354988480
GUID: v+wKi;c8(@; štítky: bi-sap::test02.

Metadata původního zdroje pro kartu 1651354988480: v původním balíčku pozastavená karta.

### Otázka (Front)

Vysvětlete, co znamená, že je zásobník simulovaný v hlavní paměti. Je takto realizován zásobník
v AVR a je v paměti dat nebo instrukcí?

### Odpověď (Back)

Zásobník není tvořen registry, ale nachází se v paměti. V AVR je zásobník simulovaný v paměti dat.

## Poznámka Anki 1651356279017

Karty Anki: 1651356279017
GUID: jSZ1Mii.6I; štítky: bi-ib::05 bi-sap::test02 bi-spol::29.

### Otázka (Front)

Popište jednotlivé typy pamětí na jednotlivých úrovní paměťové hierarchie včetně jejich řádové doby přístupu a typické kapacity.

### Odpověď (Back)

| 
      typ | 
      typická realizace | 
      doba přístupu | 
      kapacita | 

| 
      registry | 
      klopné obvody | 
      jednotky ns | 
      stovky B | 

| 
      cache | 
      SRAM | 
      10-20 ns | 
      jednotky MB | 

| 
      hlavní | 
      DRAM | 
      50-70 ns | 
      jednotky GB | 

| 
      vnější | 
      pevný disk | 
      5-15 ms | 
      jednotky TB |

