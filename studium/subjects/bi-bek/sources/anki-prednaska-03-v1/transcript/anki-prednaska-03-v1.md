# BI-BEK – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678896339818

Karty Anki: 1678896339818
GUID: Q.[%I0}!e7; štítky: bi-bek::p03 bi-ib::08.

### Otázka (Front)

Popište ochrany proti přetečení bufferu (buffer overflow).

### Odpověď (Back)

Ochrany proti přetečení bufferu (buffer overflow) lze aplikovat na úrovni:

- operačního systému,
- aplikace.

Na úrovni operačního systému se používá:

- Data Execution Prevention (DEP),

- address space layout randomization (ASLR).

Na úrovni aplikace se používá:

- kanárek na zásobníku (stack canary),
- bezpečné ošetření strukturovaných výjimek (safe structured exception handling),
- použití vícero zásobníků za účelem oddělení lokálních proměnných od návratových adres,
- kódování ukazaletů,
- použití bezpečných programovacích jazyků a knihoven.

## Poznámka Anki 1678896491771

Karty Anki: 1678896491771
GUID: ppJ3G)C@z<; štítky: bi-bek::p03 bi-ib::08.

### Otázka (Front)

Popište Data Execution Prevention (DEP)? Jak lze vypnout?

### Odpověď (Back)

Data Execution Prevention (DEP) je obranný mechanismus proti buffer overflow. Funguje tak, že v položce tabulky stránek je nastaven příznak \(\mathtt{XD}\) (execute disable) nebo \(\mathtt{NX}\) (non-executable). Při pokusu o spuštění takové stránky je vygenerována výjimka a program je ukončen. Ve Windows musí být programy linkovány se speciálním parametrem pro podporu DEP. Aplikace si DEP navíc mohou za běhu vypnout voláním funkcí z Windows API.

## Poznámka Anki 1678897075147

Karty Anki: 1678897075147
GUID: cqNXmxV|&o; štítky: bi-bek::p03 bi-ib::08.

### Otázka (Front)

Popište address space layout randomization (ASLR). Jak lze vypnout?

### Odpověď (Back)

Address space layout randomization (ASLR) je obranný mechanismus proti buffer overflow. Funguje tak, že pokud je program kompatibilní, je do paměti zaveden od náhodné adresy, a to včetně zásobníku, haldy a knihoven. Cílem je snížit pravděpodobnost úspěchu útočníka, který se pro spuštění svého exploitu snaží přepsat návratovou adresu:

- adresou v bufferu, který přepsal,
- adresou \(\mathtt{jmp/call} \ \mathtt{esp/ebp}\) v programu nebo knihovně v něm nahrané,

- adresou funkce v programu nebo knihovně v něm nahrané.

ASLR lze vypnout na Linux, na Windows 10 to již není možné. Pro podporu ASLR je potřeba na Windows programy linkovat se speciálním přepínačem.

## Poznámka Anki 1678897703615

Karty Anki: 1678897703615
GUID: F!rp;vNXQK; štítky: bi-bek::p03 bi-ib::08 ni-pb::13.

### Otázka (Front)

Popište kanárka na zásobníku (stack canary) a jeho implementace. Jak lze vypnout?

### Odpověď (Back)

Kanárek na zásobníku (stack canary) je obranný mechanismus proti buffer overflow. Funguje tak, že při vstupu do funkce je na zásobník vloženo náhodné slovo (kanárek) takovým způsobem, aby útočník nemohl přepsat návratovou adresu funkce bez jeho přepsání. V případě, že je detekována změna kanárka, je program ukončen. Mezi implementace kanárka na zásobníku patří:

- StackGuard,

- Stack Smashing Protector nebo někdy také ProPolice (GCC),

- Buffer Security Check (MSVC).

Na Linux je programy potřeba linkovat se speciálními přepínači, na Windows je ochrana automatická a naopak je potřeba použít speciální přepínače pro její vypnutí.

## Poznámka Anki 1678898023626

Karty Anki: 1678898023626
GUID: eCJ^H]#S$U; štítky: bi-bek::p03 bi-ib::08.

### Otázka (Front)

Jak funguje bezpečné ošetření strukturovaných výjimek (SEH)?

### Odpověď (Back)

Před zavoláním obslužné rutiny je ověřeno, že rutina byla vygenerována překladačem. Případně postupným dereferencováním odkazu na nadřazený \(\mathtt{\_\_try/\_\_except}\) blok se zjistí, jestli je možnost traverzovat až na blok obalující spuštění funkce \(\mathtt{main}\).

## Poznámka Anki 1678898189743

Karty Anki: 1678898189743
GUID: vVY4X3gl<_; štítky: bi-bek::p03 bi-ib::08.

### Otázka (Front)

Jak funguje kódování ukazatelů?

### Odpověď (Back)

Jelikož se útočník často snaží přepsat ukazatele, které ukazují na funkce, které budou volány, budou ukazatele kódovány. Před spuštěním programu se vygeneruje náhodná hodnota, která se naxoruje na ukazatele a pomocí stejné operace se pak těsně před voláním dekóduje.

## Poznámka Anki 1717601543696

Karty Anki: 1717601543697
GUID: BYw#aVE*K/; štítky: bi-bek::p03 bi-ib::08.

### Otázka (Front)

Popište return-oriented programming (ROP).

### Odpověď (Back)

Return-oriented programming (ROP) je technika používaná pro obcházení obran proti buffer overflow. Spočívá v tom, že namísto toho, aby útočník do procesu vkládal svůj vlastní exploit, sestaví jej ze sekvencí instrukcí, které jsou v procesu již obsaženy. Těmto sekvencím se říká gadgets a typicky se skládají z epilogu funkce a jedné instrukce před jeho začátkem.

## Poznámka Anki 1718542820105

Karty Anki: 1718542820105
GUID: DyVO-fpN&[; štítky: bi-bek::p03 bi-ib::08 ni-pb::13.

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

