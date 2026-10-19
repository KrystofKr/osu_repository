# BI-ASB – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-asb/BI-ASB.apkg; APKG SHA-256 7a0706fba841a39fa40ea1e5439c99f14f59930aaa7f6d5620a33590d53350fa. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: eea4a1b952e7287bc51501f27ae2f5ec76f032fca049ee9ef600d2729e12ef40.
Původní balíčky: BI-ASB
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1697466656384

Karty Anki: 1697466656384
GUID: d3$|^bu-1D; štítky: bi-asb::p04.

Metadata původního zdroje pro kartu 1697466656384: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to public key infrastructure (PKI)?

### Odpověď (Back)

Public key infrastructure (PKI) je sada procesů, technologií a zásad, které používají pro řízení vydávání, distribuce, použití a odvolávání digitálních certifikátů a klíčů asymetrické kryptografie. Existuje několik přístupů k vytváření PKI. Mezi ty základní patří:

- přístup s použitím certifikačních autorit,
- web of trust,
- simple public key infrastructure.

## Poznámka Anki 1698054256568

Karty Anki: 1698054256568
GUID: i*1Hdrusxp; štítky: bi-asb::p04.

Metadata původního zdroje pro kartu 1698054256568: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

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

## Poznámka Anki 1698055217739

Karty Anki: 1698055217739
GUID: c-YG[._tC+; štítky: bi-asb::p04 bi-ib::12 bi-spol::09.

### Otázka (Front)

Popište strukturu certifikátu podle ITU-T X.509.

### Odpověď (Back)

Podle ITU-T X.509 obsahuje základní verze certifikátu následující položky:

- **version** - verze certifikátu,

- **certificate serial number** - sériové číslo certifikátu,
- **signature algorithm identifier **- identifikátor algoritmu podpisu,

- **issuer name **- název vydavatele,

- **period of validity **- doba platnosti,
- **subject name** - název držitele,
- **subject's public-key info **- informace o veřejném klíči držitele,
- **signature** - podpis certifikační autority.

## Poznámka Anki 1698060426106

Karty Anki: 1698060426106
GUID: vS3o8)VeH3; štítky: bi-asb::p04 bi-ib::12 bi-spol::09.

### Otázka (Front)

Popište web of trust public key infrastructure (PKI).

### Odpověď (Back)

Web of trust** **je decentralizovaný přístup k PKI. Každý subjekt může podepsat veřejný klíč jiného subjektu (key-signing party) a potvrdit tak ztotožnění klíče se subjektem. Na základě těchto ztotožnění a důvěry ztotožňujícím subjektům se pak může každý uživatel rozhodnout, zda bude konkrétnímu subjektu důvěřovat. Implementací web of trust je Pretty Good Privacy (PGP).

## Poznámka Anki 1698061165082

Karty Anki: 1698061165082
GUID: j%;CWByvJ|; štítky: bi-asb::p04 bi-ib::12 bi-spol::09.

### Otázka (Front)

Popište public key infrastructure (PKI) s použitím certifikačních autorit.

### Odpověď (Back)

Public key infrastructure (PKI) s použitím certifikačních autorit je centralizovaný přístup k PKI. Klíče subjektů podepisuje příslušná certifikační autorita a ztotožňuje tak klíč se subjektem. Pokud tedy subjekty důvěřují certifikační autoritě, pak důvěřují i všem certifikátům, které vydala.

## Poznámka Anki 1698061449214

Karty Anki: 1698061449214
GUID: k<ni=;%;#v; štítky: bi-asb::p04 bi-ib::12 bi-spol::09.

### Otázka (Front)

Popište postup tvorby certifikátu.

### Odpověď (Back)

Certifikát lze vytvořit následujícím způsobem:

- subjekt vygeneruje pár klíčů (veřejný a soukromý);
- subjekt vytvoří certificate signing request (CSR), který doručí certifikační autoritě;
- certifikační autorita ověří identitu subjektu a vytvoří certifikát.

## Poznámka Anki 1698062524299

Karty Anki: 1698062524299
GUID: vf_J5=:^=<; štítky: bi-asb::p04 bi-ib::12 bi-spol::09.

### Otázka (Front)

V jakých formátech se ukládají certifikáty?

### Odpověď (Back)

Pro uložení certifikátu lze vybrat jeden z následujících formátů:

- Distinguished Encoding Rules (DER) - binární forma Abstract Syntax Notation One (ASN.1),

- Privacy-Enhanced Mail (PEM) - DER zakódovaný v base64,

- Public Key Cryptography Standards #12** **(PKCS #12) - formát vytvořený RSA Laboratories.

## Poznámka Anki 1698063212046

Karty Anki: 1698063212046
GUID: t?!tm=$-PX; štítky: bi-asb::p04.

Metadata původního zdroje pro kartu 1698063212046: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to registrační autorita (RA)?

### Odpověď (Back)

Registrační autorita (RA) přijímá požadavky na vydání certifikátů, kontroluje údaje a zadává tvorbu certifikátů certifikační autoritě.

## Poznámka Anki 1698063512262

Karty Anki: 1698063512262
GUID: k[JegACkNv; štítky: bi-asb::p04.

Metadata původního zdroje pro kartu 1698063512262: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte certifikační autoritu (CA).

### Odpověď (Back)

Certifikační autorita (CA) podepisuje, vydává a ukládá certifikáty. Každý subjekt si může ověřit, že byl certifikát vydán příslušnou certifikační autoritou pomocí jejího veřejného klíče.

## Poznámka Anki 1698065138009

Karty Anki: 1698065138009
GUID: wdm9ssLe*r; štítky: bi-asb::p04 bi-ib::12 bi-spol::09.

### Otázka (Front)

Popište certificate revocation list (CRL).

### Odpověď (Back)

Certificate revocation list (CRL) je struktura, která obsahuje seznam revokovaných certifikátů, tedy certifikátů, které byly zrušeny před uplynutím doby jejich platnosti. Obsahuje následující položky:

- **version** - verze CRL,

- **signature algorithm identifier** - identifikátor algoritmu podpisu,

- **this update date **- datum platnosti,
- **next update date** - datum příští aktualizace,

- **certificate revocation list entries **- dvojice sériového čísla a data revokace revokovaných certifikátů,
- **signature **- podpis certifikační autority.

## Poznámka Anki 1698065447910

Karty Anki: 1698065447910
GUID: B6n?lqIHKP; štítky: bi-asb::p04 bi-ib::12 bi-spol::09.

### Otázka (Front)

Popište Online Certificate Status Protocol (OSCP).

### Odpověď (Back)

Online Certificate Status Protocol (OSCP) je protokol, který se používá pro zjištění revokačního stavu konkrétního certifikátu. Poskytuje alternativu k certificate revocation listům, nicméně jeho využívání zatěžuje certifikační autoritu.

## Poznámka Anki 1698066368808

Karty Anki: 1698066368808
GUID: M)>JpSPDs:; štítky: bi-asb::p04 bi-ib::12 bi-spol::09.

### Otázka (Front)

Popište postup ověření certifikátu.

### Odpověď (Back)

Při ověřování certifikátu je postupně vykonána kontrola:

- důvěryhodnosti vydavatele certifikátu,
- integrity certifikátu,
- platnosti certifikátu,
- revokace certifikátu.

## Poznámka Anki 1698066584321

Karty Anki: 1698066584321
GUID: gHU7?[vA`H; štítky: bi-asb::p04 bi-ib::12.

### Otázka (Front)

Popište trust anchor.

### Odpověď (Back)

Trust anchor je subjekt, kterému je důvěřováno explicitně, tedy jeho důvěryhodnost není odvozena od jiného subjektu, např. kořenový certifikát v řetězci certifikátů.

