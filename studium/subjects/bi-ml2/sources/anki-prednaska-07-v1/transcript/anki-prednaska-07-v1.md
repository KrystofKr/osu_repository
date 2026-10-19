# BI-ML2 – Přednáška 07

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291525

Karty Anki: 1785306291526
GUID: K8Uayl&$HE; štítky: BI-ML2 iterace_07 Konsolidovano Prednaska_07.

### Otázka (Front)

Jak perceptron vznikl a jak počítá binární predikci?

### Odpověď (Back)

McCullochův–Pittsův neuron sčítal logické vstupy, porovnal je s prahem a vytvořil binární výstup. Rosenblattův perceptron přidal spojité vstupy, trénovatelné váhy a iterativní učení z označených dat.

Jednovrstvý perceptron je jeden binární lineární klasifikátor. Jeho potenciál je ξ=wᵀx+w₀=Σⱼwⱼxⱼ+w₀; w jsou váhy a w₀ intercept/bias. Pro třídy {0,1} používá g(ξ)=1 pro ξ≥0, jinak 0, tedy Ŷ=g(wᵀx+w₀). Aktivuje se, když Σⱼwⱼxⱼ≥−w₀, proto se −w₀ označuje jako práh.

## Poznámka Anki 1785306291527

Karty Anki: 1785306291528
GUID: #q<8O!r$oG; štítky: BI-ML2 iterace_07 Konsolidovano Prednaska_07.

### Otázka (Front)

Jaká je geometrie perceptronu a jak se zapisuje pomocí rozšířených vektorů a znaménkových štítků?

### Odpověď (Back)

Hranice wᵀx+w₀=0 je nadrovina s normálou w; dělí prostor na poloprostor s predikcí 1 (skóre ≥0) a 0 (skóre <0). Orientovaná vzdálenost bodu je (wᵀx+w₀)/‖w‖. Perceptron je lineární klasifikátor, protože o třídě rozhoduje znaménko afinní funkce, i když skoková aktivace je nelineární.

Intercept zahrneme jako x̃=(1,x₁,…,x<sub>p</sub>)ᵀ a w̃=(w₀,w₁,…,w<sub>p</sub>)ᵀ, takže w̃ᵀx̃=wᵀx+w₀. Štítek Y∈{0,1} převedeme na t=2Y−1∈{−1,1}. Správná klasifikace obou tříd je jedinou podmínkou tᵢx̃ᵢᵀw̃>0: pro t=1 vyžaduje kladné a pro t=−1 záporné skóre.

## Poznámka Anki 1785306291529

Karty Anki: 1785306291530
GUID: (m7ACi1]?p; štítky: BI-ML2 iterace_07 Konsolidovano Prednaska_07.

### Otázka (Front)

Jak funguje perceptronový update a proč posouvá chybně klasifikovaný bod správným směrem?

### Odpověď (Back)

Algoritmus prochází body a při chybě okamžitě upraví parametry. Pro Y∈{0,1} je error=Y−Ŷ a
w←w+(Y−Ŷ)x,   w₀←w₀+(Y−Ŷ).
Chybný kladný bod přičte x a 1, čímž zvýší skóre; chybný záporný bod je odečte a skóre sníží. V rozšířeném zápisu se potenciál aktualizovaného bodu změní správným směrem o ‖x̃‖².

Pro t∈{−1,1}: při tᵢx̃ᵢᵀw̃<sub>k</sub>≤0 se provede w̃<sub>k+1</sub>=w̃<sub>k</sub>+tᵢx̃ᵢ, jinak beze změny; sjednoceně
w̃<sub>k+1</sub>=w̃<sub>k</sub>+1[tᵢx̃ᵢᵀw̃<sub>k</sub>≤0]tᵢx̃ᵢ.
Podmínka zahrnuje špatnou stranu i bod přímo na hranici. To se drobně liší od skokové funkce, která při skóre 0 predikuje 1: formální algoritmus vyžaduje striktně kladný odstup a na hranici aktualizuje.

## Poznámka Anki 1785306291531

Karty Anki: 1785306291532
GUID: #yLPf_)96p; štítky: BI-ML2 iterace_07 Konsolidovano Prednaska_07.

### Otázka (Front)

Proč je perceptron online algoritmus a jak vypadá jeho základní trénovací smyčka?

### Odpověď (Back)

Online trénování aktualizuje parametry ihned po jednotlivém bodu; perceptron tak činí po každé chybě místo agregace přes dataset. Základní verze začíná w̃₀=0 a cyklicky prochází N bodů, například i(k)=(k mod N)+1 při indexování od 1. Trénování skončí, když celý průchod všemi body nevyvolá žádnou změnu vah.

## Poznámka Anki 1785306291533

Karty Anki: 1785306291534
GUID: RJ-9o)V{1b; štítky: BI-ML2 iterace_07 Konsolidovano Prednaska_07.

### Otázka (Front)

Co předpokládá a zaručuje věta o konvergenci perceptronu?

### Odpověď (Back)

Lineární separabilita znamená existenci w̃* s tᵢx̃ᵢᵀw̃*>0 pro všechny body. Věta používá normalizovaný silnější zápis: existují jednotkový ‖w̃*‖=1 a γ>0 takové, že tᵢx̃ᵢᵀw̃*>γ, a současně ‖x̃ᵢ‖≤R.

γ je kladná dolní mez geometrického odstupu v rozšířeném prostoru; jednotková norma odstraní libovolnou škálu. Počet chybných aktualizací je nejvýše R²/γ². Pro separabilní omezená data tedy perceptron po konečně mnoha chybách najde nějakou separující nadrovinu. Nezaručuje však maximum-margin řešení jako SVM.

## Poznámka Anki 1785306291535

Karty Anki: 1785306291536
GUID: tbmTlZS+eO; štítky: BI-ML2 iterace_07 Konsolidovano Prednaska_07.

### Otázka (Front)

Jak se dokáže mez n≤R²/γ² ve větě o konvergenci perceptronu?

### Odpověď (Back)

Po n chybách platí dvě meze:

**1. Růst správným směrem:** každý update přidá tᵢx̃ᵢ a zvětší w̃ᵀw̃* alespoň o γ, tedy w̃<sub>n</sub>ᵀw̃*≥nγ. Z Cauchyho–Schwarze a ‖w̃*‖=1 plyne ‖w̃<sub>n</sub>‖≥nγ.

**2. Omezený růst normy:**
‖w̃+tᵢx̃ᵢ‖²=‖w̃‖²+‖x̃ᵢ‖²+2tᵢx̃ᵢᵀw̃.
Při chybě je smíšený člen ≤0 a ‖x̃ᵢ‖≤R, proto se čtverec normy zvětší nejvýše o R². Po n chybách ‖w̃<sub>n</sub>‖²≤nR², tedy ‖w̃<sub>n</sub>‖≤√nR.

Spojením nγ≤√nR dostaneme pro n>0: n≤R²/γ².

## Poznámka Anki 1785306291537

Karty Anki: 1785306291538
GUID: @VY7klaVLe; štítky: BI-ML2 iterace_07 Konsolidovano Prednaska_07.

### Otázka (Front)

Jak γ, R, škálování příznaků a neseparabilita ovlivňují perceptron?

### Odpověď (Back)

Větší odstup γ zmenšuje mez R²/γ², takže dobře separovaná data vyžadují teoreticky méně chyb. Větší maximální norma R ji naopak zvětšuje. Škálování příznaků mění normy, relativní příspěvky souřadnic, geometrii odstupu i trajektorii aktualizací.

U neseparabilních dat neexistuje jediná nadrovina správná pro všechny body, takže nelze dosáhnout průchodu s nulovou chybou; záruka konvergence neplatí a základní algoritmus může aktualizovat neomezeně dlouho.

## Poznámka Anki 1785306291539

Karty Anki: 1785306291540
GUID: f}=Md|h4;s; štítky: BI-ML2 iterace_07 Konsolidovano Prednaska_07.

### Otázka (Front)

Proč jednovrstvý perceptron neumí XOR a jak jej řeší více neuronů?

### Odpověď (Back)

Jeden perceptron reprezentuje jen lineární hranici. XOR má tabulku 00→0, 01→1, 10→1, 11→0; kladné a záporné body leží v protilehlých rozích, takže je nelze oddělit jednou přímkou.

Nejde o omezení neuronových sítí obecně. Více perceptronů může ve skryté vrstvě vytvořit pomocné logické příznaky a výstupní neuron je zkombinuje do XOR. Skryté neurony tedy transformují vstupy do prostoru, kde jsou výsledné třídy lineárně separabilní.

## Poznámka Anki 1785306291541

Karty Anki: 1785306291542
GUID: xH4D[bDv[Q; štítky: BI-ML2 iterace_07 Konsolidovano Prednaska_07.

### Otázka (Front)

Proč nelze perceptronový update přímo použít ve vícevrstvé síti a co umožnilo její trénování?

### Odpověď (Back)

Výstupní chyba neurčuje cílové hodnoty skrytých neuronů, takže vzniká problém přiřazení odpovědnosti: jak jednotlivé vnitřní váhy přispěly k chybě. Efektivní trénování umožnily diferencovatelné aktivace, diferencovatelná účelová funkce, gradientní sestup a zpětné šíření derivací vrstvami.

Perceptron provádí diskrétní update jen při chybné klasifikaci; moderní síť gradientem průběžně minimalizuje hladkou ztrátu.

## Poznámka Anki 1785306291543

Karty Anki: 1785306291544
GUID: nn|Xa]&=:q; štítky: BI-ML2 iterace_07 Konsolidovano Prednaska_07.

### Otázka (Front)

Jak se perceptron vztahuje k lineární diskriminační funkci, SVM, logistické regresi a vícevrstvé síti?

### Odpověď (Back)

Perceptron i lineární diskriminační funkce používají wᵀx+w₀ a znaménko; „perceptron“ navíc označuje skokový neuron a konkrétní online učicí algoritmus.

Oproti hard-margin SVM hledá libovolnou separující nadrovinu, nikoli maximum-margin optimum. Oproti logistické regresi má skokový nepravidelný výstup bez pravděpodobností, zatímco logistická regrese používá hladký sigmoid a modeluje P(Y=1|X).

Koncepční přechod: jeden neuron → lineární hranice → XOR ukáže nedostatečnou expresivitu → více vrstev skládá nelineární příznaky → diferencovatelnost umožní společné trénování gradientem.

