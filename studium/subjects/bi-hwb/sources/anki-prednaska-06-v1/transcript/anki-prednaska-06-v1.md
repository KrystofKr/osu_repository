# BI-HWB – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-hwb/BI-HWB.apkg; APKG SHA-256 0303626d2408f7eee1801e17ecb475633a60c42f914f37290ffd8c479013ce2b. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b861d2e855c5070244800c22d62092a09b22aee0ded024030525b06a7d18285e.
Původní balíčky: BI-HWB
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1698683085457

Karty Anki: 1698683085457
GUID: yf&Z^r+BK1; štítky: bi-hwb::p06.

Metadata původního zdroje pro kartu 1698683085457: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište autentizační faktor. Jaké existují skupiny autentizančích faktorů?

### Odpověď (Back)

Autentizační faktor je informace, která se dá použít k autentizaci identity. Existují tři skupiny autentizačních faktorů:

- **znalost** - něco, co uživatel a pouze uživatel zná;

- **vlastnictví** - něco, co uživatel a pouze uživatel má;
- **biometrika** - něco, čím uživatel a pouze uživatel je.

## Poznámka Anki 1698683540114

Karty Anki: 1698683540114
GUID: NsIR:}lP#?; štítky: bi-hwb::p06 ni-pb::21.

### Otázka (Front)

Popište schéma jednoduché autentizace.

### Odpověď (Back)

Mějme dva subjekty, ověřující subjekt \(V\) (verifier) a dokazující subjekt \(T\) (prover nebo také token). Dále mějme parametry \(K_T\) (token key) a \(N\) (nonce). Jednoduché autentizační schéma vypadá následovně:
\[T \to V : T, \{T, N\}_{K_T},\]neboli dokazující \(T\) subjekt posílá verifikujícímu subjektu \(V\) svoji identitu \(T\) a kryptogram obsahující identitu dokazujícího subjektu \(T\) a nonce \(N\) šifrované pomocí token key \(K_T\).

## Poznámka Anki 1698683923948

Karty Anki: 1698683923948
GUID: M_(tq%;#]2; štítky: bi-hwb::p06 ni-pb::21.

### Otázka (Front)

Popište kryptografickou nonce. Jakým způsobem jej můžeme získat?

### Odpověď (Back)

Nonce je číslo, které se používá v kryptografických autentizačních protokolech k prokazání aktuálnosti komunikace a zabránění replay útokům. Získat ji můžeme:

- použitím čítače,
- použitím časové značky,
- náhodně nebo pseudonáhodně.

## Poznámka Anki 1698749188316

Karty Anki: 1698749188316
GUID: b{oIw|jv%1; štítky: bi-hwb::p06 ni-pb::21.

### Otázka (Front)

Popište schéma diverzifikace klíčů.

### Odpověď (Back)

Mějme dokazující subjekt \(T\) (prover nebo také token) a master key \(K_M\). Schéma diverzifikace klíčů je následující:
\[K_T = \{T\}_{K_M}.\]Tedy token key získáme zpracováním identifikátoru dokazujícího subjektu pomocí master key.

## Poznámka Anki 1698749473620

Karty Anki: 1698749473621
GUID: hrpD~a9f?W; štítky: bi-hwb::p06 ni-pb::21.

### Otázka (Front)

Popište autentizační schéma challenge-response.

### Odpověď (Back)

Mějme dva subjekty, ověřující subjekt \(V\) (verifier) a dokazující subjekt \(T\) (prover nebo také token). Dále mějme token key \(K_T\) a nonce \(N\). Schéma challenge-response je následující:

- Verfikující subjekt \(V\) posílá dokazujícímu subjektu \(T\) hodnotu nonce \(N\).

\[V \to T : N\]

- Dokazující subjekt odpovídá svou identitou \(T\) a nonce \(N\) zašifrovanou pomocí token key \(K_T\).

\[T \to V : \{T, N\}_{K_T}\]

## Poznámka Anki 1698749883592

Karty Anki: 1698749883592
GUID: yso~Mzu*1H; štítky: bi-hwb::p06 ni-pb::21.

### Otázka (Front)

Popište schéma man-in-the-middle útoku.

### Odpověď (Back)

Mějme tři subjekty, ověřující subjekt \(V\) (verifier), dokazující subjekt \(T\) (prover nebo také token) a útočníka \(M\) v pozici man-in-the-middle. Dále mějme token key \(K_T\) a nonce \(N\). Schéma man-in-the-middle útoku je následující:

- Verifikující subjekt \(V\) posílá dokazujícímu subjektu \(T\) hodnotu nonce \(N\), kterou ale zachytí subjekt \(M\).

\[V \to M : N\]

- Subjekt \(M\) přeposílá nonce \(N\) subjektu \(T\).

\[M \to T: N\]

- Subjekt \(T\) odpovídá subjektu \(M\) svou identitou \(T\) a nonce \(N\) zašifrovanými pomocí token key \(K_T\) v domění, že komunikuje s ověřujícím subjektem \(V\).

\[T \to M : \{T, N\}_{K_T}\]

- Subjekt \(M\) přeposílá tyto informace ověrujícímu subjektu \(V\).

\[M \to V : \{T, N\}_{K_T}\]

## Poznámka Anki 1698751009515

Karty Anki: 1698751009516
GUID: qZwf(};ajq; štítky: bi-hwb::p06 ni-pb::21.

### Otázka (Front)

Popište schéma symetrického protokolu Needham-Schroeder.

### Odpověď (Back)

Mějme tři subjekty \(A\), \(B\) a důvěryhodnou třetí stranu \(S\). Předpokládejme, že oba subjekty mají s důvěryhodnou stranou \(S\) sjednané klíče, tedy \(K_{AS}\) a \(K_{BS}\). V případě, že subjekt \(A\) chce bezpečně komunikovat se subjektem \(B\) je schéma protokolu Needham-Schroeder následující:

- Subjekt \(A\) pošle subjektu \(S\) svou identitu \(A\), identitu protistrany \(B\) a nonce \(N_A\).

\[A \to S : A, B, N_A\]

- Subjekt \(S\) posílá odpověď obsahující zopakovanou nonce \(N_A\), klíč \(K_{AB}\), který se použije pro pozdější komunikaci, identitu \(B\) a kryptogram obsahující klíč \(K_{AB}\) a identitu \(A\) zašifrované pomocí \(K_{BS}\), který je určen pro subjekt \(B\). Celá zpráva je šifrována pomocí \(K_{AS}\).

\[S \to A : \{N_A, K_{AB}, B, \{K_{AB}, A\}_{K_{BS}}\}_{K_{AS}}\]

- Subjekt \(A\) přepošle kryptogram s klíčem \(K_{AB}\) a svou identitou \(A\) zašifrované pomocí \(K_{BS}\) subjektu \(B\).

\[A \to B : \{K_{AB}, A\}_{K_{BS}}\]

- Subjekt \(B\) odpovídá nonce \(N_B\) a identitou \(A\) zašifrovanými pomocí klíče \(K_{AB}\).

\[B \to A : \{N_B, A\}_{K_{AB}}\]

- Subjekt \(A\) pošle upravenou nonce \(N_B\) (např. dekrementovanou) zašifrovanou pomocí \(K_{AB}\).

\[A \to B : \{N_B - 1\}_{K_{AB}}\]

## Poznámka Anki 1698753805446

Karty Anki: 1698753805446
GUID: QR7gOscOuj; štítky: bi-hwb::p06 ni-pb::21.

### Otázka (Front)

Popište one-time password algoritmy standardizované Initiative for Open Authentication (OATH).

### Odpověď (Back)

Initiative for Open Authentication (OATH) specifikuje následující tři algoritmy:

- **HMAC-based one-time password** (HOTP) - založené na čítači:

\[\operatorname{HOTP}(\text{key}, \text{counter}) = \operatorname{truncate} \big( \operatorname{HMAC}_{\text{SHA-1}}(\text{key}, \text{counter}) \big),\]

- **time-based one-time password **(TOTP) - založené na časových značkách:

\[\operatorname{TOTP} \Big( \text{key}, \Big \lfloor \frac{\text{time} - \text{oldest time}}{\text{time step}} \Big \rfloor \Big) = \operatorname{HOTP} \Big (\text{key}, \Big \lfloor \frac{\text{time} - \text{oldest time}}{\text{time step}} \Big \rfloor \Big),\]

- **OATH challenge-response algorithm **(OCRA) - založené na výměně challenge-response zpráv.

## Poznámka Anki 1698754155812

Karty Anki: 1698754155813
GUID: QH#u[S^Ey{; štítky: bi-hwb::p06 ni-pb::21.

### Otázka (Front)

Popište OATH challenge-response algorithm (OCRA).

### Odpověď (Back)

OATH challenge-response algorithm (OCRA) je one-time password algoritmus standardizovaný Initiative for Open Authentication (OATH), který je založen na výměně challenge-response zpráv. Definován je následovně:
\[\operatorname{OCRA} = \operatorname{CryptoFunction}(\text{key}, \text{DataInput}),\]kde\[\operatorname{DataInput} = \text{OcraSuite} \| \mathtt{00} \| \text{counter} \| \text{challenge questions} \| \text{hash of a PIN or password} \| \text{time},\]přičemž \(\text{OcraSuite}\) definuje \(\operatorname{CryptoFunction}\) a další parametry \(\operatorname{OCRA}\).

## Poznámka Anki 1698779437704

Karty Anki: 1698779437704
GUID: uKF:If+.Sq; štítky: bi-hwb::p06 ni-pb::21.

### Otázka (Front)

Popište schéma statické asymetrické autentizace.

### Odpověď (Back)

Mějme dva subjekty, ověřující subjekt \(V\) (verifier) a dokazující subjekt \(T\) (prover nebo také token), který vlastní veřejný klíč \(\text{VK}_T\), soukromý klíč \(\text{SK}_T\) a data \(D\), která jsou specifická pro daný token. Schéma statické asymetrické autentizace je následující:
\[T \to V : D, D_{\text{SK}_T}(D),\]tedy dokazující subjekt \(T\) pošle ověrujícímu subjektu \(V\) svá specifická data jak jako otevřený text tak i podepsaná pomocí svého soukromého klíče \(\text{SK}_T\).

## Poznámka Anki 1698779885605

Karty Anki: 1698779885605
GUID: QI+:[@Gj1i; štítky: bi-hwb::p06 ni-pb::21.

### Otázka (Front)

Popište schéma dynamické asymetrické autentizace.

### Odpověď (Back)

Mějme dva subjekty, ověřující subjekt \(V\) (verifier) a dokazující subjekt \(T\) (prover nebo také token), který vlastní veřejný klíč \(\text{VK}_T\) a soukromý klíč \(\text{SK}_T\), a nonce \(N\). Schéma dynamické asymetrické autentizace je následující:

- Ověrující subjekt \(V\) pošle dokazujícímu subjektu \(T\) hodnotu nonce \(N\).

\[V \to T : N\]

- Dokazující subjekt \(T\) odpoví tak, že hodnotu nonce \(N\) podepíše pomocí svého soukromého klíče \(\text{SK}_T\).

\[T \to V : D_{\text{SK}_T}(N)\]

## Poznámka Anki 1698781169981

Karty Anki: 1698781169981
GUID: sHuTJsQDs^; štítky: bi-hwb::p06.

### Otázka (Front)

Popište Fast Identity Online (FIDO) Alliance.

### Odpověď (Back)

Fast Identity Online (FIDO) Alliance je společnost vyvíjející několik volně dostupných standardů autentizačních metod s cílem snížit nadužívání hesel v internetovém prostoru. FIDO zaštiťuje, mimo jiné, standardy Universal Authentication Framework (UAF) nebo Universal 2nd Factor (U2F).

