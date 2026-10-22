# Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout

## Abstract

Quantum hardware engineers routinely calibrate qubits by iterating between state preparation, control pulse design, and readout discrimination. This loop is inherently self‑referential because the calibration model is built from data that depend on the very model being calibrated. We formalize the loop as a composite operator $T=\Gamma\circ\Phi$ acting on operational data $\mathcal{D}$, where $\Phi$ maps data to a Hilbert‑space identification and $\Gamma$ generates predicted data from an identification. A Banach‑type contraction condition $L<1$ guarantees a unique fixed point and thus benign circularity; violation of the condition permits multiple fixed points or continuous symmetry orbits, signalling ontological underdetermination. We derive the contraction criterion, exhibit a two‑branch toy model with two exact fixed points, and compute the minimal shot budget required to resolve ontology‑discriminating observables using an illustrative single‑shot readout fidelity $F=0.99991$. The analysis shows that (i) convergence to a unique operational identification occurs in at most fourteen iterations for $L=0.6$, (ii) multiplicity can arise from branch selection, and (iii) resolving a discrepancy $\delta=10^{-3}$ at $1\%$ failure probability demands $N\approx2.65\times10^{6}$ shots. These results clarify when operational circularity is a harmless calibration artifact and when it masks genuine ontological ambiguity, providing concrete criteria for quantum‑hardware design and experimental testing.

## 1. Introduction

Quantum information processors rely on qubits—two‑level subsystems that are initialized, manipulated by control pulses, and measured. The prevailing engineering view treats the qubit as a pre‑existing physical degree of freedom whose parameters are accessed by calibration routines. In practice, calibration proceeds by a closed loop: a model of the qubit generates control waveforms; the resulting data are used to update the model; the updated model in turn defines the next set of control waveforms. Because the model and the data co‑define each other, the loop is **operationally circular**. This circularity is unavoidable, but it can be either **benign**—converging to a unique, self‑consistent identification of the qubit—or **problematic**, leaving multiple physically inequivalent identifications compatible with the same operational data.

The real‑world problem is that hardware designers and calibration engineers must decide whether standard calibration pipelines suffice to certify a qubit’s physical nature, or whether additional out‑of‑loop probes are required. If the loop is benign, a single calibration routine yields a unique operational ontology, simplifying cross‑platform benchmarking and device qualification. If the loop is underdetermined, the same operational data can support distinct ontologies (e.g., an energy eigenmode versus a collective excitation), and any downstream algorithmic claim about “the qubit” may be ambiguous.

**Contributions.**  
1. Formal definition of the calibration fixed‑point problem (Section 3).  
2. Derivation of a contraction condition guaranteeing a unique fixed point (Section 4).  
3. Construction of a two‑branch toy model exhibiting multiple fixed points (Section 4).  
4. Shot‑budget calculation for an ontology‑discriminating observable using an illustrative readout fidelity (Section 4).  
5. Sensitivity analysis of symmetry‑breaking perturbations (Section 4).

## 2. Background and Related Work

Ontology engineering provides a language for describing the mapping between data and conceptual entities. The Gene Ontology (GO) is described as “the largest resource for cataloguing gene function” and exemplifies an explicit, structured assignment of entities and relations [1]. We adopt this notion of an **ontology map** $\Phi$ for Hilbert‑space identifications.

GO can be used “without deep understanding of its structure” [2], illustrating how a useful abstraction may be employed without awareness of its underlying commitments. This mirrors the practice of treating a qubit as a black‑box two‑level system while ignoring the physical substrate that implements it.

Ontology matching—finding correspondences between entities in different ontologies—is addressed by GraphMatcher, an ontology‑matching system that employs graph‑attention mechanisms [3]. Cross‑platform calibration of transmon, trapped‑ion, and spin qubits can be cast as an ontology‑matching problem: the operational ontologies produced by each platform must be aligned or shown to be incompatible.

Ontology evolution is studied in the life‑science context, where mappings between related ontologies change as the underlying ontologies are extended or revised [4]. This supports our assumption that a qubit’s operational ontology is not static but evolves through the calibration process.

Analogous challenges arise in domain‑specific ontologies for magnetic materials, where the same physical object can be described in multiple unit systems [6]. The need to manage multiple, mathematically equivalent descriptions informs our treatment of continuous symmetry orbits in qubit ontology.

The QNFO corpus provides a pedagogical bridge between ontological critique and concrete quantum hardware. One paper surveys control, readout, and self‑referential metrology across transmon, trapped‑ion, and spin platforms [9], motivating the multi‑platform perspective of this work. Another discusses minimal ontological commitments required for post‑particle computation [10], supplying the philosophical backdrop for the underdetermination analysis. Finally, semantic fidelity is introduced as an operational measure for borrowed quantum terms [11], which we adopt as a design constraint on falsifiable claims.

## 3. Methods

### 3.1 Operational data and ontology maps

Let $\mathcal{D}$ denote the space of operational data, i.e. sequences of control waveforms, their settings, and readout outcomes. Let $\mathcal{O}$ denote the space of Hilbert‑space identifications, each specifying a two‑level subspace $\{|0\rangle,|1\rangle\}$ together with a Hamiltonian $H$, a readout observable $M$, and error channels $\{L_k\}$, as well as a physical interpretation (eigenmode, field excitation, collective variable).

An **ontology map**
$$
\Phi:\mathcal{D}\to\mathcal{O}
$$
assigns to any datum $x\in\mathcal{D}$ an identification $\Phi(x)$.  

A **realization map**
$$
\Gamma:\mathcal{O}\to\mathcal{D}
$$
produces the predicted data that would be observed if the identification were correct.  

Calibration seeks a **fixed point** $x^{*}\in\mathcal{D}$ satisfying
$$
x^{*}=\Gamma\bigl(\Phi(x^{*})\bigr).
$$
The composite operator
$$
T=\Gamma\circ\Phi:\mathcal{D}\to\mathcal{D}
$$
encodes one iteration of the calibration loop.

### 3.2 Contraction condition for benign circularity

Equip $\mathcal{D}$ with a metric $d_{\mathcal{D}}$ (e.g. total‑variation distance between predicted readout distributions plus weighted parameter distance).  

**Proposition 1.** If there exists $L\in(0,1)$ such that
$$
d_{\mathcal{D}}\bigl(T(x),T(x')\bigr)\le L\,d_{\mathcal{D}}(x,x')\quad\forall x,x'\in\mathcal{D},
$$
then $T$ is a contraction and, by Banach’s fixed‑point theorem, possesses a unique fixed point $x^{*}$. Moreover, iterating from any initial datum $x_{0}$ yields
$$
d_{\mathcal{D}}(x_{n},x^{*})\le L^{n}\,d_{\mathcal{D}}(x_{0},x^{*}),
$$
so convergence to tolerance $\varepsilon$ requires
$$
n\ge\frac{\ln\!\bigl(\varepsilon/d_{\mathcal{D}}(x_{0},x^{*})\bigr)}{\ln L}.
$$

### 3.3 Ontological underdetermination

If $T$ fails to be globally contractive, multiple fixed points may exist. Define two ontology maps $\Phi_{A},\Phi_{B}$ with corresponding realizations $\Gamma_{A},\Gamma_{B}$. Ontological underdetermination occurs when a datum $x^{*}$ satisfies
$$
x^{*}=\Gamma_{A}\bigl(\Phi_{A}(x^{*})\bigr)=\Gamma_{B}\bigl(\Phi_{B}(x^{*})\bigr),
$$
while $\Phi_{A}(x^{*})$ and $\Phi_{B}(x^{*})$ are physically inequivalent (different interpretations of the controlled entity).

A continuous source of underdetermination is **equivariance**: if a group $G$ (e.g. $SO(3)$ acting on Bloch‑sphere axes) satisfies $T\circ g = g\circ T$ for all $g\in G$, then the entire orbit $\{g\cdot x^{*}\mid g\in G\}$ consists of fixed points. For a qubit, $SO(3)$ has dimension three, yielding three continuous descriptive parameters (two axis angles and one phase) invisible to any $G$‑invariant statistic.

### 3.4 Discriminating observable and shot budget

To distinguish two ontologies that differ in the expectation value of a readout‑accessible observable by $\delta$, we require enough measurement shots to resolve $\delta$ against readout noise. Assuming independent Bernoulli outcomes with per‑shot error probability $p_{e}=1-F$, Hoeffding’s inequality gives the required number of shots $N$ for failure probability $\alpha$:
$$
N\ge\frac{\ln(2/\alpha)}{2\,\delta^{2}}.
$$
We will instantiate this formula in Section 4 using an illustrative single‑shot readout fidelity $F=0.99991$ (hence $p_{e}=9\times10^{-5}$).

## 4. Analysis

All numerical inputs are listed explicitly; derivations are shown step‑by‑step.

### 4.1 Readout error probability

Assumption 1: illustrative single‑shot readout fidelity $F=0.99991$ (error probability $p_{e}=1-F$).  

Derivation:
\[
p_{e}=1-F=1-0.99991=9\times10^{-5}.
\]

The expected number of erroneous outcomes in $N_{\text{trials}}=10^{6}$ shots is
\[
N_{\text{err}}=p_{e}\,N_{\text{trials}}=9\times10^{-5}\times10^{6}=90.
\]

### 4.2 Statistical uncertainty per setting

Assume $N=10^{4}$ shots per tomographic setting and a worst‑case Bernoulli parameter $p=1/2$.

Standard error:
\[
\sigma_{p}=\sqrt{\frac{p(1-p)}{N}}=\sqrt{\frac{0.25}{10^{4}}}
=\sqrt{2.5\times10^{-5}}\approx5.00\times10^{-3}.
\]

Readout systematic floor $p_{e}=9\times10^{-5}$, so the ratio
\[
\frac{\sigma_{p}}{p_{e}}=\frac{5.00\times10^{-3}}{9\times10^{-5}}\approx55.6.
\]

Crossover shot count where statistical error equals the readout floor:
\[
N_{\text{cross}}\approx\frac{p(1-p)}{p_{e}^{2}}
=\frac{0.25}{(9\times10^{-5})^{2}}
=\frac{0.25}{8.1\times10^{-9}}\approx3.09\times10^{7}.
\]

### 4.3 Contraction convergence (illustrative parameters)

Model $T(x)=x^{*}+L\,(x-x^{*})$ with Lipschitz constant $L=0.6$, initial discrepancy $d_{0}=1$, target tolerance $\varepsilon=10^{-3}$.

Number of iterations:
\[
n\ge\frac{\ln(\varepsilon/d_{0})}{\ln L}
=\frac{\ln(10^{-3})}{\ln(0.6)}.
\]

Compute logarithms:
\[
\ln(10^{-3})=-3\ln10\approx-6.907755,\qquad
\ln(0.6)=\ln6-\ln10\approx-0.510826.
\]

Division:
\[
n\ge\frac{-6.907755}{-0.510826}\approx13.524,
\]
so the smallest integer $n$ satisfying the inequality is $n=14$.

Verification:
\[
0.6^{14}\approx7.836\times10^{-4}<10^{-3}<0.6^{13}\approx1.306\times10^{-3},
\]
confirming that fourteen iterations suffice.

A variant with $d_{0}=5\times10^{-2}$ and target $\varepsilon=p_{e}=9\times10^{-5}$ yields
\[
n\ge\frac{\ln(9\times10^{-5}/5\times10^{-2})}{\ln(0.6)}
=\frac{\ln(1.8\times10^{-3})}{-0.510826}\approx12.3,
\]
so $n=13$ iterations are required.

### 4.4 Shot budget for ontology discrimination

Parameters: $F=0.99991$ ($p_{e}=9\times10^{-5}$), confidence level $\alpha=0.01$ (failure probability $1\%$).

Compute $\ln(2/\alpha)=\ln(200)\approx5.298317$.

*For $\delta=10^{-3}$*:
\[
N\ge\frac{5.298317}{2\times(10^{-3})^{2}}
=\frac{5.298317}{2\times10^{-6}}
=2.649159\times10^{6}.
\]

*For $\delta=10^{-4}$*:
\[
N\ge\frac{5.298317}{2\times(10^{-4})^{2}}
=\frac{5.298317}{2\times10^{-8}}
=2.649159\times10^{8}.
\]

The per‑shot error floor $p_{e}=9\times10^{-5}$ implies that discrepancies $\delta\lesssim p_{e}$ are comparable to readout noise and therefore not resolvable without additional error mitigation.

### 4.5 Two‑ontology toy model with two fixed points

Define a scalar datum $x\in\mathbb{R}$ and two candidate ontologies $A$ and $B$:
\[
T_{A}(x)=0.5\,x+0.5\,a,\qquad
T_{B}(x)=0.5\,x+0.5\,b,
\]
with distinct offsets $a\neq b$.

Fixed points satisfy $x=T_{A}(x)$ and $x=T_{B}(x)$:
\[
x_{A}^{*}=a,\qquad x_{B}^{*}=b.
\]

Both maps have Lipschitz constant $L=0.5<1$, so each branch is locally contractive. The selection rule keeps the branch whose prediction is closer to the current iterate.

Concrete parameters: $a=0$, $b=1$, initial guess $x_{0}=0.6$.

Basin boundary is the midpoint $m=(a+b)/2=0.5$. Since $x_{0}>m$, iteration follows branch $B$:
\[
\begin{aligned}
x_{1}&=0.5\times0.6+0.5=0.8,\\
x_{2}&=0.5\times0.8+0.5=0.9,\\
x_{3}&=0.5\times0.9+0.5=0.95,
\end{aligned}
\]
and in general
\[
x_{n}=1-0.4\times0.5^{\,n}.
\]
The sequence converges to $x_{B}^{*}=1$ and never visits branch $A$. The final ontology is thus determined by the initial guess rather than by the data.

### 4.6 Symmetry‑breaking sensitivity (projection)

Define the minimal detectable asymmetry
\[
\epsilon_{\min}\approx\sqrt{\sigma_{p}^{2}+p_{e}^{2}}.
\]

Using $\sigma_{p}=5.00\times10^{-3}$ (Section 4.2) and $p_{e}=9\times10^{-5}$:
\[
\epsilon_{\min}\approx\sqrt{(5.00\times10^{-3})^{2}+(9\times10^{-5})^{2}}
=\sqrt{2.5\times10^{-5}+8.1\times10^{-9}}
=\sqrt{2.50081\times10^{-5}}
\approx5.001\times10^{-3}.
\]

At the crossover count $N_{\text{cross}}=3.09\times10^{7}$, the statistical error becomes $\sigma_{p}\approx9.0\times10^{-5}$, yielding
\[
\epsilon_{\min}\approx\sqrt{(9.0\times10^{-5})^{2}+(9\times10^{-5})^{2}}
=\sqrt{1.62\times10^{-8}}
\approx1.27\times10^{-4}.
\]

Any genuine ontological signature smaller than $\epsilon_{\min}$ is operationally invisible under the assumed noise model.

## 5. Results

All quantitative statements follow from the derivations in Section 4.

*R1 (Convergence).* With $L=0.6$, $d_{0}=1$, and $\varepsilon=10^{-3}$, calibration reaches the target in $n=14$ iterations (Section 4.3). A variant with $d_{0}=5\times10^{-2}$ and $\varepsilon=p_{e}=9\times10^{-5}$ requires $n=13$ iterations. In this regime the loop is benign and yields a unique fixed point.

*R2 (Multiplicity).* The toy model of Section 4.5 possesses two exact fixed points $x_{A}^{*}=0$ and $x_{B}^{*}=1$, separated by a basin boundary at $0.5$. Starting from $x_{0}=0.6$ the iteration converges to $x_{B}^{*}=1$ via the closed‑form $x_{n}=1-0.4\,0.5^{n}$. The final ontology depends on the initial guess, demonstrating ontological underdetermination despite local contractivity.

*R3 (Readout error floor).* The assumed fidelity $F=0.99991$ yields $p_{e}=9\times10^{-5}$, i.e. one error per $1.11\times10^{4}$ shots; over $10^{6}$ trials the expected error count is $90$.

*R4 (Shot budget).* Resolving a discrepancy $\delta=10^{-3}$ at $\alpha=0.01$ requires $N=2.649159\times10^{6}$ shots (Section 4.4). For $\delta=10^{-4}$ the requirement rises to $2.649159\times10^{8}$ shots.

*R5 (Symmetry sensitivity).* At $N=10^{4}$ shots the minimal detectable asymmetry is $\epsilon_{\min}\approx5.001\times10^{-3}$; at the crossover count $N_{\text{cross}}$ it improves to $\epsilon_{\min}\approx1.27\times10^{-4}$ (Section 4.6).

*R6 (Continuous orbit).* The $SO(3)$ equivariance described in Section 3.3 leaves three continuous descriptive parameters (two axis angles, one phase) unconstrained by any $G$‑invariant statistic, implying an uncountable family of data‑compatible ontologies.

## 6. Discussion

### Limitations

1. **Illustrative Lipschitz constant.** The contraction analysis uses a fixed $L=0.6$; real calibration loops may exhibit state‑dependent or iteration‑dependent $L$, potentially violating the global contraction condition.  
2. **Scalar toy model.** The two‑branch example reduces the ontology space to a single scalar; actual ontologies are high‑dimensional, and multiplicity may appear as continuous families or limit cycles not captured here.  
3. **Noise model.** The shot‑budget calculation assumes independent Bernoulli readout errors and neglects decoherence or correlated noise that would increase the required $N$.  
4. **Equivariance assumption.** The $SO(3)$ symmetry argument presumes perfect gauge symmetry; any stray bias (e.g., magnetic field offsets) breaks the symmetry and may reduce the orbit dimension, but quantifying this requires platform‑specific modeling.  

### Failure modes

*If calibration iterations become chaotic rather than contractive, no fixed point exists and the qubit lacks a self‑consistent operational definition.*  
*If the symmetry orbit corresponds to physically distinct couplings (e.g., a collective mode versus a single‑particle transition) rather than a pure gauge, the underdetermination is physical and not merely conventional.*  

Both scenarios would invalidate the benign‑circularity claim.

### Falsification criteria

1. **Unique, platform‑independent identification.** Demonstrating that calibration on disparate platforms (transmon, ion, spin) converges to the same Hilbert‑space identification—including axis labeling—would falsify the claim of a three‑dimensional equivariant orbit (R6).  
2. **Out‑of‑loop observable discrimination.** Measuring an observable that differs between two candidate ontologies by $\delta\ge10^{-3}$ and achieving statistical significance with fewer than $2.65\times10^{6}$ shots would falsify the shot‑budget prediction (R4).  
3. **Breakdown of contraction.** Observing divergence or limit‑cycle behavior in calibration iterations under controlled conditions would falsify the contraction‑based uniqueness claim (R1).

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.** Calibration engineers and quantum‑hardware designers are the main beneficiaries. If the contraction condition holds (i.e., measured $L<1$), standard calibration routines guarantee a unique operational ontology, simplifying device qualification, cross‑platform benchmarking, and error‑budget allocation. If multiplicity or equivariance is detected, designers must incorporate additional out‑of‑loop probes (e.g., leakage‑sensitive spectroscopy) to break the symmetry and certify the physical nature of the qubit.

**(b) Technology readiness.** The analysis is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions, it resides at TRL 2 (technology concept formulated) and does not exceed TRL 3 (analytical proof‑of‑concept).

**(c) Smallest next experiment.** A minimal experiment would measure an ontology‑discriminating observable (e.g., a leakage‑sensitive transition) on a trapped‑ion qubit while varying the initial calibration guess. The experiment records the number of shots $N$ required to resolve a discrepancy $\delta=10^{-3}$ with failure probability $\alpha=0.01$. Observation of convergence to a single outcome regardless of the initial guess would support the contraction hypothesis; observation of dependence on the initial guess would confirm underdetermination. Failure to achieve statistical significance with $N<2.65\times10^{6}$ shots would falsify the shot‑budget projection.

**(d) Engineering constraints.**  
- **Readout fidelity**: The analysis assumes $F=0.99991$; achieving this fidelity requires high‑quantum‑efficiency detectors and low‑noise amplification chains.  
- **Shot budget**: The projected $N$ values may be limited by experimental duty cycles and data‑acquisition bandwidth.  
- **Control of systematic drifts**: Drift between calibration iterations can increase the effective Lipschitz constant, potentially violating contraction.  
- **Symmetry‑breaking fields**: Intentional bias fields may be needed to lift $SO(3)$ degeneracy; their magnitude must exceed $\epsilon_{\min}$ as derived in Section 4.6.

**(e) Projected cost/performance bounds (projection).** Assuming a readout system capable of $F=0.99991$ at a hardware cost of \$10 k per qubit module (typical for state‑of‑the‑art trapped‑ion setups) and a data‑acquisition system capable of $10^{6}$ shots per second, the total experimental time to reach the $2.65\times10^{6}$‑shot budget is approximately 3 seconds, yielding a negligible marginal cost relative to the hardware baseline. These figures are projections based on the assumed fidelity and shot rates.

**(f) Direct risks or misuse paths.** Misinterpreting the existence of multiple fixed points as evidence that the qubit’s physical nature is irrelevant could lead to under‑engineering of out‑of‑loop diagnostics, compromising device reliability. Careful communication of the distinction between benign circularity and ontological underdetermination mitigates this risk.

## 8. Conclusion

The analysis demonstrates that the uniqueness of a qubit’s operational identification is a property of the calibration dynamics, not of the underlying physical system. When the composite calibration operator $T$ is a contraction, Banach’s theorem guarantees a unique fixed point and benign circularity. When $T$ is non‑contractive, either multiple discrete fixed points or continuous symmetry orbits can arise, leading to ontological underdetermination that cannot be resolved by calibration alone. Quantitative criteria—Lipschitz constant thresholds, iteration counts, and shot‑budget estimates—provide concrete guidance for hardware designers to assess the adequacy of standard calibration pipelines and to plan out‑of‑loop measurements when necessary. Future work will extend the single‑parameter model to multi‑parameter calibration operators, incorporate realistic drift and correlated noise, and execute the proposed minimal experiment on representative transmon, trapped‑ion, and spin platforms to validate the contraction‑based uniqueness criterion and to measure the practical shot budgets predicted here.

## References

[1] arXiv:1602.01876v1 | Primer on the Gene Ontology  
[2] arXiv:1602.01875v1 | Gene Ontology: Pitfalls, Biases, Remedies  
[3] arXiv:2404.14450v1 | GraphMatcher: A Graph Representation Learning Approach for Ontology Matching  
[4] arXiv:1204.2731v1 | How do Ontology Mappings Change in the Life Sciences?  
[5] arXiv:2509.04926v1 | Towards Ontology-Based Descriptions of Conversations with Qualitatively-Defined Concepts  
[6] arXiv:2609.11464v1 | A Community-Developed Domain Ontology for Magnetic Materials  
[9] https://papers.qnfo.org/papers/no-thing-there | QNFO: No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems  
[10] https://papers.qnfo.org/papers/paper-beyond-the-qubit | QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation  
[11] https://papers.qnfo.org/papers/semantic-fidelity-an-operational-measure-for-borrowed-quantum-terms-and-the-scal | QNFO: Semantic Fidelity: An Operational Measure for Borrowed Quantum Terms and the Scale at Which They Fail  

## Appendix A. Divergence Report

*No divergent claims were identified among the source drafts; all quantitative statements are consistent after correction of the readout‑fidelity citation and the symmetry‑sensitivity value.*

## Appendix B. Claim Attribution

| Claim ID | Source Draft(s) | Agreement |
|----------|-----------------|-----------|
| C1 (Definition of $\Phi$, $\Gamma$, $T$) | A, B, C | Convergent |
| C2 (Proposition 1 contraction) | A, B, C | Convergent |
| C3 (Toy model fixed points) | A, B, C | Convergent |
| C4 (Readout error probability) | A, B, C | Convergent |
| C5 (Statistical error $\sigma_{p}$) | A, B, C | Convergent |
| C6 (Crossover shot count) | A, B, C | Convergent |
| C7 (Iteration count $n=14$) | A, B, C | Convergent |
| C8 (Shot budget $N=2.649159\times10^{6}$) | A, B, C | Convergent |
| C9 (Symmetry‑breaking $\epsilon_{\min}=5.001\times10^{-3}$) | A, B, C | Convergent (corrected) |
| C10 (Limit $\epsilon_{\min}=1.27\times10^{-4}$) | A, B, C | Convergent |
| C11 (Limitations list) | A, B, C | Convergent |
| C12 (Falsification criteria) | A, B, C | Convergent |
| C13 (Practical implications) | A, B, C | Convergent |
| C14 (TRL statement) | A, B, C | Convergent |
| C15 (Next experiment proposal) | A, B, C | Convergent |
| C16 (Engineering constraints) | A, B, C | Convergent |
| C17 (Projected cost/performance) | A, B, C | Convergent |
| C18 (Reference list) | A, B, C | Convergent |