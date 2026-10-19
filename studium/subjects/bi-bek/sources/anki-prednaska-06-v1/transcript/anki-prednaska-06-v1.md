# BI-BEK – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1680704532961

Karty Anki: 1680704532962
GUID: wp9,ob{0qw; štítky: bi-bek::p06 bi-ib::09 bi-ib::25.

### Otázka (Front)

Popište Windows trustee a security identifier (SID).

### Odpověď (Back)

**Trustee** je uživatelský účet, skupina nebo logon session, na které se vztahují záznamy v access control listech (ACL). **Security identifier **(SID) je identifikátor variabilní délky, který je unikátní pro každého trustee.

## Poznámka Anki 1680704676303

Karty Anki: 1680704676303
GUID: t;PcU`*+vX; štítky: bi-bek::p06 bi-ib::09 bi-ib::25.

### Otázka (Front)

Co je to Access Control Entry (ACE) a Acces Control List (ACL) ve Windows ACL?

### Odpověď (Back)

**Access Control Entry **(ACE) povoluje, odepírá, nebo audituje přístupová práva pro nějakého trustee. **Access Control List **(ACL) je potom seznam ACEs.

## Poznámka Anki 1680704892663

Karty Anki: 1680704892663
GUID: t^_8VW]R2Z; štítky: bi-bek::p06 bi-ib::09 bi-ib::25.

### Otázka (Front)

Popište Windows securable object a security descriptor.

### Odpověď (Back)

**Securable object** je objekt, kterému může být přiřazen security descriptor. **Security descriptor** obsahuje informace o securable objectu, konkrétně:

- security identifier (SID) vlastníka a primární skupiny,

- discretionary access control list (DACL),

- system access control list (SACL),

- příznaky (control bits).

## Poznámka Anki 1680705111882

Karty Anki: 1680705111882
GUID: M?*+;1UvKi; štítky: bi-bek::p06 bi-ib::01 bi-ib::09 bi-ib::25.

### Otázka (Front)

Popište Windows discretionary access control list (DACL).

### Odpověď (Back)

Windows discretionary access control list (DACL) je seznam access control entries (ACE), které identifikují trustees a buď jim povolují nebo zakazují přístup k securable objectu.

## Poznámka Anki 1680705202575

Karty Anki: 1680705202575
GUID: L>ANyeig+5; štítky: bi-bek::p06 bi-ib::01 bi-ib::09 bi-ib::25.

### Otázka (Front)

Popište Windows system access control list (SACL).

### Odpověď (Back)

Windows system access control list (SACL) je seznam access control entries (ACE), které specifikují trustees a typy jejich přístupů k securable objectu, které budou zapsány do bezpečnostního logu.

## Poznámka Anki 1680708889387

Karty Anki: 1680708889388
GUID: eF^?A,/I#{; štítky: bi-bek::p06 bi-ib::09 bi-ib::25.

### Otázka (Front)

Popište Windows access token a security context.

### Odpověď (Back)

**Access token **je objekt, který popisuje security context procesu nebo vlákna. **Security context** je sada bezpečnostních atributů a pravidel, která jsou právě v platnosti. Mezi položky access tokenu patří:

- security identifier (SID) uživatelského účtu,
- security identifier (SID) skupin uživatele,
- výchozí discretionary access control list (DACL) pro vytváření securable objectů

a další.

## Poznámka Anki 1681311787551

Karty Anki: 1681311787551
GUID: G63__~:pO; štítky: bi-bek::p06 bi-ib::09.

### Otázka (Front)

Popište postup určení minimálních ACL.

### Odpověď (Back)

Postup je následující:

- Zjištění všech securable objectů (SO), které aplikace používá.
- Zjištení požadavků securable objectů na zabezpečení.
- Určení vhodné ACL technologie.
- Převod požadavků na technologii ACL.

## Poznámka Anki 1684012115546

Karty Anki: 1684012115546
GUID: uRVWX3fg!; štítky: bi-bek::p06 bi-ib::09.

### Otázka (Front)

Jaký je rozdíl mezi odebráním (remove) a zákázáním (disable) oprávnění v access tokenu ve Windows ACL?

### Odpověď (Back)

V případě odebrání (remove) je aplikace oprávnění nejen zbavena, ale už jej znovu nemůže získat. Zakázání (disable) jej aplikaci pouze vypne, ale lze jej opět nastavit.

