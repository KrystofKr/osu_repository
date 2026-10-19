# BI-ZUM – 04 multiagentni systemy

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610586

Karty Anki: 1785298610586
GUID: FdJzNz5~]@; štítky: AI_combined::04_multiagentni_systemy iterace_03 src_205-208.

### Otázka (Front)

Co je multiagentní systém a proč se hodí pro distribuované, dynamické nebo nekooperativní problémy?

### Odpověď (Back)

**Multiagentní systém (MAS)** je soubor nezávislých agentů ve sdíleném prostředí; každý vnímá, jedná za svými cíli a interaguje s ostatními.

- **Distribuované problémy:** globální znalost nemusí být dostupná ani efektivně spravovatelná, proto se rozhodování dělí mezi lokální agenty.
- **Dynamické prostředí:** autonomní agenti mohou rychle lokálně reagovat, měnit plány a koordinovat se bez čekání na centrum.
- **Nekooperativní uspořádání:** agenti nemají společný cíl nebo spolupracovat nechtějí, takže je nutné počítat se strategickým a konfliktním chováním.

## Poznámka Anki 1785298610587

Karty Anki: 1785298610587
GUID: txmsf:AXM*; štítky: AI_combined::04_multiagentni_systemy iterace_03 src_209-216.

### Otázka (Front)

Jak se definuje agent, co znamenají situatedness, embodiment a autonomie a jaké může mít agent vztahy k ostatním?

### Odpověď (Back)

**Russell a Norvig:** agent vnímá prostředí senzory a působí na něj efektory. Situatedness a embodiment zdůrazňují jeho umístění v konkrétním fyzickém či virtuálním prostředí.

**Wooldridge a Jennings:** je to počítačový systém schopný samostatné účelné činnosti pro vlastní či delegované cíle; přidávají tedy autonomii a vztah k zadavateli. Autonomie znamená řídit činnost bez průběžných rad podle vlastního stavu a zkušenosti.

Agent prostředí ovlivňuje, ale kvůli nedeterminismu, neúplným vjemům, selháním a jiným aktérům je plně neovládá. Může být **izolovaný**, **kooperativní** (týmový cíl), **self-interested** (vlastní prospěch) nebo **hybridní** (s někým spolupracuje a s jiným soutěží).

## Poznámka Anki 1785298610588

Karty Anki: 1785298610588
GUID: htf84JNf5{; štítky: AI_combined::04_multiagentni_systemy iterace_03 src_217-222.

### Otázka (Front)

Jaké čtyři fundamentální vlastnosti má inteligentní agent a jak se liší koordinace, kooperace a vyjednávání?

### Odpověď (Back)

Inteligentní agent je:

- **autonomní** — řídí vlastní činnost,
- **reaktivní** — průběžně reaguje na změny prostředí,
- **proaktivní** — z vlastní iniciativy sleduje cíle,
- **sociální** — interaguje s jinými agenty.
Reaktivita bez proaktivity jen odpovídá na události; proaktivita bez reaktivity ignoruje změny. Účelné chování potřebuje obojí.

**Koordinace** spravuje vazby mezi akcemi, **kooperace** je týmová práce na společném cíli a **vyjednávání** hledá shodu ve věcech společného zájmu.

## Poznámka Anki 1785298610589

Karty Anki: 1785298610589
GUID: J(*k^7>FTH; štítky: AI_combined::04_multiagentni_systemy iterace_03 src_223-228.

### Otázka (Front)

Co znamená PEAS a jak specifikuje úlohové prostředí a návrh agenta?

### Odpověď (Back)

**PEAS** = Performance measure, Environment, Actuators, Sensors:

- **Performance measure:** podle čeho se hodnotí chování — např. cíl, rychlost či bezpečnost.
- **Environment:** svět, v němž agent jedná — např. silnice, bludiště nebo herní mapa.
- **Actuators/efektory:** prostředky ovlivnění světa — kola, nohy, zbraně či komunikace.
- **Sensors:** zdroje vjemů — kamera, radar nebo zprávy.
PEAS definuje **task environment**; řešením je agent, jehož chování v tomto prostředí maximalizuje danou metriku.

## Poznámka Anki 1785298610590

Karty Anki: 1785298610590
GUID: li7jODG~A); štítky: AI_combined::04_multiagentni_systemy iterace_03 src_229-234.

### Otázka (Front)

Podle jakých šesti os se klasifikuje prostředí agenta?

### Odpověď (Back)

- **Plně vs. částečně pozorovatelné:** úplná správná informace o relevantním stavu vs. neúplné/nepřesné vjemy.
- **Deterministické vs. stochastické:** jednoznačný výsledek akce vs. pravděpodobnostní nejistota.
- **Epizodické vs. sekvenční:** nezávislé epizody vs. současná akce ovlivňuje budoucnost.
- **Statické vs. dynamické:** během rozhodování se samo nemění vs. mění se vlivem procesů či jiných aktérů.
- **Diskrétní vs. spojité:** oddělené konečné/spočetné hodnoty vs. spojité obory.
- **Single-agent vs. multi-agent:** výsledek není vs. je strategicky závislý na jednání dalších agentů.

## Poznámka Anki 1785298610591

Karty Anki: 1785298610591
GUID: <(IAq%MGp; štítky: AI_combined::04_multiagentni_systemy iterace_03 src_235-237.

### Otázka (Front)

Jaký je rozdíl mezi agentní funkcí, agentním programem a architekturou a co je třeba při návrhu řešit?

### Odpověď (Back)

**Agentní funkce** je abstraktní zobrazení f:P→A přiřazující sekvenci vjemů akci či posloupnosti akcí. **Agentní program** tuto funkci implementuje a **architektura** je fyzická nebo virtuální platforma, která program vykonává.

Návrh musí určit (1) která funkce vede ke správnému/racionálnímu chování a (2) zda ji lze realizovat dostatečně malým a výpočetně zvládnutelným programem.

## Poznámka Anki 1785298610592

Karty Anki: 1785298610592
GUID: qEb??S{fYD; štítky: AI_combined::04_multiagentni_systemy AI_combined::12_agenti_MDP_POMDP finalni_konsolidace src_238-242 src_681-692.

### Otázka (Front)

Jak se liší reflexní, modelový, cílově orientovaný a užitkově orientovaný agent?

### Odpověď (Back)

Schopnosti se postupně rozšiřují:
• **Jednoduchý reflexní agent** mapuje aktuální vjem na akci pravidly „podmínka → akce“; nemá historii ani model. Stačí při plné pozorovatelnosti, ale při částečné nerozliší stejné vjemy vzniklé z různých stavů.
• **Modelový/reflexní se stavem** udržuje vnitřní stav z minulého stavu, akce a nového vjemu. Potřebuje přechodový model prostředí a senzorový model vjemů.
• **Cílově orientovaný** přidává cíle a plánování více kroků. Cíl však hodnotí jen úspěch/neúspěch.
• **Užitkově orientovaný** odstupňovaně hodnotí výsledky, cesty a konfliktní cíle užitkovou funkcí; při nejistotě maximalizuje očekávaný užitek a dočasné cíle chápe jako prostředky dlouhodobého užitku.

## Poznámka Anki 1785298610593

Karty Anki: 1785298610593
GUID: JMyCX;e@6o; štítky: AI_combined::04_multiagentni_systemy iterace_03 src_243-250.

### Otázka (Front)

Jak se formálně reprezentují preference a rozhodování racionálního agenta pod nejistotou?

### Odpověď (Back)

Preference lze vyjádřit relací ≽ nebo utilitou u:S→R tak, že u(s₁)≥u(s₂) právě tehdy, když je s₁ alespoň tak preferovaný jako s₂.

**Loterie** ℓ=[p₁:o₁,…,pₖ:oₖ] je rozdělení nad výsledky, pᵢ>0 a Σpᵢ=1. Nejistá akce je loterie, protože neurčuje jediný výsledek. Očekávaná utilita agenta i je E[uᵢ|ℓ]=Σⱼpⱼuᵢ(oⱼ).

**Self-interested racionalita** maximalizuje vlastní očekávanou utilitu; **kooperativní racionalita** maximalizuje očekávaný součet utilit všech agentů.

