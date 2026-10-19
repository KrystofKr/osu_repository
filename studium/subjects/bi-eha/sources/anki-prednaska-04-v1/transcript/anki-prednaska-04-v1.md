# BI-EHA – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-eha/BI-EHA.apkg; APKG SHA-256 c1faeda627c79eb61a7fd805476dd25213c149be4f50abfcbce04d85b2c27853. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 5c983498accbbf883eb18eb0e5351b8f14653c14dcca6e88ff363b189b4adf5b.
Původní balíčky: BI-EHA
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1679041663589

Karty Anki: 1679041663589
GUID: qy,a1):b,z; štítky: bi-eha::p04 bi-ib::10 bi-ib::16.

### Otázka (Front)

Describe cross-site scripting (XSS). What types are there? How can it be mitigated?

### Odpověď (Back)

Cross-site scripting (XSS) attacks are a type of injection attack in which
malicious scripts are injected into otherwise trusted
websites. We discern:

- reflected XSS,
- stored XSS,
- DOM-based XSS.

XSS can usually be mitigated using the following methods:

- escaping dangerous characters,
- encoding data on output,
- allow-listing only selected tags and attributes,
- using Content Security Policy (CSP) and other HTTP headers.

## Poznámka Anki 1679042136640

Karty Anki: 1679042136640
GUID: C9^[[*7qGP; štítky: bi-eha::p04 bi-ib::10 bi-ib::16.

### Otázka (Front)

Describe stored (persistent) cross-site scripting (XSS).

### Odpověď (Back)

Stored (persistent) cross-site scripting (XSS) attack is an XSS attack where the injected script is permanently stored on the target server, such as in a database, message forum, visitor log, or comment field. The malicious script gets exectuted when a victim retireves the stored data.

## Poznámka Anki 1679042410701

Karty Anki: 1679042410701
GUID: O9+KB+$!Ke; štítky: bi-eha::p04 bi-ib::10 bi-ib::16.

### Otázka (Front)

Describe reflected (non-persistent) cross-site scripting (XSS).

### Odpověď (Back)

Reflected (non-persistent) cross-site scripting (XSS) attack is an XSS attack where the injected script is reflected off the web server, such as in an error message, search result, loaded image, or any other response that includes or is influenced by user input sent to the server.

## Poznámka Anki 1679043354962

Karty Anki: 1679043354962
GUID: nfR={Gs45g; štítky: bi-eha::p04 bi-ib::10 bi-ib::16.

### Otázka (Front)

Describe DOM-based cross-site scripting (XSS).

### Odpověď (Back)

DOM-based cross-site scripting (XSS) attack is an XSS attack, where the payload is executed as a result of modifying the DOM environment in the victim's browser. It typically arises when unvalidated input is passed to JavaScript functions that either support dynamic code execution (i.e. \(\texttt{eval}\)) or write their results back into the DOM (i.e. the \(\texttt{innerHTML}\) attribute).

## Poznámka Anki 1685718558404

Karty Anki: 1685718558404
GUID: hJF~v|ySmR; štítky: bi-eha::p04 bi-ib::10 bi-ib::16.

### Otázka (Front)

Describe SQL injection. How can it be mitigated?

### Odpověď (Back)

SQL injection is a type of injection attack in which malicious SQL queries are entered into an application and executed on the underlying database server as a result of improper input validation. This attack can be usually mitigated using the following methods:

- principle of least privilege,
- input validation,
- escaping of characters that could disrupt the structure of the SQL query,
- parameterized (prepared) statements,
- specialized tools (\(\texttt{sqlmap}\), application firewall).

## Poznámka Anki 1717686773067

Karty Anki: 1717686773067
GUID: KgLmxrqo4.; štítky: bi-eha::p04 bi-ib::10 bi-ib::16.

### Otázka (Front)

Describe command injection.

### Odpověď (Back)

Command injection is a type of injection attack in which malicious shell commands are entered into an application and executed by the operating system as a result of improper input validation. This attack can be usually mitigated using the following methods:

- input validation,
- allow-listing permitted values.

