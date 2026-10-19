# BI-KAB – Přednáška 11

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-kab/BI-KAB.apkg; APKG SHA-256 080060aa53ee5f63eca18237eef611a0bfca99908f9ab640e349ebadb96964ec. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8571882594c00598a0b5a029eed57cadb06fe0563741a3f883a87eacef0c1588.
Původní balíčky: BI-KAB
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1684242210271

Karty Anki: 1684242210271
GUID: vn:NMlV!HV; štítky: bi-kab::p11.

### Otázka (Front)

Popište podvržení veřejného klíče.

### Odpověď (Back)

Předpokládejme dva subjekty A a B, které si chtějí vyměnit šifrovanou zprávu a subjekt U, který je odposlouchává.

- Subjekt A pošle zprávu \(\text{VK}_\text A \| \text{ID}_\text A\) (dvojice veřejný klíč a identifikátor).
- Subjekt U zprávu zachytí a vygeneruje novou zprávu \(\text{VK}_\text U \| \text{ID}_\text A\), tedy podvrhne \(\text{VK}_\text U\) subjektu B.
- Subjekt B se domnívá, že \(\text{VK}_\text U\) náleží subjektu A a zašifruje zprávu \(M\) klíčem \(\text{VK}_\text U\), tedy vytvoří \(E_{\text{VK}_\text U}(M)\) a odešle ji A.
- Subjekt U zachytí \(E_{\text{VK}_\text U}(M)\) a dešifruje ji pomocí \(\text{SK}_\text U\), čímž získá zprávu \(M\).
- Subjekt U zašifruje \(M\) pomocí \(\text{VK}_\text A\), tedy vytvoří \(E_{\text{VK}_\text A}(M)\) a pošle ji A.

Tímto způsobem může subjekt U odposlouchávat či upravovat zprávy mezi A a B.

 [Obrázek: paste-5817b4fad1e3b38388578636f51687fc650dd96f.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1684242431414

Karty Anki: 1684242431414
GUID: LCB>OWf8N; štítky: bi-kab::p11 bi-spol::09.

### Otázka (Front)

Jakými způsoby lze distribuovat veřejné klíče?

### Odpověď (Back)

Veřejné klíče lze distribuovat následujícími způsoby:

- zveřejnění veřejných klíčů (public announcement),
- veřejně dostupný adresář (publicly available directory),
- autorita pro veřejné klíče (public-key authority),
- certifikace veřejných klíčů (public-key certification).

## Poznámka Anki 1684242541251

Karty Anki: 1684242541251
GUID: IwpiDt}cv; štítky: bi-kab::p11 bi-spol::09.

### Otázka (Front)

Popište distribuci veřejných klíčů zveřejněním veřejných klíčů.

### Odpověď (Back)

Jde o rychlý a jednoduchý postup. Klíče lze buď individuálně či hromadně zaslat nebo vystavit na internetu. Není však odolný proti proti podvržení VK.

## Poznámka Anki 1684243297250

Karty Anki: 1684243297250
GUID: E$_p6y~&Wc; štítky: bi-kab::p11 bi-spol::09.

### Otázka (Front)

Popište distribuci veřejných klíčů pomocí veřejně dostupného adresáře.

### Odpověď (Back)

Záznamy v adresíři jsou dvojice VK a ID (identifikátor subjektu). Nad tímto adresářem operuje důvěryhodná entita, která provádí:

- správu adresáře,
- registraci VK na požadavek účastníků (osobně či pomocí bezpečné komunikace),
- periodickou aktualizaci adresáře.
Pokud však nepovolaný subjekt získá SK důvěryhodné entity, může v adresáři provádět neautorizované změny.

## Poznámka Anki 1684244495172

Karty Anki: 1684244495172
GUID: k%Q=1p|?2r; štítky: bi-kab::p11 bi-spol::09.

### Otázka (Front)

Popište distribuci veřejných klíčů pomocí autority pro veřejné klíče. Jakou má nevýhodu?

### Odpověď (Back)

Autorita vlastní dvojici klíčů \((\text{VK}_\text{aut}, \text{SK}_\text{aut})\) a spravuje svůj adresář s veřejnými klíči subjetků. Předpokládejme dva subjekty A a B, které si chtěji vyměnit šifrovanou zprávu. Pak postupují následovně:

- Subjekt A si od autority vyžádá \(\text{VK}_\text B\). Žádost obsahuje časovou značku \(T_\text A\).
- Autorita odpoví zprávou šifrovanou pomocí \(\text{SK}_{\text{aut}}\).
- Subjekt A zprávu dešifruje pomocí \(\text{VK}_{\text{aut}}\), čímž získá:

- \(\text{VK}_\text B\) -  použije se pro šifrování;

- kopii žádosti od A (včetně \(T_\text A\)) -  ověření, že žádost nebyla po cestě k autoritě modifikována a že je aktuální.

- Subjekt A použije \(\text{VK}_\text B\) pro zašifrování zprávy, která navíc obsahuje ještě \(\text{ID}_\text A\) a náhodné číslo \(N_\text A\), které potvrzuje jedinečnost výměny.
- Po obdržení zprávy si subjekt B vyžádá stejným způsobem od autority \(\text{VK}_\text A\).
- Subjekt B odešle A zprávu \(N_\text A \| N_\text B\) zašifrovanou pomocí \(\text{VK}_\text A\), kde \(N_\text B\) generuje B.
- Subjekt A odpovídá zprávou obsahující \(N_\text B\) zašifrovanou pomocí \(\text{VK}_\text B\).

Nevýhodou však je, že každý subjekt musí komunikovat s autoritou, která představuje „úzké hrdlo“ této koncepce.

## Poznámka Anki 1684259445547

Karty Anki: 1684259445547
GUID: Am`No*wgSV; štítky: bi-ib::12 bi-kab::p11 bi-spol::09.

### Otázka (Front)

Definujte certifikát.

### Odpověď (Back)

Certifikát je struktura, která je podepsána soukromým klíčem certifikační autority a každý účastník si může verifikovat jeho obsah pomocí jejího veřejného klíče. Strvzuje spojení subjektu a veřejného klíče. Certifikát obsahuje:

- veřejný klíč držitele certifikátu,
- identifikační údaje držitele certifikátu,
- dobu platnosti certifikátu,
- další údaje vytvořené certifikační autoritou.

## Poznámka Anki 1684259739117

Karty Anki: 1684259739117
GUID: J/ypL>>%^Z; štítky: bi-ib::12 bi-kab::p11 bi-spol::09.

### Otázka (Front)

Definujte certifikační autoritu (CA). Jak lze ověřit pravost certifikátu?

### Odpověď (Back)

Certifikační autorita (CA) podepisuje, vydává a ukládá certifikáty. Každý subjekt si může ověřit, že byl certifikát vydán příslušnou certifikační autoritou pomocí jejího veřejného klíče.

## Poznámka Anki 1684265278267

Karty Anki: 1684265278267
GUID: uoZEz{$yD*; štítky: bi-kab::p11 bi-spol::09.

### Otázka (Front)

Popište distribuci veřejných klíčů na bázi certifikátů.

### Odpověď (Back)

Uvažujme důvěryhodnou certifikační autoritu a dva subjekty A a B, které si chtějí vyměnit veřejné klíče. Potom postupují následovně:

- Subjekt A doručí CA svůj veřejný klíč \(\text{VK}_\text A\) buď osobně, nebo pomocí bezpečné komunikace.
- CA vydá pro subjekt A certifikát \(C_\text A = E_{\text{SK}_\text{aut}}(T_\text A, ID_\text A, VK_\text A)\), který podepíše pomocí \(\text{SK}_\text{aut}\). Tento certifikát obsahuje:

- \(T_\text A\) - dobu platnosti,

- \(\text{ID}_\text A\) - identifikační údaje subjektu A,

- \(\text VK_\text A\) - veřejný klíč subjektu A.

- Pomocí veřejného klíče CA lze certifikát číst a zároveň ověřit, že byl skutečně vydán danou CA:

\[D_{\text{VK}_\text{aut}}(C_A) = D_{\text{VK}_\text{aut}}\big(E_{\text{SK}_\text{aut}}(T_\text A, \text{ID}_\text A, \text{VK}_\text A)\big) = (T_\text A, \text {ID}_\text A, \text{VK}_\text A).\]

- Subjekt B si zřídí certifikát \(C_\text B = E_{\text{SK}_\text{aut}}(T_\text B, \text{ID}_\text B, \text{VK}_\text B)\) stejným způsobem jako subjekt A.
- Distribuce veřejných klíčů pak spočívá ve výměně \(C_\text A\) a \(C_\text B\).

## Poznámka Anki 1684265359887

Karty Anki: 1684265359887
GUID: onO%k4|!lt; štítky: bi-ib::12 bi-kab::p11 bi-spol::09.

### Otázka (Front)

Co je to ITU-T X.509?

### Odpověď (Back)

Jde o doporučení od International Telecommunication Union, které mimo jiné definuje formát certifikátů.

## Poznámka Anki 1684265541711

Karty Anki: 1684265541711
GUID: bC#44r&~v~; štítky: bi-ib::12 bi-kab::p11 bi-spol::09.

### Otázka (Front)

Jaké mají certifikáty vydávané CA vlastnosti?

### Odpověď (Back)

Certifikáty vydané CA mají následující vlasnosti:

- kterýkoliv subjekt si může pomocí veřejného klíče CA verifikovat veřejné klíče jiných subjektů,
- nikdo jiný než CA nemůže modifikovat vydané certifikáty,
- jsou nefalšovatelné.

## Poznámka Anki 1684265876293

Karty Anki: 1684265876294
GUID: m8kXH)izo$; štítky: bi-ib::12 bi-kab::p11 bi-spol::09.

### Otázka (Front)

Co je to certifikační strom?

### Odpověď (Back)

Koncepce CA je nevýhodná pro velký počet subjektů, proto vznikají různé CA pro různé okruhy subjektů. Tyto CA poté propoujeme pomocí certifikačních stromů, které začínají vždy u **kořenového certifikátu **(certifikát CA, která jej sama sobě podepsala). Ověření certifikátu uživatele tedy představuje průchod řetězcem certifikátů, dokud není nalezen certifikát důvěryhodné CA. 

 [Obrázek: paste-b31b3d39e273ef6883b4b2893df14fa28634d0c5.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1684266316717

Karty Anki: 1684266316717
GUID: jXks,.I)2M; štítky: bi-ib::12 bi-kab::p11 bi-spol::09.

### Otázka (Front)

Co je to křížová certifikace?

### Odpověď (Back)

Pomocí křížové certifikace může jedna CA deklarovat, že důvěřuje všem certifikátům vystaveným jinou CA. Mějme dvě certifikační autority CA\(_1\) a CA\(_2\) a dva subjekty, A, který patří do certifikačního stromu CA\(_1\), a C, který patří do certifikačního stromu CA\(_2\). V případě, že C chce komunikovat s A, musí A poslat C následující množinu certifikátů:

- certifikát A podepsaný CA\(_1\),
- certifikát CA\(_1\) podepsaný CA\(_1\) (kořenový certifikát),
- certifikát CA\(_1\) podepsaný CA\(_2\) (křížový certifikát).

Tímto způsobem se uživatelé CA\(_1\) stanou důvěryhodnými pro CA\(_2\), ale naopak to už neplatí.

 [Obrázek: paste-06749e511c6cb72eb3046dadee19dab124248045.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1684266439994

Karty Anki: 1684266439994
GUID: K2_8O`=HeD; štítky: bi-ib::12 bi-kab::p11 bi-spol::09.

### Otázka (Front)

Jak dlouho je certifikát platný?

### Odpověď (Back)

Každý certifikát má omezenou dobu platnosti. Na žádost držitele lze navíc certifikát invalidovat zařazením na seznam odvolaných certifikátů.

## Poznámka Anki 1684266681400

Karty Anki: 1684266681400
GUID: ytH,DnrRK%; štítky: bi-ib::12 bi-kab::p11 bi-spol::09.

### Otázka (Front)

Co je to public key infrastructure (PKI)?

### Odpověď (Back)

Public key infrastructure (PKI) je sada procesů, technologií a zásad, které se používají pro řízení vydávání, distribuce, používání a odvolávání digitálních certifikátů a klíčů asymetrické kryptografie. Existuje několik přístupů k vytváření PKI. Mezi ty základní patří:

- přístup s použitím certifikačních autorit,
- web of trust,
- simple public key infrastructure.

## Poznámka Anki 1684267320786

Karty Anki: 1684267320787
GUID: ma,R,`l|mA; štítky: bi-kab::p11.

### Otázka (Front)

Popište distribuci tajného klíče pomocí systému veřejného klíče.

### Odpověď (Back)

Předpokládejme dva subjekty A a B, které si dříve bezpečně vyměnily své veřejné klíče a nyní si chtějí zřídit tajný klíč. Postup následující:

- Subjekt A pošle náhodnou hodnotu \(N_\text A\) a svůj identifikátor \(\text{ID}_\text A\) zašifrované pomocí \(\text{VK}_\text B\).

\[E_{\text{VK}_\text B}(N_\text A \| \text{ID}_\text A)\]

- Subjekt B potvrzuje hodnotu \(N_\text A\) společně s ní posílá náhodnou hodnotou \(N_\text B\) zašifrované pomocí \(\text{VK}_\text A\).

\[E_{\text{VK}_\text A}(N_\text A \| N_\text B)\]

- Subjekt A potvrzuje \(N_\text B\) a posílá ji zašifrovanou pomocí \(\text{VK}_\text B\).

\[E_{\text{VK}_\text B}(N_\text B)\]

- Subjekt A zvolí symetrický klíč \(k_s\), podepíše jej svým \(\text{SK}_\text A\) a odešle jej zašifrovaný pomocí \(\text{VK}_\text B\).

\[E_{\text{VK}_\text B}\big(E_{\text{SK}_\text A}(k_s)\big)\]

## Poznámka Anki 1684495351282

Karty Anki: 1684495351282
GUID: xW^[s@u`[N; štítky: bi-ib::12 bi-kab::p11 bi-spol::09.

### Otázka (Front)

Co je to registrační autorita (RA)?

### Odpověď (Back)

Registrační autorita (RA) přijímá požadavky na vydání certifikátů, kontroluje údaje a zadává tvorbu certifikátů certifikační autoritě.

