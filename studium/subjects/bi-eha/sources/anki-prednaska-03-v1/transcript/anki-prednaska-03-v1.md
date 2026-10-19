# BI-EHA – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-eha/BI-EHA.apkg; APKG SHA-256 c1faeda627c79eb61a7fd805476dd25213c149be4f50abfcbce04d85b2c27853. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 5c983498accbbf883eb18eb0e5351b8f14653c14dcca6e88ff363b189b4adf5b.
Původní balíčky: BI-EHA
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678438293028

Karty Anki: 1678438293028
GUID: EkJV|oz#vB; štítky: bi-eha::p03.

### Otázka (Front)

What is the difference between the \(\mathtt{GET}\) and \(\mathtt{POST}\) HTTP methods? What other HTTP methods are there?

### Odpověď (Back)

The \(\mathtt{GET}\) method is used to request data from the server and shouldn't change its state. The \(\mathtt{POST}\) method on the other hand, is used for creating, updating, or deleting a resource on the server. Other HTTP methods include \(\mathtt{HEAD}\), \(\mathtt{PUT}\), or \(\mathtt{DELETE}\).

## Poznámka Anki 1678438591626

Karty Anki: 1678438591627
GUID: mo;Obgvo]h; štítky: bi-eha::p03 bi-ib::16.

### Otázka (Front)

What is same-origin policy (SOP)?

### Odpověď (Back)

Same-origin policy is a web browser policy that permits scripts contained in a first web page to access data in a second web page, but only if both web pages have the same origin. Origin is defined as a combination of the URL scheme, host name and port number.

## Poznámka Anki 1678441235041

Karty Anki: 1678441235041
GUID: w_5Yt2kHYA; štítky: bi-eha::p03 bi-ib::16.

### Otázka (Front)

What is session management? How does it work in HTTP?

### Odpověď (Back)

Session management is the process of securely handling multiple requests to web-based applications from a single user. Because HTTP is a stateless protocol, session management is usually done using a session identifier or token.

## Poznámka Anki 1678450087561

Karty Anki: 1678450087561
GUID: B~x9wSz~0<; štítky: bi-eha::p03 bi-ib::10 bi-ib::16.

### Otázka (Front)

What is cross-site request forgery (CSRF)? How can it be mitigated?

### Odpověď (Back)

Cross-site request forgery is an attack that forces an user to execute unwanted actions on a web application in which they're currently authenticated. CSRF can usually be mitigated using the following methods:

- CSRF token - secret unique token is embedded to every form, an attacker cannot reliably predict this token;
- \(\mathtt{SameSite}\) cookie atribute - prevents sending cookies along with the unwanted requests;

- verification of the origin header.

## Poznámka Anki 1685712836843

Karty Anki: 1685712836843
GUID: F7%t6u$fWP; štítky: bi-eha::p03 bi-ib::12.

### Otázka (Front)

What is Server Name Indication (SNI)?

### Odpověď (Back)

Server Name Indication is an extension of the TLS protocol, that allows a client to indicate which hostname they are attempting to connect to at the start of the handshake process. This way the server can present one of many possible certificates on the same IP address and port, allowing multiple HTTPS websites to be served on the same IP address.

## Poznámka Anki 1685713991202

Karty Anki: 1685713991202
GUID: J/M.;T|LVz; štítky: bi-eha::p03 bi-ib::16.

### Otázka (Front)

What is a Uniform Resource Locator (URL)? Describe its structure.

### Odpověď (Back)

A Uniform Resource Locator (URL) is a reference to a web resource that specifies its location and a mechanism for retreiving it. It has the following structure:
\[\underbrace{\mathtt{http}}_\text{scheme}
\, \mathtt{://} \,
\underbrace{
	\underbrace{\mathtt{name:pass}}_\text{user info} 
	\, \mathtt @ \, 
	\underbrace{\mathtt{example.com}}_\text{host}
	\mathtt :
	\underbrace{\mathtt{80}}_\text{port}
}_\text{authority}
\mathtt / \,
\underbrace{\mathtt{index.php}}_\text{path}
\, \mathtt ? \,
\underbrace{\mathtt{par1=val1\&par2=val2}}_\text{query}
\, \mathtt \#
\underbrace{\mathtt{home}}_\text{fragment}\]

## Poznámka Anki 1685714855156

Karty Anki: 1685714855156
GUID: JYdIMizsv}; štítky: bi-eha::p03 bi-ib::16.

### Otázka (Front)

What is cross-origin resource sharing (CORS)?

### Odpověď (Back)

Cross-origin resource sharing (CORS) is an HTTP-header-based mechanism that allows a server to indicate origins from which a web browser should permit loading resources. This introduces flexibility to the same-origin policy.

## Poznámka Anki 1717947693840

Karty Anki: 1717947693840
GUID: g,_32Qa9|K; štítky: bi-eha::p03 bi-ib::16.

### Otázka (Front)

Describe insecure direct object references (IDOR).

### Odpověď (Back)

Insecure direct object references (IDOR) is a type of access control vulnerability that arises when a web application uses an identifier for direct access to an object but does not check for access control or authentication. For example the URL
\[\texttt{https://example.com/static/121.txt}\]suggests that access to other files may be possible by incrementing the number contained in the filename.

