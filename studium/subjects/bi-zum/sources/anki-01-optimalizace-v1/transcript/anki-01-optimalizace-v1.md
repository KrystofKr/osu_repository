# BI-ZUM – 01 optimalizace

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610546

Karty Anki: 1785298610546
GUID: v]::G:aID>; štítky: AI_combined::01_optimalizace iterace_01 src_001-009.

### Otázka (Front)

Jak se formálně definuje optimalizační problém a jakou roli mají X̂, X, f, omezení a arg max?

### Odpověď (Back)

**Prostor kandidátů X̂** určuje typ a reprezentaci všech možných kandidátů (např. Rⁿ nebo Zⁿ). **Množina přípustných řešení X ⊆ X̂** obsahuje jen kandidáty splňující omezení. **Kriteriální/účelová funkce f: X → R** jim přiřazuje kvalitu.

Úloha maximalizace hledá x* ∈ arg max<sub>x∈X</sub> f(x). **arg max** je množina maximalizátorů, nikoli maximální hodnota. Maximalizace f je ekvivalentní minimalizaci −f.

Standardní spojitý tvar: maximalizuj f(x), x ∈ Rⁿ, za podmínek g<sub>j</sub>(x) ≥ 0 a h<sub>k</sub>(x) = 0; právě omezení vymezují X.

 [Obrázek: paste-0ac5070c8f6a059fd0daac0b69a416a6f1d0517e.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1785298610547

Karty Anki: 1785298610547
GUID: egK+IwD-c?; štítky: AI_combined::01_optimalizace iterace_01 src_010-011 src_013-016.

### Otázka (Front)

Jak vypadají typické optimalizační modely: nejmenší čtverce, lineární programování, portfolio, regrese, plnění kontejneru a řízení agenta?

### Odpověď (Back)

-  [Obrázek: paste-9a1b424fad2a98d828dfa909feec255be18a56f6.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1785298610548

Karty Anki: 1785298610548
GUID: CyX0!ZG%:); štítky: AI_combined::01_optimalizace iterace_01 src_012 src_017-019.

### Otázka (Front)

Proč se používají obecné iterativní optimalizační metody AI, jaké mají schéma a kdy končí?

### Odpověď (Back)

**Proč:** problém může mít složitou, neznámou nebo špatně formalizovatelnou strukturu a nemusí existovat rychlý specializovaný algoritmus. Specializovaný algoritmus využívá známý standardní tvar funkce a omezení; obecná metoda předpokládá méně a poznává problém vyhodnocováním kandidátů.

**Schéma:** zvol x → vygeneruj kandidáta y → vyhodnoť f(x), f(y) → přijmi či odmítni y podle pravidla → opakuj.

**Konec:** dosažení dostatečné kvality, nebo vyčerpání časového či iteračního rozpočtu.

## Poznámka Anki 1785298610549

Karty Anki: 1785298610549
GUID: vpIu>}>=?V; štítky: AI_combined::01_optimalizace iterace_01 src_020-023.

### Otázka (Front)

Jak fungují hrubá síla a náhodná optimalizace a v čem se liší?

### Odpověď (Back)

**Hrubá síla** systematicky prochází zvolený vzorek prostoru, hodnotí všechny kandidáty a vrací nejlepšího. U pravidelné mřížky však počet bodů roste exponenciálně s dimenzí.

**Náhodná optimalizace** vygeneruje omezený počet nezávislých náhodných kandidátů a uchovává nejlepšího.

Rozdíl je v systematickém vs. náhodném vzorkování; ani jedna metoda přímo nevyužívá lokální strukturu kriteriální funkce.

## Poznámka Anki 1785298610550

Karty Anki: 1785298610550
GUID: H9(/!f@NrY; štítky: AI_combined::01_optimalizace iterace_01 src_024-032.

### Otázka (Front)

Jak funguje hill climbing, jeho okolí a varianta steepest-ascent a proč může metoda selhat?

### Odpověď (Back)

**Základní hill climbing:** z aktuálního x vygeneruje souseda y a při maximalizaci jej přijme jen tehdy, když f(y)>f(x). Fitness přijatých stavů proto neklesá.

**Okolí** tvoří řešení dosažitelná malou povolenou změnou: u Rⁿ např. vzdálenost ≤ ε, u bitového vektoru změna ≤ k bitů, u N dam přesun jedné dámy. **Steepest-ascent** vyhodnotí více sousedů a zvolí nejlepšího; má informovanější, ale dražší krok.

**Selhání:** v lokálním optimu není lepší soused, ačkoli lepší oblast existuje. Ve vysoké dimenzi exponenciálně roste počet vzorků potřebných k pokrytí okolí. Malé okolí zvyšuje riziko uváznutí, příliš velké kroky mohou přeskakovat užitečnou lokální strukturu a míjet optima.

## Poznámka Anki 1785298610551

Karty Anki: 1785298610551
GUID: o{(xAvh(t=; štítky: AI_combined::01_optimalizace iterace_01 src_033-039.

### Otázka (Front)

Jak funguje simulované žíhání včetně pravděpodobnosti přijetí a ochlazovacího plánu?

### Odpověď (Back)

Simulované žíhání rozšiřuje hill climbing o **teplotu t** a možnost dočasně přijmout horší řešení, aby překonalo bariéry mezi lokálními optimy.

Lepší kandidát se přijme; horší při maximalizaci typicky s pravděpodobností P = exp((f<sub>new</sub>−f<sub>curr</sub>)/t). Čím větší zhoršení, tím menší P; čím vyšší t, tím větší P.

**Ochlazovací plán** postupně snižuje t: začátek podporuje exploraci a pozdější fáze se blíží lokální exploataci hill climbingem.

## Poznámka Anki 1785298610552

Karty Anki: 1785298610552
GUID: ub)qJwOAgt; štítky: AI_combined::01_optimalizace iterace_01 src_040-044.

### Otázka (Front)

Jak funguje tabu prohledávání a jak se jeho únik z lokálního optima liší od simulovaného žíhání?

### Odpověď (Back)

**Tabu search** si v tabu listu dočasně pamatuje nedávné stavy, oblasti nebo atributy tahů a zakazuje návrat. Omezuje oscilaci a po dosažení lokálního vrcholu nutí algoritmus přijmout i zhoršující tah do jiné oblasti.

Podobnost lze měřit např. eukleidovskou či kosinovou vzdáleností (reálné vektory), Hammingovou vzdáleností (bity) nebo strukturálně (grafy/stromy).

**Rozdíl:** simulované žíhání přijímá horší tah pravděpodobnostně podle teploty; tabu search používá explicitní paměť a zákaz návratu.

## Poznámka Anki 1785298610553

Karty Anki: 1785298610553
GUID: J$q=(PTI%3; štítky: AI_combined::01_optimalizace iterace_01 src_045-051.

### Otázka (Front)

Jak se porovnávají hlavní rodiny iterativní optimalizace a jaké jsou jejich společné návrhové pilíře?

### Odpověď (Back)

- **Hrubá síla:** systematické pokrytí prostoru.
- **Náhodné hledání:** nezávislé náhodné vzorky.
- **Lokální metody:** využívají okolí jednoho řešení.
- **Populační metody:** udržují více kandidátů, kteří si předávají informaci; nejde jen o nezávislé běhy. Evoluční algoritmy používají selekci a genetické operátory, PSO upravuje pohyb podle nejlepších známých řešení. Další příklady: ACO, Intelligent Water Drops, Artificial Immune Systems a Bee Colony Optimization.
**Společné pilíře:** reprezentace a přípustnost, kriteriální funkce, generování kandidátů, pravidlo přijetí, explorace vs. exploatace, případná paměť/populace a podmínka ukončení.
---------------------------
 [Obrázek: paste-2aebf2acb319018de9561c9c0ee01c9f7784b856.jpg; soubor je v media/ v doprovodném ZIP]

