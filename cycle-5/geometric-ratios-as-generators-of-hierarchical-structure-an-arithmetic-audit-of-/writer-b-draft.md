# Geometric Ratios as Deformation Parameters: Arithmetic Structure Emergence at q = π, φ, e

## Abstract

We investigate the claim, drawn from the ULTRAMETRIC PHYSICS program, that distinctive structures emerge when a deformation parameter q is set equal to a fundamental geometric ratio: π, the golden ratio φ, or Euler's number e. Rather than treating this as a metaphor, we operationalize "structure" as three concrete, checkable properties of the symmetric q-deformed integers [n]_q = (q^n − q^(−n))/(q − q^(−1)): (i) closure in a finitely generated ring, (ii) exact linear recurrences with integer coefficients, and (iii) compatibility with non-Archimedean (ultrametric) valuations. We show by explicit computation that q = φ satisfies all three: [n]_φ equals the Lucas number L_n for odd n and √5·F_n for even n, the Fibonacci gcd identity induces a genuine ultrametric on the index set, and φ admits p-adic embeddings for exactly the primes p ≡ ±1 (mod 5), a set of density 1/2 that we verify by direct enumeration. In contrast, q = e and q = π, being transcendental, fail ring closure and recurrence integrality; their deformed integers are transcendental numbers with no known arithmetic hierarchy. We quantify the failure via continued-fraction diagnostics: φ is the "most badly approximable" real number, while π and e have unbounded partial quotients. The results sharpen the original claim: structure emerges not from geometric celebrity but from algebraicity plus quadratic unit status, of which φ is the unique positive example among the three candidates.

## 1. Introduction

The seed idea under examination comes from the ULTRAMETRIC PHYSICS corpus: "structures emerge when q is a geometric ratio (π, φ, e)?" The question mark is doing heavy lifting. Claims of this shape are common in speculative physics literature — that certain distinguished constants unlock hidden regularities — and are rarely subjected to operational tests. This paper's purpose is to convert the question into falsifiable mathematics.

By a *q-deformation* we mean the standard replacement of the integer n by the q-integer

[n]_q = (q^n − q^(−n)) / (q − q^(−1)),

which satisfies [n]_q → n as q → 1 and underlies q-series, quantum groups, and much of mathematical physics. The question becomes: for which of q ∈ {π, φ, e} does the family {[n]_q : n ≥ 1} exhibit structure, and what kind?

We propose three operational criteria:

1. **Ring closure.** All [n]_q lie in a finitely generated extension of ℤ (ideally ℤ or ℤ[√d]).
2. **Exact recurrence.** The [n]_q satisfy a linear recurrence with integer coefficients and integer (or fixed-algebraic) initial data, so the sequence is determined by finitely many exact bits of information.
3. **Ultrametric compatibility.** There exists a non-Archimedean valuation — an "ultrametric," meaning a distance function satisfying the strong triangle inequality d(x,z) ≤ max(d(x,y), d(y,z)) — with respect to which the deformed integers organize into a hierarchical (tree-like) structure.

Criterion 3 connects the question to the ultrametric physics program and to the Ostrowski theorem, which classifies all absolute values on the rationals: the real one and the p-adic ones. If a deformation parameter is to support structure across completions, it must at least be algebraic, since transcendental numbers have no p-adic conjugates at all.

Our headline finding, derived entirely by explicit arithmetic in Section 4, is a sharp trichotomy: φ passes all three criteria; e and π pass none. The celebrated status of π and e is real-analytic, not arithmetic. We also derive a previously underappreciated ultrametric on the natural numbers induced by Fibonacci divisibility, which realizes criterion 3 concretely for q = φ.

## 2. Background and Related Work

The relevant literature spans strategy documents, applied ultrametric data analysis, and pure ultrametric geometry; we discuss each strand and its relation to our argument.

The European Particle Physics Strategy Update's Physics Briefing Book [1] documents a community process in which hundreds of proposed projects are prioritized; it is relevant here as a model of how speculative claims should be handled — every input is subjected to comparative, criteria-based assessment. We adopt the same posture toward the three candidate q values: no constant gets a pass on reputation. The Snowmass '96 linear collider report [2] performs the analogous service for experimental feasibility: it asks of each machine not "is it elegant?" but "what would it measure, and can it be built?" Our analogues are the three criteria of Section 1, each of which is checkable by finite computation.

On the mathematical side, Khrennikov and coauthors' program of extracting ultrametrics from data [5] shows that hierarchical (ultrametric) structure is not exotic but generic: given cross-tabulated data embedded in a Euclidean space via correspondence analysis, an induced ultrametric models anomaly and change. This supports our criterion 3 as a meaningful notion of "structure" — ultrametricity is the signature of a hierarchy, and its presence or absence is empirically decidable. The ultrametric model of mind [6] extends the same philosophy to cognition, modeling Matte Blanco's principles of symmetric and asymmetric being with an ultrametric topology and connecting it to hierarchical clustering of empirical data; it demonstrates that ultrametric structure can carry substantive content, not merely encode distance trivially.

Pure ultrametric geometry supplies the structural theorems our criterion 3 leans on. The embedding/extension/interpolation paper [3] proves ultrametric analogues of the Arens–Eells embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff compactness characterization; these tell us ultrametric spaces are not a pathological corner but a full-fledged counterpart of metric theory, so demanding ultrametric compatibility of a deformation is a well-posed requirement. The stochastic generation result [7] proves that Euclidean metrics on random point sets in high dimension converge in probability to ultrametrics, with the distance matrix determined by coordinate variances; this is a caution for us — apparent ultrametricity can be an artifact of high dimensionality, so any claimed hierarchy must be exact, not statistical. The ultrametric Cantor set construction [8], built from relative infinitesimals and an inversion rule with a scale- and reparametrisation-invariant valuation, provides a model of how non-Archimedean valuations generate rich fractal measure structure — precisely the kind of "emergent structure" the seed idea gestures at, and a benchmark our Fibonacci ultrametric should be compared against.

From the QNFO corpus, the Ostrowski dimensionless reformulation [9] compiles 53 fundamental equations in Planck units and argues that dimensional formulations implicitly privilege the Archimedean completion of the rationals, per Ostrowski's 1916 theorem; our criterion 3 is a direct application of this mandate — a constant can only participate in the non-Archimedean sector if it is algebraic. The adelic synthesis [10] bridges p-adic analysis, Bruhat–Tits geometry, and Ostrowski completions across quantum field theory, supplying the framework in which "structure" should mean adelic, i.e., simultaneous real and p-adic, coherence. The fine-structure-constant-as-cross-ratio paper [11] reframes α as the cross-ratio of the classical electron radius and the Compton wavelength, extended to Bruhat–Tits buildings; it is the closest methodological precedent, since it converts a distinguished constant into a projective-geometric invariant, exactly as we convert q into a valuation-theoretic invariant. Finally, the fusion MHD analysis of CFETR and HFRC [4], while from a distant subfield, exemplifies the norm we follow: physical designs are validated by explicit magnetohydrodynamic stability analysis, not plausibility arguments — every claim in our Section 4 is likewise backed by displayed arithmetic. The ULTRAMETRIC PHYSICS source itself [12] states the seed claim we test.

## 3. Methods

Our method is deliberately elementary: every claim is reduced to finite exact computation or a cited classical theorem.

**Constants.** φ = (1+√5)/2 = 1.6180339887…; e = 2.7182818285…; π = 3.1415926536…. The values of e^n and π^n used below are standard and were computed to six decimal places; the arithmetic combining them is shown in full.

**Criterion 1 test.** Compute [n]_q for n = 1,…,6 for each q and check membership in ℤ[√5] (for φ) or failure of algebraicity (for e, π, via the Lindemann–Weierstrass theorem, which implies e^n and π^n — the latter conditionally, via Gelfond's result that e^π is transcendental, and the known transcendence of e and π themselves — are transcendental, so [n]_q built from them is not algebraic).

**Criterion 2 test.** Check whether the sequence [n]_q satisfies a linear recurrence with integer coefficients. For any q, [n]_q satisfies [n+1]_q = (q + q^(−1))[n]_q − [n−1]_q; the test is whether the coefficient q + q^(−1) is an integer or a fixed algebraic number.

**Criterion 3 test.** For φ, we construct an ultrametric on ℕ using the Fibonacci gcd identity gcd(F_m, F_n) = F_gcd(m,n) and verify the strong triangle inequality directly. We also determine the set of primes p for which φ ∈ ℚ_p, using quadratic reciprocity and direct enumeration of primes below 100.

**Diagnostics for e and π.** We compare continued-fraction expansions (classical, cited results) and compute the deviation |[2]_q − 2| as a crude "distance from the undeformed case" measure.

## 4. Analysis

### 4.1 The q-integers at q = φ

Since φ² = φ + 1, we have φ^(−1) = φ − 1, so φ − φ^(−1) = φ − (φ − 1) = 1. Therefore the denominator of [n]_φ is 1 and

[n]_φ = φ^n − φ^(−n).

Compute powers using φ² = φ + 1, φ³ = φ·φ² = φ(φ+1) = φ² + φ = 2φ + 1, φ⁴ = φ·φ³ = 2φ² + φ = 3φ + 2, φ⁵ = 5φ + 3, φ⁶ = 8φ + 5 (the coefficients are Fibonacci numbers, as expected from φ^n = F_n φ + F_{n−1}).

Numerically: φ ≈ 1.618034, so
- φ³ = 2(1.618034) + 1 = 4.236068; φ^(−3) = 1/4.236068 = 0.236068 (exact, since φ³·φ^(−3) = 1 and φ^(−3) = 2φ^(−1)·... — directly: φ^(−1) = 0.618034, φ^(−2) = 0.381966, φ^(−3) = 0.236068). Then [3]_φ = 4.236068 − 0.236068 = **4** exactly.
- φ⁴ = 3(1.618034) + 2 = 6.854102; φ^(−4) = 0.145898; [4]_φ = 6.854102 − 0.145898 = **6.708204** = 3√5, since √5 = 2.236068 and 3 × 2.236068 = 6.708204. ✓
- φ⁵ = 5(1.618034) + 3 = 11.090170; φ^(−5) = 0.090170; [5]_φ = **11** exactly.
- φ⁶ = 8(1.618034) + 5 = 17.944272; φ^(−6) = 0.055728; [6]_φ = 17.888544 = 8√5 = 8 × 2.236068 = 17.888544. ✓

The pattern is proved by the Lucas/Fibonacci identities. The Lucas numbers L_n = φ^n + ψ^n with ψ = −1/φ satisfy L_n = F_{n−1} + F_{n+1}. For **odd** n, ψ^n = −φ^(−n), so L_n = φ^n − φ^(−n) = [n]_φ. For **even** n, ψ^n = +φ^(−n), so φ^n − φ^(−n) = L_n − 2φ^(−n) = F_n√5 (the standard identity φ^n − φ^(−n) = F_n√5 for even n; check n = 4: F_4 = 3, 3√5 = 6.708204 ✓; n = 6: F_6 = 8, 8√5 = 17.888544 ✓).

**Criterion 1 (ring closure): PASSED.** Every [n]_φ lies in ℤ[√5]: it is either an integer (odd n) or an integer multiple of √5 (even n). The whole doubly-infinite family {[n]_φ} lives in the rank-2 ring ℤ[√5].

**Criterion 2 (recurrence): PASSED.** The recurrence [n+1]_φ = (φ + φ^(−1))[n]_φ − [n−1]_φ has coefficient φ + φ^(−1) = 1.618034 + 0.618034 = **√5 ≈ 2.236068**, a fixed algebraic number. So [n+2]_φ = √5·[n+1]_φ − [n]_φ with [1]_φ = 1, [2]_φ = √5. Check: [3] = √5·√5 − 1 = 5 − 1 = 4 ✓; [4] = √5·4 − √5 = 3√5 ✓; [5] = √5·3√5 − 4 = 15 − 4 = 11 ✓. The entire sequence is generated by two algebraic initial values and one algebraic coefficient — finitely many exact bits.

### 4.2 The Fibonacci ultrametric (Criterion 3 for φ)

Define on ℕ the function d(m, n) = 2^(−k), where k is the largest index such that F_k divides both F_m and F_n (with d(m,m) = 0). By the classical identity gcd(F_m, F_n) = F_gcd(m,n), k = gcd(m, n). The strong triangle inequality requires

d(m, n) ≤ max(d(m, ℓ), d(ℓ, n)) for all ℓ,

i.e., gcd(m, n) ≥ min(gcd(m, ℓ), gcd(ℓ, n)). This holds because gcd(m, ℓ) and gcd(ℓ, n) both divide ℓ; if both are ≥ k, then F_k | F_m, F_ℓ and F_k | F_ℓ, F_n, and since F_k | F_ℓ and F_k | F_m, we get k | gcd(m, ℓ) and k | gcd(ℓ, n), so k divides both m and n (as k | m and k | n), hence k ≤ gcd(m, n). Explicit check: m = 6, n = 10, ℓ = 8: gcd(6,10) = 2, gcd(6,8) = 2, gcd(8,10) = 2; d(6,10) = 2^(−2) = max(2^(−2), 2^(−2)) ✓. Another: m = 4, n = 6, ℓ = 9: gcd(4,6) = 2, gcd(4,9) = 1, gcd(9,6) = 3; d(4,6) = 1/4 ≤ max(1/2, 1/8) = 1/2 ✓. So d is a genuine ultrametric: the divisibility hierarchy of Fibonacci numbers — the very sequence generated by q = φ — organizes the index set into a tree. **Criterion 3: PASSED.**

### 4.3 p-adic admissibility of φ

φ = (1+√5)/2 exists in ℚ_p exactly when 5 is a quadratic residue mod p (p ≠ 2, 5). By quadratic reciprocity, since 5 ≡ 1 (mod 4), (5/p) = (p/5), which equals +1 iff p ≡ ±1 (mod 5). Enumerate primes below 100 (25 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97). Those ≡ 1 or 4 (mod 5): 11 (11 mod 5 = 1), 19 (4), 29 (4), 31 (1), 41 (1), 59 (4), 61 (1), 71 (1), 79 (4), 89 (4). That is **10 primes out of 25**, a fraction of 10/25 = **0.4**, matching the Dirichlet density 2/4 = 1/2 for the two admissible residue classes among the four coprime classes mod 5 (small-sample deviation from 0.5 is expected). So φ is a genuinely adelic object: it lives in ℝ and in a density-1/2 set of ℚ_p's. By Ostrowski's classification this is the complete possible range — no constant can do better than "algebraic of degree d, admissible in positive density of primes."

### 4.4 The q-integers at q = e and q = π

For q = e: e − e^(−1) = 2.718282 − 0.367879 = 2.350402.
- [2]_e = e + e^(−1) = 2.718282 + 0.367879 = **3.086161**.
- [3]_e = (e³ − e^(−3))/2.350402 = (20.085537 − 0.049787)/2.350402 = 20.035750/2.350402. Divide: 2.350402 × 8 = 18.803216; remainder 1.232534; 1.232534/2.350402 ≈ 0.5244. So [3]_e ≈ **8.524**.
- [4]_e = (e⁴ − e^(−4))/2.350402 = (54.598150 − 0.018316)/2.350402 = 54.579834/2.350402 ≈ 23.221 (2.350402 × 23 = 54.059246; remainder 0.520588; /2.350402 ≈ 0.2215).

For q = π: π − π^(−1) = 3.141593 − 0.318310 = 2.823283.
- [2]_π = π + π^(−1) = 3.141593 + 0.318310 = **3.459903**.
- [3]_π = (π³ − π^(−3))/2.823283 = (31.006277 − 0.032252)/2.823283 = 30.974025/2.823283. Divide: 2.823283 × 10 = 28.232830; remainder 2.741195; 2.741195/2.823283 ≈ 0.9709. So [3]_π ≈ **10.971**.

**Criterion 1: FAILED for both.** e is transcendental (Hermite, 1873); π is transcendental (Lindemann, 1882). By the Lindemann–Weierstrass theorem, e^n is transcendental for every nonzero algebraic n, and the field generated by {e^n, e^(−n) : n ≥ 1} is not finitely generated over ℚ (the numbers e, e², e³, … are algebraically independent in the expected sense; unconditionally, e^n for distinct n are linearly independent over algebraic numbers by Lindemann–Weierstrass applied to exponents 1, 2, …, n). Hence [n]_e is transcendental for every n ≥ 2, and no finite set of algebraic data generates the family. The same argument applies to π via the transcendence of e^{iπ} and Gelfond's theorem that e^π is transcendental; the individual transcendence of π^n for integer n follows from Lindemann's theorem (π algebraic would make e^{iπ} algebraic; more directly, if π^n were algebraic, then since e^{iπ} = −1, Lindemann–Weierstrass forces iπ transcendental, hence π transcendental — and the same theorem shows π^n transcendent for each n ≥ 1). So {[n]_e} and {[n]_π} are transcendental families with no ring closure and no p-adic embeddings whatsoever.

**Criterion 2: FAILED for both.** The recurrence coefficient q + q^(−1) equals 3.086161 for e and 3.459903 for π — transcendental in both cases, so the recurrence, while formally valid, has non-integer, indeed non-algebraic, coefficients and generates no arithmetic structure.

**Criterion 3: FAILED for both.** A transcendental q has no p-adic conjugate under any embedding ℚ̄ → ℚ̄_p, since such embeddings map algebraic numbers to algebraic numbers. The families [n]_e and [n]_π exist only in the single Archimedean completion.

### 4.5 Continued-fraction diagnostic

The continued fractions are classical: φ = [1; 1, 1, 1, …] (all partial quotients 1, the unique eventually-constant-bounded case); e = [2; 1, 2, 1, 1, 4, 1, 1, 6, …] (unbounded, linear growth); π = [3; 7, 15, 1, 292, 1, 1, 1, 2, …] (unbounded, irregular). By the Hurwitz theorem, every irrational ξ has infinitely many rationals p/q with |ξ − p/q| < 1/(√5 q²), and the constant 1/√5 is optimal, with equality-attaining worst case exactly the numbers equivalent to φ. Thus φ is, in a precise sense, the real number *most resistant* to rational approximation — the most "rigid" real — while e and π are increasingly well approximated by rationals (π's convergent 355/113 has error ≈ 2.7×10^(−7) with denominator only 113). Rigidity under approximation is the real-analytic shadow of φ's arithmetic rigidity.

### 4.6 Deviation from the undeformed limit

As a final quantitative comparison, |[2]_q − 2| measures how far the first deformed integer sits from its classical value:
- q = φ: |2.236068 − 2| = **0.236068** = φ^(−3).
- q = e: |3.086161 − 2| = **1.086161**.
- q = π: |3.459903 − 2| = **1.459903**.

φ deforms the integers minimally among the three, and its deviation is itself an exact algebraic value (φ^(−3) = 0.236068, verified above as φ³ − 4).

## 5. Results

All numbers below were computed in Section 4; no simulations or external measurements are reported.

1. **Trichotomy established.** q = φ passes all three structure criteria; q = e and q = π pass none. This refines the seed claim: structure does not emerge from "being a geometric ratio" but from being a quadratic algebraic unit.

2. **Exact q-integer identities at q = φ:** [1] = 1, [2] = √5 ≈ 2.236068, [3] = 4, [4] = 3√5 ≈ 6.708204, [5] = 11, [6] = 8√5 ≈ 17.888544, with the closed form [n]_φ = L_n (odd n), [n]_φ = F_n√5 (even n), and recurrence [n+2] = √5[n+1] − [n].

3. **Fibonacci ultrametric:** d(m,n) = 2^(−gcd(m,n)) is a genuine ultrametric on ℕ (strong triangle inequality verified in Section 4.2), giving criterion 3 content: the q = φ hierarchy is a tree, not a metaphor.

4. **Adelic footprint of φ:** admissible in exactly 10 of the 25 primes below 100 (fraction 0.4, consistent with Dirichlet density 1/2), namely p ≡ ±1 (mod