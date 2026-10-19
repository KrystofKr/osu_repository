# BI-KAB – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-kab/BI-KAB.apkg; APKG SHA-256 080060aa53ee5f63eca18237eef611a0bfca99908f9ab640e349ebadb96964ec. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 8571882594c00598a0b5a029eed57cadb06fe0563741a3f883a87eacef0c1588.
Původní balíčky: BI-KAB
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1680602520279

Karty Anki: 1680602520279
GUID: uOI]V[XkVm; štítky: bi-kab::p06 bi-spol::09.

### Otázka (Front)

Popište kryptosystém veřejného klíče.

### Odpověď (Back)

Kryptosystém veřejného klíče je asymetrický šifrovací systém, který sestává ze dvou klíčů:

- **veřejný klíč **(VK), který se použije pro zašifrování,

- **soukromý klíč** (SK), který se použije pro dešifrování.

Každý komunikující subjekt má tedy svůj vlastní VK a SK. Použitím daného VK je každý schopen danému subjektu poslat zašifrovanou zprávu, ale pouze příjemce ji je schopen děšifrovat pomocí svého SK, neboť odvodit SK při znalosti VK je výpočetně nemožné.

## Poznámka Anki 1680604425017

Karty Anki: 1680604425017
GUID: xi`sAr@UnG; štítky: bi-kab::p06 bi-spol::09.

### Otázka (Front)

Popište šifrovací systém RSA včetně postupu šifrování a dešifrování.

### Odpověď (Back)

RSA je asymetrický kryptosystém veřejného klíče, který je založen na modulárním umocňování. Za VK považujeme dvojici \((e, n)\) takové, že \(\gcd \big(e, \varphi(n) \big) = 1\) a 
\[n = p \cdot q,\], kde \(p\) a \(q\) jsou prvočísla. Za SK považujeme dvojici \((d, n)\), kde
\[d = | e^{-1} |_{\varphi(n)}.\]Symboly OT můžeme šifrovat zvlášť nebo po blocích. Šifrovací zobrazení potom definujeme jako
\[c = | m^e |_n\]a dešifrovací zobrazení jako
\[m = | c^d |_n.\]V dešifrovacím zobrazení používáme Bézoutovu rovnost a Eulerovu větu. Důkaz funkčnosti dešifrovacího vztahu je následující
\[| c^d |_n = | (m^e)^d |_n = |m^{e \cdot d}|_n \stackrel{\text{BR}}{=} |m^{1 + k \cdot \varphi(n)}|_n = |m \cdot (m^{\varphi(n)})^k|_n \stackrel{\text{EV}}{=} |m|_n.\]

## Poznámka Anki 1680604623997

Karty Anki: 1680604623997
GUID: gz.05BqG!0; štítky: bi-kab::p06 bi-spol::09.

### Otázka (Front)

Porovnejte RSA a exponenciální šifru.

### Odpověď (Back)

Oba šifrovací systémy jsou založeny na modulárním umocňování, ale RSA je asymetrický kryptosystém, kdežto exponenciální šifra je symetrická. Exponenciální šifra stojí na tajném sdíleném klíči \(e\) (\(d\) z něj snadno odvodíme pomocí REA) a její bezpečnost je garantována problémem diskrétního logaritmu. Bezpečnost RSA je založena na tajném rozkladu modulu \(n\), tedy problému faktorizace.

## Poznámka Anki 1680606399972

Karty Anki: 1680606399972
GUID: G%~DeG$=</; štítky: bi-kab::p06.

### Otázka (Front)

Vyslovte větu o prvočíslech.

### Odpověď (Back)

Nechť \(\pi\) je funkce, která každému \(x \in \mathbb R\) přiřadí počet prvočísel menších nebo rovných \(x\). Věta o prvočíslech říká, že
\[\displaystyle \lim_{x \to \infty} \frac{\pi(x)}{\frac x{\ln(x)}} = 1,\]neboli
\[\pi(x) \sim \frac x{\ln(x)}.\]

## Poznámka Anki 1680606910412

Karty Anki: 1680606910412
GUID: C}V4KVsEAu; štítky: bi-kab::p06 bi-spol::09.

### Otázka (Front)

Popište postup pro generování VK a SK u RSA.

### Odpověď (Back)

Postup generování VK a SK u RSA je následující:

- Čísla \(p\) a \(q\) jsou volena náhodně jako lichá čísla s 340 dekadickými číslicemi. Podle věty o prvočíslech je pravděpodobnost toho, že takto zvolená čísla jsou prvočísla přibližně

\[\frac 2{\ln(10^{340})}.\]

- Čísla jsou následně testována pomocí Rabin-Millerova pravděpodobnostního testu na 100 svědků. Pravděpodobnost, že čísla jsou složená potom činí

\[\frac 1 {10^{60}}.\]

- Následně je zvolen šifrovací exponent \(e\) a dopočteny další parametry šifry.

## Poznámka Anki 1680612959074

Karty Anki: 1680612959075
GUID: v}uv2gwlSu; štítky: bi-kab::p06 bi-spol::09.

### Otázka (Front)

Popište princip digitálního podepisování pomocí RSA. K čemu slouží?

### Odpověď (Back)

Digitální podpis umí zajistit, že

- zprávu si přečte pouze zamýšlený adresát;
- potvrzení, že zprávu skutečně odeslal daný odesílatel.
Mějme subjekt A, který chce poslat podepsanou zprávu subjektu B. Postup je následující:

- Subjekt A spočte pro zprávu \(m\) podpis \(s\) pomocí svého soukromého klíče:

\[s = D_{\text{SK}_A}(m) = |m^{d_\text A}|_{n_\text A}.\]

- Subjekt A zašifruje podpis \(S\) pomocí veřejného klíče subjektu B:

\[c = E_{\text{VK}_\text B}(s) = |s^{e_\text B}|_{n_\text B}.\]

- Subjekt B dešifruje zprávu pomocí svého soukromého klíče a získá \(s\):

\[D_{\text{SK}_\text B}(c) = D_{\text{SK}_\text B}\big(E_{\text{VK}_\text B}(s)\big) = s.\]

- Subjekt B z \(s\) pomocí veřejného klíče subjektu A a získá zprávu \(m\):
\[E_{\text{VK}_\text A}(s) = E_{\text{VK}_\text A}\big(D_{\text{SK}_\text A}(m)\big) = m.\]Identita \(E_{\text{VK}_\text A}\big(D_{\text{SK}_\text A}(m)\big) = m\) (obdobně pro \(D_{\text{SK}_\text B}\big(E_{\text{VK}_\text B}(s)\big) = s\))  plyne z rovnosti

\[E_{\text{VK}_\text A}\big(D_{\text{SK}_\text A}(m)\big) = |(m^{d_\text A})^{e_\text A}|_{n_\text A} = |m^{d_\text A \cdot e_\text A}|_{n_\text A} = m,\]protože

\[|d_\text A \cdot e_\text A|_{\varphi(n_\text A)} = 1.\]

## Poznámka Anki 1680614393704

Karty Anki: 1680614393704
GUID: i>$YY<?Xbo; štítky: bi-kab::p06 bi-spol::09.

### Otázka (Front)

Jak probíhá šifrování u RSA-CRT? V čem spočívá zrychlení?

### Odpověď (Back)

RSA-CRT použije k zašifrování stejný vztah jako RSA, tedy
\[c = |m^e|_n.\]Protože se k šifrování často využívá algoritmus square and multiply, vyplatí se používat šifrovací exponenty \(e\) s nízkou Hammingovou vahou (malým počtem jedniček v binárním zápisu).

## Poznámka Anki 1680615450806

Karty Anki: 1680615450806
GUID: k&1:U~@<j9; štítky: bi-kab::p06 bi-spol::09.

### Otázka (Front)

Definujte VK a SK u RSA-CRT

### Odpověď (Back)

U RSA-CRT pokládáme za VK považujeme dvojici \((e, n)\) takové, že \(\gcd \big(e, \varphi(n) \big) = 1\) a 
\[n = p \cdot q,\], kde \(p\) a \(q\) jsou prvočísla. Za SK považujeme pětici \((p, q, d_p, d_q, q_{\text{inv}})\), kde
\[\begin{matrix}
d_p = | d |_{p - 1}, \\
d_q = | d |_{q - 1}, \\
q_\text{inv} = | q^{-1} |_{p}
\end{matrix}\]a stejně jako u RSA
\[d = | e^{-1} |_{\varphi(n)}.\]

## Poznámka Anki 1680616141169

Karty Anki: 1680616141169
GUID: A%Q;MEpKsD; štítky: bi-kab::p06 bi-spol::09.

### Otázka (Front)

Jak probíhá dešifrování u RSA-CRT? V čem spočívá zrychlení?

### Odpověď (Back)

RSA-CRT používá Čínskou větu o zbytcích (chinese remainder theorem) k rozložení dešifrování na dva výpočty s čísly o poloviční délce. To také umožňí využít paralelní zpracování a dále výpočet urychlit.
Pro \(d_p\) a \(d_q\) musí platit následující kongurence:
\[\begin{matrix}
d_p \cdot e \equiv 1 \pmod{p - 1}, \\
d_q \cdot e \equiv 1 \pmod{q - 1}.
\end{matrix}\]Potom se použije následující postup:
\[\begin{matrix}
m_1 = |c^{d_p}|_p, \\
m_2 = |c^{d_q}|_q, \\
h = |q_\text{inv}(m_1 - m_2)|_p, \\
m = m_2 + hq.
\end{matrix}\]

## Poznámka Anki 1680618176496

Karty Anki: 1680618176496
GUID: MfyoJ%De1x; štítky: bi-ib::07 bi-kab::p06 bi-spol::09.

### Otázka (Front)

Co je to digitální podpis a jaké má vlastnosti?

### Odpověď (Back)

Digitální podpis je obvykle formou asymetrického kryptografického schématu, který využívá SK k podepsání a VK k ověření. Měl by splňovat následující vlastnosti:

- **nefalšovatelnost **(autentizace) - podpis se nedá napodobit jiným subjektem než podepisujícím;

- **integrita** - podepsaná zpráva se nedá změnit, aniž by se zneplatnil podpis;

- **nepopiratelnost** - podepisující nemá možnost později popřít, že zprávu podepsal.

## Poznámka Anki 1680618349542

Karty Anki: 1680618349542
GUID: vLB5vb.dn;; štítky: bi-kab::p06 bi-spol::09.

### Otázka (Front)

Jaké existují kategorie digitálních podpisů?

### Odpověď (Back)

Digitální podpisy dělíme na

- **přímé** (direct) - příjemce zná VK odesílatele, odesílatel však může popřít podepsání zprávy;

- **verifikované** (arbitrated) - využívá důvěryhodnou třetí stranu, která každý podpis ověřuje.

## Poznámka Anki 1680621368963

Karty Anki: 1680621368963
GUID: G!%x}Gzw[S; štítky: bi-kab::p06 bi-spol::09.

Metadata původního zdroje pro kartu 1680621368963: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište šifrovací systém ElGamal.

### Odpověď (Back)

ElGamal je kryptosystém veřejného klíče, který je založen na Diffie-Hellmanově algoritmu (resp. na problému diskrétního logaritmu). Podobně jako RSA umožňuje i digitální podepisování. Předpokládejme dva subjetky A a B, které si chtějí vyměnit zprávu. Subjekt A nejdříve připraví veřejné parametry šifry:

- A zvolí prvočíselný modul \(m\) a generátor \(g\) multiplikativní grupy \(Z_m^\times\).
- A zvolí soukromý klíč \(k_\text A\), kde \(\gcd(k_\text A, m - 1) = 1\), a spočte \(y_\text A = |g^{k_\text A}|_m.\)
- A zveřejní trojici \((m, g, y_\text A)\) jako svůj VK a \(k_\text A\) pokládá za soukromý klíč.

Nyní chce B poslat zprávu \(p\) subjektu A. Postupuje následovně:

- B zvolí \(k_\text B\), kde \(\gcd(k_\text B, m - 1) = 1\), a spočte \(y_\text B = |g^{k_\text B}|_m\).

- B spočte tajný klíč \(K\) pomocí

\[K = |y_\text A^{k_\text B}|_m = |(g^{k_\text A})^{k_\text B}|_m = |g^{k_\text A \cdot k_\text B}|_m.\]

- B zašifruje zprávu \(p\) pomocí vztahu

\[c = |p \cdot K|_m.\]

- B odešle A dvojici \((y_\text B, c)\).

Jakmile A obdrží dvojici \((y_\text B, c)\), může ji dešifrovat následujícím postupem:

- A spočte sdílený klíč \(K = |y_\text B^{k_\text A}|_m = |(g^{k_\text B})^{k_\text A}|_m = |g^{k_\text A \cdot k_\text B}|_m.\)

- A spočte \(|K^{-1}|_m\) pomocí EEA a dešifruje zprávu vztahem

\[|c \cdot K^{-1}|_m = |p \cdot K \cdot K^{-1}|_m = |p|_m.\]

