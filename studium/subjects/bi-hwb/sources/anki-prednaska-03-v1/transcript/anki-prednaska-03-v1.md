# BI-HWB – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-hwb/BI-HWB.apkg; APKG SHA-256 0303626d2408f7eee1801e17ecb475633a60c42f914f37290ffd8c479013ce2b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b861d2e855c5070244800c22d62092a09b22aee0ded024030525b06a7d18285e.
Původní balíčky: BI-HWB
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1696883979070

Karty Anki: 1696883979070
GUID: Hli3|9cm]u; štítky: bi-hwb::p03.

### Otázka (Front)

Jaké jsou požadavky na šifrování disku?

### Odpověď (Back)

Požadavky na šifrování disku jsou následující:

- **důvěrnost dat** - šifrování musí zajistit utajení dat,
- **výkon **- šifrování by nemělo omezit výkonnost disku,
- **nízké nebo žádné dodatečné požadavky na paměť úložiště** - šifrovaná data by neměla zabírat více paměti než nešifrovaná data.

## Poznámka Anki 1696884492098

Karty Anki: 1696884492098
GUID: g/m9B%67AA; štítky: bi-hwb::p03.

### Otázka (Front)

Popište tweakable block cipher.

### Odpověď (Back)

Tweakable block cipher je bloková šifra, která kromě klíče, používá další vstup, který se nazývá tweak. Tento parametr ovlivňuje proces šifrování a dešifrování tak, že pokud zašifrujeme dvakrát stejná data s různým tweakem, bude se výstup těchto procesů lišit. Využívají se zejména při šifrování disků.

## Poznámka Anki 1696885404442

Karty Anki: 1696885404443
GUID: lL8VUcrsz1; štítky: bi-hwb::p03.

### Otázka (Front)

Popište ciphertext stealing (CTS)?

### Odpověď (Back)

Ciphertext stealing je metoda použití operačních módů blokových šifer na otevřené texty, jejichž délka není dělitelná délkou bloku (jsou delší), anižby došlo k nárůstu délky šifrového textu.

## Poznámka Anki 1696885494242

Karty Anki: 1696885494243
GUID: gG=#I/Ltk+; štítky: bi-hwb::p03.

### Otázka (Front)

Ukažte ciphertext stealing (CTS) na operačním módu electionic codebook (ECB).

### Odpověď (Back)

[Obrázek: paste-6638cf36a6005d4b1ab2384ba41543dec27cd0b1.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1696885600513

Karty Anki: 1696885600513
GUID: ok=6460}81; štítky: bi-hwb::p03.

### Otázka (Front)

Ukažte ciphertext stealing (CTS) na operačním módu cipher block chaining (CBC).

### Odpověď (Back)

[Obrázek: paste-17b61ee9f626e8f6e7d87bd81ebaebf7168f4a30.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1696886651661

Karty Anki: 1696886651661
GUID: eK72&-goay; štítky: bi-hwb::p03.

### Otázka (Front)

Popište operační mód blokové šifry xor-encrypt-xor (XEX).

### Odpověď (Back)

Operační mód xor-encrypt-xor funguje tak, že každý blok otevřeného textu je nejprve modifikován pomocí pseudonáhodného bloku generovaného z inicializačního vektoru a až poté se šifruje. Následně je tím stejným blokem ještě jednou modifikován. Tento pseudonáhodný blok je po zašifrování každého bloku otevřeného textu také upraven a to pomocí aritmetiky v \(GF(2^{128})\). XEX je dán vztahy:
\[\begin{matrix}
X_1 = E_k(\text{IV}), \\
X_{i + 1} = X_i \oplus \alpha, \\
c_i = E_k(p_i \oplus X_i) \oplus X_i, \\
p_i = D_k(c_i \oplus X_i) \oplus X_i.
\end{matrix}\]

 [Obrázek: paste-ff3c624dc67752a4bc97e65987549509689200f7.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1696887673770

Karty Anki: 1696887673770
GUID: p`7UGn+%zz; štítky: bi-hwb::p03.

### Otázka (Front)

Ukažte ciphertext stealing (CTS) na operačním módu xor-encrypt-xor (XEX), tedy XEX with ciphertext stealing (XTS).

### Odpověď (Back)

[Obrázek: paste-5f026a11e41217070e455692f71b05753855c953.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1697113633604

Karty Anki: 1697113633604
GUID: w$6{R)?&3`; štítky: bi-hwb::p03.

### Otázka (Front)

Popište encrypted salt-sector initialization vector (ESSIV).

### Odpověď (Back)

Encrypted salt-sector initialization vector (ESSIV) je metoda generování inicializačních vektorů. Používají ji některé operační módy blokových šifer při šifrování disku, protože umožňuje vyhnout se nutnosti inicializační vektor ukládat nebo ho generovat z předvídatelných hodnot. ESSIV generuje IV následujícím způsobem:

- Nejprve pomocí hashovací funkce \(h\) vytvoří hash \(s\) šifrovacího klíče \(k\):

\[s = h(k).\]

- Poté pomocí tohoto hashe zašifruje číslo sektoru \(n\) a vzniká inicializační vektor IV:

\[\text{IV} = E_s(n).\]

## Poznámka Anki 1697113998168

Karty Anki: 1697113998168
GUID: q7J[!Jv5pD; štítky: bi-hwb::p03.

### Otázka (Front)

Popište úrovně šifrování úložišť. Jakými způsoby se realizují?

### Odpověď (Back)

Existují následující úrovně, na kterých lze nasadit šifrování disku:

- **soubory** - obvykle realizováno softwarově na úrovni souborového systému;
- **oddíly** - obvykle realizováno softwarově, občas hardwarově;

- **disky **(full disk encryption) - často realizováno hardwarově.

## Poznámka Anki 1697114602048

Karty Anki: 1697114602048
GUID: oH6=qx,$*-; štítky: bi-hwb::p03.

### Otázka (Front)

Popište samošifrovací disk (SED)? Jaké jsou jeho výhody a nevýhody?

### Odpověď (Back)

Samošifrovací disk nebo také self-encrypting drive (SED) je typ disku, který automaticky šifruje data zapisovaná data a dešifruje data čtená. Mezi jeho výhody patří transparentnost, rychlost a standardizace. Naopak nevýhodami jsou zejména chybějící dokumentace, nemožnost auditu nebo chybné implementace.

## Poznámka Anki 1702815510994

Karty Anki: 1702815510994
GUID: B`3}7F@+HO; štítky: bi-hwb::p03.

### Otázka (Front)

Popište model útoku na šifrované disky.

### Odpověď (Back)

Útočník, který cílí na šifrovaný disk, má následující možnosti:

- může kdykoliv číst obsah disku, proto je potřeba zajistit důvěrnost dat;
- může požadovat zašifrování a uložení libovolných souborů, proto je potřeba používat tweakable šifry;
- může modifikovat nepoužité sektory na disku a požadovat jejich dešifrování, proto není možné používat ECB a proudové šifry.

