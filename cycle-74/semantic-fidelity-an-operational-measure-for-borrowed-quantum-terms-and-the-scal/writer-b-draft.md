# Semantic Fidelity of Borrowed Quantum Terms: An Operational Divergence Measure and a Critical-Scale Estimate

## Abstract

Quantum computing borrows its vocabulary from quantum optics, condensed matter, and particle physics. We conjecture that this borrowed vocabulary carries ontological commitments that become operationally misleading as engineered quantum systems scale, and we make the conjecture precise. We define *semantic fidelity* $F_{\mathrm{sem}}(T;n)$ of a borrowed term $T$ at scale $n$ as the probability that all operational commitments implied by the term's native ontology survive $n$ independent invocations in the target circuit-model description. We state an explicit decision criterion: a term becomes decision-relevantly misleading when the probability that at least one commitment is violated exceeds one half. Calibrating the per-invocation mismatch rate $\varepsilon$ to published hardware error rates of the Tianyan-287 superconducting processor (105 qubits; single-qubit, two-qubit, and readout fidelities of 99.90%, 99.56%, and 98.7%), we derive critical scales $n^{*} \approx 693$, $157$, and $53$ invocations for terms calibrated to single-qubit, two-qubit, and readout error rates respectively, and, under a stated toy code model, a critical code distance $d^{*} = 9$. We also compute an aggregate no-error fidelity $F \approx 9.76 \times 10^{-3}$ for a representative depth-10 circuit on all 105 qubits. We situate the measure relative to vocabulary-neutral formulations of quantum theory, stabilizer formalisms for error correction, and prior critiques of qubit ontology, and we state the assumptions under which the conjecture would be falsified.

## 1. Introduction

A working quantum engineer says "photon," "phonon," "quasiparticle," or "qubit" and, in doing so, imports a picture of the world from the field in which the term was coined. The picture is harmless — indeed useful — while experiments are small and the term's native ontology and the operational circuit model agree on every prediction that matters. The conjecture examined in this paper is that the agreement is not scale-invariant: as systems grow toward error-corrected, many-qubit regimes, the ontological baggage of borrowed terms becomes an active source of error in reasoning, communication, and design.

The idea is not merely philosophical. If two collaborators use "photon" with different implied commitments — countability, localizability, mode occupancy — they may agree on every equation and yet disagree on what experiment to build next. If a funding agency evaluates a proposal using a particle-counting mental model while the relevant formalism is relational, resources may be misallocated. The contribution here is to convert this worry into a quantity.

We proceed in three steps. First, we define semantic fidelity operationally: a borrowed term is treated as a predictor-generating device, and its fidelity is the probability that its native-ontology commitments and the target formalism agree across an experiment of a given size. Second, we calibrate the mismatch rate to published hardware figures [1], which supplies a physically meaningful unit of "ontological mismatch per invocation." Third, we derive critical scales — invocation counts, and, under a toy code model, a code distance — at which the divergence becomes decision-relevant by an explicit majority criterion.

Throughout, "ontology" means the minimal set of commitments a term licenses in reasoning (e.g., that there exist countable, individually addressable excitations), not a metaphysical thesis. "Target model" means the circuit-and-stabilizer description in which quantum computation is specified [6]. The measure is defined so that it can be evaluated by simulation of growing entangled systems and by surveying practitioner mental models; in this paper we carry out the analytical calibration and identify what the simulations must test.

## 2. Background and Related Work

We discuss the works supplied in the bibliography, in each case restricting ourselves to what the supplied entries state.

**Hardware calibration point.** The Tianyan Quantum Cloud Platform entry [1] reports a cloud-accessible superconducting prototype, Tianyan-287, with 105 qubits and single-qubit gate, two-qubit gate, and readout fidelities of 99.90%, 99.56%, and 98.7%, respectively, in a Zuchongzhi 3.0-like processor. These are the only quantitative hardware figures we use, and we use them solely as a calibration scale for mismatch rates (Section 4). The entry supplies no further device details.

**Vocabulary-neutral formulations of quantum theory.** Two entries describe formalisms that do not presuppose a particle-based ontology. The quantum measure theory entry [2] proposes a realistic, spacetime interpretation in which reality constitutes a single history obeying a "law of motion" that makes definite but incomplete predictions, associating a quantum measure $|S|$ to a set $S$ of histories satisfying a sum rule generalizing classical probability. For our purposes this is a precedent for formulating quantum predictions without importing particle talk: the objects of the theory are histories, not things. The companion entry [3] states that the quantum measure $\mu$ in Quantum Measure Theory is defined for arbitrary events (sets of histories) rather than observables at a fixed time, and that, thanks to interference, $\mu$ can exceed unity, exhibiting its non-classical nature. This supplies a concrete diagnostic: a vocabulary built on classical probability intuitions ("measures are at most one") is already provably inapplicable in QMT, which is exactly the kind of commitment-violation our fidelity measure is designed to detect. A third entry, "Quantum measurements without sums" [7], reports that a conceptual analysis of quantum measurement suggests quantum mechanics can be done without direct sums, expressed entirely in terms of the tensor product, with classical spaces characterized as objects that allow copying. This is the closest structural precedent to our program: it shows that a seemingly indispensable piece of the standard vocabulary (the direct sum) can be eliminated in favor of a single structural primitive, i.e., that vocabulary reduction is a live possibility in the foundations of quantum formalism.

**Ontological baggage producing concrete paradoxes.** The entry on "impossible measurements" [4] states that naive attempts to combine relativity and quantum measurements lead to signaling between space-like separated regions — the "impossible measurements" of QFT — and that the same problem arises in non-relativistic quantum physics, where joint nonlocal measurements between spatially separated systems in general lead to signaling where one would expect no-signaling. We read this as evidence that a measurement vocabulary imported without its native caveats generates apparent violations of physical principles; the error lies in the vocabulary's implied commitments, not in the formalism.

**Formal target for error-corrected scales.** The stabilizer formalism entry [6] introduces a stabilizer formalism for operator algebra quantum error correction (OAQEC), generalizing Gottesman's formulation for traditional quantum error correcting codes and Poulin's for operator quantum error correction and subsystem codes, generating hybrid classical-quantum stabilizer codes. This is the formal environment in which our code-distance projections (Section 4) are stated: the "target model" against which borrowed terms are compared is a stabilizer-type code description.

**Cross-domain term borrowing as a phenomenon.** The holographic entanglement entropy entry [8] reports an experiment simulating quantum gravity — specifically holographic entanglement entropy — on a quantum simulator, in a context noting that quantum devices have been built for problems in quantum chemistry, condensed matter physics, and high-energy physics. This is a case study of terms traveling between fields: gravity vocabulary evaluated on a quantum device, precisely the migration pattern our measure is intended to score. The ColBERT white-box analysis entry [5] is included as a methodological analogy from information retrieval: transformer models are state-of-the-art in ad-hoc IR but poorly understood; work has claimed BERT does not satisfy the classical IR axioms; the authors dissect ColBERT's matching process through term importance and exact/soft matching patterns, noting the traditional axioms are not formally valid (the entry's text is truncated at this point and supplies no further detail). The relevance is structural: an operational dissection of whether terms in a model satisfy the "axioms" they inherited — exactly the move we make for quantum vocabulary.

**The qubit-ontology critique line.** The QNFO entry "Beyond the Qubit" [10] is described as a companion to "The Qubit Delusion" and poses the question: if the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto relational, field-theoretic reality — what comes next? It reports stripping quantum mechanics to minimal ontological commitments. This is the direct intellectual ancestor of our conjecture; our contribution is to make the "epistemic failure" quantitative and scale-dependent rather than global. The entry "No Thing There" [12] is described as a pedagogical bridge between qubit ontology critique and working physics, explaining what control pulses actually manipulate and what readout measures across superconducting transmon, trapped-ion, and spin-qubit platforms, including an electrical seesaw analogy and a self-referential metrology formalization. It supplies the operational grounding our definition requires: commitments must be tied to what control and readout actually do. The "Ultrametric Program" entry [11] claims seven research domains are seven vocabularies for one structural object — nested hierarchical partition logic defined by the ultrametric inequality, with p-adic/adelic arithmetic one realization and the hierarchy the invariant — and lists three falsifiable hypotheses (H1 compression prior, H2 Ar—, truncated in the supplied text). We use it as a precedent for the claim that a single invariant can underlie multiple vocabularies, which is the shape of a vocabulary-neutral reformulation. Finally, the QNFO computing-and-QEC entry [9] is supplied with title and DOI only; its summary gives no further detail, and we cite it only as part of the same corpus without attributing any content to it.

## 3. Methods

### 3.1 Definition of semantic fidelity

Let $T$ be a borrowed term. Associated with $T$ in its native ontology $O_{N}$ is a finite set of operational commitments $C_{T} = \{c_{1}, \dots, c_{k}\}$: statements that, if $T$ applies, are licensed as true in reasoning (e.g., for "photon": excitations are countable; each is localizable to a mode; mode occupations are the conserved quantities). Associated with the target model $O_{T}$ (circuit/stabilizer description [6]) is a set of operational predictions $P_{T}(E)$ for an experiment $E$.

Define an *invocation* of $T$ as one use of $T$ to generate a prediction or design decision within one experiment. Let $\varepsilon_{T}$ be the per-invocation probability that at least one commitment in $C_{T}$, taken at face value, diverges from the corresponding prediction of $O_{T}$ in a way that changes the operational conclusion. We assume invocations are independent and identically distributed; this is the strongest assumption in the framework and we return to it in Section 6.

The semantic fidelity of $T$ at scale $n$ is then

$$F_{\mathrm{sem}}(T; n) = (1 - \varepsilon_{T})^{n},$$

the probability that no commitment is violated across $n$ independent invocations. This is the standard no-failure probability of a Bernoulli trial sequence with failure probability $\varepsilon_{T}$ per trial.

### 3.2 Decision-relevance criterion

We stipulate the following operational criterion, chosen so that "misleading" means "more likely than not to have already produced at least one reasoning error":

$$\text{$T$ is decision-relevantly misleading at scale $n$} \iff 1 - F_{\mathrm{sem}}(T; n) \geq \tfrac{1}{2}.$$

Solving for the critical scale $n^{*}$:

$$1 - (1 - \varepsilon_{T})^{n^{*}} = \tfrac{1}{2} \quad\Longrightarrow\quad n^{*} = \frac{\ln(1/2)}{\ln(1 - \varepsilon_{T})} = \frac{-\ln 2}{\ln(1 - \varepsilon_{T})}.$$

Since $\ln(1-\varepsilon_{T}) < 0$, $n^{*} > 0$. The criterion is a convention; any threshold $\delta$ replaces $\tfrac{1}{2}$, and we note the general form $n^{*}(\delta) = \ln(1-\delta)/\ln(1-\varepsilon_{T})$.

### 3.3 Calibration of $\varepsilon_{T}$

We lack direct measurements of ontological mismatch rates; the empirical program (simulation of photonic versus circuit descriptions, and practitioner surveys) is designed to measure them. Here we adopt a conservative, explicitly labeled calibration: set $\varepsilon_{T}$ equal to a published hardware error rate, so that "one ontological mismatch per invocation" is priced at the same rarity as one gate error. This makes $n^{*}$ interpretable as the scale at which the term's baggage is as probable an event as a single gate fault. We use the Tianyan-287 figures [1]:

$$\varepsilon_{1} = 1 - 0.9990 = 1.0 \times 10^{-3}, \qquad \varepsilon_{2} = 1 - 0.9956 = 4.4 \times 10^{-3}, \qquad \varepsilon_{r} = 1 - 0.987 = 1.3 \times 10^{-2},$$

for terms calibrated to single-qubit-gate, two-qubit-gate, and readout operation rates respectively.

### 3.4 Toy code model

To express $n^{*}$ as a code distance, we adopt a toy model, stated as an assumption and not derived from any cited work: a code of distance $d$ uses $n_{\mathrm{phys}}(d) = 2d^{2} - 1$ physical qubits per logical qubit, and each physical qubit participates in one two-qubit-gate-calibrated invocation per logical operation. Under this model the critical distance $d^{*}$ is the smallest integer $d$ with $2d^{2} - 1 \geq n^{*}_{2}$. We also compute, as a labeled toy projection with leading coefficient set to unity, a logical error rate $\sim p^{(d+1)/2}$ with $p = \varepsilon_{2}$; the coefficient is not calibrated and the number is illustrative only.

## 4. Analysis

All inputs are stated with sources; all arithmetic is shown.

**Input 1 (from [1]):** single-qubit fidelity $F_{1} = 0.9990$; two-qubit fidelity $F_{2} = 0.9956$; readout fidelity $F_{r} = 0.987$; qubit count $N_{q} = 105$.

**Derivation 1: error rates.**
$$\varepsilon_{1} = 1 - 0.9990 = 1.0 \times 10^{-3}, \qquad \varepsilon_{2} = 1 - 0.9956 = 4.4 \times 10^{-3}, \qquad \varepsilon_{r} = 1 - 0.987 = 1.3 \times 10^{-2}.$$

**Derivation 2: critical scales.** Using $n^{*} = -\ln 2 / \ln(1-\varepsilon)$ with $\ln 2 = 0.693147$:

- Single-qubit calibration: $\ln(1 - 0.001) = \ln(0.9990) \approx -(0.001 + 0.001^{2}/2) = -0.0010005$. Then
$$n^{*}_{1} = \frac{0.693147}{0.0010005} \approx 692.8 \implies n^{*}_{1} \approx 693.$$
- Two-qubit calibration: $\ln(0.9956) \approx -(0.0044 + 0.0044^{2}/2) = -(0.0044 + 0.00000968) = -0.0044097$. Then
$$n^{*}_{2} = \frac{0.693147}{0.0044097} \approx 157.2 \implies n^{*}_{2} \approx 157.$$
- Readout calibration: $\ln(0.987) \approx -(0.013 + 0.013^{2}/2) = -(0.013 + 0.0000845) = -0.0130845$. Then
$$n^{*}_{r} = \frac{0.693147}{0.0130845} \approx 52.98 \implies n^{*}_{r} \approx 53.$$

**Derivation 3: semantic fidelity at the Tianyan-287 scale.** For a term calibrated at $\varepsilon_{2}$, evaluated at $n = 105$ invocations (one per qubit of the device [1]):
$$F_{\mathrm{sem}}(T; 105) = (0.9956)^{105} = \exp\!\big(105 \times (-0.0044097)\big) = \exp(-0.46302) \approx 0.6292.$$
So at the scale of a present 105-qubit device, a two-qubit-calibrated borrowed term survives all invocations with probability $\approx 0.629$; the violation probability is $\approx 0.371$, below the $0.5$ decision threshold — consistent with such terms remaining workable today, but not comfortably so.

**Derivation 4: aggregate no-error fidelity of a representative circuit.** Assume (stated assumption) a depth-$10$ circuit on all $105$ qubits with $1050$ single-qubit gate slots, $500$ two-qubit gate slots, and $105$ readouts. The no-error probability is
$$F = (0.9990)^{1050} \times (0.9956)^{500} \times (0.987)^{105}.$$
Compute each factor:
$$1050 \times (-0.0010005) = -1.05053, \quad (0.9990)^{1050} = e^{-1.05053} \approx 0.3498;$$
$$500 \times (-0.0044097) = -2.20485, \quad (0.9956)^{500} = e^{-2.20485} \approx 0.1103;$$
$$105 \times (-0.0130845) = -1.37387, \quad (0.987)^{105} = e^{-1.37387} \approx 0.2531.$$
Multiplying:
$$F \approx 0.3498 \times 0.1103 \times 0.2531 \approx 0.009763 \approx 9.76 \times 10^{-3}.$$
The aggregate failure probability is therefore $\approx 0.9902$. This is the hardware noise floor against which semantic divergence must be compared: a term whose commitments fail with probability comparable to $1 - F$ is not a marginal concern but a dominant one.

**Derivation 5: critical code distance (toy model).** With $n_{\mathrm{phys}}(d) = 2d^{2} - 1$ and $n^{*}_{2} = 157.2$:
$$2d^{2} - 1 \geq 157.2 \implies d^{2} \geq 79.1 \implies d \geq 8.89 \implies d^{*} = 9.$$
Check: $2(9)^{2} - 1 = 161 \geq 157.2$; $2(8)^{2} - 1 = 127 < 157.2$. So under the toy model, $d^{*} = 9$.

**Derivation 6: illustrative logical error scale (labeled toy projection).** With $p = 4.4 \times 10^{-3}$ and $d = 9$, the illustrative quantity $p^{(d+1)/2} = p^{5}$:
$$(4.4 \times 10^{-3})^{5} = 4.4^{5} \times 10^{-15} = 1649.2 \times 10^{-15} \approx 1.65 \times 10^{-12}.$$
This number assumes a leading coefficient of $1$ and is not a prediction about any real code; it is included only to show the regime the toy model implies.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are measured or simulated.

1. **Critical invocation scales** (majority criterion, Section 3.2, calibrated to Tianyan-287 error rates [1]): $n^{*}_{1} \approx 693$ invocations for single-qubit-calibrated terms, $n^{*}_{2} \approx 157$ for two-qubit-calibrated terms, $n^{*}_{r} \approx 53$ for readout-calibrated terms.
2. **Semantic fidelity at current scale:** $F_{\mathrm{sem}}(T; 105) \approx 0.629$ for a two-qubit-calibrated term on a 105-qubit device; violation probability $\approx 0.371$, below the decision threshold of $0.5$.
3. **Aggregate circuit no-error fidelity** (assumed depth-10, 105-qubit, 500 two-qubit gates, 105 readouts): $F \approx 9.76 \times 10^{-3}$, i.e., failure probability $\approx 0.9902$.
4. **Critical code distance (toy model, $n_{\mathrm{phys}} = 2d^{2}-1$):** $d^{*} = 9$.
5. **Illustrative logical error scale (labeled projection, coefficient assumed 1):** $p^{5} \approx 1.65 \times 10^{-12}$ at $p = 4.4 \times 10^{-3}$, $d = 9$.

**Projection statement.** Results 1, 2, and 4 are projections conditional on the stated calibration (that per-invocation ontological mismatch probability equals the corresponding hardware error rate) and the independence assumption of Section 3.1. If the true mismatch rate $\varepsilon_{T}$ is larger than the hardware error rate — plausible, since ontological commitments are invoked in reasoning, not only in gates — the critical scales shrink proportionally in $\ln(1-\varepsilon_{T})^{-1}$; if smaller, they grow. The qualitative claim — that $n^{*}$ is finite and lies in the tens-to-hundreds range for readout- and gate-calibrated rates — is the robust output.

## 6. Discussion

**What the measure does and does not claim.** The measure claims that borrowed terms carry commitments whose joint failure probability grows with scale, and that a majority criterion locates a finite critical scale. It does not claim that any particular term ("photon" included) has a measured mismatch rate; $\varepsilon_{T}$ is currently a calibration choice, not a measurement. The central empirical gap is the value of $\varepsilon_{T}$, and the proposed validation — simulating photonic versus circuit-model descriptions of multi-qubit gates and error-corrected codes, and surveying engineer mental models — is exactly the program that would replace calibration with measurement.

**Limitations and failure modes.** First, the independence assumption (Section 3.1) is likely wrong: ontological commitments are correlated across invocations because they arise from a single underlying description. Correlations can either accelerate failure (commitments fail together) or suppress it (one corrected commitment fixes many invocations); the direction is an empirical question. Second, the majority criterion is a convention. A team with high redundancy in reasoning might tolerate violation probabilities well above $0.5$; a safety-critical design review might need $F_{\mathrm{sem}} > 1 - 10^{-4}$, pushing $n^{*}$ down by a factor of $\ln(10^{-4})/\ln(0.5) \approx 13.3$ in the exponent — i.e., to roughly $n^{*}_{2}/13.3 \approx 12$ invocations under the same calibration. Third, the toy code model $n_{\mathrm{phys}} = 2d^{2}-1$ and the unit leading coefficient in Derivation 6 are stipulations, not results; $d^{*} = 9$ inherits every assumption of that model. Fourth, the calibration equates ontological mismatch with hardware error, which is conservative in pricing but arbitrary in kind: a mismatch is a reasoning error, not a physical fault, and the two may not be commensurable.

**What would falsify the conjecture.** The conjecture is falsified if, in simulation, photonic-ontology and circuit-model descriptions of growing entangled systems (e.g., error-corrected codes of increasing distance) yield decision-identical operational predictions at all accessible scales — i.e., if $\varepsilon_{T} \to 0$ empirically. It is also weakened if practitioner surveys show that working engineers' mental models are already vocabulary-neutral (e.g., that "photon" functions as a pure placeholder with no imported commitments), in which case the baggage is inert and the measure measures nothing of practical import. A third falsifier: if the critical scales derived here were shown to be so large relative to realistic experimental scales that no decision could ever be affected — though the readout-calibrated value $n^{*}_{r} \approx 53$ sits uncomfortably close to routine experiment sizes for that comfort to be assumed.

**Against ourselves.** One may argue the framework is unfalsifiable as stated because $\varepsilon_{T}$ is a free parameter; the reply is that the simulation-and-survey program fixes it, but this remains to be done. One may also argue that vocabulary problems are social, not formal, and that a divergence measure reifies a communication issue; the response is that [4] shows vocabulary-induced errors producing apparent physical paradoxes (signaling from "impossible measurements"), which is a formal, not merely social, symptom. Finally, the precedent of [7] — that direct sums can be eliminated from quantum measurement formalism — suggests vocabulary reduction is possible in principle, but does not