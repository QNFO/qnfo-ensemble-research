# Passive Signal as Passive Controller: A Systems-Theoretic Feasibility Analysis of the Signal-Worker Ontology

## Abstract

Engineers who must stabilize fragile quantum or mesoscopic states face a trade-off between active control, which injects energy continuously, and passive structural control, which encodes stabilizing information in the environment but lacks a certification theory. The Signal-Worker (S-W) ontology interprets the boson as a *signal*—a delocalized field instruction—and the fermion as a *worker*—the localized state that performs work, proposing that passive, structure-encoded control is thermodynamically superior to active, energy-intensive control. The specific gap addressed here is the absence of a control-theoretic bridge: no dissipation inequality with an explicit storage function has been derived for the Signal block, so the ontology's central engineering claim can be neither certified nor falsified. This paper treats the Signal as a discrete-time controller block and derives, with full arithmetic, (i) exact passivity of a pure integrator under the modified output $y_k = x_k + \tfrac{1}{2}u_k$, (ii) strict passivity of a leaky integrator under $y_k = (1-\alpha)x_k + \tfrac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \tfrac{\alpha^{2}}{2}$ (margin $-0.095\,x_k^{2}$ at $\alpha = 0.1$), and (iii) a worst-case passivity degradation of $5.0$ energy units over $N = 100$ steps with quantization resolution $q = 0.1$, tolerable only when the accumulated dissipation $\delta\sum_k x_k^{2}$ exceeds that budget, which requires state magnitudes of at least $0.726$ under a constant-magnitude assumption. An illustrative example quantifies delay margin ($\rho \approx 4.71$), quantization energy cost ($2.5\%$ per packet), attractor radius ($r_q = 0.05$), and robustness budget ($16.7\%$ margin erosion tolerance). The result is placed at Technology Readiness Level 1–2, and the smallest next test is a storage-function fitting for any concrete Signal dynamics.

## 1. Introduction

Engineers who must stabilize fragile quantum or mesoscopic states—such as superconducting devices, driven materials, or biological energy-transfer structures—currently face a trade-off between two control paradigms. Active control continuously injects energy, achieving stabilization at high thermodynamic cost and losing stability when the drive is removed. Passive control encodes stabilizing information in the environment's structure, offering cheap and persistent stabilization but lacking a general theory to guarantee that a proposed passive structure indeed behaves as a controller. The cost of this gap is concrete: without a certification criterion, a designer cannot decide whether a candidate passive scaffold will stabilize the target state, cannot compare candidate scaffolds quantitatively, and cannot falsify claims made for them. The Signal-Worker ontology addresses the trade-off by interpreting active quantum control as reliance on an external, energy-intensive Signal and passive structural control as relying on an intrinsic, architectural Signal, hypothesizing a Complexity-Efficiency relationship linking scaffold complexity to stabilization performance [10]. The missing bridge is a precise control-theoretic statement: does the Signal satisfy a dissipation inequality with a storage function? Without such a bridge, the ontology's central engineering question cannot be certified, designed against, or falsified.

A prior feasibility analysis [9] restated the Signal as a discrete-time controller block, derived output transformations for integrator-type dynamics, and bounded passivity degradation caused by output quantization. That work produced arithmetic-checkable quantities but stopped at the block-diagram level, omitted connections to the corpus's thermodynamic arguments, and left the engineering pathway unspecified. This paper completes the arc and, in doing so, corrects an interpretive error in the predecessor's quantization analysis: the published Section 4.3 stated that the quantization budget is tolerable only for states *small enough* that $\delta\sum_k x_k^{2}$ stays above $5.0$; the inequality in fact requires states *large enough*, because the dissipation term must exceed the degradation budget. The corrected interpretation is derived in Section 4.3 and confirmed by the structure of the inequality itself: the net margin is $\delta\sum_k x_k^{2} - \Delta_{\text{quant}}$, which is non-positive when the dissipation is too small, i.e., when states are too small.

Contributions are:

1. A block-diagram formalization of the Signal-Worker decomposition as a discrete-time passivity problem (Section 3).
2. Exact derivations, with every arithmetic step shown, of the output maps under which pure and leaky integrator Signals are passive, including a counterexample for the naive output (Section 4).
3. A worst-case quantization degradation bound ($5.0$ energy units over $100$ steps at $q = 0.1$) with the corrected state-magnitude threshold $x_\ast \ge 0.726$, and an illustrative example quantifying delay margin, quantization energy cost, attractor radius, and robustness budget (Sections 4.3–4.4, summarized in Section 5).
4. A mapping between the derived dissipation rate $\delta$ and the corpus's passive-versus-driven distinction (Section 6).
5. A practical pathway: identification of users, TRL assessment, the smallest next test, and the primary engineering constraints (Section 7).

## 2. Background and Related Work

**[1] Passive iFIR Filters for Data-Driven Control.** The work designs passive controllers as the parallel action of an integrator and a finite-impulse-response filter, with transfer function $C(z)=\frac{\gamma T_s}{1-z^{-1}}+\sum_{k=0}^{m-1}g_k z^{-k}$, where the integrator is discretized using backward Euler with sampling period $T_s$. It shows that for passive plants the closed-loop stability is guaranteed by construction and that the design requires no plant model or large datasets, with passivity enforced through convex constraints derived from the Kalman-Yakubovich-Popov lemma. This directly supports the notion that an integrator-based Signal block can be rendered passive by construction rather than by postulate; the iFIR pattern reappears in Section 7 as a template for implementing the derived output map.

**[2] Passivity-based PI control of first-order systems with I/O communication delays.** This paper treats a delayed communication channel as a transport PDE and proves that the overall loop remains passive when a scattering transformation is applied, despite the fact that the Nyquist plot of a pure delay does not lie in the right-hand side of the complex plane. It further shows, via $\sigma$-stability analysis of the characteristic quasipolynomial, that the optimal design parameter of the scattering transformation is independent of the plant parameters and the delays, and that the theoretical limit on the exponential decay rate depends on the total delay but not on the plant parameters. This motivates the delay-margin analysis in Section 4.4, where a transport delay models the spatial separation between Signal and Worker, and cautions that the heuristic safety ratio used there is a proxy for the full $\sigma$-stability treatment that work performs.

**[3] Sampled-data control design for systems with quantized actuators.** The authors design sampled-data state feedback for continuous-time linear systems with uniform input quantization $q_\Delta(u_p)$, rewriting the closed loop as a hybrid dynamical system with an auxiliary clock variable, and derive sufficient conditions for uniform global asymptotic stability of an attractor surrounding the origin in the form of bilinear matrix inequalities, with an iterative algorithm that minimizes the size of the closed-loop attractor. Their framework underpins the quantization analysis of Section 4.3, treating the quantized Signal output as a bounded perturbation of the ideal passive inequality, and their attractor-minimization objective parallels the attractor-radius quantity derived in Section 4.4.

**[4] Composite Adaptive Control Barrier Functions for Safety-Critical Systems with Parametric Uncertainty.** This work shows that safety guarantees based on control barrier functions fail when model parameters are incorrect—the calculated safe control input may drive the system into the unsafe region—and introduces a composite adaptive framework that couples parameter estimation directly to safety, proving forward invariance of the safe set for all bounded parameters (Theorem 4.7) and that the framework is strictly less conservative than robust CBFs (Theorem 5.1). It illustrates the broader theme that model uncertainty can invalidate guarantees, which is reflected in the limitations discussion of Section 6 and in the robustness-budget constraint of Section 7.

**[5] Robust Nonlinear Optimal Control via System Level Synthesis.** The authors decompose an uncertain nonlinear system, via a first-order Taylor expansion, into a nominal nonlinear trajectory and an error system described as an uncertain linear time-varying system, and jointly optimize the nominal trajectory, the affine error feedback, and dynamic linearization-error over-bounds for robust constraint satisfaction, demonstrating reduced conservatism compared to open-loop robust approaches on a constrained rigid-body rotation problem. Their nominal-plus-error decomposition informs the robustness-budget calculation in Section 4.4, where the Signal's passivity margin is eroded by a bounded deviation.

**[6] Safe Control Synthesis via Input Constrained Control Barrier Functions.** This paper introduces Input-Constrained CBFs that construct inner safe sets $\mathcal{C}_1, \mathcal{C}_2, \ldots$ whose intersection $\mathcal{C}^{*}$ can be rendered forward invariant when full input authority is unavailable, since only a subset of the safe set may then be invariant. The attractor-radius result of Section 4.4 mirrors the inner-safe-set construction: quantized, bounded outputs act as input constraints, and the guaranteed invariant set shrinks to a neighborhood of the origin rather than the origin itself.

**[7] On $\ell_2$-performance of weakly-hard real-time control systems.** The authors develop sufficient LMI conditions under which linear plants with unreliable feedback—modeled by window-based weakly-hard constraints such as "at least $r$ control attempts in every window of $s$ are successful"—have $\ell_2$-performance with a given gain $\gamma$, using a lifting that discretizes the system at instants of successful control attempts and typically reduces the computational complexity of the LMI conditions. Their framework motivates the discussion of packet-loss constraints as a future extension in Section 7, since the present analysis does not yet integrate loss sequences with the dissipation inequality.

**[8] On the relationship between control barrier functions and projected dynamical systems.** This work proves that the vector field of CBF-controlled systems is a Krasovskii-like perturbation of the set-valued map of a projected dynamical system, and provides a quantitative bound on that perturbation, e.g., $\|x-y\|\le\gamma\bigl(\tfrac{1}{a}|\mathcal{L}_f h(x)|\bigr)$ for $x$ in the set $U_{\mathrm{cbf},a}$ and $y$ its projection onto the safe-set boundary. It supports the treatment of quantization as a bounded additive perturbation in Section 4.3, with the caveat that the regularity conditions required by that theorem are not verified here.

**[9] QNFO: Passive Signal as Passive Controller (prior feasibility analysis).** The predecessor formalized the Signal as a discrete-time block, derived exact passivity for a pure integrator, strict passivity for a leaky integrator with dissipation rate $\delta = \alpha - \tfrac{\alpha^{2}}{2}$, and a worst-case quantization degradation of $5.0$ energy units, and reported the state threshold $0.726$ alongside an interpretation that the budget is tolerable for states small enough—a reading corrected here. The present paper re-derives those results with full arithmetic, fixes the interpretation, extends the treatment with an illustrative example, and adds the engineering pathway the predecessor lacked.

**[10] QNFO: Structural vs Driven Quantum Coherence.** The corpus paper proposes the Signal-Worker ontology, built on the premise that information is physical and that maintaining the order of a quantum state has an irreducible energy cost as quantified by Landauer's principle, making thermodynamic efficiency the ultimate metric for any stabilization mechanism. It introduces two complexity metrics—Krylov complexity for the dynamical complexity of the Worker state and the Lossless Complexity Index (LCI) for the structural complexity of the Signal scaffold—and applies the framework to classify actively driven systems (light-induced superconductivity, high-pressure hydrides, dynamical instabilities) as thermodynamically inefficient and transient, versus passive structural systems (proximity effects, Moiré engineering, biological scaffolds) that encode information in structure. The present paper imports no numerical values from that work; the connection is structural and is developed in Section 6.

## 3. Methods

### 3.1 Definitions

**Discrete-time passivity.** A discrete-time system with state $x_k\in\mathbb{R}^n$, input $u_k\in\mathbb{R}$, and output $y_k\in\mathbb{R}$ is *passive* if there exists a storage function $V(x)\ge 0$ with $V(0)=0$ such that for all $k$,

$$
V(x_{k+1}) - V(x_k) \le u_k\,y_k .
$$

The right-hand side $u_k y_k$ is the *supply rate*.

**Strict passivity with dissipation rate.** If additionally

$$
V(x_{k+1}) - V(x_k) \le u_k\,y_k - \delta\,x_k^{2},
\qquad \delta > 0,
$$

the system is strictly passive with dissipation rate $\delta$.

**Block interpretation of the S-W ontology.** The mapping from the corpus [10] to a control block diagram is

```
u_k (instruction) ──► [ SIGNAL ] ──y_k──► [ WORKER ] ──► work output
                        (delocalized)   (localized state)
```

The research question becomes: does a storage function $V_S$ exist such that the Signal block alone satisfies the dissipation inequality?

### 3.2 Candidate Signal dynamics

Because the corpus provides no dynamical equations, we analyze the two minimal candidate dynamics:

*Pure integrator:* $x_{k+1}=x_k+u_k$.

*Leaky integrator* (leakage $\alpha\in[0,1]$): $x_{k+1}=(1-\alpha)x_k+u_k$.

For both, the quadratic storage function $V(x)=\tfrac{1}{2}x^{2}$ is natural. The analysis seeks output maps $y_k=\beta x_k+\gamma u_k$ that satisfy the dissipation inequality.

### 3.3 Perturbation analysis under quantization and delay

Following the quantized-actuator framework of [3], we bound how uniform input quantization of resolution $q$ degrades the passivity inequality over a finite horizon, treating the quantization as a bounded additive perturbation in the spirit of the perturbation bound of [8]. In the illustrative example (Section 4.4) we also evaluate delay-phase loss using the transport-delay model of [2] and a robustness budget inspired by the nominal-plus-error decomposition of [5].

## 4. Analysis

All numerical inputs are either structural constants of the candidate dynamics or explicitly stated illustrative parameters. Every arithmetic step is shown.

### 4.1 Exact passivity of the pure integrator

**Setup.** Dynamics $x_{k+1}=x_k+u_k$; storage $V(x)=\tfrac{1}{2}x^{2}$; output $y_k=\beta x_k+\gamma u_k$.

**Step 1: storage change.**

$$
V(x_{k+1})-V(x_k)=\frac{1}{2}(x_k+u_k)^{2}-\frac{1}{2}x_k^{2}
= x_k u_k+\frac{1}{2}u_k^{2}.
$$

**Step 2: passivity requirement.** Require

$$
x_k u_k+\frac{1}{2}u_k^{2}\le u_k(\beta x_k+\gamma u_k)
= \beta x_k u_k+\gamma u_k^{2},
$$

i.e.

$$
(1-\beta)x_k u_k+\Bigl(\frac{1}{2}-\gamma\Bigr)u_k^{2}\le 0
\quad\forall x_k,u_k.
$$

**Step 3: coefficient choice.** The mixed term changes sign unless its coefficient vanishes, so $\beta=1$. Then $\frac{1}{2}-\gamma\le 0$ forces $\gamma\ge\frac{1}{2}$. The minimal exactly-passive choice is $\gamma=\frac{1}{2}$, giving

$$
y_k = x_k + \frac{1}{2}u_k,
\qquad
u_k y_k = x_k u_k + \frac{1}{2}u_k^{2}
= V(x_{k+1})-V(x_k).
$$

**Numerical check.** With $x_0=0$, $u_0=0.1$: $x_1=0.1$, $V(x_1)=\tfrac{1}{2}(0.1)^{2}=0.005$, $\Delta V=0.005-0=0.005$; $y_0=0+\tfrac{1}{2}(0.1)=0.05$, $u_0 y_0=0.1\times0.05=0.005$. Equality holds, confirming exact passivity.

### 4.2 Passivity of the leaky integrator

**Setup.** Dynamics $x_{k+1}=(1-\alpha)x_k+u_k$ with $\alpha\in[0,1]$; storage $V(x)=\tfrac{1}{2}x^{2}$; output $y_k=\beta x_k+\gamma u_k$.

**Step 1: storage change.**

$$
\begin{aligned}
V(x_{k+1})-V(x_k)
&=\frac{1}{2}\bigl[(1-\alpha)x_k+u_k\bigr]^{2}-\frac{1}{2}x_k^{2}\\
&=\frac{1}{2}\Bigl[(1-\alpha)^{2}x_k^{2}+2(1-\alpha)x_k u_k+u_k^{2}\Bigr]-\frac{1}{2}x_k^{2}\\
&=\Bigl(-\alpha+\frac{\alpha^{2}}{2}\Bigr)x_k^{2}+(1-\alpha)x_k u_k+\frac{1}{2}u_k^{2}.
\end{aligned}
$$

**Step 2: subtract supply.**

$$
\begin{aligned}
V(x_{k+1})-V(x_k)-u_k y_k
&=\Bigl(-\alpha+\frac{\alpha^{2}}{2}\Bigr)x_k^{2}
+\bigl(1-\alpha-\beta\bigr)x_k u_k
+\Bigl(\frac{1}{2}-\gamma\Bigr)u_k^{2}.
\end{aligned}
$$

**Step 3: coefficient choice.** To eliminate the mixed term we set $\beta = 1-\alpha$. Setting $\gamma=\frac{1}{2}$ removes the $u_k^{2}$ term. The remaining coefficient of $x_k^{2}$ is $-\alpha+\frac{\alpha^{2}}{2}= -\delta$ with

$$
\delta = \alpha - \frac{\alpha^{2}}{2} > 0 \quad\text{for }\alpha\in(0,1].
$$

Thus the passive output is

$$
y_k = (1-\alpha)x_k + \frac{1}{2}u_k,
\qquad
V(x_{k+1})-V(x_k) \le u_k y_k - \delta x_k^{2}.
$$

**Numerical verification for $\alpha=0.1$.**
$\beta = 1-0.1 = 0.9$, $\gamma = 0.5$, $\delta = 0.1 - \tfrac{0.1^{2}}{2} = 0.1 - 0.005 = 0.095$.

*Zero supply:* $x_0=2$, $u_0=0$ gives $x_1=0.9\times2+0=1.8$. $V(x_0)=\tfrac{1}{2}\times4=2$, $V(x_1)=\tfrac{1}{2}\times3.24=1.62$, $\Delta V=1.62-2=-0.38$. $-\delta x_0^{2}= -0.095\times4 = -0.38$. Equality holds.

*With supply:* $x_0=2$, $u_0=0.5$ gives $x_1=0.9\times2+0.5=2.3$. $V(x_1)=\tfrac{1}{2}\times5.29=2.645$, $\Delta V=2.645-2=0.645$. $y_0=0.9\times2+0.5\times0.5=1.8+0.25=2.05$, $u_0 y_0=0.5\times2.05=1.025$. $\Delta V - u_0 y_0 = 0.645-1.025 = -0.38 = -\delta x_0^{2}$. Inequality holds with margin $0.38$.

**Counterexample for the naive output.** With $y_k = x_k$ ($\beta=1,\gamma=0$) and $\alpha=0.1$,

$$
V(x_{k+1})-V(x_k)-u_k y_k
= -0.095 x_k^{2} -0.1 x_k u_k + 0.5 u_k^{2}.
$$

At $x_k=1$, $u_k=-1$ the expression equals $-0.095\times1 - 0.1\times(1)(-1) + 0.5\times1 = -0.095 + 0.1 + 0.5 = 0.505 > 0$; passivity fails.

### 4.3 Quantization degradation bound

**Assumptions.**
(i) Uniform output quantization with resolution $q=0.1$, so $|y_k - y_k^{q}| \le q/2 = 0.05$.
(ii) The Worker receives the quantized output, so the actual supply is $u_k y_k^{q}$.
(iii) Input magnitude bounded: $|u_k| \le U_{\max}=1$.
(iv) Horizon $N=100$ steps.

**Derivation.** Per-step supply error:

$$
|u_k y_k - u_k y_k^{q}| = |u_k|\,|y_k-y_k^{q}|
\le U_{\max}\cdot\frac{q}{2}=1\times0.05=0.05.
$$

Cumulative worst-case degradation:

$$
\Delta_{\text{quant}} \le \sum_{k=0}^{N-1}0.05 = N \times 0.05 = 100\times0.05 = 5.0.
$$

**Interpretation (corrected).** The leaky integrator dissipates $\delta \sum_{k} x_k^{2}$. The net passivity margin over the horizon is

$$
\delta\sum_{k=0}^{N-1}x_k^{2} - \Delta_{\text{quant}}.
$$

If state magnitudes are of order unity, the total dissipation over 100 steps is $\delta \times 100 \times 1 = 0.095\times100 = 9.5$ (for $\delta=0.095$), exceeding the quantization budget of $5.0$; the net margin is then $9.5-5.0=4.5>0$. The budget is therefore tolerable only for states *large enough* that $\delta\sum_k x_k^{2} \ge 5.0$—the published version's statement that states must be *small enough* is incorrect, since shrinking the states shrinks the dissipation and widens the deficit. A concrete threshold follows from assuming a constant state magnitude $x_\ast$:

$$
0.095 \times 100 \times x_\ast^{2} \ge 5.0
\;\Longrightarrow\;
9.5\,x_\ast^{2} \ge 5.0
\;\Longrightarrow\;
x_\ast^{2} \ge \frac{5.0}{9.5}\approx 0.5263,
$$

$$
x_\ast \ge \sqrt{0.5263}\approx 0.7255 \approx 0.726.
$$

Under the stated assumptions, the bound $\Delta_{\text{quant}} \le N U_{\max} q/2$ is exact and cannot be tightened without reducing $q$, $N$, or $U_{\max}$.

### 4.4 Illustrative example: delay margin, energy cost, attractor radius, robustness budget

All parameters in this subsection are *illustrative choices*, stated explicitly; every derived number follows from them by shown arithmetic. No number below is an empirical measurement.

**Input list.** $k_S = 2.0$ (static gain), $\epsilon_S = 0.1$ (Signal margin), $\epsilon_W = 0.2$ (Worker margin), $T_d = 0.5\ \text{s}$ (transport delay), $\omega_c = 1.0\ \text{rad s}^{-1}$ (crossover frequency), $\Delta = 0.05$ (quantization step), $u_{\max}=1.0$ (norm bound), $\lambda_W = 0.5\ \text{s}^{-1}$ (Worker contraction constant).

**Delay margin.** Phase lag at $\omega_c$:

$$
\phi_d = \omega_c T_d = 1.0 \times 0.5 = 0.5\ \text{rad}
= 0.5 \times \frac{180}{\pi} \approx 28.65^{\circ}.
$$

Combined dissipative margin proxy:

$$
M = k_S(\epsilon_S+\epsilon_W)=2.0\times(0.1+0.2)=2.0\times0.3=0.6.
$$

Normalized delay loss:

$$
\ell_d = \frac{\phi_d}{2\pi}= \frac{0.5}{2\pi}\approx 0.0796.
$$

Normalized margin:

$$
M_n = \frac{M}{1+M}= \frac{0.6}{1.6}=0.375.
$$

Safety ratio:

$$
\rho = \frac{M_n}{\ell_d}= \frac{0.375}{0.0796}\approx 4.71.
$$

**Quantization energy cost.**

$$
E_q \le \frac{\Delta}{2}\,u_{\max}= \frac{0.05}{2}\times1.0 = 0.025\ \text{J}.
$$

Nominal per-packet supply bound $E_0 = u_{\max}^{2}=1.0\ \text{J}$. Relative overhead:

$$
\frac{E_q}{E_0}= \frac{0.025}{1.0}=0.025 = 2.5\%.
$$

**Attractor radius.**

$$
r_q = \frac{\Delta/2}{\lambda_W}= \frac{0.025}{0.5}=0.05.
$$

**Robustness budget.** Combined margin $M=0.6$. The Signal's margin erosion tolerance is $\delta < \epsilon_S = 0.1$. Fraction of combined margin:

$$
\frac{\delta}{M}= \frac{0.1}{0.6}\approx 0.1667 = 16.7\%.
$$

Thus the Signal can tolerate up to a $16.7\%$ erosion of the total loop margin before its own passivity fails.

## 5. Results

All results are direct outputs of the derivations in Section 4.

* **R1 (integrator passivity).** The pure integrator is exactly passive under $y_k = x_k + \tfrac{1}{2}u_k$; supply equals storage change identically (Section 4.1).

* **R2 (leaky integrator passivity).** For any $\alpha\in(0,1]$ the leaky integrator is strictly passive under $y_k = (1-\alpha)x_k + \tfrac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \tfrac{\alpha^{2}}{2}$. At $\alpha=0.1$ the margin is $-0.095\,x_k^{2}$ (Section 4.2). The naive output $y_k = x_k$ fails, with counterexample margin $+0.505$ (Section 4.2).

* **R3 (quantization budget, corrected interpretation).** With $q=0.1$, $|u_k|\le1$, and $N=100$, the worst-case cumulative passivity degradation is $\Delta_{\text{quant}} = 5.0$ energy units (Section 4.3). The budget is tolerable only when the accumulated dissipation $\delta\sum_k x_k^{2}$ reaches $5.0$; under a constant-magnitude assumption this requires states of magnitude at least $0.726$. States smaller than this leave a positive net deficit.

* **R4 (delay margin, illustrative).** Delay phase lag $0.5\ \text{rad}\approx28.65^{\circ}$; safety ratio $\rho \approx 4.71$ (Section 4.4).

* **R5 (quantization energy cost, illustrative).** $E_q = 0.025\ \text{J}$ per packet, i.e. $2.5\%$ of the nominal supply bound (Section 4.4).

* **R6 (attractor radius, illustrative).** $r_q = 0.05$ in normalized Worker units (Section 4.4).

* **R7 (robustness budget, illustrative).** Margin erosion tolerance $16.7\%$ of the combined loop margin (Section 4.4).

**Projection.** For any future specification of Signal dynamics, the formulas of Sections 4.3–4.4 apply unchanged. The qualitative conclusions—exact integrator passivity under the corrected output, failure under the naive output, positive safety ratio, percent-level quantization cost, nonzero attractor radius—hold for any parameter set satisfying $\epsilon_S,\epsilon_W>0$ and $\rho>1$. Quantitative values are example-specific and follow exactly from the stated inputs.

## 6. Discussion

**What the framing buys.** By recasting the Signal as a passive controller, the ontological claim becomes a checkable dissipation inequality. This connects to design templates where passivity is enforced by construction ([1]), preserved across transport delays ([2]), and compatible with quantized sampled delivery ([3]). The derivations demonstrate that the framing yields concrete, arithmetic-checkable quantities (R1–R7).

**The corpus connection.** The dissipation rate $\delta = \alpha - \tfrac{\alpha^{2}}{2}$ operationalizes the corpus's passive-versus-driven distinction. In the corpus's terms [10], an actively driven system requires continuous external energy (effectively $\delta\approx0$), whereas a leaky Signal with $\alpha>0$ dissipates stored instruction even without supply, matching the passive structural control described in the ontology, where information encoded in structure achieves stability with minimal energy cost. The mapping is structural; the corpus supplies no numerical LCI values, so calibration remains open.

**The corrected interpretation and why the error mattered.** The published Section 4.3 stated that the quantization budget is tolerable only for states *small enough* that $\delta\sum_k x_k^{2}$ stays above $5.0$. The inequality $\delta\sum_k x_k^{2} \ge \Delta_{\text{quant}}$ admits only the opposite reading: the dissipation must reach the budget, and dissipation grows with state magnitude. A second reading of the same derivation confirms the correction: at constant magnitude $x_\ast$, the threshold $x_\ast \ge 0.726$ is a *lower* bound, so states below it fail and states above it pass. The practical consequence reverses: small-signal operation is the fragile regime, not the safe one, and a designer must either increase signal amplitude, reduce $q$, shorten $N$, or reduce $U_{\max}$ to protect small states.

**Limitations and failure modes.**
1. *Postulated dynamics.* The integrator models are assumptions; any different Signal dynamics require a new storage-function derivation.
2. *Quadratic storage.* The analysis relies on $V(x)=\tfrac{1}{2}x^{2}$; alternative storage functions could alter passivity conclusions.
3. *Scalar system.* Extensions to multi-input, multi-state systems are non-trivial and not covered.
4. *Illustrative parameters.* Numbers in Section 4.4 are chosen for illustration; real systems will have different values.
5. *Bounded input and finite horizon.* The quantization budget scales linearly with $N$ and $U_{\max}$; longer horizons or larger inputs increase degradation.
6. *Delay model.* The margin proxy $\rho$ is heuristic; a full $\sigma$-stability proof of the kind performed in [2] would be required for rigorous guarantees.
7. *Model uncertainty.* As shown in [4], parametric uncertainty can invalidate safety guarantees, and adaptive mechanisms are needed to retain them; the robustness budget R7 quantifies only a first-order erosion.
8. *Packet loss.* The analysis does not incorporate weakly-hard loss sequences; the LMI framework of [7] would be needed for such extensions.
9. *Discontinuity treatment.* Quantization is treated as an additive bounded perturbation, following the perturbation view of [8]; regularity conditions required by that theorem are not verified here.

**What would falsify the claims.**
* A concrete Signal dynamics specification for which no storage function $V_S$ satisfies the dissipation inequality for any output map of the form $y_k=\beta x_k+\gamma u_k$.
* An arithmetic error in the counterexample margin (e.g., if the computed margin were not $+0.505$ under the naive output).
* A demonstration that the corrected threshold direction is wrong: a construction in which states smaller than $0.726$ retain a non-negative net margin under the stated assumptions would falsify the corrected interpretation.
* Empirical evidence that the corpus's passive structural control requires the Signal to inject energy without prior supply, contradicting the passive-controller interpretation.

**Limitations list (assumptions and sensitivity).**

1. *Postulated dynamics* – exact for the integrator models; any deviation requires re-derivation.
2. *Quadratic storage* – moderate sensitivity; alternative storage may change passivity status.
3. *Scalar state/input* – high sensitivity for multi-channel Signals.
4. *Illustrative parameters* – complete sensitivity; numerical values scale directly with chosen parameters.
5. *Bounded input and horizon* – linear sensitivity in both $U_{\max}$ and $N$; the threshold $x_\ast$ scales as $\sqrt{N U_{\max} q/(2\delta N)} = \sqrt{U_{\max} q/(2\delta)}$, independent of $N$ under the constant-magnitude assumption.
6. *Delay model* – heuristic; quantitative safety ratio depends on chosen $\omega_c$ and $T_d$.
7. *No physics imported* – the analysis remains at the block-diagram level; physical implementation constraints are external.

No human-conducted experiment, measurement, survey, peer review, or