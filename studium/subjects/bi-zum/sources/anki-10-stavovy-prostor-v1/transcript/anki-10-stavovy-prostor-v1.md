# BI-ZUM – 10 stavovy prostor

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610636

Karty Anki: 1785298610636
GUID: y%:F/y(^dG; štítky: AI_combined::10_stavovy_prostor iterace_07 src_535-542.

### Otázka (Front)

Co je stavový prostor a jak je formálně zadána úloha jeho prohledávání?

### Odpověď (Back)

Stavový prostor je orientovaný graf (S,A): uzly S jsou stavy a hrany A aplikovatelné akce. Úloha obsahuje počáteční I∈S a cíle G⊆S; hledá se dosažitelný stav z G a případně cesta I→G. Mnoho úloh lze takto modelovat oddělením konfigurací, povolených změn a cíle (navigace, hry, plánování, dokazování, výpočty, optimalizace…).

Neorientovaná hrana je neuspořádaná dvojice {u,v}; orientovaná (u,v) má směr a opačná nemusí existovat — stejně jako vratnost akcí. **Stav** je konfigurace problému, jeho **reprezentace** datový popis pro uložení, porovnání a generování následníků.

## Poznámka Anki 1785298610637

Karty Anki: 1785298610637
GUID: eK,pb_|`K!; štítky: AI_combined::10_stavovy_prostor iterace_07 src_543-550.

### Otázka (Front)

Jak se stavovým prostorem modelují navigace, posuvná skládačka, symbolická integrace a N dam?

### Odpověď (Back)

- **Navigace:** stavy města/polohy, akce přejezdy, cíl destinace.
- **Posuvná skládačka:** stav je rozmístění kamenů a mezery; hrany jsou legální přesuny. Počet konfigurací prudce roste, takže celý graf je nezvládnutelný.
- **Symbolická integrace:** stavy jsou výrazy, akce ekvivalentní úpravy, cíl výraz bez integrálu. Více cest a slepé větve vyžadují hledání.
- **N dam:** stav je částečné/úplné rozmístění, akce přidá neohrožovanou dámu, cíl má N dam. Generování jen nekolidujících tahů zabuduje omezení a zmenší prostor.

## Poznámka Anki 1785298610638

Karty Anki: 1785298610638
GUID: tE.kt-AfON; štítky: AI_combined::10_stavovy_prostor iterace_07 src_551-557.

### Otázka (Front)

Co jsou následníci a cesta a kdy hledáme celou cestu oproti samotnému cílovému stavu?

### Odpověď (Back)

s′ je **následník** s, existuje-li hrana/akce (s,s′); Γ(s)={s′∈S | (s,s′)∈A}. Orientovaná cesta je posloupnost stavů a akcí (s₁,a₁,s₂,…,aₙ₋₁,sₙ). Při známém startu a deterministickém přechodu ji lze uložit jen jako akce, protože stavy dopočítáme.

U navigace, skládačky či integrace s odůvodněním potřebujeme konkrétní postup; u N dam nebo integrace bez důkazu může být hlavním výsledkem pouze konečná konfigurace/výraz.

## Poznámka Anki 1785298610639

Karty Anki: 1785298610639
GUID: OY#=k(@QE); štítky: AI_combined::10_stavovy_prostor iterace_07 src_558-566.

### Otázka (Front)

Co je prohledávací strom, jak vzniká expanzí a proč je strategie výběru uzlu zásadní?

### Odpověď (Back)

Orientovaný kořenový strom má z kořene do každého uzlu právě jednu cestu; list nemá potomky. **Prohledávací strom** má kořen I a jeho cesty odpovídají platným cestám ve stavovém grafu. Není to celý stavový graf, ale algoritmem postupně vytvořená struktura; tentýž stav se bez detekce duplicit může objevit více cestami.

**Expanze** vygeneruje následníky vybraného otevřeného listu. Schéma: vytvoř kořen → vybírej otevřený list → testuj cíl → expanduj, dokud nenajdeš cíl nebo možnosti nedojdou. Pravidlo výběru určuje čas, paměť, úplnost i optimálnost; špatné může zabloudit, neskočit v nekonečnu nebo najít dražší cestu.

## Poznámka Anki 1785298610640

Karty Anki: 1785298610640
GUID: zIoLz8}I@t; štítky: AI_combined::10_stavovy_prostor iterace_07 src_567-572.

### Otázka (Front)

Co znamenají FRESH, OPEN a CLOSED v grafovém prohledávání?

### Odpověď (Back)

- **FRESH:** stav dosud nebyl objeven.
- **OPEN:** objevený stav čekající na výběr a expanzi.
- **CLOSED:** již expandovaný stav.
OPEN je datová struktura hranice; způsob odebrání určuje strategii. CLOSED eviduje zpracované stavy. Následník, který už je OPEN/CLOSED, se běžně znovu nepřidává, aby se omezily cykly, opakované zpracování a redundantní čas/paměť.

## Poznámka Anki 1785298610641

Karty Anki: 1785298610641
GUID: c^I4jBeE8h; štítky: AI_combined::10_stavovy_prostor iterace_07 src_573-576.

### Otázka (Front)

Jak funguje Random Search ve stavovém prostoru a jaké má vlastnosti?

### Odpověď (Back)

Náhodně vybere stav z OPEN, otestuje cíl, přidá neobjevené následníky a přesune expandovaný stav do CLOSED. Nevyužívá hloubku, cenu ani odhad cíle, takže plýtvá prací v neperspektivních oblastech.

Nezaručuje nejkratší ani nejlevnější cestu. Grafová varianta je úplná v konečném grafu s korektní evidencí OPEN/CLOSED, protože nakonec expanduje všechny dosažitelné stavy; v nekonečném prostoru obecnou úplnost nemá.

## Poznámka Anki 1785298610642

Karty Anki: 1785298610642
GUID: Ah_Vb_5./$; štítky: AI_combined::10_stavovy_prostor iterace_07 src_577-586.

### Otázka (Front)

Jak funguje BFS a jaké jsou jeho záruky a složitosti?

### Odpověď (Back)

**BFS** expanduje po vrstvách hloubky 0,1,2,… pomocí fronty **FIFO**; uzly hloubky d jsou vloženy i odebrány před d+1. Je úplný při konečném větvení a cíli v konečné hloubce.

Vrací cestu s nejméně hranami; cenově optimální je jen při stejných cenách hran, protože jinak může kratší cesta stát více. Pro faktor větvení b a nejmělčí cíl d má čas i paměť řádově O(b<sup>d</sup>); hlavním limitem je exponenciálně široká hranice.

Pseudokód: FIFO←I → odeber x → test x∈G → neobjeveným následníkům nastav předchůdce a vlož je → x do CLOSED.

## Poznámka Anki 1785298610643

Karty Anki: 1785298610643
GUID: N1avzo_l%f; štítky: AI_combined::10_stavovy_prostor iterace_07 src_587-598.

### Otázka (Front)

Jak funguje DFS a jak se liší od BFS z hlediska záruk, času a paměti?

### Odpověď (Back)

**DFS** jde co nejhlouběji a po slepé větvi se vrací; iterativně používá zásobník **LIFO**, takže čerstvý následník se expanduje hned. Na konečném grafu s detekcí návštěv je úplný; v nekonečnu nebo bez ochrany proti cyklům může uvíznout. Nezaručuje nejkratší ani nejlevnější cestu.

Pro větvení b a max. hloubku m má čas O(b<sup>m</sup>). Stromově uchovává hlavně cestu a sourozence, O(bm), proti O(b<sup>d</sup>) u BFS; grafové CLOSED však může stát O(|V|). Hodí se k inkrementální konstrukci (N dam), protože rychle zkouší úplnou konfiguraci.

BFS=nejmenší hloubka/FIFO/optimální počet hran při jednotkové ceně/vysoká paměť; DFS=největší hloubka/LIFO/bez záruky kvality/obvykle menší paměť.

## Poznámka Anki 1785298610644

Karty Anki: 1785298610644
GUID: C<LN~pSWIs; štítky: AI_combined::10_stavovy_prostor iterace_07 src_599-607.

### Otázka (Front)

Jak se rekonstruuje nalezená cesta a podle čeho se porovnávají prohledávací algoritmy?

### Odpověď (Back)

Při prvním objevení y z x se nastaví **prev[y]=x** a y se vloží do OPEN. Po nalezení cíle se sleduje prev od cíle ke startu a obrácená posloupnost se převrátí; odkazy míří od potomka k rodiči, proto vzniká pozpátku. Je-li OPEN prázdné bez cíle, úplné grafové hledání vyčerpalo všechny dosažitelné možnosti.

Porovnáváme **úplnost** (vždy najde řešení, existuje-li za předpokladů), **optimálnost** (vrátí minimum zvolených nákladů), čas, paměť a podmínky záruk. Pilíře: stavy/akce, I/G, následníci, OPEN/CLOSED, výběr uzlu, test cíle a rekonstrukce cesty.

