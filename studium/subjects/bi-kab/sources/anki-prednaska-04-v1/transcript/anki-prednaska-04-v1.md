# BI-KAB – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-kab/BI-KAB.apkg; APKG SHA-256 080060aa53ee5f63eca18237eef611a0bfca99908f9ab640e349ebadb96964ec. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8571882594c00598a0b5a029eed57cadb06fe0563741a3f883a87eacef0c1588.
Původní balíčky: BI-KAB
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678803651845

Karty Anki: 1678803651845
GUID: PtL9k!<%#/; štítky: bi-kab::p04 bi-spol::10.

### Otázka (Front)

Co je to bloková šifra?

### Odpověď (Back)

Bloková šifra je taková šifra, která OT šifruje po skupinách znaků (či bitů), které nazýváme bloky, přičemž na každý blok je aplikováno stejné šifrovací zobrazení
\[c_i = E_k(p_i).\]K dešifrování se používá inverzní zobrazení, tedy
\[p_i = D_k(c_i).\]Blokové šifry typicky používají jak prvky substitučních šifer, tak prvky transpozičních šifer a dosahují tak konfúze i difúze.

## Poznámka Anki 1678814457966

Karty Anki: 1678814457966
GUID: fRmX*m}197; štítky: bi-kab::p04 bi-spol::10.

### Otázka (Front)

Popište šifru Data Encryption Standard (DES).

### Odpověď (Back)

Data Encryption Standard (DES) je bloková šifra feistelovského typu. Používá 64b bloky, 16 rund a 64b klíč. Každý 8. bit klíče je paritní, takže jeho skutečná délka je použe 56 bitů. Tento klíč je buď na začátku nebo za chodu algoritmu expandován na 16 48b rundovních klíčů \(k_0, k_1, \dots, k_{15}\). Průběh šifrování je následující:

- Místo počátečního zašumění OT se použije pevná bezklíčová permutace.
- Blok OT je rozdělen na 32b poloviny \((L_0, R_0)\).
- Každá runda se liší použitím jiného rundovního klíče \(k_i\) transformuje \((L_i, R_i)\) na \((L_{i + 1}, R_{i + 1})\) podle předpisu

\[(L_{i + 1}, R_{i + 1}) = \big(R_i, L_i \oplus f(R_i, k_i) \big), \quad i \in0, \dots, 15 .\]

- Po 16. rundě dojde ještě k výměně levé a pravé strany podle konstrukce Feistelova kryptosystému.
- Na závěr se aplikuje inverzní permutace k počáteční pevné bezklíčové permutaci.

Díky konstrukci dle Feistelova kryptosystému stačí pro dešifrování pouze obrátit pořadí aplikace rundovních klíčů.

## Poznámka Anki 1678815190884

Karty Anki: 1678815190884
GUID: j:BzF[qlTu; štítky: bi-kab::p04.

Metadata původního zdroje pro kartu 1678815190884: původní příznak autora 7.

### Otázka (Front)

Popište rundovní funkci \(f\) šifry DES.

### Odpověď (Back)

Rundovní funkce provede v \(i\)-té rundě následující operace:

- Ze dvou rotovaných částí (rotace závisí na \(i\)) původního klíče šifry \(k\) je kompresní permutací vytvořen 48b rundovní klíč \(k_i\).
- Následně se provede XOR \(k_i\) s částí \(R_{i - 1}\), která byla expanzně permutována z 32 b na 48 b.

- Na úrovni S-boxů (substitučních boxů) je provedena substituce a transpozice, tedy je dosaženo konfúze a difúze (jedná se o **nelineární **část šifry).
- Výstupní slovo S-boxu je permutováno tak, aby žádný vstupní bit nebyl použit dvakrát.

## Poznámka Anki 1678815800748

Karty Anki: 1678815800748
GUID: ux|3X+oyLj; štítky: bi-kab::p04 bi-spol::10.

### Otázka (Front)

Popište šifru Triple DES (3DES).

### Odpověď (Back)

Triple DES je bloková šifra, která za sebou třikrát použije šifru DES. Nejčastěji se používá varianta 3DES-EDE, která šifruje podle transformace
\[c = E_{k_3} \Big( D_{k_2} \big(E_{k_1}(p) \big) \Big),\]kde klíče \(k_1\), \(k_2\) a \(k_3\) jsou buď vzájemně různé (celkem 168 efektivních bitů klíče) nebo \(k_1 = k_3\) (celkem 112 efektivních bitů klíče). Pro případ rovnosti všech klíčů dostáváme opět DES. Dešifrování potom probíhá podle transformace
\[p = D_{k_1} \Big( E_{k_2} \big(D_{k_3}(c) \big) \Big).\]

## Poznámka Anki 1678830609589

Karty Anki: 1678830609589
GUID: nT^2R[QK_~; štítky: bi-kab::p04 bi-spol::10.

Metadata původního zdroje pro kartu 1678830609589: původní příznak autora 7.

### Otázka (Front)

Popište šifru Advanced Encryption Standard (AES).

### Odpověď (Back)

Advanced Encryption Standard (AES) je bloková šifra, která je nástupcem šifry DES. AES není feistelovského typu a používá 128b bloky. Podporuje tři různé délky klíče, od kterých se odvíjí počet rund.      
|       **déka klíče** |       **počet rund **(\(N_r\)) |         
|       256 bitů |       14 |         
|       192 bitů |       12 |         
|       128 bitů |       10 |       Klíč je buď na začátku nebo za chodu algoritmu expandován na \(1 + N_r\) 128b rundovních klíčů. Blok OT se následně vloží do matice \(4 \times 4\) a jedenkrát se aplikuje operace \(\mathtt{AddRoundKey}\). Zbytek šifrování probíhá následovně:

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

## Poznámka Anki 1679405979339

Karty Anki: 1679405979339
GUID: qN@RoxZgk4; štítky: bi-kab::p04 bi-spol::10.

### Otázka (Front)

Jaké existují operační módy blokových šifer?

### Odpověď (Back)

Existují následující operační módy blokových šifer:

- electronic codebook (ECB),
- cipher feedback (CFB),
- output feedback (OFB),
- cipher block chaining (CBC),
- counter mode (CTR),
- message authentication code (MAC).

## Poznámka Anki 1679406254296

Karty Anki: 1679406254297
GUID: tTJAXQnjYj; štítky: bi-kab::p04 bi-spol::10.

### Otázka (Front)

Popište operační mód blokových šifer electronic codebook (ECB) a jeho nevýhody.

### Odpověď (Back)

Electronic codebook (ECB) je operační mód blokových šifer, který každý blok OT resp. ŠT šifruje resp. dešifruje zvlášť. Používá transformace:
\[\begin{matrix}
c_i = E_k(p_i), \\
p_i = D_k(c_i).
\end{matrix}\]ECB následující nevýhody:

- stejné bloky mají stejné obrazy (ulehčuje dešifrování),
- útočník může jednotlivé bloky vyměňovat, vyjímat nebo vkládat a docílit tak změn v OT.

 [Obrázek: paste-a64fee2e62e82132f0161b9f167e1f920fdedf85.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1679407120490

Karty Anki: 1679407120490
GUID: m@.a{Cp6$|; štítky: bi-kab::p04 bi-spol::10.

### Otázka (Front)

Popište operační mód blokových šifer cipher block chaining (CBC).

### Odpověď (Back)

Cipher block chaining (CBC) je operační mód blokových šifer. Funguje tak, že při šifrování je každý blok OT nejpre upraven pomocí předchozího bloku ŠT a až poté je šifrován. Pro úpravu prvního bloku OT se používá náhodný inicializační vektor. CBC používá transformace:
\[\begin{matrix}
c_0 = \text{IV}, \\
c_i = E_k(p_i \oplus c_{i - 1}), \\
p_i = D_k(c_i) \oplus c_{i - 1}.
\end{matrix}\]

 [Obrázek: paste-a245caa6511febe379b1e74050c7c6ae7d05e6dd.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1679408016886

Karty Anki: 1679408016886
GUID: m~$?fkRs1n; štítky: bi-kab::p04 bi-spol::10.

### Otázka (Front)

Popište operační módy blokových šifrer cipher feedback (CFB) a output feedback (OFB).

### Odpověď (Back)

Cipher feedback (CFB) resp. output feedback (OFB) jsou operační módy blokových šifer, které blokovou šifru převádí na asynchronní resp. synchronní proudovou šifru. Fungují tak, že předchozí vzniklý ŠT resp. blok hesla je upraven šifrovací transformací, čímž vzniká následující blok hesla \(h\), který je následně kombinován s OT pomocí operace XOR. **CFB** používá transformace:
\[\begin{matrix}
c_0 = \text{IV}, \\
c_i = p_i \oplus E_k(c_{i - 1}), \\
p_i = c_i \oplus E_k(c_{i - 1}).
\end{matrix}\]**OFB** používá transformace:
\[\begin{matrix}
c_0 = \text{IV}; && h = E_k(\text{IV}), \\
c_i = p_i \oplus h; && h = E_k(h), \\
p_i = c_i \oplus h; && h = E_k(h).
\end{matrix}\]

 [Obrázek: paste-84a08da437f688635c47c114344e15326cd2cc3a.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1679408742879

Karty Anki: 1679408742879
GUID: OW5qkg0*pL; štítky: bi-kab::p04 bi-spol::10.

### Otázka (Front)

Popište operační mód blokových šifer counter mode (CTR) a podmínky jeho použití.

### Odpověď (Back)

Counter mode (CTR) je operační mód blokových šifer, který blokovou šifru převádí na synchronní proudovou šifru. Funguje následovně:

- čítač \(T\) je inicializován blokem \(\text{IV}\);
- aplikací šifrovacího zobrazení \(E_K\) na \(T\) vzniká první blok hesla \(h\);
- první blok OT je pomocí operace XOR kombinován s prvním blokem hesla \(h\), čímž vzniká první blok ŠT;
- čítač \(T\) je aktualizován (např. inkrementován) a aplikací \(E_k\) může vzniknout další blok hesla \(h\).

CTR používá transformace:

\[\begin{matrix}
T_i = \text{IV} + i - 1, \\
h_i = E_k(T_i), \\
c_i = p_i \oplus h_i, \\
p_i = c_i \oplus h_i.
\end{matrix}\]Podobně jako u proudových šifer vzniká v důsledku opakovaného použití stejného hesla riziko prolomení šifry. Pokud je tedy operační mód CTR opakovaně používán se stejným klíčem, je nutné zajistit, aby se obsah čítače \(T\) při jednotlivých použitích lišil.

 [Obrázek: paste-974795c249abea2e564e52d0e88c5e7d1373bc83.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1679409150998

Karty Anki: 1679409150998
GUID: qx_Ui<N;/A; štítky: bi-kab::p04 bi-spol::10.

### Otázka (Front)

Popište operační mód blokové šifry message authentication code (MAC).

### Odpověď (Back)

Message authentication code řeší ten problém, že blokové a proudové šifry sice zajistí důvěrnost ale ne integritu přenášené zprávy. Zajišťuje tedy ochranu zprávy před změnami nebo chybami během přenosu. Výpočet MAC stejně jako CBC, ale s nulovým IV a průběžné bloky ŠT se nikam neposílají. K výpočtu by měl být použit jiný klíč, než byl použit k samotnému šifrování zprávy. MAC je dán transformacemi:
\[\begin{matrix}
c_0 = \text{IV} = 0 \\
c_i = E_{k_1}(p_i \oplus c_{i - 1}) \quad i \in 1, 2, \dots n \\
\text{MAC} = E_{k_2}(c_n)
\end{matrix}\]

 [Obrázek: paste-bd49093a18f6041fbd2e38f14917a070aab758f0.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1681548985107

Karty Anki: 1681548985107
GUID: wf.BO9#5RH; štítky: bi-kab::p04 bi-spol::10.

### Otázka (Front)

Popište šifrování a dešifrování pomocí Feistelova kryptosystému.

### Odpověď (Back)

Mějme posloupnost rundovních funkcí \(f_0, f_2, \dots f_{h - 1}\). Postup šifrování je následující:

- Blok OT rozdělíme na dvě poloviny \((L_0, R_0)\).
- Pro každou rundu \(i = 0, \dots, h - 1\) spočteme

\[(L_{i + 1}, R_{i + 1}) = \big(R_i, L_i \oplus f_i(R_i) \big).\]

- Výstup poslední rundy prohodíme a jako ŠT dostaneme \((R_h, L_h)\).

Výhoda Feistelova kryptosystému spočívá v tom, že rundovní funkce **nemusejí být invertibilní**. Pro dešifrování je stačí použít v opačném pořadí:

- Blok ŠT rozdělíme na dvě poloviny \((R_h, L_h)\).
- Pro každou rundu \(i = h - 1, \dots, 0\) spočteme

\[(R_i, L_i) = \big(L_{i + 1}, R_{i + 1} \oplus f_i(L_{i + 1})\big).\]

- Výstup poslední rundy prohodíme a jako OT dostaneme \((L_0, R_0)\).

