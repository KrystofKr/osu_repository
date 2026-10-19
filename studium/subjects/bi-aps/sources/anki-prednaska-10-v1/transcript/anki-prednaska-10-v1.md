# BI-APS – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 18 poznámek, 18 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1669044488958

Karty Anki: 1669044488958
GUID: uuh/;y]LEy; štítky: bi-aps::p10 bi-ib::04.

### Otázka (Front)

Popište částečné a úplné překrývání instrukcí.

### Odpověď (Back)

- **částečné překrývání instrukcí**

- Stejný HW prostředek (SP, registry, ALU, ...) se použije jakmile jej předchozí instrukce uvolní.
- Instrukce jsou odděleny v čase, ale ve stejný okamžik je v procesoru zprocesováváno několik instrukcí.
- **časový paralelismus** - **instrukční zřetězení**

- **úplné překrývání instrukcí**

- Instrukce v daný časový okamžik mohou přistupovat ke stejnému HW, nebo používají dedikovaný HW.

- Instrukce jsou odděleny v prostoru a zpracovány paralelně.
- **prostorový paralelismus** - **superskalární architektura**

## Poznámka Anki 1669045284207

Karty Anki: 1669045284207
GUID: Lt>6J_JSlZ; štítky: bi-aps::p10 bi-ib::04.

### Otázka (Front)

Jaký typ paralelismu používá zřetězený, superzřetězený a superskalární procesor. Jak dosahují zrychlení?

### Odpověď (Back)

|       **zřetězený procesor** |       **superzřetězený procesor** |       **superskalární procesor** |         
|       paralelismus v čase (mezi po sobě jdoucími stupni IZ) |       paralelismus v čase (mezi po sobě jdoucími stupni IZ) |       paralelismus v prostoru (mezi paralelními stupni IZ) |         
|       zvyšuje hodinovou frekvenci \(f_{\text{CLK}}\) |       zvyšuje hodinovou frekvenci \(f_{\text{CLK}}\) |       zvyšuje \(\text{IPC}\) |             
|        |       zřetězení s hloubkou \(S > 10\) |        |

## Poznámka Anki 1669051125472

Karty Anki: 1669051125472
GUID: pw)en02Z9_; štítky: bi-aps::p10 bi-ib::04.

### Otázka (Front)

Popište superskalární zřetězení. Co je to šířka zřetězení?

### Odpověď (Back)

- Kombinuje časový a prostorový paralelismus.
- Ve stupni EX je řazeno paralelně více vykonávacích jednotek a to umožňuje současně zpracovávat více instrukcí napříč stupni zřetězení.

- V jednom cyklu lze načíst několik instrukcí, zatímco několik jiných se dekóduje a několik ještě jiných se vykonává ve vykonávacích jednotkách.

- **Šířka zřetězení **označuje počet instrukcí, které mohou být přineseny, dekódovány nebo dokončeny v každém cyklu.

## Poznámka Anki 1669057593639

Karty Anki: 1669057593647
GUID: NAYvv7J&)m; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669057593647: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké problémy má unifikované zřetězení oproti diverzifikovanému?

### Odpověď (Back)

- Každý stupeň instrukčního zřetězení musí podporovat všechny instrukce.
- Rozdílné typy instrukcí požadují rozdílný způsob zpracování. Je obtížné tyto různé požadavky implementovat v unifikovaném instrukčním zřetězení.
- Rozdílnost latencí: Určité typy instrukcí vyžadují složitější zpracování zatímco jiné lze realizovat velmi jednoduše.

## Poznámka Anki 1669057808438

Karty Anki: 1669057808438
GUID: CrEq[vq)?f; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669057808438: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište statickou a dynamickou superskalární mikroarchitekturu.

### Odpověď (Back)

**Statická superskalární mikroarchitektura**

- Paralelně mohou být spuštěny pouze instrukce jdoucí v programu přesně za sebou.
- Pokud jsou mezi těmito instrukcemi závislosti, vede to ke vzniku pozastavení (stalls) a tedy nevyužití předcházejících stupňů instrukčního zřetězení (tzv. rigid pipeline).

**Dynamická superskalární mikroarchitektura**

- Paralelně mohou být spuštěny instrukce připravené k vykonávání bez ohledu na programové pořadí.
- To vede ke vzniku vzájemného předbíhání instrukcí.

## Poznámka Anki 1669058067267

Karty Anki: 1669058067267
GUID: w0VbHuthg[; štítky: bi-aps::p10 bi-ib::04.

### Otázka (Front)

Popište stupně superskalárního instrukčního zřetězení.

### Odpověď (Back)

Superskalární zřetězení se člení na následující stupně:

- **instrukční/dekódovací fronta** (instruction/decode buffer) - fronta načtených instrukcí (mohou být již částečně dekódovány);
- **rozřazovací fronta** (dispatch buffer) - slouží k pozdržení instrukcí, dokud nebudou předány odpovídajícím vykonávacím jednotkám, instrukce do ní přicházejí v programovém pořadí, ale mohou z odcházet v jiném;
- **rezervační stanice** (reservation station) - fronta instrukcí připravených k provedení operace v dané vykonávací jednotce nebo čekajících na forwarding dat;
- **řadící fronta** (reorder buffer) - fronta, která zajistí dokončení instrukcí v programovém pořadí, což je nezbytné pro podporu přesných přerušení (precise exceptions);
- **zápisová fronta** (store buffer) - fronta mezi vykonávacími jednotkami a L1 datovou cache.

## Poznámka Anki 1669058166712

Karty Anki: 1669058166712
GUID: e71Z?1hN.C; štítky: bi-aps::p10 bi-ib::04.

### Otázka (Front)

Vyjmenujte logické stupně superskalárního instrukčního zřetězení a zakreslete je.

### Odpověď (Back)

Superskalární instrukční zřetězení se člení na následující logické stupně:

- načtení instrukcí (instruction fetch),
- dekódování instrukcí (instruction decode),
- rozřazování instrukcí (instruction dispatch),
- vykonávání instrukcí (instruction execute),
- dokončení instrukcí (instruction complete),
- odchod/odbavení instrukcí (instruction retire).

 [Obrázek: paste-0cecf484a64c06e38a1b9a74273ef3a54881c7b1.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1669058265355

Karty Anki: 1669058265355
GUID: N:Kcq?M|{I; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669058265355: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou požadavky na superskalární zřetězení ve stupni načtení instrukcí?

### Odpověď (Back)

Superskalární zřetězení šířky \(W\) musí být schopno v každém cyklu načíst z instrukční SP skupinu \(W\) instrukcí.

## Poznámka Anki 1669058531023

Karty Anki: 1669058531023
GUID: sL:w:rot{f; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669058531023: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište stupeň dekódování instrukcí (instruction decode) superskalárního zřetězení? Jak se v této fázi liší CISC od RISC?

### Odpověď (Back)

Proces dekódování instrukcí zahrnuje:

- identifikaci individuálních instrukcí,
- určení typu konkrétní instrukce,
- detekci meziinstrukčních závislostí mezi instrukcemi, které již byly dekódovány, ale ne rozřazeny.

Pro **CISC** procesory se tato fáze komplikuje tím, že není snadné určit začátek následující instrukce. To vede ke spekulativnímu dekódování.

## Poznámka Anki 1669058692672

Karty Anki: 1669058692672
GUID: r1iJUT~arA; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669058692672: v původním balíčku pozastavená karta.

### Otázka (Front)

K čemu slouží předdekódování ve stupni dekódování instrukcí superskalárního procesoru?

### Odpověď (Back)

Předdekódování zjednodušuje dekódování a umožňuje dekódování více instrukcí současně (odstraní se pozdější spekulativní dekódování) a může poskytnout informace o skokových instrukcích uvnitř načtené skupiny instrukcí.

## Poznámka Anki 1669058883420

Karty Anki: 1669058883420
GUID: r^yV~I?$)D; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669058883420: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte rozřazení instrukcí v superskalárním procesoru.

### Odpověď (Back)

Rozřazení je proces přiřazení instrukce k vykonávací jednotce a její následné zařazení do fronty čekajících instrukcí (do větve instrukčního zřetězení).

## Poznámka Anki 1669059115684

Karty Anki: 1669059115685
GUID: CiO-D7)S(0; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669059115685: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište stupeň rozřazování instrukcí superskalárního procesoru.

### Odpověď (Back)

- Rozřazovací stupeň dočasně ukládá instrukce do rezervačních stanic (RS), které oddělují stupeň dekódování a stupeň vykonávání instrukcí.

- Instrukce v rezervačních stanicích nemusejí mít volné vykonávací jednotky a nemusejí mít připraveny své operandy a tudíž se mohou v rámci dané stanice předbíhat.

## Poznámka Anki 1669059501036

Karty Anki: 1669059501036
GUID: QKea/_cF*9; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669059501036: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište druhy rezervačních stanic.

### Odpověď (Back)

**centralizované/sdílené rezervační stanice**

- dobré využití kapacity - všechny instrukce sdílí všechny prostředky

- náročné na HW
- složitost HW se dá snížit seskupením více vykonávacích větví pod jeden port

**distribuované/dedikované rezervační stanice**

- potenciálně horší využití kapacity, pokud rezervační stanice v některých větvích budou saturovány a jiné budou prázdné
- jednodušší HW

**hybridní rezervační stanice**

- kompromis mezi centralizovaným a distribuovaným přístupem

## Poznámka Anki 1669059665188

Karty Anki: 1669059665188
GUID: Pu||L.3O4!; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669059665188: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to řadící fronta (Reorder Buffer - ROB) ve stupni rozřazování instrukcí superskalárního procesoru.

### Odpověď (Back)

Řadící fronta (Reorder Buffer) obsahuje všechny **in-flight** instrukce (instrukce, které jsou přiřazeny vykonávacím jednotkám, ale nejsou dokončeny) a zajišťuje, že jsou dokončovány pouze v programovém pořadí. Pokud dojde k jejímu zaplnění, nemohou být další instrukce rozřazovány.

## Poznámka Anki 1669059904350

Karty Anki: 1669059904350
GUID: nqm~w`kZ#m; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669059904350: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište vykonávací jednotky superskalárního zřetězení.

### Odpověď (Back)

- Jsou umístěny do samostatných vykonávacích větví instrukčního zřetězení.
- Jsou specializovány na vykonávání instrukcí pouze určitého typu (například specializace na celočíselné aritmetické a logické operace).
- Obecně mají různou latenci.

## Poznámka Anki 1669060266625

Karty Anki: 1669060266625
GUID: inI<z(NG`x; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669060266625: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište stupeň vykonávání instrukcí (instruction execution) superskalárního procesoru.

### Odpověď (Back)

Dle typu instrukcí se ve stupni vykonávání instrukcí (instruction execution) provádějí následující operace:

- **instrukce zapisující do paměti** pokračují do zápisové fronty (store buffer);
- **instrukce čtoucí z paměti** přinášejí data z paměťového subsystému na Common Data Bus, která vede k zápisu do registrů (writeback);
- **instrukce modifikující registry** aktualizují odpovídající rezervační stanice (reservation station), aby instrukce v nich čekající získaly své operandy;
- **všechny instrukce** pokračují do řadící fronty (reorder buffer), kde mění svůj stav na vykonané a čekají na dokončení, přičemž instrukce se stane dokončenou, pokud je nejstarší instrukcí v řadící frontě.

## Poznámka Anki 1669065518724

Karty Anki: 1669065518724
GUID: u6;A8:7Y3; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669065518724: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Tomasulův algoritmus.

### Odpověď (Back)

Tomasulův algoritmus se používá pro eliminaci falešních datových meziinstrukčních závislostí (write after write a write after read) v superskalárním procesoru, které jsou důsledkem nedostatečného počtu architekturálních registrů. Skládá se ze dvou komponent:

- **přejmenování registrů** - výsledky instrukcí zpracovaných out-of-order jsou zapisovány do speciálních skrytých přejmenovaných registrů (rename registers),

- **určení pořadí výpočtu instrukcí** - dle datových závislostí je vytvořeno topologické uspořádání instrukcí.

Namísto programového pořadí jsou tak instrukce vykonávány podle dostupnosti jejich operandů (data-flow execution) a své výsledky ukládají do přejmenovaných registrů. Dodržení programového pořadí instrukcí a přenosu dat z přejmenovaných registrů do architekturálních registrů zajišťuje řadící fronta (reorder buffer).

 [Obrázek: Screenshot 2024-06-07 142224.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1669065678370

Karty Anki: 1669065678370
GUID: g>@0evAUhB; štítky: bi-aps::p10 bi-ib::04.

Metadata původního zdroje pro kartu 1669065678370: v původním balíčku pozastavená karta.

### Otázka (Front)

Kdy jsou instrukce superskalárního procesoru považovány za dokončené (completed) a odbavené (retired)?

### Odpověď (Back)

V obecném případě jsou instrukce považovány za **dokončené** (completed), když je dokončeno jejich vykonávání (opustí stupeň vykonávání instrukcí) a aktualizují architekturální stav procesoru. Nicméně pro instrukce zapisující do paměti platí, že jsou:

- **dokončené** (completed), když zapíšou data do zápisové fronty (write buffer);

- **odbavené **(retired), když se zápis projeví v datové cache.

