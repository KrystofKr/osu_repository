# Plně syntetická data XLLMA

Soukromé transakce byly 9. 10. 2026 nahrazeny nezávisle vygenerovanými smyšlenými platbami. Žádný současný výpis nepředstavuje skutečné transakce majitele projektu. Původní částky, data, bankovní údaje a poznámky se nezachovávají. Název `data_all.csv` zůstává kvůli kompatibilitě skriptů.

## Soubory

| Soubor | Význam |
|---|---|
| transactions/data_all.csv | 1 625 syntetických referenčních transakcí, identifikátory REF-* |
| transactions/data_synthetic.csv | 9 000 syntetických transakcí, identifikátory SYN-* |
| transactions/data_combined.csv | Obě sady, celkem 10 625 transakcí |
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
