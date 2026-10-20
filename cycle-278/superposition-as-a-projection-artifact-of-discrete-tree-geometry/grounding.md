# Grounding block - source: rem-rev-4708b98f-99be-4353-85a6-be6d4a2e4a6e

## Research idea

Superposition as a Projection Artifact of Discrete Tree Geometry. The conjecture: quantum superposition is not ontological but an artifact of projecting a single, definite path through a discrete, depth-organized tree of configurations onto a continuous, resolution-limited measurement basis. The wavefunction is a coarse-grained epistemic summary; collapse is Bayesian updating; the Born rule should emerge from how coarse-grained branch volumes scale with tree depth. Why it matters: it would dissolve the measurement problem and unify interpretations under one hidden-variable ontology with discrete, hierarchical (rather than continuous) hidden variables. How to test: (1) construct an explicit tree model and derive whether coarse-graining over equivalence classes reproduces the Hilbert-space formalism, including interference terms; (2) derive the Born rule from branch-counting/renormalization-group scaling and check it yields exactly |amplitude|², not merely qualitatively; (3) simulate double-slit and qubit scenarios to verify that projected tree paths reproduce quantum predictions; (4) search for Bell-inequality violations or deviations that distinguish this model from standard QM, since any empirically adequate hidden-variable tree must be nonlocal or contextual.

Source: owner notebook notes/v1/2026/05/02/_26122194417.md

Post-publication revision of the published paper "Superposition as a Projection Artifact of Discrete Tree Geometry" (version 1.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. C2: 'Analytical proof that branch-counting yields the Born rule P=|a|^2 for any two-path superposition' (Section 4 / 3.3). (confirmed by a second model)
2. Section 7c: 'If |f - P_target| > 3sigma... then the observed probability cannot be expressed as n/2^d for any integer d (since 0.625 = 5/8 is the only rational with denominator 2^3 that matches the target).' (confirmed by a second model)

## Existing paper under revision (remediation only)

# Superposition as a Projection Artifact of Discrete Tree Geometry

## Abstract
Quantum superposition underlies virtually every quantum technology, yet its ontological status remains contested. The present work addresses the gap between the continuous Hilbert‑space formalism and a hidden‑variable ontology by proposing that superposition arises from projecting a single, definite trajectory through a discrete, depth‑organized tree of configurations onto a resolution‑limited measurement basis. We construct an explicit binary‑branching tree model, derive the coarse‑graining that yields the standard wavefunction, and show that the Born rule is consistent with branch‑counting combined with a renormalisation‑group scaling of branch volumes. A concrete numerical example with depth $d=5$ demonstrates that the derived probability $P_{A}=0.625$ matches $|a|^{2}=0.625$ for amplitudes $a=\sqrt{0.625}$ and $b=\sqrt{0.375}$. The result suggests that the model can reproduce diagonal Born probabilities without invoking ontological multiplicity, though a full resolution of the measurement problem remains open, and that experimental tests can be designed by probing the discreteness scale of the underlying tree.  

## 1. Introduction
Laboratories building quantum computers, interferometers, and macroscopic‑superposition experiments face a persistent conceptual obstacle: the measurement problem. Engineers must design error‑correction protocols, yet the underlying theory offers no clear account of why a single outcome is observed when the formalism predicts a superposition of outcomes. If the superposition were merely an artifact of a hidden discrete structure, then the design of fault‑tolerant hardware could be guided by the scale at which the tree discretisation becomes relevant, potentially reducing overheads.  

The present paper shows that the apparent superposition observed in double‑slit interference, qubit rotations, and large‑scale Bose‑Einstein‑condensate experiments can be reproduced by a single deterministic path through a binary tree whose depth encodes the resolution of the measurement apparatus. Collapse then corresponds to Bayesian updating of the observer’s knowledge about which leaf of the tree was traversed. The Born rule emerges from the relative count of leaves associated with each coarse‑grained branch.  

**Contributions**  
- **C1.** Definition of a discrete binary‑branching tree model for quantum configurations and derivation of the coarse‑graining map to a wavefunction (Section 3).  
- **C2.** Analytical proof that branch‑counting yields the Born rule $P=|a|^{2}$ for any two‑path superposition (Section 4).  
- **C3.** Numerical illustration with depth $d=5$ showing $P_{A}=0.625$ matches the squared amplitude (Section 5).  
- **C4.** Discussion of experimental signatures and a minimal pilot test based on macroscopic superposition of a Bose‑Einstein condensate (Section 9).  

## 2. Background and Related Work
Discrete differential geometry provides a language for translating smooth geometric notions into combinatorial structures, as discussed in [1]. This insight motivates the representation of quantum configuration space as a discrete tree rather than a smooth manifold.  

Relativistic quantum thermodynamics discusses accelerated observers and their description via Rindler coordinates [2]. The Rindler coordinate expressions
$$
t = a^{-1}e^{a\xi}\sinh(a\tau),\qquad
x = a^{-1}e^{a\xi}\cosh(a\tau)
$$
illustrate how a change of observer path selects a different basis of field excitations. By analogy, each branch of the tree selects a distinct set of hidden variables that project onto the same measurement basis.  

  

  

  

  

  

  

## 3. Methods
### 3.1 Tree Construction
We define a rooted binary tree $\mathcal{T}$ of depth $d\in\mathbb{N}$. Each node at level $\ell$ ($0\le\ell\le d$) has two child nodes at level $\ell+1$. The total number of leaves is
$$
L = 2^{d}.
$$
A deterministic hidden‑variable trajectory corresponds to a unique leaf $\lambda\in\{1,\dots,L\}$.  

### 3.2 Coarse‑Graining Map
A measurement apparatus with resolution $\Delta$ cannot distinguish leaves that differ by fewer than $\Delta$ levels. We group leaves into equivalence classes $\mathcal{C}_{k}$, each containing $n_{k}$ leaves. The coarse‑grained state is represented by a complex amplitude
$$
\psi_{k} = \sqrt{\frac{n_{k}}{L}}\,e^{i\theta_{k}},
$$
where $\theta_{k}$ is a phase assigned by the underlying deterministic dynamics. The set $\{\psi_{k}\}$ forms the wavefunction in the effective Hilbert space.  

### 3.3 Derivation of the Born Rule
For a two‑path interferometer we consider two macroscopic branches $A$ and $B$ that correspond to two disjoint leaf sets $\mathcal{C}_{A}$ and $\mathcal{C}_{B}$ with cardinalities $n_{A}$ and $n_{B}$, respectively. The coarse‑grained amplitudes are
$$
a = \sqrt{\frac{n_{A}}{L}},\qquad b = \sqrt{\frac{n_{B}}{L}}.
$$
The probability of detecting the particle in branch $A$ after coarse‑graining is
$$
P_{A}=|a|^{2} = \frac{n_{A}}{L}.
$$
Since $n_{A}+n_{B}=L$, the complementary probability satisfies $P_{B}=|b|^{2}=1-P_{A}$. Thus the Born rule is consistent with leaf counting under the model's definition of amplitudes.  

### 3.4 Numerical Example Parameters
We select $d=5$ (depth five) to obtain $L=2^{5}=32$ leaves. We assign $n_{A}=20$ and $n_{B}=12$, yielding amplitudes
$$
a = \sqrt{\frac{20}{32}} = \sqrt{0.625},\qquad
b = \sqrt{\frac{12}{32}} = \sqrt{0.375}.
$$
The predicted detection probability for branch $A$ is $P_{A}=0.625$.  

## 4. Analysis
### 4.1 Leaf Count Verification
Given $d=5$,
$$ L = 2^{5} = 2\times2\times2\times2\times2 = 32. $$
**Step 1:** Compute $2^{5}$ by successive multiplication:
\[
2^{2}=4,\quad 2^{3}=8,\quad 2^{4}=16,\quad 2^{5}=32.
\]

### 4.2 Amplitude Calculation
\[
a = \sqrt{\frac{n_{A}}{L}} = \sqrt{\frac{20}{32}}.
\]
**Step 2:** Reduce the fraction $\frac{20}{32}= \frac{5}{8}=0.625$.
\[
a = \sqrt{0.625}.
\]
Using a calculator yields
\[
a \approx 0.790569415.
\]

Similarly,
\[
b = \sqrt{\frac{12}{32}} = \sqrt{\frac{3}{8}} = \sqrt{0.375}\approx 0.612372436.
\]

### 4.3 Probability Derivation
\[
P_{A}=|a|^{2}= (\sqrt{0.625})^{2}=0.625.
\]
**Step 3:** Square the amplitude:
\[
(\sqrt{0.625})^{2}=0.625.
\]

The complementary probability:
\[
P_{B}=1-P_{A}=1-0.625=0.375.
\]

Thus the branch‑counting rule reproduces the Born probabilities exactly for the chosen leaf distribution.

### 4.4 Connection to Circuit Capacity
An illustrative parameter dimension formula for a parametrised quantum circuit is:
\[
D_{\text{C}} = 2^{N+1} - 2.
\]
Setting $N=4$ qubits gives
\[
D_{\text{C}} = 2^{5} - 2 = 32 - 2 = 30.
\]
The exponential $2^{5}$ matches the leaf count $L$ for $d=5$, illustrating that the expressive capacity of a PQC scales identically to the number of hidden‑variable leaves at comparable depth.  

## 5. Results
The analytical derivation in Section 4 yields the following concrete numerical result:

- **R1.** For a binary tree of depth $d=5$ with leaf partition $n_{A}=20$, $n_{B}=12$, the coarse‑grained probability for branch $A$ is $P_{A}=0.625$, which equals $|a|^{2}$ for amplitude $a=\sqrt{0.625}$.

This result confirms that the Born rule is consistent with simple branch counting without invoking ontological multiplicity, given the model's assumptions. The correspondence $L=2^{d}=D_{\text{C}}$ for $N=4$ qubits further supports the claim that the hidden‑variable tree captures the same exponential growth of quantum state space as parametrised quantum circuits.

## 6. Discussion

In this section we deepen the analytical development introduced in Sections 3–5.  We first generalise the leaf‑counting derivation to arbitrary binary depth, then illustrate how the same combinatorial structure appears in the encoding of high‑dimensional quantum walks, and finally relate the discrete‑tree picture to informational and fractal perspectives drawn from the broader literature.  All quantitative steps are shown explicitly; where a numerical value is introduced without a direct source it is labelled as an **assumption**.

### 3.1 Generalised leaf‑counting probability for a binary tree

Recall the binary tree \(\mathcal{T}\) of depth \(d\in\mathbb{N}\) defined in Section 3.1.  The total number of leaves is  

\[
L(d)=2^{d}.
\]

Consider a coarse‑graining that groups the leaves into two macroscopic branches \(A\) and \(B\) with leaf counts \(n_{A}\) and \(n_{B}\) respectively, such that  

\[
n_{A}+n_{B}=L(d). \tag{1}
\]

The coarse‑grained amplitudes are defined as  

\[
a(d)=\sqrt{\frac{n_{A}}{L(d)}},\qquad 
b(d)=\sqrt{\frac{n_{B}}{L(d)}}. \tag{2}
\]

The probability of detecting the system in branch \(A\) after coarse‑graining is  

\[
P_{A}(d)=|a(d)|^{2}= \frac{n_{A}}{L(d)}. \tag{3}
\]

**Derivation of (3).**  
Insert (2) into the definition of probability:

\[
|a(d)|^{2}= \left(\sqrt{\frac{n_{A}}{L(d)}}\right)^{2}= \frac{n_{A}}{L(d)}.
\]

Because (1) guarantees \(n_{A}\le L(d)\), the ratio is a rational number of the form \(n/2^{d}\).  The complementary probability follows immediately:

\[
P_{B}(d)=1-P_{A}(d)=\frac{n_{B}}{L(d)}. \tag{4}
\]

Thus the Born rule emerges from a simple leaf‑counting argument for any depth \(d\).

### 3.2 Worked example: depth \(d=10\)

We now apply the general formula to a deeper tree.  **Assumption**: the tree remains perfectly balanced and binary.  Choose  

\[
d=10\;\Rightarrow\;L(10)=2^{10}=1024.
\]

Select a partition  

\[
n_{A}=640,\qquad n_{B}=384,
\]

which satisfies (1).  The amplitudes become  

\[
a(10)=\sqrt{\frac{640}{1024}}=\sqrt{0.625}=0.790569415,\qquad
b(10)=\sqrt{\frac{384}{1024}}=\sqrt{0.375}=0.612372436.
\]

The probabilities are  

\[
P_{A}(10)=\frac{640}{1024}=0.625,\qquad
P_{B}(10)=\frac{384}{1024}=0.375.
\]

These numbers reproduce the exact squared‑amplitude values used in the numerical illustration of Section 5 and demonstrate that the rational form \(n/2^{d}\) persists for any depth.

### 3.3 Connection to discrete‑time quantum walks

Discrete‑time quantum walks (DTQWs) provide an operational realisation of a binary branching process.  Reference [7] demonstrates discrete‑time quantum walks experimentally.

with \(\phi_{k}=0\) and \(\theta_{k}=k\Delta\theta\).  The coin toss is implemented by the unitary  

\[
S_{c}(\psi)=
\begin{pmatrix}
\cos\psi & -\sin\psi\\[2pt]
\sin\psi & \;\cos\psi
\end{pmatrix},
\tag{6}
\]

and the conditional shift by  

\[
T=\sum_{x}|x+1\rangle\langle x|\otimes|1\rangle_{c}\langle1|
   +\sum_{x}|x-1\rangle\langle x|\otimes|0\rangle_{c}\langle0|.
\tag{7}
\]

Each application of the combined step operator \(U=TS_{c}(\psi)\) doubles the number of reachable positions, exactly as a binary branching doubles the leaf count.  After \(d\) steps the walk can occupy \(2^{d}\) distinct position states, mirroring the leaf set \(\{\lambda\}\) of the hidden‑variable tree.  The mapping (5)‑(7) therefore furnishes a concrete laboratory realisation of the abstract tree model: the amplitudes associated with each leaf correspond to the complex coefficients of the walker's superposition over the \(2^{d}\) position basis states.

Because the encoding in [7] uses a *single* two‑dimensional qubit to represent an arbitrary \(n\)-dimensional state (see the method section of [7]), the number of independent parameters that can be stored scales as \(\log_{2}n\).  This logarithmic scaling matches the depth‑to‑leaf relationship \(L=2^{d}\) and reinforces the interpretation of depth \(d\) as the amount of information required to specify a leaf.

### 3.4 Information‑theoretic interpretation

The non‑Archimedean ontology presented in [9] treats every quantum state as a *unit of data storage* and identifies the Hamiltonian as a tool that measures the *hierarchical depth* of that information.  In the tree picture the depth \(d\) is precisely such a hierarchical measure: each increment of \(d\) adds one binary decision layer, increasing the informational resolution by one bit.  Consequently, the probability \(P_{A}=n_{A}/2^{d}\) can be read as the *fraction of information* allocated to branch \(A\) within the total information capacity \(2^{d}\) of the system.

Formally, let the information content of a leaf be one bit.  The total information capacity of the tree is  

\[
I_{\text{total}}(d)=L(d)\times 1 = 2^{d}\;\text{bits}.
\]

If a macroscopic branch \(A\) aggregates \(n_{A}\) leaves, its information content is  

\[
I_{A}=n_{A}\;\text{bits}.
\]

The *information‑fraction* is then  

\[
\frac{I_{A}}{I_{\text{total}}}= \frac{n_{A}}{2^{d}} = P_{A},
\]

which is exactly the Born probability derived in (3).  This identification provides a bridge between the combinatorial derivation and the informational viewpoint of [9].

### 3.5 Fractal superposition and interference geometry

  Within the tree model each leaf contributes a *wavelet* of unit amplitude; the coarse‑grained wavefunction is the algebraic sum over the leaf‑wavelets belonging to a given equivalence class \(\mathcal{C}_{k}\).  Because the leaf‑wavelets are arranged in a binary hierarchy, the resulting interference pattern exhibits a *fractal* self‑similarity: zooming into any branch reproduces the same binary branching structure at a finer scale.

To make this concrete, consider two branches \(A\) and \(B\) with leaf sets \(\mathcal{C}_{A}\) and \(\mathcal{C}_{B}\).  The coarse‑grained amplitudes are  

\[
\psi_{A}= \sum_{\lambda\in\mathcal{C}_{A}} \frac{1}{\sqrt{L}} e^{i\theta_{\lambda}},\qquad
\psi_{B}= \sum_{\lambda\in\mathcal{C}_{B}} \frac{1}{\sqrt{L}} e^{i\theta_{\lambda}}.
\tag{8}
\]

If the phases \(\theta_{\lambda}\) are uniformly distributed (an assumption compatible with the deterministic dynamics posited in Section 3.3), the cross term  

\[
2\operatorname{Re}\!\bigl(\psi_{A}^{*}\psi_{B}\bigr)
\]

averages to zero, leaving only the diagonal contributions \(|\psi_{A}|^{2}=n_{A}/L\) and \(|\psi_{B}|^{2}=n_{B}/L\).  This reproduces the Born rule while preserving the *geometric* interpretation of interference as the overlap of two self‑similar fractal sets.

### 3.6 Discrete hierarchy and experimental signatures

The Alpha Pi project [11] argues that the continuous real‑number field underlying standard quantum mechanics introduces a *fragility* that can be mitigated by adopting a *discrete hierarchy*.  In the tree model the hierarchy is explicit: each depth level corresponds to a discrete binary decision.  The project lists several experimental signatures of such a hierarchy, among them:

* deviations from standard quantum mechanics at ultra‑low energies,
* anisotropies in the fine‑structure constant \(\alpha\),
* discrete‑spacetime effects in cosmic‑ray events.

These signatures can be re‑interpreted in the present framework.  For example, a deviation at ultra‑low energy would correspond to a situation where the effective depth \(d_{\text{eff}}\) of the tree becomes comparable to the energy‑dependent coherence length, causing the observed probability to depart from the rational form \(n/2^{d_{\text{eff}}}\).  An anisotropy in \(\alpha\) could be modelled as a *non‑uniform branching factor* in different spatial directions, i.e. a tree that is locally binary but globally exhibits a slight bias in the distribution of leaves between branches.

### 3.7 Map‑territory distinction and coarse‑graining

The philosophical analysis in [12] emphasises that scientific models are *maps* of reality, not the territory itself, and that measurement necessarily introduces a *self‑referential* distortion.  The coarse‑graining map defined in Section 3.2 is precisely such a map: it collapses the fine‑grained leaf structure (the “territory”) onto a lower‑resolution wavefunction (the “map”).  The loss of information inherent in this projection is quantified by the ratio \(n_{k}/L\), which is exactly the probability assigned to the coarse‑grained outcome.  Thus the Born rule can be understood as a *measure of map fidelity*: the more leaves a coarse‑grained class contains, the higher the probability that the map will report that outcome.

### 3.8 Sensitivity analysis: irregular branching

All derivations above assume a perfectly balanced binary tree.  To assess robustness we introduce a *branching factor* \(\beta_{\ell}\in\{1,2\}\) at each level \(\ell\).  The total leaf count becomes  

\[
L_{\text{irr}}=\prod_{\ell=1}^{d}\beta_{\ell}. \tag{9}
\]

If a single level \(\ell^{*}\) has \(\beta_{\ell^{*}}=1\) (i.e. no branching at that level), the leaf count is reduced by a factor of two relative to the balanced case.  The probability for a branch that still contains \(n_{A}\) leaves is  

\[
P_{A}^{\text{irr}}=\frac{n_{A}}{L_{\text{irr}}}. \tag{10}
\]

Thus any deviation from perfect binary branching simply rescales the denominator in (3).  The *shape* of the Born rule (probability proportional to leaf fraction) is preserved, but the absolute numerical values shift.  This observation aligns with the limitation noted in Section 6.1 (Assumption A1) and demonstrates that the rule is robust to modest irregularities.

### 3.9 Worked example with irregular branching

Consider a depth‑\(d=5\) tree where level \(\ell=3\) fails to branch (\(\beta_{3}=1\)) while all other levels branch normally (\(\beta_{\ell}=2\) for \(\ell\neq3\)).  Equation (9) yields  

\[
L_{\text{irr}} = 2^{4}\times1 = 16.
\]

Choose a partition \(n_{A}=10\), \(n_{B}=6\) (satisfying \(n_{A}+n_{B}=L_{\text{irr}}\)).  The probabilities become  

\[
P_{A}^{\text{irr}} = \frac{10}{16}=0.625,\qquad
P_{B}^{\text{irr}} = \frac{6}{16}=0.375,
\]

identical to the balanced case of Section 4 because the chosen leaf numbers happen to give the same ratios.  However, if we instead chose \(n_{A}=9\), \(n_{B}=7\) we would obtain  

\[
P_{A}^{\text{irr}} = \frac{9}{16}=0.5625,\qquad
P_{B}^{\text{irr}} = \frac{7}{16}=0.4375,
\]

demonstrating how irregular branching can produce probabilities that are still rational with denominator \(2^{d-1}\) rather than \(2^{d}\).

### 3.10 Summary of extended derivations

* The leaf‑counting argument yields the Born rule for any binary depth \(d\) (Eq. 3).  
* Numerical illustration at \(d=10\) confirms the rational probability form (Section 3.2).  
* Discrete‑time quantum walks implement the same binary branching in a laboratory setting, with the encoding method of [7] providing a concrete mapping between walk positions and tree leaves.  
* An information‑theoretic reading of depth as hierarchical information matches the probability as an information‑fraction (Section 3.4, [9]).  
* The fractal superposition perspective of [10] explains why cross terms vanish under uniform phase assumptions, preserving the Born rule while retaining a geometric interpretation of interference.  
* Potential experimental signatures listed in [11] can be re‑expressed as deviations from the rational form \(n/2^{d}\) when the effective depth changes or branching becomes anisotropic.  
* The map‑territory distinction of [12] frames coarse‑graining as a deliberate loss of leaf‑level detail, with the Born probabilities quantifying that loss.  
* Sensitivity to irregular branching is captured by Eq. (9)–(10), showing that the rule is structurally stable but numerically sensitive to the total leaf count.

These extended derivations reinforce the central claim that quantum superposition and the Born rule can be understood as emergent artifacts of a discrete, depth‑organized tree geometry, while simultaneously connecting the model to experimental platforms, information theory, fractal geometry, and philosophical analysis.

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and decision impact  
Quantum hardware designers and experimental physicists who build interferometers, trapped‑atom platforms, or parametrised quantum circuits would use the branch‑counting result to assess the depth $d$ at which the hidden‑variable tree becomes relevant. If the model holds, the design decision “choose measurement resolution $\Delta$ such that the effective depth $d$ exceeds the decoherence length” replaces the current heuristic of “minimise error‑correction overhead”. In practice this means selecting detector bandwidths, timing jitter tolerances, and control‑pulse granularity that guarantee $d\ge d_{\text{crit}}$, where $d_{\text{crit}}$ is the smallest integer for which the rational probability $n/2^{d}$ reproduces the observed outcome within experimental uncertainty.

### (b) Technology readiness  
The work is purely analytical and has not undergone peer review; therefore it resides at **Technology Readiness Level 2** (formulation of concept and analytical studies). No hardware or software prototype has been built.

### (c) Minimal next experiment to de‑risk or falsify  
A feasible pilot test is a Mach‑Zehnder interferometer with a Bose‑Einstein‑condensate source, as described in the macroscopic‑superposition experiment of [4]. The experiment would vary the path‑length difference to target a target probability $P_{\text{target}}=0.625$ (the rational value $5/8$).

*Measurement:* Record the relative frequency $f$ of detections in one output port over $N=10^{4}$ trials.
*Falsification criterion:* If $|f-P_{\text{target}}|>3\sigma$, where $\sigma=\sqrt{P_{\text{target}}(1-P_{\text{target}})/N}$, then the observed probability cannot be expressed as $n/2^{d}$ for any integer $d$ (since $0.625=5/8$ is the only rational with denominator $2^{3}$ that matches the target). Such a deviation would falsify the branch‑counting hypothesis.

### (d) First‑order engineering constraints  
| Constraint | Source / Derivation |
|------------|----------------------|
| **Discrete resolution mapping** – the measurement apparatus must provide an integer‑valued resolution $\Delta$ that can be mapped to a depth $d$ (Section 3.2). | Derived from the definition of coarse‑graining in the model. |
| **Phase stability** – the deterministic dynamics that assign phases $\theta_{k}$ must remain stable across the $2^{d}$ leaves to avoid spurious cross terms (Section 3.3). | Assumption A3 in the limitation list; required for the uniform‑phase argument in Section 6. |
| **Decoherence control** – the coherence length of the system must exceed the effective tree depth $d$ so that the hidden‑variable trajectory is not destroyed before measurement (Section 6.1). | Directly follows from the need that the leaf count $L=2^{d}$ be physically meaningful. |
| **Branching regularity** – the tree must be approximately binary; irregular branching changes the denominator in Eq. (10) (Section 3.8). | Explicitly derived in the sensitivity analysis of Section 3.8. |
| **Calibration of leaf‑fraction** – the mapping $n_{A}/L$ to observed probabilities requires precise calibration of the detector’s counting efficiency. | Implicit in the probability derivation $P_{A}=n_{A}/L$ (Eq. 3). |

Constraints not yet quantified (e.g., exact jitter tolerances, required laser phase noise) remain **open questions** pending experimental data.

### (e) Projected cost and performance (projection)  
Assume a classical simulation of the hidden‑variable tree on a workstation with cost $c_{\text{leaf}} = 10^{-3}$ per leaf (a typical memory‑access cost for a simple lookup). For a depth $d = 10$ the leaf count is $L = 2^{10} = 1024$. The projected simulation cost is  

$$
C_{\text{sim}} = c_{\text{leaf}} \times L = 10^{-3} \times 1024 \approx 1.024.
$$

*Assumptions:* $c_{\text{leaf}}$ is an order‑of‑magnitude estimate for a single‑precision floating‑point operation; the simulation stores only the leaf index and a phase value. This projection is intended solely to illustrate the linear scaling $C_{\text{sim}}\propto2^{d}$ derived from Eq. (9).

### (f) Direct risks and misuse paths  
If the model were misapplied to claim that quantum randomness is entirely deterministic, it could be used to argue against the necessity of genuine quantum randomness in cryptographic key generation. The present work does **not** eliminate intrinsic randomness; it only provides a hidden‑variable reinterpretation that reproduces the statistical predictions. Misuse would therefore arise from over‑extending the conclusion beyond the scope of the derived branch‑counting rule. Users must retain standard security assumptions that rely on certified quantum randomness.
- **Assumption A1.** The tree is strictly binary and perfectly balanced; real physical systems may exhibit irregular branching.  
- **Assumption A2.** Coarse‑graining groups leaves solely by depth, ignoring possible phase correlations beyond simple counting.  
- **Assumption A3.** The mapping from leaf counts to amplitudes assumes uniform phase distribution; non‑uniform phases could modify interference terms.  
- **Assumption A4.** The resolution $\Delta$ of the measurement apparatus is treated as a fixed integer number of levels; in practice it may be continuous.  

Sensitivity analysis shows that deviations from a balanced binary structure alter $L$ and thus the derived probabilities. However, as long as the total leaf count remains $2^{d}$ and the partition ratios $n_{A}/L$, $n_{B}/L$ are preserved, the Born rule holds.

### 7.2 Potential Falsification
A single observation that would falsify the main claim is the detection of a probability $P$ that cannot be expressed as a rational ratio $n/L$ with integer $n$ and $L=2^{d}$ for any integer depth $d$. For example, measuring $P=0.333\ldots$ (exactly $1/3$) in a two‑path interferometer would contradict the branch‑counting prediction, because $1/3$ cannot be written as $n/2^{d}$ for any integer $n$ and $d$.

### 7.3 Open Questions
- How does the model accommodate continuous phase evolution and interference fringes beyond simple amplitude magnitudes?  
- Can the tree structure be generalised to non‑binary branching to capture higher‑dimensional Hilbert spaces?  
- What is the relationship between the tree depth $d$ and physical parameters such as decoherence time or spatial separation in macroscopic superpositions?



### (a) Intended users and decision impact  
Quantum hardware designers and experimental physicists who build interferometers, trapped‑atom platforms, or parametrised quantum circuits would use the branch‑counting result to assess the depth $d$ at which the hidden‑variable tree becomes relevant. If the model holds, the design decision “choose measurement resolution $\Delta$ such that the effective depth $d$ exceeds the decoherence length” replaces the current heuristic of “minimise error‑correction overhead”. In practice this means selecting detector bandwidths, timing jitter tolerances, and control‑pulse granularity that guarantee $d\ge d_{\text{crit}}$, where $d_{\text{crit}}$ is the smallest integer for which the rational probability $n/2^{d}$ reproduces the observed outcome within experimental uncertainty.  

### (b) Technology readiness  
The work is purely analytical and has not undergone peer review; therefore it resides at **Technology Readiness Level 2** (formulation of concept and analytical studies). No hardware or software prototype has been built.

### (c) Minimal next experiment to de‑risk or falsify  
A feasible pilot test is a Mach‑Zehnder interferometer with a Bose‑Einstein‑condensate source, as described in the macroscopic‑superposition experiment of [4]. The experiment would vary the path‑length difference to target a target probability $P_{\text{target}}=0.625$ (the rational value $5/8$).  

*Measurement:* Record the relative frequency $f$ of detections in one output port over $N=10^{4}$ trials.  
*Falsification criterion:* If $|f-P_{\text{target}}|>3\sigma$, where $\sigma=\sqrt{P_{\text{target}}(1-P_{\text{target}})/N}$, then the observed probability cannot be expressed as $n/2^{d}$ for any integer $d$ (since $0.625=5/8$ is the only rational with denominator $2^{3}$ that matches the target). Such a deviation would falsify the branch‑counting hypothesis.

### (d) First‑order engineering constraints  
| Constraint | Source / Derivation |
|------------|----------------------|
| **Discrete resolution mapping** – the measurement apparatus must provide an integer‑valued resolution $\Delta$ that can be mapped to a depth $d$ (Section 3.2). | Derived from the definition of coarse‑graining in the model. |
| **Phase stability** – the deterministic dynamics that assign phases $\theta_{k}$ must remain stable across the $2^{d}$ leaves to avoid spurious cross terms (Section 3.3). | Assumption A3 in the limitation list; required for the uniform‑phase argument in Section 6. |
| **Decoherence control** – the coherence length of the system must exceed the effective tree depth $d$ so that the hidden‑variable trajectory is not destroyed before measurement (Section 6.1). | Directly follows from the need that the leaf count $L=2^{d}$ be physically meaningful. |
| **Branching regularity** – the tree must be approximately binary; irregular branching changes the denominator in Eq. (10) (Section 3.8). | Explicitly derived in the sensitivity analysis of Section 3.8. |
| **Calibration of leaf‑fraction** – the mapping $n_{A}/L$ to observed probabilities requires precise calibration of the detector’s counting efficiency. | Implicit in the probability derivation $P_{A}=n_{A}/L$ (Eq. 3). |

Constraints not yet quantified (e.g., exact jitter tolerances, required laser phase noise) remain **open questions** pending experimental data.

### (e) Projected cost and performance (projection)  
Assume a classical simulation of the hidden‑variable tree on a workstation with cost $c_{\text{leaf}}=10^{-3}$ per leaf (a typical memory‑access cost for a simple lookup). For a depth $d=10$ the leaf count is $L=2^{10}=1024$. The projected simulation cost is  

\[
C_{\text{sim}} = c_{\text{leaf}}\times L = 10^{-3} \times 1024 \approx 1.024.
\]

*Assumptions:* $c_{\text{leaf}}$ is an order‑of‑magnitude estimate for a single‑precision floating‑point operation; the simulation stores only the leaf index and a phase value. This projection is intended solely to illustrate the linear scaling $C_{\text{sim}}\propto2^{d}$ derived from Eq. (9).

### (f) Direct risks and misuse paths  
If the model were misapplied to claim that quantum randomness is entirely deterministic, it could be used to argue against the necessity of genuine quantum randomness in cryptographic key generation. The present work does **not** eliminate intrinsic randomness; it only provides a hidden‑variable reinterpretation that reproduces the statistical predictions. Misuse would therefore arise from over‑extending the conclusion beyond the scope of the derived branch‑counting rule. Users must retain standard security assumptions that rely on certified quantum randomness.

## 9. Conclusion
### 9.1 Intended Users and Design Impact
Quantum hardware designers and experimental physicists would use the result to assess the scale at which hidden‑variable discreteness becomes relevant. If the depth $d$ corresponding to a given experimental resolution is known, designers can predict the minimal leaf count required to reproduce observed probabilities, potentially informing error‑correction thresholds and measurement bandwidth specifications.

### 9.2 Technology Readiness Level
The work is purely analytical and has not undergone peer review; therefore it resides at **TRL 2** (formulation of concept and analytical studies).

### 9.3 Minimal Next Experiment
A feasible pilot test involves a Mach‑Zehnder interferometer with a Bose‑Einstein condensate source as in [4]. By varying the path‑length difference to achieve a target probability $P=0.625$, the experiment can test whether the observed probability can be expressed as $n/2^{d}$ for some integer $d$. A measured probability deviating from any such rational ratio would refute the tree‑projection hypothesis.

### 9.4 Engineering Constraints
- **Discrete Resolution:** The measurement apparatus must have a well‑characterised resolution $\Delta$ that can be mapped to an integer tree depth $d$.  
- **Phase Stability:** Maintaining phase coherence across the two branches is essential to isolate the effect of leaf counting from conventional interference.  
- **Decoherence Control:** Environmental decoherence must be suppressed below the scale at which the tree discretisation would manifest, as suggested by macroscopic superposition experiments [4].

### 9.5 Projected Performance Bounds
Assuming a depth $d=10$ (leaf count $L=1024$) and a partition $n_{A}=640$, $n_{B}=384$, the projected probability for branch $A$ is
\[
P_{A}= \frac{640}{1024}=0.625.
\]
This projection relies on the assumptions of a balanced binary tree and uniform phase distribution.

### 9.6 Risks and Misuse
If the model were misapplied to claim that quantum randomness is entirely deterministic, it could be misused to argue against the need for genuine quantum randomness in cryptographic protocols. The present work does not claim to eliminate intrinsic randomness; it merely provides a hidden‑variable reinterpretation that reproduces standard statistical predictions.

## 10. Conclusion
We have presented a discrete‑tree hidden‑variable model that reproduces the standard quantum superposition formalism through a projection onto a coarse‑grained measurement basis. By explicit branch counting we derived the Born rule and demonstrated quantitative agreement with a concrete numerical example. The model aligns with existing literature on discrete geometry [1] and observer‑dependent mode selection [2]. The framework offers a clear pathway for experimental falsification and suggests that the measurement problem may be resolved without invoking ontological multiplicity. Future work will extend the model to incorporate phase dynamics, irregular branching, and connections to non‑commutative geometry [8].

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.1-proportionate-notice). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 15 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Discrete differential geometry. Consistency as integrability. arXiv:math/0504358v1. https://arxiv.org/abs/math/0504358v1
[2] Superpositions of thermalisations in relativistic quantum field theory. arXiv:2307.02593v2. https://arxiv.org/abs/2307.02593v2
[4] Verifying quantum superpositions at metre scales. arXiv:1607.01454v2. https://arxiv.org/abs/1607.01454v2
[7] Experimental demonstration of quantum walks with initial superposition states. arXiv:1805.09784v3. https://arxiv.org/abs/1805.09784v3
[8] The rings of noncommutative projective geometry. arXiv:math/0205005v2. https://arxiv.org/abs/math/0205005v2
[9] https://papers.qnfo.org/papers/unified-theory-of-non-archimedean-ontology. QNFO: Unified Theory of Non-Archimedean Ontology.
[10] https://papers.qnfo.org/papers/treatise-on-waves. QNFO: Waves Do Math.
[11] https://papers.qnfo.org/papers/alpha-pi-project. QNFO: Alpha Pi Project.
[12] https://papers.qnfo.org/papers/principia-ontologica. QNFO: Principia Ontologica.

## Appendix A. Divergence report
*The following points represent substantive disagreements between Draft A and Draft B. The main text adopts the convention of Draft A (branch counting yields the Born rule). The divergent claims are documented here for transparency.*

- **D1.** Draft B argues that uniform branch counting cannot derive the Born rule because the probability measure $p_i = f_i$ (with $f_i$ the leaf‑fraction) only matches $|a_i|^{2}$ if the volume fractions are already set to $|a_i|^{2}$. Draft A treats the equality as a derivation, not a circular assumption.  
- **D2.** Draft B introduces a power‑law measure $p_i = f_i^{\gamma}$ and shows that only $\gamma=1$ normalises for all partitions, concluding that any $\gamma\neq1$ fails. Draft A does not consider alternative exponents.  
- **D3.** Draft B presents an interference test showing that non‑negative coarse‑graining measures cannot reproduce the quantum cross term $2\,\mathrm{Re}(a_1^{*}a_2)$ without encoding phase ontologically. Draft A assumes phase $\theta_k$ is supplied by the deterministic dynamics and does not analyse this constraint.  
- **D4.** Draft B derives the CHSH bound $|S|\le 2$ for deterministic leaf assignments, concluding that the tree model must be non‑local or contextual to match quantum predictions. Draft A does not address Bell‑type inequalities.  

## Appendix B. Claim attribution
| Claim ID | Source Draft(s) | Agreement |
|----------|----------------|-----------|
| C1 | A, B | CONVERGENT |
| C2 | A, B | CONVERGENT |
| C3 | A, B | CONVERGENT |
| C4 | A, B | CONVERGENT |
| C5 | A, B | CONVERGENT |
| D1 | A (supports), B (contradicts) | DIVERGENT |
| D2 | B only | SINGLE |
| D3 | B only | SINGLE |
| D4 | B only | SINGLE |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:math/0504358v1 | Discrete differential geometry. Consistency as integrability
arXiv:2307.02593v2 | Superpositions of thermalisations in relativistic quantum field theory
arXiv:2207.00021v3 | Quantum conformal symmetries for spacetimes in superposition
arXiv:1607.01454v2 | Verifying quantum superpositions at metre scales
arXiv:2101.11628v2 | Spacetime Quantum Reference Frames and superpositions of proper times
arXiv:2102.01659v2 | Capacity and quantum geometry of parametrized quantum circuits
arXiv:1805.09784v3 | Experimental demonstration of quantum walks with initial superposition states
arXiv:math/0205005v2 | The rings of noncommutative projective geometry

## QNFO corpus context (Vectorize)

QNFO: Unified Theory of Non-Archimedean Ontology | https://papers.qnfo.org/papers/unified-theory-of-non-archimedean-ontology
QNFO: Waves Do Math | https://papers.qnfo.org/papers/treatise-on-waves
QNFO: Alpha Pi Project | https://papers.qnfo.org/papers/alpha-pi-project
QNFO: Principia Ontologica | https://papers.qnfo.org/papers/principia-ontologica

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:math/0504358v1 | Discrete differential geometry. Consistency as integrability
  A new field of discrete differential geometry is presently emerging on the border between differential and discrete geometry. Whereas classical differential geometry investigates smooth geometric shapes (such as surfaces), and discrete geometry studies geometric shapes with finite number of elements (such as polyhedra), the discrete differential geometry aims at the development of discrete equival
  Full text (https://arxiv.org/html/math/0504358v1), excerpts of its own sections:
  § Chapter 0 Introduction: A new field of discrete differential geometry is presently emerging on the border between differential and discrete geometry. Whereas classical differential geometry investigates smooth geometric shapes (such as surfaces), and discrete geometry studies geometric shapes with finite number of elements (such as polyhedra), the discrete differential geometry aims at the development of discrete equivalents of notions and methods of smooth surface theory. Current interest in this field derives not only from its importance in pure mathematics but also from its relevance for other fields like computer graphics. Recent progress in discrete differential geometry has lead, somewhat unexpectedly, to a better understanding of some fundamental structures lying in the basis of the classical differential geometry and of the theory of integrable systems (this is schematically presented on Fig.  1 ). The goal of this book is to give a systematic presentation of current achievements in this field. [...]
  § Chapter 1 Classical differential geometry: In this chapter we discuss some classical results of the differential geometry of nets (parametrized surfaces and coordinate systems) in ${\mathbb{R}}^{N}$ , mainly concentrated around the topics of transformations of nets and of their permutability properties. This classical area was very popular in the differential geometry of the 19th and of the first quarter of the 20th century, and is well documented in the fundamental treatises [ Bi , Da1 , Da2 , E1 , E2 , Tzi ] and others. Our presentation mainly follows these classical treatments, of course with modifications which reflect our present points of view. We do not trace back the exact origin of the concrete classical results: often enough this turns out to be a complicated task in the history of mathematics which still waits for its competent investigation. [...]
  § 1.1 Conjugate nets and their transformations: Conjugate nets. This classical notion can be defined as follows. Definition 1.1 A map $f:{\mathbb{R}}^{m}\to{\mathbb{R}}^{N}$ is called an $m$ -dimensional conjugate net in ${\mathbb{R}}^{N}$ , if $\partial_{i}\partial_{j}f\in{\rm span}(\partial_{i}f,\partial_{j}f)$ at any $u\in{\mathbb{R}}^{m}$ and for all pairs $1\leq i\neq j\leq m$ . A parametrized surface in the three-space ( $m=2$ , $N=3$ ) is a conjugate net, if its second fundamental form is diagonal in this parametrization. Such a parametrization exists for a general surface in the three-space. It is important to note that Definition 1.1 , as well as Definition 1.2 below, are dealing with projectively invariant notions only, and thus belong to the projective differential geometry. In this setting the space ${\mathbb{R}}^{N}$ where conjugate net lives should be interpreted as an affine part of ${\mathbb{P}}({\mathbb{R}}^{N+1})$ . [...]
  § 1.2 Orthogonal nets and their transformations: Orthogonal nets. An important subclass of conjugate nets is fixed in the following definition. Definition 1.4 A conjugate net $f:{\mathbb{R}}^{m}\to{\mathbb{R}}^{N}$ is called an $m$ -dimensional O-net (orthogonal net) in ${\mathbb{R}}^{N}$ , if there holds $\partial_{i}f\perp\partial_{j}f\,$ at any $u\in{\mathbb{R}}^{m}$ and for all $1\leq i\neq j\leq m$ . Such a net is called an orthogonal coordinate system if $m=N$ . Two-dimensional $(m=2)$ orthogonal nets are called O-surfaces . An O-surface in ${\mathbb{R}}^{3}$ is nothing but a surface parametrized along its curvature lines, or, otherwise said, parametrized so that both the first and the second fundamental forms are diagonal. [...]
[2] arXiv:2307.02593v2 | Superpositions of thermalisations in relativistic quantum field theory
  Recent results in relativistic quantum information and quantum thermodynamics have independently shown that in the quantum regime, a system may fail to thermalise when subject to quantum-controlled application of the same, single thermalisation channel. For example, an accelerating system with fixed proper acceleration is known to thermalise to an acceleration-dependent temperature, known as the U
  Full text (https://arxiv.org/html/2307.02593v2), excerpts of its own sections:
  § 1 Introduction: Historically, quantum thermodynamics has sought to establish the laws of classical thermodynamics from quantum mechanics [ 1 , 2 ] . A key development in the field was the Markovian master equation proposed by Lindblad and Gorini-Kossakowski-Sudarshan [ 3 , 4 ] , which supplied a framework for analysing the quantum dynamics of systems interacting with an environment [ 5 ] . Apart from its fundamental significance, quantum thermodynamics is closely tied to applied research fields such as ultracold atomic systems [ 6 ] and quantum information processing [ 7 ] , both widely regarded as forming the basis of emerging quantum technologies. Beyond this, quantum thermodynamics motivates a related set of fundamental questions, namely how one characterises classical, macroscopic phenomena such as energy, work, and temperature when they are subject to quantum indeterminacy. [...]
  § 2.1 Rindler Coordinates: Let us first review the Rindler coordinates, describing uniformly accelerated observers in Minkowski spacetime. The worldline of a uniformly accelerated observer in the right Rindler wedge of Minkowski spacetime, for which we use coordinates $(t,x,y,z)$ , can be described in terms of the Rindler coordinates $(\tau,\xi,y,z)$ [ 31 ] , $\displaystyle t$ $\displaystyle=a^{-1}e^{a\xi}\sinh(a\tau),\vphantom{\frac{1}{2}}$ (1) $\displaystyle x$ $\displaystyle=a^{-1}e^{a\xi}\cosh(a\tau),\vphantom{\frac{1}{2}}$ (2) with all other coordinates constant, where $\tau$ and $a$ are the proper time and acceleration of the observer. [...]
  § 2.2 Diamond Coordinates: The Rindler coodinates define unbounded regions of spacetime that partition Minkowski spacetime into disjoint regions. Another set of coordinates that possesses a similar feature are those parametrising so-called spacetime diamonds. Interest in this coordinate system increased following Martinetti and Rovelli’s application of the thermal time hypothesis to derive the diamond temperature for finite-lifetime observers, a generalisation of the Unruh effect for such observers [ 39 , 40 ] . More recently it has been proposed as a way of witnessing vacuum entanglement [ 41 , 42 , 43 ] and has attracted interest due to its relevance for conformal quantum mechanics [ 44 , 45 ] and its relationship with the de Sitter universe [ 46 , 47 , 48 , 49 , 50 ] . A static observer (who stays at $\mathbf{r}=(x,y,z)=0$ ) with a finite lifetime lives in a diamond, defined as the overlapping region between the future and past lightcones at their birth and death respectively [ 41 , 40 , 39 ] . [...]
  § 7 Conclusion: In this paper, we have pinpointed the physical origin of recent results where quantum probes interacting with a superposition of seemingly invariant states of environment nevertheless do not thermalise. We have shown that the fundamental reason for this nonthermalisation is the fact that for each amplitude the probe interacts with a different set of modes, eg modes localised in a Rindler wedge arising from a given accelerated motion. For spatial superpositions of such motions, the relevant field modes with which the probe can interact are incommensurate and correlated in a complicated manner, resulting in general in a different than Planckian distribution of particles accessible to such a superposed observer or probe. As a result, dynamics of any probe interacting with a field in a such a scenario would lack a detailed balanced-satisfying response, as shown in the present work on concrete examples. On the other hand, when the involved modes are orthogonal or identical, thermality is recovered. [...]
[3] arXiv:2207.00021v3 | Quantum conformal symmetries for spacetimes in superposition
  Without a complete theory of quantum gravity, the question of how quantum fields and quantum particles behave in a superposition of spacetimes seems beyond the reach of theoretical and experimental investigations. Here we use an extension of the quantum reference frame formalism to address this question for the Klein-Gordon field residing on a superposition of conformally equivalent metrics. Based
  Full text (https://arxiv.org/html/2207.00021v3), excerpts of its own sections:
  § 1 Introduction: Imagine you are living in a universe expanding in a quantum superposition of different Hubble rates. How would fields and particles behave in such a world? Since we lack a complete and generally accepted theory of quantum gravity, an answer to this question remains currently out of reach. Here, we employ an extension of the quantum reference frame formalism to relate this exotic situation to a corresponding one that is more easily captured by quantum field theory on curved spacetime (QFTCS). More precisely, we map a massive Klein-Gordon (KG) field that resides on a superposition of conformally related spacetimes to a KG field with a superposition of mass parameters on a fixed spacetime. In that way, we establish an equivalence between a situation with a superposition of spacetimes and one with a definite, classical spacetime. Doing so, we identify an additional symmetry of the KG equation – a quantum conformal symmetry – which goes beyond its invariance under diffeomorphisms. [...]
  § 2 Conformal invariance: Symmetries of the KG Field: Let us start by reviewing the symmetry properties of the Klein-Gordon (KG) equation in curved spacetime, $\displaystyle\square_{g}\phi(x)\equiv g^{\mu\nu}\nabla_{\mu}\nabla_{\nu}\phi(x)=m^{2}\phi(x).$ (1) While the standard KG equation is not invariant under conformal transformations, it has been shown [ 24 ] that by adding a non-minimal coupling term, the new equation $\displaystyle(\square_{g}+\xi R)\phi(x)=m^{2}\phi(x)$ (2) is invariant under $g_{ab}\to\Omega^{2}(x)g_{ab}$ and $\phi\to\Omega^{-1}(x)\phi$ only for $\xi=\frac{1}{6}$ and $m=0$ . 1 1 1 Here, we use abstract index notation for tensors, which indicates the type of object in a coordinate-free way rather than its components in any particular basis. The coupling term $\xi R$ can also be interpreted as contributing to the mass of the KG field. 2 2 2 A justification for this step can be seen by inspecting the action for the KG field in a non-dynamical spacetime: $\mathcal{S}=\int_{M}d^{4}x\sqrt{-g}\left(\frac{1}{2}g^{\mu\nu}\partial_{\mu}\phi\partial_{\nu}\phi-\xi R\phi^{2}+\frac{1}{2}m^{2}\phi^{2}\right)$ . [...]
  § 3 Superpositions of Spacetimes and Quantum Conformal Transformations: Let us now turn to the main objective of this work: elevating the classical symmetries studied above to the quantum level. First, let us note that the conformal invariance not only holds for the classical KG field but also for the quantized one. For a revision of the quantization of a scalar KG field, see App. C . [...]
  § 5 Conclusion: We started this work by asking the question of how fields and particles would behave in a universe that is expanding in a quantum superposition of different Hubble rates. By exploiting a particular symmetry of the Klein-Gordon equation, we showed that this situation corresponds to one in which a field in superposition of different spacetime-dependent effective masses inhabits a definite Minkowski spacetime. More concretely, we constructed an operator $\hat{\mathcal{S}}$ , which maps between quantum states describing these two situations. This allowed us to formalize a new extended symmetry principle: an invariance under quantum conformal transformations, which manifests in the equivalence of states that are related by the action of $\mathcal{\hat{S}}$ . Besides providing a deeper intuition for the meaning of quantum fields on geometries in superposition, we further utilized this symmetry to derive the equivalent of cosmological particle production in Minkowski spacetime with modified mass in superposition. [...]
[4] arXiv:1607.01454v2 | Verifying quantum superpositions at metre scales
  While the existence of quantum superpositions of massive particles over microscopic separations has been established since the birth of quantum mechanics, the maintenance of superposition states over macroscopic separations is a subject of modern experimental tests. In Ref. [1], T. Kovachy et al. report on applying optical pulses to place a freely falling Bose-Einstein condensate into a superposit
  Full text (https://ar5iv.labs.arxiv.org/html/1607.01454v2), excerpts of its own sections:
  § Submission history: From: Dan Stamper-Kurn [ view email ] [v1] Wed, 6 Jul 2016 01:38:27 UTC (86 KB) [v2] Fri, 15 Jul 2016 21:38:16 UTC (86 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Verifying quantum superpositions at metre scales, by Dan M. Stamper-Kurn and 2 other authors View PDF view license
  § Current browse context:: quant-ph < prev | next > new | recent | 2016-07 Change to browse by: physics physics.atom-ph
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[5] arXiv:2101.11628v2 | Spacetime Quantum Reference Frames and superpositions of proper times
  In general relativity, the description of spacetime relies on idealised rods and clocks, which identify a reference frame. In any concrete scenario, reference frames are associated to physical systems, which are ultimately quantum in nature. A relativistic description of the laws of physics hence needs to take into account such quantum reference frames (QRFs), through which spacetime can be given 
  Full text (https://arxiv.org/html/2101.11628v2), excerpts of its own sections:
  § 1 Introduction: In both quantum theory and general relativity, spacetime is treated as an abstract entity. In quantum theory, spacetime is considered as a fixed, non-dynamical background providing an arena for physical phenomena. In general relativity, spacetime is a dynamical quantity, which is influenced by a change in the configuration of massive bodies. In both cases, spacetime coordinates acquire meaning via rods and clocks, which identify a reference frame. However, these rods and clocks, and hence reference frames, are typically treated as idealised classical systems. In this sense, the description of spacetime is not fully operational. Reference frames are very useful to specify the point of view from which observations are carried out. Although measurements are usually made in a specific reference frame, all physical laws are formulated in a way that is independent of the reference frame chosen, thanks to the principle of general covariance. This means that there is no preferred reference frame. [...]
  § 2 From a covariant timeless model to relational dynamics in a locally inertial quantum reference frame: \includegraphics [scale=0.35]GlobalModel Figure 1: We consider a system of $N$ relativistic quantum particles in a weak gravitational field produced by a mass $M$ . Each particle has a quantum state representing its position in the spacetime diagram, as well as a clock state (the hands of the clocks) which keeps the proper time in the particle’s frame. We introduce a timeless model, in which the global state of the $N$ particles and of the mass $M$ is “frozen”, and is described by an $N$ -particle quantum state in spacetime. Concretely, this means that the quantum state of the external variables can be, for instance, in a quantum superposition of coordinate times $x^{0}$ and spatial coordinates $\mathbf{x}$ . Classically, the position in spacetime and the velocity of a particle influence its proper time due to relativistic time dilation. When the particle is in a quantum superposition of positions or velocities, the proper time displayed by its internal clock is also in a quantum superposition from an external perspective. [...]
  § 3 Extended symmetries and QRF changes: The construction we have introduced in the previous section is compatible with an extended notion of spacetime symmetries. This means that every quantum particle can equally serve as a QRF, and that no preferred QRF is singled out. [...]
  § 5 Discussion: In this work, we have introduced the notion of a spacetime quantum reference frame, i.e., a reference frame in spacetime associated to a quantum system which can be in a superposition, or entangled from the point of view of another quantum system. We have developed a formulation to describe a set of relativistic quantum particles in a weak gravitational field from the perspective of such spacetime quantum reference frame. In order to achieve this, we developed a covariant formulation describing both the quantum state associated to the position/momentum of the particles and its internal state. The former is used to fix the spacetime quantum reference frame, and the latter is used as the internal clock of the quantum reference frame ticking according to its own proper time. This formulation allows us to compare the dynamical evolution in the proper time of different quantum clocks, when the state of their external variables (position or momentum) is in a quantum superposition from the perspective of one of them. [...]
[6] arXiv:2102.01659v2 | Capacity and quantum geometry of parametrized quantum circuits
  To harness the potential of noisy intermediate-scale quantum devices, it is paramount to find the best type of circuits to run hybrid quantum-classical algorithms. Key candidates are parametrized quantum circuits that can be effectively implemented on current devices. Here, we evaluate the capacity and trainability of these circuits using the geometric structure of the parameter space via the effe
  Full text (https://arxiv.org/html/2102.01659v2), excerpts of its own sections:
  § I Introduction: Quantum computers promise to tackle challenging problems for classical computers such as drug design, combinatorial optimisation and simulation of many-body physics. While fully-fledged large-scale quantum computers with error correction are not expected to be available for many years, noisy intermediate-scale quantum (NISQ) devices have been investigated as a way to approach computationally hard problems with quantum processors available now and in the near future  [ 1 , 2 ] . Variational quantum algorithms (VQA)  [ 3 , 4 , 5 , 6 ] have been a major hope in achieving a quantum speedup with NISQ devices. The core idea is to update a parametrized quantum circuit (PQC) in a hybrid quantum-classical fashion. Measurements performed on the PQC are fed into a classical computer to propose a new set of variational parameters. A key challenge has been the occurrence of barren plateaus, i.e. the gradients used for optimisation vanish exponentially with increasing number of qubits  [ 7 ] , as well as for various types of cost functions  [ 8 ] , entanglement  [ 9 ] and noise  [ 10 ] . [...]
  § II Parametrized quantum circuits: A PQC generates a quantum state of $N$ qubits $|\psi(\theta)\rangle=U(\theta)|0\rangle^{\otimes N}\,,$ (1) with the unitary $U(\theta)$ , the $M$ -dimensional parameter vector $\theta$ and product state $|0\rangle^{\otimes N}$ as [...]
  § V Results: As a demonstration of our methods, we provide an in-depth characterization of a PQC consisting of randomly chosen $x$ , $y$ , $z$ rotations and CNOT gates in a chain topology as function of number of layers $p$ in Fig. 3 . The parameter dimension $D_{\text{C}}$ (i.e. number of independent parameters of the quantum state that can be expressed by the PQC) increases linearly with $p$ in Fig. 3 a, until it reaches the maximal possible value for $D_{\text{C}}=2^{N+1}-2$ at a characteristic number of layers $p_{\text{c}}$ . This point is reflected in the spectrum of the QFI $\mathcal{F}$ , averaged over random instances of the PQC (see Fig. 3 b-d). Most notably, the variance of the logarithm of the non-zero eigenvalues reaches a maximum for $p_{\text{c}}$ (Fig. 3 b). Further, the minimum taken over all eigenvalues becomes minimal (Fig. 3 c). We can see this more clearly in the distribution of eigenvalues (Fig. 3 d). With increasing $p$ , the distribution becomes broader, with a pronounced tail of small eigenvalues of $\mathcal{F}$ appearing close to the transition at $p_{\text{c}}$ . [...]
  § VI Discussion: We investigated the capacity and trainability of hardware efficient PQCs using the quantum geometric structure of the parameter space. We introduced the notion of parameter dimension $D_{\text{C}}$ and effective quantum dimension $G_{\text{C}}$ which are global and local measures respectively of the space of quantum states that can be accessed by the PQC. Both can be derived from the QFI. We applied these concepts on PQCs composed of layers of single-qubit rotations and different types of entangling gates arranged in various geometries. For comparable circuit depth $p$ , we find strong numerical evidence that PQCs constructed from CNOT or $\sqrt{\text{iSWAP}}$ gates have lower variance of the gradient, and thus higher expressibility compared to PQCs with CPHASE gates. While two-qubit gates such as CNOT and CPHASE gate can be expressed as each other by applying specific single-qubit rotations, the PQCs we use only have a limited amount of single qubit rotations and thus the choice and arrangement of two-qubit gates strongly affects the expressibility of the PQC. [...]
[7] arXiv:1805.09784v3 | Experimental demonstration of quantum walks with initial superposition states
  The preparation of initial superposition states of discrete-time quantum walks (DTQWs) are necessary for the study and applications of DTQWs. In linear optics, it is easy to prepare initial superposition states of the coin, which are always encoded by polarization states; while the preparation of superposition states of the walker is challenging. Based on a novel encoding method, we here propose a
  Full text (https://arxiv.org/html/1805.09784v3), excerpts of its own sections:
  § I INTRODUCTION: Quantum walks (QWs) are extensions of the classical random walk [ 1 ] and have wide applications in quantum algorithms [ 2 , 3 , 4 ] , quantum simulations [ 5 , 7 , 8 , 6 , 9 , 10 ] , quantum computation [ 11 , 12 , 13 ] , and so on [ 14 , 15 ] . In standard one-dimensional (1D) discrete-time quantum walks (DTQWs) [ 16 , 17 ] , the walker’s position can be denoted as $|x\rangle$ ( $x$ is an integer) and the coin can be described with the basis states $|0\rangle_{c}$ and $|1\rangle_{c}$ . The evolutions of the walker and the coin are usually characterized by a time-independent unitary operator $U=TS_{c}(\psi)$ . In each step, the coin is tossed by $S_{c}(\psi)=\left(\begin{array}[]{cc}\cos\psi&-\sin\psi\\ \sin\psi&\cos\psi\end{array}\right)$ with $\psi\in(0^{\circ},~90^{\circ})$ , and the walker is shifted by $T=\sum_{x}|x+1\rangle\langle x|\otimes|1\rangle_{c}\langle 1|+\sum_{x}|x-1\rangle\langle x|\otimes|0\rangle_{c}\langle 0|$ . [...]
  § II RESULTS: DTQW Protocol in Linear Optics To implement DTQW in polarization space, we propose a novel encoding method in the Method section. Here we make the specific choice of encoding the walker’s positions using non-orthogonal states $|k\rangle_{p}=\cos\theta_{k}|H\rangle+e^{i\phi_{k}}\sin\theta_{k}|V\rangle$ (with integer $k$ ) in the polarization space of single photons, by setting $\theta_{k}=k\Delta\theta$ and $\phi_{k}=0$ . The coin is encoded by two paths $|0\rangle$ and $|1\rangle$ of the single photons. As shown in Fig. 1(a), the operator for the conditional translation of $|k\rangle_{p}$ should be expressed as $T_{p}=\sum_{k}|k+1\rangle_{p}\langle k|\otimes|1\rangle\langle 1|+\sum_{k}|k-1\rangle_{p}\langle k|\otimes|0\rangle\langle 0|.$ In this case, the coin operator $S_{c}$ can be implemented by a $\cos^{2}\psi/\sin^{2}\psi$ beam splitter (BS) and the operator $T_{p}$ can be implemented via two HWPs oriented at $0^{o}$ and two HWPs oriented at $\Delta\theta/2$ (step forward) and $-\Delta\theta/2$ (step back), as shown in Fig. 1(b). [...]
  § III Discussion: To implement DTQW for larger steps, the errors of the experiment should be analyzed and improved. The errors are related to the following factors: (i) The number of coincidence counts. Because of the leakage of photons at BS 1, the number of coincidence counts will decrease rapidly with increasing the DTQW steps. The ratio of reflection to transmission of all beam splitters adopted in our experiment is 50:50. The loss of detected photons after every two steps of DTQW is about $70\%$ . It is an advantage of two optical loops adopted in the setup: photons are leaked and detected after every two steps rather than after each step. The errors in the experiment can be reduced by increasing the number of coincident counts. One method is to replace the 50:50 coupler (i.e., BS 1) by a coupler with better ratios. The other method is to increase the number of input photons. This can be achieved in several ways. [...]
  § IV METHODS: The encoding method Suppose there is an $n$ -dimensional state $|\Psi\rangle=\sum_{k=1}^{n}a_{k}|k\rangle~~\textrm{with}~~~\sum_{k=1}^{n}|a_{k}|^{2}=1,$ (3) in which $|k\rangle$ ( $k=1,2,...,n$ ) are orthogonal states. In the following, we propose a method to encode this state with a two-dimensional qubit and to read out all $a_{k}$ from the qubit by measurement. The obtained $a_{k}$ can be used to reconstruct the $n$ -dimensional state $|\Psi\rangle$ of Eq. ( 3 ). [...]
[8] arXiv:math/0205005v2 | The rings of noncommutative projective geometry
  In the past 15 years a study of ``noncommutative projective geometry'' has flourished. By using and generalizing techniques of commutative projective geometry, one can study certain noncommutative graded rings and obtain results for which no purely algebraic proof is known. For instance, noncommutative graded domains of quadratic growth, or ``noncommutative curves,'' have now been classified by ge
  Full text (https://arxiv.org/html/math/0205005v2), excerpts of its own sections:
  § 1. Introduction: Noncommutative projective geometry is a new field of mathematics which studies noncommutative graded rings and their categories of modules via the techniques of projective algebraic geometry. This new “geometry” has been able to prove ring-theoretic theorems (for which no purely algebraic proof is known) and has led to new questions which a classical ring theorist would not have asked. This paper will survey some of these new answers and questions. But first, we would like to say that an excellent survey article [ SV ] already exists. In fact, the lecture on which this paper is based was in turn based on that survey. Thus, similarities between the two papers must exist and we express our great debt to the previous article’s authors. We hope that this simplified survey will encourage the reader to examine [ SV ] . However, we have also added some new material, particularly in Section  6 . To give this paper an overlying structure, we will give our opinionated answer to the question Question 1.1 . Which rings should be included in noncommutative projective geometry? [...]
  § 2. Artin-Zhang Theorem: Noncommutative rings have few prime ideals compared to commutative rings. Hence, defining a projective scheme as a ringed topological space on the homogeneous primes of $R$ would not be useful. Instead, we look to the Serre Correspondence Theorem ( SCT ) for a definition of noncommutative projective scheme. First, we need some notation for module categories associated to $R$ or a commutative scheme $X$ . • $\Gr R$ – the category of graded right $R$ -modules, • $\Tors R$ – the full subcategory generated by all $M\in\Gr R$ with $M_{i}=0$ for all $i\gg 0$ , • $\QGr R$ – the quotient category $\Gr R/\Tors R$ , • $\gr R,\tors R,\qgr R$ – the respective subcategory of noetherian objects, • $\Qch X,\coh X$ – the category of quasicoherent (resp. coherent) sheaves on the scheme $X$ . The SCT states that if $R$ is commutative and finitely generated by $R_{1}$ , then there is a category equivalence $\QGr R\cong\Qch(\Proj R)$ . Further, under these equivalences, $\pi R$ corresponds to ${\mathcal{O}}_{X}$ , where $\pi R$ is the image of $R$ in $\QGr R$ . [...]
  § 3. Twisted homogeneous coordinate rings: In this section we will discuss those rings $R$ which are closest to commutative rings in the sense of the Artin-Zhang Theorem. Twisted homogeneous coordinate rings are rings of the form $\Gamma(\Qch X,{\mathcal{O}}_{X},s)_{\geq 0}$ for some proper commutative scheme $X$ , with $({\mathcal{O}}_{X},s)$ ample. By the Artin-Zhang Theorem, a ring $R$ with ( R0 )–( R2 ) and $(\QGr R,\pi R)\cong(\Qch X,{\mathcal{O}}_{X})$ for some commutative proper scheme $X$ is isomorphic to a twisted homogeneous coordinate ring in sufficiently high degree. Twisted homogeneous coordinate rings are so called because any autoequivalence of $\Qch X$ is of the form ${\sigma}_{*}(-\otimes{\mathcal{L}})$ for some automorphism ${\sigma}$ and invertible sheaf ${\mathcal{L}}$ on $X$ [ AZ1 , Corollary 6.9] , [ AV , Proposition 2.15] . Knowledge of automorphisms and invertible sheaves then allows one to study these twisted rings. [...]
  § 4. Quantum polynomial rings: Since any commutative projective scheme can be embedded in ${\mathbb{P}}^{n}$ for some $n$ , many projective geometry propositions are mainly concerned with projective $n$ -space or its homogeneous coordinate ring $k[x_{0},\dots,x_{n}]$ . [...]
[9] QNFO: Unified Theory of Non-Archimedean Ontology | https://papers.qnfo.org/papers/unified-theory-of-non-archimedean-ontology
  URL: https://papers.qnfo.org/papers/unified-theory-of-non-archimedean-ontology/ Date: 2026-03-15 Version: 1.0 The foundational premise of this framework is that the universe is constructed not from matter or energy, but from pure information. In this view, physical objects and phenomena are emergent properties that arise from underlying data structures and their processing. While classical physics
  Full text (https://papers.qnfo.org/papers/unified-theory-of-non-archimedean-ontology), excerpts of its own sections:
  § A Unified Theory: of Non-Archimedean Ontology **Author:** Rowan Brad Quni-Gudzinas **Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com) **ORCID:** 0009-0002-4317-5604 **ISNI:** 0000000526456062 **URL:** https://papers.qnfo.org/papers/unified-theory-of-non-archimedean-ontology/ **Date:** 2026-03-15 **Version:** 1.0
  § 1.1 The Base of Reality: The foundational premise of this framework is that the universe is constructed not from matter or energy, but from pure information. In this view, physical objects and phenomena are emergent properties that arise from underlying data structures and their processing. While classical physics regards mass and energy as fundamental, that perspective is considered incomplete here. Reality is modeled as a cosmic computational system processing vast streams of interconnected data, with the tangible world we perceive being a projection of these informational dynamics. The limits of human epistemology have historically obscured this computational nature; by shifting focus from material particles to the data they encode, a new understanding of ontology becomes possible. Within this model, every quantum state functions as a unit of data storage. Interactions between these states are equivalent to calculations that collectively dictate the evolution of the cosmos. Matter is therefore a secondary phenomenon, a transient vessel for the flow of information. [...]
  § 1.2 The Energy Layer: In this framework, energy is an abstraction used to quantify the magnitude of change within a system, rather than a fundamental constituent of the world. Information precedes energy, acting as the blueprint that dictates physical behavior. The Hamiltonian operator, a cornerstone of quantum mechanics, is reinterpreted as a tool for measuring this underlying data by extracting the hierarchical depth of information within a given state. The discrete energy levels observed in quantum systems are thus the eigenvalues of this informational structure. This redefinition aims to reveal the mathematical core of physical processes. When physical systems interact, they engage in a structured exchange of data governed by the precise rules of quantum mechanics. These laws ensure that no fundamental information is destroyed, maintaining the overall balance of the cosmological system. An interaction, such as a photon striking an electron, is modeled as an algorithm updating the local state of the universal computer. [...]
  § 4.1 MWI Overview: The Many-Worlds Interpretation (MWI) is a widely discussed theory in quantum physics that attempts to explain quantum superposition and measurement. It proposes a solution to the paradoxes that have plagued scientists for nearly a century by suggesting that every conceivable quantum outcome occurs. This framework posits an ever-expanding multiverse, constantly fracturing into parallel dimensions. While compelling, this theory requires an extravagant ontological leap and, in our view, misunderstands the true structure of existence. At its core, MWI claims that every physical possibility is realized in a separate, parallel reality. It insists that the universe splits every time a subatomic particle faces a quantum choice, meaning countless copies of you are experiencing different versions of your life across infinite dimensions. This proposition removes the concept of collapsed probabilities, replacing it with a branching bush of simultaneous existences. [...]
[10] QNFO: Waves Do Math | https://papers.qnfo.org/papers/treatise-on-waves
  Stand at the edge of the ocean. One is at the boundary between two worlds: the solid, seemingly definite world underfoot, and the fluid, ever-changing world of the sea. Intuition tells us these are fundamentally different kinds of existence. Intuition is wrong. This treatise demonstrates that there is only one reality, governed by a single, universal set of principles—the principles of waves. This
  Full text (https://papers.qnfo.org/papers/treatise-on-waves), excerpts of its own sections:
  § A Treatise: on Waves: The Physical Nature of Reality **Author:** Rowan Brad Quni-Gudzinas **Affiliation:** QNFO **Email:** rowan.quni@qnfo.org **ORCID:** 0009-0002-4317-5604 **ISNI:** 0000000526456062 **DOI:** https://papers.qnfo.org/papers/treatise-on-waves/ **Version:** 1.1 **Date:** 2025-09-06
  § One Reality, Many Scales: Stand at the edge of the ocean. One is at the boundary between two worlds: the solid, seemingly definite world underfoot, and the fluid, ever-changing world of the sea. Intuition tells us these are fundamentally different kinds of existence. Intuition is wrong. This treatise demonstrates that there is only one reality, governed by a single, universal set of principles—the principles of **waves**. This reality is **fractal**, meaning the same fundamental patterns of behavior repeat at every conceivable scale. The intricate dance of waves shaping a coastline follows the exact same logic that shapes an atom. To understand one is to possess the key to understanding the other. The apparent macroscopic differences between a water wave and a quantum field excitation are merely differences in scale and the medium’s local properties, not differences in underlying ontological essence. This unified perspective challenges centuries of dualistic thinking, proposing a seamless continuum of existence from the grand cosmic scale to the Planck realm. [...]
  § Part: I: A Tangible Wave - Principles of a Fractal Reality In this first part, we ground our inquiry in direct, observable phenomena from the macroscopic world. By dissecting the behaviors of physical waves, particularly those in the ocean, we establish foundational principles that are universal architects of all physical form and identity. We demonstrate how seemingly simple interactions like compounding ripples lead to the emergence of complex structures and stable entities, governed by fractal rules that apply across every scale of existence. This segment builds a concrete, intuitive understanding that will guide us through the more abstract realms of the quantum, unveiling the computational logic that sculpts the entire cosmos and making visible patterns that would otherwise remain hidden from conventional perception.
  § 1.0 The Principle of: Compounded Motion This section establishes the most fundamental characteristic of a wave-based reality: influences do not clash or obstruct, but rather merge and combine. This is the **Principle of Compounded Motion**, a direct observation from our tangible world that holds true even for the most abstract constituents of the cosmos. It posits that at every point in the universal field, the total state is the sum of all co-existing wave patterns. This axiom forms the bedrock of fractal existence, demonstrating reality’s continuous, additive computation of its own state, unifying diverse physical interactions under one elegant rule. From macrocosm to microcosm, reality performs ceaseless computations through linear addition, defining the fundamental arithmetic of physical processes that shape everything from light to matter. ##### 1.1 The Universal Law of Superposition The Principle of Compounded Motion is formally understood as the **Universal Law of Superposition**, which describes how distinct wave patterns integrate their effects. [...]
  § 2.0: Interference - The Fractal Architecture of Form If superposition is the fundamental arithmetic of reality, then **interference** is the geometry it continuously sculpts. [...]
[11] QNFO: Alpha Pi Project | https://papers.qnfo.org/papers/alpha-pi-project
  The Alpha Pi project begins with a practical engineering challenge: quantum states are exquisitely fragile, decohering rapidly due to environmental noise. This fragility stems not merely from technical limitations but from a deeper mathematical vulnerability: the continuous real‑number field that underlies standard quantum mechanics. The Bloch sphere—the canonical representation of a qubit’s state
  Full text (https://papers.qnfo.org/papers/alpha-pi-project), excerpts of its own sections:
  § From Cardiac Rhythms to: Cosmic Fractals **Author:** Rowan Brad Quni-Gudzinas **Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com) **ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604) **ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062) **DOI:** https://papers.qnfo.org/papers/alpha-pi-project/ **Date:** 2026-04-09 **Version:** 1.0
  § 1. The: Core Problem: Quantum Fragility in a Continuous World The Alpha Pi project begins with a practical engineering challenge: **quantum states are exquisitely fragile**, decohering rapidly due to environmental noise. This fragility stems not merely from technical limitations but from a deeper **mathematical vulnerability**: the continuous real‑number field that underlies standard quantum mechanics. The Bloch sphere—the canonical representation of a qubit’s state—is a smooth, continuous manifold with no discrete boundaries, allowing infinitesimal thermal drifts to accumulate linearly into significant errors. Active quantum error correction (QEC) fights this drift but imposes unsustainable resource burdens: surface codes require physical‑to‑logical qubit ratios of ~1000:1, face thermodynamic walls (Landauer’s principle, Heisenberg back‑action), and hit a **signal‑processing ceiling** beyond which no classical filtering can eliminate fundamental quantum back‑action.
  § 2. The: Biomedical Analogy: Borrowing from Cardiology A century of cardiology provides a ready‑made toolkit. Willem Einthoven’s techniques for extracting weak cardiac signals from noise—**differential amplification, vector analysis, matched filtering, ensemble averaging, crosstalk mitigation, impulse‑response deconvolution, and closed‑loop feedback**—translate directly to quantum readout. These methods improve fidelity but reveal diminishing returns, confirming that the noise problem is intrinsic to the continuous framework, not merely technical. The biomedical analogy thus serves a dual purpose: offering practical improvements while highlighting the need for a more fundamental solution.
  § 3.: The Ontological Pivot: Replacing the Continuum with a Discrete Hierarchy Confronting the signal‑processing ceiling forces an **ontological pivot**. [...]
  § 7.6 Experimental Signatures: 1. Deviations from standard quantum mechanics at ultra‑low energies. 2. Anisotropies in the fine‑structure constant \(\alpha\). 3. Discrete‑spacetime effects in cosmic‑ray events. 4. Prime periodicity in particle mass ratios. 5. Modified dispersion relations at high energies. 6. Lorentz‑violation signatures. 7. Tests with few‑particle systems in ultracold traps.
  § 7.6 Experimental Signatures: The ultrametric framework makes several **testable predictions** that distinguish it from standard quantum mechanics and general relativity. **Deviations from standard quantum mechanics at ultra‑low energies** are expected because the discrete tree structure becomes relevant when energy scales approach the level spacing between tree vertices. These could manifest as **anomalies in few‑particle interference patterns** in ultracold atomic systems or **modified tunneling rates** in mesoscopic devices. **Anisotropies in the fine‑structure constant \(\alpha\)** could arise if the local tree structure is not perfectly isotropic; astrophysical observations of quasar absorption lines could reveal such variations. **Discrete‑spacetime effects in cosmic‑ray events** include anomalous shower development or unexpected thresholds in the energy spectrum of ultra‑high‑energy cosmic rays. [...]
[12] QNFO: Principia Ontologica | https://papers.qnfo.org/papers/principia-ontologica
  Human understanding operates through representational models rather than direct reality apprehension. Alfred Korzybski famously articulated this principle, noting that abstractions derived from perception necessarily differ from their source. Cognitive frameworks function as biological data-compression heuristics evolved for survival, not for producing perfect copies of an ultimate territory. Ever
  Full text (https://papers.qnfo.org/papers/principia-ontologica), excerpts of its own sections:
  § Information,: Non-Archimedean Geometry, and Semantic Self *A Framework for Cosmology, Consciousness, and Meaning*
  § 1.1 The Map-Territory: Distinction Human understanding operates through representational models rather than direct reality apprehension. Alfred Korzybski famously articulated this principle, noting that abstractions derived from perception necessarily differ from their source. Cognitive frameworks function as biological data-compression heuristics evolved for survival, not for producing perfect copies of an ultimate territory. Every scientific theory and philosophical system consequently constitutes a specialized map with inherent simplifications. These maps prove useful for navigation and prediction within specific domains of experience. Confusing the symbolic representation with the actual entity it references leads to significant categorical errors. Recognizing this distinction forms the essential first step toward epistemic humility. Historical examples repeatedly demonstrate the consequences of map-territory confusion. Medieval cosmological models placing Earth at the universe’s center reflected theological maps, not astronomical observations. [...]
  § 1.2 Biological Cognitive: Heuristics Cognitive systems evolved under stringent pressures for efficiency and adaptive utility. Neural tissue consumes disproportionate metabolic resources relative to other bodily functions. Natural selection therefore favors heuristic shortcuts that yield sufficiently accurate results with minimal computational cost. These shortcuts manifest as systematic biases in perception, memory, and reasoning. For example, visual processing assumes light comes from above, aiding three-dimensional object recognition. Auditory systems privilege human speech frequencies over other environmental sounds. Such biases are features, not flaws, within their evolutionary context. Pattern recognition constitutes a primary heuristic mechanism for navigating complex environments. The human brain excels at identifying familiar configurations in sensory data, sometimes detecting patterns where none exist. This tendency supports rapid threat assessment and opportunity identification. It also underlies superstition and conspiracy theorizing when applied indiscriminately. [...]
  § 1.3 The: Epistemological Knot of Self-Reference Any investigation of reality must confront the investigator’s situatedness within the subject of study. The observer cannot step outside the system being observed to achieve a perfectly objective viewpoint. This self-referential condition creates logical and empirical complexities across multiple disciplines. In physics, measurement instruments interact with quantum systems, affecting observed properties. In psychology, the act of introspection alters mental states being examined. Sociology faces the challenge of researchers influencing the societies they study. Self-reference is a structural condition of inquiry, not a mere procedural obstacle. Gödel’s incompleteness theorems mathematically formalized limitations arising from self-reference in formal systems. Any consistent axiomatic system capable of basic arithmetic contains true statements unprovable within the system. The system cannot demonstrate its own consistency without resorting to axioms outside itself. This result shattered Hilbert’s program for complete mathematical formalization. [...]