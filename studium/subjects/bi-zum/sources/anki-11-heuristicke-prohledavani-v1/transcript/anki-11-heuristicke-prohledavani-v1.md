# BI-ZUM – 11 heuristicke prohledavani

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610645

Karty Anki: 1785298610645
GUID: q+#V`]r9A,; štítky: AI_combined::11_heuristicke_prohledavani iterace_08 src_608-612.

### Otázka (Front)

Co je stavový prostor s ohodnocenými akcemi a jak se definuje cena a cíl cesty?

### Odpověď (Back)

Je to (S,A,c), kde S jsou stavy, A orientované akce a c:A→R₀⁺ jejich nezáporné ceny. Cena může vyjadřovat vzdálenost, čas, peníze, energii, riziko apod.

Pro cestu p=(s₁,a₁,s₂,…,aₙ₋₁,sₙ) je **C(p)=Σᵢc(aᵢ)**. Cílem je cesta z počátku do cíle s minimálním součtem. Nestačí minimalizovat počet kroků, protože kratší cesta může obsahovat dražší akce.

## Poznámka Anki 1785298610646

Karty Anki: 1785298610646
GUID: D;L~cMqTF1; štítky: AI_combined::11_heuristicke_prohledavani iterace_08 src_613-622.

### Otázka (Front)

Jak funguje Dijkstrův algoritmus a proč vrací optimální cesty?

### Odpověď (Back)

Dijkstra hledá nejlevnější cesty z počátku. g(s) je nejnižší dosud známá cena; OPEN je prioritní fronta podle g. Vybere minimum g a pro každou hranu (x,y) provede **relaxaci**: pokud g(x)+c(x,y)<g(y), aktualizuje g(y), prev[y] a prioritu.

Cíl lze bezpečně přijmout až při odebrání z OPEN, ne při prvním vygenerování. Invariant: při nezáporných cenách má odebraný uzel definitivně optimální g. Záporná hrana by mohla později zlevnit již uzavřený uzel a invariant porušit. dist ukládá ceny a prev rekonstruuje cestu.

## Poznámka Anki 1785298610647

Karty Anki: 1785298610647
GUID: u.kM0vbWQ1; štítky: AI_combined::11_heuristicke_prohledavani iterace_08 src_623-627.

### Otázka (Front)

Jaká je složitost Dijkstrova algoritmu, jak souvisí s BFS a proč může být v AI nepraktický?

### Odpověď (Back)

S vhodnou prioritní frontou je ve zdroji O(|A|+|S|log|S|). Dijkstra i BFS expandují podle rostoucí ceny cesty; BFS chápe cenu jako počet kroků. Mají-li všechny akce stejnou kladnou cenu, chovají se ekvivalentně.

Dijkstra neví, kde je cíl, a expanduje všesměrově podle g, takže zpracuje mnoho irelevantních stavů. Polynomiální složitost vůči explicitnímu grafu nepomáhá, pokud implicitní stavový prostor obsahuje astronomicky mnoho stavů.

## Poznámka Anki 1785298610648

Karty Anki: 1785298610648
GUID: h?Uw5w!zZ$; štítky: AI_combined::11_heuristicke_prohledavani iterace_08 src_628-635.

### Otázka (Front)

Co je heuristika a best-first search a jaký je rozdíl mezi minimem a arg min?

### Odpověď (Back)

**Heuristika** h:S→R₀⁺ levně odhaduje cenu nejlevnější zbývající cesty k cíli; v cíli h=0. Pomáhá prioritizovat perspektivní stavy, ale nemusí být přesná — přesný odhad by často vyřešil původní problém. V navigaci lze použít eukleidovskou vzdálenost či ortodromu.

**Best-first search** je rodina metod, které řadí OPEN hodnoticí funkcí a expandují nejslibnější uzel; není totožný s Breadth-First Search, který řadí hloubkou. Minimum je nejnižší hodnota funkce, **arg min** množina argumentů, kde jí dosahuje.

## Poznámka Anki 1785298610649

Karty Anki: 1785298610649
GUID: mALTx](OBt; štítky: AI_combined::11_heuristicke_prohledavani iterace_08 src_636-645.

### Otázka (Front)

Jak funguje Greedy search, jak se liší od Dijkstry a proč nezaručuje optimální cestu?

### Odpověď (Back)

Greedy vybírá s*∈arg min<sub>s∈OPEN</sub>h(s); prioritou je jen odhad zbývající ceny. „Hladově“ volí stav vypadající nejblíž cíli a ignoruje dosavadní g(s). Dijkstra naopak minimalizuje pouze g.

Výhodou je silná orientace na cíl a s dobrou h méně expanzí. Neoptimalita plyne z ignorování už zaplacené ceny: geometricky blízký stav může být za překážkou či dosažen draze. Výkon silně závisí na h; patologicky může dlouho sledovat přitažlivou slepou větev a přehlédnout mnohem kratší cestu.

## Poznámka Anki 1785298610650

Karty Anki: 1785298610650
GUID: AV0)qj0%3r; štítky: AI_combined::11_heuristicke_prohledavani iterace_08 src_646-655.

### Otázka (Front)

Jak funguje A* a jak spojuje Dijkstru s Greedy search?

### Odpověď (Back)

A* používá **f(s)=g(s)+h(s)**: skutečnou dosavadní cenu plus odhad zbytku, tedy odhad ceny úplného řešení přes s. Expanduje arg min f. Při hraně (x,y) navrhne g′(y)=g(x)+c(x,y); je-li levnější, aktualizuje g, prev a prioritu g′+h pomocí decrease/update-key.

Při h=0 je A*=Dijkstra. Greedy používá jen h; A* přidáním g penalizuje draze dosažené zkratky. Dijkstra používá jen g; A* přidáním h směřuje k cíli. Geometricky kombinuje kontury g od počátku a h od cíle.

## Poznámka Anki 1785298610651

Karty Anki: 1785298610651
GUID: x(^%:ldn$v; štítky: AI_combined::11_heuristicke_prohledavani iterace_08 src_656-662.

### Otázka (Front)

Co jsou optimální a přípustná heuristika a proč přípustnost sama nestačí k praktické užitečnosti?

### Odpověď (Back)

**h*(s)** je skutečná cena nejlevnější cesty ze s k nejbližšímu cíli. Je teoreticky nejlepší a dominuje všechny přípustné heuristiky, ale její výpočet bývá stejně těžký jako původní úloha.

h je **přípustná/admissible**, když h(s)≤h*(s): nikdy nenadhodnocuje a je „optimistická“. Vzdušná vzdálenost je přípustná, protože silniční trasa nemůže být kratší než přímá. Samotná přípustnost nezaručuje informativnost — h=0 je přípustná, ale redukuje A* na Dijkstru.

## Poznámka Anki 1785298610652

Karty Anki: 1785298610652
GUID: N~K6!#j(NG; štítky: AI_combined::11_heuristicke_prohledavani iterace_08 src_663-671.

### Otázka (Front)

Co je konzistentní heuristika a jaké podmínky zajišťují optimálnost A*?

### Odpověď (Back)

**Konzistence:** pro každou hranu (x,y) platí h(x)≤c(x,y)+h(y); odhad nesmí po kroku klesnout o více než cenu kroku. Pak f=g+h podél cesty neklesá. Opakováním podél optimální cesty k cíli s h(cíl)=0 plyne přípustnost. Nekonzistence nastane, když h(x)−h(y)>c(x,y).

S konzistentní h je g uzlu při odebrání z OPEN definitivní, není třeba znovu otevírat a první expandovaný cíl je optimální. S přípustnou, ale nekonzistentní h lze optimálnost zachovat znovuotevíráním uzlu po nalezení levnější cesty. Nepřípustná h může vrátit dražší cíl. Cíl se testuje při odebrání z OPEN, kdy je podmíněně nejlevnější.

## Poznámka Anki 1785298610653

Karty Anki: 1785298610653
GUID: nTLGac8?01; štítky: AI_combined::11_heuristicke_prohledavani iterace_08 src_672-677.

### Otázka (Front)

Co znamená dominance heuristik a jaký kompromis určuje jejich praktickou kvalitu?

### Odpověď (Back)

Přípustná h₁ **dominuje** h₂, pokud h₁(s)≥h₂(s) pro všechna s; je vždy alespoň tak informativní, ale stále ≤h*. h* dominuje všem přípustným. Dominující heuristika typicky expanduje nejvýše stejně uzlů, nemusí však být rychlejší, pokud je její výpočet drahý.

Kompromis je mezi rychlou slabou h s mnoha levnými expanzemi a přesnou drahou h s méně dražšími expanzemi. h₂ je jednoznačně lepší než h₁, pokud ji dominuje a není výpočetně náročnější.

## Poznámka Anki 1785298610654

Karty Anki: 1785298610654
GUID: NxDJak9[e`; štítky: AI_combined::11_heuristicke_prohledavani iterace_08 src_678-680.

### Otázka (Front)

Jak se porovnávají Dijkstra, Greedy a A* a co určuje efektivitu informovaného prohledávání?

### Odpověď (Back)

**Dijkstra:** f=g, optimální pro nezáporné ceny, bez směru k cíli. **Greedy:** f=h, cílený a často rychlý, ale obecně neoptimální. **A*:** f=g+h, optimální při odpovídající přípustnosti/konzistenci a správném zacházení s CLOSED.

Efektivitu určují kvalita odhadu, cena výpočtu h a správa OPEN, relaxací a znovuotevírání. Pilíře: aditivní ceny, g, h, f, prioritní expanze, relaxace, přípustnost, konzistence, dominance a kompromis informace vs. cena.

