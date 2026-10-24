# Ověření studijních skillů

## Aktualizace 24. 10. 2026 — konvence a opravy hodnocení

`study-tutor` nově vyžaduje ověření původní definice před výkladem či opravou,
pokud správnost závisí na konvenci. Rozlišuje ji od osnovy a historického
souhrnu, při námitce kontroluje vlastní kritérium a na žádost o příklad
z materiálů vyžaduje dohledaný zdrojový příklad. Neověřená konvence se nesmí
proměnit v připsanou chybu studenta. `study-library` předává potřebné definice,
jejich kontext, původ a rozdíly konvencí. Zachováno bylo již nainstalované
pořadí zpětné vazby, navazující otázky a zápisu checkpointu.

Úložiště podporuje `unassessed` a append-only opravy přes `correction_of`.
Oprava zachovává zadání, odpověď, lekci i téma a uplatní se na původním místě
aktivity. Historie označuje nahrazené záznamy; `resume` rozlišuje poslední
účinnou aktivitu a poslední opravu. Nástroj neodvozuje věcnou správnost
definice z textu — tu musí ověřit učitel podle materiálu.

Příkaz `.venv/bin/python -B -m unittest discover -s study-skills/tests -v`
úspěšně dokončil **54 testů**, z toho 14 nových pro toto rozšíření. Testy
pracují výhradně v dočasných adresářích. Nové scénáře ověřují:

- Opravu neúspěchu připsaného kvůli cizí konvenci s doloženou citací,
  zachování originálu a odstranění neoprávněně připsané obtíže.
- Oddělení dvou předmětů s odlišným významem F a nezměněný stav druhého kurzu.
- Uchování nejisté odpovědi při dostupnosti pouhé osnovy bez změny znalostí
  nebo opakování; zákaz připsání chybných představ přes `unassessed`.
- Zrušení vadného hodnocení nebo výkladu a obnovení předchozích podkladů.
- Opravu starší aktivity bez přepsání pozdějšího pokusu, jeho obtíží a termínu.
- Řetězení oprav, idempotenci, označení nahrazených zápisů i přes hranice
  stránkování a nezvýšení počtu původních aktivit.
- Odmítnutí neplatných, cizích a již nahrazených cílů, změny původního zadání
  nebo odpovědi, neplatné citace a zachování stavu při přerušeném zápisu.
- Obnovení opraveného výsledku a označené historie v novém procesu CLI.

Tyto testy ověřují chování úložiště, nikoli automaticky úsudek jazykového
modelu. Pro následné ověření výukového chování použij skutečné materiály
s odlišnými konvencemi F, souhrn bez definice a námitku studenta proti
chybnému kritériu. Sleduj, zda učitel před hodnocením dohledá definici,
přizná nejistotu a opraví dotčené záznamy namísto dalšího napovídání.

## Instalace

Vytvořené skilly: `study-progress`, `study-library`, `study-tutor`.
Pracovní verze jsou v tomto adresáři; nainstalované kopie v
`/home/grogy/.codex/skills/`. Nainstalované soubory odpovídají pracovním verzím
podle SHA-256 a všechny relativní odkazy mezi skilly a jejich referencemi existují.

Lokální `codex debug prompt-input` úspěšně objevil všechny tři názvy skillů.
Ověřeno na `codex-cli 0.162.0-alpha.17.2`; příkaz neprováděl výuku ani modelový požadavek.
Současná konverzace může k automatickému výběru potřebovat nové načtení seznamu skillů.

## Automatické testy

V kořeni projektu spusť:

```bash
.venv/bin/python -B -m unittest discover -s study-skills/tests -v
```

Výsledek původního ověření po změně na přímé převzetí materiálů a doplnění IPYNB a PPT: **40 testů prošlo** (Python 3.12.3). Aktuální ověření je uvedeno výše.
Validátor `skill-creator/scripts/quick_validate.py` také úspěšně ověřil každý ze tří skillů.

Testy pracují pouze v dočasných adresářích a ověřují:

- Oddělení dvou předmětů i při shodných ID témat, zdrojů a checkpointů.
- Obnovení posledního kroku v novém procesu a výběr splatného opakování.
- Rozlišení výkladu, výsledku s nápovědou a samostatně doloženého úspěchu.
- Návrat k procvičování po neúspěšném opakování se zachováním historie.
- Idempotentní opakování zápisu a odmítnutí konfliktního přepisu výsledku.
- Odmítnutí neúplných nebo neplatných výsledků bez změny předchozího stavu.
- Ověření citace vůči předmětu, tématu, zdroji a existujícímu locatoru.
- Dohledání textu a zachování původního číslování řádků, snímků PPTX a odstavců DOCX.
- Indexaci buněk notebooku IPYNB bez spouštění kódu, zachování jejich pořadí a typu, citace `cell:N`, vynechání uložených výstupů a odmítnutí neplatných notebooků.
- Převod starších PPT přes LibreOffice, zachování čísel snímků včetně prázdných, odstranění dočasných převodů a rozpoznání chybějícího nebo neúspěšného převodníku.
- Zachování staré verze zdroje a citace po přidání nové verze.
- Přesun dodaného materiálu pod původním názvem, zachování obsahu a odstranění vstupního umístění.
- Nezávislost převzatého materiálu na později znovu vytvořené vstupní cestě a detekci poškození materiálu.
- Vrácení originálu i přepisu při selhání zápisu katalogu nebo přesunu druhého souboru.
- Úklid částečného cílového souboru při selhání přesunu, ochranu před přepsáním cíle a před odebráním materiálu jinému předmětu.
- Evidenci nečitelných souborů a použití přepisu s pravdivými locatory.
- Odmítnutí neplatných ID, neznámého předmětu, aliased adresářů a neznámé verze schématu.
- Zachování původního stavu při simulovaném přerušení atomického zápisu.
- Dvanáct souběžných zápisů ze čtyř procesů bez ztráty aktualizace.
- Stránkování historie, rozhraní CLI a zachování sdíleného profilu.

## Skutečný import starších PPT do DZDB

Pět dodaných originálů PPT bylo převzato přesunem a ověřeno shodným SHA-256 i
zachováním původních souborů po přesunu. Místní LibreOffice Impress 24.2.7.2
provedl dočasný převod do PPTX. Prezentace mají postupně 59, 31, 27, 32 a 28
snímků, celkem 177; všechny mají textový index a ověřené locatory `slide:N`.
Pro každou prezentaci proběhlo úspěšné tematické vyhledání. Stavy ostatních
předmětů zůstaly beze změny. V knihovně jsou původní PPT, nikoli trvalé pracovní
kopie PPTX. Věrnost grafiky, tabulek a vzorců nebyla tímto textovým ověřením potvrzena.

## Původní nezávislý test spolupráce skillů

Tato část zachycuje test původní verze před změnou importu z kopírování na přesun.
Aktuální převzetí materiálů a návrat při chybě ověřuje automatická sada výše.

Samostatný hodnoticí agent bez historie této konverzace přečetl skilly a provedl
čtyři scénáře v izolovaném dočasném adresáři pod `/tmp`. V hlavním úspěšném běhu
provedl 38 příkazů CLI a samostatně zopakoval sadu 27 automatických testů.
Zdrojové soubory skillů během testu nezměnil.

1. **Zahájení výuky:** založil testovací lineární algebru s cílem řešit soustavy,
   přidal poznámky, dohledal pasáž a uložil uskutečněný výklad jako `introduced`.
   Další krok předal jako otázku k samostatnému řešení.
2. **Navázání mezi dvěma předměty:** při nejednoznačném „pokračuj v učení“ položil
   otázku na předmět. Po výslovně označené testovací volbě načetl odpovídající
   `next_step` a zachoval oddělení obou předmětů.
3. **Výsledek se dvěma nápovědami:** samotné prohlášení o úspěchu neuložil jako
   ověřenou znalost. Po doplnění explicitní testovací odpovědi zapsal skutečný
   obsah aktivity, `passed` a `hints_used: 2`; téma zůstalo `practicing`.
4. **Nová verze zdroje:** aktualizoval vstupní materiál a přidal ho pod novým ID.
   Dřívější checkpoint nadále odkazoval na původní `line:4` a její původní obsah.

Navíc ověřil oddělení shodných lokálních ID, idempotenci zápisu, odmítnutí
konfliktního retry a neexistující citace. Ve skillech nezjistil funkční závadu.
Jde o simulované výukové situace s označenými testovacími odpověďmi, nikoli o
vyhodnocení skutečných znalostí uživatele. Body vyžadující jeho odpověď hodnotitel
posuzoval podle instrukcí; neproběhla skutečná vícedenní výuka ani nové uživatelské chaty.

## Praktické použití a limity

Vstupní bod je `$study-tutor`, například:

```text
$study-tutor Chci se učit předmět XTILO z materiálů, které ti určím.
```

Skilly se nejprve domluví na cíli, rozsahu a materiálech. V tomto projektu je
výchozí datové úložiště `/home/grogy/osu_repository/studium/`. Instalace nevytvořila
skutečné předměty ani uživateli nepřipsala testovací znalosti. Jiný chat potřebuje
přístup ke stejnému úložišti. Pro jiné projekty lze určit společnou absolutní cestu.

Sada ověřuje rozpoznání chybějícího PDF backendu a cestu s UTF-8 přepisem.
Projektové virtuální prostředí nyní obsahuje `pypdf`; při skutečném importu APAI
bylo ověřeno načtení 24 textových stran. V extrahovaném textu byly na sedmi stranách
zjištěny nečitelné znaky, takže věrnost matematického zápisu není potvrzená.
Převzatý PDF originál zůstává referencí a příslušné stránky je třeba kontrolovat
vizuálně. Skenované dokumenty potřebují OCR nebo čitelný přepis. Uložené termíny opakování se zobrazují
při návratu do výuky a neposílají automatické notifikace.

Automatické testy ověřují funkčnost úložiště a jeho pravidla. Neměří dlouhodobou
účinnost výuky ani nezaručují automatický výběr správného skillu pro každou formulaci.
