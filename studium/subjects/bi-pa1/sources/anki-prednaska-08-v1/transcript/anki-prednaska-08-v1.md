# BI-PA1 – Přednáška 08

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-PA1
Rozsah: 1 poznámek, 1 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1718549399893

Karty Anki: 1718549399893
GUID: t74$EeB,k$; štítky: bi-pa1::p08 bi-spol::19.

### Otázka (Front)

Popište ukazatelovou aritmetiku (pointer arithmetic).

### Odpověď (Back)

Ukazatelová arimetika (pointer arithmetic) spočívá v použití aritmetických a porovnávacích operátorů na ukazetele. Konkrétně pro ukazatel \(\texttt p\) typu \(\texttt{T*}\) a proměnnou \(\texttt n\) typu \(\texttt{int}\) se operace
\[\texttt{p + n} \quad \text{resp.} \quad \texttt{p - n}\]provádí tak, že adresa uložená v \(\texttt p\) je zvětšena resp. zmenšena o \(\texttt n \cdot \texttt{sizeof(T)}\) bytů. Operaci přičítání s dereferencí (indirection) lze navíc nahradit subscript operátorem
\[\texttt{*(p + n)} \equiv \texttt{p[n]}.\]Rozdílem dvou ukazatelů je však hodnota typu \(\texttt{std::ptrdiff_t}\), která obsahuje počet prvků mezi danými ukazateli.

