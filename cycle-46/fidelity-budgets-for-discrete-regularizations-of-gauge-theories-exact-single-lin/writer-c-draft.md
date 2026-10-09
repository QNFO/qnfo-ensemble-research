# Truncation Fidelity Budgets for Discrete Regularizations of Gauge Theories: From Quantum Link Models to Bruhat–Tits Trees

## Abstract

Discrete regularizations of gauge theories — finite-dimensional link Hilbert spaces in quantum link models, truncated electric bases on quantum computers, tensor networks on Bruhat–Tits trees — all face the same structural question: when does the discrete object faithfully encode its continuum or infinite-dimensional target? We develop a unified fidelity-budget framework that answers this question quantitatively at a target accuracy of $\epsilon = 10^{-4}$. The framework decomposes total error into truncation error per link, propagated over the number of links or boundary vertices, and yields explicit requirements on the truncation level $\ell_{\max}$. Under a Gaussian model for the electric-flux distribution we show that a per-link truncation level $\ell_{\max} \approx 4.45\,\sigma$ suffices for $\epsilon = 10^{-4}$ on a single link, while a hundred-link simulation requires $\ell_{\max} \approx 5.39\,\sigma$ — only logarithmically more expensive. Distribution-free (Chebyshev) bounds, by contrast, demand $\ell_{\max} = 100\,\sigma$, a gap of more than an order of magnitude that quantifies exactly what dynamical information (such as Hilbert-space fragmentation) buys. We apply the same budget to holographic quantum error correction organized as renormalization-group flow on the Bruhat–Tits tree $\mathcal{T}_2$, computing boundary vertex counts and qubit-equivalent costs at depth $L = 10$. The framework turns "reaching the quantum-field-theory limit" from a qualitative aspiration into an auditable numerical checklist.

## 1. Introduction

A gauge theory is not directly what an experiment builds. Whether the platform is a quantum simulator of synthetic matter, a gate-based quantum computer, or a tensor-network code, the theory must first be regularized: the continuum gauge field replaced by a finite-dimensional Hilbert space per link, the continuum geometry replaced by a discrete graph. The central fidelity question is then always the same. Given a discrete regularization $R$ of a target theory $T$, and a tolerance $\epsilon$, does the regularized dynamics agree with the target dynamics to within $\epsilon$ on the observables of interest — and if not, what exactly must be increased, and by how much?

This question has been posed independently in several communities. In quantum link models — gauge theories whose link Hilbert spaces are finite-dimensional representations rather than the infinite-dimensional Kogut–Susskind spaces — the question of when the genuine quantum-field-theory limit is reached has been analyzed for far-from-equilibrium dynamics [1]. In trapped-ion quantum computers, the recent observation of genuine $2+1$D string dynamics in a $\mathrm{U}(1)$ lattice gauge theory with a tunable plaquette term demonstrates that dynamical phenomena absent in one dimension can now be accessed, but only after the gauge field is truncated on every link [2]. A formalism for estimating truncation uncertainties against the Kogut–Susskind limit, leveraging Hilbert-space fragmentation to bound the excitation of large electric fields, has been developed precisely to make these errors quantitative [3]. In a completely different corner of the literature, holographic quantum error correction has been organized as renormalization-group (RG) flow on the Bruhat–Tits tree $\mathcal{T}_p$ — the $p$-adic analogue of anti-de Sitter space — with a conditional threshold analysis at accuracy $10^{-4}$ [9], building on the identification of the tree as a holographic geometry [11].

The contribution of this paper is to place these instances under one quantitative framework, which we call the **fidelity budget**: a decomposition of the total admissible error $\epsilon$ into per-component truncation errors, combined with explicit scaling laws that convert a budget into hardware requirements (truncation levels, qubit counts, tree depths). We derive all numbers with fully shown arithmetic in Section 4, and we are careful in Section 5 to report only what we actually computed, or clearly labeled projections. The framework is deliberately conservative: it uses worst-case and model-based bounds whose assumptions are stated explicitly, so that each number can be audited, and falsified, independently.

Our thesis is that the gap between "the regularization is faithful" and "the regularization is not" is almost always logarithmic in the accuracy on the side of informed (dynamics-aware) bounds, and polynomial on the side of uninformed bounds. The ratio between these two scalings — more than a factor of $20$ in truncation level at $\epsilon = 10^{-4}$ — is the quantitative content of statements like "fragmentation helps quantum simulation" [3], and it recurs, we argue, in every discrete regularization of a gauge theory, including the $p$-adic holographic setting [9, 11].

## 2. Background and Related Work

We review the twelve works of the bibliography in order, indicating how each enters the framework.

**[1] Achieving the quantum field theory limit in far-from-equilibrium quantum link models (arXiv:2112.04501v3).** This work asks when quantum link model realizations of gauge theories in quantum synthetic matter reach the genuine quantum-field-theory limit, with attention to far-from-equilibrium dynamics. It is the closest structural antecedent to our question: a finite-dimensional regularization (the quantum link) must be shown to reproduce continuum observables. Our fidelity budget supplies the quantitative instrument that such analyses need: a per-link error tolerance derived from a total budget, so that "reaching the limit" becomes a checkable inequality rather than a qualitative comparison.

**[2] Observation of genuine $2+1$D string dynamics in a U(1) lattice gauge theory with a tunable plaquette term on a trapped-ion quantum computer (arXiv:2604.07436v1).** This experiment demonstrates string dynamics relevant to hadronization in $2+1$ dimensions, where a plaquette term endows the gauge field with dynamics and enables photon-like propagation. The plaquette term is also the main new source of truncation sensitivity relative to $1+1$D: magnetic energy involves products of link operators around a loop, so truncation errors on different links coherently enter the same term. Our budget in Section 4 treats the number of links in a plaquette ($4$ in $2+1$D square lattices) as the coherence multiplier for magnetic-sector errors.

**[3] Truncation uncertainties for accurate quantum simulations of lattice gauge theories (arXiv:2508.00061v4).** This work develops a formalism for estimating the size of truncation errors incurred when the gauge field's Hilbert space on each link is discretized, exploiting Hilbert-space fragmentation in the electric basis, which limits the excitation of large electric fields. This is the direct quantitative ancestor of our Section 4: we adopt its logic that dynamics-aware bounds on the reachable electric-flux sector convert into dramatically smaller required truncation levels, and we make the comparison against dynamics-unaware bounds explicit with shown arithmetic.

**[4] A change of perspective: switching quantum reference frames via a perspective-neutral framework (arXiv:1809.00556v4).** This work treats reference frames as quantum systems and relates descriptions relative to different quantum reference frames through a perspective-neutral framework. Its relevance here is conceptual: the "target theory" $T$ of a regularization is only defined relative to a choice of frame, and a truncation that is harmless in one frame (e.g., the electric basis) may be nonlocal and severe in another. Our budget is therefore frame-dependent, and we flag this as a limitation in Section 6.

**[5] An axiomatic approach to quantum gauge field theory (arXiv:hep-th/9511122v1).** This constructive proposal formulates Osterwalder–Schrader-like axioms for the characteristic functional of a measure on the space of generalized connections modulo gauge transformations. It supplies the continuum-side definition of the target $T$ at the level of measures on connections: a regularization is faithful if the pushforward of the regularized measure through the coarse-graining map converges to such a measure. Our budget is an operational, finite-$\epsilon$ version of this convergence requirement.

**[6] A groupoidal approach to quantum reference frames (arXiv:2608.14133v1).** This work develops groupoid-based relational quantum field theory on curved spacetimes, where global symmetry groups are absent or too small for the group-based quantum reference frame formalism. For our framework it matters because on curved or $p$-adic backgrounds [9, 11] there is no global gauge group with respect to which truncation errors can be gauge-averaged; the groupoidal perspective suggests that the budget must be assigned locally, per vertex or per edge, which is exactly how we proceed.

**[7] SU_q(n) Gauge Theory (arXiv:hep-th/9601033v2).** This work defines a field theory with local quantum-group $\mathrm{SU}_q(n)$ transformations on a classical spacetime, with gauge potentials in a quantum Lie algebra. It is a useful limiting case for us: the deformation parameter $q$ acts as a one-parameter family of regularizations of the classical gauge algebra, and the fidelity question becomes the $q \to 1$ limit. Our budget applies verbatim with $\epsilon$ measuring deviation of correlators from their $q=1$ values.

**[8] Quantum Energy Inequalities and Stability Conditions in Quantum Field Theory (arXiv:math-ph/0502002v1).** This review connects quantum energy inequalities (QEIs) to microscopic and mesoscopic stability of quantum field theory. QEIs bound the magnitude and duration of negative energy excitations, and hence bound the tail of the energy distribution that a truncation must capture. This is precisely the input our Gaussian model in Section 4 needs: a physically motivated bound on the variance $\sigma^2$ of the electric flux, supplied not by assumption but by a stability condition on the target theory.

**[9] Holographic Quantum Error Correction as AdS/CFT Renormalization-Group Flow on Bruhat–Tits Trees: A Conditional Threshold Analysis at $10^{-4}$ (DOI 10.5281/zenodo.23107746).** This work analyzes quantum error correction organized as RG flow on the Bruhat–Tits tree $\mathcal{T}_p$, the $p$-adic analogue of hyperbolic AdS space, with the encoding map of a holographic code literally an RG trajectory, and states a conditional threshold at accuracy $10^{-4}$. We adopt the same target accuracy and, in Section 4, compute the tree-geometry quantities (boundary vertex counts, edge counts, qubit-equivalent costs) that such a threshold analysis requires as inputs.

**[10] The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics (DOI 10.5281/zenodo.22025544).** This register organizes sixteen published records from a single research program into one testable claim: that trapped-ion quantum simulators are the first near-term platform on which ultrametric ($p$-adic) structure in quantum dynamics can be accepted or rejected by measurement. It supplies the experimental side of our framework: the fidelity budget is exactly the kind of pre-registered, auditable numerical structure that a falsifiability register needs, and the platform overlap with [2] makes a combined test realistic.

**[11] Holographic QEC as AdS/CFT RG Flow on Bruhat–Tits Trees (DOI pending).** This work completes a trilogy by showing that the Bruhat–Tits tree $\mathcal{T}_p$ is the $p$-adic analog of anti-de Sitter space and that tensor networks on $\mathcal{T}_p$ are holographic, building on prior tasks that established bosonic QEC as RG fixed-point subspaces on such trees. It provides the geometric identification that makes our tree-count computations in Section 4 physically meaningful rather than merely combinatorial.

**[12] The Adelic Cross-Domain Program: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat-Tits Trees (DOI 10.5281/zenodo.21754154).** This program connects fine-structure constants and Standard Model mass ratios through Bruhat–Tits tree structures, with a documented v3.2 correction pass in which arithmetic errors in mass ratio triplets were corrected (5 of 9 verified independently) and an "honest structural correspondence" standard was adopted. Its methodological lesson directly shapes this paper: every quantitative claim must carry shown arithmetic and an explicit verification status, which is the standard we enforce in Sections 4 and 5.

## 3. Methods

### 3.1 The fidelity budget

Let $R$ be a discrete regularization of a target theory $T$, and let $\mathcal{O}$ be a set of observables on which agreement is demanded. We define the fidelity budget as the constraint

$$
\Delta_R(T;\mathcal{O}) \;=\; \sup_{O \in \mathcal{O}} \big| \langle O \rangle_R - \langle O \rangle_T \big| \;\le\; \epsilon,
$$

where $\epsilon$ is the target accuracy. We take $\epsilon = 10^{-4}$ throughout, matching the conditional threshold of [9]. The budget is decomposed as

$$
\epsilon \;=\; \epsilon_{\text{trunc}} + \epsilon_{\text{dyn}} + \epsilon_{\text{impl}},
$$

where $\epsilon_{\text{trunc}}$ is the error from finite link Hilbert spaces (or finite tree depth), $\epsilon_{\text{dyn}}$ the error from finite evolution time or finite RG depth, and $\epsilon_{\text{impl}}$ the implementation error (gate noise, readout). This paper isolates $\epsilon_{\text{trunc}}$; the other terms are reserved for future work and are not assigned numbers here.

### 3.2 Truncation model for the electric sector

On each link, the electric basis $\{|\ell\rangle\}_{\ell \in \mathbb{Z}}$ carries flux quanta with electric energy $E(\ell) = \tfrac{g^2}{2}\ell^2$ (Kogut–Susskind convention). A truncation keeps $|\ell| \le \ell_{\max}$, i.e., $n_{\text{states}} = 2\ell_{\max}+1$ states per link, encoded in

$$
q \;=\; \left\lceil \log_2\!\left(2\ell_{\max}+1\right) \right\rceil
$$

qubits per link. The truncation error is the total probability weight outside the kept sector,

$$
\epsilon_{\text{link}} \;=\; \sum_{|\ell| > \ell_{\max}} P(\ell),
$$

where $P(\ell)$ is the electric-flux distribution of the state being simulated.

### 3.3 Two models for $P(\ell)$

**Model G (Gaussian).** If the electric flux is approximately Gaussian with variance $\sigma^2$ — motivated by QEI-type stability conditions on the target theory [8], which bound the energy content of excitations — then the two-sided tail is

$$
\epsilon_{\text{link}} \;\approx\; 2\,\exp\!\left(-\frac{\ell_{\max}^2}{2\sigma^2}\right).
$$

**Model C (Chebyshev, distribution-free).** With only the variance known,

$$
\epsilon_{\text{link}} \;\le\; \frac{\sigma^2}{\ell_{\max}^2}.
$$

Model C is the correct bound if nothing is known about the dynamics; Model G is the correct bound if the dynamics is locally stable and mixing in the electric sector. The gap between them is the quantitative value of dynamical information such as fragmentation [3].

### 3.4 Propagation over links

For $N_L$ independent links with per-link error $\epsilon_{\text{link}}$ each, a union bound gives

$$
\epsilon_{\text{trunc}} \;\le\; N_L\,\epsilon_{\text{link}},
$$

so a total budget $\epsilon_{\text{trunc}} \le \epsilon$ requires $\epsilon_{\text{link}} \le \epsilon / N_L$. For coherent (magnetic/plaquette) errors the multiplier is the loop length rather than the link count; we treat the $4$-link plaquette of [2] as the smallest such multiplier and report it separately.

### 3.5 Tree-geometry model for the $p$-adic holographic code

Following [9, 11], the encoding is an RG trajectory on the Bruhat–Tits tree $\mathcal{T}_p$ toward the boundary. At depth $L$ the tree has boundary vertices

$$
N_{\partial}(L) \;=\; (p+1)\,p^{L-1},
$$

total edges

$$
N_{\text{edge}}(L) \;=\; 1 + (p+1)\sum_{k=0}^{L-1} p^k \;=\; 1 + (p+1)\,\frac{p^L - 1}{p - 1},
$$

and the boundary requires $\lceil \log_2 N_{\partial}(L) \rceil$ qubits if each boundary vertex is addressed by a binary index.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Single-link truncation level at $\epsilon = 10^{-4}$ (Model G)

**Inputs.** Target accuracy $\epsilon = 10^{-4}$ (source: threshold convention of [9]); flux variance $\sigma \in \{1, 2, 3\}$ in units of the flux quantum (source: model parameter, three illustrative values; see Section 6 for the assumption's status).

**Step 1.** Invert the Gaussian tail:

$$
2\,\exp\!\left(-\frac{\ell_{\max}^2}{2\sigma^2}\right) = 10^{-4}
\quad\Longrightarrow\quad
\frac{\ell_{\max}^2}{2\sigma^2} = \ln\!\left(2 \times 10^{4}\right).
$$

**Step 2.** Compute the logarithm: $\ln(2 \times 10^{4}) = \ln 2 + 4\ln 10 = 0.693147 + 4 \times 2.302585 = 0.693147 + 9.210340 = 9.903487$.

**Step 3.** Double and take the square root: $2 \times 9.903487 = 19.806974$; $\sqrt{19.806974} = 4.45016$. Hence

$$
\ell_{\max} = 4.45016\,\sigma.
$$

**Step 4.** Round up to integer truncation levels and compute qubit counts $q = \lceil \log_2(2\ell_{\max}+1)\rceil$:

- $\sigma = 1$: $\ell_{\max} = \lceil 4.45016 \rceil = 5$; $n_{\text{states}} = 2(5)+1 = 11$; $\log_2 11 = 3.45948$; $q = 4$.
- $\sigma = 2$: $\ell_{\max} = \lceil 8.90032 \rceil = 9$; $n_{\text{states}} = 19$; $\log_2 19 = 4.24793$; $q = 5$.
- $\sigma = 3$: $\ell_{\max} = \lceil 13.35048 \rceil = 14$; $n_{\text{states}} = 29$; $\log_2 29 = 4.85798$; $q = 5$.

### 4.2 The Chebyshev contrast (Model C)

**Inputs.** Same $\epsilon = 10^{-4}$; same $\sigma$.

**Step 1.** Invert $\sigma^2/\ell_{\max}^2 = 10^{-4}$:

$$
\ell_{\max} = \sigma \sqrt{10^{4}} = 100\,\sigma.
$$

**Step 2.** Ratio to the Gaussian requirement:

$$
\frac{100\,\sigma}{4.45016\,\sigma} = \frac{100}{4.45016} = 22.4716.
$$

So the dynamics-unaware bound demands a truncation level $22.47$ times larger than the dynamics-aware bound at the same accuracy. In qubits for $\sigma = 1$: Model C needs $2(100)+1 = 201$ states, $\log_2 201 = 7.65105$, $q = 8$ qubits per link, versus $q = 4$ for Model G — a $2\times$ qubit overhead per link, compounding exponentially with system size.

### 4.3 Propagation to $N_L = 100$ links

**Inputs.** $N_L = 100$ links (source: illustrative system size, e.g., a $10\times10$ plaquette array has $200$ links; we take the smaller round value $100$ and note the sensitivity); total budget $\epsilon_{\text{trunc}} = 10^{-4}$.

**Step 1.** Per-link budget: $\epsilon_{\text{link}} = 10^{-4}/100 = 10^{-6}$.

**Step 2.** Invert the Gaussian tail at $\epsilon_{\text{link}} = 10^{-6}$:

$$
\ell_{\max} = \sigma\sqrt{2\ln(2\times 10^{6})}.
$$

Compute: $\ln(2\times10^{6}) = \ln 2 + 6\ln 10 = 0.693147 + 13.815511 = 14.508658$; $2 \times 14.508658 = 29.017316$; $\sqrt{29.017316} = 5.38677$. Hence

$$
\ell_{\max} = 5.38677\,\sigma.
$$

**Step 3.** Compare with the single-link value $4.45016\,\sigma$:

$$
\frac{5.38677}{4.45016} = 1.21046.
$$

Going from one link to one hundred links costs only a factor $1.21$ in truncation level — the logarithmic scaling that is the central quantitative claim of this paper.

**Step 4.** Qubit counts at $N_L = 100$:

- $\sigma = 1$: $\ell_{\max} = \lceil 5.38677 \rceil = 6$; $n_{\text{states}} = 13$; $\log_2 13 = 3.70044$; $q = 4$.
- $\sigma = 2$: $\ell_{\max} = \lceil 10.77354 \rceil = 11$; $n_{\text{states}} = 23$; $\log_2 23 = 4.52356$; $q = 5$.
- $\sigma = 3$: $\ell_{\max} = \lceil 16.16031 \rceil = 17$; $n_{\text{states}} = 35$; $\log_2 35 = 5.12928$; $q = 6$.

Note that for $\sigma = 1$ the qubit count does not change at all between the single-link and hundred-link budgets ($4 \to 4$): the entire hundred-fold tightening of the budget is absorbed inside one qubit's worth of headroom.

### 4.4 Plaquette coherence multiplier

**Inputs.** Plaquette loop length $4$ (source: square-lattice $2+1$D geometry of [2]); per-link truncation error $\epsilon_{\text{link}}$.

**Step 1.** If the four link errors around one plaquette enter the magnetic term coherently, the plaquette-level error is bounded by $4\,\epsilon_{\text{link}}$ (union bound over the loop).

**Step 2.** For a total magnetic budget of $10^{-4}$ over a single plaquette, the per-link requirement is $\epsilon_{\text{link}} = 10^{-4}/4 = 2.5 \times 10^{-5}$.

**Step 3.** Invert the Gaussian tail at $2.5\times10^{-5}$: $\ln(2/2.5\times10^{-5}) = \ln(8\times10^{4}) = \ln 8 + 4\ln 10 = 2.079442 + 9.210340 = 11.289782$; $2 \times 11.289782 = 22.579564$; $\sqrt{22.579564} = 4.75180$. Hence $\ell_{\max} = 4.75180\,\sigma$, versus $4.45016\,\sigma$ for the single-link electric budget — a factor $4.75180/4.45016 = 1.06778$, i.e., under $7\%$ additional truncation level for full plaquette coherence.

### 4.5 Bruhat–Tits tree geometry at $p = 2$, $L = 10$

**Inputs.** $p = 2$ (source: the simplest nontrivial Bruhat–Tits tree, used as the canonical case in [9, 11]); depth $L = 10$ (source: illustrative RG depth, chosen so that the boundary exceeds $2^{10}$ vertices).

**Step 1.** Boundary vertices: $N_{\partial}(10) = (2+1)\,2^{9} = 3 \times 512 = 1536$.

**Step 2.** Binary address width: $\log_2 1536 = \log_2(3 \cdot 2^9) = 9 + \log_2 3 = 9 + 1.584963 = 10.584963$; $\lceil 10.584963 \rceil = 11$ qubits to address the boundary.

**Step 3.** Total edges: $N_{\text{edge}}(10) = 1 + 3\,(2^{10}-1) = 1 + 3 \times 1023 = 1 + 3069 = 3070$.

**Step 4.** If each edge carries one truncated gauge link with the Section 4.3 budget, the union bound over $3070$ links requires $\epsilon_{\text{link}} = 10^{-4}/3070 = 3.2573 \times 10^{-8}$ (computed: $10^{-4}/3070 = 3.25733\times10^{-8}$). Inverting the Gaussian tail: $\ln(2/3.25733\times10^{-8}) = \ln(6.13997\times10^{7}) = \ln 6.13997 + 7\ln 10 = 1.815615 + 16.118095 = 17.933710$; $2 \times 17.933710 = 35.867420$; $\sqrt{35.867420} = 5.98894$. Hence $\ell_{\max} = 5.98894\,\sigma$ — for $\sigma = 1$, $\ell_{\max} = 6$, $n_{\text{states}} = 13$, $q = 4$: the same $4$ qubits per link as the hundred-link lattice case. The logarithmic scaling persists at tree scale.

### 4.6 Fragmentation-bounded dynamics (illustrative reachability)

**Inputs.** Conserved total electric energy $E_0 = 100$ in units of $g^2/2$ (source: illustrative initial-state preparation; the conservation structure is the fragmentation mechanism of [3]).

**Step 1.** If fragmentation conserves the electric energy sector, no link can exceed $\tfrac{g^2}{2}\ell^2 \le E_0$, so $\ell \le \sqrt{2E_0/g^2} = \sqrt{2 \times 100} = \sqrt{200} = 14.14214$.

**Step 2.** A truncation at $\ell_{\max} = 15$ (rounding up $14.14214$) is then *exact* for the reachable sector regardless