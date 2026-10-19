# BI-ML2 – Přednáška 09

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 17 poznámek, 17 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291579

Karty Anki: 1785306291580
GUID: _Bp*d7u?tG; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak se liší full-batch, minibatchové a online gradientní učení a jak velikost dávky ovlivňuje gradient?

### Odpověď (Back)

Síť minimalizuje J(w)=(1/N)ΣᵢL(Yᵢ,f(xᵢ;w)), kde w obsahuje všechny trénovatelné parametry. Deterministický full-batch sestup používá přesný gradient ∇J=(1/N)Σᵢ∇Lᵢ, ale jeden update nad velkým datasetem je pomalý a paměťově náročný.

Minibatch velikosti m používá J̃(w)=(1/m)Σᵢ₌₁ᵐL(Y⁽ⁱ⁾,f(x⁽ⁱ⁾;w)); ∇J̃ je stochastický odhad plného gradientu a při rovnoměrně náhodném výběru dávky je nezaujatý. Náklady kroku závisejí na m, nikoli přímo na N. Menší m dává častější, levnější, ale hlučnější aktualizace; větší m přesněji aproximuje plný gradient a lépe využívá paralelní hardware, ale potřebuje více paměti. Krajní případy jsou online učení m=1 a full-batch m=N. Volba m tedy vyvažuje přesnost gradientu, frekvenci aktualizací, paměť a paralelizaci.

## Poznámka Anki 1785306291581

Karty Anki: 1785306291582
GUID: 0B`hm<^|7A; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak probíhá minibatchové SGD přes epochy a proč se řídí learning rate?

### Odpověď (Back)

Na začátku epochy se data náhodně zamíchají a rozdělí do dávek, aby původní pořadí (např. seskupení tříd) systematicky nezkreslovalo gradienty. Epocha je úplný průchod N body a obsahuje přibližně N/m, přesněji ⌈N/m⌉, aktualizací. Na jejím konci se sleduje trénovací/validační ztráta a výkon; konec určí počet epoch, ustálení cíle nebo validace.

SGD v širším smyslu používá náhodnou dávku a update w←w−ε∇J̃(w). Gradient ukazuje nejrychlejší lokální růst, proto se odečítá. Learning rate ε určuje délku kroku: příliš velký přeskakuje minimum, osciluje či diverguje, příliš malý konverguje pomalu. Proto se často mění v čase: pro lineární plán je při k≤τ
ε<sub>k</sub>=(1−k/τ)ε₀+(k/τ)ε<sub>τ</sub>,
a pro k>τ zůstane ε<sub>τ</sub>; ε₀ je počáteční, ε<sub>τ</sub> konečná hodnota a τ délka přechodu.

## Poznámka Anki 1785306291583

Karty Anki: 1785306291584
GUID: mWQT-of[OM; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Proč záleží na inicializaci vah a jak funguje Xavierova inicializace?

### Odpověď (Back)

Inicializace určuje počáteční oblast nekonvexní účelové funkce, škálu aktivací a gradientů i další optimalizační trajektorii. Váhy se proto inicializují náhodně z vhodně škálovaného normálního či rovnoměrného rozdělení: příliš malé mohou tlumit aktivace a gradienty, příliš velké je zvětšovat nebo saturovat aktivace.

Xavierova rovnoměrná inicializace pro m vstupů a n neuronů volí každou váhu z Uniform(−√(6/(m+n)), √(6/(m+n))). Cílem je udržet rozumnou škálu signálu a gradientu napříč vrstvami.

## Poznámka Anki 1785306291585

Karty Anki: 1785306291586
GUID: _{8EI$1f<w; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak funguje SGD s momentem a proč urychluje pohyb údolím účelové funkce?

### Odpověď (Back)

Momentum kombinuje aktuální gradient s akumulovaným směrem minulých aktualizací. Aktualizuje rychlost a parametry:
v←μv−ε∇J̃(w),   w←w+v.
μ určuje zachování předchozí rychlosti; při μ=0 jde o běžné SGD. Fyzikální analogií je hmotné těleso v potenciálovém poli, na něž gradient působí jako síla.

Opakovaně podobné gradienty se v rychlosti akumulují a pohyb v konzistentním směru zrychlí. Střídající se příčné složky v úzkém údolí se naopak částečně vyruší, čímž klesnou oscilace. Nesterovovo momentum vyhodnocuje gradient s ohledem na předběžný posun parametrů daný aktuální rychlostí.

## Poznámka Anki 1785306291587

Karty Anki: 1785306291588
GUID: 4j9$~YPT^K; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak funguje AdaGrad a jaké má výhody a omezení?

### Odpověď (Back)

Různé parametry mohou potřebovat jiné learning rates kvůli odlišným škálám a historii gradientů. Adaptivní optimalizátory proto mění krok každé souřadnice. AdaGrad pro g=∇J̃(w) akumuluje po složkách
r←r+g⊙g
a aktualizuje
w←w−[ε/(δ+√r)]⊙g.
r zaznamenává celkovou historickou velikost gradientů; δ brání dělení nulou a stabilizuje výpočet.

Často velké gradienty rychle zvětší r a zmenší efektivní krok. Řídké či vzácné gradienty udrží relativně větší krok déle, což je výhoda pro sparse příznaky. Protože však r obsahuje celou historii a pouze roste, learning rates mohou klesnout téměř k nule a učení se prakticky zastavit.

## Poznámka Anki 1785306291589

Karty Anki: 1785306291590
GUID: 3@e7U+tWLl; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak RMSProp upravuje AdaGrad a jak vypadá RMSProp s momentem?

### Odpověď (Back)

RMSProp nahrazuje AdaGradův neomezeně rostoucí součet exponenciálně váženým průměrem:
r←ρr+(1−ρ)g⊙g.
Větší ρ pomaleji zapomíná starší gradienty. S momentem pak
v←μv−[ε/(δ+√r)]⊙g,   w←w+v.

AdaGrad váží všechny čtverce gradientů od začátku, zatímco RMSProp zdůrazňuje nedávnou historii. Proto se jeho efektivní learning rates nemusí monotónně vytratit a mohou se přizpůsobovat měnící se geometrii účelové funkce.

## Poznámka Anki 1785306291591

Karty Anki: 1785306291592
GUID: ^uL)bD~m$P; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak Adam kombinuje adaptivní první a druhý moment gradientu?

### Odpověď (Back)

Adam („adaptive moments“) akumuluje exponenciální průměr gradientu
s←ρ₁s+(1−ρ₁)g
a jeho čtverce
r←ρ₂r+(1−ρ₂)g⊙g.
s vyhlazuje směr podobně jako momentum, r odhaduje nedávnou velikost čtverců gradientu pro škálování jednotlivých souřadnic.

Protože s a r začínají nulou, rané odhady jsou zkreslené k nule. V kroku t se opraví ŝ=s/(1−ρ₁ᵗ) a r̂=r/(1−ρ₂ᵗ). Finální update je
w←w−ε ŝ/(δ+√r̂)
po složkách. Adam tedy spojuje směrové vyhlazování momenta s adaptivním škálováním RMSPropu. Je široce použitelný, ale není univerzálně nejlepší pro každou architekturu, dataset a cíl.

## Poznámka Anki 1785306291593

Karty Anki: 1785306291594
GUID: RrAx`bCaoN; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak se liší optimalizace prvního a druhého řádu a proč je u velkých sítí klíčová generalizace?

### Odpověď (Back)

Metody druhého řádu používají kromě gradientu zakřivení, typicky Hessovu matici nebo aproximaci. Newtonův krok pracuje s gradientem a inverzí Hessovy matice; BFGS iterativně aproximuje informaci z inverzního Hessianu. U velkých sítí jsou výpočet, uložení a řešení hessianových systémů příliš náročné, proto se častěji používá SGD či Adam.

Vícevrstvá síť má nekonvexní cíl se sedlovými body a lokálními minimy. Sedlový bod má nulový gradient, ale v některých směrech je lokálním minimem a v jiných maximem. Prakticky bývá důležitější než přesné globální minimum přeučení: velká expresivní síť může trénovací data i zapamatovat, ale špatně generalizovat. Regularizace upravuje model či trénování tak, aby omezila přizpůsobení náhodným detailům a podpořila výkon na nových datech.

## Poznámka Anki 1785306291595

Karty Anki: 1785306291596
GUID: ?wt*HTbU=F; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak funguje explicitní regularizace λΩ(w) a jak se liší L1 od L2?

### Odpověď (Back)

Regularizovaný cíl je J′(w)=J(w)+λΩ(w). λ řídí kompromis mezi přizpůsobením datům a jednoduchostí: příliš malé dovoluje přeučení, příliš velké vede k podučení a vysoké trénovací chybě.

**L2:** Ω(w)=‖w‖₂²=Σⱼwⱼ². Plynule tlačí všechny váhy k nule, omezuje extrémy a ke gradientu přidává 2λw.

**L1:** Ω(w)=‖w‖₁=Σⱼ|wⱼ|. Výrazněji podporuje přesné nuly a tím řídkou síť, v níž se mnoho spojení efektivně nepoužívá. L2 obvykle váhy pouze zmenšuje, L1 častěji některé úplně vynuluje.

## Poznámka Anki 1785306291597

Karty Anki: 1785306291598
GUID: pr_W|9>,HC; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak funguje early stopping a proč je regularizací?

### Odpověď (Back)

Po každé epoše se vyhodnotí validační chyba na datech oddělených od aktualizace vah. Při zlepšení se uloží parametry; po patience ℓ po sobě jdoucích epochách bez zlepšení se trénování ukončí a obnoví se nejlepší uložené váhy, protože poslední epocha nemusí být nejlepší.

Early stopping brání fázi, kdy trénovací chyba dál klesá hlavně zapamatováním detailů, zatímco validační chyba už roste—typický signál přeučení. Testovací množina se k rozhodování nesmí používat, jinak se jí model opakovaně přizpůsobí a test přestane být nezávislým hodnocením.

## Poznámka Anki 1785306291599

Karty Anki: 1785306291600
GUID: fYghMB|Fhw; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak funguje standardní a inverted dropout při trénování a inferenci?

### Odpověď (Back)

Dropout během trénování nezávisle vynuluje každou vybranou aktivaci s Bernoulliho pravděpodobností vypnutí p; keep probability je 1−p a pro každou dávku vzniká nová maska. Při standardní inferenci se neurony náhodně nevypínají.

Inverted dropout počítá
h̃=(μ⊙h)/(1−p),   μⱼ∼Bernoulli(1−p).
Zachované aktivace škáluje 1/(1−p), takže E[h̃|h]=h. Při inferenci pak síť běží deterministicky bez masky i bez další změny škály.

## Poznámka Anki 1785306291601

Karty Anki: 1785306291602
GUID: ZOq6x+=Qjw; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Proč dropout regularizuje síť a jak souvisí s baggingem a ko-adaptací?

### Odpověď (Back)

Každá maska definuje jinou podsíť se sdílenými parametry; plná síť při inferenci levně aproximuje průměr rozhodnutí mnoha těchto podsítí, podobně jako bagging. Výpočet je levný—jen binární maska a násobení—oproti explicitnímu trénování souboru sítí.

Protože libovolná spolupracující aktivace může zmizet, neuron se nemůže spoléhat na úzkou stálou kombinaci jiných neuronů (ko-adaptaci). Příznaky musejí být robustně užitečné v různých kontextech; obrazový model tak například využívá širší spektrum signálů místo jediné části obrazu.

Dropout v každém kroku snižuje efektivní kapacitu aktivní podsítě, proto může model s dropoutem potřebovat více neuronů než model bez něj.

## Poznámka Anki 1785306291603

Karty Anki: 1785306291604
GUID: ?EnhI,<m@g; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak jednoduchý součinový model vysvětluje mizející a explodující gradient v hluboké síti?

### Odpověď (Back)

Pro f(x,w)=x∏<sub>j=1</sub><sup>l</sup>w<sub>j</sub> platí
∂f/∂w<sub>i</sub>=x∏<sub>j≠i</sub>w<sub>j</sub>=f/w<sub>i</sub> pro w<sub>i</sub>≠0.
Jsou-li všechny váhy stejné w, pak f=xw<sup>l</sup> a ∂f/∂w<sub>i</sub>=xw<sup>l−1</sup>. Pro |w| výrazně pod 1 gradient s hloubkou mizí; pro |w| nad 1 může explodovat. Výstup i gradient jsou tedy citlivé na násobení mnoha vah.

Proto je obtížné zvolit jeden globální learning rate: stejný krok může být v některých vrstvách zanedbatelný a v jiných destabilizující.

## Poznámka Anki 1785306291605

Karty Anki: 1785306291606
GUID: &E4#G0_3@c; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak batch normalization standardizuje preaktivace a proč používá γ a β?

### Odpověď (Back)

Batch normalization (BN) během trénování standardizuje pro každý neuron/kanál preaktivace před aktivační funkcí podle aktuální minibatch velikosti m. Pro hodnoty h<sub>i,j</sub>:
μ̂<sub>j</sub>=(1/m)Σᵢh<sub>i,j</sub>,
σ̂<sub>j</sub>²=(1/m)Σᵢ(h<sub>i,j</sub>−μ̂<sub>j</sub>)²,
h′<sub>i,j</sub>=(h<sub>i,j</sub>−μ̂<sub>j</sub>)/√(δ+σ̂<sub>j</sub>²),
výstup=γ<sub>j</sub>h′<sub>i,j</sub>+β<sub>j</sub>.
δ stabilizuje malý rozptyl; γ je naučená škála a β posun.

γ a β dovolí síti zvolit vhodnou střední hodnotu a rozptyl místo pevného (0,1), ale škála a posun jsou řízeny dvěma přímými parametry namísto složité interakce předchozích vah. Učí se gradientem spolu se síťovými vahami a gradient prochází také výpočtem dávkového průměru a rozptylu.

## Poznámka Anki 1785306291607

Karty Anki: 1785306291608
GUID: RI(S*6=r(G; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jaké statistiky používá batch normalization při trénování a při inferenci?

### Odpověď (Back)

Při trénování BN používá průměr a rozptyl aktuální minibatch. Při inferenci by to bylo nestabilní a nedeterministické—predikce může běžet po jednom bodu či na jinak složených dávkách—proto používá běžící populační odhady z trénování.

Podle materiálu:
μ<sub>j</sub>←(1−ρ)μ<sub>j</sub>+ρμ̂<sub>j</sub>,
σ<sub>j</sub>²←(1−ρ)σ<sub>j</sub>²+ρσ̂<sub>j</sub>²,
kde ρ určuje váhu aktuální dávky vůči historii. Bias afinní vrstvy se před BN často vynechává: odečtení průměru by jeho konstantní posun odstranilo a β už poskytuje vlastní naučený posun.

## Poznámka Anki 1785306291609

Karty Anki: 1785306291610
GUID: >/7M#tS/ly; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak se batch normalization používá u obrazů a jak se liší od minibatchového učení a dropoutu?

### Odpověď (Back)

U obrazových či časových dat se statistiky, γ a β typicky sdílejí přes prostorové/časové pozice a liší se pouze mezi kanály. Kanálová BN tedy používá pro všechny pozice jednoho kanálu společné parametry i statistiky. Obvykle leží mezi afinní transformací a aktivací, existují však i varianty po aktivaci.

BN stabilizuje velmi rozdílné škály preaktivací a gradientů napříč vrstvami a může usnadnit volbu learning rate; přesný mechanismus jejího empirického přínosu však nelze zredukovat na jediné všeobecně přijaté vysvětlení.

Minibatchové učení používá dávku k odhadu gradientu, BN ji používá k transformaci mezivýsledků. Dropout se při inferenci vypne, zatímco BN zůstává v síti a používá uložené běžící statistiky.

## Poznámka Anki 1785306291611

Karty Anki: 1785306291612
GUID: >8x+s.Vp}o; štítky: BI-ML2 iterace_09 Konsolidovano Prednaska_09.

### Otázka (Front)

Jak do sebe zapadají optimalizace, regularizace, náhodnost a stabilizace při praktickém trénování hluboké sítě?

### Odpověď (Back)

Optimalizátor určuje, jak měnit parametry ke snížení trénovacího cíle; regularizace mění cíl či průběh trénování pro lepší generalizaci. Learning rate řídí velikost kroku, λ sílu penalizace složitosti. Momentum kombinuje směry gradientů v čase, zatímco adaptivní škálování mění krok každé souřadnice podle historie velikostí gradientu.

Minibatchový krok: vybrat dávku → dopředný chod → průměrná ztráta → backpropagation → update optimalizátorem. Náhodná inicializace volí start, náhodná dávka vytváří stochastický gradient a dropout vybírá aktivní podsíť.

Early stopping a dropout míří proti přeučení různě: první omezuje dobu přizpůsobování, druhý závislost na konkrétních vnitřních reprezentacích. Inicializace, BN a adaptivní optimalizátory všechny řeší nevhodné škály—na začátku, uvnitř sítě a při převodu gradientů na kroky. Hlavní pilíře jsou minibatchový odhad gradientu, vhodná optimalizace, regularizace a stabilizace mezilehlých škál.

