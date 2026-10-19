# BI-APS – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 29 poznámek, 29 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1663663022373

Karty Anki: 1663663022373
GUID: bEWP}+B%OG; štítky: bi-aps::p01 bi-spol::29.

### Otázka (Front)

Definujte ISA.

### Odpověď (Back)

Instruction Set Architecture (ISA) je abstraktní rozhraní mezi hardware a nízkoúrovňovým software, které zahrnuje veškeré informace nezbytné k psaní korektních programů ve strojovém jazyce.

## Poznámka Anki 1663663119757

Karty Anki: 1663663119757
GUID: A3aC@Yr)<e; štítky: bi-aps::p01 bi-spol::29.

### Otázka (Front)

Vyjmenujte příklady dnes používaných ISA.

### Odpověď (Back)

- IA-32 (x86) a x86-64
- ARM32, ARM64
- AVR, AVR32
- RISC-V

## Poznámka Anki 1663663162254

Karty Anki: 1663663162254
GUID: gf#5)iNCU^; štítky: bi-aps::p01 bi-spol::29.

### Otázka (Front)

Co musí ISA definovat?

### Odpověď (Back)

- množina strojových instrukcí procesoru
- podporované datové typy
- adresní módy
- soubor registrů
- organizace paměti

## Poznámka Anki 1663663269708

Karty Anki: 1663663269708
GUID: zvVV-bY:$w; štítky: bi-aps::p01 bi-spol::29.

### Otázka (Front)

Rozdělte množinu strojových operací dle operace, kterou vykonávají.

### Odpověď (Back)

- výpočetní instrukce - aritmetické a logické instrukce
- instrukce pro řízení toku programu - skokové instrukce
- instrukce pro přístup do paměti - čtení a zápis obsahu v paměti
- speciální instrukce - např. breakpoint

## Poznámka Anki 1663663322391

Karty Anki: 1663663322391
GUID: dwcf0j!xHZ; štítky: bi-aps::p01 bi-spol::29.

### Otázka (Front)

Co je to složitá instrukce?

### Odpověď (Back)

Je to instrukce, která je schopna vykonat několik různých operací.

## Poznámka Anki 1663663430993

Karty Anki: 1663663430993
GUID: lyt~&1SxFp; štítky: bi-aps::p01.

### Otázka (Front)

Jak lze jednoznačně odlišit RISC a CISC?

### Odpověď (Back)

Pokud ISA obsahuje ALU instrukci, která je schopna zároveň přistupovat do paměti, jedná se o CISC.

## Poznámka Anki 1663663712937

Karty Anki: 1663663712937
GUID: eGgcVtPsYa; štítky: bi-aps::p01.

### Otázka (Front)

Porovnejte CISC a RISC.

### Odpověď (Back)

| 
      **Complex Instruction Set Computer** | 
      **Reduced Instruction Set Computer** | 

| 
      obvykle větší počet instrukcí | 
      obvykle menší počet instrukcí | 

| 
      instrukce různé délky (1B-13B) | 
      jedna nebo dvě délky instrukcí (2B, 4B) | 

| 
      obvykle mnoho adresních módů | 
      obvykle méně jednodušších adresních módů |

## Poznámka Anki 1663703660833

Karty Anki: 1663703660833
GUID: KQAPV.c-(r; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663703660833: v původním balíčku pozastavená karta.

### Otázka (Front)

Co vyjadřuje závorková notace u definice ISA?

### Odpověď (Back)

ISA (počet operandů, počet paměťových operandů), např. ISA s akumulátorem (1,1)

## Poznámka Anki 1663704108801

Karty Anki: 1663704108801
GUID: j#1a-2)}mH; štítky: bi-aps::p01 bi-spol::29.

Metadata původního zdroje pro kartu 1663704108801: původní příznak autora 6.

### Otázka (Front)

Vyjmenujte základní třídy ISA.

### Odpověď (Back)

- ISA se zásobníkem (0, 0) - prakticky zaniklá
- ISA s akumulátorem (1, 1) - pouze v jednoduchých mikrokontrolerech
- GPR ISA (3, 3) s memory-memory arch. - nepoužívá se
- GPR ISA (2, 0) s load/store a register-register arch. - Atmel AVR
- GPR ISA (3, 0) s load/store a register-register arch. - RISC
- GPR ISA (2, 1) s register-memory arch. - CISC

## Poznámka Anki 1663704448286

Karty Anki: 1663704448286
GUID: klMm/2|6Vo; štítky: bi-aps::p01 bi-spol::29.

### Otázka (Front)

Popište general purpose register (GPR).

### Odpověď (Back)

General purpose register (GPR) je malá paměť, která je velmi rychle přístupná pro procesor. GPR se využívá pro ukládání jak dat, tak adres, případně lze specializovat pro další formáty, jako jsou floating point čísla. Typicky se používají jako explicitní operandy aritmeticko-logické jednotky v GPR orientované ISA.

## Poznámka Anki 1663704683937

Karty Anki: 1663704683937
GUID: IU9~mAvkSg; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663704683937: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište výhody a nevýhody load/store (3, 0) architektury.

### Odpověď (Back)

**Výhody**

- pevná délka instrukce a jednoduché kódování
- jednoduché a rychlé dekódování instrukce a čtení/zápis hodnot z/do registrů
- všechny operandy ALU instrukcí jsou v registrech
- větší flexibilita při využívání registrů, jejichž počet je vždy omezen
- snadná implementace zřetězeného zpracování (pipelining)

**Nevýhody**

- menší hustota kódování
- nutnost použít instrukce \(\mathtt{load}\) a \(\mathtt{store}\) pro čtení/zápis z/do paměti

## Poznámka Anki 1663704831885

Karty Anki: 1663704831885
GUID: wGjBjVEbI/; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663704831885: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište výhody a nevýhody ISA (2, 1) oproti load/store ISA (3, 0).

### Odpověď (Back)

**Výhody**

- přimý přístup do paměti (bez \(\mathtt{load}\) instrukce)

- lepší hustota kódování

**Nevýhody**

- jeden zdrojový operand je přepsán (pro zachování hodnoty je potřeba použít \(\mathtt{move}\))

- variabilita latence instrukce podle toho, za je operand v registru nebo v paměti
- komplikované zřetězené zpracování instrukcí (pipelining)

## Poznámka Anki 1663705675325

Karty Anki: 1663705675325
GUID: x{fGY_::%n; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663705675325: v původním balíčku pozastavená karta.

### Otázka (Front)

Porovnejte ISA s instrukcemi různých délek a ISA s jednotnou délkou instrukce.

### Odpověď (Back)

| Instrukce různých délek | Jednotná délka instrukce | 
    
| lepší hustota kódování | programy zabírají více paměti | 
    
| každý operand může mít svůj identifikátor adresního módu | implementace složitějších adresních módů je obtížná | 
    
| složité dekódování | rychlé a jednoduché dekódování | 
    
|  | lze načíst a paralelně dekódovat několik instrukcí najednou |

## Poznámka Anki 1663705727894

Karty Anki: 1663705727894
GUID: CQmFrZFa.g; štítky: bi-aps::p01.

### Otázka (Front)

Definujte zarovnaný prvek.

### Odpověď (Back)

Datový element je zarovnán, je-li uložen na adrese, která je dělitelná jeho velikostí.

## Poznámka Anki 1663706154119

Karty Anki: 1663706154119
GUID: MA4!j)Q0%3; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663706154119: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište výhody a nevýhody nezarovnaných dat. Podporují současné procesory nezarovnaná data?

### Odpověď (Back)

**Výhody**

- šetří paměť (datový element může začínat na libovolné adrese)

**Nevýhody**

- režie plochy čipu na "zarovnávací" obvody
- nezarovnaná data vyžadují více přístupů do paměti

Procesory s IA-32 architekturou plně podporují nezarovnaná data, ale jejich překladače je často zarovnávají z důvodu výkonnosti. Procesory s RISC architekturou vygenerují při přístupu k nezarovnaným datům výjimku.

## Poznámka Anki 1663706230531

Karty Anki: 1663706230531
GUID: LXDe$IJ1C,; štítky: bi-aps::p01.

### Otázka (Front)

Definujte mikroarchitekturu. Kde leží v hierarchii?

### Odpověď (Back)

Mikroarchitektura je detailní interní organizace procesoru, včetně hlavních
funkčních jednotek, jejich propojení a řízení.

Platí hierarchie: architektura (ISA), mikroarchitektura, HW realizace procesoru.

## Poznámka Anki 1663706475760

Karty Anki: 1663706475761
GUID: kf0,*AxX{J; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663706475761: v původním balíčku pozastavená karta.

### Otázka (Front)

Uvěďte vzorec Amdahlova zákona.

### Odpověď (Back)

\[S(p) = \frac{\alpha + 1 - \alpha}{\alpha + \frac{1 - \alpha}{p}}\]

- \(S\) (Speedup) - zrychlení
- \(p\) - počet procesorů
- \(\alpha\) - sekvenční část programu

## Poznámka Anki 1663707242586

Karty Anki: 1663707242586
GUID: OgrRl/*vbl; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663707242586: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte propustnost.

### Odpověď (Back)

Jde o počet sekvenčně vykonaných programů \(\text{prg}\) za jednotku času na jádru \(\text{core}\).
\[P_{\text{core}}(\text{prg}) = \frac{1}{T_{\text{core}}(\text{prg})}\]

-  \(T_{\text{core}}\) - doba pro vykonání programu \(\text{prg}\) na jádru \(\text{core}\)

## Poznámka Anki 1663707337705

Karty Anki: 1663707337705
GUID: k7@onfm5%P; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663707337705: v původním balíčku pozastavená karta.

### Otázka (Front)

Uveďte vzorec pro výpočet propustnosti paralelního systému.

### Odpověď (Back)

\[P_{\text{CPU}}(\text{prg}) = \frac{\text{počet provedených programů prg}}{\text{CPU čas provedení tohoto počtu programů prg}}\]

## Poznámka Anki 1663708263927

Karty Anki: 1663708263928
GUID: sp$Or}KqWT; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663708263928: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte dobu pro vykonání programu.

### Odpověď (Back)

\[T_\text{core}(\text{prg}) = T_\text{CLK} \cdot \text{Cyc}_\text{core}(\text{prg}) = T_\text{CLK} \cdot \text{IC}(\text{prg}) \cdot \text{CPI}(\text{prg}) = \frac{\text{IC}(\text{prg}) \cdot \text{CPI}(\text{prg})}{f_\text{CLK}} = \frac{T_\text{CLK} \cdot \text{IC}(\text{prg})}{\text{IPC}(\text{prg})}\]

- \(T_\text{CLK}\) - doba trvání hodinového cyklu (platí \( T_\text{CLK} = 1/f_\text{CLK}\))
- \(\text{Cyc}_{\text{core}}(\text{prg})\) - počet hodinových cyklů pro provedení programu \(\text{prg}\)
- \(\text{IC}(\text{prg})\) (Instruction Count) - počet instrukcí pro provedení programu \(\text{prg}\)
- \(\text{CPI}(\text{prg})\) (clock Cycles Per Instruction) - průměrný počet hodinových cyklů jádra na instrukci při provádění programu \(\text{prg}\)
- \(\text{IPC}(\text{prg})\) (Instructions Per clock Cycle) - převrácená hodnota \(\text{CPI}(\text{prg})\).

## Poznámka Anki 1663708807604

Karty Anki: 1663708807604
GUID: LYI#McQrzJ; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663708807604: v původním balíčku pozastavená karta.

### Otázka (Front)

Uveďte vzorec pro výpočet počtu hodinových cyklů pro provedení programu \(\text{prg}\).

### Odpověď (Back)

\[\text{Cyc}_\text{core}(\text{prg}) = \sum_{i=1}^{C} \text{ic}_i(\text{prg}) \cdot \text{cpi}_i(\text{prg})\]

- \(\text{ic}_i(\text{prg})\) (Instruction Count) - počet instrukcí typu \(i\)
- \(\text{cpi}_i(\text{prg})\) (Cycles Per Instruction) - počet cyklů na provedení instrukce \(i\)
- \(C\) - index poslední instrukce

## Poznámka Anki 1663708989781

Karty Anki: 1663708989781
GUID: MSuKp~10Jg; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663708989781: v původním balíčku pozastavená karta.

### Otázka (Front)

Uveďte vzorec pro výpočet průměrné hodnoty Cycles Per Instruction pro program \(\text{prg}\).

### Odpověď (Back)

\[\text{CPI}(\text{prg}) = \frac{\text{Cyc}_\text{core}(\text{prg})}{\text{IC}(\text{prg})}\]

- \(\text{Cyc}_\text{core}(\text{prg})\) - počet hodinových cyklů pro provedení programu \(\text{prg}\)
- \(\text{IC}(\text{prg})\) (Instruction Count) - počet instrukcí pro provedení programu \(\text{prg}\)

## Poznámka Anki 1663709369085

Karty Anki: 1663709369085
GUID: I-C(~$Vk3S; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663709369085: původní příznak autora 7; v původním balíčku pozastavená karta.

### Otázka (Front)

Uveďte vzorce pro výpočet MIPS (Million Instructions Per Second).

### Odpověď (Back)

\[\text{MIPS}(\text{prg}) = \frac{\text{IPS}(\text{prg})}{10^6} = \frac{f_\text{CLK}}{\text{CPI}(\text{prg}) \cdot 10^6}\]

- \(\text{IPS}(\text{prg})\) (Instructions Per Second) - počet instrukcí provedených za sekundu při programu \( \text{prg}\)
- \(f_\text{CLK}\) - frekvence hodin
- \(\text{CPI}(\text{prg})\) (Cycles Per Instruction) - průměrný počet hodinových cyklů jádra na instrukci při programu \(\text{prg}\)

## Poznámka Anki 1663709467029

Karty Anki: 1663709467029
GUID: HnXT^t(*<7; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663709467029: v původním balíčku pozastavená karta.

### Otázka (Front)

Uveďte vzorec pro výpočet GFLOPS.

### Odpověď (Back)

\[\text{GFLOPS}(\text{prg}) = \frac{\text{floating point operations per second}(\text{prg})}{10^9}\]

## Poznámka Anki 1663709677374

Karty Anki: 1663709677374
GUID: hRVt1#i@]B; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663709677374: v původním balíčku pozastavená karta.

### Otázka (Front)

Uveďte příklady zkušebních úloh (benchmarks).

### Odpověď (Back)

- zkušební úlohy SPEC (Standard Performance Evaluation Corporation) - zkušební úlohy zaměřené na grafické výpočty, paralelní výpočty, cloudové výpočty, atd. [zrychlení vůči referenci]
- LINPAC pro HPC systémy - řešení systému hustých lineárních rovnic [horní odhad GFLOPS]
- HPCG pro HPC systémy - řešení systému řídkých lineárních rovnic [dolní odhad GFLOPS]

## Poznámka Anki 1663709897243

Karty Anki: 1663709897243
GUID: Ll*c^(yQj<; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663709897243: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište statický příkon (Static Power Consumption).

### Odpověď (Back)

Statický příkon započítává i když signály nemění hodnotu a procesor je nečinný.
\[P_\text{static} = I_{DD} \cdot V_{DD}\]

- \(I_{DD}\) - ztrátový proud
- \(V_{DD}\) - napájecí napětí

## Poznámka Anki 1663710019078

Karty Anki: 1663710019078
GUID: O3w_XM(]=.; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663710019078: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište dynamický příkon.

### Odpověď (Back)

Jde o příkon spotřebovaný k nabíjení kondenzátorů, když signály mění hodnotu z 0 na 1.
\[P_\text{dynamic} = C \cdot V^2_{DD} \cdot \frac{f_\text{CLK}}{2}\]

- \(V_{DD}\) - napájecí napětí
- \(C\) - kapacita spínacího transistoru
- \(f_\text{CLK}\) - frekvence hodin

## Poznámka Anki 1663710290983

Karty Anki: 1663710290984
GUID: O@).nJ33{m; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663710290984: v původním balíčku pozastavená karta.

### Otázka (Front)

Uveďte vzorec pro výpočet \(\text{EPI}(\text{prg})\) (Energy Per Instruction).

### Odpověď (Back)

\[\text{EPI}(\text{prg}) = \frac{\text{energie}(\text{prg})[J]}{\text{IC}(\text{prg})[\text{instr}]} = \frac{\text{příkon}(\text{prg})[W]}{\text{IPS}(\text{prg})[\text{instr}/s]}\]

- \(\text{IC}(\text{prg})\) (Instruction Count) - počet instrukcí pro provedení \(\text{prg}\)
- \(\text{IPS}(\text{prg})\) (Instructions Per Second) - počet instrukcí za sekundu při provádění \(\text{prg}\)

## Poznámka Anki 1663710383722

Karty Anki: 1663710383722
GUID: eQCWT7Y8[z; štítky: bi-aps::p01.

Metadata původního zdroje pro kartu 1663710383722: v původním balíčku pozastavená karta.

### Otázka (Front)

Uveďte vzorec pro výpočet \(\text{Eff}_\text{CPU}(\text{prg})\) (Performance Per Watt).

### Odpověď (Back)

\[\text{Eff}_\text{CPU}(\text{prg}) = \frac{\text{GFLOPS}(\text{prg})[\text{GFLOPS}]}{\text{příkon}(\text{prg})[W]}\]

