# BI-ADU – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-adu/BI-ADU.apkg; APKG SHA-256 82e24d30673cd0e7a3a5aa4e190d583b7bbdacb9961363822343a47e911816b0. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e4dcf13ba19280a57f78abe30db474a9b8da6ee148ccef4aa2c510acfc892435.
Původní balíčky: BI-ADU
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678264429905

Karty Anki: 1678264429905
GUID: jjhcsM^4YN; štítky: bi-adu::p03 bi-ib::01.

Metadata původního zdroje pro kartu 1678264429905: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak se testuje autorizace na tradičním Unixovém systému a systému podporujícím privilegia?

### Odpověď (Back)

**Tradiční Unixový systém **testuje, jestli \(\mathtt{UID} = 0\). U **systému podporujícího privilegia** si každý proces je spjatý s množinou svých privilegií, která je pak při autorizaci testována.

## Poznámka Anki 1678264968969

Karty Anki: 1678264968969
GUID: DG(9mR;}uH; štítky: bi-adu::p03 bi-ib::01.

Metadata původního zdroje pro kartu 1678264968969: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou množiny privilegií? Jak probíhá jejich dědění?

### Odpověď (Back)

Z pohledu implementace se privilegia dělí do čtyř kategorií:

- **inheritable**,
- **permitted**,
- **effective **- testovaná kernelem při autorizaci,
- **limit**.

Dědění probíhá podle následujícího schématu:

 [Obrázek: paste-f3f9c0d48948dbf4aa44bee906716acbb1046da1.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1678265317458

Karty Anki: 1678265317458
GUID: l6wPcl}fP<; štítky: bi-adu::p03.

Metadata původního zdroje pro kartu 1678265317458: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakým příkazem se spravují privilegia? Jaký používají konfigurační soubor?

### Odpověď (Back)

Ke správě privilegií se používá příkaz \(\mathtt{ppriv}\) a jejich konfiguraci lze provádět v souboru\(\mathtt{/etc/security/policy\text.conf}\).

## Poznámka Anki 1678265651905

Karty Anki: 1678265651905
GUID: Nqjj5s#qFb; štítky: bi-adu::p03 bi-ib::01.

Metadata původního zdroje pro kartu 1678265651905: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to role-based access control (RBAC)? K čemu slouží?

### Odpověď (Back)

Role-based access control slouží k rozdělení kompetencí do **rolí**, kterým lze přiřazovat **autorizace **a **profily**. **Profily** jsou tvořeny **příkazy**, které lze spouštět s danými **identitami** a **privilegii**.

## Poznámka Anki 1678266378326

Karty Anki: 1678266378326
GUID: P//(0nv`DG; štítky: bi-adu::p03 bi-ib::01.

Metadata původního zdroje pro kartu 1678266378326: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to role v rámci role-based access control? Jaký používají konfigurační soubor?

### Odpověď (Back)

Role vykazuje stejné vlastnosti jako běžný uživatel, ale nelze se jejím jménem přihlásit (namísto toho se použije \(\mathtt{su}\)). Rolím se přiřazuje množina **profilů**. To, jaké role uživatel má, lze konfigurovat v souboru \(\mathtt{/etc/user\_attr}\).

## Poznámka Anki 1678266460735

Karty Anki: 1678266460735
GUID: HTnZAb>hw;; štítky: bi-adu::p03.

Metadata původního zdroje pro kartu 1678266460735: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak se provede příkaz pod role-based access control profilem?

### Odpověď (Back)

Příkaz musí být volán v profilovém shellu (\(\mathtt{pfbash}\), \(\mathtt{pfksh}\)).

## Poznámka Anki 1678266604074

Karty Anki: 1678266604074
GUID: zuTXhx37?`; štítky: bi-adu::p03 bi-ib::01.

Metadata původního zdroje pro kartu 1678266604074: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to profil v rámci role-based access control? Jaké používají konfigurační soubory?

### Odpověď (Back)

Profil představuje množinu příkazů nebo skriptů, které jsou spouštěny se speciálními atributy (jiné \(\mathtt{UID}\) nebo \(\mathtt{GID}\), speciální privilegia). Definovány jsou v souboru \(\mathtt{/etc/security/prof\_attr}\) a v souboru \(\mathtt{/etc/security/exec\_attr}\) jim lze přiřadit příkazy a skripty.

## Poznámka Anki 1678267415335

Karty Anki: 1678267415335
GUID: blu?fp=?-{; štítky: bi-adu::p03.

Metadata původního zdroje pro kartu 1678267415335: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to autorizace v rámci role-based access control? Jaký používají konfigurační soubor?

### Odpověď (Back)

Autorizace se přiděluje rolím a aplikace podporující role-based access control ji potom mohou kontrolovat. Konfigurovat je lze v souboru \(\mathtt{/etc/security/auth\_attr}\).

## Poznámka Anki 1678267957254

Karty Anki: 1678267957254
GUID: rpu%)j+68J; štítky: bi-adu::p03 bi-ib::01 bi-ib::25.

Metadata původního zdroje pro kartu 1678267957254: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Pluggable Authentication Modules (PAM)? Kde se konfigurují?

### Odpověď (Back)

Pluggable authentication modules (PAM) poskytují framework pro autentizaci uživatelů napříč operačním systémem. Programy pak mohou za běhu komunikovat s PAM moduly, což umožňuje vývoj aplikací nezávisle na autentizačních schématech. Konfigurace PAM probíhá v \(\texttt{/etc/pam.d}\).

## Poznámka Anki 1678268208898

Karty Anki: 1678268208898
GUID: jhS+^[+NQh; štítky: bi-adu::p03 bi-ib::01 bi-ib::25.

Metadata původního zdroje pro kartu 1678268208898: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké existují typy pluggable authentication modules modulů?

### Odpověď (Back)

Existují čtyři následující typy PAM modulů:

- **authentication** - autentizace;
- **account** - autorizace, kontrola expirace hesla, omezení přístupu na základě času;
- **password** - změna hesla;
- **session** - moduly spouštěné na začátku a konci uživatelské relace.

