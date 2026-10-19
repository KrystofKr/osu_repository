# Goodfellow – Blok 02 – karty 101–200

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: Goodfellow
Rozsah: 100 poznámek, 100 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.

## Poznámka Anki 1790001406017

Karty Anki: 1790001406017
GUID: i7&Uv6p~>]; štítky: (žádné).

### Otázka (Front)

Je matrix multiplication komutativní?

### Odpověď (Back)

Obecně ne; AB se nemusí rovnat BA a jeden z obou součinů ani nemusí být definován.

## Poznámka Anki 1790001406018

Karty Anki: 1790001406018
GUID: oHCk;g=q7Z; štítky: (žádné).

### Otázka (Front)

Je matrix multiplication asociativní?

### Odpověď (Back)

Ano: A(BC)=(AB)C, pokud jsou všechny součiny rozměrově definované.

## Poznámka Anki 1790001406019

Karty Anki: 1790001406019
GUID: yz;AoDoA%+; štítky: (žádné).

### Otázka (Front)

Je matrix multiplication distributivní?

### Odpověď (Back)

Ano: A(B+C)=AB+AC a (A+B)C=AC+BC.

## Poznámka Anki 1790001406020

Karty Anki: 1790001406020
GUID: Do2vem>)Zw; štítky: (žádné).

### Otázka (Front)

Jak se transpose součinu matrices vztahuje k transpose faktorů?

### Odpověď (Back)

(AB)ᵀ=BᵀAᵀ; pořadí se obrátí.

## Poznámka Anki 1790001406021

Karty Anki: 1790001406021
GUID: jA7v08NB[*; štítky: (žádné).

### Otázka (Front)

Co je Hadamard product A⊙B?

### Odpověď (Back)

Element-wise násobení matrices stejného tvaru: (A⊙B)_i,j=A_i,jB_i,j.

## Poznámka Anki 1790001406022

Karty Anki: 1790001406022
GUID: xTHw]3DB_M; štítky: (žádné).

### Otázka (Front)

Jak se liší dot product vectorů od Hadamard productu?

### Odpověď (Back)

Dot product xᵀy=Σ_i x_i y_i je scalar, zatímco x⊙y je vector element-wise součinů.

## Poznámka Anki 1790001406023

Karty Anki: 1790001406023
GUID: JP7;~pPz%6; štítky: (žádné).

### Otázka (Front)

Jak lze dot product vyjádřit pomocí norem a úhlu?

### Odpověď (Back)

xᵀy=||x||₂||y||₂ cos θ.

## Poznámka Anki 1790001406024

Karty Anki: 1790001406024
GUID: dK_h,s,ER5; štítky: (žádné).

### Otázka (Front)

Kdy jsou dva nenulové vectors orthogonal?

### Odpověď (Back)

Když jejich dot product je nulový.

## Poznámka Anki 1790001406025

Karty Anki: 1790001406025
GUID: oj|BM[Gekf; štítky: (žádné).

### Otázka (Front)

Co je identity matrix I?

### Odpověď (Back)

Square matrix s jedničkami na diagonále a nulami jinde, která splňuje Ix=x a AI=A.

## Poznámka Anki 1790001406026

Karty Anki: 1790001406026
GUID: N<Ud:5#EAF; štítky: (žádné).

### Otázka (Front)

Co je inverse matrix A⁻¹?

### Odpověď (Back)

Matrix splňující A⁻¹A=I a AA⁻¹=I.

## Poznámka Anki 1790001406027

Karty Anki: 1790001406027
GUID: xb7SbEWX;q; štítky: (žádné).

### Otázka (Front)

Kdy má square matrix unikátní inverse?

### Odpověď (Back)

Právě tehdy, když je nonsingular, tedy má full rank a determinant nenulový.

## Poznámka Anki 1790001406028

Karty Anki: 1790001406028
GUID: lAy!nc$k=b; štítky: (žádné).

### Otázka (Front)

Proč se explicitní výpočet A⁻¹ při numerickém řešení Ax=b obvykle nedoporučuje?

### Odpověď (Back)

Specializované solvery jsou přesnější a efektivnější než výpočet inverse a následné násobení.

## Poznámka Anki 1790001406029

Karty Anki: 1790001406029
GUID: Bo1U1[H9G+; štítky: (žádné).

### Otázka (Front)

Co je linear combination vectorů v^(1),…,v^(n)?

### Odpověď (Back)

Výraz Σ_i c_i v^(i), kde c_i jsou scalars.

## Poznámka Anki 1790001406030

Karty Anki: 1790001406030
GUID: rvmonmQg/;; štítky: (žádné).

### Otázka (Front)

Co je span množiny vectorů?

### Odpověď (Back)

Množina všech jejich možných lineárních kombinací.

## Poznámka Anki 1790001406031

Karty Anki: 1790001406031
GUID: zIPK<ulbLU; štítky: (žádné).

### Otázka (Front)

Co znamená, že vector x je v column space matrix A?

### Odpověď (Back)

x lze vyjádřit jako lineární kombinaci sloupců A.

## Poznámka Anki 1790001406032

Karty Anki: 1790001406032
GUID: JSH,E7tq~k; štítky: (žádné).

### Otázka (Front)

Proč má Ax=b řešení pouze tehdy, když b leží ve span sloupců A?

### Odpověď (Back)

Ax je vždy lineární kombinací sloupců A s koeficienty danými x.

## Poznámka Anki 1790001406033

Karty Anki: 1790001406033
GUID: vo0L(7Lp>Z; štítky: (žádné).

### Otázka (Front)

Co znamená linear dependence množiny vectorů?

### Odpověď (Back)

Alespoň jeden vector lze vyjádřit jako lineární kombinaci ostatních; ekvivalentně existuje netriviální kombinace Σ_i c_i v_i=0.

## Poznámka Anki 1790001406034

Karty Anki: 1790001406034
GUID: qkzWA{}ejP; štítky: (žádné).

### Otázka (Front)

Co znamená linear independence?

### Odpověď (Back)

Jediná kombinace Σ_i c_i v_i=0 má všechny koeficienty c_i=0.

## Poznámka Anki 1790001406035

Karty Anki: 1790001406035
GUID: QU}cx8Q,NX; štítky: (žádné).

### Otázka (Front)

Co je rank matrix?

### Odpověď (Back)

Dimenze jejího column space; rovná se také dimenzi row space.

## Poznámka Anki 1790001406036

Karty Anki: 1790001406036
GUID: mni7WCB1r?; štítky: (žádné).

### Otázka (Front)

Co znamená full column rank?

### Odpověď (Back)

Sloupce matrix jsou linearly independent a rank se rovná počtu sloupců.

## Poznámka Anki 1790001406037

Karty Anki: 1790001406037
GUID: f~rT#WKZEY; štítky: (žádné).

### Otázka (Front)

Co znamená full row rank?

### Odpověď (Back)

Řádky matrix jsou linearly independent a rank se rovná počtu řádků.

## Poznámka Anki 1790001406038

Karty Anki: 1790001406038
GUID: q}&1-FpY|0; štítky: (žádné).

### Otázka (Front)

Jak full rank souvisí s invertibilitou square matrix?

### Odpověď (Back)

Square matrix je invertibilní právě tehdy, když má full rank.

## Poznámka Anki 1790001406039

Karty Anki: 1790001406039
GUID: zD&^[6N;(D; štítky: (žádné).

### Otázka (Front)

Co je L^p norm vectoru x?

### Odpověď (Back)

[Obrázek: paste-8ff35d2e3998d23bee010926c8ea5ed2357e10f2.jpg; soubor je v media/ v doprovodném ZIP] 
 [Obrázek: paste-74c1392d1c6d7a5535eddd938cfcb09317ecdd22.jpg; soubor je v media/ v doprovodném ZIP] 
 [Obrázek: paste-1a04d409d7097fc57eb79bc3051073c250fd0778.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1790001406040

Karty Anki: 1790001406040
GUID: cMGD7CC)vU; štítky: (žádné).

### Otázka (Front)

Co je Euclidean neboli L² norm?

### Odpověď (Back)

||x||₂=sqrt(Σ_i x_i²).

## Poznámka Anki 1790001406041

Karty Anki: 1790001406041
GUID: z_fRWn3E`z; štítky: (žádné).

### Otázka (Front)

Jak souvisí squared L² norm s dot productem?

### Odpověď (Back)

||x||₂²=xᵀx.

## Poznámka Anki 1790001406042

Karty Anki: 1790001406042
GUID: FF}q;Y}$AF; štítky: (žádné).

### Otázka (Front)

Co je L¹ norm?

### Odpověď (Back)

||x||₁=Σ_i |x_i|; často podporuje sparse solutions, protože lineárně penalizuje nenulové components.

## Poznámka Anki 1790001406043

Karty Anki: 1790001406043
GUID: CO~[xe}pSa; štítky: (žádné).

### Otázka (Front)

Co je L∞ norm?

### Odpověď (Back)

Maximum absolute component: ||x||∞=max_i |x_i|.

## Poznámka Anki 1790001406044

Karty Anki: 1790001406044
GUID: c_[WoJ5/FB; štítky: (žádné).

### Otázka (Front)

Proč p<1 nedává skutečnou normu v definici L^p?

### Odpověď (Back)

Nesplňuje triangle inequality.

## Poznámka Anki 1790001406045

Karty Anki: 1790001406045
GUID: mDWl*xTs`X; štítky: (žádné).

### Otázka (Front)

Co se někdy neformálně označuje jako L⁰ 'norm'?

### Odpověď (Back)

Počet nenulových components vectoru, ačkoli nejde o matematickou normu.

## Poznámka Anki 1790001406046

Karty Anki: 1790001406046
GUID: LR@XHSGTtv; štítky: (žádné).

### Otázka (Front)

Co je Frobenius norm matrix A?

### Odpověď (Back)

[Obrázek: paste-9c17c1f845ec09b4a2f3eacc084c1e013b77ef68.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1790001406047

Karty Anki: 1790001406047
GUID: B1<BQByI$s; štítky: (žádné).

### Otázka (Front)

Co je diagonal matrix?

### Odpověď (Back)

Matrix, jejíž všechny off-diagonal prvky jsou nulové.

## Poznámka Anki 1790001406048

Karty Anki: 1790001406048
GUID: M5kB|b}7Zk; štítky: (žádné).

### Otázka (Front)

Jaká je computational výhoda diagonal matrix D?

### Odpověď (Back)

Násobení Dx pouze škáluje jednotlivé components x a lze jej provést v O(n).

## Poznámka Anki 1790001406050

Karty Anki: 1790001406050
GUID: Gt2&&1&g}J; štítky: (žádné).

### Otázka (Front)

Co je unit vector?

### Odpověď (Back)

Vector s Euclidean norm 1.

## Poznámka Anki 1790001406051

Karty Anki: 1790001406051
GUID: M#t3GJxP{U; štítky: (žádné).

### Otázka (Front)

Co znamená, že vectors jsou orthonormal?

### Odpověď (Back)

Jsou navzájem orthogonal a každý má normu 1.

## Poznámka Anki 1790001406052

Karty Anki: 1790001406052
GUID: p*Cz9`3ZKe; štítky: (žádné).

### Otázka (Front)

Co je orthogonal matrix Q?

### Odpověď (Back)

Square matrix s orthonormal columns i rows, takže QᵀQ=QQᵀ=I a Q⁻¹=Qᵀ.

## Poznámka Anki 1790001406053

Karty Anki: 1790001406053
GUID: O{@mxL}au(; štítky: (žádné).

### Otázka (Front)

Proč orthogonal matrix zachovává Euclidean norm?

### Odpověď (Back)

||Qx||₂²=xᵀQᵀQx=xᵀx.

## Poznámka Anki 1790001406054

Karty Anki: 1790001406054
GUID: LU58#,P@6V; štítky: (žádné).

### Otázka (Front)

Co je eigenvector matrix A?

### Odpověď (Back)

Nenulový vector v splňující Av=λv pro nějakou scalar eigenvalue λ.

## Poznámka Anki 1790001406055

Karty Anki: 1790001406055
GUID: }V(E4>#BH; štítky: (žádné).

### Otázka (Front)

Co znamená eigenvalue λ geometricky?

### Odpověď (Back)

A transformuje příslušný eigenvector pouze škálováním faktorem λ bez změny jeho směru, s výjimkou obrácení znaménka.

## Poznámka Anki 1790001406056

Karty Anki: 1790001406056
GUID: F_5+D?y/uD; štítky: (žádné).

### Otázka (Front)

Jak vypadá eigendecomposition diagonalizovatelné matice (A)?

### Odpověď (Back)

[Obrázek: paste-a2cb0791a3592adf893bdabd326e981d85dbebab.jpg; soubor je v media/ v doprovodném ZIP] 
 [Obrázek: paste-1cdaad2c7408e82072750894906260c5a2fb9660.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1790001406057

Karty Anki: 1790001406057
GUID: c6nQ2>:J~|; štítky: (žádné).

### Otázka (Front)

Jak vypadá eigendecomposition real symmetric matrix A?

### Odpověď (Back)

A=QΛQᵀ s orthogonal Q a real diagonal Λ.

## Poznámka Anki 1790001406058

Karty Anki: 1790001406058
GUID: dcjWs^DzDm; štítky: (žádné).

### Otázka (Front)

Proč jsou symmetric matrices zvlášť příjemné pro eigendecomposition?

### Odpověď (Back)

Mají úplnou orthonormal eigenbasis a všechny eigenvalues jsou reálné.

## Poznámka Anki 1790001406059

Karty Anki: 1790001406059
GUID: Dq7XCGe_mN; štítky: (žádné).

### Otázka (Front)

Co je positive definite matrix?

### Odpověď (Back)

Symmetric matrix A, pro kterou xᵀAx>0 pro každý nenulový x.

## Poznámka Anki 1790001406060

Karty Anki: 1790001406060
GUID: y}K1JA|+BO; štítky: (žádné).

### Otázka (Front)

Co je positive semidefinite matrix?

### Odpověď (Back)

Symmetric matrix A, pro kterou xᵀAx≥0 pro každý x.

## Poznámka Anki 1790001406061

Karty Anki: 1790001406061
GUID: FOcFeguG]7; štítky: (žádné).

### Otázka (Front)

Jak lze positive definiteness charakterizovat eigenvalues?

### Odpověď (Back)

Symmetric matrix je positive definite právě tehdy, když všechny eigenvalues jsou kladné; PSD když jsou nezáporné.

## Poznámka Anki 1790001406062

Karty Anki: 1790001406062
GUID: gJ84yOfM22; štítky: (žádné).

### Otázka (Front)

Co je negative definite matrix?

### Odpověď (Back)

Symmetric matrix s xᵀAx<0 pro každý nenulový x; ekvivalentně má všechny eigenvalues záporné.

## Poznámka Anki 1790001406063

Karty Anki: 1790001406063
GUID: tIJjK?dj74; štítky: (žádné).

### Otázka (Front)

Co je singular value decomposition matrix A?

### Odpověď (Back)

Factorization A=UDVᵀ, kde U a V jsou orthogonal matrices a D obsahuje nezáporné singular values.

## Poznámka Anki 1790001406064

Karty Anki: 1790001406064
GUID: Qa-2-LqIOX; štítky: (žádné).

### Otázka (Front)

Jak se SVD liší od eigendecomposition?

### Odpověď (Back)

SVD existuje pro libovolnou real m×n matrix, zatímco standardní eigendecomposition se týká square matrices a nemusí být vždy diagonalizovatelná.

## Poznámka Anki 1790001406065

Karty Anki: 1790001406065
GUID: E9bAW}Y8pT; štítky: (žádné).

### Otázka (Front)

Jak souvisejí singular values A s eigenvalues AᵀA?

### Odpověď (Back)

Singular values jsou druhé odmocniny eigenvalues AᵀA.

## Poznámka Anki 1790001406066

Karty Anki: 1790001406066
GUID: I-rjeT.6U|; štítky: (žádné).

### Otázka (Front)

Co představují right singular vectors A?

### Odpověď (Back)

Columns V jsou eigenvectors AᵀA.

## Poznámka Anki 1790001406067

Karty Anki: 1790001406067
GUID: x5;p]QDI/%; štítky: (žádné).

### Otázka (Front)

Co představují left singular vectors A?

### Odpověď (Back)

Columns U jsou eigenvectors AAᵀ.

## Poznámka Anki 1790001406068

Karty Anki: 1790001406068
GUID: Ed-:d3$C#S; štítky: (žádné).

### Otázka (Front)

Co je Moore–Penrose pseudoinverse A⁺?

### Odpověď (Back)

Generalizace inverse na rectangular nebo singular matrices, získaná ze SVD jako A⁺=VD⁺Uᵀ.

## Poznámka Anki 1790001406069

Karty Anki: 1790001406069
GUID: j|ipLSyDI>; štítky: (žádné).

### Otázka (Front)

Jak se vytváří D⁺ při pseudoinverse?

### Odpověď (Back)

Nenulové singular values se převrátí a matrix se transponuje do odpovídajícího tvaru; nulové singular values zůstávají nulové.

## Poznámka Anki 1790001406070

Karty Anki: 1790001406070
GUID: qS~pg4Ml8T; štítky: (žádné).

### Otázka (Front)

Jaký least-squares problém řeší A⁺?

### Odpověď (Back)

x=A⁺y dává řešení minimalizující ||Ax−y||₂; z více řešení volí minimum-norm solution.

## Poznámka Anki 1790001406071

Karty Anki: 1790001406071
GUID: tYt[ZU7byt; štítky: (žádné).

### Otázka (Front)

Co je trace matrix A?

### Odpověď (Back)

Tr(A)=Σ_i A_i,i, součet diagonal elements.

## Poznámka Anki 1790001406072

Karty Anki: 1790001406072
GUID: FD)b-y9Bz^; štítky: (žádné).

### Otázka (Front)

Jaká důležitá cyclic property platí pro trace?

### Odpověď (Back)

Tr(ABC)=Tr(CAB)=Tr(BCA), pokud jsou součiny rozměrově definované.

## Poznámka Anki 1790001406073

Karty Anki: 1790001406073
GUID: y@olP7zCV; štítky: (žádné).

### Otázka (Front)

Proč je trace užitečná v matrix calculus?

### Odpověď (Back)

Umožňuje přepisovat sums scalar products do kompaktní matrix formy a cyklicky měnit pořadí faktorů.

## Poznámka Anki 1790001406074

Karty Anki: 1790001406074
GUID: BV1S8Lc@e0; štítky: (žádné).

### Otázka (Front)

Co je determinant square matrix A?

### Odpověď (Back)

Scalar det(A) popisující oriented volume scaling lineární transformace A.

## Poznámka Anki 1790001406075

Karty Anki: 1790001406075
GUID: EG>ejk5[kW; štítky: (žádné).

### Otázka (Front)

Co znamená det(A)=0?

### Odpověď (Back)

Matrix je singular a transformace zkolabuje prostor do nižší dimenze.

## Poznámka Anki 1790001406076

Karty Anki: 1790001406076
GUID: y!)ppN)Mxn; štítky: (žádné).

### Otázka (Front)

Jak determinant souvisí s eigenvalues?

### Odpověď (Back)

Det(A) je součin eigenvalues A, s algebraickou multiplicitou.

## Poznámka Anki 1790001406077

Karty Anki: 1790001406077
GUID: i-5~_.5>KK; štítky: (žádné).

### Otázka (Front)

Jak determinant orthogonal matrix souvisí s volume?

### Odpověď (Back)

Má absolutní hodnotu 1, takže orthogonal transformace zachovává volume.

## Poznámka Anki 1790001406078

Karty Anki: 1790001406078
GUID: DU^Ws>G<Q(; štítky: (žádné).

### Otázka (Front)

Jaký optimization problem řeší první principal component PCA?

### Odpověď (Back)

Hledá unit vector w, který minimalizuje reconstruction error po projekci na span(w), ekvivalentně maximalizuje variance wᵀx.

## Poznámka Anki 1790001406079

Karty Anki: 1790001406079
GUID: AJUUu}K{/r; štítky: (žádné).

### Otázka (Front)

Jak se data před standardní PCA typicky centrují?

### Odpověď (Back)

Odečte se sample mean, aby principal directions popisovaly variabilitu kolem středu dat.

## Poznámka Anki 1790001406080

Karty Anki: 1790001406080
GUID: eCGJmV*YlR; štítky: (žádné).

### Otázka (Front)

Jaká je první principal direction v terms covariance matrix?

### Odpověď (Back)

Eigenvector covariance matrix s největší eigenvalue.

## Poznámka Anki 1790001406081

Karty Anki: 1790001406081
GUID: EgbBO$Wku/; štítky: (žádné).

### Otázka (Front)

Co reprezentuje eigenvalue odpovídající principal component?

### Odpověď (Back)

Variance dat zachovanou v tomto směru.

## Poznámka Anki 1790001406082

Karty Anki: 1790001406082
GUID: Dig0JM~v=k; štítky: (žádné).

### Otázka (Front)

Jak se získá d-dimensional PCA subspace?

### Odpověď (Back)

Použije se d eigenvectors covariance matrix s největšími eigenvalues.

## Poznámka Anki 1790001406083

Karty Anki: 1790001406083
GUID: EP>5Z6>nZD; štítky: (žádné).

### Otázka (Front)

Proč PCA poskytuje optimální linear low-dimensional reconstruction podle squared error?

### Odpověď (Back)

Principal subspace zachovává maximum total variance, a tím minimalizuje variance ztracenou v orthogonal complement.

## Poznámka Anki 1790001406084

Karty Anki: 1790001406084
GUID: v<5Qr2p7cn; štítky: (žádné).

### Otázka (Front)

Proč deep learning potřebuje probability theory?

### Odpověď (Back)

K reprezentaci uncertainty, návrhu probabilistic models, definici likelihoods a rozhodování při neúplné nebo noisy informaci.

## Poznámka Anki 1790001406085

Karty Anki: 1790001406085
GUID: f%h>p8X(H$; štítky: (žádné).

### Otázka (Front)

Jaké hlavní zdroje uncertainty uvádí kniha?

### Odpověď (Back)

Inherent stochasticity systému, incomplete observability a incomplete modeling.

## Poznámka Anki 1790001406086

Karty Anki: 1790001406086
GUID: qu[PG>rd*1; štítky: (žádné).

### Otázka (Front)

Co je random variable?

### Odpověď (Back)

Proměnná, která může nabývat různých hodnot podle probability distribution.

## Poznámka Anki 1790001406087

Karty Anki: 1790001406087
GUID: vq7lSb9?/@; štítky: (žádné).

### Otázka (Front)

Co je probability mass function (PMF)?

### Odpověď (Back)

Funkce P(x) pro discrete random variable, která přiřazuje každému možnému stavu nezápornou probability a sumuje se na 1.

## Poznámka Anki 1790001406088

Karty Anki: 1790001406088
GUID: b?[o33Op)!; štítky: (žádné).

### Otázka (Front)

Co je probability density function (PDF)?

### Odpověď (Back)

Nezáporná funkce p(x) pro continuous random variable, jejíž integral přes celý prostor je 1; probability intervalu je integral density přes interval.

## Poznámka Anki 1790001406089

Karty Anki: 1790001406089
GUID: uzQ2-({VU); štítky: (žádné).

### Otázka (Front)

Proč p(x) u continuous variable není probability přesného bodu x?

### Odpověď (Back)

Jednotlivý bod má measure zero a probability se získává integrací density přes oblast.

## Poznámka Anki 1790001406090

Karty Anki: 1790001406090
GUID: gxIbGcCa$l; štítky: (žádné).

### Otázka (Front)

Co je joint probability distribution?

### Odpověď (Back)

Distribution nad více random variables současně, například P(x,y).

## Poznámka Anki 1790001406091

Karty Anki: 1790001406091
GUID: L|&uY5r~i8; štítky: (žádné).

### Otázka (Front)

Co je marginal probability?

### Odpověď (Back)

Distribution subsetu variables získaná sumací nebo integrací ostatních variables z joint distribution.

## Poznámka Anki 1790001406092

Karty Anki: 1790001406092
GUID: C8jt%zJdk5; štítky: (žádné).

### Otázka (Front)

Jak se marginalizuje discrete y z P(x,y)?

### Odpověď (Back)

P(x)=Σ_y P(x,y).

## Poznámka Anki 1790001406093

Karty Anki: 1790001406093
GUID: Pf3}p=IXo); štítky: (žádné).

### Otázka (Front)

Jak se marginalizuje continuous y z p(x,y)?

### Odpověď (Back)

p(x)=∫p(x,y)dy.

## Poznámka Anki 1790001406094

Karty Anki: 1790001406094
GUID: n,xIVS>k&,; štítky: (žádné).

### Otázka (Front)

Co je conditional probability P(y|x)?

### Odpověď (Back)

Probability y po zohlednění informace, že x nastalo: P(y|x)=P(x,y)/P(x), pokud P(x)>0.

## Poznámka Anki 1790001406095

Karty Anki: 1790001406095
GUID: dutIY;zmTX; štítky: (žádné).

### Otázka (Front)

Jak z conditional a marginal distribution získáme joint distribution?

### Odpověď (Back)

P(x,y)=P(x)P(y|x).

## Poznámka Anki 1790001406096

Karty Anki: 1790001406096
GUID: k:-%Bl25Pa; štítky: (žádné).

### Otázka (Front)

Co je chain rule probability?

### Odpověď (Back)

Joint distribution lze rozložit jako P(x¹,…,xⁿ)=P(x¹)∏_{i=2}^n P(xⁱ|x¹,…,xⁱ⁻¹).

## Poznámka Anki 1790001406097

Karty Anki: 1790001406097
GUID: Kp!di/vbe}; štítky: (žádné).

### Otázka (Front)

Co znamená independence random variables x a y?

### Odpověď (Back)

P(x,y)=P(x)P(y) pro všechny jejich hodnoty.

## Poznámka Anki 1790001406098

Karty Anki: 1790001406098
GUID: y_-^f5;6V+; štítky: (žádné).

### Otázka (Front)

Co znamená conditional independence x ⟂ y | z?

### Odpověď (Back)

P(x,y|z)=P(x|z)P(y|z); po znalosti z neposkytuje x dodatečnou informaci o y.

## Poznámka Anki 1790001406099

Karty Anki: 1790001406099
GUID: y=qpMF`N1h; štítky: (žádné).

### Otázka (Front)

Proč jsou independence assumptions důležité?

### Odpověď (Back)

Umožňují kompaktněji reprezentovat high-dimensional distributions a snižují počet potřebných parametrů.

## Poznámka Anki 1790001406100

Karty Anki: 1790001406100
GUID: <``9DrlzA; štítky: (žádné).

### Otázka (Front)

Co je expectation E[f(x)]?

### Odpověď (Back)

Probability-weighted average funkce f(x): sum pro discrete x nebo integral pro continuous x.

## Poznámka Anki 1790001406101

Karty Anki: 1790001406101
GUID: L0,8T*k?@}; štítky: (žádné).

### Otázka (Front)

Jaká je linearity expectation?

### Odpověď (Back)

E[αf(x)+βg(x)]=αE[f(x)]+βE[g(x)] bez potřeby independence.

## Poznámka Anki 1790001406102

Karty Anki: 1790001406102
GUID: ynEb}q|y?G; štítky: (žádné).

### Otázka (Front)

Co je variance Var(x)?

### Odpověď (Back)

E[(x−E[x])²], míra variability random variable kolem mean.

## Poznámka Anki 1790001406103

Karty Anki: 1790001406103
GUID: CUd%Rj*?iK; štítky: (žádné).

### Otázka (Front)

Jak lze variance přepsat pomocí druhého momentu?

### Odpověď (Back)

Var(x)=E[x²]−E[x]².

## Poznámka Anki 1790001406104

Karty Anki: 1790001406104
GUID: B?L]6igf]~; štítky: (žádné).

### Otázka (Front)

Co je standard deviation?

### Odpověď (Back)

Druhá odmocnina variance.

## Poznámka Anki 1790001406105

Karty Anki: 1790001406105
GUID: y1y^_!)`]!; štítky: (žádné).

### Otázka (Front)

Co je covariance Cov(x,y)?

### Odpověď (Back)

E[(x−E[x])(y−E[y])], míra lineární společné variability dvou variables.

## Poznámka Anki 1790001406106

Karty Anki: 1790001406106
GUID: N<Z<b62S4g; štítky: (žádné).

### Otázka (Front)

Co znamená kladná covariance?

### Odpověď (Back)

Hodnoty nad průměrem jedné variable mají tendenci doprovázet hodnoty nad průměrem druhé.

## Poznámka Anki 1790001406107

Karty Anki: 1790001406107
GUID: CzVJt)x_k|; štítky: (žádné).

### Otázka (Front)

Znamená nulová covariance independence?

### Odpověď (Back)

Obecně ne; znamená pouze absenci lineární dependence. Independence však při konečných momentech implikuje nulovou covariance.

## Poznámka Anki 1790001406108

Karty Anki: 1790001406108
GUID: e7^3cDGM9O; štítky: (žádné).

### Otázka (Front)

Co je covariance matrix random vectoru x?

### Odpověď (Back)

Matrix Cov(x)_i,j=Cov(x_i,x_j).

## Poznámka Anki 1790001406109

Karty Anki: 1790001406109
GUID: MN9(N{7Q[D; štítky: (žádné).

### Otázka (Front)

Jaké properties má covariance matrix?

### Odpověď (Back)

Je symmetric a positive semidefinite.

## Poznámka Anki 1790001406110

Karty Anki: 1790001406110
GUID: I4?32jkSi{; štítky: (žádné).

### Otázka (Front)

Co je Bernoulli distribution?

### Odpověď (Back)

Distribution nad binary variable x∈{0,1} s P(x=1)=φ a P(x=0)=1−φ.

## Poznámka Anki 1790001406111

Karty Anki: 1790001406111
GUID: rLl@KF_oG^; štítky: (žádné).

### Otázka (Front)

Jaké mean a variance má Bernoulli(φ)?

### Odpověď (Back)

E[x]=φ a Var(x)=φ(1−φ).

## Poznámka Anki 1790001406112

Karty Anki: 1790001406112
GUID: NI+APk.3uO; štítky: (žádné).

### Otázka (Front)

Co je multinoulli neboli categorical distribution?

### Odpověď (Back)

Distribution nad jednou z k kategorií parametrizovaná probability vectorem p, jehož components jsou nezáporné a sumují se na 1.

## Poznámka Anki 1790001406113

Karty Anki: 1790001406113
GUID: p.v{zEN+OL; štítky: (žádné).

### Otázka (Front)

Co je Gaussian neboli normal distribution?

### Odpověď (Back)

Continuous distribution N(x;μ,σ²) definovaná mean μ a variance σ².

## Poznámka Anki 1790001406114

Karty Anki: 1790001406114
GUID: B(`;.eUR+^; štítky: (žádné).

### Otázka (Front)

Proč se Gaussian distribution často používá?

### Odpověď (Back)

Má jednoduché analytické vlastnosti, maximum entropy při fixní mean a variance a vzniká přirozeně v mnoha sumách náhodných vlivů.

## Poznámka Anki 1790001406115

Karty Anki: 1790001406115
GUID: hKxua!z><b; štítky: (žádné).

### Otázka (Front)

Co je multivariate Gaussian distribution?

### Odpověď (Back)

Distribution N(x;μ,Σ) nad vectorem x, kde μ je mean vector a Σ positive semidefinite covariance matrix.

## Poznámka Anki 1790001406116

Karty Anki: 1790001406116
GUID: Q?*Rx%fK/N; štítky: (žádné).

### Otázka (Front)

Co je precision matrix?

### Odpověď (Back)

Inverse covariance β=Σ⁻¹, pokud inverse existuje.

## Poznámka Anki 1790001406117

Karty Anki: 1790001406117
GUID: Pb$+(cahln; štítky: (žádné).

### Otázka (Front)

Jakou computational výhodu má diagonal covariance Gaussian?

### Odpověď (Back)

Jednotlivé dimensions jsou conditionally/explicitně independent a likelihood se počítá jako součin jednorozměrných Gaussian terms.

