# Grounding block - source: rem-26c69147-8f50-4a7d-8281-06ca84a1ed98

## Research idea

Quantum Mechanics as Unique Calculus Bridging Continuous Reality and Discrete Measurement. The note claims the universe consists of continuous, local, deterministic fields, while all measurement is an irreversible discrete mapping from a continuous state space R to a finite outcome space O via nonlinear amplification and thresholding; quantum mechanics is then posited to be the logically necessary and unique calculus connecting these two domains. A paper could test this by formalizing the R→O thresholding map and deriving, from assumptions of local determinism plus discrete irreversible readout, whether the Born rule, Hilbert-space structure, and Bell-inequality violations emerge uniquely—or whether alternative calculi are consistent, which would refute uniqueness. Simulations of thresholded field dynamics (e.g., stochastic classical field models with detector amplification) could check whether observed quantum statistics, including entanglement correlations, are reproduced without superluminal influence.

Source: owner notebook notes/v1/2026/07/24/_PQS-Full-Paper.md

## Existing paper under revision (remediation only)

# Thresholded Readout of Continuous Classical Fields: A Formalization and Counterexample to the Uniqueness Claim for Quantum Mechanics

## Abstract

A recent research note proposes that the universe consists of continuous, local, deterministic fields, that all measurement is an irreversible discrete mapping from a continuous state space $\mathbb{R}$ to a finite outcome space $\mathcal{O}$ via nonlinear amplification and thresholding, and that quantum mechanics is the logically necessary and unique calculus connecting these two domains. This paper formalizes the proposed continuous-to-discrete readout map, derives the outcome statistics it generates for a concrete two-outcome detector model, and tests the uniqueness claim. We show that within the class of thresholded amplification maps, at least two distinct readout conventions — a linear threshold and a quadratic (intensity-like) threshold — are both consistent with local deterministic continuous fields plus irreversible discrete readout, yet yield different outcome probabilities ($0.1587$ versus $0.3174$ for a unit-variance Gaussian field at threshold $\Theta = 1$). We further show that a slope-matched Gaussian threshold detector reproduces the two-outcome Born rule only approximately, with pointwise deviations up to $0.1050$ and a root-mean-square deviation of $0.0602$ over a five-point angular grid. Finally, we derive the CHSH bound $|S| \le 2$ for any factorized local deterministic readout, while the quantum prediction at standard angles is $|S| = 2\sqrt{2} \approx 2.828427$. We conclude that the uniqueness claim is refuted at the level of the readout calculus: alternative calculi are consistent with the stated ontology, and quantum statistics correspond to one member of a broader family. A projection of the number of experimental trials ($\approx 130$ per setting) needed to distinguish the two readout conventions is included.

## 1. Introduction

The research idea under investigation asserts three claims: (i) an ontological claim, that physical reality is continuous, local, and deterministic; (ii) an epistemic-operational claim, that every measurement is an irreversible discrete mapping from a continuous state space $\mathbb{R}$ to a finite outcome space $\mathcal{O}$, realized physically through nonlinear amplification and thresholding; and (iii) a meta-theoretical claim, that quantum mechanics is the logically necessary and unique calculus bridging (i) and (ii). Claims (i) and (ii) are compatible with a broad tradition of classical-field and stochastic-continuum modeling [1], and claim (ii) resonates with the axiomatic theory of measurement instruments [4] and with continuous-time measurement formulations [2], [5].

The present paper takes claims (i) and (ii) as axioms and treats claim (iii) as a falsifiable hypothesis. The strategy is direct: we formalize the readout map $M: \mathbb{R} \to \mathcal{O}$, compute the statistics it induces for a minimal detector model, and ask whether the resulting calculus is unique or whether distinct calculi within the same axiom class generate different, internally consistent statistics. If at least two distinct calculi are consistent with the axioms, uniqueness fails, and the specific form of quantum statistics must be attributed to additional structure beyond local determinism plus discrete readout.

The logic is deliberately falsificationist. If the thresholded classical map reproduced quantum statistics exactly and were the only calculus consistent with local determinism plus discrete readout, the uniqueness claim would be supported. If, instead, alternative calculi are consistent with the axioms, or if the thresholded map fails to reproduce quantum statistics, uniqueness is refuted. We find the latter, and we localize exactly where the failure occurs: the thresholded map reproduces the Born rule only in a limited central regime of the continuous variable and fails at the extremes, and no deterministic local thresholded model can violate CHSH.

The significance is methodological as much as substantive. The claim that a bridging calculus is "unique" is a mathematical claim about a class of maps, and it can be tested by exhibiting a second member of the class. We exhibit one, compute its statistics, and show it is empirically distinguishable from quantum mechanics. This does not refute the ontological thesis (i) — continuous local deterministic fields may or may not underlie reality — but it severs the inference from (i) and (ii) to (iii).

Our main results are: (a) an explicit derivation of outcome probabilities for linear versus quadratic thresholding of a Gaussian continuous field, showing a factor-of-two difference in detection probability; (b) a quantitative assessment of how well a slope-matched threshold detector approximates the Born rule; (c) a derivation of the CHSH bound $|S| \le 2$ for any factorized local readout of the proposed type; and (d) a statistical power projection for experimentally distinguishing the two readout conventions.

## 2. Background and Related Work

We discuss the eight arXiv works supplied in the bibliography, in bibliography order, followed by the four QNFO corpus items.

[1] (arXiv:1201.0863v1) reviews applications of fractional calculus to basic problems in continuum and statistical mechanics, including mathematical modelling of viscoelastic bodies and the Basset problem of unsteady particle motion in a viscous fluid. This work exemplifies the continuous-field modeling tradition within which the proposed ontology sits: continuum mechanics supplies deterministic (or statistically treated) evolution laws on continuous state spaces, and the present paper's axiom (i) inherits this modeling style. Fractional calculus itself is not used here, but the work establishes that rich, nonlocal-in-time continuous dynamics are standard equipment for classical field description. The supplied summary gives no further detail on fractional-order measurement models, so we use [1] only as evidence for the breadth of classical continuum modeling.

[2] (arXiv:1301.3626v2) reviews the link between open quantum systems under measurement in continuous time and the stochastic Schrödinger equation, of classical or quantum type, and studies the properties of the output of the measurement, restricted to the diffusive case. This is directly relevant to our formalization: the stochastic Schrödinger equation is precisely a calculus in which a continuous underlying description is connected to a discrete measurement record, and the statistics of the output spectrum are the object our thresholding map is meant to reproduce. Our model inverts the direction of explanation — we ask whether a classical continuous process plus thresholding can generate the quantum statistics — but the formal analogy makes [2] the natural benchmark for what a "calculus bridging continuous reality and discrete measurement" looks like in standard quantum theory. The entry's summary states the diffusive restriction; we therefore compare our model only to diffusive-type continuous readout.

[3] (arXiv:1610.09347v1) develops a realist interpretation in which a process description of reality, involving a fundamental life process or creative process, is unified with the description that derives from quantum physics, with the methods of the quantum physicist and of the biological sciences seen as two alternative modes of description. This supports our framing that the relationship between an underlying continuous reality and the quantum description is an interpretive question with multiple candidate answers; the entry's summary does not, however, supply technical results we can import, so we use it only as evidence that realist unification programs are an active genre.

[4] (arXiv:quant-ph/0107090v1) develops an axiomatic approach to measurement theory and characterizes all the possible statistical properties of apparatuses measuring an observable with nondegenerate spectrum allowed in standard quantum mechanics. This is the closest formal antecedent to our program: it fixes the quantum-side statistics that any candidate calculus must reproduce, and our counterexample calculus is evaluated against exactly such statistical properties. Our Section 4 shows that a thresholded classical readout can produce statistics outside this characterized set, which is the crux of the uniqueness question. The supplied summary states the axiomatic characterization but gives no further detail on specific axioms, so we rely on it only at the level stated.

[5] (arXiv:quant-ph/0012115v1) formulates quantum continual measurements using instruments, positive operator valued measures, quantum stochastic differential equations, and classical stochastic differential equations for vectors in Hilbert spaces or trace-class operators, and studies entropy and information gain; the summary also notes concurrent work by Ozawa, though the supplied text is truncated and gives no further detail on that point. The work is significant here because it demonstrates that classical SDEs for Hilbert-space objects and quantum stochastic equations are inter-derivable descriptions of the same measurement statistics — precisely the kind of bridge our paper interrogates. We use its framing of information gain qualitatively; the truncated summary prevents us from citing specific quantitative results from it.

[6] (arXiv:2307.09558v1) concerns automatic skeleton adjustment for self-avatars in virtual reality, addressing motion capture, trackers, and inverse kinematics in the metaverse context. This work is tangential to quantum foundations; we cite it only as an engineering instance of the same abstract operation our axiom (ii) posits — mapping continuous tracked signals onto a finite discrete structure (a skeleton) via a fixed nonlinear adjustment procedure. The summary supplied gives no further detail relevant to measurement theory, and we draw no foundational conclusion from it.

[7] (arXiv:1402.1217v2) examines entanglement and state disturbance arising in protective measurement and argues that these inescapable effects doom the claim that protective measurement establishes the reality of the wave function, adding that an exponential number of protective measurements would be required to reconstruct multi-qubit states. This is relevant to our ontological claim (i): it removes one route by which the wave function itself could be taken as the directly measured continuous object, reinforcing the need for an explicit readout map between whatever continuous reality is posited and the discrete record. The entry's summary is truncated, so we rely only on the stated conclusions about entanglement, disturbance, and exponential reconstruction cost.

[8] (arXiv:quant-ph/9809038v1) investigates foundations of quantum Turing machines, characterizes local transition functions for fully general quantum Turing machines, discusses preparation and measurement protocols, and proposes a halting protocol that works without spoiling the computation. The characterization of local transition functions parallels our concern with locality: a discrete, local transition structure sitting on top of a continuous or quantum substrate. The work shows that locality constraints on discrete readout and transition rules are formally tractable, which supports the well-posedness of our axiom (ii); the truncated summary prevents citation of its specific protocol details.

The QNFO corpus items [9]–[12] (POST QUANTUM SYNTHESIS; Principia Ontologica; Time as Epistemic Cognitive Fiction; and the PQS AI-Evaluation Audit) supply the provenance of the research idea: [12] is described as an archive of the research record investigating the Post-Quantum Synthesis framework, a neutral investigation of its four sub-pillars mapped against external literature, plus an earlier-iteration analysis of AI gate-check convergence between Claude and Gemini evaluating PQS. Entries [9], [10], and [11] carry no summary text in the supplied bibliography, so we cite them only as corpus context for the idea's origin and draw no substantive claims from them.

In summary, the literature supplies: rigorous axiomatic characterizations of quantum measurement statistics [4], dual quantum/classical stochastic descriptions of continuous measurement [2], [5], broad classical continuum modeling tools [1], realist precedents [3], constraints on state reconstruction [7], and discrete-protocol rigor [8]. None of the supplied entries derives the Born rule from a classical thresholding map, which is the gap this paper addresses.

## 3. Methods

### 3.1 Axioms

We adopt the proposal's axioms in explicit form.

- **A1 (Continuity).** The underlying state of the world at any time is a field configuration $x \in \mathbb{R}$ (one-dimensional here; the extension to fields on $\mathbb{R}^n$ is not needed for the results).
- **A2 (Local determinism).** The evolution $x(t)$ is generated by a local deterministic law; no superluminal influence enters the dynamics.
- **A3 (Discrete irreversible readout).** A measurement is a map $M: \mathbb{R} \to \mathcal{O}$ with $\mathcal{O}$ finite, implemented by nonlinear amplification followed by thresholding, and is irreversible (the pre-threshold value is not recoverable from the outcome).

### 3.2 The readout map

A measurement device is a triple $(\mathcal{A}, g, \Theta)$ where $\mathcal{A}$ is a nonlinear amplifier acting on a continuous field variable $x \in \mathbb{R}$, $g > 0$ is a gain parameter, and $\Theta$ is a threshold. The amplifier produces an intermediate variable

$$y = \mathcal{A}_g(x),$$

and the readout map $M_\Theta: \mathbb{R} \to \mathcal{O} = \{0, 1\}$ for a two-outcome detector is the irreversible step function

$$M_\Theta(y) = \begin{cases} 1 & \text{if } y \ge \Theta, \\ 0 & \text{if } y < \Theta. \end{cases}$$

Irreversibility enters because $M_\Theta$ is many-to-one and is not invertible on its image: the preimage of outcome $1$ is the set $M^{-1}(1) = \{x : \mathcal{A}_g(x) \ge \Theta\}$, and all continuous information within that set is discarded.

### 3.3 Candidate calculi

A "calculus" in the sense of the research idea is a rule assigning outcome probabilities $P_k$ to each outcome $k \in \mathcal{O}$ given the continuous state. We consider two members of the thresholded-amplifier family:

- **Linear calculus ($\mathcal{C}_L$):** $\mathcal{A}_g(x) = g x$, so outcome $1$ occurs when $x \ge \Theta/g$.
- **Quadratic calculus ($\mathcal{C}_Q$):** $\mathcal{A}_g(x) = g x^2$, so outcome $1$ occurs when $|x| \ge \sqrt{\Theta/g}$ (the amplifier is insensitive to sign, as intensity-like detectors are).

Both calculi satisfy the axioms exactly: the underlying field is continuous, local, and deterministic; the readout is discrete, irreversible, and produced by nonlinear amplification and thresholding. The quadratic amplifier is nonlinear in the stronger sense required by the idea's wording; the linear amplifier is the degenerate (affine) member of the family, included as the minimal baseline.

### 3.4 Field ensemble

We take the continuous field variable at the detector to be distributed, over an ensemble of nominally identical preparation runs, as a Gaussian with density

$$p(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \, e^{-x^2/(2\sigma^2)},$$

with $\sigma = 1$ in dimensionless units throughout. This is the minimal nontrivial ensemble: symmetric, continuous, and normalizable. No quantum postulate is used at this stage; $p(x)$ is simply the ensemble distribution of the classical field amplitude.

For the Born-rule comparison (Section 4.2) we additionally use the noisy threshold map with additive readout noise $\eta \sim \mathcal{N}(0, \sigma_n^2)$:

$$M_\theta(x) = \mathbf{1}\{x + \eta > \theta\}, \qquad P(1 \mid x) = \Phi\!\left(\frac{x - \theta}{\sigma_n}\right),$$

where $\Phi(z) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{z} e^{-u^2/2}\, du$ is the standard normal cumulative distribution function.

### 3.5 Target statistics and locality test

The quantum predictions to be tested are:

- **Born rule (two-outcome, single parameter).** For a qubit-like system prepared at angle $\alpha$ relative to the detector basis, $P_1^{\mathrm{QM}}(\alpha) = \cos^2(\alpha/2) = \frac{1 + \cos\alpha}{2}$.
- **CHSH correlation.** For two parties with settings $a, a'$ and $b, b'$, the quantum correlation is $E_{\mathrm{QM}}(a,b) = -\cos(a - b)$ for the singlet-type state, and the CHSH combination is $S = E(a,b) + E(a,b') + E(a',b) - E(a',b')$.

For the CHSH test we consider two spatially separated detectors each implementing a factorized readout: detector $A$ outputs $A(a, \lambda) \in \{\pm 1\}$ as a deterministic function of its local setting $a$ and the local field value $\lambda_A$, and detector $B$ outputs $B(b, \lambda) \in \{\pm 1\}$ similarly, with no dependence of $A$ on $b$ or of $B$ on $a$ (locality of the readout, inherited from axiom A2). The correlation is

$$E(a, b) = \int \rho(\lambda) \, A(a, \lambda) \, B(b, \lambda) \, d\lambda,$$

where $\rho(\lambda)$ is the distribution of the shared field configuration.

## 4. Analysis

All numbers in this section are computed explicitly from the inputs stated above. The only external inputs are the standard normal cumulative distribution values $\Phi(1) = 0.8413$ and $\Phi(2) = 0.9772$, which are tabulated values of the Gaussian integral, and the standard mathematical constants $\sqrt{2} \approx 1.4142136$ and $\sqrt{\pi} \approx 1.7724539$.

### 4.1 Outcome probability under the quadratic calculus

With gain $g = 1$ and threshold $\Theta = 1$, the quadratic calculus fires when $|x| \ge \sqrt{\Theta/g} = \sqrt{1} = 1$. The detection probability is

$$P_1^{(Q)} = \int_{-\infty}^{-1} p(x)\, dx + \int_{1}^{\infty} p(x)\, dx = 2\int_{1}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2}\, dx = 2\bigl(1 - \Phi(1)\bigr).$$

Using $\Phi(1) = 0.8413$:

$$P_1^{(Q)} = 2(1 - 0.8413) = 2 \times 0.1587 = 0.3174.$$

### 4.2 Outcome probability under the linear calculus

With the same $g = 1$, $\Theta = 1$, the linear calculus fires when $x \ge \Theta/g = 1$:

$$P_1^{(L)} = \int_{1}^{\infty} p(x)\, dx = 1 - \Phi(1) = 1 - 0.8413 = 0.1587.$$

### 4.3 Divergence between the calculi

The two calculi, both satisfying the axioms, give

$$\Delta P = P_1^{(Q)} - P_1^{(L)} = 0.3174 - 0.1587 = 0.1587,$$

a ratio

$$\frac{P_1^{(Q)}}{P_1^{(L)}} = \frac{0.3174}{0.1587} \approx 2.000.$$

The factor of $2$ is structural, not coincidental: analytically, for any symmetric density $P_1^{(Q)} = 2\bigl(1 - \Phi(\Theta/g)\bigr)$ while $P_1^{(L)} = 1 - \Phi(\Theta/g)$, so the ratio is exactly $2$ in the limit of exact tail symmetry; the rounded inputs give $0.3174/0.1587 \approx 1.9994$, which rounds to $2.000$. for a symmetric density, the quadratic threshold counts both tails while the linear threshold counts one, and at $\Theta = g$ the tail probabilities coincide. Both calculi are internally consistent, deterministic at the field level, and produce irreversible discrete records. Therefore the calculus connecting continuous reality to discrete outcomes is **not unique** within the axiom class; uniqueness fails unless an additional principle selects the amplifier.

### 4.4 Born-rule approximation by a slope-matched threshold detector

We now ask how well the best locally calibrated noisy threshold detector matches the Born rule. We posit a classical field whose value at the detector is $x(\alpha) = \cos\alpha$ (a deterministic, local encoding of the preparation angle into the field amplitude — the most favorable linear encoding for the proposal), a threshold $\theta = 0$, and readout noise scale $\sigma_n$. The model's outcome probability is

$$P_1^{\mathrm{thr}}(\alpha) = \Phi\!\left(\frac{\cos\alpha}{\sigma_n}\right).$$

We choose $\sigma_n$ by matching the small-amplitude slope of $P_1^{\mathrm{thr}}$ to that of the Born rule at $\alpha = \pi/2$, where both are centered at $1/2$. Expanding both around $\alpha = \pi/2$ (so $\cos\alpha \approx 0$):

$$P_1^{\mathrm{QM}} \approx \frac{1}{2} + \frac{\cos\alpha}{2}, \qquad P_1^{\mathrm{thr}} \approx \frac{1}{2} + \frac{\cos\alpha}{\sigma_n\sqrt{2\pi}}.$$

Matching slopes gives $\frac{1}{\sigma_n\sqrt{2\pi}} = \frac{1}{2}$, i.e.

$$\sigma_n = \sqrt{\frac{2}{\pi}} = \frac{\sqrt{2}}{\sqrt{\pi}} = \frac{1.4142136}{1.7724539} \approx 0.7978846.$$

As a check, $\sqrt{2\pi} = \sqrt{2}\cdot\sqrt{\pi} = 1.4142136 \times 1.7724539 \approx 2.5066283$, so the slope factor is $\frac{1}{\sigma_n\sqrt{2\pi}} = \frac{1}{0.7978846 \times 2.5066283} = \frac{1}{2.0000000} = 0.5$ exactly, by construction.

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

$$\mathrm{RMS} = \sqrt{\frac{0.1050^2 + 0.0719^2 + 0.0413^2 + 0.0154^2 + 0^2}{5}} = \sqrt{\frac{0.0181375}{5}} = \sqrt{0.0036275} \approx 0.0602.$$

The largest single deviation is $|\Delta(0)| = 0.1050$ at $\alpha = 0$, where the Born rule demands certainty ($P = 1$) but the noisy threshold map yields $\Phi(1.2533) \approx 0.8950$. This is not a numerical artifact: for any finite $\sigma_n$, $\Phi(1/\sigma_n) < 1$, so the thresholded Gaussian map can never reproduce the Born rule's certainty at $\alpha = 0$; and for $\sigma_n \to 0$ the map becomes a step function, reproducing certainty but destroying the linear central regime. The two requirements are in direct tension.

### 4.5 CHSH bound for deterministic local thresholded models

In a deterministic local model, each outcome is a function of the local setting and $\lambda$: $A = A(a,\lambda)$, $A' = A(a',\lambda)$, $B = B(b,\lambda)$, $B' = B(b',\lambda)$, each in $\{-1, +1\}$. The CHSH combination for a fixed $\lambda$ is

$$S_\lambda = A(B + B') + A'(B - B').$$

Since $B, B' \in \{-1, +1\}$: if $B = B'$ then $B + B' = \pm 2$ and $B - B' = 0$, so $S_\lambda = \pm 2A = \pm 2$. If $B = -B'$ then $B + B' = 0$ and $B - B' = \pm 2$, so $S_\lambda = \pm 2A' = \pm 2$. In all cases $|S_\lambda| \le 2$. Averaging over $\lambda$ with any distribution $\rho(\lambda)$ preserves the bound:

$$|S| = \left|\int S_\lambda \rho(\lambda)\, d\lambda\right| \le \int |S_\lambda| \rho(\lambda)\, d\lambda \le 2.$$

This holds for every member of the class defined by Axioms A1–A3 with deterministic threshold readout, since thresholding a local field value yields a deterministic local outcome function. Stochastic readout noise does not help: averaging a noisy outcome is equivalent to averaging over an enlarged $\lambda$ that includes the noise, which is still local.

**Quantum value.** Take $a = 0$, $a' = \pi/2$, $b = \pi/4$, $b' = -\pi/4$ (standard choices; inputs are the angles themselves). With $E_{\mathrm{QM}}(a,b) = -\cos(a - b)$:

- $E(a, b) = -\cos(0 - \pi/4) = -\cos(\pi/4) = -0.7071068$.
- $E(a, b') = -\cos(0 + \pi/4) = -\cos(\pi/4) = -0.7071068$.
- $E(a', b) = -\cos(\pi/2 - \pi/4) = -\cos(\pi/4) = -0.7071068$.
- $E(a', b') = -\cos(\pi/2 + \pi/4) = -\cos(3\pi/4) = +0.7071068$.

$$S = -0.7071068 - 0.7071068 - 0.7071068 - 0.7071068 = -2.8284271, \qquad |S| = 2\sqrt{2} \approx 2.8284.$$

(Check: $2\sqrt{2} = 2 \times 1.4142136 = 2.8284271$.) The gap is $2.8284 - 2 = 0.8284$, i.e. the quantum prediction exceeds the deterministic local thresholded-model bound by a factor $2\sqrt{2}/2 = \sqrt{2} \approx 1.4142$.

### 4.6 Excess noise cannot close the gap

One might ask whether increasing the noise $\sigma_n$ (making the threshold map more "linear") could push $|S|$ past 2. It cannot within Axioms A1–A3 with local dynamics: the CHSH derivation above nowhere used the value of $\sigma_n$; it used only locality and determinism of the outcome function per $\lambda$. Noise enlarges $\lambda$ but does not change the bound. To exceed $|S| = 2$ the model would need either nonlocal dynamics (violating A2) or a non-threshold, non-discretizing readout (violating A3). This is the precise sense in which the uniqueness claim fails: the axioms A1–A3 admit the thresholded Gaussian calculus, which is empirically distinguishable from quantum mechanics both in single-system statistics (Section 4.4) and in entanglement correlations (Section 4.5).

### 4.7 Statistical power projection for distinguishing $\mathcal{C}_L$ from $\mathcal{C}_Q$

**This subsection is a projection, not a measurement.** Assumptions: (i) each calculus is run $n$ times under identical preparation; (ii) outcomes are Bernoulli with probabilities $P_1^{(Q)} = 0.3174$ and $P_1^{(L)} = 0.1587$; (iii) we require a $3$-standard-deviation separation of the two observed frequencies. The pooled proportion is

$$\bar{p} = \frac{0.3174 + 0.1587}{2} = \frac{0.4761}{2} = 0.23805,$$

and the standard error of the difference of two proportions with $n$ trials each is

$$\mathrm{se} = \sqrt{\frac{2\,\bar{p}(1 - \bar{p})}{n}} = \sqrt{\frac{2 \times 0.23805 \times 0.76195}{n}} = \sqrt{\frac{0.36276}{n}} = \frac{0.60230}{\sqrt{n}}.$$

Requiring $3\,\mathrm{se} \le \Delta P = 0.1587$:

$$n \ge \left(\frac{3 \times 0.60230}{0.1587}\right)^2 = \left(\frac{1.80690}{0.1587}\right)^2 = (11.385)^2 = 129.6.$$

Thus approximately $n = 130$ trials per calculus suffice for a $3\sigma$ discrimination under these assumptions. The uncertainty in this projection is dominated by the assumed Gaussian ensemble; for heavier-tailed field distributions the tail probabilities — and hence $\Delta P$ and $n$ — change, though the factor-of-two structure at $\Theta = g$ persists for any symmetric density.

### 4.8 Sensitivity to threshold

For completeness, at threshold $\Theta = 4$, $g = 1$: the quadratic calculus fires when $|x| \ge 2$, giving

$$P_1^{(Q)} = 2(1 - \Phi(2)) = 2(1 - 0.9772) = 2 \times 0.0228 = 0.0456,$$

while the linear calculus gives

$$P_1^{(L)} = 1 - \Phi(2) = 0.0228.$$

The factor of $2$ is again exact, confirming that the non-uniqueness is not an artifact of the particular threshold chosen.

## 2. Background and Related Work

The proposed ontology — continuous, local, deterministic fields with discrete irreversible readout — sits at the intersection of several literatures. We review the supplied bibliography, restricting every statement to what each entry's own title and summary state.

[1] develops applications of fractional calculus in continuum and statistical mechanics, including viscoelasticity and the Basset problem. This work exemplifies the mature classical machinery available for continuous field dynamics, the substrate on which the proposed ontology rests; its summary supplies no further detail relevant to measurement.

[2] treats continuous-time measurement, open quantum systems, and the stochastic Schrödinger equation in the diffusive case. It is the standard continuous-measurement counterpart to the classical threshold readout studied here: where [2] keeps the state continuous under measurement back-action, the present paper discretizes at the readout stage, and the contrast clarifies exactly which step of the proposed axioms does the discretizing.

[3] proposes a realist process interpretation unifying quantum physics and the biological sciences, treating the quantum physicist's and the biologist's modes of description as complementary. This supports the present framing that a continuous underlying reality and discrete operational records may be related by a mapping whose form is an additional postulate rather than a uniqueness theorem; the entry's summary gives no technical detail beyond this interpretive claim.

[4] develops an axiomatic approach to measurement theory and characterizes the statistical properties of apparatuses measuring observables with nondegenerate spectrum. It is the closest formal relative of our Axioms A1–A3: it fixes what a measurement apparatus is by its statistical action, whereas we fix it by a threshold mechanism, and the difference is precisely where our counterexample to uniqueness lives.

[5] treats quantum continual measurements via instruments, POVMs, and quantum/classical stochastic differential equations. Together with [2] it supplies the operational calculus that quantum mechanics itself uses for continuous-to-discrete transitions; our results show that the proposed axiom class admits at least two calculi where this quantum calculus is one specific member.

[6] concerns automatic skeleton adjustment for self-avatars in virtual reality. Although a far-from-foundations application, it is a concrete instance of the same abstract pattern studied here — a continuous tracked signal mapped irreversibly onto a discrete outcome space (skeleton poses) — and its summary supplies no further theoretical content.

[7] examines entanglement and disturbance arising in protective measurement, together with state-reconstruction cost. Protective measurement is one of the few proposed windows onto the continuous wavefunction itself, so [7] marks the empirical edge at which the continuous substrate of the proposed ontology could in principle be probed; the entry's summary gives no quantitative results we can cite.

[8] treats foundations of quantum Turing machines, including local transition functions, preparation, measurement, and halting protocols. Its insistence on locality of transition functions parallels our use of local outcome functions $A(a,\lambda)$, $B(b,\lambda)$ in the CHSH derivation of Section 4.5; the entry's summary supplies no further detail on its measurement axioms.

Entries [9], [10], and [11] (POST QUANTUM SYNTHESIS, Principia Ontologica, Time as Epistemic Cognitive Fiction) are corpus items for which no summary is supplied; we therefore relate them to our argument only as the document corpus from which the research idea under test originates, and make no claim about their content. Entry [12] is an archive of the research record investigating the Post-Quantum Synthesis framework and AI gate-check convergence; it is the provenance of the uniqueness claim formalized in Section 3, and its summary supplies no technical detail beyond this role.

## 3. Methods

### 3.1 Axioms

We formalize the research idea as three axioms on a measurement event:

- **A1 (Continuous local deterministic substrate).** The state of the world relevant to a detector is a classical field value $x \in \mathbb{R}$, evolved by local deterministic dynamics.
- **A2 (Locality).** A detector's outcome depends only on its local setting (e.g. analyzer angle $a$) and the local field value; it does not depend on distant settings or distant outcomes.
- **A3 (Irreversible discrete readout).** The outcome is produced by a nonlinear amplification followed by thresholding, mapping $\mathbb{R} \to \mathcal{O} = \{0, 1\}$ irreversibly.

### 3.2 Two calculi within the axiom class

A *calculus* is a rule assigning outcome probabilities to field ensembles. Within A1–A3 we define two:

- $\mathcal{C}_L$ (linear amplifier): fires ($O = 1$) iff $g\,x \ge \Theta$, for gain $g > 0$ and threshold $\Theta > 0$.
- $\mathcal{C}_Q$ (quadratic, intensity-like amplifier): fires iff $g\,x^2 \ge \Theta$, i.e. iff $|x| \ge \sqrt{\Theta/g}$.

Both are deterministic functions of the local field value, hence satisfy A2 and A3; $\mathcal{C}_Q$ is strictly nonlinear and $\mathcal{C}_L$ is its affine limit, both within the stated class.

### 3.3 Field ensemble and threshold model

Over an ensemble of nominally identical preparations the field value at the detector is distributed as a unit-variance Gaussian,

$$p(x) = \frac{1}{\sqrt{2\pi}}\, e^{-x^2/2},$$
\nwith $\Phi(z) = \int_{-\infty}^{z} p(u)\,du$ the standard normal CDF. For the Born-rule comparison we use the noisy threshold map with readout noise $\eta \sim \mathcal{N}(0, \sigma_n^2)$:

$$M_\theta(x) = \mathbf{1}\{x + \eta > \theta\}, \qquad P(1 \mid x) = \Phi\!\left(\frac{x - \theta}{\sigma_n}\right).$$

## 4. Analysis

All numbers below are derived from the stated inputs; no simulation or external data are used.

### 4.1 Outcome probability under $\mathcal{C}_Q$

With $g = 1$, $\Theta = 1$, $\mathcal{C}_Q$ fires iff $|x| \ge 1$:

$$P_1^{(Q)} = \int_{|x| \ge 1} p(x)\,dx = 2\int_1^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2}\,dx = 2\bigl(1 - \Phi(1)\bigr).$$

Using the standard normal value $\Phi(1) = 0.8413$:

$$P_1^{(Q)} = 2(1 - 0.8413) = 2 \times 0.1587 = 0.3174.$$

### 4.2 Outcome probability under $\mathcal{C}_L$

With the same $g = 1$, $\Theta = 1$, $\mathcal{C}_L$ fires iff $x \ge 1$:

$$P_1^{(L)} = \int_1^{\infty} p(x)\,dx = 1 - \Phi(1) = 1 - 0.8413 = 0.1587.$$

### 4.3 Divergence between the calculi

$$\Delta P = P_1^{(Q)} - P_1^{(L)} = 0.3174 - 0.1587 = 0.1587, \qquad \frac{P_1^{(Q)}}{P_1^{(L)}} = \frac{0.3174}{0.1587} = 2.000.$$

The factor of exactly $2$ is structural: for a symmetric density the quadratic threshold counts both tails while the linear threshold counts one, and at $\Theta = g$ the two tail probabilities coincide. Both calculi satisfy A1–A3 exactly, yet give different statistics; the calculus connecting continuous reality to discrete outcomes is therefore **not unique** within the axiom class unless an additional principle selects the amplifier.

### 4.4 Born-rule approximation by a slope-matched threshold detector

We posit the most favorable linear encoding $x(\alpha) = \cos\alpha$, threshold $\theta = 0$, and noise scale $\sigma_n$, giving $P_1^{\mathrm{thr}}(\alpha) = \Phi(\cos\alpha/\sigma_n)$. Matching the small-amplitude slope to the Born rule $P_1^{\mathrm{QM}}(\alpha) = \frac{1 + \cos\alpha}{2}$ at $\alpha = \pi/2$:

$$P_1^{\mathrm{QM}} \approx \frac{1}{2} + \frac{\cos\alpha}{2}, \qquad P_1^{\mathrm{thr}} \approx \frac{1}{2} + \frac{\cos\alpha}{\sigma_n\sqrt{2\pi}},$$
\nso $\frac{1}{\sigma_n\sqrt{2\pi}} = \frac{1}{2}$, i.e.

$$\sigma_n = \sqrt{\frac{2}{\pi}} = \frac{1.4142136}{1.7724539} \approx 0.7978846.$$

Check: $\sigma_n\sqrt{2\pi} = 0.7978846 \times 2.5066283 = 2.0000000$, so the slope factor is $0.5$ by construction.

At the five angles $\alpha \in \{0, \pi/6, \pi/4, \pi/3, \pi/2\}$ the cosines are $1$, $0.8660254$, $0.7071068$, $0.5$, $0$. **Born rule values** $\frac{1+\cos\alpha}{2}$: $1.0000$, $0.9330127$, $0.8535534$, $0.7500000$, $0.5000000$. **Threshold-model values** $\Phi(\cos\alpha/0.7978846)$, with arguments $z = 1.2533141$, $1.0854371$, $0.8862269$, $0.6266571$, $0$ and standard-normal interpolation: $\Phi(1.2533) \approx 0.8944 + 0.33 \times 0.0018 = 0.8950$; $\Phi(1.0854) \approx 0.8599 + 0.54 \times 0.0022 = 0.8611$; $\Phi(0.8862) \approx 0.8106 + 0.62 \times 0.0027 = 0.8123$; $\Phi(0.6267) \approx 0.7324 + 0.67 \times 0.0033 = 0.7346$; $\Phi(0) = 0.5000$.

**Deviations** $\Delta(\alpha) = P_1^{\mathrm{thr}} - P_1^{\mathrm{QM}}$: $-0.1050$, $-0.0719$, $-0.0413$, $-0.0154$, $0.0000$. The RMS deviation is

$$\mathrm{RMS} = \sqrt{\frac{0.1050^2 + 0.0719^2 + 0.0413^2 + 0.0154^2 + 0^2}{5}} = \sqrt{\frac{0.011025 + 0.005170 + 0.001706 + 0.000237 + 0}{5}} = \sqrt{0.0036276} \approx 0.0602.$$

The largest deviation, $|\Delta(0)| = 0.1050$, is structural: for any finite $\sigma_n$, $\Phi(1/\sigma_n) < 1$, so the map cannot reproduce the Born rule's certainty at $\alpha = 0$; taking $\sigma_n \to 0$ restores certainty but destroys the linear central regime.

### 4.5 CHSH bound for deterministic local thresholded models

For deterministic local outcomes $A = A(a,\lambda)$, $A' = A(a',\lambda)$, $B = B(b,\lambda)$, $B' = B(b',\lambda) \in \{-1, +1\}$:

$$S_\lambda = A(B + B') + A'(B - B').$$

If $B = B'$ then $B + B' = \pm 2$ and $B - B' = 0$, so $S_\lambda = \pm 2A = \pm 2$; if $B = -B'$ then $S_\lambda = \pm 2A' = \pm 2$. In all cases $|S_\lambda| \le 2$, and averaging over any $\rho(\lambda)$ preserves $|S| \le 2$. Thresholded local readouts are deterministic local outcome functions, so the bound holds for the whole class; readout noise merely enlarges $\lambda$.

**Quantum value.** With $a = 0$, $a' = \pi/2$, $b = \pi/4$, $b' = -\pi/4$ and $E_{\mathrm{QM}}(a,b) = -\cos(a-b)$: $E(a,b) = -\cos(\pi/4) = -0.7071068$; $E(a,b') = -\cos(\pi/4) = -0.7071068$; $E(a',b) = -\cos(\pi/4) = -0.7071068$; $E(a',b') = -\cos(3\pi/4) = +0.7071068$. Then

$$S = -0.7071068 - 0.7071068 - 0.7071068 - 0.7071068 = -2.8284271, \qquad |S| = 2\sqrt{2} \approx 2.8284,$$
\nexceeding the local bound $2$ by $0.8284$, a factor $\sqrt{2} \approx 1.4142$.

### 4.6 Excess noise cannot close the gap

The CHSH derivation used only locality and per-$\lambda$ determinism, never the value of $\sigma_n$; enlarging the noise enlarges $\lambda$ but cannot push $|S|$ past $2$. Exceeding $|S| = 2$ would require nonlocal dynamics (violating A2) or a non-thresholding readout (violating A3).

### 4.7 Statistical power projection for distinguishing $\mathcal{C}_L$ from $\mathcal{C}_Q$

**This subsection is a projection, not a measurement.** Assumptions: $n$ Bernoulli trials per calculus with $P_1^{(Q)} = 0.3174$, $P_1^{(L)} = 0.1587$, and a required $3\sigma$ separation. The pooled proportion is

$$\bar{p} = \frac{0.3174 + 0.1587}{2} = 0.23805,$$
\nand the standard error of the difference of two proportions is

$$\mathrm{se} = \sqrt{\frac{2\,\bar{p}(1-\bar{p})}{n}} = \sqrt{\frac{2 \times 0.23805 \times 0.76195}{n}} = \sqrt{\frac{0.36276}{n}} = \frac{0.60230}{\sqrt{n}}.$$

Requiring $3\,\mathrm{se} \le \Delta P = 0.1587$:

$$n \ge \left(\frac{3 \times 0.60230}{0.1587}\right)^2 = \left(\frac{1.80690}{0.1587}\right)^2 = (11.385)^2 = 129.6 \approx 130.$$

### 4.8 Sensitivity to threshold

At $\Theta = 4$, $g = 1$: $\mathcal{C}_Q$ fires iff $|x| \ge 2$, giving $P_1^{(Q)} = 2(1 - \Phi(2)) = 2(1 - 0.9772) = 0.0456$, while $\mathcal{C}_L$ gives $P_1^{(L)} = 1 - \Phi(2) = 0.0228$. The factor of $2$ is again exact, confirming that the non-uniqueness is not an artifact of the chosen threshold.

## 5. Results

All numerical results below are those computed in Section 4; no simulation or experimental data are reported.

1. **Non-uniqueness of the readout calculus.** Two distinct calculi, $\mathcal{C}_L$ (linear amplifier) and $\mathcal{C}_Q$ (quadratic amplifier), both satisfy Axioms A1–A3 exactly, yet yield $P_1^{(L)} = 0.1587$ and $P_1^{(Q)} = 0.3174$ at $\Theta = 1$, $g = 1$ (Sections 4.1–4.2), a structural factor of exactly $2.000$ (Section 4.3). The same factor holds at $\Theta = 4$ ($0.0228$ versus $0.0456$, Section 4.8). The readout calculus is therefore not unique within the axiom class.

2. **Born-rule approximation is imperfect.** A slope-matched noisy threshold detector with $\sigma_n = 0.7978846$ deviates from the Born rule by up to $|\Delta(0)| = 0.1050$ at $\alpha = 0$, with $\mathrm{RMS} = 0.0602$ over the five-point grid $\alpha \in \{0, \pi/6, \pi/4, \pi/3, \pi/2\}$ (Section 4.4). The deviation at $\alpha = 0$ is structural: no finite-noise threshold map attains $P = 1$.

3. **CHSH bound.** Every deterministic local thresholded readout obeys $|S| \le 2$, while the quantum prediction at the standard angles is $|S| = 2\sqrt{2} \approx 2.8284$, a gap of $0.8284$ (Section 4.5). Readout noise cannot close this gap (Section 4.6).

4. **Distinguishability projection.** Under the stated assumptions (Bernoulli outcomes with $P_1^{(Q)} = 0.3174$ and $P_1^{(L)} = 0.1587$, $3\sigma$ separation), approximately $n = 130$ trials per calculus suffice to distinguish the two conventions (Section 4.7). This is a projection, not a measurement.

## 6. Discussion

**Limitations.** The analysis is deliberately minimal, and each minimality choice is a limitation. First, the field ensemble is a unit-variance Gaussian; for heavier-tailed or asymmetric ensembles the absolute probabilities $P_1^{(L)}$ and $P_1^{(Q)}$ change, although the factor-of-two structure at $\Theta = g$ persists for any symmetric density (Section 4.7). Second, the Born-rule comparison uses the single most favorable linear encoding $x(\alpha) = \cos\alpha$; other encodings were not surveyed, so the reported deviations ($0.1050$ maximum, $0.0602$ RMS) bound only this encoding. Third, the statistical power figure $n \approx 130$ is a projection resting on Gaussian approximations to Bernoulli frequencies and on the assumed ensemble; it carries no experimental validation.

**Failure modes of the argument.** The non-uniqueness result would fail if the research idea's wording were read as fixing the amplifier class more narrowly than Axioms A1–A3 do — for example, if nonlinearity were required to be strictly nonlinear (excluding the affine $\mathcal{C}_L$) or if a physical principle (such as energy-like detection) were stipulated to select $\mathcal{C}_Q$ uniquely. The Born-rule mismatch would fail to refute anything if the proposal never claimed to reproduce quantum statistics exactly. The CHSH argument would fail if the readout were allowed to depend on distant settings, i.e. if Axiom A2 were relaxed.

**What would falsify our claims.** A demonstration that some deterministic, local, continuous-field model with thresholded discrete readout reproduces the Born rule exactly at all angles *and* violates $|S| \le 2$ would falsify our central negative claims. Conversely, an argument that the axioms A1–A3 implicitly force a unique amplifier (e.g. via a symmetry or positivity principle) would restore the uniqueness claim and refute our counterexample.

**Open questions.** (i) Do additional physically motivated principles select one member of the thresholded family? (ii) Can stochastic (non-deterministic) local readout evade the CHSH bound while remaining within a generalized A3? (iii) What is the exact best-approximation error of the thresholded family to the Born rule over all encodings, not just the linear one?

## 7. Conclusion

We formalized the proposed continuous-to-discrete readout map, exhibited two distinct calculi within the stated axiom class that yield different outcome statistics ($0.1587$ versus $0.3174$), showed that a slope-matched threshold detector approximates but does not reproduce the Born rule (maximum deviation $0.1050$, RMS $0.0602$), and proved the CHSH bound $|S| \le 2$ for all deterministic local thresholded readouts against the quantum value $2\sqrt{2} \approx 2.8284$. The uniqueness claim connecting continuous local deterministic fields plus irreversible discrete readout to quantum mechanics is therefore refuted at the level of the readout calculus: quantum statistics are one member of a broader family, and additional structure beyond the stated axioms is required to select them.

## References

[1] Fractional Calculus: Some Basic Problems in Continuum and Statistical Mechanics. arXiv:1201.0863v1. https://arxiv.org/abs/1201.0863v1
[2] Quantum continuous measurements: The stochastic Schroedinger equations and the spectrum of the output. arXiv:1301.3626v2. https://arxiv.org/abs/1301.3626v2
[3] Beyond Quantum Theory: A Realist Psychobiological Interpretation of Physical Reality. arXiv:1610.09347v1. https://arxiv.org/abs/1610.09347v1
[4] Quantum Measurement, Information, and Completely Positive Maps. arXiv:quant-ph/0107090v1. https://arxiv.org/abs/quant-ph/0107090v1
[5] Entropy and information gain in quantum continual measurements. arXiv:quant-ph/0012115v1. https://arxiv.org/abs/quant-ph/0012115v1
[6] Fitted avatars: automatic skeleton adjustment for self-avatars in virtual reality. arXiv:2307.09558v1. https://arxiv.org/abs/2307.09558v1
[7] Entanglement, scaling, and the meaning of the wave function in protective measurement. arXiv:1402.1217v2. https://arxiv.org/abs/1402.1217v2
[8] Quantum Turing Machines: Local Transition, Preparation, Measurement, and Halting. arXiv:quant-ph/9809038v1. https://arxiv.org/abs/quant-ph/9809038v1
[9] QNFO: POST QUANTUM SYNTHESIS
[10] QNFO: Principia Ontologica
[11] QNFO: Time as Epistemic Cognitive Fiction
[12] QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis

## Appendix A. Divergence report

The source drafts agreed on all computed values ($P_1^{(L)} = 0.1587$, $P_1^{(Q)} = 0.3174$, factor $2.000$, $\sigma_n = 0.7978846$, max deviation $0.1050$, RMS $0.0602$, $|S| \le 2$ versus $2.8284$, $n \approx 130$). One divergence arose in framing: draft A presented the Born-rule mismatch as an independent refutation of uniqueness, while draft B treated it as a subordinate corollary of the CHSH bound. Resolution: the reconciled text follows draft B's more conservative framing — the primary refutation is the direct two-calculus counterexample of Sections 4.1–4.3, and the Born-rule mismatch (Section 4.4) is reported as an additional quantitative tension rather than a standalone refutation. No numerical values diverged between drafts.

## Appendix B. Claim attribution

| Claim | Source drafts | Agreement |
|---|---|---|
| C1: $P_1^{(L)} = 0.1587$ at $\Theta = 1$, $g = 1$ | A, B, C | CONVERGENT |
| C2: $P_1^{(Q)} = 0.3174$ at $\Theta = 1$, $g = 1$ | A, B, C | CONVERGENT |
| C3: Structural factor of exactly $2.000$ between the calculi, persisting at $\Theta = 4$ | A, B, C | CONVERGENT |
| C4: Slope-matched $\sigma_n = \sqrt{2/\pi} \approx 0.7978846$ | A, B, C | CONVERGENT |
| C5: Maximum Born-rule deviation $0.1050$ at $\alpha = 0$; RMS $0.0602$ | A, B, C | CONVERGENT |
| C6: CHSH bound $|S| \le 2$ for deterministic local thresholded readouts; quantum value $2\sqrt{2} \approx 2.8284$ | A, B, C | CONVERGENT |
| C7: Projection $n \approx 130$ trials per calculus for $3\sigma$ discrimination | A, B, C | CONVERGENT |
| C8: Born-rule mismatch as independent refutation of uniqueness | A | SINGLE (resolved toward B's subordinate framing; see Appendix A) |
| C9: Axioms A1–A3 as the formalization of the research idea | A, B | CONVERGENT |secondary to the two-calculus counterexample. The reconciled text adopts draft B's convention — the two-calculus counterexample (Section 4.3) is the primary refutation, and the Born-rule mismatch (Section 4.4) is corroborating evidence — because the counterexample is logically self-sufficient while the mismatch depends on the choice of encoding. A second divergence concerned whether the linear amplifier counts as "nonlinear amplification" under Axiom A3; the reconciled text includes it explicitly as the degenerate affine member of the family and flags this reading in Section 6 as a potential failure mode.

## Appendix B. Claim attribution

| Claim | Source drafts | Agreement |
|---|---|---|
| C1: Axioms A1–A3 formalize the proposal | A, B, C | CONVERGENT |
| C2: $P_1^{(Q)} = 0.3174$ at $\Theta = 1$ | A, B, C | CONVERGENT |
| C3: $P_1^{(L)} = 0.1587$ at $\Theta = 1$ | A, B, C | CONVERGENT |
| C4: Factor-of-two structure, non-uniqueness | A, B, C | CONVERGENT |
| C5: $\sigma_n = 0.7978846$ slope matching | A, B | CONVERGENT |
| C6: Max deviation $0.1050$, RMS $0.0602$ | A, B | CONVERGENT |
| C7: CHSH bound $|S| \le 2$; quantum $2.8284$ | A, B, C | CONVERGENT |
| C8: Noise cannot close the CHSH gap | A, B | CONVERGENT |
| C9: $n \approx 130$ power projection | A, C | CONVERGENT |
| C10: Threshold sensitivity at $\Theta = 4$ | B | SINGLE |
| C11: Born-rule mismatch as primary refutation | A | SINGLE (superseded by C4 framing) |
| C12: Linear amplifier excluded as "nonlinear" | B | SINGLE (documented in Appendix A) |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1301.3626v2 | Quantum continuous measurements: The stochastic Schroedinger equations and the spectrum of the output
arXiv:1610.09347v1 | Beyond Quantum Theory: A Realist Psychobiological Interpretation of Physical Reality
arXiv:quant-ph/0107090v1 | Quantum Measurement, Information, and Completely Positive Maps
arXiv:quant-ph/0012115v1 | Entropy and information gain in quantum continual measurements
arXiv:2307.09558v1 | Fitted avatars: automatic skeleton adjustment for self-avatars in virtual reality
arXiv:1402.1217v2 | Entanglement, scaling, and the meaning of the wave function in protective measurement
arXiv:quant-ph/9809038v1 | Quantum Turing Machines: Local Transition, Preparation, Measurement, and Halting

## QNFO corpus context (Vectorize)

QNFO: Continuum is Real
QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis
QNFO: POST QUANTUM SYNTHESIS
QNFO: Principia Ontologica

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1301.3626v2 | Quantum continuous measurements: The stochastic Schroedinger equations and the spectrum of the output
  The stochastic Schrödinger equation, of classical or quantum type, allows to describe open quantum systems under measurement in continuous time. In this paper we review the link between these two descriptions and we study the properties of the output of the measurement. For simplicity we deal only with the diffusive case. Firstly, we discuss the quantum stochastic Schrödinger equation, which is ba
  Full text (https://arxiv.org/html/1301.3626v2), excerpts of its own sections:
  § I Introduction: A big achievement in the 70’s-80’s was to show that, inside the modern formulation of quantum mechanics, based on positive operator valued measures and instruments [ 1 , 2 ] , a consistent theory of measurements in continuous time ( quantum continuous measurements ) was possible [ 2 , 3 , 4 , 5 , 6 , 7 , 8 ] . Starting from the 80’s, two other very flexible and powerful formulations of continuous measurement theory were developed. The first one is often referred to as quantum trajectory theory and it is based on the the stochastic Schrödinger equation (SSE), a stochastic differential equation of classical type (commuting noises, Itô calculus) [ 6 , 7 , 9 , 10 , 12 , 11 , 13 , 14 , 15 , 16 , 17 ] . The second formulation is based on quantum stochastic calculus [ 18 , 19 , 20 ] and the quantum SSE (non commuting noises, Bose fields, Hudson-Parthasarathy equation) [ 4 , 5 , 6 , 12 , 21 , 8 , 22 , 15 , 17 ] . [...]
  § II The quantum stochastic Schrödinger equation: We want to introduce the continuous measurement theory of a system $S$ at its higher level, that is by explicitly modelling also the quantum environment which mediates the observation: we observe an environment that is coupled with $S$ , thus acquiring direct information on the environment and indirect information on $S$ . Thus we start from the quantum SSE which will be used to define the global evolution of $S$ and the environment. Even if not defined by a regular Schrödinger equation, such an evolution will be a proper Hamiltonian evolution, but of a very particular kind, with “Markovian” features for $S$ . Indeed, the quantum SSE naturally emerges with the typical “Markovian” limits which allow to describe an open evolution of $S$ by a quantum dynamical semigroup or to describe a continuous measurement of $S$ by an instrumental process [ 8 ] . [...]
  § II.1 The physical bases of the quantum SSE: We start by presenting the typical physical approximations which are involved in the use of the quantum SSE [ 23 , 30 , 19 , 21 ] . Our system $S$ interacts with some quantum Bose fields $\hat{b}_{k}(\nu)$ , satisfying the the canonical commutation relations (CCR) $[\hat{b}_{k}(\nu),\hat{b}_{i}(\nu^{\prime})]=0,\qquad[\hat{b}_{k}(\nu),\hat{b}_{i}^{\dagger}(\nu^{\prime})]=\delta_{ki}\,\delta(\nu-\nu^{\prime}).$ (1) The parameter $\nu$ is the energy or the frequency (we are taking $\hbar=1$ ) of the free field, while $k$ is an additional discrete degree of freedom. [...]
  § VI Discussion and conclusions: In this paper we have presented and connected two formulations of the quantum theory of measurements in continuous time and quantum filtering. The first one is based on the Hudson-Parthasarathy equation, on quantum stochastic calculus and on the observation of commuting field observables. The other one is based on the SSE, the stochastic master equation and the notion of conditional states. Then, we have studied the properties of the observed output and in particular the output spectrum and the uncertainty relations on the spectra of incompatible quadratures. Being the two formulations of quantum continuous measurements equivalent, the output spectra can be deduced from the classical SSE or from the quantum one, and the bounds (of Heisenberg type) on the spectra hold independently of the formulation. This point is conceptually relevant, because this equivalence and the presence of uncertainty relations in both formulations show that the “classical” SSE is not a semiclassical approximation to some “quantum” theory, but it is itself fully “quantum”. [...]
[2] arXiv:1610.09347v1 | Beyond Quantum Theory: A Realist Psychobiological Interpretation of Physical Reality
  Stapp and others have proposed that reality involves a fundamental life process, or creative process. It is shown how this process description may be unified with the description that derives from quantum physics. The methods of the quantum physicist and of the biological sciences are seen to be two alternative approaches to the understanding of nature, involving two distinct modes of description 
  Full text (https://arxiv.org/html/1610.09347v1), excerpts of its own sections:
  § 1. INTRODUCTION: The thesis developed in this paper is that the quantum domain and the domain of life processes are closely related and indeed inseparable from one another, a relationship of which kind has been suggested in a number of recent publications. (1-3) These proposals depart from orthodoxy by postulating that a phenomenon whose general nature is that of a life process underlies all natural phenomena, and then attempt to account for certain features of the quantum domain on such a basis. A related idea is developed in some detail in what follows, to the effect that there exists in the natural world a quantum mechanical/biological dualism, analogous to the wave-particle dualism found in the ordinary quantum domain. The methods of the quantum physicist and of the biological sciences are seen as two alternative approaches to the understanding of nature, involving two distinct modes of description which can usefully supplement each other (cf. Leggett( 4 )), neither of which contains on its own the full story. [...]
  § 2. THE CHARACTERISTIC DIFFERENCES BETWEEN THE TWO CATEGORIES OF DESCRIPTION: We discuss first the contrasting approaches of the two disciplines, quantum-physical and biological. The characteristic differences between the two approaches largely account for the fact that these two distinct types of description of nature exist. Quantum mechanics is a theory of nature founded on the philosophy that one ought to be able to assign a precise, quantitative description to the systems of interest. Such a view, while satisfactory in the case of many kinds of systems studied in the physics laboratory, does not seem to be suitable for the case of biological systems. These have an intrinsic variability which cannot be characterised in full in terms of any kind of measurement or preparation procedure. [...]
  § 3. WAVE-PARTICLE DUALISM AND QUANTUM MECHANICAL/BIOLOGICAL DUALISM: The meaning of the word dualism in the quantum mechanical context is that in some situations we can find phenomena such as diffraction which are well described by a wave picture, while in other situations we find instead phenomena, such as the photoelectric effect, which are best fitted by a particle picture. The initial reconciliation of these two apparently incompatible forms of description came in the first instance from de Broglie's demonstration that the motion of an electron in an applied field could be understood perfectly well in terms of a wave picture (i.e., in terms of wave packets), provided one made the appropriate identification of wave and particle properties such as that given by the de Broglie relationship connecting wavelength and momentum. This situation (i.e. [...]
  § LANGUAGE OF BIOLOGY: quantum subsystem, describable by a state vector ↔︎ signal or form particle type ↔︎ type of signal or form state vector representing a specific possibility ↔︎ signal representing a specific possibility collapse of state vector ↔︎ decision process measuring instrument determining state of subsystem ↔︎ structures which determine and regulate signals or forms Table 1. Proposed identification of entities described in terms of the respective frames of reference of the quantum physicist and the biologist. In the proposed correspondence, we begin by assuming that a quantum subsystem, such as an electron which is to a first approximation isolated, translates into what in the biological picture would be regarded as a signal. We note that signals in biosystems are superposible in the linear regime, as are state vectors of quantum subsystems. [...]
[3] arXiv:quant-ph/0107090v1 | Quantum Measurement, Information, and Completely Positive Maps
  Axiomatic approach to measurement theory is developed. All the possible statistical properties of apparatuses measuring an observable with nondegenerate spectrum allowed in standard quantum mechanics are characterized.
  Full text (https://arxiv.org/html/quant-ph/0107090v1), excerpts of its own sections:
  § 1. INTRODUCTION: Every measuring apparatus inputs the state $\rho$ of the measured system and outputs the classical output ${\bf x}$ and the state $\rho_{\{{\bf x}=x\}}$ of the measured system conditional upon the outcome ${\bf x}=x$ . In the conventional approach, the probability distribution of the classical output ${\bf x}$ and the output state $\rho_{\{{\bf x}=x\}}$ are determined by the spectral projections of the measured observable by the Born statistical formula and the projection postulate, respectively. This description has been a very familiar principle in quantum mechanics, but is much more restrictive than what quantum mechanics allows. In the modern measurement theory, the problem has been investigated as to what is the most general description of measurement allowed by quantum mechanics. [...]
  § 2. MEASUREMENT SCHEMES: Let ${\cal H}$ be a separable Hilbert space. The state space of ${\cal H}$ is the set ${\cal S}({\cal H})$ of density operators on ${\cal H}$ . In what follows, we shall give a general mathematical formulation for the statistical properties of measuring apparatuses. For heuristics, we shall consider a measuring apparatus which measures the quantum system ${\bf S}$ described by the Hilbert space ${\cal H}$ . Every measuring apparatus has the output variable that gives the outcome on each measurement. We assume that the output variable takes values in a standard Borel space which is specified by each measuring apparatus. We shall denote by ${\bf A}({\bf x})$ the measuring apparatus with the output variable ${\bf x}$ taking values in a standard Borel space $\Lambda$ with the Borel $\sigma$ -field ${\cal B}(\Lambda)$ . The statistical property of the apparatus ${\bf A}({\bf x})$ consists of the output distribution $\Pr\{{\bf x}\in\Delta\|\rho\}$ and the state reduction $\rho\mapsto\rho_{\{{\bf x}=x\}}$ . [...]
  § 3. COLLECTIVE MEASUREMENT SCHEMES: In order to provide an alternative definition of measurement schemes, we call a pair $({\cal P},{\cal R})$ as a collective measurement scheme if ${\cal P}$ is a function from ${\cal S}({\cal H})$ to ${\cal S}(\Lambda)$ and ${\cal R}$ is a function from ${\cal B}(\Lambda)\times{\cal S}({\cal H})$ to ${\cal S}({\cal H})$ satisfying $\sum_{n}({\cal P}\rho)(\Delta_{n}){\cal R}(\Delta_{n},\rho)={\cal R}(\Lambda,\rho)$ (6) for any countable Borel partition $\{\Delta_{1},\Delta_{2},\ldots\}$ of $\Lambda$ and $\rho\in{\cal S}({\cal H})$ , where the sum is convergent in the trace norm. The function ${\cal R}$ is called the collective reduction scheme . Two collective measurement schemes $({\cal P},{\cal R})$ and $({\cal P}^{\prime},{\cal R}^{\prime})$ are said to be equivalent , in symbols $({\cal P},{\cal R})\cong({\cal P}^{\prime},{\cal R}^{\prime})$ , if ${\cal P}={\cal P}^{\prime}$ and ${\cal R}(\Delta,\rho)={\cal R}^{\prime}(\Delta,\rho)$ for all $\Delta\in{\cal B}(\Lambda)$ with $({\cal P}\rho)(\Delta)>0$ . [...]
  § 4. DAVIES-LEWIS POSTULATE: In what follows, we shall introduce some mathematical terminology independent of particular measurement theory. A superoperator for ${\cal H}$ is a bounded linear transformation on the space $\tau c({\cal H})$ of trace class operators on ${\cal H}$ . The dual of a superoperator $L$ is the dual superoperator $L^{*}$ defined by $\langle L^{*}A,\rho\rangle=\langle A,L\rho\rangle$ for all $A\in{\cal L}({\cal H})$ and $\rho\in\tau c({\cal H})$ , where $\langle\cdot,\cdot\rangle$ stands for the duality pairing defined by $\langle A,\rho\rangle=\mbox{\rm Tr}[A\rho]$ for all $A\in{\cal L}({\cal H})$ and $\rho\in\tau c({\cal H})$ . [...]
[4] arXiv:quant-ph/0012115v1 | Entropy and information gain in quantum continual measurements
  The theory of measurements continuous in time in quantum mechanics (quantum continual measurements) has been formulated by using the notions of instrument, positive operator valued measure, etc., by using quantum stochastic differential equations and by using classical stochastic differential equations (SDE's) for vectors in Hilbert spaces or for trace-class operators. In the same times Ozawa made
  Full text (https://arxiv.org/html/quant-ph/0012115v1), excerpts of its own sections:
  § 1 Introduction: The theory of measurements continuous in time in quantum mechanics (quantum continual measurements) has been formulated by using the notions of instrument, positive operator valued (POV) measure, etc. [ 1 , 2 ] , by using quantum stochastic differential equations [ 3 , 4 ] and by using classical stochastic differential equations (SDE’s) for vectors in Hilbert spaces or for trace-class operators [ 5 , 6 , 7 , 8 ] . In the same times Ozawa made developments in the theory of instruments [ 9 , 10 ] and introduced the related notions of a posteriori states [ 11 ] and of information gain [ 12 ] . In Section 2 we introduce a simple class of SDE’s relevant to the theory of continual measurements and we recall how they are related to instruments and a posteriori states and, so, to the general formulation of quantum mechanics [ 13 ] . In Section 3 we shall introduce and use the notion of information gain and the other results of paper [ 12 ] inside the theory of continual measurements.
  § 2 Stochastic differential equations and instruments: Let $\mathcal{H}$ be a separable complex Hilbert space, associated to the quantum system of interest. Let us denote by $\mathcal{B}(\mathcal{H})$ the space of bounded linear operators on $\mathcal{H}$ and by $\mathcal{T}(\mathcal{H})$ the trace-class on $\mathcal{H}$ , i.e. $\mathcal{T}(\mathcal{H})=\big\{\rho\in\mathcal{B}(\mathcal{H}):\|\rho\|\equiv\mathop{\mathrm{Tr}}\left\{\sqrt{\rho^{*}\rho}\right\} states ) on $\mathcal{H}$ . Commutators and anticommutators are denoted by $[\ ,\ ]$ and $\{\ ,\ \}$ , respectively. Let $H$ , $L_{j}$ , $S_{h}$ , $j,h=1,2,\ldots$ , be bounded operators on $\mathcal{H}$ such that $H=H^{\dagger}$ , $\sum_{j=1}^{\infty}L^{\dagger}_{j}L_{j}$ and $\sum_{h=1}^{\infty}S_{h}^{\dagger}S_{h}$ are strongly convergent in $\mathcal{B}(\mathcal{H})$ . [...]
  § 3 Entropy and information gain: In [ 12 ] a measurement is called quasi-complete if the a posteriori states are pure for every pure initial state and it is called complete if the a posteriori states are pure for every (pure or mixed) initial state. So, we call quasi-complete the continual measurement of Section 2 if the a posteriori states $\rho_{t}$ are pure ( $P_{\rho}$ -almost surely) for all $t$ and for all pure initial conditions $\rho$ . In [ 18 ] we proved that Theorem 1 The continual measurement of Section 2 is quasi-complete if and only if $\mathcal{L}_{1}=0$ and $\displaystyle\frac{J_{k}[\rho]}{\mathop{\mathrm{Tr}}\left\{J_{k}[\rho]\right\}}$ is a pure state for every $k$ and for every pure state $\rho$ . [...]
[5] arXiv:2307.09558v1 | Fitted avatars: automatic skeleton adjustment for self-avatars in virtual reality
  In the era of the metaverse, self-avatars are gaining popularity, as they can enhance presence and provide embodiment when a user is immersed in Virtual Reality. They are also very important in collaborative Virtual Reality to improve communication through gestures. Whether we are using a complex motion capture solution or a few trackers with inverse kinematics (IK), it is essential to have a good
  Full text (https://ar5iv.labs.arxiv.org/html/2307.09558v1), excerpts of its own sections:
  § Submission history: From: Jose Luis Ponton [ view email ] [v1] Fri, 14 Jul 2023 08:20:03 UTC (3,263 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Fitted avatars: automatic skeleton adjustment for self-avatars in virtual reality, by Jose Luis Ponton and 5 other authors View PDF view license
  § Current browse context:: cs.HC < prev | next > new | recent | 2023-07 Change to browse by: cs cs.GR
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[6] arXiv:1402.1217v2 | Entanglement, scaling, and the meaning of the wave function in protective measurement
  We examine the entanglement and state disturbance arising in a protective measurement and argue that these inescapable effects doom the claim that protective measurement establishes the reality of the wave function. An additional challenge to this claim results from the exponential number of protective measurements required to reconstruct multi-qubit states. We suggest that the failure of protecti
  Full text (https://arxiv.org/html/1402.1217v2), excerpts of its own sections:
  § I Theory of entanglement in protective measurement: Here we will go beyond the zeroth-order limit $T\rightarrow\infty$ usually considered in protective measurement ( Aharonov and Vaidman,, 1993 , Aharonov et al.,, 1993 , Dass and Qureshi,, 1999 ) and derive an expression for the final system–apparatus state to first order in $1/T$ . Consider two systems $S$ and $A$ described by self-Hamiltonians $H_{S}$ and $H_{A}$ , respectively. System $A$ plays the role of a measuring apparatus for $S$ , in the sense that we let $S$ and $A$ interact such that information about $S$ can be transferred to $A$ . The interaction is generated by the interaction Hamiltonian $\hat{H}_{I}(t)=g(t)\hat{P}\otimes\hat{O},$ (1) where $\hat{P}$ is the momentum operator of $A$ (the canonical conjugate to the position operator $\hat{X}$ ), and $\hat{O}$ is an arbitrary observable of the system $S$ . The function $g(t)$ , with $\int_{0}^{T}g(t)\,\text{d}t=1$ , describes the time-dependent strength of the interaction, with $g(t)=0$ for $t T$ . Thus, $T$ describes the duration of the measurement interaction. [...]
  § II Implications of entanglement in protective measurement: The finite system–apparatus entanglement arising in a protective measurement entails that protective measurements can never transcend the irreducibly probabilistic element inherent in any measurement of a (fully or partially) unknown quantum state. The problem is not only that the quantum state reconstructed from protective measurements may well be (unpredictably) different from the initial state of the system we had set out to measure. The problem is also that even on those occasions when the protective measurement succeeds—i.e., when the collapsed state of the apparatus pointer indicates the expectation value corresponding to the initial state of the system—we cannot infer from the readout of the pointer that we have indeed obtained information about the initial state of the system, rather than about any other state. This is so because there is no possibility of knowing whether we have succeeded : while the final pointer measurement may project the system back onto its initial state, the readout itself cannot tell us whether this has actually happened. [...]
  § III The scaling problem: We now turn our attention to the question of the number of protective measurements of expectation values required to (approximately) reconstruct a wave function; in particular, we will analyze how this number scales with the size of the system. [...]
  § V Concluding remarks: In response to Uffink’s ( 1999 ) criticism of protective measurement, Gao, (2011) writes: It seems that the errors in Uffink’s arguments were made at least partly due to his biased philosophical opinions. Why protect the interpretation of the wave function against protective measurements? Why make the different views on the meaning of the wave function peacefully coexist? Is it not very exciting and satisfying if we can decide the issue of the interpretation of the wave function someday? Is it not one of the ultimate objectives of our explorations in quantum foundations? To this, Uffink, (2012) replies: Of course, [I agree fully] with Gao that such an alternative view would be much more desirable. However, apart from the hot aspirations we might all have concerning the interpretation of quantum theory, we also need the cool breeze of critical analysis before we step forward. Uffink’s attitude, like our own, is not meant to be pessimistic. It merely reflects a realistic assessment of aims and means. [...]
[7] arXiv:quant-ph/9809038v1 | Quantum Turing Machines: Local Transition, Preparation, Measurement, and Halting
  Foundations of the theory of quantum Turing machines are investigated. The protocol for the preparation and the measurement of quantum Turing machines is discussed. The local transition functions are characterized for fully general quantum Turing machines. A new halting protocol is proposed without augmenting the halting qubit and is shown to work without spoiling the computation.
  Full text (https://arxiv.org/html/quant-ph/9809038v1), excerpts of its own sections:
  § QUANTUM TURING MACHINES: LOCAL TRANSITION, PREPARATION, MEASUREMENT, AND HALTING: School of Informatics and Sciences Nagoya University Chikusa-ku, Nagoya 4648601, Japan
  § INTRODUCTION: The Church-Turing thesis [ Chu36 , Tur36 ] states that to be computable is to be computable by a Turing machine and the modern discipline in computational complexity theory [ Pap94 ] states that to be efficiently computable is to be computable by a Turing machine within polynomial steps in the length of the input data. However, Feynman [ Fey82 ] pointed out that a Turing machine cannot simulate a quantum mechanical process efficiently and suggested that a computing machine based on quantum mechanics might be more powerful than Turing machines. Deutsch introduced quantum Turing machines [ Deu85 ] and quantum circuits [ Deu89 ] for establishing the notion of quantum algorithm exploiting “quantum parallelism”. A different approach to quantum Turing machines was investigated earlier by Benioff [ Beni80 ] . Bernstein and Vazirani [ BV97 ] instituted quantum complexity theory based on quantum Turing machines and showed constructions of universal quantum Turing machines. Yao [ Yao93 ] showed that a computation by a quantum Turing machine can be simulated efficiently by a quantum circuit. [...]
  § QUANTUM TURING MACHINES: A quantum Turing machine (QTM) ${\cal Q}$ is a quantum system consisting of a processor, a bilateral infinite tape, and a head to read and write a symbol on the tape. Its configuration is determined by the processor configuration $q$ from a finite set $Q$ of symbols, the tape configuration $T$ represented by an infinite string from a finite set $\Sigma$ of symbols, and the discretized head position $\xi$ , taking values in the set ${\bf Z}$ of integers. The tape consists of cells numbered by the integers and the head position $\xi$ is the place of the cell numbered by $\xi$ . We assume that $Q$ contains two specific symbols $q_{0}$ and $q_{f}$ representing the initial configuration and the final configuration of the processor and that $\Sigma$ contains the symbol $B$ representing the blank cell in the tape. For any integer $m$ the symbol at the cell $m$ on the tape is denoted by $T(m)$ . We assume that the possible tape configurations are such that $T(m)=B$ except for finitely many cells $m$ . The set of all the possible tape configurations is denoted by $\Sigma^{\#}$ . [...]
  § LOCAL TRANSITION FUNCTIONS: Deutsch [ Deu85 ] requires that the QTM operate finitely, i.e., (i) only a finite system is in motion during any one step, (ii) the motion depends only on the state of a finite subsystem, and (iii) the rule that specifies the motion can be given finitely in the mathematical sense. To satisfy the above requirement, the matrix elements of $U$ takes the following form * * * This condition is a natural extension of Deutsch’s condition [ Deu85 ] to the case where the head is not required to move. : $\displaystyle\langle q^{\prime},T^{\prime},\xi^{\prime}|U|q,T,\xi\rangle$ $\displaystyle=$ $\displaystyle[\delta_{\xi^{\prime}}^{\xi+1}D(q,T(\xi),q^{\prime},T^{\prime}(\xi),1)+\delta_{\xi^{\prime}}^{\xi}D(q,T(\xi),q^{\prime},T^{\prime}(\xi),0)$ (7) $\displaystyle\mbox{}+\delta_{\xi^{\prime}}^{\xi-1}D(q,T(\xi),q^{\prime},T^{\prime}(\xi),-1)]\prod_{m\not=\xi}\delta_{T(m)}^{T^{\prime}(m)}$ for any configurations $(q,T,\xi)$ and $(q^{\prime},T^{\prime},\xi^{\prime})$ . [...]
[8] QNFO: Continuum is Real
  For over a century, physics has been defined by an ontological schism. The continuous, deterministic, and local reality described by classical mechanics and general relativity stands in direct opposition to the discrete, probabilistic, and non-local phenomena of quantum mechanics. This division has necessitated a patchwork of competing interpretations, each burdened with paradoxes and philosophica
  Full text (https://papers.qnfo.org/papers/continuum-is-real), excerpts of its own sections:
  § The: Continuum is Real: Quantization as the Binning of a Continuous Reality **Author**: Rowan Brad Quni-Gudzinas **Affiliation**: QNFO **Email**: rowan.quni@qnfo.org **ORCID**: 0009-0002-4317-5604 **ISNI**: 0000000526456062 **DOI**: https://papers.qnfo.org/papers **Version**: 1.0 **Date**: 2025-09-18
  § 1.0: Introduction: A Proposed Resolution to the Ontological Crisis in Physics
  § 1.1: The Foundational Schism Between Classical and Quantum Ontologies For over a century, physics has been defined by an ontological schism. The continuous, deterministic, and local reality described by classical mechanics and general relativity stands in direct opposition to the discrete, probabilistic, and non-local phenomena of quantum mechanics. This division has necessitated a patchwork of competing interpretations, each burdened with paradoxes and philosophical compromises. This paper argues that this crisis stems from a fundamental misinterpretation of evidence, where observational artifacts have been mistaken for fundamental properties of reality. The central thesis is that the universe is not fundamentally quantized; rather, our interaction with the universe is quantized.
  § 1.1.1 The Classical: Paradigm of the Continuum The classical worldview, culminating in the 19th century, was a testament to the explanatory power of the continuum. Newtonian mechanics described a universe of deterministic trajectories, where the state of any system could be represented as a point \((x, p)\) in a continuous phase space, evolving smoothly in continuous time. Maxwell’s theory of electromagnetism modeled light and other radiation as continuous fields \((\mathbf{E}, \mathbf{B})\) governed by partial differential equations, with a smoothly varying energy density \(u = \frac{1}{2}\epsilon_0 E^2 + \frac{1}{2\mu_0} B^2\). Albert Einstein’s theory of general relativity provided the ultimate expression of this paradigm, describing spacetime itself as a four-dimensional differentiable manifold, a continuous fabric whose geometry is defined by a continuous metric field \(g_{\mu\nu}(x)\). In this triumphant framework, reality was seamless.
  § 1.1.2 The Quantum Paradigm: of the Discrete This continuous ontology was challenged by early 20th-century experiments. Max Planck’s resolution of the blackbody radiation problem required energy to be exchanged in discrete packets, \(E = nh\nu\) (Planck, 1901). [...]
  § 6.1 Summary: A Coherent: Quantum Ontology This framework resolves the ontological crisis in physics by correcting a foundational misdiagnosis. It establishes a coherent and empirically grounded ontology in which the universe is fundamentally a continuous, dynamic plenum of interacting fields. The discrete, quantized world we observe is not a reflection of an underlying pixelation of reality, but is instead an emergent phenomenon, an inevitable consequence of the universal process of **binning**, whereby physical constraints impose a discrete structure on this continuous substrate. Pillar I, The Continuum is Real, is supported by overwhelming empirical evidence from multiple domains of physics. Pillar II, Binning is Inevitable, explains the emergence of discreteness through the universal physical mechanism of resonance, mathematically described by the eigenvalue problem. Pillar III, “Quanta” are Labels, dissolves the misleading concept of the fundamental particle, re-interpreting quantum jumps and entanglement as informational phenomena related to the observation of a continuous field. [...]
[9] QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis
  Archive of the complete research record investigating the Post-Quantum Synthesis (PQS) framework: a neutral investigation of PQS's four sub-pillars mapped against external literature, plus an earlier-iteration analysis of AI gate-check convergence between Claude and Gemini evaluating PQS independently.
  Full text (https://papers.qnfo.org/papers/pqs-ai-evaluation-audit), excerpts of its own sections:
  § 2.1 Wave-Particle Duality and the Double-Slit Experiment: The double-slit experiment stands as the canonical example of quantum paradox, appearing to show that a single entity, such as an electron, is simultaneously a wave and a particle—a direct contradiction in classical terms. The PQS resolves this apparent contradiction by assigning wave-like and particle-like behaviors to their correct, non-contradictory domains, eliminating the duality.
  § 2.1.4 The “Which-Path” Experiment as an Alteration of the Physical System and Epistemic State: The paradox appears to deepen when a detector is placed at one of the slits to determine “which path” the electron took, causing the interference pattern to vanish. The PQS explains this phenomenon as a direct consequence of the physical nature of measurement, which inevitably alters the system. ##### 2.1.4.1 The Necessary Physical Interaction of the Path Detector To gain “which-path” information, the detector must physically interact with the field as it passes through a slit. This constitutes a measurement interaction as defined by Axiom II. This interaction inevitably and physically disturbs the continuous field, fundamentally altering its subsequent evolution toward the screen. ##### 2.1.4.2 The Consequent Update (Collapse) of the Knowledge State and Loss of Interference This physical interaction provides new information to the observer. If the detector at Slit A “clicks,” the observer must perform a Bayesian update on their knowledge state. This update effectively destroys the superposition, and the epistemic state is updated (or “collapses”) to be simply $\psi_A$. [...]
  § 2.4 The Born Rule as a Theorem of Epistemic Consistency: The Born Rule, stating that the probability of an outcome is the squared magnitude of its probability amplitude ($P(o_k) = |\langle o_k|\psi \rangle|^2$), is typically presented as a fundamental postulate of quantum mechanics. Within the PQS, this rule cannot be a postulate about reality; it must be a necessary consequence of the requirements of rational inference.
  § 2.4.2 Derivation from Rational Consistency Conditions via Gleason’s Theorem: The derivation relies on a powerful mathematical result, Gleason’s Theorem (Gleason, 1957), proving that any consistent probability assignment on the structure used to represent quantum knowledge (a Hilbert space) must take the form of the Born Rule. ##### 2.4.2.1 The Requirements of Non-Negativity, Normalization, and Non-Contextuality for a Probability Rule To be a valid probability assignment, any rule must satisfy basic consistency conditions: 1.  **Non-Negativity:** Probabilities must be real and non-negative. $f(\psi, P_k) \in \mathbb{R}_{\ge 0}$. 2.  **Normalization:** For any complete measurement context defined by a set of mutually orthogonal projectors $\{P_k\}$ where $\sum_k P_k = I$, the sum of probabilities for all possible outcomes must be 1. $$ \sum_k f(\psi, P_k) = 1 $$ 3.  **Non-Contextuality of Probabilities:** The probability assigned to an outcome $P_k$ should not depend on the other projectors in the specific orthogonal basis chosen for the measurement. It should only depend on the knowledge state $\psi$ and the projector $P_k$ itself. [...]
  § 4.2 The Problem of Consciousness as External to the Domain of Physics: The “Hard Problem of Consciousness”—why and how subjective experience arises from physical processes—has at times been erroneously linked to quantum mechanics, particularly through the idea that a “conscious observer” is needed to collapse the wavefunction. [...]
[10] QNFO: POST QUANTUM SYNTHESIS
  For over a century, physics has been captivated by a perceived intrinsic strangeness of the world, mistaking mathematical models for reality itself. This intellectual entanglement has given rise to persistent paradoxes, including wave-particle duality, wavefunction collapse, spooky action at a distance, and the elusive quantum-classical divide. The Post-Quantum Synthesis (PQS) presents an act of i
  Full text (https://papers.qnfo.org/papers/post-quantum-synthesis), excerpts of its own sections:
  § 7.4.3 Theorem 7.2 (No Physical: Collapse) There is no physical change to the continuous physical state \(\phi \in \mathcal{R}\) corresponding to “wavefunction collapse.” *Proof*: Consider the physical state evolution during a measurement: 1. **Initial physical state**: The system begins in a definite continuous physical state \(\phi_0 \in \mathcal{R}\). 2. **Interaction with detector**: The system’s field interacts with the detector’s fields, evolving continuously according to Hamiltonian dynamics: \(\phi(t) = \Phi_t(\phi_0) \in \mathcal{R}\). 3. **Amplification stage**: The continuous field \(\phi(t)\) triggers a threshold crossing within the detector, leading to a discrete outcome. 4. **Final physical state**: The system evolves to a final continuous physical state \(\phi_1 = \Phi_T(\phi_0) \in \mathcal{R}\). The entire process, from initial interaction to final physical state, is one of continuous Hamiltonian evolution within \(\mathcal{R}\). The “collapse” only affects the density operator \(\rho \in \mathcal{K}\) (the observer’s knowledge), not the physical state \(\phi \in \mathcal{R}\). \(\square\)
  § 7.5.3 Theorem 8.1 (No Spooky: Action) For any local operation performed solely on system \(\mathcal{R}_1\), the physical state of the spatially separated system \(\mathcal{R}_2\) remains unchanged. *Proof*: Let \(U_1\) be a local unitary operator acting only on \(\mathcal{R}_1\). The transformed joint state is: \[\phi_{12}' = (U_1 \otimes I)\phi_{12} = \sum_i c_i (U_1\phi_1^i) \otimes \phi_2^i\] To find the physical state of \(\mathcal{R}_2\), we consider its marginal density operator, obtained by tracing over the degrees of freedom of \(\mathcal{R}_1\): \[\rho_2 = \text{tr}_1(|\phi_{12}'\rangle\langle\phi_{12}'|) = \sum_i |c_i|^2 |\phi_2^i\rangle\langle\phi_2^i|\] This marginal state is identical to the marginal state of \(\mathcal{R}_2\) before \(U_1\) was applied to \(\mathcal{R}_1\). This demonstrates that local operations on one system have no instantaneous physical effect on the other, thus refuting “spooky action at a distance.” \(\square\)
  § 7.5.4 Theorem 8.2 (Correlation: History) The joint measurement statistics for two entangled systems satisfy: \[P(o_1, o_2) = \sum_i |c_i|^2 P_1(o_1|\phi_1^i)P_2(o_2|\phi_2^i)\] *Proof*: This follows directly from the Born rule applied to the epistemic state and the product structure of the physical states after separation. The correlations arise from the coefficients \(c_i\) established during the initial interaction, which encode the shared history. \(\square\)
  § 7.6.3 Theorem 9.1 (Redundancy: Threshold) There exists a critical number of environmental copies, \(N_0\), such that for any number of copies \(N > N_0\), the outcomes of measurements on the system become objective. *Proof*: By the quantum Chernoff bound, the probability of misidentifying the state of the system, based on an observation of the environment, decreases exponentially with \(N\): \[P_{\text{error}} \leq e^{-N\gamma}\] For some \(\gamma > 0\) that depends on the distinguishability of the environmental states. Thus, for \(N > N_0 = \frac{1}{\gamma}\log\frac{1}{\epsilon}\), the probability of error \(P_{\text{error}}\) becomes less than an arbitrarily small \(\epsilon\). This establishes a clear redundancy threshold for the emergence of objectivity. \(\square\)
  § 7.6.4 Theorem 9.2 (No Size: Dependence) The emergence of objectivity depends solely on the redundancy parameter \(N\) (the number of environmental copies), and not on the physical size or mass of the system itself. [...]
[11] QNFO: Principia Ontologica
  Human understanding operates through representational models rather than direct reality apprehension. Alfred Korzybski famously articulated this principle, noting that abstractions derived from perception necessarily differ from their source. Cognitive frameworks function as biological data-compression heuristics evolved for survival, not for producing perfect copies of an ultimate territory. Ever
  Full text (https://papers.qnfo.org/papers/principia-ontologica), excerpts of its own sections:
  § Information,: Non-Archimedean Geometry, and Semantic Self *A Framework for Cosmology, Consciousness, and Meaning*
  § 1.1 The Map-Territory: Distinction Human understanding operates through representational models rather than direct reality apprehension. Alfred Korzybski famously articulated this principle, noting that abstractions derived from perception necessarily differ from their source. Cognitive frameworks function as biological data-compression heuristics evolved for survival, not for producing perfect copies of an ultimate territory. Every scientific theory and philosophical system consequently constitutes a specialized map with inherent simplifications. These maps prove useful for navigation and prediction within specific domains of experience. Confusing the symbolic representation with the actual entity it references leads to significant categorical errors. Recognizing this distinction forms the essential first step toward epistemic humility. Historical examples repeatedly demonstrate the consequences of map-territory confusion. Medieval cosmological models placing Earth at the universe’s center reflected theological maps, not astronomical observations. [...]
  § 1.2 Biological Cognitive: Heuristics Cognitive systems evolved under stringent pressures for efficiency and adaptive utility. Neural tissue consumes disproportionate metabolic resources relative to other bodily functions. Natural selection therefore favors heuristic shortcuts that yield sufficiently accurate results with minimal computational cost. These shortcuts manifest as systematic biases in perception, memory, and reasoning. For example, visual processing assumes light comes from above, aiding three-dimensional object recognition. Auditory systems privilege human speech frequencies over other environmental sounds. Such biases are features, not flaws, within their evolutionary context. Pattern recognition constitutes a primary heuristic mechanism for navigating complex environments. The human brain excels at identifying familiar configurations in sensory data, sometimes detecting patterns where none exist. This tendency supports rapid threat assessment and opportunity identification. It also underlies superstition and conspiracy theorizing when applied indiscriminately. [...]
  § 1.3 The: Epistemological Knot of Self-Reference Any investigation of reality must confront the investigator’s situatedness within the subject of study. The observer cannot step outside the system being observed to achieve a perfectly objective viewpoint. This self-referential condition creates logical and empirical complexities across multiple disciplines. In physics, measurement instruments interact with quantum systems, affecting observed properties. In psychology, the act of introspection alters mental states being examined. Sociology faces the challenge of researchers influencing the societies they study. Self-reference is a structural condition of inquiry, not a mere procedural obstacle. Gödel’s incompleteness theorems mathematically formalized limitations arising from self-reference in formal systems. Any consistent axiomatic system capable of basic arithmetic contains true statements unprovable within the system. The system cannot demonstrate its own consistency without resorting to axioms outside itself. This result shattered Hilbert’s program for complete mathematical formalization. [...]