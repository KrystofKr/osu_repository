# NI-KOP – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-kop/NI-KOP.apkg; APKG SHA-256 839a7b994c41f5101e3831bc0e7a29bed2ac769c91a17b3a39e01193f3c2cc2d. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 54a89306e31a0c0ff7d34f4ba51d9605d206359fb3335f23415bf297cf4d5a1c.
Původní balíčky: NI-KOP
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1732653871778

Karty Anki: 1732653871778
GUID: r.O#-P>d(N; štítky: ni-kop::p09 ni-spol::14.

### Otázka (Front)

Popište genetický algoritmus a jeho obecnou strukturu.

### Odpověď (Back)

Genetický algoritmus patří mezi evoluční algoritmy. Vyznačuje se následujícími vlastnostmi:

- **kódování jedince** - binární řetězec;

- **křížení **- dominující operátor (jednobodové, dvoubodové, uniformní);

- **mutace **- upozaděný operátor (inverze bitů);

- **řízení populace** - náhrada (en bloc nebo s elitismem).
Genetický algoritmus používá obecnou strukturu evolučního algoritmu (selekce, křížení, mutace a řízení populace).

## Poznámka Anki 1732654439560

Karty Anki: 1732654439560
GUID: LD$l/n/!3X; štítky: ni-kop::p09 ni-spol::14.

### Otázka (Front)

Popište populaci v evolučních algoritmech a metody jejího řízení.

### Odpověď (Back)

Populace je v evolučních algoritmech množina jedinců. Při křížení a mutaci vznikne z \(\mu\) rodičů \(\lambda\) potomků a výslednou populaci lze řídit následujícími metodami:

- **náhrada **\((\mu = \lambda)\) - potomci nahradí rodiče (náhrada en bloc), případně několik málo elitních rodičů zůstane v nové populaci (náhrada s elitismem);

- **soutěž** \((\mu + \lambda)\) - nová populace je vytvořena výběrem ze skupiny rodičů a potomků;

- **soutěž **\((\mu, \lambda)\) - nová populace je vytvořena výběrem pouze z potomků.

### Doplňující pole (Extra)

V případě \((\mu, \lambda)\) soutěže vyprodukuje \(\mu\) rodičů \(\lambda > \mu\) potomků. Pokud nastává rovnost, dochází k  náhradě en bloc \((\mu = \lambda)\).

## Poznámka Anki 1732656354868

Karty Anki: 1732656354868
GUID: K=>hX`;KG0; štítky: ni-kop::p09 ni-spol::14.

### Otázka (Front)

Popište metody křížení v genetickém algoritmu a jejich problémy.

### Odpověď (Back)

Metody křízení v genetickém algoritmu jsou závislé na zvoleném kódování. Předpokládejme dva jedince kódované pomocí binárních řetězců:
\[\begin{matrix}
a_1a_2 \dots a_n,\\
b_1b_2 \dots b_n,\\
\end{matrix}\]pak existují následující metody křížení jedinců:

- **jednobodové křížení **- je zvolen náhodný index \(i\) a potomci jsou sestrojeni jako

\[\begin{matrix}
a_1 \dots a_ib_{i + 1} \dots b_n,\\
b_1 \dots b_ia_{i + 1} \dots a_n;
\end{matrix}\]

- **dvoubodové křížení** - jsou zvoleny dva náhodné indexy \(i\) a \(j\) takové, že \(i < j\), a potomci jsou sestrojeni jako

\[\begin{matrix}
a_1 \dots a_ib_{i + 1} \dots  b_ja_{j + 1} \dots a_n,\\
b_1 \dots b_ia_{i + 1} \dots a_jb_{j + 1} \dots b_n;
\end{matrix}\]

- **uniformní křížení **- je zvolen náhodný binární řetězec, pokud je na jeho \(i\)-tém indexu \(0\), použije se v prvním potomku \(a_i\), pokud \(1\) tak \(b_i\), a druhý potomek je sestrojen inverzí tohoto binárního řetězce.

Jednobodové a dvoubodové křížení je závislé na pořadí, což způsobuje nerobustnost. Řešením je permutace prvků řetězce při zachování jejich významu (zapamatování původního pořadí).

## Poznámka Anki 1732657918869

Karty Anki: 1732657918869
GUID: pT=~ZYY*;B; štítky: ni-kop::p09 ni-spol::14.

### Otázka (Front)

Popište mutaci v genetickém algoritmu.

### Odpověď (Back)

Mutace v genetickém algoritmu je závislá na zvoleném kódování. Předpokládejme jedince kódované pomocí binárních řetězců. Při mutaci jsou jedinci interpretováni jako konkatenace těchto řetezců, ve které jsou invertovány bity na náhodných pozicích, dokud není dosaženo požadované pravděpodobnosti mutace.

## Poznámka Anki 1732658946599

Karty Anki: 1732658946599
GUID: f1qO}oAW}h; štítky: ni-kop::p09 ni-spol::14.

### Otázka (Front)

Popište selekci, selekční tlak a zdatnost jedince v evolučních algoritmech.

### Odpověď (Back)

**Selekce **je fáze evolučních algoritmů s cílem dosáhnout toho, aby početní zastoupení jedinců v populaci odpovídalo jejich zdatnosti. Probíhá v následujících krocích:

- z konfigurace, kterou jedinec reprezentuje, je vypočteno optimalizační kritérium odpovídající **zdatnosti jedince**;
- zdatnost jedince je na základě selekčního tlaku přepočtena na pravděpodobnost výběru jedince;
- proběhne náhodný výběr jedinců.

**Selekční tlak** je pravděpodobnost výběru nejzdatnějšího jedince. Určuje tedy, jak velký důraz je při náhodném výběru jedinců kladen na zdatnost.

## Poznámka Anki 1732740640157

Karty Anki: 1732740640157
GUID: k=h>lwRma,; štítky: ni-kop::p09 ni-spol::14.

Metadata původního zdroje pro kartu 1732740640157: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište vliv selekčního tlaku v evolučních algoritmech a jeho vazbu s pravděpodobností mutace.

### Odpověď (Back)

Selekční tlak v evolučních algoritmech má následující vliv:

- **příliš vysoký selekční tlak** - nebezpečí uváznutí v lokálním optimu (degenerace populace),

- **příliš nízký selekční tlak** - nebezpečí převážení mutace nad pomalou konvergencí (divergence).

Při snižování selekčního tlaku, musí tedy být snižována i pravděpodobnost mutace.

## Poznámka Anki 1732740908543

Karty Anki: 1732740908543
GUID: j@4~rd;qWn; štítky: ni-kop::p09 ni-spol::14.

### Otázka (Front)

Popište metody náhodného výběru jedinců v selekci evolučních algoritmů.

### Odpověď (Back)

Mezi metody náhodného výběru jedinců v selekci evolučních algoritmů patří:

- **ruletový výběr** - rozevření políčka rulety odpovídá pravděpodobnosti výběru, \(m\)-krát je zvolen náhodný úhel a vybrán odpovídající jedinec;

- **univerzální stochastické vzorkování** - vychází z ruletového výběru, je zvolen náhodný úhel, který je \((m - 1)\)-krát odměřen a je vybrán odpovídající jedinec.

### Doplňující pole (Extra)

Dále existuje turnajový výběr, který kombinuje přepočet zdatnosti na pravděpodobnost výběru jedince a náhodný výběr jedinců do jediného kroku.

## Poznámka Anki 1732741315243

Karty Anki: 1732741315243
GUID: Pz%O|hvq?y; štítky: ni-kop::p09 ni-spol::14.

### Otázka (Front)

Popište metody přepočtu zdatnosti na pravděpodobnost výběru jedince v selekci evolučních algoritmů.

### Odpověď (Back)

Pro přepočet zdatnosti na pravděpodobnost výběru jedince v selekci evolučních algoritmů není typicky využita přímá úměra, protože často vede k uváznutí v lokálním optimu (degeneraci populace). Pro zachování diverzity je totiž potřeba v populaci ponechat slabší jedince. Používají se následující metody:

- **scaling** - přepočet pomocí lineární funkce,

- **ranking** - seřazení jedinců podle zdatnosti a výběr na základě pořadí,

- **truncation selection** - výběr několika nejzdatnějších jedinců.

### Doplňující pole (Extra)

Dále existuje turnajový výběr, který kombinuje přepočet zdatnosti na pravděpodobnost výběru jedince a náhodný výběr jedinců do jediného kroku.

## Poznámka Anki 1732741966650

Karty Anki: 1732741966650
GUID: d8fx-O{D*r; štítky: ni-kop::p09 ni-spol::14.

### Otázka (Front)

Popište turnajový výběr v evolučních algoritmech a jeho souvislost se selekčním tlakem.

### Odpověď (Back)

Turnajový výběr kombinuje přepočet zdatnosti na pravděpodobnost výběru jedince a náhodný výběr jedinců v selekci evolučních algoritmů do jediného kroku. Funguje tak, že náhodně vybere několik jedinců a z nich zvolí toho nejzdatnějšího. Tento proces je opakován až do naplnění nové populace. Řízením velikosti turnaje lze řídit selekční tlak:

- **turnaj s celou populací** - vysoký selekční tlak, nejzdatnější jedinec je vždy vybrán (intenzifikace),

- **turnaj s jedním jedincem** - nízký selekční tlak, nezáleží na zdatnosti jedinců (diverzifikace).

## Poznámka Anki 1732742395594

Karty Anki: 1732742395594
GUID: IU|GOE.J*n; štítky: ni-kop::p09 ni-spol::14.

Metadata původního zdroje pro kartu 1732742395594: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište ukončovací podmínky genetického algoritmu.

### Odpověď (Back)

Ukončovací podmínky genetického algoritmu jsou typicky voleny podle:

- **peveného počtu populací** - algoritmus je ukončen po daném počtu populací,
- **příznaků konvergence** - změna průměrné zdatnosti mezi populacemi nebo rozložení zdatnosti v populaci.

## Poznámka Anki 1733088895677

Karty Anki: 1733088895677
GUID: w6&:m[NuZ0; štítky: ni-kop::p09 ni-spol::14.

### Otázka (Front)

Popište evoluční algoritmy a jejich obecnou strukturu. Uveďte příklady.

### Odpověď (Back)

Evoluční algoritmy jsou lokální heuristiky založené na práci s vícero stavy (jedinci). Jejich základním principem je, že stavy mezi sebou interagují a jejich kombinacemi vznikají nové stavy. Evoluční algoritmy jsou nejprve inicializovány s počáteční populací a poté v cyklu iterují následující kroky:

- **selekce **- výběr rodičů další populace s cílem zvýšení podílu zdatných jedinců (intenzifikace),

- **křížení **(binární operátor) - rekombinace genetické informace do nových jedinců,

- **mutace** (unární operátor) - náhodný zdroj nové genetické informace (diverzifikace),
- **řízení populace **- nahrazení staré populace novou populací.

Jejich výstupem je poté konečná populace. Mezi evoluční algoritmy patří:

- genetický algoritmus,
- genetické programování,
- evoluční strategie,
- evoluční programování.

