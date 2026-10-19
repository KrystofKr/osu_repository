# BI-HWB – Přednáška 11

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-hwb/BI-HWB.apkg; APKG SHA-256 0303626d2408f7eee1801e17ecb475633a60c42f914f37290ffd8c479013ce2b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b861d2e855c5070244800c22d62092a09b22aee0ded024030525b06a7d18285e.
Původní balíčky: BI-HWB
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1701709014060

Karty Anki: 1701709014060
GUID: n<[CJpKVJS; štítky: bi-hwb::p11.

### Otázka (Front)

Popište vestavný systém (embedded system). Uveďte příklady.

### Odpověď (Back)

Vestavný systém (embedded system) je jednoúčelový systém, který plní dedikovanou funkci v rámci většího elektronického systému. Jeho řídící systém bývá pevně zabudován do zařízení, které ovládá. Příkladem vestavného systému může být autopilot letadla, router nebo třeba kalkulačka.

## Poznámka Anki 1701712639358

Karty Anki: 1701712639358
GUID: iWxqb}7EEf; štítky: bi-hwb::p11.

### Otázka (Front)

Popište útok Meltdown.

### Odpověď (Back)

Meltdown je útok cílený na superskalární procesory, který zneužívá out-of-order provádění instrukcí a cache postranní kanál. Předpokládejme, že v user space máme alokované pole \(\texttt{probe_array}\) o velikosti \(256 \cdot 4096\) bytů, kde \(256\) je počet všech možných hodnot bytu a \(4096\) bytů je běžná velikost stránky. Potom útok Meltdown probíhá následovně:

- Nejprve je přistoupeno na adresu v kernel space s cílem přečíst jeden byte dat \(b\).
- Poté je přistoupeno k \(\texttt{probe_array[} b \cdot 4096 \texttt ]\), čímž je do cache načtena jedna konkrétní stránka obsahující část \(\texttt{probe_array} \).
- Nakonec je za pomocí flush and reload postranního kanálu zjištěno číslo stránky, ke které bylo přistoupeno, a je tak získána hodnota \(b\).

Protože superskalární procesor vykonává instrukce mimo programové pořadí, jsou tyto instrukce provedeny dříve, než dojde k dohledání, že daná adresa náleží kernel space, a je vyvolána výjimka.

## Poznámka Anki 1701713244527

Karty Anki: 1701713244527
GUID: e,!MWd.yEM; štítky: bi-hwb::p11.

### Otázka (Front)

Popište útok Spectre (varianta bounds check bypass).

### Odpověď (Back)

Spectre je útok cílený na superskalární procesory, který zneužívá spekulativní provádění instrukcí a cache postranní kanál. Předpokládejme, že v user space máme alokované pole \(\texttt{probe_array}\) o velikosti \(256 \cdot 4096\) bytů, kde \(256\) je počet všech možných hodnot bytu a \(4096\) bytů je běžná velikost stránky. Dále předpokládejme pole \(\texttt{array}\) ukazující do libovolné paměti a proměnnou \(\texttt{array_size}\). Potom útok Spectre probíhá následovně:

- Nejprve je vyhodnocena podmínka \(\texttt x < \texttt{array_size}\).
- Na základě této podmínky je přistoupeno k \(\texttt{probe_array[array[x]} \cdot 4096 \texttt ]\) s cílem přečíst jeden byte dat \(b\). Tím je do cache načtena jedna konkrétní stránka obsahující část \(\texttt{probe_array} \).
- Nakonec je za pomocí flush and reload postranního kanálu zjištěno číslo stránky, ke které bylo přistoupeno, a je tak získána hodnota \(b\).
Protože \(\texttt x\) je hodnota, kterou útočník dokáže ovlivnit, může prediktor skoků vytrénovat tak, aby umožňil spekulativně vykonat přístup do paměti, který by se za normálních okolností neměl provést.

## Poznámka Anki 1701713599555

Karty Anki: 1701713599555
GUID: d)l..jEHdQ; štítky: bi-hwb::p11.

### Otázka (Front)

Popište útok PLATYPUS (Power Leakage Attacks: Targeting Your Protected User Secrets).

### Odpověď (Back)

Útok PLATYPUS (Power Leakage Attacks: Targeting Your Protected User Secrets) je typ útoku odběrovým postranním kanálem, který zneužívá technologii Intel Running Average Power Limit (RAPL) nebo podobné technologie. RAPL umožňuje získávat poměrně přesné informace o odběru procesoru a jeho jader. Útočník s takovým přístupem může pomocí statistické analýzy odvodit data a operace, které se na procesoru vykonávají.

