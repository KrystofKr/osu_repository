# NI-REV – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-rev/NI-REV.apkg; APKG SHA-256 9670f49b042e57cbd1c6d96f27c545d7e3e73f639dfdfaa5254dbc7ff55faa9f. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7fc653b9bed751e297f56e0ab41b46bdc555bbf2270d66a69096723b55136e70.
Původní balíčky: NI-REV
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1727341773362

Karty Anki: 1727341773362
GUID: k.F(L~3qu#; štítky: ni-pb::12 ni-rev::p01.

### Otázka (Front)

Popište reverzní inženýrství (reverse engineering).

### Odpověď (Back)

Reverzní inženýrství (reverse engineering) je proces analýzy systému, softwaru nebo zařízení, jehož cílem je vytvořit reprezentaci analyzovaného objektu na vyšší úrovni abstrakce, zdokumentovat jej a pochopit jeho fungování.

## Poznámka Anki 1727342420150

Karty Anki: 1727342420150
GUID: cDuJi*|d0/; štítky: ni-pb::12 ni-pb::14 ni-rev::p01 ni-rev::p04.

### Otázka (Front)

Popište disassemblování (disassembling).

### Odpověď (Back)

Disassemblování (disassembling) je proces transformace spustitelného kódu ze strojového jazyka do assembleru cílového procesoru. Může být komplikováno pomocí obfuskací, kódování nebo komprese. K disassemblování existují dva základní přístupy:

- lineární průchod (linear sweep),
- rekurzivní průchod (recursive traversal).

## Poznámka Anki 1727342649535

Karty Anki: 1727342649535
GUID: oPbowXrK.q; štítky: ni-pb::12 ni-rev::p01.

### Otázka (Front)

Popište dekompilaci (decompilation).

### Odpověď (Back)

Dekompilace (decompilation) je proces transformace spustitelného kódu do vyššího programovacího jazyka. Často není stoprocentní, tedy není možná rekompilace. Může být komplikována obfuskací, packery ale i složitějšími konstrukcemi, jako je polymorfismus.

## Poznámka Anki 1727343113840

Karty Anki: 1727343113841
GUID: inB6~MB?h:; štítky: ni-pb::12 ni-rev::p01.

### Otázka (Front)

Popište statickou analýzu kódu (analýzu mrtvého kódu).

### Odpověď (Back)

Statická analýza kódu (static code analysis) je analýza kódu, která je prováděna na neběžícím spustitelném kódu. Typicky postupuje následovně:

- kód disassemblujeme pomocí disassembleru,
- odstraníme knihovní kód a kód generovaný kompilátorem,
- extrahujeme všechny informace ze spustitelného kódu (jména tříd, RTTI, typy) a použijeme je pro okomentování assembleru,
- provedeme analýzu.

## Poznámka Anki 1727343228410

Karty Anki: 1727343228410
GUID: Mh7,_sb6x}; štítky: ni-pb::12 ni-rev::p01.

### Otázka (Front)

Popište dynamickou analýzu kódu (analýzu živého kódu).

### Odpověď (Back)

Dynamická analýza kódu (dynamic code analysis) je analýza kódu, která je prováděna na běžícím spustitelném kódu. Typicky postupuje následovně:

- kód načteme do debuggeru,
- můžeme nastavit breakpointy, watchpointy apod.,
- provedeme analýzu.

## Poznámka Anki 1727343477672

Karty Anki: 1727343477672
GUID: qZhLHoQ,0V; štítky: ni-pb::12 ni-rev::p01.

### Otázka (Front)

Popište application binary interface (ABI).

### Odpověď (Back)

Application binary interface (ABI) je rozhraní popisující správné chování binárního kódu na cílové platformě, které je nutné pro kompatibilitu s jiným binárním kódem a operačním systémem. Typicky definuje:

- způsob předávání parametrů funkcím,
- zarovnání dat a zásobníku,
- použití registrů procesoru

a další.

## Poznámka Anki 1727343631834

Karty Anki: 1727343631834
GUID: Fd-O59B!cY; štítky: ni-rev::p01.

Metadata původního zdroje pro kartu 1727343631834: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to dekorace jmen (name mangling)?

### Odpověď (Back)

Dekorace jmen (name mangling) je proces zanášení dodatečné informace do jména symbolu, čímž vznikají unikátní pojmenování symbolů.

## Poznámka Anki 1727344441391

Karty Anki: 1727344441392
GUID: z[$Ec%GYH0; štítky: ni-pb::13 ni-rev::p01.

### Otázka (Front)

Popište volací konvence (calling conventions).

### Odpověď (Back)

Volací konvence (calling conventions) určují, jak jsou funkce volány, jak jim jsou předávány parametry, jak vrací svůj výsledek a kdo odstraňuje použité parametry. Mezi často používané konvence patří:

- \(\texttt{__cdecl}\) - implicitní pro C, úklid provádí volající;

- \(\texttt{__stdcall}\) - podobné \(\texttt{__cdecl}\), úklid provádí volaný;

- \(\texttt{__thiscall}\) - implcitní pro volání metod, v registru \(\texttt{ECX}\) je předáván \(\texttt{*this}\), úklid provádí volaný.

## Poznámka Anki 1727344488582

Karty Anki: 1727344488582
GUID: CuQKAM+@JX; štítky: ni-rev::p01.

Metadata původního zdroje pro kartu 1727344488582: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište prolog a epilog funkce.

### Odpověď (Back)

Prolog a epilog funkce představují „standardní úvod“ a „standardní konec“ funkce. Oba pracují s ukazatelem na vrchol zásobníku (\(\texttt{esp}\)) a ukazatelem na základ zásobníku (\(\texttt{ebp}\)). V prologu jsou typicky prováděny následující operace:

- \(\texttt{ebp}\) je uložen na zásobník

\[\texttt{push ebp};\]

- \(\texttt{ebp}\) je nastaven na \(\texttt{esp}\)

\[\texttt{mov ebp, esp};\]

- \(\texttt{esp}\) je posunut (na x86 k nižším adresám) tak, aby byl vytvořen prostor pro lokální proměnné funkce

\[\texttt{sub esp, X};\]

- typicky je ještě zajištěno zarovnání zásobníku, jsou uloženy zachovávané registry a volitelně může dojít k vložení kanárka (stack canary) nebo strukturované obsluhy výjimek (SEH).

V epilogu se typicky provádí následující operace:

- typicky se provede obnovení zachovaných registrů a volitelně může dojít ke kontrole kanárka (stack canary) a obnovení předchozího stavu strukturované obsluhy výjimek (SEH);
- \(\texttt{esp}\) je nastaven na \(\texttt{ebp}\), čímž dojde k uvolnění lokálních proměnných funkce

\[\texttt{mov esp, ebp};\]

- \(\texttt{ebp}\) je obnoven ze zásobníku

\[\texttt{pop ebp};\]

- dojde k návratu z funkce

\[\texttt{ret}.\]

## Poznámka Anki 1727344525083

Karty Anki: 1727344525083
GUID: H$ml69ARdz; štítky: ni-rev::p01.

Metadata původního zdroje pro kartu 1727344525083: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište kanárka na zásobníku (stack canary) a jeho implementace. Jak lze vypnout?

### Odpověď (Back)

Kanárek na zásobníku (stack canary) je obranný mechanismus proti buffer overflow. Funguje tak, že při vstupu do funkce je na zásobník vloženo náhodné slovo (kanárek) takovým způsobem, aby útočník nemohl přepsat návratovou adresu funkce bez jeho přepsání. V případě, že je detekována změna kanárka, je program ukončen. Mezi implementace kanárka na zásobníku patří:

- StackGuard,

- Stack Smashing Protector nebo někdy také ProPolice (GCC),

- Buffer Security Check (MSVC).

Na Linux je programy potřeba linkovat se speciálními přepínači, na Windows je ochrana automatická a naopak je potřeba použít speciální přepínače pro její vypnutí.

## Poznámka Anki 1728217332220

Karty Anki: 1728217332220
GUID: BI@W>mGbZq; štítky: ni-pb::13 ni-rev::p01.

### Otázka (Front)

Popište identifikaci instalace kanárka (stack canary) v prologu funkce.

### Odpověď (Back)

Instalaci kanárka (stack canary) můžeme identifikovat pomocí:

- přístupu k \(\texttt{[gs:0x14]}\) u GCC (Stack Smashing Protector):

\[\texttt{mov %[gs:0x14], %eax},\]

- XORu \(\texttt{eax} \) s \(\texttt{ebp}\) u MSVC (Buffer Security Check):

\[\texttt{xor eax, ebp}.\]

## Poznámka Anki 1728217707442

Karty Anki: 1728217707442
GUID: N}s21bbpz`; štítky: ni-pb::13 ni-rev::p01.

### Otázka (Front)

Popište identifikaci instalace strukturované obsluhy výjimek (SEH) v prologu funkce.

### Odpověď (Back)

Instalace strukturované obsluhy výjimek (SEH) je specifická pro MSVC a můžeme ji identifikovat pomocí přístupu k adrese \(\texttt{fs:[0h]}\), která odkazuje do thread information blocku (TIB) na aktuální nejvyšší \(\texttt{EXCEPTION_REGISTRATION}\) strukturu:\[\texttt{mov eax, dword ptr fs:[0h]}.\]

