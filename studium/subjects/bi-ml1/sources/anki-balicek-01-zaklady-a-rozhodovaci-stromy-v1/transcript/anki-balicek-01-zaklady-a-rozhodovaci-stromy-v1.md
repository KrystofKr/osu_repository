# BI-ML1 – 01 Zaklady a rozhodovaci stromy

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::3 BI-ML1::01 Zaklady a rozhodovaci stromy
Rozsah: 15 poznámek, 15 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785269100001

Karty Anki: 1785269200001
GUID: 5eb1c266bc2f; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Vysvětli pojmy **cílová proměnná**, **příznak**, **parametry** a **učení modelu**. Jak učení souvisí s optimalizací?

### Odpověď (Back)

- **Cílová (vysvětlovaná) proměnná Y:** veličina, kterou chceme predikovat nebo vysvětlit.
- **Příznak X<sub>j</sub>:** měřená či odvozená charakteristika vstupu použitá k predikci Y.
- **Parametry:** číselné hodnoty určující konkrétní chování modelu; odhadují se z trénovacích dat.
- **Učení:** odhad parametrů tak, aby model co nejlépe splnil kritérium kvality. Často jde o optimalizaci: minimalizaci chyby, případně maximalizaci jiné účelové funkce.

## Poznámka Anki 1785269100002

Karty Anki: 1785269200002
GUID: b629b441297c; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Jak se liší **parametry** a **hyperparametry** modelu a co je ladění hyperparametrů?

### Odpověď (Back)

**Parametry** se odhadují z trénovacích dat při běžném učení konkrétního modelu. **Hyperparametry** určují jeho strukturu, složitost nebo způsob učení a volí se samostatně (např. maximální hloubka stromu). **Ladění** vybírá hodnoty hyperparametrů s nejlepším odhadem generalizace.

## Poznámka Anki 1785269100003

Karty Anki: 1785269200003
GUID: ddf418a404bd; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Porovnej **supervizované** a **nesupervizované** učení a uveď typické úlohy nesupervizovaného učení.

### Odpověď (Back)

| Supervizované | Nesupervizované | 
| Známe příznaky X i správné cíle Y; „učitelem“ jsou právě hodnoty Y. Model se učí vztah X → Y. | Cíl Y není zadán; hledáme strukturu samotných příznaků. | 

Typické nesupervizované úlohy:

- **shlukování** objektů podle podobnosti, např. segmentace zákazníků;
- **detekce anomálií**, např. podezřelých transakcí při neúplných štítcích podvodů.

## Poznámka Anki 1785269100005

Karty Anki: 1785269200005
GUID: 9c17d779a640; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Jak se formuluje cíl supervizovaného učení a jak se liší **klasifikace**, **binární klasifikace** a **regrese**?

### Odpověď (Back)

Hledáme funkci f tak, aby **Y ≈ f(X<sub>1</sub>,…,X<sub>p</sub>)**.
| Úloha | Cílová proměnná | 
| Klasifikace | Diskrétní třída z konečné či malé množiny. | 
| Binární klasifikace | Právě dvě třídy, např. nemocný/zdravý. | 
| Regrese | Číselná veličina, kterou je rozumné považovat za spojitou. |

## Poznámka Anki 1785269100006

Karty Anki: 1785269200006
GUID: fd637be193aa; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Jak rozhodovací strom vytváří predikci a co znamenají jeho **vnitřní uzly** a **listy**? Lze jej použít pro klasifikaci i regresi?

### Odpověď (Back)

Strom vede vstup od **kořene** postupnými testy příznaků až do jednoho **listu**.

- **Vnitřní uzel:** test příznaku; výsledek určí větev.
- **List:** konečná predikce.
Ano: klasifikační strom vrací diskrétní třídu, regresní strom číselnou hodnotu.

## Poznámka Anki 1785269100007

Karty Anki: 1785269200007
GUID: a61a6e49b83e; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Proč se optimální rozhodovací strom obvykle nehledá úplným prohledáním a jak strom konstruuje **ID3**? Jaký je důsledek jeho hladovosti?

### Odpověď (Back)

Počet možných stromů roste kombinatoricky a konstrukce optimálního stromu je **NP-úplná**: pro obecný případ neznáme polynomiální algoritmus, úplné prohledání je prakticky neúnosné.

**ID3** proto používá hladovou rekurzi: v uzlu zvolí aktuálně nejlepší rozdělení, rozdělí data a postup opakuje v potomcích. Lokální volby nepřehodnocuje, takže lokálně nejlepší split může zablokovat lepší pozdější kombinaci. Ani maximální okamžitý informační zisk proto nezaručuje globálně optimální či perfektní strom.

## Poznámka Anki 1785269100008

Karty Anki: 1785269200008
GUID: 85ff534036e1; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Kdy se zastavuje růst rozhodovacího stromu a jak jeho hloubka souvisí s přeučením?

### Odpověď (Back)

Růst lze zastavit např. při:

- dosažení **max_depth**,
- příliš malém počtu vzorků v uzlu,
- čistém uzlu,
- nedostatečném zlepšení kritéria.

Vysoká přesnost na trénovacích datech sama nedokazuje kvalitu. Velmi hluboký strom může vytvářet malé listy, zapamatovat šum a zhoršit výkon na nových datech. **max_depth** tedy řídí složitost a riziko přeučení.

## Poznámka Anki 1785269100009

Karty Anki: 1785269200009
GUID: 68e4563acd6a; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Co je **nečistota uzlu** a jak je definována entropie? Uveď její hlavní vlastnosti pro binární uzel.

### Odpověď (Back)

[Obrázek: paste-69cdbf2b004213a0d6d275289de2e46ad9448bbb.jpg; soubor je v media/ v doprovodném ZIP]  [Obrázek: paste-8e36fc8029c4070061819068dceeb99e55e95411.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1785269100010

Karty Anki: 1785269200010
GUID: 25f89f70f3f5; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Co je **informační zisk** rozdělení a jak jej používá ID3? Jaké má krajní hodnoty?

### Odpověď (Back)

[Obrázek: paste-9c762f82de5d1203f869bfe806f280744971582b.jpg; soubor je v media/ v doprovodném ZIP] 

Entropie potomků se váží velikostí, protože větší potomek reprezentuje větší část dat. ID3 volí split s nejvyšším IG, tedy největším poklesem vážené entropie.

- Split zachovávající třídní poměry: **IG=0**.
- Dokonale čisté potomky: **IG=H(D)**.

## Poznámka Anki 1785269100011

Karty Anki: 1785269200011
GUID: 86045ea762dc; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Jak je definována a interpretována **Giniho nečistota**? Jak se použije při stavbě stromu a co sdílí s entropií?

### Odpověď (Back)

[Obrázek: paste-c85e244f67ab718d89be5c2490a4c8668a3056e7.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1785269100012

Karty Anki: 1785269200012
GUID: 7174d8afba21; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Jak se klasifikačnímu listu stromu přiřadí predikovaná třída a co se děje při shodě četností?

### Odpověď (Back)

List obvykle predikuje **nejčetnější třídu** mezi trénovacími vzorky, které do něj dopadly. Při shodě musí být určeno pravidlo, např. pevná priorita tříd, náhodná volba nebo jiné deterministické kritérium.

## Poznámka Anki 1785269100013

Karty Anki: 1785269200013
GUID: 08b61262a5c4; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Co je klasifikační **přesnost** a jak souvisí s chybovostí?

### Odpověď (Back)

**Přesnost (accuracy)** je podíl správně klasifikovaných vzorků ze všech hodnocených vzorků. Při jednoduché klasifikaci platí **chybovost = 1 − přesnost**.

## Poznámka Anki 1785269100014

Karty Anki: 1785269200014
GUID: ea66951498d7; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Porovnej **trénovací** a **testovací** data i chybu. Co je generalizace a proč data oddělujeme?

### Odpověď (Back)

|  | Trénovací | Testovací | 
| Data | Slouží k odhadu parametrů a vytvoření modelu. | Nezávislá data nepoužitá k učení ani výběru modelu; slouží k finálnímu odhadu. | 
| Chyba | Měřena na datech, z nichž se model učil. | Měřena na dosud neviděných datech, proto lépe odhaduje budoucí výkon. | 

**Generalizace** je schopnost uspět na nových datech ze stejného datového procesu. Oddělení dat brání tomu, abychom stejnými pozorováními model přizpůsobili i „nezávisle“ posoudili.

## Poznámka Anki 1785269100015

Karty Anki: 1785269200015
GUID: 800992faf378; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Co je **overfitting** a jak se s rostoucí složitostí typicky mění trénovací a testovací chyba? Jaký je skutečný cíl učení?

### Odpověď (Back)

**Overfitting**: model se přizpůsobí detailům a šumu trénovacích dat, má nízkou trénovací, ale vyšší chybu na nových datech.

- Složitější model: trénovací chyba obvykle klesá nebo zůstává stejná.
- Testovací chyba obvykle nejprve klesá (zachycení struktury), pak kvůli přeučení roste.

Cílem tedy není minimum trénovací chyby, ale minimum **očekávané chyby na nových datech**.

## Poznámka Anki 1785269100016

Karty Anki: 1785269200016
GUID: ae92c2c59e87; štítky: 01_Zaklady_a_rozhodovaci_stromy BI-ML1 konsolidace.

### Otázka (Front)

Proč se testovací množina nesmí používat k výběru **max_depth** ani jiné konfigurace? Proč je minimum z mnoha testovaných konfigurací optimistické?

### Odpověď (Back)

Jakmile podle testovacích výsledků vybereme hyperparametr, informace z testu ovlivnila model. Stejný test už není nezávislý a hlášená chyba je optimisticky zkreslená.

Z mnoha konfigurací navíc vybereme tu, která na konkrétním testovacím vzorku uspěla částečně náhodou; naměřené minimum proto podhodnocuje očekávanou chybu. Test se má použít **až jednou po učení a ladění**.

