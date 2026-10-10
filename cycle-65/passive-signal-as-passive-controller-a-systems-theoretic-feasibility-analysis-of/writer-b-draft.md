# Re-entry as a Passive Control System: A Formal Feasibility Analysis of the "Signal" Hypothesis in the QNFO Corpus

## Abstract

The QNFO corpus proposes a Signal-Worker (S-W) ontology in which the boson is interpreted as a *signal* — a delocalized field instruction — and the fermion as a *worker* — the localized state that performs work. A companion re-entry document (DOI 10.5281/zenodo.18515457) poses the engineering question of whether the Signal can be made to function as a passive control system. This paper formalizes that question in the standard language of passivity-based control. We treat the Signal as a discrete-time controller block and ask under what conditions the closed Signal-Worker loop satisfies a dissipation inequality. We derive, with full arithmetic, (i) the exact passivity of a discrete integrator under a modified output $y_k = x_k + \frac{1}{2}u_k$, (ii) the output transformation $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ that renders a leaky integrator passive with an explicit dissipation rate $-0.095\,x_k^2$ for leakage $\alpha = 0.1$, verified numerically step by step, and (iii) a worst-case passivity degradation bound of $5.0$ energy units over $N = 100$ steps under actuator quantization with resolution $q = 0.1$. We situate the analysis against eight works from the provided control- and quantum-control literature and against the two QNFO corpus documents. We conclude that the Signal-as-passive-controller hypothesis is well-posed and internally consistent at the level of abstract block diagrams, but that the corpus documents supplied contain no dynamical equations, so no physical validation is possible from the provided material alone.

## 1. Introduction

The QNFO corpus is a collection of documents that propose a reinterpretation of quantum phenomena through a decomposition it calls the Signal-Worker (S-W) ontology. According to the corpus document on Signal-Worker boundary confinement [10], the ontology assigns the boson the role of *signal* — "the delocalized field instruction" — and the fermion the role of *worker* — "the localized state that performs work" — and presents this as a proposed decomposition of what the corpus calls the "wave–particle duality fog." A second corpus document addresses structural versus driven quantum coherence [9]; the summary supplied for that entry gives no further detail, so we can relate to it only through its title and identifier.

The present paper responds to a re-entry document in the same corpus, DOI 10.5281/zenodo.18515457, which — as stated in the grounding input — is "engineered to function as a passive control system ('Signal')." The engineering question is therefore: can the Signal, in the S-W ontology, be modeled as a *passive* control system in the precise sense used in systems and control theory?

Passivity is a standard notion: a system is passive if it cannot produce more energy than is supplied to it, formalized by a dissipation inequality involving a nonnegative *storage function* and a *supply rate* (defined in Section 3). Passivity is attractive as an engineering requirement because passive blocks composed in feedback remain stable, a property exploited across the control literature, from data-driven controller design [1] to control over delayed communication channels [2].

Our contribution is deliberately modest and methodological. We do not claim that the S-W ontology is physically correct, and we do not import any physics beyond what the corpus entries state. Instead we:

1. Translate the Signal-Worker re-entry question into a well-posed block-diagram problem with a dissipation inequality.
2. Derive, with every arithmetic step shown, the conditions under which candidate Signal dynamics (a pure integrator and a leaky integrator) satisfy discrete-time passivity, including the exact output transformations required.
3. Derive a worst-case bound on how actuator quantization — a realistic implementation constraint — degrades passivity, connecting to the sampled-data quantized-control literature [3].
4. Identify precisely what evidence would be required from the corpus to confirm or falsify the hypothesis, and what in the provided material is missing.

The paper is organized as follows. Section 2 reviews the provided bibliography. Section 3 defines the formal problem. Section 4 carries out the derivations with explicit arithmetic. Section 5 states the results. Section 6 discusses limitations and failure modes. Section 7 concludes.

## 2. Background and Related Work

We discuss all ten provided bibliography entries. Statements about each work are restricted to what its supplied summary states.

**[1] Passive iFIR Filters for Data-Driven Control (arXiv:2403.06640v2).** This work designs a new class of passive controllers formed by the parallel action of an integrator and a finite impulse response (FIR) filter. The summary states that these "iFIR" controllers are more expressive than PID controllers while retaining their features and simplicity, that a model-free data-driven design is provided based on virtual reference feedback tuning, and that passivity is enforced through constraints (the summary text is truncated at this point). This is directly relevant to our problem: the Signal block we analyze in Section 4 is exactly an integrator, and [1] shows that integrator-based structures can be made passive by construction and tuned from data without a model. If the Signal is to be engineered rather than merely postulated, the iFIR design pattern is the closest supplied template.

**[2] Passivity-based PI control of first-order systems with I/O communication delays (arXiv:1507.01146v1).** This work revisits PI control of first-order linear passive systems through a delayed communication channel, using the relative stability concept called sigma-stability. The delayed channel is treated as a transport PDE, passivity of the overall loop is guaranteed, and the resulting closed-loop system is of neutral type; spectral methods are then applied (the summary is truncated mid-sentence). For the Signal-Worker question, this matters because the S-W ontology separates the delocalized signal from the localized worker — geometrically, a separation across a boundary. If the Signal acts on the Worker across any spatial extent, a transport delay is the minimal model of that separation, and [2] shows that passivity can survive such delays when the channel is modeled as a transport PDE.

**[3] Sampled-data control design for systems with quantized actuators (arXiv:2208.05694v3).** This work designs sampled-data state feedback for continuous-time linear systems with uniform input quantization, ensuring uniform global asymptotic stability of an attractor surrounding the origin by rewriting the closed loop as a hybrid dynamical system, using an auxiliary construction (summary truncated). This motivates our quantization analysis in Section 4.3: any engineered Signal will be implemented in discrete time with finite-resolution actuation, and [3] establishes the standard framework — stability of an attractor around, rather than at, the origin — under exactly those conditions.

**[4] Bringing Quantum Systems under Control (arXiv:2412.00736v1).** This tutorial connects quantum computing to bilinear control systems. It states that quantum computing has potential in cryptography, simulation, optimization, and machine learning, that new algorithms with unprecedented capabilities can be developed, and that experimental realization of quantum devices is an active field of research (summary truncated). We cite it as the supplied bridge between control theory and quantum systems: it frames the general question of how control-theoretic concepts apply to quantum hardware, which is the category of question the Signal-Worker re-entry poses.

**[5] On the infeasibility of entanglement generation in Gaussian quantum systems via classical control (arXiv:1107.3174v1).** This work uses a system-theoretic approach to show two negative results: classical linear time-invariant controllers cannot generate steady-state entanglement in a bipartite Gaussian quantum system initialized in a Gaussian state, and cannot generate entanglement in finite time from a separable Gaussian initial state (summary truncated). This is an important caution for our hypothesis: system-theoretic controller classes, of exactly the kind we formalize for the Signal, have provable limits on what they can do to quantum systems. If the Signal is a classical passive controller, results of the type in [5] delimit what Signal-mediated effects can and cannot produce.

**[6] Composite Adaptive Control Barrier Functions for Safety-Critical Systems with Parametric Uncertainty (arXiv:2601.17683v3).** This work addresses the fact that control barrier functions (CBFs) — certificates that guarantee safety but require accurate system models — lose their guarantees under parametric uncertainty. It notes that robust methods maintain safety via worst-case bounds at the cost of performance, while modular learning schemes decouple estimation from safety and risk constraint violations during transients, and presents the composite adaptive CBF approach (summary truncated). We invoke this pattern in Section 6: the Signal-Worker hypothesis is a model-dependent safety-like claim, and [6] illustrates the standard taxonomy of responses (robust worst-case versus adaptive/learning) when the model is uncertain — which, for the corpus, it certainly is.

**[7] Robust Nonlinear Optimal Control via System Level Synthesis (arXiv:2301.04943v3).** This work treats finite-horizon constrained robust optimal control for nonlinear systems with norm-bounded disturbances by decomposing the uncertain nonlinear system, via a first-order Taylor expansion, into a nominal system and an error described as an uncertain linear time-varying system, leveraging system level synthesis (summary truncated). This supplies the decomposition pattern we adopt methodologically: separate a nominal closed loop (Signal driving Worker) from a deviation term, and analyze robustness of the nominal part — the approach we take when we ask what the passivity guarantee tolerates.

**[8] Using quantum computers in control: interval matrix properties (arXiv:2403.17711v1).** This work explores the use of quantum computers for problems in systems and control theory, noting that quantum algorithms have been developed for binary optimization, which plays a role in various control problems (summary truncated). We cite it as the reverse direction of [4]: control problems posed to quantum computers. It is relevant to the corpus context because the QNFO documents concern quantum coherence, and [8] shows that the control-quantum interface is being explored in both directions in the supplied literature.

**[9] QNFO: Structural vs Driven Quantum Coherence (DOI 10.5281/zenodo.18441401).** The summary supplied for this entry is empty; it gives no further detail beyond the title. We therefore use it only as evidence that the corpus distinguishes *structural* from *driven* coherence — a distinction that, read against the title alone, suggests the corpus already separates passive (structural) from actively driven behavior, the same distinction passivity theory formalizes. Beyond that reading of the title, we make no claims about this document.

**[10] QNFO: Signal-Worker Boundary Confinement (DOI 10.5281/zenodo.21974194).** This entry supplies the core ontology: the boson is the *signal*, "the delocalized field instruction," and the fermion is the *worker*, "the localized state that performs work." The entry describes itself as "the red-team-hardened correction" of the ontology. This is the primary source for the Signal-Worker decomposition that the re-entry document asks us to treat as a passive control system. Notably, the ontology's own vocabulary — instruction (input), worker (actuator/state), boundary (channel) — maps naturally onto the control-theoretic triples of input, plant, and interconnection, which is the mapping we formalize in Section 3.

## 3. Methods

### 3.1 Definitions

**Discrete-time passivity.** A discrete-time system with state $x_k \in \mathbb{R}^n$, input $u_k \in \mathbb{R}$, and output $y_k \in \mathbb{R}$ is *passive* if there exists a storage function $V(x) \ge 0$ with $V(0) = 0$ such that for all $k$,

$$V(x_{k+1}) - V(x_k) \le u_k\, y_k.$$

The right-hand side $u_k y_k$ is the *supply rate*: the power injected at step $k$. Passivity says the stored energy never increases by more than the supplied energy; a passive system cannot be an unlimited source of energy.

**Strict passivity with dissipation rate.** If moreover

$$V(x_{k+1}) - V(x_k) \le u_k\, y_k - \delta\, x_k^2$$

for some $\delta > 0$, the system is strictly passive with dissipation rate $\delta$: stored energy decreases strictly whenever the state is nonzero and no supply is injected.

**Block interpretation of the S-W ontology.** We map the corpus ontology [10] onto a control block diagram as follows:

```text
  u_k (instruction) ──► [ SIGNAL ] ──y_k──► [ WORKER ] ──► work output
                          (delocalized)       (localized state)
```

The Signal is the controller block; the Worker is the driven plant. The re-entry question — is the Signal a *passive* control system? — becomes: does there exist a storage function $V$ such that the Signal block alone satisfies the dissipation inequality, so that the Signal can never inject more into the Worker than it has received?

### 3.2 Candidate Signal dynamics

Because the corpus documents supply no equations, we analyze the two minimal candidate dynamics for a Signal whose role is to *accumulate and relay an instruction*:

- **Pure integrator (undriven relay):**
$$x_{k+1} = x_k + u_k.$$
- **Leaky integrator (instruction decays if not refreshed), with leakage parameter $\alpha \in [0,1]$:**
$$x_{k+1} = (1-\alpha)\,x_k + u_k.$$

The natural storage function for both is the quadratic $V(x) = \frac{1}{2}x^2$, representing the accumulated instruction magnitude. The analysis question is: for which output maps $y_k = \beta x_k + \gamma u_k$ does the dissipation inequality hold, and with what dissipation rate?

### 3.3 Perturbation analysis under quantization

Following the motivation of [3], we then ask how uniform input quantization of resolution $q$ (the actuator can only apply values on a grid of spacing $q$, so the applied input $u_k^{q}$ satisfies $|u_k - u_k^{q}| \le \frac{q}{2}$) degrades the passivity inequality, and we bound the degradation over a finite horizon.

## 4. Analysis

Every input number below is either a structural constant of the candidate dynamics or an explicitly stated assumption. All arithmetic is shown.

### 4.1 Exact passivity of the pure integrator

**Setup.** Dynamics $x_{k+1} = x_k + u_k$; storage $V(x) = \frac{1}{2}x^2$; candidate output $y_k = \beta x_k + \gamma u_k$.

**Step 1: expand the storage change.**

$$V(x_{k+1}) - V(x_k) = \frac{1}{2}(x_k + u_k)^2 - \frac{1}{2}x_k^2 = x_k u_k + \frac{1}{2}u_k^2.$$

**Step 2: state the passivity requirement.** We need

$$x_k u_k + \frac{1}{2}u_k^2 \le u_k(\beta x_k + \gamma u_k) = \beta x_k u_k + \gamma u_k^2$$

for all $(x_k, u_k)$. Rearranging,

$$(1-\beta)\,x_k u_k + \left(\frac{1}{2}-\gamma\right)u_k^2 \le 0 \quad \text{for all } x_k, u_k.$$

**Step 3: solve the coefficients.** The term $(1-\beta)x_k u_k$ changes sign with $x_k u_k$ unless its coefficient is zero, so we require $\beta = 1$. Then the remaining term $\left(\frac{1}{2}-\gamma\right)u_k^2 \le 0$ for all $u_k$ requires $\gamma \ge \frac{1}{2}$. The minimal (exactly passive) choice is

$$\boxed{y_k = x_k + \frac{1}{2}u_k,}$$

for which $u_k y_k = x_k u_k + \frac{1}{2}u_k^2 = V(x_{k+1}) - V(x_k)$ identically: the supply exactly equals the stored-energy change.

**Numerical verification.** Take $x_0 = 0$, $u_0 = 0.1$. Then $x_1 = 0 + 0.1 = 0.1$; $V(x_1) = \frac{1}{2}(0.1)^2 = 0.005$; $V(x_0) = 0$; so $\Delta V = 0.005 - 0 = 0.005$. The modified output is $y_0 = 0 + \frac{1}{2}(0.1) = 0.05$, and the supply is $u_0 y_0 = 0.1 \times 0.05 = 0.005$. Supply equals storage change exactly, confirming exact passivity.

### 4.2 Passivity of the leaky integrator

**Setup.** Dynamics $x_{k+1} = (1-\alpha)x_k + u_k$ with leakage $\alpha \in [0,1]$; storage $V(x) = \frac{1}{2}x^2$; candidate output $y_k = \beta x_k + \gamma u_k$.

**Step 1: expand the storage change.**

$$V(x_{k+1}) - V(x_k) = \frac{1}{2}\left[(1-\alpha)x_k + u_k\right]^2 - \frac{1}{2}x_k^2.$$

Expanding the square: $(1-\alpha)^2 x_k^2 + 2(1-\alpha)x_k u_k + u_k^2$. Since $(1-\alpha)^2 - 1 = -2\alpha + \alpha^2$, we obtain

$$V(x_{k+1}) - V(x_k) = \left(-\alpha + \frac{\alpha^2}{2}\right)x_k^2 + (1-\alpha)\,x_k u_k + \frac{1}{2}u_k^2.$$

**Step 2: subtract the supply.** The passivity margin is

$$V(x_{k+1}) - V(x_k) - u_k y_k = \left(-\alpha + \frac{\alpha^2}{2} - \beta\right)x_k^2 + (1 - \alpha - \beta)\,x_k u_k + \left(\frac{1}{2}-\gamma\right)u_k^2.$$

**Step 3: choose the output coefficients.** The binary form $a x_k^2 + b\, x_k u_k$ with $b \ne 0$ is indefinite (take $u_k = -\frac{a}{b}x_k$ with sign chosen to make it positive), so we require $b = 0$, i.e.

$$\beta = 1 - \alpha.$$

Then the $x_k^2$ coefficient becomes $-\alpha + \frac{\alpha^2}{2} - (1-\alpha) = \frac{\alpha^2}{2} - 1$, which is strictly negative for all $\alpha < \sqrt{2}$ — in particular on the whole assumed range $\alpha \in [0,1]$. Setting $\gamma = \frac{1}{2}$ kills the $u_k^2$ term. The passive output is therefore

$$\boxed{y_k = (1-\alpha)\,x_k + \frac{1}{2}u_k,}$$

with dissipation inequality

$$V(x_{k+1}) - V(x_k) \le u_k y_k - \delta\,x_k^2, \qquad \delta = 1 - \frac{\alpha^2}{2} \;>\; 0.$$

Note $\delta$ is the *strict* dissipation rate in the sense of Section 3.1 (energy decays even with zero supply).

**Numerical verification with $\alpha = 0.1$.** Then $\beta = 1 - 0.1 = 0.9$, $\gamma = 0.5$, and the $x_k^2$ coefficient is $\frac{\alpha^2}{2} - \alpha = \frac{0.01}{2} - 0.1 = 0.005 - 0.1 = -0.095$, i.e. the margin is $-0.095\,x_k^2 \le 0$ for all $x_k$.

Concrete check, zero supply: take $x_0 = 2$, $u_0 = 0$. Then $x_1 = (1-0.1)\times 2 + 0 = 1.8$. Stored energies: $V(x_0) = \frac{1}{2}\times 4 = 2$; $V(x_1) = \frac{1}{2}\times 3.24 = 1.62$. So $\Delta V = 1.62 - 2 = -0.38$. The formula predicts $\left(\frac{\alpha^2}{2}-\alpha\right)x_0^2 = -0.095 \times 4 = -0.38$. Exact match.

Concrete check with supply: take $x_0 = 2$, $u_0 = 0.5$. Then $x_1 = 0.9 \times 2 + 0.5 = 2.3$; $V(x_1) = \frac{1}{2}\times 5.29 = 2.645$; $\Delta V = 2.645 - 2 = 0.645$. Output: $y_0 = 0.9 \times 2 + 0.5 \times 0.5 = 1.8 + 0.25 = 2.05$; supply $u_0 y_0 = 0.5 \times 2.05 = 1.025$. Margin: $\Delta V - u_0 y_0 = 0.645 - 1.025 = -0.38$, again equal to $-0.095 \times 2^2 = -0.38$. The dissipation inequality holds with margin $0.38$ at this step.

**Counterexample for the naive output.** With the unmodified output $y_k = x_k$ (i.e. $\beta = 1$, $\gamma = 0$) and $\alpha = 0.1$, the margin is $\left(-0.1 + 0.005\right)x_k^2 + \left(1 - 0.1 - 1\right)x_k u_k + \frac{1}{2}u_k^2 = -0.095\,x_k^2 - 0.1\,x_k u_k + 0.5\,u_k^2$. At $x_k = 1$, $u_k = -1$: $-0.095 + 0.1 + 0.5 = 0.505 > 0$: passivity **fails**. This is a substantive finding: the leaky Signal is passive only under the corrected output map $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$, not under the naive state-as-output choice.

### 4.3 Quantization degradation bound

**Assumptions (stated explicitly).** (i) The Signal output is quantized with uniform resolution $q = 0.1$, so the applied output satisfies $|y_k - y_k^{q}| \le \frac{q}{2} = 0.05$. (ii) The Worker-side supply actually delivered is $u_k y_k^{q}$ instead of $u_k y_k$. (iii) The input magnitude is bounded, $|u_k| \le U_{\max} = 1$ (assumption). (iv) Horizon $N = 100$ steps.

**Derivation.** The per-step supply error is

$$|u_k y_k - u_k y_k^{q}| = |u_k|\,|y_k - y_k^{q}| \le U_{\max}\cdot\frac{q}{2} = 1 \times 0.05 = 0.05.$$

Over the horizon, the worst-case cumulative passivity degradation is

$$\Delta_{\text{quant}} \le \sum_{k=0}^{N-1} 0.05 = N \times 0.05 = 100 \times 0.05 = 5.0.$$

**Interpretation.** The leaky Signal of Section 4.2