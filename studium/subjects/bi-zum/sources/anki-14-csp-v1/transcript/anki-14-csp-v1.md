# BI-ZUM – 14 CSP

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 3 poznámek, 3 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610666

Karty Anki: 1785298610666
GUID: g>e&dhGQ}A; štítky: AI_combined::14_CSP iterace_10 src_757-761.

### Otázka (Front)

Jak je formálně definován CSP, jeho omezení a řešení?

### Odpověď (Back)

**CSP=(X,D,C)**: konečná množina proměnných X, jejich společná či individuální konečná doména D a množina omezení C. Proměnné jsou rozhodnutí, domény možné hodnoty a omezení povolené kombinace.

Omezení nad x₁,…,x<sub>k</sub> je relačně podmnožina D₁×…×D<sub>k</sub> obsahující právě povolené k-tice. Lze je zadat **extenzionálně** výčtem, **intenzionálně** formulí nebo procedurou rozhodující přípustnost. **Řešení** je úplné přiřazení hodnot z domén všem proměnným, které splňuje všechna omezení.

## Poznámka Anki 1785298610667

Karty Anki: 1785298610667
GUID: dXcCVJ}{AL; štítky: AI_combined::14_CSP iterace_10 src_762-766.

### Otázka (Front)

Jaké typické úlohy ilustrují CSP a jak se struktura omezení zapisuje hypergrafem?

### Odpověď (Back)

**Sudoku:** buňky jsou proměnné, doména {1,…,9} a globální allDifferent pro každý řádek, sloupec a blok 3×3. Je globální, protože váže mnoho proměnných a specializovaná propagace odvodí více než sada párových nerovností.

**Barvení mapy:** proměnné jsou oblasti, doména barvy a sousední oblasti mají omezení ≠. **SEND+MORE=MONEY:** pomocné proměnné přenosů rozkládají globální aritmetickou rovnost na lokální sloupcová omezení.

V **hypergrafu** jsou proměnné vrcholy a každé omezení je hyperhrana spojující všechny proměnné, na nichž závisí; počet těchto proměnných je arita omezení.

## Poznámka Anki 1785298610668

Karty Anki: 1785298610668
GUID: G@xaL)~PJ:; štítky: AI_combined::14_CSP iterace_10 src_767-772.

### Otázka (Front)

Jak probíhá prohledávání CSP a jakou roli mají konzistence, propagace a heuristiky?

### Odpověď (Back)

Stav je částečné přiřazení S′:X′→D pro X′⊆X. Začíná se prázdným přiřazením, akce přiřadí hodnotu dosud nepřiřazené proměnné a cílem je úplné konzistentní přiřazení. Základní konzistence znamená, že není porušeno žádné omezení, jehož všechny proměnné už mají hodnotu; silnější propagace může spor odhalit dříve.

Přiřazovací akce jsou **komutativní**: stejné dvojice proměnná–hodnota dají bez ohledu na pořadí stejný výsledek, pořadí však zásadně mění velikost hledání. **Propagace** odstraňuje hodnoty neslučitelné s omezeními; pokud neurčí pokračování, **prohledávání** větví přes alternativy. Heuristiky výběru proměnné a hodnoty mají rychle vyvolat další propagaci nebo odhalit spor a zmenšit strom.

