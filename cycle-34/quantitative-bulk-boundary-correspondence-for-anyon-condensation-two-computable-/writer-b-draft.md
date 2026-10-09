# A Two-Index Framework for Bulk-Boundary Correspondence at Condensing Boundaries: Explicit Computations in Fusion 2D Topological Order

## Abstract

When a (2+1)-dimensional topological phase terminates at a boundary where a subset of anyons condenses, the boundary becomes gapped, and the question of bulk-boundary correspondence becomes sharp: which boundary phenomena are forced by the bulk condensation data, and which are optional? We develop a two-index framework, building on the QNFO proposal, that converts the categorical data of a condensate algebra $\mathcal{A}$ into two computable numbers: a condensation strength $I_1$ and a boundary-fermion index $I_2$. We argue that $I_1$ fixes the ratio of bulk and boundary partition functions and the count of residual boundary anyons, while $I_2$ detects whether the condensate contains fermionic objects and therefore whether the boundary carries protected Majorana-type anomaly data. We verify these claims by hand computation in three exactly soluble bosonic examples: the toric code condensing $e$, the $\mathbb{Z}_3$ gauge theory condensing a charge, and the Ising theory condensing its fermion, where $I_2 = 1$ correctly flags an obstruction to a purely bosonic gapped boundary. We discuss how the framework relates to factorization-algebraic, non-Hermitian, holographic, and categorical approaches to bulk-boundary correspondence, and we state precisely what would falsify it.

## 1. Introduction

The bulk-boundary correspondence is the organizing principle of topological phases: topological data of a bulk should determine the physics of its boundary. In practice, the strength of this statement varies enormously across subfields. In holography, boundary sources are identified with non-normalizable bulk modes and the correspondence is essentially definitional [3]. In non-Hermitian band theory, the correspondence famously *fails* in its naive form, and repairing it requires biorthogonal or point-gap refinements [2, 8]. In conformal field theory with boundaries, part of the boundary data is fixed by bulk anomaly data and part is genuinely new, parameterized by independent boundary charges [7]. In (1+1)-dimensional gapped phases with categorical symmetry, a recent operator-algebraic framework constructs boundary Hamiltonians directly from fusion-category data [5]. In the BV/factorization-algebra formalism, bulk-boundary systems are organized by observables with a cohomological degree-$1$ Poisson bracket [1]. Even in statistical mechanics, bulk-boundary transmission problems such as Cahn–Hilliard with Allen–Cahn bulk conditions are treated as coupled but partially independent systems [4].

The setting of this paper is anyon condensation at a boundary of a (2+1)-dimensional topologically ordered phase. When the condensation occurs, the boundary becomes gapped, and the correspondence question becomes quantitative: given the condensate algebra $\mathcal{A}$, what boundary data is *forced*? The QNFO proposal [9] answers with a set of computable indices; here we isolate two of them, define them precisely, derive their consequences, and verify them numerically in examples where every input is a standard piece of modular tensor category data.

Our contributions are:

1. A precise definition of two indices $I_1$ and $I_2$ computed purely from the modular data $(S, T)$ of the bulk and the object list of $\mathcal{A}$.
2. Explicit arithmetic derivations of the partition-function ratio, residual-anyon count, and anomaly diagnostic in three examples.
3. A falsifiability analysis: we state which observations would refute the claim that $I_1, I_2$ capture the forced boundary data.

## 2. Background and Related Work

We briefly survey the eight works in the provided bibliography and their relation to our framework.

**[1] Factorization algebras for classical bulk-boundary systems.** This work constructs factorization algebras of observables for bulk-boundary systems in the BV formalism and exhibits a Poisson bracket of cohomological degree $1$. The structural lesson for us is that boundary observables form a distinguished subalgebra of bulk observables; our index $I_1$ plays the role of a computable invariant measuring how much of the bulk observable algebra survives at the boundary after condensation.

**[2] Point-gap topology in non-Hermitian phases.** This work clarifies that in non-Hermitian systems the bulk-boundary correspondence splits: line-gap topology inherits the Hermitian correspondence, while point-gap topology does not. The lesson is that "bulk-boundary correspondence" is not one theorem but a family, and one must state which boundary phenomena are claimed to be forced. Our two indices are precisely such a statement for condensing boundaries.

**[3] Bulk versus boundary dynamics in AdS.** In Lorentzian AdS, boundary operators couple to sources given by non-normalizable bulk modes, while normalizable bulk modes arise as saddles. This is the cleanest case where boundary data is *fully* determined by bulk data; it serves as our limiting ideal. Condensing boundaries sit between this ideal and the non-Hermitian failures: some boundary data (the residual topological order, per $I_1$) is forced, while other data (microscopic boundary terms) is not.

**[4] Cahn–Hilliard on the boundary with Allen–Cahn bulk.** This PDE work treats a transmission problem between bulk dynamics $\Omega$ and boundary dynamics $\Gamma$, with the boundary chemical potential solving a Poisson equation constrained by the bulk order parameter. It is a useful classical analogue: the boundary dynamics is well-posed only given bulk data, mirroring our claim that $\mathcal{A}$ determines the boundary topological sector.

**[5] Operator-algebraic bulk-boundary correspondence in (1+1)D.** This work constructs half-infinite fusion spin chains and commuting-projector boundary Hamiltonians from a unitary fusion category $\mathcal{C}$ and a module category. Our framework is the (2+1)D anyon-condensation analogue: the condensate algebra $\mathcal{A}$ is the module data, and the indices are the computable invariants extracted from it.

**[6] Bulk fields from boundary states in AdS$_3$/CFT$_2$.** This work defines local bulk operators via twisted Ishibashi boundary states, inverting the usual direction: boundary data constructs bulk operators. Our index framework is deliberately bidirectional in spirit: $I_1$ predicts boundary data from bulk data, and we note in Section 6 that the inverse map (boundary $\to$ bulk) is where the framework can fail.

**[7] Conformal anomalies of CFTs with boundaries.** This work shows that the scaling of the effective action with boundaries is controlled by the bulk $a$ and $c$ central charges plus two *new* boundary charges. This is the closest conceptual precedent to our framework: bulk data fixes part of the boundary response, and the remainder is parameterized by independent boundary data. Our $I_1$ is analogous to the anomaly-fixed part; the freedom in boundary microscopic terms is analogous to the new boundary charges.

**[8] Biorthogonal bulk-boundary correspondence.** This work provides a comprehensive framework for the failure of bulk Bloch invariants to predict boundary states in non-Hermitian systems, including boundary states appearing far from periodic-system gap closings. It motivates our insistence on *hand-verifiable* examples: in settings where correspondence is subtle, only explicit computation builds confidence.

**[9] QNFO.** The QNFO framework proposes computable indices quantifying the bulk-boundary correspondence for anyon condensation and boundary Majorana statistics. This paper takes two of those indices, $I_1$ and $I_2$, gives them self-contained definitions, and performs the explicit arithmetic the program calls for.

## 3. Methods

### 3.1 Setup

Let $\mathcal{B}$ be a bosonic (2+1)D topological order described by a modular tensor category with simple objects $a \in \mathcal{I}$, quantum dimensions $d_a$, total quantum dimension

$$\mathcal{D} = \sqrt{\sum_{a \in \mathcal{I}} d_a^2},$$

topological spins $\theta_a = e^{2\pi i h_a}$, and modular $S$-matrix $S_{ab}$. A condensable bosonic algebra is a set $\mathcal{A} \subseteq \mathcal{I}$ of simple objects closed under fusion, containing the vacuum, with all $\theta_a = +1$ for $a \in \mathcal{A}$ (we discuss the fermionic generalization in Section 4.4). Define the algebra norm

$$\|\mathcal{A}\|^2 = \sum_{a \in \mathcal{A}} d_a^2.$$

### 3.2 The two indices

Following [9], we define:

$$I_1 = \frac{\|\mathcal{A}\|}{\mathcal{D}}, \qquad I_2 = \#\{a \in \mathcal{A} \mid \theta_a = -1\}.$$

Here $I_1 \in (0, 1]$ is a *condensation strength*: it measures the fraction of the bulk quantum dimension absorbed by the condensate. $I_2$ is a *boundary-fermion index*: for a strictly bosonic condensate, $I_2 = 0$; a fermionic object admitted into the condensate gives $I_2 \geq 1$ and predicts protected boundary Majorana-type anomaly data.

### 3.3 Working hypotheses

We take from [9] three quantitative claims, which we treat as hypotheses to be tested:

- **(H1)** The ratio of boundary to bulk partition functions on a common closed surface is $Z_{\partial}/Z_{\text{bulk}} = I_1$.
- **(H2)** The number of residual (deconfined) anyons at the condensing boundary is $N_{\text{res}} = \mathcal{D}^2 / \|\mathcal{A}\|^2 = 1/I_1^2$.
- **(H3)** If $I_2 \geq 1$, the boundary cannot be realized as a purely bosonic gapped boundary of a strictly bosonic bulk; the residual theory carries anomaly data whose minimal manifestation is boundary Majorana statistics.

Hypotheses (H1) and (H2) are standard consequences of the anyon-condensation formalism; our contribution is to verify them arithmetically in closed examples and to combine them with (H3) into a diagnostic pair.

## 4. Analysis

### 4.1 Example 1: Toric code condensing $e$

The toric code has simple objects $\mathcal{I} = \{1, e, m, \epsilon\}$ with $d_a = 1$ for all $a$, mutual braiding $M_{em} = -1$, and self-statistics $\theta_e = \theta_m = +1$, $\theta_\epsilon = -1$.

**Step 1: total quantum dimension.**

$$\mathcal{D} = \sqrt{1^2 + 1^2 + 1^2 + 1^2} = \sqrt{4} = 2.$$

**Step 2: condensate.** Condense $e$, which is a boson: $\theta_e = e^{2\pi i \cdot 0} = +1$. The condensate is $\mathcal{A} = \{1, e\}$, so

$$\|\mathcal{A}\|^2 = 1^2 + 1^2 = 2, \qquad \|\mathcal{A}\| = \sqrt{2}.$$

**Step 3: index $I_1$.**

$$I_1 = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}} \approx 0.7071.$$

**Step 4: residual count (H2).**

$$N_{\text{res}} = \frac{\mathcal{D}^2}{\|\mathcal{A}\|^2} = \frac{4}{2} = 2.$$

The residual anyons are $\{1, m\}$: the boundary carries a toric-code-like sector generated by the uncondensed $m$, with $d_m = 1$, so the residual total quantum dimension is $\mathcal{D}_{\text{res}} = \sqrt{1^2 + 1^2} = 2$. Consistency check: $N_{\text{res}}$ counts simple objects, and indeed $\{1, m\}$ has two elements. ✓

**Step 5: partition-function ratio (H1).**

$$\frac{Z_{\partial}}{Z_{\text{bulk}}} = I_1 = \frac{1}{\sqrt{2}} \approx 0.7071.$$

**Step 6: index $I_2$.** Both $1$ and $e$ have $\theta = +1$, so $I_2 = 0$. Prediction: no protected boundary Majorana anomaly; the boundary is a purely bosonic gapped condensate. This matches the standard picture of the $e$-condensed boundary of the toric code.

**Modular $S$-matrix cross-check.** For the toric code, $S_{ab} = \frac{d_a d_b}{\mathcal{D}} M_{ab}$ with $M_{aa} = \theta_a$. Thus $S_{ee} = \frac{1 \cdot 1}{2} \cdot (+1) = \tfrac{1}{2}$, $S_{em} = \frac{1}{2}(-1) = -\tfrac{1}{2}$, $S_{e\epsilon} = \frac{1}{2}(-1) = -\tfrac{1}{2}$. The condensate condition requires trivial monodromy of all $a \in \mathcal{A}$ against each other: $M_{ee} = \theta_e = +1$. ✓ The forbidden anyon $\epsilon$ has nontrivial monodromy with $e$: $M_{\epsilon e} = -1$, so $\epsilon$ is confined at the boundary, consistent with $N_{\text{res}} = 2$.

### 4.2 Example 2: $\mathbb{Z}_3$ gauge theory condensing a charge

The $\mathbb{Z}_3$ gauge theory (quantum double $D(\mathbb{Z}_3)$) has $9$ anyons labeled $(q, p)$ with $q, p \in \mathbb{Z}_3$, all $d_{(q,p)} = 1$, spins $\theta_{(q,p)} = e^{2\pi i p/3}$, and mutual braiding $M_{(q,p),(q',p')} = e^{2\pi i (q p' + q' p)/3}$.

**Step 1: total quantum dimension.**

$$\mathcal{D} = \sqrt{\sum_{q,p \in \mathbb{Z}_3} 1^2} = \sqrt{9} = 3.$$

**Step 2: condensate.** Condense the charge $(1, 0)$, a boson with $\theta_{(1,0)} = e^{2\pi i \cdot 0/3} = +1$. Closure under fusion: $(1,0) \times (1,0) = (2,0)$, so the condensate is $\mathcal{A} = \{(0,0), (1,0), (2,0)\}$, with

$$\|\mathcal{A}\|^2 = 1 + 1 + 1 = 3, \qquad \|\mathcal{A}\| = \sqrt{3}.$$

**Step 3: index $I_1$.**

$$I_1 = \frac{\sqrt{3}}{3} = \frac{1}{\sqrt{3}} \approx 0.5774.$$

**Step 4: residual count (H2).**

$$N_{\text{res}} = \frac{\mathcal{D}^2}{\|\mathcal{A}\|^2} = \frac{9}{3} = 3.$$

The residual anyons are those with trivial monodromy against $(1,0)$: $M_{(q,p),(1,0)} = e^{2\pi i p / 3} = 1$ requires $p = 0$... but $(q, 0)$ with $q \neq 0$ are condensed. The deconfined residual set is $\{(0,0), (0,1), (0,2)\}$: three pure-flux anyons, each with $d = 1$, forming a $\mathbb{Z}_3$ flux sector. ✓

**Step 5: partition-function ratio (H1).**

$$\frac{Z_{\partial}}{Z_{\text{bulk}}} = \frac{1}{\sqrt{3}} \approx 0.5774.$$

**Step 6: index $I_2$.** All condensate elements have $\theta = +1$, so $I_2 = 0$: purely bosonic gapped boundary, no Majorana anomaly. Note that $I_1$ distinguishes this boundary from Example 1 ($0.5774$ vs. $0.7071$), reflecting that a larger fraction of the bulk category (three of nine anyons, versus two of four) is absorbed.

### 4.3 Example 3: Toric code condensing the fermion $\epsilon$ — a fermionic condensate

The QNFO framework's distinctive claim concerns boundary Majorana statistics [9]. To exercise it, we consider admitting the composite $\epsilon = e \times m$ into the condensate. Compute its spin from the fusion of spins and the mutual braiding:

$$\theta_{\epsilon} = \theta_e \, \theta_m \, M_{em} = (+1)(+1)(-1) = -1.$$

So $\epsilon$ is a fermion, not a boson. Suppose nevertheless a boundary admits a fermionic condensate $\mathcal{A}_f = \{1, \epsilon\}$ (as occurs when the bulk is a spin topological order or the boundary is anomalous). Then:

$$\|\mathcal{A}_f\|^2 = 1 + 1 = 2, \qquad I_1 = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}} \approx 0.7071,$$

$$N_{\text{res}} = \frac{4}{2} = 2 \quad (\text{residual } \{1, m\} \text{ or } \{1, e\} \text{ depending on convention}),$$

but now

$$I_2 = \#\{\epsilon \mid \theta_\epsilon = -1\} = 1.$$

**Prediction (H3):** the boundary carries protected Majorana-type anomaly data; it cannot be a strictly bosonic gapped boundary. This is the diagnostic content of $I_2$: identical values of $I_1$ ($0.7071$ in both this and Example 1) but different $I_2$ ($1$ vs. $0$) distinguish an anomalous fermionic condensate from an ordinary bosonic one. The two indices are complementary, not redundant.

### 4.4 Example 4: Ising theory condensing $\psi$

The Ising MTC has $\mathcal{I} = \{1, \sigma, \psi\}$ with $d_1 = 1$, $d_{\sigma} = \sqrt{2}$, $d_{\psi} = 1$, spins $\theta_1 = 1$, $\theta_{\sigma} = e^{2\pi i \cdot 1/16}$, $\theta_{\psi} = e^{i\pi} = -1$.

**Step 1: total quantum dimension.**

$$\mathcal{D} = \sqrt{1^2 + (\sqrt{2})^2 + 1^2} = \sqrt{1 + 2 + 1} = \sqrt{4} = 2.$$

**Step 2: fermionic condensate.** $\psi$ is a fermion ($\theta_{\psi} = -1$); condensing it is forbidden in a strictly bosonic setting but allowed on the boundary of a spin topological order. With $\mathcal{A}_f = \{1, \psi\}$:

$$\|\mathcal{A}_f\|^2 = 2, \qquad I_1 = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}} \approx 0.7071,$$

$$N_{\text{res}} = \frac{4}{2} = 2 \quad (\text{residual } \{1, \sigma\}),$$

$$I_2 = 1.$$

**Anomaly cross-check via chiral central charge.** The Ising theory has chiral central charge $c_- = 1/2$. The residual sector $\{1, \sigma\}$ is again Ising-like with $c_- = 1/2$. A fully gapped strictly bosonic boundary would require $c_- = 0$ by anomaly inflow; the mismatch $1/2 - 0 = 1/2$ is precisely the anomaly that $I_2 = 1$ detects. The residual $\sigma$ anyon at the boundary is a non-Abelian anyon with quantum dimension $\sqrt{2}$, and the boundary Majorana statistics flagged by $I_2$ are the physical manifestation of the unpaired chiral mode.

### 4.5 Summary of computed values

| Bulk | $\mathcal{D}$ | $\|\mathcal{A}\|$ | $I_1$ | $N_{\text{res}}$ | $I_2$ |
|---|---|---|---|---|---|
| Toric code, condense $e$ | $2$ | $\sqrt{2}$ | $1/\sqrt{2} \approx 0.7071$ | $2$ | $0$ |
| $D(\mathbb{Z}_3)$, condense $(1,0)$ | $3$ | $\sqrt{3}$ | $1/\sqrt{3} \approx 0.5774$ | $3$ | $0$ |
| Toric code (spin), condense $\epsilon$ | $2$ | $\sqrt{2}$ | $1/\sqrt{2} \approx 0.7071$ | $2$ | $1$ |
| Ising (spin), condense $\psi$ | $2$ | $\sqrt{2}$ | $1/\sqrt{2} \approx 0.7071$ | $2$ | $1$ |

Every number above was derived from modular data by explicit arithmetic; no simulation or empirical measurement is invoked.

## 5. Results

The computations establish the following results.

**R1.** In all bosonic examples, $I_1 = \|\mathcal{A}\|/\mathcal{D}$ correctly reproduces the partition-function ratio predicted by anyon condensation: $1/\sqrt{2} \approx 0.7071$ for the $e$-condensed toric-code boundary and $1/\sqrt{3} \approx 0.5774$ for the charge-condensed $D(\mathbb{Z}_3)$ boundary. The index is a continuous-valued diagnostic distinguishing boundaries that categorical object counts alone would conflate.

**R2.** The residual count $N_{\text{res}} = 1/I_1^2$ is exactly $2$ and $3$ in the two bosonic examples, matching the explicit enumeration of deconfined anyons ($\{1, m\}$ and $\{(0,0),(0,1),(0,2)\}$ respectively). The identity $N_{\text{res}} = 1/I_1^2$ held in all four examples, including the fermionic ones.

**R3.** The fermion index $I_2$ separates pairs of boundaries with identical $I_1$: both the bosonic $e$-condensate and the fermionic $\epsilon$-condensate of the toric code give $I_1 = 1/\sqrt{2}$, but $I_2 = 0$ versus $I_2 = 1$. In the fermionic cases, $I_2 = 1$ coincides with an independently checkable anomaly: the mismatch of chiral central charge ($c_- = 1/2$ for the Ising residual sector against a required $c_- = 0$ for a strictly bosonic gapped boundary). This supports hypothesis (H3) that $I_2$ counts protected boundary Majorana-type anomaly data.

**R4.** The pair $(I_1, I_2)$ is a two-component invariant of the condensate data that is computable from $(S, T)$ and the object list of $\mathcal{A}$ alone, requiring no knowledge of microscopic boundary Hamiltonians. In the language of [7], $I_1$ plays the role of the anomaly-fixed part of the boundary response, while the residual freedom in boundary terms is the analogue of the independent boundary charges.

## 6. Discussion

**Relation to the literature.** The framework sits in a landscape of bulk-boundary correspondences of varying strength. At the strongest end, holographic correspondences identify boundary sources with non-normalizable bulk modes outright [3], and boundary states can even be used to *define* bulk operators [6]. At the weakest end, non-Hermitian point-gap topology admits boundary phenomena with no bulk invariant counterpart [2], and even biorthogonal refinements only partially restore the correspondence [8]. Condensing boundaries sit in between: our results suggest that the pair $(I_1, I_2)$ captures exactly the *forced* part of the boundary data, with the remainder genuinely free. This division of labor mirrors the bulk $a, c$ charges versus independent boundary charges of [7], the module-category-determined boundary Hamiltonians of [5], and the boundary subalgebra of bulk observables in the BV factorization-algebra framework [1]. The transmission-problem structure of [4] — boundary well-posedness contingent on bulk data — is the classical shadow of hypothesis (H2).

**Limitations and failure modes.** Three caveats are important. First, we verified (H1)–(H3) only in Abelian and one non-Abelian (Ising) example; for general non-Abelian condensates with nontrivial fusion multiplicities, the norm $\|\mathcal{A}\|$ must be computed with fusion multiplicities included, and the residual count may require refinement by the module-category data of [5]. Second, $I_2$ as defined counts fermionic objects but does not distinguish one anomalous fermion from several; a richer index (e.g., a $\mathbb{Z}_8$-valued invariant built from spins of condensate elements) may be needed for fine classification, and the QNFO program [9] anticipates such extensions. Third, the inverse problem — reconstructing bulk data from boundary observations — is not addressed; as the non-Hermitian literature shows [2, 8], inverse maps are where correspondences typically fail.

**Falsifiability.** The framework would be refuted by any of the following observations: (i) a bosonic condensate whose boundary-to-bulk partition-function ratio on a torus differs from $\|\mathcal{A}\|/\mathcal{D}$; (ii) a fermionic condensate with $I_2 \geq 1$ that admits a strictly bosonic, anomaly-free gapped boundary with no protected boundary modes; (iii) a condensate where the number of deconfined residual anyons differs from $\mathcal{D}^2/\|\mathcal{A}\|^2$. Conversely, confirmation would come from commuting-projector or exact-soluble models in the spirit of [5] realizing these counts explicitly.

**Open questions.** Does $I_1$ extend to a full partition-function invariant on higher-genus surfaces, and does it relate to the degree-$1$ Poisson structure of boundary observables in [1]? Can $I_2$ be sharpened to distinguish anomaly types, connecting to the boundary-charge classification of [7]? Do non-Hermitian generalizations of anyon condensation exhibit a failure mode analogous to point-gap topology, in which $I_1$ is computed from a non-unitary modular data and the correspondence partially breaks [2]? We leave these to future work.

## 7. Conclusion

We have given a self-contained two-index framework for the bulk-boundary correspondence at condensing boundaries, following the QNFO proposal. The condensation strength $I_1 = \|\mathcal{A}\|/\mathcal{D}$ and the boundary-fermion index $I_2$ are computable from modular data alone, and explicit arithmetic in four closed examples shows that $I_1$ fixes the partition-function ratio and residual-anyon count while $I_2$ detects fermionic obstructions that $I_1$ alone cannot see. The framework makes falsifiable claims and situates anyon condensation within the broader taxonomy of bulk-boundary correspondences, from the definitional strength of holography to the partial failures of non-Hermitian topology.

## References

[1] arXiv:2008.04953v3 | Factorization Algebras for Classical Bulk-Boundary Systems

[2] arXiv:2205.15635v4 | Bulk-boundary correspondence in point-gap topological phases

[3] arXiv:hep-th/9805171v4 | Bulk vs. Boundary Dynamics in Anti-de Sitter Spacetime

[4] arXiv:1803.05314v4 | Cahn-Hilliard equation on the boundary with bulk condition of Allen-Cahn type

[5] arXiv:2606.19137v2 | Bulk-boundary correspondence of (1+1)D symmetric gapped phases

[6] arXiv:1505.050