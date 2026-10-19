# BI-EHA – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-eha/BI-EHA.apkg; APKG SHA-256 c1faeda627c79eb61a7fd805476dd25213c149be4f50abfcbce04d85b2c27853. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 5c983498accbbf883eb18eb0e5351b8f14653c14dcca6e88ff363b189b4adf5b.
Původní balíčky: BI-EHA
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1683272181496

Karty Anki: 1683272181496
GUID: Q[!%L5-<TA; štítky: bi-eha::p10.

### Otázka (Front)

What is Active Directory?

### Odpověď (Back)

Active Directory is a directory service developed by Microsoft for Windows domain networks. It uses Kerberos 5 as an authentication protocol.

## Poznámka Anki 1683272352855

Karty Anki: 1683272352855
GUID: Mj)Xx;WdR*; štítky: bi-eha::p10.

### Otázka (Front)

What is a Key Distribution Center and what are its components?

### Odpověď (Back)

The Key Distribution Center is the main Kerberos service. It consists of:

- **authentication server** - issues ticket-granting tickets,

- **ticket-granting server** - issues service tickets,

- **database**.

## Poznámka Anki 1683273091414

Karty Anki: 1683273091414
GUID: kd}R^J+Lm1; štítky: bi-eha::p10 ni-pb::21.

### Otázka (Front)

Describe the process of Kerberos authentication.

### Odpověď (Back)

The Kerberos authentication process goes as follows:

- The client sends an authentication server request to the domain controller. This request contains an encrypted timestamp.
- The domain controller replies with an authentication server reply** **containing a ticket-granting ticket.
- The client sends a ticket-granting server request to the domain controller. This request contains the ticket-granting ticket.
- The domain controller replies with a ticket-granting server reply containing a service ticket.
- Using the service ticket the client may issue application server requests to the application server.
- The application server may reply with application server replies if mutual authentication is required.

 [Obrázek: paste-ed493e989608f0682037ca8a4a16004f7b1c16e5.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1683274117711

Karty Anki: 1683274117711
GUID: EJJVcn@D<); štítky: bi-eha::p10.

### Otázka (Front)

What is Kerberos delegation?

### Odpověď (Back)

Kerberos delegation is a feature of the Kerberos authentication protocol that allows a service to forward the credentials of a client to another service on behalf of the client. This way the client is able to access additional resources without the need for reauthentication.

## Poznámka Anki 1683274696928

Karty Anki: 1683274696928
GUID: e*dyhvi?e!; štítky: bi-eha::p10.

### Otázka (Front)

What types of Kerberos delegation are there?

### Odpověď (Back)

Kerberos supports the following types of delegation:

- **unconstrained delegation** - ticket-granting tickets get stored in memory so that the service can authenticate on behalf of the client without any limitations,

- **constrained delegation **- allows the client to configure which services their account can be delegated to,

- **resource-based constrained delegation** - allows the service  to configure trusted sources of delegation.

## Poznámka Anki 1685910327191

Karty Anki: 1685910327191
GUID: CJ7hwqd)i=; štítky: bi-eha::p10.

Metadata původního zdroje pro kartu 1685910327191: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the methodology used for testing Lightweight Directory Access Protocol (LDAP).

### Odpověď (Back)

Testing LDAP usually follows these steps:

- **reconnaissance** - gather information about the LDAP implementation,

- **enumeration** - gather information about the directory structure, user accounts and groups,

- **exploitation** and **privilege escalation** - test for LDAP injection, data manipulation, or server-side vulnerabilities.

## Poznámka Anki 1685912485538

Karty Anki: 1685912485538
GUID: s#>^ULrF)n; štítky: bi-eha::p10 ni-pb::21.

### Otázka (Front)

How can Kerberos delegation be exploited?

### Odpověď (Back)

Kerberos delegation can be exploited in the following ways:

- misconfigured delegation settings may allow unauthorized services to request delegated credentials,
- an attacker may extract credentials stored for delegation from the service's memory.

## Poznámka Anki 1685913099627

Karty Anki: 1685913099627
GUID: Ii2`c6RBvY; štítky: bi-eha::p10 ni-pb::21.

### Otázka (Front)

What is ASREPRoasting?

### Odpověď (Back)

ASREPRoasting is an attack that is associated with the Kerberos authentication protocol. It is targeted at accounts that have preauthentication disabled which means that they don't have to verify their identity in the authentication process. The attack can be carried out as follows:

- The attacker seeks out (guesses) an account with preauthentication disabled.
- The attacker requests the AS-REP (authentication server reply) from the domain controller for the account.
- The attacker receives the message which contains an encrypted hash of the account's password.
- The attacker proceeds to recover the password using an offline brute-force or dictionary attack.

## Poznámka Anki 1685913875770

Karty Anki: 1685913875771
GUID: mDCW8F8O?W; štítky: bi-eha::p10 ni-pb::21.

### Otázka (Front)

What is Kerberoasting?

### Odpověď (Back)

Kerberoasting is an attack that is associated with the Kerberos authentication protocol. It is targeted at accounts that have Service Principal Names (SPN) registered, because these accounts often have non-expiring passwords. The attack can be carried out as follows:

- The attacker enumerates accounts with associated SPNs and chooses a target.
- The attacker requests a service ticket from the domain controller for the account.
- The attacker receives the message which contains an encrypted hash of the account's password.
- The attacker proceeds to recover the password using an offline brute-force or dictionary attack.

## Poznámka Anki 1685914266540

Karty Anki: 1685914266540
GUID: u7iMBHRgzO; štítky: bi-eha::p10 ni-pb::21.

### Otázka (Front)

What is a silver ticket in Kerberos? How can it be obtained?

### Odpověď (Back)

A silver ticket is a forged Kerberos ticket that allows the attacker to authenticate as a specific service on a compromised system. It can be obtained as follows:

- First, the attacker needs to retrieve a hash of a service account and crack it.
- Then the attacker can forge a service ticket that allows them to authenticate as the compromised service.

## Poznámka Anki 1685914725910

Karty Anki: 1685914725910
GUID: id1A1VR/>R; štítky: bi-eha::p10 ni-pb::21.

### Otázka (Front)

What is a golden ticket in Kerberos? How can it be obtained?

### Odpověď (Back)

A golden ticket is a forged Kerberos ticket that provides the highest level of access within an Active Directory environment allowing an attacker to impersonate any user account in the domain. It can be obtained as follows:

- First, the attacker needs to compromise the domain controller.
- The attacker then needs to crack the hash of the \(\mathtt{krbtgt}\) account which is a default account used to authenticate Kerberos tickets.
- Thereafter, the attacker can forge a service ticket that has a long duration (typically 10 years).

