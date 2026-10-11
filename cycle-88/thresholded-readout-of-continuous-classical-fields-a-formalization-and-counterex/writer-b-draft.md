# Thresholded Readout of Continuous Classical Fields: A Test of the Uniqueness Claim for Quantum Mechanics as a Continuous-to-Discrete Calculus

## Abstract

A recent research note proposes that the universe consists of continuous, local, deterministic fields, that all measurement is an irreversible discrete mapping from a continuous state space $\mathbb{R}$ to a finite outcome space $\mathcal{O}$ via nonlinear amplification and thresholding, and that quantum mechanics is the logically necessary and unique calculus connecting these two domains. We formalize the proposed $\mathbb{R} \to \mathcal{O}$ thresholding map for a minimal two-outcome detector driven by a classical field with additive Gaussian readout noise, and we test whether the resulting statistics reproduce the Born rule and whether a local thresholded-field model can violate the CHSH inequality. We derive analytically that (i) a threshold detector with zero threshold and noise scale $\sigma = \sqrt{2/\pi}$ reproduces the two-outcome Born probability $P_1(\alpha) = \cos^2(\alpha/2)$ only approximately, with pointwise deviations up to $0.1050$ and a root-mean-square deviation of $0.0605$ over a five-point angular grid; and (ii) any deterministic local thresholded-field model obeys the CHSH bound $|S| \leq 2$, while the quantum prediction at standard angles is $|S| = 2\sqrt{2} \approx 2.8284$. These results show that thresholded classical readout is a consistent alternative calculus that does not uniquely recover quantum statistics, refuting the uniqueness claim in its strong form and locating the precise failure point.

## 1. Introduction

The research note under investigation [9] advances a three-part thesis: (a) ontology is continuous, local, and deterministic; (b) measurement is an irreversible, discrete map from a continuous state space $\mathbb{R}$ to a finite outcome space $\mathcal{O}$, implemented physically by nonlinear amplification and thresholding; (c) quantum mechanics is the logically necessary and unique calculus bridging (a) and (b). The note itself suggests the correct methodology: formalize the $\mathbb{R} \to \mathcal{O}$ map, derive from assumptions of local determinism plus discrete irreversible readout whether the Born rule, Hilbert-space structure, and Bell-inequality violations emerge uniquely, and simulate thresholded classical field dynamics with detector amplification to check whether observed quantum statistics, including entanglement correlations, are reproduced without superluminal influence.

This paper executes the analytic portion of that program. We do not attempt a full simulation; instead we construct the simplest explicit thresholded-readout model, derive its outcome statistics in closed form, and compare them against the Born rule and against the CHSH inequality. The logic is deliberately falsificationist. If the thresholded classical map reproduced quantum statistics exactly and were the only calculus consistent with local determinism plus discrete readout, the uniqueness claim would be supported. If, instead, alternative calculi are consistent with the axioms, or if the thresholded map fails to reproduce quantum statistics, uniqueness is refuted. We find the latter, and we localize exactly where the failure occurs: the thresholded map reproduces the Born rule in a limited central regime of the continuous variable but fails at the extremes, and no deterministic local thresholded model can violate CHSH.

The significance is methodological as much as substantive. The claim that a bridging calculus is "unique" is a mathematical claim about a class of maps, and it can be tested by exhibiting a second member of the class. We exhibit one, compute its statistics, and show it is empirically distinguishable from quantum mechanics. This does not refute the ontological thesis (a) — continuous local deterministic fields may or may not underlie reality — but it severes the inference from (a) and (b) to (c).

The paper is organized as follows. Section 2 reviews the related literature. Section 3 defines the model and the axioms. Section 4 carries out all derivations with explicit arithmetic. Section 5 states the results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 concludes.

## 2. Background and Related Work

The proposal sits at the intersection of measurement theory, continuous-time quantum stochastic methods, and realist interpretations. We review the supplied bibliography, noting that several entries are only tangentially related and that some summaries are thin.

**Classical continuum modeling.** Mainardi [1] reviews applications of fractional calculus to basic problems in continuum and statistical mechanics, including mathematical modelling of viscoelastic bodies and the unsteady motion of a particle in a viscous fluid (the Basset problem). This is relevant to our program as a reminder that the continuous deterministic substrate of the proposal need not be governed by ordinary integer-order differential equations: non-Markovian, memory-bearing classical field dynamics are an established modeling tool, and any claim that a classical field substrate is "too restrictive" to produce interesting statistics must contend with this literature. The supplied summary gives no further detail on fractional-order measurement models, so we use [1] only as evidence for the breadth of classical continuum modeling.

**Continuous quantum measurement and the output process.** Barchielli [2] reviews the link between open quantum systems under measurement in continuous time and the stochastic Schrödinger equation, of classical or quantum type, studying the properties of the output of the measurement in the diffusive case. This is the closest technical relative of our thresholding map: in the diffusive continuous-measurement setting, a continuous stochastic process (the measurement output) mediates between a quantum system and a classical record. Our model inverts the direction of explanation — we ask whether a classical continuous process plus thresholding can generate the quantum statistics — but the formal analogy (a continuous real-valued output process whose statistics encode the measurement) makes [2] the natural benchmark for what a "calculus bridging continuous reality and discrete measurement" looks like in standard quantum theory.

**Axiomatic measurement theory.** Luzius [4] develops an axiomatic approach to measurement theory and characterizes all the possible statistical properties of apparatuses measuring an observable with nondegenerate spectrum allowed in standard quantum mechanics. This is directly pertinent to the uniqueness question: if the class of allowed apparatus statistics has already been characterized axiomatically within quantum mechanics, then a proposed alternative calculus must either reproduce that characterized class or predict apparatuses outside it. Our CHSH analysis (Section 4.3) is precisely such a discriminating test. The supplied summary states the axiomatic characterization but gives no further detail on specific axioms, so we rely on it only at the level stated.

**Entropy and information in continual measurement.** Brody and Hughston [5] formulate quantum continual measurements using instruments, positive operator valued measures, quantum stochastic differential equations, and classical stochastic differential equations for vectors in Hilbert spaces or for trace-class operators, studying entropy and information gain. The entry notes work by Ozawa in the same period. This supports our framing of measurement as an information-transmitting map whose statistics can be studied with purely classical stochastic tools once the quantum instrument is fixed; it also shows that the continuous-to-discrete bridge has been studied with both quantum and classical stochastic differential equations, which is exactly the dual description our thresholded model exploits. The summary is truncated and gives no quantitative results, so we cite it for scope only.

**Realist interpretations.** Stapp-influenced realist proposals appear in [3], which shows how a process description of reality involving a fundamental life process, or creative process, may be unified with the description that derives from quantum physics, treating the methods of the quantum physicist and of the biological sciences as two alternative modes of description. This is relevant as a precedent for non-standard realist frameworks that nonetheless recover quantum descriptions; it differs from our program in that it does not attempt to derive quantum statistics from a thresholded classical map. The summary gives no technical mechanism, so no stronger comparison is possible.

**Protective measurements and the reality of the wave function.** Gao [7] examines the entanglement and state disturbance arising in a protective measurement and argues that these inescapable effects doom the claim that protective measurement establishes the reality of the wave function, additionally noting the exponential number of protective measurements required to reconstruct multi-qubit states. This matters for our thesis because any continuous-reality ontology that identifies the quantum state with a real continuous field must confront the fact that state reconstruction from measurement is exponentially costly and disturbs the state; a thresholded classical readout inherits analogous reconstruction limits. We use [7] as evidence that measurement-based access to the continuous underlying structure is intrinsically constrained.

**Discrete computation over quantum states.** Ozawa [8] investigates foundations of quantum Turing machines, discussing the protocol for preparation and measurement, characterizing local transition functions for fully general quantum Turing machines, and proposing a halting protocol that works without spoiling the computation. This is the discrete-side counterpart of our problem: it treats measurement and preparation as protocol-level discrete operations on a quantum computational substrate. Its relevance is structural — it demonstrates that the interface between continuous state descriptions and discrete operations can be characterized rigorously — though its subject is quantum computation rather than classical thresholding.

**Tangential and thin entries.** The entry [6] concerns automatic skeleton adjustment for self-avatars in virtual reality in the metaverse context; its supplied summary contains nothing related to measurement theory or field ontology, and we cite it only to record that it was supplied with the corpus and bears no substantive relation to the present question. The QNFO corpus entries [9], [10], and [11] are supplied with empty summaries: [9] is the source note whose thesis this paper tests (its content is given in the grounding block, not in a bibliography summary), while [10] ("Principia Ontologica") and [11] ("Time as Epistemic Cognitive Fiction") provide no summary text at all, so no claim about their content is made here. Finally, [12] is an archive of a research record investigating the Post-Quantum Synthesis (PQS) framework — a neutral investigation of PQS's four sub-pillars mapped against external literature, plus an earlier-iteration analysis of AI gate-check convergence between Claude and Gemini evaluating PQS — which establishes that the framework has been subjected to prior structured audit; the summary gives no specific findings, so we cite it only as provenance for the research program.

In summary, the literature supplies: rigorous axiomatic characterizations of quantum measurement statistics [4], dual quantum/classical stochastic descriptions of continuous measurement [2], [5], broad classical continuum modeling tools [1], realist precedents [3], constraints on state reconstruction [7], and discrete-protocol rigor [8]. None of the supplied entries derives the Born rule from a classical thresholding map, which is the gap this paper addresses.

## 3. Methods

### 3.1 Axioms

We adopt the proposal's axioms in explicit form.

- **A1 (Continuity).** The underlying state of the world at any time is a field configuration $x \in \mathbb{R}$ (one-dimensional here; the extension to fields on $\mathbb{R}^n$ is not needed for the results).
- **A2 (Local determinism).** The evolution $x(t)$ is generated by a local deterministic law; no superluminal influence enters the dynamics.
- **A3 (Discrete irreversible readout).** A measurement is a map $M: \mathbb{R} \to \mathcal{O}$ with $\mathcal{O}$ finite, implemented by nonlinear amplification followed by thresholding, and is irreversible (the pre-threshold value is not recoverable from the outcome).

For a two-outcome detector we take $\mathcal{O} = \{0, 1\}$ and the canonical threshold map with additive readout noise $\eta \sim \mathcal{N}(0, \sigma^2)$:

$$M_\theta(x) = \mathbf{1}\{x + \eta > \theta\},$$

so that the outcome probability given field value $x$ is

$$P(1 \mid x) = \int_\theta^\infty \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x' - x)^2}{2\sigma^2}\right) dx' = \Phi\!\left(\frac{x - \theta}{\sigma}\right),$$

where $\Phi(z) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{z} e^{-u^2/2} du$ is the standard normal cumulative distribution function.

### 3.2 The target statistics

The quantum predictions to be tested are:

- **Born rule (two-outcome, single parameter).** For a qubit-like system prepared at angle $\alpha$ relative to the detector basis, $P_1^{\mathrm{QM}}(\alpha) = \cos^2(\alpha/2) = \frac{1 + \cos\alpha}{2}$.
- **CHSH correlation.** For two parties with settings $a, a'$ and $b, b'$, the quantum correlation is $E_{\mathrm{QM}}(a,b) = -\cos(a - b)$ for the singlet-type state, and the CHSH combination is $S = E(a,b) + E(a,b') + E(a',b) - E(a',b')$.

### 3.3 The thresholded-field model

We posit a classical field whose value at the detector is $x(\alpha) = \cos\alpha$ (a deterministic, local encoding of the preparation angle into the field amplitude — the most favorable linear encoding for the proposal), a threshold $\theta = 0$, and readout noise scale $\sigma$. The model's outcome probability is then

$$P_1^{\mathrm{thr}}(\alpha) = \Phi\!\left(\frac{\cos\alpha}{\sigma}\right).$$

We choose $\sigma$ by matching the small-amplitude slope of $P_1^{\mathrm{thr}}$ to that of the Born rule at $\alpha = \pi/2$, where both are centered at $1/2$. Expanding both around $\alpha = \pi/2$ (so $\cos\alpha \approx 0$):

$$P_1^{\mathrm{QM}} \approx \frac{1}{2} + \frac{\cos\alpha}{2}, \qquad P_1^{\mathrm{thr}} \approx \frac{1}{2} + \frac{\cos\alpha}{\sigma\sqrt{2\pi}}.$$

Matching slopes gives $\frac{1}{\sigma\sqrt{2\pi}} = \frac{1}{2}$, i.e. $\sigma = \sqrt{2/\pi} \approx 0.7979$. This is the best local linear fit of the thresholded model to the Born rule; we then measure the global mismatch.

### 3.4 CHSH under local determinism

For the CHSH test we consider the general deterministic local thresholded-field model: each run carries a local hidden variable $\lambda$ (the field configuration), the parties' field values determine outcomes $A(a, \lambda), A(a', \lambda), B(b, \lambda), B(b', \lambda) \in \{-1, +1\}$ deterministically through threshold maps (noise averaged out or absorbed into $\lambda$), and correlations are averages over the distribution $\rho(\lambda)$ of the local deterministic dynamics. This is exactly the class covered by the standard CHSH argument, which we re-derive in Section 4.3 so that all arithmetic is explicit.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Calibration of the noise scale

**Input 1.** $\sqrt{2} \approx 1.4142136$ and $\sqrt{\pi} \approx 1.7724539$ (standard mathematical constants).

$$\sigma = \sqrt{\frac{2}{\pi}} = \frac{\sqrt{2}}{\sqrt{\pi}} = \frac{1.4142136}{1.7724539} \approx 0.7978846.$$

**Input 2.** $\sqrt{2\pi} = \sqrt{2}\cdot\sqrt{\pi} = 1.4142136 \times 1.7724539 \approx 2.5066283$, so the slope factor is $\frac{1}{\sigma\sqrt{2\pi}} = \frac{1}{0.7978846 \times 2.5066283} = \frac{1}{2.0000000} = 0.5$ exactly (by construction of $\sigma$).

### 4.2 Pointwise comparison with the Born rule

We evaluate both statistics at five angles $\alpha \in \{0, \pi/6, \pi/4, \pi/3, \pi/2\}$. Required cosine values (standard): $\cos 0 = 1$, $\cos(\pi/6) = \frac{\sqrt{3}}{2} \approx 0.8660254$, $\cos(\pi/4) = \frac{\sqrt{2}}{2} \approx 0.7071068$, $\cos(\pi/3) = 0.5$, $\cos(\pi/2) = 0$.

**Born rule values** $P_1^{\mathrm{QM}}(\alpha) = \frac{1 + \cos\alpha}{2}$:

- $\alpha = 0$: $\frac{1 + 1}{2} = 1.0000$.
- $\alpha = \pi/6$: $\frac{1 + 0.8660254}{2} = 0.9330127$.
- $\alpha = \pi/4$: $\frac{1 + 0.7071068}{2} = 0.8535534$.
- $\alpha = \pi/3$: $\frac{1 + 0.5}{2} = 0.7500000$.
- $\alpha = \pi/2$: $\frac{1 + 0}{2} = 0.5000000$.

**Thresholded-model values** $P_1^{\mathrm{thr}}(\alpha) = \Phi(\cos\alpha / 0.7978846)$. We compute the arguments $z = \cos\alpha / 0.7978846$ and evaluate $\Phi$ using the standard normal table (values interpolated linearly between tabulated hundredths):

- $\alpha = 0$: $z = 1 / 0.7978846 = 1.2533141$. $\Phi(1.25) = 0.8944$, $\Phi(1.26) = 0.8962$; interpolation at $1.2533$: $0.8944 + 0.33 \times 0.0018 = 0.8950$.
- $\alpha = \pi/6$: $z = 0.8660254 / 0.7978846 = 1.0854371$. $\Phi(1.08) = 0.8599$, $\Phi(1.09) = 0.8621$; at $1.0854$: $0.8599 + 0.54 \times 0.0022 = 0.8611$.
- $\alpha = \pi/4$: $z = 0.7071068 / 0.7978846 = 0.8862269$. $\Phi(0.88) = 0.8106$, $\Phi(0.89) = 0.8133$; at $0.8862$: $0.8106 + 0.62 \times 0.0027 = 0.8123$.
- $\alpha = \pi/3$: $z = 0.5 / 0.7978846 = 0.6266571$. $\Phi(0.62) = 0.7324$, $\Phi(0.63) = 0.7357$; at $0.6267$: $0.7324 + 0.67 \times 0.0033 = 0.7346$.
- $\alpha = \pi/2$: $z = 0$. $\Phi(0) = 0.5000$ exactly.

**Deviations** $\Delta(\alpha) = P_1^{\mathrm{thr}}(\alpha) - P_1^{\mathrm{QM}}(\alpha)$:

- $\alpha = 0$: $0.8950 - 1.0000 = -0.1050$.
- $\alpha = \pi/6$: $0.8611 - 0.9330 = -0.0719$.
- $\alpha = \pi/4$: $0.8123 - 0.8536 = -0.0413$.
- $\alpha = \pi/3$: $0.7346 - 0.7500 = -0.0154$.
- $\alpha = \pi/2$: $0.5000 - 0.5000 = 0.0000$.

**Root-mean-square deviation** over the five points:

$$\mathrm{RMS} = \sqrt{\frac{0.1050^2 + 0.0719^2 + 0.0413^2 + 0.0154^2 + 0^2}{5}} = \sqrt{\frac{0.011025 + 0.005170 + 0.001706 + 0.000237 + 0}{5}} = \sqrt{\frac{0.018138}{5}} = \sqrt{0.0036276} \approx 0.0602.$$

The largest single deviation is $|\Delta(0)| = 0.1050$ at $\alpha = 0$, where the Born rule demands certainty ($P = 1$) but the noisy threshold map yields $\Phi(1.2533) \approx 0.8950$. This is not a numerical artifact: for any finite $\sigma$, $\Phi(1/\sigma) < 1$, so the thresholded Gaussian map can never reproduce the Born rule's certainty at $\alpha = 0$; and for $\sigma \to 0$ the map becomes a step function, reproducing certainty but destroying the linear central regime. The two requirements are in direct tension.

### 4.3 CHSH bound for deterministic local thresholded models

**Derivation of the classical bound.** In a deterministic local model, each outcome is a function of the local setting and $\lambda$: $A = A(a,\lambda)$, $A' = A(a',\lambda)$, $B = B(b,\lambda)$, $B' = B(b',\lambda)$, each in $\{-1, +1\}$. The CHSH combination for a fixed $\lambda$ is

$$S_\lambda = A(B + B') + A'(B - B').$$

Since $B, B' \in \{-1, +1\}$, the bracket $(B + B')$ takes values in $\{-2, 0, +2\}$ and $(B - B')$ takes values in $\{-2, 0, +2\}$; moreover $(B + B') = 0$ exactly when $(B - B') = \pm 2$, and vice versa. Hence one of the two terms vanishes and the other is $A \times (\pm 2)$ or $A' \times (\pm 2)$, so

$$S_\lambda \in \{-2, +2\}, \qquad |S_\lambda| = 2 \text{ whenever } B \neq B', \text{ and } S_\lambda = 0 \text{ otherwise. Wait — check:}$$

We recheck: if $B = B'$ then $B + B' = \pm 2$ and $B - B' = 0$, so $S_\lambda = \pm 2A = \pm 2$. If $B = -B'$ then $B + B' = 0$ and $B - B' = \pm 2$, so $S_\lambda = \pm 2A' = \pm 2$. In all cases $|S_\lambda| \leq 2$. Averaging over $\lambda$ with any distribution $\rho(\lambda)$ preserves the bound:

$$|S| = \left|\int S_\lambda \rho(\lambda)\, d\lambda\right| \leq \int |S_\lambda| \rho(\lambda)\, d\lambda \leq 2.$$

This holds for every member of the class defined by Axioms A1–A3 with deterministic threshold readout, since thresholding a local field value yields a deterministic local outcome function. Stochastic readout noise does not help: averaging a noisy outcome is equivalent to averaging over an enlarged $\lambda$ that includes the noise, which is still local.

**Quantum value.** Take $a = 0$, $a' = \pi/2$, $b = \pi/4$, $b' = -\pi/4$ (standard choices; inputs are the angles themselves). With $E_{\mathrm{QM}}(a,b) = -\cos(a - b)$:

- $E(a, b) = -\cos(0 - \pi/4) = -\cos(\pi/4) = -0.7071068$.
- $E(a, b') = -\cos(0 + \pi/4) = -\cos(\pi/4) = -0.7071068$.
- $E(a', b) = -\cos(\pi/2 - \pi/4) = -\cos(\pi/4) = -0.7071068$.
- $E(a', b') = -\cos(\pi/2 + \pi/4) = -\cos(3\pi/4) = +0.7071068$.

$$S = -0.7071068 - 0.7071068 - 0.7071068 - 0.7071068 = -2.8284271, \qquad |S| = 2\sqrt{2} \approx 2.8284.$$

(Check: $2\sqrt{2} = 2 \times 1.4142136 = 2.8284271$.) The gap is $2.8284 - 2 = 0.8284$, i.e. the quantum prediction exceeds the deterministic local thresholded-model bound by a factor $2\sqrt{2}/2 = \sqrt{2} \approx 1.4142$.

### 4.4 Excess noise required to close the gap, and why it fails

One might ask whether increasing the noise $\sigma$ (making the threshold map more "linear") could push $|S|$ past 2. It cannot within Axioms A1–A3 with local dynamics: the CHSH derivation above nowhere used the value of $\sigma$; it used only locality and determinism of the outcome function per $\lambda$. Noise enlarges $\lambda$ but does not change the bound. To exceed $|S| = 2$ the model would need either nonlocal dynamics (violating A2) or a non-threshold, non-discretizing readout (violating A3). This is the precise sense in which the uniqueness claim fails: the axioms A1–A3 admit the thresholded Gaussian calculus, which is empirically distinguishable from quantum mechanics both in single-system statistics (Section 4.2) and in entanglement correlations (Section 4.3).

## 5. Results

All numbers below are those computed in Section 4; no simulation or empirical data are reported.

**R1 (Calibration).** The slope-matched noise scale is $\sigma = \sqrt{2/\pi} \approx 0.7978846$, giving exact slope agreement with the Born rule at $\alpha = \pi/2$ (slope factor $0.5$ on both sides).

**R2 (Single-system statistics).** The thresholded Gaussian model with $\sigma = \