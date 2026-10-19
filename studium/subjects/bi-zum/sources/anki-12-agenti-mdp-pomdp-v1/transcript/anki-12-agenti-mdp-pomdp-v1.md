# BI-ZUM – 12 agenti MDP POMDP

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610655

Karty Anki: 1785298610655
GUID: BQK*xq.64B; štítky: AI_combined::12_agenti_MDP_POMDP iterace_09 src_693-696.

### Otázka (Front)

Jak je uspořádán učící se agent a jak se liší jeho čtyři komponenty?

### Odpověď (Back)

**Výkonný prvek** volí akce. **Učící prvek** na základě zkušenosti mění výkonný prvek. **Kritik** porovnává pozorované výsledky s výkonnostním kritériem a dodává zpětnou vazbu. **Generátor problémů** navrhuje informativní explorativní akce, které mohou krátkodobě vypadat hůře, ale zlepšit budoucí rozhodování.

Vývoj schopností lze shrnout: reflex → paměť a model → cíle a plánování → užitkové porovnávání nejistých výsledků → adaptace modelu či strategie ze zkušenosti.

## Poznámka Anki 1785298610656

Karty Anki: 1785298610656
GUID: If9ap&^K1Y; štítky: AI_combined::12_agenti_MDP_POMDP iterace_09 src_697-708.

### Otázka (Front)

Co je konečný plně pozorovatelný MDP a proč je jeho řešením politika?

### Odpověď (Back)

**MDP** je určen (S,A,s₀,P,R): stavy, akce, počáteční stav, přechody P(s′|s,a) a okamžité odměny R(s). Prostředí je nedeterministické: jedna akce může vést do více stavů s danými pravděpodobnostmi. Platí **Markovova vlastnost** — při známém aktuálním stavu a akci nezávisí následující stav na starší historii.

Pevný plán nestačí, protože po stochastickém výsledku je třeba reagovat. Řešením je **politika** π:S→A, úplná pro všechny stavy nebo částečná jen pro některé. Stejná politika může vytvářet různé historie, proto se hodnotí očekávaným užitkem přes všechny běhy. **Optimální politika π*** tento dlouhodobý očekávaný užitek maximalizuje. R(s) je jen lokální odměna, zatímco U(s) zahrnuje očekávané budoucí odměny.

## Poznámka Anki 1785298610657

Karty Anki: 1785298610657
GUID: z+I[e6(Nx?; štítky: AI_combined::12_agenti_MDP_POMDP iterace_09 src_709-713.

### Otázka (Front)

Jak se definuje užitek historie a jakou roli má diskontní faktor γ?

### Odpověď (Back)

Stacionarita preferencí znamená, že připojení stejného počátečního stavu ke dvěma budoucím posloupnostem nezmění jejich pořadí. **Aditivní užitek** je U([s₀,s₁,…])=R(s₀)+R(s₁)+…, takže všechny odměny mají stejnou váhu.

**Diskontovaný užitek** je U=Σ<sub>t=0</sub><sup>∞</sup>γ<sup>t</sup>R(s<sub>t</sub>), 0<γ<1. Malé γ preferuje okamžité odměny, γ blízké 1 dlouhodobé následky. Pro omezené odměny zajišťuje konečnost nekonečného součtu: je-li |R(s)|≤R<sub>max</sub>, pak |U|≤R<sub>max</sub>/(1−γ).

## Poznámka Anki 1785298610658

Karty Anki: 1785298610658
GUID: bX&ucd0)3N; štítky: AI_combined::12_agenti_MDP_POMDP iterace_09 src_714-718.

### Otázka (Front)

Jak jsou definovány hodnoty stavů a Bellmanova rovnice optimality v diskontovaném MDP?

### Odpověď (Back)

Pro pevnou politiku je **U<sup>π</sup>(s)=E[Σ<sub>t=0</sub><sup>∞</sup>γ<sup>t</sup>R(s<sub>t</sub>) | π,s₀=s]**. Optimální hodnota je U*(s)=max<sub>π</sub>U<sup>π</sup>(s). Optimální akce splňuje π*(s)∈arg max<sub>a</sub>Σ<sub>s′</sub>P(s′|s,a)U*(s′).

**Bellmanova rovnice:** U*(s)=R(s)+γ max<sub>a</sub>Σ<sub>s′</sub>P(s′|s,a)U*(s′). Je rekurzivní, protože hodnotu stavu vyjadřuje okamžitou odměnou a hodnotami následných stavů, které jsou definovány stejným způsobem.

## Poznámka Anki 1785298610659

Karty Anki: 1785298610659
GUID: l%QG}2xss7; štítky: AI_combined::12_agenti_MDP_POMDP iterace_09 src_719-722.

### Otázka (Front)

Jak funguje value iteration a proč konverguje?

### Odpověď (Back)

Inicializuje odhady U₀ a opakuje pro všechny stavy **Bellmanovu aktualizaci**: U<sub>i+1</sub>(s)=R(s)+γ max<sub>a</sub>Σ<sub>s′</sub>P(s′|s,a)U<sub>i</sub>(s′). Po stabilizaci hodnot z nich odvodí chamtivou politiku.

Pro γ<1 Bellmanův optimalizační operátor tvoří kontrakci s faktorem γ, takže každá iterace zmenšuje maximální chybu a hodnoty konvergují k pevnému bodu U*. Pro optimální či téměř optimální politiku často není nutná extrémní numerická přesnost; rozhodující je správné pořadí očekávaných hodnot akcí.

## Poznámka Anki 1785298610660

Karty Anki: 1785298610660
GUID: KPPYo46N[W; štítky: AI_combined::12_agenti_MDP_POMDP iterace_09 src_723-727.

### Otázka (Front)

Jak funguje policy iteration a jak se liší od value iteration?

### Odpověď (Back)

**Policy iteration** střídá dva kroky: (1) vyhodnocení aktuální politiky a (2) její chamtivé zlepšení v každém stavu.

Pro pevnou π platí U<sup>π</sup>(s)=R(s)+γΣ<sub>s′</sub>P(s′|s,π(s))U<sup>π</sup>(s′); maximum zmizí, protože akci už určuje π. Přesné vyhodnocení je soustava lineárních rovnic v U<sup>π</sup>(s). Přibližně je lze získat několika aktualizacemi U<sub>i+1</sub>(s)=R(s)+γΣ<sub>s′</sub>P(s′|s,π(s))U<sub>i</sub>(s′).

**Rozdíl:** value iteration přímo opakuje optimalizační Bellmanovy aktualizace; policy iteration opakovaně vyhodnotí jednu politiku a poté ji zlepší.

## Poznámka Anki 1785298610661

Karty Anki: 1785298610661
GUID: cYD^LidUM$; štítky: AI_combined::12_agenti_MDP_POMDP iterace_09 src_728-735.

### Otázka (Front)

Co je POMDP, belief state a jak se belief aktualizuje?

### Odpověď (Back)

**POMDP** rozšiřuje MDP o částečnou pozorovatelnost. Obsahuje S, A, P(s′|s,a), R(s), množinu pozorování, senzorový model O(o|s) a případně počáteční rozdělení stavů. O(o|s) je pravděpodobnost pozorování o ve skutečném stavu s.

Jediný odhad stavu nestačí, proto agent udržuje **belief state b(s)**, pravděpodobnostní rozdělení nad fyzickými stavy. Po akci nejprve přechodovým modelem předpoví nové rozdělení a pak je pomocí O a Bayesova pravidla koriguje podle pozorování. Belief agent zná přesně, takže POMDP lze převést na plně pozorovatelný rozhodovací problém v prostoru beliefů. Ten je však spojitý, vysokodimenzionální a větví přes akce i pozorování, proto je řešení výrazně těžší než u MDP.

## Poznámka Anki 1785298610662

Karty Anki: 1785298610662
GUID: GaC2F+,{4v; štítky: AI_combined::12_agenti_MDP_POMDP iterace_09 src_736-740.

### Otázka (Front)

Jak funguje omezený look-ahead v POMDP a jaký má kompromis?

### Odpověď (Back)

Z aktuálního beliefu se rozvine strom do hloubky d. V **rozhodovacích uzlech** se maximalizuje přes akce; v **pozorovacích uzlech** se hodnoty potomků průměrují podle pravděpodobností pozorování. Listy se ohodnotí heuristikou, která odhaduje užitek za omezeným horizontem, a hodnoty se zpětně propagují ke kořeni.

Velikost roste přibližně jako O((|A|·|O|)<sup>d</sup>). Větší hloubka lépe zachytí dlouhodobé důsledky, ale exponenciálně zvyšuje časové a paměťové nároky.

