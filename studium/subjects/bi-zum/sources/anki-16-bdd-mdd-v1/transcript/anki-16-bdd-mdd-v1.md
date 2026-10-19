# BI-ZUM – 16 BDD MDD

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610674

Karty Anki: 1785298610674
GUID: hV8O=$p}`); štítky: AI_combined::16_BDD_MDD iterace_11 src_805-810.

### Otázka (Front)

Jak výrokovou formuli reprezentuje uspořádaný binární rozhodovací strom BDT a proč je neefektivní?

### Odpověď (Back)

Formule nad n proměnnými určuje booleovskou funkci B:{0,1}<sup>n</sup>→{0,1}. Kanonická reprezentace je žádoucí, protože syntakticky různé formule mohou určovat stejnou funkci a ekvivalenci pak lze ověřit strukturálním porovnáním.

**Uspořádaný BDT** je úplný binární strom s pevným pořadím proměnných; každá úroveň testuje jednu proměnnou, low/levá hrana odpovídá 0, high/pravá 1 a list nese hodnotu funkce pro dané ohodnocení. Má 2<sup>n</sup> listů a opakuje identické podproblémy, takže je prostorově exponenciální i pro jednoduše strukturované funkce.

## Poznámka Anki 1785298610675

Karty Anki: 1785298610675
GUID: PHL<L`B`Bz; štítky: AI_combined::16_BDD_MDD iterace_11 src_811-816.

### Otázka (Front)

Jak se z BDT vytvoří ROBDD a proč je při pevném pořadí kanonický?

### Odpověď (Back)

Redukce opakovaně používá tři pravidla:
1. všechny listy 0 sloučit do terminálu 0 a všechny listy 1 do terminálu 1;
2. sloučit izomorfní uzly se stejnou proměnnou i totožnými low a high následníky;
3. odstranit uzel s low=high, protože jeho proměnná výsledek neovlivňuje.

Výsledkem je **ROBDD** (Reduced Ordered BDD). Pro danou funkci a pevné globální pořadí proměnných je jedinečný až na přejmenování uzlů. Dvě formule jsou proto ekvivalentní právě tehdy, když jejich ROBDD se stejným pořadím mají stejný kořenový diagram.

## Poznámka Anki 1785298610676

Karty Anki: 1785298610676
GUID: oc4E_,$Rm_; štítky: AI_combined::16_BDD_MDD iterace_11 src_817-823.

### Otázka (Front)

Jak se čtou cesty v BDD a jak souvisejí restrikce a Shannonův rozvoj?

### Odpověď (Back)

Vnitřní uzel v má var(v), low(v) pro 0 a high(v) pro 1. Cesta z kořene k terminálu 1 je částečné přiřazení, jehož všechny konzistentní úplné doplňky formuli splňují; cesta k 0 je všechny falzifikuje. Formule je splnitelná, je-li 1 dosažitelná, a validní, redukuje-li se celý diagram na terminál 1.

**Restrikce** B<sub>φ</sub>|<sub>x=0/1</sub> vznikne dosazením hodnoty x; v BDD se každý uzel x obejde přesměrováním na low/high následníka a výsledek se zredukuje. **Shannonův rozvoj:** B<sub>φ</sub>=(¬x∧B<sub>φ</sub>|<sub>x=0</sub>)∨(x∧B<sub>φ</sub>|<sub>x=1</sub>).

## Poznámka Anki 1785298610677

Karty Anki: 1785298610677
GUID: O<A1qft:@e; štítky: AI_combined::16_BDD_MDD iterace_11 src_824-831.

### Otázka (Front)

Jak funguje operace APPLY nad BDD a proč záleží na pořadí proměnných?

### Odpověď (Back)

**APPLY** z BDD funkcí B<sub>φ</sub>, B<sub>ψ</sub> vytvoří BDD pro B<sub>φ</sub>◦B<sub>ψ</sub> (např. ∧, ∨, ⇒). Jsou-li oba uzly terminály, aplikuje spojku na jejich hodnoty. Testují-li stejnou proměnnou, rekurzivně spojí dvojice low a high následníků. Testují-li různé, rozvine proměnnou dřívější v globálním pořadí a druhý uzel v obou větvích ponechá. Memoizace zpracuje každý pár uzlů nejvýše jednou: O(|B<sub>φ</sub>|·|B<sub>ψ</sub>|) času i prostoru.

Pořadí určuje sdílení podproblémů: tatáž funkce může mít lineární nebo exponenciální BDD. Optimální pořadí je NP-těžké hledat, proto se používají heuristiky a dynamické přeuspořádávání. Ordered BDD zachovává na všech cestách jedno globální pořadí; obecný BDD může mít v různých větvích pořadí odlišné.

## Poznámka Anki 1785298610678

Karty Anki: 1785298610678
GUID: Q>D9Ich)Ys; štítky: AI_combined::16_BDD_MDD iterace_11 src_832-838.

### Otázka (Front)

Co je MDD a jaké jsou výhody a omezení BDD/MDD jako symbolických reprezentací?

### Odpověď (Back)

**MDD** zobecňuje BDD na proměnné s konečnou vícehodnotovou doménou D: uzel má větev pro každou hodnotu. Pro G:D<sup>n</sup>→{False,True} reprezentuje množinu G<sub>True</sub>⊆D<sup>n</sup>. Průnik a sjednocení reprezentovaných množin lze provést logickou konjunkcí/disjunkcí při průběžné redukci. Proměnné blízko kořene dělí celý soubor na velké části, proto se heuristicky volí rozlišující příznaky.

**Výhody:** kompaktní reprezentace velkých množin přiřazení, kanoničnost při pevném pořadí a symbolické operace bez explicitního výčtu. **Omezení:** velikost může zůstat exponenciální a silně závisí na pořadí.

Celkový rámec zdroje propojuje agentní architektury, MDP/POMDP, QUBO, CSP/SAT a kanonické symbolické BDD/MDD.

