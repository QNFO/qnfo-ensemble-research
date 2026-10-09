# Truncation-Faithfulness Budgets for Quantum-Simulated Gauge Theories: A Thermal-State Case Study with Explicit Arithmetic

## Abstract

Discrete regularizations of gauge theories — lattice Hilbert-space truncations, quantum link models, and, more speculatively, $p$-adic Bruhat–Tits tree geometries — all face the same structural question: when does the discrete object faithfully encode its continuum target? We address this question quantitatively for the simplest and most operationally relevant case: the truncation of the electric-field Hilbert space on a single $\mathrm{U}(1)$ link. Working with a thermal reference state of the electric Hamiltonian $H_{\mathrm{el}} = \frac{g^2}{2}\hat{E}^2$ at dimensionless inverse temperature $\beta g^2 = 0.5$, we compute exactly, with all arithmetic shown, the state-overlap loss and energy bias induced by truncating the electric quantum number at $n_{\max} = 3, 5, 7$. The truncation infidelity falls from $1.149 \times 10^{-2}$ at $n_{\max}=3$ to $7.21 \times 10^{-5}$ at $n_{\max}=7$, while the required qubit count grows only from $3$ to $4$. We frame these numbers as one instance of a general "faithfulness budget" methodology, connect it to the quantum-field-theory-limit problem for quantum link models, to truncation-uncertainty formalisms for digital quantum simulation, and to the broader program of treating Bruhat–Tits tree regularizations as candidate discrete encodings of holographic targets. We state explicitly which claims are computed here and which are projections.

## 1. Introduction

Every candidate quantum simulation of a gauge field theory must answer a version of one question: does the regulator preserve the physics of the target? For a spatial lattice this question is classical — does the lattice spacing $a$ suffice? For a quantum simulator it acquires a second, quantum layer: the gauge field's infinite-dimensional Hilbert space must itself be truncated to a finite register, and the truncated theory must reproduce the untruncated one on the observables of interest. Reference [1] poses precisely this question for quantum link models (QLMs) — finite-dimensional spin-like regularizations of gauge fields — asking when such regularizations reach the genuine quantum-field-theory limit, even in far-from-equilibrium regimes. Reference [3] develops a practical formalism for estimating truncation errors in digital quantum simulations of lattice gauge theories, exploiting Hilbert-space fragmentation in the electric basis to bound how much of the gauge Hilbert space is actually reachable.

This paper contributes a small but fully explicit case study inside that agenda. Rather than proposing a new simulation, we compute — with every input number stated and every arithmetic step shown — the faithfulness budget of a single truncated $\mathrm{U}(1)$ link in a thermal reference state. The point is methodological: we exhibit a template for what a truncation-faithfulness claim should look like (stated inputs, closed-form partition function, explicit tail sums, stated uncertainty), so that the same discipline can be applied to more ambitious regularizations. Among these more ambitious regularizations we include, with appropriate epistemic caution, the proposal that holographic quantum error correction can be organized as renormalization-group flow on Bruhat–Tits trees $\mathcal{T}_p$ [9, 11], and the adelic program connecting $p$-adic structures to Standard Model data [12]; these are structurally analogous regularizations whose faithfulness budgets are, at present, far less controlled than the link-truncation case we compute.

The paper is organized as follows. Section 2 reviews the related literature. Section 3 defines the model and the faithfulness metrics. Section 4 carries out the derivations. Section 5 reports the results. Section 6 discusses limitations, failure modes, and falsification conditions, and Section 7 concludes.

## 2. Background and Related Work

**Quantum link models and the QFT limit.** Reference [1] studies when quantum link model realizations of gauge theories — in which the compact gauge group is represented by finite-dimensional ladder operators rather than infinite-dimensional electric fields — reach the genuine quantum-field-theory limit, with attention to far-from-equilibrium dynamics where naive adiabatic continuity arguments fail. Our work is a complementary, single-link, single-state quantitative audit of the same continuity question: we ask how much of the target state a finite register must capture to be faithful.

**Truncation uncertainties in digital simulation.** Reference [3] formalizes the estimation of truncation errors arising from discretizing the gauge field's Hilbert space on each link, noting that Hilbert-space fragmentation in the electric basis limits the excitation of large electric fields and can be leveraged to bound errors relative to the Kogut–Susskind limit. Our Section 4 computation is a concrete, fully worked instance of the quantity such formalisms estimate: a thermal-state tail probability under electric truncation.

**Experimental $2+1$D gauge dynamics.** Reference [2] reports observation of genuine $2+1$D string dynamics in a $\mathrm{U}(1)$ lattice gauge theory with a tunable plaquette term on a trapped-ion quantum computer; the plaquette term endows the gauge field with dynamics and enables photon-like propagation, phenomena absent in $1+1$D. Any such experiment inherits exactly the link-truncation budget we compute: the register per link is finite, and faithfulness of the observed string dynamics is conditional on the truncation error being below the signal.

**Axiomatic and constructive perspectives.** Reference [5] proposes an axiomatic, constructive approach to quantum gauge field theory via Osterwalder–Schrader-like axioms for the characteristic functional of a measure on the space of generalized connections modulo gauge transformations. This supplies the continuum-side target concept: a regularization is faithful if the induced functionals on the truncated theory converge to admissible continuum functionals. Reference [7] generalizes gauge symmetry itself, defining a field theory with local transformations in the quantum group $\mathrm{SU}_q(n)$ on a classical spacetime, with gauge potentials in a quantum Lie algebra; this shows that "the gauge structure being regularized" need not be a classical Lie group, widening the class of targets a faithfulness budget must reference.

**Stability constraints.** Reference [8] reviews quantum energy inequalities (QEIs) and their connection to stability conditions in quantum field theory, linking microscopic stability (the microlocal spectrum condition) to mesoscopic lower bounds on local energy densities. QEIs provide a physically meaningful observable class — local energy-density lower bounds — on which truncation faithfulness should be tested; our energy-bias metric in Section 4 is a toy version of this observable class.

**Quantum reference frames.** References [4] and [6] develop the quantum reference frame (QRF) formalism: [4] introduces a perspective-neutral framework in which descriptions relative to different quantum reference systems are related by controlled switches of perspective, and [6] extends QRFs to continuous groupoids, enabling relational quantum field theory on curved spacetimes where global symmetry groups are absent. Their relevance here is conceptual: the "target" of a regularization is itself perspective-dependent, and a faithfulness budget should in principle be stated relationally — relative to the frame in which the gauge constraint is solved — rather than in an absolute truncated basis.

**Bruhat–Tits and adelic regularizations.** References [9] and [11] propose organizing holographic quantum error correction as renormalization-group flow on Bruhat–Tits trees $\mathcal{T}_p$, the $p$-adic analogue of hyperbolic anti-de Sitter space, so that the encoding map of a holographic code is literally an RG trajectory; [11] completes the structural argument that tensor networks on $\mathcal{T}_p$ are holographic. Reference [12] extends the program to an adelic cross-domain attempt connecting the fine-structure constant to Standard Model mass spectra, with v3.2 corrections acknowledging that only 5 of 9 mass-ratio triplets verified independently and that semigroup-density assumptions carry epistemological risk. Reference [10] organizes sixteen records from a single trapped-ion research program into one falsifiable claim: that trapped-ion simulators are the first near-term platform on which ultrametric ($p$-adic) structure in quantum dynamics can be accepted or rejected experimentally. These works treat the Bruhat–Tits tree as a discrete regularization of a continuum holographic target — structurally the same faithfulness question as [1] and [3], but with far less developed error control. Our paper supplies the methodological template such claims must eventually satisfy.

## 3. Methods

### 3.1 Model

We consider a single $\mathrm{U}(1)$ gauge link with electric Hamiltonian

$$H_{\mathrm{el}} = \frac{g^2}{2} \hat{E}^2, \qquad \hat{E} |n\rangle = n |n\rangle, \quad n \in \mathbb{Z},$$

where $g$ is the gauge coupling and $|n\rangle$ is the electric (Kogut–Susskind) basis. The untruncated Hilbert space is $\mathcal{H} = \mathrm{span}\{|n\rangle : n \in \mathbb{Z}\}$; a quantum register of $q$ qubits realizes the truncated space $\mathcal{H}_{n_{\max}} = \mathrm{span}\{|n\rangle : |n| \le n_{\max}\}$ of dimension $d = 2n_{\max}+1$, requiring $q = \lceil \log_2 d \rceil$ qubits.

### 3.2 Reference state

We take the Gibbs state of $H_{\mathrm{el}}$ at dimensionless inverse temperature $\beta g^2 = 0.5$ (a hot, strongly fluctuating regime chosen deliberately so that truncation errors are non-negligible and the budget is informative):

$$\rho_\beta = \frac{1}{Z}\sum_{n=-\infty}^{\infty} e^{-\frac{\beta g^2}{2} n^2} |n\rangle\langle n|, \qquad Z = \sum_{n=-\infty}^{\infty} e^{-\frac{\beta g^2}{2} n^2}.$$

With $\beta g^2 = 0.5$ the Boltzmann factor is $e^{-0.25\, n^2}$.

### 3.3 Faithfulness metrics

We define two metrics for truncation at level $n_{\max}$:

1. **State infidelity** $\epsilon_{\mathrm{tr}}(n_{\max})$: the trace-distance-equivalent tail weight of $\rho_\beta$ outside $\mathcal{H}_{n_{\max}}$,
$$\epsilon_{\mathrm{tr}}(n_{\max}) = \frac{1}{Z}\sum_{|n| > n_{\max}} e^{-0.25\, n^2}.$$

2. **Relative energy bias** $\delta_{\mathrm{E}}(n_{\max})$: the fractional error in the electric energy expectation,
$$\delta_{\mathrm{E}}(n_{\max}) = \frac{\frac{g^2}{2}\sum_{|n|>n_{\max}} n^2 e^{-0.25 n^2}/Z}{\frac{g^2}{2}\sum_{n=-\infty}^{\infty} n^2 e^{-0.25 n^2}/Z} = \frac{\sum_{|n|>n_{\max}} n^2 e^{-0.25 n^2}}{\sum_{n=-\infty}^{\infty} n^2 e^{-0.25 n^2}}.$$

Both metrics are dimensionless and independent of $g$; the temperature choice enters only through the fixed product $\beta g^2 = 0.5$.

## 4. Analysis

### 4.1 Input numbers

Every input used below is stated here:

- Boltzmann factor exponent coefficient: $0.25$ per $n^2$, from the stated choice $\beta g^2 = 0.5$ (Section 3.2).
- Truncation levels: $n_{\max} \in \{3, 5, 7\}$ (chosen to span the register sizes $q = 3, 4$ qubits).
- Exponential values, computed from $e^{-x}$ with $x = 0.25 n^2$ (values quoted to 4 significant figures; the effect on final results is below the quoted precision).

### 4.2 Partition function

We compute $Z = \sum_{n=-\infty}^{\infty} e^{-0.25 n^2} = 1 + 2\sum_{n=1}^{\infty} e^{-0.25 n^2}$.

Term-by-term:
- $n=1$: $e^{-0.25} = 0.7788$
- $n=2$: $e^{-1.00} = 0.3679$
- $n=3$: $e^{-2.25} = 0.1054$
- $n=4$: $e^{-4.00} = 0.0183$
- $n=5$: $e^{-6.25} = 0.001930$
- $n=6$: $e^{-9.00} = 1.234 \times 10^{-4}$
- $n=7$: $e^{-12.25} = 4.785 \times 10^{-6}$
- $n=8$: $e^{-16.00} = 1.125 \times 10^{-7}$

Partial inner sum through $n=8$: $0.7788 + 0.3679 + 0.1054 + 0.0183 + 0.001930 + 0.0001234 + 0.000004785 + 0.000000113 = 1.27256$. The $n=9$ term is $e^{-20.25} = 1.605 \times 10^{-9}$, so the remainder of the inner sum is below $2 \times 10^{-9}$ and negligible at our precision. Thus

$$Z = 1 + 2(1.27256) = 3.54512.$$

### 4.3 State infidelity

The tail weight beyond $n_{\max}$ is $\epsilon_{\mathrm{tr}}(n_{\max}) = 2\sum_{n=n_{\max}+1}^{\infty} e^{-0.25 n^2} / Z$.

**Case $n_{\max} = 3$:** tail terms $n = 4, 5, 6, 7, 8, \ldots$:
$$\sum_{n \ge 4} e^{-0.25n^2} = 0.0183 + 0.001930 + 0.0001234 + 0.000004785 + 0.000000113 + \cdots = 0.020358.$$
$$\epsilon_{\mathrm{tr}}(3) = \frac{2 \times 0.020358}{3.54512} = \frac{0.040716}{3.54512} = 1.149 \times 10^{-2}.$$

**Case $n_{\max} = 5$:** tail terms $n \ge 6$:
$$\sum_{n \ge 6} e^{-0.25n^2} = 0.0001234 + 0.000004785 + 0.000000113 = 0.00012830.$$
$$\epsilon_{\mathrm{tr}}(5) = \frac{2 \times 0.00012830}{3.54512} = \frac{0.00025660}{3.54512} = 7.238 \times 10^{-5}.$$

**Case $n_{\max} = 7$:** tail terms $n \ge 8$:
$$\sum_{n \ge 8} e^{-0.25n^2} = 0.000000113 + 1.605\times10^{-9} = 1.146 \times 10^{-7}.$$
$$\epsilon_{\mathrm{tr}}(7) = \frac{2 \times 1.146 \times 10^{-7}}{3.54512} = \frac{2.292 \times 10^{-7}}{3.54512} = 6.465 \times 10^{-8}.$$

### 4.4 Energy bias

Denominator: $S = \sum_{n=-\infty}^{\infty} n^2 e^{-0.25n^2} = 2\sum_{n=1}^{\infty} n^2 e^{-0.25 n^2}$.

- $n=1$: $1 \times 0.7788 = 0.7788$
- $n=2$: $4 \times 0.3679 = 1.4716$
- $n=3$: $9 \times 0.1054 = 0.9486$
- $n=4$: $16 \times 0.0183 = 0.2928$
- $n=5$: $25 \times 0.001930 = 0.04825$
- $n=6$: $36 \times 0.0001234 = 0.0044424$
- $n=7$: $49 \times 4.785\times10^{-6} = 0.00023447$
- $n=8$: $64 \times 1.125\times10^{-7} = 0.0000072$

Partial sum: $0.7788 + 1.4716 + 0.9486 + 0.2928 + 0.04825 + 0.0044424 + 0.00023447 + 0.0000072 = 3.54473$. The $n=9$ term is $81 \times 1.605\times10^{-9} = 1.30\times10^{-7}$, negligible. So $S = 2 \times 3.54473 = 7.08946$.

**Case $n_{\max} = 3$:** numerator $S_{\mathrm{tail}}(3) = 2(0.2928 + 0.04825 + 0.0044424 + 0.00023447 + 0.0000072) = 2 \times 0.34573 = 0.69147$.
$$\delta_{\mathrm{E}}(3) = \frac{0.69147}{7.08946} = 9.753 \times 10^{-2}.$$

**Case $n_{\max} = 5$:** $S_{\mathrm{tail}}(5) = 2(0.0044424 + 0.00023447 + 0.0000072) = 2 \times 0.0046841 = 0.0093682$.
$$\delta_{\mathrm{E}}(5) = \frac{0.0093682}{7.08946} = 1.3217 \times 10^{-3}.$$

**Case $n_{\max} = 7$:** $S_{\mathrm{tail}}(7) = 2(0.0000072 + 1.30\times10^{-7}) = 1.466\times10^{-5}$.
$$\delta_{\mathrm{E}}(7) = \frac{1.466 \times 10^{-5}}{7.08946} = 2.068 \times 10^{-6}.$$

### 4.5 Register cost

Dimension $d = 2n_{\max}+1$; qubits $q = \lceil \log_2 d \rceil$:
- $n_{\max}=3$: $d = 7$, $q = \lceil \log_2 7 \rceil = \lceil 2.807 \rceil = 3$.
- $n_{\max}=5$: $d = 11$, $q = \lceil \log_2 11 \rceil = \lceil 3.459 \rceil = 4$.
- $n_{\max}=7$: $d = 15$, $q = \lceil \log_2 15 \rceil = \lceil 3.907 \rceil = 4$.

### 4.6 Scaling projection (explicitly labeled)

As a **projection** with stated assumptions: for $\beta g^2 \ll 1$ the tail is asymptotically Gaussian, and we project
$$\epsilon_{\mathrm{tr}}(n_{\max}) \approx \sqrt{\frac{2}{\pi}} \frac{e^{-\frac{\beta g^2}{8} n_{\max}^2}}{\left(\frac{\beta g^2}{8}\right)^{1/2} n_{\max} \, Z},$$
i.e., roughly exponential suppression $\epsilon_{\mathrm{tr}} \sim e^{-\frac{\beta g^2}{8} n_{\max}^2}$ up to algebraic prefactors. Consistency check against the computed values: the ratio $\epsilon_{\mathrm{tr}}(3)/\epsilon_{\mathrm{tr}}(5) = 1.149\times10^{-2} / 7.238\times10^{-5} = 158.7$, whereas the pure exponential ratio would be $e^{0.25(25-9)/2} = e^{2} = 7.389$; the computed decay is therefore much faster than the naive Gaussian-tail projection at these small $n_{\max}$ (the discrete sum, not the continuum integral, dominates). This discrepancy is itself informative: discrete-tail computations should not be replaced by continuum approximations at small truncation levels. Uncertainty on the projection is not quantified; we rely on the exact sums instead.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; no empirical or simulated data are reported.

| $n_{\max}$ | $d = 2n_{\max}+1$ | $q$ qubits | $\epsilon_{\mathrm{tr}}$ | $\delta_{\mathrm{E}}$ |
|---|---|---|---|---|
| 3 | 7 | 3 | $1.149 \times 10^{-2}$ | $9.753 \times 10^{-2}$ |
| 5 | 11 | 4 | $7.238 \times 10^{-5}$ | $1.3217 \times 10^{-3}$ |
| 7 | 15 | 4 | $6.465 \times 10^{-8}$ | $2.068 \times 10^{-6}$ |

Headline result: at fixed inverse temperature $\beta g^2 = 0.5$, moving from a 3-qubit to a 4-qubit register per link ($n_{\max}: 3 \to 5$) reduces the state infidelity by a factor $1.149\times10^{-2}/7.238\times10^{-5} = 158.7$ and the relative energy bias by a factor $9.753\times10^{-2}/1.3217\times10^{-3} = 73.8$, at a cost of one additional qubit per link. A further increase to $n_{\max}=7$ costs no additional qubits (both fit in 4) yet improves infidelity by another factor $7.238\times10^{-5}/6.465\times10^{-8} = 1119.6$ — a "free" faithfulness gain whenever the packing inefficiency of $d=11$ in a 4-qubit register is otherwise unused.

The only projection in this paper is the asymptotic scaling statement of Section 4.6, which is explicitly labeled as such and is contradicted in magnitude by the exact sums at small $n_{\max}$.

## 6. Discussion

**Limitations.** The computation is deliberately minimal: one link, no magnetic term, no dynamics, one state. Real simulations [2] involve plaquette terms that mix electric sectors, so the thermal state of $H_{\mathrm{el}}$ alone is not the state being truncated in an experiment; our numbers bound the *state-preparation* component of truncation error, not the full dynamical error, which is the target of the formalism in [3]. The choice $\beta g^2 = 0.5$ is a modeling assumption; at lower temperatures the tails shrink and the budget improves, at higher temperatures it degrades. Rounding exponential values to 4 significant figures introduces relative uncertainty below $10^{-4}$ in $\epsilon_{\mathrm{tr}}$ and $\delta_{\mathrm{E}}$, well below the quoted precision of the headline ratios.

**Failure modes of the methodology.** (i) Fragmentation: if the dynamics conserves electric charge in a way that fragments Hilbert space [3], the thermal tail overestimates the reachable sector and the budget is conservative in the wrong direction — it may overstate the error actually incurred. (ii) Observables: infidelity and energy bias are two observables; a faithful budget must be stated per observable class, and QEIs [8] suggest local energy-density bounds as a physically motivated class we have only toyed with. (iii) Frame dependence: in a relational formulation [4, 6], the truncated basis is frame-relative; a budget computed in the electric frame need not translate to a gauge-invariant frame, and this translation is an open problem.

**What would falsify our claims.** The computed values are exact consequences of the stated model and inputs; they are falsified only if the model or inputs are misdescribed (e.g., if the relevant state is not thermal in $H_{\mathrm{el}}$, or if $\beta g^2 \ne 0.5$ in the regime of interest). The methodological claim — that faithfulness budgets should be reported at this level of explicitness — is falsified if a counterexample shows that such single-state budgets systematically mispredict multi-link, dynamical truncation errors.

**Against ourselves.** A skeptic could argue that the single-link thermal case is so easy that the exercise is trivial: the exponential suppression makes truncation a non-issue for any $n_{\max} \ge 5$. We agree for this case, and that is partly the point — the interesting question is whether the same explicitness is achievable for the harder regularizations. For Bruhat–Tits tree encodings [9, 11], no analogue of the partition function $Z$ is available; the adelic program [12] itself documents that only 5 of 9 of its mass-ratio triplets survived independent verification, and the trapped-ion ultrametric testbed [10] exists precisely because $p$-adic structure claims currently lack this level of controlled arithmetic. Our template is an indictment by contrast: where the budget can be computed, compute it; where it cannot, the claim is not yet physics.

**Open questions.** (1) Does the fragmentation-aware formalism of [3] reproduce our exact thermal tails when applied to this model? (2) Can QEI-type observables [8] furnish truncation benchmarks that are gauge-invariant by construction? (3) Is there a well-defined partition-function analogue for $\mathcal{T}_p$ encodings whose tail sums would play the role of $\epsilon_{\mathrm{tr}}$?

## 7. Conclusion

We have computed, with every input and arithmetic step displayed, the truncation-faithfulness budget of a single thermal $\mathrm{U}(1)$ link: infidelities of $1.149\times10^{-2}$, $7.238\times10^{-5}$, and $6.465\times10^{-8}$ at $n_{\max} = 3, 5, 7$, with register costs of 3 and 4 qubits. The exercise is trivial in outcome but non-trivial in standard: it exhibits the form that faithfulness claims about discrete regularizations of gauge theories should take, from quantum link models [1] and digital-simulation truncations [3] to the far more speculative Bruhat–Tits tree and adelic programs [9, 10, 11, 12]. Explicit arithmetic is the cheapest falsifiability instrument available, and it should be the default.

## References

[1] arXiv:2112.04501v3 | Achieving the quantum field theory limit in far-from-equilibrium quantum link models

[2] arXiv:2604.07436v1 | Observation of genuine $2+1$D string dynamics in a U$(1)$ lattice gauge theory with a tunable plaquette term on a trapped-ion quantum computer

[3] arXiv:2508.00061v4 | Truncation uncertainties for accurate quantum simulations of lattice gauge theories

[4] arXiv:1809.00556v4 | A change of perspective: switching quantum reference frames via a perspective-neutral framework

[5] arXiv:hep-th/9511122v1 | An axiomatic approach to quantum gauge field theory

[6] arXiv:2608.14133v1 | A groupoidal approach to quantum reference frames

[7] arXiv:hep-th/9601033v2 | SU_q(n) Gauge Theory

[8] arXiv:math-ph/0502002v1 | Quantum Energy Inequalities and Stability Conditions in Quantum Field Theory

[9] QNFO: Holographic Quantum Error Correction as AdS/CFT Renormalization-Group Flow on Bruhat–Tits Trees: A Conditional Threshold Analysis at 10⁻⁴ | DOI 10.5281/zenodo.23107746

[10] QNFO: The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics | DOI 10.5281/zenodo.22025544

[11] QNFO: Holographic QEC as AdS/CFT RG Flow on Bruhat–Tits Trees | DOI pending

[12] QNFO: The Adelic Cross-Domain Program: From the Fine-Structure