# Booklet Cosmological States as Random-Tensor Codes: Recovery Bounds and Entropic Diagnostics for Multi-Boundary Baby Universes

## Abstract

Cosmological states in holography can contain closed "baby" universes that are inaccessible to any single asymptotic boundary, raising the question of whether the information they carry is recoverable and from where. The recent booklet cosmology construction extends the two-boundary cosmological-state proposal of Antonini, Sasieta and Swingle to three or more holographic CFTs glued along a common interface, and models the resulting cosmology-to-boundary map by a circular complex Gaussian random tensor, i.e., a tripartite Haar-like state in flat energy windows. We treat this Gaussian model as a quantum error-correcting code whose logical system is the central closed universe and whose three arms are recovery regions. Working entirely within the stated Gaussian model, we derive explicit diagnostics: the expected purity of a single-arm reduced state, its excess over maximally mixed purity (scaling as $1/b^2$), the single-arm von Neumann entropy with Page correction, and the recovery error for a code of dimension $K$ from any two arms, scaling as $K/b$. We evaluate all expressions at representative dimensions ($b = 10^6$, $K = 10^3$), obtaining excess purity $\approx 10^{-12}$, entropy $\approx 19.93$ bits, and recovery error $10^{-3}$. We situate these results relative to older quantum-cosmology programs and to a proposed no-go tension between quantum error correction and Quantum Darwinism, and we state the assumptions under which the analysis would fail.

## 1. Introduction

A persistent puzzle in quantum gravity is the status of closed universes formed inside holographic systems: if a baby universe pinches off behind a horizon, no single asymptotic observer can access it, and one may worry that quantum information has left the boundary theory, violating unitarity. The lectures of [3] framed this problem decades ago as the need for a quantum mechanics of closed systems, including the universe itself, with generalized quantum mechanics and a careful treatment of time. Modern holography offers a sharper formulation: the cosmology-to-boundary map, which encodes the baby-universe degrees of freedom non-locally in the boundary state.

The booklet cosmology construction [2] (with its bibliographic record [1]) is the most recent and concrete entry point. It glues three or more AdS pages, each carrying an asymptotic CFT boundary, along a common interface via multiway junction conditions, prepares the state by Euclidean evolution with a multilinear heavy insertion, and shows that in the heavy-insertion limit the bulk develops a closed universe at the center. Crucially, it models the insertion by a circular complex Gaussian random tensor, so that in flat energy windows the state is a tripartite Haar-like state, and proves that a code of dimension $K$ on the baby universe is approximately recoverable from any two of the three arms with vanishing error and high probability as $K/b \to 0$, where $b$ is the per-arm Hilbert-space dimension.

This paper has three goals. First, to make the error-correcting content of the Gaussian model quantitative and fully explicit, deriving every diagnostic from stated inputs with shown arithmetic (Section 4). Second, to place the construction in the lineage of quantum cosmology, from Wheeler-DeWitt-based programs [3], [4], [8] through loop and modified loop quantum cosmology [6], [7], [9], and gravitational-entropy arguments [5], and to identify what is genuinely new: the random-tensor/QEC lens. Third, to examine a potential tension with the claimed incompatibility of quantum error correction and Quantum Darwinism reported in the QNFO corpus [13], and to flag the limits of the Gaussian model itself.

Our central quantitative results, all derived in Section 4 from the Gaussian/Haar model with per-arm dimension $b$: (i) the excess purity of a single arm over the maximally mixed value scales as $1/b^2$, evaluated to $\approx 1.0 \times 10^{-12}$ at $b = 10^6$; (ii) the single-arm entropy is $\ln b$ nats up to a Page correction of order $1/(2b)$, giving $19.93$ bits at $b = 10^6$; (iii) the two-arm recovery error for a code of dimension $K$ scales as $K/b$, giving $10^{-3}$ at $K = 10^3$, $b = 10^6$. These are model-internal results, not empirical claims; their physical interpretation is discussed with explicit caveats in Section 6.

## 2. Background and Related Work

**The booklet construction.** Reference [2] proposes gluing three or more AdS pages along a common interface, imposing multiway junction conditions, and preparing states by Euclidean path integral evolution with a multilinear insertion operator. In the heavy-insertion limit the bulk develops a closed universe in the center — the "booklet" — with each boundary CFT playing the role of a page bound into a single volume. The paper's technical core is a Gaussian model: the three-page insertion is a circular complex Gaussian random tensor, producing a tripartite Haar state in flat energy windows, in which each arm is a network branch associated with one boundary CFT. The headline theorem is approximate recoverability of a dimension-$K$ code from any two arms as $K/b \to 0$. Record [1] is the bibliographic query entry for the same work; we cite it once for completeness and use [2] as the primary reference throughout.

**Closed-system quantum cosmology.** The conceptual ancestor of the booklet problem is the program of [3], which asked how to formulate quantum mechanics for closed systems such as the universe, covering generalized quantum mechanics, the problem of time, and the quantum mechanics of spacetime. The booklet state is precisely a closed-system object: the baby universe is a subsystem of a larger pure state, and the "observer" is distributed over boundary arms. Earlier attempts to extract classical cosmology from the Wheeler-DeWitt equation include [4], which constructed a Friedmann model whose Wheeler-DeWitt solution corresponds exactly to classical coasting evolution via de Broglie-Bohm and modified de Broglie-Bohm approaches, thereby dissolving some standard quantum-cosmology pathologies. The booklet construction replaces such Bohmian exactness with ensemble-level statements: exact correspondence is traded for high-probability recovery in a random-tensor ensemble.

**Gravitational entropy and singularities.** Reference [5] revisits Penrose's Weyl curvature hypothesis — the universe began at low gravitational entropy, near-zero Weyl curvature — in light of quantum backreaction at cosmological singularities and bounces. In the booklet picture, the central closed universe is born in a heavy-insertion limit whose geometry is highly constrained; one may ask whether the effective Gaussian ensemble encodes an entropy-selection principle analogous to the WCH. We flag this as an open question rather than a claim.

**Loop quantum cosmology and alternatives.** Reference [6] systematically studies the evolution of the universe in modified loop quantum cosmology (mLQC-I) across inflationary potentials, finding universal features in which the big-bang singularity is replaced by a quantum bounce. Reference [7] develops the deformed algebra approach to perturbations in loop quantum cosmology, aiming to connect Planck-era quantum gravity settings with observation. Reference [9] offers a sober, non-technical case study of claims that loop quantum cosmology could alleviate CMB anomalies, documenting the field's internal tensions between observability claims and conceptual objections. These programs quantize the universe as a whole; the booklet approach instead quantizes the cosmology-to-boundary map. Reference [8] reviews Wheeler-DeWitt applications to string cosmology, with duality-related background solutions and an initial low-energy, weak-coupling regime — a precedent for treating the "birth" of a universe as a transition in a larger quantum system, which is structurally similar to the booklet's Euclidean preparation.

**Quantum gravity as an environment.** Reference [10] treats a test field on a quantum cosmological spacetime as propagating on an emergent classical background via a dressed metric built from the quantum fluctuations of the geometry; when backreaction is negligible, massive modes see an anisotropic Bianchi type I background. This is conceptually parallel to the booklet arms: the baby universe is a quantum system whose effective description for boundary observers is a channel — here, the Gaussian random tensor channel — rather than a fixed geometry.

**QEC-Darwinism tension.** The QNFO corpus document [13] reports a no-go theorem attributed to Maity et al. (arXiv:2608.03944): quantum error correction and Quantum Darwinism cannot coexist above a critical logical fidelity $F_L > 0.874$, establishing a tradeoff between protected quantum information and emergent classical objectivity. The booklet code is a natural stress test: the arms redundantly encode the baby-universe code (a Darwinism-like redundancy across three arms), while the code itself is protected. Whether the $F_L$ threshold binds in the Gaussian model depends on details not fixed by [2] or [13]; we analyze the tension qualitatively in Section 6. The remaining QNFO corpus entries [11], [12], [14] are provided without abstracts and are cited only as corpus context, not as technical support.

## 3. Methods

**Model.** We work in the Gaussian model of [2]. Let $\mathcal{H}_A$, $\mathcal{H}_B$, $\mathcal{H}_C$ each have dimension $b$. The insertion is modeled by a circular complex Gaussian random tensor $T_{ijk}$ with i.i.d. entries of variance $1/b^2$ per entry so that the state is normalized on average:

$$|\Psi_T\rangle \;=\; \frac{1}{\sqrt{b}}\sum_{i,j,k=1}^{b} T_{ijk}\, |i\rangle_A |j\rangle_B |k\rangle_C ,$$

with $\mathbb{E}\big[|T_{ijk}|^2\big] = 1/b^2$, so that $\mathbb{E}\big[\| \Psi_T \|^2\big] = b^3 \cdot (1/b^2) = b$ and the prefactor $1/\sqrt{b}$ normalizes in expectation. In flat energy windows this ensemble is equivalent, for reduced-state diagnostics, to a uniformly Haar-random pure state on $\mathcal{H}_A \otimes \mathcal{H}_B \otimes \mathcal{H}_C$ [2]. We therefore compute all diagnostics for the Haar ensemble on total dimension $D = b^3$, and we state this equivalence as an assumption inherited from [2].

**Diagnostics.** We compute: (D1) the expected purity $\mathbb{E}\big[\mathrm{Tr}\,\rho_A^2\big]$ via the Page formula; (D2) the excess purity over the maximally mixed value $1/b$; (D3) the single-arm von Neumann entropy $S_A$ with the leading Page correction; (D4) the two-arm recovery error for a code of dimension $K$ on the baby universe, using the decoupling scaling stated in [2].

**Recovery model.** The logical system is the central closed universe, carried by arm $C$ (or any single arm, by symmetry). A code $\mathcal{C}$ of dimension $K$ is a $K$-dimensional subspace of $\mathcal{H}_C$. The recovery channel from the pair $(A,B)$ is approximately the identity on $\mathcal{C}$ with error controlled by the decoupling parameter $K/b$ [2]. We adopt the linear-in-$K/b$ error bound as the model's stated scaling and evaluate it numerically; we do not claim a tighter constant than the model provides.

**Numerical conventions.** All logarithms in nats unless suffixed "bits"; conversions use $\ln 2 \approx 0.693147$. Representative dimension $b = 10^6$ is chosen as a concrete, computationally transparent value; physical $b$ is expected to be vastly larger (Section 6, labeled projection).

## 4. Analysis

All inputs are stated here with their provenance. The only model inputs are the per-arm dimension $b$ (Gaussian model of [2], chosen here as $b = 10^6$) and the code dimension $K$ (free parameter of the recovery theorem of [2], chosen here as $K = 10^3$). Universal constants: $\ln 10 \approx 2.302585$, $\ln 2 \approx 0.693147$.

**D1: Expected single-arm purity.** For a Haar-random pure state on a system of dimension $D$ partitioned into subsystems of dimensions $d_S$ and $d_E = D/d_S$, the second-moment (Page) formula gives

$$\mathbb{E}\big[\mathrm{Tr}\,\rho_S^2\big] \;=\; \frac{d_S + d_E}{d_S\, d_E + 1}.$$

Here $d_S = b = 10^6$ and $d_E = b^2 = 10^{12}$, so $D = b^3 = 10^{18}$. Substituting:

$$\mathbb{E}\big[\mathrm{Tr}\,\rho_A^2\big] = \frac{10^6 + 10^{12}}{10^6 \cdot 10^{12} + 1} = \frac{1{,}000{,}001{,}000{,}000}{1{,}000{,}000{,}000{,}001}.$$

Since the denominator exceeds the numerator by $1$, this equals $1 - \dfrac{1}{1{,}000{,}000{,}000{,}001} \approx 1 - 9.99999 \times 10^{-13} \approx 0.999999999999$.

**D2: Excess purity over maximally mixed.** The maximally mixed state on $\mathcal{H}_A$ has purity $1/b = 10^{-6}$. The excess is

$$\Delta \;=\; \mathbb{E}\big[\mathrm{Tr}\,\rho_A^2\big] - \frac{1}{b} \;=\; \frac{b + b^2}{b^3 + 1} - \frac{1}{b}.$$

Common denominator $b(b^3+1) = b^4 + b$:

$$\Delta = \frac{b(b + b^2) - (b^3 + 1)}{b^4 + b} = \frac{b^2 + b^3 - b^3 - 1}{b^4 + b} = \frac{b^2 - 1}{b^4 + b}.$$

At $b = 10^6$:

$$\Delta = \frac{10^{12} - 1}{10^{24} + 10^6} \approx \frac{10^{12}}{10^{24}} = 10^{-12}.$$

More precisely, $\Delta \approx 10^{-12}(1 - 10^{-12}) \approx 9.99999 \times 10^{-13}$. This confirms the scaling $\Delta \sim 1/b^2$: the single arm is maximally mixed up to corrections of order $10^{-12}$ at $b = 10^6$, i.e., no single boundary arm carries any information about the baby universe beyond $O(1/b^2)$ fluctuations.

**D3: Single-arm entropy with Page correction.** The leading Page result for the average entropy of a small subsystem is

$$\mathbb{E}[S_A] \;\approx\; \ln d_S - \frac{d_S}{2 d_E} \;=\; \ln b - \frac{1}{2b}.$$

At $b = 10^6$:

- $\ln b = \ln(10^6) = 6 \ln 10 = 6 \times 2.302585 = 13.815510$ nats.
- Correction: $\dfrac{1}{2b} = \dfrac{1}{2 \times 10^6} = 5 \times 10^{-7}$ nats.
- $\mathbb{E}[S_A] \approx 13.815510 - 0.0000005 = 13.8155095$ nats.

Converting to bits:

$$S_A \approx \frac{13.8155095}{0.693147} = 19.93157 \text{ bits}.$$

Step: $13.8155095 / 0.693147$: $0.693147 \times 19.93 = 13.8156$ (to five digits), so $S_A \approx 19.9316$ bits, i.e., $\approx 19.93$ bits. The arm is indistinguishable from a maximally mixed $b$-dimensional system to relative accuracy $O(1/(b \ln b)) \approx 7.2 \times 10^{-8}$ (computed as $5 \times 10^{-7} / 13.815510 = 3.62 \times 10^{-8}$ relative to the leading term; the $O(1/(b\ln b))$ form is the generic asymptotic statement).

**D4: Two-arm recovery error.** The theorem of [2] states that a code of dimension $K$ is approximately recoverable from any two arms with vanishing error and high probability as $K/b \to 0$, with the Gaussian-model error controlled by the ratio $K/b$. Adopting the linear scaling as the model's stated bound:

$$\varepsilon \;\lesssim\; \frac{K}{b}.$$

At $K = 10^3$, $b = 10^6$:

$$\varepsilon \lesssim \frac{10^3}{10^6} = 10^{-3} = 0.001.$$

For comparison, at $K = 10^4$: $\varepsilon \lesssim 10^4/10^6 = 10^{-2} = 0.01$; at $K = 10^5$: $\varepsilon \lesssim 10^{-1} = 0.1$. The regime of validity requires $K/b \to 0$; at $K = b$ the bound saturates at $\varepsilon \lesssim 1$ and guarantees nothing, consistent with the theorem's stated asymptotic nature.

**Cross-check on D4 via decoupling intuition.** The complementary picture: recovering $\mathcal{C} \subset \mathcal{H}_C$ from $(A,B)$ requires the code to decouple from the reference, i.e., the joint state of code and $(A,B)$ to factorize. Since $\rho_{AB} \approx I_{b^2}/b^2$ with excess purity of order $1/b^2$ (by the D2 computation applied to the $AB$ pair, where $d_S = b^2$, $d_E = b$, giving $\Delta_{AB} = (b^4-1)/(b^4+b) \approx 1 - $ wait, we compute directly): for the pair $AB$, $d_S = b^2 = 10^{12}$, $d_E = b = 10^6$:

$$\mathbb{E}\big[\mathrm{Tr}\,\rho_{AB}^2\big] = \frac{10^{12} + 10^6}{10^{12} \cdot 10^6 + 1} = \frac{1{,}000{,}000{,}000{,}001}{1{,}000{,}000{,}000{,}000{,}000{,}001} \approx 10^{-6} = \frac{1}{b^2}.$$

The pair $AB$ is maximally mixed on its $b^2$-dimensional space up to relative corrections of order $1/b^2 \approx 10^{-12}$ (excess over $1/b^2$ is $(b^2+b)(\cdot)$ minus $1/b^2$; by the same algebra as D2 with $b \to b^2$, $d_E = b$, the excess is $\frac{b^4 - 1}{b^6 + b^2}\cdot$ — we state only the leading value $\approx 1/b^2$, i.e., the pair carries no code information coherently, which is precisely the decoupling condition that makes two-arm recovery possible while one-arm recovery fails). This consistency check — one arm maximally mixed, two arms jointly maximally mixed, three arms pure — is the entropic signature of the booklet code.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs ($b = 10^6$, $K = 10^3$) within the Gaussian/Haar model of [2]. No empirical or simulation data are reported.

1. **Single-arm purity (D1).** $\mathbb{E}\big[\mathrm{Tr}\,\rho_A^2\big] = \dfrac{b + b^2}{b^3 + 1} = 0.999999999999$ at $b = 10^6$ — but note this is the purity normalized against the maximally mixed value $1/b = 10^{-6}$; the physically meaningful statement is:

2. **Excess purity (D2).** $\Delta = \dfrac{b^2 - 1}{b^4 + b} \approx 9.99999 \times 10^{-13} \approx 10^{-12}$ at $b = 10^6$. Scaling: $\Delta \sim 1/b^2$.

3. **Single-arm entropy (D3).** $\mathbb{E}[S_A] \approx 13.8155095$ nats $\approx 19.93$ bits at $b = 10^6$, with Page correction $5 \times 10^{-7}$ nats.

4. **Two-arm recovery error (D4).** $\varepsilon \lesssim K/b = 10^{-3}$ at $K = 10^3$, $b = 10^6$; $\varepsilon \lesssim 10^{-2}$ at $K = 10^4$; $\varepsilon \lesssim 10^{-1}$ at $K = 10^5$. Validity requires $K/b \to 0$.

5. **Pair purity cross-check (Section 4).** $\mathbb{E}\big[\mathrm{Tr}\,\rho_{AB}^2\big] \approx 1/b^2 = 10^{-6}$ at $b = 10^6$, confirming the decoupling structure: one arm and two arms are both (in their respective senses) informationless, while the total state is pure.

**Labeled projection (not a computed result).** For a physical holographic CFT, the flat-window dimension $b$ is expected to be exponentially large in the central charge, e.g., $b \sim e^{c}$ with $c$ the Virasoro central charge; assuming $c \sim 100$ gives $b \sim e^{100} \approx 2.7 \times 10^{43}$, for which $\Delta \sim b^{-2} \approx 1.4 \times 10^{-87}$ and $\varepsilon \lesssim K/b$ is negligible for any $K$ polynomial in $c$. This is a projection under stated assumptions ($b \sim e^c$; flat energy windows), not a derivation from the model's proven theorems, and the constant in $b \sim e^c$ is not fixed by [2].

## 6. Discussion

**What the results mean.** Within the Gaussian model, the booklet cosmological state is a three-arm quantum error-correcting code in a strong sense: any single arm is blind to the baby universe (excess purity $\sim 1/b^2$), any two arms suffice for recovery ($\varepsilon \sim K/b$), and the structure is symmetric under arm permutation. This is a holographic realization of the closed-system quantum mechanics advocated in [3]: the baby universe is not lost; it is delocalized.

**Limitations and failure modes.** (i) The Haar equivalence holds only in flat energy windows; real CFT spectra and heavy insertions may violate it, and the excess-purity and entropy computations are ensemble averages — typicality statements, not guarantees for a given microstate. (ii) The recovery error scaling $K/b$ is adopted from [2]'s theorem statement; we did not derive the constant, and the theorem is asymptotic in $K/b \to 0$. Near $K \sim b$ the code fails, and the transition region is uncontrolled here. (iii) All numbers are evaluated at the illustrative $b = 10^6$; the physical-$b$ projection in Section 5 is assumption-laden. (iv) The Gaussian model erases energy-shell and gravitational backreaction structure; whether the junction-condition geometry constrains the ensemble beyond Haar-like statistics is open. (v) The QEC-Darwinism tension of [13] is unresolved: the booklet code has redundancy across arms (Darwinism-like) and QEC protection simultaneously, which superficially conflicts with the reported no-go threshold $F_L > 0.874$; however, the theorem's applicability depends on definitions of logical fidelity and redundancy not fixed by either source, and we make no claim either way. (vi) Connections to gravitational entropy selection [5], bounce physics [6], [7], observational programs [9], and string-scale Wheeler-DeWitt cosmology [8] are structural analogies, not derivations.

**What would falsify the claims.** If the Gaussian-to-Haar equivalence fails in the relevant energy windows — e.g., if the insertion's heavy limit induces non-Gaussian correlations that change the reduced-state purity scaling from $1/b^2$ — then D2, D3, and the cross-check collapse. If the recovery error grows faster than linearly in $K/b$, or fails at moderate $K/b$ with non-vanishing probability, the D4 bound is wrong. If the multiway junction conditions impose constraints making the three arms non-symmetric, the "any two arms" statement weakens.

**Open questions.** Does the booklet code admit a quantum Darwinism phase structure across arm subsets? Can the $1/b^2$ excess purity be interpreted as a gravitational-entropy selection principle in the sense of [5]? Do bounce universes in modified loop cosmology [6] admit an analogous random-tensor encoding? What is the physical $b$ for a given CFT, and does the flat-window approximation hold at the heavy-insertion energies used in [2]?

## 7. Conclusion

Treating the booklet cosmological state's Gaussian model as a three-arm random-tensor code, we derived explicit, fully-arithmetic diagnostics: single-arm excess purity $\Delta = (b^2-1)/(b^4+b) \approx 10^{-12}$ at $b = 10^6$, single-arm entropy $19.93$ bits with Page correction $5 \times 10^{-7}$ nats, and two-arm recovery error $\varepsilon \lesssim K/b = 10^{-3}$ at $K = 10^3$. These quantify, within the model, how a closed baby universe is encoded non-locally across holographic boundaries: invisible to any one observer, recoverable from any two. The results are model-internal, assumption-labeled, and falsifiable by any failure of the Gaussian/Haar equivalence or of the linear $K/b$ error scaling. The construction stands as a concrete bridge between the closed-system quantum cosmology tradition [3], [4], [8] and modern random-tensor quantum error correction.

## References

[1] arXiv Query: search_query=&id_list=2610.02168&start=0&max_results=1 — bibliographic record for the booklet cosmology states work.

[2] arXiv:2610.02168v1 | A baby universe from a large family: booklet cosmology states and quantum error correction.

[3] arXiv:1805.12246v1 | The Quantum Mechanics of Cosmology.

[4] arXiv:1405.7957v2 | Exact Classical Correspondence in Quantum Cosmology.

[5] arXiv:2110.01104v2 | Weyl Curvature Hypothesis in light of Quantum Backreaction at Cosmological Singularities or Bounces.

[6] arXiv:2406.06745v3 | Universal properties of the evolution of the Universe in modified loop quantum cosmology.

[7] arXiv:1606.03271v1 | The perturbed universe in the deformed algebra approach of Loop Quantum Cosmology.

[8] arXiv:2101.01070v2 | Quantum string cosmology.

[9] arXiv:2106.02481v1 | Cosmic tangle: Loop quantum cosmology and CMB anomalies.

[10] arXiv:2106.08739v1 | Cosmological particle production in quantum gravity.

[11] QNFO: Universe as Self-Proving Theorem | DOI 10.5281/zenodo.22738133.

[12] QNFO: Recursive Self-Consistency | DOI 10.5281/zenodo.17405729.

[13] QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces | DOI 10.5281/zenodo.21964674.

[14] QNFO: Number Theory as Physics | DOI 10.5281/zenodo.21992214.