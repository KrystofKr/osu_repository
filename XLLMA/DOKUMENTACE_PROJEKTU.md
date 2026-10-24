# XLLMA: souhrn projektu a výsledků

Stav projektu k **9. 10. 2026**. Dokument shrnuje vývoj řešení a tři dokončené experimenty s lokálním jazykovým modelem. Podrobné soubory, skripty a příkazy popisuje [data/README.md](data/README.md).

## 1. Cíl a hlavní výsledek

Projekt ověřuje kategorizaci českých bankovních transakcí modelem **Qwen3.5:4b** ve dvou úlohách: výběr z pevného číselníku a návrh vlastní taxonomie s následnou klasifikací.

**Dávka 16 dosáhla vyšší shody se scénáři a kratšího času než zpracování po jedné. Vlastní taxonomie nepřinesla jednoznačné zlepšení.** Výsledky platí pro použitý model, prompt a syntetická data; jejich příčiny ani přenos na reálné výpisy zatím nebyly ověřeny.

| Oblast | Stav |
|---|---|
| Dataset | 10 625 transakcí: 1 625 referenčních a 9 000 hlavních syntetických |
| Období transakcí | 1. 1. 2022 až 5. 10. 2026 |
| Hlavní sada | 12 smyšlených profilů |
| Pevná taxonomie | 89 podrobných kategorií a 15 hlavních skupin |
| Zastoupené scénáře | 68 podrobných kategorií a 14 hlavních skupin |
| Model a prostředí | `qwen3.5:4b`, lokální Ollama 0.34.0 |
| Vlastní taxonomie Qwenu | 29 kategorií a 14 skupin; při klasifikaci použito 28 kategorií |

## 2. Vývoj řešení a data

Projekt začal sloučením soukromých bankovních CSV a konzistentním nahrazením osobních jmen. Pseudonymizace však zachovávala částky a časové i nákupní vzorce. Proto byly **9. 10. 2026 všechny soukromé transakce a jejich odvozené výstupy nahrazeny plně syntetickými daty**. Současné výsledky nepopisují finanční chování majitele projektu.

Následně vznikl generátor rozmanitých plateb, veřejný katalog poskytovatelů, pravidlová klasifikace, stabilní číselníky, EDA a automatické kontroly. Po ručním testu a pilotu na 50 transakcích převzal úplnou i omezenou LLM klasifikaci skript `classify_all_llm.py`. Posledním rozšířením je návrh vlastní taxonomie modelem.

### Současné datové sady

- **Reference:** 1 625 smyšlených plateb s identifikátory `REF-*` v `data_all.csv`. Historický název zůstal kvůli kompatibilitě.
- **Hlavní sada:** 9 000 plateb `SYN-*`, seed `20261009`; modeluje různé domácnosti, pravidelné příjmy a výdaje, nákupy, převody, vratky i dovolené.
- **Kombinovaná sada:** `data_combined.csv`, každý z 10 625 identifikátorů právě jednou.

Reference pochází ze stejného typu generátoru jako hlavní sada. Její scénáře obnovuje `recover_reference_scenarios.py`: přegeneruje data se seedem `20261010`, vybere referenci se seedem `20261011` a zapíše štítky pouze při přesné shodě všech bankovních sloupců. **Reference není nezávislý reálný benchmark.**

CSV používají UTF-8, středník a desetinnou čárku. Všechny zaúčtované částky jsou v CZK; 413 řádků navíc uchovává původní částku v EUR. Kurzy, roční navýšení částek a preference profilů jsou modelové předpoklady. Bankovní účty, karty a osobní jména jsou smyšlené.

Katalog obsahuje 117 položek v 67 kategoriích; 111 je povoleno pro generování. Veřejné názvy poskytovatelů nejsou potvrzenými bankovními descriptory ani dokladem skutečných nákupů. Podrobnosti a úroveň ověření uvádí [dokumentace katalogu](project/scripts/merchant_catalog_README.md).

### Štítky a závěry EDA

| Druh štítku | Zdroj a význam |
|---|---|
| Scénář generátoru | `reference_scenarios.csv`, `synthetic_profiles.csv`; cíl hodnocení |
| Heuristický odhad | `original_profiles.csv`; pravidla podle typu operace, protistrany a poznámek |
| Predikce modelu | Journal konkrétního experimentu; měřený výsledek |

Heuristika označuje **786 z 1 625 referenčních řádků jako neurčené (48,37 %)**. Její štítky ani slovní jistota nejsou nezávislou pravdou. Také scénář generátoru vyjadřuje konstrukční záměr, který nemusí být z bankovního textu poznatelný.

[EDA notebook](project/notebooks/EDA.ipynb) ověřil kvalitu a propojení dat: bez neplatných dat či částek, poškozených znaků v kontrolovaných polích a zcela duplicitních řádků. Ukázal také důležitá omezení:

- Osobní popis je vyplněn u 4,01 % řádků a zpráva pro příjemce u 50,02 %. Četnosti jsou konstrukční předpoklad; některé zprávy mohou přímo prozradit scénář.
- Větší hlavní sada a četné kategorie ovládají celkové skóre, proto se hodnotí i jednotlivé zdroje a macro-F1.
- Rok 2026 končí 5. října. Součty zahrnují převody a vratky; rozdíl příjmů a výdajů není zůstatek účtu.

## 3. Společná metodika experimentů

Model dostává pouze sedm polí: `Datum provedeni`, `Nazev protiuctu`, `Castka`, `Mena`, `Typ transakce`, `Popis pro me` a `Zprava pro prijemce`. Scénáře, profily, heuristické štítky, auditní důvody ani katalog do požadavků nevstupují. Hodnoticí štítky se připojují až při vyhodnocení.

| Parametr klasifikace | Nastavení |
|---|---|
| Model | `qwen3.5:4b`, stejný digest ve všech třech experimentech |
| Temperature / seed | 0 / 42 |
| Kontext | 8 192 tokenů |
| Thinking / stream | Vypnuto / vypnuto |
| Workers | 1 při posledním spuštění dokončených běhů |
| Limit odpovědi | 80 × počet transakcí v požadavku |

Ollama běží lokálně na `http://127.0.0.1:11434`; model se nedotrénovává. Dávka 16 znamená společný kontext pro 16 položek. Model vrací JSON s místními identifikátory a dvěma kódy kategorií. Skript kontroluje úplnost, jedinečnost a platnost odpovědí; hlavní kategorii nedopočítává z podrobné, takže případný nesoulad zůstává měřitelný.

`run.json` ukládá prompt, parametry, digest modelu a SHA-256 vstupů. `predictions.jsonl` umožňuje pokračovat po přerušení a slouží vyhodnocení. Změna vstupů, taxonomie či uzamčené konfigurace vyžaduje novou výstupní složku.

Shoda a F1 měří soulad se scénářem generátoru. Macro-F1 průměruje cílové kategorie s nenulovým zastoupením a upozorňuje na slabé výsledky méně četných kategorií. Časy sčítají aktivní běhy včetně komunikace a zápisu, bez pauz a vyhodnocení; nejde o opakovaný řízený benchmark hardwaru.

## 4. Experimenty A a B: pevná taxonomie

**A** klasifikoval všech 10 625 transakcí v dávkách po 16. **B** zpracoval stejné transakce po jedné, bez historie předchozích požadavků. Zachoval modelový digest, prompt, taxonomii, vstupy i ostatní klasifikační parametry; limit odpovědi se v obou případech řídil pravidlem 80 tokenů na položku.

| Metrika, všech 10 625 řádků | A: dávka 16 | B: po jedné |
|---|---:|---:|
| Shoda podrobné kategorie | 58,26 % | 45,18 % |
| Macro-F1 podrobné kategorie | 40,48 % | 37,66 % |
| Shoda hlavní kategorie | 71,30 % | 60,51 % |
| Macro-F1 hlavní kategorie | 68,94 % | 63,82 % |
| Současná shoda obou úrovní | 58,23 % | 45,18 % |
| Konzistence hierarchie | 99,69 % | 99,60 % |
| Neurčeno | 3,05 % | 11,95 % |
| Čas klasifikace | 40,55 min | 88,68 min |

**Zpracování po jedné snížilo podrobnou shodu o 13,08 procentního bodu a trvalo přibližně 2,19× déle.** Stejný trend přetrval po vynechání 50 příkladů použitých při vývoji promptu: A dosáhl podrobné/hlavní shody 58,22 % / 71,25 %, B 45,13 % / 60,47 %.

Kontrola potvrdila správné párování identifikátorů, scénářů a vstupů. Podrobné přiřazení se zlepšilo u 599 řádků a zhoršilo u 1 989. Největší propad nastal u telefonu a internetu: recall klesl z 86,75 % na 0 % u 800 transakcí. Odpovědi byly úplné a limit výstupních tokenů pokles nevysvětluje.

Možným vysvětlením je vliv společného kontextu, chyby při převodu významu na abstraktní kódy nebo využití pravidelností generátoru. **Příčina nebyla izolovaným experimentem prokázána.** Ani pozorované rozdíly podle pozice v dávce ji neurčují, protože pořadí a obtížnost nebyly náhodně vyvážené.

Podklady: [report A](data/experiments/qwen3.5_4b_all_categories/evaluation_report.md), [report B](data/experiments/qwen3.5_4b_single_t0/evaluation_report.md), [párové porovnání A/B](data/experiments/qwen3.5_4b_single_t0/comparison_report.md).

## 5. Experiment C: vlastní taxonomie Qwenu

Ze společné sady se náhodně vybralo **512 transakcí bez opakování, seed 42**. Qwen z osmi vzorků po 64 navrhl kategorie a jejich definice, poté je sjednotil. Nedostal pevný číselník ani hodnoticí štítky. Skript přidělil kódy D/H a zmrazil `taxonomy.json`; následně model označil všech 10 625 řádků v dávce 16.

Neplatné návrhy se vracely modelu k opravě a nepoužité hlavní skupiny se odstranily. Významy a názvy se ručně neopravovaly. Návrh používal kontext 16 384 tokenů, sjednocení 32 768; klasifikace zachovala společné nastavení.

| Výsledek | Hodnota |
|---|---:|
| Navržené podrobné kategorie / hlavní skupiny | 29 / 14 |
| Použité podrobné kategorie | 28 |
| Neurčitý účel | 924 řádků; 8,70 % |
| Konzistence vlastní hierarchie | 98,46 %; 164 nesouladů |
| Evidovaný čas návrhu / klasifikace | 3,29 / 39,99 min |

Evidovaný čas návrhu nezahrnuje počáteční neúspěšný pokus při přípravě validace. Taxonomie obsahuje významové vady: neurčitý účel patří pod příjmy, doprava je spojena s telekomunikacemi a některé sportovní a cestovní kategorie se překrývají.

### Srovnání odlišných kategorií

Přímá shoda nových D/H kódů s původními K/G kódy nedává smysl. Primárně se proto porovnává rozdělení transakcí na **10 113 řádcích mimo návrhový vzorek**; na stejném řezu se přepočítal experiment A. ARI zohledňuje náhodnou shodu, homogenita čistotu kategorií vůči scénářům, úplnost jejich nerozpadání a V-measure obě poslední vlastnosti spojuje.

| Úroveň a taxonomie | ARI | Homogenita | Úplnost | V-measure |
|---|---:|---:|---:|---:|
| Podrobná, pevná A | 0,5960 | 72,95 % | 74,19 % | 73,57 % |
| Podrobná, vlastní C | 0,6605 | 65,26 % | 78,93 % | 71,44 % |
| Hlavní, pevná A | 0,5707 | 65,05 % | 62,82 % | 63,92 % |
| Hlavní, vlastní C | 0,4295 | 54,79 % | 54,65 % | 54,72 % |

**Vlastní taxonomie zvýšila podrobný ARI, ale snížila V-measure na obou úrovních i hlavní ARI.** Výsledek není jednoznačně lepší; srovnání zahrnuje změnu granularity, definic i promptu. Metriky rozdělení navíc neověřují správnost názvů a významů kategorií.

Doplňková většinová asociace nových kategorií ke scénářům, odvozená pouze z 512 návrhových řádků, dosáhla na zbytku podrobné shody 62,21 % a macro-F1 22,53 %; hlavní shody 63,18 % a macro-F1 40,81 %. Jde o statistické přiřazení, které nelze přímo srovnávat s přesností A ani považovat za ručně ověřenou významovou ekvivalenci.

Podklady: [report C](data/experiments/qwen3.5_4b_discovered/evaluation_report.md), [návrhový manifest](data/experiments/qwen3.5_4b_discovered/discovery.json), [zmrazená taxonomie](data/experiments/qwen3.5_4b_discovered/taxonomy.json), [podrobný číselník](data/experiments/qwen3.5_4b_discovered/category_dictionary.csv).

## 6. Organizace, kontroly a reprodukování

| Umístění | Obsah |
|---|---|
| `data/transactions/` | Referenční, hlavní a kombinované bankovní CSV |
| `data/profiles/`, `data/dictionaries/` | Scénáře, heuristické štítky, profily a pevné číselníky |
| `data/diagnostics/`, `data/experiments/` | Audity, manifesty, predikce, metriky, reporty a grafy |
| `project/scripts/` | Generování, validace, klasifikace a vyhodnocení |
| `project/notebooks/EDA.ipynb`, `project/tests/` | Analýza a automatické kontroly |

Validátor a testy kontrolují schémata, datové návaznosti, prefixy REF/SYN, číselníky, obnovu scénářů, oddělení metadat od LLM vstupů, odpovědi modelu, pokračování běhů a metriky. **Při poslední revizi prošlo 18 testů.** Základní kontrola z kořene repozitáře `osu_repository`:

```bash
.venv/bin/python XLLMA/project/scripts/validate_data.py
.venv/bin/python -m unittest discover -s XLLMA/project/tests -v
```

Úplné příkazy pro generování, nové běhy a vyhodnocení jsou v [data/README.md](data/README.md). Nový experiment patří do nové složky. Pro srovnání bez historických 50 vývojových příkladů je nutné převzít `evaluation_context.prompt_development_ids`; nové běhy je automaticky nedědí.

**CSV a `data/experiments/` jsou ignorované Gitem**, takže odkazy na výsledky vyžadují místní artefakty. Generátor i obnova scénářů předpokládají existující syntetickou referenci; vytvoření celého datasetu z čistého klonu zatím není hotové jedním příkazem. Generování přepisuje data a metadata, proto po změně vstupů nelze pokračovat ve starém experimentu. Vyhodnocení lze zopakovat z kompletního journalu bez nové inference.

## 7. Omezení a další kroky

Dosavadní výsledky vycházejí z jednoho dokončeného běhu každé konfigurace a ze scénářů společného typu generátoru. Chybí nezávislá lidská anotace, test reálných výpisů a ověření na nových obchodnících. Některé účely nelze z dostupného textu určit; modelované poznámky a pravidelné platby mohou úlohu naopak usnadňovat. Teplota 0 a pevný seed nezaručují totožný výsledek po změně softwaru či hardwaru.

Další kroky, **zatím neprovedené**:

1. Ručně posoudit reprezentativní i nejednoznačné platby a významovou kvalitu navržené taxonomie.
2. Porovnat stejné transakce samostatně a na různých pozicích v náhodných dávkách; ověřit výstup názvů kategorií místo kódů.
3. Otestovat variantu bez poznámek a obchodníky nepoužité při vývoji promptu či taxonomie.
4. Doplnit opakování, jiné teploty a případně další model; klasifikátor zatím vyžaduje parametrizaci teploty a inference seedu.
5. Doplnit vytvoření syntetické reference z čistého klonu a přenos datových i výsledkových artefaktů.
