# The Base State Hypothesis: A Falsification Protocol for Instantiating a Substrate Capable of Hosting the Standard Model

## Abstract

We formalize the question raised by the re-entry of DOI 10.5281/zenodo.18515457: can a single, explicitly constructible quantum object — a "Base State" — serve as a substrate on which the structure of the Standard Model could be hosted? We give the hypothesis a precise, testable form. A Base State is defined as a normalized state vector (or density operator) in a finite-dimensional Hilbert space together with a declared readout map, such that every empirically accessible structure is obtained by measurement, state preparation, and composition rather than by postulating particles ab initio. We then ask what present quantum platforms could host such an object. Using the published fidelities of the Tianyan-287 superconducting processor (105 qubits; single-qubit gates 99.90%, two-qubit gates 99.56%, readout 98.7%), we derive an explicit circuit-fidelity budget: a representative circuit using all 105 qubits with 100 two-qubit gates is limited by readout alone to a fidelity of approximately $0.253$, and the full budget yields $F_{\mathrm{circ}} \approx 0.147$. We further show that a generic state on 105 qubits requires $2^{106} - 2 \approx 8.11 \times 10^{31}$ real parameters to specify, while only $105$ bits are needed to index a computational basis state — a compression gap that motivates structured, design-like state families. We propose a three-stage falsification protocol and argue that the Base State hypothesis is currently unfalsified but unconfirmed: no existing platform can prepare and verify a candidate at scale.

## 1. Introduction

The re-entry question attached to DOI 10.5281/zenodo.18515457 asks whether one can instantiate a "Base State" capable of hosting the Standard Model. The question is deliberately ontological rather than computational: instead of asking whether quantum computers can simulate known physics, it asks whether a single quantum object — prepared, verified, and composed — could be the primitive from which field-theoretic structure emerges. The companion literature in the QNFO corpus frames this as a reaction against "particle ontology" projected onto relational, field-theoretic reality [10], and the Manifesto for Honest Computation demands that any such proposal come with a concrete portfolio and a falsification pledge [12].

This paper does three things. First, it gives the Base State hypothesis a definition precise enough to be wrong: Section 3 states exactly what object counts as a Base State and what would count as hosting. Second, it performs an honest feasibility audit using only numbers that are publicly supplied in the grounding material — the fidelities of the Tianyan-287 processor [2] — to determine whether current hardware could even prepare and verify a candidate Base State at the 100-qubit scale. Third, it proposes a falsification protocol in the spirit of the automata-learning literature, where a model is recovered from noisy, incomplete data by evidence-driven merging rather than by optimizing a numeric target [1].

Our conclusions are negative in the short term and constructive in the long term. The parameter-counting and fidelity analyses of Section 4 show that (i) a generic 105-qubit state is unspecifiable in any practical sense, so a viable Base State must be highly structured, and (ii) current readout fidelity alone caps whole-register verification fidelity near $0.25$, so no candidate can today be certified on a full superconducting register of this size. The hypothesis therefore survives as an open research program, not a result.

## 2. Background and Related Work

We review the twelve supplied works and their bearing on the Base State question.

[1] presents an interactive version of an evidence-driven state-merging (EDSM) algorithm for learning variants of finite state automata, where learning amounts to recovering or reverse-engineering the model generating noisy, incomplete, or imperfectly sampled data, with domain expertise injected by a human in the loop. This is directly relevant methodologically: inferring a Base State from measurement data is a model-recovery problem under noise, not a numeric optimization, and the EDSM pattern — merge states when evidence supports it, consult an oracle when it does not — is a template for how a candidate Base State's equivalence classes of measurement outcomes could be inferred.

[2] describes the Tianyan Quantum Cloud Platform, offering cloud services demonstrating quantum advantage capabilities with a Zuchongzhi 3.0-like superconducting processor; the cloud-accessible prototype Tianyan-287 features 105 qubits with single-qubit gate, two-qubit gate, and readout fidelities of 99.90%, 99.56%, and 98.7%, respectively. These are the only hardware performance numbers supplied in our grounding material, and Section 4 uses them as the quantitative basis of the feasibility audit.

[3] reviews and compares Bell-state measurement and quantum teleportation schemes using linear optics with three resource types — two-photon pairs, entangled coherent states, and hybrid entangled states — and reports that perfect teleportation with linear optics is possible in principle based on a hybrid approach combining two-photon pairs and entangled coherent states. For the Base State program this matters because teleportation is the minimal operation by which a state prepared in one physical substrate could be transferred into another; the existence of in-principle perfect transfer with hybrid resources suggests that substrate-independence of a Base State is not obviously blocked at the level of principle.

[4] discusses coherent states from three perspectives — Schroedinger's seminal approach, the experimental take of quantum optics, and theoretical developments in quantum gravity — as a comparative study intended to connect the approaches and serve pedagogical purposes. The relevance is conceptual: a Base State candidate must be a state that is robust, classical-like in its stability, and yet capable of supporting rich structure, which is precisely the role coherent states have played across these three literatures.

[5] proposes a non-variational, full circuit-based quantum algorithm for obtaining excited states in quantum chemistry, noting that excited-state determination plays a crucial role in predicting and modeling chemical reactions and other physical processes beyond widely studied ground-state problems. This supplies the constructive counterpart to our audit: if a Base State is to host dynamics, the machinery for accessing excitations above it must be circuit-native rather than variational, and [5] demonstrates that such machinery is an active object of design.

[6] investigates possibilities for generating nonclassical states — entangled, steered, and other nonclassical states — in a physical system composed of light and a semiconductor, motivated by the observation that solid-state quantum computing proposals are extremely promising for room-temperature machines and would require in-built sources of nonclassical states. This addresses the preparation side of the Base State problem: the substrate must contain its own sources of the nonclassical states the program needs, not import them.

[7] studies quantum state designs — structures enabling efficient sampling of random quantum states, with applications from circuit design to black hole physics — and the open question of how symmetry, which is expected to reduce the randomness of a state, affects state designs. This is the closest technical analogue to our compression-gap argument in Section 4: a hostable Base State cannot be Haar-generic and must live in a symmetry-constrained, design-like family, and [7] confirms that the interplay of symmetry and design structure is an open research question rather than settled technology.

[8] extends nonlocal games, in the flavour of categorical quantum mechanics, to allow quantum questions and answers using quantum sets (special symmetric dagger Frobenius algebras) and the quantum functions of Musto, Reutter, and Verdon, with equations presented in a diagrammatic calculus for tensor categories. This supplies the compositional language in which a Base State and its admissible interactions could be stated without committing to a particle ontology: algebras and morphisms, not particles.

[9] (QNFO: Standard Model, DOI 10.5281/zenodo.17210901) is supplied in the bibliography with no summary text; the entry as given provides only its title and identifier, and no further detail. We therefore use it only as the declared reference object for "the Standard Model" as the target structure to be hosted.

[10] (QNFO: Beyond the Qubit, DOI 10.5281/zenodo.22753022) is the companion paper to "The Qubit Delusion" (v1.1, 10.5281/zenodo.21254143); its supplied summary states that it asks what comes next if the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto relational, field-theoretic reality — and that it strips quantum mechanics to its minimal ontological commitments. The Base State hypothesis of this paper is precisely an attempt to answer that "what comes next" question in a falsifiable form.

[11] (QNFO: EMERGENT CORRELATION IN A LOCAL-DETERMINISTIC UNIVERSE, DOI 10.5281/zenodo.18015329) is likewise supplied with no summary text; only the title and identifier are available, and we rely on it only as a declared position in the emergence-of-correlation debate, without attributing any specific result to it.

[12] (QNFO: Manifesto for Honest Computation, DOI 10.5281/zenodo.21299278) is described as Phase VI (Final Synthesis), containing 5 principles, a concrete portfolio, and the Falsification Pledge. This paper adopts that methodological stance: every claim below is either derived with shown arithmetic or explicitly labeled as a projection with stated assumptions, and Section 6 states what would falsify the program.

## 3. Methods

### 3.1 Definition of a Base State

Let $\mathcal{H}_N$ be a Hilbert space of dimension $D_N = 2^N$, spanned by a declared computational basis $\{|b\rangle\}_{b \in \{0,1\}^N}$. A **Base State candidate** is a pair

$$
\mathcal{B} = \left( |\psi_0\rangle \in \mathcal{H}_N,\; \mathcal{R}: \mathcal{H}_N \rightarrow \{0,1\}^N \right),
$$

where $|\psi_0\rangle$ is a normalized state vector (or, in the mixed generalization, a density operator $\rho_0$ with $\mathrm{Tr}(\rho_0) = 1$) and $\mathcal{R}$ is a declared readout map. We say $\mathcal{B}$ **hosts** a target structure $\mathcal{T}$ (here, nominally, the Standard Model, per [9]) if:

1. **Preparation**: $|\psi_0\rangle$ is preparable from a product initial state by a circuit of finite, stated depth.
2. **Verifiability**: there exists a measurement statistics test whose pass probability, under the hypothesis that the prepared state is $|\psi_0\rangle$, exceeds a declared threshold $\theta$, and whose pass probability under every state in a declared alternative set is below $\theta$.
3. **Compositional productivity**: admissible operations on $\mathcal{B}$ form a closed algebraic structure (in the categorical sense of objects and morphisms, as in [8]) rich enough to encode the interaction pattern of $\mathcal{T}$.

Condition 3 is deliberately left programmatic; conditions 1 and 2 are auditable with hardware numbers, and Section 4 audits them.

### 3.2 Audit quantities

For a platform with single-qubit gate fidelity $F_1$, two-qubit gate fidelity $F_2$, and readout fidelity $F_r$ (all as reported in [2] for Tianyan-287), we model a circuit with $n_1$ single-qubit gates, $n_2$ two-qubit gates, and $n_r$ readout events by the independent-error product

$$
F_{\mathrm{circ}}(n_1, n_2, n_r) \;=\; F_1^{\,n_1} \, F_2^{\,n_2} \, F_r^{\,n_r},
$$

or, in log form,

$$
\ln F_{\mathrm{circ}} \;=\; n_1 \ln F_1 + n_2 \ln F_2 + n_r \ln F_r.
$$

This is a first-order model: it assumes errors are independent and multiplicative and ignores crosstalk, leakage, and correlated decay. It is the standard budgeting convention and is conservative for our purposes because it can only overestimate fidelity when correlations are harmful.

### 3.3 Specifiability accounting

A pure state $|\psi\rangle \in \mathcal{H}_N$ is specified, up to normalization and global phase, by $2 D_N - 2$ real numbers: $D_N$ complex amplitudes contribute $2 D_N$ real numbers, normalization removes $1$, and the global phase removes $1$ more. We compare this against the $\log_2 D_N = N$ bits needed to index a single computational basis state, and against the design-family picture of [7], in which one samples structured states efficiently rather than writing them out.

### 3.4 Falsification protocol

Following the model-recovery stance of [1] and the Falsification Pledge of [12], the protocol is:

- **Stage P (Preparation)**: prepare a candidate $|\psi_0\rangle$ on the full register; record circuit depth and gate counts.
- **Stage V (Verification)**: run a statistics test with threshold $\theta = 0.5$; the candidate fails if the achievable $F_{\mathrm{circ}}$ budget falls below $\theta$.
- **Stage C (Composition)**: demonstrate one nontrivial closed composition (e.g., a teleportation-grade transfer as in [3]) out of the Base State.

## 4. Analysis

All hardware inputs in this section come from [2]: $N = 105$ qubits; $F_1 = 0.9990$; $F_2 = 0.9956$; $F_r = 0.987$. All other quantities are derived below with full arithmetic.

### 4.1 Hilbert space dimension and parameter count

Input: $N = 105$ [2]. Then

$$
D_{105} = 2^{105} = 2^{100} \cdot 2^{5} = 1.2676506 \times 10^{30} \times 32 = 4.0564819 \times 10^{31}.
$$

The number of real parameters needed to specify a generic pure state (Section 3.3) is

$$
2 D_{105} - 2 = 2^{106} - 2 = 8.1129638 \times 10^{31} - 2 \approx 8.113 \times 10^{31}.
$$

Per qubit, this is

$$
\frac{2^{106} - 2}{105} = \frac{8.1129638 \times 10^{31}}{105} \approx 7.727 \times 10^{29}
$$

real numbers per qubit of register. By contrast, indexing one computational basis state costs $\log_2 D_{105} = 105$ bits. The compression ratio between generic-state specification and basis indexing is

$$
\frac{2^{106} - 2}{105} \approx 7.727 \times 10^{29}.
$$

**Interpretation**: a Base State that is Haar-generic is unspecifiable by roughly thirty orders of magnitude. Any viable candidate must therefore belong to a structured, efficiently parameterized family — exactly the regime that quantum state designs address [7], and exactly where the effect of symmetry on such families remains, per [7], an open question.

### 4.2 Per-gate error budget

From [2]:

$$
\epsilon_1 = 1 - F_1 = 1 - 0.9990 = 1.0 \times 10^{-3},
$$
$$
\epsilon_2 = 1 - F_2 = 1 - 0.9956 = 4.4 \times 10^{-3},
$$
$$
\epsilon_r = 1 - F_r = 1 - 0.987 = 1.3 \times 10^{-2}.
$$

Log-fidelities (natural log):

$$
\ln F_1 = \ln(0.9990) \approx -1.0005 \times 10^{-3},
$$
$$
\ln F_2 = \ln(0.9956) \approx -4.4097 \times 10^{-3},
$$
$$
\ln F_r = \ln(0.987) \approx -1.30816 \times 10^{-2}.
$$

### 4.3 Readout-only ceiling for full-register verification

Any verification protocol that reads out all $N = 105$ qubits incurs at least $n_r = 105$ readout events. With no other operations ($n_1 = n_2 = 0$):

$$
\ln F_{\mathrm{ro}} = 105 \times (-1.30816 \times 10^{-2}) = -1.37357,
$$
$$
F_{\mathrm{ro}} = e^{-1.37357} \approx 0.2532.
$$

**Result**: readout alone caps full-register verification fidelity at approximately $0.253$, far below the Stage V threshold $\theta = 0.5$. No candidate Base State on this platform can be verified on the full register at $\theta = 0.5$, regardless of how good the gates are. This is a structural bottleneck, not a gate-quality one.

### 4.4 Representative full-register circuit

Consider a representative preparation circuit using all 105 qubits with $n_1 = 105$ single-qubit gates, $n_2 = 100$ two-qubit gates, and $n_r = 105$ readouts. Then

$$
\ln F_{\mathrm{circ}} = 105(-1.0005 \times 10^{-3}) + 100(-4.4097 \times 10^{-3}) + 105(-1.30816 \times 10^{-2}).
$$

Term by term:

$$
105 \times (-1.0005 \times 10^{-3}) = -0.10505,
$$
$$
100 \times (-4.4097 \times 10^{-3}) = -0.44097,
$$
$$
105 \times (-1.30816 \times 10^{-2}) = -1.37357.
$$

Sum:

$$
\ln F_{\mathrm{circ}} = -0.10505 - 0.44097 - 1.37357 = -1.91959,
$$
$$
F_{\mathrm{circ}} = e^{-1.91959} \approx 0.1467.
$$

Decomposing the contributions as fidelity factors:

- single-qubit gates alone: $e^{-0.10505} \approx 0.9003$;
- two-qubit gates alone: $e^{-0.44097} \approx 0.6434$;
- readout alone: $e^{-1.37357} \approx 0.2532$ (Section 4.3).

The product $0.9003 \times 0.6434 \times 0.2532 \approx 0.1467$ confirms the log-domain computation.

### 4.5 Gate-budget headroom under ideal readout

To ask how large a circuit the gates alone could support at $\theta = 0.5$, set $n_r = 0$ and $n_1 = n_2 = n$, and solve

$$
n \left( \ln F_1 + \ln F_2 \right) = \ln 0.5 = -0.69315.
$$

Since $\ln F_1 + \ln F_2 = -1.0005 \times 10^{-3} - 4.4097 \times 10^{-3} = -5.4102 \times 10^{-3}$,

$$
n = \frac{-0.69315}{-5.4102 \times 10^{-3}} \approx 128.1,
$$

so approximately $n = 128$ layers, each containing one single-qubit and one two-qubit gate per active qubit pair, could be tolerated at $\theta = 0.5$ if readout were perfect. Restoring real readout ($n_r = 105$) consumes $\ln$-budget $1.37357$, which already exceeds the total budget $0.69315$ by a factor

$$
\frac{1.37357}{0.69315} \approx 1.982,
$$

i.e., readout alone uses about $1.98$ times the entire $\theta = 0.5$ budget. This quantifies the bottleneck of Section 4.3.

### 4.6 Projection: required readout fidelity

**Projection** (labeled as such; assumptions: $n_1 = 105$, $n_2 = 100$, $n_r = 105$, $F_1$ and $F_2$ as in [2], target $\theta = 0.5$). The required readout fidelity $F_r^{*}$ satisfies

$$
\ln F_r^{*} = \frac{\ln 0.5 - \ln F_1^{105} - \ln F_2^{100}}{105} = \frac{-0.69315 + 0.10505 + 0.44097}{105} = \frac{-0.14713}{105} = -1.4012 \times 10^{-3},
$$

$$
F_r^{*} = e^{-1.4012 \times 10^{-3}} \approx 0.99860.
$$

So full-register verification at $\theta = 0.5$ for this circuit class requires readout fidelity $\approx 0.9986$, versus the supplied $0.987$ [2] — an improvement of $1.16 \times 10^{-2}$ in error terms ($1.3 \times 10^{-2} \rightarrow 1.4 \times 10^{-3}$, a reduction by a factor of $\frac{1.3 \times 10^{-2}}{1.4 \times 10^{-3}} \approx 9.3$). Uncertainty: this projection inherits the independence assumption of Section 3.2; correlated errors would only lower the achievable fidelity, so $0.9986$ is a best-case requirement.

## 5. Results

All numbers below are computed in Section 4 from the inputs of [2]; the single projection is labeled.

1. **Dimension and specifiability.** $D_{105} = 2^{105} \approx 4.056 \times 10^{31}$; a generic pure state requires $2^{106} - 2 \approx 8.113 \times 10^{31}$ real parameters, i.e., $\approx 7.727 \times 10^{29}$ real numbers per qubit, versus $105$ bits to index a basis state (Section 4.1). Consequently, any hostable Base State must be a structured, design-like state, not a generic state.
2. **Per-gate errors.** $\epsilon_1 = 1.0 \times 10^{-3}$, $\epsilon_2 = 4.4 \times 10^{-3}$, $\epsilon_r = 1.3 \times 10^{-2}$ (Section 4.2).
3. **Readout ceiling.** Full-register readout of 105 qubits at $F_r = 0.987$ caps verification fidelity at $F_{\mathrm{ro}} \approx 0.2532$ (Section 4.3).
4. **Representative circuit.** With $n_1 = 105$, $n_2 = 100$, $n_r = 105$: $F_{\mathrm{circ}} \approx 0.1467$ (Section 4.4).
5. **Gate headroom.** With perfect readout, $\approx 128$ combined gate layers are tolerable at $\theta = 0.5$; with real readout, readout alone consumes $\approx 1.98\times$ the entire $\theta = 0.5$ budget (Section 4.5).
6. **Projection (stated assumptions of Section 4.6).** Full-register verification at $\theta = 0.5$ for this circuit class requires $F_r^{*} \approx 0.9986$, a $\approx 9.3\times$ reduction in readout error relative to the supplied value. Uncertainty: best-case under the independence model; correlated errors raise the requirement.

**Status of the hypothesis.** Under the Stage V threshold $\theta = 0.5$, no candidate Base State on a 105-qubit register of the Tianyan-287 class can currently be verified (Results 3 and 4). The Base State hypothesis is therefore unfalsified but unconfirmed: the obstruction is quantitative (fidelity budgets), not a no-go at the level of principle — in-principle perfect state transfer with hybrid linear-optic resources is reported in [3], and structured state families of the kind needed are actively studied [7].

## 6. Discussion

**Limitations of the fidelity model.** The multiplicative budget of Section 3.2 assumes independent errors. Real superconducting devices exhibit crosstalk, leakage, and correlated decay; all of these can only reduce $F_{\mathrm{circ}}$ below our values, so our numbers are upper bounds on achievable fidelity. Conversely, error correction and mitigation could beat single-shot budgets; our analysis deliberately models uncorrected circuits, and a fault-tolerant re-audit would change the conclusions quantitatively. We flag this as the largest single caveat.

**Limitations of the definition.** Condition 3 of Section 3.1 (compositional productivity) is programmatic, not operational. We have not specified a metric for "rich enough to encode the interaction pattern" of the Standard Model, and until we do, the hosting claim cannot fail at Stage C — a weakness, since an unfalsifiable condition is exactly what the Falsification Pledge of [12] forbids. A minimal fix is to require the admissible operations to reproduce a declared nonlocal-game winning behavior in the sense of [8], which would make Stage C decidable.

**What would falsify the program.** Three concrete falsifiers: (i) a proof that symmetry-constrained state families cannot support the compositional closure required at Stage C, which would break the escape from the compression gap of Section 4.1; (ii) demonstration that the readout bottleneck of Section 4.3 is physical rather than engineering-limited, i.e., that no readout scheme on any substrate can exceed the ceiling we computed relative to gate fidelities; (iii) failure of hybrid-transfer schemes of the type reviewed in [3] to preserve the structured character of a Base State across substrates, which would confine the program to a single platform.

**Against ourselves.** A skeptic may argue that the entire Base State framing is unnecessary: standard quantum simulation already hosts effective field theories on qubit registers, and the ontological critique of the qubit-gate-circuit model voiced in [10] is philosophy, not physics. Our reply is that the compression-gap result of Section 4.1 is ontology-neutral arithmetic — generic states are unspecifiable, so any working program already relies on structured state families, and making that reliance explicit is a contribution regardless of one's ontology. A second skeptic may note that our audit uses one platform's numbers [2]; this is true and unavoidable given the grounding material, and we treat the audit as a template rather than a verdict on superconducting technology generally. A third objection: the automata-learning analogy of [1] may be superficial, since physical state spaces are continuous. We concede the disanalogy but note that the EDSM pattern — merging observational equivalence classes under noisy evidence — is precisely what a statistics-based Stage V test performs on measurement outcome classes.

**Open questions.** How does symmetry constrain state-design families in the sense of [7], and can that constraint be turned into a positive parameterization for Base State candidates? Can excited-state machinery of the non-variational, circuit-native type proposed in [5] be repurposed to probe excitations above a Base State? Can in-built nonclassical state sources of the light–semiconductor type studied in [6] supply the preparation side at room temperature, as their motivation suggests? And can coherent-state intuition, spanning Schroedinger's approach, quantum optics, and quantum gravity as surveyed in [4], guide which structured families are dynamically stable enough to serve as a substrate?

## 7. Conclusion

We have converted the re-entry question of DOI 10.5281/zenodo.18515457 into a defined object, an auditable protocol, and a set of computed feasibility numbers. The arithmetic is sobering: a generic 105-qubit state requires $\approx 8.113 \times 10^{31}$ real parameters to specify; full-register verification on a Tianyan-287-class device is readout-limited to $\approx 0.253$ fidelity, and a representative full-register circuit achieves $\approx 0.147$; reaching the $\theta = 0.5$ verification threshold requires readout fidelity $\approx 0.9986$ under best-case assumptions. None of this refutes the Base State hypothesis; all of it constrains it. The viable path is structured, symmetry-aware, design-like state families [7], prepared by in-substrate sources [6], verified by statistics tests in the model-recovery spirit of [1], composed in the algebraic language of [8], and held to the falsification discipline of [12]. The program is open, and the next concrete milestone is a Stage V pass on any register, at any scale, with the budget arithmetic shown.

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
[10