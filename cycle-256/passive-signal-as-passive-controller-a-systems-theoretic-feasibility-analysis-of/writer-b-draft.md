# Passive Signal as Passive Controller: A Systems-Theoretic Feasibility Analysis of the Signal-Worker Ontology, Revised

## Abstract

Engineers who must stabilize fragile quantum or mesoscopic states currently choose between active control, which injects energy continuously and fails when the drive is removed, and passive structural control, which lacks a general certification theory. The Signal-Worker (S-W) ontology interprets the boson as a *signal*—a delocalized field instruction—and the fermion as a *worker*—the localized state that performs work, and proposes that passive, structure-encoded control is thermodynamically superior to active control. The specific gap is that this ontological claim has never been connected to a checkable control-theoretic certificate: no dissipation inequality, storage function, or output map has been derived for the Signal as a controller block. This paper treats the Signal as a discrete-time controller block and derives, with every arithmetic step shown, (i) exact passivity of a pure integrator under the output $y_k = x_k + \tfrac{1}{2}u_k$, (ii) strict passivity of a leaky integrator under $y_k = (1-\alpha)x_k + \tfrac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \tfrac{\alpha^{2}}{2}$, giving a margin of $-0.095\,x_k^{2}$ at $\alpha = 0.1$, (iii) a counterexample showing the naive output $y_k = x_k$ fails with margin $+0.505$, and (iv) a worst-case quantization degradation of $5.0$ energy units over $N = 100$ steps at resolution $q = 0.1$, tolerable only when the state magnitude reaches $x_{*} \geq 0.726$. An illustrative example quantifies a delay safety ratio $\rho \approx 4.71$, a quantization energy cost of $2.5\%$ per packet, an attractor radius $r_q = 0.05$, and a robustness budget of $16.7\%$ margin erosion tolerance. The work sits at Technology Readiness Level 1-2; the smallest next test is storage-function fitting for any concrete Signal dynamics.

## 1. Introduction

Engineers who must stabilize fragile quantum or mesoscopic states—superconducting devices, light-induced superconducting materials, or biological energy-transfer structures—face a concrete trade-off between two control paradigms today. Active control continuously injects energy into the system: it achieves stabilization at high thermodynamic cost, and the stabilized state decays as soon as the drive is removed. Passive control encodes stabilizing information in the structure of the environment itself: it is cheap and persistent, but no general theory currently exists that lets an engineer certify that a proposed passive structure behaves as a controller, in the sense of satisfying a dissipation inequality with a storage function. The cost of this gap is practical: without a certificate, a passive design cannot be compared against an active one on a common footing, cannot be designed against specifications, and cannot be falsified by experiment. A working certificate would change the design decision: an engineer could accept or reject a candidate passive structure by checking one inequality, rather than arguing about thermodynamic superiority in the abstract.

The Signal-Worker ontology addresses this trade-off at the level of physical interpretation. It interprets the boson as a *signal*—a delocalized field instruction—and the fermion as a *worker*—the localized state that performs work, and hypothesizes a Complexity-Efficiency relationship linking scaffold complexity to stabilization performance [10]. That work analyzes actively driven systems (light-induced superconductivity, high-pressure hydrides, dynamical instabilities) as sharing the architectural motif of reliance on an external, energy-intensive Signal, and passive systems (proximity effects, Moiré engineering, biological scaffolds) as relying on an intrinsic, architectural Signal [10]. The missing bridge is precise: does the Signal, modeled as a control block, satisfy a dissipation inequality with a storage function? Without that bridge, the ontology's central engineering question cannot be certified, designed against, or falsified.

A prior feasibility analysis [9] restated the Signal as a discrete-time controller block, derived output transformations for integrator-type dynamics, and bounded passivity degradation caused by output quantization. That work produced arithmetic-checkable quantities but stopped at the block-diagram level, left the connection to the ontology's thermodynamic arguments implicit, and did not state the engineering pathway. The present paper is a revision of that analysis: it re-derives every result with full arithmetic, examines the interpretation of the quantization budget against the derivation itself, and completes the pathway.

A specific interpretive question is settled here. The quantization budget of Section 4.3 has been subject to two readings: one under which the budget is tolerable only for states *large enough* that the total dissipation $\delta \sum_{k} x_k^{2}$ stays above $5.0$, and one under which it is tolerable only for states *small enough*. The derivation in Section 4.3 supports the first reading and refutes the second: the absolute error budget $N U_{\max} q/2$ is independent of the state magnitude, while the dissipation $\delta \sum_{k} x_k^{2}$ increases monotonically with state magnitude, so shrinking the state shrinks the dissipation and enlarges the violation. A second, independent check—the per-step sufficient condition $\delta x_{*}^{2} \geq U_{\max} q/2$—yields the same threshold $x_{*} \geq 0.726$, confirming the first reading.

The contributions are:

1. A block-diagram formalization of the Signal-Worker decomposition as a discrete-time passivity problem, with definitions of passivity, strict passivity, and dissipation rate (Section 3).
2. Exact derivations, with every arithmetic step shown, of the output maps under which pure and leaky integrator Signals are passive, including a counterexample for the naive output $y_k = x_k$ (Section 4.1-4.2).
3. A worst-case quantization degradation bound $\Delta_{\text{quant}} = N U_{\max} q/2 = 5.0$ energy units at the stated operating point, a state-magnitude threshold $x_{*} \geq 0.726$ derived two independent ways, and an explicit refutation of the small-state reading of the budget (Section 4.3).
4. An illustrative example, with all parameters labeled as choices rather than measurements, quantifying delay safety ratio ($\rho \approx 4.71$), quantization energy cost ($2.5\%$ per packet), attractor radius ($r_q = 0.05$), and robustness budget ($16.7\%$ margin erosion tolerance) (Section 4.4).
5. A mapping between the derived dissipation rate $\delta$ and the ontology's passive-versus-driven distinction, with the calibration status stated honestly (Section 6).
6. A practical pathway: named users, a Technology Readiness Level assessment, the smallest next test, binding constraints, order-of-magnitude projections, and misuse risks (Section 7).

## 2. Background and Related Work

**Passivity-by-construction controllers.** The passive iFID work [1] designs controllers as the parallel action of an integrator and a finite impulse response filter, with transfer function $C(z) = \frac{\gamma T_{s}}{1-z^{-1}} + \sum_{k=0}^{m-1} g_{k} z^{-k}$, where the integrator is discretized by backward Euler with sampling period $T_{s}$ and $\gamma$ is the integral gain. The design enforces passivity through convex constraints combining virtual reference feedback tuning with a Kalman-Yakubovich-Popov-based formulation, requires no plant model, and guarantees closed-loop stability by construction for passive plants [1]. This supports the present paper's central move: an integrator-based Signal block can be rendered passive by construction, provided the output map is chosen correctly, which is exactly what Section 4 derives.

**Passivity across delays.** The delayed-PI work [2] treats a delayed communication channel as a transport partial differential equation and shows that although passivity arguments fail for a raw delay—because the Nyquist plot of a pure delay does not lie in the right half of the complex plane—a scattering transformation restores passivity of the overall loop, yielding a closed-loop system of neutral type. Its $\sigma$-stability analysis characterizes the set of controller gains for which all characteristic roots have real parts below $-\sigma$, and finds that the optimal scattering design parameter is independent of both plant parameters and the delay, with decay ratios almost twice those of the literature default [2]. Section 4.4 borrows the structural idea that a transport delay between Signal and Worker erodes margin, while stopping short of a full $\sigma$-stability proof.

**Quantized control.** The sampled-data quantized-control work [3] designs sampled-data state feedback for continuous-time linear plants with uniform input quantization $q_{\Delta}(u_{p})$ acting on the actuated input, formulated as a hybrid system with an auxiliary clock variable triggering sampling events. It proves uniform global asymptotic stability of an attractor surrounding the origin, gives sufficient conditions as bilinear matrix inequalities, and provides an algorithm that minimizes the size of the closed-loop attractor [3]. Section 4.3 uses the same modeling stance—quantization as a bounded perturbation of an ideal inequality—and Section 4.4's attractor radius is the scalar analogue of the attractor set in [3].

**Safety under model uncertainty.** The composite adaptive control barrier function work [4] establishes that control barrier function guarantees fail when model parameters are incorrect, because the calculated safe control input may drive the system into the unsafe region, and builds an adaptation law from a composite energy function coupling a logarithmic safety barrier, a control Lyapunov function, and a quadratic parameter-error term. Its theorems show the safe set remains forward invariant for all bounded parameters, that the guarantee survives bounded state-derivative measurement errors, and that the admissible control set strictly contains the robust set [4]. Section 6 uses this as the template for the limitation that parametric uncertainty can invalidate the passivity margin computed here.

**Robustness budgets.** The system-level-synthesis robust control work [5] decomposes an uncertain nonlinear system, via a first-order Taylor expansion, into a nominal nonlinear trajectory and an error system described as an uncertain linear time-varying system, and jointly optimizes the nominal trajectory, the affine error feedback, and dynamic linearization error over-bounds for robust constraint satisfaction; the reachable set is tight for linear systems with affine feedback [5]. Section 4.4's robustness budget—how much margin erosion the Signal can absorb—follows the same nominal-plus-bounded-error logic in scalar form.

**Input-constrained safety.** The input-constrained control barrier function work [6] addresses the case where control authority is limited: only a subset of the safe set can then be rendered forward invariant, and the method constructs nested intermediate sets whose intersection forms an inner safe set, demonstrated on adaptive cruise control and spacecraft rendezvous [6]. Section 4.4's attractor radius plays the same role here: quantized, bounded outputs act as an input constraint, and the guarantee shrinks from the origin to a ball of radius $r_q$.

**Lossy channels.** The weakly-hard real-time control work [7] models feedback-channel failures with window-based constraints—for example that at least $r$ of every $s$ control attempts succeed—and derives sufficient linear matrix inequality conditions under which the switched closed-loop system has $\ell_{2}$-performance with gain $\gamma$, using a lifting that discretizes the system at successful instants and typically reduces computational complexity [7]. Section 7 identifies the integration of such loss constraints with the dissipation inequality as an open extension; no result of this paper depends on [7].

**Discontinuous limits.** The projected dynamical systems work [8] proves that the vector field of a CBF-controlled system is a Krasovskii-like perturbation of the set-valued map of a differential inclusion, with a quantitative bound on the perturbation, and that trajectories of the CBF-controlled system uniformly converge to trajectories of the projected dynamical system [8]. Section 4.3 treats quantization as a bounded additive perturbation in the same spirit; the regularity conditions required by a theorem of that type are not verified here, which is stated as a limitation.

**The prior feasibility analysis.** The predecessor [9] formalized the Signal as a discrete-time block, derived exact passivity for a pure integrator under $y_k = x_k + \tfrac{1}{2}u_k$, strict passivity for a leaky integrator with $\delta = \alpha - \tfrac{\alpha^{2}}{2}$, and a worst-case quantization degradation of $5.0$ energy units, and reported the threshold $x_{*} \geq 0.726$ [9]. The present paper re-derives those results with every arithmetic step visible, adds the two-way check on the state threshold, resolves the interpretation question, and supplies the engineering pathway.

**The ontological source.** The Signal-Worker ontology [10] builds its framework on the premise that information is physical and that maintaining the order of a quantum state has an irreducible energy cost quantified by Landauer's principle, and introduces two complexity metrics: Krylov complexity for the dynamical complexity of the quantum state (the Worker) and the Lossless Complexity Index (LCI) for the structural complexity of the environment (the Signal or scaffold) [10]. It classifies actively driven systems—light-induced superconductivity, high-pressure hydrides, dynamical instabilities—as sharing reliance on an external, energy-intensive Signal with consequences of thermodynamic inefficiency, transience, and dynamical instability, and passive systems—proximity effects, Moiré engineering, biological scaffolds—as achieving high stability with minimal energy cost by encoding information in structure, with the FMO complex's phononic scaffold as a concrete design target [10]. Section 6 maps the dissipation rate $\delta$ onto this passive-versus-driven distinction; the ontology supplies no dynamical equations or numerical LCI values, so the mapping remains structural and uncalibrated.

## 3. Methods

### 3.1 Definitions

**Discrete-time passivity.** A discrete-time system with state $x_k \in \mathbb{R}^n$, input $u_k \in \mathbb{R}$, and output $y_k \in \mathbb{R}$ is *passive* if there exists a storage function $V(x) \geq 0$ with $V(0) = 0$ such that for all $k$,

$$
V(x_{k+1}) - V(x_k) \leq u_k\, y_k .
$$

The right-hand side $u_k y_k$ is the *supply rate*: the energy the block extracts from its environment per step.

**Strict passivity with dissipation rate.** If additionally

$$
V(x_{k+1}) - V(x_k) \leq u_k\, y_k - \delta\, x_k^{2}, \qquad \delta > 0,
$$

the system is *strictly passive* with dissipation rate $\delta$. The term $\delta x_k^{2}$ is energy the block removes from its state per step even when the supply is zero; it is the quantity that will later be mapped onto the ontology's passive-versus-driven distinction.

**Block interpretation of the S-W ontology.** The mapping from the ontology [10] to a control block diagram is:

```
u_k (instruction) ──> [ SIGNAL ] ──y_k──> [ WORKER ] ──> work output
                       (delocalized)    (localized state)
```

The research question becomes: does a storage function $V_{S}$ exist such that the Signal block alone satisfies the dissipation inequality?

### 3.2 Candidate Signal dynamics

The ontology provides no dynamical equations, so the analysis covers the two minimal candidate dynamics, stated as assumptions of the model:

*Pure integrator:* $x_{k+1} = x_k + u_k$.

*Leaky integrator* (leakage $\alpha \in [0,1]$): $x_{k+1} = (1-\alpha)x_k + u_k$.

For both, the quadratic storage function $V(x) = \tfrac{1}{2}x^{2}$ is the natural candidate because it is positive definite and radially unbounded. The analysis seeks output maps of the affine form $y_k = \beta x_k + \gamma u_k$ that satisfy the dissipation inequality; the coefficients $\beta$ and $\gamma$ are the design variables.

### 3.3 Perturbation analysis under quantization and delay

Following the modeling stance of the quantized-actuator literature [3], uniform output quantization of resolution $q$ is treated as a bounded perturbation of the ideal passive inequality over a finite horizon. The illustrative example of Section 4.4 additionally evaluates delay-phase loss using the transport-delay picture of [2] and a robustness budget in the nominal-plus-bounded-error spirit of [5]. All perturbation results are bounds derived by arithmetic; no simulation is performed.

## 4. Analysis

All numerical inputs are either structural constants of the candidate dynamics or explicitly stated illustrative parameters. Every arithmetic step is shown.

### 4.1 Exact passivity of the pure integrator

**Setup.** Dynamics $x_{k+1} = x_k + u_k$; storage $V(x) = \tfrac{1}{2}x^{2}$; output $y_k = \beta x_k + \gamma u_k$.

**Step 1: storage change.**

$$
V(x_{k+1}) - V(x_k) = \frac{1}{2}(x_k + u_k)^{2} - \frac{1}{2}x_k^{2} = x_k u_k + \frac{1}{2}u_k^{2}.
$$

**Step 2: passivity requirement.** Require

$$
x_k u_k + \frac{1}{2}u_k^{2} \leq u_k(\beta x_k + \gamma u_k) = \beta x_k u_k + \gamma u_k^{2},
$$

that is,

$$
(1 - \beta)x_k u_k + \left(\frac{1}{2} - \gamma\right)u_k^{2} \leq 0 \quad \forall x_k, u_k.
$$

**Step 3: coefficient choice.** The mixed term $x_k u_k$ takes both signs over admissible pairs, so its coefficient must vanish: $\beta = 1$. Then $\frac{1}{2} - \gamma \leq 0$ forces $\gamma \geq \frac{1}{2}$. The minimal exactly-passive choice is $\gamma = \frac{1}{2}$, giving

$$
y_k = x_k + \frac{1}{2}u_k, \qquad u_k y_k = x_k u_k + \frac{1}{2}u_k^{2} = V(x_{k+1}) - V(x_k).
$$

**Numerical check.** With $x_0 = 0$, $u_0 = 0.1$: $x_1 = 0 + 0.1 = 0.1$; $V(x_1) = \tfrac{1}{2}(0.1)^{2} = 0.005$; $\Delta V = 0.005 - 0 = 0.005$. The output is $y_0 = 0 + \tfrac{1}{2}(0.1) = 0.05$, so $u_0 y_0 = 0.1 \times 0.05 = 0.005$. Supply equals storage change exactly; equality holds and confirms exact passivity.

### 4.2 Passivity of the leaky integrator

**Setup.** Dynamics $x_{k+1} = (1-\alpha)x_k + u_k$ with $\alpha \in [0,1]$; storage $V(x) = \tfrac{1}{2}x^{2}$; output $y_k = \beta x_k + \gamma u_k$.

**Step 1: storage change.**

$$
\begin{aligned}
V(x_{k+1}) - V(x_k)
&= \frac{1}{2}\bigl[(1-\alpha)x_k + u_k\bigr]^{2} - \frac{1}{2}x_k^{2} \\
&= \frac{1}{2}\Bigl[(1-\alpha)^{2}x_k^{2} + 2(1-\alpha)x_k u_k + u_k^{2}\Bigr] - \frac{1}{2}x_k^{2} \\
&= \left(-\alpha + \frac{\alpha^{2}}{2}\right)x_k^{2} + (1-\alpha)x_k u_k + \frac{1}{2}u_k^{2}.
\end{aligned}
$$

**Step 2: subtract supply.**

$$
V(x_{k+1}) - V(x_k) - u_k y_k
= \left(-\alpha + \frac{\alpha^{2}}{2}\right)x_k^{2} + (1 - \alpha - \beta)x_k u_k + \left(\frac{1}{2} - \gamma\right)u_k^{2}.
$$

**Step 3: coefficient choice.** To eliminate the mixed term for all admissible pairs, set $\beta = 1 - \alpha$. Setting $\gamma = \frac{1}{2}$ removes the $u_k^{2}$ term. The remaining coefficient of $x_k^{2}$ is $-\alpha + \frac{\alpha^{2}}{2} = -\delta$ with

$$
\delta = \alpha - \frac{\alpha^{2}}{2} > 0 \quad \text{for } \alpha \in