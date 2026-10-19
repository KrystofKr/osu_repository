# NI-MPI – Přednáška 07

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::NI-MPI
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1730831223785

Karty Anki: 1730831223785
GUID: OI*pYQ*rq+; štítky: ni-mpi::p07 ni-spol::05.

### Otázka (Front)

Popište numerickou matematiku.

### Odpověď (Back)

Numerická matematika je odvětví matematiky, které se věnuje matematickým metodám hledajícím přibližná řešení matematických úloh a jejich spolehlivosti. Typicky využívá počítače. Zahrnuje např. metody pro řešení soustav lineárních rovnic, výpočet integrálů nebo hledání lokálních a globálních extrémů.

## Poznámka Anki 1730831757050

Karty Anki: 1730831757051
GUID: uo=98jYcS<; štítky: ni-mpi::p07 ni-spol::05.

### Otázka (Front)

Popište kategorizaci chyb v numerické matematice.

### Odpověď (Back)

Chyby v numerické matematice dělíme dle jejich původu na:

- **chyby modelu** - matematický model úlohy je zjednodušený (např. je zanedbáno tření);

- **chyby dat** - vstupní data pocházejí z měření, která nemají absolutní přesnost;

- **chyby algoritmu** - algoritmus v konečném počtu kroků nenajde přesné řešení, ale pouze přibližné;

- **zakrouhlovací chyby** - chyby v aritmetických operacích při samotném výpočtu.

## Poznámka Anki 1730834945023

Karty Anki: 1730834945023
GUID: j=%i2pR$,^; štítky: duplicate ni-mpi::p07.

### Otázka (Front)

Popište reprezentaci čísel v pohyblivé řádové čárce (floating point) podle IEEE 754.

### Odpověď (Back)

Podle IEEE 754 jsou čísla s pohyblivou řádovou čárkou (floating point) reprezentována v podobě:
\[(-1)^s \cdot m \cdot 2^{e - b}, \]kde:

- \(s \in \{ 0, 1 \}\) je znaménko (signum),

- \(m\) je mantisa (signifikant) v přímém kódu,

- \(2\) je základ (base),

- \(e\) je exponent v aditivním kódu s konstantou \(b\).

### Doplňující pole (Extra)

Délka exponentu \(e\) jakožto binárního řetězce je značena \(d\).

## Poznámka Anki 1730835470868

Karty Anki: 1730835470868
GUID: JjWL!zz6{<; štítky: duplicate ni-mpi::p07.

### Otázka (Front)

Popište mezní případy čísel v pohyblivé řádové čárce (floating point) podle IEEE 754.

### Odpověď (Back)

Norma IEEE 754 definuje následující mezní případy čísel v pohyblivé řádové čárce (floating point):

| 
      **exponent** | 
      **mantisa** | 
      **hodnota** | 

| 
      \(e = 2^d - 1\)
 | 
      \(m \neq 0\)
 | 
      \(x = \texttt{NaN}\)
 | 

| 
      \(e = 2^d - 1\) | 
      \(m = 0\)
 | 
      \(x = (-1)^s \cdot \infty\)
 | 

| 
      \(e = 0\) | 
      \(m = 0\)
 | 
      \(x = (-1)^s \cdot 0\)
 |

## Poznámka Anki 1730836183810

Karty Anki: 1730836183810
GUID: AGH?M8/aqc; štítky: duplicate ni-mpi::p07.

### Otázka (Front)

Popište normalizovaná a subnormální čísla v pohyblivé řádové čárce (floating point) a princip skryté jedničky podle IEEE 754.

### Odpověď (Back)

Číslo v pohyblivé řádové čárce (floating point) nazveme **normalizované**, jestliže \(e \in (0, 2^d - 1)\). Jeho hodnotu pak získáme jako\[(-1)^s \cdot (1.m_2)_2 \cdot 2^{e - b}.\]V tomto tvaru bude první bit mantisy vždy jednička, proto není nutné tuto jedničku ukládat, čímž vzniká tzv. **skrytá jednička**. **Subnormální** číslo v pohyblivé řádové čárce je číslo, pro které platí \(e = 0\) a \(m \neq 0\). Jeho hodnotu získáme jako\[(-1)^s \cdot (0.m_2)_2 \cdot 2^{1 - b}.\]

### Doplňující pole (Extra)

Číslo v pohyblivé řádové čárce je v normalizovaném tvaru, pokud mantisu již nelze posunout více doleva. Symbol \(m_2\) značí binární reprezentaci mantisy (signifikantu) a \(.\) je zde chápána jako binární tečka.

## Poznámka Anki 1730837386041

Karty Anki: 1730837386041
GUID: sI?Od,Y(2m; štítky: ni-mpi::p07 ni-spol::05.

### Otázka (Front)

Definujte množinu strojových čísel a strojovou přesnost.

### Odpověď (Back)

**Množina strojových čísel** je podmnožina \(\mathbb R\), která je označována\[F \equiv F(|m|, |e|, b).\]\(F\) je charakterizována pomocí **strojové přesnosti** (machine epsilon) \(\varepsilon_F\), což je vzdálenost čísla \(1\) od nejbližšího vyššího čísla v \(F\), tj.\[\varepsilon_F = (1.0 \dots 01)_2 \cdot 2^0 - (1.0 \dots 00)_2 \cdot 2^0.\]

## Poznámka Anki 1730837631009

Karty Anki: 1730837631009
GUID: fCdBh9G&U0; štítky: ni-mpi::p07 ni-spol::05.

### Otázka (Front)

Definujte zobrazení \(\operatorname{fl}\) (float).

### Odpověď (Back)

Zobrazení \(\operatorname{fl}: \mathbb R \to F\) je zobrazení, které každému reálnému číslu přiřadí „nejbilžší“ strojové číslo, přičemž „nejbližší“ číslo je vybráno na základě zvolené strategie zaokrouhlování či usekávání.

## Poznámka Anki 1730837802005

Karty Anki: 1730837802005
GUID: O%u4:pEfJa; štítky: ni-mpi::p07 ni-spol::05.

### Otázka (Front)

Definujte absolutní a relativní chybu reprezentace čísel pomocí strojových čísel.

### Odpověď (Back)

Nechť je číslo \(\alpha \in F\) přibližnou hodnotou čísla \(a \in \mathbb R\) (téměř vždy \(\alpha = \operatorname{fl}(a)\)). Potom **absolutní chybou **reprezentace \(a\) pomocí \(\alpha\) rozumíme hodnotu
\[| \alpha - a |.\]Pro \(a \neq 0\) definujeme **relativní chybu** reprezentace \(a\) pomocí \(\alpha\) jako
\[\frac{|\alpha - a|}{|a|}.\]

## Poznámka Anki 1730839851239

Karty Anki: 1730839851239
GUID: bbC&G~/oY;; štítky: ni-mpi::p07 ni-spol::05.

### Otázka (Front)

Popište zaokrouhlovací jednotku (unit roundoff error).

### Odpověď (Back)

Zaokrouhlovací jednotka (unit roundoff error) \(\mathbf u\) označuje horní mez relativní chyby. Pro normalizované číslo platí
\[\mathbf u = 2^{-|m|}.\]

### Doplňující pole (Extra)

Pro číslo s jednoduchou přesností tedy dostáváme \(\mathbf u = 2^{-23}\).

## Poznámka Anki 1730839994758

Karty Anki: 1730839994758
GUID: ir6q&s;1!|; štítky: ni-mpi::p07 ni-spol::05.

### Otázka (Front)

Vyslovte tvrzení „o odhadu relativní chyby v reprezentaci pomocí strojového čísla.“

### Odpověď (Back)

Nechť \(x \in \mathbb R\) leží mezi nejmenším a největším normalizovaným kladným číslem množiny \(F\). Pak platí
\[\operatorname{fl}(x) = x(1 + \delta), \quad |\delta| \leq \mathbf u,\]kde \(\mathbf u\) je zaokrouhlovací jednotka (unit roundoff error).

## Poznámka Anki 1730840140271

Karty Anki: 1730840140271
GUID: F7,`UYut(.; štítky: ni-mpi::p07 ni-spol::05.

### Otázka (Front)

Vyslovte tvrzení „o odhadu relativní chyby při aritmetických operacích se strojovými čísly.“

### Odpověď (Back)

Nechť \(x, y \in F\) a \(\odot\) značí operaci sčítání, odčítání, násobení nebo dělení. Pokud je výsledek v intervalu normalizovaných čísel, tak platí
\[\operatorname{fl}(x \odot y) = (x \odot y)(1 + \delta), \quad |\delta| \leq \mathbf u,\]kde \(\mathbf u\) je zaokrouhlovací jednotka.

## Poznámka Anki 1730843062376

Karty Anki: 1730843062376
GUID: gvG<x[P]Kf; štítky: ni-mpi::p07 ni-spol::05.

### Otázka (Front)

Popište numerickou chybu typu krácení (cancellation) a její řešení.

### Odpověď (Back)

Numerická chyba typu krácení (cancellation) je zaokrouhlovací chyba, která nastává v případě, že jsou od sebe odčítána dvě skoro stejně velká čísla. Cifry nejvyšších řádů se odečtou a posunutím výsledku vznikají na konci reprezentovaného čísla prázdné pozice, které není možné dopočítat.
\[\begin{matrix}
\begin{matrix}
6.666\ 666\ 667\\
6.661\ 729\ 492\\
\hline
\end{matrix}\\
\begin{matrix}
0.004\ 937\ 175\\
4.937\ 175\ \color{red}{000}
\end{matrix}
\end{matrix}\]Krácení se lze vyhnout následujícími způsoby:

- přeformulování problému tak, aby nedocházelo k odčítání;
- použitím rozvojů funkcí do řad (např. do Taylorovy řady);
- použitím jiných rovností.

## Poznámka Anki 1730843374680

Karty Anki: 1730843374680
GUID: Dfu2`%l1mc; štítky: ni-mpi::p07 ni-spol::05.

### Otázka (Front)

Popište původ a řešení zaokrouhlovacích chyb.

### Odpověď (Back)

Zaokrouhlovací chyby vznikají v důsledku zaokrouhlovacích chyb v jednotlivých operacích a jejich kumulace a v důsledku krácení (cancellation). Lze se jim vyhnout pomocí:

- exaktní aritmetiky (\(\mathbb Z\), \(\mathbb Q\) nebo \(GF(p)\)),
- intervalové aritmetiky,
- reprezentace čísel formátem unum.

