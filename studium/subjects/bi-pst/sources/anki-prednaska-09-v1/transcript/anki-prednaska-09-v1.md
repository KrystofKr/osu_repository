# BI-PST – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-pst/BI-PST.apkg; APKG SHA-256 1b0cea15a4362f71d40f74130e70b25176d8b28f02d0546ab2b515682157fa11. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: f340f7d8957f2d6990d7a07f7c5b81fd8545ba30cdcc33d3db6bbdc37238df22.
Původní balíčky: BI-PST
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1700648566061

Karty Anki: 1700648566061
GUID: KR-HqLVa^S; štítky: bi-pst::p09 bi-spol::26 bi-spol::27.

### Otázka (Front)

Definujte náhodný výběr.

### Odpověď (Back)

Náhodným výběrem z rozdělení \(F\) nazveme \(n\)-tici i.i.d. náhodných veličin \(X_1, \dots, X_n\) s distribuční funkcí \(F\).

## Poznámka Anki 1700649791320

Karty Anki: 1700649791320
GUID: Q&Tj6ghsa:; štítky: bi-pst::p09 bi-spol::27.

### Otázka (Front)

Definujte bodový odhad.

### Odpověď (Back)

Bodový odhad parametru \(\theta\) je funkce \(\hat \theta_n(X_1, \dots X_n)\) náhodného výběru, která nezávisí na hodnotách \(\theta\).

## Poznámka Anki 1700649906265

Karty Anki: 1700649906266
GUID: Ap*F0k|dFk; štítky: bi-pst::p09 bi-spol::27.

Metadata původního zdroje pro kartu 1700649906266: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte nestranný (nevychýlený) odhad.

### Odpověď (Back)

Odhad \(\hat \theta_n\) parametru \(\theta\) nazveme nestranný (nevychýlený), jestliže pro všechna \(\theta \in \Theta\) platí\[\operatorname E \hat \theta_n = \theta.\]

## Poznámka Anki 1700649996154

Karty Anki: 1700649996154
GUID: F%LuFIEl</; štítky: bi-pst::p09 bi-spol::27.

Metadata původního zdroje pro kartu 1700649996154: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte konzistentní odhad.

### Odpověď (Back)

Odhad \(\hat \theta_n\) parametru \(\theta\) se nazývá konzistentní, jestliže pro každé \(\theta \in \Theta\) platí\[\hat \theta_n \xrightarrow{\operatorname P} \theta \quad \text{pro} \quad n \to +\infty.\]To znamená, že pro každé \(\varepsilon > 0\) a \(\theta \in \Theta\) platí\[\displaystyle \lim_{n \to +\infty} \operatorname P(|\hat \theta_n(X_1, \dots, X_n) - \theta| \geq \varepsilon) = 0.\]

## Poznámka Anki 1700651340841

Karty Anki: 1700651340842
GUID: ys=/X77k0k; štítky: bi-pst::p09 bi-spol::27.

Metadata původního zdroje pro kartu 1700651340842: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Definujte nejlepší nestranný odhad.

### Odpověď (Back)

Odhad \(\hat \theta_n^*(X_1, \dots, X_n)\) se nazývá nejlepší nestranný odhad parametru \(\theta\), pokud je nestranný a pro každý jiný nestranný odhad \(\hat \theta_n\) platí, že pro všechna \(\theta \in \Theta\)\[\operatorname{var}(\hat \theta_n) \geq \operatorname{var}(\hat \theta_n^*).\]

## Poznámka Anki 1700692788126

Karty Anki: 1700692788126
GUID: tK~C~Uos*f; štítky: bi-pst::p09 bi-spol::27.

### Otázka (Front)

Popište metodu momentů.

### Odpověď (Back)

Metoda momentů se používá k odhadu parametrů rozdělení. Mějme náhodný výběr \(X_1, \dots, X_n\) z rozdělení určeného \(d\)-rozměrným parametrem \(\theta = (\theta_1, \dots, \theta_d)\). Potom je postup metody momentů následující:

- napočteme teoretické momenty \(\operatorname E X_i^k, \quad k = 1, \dots, d\);
- vyjádříme parametry jako funkce momentů;
- odhadneme teoretické momenty pomocí jejich výběrových verzí:

\[\widehat{\operatorname E X_i^k} = \frac 1 n \displaystyle \sum_{i = 1}^n X_i^k\]

- dosadíme odhadnuté momenty do vztahů mezi parametry a teoretickými momenty;
- vyřešíme soustavu rovnic a získáme tak odhady parametrů rozdělení.

## Poznámka Anki 1700693193168

Karty Anki: 1700693193168
GUID: P#UrZz,e5O; štítky: bi-pst::p09 bi-spol::27.

### Otázka (Front)

Definujte věrohodnostní funkci.

### Odpověď (Back)

Uvažujme náhodný výběr \(X_1, \dots, X_n\) se sdruženou hustotou, resp. pravděpodobností
\[\begin{matrix}
f_\theta = \displaystyle \prod_{i = 1}^n f_\theta(x_i), \\
p_\theta = \displaystyle \prod_{i = 1}^n \operatorname P_\theta (X_i = x_i)
\end{matrix}\]pro spojité, resp. diskrétní rozdělení. Při pevných pozorovaných hodnotách \(\mathbf x = (x_1, \dots, x_n) \) se \(f_\theta(\mathbf x)\), resp. \(p_\theta(\mathbf x)\) jakožto funkce \(\theta\) nazývá věrohodnostní funkcí a značí se \(L(\theta; \mathbf x)\), případně pouze \(L(\theta)\).

## Poznámka Anki 1700693608606

Karty Anki: 1700693608607
GUID: K0pl|Baz&S; štítky: bi-pst::p09 bi-spol::27.

### Otázka (Front)

Popište metodu maximální věrohodnosti a definujte maximálně věrohodný odhad.

### Odpověď (Back)

**Metoda maximální věrohodnosti** se používá k odhadu parametrů rozdělení, čehož dosahuje maximalizací věrohodnostní funkce. Hodnota \(\hat \theta_n\) parametru \(\theta\), která maximalizuje věrohodnostní funkci \(L(\theta; \mathbf x)\) pro dané \(\mathbf X = \mathbf x\) se nazývá **maximálně věrohodný odhad **(MLE) parametru \(\theta\). To znamená, že pro všechna \(\theta \in \Theta\) platí
\[L(\hat \theta_n; \mathbf x) \geq L(\theta; \mathbf x).\]

## Poznámka Anki 1701096439082

Karty Anki: 1701096439082
GUID: As/H]2`b~9; štítky: bi-pst::p09 bi-spol::27.

### Otázka (Front)

Popište výběrový průměr.

### Odpověď (Back)

Výběrový průměr se používá jako bodový odhad střední hodnoty \(\operatorname E X\). Spočíst lze pomocí následujícího vzorce:\[\bar X_n = \frac 1 n \displaystyle \sum_{i = 1}^n X_i.\]

## Poznámka Anki 1701096519605

Karty Anki: 1701096519605
GUID: b#$BP>*zKi; štítky: bi-pst::p09 bi-spol::27.

### Otázka (Front)

Popište výběrový rozptyl.

### Odpověď (Back)

Výběrový rozptyl se používá jako bodový odhad rozptylu \(\operatorname{var} X\). Spočíst lze pomocí následujícího vzorce:\[s_n^2 = s_X^2 = \frac 1 {n - 1} \displaystyle \sum_{i = 1}^n(X_i - \bar X_n)^2 = \frac 1 {n - 1} \Big( \displaystyle \sum_{i = 1}^n X_i^2 - n\bar X_n^2 \Big).\]

## Poznámka Anki 1701096641950

Karty Anki: 1701096641951
GUID: K#3N!Z%$*u; štítky: bi-pst::p09 bi-spol::27.

### Otázka (Front)

Popište \(k\)-tý výběrový moment.

### Odpověď (Back)

Jako bodový odhad \(k\)-tého momentu \(\mu_k = \operatorname E X^k\) můžeme použít \(k\)-tý výběrový moment. Spočíst lze pomocí následujícího vzorce:
\[m_k = \frac 1 n \displaystyle \sum_{i = 1}^n X_i^k.\]

## Poznámka Anki 1701096813492

Karty Anki: 1701096813492
GUID: fN)9tpgJK_; štítky: bi-pst::p09 bi-spol::27.

### Otázka (Front)

Vyslovte větu o konzistenci odhadu.

### Odpověď (Back)

Nechť \(\operatorname E \hat \theta_n^2 < +\infty\) pro každé \(n\). Pokud pro \(n \to +\infty\) platí
\[\begin{matrix}
\operatorname E \hat \theta_n \to \theta, \\
\operatorname{var} \hat \theta_n \to 0,
\end{matrix}\]pak je \(\hat \theta_n\) konzistentní.

