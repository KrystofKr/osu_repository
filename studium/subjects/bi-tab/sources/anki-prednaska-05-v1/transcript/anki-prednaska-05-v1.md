# BI-TAB – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-tab/BI-TAB.apkg; APKG SHA-256 aad5d9418346792a97b103483c6a92411d60f79d52fd5a423fd0fc14dffe748b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 53183dd48468239630c7cf283347984511ecad52b3dee78ea36f4c1d42180eeb.
Původní balíčky: BI-TAB
Rozsah: 19 poznámek, 19 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1710965743973

Karty Anki: 1710965743974
GUID: Gc1u]EE8B-; štítky: bi-tab::p05.

### Otázka (Front)

Uveďte příklady metod ochrany paměti.

### Odpověď (Back)

Mezi metody ochrany paměti patří:

- ohrady (fences),
- relokace,
- mezní registry (base/bound),
- značkovaná architektura (tagged architecture),
- segmentace a stránkování,
- zámky a klíče.

## Poznámka Anki 1710966032438

Karty Anki: 1710966032438
GUID: zG&_iaEI=); štítky: bi-tab::p05.

### Otázka (Front)

Popište ochranu paměti za pomoci ohrad (fences).

### Odpověď (Back)

Ohrady (fences) je metoda ochrany paměti, která paměť rozdělí na dvě části. Jednu z nich používá operační systém, tu druhou pak uživatelské procesy. Je vhodná pro systémy s jedním uživatelem, neboť dokáže oddělit pouze operační systém, ale jednotlivé procesy už ne. Implementuje se typicky pomocí pevné hranice definované ve fence registru.

## Poznámka Anki 1710966329458

Karty Anki: 1710966329459
GUID: ooN$aAPB!%; štítky: bi-tab::p05.

### Otázka (Front)

Popište ochranu paměti za pomoci relokace.

### Odpověď (Back)

Relokace je metoda ochrany paměti, při které jsou programy navrhovány tak, aby v paměti ležely od adresy nula. Používají relativní odkazy, ke kterým je následně přičítán relokační faktor. Operační systém se nachází v nejnižší části paměti a programy do něj nemohou zasahovat. Nedokáže však vzájemně oddělit jednotlivé procesy, což se řeší pomocí protection key.

## Poznámka Anki 1710966898158

Karty Anki: 1710966898158
GUID: hu4>FO&t}0; štítky: bi-tab::p05.

### Otázka (Front)

Popište ochranu paměti za pomoci relokace s protection key.

### Odpověď (Back)

Protection key rozšiřuje ochranu paměti za pomoci relokace a umožňuje oddělit jednotlivé procesy. Je uložen v každém chunku paměti a typicky obsahuje PID. Procesor pak při každém přístupu do paměti porovnává protection key chunku s PID přistupujícího procesu.

## Poznámka Anki 1710967195105

Karty Anki: 1710967195105
GUID: xycei7d53e; štítky: bi-tab::p05.

### Otázka (Front)

Popište ochranu paměti za pomoci mezních registrů (base/bound).

### Odpověď (Back)

Mezní registry (base/bound) je metoda ochrany paměti, při které jsou definovány registry obsahující nejvyšší a nejnižší dostupnou adresu. Tyto registry se nastavují dynamicky při předávání řízení procesu a umožňují tak oddělení jednotlivých procesů. Její nevýhodou je, že neumožňuje selektivní sdílení dat.

## Poznámka Anki 1710967370548

Karty Anki: 1710967370548
GUID: c(?YmlAQ`&; štítky: bi-tab::p05.

### Otázka (Front)

Popište ochranu paměti za pomoci značkované architektury (tagged architecture).

### Odpověď (Back)

Značkovaná architektura (tagged architecture) je metoda ochrany paměti, při které je s každou adresou spojeno několik řídících bitů (tags), které určují typ uložených dat a povolené operace.

## Poznámka Anki 1710968704420

Karty Anki: 1710968704420
GUID: wjk0wdIYx4; štítky: bi-tab::p05.

### Otázka (Front)

Popište ochranu paměti za pomoci segmentace.

### Odpověď (Back)

Ochrana paměti pomocí segmentace probíhá tak, že při přístupu k adrese, která se skládá ze dvou částí, segment selector a offset, je kontrolováno, že offset nepřesahuje délku segmentu. Její výhodou je, že umožňuje selektivní sdílení dat.

## Poznámka Anki 1711037115237

Karty Anki: 1711037115237
GUID: y1e)Y!!C0l; štítky: bi-tab::p05.

### Otázka (Front)

Popište metodu ochrany paměti za pomocí stránkování.

### Odpověď (Back)

Ochrana paměti za pomocí stránkování je jedna nejrozšířenějších metod ochrany paměti, která kombinuje principy ostatních metod. Každému procesu přiděluje virtuální adresní prostor a procesy se tak nemohou vzájemně ovlivňovat. Navíc podobně jako značkovaná architektura (tagged architecture) umožňuje pro každou stránku definovat úrovně přístupu a povolené operace.

## Poznámka Anki 1711038404635

Karty Anki: 1711038404635
GUID: vh:?Y?evl#; štítky: bi-tab::p05.

Metadata původního zdroje pro kartu 1711038404635: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište direct memory access (DMA) útok. Uveďte typy portů, které mohou DMA povolovat.

### Odpověď (Back)

Direct memory access (DMA) útok je typ útoku postranním kanálem, kdy útočník získá přímý přístup do paměti skrze hardwarové porty. Mezi porty, které mohou dovolovat DMA patří FireWire, ExpressCard nebo Thunderbolt.

## Poznámka Anki 1711039675177

Karty Anki: 1711039675177
GUID: w@%g99OF3[; štítky: bi-tab::p05.

### Otázka (Front)

Popište útok cold boot.

### Odpověď (Back)

Útok cold boot je typ útoku postranním kanálem, jehož cílem je získat obraz operační paměti počítače. Zneužívá toho, že obsah volatilních pamětí, jako je SRAM nebo DRAM, zůstává čitelný ještě několik sekund po vypnutí napájení. Typicky probíhá následujícím způsobem:

- Útočník provede hard reset stroje (odebere mu napájení).
- Typicky ještě cílovou paměť prudce zchladí, aby zpomalil degradaci jejího obsahu.
- Paměť vyjme a vloží do jiného stroje, pomocí nějž si zkopíruje obsah paměti.

## Poznámka Anki 1711040421410

Karty Anki: 1711040421410
GUID: v)beA7$3G-; štítky: bi-tab::p05.

### Otázka (Front)

Popište TRESOR.

### Odpověď (Back)

TRESOR je patch Linuxového jádra zavedený v reakci na DMA a cold boot útoky. Mění nakládání s kryptografickými klíči tak, že namísto v RAM jsou ukládány v registrech procesoru. Využívá k tomu instrukční sadu AES-NI. Tuto metodu však lze obejít např. využitím speciálního souboru \(\mathtt{/dev/kmem}\), který umožňuje přístup do systémové paměti.

## Poznámka Anki 1711041961705

Karty Anki: 1711041961705
GUID: AGB8>a$y85; štítky: bi-tab::p05.

Metadata původního zdroje pro kartu 1711041961705: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište stupně superskalárního instrukčního zřetězení.

### Odpověď (Back)

Superskalární zřetězení se člení na následující stupně:

- **instrukční/dekódovací fronta** (instruction/decode buffer) - fronta načtených instrukcí (mohou být již částečně dekódovány);
- **rozřazovací fronta** (dispatch buffer) - slouží k pozdržení instrukcí, dokud nebudou předány odpovídajícím vykonávacím jednotkám, instrukce do ní přicházejí v programovém pořadí, ale mohou z odcházet v jiném;
- **rezervační stanice** (reservation station) - fronta instrukcí připravených k provedení operace v dané vykonávací jednotce nebo čekajících na forwarding dat;
- **řadící fronta** (reorder buffer) - fronta, která zajistí dokončení instrukcí v programovém pořadí, což je nezbytné pro podporu přesných přerušení (precise exceptions);
- **zápisová fronta** (store buffer) - fronta mezi vykonávacími jednotkami a L1 datovou cache.

## Poznámka Anki 1711049989435

Karty Anki: 1711049989436
GUID: Fh$T#R[@Pt; štítky: bi-tab::p05.

### Otázka (Front)

Popište postranní kanál technikou flush and reload.

### Odpověď (Back)

Flush and reload je typ útoku postranním kanálem, jehož cílem je zjistit, zda se za nějaký časový interval pracovalo s konkrétním blokem paměti. Funguje následujícím způsobem:

- Sledovaný blok je odstraněn z cache (flush).
- Uplyne časový interval, během kterého může a nemusí nějaký proces k bloku přistoupit.
- Následně je k danému bloku přistoupeno (reload) a v případě, že nastane cache hit, byl tento blok používán nějakým procesem.

## Poznámka Anki 1711050274022

Karty Anki: 1711050274023
GUID: mf;BOKU/WA; štítky: bi-ib::17 bi-tab::p05.

### Otázka (Front)

Popište flush and reload postranní kanál na příkladu algoritmu square and multiply.

### Odpověď (Back)

Alogirtmus square and multiply je implementován v knihovně OpenSSL, jejíž paměťové stránky jsou typicky sdíleny napříč několika procesy. Útočník může pomocí flush and reload sledovat, jaká část kódu je prováděna, a tedy zda se provádí operace násobení. Tímto způsobem může např. získat tajný klíč šifry RSA, která tento algoritmus využívá.

## Poznámka Anki 1711053156976

Karty Anki: 1711053156976
GUID: Am+/&K,{k?; štítky: bi-tab::p05.

Metadata původního zdroje pro kartu 1711053156976: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište útok Meltdown.

### Odpověď (Back)

Meltdown je útok cílený na superskalární procesory, který zneužívá out-of-order provádění instrukcí a cache postranní kanál. Předpokládejme, že v user space máme alokované pole \(\texttt{probe_array}\) o velikosti \(256 \cdot 4096\) bytů, kde \(256\) je počet všech možných hodnot bytu a \(4096\) bytů je běžná velikost stránky. Potom útok Meltdown probíhá následovně:

- Nejprve je přistoupeno na adresu v kernel space s cílem přečíst jeden byte dat \(b\).
- Poté je přistoupeno k \(\texttt{probe_array[} b \cdot 4096 \texttt ]\), čímž je do cache načtena jedna konkrétní stránka obsahující část \(\texttt{probe_array} \).
- Nakonec je za pomocí flush and reload postranního kanálu zjištěno číslo stránky, ke které bylo přistoupeno, a je tak získána hodnota \(b\).

Protože superskalární procesor vykonává instrukce mimo programové pořadí, jsou tyto instrukce provedeny dříve, než dojde k dohledání, že daná adresa náleží kernel space, a je vyvolána výjimka.

## Poznámka Anki 1711054739845

Karty Anki: 1711054739845
GUID: bQ5pi3zXms; štítky: bi-tab::p05.

### Otázka (Front)

Popište obrany proti útoku Meltdown.

### Odpověď (Back)

Proti útoku Meltdown se lze bránit následujícími způsoby:

- **kernel address space layout randomization **(KASLR) - randomizace adresy, od které je v paměti umístěn kernel;

- **kernel page-table isolation **(KPTI nebo dříve KAISER) - vytvoření dvou separátních stránkovacích tabulek pro kernel space a user space, přičemž user space tabulka obsahuje pouze minimum kernel space adres.

## Poznámka Anki 1711110555134

Karty Anki: 1711110555135
GUID: lD&USu66&j; štítky: bi-tab::p05.

Metadata původního zdroje pro kartu 1711110555135: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište útok Spectre (varianta bounds check bypass).

### Odpověď (Back)

Spectre je útok cílený na superskalární procesory, který zneužívá spekulativní provádění instrukcí a cache postranní kanál. Předpokládejme, že v user space máme alokované pole \(\texttt{probe_array}\) o velikosti \(256 \cdot 4096\) bytů, kde \(256\) je počet všech možných hodnot bytu a \(4096\) bytů je běžná velikost stránky. Dále předpokládejme pole \(\texttt{array}\) ukazující do libovolné paměti a proměnnou \(\texttt{array_size}\). Potom útok Spectre probíhá následovně:

- Nejprve je vyhodnocena podmínka \(\texttt x < \texttt{array_size}\).
- Na základě této podmínky je přistoupeno k \(\texttt{probe_array[array[x]} \cdot 4096 \texttt ]\) s cílem přečíst jeden byte dat \(b\). Tím je do cache načtena jedna konkrétní stránka obsahující část \(\texttt{probe_array} \).
- Nakonec je za pomocí flush and reload postranního kanálu zjištěno číslo stránky, ke které bylo přistoupeno, a je tak získána hodnota \(b\).
Protože \(\texttt x\) je hodnota, kterou útočník dokáže ovlivnit, může prediktor skoků vytrénovat tak, aby umožňil spekulativně vykonat přístup do paměti, který by se za normálních okolností neměl provést.

## Poznámka Anki 1711115217570

Karty Anki: 1711115217570
GUID: MN6h;~wX~p; štítky: bi-tab::p05.

### Otázka (Front)

Popište ovlivnění (mistraining) predikce skoků cizího procesu.

### Odpověď (Back)

Ovlivnění (mistraining) prediktorů v cizím procesu lze dosáhnout kvůli tomu, že na jeden prediktor se může mapovat vícero adres podmíněných skoků. V případě, že útočník ve svém adresním prostoru nalezne podmíněný skok, jehož adresa je kongruentní s adresou podmíněného skoku cizího procesu, může ovlivnit prediktorem vydávané predikce.

## Poznámka Anki 1711117233444

Karty Anki: 1711117233444
GUID: F4iw=ghL:1; štítky: bi-tab::p05.

### Otázka (Front)

Popište obrany proti útoku Spectre.

### Odpověď (Back)

Proti útoku Spectre a všem jeho variantám neexistuje absolutní obrana. Nicméně mezi technologie, které se používají, patří např. retpoline (return trampoline). Pomocí ní lze nepřímé skoky nahradit za volání instrukce \(\texttt{ret}\) a zabránit tak procesoru ve spekulativním provádění, protože místo indirect branch predictoru je použit return address stack.

