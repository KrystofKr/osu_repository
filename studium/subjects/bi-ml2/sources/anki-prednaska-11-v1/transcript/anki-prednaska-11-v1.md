# BI-ML2 – Přednáška 11

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291647

Karty Anki: 1785306291648
GUID: KmuK<!3YzD; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Co řeší NLP, jaké roviny jazyka rozlišuje a proč se prosadil statistický přístup?

### Odpověď (Back)

NLP je strojové zpracování lidského jazyka pro analýzu, klasifikaci či generování textu. Lingvistika rozlišuje: **syntax**—formální spojování znaků a pořadí slov; **sémantiku**—význam slov a struktur; **pragmatiku**—vztah sdělení k osobám a situaci. Gramaticky správná věta může mít nejasný či kontextově nevhodný význam, proto syntax sama nestačí; ML úlohy často míří na význam, např. téma či sentiment.

Pravidlový přístup ručně specifikuje gramatická a další pravidla, ale naráží na výjimky, nejednoznačnost, kontext a potřebu metapravidel. Statistický přístup místo toho považuje text za data a vztahy odhaduje z rozsáhlého reprezentativního vzorku; více dat poskytuje více pozorování pro odhad parametrů.

## Poznámka Anki 1785306291649

Karty Anki: 1785306291650
GUID: VeeA0g/v#f; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Co je korpus a proč musí odpovídat cílové NLP úloze?

### Odpověď (Back)

Dokument je jednotlivý text; korpus je strukturovaná či nestrukturovaná kolekce dokumentů/textových jednotek používaná jako jazyková data. Anotovaný korpus obsahuje navíc ruční či automatické informace, např. lemmata, slovní druhy, morfologické značky nebo syntaktické vztahy.

Model se učí rozdělení a zákonitosti korpusu, proto systematicky odlišný nereprezentativní korpus vede ke špatné generalizaci na cílové texty.

## Poznámka Anki 1785306291651

Karty Anki: 1785306291652
GUID: afJQ$8+j-f; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Jak funguje bag-of-words a kdy je ignorování pořadí přijatelné či zásadně omezující?

### Odpověď (Back)

Bag-of-words (BoW) popíše dokument výskyty tokenů ze slovníku 𝒟 a chápe jej jako neuspořádanou množinu/multiset. Zachová, která slova se objevila a případně kolikrát, ale ztratí pořadí, syntax a většinu lokálního kontextu.

Může stačit pro tématickou klasifikaci, spam či některé sentimentové úlohy. Je nevhodný pro překlad, generování a detailní porozumění závislé na sekvenčním kontextu. Slovník vznikne výběrem různých tokenů z předzpracovaného korpusu; každý token pak definuje jeden příznak.

## Poznámka Anki 1785306291653

Karty Anki: 1785306291654
GUID: Ro/c4Q)LnB; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Co je dokumentově-termová matice a proč je vysokodimenzionální a řídká?

### Odpověď (Back)

Pro N dokumentů a slovník D má matice X rozměr N×D. Řádek je D-rozměrný dokument; sloupec představuje term napříč dokumenty; při četnostní reprezentaci X<sub>ij</sub> udává počet výskytů j-tého termu v i-tém dokumentu.

Dimenze je vysoká, protože každý term má vlastní sloupec; u flektivní češtiny ji bez normalizace dále násobí mnoho tvarů téhož lexému. Matice je zároveň řídká—dokument používá jen zlomek slovníku, takže většina prvků je nulová. Řídký formát ukládá hlavně nenulové hodnoty a šetří paměť i výpočet. Prostý BoW tak kombinuje vysokou dimenzi, řídkost a nevhodné stejné zacházení s velmi běžnými i vzácnými slovy.

## Poznámka Anki 1785306291655

Karty Anki: 1785306291656
GUID: S5sX>La|dO; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Jak se mají odstraňovat stop slova a interpunkce a proč záleží na úloze?

### Odpověď (Back)

Stop slova jsou velmi časté či málo rozlišující termy, např. spojky, předložky, členy a pomocná slovesa. Jejich odstranění zmenší slovník a náklady, ale četnost sama neznamená neužitečnost: slovo časté v jednom rozsáhlém tématu může být klíčovým indikátorem. Automatický práh podle podílu dokumentů tak může poškodit shlukování; seznam musí odpovídat konkrétnímu cíli.

Interpunkce se v BoW často odstraňuje ze stejného důvodu, ne však bezpodmínečně. Emotikony a některá znaménka mohou nést sentiment, tón či styl.

## Poznámka Anki 1785306291657

Karty Anki: 1785306291658
GUID: +jtsMN4;3j; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Jak lemmatizace a morfologické tagování předzpracovávají český text?

### Odpověď (Back)

Lemmatizace nahrazuje konkrétní ohýbaný povrchový tvar kanonickým lemmatem—např. infinitivem či 1. pádem—čímž slučuje gramatické varianty do jednoho příznaku a výrazně pomáhá flektivní češtině. Není triviální: správná analýza závisí na kontextu a víceznačných tvarech. Morfologické tagování přiřazuje slovní druh, rod, číslo, pád apod. a pomáhá vybrat správné lemma. Materiál uvádí MorphoDiTa (ÚFAL MFF UK), jejíž automatický výstup může chybovat.

Typická pipeline: tokenizace → sjednocení velikosti písmen → výběrové odstranění znaků a stop slov → případná lemmatizace → vektorizace. Lowercase slučuje varianty, ale může zničit informaci ve vlastních jménech, zkratkách či jinak významově odlišných výrazech.

## Poznámka Anki 1785306291659

Karty Anki: 1785306291660
GUID: @}hTmNxgjw; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Co je tf-idf a jaké varianty term frequency lze použít?

### Odpověď (Back)

Tf-idf = term frequency–inverse document frequency. Váha má být vysoká, když je term významný v konkrétním dokumentu, ale ne běžný v korpusu; skládá se z tf(w,d) a idf(w,C).

Varianty tf: binární 1/0 podle přítomnosti; četnost f<sub>w,d</sub>; logaritmická log(1+f<sub>w,d</sub>), která tlumí mnohonásobné opakování a díky +1 dává nepřítomnému termu log1=0; nebo normalizovaná
tf(w,d)=1/2+(1/2)·f<sub>w,d</sub>/max<sub>w′∈d</sub>f<sub>w′,d</sub>,
která omezuje vliv absolutní délky a celkové četnosti dokumentu.

## Poznámka Anki 1785306291661

Karty Anki: 1785306291662
GUID: 9g1WcHF!bs; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Jak se počítá idf a výsledná tf-idf váha a jak se interpretují?

### Odpověď (Back)

Document frequency df(w) je počet dokumentů obsahujících w. Základní
idf(w,C)=log(|C|/|{d∈C:w∈d}|).
S rostoucím df idf klesá; vzácný term má vyšší idf a term ve všech dokumentech idf=log1=0. Výsledná
tf-idf(w,d)=tf(w,d)·idf(w,C).
Je vysoká pro term častý v daném dokumentu, ale vzácný napříč korpusem; nízká, když term chybí, je lokálně slabý nebo globálně běžný. I vzácný term má v dokumentu nulovou váhu, pokud tf=0.

Tf-idf není jediná pevná transformace—existují varianty tf, idf, vyhlazení a normalizace. Tf vyžaduje jen dokument, idf celý korpus.

## Poznámka Anki 1785306291663

Karty Anki: 1785306291664
GUID: 3mCo<f/TTJ; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Jak se správně učí tf-idf vectorizér bez data leakage?

### Odpověď (Back)

Nejprve rozdělíme surové dokumenty na train/test. Vectorizér (např. scikit-learn TfidfVectorizer) se **fitne pouze na train**: naučí slovník a idf; test se jen transformuje stejným slovníkem a idf. Term mimo trénovací slovník nemá sloupec a obvykle se ignoruje.

Fit před rozdělením by dovolil slovníku či idf využít testová data, tedy data leakage a nadhodnocené hodnocení. Po transformaci se textová úloha stane numerickou tabulkou s dokumenty v řádcích a termy ve sloupcích.

## Poznámka Anki 1785306291665

Karty Anki: 1785306291666
GUID: tk3J-3@9GE; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Které modely fungují nad BoW/tf-idf a jak se řídká reprezentace liší od embeddingů?

### Odpověď (Back)

Nad vysokodimenzionálními textovými vektory lze použít logistickou regresi, SVC a naivní Bayes. Naivní Bayes efektivně pracuje s řídkými četnostmi a silný předpoklad nezávislosti snižuje datové nároky. Lineární modely bývají účinné, protože samotné termy jsou informativní a jejich vážený součet dobře odděluje témata či sentiment.

BoW/tf-idf dává každému termu nezávislou řídkou souřadnici, takže nevyjadřuje podobnost různých slov. Embedding je hustý, obvykle nížerozměrný naučený vektor, v němž lze sdílet sémantickou strukturu. Klasický přístup je jednoduchý, interpretovatelný a účinný v řídkém formátu, ale ignoruje pořadí, kompozici významu a širší kontext.

## Poznámka Anki 1785306291667

Karty Anki: 1785306291668
GUID: bDfnZ2eAZg; štítky: BI-ML2 iterace_11 Konsolidovano Prednaska_11.

### Otázka (Front)

Jaká je celá klasická pipeline klasifikace dokumentů a jaký kompromis představuje?

### Odpověď (Back)

Korpus → rozdělení dat → předzpracování → slovník → řídké dokumentové vektory → případné tf-idf → klasifikátor. Stop slova odstraňují zvolené málo užitečné termy, lemmatizace slučuje gramatické varianty a tf-idf váží zbytek podle lokální četnosti a globální vzácnosti.

BoW obětuje pořadí a část jazykové struktury výměnou za jednoduchou, škálovatelnou numerickou reprezentaci použitelnou standardními metodami strojového učení.

