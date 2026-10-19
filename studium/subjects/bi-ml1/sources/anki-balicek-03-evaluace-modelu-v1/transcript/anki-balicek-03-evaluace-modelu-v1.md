# BI-ML1 – 03 Evaluace modelu

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::3 BI-ML1::03 Evaluace modelu
Rozsah: 27 poznámek, 27 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785269100040

Karty Anki: 1785269200040
GUID: 80721e49838b; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Co je **generalizace**, proč nestačí výkon na trénovacích datech a proč je volba evaluační metriky součástí formulace úlohy?

### Odpověď (Back)

**Generalizace** je schopnost modelu uspět na nových vstupech, které při tréninku neviděl. Výkon na trénovacích datech nestačí, protože model je může přeučit; přesné přizpůsobení známým datům nezaručuje malou budoucí chybu.

Různé metriky zvýhodňují různé druhy chování a chyb. Volbou metriky tedy určujeme, co v dané úloze považujeme za kvalitní model.

## Poznámka Anki 1785269100041

Karty Anki: 1785269200041
GUID: 0da2e5111fb1; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Co je **ztrátová funkce** a jak se liší kvadratická a absolutní ztráta?

### Odpověď (Back)

Ztrátová funkce **L(Y,Ŷ)** měří chybu jedné konkrétní predikce. Bývá nezáporná a menší hodnota znamená lepší predikci.

- **Kvadratická:** L(Y,Ŷ)=(Y−Ŷ)<sup>2</sup>; velké chyby penalizuje silně.
- **Absolutní (L1):** L(Y,Ŷ)=|Y−Ŷ|; roste s chybou lineárně.

## Poznámka Anki 1785269100042

Karty Anki: 1785269200042
GUID: c1b916471bbc; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Co vrací pravděpodobnostní binární klasifikátor a jak z pravděpodobnosti vznikne predikce třídy? Jak ji může odhadnout list stromu?

### Odpověď (Back)

Model vrací **p̂(x)=P̂(Y=1|X=x)**. List rozhodovacího stromu ji může odhadnout relativní četností třídy 1 mezi trénovacími vzorky v listu.

Při standardním prahu se predikuje **Ŷ=1 pro p̂>0,5**, jinak Ŷ=0.

## Poznámka Anki 1785269100043

Karty Anki: 1785269200043
GUID: ddebef2e6a2e; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak je definována a jak se chová **binární křížová entropie** pro jednu predikci?

### Odpověď (Back)

**L(Y,p̂)=−Y log(p̂)−(1−Y)log(1−p̂)**.

- Pro Y=1: **−log(p̂)**.
- Pro Y=0: **−log(1−p̂)**.

Přiřadí-li model skutečné třídě pravděpodobnost blízkou nule, ztráta prudce roste; sebejistou chybnou predikci tedy penalizuje velmi silně.

## Poznámka Anki 1785269100044

Karty Anki: 1785269200044
GUID: 0511ed3f3509; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak se ze ztráty jednotlivého vzorku vytvoří **průměrná trénovací chyba**, MSE a MAE? Jak souvisí MSE s RSS?

### Odpověď (Back)

**err<sub>train</sub>=(1/N)Σ<sub>i</sub>L(Y<sub>i</sub>,Ŷ(x<sub>i</sub>))**.

- **MSE<sub>train</sub>=(1/N)Σ(Y<sub>i</sub>−Ŷ<sub>i</sub>)²**.
- **MAE<sub>train</sub>=(1/N)Σ|Y<sub>i</sub>−Ŷ<sub>i</sub>|**.

RSS je součet čtverců bez faktoru 1/N. MSE a RSS se tedy liší jen kladnou konstantou a mají stejné minimalizátory.

## Poznámka Anki 1785269100045

Karty Anki: 1785269200045
GUID: 42c0144e4675; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Co se při fixních hyperparametrech optimalizuje během trénování a jak se liší **explicitní** a **iterativní** učení parametrů?

### Odpověď (Back)

Hledají se parametry minimalizující trénovací chybu.

- **Explicitní řešení:** parametry získáme přímo vzorcem.
- **Iterativní řešení:** k minimu se postupně přibližujeme, např. gradientním sestupem.

Je-li účelová funkce nekonvexní, iterativní algoritmus může skončit pouze v lokálním, nikoli globálním minimu.

## Poznámka Anki 1785269100046

Karty Anki: 1785269200046
GUID: 1840261e26c1; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak se liší testovací chyba konkrétního modelu **Err<sub>D</sub>**, její výběrový odhad a očekávaná testovací chyba **Err**?

### Odpověď (Back)

- **Err<sub>D</sub>=E[L(Y,Ŷ(X))|D]**: očekávaná ztráta modelu natrénovaného z konkrétní náhodné množiny D na novém vstupu.
- **err<sub>test</sub>=(1/N<sub>test</sub>)ΣL(Y<sub>i</sub>,Ŷ(x<sub>i</sub>))**: výběrový odhad Err<sub>D</sub>. Je nestranný, jsou-li testovací vzorky nezávislé na trénovacích datech a nebyly použity při tvorbě modelu.
- **Err=E<sub>D</sub>[Err<sub>D</sub>]**: průměruje výkonnost také přes možné trénovací množiny.

## Poznámka Anki 1785269100047

Karty Anki: 1785269200047
GUID: 82e1409b95a4; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak se liší **výběr** a **ohodnocení** modelu a jaké role mají train, validation, test a hold-out?

### Odpověď (Back)

**Výběr** porovnává kandidáty; **ohodnocení** nezávisle odhaduje chybu již vybraného finálního modelu. Stejná data nelze použít pro obojí, protože výběr se jim přizpůsobí.

- **Train:** parametry při fixních hyperparametrech.
- **Validation:** hyperparametry a třída modelu.
- **Test:** až konečný nezávislý odhad generalizace.

**Hold-out** znamená oddělit test a použít jej jednou na konci. Porovnávání vítězů různých tříd modelů na testu je už další výběr, a tedy chyba.

## Poznámka Anki 1785269100048

Karty Anki: 1785269200048
GUID: 0001f8f15ee3; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Proč se test odděluje před předzpracováním, co je **data leakage** a jak korektně transformovat validační a testovací data?

### Odpověď (Back)

**Data leakage** je použití informace, která má být dostupná až při validaci, testování nebo v budoucnu, během trénování či výběru modelu.

Test se oddělí před všemi kroky, které z dat něco odhadují. Parametry předzpracování se naučí **jen na trénovacích datech** a beze změny se aplikují na validaci a test; jinak se informace z nich propíše do modelovací procedury.

## Poznámka Anki 1785269100049

Karty Anki: 1785269200049
GUID: 6d3f9d27427c; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Kdy data před rozdělením náhodně promíchat a kdy použít **chronologický split**?

### Odpověď (Back)

Validace a test odhadují budoucí výkon jen tehdy, když odpovídají rozdělení budoucích dat a nevznikají nežádoucí procesní rozdíly.

- **Náhodné promíchání:** odstraní umělé pořadí řádků a je vhodné, chceme-li reprezentativní části z téhož procesu.
- **Chronologický split:** u predikce budoucnosti z minulosti, časových řad či nestacionárního procesu, jehož vlastnosti se v čase mění. Trénujeme na starších a hodnotíme na pozdějších datech.

Náhodný split časových dat může pustit budoucí informace do tréninku a dát příliš optimistický výsledek.

## Poznámka Anki 1785269100050

Karty Anki: 1785269200050
GUID: 245f3a4fd637; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak probíhá **k-fold cross-validation**, jak se z ní vyberou hyperparametry a získá finální model?

### Odpověď (Back)

1. Data se rozdělí na k foldů.
2. Model se k-krát trénuje na k−1 foldech; každý fold je právě jednou validační.
3. CV chyba je **ê=(1/k)Σ<sub>j</sub>e<sub>j</sub>**.
4. Pro každou konfiguraci se spočítá průměrná validační chyba a vybere nejnižší.
5. Foldy vytvořily k pomocných modelů, nikoli finální model. Vybrané hyperparametry se proto zafixují a model se znovu natrénuje na celé dostupné trénovací množině.

## Poznámka Anki 1785269100051

Karty Anki: 1785269200051
GUID: 70d573e76b01; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak volba počtu foldů ovlivňuje náročnost křížové validace, co je **LOOCV** a co CV chyba přibližně odhaduje?

### Odpověď (Back)

Běžně se používá **k=5 nebo 10**. Při **leave-one-out CV** je k=N: model se N-krát trénuje na všech vzorcích kromě jednoho a hodnotí na vynechaném.

Větší k znamená více trénování a vyšší náklady; u drahých modelů či velkých dat proto může být CV nepřijatelná a jediný validační split praktičtější. Pro fixní modelovací proceduru CV chyba přibližně odhaduje její očekávaný výkon na nových datech při trénování na podobně velkých náhodných množinách.

## Poznámka Anki 1785269100052

Karty Anki: 1785269200052
GUID: 803048412598; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak funguje **nested cross-validation**, co odhaduje a jak se liší od hold-out testu?

### Odpověď (Back)

- **Vnitřní CV** na trénovací části vnějšího foldu vybírá hyperparametry či třídu modelu.
- **Vnější CV** hodnotí výsledek na datech nepoužitých ani k tréninku, ani vnitřnímu výběru.

Vnější chyba odhaduje očekávanou výkonnost **celé procedury výběru a trénování**, ne chybu jednoho konkrétního modelu. V jednotlivých foldech vznikají různé modely; pro nasazení se procedura znovu spustí na všech datech.

**Hold-out** naproti tomu hodnotí jeden konkrétní již natrénovaný model.

## Poznámka Anki 1785269100053

Karty Anki: 1785269200053
GUID: bd9f9cfb88c8; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Proč po ukončení evaluace někdy přetrénovat produkční model na **všech datech** a jaký to má důsledek pro jeho ohodnocení?

### Odpověď (Back)

Model využije více informací a může predikovat lépe než model trénovaný jen na části dat. Po zahrnutí všech dat však nezůstane nezávislá množina pro přímé změření chyby tohoto konkrétního produkčního modelu; spoléháme proto na odhad získaný předchozí korektní evaluační procedurou.

## Poznámka Anki 1785269100054

Karty Anki: 1785269200054
GUID: e6e20002613e; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Porovnej regresní metriky **MSE, RMSE a MAE**: vzorce, jednotky a citlivost na odlehlé hodnoty.

### Odpověď (Back)

| Metrika | Definice a vlastnosti | 
| MSE | (1/N)Σ(Y−Ŷ)². Kvadraticky zdůrazňuje velké chyby; jediný odlehlý reziduál může převážit mnoho běžných. Jednotky jsou umocněné na druhou. | 
| RMSE | √MSE. Má stejné jednotky jako Y. Odmocnina je rostoucí, takže pořadí modelů proti MSE nezmění. | 
| MAE | (1/N)Σ|Y−Ŷ|. Chyby započítává lineárně, proto je vůči odlehlým hodnotám robustnější než MSE. |

## Poznámka Anki 1785269100055

Karty Anki: 1785269200055
GUID: 02e4eb7185ce; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak je v materiálu definována **RMSLE** a jaký typ chyby zdůrazňuje?

### Odpověď (Back)

**RMSLE=√[(1/N)Σ(log Y<sub>i</sub>−log Ŷ<sub>i</sub>)²]**, přičemž logaritmy musí být definovány.

Soustředí se na relativní či poměrové rozdíly: stejný násobný omyl má podobný význam u malých i velkých hodnot. Logaritmus stlačuje velké hodnoty, takže je RMSLE vůči nim méně citlivá než RMSE.

## Poznámka Anki 1785269100056

Karty Anki: 1785269200056
GUID: de8b3a0f4c60; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak je definován a interpretován koeficient determinace **R²**?

### Odpověď (Back)

**R²=1−RSS/SST**, kde:

- **RSS=Σ(Y<sub>i</sub>−Ŷ<sub>i</sub>)²**: nevysvětlená kvadratická variabilita po použití modelu;
- **SST=Σ(Y<sub>i</sub>−Ȳ)²**: celková variabilita cíle kolem průměru.

**R²=1**: dokonalé predikce, RSS=0. **R²=0**: stejná kvadratická chyba jako konstantní predikce průměrem. **R²<0**: model je horší než tato průměrová baseline.

## Poznámka Anki 1785269100057

Karty Anki: 1785269200057
GUID: 7249f2c6a7da; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Co je **matice záměn**, co znamenají TP/FP/FN/TN a jaké základní součty z ní získáme?

### Odpověď (Back)

Je to tabulka četností skutečných a predikovaných tříd; oproti samotné ztrátě přímo ukazuje druhy rozhodnutí.

|  | Ŷ=1 | Ŷ=0 | 
| Y=1 | **TP**: správně pozitivní | **FN**: chybně negativní | 
| Y=0 | **FP**: chybně pozitivní | **TN**: správně negativní | 

- N=TP+FP+FN+TN
- skutečně pozitivní N<sub>+</sub>=TP+FN; skutečně negativní N<sub>−</sub>=FP+TN
- predikovaně pozitivní N̂<sub>+</sub>=TP+FP; predikovaně negativní N̂<sub>−</sub>=FN+TN

Dokonalý klasifikátor má FP=FN=0, tedy jen diagonálu TP/TN.

## Poznámka Anki 1785269100058

Karty Anki: 1785269200058
GUID: 851830d687e5; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak jsou definovány **TPR** a **FNR**, jak se interpretují a jaké mají další názvy?

### Odpověď (Back)

- **TPR=TP/(TP+FN)=TP/N<sub>+</sub>=P̂(Ŷ=1|Y=1)**: pravděpodobnost zachycení pozitivního případu. Také senzitivita, recall, hit rate.
- **FNR=FN/(TP+FN)=FN/N<sub>+</sub>**: podíl nezachycených pozitivních. Také miss rate, míra chyby II. druhu.

Obě podmiňují skutečně pozitivními a platí **TPR+FNR=1**.

## Poznámka Anki 1785269100059

Karty Anki: 1785269200059
GUID: 750da103b0b0; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak jsou definovány **TNR** a **FPR**, jak se interpretují a jaké mají další názvy?

### Odpověď (Back)

- **TNR=TN/(FP+TN)=TN/N<sub>−</sub>=P̂(Ŷ=0|Y=0)**: pravděpodobnost správného zamítnutí negativního. Také specificita, selektivita.
- **FPR=FP/(FP+TN)=FP/N<sub>−</sub>**: podíl falešných poplachů mezi negativními. Také false alarm rate, míra chyby I. druhu.

Obě podmiňují skutečně negativními a platí **TNR+FPR=1**.

## Poznámka Anki 1785269100060

Karty Anki: 1785269200060
GUID: d4de0b69fc0c; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak je definována **precision** a jaký je zásadní rozdíl mezi precision a recall?

### Odpověď (Back)

**Precision = PPV = TP/(TP+FP)=TP/N̂<sub>+</sub>=P̂(Y=1|Ŷ=1)**: podíl skutečně pozitivních mezi pozitivními predikcemi.

**Recall** podmiňuje skutečně pozitivními (kolik pozitivních jsme zachytili), zatímco **precision** podmiňuje predikovaně pozitivními (kolik poplachů bylo správných).

## Poznámka Anki 1785269100061

Karty Anki: 1785269200061
GUID: de85e032fea8; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak je definována **accuracy** a proč může být zavádějící u nevyvážených tříd?

### Odpověď (Back)

**ACC=(TP+TN)/N=P̂(Ŷ=Y)**: podíl správně klasifikovaných případů.

U vzácné pozitivní třídy může vysokou accuracy získat neužitečný model predikující jen majoritní třídu. Je-li např. 99 % případů negativních, stálá predikce 0 dosáhne 99% accuracy, ale **TPR=0** a nezachytí žádný pozitivní případ.

## Poznámka Anki 1785269100062

Karty Anki: 1785269200062
GUID: eab228ec8fb8; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jak je definováno **F1 skóre**, proč používá harmonický průměr a co nezohledňuje?

### Odpověď (Back)

**F1=2·precision·recall/(precision+recall)**.

Harmonický průměr zůstává nízký, je-li nízká kterákoli složka, takže vyžaduje současně dobrou precision i recall. Hodí se pro nevyvážené úlohy se vzácnou pozitivní třídou, chceme-li vyvažovat falešné poplachy a nezachycené pozitivní. Přímo však **nezohledňuje TN**.

## Poznámka Anki 1785269100063

Karty Anki: 1785269200063
GUID: 8c7714e25d9c; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Co je rozhodovací práh **τ** a jak jeho změna ovlivňuje pozitivní predikce, TPR a FPR?

### Odpověď (Back)

**Ŷ<sub>τ</sub>=1, pokud p̂(X)>τ**, jinak 0. τ=0,5 odpovídá volbě třídy s vyšší odhadnutou pravděpodobností.

- **Zvýšení τ:** méně (nikdy více) pozitivních predikcí; TPR i FPR jsou nerostoucí.
- **Snížení τ:** více zachycených pozitivních (vyšší TPR), ale typicky i více falešných poplachů (vyšší FPR).

Práh tedy řídí kompromis mezi záchytem a falešnými poplachy.

## Poznámka Anki 1785269100064

Karty Anki: 1785269200064
GUID: f1dfc267adaa; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Co je **ROC křivka** a jak interpretovat její body, extrémy, ideální roh a diagonálu?

### Odpověď (Back)

ROC vykresluje **TPR proti FPR** při změně prahu; každý τ dává bod (FPR<sub>τ</sub>,TPR<sub>τ</sub>).

- Velmi vysoký práh → přibližně (0,0).
- Velmi nízký práh → přibližně (1,1).
- Ideál je levý horní roh (0,1): žádné FP a všechny pozitivní zachyceny.
- Diagonála TPR≈FPR odpovídá náhodnému pořadí.

Kvalitní model rychle stoupá k levému hornímu rohu: vysoký TPR při nízkém FPR.

## Poznámka Anki 1785269100065

Karty Anki: 1785269200065
GUID: 949b7c81a5ba; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Co je **ROC-AUC**, jaké hodnoty mají ideální a náhodný klasifikátor a jak se liší od accuracy?

### Odpověď (Back)

**AUC** je plocha pod ROC křivkou a souhrnně hodnotí kvalitu pořadí napříč všemi uvažovanými prahy. Ideální klasifikátor má **AUC=1**, náhodný **AUC=0,5**.

**Accuracy** hodnotí konkrétní binární rozhodnutí při jednom zvoleném prahu; ROC-AUC není vázána na jediný práh a shrnuje rozlišovací schopnost modelu přes prahy.

## Poznámka Anki 1785269100066

Karty Anki: 1785269200066
GUID: d2c2cf5bbdcd; štítky: 03_Evaluace_modelu BI-ML1 konsolidace.

### Otázka (Front)

Jaký jednotný rámec spojuje **trénování, výběr a finální ohodnocení** modelu?

### Odpověď (Back)

1. **Trénovací data:** učení parametrů.
2. **Validační data nebo cross-validation:** výběr hyperparametrů a třídy modelu.
3. **Nezávislá testovací data:** až závěrečný odhad výkonu vybraného modelu.

