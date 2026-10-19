# NI-REV – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-rev/NI-REV.apkg; APKG SHA-256 9670f49b042e57cbd1c6d96f27c545d7e3e73f639dfdfaa5254dbc7ff55faa9f. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7fc653b9bed751e297f56e0ab41b46bdc555bbf2270d66a69096723b55136e70.
Původní balíčky: NI-REV
Rozsah: 20 poznámek, 20 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1730975196316

Karty Anki: 1730975196316
GUID: L,$)rAnC2+; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište disassemblování lineárním průchodem (linear sweep).

### Odpověď (Back)

Disassemblování lineárním průchodem (linear sweep) disassembluje linárně byte po bytu od začátku sekce \(\texttt{.text}\) až do jejího konce. Výhodou lineárního průchodu je rychlost a jednoduchost, nicméně v případě nejednoznačnosti toku kódu nebo promíchání kódu a dat může produkovat nesprávné výsledky.

## Poznámka Anki 1730975753417

Karty Anki: 1730975753417
GUID: sVe%rFHSQD; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište disassemblování rekurzivním průchodem (recursive traversal).

### Odpověď (Back)

Disassemblování rekurzivním průchodem (recursive traversal) disassembluje na základě sledování toku kódu. Pokud je nalezena skoková instrukce, je uložena její návratová adresa a po skončení analýzy instrukcí na cílové adrese skoku, pokračuje analýza na uložené návratové adrese. Výhodou rekurzivního průchodu je, že dokáže částečně odlišit kód a data (výjimkou jsou např. skokové tabulky). Oproti linárnímu průchodu (linear sweep) je ale pomalejší.

## Poznámka Anki 1730976686850

Karty Anki: 1730976686850
GUID: t;asvT1I+l; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište disassemblování rozšířeným lineárním průchodem (linear sweep).

### Odpověď (Back)

Disassemblování rozšířeným lineárním průchodem (linear sweep) dokáže částečně identifikovat skokové tabulky a odlišit tak kód od dat. Pokud jsou skokové tabulky umístěny v sekci \(\texttt{.text}\), pak musí mít odpovídající záznamy v relokační tabulce. Pomocí těchto záznamů lze skokové tabulky najít a označit jako data.

## Poznámka Anki 1730976911363

Karty Anki: 1730976911364
GUID: g&)+FX7N7?; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište disassemblování hybridním přístupem.

### Odpověď (Back)

Lineární průchod (linear sweep) a rekurzivní průchod (recursive traversal) mají komplementární silné a slabé stránky a lze je tak zkombinovat do hybridního přístupu a to následujícím způsobem:

- prvotní disassemblování se provede rozšířeným lineárním průchodem,
- každá nalezená funkce je ověřena pomocí rekurzivního průchodu.

## Poznámka Anki 1730977290881

Karty Anki: 1730977290881
GUID: EUole2MRxx; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište obfuskaci a transformační cíl.

### Odpověď (Back)

**Obfuskací** je v kontextu softwaru proces změny transformačního cíle tak, aby mu bylo obtížené porozumět, ale byla zachována jeho funkcionalita. Typicky cílí na zmatení disassembleru, debuggeru, dekompilátoru nebo reverzního analytika. **Transformačním cílem** je potom objekt, který má být obfuskován.

## Poznámka Anki 1730985699602

Karty Anki: 1730985699602
GUID: c^!5o,0|q(; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište obfuskační metriky a požadavky na obfuskační transformace.

### Odpověď (Back)

Obfuskace lze popsat pomocí následujících obfuskačních metrik:

- potence (potency) \(\mathcal T_{\text{pot}}\),
- odolnost (resilience) \(\mathcal T_{\text{res}}\),
- cena (cost) \(\mathcal T_{\text{cost}}\).

Po obfuskačních transformacích pak požadujeme, aby měly vysokou potenci, vysokou odolnost a nízkou cenu.

## Poznámka Anki 1730986021567

Karty Anki: 1730986021567
GUID: L0>_.hyV@v; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište obfuskační metriku potence (potency).

### Odpověď (Back)

Potence (potency) \(\mathcal T_\text{pot}\) je obfuskační metrika, která měří, jak moc transformace programu \(P\) na obfuskovaný program \(P'\) zmate reverzního analytika. Definována je následovně:
\[\mathcal T_\text{pot}(P) = \frac{E(P')}{E(P) - 1},\]kde \(E(P)\) je složitost \(P\) podle nějaké metriky (např. délka programu nebo cyklomatická složitost).

## Poznámka Anki 1730986450486

Karty Anki: 1730986450486
GUID: j;k89.fb#); štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište obfuskační metriku odolnost (resilience).

### Odpověď (Back)

Odolnost (resilience) \(\mathcal T_\text{res}\) je obfuskační metrika, která měří, jak obtížné je odstranit obfuskační transformaci deobfuskátorem. Definována je následovně:\[\mathcal T_\text{res} = \operatorname{Resilience}(\mathcal T_\text{deobfuscator effort}, \mathcal T_\text{programmer effort}),\]kde \(\mathcal T_\text{programmer effort}\) označuje čas potřebný pro vytvoření automatického deobfuskátoru snižujícího potenci (potency) \(\mathcal T_\text{pot}\) a \(T_\text{deobfuscator effort}\) vyjadřuje časovou a paměťovou složitost deobfuskátoru snižujícího potenci \(\mathcal T_\text{pot}\).

### Doplňující pole (Extra)

\(\operatorname{Resilience}\) označuje tabulku, která dvojicím hodnot \(T_\text{deobfuscator effort}\) a \(T_\text{programmer effort}\) přiřadí konkrétní ohodnocení odolnosti.

## Poznámka Anki 1731000004887

Karty Anki: 1731000004887
GUID: KR@utPdx{;; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište obfuskační metriku cena (cost).

### Odpověď (Back)

Cena (cost) \(\mathcal T_\text{cost}\) je obfuskační metrika, která měří nárůst výpočetního času (nebo jiných zdrojů) v důsledku použití obfuskační transformace. Definována je následovně:\[\mathcal T_\text{cost} (P) = \begin{cases}
\text{extrémní} & P' \text{ vyžaduje exponenciálně větší zdroje než } P,\\
\text{drahá} & P' \text{ vyžaduje polynomiálně větší zdroje než } P,\\
\text{levná} & P' \text{ vyžaduje lineárně větší zdroje než } P,\\
\text{nulová} & P' \text{ vyžaduje konstantně větší zdroje než } P.\\
\end{cases}\]

## Poznámka Anki 1731000134091

Karty Anki: 1731000134091
GUID: kbARZDi:Do; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište obfuskaci rozložení (layout obfuscation).

### Odpověď (Back)

Obfuskace rozložení (layout obfuscation) je obfuskace, která se zaměřuje na lexikální strukturu aplikace (formátování, komentáře, jména identifikátorů). Mezi transformace, které používá, patří:

- odstranění ladících informací,
- odstranení komentářů,
- přejmenování identifikátorů.

## Poznámka Anki 1731001586497

Karty Anki: 1731001586497
GUID: s1wdoHk+0_; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište obfuskaci řízení (control obfuscation).

### Odpověď (Back)

Obfuskace řízení (control obfuscation) je obfuskace, která se zaměřuje na tok kódu. Používá následující transformace:

- **transformace výpočtu **- vkládání zbytečného nebo mrtvého kódu, změny v algoritmech;

- **transformace pořadí** - náhodně mění pořadí výpočtů;
- **transformace agregace** - rozděluje související a slučuje nesouvisející výpočty.

## Poznámka Anki 1731001710263

Karty Anki: 1731001710263
GUID: GO5mv(;qIR; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište neprůhledné predikáty (opaque predicates) a neprůhledné proměnné (opaque variables).

### Odpověď (Back)

Neprůhledné predikáty (opaque predicates) a neprůhledné proměnné (opaque variables) jsou predikáty a proměnné, jejichž hodnoty nebo vlastnosti jsou známy v době obfuskování, ale při deobfuskaci je obtížné je odhadnout. Velmi často se používají při obfuskaci řízení (control obfuscation).

## Poznámka Anki 1731002088141

Karty Anki: 1731002088142
GUID: dc?VRPrg@F; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište techniky používané v transformacích výpočtu při obfuskaci řízení (control obfuscation).

### Odpověď (Back)

V transformacích výpočtu při obfuskaci řízení (control obfuscation) lze použít následující techniky:

- vkládání mrtvého nebo zbytečného kódu,
- rozšíření podmínek cyklů,
- konverze reducibilního control-flow grafu (CFG) na ireducibilní,
- odstranění knihovních volání a programovacích idiomů,
- tabulková interpretace,
- přidání zbytečných argumentů,
- paralelizace kódu.

## Poznámka Anki 1732201667039

Karty Anki: 1732201667039
GUID: Neu]:-RC71; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište konverzi reducibilního control-flow grafu (CFG) na ireducibilní.

### Odpověď (Back)

Konverze reducibilního control-flow grafu (CFG) na ireducibilní je technika používaná v transformacích výpočtu při obfuskaci řízení (control obfuscation). CFG je typicky reducibilní, pokud zdrojový kód používá strukturované konstrukty (např. \(\texttt{for}\), \(\texttt{while}\), \(\texttt{if}\)/\(\texttt{else}\)). Jakmile je v kódu použito \(\texttt{goto}\), stává se ireducibilbím, což vede na složitý dekompilovaný kód.

## Poznámka Anki 1732202453681

Karty Anki: 1732202453681
GUID: x|]0j-^UQS; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište tabulkovou interpretaci.

### Odpověď (Back)

Tabulková interpretace je technika používaná v transformacích výpočtu při obfuskaci řízení (control obfuscation). Spočívá v rozdělení programu do několika očíslovaných částí a použití smyčky, v jejíž iteracích jsou jednotlivé části spouštěny. Pro výběr spouštěných částí je vhodné použít \(\texttt{switch}\) nebo \(\texttt{goto}\).

### Doplňující pole (Extra)

Na tabulkovou interpretaci lze nahlížet jako na běh programu na virtuálním stroji. Jednotlivé části programu představují instrukce a jejich čísla operační kódy.

## Poznámka Anki 1732202853449

Karty Anki: 1732202853449
GUID: OJsXk$*Kdz; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište techniky používané v transformacích agregace při obfuskaci řízení (control obfuscation).

### Odpověď (Back)

V transformacích agregace při obfuskaci řízení (control obfuscation) lze použít následující techniky:

- inlining,
- outlining,
- interleaving,
- klonování,
- transformace smyček.

## Poznámka Anki 1732204119016

Karty Anki: 1732204119016
GUID: w0v*:FcISk; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište interleaving v kontextu obfuskace.

### Odpověď (Back)

Interleaving je technika používaná v transformacích agregace při obfuskaci řízení (control obfuscation). V případě funkcí se provádí tak, že několik funkcí je spojeno do jedné funkce s novým argumentem, pomocí kterého volající určuje větev (dílčí původní funkci), jež má být spuštěna. V případě proměnných funguje tak, že několik proměnných je spojeno do jednoho binárního bloku a pro přístup k jednotlivým částem se používají gettery a settery.

## Poznámka Anki 1732204441411

Karty Anki: 1732204441411
GUID: jk#h`ZPW-t; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište klonování v kontextu obfuskace.

### Odpověď (Back)

Klonování je technika používaná v transformacích agregace při obfuskaci řízení (control obfuscation). Spočívá v tom, že je vytvořena rodičovská třída s virtuální metodou a hierarchie z ní dědících tříd, které tuto metodu přepisují svými metodami s různými implementacemi.

## Poznámka Anki 1732204606919

Karty Anki: 1732204606919
GUID: g)J$pZIz]L; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište transformaci smyček v kontextu obfuskace.

### Odpověď (Back)

Transformace smyček je technika používaná v transformacích agregace při obfuskaci řízení (control obfuscation). Existují následující typy:

- **loop blocking** - tělo smyčky je rozděleno pro lepší využití cache;

- **loop unrolling** - tělo smyčky je replikováno několikrát po sobě, čímž jsou odstraněny skokové instrukce;

- **loop fission** - tělo smyčky je rozděleno do několika smyček, které mohou běžet paralelně.

## Poznámka Anki 1734285740197

Karty Anki: 1734285740197
GUID: F,kx;=/|:p; štítky: ni-pb::14 ni-rev::p04.

### Otázka (Front)

Popište vkládání mrtvého nebo zbytečného kódu a rozšíření podmínek cyklů.

### Odpověď (Back)

Vkládání mrtvého nebo zbytečného kódu a rozšíření podmínek cyklů jsou techniky používané v transformacích výpočtu při obfuskaci řízení (control obfuscation) založené na neprůhledných predikátech (opaque predicates). **Vkládání mrtvého nebo zbytečného kódu** spočívá ve vkládání nikdy nespuštěných větví za neprůhledné predikáty nebo přidání kódu nesouvisejícího s původní funkcionalitou. **Rozšíření podmínek cyklů** pak neprůhledné predikáty zahrnuje do ukončovacích podmínek cyklů, čímž ztěžuje jejich pochopení.

