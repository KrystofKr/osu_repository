# BI-EHA – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-eha/BI-EHA.apkg; APKG SHA-256 c1faeda627c79eb61a7fd805476dd25213c149be4f50abfcbce04d85b2c27853. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 5c983498accbbf883eb18eb0e5351b8f14653c14dcca6e88ff363b189b4adf5b.
Původní balíčky: BI-EHA
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1681461466402

Karty Anki: 1681461466402
GUID: BS0ngn1JZJ; štítky: bi-eha::p07 bi-ib::07 bi-ib::15.

### Otázka (Front)

Describe the OWASP risk rating methodology.

### Odpověď (Back)

According to OWASP, risk is calculated using the following formula:
\[\text{risk} = \text{likelihood} \cdot \text{impact}.\]Risk rating should follow these steps:

- identifying a risk,
- factors for estimating likelihood,
- factors for estimating impact,
- determining the severity of the risk,
- deciding what to fix,
- customizing your risk rating model.

## Poznámka Anki 1681461891414

Karty Anki: 1681461891414
GUID: O1Hd[WrrBX; štítky: bi-eha::p07 bi-ib::07 bi-ib::14 bi-ib::15 bi-ib::26.

### Otázka (Front)

Describe the Common Vulnerability Scoring System (CVSS).

### Odpověď (Back)

Common Vulnerability Scoring System (CVSS) is a widely used industry standard which determines the severity of a vulnerability based on three categories of metrics:

- **base metrics** - characteristics of the vulnerability itself (exploitability, impact),

- **temporal metrics** - characteristics that evolve over time,

- **environmental metrics** - characteristics that are implementation or enviroment-dependent.

## Poznámka Anki 1681462001639

Karty Anki: 1681462001639
GUID: PC{P#@T6Ow; štítky: bi-eha::p07 bi-ib::07 bi-ib::14 bi-ib::15 bi-ib::26.

### Otázka (Front)

What risk rating methodologies exist?

### Odpověď (Back)

Risks can be scored based on the following methodologies:

- **basic scoring**,

- **DREAD**,

- **OWASP**,

- **CVSS**.

## Poznámka Anki 1685799996547

Karty Anki: 1685799996548
GUID: hsXg{A`b7D; štítky: bi-eha::p07.

Metadata původního zdroje pro kartu 1685799996548: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the DREAD risk rating methodology.

### Odpověď (Back)

DREAD rates risks based on the following categories:

- **damage potential**,

- **reproducibility**,

- **exploitability**,

- **affected users**,

- **discoverability**.

In each of these categories the risk is assigned a rating from \(1\) to \(10\). The final score is then calculated as:

\[\text{risk} = \frac {D + R + E + A + D} 5.\]

## Poznámka Anki 1685800505261

Karty Anki: 1685800505261
GUID: L1^A%Tv@0g; štítky: bi-eha::p07 bi-ib::07 bi-ib::14 bi-ib::15 bi-ib::26.

### Otázka (Front)

What is the difference between CVE and NVD?

### Odpověď (Back)

The Common Vulnerabilities and Exposures (**CVE**) database is a database maintained by MITRE that offers a standardized of identifying known vulnerabilities. The National Vulnerability Database (**NVD**) is maintained by a U.S. government-funded organization. It incorporates the CVE database and provides more information on top of it, such as impact assesments, or remediation guidance.

## Poznámka Anki 1717854792608

Karty Anki: 1717854792608
GUID: O@=F=s)wif; štítky: bi-eha::p07 bi-ib::15 bi-ib::26.

### Otázka (Front)

Describe the base metrics of the Common Vulnerability Scoring System Version 3.1 (CVSSv3.1).

### Odpověď (Back)

The base metrics of the Common Vulnerability Scoring System Version 3.1 (CVSSv3.1) are further split into exploitability metrics and impact metrics. The exploitability metrics include:

- **attack vector** - physical, local, adjacent network, network;

- **attack complexity** - low, high;

- **privileges required **- none, low, high;

- **user interaction** - none, required;

- **scope** - unchanged, changed.

The impact metrics include:

- **confidentiality impact** - none, low, high;

- **integrity impact** - none, low, high;
- **availability impact** - none, low, high.

## Poznámka Anki 1717855441641

Karty Anki: 1717855441641
GUID: wQb@}+3+jP; štítky: bi-eha::p07 bi-ib::15.

Metadata původního zdroje pro kartu 1717855441641: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the changes made by the Common Vulnerability Scoring System Version 4 (CVSSv4).

### Odpověď (Back)

The Common Vulnerability Scoring System Version 4 (CVSSv4) introduces the following changes:

- added attack requirements as a base metric,
- enhanced user interaction metric granularity (none, active, passive),
- added safety metrics to support operational technology (OT) systems,
- separated impact metrics to vulnerable system metrics and subsequent system metrics

and others.

