# Veřejný katalog poskytovatelů pro syntetická data

Katalog obsahuje veřejné názvy firem a služeb a výslovně smyšlené osobní protistrany. Pole `name` nyní používá veřejné kanonické názvy, nikoli descriptory ze soukromého výpisu. `origin = public-catalog` označuje veřejný zdroj; `fictional-person` smyšlenou osobu.

Ověření subjektů je uložený záznam ze 7. 10. 2026. Nejde o potvrzení bankovního descriptoru, platby, ceny, účtu ani existence provozovny v celém období generovaných dat. Ověření se během generování znovu neprovádí.

- `canonical_name`: veřejný název subjektu nebo smyšlené osoby.
- `source`, `verification_sources`: doklady veřejného poskytovatele.
- `checked_on`: datum kontroly, včetně neúspěšné.
- `verified_on`: datum doložení; u nedoložených subjektů a smyšlených osob zůstává prázdné.
- `verification_status`, `verification_scope`: stav a rozsah uloženého ověření.
- `category_fit`: relevance kategorie; confirmed, plausible, unsupported nebo synthetic_context.
- `enabled_for_generation`: generátor smí použít pouze povolené položky.

Nejednoznačné či nedostatečně doložené kombinace nejsou pro generování povolené. `verification_note` vysvětluje, že modelovaný název není dokladem soukromé bankovní transakce. Přehled katalogu je v `../../data/diagnostics/merchant_verification.csv`.
