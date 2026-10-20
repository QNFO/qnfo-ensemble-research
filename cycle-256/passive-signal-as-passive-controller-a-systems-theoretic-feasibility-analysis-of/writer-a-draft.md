# Passive Signal as Passive Controller: A Systems-Theoretic Feasibility Analysis of the Signal‑Worker Ontology

## Abstract

The Signal‑Worker (S‑W) ontology interprets the boson as a *signal*—a delocalized field instruction—and the fermion as a *worker*—the localized state that performs work, proposing that passive, structure‑encoded control is thermodynamically superior to active, energy‑intensive control. This paper bridges the ontological claim to control‑theoretic certification by treating the Signal as a discrete‑time controller block and deriving, with full arithmetic, (i) exact passivity of a pure integrator under the modified output \(y_k = x_k + \tfrac{1}{2}u_k\), (ii) strict passivity of a leaky integrator under \(y_k = (1-\alpha)x_k + \tfrac{1}{2}u_k\) with dissipation rate \(\delta = \alpha - \tfrac{\alpha^{2}}{2}\) (margin \(-0.095\,x_k^{2}\) at \(\alpha = 0.1\)), and (iii) a worst‑case passivity degradation of \(5.0\) energy units over \(N = 100\) steps with quantization resolution \(q = 0.1\). An illustrative example quantifies delay margin (\(\rho \approx 4.71\)), quantization energy cost (\(2.5\%\) per packet), attractor radius (\(r_q = 0.05\)), and robustness budget (\(16.7\%\) margin erosion tolerance). The result is placed at Technology Readiness Level 1–2, and the smallest next test is a storage‑function fitting for any concrete Signal dynamics.

## 1. Introduction

Engineers who must stabilize fragile quantum or mesoscopic states—such as superconducting devices, driven materials, or biological energy‑transfer structures—currently face a trade‑off between two control paradigms. Active control continuously injects energy, achieving stabilization at high thermodynamic cost and loss of stability when the drive is removed. Passive control encodes stabilizing information in the environment’s structure, offering cheap and persistent stabilization but lacking a general theory to guarantee that a proposed passive structure indeed behaves as a controller. The Signal‑Worker ontology addresses this trade‑off by interpreting active quantum control as reliance on an external, energy‑intensive Signal and passive structural control as relying on an intrinsic, architectural Signal, hypothesizing a Complexity‑Efficiency relationship linking scaffold complexity to stabilization performance. The missing bridge is a precise control‑theoretic statement—does the Signal satisfy a dissipation inequality with a storage function? Without such a bridge, the ontology’s central engineering question cannot be certified, designed against, or falsified.

A prior feasibility analysis [9] restated the Signal as a discrete‑time controller block, derived output transformations for integrator‑type dynamics, and bounded passivity degradation caused by output quantization. That work produced arithmetic‑checkable quantities but stopped at the block‑diagram level, omitted connections to the corpus’s thermodynamic arguments, and left the engineering pathway unspecified.

This paper completes the arc. Contributions are:

1. A block‑diagram formalization of the Signal‑Worker decomposition as a discrete‑time passivity problem (Section 3).  
2. Exact derivations, with every arithmetic step shown, of the output maps under which pure and leaky integrator Signals are passive, including a counterexample for the naive output (Section 4).  
3. A worst‑case quantization degradation bound (\(5.0\) energy units over \(100\) steps at \(q = 0.1\)) and an illustrative example quantifying delay margin, quantization energy cost, attractor radius, and robustness budget (Sections 4.3–4.4, summarized in Section 5).  
4. A mapping between the derived dissipation rate \(\delta\) and the corpus’s passive‑versus‑driven distinction (Section 6).  
5. A practical pathway: identification of users, TRL assessment, the smallest next test, and the primary engineering constraints (Section 7).

## 2. Background and Related Work

**[1] Passive iFIR Filters for Data‑Driven Control.** The work designs passive controllers as the parallel action of an integrator and a finite‑impulse‑response filter, with transfer function \(C(z)=\frac{\gamma T_s}{1-z^{-1}}+\sum_{k=0}^{m-1}g_k z^{-k}\). It shows that for passive plants the closed‑loop stability is guaranteed by construction and that the design requires no plant model, directly supporting the notion that an integrator‑based Signal block can be rendered passive by construction.

**[2] Passivity‑based PI control of first‑order systems with I/O communication delays.** This paper treats a delayed communication channel as a transport PDE and proves that the overall loop remains passive when a scattering transformation is applied, despite the Nyquist plot of a pure delay lying outside the right‑half plane. The result motivates the delay‑margin analysis in Section 4.4, where a transport delay models the spatial separation between Signal and Worker.

**[3] Sampled‑data control design for systems with quantized actuators.** The authors design sampled‑data state feedback for continuous‑time linear systems with uniform input quantization; this design is used as a basis for the quantization analysis in Section 4.3. Their framework underpins the quantization analysis of Section 4.3, treating the quantized Signal output as a bounded perturbation of the ideal passive inequality.

**[4] Composite Adaptive Control Barrier Functions for Safety‑Critical Systems with Parametric Uncertainty.** This work shows that safety guarantees based on control barrier functions can fail under parametric uncertainty, and introduces adaptive mechanisms to retain safety. It illustrates the broader theme that model uncertainty can invalidate guarantees, which is reflected in the limitations discussion of Section 6.

**[5] Robust Nonlinear Optimal Control via System Level Synthesis.** The authors decompose an uncertain nonlinear system into a nominal trajectory and a norm‑bounded error, jointly optimizing both. Their nominal‑plus‑error decomposition informs the robustness‑budget calculation in Section 4.4, where the Signal’s passivity margin is eroded by a bounded deviation.

**[6] Safe Control Synthesis via Input Constrained Control Barrier Functions.** This paper introduces Input‑Constrained CBFs that construct inner safe sets when full input authority is unavailable. The attractor‑radius result of Section 4.4 mirrors the inner‑safe‑set construction, highlighting how quantized, bounded outputs can be interpreted as input constraints.

**[7] On \(\ell_2\)-performance of weakly‑hard real‑time control systems.** The authors develop LMI conditions for \(\ell_2\) performance under weakly‑hard packet‑loss constraints, showing how loss sequences can be modeled and analyzed. Their framework motivates the discussion of packet‑loss constraints as a future extension in Section 7(d).

**[8] On the relationship between control barrier functions and projected dynamical systems.** This work proves that CBF‑controlled systems are Krasovskii‑like perturbations of projected dynamical systems, providing a quantitative bound on the perturbation. It supports the treatment of quantization as a bounded additive perturbation in Section 4.3.

**[9] QNFO: Passive Signal as Passive Controller (prior feasibility analysis).** The predecessor formalized the Signal as a discrete‑time block, derived exact passivity for a pure integrator, strict passivity for a leaky integrator, and a worst‑case quantization degradation of \(5.0\) energy units. The present paper re‑derives those results with full arithmetic, extends them with an illustrative example, and adds the engineering pathway the predecessor lacked.

**[10] QNFO: Structural vs Driven Quantum Coherence.** The corpus introduces the Signal‑Worker ontology, distinguishes active (driven) from passive (structural) control, and motivates a thermodynamic efficiency analysis of scaffold complexity, providing the conceptual motivation for the control‑theoretic framing.

## 3. Methods

### 3.1 Definitions

**Discrete‑time passivity.** A discrete‑time system with state \(x_k\in\mathbb{R}^n\), input \(u_k\in\mathbb{R}\), and output \(y_k\in\mathbb{R}\) is *passive* if there exists a storage function \(V(x)\ge 0\) with \(V(0)=0\) such that for all \(k\),

$$
V(x_{k+1}) - V(x_k) \le u_k\,y_k .
$$

The right‑hand side \(u_k y_k\) is the *supply rate*.

**Strict passivity with dissipation rate.** If additionally

$$
V(x_{k+1}) - V(x_k) \le u_k\,y_k - \delta\,x_k^{2},
\qquad \delta > 0,
$$

the system is strictly passive with dissipation rate \(\delta\).

**Block interpretation of the S‑W ontology.** The mapping from the corpus [10] to a control block diagram is

```
u_k (instruction) ──► [ SIGNAL ] ──y_k──► [ WORKER ] ──► work output
                        (delocalized)   (localized state)
```

The research question becomes: does a storage function \(V_S\) exist such that the Signal block alone satisfies the dissipation inequality?

### 3.2 Candidate Signal dynamics

Because the corpus provides no dynamical equations, we analyze the two minimal candidate dynamics:

*Pure integrator:* \(x_{k+1}=x_k+u_k\).

*Leaky integrator* (leakage \(\alpha\in[0,1]\)): \(x_{k+1}=(1-\alpha)x_k+u_k\).

For both, the quadratic storage function \(V(x)=\tfrac{1}{2}x^{2}\) is natural. The analysis seeks output maps \(y_k=\beta x_k+\gamma u_k\) that satisfy the dissipation inequality.

### 3.3 Perturbation analysis under quantization and delay

Following the quantized‑actuator framework of [3], we bound how uniform input quantization of resolution \(q\) degrades the passivity inequality over a finite horizon. In the illustrative example (Section 4.4) we also evaluate delay‑phase loss using the transport‑delay model of [2] and a robustness budget inspired by the nominal‑plus‑error decomposition of [5].

## 4. Analysis

All numerical inputs are either structural constants of the candidate dynamics or explicitly stated illustrative parameters. Every arithmetic step is shown.

### 4.1 Exact passivity of the pure integrator

**Setup.** Dynamics \(x_{k+1}=x_k+u_k\); storage \(V(x)=\tfrac{1}{2}x^{2}\); output \(y_k=\beta x_k+\gamma u_k\).

**Step 1: storage change.**

\[
V(x_{k+1})-V(x_k)=\frac{1}{2}(x_k+u_k)^{2}-\frac{1}{2}x_k^{2}
= x_k u_k+\frac{1}{2}u_k^{2}.
\]

**Step 2: passivity requirement.** Require

\[
x_k u_k+\frac{1}{2}u_k^{2}\le u_k(\beta x_k+\gamma u_k)
= \beta x_k u_k+\gamma u_k^{2},
\]

i.e.

\[
(1-\beta)x_k u_k+\Bigl(\frac{1}{2}-\gamma\Bigr)u_k^{2}\le 0
\quad\forall x_k,u_k.
\]

**Step 3: coefficient choice.** The mixed term changes sign unless its coefficient vanishes, so \(\beta=1\). Then \(\frac{1}{2}-\gamma\le 0\) forces \(\gamma\ge\frac{1}{2}\). The minimal exactly‑passive choice is \(\gamma=\frac{1}{2}\), giving

\[
y_k = x_k + \frac{1}{2}u_k,
\qquad
u_k y_k = x_k u_k + \frac{1}{2}u_k^{2}
= V(x_{k+1})-V(x_k).
\]

**Numerical check.** With \(x_0=0\), \(u_0=0.1\):
\(x_1=0.1\), \(V(x_1)=0.005\), \(\Delta V=0.005\);
\(y_0=0+0.05=0.05\), \(u_0 y_0=0.005\). Equality holds, confirming exact passivity.

### 4.2 Passivity of the leaky integrator

**Setup.** Dynamics \(x_{k+1}=(1-\alpha)x_k+u_k\) with \(\alpha\in[0,1]\); storage \(V(x)=\tfrac{1}{2}x^{2}\); output \(y_k=\beta x_k+\gamma u_k\).

**Step 1: storage change.**

\[
\begin{aligned}
V(x_{k+1})-V(x_k)
&=\frac{1}{2}\bigl[(1-\alpha)x_k+u_k\bigr]^{2}-\frac{1}{2}x_k^{2}\\
&=\frac{1}{2}\Bigl[(1-\alpha)^{2}x_k^{2}+2(1-\alpha)x_k u_k+u_k^{2}\Bigr]-\frac{1}{2}x_k^{2}\\
&=\Bigl(-\alpha+\frac{\alpha^{2}}{2}\Bigr)x_k^{2}+(1-\alpha)x_k u_k+\frac{1}{2}u_k^{2}.
\end{aligned}
\]

**Step 2: subtract supply.**

\[
\begin{aligned}
V(x_{k+1})-V(x_k)-u_k y_k
&=\Bigl(-\alpha+\frac{\alpha^{2}}{2}\Bigr)x_k^{2}
+\bigl(1-\alpha-\beta\bigr)x_k u_k
+\Bigl(\frac{1}{2}-\gamma\Bigr)u_k^{2}.
\end{aligned}
\]

**Step 3: coefficient choice.** To eliminate the mixed term we set \(\beta = 1-\alpha\). Setting \(\gamma=\frac{1}{2}\) removes the \(u_k^{2}\) term. The remaining coefficient of \(x_k^{2}\) is \(-\alpha+\frac{\alpha^{2}}{2}= -\delta\) with

\[
\delta = \alpha - \frac{\alpha^{2}}{2} > 0 \quad\text{for }\alpha\in(0,1].
\]

Thus the passive output is

\[
y_k = (1-\alpha)x_k + \frac{1}{2}u_k,
\qquad
V(x_{k+1})-V(x_k) \le u_k y_k - \delta x_k^{2}.
\]

**Numerical verification for \(\alpha=0.1\).**  
\(\beta = 0.9\), \(\gamma = 0.5\), \(\delta = 0.1 - 0.005 = 0.095\).  

*Zero supply:* \(x_0=2\), \(u_0=0\) → \(x_1=1.8\).  
\(V(x_0)=2\), \(V(x_1)=1.62\), \(\Delta V=-0.38\).  
\(-\delta x_0^{2}= -0.095\times4 = -0.38\). Equality holds.

*With supply:* \(x_0=2\), \(u_0=0.5\) → \(x_1=0.9\times2+0.5=2.3\).  
\(V(x_1)=2.645\), \(\Delta V=0.645\).  
\(y_0=0.9\times2+0.5\times0.5=2.05\), \(u_0 y_0=1.025\).  
\(\Delta V - u_0 y_0 = -0.38 = -\delta x_0^{2}\). Inequality holds with margin \(0.38\).

**Counterexample for the naive output.** With \(y_k = x_k\) (\(\beta=1,\gamma=0\)) and \(\alpha=0.1\),

\[
V(x_{k+1})-V(x_k)-u_k y_k
= -0.095 x_k^{2} -0.1 x_k u_k + 0.5 u_k^{2}.
\]

At \(x_k=1\), \(u_k=-1\) the expression equals \(-0.095 + 0.1 + 0.5 = 0.505 > 0\); passivity fails.

### 4.3 Quantization degradation bound

**Assumptions.**  
(i) Uniform output quantization with resolution \(q=0.1\) ⇒ \(|y_k - y_k^{q}| \le q/2 = 0.05\).  
(ii) The Worker receives the quantized output, so the actual supply is \(u_k y_k^{q}\).  
(iii) Input magnitude bounded: \(|u_k| \le U_{\max}=1\).  
(iv) Horizon \(N=100\) steps.

**Derivation.** Per‑step supply error:

\[
|u_k y_k - u_k y_k^{q}| = |u_k|\,|y_k-y_k^{q}|
\le U_{\max}\cdot\frac{q}{2}=0.05.
\]

Cumulative worst‑case degradation:

\[
\Delta_{\text{quant}} \le \sum_{k=0}^{N-1}0.05 = N \times 0.05 = 5.0.
\]

**Interpretation.** The leaky integrator dissipates \(\delta \sum x_k^{2}\). If state magnitudes are of order unity, the total dissipation over 100 steps is \(\delta \times 100 \approx 9.5\) (for \(\delta=0.095\)), exceeding the quantization budget; thus the budget is tolerable only for states large enough that \(\delta\sum x_k^{2} > 5.0\). A concrete threshold follows from assuming a constant state magnitude \(x_\ast\):

\[
0.095 \times 100 \times x_\ast^{2} \ge 5.0
\;\Longrightarrow\;
x_\ast^{2} \ge \frac{5.0}{9.5}\approx 0.526,
\qquad
x_\ast \ge 0.726.
\]

Under the stated assumptions, the bound \(\Delta_{\text{quant}} \le N U_{\max} q/2\) is exact and cannot be tightened without reducing \(q\), \(N\), or \(U_{\max}\).

### 4.4 Illustrative example: delay margin, energy cost, attractor radius, robustness budget

All parameters in this subsection are *illustrative choices*, stated explicitly; every derived number follows from them by shown arithmetic. No number below is an empirical measurement.

**Input list.** \(k_S = 2.0\) (static gain), \(\epsilon_S = 0.1\) (Signal margin), \(\epsilon_W = 0.2\) (Worker margin), \(T_d = 0.5\ \text{s}\) (transport delay), \(\omega_c = 1.0\ \text{rad s}^{-1}\) (crossover frequency), \(\Delta = 0.05\) (quantization step), \(u_{\max}=1.0\) (norm bound), \(\lambda_W = 0.5\ \text{s}^{-1}\) (Worker contraction constant).

**Delay margin.** Phase lag at \(\omega_c\):

\[
\phi_d = \omega_c T_d = 1.0 \times 0.5 = 0.5\ \text{rad}
= 0.5 \times \frac{180}{\pi} \approx 28.65^{\circ}.
\]

Combined dissipative margin proxy:

\[
M = k_S(\epsilon_S+\epsilon_W)=2.0\times(0.1+0.2)=0.6.
\]

Normalized delay loss:

\[
\ell_d = \frac{\phi_d}{2\pi}= \frac{0.5}{2\pi}\approx 0.0796.
\]

Normalized margin:

\[
M_n = \frac{M}{1+M}= \frac{0.6}{1.6}=0.375.
\]

Safety ratio:

\[
\rho = \frac{M_n}{\ell_d}= \frac{0.375}{0.0796}\approx 4.71.
\]

**Quantization energy cost.**  

\[
E_q \le \frac{\Delta}{2}\,u_{\max}= \frac{0.05}{2}\times1.0 = 0.025\ \text{J}.
\]

Nominal per‑packet supply bound \(E_0 = u_{\max}^{2}=1.0\ \text{J}\).  
Relative overhead:

\[
\frac{E_q}{E_0}= \frac{0.025}{1.0}=0.025 = 2.5\%.
\]

**Attractor radius.**  

\[
r_q = \frac{\Delta/2}{\lambda_W}= \frac{0.025}{0.5}=0.05.
\]

**Robustness budget.**  
Combined margin \(M=0.6\). The Signal’s margin erosion tolerance is \(\delta < \epsilon_S = 0.1\). Fraction of combined margin:

\[
\frac{\delta}{M}= \frac{0.1}{0.6}\approx 0.1667 = 16.7\%.
\]

Thus the Signal can tolerate up to a \(16.7\%\) erosion of the total loop margin before its own passivity fails.

## 5. Results

All results are direct outputs of the derivations in Section 4.

* **R1 (integrator passivity).** The pure integrator is exactly passive under \(y_k = x_k + \tfrac{1}{2}u_k\); supply equals storage change identically (Section 4.1).

* **R2 (leaky integrator passivity).** For any \(\alpha\in(0,1]\) the leaky integrator is strictly passive under \(y_k = (1-\alpha)x_k + \tfrac{1}{2}u_k\) with dissipation rate \(\delta = \alpha - \tfrac{\alpha^{2}}{2}\). At \(\alpha=0.1\) the margin is \(-0.095\,x_k^{2}\) (Section 4.2). The naive output \(y_k = x_k\) fails, with counterexample margin \(+0.505\) (Section 4.2).

* **R3 (quantization budget).** With \(q=0.1\), \(|u_k|\le1\), and \(N=100\), the worst‑case cumulative passivity degradation is \(\Delta_{\text{quant}} = 5.0\) energy units (Section 4.3). States larger than \(0.726\) in magnitude keep the net margin non‑positive.

* **R4 (delay margin, illustrative).** Delay phase lag \(0.5\ \text{rad}\approx28.65^{\circ}\); safety ratio \(\rho \approx 4.71\) (Section 4.4).

* **R5 (quantization energy cost, illustrative).** \(E_q = 0.025\ \text{J}\) per packet, i.e. \(2.5\%\) of the nominal supply bound \(E_0 = 1.0\ \text{J}\) (Section 4.4).

* **R6 (attractor radius, illustrative).** \(r_q = 0.05\) in normalized Worker units (Section 4.4).

* **R7 (robustness budget, illustrative).** Margin erosion tolerance \(16.7\%\) of the combined loop margin before Signal passivity fails (Section 4.4).

**Projection.** For any future specification of Signal dynamics, the formulas of Sections 4.3–4.4 apply unchanged. The qualitative conclusions—exact integrator passivity under the corrected output, failure under the naive output, positive safety ratio, percent‑level quantization cost, nonzero attractor radius—hold for any parameter set satisfying \(\epsilon_S,\epsilon_W>0\) and \(\rho>1\). Quantitative values are example‑specific and follow exactly from the stated inputs.

## 6. Discussion

**What the framing buys.** By recasting the Signal as a passive controller, the ontological claim becomes a checkable dissipation inequality. This connects to design templates where passivity is enforced by construction ([1]), preserved across transport delays ([2]), and compatible with quantized sampled delivery ([3]). The derivations demonstrate that the framing yields concrete, arithmetic‑checkable quantities (R1–R7).

**The corpus connection.** The dissipation rate \(\delta = \alpha - \tfrac{\alpha^{2}}{2}\) operationalizes the corpus’s passive‑versus‑driven distinction. In the corpus’s terms [10], an actively driven system requires continuous external energy (effectively \(\delta\approx0\)), whereas a leaky Signal with \(\alpha>0\) dissipates stored instruction even without supply, matching the passive structural control described in the ontology. The mapping is structural; the corpus supplies no numerical LCI values, so calibration remains open.

**Limitations and failure modes.**  
1. *Postulated dynamics.* The integrator models are assumptions; any different Signal dynamics require a new storage‑function derivation.  
2. *Quadratic storage.* The analysis relies on \(V(x)=\tfrac{1}{2}x^{2}\); alternative storage functions could alter passivity conclusions.  
3. *Scalar system.* Extensions to multi‑input, multi‑state systems are non‑trivial and not covered.  
4. *Illustrative parameters.* Numbers in Section 4.4 are chosen for illustration; real systems will have different values.  
5. *Bounded input and finite horizon.* The quantization budget scales linearly with \(N\) and \(U_{\max}\); longer horizons or larger inputs increase degradation.  
6. *Delay model.* The margin proxy \(\rho\) is heuristic; a full sigma‑stability proof would be required for rigorous guarantees.  
7. *Model uncertainty.* As shown in [4] and [6], parametric uncertainty can invalidate safety guarantees; the robustness budget R7 quantifies only a first‑order erosion.  
8. *Packet loss.* The analysis does not incorporate weakly‑hard loss sequences; the framework of [7] would be needed for such extensions.  
9. *Discontinuity treatment.* Quantization is treated as an additive bounded perturbation, following the perturbation view of [8]; regularity conditions required by that theorem are not verified here.

**What would falsify the claims.**  
* A concrete Signal dynamics specification for which no storage function \(V_S\) satisfies the dissipation inequality for any output map of the form \(y_k=\beta x_k+\gamma u_k\).  
* An arithmetic error in the counterexample margin (e.g., if the computed margin were not \(+0.505\) under the naive output).  
* Empirical evidence that the corpus’s passive structural control requires the Signal to inject energy without prior supply, contradicting the passive‑controller interpretation.

**Limitations list (assumptions and sensitivity).**  

1. *Postulated dynamics* – exact for the integrator models; any deviation requires re‑derivation.  
2. *Quadratic storage* – moderate sensitivity; alternative storage may change passivity status.  
3. *Scalar state/input* – high sensitivity for multi‑channel Signals.  
4. *Illustrative parameters* – complete sensitivity; numerical values scale directly with chosen parameters.  
5. *Bounded input & horizon* – linear sensitivity in both \(U_{\max}\) and \(N\).  
6. *Delay model* – heuristic; quantitative safety ratio depends on chosen \(\omega_c\) and \(T_d\).  
7. *No physics imported* – the analysis remains at the block‑diagram level; physical implementation constraints are external.

No human‑conducted experiment, measurement, survey, peer review, or data deposition was performed. All quantitative claims are either derived analytically in the text or labeled as projections with explicit assumptions.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and which decision, design parameter, process or policy changes if it holds.**  
The immediate users are control engineers and theorists tasked with evaluating or formalizing claims from the Signal‑Worker research programme. The result gives them a concrete certification target: a storage‑function inequality with the explicit output map $y_k=(1-\alpha)x_k+\tfrac{1}{2}u_k$ (for a leaky Signal) or $y_k=x_k+\tfrac{1}{2}u_k$ (for a pure integrator). If the result holds, the design parameter that must be implemented is the corrected output map; any implementation that reports the naive state output $y_k=x_k$ would violate passivity. A second user group is designers of passivity‑based controller structures; the iFIR pattern of [1] provides a template for constructing a Signal block that satisfies the derived output map by design rather than by postulate. Beyond these groups the work is foundational: it establishes the form of a certification question that any future physical or simulated Signal must satisfy before a deployment decision can be made.

**(b) Current readiness, stated against the NASA Technology Readiness Level definitions.**  
The work is purely analytical, has not been peer‑reviewed, and contains no experimental or simulation validation. Accordingly it resides at Technology Readiness Level 1–2 (basic principles observed and reported; formulation of a concept). Analytical work of this kind never exceeds TRL 3, and no manufacturing or deployment readiness can be claimed.

**(c) The smallest next experiment, prototype, pilot or calculation that would de‑risk or falsify the result: what is measured and which outcome refutes it.**  
The smallest de‑risking step is a calculation rather than a physical experiment. Given any concrete specification of Signal dynamics (e.g., a discrete‑time model supplied by the corpus or a candidate physical scaffold), one would attempt to fit a storage function $V_S(x)$—starting with the quadratic ansatz $V_S=\tfrac{1}{2}x^2$—such that the dissipation inequality  
$$V_S(x_{k+1})-V_S(x_k)\le u_k\,y_k-\delta\,x_k^2$$  
holds for all admissible $(x_k,u_k)$. Failure to find any output map of the form $y_k=\beta x_k+\gamma u_k$ that satisfies the inequality for the given dynamics would falsify the central claim. A second, equally minimal step is a numerical simulation of the leaky integrator with quantized output ($q=0.1$) over $N=100$ steps under the bound $|u_k|\le1$; observing a cumulative supply error exceeding the derived bound $\Delta_{\text{quant}}=5.0$ energy units would falsify the quantization‑budget claim.

**(d) The engineering, manufacturing or deployment constraints that would bind first (materials, tolerances, components, data, compute, energy, cost drivers, scale‑up, regulation), each stated only when the grounding supports it or Section 4 derives it; otherwise list it as an open question.**  
1. *Specification data.* No engineering step is possible until an explicit Signal dynamics model is provided; this is the primary binding constraint today (derived from the lack of corpus equations).  
2. *Quantization resolution.* The degradation bound $\Delta_{\text{quant}}=N\,U_{\max}\,q/2$ shows that the actuator/output resolution $q$ and the horizon $N$ are the first numerical design constraints once a dynamics model exists.  
3. *Channel delay and loss.* The safety‑ratio $\rho$ depends on transport delay $T_d$ and crossover frequency $\omega_c$; any increase in $T_d$ erodes $\rho$ and must be bounded to keep $\rho>1$ (heuristic from Section 4.4).  
4. *Model uncertainty.* The robustness‑budget analysis (Section 4.4) limits allowable erosion of the combined margin $M$ to $16.7\%$; parameter‑identification error must therefore be kept below this fraction.  
5. *Packet loss.* Weakly‑hard loss constraints described in [7] are not yet integrated with the dissipation inequality; handling loss sequences remains an open question.  
6. *Physical implementation.* No material, tolerance, or regulatory constraints can be listed until a concrete Signal hardware or scaffold is proposed; these remain open questions.

**(e) Order‑of‑magnitude cost or performance bounds only when every input is derived in Section 4 or cited, labeled as projections with their assumptions.**  
- *Dissipation‑rate range.* From $\delta=\alpha-\alpha^{2}/2$ with $\alpha\in[0,1]$ we obtain $0\le\delta\le0.5$ (maximum at $\alpha=1$). This is a projection derived directly from the formula in Section 4.2.  
- *Quantization‑budget scaling.* The worst‑case cumulative degradation is $\Delta_{\text{quant}}=N\,U_{\max}\,q/2$. At the operating point $N=100$, $U_{\max}=1$, $q=0.1$, this yields $\Delta_{\text{quant}}=5.0$ energy units (Section 4.3). Doubling $q$ to $0.2$ would double the budget to $10.0$; halving $q$ to $0.05$ would halve it to $2.5$, assuming $N$ and $U_{\max}$ unchanged.  
- *Per