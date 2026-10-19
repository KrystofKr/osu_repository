# BI-ASB – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-asb/BI-ASB.apkg; APKG SHA-256 7a0706fba841a39fa40ea1e5439c99f14f59930aaa7f6d5620a33590d53350fa. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: eea4a1b952e7287bc51501f27ae2f5ec76f032fca049ee9ef600d2729e12ef40.
Původní balíčky: BI-ASB
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1698670621909

Karty Anki: 1698670621909
GUID: JP{n;{IZG~; štítky: bi-asb::p05 bi-ib::12.

### Otázka (Front)

Uveďte možnosti šifrování na jednotlivých vrstvách Open Systems Interconnection (OSI) modelu společně s typickými šifrovacími protokoly.

### Odpověď (Back)

Šifrování lze provádět na všech vrstvách Open Systems Interconnection (OSI) modelu:

|       
      **vrstva** | 
      **význam** |       
      **protokoly** | 

| 
      aplikační | 
      šifrování na úrovni aplikace | 
      různé šifrovací systémy závislé na aplikaci | 

|       
      prezentační | 
      podpora aplikační vrstvy | 
      
 | 

|       
      relační | 
      podpora aplikační vrstvy | 
      
 | 

|       
      transportní | 
      šifrování aplikačního protokolu | 
      SSL/TLS, Datagram Transport Layer Security (DTLS) | 

|       
      síťová | 
      šifrování mezi dvěma síťovými uzly | 
      některé VPN jako např. IPSec | 

|       
      linková | 
      šifrování mezi dvěma síťovými rozhraními | 
      Wi-Fi | 

|       
      fyzická | 
      šifrování fyzického spoje | 
      
 |

## Poznámka Anki 1698671017522

Karty Anki: 1698671017522
GUID: y,`%_lZEU|; štítky: bi-asb::p05.

Metadata původního zdroje pro kartu 1698671017522: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Transport Layer Security (TLS) protokol.

### Odpověď (Back)

Transport Layer Security (TLS) je protokol, který má za cíl zajistit důvěrnost a integritu dat mezi dvěma komunikujicími aplikacemi na transportní vrstvě. Sestává ze dvou vrstev:

- **nižší** - TLS Record Protocol,

- **vyšší** - čtyři TLS protokoly: Handshake, Alert, Change Cipher Spec a Application Data.

## Poznámka Anki 1698673893691

Karty Anki: 1698673893691
GUID: iGpi7}2=kO; štítky: bi-asb::p05 bi-ib::12.

### Otázka (Front)

Popište handshake v Transport Layer Security (TLS) protokolu verze 1.2.

### Odpověď (Back)

Transport Layer Security (TLS) handshake probíhá ve verzi 1.2 následovně:

- Klient posílá zprávu \(\mathtt{ClientHello}\), která obsahuje čas, náhodná data, seznam šifrovacích sad (cipher suites), šifrovacích metod a rozšíření.
- Server posílá zprávu \(\mathtt{ServerHello}\), která obsahuje stejné typy položek jako \(\mathtt{ClientHello}\) ale vztažené k serveru.
- Server posílá zprávu \(\mathtt{Certificate}\), která obsahuje celý certifikační řetězec (certificate chain) typicky bez kořenového certifikátu.
- Pokud \(\mathtt{Certificate}\) neobsahuje dostatek dat pro sjednání pre-master secret (např. v případě Diffie-Hellmanova algoritmu), posílá server zprávu \(\mathtt{ServerKeyExchange}\), která obsahuje výběr algoritmu a jeho parametry (v případě Diffie-Hellmanova algoritmu hodnotu \(y\) serveru, která je podepsána).
- Server posílá zprávu \(\mathtt{ServerHelloDone}\), čímž indikuje ukončení všech hello zpráv.
- Klient posílá zprávu \(\mathtt{ClientKeyExchange}\), která obsahuje buď přímo vygenerovaný pre-master secret nebo parametry klienta sloužící pro jeho generování (např. v případě Diffie-Hellmanova algoritmu).
- Klient posílá zprávu \(\mathtt{ChangeCipherSpec}\), což je poslední nešifrovaná zpráva, kterou klient indikuje, že je připraven navázat šifrované spojení dle sjednaných parametrů.
- Klient posílá zprávu \(\mathtt{Finished}\), která obsahuje hash doposud poslaných zpráv zašifrovaný pomocí sjednaných parametrů.
- Server ověří zprávu \(\mathtt{Finished}\) od klienta a obdobným způsobem posílá zprávy \(\mathtt{ChangeCipherSpec}\) a \(\mathtt{Finished}\).
- Klient ověří zprávu \(\mathtt{Finished}\) od serveru.

## Poznámka Anki 1698674918222

Karty Anki: 1698674918223
GUID: Q#n>#E>nr(; štítky: bi-asb::p05 bi-ib::12.

### Otázka (Front)

Popište cipher suite (šifrovací sadu) v protokolu Transport Layer Security (TLS).

### Odpověď (Back)

Cipher suite (šifrovací sada) v protokolu Transport Layer Security (TLS) je sada algoritmů, které se využívají pro zabezpečení síťového spojení. Skládá se ze čtyř složek:

1. algoritmus výměny klíče,

2. autentizační algoritmus, 

3. algoritmus hromadného šifrování,

4. algoritmus pro message authentication code nebo hashování.

Tedy například:

\[\mathtt{TLS} \mathtt{\_}
\underbrace{\mathtt{ECDHE}}_\text{(1)} \mathtt{\_}
\underbrace{\mathtt{RSA}}_\text{(2)} \mathtt{\_ WITH \_}
\underbrace{\mathtt{AES \_ 128 \_ GCM}}_\text{(3)} \mathtt{\_}
\underbrace{\mathtt{SHA256}}_\text{(4)}.\]

## Poznámka Anki 1698675712407

Karty Anki: 1698675712407
GUID: p}ThH,Ft?N; štítky: bi-asb::p05 bi-ib::12.

### Otázka (Front)

Jakým způsobem se z pre-master secret generuje master secret a key block v Transport Layer Security (TLS)?

### Odpověď (Back)

Pro vygenerování master secret a key blocku z pre-master secret se v TLS použije pseudo-random function (PRF) s rozhraním
\[\operatorname{PRF}(\text{secret}, \text{label}, \text{seed}),\]která interně používá hash-based message authentication code (HMAC). Master secret a key block získáme z pre-master secret, náhodných dat klienta \(N_\text C\) a náhodných dat serveru \(N_\text S\) jako:
\[\begin{matrix}
\mathtt{master \ secret} = \operatorname{PRF}(\mathtt{pre\text-master \ secret}, \text{"master secret"}, N_\text C \| N_\text S) \\
\mathtt{key \ block} = \operatorname{PRF}(\mathtt{master \ secret}, \text{"key expansion"}, N_\text S \| N_\text C).
\end{matrix}\]Z key blocku potom získáváme MAC klíč serveru a klienta, šifrovací klíč serveru a klienta a případné inicializační vektory.

## Poznámka Anki 1698676270074

Karty Anki: 1698676270074
GUID: A[RSlA{w4k; štítky: bi-asb::p05 bi-ib::12 bi-ib::13 bi-spol::09.

Metadata původního zdroje pro kartu 1698676270074: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište static a ephemeral Diffie-Hellmanův algoritmus.

### Odpověď (Back)

Diffie-Hellmanův algoritmus můžeme provést následujícími způsoby:

- **static-static** - obě strany mají neměnné veřejné i soukromé klíče podepsané certifikační autoritou,

- **static-ephemeral** - jedna strana používá certifikovaný klíč a druhá strana náhodně generovaný privátní klíč,

- **ephemeral-ephemeral** - obě strany používají náhodně generovaný privátní klíč.

## Poznámka Anki 1698676430346

Karty Anki: 1698676430346
GUID: pY,vYS[gV?; štítky: bi-asb::p05 bi-ib::12 bi-ib::13.

Metadata původního zdroje pro kartu 1698676430346: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište perfect forward secrecy (PFS). Jak je jí dosaženo v Transport Layer Security (TLS) protokolu?

### Odpověď (Back)

Perfect forward secrecy (PFS) je vlasnost algoritmů výměny klíče, která zajišťuje, že při kompromitaci používaných klíčů nedojde k ohrožení důvěrnosti již proběhlých přenosů, které algoritmus výměny klíče používaly. V TLS protokolu ji zajišťuje pouze ephemeral Diffie-Hellmanův algoritmus.

## Poznámka Anki 1698677152097

Karty Anki: 1698677152097
GUID: FYAPordZ/|; štítky: bi-asb::p05 bi-ib::12.

### Otázka (Front)

Popište rozdíly mezi Transport Layer Security (TLS) verzí 1.2 a 1.3.

### Odpověď (Back)

Mezi zásadní rozdíly mezi TLS 1.2 a 1.3 patří:

- povinnost perfect forward secrecy (tedy ephemeral Diffie-Hellmanova algoritmu);
- povinnost implementovat určité šifrovací sady;
- one-round-trip-time navazování relací a zero-round-trip-time navazování relací při pokračování z předešlé relace;

- přidání podpory authenticated encryption with associated data (AEAD) šifer, ChaCha20 a Poly1305 MAC;
- odstranění slabých a nepoužívaných šifer, hashovacích funkcí a eliptických křivek (RC4, DES, MD5 a další);
- odstranění nepoužívaných funkcí jako např. komprese.

