# BI-KAB – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-kab/BI-KAB.apkg; APKG SHA-256 080060aa53ee5f63eca18237eef611a0bfca99908f9ab640e349ebadb96964ec. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8571882594c00598a0b5a029eed57cadb06fe0563741a3f883a87eacef0c1588.
Původní balíčky: BI-KAB
Rozsah: 18 poznámek, 18 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1682426629640

Karty Anki: 1682426629640
GUID: fH[jm%-I@; štítky: bi-kab::p09.

### Otázka (Front)

Popište kryprografii eliptických křivek (ECC).

### Odpověď (Back)

ECC je současným a moderním směrem  kryptografie. Poskytuje alternativu pro realizaci elektronických podpisů nebo RSA. Navíc je oproti starším kryptosystémům rychlejší a méně náročný na hardware.

## Poznámka Anki 1682426931060

Karty Anki: 1682426931060
GUID: KWcN1saXR*; štítky: bi-ib::12 bi-ib::13 bi-kab::p09 bi-spol::09.

### Otázka (Front)

Definujte eliptickou křivku. Co pro ni platí?

### Odpověď (Back)

Eliptická křivka \(E\) je taková množina bodů v rovině, že všechny její body vyhovují rovnici
\[y^2 = x^3 + ax + b.\]Platí, že součtem dvou různých bodů \(P\) a \(Q\) z \(E\) bude opět bod ležící na \(E\), tedy vyhovující výše uvedené rovnici.

## Poznámka Anki 1682427532369

Karty Anki: 1682427532369
GUID: f0!sz0?{sM; štítky: bi-ib::12 bi-ib::13 bi-kab::p09 bi-spol::09.

### Otázka (Front)

Popište variantu eliptických křivek využívaných v kryptografii.

### Odpověď (Back)

V kryptografii využíváme eliptickou křivku nad aditivním Galoisovým tělesem \(GF(p)\), kde \(p\) je prvočíslo (příp. \(GF(2^m)\)). Ta je definována jako bod \(O\) v nekonečnu společně s množinou bodů \(P = [x,y]\), kde \(x, y \in GF(p)\) a vyhovují rovnici
\[y^2 = x^3 + ax + b \pmod p.\]

## Poznámka Anki 1682428534470

Karty Anki: 1682428534470
GUID: A8~88EW{yn; štítky: bi-ib::12 bi-kab::p09.

### Otázka (Front)

Definujte řád bodu na eliptické křivce.

### Odpověď (Back)

Pro bod \(P \in E\) postupně konstruujeme posloupnost \(1 \cdot P, 2 \cdot P, 3 \cdot P, \dots\), což jsou body ležící na \(E\). Protože křivka \(E\) má konečný počet bodů \(\#E\), začne se po určitém kroku \(m \in \mathbb N\) posloupnost opakovat. Tedy pro \(n \in \mathbb N\) platí
\[n \cdot P = m \cdot P \quad \text{neboli} \quad n \cdot P - m \cdot P = O.\]Nejmenší \(r = m - n\) takové, že \(r \cdot P = O\) nazveme **řádem bodu **\(P\).

## Poznámka Anki 1682428619878

Karty Anki: 1682428619878
GUID: wMj}tcbc]U; štítky: bi-kab::p09.

### Otázka (Front)

Definujte řád eliptické křivky. Co pro něj platí?

### Odpověď (Back)

Řádem eliptické křivky \(E\) nazveme počet bodů na této křivce, tedy \(\#E\). Platí, že řád bodu \(P \in E\) dělí řád této křivky.

## Poznámka Anki 1682428946208

Karty Anki: 1682428946209
GUID: CC)kR!C@*N; štítky: bi-kab::p09.

### Otázka (Front)

Co je to kofaktor eliptické křivky?

### Odpověď (Back)

Mějme eliptickou křivku \(E\) řádu \(\#E\) a řád \(r\) jejího počátečního bodu \(P\). Kofaktor potom definujeme jako následující podíl
\[\frac {\#E} {r}\]a pro potřeby kryptografie požadujeme, aby byl malý.

## Poznámka Anki 1682429503543

Karty Anki: 1682429503544
GUID: dD3%oc6SnE; štítky: bi-kab::p09.

### Otázka (Front)

Jaké body z eliptických křivek vybíráme pro potřebu kryptografie?

### Odpověď (Back)

V kryptografii vybíráme takové body, jejichž řád je roven největšímu prvočíslu v rozkladu čísla \(\#E\) nebo jeho násobku.

## Poznámka Anki 1682429676116

Karty Anki: 1682429676116
GUID: H{gGJlzgj%; štítky: bi-kab::p09.

### Otázka (Front)

Jaký je rozdíl mezi klasickou a kvantovou informací? Z čeho tento rozdíl pramení?

### Odpověď (Back)

**Klasickou informaci** lze libovolně kopírovat a číst, zejména lze vytvořit identickou kopii takové informace. **Kvantovou informaci **její čtení ovlivňuje, proto nelze vytvořit identickou kopii neznámého kvantového stavu. To vychází z **Heisenbergova principu neurčitosti**.

## Poznámka Anki 1682430007830

Karty Anki: 1682430007830
GUID: xQ>OE~;r-j; štítky: bi-kab::p09.

### Otázka (Front)

Vyslovte Heisenbergův princip neurčitosti.

### Odpověď (Back)

Heisenberův princip neurčitosti je matematická vlastnost dvou kanonicky konjugovaných veličin. Nejznáměji je definován pro polohu a hybnost elementární částice v kvantové fyzice:
\[\Delta x \cdot \Delta p = \frac \hbar 2,\]kde \(\hbar \) je redukovaná Planckova konstanta. Tedy čím přesněji určíme jednu z konjugovaných veličin, tím méně přesně lze určit veličinu druhou.

## Poznámka Anki 1682430190432

Karty Anki: 1682430190432
GUID: eHSE9m;X`D; štítky: bi-kab::p09.

### Otázka (Front)

Jaký je rozdíl mezi klasickou a kvantovou kryptografií?

### Odpověď (Back)

**Klasická kryptografie **se musí vyrovnat s možností neomezeného kopírování nosičů klasické informace, kdežto **kvantová kryptografie **je založena na nemožnosti tvorby identických kopií neznámého kvantového stavu.

## Poznámka Anki 1682430586914

Karty Anki: 1682430586914
GUID: G~tE3X-)b(; štítky: bi-kab::p09.

### Otázka (Front)

Co je to kvantový bit (qubit)?

### Odpověď (Back)

Za fyzikální obraz qubitu považujeme libovolný kvantově mechanicky popsaný objekt (foton, elektron, atom) jehož stavy jsou prvky dvourozměrného Hilbertova prostoru. Měřením qubitu získáme hodnotu odpovídající právě jednomu vlastnímu stavu, tedy nejvýše jeden bit klasické informace.

## Poznámka Anki 1682445623664

Karty Anki: 1682445623664
GUID: m(r$<-UU]9; štítky: bi-ib::12 bi-kab::p09 bi-spol::09.

### Otázka (Front)

Popište problém diskrétního logaritmu nad eliptickou křivkou.

### Odpověď (Back)

Mějme eliptickou křivku \(E\). Zvolme si číslo \(k\) jako privátní klíč a spočtěme \(Q = k \cdot P\), kde \(P \in E\). Potom \(Q\) a \(P\) můžeme vystavit jako část veřejného klíče. Problém diskrétního logaritmu spočívá v tom, jak z bodů \(Q\) a \(P\) získat zpět klíč \(k\). Pro malý řád \(r\) bodu \(P\) je úloha triviální, ale pokud máme \(r = 2^{256}\), dostáváme přibližně \(2^{128}\) operací, což je zhruba na úrovni luštitelnosti symetrické blokové šifry se 128b klíčem. Z výpočetního hlediska se tedy jedná o neřešitelnou úlohu.

## Poznámka Anki 1682446592425

Karty Anki: 1682446592425
GUID: I04([)*yi[; štítky: bi-ib::12 bi-ib::13 bi-kab::p09 bi-spol::09.

### Otázka (Front)

Popište Diffie-Hellmannův algoritmus nad eliptickou křivkou.

### Odpověď (Back)

Mějme eliptickou křivku \(E\) s počátečním bodem \(P\) (veřejné parametry). Každý subjekt nechť si náhodně zvolí svůj tajný klíč \(k_i\). Pro dva subjekty A a B s klíči k \(k_\text A\) a \(k_\text B\) probíhá komunikace následovně:

- Subjekt A spočte a pošle druhému subjektu bod \(Q_\text A \in E\), pro který platí

\[Q_\text A = k_\text A \cdot P.\]

- Subjekt B spočte společný bod \(X \in E\) pomocí vztahu

\[X = k_\text B \cdot Q_\text A = k_\text A \cdot k_\text B \cdot P.\]

- Subjekt B spočte a pošle prvnímu subjektu bod \(Q_\text B \in E\), pro který platí

\[Q_\text B = k_\text B \cdot P.\]

- Subjekt A spočte společný bod \(X\) pomocí vztahu

\[X = k_\text A \cdot Q_\text B = k_\text A \cdot k_\text B \cdot P.\]Podle smluveného algoritmu se ze společného bodu \(X\) spočte společný klíč \(K\). Neautorizované subjekty odposlouchávající komunikaci nemohou \(X\) (resp.  \(K\)) najít v rozumném čase, neboť by byly nuceny řešit problém diskrétního logaritmu nad eliptickou křivkou.

## Poznámka Anki 1682447082966

Karty Anki: 1682447082966
GUID: P|mM*m34-4; štítky: bi-kab::p09.

### Otázka (Front)

K čemu je dnes používán algoritmus Benett-Brassard 1984 (BB84)? Na čem je založen?

### Odpověď (Back)

BB84 se používá ke zřízení společného klíče pro symetrickou Vernamovu šifru na základě kvantových jevů, které jsou schopny zajistit perfektní utajení. Je založen na Heisenbergově principu neurčitosti v kombinaci s polarizačním kódováním.

## Poznámka Anki 1682447279011

Karty Anki: 1682447279011
GUID: pWMP/U%QK:; štítky: bi-kab::p09.

### Otázka (Front)

Popište průběh komunikace algoritmu BB84.

### Odpověď (Back)

Algoritmus BB84 probíhá následovně:

- Odesílatel vygeneruje náhodnou binární posloupnost a provede její polarizační kódování dle náhodně zvolené báze.

 [Obrázek: paste-4b76512e12c6b543d743f763ac77062fb9a89b45.jpg; soubor je v media/ v doprovodném ZIP] 

- Příjemce dekóduje přijaté fotony dle náhodně zvolené báze.

 [Obrázek: paste-8686b99c0fb445848210aa88af75f04ebc397d9c.jpg; soubor je v media/ v doprovodném ZIP] 

- Odesílatel oznámí přijemci (veřejně s autentizací původu zprávy), jakou bázi při kódování použil. To samé učiní i příjemce. Bity, kde došlo ke shodě, budou použity pro symetrický klíč.

 [Obrázek: paste-d2836e6d10375ff359d8dcff8c2e87b464a1dcf8.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1683577091670

Karty Anki: 1683577091670
GUID: EL_}J`lk7J; štítky: bi-kab::p09.

### Otázka (Front)

Popište princip detekce odposlechu v protokolu BB84. Co je to Privacy Aplification?

### Odpověď (Back)

Princip detekce odposlechu algoritmu BB84 spočívá v tom, že odposlouchávající útočník změní stav odposlouchávaných qubitů, což se projeví jako chyba v přenosu. Po skončení průběhu algoritmu BB84 tedy obě strany obětují několik bitů klíče a veřejným kanálem (s autentizací původu zprávy) je porovnají. Pokud se shodují, může být klíč použit, pokud ne, pravděpodobně došlo k odposlechu a algoritmus musí být opakován. V současných systémech se ještě používá Privacy Amplification, která má za cíl dále minimalizovat množství informace, které útočník mohl odposlechnout.

## Poznámka Anki 1683637127197

Karty Anki: 1683637127197
GUID: muq2q%ho>@; štítky: bi-kab::p09.

### Otázka (Front)

Popište proces odposlechu u protokolu BB84 a odvození pravděpodobnosti detekce odposlechu.

### Odpověď (Back)

[Obrázek: paste-066f04ae9e3949e239fecffb13e976c935951abc.jpg; soubor je v media/ v doprovodném ZIP] 

Při obětování \(n\) bitů je pravděpodobnost úspěšné detekce odposlechu
\[1 - \Big( \frac 3 4 \Big)^n.\]

## Poznámka Anki 1684497003510

Karty Anki: 1684497003510
GUID: G2^^j_Rbw0; štítky: bi-ib::12 bi-kab::p09.

### Otázka (Front)

Co je to singulární eliptická křivka?

### Odpověď (Back)

Singulární eliptická křivka je taková křivka, která má nulový diskriminant
\[D= 4 a^3 + 27 b ^2.\]Tyto křivky jsou nevhodné pro kryptografii, protože obsahují body, ve kterých je výpočet diskrétního logaritmu jednoduchý nebo naprosto triviální.

