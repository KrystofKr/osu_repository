# BI-HWB – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-hwb/BI-HWB.apkg; APKG SHA-256 0303626d2408f7eee1801e17ecb475633a60c42f914f37290ffd8c479013ce2b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b861d2e855c5070244800c22d62092a09b22aee0ded024030525b06a7d18285e.
Původní balíčky: BI-HWB
Rozsah: 17 poznámek, 17 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1700499763177

Karty Anki: 1700499763177
GUID: kGFo2Yj^ez; štítky: bi-hwb::p09.

Metadata původního zdroje pro kartu 1700499763177: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to generátor pseudonáhodných čísel (PRNG)?

### Odpověď (Back)

Generátor pseudonáhodných čísel (PRNG) je deterministrický algoritmus, jehož výstup je posloupnost, která sice ve skutečnosti není náhodná, ale útočníkovi se jako náhodná jeví, pokud mu nejsou známy některé parametry generátoru.

## Poznámka Anki 1700499844671

Karty Anki: 1700499844671
GUID: e2L2ySii[<; štítky: bi-hwb::p09.

Metadata původního zdroje pro kartu 1700499844671: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Jak fungují generátory skutečně náhodných čísel (TRNG)?

### Odpověď (Back)

Generátory skutečně náhodných čísel (TRNG) jsou nedeterministrické a využívají zdroje entropie, kterými jsou zpravidla fyzikální nebo vnější jevy. Příkladem může být:

- radioaktivní rozpad,
- atomosférický šum,
- teplotní šum,
- chování uživatele.

Oproti generátorům pseudonáhodných čísel (PRNG) ale často mívají horší statistické vlastnosti, a proto se u nich používá post-processing.

## Poznámka Anki 1700500409069

Karty Anki: 1700500409069
GUID: QaM}z)ZZ`p; štítky: bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Popište hybridní generátor náhodných čísel (HRNG).

### Odpověď (Back)

Hybridní generátory náhodných čísel (HRNG) jsou často realizovány jako:

- PRNG, který je opakovaně inicializovaný seedem generovaným TRNG,
- TRNG s algoritmickým post-processingem.

Tím je možné kompenzovat horší statistické vlastnosti TRNG. Vždy ale platí, že PRNG nemůže zvýšit entropii, protože ta je určena pouze entropií jeho vstupu.

## Poznámka Anki 1700501068852

Karty Anki: 1700501068853
GUID: Qq:_`1t8r+; štítky: bi-hwb::p09.

Metadata původního zdroje pro kartu 1700501068853: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to post-processing u TRNG? Uveďte příklady.

### Odpověď (Back)

Protože výstupy TRNG mají zpravidla horší statistické vlastnosti, je nutné je dále zpracovávat. Post-processing se provádí zejména za cílem:

- ostranění nevyváženosti jedniček a nul a zajištění rovnoměrného rozdělení,
- zhuštení entropie výstupních bitů za cenu snížení rychlosti jejich generování.

Způsoby, kterými lze zajistit lepší statistické vlastnosti TRNG jsou:

- XOR výstupu TRNG s výstupem kryptograficky silného PRNG,
- XOR výstupů dvou nebo více různých TRNG,
- hashování výstupu TRNG kryptograficky silnou hashovací funkcí,
- použití John von Neumannova dekorelátoru nebo XOR korektoru.

## Poznámka Anki 1700501163605

Karty Anki: 1700501163605
GUID: df{W]cb#Lg; štítky: bi-hwb::p09.

Metadata původního zdroje pro kartu 1700501163605: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Jak lze testovat náhodné generátory? Uveďte příklady.

### Odpověď (Back)

K testování RNG se používají statistické testy, které mohou odhalit nekvalitní generátory. Nedokáží však dokázat, že generátor kvalitní je. Jsou založeny na testování statistických hypotéz. Mezi příklady testů náhodných generátorů patří:

- **frekvenční test** - testuje podíl jedniček a nul;

- **runs test** - testuje, zda počet a délka řetězců po sobě jdoucích stejných bitů odpovídá náhodné posloupnosti;
- **test hodností matic** - testuje na lineární závistlosti podposloupností;

- **spektrální test** - testuje na periodicitu;

- **Mauerův univerzální statistický test** - testuje, zda lze posloupnost bezztrátově komprimovat (výrazně komprimovatelná posloupnost nemá dostatečnou entropii).

## Poznámka Anki 1700501341241

Karty Anki: 1700501341241
GUID: f;X9lx|IJ^; štítky: bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Kdy se provádí testování náhodných generátorů?

### Odpověď (Back)

Testování náhodných generátorů by se mělo provádět:

- **při návrhu** - ověření vlastností, používají se složitější testy;

- **za běhu** - generátor by měl být schopen včas detekovat poruchu, používají se jednodušší testy.

## Poznámka Anki 1700502724449

Karty Anki: 1700502724449
GUID: dFw*YPGvto; štítky: bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Jakým způsobem se testují generátory skutečně náhodných čísel (TRNG)?

### Odpověď (Back)

Pro testování generátorů skutečně náhodných čísel (TRNG) se používá následující postup:

- identifikace zdroje entropie,
- sestavení statistického modelu fyzikálního šumu,
- experimentální vyhodnocení parametrů modelu.

Tím vzniká statistický model TRNG. Krom toho lze na TRNG aplikovat běžné statistické testy. Při testování je vždy potřeba vynechat post-processing.

## Poznámka Anki 1700502876210

Karty Anki: 1700502876210
GUID: QNhiC#6!6P; štítky: bi-hwb::p09.

Metadata původního zdroje pro kartu 1700502876210: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište lineární kongruentní generátor.

### Odpověď (Back)

Jde o jeden z nejstarších a nejznámějších PRNG, který však není kryptograficky bezpečný. Používá vztah
\[X_{n + 1} = a \cdot X_n + c \pmod m,\]kde \(m\) je modul (často mocnina dvou), \(a\) je násobitel, \(c\) je inkrement, \(X_0\) je počáteční hodnota (seed) a 
\((X)_{n = 1}^\infty\) je posloupnost pseudonáhodných čísel. Platí, že posloupnost pseudonáhodných čísel se začne opakovat nevýše po \(m\) iteracích.

## Poznámka Anki 1700503078660

Karty Anki: 1700503078661
GUID: L;bUMK8E=1; štítky: bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Popište slabiny lineárního kongruentního generátoru.

### Odpověď (Back)

Mezi kryptologické slabiny lineárního kongruentního generátoru patří:

- pokud je použito \(m = 2^k\), mají niží bity \(X_i\) kratší periodu než celá sekvence;
- po sobě jdoucí hodnoty jsou korelované;
- parametry generátoru lze odvodit z pár hodnot \(X_i\).

## Poznámka Anki 1700503494422

Karty Anki: 1700503494422
GUID: i=MKP)V1.:; štítky: bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Popište využítí linear-feedback shift register (LFSR) jako generátoru pseudonáhodných čísel (PRNG).

### Odpověď (Back)

K implementaci generátorů pseudonáhodných čísel (PRNG) se obvykle používají konkrétně Fibonacci  LSFR a Galois  LSFR. Nicméně samy o sobě jsou kryptograficky slabé a pro jejich zesílení se používá např. nelineární filtr výstupu, nelineární kombinace výstupů několika LSFR nebo gated clock (jako u A5/1).

## Poznámka Anki 1700503706346

Karty Anki: 1700503706346
GUID: l*VtTFtcAx; štítky: bi-hwb::p09.

Metadata původního zdroje pro kartu 1700503706346: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište vlastnosti kvalitních kryptograficky bepzečných generátorů náhodných a pseudonáhodných čísel.

### Odpověď (Back)

Na kvalitní kryptograficky bepzečné generátory náhodných a pseudonáhodných čísel klademe následující požadavky:

- generovaná čísla musí být nepředvídatelná (odolnost proti next-bit test a state compromise),
- generovaná čísla musí mít rovnoměrné rozdělení,
- generátor musí mít dostatečně dlouhou periodu,
- generátor musí projít statistickými testy.

## Poznámka Anki 1700504070176

Karty Anki: 1700504070176
GUID: wH_1Ujpv?0; štítky: bi-hwb::p09.

Metadata původního zdroje pro kartu 1700504070176: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Uveďte způsoby, kterými lze realizovat PRNG.

### Odpověď (Back)

Kryptograficky bezpečné PRNG lze realizovat následujícími způsoby:

- **bezpečná bloková šifra v režimu CTR** - náhodně se zvolí klíč (seed) a počáteční hodnota čítače \(i\) a pomocí těchto parametrů se šifrují postupně hodnoty \(i, i + 1, \dots\);

- **kryptograficky bezpečná hashovací funkce aplikovaná na čítač** - náhodně se zvolí počáteční hodnota čítače \(i\) a následně hashuje posloupnost \(i, i + 1, \dots\);

- **proudové šifry** - proudová šifra je v zásadě PRNG, jehož výstup se kombinuje s plaintextem;

- **algoritmy založené na teorii čísel** - musí u nich být proveden důkaz bezpečnosti.

## Poznámka Anki 1700504628519

Karty Anki: 1700504628520
GUID: P!Qr8`v~>%; štítky: bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Popište jitter a jeho využití pro generátory skutečně náhodných čísel (TRNG).

### Odpověď (Back)

Jitter popisuje variaci jedné nebo více charakteristik periodického signálu. Pro implementaci generátorů skutečně náhodných čísel (TRNG) se nejčastěji používá hodinový signál. Hrana tohoto signálu totiž nepřichází vždy ve stejný moment, a tak můžeme od jejího předstihu či zpoždění odvozovat náhodné hodnoty.

## Poznámka Anki 1700504871499

Karty Anki: 1700504871499
GUID: cmV+mW_3@L; štítky: bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Popište metastabilitu klopného obvodu a její využití pro generátory skutečně náhodných čísel (TRNG).

### Odpověď (Back)

Klopný obvod požaduje, aby vstupní signál byl po určitou dobu před (setup time) a po (hold time) hodinové hraně stabilní. Pokud jsou tyto požadavky porušeny, může vstoupit do metastabilního stavu, ve kterém chvíli setrvá a poté přejde buď do logické nuly nebo jedničky, což můžeme využít ke generování náhodných hodnot.

## Poznámka Anki 1700505786380

Karty Anki: 1700505786380
GUID: Q.f1MT:j*+; štítky: bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Popište problémy snižující bezpečnost generátoru pseudonáhodných čísel (PRNG).

### Odpověď (Back)

Mezi problémy snižující bezpečnost generátoru pseudonáhodných čísel (PRNG) patří:

- použití slabého PRNG,
- použití krátkého nebo málo náhodného seedu,
- únik vnitřního stavu PRNG (např. pomocí útoku postranním kanálem).

## Poznámka Anki 1700505897457

Karty Anki: 1700505897457
GUID: GauQCrANID; štítky: bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Popište útoky na generátory skutečně náhodných čísel (TRNG).

### Odpověď (Back)

Na generátory skutečně náhodných čísel (TRNG) lze provádět pasivní útoky:

- útok postranním kanálem,

ale také aktivní útoky:

- provoz mimo povolené specifikace (např. teplota nebo napětí),
- ozáření,
- ovlivnění elektromagnetickým polem.

## Poznámka Anki 1718028908982

Karty Anki: 1718028908983
GUID: DXOVO=p,)`; štítky: bi-hwb::p09 bi-ib::19.

### Otázka (Front)

Popište transient effect ring oscillator (TERO) a jeho využití pro generátory skutečně náhodných čísel (TRNG).

### Odpověď (Back)

Transient effect ring oscillator (TERO) je typ kruhového oscilátoru (ring oscillator), který osciluje pouze dočasně. Počet oscilací lze následně použít pro generování náhodných čísel.

