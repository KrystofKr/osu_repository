# BI-HWB – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-hwb/BI-HWB.apkg; APKG SHA-256 0303626d2408f7eee1801e17ecb475633a60c42f914f37290ffd8c479013ce2b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b861d2e855c5070244800c22d62092a09b22aee0ded024030525b06a7d18285e.
Původní balíčky: BI-HWB
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1699888858478

Karty Anki: 1699888858478
GUID: n#^_,jdJkl; štítky: bi-hwb::p08.

### Otázka (Front)

Popište trusted (důvěřovaný) a trustworthy (důvěryhodný) systém.

### Odpověď (Back)

Systém je považovaný za trusted (důvěřovaný), jestliže jeho selhání může způsobit porušení bezpečnostních zásad, zatímco trustworthy (důvěryhodný) systém je systém, který neselže.

## Poznámka Anki 1699889335392

Karty Anki: 1699889335392
GUID: m@xHgg>)-C; štítky: bi-hwb::p08.

### Otázka (Front)

Popište root of trust (kořen důvěry).

### Odpověď (Back)

Root of trust (kořen důvěry) je komponenta realizující bezpečnostní funkci, na kterou systém spoléhá, ale jejíž důvěryhodnost buď nemůže být explicitně ověřena nebo je ověřena na nižší úrovni abstrakce. Root of trust tvoří první část chain of trust (řetězce důvěry).

## Poznámka Anki 1699889895025

Karty Anki: 1699889895025
GUID: GS6>|+c%~2; štítky: bi-hwb::p08.

### Otázka (Front)

Popište physical unclonable function (PUF).

### Odpověď (Back)

Physical unclonable function je fyzické zařízení, které na vstup daný fyzikálním stavem systému a výzvou (challenge) vyprodukuje odpověď v podobě unikátního řetězce (otisku). Kvalitně realizovaná PUF by měla fungovat jako jednosměrná funkce, přičemž jednosměrnost je obvykle garantována právě unikátním fyzikálním stavem systému, kterého je dosaženo vlivem náhodných a nekontrolovatelných jevů při výrobním procesu.

## Poznámka Anki 1699890660334

Karty Anki: 1699890660334
GUID: eICzN=I6n; štítky: bi-hwb::p08.

### Otázka (Front)

Popište vlastnosti physical unclonable function (PUF).

### Odpověď (Back)

Physical unclonable function (PUF) by měla mít následující vlastnosti:

- **snadná vyhodnotitelnost **- vysoká rychlost, malá zabraná plocha, nízká spotřeba;

- **reprodukovatelnost** - rozdíly v odpovědích na stejné výzvy by měly být dostatečné malé;

- **jedinečnost** - odpovědi dvou PUF na stejnou výzvu by měly být maximálně odlišné;

- **nepředvídatelnost **- pokud jsou známé odpovědi na posloupnost \(n\) výzev, nemělo by být možné předpovědět odpověď na \(n+1\). výzvu;

- **jednosměrnost **- nemělo by být možné pro danou odpověď nalézt odpovídající výzvu ani výzvu, která by generovala podobnou odpověď;

- **tamper evidence **- nemělo by být možné fyzicky změnit PUF bez pozorovatelné změny v jejím chování;

- **neklonovatelnost** - fyzická (nemělo by být možné vyrobit dvě PUF se stejnými vlastnostmi) a matematická (prostor párů výzev a odpovědí by měl být dostatečně velký).

## Poznámka Anki 1699890914520

Karty Anki: 1699890914520
GUID: Q?WEi$8;;7; štítky: bi-hwb::p08.

### Otázka (Front)

Provnejte physical unclonable function (PUF) a generátor skutečně náhodných čísel (TRNG).

### Odpověď (Back)

Physical unclonable function (PUF) i generátor skutečně náhodných čísel (TRNG) mohou mít stejný základ realizace, ale TRNG využívá kontinuální náhodný fyzikální proces, kdežto PUF používá náhodný proces, který proběhl pouze jedenkrát při výrobě.

## Poznámka Anki 1699891115927

Karty Anki: 1699891115927
GUID: FU%?e,DUH!; štítky: bi-hwb::p08.

### Otázka (Front)

Popište klasifikaci physical unclonable function (PUF).

### Odpověď (Back)

Physical unclonable function (PUF) můžeme dělit dle následujících kritérií:

- elektronické a neelektronické PUF,
- intrinsické a neintrinsické PUF,
- silné a slabé PUF.

## Poznámka Anki 1699891159670

Karty Anki: 1699891159670
GUID: o9)$UlK6Tg; štítky: bi-hwb::p08.

### Otázka (Front)

Popište intrinsickou physical unclonable function (PUF).

### Odpověď (Back)

Intrinsická physical unclonable function (PUF) je taková PUF, u které je PUF i měřící a vyhodnocovací vybavení součástí jednoho čipu.

## Poznámka Anki 1699892840353

Karty Anki: 1699892840353
GUID: HM`2zU`m8_; štítky: bi-hwb::p08.

### Otázka (Front)

Popište metriky vyhodnocení physical unclonable function (PUF).

### Odpověď (Back)

Používají se následující metriky vyhodnocení physical unclonable function (PUF):

- **intra-hammingova vzdálenost** - označuje reprodukovatelnost výstupu PUF,

- **inter-hammingova vzdálenost **- označuje jedinečnost výstupu PUF,

- **náhodnost** - odhaduje entropii PUF.

## Poznámka Anki 1699915823601

Karty Anki: 1699915823601
GUID: f4!+X</^mM; štítky: bi-hwb::p08.

### Otázka (Front)

Popište využití physical unclonable function (PUF).

### Odpověď (Back)

Physical unclonable function (PUF) můžeme využít v následujících scénářích:

- **identifikace** - vyžaduje reprodukovatelnost a jedinečnost;

- **autentizace **- vyžaduje reprodukovatelnost, jedinečnost a nepředvídatelnost a každý pár výzva-odpověď lze použít nejvýše jednou;
- **generování klíčů** - vyžadovalo by perfektní reprodukovatelnost, kterou PUF nemá, proto se používají samoopravné kódy.

## Poznámka Anki 1699916844009

Karty Anki: 1699916844009
GUID: zZxnZrrRac; štítky: bi-hwb::p08 bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Popište využití SRAM pro physical unclonable functions (PUF) a generátory skutečně náhodných čísel (TRNG).

### Odpověď (Back)

Po spuštení napájení mají některé buňky SRAM paměti preferenci k logické \(0\) nebo \(1\), případně nemají preferenci žádnou a chovají se náhodně. Toho lze využít při implementaci physical unclonable function (PUF) a generátorů skutečně náhodných čísel (TRNG).

## Poznámka Anki 1699917165872

Karty Anki: 1699917165872
GUID: IhBQ*u!h4L; štítky: bi-hwb::p08.

### Otázka (Front)

Popište arbiter physical unclonable function (PUF).

### Odpověď (Back)

Arbiter physical unclonable function (PUF) funguje s použitím switch komponent, které na základě řídícího vstupu, kterým bývá jeden bit výzvy, dokáží propojit své vstupy a výstupy různými způsoby. Tím vznikají různé cesty napříč obvodem. Arbitr pak detekuje, na který z jeho vstupů přišel signál dříve a podle této informace produkuje výsledný bit odpovědi.

 [Obrázek: paste-79cd712603afc8d3045dcb8298340d70236283c9.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1699917419957

Karty Anki: 1699917419957
GUID: tM}reu_8sC; štítky: bi-hwb::p08.

### Otázka (Front)

Popište ring oscillator physical unclonable function (ROPUF).

### Odpověď (Back)

Ring oscillator physical unclonable function (ROPUF) používá jako zdroj náhodnosti zpoždení kruhových oscilátorů (lichý počet invertorů zapojený ve smyčce), které je způsobeno náhodnými odchylkami ve zpoždění hradel a jejich propojení.

