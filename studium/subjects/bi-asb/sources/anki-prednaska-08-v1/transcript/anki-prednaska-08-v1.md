# BI-ASB – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-asb/BI-ASB.apkg; APKG SHA-256 7a0706fba841a39fa40ea1e5439c99f14f59930aaa7f6d5620a33590d53350fa. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: eea4a1b952e7287bc51501f27ae2f5ec76f032fca049ee9ef600d2729e12ef40.
Původní balíčky: BI-ASB
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1701089140854

Karty Anki: 1701089140854
GUID: ARAZ?YgPIY; štítky: bi-asb::p08 bi-ib::12 ni-pb::21.

### Otázka (Front)

Popište naivní přístup k autentizaci a jeho nevýhody.

### Odpověď (Back)

Naivní přístup k autentizaci předpokládá, že klient i autentizátor mají smluvené společné heslo. Autentizace potom probíhá následovně:

- Klient posílá autentizátoru authentication request, ve kterém se identifikuje.
- Klient posílá autentizátoru heslo formou otevřeného textu.
- Autentizátor ověří heslo a posílá klientovi výsledek autentizace.

Mezi nevýhody tohoto přístupu patří:

- heslo je přenášeno formou otevřeného textu, tedy je náchylné k odposlechu (eavesdropping);
- schéma nepoužívá nonce, tedy je náchylné k replay útokům.

## Poznámka Anki 1701091496485

Karty Anki: 1701091496486
GUID: x-,#^2/Ix+; štítky: bi-asb::p08 bi-ib::12 ni-pb::21.

### Otázka (Front)

Popište challenge/response autentizaci a její nevýhody.

### Odpověď (Back)

Challenge/response autentizace předpokládá, že klient i autentizátor mají smluvený společný klíč. Autentizace potom probíhá následovně:

- Klient posílá autentizátoru authentication request, ve kterém se identifikuje.
- Autentizátor posílá klientovi challenge ve formě nonce.
- Klient zašifruje nonce pomocí sdíleného klíče a pošle ji autentizátoru.
- Autentizátor na své straně také zašifruje nonce pomocí sdíleného klíče, porovná výsledky a posílá klientovi výsledek autentizace.

Mezi nevýhody tohoto přístupu patří:

- challenge lze zachytit a provést na ni offline brute-force útok;

- pokud dojde k zopakování nonce, lze na toto schéma provést replay útok;
- odpověď klienta používá klíč v otevřeném textu (měla by používat hashovaný klíč).

## Poznámka Anki 1701091684759

Karty Anki: 1701091684759
GUID: E8fxsX2cS4; štítky: bi-asb::p08 bi-ib::12 ni-pb::21.

### Otázka (Front)

Popište autentizaci s použitím hesla a Diffie-Hellmanova algoritmu a její nevýhody.

### Odpověď (Back)

Autenziace s použitím hesla a Diffie-Hellmanova algoritmu předpokládá, že klient i autentizátor mají smluvené společné heslo. Tato metoda se používá v SSH pod jménem password authentication. Autentizace potom probíhá následovně:

- Proběhne sjednání klíče podle Diffie-Hellmanova algoritmu a sestavení šifrované relace.
- Klient posílá autentizátoru authentication request, ve kterém se identifikuje.
- Klient posílá autentizátoru hash svého hesla.
- Autentizátor ověří heslo a posílá klientovi výsledek autentizace.

Mezi nevýhody tohoto přístupu patří:

- bezpečnost závisí na bezpečnosti šifrované relace a síle hesla,
- autentizátor potřebuje mít zřízený certifikát.

## Poznámka Anki 1701092106437

Karty Anki: 1701092106437
GUID: P5i>>_*CpL; štítky: bi-asb::p08 bi-ib::12 ni-pb::21.

### Otázka (Front)

Popište autentizaci založenou na systému veřejného klíče a její nevýhody.

### Odpověď (Back)

Autentizace založená na systému veřejného klíče předpokládá, že na autentizátoru je nainstalován veřejný klíč klienta. Tato metoda se používá v SSH pod jménem public key authentication. Autentizace potom probíhá následovně:

- Klient posílá autentizátoru authentication request, ve kterém se identifikuje.
- Autentizátor posílá klientovi nonce.
- Klient podepíše nonce pomocí svého soukromého klíče a pošle ji autentizátoru.
- Autentizátor na své straně ověří podepsanou nonce pomocí veřejného klíče klienta, porovná výsledky a posílá klientovi výsledek autentizace.

Mezi nevýhody tohoto přístupu patří:

- problémy spojené s kompromitací soukromého klíče,
- problémy spojené s distribucí veřejného klíče.

## Poznámka Anki 1701092403103

Karty Anki: 1701092403103
GUID: LkZa?/?L.&; štítky: bi-asb::p08 bi-ib::12 ni-pb::21.

### Otázka (Front)

Popište autentizaci založenou na certifikátech a její nevýhody.

### Odpověď (Back)

Autentizace založená na certifikátech probíhá následovně:

- Klient posílá autentizátoru authentication request, ve kterém se identifikuje.
- Klient posílá autentizátoru svůj certifikát.
- Autentizátor posílá klientovi nonce.
- Klient podepíše nonce pomocí svého soukromého klíče a pošle ji autentizátoru.
- Autentizátor na své straně ověří podepsanou nonce pomocí veřejného klíče klienta, porovná výsledky a posílá klientovi výsledek autentizace.

Mezi nevýhody tohoto přístupu patří:

- do procesu autentizace vstupuje třetí strana v podobě certifikační autority,
- nutnost získání certifikátu a jeho validace,
- overhead v komunikaci.

## Poznámka Anki 1701093094869

Karty Anki: 1701093094869
GUID: IQ!__2GA>5; štítky: bi-asb::p08.

Metadata původního zdroje pro kartu 1701093094869: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište one-time password algoritmy standardizované Initiative for Open Authentication (OATH).

### Odpověď (Back)

Initiative for Open Authentication (OATH) specifikuje následující tři algoritmy:

- **HMAC-based one-time password** (HOTP) - založené na čítači:

\[\operatorname{HOTP}(\text{key}, \text{counter}) = \operatorname{truncate}(\operatorname{HMAC}_{\text{SHA-1}}(\text{key}, \text{counter}),\]

- **time-based one-time password **(TOTP) - založené na časových značkách:

\[\operatorname{TOTP}(\text{key}, \lfloor\frac{\text{time} - \text{oldest time}}{\text{time step}}\rfloor) = \operatorname{HOTP}(\text{key}, \lfloor\frac{\text{time} - \text{oldest time}}{\text{time step}}\rfloor),\]

- **OATH challenge-response algorithm **(OCRA) - založené na výměně challenge-response zpráv.

## Poznámka Anki 1701093534137

Karty Anki: 1701093534137
GUID: v1!i^V<&0L; štítky: bi-asb::p08 bi-ib::18 bi-ib::25 ni-pb::21.

### Otázka (Front)

Popište multi-factor authentication (MFA).

### Odpověď (Back)

Multi-factor authentication je typ autentizace, který kombinuje dva nebo více autentizačních faktorů.

## Poznámka Anki 1701093908036

Karty Anki: 1701093908036
GUID: P2B~.+@I~N; štítky: bi-asb::p08.

Metadata původního zdroje pro kartu 1701093908036: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište rainbow tables.

### Odpověď (Back)

Rainbow tables jsou tabulky obsahující předpočítané výstupy hashovacích funkcí pro nejčastěji používaná hesla, které se často používají při lámání hesel. Nabízejí mnohem vyšší efektivitu než klasický brute-force útok, ale zabírají více paměťového místa.

## Poznámka Anki 1701094218562

Karty Anki: 1701094218562
GUID: eDgE{tg=0H; štítky: bi-asb::p08.

Metadata původního zdroje pro kartu 1701094218562: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Jaký je rozdíl mezi online a offline lámáním hesel?

### Odpověď (Back)

**Online** lámání hesel znamená, že útočník aktivně komunikuje s procesem nebo vzdáleným systémem, což zamená, že je limitován rychlostí přenosu. **Offline **lámáním hesel se většinou rozumí útok na lokální databázi hesel, kterou má útočník pod kontrolou, a proto může útok urychlit pomocí paralelních výpočtů. V tomto případě se útočník snaží z hashů v databázi zpětně získat hesla.

## Poznámka Anki 1701094542848

Karty Anki: 1701094542848
GUID: z(Pj9(U5NH; štítky: bi-asb::p08.

Metadata původního zdroje pro kartu 1701094542848: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

V jakém formátu jsou ukládána hesla v \(\mathtt{/etc/shadow}\)?

### Odpověď (Back)

Hesla v souboru \(\mathtt{/etc/shadow}\) mají následující formát:
\[\mathtt{\$<algoritmus>\$<sul>\$<hash>}.\]

## Poznámka Anki 1701094724254

Karty Anki: 1701094724255
GUID: uQR9Qz!w^x; štítky: bi-asb::p08.

Metadata původního zdroje pro kartu 1701094724255: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište entropii hesla. Jak se spočte?

### Odpověď (Back)

Entropie hesla vyjadřuje jeho náhodnost či nepředvídatelnost. Spočítat ji můžeme jako počet bitů nutných pro efektivní zakódování hesla:
\[\log_2(L^N),\]kde \(L\) je počet všech znaků, které se v hesle mohou vyskytnout a \(N\) je jeho délka.

## Poznámka Anki 1701095754863

Karty Anki: 1701095754863
GUID: tV+@S8oC}j; štítky: bi-asb::p08 ni-pb::21.

### Otázka (Front)

Popište OAuth a princip jeho fungování.

### Odpověď (Back)

Oauth (Open Authorization) je otevřený standard protokolu, který se používá k delegaci autorizace. Předpokládejme uživatele s účtem v aplikaci \(A\), který chce prostředníctvím aplikace \(B\) třetí strany používat prostředky ze svého účtu v aplikaci \(A\). Postup vypadá následovně:

- Aplikace \(B\) požádá uživatele o autorizaci.
- Uživatel poskytne autorizaci aplikaci \(B\).
- Na základě toho si aplikace \(B\) od autorizačního serveru aplikace \(A\) vyžádá access token.
- Prostřednictvím access tokenu se aplikace \(B\) autorizuje na serveru aplikace \(A\) a získá požadované prostředky.

## Poznámka Anki 1701099595282

Karty Anki: 1701099595282
GUID: B4nnn)7M={; štítky: bi-asb::p08.

Metadata původního zdroje pro kartu 1701099595282: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište autentizační faktor. Jaké existují skupiny autentizančích faktorů?

### Odpověď (Back)

Autentizační faktor je informace, která se dá použít k autentizaci identity. Existují tři skupiny autentizačních faktorů:

- **znalost** - něco, co uživatel a pouze uživatel zná;

- **vlastnictví** - něco, co uživatel a pouze uživatel má;
- **biometrika** - něco, čím uživatel a pouze uživatel je.

## Poznámka Anki 1701103524266

Karty Anki: 1701103524266
GUID: uy~S4Z6}t=; štítky: bi-asb::p08.

### Otázka (Front)

Popište výpočet LAN Manager hash (LM hash).

### Odpověď (Back)

LAN Manager hash (LM hash) lze spočítat z uživatelského hesla, jehož délka je omezena na 14 znaků, následujícím způsobem:

- Heslo se převede na velká písmena.
- Heslo se doplní zprava nulovými byty na délku 14 znaků.
- Heslo se rozdělí na dvě poloviny, ze kterých se vytvoří klíče šifry DES.
- Oba klíče se postupně použijí k zašifrování konstantního řetězce \(\mathtt{KGS!@\#\$\%}\).
- Výsledné řetězce se spojí za sebe a vzniká LM hash.

