# NI-REV – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-rev/NI-REV.apkg; APKG SHA-256 9670f49b042e57cbd1c6d96f27c545d7e3e73f639dfdfaa5254dbc7ff55faa9f. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7fc653b9bed751e297f56e0ab41b46bdc555bbf2270d66a69096723b55136e70.
Původní balíčky: NI-REV
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1733413384620

Karty Anki: 1733413384620
GUID: I;-^iGZ~a=; štítky: ni-pb::15 ni-rev::p06.

### Otázka (Front)

Popište debugger.

### Odpověď (Back)

Debugger je počítačový program, který se používá pro testování a hledání chyb v jiných programech za jejich běhu. Rozlišujeme následující typy debuggerů podle jejich využití:

- **user-mode debugger** - ladění běžných programů,

- **kernel debugger** - ladění jádra operačního systému a jeho ovladačů.

Dále rozlišujeme debuggery podle úrovně, na které zkoumají kód programu:

- **source-level debugger** - ladění na úrovni zdrojového kódu, typicky integrován v IDE;

- **assembly-level **(low-level) **debugger** - ladění na úrovni assembleru.

Na Windows lze debuggery dále rozlišit podle způsobu, kterým program řídí:

- **neinvazivní** - debugger program řídí zastavováním a spouštěním jeho vláken, velmi omezený, ale obtížně detekovatelný;
- **invazivní** - debugger program řídí skrze Windows API a zpracovává debugovací události.

## Poznámka Anki 1733415572511

Karty Anki: 1733415572512
GUID: oB+W{`:O6h; štítky: ni-pb::15 ni-rev::p06.

### Otázka (Front)

Popište metody připojení invazivního debuggeru na Windows.

### Odpověď (Back)

Na Windows se může invazivní debugger k programu připojit následujícími způsoby:

- **při vytváření procesu** - pomocí funkce \(\texttt{CreateProcess}\), je vygenerována událost \(\texttt{CREATE_PROCESS_DEBUG_EVENT}\);

- **za běhu procesu** - pomocí funkce \(\texttt{DebugActiveProcess}\), jsou dodatečně vygenerovány události \(\texttt{CREATE_PROCESS_DEBUG_EVENT}\), \(\texttt{CREATE_THREAD_DEBUG_EVENT}\), \(\texttt{LOAD_DLL_DEBUG_EVENT}\), vyžaduje potřebná oprávnění.

## Poznámka Anki 1733420935828

Karty Anki: 1733420935828
GUID: rfedm$/);?; štítky: ni-pb::15 ni-rev::p06.

### Otázka (Front)

Popište softwarový breakpoint a princip jeho nastavení.

### Odpověď (Back)

Softwarový breakpoint je výjimka (synchronní přerušení). Na MSVC je zpracovávána některým z handlerů v řetězci \(\texttt{EXCEPTION_REGISTRATION}\) struktur. Pro implementaci softwarového breakpointu se typicky využívá instrukce \(\texttt{int3}\) a princip jeho nastavení je následující:

- první byte na adrese breakpointu přepíšeme instrukcí \(\texttt{int3}\) (\(\texttt{0xCC}\)) a uložíme si jeho původní hodnotu,
- vyprázdníme instrukční cache a spustíme debugger.

Jakmile dojde k vyvolání breakpointu, pokračujeme následovně:

- obnovíme původní hodnotu přepsaného bytu,
- snížíme \(\texttt{EIP}\) o jedna (nyní obsahuje adresu breakpointu) a nastavíme příznak trap,
- vyprázdníme instrukční cache a spustíme debugger.

Díky příznaku trap dojde opět k debugovací události, při které obnovíme breakpoint.

## Poznámka Anki 1733421107075

Karty Anki: 1733421107075
GUID: m^((e}%@ij; štítky: ni-pb::15 ni-rev::p06.

### Otázka (Front)

Popište hardwarový breakpoint.

### Odpověď (Back)

Hardwarové breapointy jsou implementovány pomocí debugovacích registrů. Architektura Intel x86 obsahuje následující registry:

- \(\texttt{DR0-DR3}\) - adresy hardwarových breakpointů,

- \(\texttt{DR6}\) - informace o nastalé debugovací události,

- \(\texttt{DR7}\) - řídící informace (velikost sledovaného místa, odlišení breakpointů na spuštění, čtení a zápis).

## Poznámka Anki 1733421304554

Karty Anki: 1733421304554
GUID: Pnz3VTBI=[; štítky: ni-pb::15 ni-rev::p06.

### Otázka (Front)

Porovnejte softwarové a hardwarové breakpointy.

### Odpověď (Back)

Mezi softwarovými a hardwarovými breakpointy jsou následující rozdíly:

| 
      **softwarové breakpointy** | 
      **hardwarové breakpointy**
 | 

| 
      neomezené množství | 
      omezené množství | 

| 
      dokáží detekovat spuštění instrukce | 
      dokáží detekovat spuštění instrukce a přístupy do paměti | 

| 
      mění obsah paměti | 
      nemění obsah paměti | 

| 
      jednodušší detekce | 
      složitější detekce |

## Poznámka Anki 1733421912272

Karty Anki: 1733421912272
GUID: Ihl*fQ[.U&; štítky: ni-pb::15 ni-rev::p06.

### Otázka (Front)

Popište postupy pro debugging jádra operačního systému.

### Odpověď (Back)

Pro debugging jádra operačního systému lze použít následující postupy:

- **lokální **- přímo z počítače, na kterém debugger běží;

- **vzdálený **- přes USB, TCP/IP, sériovou linku nebo podobné rozhraní;

- **virtuální** - pomocí virtualizačního nástroje.

## Poznámka Anki 1733423005462

Karty Anki: 1733423005463
GUID: i^!%*os:S&; štítky: ni-pb::15 ni-rev::p06.

### Otázka (Front)

Popište anti-debugging.

### Odpověď (Back)

Anti-debugging je soubor technik, kterými se počítačový program snaží bránit proti debuggingu. Jejich cílem je zejména:

- detekovat připojený debugger,
- ovlivňovat činnost debuggeru,
- uniknout z debuggingu.

## Poznámka Anki 1733423531819

Karty Anki: 1733423531819
GUID: P,Mx<%oSIG; štítky: ni-pb::15 ni-rev::p06.

### Otázka (Front)

Popište anti-debugging techniky pro detekci debuggeru.

### Odpověď (Back)

Techniky anti-debuggingu pro detekci debuggeru zahrnují:

- **funkce Windows API** - např. \(\texttt{IsDebuggerPresent}\) nebo \(\texttt{OutputDebugString}\),
- **příznak **\(\texttt{BeingDebugged}\) - manuální kontrola příznaku v process environment blocku (PEB),

- **příznak **\(\texttt{ProcessHeap}\) - debuggery typicky alokují v debugovaném procesu paměť,

- **skenování procesů** - hledání debuggerů mezi běžícími procesy,

- **časování** - detekce krokování a pozastavení.

## Poznámka Anki 1733423815758

Karty Anki: 1733423815758
GUID: pB7T+mjZGE; štítky: ni-pb::15 ni-rev::p06.

### Otázka (Front)

Popište anti-debugging techniky pro ovlivnění činnosti debuggeru.

### Odpověď (Back)

Techniky anti-debuggingu pro ovlivnění činnosti debuggeru zahrnují:

- **generování výjimek** - zahlcení analytika výjimkami a skrytí kódu do handleru výjimky;

- **změna toku kódu ****breakpointem** - debugger odchytí i výjimky vznikající z instrukcí \(\texttt{int3}\), které již v programu byly obsaženy, čímž změní tok kódu;

- **zranitelnosti ****debuggerů** - vyvolání chyby v debuggeru zneužitím zranitelnosti;

- **self-debugging **- k procesu může být najednou připojen pouze jeden debugger.

## Poznámka Anki 1733423999772

Karty Anki: 1733423999772
GUID: of/p}|i{ak; štítky: ni-pb::15 ni-rev::p06.

### Otázka (Front)

Popište anti-debugging techniky pro únik z debuggingu.

### Odpověď (Back)

Techniky anti-debuggingu pro únik z debuggingu zarhnují:

- injekce kódu do jiného procesu,
- skrytí kódu do handleru výjimky,
- skrytí kódu před nebo za funkci \(\texttt{main}\) pomocí funkce \(\texttt{_initterm}\),
- skrytí kódu před funkci \(\texttt{start}\) (např. do thread-local storage).

