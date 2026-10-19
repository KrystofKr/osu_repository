# Pravděpodobnost a statistika – Původní blok 05

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::Pravděpodobnost a statistika
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1783851674938

Karty Anki: 1783851674938
GUID: dw(A*UwTsg; štítky: konsolidace::blok_5 limitni_vety statistika vyberovy_prumer.

### Otázka (Front)

Proč jsou limitní věty základem přechodu od pravděpodobnosti ke statistice?

### Odpověď (Back)

**Pravděpodobnost** vychází ze známého modelu a popisuje chování náhodných veličin. **Statistika** vychází z opakovaných pozorování a usuzuje na neznámé vlastnosti modelu, například střední hodnotu nebo pravděpodobnost úspěchu.

Limitní věty vysvětlují, proč tento postup funguje: při mnoha nezávislých opakováních se agregované statistiky stabilizují a jejich chyby mají předvídatelné asymptotické chování. Přirozeným odhadem střední hodnoty je proto výběrový průměr
**X̄<sub>n</sub>=(1/n)Σ<sub>i=1</sub><sup>n</sup>X<sub>i</sub>**,
který využívá všechna pozorování a s rostoucím n se stabilizuje kolem skutečné střední hodnoty.

## Poznámka Anki 1783851674939

Karty Anki: 1783851674939
GUID: wrHwXNA&`m; štítky: konsolidace::blok_5 markovova_nerovnost.

### Otázka (Front)

Co říká Markovova nerovnost, jaké má předpoklady a co znamená?

### Odpověď (Back)

Je-li **X≥0**, E[X]<∞ a a>0, pak
**P(X≥a)≤E[X]/a**.

Dává horní mez pravděpodobnosti velkých hodnot pouze ze střední hodnoty, bez znalosti přesného rozdělení. Slovně: má-li nezáporná veličina malou střední hodnotu, nemůže příliš často nabývat velmi velkých hodnot. Nerovnost bývá hrubá, ale je velmi obecná.

## Poznámka Anki 1783851674940

Karty Anki: 1783851674940
GUID: nGO+{LE3f,; štítky: cebysevova_nerovnost konsolidace::blok_5 markovova_nerovnost.

### Otázka (Front)

Co říká Čebyševova nerovnost a jak vznikne z Markovovy nerovnosti?

### Odpověď (Back)

Pro náhodnou veličinu X se střední hodnotou μ, konečným rozptylem σ² a ε>0 platí
**P(|X−μ|≥ε)≤σ²/ε²**.

Odvození: na nezápornou veličinu **Y=(X−E[X])²** použijeme Markovovu nerovnost s prahem ε²:
P(Y≥ε²)≤E[Y]/ε²=var(X)/ε².

Čebyševova nerovnost tedy převádí informaci o rozptylu na obecnou horní mez pravděpodobnosti velké odchylky od průměru. V logice limitních vět je Markovova nerovnost obecným odhadem chvostu a Čebyševova její specializací pro koncentraci kolem střední hodnoty.

## Poznámka Anki 1783851674941

Karty Anki: 1783851674941
GUID: b+~[tx>r=]; štítky: koncentrace konsolidace::blok_5 rozptyl vyberovy_prumer.

### Otázka (Front)

Jaké jsou střední hodnota a rozptyl výběrového průměru a jak z nich plyne jeho koncentrace?

### Odpověď (Back)

Pro i.i.d. veličiny X<sub>1</sub>,…,X<sub>n</sub> se střední hodnotou μ a rozptylem σ² platí
**E[X̄<sub>n</sub>]=μ**,   **var(X̄<sub>n</sub>)=σ²/n**.

Rozptyl klesá jako 1/n, protože rozptyly nezávislých veličin se při součtu sčítají, zatímco dělení součtu číslem n škáluje rozptyl faktorem 1/n². Průměrování tedy potlačuje náhodné kolísání.

Čebyševova nerovnost dává
**P(|X̄<sub>n</sub>−μ|≥ε)≤σ²/(nε²)→0**.
Tím přímo ukazuje, že se průměr s rostoucím n koncentruje kolem μ.

## Poznámka Anki 1783851674942

Karty Anki: 1783851674942
GUID: Fb$E49syB_; štítky: konsolidace::blok_5 konzistence slaby zakon_velkych_cisel.

### Otázka (Front)

Co říká slabý zákon velkých čísel a proč z něj plyne konzistence výběrového průměru?

### Odpověď (Back)

Pro i.i.d. náhodné veličiny s konečnou střední hodnotou μ platí
**X̄<sub>n</sub> →<sup>P</sup> μ**,
tj. pro každé ε>0 je P(|X̄<sub>n</sub>−μ|≥ε)→0.

Neříká, že X̄<sub>n</sub>=μ pro konečné n. Říká, že pravděpodobnost libovolně velké pevně zvolené odchylky klesá k nule. Výběrový průměr je proto **konzistentním odhadem** μ: s rostoucím rozsahem výběru se k odhadovanému parametru přibližuje.

## Poznámka Anki 1783851674943

Karty Anki: 1783851674943
GUID: pB)PwzLUj$; štítky: konsolidace::blok_5 konvergence silny zakon_velkych_cisel.

### Otázka (Front)

Co říká silný zákon velkých čísel a jak se liší od slabého?

### Odpověď (Back)

Pro i.i.d. náhodné veličiny s konečnou střední hodnotou μ platí
**X̄<sub>n</sub> → μ skoro jistě**.

To znamená, že s pravděpodobností 1 se podél celé realizované posloupnosti výběrové průměry skutečně stabilizují k μ. Slabý zákon požaduje jen konvergenci v pravděpodobnosti. Skoro jistá konvergence je silnější: **implikuje konvergenci v pravděpodobnosti**, opačná implikace obecně neplatí.

## Poznámka Anki 1783851674944

Karty Anki: 1783851674944
GUID: x-TLfbs|<D; štítky: konsolidace::blok_5 konvergence_v_distribuci konvergence_v_pravdepodobnosti.

### Otázka (Front)

Co je konvergence v distribuci a jak souvisí s konvergencí v pravděpodobnosti?

### Odpověď (Back)

Platí **X<sub>n</sub> ⇒ X**, jestliže
**F<sub>Xₙ</sub>(x)→F<sub>X</sub>(x)**
ve všech bodech spojitosti limitní distribuční funkce F<sub>X</sub>.

Konvergence v distribuci říká, že se asymptoticky přibližuje **tvar rozdělení**; nevyžaduje, aby se jednotlivé hodnoty X<sub>n</sub> přibližovaly X. Konvergence v pravděpodobnosti je silnější a popisuje přibližování samotných hodnot:
**X<sub>n</sub>→<sup>P</sup>X ⇒ X<sub>n</sub>⇒X**.
Obrácená implikace obecně neplatí.

## Poznámka Anki 1783851674945

Karty Anki: 1783851674945
GUID: F@F*YFQpN_; štítky: centralni_limitni_veta konsolidace::blok_5 standardizace.

### Otázka (Front)

Co říká centrální limitní věta a proč se součet či průměr standardizuje?

### Odpověď (Back)

Pro i.i.d. veličiny X<sub>i</sub> se střední hodnotou μ a kladným konečným rozptylem σ² platí
**(Σ<sub>i=1</sub><sup>n</sup>X<sub>i</sub>−nμ)/(σ√n) ⇒ N(0,1)**.
Ekvivalentně pro výběrový průměr
**Z<sub>n</sub>=√n(X̄<sub>n</sub>−μ)/σ ⇒ N(0,1)**.

Součet má střední hodnotu nμ a rozptyl nσ², proto odečteme nμ a dělíme σ√n. U průměru je typická chyba řádu **σ/√n**; faktor √n ji zvětší na netriviální měřítko. Po standardizaci má součet či průměr mnoha nezávislých příspěvků přibližně normální rozdělení, do značné míry bez ohledu na původní tvar rozdělení.

## Poznámka Anki 1783851674946

Karty Anki: 1783851674946
GUID: O8~wK+/wpr; štítky: centralni_limitni_veta integrace konsolidace::blok_5 limitni_vety zakon_velkych_cisel.

### Otázka (Front)

Jak spolu souvisejí nerovnosti, zákony velkých čísel a centrální limitní věta?

### Odpověď (Back)

Jde o tři úrovně asymptotické informace:

1. **Markovova a Čebyševova nerovnost** dávají obecné horní meze pravděpodobností odchylek.
2. **Zákony velkých čísel** říkají, že X̄<sub>n</sub> míří k μ, tedy že chyba mizí.
3. **Centrální limitní věta** popisuje jemněji velikost a tvar chyby: X̄<sub>n</sub>−μ je typicky řádu σ/√n a po standardizaci je asymptoticky normální.

Tvrzení X̄<sub>n</sub>→μ tedy říká kam průměr míří; tvrzení √n(X̄<sub>n</sub>−μ)/σ⇒N(0,1) říká jak kolísá kolem cíle. Normální limit umožňuje konstruovat intervaly spolehlivosti a testy hypotéz.

## Poznámka Anki 1783851674947

Karty Anki: 1783851674947
GUID: Ho|Ai7_r-7; štítky: aproximace centralni_limitni_veta konsolidace::blok_5 normalni_rozdeleni.

### Otázka (Front)

Jak se centrální limitní věta používá k normální aproximaci součtu a výběrového průměru?

### Odpověď (Back)

Pro velké n přibližně platí
**S<sub>n</sub>=ΣX<sub>i</sub> ≈ N(nμ,nσ²)**,
**X̄<sub>n</sub> ≈ N(μ,σ²/n)**.

Proto
**P(X̄<sub>n</sub>≤a)≈Φ(√n(a−μ)/σ)**
a
**P(a≤X̄<sub>n</sub>≤b)≈Φ(√n(b−μ)/σ)−Φ(√n(a−μ)/σ)**,
kde Φ je CDF N(0,1).

Je nutné rozlišovat **přesnou** normalitu a **asymptotickou aproximaci**: je-li původní výběr normální, je průměr normální pro každé n; u obecnějších rozdělení dává CLV pouze aproximaci, která se typicky zlepšuje s rostoucím n.

