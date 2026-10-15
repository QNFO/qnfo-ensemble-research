# Passive Signal as Passive Controller: A Systems-Theoretic Feasibility Analysis of the Signal-Worker Ontology

## Abstract

The Signal-Worker (S-W) ontology interprets the boson as a *signal* — a delocalized field instruction — and the fermion as a *worker* — the localized state that performs work, and proposes that passive, structure-encoded control is thermodynamically superior to active, energy-intensive control. A prior feasibility analysis formalized the question of whether the Signal can function as a passive control system, but left open the engineering pathway: who would use such a result, what would have to be built, and what would falsify it. This paper closes that gap. We treat the Signal as a discrete-time controller block and derive, with full arithmetic, (i) exact passivity of a discrete integrator under the modified output $y_k = x_k + \frac{1}{2}u_k$, (ii) strict passivity of a leaky integrator under $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \frac{\alpha^2}{2}$, verified step by step for $\alpha = 0.1$ (margin $-0.095\,x_k^2$), and (iii) a worst-case passivity degradation of $5.0$ energy units over $N = 100$ steps under output quantization with resolution $q = 0.1$. A labeled illustrative example quantifies delay margin (safety ratio $\rho \approx 4.71$), quantization energy cost ($2.5\%$ per packet), attractor radius ($r_q = 0.05$), and robustness budget ($16.7\%$ margin erosion tolerance). We conclude the hypothesis is well-posed at the block-diagram level, is TRL 1-2 as pure analysis, and identify the smallest next test: fitting a storage function to whatever Signal dynamics the corpus specifies.

## 1. Introduction

Engineers who must stabilize fragile quantum or mesoscopic states — in superconducting devices, driven materials, or biological energy-transfer structures — currently face a trade-off between two control paradigms. Active control pumps energy into the system continuously: it works, but it is thermodynamically expensive, transient, and unstable when the drive is removed. Passive control encodes the stabilizing information in the structure of the environment itself: it is cheap and persistent, but there is no general theory saying when a proposed passive structure will actually behave as a controller. The Signal-Worker ontology addresses exactly this trade-off: it analyzes actively driven quantum systems (light-induced superconductivity, high-pressure hydrides, dynamical instabilities) as relying on an external, energy-intensive Signal, and passive structural control (proximity effects, Moiré engineering, biological scaffolds) as relying on an intrinsic, architectural Signal, and hypothesizes a Complexity-Efficiency relationship linking the structural complexity of the scaffold to stabilization performance [10]. What is missing is a bridge from that ontological claim to the precise language in which control engineers certify that a block is passive: a dissipation inequality with a storage function. Without that bridge, the ontology's central engineering question — can the Signal function as a passive control system? — cannot be checked, designed against, or falsified.

A prior feasibility analysis [9] took the first step: it restated the Signal as a discrete-time controller block, derived the output transformations under which integrator-type Signal dynamics satisfy a dissipation inequality, and bounded the passivity degradation caused by output quantization. That analysis established that the framing is not vacuous — it produces concrete, arithmetic-checkable quantities — but it stopped at the block-diagram level and did not connect the result to the corpus's own thermodynamic and complexity arguments, nor state what evidence would confirm or refute the hypothesis, nor assess whether the result is anywhere near engineering practice.

This paper completes the arc. We do not claim the S-W ontology is physically correct, and we import no physics beyond what the corpus documents state. We treat the ontology's own vocabulary — instruction (input), worker (actuator/state), boundary (channel) — as a mapping onto the control-theoretic triple of input, plant, and interconnection, and we analyze the consequences. Our contributions:

1. A block-diagram formalization of the Signal-Worker decomposition as a discrete-time passivity problem, with definitions (Section 3).
2. Exact derivations, with every arithmetic step shown, of the output maps under which pure and leaky integrator Signals are passive, including a counterexample showing the naive output fails (Section 4).
3. A worst-case quantization degradation bound ($5.0$ energy units over $100$ steps at resolution $q = 0.1$) and a labeled illustrative example quantifying delay margin, quantization energy cost, attractor radius, and robustness budget (Sections 4.3–4.4, reported in Section 5).
4. A connection between the passivity result and the corpus's own Complexity-Efficiency hypothesis, showing that the dissipation rate $\delta$ is the control-theoretic analogue of the corpus's passive-versus-driven distinction (Sections 5 and 6).
5. An explicit statement of the practical pathway: who would use the result, its technology readiness level, the smallest next test, and the constraints that would bind first (Section 7).

## 2. Background and Related Work

This section discusses the ten works that ground the analysis. Each is cited for a specific point its text makes.

**[1] Passive iFIR Filters for Data-Driven Control (arXiv:2403.06640v2).** This work designs passive controllers formed by the parallel action of an integrator and a finite impulse response filter, with the transfer function $C(z) = \frac{\gamma T_s}{1-z^{-1}} + \sum_{k=0}^{m-1}g_k z^{-k}$, where the integrator is discretized by backward Euler. Its introduction notes that with passive plants, PID control leads to inherently stable closed loops even when the plant is uncertain, and its conclusions state that for passive plants the stability of the closed loop is guaranteed by construction, with a design requiring no plant model or large datasets. This is directly relevant to the Signal question: the Signal block analyzed in Section 4 is exactly a discrete integrator, and [1] shows that integrator-based controller structures can be made passive by construction and tuned from data. If the Signal is to be engineered rather than merely postulated, the iFIR pattern is the closest available template.

**[2] Passivity-based PI control of first-order systems with I/O communication delays (arXiv:1507.01146v1).** This work revisits PI control of first-order linear passive systems through a delayed communication channel, treating the channel as a transport PDE, and guarantees passivity of the overall loop, yielding a closed-loop system of neutral type analyzed by spectral methods. Its introduction states the key obstacle plainly: if a delayed communication channel stands between plant and controller, passivity arguments fail because the Nyquist plot of a pure delay does not lie in the right-hand side of the complex plane. Its concluding remarks report that the optimal choice of the scattering-transformation design parameter is independent of the plant parameters and the delays, and that with it, exponential decay ratios almost twice as large as those suggested in the literature are attainable. For the S-W question this matters because the ontology separates the delocalized signal from the localized worker across a boundary; if the Signal acts on the Worker across any spatial extent, a transport delay is the minimal model of that separation, and [2] shows passivity can survive it — but only with an explicit transformation and at a quantifiable cost, which motivates the delay-margin analysis of Section 4.4.

**[3] Sampled-data control design for systems with quantized actuators (arXiv:2208.05694v3).** This work designs sampled-data state feedback for continuous-time linear systems with uniform input quantization of the form $\dot{x}_p = A_p x_p + B_p\, q_\Delta(u_p)$, ensuring uniform global asymptotic stability (UGAS) of an attractor surrounding the origin, with the closed loop rewritten as a hybrid dynamical system using an auxiliary clock variable. Its conclusion states that sufficient conditions take the form of bilinear matrix inequalities and that an iterative convex-concave algorithm minimizes the size of the closed-loop attractor. This motivates the quantization analysis of Section 4.3: any engineered Signal will be implemented in discrete time with finite-resolution actuation, and [3] establishes the standard framework — stability of an attractor around, rather than at, the origin — under exactly those conditions.

**[4] Composite Adaptive Control Barrier Functions for Safety-Critical Systems with Parametric Uncertainty (arXiv:2601.17683v3).** This work addresses the fact that control barrier functions (CBFs) — certificates that guarantee safety but require accurate models — lose their guarantees under parametric uncertainty. Its formulation considers $\dot{x}(t) = f(x(t)) + F(x(t))\theta_* + G(x(t))u(t)$ with unknown constant parameters $\theta_*$ bounded by $\theta_{\max}$, and its conclusions state that the resulting closed loop is safe for all bounded parameters (Theorem 4.7), noise-robust (Theorem 4.24), and uniformly ultimately bounded (Theorem 4.12), and is strictly less conservative than robust CBF (Theorem 5.1). We invoke this pattern in Section 6: the Signal-Worker hypothesis is a model-dependent claim, and [4] illustrates the standard taxonomy of responses — robust worst-case bounds versus adaptive estimation — when the model is uncertain, which for the corpus it certainly is.

**[5] Robust Nonlinear Optimal Control via System Level Synthesis (arXiv:2301.04943v3).** This work treats finite-horizon constrained robust optimal control for nonlinear systems with norm-bounded disturbances by decomposing the uncertain nonlinear system, via a first-order Taylor expansion, into a nominal system and an error described as an uncertain linear time-varying system, jointly optimizing the nominal trajectory, the affine error feedback, and the dynamic linearization error over-bounds. Its conclusion reports demonstrated reduced conservatism compared to open-loop robust and existing linear approaches, for a rigid body in rotation with state constraints. This supplies the decomposition pattern adopted in Section 4.4's robustness budget: separate a nominal closed loop (Signal driving Worker) from a norm-bounded deviation term, and analyze how much margin erosion the nominal passivity tolerates.

**[6] Safe Control Synthesis via Input Constrained Control Barrier Functions (arXiv:2104.01704v1).** This work introduces the Input Constrained CBF (ICCBF): when the safe set associated with a barrier function $h$ cannot be rendered forward invariant by any admissible controller, the method constructs intermediate sets $\mathcal{C}_1 = \{x : b_1(x) \ge 0\}$ with $b_1(x) = \inf_{u \in \mathcal{U}}[\dot{h}(x,u) + \alpha_0(h(x))]$, and renders the resulting inner safe set forward invariant. Its conclusion reports demonstration on adaptive cruise control and spacecraft rendezvous problems, and flags robustness to noise and model mismatch as open. This bears on the Signal-Worker question because a passive Signal with quantized, bounded outputs is precisely a controller with input constraints: the attractor-radius result of Section 4.4 is the passivity-side analogue of [6]'s inner-safe-set construction, and [6]'s acknowledged open robustness question is the same fragility discussed in Section 6.

**[7] On $\ell_2$-performance of weakly-hard real-time control systems (arXiv:2305.07875v3).** This work considers control systems with failures in the feedback channel, modeled by window-based weakly-hard constraints — at least $r$ successful control attempts in every window of $s$. Its Theorem 1 gives sufficient linear-matrix-inequality conditions under which the constrained-switching closed loop has $\ell_2$-performance with gain $\gamma$, with a Lyapunov function $V(x_k) = x_k^\top\left(\sum_{i=1}^{n_\mathcal{V}}\eta_i(k)S_i^{-1}\right)x_k$; the lifting technique discretizes the system at successful control instants and typically reduces the computational complexity of the LMI conditions. This is relevant because a Signal-Worker loop implemented over a real channel will suffer packet loss, and [7] provides the analysis machinery for passivity-adjacent performance guarantees under such loss — a deployment constraint Section 7 lists as binding early.

**[8] On the relationship between control barrier functions and projected dynamical systems (arXiv:2309.04378v1).** This work proves that the vector field of a CBF-controlled system is a Krasovskii-like perturbation of the set-valued map of a projected dynamical system (PDS), with a quantitative bound on the perturbation (Theorem 3.1), and its conclusion states that CBF-controlled systems uniformly converge to trajectories of the PDS and may serve as continuous implementations of discontinuous PDSs, preserving asymptotic stability of the origin without introducing undesired equilibria in the convex, fully-actuated case. This connects to the Signal question at a conceptual level: a passive Signal with a quantized output is a discontinuous controller, and [8] shows that discontinuity can be analyzed as a bounded perturbation of a well-behaved limiting system — the same move Section 4.3 makes when it treats quantization as a bounded perturbation of the passive inequality.

**[9] QNFO: Passive Signal as Passive Controller (prior feasibility analysis).** This work, the direct predecessor of the present paper, formalized the re-entry question as a discrete-time dissipation inequality. Its results section reports: the pure integrator is exactly passive under the modified output $y_k = x_k + \frac{1}{2}u_k$; the leaky integrator is strictly passive for $\alpha \in (0,1]$ under $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \alpha^2/2$, with margin $-0.095\,x_k^2$ at $\alpha = 0.1$ and failure under the naive output (counterexample margin $+0.505$); and a worst-case cumulative quantization degradation of $\Delta_{\text{quant}} = 5.0$ energy units under resolution $q = 0.1$, input bound $|u_k| \le 1$, and horizon $N = 100$. Its discussion concludes that the corpus material contains no dynamical equations, so the candidate Signal dynamics are postulated rather than derived. The present paper re-derives those results with full arithmetic (Section 4), extends them with the illustrative example of Section 4.4, and adds the corpus connection and engineering pathway the predecessor lacked.

**[10] QNFO: Structural vs Driven Quantum Coherence.** This document supplies the ontology's substantive content. Its theoretical framework grounds the analysis in Landauer's principle — information is physical, and maintaining the order of a quantum state has an irreducible energy cost — and introduces two complexity metrics: Krylov complexity, quantifying the dynamical complexity of the quantum state itself (the 'Worker'), and the Lossless Complexity Index (LCI), quantifying the structural complexity of the environment (the 'Signal' or scaffold). Its survey of active control finds that light-induced superconductivity, high-pressure hydrides, and dynamical instabilities share the architectural motif of reliance on an external, energy-intensive Signal, leading to thermodynamic inefficiency, transience, and dynamical instability, which it links to low LCI in the substrate. Its survey of passive structural control finds that proximity effects, Moiré engineering, and biological scaffolds rely on an intrinsic, architectural Signal, achieving high stability with minimal energy cost, and identifies the FMO complex's 'phononic scaffold' as a concrete design target: room-temperature coherence is not forbidden by physics but requires a structural environment that filters and shapes the thermal bath. This is the primary source for the Signal-Worker decomposition and for the Complexity-Efficiency hypothesis that Section 5 connects to the dissipation rate derived here.

## 3. Methods

### 3.1 Definitions

**Discrete-time passivity.** A discrete-time system with state $x_k \in \mathbb{R}^n$, input $u_k \in \mathbb{R}$, and output $y_k \in \mathbb{R}$ is *passive* if there exists a storage function $V(x) \ge 0$ with $V(0) = 0$ such that for all $k$,

$$V(x_{k+1}) - V(x_k) \le u_k\, y_k.$$

The right-hand side $u_k y_k$ is the *supply rate*: the energy injected at step $k$. Passivity says the stored energy never increases by more than the supplied energy; a passive system cannot be an unlimited source of energy.

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

Because the corpus documents state no dynamical equations, we analyze the two minimal candidate dynamics for a Signal whose role is to *accumulate and relay an instruction*:

- **Pure integrator (undriven relay):** $x_{k+1} = x_k + u_k.$
- **Leaky integrator (instruction decays if not refreshed), with leakage parameter $\alpha \in [0,1]$:** $x_{k+1} = (1-\alpha)\,x_k + u_k.$

The natural storage function for both is the quadratic $V(x) = \frac{1}{2}x^2$. The analysis question is: for which output maps $y_k = \beta x_k + \gamma u_k$ does the dissipation inequality hold, and with what dissipation rate?

### 3.3 Perturbation analysis under quantization and delay

Following the motivation of [3], we bound how uniform input quantization of resolution $q$ degrades the passivity inequality over a finite horizon. In a clearly labeled illustrative example (Section 4.4), we additionally evaluate, in the spirit of [2], the delay phase loss at a chosen crossover frequency against a chosen dissipative margin, and, in the spirit of [5], the erosion budget on the Signal's passivity margin under a norm-bounded deviation.

## 4. Analysis

Every input number below is either a structural constant of the candidate dynamics or an explicitly stated assumption or illustrative chosen parameter. All arithmetic is shown.

### 4.1 Exact passivity of the pure integrator

**Setup.** Dynamics $x_{k+1} = x_k + u_k$; storage $V(x) = \frac{1}{2}x^2$; candidate output $y_k = \beta x_k + \gamma u_k$.

**Step 1: expand the storage change.**

$$V(x_{k+1}) - V(x_k) = \frac{1}{2}(x_k + u_k)^2 - \frac{1}{2}x_k^2 = x_k u_k + \frac{1}{2}u_k^2.$$

**Step 2: state the passivity requirement.** We need

$$x_k u_k + \frac{1}{2}u_k^2 \le u_k(\beta x_k + \gamma u_k) = \beta x_k u_k + \gamma u_k^2$$

for all $(x_k, u_k)$. Rearranging,

$$(1-\beta)\,x_k u_k + \left(\frac{1}{2}-\gamma\right)u_k^2 \le 0 \quad \text{for all } x_k, u_k.$$

**Step 3: solve the coefficients.** The term $(1-\beta)x_k u_k$ changes sign with $x_k u_k$ unless its coefficient is zero, so we require $\beta = 1$. Then the remaining term $\left(\frac{1}{2}-\gamma\right)u_k^2 \le 0$ for all $u_k$ requires $\gamma \ge \frac{1}{2}$. The minimal (exactly passive) choice is

$$y_k = x_k + \frac{1}{2}u_k,$$

for which $u_k y_k = x_k u_k + \frac{1}{2}u_k^2 = V(x_{k+1}) - V(x_k)$ identically: the supply exactly equals the stored-energy change.

**Numerical verification.** Take $x_0 = 0$, $u_0 = 0.1$. Then $x_1 = 0 + 0.1 = 0.1$; $V(x_1) = \frac{1}{2}(0.1)^2 = 0.005$; $V(x_0) = 0$; so $\Delta V = 0.005 - 0 = 0.005$. The modified output is $y_0 = 0 + \frac{1}{2}(0.1) = 0.05$, and the supply is $u_0 y_0 = 0.1 \times 0.05 = 0.005$. Supply equals storage change exactly, confirming exact passivity.

### 4.2 Passivity of the leaky integrator

**Setup.** Dynamics $x_{k+1} = (1-\alpha)x_k + u_k$ with leakage $\alpha \in [0,1]$; storage $V(x) = \frac{1}{2}x^2$; candidate output $y_k = \beta x_k + \gamma u_k$.

**Step 1: expand the storage change.**

$$V(x_{k+1}) - V(x_k) = \frac{1}{2}\left[(1-\alpha)x_k + u_k\right]^2 - \frac{1}{2}x_k^2.$$

Expanding the square: $(1-\alpha)^2 x_k^2 + 2(1-\alpha)x_k u_k + u_k^2$. Since $(1-\alpha)^2 - 1 = -2\alpha + \alpha^2$, we obtain

$$V(x_{k+1}) - V(x_k) = \left(-\alpha + \frac{\alpha^2}{2}\right)x_k^2 + (1-\alpha)\,x_k u_k + \frac{1}{2}u_k^2.$$

**Step 2: subtract the supply.** The passivity margin is

$$V(x_{k+1}) - V(x_k) - u_k y_k = \left(-\alpha + \frac{\alpha^2}{2}\right)x_k^2 + \left(1 - \alpha - \beta\right)x_k u_k + \left(\frac{1}{2}-\gamma\right)u_k^2.$$

**Step 3: choose the output coefficients.** The binary form $a x_k^2 + b\, x_k u_k$ with $b \ne 0$ is indefinite, so we require $b = 0$, i.e.

$$\beta = 1 - \alpha.$$

Then the $x_k^2$ coefficient is $-\alpha + \frac{\alpha^2}{2}$, which is strictly negative for all $\alpha \in (0,1]$ (at $\alpha = 0$ it vanishes and the passivity is exact rather than strict). Setting $\gamma = \frac{1}{2}$ kills the $u_k^2$ term. The passive output is therefore

$$y_k = (1-\alpha)\,x_k + \frac{1}{2}u_k,$$

with dissipation inequality

$$V(x_{k+1}) - V(x_k) \le u_k y_k - \delta\,x_k^2, \qquad \delta = \alpha - \frac{\alpha^2}{2} \;>\; 0 \quad \text{for } \alpha \in (0,1].$$

**Numerical verification with $\alpha = 0.1$.** Then $\beta = 1 - 0.1 = 0.9$, $\gamma = 0.5$, and the $x_k^2$ coefficient is $\frac{\alpha^2}{2} - \alpha = \frac{0.01}{2} - 0.1 = 0.005 - 0.1 = -0.095$, i.e. the margin is $-0.095\,x_k^2 \le 0$ for all $x_k$.

Concrete check, zero supply: take $x_0 = 2$, $u_0 = 0$. Then $x_1 = (1-0.1)\times 2 + 0 = 1.8$. Stored energies: $V(x_0) = \frac{1}{2}\times 4 = 2$; $V(x_1) = \frac{1}{2}\times 3.24 = 1.62$. So $\Delta V = 1.62 - 2 = -0.38$. The formula predicts $\left(\frac{\alpha^2}{2}-\alpha\right)x_0^2 = -0.095 \times 4 = -0.38$. Exact match.

Concrete check with supply: take $x_0 = 2$, $u_0 = 0.5$. Then $x_1 = 0.9 \times 2 + 0.5 = 2.3$; $V(x_1) = \frac{1}{2}\times 5.29 = 2.645$; $\Delta V = 2.645 - 2 = 0.645$. Output: $y_0 = 0.9 \times 2 + 0.5 \times 0.5 = 2.05$; supply $u_0 y_0 = 0.5 \times 2.05 = 1.025$. Margin: $\Delta V - u_0 y_0 = 0.645 - 1.025 = -0.38$, again equal to $-0.095 \times 2^2 = -0.38$. The dissipation inequality holds with margin $0.38$ at this step.

**Counterexample for the naive output.** With the unmodified output $y_k = x_k$ (i.e. $\beta = 1$, $\gamma = 0$) and $\alpha = 0.1$, the margin is $-0.095\,x_k^2 - 0.1\,x_k u_k + 0.5\,u_k^2$. At $x_k = 1$, $u_k = -1$: $-0.095 + 0.1 + 0.5 = 0.505 > 0$: passivity **fails**. This is a substantive finding: the leaky Signal is passive only under the corrected output map $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$, not under the naive state-as-output choice.

### 4.3 Quantization degradation bound

**Assumptions (stated explicitly).** (i) The Signal output is quantized with uniform resolution $q = 0.1$, so the applied output satisfies $|y_k - y_k^{q}| \le \frac{q}{2} = 0.05$. (ii) The Worker-side supply actually delivered is $u_k y_k^{q}$ instead of $u_k y_k$. (iii) The input magnitude is bounded, $|u_k| \le U_{\max} = 1$ (assumption). (iv) Horizon $N = 100$ steps.

**Derivation.** The per-step supply error is

$$|u_k y_k - u_k y_k^{q}| = |u_k|\,|y_k - y_k^{q}| \le U_{\max}\cdot\frac{q}{2} = 1 \times 0.05 = 0.05.$$

Over the horizon, the worst-case cumulative passivity degradation is

$$\Delta_{\text{quant}} \le \sum_{k=0}^{N-1} 0.05 = N \times 0.05 = 100 \times 0.05 = 5.0.$$

**Interpretation.** The leaky Signal of Section 4.2 dissipates at rate $\delta = \alpha - \frac{\alpha^2}{2} = 0.1 - 0.005 = 0.095$ per unit $x_k^2$; whether the quantization budget of $5.0$ energy units over $100$ steps is tolerable depends on the state magnitudes involved, which the corpus does not specify. The bound is structural: no passive quantized Signal can promise a tighter passivity inequality than this budget allows under the stated assumptions.

### 4.4 Illustrative example: delay margin, energy cost, attractor radius, robustness budget

All parameters in this subsection are *illustrative parameters chosen for the worked example*, stated explicitly; every derived number follows from them by shown arithmetic. No number below is an empirical measurement.

**Input list.** $k_S = 2.0$ (static gain of the Signal's dissipative path, chosen); $\epsilon_S = 0.1$ (Signal passivity margin, chosen); $\epsilon_W = 0.2$ (Worker passivity margin, chosen); $T_d = 0.5\ \mathrm{s}$ (transport delay of the delocalized channel, chosen); $\omega_c = 1.0\ \mathrm{rad\,s^{-1}}$ (loop crossover frequency, chosen); $\Delta = 0.05$ (uniform quantization step, chosen); $u_{\max} = 1.0$ (norm bound, chosen); $\lambda_W = 0.5\ \mathrm{s^{-1}}$ (Worker contraction constant, chosen).

**Delay margin.** A pure delay $T_d$ contributes phase lag $\phi_d(\omega) = \omega T_d$ at frequency $\omega$. At $\omega = \omega_c$:

$$\phi_d(\omega_c) = (1.0\ \mathrm{rad\,s^{-1}})(0.5\ \mathrm{s}) = 0.5\ \mathrm{rad} = 0.5 \times \frac{180}{\pi} \approx 0.5 \times 57.29578 \approx 28.65^{\circ}.$$

The combined dissipative margin proxy is $M = k_S(\epsilon_S + \epsilon_W) = 2.0 \times (0.1 + 0.2) = 0.6$. The normalized delay loss is $\ell_d = \phi_d(\omega_c)/(2\pi) = 0.5/(2\pi) \approx 0.0796$; the normalized margin is $M_n = M/(1+M) = 0.6/1.6 = 0.375$. Since $M_n = 0.375 > \ell_d \approx 0.0796$, the illustrative margin condition is satisfied with ratio $\rho = M_n/\ell_d = 0.375/0.0796 \approx 4.71$. This margin proxy is a heuristic consistent with the loop-passivity guarantee pattern of [2], not a sigma-stability certificate.

**Quantization energy cost.** With quantization step $\Delta$ and input norm bounded by $u_{\max}$, the worst-case excess energy per delivered packet attributable to quantization is $E_q \le (\Delta/2)\,u_{\max} = (0.05/2)(1.0) = 0.025\ \mathrm{J}$. The nominal per-packet supply at full magnitude is $E_0 = u_{\max}^2 = 1.0\ \mathrm{J}$ (conservative bound with unit feedthrough). The relative overhead is $E_q/E_0 = 0.025/1.0 = 2.5\%$.

**Attractor radius.** If the Worker's closed-loop contraction rate toward the attractor is at least $\lambda_W$ per unit input error, and the input error is bounded by $\Delta/2$, the guaranteed attractor radius contribution is $r_q = (\Delta/2)/\lambda_W = 0.025/0.5 = 0.05$ in normalized Worker units, in the UGAS-of-attractor sense of [3]. No passive quantized Signal can promise convergence to a point from quantization alone.

**Robustness budget.** Following the nominal-plus-error structure of [5], let the uncertain LTV deviation have norm bound $\delta$ on the Signal's passivity margin: $\epsilon_S^{\text{actual}} = \epsilon_S - \delta$. Passivity of the Signal block is retained iff $\delta < \epsilon_S = 0.1$. As a fraction of the combined margin $M = 0.6$, this is $\delta/M = 0.1/0.6 \approx 0.1667$, i.e., the Signal can tolerate erosion of up to about $16.7\%$ of the combined loop margin before its own passivity fails.

## 5. Results

All results below are the direct outputs of Section 4's derivations from the stated inputs and illustrative parameters; none are empirical.

- **R1 (integrator passivity).** The pure integrator is exactly passive under the modified output $y_k = x_k + \frac{1}{2}u_k$; supply equals storage change identically (verified numerically in Section 4.1).
- **R2 (leaky integrator passivity).** The leaky integrator is strictly