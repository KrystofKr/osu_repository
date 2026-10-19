# BI-ZUM – 02 evolucni vypocty

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 17 poznámek, 17 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610554

Karty Anki: 1785298610554
GUID: e^|`iCu<kQ; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_052-054 src_058-060.

### Otázka (Front)

Co jsou evoluční algoritmy, proč používají populaci a jak probíhá jejich generační cyklus?

### Odpověď (Back)

Jde o stochastické populační optimalizační metody inspirované evolucí. Populace současně pokrývá více oblastí, dovoluje výměnu dílčí informace a snižuje závislost na jediné lokální trajektorii.

**Cyklus:** inicializace populace → vyhodnocení fitness → selekce rodičů → reprodukce (křížení a mutace) → vyhodnocení potomků → náhrada části či celé populace → opakování.

**Pojmy:** jedinec = kandidátní řešení; populace = soubor jedinců; generace = jeden cyklus. Selekce vybírá rodiče, reprodukce tvoří potomky a náhrada určuje příští populaci. Mutace mění jednoho jedince, křížení kombinuje více rodičů.

## Poznámka Anki 1785298610555

Karty Anki: 1785298610555
GUID: f~:f8),,{y; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_055-057 src_061.

### Otázka (Front)

Co jsou genotyp, fenotyp a fitness a proč musejí evoluční operátory respektovat reprezentaci?

### Odpověď (Back)

**Genotyp** je reprezentace, s níž pracují operátory (bitový řetězec, reálný vektor, strom, automat…). **Fenotyp** je význam či realizované chování genotypu; různé genotypy mohou mít stejný nebo podobný fenotyp. **Fitness** měří kvalitu/adaptaci řešení.

Operátory musí pro danou reprezentaci vytvářet smysluplné a pokud možno přípustné potomky: bitová inverze funguje pro bity, ale ne automaticky pro permutace, stromy či jiné omezené struktury.

## Poznámka Anki 1785298610556

Karty Anki: 1785298610556
GUID: bx!jl9/J?V; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_062-065.

### Otázka (Front)

Co charakterizuje klasický genetický algoritmus a jak probíhá generace a inicializace?

### Odpověď (Back)

Klasický **GA** optimalizuje fitness nad chromozomy pevné délky, typicky x ∈ {0,1}ⁿ, pomocí selekce, křížení a mutace. V generaci se opakovaně vyberou rodiče, vytvoří a zmutují potomci, potomci se vyhodnotí a požadovaný počet z nich nahradí původní populaci.

**Neinformovaná inicializace:** náhodná, univerzální a obvykle diverzní. **Informovaná inicializace:** používá heuristiky či dřívější řešení; může zrychlit začátek, ale také zmenšit diverzitu a uzavřít populaci v lokální oblasti.

## Poznámka Anki 1785298610557

Karty Anki: 1785298610557
GUID: OUrPMH/2)!; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_066-069.

### Otázka (Front)

Jak funguje ruletová a turnajová selekce a jak ovlivňují selekční tlak?

### Odpověď (Back)

**Ruleta:** pro nezáporné fitness pᵢ=fᵢ/Σⱼfⱼ. Je citlivá na měřítko a posun fitness, vyžaduje platné nezáporné váhy a extrémní jedinci mohou vytvořit příliš silný tlak.

**Turnaj:** náhodně se vybere k jedinců a zvítězí nejlepší; záleží na pořadí, ne na absolutním měřítku. Větší k zvyšuje tlak a exploataci, menší k zachovává více náhody a diverzity.

## Poznámka Anki 1785298610558

Karty Anki: 1785298610558
GUID: M$t$AM|,Ci; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_070-071 src_112-114.

### Otázka (Front)

Jak funguje bit-flip mutace a jak volba či změna míry mutace ovlivňuje evoluci?

### Odpověď (Back)

Každý bit se nezávisle invertuje s pravděpodobností p<sub>m</sub>; v chromozomu délky n se očekává n·p<sub>m</sub> změněných bitů.

**Příliš vysoká/velká mutace** ničí užitečné stavební bloky a blíží hledání náhodnému vzorkování. **Příliš nízká** vytváří málo nové informace, zhoršuje únik z lokálních optim a podporuje předčasnou konvergenci. Proto lze míru měnit: zpočátku větší změny pro exploraci, později menší pro doladění; řízení může záviset na čase nebo úspěšnosti mutací.

## Poznámka Anki 1785298610559

Karty Anki: 1785298610559
GUID: k(UoBfqtRL; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_072-075.

### Otázka (Front)

Jak fungují hlavní druhy křížení binárních chromozomů a kdy standardní křížení nepoužít?

### Odpověď (Back)

- **Jednobodové:** potomek kombinuje prefix jednoho a suffix druhého rodiče.
- **Dvou-/n-bodové:** mezi body řezu se střídají celé úseky rodičů.
- **Uniformní:** rodič se volí samostatně pro každou pozici; méně zachovává souvislé bloky.
Křížení je vhodné vynechat nebo nahradit specializovanou rekombinací, pokud narušuje význam kódu nebo často tvoří neplatná řešení; evoluce může pracovat jen s mutací.

## Poznámka Anki 1785298610560

Karty Anki: 1785298610560
GUID: D_`@tiG!Pd; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_076-080.

### Otázka (Front)

Jak se problém batohu řeší genetickým algoritmem a jak se zachází s nepřípustností?

### Odpověď (Back)

Hledá se podmnožina předmětů maximalizující Σvᵢ při Σwᵢ≤W. Binární chromozom x ∈ {0,1}ⁿ má xᵢ=1 právě pro vložený předmět.

Jednoduchá fitness je součet hodnot přípustného řešení a např. 0 při překročení kapacity. Tvrdá nulová penalizace však nerozlišuje malé a velké porušení, takže ztrácí směr ke zlepšení; lepší může být odstupňovaná penalizace nebo opravný operátor.

Rozhodovací batoh je NP-úplný a optimalizační NP-těžký, takže GA je heuristika bez obecné záruky optima.

## Poznámka Anki 1785298610561

Karty Anki: 1785298610561
GUID: NxWx{C)V:; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_081-087.

### Otázka (Front)

Jak genetické programování reprezentuje a inicializuje programy a v čem se liší od GA?

### Odpověď (Back)

**GP** evolvuje kořenové stromy proměnné velikosti, zatímco klasický GA obvykle lineární chromozomy pevné délky. Listy jsou terminály T (vstupy, konstanty), vnitřní uzly funkce F (aritmetické, logické, řídicí); arita uzlů musí být zachována.

**Inicializace:**

- **GROW:** do hloubky D<sub>max</sub> volí funkce i terminály, na D<sub>max</sub> jen terminály → nepravidelné větve.
- **FULL:** před D<sub>max</sub> jen funkce, na D<sub>max</sub> terminály → všechny větve mají plnou hloubku.
- **PCT1:** pravděpodobnostní tvorba s řízenou očekávanou velikostí podle mj. arit funkcí.

## Poznámka Anki 1785298610562

Karty Anki: 1785298610562
GUID: z}X|5VwBB&; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_088-093.

### Otázka (Front)

Jaké mutace a křížení používá genetické programování a proč je strukturálně flexibilní?

### Odpověď (Back)

- **Subtree mutation:** nahradí vybraný podstrom novým náhodným podstromem.
- **Point mutation:** nahradí uzel jiným stejné arity.
- **Shrink mutation:** nahradí podstrom terminálem a program zmenší.
- **Permutation mutation:** přeuspořádá potomky funkčního uzlu; význam mění hlavně u nekomutativních funkcí.
- **Křížení:** vymění podstromy dvou rodičů.
GP mění hodnoty, topologii i velikost programu, takže struktura řešení nemusí být předem pevná.

## Poznámka Anki 1785298610563

Karty Anki: 1785298610563
GUID: ukmkvq:Jda; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_094-096.

### Otázka (Front)

Co charakterizuje evoluční programování (EP) a jak se liší od klasického GA?

### Odpověď (Back)

EP původně evolvovalo **chování agentů reprezentované stavovými automaty** a spoléhalo hlavně na mutaci, nikoli na křížení. Mutovat mohou stavy, počáteční/cílové stavy, přechodová tabulka i vazba vstupů na přechody, pokud zůstane automat platný.

EP zdůrazňuje adaptaci chování mutací strukturovaného modelu; klasický GA typicky kombinuje selekci, křížení a mutaci binárních chromozomů.

## Poznámka Anki 1785298610564

Karty Anki: 1785298610564
GUID: Op((;y>~GZ; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_097-101.

### Otázka (Front)

Co jsou evoluční strategie a jak se liší schémata (1+λ)-ES, (μ+λ)-ES a (μ,λ)-ES?

### Odpověď (Back)

**ES** optimalizují zejména reálné vektory pomocí gaussovské mutace, schémat μ/λ a adaptace velikosti kroku.

- **(1+λ):** jeden rodič vytvoří λ potomků; přežije nejlepší z rodiče i potomků.
- **(μ+λ):** μ nových rodičů se vybere ze sjednocení μ rodičů a λ potomků.
- **(μ,λ):** μ nových rodičů se vybírá pouze z λ potomků.
„+“ je elitistické a nejlepší kvalita neklesá; „,“ vynucuje generační obměnu, ale nejlepší rodič může zaniknout.

## Poznámka Anki 1785298610565

Karty Anki: 1785298610565
GUID: ou^!|Ubxh8; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_102-105.

### Otázka (Front)

Jak funguje gaussovská mutace a adaptace velikosti kroku v evolučních strategiích?

### Odpověď (Back)

Typicky x′ᵢ=xᵢ+σᵢN(0,1). Malé σ podporuje jemnou lokální exploataci, velké σ širší exploraci, ale častěji ničí dobré řešení.

**Endogenní strategické parametry:** jedinec nese vedle řešení G také parametry mutace S (např. σ pro dimenze), takže evoluce optimalizuje řešení i způsob jeho změny.

**Rechenbergovo pravidlo 1/5:** cílí asi na 20 % úspěšných mutací; při vyšší úspěšnosti σ zvětší, při nižší zmenší.

## Poznámka Anki 1785298610566

Karty Anki: 1785298610566
GUID: F>X8VJQiIA; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_106-108.

### Otázka (Front)

Jak funguje diskrétní a aritmetická rekombinace v ES a co znamená parametr ρ?

### Odpověď (Back)

**Diskrétní rekombinace:** každá složka potomka se jako celek převezme od některého rodiče. **Aritmetická rekombinace:** složka vznikne průměrem či váženou kombinací rodičovských hodnot.

V zápisu (μ/ρ +, λ)-ES nebo (μ/ρ, λ)-ES udává **ρ počet rodičů jednoho potomka**: ρ=1 bez rekombinace, ρ=2 párová, ρ=μ rekombinace celé rodičovské populace.

## Poznámka Anki 1785298610567

Karty Anki: 1785298610567
GUID: KXaSrh@kFB; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_109-111.

### Otázka (Front)

Co znamenají explorace a exploatace v evoluci a jak je ovlivňuje selekční tlak?

### Odpověď (Back)

**Exploatace** intenzivně prohledává okolí kvalitních řešení; podporuje ji selekce a lokální operátory. **Explorace** hledá nové vzdálenější oblasti a snižuje riziko lokálního optima; podporuje ji mutace a populační diverzita.

Silný selekční tlak rychle množí nejlepší jedince a posiluje exploataci, ale může zničit diverzitu. Slabší tlak zachovává exploraci, ale zpomaluje soustředění na slibné oblasti.

## Poznámka Anki 1785298610568

Karty Anki: 1785298610568
GUID: f{a6f+-Sj?; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_115-116 src_124.

### Otázka (Front)

Co je předčasná konvergence a jak souvisí s lokálním optimem a účinností křížení?

### Odpověď (Back)

**Předčasná konvergence** nastane, když populace brzy ztratí genotypovou či fenotypovou diverzitu a soustředí se v suboptimální oblasti. Je populační obdobou uváznutí jedincového hledání v lokálním optimu: v obou případech chybí cesta ke vzdálenějšímu lepšímu řešení.

V téměř homogenní populaci nesou rodiče stejnou informaci, takže křížení tvoří podobné potomky a přestává pomáhat s únikem.

## Poznámka Anki 1785298610569

Karty Anki: 1785298610569
GUID: g*x>+&_6KA; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_117-122.

### Otázka (Front)

Co je niching a jak diverzitu udržují ostrovní model, fitness sharing, deterministic crowding a novelty search?

### Odpověď (Back)

**Niching** udržuje více odlišných řešení/subpopulací podle podobnosti genotypů či fenotypů.

- **Ostrovní model:** izolované populace evolvují zvlášť a jen občas migrují.
- **Fitness sharing:** blízcí jedinci si dělí fitness, takže husté niky mají nižší efektivní odměnu.
- **Deterministic crowding:** potomek soutěží s nejpodobnějším rodičem a nahradí jej jen při vyšší fitness.
- **Novelty search:** odměňuje behaviorální novost namísto přímé cílové fitness.

## Poznámka Anki 1785298610570

Karty Anki: 1785298610570
GUID: G~$bh?86x[; štítky: AI_combined::02_evolucni_vypocty iterace_01 src_123 src_125.

### Otázka (Front)

Jak se porovnávají GA, GP, EP a ES a které návrhové volby určují chování evolučního algoritmu?

### Odpověď (Back)

**Typická reprezentace:** GA = binární chromozom pevné délky; GP = programový strom proměnné velikosti; EP = struktura chování, např. stavový automat; ES = reálný vektor doplněný parametry mutace.

**Klíčové volby návrhu:** reprezentace genotypu, fitness a zacházení s omezeními, inicializace, selekční tlak, mutace, křížení, schéma náhrady, velikost populace, mechanismy diverzity a ukončovací podmínka.

