# NI-HWB – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-hwb/NI-HWB.apkg; APKG SHA-256 a65d26859a40bf4bc1c7dc8804425425d385ad2331d944e375f0fd10ce6e3550. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: ac319344d2de2cb4060d944b0c9d196f41ac858e59c961026ffe267a795b1399.
Původní balíčky: NI-HWB
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1741601633519

Karty Anki: 1741601633519
GUID: C7Sis_F#rX; štítky: ni-hwb::p04.

### Otázka (Front)

Describe the influence of electronic noise on the power consumption signal.

### Odpověď (Back)

The electronic noise component \(P_\text{el. noise}\) of the power consumption signal is measured by repeating the same operation with the same data. It is approximated using the normal distribution. Therefore, electronic noise can be decreased by averaging the traces.

## Poznámka Anki 1741603354432

Karty Anki: 1741603354432
GUID: kWhpS/+Hy=; štítky: ni-hwb::p04.

### Otázka (Front)

Describe the influence of data on the power consumption signal.

### Odpověď (Back)

The data-dependent component \(P_\text{data}\) of the power consumption signal is measured by repeating a single operation with different data. It is usually approximated using the normal distribution. This stems from the fact that microcontrollers typically leak hamming weights of internal data because they precharge their buses to either a logical 1 or 0 to eliminate electronic noise (circuit floating). Assuming uniformly distrbuted data, hamming weights can be modelled using the binomial distrubution. However, by applying a model of electronic noise, their distribution converges to the normal distribution.

### Doplňující pole (Extra)

In order to precharge their busses, microcontrollers can use the following components which have characteristic impact on the leakage \(l\) of the internal data \(d\) as the value of the signal changes:

- **pullup resistors** - maintain a logical 1, therefore\[l = \operatorname{hw}(\overline d),\]
- **exciters** - maintain a logical 0, therefore\[l = \operatorname{hw}(d),\]

where \(\operatorname{hw}(d)\) is the hamming weight taken from the binary form of \(d\).

## Poznámka Anki 1741604203247

Karty Anki: 1741604203247
GUID: e/@uwXa7Mv; štítky: ni-hwb::p04.

### Otázka (Front)

Describe the signal-to-noise ratio (SNR).

### Odpověď (Back)

Signal-to-noise ratio (SNR) compares the level of the desired signal to the level of noise:\[\text{SNR} = \frac{\operatorname{var} (\text{signal})}{\operatorname{var}(\text{noise})} = \frac{\operatorname{var} P_\text{exp}}{\operatorname{var}(P_\text{sw. noise} + P_\text{el. noise})}.\]Higher SNR values indicate a better ratio of \(P_\text{exp}\) to overall noise. This can be used to optimize power analysis by only analysing time intervals with high SNR.

## Poznámka Anki 1741605160462

Karty Anki: 1741605160462
GUID: I>ipqTy|?F; štítky: ni-hwb::p04.

### Otázka (Front)

Describe the compression of traces in a power analysis attack.

### Odpověď (Back)

The compression of traces in a power analysis attack aims reduce the computational complexity of the attack. Measured traces typically contain redundancies which can be decreased using the following methods of compression:

- **maximum extraction** - only keep intervals with high signal-to-noise ratio (SNR),

- **integration** - sum up raw values, absolute values, or squares of traces from an interval.

## Poznámka Anki 1741605883260

Karty Anki: 1741605883260
GUID: Et:(?C6f`W; štítky: ni-hwb::p04.

### Otázka (Front)

Describe hiding in the context of power side-channels.

### Odpověď (Back)

Hiding is a power side-channel countermeasure that attempts to minimize the exploitable component \(P_\text{exp}\) of the power consumption signal therefore minimizing the signal-to-noise ratio (SNR). This is done by minimizing the dependence of the signal on both data and operations. There are two main approaches to hiding:

- hiding in time,
- hiding in amplitude.

## Poznámka Anki 1741606286357

Karty Anki: 1741606286357
GUID: btiIA?0bF-; štítky: ni-hwb::p04.

### Otázka (Front)

Describe hiding in time in the context of power side-channels.

### Odpověď (Back)

Hiding in time is an approach to the hiding power-side channel countermeasure. Because differential power analysis (DPA) requires traces to be aligned, hiding in time deliberatly misaligns them. This is done by performing operations at different points in time for every encryption. There are two main approaches to hiding in time:

- **insertion of dummy operations** - random clock cycles or \(\texttt{nop}\)s before, during, and after encryption;

- **shuffling** - randomizing the sequence of operations (e.g. S-Box lookups can be done in any order).

This can be implemented in:

- **software** - using random number generators (RNG);
- **hardware** - dummy clock cycles (cycles in which dummy operations are performed), skipping of clock pulses, changing of clock frequencies, switching between multiple clocks.

## Poznámka Anki 1741606556951

Karty Anki: 1741606556951
GUID: P*f3C?@h7|; štítky: ni-hwb::p04.

### Otázka (Front)

Describe hiding in amplitude in the context of power side-channels.

### Odpověď (Back)

Hiding in time is an approach to the hiding power-side channel countermeasure. It works by manipulating the power consumption signal to randomize power consumption of all operations. There are two main approaches to hiding in amplitude:

- **minimizing the exploitabe component** (\(\operatorname{var} P_\text{exp} \to 0\)) - all operations consume the same amount of power for any data;

- **maximizing noise **(\(\operatorname{var} (P_\text{sw. noise} + P_\text{el. noise}) \to \infty\)) - random switching dominates power consumption.

This can be implemented in:

- **software** - choosing instructions with low leakage, avoiding data-dependent branching and memory adressing, paralelization;

- **hardware** - power supply filtering, noise generators.

## Poznámka Anki 1741644924008

Karty Anki: 1741644924009
GUID: FL[Mp0j9a^; štítky: ni-hwb::p04.

### Otázka (Front)

Describe the influence of operations on the power consumption signal.

### Odpověď (Back)

The operation-dependent component \(P_\text{op}\) of the power consumption signal is measured by repeating different operations with the same data. It is usually aproximated using the normal distribution; however, a larger amount of samles is required to eliminate electronic noise. Although often assumed, in practice \(P_\text{op}\) and \(P_\text{data}\) are rarely independent.

## Poznámka Anki 1741695509391

Karty Anki: 1741695509391
GUID: yQo*iN<s6e; štítky: ni-hwb::p04 ni-hwb::p05.

### Otázka (Front)

Describe attacks on hiding in the context of power side-channels.

### Odpověď (Back)

Methods of attacking the hiding countermeasure in power side-channel attacks differ based on the type of hiding used. Hiding in time can be attacked using:

- **trace realignment** - computing cross-correlation to discover prominent features and using them to realign the traces,

- **trace integration** - adding the trace to itself shifted along the time axis may bring traces into alignment.

 [Obrázek: paste-09c0894f402e4b02f97b57af97ca953ce243e725.jpg; soubor je v media/ v doprovodném ZIP] 

Hiding in amplitude can typically be attacked by targetting the used logic style. Additional leakage may then be caused by:

- imperfections in cells or routing,
- glitches in logic functions.

