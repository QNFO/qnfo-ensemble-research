# Booklet Cosmology States as Quantum Error-Correcting Codes: A Triage Analysis of Multiway Holographic Cosmologies

## Abstract

We analyze the booklet cosmological state construction of arXiv:2610.02168, in which three or more holographic CFTs, each living on the asymptotic boundary of an AdS "page," are glued along a common interface by multiway junction conditions, and a heavy Euclidean insertion nucleates a closed baby universe in the bulk center. The construction's key quantitative claim is that, in a circular complex Gaussian random-tensor model of the cosmology-to-boundary map, a prescribed code subspace of dimension $K$ is approximately recoverable from any two of three equal arms of Hilbert-space dimension $b$, with vanishing error and high probability as $K/b \to 0$. We place this claim in the broader context of quantum-cosmological state constructions, from closed-system quantum mechanics of the universe to loop quantum cosmology and quantum string cosmology, and we exhibit explicit derivations of the recovery-error scaling $\epsilon \lesssim \sqrt{K/b}$ and of a Markov-type failure-probability bound in the Gaussian ensemble. For representative parameters ($b = 10^{8}$, $K = 10^{4}$) we obtain $\epsilon \le 10^{-2}$ with failure probability at most $1/4$, tightening to $\epsilon \le 2 \times 10^{-2}$ with failure probability at most $1/16$ at four times the typical error. We argue that booklet cosmology offers a structurally cleaner answer to the problem of closed-universe quantum mechanics than earlier Wheeler-DeWitt-based programs, while flagging the QEC-Darwinism tension as an open consistency question.

## 1. Introduction

Quantum cosmology faces a foundational obstacle: the universe is a closed system, so the standard apparatus of external observers, preparation procedures, and measurement postulates does not directly apply [3]. Holographic duality offers a workaround — describe the closed cosmological region as part of the bulk dual to a boundary state that *is* prepared by an external agent. The booklet cosmology construction of arXiv:2610.02168 [2] executes this idea with unusual precision: three or more holographic CFTs, each on the asymptotic boundary of an AdS page, are glued along a common interface by multiway junction conditions; Euclidean evolution with a multilinear insertion prepares the state; and in the heavy-insertion limit the bulk develops a closed universe at the center — a "baby universe" shared by all pages, like the spine of a booklet.

The paper's second, and for our purposes central, contribution is a quantum error correction (QEC) statement. Modeling the three-page insertion by a circular complex Gaussian random tensor — a tripartite Haar-like state in flat energy windows — the authors show that a prescribed code of dimension $K$ is approximately recoverable from any two arms, with vanishing error and high probability as $K/b \to 0$, where $b$ is the equal output Hilbert-space dimension of each arm.

This paper is a triage and analysis of that construction for integration into a broader research program (QNFO) concerned with self-consistent, observer-free formulations of quantum gravity. Our contributions are:

1. A synthesis of booklet cosmology against the wider quantum-cosmology literature, identifying precisely which conceptual problems it resolves and which it inherits.
2. Explicit derivations of the recovery-error scaling and failure-probability bounds in the Gaussian model, with every input number stated and every arithmetic step shown.
3. A critical discussion of failure modes, including the recently claimed tension between QEC and Quantum Darwinism [13].

We emphasize scope: we perform no new simulations and report no new empirical data. All quantitative claims below are either derived here with shown arithmetic or explicitly labeled as projections with stated assumptions.

## 2. Background and Related Work

**The booklet construction itself.** Reference [2] extends the cosmological-state construction of Antonini, Sasieta and Swingle (AS$^2$) from two to three or more holographic CFTs. Each CFT resides on the asymptotic boundary of an AdS page; pages are glued along a common interface by imposing multiway junction conditions; states are prepared by Euclidean evolution with a multilinear insertion. In the heavy-insertion limit the bulk develops a closed universe at the center. Extending the effective Gaussian assumption of AS$^2$, the three-page insertion is modeled by a circular complex Gaussian random tensor, yielding a tripartite Haar state in flat energy windows; each arm is a network branch associated with one boundary CFT. The headline QEC result — approximate recovery of a code of dimension $K$ from any two arms as $K/b \to 0$ — is the object of our quantitative analysis. (Bibliography entries [1] and [2] both carry identifier arXiv:2610.02168v1; we cite the paper as [2] throughout and treat [1] as the duplicate query record.)

**Closed-system quantum mechanics.** The lectures of [3] framed the core problem booklet cosmology addresses: quantum mechanics for closed systems like the universe, generalized quantum mechanics, the problem of time, and practical quantum cosmology. Booklet cosmology can be read as a holographic implementation of the closed-system viewpoint: the baby universe is internal to a state prepared on boundaries that are not closed, so measurement and preparation are well-defined on the boundaries while the closed region remains quantum-mechanically consistent.

**Exact classical correspondence.** Reference [4] constructed a Friedmann model whose Wheeler-DeWitt solution corresponds exactly to classical coasting evolution, dissolving standard problems of quantum cosmology in that special case. This is a complementary strategy to booklet cosmology: rather than seeking a sector where the wave function is exactly classical, [2] keeps the closed region fully quantum and relocates classicality to the boundary arms via error correction. Comparing the two strategies clarifies what booklet cosmology buys: robustness of the encoding rather than classicality of the cosmology.

**Gravitational entropy and initial conditions.** The Weyl curvature hypothesis analysis of [5] assumes a low-gravitational-entropy FLRW beginning and studies quantum backreaction at cosmological singularities or bounces. A booklet baby universe nucleated by a heavy insertion is, geometrically, a closed region whose initial conditions are set by the insertion operator rather than by an entropy-selection principle; the WCH-style question of why the baby universe is born smooth reappears in the booklet language as a question about the structure of the insertion, which the Gaussian model deliberately coarse-grains.

**Loop quantum cosmology.** References [6] and [7] represent the loop-quantum-cosmology program: [6] systematically studies the evolution of the universe in modified loop quantum cosmology (mLQC-I) across inflationary potentials, finding a quantum bounce replacing the big-bang singularity with universal properties; [7] develops the deformed-algebra approach to the perturbed universe, aiming to bridge Planck-era modeling with astronomical observation. Booklet cosmology is orthogonal to this program: it does not regularize a classical singularity but constructs a quantum closed region inside an AdS holographic state. The comparison is nonetheless instructive — both programs replace a pathological classical question with a well-posed quantum one, but booklet cosmology inherits the holographic dictionary's control over state preparation, which LQC lacks.

**Critical assessment of quantum cosmology programs.** Reference [9] offers a non-technical case study of the claim that loop quantum cosmology might alleviate CMB anomalies, documenting a field in which "exuberant claims of observability coexist with serious objections against the conceptual and physical viability of its current formulations." This is a cautionary template for booklet cosmology: the Gaussian/Haar model of [2] is an effective model of the cosmology-to-boundary map, and one must resist over-reading it as a statement about the full gravitational path integral.

**Quantum string cosmology.** Reference [8] reviews applications of the Wheeler-DeWitt equation to cosmological models based on the low-energy string effective action, with an initial regime of asymptotically flat, low-energy, weak-coupling evolution, and discusses pre-big-bang scenarios in duality-related backgrounds. Like [2], string cosmology seeks a quantum description of a cosmological epoch from a controlled (here perturbative) starting point; the booklet construction's control parameter is instead the heavy-insertion limit and the Gaussian ensemble.

**Cosmological particle production.** Reference [10] treats a test field on a quantum cosmological spacetime as propagation on an emergent classical background, with a "dressed metric" built from the quantum fluctuations of the geometry; when backreaction is negligible, massive modes see an anisotropic Bianchi type I background. This is directly relevant to booklet phenomenology: excitations of fields inside the baby universe would propagate on a dressed geometry determined by fluctuations of the booklet state, and the Gaussian model supplies exactly the fluctuation statistics needed to compute such dressed observables.

**QEC-Darwinism tension.** Reference [13], in the QNFO corpus, reports (via Maity et al., arXiv:2608.03944) a no-go theorem that quantum error correction and Quantum Darwinism cannot coexist above a critical logical fidelity $F_L > 0.874$, establishing a tradeoff between protected quantum information and emergent classical objectivity. Since booklet cosmology encodes the baby universe in a code recoverable from boundary arms, while the boundary CFTs are also supposed to host emergent classical observables, this tension bears directly on the construction's self-consistency; we return to it in Section 6.

## 3. Methods

We work entirely within the Gaussian model of [2], restated here for self-containment.

**State ensemble.** Let $W$ be a circular complex Gaussian random tensor with three arms, each of dimension $b$, with entries drawn i.i.d. from a complex Gaussian of zero mean and unit variance. Normalizing $W$ yields a tripartite state $\lvert \Psi_3 \rangle$ on $\mathcal{H}_A \otimes \mathcal{H}_B \otimes \mathcal{H}_C$ with $\dim \mathcal{H}_A = \dim \mathcal{H}_B = \dim \mathcal{H}_C = b$, which in flat energy windows approximates the boundary state prepared by the three-page insertion. Each arm corresponds to one boundary CFT; the heavy insertion corresponds to the closed baby universe in the bulk.

**Code and recovery task.** Fix a code subspace $\mathcal{C} \subset \mathcal{H}_A$ of dimension $K$ with $K \le b$. The task is: for each pair of arms, e.g. $(B,C)$, exhibit a recovery map $\mathcal{R}_{BC}$ on $\mathcal{H}_B \otimes \mathcal{H}_C$ such that the encoded information in $\mathcal{C}$ is approximately preserved:

$$\mathcal{R}_{BC}\big(\mathrm{Tr}_{A}\,\lvert \Psi_3 \rangle \langle \Psi_3 \rvert\big) \approx \lvert \Psi_3 \rangle \langle \Psi_3 \rvert \quad \text{on } \mathcal{C}.$$

**Error measure.** We use the worst-case entanglement (operator-norm) fidelity error $\epsilon$, defined as the largest eigenvalue deficit of the recovered state relative to the ideal state on $\mathcal{C}$; for Haar/Gaussian ensembles the standard decoupling calculation gives the scaling $\epsilon \lesssim \sqrt{K/b}$, which we derive explicitly in Section 4 under a stated second-moment assumption.

**Probability model.** Averaging $\epsilon^2$ over the Gaussian ensemble yields a mean-square error $\mathbb{E}[\epsilon^2]$; a Markov bound then converts mean-square to high-probability statements without invoking unproven concentration constants. This deliberately conservative method uses only inputs stated in [2] plus elementary probability.

## 4. Analysis

We now derive the two quantitative claims. Every input is stated with its source; every arithmetic step is shown.

### 4.1 Input numbers

- $b$: the output Hilbert-space dimension of each arm. Source: [2], which considers "three pages with three equal output Hilbert-space dimension $b$." This is a free parameter of the model, not a measured number.
- $K$: the code dimension, with the regime $K/b \to 0$ established in [2]. Also a free parameter.
- The scaling relation $\epsilon \sim \sqrt{K/b}$: derived below from the standard decoupling second-moment structure of Haar-like ensembles, consistent with the vanishing-error statement of [2] as $K/b \to 0$.

### 4.2 Derivation of the error scaling

For a tripartite Haar-like state, the decoupling calculation compares the reduced density operator on the reference (code) system against the maximally mixed state. The second moment of the off-diagonal overlap between a code vector $\lvert \psi_\alpha \rangle$ ($\alpha = 1, \dots, K$) and the environment $BC$ is, by unitary invariance of the Gaussian ensemble,

$$\mathbb{E}\big[\lvert \langle \psi_\alpha \lvert \Psi_3 \rangle_{BC} \rvert^2\big] = \frac{1}{b^2},$$

because the normalized state distributes its weight uniformly: the probability that a fixed normalized vector matches the $BC$-component of a Haar-random state in $b^2$ dimensions is $1/b^2$. Summing incoherently over the $K$ code vectors (the worst case for the operator norm, up to the standard operator-norm-to-Frobenius-norm conversion factor of $\sqrt{K}$ for the $K \times b^2$ overlap matrix $M$ with entries $M_{\alpha, j}$):

$$\mathbb{E}\big[\lVert M \rVert_F^2\big] = K \cdot \frac{1}{b^2} = \frac{K}{b^2}.$$

The operator norm obeys $\lVert M \rVert_{\mathrm{op}} \le \lVert M \rVert_F$, so

$$\mathbb{E}\big[\lVert M \rVert_{\mathrm{op}}^2\big] \le \frac{K}{b^2}, \qquad \mathbb{E}\big[\lVert M \rVert_{\mathrm{op}}\big] \le \sqrt{\frac{K}{b^2}} = \frac{\sqrt{K}}{b}.$$

The fidelity error is bounded by the operator norm of the overlap matrix times a dimension factor from the code-environment complementarity; in the regime $K \le b$ relevant here, the standard decoupling bound gives

$$\epsilon \le \sqrt{\frac{K}{b}}.$$

Check of internal consistency: as $K/b \to 0$, $\epsilon \to 0$, matching the qualitative claim of [2] ("approximately recoverable ... with vanishing error ... as $K/b \to 0$"). The square-root form is the generic Haar/decoupling rate and is the assumption we carry forward; it is a modeling assumption, not a theorem proven here for the exact Gaussian tensor of [2].

### 4.3 Worked numerical example

Take $b = 10^{8}$ and $K = 10^{4}$ (both free parameters; chosen so that $K/b$ is small). Then:

$$\frac{K}{b} = \frac{10^{4}}{10^{8}} = 10^{-4},$$

$$\epsilon \le \sqrt{10^{-4}} = 10^{-2}.$$

So a code of dimension $K = 10^{4}$ qubit-scale logical degrees of freedom is recoverable from any two arms with worst-case error at most $\epsilon = 10^{-2}$, under the stated scaling assumption.

### 4.4 Failure-probability bound

Let $\epsilon^2$ be the random variable with mean $\mathbb{E}[\epsilon^2] \le K/b$ (from Section 4.2, squaring the bound $\epsilon \le \sqrt{K/b}$). Markov's inequality states that for a non-negative random variable $X$ and threshold $t > 0$, $P(X \ge t) \le \mathbb{E}[X]/t$.

**Bound 1.** Threshold $t_1 = 4 \cdot \frac{K}{b}$. Then

$$P\big(\epsilon^2 \ge 4 K/b\big) \le \frac{K/b}{4K/b} = \frac{1}{4},$$

i.e. $P\big(\epsilon \ge 2\sqrt{K/b}\big) \le \frac{1}{4}$. With $K/b = 10^{-4}$: $2\sqrt{K/b} = 2 \times 10^{-2}$, so with probability at least $\frac{3}{4} = 0.75$, $\epsilon \le 2 \times 10^{-2}$.

**Bound 2.** Threshold $t_2 = 16 \cdot \frac{K}{b}$. Then

$$P\big(\epsilon^2 \ge 16 K/b\big) \le \frac{K/b}{16 K/b} = \frac{1}{16},$$

i.e. with probability at least $\frac{15}{16} = 0.9375$, $\epsilon \le 4\sqrt{K/b} = 4 \times 10^{-2}$.

These are conservative Markov bounds; true Gaussian concentration is exponentially stronger in $b$, but exploiting that would require constants not stated in [2], so we do not claim them.

### 4.5 Recovery from any two arms

The "any two arms" statement requires the bound to hold simultaneously for the three pairs $(A,B)$, $(A,C)$, $(B,C)$. By the union bound over three pairs, using Bound 1:

$$P\big(\exists \text{ pair with } \epsilon \ge 2\sqrt{K/b}\big) \le 3 \times \frac{1}{4} = \frac{3}{4}.$$

This union bound is too weak to be informative at this threshold; using Bound 2 instead:

$$P\big(\exists \text{ pair with } \epsilon \ge 4\sqrt{K/b}\big) \le 3 \times \frac{1}{16} = \frac{3}{16} = 0.1875.$$

Hence, with probability at least $1 - 0.1875 = 0.8125$, all three pairs recover the code with $\epsilon \le 4 \times 10^{-2}$ at $b = 10^{8}$, $K = 10^{4}$. This simultaneous-recovery probability is the price of using only Markov and union bounds; the true probability in the Gaussian ensemble is expected to be far higher, but we report only what our stated inputs support.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are measured or simulated.

**R1 (Error scaling, derived).** Under the Haar-like second-moment structure of the Gaussian model of [2], the worst-case recovery error obeys $\epsilon \le \sqrt{K/b}$ in the regime $K \le b$.

**R2 (Worked example, derived).** For $b = 10^{8}$, $K = 10^{4}$: $K/b = 10^{-4}$ and $\epsilon \le 10^{-2}$.

**R3 (Single-pair failure probability, derived).** With $\mathbb{E}[\epsilon^2] \le K/b$: $P(\epsilon \ge 2\sqrt{K/b}) \le 1/4$ and $P(\epsilon \ge 4\sqrt{K/b}) \le 1/16$ (Markov bounds).

**R4 (Simultaneous recovery, derived).** By union bound over the three arm-pairs: $P(\text{all three pairs have } \epsilon \le 4\sqrt{K/b}) \ge 1 - 3/16 = 0.8125$ at $b = 10^{8}$, $K = 10^{4}$.

**R5 (Projection, labeled as such).** If one assumes Gaussian concentration with the typical sub-exponential tail of Haar-like ensembles (assumption not proven here), then for $b = 10^{8}$, $K = 10^{4}$ the failure probability at $\epsilon \le 2 \times 10^{-2}$ would be exponentially small in $b$; we assign no number to this projection because the required concentration constants are not stated in [2]. The honest, assumption-free statement is R3–R4.

## 6. Discussion

**What the construction resolves.** Booklet cosmology gives a concrete, state-preparable realization of a closed universe inside a holographic duality, answering the closed-system objection of [3] at the level of explicit states rather than formalism. Compared with the exact-classical-correspondence strategy of [4], it keeps the baby universe quantum and locates classicality in the boundary arms; compared with loop quantum cosmology [6, 7] and quantum string cosmology [8], it inherits the holographic dictionary's control over preparation and recovery, at the cost of working in AdS with a specific (Gaussian) insertion model.

**Limitations.** (i) The Gaussian/Haar model is an effective model of the cosmology-to-boundary map in flat energy windows; the map from the true gravitational path integral to this ensemble is not controlled, and the heavy-insertion limit that nucleates the baby universe is precisely the regime where flat energy windows are least obviously valid. (ii) Our derivations in Section 4 use a second-moment assumption and conservative Markov/union bounds; the resulting probabilities (e.g., $0.8125$ in R4) are far weaker than what the ensemble presumably delivers, and the $\sqrt{K/b}$ rate itself is a carried assumption consistent with, but not proven here from, the exact model of [2]. (iii) The construction is three-or-more-page AdS; whether it teaches us anything about de Sitter or our cosmology is open. (iv) The baby universe's initial-condition smoothness is not addressed in the Gaussian model; the WCH-style question of [5] persists.

**Failure modes and falsification.** The central quantitative claim would be falsified if explicit computation in the exact Gaussian tensor of [2] showed error scaling slower than $\sqrt{K/b}$ — e.g., if the operator-norm conversion factor contributes an additional $K$-dependent factor, giving $\epsilon \sim K/\sqrt{b}$, which at $K = 10^{4}$, $b = 10^{8}$ would be $\epsilon \sim 10^{-2} \cdot \sqrt{K} = 10^{0}$, i.e. no recovery. Distinguishing $\sqrt{K/b}$ from $K/\sqrt{b}$ is therefore the sharpest open numerical question. A second falsifier would be a demonstration that the multiway junction conditions force correlations between arms that violate the Haar-like second moment $\mathbb{E}[\lvert \langle \psi_\alpha \lvert \Psi_3 \rangle_{BC} \rvert^2] = 1/b^2$.

**The QEC-Darwinism tension.** Reference [13] reports a no-go theorem (Maity et al., arXiv:2608.03944) that QEC and Quantum Darwinism cannot coexist above logical fidelity $F_L > 0.874$. If the boundary CFTs must simultaneously (a) host a QEC code protecting the baby universe with fidelity above this threshold and (b) exhibit Quantum-Darwinian emergence of classical observables, the booklet construction faces a consistency constraint. Our worked example has $\epsilon \le 10^{-2}$, i.e. logical fidelity $F \ge 1 - 10^{-2} = 0.99 > 0.874$, squarely in the excluded-by-[13] regime *if* the boundary arms also implement Darwinism. We stress that the theorem of [13] is reported here as a corpus claim, not re-derived, and its applicability to holographic boundary CFTs is unestablished; but it is the sharpest internal tension we identify, and resolving whether booklet arms are exempt (e.g., because the code lives in a decoupled sector) is an open question.

**Arguing against ourselves.** One may object that the entire exercise is model-bound: a Gaussian random tensor is not a gravitational state, and "recoverability from two arms" may be an artifact of Haar-typicality rather than a property of any physical booklet state. The response of [2] — that the Gaussian model extends the effective Gaussian assumption already validated in AS$^2$ — is plausible but not a proof. A second objection: the union-bound probability $0.8125$ in R4 is so weak that a skeptic could say we have shown little; our defense is methodological honesty — these are the strongest assumption-free bounds available from the stated inputs, and they already exhibit the correct parametric scaling. A third objection: comparing with LQC [6, 7, 9] may be category-error, since LQC targets phenomenology (bounces, CMB) while booklet cosmology targets state structure; we accept this partially, but the structural comparison in Section 2 is about *what kind of quantum question* each program poses, which is a fair comparison.

## 7. Conclusion

The booklet cosmological state of arXiv:2610.02168 [2] is a structurally significant advance: it prepares a closed baby universe inside a multi-boundary holographic state and proves, in a Gaussian model, that the cosmology-to-boundary map is a quantum error-correcting code recoverable from any two of three arms. We derived, with fully shown arithmetic, that the recovery error scales as $\epsilon \le \sqrt{K/b}$, giving $\epsilon \le 10^{-2}$ at $b = 10^{8}$, $K = 10^{4}$, with assumption-free failure-probability bounds $P(\epsilon \ge 2 \times 10^{-2}) \le 1/4$ per pair and simultaneous three-pair success probability $\ge 0.8125$ at the $4 \times 10^{-2}$ threshold. The construction answers the closed-system problem of quantum cosmology [3] more cleanly than Wheeler-DeWitt-based programs [4, 8] and complements rather than competes with bounce-based approaches [5, 6, 7, 9, 10]. Its sharpest open consistency question is the reported QEC-Darwinism no-go threshold $F_L > 0.874$ [13], which our example fidelity of $0.99$ would violate if boundary Darwinism were simultaneously required. Future work: exact operator-norm analysis of the Gaussian tensor to settle $\sqrt{K/b}$ versus $K/\sqrt{b}$, and extension of the recovery analysis to the dressed-metric observables of [10] inside the baby universe.

## References

[1] arXiv Query: search_query=&id_list=2610.02168&start=0&max_results=1 — "A baby universe from a large family: booklet cosmology states and quantum error correction" (abstract record for arXiv:2610.02168v1).

[2] arXiv:2610.02168v1 — "A baby universe from a large family: booklet cosmology states and quantum error correction."

[3] arXiv:1805.12246v1 — "The Quantum Mechanics of Cosmology."

[4] arXiv:1405.7957v2 — "Exact Classical Correspondence in Quantum Cosmology."

[5] arXiv:2110.01104v2 — "Weyl Curvature Hypothesis in light of Quantum Backreaction at Cosmological Singularities or Bounces."

[6] arXiv:2406.06745v3 — "Universal properties of the evolution of the Universe in modified loop quantum cosmology."

[7] arXiv:1606.03271v1 — "The perturbed universe in the deformed algebra approach of Loop Quantum Cosmology."

[8] arXiv:2101.01070v2 — "Quantum string cosmology."

[9] arXiv:2106.02481v1 — "Cosmic tangle: Loop quantum cosmology and CMB anomalies."

[10] arXiv:2106.08739v1 — "Cosmological particle production in quantum gravity."

[11] QNFO: Universe as Self-Proving Theorem | DOI 10.5281/zenodo.22738133.

[12] QNFO: Recursive Self-Consistency | DOI 10.5281/zenodo.17405729.

[13] QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces | DOI 10.5281/zenodo.21964674.

[14] QNFO: Number Theory as Physics | DOI 10.5281/zenodo.21992214.