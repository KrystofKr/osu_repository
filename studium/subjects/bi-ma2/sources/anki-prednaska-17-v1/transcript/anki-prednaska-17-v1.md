# BI-MA2 – Přednáška 17

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1671457373047

Karty Anki: 1671457373047
GUID: K!aFxMnNZ[; štítky: bi-ma2::p17.

### Otázka (Front)

Popište úlohu, kterou řeší spádová metoda.

### Odpověď (Back)

Minimalizuj \(f(\mathbf x)\), kde

- \(f: \mathbb R^n \to \mathbb R\) a \(x\) probíhá všechny možné hodnoty \(\mathbf x \in D_f\),

- definiční obor \(D_f\) je otevřená množina,
- funkce \(f\) je minimálné dvakrát spojitě diferencovatelná.

## Poznámka Anki 1671457582360

Karty Anki: 1671457582360
GUID: /`Dw^X>.5; štítky: bi-ma2::p17.

### Otázka (Front)

Popište jeden krok spádové metody.

### Odpověď (Back)

Nechť je dáno \(\mathbf x \in D_f\).

1. Urči směr \(\Delta \mathbf x\).
2. Zvol velikost kroku \(t > 0\).
3. Napočti \(\mathbf x + t \Delta \mathbf x\) a ulož ho do \(\mathbf x\).

Tento postup opakuj dokud není splněno kriérium pro zastavení iterační smyčky. Praktické kritérium pro zastavení může být například dostatečná nulovost gradientu. Je také vhodné kontrolovat maximální počet iterací.

## Poznámka Anki 1671457954756

Karty Anki: 1671457954756
GUID: mR=1m,Em;C; štítky: bi-ma2::p17.

### Otázka (Front)

Popište obecný postup volby směru kroku spádové metody.

### Odpověď (Back)

Pro \(t\) blízká nule přibližně platí (s použitím Taylorovy věty), že
\[f(\mathbf x + t \Delta \mathbf x) \approx f(\mathbf x) + t \nabla f(\mathbf x) \cdot \Delta \mathbf x.\]Pokud chceme být schopni i malým krokem funkční hodnotu zmenšit, musíme směr kroku, tj. \(\Delta \mathbf x\), vždy volit tak, aby
\[\nabla f(\mathbf x) \cdot \Delta \mathbf x < 0.\]

## Poznámka Anki 1671458487044

Karty Anki: 1671458487044
GUID: B|x%a:Mg&m; štítky: bi-ma2::p17.

### Otázka (Front)

Popište volbu škálovacího faktoru \(t\) pomocí zpětného krokování ve spádové metodě.

### Odpověď (Back)

Nechť máme bod \(\mathbf x\) a již jsme zvolili směr \(\Delta \mathbf x\). Ideálně bychom chtěli \(t > 0\) zvolit tak, aby v tomto bodě \(t\) bylo nabyto minimum funkce jedné proměnné \(s > 0,\)
\[s \mapsto f(\mathbf x + s \Delta \mathbf x).\]Zpětné krokování probíhá následovně:

- Jsou dány \(f\), směr \(\Delta \mathbf x\), bod \(x \in D_f\) a parametry \(\alpha \in (0, \frac 1 2)\), \(\beta \in (0,1)\).
- Polož \(t := 1.\) Dokud \(f( \mathbf x + t \Delta \mathbf x) > f(\mathbf x) + \alpha t \nabla f(\mathbf x) \cdot \Delta \mathbf x\) změň \(t\) na \(\beta t\).
- Vrať \(t\).

Parametr \(\alpha\) kontroluje, jaký pokles jsme ochotní akceptovat. Parametr \(\beta \) pak udává, jak rychle zmenšujeme prvotní \(t\) (proto zpětné krokování).

## Poznámka Anki 1671459146445

Karty Anki: 1671459146445
GUID: HmG&KnP)>3; štítky: bi-ma2::p17.

### Otázka (Front)

Popište volbu směru ve spádové metodě.

### Odpověď (Back)

Předpokládejme, že jsme v bodě \(\mathbf x\) a vydáme se malým krokem směrem \(\mathbf s\). Potom lineární aproximace změny funkční hodnoty je
\[f(\mathbf x + \mathbf s) \approx f(\mathbf x) + \nabla f(\mathbf x) \cdot \mathbf s.\]Směry, ve kterých dojde k poklesu funkční hodnoty, splňují \(\nabla f(\mathbf x) \cdot \mathbf s < 0\). Zvolme normu \(\| \cdot \|\) na \(\mathbb R^n\). Směr nejprudšího poklesu je pak dán řešením úlohy
\[\Delta \mathbf x = \operatorname{argmin} \set{\nabla f(\mathbf x) \cdot \mathbf s \, \mid \, \| \mathbf s \| \leq 1}.\]Pro reálnou symetrickou PD matici \(\mathbf P \in \mathbb R^{n,n}\) můžeme definovat normu (pro Euklidovskou máme \(\mathbf P = \mathbf E)\)
\[\| s \|_\mathbf P := \sqrt{\mathbf s^T \mathbf P \mathbf s}, \quad s\in \mathbb R^n.\]Směr největšího poklesu vzhledem k této normě je pak dán vektorem
\[\Delta \mathbf x = - \mathbf P^{-1} \nabla f(\mathbf x)^T.\]

## Poznámka Anki 1671460748040

Karty Anki: 1671460748040
GUID: QSh<+}VKL~; štítky: bi-ma2::p17.

### Otázka (Front)

Popište gradientovou metodu (gradientní sestup). Jaké jsou jeho výhody a nevýhody?

### Odpověď (Back)

Očividným kandidátem pro volbu směru kroku při minimalizaci je krok ve směru záporně vzatého gradientu (je-li nenulový), tj. volíme \(\mathbf P = \mathbf E\),
\[\Delta \mathbf x := -\nabla f(\mathbf x).\]Potom skutečně
\[\nabla f(\mathbf x) \cdot \Delta\mathbf x = -|| \Delta \mathbf x ||^2 < 0.\]Výhodou je, že gradient je snadno spočítatelný. Výsledný směr nemusí být nejvhodnější a není využita informace obsažená ve vyšších derivacích.

 [Obrázek: paste-80c3acb503a7557784dad7d30fca77dbb81af34a.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1671461554266

Karty Anki: 1671461554266
GUID: oqIo6H*r8; štítky: bi-ma2::p17.

### Otázka (Front)

Popište Newtonovu metodu jakožto typ spádové metody.

### Odpověď (Back)

Newtonova metoda volí směr v bodě \(\mathbf x\) vzhledem k Hessově matici \(\mathbf P = \nabla^2 f(\mathbf x)\), tedy
\[s_- = - \frac{\mathbf P^{-1} \mathbf c}{||\mathbf (P^{\frac 1 2})^{-1} \mathbf c ||},\]kde \(\mathbf c = \nabla f(\mathbf x)\). Tj. bez pro nás nepodstatného normalizačního faktoru dostáváme
\[\Delta \mathbf x = -\big(\nabla ^2 f(\mathbf x)\big)^{-1} \cdot \nabla f(\mathbf x)^T.\]

 [Obrázek: paste-57b3a5c78e3763f9c4f2e987d83e28c3449f7218.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1671491393720

Karty Anki: 1671491393720
GUID: Q-D:WTyQPR; štítky: bi-ma2::p17.

### Otázka (Front)

Popište princip spádové metody.

### Odpověď (Back)

V každé iteraci se snažíme snížit hodnotu minimalizované funkce \(f\).

Nechť je tedy dáno \(\mathbf x^{(1)} \in D_f\). Sestavíme posloupnost vektorů \(\mathbf x^{(k)}\), \(k = 1,2, \dots\), podle rekurentního předpisu

\[\mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} + t^{(k)} \Delta \mathbf x^{(k)},\]kde \(\Delta \mathbf x^{(k)}\) je vhodně zvolený vektor (**směr poklesu**) a \(t^{(k)}\) **délka** **kroku**.

Následující člen musí být zvolen tak, aby \(f(\mathbf{x}^{(k+1)}) < f(\mathbf{x}^{(k)})\), samozřejmě vyjma případu, kdy \(\mathbf{x}^{(k)}\) je již optimální (je bodem lokálního minima).

### Doplňující pole (Extra)

\(\mathbf x^{(k)}\) v tomto kontextu označuje **index** vektoru ve vektorové posloupnosti, kterou konstruujeme.

