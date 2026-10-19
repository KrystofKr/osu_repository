# BI-ZUM – 05 teorie her

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610594

Karty Anki: 1785298610594
GUID: psd90>j,3,; štítky: AI_combined::05_teorie_her iterace_03 src_251-257 src_281.

### Otázka (Front)

Co studuje teorie her a jak je definována konečná hra v normální formě?

### Odpověď (Back)

Teorie her studuje strategické situace, v nichž utility a rozhodnutí agentů vzájemně závisejí. Kooperativní teorie bere jako jednotku tým/koalici, nekooperativní jednotlivého strategického hráče. **Normální forma** zachycuje typicky současné volby maticí; **extenzivní forma** pořadí rozhodnutí stromem.

Konečná normální hra je G=(N,A,u): N = hráči, A=A₁×…×Aₙ = akční profily a=(a₁,…,aₙ), u=(u₁,…,uₙ), kde uᵢ:A→R hodnotí úplný profil. Utilita závisí na všech akcích, protože výsledek vlastní volby ovlivňují ostatní.

Hlavní témata kapitoly: agent a prostředí, autonomie a interakce, PEAS, preference a očekávaná utilita, strategická závislost, normální forma, Paretova efektivnost a Nashova stabilita.

## Poznámka Anki 1785298610595

Karty Anki: 1785298610595
GUID: w+.<WSR&sd; štítky: AI_combined::05_teorie_her iterace_03 src_258-260.

### Otázka (Front)

Co ukazují kámen–nůžky–papír a vězňovo dilema jako hry v normální formě?

### Odpověď (Back)

**Kámen–nůžky–papír** je dvouhráčová zero-sum hra: remíza dává (0,0), výhra/prohra (+1,−1), takže součet je vždy 0.

**Vězňovo dilema** odděluje individuální racionalitu od kolektivní efektivnosti. Udání je pro každého nejlepší odpovědí bez ohledu na volbu druhého, proto je vzájemné udání stabilní. Oba však dopadnou hůře než při vzájemném neudání.

## Poznámka Anki 1785298610596

Karty Anki: 1785298610596
GUID: uZ~{2&KVqK; štítky: AI_combined::05_teorie_her iterace_03 src_261-265.

### Otázka (Front)

Jak se liší common-payoff, constant-sum a zero-sum hry?

### Odpověď (Back)

- **Common-payoff:** pro každý profil u₁(a)=…=uₙ(a); hráči hodnotí výsledky shodně. Modeluje čistou koordinaci či týmové rozhodování.
- **Constant-sum:** Σᵢuᵢ(a)=c pro každý profil; zlepšení jednoho musí být kompenzováno zhoršením jiných.
- **Zero-sum:** speciální constant-sum hra s c=0; zisk jedněch přesně vyrovnává ztrátu druhých.
Common-payoff znamená překryv zájmů, constant-sum jejich přímý konflikt.

## Poznámka Anki 1785298610597

Karty Anki: 1785298610597
GUID: PzY?Un8QI5; štítky: AI_combined::05_teorie_her iterace_03 src_266-273.

### Otázka (Front)

Co jsou Paretova dominance, Paretovo optimum a Paretova fronta?

### Odpověď (Back)

Normální forma umožňuje hodnotit celé profily podle globální efektivnosti. Utility hráčů jsou různá kritéria, proto jde o multikriteriální optimalizaci.

a′ **paretovsky dominuje** a, když uᵢ(a′)≥uᵢ(a) pro všechny hráče a alespoň pro jednoho přísně. Profil je **paretovsky optimální**, pokud jej žádný jiný nedominuje. Optim může být více; jejich množina je **Paretova fronta**. U ceny↓ a kvality↑ je výrobek optimální, pokud jiný není současně nejvýše stejně drahý a alespoň stejně kvalitní s jedním přísným zlepšením.

V matici na straně 313 jsou paretovsky optimální (E,C):(8,3), (F,D):(6,5), (G,B):(0,8) a (G,C):(5,7).

## Poznámka Anki 1785298610598

Karty Anki: 1785298610598
GUID: tl!f&dBUA}; štítky: AI_combined::05_teorie_her iterace_03 src_274-280.

### Otázka (Front)

Co jsou best response a Nashova rovnováha a jak se liší od Paretovy optimality?

### Odpověď (Back)

a<sub>−i</sub> je profil akcí všech hráčů kromě i. **Best response** je BR(a<sub>−i</sub>)=arg max<sub>âᵢ∈Aᵢ</sub>uᵢ(âᵢ,a<sub>−i</sub>). Profil a je **Nashova rovnováha**, když aᵢ∈BR(a<sub>−i</sub>) pro každého i. Při fixních akcích ostatních si tedy nikdo jednostrannou změnou nepolepší.

**Pareto** měří globální efektivnost — zda lze někoho zlepšit bez poškození jiného. **Nash** měří individuální stabilitu. Nashova rovnováha může být paretovsky neoptimální, jako ve vězňově dilematu.

V matici na straně 316 jsou Nashovy rovnováhy (E,D):(9,8), (F,A):(7,9) a (G,B):(9,9).

