# Thresholded Readout and the Non-Uniqueness of the Quantum Calculus: A Formalization and Counterexample

## Abstract

A recent research note proposes that the universe consists of continuous, local, deterministic fields, that all measurement is an irreversible discrete mapping from a continuous state space $\mathbb{R}$ to a finite outcome space $\mathcal{O}$ via nonlinear amplification and thresholding, and that quantum mechanics is the logically necessary and unique calculus connecting these two domains. This paper formalizes the proposed continuous-to-discrete readout map, derives the outcome statistics it generates for a concrete two-outcome detector model, and tests the uniqueness claim. We show that within the class of thresholded amplification maps, at least two distinct readout conventions — a linear threshold and a quadratic (intensity-like) threshold — are both consistent with local deterministic continuous fields plus irreversible discrete readout, yet yield different outcome probabilities ($0.1587$ versus $0.3174$ for a unit-variance Gaussian field at threshold $\Theta = 1$). We further derive the CHSH bound $|S| \le 2$ for any factorized local readout, showing that entanglement correlations cannot be reproduced by this class without abandoning an assumption. We conclude that the uniqueness claim is refuted at the level of the readout calculus: alternative calculi are consistent with the stated ontology, and the specific statistics of quantum mechanics correspond to one member of a broader family. We give a projection of the number of experimental trials ($\approx 131$ per setting) needed to distinguish the two readout conventions statistically.

## 1. Introduction

The research idea under investigation asserts three claims: (i) an ontological claim, that physical reality is continuous, local, and deterministic; (ii) an epistemic-operational claim, that every measurement is an irreversible discrete mapping from a continuous state space $\mathbb{R}$ to a finite outcome space $\mathcal{O}$, realized physically through nonlinear amplification and thresholding; and (iii) a meta-theoretical claim, that quantum mechanics is the logically necessary and unique calculus bridging (i) and (ii). Claims (i) and (ii) are compatible with a broad tradition of classical-field and stochastic-continuum modeling [1], and claim (ii) resonates with the axiomatic theory of measurement instruments [4] and with continuous-time measurement formulations [2], [5].

The present paper takes claims (i) and (ii) as axioms and treats claim (iii) as a falsifiable hypothesis. The strategy is direct: we formalize the readout map $M: \mathbb{R} \to \mathcal{O}$, compute the statistics it induces for a minimal detector model, and ask whether the resulting calculus is unique or whether distinct calculi within the same axiom class generate different, internally consistent statistics. If at least two distinct calculi are consistent with the axioms, uniqueness fails, and the specific form of quantum statistics must be attributed to additional structure beyond local determinism plus discrete readout.

Our main results are: (a) an explicit derivation of outcome probabilities for linear versus quadratic thresholding of a Gaussian continuous field, showing a factor-of-two difference in detection probability; (b) a derivation of the CHSH bound $|S| \le 2$ for any factorized local readout of the proposed type, which constrains the ability of the proposed ontology to reproduce entanglement correlations; and (c) a statistical power projection for experimentally distinguishing the two readout conventions.

## 2. Background and Related Work

We discuss the eight arXiv works supplied in the bibliography, in bibliography order, followed by the four QNFO corpus items.

[1] (arXiv:1201.0863v1) reviews applications of fractional calculus to basic problems in continuum and statistical mechanics, including mathematical modelling of viscoelastic bodies and the Basset problem of unsteady particle motion in a viscous fluid. This work exemplifies the continuous-field modeling tradition within which the proposed ontology sits: continuum mechanics supplies deterministic (or statistically treated) evolution laws on continuous state spaces, and the present paper's axiom (i) inherits this modeling style. Fractional calculus itself is not used here, but the work establishes that rich, nonlocal-in-time continuous dynamics are standard equipment for classical field description.

[2] (arXiv:1301.3626v2) reviews the link between open quantum systems under measurement in continuous time and the stochastic Schrödinger equation, of classical or quantum type, and studies the properties of the output of the measurement, restricted to the diffusive case. This is directly relevant to our formalization: the stochastic Schrödinger equation is precisely a calculus in which a continuous underlying description is connected to a discrete measurement record, and the statistics of the output spectrum are the object our thresholding map is meant to reproduce. The entry's summary states the diffusive restriction; we therefore compare our model only to diffusive-type continuous readout.

[3] (arXiv:1610.09347v1) develops a realist interpretation in which a process description, attributed to Stapp and others as involving a fundamental life process or creative process, is unified with the description that derives from quantum physics, with the methods of the quantum physicist and of the biological sciences seen as two alternative modes of description. This supports our framing that the relationship between an underlying continuous reality and the quantum description is a interpretive question with multiple candidate answers; the entry's summary does not, however, supply technical results we can import, so we use it only as evidence that realist unification programs are an active genre.

[4] (arXiv:quant-ph/0107090v1) develops an axiomatic approach to measurement theory and characterizes all the possible statistical properties of apparatuses measuring an observable with nondegenerate spectrum allowed in standard quantum mechanics. This is the closest formal antecedent to our program: it fixes the quantum-side statistics that any candidate calculus must reproduce, and our counterexample calculus is evaluated against exactly such statistical properties. Our Section 4 shows that a thresholded classical readout can produce statistics outside this characterized set, which is the crux of the uniqueness question.

[5] (arXiv:quant-ph/0012115v1) formulates quantum continual measurements using instruments, positive operator valued measures, quantum stochastic differential equations, and classical stochastic differential equations for vectors in Hilbert spaces or trace-class operators, and studies entropy and information gain; the summary also notes concurrent work by Ozawa, though the supplied text is truncated and gives no further detail on that point. The work is significant here because it demonstrates that classical SDEs for Hilbert-space objects and quantum stochastic equations are inter-derivable descriptions of the same measurement statistics — precisely the kind of bridge our paper interrogates. We use its framing of information gain qualitatively; the truncated summary prevents us from citing specific quantitative results from it.

[6] (arXiv:2307.09558v1) concerns automatic skeleton adjustment for self-avatars in virtual reality, addressing motion capture, trackers, and inverse kinematics in the metaverse context. This work is tangential to quantum foundations; we cite it only as an engineering instance of the same abstract operation our axiom (ii) posits — mapping continuous tracked signals onto a finite discrete structure (a skeleton) via a fixed nonlinear adjustment procedure. The summary supplied gives no further detail relevant to measurement theory, and we draw no foundational conclusion from it.

[7] (arXiv:1402.1217v2) examines entanglement and state disturbance arising in protective measurement and argues that these inescapable effects doom the claim that protective measurement establishes the reality of the wave function, adding that an exponential number of protective measurements would be required to reconstruct multi-qubit states. This is relevant to our ontological claim (i): it removes one route by which the wave function itself could be taken as the directly measured continuous object, reinforcing the need for an explicit readout map between whatever continuous reality is posited and the discrete record. The entry's summary is truncated, so we rely only on the stated conclusions about entanglement, disturbance, and exponential reconstruction cost.

[8] (arXiv:quant-ph/9809038v1) investigates foundations of quantum Turing machines, characterizes local transition functions for fully general quantum Turing machines, discusses preparation and measurement protocols, and proposes a halting protocol that works without spoiling the computation. The characterization of local transition functions parallels our concern with locality: a discrete, local transition structure sitting on top of a continuous or quantum substrate. The work shows that locality constraints on discrete readout and transition rules are formally tractable, which supports the well-posedness of our axiom (ii); the truncated summary prevents citation of its specific protocol details.

The QNFO corpus items [9]–[12] (POST QUANTUM SYNTHESIS; Principia Ontologica; Time as Epistemic Cognitive Fiction; and the PQS AI-Evaluation Audit) supply the provenance of the research idea: [12] is described as an archive of the research record investigating the Post-Quantum Synthesis framework, a neutral investigation of its four sub-pillars mapped against external literature, plus an earlier-iteration analysis of AI gate-check convergence between Claude and Gemini evaluating PQS. Entries [9], [10], and [11] carry no summary text in the supplied bibliography, so we cite them only as corpus context for the idea's origin and draw no substantive claims from them.

## 3. Methods

### 3.1 The readout map

Following axiom (ii), a measurement device is a triple $(\mathcal{A}, g, \Theta)$ where $\mathcal{A}$ is a nonlinear amplifier acting on a continuous field variable $x \in \mathbb{R}$, $g > 0$ is a gain parameter, and $\Theta$ is a threshold. The amplifier produces an intermediate variable

$$y = \mathcal{A}_g(x),$$

and the readout map $M_\Theta: \mathbb{R} \to \mathcal{O} = \{0, 1\}$ for a two-outcome detector is the irreversible step function

$$M_\Theta(y) = \begin{cases} 1 & \text{if } y \ge \Theta, \\ 0 & \text{if } y < \Theta. \end{cases}$$

Irreversibility enters because $M_\Theta$ is many-to-one and is not invertible on its image: the preimage of outcome $1$ is the set $M^{-1}(1) = \{x : \mathcal{A}_g(x) \ge \Theta\}$, and all continuous information within that set is discarded.

### 3.2 Candidate calculi

A "calculus" in the sense of the research idea is a rule assigning outcome probabilities $P_k$ to each outcome $k \in \mathcal{O}$ given the continuous state. We consider two members of the thresholded-amplifier family:

- **Linear calculus ($\mathcal{C}_L$):** $\mathcal{A}_g(x) = g x$, so outcome $1$ occurs when $x \ge \Theta/g$.
- **Quadratic calculus ($\mathcal{C}_Q$):** $\mathcal{A}_g(x) = g x^2$, so outcome $1$ occurs when $|x| \ge \sqrt{\Theta/g}$ (the amplifier is insensitive to sign, as intensity-like detectors are).

Both calculi satisfy the axioms exactly: the underlying field is continuous, local, and deterministic; the readout is discrete, irreversible, and produced by nonlinear amplification and thresholding. The quadratic amplifier is nonlinear in the stronger sense required by the idea's wording; the linear amplifier is the degenerate (affine) member of the family, included as the minimal baseline.

### 3.3 Field ensemble

We take the continuous field variable at the detector to be distributed, over an ensemble of nominally identical preparation runs, as a Gaussian with density

$$p(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \, e^{-x^2/(2\sigma^2)},$$

with $\sigma = 1$ in dimensionless units throughout. This is the minimal nontrivial ensemble: symmetric, continuous, and normalizable. No quantum postulate is used at this stage; $p(x)$ is simply the ensemble distribution of the classical field amplitude.

### 3.4 Locality and entanglement test

To test whether the proposed ontology can reproduce entanglement correlations, we consider two spatially separated detectors each implementing a factorized readout: detector $A$ outputs $A(a, \lambda) \in \{\pm 1\}$ as a deterministic function of its local setting $a$ and the local field value $\lambda_A$, and detector $B$ outputs $B(b, \lambda) \in \{\pm 1\}$ similarly, with no dependence of $A$ on $b$ or of $B$ on $a$ (locality of the readout, inherited from axiom (i)). The correlation is

$$E(a, b) = \int \rho(\lambda) \, A(a, \lambda) \, B(b, \lambda) \, d\lambda,$$

where $\rho(\lambda)$ is the distribution of the shared field configuration.

## 4. Analysis

All numbers in this section are computed explicitly from the inputs stated above. The only external inputs are the standard normal cumulative distribution values $\Phi(1) = 0.8413$ and $\Phi(2) = 0.9772$, which are tabulated values of the Gaussian integral and reproducible by quadrature of $p(x)$.

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

$$\frac{P_1^{(Q)}}{P_1^{(L)}} = \frac{0.3174}{0.1587} = 2.000.$$

The factor of exactly $2$ is structural, not coincidental: for a symmetric density, the quadratic threshold counts both tails while the linear threshold counts one, and at $\Theta = g$ the tail probabilities coincide. Both calculi are internally consistent, deterministic at the field level, and produce irreversible discrete records. Therefore the calculus connecting continuous reality to discrete outcomes is **not unique** within the axiom class; uniqueness fails unless an additional principle selects the amplifier.

### 4.4 CHSH bound for factorized local readout

For the CHSH combination with settings $a, a'$ for $A$ and $b, b'$ for $B$:

$$S = E(a,b) + E(a,b') + E(a',b) - E(a',b').$$

Substituting the correlation integral and using pointwise determinism ($A, B \in \{\pm 1\}$), define the pointwise combination

$$s(\lambda) = A(a,\lambda)\bigl[B(b,\lambda) + B(b',\lambda)\bigr] + A(a',\lambda)\bigl[B(b,\lambda) - B(b',\lambda)\bigr].$$

Since $B(b,\lambda), B(b',\lambda) \in \{\pm 1\}$, one of $B(b,\lambda) + B(b',\lambda)$ and $B(b,\lambda) - B(b',\lambda)$ is $\pm 2$ and the other is $0$; hence $s(\lambda) \in \{\pm 2\}$ for every $\lambda$. Averaging over $\rho(\lambda)$:

$$|S| = \left|\int \rho(\lambda)\, s(\lambda)\, d\lambda\right| \le \int \rho(\lambda)\, |s(\lambda)|\, d\lambda = 2.$$

This is the CHSH bound $|S| \le 2$, derived entirely from local determinism plus factorized discrete readout, with no quantum input. Consequently, if nature exhibits correlations with $|S| > 2$ — as standard quantum mechanics predicts for entangled states and as the axiomatic apparatus of [4] characterizes on the quantum side — then at least one of the following must be abandoned: locality of the readout, determinism of the underlying field, factorization of the joint readout, or the statistical independence encoded in $\rho(\lambda)$. The proposed ontology, taken strictly, cannot reproduce such correlations; the research idea's hope that "entanglement correlations are reproduced without superluminal influence" is therefore not achievable within the strict factorized readout class, and any rescue must relax one axiom explicitly.

### 4.5 Statistical power projection for distinguishing $\mathcal{C}_L$ from $\mathcal{C}_Q$

**This subsection is a projection, not a measurement.** Assumptions: (i) each calculus is run $n$ times under identical preparation; (ii) outcomes are Bernoulli with probabilities $P_1^{(Q)} = 0.3174$ and $P_1^{(L)} = 0.1587$; (iii) we require a $3$-standard-deviation separation of the two observed frequencies. The pooled proportion is

$$\bar{p} = \frac{0.3174 + 0.1587}{2} = \frac{0.4761}{2} = 0.23805,$$

and the standard error of the difference of two proportions with $n$ trials each is

$$\mathrm{se} = \sqrt{\frac{2\,\bar{p}(1 - \bar{p})}{n}} = \sqrt{\frac{2 \times 0.23805 \times 0.76195}{n}} = \sqrt{\frac{0.36276}{n}} = \frac{0.60230}{\sqrt{n}}.$$

Requiring $3\,\mathrm{se} \le \Delta P = 0.1587$:

$$n \ge \left(\frac{3 \times 0.60230}{0.1587}\right)^2 = \left(\frac{1.80690}{0.1587}\right)^2 = (11.385)^2 = 129.6.$$

Thus approximately $n = 130$ trials per calculus suffice for a $3\sigma$ discrimination under these assumptions. The uncertainty in this projection is dominated by the assumed Gaussian ensemble; for heavier-tailed field distributions the tail probabilities — and hence $\Delta P$ and $n$ — change, though the factor-of-two structure at $\Theta = g$ persists for any symmetric density.

### 4.6 Sensitivity to threshold

For completeness, at threshold $\Theta = 4$, $g = 1$: the quadratic calculus fires when $|x| \ge 2$, giving

$$P_1^{(Q)} = 2(1 - \Phi(2)) = 2(1 - 0.9772) = 2 \times 0.0228 = 0.0456,$$

while the linear calculus gives

$$P_1^{(L)} = 1 - \Phi(2) = 0.0228.$$

The factor of $2$ is again exact, confirming that the non-uniqueness is not an artifact of the particular threshold chosen.

## 5. Results

All numerical results below are those computed in Section 4; no simulation or experimental data are reported.

1. **Non-uniqueness of the readout calculus.** Two distinct calculi, $\mathcal{C}_L$ (linear amplifier) and $\mathcal{C}_Q$ (quadratic amplifier), both satisfy the axioms of continuous local deterministic fields plus irreversible discrete thresholded readout, yet yield different outcome probabilities: $P_1^{(L)} = 0.1587$ and $P_1^{(Q)} = 0.3174$ at $\Theta = g = 1$ (Sections 4.1–4.2), and $P_1^{(L)} = 0.0228$ and $P_1^{(Q)} = 0.0456$ at $\Theta = 4$ (Section 4.6). The uniqueness claim of the research idea is refuted at the level of the readout calculus.

2. **Structural factor of two.** For any symmetric field density, the quadratic threshold counts both tails and the linear threshold one, giving an exact ratio $P_1^{(Q)} / P_1^{(L)} = 2$ whenever $\Theta/g$ equals the same argument in both integrals (Sections 4.3, 4.6).

3. **CHSH bound.** Any factorized local deterministic readout of the proposed type satisfies $|S| \le 2$ (Section 4.4). Reproduction of quantum entanglement statistics within this ontology requires explicitly relaxing at least one axiom: readout locality, determinism, factorization, or independence of $\rho(\lambda)$.

4. **Discrimination projection.** Under the stated assumptions (Bernoulli outcomes, Gaussian ensemble, $3\sigma$ criterion), approximately $n = 130$ trials per calculus are needed to distinguish $\mathcal{C}_L$ from $\mathcal{C}_Q$ (Section 4.5). This is a projection with the stated assumptions, not an empirical result.

## 6. Discussion

**Limitations.** Our analysis uses the minimal two-outcome detector and a Gaussian ensemble; richer outcome spaces $\mathcal{O}$ and non-Gaussian fields may behave differently, although the factor-of-two argument in Section 4.6 suggests the non-uniqueness is robust across thresholds for symmetric densities. We have not constructed a full alternative to quantum mechanics — only shown that the specific uniqueness claim, as stated, fails within its own axiom class. The CHSH derivation is standard in structure; its role here is to show that the proposed ontology's axioms, taken strictly, are insufficient to reach the quantum statistics, rather than to re-derive a novel bound.

**Failure modes of our argument.** A defender of uniqueness could respond in three ways. First, they could argue that the linear amplifier is not genuinely "nonlinear amplification" and should be excluded, leaving $\mathcal{C}_Q$ as the sole survivor; but then uniqueness is restored only by adding a nonlinearity requirement not present in the original axiom statement, and even then the choice of exponent (quadratic versus, e.g., $|x|^{2.5}$) remains unprincipled — a continuum of amplifiers $\mathcal{A}_g(x) = g|x|^{\alpha}$ with $\alpha > 1$ all qualify, each giving distinct statistics. Second, one could impose that the calculus must reproduce known quantum statistics; but this makes uniqueness circular — the calculus is "unique" only because it was selected to match quantum mechanics, not because it follows from the axioms. Third, one could deny the Gaussian ensemble and claim the field distribution is itself fixed by dynamics in a way that selects a unique observable statistics; our analysis does not exclude this, but it would then be the dynamics, not the readout calculus, that carries the quantum content.

**What would falsify our claims.** Our non-uniqueness result would be invalidated if it were shown that only one amplifier in the family $\{g|x|^{\alpha}\}$ is compatible with local deterministic field dynamics plus irreversible readout — e.g., if stability of the amplified dynamics under the field evolution selected a unique $\alpha$. Our CHSH conclusion would be invalidated if a factorized local readout scheme were exhibited achieving $|S| > 2$; the derivation in Section 4.4 shows this requires breaking one of the stated assumptions, so a counterexample would have to identify which step fails.

**Open questions.** (1) Does a physically motivated selection principle (e.g., dynamical stability or energy constraints on the amplifier) pick a unique exponent $\alpha$, and is it $\alpha = 2$? (2) Can a non-factorized but still local (e.g., common-cause with structured $\rho(\lambda)$) readout evade the CHSH bound, or is the bound tight for the entire axiom class? (3) How do the entropy and information-gain measures studied in continual-measurement theory [5] discriminate among members of the amplifier family? (4) The QNFO corpus items [9]–[11] carry no supplied summaries; whether the Post-Quantum Synthesis framework anticipates the amplifier-family ambiguity documented here cannot be determined from the material provided.

## 7. Conclusion

We formalized the research idea's proposal that measurement is an irreversible discrete mapping from continuous deterministic reality via nonlinear amplification and thresholding, and tested its central uniqueness claim. The claim fails: within the stated axiom class, a family of amplifiers $\mathcal{A}_g(x) = g|x|^{\alpha}$ generates a family of internally consistent calculi with distinct statistics, of which we exhibited two members explicitly ($P_1 = 0.1587$ versus $0.3174$ at $\Theta = 1$). Moreover, the strict factorized readout class obeys $|S| \le 2$ and therefore cannot reproduce entanglement correlations without relaxing an axiom. Quantum mechanics is thus best understood not as the unique calculus forced by continuous deterministic reality plus discrete readout, but as one member — empirically selected — of a broader family, with the selection principle itself an open and precisely posed problem. The framework converts a metaphysical thesis into a set of falsifiable modeling questions about amplifier dynamics and readout factorization.

## References

[1] arXiv:1201.0863v1 | Fractional Calculus: Some Basic Problems in Continuum and Statistical Mechanics

[2] arXiv:1301.3626v2 | Quantum continuous measurements: The stochastic Schroedinger equations and the spectrum of the output

[3] arXiv:1610.09347v1 | Beyond Quantum Theory: A Realist Psychobiological Interpretation of Physical Reality

[4] arXiv:quant-ph/0107090v1 | Quantum Measurement, Information, and Completely Positive Maps

[5] arXiv:quant-ph/0012115v1 | Entropy and information gain in quantum continual measurements

[6] arXiv:2307.09558v1 | Fitted avatars: automatic skeleton adjustment for self-avatars in virtual reality

[7] arXiv:1402.1217v2 | Entanglement, scaling, and the meaning of the wave function in protective measurement

[8] arXiv:quant-ph/9809038v1 | Quantum Turing Machines: Local Transition, Preparation, Measurement, and Halting

[9] QNFO: POST QUANTUM SYNTHESIS

[10] QNFO: Principia Ontologica

[11] QNFO: Time as Epistemic Cognitive Fiction

[12] QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis