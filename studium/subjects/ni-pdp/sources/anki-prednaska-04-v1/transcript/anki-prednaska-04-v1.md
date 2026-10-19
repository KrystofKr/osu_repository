# NI-PDP – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-pdp/NI-PDP.apkg; APKG SHA-256 b38783778a590460b03050d14b21f60017ff90d9b0abe806748521d92454df28. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: da16e1b818a2fcaa42e78195ece6396a24afd5754b63362dce0d5df6925e0f3f.
Původní balíčky: NI-PDP
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1742053418352

Karty Anki: 1742053418352
GUID: dS#kEb?%/w; štítky: ni-pdp::p04.

### Otázka (Front)

Popište klasifikaci paralelizovatelných programů.

### Odpověď (Back)

Sekvenční algoritmy se z hlediska paralelizovatelnosti na vícejádrových procesorech se sdílenou pamětí dělí na:

- **výpočetně intenzivní **- čas procesoru strávený výpočtem nad daty je větší než čas strávený přesunem dat z paměti (např. násobení matic má složitost \(\mathcal O(n^3)\), ale paměťová reprezentace zabírá \(\mathcal O(n^2)\)),

- **paměťově intenzivní** - čas procesoru strávený výpočtem nad daty je menší než čas strávený přesunem dat z paměti, jejich výpočetní výkon je omezen propustností paměti (např. skalární součin).

## Poznámka Anki 1742054316593

Karty Anki: 1742054316593
GUID: G>R7;l#RS*; štítky: ni-pdp::p04.

### Otázka (Front)

Popište zdroje neefektivity paralelizovatelných algoritmů.

### Odpověď (Back)

Mezi zdroje neefektivity paralelizovatelných algoritmů patří:

- **nevyvážená výpočetní zátěž** - vlákna příliš často čekají na bariéře a jádra nejsou plně využita;
- **příliš těsná synchronizace** - velký počet bariér nebo kritických sekcí;

- **omezený paralelismus** - pokud je paralelizace algoritmu omezena povahou problému, neměl by výpočet používat více vláken, než je nutné

- **vysoká řežie správy vláken** - časté vytváření nebo zánik vláken, nevhodné použití dynamického plánování (\(\texttt{schedule(dynamic)}\)),

- **významná sekvenční část** - paralelizace příliš malé části algoritmu nebo překročení hranice počtu vláken stanovené Amdahlovým zákonem;

- **neefektivní využití ****cache** - častý zápis do sdílených proměnných v cache a falešné sdílení.

## Poznámka Anki 1742054812215

Karty Anki: 1742054812216
GUID: F;Pp`oa*^y; štítky: ni-pdp::p04.

### Otázka (Front)

Popište falešné sdílení (false sharing).

### Odpověď (Back)

Falešné sdílení (false sharing) je jeden ze zdrojů neefektivity paralelizovatelných algoritmů. Dochází k němu v případě, že různá vlákna najednou zapisují na adresy, které jsou mapovány do stejného bloku cache. V důsledku toho je podle koherenčního protokolu (např. MESI) blok invalidován a při dalším přístupu nastává cache miss, což zpomaluje výpočet.

## Poznámka Anki 1742055252765

Karty Anki: 1742055252765
GUID: gQY]NkKK=Q; štítky: ni-pdp::p04.

### Otázka (Front)

Popište postup odstranění falešného sdílení.

### Odpověď (Back)

Postupy pro odstranění falešného sdílení se liší podle velikosti paměťové oblasti. Pro velká pole se falešnému sdílení lze vyhnout splněním dvou podmínek:

- **vhodná granularita plánování** - vláknům jsou přidělovány bloky pole o velikosti bloku cache,

- **zarovnání** - začátek pole je v paměti zarovnán se začátkem bloku cache.

Pro malá pole je navíc potřeba jejich prvky doplnit o výplň tak, aby velikost prvku byla rovna velikosti bloku cache. Následně lze použít stejný postup jako pro velká pole.

## Poznámka Anki 1742056602617

Karty Anki: 1742056602617
GUID: dI&0n+:I)e; štítky: ni-pdp::p04.

### Otázka (Front)

Popište postup paralelizace výpočtu histogramu.

### Odpověď (Back)

Paralelní výpočet histogramu hodnot v rozsahu \(0, \dots, r\) probíhá v následujících krocích:

- každé vlákno ve sdílené paměti inicializuje svůj lokální histogram,
- vlákna paralelně zpracovávají vstupní pole a zapisují do svých lokálních histogramů,
- vlákna provedou paralelní redukci lokálních čítačů:

 [Obrázek: paste-d09491afdb768a98181c94cd0b16cf4a6fedf507.jpg; soubor je v media/ v doprovodném ZIP] 

Tento postup používá datový paralelismus (direktivu \(\texttt{for}\)) a statické plánování. Časová složitost paralelního výpočtu je\[T(n, r, p) = \mathcal O(r) + \mathcal O \Big(\frac n p \Big) + \mathcal O(r).\]Algoritmus je však paměťově intenzivní a jeko výkonnost je tak omezená.

## Poznámka Anki 1742128993068

Karty Anki: 1742128993068
GUID: D[~(PFN2]B; štítky: ni-pdp::p04.

### Otázka (Front)

Popište postup paralelizace násobení polynomů.

### Odpověď (Back)

Násobení polynomů se implementuje pomocí dvou cyklů, kde:

- vnější  \(i\)-cyklus prochází koeficienty prvního polynomu,
- vnitřní \(j\)- cyklus prochází koeficienty druhého polynomu a přičítá jejich součin k hodnotě \((i+j)\)-tého koeficientu výsledného polynomu.
Pro paralelizaci tohoto algoritmu pomocí datového paralelismu (direktiva  \(\texttt{for}\))  existuje několik přístupů:

- **paralelizace vnějšího **\(i\)**-cyklu** - vyžaduje synchronizaci zápisu (např. \(\texttt{atomic update}\)), trpí falešným sdílením;

- **paralelizace vnitřního **\(j\)**-cyklu **- trpí neodstranitelným falešným sdílením, vysoká režie synchronizace kvůli implicitní bariéře (pro každé \(i\));

- **paralelizace dekompozicí výstupního polynomu na disjunktní oblasti zápisů podle hodnoty součtu **\(i + j\) - bez nutnosti synchronizace zápisu a bez falešného sdílení, vlákna počítají podle vzorce\[c_k = \displaystyle \sum_{l = \max(0, k - n)}^{\min(k, m)} a_l b_{l -k}\]a jsou plánována staticky s velikostí chunku rovné počtu objektů datového typu koeficientu polynomu, které se vejdou do jednoho cache bloku.

## Poznámka Anki 1742130222721

Karty Anki: 1742130222721
GUID: K}Q%cb=Uch; štítky: ni-pdp::p04.

### Otázka (Front)

Popište postup paralelizace násobení hustých matic.

### Odpověď (Back)

Násobení hustých matic (klasický algoritmus se složitostí \(\mathcal O(n^3)\)) se implementuje pomocí dvou cyklů, kde:

- první \(i\)-cyklus prochází první index první matice,
- druhý \(j\)-cyklus prochází druhý index druhé matice,
- třetí \(k\)-cyklus prochází druhý index první matice a první index druhé matice, aby spočítal skalární součin.

Pro paralelizaci tohoto algoritmu pomocí datového paralelismu (direktiva  \(\texttt{for}\))  existuje několik přístupů, přičemž všechny jsou bez nutnosti synchronizace:

- **paralelizace **\(i\)**-cyklu** - bez falešného sdílení;

- **paralelizace **\(j\)**-cyklu** - pro velká \(\frac n p\) bez falešného sdílení, vyšší režie synchronizace kvůli implicitní bariéře (pro každé \(i\));
- **paralelizace **\(k\)**-cyklu** - bez falešného sdílení (zápis výsledku provádí master), nejvyšší režie synchronizace kvůli implicitní bariéře (pro každé \(j\)).

Vlákna jsou vlánována vždy staticky s implicitní velikostí chunku \(\frac n p\).

## Poznámka Anki 1742132627310

Karty Anki: 1742132627310
GUID: C%49O^&m;^; štítky: ni-pdp::p04.

### Otázka (Front)

Popište souřadnicový (coordinate) formát uložení řídkých matic a postup paralelizace s ním souvisejícího algoritmu násobení řídkých matic vektorem.

### Odpověď (Back)

**Souřadnicový **(coordinate) **formát uložení řídkých matic** reprezentuje matici pomocí tří polí:

- \(\texttt{RowInd}\) - indexy řádků nenulových prvků matice,

- \(\mathtt{ColInd}\) - indexy sloupců nenulových prvků matice,

- \(\texttt{Elems}\) - hodnoty nenulových prvků matice,
kde konkrétní index do těchto polí popisuje vždy stejný prvek. **Algoritmus násobení řídké matice ** \(\mathbf A\) **v součadnicovém formátu vektorem  **\(\mathbf x\)  pak iteruje přes všechny indexy a počítá\[\texttt{y[RowInd[i]] += Elems[i] * x[ColInd[i]]}.\]Paralelizuje se pomocí datového paralelismu (direktiva \(\texttt{for}\)). Kvůli nepřímé adresaci je však potřeba zajistit synchronizaci zápisu (např \(\texttt{atomic update}\)) a bude docházet k falešnému sdílení.

## Poznámka Anki 1742134749822

Karty Anki: 1742134749822
GUID: pR<s1/ve0; štítky: ni-pdp::p04.

### Otázka (Front)

Popište formát komprimovaných řádků (compressed sparse row) pro uložení řídkých matic a postup paralelizace s ním souvisejícího algoritmu násobení řídkých matic vektorem.

### Odpověď (Back)

**Formát komprimovaných řádků **(compressed sparse row) **pro uložení řídkých matic** reprezentuje matici pomocí tří polí:

- \( \texttt{RowStart}\) - indexy pole \(\texttt{ColInd}\), od nichž jsou v \(\texttt{ColInd}\) uloženy indexy sloupců nenulových prvků matice jednotlivých řádků;

- \(\texttt{ColInd}\) - indexy sloupců nenulových prvků matice;

- \(\texttt{Elems}\) - hodnoty nenulových prvků matice,
kde konkrétní index v \(\texttt{ColInd}\) a \(\texttt{Elems}\) popisuje vždy stejný prvek. Navíc jsou položky lexikograficky uspořádány podle indexu řádku a sloupce. **Algoritmus násobení řídké matice **\(\mathbf A\) **ve formátu komprimovaných řádků vektorem **\(\mathbf x\) pak iteruje přes všechny řádky  \(i\) a následně přes všechny prvky \(j\) daného řádku a počítá\[\texttt{y[i] += Elems[k] * x[ColInd[k]]}.\]Paralelizuje se pomocí datového paralelismu (direktiva \(\texttt{for}\)) se statickým plánováním. Každému vláknu by mělo být přiděleno \(\frac N p\) nenulových prvků, kde \(N\) je celkový počet nenulových prvků, s tím, že by vlákna ale měla získávat pouze celé řádky. Protože \(\texttt{RowStart}\) je seřazená posloupnost a každý jeho prvek označuje součet počtů nenulových prvků na předcházejících řádcích, mohou v něm vlákna hledat svůj ideální dělící bod pomocí binárního vyhledávání. Tím je eliminována nutnost synchronizace zápisu, nicméně stále může docházet k falešnému sdílení.

