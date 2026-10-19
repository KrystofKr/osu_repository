# BI-KAB – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-kab/BI-KAB.apkg; APKG SHA-256 080060aa53ee5f63eca18237eef611a0bfca99908f9ab640e349ebadb96964ec. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8571882594c00598a0b5a029eed57cadb06fe0563741a3f883a87eacef0c1588.
Původní balíčky: BI-KAB
Rozsah: 22 poznámek, 22 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1679483142577

Karty Anki: 1679483142577
GUID: O$u0DE72jH; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Definujte jednosměrnou funkci.

### Odpověď (Back)

Funkci \(f: X \to Y\) nazveme jednosměrnou, právě když je jednoduché pro libovolnou hodnotu \(x \in X\) spočítat její obraz \(y = f(x)\), ale pro náhodně zvolený obraz \(y \in f(X)\) nelze (je výpočetně nemožné) najít jeho vzor \(x \in X\) takový, aby platilo \(y = f(x)\), přestože však víme, že alespoň jeden takový vzor existuje.

## Poznámka Anki 1679483293479

Karty Anki: 1679483293479
GUID: E9?}fT+Ocr; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Jak dělíme jednosměrné funkce?

### Odpověď (Back)

Rozeznáváme jednosměrné funkce 1. a 2. typu. U jednosměrných funkcí **1. typu** je jednosměrnost dána složitostí operace a její inverze (např. násobení prvočísel vs. faktorizace výsledku). Jednodsměrnost jednosměrných funkcí **2. typu** je dána znalostí „padacích vrátek“ (např. klíč u asymetrické kryptografie).

## Poznámka Anki 1679483668576

Karty Anki: 1679483668576
GUID: p/!J`#jdqJ; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Definujte kryptografickou hashovací funkci.

### Odpověď (Back)

Mějme množinu \(X\) obsahující všechny binární řetězce délky nejvýše \(d \in \mathbb N_0\). Funkci \(h: X \to \{ 0, 1 \}^n\) nazveme kryptografickou hashovací funkcí, jestliže je jednosměrná 1. typu a bezkolizní. Říkáme, že každému binárnímu řetězci z množiny \(X\) přiřadí binární hash délky \(n\) bitů.

## Poznámka Anki 1679483734267

Karty Anki: 1679483734267
GUID: pthAj?BLti; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Co je to orákulum?

### Odpověď (Back)

Orákulum je libovolný stroj, který na vstup odpovídá výstupem, přičemž pro stejný vstup vrací vždy stejný výstup.

## Poznámka Anki 1679483831034

Karty Anki: 1679483831034
GUID: A`lHga^F$Q; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Co je to náhodné orákulum a jaký má vztah k hashovací funkci?

### Odpověď (Back)

Náhodné orákulum je takové orákulum, které na nový vstup odpovídá náhodným výběrem z množiny výstupů. Z hlediska bezpečnosti požadujeme, aby se hashovací funkce chovala jako náhodné orákulum.

## Poznámka Anki 1679483955297

Karty Anki: 1679483955297
GUID: KD2}j^o0Fd; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Definujte bezkoliznost 1. řádu.

### Odpověď (Back)

Hashovací funkce \(h\) je odolná proti kolizi 1. řádu, jestliže je výpočetně nemožné nalézt dva různé vzory \(x\) a \(x'\) tak, aby \(h(x) = h(x')\).

## Poznámka Anki 1679484024099

Karty Anki: 1679484024099
GUID: I8uRu[buVl; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Definujte bezkoliznost 2. řádu.

### Odpověď (Back)

Hashovací funkce \(h\) je odolná proti kolizi 2. řádu, jestliže pro jakýkoliv vzor \(x\) je výpočetně nemožné nalézt druhý vzor \(x'\) takový, že \(x \neq x'\) a zároveň \(h(x) = h(x')\).

## Poznámka Anki 1679490512948

Karty Anki: 1679490512948
GUID: m,/2J-qB}_; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Popište narozeninový paradox. Jaká je složitost nalezení kolize 1. řádu?

### Odpověď (Back)

Narozeninový paradox odpovídá na otázku kolik lidí v místnosti stačí, aby byla pravděpodobnost 50 %, že aspoň dva mají narozeniny ve stejný den.

**Odvození**
Mějme množinu \(n\) různých kuliček a proveďme výběr \(k\) kuliček postupně po jedné s vracením do množiny. Potom pravděpodobnost, že vybereme některou kuličku dvakrát nebo vícekrát je
\[P(n, k) = 1- \frac{n(n - 1) \cdots (n - k + 1)}{n^k} \approx 1 - e^{-\frac{k \cdot (k + 1)}{2n}}.\]V důsledku platí, že pro velká \(n\) se při výběru \(k = (2n \cdot \ln 2)^{\frac 1 2} \approx n^{\frac 1 2}\) kuliček s přibližně 50% pravděpodobností stane, že vybereme dvakrát stejnou kuličku. Tedy pro hashovací funkci s \(b\) bitovým hashem potřebujeme zahashovat \(n^{\frac 1 2} = (2^b)^{\frac 1 2} = 2^{\frac b 2}\) zpráv, abychom s 50% pravděpodobností nalezli kolizi 1. řádu.

## Poznámka Anki 1679491117646

Karty Anki: 1679491117646
GUID: fItkVOu><0; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Jaká je složitost nalezení kolize 2. řádu?

### Odpověď (Back)

Pokud se hashovací funkce \(h\), která generuje \(n\)-bitový hash, chová jako náhodné orákulum, pak je složitost nalezení kolize 2. řádu přibližně \(2^n\).

## Poznámka Anki 1680007957936

Karty Anki: 1680007957936
GUID: q5+k*x22Y3; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Jak fungují moderní hashovací funkce?

### Odpověď (Back)

Protože zprávy mohou být velmi dlouhé, zpracovávají je moderní hashovací funkce postupně po blocích. To nám ale přináší potřebu zprávu zarovnat na celý počet bloků. Po tomto zarovnání budeme požadovat, aby bylo bezkolizní a šlo jednoznačně odejmout** **(např. zprávy \(\mathtt 1\) a \(\mathtt{10}\) by při zarování nulami zprava na délku \(3\) měli stejný obraz).

## Poznámka Anki 1680008169275

Karty Anki: 1680008169276
GUID: DJ!v(lsPx$; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Jaké se používají metody k zarovnání do bloků u hashovacích funkcí?

### Odpověď (Back)

Existují dva přístupy:

- zprávu doplníme bitem \(\mathtt 1\) a poté potřebným počtem bitů \(\mathtt 0\);

- použijeme Damgård-Merklovo zesílení - zprávu nejprve doplníme bitem \(\mathtt 1\) a poté bity \(\mathtt 0\) tak, aby do celého bloku zbývalo ještě 64 bitů a do tohoto zbývajícího prostoru vložíme počet bitů původní zprávy.

## Poznámka Anki 1680009306638

Karty Anki: 1680009306638
GUID: k|eYMD$!f:; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Popište Damgård-Merklovu konstrukci hashovací funkce. Jak vzniká výsledný hash?

### Odpověď (Back)

Hashovací funkce \(f\) je konstruována tak, že do ní vstupuje aktuální blok zprávy \(M_i\) a kontext (prostupující hash) \(H_{i - 1}\). Pro první blok je kontext dán konstantním inicializačním vektorem. Tedy platí:
\[\begin{matrix}
H_0 = \text{IV}, \\
H_i=f( M_i, H_{i - 1}).
\end{matrix}\]Zahashováním posledního bloku zprávy \(M_n\) dostáváme \(H_n\), z něhož bereme buď část nebo celou délku jako výsledný hash. Protože \(f\) zpracovává širší vstup na kratší, nazveme \(f\) kompresní funkcí.

## Poznámka Anki 1680009438851

Karty Anki: 1680009438851
GUID: )]g/=F=Pe; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Co je to kolize kompresní funkce?

### Odpověď (Back)

Kolize kompresní funkce \(f\) spočívá v nalezení inicializační hodnoty \(H\) a dvou různých bloků \(B_1\) a \(B_2\) tak, že \(f(H, B_1) = f(H, B_2)\).

## Poznámka Anki 1680010636738

Karty Anki: 1680010636738
GUID: xw.PX==BsR; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Co platí pro bezkoliznost hashovací a kompresní funkce u Damgård-Merklovy konstrukce?

### Odpověď (Back)

Obecně platí, že je-li hashovací funkce bezkolizní, pak je i kompresní funkce bezkolizní, ale naopak tato implikace v obecném případě neplatí. U Damgård-Merklovy konstrukce je však dokázáno, že pokud je kompresní funkce bezkolizní, pak je bezkolizní i z ní zkonstruovaná iterovaná hashovací funkce. Této vlastnoti využívají všechny moderní hashovací funkce, protože umožňuje soustředit se pouze na návrh kvalitní kompresní funkce.

## Poznámka Anki 1680012634205

Karty Anki: 1680012634205
GUID: GWl::^F:5?; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Popište konstrukci kompresní funkce.

### Odpověď (Back)

Po kompresní funkci chceme, aby byla robustní, zajistila dokonalé promíchání bitů zprávy a aby byla jednosměrná. Konstrukce kompresních funkcí na bázi blokových šifer splňuje požadavky na jednosměrnost a na chování náhodného orákula. Kvalitní bloková šifra \(E_k\) je totiž jednosměrná vzhledem k pevnému klíči. Odtud plyne možnost konstrukce kompresní funkce jako
\[H_i = f(M_i, H_{i - 1}) = E_{M_i}(H_{i - 1}).\]

## Poznámka Anki 1680013522641

Karty Anki: 1680013522641
GUID: k=)%{F_x=G; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Popište Davies-Meyerovu konstrukci kompresní funkce.

### Odpověď (Back)

Davies-Meyerova konstrukce se oproti základní konstrukci liší tím, že zesiluje vlastnost jednosměrnosti přičtením vzoru:
\[H_i = f(M_i, H_{i - 1}) = E_{M_i}(H_{i - 1}) \oplus H_{i - 1}.\]

## Poznámka Anki 1680015244784

Karty Anki: 1680015244784
GUID: /Aop)ukvz; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Popište SHA-1.

### Odpověď (Back)

SHA-1 je hashovací funkce, která používá 512b bloky, produkuje 160b hash a kontext její kompresní funkce má 160 bitů. SHA-1 není považována za kryptograficky bezpečnou.

## Poznámka Anki 1680015745725

Karty Anki: 1680015745725
GUID: JrA~dQpn`R; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Popište kompresní funkci SHA-1.

### Odpověď (Back)

Kompresní funkce na vstupu obdrží 512b blok zprávy \(M_i\) a 160b kontext. Celkem provede 80 rund, ve kterých je kontext postupně upravován 32b částmi \(M_i\) (rundy 0-15) a poté slovy z nich odvozených (rundy 16-79). Navíc se na místě \(F\) (na obrázku) po 20 rundách střídají 4 různé funkce. Po skončení se k výsledku podle Davies-Meyerovy konstrukce přičte původní kontext \(H_{i - 1}\).

 [Obrázek: paste-80401505d1860266dbe0cf18644c8a7c590fa1bf.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1680016218998

Karty Anki: 1680016218999
GUID: q/H,)c`&_n; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Popište SHA-256.

### Odpověď (Back)

SHA-256 je hashovací funkce, která používá 512b bloky, generuje 256b hash (lze zkrátit na 196 nebo 128 bitů) a kontext její kompresní funkce má 256 bitů. Používá stejnou základní strukturu a operace jako SHA-1.

## Poznámka Anki 1680016539297

Karty Anki: 1680016539297
GUID: HtL@8x3Co.; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Popište kompresní funkci SHA-256.

### Odpověď (Back)

Kompresní funkce na vstupu obdrží 512b blok zprávy \(M_i\) a 256b kontext. Celkem provede 64 nebo 80 rund, ve kterých je kontext postupně upravován 32b částmi \(M_i\) (rundy 0-15) a poté slovy z nich odvozených (rundy 16-63/79). Po skončení se k výsledku podle Davies-Meyerovy konstrukce přičte původní kontext \(H_{i - 1}\).

 [Obrázek: paste-df85888ff90e8ee56dbc83424a0cbc4fc3ed510e.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1680016935861

Karty Anki: 1680016935861
GUID: qu>X]6)ugn; štítky: bi-kab::p05 bi-spol::09.

### Otázka (Front)

Jaké mají hashovací funkce využití v kryptografii?

### Odpověď (Back)

Hashovací funkce se dají využít následovně:

- kontrola integrity dat, identifikace dat a autentizace původu dat,
- ukládání a kontrola přihlašovacích hesel (ideálně s použitím solení),
- pseudonáhodné generátory,
- odvozování klíčů.

## Poznámka Anki 1680018156799

Karty Anki: 1680018156800
GUID: rn)}.*]wp; štítky: bi-ib::07 bi-kab::p05 bi-spol::09.

### Otázka (Front)

Popište hash-based message authentication code (HMAC).

### Odpověď (Back)

HMAC (hash-based message authentication code) má podobné využití jako MAC, ale namísto blokové šifry používá hashovací funkci. Uvažujme obecnou hashovací funkci \(h\) s velikostí bloku \(b\). Vstupní klíč \(k\) musíme nejprve zarovnat na \(b\) bitů, tedy

- je-li klíč moc krátký, doplníme ho bity \(\mathtt 0\) vlevo od MSB,
- je-li klíč moc dlouhý, redukujeme ho pomocí dané hashovací funkce.

Hodnotu HMAC zprávy \(m\) při klíči \(k\) potom definujeme jako

\[\text{HMAC}_k(m) = h\Big( \big(k \oplus \text{opad} \big) \| h\big((k \oplus \text{ipad}) \| m \big) \Big),\]kde

- \(\|\) označuje zřetězení,

- \(\text{opad}\) je vnější padding velikosti \(b\) (opakovaná hodnota \(\mathtt{0x5c}\)),

- \(\text{ipad}\) je vnitřní padding velikosti \(b\) (opakovaná hodnota \(\mathtt{0x36}\)).

 [Obrázek: paste-437114c5f0bcf03a93cb91ade7116f4f2d81edc5.jpg; soubor je v media/ v doprovodném ZIP]

