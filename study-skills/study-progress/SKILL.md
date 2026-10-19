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
5. Při opakování stejného zápisu zachovej `checkpoint_id`; shodný zápis je idempotentní, odlišný obsah pod stejným ID je chyba. Při opravě hodnocení vytvoř nový záznam s vysvětlením opravy.
6. Ukládej po vyhodnocených cvičeních i dokončených výkladech. Konec lekce není jediný okamžik zápisu. V případě chyby zápisu ji uveď a netvrď, že je postup uložený.

## Interpretace výsledků

- `introduced`: látka byla představena, zvládnutí nebylo ověřeno.
- `needs-practice`: pokus ukázal potřebu dalšího procvičení.
- `passed`: odpověď splnila uvedené kritérium. S nápovědou se téma vede jako `practicing`; bez nápovědy jako `demonstrated`.
- `demonstrated` znamená doložený úspěch v zaznamenané aktivitě. Zohledni obtížnost, šíři cíle a pozdější opakování; jeden lehký příklad nepotvrzuje zvládnutí celého předmětu.
- Vysvětlení asistenta, přečtený text ani uživatelovo „rozumím“ samy o sobě nejsou úspěšným testem.

Při předání učiteli vrať pouze vybraný předmět: cíle, relevantní stav témat, poslední checkpoint, otevřené obtíže a naplánované opakování. Načtení stavu neopravňuje ke změně materiálů ani výsledků.
