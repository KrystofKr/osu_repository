# Plně syntetická data XLLMA

Souhrn vývoje, rozhodnutí a všech experimentů je v [dokumentaci postupu a výsledků](../DOKUMENTACE_PROJEKTU.md).

Soukromé transakce byly 9. 10. 2026 nahrazeny nezávisle vygenerovanými smyšlenými platbami. Žádný současný výpis nepředstavuje skutečné transakce majitele projektu. Původní částky, data, bankovní údaje a poznámky se nezachovávají. Název `data_all.csv` zůstává kvůli kompatibilitě skriptů.

## Soubory

| Soubor | Význam |
|---|---|
| transactions/data_all.csv | 1 625 syntetických referenčních transakcí, identifikátory REF-* |
| transactions/data_synthetic.csv | 9 000 syntetických transakcí, identifikátory SYN-* |
| transactions/data_combined.csv | Obě sady, celkem 10 625 transakcí |
| profiles/reference_scenarios.csv | Obnovené scénáře referenčních transakcí po přesném ověření reprodukce |
| profiles/original_profiles.csv | Heuristická kategorizace syntetické reference; historický název souboru |
| profiles/synthetic_profiles.csv | Kategorie ze scénářů generátoru a 12 smyšlených profilů |
| dictionaries/category_dictionary.csv | Stabilní kódy kategorií, četnosti řádků a identifikátorů |
| dictionaries/category_mapping.csv | Převod názvů kategorií na kódy a hlavní skupiny |
| dictionaries/main_category_dictionary.csv | Četnosti hlavních skupin |
| diagnostics/original_classification_audit.csv | Důvody heuristického zařazení reference, nikoli soukromých dat |
| diagnostics/merchant_verification.csv | Veřejný katalog poskytovatelů, bez původních bankovních descriptorů |

V obou profile souborech je `Synteticka = 1`. Zdroj sady rozlišuj podle souboru metadat nebo prefixu identifikátoru, nikoli tímto příznakem. Oznámení „original“ ve skriptech a názvy sloupců `Cetnost originalni ...` znamenají syntetickou referenci. Profil R00 je společné označení heuristicky klasifikované reference, nikoli osoba či jeden účet.

## Spuštění

```bash
.venv/bin/python -m pip install -r XLLMA/project/requirements.txt
python3 XLLMA/project/scripts/generate_synthetic.py
python3 XLLMA/project/scripts/classify_original.py
python3 XLLMA/project/scripts/build_category_dictionaries.py
python3 XLLMA/project/scripts/validate_data.py
.venv/bin/python -m unittest discover -s XLLMA/project/tests -v
```

Generátor přepisuje hlavní syntetickou sadu, její metadata a společný výpis. Klasifikátor přepisuje referenční metadata a audit. Číselníky se obnovují poslední. `validate_data.py` kontroluje bez zápisu. Testy pracují v dočasné složce. Import skriptů data nepřepisuje.

Notebook `../project/notebooks/EDA.ipynb` analyzuje odděleně referenci a hlavní syntetickou sadu. CSV jsou UTF-8, oddělovač středník, desetinná čárka; CSV jsou ignorována Gitem.

## Omezení a LLM

Kategorie reference jsou heuristické odhady, nikoli ruční pravda. Kategorie hlavní sady pocházejí ze scénářů generátoru a nemusejí být poznatelné z textu platby. Správnost LLM vyžaduje nezávisle posouzené příklady; shoda s pravidly sama není správnost. Žádné současné výsledky nelze prezentovat jako analýzu reálného uživatele.

Generátor používá pevné fiktivní kurzy, modelovou inflaci, pevné profily a předpoklady pro četnost poznámek (4 % popis pro mě, 50 % zpráva pro příjemce). Tyto parametry nyní nejsou odvozené ze soukromého výpisu. Názvy firem pocházejí z veřejného katalogu, bankovní čísla a osobní jména jsou smyšlená. Názvy nejsou potvrzenými bankovními descriptory a katalog neprokazuje skutečný nákup ani dostupnost služby v každém historickém dni.


## Kontrola označení zdrojů

Generátor, klasifikátor, číselníky a validátor odmítnou `data_all.csv` bez prefixů REF-. Validátor kontroluje SYN- u hlavní sady a příznak `Synteticka = 1` v obou metadatech; stejné kontroly má EDA. Jde o ochranu před nechtěným vložením běžného bankovního exportu, nikoli o důkaz syntetického původu libovolně přeznačených dat.

Historické názvy `original_profiles.csv`, `original_classification_audit.csv`, `classify_original.py` a sloupce `Cetnost originalni ...` jsou ponechané kvůli kompatibilitě. `Puvodni kategorie` je vstupní název před sjednocením aliasů. Bankovní sloupce `Originalni castka` a `Originalni mena` označují částku a měnu před přepočtem, nikoli původ soukromých dat. Nulové kategorie v číselníku zůstávají kvůli stabilním kódům; nejsou dokladem současných transakcí.


## Úplná klasifikace a vyhodnocení

`classify_all_llm.py` zpracuje celý společný výpis do 89 podrobných a 15 hlavních kategorií. Qwen vybírá oba kódy; nesoulad mezi jejich hierarchií se vykazuje jako chyba konzistence, automaticky se neopravuje. Každý požadavek obsahuje pevnou taxonomii a dávku 16 nezávislých transakcí. Model dostává pouze bankovní údaje, nikoli scénáře, heuristické štítky nebo katalog poskytovatelů.

Pro syntetickou referenci byl scénář generátoru obnoven pomocí seedů 20261010 a 20261011 v `recover_reference_scenarios.py`. Zápis `profiles/reference_scenarios.csv` proběhne pouze po přesné shodě všech bankovních sloupců se současným výpisem. Soubor je samostatná scénářová reference, nenahrazuje heuristické `original_profiles.csv` a není vstupem do modelu.

Ze složky XLLMA:

```bash
python3 project/scripts/recover_reference_scenarios.py
python3 project/scripts/classify_all_llm.py
python3 project/scripts/evaluate_llm.py
```

Přerušená klasifikace pokračuje ze souboru `predictions.jsonl`. `run.json` uzamyká vstupní soubory, digest modelu, prompt, nastavení i velikost dávky. `--workers` určuje souběžné požadavky; zrychlí běh pouze při paralelní podpoře serveru. Host musí být lokální. Výstupy zůstávají pod `data/experiments/qwen3.5_4b_all_categories/`.

Malý kontrolní běh používá stejný skript:

```bash
python3 project/scripts/classify_all_llm.py --max-new 50 --output data/experiments/pilot
python3 project/scripts/evaluate_llm.py --experiment data/experiments/pilot --allow-partial
```

Limit vybere prvních 50 dosud nezpracovaných transakcí v pořadí společného výpisu; není to náhodný ani reprezentativní vzorek. Opakování zpracuje dalších 50. Bez `--max-new` se dokončí celý výpis. Při změně vstupů, promptu, modelového digestu nebo velikosti dávky použij novou výstupní složku. Klasifikace vybírá z pevné taxonomie a nemění bankovní výpisy ani jejich metadata. Lokální API musí běžet na 127.0.0.1:11434; výsledky experimentů jsou ignorované Gitem.

- `run.json`: nastavení, kontrolní součty vstupů, digest modelu a průběh běhu.
- `predictions.jsonl`: průběžný zápis odpovědí potřebný pro pokračování klasifikace a vyhodnocení.
- `predictions.csv`: každý bankovní řádek, obě kategorie Qwenu, scénářové štítky, shody a konzistence hierarchie; referenční řádky obsahují navíc heuristické kódy.
- `evaluation_report.md`: parametry experimentu, čas klasifikace, souhrn výsledků a nejčastější záměny.
- `evaluation.json`: metriky za celý výpis a jednotlivé sady, včetně podrobných a hlavních kategorií.
- `category_metrics.csv`: precision, recall a F1 jednotlivých kategorií a skupin.
- `confusions.csv`: četnosti cílových a predikovaných dvojic kategorií.

Evaluator standardně odmítá neúplný běh; `--allow-partial` je pouze pro průběžnou kontrolu. Přesnost a macro-F1 vyjadřují shodu se scénářovým záměrem generátoru. Neprokazují stejnou kvalitu na reálných výpisech; část scénářů nelze z bankovního textu jednoznačně určit. Macro-F1 používá kategorie s nenulovým cílovým zastoupením. Srovnání s heuristikou je vykázané zvlášť jako shoda, nikoli nezávislá přesnost.

Aktuální Qwen3.5 ve verzi Ollamy 0.34.0 paralelní požadavky nepodporuje; pro něj používej `--workers 1`. Pro export grafů vyhodnocení spusť `.venv/bin/python XLLMA/project/scripts/evaluate_llm.py --plots` z kořene repozitáře.

U dokončeného experimentu obsahuje vyhodnocení i řádek `excluding_pilot`, který vynechává 50 transakcí z prvního pilotu použitého při úpravě instrukcí. Jejich identifikátory jsou uložené v `run.json` pod `evaluation_context.prompt_development_ids`. Starý pilotní skript a jeho samostatné výstupy byly odstraněny; úplný experiment na nich nezávisí. Nové experimenty bez těchto metadat tento řádek nevytvářejí.

### Porovnání s jednotlivými transakcemi

Experiment `qwen3.5_4b_single_t0` používá jednu transakci na požadavek, jednoho pracovníka, teplotu 0, seed 42, kontext 8 192 tokenů a limit odpovědi 80 tokenů. Zachovává modelový digest, prompt, vstupní soubory a taxonomii experimentu s dávkou 16. Identifikátory 50 vývojových příkladů jsou převzaté do jeho `evaluation_context`, aby bylo možné porovnat i shodu bez těchto příkladů.

Ze složky XLLMA:

```bash
python3 project/scripts/classify_all_llm.py --batch-size 1 --workers 1 --output data/experiments/qwen3.5_4b_single_t0
python3 project/scripts/evaluate_llm.py --experiment data/experiments/qwen3.5_4b_single_t0
```

Každý požadavek dostává samostatnou transakci a společné instrukce, bez historie předchozích požadavků. Čas v reportu sčítá aktivní spuštění klasifikátoru; pauzy mezi pokračováními a vyhodnocení do něj nevstupují. Výsledek s dávkou 1 lze porovnat s dávkou 16 na stejných identifikátorech. Teplota se v tomto srovnání nemění.

Dokončené [porovnání obou běhů](experiments/qwen3.5_4b_single_t0/comparison_report.md) ukazuje při zpracování po jedné podrobnou shodu 45,18 % a hlavní shodu 60,51 %, oproti 58,26 % a 71,30 % v dávce 16. Čas vzrostl ze 40,55 na 88,68 minut. Jde o výsledek tohoto modelu, promptu a syntetických dat, nikoli obecné pravidlo o velikosti dávek. Reporty experimentů jsou místní ignorované výstupy.

### Kategorie navržené samotným LLM

Experiment `qwen3.5_4b_discovered` má dvě oddělené fáze. `discover_categories.py` vybere 512 náhodných transakcí bez opakování (seed 42). Qwen z osmi vzorků po 64 navrhne vlastní české hlavní a podrobné kategorie, jejich definice a jednu kategorii pro neurčitelný účel. Poté vlastní návrhy sjednotí. Existující číselníky, scénáře, heuristika, profily a katalog obchodníků nejsou vstupem návrhu ani následné klasifikace. Technické stropy návrhu jsou 60 podrobných kategorií a 16 hlavních skupin; konkrétní počet volí model.

Skript přidělí novým kategoriím kódy D001… a skupinám H001…, odstraní pouze nepoužité hlavní skupiny a zmrazí `taxonomy.json`. Významy a názvy nepřepisuje ručně. Pokud návrh nemá platnou strukturu, může požádat Qwen o dvě opravy; všechny požadavky a odpovědi uchovává. Klasifikace potom používá pouze tuto zmrazenou taxonomii a její definice, dávku 16, teplotu 0 a ostatní klasifikační nastavení předchozího dávkového experimentu. Během označování se kategorie nedoplňují.

Ze složky XLLMA:

```bash
python3 project/scripts/discover_categories.py
python3 project/scripts/classify_all_llm.py --taxonomy data/experiments/qwen3.5_4b_discovered/taxonomy.json --output data/experiments/qwen3.5_4b_discovered
python3 project/scripts/evaluate_discovered.py --plots
```

Návrh i klasifikaci lze obnovit opakováním příkazu; změna dat, nastavení nebo taxonomie vyžaduje novou výstupní složku. Návrh používá kontext 16 384 tokenů, sjednocení 32 768 a klasifikace 8 192. Thinking je vypnuto. Taxonomie a její kontrolní součet jsou součástí konfigurace klasifikace. Původní číselníky ani bankovní CSV tento experiment nepřepisuje.

`evaluate_discovered.py` vyhodnocuje především 10 113 transakcí mimo návrhový vzorek. Odlišné názvy a granularita kategorií znamenají, že přímá shoda nových kódů D/H se scénářovými K/G nedává smysl. Report proto porovnává rozdělení pomocí ARI, homogenity, úplnosti a V-measure; stejné metriky počítá pro předchozí dávkový experiment na stejných řádcích. Navíc jen na návrhových řádcích stanoví většinovou asociaci nových kategorií ke scénářům a měří její shodu na zbytku. Tato asociace je statistická, může být více ku jedné a nenahrazuje významové ověření kategorií. Neurčené a v kalibračním vzorku nepozorované kategorie zůstávají bez asociace.

Výstupy jsou v `data/experiments/qwen3.5_4b_discovered/`: vlastní `category_dictionary.csv` a `main_category_dictionary.csv` s četnostmi, `predictions.csv`, `evaluation.json`, `contingency.csv`, [výsledkový report](experiments/qwen3.5_4b_discovered/evaluation_report.md) a grafy. `discovery.json`, `proposal_*.json`, `merged_proposal*.json`, `taxonomy.json`, `run.json` a `predictions.jsonl` uchovávají průběh a podklady pro pokračování. Výstupy jsou ignorované Gitem. Náhodný vzorek nemusí zachytit vzácné účely; zbývající řádky pocházejí ze stejného syntetického generátoru. Výsledky tedy neprokazují kvalitu na reálných platbách ani nových obchodnících.

Dokončený běh vytvořil 29 kategorií a 14 hlavních skupin a označil všech 10 625 transakcí. Použil 28 kategorií; neurčený účel má 924 řádků (8,70 %) a 164 zařazení porušuje vlastní hierarchii. Návrh trval evidovaných 3,29 minuty a klasifikace 39,99 minuty. Na 10 113 řádcích mimo návrhový vzorek má podrobné rozdělení ARI 0,6605 oproti 0,5960 s pevným číselníkem; hlavní rozdělení má ARI 0,4295 oproti 0,5707. V-measure je v obou úrovních nižší: 71,44 % oproti 73,57 % a 54,72 % oproti 63,92 %. Výsledek tedy není jednoznačně lepší. Model například zařadil neurčitý účel pod příjmy a vytvořil překrývající se sportovní a cestovní kategorie; tyto vady nebyly ručně opravovány.

## Přehled skriptů

| Skript v `../project/scripts/` | Úloha |
|---|---|
| `generate_synthetic.py` | Generování hlavní syntetické sady, profilů a společného výpisu |
| `classify_original.py` | Heuristická klasifikace syntetické reference pro srovnání |
| `build_category_dictionaries.py` | Stabilní kódy kategorií, mapování a četnosti |
| `validate_data.py` | Kontrola konzistence výpisů, profilů, scénářů a číselníků |
| `recover_reference_scenarios.py` | Obnova scénářových štítků při přesné reprodukci referenčních transakcí |
| `classify_all_llm.py` | Úplná i omezená klasifikace lokálním LLM s pokračováním po přerušení |
| `discover_categories.py` | Návrh a zmrazení vlastní taxonomie lokálním LLM bez současných štítků |
| `evaluate_llm.py` | Vyhodnocení uložených odpovědí, tabulky a volitelné grafy |
| `evaluate_discovered.py` | Vyhodnocení vlastní taxonomie, četnosti a srovnání rozdělení s předchozím experimentem |
| `llm_utils.py` | Sdílený klient Ollamy a čtení/zápis experimentů; nespouští se samostatně |
| `data_paths.py` | Společné umístění datových souborů; nespouští se samostatně |
