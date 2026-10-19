# BI-ML1 – 04 Linearni regrese a OLS

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::3 BI-ML1::04 Linearni regrese a OLS
Rozsah: 23 poznámek, 23 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785269100067

Karty Anki: 1785269200067
GUID: 266c0fd8d232; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Jaký model předpokládá **lineární regrese**, co představuje chyba ε a intercept w<sub>0</sub>?

### Odpověď (Back)

Jde o supervizovanou regresi spojitého cíle:

**Y=w<sub>0</sub>+w<sub>1</sub>x<sub>1</sub>+⋯+w<sub>p</sub>x<sub>p</sub>+ε**.

- **ε** obsahuje nevysvětlené vlivy, měřicí chyby, nekonzistence a další náhodnost; stejné X proto nemusí vždy dát stejné Y. Obvykle předpokládáme E[ε]=0.
- **w<sub>0</sub>** zachytí systematickou střední úroveň, aby chyba mohla mít nulový průměr. Je to očekávané Y při všech x<sub>j</sub>=0, ale pokud takový bod není věcně relevantní, nemusí mít praktickou interpretaci.

## Poznámka Anki 1785269100068

Karty Anki: 1785269200068
GUID: 53082f962937; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Jak se lineární regrese zapíše **vektorově** a co bodová predikce statisticky odhaduje?

### Odpověď (Back)

Přidáme x<sub>0</sub>=1:

- x=(1,x<sub>1</sub>,…,x<sub>p</sub>)ᵀ, w=(w<sub>0</sub>,…,w<sub>p</sub>)ᵀ;
- **Y=wᵀx+ε**;
- po odhadu parametrů **Ŷ=ŵᵀx**.

Při E[ε]=0 platí **E[Y|X=x]=wᵀx**. Predikce tedy odhaduje podmíněný průměr, nikoli náhodnou chybu konkrétního budoucího pozorování. Ani dokonale známé w nezaručí přesné jednotlivé Y, protože zůstává ε.

## Poznámka Anki 1785269100069

Karty Anki: 1785269200069
GUID: d9aa032966da; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Co znamená **linearita vůči koeficientům** a jak se interpretuje koeficient w<sub>j</sub>?

### Odpověď (Back)

Predikce je lineární kombinací neznámých koeficientů a každý w<sub>j</sub> vstupuje v první mocnině.

Zvýší-li se x<sub>j</sub> o jednotku a **ostatní příznaky zůstanou stejné**, podmíněná střední hodnota Y se změní o w<sub>j</sub>. Podmínka fixace ostatních vstupů je nutná, protože jde o parciální vztah daného příznaku s predikcí.

## Poznámka Anki 1785269100070

Karty Anki: 1785269200070
GUID: 85c65aba9b17; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Jak souvisejí **ztráta, náhodná chyba, reziduum a RSS** v lineární regresi?

### Odpověď (Back)

- **Ztráta L(Y,Ŷ)** je nezáporná závažnost chyby; pro nejmenší čtverce se používá (Y−Ŷ)².
- Chyby se agregují přes celou trénovací množinu, neoptimalizuje se jediný bod.
- **Reziduum r<sub>i</sub>=Y<sub>i</sub>−wᵀx<sub>i</sub>** je pozorovaný rozdíl pro zvolené/odhadnuté parametry; **ε<sub>i</sub>** je nepozorovaná chyba skutečného generujícího modelu.
- **RSS(w)=Σ<sub>i=1</sub><sup>N</sup>(Y<sub>i</sub>−wᵀx<sub>i</sub>)²** měří celkovou kvadratickou neshodu na tréninku.

## Poznámka Anki 1785269100071

Karty Anki: 1785269200071
GUID: 61074a24633e; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Co je **OLS** a jak se formálně zapisuje odhad parametrů?

### Odpověď (Back)

**OLS = Ordinary Least Squares**, obyčejná metoda nejmenších čtverců. Odhaduje koeficienty minimalizací RSS:

**ŵ<sub>OLS</sub> ∈ arg min<sub>w</sub> RSS(w)**.

Jde o optimalizaci funkce vektorové proměnné, protože RSS současně závisí na p+1 koeficientech w<sub>0</sub>,…,w<sub>p</sub>.

## Poznámka Anki 1785269100072

Karty Anki: 1785269200072
GUID: f0abaa010edb; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Co je **parciální derivace** a **gradient** a jaký mají geometrický význam?

### Odpověď (Back)

- **Parciální derivace** mění jednu proměnnou a ostatní drží konstantní; obyčejná derivace je pro funkci jedné proměnné.
- Pro f:R<sup>d</sup>→R je **∇f=(∂f/∂x<sub>1</sub>,…,∂f/∂x<sub>d</sub>)ᵀ**.
- Gradient ukazuje směr nejrychlejšího lokálního růstu a je-li nenulový, je kolmý k vrstevnici procházející bodem.

## Poznámka Anki 1785269100073

Karty Anki: 1785269200073
GUID: a0b39111bbe0; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Co je **stacionární bod** a proč nulový gradient sám nepotvrzuje minimum?

### Odpověď (Back)

Stacionární bod x* splňuje **∇f(x*)=0**. Nulový gradient je nutnou podmínkou vnitřního lokálního extrému diferencovatelné funkce, ale stacionární bod může být minimum, maximum i sedlový bod. K rozlišení potřebujeme informaci o zakřivení, typicky Hessovu matici.

## Poznámka Anki 1785269100074

Karty Anki: 1785269200074
GUID: 41431d466804; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Co je **Hessova matice**, pozitivní definitnost a semidefinitnost a jak klasifikují stacionární bod?

### Odpověď (Back)

Hessián je čtvercová matice všech druhých parciálních derivací a popisuje lokální zakřivení.

- **Pozitivně definitní H:** sᵀHs>0 pro každé s≠0. Je-li navíc ∇f(x*)=0, jde o ostré lokální minimum.
- **Pozitivně semidefinitní H:** sᵀHs≥0 pro každé s. Za vhodných podmínek na okolí podporuje závěr o neostrém lokálním minimu.

## Poznámka Anki 1785269100075

Karty Anki: 1785269200075
GUID: e7a7e147031d; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Urči gradient, Hessián a minimum funkce **f(x,y)=x²+y²**.

### Odpověď (Back)

**∇f(x,y)=(2x,2y)ᵀ** a **H<sub>f</sub>=2I**. V počátku je gradient nulový a Hessián 2I je pozitivně definitní, takže (0,0) je ostré minimum.

## Poznámka Anki 1785269100076

Karty Anki: 1785269200076
GUID: 24c24b1e692a; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Jak se trénovací lineární regrese zapíše pomocí **návrhové matice X** a jaké mají objekty rozměry?

### Odpověď (Back)

Pro N dvojic (Y<sub>i</sub>,x<sub>i</sub>) s interceptem:

- **X∈R<sup>N×(p+1)</sup>**; řádek i je x<sub>i</sub>ᵀ=(1,x<sub>i1</sub>,…,x<sub>ip</sub>) a první sloupec tvoří jedničky;
- **Y∈R<sup>N</sup>** je sloupcový vektor cílů;
- **w∈R<sup>p+1</sup>** je sloupcový vektor parametrů;
- **Y=Xw+ε**; Xw je vektor modelových středních hodnot/predikcí pro všechny trénovací vstupy.

## Poznámka Anki 1785269100077

Karty Anki: 1785269200077
GUID: 3b9c9a37a18f; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Jak se RSS zapíše pomocí **eukleidovské normy** a proč tento zápis platí?

### Odpověď (Back)

**RSS(w)=‖Y−Xw‖²**. Vektor Y−Xw obsahuje jednotlivá rezidua a druhá mocnina eukleidovské normy je součet čtverců jeho složek.

## Poznámka Anki 1785269100078

Karty Anki: 1785269200078
GUID: f3c21e021831; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Jak se z gradientu RSS odvodí **normální rovnice**?

### Odpověď (Back)

**∇RSS(w)=−2Xᵀ(Y−Xw)=−2XᵀY+2XᵀXw**.

Položením gradientu na nulu dostaneme **XᵀXw=XᵀY**. Nazývá se normální rovnice a je podmínkou prvního řádu charakterizující řešení nejmenších čtverců.

## Poznámka Anki 1785269100079

Karty Anki: 1785269200079
GUID: 4ee86f7c30c2; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Jaký je Hessián RSS a proč z něj plyne **konvexita** a globální optimalita řešení normální rovnice?

### Odpověď (Back)

**H<sub>RSS</sub>=2XᵀX** a nezávisí na w. Pro každý s:

**sᵀXᵀXs=‖Xs‖²≥0**,

takže XᵀX je pozitivně semidefinitní a RSS je konvexní kvadratická funkce. Každý její stacionární bod, tedy každé řešení normální rovnice, je proto globálním minimem; nemůže jít o neglobální lokální minimum.

## Poznámka Anki 1785269100080

Karty Anki: 1785269200080
GUID: fa636698436e; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Kdy má OLS **jednoznačné uzavřené řešení** a jak se z něj predikuje nový bod?

### Odpověď (Back)

Je-li **XᵀX regulární** (má inverzi a triviální nulový prostor), normální rovnice má jediné řešení:

**ŵ<sub>OLS</sub>=(XᵀX)<sup>−1</sup>XᵀY**.

Pro nový x: **Ŷ=xᵀŵ<sub>OLS</sub>=xᵀ(XᵀX)<sup>−1</sup>XᵀY**. Regularita znamená, že pro s≠0 není Xs=0, takže Hessián je pozitivně definitní, RSS má jediné ostré minimum a koeficienty i predikční funkce jsou jednoznačné.

## Poznámka Anki 1785269100081

Karty Anki: 1785269200081
GUID: 5ab4a8c29470; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Jaké jsou čtyři hlavní kroky **metody nejmenších čtverců**?

### Odpověď (Back)

1. Zapsat model **Y=Xw+ε**.
2. Definovat **RSS=‖Y−Xw‖²**.
3. Odvodit normální rovnici **XᵀXw=XᵀY**.
4. Vyřešit ji pro ŵ.

## Poznámka Anki 1785269100082

Karty Anki: 1785269200082
GUID: 783bd83417b0; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Proč mají minimalizace **RSS a MSE** stejné řešení a jak kvadratická ztráta zvýrazňuje velká rezidua?

### Odpověď (Back)

**MSE=RSS/N**; dělení kladnou konstantou N nemění polohu minima. Reziduum se umocňuje, takže např. dvojnásobná velikost chyby znamená čtyřnásobnou ztrátu.

## Poznámka Anki 1785269100083

Karty Anki: 1785269200083
GUID: 363ce9869df0; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Jak se liší skutečné koeficienty **w** a odhad **ŵ** a proč je ŵ náhodný?

### Odpověď (Back)

**w** jsou neznámé parametry datového mechanismu; **ŵ** jsou hodnoty vypočtené z konkrétní trénovací množiny. I při deterministickém výpočetním vzorci je ŵ náhodná veličina, protože závisí na náhodně získaných Y a případně i X.

## Poznámka Anki 1785269100084

Karty Anki: 1785269200084
GUID: 98142a74394e; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Proč je lineární regrese **parametrická metoda** a proč může být méně citlivá na vysokou dimenzi než kNN?

### Odpověď (Back)

Předem předpokládá konečněrozměrný tvar popsaný **p+1 koeficienty** pro p příznaků a intercept. Na rozdíl od kNN nemusí hustě pokrýt celý vstupní prostor sousedy; odhaduje konečný počet globálních parametrů.

## Poznámka Anki 1785269100085

Karty Anki: 1785269200085
GUID: 0f7a3c0cda4e; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Kdy může p+1 bodů určit p+1 koeficientů a proč samotný počet vzorků nezaručuje jednoznačný OLS odhad?

### Odpověď (Back)

V ideálním bezchybném případě poskytne p+1 bodů p+1 rovnic pro p+1 neznámých, ale pouze pokud jsou lineárně nezávislé. Ani N≥p+1 nestačí, jestliže řádky nebo sloupce X zůstávají lineárně závislé; pak XᵀX nemusí být regulární.

## Poznámka Anki 1785269100086

Karty Anki: 1785269200086
GUID: f8335fa82f4f; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Jak **silná korelace příznaků** ovlivňuje OLS koeficienty a generalizaci?

### Odpověď (Back)

Sloupce X se mohou stát téměř lineárně závislými. Výpočet je pak numericky nestabilní a malé změny dat mohou vyvolat velké změny koeficientů. Model tak může silně reagovat na náhodné zvláštnosti tréninku, přeučit se a hůře predikovat nová data.

## Poznámka Anki 1785269100087

Karty Anki: 1785269200087
GUID: ca41cc5bc184; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Co lineární regrese modeluje z **diskriminativního pohledu** a proč tím neurčuje celé rozdělení Y|X=x?

### Odpověď (Back)

Přímo modeluje **podmíněnou střední hodnotu E[Y|X=x]=wᵀx**. Samotný vztah určuje jen průměr; tvar a variabilitu celého podmíněného rozdělení Y|X=x určí až další předpoklady o náhodné složce ε.

## Poznámka Anki 1785269100088

Karty Anki: 1785269200088
GUID: dd5e639eebbc; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Proč nízké **trénovací RSS** nezaručuje nízkou testovací chybu a jakou roli mají X a Y v OLS vzorci?

### Odpověď (Back)

RSS hodnotí přizpůsobení pouze na pozorovaných trénovacích bodech. Příliš mnoho nestabilních parametrů nebo nevhodné příznaky mohou zachytit šum a zhoršit budoucí predikce.

Ve vzorci **ŵ=(XᵀX)<sup>−1</sup>XᵀY** určuje X geometrii a hodnoty příznaků, zatímco Y obsahuje pozorované cíle, jimž se model přizpůsobuje.

## Poznámka Anki 1785269100089

Karty Anki: 1785269200089
GUID: 830e05168396; štítky: 04_Linearni_regrese_a_OLS BI-ML1 konsolidace.

### Otázka (Front)

Co platí při **singulární XᵀX**, jak se liší podmínka prvního a druhého řádu a jaká je hierarchie lineární regrese → ztráta → OLS?

### Odpověď (Back)

Je-li XᵀX pouze pozitivně semidefinitní, RSS zůstává konvexní, ale minimum nemusí být ostré ani reprezentované jediným vektorem koeficientů.

- **První řád:** nulový gradient určí kandidáty/řešení normální rovnice.
- **Druhý řád:** Hessián popíše zakřivení a rozhodne o typu minima a jeho ostrosti.

**Lineární regrese** určuje model Y=wᵀx+ε, **kvadratická ztráta** kritérium chyby a **OLS** je metoda odhadu w minimalizující toto kritérium.

