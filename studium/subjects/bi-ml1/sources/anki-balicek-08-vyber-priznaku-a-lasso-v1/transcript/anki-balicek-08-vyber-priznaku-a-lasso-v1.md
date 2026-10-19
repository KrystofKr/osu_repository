# BI-ML1 – 08 Vyber priznaku a Lasso

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::3 BI-ML1::08 Vyber priznaku a Lasso
Rozsah: 23 poznámek, 23 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785269100153

Karty Anki: 1785269200153
GUID: b96f84dac8b1; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Co je **výběr příznaků**, jak se liší od redukce dimenzionality a co jsou nerelevantní a redundantní příznaky?

### Odpověď (Back)

Feature selection je předzpracování, které ponechá podmnožinu **původních** příznaků; redukce dimenzionality často vytváří nové transformované příznaky.

- **Nerelevantní:** nenese užitečnou informaci o cíli. V konečném vzorku může náhodně působit užitečně, zvýšit variance a přeučení.
- **Redundantní:** jeho informace je už obsažena v jiných; v lineární regresi může způsobit kolinearitu, nestabilní či nejednoznačné koeficienty.

## Poznámka Anki 1785269100154

Karty Anki: 1785269200154
GUID: a60fb52ee887; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jaké hlavní výhody přináší **výběr příznaků**?

### Odpověď (Back)

- Snižuje dimenzi, řídnutí dat a zlepšuje informativnost vzdáleností; zvlášť důležité pro kNN.
- Zlepšuje interpretovatelnost: je zřetelnější, jaké vstupy model používá.
- Snižuje paměťové a výpočetní nároky a obvykle zrychlí trénink i predikci.

## Poznámka Anki 1785269100155

Karty Anki: 1785269200155
GUID: 178131971dbe; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Porovnej **filter, wrapper a embedded** metody výběru příznaků a supervizované/nesupervizované filtry.

### Odpověď (Back)

| Filter | Statisticky hodnotí data odděleně od cílového predikčního modelu. Nesupervizovaný sleduje např. rozptyl, missingy a redundanci; supervizovaný vztah příznaku k Y. | 
| Wrapper | Opakovaně trénuje pomocný model a hodnotí kandidátní podmnožiny podle jeho výkonu. | 
| Embedded | Výběr je přímo součástí optimalizace cílového modelu. | 

Wrapper tedy na rozdíl od filtru zohledňuje konkrétní model, ale oproti embedded výběru vyžaduje mnoho samostatných trénování.

## Poznámka Anki 1785269100156

Karty Anki: 1785269200156
GUID: b32f15577942; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jak fungují jednoduché **nesupervizované filtry** podle rozptylu, missingů a korelace mezi příznaky a jaká mají omezení?

### Odpověď (Back)

- Téměř konstantní příznak s velmi nízkou variancí obvykle nerozlišuje objekty; nenulová variance však sama nedokazuje predikční užitečnost.
- Příznak s mnoha missingy nese málo spolehlivě pozorované informace a imputace může být nejistá.
- Ze silně korelované dvojice lze jeden odstranit kvůli redundanci a kolinearitě.

Vysoká korelace ale nemusí znamenat úplnou zaměnitelnost: příznaky se mohou lišit nelineárními vztahy, interakcemi, dostupností či robustností vůči šumu.

## Poznámka Anki 1785269100157

Karty Anki: 1785269200157
GUID: f09b7786fcb7; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jak lze příznaky filtrovat podle vztahu k cíli pomocí **korelace, t-testu a χ² testu** a jaká jsou omezení?

### Odpověď (Back)

- **Spojitý X a spojitý Y:** slabá lineární korelace může označit kandidáta k odstranění, ale přehlédne nelinearitu či interakce.
- **Binární X, spojitý Y:** dvouvýběrový t-test porovná střední Y ve dvou skupinách. Vysoké p jen znamená nedostatek důkazu daného rozdílu, ne důkaz irelevance.
- **Diskrétní X a Y:** χ² test s H<sub>0</sub> o nezávislosti. Vysoké p opět pouze neprokazuje vztah v daných datech/testu.

## Poznámka Anki 1785269100158

Karty Anki: 1785269200158
GUID: c254aa5d2229; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jaké dvě obecné slabiny mají **supervizované filtrační metody** při mnoha příznacích?

### Odpověď (Back)

- **Vícenásobné testování:** s počtem jednotlivých testů roste pravděpodobnost náhodně významných výsledků.
- **Ignorování modelové struktury:** samostatné hodnocení příznaků nemusí zachytit interakce a kombinace, které konkrétní model využije, takže filtr nemusí dát nejlepší podmnožinu.

## Poznámka Anki 1785269100159

Karty Anki: 1785269200159
GUID: 9a2c30f24adb; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jak fungují **wrapper metody**, jaké mají výhody, rizika a výpočetní problém?

### Odpověď (Back)

Pro kandidátní podmnožiny opakovaně natrénují pomocný model, změří **validační/CV výkon** a vyberou nejlepší; trénovací chyba by zvýhodnila větší podmnožiny a přeučení.

- **Výhoda:** hledají příznaky přímo pro konkrétní model a metriku; výsledek je proto modelově specifický.
- **Riziko:** mnoho porovnání může přeučit výběr i na validační data.
- **Náklady:** p příznaků má 2<sup>p</sup> podmnožin, takže úplné prohledání je exponenciální; používají se hladové heuristiky.

## Poznámka Anki 1785269100160

Karty Anki: 1785269200160
GUID: 691774215cf3; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jak funguje **forward selection** a proč nemusí najít globálně nejlepší podmnožinu?

### Odpověď (Back)

Začne prázdnou množinou. Nejprve samostatně vyhodnotí kandidáty na první příznak; potom ke stávající množině zkouší každý dosud nevybraný a ponechá nejlepší rozšíření. Skončí při cílovém počtu nebo nedostatečném zlepšení.

Je hladový a dříve přidané příznaky obvykle neodebírá, takže lokálně výhodná volba může zablokovat lepší pozdější kombinaci.

## Poznámka Anki 1785269100161

Karty Anki: 1785269200161
GUID: 8ffdd577b681; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jak funguje **backward selection** a jak se liší od forward selection?

### Odpověď (Back)

Začne všemi příznaky; v každém kroku zkusí samostatně odstranit každý aktuální příznak a provede nejvýhodnější odstranění. Končí při cílovém počtu nebo nepřijatelném dalším zhoršení. Musí být možné natrénovat model už na úplné množině.

Forward začíná prázdnou, backward plnou množinou. Jde o různé hladové cesty, takže nemusí skončit stejně.

## Poznámka Anki 1785269100162

Karty Anki: 1785269200162
GUID: 6b7bcf2b9299; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Co je **RFE**, jak hodnotí důležitost a jak se liší od klasického backward selection?

### Odpověď (Back)

Recursive Feature Elimination opakovaně natrénuje model, odstraní nejméně důležitý příznak podle jeho vnitřního skóre a model přetrénuje, protože důležitosti se po odstranění mění.

- Vyžaduje model se smysluplnou feature importance.
- Lineární/logistický model: např. |standardizovaného koeficientu|; bez standardizace velikost závisí na jednotkách.
- Strom: např. celkový pokles nečistoty způsobený příznakem.

Backward samostatně vyhodnotí odstranění každého kandidáta; RFE použije importance z jednoho modelu v daném kroku.

## Poznámka Anki 1785269100163

Karty Anki: 1785269200163
GUID: 013c1ebbc7ed; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Co je **embedded výběr** a jak se projeví u lineárních modelů?

### Odpověď (Back)

Výběr vzniká přímo optimalizací cílového modelu. U lineárního modelu se některé koeficienty stanou přesně nulovými a vybrané jsou příznaky s nenulovými koeficienty. Typický regresní příklad je **Lasso**; pro binární klasifikaci logistická regrese s L1 penalizací.

## Poznámka Anki 1785269100164

Karty Anki: 1785269200164
GUID: c5d2a68b4193; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Co znamená **Lasso**, jakou má účelovou funkci a jak λ vytváří sparse řešení?

### Odpověď (Back)

**Lasso = Least Absolute Shrinkage and Selection Operator**:

**‖Y−Xw‖²+λΣ<sub>j=1</sub><sup>p</sup>|w<sub>j</sub>|**,

intercept se nepenalizuje. Jde o L1 regularizaci; λ=0 dává OLS. Rostoucí λ silněji stahuje koeficienty a více z nich nastaví přesně na nulu. **Sparse** vektor má mnoho nulových složek, takže příslušné příznaky jsou odstraněny. Ridge koeficienty typicky jen zmenšuje, nikoli přesně nuluje.

## Poznámka Anki 1785269100165

Karty Anki: 1785269200165
GUID: e8f3e652d455; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Proč Lasso nemá stejný uzavřený vzorec jako Ridge a jak se numericky optimalizuje?

### Odpověď (Back)

|w<sub>j</sub>| není diferencovatelná v nule, takže nelze jednoduše zopakovat hladké maticové odvození Ridge. Lasso se řeší iterativně, např. subgradientními metodami nebo souřadnicovou optimalizací; nediferencovatelnost neznamená, že optimalizace není možná.

## Poznámka Anki 1785269100166

Karty Anki: 1785269200166
GUID: fc952fbca0dc; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jaká je **vázaná a geometrická interpretace** Lassa a Ridge a proč L1 podporuje nulové koeficienty?

### Odpověď (Back)

Penalizovaným úlohám odpovídá minimalizace RSS při omezení:

- **Lasso:** Σ|w<sub>j</sub>|≤B — ve 2D kosočtverec (L1 koule).
- **Ridge:** Σw<sub>j</sub>²≤B — ve 2D kruh (L2 koule).

L1 oblast má rohy na souřadnicových osách; vrstevnice RSS se jí často poprvé dotkne v rohu, takže některá souřadnice je přesně 0. Hladká L2 hranice rohy nemá a přesné nuly zvýhodňuje méně.

## Poznámka Anki 1785269100167

Karty Anki: 1785269200167
GUID: 68b47b9b1f67; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jak Lasso řídí kompromis **fit–generalizace**, jak vybrat λ a proč standardizovat příznaky?

### Odpověď (Back)

Regularizace přijme vyšší trénovací RSS za menší/stabilnější koeficienty. Lasso může snížit variance a přeučení, ale příliš velké λ vynuluje i relevantní vstupy a zvýší bias.

λ vybíráme validací nebo CV, ne minimem trénovacího RSS (to preferuje λ=0). Příznaky obvykle standardizujeme, protože velikost koeficientu závisí na měřítku; průměr a směrodatná odchylka se odhadují pouze z trénovací části daného splitu/foldu.

## Poznámka Anki 1785269100168

Karty Anki: 1785269200168
GUID: c8d97ec6e4c7; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jak vypadají **OLS a Ridge koeficienty při ortonormálních příznacích** XᵀX=I?

### Odpověď (Back)

XᵀX=I znamená ortonormální sloupce.

- **OLS:** ŵ<sub>OLS</sub>=XᵀY.
- **Ridge:** ŵ<sub>Ridge,j</sub>=ŵ<sub>OLS,j</sub>/(1+λ).

Ridge tedy všechny neinterceptové koeficienty plynule násobí stejným faktorem 1/(1+λ).

## Poznámka Anki 1785269100169

Karty Anki: 1785269200169
GUID: 920aaf5ecdc5; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Co je **soft thresholding** Lassa při XᵀX=I a jak ukazuje rozdíl proti Ridge?

### Odpověď (Back)

V použitém škálování:

**ŵ<sub>Lasso,j</sub>=sgn(ŵ<sub>OLS,j</sub>)·max(0,|ŵ<sub>OLS,j</sub>|−λ/2)**.

- |ŵ<sub>OLS,j</sub>|≤λ/2 → přesně 0.
- Větší kladný koeficient se zmenší o λ/2.
- Větší záporný se posune o λ/2 k nule a zůstane záporný.

Přesný práh se mezi zdroji liší podle faktorů 1/2, 1/N apod. před RSS. Ridge zmenšuje plynule všechny; Lasso navíc vynuluje ty pod prahem.

## Poznámka Anki 1785269100170

Karty Anki: 1785269200170
GUID: 3b87b2e756d0; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jak přidat L1 penalizaci k logistické regresi a jak se Lasso a Ridge chovají ke **kolineárním příznakům**?

### Odpověď (Back)

K záporné log-věrohodnosti/binární cross-entropy se přičte **λΣ|w<sub>j</sub>|** a celek se minimalizuje.

Při silné kolinearitě může Lasso arbitrárně ponechat jeden podobný příznak a ostatní vynulovat; volba může být mezi výběry nestabilní a vybraný příznak nemusí být v budoucnu stejně spolehlivý. Ridge spíše rozdělí vliv mezi více korelovaných příznaků.

## Poznámka Anki 1785269100171

Karty Anki: 1785269200171
GUID: c89695125ce1; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Co je **Elastic Net** a kdy je vhodnější než čisté Lasso?

### Odpověď (Back)

Kombinuje L1 a L2 penalizaci:

**λ<sub>1</sub>Σ|w<sub>j</sub>|+λ<sub>2</sub>Σw<sub>j</sub>²**.

Z Lassa přebírá sparse modely s přesnými nulami; z Ridge stabilnější práci s kolinearitou a tendenci ponechávat skupiny souvisejících příznaků. Hodí se pro mnoho příznaků se silně korelovanými skupinami.

## Poznámka Anki 1785269100172

Karty Anki: 1785269200172
GUID: 159eb0c775d7; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jak se výběr pomocí Lassa liší od **forward selection a RFE** a jak jej rozšířit na nelineární vztahy?

### Odpověď (Back)

- **Lasso:** společná penalizovaná optimalizace vytváří nulové koeficienty.
- **Forward:** přidává příznaky po jednom podle validačního výkonu.
- **RFE:** opakovaně odstraňuje podle importance modelu.

Lasso posuzuje užitečnost v rámci lineárního vztahu ve zvolených příznacích. Pro nelinearitu nejprve vytvoříme bázové funkce a L1 aplikujeme na jejich koeficienty. Velké množství bází ale zvyšuje náklady a náhodné vztahy, proto je nutná pečlivá validace λ.

## Poznámka Anki 1785269100173

Karty Anki: 1785269200173
GUID: 557ba8f8600c; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jak zabránit **data leakage** při výběru příznaků a cross-validation?

### Odpověď (Back)

Celý výběr je součást modelovací procedury a smí používat jen trénovací data; test nesmí ovlivnit rozhodnutí. Výběr před splitem přenese informace z validace/testu do vstupů modelu a optimisticky zkreslí evaluaci.

V CV se výběr provede znovu **uvnitř každého trénovacího foldu** a výsledná transformace se aplikuje na jeho validační fold. Jednorázový výběr na celém datasetu před CV už validační foldy kontaminuje.

## Poznámka Anki 1785269100174

Karty Anki: 1785269200174
GUID: 92f3c501cf15; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jaký celkový kompromis řeší feature selection a jaká hierarchie spojuje **filtry, wrappery a embedded** metody?

### Odpověď (Back)

Hledá kompromis mezi zachováním predikční informace a odstraněním dimenze, šumu, redundance a výpočetní složitosti.

- **Filter:** hodnotí data před modelem.
- **Wrapper:** hodnotí podmnožiny opakovaným trénováním modelu.
- **Embedded:** výběr je přímo součástí optimalizace modelu.

## Poznámka Anki 1785269100175

Karty Anki: 1785269200175
GUID: eb409e28ab18; štítky: 08_Vyber_priznaku_a_Lasso BI-ML1 konsolidace.

### Otázka (Front)

Jaký meta-princip vysvětluje výběr příznaků pomocí **Lassa**?

### Odpověď (Back)

L1 penalizace změní geometrii optimalizace: přípustná oblast má rohy na souřadnicových osách, takže se jí vrstevnice chyby často dotkne právě tam. Optimální řešení proto často obsahuje **přesně nulové koeficienty**, které příznaky automaticky vyřadí.

