# NI-SBF – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-sbf/NI-SBF.apkg; APKG SHA-256 eea8ecb13bdb56a02027b1cf6860588c0d4e44a6ec0b1d9b60c8cf7bc0df0806. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e39cc77808ce484ac431215d36a50c128a0bf18ed66d8b544ffa1d5eb2a9d7be.
Původní balíčky: NI-SBF
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1731505144659

Karty Anki: 1731505144659
GUID: h4@,v@V94&; štítky: ni-sbf::p08.

Metadata původního zdroje pro kartu 1731505144659: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the symmetric Needham-Schroeder protocol.

### Odpověď (Back)

Suppose three subjects \(A\), \(B\) and a trusted third party \(S\). Suppose further that both \(A\) and \(B\) already have established shared keys with \(A\), namely \(K_{AS}\) and \(K_{BS}\). The symmetric Needham-Schroeder protocol enables \(A\) to securely communicate with \(B\) as follows:

- Subject \(A\) sends its own identity, the identity of the other party \(B\), and a nonce \(N_A\) to \(S\).

\[A \to S : A, B, N_A\]

- Subject \(S\) resopnds with a repeated nonce \(N_A\), a key which will be later used to encrypt communication \(K_{AB}\), the identity of \(B\), and a cryptogram which contains \(K_{AB}\) and the identity of \(A\) encrypted using \(K_{BS}\). This cryptogram is intended to be read by \(B\). The message as a whole is encrypted using \(K_{AS}\).

\[S \to A : \{N_A, K_{AB}, B, \{K_{AB}, A\}_{K_{BS}}\}_{K_{AS}}\]

- Subject \(A\) sends the cryptogram containing \(K_{AB}\) and the identity of \(A\) encrypted using \(K_{BS}\) to \(B\).

\[A \to B : \{K_{AB}, A\}_{K_{BS}}\]

- Subject \(B\) responds with a nonce \(N_B\) and the identity of \(A\) encrypted using \(K_{AB}\).

\[B \to A : \{N_B, A\}_{K_{AB}}\]

- Subject \(A\) responds back with a modified nonce \(N_B\) (e.g. decremented) encrypted using \(K_{AB}\).

\[A \to B : \{N_B - 1\}_{K_{AB}}\]

## Poznámka Anki 1731506142079

Karty Anki: 1731506142079
GUID: us-05OHAeQ; štítky: ni-pb::21 ni-sbf::p08.

### Otázka (Front)

Describe the Denning-Sacco protocol.

### Odpověď (Back)

Denning-Sacco protocol is an authentication protocol that improves the symmetric Needham-Schroeder protocol by adding timestamps. This mitigates the risk of replay attacks.

## Poznámka Anki 1731506663050

Karty Anki: 1731506663050
GUID: l&,<R8HD)(; štítky: ni-sbf::p08.

Metadata původního zdroje pro kartu 1731506663050: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

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

## Poznámka Anki 1731506960872

Karty Anki: 1731506960873
GUID: iPQ@RFYJA[; štítky: ni-pb::21 ni-sbf::p08.

### Otázka (Front)

Describe a Kerberos realm.

### Odpověď (Back)

Kerberos realm is a set of managed nodes that share the same Kerberos database. Interoperating realms share a secret key which enables clients to authenticate locally and then interact with services in remote realms by requesting a ticket-granting ticket for a remote ticket-granting server.

## Poznámka Anki 1731507346363

Karty Anki: 1731507346363
GUID: or(0}>/4bV; štítky: ni-pb::21 ni-sbf::p08.

### Otázka (Front)

Describe the pass-the-ticket attack.

### Odpověď (Back)

Pass-the-ticket attack is an attack that is associated with the Kerberos protocol in which the attacker extracts a ticket-granting ticket from the memory of the Local Security Authority (LSA) process (e.g. using \(\mathtt{mimikatz}\)). This can be used to request a service ticket and bypass authentication.

## Poznámka Anki 1731507392921

Karty Anki: 1731507392921
GUID: pl,<(MoUB]; štítky: ni-sbf::p08.

Metadata původního zdroje pro kartu 1731507392921: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is a golden ticket in Kerberos? How can it be obtained?

### Odpověď (Back)

A golden ticket is a forged Kerberos ticket that provides the highest level of access within an Active Directory environment allowing an attacker to impersonate any user account in the domain. It can be obtained as follows:

- First, the attacker needs to compromise the domain controller.
- The attacker then needs to crack the hash of the \(\mathtt{krbtgt}\) account which is a default account used to authenticate Kerberos tickets.
- Thereafter, the attacker can forge a service ticket that has a long duration (typically 10 years).

## Poznámka Anki 1731507410000

Karty Anki: 1731507410000
GUID: B-oA>z)93b; štítky: ni-sbf::p08.

Metadata původního zdroje pro kartu 1731507410000: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is a silver ticket in Kerberos? How can it be obtained?

### Odpověď (Back)

A silver ticket is a forged Kerberos ticket that allows the attacker to authenticate as a specific service on a compromised system. It can be obtained as follows:

- First, the attacker needs to retrieve a hash of a service account and crack it.
- Then the attacker can forge a service ticket that allows them to authenticate as the compromised service.

## Poznámka Anki 1731507734783

Karty Anki: 1731507734783
GUID: jkzZ2z>CBG; štítky: ni-sbf::p08.

Metadata původního zdroje pro kartu 1731507734783: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is Kerberoasting?

### Odpověď (Back)

Kerberoasting is an attack that is associated with the Kerberos authentication protocol. It is targeted at accounts that have Service Principal Names (SPN) registered, because these accounts often have non-expiring passwords. The attack can be carried out as follows:

- The attacker enumerates accounts with associated SPNs and chooses a target.
- The attacker requests a service ticket from the domain controller for the account.
- The attacker receives the message which contains an encrypted hash of the account's password.
- The attacker proceeds to recover the password using an offline brute-force or dictionary attack.

## Poznámka Anki 1731507844700

Karty Anki: 1731507844700
GUID: H^;u#2p:F@; štítky: ni-sbf::p08.

Metadata původního zdroje pro kartu 1731507844700: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe Microsoft Credential Guard.

### Odpověď (Back)

Microsoft Credential Guard is a Microsoft security measure that uses virtualization-based security (VBS) to provide an isolated storage for the Local Security Authority (LSA) to store secrets (such as password hashes or Kerberos ticket-granting tickets).

