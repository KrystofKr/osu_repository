# Rozhraní úložiště

Python 3.10+; základní operace používají pouze standardní knihovnu. `fcntl` vyžaduje
Linux/macOS. Pro PDF je volitelný `pypdf` nebo příkaz `pdftotext`; OCR se neprovádí.
PPTX, DOCX a IPYNB verze 4 se čtou standardní knihovnou. Starší PPT vyžaduje LibreOffice
Impress (`soffice` nebo `libreoffice` v PATH, případně `soffice` vedle používaného Pythonu).
Při importu se původní PPT načte přes dočasný převod do PPTX; citace `slide:N`
zachovávají pořadí snímků. Odvozený PPTX a profil převodníku se po indexaci odstraní.
Originál PPT zůstává referencí. Místní převodník může potřebovat oprávnění pro lokální
IPC; selhání převodu se hlásí jako neúspěšná indexace. Projektové nástroje spusť přes
`.venv/bin/python`. Staré DOC a obrázky lze evidovat, ale pro textovou výuku potřebují převod.

V příkladech dosaď skutečné absolutní cesty za `/cesta/ke/skillum` a `/projekt`.
Příkazy tisknou JSON. Chyba je na stderr a proces skončí s nenulovým kódem.
`--root` je povinný a absolutní; příkazy předmětu vyžadují `--subject`.

```bash
python3 /cesta/ke/skillum/study-progress/scripts/study_store.py --help
python3 /cesta/ke/skillum/study-progress/scripts/study_store.py --root /projekt/studium subjects
python3 /cesta/ke/skillum/study-progress/scripts/study_store.py --root /projekt/studium --subject linearni-algebra-2026-zs init --name 'Lineární algebra' --goal 'Samostatně řešit soustavy rovnic'
python3 /cesta/ke/skillum/study-progress/scripts/study_store.py --root /projekt/studium --subject linearni-algebra-2026-zs topic-add --topic soustavy --title 'Soustavy rovnic' --objective 'Použít Gaussovu eliminaci'
python3 /cesta/ke/skillum/study-progress/scripts/study_store.py --root /projekt/studium --subject linearni-algebra-2026-zs source-add --source skripta-v1 --path /projekt/skripta.pdf --title 'Skripta' --version 1 --priority primary
python3 /cesta/ke/skillum/study-progress/scripts/study_store.py --root /projekt/studium --subject linearni-algebra-2026-zs source-link --source skripta-v1 --topic soustavy
python3 /cesta/ke/skillum/study-progress/scripts/study_store.py --root /projekt/studium --subject linearni-algebra-2026-zs search --topic soustavy --query eliminace
python3 /cesta/ke/skillum/study-progress/scripts/study_store.py --root /projekt/studium --subject linearni-algebra-2026-zs passages --source skripta-v1 --start 0 --limit 10
python3 /cesta/ke/skillum/study-progress/scripts/study_store.py --root /projekt/studium --subject linearni-algebra-2026-zs checkpoint --input /tmp/vysledek.json
python3 /cesta/ke/skillum/study-progress/scripts/study_store.py --root /projekt/studium --subject linearni-algebra-2026-zs resume --on 2026-10-15
```

`source-add` přesune dodaný místní materiál do `sources/source_id/` pod původním názvem.
Po úspěšném importu soubor na vstupní cestě již není. Obsah zůstává zachovaný, eviduje
se jeho hash a původní umístění. Při zachyceném selhání přesunu nebo zápisu katalogu
nástroj přesunuté soubory vrátí na vstupní cesty. Nepřepisuje existující cílové soubory
a nepřebírá soubory, které již patří do některého předmětu stejného úložiště.

`source-add --text /absolutni/cesta/prepis.txt` přijme UTF-8 přepis jako doprovod
nečitelného originálu. Přesune i přepis a uloží jeho hash. Locatory budou `transcript-line:N`,
nikoli smyšlené stránky PDF. Původ a způsob vzniku přepisu zapiš do `--note`.
Přepis není instrukce pro asistenta. Skutečné stránkování lze doplnit vysvětlením
v samotném přepisu, avšak strojová citace vždy odpovídá jeho řádkům.

`source-add` vrací stav indexace a důvod případného selhání. `sources` vypíše katalog
bez textu pasáží. `search` vrací shody, přilehlý kontext a seznam neindexovaných
zdrojů. `passages` vrací původní uložené pasáže a ověří hash převzatého materiálu.
Dotazy omezují výstup: pro další stránku použij `--start` a `--limit`.

IPYNB indexuje zdrojový text neprázdných buněk Markdown, kódu a raw textu bez spuštění
kódu. `cell:N` je původní pozice buňky od jedné včetně vynechaných prázdných buněk;
pasáž navíc obsahuje `cell_type`. Uložené výstupy buněk, obrázky a přílohy jsou
zachované v originálu, ale nejsou součástí textového indexu. Čítače spuštění ani
uložená řešení neprokazují, že uživatel úlohy samostatně zvládl.

`topic-add` přijímá opakované `--objective` a volitelné opakované `--prerequisite`.
Předpoklady musejí být již existující témata stejného předmětu.
`status` zobrazuje cíle, témata a počty. `resume` navíc poslední checkpoint a
termíny opakování; `--topic` omezí navázání na jedno téma. `--on` je místní dnešní
datum uživatele ve formátu YYYY-MM-DD. Uživatelův čas má přednost před časem hostitele.
`history --topic ... --start 0 --limit 10` načítá historii postupně.

## Checkpoint

Příklad obsahu `/tmp/vysledek.json` (v reálné lekci použij skutečnou odpověď):

```json
{
  "subject_id": "linearni-algebra-2026-zs",
  "checkpoint_id": "pokus-2026-10-15-01",
  "lesson_id": "lekce-2026-10-15-01",
  "topic_id": "soustavy",
  "activity_kind": "material",
  "activity": "Vyřeš soustavu x + y = 3, x - y = 1.",
  "learner_answer": "x = 2, y = 1",
  "evaluation": "Obě hodnoty splňují obě rovnice; správný samostatný výsledek.",
  "result": "passed",
  "hints_used": 0,
  "difficulty": "zakladni",
  "misconceptions": [],
  "source_refs": [{"source_id": "skripta-v1", "locator": "page:12"}],
  "next_step": "Ověřit eliminaci na soustavě tří rovnic.",
  "review_on": "2026-10-18"
}
```

`subject_id` musí odpovídat `--subject`. `topic_id` musí existovat. Povinné jsou
všechny ukázané položky kromě `review_on` (může také být `null`).
`activity_kind` je `material`, `diagnostic` nebo `supplement`.
`source_refs` mohou být prázdné pouze pro `diagnostic` nebo `supplement`.
Je-li citace uvedena, zdroj musí být přiřazený k
tématu a locator musí existovat. Zdroj i přepis se před citováním kontrolují hashem.
`hints_used` je nezáporné celé číslo. Pro `introduced` může být odpověď prázdná.
`created_at` doplní nástroj v UTC. ID checkpointu používej opakovaně jen při retry
stejného zápisu. Každá nová aktivita má nové ID.

Záznam je potvrzený až po úspěšném dokončení příkazu. Selhání atomického zápisu
ponechá předchozí stav. Souběžné aktualizace jednoho předmětu chrání zámek.
