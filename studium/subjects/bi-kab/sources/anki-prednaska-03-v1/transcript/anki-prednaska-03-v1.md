# BI-KAB – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-kab/BI-KAB.apkg; APKG SHA-256 080060aa53ee5f63eca18237eef611a0bfca99908f9ab640e349ebadb96964ec. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8571882594c00598a0b5a029eed57cadb06fe0563741a3f883a87eacef0c1588.
Původní balíčky: BI-KAB
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678185386780

Karty Anki: 1678185386781
GUID: M>HHf7c%~8; štítky: bi-ib::13 bi-kab::p03 bi-spol::10.

### Otázka (Front)

Co je to proudová šifra? Jakou běžně používá transformaci OT?

### Odpověď (Back)

Proudová šifra je symetrická šifra. Před začátkem šifrování je z šifrovacího klíče \(k\) vygenerována pseudonáhodná heslová posloupnost (keystream) \(h_1, h_2, \dots\), kde každý prvek \(h_i\) představuje libovolnou substituci \(E_{h_i}\). OT je potom znak po znaku či bit po bitu kombinován s heslem. Protože šifrování zpravidla probíhá nad binární abecedou, kombinuje se OT s heslem pomocí operace XOR. Šifrovací a dešifrovací zobrazení jsou tedy definována jako
\[\begin{matrix}
c_i = E_{h_i}(p_i) = p_i \oplus h_i, \\
p_i = D_{h_i}(c_i) = c_i \oplus h_i.
\end{matrix}\]Šifrovací a dešifrovací transformace je stejná, protože binární sčítání a odečítání jsou ekvivalentní operace.

## Poznámka Anki 1678186131178

Karty Anki: 1678186131178
GUID: DW+E4]l|nR; štítky: bi-kab::p03.

### Otázka (Front)

Kdy šifru nazveme absolutně bezpečnou? Uveďte příklad.

### Odpověď (Back)

Šifra je absolutně bezpečná, pokud ŠT nenese žádnou informaci o OT. Přikladem je Vernamova šifra.

## Poznámka Anki 1678186633052

Karty Anki: 1678186633052
GUID: xrdEV4&cgq; štítky: bi-kab::p03 bi-spol::10.

### Otázka (Front)

Co je to Vernamova šifra?

### Odpověď (Back)

Vernamova šifra je proudová šifra (šla by řadit ale i mezi polyalfabetické substituční), která je absolutně bezpečná, při splnění následujících podmínek:

- klíč je tak dlouhý jako OT,
- klíč je dokonale náhodný,
- klíč není použit opakovaně,
- klíč je udržen v tajnosti.

## Poznámka Anki 1678188397269

Karty Anki: 1678188397269
GUID: H~x6+uC2ju; štítky: bi-ib::13 bi-kab::p03 bi-spol::10.

### Otázka (Front)

Co je to algoritmická proudová šifra?

### Odpověď (Back)

Aby klíč proudové šifry nemusel být měněn příliš často, používá se měnící inicializační vektor, který je vždy vybrán náhodně a je přenášen v otevřené formě. IV uvede algoritmus pro generování hesla po každé do jiného iniciálního stavu, čímž je zajištěna různost hesla.

## Poznámka Anki 1678190676993

Karty Anki: 1678190676994
GUID: lCb}m8NG?E; štítky: bi-ib::13 bi-kab::p03 bi-spol::10.

### Otázka (Front)

Popište šifru RC4.

### Odpověď (Back)

RC4 je proudová šifra, která umožňuje používat klíče \(k\) s různými délkami \(n\) do maxima 256 bytů. Nejdříve inicializuje identickou permutaci \(S\), kterou promíchá pomocí klíče \(k\). 

- \(S(0) = 0, S(1) = 1, \dots S(255) = 255\)

- \(j = 0\)
- \(\mathtt{for} \ i = 0 \ \mathtt{to} \ 255\)

- \(j = | j + S(i) + k( |i|_n ) |_{256}\)
- \(\mathtt{swap}\big( S(i), S(j) \big)\)

Z takto promíchané permutace \(S\) potom pseudonáhodně generuje heslovou posloupnost.

- \(i = j = 0\)

- \(\mathtt{for} \ l = 0 \ \mathtt{to} \ n -1\)

- \(i = | i + 1 |_{256}\)
- \(j = | j + S(i) |_{256}\)
- \(\mathtt{swap}\big( S(i), S(j) \big)\)
- \(h(l) = S\big( | S(i) + S(j) |_{256} \big)\)

## Poznámka Anki 1678190959098

Karty Anki: 1678190959098
GUID: A;-ferL[nt; štítky: bi-kab::p03 bi-spol::10.

### Otázka (Front)

Proč u aditivní šifry není vhodné použít stejné heslo vícekrát?

### Odpověď (Back)

Pokud narazíme na dva ŠT \(c\) a \(c'\) šifrované pomocí stejného hesla a víme, že byla použita invertibilní operace (jako např. XOR nebo sčítání), lze od sebe oba ŠT odečíst, čímž eliminujeme heslo.
\[\begin{matrix}
\begin{matrix}
c_i =  | p_i + h_i |_m \\
c'_i = | p'_i + h_i |_m \\
\hline
\end{matrix} \\
\begin{matrix}
| c_i - c'_i |_m = | p_i - p'_i |_m \\
\end{matrix}
\end{matrix}\]Dále už můžeme luštit jako při použití knižní šifry.

## Poznámka Anki 1678191023789

Karty Anki: 1678191023789
GUID: FR<h]^]@%P; štítky: bi-kab::p03 bi-spol::10.

### Otázka (Front)

Jaká je aplikace proudové šifry?

### Odpověď (Back)

Proudové šifry s výhodou použijeme v případě, že do komunikačního kanálu přicházejí znaky v pravidelných či nepravidelných časových intervalech a zároveň je nutné tyto znaky přenést okamžitě. Příkladem může být terminálové spojení.

## Poznámka Anki 1678191575162

Karty Anki: 1678191575162
GUID: q#:Fr[WY!d; štítky: bi-kab::p03 bi-spol::10.

### Otázka (Front)

Co jsou to synchronní a asynchronní proudové šifry?

### Odpověď (Back)

Pokud heslo nezávisí na ŠT ani OT je proudová šifra **synchronní**. Při použití synchronní šifry musí totiž být odesílatel i příjemce přesně synchronizováni, jinak může výpadek jednoho znaku ŠT narušit zbývající část zprávy. **Asynchronní **(samosynchronizující) proudová šifra naopak pro generování hesla používá jak klíč tak \(n\) předchozích bitů či znaků ŠT, tedy po souvislé posloupnosti \(n + 1\) správných bitů či znaků ŠT dojde automaticky k synchronizaci.

## Poznámka Anki 1678192462231

Karty Anki: 1678192462231
GUID: ixSgY[f_+k; štítky: bi-kab::p03 bi-spol::10.

### Otázka (Front)

Popište šifru Salsa20.

### Odpověď (Back)

Šifra Salsa20 je proudová šifra založená na operaci add-rotate-XOR (ARX). Vnitřní stav je tvořen 32bitovými slovy v matici \(4 \times 4\) obsahující 8 klíčových slov, 2 slova pozice keystreamu, 2 slova nonce a 4 pevná slova:

 [Obrázek: paste-864c97db58624dd09ed5be4bc3013bb02c8d7720.jpg; soubor je v media/ v doprovodném ZIP] 

Základní operací je čtvrtinová runda (quarter-round) \(\text{QR}(a, b, c, d)\), jejímž vstupem i výstupem jsou čtyři slova. Liché rundy aplikují \(\text{QR}\) na sloupce matice, sudé zase na řádky.\[\begin{matrix}
a := a \oplus (d \boxplus c ) \lll 18 \\
b := b \oplus (a \boxplus d) \lll 7 \\
c := c \oplus (b \boxplus a) \lll 9 \\
d := d \oplus (c \boxplus b) \lll 13
\end{matrix}\]Rund proběhne dohromady 20 a následně se k výsledku přičte vstup. Výstupem je 64 B keystreamu.

## Poznámka Anki 1678200090661

Karty Anki: 1678200090661
GUID: c4T1mW!X=V; štítky: bi-kab::p03 bi-spol::10.

### Otázka (Front)

Popište šifru A5/1.

### Odpověď (Back)

A5/1 je synchronní proudová šifra, který se používá k zabezpečení komunikace mobilních telefonů. Skládá se z tří linear-feedback shift registrů (LFSR).

 [Obrázek: paste-1fe3dad51a8bcb38f375b6585df11bc1a130352f.jpg; soubor je v media/ v doprovodném ZIP] 

Zvýrazněné bity se nazývají taktovací bity. Jeden takt šifry vypadá následovně:

1. Spočte se většinová hodnota \(h\) taktovacích bitů.
2. Posunou se ty registry, které mají taktovací bit rovný \(h\).
3. Spočte se XOR nejvyšších bitů registrů a vznikne tak jeden bit keystreamu.
4. Pomocí zpětné vazby se doplní posuvné registry.

Právě mechanizmus posouvání registrů na základě taktovacích bitů je jediným **nelineárním** prvkem šifry a stojí na něm její bezpečnost.

## Poznámka Anki 1678214173473

Karty Anki: 1678214173473
GUID: KgH+OpQ0Wv; štítky: bi-kab::p03 bi-spol::10.

Metadata původního zdroje pro kartu 1678214173473: původní příznak autora 7.

### Otázka (Front)

Jak probíhá inicializace A5/1?

### Odpověď (Back)

Bity vešech tří registrů se nastaví na \(\mathtt 0\). Následně se bit po bitu XORují všechny tři registry s 64b klíčem, přičemž po každém bitu jsou všechny registry posunuty. Stejným způsobem jsou registry XORovány s 22b inicializačním vektorem. Na závěr je vykonáno 100 taktů šifry a jejich výstup je zahozen.

## Poznámka Anki 1678214385375

Karty Anki: 1678214385375
GUID: M,bm_Y=R0P; štítky: bi-kab::p03 bi-spol::10.

### Otázka (Front)

Jak probíhá šifrování telefonního hovoru pomocí A5/1?

### Odpověď (Back)

Komunikace spočívá v přenosu posloupnosti rámců o 228 bitech, kde prvních 114 bitů se využije pro šifrování směru GSM-telefon a druhá polovina potom pro opačný směr. Pro jeden rámec se provedou následující kroky:

- inicializace šifry,
- provedení 228 taktů, čímž se vyprodukuje 228 bitů keystreamu.

Pro další rámce se použije stejný klíč, ale jiný inicializační vektor.

## Poznámka Anki 1678802131678

Karty Anki: 1678802131679
GUID: rZh{v>uI$~; štítky: bi-kab::p03 bi-spol::10.

### Otázka (Front)

Popište šifru ChaCha20.

### Odpověď (Back)

ChaCha20 je proudová šifra, která vznikla upravením šifry Salsa20. Její vnitřní stav je opět tvořen 32bitovými slovy v matici \(4 \times 4\) obsahující 8 klíčových slov, 2 slova counteru, 2 slova nonce a 4 pevná slova:

 [Obrázek: paste-cf0b614217c48c5a2daf35ca3d01d0e0a02ad6ee.jpg; soubor je v media/ v doprovodném ZIP] 

Základní operací je stejně jako u Salsa20 čtvrtinová runda (quarter-round) \(\text{QR}(a, b, c, d)\) s čtyřmi vstupními a čtyřmi výstupními slovy. Liché rundy se aplikují na sloupce ale sudé rundy na diagonály. \(\text{QR}\) je nyní definována následovně:
\[\begin{matrix}
a := a \boxplus b; \quad d := d \oplus a; \quad d \lll 16 \\
c := c \boxplus d; \quad b := b \oplus c; \quad b \lll 12 \\
a := a \boxplus b; \quad d:= d \oplus a; \quad d \lll 8 \\
c := c \boxplus d; \quad b := b \oplus c; \quad b \lll 7
\end{matrix}\]Rund proběhne dohromady 20 a následně se k výsledku přičte vstup. Výstupem je 64 B keystreamu.

