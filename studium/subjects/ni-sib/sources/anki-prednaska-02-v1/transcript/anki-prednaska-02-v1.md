# NI-SIB – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-sib/NI-SIB.apkg; APKG SHA-256 95641176062256a9121d10e445a549c19414498695e2c1d4e0fbc7a358695d55. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 1ab77a94174f56eddeeb294fe26c793d378425a79850f93803dec00e9a62ed4d.
Původní balíčky: NI-SIB
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1740515764889

Karty Anki: 1740515764889
GUID: jGDt8QM:=Y; štítky: ni-sib::p02.

### Otázka (Front)

Describe DNS fast flux and double DNS fast flux.

### Odpověď (Back)

**DNS fast flux** is a botnet-based evasion technique often used to conceal phishing, malware, or command and control servers. It is carried out by frequently reassigning the IP within a DNS record of a domain. The IPs used are pulled from a botnet whose members proxy the comunication to the concealed server. **Double DNS fast flux** involves the additional fast-fluxing of the authoritative DNS server of the concealed domain.

## Poznámka Anki 1740515789887

Karty Anki: 1740515789887
GUID: rF<[OV$7Nj; štítky: ni-sib::p02.

Metadata původního zdroje pro kartu 1740515789887: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is an attack vector? List examples.

### Odpověď (Back)

An attack vector is a path, method, or scenario that can be exploited to penetrate a target system. This includes open ports, running services, unprotected interfaces, etc.

## Poznámka Anki 1740515981510

Karty Anki: 1740515981510
GUID: QxU=3/Y+FA; štítky: ni-sib::p02.

### Otázka (Front)

Describe an indicator of compromise (IoC).

### Odpověď (Back)

Indicator of compromise is a piece of digital evidence that indicates a network or an operating system may have been breached.

## Poznámka Anki 1740516503018

Karty Anki: 1740516503018
GUID: cFHp9wQFsw; štítky: ni-sib::p02.

Metadata původního zdroje pro kartu 1740516503018: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

List basic types of network attacks.

### Odpověď (Back)

Basic types of network attacks include:

- eavesdropping,

- tampering,

- spoofing,

- attacks targeted at passwords,

- denial of service atttacks (DoS),

- man-in-the-middle (MITM),

- hijacking,
and others.

## Poznámka Anki 1740517290977

Karty Anki: 1740517290977
GUID: gww?`}05/X; štítky: ni-sib::p02.

### Otázka (Front)

Describe the approaches to classification of network attacks.

### Odpověď (Back)

Network attacks may be classified based on the following criteria:

- attack vector,
- attack targets,
- used vulnerabilities and exploits.

## Poznámka Anki 1740517341645

Karty Anki: 1740517341645
GUID: Ci+ej,qNg*; štítky: ni-sib::p02.

Metadata původního zdroje pro kartu 1740517341645: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

List common threat actors and their motivation.

### Odpověď (Back)

| 
      **threat actor** | 
      **motivation** | 

| 
      cybercriminals
 | 
      profit | 

| 
      nation-states | 
      geopolitical motivation | 

| 
      terrorist groups | 
      ideological violence | 

| 
      thrill-seekers | 
      satisfaction | 

| 
      insider threats | 
      discontent | 

| 
      hackers | 
      variable motivation |

## Poznámka Anki 1740517874651

Karty Anki: 1740517874651
GUID: d40-&qz=ZS; štítky: ni-sib::p02.

### Otázka (Front)

Describe the approaches for network attack monitoring.

### Odpověď (Back)

Network attack monitoring can be categorized as follows:

- **host-based** - analyzes system logs, uses auditing tools;

- **network-based** - analyzes network nodes and data flowing through the network.

Network-based attack monitoring can be further categorized as follows:

- **active** - runs active analysis, often uses tools such as \(\texttt{ping}\) or \(\texttt{traceroute}\);

- **passive** - passively analyzes data flowing through the network.

## Poznámka Anki 1740518449066

Karty Anki: 1740518449066
GUID: IfT}/@P3Jq; štítky: ni-sib::p02.

### Otázka (Front)

Describe data units used in network attack monitoring.

### Odpověď (Back)

Data units used in network attack monitoring include:

- **counters** - high-level information, cheap implementation (e.g. total number of packets transmitted);

- **IP flows** - aggregated packets with common properties (NetFlow, IPFIX);

- **packets** - packet capture and deep packet inspection (DPI).

## Poznámka Anki 1740518850659

Karty Anki: 1740518850659
GUID: GNFKl{n3WO; štítky: ni-sib::p02.

### Otázka (Front)

Describe an IP flow.

### Odpověď (Back)

IP flow is a set of packets with common properties observed at a given point in a network over a given time period. These properties may be derived form:

- packet header fields (destination IP address),
- inherent characteristics (number of MPLS labels),
- packet treatment (output interface).

A typical flow key consists of the following:

- source and destination IP address,
- source and destination port,
- transport layer protocol.

There are two main IP flow standards:

- NetFlow by Cisco,
- IP flow information export (IPFIX) by IEEE.

## Poznámka Anki 1740518946573

Karty Anki: 1740518946574
GUID: zD8po,gMCC; štítky: ni-sib::p02.

### Otázka (Front)

Describe the classification of IP flows.

### Odpověď (Back)

IP flows can be categorized as follows:

- **uni-flow** - unidirectional communication,

- **bi-flow** - bidirectional communication.

