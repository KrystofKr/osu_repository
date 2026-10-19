# BI-PSI – Proseminář 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-psi/BI-PSI.apkg; APKG SHA-256 de3459b5749b7561c58ca1888745fb5e7a4e9513c07e81d554048a9717edb571. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 2b00361eedd866dc0049df9b467b1b3d10c8acc06f2f615bd98666c81938bb28.
Původní balíčky: BI-PSI
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1652614078211

Karty Anki: 1652614078214
GUID: CH!N&!Q)]Q; štítky: bi-psi::ps04.

### Otázka (Front)

Napište vzorec pro výpočet efektivity schématu Stop-and-Wait (jednotlivé potvrzování) pomocí objemu dat.

### Odpověď (Back)

\[\eta_0 = \frac{l_m}{l_m + l_a + 2 T_d \cdot C}\]
\(\eta_0\) je efektivita, \(l_m\) délka zprávy, \(l_a\) délka potvrzení, \(T_d\) dopravní zpoždění (čas doručování zprávy) a \(C\) rychlost linky v bitech za vteřinu.

## Poznámka Anki 1652614103422

Karty Anki: 1652614103422
GUID: FVeGTMV_Hy; štítky: bi-psi::ps04.

Metadata původního zdroje pro kartu 1652614103422: v původním balíčku pozastavená karta.

### Otázka (Front)

Napište vzorec pro výpočet efektivity schématu Stop-and-Wait (jednotlivé potvrzování) pomocí času.

### Odpověď (Back)

\[\eta_0 = \frac{\frac{l_m}{C}}{\frac{l_m}{C}+\frac{l_a}{C}+2T_d}\]
\(\eta_0\) je efektivita, \(l_m\) délka zprávy, \(l_a\) délka potvrzení, \(T_d\) dopravní zpoždění (čas doručování zprávy) a \(C\) rychlost linky v bitech za vteřinu.

## Poznámka Anki 1652614310952

Karty Anki: 1652614310953
GUID: p<@$j3_.eH; štítky: bi-psi::ps04.

### Otázka (Front)

Napište zjednodušený vzorec pro výpočet efektivity schématu Stop-and-Wait (jednotlivé potvrzování) pomocí času.

### Odpověď (Back)

\[\eta_0 = \frac{\frac{l_m}{C}}{T} = \frac{l_m}{C \cdot T}\]
\(\eta_0\) je efektivita, \(l_m\) délka zprávy, \(T\) komunikační odezva, kterou zjistíme pomocí utility \(\mathtt{ping}\) a \(C\) rychlost linky v bitech za vteřinu.

## Poznámka Anki 1652614498060

Karty Anki: 1652614498060
GUID: uxx}*/zBx+; štítky: bi-psi::ps04.

Metadata původního zdroje pro kartu 1652614498060: v původním balíčku pozastavená karta.

### Otázka (Front)

Napište vzorec pro výpočet efektivity pipeliningu (kontinuálního potvrzování).

### Odpověď (Back)

\[\eta_0 = \frac{W \cdot l_m}{l_m + l_a + 2 T_d \cdot C}\]
\(\eta_0\) je efektivita, \(l_m\) délka zprávy, \(l_a\) délka potvrzení, \(T_d\) dopravní zpoždění (čas doručování zprávy), \(C\) rychlost linky v bitech za vteřinu a \(W\) je délka okénka (počet rámců odesílaných bez čekání na potvrzení).

## Poznámka Anki 1652614528876

Karty Anki: 1652614528876
GUID: K~lKHjfs9-; štítky: bi-psi::ps04.

### Otázka (Front)

Jak obecně spočítáme efektivitu potvrzovacího schématu?

### Odpověď (Back)

\[\eta = \min ( \frac{\text{useful data}}{\text{useful data} + \text{unuseful data}}, 1)\]

## Poznámka Anki 1652822186543

Karty Anki: 1652822186544
GUID: r;l$FC[6im; štítky: bi-psi::ps04.

### Otázka (Front)

Uveďte vzorec pro výpočet délky přenosu.

### Odpověď (Back)

\[t= \bigg( 2 \cdot \frac{s}{v} + \frac{l_m}{C_B} + \frac{l_a}{C_B} \bigg) \cdot \frac{V}{l_m}\]
\(t\) je doba přenosu v sekundách, \(s\) je vzdálenost, \(v\) rychlost světla, \(l_m\) velikost rámce v bytech, \(C_B\) přenosová rychlost v bytech za sekundu, \(l_a\) velikost potvrzení v bytech a \(V\) objem dat.

