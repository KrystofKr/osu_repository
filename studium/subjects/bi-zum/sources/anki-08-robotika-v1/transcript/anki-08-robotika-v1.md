# BI-ZUM – 08 robotika

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610615

Karty Anki: 1785298610615
GUID: M6bj5IBh^x; štítky: AI_combined::08_robotika iterace_06 src_405-412.

### Otázka (Front)

Co je robotika a robot, jaká je základní řídicí smyčka a jaké jsou hlavní kategorie robotů?

### Odpověď (Back)

**Robotika** spojuje mechaniku, elektrotechniku, informatiku, matematiku a fyziku při návrhu, konstrukci, řízení a použití robotů. **Robot** je fyzický agent: senzory vnímá, řídicí systém volí akce a efektory fyzicky působí.

Kategorie:

- **Manipulátor:** ukotvený kloubový řetězec umisťující koncový efektor, typicky v průmyslu.
- **Mobilní robot:** pohybuje se koly/nohami apod. a odhaduje polohu a orientaci.
- **Mobilní manipulátor:** mobilní základna + rameno.
- **Humanoid:** lidská stavba pro lidské prostředí/nástroje, bipedální pohyb a interakci.

## Poznámka Anki 1785298610616

Karty Anki: 1785298610616
GUID: s3U4H3b/]G; štítky: AI_combined::08_robotika iterace_06 src_413-419.

### Otázka (Front)

Jak se klasifikují senzory robota a které vlastnosti určují jejich použitelnost?

### Odpověď (Back)

Senzor převádí fyzikální jev na měření pro odhad stavu. **Pasivní** zachycuje přirozenou energii (kamera, mikrofon); **aktivní** vysílá energii a měří odezvu (sonar, lidar). **Proprioceptivní** měří vnitřní stav robota; **exteroceptivní** okolí. Jde o nezávislé osy: způsob získání signálu vs. co se měří.

**Zorné pole** je úhlová oblast a **dosah** interval vzdáleností. Přesnost = blízkost pravdě, opakovatelnost = shoda opakovaných měření, rozlišení = nejmenší rozpoznaná změna. Použitelnost dále ovlivňují absorpce/odraz, šum, rychlost, kalibrace, spolehlivost, spotřeba, velikost a cena.

## Poznámka Anki 1785298610617

Karty Anki: 1785298610617
GUID: ABEIOAZLpX; štítky: AI_combined::08_robotika iterace_06 src_420-424.

### Otázka (Front)

Jaké hlavní druhy robotických senzorů se používají a co měří?

### Odpověď (Back)

- **Lokalizační:** poloha/orientace — GPS, IMU, odometrie.
- **Proximitní:** přítomnost či vzdálenost objektu — sonar, IR dálkoměr, lidar.
- **Taktilní:** kontakt a jeho místo; senzory síly/tlaku navíc velikost, směr a momenty.
- **Kamery:** obraz pro vidění a rozpoznávání.
- **Mikrofony:** řeč, zvukové události či směr zdroje.
- **Typicky proprioceptivní:** gyroskop měří úhlový pohyb, akcelerometr zrychlení, enkodér/odometr změny polohy kloubu či kola.

## Poznámka Anki 1785298610618

Karty Anki: 1785298610618
GUID: wwGq5ec@bb; štítky: AI_combined::08_robotika iterace_06 src_425-430.

### Otázka (Front)

Co jsou efektor, koncový efektor a aktuátor a jaké mechanismy robot používá?

### Odpověď (Back)

**Efektor** vykonává fyzickou akci. Lokomoční efektor mění polohu robota (kola, nohy, pásy, ploutve či paže pro šplhání); manipulační mění objekty (rameno s chapadlem). **Koncový efektor** je nástroj na konci řetězce — chapadlo, hořák, měřidlo, obráběcí či řezací nástroj.

**Aktuátor** převádí energii na pohyb/sílu, zatímco efektor ji využije k působení na svět. Aktuátory mohou být elektrické motory, hydraulické/pneumatické válce, umělé svaly či piezoelektrické materiály.

## Poznámka Anki 1785298610619

Karty Anki: 1785298610619
GUID: gl!nKVb;HO; štítky: AI_combined::08_robotika iterace_06 src_431-435.

### Otázka (Front)

Co znamenají stupně volnosti, kinematický a dynamický stav a základní typy kloubů?

### Odpověď (Back)

**Stupeň volnosti (DOF)** je jeden nezávislý parametr pohybu — translace nebo rotace. Volné tuhé těleso v 3D má 6 DOF: tři translace a tři rotace.

**Kinematický stav** popisuje polohy/úhly DOF; **dynamický** navíc rychlosti a případně veličiny spojené se silami. Rotační kloub rotuje kolem osy, prizmatický se posouvá podél osy; každý základní kloub má 1 DOF. Kloub s n DOF lze modelovat posloupností n jednoduchých jednoosých kloubů.

## Poznámka Anki 1785298610620

Karty Anki: 1785298610620
GUID: nnXq2w^}P%; štítky: AI_combined::08_robotika iterace_06 src_436-443.

### Otázka (Front)

Jak funguje dopředná kinematika a skládání homogenních transformací?

### Odpověď (Back)

Dopředná kinematika z konfigurace kloubů q (úhly a vysunutí) počítá polohu a orientaci — **pózu** — koncového efektoru vzhledem k základně.

Převod bodu ze soustavy B do A: x<sub>A</sub>=t+Rx<sub>B</sub>. Homogenní matice T<sub>A←B</sub>=[[R,t],[0,1]] převádí [x<sub>B</sub>;1] na [x<sub>A</sub>;1], takže rotaci i translaci lze skládat násobením.

**Kinematický řetězec** je posloupnost článků a kloubů. T<sub>W←C</sub>=T<sub>W←A</sub>T<sub>A←B</sub>T<sub>B←C</sub>. Pořadí je zásadní, protože násobení není komutativní a určuje soustavu, v níž transformace působí.

## Poznámka Anki 1785298610621

Karty Anki: 1785298610621
GUID: kFY,3b9ju~; štítky: AI_combined::08_robotika iterace_06 src_444-452.

### Otázka (Front)

Co je inverzní kinematika, jaké může mít výsledky a jak se řeší?

### Odpověď (Back)

**Inverzní kinematika (IK)** hledá konfiguraci q pro požadovanou pózu efektoru. Je obtížnější než dopředná: řeší nelineární rovnice a zobrazení klouby→póza nemusí být prosté ani surjektivní.

Výsledek může být žádný (póza mimo pracovní prostor nebo omezení), jeden, více či nekonečně mnoho (např. loket nahoru/dolů). **Uzavřené řešení** je algebraické/geometrické; geometrické rozkládá prostorovou úlohu na jednodušší rovinné. **Numerické** iterativně snižuje chybu; Jacobián lokálně mapuje změny kloubů na změnu pózy a inverze/pseudoinverze koriguje q.

IK lze formulovat jako minimalizaci chyby pózy s penalizacemi za kloubová omezení, nehladkost či nežádoucí konfiguraci.

## Poznámka Anki 1785298610622

Karty Anki: 1785298610622
GUID: 0A@/A@I}7; štítky: AI_combined::08_robotika iterace_06 src_453-458.

### Otázka (Front)

Jak souvisí robotika s AI a jak se liší lead-through, teach, off-line, teleoperované a autonomní řízení?

### Odpověď (Back)

Robot je fyzický hardware; AI poskytuje řídicího softwarového agenta, který interpretuje senzory, rozhoduje a řídí efektory.

- **Lead-through:** operátor fyzicky vede efektor a robot zaznamená trajektorii.
- **Teach:** ovladačem nastaví posloupnost konfigurací k pozdějšímu přehrání.
- **Off-line:** program/trajektorie vzniká v modelu či simulaci mimo robot.
- **Teleoperace:** člověk průběžně řídí na dálku; haptika může vracet sílu/dotyk.
- **Autonomní:** počítač volí akce ze senzorické zpětné vazby bez průběžného člověka.

## Poznámka Anki 1785298610623

Karty Anki: 1785298610623
GUID: bOLe~oNq=O; štítky: AI_combined::08_robotika iterace_06 src_459-467.

### Otázka (Front)

Jak fungují hierarchické, reaktivní a hybridní paradigma robotické inteligence?

### Odpověď (Back)

Funkční primitiva: **Sense** interpretuje data, **Plan** tvoří pokyny, **Act** je převádí na aktuátory a **Learn** mění budoucí chování zkušeností.

- **Hierarchické/deliberativní:** Sense→Plan→Act, explicitní model a plán. Má dlouhodobý rozhled, ale vyžaduje přesný model a pomalé přeplánování.
- **Reaktivní:** vjemy se bez modelu a dlouhodobého plánu mapují na akční vzorce. Behaviorální moduly paralelně navrhují akce a arbitr je kombinuje/volí. Reaguje rychle, ale hůře plánuje a potřebuje dobrou pozorovatelnost.
- **Hybridní:** vyšší vrstva plánuje misi a podcíle, nižší rychle realizuje chování podle senzorů.

## Poznámka Anki 1785298610624

Karty Anki: 1785298610624
GUID: Ed4OWU0>MZ; štítky: AI_combined::08_robotika iterace_06 src_468-470.

### Otázka (Front)

Co je robotické vnímání a proč není totožné se senzorickým měřením?

### Odpověď (Back)

**Robotické vnímání** interpretuje senzorické odezvy do odhadů objektů, vlastností a stavu relevantních pro rozhodování. Měření je pouze šumový, neúplný a na senzoru závislý signál; percepce jej filtruje, slučuje s dalšími zdroji a významově interpretuje.

Typické úlohy: zpracování signálů/obrazu, extrakce příznaků, segmentace, rozpoznávání a klasifikace, sledování objektů a 3D rekonstrukce.

## Poznámka Anki 1785298610625

Karty Anki: 1785298610625
GUID: j)<hp}<7iy; štítky: AI_combined::08_robotika iterace_06 src_471-477.

### Otázka (Front)

Jak se liší plánování cesty a pohybu robota a jak souvisejí diskretizace, dynamika a zpětná vazba?

### Odpověď (Back)

**Plánování cesty** hledá geometrickou kolizně volnou křivku; **plánování pohybu** navíc respektuje čas, kinematiku, limity kloubů, síly, momenty a realizaci trajektorie. Spojitý prostor se pro BFS/DFS/Dijkstru/A* diskretizuje na konečný graf: buněčný rozklad dělí volný prostor na oblasti, skeletonizace na síť reprezentativních křivek.

Kinematický plán ignoruje hmotnost, setrvačnost, tření a vnější síly. **Dynamické plánování** je zahrne přímo, ale výrazně zvětší úlohu; alternativou je jednodušší kinematický plán průběžně opravovaný zpětnovazebním řízením podle naměřené odchylky.

## Poznámka Anki 1785298610626

Karty Anki: 1785298610626
GUID: As=?xaM|lr; štítky: AI_combined::08_robotika iterace_06 src_478-485.

### Otázka (Front)

Jak funguje uzavřená regulační smyčka a regulátory P, PI, PD a PID?

### Odpověď (Back)

Smyčka porovnává referenci r(t) s výstupem y(t), počítá chybu **e(t)=r(t)−y(t)** a podle ní opakovaně vytváří zásah.

- **P:** K<sub>p</sub>e(t), okamžitá reakce; vyšší K<sub>p</sub> zrychlí, ale může zvýšit překmit/nestabilitu.
- **I:** K<sub>i</sub>∫e(τ)dτ, akumuluje chybu a odstraní ustálenou odchylku; může zvýšit překmit a dobu ustálení.
- **D:** K<sub>d</sub>de/dt, reaguje na trend a tlumí; je citlivý na šum.
PI=P+I, PD=P+D a **PID**: u(t)=K<sub>p</sub>e(t)+K<sub>i</sub>∫<sub>t₀</sub><sup>t</sup>e(τ)dτ+K<sub>d</sub>de(t)/dt. Ladění vyvažuje rychlost, překmit, oscilace, ustálenou chybu, šum a stabilitu.

## Poznámka Anki 1785298610627

Karty Anki: 1785298610627
GUID: t{k^MwM?{b; štítky: AI_combined::08_robotika iterace_06 src_486-490.

### Otázka (Front)

Jak funguje reinforcement learning v robotickém řízení a čím doplňuje klasický regulátor?

### Odpověď (Back)

V **RL** agent pozoruje stav/pozorování, zvolí akci, prostředí přejde do dalšího stavu a vrátí skalární odměnu; zkušenost upraví strategii. Odměna hodnotí bezprostřední žádoucnost, ale neříká přímo správnou akci. Kvůli opožděným důsledkům se maximalizuje očekávaný **kumulativní dlouhodobý výnos**, ne jen příští odměna.

Klasický regulátor sleduje zadanou referenci podle chyby a modelu; RL může ze zkušenosti naučit volbu cílů, akcí či parametrů tam, kde je ruční návrh obtížný.

