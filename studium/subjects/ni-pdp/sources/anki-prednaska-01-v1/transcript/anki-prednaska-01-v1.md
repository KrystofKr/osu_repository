# NI-PDP – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-pdp/NI-PDP.apkg; APKG SHA-256 b38783778a590460b03050d14b21f60017ff90d9b0abe806748521d92454df28. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: da16e1b818a2fcaa42e78195ece6396a24afd5754b63362dce0d5df6925e0f3f.
Původní balíčky: NI-PDP
Rozsah: 24 poznámek, 24 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1739806368262

Karty Anki: 1739806368262
GUID: u@1p*L|c(I; štítky: ni-pdp::p01.

### Otázka (Front)

Popište paralelní počítač.

### Odpověď (Back)

Paralelní počítač je skupina propojených výpočetních uzlů, které komunikují a spolupracují, aby rychleji vyřešily velké a výpočetně či pamětově náročné vypočetní úlohy.

## Poznámka Anki 1739807100424

Karty Anki: 1739807100424
GUID: QsSwK@^/^=; štítky: ni-pdp::p01.

### Otázka (Front)

Popište modely paralelních systémů.

### Odpověď (Back)

Modely paralelních systémů se dělí podle úrovně pohledu na:

- **modely výpočetního stroje** - HW, ISA, OS;

- **modely architektury** - toky dat či instrukcí, organizace paměti, propojovací sítě;

- **výpočetní modely** - analytické modely architektury pro navrhování a verifikaci paralelních programů (PRAM, BSP, APRAM);

- **programovací modely** - sémantika paralelních vyšších jazyků a prostředí, modely přístupu do sdílené paměti.

## Poznámka Anki 1739808794596

Karty Anki: 1739808794596
GUID: uT6jA)Qo)(; štítky: ni-pdp::p01.

### Otázka (Front)

Popište vypočetní model parallel random-access machine (PRAM).

### Odpověď (Back)

Výpočetní model parallel random-access machine (PRAM) se skládá z:

- procesorů random-access machine (RAM) \(P_1, P_2, \dots P_p\), každý z nichž má vlastní lokální paměť;
- pole sdílených paměťových buněk \(M[1], M[2], \dots, M[m]\).

Každý procesor může přistupovat do jakékoliv buňky sdílené paměti v čase \(\mathcal O(1)\) a řízení konfliktů při přístupu musí být explicitně oštřeno (EREW, CREW, CRCW). Všechny procesory synchronně provádí následující typy instrukcí:

- \(\texttt{READ}\) (\(\texttt R\)) - čtení buňky sdílené paměti,

- \(\texttt{WRITE}\) (\(\texttt W\)) - zápis buňky sdílené paměti,

- \(\texttt{LOCAL}\) (\(\texttt L\)) - lokální operace.

Jediným způsobem komunikace procesorů je čtení a zápis buněk sdílené paměti.

## Poznámka Anki 1739808962128

Karty Anki: 1739808962129
GUID: MG_WYMfP3L; štítky: ni-pdp::p01.

### Otázka (Front)

Popište typy parallel random-access machine (PRAM) výpočetního modelu.

### Odpověď (Back)

Parallel random-access machine (PRAM) výpočetní modely se dělí na dva typy:

- **jednotkový** - všechny instrukce (\(\texttt R\), \(\texttt W\) i \(\texttt L\)) trvají čas 1;
- **globální **- instrukce \(\texttt L\) trvá čas 1 a instrukce \(\texttt R\) a \(\texttt W\) trvají konstantní čas \(d > 1\).

## Poznámka Anki 1739809504072

Karty Anki: 1739809504072
GUID: mn380~*cj>; štítky: ni-pdp::p01.

### Otázka (Front)

Popište ošetření konfliktů při přístupu do sdílené paměti ve výpočetním modelu parallel random-access machine (PRAM).

### Odpověď (Back)

Ošetření konfliktů při přístupu do sdílené paměti ve výpočetním modelu parallel random-access machine (PRAM) lze implementovat následujícími metodami:

- **exclusive read exclusive write **(EREW) - procesory nesmí číst nebo zapisovat sdílenou paměťovou buňku současně;

- **concurrent read exclusive write** (CREW) - procesory nesmí zapisovat sdílenou paměťovou buňku současně, současné čtení je povoleno;

- **concurrent read concurrent write** (CRCW) - procesory smí číst i zapisovat sdílenou paměťovou buňku současně.

Metodu CRCW lze dále rozdělit na:

- **priority CRCW** - procesory mají pevné priority a dokončení zápisu je povoleno procesoru s nejvyšší prioritou;
- **arbitrary** **CRCW** - dokončení zápisu je povoleno náhodně zvolenému procesoru (algoritmus nemůže o zvoleném procesoru činit žádné předpoklady),

- **common** **CRCW** - dokončení zápisu je povoleno všem procesorům právě tehdy, když jsou všechny zapisované hodnoty stejné (algoritmus musí zajistit splnění této podmínky).

## Poznámka Anki 1739810338108

Karty Anki: 1739810338108
GUID: d9e1Cc6r<d; štítky: ni-pdp::p01.

### Otázka (Front)

Popište výpočetní model asynchronous parallel random-access machine (APRAM).

### Odpověď (Back)

Výpočetní model asynchronous parallel random-access machine (APRAM) používá stejné instukce jako model parallel random-access machine (PRAM). Liší se však v následujících rysech:

- přístup procesoru do sdílené paměti není v čase \(\mathcal O(1)\),
- explicitního ošetření konfliktů při přístupu do sdílené paměti je dosaženo pomocí bariérové synchronizace,
- procesory pracují asynchronně.

Výpočet v modelu APRAM je pak posloupnost globálních fází oddělených bariérovou synchronizací, ve kterých procesory pracují asynchronně. Bariérová synchronizace může být implementována dvojím způsobem:

- centrální čítač,
- binární redukční strom.

Navíc platí, že procesory nemohou v jedné globální fázi přistupovat ke stejné buňce sdílené paměti, pokud do ní aspoň jeden z nich zapisuje.

## Poznámka Anki 1740001529984

Karty Anki: 1740001529984
GUID: e:Cj{_bBMX; štítky: ni-pdp::p01.

### Otázka (Front)

Popište implementace bariéry pomocí centrálního čítače ve výpočetním modelu asynchronous parallel random-access machine (APRAM).

### Odpověď (Back)

Bariéra ve výpočetním modelu asynchronous parallel random-access machine (APRAM) implementovaná pomocí centrálního čítače funguje tak, že čítač je zpočátku inicializován s hodnotou 0, bariéra je nastavena do příchozí fáze a procesy k ní přistupují ve vzájemném vyloučení. Průběh synchronizace je následující:

- příchozí proces zkontroluje, zda je bariéra v příchozí fázi a inkrementuje čítač;
- je-li hodnota čítače menší než \(p\), proces se deaktivuje;
- je-li hodnota čítače rovna \(p\), proces nastaví bariéru do odchozí fáze a aktivuje ostatní procesy;
- poslední odchozí proces nastaví bariéru zpět do příchozí fáze.

Časová složitost synchronizace pomocí této metody je

\[B(p) = \Theta (dp),\]kde \(p\) je celkový počet procesů a \(d\) časová složitost globální operace \(\mathtt R\) či \(\mathtt W\).

## Poznámka Anki 1740002396952

Karty Anki: 1740002396952
GUID: zmwLviSu7S; štítky: ni-pdp::p01.

### Otázka (Front)

Popište implementace bariéry pomocí binárního redukčního stromu ve výpočetním modelu asynchronous parallel random-access machine (APRAM).

### Odpověď (Back)

Bariéra ve výpočetním modelu asynchronous parallel random-access machine (APRAM) implementovaná pomocí binárního redukčního stormu funguje tak, že jednotlivé procesy jsou chápány jako listy binárního redukčního stromu. Průběh synchronizace je následující:

- příchozí proces zkontroluje, zda je bariéra v příchozí fázi, a pošle signál do rodičovského vrcholu;
- jakmile rodičovksý vrchol obdrží signál z obou svých podstromů, pošle signál svému rodičovskému vrcholu;
- jakmile signály doputují do kořene, je bariéra přepnuta do odchozí fáze a směrem z kořene do listů je šířen aktivační signál.

Časová složitost synchronizace pomocí této metody je

\[B(p) = \Theta(d \log p)\]kde \(p\) je celkový počet procesů a \(d\) časová složitost globální operace \(\mathtt R\) či \(\mathtt W\).

## Poznámka Anki 1740067779389

Karty Anki: 1740067779389
GUID: n?Y(cvmNlE; štítky: ni-pdp::p01.

### Otázka (Front)

Popište programovací model datový (iterační) paralelismus.

### Odpověď (Back)

Datový (iterační) paralelismus je programovací model paralelních systémů. Spočívá ve vytvoření smyčky, jejíž iterace jsou prováděny paralelně jednotlivými procesory tak, jak jsou naplánovány (scheduled). Předpokladem je datová nezávislost jednotlivých iterací, která může být zajištěna:

- překladačem (implicitně),
- programátorem (explicitně).

## Poznámka Anki 1740068236063

Karty Anki: 1740068236063
GUID: x@OlF)&&a<; štítky: ni-pdp::p01.

### Otázka (Front)

Popište programovací model funkční paralelismus (task parallelism).

### Odpověď (Back)

Funkční paralelismus (task parallelism) je programovací model paralelních systémů. Spočívá v tom, že program je rozdělen na nezávislé části, zvané úlohy (tasks), které mohou být prováděny paralelně jednotlivými procesory. Úlohy jsou podle jejich vzájemných datových závislostí organizovány do grafu úloh, který určuje jejich plánování. Funkční paralelismus typicky využívá task pool, ze kterého nevyužité procesory úlohy postupně odebírají.

## Poznámka Anki 1740069125494

Karty Anki: 1740069125494
GUID: i#7S;`*bW6; štítky: ni-pdp::p01.

### Otázka (Front)

Definujte paralelní čas.

### Odpověď (Back)

Paralelní čas \(T(n, p)\) je čas, který uplynul od začátku paralelního výpočtu do okamžiku, kdy poslední procesor skončil výpočet. Závisí na:

- **velikosti instance **\(n\),
- **počtu procesorů** \(p\) - je ovlivněn architekturou paralelního počítače.

Jeho měření probíhá čítáním:

- **výpočetních kroků** - aritmeticko-logické a paměťové operace,

- **komunikačních kroků** - přenos dat mezi procesory.

### Doplňující pole (Extra)

Podle kontextu může parameter \(p\) znamenat také počet jader, procesů, vláken atd.

## Poznámka Anki 1740228293143

Karty Anki: 1740228293143
GUID: lBBrs+:No6; štítky: ni-pdp::p01.

### Otázka (Front)

Popište programovací model paralelních programovacích šablon.

### Odpověď (Back)

Praralelní programovací šablony jsou programovací model paralelních systémů. Patří mezi ně:

- **pipelining** - vlákna se podílí na postupném zpracování;

- **fork-join** - počáteční vlákno začne provádět program sekvenčně a vytváří tým paralelních vláken;

- **single program multiple data** (SPMD) - všechna vlákna provádí asynchronně stejný kód, který je větven podle jejich identifikátorů;

- **master-slave** - master přiděluje práci, slave ji vykonává a vrací výsledky;

- **client-server** - client požaduje práci, server ji vykonává a vrací výsledky;

- **producent-konzument** - producentská vlákna přidávají práci do fronty, konzumentská vláka ji vykonávají a vrací výsledky.

## Poznámka Anki 1740229351543

Karty Anki: 1740229351543
GUID: L+_sSAIY79; štítky: ni-pdp::p01.

### Otázka (Front)

Definujte paralelní cenu, vyslovte a dokažte lemma o jejím vztahu s horní mezí časové složitosti.

### Odpověď (Back)

Paralelní cena je definována pomocí paralelního času:\[C(n, p) = p \cdot T(n, p).\]Navíc platí, že nikdy nemůže být nižší než horní mez časové složitosti \(SU^K(n)\), tedy\[C(n, p) = \Omega \big ( SU^K(n) \big ).\]
**Důkaz** 
Důkaz provedeme sporem. Předpokládejme\[C(n, p) = p \cdot T(n, p) = \mathcal o \big( SU^K(n) \big ).\]Pokud však budeme simulovat sekvenční běh takového algoritmu na jednom procesoru (pro \(p = 1\)), dostaneme lepší sekvenční složitost než \(SU^K(n)\), což je ve sporu s její definicí.

## Poznámka Anki 1740229606980

Karty Anki: 1740229606980
GUID: ib.(H8b!!M; štítky: ni-pdp::p01.

### Otázka (Front)

Definujte cenově optimální paralelní algoritmus.

### Odpověď (Back)

Paralelní algoritmus je cenově optimální, pokud\[C(n, p) = \mathcal O \big( SU^K(n) \big).\]Z lemmatu o vztahu paralelní ceny s horní mezí časové složitosti plyne, že tato podmínka je ekvivalentní s\[C(n, p) = \Theta \big( SU^K(n) \big).\]

## Poznámka Anki 1740230224295

Karty Anki: 1740230224295
GUID: i)o&&5o@mr; štítky: ni-pdp::p01.

### Otázka (Front)

Definujte paralelní zrychlení, vyslovte a dokažte lemma o jeho vztahu s počtem procesorů.

### Odpověď (Back)

Paralelní zrychlení je definováno pomocí paralelního času:\[S(n, p) = \frac{SU^K(n)}{T(n, p)}.\]Navíc platí, že nikdy nemůže být vyšší než počet procesorů, tedy\[S(n, p) = \mathcal O(p).\]
**Důkaz** 
Důkaz provedeme sporem. Předpokládejme\[S(n, p) = \frac{SU^K(n)}{T(n, p)} = \omega (p),\]vynásobme \(T(n, p)\) a získáme\[SU^K(n) = \omega \big( p \cdot T(n, p) \big) = \omega \big( C(n, p) \big)\]neboli\[C(n, p) = \mathcal o \big( SU^K(n) \big),\]což je spor s lemmatem o vztahu paralelní ceny a horní mezí časové složitosti.

## Poznámka Anki 1740230413933

Karty Anki: 1740230413933
GUID: gg8irD#m*<; štítky: ni-pdp::p01.

### Otázka (Front)

Definujte lineární paralelní zrychlení.

### Odpověď (Back)

Paralelní zrychlení je lineární s počtem procesorů právě tehdy, když\[S(n, p) = \Omega(p).\]Z lemmatu o vztahu paralelního zrychlení s počtem procesorů plyne, že tato podmínka je ekvivalentní s\[S(n, p) = \Theta (p).\]

## Poznámka Anki 1740231444198

Karty Anki: 1740231444198
GUID: Lq6m|Iy_Eq; štítky: ni-pdp::p01.

### Otázka (Front)

Definujte paralelní efektivnost.

### Odpověď (Back)

Paralelní efektivnost je definována pomocí paralelní ceny:\[E(n, p) = \frac{SU^K(n)}{C(n, p)}\]a platí \(E(n, p) \leq 1\). Alternativně lze paralelní efektivnost chápat jako paralelní zrychlení ku počtu procesorů, protože\[E(n, p) = \frac{SU^K(n)}{C(n, p)} =  \frac{S(n, p) \cdot T(n, p)}{p \cdot T(n , p)} = \frac{S(n, p)}{p}.\]

## Poznámka Anki 1740231638146

Karty Anki: 1740231638146
GUID: AWz$DWsKwx; štítky: ni-pdp::p01.

### Otázka (Front)

Definujte konstantní efektivnost.

### Odpověď (Back)

Paralelní algoritmus má konstantní efektivnost, jestliže existuje \(\varepsilon \in (0, 1)\) takové, že\[E(n, p) \geq \varepsilon\]pro všechna \(n\) a \(p\). Tato podmínka je ekvivalentní s\[E(n, p) = \Omega (1).\]

## Poznámka Anki 1740231730734

Karty Anki: 1740231730734
GUID: Pdndnk]0:r; štítky: ni-pdp::p01.

### Otázka (Front)

Vyslovte větu o paralelní optimalitě výkonnosti.

### Odpověď (Back)

Následující tvrzení o paralelním algoritmu jsou ekvivalentní:

- algoritmus je cenově optimální,
- algoritmus má lineární zrychlení,
- algoritmus má konstantní efektivnost.

## Poznámka Anki 1740231902882

Karty Anki: 1740231902882
GUID: JNfDi~Zu9z; štítky: ni-pdp::p01.

### Otázka (Front)

Definujte paralelní škálovatelnost.

### Odpověď (Back)

Paralelní algoritmus je paralelně škálovatelný, jestliže je schopen udržet stejnou hodnotu paralelní efektivnosti \(E(n, p)\) pro měnící se velikost instance \(n\) a počet procesorů \(p\). Rozlišujeme:

- **silnou škálovatelnost** (Amdahlův zákon) - rychlost poklesu paralelní efektivnosti pro konstantní \(n\) a rostoucí \(p\),

- **slabou škálovatelnost** (Gustafsonův zákon) - rychlost růstu \(n\) takového, že při rostoucím \(p\) zůstává paralelní efektivnost stejná.

## Poznámka Anki 1740232733396

Karty Anki: 1740232733396
GUID: sM(7NlB9cW; štítky: ni-pdp::p01.

Metadata původního zdroje pro kartu 1740232733396: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište Amdahlův zákon.

### Odpověď (Back)

Amdahlův zákon předpokládá, že řešená instance má konstantní velikost \(n\) a jediným parametrem je počet procesorů \(p\). Každý program se pak skládá z:

- **sekvenční části** (\(f_s\)) - může být prováděna pouze jedním vláknem a \(f_s \in (0, 1)\),

- **paralelizovatelné části** (\(1 - f_s\)) - může být prováděna více vlákny paralelně.

Pak podle Amdahlova zákona platí následující vztah pro paralelní zrychlení:\[S(n, p) = \frac{f_s + (1 - f_s)}{f_s + \frac{1 - f_s}{p}} = \frac{1}{f_s + \frac{1 - f_s}{p}},\]přičemž \(S(n, p) \leq \frac 1 {f_s}.\) Při konstantní velikosti instance nemá po jisté hranici zvyšování \(p\) smysl, protože pro přidané procesory nezbývá dostatek paralelní práce.

## Poznámka Anki 1740234526372

Karty Anki: 1740234526372
GUID: LJbPoZao]3; štítky: ni-pdp::p01.

### Otázka (Front)

Popište Gustafsonův zákon.

### Odpověď (Back)

Gustafsonův zákon relaxuje podmínku na konstantní velikost řešené instance definovanou Amdahlovým zákonem. Podle něj má být s rostoucím počtem procesorů \(p\) navyšována i velikost instance \(n\). Pak:

- **sekvenční část** trvá vždy konstantní čas \(t_\text{seq}\),

- **paralelní část** škáluje lineárně s \(p\) a trvá čas \(t_\text{par}(n, p)\).

Podle Gustafsonova zákona platí následující vztah pro paralelní zrychlení:

\[S(n, p) = \frac{t_\text{seq} + t_\text{par}(n, 1)}{t_\text{seq} + t_\text{seq}(n, p)}.\]Pokud je paralelní část pefektně parelelizovatelná, tedy\[t_\text{par}(n, p) = \frac{SU^K(n) - t_\text{seq}}{p},\]dostaneme\[S(n, p) = \frac{t_\text{seq} + SU^K(n) - t_\text{seq}}{t_\text{seq} + \frac{SU^K(n) - t_\text{seq}}{p}}\]a platí\[\displaystyle \lim_{n \to \infty} S(n, p) = p.\]

## Poznámka Anki 1740262716637

Karty Anki: 1740262716637
GUID: uo_VDKmdxD; štítky: ni-pdp::p01.

### Otázka (Front)

Definujte izoefektivní funkce.

### Odpověď (Back)

Mějme \(\varepsilon \in (0, 1)\). Izoefektivní funkce \(\psi_1\), kde\[n = \psi_1(p),\]pro zadaný počet procesorů \(p\) udává minimální velikost instance \(n\), při které je paralelní efektivita \(E(n, p)\) alespoň \(\varepsilon\). Formálně se jedná o asymptoticky minimální funkci takovou, že\[\forall n_p = \Omega \big( \psi_1(p) \big) : E(n_p, p) \geq \varepsilon\]a stojí tak na Gustafsonově zákonu. Izoefektivní funkce \(\psi_2\), kde\[p = \psi_2(n),\]pro zadanou velikost instance \(n\) udává maximální počet procesorů \(p\), při kterém je paralelní efektivita \(E(n, p)\) alespoň \(\varepsilon\). Formálně se jedná o asymptoticky maximální funkci takovou, že\[\forall p_n = \mathcal O \big( \psi_2(n) \big) : E(n, p_n) \geq \varepsilon\]a stojí tak na Amdahlově zákonu.

## Poznámka Anki 1740332074633

Karty Anki: 1740332074633
GUID: H=QczA+/^y; štítky: ni-pdp::p01.

### Otázka (Front)

Definujte horní mez časové složitosti řešení problému.

### Odpověď (Back)

Horní mez časové složitosti řešení problému \(K\) je nejhorší časová složitost nejlepšího existujícího sekvenčního algoritmu pro \(K\) a značí se \(SU^K(n)\).

