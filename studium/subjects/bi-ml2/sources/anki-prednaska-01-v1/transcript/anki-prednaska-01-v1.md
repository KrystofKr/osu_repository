# BI-ML2 – Přednáška 01

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::4 BI-ML2
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785306291379

Karty Anki: 1785306291380
GUID: T:[I#R_q#E; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Jak je formulována vícerozměrná lineární regrese a jak se získá řešení OLS?

### Odpověď (Back)

**Model jednoho pozorování:** Y = wᵀx + ε, kde x obsahuje příznaky (případně i konstantní příznak pro intercept), w jsou parametry a E[ε] = 0. Proto E[Y|x] = wᵀx a predikce Ŷ = ŵᵀx je bodovým odhadem této podmíněné střední hodnoty.

**Celý trénovací soubor:** Y = Xw + ε; řádek i matice X je xᵢᵀ.

**OLS:** minimalizuje RSS(w) = ‖Y − Xw‖² = Σᵢ(Yᵢ − xᵢᵀw)². Položením gradientu na nulu vznikne normální rovnice XᵀXw = XᵀY. Je-li XᵀX regulární, ŵ<sub>OLS</sub> = (XᵀX)⁻¹XᵀY. Je-li singulární, lze použít Mooreovu–Penroseovu pseudoinverzi nebo regularizaci (např. hřebenovou regresi).
 [Obrázek: paste-b599438393a7b7319782d47be4e0ba390c59e7be.jpg; soubor je v media/ v doprovodném ZIP] 
 [Obrázek: paste-e87d368feb475d1e527d6bda6566bf355dba09be.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1785306291381

Karty Anki: 1785306291382
GUID: g!G-/jVM!b; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Jak funguje hřebenová regrese včetně řešení, významu λ a práce s interceptem?

### Odpověď (Back)

Minimalizuje RSS<sub>λ</sub>(w) = ‖Y − Xw‖² + λwᵀI₀w, kde I₀ má u interceptu 0 a u ostatních parametrů 1. Intercept se obvykle nepenalizuje: určuje globální posun, ne citlivost na příznaky, a jeho penalizace by závisela na zvoleném počátku škály Y.

Uzavřené řešení je ŵ<sub>λ</sub> = (XᵀX + λI₀)⁻¹XᵀY. Parametr λ řídí kompromis mezi shodou s daty a malými vahami; větší λ více zmenšuje penalizované koeficienty. Pro λ = 0 dostáváme OLS, pokud je jeho řešení dobře definováno.

## Poznámka Anki 1785306291383

Karty Anki: 1785306291384
GUID: V0GboJH*.g; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Co je lineární model bázových funkcí, jak se trénuje a jaké báze lze použít?

### Odpověď (Back)

[Obrázek: paste-5e720cbc3155e30f68951bedcb1816939e11c089.jpg; soubor je v media/ v doprovodném ZIP]  [Obrázek: paste-f0fd5b0ac46c7cc816a7430439acbfea2b82efd1.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1785306291385

Karty Anki: 1785306291386
GUID: AZ|QRq^2Al; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Jak a proč se regularizovaný model bázových funkcí převádí do duální reprezentace?

### Odpověď (Back)

[Obrázek: paste-8adf7d91677736407365b517527ed5e51657c812.jpg; soubor je v media/ v doprovodném ZIP]  [Obrázek: paste-aa60f4f742e9f363dd12ffda862ec52b1a0b8cee.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1785306291387

Karty Anki: 1785306291388
GUID: s#:d)IS~xL; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Co je Gramova matice a jak souvisí s jádrem a podmínkami platného jádra?

### Odpověď (Back)

Gramova matice je G = ΦΦᵀ ∈ ℝ<sup>N×N</sup>; její prvek Gᵢⱼ = ϕ(xᵢ)ᵀϕ(xⱼ). Jádro odpovídající zobrazení ϕ je k(x, y) = ϕ(x)ᵀϕ(y), takže Gᵢⱼ = k(xᵢ, xⱼ).

G je symetrická, protože Gᵀ = G, a pozitivně semidefinitní, protože pro každý a platí aᵀGa = ‖Φᵀa‖² ≥ 0. Platné reálné jádro proto musí být symetrické a pro libovolnou konečnou množinu bodů vytvořit pozitivně semidefinitní Gramovu matici. Nemusí však být bodově nezáporné: některé hodnoty k(x, y) mohou být záporné.

Gramova matice je jádro vyhodnocené na všech dvojicích trénovacích bodů.

 [Obrázek: paste-43de32959a1fe84e64db8f3ae20f7c400af63375.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1785306291389

Karty Anki: 1785306291390
GUID: e$P1#J:@Qe; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Jak vypadá hřebenová regrese v duální (jádrové) reprezentaci?

### Odpověď (Back)

Po dosazení w = Φᵀα a G = ΦΦᵀ je účelová funkce RSS<sub>λ</sub>(α) = ‖Y − Gα‖² + λαᵀGα. Pro λ > 0 se používá kanonické řešení α̂ = (G + λI)⁻¹Y.

Matice G + λI je regulární: G je pozitivně semidefinitní, takže má nezáporná vlastní čísla, a přičtení λI je posune na kladné hodnoty.

Predikce je Ŷ(x) = Σᵢ₌₁ᴺ α̂ᵢk(xᵢ, x), tedy vážená lineární kombinace podobností nového bodu ke všem trénovacím bodům.
 [Obrázek: paste-9e784e98538d796f06b6acc7b94a99a740fc0d4b.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1785306291391

Karty Anki: 1785306291392
GUID: rPJsrSIlAB; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Co je jádrový trik, kdy ho lze použít a jak propojuje bázové funkce s hřebenovou regresí?

### Odpověď (Back)

Jádrový trik nahrazuje skalární součiny ϕ(x)ᵀϕ(y) přímo hodnotami k(x, y), takže se explicitně nekonstruují souřadnice ϕ(x). Lze jej použít, když algoritmus pracuje s transformovanými vstupy pouze prostřednictvím jejich skalárních součinů. Umožňuje tak efektivně využít velmi vysoké až nekonečně rozměrné příznakové prostory.

Explicitní model počítá ϕ(x) a váhy w; jádrová reprezentace používá párové hodnoty k(xᵢ, xⱼ) a duální koeficienty α.

**Přechod k jádrové regresi:** (1) zvolit transformaci ϕ, (2) regularizovat lineární model v transformovaném prostoru, (3) přepsat w = Φᵀα, (4) nahradit všechny skalární součiny transformovaných bodů jádrem. Hřebenová regrese tedy stabilizuje flexibilní model bázových funkcí a duální přepis zpřístupní jádrový trik.

## Poznámka Anki 1785306291393

Karty Anki: 1785306291394
GUID: %RiULy4f7L; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Jak se výpočetně porovnává primární a duální hřebenová regrese?

### Odpověď (Back)

Primární řešení invertuje matici M×M a přímá inverze má přibližně složitost O(M³), kde M je počet explicitních příznaků či bázových funkcí. Duální řešení invertuje matici N×N se složitostí přibližně O(N³), kde N je počet trénovacích bodů.

Duální reprezentace může být výhodnější pro M ≫ N; primární pro N ≫ M. Jde o orientační srovnání přímých maticových řešení.

 [Obrázek: paste-0339ea4676a3b5cff80532a5b2d013013fe7829d.jpg; soubor je v media/ v doprovodném ZIP] 
 [Obrázek: paste-86582d99779e457340a8d680dfe4c15fc00ea7c3.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1785306291395

Karty Anki: 1785306291396
GUID: a@+:*W8PGN; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Jak fungují lineární a nehomogenní polynomiální jádra včetně explicitního kvadratického příkladu?

### Odpověď (Back)

**Lineární jádro:** k(x, y) = xᵀy, odpovídá ϕ(x) = x.

**Nehomogenní polynomiální jádro stupně n:** k(x, y) = (xᵀy + 1)ⁿ. Člen +1 způsobí, že implicitní prostor obsahuje monomy všech stupňů od 0 do n, ne jen přesně stupně n.

Pro x ∈ ℝ² a n = 2 lze použít ϕ(x) = (1, √2x₁, √2x₂, x₁², x₂², √2x₁x₂)ᵀ. Faktory √2 zajistí, aby skalární součin reprodukoval koeficient 2 u smíšených členů rozvoje.

Pro vstup dimenze p má kvadratické nehomogenní jádro (p + 1)(p + 2)/2 implicitních příznaků. Pro 1024 pixelů je to 525 825. Při 1000 obrazech proto duální výpočet pracuje s Gramovou maticí 1000×1000 namísto primární matice přibližně 525 825×525 825.

## Poznámka Anki 1785306291397

Karty Anki: 1785306291398
GUID: Kj8f#JsSXv; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Jak je definováno Gaussovské (RBF) jádro a jak se interpretuje?

### Odpověď (Back)

k(x, y) = exp(−γ‖x − y‖²), kde γ > 0 řídí prostorovou škálu podobnosti. Je radiální (RBF), protože závisí pouze na vzdálenosti ‖x − y‖, nikoli na absolutní poloze či směru bodů. Pro blízké body je k blízko 1; s rostoucí vzdáleností podobnost rychle klesá k 0.

## Poznámka Anki 1785306291399

Karty Anki: 1785306291400
GUID: :ad<.L3U^H; štítky: BI-ML2 iterace_01 Konsolidovano Prednaska_01.

### Otázka (Front)

Co jsou kernel machine a vector machine a jak do nich zapadá duální jádrová regrese?

### Odpověď (Back)

Obecný jádrový model (kernel machine) má tvar f(x) = Σⱼ₌₁ᴷ αⱼk(μⱼ, x), kde μⱼ jsou zvolená centra a αⱼ koeficienty. Vector machine je jeho speciální případ, v němž jsou centra μⱼ vybrána z trénovacích bodů.

Duální jádrová regrese má f(x) = Σᵢ₌₁ᴺ αᵢk(xᵢ, x): používá všechny trénovací body jako centra, a je tedy vector machine.

