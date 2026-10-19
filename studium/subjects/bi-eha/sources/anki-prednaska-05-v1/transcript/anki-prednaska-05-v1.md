# BI-EHA – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-eha/BI-EHA.apkg; APKG SHA-256 c1faeda627c79eb61a7fd805476dd25213c149be4f50abfcbce04d85b2c27853. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 5c983498accbbf883eb18eb0e5351b8f14653c14dcca6e88ff363b189b4adf5b.
Původní balíčky: BI-EHA
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1680250594824

Karty Anki: 1680250594824
GUID: uc28:GY3Wz; štítky: bi-eha::p05 bi-ib::10 bi-ib::16.

### Otázka (Front)

What is a server-side request forgery (SSRF) attack? How can it be mitigated?

### Odpověď (Back)

Server-side request forgery (SSRF) attack is an attack where the attacker can abuse
functionality on the server to read or update internal resources that weren't otherwise publicly available, or execute requests to arbitrary locations. SSRF can usually be mitigated using the following methods:

- limit the network access of the server (using a firewall),
- principle of least privilege,
- input validation.

## Poznámka Anki 1680250818203

Karty Anki: 1680250818203
GUID: g?)EsWk$41; štítky: bi-eha::p05 bi-ib::10 bi-ib::16.

### Otázka (Front)

Describe XML external entity (XXE) attack.

### Odpověď (Back)

XML external entity (XXE) attack is a type of injection attack. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured parser. This may lead to information disclosure, DoS, or SSRF.

## Poznámka Anki 1685719951110

Karty Anki: 1685719951110
GUID: +Rw;q%`WW; štítky: bi-eha::p05.

Metadata původního zdroje pro kartu 1685719951110: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is a file inclusion attack? How can it be mitigated?

### Odpověď (Back)

A file inclusion attack is an attack targeted at applications that internally operate with files that can be selected using unvalidated user input. We discern:

- **local file inclusion** (LFI) - the attacker executes or displays a locally available file (typically leads to information disclosure),

- **remote file inclusion** (RFI) - the attacker executes or displays a file that isn't availabe on the vulnerable machine, instead, it may be hosted externally by the attacker (typically leads to remote code execution or information disclosure).

File inclusion vulnerabilities can usually be mitigated using the following methods:

- avoid directly using filenames and URLs,
- consider using a \(\mathtt{chroot}\) jail,
- use an allow-list of includable files.

## Poznámka Anki 1717948410504

Karty Anki: 1717948410504
GUID: MByR#t[%Dq; štítky: bi-eha::p05 bi-ib::16.

### Otázka (Front)

List commonly used HTTP security headers.

### Odpověď (Back)

Commonly used HTTP security headers include:

- \(\texttt{Strict-Transport-Security}\),

- \(\texttt{X-Frame-Options}\),

- \(\texttt{X-Content-Type-Options}\),

- \(\texttt{Content-Security-Policy}\)

and others.

## Poznámka Anki 1717948639958

Karty Anki: 1717948639959
GUID: K94HwX_3Pv; štítky: bi-eha::p05.

Metadata původního zdroje pro kartu 1717948639959: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the HTTP \(\texttt{Strict-Transport-Security}\) (HSTS) header.

### Odpověď (Back)

The HTTP \(\texttt{Strict-Transport-Security}\) header (HSTS) indicates, that a given page should only be accessed via HTTPS and all further HTTP requests should be converted to HTTPS.

## Poznámka Anki 1717948827289

Karty Anki: 1717948827289
GUID: r7Ri=Rsb!+; štítky: bi-eha::p05 bi-ib::16.

### Otázka (Front)

Describe the HTTP \(\texttt{X-Frame-Options}\) header.

### Odpověď (Back)

The HTTP \(\texttt{X-Frame-Options}\) header controls whether the content of the webpage can be displayed within frames (such as \(\texttt{<frame>}\), \(\texttt{<embed>}\), or \(\texttt{<object>}\)). This is used to prevent clickjacking.

## Poznámka Anki 1717949003071

Karty Anki: 1717949003071
GUID: h~xyW5s~e5; štítky: bi-eha::p05 bi-ib::16.

### Otázka (Front)

Describe the HTTP \(\texttt{X-Content-Type-Options}\) header.

### Odpověď (Back)

The HTTP \(\texttt{X-Content-Type-Options}\) header prevents the browser from interpreting files as a different MIME type to what is specified in the \(\texttt{Content-Type}\) header. This is used to ensure that non-executable MIME types aren't interpreted as executable MIME types.

## Poznámka Anki 1717949839136

Karty Anki: 1717949839136
GUID: d}0`Kw7=!c; štítky: bi-eha::p05.

Metadata původního zdroje pro kartu 1717949839136: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the HTTP \(\texttt{Content-Security-Policy}\) (CSP) header.

### Odpověď (Back)

The HTTP \(\texttt{Content-Security-Policy}\) header restricts which resources can be loaded on a given webpage and the URLs that they can be loaded from. The CSP header is used in place of the \(\texttt{X-XSS-Protection}\) header as a protection against cross-site scripting. Possible attributes of this header include \(\texttt{script-src}\), \(\texttt{img-src}\), or \(\texttt{font-src}\).

## Poznámka Anki 1717950717233

Karty Anki: 1717950717233
GUID: N2a[~oE3rp; štítky: bi-eha::p05 bi-ib::16.

### Otázka (Front)

Describe server-side template injection (SSTI).

### Odpověď (Back)

Server-side template injection (SSTI) is a type of injection attack in which malicious payloads are injected into a template and executed on the server by a template engine as a result of improper input validation. This attack can be usually mitigated using the following methods:

- using a "logic-less" template engine (such as Mustache),
- running the template engine in a virtualized environment.

## Poznámka Anki 1717950912035

Karty Anki: 1717950912035
GUID: Jv*nXppKti; štítky: bi-eha::p05 bi-ib::16.

### Otázka (Front)

Describe open redirection.

### Odpověď (Back)

Open redirection vulnerabilities arise when unvalidated input is passed to JavaScript functions that trigger redirections. This can be used to mount phishing attacks.

