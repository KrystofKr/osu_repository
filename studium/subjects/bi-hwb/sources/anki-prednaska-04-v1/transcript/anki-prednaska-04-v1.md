# BI-HWB – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-hwb/BI-HWB.apkg; APKG SHA-256 0303626d2408f7eee1801e17ecb475633a60c42f914f37290ffd8c479013ce2b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b861d2e855c5070244800c22d62092a09b22aee0ded024030525b06a7d18285e.
Původní balíčky: BI-HWB
Rozsah: 3 poznámek, 3 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1697479811577

Karty Anki: 1697479811577
GUID: iAE+s/M40{; štítky: bi-hwb::p04.

Metadata původního zdroje pro kartu 1697479811577: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište šifru Advanced Encryption Standard (AES).

### Odpověď (Back)

Advanced Encryption Standard (AES) je bloková šifra, která je nástupcem šifry DES. AES není feistelovského typu a používá 128b bloky. Podporuje tři různé délky klíče, od kterých se odvíjí počet rund.

| 
      **déka klíče** | 
      **počet rund **(\(N_r\)) | 

| 
      256 bitů | 
      14 | 

| 
      192 bitů | 
      12 | 

| 
      128 bitů | 
      10 | 

Klíč je buď na začátku nebo za chodu algoritmu expandován na \(1 + N_r\) 128b rundovních klíčů. Blok OT se následně vloží do matice \(4 \times 4\) a jedenkrát se aplikuje operace \(\mathtt{AddRoundKey}\). Zbytek šifrování probíhá následovně:

- \(\mathtt{SubBytes}\) - Na každý byte matice zvlášť je aplikována substituce daná pevnou substituční tabulkou (**nelineární **prvek šifry).

- \(\mathtt{ShiftRows}\) - První řádek se cyklicky posune o nula pozic doprava, druhý o jednu, třetí o dvě a čtvrtý o tři.

- \(\mathtt{MixColumns}\) - Na každý jednotlivý sloupec se aplikuje substituce podle předpisu níže. Tato operace je vynechána v poslední rundě.

\[\begin{pmatrix}
b_0 \\
b_1 \\
b_2 \\
b_3
\end{pmatrix} = 
\begin{pmatrix}
2 & 3 & 1 & 1 \\
1 & 2 & 3 & 1 \\
1 & 1 & 2 & 3 \\
3 & 1 & 1 & 2
\end{pmatrix} \cdot
\begin{pmatrix}
a_0 \\
a_1 \\
a_2 \\
a_3
\end{pmatrix}\]

- \(\mathtt{AddRoundKey}\) - Na sloupce matice se postupně aplikuje XOR s rundovním klíčem.

Algoritmus pracuje s prvky Galoisova tělesa \(GF(2^8)\) a byty matice jsou chápány jako polynomy s koeficienty tohoto tělesa. Pro dešifrování stačí aplikovat inverzní operace k těm provedeným při šifrování.

## Poznámka Anki 1697483716047

Karty Anki: 1697483716047
GUID: m:dWcj?S;,; štítky: bi-hwb::p04 bi-spol::10.

### Otázka (Front)

Popište expanzi klíče AES.

### Odpověď (Back)

Uvažujme 32b slova a šifru AES s šifrovacím klíčem \(k\) o délce \(N_k\) slov. Dále mějme pole slov \(w\). Vložme klíč \(k\) na začátek pole \(w\), tedy do \(w[0], \dots, w[N_k - 1]\). Hodnotu \(w[i]\) pak získáme následujícím způsobem:

- Vybereme slovo \(w[i - N_k]\) a pokud \(|i|_{N_k} = 0\), aplikujeme na toto slovo posloupnost operací \(\mathtt{RotWord}\) (rotace bytů slova), \(\mathtt{SubWord}\) (substituce bytů slova) a \(\mathtt{Rcon}\) (násobení bytů slova konstantou).
- Vybereme slovo \(w[i - 1]\) a pokud je \(N_k > 6\) a zároveň \(|i|_{N_k} = 4\), aplikujeme na toto slovo operaci \(\mathtt{SubWord}\) (substituce bytů slova).
- Obě slova následně XORujeme a uložíme do \(w[i]\).

## Poznámka Anki 1698345056905

Karty Anki: 1698345056905
GUID: Gw>NLs!3j~; štítky: bi-hwb::p04 bi-spol::10.

### Otázka (Front)

Popište T-box.

### Odpověď (Back)

T-box je vyhledávací tabulka, která se používá jako rychlejší alternativa k posloupnosti operací \(\mathtt{SubBytes}\), \(\mathtt{ShiftRows}\) a \(\mathtt{MixColumns}\) v šifře AES. Každá z tabulek obsahuje předpočítaná výsledná slova pro všechny možné hodnoty bytu \(a\).
\[T_0[a] = \begin{bmatrix}
\mathtt{02} \cdot \mathtt{SBox(a)} \\
\mathtt{01} \cdot \mathtt{SBox(a)} \\
\mathtt{01} \cdot \mathtt{SBox(a)} \\
\mathtt{03} \cdot \mathtt{SBox(a)} \\
\end{bmatrix} \quad
T_1[a] = \begin{bmatrix}
\mathtt{03} \cdot \mathtt{SBox(a)} \\
\mathtt{02} \cdot \mathtt{SBox(a)} \\
\mathtt{01} \cdot \mathtt{SBox(a)} \\
\mathtt{01} \cdot \mathtt{SBox(a)} \\
\end{bmatrix} \quad
T_2[a] = \begin{bmatrix}
\mathtt{01} \cdot \mathtt{SBox(a)} \\
\mathtt{03} \cdot \mathtt{SBox(a)} \\
\mathtt{02} \cdot \mathtt{SBox(a)} \\
\mathtt{01} \cdot \mathtt{SBox(a)} \\
\end{bmatrix} \quad
T_3[a] = \begin{bmatrix}
\mathtt{01} \cdot \mathtt{SBox(a)} \\
\mathtt{01} \cdot \mathtt{SBox(a)} \\
\mathtt{03} \cdot \mathtt{SBox(a)} \\
\mathtt{02} \cdot \mathtt{SBox(a)} \\
\end{bmatrix}\]Byty \(d_{i, j}\) slova ve sloupci výsledného stavu získáme z bytů \(a_{i, j}\) slova ve sloupci aktuálního stavu pomocí součtu:
\[\begin{bmatrix}
d_{0, j} \\
d_{1, j} \\
d_{2, j} \\
d_{3, j} \\
\end{bmatrix} = T_0[a_{0, |j|_4}] \oplus T_1[a_{1, |j + 1|_4}] \oplus T_2[a_{2, |j + 2|_4}] \oplus T_3[a_{3, |j + 3|_4}].\]

