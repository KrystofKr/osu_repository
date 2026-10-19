# BI-ZUM – 06 neuronove site

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610599

Karty Anki: 1785298610599
GUID: m1FZ>ye^B~; štítky: AI_combined::06_neuronove_site iterace_04 src_282-287.

### Otázka (Front)

Jak funguje umělý neuron a klasický perceptron a jaký význam mají váhy, bias a práh?

### Odpověď (Back)

Umělá neuronová síť skládá propojené neurony; biologickou inspirací jsou dendrity (vstupy), tělo neuronu (integrace) a axon (výstup). Umělý neuron počítá vážený součet a aktivaci.

**Perceptron:** z=w·x+b a skoková funkce vytvoří binární výstup podle znaménka z. Váha wᵢ určuje znaménko a sílu vlivu xᵢ; bias b posouvá rozhodovací hranici a určuje snadnost aktivace. Prahový zápis w·x>θ je ekvivalentní w·x+b>0 pro b=−θ.

## Poznámka Anki 1785298610600

Karty Anki: 1785298610600
GUID: pbabO&?^U-; štítky: AI_combined::06_neuronove_site iterace_04 src_288-294.

### Otázka (Front)

Proč je perceptron lineární klasifikátor, proč nezvládne XOR a jak to řeší vícevrstvý perceptron?

### Odpověď (Back)

Rozhodovací hranice perceptronu je nadrovina w·x+b=0. Data jsou **lineárně separabilní**, pokud je lze přímkou/rovinou/nadrovinou rozdělit bez chyb. XOR takto oddělit nelze, proto jej jeden perceptron nereprezentuje.

**Vícevrstvý perceptron (MLP)** skládá lineární transformace a nelineární aktivace, a tím vytváří nelineární hranice. Bez nelinearity by libovolně mnoho vrstev bylo stále jedinou lineární transformací.

Příklad NAND: w₁=w₂=−2, b=3; výraz −2x₁−2x₂+3 je nekladný jen pro (1,1). Skládáním takových neuronů lze realizovat složité logické obvody, např. úplnou sčítačku.

## Poznámka Anki 1785298610601

Karty Anki: 1785298610601
GUID: EPZO|a.~)v; štítky: AI_combined::06_neuronove_site iterace_04 src_295-299.

### Otázka (Front)

Jak se liší skokový perceptron od sigmoidního neuronu a proč se sigmoid lépe učí gradientem?

### Odpověď (Back)

Skoková aktivace se při malé změně parametrů obvykle nezmění vůbec, ale při překročení prahu skočí; není hladká a gradientní trénování je obtížné.

**Sigmoidní neuron** používá σ(z)=1/(1+e<sup>−z</sup>) pro z=w·x+b. Pro velké záporné z se blíží 0, pro velké kladné 1 a mezi nimi hladce přechází, takže aproximuje skokovou funkci. Malé změny vah a biasu způsobují malé změny výstupu a umožňují diferencovatelnou ztrátu.

Perceptron má diskrétní binární výstup; sigmoid spojitý výstup v (0,1).

## Poznámka Anki 1785298610602

Karty Anki: 1785298610602
GUID: Kag%fgXi3]; štítky: AI_combined::06_neuronove_site iterace_04 src_300-305.

### Otázka (Front)

Jak je uspořádána dopředná plně propojená neuronová síť a jakou roli mají její vrstvy?

### Odpověď (Back)

V **dopředné síti** informace proudí od vstupu přes skryté vrstvy k výstupu bez zpětných cyklů.

- **Vstupní vrstva:** reprezentuje vstupní vektor a obvykle neprovádí naučenou transformaci.
- **Skryté vrstvy:** vytvářejí interní reprezentace a postupně složitější rysy.
- **Výstupní vrstva:** převádí poslední reprezentaci na požadovaný typ predikce — skóre, pravděpodobnost či reálnou hodnotu.
**Plně propojené** sousední vrstvy znamenají, že každý neuron další vrstvy přijímá výstup každého neuronu předchozí vrstvy, každý s vlastní vahou. Jde o základní obecnou architekturu a stavební prvek složitějších sítí.

## Poznámka Anki 1785298610603

Karty Anki: 1785298610603
GUID: z:_h<PmDq1; štítky: AI_combined::06_neuronove_site iterace_04 src_306-312.

### Otázka (Front)

Jak se trénování neuronové sítě převádí na optimalizaci a jak je definována střední kvadratická chyba?

### Odpověď (Back)

Cílem je nastavit váhy w a biasy b tak, aby síť aproximovala požadované y(x): (1) zvolí se skalární **ztrátová/cost/objective funkce** měřící nesoulad a (2) minimalizuje se vzhledem k parametrům.

Ve zdroji: C(w,b)=1/(2n)·Σ<sub>x</sub>||y(x)−a(x)||², kde n je počet příkladů a a(x) výstup sítě. Kvadrát dává nezáporné příspěvky, více trestá velké chyby a je hladký; dělení n průměruje a 1/2 se při derivaci zruší s koeficientem 2.

Hladkost je důležitá, protože malé změny parametrů předvídatelně mění ztrátu a derivace udávají lokální směr její změny.

## Poznámka Anki 1785298610604

Karty Anki: 1785298610604
GUID: PxxwzEX2b<; štítky: AI_combined::06_neuronove_site iterace_04 src_313-318.

### Otázka (Front)

Co je gradientní sestup a jak rychlost učení ovlivňuje aktualizaci parametrů?

### Odpověď (Back)

**Gradient** skalární funkce je vektor parciálních derivací; ukazuje směr nejrychlejšího růstu a jeho velikost lokální rychlost růstu. Gradientní sestup proto aktualizuje souhrnný vektor parametrů θ opačným směrem:

**θ ← θ − η∇C(θ)**.

Learning rate η určuje velikost kroku. Příliš vysoká může minimum přeskakovat, oscilovat nebo ztrátu zvyšovat; příliš nízká vede k velmi pomalému učení a mnoha aktualizacím.

## Poznámka Anki 1785298610605

Karty Anki: 1785298610605
GUID: gxqHtMeFz3; štítky: AI_combined::06_neuronove_site iterace_04 src_319-327 src_334-335.

### Otázka (Front)

Co je backpropagation, jak se liší od gradientního sestupu a jak probíhá jedna trénovací iterace?

### Odpověď (Back)

**Backpropagation** efektivně počítá gradient ztráty podle všech vah a biasů opakovaným řetězovým pravidlem. Po dopředném výpočtu šíří informaci o chybě od výstupu zpět a využívá uložené mezivýsledky.

**Iterace:** (1) dopředný průchod vypočte aktivace a predikci → (2) spočítá se ztráta → (3) backpropagation vypočte derivace → (4) optimalizátor, např. gradientní sestup, aktualizuje parametry.

Backpropagation tedy **počítá gradienty**; gradientní sestup je **používá k aktualizaci**. Celý rámec: architektura určuje predikci, ztráta měří chybu, backpropagation citlivost parametrů a optimalizátor parametry mění.

## Poznámka Anki 1785298610606

Karty Anki: 1785298610606
GUID: t%z3r}-)_z; štítky: AI_combined::06_neuronove_site iterace_04 src_328-333.

### Otázka (Front)

Co je hluboké učení, jak se liší od tradičního přístupu k příznakům a co umožňuje hierarchie reprezentací?

### Odpověď (Back)

Hluboké učení se učí **hierarchii reprezentací**: každá vrstva kombinuje jednodušší vzory z předchozí vrstvy do abstraktnějších a úlohově relevantnějších konceptů. Podle terminologie zdroje má hluboká síť alespoň tři skryté vrstvy.

Tradiční přístup používá ručně navržené složité příznaky a jednodušší model; deep learning přijímá syrovější vstupy a složité příznaky se učí sám. Příklady: popis obrázků, Go, text→obraz, 3D rekonstrukce/generování, syntéza obrazu, řeč a překlad.

Aritmetika v latentním prostoru 3D objektů ukazuje, že vektory mohou zachytit sémantické vlastnosti a jejich algebraické operace odpovídat smysluplným změnám objektu.

