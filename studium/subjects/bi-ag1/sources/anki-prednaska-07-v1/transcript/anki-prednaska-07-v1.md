# BI-AG1 – Přednáška 07

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-AG1
Rozsah: 18 poznámek, 18 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1667205280721

Karty Anki: 1667205280721
GUID: iF#Km~uDKN; štítky: bi-ag1::p07 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište hashovací tabulku a kolizi.

### Odpověď (Back)

Pro nějaké univerzum klíčů \(\mathcal{U}\) zvolme konečnou množinu přihrádek \(\mathcal{P} = \set{0, \dots, m-1}\) (**hashovací tabulku**) a hashovací funkci \(h: \mathcal{U} \to \mathcal{P}\), která každému klíči univerza přidělí jednu přihrádku.

Díky poměru \(m\) a \(|\mathcal{U}|\) (\(m \ll |\mathcal{U}|\)) se bude stávat, že několik prvků padne do stejné přihrádky. Tomu se říká **kolize**.

## Poznámka Anki 1667206392939

Karty Anki: 1667206392939
GUID: MN!|-S;<de; štítky: bi-ag1::p07 bi-spol::04 bi-spol::23.

### Otázka (Front)

Jakými metodami lze řešit kolize v hashovací tabulce?

### Odpověď (Back)

- **řetězení **(otevřené hashování)

- **otevřené adresování **(uzavřené hashování)

## Poznámka Anki 1667206586681

Karty Anki: 1667206586681
GUID: hXIXZeRdma; štítky: bi-ag1::p07 bi-spol::04.

### Otázka (Front)

Jaké vlastnosti má ideální hashovací funkce?

### Odpověď (Back)

- Výpočet \(h(k)\) je rychlý (\(\mathcal{O}(1)\)) a funkce \(h\) neukládá data do paměti (její výpočet je nezávislý na historii předchozích volání).
- Hashovací funkce rozděluje univerzum \(\mathcal{U}\) do přihrádek rovnoměrně.

## Poznámka Anki 1667206755665

Karty Anki: 1667206755665
GUID: A|56_{TJHi; štítky: bi-ag1::p07 bi-spol::04 bi-spol::23.

### Otázka (Front)

Vyslovte (neformální) větu o složitosti ideálního hashování.

### Odpověď (Back)

Mějme hashovací tabulku velikosti \(m\) s \(n\) prvky a ideální hashovací funkcí a nechť jsou prvky univerza vybírány nezávisle rovnoměrně náhodně. Pak platí:

- průměr počtu prvků v přihrádce je \(\frac n m\),
- skoro všechny přihrádky obsahují \(\mathcal O( \frac n m)\) prvků.

Proto je i průměrná časová složitost operací nad hashovací tabulkou \(\mathcal O(\frac n m)\).

## Poznámka Anki 1667206882400

Karty Anki: 1667206882400
GUID: i7WN3Kf2nL; štítky: bi-ag1::p07 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište hashovací tabulku s řetízky.

### Odpověď (Back)

hashovací tabulka je pole \(m\) přihrádek, které jsou buď prázdné nebo obsahují ukazatel na řetízky (= spojové seznamy) uložených prvků.

## Poznámka Anki 1667207549007

Karty Anki: 1667207549007
GUID: d[B#@T$Elm; štítky: bi-ag1::p07 bi-spol::04 bi-spol::23.

### Otázka (Front)

Vyslovte (neformální) větu o složitosti hashovací tabulky s řetízky.

### Odpověď (Back)

Mějme hashovací tabulku s řetízky velikosti \(m\) s \(n\) prvky a ideální hashovací funkcí a nechť jsou prvky univerza vybírány nezávisle rovnoměrně náhodně. Pak platí, že skoro všechny řetízky mají délku nejvýše \(\lceil \frac n m \rceil\). Pokud zvolíme počet přihrádek

\[m = \Theta (n),\]vyjde konstatní délka řetízku, a proto budou mít operace nad hashovací tabulkou časovou složitost \(\mathcal O(1)\).

## Poznámka Anki 1667207785833

Karty Anki: 1667207785833
GUID: La+n)N;|P5; štítky: bi-ag1::p07 bi-spol::04 bi-spol::23.

### Otázka (Front)

Popište hashovací tabulku s otevřenou adresací a její hashovací funkci.

### Odpověď (Back)

**Hashovací tabulka s otevřenou adresací** je pole s \(m\) přihrádkami \(A[0], \dots, A[m - 1]\), jenže narozdíl od hashovací tabulky s řetízky se do každé přihrádky vejde pouze jeden prvek.

**Hashovací funkce** tedy každému klíči \(k \in \mathcal{U}\) přiřadí jeho vyhledávací posloupnost \(h(k, 0), h(k, 1), . . . , h(k, m − 1)\), která je ideálně permutací posloupnosti \(\set{0, 1, \dots, m − 1}\).

## Poznámka Anki 1667208121342

Karty Anki: 1667208121342
GUID: lAtEdC}]=R; štítky: bi-ag1::p07 bi-spol::04 bi-spol::23.

### Otázka (Front)

Jak probíhá mazání prvků v hashovací tabulce s otevřeným adresováním.

### Odpověď (Back)

Označení přihrádky smazaného prvku za prázdnou by mohlo způsobit chyby ve vyhledávání, protože vyhledávací posloupnost nějakého prvku by tím mohla být přerušena. Místo toho budeme prvky označovat za smazané, např. pomocí tzv. **náhrobku **\(\dagger\). Těchto míst pak můžeme využít při vkladání prvků. Jakmile přesáhne počet náhrobků předem určenou mez, tabulka se přehashuje.

## Poznámka Anki 1667211322906

Karty Anki: 1667211322906
GUID: D#weHid_i}; štítky: bi-ag1::p07 bi-spol::04.

### Otázka (Front)

Popište vyhledávací posloupnost lineární přidávání.

### Odpověď (Back)

Vyhledávací posloupnost je dána funkcí \(h(k, i) = (f (k) + i) \bmod m\), kde \(f(k)\) je „obyčejná“ hashovací funkce a \(i\) je počet neúspěšných pokusů v aktuální operaci.

## Poznámka Anki 1667211438929

Karty Anki: 1667211438929
GUID: qYzJ4GlnW-; štítky: bi-ag1::p07 bi-spol::04.

### Otázka (Front)

Popište vyhledávací posloupnost dvojité hashování.

### Odpověď (Back)

Vyhledávací posloupnost je dána funkcí \(h(k, i) = (f (k) + i \cdot g(k)) \bmod m\), kde \(f : \mathcal{U} \to \set{0, \dots, m - 1}\) a \(g : \mathcal{U} \to \set{0, \dots, m - 1}\) jsou dvě různé hashovací funkce, \(m\) je prvočíslo a \(i\) je počet neúspěšných pokusů v aktuální operaci.

## Poznámka Anki 1667211548099

Karty Anki: 1667211548099
GUID: C,}a;HVySx; štítky: bi-ag1::p07 bi-spol::04 bi-spol::23.

### Otázka (Front)

Vyslovte větu o efektivitě hashovací tabulky s otevřenou adresací.

### Odpověď (Back)

Mějme hashovací tabulku s otevřenou adresací velikosti \(m\) s \(n\) prvky a nechť jsou její vyhledávací posloupnosti náhodnými permutacemi. Pak platí, že neúspěšné hledání nahlédne průměrně do nejvýše
\[\frac 1 {1 - \alpha}\]přihrádek, kde
\[\alpha = \frac n m, \quad n < m,\]je faktor naplnění.

## Poznámka Anki 1667212109958

Karty Anki: 1667212109958
GUID: qu@kxE.au@; štítky: bi-ag1::p07 bi-spol::04 bi-spol::23.

### Otázka (Front)

Uveďte příklady hashovacích funkcí.

### Odpověď (Back)

- **lineární kongruence**: \(k \mapsto ak \bmod m\), kde \(m\) je prvočíslo a \(a\) je konstanta nesoudělná s \(m\)

- **vyšší bity součinu**: \(k \mapsto \lfloor (ak \bmod 2^w) / 2^{w-l} \rfloor\) neboli spočteme \(ak\), kde \(a\) je lichá konstanta nesoudělná s \(2^w\), ořízneme výsledek na \(w\) bitů a z nich vezmeme nejvyšších \(l\) (\(2^l\) označuje velikosti tabulky, \(2^w\) šířku hashovaného čísla)
- **skalární součin**: \(k_0, \dots, k_{d-1} \mapsto \bigg(\sum \limits_{i=0}^{d-1} a_ik_i \bigg) \bmod m\)
- **polynom**: \(k_0, \dots, k_{d-1} \mapsto \bigg(\sum \limits_{i=0}^{d-1} a^i k_i \bigg) \bmod m\)

## Poznámka Anki 1667212204364

Karty Anki: 1667212204364
GUID: O>W,o>T7,5; štítky: bi-ag1::p07 bi-spol::04.

### Otázka (Front)

Definujte slovník.

### Odpověď (Back)

Slovník je datová struktura, která umožňuje reprezentovat dynamickou podmnožinu prvků s unikátními klíči \(K \subseteq \mathcal{U}\), kde \(|K| \ll |\mathcal{U}|\), a efektivně podporovat operace \(\mathtt{Find}(k)\), \(\mathtt{Insert}(k)\) a \(\mathtt{Delete}(k)\).

## Poznámka Anki 1674314235045

Karty Anki: 1674314235045
GUID: ox6jGG4<`F; štítky: bi-ag1::p07.

### Otázka (Front)

Definujte diskrétní pravděpododobnostní prostor, jev a pravděpodobnost jevu.

### Odpověď (Back)

**Diskrétní pravděpodobnostní prostor** je dvojice \((\Omega, \mathbf P)\), kde 

- \(\Omega\) je konečná nebo spočetně nekonečná množina elementárních jevů.
- \(\mathbf P : \Omega \to \langle 0, 1 \rangle\) je funkce, která elementárním jevům přiřazuje jejich pravděpodobnosti, taková, že součet pravděpodobností všech elementárních jevů je roven \(1\), čili \(\sum \limits_{\omega \in \Omega} \mathbf P(\omega) = 1\).
**Jev **je nějaká množina elementárních jevů \(A \subseteq \Omega\).
**Pravděpodobnost jevu** \(A\) definujeme jako \(\mathbf P(A) = \sum \limits_{\omega \in A} \mathbf P(\omega)\).

## Poznámka Anki 1674314275172

Karty Anki: 1674314275172
GUID: GK>+jjqQY?; štítky: bi-ag1::p07 bi-spol::26 duplicate.

### Otázka (Front)

Definujte diskrétní náhodnou veličinu.

### Odpověď (Back)

Náhodná veličina \(X\) se nazývá diskrétní, jesliže nabývá pouze hodnot z nějaké nejvýše spočetné množiny \(\mathcal X = \{ x_1, x_2, \dots \}\) takové, že platí\[\displaystyle \sum_{x \in \mathcal X} \operatorname P(X = x) = 1.\]Pravděpodobnosti možných hodnot náhodné veličiny \(X\) potom jsou\[\operatorname P(X = x_k), \quad k = 1, 2, \dots.\]

## Poznámka Anki 1674314402131

Karty Anki: 1674314402131
GUID: s;VJpVVN;{; štítky: bi-ag1::p07 bi-spol::26 duplicate.

### Otázka (Front)

Definujte střední hodnotu diskrétní náhodné veličiny.

### Odpověď (Back)

Střední hodnota diskrétní náhodné veličiny \(X\), nabývající hodnot \(x_1, x_2, \dots\), je průměr všech hodnot veličiny \(X\) vážený pravděpodobnostmi příslušných elementárních jevů, tedy\[\sum \limits_{\omega \in \Omega} X(\omega) \cdot \mathbf P(\omega) = \displaystyle \sum_{x_k} x_k \cdot \mathbf P[X = x_k].\]Nutnou podmínkou je, že uvedená suma konverguje. Jinak říkáme, že střední hodnota náhodné veličiny \(X\) neexistuje.

## Poznámka Anki 1674314798644

Karty Anki: 1674314798644
GUID: &)4|7<}-o; štítky: bi-ag1::p07 bi-spol::26.

### Otázka (Front)

Vyslovte a dokažte větu o linearitě střední hodnoty.

### Odpověď (Back)

Nechť \(\alpha\) a \(\beta\) jsou reálná čísla a nechť \(X\) a \(Y\) jsou náhodné veličiny. Potom \(\mathbf E[\alpha X + \beta Y] = \alpha \mathbf E[X] + \beta \mathbf E[Y]\).

**Důkaz** 
\[\mathbf E[\alpha X + \beta Y] = \sum \limits_{\omega \in \Omega} (\alpha X + \beta Y)(\omega) \cdot \mathbf P(\omega) = \sum \limits_{\omega \in \Omega} \big(\alpha X(\omega) + \beta Y(\omega) \big) \cdot \mathbf P(\omega) = \sum \limits_{\omega \in \Omega} \alpha X(\omega) \cdot \mathbf P(\omega) + \sum \limits_{\omega \in \Omega} \beta Y(\omega) \cdot \mathbf P(\omega) = \alpha \sum \limits_{\omega \in \Omega} X(\omega) \cdot \mathbf P(\omega) + \beta \sum \limits_{\omega \in \Omega} Y(\omega) \cdot P(\omega) = \alpha \mathbf E[X] + \beta \mathbf E[Y].\]

## Poznámka Anki 1674314931857

Karty Anki: 1674314931857
GUID: PAW7ss7a|1; štítky: bi-ag1::p07.

### Otázka (Front)

Vyslovte větu o opakování nezávislých pokusů.

### Odpověď (Back)

Uvažujme sérii nezávislých pokusů, ve kterých sledujeme, zda nastal nějaký jev \(J\). Pravděpodobnost, že jev \(J\) nastane, je v každém pokusu stále stejná a rovna \(p\). Definujme náhodnou veličinu \(T\) jako pořadí pokusu, ve kterém jev \(J\) nastal poprvé. Pak
\[\mathbf E[T] = \frac 1 p.\]

