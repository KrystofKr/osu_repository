# BI-ZUM – 13 kvantove zihani QUBO

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 3 poznámek, 3 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610663

Karty Anki: 1785298610663
GUID: v?TH<F`]Xa; štítky: AI_combined::13_kvantove_zihani_QUBO iterace_10 src_741-746.

### Otázka (Front)

Co je qubit a jak funguje adiabatický model kvantového výpočtu?

### Odpověď (Back)

**Qubit** je stav |ψ⟩=α|0⟩+β|1⟩ s komplexními amplitudami, kde |α|²+|β|²=1; měření vrátí 0 s pravděpodobností |α|² a 1 s pravděpodobností |β|².

**Hradlový model** skládá algoritmus ze sekvence kvantových hradel. **Adiabatický model** připraví základní stav snadného počátečního Hamiltoniánu a dostatečně pomalu jej mění na problémový Hamiltonián, jehož základní stav (minimum energie) kóduje řešení. V plánu H(s)=A(s)H<sub>poč</sub>+B(s)H<sub>problém</sub> funkce A postupně zeslabuje počáteční a B zesiluje problémový Hamiltonián.

## Poznámka Anki 1785298610664

Karty Anki: 1785298610664
GUID: xqO:rA]K{L; štítky: AI_combined::13_kvantove_zihani_QUBO iterace_10 src_747-750.

### Otázka (Front)

Co je QUBO a jak souvisí jeho matematický zápis s fyzickým annealerem?

### Odpověď (Back)

**QUBO** (Quadratic Unconstrained Binary Optimization) minimalizuje kvadratickou funkci binárních proměnných, typicky min<sub>x∈{0,1}<sup>n</sup></sub>xᵀQx. Protože x<sub>i</sub>²=x<sub>i</sub>, lze lineární člen a<sub>i</sub>x<sub>i</sub> uložit na diagonálu Q jako a<sub>i</sub>x<sub>i</sub>².

Nenulový q<sub>ij</sub> vyžaduje vazbu odpovídajících qubitů. Omezená fyzická konektivita proto nutí logickou proměnnou vložit do řetězce více qubitů. Intuitivně simulované žíhání překonává energetické bariéry tepelnými fluktuacemi, zatímco kvantové žíhání může tunelovat skrz úzké bariéry.

## Poznámka Anki 1785298610665

Karty Anki: 1785298610665
GUID: lRW8Q*@I0_; štítky: AI_combined::13_kvantove_zihani_QUBO iterace_10 src_751-756.

### Otázka (Front)

Jak se omezení převádějí na penalizace v QUBO a jaké jsou základní vzory?

### Odpověď (Back)

K účelové funkci se přičtou nezáporné penalizace: nulové pro přípustné a kladné pro porušující přiřazení.

Základní binární vzory:
• x+y≤1: **xy** (trestá jen x=y=1).
• x=y: **x+y−2xy** (trestá nerovnost).
• x⇒y: **x−xy=x(1−y)** (trestá jen x=1,y=0).
• právě jedna z x₁,…,xₙ: **(Σᵢxᵢ−1)²** = −Σᵢxᵢ+2Σᵢ<ⱼxᵢxⱼ+1.

Koeficient penalizace musí převýšit nejlepší možné zlepšení původní účelové funkce dosažené porušením; jinak může být globální minimum nepřípustné.

