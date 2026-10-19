# BI-APS – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1668439502268

Karty Anki: 1668439502268
GUID: D]D?oCow&b; štítky: bi-aps::p09.

### Otázka (Front)

Definujte sekvenčně konzistentní počítač.

### Odpověď (Back)

Počítač je sekvenčně konzistentní, jestliže je výsledek provádění programu stejný, jako kdyby paměťové operace na všech procesorech byly provedeny v nějakém globálním sekvenčním pořadí a operace každého jednotlivého procesoru se objevují v této posloupnosti v pořadí daném jeho programem.

## Poznámka Anki 1668439854928

Karty Anki: 1668439854928
GUID: Bp4f;E{pAO; štítky: bi-aps::p09.

Metadata původního zdroje pro kartu 1668439854928: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak je zajištěna sekvenční konzistence v SMP se sdílenou pamětí?

### Odpověď (Back)

Serializace dat na sdílené sběrnici zajistí nějaké (arbitrem sběrnice určené) globální sekvenční proložení instrukcí.

## Poznámka Anki 1668440262300

Karty Anki: 1668440262300
GUID: wC]LG?5a!#; štítky: bi-aps::p09 bi-spol::17.

### Otázka (Front)

Jaké rozeznáváme typy synchronizačních primitiv.

### Odpověď (Back)

- **vzájemné vyloučení **/ **kritická sekce **(Mutual Exclusion) - pouze jeden proces (vlákno) může v jednom okamžiku provádět označený kus kódu

- **synchronizační bariéria **(Synchronization Barrier) - všechny procesy (vlákna) dané skupiny procesů (vláken) musí v tomto bodě čekat až dorazí poslední, a teprve pak mohou pokračovat

- **dvoubodová bariéra** (Point-to-Point Synchronization) - zajištění předání dat mezi dvěma procesy (vlákny); jeden z procesů (vláken) může eventuálně pokračovat v činnosti bez nutnosti čekání

 [Obrázek: paste-cc5da2d8b6330069dd52508c56283b50f0af366d.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1668440794280

Karty Anki: 1668440794280
GUID: l5egs]bw6u; štítky: bi-aps::p09 bi-spol::17.

### Otázka (Front)

Popište sémantiku instrukce \(\mathtt{test \text- and \text- set}\).

### Odpověď (Back)

Instukce \(\mathtt{test \text- and \text- set}\) je atomická instrukce, která se používá k implementaci zámků pro vzájemné vyloučení. Pracuje nad sdílenou proměnnou \(Z\), kde

- \(Z = 0\) znamená, že kritická sekce je uvolněná,

- \(Z = 1\) znamená, že kritická sekce je obsazená.

Při volání \(\mathtt{test \text- and \text- set}\) je do \(Z\) zapsána \(\mathtt 1\), ale vrácena její hodnota před změnou. V případě, že instrukce vrátí \(\mathtt 0\), pak byl zámek získán, v opačném případě nikoliv.

## Poznámka Anki 1668444711173

Karty Anki: 1668444711173
GUID: JgY+Pg0Qea; štítky: bi-aps::p09 bi-spol::17.

Metadata původního zdroje pro kartu 1668444711173: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to ping-pong efekt u vzájemného vyloučení?

### Odpověď (Back)

- Mějme situaci, kdy dvě jádra \(\text{Core}_1\) a \(\text{Core}_2\) čekají na přidělení sběrnice k pokusu o získání zámku a třetí jádro \(\text{Core}_3\) čeká na přidělení sběrnice k odemčení zámku.
- Zámek je implementován pomocí operace \(\mathtt{test}\text{-}\mathtt{and}\text{-}\mathtt{set}\).
- V případě že arbitr sběrnice bude sběrnici přidělovat střídavě \(\text{Core}_1\) a \(\text{Core}_2\) bude docházet k opakované modifikaci a invalidaci bloků těchto jader a zámek nebude odemknut.

## Poznámka Anki 1668445526928

Karty Anki: 1668445526928
GUID: E`]?xsq@3[; štítky: bi-aps::p09 bi-spol::17.

### Otázka (Front)

Popište sémantiku instrukcí \(\mathtt{load}\text{-}\mathtt{linked}\) a \(\mathtt{store}\text{-}\mathtt{conditional}\).

### Odpověď (Back)

- Pro jejich implementaci potřebujeme následující HW podporu:

- **registr adresy zámku **\(\mathtt{LAR}\) (Lock Address Register)

- **příznak uzamčení **\(\mathtt{LF}\) (Lock Flag)

- \(\mathtt{ll(R1, M[Cnt])}\) provede \(\langle \langle \mathtt{R1 \leftarrow M[Cnt]; \, LAR \leftarrow Addr(Cnt); \, LF \leftarrow 1;} \rangle \rangle\)

- \(\mathtt{sc(R1, M[Cnt])}\) provede \(\langle \langle \mathtt{if([LF] == 1)  \,  \{ M[Cnt] \leftarrow R1; \} \, R1 \leftarrow LF; LF \leftarrow 0;} \rangle \rangle\)
- Příznak \(\mathtt{LF}\) se:

- nastavuje instrukcí \(\mathtt{ll}\),
- nuluje instrukcí \(\mathtt{sc}\),
- nuluje při přepnutí kontextu nebo přerušení,
- nuluje když odposlouchávající řadič SP detekuje shodu adresy v \(\mathtt{BusUpgr}\) nebo \(\mathtt{BusRdX}\) transakci s adresou ve svém \(\mathtt{LAR}\) a zároveň jeho \(\mathtt{LF} = 1\) .

## Poznámka Anki 1668445629552

Karty Anki: 1668445629553
GUID: ;%39V^RQh; štítky: bi-aps::p09 bi-spol::17.

Metadata původního zdroje pro kartu 1668445629553: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak při používání \(\mathtt{ll}\) a \(\mathtt{sc}\) může dojít k livelocku?

### Odpověď (Back)

Pokud mezi těmito instrukcemi pracujeme s pamětí, hrozí, že dojde k odstranění bloku obsahujícího \(\mathtt{LAR}\), a program se zablokuje.

