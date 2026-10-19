# BI-ML2 – Přednáška 12

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291669

Karty Anki: 1785306291670
GUID: Y25.YL4^Dc; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Co je posilované učení a jak probíhá interakce agenta s prostředím?

### Odpověď (Back)

V posilovaném učení (RL) se agent interakcí učí volit akce maximalizující očekávanou kumulativní odměnu. Ve stavu/pozorování zvolí akci; prostředí odpoví okamžitou číselnou odměnou a novým stavem. Akce ovlivňuje nejen současnou odměnu, ale i budoucí stavy, proto cíl není krátkozraký.

Na rozdíl od supervizovaného učení agent nedostává správnou akci pro každou situaci a musí ji objevit z důsledků vlastního zkoušení. Prostředí může být stochastické—stejná volba má různé výsledky—nebo nestacionární, když se rozdělení přechodů či odměn mění. Typický cíl je maximalizovat očekávaný součet současných a budoucích odměn. Hry jsou přirozený příklad: mají stavy, akce, pravidla přechodu a odměnu např. za vítězství.

## Poznámka Anki 1785306291671

Karty Anki: 1785306291672
GUID: f(Jq*Q~9NI; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Co je dilema explorace versus exploitace a proč je nutný jejich kompromis?

### Odpověď (Back)

**Explorace** zkouší málo známé akce pro získání informace; **exploitace** volí podle současných odhadů nejlepší akci. Čistá exploitace může po náhodných raných výsledcích uvíznout u suboptimální volby, zatímco čistá explorace dál plýtvá kroky na známé špatné akce. Úspěšná strategie oboje kombinuje a postupně zvýhodňuje slibné možnosti.

Jeden úspěšný pokus nestačí, protože jednotlivá odměna je náhodná; příklad chůze/kolo/metro ukazuje, že první výsledky mohou klamat. Čím delší zbývající rozhodovací horizont, tím více budoucích kroků může využít informaci zaplacenou dnešní explorací.

## Poznámka Anki 1785306291673

Karty Anki: 1785306291674
GUID: z6+]FJ)|Pb; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Co je k-ruký bandita a jak se definuje skutečná hodnota akce?

### Odpověď (Back)

Jednoruký bandita má jen jednu akci a tedy žádný problém výběru. K-ruký bandita nabízí k akcí/pák; každá generuje náhodnou odměnu z vlastního neznámého rozdělení. V čase t agent volí A<sub>t</sub> a dostane R<sub>t</sub>.

Skutečná hodnota je q*(a)=E[R<sub>t</sub>|A<sub>t</sub>=a]; hodnotová funkce q*:𝒜→ℝ přiřadí akci očekávanou odměnu. Při známých hodnotách by se volilo z arg max<sub>a</sub>q*(a), ale q* neznáme a odhadujeme je z pozorovaných odměn.

## Poznámka Anki 1785306291675

Karty Anki: 1785306291676
GUID: @GyLj;Pk8M; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Jak se výběrovým průměrem odhaduje hodnota akce a kdy konverguje?

### Odpověď (Back)

Q<sub>t</sub>(a) je odhad před rozhodnutím v čase t. Ve stacionárním banditovi je přirozeným odhadem průměr všech dřívějších odměn akce:
Q<sub>t</sub>(a)=Σ<sub>τ=1</sub><sup>t−1</sup>R<sub>τ</sub>1(A<sub>τ</sub>=a) / Σ<sub>τ=1</sub><sup>t−1</sup>1(A<sub>τ</sub>=a).
Čitatel sčítá její odměny, jmenovatel počet výběrů.

Pokud je rozdělení odměn stacionární a akce je vybrána nekonečněkrát, zákon velkých čísel dává Q<sub>t</sub>(a)→q*(a).

## Poznámka Anki 1785306291677

Karty Anki: 1785306291678
GUID: fQ,-t;,Lbz; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Jak se liší hladový a ε-hladový výběr a co přesně při konstantním ε konverguje?

### Odpověď (Back)

Hladové pravidlo vybírá A<sub>t</sub>∈arg max<sub>a</sub>Q<sub>t</sub>(a), při shodě typicky náhodně. Je čistě exploitační, takže po chybných počátcích může trvale preferovat suboptimum; v nestacionaritě nemusí znovu prověřit dříve horší akce.

ε-hladové pravidlo s pravděpodobností 1−ε volí hladově a s ε náhodně. Větší ε rychleji prozkoumává, ale častěji volí podřadné akce; menší ε více využívá, ale pomaleji opravuje omyly. Při konstantním ε>0 má každá akce stále kladnou šanci výběru. Ve stacionárním prostředí s výběrovými průměry je proto každá zkoušena nekonečněkrát a Q→q*. Neznamená to však, že se vždy volí optimum: chyba odhadu mizí, ale trvalá ε-explorace dál občas vybere suboptimální akci.

## Poznámka Anki 1785306291679

Karty Anki: 1785306291680
GUID: WE[(/`n0GI; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Jak se inkrementálně aktualizuje výběrový průměr a jak vypadá jednoduchý ε-hladový algoritmus?

### Odpověď (Back)

Pro n-tou odměnu R<sub>n</sub> dané akce a dosavadní odhad Q<sub>n</sub> platí
Q<sub>n+1</sub>=Q<sub>n</sub>+(1/n)(R<sub>n</sub>−Q<sub>n</sub>).
R−Q je predikční chyba a 1/n klesající krok. Jde o obecný vzor: nový odhad ← starý + krok·(cíl−starý). Nová odměna má s rostoucím n menší vliv; stačí uchovávat Q(a) a počet N(a), ne celou historii.

Algoritmus inicializuje Q(a)=N(a)=0 a ε. Opakovaně vybere akci ε-hladově, pozoruje R, zvýší N(A) a aktualizuje pouze
Q(A)←Q(A)+[1/N(A)]·[R−Q(A)].
Ostatní Q se nemění, protože jejich hypotetické odměny nebyly pozorovány.

## Poznámka Anki 1785306291681

Karty Anki: 1785306291682
GUID: ,pKPBE]iOd; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Jak se v nestacionárním banditovi používá konstantní krok α a jak souvisí s podmínkami konvergence?

### Odpověď (Back)

Ve stacionárním banditovi se rozdělení odměn nemění; v nestacionárním se hodnoty či rozdělení mění. Výběrový průměr váží staré i nové odměny stejně a reaguje pomalu. Proto se používá
Q<sub>n+1</sub>=Q<sub>n</sub>+α(R<sub>n</sub>−Q<sub>n</sub>)=αR<sub>n</sub>+(1−α)Q<sub>n</sub>,
exponenciálně vážený průměr zdůrazňující novější data. Velké α reaguje rychle, ale je hlučné; malé je hladké, ale pomalé.

Konstantní α nechává novému šumu nenulovou váhu, takže ani ve stacionárním případě odhad nekonverguje k jedné konstantě, nýbrž kolísá. Standardní podmínky stochastické aproximace jsou Σα<sub>n</sub>=∞ (nevyčerpat možnost oprav) a Σα<sub>n</sub>²<∞ (omezit kumulovaný šum). α<sub>n</sub>=1/n je splňuje; konstantní α druhou nesplňuje. V nestacionaritě je to žádoucí—cílem je sledovat pohybující se hodnotu, ne konvergovat k pevné.

## Poznámka Anki 1785306291683

Karty Anki: 1785306291684
GUID: V@[VPY+jyw; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Jak optimistické počáteční hodnoty podporují exploraci a jaké mají omezení?

### Odpověď (Back)

Všechny Q(a) se inicializují nerealisticky vysoko. Po vyzkoušení akce její odhad obvykle klesne, zatímco nevyzkoušené zůstanou atraktivní; i čistě hladový výběr tak na začátku projde různé akce. Počáteční Q lze také chápat jako apriorní očekávání.

Efekt je nejsilnější na začátku a pozorované odměny jej postupně překryjí. Samotný optimismus proto nezajišťuje průběžné znovuzkoušení akcí v měnícím se prostředí.

## Poznámka Anki 1785306291685

Karty Anki: 1785306291686
GUID: ~/sn|v8u5d; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Jak UCB systematicky kombinuje exploitaci s explorací?

### Odpověď (Back)

UCB (Upper Confidence Bound) řeší slabinu náhodné ε-explorace: vybírá podle odhadu i nejistoty:
A<sub>t</sub>=arg max<sub>a</sub>[Q<sub>t</sub>(a)+c√(ln t/N<sub>t</sub>(a))].
Q je exploitační odhad; druhý člen je explorační bonus. Klesá s počtem výběrů N(a), ale u dlouho zanedbané akce roste s ln t. Parametr c řídí exploraci: větší c více zkouší nejisté akce, menší se blíží greedy.

UCB preferuje slibné či nedostatečně prozkoumané akce místo rovnoměrně náhodných. N(a)=0 se řeší počátečním vyzkoušením všech akcí nebo nekonečným bonusem. Oproti optimismu průběžně aktualizuje nejistotu; oproti ε-greedy exploruje cíleně podle odhadu a nejistoty.

## Poznámka Anki 1785306291687

Karty Anki: 1785306291688
GUID: n-IisC`t2z; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Jak MDP rozšiřuje banditový problém o stavovou dynamiku?

### Odpověď (Back)

Bandita nemá stavovou dynamiku: volba přímo vytvoří odměnu a nemění budoucí možnosti. MDP (Markovský rozhodovací proces) modeluje sekvenční rozhodování pomocí stavů 𝒮, akcí 𝒜 a dynamiky
p(s′,r|s,a)=P(S<sub>t+1</sub>=s′,R<sub>t+1</sub>=r|S<sub>t</sub>=s,A<sub>t</sub>=a).
Ve stavu S<sub>t</sub> agent zvolí A<sub>t</sub>, prostředí společně náhodně vytvoří R<sub>t+1</sub> a S<sub>t+1</sub>. Společná distribuce zachycuje, že stejná akce může vést k různým párům nového stavu a odměny.

## Poznámka Anki 1785306291689

Karty Anki: 1785306291690
GUID: E_<<jB?=cJ; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Co je Markovská vlastnost a co musí obsahovat správně zvolený stav?

### Odpověď (Back)

Markovská vlastnost říká, že při známých S<sub>t</sub>,A<sub>t</sub> budoucí stav a odměna nezávisí na celé minulosti:
P(S<sub>t+1</sub>,R<sub>t+1</sub>|S<sub>t</sub>,A<sub>t</sub>,S<sub>t−1</sub>,A<sub>t−1</sub>,…)=P(S<sub>t+1</sub>,R<sub>t+1</sub>|S<sub>t</sub>,A<sub>t</sub>).
Stav proto musí shrnout veškerou minulou informaci relevantní pro predikci dynamiky. Pokud něco chybí, stejný zaznamenaný stav má podle skryté historie jiné přechody a reprezentace není Markovská.

Na rozdíl od bandity akce v MDP mění i budoucí stav a tím dlouhodobé odměny.

## Poznámka Anki 1785306291691

Karty Anki: 1785306291692
GUID: XlRGQgm1Sf; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Co je diskontovaný return G_t a jak γ řídí krátkodobé versus dlouhodobé rozhodování?

### Odpověď (Back)

Celková diskontovaná odměna od t je
G<sub>t</sub>=R<sub>t+1</sub>+γR<sub>t+2</sub>+γ²R<sub>t+3</sub>+…=Σ<sub>k=0</sub><sup>∞</sup>γ<sup>k</sup>R<sub>t+k+1</sub>,   γ∈[0,1].
γ=0 hodnotí jen nejbližší odměnu; menší γ preferuje blízké výsledky, γ blízko 1 pomalu diskontuje a zdůrazní dlouhodobé důsledky. Ve stochastickém MDP agent maximalizuje E[G<sub>t</sub>], protože trajektorie není jistá.

Akce s malou okamžitou odměnou může otevřít velmi výnosné budoucí stavy; vysoká okamžitá odměna může naopak vést do špatného stavu. G<sub>t</sub> zachycuje celý tento rozdíl oproti krátkozrakému R<sub>t+1</sub>.

## Poznámka Anki 1785306291693

Karty Anki: 1785306291694
GUID: +0B@h1|wdk; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Co je action-value funkce q(s,a) a proč se v moderním RL aproximuje?

### Odpověď (Back)

q(s,a)=E[G<sub>t</sub>|S<sub>t</sub>=s,A<sub>t</sub>=a] hodnotí očekávaný dlouhodobý výnos po volbě a ve stavu s při daném následném chování. V banditovi q*(a) závisí jen na akci a okamžité odměně; MDP hodnota závisí na stavu a budoucí trajektorii. Rozhodování preferuje nejvyšší q v aktuálním stavu.

Optimální action-value udává nejvyšší dosažitelný očekávaný return po dané první akci a následných optimálních volbách. Protože kombinací stav–akce může být příliš mnoho či spojitě nekonečno, q se často aproximuje, např. neuronovou sítí predikující návratnost ze stavu a akce.

## Poznámka Anki 1785306291695

Karty Anki: 1785306291696
GUID: ,*#](@W+Gw; štítky: BI-ML2 Iterace_12 Konsolidovano Prednaska_12.

### Otázka (Front)

Jaká je celková struktura základního RL a jak do ní zapadají bandity, MDP a částečná pozorovatelnost?

### Odpověď (Back)

V částečně pozorovatelném prostředí agent nevidí plný stav, jen neúplné či zašuměné pozorování; aktuální vstup nemusí stačit, a proto musí využívat historii. RL se od supervize liší učením z důsledků vlastních sekvenčních akcí a od nesupervizovaného učení cílem maximalizovat odměnu, ne pouze objevit strukturu dat.

Základní rámec spojuje nejistotu odměn, exploraci/exploitaci a dlouhodobé změny stavů. Bandita učí hodnoty akcí bez stavů; MDP přidá stav, pravděpodobné přechody a celý budoucí return. Banditové strategie jsou greedy, ε-greedy, optimistické Q a UCB—tedy bez explorace, náhodná průběžná, počáteční optimistická a systematická podle nejistoty. Společný učicí princip je oprava odhadu o krok·(nový cíl−dosavadní predikce).

