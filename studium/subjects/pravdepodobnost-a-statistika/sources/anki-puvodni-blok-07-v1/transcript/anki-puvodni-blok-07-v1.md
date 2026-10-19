# Pravděpodobnost a statistika – Původní blok 07

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::Pravděpodobnost a statistika
Rozsah: 16 poznámek, 16 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783851674970

Karty Anki: 1783851674970
GUID: vUx#Dd8MaE; štítky: coverage interval_spolehlivosti konsolidace::blok_7 konstrukce pivot.

### Otázka (Front)

Co je interval spolehlivosti, jak se interpretuje a jak se obecně konstruuje?

### Odpověď (Back)

**100·(1−α)% interval spolehlivosti** pro parametr θ je dvojice statistik L(X), U(X) s pokrytím **P<sub>θ</sub>(L<θ<U)=1−α** (případně alespoň 1−α). Parametr je ve frekventistickém pojetí pevný, náhodný je interval před pozorováním dat; po výpočtu už neříkáme, že θ leží v konkrétním intervalu s pravděpodobností 1−α, ale že použitá procedura má dlouhodobé pokrytí 1−α.

**Oboustranný interval** má tvar (L,U). Jednostranný interval má buď dolní mez (L,+∞), nebo horní mez (−∞,U). Obecná konstrukce používá **pivot** H(X,θ) se známým rozdělením: zvolí se jeho kvantily s celkovou pravděpodobností 1−α a nerovnost se algebraicky vyřeší pro θ.

Pro střední hodnotu se používá normální nebo Studentovo t-rozdělení podle znalosti rozptylu; pro rozptyl normální populace χ²-rozdělení; mimo přesné modely lze u velkých výběrů využít asymptotiku.

## Poznámka Anki 1783851674971

Karty Anki: 1783851674971
GUID: vdE`C5W2*,; štítky: bernoulli clv interval_prumer konsolidace::blok_7 podil z_interval.

### Otázka (Front)

Jak se sestrojí interval spolehlivosti pro střední hodnotu při známém rozptylu a jak se rozšíří pomocí CLV?

### Odpověď (Back)

Pro i.i.d. normální výběr X<sub>i</sub>∼N(μ,σ²) se známým σ platí **X̄∼N(μ,σ²/n)** a **Z=(X̄−μ)/(σ/√n)∼N(0,1)**. Označíme-li z<sub>1−α/2</sub> standardní normální kvantil, je oboustranný interval
**X̄ ± z<sub>1−α/2</sub>·σ/√n**.

Jednostranný interval s dolní mezí je (X̄−z<sub>1−α</sub>σ/√n,+∞), s horní mezí (−∞,X̄+z<sub>1−α</sub>σ/√n). Pro velké n dává centrální limitní věta stejné vzorce přibližně i pro nenormální data; kvalita aproximace závisí na n, šikmosti, těžkých ocasech a dalších vlastnostech rozdělení.

Pro Bernoulliho data je p̂=X̄ a základní Waldův interval **p̂ ± z<sub>1−α/2</sub>√(p̂(1−p̂)/n)**. Je pouze asymptotický a u malého n nebo p blízko 0 či 1 může fungovat špatně; v praxi bývá spolehlivější Wilsonův interval.

## Poznámka Anki 1783851674972

Karty Anki: 1783851674972
GUID: E8eF!A[^c5; štítky: interval_prumer konsolidace::blok_7 neznamy_rozptyl student_t.

### Otázka (Front)

Jak se sestrojí přesný interval pro střední hodnotu normální populace při neznámém rozptylu?

### Odpověď (Back)

Je-li X<sub>1</sub>,…,X<sub>n</sub> normální výběr a σ² neznáme, nahrazujeme σ výběrovou směrodatnou odchylkou s. Potom
**T=(X̄−μ)/(s/√n)∼t<sub>n−1</sub>**.

Oboustranný 100·(1−α)% interval je
**X̄ ± t<sub>1−α/2,n−1</sub>·s/√n**.
Jednostranný interval s dolní mezí je (X̄−t<sub>1−α,n−1</sub>s/√n,+∞), s horní mezí (−∞,X̄+t<sub>1−α,n−1</sub>s/√n).

t-rozdělení má těžší ocasy než N(0,1), protože zahrnuje nejistotu odhadu σ; proto je interval zejména pro malé n širší. S rostoucími stupni volnosti t-rozdělení splývá se standardním normálním. Stejný pivot stojí i za jednovýběrovým t-testem.

## Poznámka Anki 1783851674973

Karty Anki: 1783851674973
GUID: Fw**r!fY)8; štítky: chi_kvadrat interval_rozptyl konsolidace::blok_7 normalita.

### Otázka (Front)

Jak se sestrojí interval spolehlivosti pro rozptyl normální populace?

### Odpověď (Back)

Pro normální výběr platí přesně
**Q=(n−1)s²/σ²∼χ²<sub>ν</sub>**, kde ν=n−1. Označíme-li q<sub>p,ν</sub> p-kvantil χ²-rozdělení, oboustranný interval je
**((n−1)s²/q<sub>1−α/2,ν</sub>, (n−1)s²/q<sub>α/2,ν</sub>)**.

Jednostranný interval s dolní mezí je ((n−1)s²/q<sub>1−α,ν</sub>,+∞); interval s horní mezí je (0,(n−1)s²/q<sub>α,ν</sub>). Tato forma používá běžnou konvenci p-kvantilů; při značení kritických hodnot horním ocasem vypadají indexy opačně.

Na rozdíl od intervalů pro μ založených na standardizovaném průměru stojí tento interval na škálovaném výběrovém rozptylu. Přesné χ²-rozdělení vyžaduje normalitu a je na její porušení citlivé.

## Poznámka Anki 1783851674974

Karty Anki: 1783851674974
GUID: BX&8f7IM=D; štítky: alpha chyba_I chyba_II konsolidace::blok_7 sila testovani_hypotez.

### Otázka (Front)

Jaká je logika testování hypotéz, chyb I. a II. druhu, hladiny významnosti a síly testu?

### Odpověď (Back)

**Nulová hypotéza H<sub>0</sub>** je výchozí tvrzení, proti němuž hledáme evidenci; **alternativa H<sub>A</sub>** je konkurenční tvrzení. Výsledek je „H<sub>0</sub> zamítáme“ nebo „H<sub>0</sub> nezamítáme“ — nezamítnutí není důkaz její pravdivosti.

**Chyba I. druhu:** zamítnutí pravdivé H<sub>0</sub>; její maximální předem stanovená pravděpodobnost je hladina významnosti α. **Chyba II. druhu:** nezamítnutí H<sub>0</sub>, když platí alternativa; její pravděpodobnost se obvykle značí β. **Síla testu** je 1−β, tedy pravděpodobnost správného zamítnutí při konkrétní alternativě.

Hypotézy jsou asymetrické, protože konstrukce testu přímo kontroluje chybu I. druhu. Při pevném rozsahu výběru obvykle nelze libovolně snížit obě chyby; sílu zvyšuje větší n, větší skutečný efekt a nižší variabilita. Kapitola testování propojuje tuto rozhodovací logiku s testovými statistikami, kritickými obory, p-hodnotami a intervaly spolehlivosti.

## Poznámka Anki 1783851674975

Karty Anki: 1783851674975
GUID: EM:`,BL>t2; štítky: dualita interval_test jednostranny_test konsolidace::blok_7.

### Otázka (Front)

Jak spolu souvisejí intervaly spolehlivosti a oboustranné či jednostranné testy?

### Odpověď (Back)

Pro test H<sub>0</sub>:θ=θ<sub>0</sub> proti H<sub>A</sub>:θ≠θ<sub>0</sub> na hladině α platí dualita: **H<sub>0</sub> zamítneme právě tehdy, když θ<sub>0</sub> neleží v odpovídajícím 100·(1−α)% oboustranném intervalu spolehlivosti**.

Pro H<sub>A</sub>:θ>θ<sub>0</sub> použijeme jednostranný interval s dolní mezí (L,+∞) a zamítáme, když θ<sub>0</sub><L. Pro H<sub>A</sub>:θ<θ<sub>0</sub> použijeme interval s horní mezí (−∞,U) a zamítáme, když θ<sub>0</sub>>U.

Kritický obor a interval jsou dvě algebraicky ekvivalentní reprezentace téhož testu, pokud vycházejí ze stejné statistiky, stejné hladiny a stejné alternativy.

## Poznámka Anki 1783851674976

Karty Anki: 1783851674976
GUID: rsIHz@l|1;; štítky: konsolidace::blok_7 kriticky_obor p_hodnota testova_statistika vyznamnost.

### Otázka (Front)

Co jsou testová statistika, kritický obor a p-hodnota a jak se podle nich rozhoduje?

### Odpověď (Back)

**Testová statistika** T=T(X) je funkce dat, jejíž rozdělení za H<sub>0</sub> známe nebo umíme aproximovat. **Kritický obor** je množina extrémních hodnot T, při nichž H<sub>0</sub> zamítáme; volí se tak, aby pravděpodobnost zamítnutí za H<sub>0</sub> nepřesáhla α.

**p-hodnota** je za H<sub>0</sub> pravděpodobnost získat výsledek alespoň tak extrémní jako pozorovaný, ve směru stanoveném alternativou. Ekvivalentně je to nejmenší hladina α, na níž by daný test H<sub>0</sub> zamítl. Rozhodnutí: **p≤α ⇒ zamítáme H<sub>0</sub>**; p>α ⇒ nezamítáme.

Malá p-hodnota měří neslučitelnost dat s H<sub>0</sub>, nikoli pravděpodobnost, že H<sub>0</sub> je pravdivá. Statistická významnost také sama neříká, že efekt je velký, důležitý nebo kauzální.

## Poznámka Anki 1783851674977

Karty Anki: 1783851674977
GUID: FA2^^-z&DP; štítky: clv konsolidace::blok_7 stredni_hodnota t_test z_test.

### Otázka (Front)

Jak se testuje střední hodnota jedním výběrem při známém či neznámém rozptylu a co se mění mimo normalitu?

### Odpověď (Back)

Pro H<sub>0</sub>:μ=μ<sub>0</sub> a známé σ používáme
**Z=(X̄−μ<sub>0</sub>)/(σ/√n)**. Při oboustranné alternativě zamítáme, když |Z|>z<sub>1−α/2</sub>; jednostranně používáme příslušný jeden ocas.

Při neznámém σ a normálním výběru používáme
**T=(X̄−μ<sub>0</sub>)/(s/√n)∼t<sub>n−1</sub>** a oboustranně zamítáme pro |T|>t<sub>1−α/2,n−1</sub>. Obě rozhodnutí jsou ekvivalentní kontrole, zda μ<sub>0</sub> leží v odpovídajícím intervalu spolehlivosti.

Mimo normální rozdělení lze pro velké n použít asymptotický test založený na CLV. Na rozdíl od přesného normálního či t-testu má pouze přibližnou hladinu; její kvalita závisí na velikosti výběru a tvaru populace.

## Poznámka Anki 1783851674978

Karty Anki: 1783851674978
GUID: kU7-*.e?u_; štítky: chi_kvadrat konsolidace::blok_7 normalita test_rozptylu.

### Otázka (Front)

Jak se testuje hypotéza o rozptylu normální populace?

### Odpověď (Back)

Pro normální výběr a H<sub>0</sub>:σ²=σ<sub>0</sub>² platí za H<sub>0</sub>
**Q=(n−1)s²/σ<sub>0</sub>²∼χ²<sub>n−1</sub>**.

Při oboustranné alternativě σ²≠σ<sub>0</sub>² zamítáme, když **Q<q<sub>α/2,n−1</sub>** nebo **Q>q<sub>1−α/2,n−1</sub>**, kde q<sub>p,ν</sub> je p-kvantil χ²<sub>ν</sub>. Pro jednostranné alternativy se použije pouze příslušný ocas. Test je přesně duální k χ²-intervalu pro σ² a jeho platnost je citlivá na předpoklad normality.

## Poznámka Anki 1783851674979

Karty Anki: 1783851674979
GUID: BesR&CXG*$; štítky: dvouvyberovy_t_test konsolidace::blok_7 nezavislost parovy_t_test welch.

### Otázka (Front)

Kdy použít párový a kdy dvouvýběrový t-test?

### Odpověď (Back)

**Párový t-test** se používá, když každé pozorování v jedné podmínce přirozeně patří k pozorování ve druhé podmínce, například před–po u stejného člověka. Uvnitř páru může být závislost; nezávislé mají být jednotlivé páry. Vytvoříme rozdíly D<sub>i</sub>=Y<sub>i</sub>−X<sub>i</sub> a provedeme jednovýběrový t-test H<sub>0</sub>:μ<sub>D</sub>=0.

**Dvouvýběrový t-test** porovnává střední hodnoty dvou nezávislých skupin. Při předpokladu shodných rozptylů lze použít pooled variantu; bez tohoto předpokladu Welchův t-test, který upravuje standardní chybu i stupně volnosti.

Rozhodující není počet sloupců dat, ale struktura závislosti: spárovaná měření se nesmějí analyzovat jako dvě nezávislé skupiny a naopak.

## Poznámka Anki 1783851674980

Karty Anki: 1783851674980
GUID: AKMD*J$ScA; štítky: f_test konsolidace::blok_7 normalita rozptyly.

### Otázka (Front)

Co testuje F-test shody dvou rozptylů a jaké má omezení?

### Odpověď (Back)

Pro dva nezávislé normální výběry testuje F-test H<sub>0</sub>:σ<sub>1</sub>²=σ<sub>2</sub>² pomocí poměru
**F=s<sub>1</sub>²/s<sub>2</sub>²∼F<sub>n₁−1,n₂−1</sub>** za H<sub>0</sub>. Oboustranný test zamítá v obou ocasech F-rozdělení; jednostranný v ocasu odpovídajícím alternativě.

Test je **velmi citlivý na nenormalitu a odlehlé hodnoty**. Když je normalita pochybná, bývá vhodnější robustnější test rozptylové homogenity, například Leveneův nebo Brownův–Forsytheův test.

## Poznámka Anki 1783851674981

Karty Anki: 1783851674981
GUID: vr!zc#E578; štítky: intercept konsolidace::blok_7 linearni_regrese model rezidua smernice.

### Otázka (Front)

Jak zní jednoduchý lineární regresní model a co znamenají jeho parametry a rezidua?

### Odpověď (Back)

Jednoduchý lineární model je
**Y<sub>i</sub>=α+βx<sub>i</sub>+ε<sub>i</sub>**, i=1,…,n. Hodnoty x<sub>i</sub> se obvykle považují za pevně zadané; chyby jsou nezávislé, mají E(ε<sub>i</sub>)=0 a Var(ε<sub>i</sub>)=σ². Normalita ε<sub>i</sub> je potřeba pro přesné malé-výběrové intervaly a testy, nikoli pro samotný výpočet OLS přímky.

**α** je očekávaná odezva při x=0 (má smysl jen, je-li x=0 relevantní); **β** je změna E(Y|x) při zvýšení x o jednu jednotku. Odhadnutá hodnota je Ŷ<sub>i</sub>=a+bx<sub>i</sub> a **reziduum** e<sub>i</sub>=Y<sub>i</sub>−Ŷ<sub>i</sub> je pozorovaná nevysvětlená odchylka.

Regrese navazuje na kovarianci a korelaci, ale navíc stanovuje směrový model odezvy Y podmíněné x.

## Poznámka Anki 1783851674982

Karty Anki: 1783851674982
GUID: G-rs4XMYU-; štítky: konsolidace::blok_7 korelace kovariance nejmensi_ctverce ols smernice.

### Otázka (Front)

Jak metoda nejmenších čtverců odhaduje regresní přímku a jak směrnice souvisí s kovariancí a korelací?

### Odpověď (Back)

Metoda nejmenších čtverců volí a,b tak, aby minimalizovala reziduální součet čtverců
**SSE=Σ[y<sub>i</sub>−(a+bx<sub>i</sub>)]²**.

Označíme S<sub>xx</sub>=Σ(x<sub>i</sub>−x̄)² a S<sub>xy</sub>=Σ(x<sub>i</sub>−x̄)(y<sub>i</sub>−ȳ). Potom
**b=S<sub>xy</sub>/S<sub>xx</sub>**,   **a=ȳ−bx̄**.
Odhadnutá přímka tedy prochází bodem (x̄,ȳ). Směrnice b je odhadovaná průměrná změna Y na jednotku x.

Při konzistentních definicích výběrových momentů platí
**b=s<sub>XY</sub>/s<sub>X</sub>²=r<sub>XY</sub>(s<sub>Y</sub>/s<sub>X</sub>)**. Kovariance určuje směr společného kolísání, korelace jej normalizuje a regresní směrnice převádí vazbu do jednotek Y na jednotku x.

## Poznámka Anki 1783851674983

Karty Anki: 1783851674983
GUID: cB2MI#V`; štítky: konsolidace::blok_7 r_squared rezidualni_rozptyl sse.

### Otázka (Front)

Jak se v jednoduché regresi odhaduje rozptyl chyb a interpretuje koeficient determinace R²?

### Odpověď (Back)

Po odhadu dvou parametrů a,b má reziduální součet čtverců SSE n−2 stupňů volnosti. Nestranný odhad rozptylu chyb je
**s²=SSE/(n−2)**, jeho odmocnina s je reziduální směrodatná chyba.

Celkový součet čtverců je **SST=Σ(y<sub>i</sub>−ȳ)²** a v modelu s interceptem platí
**R²=1−SSE/SST**. Vyjadřuje podíl výběrové variability Y, který v daném souboru zachytí lineární model; v jednoduché regresi s interceptem je R²=r<sub>XY</sub>².

Vysoké R² znamená těsnější lineární přizpůsobení, ale samo nezaručuje kauzalitu, správnou specifikaci modelu, dobré predikce mimo rozsah dat ani splnění předpokladů o reziduích.

## Poznámka Anki 1783851674984

Karty Anki: 1783851674984
GUID: G^]5$L)A%Z; štítky: beta konsolidace::blok_7 korelace regresni_inference test_smernice.

### Otázka (Front)

Jak se v jednoduché regresi testuje lineární závislost a jak to souvisí s testem nulové korelace?

### Odpověď (Back)

Lineární vliv x na střední odezvu se testuje hypotézou **H<sub>0</sub>:β=0** proti například H<sub>A</sub>:β≠0. Za H<sub>0</sub> se model redukuje na konstantní střední hodnotu Y<sub>i</sub>=α+ε<sub>i</sub>.

Používá se statistika **t=b/SE(b)** se stupni volnosti n−2; ekvivalentně se kontroluje, zda 0 leží v intervalu spolehlivosti pro β, nebo zda p-hodnota nepřesahuje α. Korelace pouze měří symetrickou sílu lineární asociace, zatímco regrese modeluje podmíněnou střední hodnotu Y a má směr.

V jednoduché lineární regresi s interceptem a za obvyklých předpokladů je oboustranný test β=0 algebraicky ekvivalentní testu populační korelace ρ=0: oba zkoumají existenci lineární vazby. Statistická významnost ale neříká, že vztah je prakticky velký nebo kauzální.

## Poznámka Anki 1783851674985

Karty Anki: 1783851674985
GUID: b6VE6`O;c}; štítky: confidence_band interval_stredni_odezvy konsolidace::blok_7 predikce predikcni_interval.

### Otázka (Front)

Jak se v jednoduché regresi predikuje odezva a jak se liší interval pro střední odezvu, predikční interval a pás spolehlivosti?

### Odpověď (Back)

Pro dané x<sub>0</sub> je bodová predikce **ŷ(x<sub>0</sub>)=a+bx<sub>0</sub>**. Položme S<sub>xx</sub>=Σ(x<sub>i</sub>−x̄)² a s²=SSE/(n−2).

**Bodový interval pro střední odezvu E(Y|x<sub>0</sub>):**
ŷ(x<sub>0</sub>) ± t<sub>1−α/2,n−2</sub>s√[1/n+(x<sub>0</sub>−x̄)²/S<sub>xx</sub>].

**Predikční interval pro jednu budoucí hodnotu Y<sub>new</sub>:**
ŷ(x<sub>0</sub>) ± t<sub>1−α/2,n−2</sub>s√[1+1/n+(x<sub>0</sub>−x̄)²/S<sub>xx</sub>].
Je širší kvůli dodatečné individuální chybě „1“. Vzorec bez této jedničky, uvedený v původním decku jako predikční interval, je ve skutečnosti bodový interval pro střední odezvu.

**Simultánní pás spolehlivosti** má pokrýt celou skutečnou regresní funkci v určeném rozsahu x; je širší než jednotlivé bodové intervaly pro střední odezvu, ale je jiným objektem než interval pro budoucí jednotlivce. Všechny intervaly se rozšiřují dál od x̄ a extrapolace mimo rozsah dat je riziková.

