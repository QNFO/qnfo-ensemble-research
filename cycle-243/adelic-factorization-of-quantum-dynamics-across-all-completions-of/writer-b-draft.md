# Adelic Factorization of Quantum Dynamics Across All Completions of ℚ

## Abstract

Quantum mechanics is formulated over the real numbers, but Ostrowski's theorem shows that the rational field ℚ admits one Archimedean completion, ℝ, and infinitely many non-Archimedean completions ℚ_p, one per prime. The specific gap is that no existing framework states what consistency conditions would force a physical theory to live on all completions at once, and none quantifies how local contributions at different places combine. We treat the adelic factorization of quantum dynamics as a conjecture structured by the local–global template of Tate's 1950 thesis, and we develop it in three steps: a formal adelic path integral whose convergence is left open; exact arithmetic verification of the multiplicative product formula |x|_∞ ∏_p |x|_p = 1 for x = 6, 10, 12, and 30; and a worked aggregation of the published gate fidelities of the Tianyan-287 processor (0.9990, 0.9956, 0.9870), giving a mean fidelity of 0.993866̄ (99.39% rounded) and a product fidelity of 0.9816745428 (98.17% rounded), with a mean-minus-product gap of 0.0121921238. The product formula holds exactly in every case computed, which supplies the cleanest known instance of an adelic constraint that is verifiable by hand. In practice, the work offers quantum-hardware benchmarking a multiplicative aggregation convention with an exact arithmetic anchor, and offers the adelic-physics program a falsifiable structural target: any candidate adelic quantum theory must reproduce the product formula as an identity on amplitudes.

## 1. Introduction

Engineers who operate multi-component quantum processors face a concrete aggregation problem today. A superconducting device such as the Tianyan-287 processor, which provides 105 qubits with single-qubit gate fidelity 99.90%, two-qubit gate fidelity 99.56%, and readout fidelity 98.7% [2], is characterized by several independent error rates, and the success probability of a circuit depends on all of them multiplicatively. Choosing how to combine component-level figures of merit — by averaging, by multiplication, or by some other rule — changes which device counts as better and which upgrades are funded. Today this choice is a convention without a theoretical anchor. The same aggregation question appears, in a deeper form, in the foundations of physics: quantum theory is written over ℝ, and nothing in the standard formalism explains why that particular completion of ℚ is singled out.

Ostrowski's theorem classifies the completions of ℚ: every non-trivial absolute value is equivalent either to the standard Archimedean absolute value |·|_∞ or to a p-adic absolute value |·|_p for some prime p [11]. The p-adic absolute value is defined by writing a nonzero rational x as x = p^k · a/b with p ∤ a and p ∤ b, so that |x|_p = p^{-k}; it satisfies the ultrametric inequality |x + y|_p ≤ max(|x|_p, |y|_p), which is strictly stronger than the Archimedean triangle inequality and is the source of the qualitative differences between real and p-adic analysis [11]. The adele ring 𝔸_ℚ is the restricted direct product ℝ × ∏′_p ℚ_p, in which all but finitely many p-adic components lie in ℤ_p [11]. If a physical amplitude could be assigned one factor per place, the global object would be an adelic product

$$
\mathcal{A} \;=\; \prod_{v\in\{\infty,2,3,5,\dots\}} \mathcal{A}_v ,
$$

and the dominance of the Archimedean factor in laboratory experiments would become a consequence of a global consistency condition rather than a fundamental axiom. The prior version of this work proposed exactly this factorization and identified Tate's 1950 thesis as the structural template for it [9]; the template has since been articulated in detail, with four correspondences: local zeta integrals to local quantum dynamics, idele class group integration to global coherence via the product formula, the functional equation to path integral consistency, and the Archimedean factor to the distinguished role of measurement at the ∞-place [11].

What would change if the conjecture holds. For the hardware engineer, a principled rule for combining place-wise figures of merit, anchored in an exact arithmetic identity. For the physicist, a reason to expect observable or structural signatures of the finite-prime factors, and a criterion — reproduction of the product formula — that any candidate adelic quantum theory must satisfy before it can be taken seriously. For the field, an answer to the question "why ℝ?" that is a theorem-shaped target rather than an accident of history.

This paper is a post-publication revision of the earlier version [9]. It strengthens the earlier treatment in three ways: it verifies the multiplicative product formula by explicit arithmetic for more integers than the single prior instance; it derives the fidelity aggregates with every arithmetic step shown; and it states every conjecture as a conjecture, separating exact arithmetic from physical interpretation.

The contributions are:

- An explicit arithmetic verification of the product formula |x|_∞ ∏_p |x|_p = 1 for x = 6, 10, 12, and 30, with every factor computed (Section 4.1), extending the verification for x = 6, 10, 12 reported in [10].
- A formal adelic path integral construction, with the convergence of the infinite product over primes stated as an open problem rather than assumed (Section 3.1, discussed in Section 6).
- Exact derivation, with all intermediate arithmetic, of the mean fidelity 0.993866̄ and the product fidelity 0.9816745428 from the published Tianyan-287 figures [2], and of their gap 0.0121921238 (Sections 4.2 and 4.3).
- A falsifiability analysis identifying which observation would refute the adelic factorization conjecture and which assumptions it rests on (Section 6).

## 2. Background and Related Work

The adelic factorization conjecture draws on two literatures: arithmetic geometry, where adelic objects already enforce global constraints, and quantum information, where concrete numbers and near-term experiments live. We review the specific results used.

**Adelic measures and equidistribution.** The theory of quasi-adelic measures on the projective line gives the sharpest available model of "local data controlled by a global condition." Baker-Rumely and Favre-Rivera-Letelier independently proved an arithmetic equidistribution theorem for points of small height on the Berkovich compactification of ℙ^1 with respect to an adelic measure, and Chambert-Loir proved a more general version for curves [1]. The mechanism is local: for each place v of the number field, the μ_v-energy of the probability measure [S_n]_v is the double average (1/2|S_n|²) ∑_{x≠y} g_{μ_v}(x,y) of a local Green's function, and the theorem establishes that this energy tends to zero at every place simultaneously as the Galois-invariant sets S_n grow [1]. Two technical facts from the same work matter for our construction. First, the quasi-adelic property is stable under scaling: if M_v is scaled by r, the capacity obeys Cap(rM_v) = r² Cap(M_v), and the associated local and external radii scale as r_in(μ_{M_v}) = r_in(M_v)/√Cap(M_v) and r_out(μ_{M_v}) = r_out(M_v)/√Cap(M_v) [1]. Second, the adelic condition is genuinely global: in the analysis of a map f, there is a finite set S of places outside which the local Green's function takes the uniform form G_{F,C,v}(t_1,t_2) = log‖(t_1,t_2)‖_v + c_v, with the constants c_v tied together across places [1]. This is precisely the logical shape we conjecture for quantum amplitudes: local factors, one per place, constrained by a condition that no single place can verify alone.

**Adelic line bundles and rigidity.** A second global-constraint mechanism comes from the arithmetic Hodge index theorem. The second paper in that series extends the Hodge index theorem for adelic line bundles from number fields to finitely generated fields over ℚ, working with the group of isomorphism classes of adelic ℚ-line bundles over a projective variety [4]. The theorem is then applied to obtain a rigidity property of the sets of preperiodic points of polarizable algebraic dynamical systems, where a polarized system is a triple (X, f, L) with f* L = qL for some rational q > 1 [4]. In the proof, the admissible extensions of line bundles associated to two maps are shown to be nef, and a fundamental inequality for nef adelic bundles is applied to conclude that the two maps agree on a Zariski-dense set of preperiodic points [4]. The lesson we import is that adelic data can force rigidity: a condition satisfied at every place can pin down global objects uniquely. If quantum amplitudes carry adelic line-bundle-like structure, the same mechanism would explain why the Archimedean sector cannot be varied independently of the p-adic sectors.

**Adelic groups.** On the group-theoretic side, the category of finite-dimensional compact connected abelian groups (finite-dimensional protori) is equivalent to the category of adelic tori, and each adelic torus G admits a proper short exact sequence 0 → ℚ^n → 𝓛(G) → G → 0 with the adelic exponential as the connecting map [6]. The construction behind this equivalence is itself instructive: it begins with a nonprincipal ultrafilter u on the set of primes, forms the ultraproduct of the finite fields 𝔽_p, and obtains a characteristic-zero field of cardinality 2^{ℵ₀} containing an algebraic closure of its prime field; the ultraproduct of ℤ_p is then a valuation domain [6]. For our purposes the exact sequence supplies a concrete Lie-theoretic handle on adelic phase spaces: an adelic torus has an honest Lie algebra and exponential map, so Hamiltonian flows on adelic groups are definable objects, not merely analogies.

**Counting over discrete structures.** Sums over p-adic lattices and products over places both reduce, in toy models, to counting integer points in polyhedra. In social choice theory, the probability of a voting event under the impartial anonymous culture assumption is computed by counting integral solutions to a system of linear inequalities, a task for which Ehrhart theory was introduced into that field [5]. Because the dimension and complexity of the polyhedra grow rapidly, that work exploits the symmetry of the linear systems to obtain symmetry-reduced lower-dimensional reformulations, from which exact limiting probabilities for large elections with four candidates were computed [5]. The methodological transfer is direct: any future evaluation of an adelic path integral truncated to finitely many places becomes a weighted lattice-point problem of exactly this type, and the symmetry-reduction techniques are reusable.

**Quantum hardware and quantum simulation.** The quantitative anchor of this paper is the Tianyan-287 processor, a cloud-accessible superconducting quantum prototype with 105 qubits and single-qubit, two-qubit, and readout fidelities of 99.90%, 99.56%, and 98.7% respectively [2]. The platform has demonstrated a large-scale random circuit sampling experiment with 74 qubits and 24 cycles using iSWAP-like two-qubit gates arranged in the sequence ABCD–CDAB per cycle, with single-qubit gates drawn from {√X, √Y, √W} [2]. These published figures are the only empirical numbers used in this paper, and they enter solely as inputs to the aggregation arithmetic of Section 4.2.

Two further works connect to the experimental program. The quantum sawtooth map — a kicked system with Hamiltonian H(θ, I; τ) = I²/2 + V(θ) ∑_j δ(τ − jT) — can be simulated on a quantum computer with exponentially efficient circuits built from the forward/backward quantum Fourier transform, and the localization length of the system can be extracted with a quadratic speedup over classical simulation [7]. The authors of that work emphasize that a quantum computer with fewer than 10 qubits can already simulate quantum localization effects and compute the fidelity of quantum motion, making dynamical quantities a demanding testing ground for first-generation processors [7]. This matters here because fidelity of quantum motion is exactly the quantity whose adelic-style aggregation we compute in Section 4.2, and because any p-adic or adelic dynamical prediction would have to be extracted through circuits of this kind. On the theoretical side, consistent dynamics coupling classical and quantum degrees of freedom exists provided it is stochastic: the resulting hybrid dynamics is linear in the hybrid state, completely positive, and trace preserving, and it can be unravelled for efficient simulation of finite-dimensional hybrid systems [8]. Its toy models exhibit stochastic collapses of the quantum degrees of freedom, a trade-off between classical diffusion and quantum decoherence, and energy non-conservation, which that work identifies as a possible experimental signature of fundamental hybrid dynamics [8]. A mixed Archimedean/non-Archimedean quantum evolution, if one exists, would be a hybrid dynamics in this sense, and the stochastic-CP-TP framework is the only known consistent template for it.

**The adelic-physics program.** The conjecture itself descends from a line of internal program documents. The prior version of this paper proposed the factorization 𝒜 = ∏_v 𝒜_v and framed the emergence of ℝ as a global consistency artifact [9]. The Zitterbewegung extension computed the standard Archimedean trembling frequency ω_∞ = 2m_e c²/ħ = 1.5521 × 10²¹ rad s⁻¹ for the electron, verified the product formula |x|_∞ ∏_p |x|_p = 1 exactly for x = 6, 10, and 12, and conjectured a suppression law under which cross-sector interference amplitude is proportional to ∏_p |r|_p, giving a ratio A_int/A_0 = λ_C/ℓ of 3.863 × 10⁻¹³ at ℓ = 1 m [10]. That work is explicit that the suppression law is a conjecture and not a derivation, and that the adelic Dirac equation it postulates has not been derived from an action principle over 𝔸 [10]; we adopt the same standard of honesty here. The template document [11] supplies the structural core we use: the classification of local fields, the definition of the adele ring as a restricted direct product, and the four correspondences between Tate's thesis and adelic quantum mechanics listed in Section 1, together with the observation that the Dragovich program has realized the template for free (quadratic) theories via explicit adelic path integral constructions and that Huang, Stoica, and Zhong have provided an independent proof-of-concept in conformal field theory [11]. Finally, a companion document proposes a depth-breadth-valuation ontology of the physical continuum [12]; we cite it only for the framing that valuations, not metrics, may be the organizing principle of local dynamics, a framing this paper's product-formula arithmetic illustrates concretely.

## 3. Methods

The paper's own method is arithmetic and formal: we state a model, derive exact identities and aggregates from stated inputs, and label every physical interpretation as conjecture. No experiment, simulation, or measurement is performed; the only empirical numbers are the published Tianyan-287 fidelities [2], used as inputs.

### 3.1 Formal adelic path integral

For a quantum system with classical action S[x], the Archimedean path integral is

$$
Z_\infty = \int \mathcal{D}x \; e^{\frac{i}{\hbar} S[x]} .
$$

For each prime p we replace the exponential by the p-adic additive character χ_p, giving

$$
Z_p = \int_{\mathbb{Q}_p} \mathcal{D}x \; \chi_p\!\bigl(S[x]\bigr),
$$

and define the adelic partition function as the formal product

$$
Z_{\mathbb{A}} = Z_\infty \prod_{p\ \mathrm{prime}} Z_p .
$$

We treat this as a definition, not a result. Convergence of the infinite product is an open problem; the adelic-measure techniques of [1] and the adelic-torus exact sequence of [6] are structural analogies and are not shown here to ensure convergence. The template document [11] reports that the Dragovich program has realized this construction for free (quadratic) theories; no quadratic-theory evaluation is performed in the present paper.

### 3.2 Product-formula arithmetic

The multiplicative product formula for the absolute values of ℚ states

$$
|x|_\infty \prod_{p\ \mathrm{prime}} |x|_p = 1 \qquad \text{for every } x \in \mathbb{Q}\setminus\{0\}.
$$

We verify it by direct computation for a set of integers, using the definition |x|_p = p^{-k} when x = p^k · a/b with p ∤ a, p ∤ b [11]. For an integer N with prime factorization N = ∏_p p^{k_p}, the formula reduces to N · ∏_{p | N} p^{-k_p} = 1, since |N|_p = 1 for every prime p that does not divide N. Every step is shown in Section 4.1. This arithmetic is exact and carries no physical content by itself; the physical claim — that amplitude ratios between sectors scale as ∏_p |r|_p — remains the conjecture stated in [10].

### 3.3 Aggregation of published fidelity data

From the processor description [2] we take three fidelities, converted from percentages to decimals:

- $f_1 = 99.90\% = 0.9990$ (single-qubit gate fidelity),
- $f_2 = 99.56\% = 0.9956$ (two-qubit gate fidelity),
- $f_3 = 98.7\% = 0.9870$ (readout fidelity).

We compute two aggregates: the arithmetic mean $\bar{F} = (f_1 + f_2 + f_3)/3$ and the product $F_{\mathrm{prod}} = f_1 f_2 f_3$. The interpretation — that each fidelity is a "local-place" contribution and the product mimics the adelic product over places — is a labeled hypothesis (Section 4.3), not a derivation. The product aggregate is, however, the operationally correct quantity for circuit success probability: a circuit using one gate of each type succeeds with probability f_1 f_2 f_3 under independence, so the arithmetic is physically meaningful regardless of the adelic interpretation.

## 4. Analysis

### 4.1 Product formula: explicit verification

We verify |x|_∞ ∏_p |x|_p = 1 for x = 6, 10, 12, and 30. The cases x = 6, 10, 12 were verified in [10]; we recompute them here and add x = 30.

**Case x = 6.** The integer 6 = 2 · 3, so k_2 = 1 and k_3 = 1, and |6|_p = 1 for all p ∉ {2, 3}. Then

$$
|6|_\infty = 6, \qquad |6|_2 = 2^{-1} = \tfrac{1}{2}, \qquad |6|_3 = 3^{-1} = \tfrac{1}{3}.
$$

The product over all places is

$$
6 \cdot \tfrac{1}{2} \cdot \tfrac{1}{3} = \frac{6}{6} = 1 .
$$

**Case x = 10.** 10 = 2 · 5, so |10|_2 = 1/2, |10|_5 = 1/5, and |10|_p = 1 otherwise:

$$
10 \cdot \tfrac{1}{2} \cdot \tfrac{1}{5} = \frac{10}{10} = 1 .
$$

**Case x = 12.** 12 = 2² · 3, so |12|_2 = 2^{-2} = 1/4, |12|_3 = 1/3, and |12|_p = 1 otherwise:

$$
12 \cdot \tfrac{1}{4} \cdot \tfrac{1}{3} = \frac{12}{12} = 1 .
$$

**Case x = 30.** 30 = 2 · 3 · 5, so |30|_2 = 1/2, |30|_3 = 1/3, |30|_5 = 1/5, and |30|_p = 1 otherwise:

$$
30 \cdot \tfrac{1}{2} \cdot \tfrac{1}{3} \cdot \tfrac{1}{5} = \frac{30}{30} = 1 .
$$

In each case the product equals 1 exactly, with no rounding at any step. The general reason is visible in the computations: for an integer N = ∏_{p|N} p^{k_p}, the Archimedean factor contributes ∏_{p|N} p^{k_p} and the p-adic factors contribute exactly ∏_{p|N} p^{-k_p}, so the two cancel term by term. The number of places at which the product is nontrivial equals the number ω(N) of distinct prime divisors of N: ω(6) = ω(10) = ω(12) = 2 and ω(30) = 3. The formula is therefore an identity whose content is the matching of one Archimedean factor against one p-adic factor per prime divisor — the elementary shadow of the local–global structure that Tate's thesis exploits at a far deeper level [11].

### 4.2 Fidelity aggregates: full arithmetic

All input numbers come from the processor description [2]; none are assumed. The inputs are f_1 = 0.9990, f_2 = 0.9956, f_3 = 0.9870.

**Step 1: the arithmetic mean.** First the sum:

$$
\begin{aligned}
f_1 + f_2 + f_3 &= 0.9990 + 0.9956 + 0.9870 \\
&= (0.9990 + 0.9956) + 0.9870 \\
&= 1.9946 + 0.9870 \\
&= 2.9816 .
\end{aligned}
$$

Then the division:

$$
\bar{F} = \frac{2.9816}{3} = 0.993866\overline{6},
$$

since 3 × 0.993866̄ = 2.9816 exactly (the digit 6 repeats with period 1). As a percentage:

$$
\bar{F}_{\%} = 0.993866\overline{6} \times 100\% = 99.3867\overline{6}\% \approx 99.39\% .
$$

**Step 2: the product.** Multiply the first two factors:

$$
\begin{aligned}
f_1 \times f_2 &= 0.9990 \times 0.9956 \\
&= (1 - 0.0010) \times 0.9956 \\
&= 0.9956 - 0.0010 \times 0.9956 \\
&= 0.9956 - 0.0009956 \\
&= 0.9946044 .
\end{aligned}
$$

Multiply by the third factor:

$$
\begin{aligned}
F_{\mathrm{prod}} &= 0.9946044 \times 0.9870 \\
&= 0.9946044 \times (1 - 0.0130) \\
&= 0.9946044 - 0.0130 \times 0.9946044 \\
&= 0.9946044 - 0.0129298572 \\
&= 0.9816745428 .
\end{aligned}
$$

As a percentage:

$$
F_{\mathrm{prod},\%} = 0.9816745428 \times 100\% = 98.16745428\% \approx 98.17\% .
$$

**Step 3: the gap.**

$$
\bar{F} - F_{\mathrm{prod}} = 0.993866\overline{6} - 0.9816745428 .
$$

Using $\bar{F} = 0.9938666667$ to ten decimal places:

$$
0.9938666667 - 0.9816745428 = 0.0121921239 ,
$$

which agrees with the exact value 0.0121921238̄ to the displayed precision; the exact gap is $\bar{F} - F_{\mathrm{prod}} = 0.012192123\overline{8}$, i.e. about 1.22 percentage points.

### 4.3 Interpretation, with status labels

Three statements must be kept apart.

1. **Exact arithmetic (established here).** The values $\bar{F} = 0.993866\overline{6}$, $F_{\mathrm{prod}} = 0.9816745428$, and the gap 0.0121921238̄ follow from the inputs of [2] by the arithmetic of Section 4.2. The product aggregate is the correct circuit-success probability under independence of the three error sources.

2. **Exact arithmetic (established in [10] and Section 4.1).** The product formula |x|_∞ ∏_p |x|_p = 1 holds exactly for x = 6, 10, 12, 30.

3. **Conjecture (not established).** That each fidelity corresponds to a contribution from a distinct completion — for instance f_1 from ∞, f_2 from ℚ_2, f_3 from ℚ_3 — and that a global adelic amplitude is the product of such local factors. The gap of 1.22 percentage points quantifies how multiplicative aggregation penalizes local imperfections more strongly than averaging in this toy setting; whether the gap carries any physical meaning in a genuine adelic quantum theory is entirely open. Likewise, the conjecture of [10] that cross-sector interference amplitudes scale as ∏_p |r|_p is not derived here.

## 5. Results

All numbers below are computed in Section 4 from stated inputs; none are empirical measurements by this paper, and the fidelity inputs are published figures of the Tianyan-287 processor [2].

1. **Product formula verifications.** |x|_∞ ∏_p |x|_p = 1 holds exactly for x = 6, 10, 12, and 30 (Section 4.1). The number of nontrivial places equals ω(x), the number of distinct prime divisors: ω(6) = ω(10) = ω(12) = 2, ω(30) = 3.

2. **Mean fidelity.** $\bar{F} = 0.993866\overline{6}$, i.e. 99.3867̄%, rounded to 99.39% (Section 4.2, Step 1).

3. **Product fidelity.** $F_{\mathrm{prod}} = 0.9816745428$, i.e. 98.16745428%, rounded to 98.17% (Section 4.2, Step 2).

4. **Aggregation gap.** $\bar{F} - F_{\mathrm{prod}} = 0.012192123\overline{8}$, about 1.22 percentage points (Section 4.2, Step 3).

The two fidelity aggregates are the only quantitative results of this paper beyond the product-formula identities. The exact values, not the rounded percentages, are authoritative. The product fidelity is lower than the mean because multiplication accumulates imperfections across components; this is a general property of independent error sources, not evidence for adelic structure.

## 6. Discussion

### 6.1 Limitations

The conjecture rests on assumptions that must be listed explicitly, because the result is sensitive to each of them.

- **The factorization is postulated, not derived.** No action principle over 𝔸 is written down, and no theorem establishes that a consistent quantum theory must factor over places. The four correspondences of [11] are structural analogies; the Dragovich realizations for free quadratic theories and the conformal-field-theory proof-of-concept cited there are reported results of other programs, not derivations performed here.
- **Convergence of the infinite product is open.** $Z_{\mathbb{A}} = Z_\infty \prod_p Z_p$ is defined formally; without a regularization scheme the product may diverge. The toy fidelity example truncates the product to three "places," which is a drastic simplification: a genuine adelic product runs over all primes.
- **The measure is undefined.** The adelic measures of [1] are built for arithmetic equidistribution on ℙ^1, with local Green's functions and capacities; no analogue for quantum amplitudes is constructed here. Different choices of measure could change the product drastically, and the scaling behavior Cap(rM_v) = r² Cap(M_v) [1] has no established quantum counterpart.
- **The place-to-fidelity map is arbitrary.** Assigning f_1, f_2, f_3 to ∞, ℚ_2, ℚ_3 is a labeling choice with no theoretical justification; any permutation of the assignment leaves the arithmetic unchanged, which shows the assignment carries no content.
- **Sparse empirical input.** The only empirical numbers are three fidelities from one processor [2]. The illustration is not a test of anything.
- **No p-adic experiment exists.** No physical system is known to implement ℚ_p-valued quantum evolution; the p-adic harmonic-oscillator and spin-½ models of the prior version [9] remain formal definitions without derivations.
- **Possible conflict with relativity.** The ultrametric topology of ℚ_p — in which every triangle is isosceles and all balls are simultaneously open and closed [11] — has no established compatibility with Lorentz invariance.
- **Hybrid dynamics is the only known consistent template, and it is stochastic.** If Archimedean and non-Archimedean sectors coexist, their coupling would be a hybrid classical-quantum-style dynamics; the known consistent such dynamics is stochastic, linear, completely positive, and trace preserving, with energy non-conservation as a generic feature [8]. A unitary adelic quantum theory would therefore have to evade, or explain, the stochasticity that the hybrid literature finds necessary.

### 6.2 What would falsify the conjecture

The main result of this paper is exact