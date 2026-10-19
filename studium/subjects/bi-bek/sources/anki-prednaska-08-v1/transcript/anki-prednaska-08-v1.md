# BI-BEK – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1681915401570

Karty Anki: 1681915401570
GUID: G,[2bTT_pB; štítky: bi-bek::p08 bi-ib::19.

### Otázka (Front)

Popište vlastnosti kvalitních kryptograficky bezpečných generátorů náhodných a pseudonáhodných čísel.

### Odpověď (Back)

Na kvalitní kryptograficky bepzečné generátory náhodných a pseudonáhodných čísel klademe následující požadavky:

- generovaná čísla musí být nepředvídatelná (odolnost proti next-bit test a state compromise),
- generovaná čísla musí mít rovnoměrné rozdělení,
- generátor musí mít dostatečně dlouhou periodu,
- generátor musí projít statistickými testy.

## Poznámka Anki 1681915631554

Karty Anki: 1681915631554
GUID: BgyC4~0&wu; štítky: bi-bek::p08.

Metadata původního zdroje pro kartu 1681915631554: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to next-bit test pseudonáhodného generátoru?

### Odpověď (Back)

Řekneme, že PRNG je odolný proti next-bit test v případě, že i přestože je známo prvních \(k\) bitů náhodné posloupnosti, neexistuje algoritmus s polynomiální složitostí, který by dokázal předpovědět \(k + 1\) bit s pravděpodobností úspěchu vyšší než \(\frac 1 2\).

## Poznámka Anki 1681915669990

Karty Anki: 1681915669990
GUID: cmh6CnXK&5; štítky: bi-bek::p08.

Metadata původního zdroje pro kartu 1681915669990: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to state compromise pseudonáhodného generátoru?

### Odpověď (Back)

Řekneme, že PRNG je odolný proti state compromise v případě, že i přestože je zjištěn vnitřní stav generátoru, nelze zpětně zrekonstruovat dosavadní vygenerovanou náhodnou posloupnost. Navíc pokud do generátoru vstupuje další entropie, nemělo by být možné předpovědět ani jeho stav v další iteraci.

## Poznámka Anki 1681918120299

Karty Anki: 1681918120299
GUID: fGTbgjC#lG; štítky: bi-bek::p08.

### Otázka (Front)

Definujte kryptografický klíč.

### Odpověď (Back)

Kryptografický klíč je parametr kryptografického algoritmu, který určuje jeho chod tak, že entita se znalostí klíče je schopna reprodukovat nebo zvrátit chod algoritmu, zatímco entita bez znalosti klíče ne.

## Poznámka Anki 1681918147313

Karty Anki: 1681918147313
GUID: oB|n[l|DOI; štítky: bi-bek::p08.

### Otázka (Front)

Definujte správu klíčů.

### Odpověď (Back)

Správou klíčů rozumíme nakládání s kryptografickými klíči a souvisejícími parametry (inicializační vektory, hesla) během celého životního cyklu klíčů včetně jejich tvorby, skladování, výměny, vstupu, výstupu a likvidace.

## Poznámka Anki 1681918230723

Karty Anki: 1681918230723
GUID: KhyR3uAKsR; štítky: bi-bek::p08.

### Otázka (Front)

Jak dělíme kryptografické klíče?

### Odpověď (Back)

Klíče dělíme na

- **asymetrické **(veřejné, soukromé),
- **symetrické**.

Z hlediska předpokládané doby života ještě rozeznáváme klíče

- **trvalé **(static),

- **dočasné** (ephemeral).

## Poznámka Anki 1681918550785

Karty Anki: 1681918550785
GUID: D.SRxb-S9}; štítky: bi-bek::p08.

### Otázka (Front)

Definujte zřízení klíče.

### Odpověď (Back)

Výměna klíče je proces, během kterého se bezpečně zřídí klíč mezi kryptografickými moduly za použití manuálního přenosu, automatických metod, nebo jejich kombinace.

## Poznámka Anki 1681918838110

Karty Anki: 1681918838110
GUID: iLwT-XIPU$; štítky: bi-bek::p08 ni-pb::21.

### Otázka (Front)

Definujte kryptografickou sůl.

### Odpověď (Back)

Kryptografická sůl je parametr, který vstupuje do kryptografického algoritmu a ovlivňuje jej tak, aby výsledek tohoto algoritmu byl různý i přesto, že vstup je stejný. Tím zvyšuje náročnost útoků, protože útočník nemůže tento výsledek použít znovu pro stejný vstup.

## Poznámka Anki 1683818629789

Karty Anki: 1683818629789
GUID: JW{bveMO|g; štítky: bi-bek::p08 bi-ib::07.

### Otázka (Front)

Porovnejte MAC či HMAC a digitální podpis pro potřeby zajištění integrity dat.

### Odpověď (Back)

| 
      **MAC či HMAC** | 
      **digitální podpis** | 

| 
      velmi rychlý výpočet | 
      pomalý výpočet | 

| 
      pro HMAC je nutný symetrický klíč, který je potřeba sdílet | problém distribuce veřejného klíče | 

| 
      
 | 
      lze použít pro nepopiratelnost (podpis může vygenerovat pouze vlasntík soukromého klíče) |

## Poznámka Anki 1684165047870

Karty Anki: 1684165047882
GUID: A!Fre6Fyv^; štítky: bi-bek::p08.

### Otázka (Front)

Proč není vhodné použít CRC nebo hash jako jedinou techniku ověření integrity? Jaké jiné techniky můžeme použít?

### Odpověď (Back)

CRC a hash jsou sice schopné zajistit, že nedošlo k modifikaci dat, ale neposkytují jistotu, že je nikdo nepřepočítal. Namísto nich se doporučuje použít klíčovaný hash (HMAC) nebo digitální podpis.

## Poznámka Anki 1684504702289

Karty Anki: 1684504702326
GUID: H#`go!ic1~; štítky: bi-bek::p08.

### Otázka (Front)

Jaké jsou požadavky na key-derivation function?

### Odpověď (Back)

Po key-derivation function požadujeme následující vlastnosti:

- pro libovolně dlouhý vstup vygeneruje výstup o dané délce,
- do výstupu jsou zahrnuty všechny bity hesla,
- musí zahrnovat kryptografickou sůl,
- musí být pomalá (jako obrana proti brute-force útokům),
- musí být náročná na paměť (jako obrana proti specializovanému hardware),
- nemusí být nutně bezkolizní.

## Poznámka Anki 1687441869139

Karty Anki: 1687441869139
GUID: z>yc$3f.K>; štítky: bi-bek::p08.

### Otázka (Front)

Porovnejte trvalý klíč (static key) a dočasný klíč (ephemeral key).

### Odpověď (Back)

**Trvalý klíč** je kryptografický klíč, který je určen k použití po delší časový interval, typicky v mnoho instancích schématu zřízení kryptografického klíče. **Dočasný klíč** je naproti tomu takový kryptografický klíč, který je pro každou instanci schématu zřízení kryptografického klíče generován znovu.

