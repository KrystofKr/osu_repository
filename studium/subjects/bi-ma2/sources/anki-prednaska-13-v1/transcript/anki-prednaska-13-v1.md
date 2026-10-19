# BI-MA2 – Přednáška 13

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-MA2
Rozsah: 3 poznámek, 3 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1667829778033

Karty Anki: 1667829778034
GUID: MV`fo0@ob(; štítky: bi-ma2::p13.

### Otázka (Front)

Popište iterační metodu analýzy rekurentních rovnic.

### Odpověď (Back)

Pokud aplikujeme iterační metodu na rekurenci tvaru:
\[T(n) = aT\Big(\frac{n}{b}\Big) + f(n),\]pak je obecně potřeba:

- určit počet iterací, nutných k dosažení koncových podmínek,
- sečíst řadu nebo odhadnout její součet, případně rozhodnout o její konvergenci/divergenci, nebo nalézt asymptotické chování posloupnosti částečných součtů divergentní číselné řady,
- následně určit, který z členů \(A(n)\) a \(B(n)\) kontroluje výsledné chování.

## Poznámka Anki 1667830803039

Karty Anki: 1667830803039
GUID: i$nZ]8/qA[; štítky: bi-ma2::p13.

### Otázka (Front)

Vyslovte větu o Mistrovské metodě.

### Odpověď (Back)

Nechť \(a \geq 1\) a \(b > 1\) jsou reálné konstanty, \(f\) je kladná funce jedné proměnné. Uvažujme rekurentní rovnici
\[T(n) = a T\Big(\frac{n}{b}\Big) + f(n),\]kde \(\frac{n}{b}\) v argumentu může znamenat i \(\lceil \frac{n}{b} \rceil\) nebo \(\lfloor \frac{n}{b} \rfloor\).
Potom (všechny vztahy myšleny pro \(n \to \infty\)):

- Pokud \(f(n) = \mathcal{O}(n^{\log_b(a) - \varepsilon})\) pro nějaké \(\varepsilon > 0\), potom \(T(n) = \Theta(n^{\log_b(a)})\).
- Pokud \(f(n) = \Theta(n^{\log_b(a)})\), pak \(T(n) = \Theta\big(n^{\log_b(a)} \cdot \ln(n)\big)\)
- Pokud \(f(n) = \Omega(n^{\log_b(a) + \varepsilon})\) pro nějaké \(\varepsilon > 0\) a pokud existuje \(d \in (0,1)\) a \(n_0 \in \mathbb{N}\) takové, že \(af(\frac{n}{b}) \leq d \cdot f(n)\), pro každé \(n \geq n_0\), pak \(T(n) = \Theta(f(n))\).

## Poznámka Anki 1667832201053

Karty Anki: 1667832201053
GUID: c6S}ei0d@X; štítky: bi-ma2::p13.

### Otázka (Front)

Popište substituční metodu analýzy rekurentních rovnic.

### Odpověď (Back)

Mějeme rekurenci
\[T(n) = aT\Big(\frac{n}{b}\Big) + f(n).\]Tato metoda spočívá ve dvou krocích:

- Uhodněte/odhadněte asymptotické chování \(T(n)\), vyjádřené pomocí \(\Theta, \mathcal{O}, \Omega, \dots\)
- Dokažte jeho platnost pomocí matematické indukce.

