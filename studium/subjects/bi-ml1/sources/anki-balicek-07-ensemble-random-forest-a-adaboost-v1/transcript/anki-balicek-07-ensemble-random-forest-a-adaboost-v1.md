# BI-ML1 – 07 Ensemble, Random Forest a AdaBoost

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::3 BI-ML1::07 Ensemble, Random Forest a AdaBoost
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785269100137

Karty Anki: 1785269200137
GUID: 9b175181f31e; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Co je **ensemble**, base/weak learner a jak se liší **bagging a boosting**?

### Odpověď (Back)

Ensemble kombinuje predikce více **base learnerů** do jednoho výsledku; vhodně odlišné modely mohou generalizovat lépe než jediný. **Weak learner** je samostatně jen mírně úspěšný podmodel, který přispěje ke kvalitnímu souboru.

| Bagging | Boosting | 
| Bootstrap aggregating: převážně nezávislé modely na náhodných výběrech a následná agregace. Příklad: Random Forest. | Modely vznikají sekvenčně; další reagují na chyby předchozích. Příklad: AdaBoost. |

## Poznámka Anki 1785269100138

Karty Anki: 1785269200138
GUID: d8e310dd20e5; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jak funguje **bagging a bootstrap** a jak z nich vzniká Random Forest?

### Odpověď (Back)

1. Opakovaně vytvořit náhodný dataset **výběrem s opakováním**: některý původní řádek může být několikrát, jiný vůbec.
2. Datasety vznikají nezávisle a liší se; obvykle mají velikost originálu, ale nemusí.
3. Na každém samostatně natrénovat podmodel.
4. Predikce agregovat.

U Random Forest jsou podmodely rozhodovací stromy natrénované na jednotlivých bootstrapových výběrech.

## Poznámka Anki 1785269100139

Karty Anki: 1785269200139
GUID: 814d5136ceeb; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jak Random Forest agreguje **klasifikační, regresní a pravděpodobnostní** predikce?

### Odpověď (Back)

- **Klasifikace:** většinové hlasování tříd.
- **Regrese:** **Ŷ=(1/n)ΣŶ<sub>i</sub>**.
- **Pravděpodobnost třídy 1:** **p̂=(1/n)Σp̂<sub>i</sub>**, poté např. třída 1 pro p̂>0,5.

Hlasování používá jen konečné třídy stromů; průměrování pravděpodobností zohledňuje i míru jejich jistoty.

## Poznámka Anki 1785269100140

Karty Anki: 1785269200140
GUID: c7dda3335817; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jaké klíčové hyperparametry a zdroje náhodnosti má **Random Forest**?

### Odpověď (Back)

- **n_estimators:** počet stromů.
- **max_depth:** maximální hloubka jednotlivého stromu.
- **max_features:** počet náhodně zvolených kandidátních příznaků při každém splitu; pro klasifikaci bývá výchozí přibližně √p.

Podmnožina se obvykle volí znovu v jednotlivých uzlech, ne jednou pro celý strom. Dva zdroje diverzity jsou bootstrap vzorků a náhodný výběr příznaků. Omezení max_features brání tomu, aby všechny stromy vždy použily stejný dominantní příznak.

## Poznámka Anki 1785269100141

Karty Anki: 1785269200141
GUID: 7bce7402e07a; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Proč je pro bagging důležitá **diverzita** a jak Random Forest snižuje variance a přeučení?

### Odpověď (Back)

Rozhodovací stromy jsou vhodné, protože mají vysokou variance: malé změny dat mohou zásadně změnit strukturu i predikce. Agregace odlišných stromů částečně vyruší jejich náhodné odchylky a sníží variance, zejména mají-li přiměřenou kvalitu a ne dokonale korelované chyby.

Identické stromy by žádné zlepšení nepřinesly. Bootstrap a max_features snižují korelaci stromů, takže les bývá robustnější a méně náchylný k přeučení než jeden strom.

## Poznámka Anki 1785269100142

Karty Anki: 1785269200142
GUID: a9fa3e84fcc2; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jaké jsou nevýhody Random Forestu z hlediska **interpretace** a co přesně znamená jeho náhodnost?

### Odpověď (Back)

Les částečně ztrácí jednoduchou interpretovatelnost jednoho stromu: predikce kombinuje mnoho různých cest a struktur.

„Náhodný“ neznamená náhodné hádání při predikci. Randomizace vytváří bootstrap datasety a kandidátní příznaky během konstrukce; natrénované stromy pak pro daný vstup deterministicky používají naučená pravidla.

## Poznámka Anki 1785269100143

Karty Anki: 1785269200143
GUID: 9eab79664cb4; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Co je **sample_weight** a jak váhy mění stavbu rozhodovacího stromu a informační zisk?

### Odpověď (Back)

Sample weight je nezáporná relativní důležitost trénovacího bodu; nevážené učení má stejné váhy (např. 1). Součet nemusí být vždy 1, ale AdaBoost je normalizuje.

- Vyšší váha vede strom k preferenci splitů, které bod správně klasifikují.
- Podíl třídy v uzlu = součet vah třídy / součet všech vah uzlu.
- **t<sub>L</sub>** = váha levého potomka / váha rodiče (analogicky t<sub>R</sub>).
- **IG=H(D)−t<sub>L</sub>H(D<sub>L</sub>)−t<sub>R</sub>H(D<sub>R</sub>)**, přičemž četnosti i velikosti jsou vážené.

Změna vah proto může změnit nejlepší split oproti neváženému stromu.

## Poznámka Anki 1785269100144

Karty Anki: 1785269200144
GUID: d05c5ea68c64; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jaká je základní myšlenka AdaBoostu a jak probíhá **inicializace a přesouvání pozornosti**?

### Odpověď (Back)

Boosting učí podmodely sekvenčně; každý další se více zaměřuje na případy, které předchozí nezvládl. AdaBoost to realizuje změnou vah bodů:

1. Inicializovat N vah rovnoměrně **w<sub>i</sub>=1/N**.
2. Natrénovat vážený podmodel.
3. Zvýšit váhy chybně klasifikovaných bodů; po normalizaci relativní váha správných klesne.
4. Normalizovat zpět na součet 1 a pokračovat nejvýše do **n_estimators**.

## Poznámka Anki 1785269100145

Karty Anki: 1785269200145
GUID: 7eb174ebdcbb; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jak se v popsaném AdaBoostu počítá **vážená chyba e<sup>(m)</sup> a hlasovací váha α<sup>(m)</sup>**?

### Odpověď (Back)

**e<sup>(m)</sup>** je součet aktuálních vah chybně klasifikovaných bodů; prostý podíl chyb je to jen při rovnoměrných vahách. Pro e=0 může algoritmus skončit.

**α<sup>(m)</sup>=learning_rate·log[(1−e<sup>(m)</sup>)/e<sup>(m)</sup>]**.

- Menší e → větší kladná váha; při e→0 roste velmi vysoko.
- e=0,5 → α=0, model nehlasuje.
- e>0,5 → α<0, model je horší než náhodné binární rozhodování.

## Poznámka Anki 1785269100146

Karty Anki: 1785269200146
GUID: 4a3afebd31a2; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jak AdaBoost aktualizuje **váhy bodů** a skládá konečné predikce?

### Odpověď (Back)

Pro chybně klasifikovaný bod se před normalizací použije **w<sub>i</sub>←w<sub>i</sub>·exp(α<sup>(m)</sup>)**; správně klasifikované váhy se v uvedeném zápisu přímo nezvyšují. Následující strom pak díky váženému kritériu považuje dřívější chyby za důležitější.

Finále je **vážené hlasování**: pro každou třídu se sečtou α modelů, které ji predikují, a vybere vyšší součet. Přesnější podmodel podle aktuálních vah má větší vliv; stromy tedy nehlasují stejně.

## Poznámka Anki 1785269100147

Karty Anki: 1785269200147
GUID: dcab11845c08; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jakou roli má v AdaBoostu **learning_rate** a jak souvisí s n_estimators a regularizací?

### Odpověď (Back)

Learning rate násobí α jednotlivých podmodelů a řídí rychlost přizpůsobení. Nižší hodnota zmenší jednotlivé kroky, zpomalí učení a může omezit příliš rychlé přeučení, proto funguje jako regularizační hyperparametr. Pro srovnatelný výkon však obvykle vyžaduje více podmodelů, tedy vyšší n_estimators.

## Poznámka Anki 1785269100148

Karty Anki: 1785269200148
GUID: ddd249bfb433; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jak se bagging a boosting typicky liší v bias–variance účinku a jaké podmodely může AdaBoost používat?

### Odpověď (Back)

**Bagging** primárně snižuje variance; **boosting** postupným opravováním systematických chyb typicky snižuje bias.

AdaBoost často používá mělké stromy: jednoduché weak learnery se sekvenčně skládají do flexibilního celku. Nemusí však používat jen stromy — stačí model podporující váhy vzorků. Vícetřídní rozšíření v materiálu je **AdaBoost-SAMME**, regresní varianta **AdaBoost.R2**.

## Poznámka Anki 1785269100149

Karty Anki: 1785269200149
GUID: ef1b35605008; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jak se liší Random Forest a AdaBoost v **práci s daty, závislosti podmodelů a paralelizaci**?

### Odpověď (Back)

| Random Forest / bagging | AdaBoost | 
| Nezávislé bootstrapové výběry; základní stromy se neučí podle chyb předchozích. Lze je přirozeně paralelizovat. | Dataset zůstává, adaptivně se mění váhy bodů. Další model závisí na chybách předchozího, proto se základní boosting paralelizuje obtížně. |

## Poznámka Anki 1785269100150

Karty Anki: 1785269200150
GUID: 97e1e7c05d68; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jaké výpočetní náklady přináší **vyšší počet stromů** v ensemble?

### Odpověď (Back)

Vyšší počet stromů obvykle zvětšuje výpočetní náročnost a kapacitu; vliv na přeučení závisí na metodě a dalších hyperparametrech. Při trénování Random Forestu je nutné vytvořit mnoho stromů. Při predikci musí více podmodelů vyhodnotit nový vstup a jejich výstupy se agregují.

## Poznámka Anki 1785269100151

Karty Anki: 1785269200151
GUID: e61839a3c0a8; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jaký meta-princip vysvětluje úspěch a jak probíhá **predikce Random Forestu**?

### Odpověď (Back)

Les kombinuje nestabilní, ale užitečné stromy, randomizací zvýší jejich různorodost a agregací redukuje náhodné chyby.

1. Předat vstup všem stromům.
2. Získat jejich predikce.
3. Agregovat hlasováním nebo průměrem.
4. Vrátit výslednou třídu či hodnotu.

## Poznámka Anki 1785269100152

Karty Anki: 1785269200152
GUID: 564ea6a883ee; štítky: 07_Ensemble_Random_Forest_a_AdaBoost BI-ML1 konsolidace.

### Otázka (Front)

Jaký meta-princip vysvětluje AdaBoost, jak probíhá jedna iterace a jak se jeho práce s chybami liší od Random Forestu?

### Odpověď (Back)

AdaBoost přesouvá pozornost k obtížným vzorkům a kombinuje podmodely podle kvality.

1. Natrénovat vážený podmodel.
2. Změřit váženou chybu.
3. Určit hlasovací váhu.
4. Zvýšit váhy chybně klasifikovaných bodů.

Random Forest chyby jednotlivých stromů **vyhlazuje agregací**; AdaBoost je používá k **řízení konstrukce dalších modelů**.

