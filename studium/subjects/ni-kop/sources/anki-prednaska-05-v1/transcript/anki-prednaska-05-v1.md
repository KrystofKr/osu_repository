# NI-KOP – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 10 poznámek, 10 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1729534481434

Karty Anki: 1729534481434
GUID: f$^tg>3z]; štítky: ni-kop::p05.

### Otázka (Front)

Definujte pseudopolynomiální algoritmus. Uveďte příklad.

### Odpověď (Back)

Pseudopolynomiální algoritmus je algoritmus, jehož počet kroků závisí jak polynomiálně na velikosti instance, tak na vstupní proměnné, která s velikostí instance nesouvisí. Pseudopolynomiálním algoritmem je např. algoritmus dynamického programování pro řešení 0/1 problému batohu s dekompozicí dle váhy nebo ceny.

## Poznámka Anki 1729534993086

Karty Anki: 1729534993086
GUID: hn`XaMp#6-; štítky: ni-kop::p05.

### Otázka (Front)

Popište aproximativní algoritmus.

### Odpověď (Back)

Aproximativní algoritmus je algoritmus, který nezaručuje optimalitu řešení, ale pouze jeho kvalitu pro všechny instance daného problému.

### Doplňující pole (Extra)

Zárukou kvality rozumíme např. splnění požadavku, aby nejhorší případ nebyl horší o více než dané procento od optimálního řešení.

## Poznámka Anki 1729535661866

Karty Anki: 1729535661866
GUID: Jw&`})CO[2; štítky: ni-kop::p05.

### Otázka (Front)

Definujte relativní kvalitu a relativní chybu aproximativního algoritmu.

### Odpověď (Back)

Mějme aproximativní řešení \(\operatorname{APR}(I)\) a optimální řešení \(\operatorname{OPT}(I)\) instance \(I\) a optimalizační kritérium \(C(Y)\). Aproximativní algoritmus \(\operatorname{APR}\) má **relativní kvalitu** \(R\), jestliže
\[R \geq \displaystyle \max_{\forall I} \bigg \{ \frac{C \big( \operatorname{APR}(I) \big) }{C \big( \operatorname{OPT}(I) \big)}, \frac{C \big( \operatorname{OPT}(I) \big) }{C \big( \operatorname{APR}(I) \big)}  \bigg \}.\]Dále má \(\operatorname{APR}\) **relativní chybu **\(\varepsilon\), jestliže
\[\varepsilon \geq \displaystyle \max_{\forall I} \Bigg \{ \frac{ \big| C \big( \operatorname{APR}(I) \big) - C \big( \operatorname{OPT}(I) \big) \big| }{ \max \Big\{ C \big( \operatorname{APR}(I) \big), C \big( \operatorname{OPT}(I) \big) \Big \} }  \Bigg \}.\]

### Doplňující pole (Extra)

Funkci \(\max\) zde používáme pro sjednocení hodnot pro minimalizační a maximalizační problémy.

## Poznámka Anki 1729535810055

Karty Anki: 1729535810055
GUID: e_t>{!w]ym; štítky: ni-kop::p05.

### Otázka (Front)

Definujte \(R\)-aproximativní a \(\varepsilon\)-aproximativní algoritmus.

### Odpověď (Back)

Aproximativní algoritmus pro problém \(\Pi\) je \(R\)**-aproximativní** resp. \(\varepsilon\)**-aproximativní**, jestliže každou instanci \(\Pi\) vyřeší v polynomiálním čase s relativní kvalitou \(R\) resp. relativní chybou \(\varepsilon\).

## Poznámka Anki 1729535918778

Karty Anki: 1729535918778
GUID: q28;eNVEt|; štítky: ni-kop::p05.

### Otázka (Front)

Definujte \(R\)-aproximativní a \(\varepsilon\)-aproximativní optimalizační problém a aproximační práh problému.

### Odpověď (Back)

Optimalizační problém \(\Pi\) je \(R\)**-aproximativní** resp. \(\varepsilon\)**-aproximativní**, jestliže pro něj existuje \(R\)-aproximativní resp. \(\varepsilon\)-aproximativní polynomiální algoritmus. Číslo \(R\) resp. \(\varepsilon\) nazveme aproximačním prahem problému \(\Pi\).

## Poznámka Anki 1729535973840

Karty Anki: 1729535973840
GUID: j#&<;Pcv%#; štítky: ni-kop::p05.

### Otázka (Front)

Definujte třídu \(\text{APX}\). Jaký je její vztah k třídám \(\text{NPO}\) a \(\text{PTAS}\)?

### Odpověď (Back)

Optimalizační problém \(\Pi\) patří do třídy \(\text{APX}\), jestliže je \(R\)-aproximativní pro konečné \(R\). Platí, že \(\text{PTAS} \subset \text{APX} \subset \text{NPO}\).

## Poznámka Anki 1729536934680

Karty Anki: 1729536934680
GUID: vUn_|Ue>/`; štítky: ni-kop::p05.

### Otázka (Front)

Definujte polynomiální aproximační sechéma (polynomial time approximation scheme) problému a třídu \(\text{PTAS}\). Jaký je její vztak k třídám \(\text{APX}\) a \(\text{FPTAS}\)?

### Odpověď (Back)

Aproximativní algoritmus, který pro každé \(\varepsilon \in (0, 1)\) vyřeší každou instanci \(I\) problému \(\Pi\) s relativní chybou nejvýše \(\varepsilon\) v čase polynomiálně závislém na \(I\), nazýváme **polynomiálním aproximačním schématem **(polynomial time approximation scheme) **problému** \(\Pi\). Pokud pro problém \(\Pi\) existuje polynomiální aproximační schéma, pak patří do třídy \(\text{PTAS}\). Platí, že \(\text{FPTAS} \subset \text{PTAS} \subset \text{APX}\).

## Poznámka Anki 1729537230327

Karty Anki: 1729537230327
GUID: o{S=^yv`2E; štítky: ni-kop::p05.

### Otázka (Front)

Definujte plně polynomiální aproximační schéma (fully polynomial time approximation scheme) problému a třídu \(\text{FPTAS}\). Jaký je její vztak k třídám \(\text{PTAS}\) a \(\text{PO}\)?

### Odpověď (Back)

Polynomiální aproximační schéma (polynomial time approximation scheme), jehož čas výpočtu závisí polynomiálně na \(\frac 1 \varepsilon\), nazýváme **plně polynomiálním aproximačním schématem** (fully polynomial time approximation scheme). Pokud pro problém \(\Pi\) existuje plně polynomiální aproximační schéma, pak patří do třídy \(\text{FPTAS}\). Platí, že \(\text{PO} \subset \text{FPTAS} \subset \text{PTAS}\).

## Poznámka Anki 1729540909608

Karty Anki: 1729540909608
GUID: A.,+lxc;=+; štítky: ni-kop::p05.

### Otázka (Front)

Popište \(\text{APX}\) redukci. Co platí pro \(\text{APX}\)-redukovatelné problémy?

### Odpověď (Back)

\(\text{APX}\) redukce je typ polynomiální redukce, která je speciálním případem Turingovy redukce v polynomiálním čase. Funguje v následujících krocích:

- instance \(I_1\) problému \(\Pi_1\) je redukována na instanci \(I_2\) problému \(\Pi_2 \in \text{NPO}\), pro který existuje aproximativní algoritmus, tak, aby byla zachována existence řešení;
- instance \(I_2\) je vyřešena aproximativním algoritmem s relativní kvalitou \(R\);
- řešení instance \(I_2\) je redukováno na řešení instance \(I_1\) tak, aby bylo řešení zachováno, přičemž relativní kvalita redukovaného řešení je \(\mathcal O(R)\).

Tuto skutečnost značíme \(\Pi_1 \stackrel{\text{APX}}\propto \Pi_2\) a platí, že \(\Pi_2 \in \text{APX} \Rightarrow \Pi_1 \in \text{APX}\) (obdobně pro \(\text{PTAS}\)).

## Poznámka Anki 1729541070138

Karty Anki: 1729541070138
GUID: h0G;Q|+S7$; štítky: ni-kop::p05.

### Otázka (Front)

Definujte \(X\)-těžký (\(X\)-hard) problém pro třídy \(\text{NPO}\) a \(\text{APX}\) pomocí \(\text{APX}\) redukce.

### Odpověď (Back)

Porblém \(\Pi\) je \(\text{NPO}\)-těžký resp. \(\text{APX}\)-těžký, jestliže pro všechny problémy \(\Pi' \in \text{NPO}\) resp. \(\Pi' \in \text{APX}\) platí
\[\Pi' \stackrel{\text{APX}}\propto \Pi.\]

