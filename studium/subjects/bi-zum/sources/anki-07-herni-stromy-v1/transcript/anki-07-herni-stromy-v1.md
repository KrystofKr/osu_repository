# BI-ZUM – 07 herni stromy

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610607

Karty Anki: 1785298610607
GUID: q)(TmnQ1Wg; štítky: AI_combined::07_herni_stromy iterace_05 src_336-347.

### Otázka (Front)

Jak se liší normální a extenzivní forma hry a jak je konečná extenzivní hra formálně definována?

### Odpověď (Back)

Normální forma zachycuje strategie a výplaty maticí; **extenzivní forma** stromem explicitně popisuje pořadí tahů, hráče na tahu, dostupné akce a výsledky. Hodí se pro sekvenční hry jako šachy, dáma, piškvorky, Reversi či Go.

Konečná hra je osmice (N,A,H,T,χ,ρ,σ,u): N hráči; A všechny akce; H rozhodovací uzly; T terminály, H∩T=∅; χ:H→2<sup>A</sup> dostupné akce; ρ:H→N hráč na tahu; σ:H×A→H∪T následník; uᵢ:T→R utility hráčů. Prostota σ zajišťuje jediného předchůdce každého nekorenového uzlu, tedy strom. Vnitřní uzly jsou rozhodnutí, hrany akce a listy terminální výsledky.

## Poznámka Anki 1785298610608

Karty Anki: 1785298610608
GUID: ctw:{u_&F0; štítky: AI_combined::07_herni_stromy iterace_05 src_348-353.

### Otázka (Front)

Jak se modeluje dvouhráčová zero-sum hra a co znamenají uzly MAX a MIN?

### Odpověď (Back)

V každém terminálu t platí u₁(t)+u₂(t)=0: zisk jednoho je stejnou ztrátou druhého. Výhru/prohru/remízu lze z pohledu prvního hráče kódovat +1/−1/0; druhý má opačnou hodnotu. Proto stačí jediná funkce u, neboť u₂=−u₁.

**MAX** je hráč v kořeni maximalizující u, **MIN** soupeř minimalizující tutéž funkci. Jejich uzly se střídají podle tahu: MAX vybírá nejvyšší a MIN nejnižší hodnotu potomka.

## Poznámka Anki 1785298610609

Karty Anki: 1785298610609
GUID: s>O2Fd,KGu; štítky: AI_combined::07_herni_stromy iterace_05 src_354-359.

### Otázka (Front)

Co je perfektní hra a jak se prakticky nahrazuje úplné prohledání herního stromu?

### Odpověď (Back)

Perfektní hráč v každém tahu optimalizuje svůj **zaručený výsledek** proti nejlepší možné reakci soupeře. Bezchybná akce MAX maximalizuje minimum, které může MIN vynutit (maximin); chybná dává horší zaručený výsledek než jiná dostupná akce.

Úplný strom složitých her je kvůli kombinatorickému růstu nezvládnutelný. Proto se expanduje jen do hloubky d a hraniční neterminální listy se ohodnotí rychlou **heuristickou evaluační funkcí**. Skutečná evaluace je utilita terminálu; heuristická jen odhad stavu na hloubkovém limitu.

## Poznámka Anki 1785298610610

Karty Anki: 1785298610610
GUID: i20nQs>e>e; štítky: AI_combined::07_herni_stromy iterace_05 src_360-370.

### Otázka (Front)

Jak funguje Minimax, jaké má rekurence, záruky a časovou složitost?

### Odpověď (Back)

Minimax počítá nejvyšší zaručenou utilitu MAX za předpokladu perfektního MIN. List x má eval(x)=u(x), skutečnou nebo heuristickou hodnotu. Rekurze:

MAX: eval(x)=max<sub>a∈χ(x)</sub>eval(σ(x,a)); MIN: eval(x)=min<sub>a∈χ(x)</sub>eval(σ(x,a)). V kořeni se volí a∈arg max<sub>a∈χ(x₀)</sub>eval(σ(x₀,a)). Hodnoty se šíří od listů, protože rodič závisí na potomcích.

Úplný konečný strom s přesnými terminálními utilitami zaručí optimální tah proti perfektnímu soupeři. Hloubkový limit tuto záruku ruší kvůli chybě evaluace či ději za horizontem. Pro větvení b a hloubku d je čas O(b<sup>d</sup>); každá další úroveň násobí práci přibližně b.

## Poznámka Anki 1785298610611

Karty Anki: 1785298610611
GUID: nNd_MBdp>h; štítky: AI_combined::07_herni_stromy iterace_05 src_371-384.

### Otázka (Front)

Jak funguje alfa–beta prořezávání včetně významu mezí, aktualizací a podmínky cutoff?

### Odpověď (Back)

Alfa–beta vrací stejnou hodnotu a tah jako Minimax, ale vynechá podstromy, které už nemohou změnit rozhodnutí.

**α** je dolní mez — nejlepší hodnota, kterou si MAX už zaručí; **β** horní mez — nejnižší hodnota, kterou už může vynutit MIN. V kořeni α=−∞, β=+∞; potomci meze dědí. V MAX se α←max(α,v), v MIN β←min(β,v). α může jen růst, β jen klesat.

V MAX nastává β-řez při v≥β, v MIN α-řez při v≤α. Jednotně se podstrom ukončí při **α≥β**, protože předek už má alespoň stejně dobrou alternativu. Interval [α,β] vymezuje hodnoty ještě relevantní pro rozhodnutí předků.

## Poznámka Anki 1785298610612

Karty Anki: 1785298610612
GUID: JV%Gc#K&Ah; štítky: AI_combined::07_herni_stromy iterace_05 src_385-391.

### Otázka (Front)

Jak řazení tahů ovlivňuje alfa–beta prořezávání a jaké jsou jeho časové složitosti?

### Odpověď (Back)

Dobré tahy nalezené brzy rychle zpřísní α/β a vytvoří více cutoffů. Ideálně se v MAX zkoušejí nejvyšší a v MIN nejnižší očekávané hodnoty.

- Základní Minimax: O(b<sup>d</sup>).
- Ideální pořadí: O(b<sup>d/2</sup>), efektivní větvení ≈√b a za stejný rozpočet přibližně dvojnásobná hloubka.
- Náhodné pořadí podle zdroje: přibližně O(b<sup>3d/4</sup>) pro menší b.
Heuristické řazení odhaduje nejlepší tahy. **Killer heuristic** upřednostní tah, který způsobil cutoff v jiné větvi stejné či podobné hloubky.

## Poznámka Anki 1785298610613

Karty Anki: 1785298610613
GUID: u9BY~|9`Zv; štítky: AI_combined::07_herni_stromy iterace_05 src_392-399.

### Otázka (Front)

Jaké vlastnosti má mít herní evaluační funkce a jak se řeší problém horizontu?

### Odpověď (Back)

Evaluace má být **rychlá** (volá se v mnoha listech) a **spolehlivá** (koreluje se skutečnou kvalitou). Levnější dostatečný odhad může být lepší než přesnější drahý, protože dovolí hlubší hledání. Materiální šachová evaluace rychle sčítá počty a hodnoty figur, ale nezachytí všechny taktické a poziční faktory.

**Problém horizontu:** důležitý důsledek leží těsně za hloubkou d. **Quiescence search** proto v takticky nestabilních pozicích pokračuje jen vybranými vynucenými tahy, dokud nenastane relativně klidný stav; nerozšiřuje vše, aby neobnovila explozi.

Hloubka snižuje závislost na evaluaci, ale stojí výpočet; lepší evaluace může kompenzovat menší hloubku. Evaluace hodnotí jeden stav, Minimax skládá hodnoty mnoha stavů podle protichůdných voleb.

## Poznámka Anki 1785298610614

Karty Anki: 1785298610614
GUID: vXX$e+IVeT; štítky: AI_combined::07_herni_stromy iterace_05 src_400-404.

### Otázka (Front)

Jak se MCTS liší od Minimaxu a jaké vrstvy a kompromisy tvoří praktický systém pro hraní složitých her?

### Odpověď (Back)

Minimax s alfa–beta není jediná možnost. **Monte Carlo Tree Search** selektivně rozvíjí slibné části stromu podle statistických výsledků simulací místo systematické expanze všech uzlů do pevné hloubky. AlphaGo ve zdroji kombinuje MCTS s hlubokými sítěmi odhadujícími stavy a akce, učenými z expertních dat a reinforcement learningem ze self-play.

Vrstvy řešení: model hry (stavy, akce, utility) → vyhledávání a propagace hodnot → prořezávání → evaluace neprohledaného pokračování → řazení tahů. Výpočetní rozpočet se dělí mezi šířku, hloubku, kvalitu evaluace a režii heuristik; cílem je nejlepší tah v dostupném čase, nikoli úplnost.

