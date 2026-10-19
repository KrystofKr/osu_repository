# BI-AG1 – Přednáška 12

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 18 poznámek, 18 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1670228625694

Karty Anki: 1670228625694
GUID: i(P.v^O]0n; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Definujte vzdálenost dvou vrcholů v ohodnoceném orientovaném grafu.

### Odpověď (Back)

Pro libovolné dva vrcholy \(u\) a \(v\) ohodnoceného orientovaného grafu, vzdálenost \(d(u, v)\) je minimum z délek všech \(uv\)-cest (cest z \(u\) do \(v\)), případně \(+\infty\), pokud žádná \(uv\)-cesta neexistuje.

## Poznámka Anki 1670228660123

Karty Anki: 1670228660123
GUID: HChJ6{l4k[; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Definujte nejkratší cestu.

### Odpověď (Back)

Nejkratší \(uv\)-cesta je libovolná \(uv\)-cesta, jejíž délka je rovná vzdálenosti \(d(u, v)\).

## Poznámka Anki 1670229625964

Karty Anki: 1670229625964
GUID: g#b~W;-,Mg; štítky: bi-ag1::p12.

### Otázka (Front)

Jak těžký je problém nalezení délky nejkratší cesty mezi dvěma vrcholy pro graf ohodnocený obecnými (tedy i zápornými) délkami?

### Odpověď (Back)

Jde o NP-úplný problém.

## Poznámka Anki 1670230668165

Karty Anki: 1670230668165
GUID: w=lqxl(3}A; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Definujte relaxaci vrcholu v D.A.

### Odpověď (Back)

Přepočítání ohodnocení \(h(w)\) následníka \(w\) vrcholu \(v\) v D.A. budeme nazývat relaxace následníka \(w\) vrcholu \(v\).

## Poznámka Anki 1670231011335

Karty Anki: 1670231011335
GUID: euuW0}1|mS; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o konečnosti a správnosti D.A.

### Odpověď (Back)

D.A. na grafu s kladnými délkami hran se v konečném čase zastaví a po jeho skončení budou všechny dosažitelné vrcholy \(v\) uzavřeny s \(h(v) = d(v_0, v)\).

**Důkaz
**Dokážeme následující 4 vlastnosti D.A.:

1. Ohodnocení \(h(v)\) v průběhu D.A. nikdy neroste a je-li konečné, rovná se délce nejkratší dosud nalezené \(v_0v\)-cesty zachycené inverzí posloupnosti \(v\), \(P(v)\), \(P(P(v)), \dots, v_0\).
2. D.A. postupně otevírá všechny vrcholy dosažitelné z \(v_0\) a jakmile je otevřený vrchol uzavřen, nemůže být znovu otevřen.
3. D.A. se v konečném čase zastaví.
4. D.A. uzavírá všechny dosažitelné vrcholy v pořadí jejich neklesající vzdálenosti od \(v_0\) a po skončení je \(h(v) = d(v_0, v)\).

## Poznámka Anki 1670231170699

Karty Anki: 1670231170699
GUID: xOi}T2ruq(; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte první vlastnost D.A.

### Odpověď (Back)

Ohodnocení \(h(v)\) v průběhu D.A. nikdy neroste a je-li konečné, rovná se délce nejkratší dosud nalezené \(v_0v\)-cesty zachycené inverzí posloupnosti \(v\), \(P(v)\), \(P(P(v)), \dots, v_0\).

**Důkaz**

- Indukcí podle doby běhu D.A.
- Na počátku výpočtu tvrzení platí pro \(v_0\), neboť \(h(v_0) = 0\).
- Kdykoliv D.A. relaxuje vrchol \(w\), snižuje jeho \(h(w)\) a \(w\) je následníkem otevřeného vrcholu \(v\), jehož \(h(v)\) je konečné.
- Podle indukčního předpokladu je \(h(v)\) rovno délce nejkratší dosud nalezené \(v_0v\)-cesty.
- Relaxace \(w\) znamená nalezení \(v_0w\)-cesty přidáním hrany \((v, w)\) délky \(l(v, w)\) k této cestě, jejíž délka \(h(v) + l((v, w))\) je menší než délka předchozí nejkratší cesty a to je přesně to konečné číslo, na které se sníží \(h(w)\).
- Při každé relaxaci si D.A. v poli \(P\) pamatuje předchůdce, který relaxaci způsobil a který poskytl kratší cestu.

## Poznámka Anki 1670231357336

Karty Anki: 1670231357336
GUID: n5w=|K1,qf; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte druhou vlastnost D.A.

### Odpověď (Back)

D.A. postupně otevírá všechny vrcholy dosažitelné z \(v_0\) a jakmile je otevřený vrchol uzavřen, nemůže být znovu otevřen.

**Důkaz**

- Prvním otevřeným a následně uzavřeným vrcholem je \(v_0\).
- Vrchol je poprvé otevřen, právě když je do té doby nenalezeným následníkem dříve otevřeného vrcholu a tudíž je dosažitelný z \(v_0\).
- Protože D.A. na začátku hlavního cyklu vybere otevřený vrchol \(v\) s nejmenším \(h(v)\), mají všechny ostatní otevřené vrcholy \(o\) hodnotu \(h(o) \geq h(v)\) a to včetně následníků \(w\) vrcholu \(v\) po jejich případné relaxaci, protože \(l((v, w)) > 0\).
- Protože D.A. potom takový vrchol uzavře, nemůže být už nikdy otevřen, neboť není možné, že bychom do něj našli kratší cestu.

## Poznámka Anki 1670231427165

Karty Anki: 1670231427166
GUID: M41MSfVUSF; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte třetí vlastnost D.A.

### Odpověď (Back)

D.A. se v konečném čase zastaví.

**Důkaz**

- Dle Vlastnosti 2 se otvírají právě a jenom dosažitelné vrcholy.
- Dále pokud se otevřený vrchol uzavře, již se nikdy znovu neotevře.
- D.A. v každé iteraci hlavního cyklu uzavře jeden vrchol.
- Počet iterací cyklu D.A. je tedy \(\mathcal O(|V|)\) a počet relaxovaných následníků v každé iteraci je také konečný.

## Poznámka Anki 1670231544886

Karty Anki: 1670231544886
GUID: dFNp(GOyy~; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte čtvrtou vlastnost D.A.

### Odpověď (Back)

D.A. uzavírá všechny dosažitelné vrcholy v pořadí jejich neklesající vzdálenosti od \(v_0\) a po skončení je \(h(v) = d(v_0, v)\).

**Důkaz**

- V každém kroku uzavře D.A. otevřený vrchol v s nejmenší \(h(v)\) a hodnoty \(h(v)\) uzavíraných vrcholů tedy tvoří neklesající posloupnost.
- Protože zavřený vrchol dle Vlastnosti 2 nemůže být znovu otevřen, má jeho \(h(v)\) na konci stále tuto hodnotu.
- Ta dle Vlastnosti 1 byla délkou nejkratší \(v_0v\)-cesty v době uzavření vrcholu \(v\).
- Kratší \(v_0v\)-cesta tedy v grafu neexistuje a proto \(h(v) = d(v_0, v)\).

## Poznámka Anki 1670231641139

Karty Anki: 1670231641139
GUID: JOAGrDyF.?; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o časové složitosti D.A.

### Odpověď (Back)

Pokud jsou délky hran kladné, potom D.A. nad souvislým grafem o \(n\) vrcholech běží v čase \(\mathcal O(n^2)\).

**Důkaz**

- Inicializace trvá \(\mathcal O(n)\).
- Každý vrchol uzavřeme nejvýše jednou.
- Vnějším cyklem projdeme nejvýše \(n\)-krát.
- Pokaždé hledáme minimum až z \(n\) ohodnocení vrcholů a procházíme až \(n\) následníků.

## Poznámka Anki 1670231946366

Karty Anki: 1670231946366
GUID: sd7k1&G]mL; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o časové složitosti D.A. s binární haldou.

### Odpověď (Back)

Časová složitost \(\mathtt{DijkstraHalda}\) je \(\mathcal O(|E| \log |V|)\).

**Důkaz**

- Inicializace a \(\mathtt{HeapBuild}\) trvají \(O(|V|)\).
- Celková složitost vyjímání vrcholů z haldy (\(\mathtt{HeapExtractMin}\)) je \(\mathcal O(|V | \log |V|)\).
- Celková složitost potenciálních relaxací je \(\mathcal O(|E| \log |V|)\), neboť počet volání operace \(\mathtt{HeapChangeKey}\) je nejvýše \(|E|\).

## Poznámka Anki 1670233160563

Karty Anki: 1670233160563
GUID: G;{rR/VMdd; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Definujte fáze výpočtu Bellman-Fordova algoritmu (\(\texttt{Bellman-Ford}\)).

### Odpověď (Back)

Definujeme fáze výpočtu následovně:

- Nechť \(A_0 = \set{v_0}\).
- Fáze \(F_0\) = otevření počátečního vrcholu \(v_0\), čili všech prvků množiny \(A_0 = \set{v_0}\).
- \(A_i\) je množina vrcholů, které byly relaxovány jako následníci vrcholů z množiny \(A_{i-1}\).
- Vytvoření množiny vrcholů \(A_i\) se nazývá fáze \(F_i\).

## Poznámka Anki 1670233505715

Karty Anki: 1670233505715
GUID: g-HEU|5ZVi; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte první vlastnost Bellman-Fordova algoritmu (\(\texttt{Bellman-Ford}\)).

### Odpověď (Back)

Pro každý nalezený vrchol \(v\) platí na konci fáze \(F_i\), že \(h(v) \leq l(S)\), kde \(S\) je nejkratší \(v_0v\)-sled o nejvýše \(i\) hranách.

**Důkaz**

- Tvrzení dokážeme indukcí podle \(i\).
- Pro \(i = 0\) tvrzení platí: jediný vrchol dosažitelný z \(v_0\) sledem s \(0\) hranami je \(v_0\) sám; \(h(v_0) = 0\) a pro ostatní vrcholy v je \(h(v) = +\infty\).
- Dále nechť \(i > 0\).
- Zvolme nějaký nalezený vrchol \(v\) na konci fáze \(F_i\).
- Označme \(S\) nejkratší \(v_0v\)-sled o nejvýše \(i\) hranách.
- Dále označme \(e(S)\) počet hran v sledu \(S\).
- Pokud \(e(S) < i\), platilo \(h(v) \leq l(S)\) už na konci předchozí fáze \(F_{i-1}\) a jelikož ohodnocení vrcholů nerostou, platí nadále.

- Pokud \(e(S) = i\), označme \(uv\) jeho poslední hranu a \(S'\) podsled z \(v_0\) do \(u\).

- Na konci fáze \(F_{i-1}\) je z indukce \(h(u) \leq l(S')\).

- Na tuto hodnotu muselo být \(h(u)\) nastaveno nejpozději ve fázi \(F_{i-1}\), čímž byl vrchol \(u\) otevřen.

- Nejpozději ve fázi \(F_i\) proto museli být relaxováni jeho následníci a \(u\) musel být uzavřen.

- Na začátku relaxace muselo stále platit \(h(u) \leq l(S')\), hodnota \(h(u)\) se sice mohla změnit, ale ne zvýšit.

- Po relaxaci tedy muselo platit \(h(v) \leq h(u) + l((u, v)) \leq l(S') + l((u, v)) = l(S)\).

## Poznámka Anki 1670233978838

Karty Anki: 1670233978838
GUID: wjMd?`Ra1p; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o konečnosti Bellman-Fordova algoritmu (\(\texttt{Bellman-Ford}\)).

### Odpověď (Back)

Nechť \(G = (V, E)\) a \(n = |V|\). Pokud \(G\) neobsahuje záporné cykly, po fázi \(F_n\) se B.F.A. zastaví.

**Důkaz
**Důsledkem Vlastnosti 1 B.F.A. je, že po fázi \(F_{n-1}\) jsou ohodnocení všech vrcholů shora omezena délkami nejkratších cest, a protože nejkratší cesty mají nejvýše \(n - 1\) hran, tak se ve fázi \(F_n\) už nemohou změnit, tedy algoritmus už žádný vrchol neotevře a zastaví se.

## Poznámka Anki 1670235682278

Karty Anki: 1670235682278
GUID: db&=~(.0Zu; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte větu o složitosti Bellman-Fordova algoritmu (\(\texttt{Bellman-Ford}\)).

### Odpověď (Back)

V grafu bez záporných cyklů nalezne B.F.A. všechny vzdálenosti z vrcholu \(v_0\) v čase \(\mathcal O(|V | \cdot |E|)\).

**Důkaz**

- Podle věty o konečnosti B.F.A. (která je důsledkem Vlastnosti 1) se po \(|V|\) fázích algoritmus zastaví a podle Vlastnosti 2 o dosažitelnosti vrcholů a Vlastnosti 3 o významu \(h(v)\) na konci relaxačního algoritmu vydá správný výsledek.
- Během jedné fáze přitom relaxuje každý vrchol své následníky nejvýše jednou, takže celá fáze dohromady trvá \(\mathcal O(|E|)\).

## Poznámka Anki 1670236180473

Karty Anki: 1670236180474
GUID: OJaqBEk[y;; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte druhou vlastnost algoritmu \(\mathtt{Relaxace}\).

### Odpověď (Back)

Pokud se výpočet zastaví, uzavřené jsou právě vrcholy dosažitelné z \(v_0\).

**Důkaz**

- Podobné důkazu Vlastnosti 2 \(\mathtt{BFS}\) s rozdílem, že uzavřený vrchol je možné znovu otevřít.
- Prvním otevřeným a následně uzavřeným vrcholem je \(v_0\).
- Vrchol je otevřen, právě když je relaxovaným následníkem otevřeného vrcholu. Každý otevřený vrchol je tak dosažitelný z \(v_0\).
- Vrchol je uzavřen, právě když byl před tím otevřený a zrelaxoval všechny své následníky, a proto je dosažitelný z \(v_0\).
- Vrchol, který není dosažitelný z \(v_0\), nemůže být ani otevřen a tedy ani uzavřen.

## Poznámka Anki 1670236684888

Karty Anki: 1670236684888
GUID: m<+1@%VO`1; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Vyslovte a dokažte třetí vlastnost algoritmu \(\mathtt{Relaxace}\).

### Odpověď (Back)

Pokud se výpočet zastaví, \(h(v)\) uzavřeného vrcholu je rovno vzdálenosti \(d(v_0, v)\).

**Důkaz**

- Podobné důkazu Vlastnosti 3 \(\mathtt{BFS}\).
- Vrchol \(v\) označíme za „špatný“, pokud \(h(v) \neq d(v_0, v)\).
- Jelikož \(h(v)\) odpovídá délce nějakého \(v_0v\)-sledu, musí být \(h(v) > d(v_0, v)\).
- Pro spor předpokládejme, že existují nějaké „špatné“ vrcholy.
- Ze všech „špatných“ vrcholů vybereme v ten, který má z nich nejkratší \(v_0v\)-cestu \(P\) (a tedy \(h(v) > d(v_0, v)\)).
- Nechť \(p\) je předchůdce vrcholu \(v\) na \(P\) (musí existovat, neboť \(v_0\) není špatný).
- Vrchol \(p\) nemůže být špatný z definice \(v\), protože část \(P\) z \(v_0\) do \(p\) je nejkratší \(v_0p\)-cestou. Tedy \(h(p) = d(v_0, p)\).
- Poté, co \(p\) získal toto ohodnocení, byl otevřen a později musel relaxovat své následníky, mimo jiné \(v\), a pak byl zavřen.
- Protože \(p\) je předchůdce \(v\) na nejkratší \(v_0v\)-cestě \(P\), platí po uzavření \(p\): \(h(v) \leq h(p) + l((p, v)) = d(v_0, p) + l((p, v)) = d(v_0, v)\).
- Jelikož ohodnocení vrcholů nikdy nerostou, došlo ke sporu s předpokladem, že po zastavení algoritmu platí \(h(v) > d(v_0, v)\).

## Poznámka Anki 1716565110798

Karty Anki: 1716565110798
GUID: M[$ERp>qgV; štítky: bi-ag1::p12 bi-spol::03.

### Otázka (Front)

Popište vlastnosti Bellman-Fordova algoritmu (\(\texttt{Bellman-Ford}\)).

### Odpověď (Back)

Bellman-Fordův algoritmus (\(\texttt{Bellman-Ford}\)) má následující vlastnosti:

- Pro každý nalezený vrchol \(v\) platí na konci fáze \(F_i\), že \(h(v) \leq l(S)\), kde \(S\) je nejkratší \(v_0v\)-sled o nejvýše \(i\) hranách.

- Ohodnocení \(h(v)\) v průběhu B.F.A. nikdy neroste a je-li konečné, rovná se délce **nějakého **\(v_0v\)-**sledu **zachyceného inverzí posloupnosti \(v\), \(P(v)\), \(P(P(v)), \dots, v_0\).
- B.F.A. se v konečném čase zastaví.

