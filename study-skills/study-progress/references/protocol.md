# Společný protokol studijních skillů

Tento soubor je společnou definicí pro `study-progress`, `study-library` a `study-tutor`.
Instaluj je jako tři sourozenecké adresáře. Instrukce a skripty patří ke skillům;
osobní studijní data patří do samostatného úložiště.

## Výběr úložiště a předmětu

- Použij cestu výslovně určenou uživatelem nebo již dohodnutou v této konverzaci.
  Jinak v aktuálním projektu použij `studium/` v kořeni projektu. Pracuješ-li mimo
  jednoznačný projekt, nejprve zjisti umístění. Pro CLI vždy převeď cestu na absolutní.
- Při navazování vypiš `subjects`. Identifikuj předmět podle zadání a uloženého názvu.
  Předmět aktivně zvolený uživatelem platí do výslovného přepnutí v této konverzaci.
  Pokud je více možných předmětů a žádný zvolený, zeptej se. Jeden existující předmět
  lze použít pro obecné „pokračuj v učení“, ale ne pro jiný výslovně jmenovaný předmět.
- `subject_id` je stabilní identifikátor malými ASCII písmeny, číslicemi a pomlčkami,
  například `linearni-algebra-2026-zs`. `topic_id`, `source_id`, `lesson_id` a
  `checkpoint_id` používají stejný formát (nejvýše 64 znaků).
- Každá operace nad předmětem vyžaduje `--subject`. Žádný globální „poslední předmět“
  se neukládá. Témata a zdroje mohou mít stejné ID ve dvou předmětech, ale nikdy se
  automaticky neslučují. Křížový přenos musí být výslovný a doložený v cílovém předmětu.

## Data

```text
studium/
├── profil.md                 # volitelný; jazyk, tempo, způsob nápovědy
└── subjects/
    └── subject-id/
        ├── state.json        # cíle, témata, katalog, checkpointy
        ├── .lock             # zámek souběžných zápisů
        └── sources/          # převzaté originály pod původními názvy
```

`profil.md` smí obsahovat obecné preference. Konkrétní znalosti, chyby, zdroje a
výsledky patří do odpovídajícího předmětu. Profil se při výuce automaticky nemění.
JSON používáme kvůli čtení i validaci standardním Pythonem bez dalších balíčků.
`state.json` má `schema_version: 1` a povinné `subject_id`, `name`, `goals`,
`topics`, `sources`, `checkpoints`. Podřízené záznamy nesou vlastní `subject_id`.

Používej společný nástroj `study-progress/scripts/study_store.py` pro všechny změny
stavu. Zamyká změny jednoho předmětu a nahrazuje JSON atomicky; jednotlivé skilly
nepřepisují stav vlastními neověřenými zápisy. Při neznámé verzi nebo neshodě ID
zastav operaci a vysvětli problém, nezakládej náhradní paměť.

## Předání mezi rolemi

1. **Učitel → paměť:** vybraný předmět a případné téma; požadavek na `resume`.
2. **Učitel → zdroje:** stejný předmět, téma a hledaný pojem.
3. **Zdroje → učitel:** původní pasáže, `source_id`, verze, `locator`, priorita,
   informace o nečitelných zdrojích nebo rozporech. Závisí-li výklad či hodnocení
   na konvenci, také doložená definice, význam značení a podmínky; osnova ani
   historický souhrn ji nenahrazují. Neověřený význam předej jako nejistotu.
4. **Učitel → paměť:** checkpoint s výsledkem skutečné aktivity a dalším krokem.
5. **Paměť → učitel:** potvrzení zápisu, aktuální stav tématu a plán opakování.

Při `passed` vyžaduj odpověď a vyhodnocení s kritériem úspěchu. Nápověda má být
zaznamenána; stav `demonstrated` nástroj povolí pouze u úspěchu bez nápovědy.
Historie checkpointů se zachovává. Další `introduced` nesmaže dříve ověřenou
dovednost; pozdější `needs-practice` ji naopak vrátí k procvičení.

`unassessed` uchovává neuzavřenou aktivitu bez připsání chyby, úspěchu nebo
výkladu. Nejistota učitele se nesmí proměnit v obtíž studenta.
Oprava používá nové ID a `correction_of` odkazující na aktuální účinnou verzi
téže aktivity. Zachovává její zadání, odpověď, téma i lekci. Účinný výsledek se
uplatní na místě původní aktivity; pozdější pokusy mají stále svou platnost.
`history` označuje nahrazené záznamy, `resume` vrací poslední účinnou aktivitu
a zvlášť poslední opravu. Oprava se nepočítá jako nový pokus a samotný výklad
neopraví dřívější nesprávné hodnocení.

## Zdroje a omezení

Dodané místní originály se přes `source-add` přesouvají do knihovny pod původními
názvy a evidují se se SHA-256. Jejich obsah se nemění a nevytváří se duplicitní
pracovní kopie. `original_path` uchovává dřívější vstupní umístění, `file` označuje
aktuální relativní cestu v předmětu a `ingest_mode: move` označuje převzetí přesunem.
Stejný postup platí pro dodaný přepis. Před převzetím musí uživatel výslovně přiřadit
dané materiály k předmětu podle `study-library`. Nová verze má nové `source_id`.
Citace checkpointu obsahuje `source_id` a přesný `locator` vrácený nástrojem.
Katalog obsahuje extrahované pasáže s původním číslováním. Skryté snímky se také
evidují; při použití posuzuj jejich relevanci. Textová extrakce sama nezaručuje
správné zachycení obrázků, tabulek, matematického zápisu či poznámek přednášejícího.

Studijní stav je navázaný na soubory tohoto úložiště. Další chat musí mít přístup
ke stejnému úložišti a skillům. Přenos na jiný počítač vyžaduje přenos těchto dat.
Uložené datum opakování nespouští úlohu na pozadí.
