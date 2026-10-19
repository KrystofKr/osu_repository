# BI-PSI – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 21 poznámek, 21 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1650878890873

Karty Anki: 1650878890874
GUID: NLFf~X@g%t; štítky: bi-ib::12 bi-ib::21 bi-psi::p10.

### Otázka (Front)

Popište a porovnejte protokoly Secure Shell Protocol (SSH) a Telnet.

### Odpověď (Back)

Protokoly Secure Shell Protocol (SSH) a Telnet (teletype network) jsou protokoly aplikační vrstvy, které se používají pro vzdálený přístup. Postaveny jsou na architektuře klient/server a pro přenos dat používají protokol TCP. Odlišují je následující rozdíly:

| 
      **Secure Shell Protocol (SSH)** | **Telnet** | 

| 
      používá port 22 | 
      používá port 23 | 

| 
      šifruje přenášená data
 | 
      nešifruje přenášená data |

## Poznámka Anki 1650878977200

Karty Anki: 1650878977200
GUID: AlhdCb~Tm#; štítky: bi-psi::p10.

### Otázka (Front)

Popište RDP.

### Odpověď (Back)

Remote Desktop Protocol emuluje přístup ke grafickému rozhraní počítače. Je přenášen v položce data protokolu TCP a funguje na portu 3389.

## Poznámka Anki 1650879110878

Karty Anki: 1650879110878
GUID: J6C!B=fFL-; štítky: bi-psi::p10.

### Otázka (Front)

Popište FTP.

### Odpověď (Back)

File Transfer Protocol přenáší data v paketu protokolu TCP. Vytváří dvě různá spojení, pro příkazy a pro data, která se liší cílovými porty. Má šifrovanou varitantu SFTP. Pracuje buď v aktivním nebo pasivním módu.

## Poznámka Anki 1650879759449

Karty Anki: 1650879759450
GUID: O0BV$Vb.*0; štítky: bi-psi::p10.

### Otázka (Front)

Popište průběh komunikace přes FTP v různých módech.

### Odpověď (Back)

1. klient zahájí autentizaci na portu 21 (příkaz AUTH)
2. klient pošle jméno a heslo (příkazy USER a PASS)
3. server ověří údaje klienta
4a. (**aktivní mód**) klient navrhne serveru datový port (příkaz PORT), server otevře spojení na navržený port
4b. (**pasivní mód**) klient požádá o pasivní mód (příkaz PASV), server navrhne datový port, klient si zvolí svůj port a otevře spojení
5. dojde k přenosu dat
6. klient ukončí spojení se serverem (příkaz QUIT)

## Poznámka Anki 1650885131338

Karty Anki: 1650885131349
GUID: B<avyLGN,j; štítky: bi-psi::p10.

### Otázka (Front)

Co je to Mail Transfer Agent (MTA)?

### Odpověď (Back)

Je to program běžící na poštovním serveru, který odesílá či přijímá elektronickou poštu.

## Poznámka Anki 1650885174325

Karty Anki: 1650885174325
GUID: bgi0{8k)5[; štítky: bi-psi::p10.

### Otázka (Front)

Co je to MTA Relay?

### Odpověď (Back)

Je to server přístupný z internetu (umisťuje se to DMZ), který přeposílá požadavky na MTA. Funguje jako ochrana před útočníky.

## Poznámka Anki 1650885215957

Karty Anki: 1650885215957
GUID: K$x5/zz)2h; štítky: bi-psi::p10.

### Otázka (Front)

Co je to User Agent (UA) v rámci elektronické pošty?

### Odpověď (Back)

Je to program běžící v zařízení uživatele, který načítá poštu z mailboxu na poštovním serveru.

## Poznámka Anki 1650885512708

Karty Anki: 1650885512708
GUID: xa-p*oBq~j; štítky: bi-psi::p10.

### Otázka (Front)

Jak probíhá doručování emailů?

### Odpověď (Back)

1. odesílatel napíše email a pomocí svého UA jej doručí na MTA protokolem SMTP
2. z doménového jména v emailové adrese se pomocí DNS protokolu zjistí IP adresa cílového poštovního serveru (MX záznam)
3. MTA prostřednictvím MTA Relaye pošle email přijemci
4. MTA Relay přijemce předá email MTA, který uchovává emaily příjemce a uloží email do mailboxu
5. UA přijemce kontaktuje MTA a načte obsah mailboxu

## Poznámka Anki 1650885758111

Karty Anki: 1650885758112
GUID: usBb72:7z); štítky: bi-psi::p10.

### Otázka (Front)

Co je to SMTP? Jaký používá port?

### Odpověď (Back)

Simple Mail Transfer Protocol je protokol určený pro přeposílání emailů mezi poštovními servery, popř. mezi UA a MTA. Používá port 25.

## Poznámka Anki 1650885995125

Karty Anki: 1650885995125
GUID: bQxI0=,1`7; štítky: bi-psi::p10.

### Otázka (Front)

Co jsou to protokoly POP3 (POP3s) a IMAP (IMAPs) a jak se liší?

### Odpověď (Back)

Jsou to protokoly určené pro čtení pošty prostřednictvím UA a MTA.
UA používající **POP3** kopírují na klientských stanicích obsah mailboxu.
**IMAP** funguje jako projekce mailboxu. UA pracuje se schránkou živě.

## Poznámka Anki 1650886099277

Karty Anki: 1650886099278
GUID: Iw0Mw^eXjs; štítky: bi-psi::p10.

### Otázka (Front)

Co je to SPAM?

### Odpověď (Back)

Je to elektronická pošta, která je zasílána do mailboxu uživatele bez toho, že by vyjádřil zájem o její odběr. Součástí SPAMu může být malware, typické jsou také útoky na vylákání identity (phishing).

## Poznámka Anki 1650886326217

Karty Anki: 1650886326217
GUID: u.Xhvsnzda; štítky: bi-psi::p10.

### Otázka (Front)

Kde probíhá filtrování SPAMu?

### Odpověď (Back)

- na straně serveru - SPAM detektorem (modul MTA)
- na straně klienta - detektorem v rámci UA

## Poznámka Anki 1650886456411

Karty Anki: 1650886456411
GUID: Jy9g}Hm7LH; štítky: bi-psi::p10.

### Otázka (Front)

Popište Hyper-Text Transfer Protocol (HTTP).

### Odpověď (Back)

- používá se pro přenos obsahu webových stránek
- přenáší se jako data protokolu transportní vrstvy
- používá port 80
- funguje na principu žádost-odpověď
- je bezestavový (každá relace je chápána jako nová), k zapamatování informací používají cookies

## Poznámka Anki 1650886560878

Karty Anki: 1650886560878
GUID: J9%]aSJt$(; štítky: bi-psi::p10.

### Otázka (Front)

Vyjmenujte žádosti a odpovědi v HTTP.

### Odpověď (Back)

**Žádosti**:

- GET - načtení stránky
- HEAD - načtení hlavičky
- POST/PUT - odeslání dat
- DELETE - smazání informací na serveru
**Odpovědi**:

- 200 - OK
- 301 - permanentně přesunuto
- 404 - chyba ve zprávě
- 505 - vnitřní chyba serveru

## Poznámka Anki 1650886629188

Karty Anki: 1650886629188
GUID: c$S}QcaEeS; štítky: bi-psi::p10.

### Otázka (Front)

Popište princip fungování cookies.

### Odpověď (Back)

Při prvním přístupu vygeneruje server pro klienta identifikátor a uloží jej u klienta jako cookie. Při dalších přístupech může server upravovat chování na základě uložených cookies.

## Poznámka Anki 1650887156609

Karty Anki: 1650887156609
GUID: ohLdA^btb7; štítky: bi-ib::12 bi-psi::p10.

### Otázka (Front)

Popište princip protokolu HTTPS.

### Odpověď (Back)

1. klient pošle žádost o načtení stránky
2. server pošle klientovi svůj certifikát
3. klient ověří certifikát, v případě problému vypíše varování
4. klient vygeneruje náhodný šifrovací klíč a odešle jej serveru zašifrovaný pomocí veřejného klíče serveru (z certifikátu)
5. server klíč obdrží a dešifruje
6. server odešle obsah stránky zašifrovaný pomocí klíče
7. klient dešifruje data a získá obsah webové stránky

## Poznámka Anki 1650887271104

Karty Anki: 1650887271104
GUID: pK+LccU),B; štítky: bi-psi::p10.

### Otázka (Front)

Popište Network Time Protocol (NTP).

### Odpověď (Back)

Network Time Protocol (NTP) je protokol aplikační vrstvy používaný pro synchronizaci hodin. Typicky je implementován pomocí protokolu UDP a používá port 123. Servery provozující NTP se nazývají strata a jsou řazeny hierarchicky dle vzálenosti od atomových hodin. Komunikace protokolu NTP vypadá následovně:

- klient odešle žádost na NTP server,
- NTP server přijme klientovu žádost a začne ji zpracovávat,
- NTP server dokončí zpracování žádosti a odešle odpověď,
- klient přijme odpověď NTP serveru.

V každém z těchto kroků jsou vytvořeny timestampy, z nichž klient následně dokáže spočítat správný způsob úpravy svých hodin.

 [Obrázek: paste-ad778c42e383998a38865147bea05789e8a92fd5.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1650887433399

Karty Anki: 1650887433399
GUID: MD}_q7p]Iy; štítky: bi-psi::p10.

### Otázka (Front)

Popište BitTorrent protokol.

### Odpověď (Back)

BitTorrent realizuje sdílení dat mezi uživateli (P2P).
Fungování:

1. uživatel si stáhne .torrent soubor s informacemi o částech stahovaného souboru
2. z trackeru si zjistí, kteří uživatelé dané části mají
3. začne paralelně stahovat dostupné části souboru z různých zdrojů

## Poznámka Anki 1650887755361

Karty Anki: 1650887755361
GUID: Cn(~..8gxh; štítky: bi-psi::p10.

### Otázka (Front)

Za pomocí jakých protokolů funguje VoIP?

### Odpověď (Back)

Prostřednictvím protokolů SIP (Session Initiation Protocol) a RTP (Real Time Protocol), kde SIP má za úkol navázání spojení a RTP realizuje přenos hlasu.

## Poznámka Anki 1652701667235

Karty Anki: 1652701667235
GUID: ri?`9><%hr; štítky: bi-psi bi-psi::p10.

### Otázka (Front)

Co je to HTTPS a jaký port používá?

### Odpověď (Back)

HTTPS je zabezpečená varianta HTTP. Používá port 443.

## Poznámka Anki 1652702222882

Karty Anki: 1652702222882
GUID: ir!O]{RsI@; štítky: bi-psi::p10.

### Otázka (Front)

Popište proces navázání komunikace pomocí SIP. K čemu slouží RTP proxy a kdy je potřeba?

### Odpověď (Back)

1. UA1 chce komunikovat s UA2 pomocí VoIP.

2. UA1 se obrátí na svůj SIP server.

3. SIP server UA1 zjistí od DNS serveru IP adresu SIP serveru zprostředkovávajícího komunikaci s UA2 (SRV záznam na DNS serveru).

4. SIP server UA1 se obrátí s žádostí otevření komunikace na SIP server UA2.

5. SIP server UA2 se obrátí s žádostí otevření komunikace na SIP server UA1.

6. mezi UA1 a UA2 je spuštěn RTP protokol a začne přenos hlasu.

- RTP potřebuje, aby mezi sebou byli UA1 a UA2 dostupní pomocí směrování (bez NATu), pokud nejsou, použije se RTP proxy.

