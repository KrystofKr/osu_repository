# BI-ZUM – 03 planovani

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 15 poznámek, 15 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610571

Karty Anki: 1785298610571
GUID: z4k(zwoLKu; štítky: AI_combined::03_planovani iterace_02 src_126-130.

### Otázka (Front)

Co je General Problem Solving (GPS), jaký má řetězec a proč by obecná AI neměla spoléhat na ručně vytvořené heuristiky?

### Odpověď (Back)

**GPS** nahrazuje zvláštní program pro každou úlohu univerzálním solverem nad formálním popisem: **problém → model → formální jazyk → solver → řešení → interpretace v původní doméně**. Člověk volí model a jazyk a zapíše instanci; solver ji automaticky řeší.

Ručně vytvořená heuristika přenáší podstatnou část inteligence na člověka a bývá doménově specifická. Obecný solver by ji měl odvozovat ze struktury formálního zadání. Neinformované hledání používá jen strukturu prostoru a ceny hran; informované navíc heuristický odhad zbývající ceny k cíli.

## Poznámka Anki 1785298610572

Karty Anki: 1785298610572
GUID: pF~[JPLa9i; štítky: AI_combined::03_planovani iterace_02 src_131-133.

### Otázka (Front)

Co je automatické plánování a proč používá dynamicky generovaný stavový prostor?

### Odpověď (Back)

**Automatické plánování** hledá posloupnost akcí převádějící počáteční konfiguraci do stavu splňujícího cíl.

**Statický pohled** předpokládá explicitní graf všech stavů a přechodů. **Dynamický pohled** zná počáteční stav a pravidla akcí a následníky generuje teprve během hledání. Tím kompaktně reprezentuje obrovský implicitní prostor bez předchozího výčtu všech stavů a hran.

## Poznámka Anki 1785298610573

Karty Anki: 1785298610573
GUID: D}j>d?#W%J; štítky: AI_combined::03_planovani iterace_02 src_134-138.

### Otázka (Front)

Podle čeho se klasifikují plánovací modely a jaké předpoklady má klasické plánování ve STRIPS?

### Odpověď (Back)

Tři osy jsou:

- **Dynamika:** deterministická akce má jeden výsledek; nedeterministická více výsledků bez nutných pravděpodobností; pravděpodobnostní přiřazuje výsledkům pravděpodobnosti.
- **Pozorovatelnost:** úplná = znám celý stav, částečná = jen část, nulová = žádná zpětná vazba o stavu.
- **Prostor:** diskrétní má konečně či spočetně oddělených stavů; spojitý nespočetně mnoho plynule se měnících stavů.
Klasický STRIPS předpokládá deterministické akce, plně známý počáteční stav a konečný diskrétní prostor.

## Poznámka Anki 1785298610574

Karty Anki: 1785298610574
GUID: wM*Sj|/:(Y; štítky: AI_combined::03_planovani iterace_02 src_139-149.

### Otázka (Front)

Jak je formálně definována úloha, stav, akce, přechod, cíl a plán ve STRIPS?

### Odpověď (Back)

Úloha je Π=(P,A,I,G): P = konečná množina atomů, A = akce, I⊆P = počáteční stav, G⊆P = cílové atomy. Stav s⊆P obsahuje právě pravdivé atomy; nepřítomné jsou nepravdivé a potenciálních stavů je 2<sup>|P|</sup>.

Akce a=⟨pre(a),add(a),del(a)⟩ je použitelná, když pre(a)⊆s, a vytvoří app<sub>a</sub>(s)=(s\del(a))∪add(a). Add efekt atom zpravdiví, delete efekt jej odstraní.

Cíl platí, když G⊆s; další atomy nevadí. Plán π=(a₁,…,aₙ) je aplikovatelná posloupnost končící v cíli; při jednotkových cenách je optimální plán nejkratší. STRIPS je kompaktní generativní popis, nikoli explicitní stavový graf.

## Poznámka Anki 1785298610575

Karty Anki: 1785298610575
GUID: G_G!1_Q7}<; štítky: AI_combined::03_planovani iterace_02 src_150-156.

### Otázka (Front)

Jak predikátová formulace zkompaktňuje STRIPS a jaký je rozdíl mezi akčním schématem a uzemněnou akcí?

### Odpověď (Back)

Ruční výčet konkrétních atomů a akcí rychle roste s počtem objektů. Predikátová formulace používá:

- **univerzum** = konečnou množinu objektů domény,
- **predikát** = pojmenovanou relaci; po dosazení objektů vznikne atom, např. on(red,blue),
- **akční schéma** = obecnou parametrizovanou akci s proměnnými.
**Substituce** nahradí všechny proměnné konkrétními objekty a vytvoří uzemněnou akci s konkrétními pre/add/del. STRIPS tím výpočetně těžkost neodstraňuje, ale jeho struktura dovoluje doménově nezávislému solveru odvozovat vztahy podcílů a automatické heuristiky.

## Poznámka Anki 1785298610576

Karty Anki: 1785298610576
GUID: BGzsn2w`l#; štítky: AI_combined::03_planovani iterace_02 src_157-159.

### Otázka (Front)

Jak se liší optimální a vyhovující plánování a dopředné, zpětné a obousměrné hledání?

### Odpověď (Back)

**Optimální solver** musí nalézt nejlevnější či nejkratší plán; **vyhovující (satisficing)** hledá libovolný platný plán bez záruky optimality.

**Dopředné plánování** generuje stavy od I, **zpětné** regresuje cílové podmínky směrem k I a **obousměrné** hledá průnik obou směrů. Běžný obecný přístup je heuristické dopředné hledání: následníci vznikají od počátečního stavu a řadí se podle automaticky vytvořeného odhadu zbývající ceny.

## Poznámka Anki 1785298610577

Karty Anki: 1785298610577
GUID: M0{A9PkO:a; štítky: AI_combined::03_planovani iterace_02 src_160-163.

### Otázka (Front)

Jak je definována heuristika h_goal ve STRIPS a proč je slabá?

### Odpověď (Back)

**h<sub>goal</sub>(s)=|G\s|**, tedy počet cílových atomů, které ve stavu s ještě neplatí.

Je málo informativní, protože stejně hodnotí stavy se stejně mnoha chybějícími cíli, i když se jejich skutečná obtížnost liší. Je citlivá na formulaci: tentýž věcný cíl lze zapsat jedním nebo mnoha atomy. Navíc ignoruje akce, jejich předpoklady, ceny a interakce mezi cíli.

## Poznámka Anki 1785298610578

Karty Anki: 1785298610578
GUID: Ax*k%X_yns; štítky: AI_combined::03_planovani iterace_02 src_164-166.

### Otázka (Front)

Jak vzniká heuristika ze zjednodušeného problému a jak se liší relaxace od abstrakce?

### Odpověď (Back)

Optimální cena řešení jednodušší verze se použije jako odhad ceny původní úlohy.

**Relaxace** přibližně zachová reprezentaci, ale odstraní některá omezení; bývá velmi informativní a často se používá ve vyhovujícím plánování. **Abstrakce** sloučí konkrétní stavy do menšího prostoru a zachová přechody jen na zhrubené úrovni; optimální abstraktní vzdálenost může být přípustná, takže se hodí i pro optimální plánování.

## Poznámka Anki 1785298610579

Karty Anki: 1785298610579
GUID: N*xhJV3PR|; štítky: AI_combined::03_planovani iterace_02 src_167-176.

### Otázka (Front)

Co je delete relaxace STRIPS, jaké má formální vlastnosti a co říká o řešitelnosti původní úlohy?

### Odpověď (Back)

Protože jsou předpoklady pozitivní, add efekty zpřístupňují další akce a cíle, zatímco delete efekty mohou rušit již dosažené podmínky. Delete relaxace je odstraní: pro a=⟨pre,add,del⟩ je a⁺=⟨pre,add,∅⟩ a Π⁺=(P,{a⁺|a∈A},I,G).

Stavy rostou monotónně s₀⊆s₁⊆… . Každý plán původní Π je po relaxaci platný v Π⁺. Je-li Π⁺ neřešitelná, je neřešitelná i Π; opačně to neplatí, protože relaxovaný plán může současně využívat atomy, které by se původně mazaly.

Jednoduchý hladový postup opakovaně přidává použitelnou akci přinášející nový atom, dokud nesplní G nebo už žádná taková akce není. Nemusí však nalézt nejkratší relaxovaný plán.

## Poznámka Anki 1785298610580

Karty Anki: 1785298610580
GUID: f.fPFjKuQN; štítky: AI_combined::03_planovani iterace_02 src_177-180.

### Otázka (Front)

Co je heuristika h⁺, proč je přípustná a proč se nahrazuje aproximacemi?

### Odpověď (Back)

**h⁺(s)** je délka nejkratšího plánu ze stavu s k cíli v delete-relaxované úloze. Relaxace může optimální plán jen zkrátit nebo zachovat, takže h⁺ nikdy nepřekročí skutečnou optimální cenu a je přípustná.

Přesné hledání nejkratšího relaxovaného plánu je ale stále výpočetně těžké (obecně NP-úplné), proto se používají levnější aproximace: **h<sub>max</sub>**, **h<sub>add</sub>** a extrakce relaxovaného plánu **h<sub>FF</sub>**.

## Poznámka Anki 1785298610581

Karty Anki: 1785298610581
GUID: u$[9p=5n((; štítky: AI_combined::03_planovani iterace_02 src_181-185.

### Otázka (Front)

Jak funguje heuristika h_max, jaké má rekurence, výhodu a omezení?

### Odpověď (Back)

Cenu konjunkce podcílů aproximuje maximem, jako by se jejich dosažení překrývalo či probíhalo souběžně. Pro jednotkové ceny:

cost<sub>max</sub>(a)=1+max<sub>p∈pre(a)</sub> cost<sub>max</sub>(p); atom získá minimum přes akce, které jej přidávají, a počáteční atom má cenu 0. Potom h<sub>max</sub>(s)=max<sub>g∈G</sub> cost<sub>max</sub>(g); nedosažitelný cíl dává ∞.

Maximum ceny nepřičítá, takže heuristika nepřekročí cenu plánu a je **přípustná**. Je však příliš optimistická a obvykle méně informativní.

## Poznámka Anki 1785298610582

Karty Anki: 1785298610582
GUID: xCgbJk3|S{; štítky: AI_combined::03_planovani iterace_02 src_186-191.

### Otázka (Front)

Jak funguje heuristika h_add a jak se liší od h_max?

### Odpověď (Back)

h<sub>add</sub> aproximuje cenu konjunkce **součtem**, jako by podcíle byly nákladově nezávislé. Pro jednotkové ceny:

cost<sub>add</sub>(a)=1+Σ<sub>p∈pre(a)</sub> cost<sub>add</sub>(p); atom získá minimum přes přidávající akce a počáteční atom cenu 0. Potom h<sub>add</sub>(s)=Σ<sub>g∈G</sub> cost<sub>add</sub>(g); nedosažitelný cíl dává ∞.

Rozlišuje více nákladných podcílů, a proto bývá informativnější než h<sub>max</sub>. Může však opakovaně započítat sdílenou akci či předpoklad a skutečnou cenu nadhodnotit, takže obecně **není přípustná**. h<sub>max</sub> je slabší, ale přípustná.

## Poznámka Anki 1785298610583

Karty Anki: 1785298610583
GUID: cU*@%&w~dY; štítky: AI_combined::03_planovani iterace_02 src_192-196.

### Otázka (Front)

Jak funguje heuristika h_FF a jak se liší od h⁺?

### Odpověď (Back)

h<sub>FF</sub> nejprve dopředně vytvoří strukturu dosažitelnosti v delete-relaxovaném problému a pak zpětně hladově vybere konkrétní podpůrné akce. Hodnota je počet akcí v takto extrahovaném relaxovaném plánu.

Protože extrakce nemusí najít nejkratší relaxovaný plán, h<sub>FF</sub> obecně není přípustná. Prakticky je však účinná: zachycuje konkrétní akce a jejich sdílení mezi cíli podstatně levněji než přesný výpočet.

**h⁺** = délka optimálního relaxovaného plánu, přípustná, ale těžko vypočitatelná. **h<sub>FF</sub>** = délka rychle extrahovaného, potenciálně suboptimálního relaxovaného plánu.

## Poznámka Anki 1785298610584

Karty Anki: 1785298610584
GUID: Gbwo_<7~60; štítky: AI_combined::03_planovani iterace_02 src_197-202.

### Otázka (Front)

Co je abstrakce stavového prostoru a jak vzniká přípustná abstrakční heuristika?

### Odpověď (Back)

Zobrazení α převádí konkrétní stavy do menšího abstraktního prostoru; ve STRIPS lze např. ignorovat vybrané atomy, takže stavy lišící se jen v nich splynou. Abstrakce odstraňuje rozlišení a omezení, proto optimální abstraktní cesta nemůže být dražší než konkrétní a její cena je přípustný dolní odhad.

**Kompromis:** hrubá abstrakce = malý a levný prostor, ale slabý odhad; jemná = informativnější, ale dražší na čas a paměť. Volba ignorovaných atomů je obtížná kvůli obrovskému počtu možností.

Na rozdíl od delete relaxace, která zachová atomy a akce a odstraní negativní efekty, abstrakce slučuje stavy a zachovává přechody jen zhruba.

## Poznámka Anki 1785298610585

Karty Anki: 1785298610585
GUID: Ehx#M:I]8R; štítky: AI_combined::03_planovani iterace_02 src_203-204.

### Otázka (Front)

Jaké jsou hlavní vrstvy automatického plánování a jak spolu souvisejí model, jazyk a solver?

### Odpověď (Back)

Vrstvy jsou: volba plánovacího modelu → kompaktní reprezentace (např. STRIPS) → implicitní stavový prostor → prohledávací strategie → automatické heuristiky z relaxace či abstrakce.

**Model** určuje předpoklady o světě, **jazyk** je formálně zapisuje a **solver** využívá strukturu jazyka k nalezení plánu. Správnost a použitelnost výsledku závisejí na všech třech vrstvách.

