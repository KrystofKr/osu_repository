# BI-SAP – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-sap/BI-SAP.apkg; APKG SHA-256 1f67b9282d55c6e8fb096f86041a008a959b3ade7ab78b051bce1ceb2cf0a3bd. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 624f9e0b4061e0e62a0e80089c16bfc9c700ec35ffa2dae8f3cc15f23be9a383.
Původní balíčky: BI-SAP
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1647987164543

Karty Anki: 1647987164543
GUID: k@F*K~-HSM; štítky: bi-sap::otazky04 bi-sap::p05 bi-spol::30.

### Otázka (Front)

Popište řádovou mřížku a její vlastnosti.

### Odpověď (Back)

Řádová mřížka určuje formát čísel zobrazitelných na počítači. Definuje:

- nejvyšší řád (\(n\)),
- nejnižší řád (\(-m\)),

např. pro řádovou mřížku

 [Obrázek: paste-d61f8055e83ed209e87ebcbb254686267a5e1be0.jpg; soubor je v media/ v doprovodném ZIP] 

máme

\[\begin{matrix}
n = 1\\
-m = -3
\end{matrix}\]

Základními vlastnostmi řádové mřížky jsou:

- **délka **(\(l\)) - počet řádů řádové mřížky;
- **jednotka **(\(\varepsilon\)) - nejmenší nezáporné zobrazitelné číslo;
- **modul **(\(M\)) - nejmenší kladné číslo, které už zobrazitelné není.

## Poznámka Anki 1648936273444

Karty Anki: 1648936273444
GUID: LSn*g6`ID3; štítky: bi-sap::otazky05 bi-sap::p05.

Metadata původního zdroje pro kartu 1648936273444: v původním balíčku pozastavená karta.

### Otázka (Front)

Zapište výraz pro detekci overflow při sčítání v doplňkovém kódu.

### Odpověď (Back)

\(C_{\text {in} } \oplus C_{\text {out} }\) vzhledem k poslednímu bloku sčítačky.

## Poznámka Anki 1648989119187

Karty Anki: 1648989119187
GUID: cOdLu+^/r^; štítky: bi-sap::otazky05 bi-sap::p05.

Metadata původního zdroje pro kartu 1648989119187: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolik cifer může mít výsledek součtu dvou \(n\) ciferných čísel?

### Odpověď (Back)

\(n+1\)

## Poznámka Anki 1648989147344

Karty Anki: 1648989147344
GUID: j3q*y5Pgw$; štítky: bi-sap::otazky05 bi-sap::p05.

Metadata původního zdroje pro kartu 1648989147344: v původním balíčku pozastavená karta.

### Otázka (Front)

Kolik cifer může mít výsledek součinu dvou \(n\) ciferných čísel?

### Odpověď (Back)

\(2n\)

## Poznámka Anki 1648989275232

Karty Anki: 1648989275232
GUID: d-Qf}p~5E^; štítky: bi-sap::otazky05 bi-sap::p05 bi-spol::30.

Metadata původního zdroje pro kartu 1648989275232: v původním balíčku pozastavená karta.

### Otázka (Front)

Vysvětlete jaký je rozdíl mezi přenosem (carry) a přeplněním (overflow).

### Odpověď (Back)

**Carry** se objevuje u přímého kódu a naznačuje, že se výsledek aritmetické operace nachází mimo meze čísel vyjádřitelných v akutální řádové mřížce. **Overflow** se objevuje u doplňkového kódu a naznačuje, že výsledek aritmetické operace by buď moc vysoký nebo moc nízký, a proto došlo k přetečení nebo podtečení do čísel s opačným znaménkem.

## Poznámka Anki 1717180625000

Karty Anki: 1717180625000
GUID: g6gCL8sY(3; štítky: bi-sap::p05 bi-spol::29.

### Otázka (Front)

Vyjmenujte nejčastěji používané kódy pro zobrazení čísel se znaménkem.

### Odpověď (Back)

Pro zobrazení čísel se znaménkem se nejčastěji používají:

- přímý kód (sign-magnitude),
- aditivní kód (offset binary),
- doplňkový kód pro dvojkovou soustavu (two's complement).

## Poznámka Anki 1717181041732

Karty Anki: 1717181041732
GUID: zXp*L2hI=p; štítky: bi-sap::p05 bi-spol::29.

### Otázka (Front)

Popište doplňkový kód (two's complement).

### Odpověď (Back)

Doplňkový kód (two's complement) je kód pro zobrazení čísel se znaménkem. Nejvyšší bit čísla určuje znaménko reprezentovaného čísla (\(\mathtt 0\) pro kladná \(\mathtt 1\) pro záporná), ale zároveň je organickou součástí reprezentovaného čísla. Platí:
\[\mathcal D(x) = \begin{cases}
x && x \in \langle 0, \frac M 2),\\
x + M && x \in \langle - \frac M 2, 0).
\end{cases}\]

 [Obrázek: paste-c8c9368daa7b6a9ddc82ef53f1f5fdd2b02ce66c.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1717241078660

Karty Anki: 1717241078660
GUID: eL&>[{WgRL; štítky: bi-sap::p05 bi-spol::30.

Metadata původního zdroje pro kartu 1717241078660: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus pro získání obrazu záporného čísla v doplňkovém kódu.

### Odpověď (Back)

Pro získání obrazu záporného čísla v doplňkovém kódu postupujeme následovně:

- zapíšeme binární absolutní hodnotu daného čísla do řádové mřížky,
- invertujeme všechny bity,
- přičteme jedničku.

### Doplňující pole (Extra)

Prakticky lze tento algoritmus provést následovně:

- zapíšeme binární absolutní hodnotu daného čísla do řádové mřížky,
- všechny bity zprava až po první jedničku včetně necháme v původní podobě,
- zbytek bitů invertujeme.

## Poznámka Anki 1717243573608

Karty Anki: 1717243573609
GUID: QY/^y7u!Ds; štítky: bi-sap::p05 bi-spol::30.

### Otázka (Front)

Popište přímý kód (sign-magnitude).

### Odpověď (Back)

Přímý kód (sign-magnitude) je kód pro zobrazení čísel se znaménkem. Nejvyšší bit určuje znaménko (sign) reprezentovaného čísla ( \(\texttt 0\) pro kladná  \(\texttt 1\) pro záporná) a zbytek bitů obsahuje absolutní hodnotu čísla (magnitude). Bit, který určuje znaménko, však není součástí reprezentace samotného čísla a s oběma částmi se pracuje separátně. Pro přímý kód je typické, že obsahuje jak kladnou, tak zápornou reprezentaci nuly. Platí:
\[\mathcal P(x) = \begin{cases}
x && x \in \langle 0, \frac M 2),\\
x + \frac M 2 && x \in ( - \frac M 2, 0 \rangle
\end{cases}\]

 [Obrázek: Screenshot 2024-06-01 135134.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1717243925044

Karty Anki: 1717243925044
GUID: w6HEEV.:>n; štítky: bi-sap::p05 bi-spol::30.

### Otázka (Front)

Popište aditivní kód (offset binary).

### Odpověď (Back)

Aditivní kód (offset binary) je kód pro zobrazení čísel se znaménkem. Funguje tak, že nula je „posunuta“ o konstantu \(K\), přičemž nejčastěji \(K = \frac M 2\). Platí:
\[\mathcal A(x) = x + K \quad x \in \langle-K, M-K).\]

 [Obrázek: paste-650bc586ecada67b93bb36fb64ab95dace6b8d68.jpg; soubor je v media/ v doprovodném ZIP]

