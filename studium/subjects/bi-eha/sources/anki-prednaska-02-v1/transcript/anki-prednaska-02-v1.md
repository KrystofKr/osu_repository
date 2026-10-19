# BI-EHA – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-eha/BI-EHA.apkg; APKG SHA-256 c1faeda627c79eb61a7fd805476dd25213c149be4f50abfcbce04d85b2c27853. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 5c983498accbbf883eb18eb0e5351b8f14653c14dcca6e88ff363b189b4adf5b.
Původní balíčky: BI-EHA
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1677836344306

Karty Anki: 1677836344306
GUID: kVuAQTMNe/; štítky: bi-eha::p02 bi-ib::11 bi-ib::21.

### Otázka (Front)

What is the difference between a packet sniffer and a packet analyzer?

### Odpověď (Back)

A **packet sniffer** only captures and records all selected packets that pass through the network. Whereas **packet analyzer **decodes, processes and analyses the captured packets and structures them into human readable format.

## Poznámka Anki 1677836549425

Karty Anki: 1677836549425
GUID: jJZ6oa_C~;; štítky: bi-eha::p02 bi-ib::11 bi-ib::21.

### Otázka (Front)

What is ARP spoofing? How can it be mitigated?

### Odpověď (Back)

ARP spoofing (ARP cache poisoning or ARP poison routing) is an attack with the goal to associate the attacker's MAC address with the IP address of another host. The attack usually goes as follows:

- The attacker monitors the network for ARP requests.
- Once the attacker detects an ARP request, they generate an ARP reply with their own MAC address.
- The victim updates their ARP cache with the attacker's MAC address, associating it with the targeted IP.

ARP spoofing can be mitigated using the following methods:

- tools to detect ARP spoofing such as an IDS or IPS,
- static ARP entries,
- ARP filtering.

## Poznámka Anki 1677836640030

Karty Anki: 1677836640030
GUID: AS(AdXgh5c; štítky: bi-eha::p02 bi-ib::11 bi-ib::21.

### Otázka (Front)

What is MAC flooding? How can it be mitigated?

### Odpověď (Back)

MAC flooding is an attack aimed at network switches. The attack usually goes as follows:

- The attacker feeds the switch a large amount of frames with different MAC addresses causing its MAC table to fill up forcing out legitimate records.
- The switch has to resort to broadcasting frames to all its interfaces in order to relearn the forced-out records of its MAC table.
- The attacker may use a packet analyzer to capture the data being transmitted.

MAC flooding can usually be mitigated using port-based network access control (802.1X).

## Poznámka Anki 1677844866733

Karty Anki: 1677844866733
GUID: qX_6xN-1il; štítky: bi-eha::p02 bi-ib::11 bi-ib::21 bi-spol::25.

### Otázka (Front)

What is DNS spoofing? How can it be mitigated?

### Odpověď (Back)

DNS spoofing is a group of attacks with the goal to associate a domain name with an IP address injected by the attacker. One of the ways to carry out a DNS spoofing attack is using a MITM approach:

- The attacker monitors the network for DNS requests.
- Once the attacker detects a DNS query, they generate a DNS reply with an altered IP address.
- On the victims machine, the DNS query gets resolved to the IP address injected by the attacker.

DNS spoofing attacks can be usually mitigated using DNSSEC.

## Poznámka Anki 1685709781052

Karty Anki: 1685709781069
GUID: gI${@_7Epn; štítky: bi-eha::p02 bi-ib::11 bi-ib::21.

### Otázka (Front)

What are the differences between packet sniffing on an interface, hub, or switch?

### Odpověď (Back)

Sniffing on an **interface** is usually used to analyse network activity of a single device. Traffic that is directed towards other network nodes won't be caputured using this method. However, a packet sniffer attached to a **hub **will be able to capture all packets passing through it, since a hub replicates inbound data to all ports. If a packet sniffer is attached to a **switch**, it'll only be able to capture data in the corresponding network node.

## Poznámka Anki 1685709996319

Karty Anki: 1685709996319
GUID: qonIPB/m[j; štítky: bi-eha::p02 bi-ib::11 bi-ib::21.

### Otázka (Front)

What is promiscuous mode?

### Odpověď (Back)

Promiscuous mode is a mode of the network interface controller (NIC) that causes the controller to pass all traffic it receives to the OS, rather than only the traffic that is specifically addressed to it.

## Poznámka Anki 1685712316891

Karty Anki: 1685712316891
GUID: vu5`nGG^8b; štítky: bi-eha::p02 bi-ib::11 bi-ib::21 bi-spol::25.

### Otázka (Front)

What is DNS cache poisoning?

### Odpověď (Back)

DNS cache poisoning is a form of DNS spoofing. This attack can be carried out as follows:

- The attacker issues a request to a DNS resolver for a domain.
- The attacker forges a response from the authoritative nameserver of this domain and injects an arbitrary IP address.
- The DNS server saves the association into its cache and serves it to other clients.

