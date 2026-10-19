# NI-SIB – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-sib/NI-SIB.apkg; APKG SHA-256 95641176062256a9121d10e445a549c19414498695e2c1d4e0fbc7a358695d55. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 1ab77a94174f56eddeeb294fe26c793d378425a79850f93803dec00e9a62ed4d.
Původní balíčky: NI-SIB
Rozsah: 17 poznámek, 17 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1741126323451

Karty Anki: 1741126323451
GUID: F@~}4@]4-Q; štítky: ni-sib::p03.

Metadata původního zdroje pro kartu 1741126323451: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe port scanning.

### Odpověď (Back)

Port scanning is a technique used to detect open ports on a remote device. Its goal is to identify services running on the device. With regard to the type of the scan, we discern:

- **horizonal scanning** - scanning a given port across multiple devices,

- **vertical scanning** - scanning multiple ports on a given device.

Additionally, we discern the following types of scans by the protocol used:

- TCP scan,
- UDP scan.

An effective defence agains port scanning can be provided by a firewall, IDS, or IPS.

## Poznámka Anki 1741126759402

Karty Anki: 1741126759402
GUID: lq[9blE,/{; štítky: ni-sib::p03.

### Otázka (Front)

Describe the difference between TCP and UDP port scanning.

### Odpověď (Back)

**TCP port scanning** is typically carried out by sending TCP SYN packets. If the target device responds with a SYN ACK packet, the port is deemed open. **UDP port scanning**, on the other hand, considers ports to be open if they either return a UDP response or if they do not return any response at all. If there is no filtering in place, closed UDP ports will respond with a special ICMP error message.

## Poznámka Anki 1741127234668

Karty Anki: 1741127234668
GUID: QfG1-*4#[`; štítky: ni-sib::p03.

### Otázka (Front)

Describe the port states defined by \(\texttt{nmap}\).

### Odpověď (Back)

Port states defined by \(\texttt{nmap}\) include:

- **open** - probe packets were received, an application is listening on this port;

- **closed** - probe packets were not received, an application is not listening on this port;

- **filtered** - probe packets were not received, communication is probably being dropped by a firewall or router;
- **unfiltered** - probe packets were received, can be either open or closed.

## Poznámka Anki 1741127798896

Karty Anki: 1741127798896
GUID: fZ35,%765M; štítky: ni-sib::p03.

### Otázka (Front)

Describe TCP port scan types supported by \(\texttt{nmap}\).

### Odpověď (Back)

TCP port scan types supported by \(\texttt{nmap}\) include:

- **SYN scan** - sets the \(\texttt{SYN}\) flag,
- **null scan** - doesn't set any flags,

- **FIN scan** - sets the \(\texttt{FIN}\) flag,

- **XMAS scan** - sets the \(\texttt{FIN}\), \(\texttt{PSH}\), and \(\texttt{URG}\) flags.

The advantage of the null, FIN, and XMAS scans is that they can bypass certain firewalls that attempt to prevent port scanning by filtering packets with the \(\texttt{SYN}\) flag set.

## Poznámka Anki 1741128250281

Karty Anki: 1741128250282
GUID: pmvlgOG4cE; štítky: ni-sib::p03.

### Otázka (Front)

Describe ARP scanning and ARP fingerprinting.

### Odpověď (Back)

**ARP scanning** is a technique used to detect active hosts in a subnet. It works by sending an ARP request for each possible IP address and analyzing the responses received. **ARP fingerprinting **extends ARP scanning by attempting to fingerprint hosts through the analysis of their responses to various types of ARP requests.

## Poznámka Anki 1741128750796

Karty Anki: 1741128750796
GUID: hqCRjdn|pH; štítky: ni-sib::p03.

Metadata původního zdroje pro kartu 1741128750796: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a denial-of-service (DoS) attack.

### Odpověď (Back)

Denial-of-service (DoS) attack is an attack againt a computer, application, shared resource, or service with the goal of making it partially or fully inacessible for legitimate users.

## Poznámka Anki 1741162057411

Karty Anki: 1741162057411
GUID: b!d,tx_kg|; štítky: ni-sib::p03.

Metadata původního zdroje pro kartu 1741162057411: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Desrcribe a distributed denial-of-service (DDoS) attack.

### Odpověď (Back)

Distributed denial-of-service (DDoS) attack is a type of denial-of-service (DoS) attack in which the victim is attacked from multiple sources at the same time.

## Poznámka Anki 1741162230568

Karty Anki: 1741162230568
GUID: D=8PZ>)..!; štítky: ni-sib::p03.

### Otázka (Front)

Describe the architecture of a distributed denial-of-service (DDoS) attack.

### Odpověď (Back)

Distributed denial-of-service (DDoS) attacks are usually supported by botnets consisting of the following nodes:

- **master** - manages and controls slaves,

- **slaves** - flood the victim with traffic from a spoofed source IP address.

## Poznámka Anki 1741162613524

Karty Anki: 1741162613525
GUID: NQ6Y(PhV*`; štítky: ni-sib::p03.

Metadata původního zdroje pro kartu 1741162613525: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a SYN flood attack.

### Odpověď (Back)

SYN flood attack is a type of denial-of-service (DoS) attack targeting the implementation of the TCP protocol. It assumes that upon receiving a SYN packet, the target device will allocate resources which get later freed after a timeout occurs. SYN flood works by flooding the target with SYN packets and exhausting the capcacity its \(\texttt{listen}\) queue. As a result the target is forced to refuse new incoming connections.

## Poznámka Anki 1741166723844

Karty Anki: 1741166723844
GUID: O]_X3NGXT,; štítky: ni-sib::p03.

### Otázka (Front)

Describe a UDP flood attack.

### Odpověď (Back)

UDP flood attack is a type of denial-of-service (DoS) attack targeting the implementation of the UDP protocol. The attack works by flooding random UDP ports of the target with UDP packets. Assuming most of the ports are closed, this causes the target to respond with a large volume of ICMP packets eventually leading it to become unreachable for legitimate clients.

## Poznámka Anki 1741166863803

Karty Anki: 1741166863804
GUID: QE?_nRst>4; štítky: ni-sib::p03.

Metadata původního zdroje pro kartu 1741166863804: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the ping of death.

### Odpověď (Back)

Ping of death is a type of denial-of-service (DoS) attack targetting the ICMP protocol (other protocols may be used as well). The attack works by sending a fragmented packet which upon being composed exceeds the maximal length of an IP packet possibly causing buffer overflow.

## Poznámka Anki 1741167043840

Karty Anki: 1741167043840
GUID: GK2XsSmBJP; štítky: ni-sib::p03.

### Otázka (Front)

Describe denial-of-service (DoS) attacks in Wi-Fi networks.

### Odpověď (Back)

Denial-of-service (DoS) attacks in Wi-Fi networks include:

- **deauthentication attacks** - attacker sends a deauthentication frame with a spoofed source address causing the victim to disconnect from the network,

- **jamming** - attacker generates noise on a Wi-Fi channel making it unusable.

## Poznámka Anki 1741167383456

Karty Anki: 1741167383456
GUID: m_sz-GyT=9; štítky: ni-sib::p03.

### Otázka (Front)

Describe application layer denial-of-service (DoS) attacks.

### Odpověď (Back)

Application layer denial-of-service (DoS) attacks include:

- **HTTP **\(\texttt{GET}\)**/**\(\texttt{POST}\)** flooding** - similar to SYN flooding but with HTTP requests;
- **Slowloris** - attacker opens a large number of HTTP connections to the server and keeps them open by only sending small parts of the requests without ever completing them, therefore exhausting the connection pool of the server.

## Poznámka Anki 1741168018483

Karty Anki: 1741168018483
GUID: mB@H-1BPm!; štítky: ni-sib::p03.

Metadata původního zdroje pro kartu 1741168018483: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a reflection (amplification) denial-of-service (RDoS) attack.

### Odpověď (Back)

Reflection (amplification) denial-of-service (RDoS) attack is a type of denial-of-service attack (DoS) which abuses the functionality of certain protocols (e.g. DNS, NTP, or SSDP) whose responses are relatively large even if the requests are small. The attack works sending requests with spoofed source IP addresses to servers running these protocols which in turn flood the victim whose IP address was spoofed in the request with their responses.

## Poznámka Anki 1741168715055

Karty Anki: 1741168715055
GUID: HFQ^-Qm*w9; štítky: ni-sib::p03.

### Otázka (Front)

Describe a distributed reflection denial-of-service (DRDoS) attack and its architecture.

### Odpověď (Back)

Distributed reflection denial-of-service (DRDoS) attack is a combination of the reflection denial-of-service (RDoS) and distributed denial-of-service (DDoS) attacks. Similarly to DDoS, DRDoS is typically supported by botnets consisting of the following nodes:

- **master** - manages and controls slaves,

- **slaves** - each slave launches their own RDoS attack through a reflector node,

- **reflector** - server running a protocol abused in the RDoS attacks, typically not controlled by the master.

## Poznámka Anki 1741169072858

Karty Anki: 1741169072858
GUID: KQ664Xw?f5; štítky: ni-sib::p03.

Metadata původního zdroje pro kartu 1741169072858: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe defences against SYN flood attacks.

### Odpověď (Back)

SYN flood attack defences include:

- **filtering** - prevents the attacker from using a spoofed IP address;

- **increasing the capacity of the **\(\texttt{listen}\) **queue** - not very effective, hard to scale;

- **decreasing the time to timeout** - can deny legitimate requests;

- **recycling oldest half-open connections** - not very effective if the capcacity of the \(\texttt{listen}\) queue is small or the intensity of the attack is high;

- **SYN cache** - replaces the \(\texttt{listen} \) queue with a hash table minimizing the amount of allocated resources;

- **SYN cookies** - the state information of the connection is encoded in the TCP sequence number of the SYN ACK packet and resources are allocated only if the handshake is completed.

## Poznámka Anki 1742136544458

Karty Anki: 1742136544458
GUID: n;La1xTAl6; štítky: ni-sib::p03.

### Otázka (Front)

Describe defences agains distributed denial-of-service (DDoS) attacks .

### Odpověď (Back)

Distributed denial-of-service (DDoS) attack defences include:

- **SYN proxy** - only connections that complete the handshake are forwarded to the endpoint,

- **black hole filtering** - discarding packets based on rules,

- **remote-triggered black hole **(RTBH)** filtering** - black hole filtering on remote routers before the traffic enters the protected network,

- **ISP-based** **protection** - countermeasures provided by the internet service provider (ISP).

