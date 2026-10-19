# Pravděpodobnost a statistika – Původní blok 06

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::Pravděpodobnost a statistika
Rozsah: 22 poznámek, 22 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783851674948

Karty Anki: 1783851674948
GUID: uIk8,6;IQ8; štítky: konsolidace::blok_6 model parametricka_trida statistika workflow.

### Otázka (Front)

Jak se liší pravděpodobnostní a statistický problém a jaký je základní postup statistického uvažování?

### Odpověď (Back)

**Teorie pravděpodobnosti** postupuje od známého modelu a jeho parametrů k predikci chování dat. **Matematická statistika** postupuje opačně: z pozorovaných dat volí model, odhaduje jeho parametry a ověřuje, zda je s daty slučitelný.

Základní postup:
1. pomocí povahy problému a dat zvolit rozumnou parametrickou rodinu **{F<sub>θ</sub>: θ∈Θ}**;
2. odhadnout její parametr θ bodově nebo intervalově;
3. ověřit tvar modelu testem dobré shody a konkrétní tvrzení o parametrech parametrickými testy.

Volbu modelu vedou zejména diskrétnost či spojitost, obor možných hodnot, tvar rozdělení a známé strukturální vlastnosti.

## Poznámka Anki 1783851674949

Karty Anki: 1783851674949
GUID: rX.s#=B8{Z; štítky: iid konsolidace::blok_6 nahodny_vyber realizace.

### Otázka (Front)

Co je náhodný výběr, jeho realizace a proč jsou důležité předpoklady i.i.d.?

### Odpověď (Back)

**Náhodný výběr z rozdělení F** je vektor X<sub>1</sub>,…,X<sub>n</sub> nezávislých a stejně rozdělených veličin s distribuční funkcí F; anglicky **i.i.d. sample** (independent and identically distributed).

Stejné rozdělení znamená, že všechna pozorování pocházejí ze stejného modelu. Nezávislost brání tomu, aby pozorování nesla redundantní informaci způsobenou vzájemnou závislostí.

**Realizace** je konkrétní pozorovaný vektor x<sub>1</sub>,…,x<sub>n</sub>. Náhodný výběr je tedy náhodný objekt před měřením, realizace jsou skutečná data. Příklady: opakovaná fyzikální měření, doby běhu algoritmu nebo výšky náhodně vybraných lidí.

## Poznámka Anki 1783851674950

Karty Anki: 1783851674950
GUID: O(=46a/@S%; štítky: bernoulli exponencialni konsolidace::blok_6 normalni parametricke_modely.

### Otázka (Front)

Jaké parametrické modely se přirozeně volí pro minci, čekací dobu a IQ a jaké mají parametry?

### Odpověď (Back)

• Hod neznámou mincí: **Bernoulliho rozdělení Be(p)**, p∈[0,1], kde p je pravděpodobnost úspěchu.
• Čas mezi příchozími požadavky: **exponenciální rozdělení Exp(λ)**, λ>0, kde λ je intenzita.
• IQ v populaci: **normální rozdělení N(μ,σ²)**, μ∈R, σ²>0.

Normální model má dvourozměrný parametr θ=(μ,σ²): μ určuje polohu a σ² variabilitu. Příklady ukazují, že parametr může být skalár i vektor.

## Poznámka Anki 1783851674951

Karty Anki: 1783851674951
GUID: c96N#F$KB^; štítky: histogram hustota konsolidace::blok_6 vizualizace.

### Otázka (Front)

Jak je definován normalizovaný histogram, proč má plochu 1 a jaká jsou jeho omezení?

### Odpověď (Back)

Rozsah dat se rozdělí do přihrádek. Má-li přihrádka šířku h a obsahuje m<sub>i</sub> z n pozorování, výška jejího sloupce je
**m<sub>i</sub>/(hn)**.
Jeho plocha je h·m<sub>i</sub>/(hn)=m<sub>i</sub>/n, takže celková plocha histogramu je 1. Histogram tak funguje jako grafický odhad hustoty a lze jej porovnávat s hustotami modelů.

Výsledek je citlivý na počet, šířku i umístění přihrádek: příliš mnoho přihrádek zvýrazní šum, příliš málo zakryje strukturu. V příkladu čekání na autobus histogram připomínal exponenciální rozdělení.

## Poznámka Anki 1783851674952

Karty Anki: 1783851674952
GUID: EoA}}0XiE); štítky: ecdf empiricka_distribucni_funkce konsolidace::blok_6 pravdepodobnost.

### Otázka (Front)

Co je empirická distribuční funkce, jak vypadá a jak se z ní odhadují pravděpodobnosti?

### Odpověď (Back)

Empirická distribuční funkce je
**F<sub>n</sub>(x)=(1/n)Σ<sub>i=1</sub><sup>n</sup>1<sub>{Xᵢ≤x}</sub>**.
Udává podíl pozorování nepřesahujících x, a proto přímo odhaduje P(X≤x). Je po částech konstantní a v každém pozorování má skok 1/n; při opakovaných hodnotách se příslušné skoky sečtou.

Na rozdíl od histogramu nepotřebuje volbu přihrádek, proto je stabilní a spolehlivou vizualizací rozdělení. V příkladu s čekáním na autobus bylo F<sub>n</sub>(6)=11/15≈0,733.

## Poznámka Anki 1783851674953

Karty Anki: 1783851674953
GUID: RhEzi9109F; štítky: ecdf konsolidace::blok_6 kvantily median.

### Otázka (Front)

Jak se z empirické distribuční funkce odhadují kvantily a medián?

### Odpověď (Back)

α-kvantil je hodnota, pod níž leží přibližně podíl α populace. Ze seřazených dat x<sub>(1)</sub>≤…≤x<sub>(n)</sub> se ve skriptech odhaduje jako
**x<sub>(⌈nα⌉)</sub>**.

Jde o inverzní čtení empirické distribuční funkce: hledáme nejmenší x, pro které F<sub>n</sub>(x)≥α. Pro liché n je medián prostřední hodnota x<sub>(⌈n/2⌉)</sub>; při sudém n software často používá průměr dvou prostředních hodnot.

V příkladu čekání na autobus vyšel medián 3,4 minuty: přibližně polovina čekání je kratší a polovina delší.

## Poznámka Anki 1783851674954

Karty Anki: 1783851674954
GUID: QKN=WsGU{|; štítky: bodovy_odhad konsolidace::blok_6 parametr statistika.

### Otázka (Front)

Co je statistika a bodový odhad a lze odhadovat i funkci parametru?

### Odpověď (Back)

**Statistika** je libovolná funkce náhodného výběru, která přímo nezávisí na neznámém parametru modelu. **Bodový odhad** parametru θ je statistika θ̂<sub>n</sub>(X<sub>1</sub>,…,X<sub>n</sub>) určená k odhadu θ.

Lze odhadovat i funkci g(θ): pro X∼Exp(λ) lze například odhadovat nejen λ, ale také g(λ)=1/λ=E[X]. Protože jsou odhady funkcemi náhodného výběru, jsou před pozorováním dat samy náhodnými veličinami.

## Poznámka Anki 1783851674955

Karty Anki: 1783851674955
GUID: e%MoSRrt*R; štítky: konsolidace::blok_6 momenty vyberovy_prumer vyberovy_rozptyl.

### Otázka (Front)

Jaké základní výběrové statistiky odhadují polohu, variabilitu a momenty?

### Odpověď (Back)

• **Výběrový průměr:** X̄<sub>n</sub>=(1/n)ΣX<sub>i</sub>, odhaduje E[X].
• **Výběrový rozptyl:** s<sub>n</sub>²=(1/(n−1))Σ(X<sub>i</sub>−X̄<sub>n</sub>)², odhaduje var(X). Jmenovatel n−1 zajišťuje nestrannost.
• **Výběrová směrodatná odchylka:** s<sub>n</sub>=√s<sub>n</sub>².
• **k-tý výběrový moment:** m<sub>k</sub>=(1/n)ΣX<sub>i</sub><sup>k</sup>, odhaduje E[X<sup>k</sup>].

## Poznámka Anki 1783851674956

Karty Anki: 1783851674956
GUID: Mw=QC6x*1`; štítky: konsolidace::blok_6 korelace vyberova_kovariance.

### Otázka (Front)

Jak jsou definovány výběrová kovariance a korelace a co odhadují?

### Odpověď (Back)

Pro párová data (X<sub>i</sub>,Y<sub>i</sub>) je výběrová kovariance
**s<sub>X,Y</sub>=(1/(n−1))Σ(X<sub>i</sub>−X̄)(Y<sub>i</sub>−Ȳ)**,
která odhaduje populační kovarianci.

Výběrový korelační koeficient je
**r=s<sub>X,Y</sub>/(s<sub>X</sub>s<sub>Y</sub>)**
a odhaduje populační korelaci. Kovariance zachovává jednotky a měřítko veličin, korelace je normalizovaná a bezrozměrná.

## Poznámka Anki 1783851674957

Karty Anki: 1783851674957
GUID: PV*XEoN0sf; štítky: konsolidace::blok_6 konzistence nestrannost odhad.

### Otázka (Front)

Jaký je rozdíl mezi nestranností a konzistencí odhadu a jaká podmínka zajišťuje konzistenci?

### Odpověď (Back)

Odhad θ̂<sub>n</sub> je **nestranný**, pokud E[θ̂<sub>n</sub>]=θ pro každé přípustné θ. Pro pevné n tedy nemá systematický posun.

Je **konzistentní**, pokud θ̂<sub>n</sub>→θ v pravděpodobnosti, tj. pro každé ε>0 platí
**P(|θ̂<sub>n</sub>−θ|≥ε)→0**.
Konzistence říká, že s rostoucím výběrem lze chybu učinit s vysokou pravděpodobností libovolně malou.

Postačující podmínka: jestliže **E[θ̂<sub>n</sub>]→θ** a **var(θ̂<sub>n</sub>)→0**, pak je odhad konzistentní. Nestrannost je vlastnost středu pro pevné n; konzistence je asymptotická vlastnost celé distribuce odhadu.

## Poznámka Anki 1783851674958

Karty Anki: 1783851674958
GUID: il+Io>ZfL=; štítky: konsolidace::blok_6 konzistence nestrannost vyberovy_prumer.

### Otázka (Front)

Proč je výběrový průměr nestranným a konzistentním odhadem střední hodnoty?

### Odpověď (Back)

Pro i.i.d. výběr s E[X<sub>i</sub>]=μ a var(X<sub>i</sub>)=σ² platí
**E[X̄<sub>n</sub>]=μ**, takže je výběrový průměr nestranný, a
**var(X̄<sub>n</sub>)=σ²/n→0**.

Konzistence plyne buď přímo ze slabého zákona velkých čísel, nebo z podmínky E[X̄<sub>n</sub>]=μ a var(X̄<sub>n</sub>)→0. Vztah σ²/n znamená, že s rostoucím n náhodné kolísání klesá a odhad je přesnější.

## Poznámka Anki 1783851674959

Karty Anki: 1783851674959
GUID: g$08q55,?#; štítky: besselova_korekce konsolidace::blok_6 nestrannost vyberovy_rozptyl.

### Otázka (Front)

Jaké jsou definice a dva algebraické tvary výběrového rozptylu a proč se dělí n−1?

### Odpověď (Back)

Výběrový rozptyl je
**s<sub>n</sub>²=(1/(n−1))Σ(X<sub>i</sub>−X̄<sub>n</sub>)²**.
Ekvivalentně
**s<sub>n</sub>²=(1/(n−1))(ΣX<sub>i</sub>²−nX̄<sub>n</sub>²)**.

Druhý tvar usnadňuje výpočty očekávané hodnoty. S využitím E[X<sub>i</sub>²]=σ²+μ² a E[X̄<sub>n</sub>²]=σ²/n+μ² dostaneme **E[s<sub>n</sub>²]=σ²**. Dělení n−1 je tedy Besselova korekce potřebná pro nestrannost; dělení n by rozptyl systematicky podhodnocovalo. Na rozdíl od průměru, u něhož přirozené dělení n nestrannost zachovává, se při odhadu rozptylu jeden stupeň volnosti spotřebuje odhadem X̄.

## Poznámka Anki 1783851674960

Karty Anki: 1783851674960
GUID: dM`sWc/fe:; štítky: konsolidace::blok_6 konzistence vyberovy_rozptyl.

### Otázka (Front)

Proč je výběrový rozptyl konzistentním odhadem populačního rozptylu?

### Odpověď (Back)

Přepišme jej jako
**s<sub>n</sub>²=(n/(n−1))[(1/n)ΣX<sub>i</sub>²−X̄<sub>n</sub>²]**.

Ze zákona velkých čísel platí (1/n)ΣX<sub>i</sub>²→E[X²] a X̄<sub>n</sub>→μ v pravděpodobnosti, zatímco n/(n−1)→1. Proto
**s<sub>n</sub>²→E[X²]−μ²=σ²**.
Konzistence znamená, že se s rostoucím počtem pozorování odhad variability stabilizuje kolem skutečného rozptylu.

## Poznámka Anki 1783851674961

Karty Anki: 1783851674961
GUID: oIY-tuTRA]; štítky: cramer_rao efektivita konsolidace::blok_6 nejlepsi_nestranny_odhad.

### Otázka (Front)

Co znamená nejlepší nestranný odhad a Raoova–Cramérova mez?

### Odpověď (Back)

**Nejlepší nestranný odhad** má mezi všemi nestrannými odhady téhož parametru nejmenší rozptyl pro každou hodnotu θ. Je tedy bez systematické chyby a současně má nejmenší možné náhodné kolísání.

**Raoova–Cramérova mez** je dolní mez rozptylu nestranných odhadů. Dosáhne-li ji konkrétní nestranný odhad, je nejlepší nestranný.

Ve skriptech: výběrový průměr je nejlepším nestranným odhadem střední hodnoty pro binomické, Poissonovo, exponenciální a normální rozdělení; výběrový rozptyl je nejlepším nestranným odhadem σ² v normálním modelu.

## Poznámka Anki 1783851674962

Karty Anki: 1783851674962
GUID: I_Ys(FN)+=; štítky: konsolidace::blok_6 konzistence metoda_momentu odhad.

### Otázka (Front)

Jak funguje metoda momentů a proč bývají její odhady konzistentní?

### Odpověď (Back)

Pro d neznámých parametrů se obvykle vybere alespoň d teoretických momentů, vyjádří se jimi parametry a momenty E[X<sup>k</sup>] se nahradí výběrovými momenty
**m<sub>k</sub>=(1/n)ΣX<sub>i</sub><sup>k</sup>**.
Vzniklá soustava rovnic se vyřeší pro odhady parametrů.

Metoda dává smysl díky zákonu velkých čísel: výběrové momenty konvergují k teoretickým, takže momentové odhady často bývají konzistentní. Je rychlá a jednoduchá, ale není obecně optimální a nemusí být nestranná.

## Poznámka Anki 1783851674963

Karty Anki: 1783851674963
GUID: Q%usCyNGs-; štítky: konsolidace::blok_6 metoda_momentu rozptyl vychyleni.

### Otázka (Front)

Jaký je momentový odhad rozptylu a jak se liší od nestranného výběrového rozptylu?

### Odpověď (Back)

Z rovností E[X]=μ a E[X²]=σ²+μ² dostaneme po nahrazení teoretických momentů výběrovými
**σ̂²<sub>MM</sub>=m<sub>2</sub>−m<sub>1</sub>²=(1/n)ΣX<sub>i</sub>²−X̄<sub>n</sub>²**
**=((n−1)/n)s<sub>n</sub>²**.

Momentový odhad tedy používá efektivně jmenovatel n, nikoli n−1. Proto systematicky podhodnocuje σ² a není nestranný, ale jeho vychýlení mizí s n, takže je konzistentní. Výběrový rozptyl je oproti tomu záměrně korigován na nestrannost.

## Poznámka Anki 1783851674964

Karty Anki: 1783851674964
GUID: f]r>rhhj;p; štítky: konsolidace::blok_6 log_verohodnost maximum_likelihood mle verohodnost.

### Otázka (Front)

Co je věrohodnost a maximálně věrohodný odhad a proč se používá log-věrohodnost?

### Odpověď (Back)

Pro pevná data x=(x<sub>1</sub>,…,x<sub>n</sub>) je **věrohodnostní funkce** L(θ;x) jejich sdružená pravděpodobnost nebo hustota chápaná jako funkce parametru θ. Oproti hustotě jsou zde data pevná a mění se parametr.

**MLE** θ̂ maximalizuje L(θ;x): volí parametr, pod nímž jsou pozorovaná data nejvěrohodnější. Často se maximalizuje ℓ(θ)=log L(θ;x), protože logaritmus převádí součiny na součty a jako rostoucí funkce zachovává maximum. Pro vícerozměrný parametr se typicky řeší ∂ℓ/∂θ<sub>j</sub>=0.

MLE je invariantní: MLE funkce g(θ) je g(θ̂). Za vhodných regularitních podmínek bývá konzistentní a má dobré asymptotické vlastnosti.

## Poznámka Anki 1783851674965

Karty Anki: 1783851674965
GUID: O*Ux5rcI[z; štítky: bernoulli konsolidace::blok_6 mle relativni_cetnost.

### Otázka (Front)

Jak se odvodí MLE parametru p v Bernoulliho modelu?

### Odpověď (Back)

Je-li ve výběru n Bernoulliho pozorování k úspěchů, pak
**L(p)=p<sup>k</sup>(1−p)<sup>n−k</sup>**
a maximum nastává v
**p̂=k/n=X̄**.

MLE je tedy relativní četnost úspěchů. Pro posloupnost H,O,H,H je k=3, n=4, a proto p̂=3/4; věrohodnost p³(1−p) má maximum právě v tomto bodě.

## Poznámka Anki 1783851674966

Karty Anki: 1783851674966
GUID: mu`dH94`g,; štítky: konsolidace::blok_6 mle normalni_rozdeleni stredni_hodnota.

### Otázka (Front)

Jaký je MLE střední hodnoty normálního rozdělení?

### Odpověď (Back)

Pro i.i.d. výběr z N(μ,σ²) vede derivace log-věrohodnosti podle μ k rovnici
**Σ(x<sub>i</sub>−μ)=0**,
tedy
**μ̂<sub>MLE</sub>=X̄<sub>n</sub>**.

Výběrový průměr je proto současně přirozeným, momentovým i maximálně věrohodným odhadem normální střední hodnoty.

## Poznámka Anki 1783851674967

Karty Anki: 1783851674967
GUID: N&o,Isld_a; štítky: konsolidace::blok_6 metoda_momentu mle normalni_rozdeleni rozptyl.

### Otázka (Front)

Jaký je MLE rozptylu normálního rozdělení a jak souvisí s momentovým a výběrovým rozptylem?

### Odpověď (Back)

Při současném odhadu μ a σ² v normálním modelu vychází
**σ̂²<sub>MLE</sub>=(1/n)Σ(X<sub>i</sub>−X̄<sub>n</sub>)²**
**=((n−1)/n)s<sub>n</sub>²**.

Má stejný tvar jako momentový odhad rozptylu. Používá jmenovatel n, takže systematicky podhodnocuje σ² a není nestranný; nestranný výběrový rozptyl používá n−1. Všechny tři odhady jsou konzistentní, ale jejich konstrukce a vlastnosti pro konečné n se liší.

## Poznámka Anki 1783851674968

Karty Anki: 1783851674968
GUID: Ck>fw$1`+(; štítky: konsolidace::blok_6 metoda_momentu mle vlastnosti_odhadu.

### Otázka (Front)

Jaký je hlavní rozdíl mezi metodou momentů a maximální věrohodností a jak hodnotit kvalitu jejich odhadů?

### Odpověď (Back)

**Metoda momentů** přizpůsobuje teoretické momenty empirickým; je jednoduchá a rychlá. **Maximální věrohodnost** využívá celý pravděpodobnostní model a volí parametr, který nejlépe podporuje pozorovaná data; často má lepší asymptotické vlastnosti.

Kvalita odhadu má více rozměrů: **nestrannost** znamená správný průměr pro pevné n, **konzistence** konvergenci ke skutečnému parametru a **nejlepší nestrannost** minimální rozptyl mezi nestrannými odhady. Žádná jednotlivá vlastnost sama nepopisuje vše.

Logika kapitoly: po výběrovém průměru a rozptylu se zavádějí obecné konstrukce odhadů — metoda momentů a MLE — a porovnávají se jejich konečně-výběrové a asymptotické vlastnosti.

## Poznámka Anki 1783851674969

Karty Anki: 1783851674969
GUID: xz,f]S*wp7; štítky: exponencialni histogram konsolidace::blok_6 mle model_selection.

### Otázka (Front)

Jak se v příkladu čekání na autobus kombinoval odhad parametrů s volbou modelu?

### Odpověď (Back)

Pro stejná data se maximální věrohodností odhadly parametry modelů **Unif(0,b)**, **Exp(λ)** a **N(μ,σ²)**. Jejich odhadnuté hustoty se pak překreslily přes histogram.

Nejlépe odpovídalo exponenciální rozdělení. Vizuální porovnání histogramu s odhadnutými hustotami je užitečná diagnostika: propojuje volbu tvaru rozdělení s odhadem parametrů. Samo o sobě však není formálním testem dobré shody.

