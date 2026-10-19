# BI-DBS – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-dbs/BI-DBS.apkg; APKG SHA-256 2adef415f377fbe4eac7b4dd1e452577d8eedea5e207be2be6c2aeb0e90cf4eb. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7f054157e2673745662b1c45d22f99de1a01232f0420fd85b7b7f7c2b095d969.
Původní balíčky: BI-DBS
Rozsah: 17 poznámek, 17 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1650902933268

Karty Anki: 1650902933269
GUID: EfRuJ=hJs%; štítky: bi-dbs::p10 bi-spol::06.

### Otázka (Front)

Popište transakci.

### Odpověď (Back)

Transakce je sekvence akcí měnících stav databáze, které spolu logicky souvisí.

## Poznámka Anki 1650902973051

Karty Anki: 1650902973051
GUID: LuR6x@CVaf; štítky: bi-dbs::p10.

Metadata původního zdroje pro kartu 1650902973051: v původním balíčku pozastavená karta.

### Otázka (Front)

Co znamená, že databáze je konzistentní?

### Odpověď (Back)

Znamená to, že platí všechna IO definovaná ve schématu.

## Poznámka Anki 1650903136887

Karty Anki: 1650903136887
GUID: z(.wr-RP5o; štítky: bi-dbs::p10 bi-spol::06.

### Otázka (Front)

Vyjmenujte vlastnosti transakcí.

### Odpověď (Back)

Transakce splňují následující vlastnosti:

- **atomicity** - transakce musí buď proběhnout celá nebo neproběhne vůbec,

- **consistency** - transakce transformuje databázi z konzistentního stavu do jiného konzistentního stavu,
- **independence** - dílčí efekty jedné transakce nejsou viditelné jiným transakcím,
- **durability** - efekty úspěšně ukončené (potvrzené) transakce jsou trvale uloženy.

## Poznámka Anki 1716482602833

Karty Anki: 1716482602833
GUID: ip,%-t|<*W; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716482602833: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište moduly transakčního zpracování.

### Odpověď (Back)

Existují následující moduly transakčního zpracování:

- **modul řízení souběžného zpracování** - zajišťuje konzistentní stav databáze pro všechny uživatele, kteří mohou současně pracovat se stejnými daty;

- **modul zotavení z chyb** - zajišťuje konzistentní stav databáze i v případě chyby.

## Poznámka Anki 1716482979835

Karty Anki: 1716482979835
GUID: QJI`z.X(^o; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716482979835: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište stavy transakce.

### Odpověď (Back)

Transakce se může nacházet v následujících stavech:

- **active** - transakce probíhá,

- **partially commited** - všechny operace transakce jsou dokončeny,
- **comitted** - transakce byla potvrzena (příkaz \(\mathtt{COMMIT}\)),

- **failed** - transakce selhala a nemůže pokračovat,

- **aborted** - transakce byla zrušena (příkaz \(\texttt{ROLLBACK}\)).

 [Obrázek: paste-f1768fe828a2b8599ee92c62377ce1a7c2e79801.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1716484256523

Karty Anki: 1716484256523
GUID: cnf%yb%%a^; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716484256523: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište transakční žurnál (transaction journal).

### Odpověď (Back)

Transakční žurnál (transaction journal) obsahuje záznamy o prováděných transakcích, které slouží k zotavení databáze v případě chyby. Záznamy jsou ukládány ve formě změnových vektorů. Žurnál a přidružená infrastruktura umožňuje dodržení vlastností atomicity a durability.

## Poznámka Anki 1716485055735

Karty Anki: 1716485055735
GUID: I22BNJ05-o; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716485055735: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište rozvrh transakcí.

### Odpověď (Back)

Rozvrh transakcí stanovuje pořadí provádění jednotlivých operací transakcí. Pro dosažení vyššího výkonu může být žádoucí prokládat operace různých transakcí. Z tohoto pohledu rozdělujeme rozvrhy na:

- **sériové **- operace každé transakce jsou prováděny vždy pospolu,

- **paralelní** - operace různých transakcí mohou být prokládány.

## Poznámka Anki 1716485522510

Karty Anki: 1716485522511
GUID: OTr!,Z&X84; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716485522511: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište anomálie vznikající při paralelním zpracování transakcí.

### Odpověď (Back)

Při paralelním zpracování transakcí může dojít k anomáliím plynoucím z prokládání operací různých transakcí. Mezi tyto anomálie patří:

- **ztráta aktualizace **- transakce \(T_1\) provede aktualizaci dat, která je následně přepsána aktualizací provedenou transakcí \(T_2\);

- **neopakovatelné čtení** - transakce \(T_1\) získá z dvou stejných dotazů různý výsledek, protože data byla mezitím upravena transakcí \(T_2\);

- **fantom** - transakce \(T_1\) získá z dvou stejných dotazů různý výsledek, protože transakce \(T_2\) mezitím vložila nová data nebo některá data smazala.

## Poznámka Anki 1716486363231

Karty Anki: 1716486363231
GUID: oiaQ>c/2Y%; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716486363231: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište metody řešení problémů paralelního zpracování transakcí.

### Odpověď (Back)

Problémy plynoucí z paralelního zpracování transakcí lze řešit následujícími způsoby:

- **testování uspořádatelnosti rozvrhů **- kontrola, zda je rozvrh uspořádatelný, nepoužívá se kvůli časové náročnosti;

- **konstrukce uspořádatelných rozvrhů** - konstrukce rozvrhů tak, aby byly uspořádatelné, používá uzamykací protokoly.

## Poznámka Anki 1716486413867

Karty Anki: 1716486413867
GUID: LuW.X0I(Db; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716486413867: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište uzamykací protokol a dvoufázový uzamykací protokol.

### Odpověď (Back)

**Uzamykací protokol** je množina pravidel, které udávají, kdy transakce bude uzamykat a odemykat objekty databáze. **Dvoufázovým uzamykacím** protokolem je uzamykací protokol tehdy, když používá dvoufázové transakce.

## Poznámka Anki 1716486549798

Karty Anki: 1716486549798
GUID: y>/dqIaoHU; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716486549798: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište dobře formovanou transakci.

### Odpověď (Back)

Transakci nazveme dobře formovanou, jesliže:

- zamyká objekt, pokud k němu chce přistupovat;
- nezamyká objekt, pokud ho již zamkla,
- neodemyká objekt, pokud jej nezamkla;
- po jejím skončení nezůstane žádný objekt zamčený.

## Poznámka Anki 1716486730769

Karty Anki: 1716486730769
GUID: Bu5BC}{3xb; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716486730769: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište legální rozvrh transakcí.

### Odpověď (Back)

Rozvrh transakcí nazveme legální, jestliže:

- v případě, že chce transakce přistoupit k objektu, musí jej uzamknout;
- v případě, že je objekt již uzamčen jinou transakcí, čeká transakce na jeho odemčení.

## Poznámka Anki 1716487038521

Karty Anki: 1716487038521
GUID: em0t<T(Y|X; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716487038521: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište dvoufázovou transakci.

### Odpověď (Back)

Transakci nazveme dvoufázovou, jestliže se skládá z následujících dvou fází:

- **1. fáze** - transakce uzamyká objekty a provádí operace;

- **2. fáze** - transakce odemyká objekty a nesmí již žádné objekty zamykat.

## Poznámka Anki 1716487209323

Karty Anki: 1716487209323
GUID: n#xq}XRKr<; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716487209323: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište konstrukci uspořádatelného transakčního rozvrhu.

### Odpověď (Back)

Jestliže jsou všechny transakce dobře formované a dvoufázové, pak je každý jejich legální transakční rozvrh uspořádatelný.

## Poznámka Anki 1716487372549

Karty Anki: 1716487372549
GUID: j),T9Dz2@j; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716487372549: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište uspořádatelný rozvrh transakcí.

### Odpověď (Back)

Rozvrh transakcí je uspořádatelný, pokud k němu existuje ekvivalentní sériový rozvrh. Uspořádatelné rozvrhy umožňují dodržení vlastnosti independence.

## Poznámka Anki 1716487753435

Karty Anki: 1716487753435
GUID: p09CaueKag; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716487753435: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište stupně izolace.

### Odpověď (Back)

Stupně izolace udávají, které z anomálií vznikajících kvůli paralelnímu zpracování transakcí jsou v databázi přípustné. Standard nařizuje nejvyšší úroveň izolace serializable, která nepřipouští žádnou z anomálií. V praxi se nicméně často používá úroveň read commited, která povoluje neopakovatelné čtení a fantom.

## Poznámka Anki 1716487861270

Karty Anki: 1716487861270
GUID: i`OZ1Uy6U,; štítky: bi-dbs::p10 bi-spol::06.

Metadata původního zdroje pro kartu 1716487861270: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak je zajištěna vlastnost consistency transakcí?

### Odpověď (Back)

Consistency je zajištěna přímo v interních algoritmech Data Manipulation Language (DML) a tím, že transakce smí obsahovat více DML příkazů.

