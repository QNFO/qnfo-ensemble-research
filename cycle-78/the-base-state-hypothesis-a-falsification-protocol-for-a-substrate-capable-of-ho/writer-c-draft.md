# The Base State Hypothesis: A Relational Substrate for Standard-Model Structure, Assessed Against Contemporary Quantum Platforms

## Abstract

We ask whether a minimal relational substrate — a "Base State" — could in principle host the structure we call the Standard Model, rather than the Standard Model being built up from particle-like primitives on a qubit-gate substrate. The question is a re-entry of a prior constructive programme (DOI 10.5281/zenodo.18515457) into a concrete setting. Our method is deliberately indirect: we (i) formalise the Base State as a labelled transition system whose states are merged by evidence, importing the state-merging methodology of automata learning [1]; (ii) quantify the error budget of the best cloud-accessible superconducting platform described in the supplied literature, Tianyan-287 with 105 qubits and gate fidelities of 99.90% (single-qubit), 99.56% (two-qubit) and 98.7% (readout) [2]; and (iii) show by explicit arithmetic that a gate-circuit realisation of even a modest relational state space exhausts any plausible two-qubit budget, while coherent-state [3], [4], excited-state [5], nonclassical-state [6], state-design [7] and categorical [8] resources each address only fragments of the required structure. We derive that a serial two-qubit chain on Tianyan-287 retains above 50% aggregate fidelity for at most 157 gates, and that the 105-qubit register spans $2^{105} \approx 4.06 \times 10^{31}$ basis states — a counting argument that motivates, though it does not prove, the Base State alternative. We state falsification conditions explicitly.

## 1. Introduction

The Standard Model of particle physics is conventionally presented as a list of particles and interactions on a background stage. A dissenting constructive tradition — represented in the supplied corpus by "Beyond the Qubit: Constructive Paradigms for Post-Particle Computation" [10] and its companion "The Qubit Delusion" — argues that the qubit-gate-circuit model is an epistemic failure: a projection of particle ontology onto what is better described as relational, field-theoretic reality. If that critique is accepted even provisionally, the constructive question becomes: what minimal object could host Standard-Model-like structure without presupposing particles? We call this candidate object the **Base State**.

The present paper is a re-entry of the programme seeded at DOI 10.5281/zenodo.18515457 — the question of instantiating a Base State capable of hosting the Standard Model — into contact with concrete, quantitatively specified quantum platforms and methods. Our contribution is not a derivation of the Standard Model. It is a disciplined framing plus a quantitative feasibility argument:

1. We define the Base State abstractly as a relational transition system, and argue that the methodology for recovering such systems from evidence already exists in automata learning [1].
2. We compute the error budget of the strongest hardware platform described in our source material [2] and show, with explicit arithmetic, where a gate-circuit encoding of a relational state space fails.
3. We survey which fragments of the required machinery — coherent states [3], [4], excited states [5], nonclassical solid-state sources [6], state designs [7], categorical compositional structure [8] — are available, and which are missing.
4. We state falsification conditions, in the spirit of the "Falsification Pledge" of the Manifesto for Honest Computation [12].

Throughout, we are strict about what our sources support. Several supplied bibliography entries carry only titles or very short summaries; where that is the case we say so explicitly and lean on them only to the extent their summaries allow.

## 2. Background and Related Work

**Automata learning and evidence-driven state merging [1].** The interactive EDSM work of [1] learns variants of finite state automata from noisy, incomplete, or imperfectly sampled data, framing learning as recovering or reverse-engineering the model that generated the data rather than optimising a numeric target. The supplied summary also indicates that domain expertise and human knowledge are incorporated (the summary truncates mid-sentence on this point). This is directly relevant to the Base State programme: if the Base State is a relational transition system, then the problem of instantiating it from observational evidence is structurally an automata-identification problem, and the state-merging machinery of [1] is the closest supplied method. We adopt this as our formal scaffold in Section 3.

**Cloud quantum hardware: Tianyan-287 [2].** The Tianyan Quantum Cloud Platform offers cloud services demonstrating quantum advantage capabilities with a Zuchongzhi 3.0-like superconducting processor; the cloud-accessible prototype Tianyan-287 features 105 qubits with single-qubit gate, two-qubit gate, and readout fidelities of 99.90%, 99.56%, and 98.7% respectively. This is the only quantitative hardware specification in our bibliography, and it anchors our error-budget arithmetic in Section 4.

**Linear-optical teleportation and hybrid entanglement [3].** Reference [3] reviews and compares Bell-state measurement and teleportation schemes using linear optics with three resource types: two-photon pairs, entangled coherent states, and hybrid entangled states, and reports that perfect teleportation with linear optics is possible in principle based on a hybrid approach combining two-photon pairs and entangled coherent states. For us this establishes that entanglement distribution — a relational, not particle-ontological, resource — can in principle be moved without gate-circuit overhead, a fragment of the Base State toolkit.

**Coherent states across physics [4].** Reference [4] discusses coherent states from three perspectives — Schroedinger's seminal approach, the experimental take of quantum optics, and theoretical developments in quantum gravity — as a comparative, pedagogically oriented study. The supplied summary gives no further technical detail; we use it only to justify treating "coherent state" as a unifying object spanning microscopic and gravitational regimes, which is precisely the span a Base State would need.

**Excited states in quantum chemistry [5].** Reference [5] proposes a non-variational, full circuit-based quantum algorithm for obtaining excited states, motivated by the role of excited states in predicting chemical reactions and other physical processes. The summary truncates before the algorithm's performance claims; we cite it as evidence that circuit-based methods remain the default for spectral structure, and note in Section 6 that a Base State account must reproduce spectral excitation without the circuit machinery [5] assumes.

**Nonclassical state generation in semiconductors [6].** Reference [6] investigates the generation of nonclassical states — entangled, steered, and others — in a physical system composed of light and a semiconductor, motivated by the observation that solid-state quantum computing proposals are extremely promising for room-temperature machines and would require in-built sources of nonclassical states. This addresses the "source" fragment of the Base State problem: where does the nonclassicality come from?

**Quantum state designs under symmetry [7].** Reference [7] studies quantum state designs, which enable efficient sampling of random quantum states and play a role in benchmarking protocols from circuit design to black hole physics, and asks how symmetry — ubiquitous, and expected to reduce the randomness of a state — affects state designs; the summary indicates this effect remained unresolved. Symmetry is the load-bearing concept for any Standard-Model-hosting substrate (gauge symmetry), so [7] marks exactly the open point where our programme meets open mathematics.

**Categorical quantum mechanics and quantum games [8].** Reference [8], in the flavour of categorical quantum mechanics, extends nonlocal games to allow quantum questions and answers, using quantum sets (special symmetric dagger Frobenius algebras) and the quantum functions of Musto, Reutter, and Verdon, with equations in a diagrammatic calculus for tensor categories. Dagger Frobenius algebras are the categorical encoding of compositional structure; this is the supplied formal language closest to a relational ontology of interaction.

**The QNFO corpus [9], [10], [11], [12].** The supplied entry for "QNFO: Standard Model" [9] carries no summary text; we therefore use it only as the corpus node naming the Standard Model context, and make no claim about its contents. "Beyond the Qubit" [10] is described as a companion to "The Qubit Delusion" (v1.1, DOI 10.5281/zenodo.21254143), arguing that the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto relational, field-theoretic reality — and stripping quantum mechanics to its minimal ontological commitments (the summary truncates there). "EMERGENT CORRELATION IN A LOCAL-DETERMINISTIC UNIVERSE" [11] likewise carries no summary; we cite it only by title, as the corpus's treatment of emergent correlation, and draw no findings from it. Finally, the "Manifesto for Honest Computation" [12] is described as a final synthesis with 5 principles, a concrete portfolio, and the Falsification Pledge; we adopt the Falsification Pledge as methodological constraint: every claim in this paper is either computed, sourced, or explicitly labelled a projection.

## 3. Methods

### 3.1 The Base State as a labelled transition system

We define the Base State $B$ as a tuple

$$B = (S, \Sigma, \delta, \lambda, \mathcal{G}),$$

where $S$ is a set of relational states, $\Sigma$ an alphabet of interaction events, $\delta : S \times \Sigma \to S$ a (possibly probabilistic) transition function, $\lambda : S \to \mathcal{O}$ a labelling into observables $\mathcal{O}$, and $\mathcal{G}$ a symmetry group acting on $B$. The Standard-Model-hosting requirement is then the constraint that $\mathcal{G}$ contain a subgroup isomorphic in representation content to the gauge structure $SU(3) \times SU(2) \times U(1)$. As pure arithmetic on Lie-algebra dimensions, $\dim SU(3) = 3^2 - 1 = 8$, $\dim SU(2) = 2^2 - 1 = 3$, $\dim U(1) = 1$, so the minimal gauge algebra has dimension

$$d_{\mathcal{G}} = 8 + 3 + 1 = 12.$$

This is a counting statement about the target symmetry, not a derivation of the Standard Model.

### 3.2 Evidence-driven instantiation

Following the methodology of [1], we treat instantiation of $B$ as automata identification: candidate states in $S$ are merged when evidence does not distinguish them, with human/domain input used where data is sparse, exactly the interactive EDSM setting [1] describes. The novelty is only in the interpretation: the "automaton" is the substrate, and the "data" is whatever relational evidence the platform provides.

### 3.3 The gate-circuit counterfactual

To test whether the standard qubit-gate-circuit model — the target of the critique in [10] — can host $B$, we compute its error budget on the strongest supplied platform, Tianyan-287 [2]. We model a circuit of $n$ two-qubit gates and $m$ readout events as a serial chain; the aggregate success probability under independent errors is

$$F_{\text{circuit}}(n, m) = f_{2q}^{\,n} \cdot f_{\text{ro}}^{\,m},$$

with $f_{2q} = 0.9956$ and $f_{\text{ro}} = 0.987$ taken from [2]. This independence assumption is optimistic (it ignores crosstalk and state-preparation error), so all conclusions drawn from it are upper bounds on circuit capability.

### 3.4 Resource fragments

We catalogue which supplied works supply which fragment: entanglement distribution [3], coherent-state unification [4], spectral excitation [5], nonclassical sources [6], symmetric random-state sampling [7], compositional categorical structure [8]. The Base State requires all fragments simultaneously; no supplied work supplies more than one.

## 4. Analysis

All input numbers below come from the supplied bibliography. We show every arithmetic step.

**Input 1 (from [2]):** single-qubit gate fidelity $f_{1q} = 0.9990$; two-qubit gate fidelity $f_{2q} = 0.9956$; readout fidelity $f_{\text{ro}} = 0.987$; qubit count $N_q = 105$.

**Derivation 4.1 — per-op error rates.**

$$\varepsilon_{1q} = 1 - f_{1q} = 1 - 0.9990 = 1.0 \times 10^{-3},$$

$$\varepsilon_{2q} = 1 - f_{2q} = 1 - 0.9956 = 4.4 \times 10^{-3},$$

$$\varepsilon_{\text{ro}} = 1 - f_{\text{ro}} = 1 - 0.987 = 1.3 \times 10^{-2}.$$

The two-qubit gate is $4.4$ times as error-prone as the single-qubit gate ($\varepsilon_{2q}/\varepsilon_{1q} = 4.4 \times 10^{-3} / 1.0 \times 10^{-3} = 4.4$), and readout is $13$ times as error-prone ($1.3 \times 10^{-2} / 1.0 \times 10^{-3} = 13$).

**Derivation 4.2 — two-qubit gate budget at 50% aggregate fidelity.** Setting $F_{\text{circuit}}(n, 0) = f_{2q}^{\,n} \geq 0.5$ and solving for $n$:

$$n \leq \frac{\ln 0.5}{\ln f_{2q}} = \frac{-0.693147}{\ln 0.9956}.$$

Compute $\ln 0.9956$: since $\ln(1 - x) \approx -x - x^2/2$ with $x = 0.0044$, we get $\ln 0.9956 \approx -0.0044 - 0.0044^2/2 = -0.0044 - 9.68 \times 10^{-6} = -0.00440968$. Then

$$n \leq \frac{-0.693147}{-0.00440968} \approx 157.23.$$

So a purely two-qubit-gate serial circuit on Tianyan-287 retains above 50% aggregate fidelity for at most $n = 157$ two-qubit gates. Including even a single readout at the end, the budget tightens: $f_{2q}^{\,n} \cdot 0.987 \geq 0.5$ gives $f_{2q}^{\,n} \geq 0.506584$ (since $0.5/0.987 = 0.506584\ldots$), so

$$n \leq \frac{\ln 0.506584}{\ln 0.9956} = \frac{-0.680\,027}{-0.00440968} \approx 154.2,$$

i.e. $n = 154$ two-qubit gates with one final readout. (Check: $\ln 0.506584 = \ln 0.5 + \ln 1.013168 \approx -0.693147 + 0.013081 = -0.680066$; the small difference in the fourth decimal does not change the integer bound $n = 154$.)

**Derivation 4.3 — Hilbert-space counting.** The register of $N_q = 105$ qubits spans

$$\dim \mathcal{H} = 2^{105}.$$

Compute stepwise: $2^{10} = 1024$, so $2^{100} = (2^{10})^{10} = 1024^{10}$. Now $1024^{10} = (1.024 \times 10^{3})^{10} = 1.024^{10} \times 10^{30}$. And $1.024^{10}$: $\ln 1.024 = 0.023717$, times $10$ gives $0.23717$, and $e^{0.23717} \approx 1.2677$. Hence $2^{100} \approx 1.2677 \times 10^{30}$ and

$$2^{105} = 2^{100} \cdot 2^{5} \approx 1.2677 \times 10^{30} \times 32 = 4.057 \times 10^{31}.$$

So the Tianyan-287 register spans $2^{105} \approx 4.06 \times 10^{31}$ basis states.

**Derivation 4.4 — cost of encoding a relational state space.** Suppose the Base State's relational state space $S$ has $|S| = k$ distinguishable configurations. A gate-circuit encoding needs at least $\lceil \log_2 k \rceil$ qubits, but — the crucial point — every *dynamics* $\delta$ must be compiled into gates. If we conservatively assume each relational transition requires one two-qubit gate per active pair and a transition system of degree $r$ (each state has $r$ outgoing edges), the transition table has $k \cdot r$ edges. Even for a toy relational system with $k = 100$ states and $r = 4$, that is $k \cdot r = 400$ edges; if a single coherent computation must touch even a fraction $\phi$ of them, the two-qubit budget from Derivation 4.2 requires

$$\phi \cdot 400 \leq 157 \quad \Rightarrow \quad \phi \leq \frac{157}{400} = 0.3925.$$

So even a 100-state toy relational system can have at most about 39% of its transition structure touched per coherent circuit run before aggregate fidelity drops below 50%. For a substrate intended to host a 12-dimensional gauge algebra (Derivation in Section 3.1: $d_{\mathcal{G}} = 12$) with representation structure far richer than 100 states, the gate-circuit route is not merely expensive; it is structurally mismatched. This is the quantitative core of the critique in [10], now grounded in the measured fidelities of [2].

**Derivation 4.5 — what the counting does and does not show.** The $2^{105} \approx 4.06 \times 10^{31}$-dimensional register is large enough in *dimension* to embed any finite $k$ with $k \leq 2^{105}$; the failure is in *dynamics*, not capacity. We therefore conclude that the obstacle is the gate-circuit compilation model itself, not hardware scale — which is exactly the claim the companion paper [10] makes qualitatively.

## 5. Results

All numbers below are computed in Section 4 from stated inputs; none are measured or simulated by us.

- **R1 (computed).** Per-operation error rates on Tianyan-287 [2]: $\varepsilon_{1q} = 1.0 \times 10^{-3}$, $\varepsilon_{2q} = 4.4 \times 10^{-3}$, $\varepsilon_{\text{ro}} = 1.3 \times 10^{-2}$.
- **R2 (computed).** A serial two-qubit circuit on Tianyan-287 retains $\geq 50\%$ aggregate fidelity for at most $n = 157$ two-qubit gates, or $n = 154$ with one final readout.
- **R3 (computed).** The 105-qubit register spans $2^{105} \approx 4.06 \times 10^{31}$ basis states.
- **R4 (computed, toy model).** For a toy relational system with $k = 100$ states and out-degree $r = 4$, at most a fraction $\phi \leq 0.3925$ of transition structure can be touched per coherent run under the 50% fidelity threshold.
- **R5 (computed).** The minimal Standard-Model gauge algebra has dimension $d_{\mathcal{G}} = 12$.
- **R6 (projection, stated assumptions).** Extrapolating R2's serial model, a circuit touching a full 400-edge toy transition table would need aggregate fidelity $f_{2q}^{\,400}$. Compute: $\ln f_{2q}^{\,400} = 400 \times (-0.00440968) = -1.76387$, so $f_{2q}^{\,400} = e^{-1.76387} \approx 0.1714$. **Assumptions:** independent errors, no crosstalk, no state-preparation or idling error, serial compilation; the true value is an upper bound on achievable fidelity. Uncertainty bound: any additional per-gate error $\varepsilon'$ shifts the exponent by $400\,\varepsilon'$; e.g. $\varepsilon' = 10^{-3}$ gives $e^{-1.76387 - 0.4} \approx 0.1148$, so the projection is robust in concluding that a full-table circuit fails well below any useful threshold.

**Fragment availability (qualitative, sourced).** Entanglement distribution without gate overhead: available in principle via hybrid linear-optical teleportation [3]. Coherent-state framing across scales: available as a unifying language [4]. Spectral excitation: available only within circuit-based algorithms [5]. Nonclassical state sources: available for light–semiconductor systems [6]. Symmetric state designs: open problem [7]. Compositional categorical structure: available as formal language [8]. No supplied work combines two or more fragments.

## 6. Discussion

**What the argument establishes.** The quantitative core (R2, R4, R6) shows that the gate-circuit model, on the best supplied hardware, cannot coherently traverse even toy relational state spaces; combined with the capacity result R3, the bottleneck is the compilation paradigm, supporting the qualitative critique of [10]. The methodological core — evidence-driven state merging [1] — gives the Base State programme a concrete instantiation path that does not presuppose the answer.

**Limitations and failure modes.** First, our error model assumes independence; correlated errors would only *worsen* circuit budgets, but correlated *error correction* could rescue the gate model, and we have no supplied data on error correction on Tianyan-287. Second, the toy model of Derivation 4.4 ($k = 100$, $r = 4$, one gate per edge) is a caricature; a real relational substrate might admit parallel transitions, amortised compilation, or analog evolution that no gate count captures. Third, we have not defined $\Sigma$, $\delta$, or $\mathcal{G}$ for any physically meaningful Base State; Section 3.1 is a scaffold, not a theory. Fourth, the claim that the Standard Model's gauge structure should appear as a subgroup of $\mathcal{G}$ is an assumption imported from the corpus framing [9], [10], not derived here.

**What would falsify the claims.** (i) A demonstration that error-corrected gate circuits on a 105-qubit-class device sustain logical circuits of $\geq 10^{4}$ two-qubit gates at useful fidelity would dissolve the R2/R4 bottleneck and weaken the case for the Base State alternative. (ii) A concrete instantiation of a Base State that reproduces even one Standard-Model representation (e.g., a single chiral fermion multiplet) from relational transitions would, if it failed to extend, falsify the programme's scalability. (iii) Conversely, if evidence-driven state merging [1] applied to physical data consistently yields transition systems with no gauge-like symmetry, the Base State hypothesis loses its target. Per the Falsification Pledge of [12], we commit to these conditions in advance.

**Against ourselves.** The strongest objection to this paper is that it attacks a strawman: nobody proposes compiling the Standard Model gate-by-gate. Our reply is that the critique in [10] is about ontology, not engineering, and our arithmetic (R2–R4) merely shows the engineering symptom of the ontological mismatch. A second objection: the fragments survey (Section 5) is thin because several supplied entries ([9], [11], and parts of [4], [5]) carry minimal or truncated summaries; we have deliberately restricted ourselves to what those summaries state, and the synthesis could be stronger with fuller sources. A third objection: "coherent state" in [4] and "state design" in [7] are technical notions unrelated to our "Base State" except by analogy; we flag this as analogy, not identity.

**Open questions.** Can $\mathcal{G}$ with $\dim \mathcal{G} \geq 12$ emerge from state-merging dynamics at all? Do symmetric state designs [7] provide the sampling tool needed to benchmark a Base State? Can hybrid entangled resources [3] replace two-qubit gates as the transition primitive?

## 7. Conclusion

We have reframed the re-entry question — can a Base State host the Standard Model? — as a three-part programme: a relational transition-system scaffold with evidence-driven instantiation borrowed from automata learning [1]; a quantitative demonstration, from the measured fidelities of the 105-qubit Tianyan-287 platform [2], that the gate-circuit compilation model fails on even toy relational state spaces ($n \leq 157$ two-qubit gates at 50% fidelity; $\phi \leq 0.3925$ transition coverage for a 100-state system); and a fragment survey showing that the needed machinery — teleportable entanglement [3], coherent-state unification [4], excitation [5], nonclassical sources [6], symmetric designs [7], categorical composition [8] — exists only piecemeal. The counting result $2^{105} \approx 4.06 \times 10^{31}$ shows capacity is not the obstacle; paradigm is. We have stated falsification conditions and commit to them. The next step is not a bigger register but a smaller ontology: define $\Sigma$ and $\delta$ for one gauge multiplet and let the evidence merge the rest.

## References

[1] arXiv:1707.09430v1 | Human in the Loop: Interactive Passive Automata Learning via Evidence-Driven State-Merging Algorithms

[2] arXiv:2512.10504v2 | Tianyan: Cloud services with quantum advantage

[3] arXiv:1304.1214v1 | Bell-state measurement and quantum teleportation using linear optics: two-photon pairs, entangled coherent states, and hybrid entanglement

[4] arXiv:2003.11810v4 | Searching for Coherent States: From Origins to Quantum Gravity

[5] arXiv:2112.14193v3 | A full circuit-based quantum algorithm for excited-states in quantum chemistry

[6] arXiv:1811.09849v1 | Interaction of light and semiconductor can generate quantum states required for solid state quantum computing: Entangled, steered and other nonclassical states

[7] arXiv:2402.08949v3 | Unraveling the emergence of quantum state designs in systems with symmetry

[8] arXiv:2408.15444v4 | Quantum games and synchronicity

[9] QNFO: Standard Model | DOI 10.5281/zenodo.17210901

[10] QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation | DOI 10.5281/zenodo.22753022

[11] QNFO: EMERGENT CORRELATION IN A LOCAL-DETERMINISTIC UNIVERSE | DOI 10.5281/zenodo.18015329

[12] QNFO: Manifesto for Honest Computation | DOI 10.5281/zenodo.21299278