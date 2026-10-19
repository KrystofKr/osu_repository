# NI-HWB – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-hwb/NI-HWB.apkg; APKG SHA-256 a65d26859a40bf4bc1c7dc8804425425d385ad2331d944e375f0fd10ce6e3550. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: ac319344d2de2cb4060d944b0c9d196f41ac858e59c961026ffe267a795b1399.
Původní balíčky: NI-HWB
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1740391359375

Karty Anki: 1740391359375
GUID: fX8r{L@W7E; štítky: ni-hwb::p02.

Metadata původního zdroje pro kartu 1740391359375: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the origin of the power analysis side-channel attack.

### Odpověď (Back)

The power consumption of a device depends on the degree of activity of its logical circuits which are typically made up of CMOS transistors. State transitions of a CMOS transistor increase the power consumption of the device linking the power consumption to the operations and values which are processed on the device as activity on its logical circuits triggers these transitions.

## Poznámka Anki 1740392746851

Karty Anki: 1740392746851
GUID: i6EY%3Xy|4; štítky: ni-hwb::p02.

Metadata původního zdroje pro kartu 1740392746851: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the common approach for power analysis side-channel attacks.

### Odpověď (Back)

Power analysis side-channel attacks usually use the following infrastructure:

- **cryptographic device** - carries out cryptographic computations,

- **oscilloscope** - measures the power consumption of the cryptographic device and provides the data to the computer,

- **computer** - controls the computations carried out by the cryptographic device and analyses data from the oscilloscope.

## Poznámka Anki 1740394170566

Karty Anki: 1740394170566
GUID: t7!5p0#a|g; štítky: ni-hwb::p02.

### Otázka (Front)

Describe the properties of a power consumption signal.

### Odpověď (Back)

Power consumption signal consists of the following properties:\[P_\text{total}(t) = P_\text{op}(t) + P_\text{data}(t) + P_\text{el. noise}(t) + P_\text{const} (t),\]where:

- \(P_\text{op}\) is operation-dependent power consumption,

- \(P_\text{data}\) is data-dependent power consumption,

- \(P_\text{el. noise}\) is electronic noise independent of both operations and data,

- \(P_\text{const}\) is a constant component.

Only \(P_\text{op}\) and \(P_\text{data}\) are exploitable by power analysis attacks. This can be expressed as

\[P_\text{op}(t) + P_\text{data}(t) = P_\text{exp}(t) + P_\text{sw. noise}(t),\]where:

- \(P_\text{exp}\) is the exploitable component,

- \(P_\text{sw. noise}\) is switching noise which is dependent on both operations and data but not exploitable.

Therefore:

\[P_\text{total}(t) = P_\text{exp}(t) + P_\text{sw. noise}(t) + P_\text{el. noise}(t) + P_\text{const}(t).\]

## Poznámka Anki 1740394206820

Karty Anki: 1740394206820
GUID: j3g%o@g:W6; štítky: ni-hwb::p02.

Metadata původního zdroje pro kartu 1740394206820: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the types of power analysis side-channel attacks.

### Odpověď (Back)

Power analysis side-channel attacks can be categorized as follows:

- **simple power analysis** - single trace analysed along the time axis,

- **differential power analysis** - multiple traces analysed at the same fixed points in time.

## Poznámka Anki 1740394227584

Karty Anki: 1740394227584
GUID: lUZ^N22?!P; štítky: ni-hwb::p02.

Metadata původního zdroje pro kartu 1740394227584: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the process of differential power analysis.

### Odpověď (Back)

Differential power analysis consists of the following phases:

- choose an intermediate value \(v = f(d, k)\) which depends on known input data \(d\) and an unknown partial key (the partial key must be short enough to be guessable);
- measure power traces \(t_i\) while encrypting different samples of data \(d_i\);
- build a matrix of hypothetical intermediate values \(v_{ij}\) for each of the possible keys \(k\) and used data samples \(d\);
- using a power consumption model, compute the matrix \(h_{ij}\) of hypothetical power consumption;
- statistically evaluate which hypothetical key best matches the measued power traces.

## Poznámka Anki 1740395308189

Karty Anki: 1740395308189
GUID: KT|&`v(y*=; štítky: ni-hwb::p02.

Metadata původního zdroje pro kartu 1740395308189: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the power consumption models used in differential power analysis.

### Odpověď (Back)

Differential power analysis uses the following power consumption models:

- **single bit model** - the power consumption depends on a single bit of the intermediate value,

- **haming weight **- the power consumption depends on the number of set bits in the intermediate value,

- **hamming distance** - the power consumption depends on the number of differing bits between the current and the previous intermediate value.

## Poznámka Anki 1740486352459

Karty Anki: 1740486352459
GUID: E*!G{l:/Bs; štítky: ni-hwb::p02.

### Otázka (Front)

Describe the difference between correlation power analysis (CPA) and differential power analysis (DPA).

### Odpověď (Back)

Both correlation power analysis (CPA) and differential power analysis (DPA) are types of power analysis side-channel attacks but they differ in the following characteristics:

| 
      **correlation power analysis **(CPA) | 
      **differential power analysis** (DPA) | 

| 
      compares power traces with a theoretical model of power consumption | 
      compares power traces with differing keys or data | 

| 
      typically uses Pearson's correlation coefficient  | typically uses difference of means or distance of means | 

| 
      typically requires a smaller number of power traces | 
      typically requires a larger number of power traces
 |

## Poznámka Anki 1741121497078

Karty Anki: 1741121497078
GUID: O7~SJ]y/cD; štítky: ni-hwb::p02.

### Otázka (Front)

Describe the statistical evaluation in differential power analysis (DPA).

### Odpověď (Back)

Statistical evaluation in differential power analysis (DPA) requires the following data:

- known plaintexts,
- measured traces of power consumption paired to the plaintexts.
It starts off with a matrix of traces \(\mathbf T\) where:

- the row index specifies a trace,
- the column index specifies a point in time,
- the element is the byte of a trace at a given point in time.

Now suppose we are targetting the first byte of the key using an intermediate value\[v_{i, j} = \texttt{SBox}(d_i^{(0)} \oplus k_j^{(0)}),\]where \(d_i^{(0)}\) is the first byte of the \(i\)-th plaintext and \(k_j^{(0)}\) is the \(j\)-th possible value of the first byte of a key. This yields the matrix of hypothetical intermediate \(\mathbf V\) values where:

- the row index specifies a plaintext,
- the column index specifies a possible value of the first byte of the key,
- the element is the intermediate value \(v_{i, j}\).

Next, by applying a model of power consumption on \(\mathbf V\) we receive the matrix of hypothetical power consumption \(\mathbf H\). The dimensions of this matrix as well as the meaning of its columns and rows remains the same. Thereafter, we construct a correlation matrix \(\mathbf R\) of matrices \(\mathbf T\) and \(\mathbf H\) where:

- the row index specifies a possible value of the first byte of the key,
- the column index speficies a point in time.
- the element is the correlation between the measured power consumption and the hypothetical power consumption.

The last step is to identify the largest absolute value in the matrix. The larger the absolute value the stronger the correlation meaning a higher probability of the key byte hypothesis being correct.

