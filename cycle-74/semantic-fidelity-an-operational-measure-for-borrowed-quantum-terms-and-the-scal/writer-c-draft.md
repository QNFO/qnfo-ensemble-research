# Semantic Fidelity: An Operational Measure for Borrowed Quantum Terms and the Scale at Which They Fail

## Abstract

Quantum computing borrows its vocabulary from quantum optics, condensed matter, and particle physics, and this borrowed ontology can quietly conflict with the operational content of the circuit model it is meant to describe. We propose an operational quantity, semantic fidelity $F_S$, defined as one minus the total variation distance between the decision-relevant outcome distributions implied by a borrowed term's native ontology and those implied by the target circuit model. We illustrate the measure on the term "photon": for two indistinguishable bosons at a balanced beamsplitter, the native ontology predicts bunching with probability $1$, while a distinguishable-particle (qubit-like) reading predicts a split outcome with probability $1/2$, giving $F_S = 1/2$ per interference element. Because semantic divergence compounds across independent elements, the total variation distance over $k$ such elements is $1 - 2^{-k}$, crossing a decision-relevance threshold of $0.9$ at $k = 4$, i.e., roughly eight qubits of photonic hardware. We further compute gate budgets implied by published superconducting fidelities (single-qubit $99.90\%$, two-qubit $99.56\%$, readout $98.7\%$), yielding error-free-gate budgets of approximately $1000$, $227$, and $77$ operations. We argue that semantic fidelity supplies a vocabulary-neutral diagnostic for when borrowed terms become decision-relevantly misleading, and we discuss validation paths and failure modes.

## 1. Introduction

Quantum computing did not inherit its language from its own foundations. Words such as "photon," "quasiparticle," "exchange," and "particle number" arrive from quantum optics, condensed matter physics, and particle physics, each carrying an ontology — a commitment about what exists and what can be distinguished, copied, and counted. The circuit model of quantum computation, by contrast, commits only to finite-dimensional unitary dynamics, measurement, and classical control. When the two ontologies agree on all operational predictions, the borrowed vocabulary is harmless shorthand. When they disagree, the borrowed term becomes actively misleading: it suggests experiments, error models, or engineering intuitions that the circuit model does not support.

The central conjecture of this paper, following the research idea recorded in the author's notebook [source: owner notebook notes/v1/2026/07/20], is that this disagreement is not merely philosophical but quantifiable. We define an operational semantic fidelity $F_S$ for a borrowed term $T$ used in a computational context $C$: the closeness, in total variation distance, between the outcome distributions that $T$'s native ontology predicts and those that $C$'s formalism predicts, restricted to the observables that actually drive decisions in $C$. A term is semantically faithful at scale $n$ if $F_S$ remains above a decision threshold; it becomes provably misleading at the smallest $n$ where $F_S$ falls below that threshold.

This matters for three reasons. First, semantic drift is a candidate explanation for stalled collaborations between physicists and engineers: if the two communities attach different operational content to the same word, joint designs can fail without any party making an arithmetic error. Second, a quantitative measure converts a vague worry about "ontological baggage" into a testable engineering specification, in the same way that gate fidelity converted "noise" into a budget. Third, a vocabulary-neutral formulation sharpens the question of what the quantum formalism itself asserts, as opposed to what its particle-flavored dialect asserts.

Our contributions are: (i) a formal definition of operational semantic fidelity (Section 3); (ii) a fully worked derivation for the term "photon," including an explicit compounding law and a concrete qubit count at which the term crosses a stated decision threshold (Section 4); (iii) gate-budget computations from published superconducting fidelities, showing that even the native vocabulary of the circuit model has finite semantic reach (Section 4); and (iv) a discussion of validation, falsification, and limits (Section 6). We report only quantities we derive here or clearly labeled projections with stated assumptions; we perform no new experiments and cite no empirical results beyond those stated in the supplied literature summaries.

## 2. Background and Related Work

We organize the related work into four strands: quantitative device characterizations, vocabulary-neutral formulations of quantum theory, analyses of term meaning imported from information retrieval, and the QNFO corpus of ontological critiques.

**Device-level characterizations.** The Tianyan Quantum Cloud Platform report [1] describes a cloud-accessible superconducting prototype, Tianyan-287, with $105$ qubits and operational fidelities of $99.90\%$ (single-qubit gates), $99.56\%$ (two-qubit gates), and $98.7\%$ (readout). These numbers are exactly the kind of operational budget that our measure treats as the target side of the comparison: they quantify how far the implemented circuit model departs from its own idealized vocabulary. We use them in Section 4 to compute error-free-gate budgets. The holographic entanglement entropy simulation on a quantum simulator [8] reports an experiment simulating quantum gravity, motivated by the difficulty of modeling such problems classically; it is an example of a term ("holographic entropy") traveling from high-energy physics into quantum simulation, i.e., a borrowed term whose native ontology lives far from the simulating device. The supplied summary gives no further quantitative detail, so we use it only as an instance of cross-domain vocabulary transfer, not as a source of numbers.

**Vocabulary-neutral formulations.** Quantum Measure Theory [2] proposes a realistic, spacetime interpretation in which reality constitutes a single history obeying a "law of motion" that makes definite but incomplete predictions, and associates a "quantum measure" $|S|$ to a set $S$ of histories, satisfying a sum rule generalizing classical probability. This is a candidate vocabulary-neutral base: histories, not particles, carry the ontology. The follow-up work [3] notes that the quantum measure $\mu$ is defined for arbitrary events (sets of histories) rather than observables at a fixed time, and that interference effects allow $\mu$ to exceed unity, exhibiting its non-classical nature. That $\mu > 1$ is possible is precisely the kind of statement a particle-counting vocabulary cannot accommodate — a concrete instance of our thesis that borrowed classical-ontological terms (here, "measure" as a probability-like quantity) mislead at the formal level. The "impossible measurements" analysis [4] shows that naive combinations of relativity and quantum measurement lead to signaling between space-like separated regions, and that the same problem arises non-relativistically, where joint nonlocal measurements between spatially separated systems generically signal when no-signaling would be expected. This is an ontology clash made operational: the term "measurement," borrowed with its classical connotation of a localized probe, predicts signaling that the formalism forbids or permits depending on framing. The categorical analysis of quantum measurement without sums [7] shows that quantum mechanics can be expressed entirely in terms of the tensor product, without direct sums, with classical spaces characterized as objects that allow copying. This supplies a formal articulation of our key distinction: the ability to copy is the ontological marker separating classical-particle vocabulary from quantum vocabulary, and a borrowed term that presupposes copyability (e.g., "particle," "photon" as a countable object) is exactly a term whose native ontology exceeds what the tensor-product formalism grants.

**Error correction as a vocabulary consumer.** The stabilizer formalism for operator algebra quantum error correction [6] generalizes Gottesman's formulation for traditional quantum error correcting codes and Poulin's for operator quantum error correction and subsystem codes, generating hybrid classical-quantum stabilizer codes. Error-corrected codes are where borrowed vocabulary is under the most strain: "code distance," "logical qubit," and "error" are terms whose operational meaning depends on which layer of the hybrid classical-quantum structure they attach to. Our measure is designed to be applicable at this boundary, though we do not compute a code-distance threshold here (see Section 6).

**Term meaning in information retrieval.** The white-box analysis of ColBERT [5] dissects the matching process of a transformer-based retrieval model through term importance and exact/soft matching patterns, in a context where it had been claimed that BERT does not satisfy the classical IR axioms, though the authors note the traditional axioms are not formally violated in the way claimed. Methodologically this is our closest analogue outside physics: a work that opens the box on how a system actually uses its terms, as opposed to how its vocabulary suggests it does. We borrow the posture, not the machinery: our "white box" is the operational outcome distribution.

**The QNFO corpus.** The QNFO work on computing and quantum error correction [9] is supplied to us with no summary text; we therefore cite it only as part of the corpus context and draw no claim from it. "Beyond the Qubit" [10], a companion to "The Qubit Delusion," argues that if the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto relational, field-theoretic reality — then constructive post-particle paradigms are needed, and it strips quantum mechanics to minimal ontological commitments. Our paper accepts the diagnosis of ontological projection but differs in method: rather than arguing the failure globally, we localize it with an operational divergence and a scale. "The Ultrametric Program" [11] claims that seven research domains are seven vocabularies for one structural object — nested hierarchical partition logic defined by the ultrametric inequality — with three falsifiable hypotheses; this is a vocabulary-invariant reading of physics that our semantic-fidelity program could in principle serve as a measuring instrument for, though the supplied summary is truncated and we make no use of its specific hypotheses. Finally, "No Thing There" [12] is a pedagogical bridge between qubit ontology critique and working physics, explaining what control pulses actually manipulate and what readout measures across superconducting transmon, trapped-ion, and spin qubit platforms, including a self-referential metrology formalization. It supplies the engineering ground truth against which any semantic-fidelity measure must be calibrated: the measure is useful only if it tracks what control and readout actually do.

## 3. Methods

### 3.1 Definitions

Fix a computational context $C$: a family of circuits (or code operations) parameterized by a size $n$, a set of decision-relevant observables $\mathcal{O}_C$, and a decision rule that maps measurement outcomes to actions. Fix a borrowed term $T$ with a native ontology $O_T$: a set of commitments (distinguishability, copyability, number conservation, locality of probes) strong enough to generate predictions. Concretely, both $O_T$ and the formalism of $C$ induce probability distributions over outcomes of the observables in $\mathcal{O}_C$:

$$P_T^{(n)}(x) \quad \text{and} \quad P_C^{(n)}(x), \qquad x \in \mathcal{X}^{(n)},$$

where $\mathcal{X}^{(n)}$ is the outcome space at size $n$. The operational divergence is the total variation distance

$$D_{TV}^{(n)}(T, C) = \frac{1}{2} \sum_{x \in \mathcal{X}^{(n)}} \left| P_T^{(n)}(x) - P_C^{(n)}(x) \right|,$$

and the semantic fidelity is

$$F_S^{(n)}(T, C) = 1 - D_{TV}^{(n)}(T, C).$$

Total variation distance (half the $\ell_1$ distance between distributions) is chosen because it has a direct decision meaning: it upper-bounds the advantage any decision rule can gain by using one description instead of the other. If $D_{TV}^{(n)} = \delta$, then no test built on $\mathcal{O}_C$ can distinguish the two ontologies with advantage exceeding $\delta$; conversely some test achieves advantage close to $\delta$.

### 3.2 Decision threshold and failure scale

Fix a decision-relevance threshold $\varepsilon \in (0,1)$, set by the cost of a wrong design decision in context $C$. The term $T$ is **semantically faithful** at size $n$ if $D_{TV}^{(n)} \leq \varepsilon$ and **provably misleading** at the smallest $n^*$ with

$$D_{TV}^{(n^*)} > \varepsilon.$$

The qualifier "provably" is earned because $D_{TV}$ is computed from the two ontologies' own predictions, not from hardware data: it is a statement about vocabularies, conditional on each vocabulary's generating the distributions claimed.

### 3.3 Compounding across independent elements

Realistic contexts contain many independent loci where a borrowed term is invoked. If the context decomposes into $k$ independent elements, each with per-element divergence $\delta_i = D_{TV}^{(1)}$ on element $i$, and the joint outcome distribution factorizes, then the joint divergence is

$$D_{TV}^{(k)} = 1 - \prod_{i=1}^{k} (1 - \delta_i).$$

For identical elements with $\delta_i = \delta$ this gives the compounding law

$$D_{TV}^{(k)} = 1 - (1 - \delta)^{k}.$$

This law is what converts a per-element semantic gap into a scale: even a small per-element divergence becomes decision-relevant once $k \gtrsim \ln(1-\varepsilon)/\ln(1-\delta)$... more precisely, once $(1-\delta)^k \leq 1 - \varepsilon$.

### 3.4 Validation plan (survey component)

The measure is validated in three steps: (i) analytic computation of $F_S$ for canonical borrowed terms ("photon," "particle number," "measurement") in circuit contexts, as begun in Section 4; (ii) simulation of growing entangled systems comparing photonic-ontological and circuit-model predictions, to check that the compounding law holds when elements are only approximately independent; and (iii) a survey of engineer mental models, testing whether practitioners whose descriptions diverge by $D_{TV} \geq \varepsilon$ also make divergent design choices. Steps (ii) and (iii) are future work; this paper executes step (i) and states the projections that follow from it.

## 4. Analysis

Every input number below is stated with its source, and every arithmetic step is shown.

### 4.1 Per-element divergence for "photon": the two-boson beamsplitter

**Setup.** The term "photon" carries, in its native quantum-optical ontology, the commitments of bosonic indistinguishability and the copyability-free structure emphasized in the categorical analysis [7]. Consider the canonical decision-relevant observable: a balanced beamsplitter with one particle in each input port, and the output observable "do the two particles exit the same port or different ports?"

**Native-ontology (bosonic) prediction.** For two indistinguishable bosons at a $50/50$ beamsplitter, the two amplitudes for the "split" outcomes (one in each output port) interfere destructively; the bunching outcome (both in the same port, either port) occurs with probability

$$P_T(\text{same}) = 1, \qquad P_T(\text{split}) = 0.$$

This is the standard two-boson interference result; we take it as the prediction generated by the native ontology of "photon."

**Distinguishable-particle (qubit-like) prediction.** The circuit-model reading — two distinguishable two-level systems, each routed $50/50$ — assigns independent $50/50$ outcomes:

$$P_C(\text{same}) = \frac{1}{2}, \qquad P_C(\text{split}) = \frac{1}{2}.$$

**Divergence.** With outcome space $\mathcal{X} = \{\text{same}, \text{split}\}$:

$$D_{TV}^{(1)} = \frac{1}{2}\left( \left| 1 - \tfrac{1}{2} \right| + \left| 0 - \tfrac{1}{2} \right| \right) = \frac{1}{2}\left( \tfrac{1}{2} + \tfrac{1}{2} \right) = \frac{1}{2}.$$

$$F_S^{(1)}(\text{photon}, \text{circuit}) = 1 - \frac{1}{2} = \frac{1}{2}.$$

So a single two-photon interference element already has semantic fidelity $0.5$: a decision rule betting on the qubit-like reading is wrong half the time on the bunching question.

### 4.2 Compounding: the scale at which "photon" becomes provably misleading

**Assumption (stated).** The context contains $k$ independent two-photon interference elements, each with the per-element divergence $\delta = 1/2$ derived above, and the joint outcome distribution factorizes. Under the compounding law of Section 3.3:

$$D_{TV}^{(k)} = 1 - \left(1 - \frac{1}{2}\right)^{k} = 1 - 2^{-k}.$$

We tabulate:

$$
\begin{array}{c|cccccc}
k & 1 & 2 & 3 & 4 & 5 & 6 \\
\hline
D_{TV}^{(k)} & 0.5 & 0.75 & 0.875 & 0.9375 & 0.96875 & 0.984375 \\
F_S^{(k)} & 0.5 & 0.25 & 0.125 & 0.0625 & 0.03125 & 0.015625
\end{array}
$$

**Threshold crossing.** With the decision threshold $\varepsilon = 0.9$ (a design choice; we state it explicitly), the term becomes provably misleading at the smallest $k^*$ with $1 - 2^{-k} > 0.9$, i.e., $2^{-k} < 0.1$, i.e.,

$$k > \frac{\ln(0.1)}{\ln(0.5)} = \frac{-2.302585\ldots}{-0.693147\ldots} \approx 3.3219,$$

so $k^* = 4$. Checking: $D_{TV}^{(3)} = 0.875 \leq 0.9$ and $D_{TV}^{(4)} = 0.9375 > 0.9$. Each element involves two particles, so the crossing occurs at $2 \times 4 = 8$ particles' worth of interferometric hardware.

**Projection (labeled).** If each interference element is implemented with a two-qubit (or two-mode) unitary, the term "photon" becomes decision-relevantly misleading at approximately $n^* = 8$ qubits of photonic-interference hardware. This is a projection from the compounding law under the stated independence and factorization assumptions, not a simulation result; correlations among elements could raise or lower $n^*$, and Section 6 quantifies the direction of that uncertainty.

### 4.3 Gate budgets for the circuit model's own vocabulary

Even the circuit model's native vocabulary ("qubit," "gate") has finite semantic reach, because hardware departs from it. The Tianyan-287 report [1] supplies the input fidelities. We compute the expected number of consecutive operations before the first departure from the ideal-circuit prediction, i.e., the error-free budget $N = 1/(1 - F)$ for fidelity $F$.

**Single-qubit gates.** Input: $F_1 = 99.90\% = 0.9990$ [1]. Error per gate: $p_1 = 1 - 0.9990 = 0.0010 = 1.0 \times 10^{-3}$.

$$N_1 = \frac{1}{p_1} = \frac{1}{1.0 \times 10^{-3}} = 1000 \text{ gates}.$$

**Two-qubit gates.** Input: $F_2 = 99.56\% = 0.9956$ [1]. Error per gate: $p_2 = 1 - 0.9956 = 0.0044 = 4.4 \times 10^{-3}$.

$$N_2 = \frac{1}{p_2} = \frac{1}{4.4 \times 10^{-3}} = 227.27\ldots \approx 227 \text{ gates}.$$

**Readout.** Input: $F_r = 98.7\% = 0.987$ [1]. Error per readout: $p_r = 1 - 0.987 = 0.013 = 1.3 \times 10^{-2}$.

$$N_r = \frac{1}{p_r} = \frac{1}{1.3 \times 10^{-2}} = 76.92\ldots \approx 77 \text{ readouts}.$$

**Interpretation.** These budgets are the semantic reach of the word "qubit" as used on this platform: beyond roughly $227$ two-qubit gates or $77$ readout events, the ideal-circuit meaning of "qubit" diverges from the implemented meaning with probability approaching unity (the probability of at least one departure after $N_2$ gates is $1 - (1 - p_2)^{N_2} = 1 - 0.9956^{227} \approx 1 - e^{-227 \times 0.0044} \approx 1 - e^{-0.9988} \approx 0.632$ at exactly $N_2$ gates, and exceeds $0.9$ at $k$ gates where $(0.9956)^k < 0.1$, i.e., $k > \ln(0.1)/\ln(0.9956) = (-2.302585)/(-0.0044097) \approx 522.2$, so $k = 523$ gates). The readout channel is the weakest link: the word "qubit" survives only $\approx 77$ readouts before its ideal meaning is more likely than not to have been violated.

### 4.4 Where the measure attaches to error correction

Error-corrected codes are the regime where the circuit model's vocabulary is stretched furthest, and the operator-algebra stabilizer framework [6] makes the hybrid classical-quantum layering explicit. We do not compute a code-distance threshold here, because doing so requires noise-model inputs not supplied in the literature summaries; we flag it as the primary simulation target for step (ii) of the validation plan. What the analysis of Section 4.2 already shows is the shape of the answer: if each code cycle contains $k_{\text{cycle}}$ loci where a borrowed term (e.g., "anyon," "particle number," "syndrome") carries divergent ontological content with per-locus divergence $\delta$, the cycle-level divergence is $1 - (1-\delta)^{k_{\text{cycle}}}$, and the code distance at which the term misleads is obtained by the same threshold computation as in Section 4.2 with $k$ replaced by the number of cycles times loci per cycle.

## 5. Results

We report only quantities derived in Section 4, plus clearly labeled projections.

**R1 (derived).** For the term "photon" at a balanced two-boson beamsplitter, the operational divergence between the native bosonic ontology and the distinguishable-particle circuit reading is $D_{TV}^{(1)} = 1/2$, hence $F_S^{(1)} = 1/2$ (Section 4.1).

**R2 (derived, under stated independence assumption).** Across $k$ independent interference elements, $D_{TV}^{(k)} = 1 - 2^{-k}$; values: $0.5, 0.75, 0.875, 0.9375, 0.96875, 0.984375$ for $k = 1,\ldots,6$ (Section 4.2).

**R3 (derived, given threshold $\varepsilon = 0.9$).** The crossing index is $k^* = 4$ elements, since $D_{TV}^{(3)} = 0.875 \leq 0.9 < 0.9375 = D_{TV}^{(4)}$ (Section 4.2).

**R4 (projection).** Under the assumption that each interference element is a two-qubit (two-mode) unitary, "photon" becomes provably misleading at approximately $n^* = 8$ qubits of photonic-interference hardware. Uncertainty: element correlations can shift $n^*$ by a factor of order unity in either direction; the projection is exact only under perfect independence and factorization.

**R5 (derived from [1]).** Using the Tianyan-287 fidelities $F_1 = 0.9990$, $F_2 = 0.9956$, $F_r = 0.987$: error-free budgets $N_1 = 1000$ single-qubit gates, $N_2 \approx 227$ two-qubit gates, $N_r \approx 77$ readouts; the probability of at least one two-qubit-gate departure exceeds $0.9$ at $k = 523$ gates (Section 4.3).

**R6 (qualitative, from the literature summaries).** The formalism-level analogues of semantic divergence are documented in the supplied literature: the quantum measure $\mu$ can exceed unity through interference [3], "measurement" with a classical localized-probe connotation predicts signaling where none is expected [4], and the copyability presupposed by particle vocabulary is exactly what the tensor-product-only formulation of measurement denies to quantum systems [7].

## 6. Discussion

**Limitations.** The derivation of R1–R3 is analytic and conditional: it compares two idealized ontologies, not two physical devices. The compounding law assumes independence and factorization; real interferometric elements share modes, sources, and control hardware, so the true joint divergence can be smaller (common-cause structure reduces effective independence) or larger (coherent accumulation of phase-type divergences). The threshold $\varepsilon = 0.9$ is a stipulation, not a measurement; a different application domain would set it differently, and the crossing index $k^*$ scales as $\ln(1-\varepsilon)/\ln(1-\delta)$, so it is sensitive to both $\varepsilon$ and the per-element $\delta$. The gate budgets of R5 are expectations under an independence-of-errors assumption that real devices may violate through correlated or leakage-type errors; the supplied summary of [1] states the fidelities but not their error correlations, so R5 should be read as an optimistic budget.

**Failure modes of the measure itself.** First, the choice of decision-relevant observables $\mathcal{O}_C$ is a modeling act; an adversarial or careless choice can manufacture or hide divergence. Second, $F_S$ compares ontologies as prediction-generators, but a borrowed term can be heuristically fruitful even while operationally divergent — the measure penalizes exactly the cases where the term changes decisions, which may be the cases where the term is doing useful exploratory work. Third, the measure is silent about terms whose native ontology generates no predictions at all in $\mathcal{O}_C$; for such terms a different diagnostic (predictive vacuity) is needed.

**What would falsify the claims.** The central empirical claim — that operational divergence at scale $n^*$ correlates with real collaboration and design failures — would be falsified by the survey in step (iii) of the validation plan finding no association between practitioners' description-level divergences and their design choices. The compounding law would be falsified by simulation (step ii) showing that joint divergence grows sub-multiplicatively in a way that pushes $n^*$ beyond practical scales, i.e., that borrowed terms remain decision-faithful at all practically relevant $n$. The claim that the beamsplitter divergence is generic would be falsified by finding that the decision-relevant observables of actual photonic computing contexts never include the bunching/split question in a decision-relevant role.

**Arguing against ourselves.** A skeptic may say the beamsplitter example is a strawman: no engineer confuses a photonic interference element with two distinguishable qubits, and the divergence $1/2$ reflects a deliberately naive reading. Our reply is that the measure is aimed not at expert confusion but at the silent migration of intuitions — error models, counting arguments, resource estimates — that inherit particle ontology without the user noticing; the QNFO critique [10] makes exactly this point at the paradigm level, and "No Thing There" [12] documents how far actual control and readout practice sits from the particle picture. A second objection: the vocabulary-neutral base we gesture at (histories [2], tensor-product-only measurement [7]) is itself a vocabulary, so the measure only relocates the problem. This is partly right; our defense is that $F_S$ is defined pairwise between any two vocabularies and does not privilege one as fundamental — the ultrametric-program claim that multiple domain vocabularies describe one structural object [11] is compatible with, and motivates, a pairwise divergence measure. A third objection: the $n^* = 8$ projection is far below the $105$-qubit scale of current platforms [1], suggesting the effect should already have been noticed. We agree this is a tension; the resolution we propose is that at large scales practitioners stop using the borrowed term operationally (they use tomography, benchmarking, and error budgets instead), so the divergence manifests as vocabulary abandonment rather than as error — a hypothesis the survey component could test.

**Open questions.** (i) What is the per-element divergence $\delta$ for