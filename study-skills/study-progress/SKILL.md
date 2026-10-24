---
name: study-progress
description: Ukládej, obnovuj a zobrazuj studijní postup odděleně podle předmětů. Použij při navázání na výuku, záznamu výsledku cvičení nebo dotazu na znalosti a opakování. Samotnou výuku vede study-tutor a materiály spravuje study-library.
---

# Studijní paměť

Udržuj doložitelný stav učení, aby další lekce mohla navázat i v novém chatu.

Před první operací přečti [společný protokol](references/protocol.md).
Pro příkazy a formát vstupů použij [rozhraní úložiště](references/storage.md).
Úložiště obsluhuje `scripts/study_store.py`; cesta ke skriptu je relativní k tomuto skillu.

## Postup

1. Urči absolutní cestu ke studijnímu úložišti a konkrétní `subject_id` podle protokolu. Při nejasném předmětu polož jednu krátkou otázku. Nevytvářej předmět pouze podle názvu složky projektu.
2. Pro navázání načti `resume`. Pro přehled použij `status`. Neodvozuj znalosti z paměti chatu, když existují uložené výsledky.
3. Nový předmět založ pomocí `init` s názvem a alespoň jedním cílem. Chybějící informace zjisti od uživatele; nezačínej se smyšlenými předměty či výsledky.
4. Z výuky převezmi výsledek konkrétní aktivity: zadání, skutečnou odpověď, vyhodnocení, míru nápovědy, chyby, použité zdroje a další krok. Zapiš ho přes `checkpoint` ještě před další výukovou aktivitou. Při samotném výkladu může být odpověď prázdná a výsledek musí být `introduced`.
5. Při opakování stejného zápisu zachovej `checkpoint_id`; shodný zápis je idempotentní, odlišný obsah pod stejným ID je chyba. Při opravě vytvoř nový záznam s `correction_of` odkazujícím na účinný checkpoint téže aktivity a v `evaluation` uveď důvod i ověřený podklad. Zachovej původní `lesson_id`, `topic_id`, `activity` a skutečnou `learner_answer`; oprava není nový pokus. Projdi související hodnocení, neoprávněně připsané obtíže i další kroky a oprav každý dotčený záznam zvlášť. Původní historii nemaž; pro interpretaci používej `is_effective` z `history` a aktuální stav z `resume`.
6. Ukládej po vyhodnocených cvičeních i dokončených výkladech. Konec lekce není jediný okamžik zápisu. V případě chyby zápisu ji uveď a netvrď, že je postup uložený.

## Interpretace výsledků

- `introduced`: látka byla představena, zvládnutí nebylo ověřeno.
- `unassessed`: hodnocení není uzavřeno, například kvůli neověřené konvenci nebo zrušenému kritériu. Nedokládá chybu, zvládnutí ani výklad a nemění stav znalostí či termín opakování. Důvod a ověření zaznamenej do `evaluation` a `next_step`; nevymýšlej odpověď a nepřipisuj `misconceptions`.
- `needs-practice`: pokus ukázal potřebu dalšího procvičení.
- `passed`: odpověď splnila uvedené kritérium. S nápovědou se téma vede jako `practicing`; bez nápovědy jako `demonstrated`.
- `demonstrated` znamená doložený úspěch v zaznamenané aktivitě. Zohledni obtížnost, šíři cíle a pozdější opakování; jeden lehký příklad nepotvrzuje zvládnutí celého předmětu.
- Vysvětlení asistenta, přečtený text ani uživatelovo „rozumím“ samy o sobě nejsou úspěšným testem.
- Nejistota učitele ani použití jiné možné konvence nejsou samy o sobě `needs-practice`. Před přijetím negativního hodnocení musí být doložené kritérium pro danou aktivitu. Při chybě učitele lze původní výsledek opravit na `passed`, `needs-practice`, `introduced` nebo `unassessed` podle skutečných podkladů; pouhé nové vysvětlení chybný záznam neopraví.

Při předání učiteli vrať pouze vybraný předmět: cíle, relevantní stav témat, poslední checkpoint, otevřené obtíže a naplánované opakování. Načtení stavu neopravňuje ke změně materiálů ani výsledků.
