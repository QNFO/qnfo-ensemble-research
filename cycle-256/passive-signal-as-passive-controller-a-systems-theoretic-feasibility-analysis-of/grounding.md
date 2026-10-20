# Grounding block - source: rem-rev-7c5e023d-eb6e-43e9-8013-a08222bd9e3b

## Research idea

Re-entry from 10.5281/zenodo.18515457: engineered to function as a passive control system (‘Signal’)?

Post-publication revision of the published paper "Passive Signal as Passive Controller: A Systems-Theoretic Feasibility Analysis of the Signal‑Worker Ontology" (version 2.1.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Section 4.3 interpretation: 'the budget is therefore tolerable only for states small enough that δ Σ x_k² stays above 5.0.' (confirmed by a second model)

## Existing paper under revision (remediation only)

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
5. A practical pathway: identification of users, TRL assessment, the smallest next test, and the primary engineering constraints (Section 8).

## 2. Background and Related Work

**[1] Passive iFIR Filters for Data‑Driven Control.** The work designs passive controllers as the parallel action of an integrator and a finite‑impulse‑response filter, with transfer function \(C(z)=\frac{\gamma T_s}{1-z^{-1}}+\sum_{k=0}^{m-1}g_k z^{-k}\). It shows that for passive plants the closed‑loop stability is guaranteed by construction and that the design requires no plant model, directly supporting the notion that an integrator‑based Signal block can be rendered passive by construction.

**[2] Passivity‑based PI control of first‑order systems with I/O communication delays.** This paper treats a delayed communication channel as a transport PDE and proves that the overall loop remains passive when a scattering transformation is applied, despite the Nyquist plot of a pure delay lying outside the right‑half plane. The result motivates the delay‑margin analysis in Section 4.4, where a transport delay models the spatial separation between Signal and Worker.

**[3] Sampled‑data control design for systems with quantized actuators.** The authors design sampled‑data state feedback for continuous‑time linear systems with uniform input quantization; this design is used as a basis for the quantization analysis in Section 4.3. Their framework underpins the quantization analysis of Section 4.3, treating the quantized Signal output as a bounded perturbation of the ideal passive inequality.

**[4] Composite Adaptive Control Barrier Functions for Safety‑Critical Systems with Parametric Uncertainty.** This work shows that safety guarantees based on control barrier functions can fail under parametric uncertainty, and introduces adaptive mechanisms to retain safety. It illustrates the broader theme that model uncertainty can invalidate guarantees, which is reflected in the limitations discussion of Section 6.

**[5] Robust Nonlinear Optimal Control via System Level Synthesis.** The authors decompose an uncertain nonlinear system into a nominal trajectory and a norm‑bounded error, jointly optimizing both. Their nominal‑plus‑error decomposition informs the robustness‑budget calculation in Section 4.4, where the Signal’s passivity margin is eroded by a bounded deviation.

**[6] Safe Control Synthesis via Input Constrained Control Barrier Functions.** This paper introduces Input‑Constrained CBFs that construct inner safe sets when full input authority is unavailable. The attractor‑radius result of Section 4.4 mirrors the inner‑safe‑set construction, highlighting how quantized, bounded outputs can be interpreted as input constraints.

**[7] On \(\ell_2\)-performance of weakly‑hard real‑time control systems.** The authors develop LMI conditions for \(\ell_2\) performance under weakly‑hard packet‑loss constraints, showing how loss sequences can be modeled and analyzed. Their framework motivates the discussion of packet‑loss constraints as a future extension in Section 8(d).

**[8] On the relationship between control barrier functions and projected dynamical systems.** This work proves that CBF‑controlled systems are Krasovskii‑like perturbations of projected dynamical systems, providing a quantitative bound on the perturbation. It supports the treatment of quantization as a bounded additive perturbation in Section 4.3.

**[9] QNFO: Passive Signal as Passive Controller (prior feasibility analysis).** The predecessor formalized the Signal as a discrete‑time block, derived exact passivity for a pure integrator, strict passivity for a leaky integrator, and a worst‑case quantization degradation of \(5.0\) energy units. The present paper re‑derives those results with full arithmetic, extends them with an illustrative example, and adds the engineering pathway the predecessor lacked.



## 3. Methods

### 3.1 Definitions

**Discrete‑time passivity.** A discrete‑time system with state \(x_k\in\mathbb{R}^n\), input \(u_k\in\mathbb{R}\), and output \(y_k\in\mathbb{R}\) is *passive* if there exists a storage function \(V(x)\ge 0\) with \(V(0)=0\) such that for all \(k\),

\[
V(x_{k+1}) - V(x_k) \le u_k\,y_k .
\]

The right‑hand side \(u_k y_k\) is the *supply rate*.

**Strict passivity with dissipation rate.** If additionally

\[
V(x_{k+1}) - V(x_k) \le u_k\,y_k - \delta\,x_k^{2},
\qquad \delta > 0,
\]

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

**Interpretation.** The leaky integrator dissipates \(\delta \sum_{k} x_k^{2}\). If state magnitudes are of order unity, the total dissipation over 100 steps is \(\delta \times 100 \approx 9.5\) (for \(\delta=0.095\)), exceeding the quantization budget; thus the budget is tolerable only for states large enough that \(\delta\sum x_k^{2} > 5.0\). A concrete threshold follows from assuming a constant state magnitude \(x_\ast\):

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

* **R5 (quantization energy cost, illustrative).** \(E_q = 0.025\ \text{J}\) per packet, i.e. \(2.5\%\) of the nominal supply bound (Section 4.4).

* **R6 (attractor radius, illustrative).** \(r_q = 0.05\) in normalized Worker units (Section 4.4).

* **R7 (robustness budget, illustrative).** Margin erosion tolerance \(16.7\%\) of the combined loop margin (Section 4.4).

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


 No human‑conducted experiment, measurement, survey, peer review, or data deposition was performed. All quantitative claims are either derived analytively in the text or labeled as projections with explicit assumptions.

## Appendix A. Divergence Report

No divergent claims were identified among the independent drafts. All substantive statements in the manuscript are convergent across the source versions.

## Appendix B. Claim Attribution

| Claim ID | Statement (as in the paper) | Source Draft(s) |
|----------|-----------------------------|-----------------|
| C1 | The pure integrator is exactly passive under the output \(y_k = x_k + \tfrac{1}{2}u_k\). | Draft A, Draft B, Draft C |
| C2 | The leaky integrator is strictly passive under \(y_k = (1-\alpha)x_k + \tfrac{1}{2}u_k\) with dissipation rate \(\delta = \alpha - \tfrac{\alpha^{2}}{2}\). | Draft A, Draft B, Draft C |
| C3 | For \(\alpha = 0.1\) the dissipation margin is \(-0.095\,x_k^{2}\). | Draft A, Draft B, Draft C |
| C4 | The naive output \(y_k = x_k\) fails passivity, with counterexample margin \(+0.505\) at \(x_k = 1,\;u_k = -1\). | Draft A, Draft B, Draft C |
| C5 | Uniform output quantization with resolution \(q = 0.1\) yields a worst‑case cumulative passivity degradation \(\Delta_{\text{quant}} = 5.0\) energy units over \(N = 100\) steps. | Draft A, Draft B, Draft C |
| C6 | The delay phase lag at \(\omega_c = 1.0\ \text{rad/s}\) and transport delay \(T_d = 0.5\ \text{s}\) is \(\phi_d = 0.5\ \text{rad} \approx 28.65^{\circ}\). | Draft A, Draft B, Draft C |
| C7 | The safety ratio \(\rho = M_n / \ell_d \approx 4.71\). | Draft A, Draft B, Draft C |
| C8 | Quantization energy cost per packet is \(E_q = 0.025\ \text{J}\), i.e. \(2.5\%\) of the nominal supply bound \(E_0 = 1.0\ \text{J}\). | Draft A, Draft B, Draft C |
| C9 | Attractor radius due to quantization is \(r_q = 0.05\) (normalized Worker units). | Draft A, Draft B, Draft C |
| C10 | Robustness budget allows margin erosion up to \(16.7\%\) of the combined loop margin before Signal passivity fails. | Draft A, Draft B, Draft C |
| C11 | The dissipation rate \(\delta\) provides a control‑theoretic analogue of the corpus’s passive‑versus‑driven distinction. | Draft A, Draft B, Draft C |
| C12 | The work is at Technology Readiness Level 1–2 (analytical, unreviewed). | Draft A, Draft B, Draft C |
| C13 | The smallest next test is fitting a storage function to any concrete Signal dynamics; failure is the inability to satisfy the dissipation inequality for any output map of the form \(y_k = \beta x_k + \gamma u_k\). | Draft A, Draft B, Draft C |
| C14 | Primary constraints before implementation are (i) specification of Signal dynamics, (ii) quantization resolution, (iii) channel delay and loss, (iv) model uncertainty. | Draft A, Draft B, Draft C |
| C15 | Order‑of‑magnitude bounds: \(\delta \in [0,0.5]\) for \(\alpha \in [0,1]\); \(\Delta_{\text{quant}} = N U_{\max} q/2\). | Draft A, Draft B, Draft C |
| C16 | Risks include misinterpreting the analytical passivity results as empirical validation of the Signal‑Worker ontology. | Draft A, Draft B, Draft C |



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
- *Quantization‑budget scaling.* The worst‑case cumulative degradation is $\Delta_{\text{quant}}=N\,U_{\max}\,q/2$. At the operating point $N=100$, $U_{\max}=1$, $q=0.1$ this yields $\Delta_{\text{quant}}=5.0$ energy units (Section 4.3). Doubling $q$ to $0.2$ would double the budget to $10.0$; halving $q$ to $0.05$ would halve it to $2.5$, assuming $N$ and $U_{\max}$ unchanged.  
- *Per‑packet quantization energy cost.* With $\Delta=0.05$ and $u_{\max}=1$, the excess energy per packet is $E_q\le(\Delta/2)u_{\max}=0.025$ J, i.e. $2.5\%$ of the nominal supply bound $E_0=u_{\max}^{2}=1.0$ J (Section 4.4).  
- *Attractor radius.* Using the contraction constant $\lambda_W=0.5\ \text{s}^{-1}$, the guaranteed attractor radius is $r_q=(\Delta/2)/\lambda_W=0.05$ (Section 4.4).  

All these numbers are algebraic consequences of the formulas derived in Section 4 and the illustrative parameters explicitly listed there; they are therefore projections with the stated assumptions.

**(f) Direct risks or misuse paths, where one exists.**  
The principal risk is rhetorical misuse: citing the passivity results as empirical validation of the Signal‑Worker ontology would be misleading, because the analysis only shows internal consistency of a block‑diagram abstraction on postulated dynamics. A second misuse would be transferring the illustrative quantitative values (e.g., $\rho\approx4.71$, $2.5\%$ overhead) to real systems without re‑deriving them for the actual parameters; such transfer would overstate performance. Finally, 

## 9. Conclusion

We have completed the feasibility arc for the Signal‑Worker ontology's central engineering question. The Signal, modeled as a discrete‑time controller block, is exactly passive as a pure integrator under the output map $y_k = x_k + \frac{1}{2}u_k$ and strictly passive as a leaky integrator under $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \frac{\alpha^{2}}{2}$ — a result that fails under the naive state output, with counterexample margin $+0.505$. Output quantization degrades the passivity budget by at most $N\,U_{\max}\,q/2$, which is $5.0$ energy units at the stated operating point. A labeled illustrative example quantifies the delay margin ($\rho \approx 4.71$), quantization energy cost ($2.5\%$ per packet), attractor radius ($r_q = 0.05$), and robustness budget ($16.7\%$ margin erosion tolerance). The dissipation rate $\delta$ gives the corpus's passive‑versus‑driven distinction a tunable control‑theoretic analogue, though the mapping remains uncalibrated because the corpus supplies no dynamical equations or numerical complexity values. The hypothesis is well‑posed and internally consistent at the block‑diagram level; it is TRL 1–2 as pure analysis; and the smallest next test is the fitting of a storage function to whatever Signal dynamics a future specification provides, with failure defined as the nonexistence of any output map rendering the dissipation inequality satisfied.

## Version History

- Version 2.0.1 (2026-10-19, from 2.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals
- Version 2.0.2 (2026-10-19, from 2.0.1): wording: sentences that read as reporting completed experiments or measurements were restated as proposals
- Version 2.0.3 (2026-10-19, from 2.0.2): wording: sentences that read as reporting completed experiments or measurements were restated as proposals
- Version 2.1.0 (2026-10-19, from 2.0.3): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Appendix A. Divergence Report; Appendix B. Claim Attribution. references 10 -> 10. length 7200 -> 4650 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.27.5-revision-claimgate). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 13 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Passive iFIR Filters for Data-Driven Control. arXiv:2403.06640v2. https://arxiv.org/abs/2403.06640v2
[2] Passivity-based PI control of first-order systems with I/O communication delays: A complete sigma-stability analysis. arXiv:1507.01146v1. https://arxiv.org/abs/1507.01146v1
[3] Sampled-data control design for systems with quantized actuators. arXiv:2208.05694v3. https://arxiv.org/abs/2208.05694v3
[4] Composite Adaptive Control Barrier Functions for Safety-Critical Systems with Parametric Uncertainty. arXiv:2601.17683v3. https://arxiv.org/abs/2601.17683v3
[5] Robust Nonlinear Optimal Control via System Level Synthesis. arXiv:2301.04943v3. https://arxiv.org/abs/2301.04943v3
[6] Safe Control Synthesis via Input Constrained Control Barrier Functions. arXiv:2104.01704v1. https://arxiv.org/abs/2104.01704v1
[7] On $\ell_2$-performance of weakly-hard real-time control systems. arXiv:2305.07875v3. https://arxiv.org/abs/2305.07875v3
[8] On the relationship between control barrier functions and projected dynamical systems. arXiv:2309.04378v1. https://arxiv.org/abs/2309.04378v1
[9] https://papers.qnfo.org/papers/passive-signal-as-passive-controller-a-systems-theoretic-feasibility-analysis-of. QNFO: Passive Signal as Passive Controller: A Systems-Theoretic Feasibility Analysis of the Signal-Worker Ontology.
[10] https://papers.qnfo.org/papers/structural-vs-driven-quantum-coherence. QNFO: Structural vs Driven Quantum Coherence.


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2403.06640v2 | Passive iFIR Filters for Data-Driven Control
arXiv:1507.01146v1 | Passivity-based PI control of first-order systems with I/O communication delays: A complete sigma-stability analysis
arXiv:2208.05694v3 | Sampled-data control design for systems with quantized actuators
arXiv:2601.17683v3 | Composite Adaptive Control Barrier Functions for Safety-Critical Systems with Parametric Uncertainty
arXiv:2301.04943v3 | Robust Nonlinear Optimal Control via System Level Synthesis
arXiv:2104.01704v1 | Safe Control Synthesis via Input Constrained Control Barrier Functions
arXiv:2305.07875v3 | On $\ell_2$-performance of weakly-hard real-time control systems
arXiv:2309.04378v1 | On the relationship between control barrier functions and projected dynamical systems

## QNFO corpus context (Vectorize)

QNFO: Passive Signal as Passive Controller: A Systems-Theoretic Feasibility Analysis of the Signal‑Worker Ontology | https://papers.qnfo.org/papers/passive-signal-as-passive-controller-a-systems-theoretic-feasibility-analysis-of
QNFO: Structural vs Driven Quantum Coherence | https://papers.qnfo.org/papers/structural-vs-driven-quantum-coherence

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2403.06640v2 | Passive iFIR Filters for Data-Driven Control
  We consider the design of a new class of passive iFIR controllers given by the parallel action of an integrator and a finite impulse response filter. iFIRs are more expressive than PID controllers but retain their features and simplicity. The paper provides a model-free data-driven design for passive iFIR controllers based on virtual reference feedback tuning. Passivity is enforced through constra
  Full text (https://arxiv.org/html/2403.06640v2), excerpts of its own sections:
  § I Introduction: From simple prototyping to advanced control applications, a PID controller goes a long way due to its simple structure, intuitive tuning, and the presence of integral action for perfect regulation. In addition, with passive plants, PID control leads to inherently stable closed loops, even when the plant is uncertain and its model is approximated. This makes PID control one of the most common control techniques in industry [ 1 , 2 , 3 ] . In many control applications, a stabilizing feedback action must also satisfy complex performance requirements. These are often specified as desired input/output behaviors, in the form of a set of data or a desired transfer function. In this setting, the PID control shows limitations [ 4 , 5 ] . Ideally, we want a controller that retains the simplicity of PID control and its fundamental properties, namely integral action and passivity, but is more flexible. In this paper, we investigate the design of iFIR controllers, which combine the parallel action of a finite impulse response filter (FIR) and an integrator for perfect regulation. [...]
  § II Data-driven design of iFIR controllers: iFIR controllers $C$ combine integration and finite impulse response filtering. Given the finite coefficients $\{g_{k}\}_{k=0,...,m-1}$ , the controller is given by $C(z)\ =\ \underbrace{\frac{\gamma T_{s}}{1-z^{-1}}}_{\mbox{integrator}}+\underbrace{\ \sum_{k=0}^{m-1}g_{k}z^{-k}}_{\mbox{FIR filter}}$ (1) where the integrator is discretized using backward Euler discretization with sampling period $T_{s}$ . $\gamma$ is the integral gain. In fact, $C$ shows a generalized PID structure, where the proportional and derivative terms are replaced by a FIR filter. $C$ can be easily designed from data, following the approach of virtual reference feedback tuning [ 10 ] . In Figure  1 , we represent the desired closed-loop performance with a time-invariant (possibly nonlinear) reference model $M_{r}$ . $P$ is a time-invariant single-input single-output plant. The plant is not necessarily linear but we assume passivity from the input $u$ to the output $y$ (e.g. Euler-Lagrangian systems and port-Hamiltonian systems [ 1 , 19 ] ). [...]
  § III Passive iFIR controllers: Although VRFT is an established and effective design methodology, the data-driven optimal controller ( 2 ) does not guarantee closed-loop stability . For passive plants $P$ , we tackle this issue through passivity. We combine the least-square fitting ( 5 ) with specific constraints that enforce passivity. This leads to the derivation of the passive iFIR controller that best fits the desired input / output data ( 2 ). The first formulation is a straightforward application of the Kalman-Yakubovich-Popov (KYP) lemma. [...]
  § IV-A Fitting of passive FIR filters: We identify passive FIR filters to illustrate the effectiveness of ( 7 ), ( 10 ) and ( 14 ) in dealing with the targets $C_{q}(s)=\frac{1}{(0.5s+1)^{q}}\qquad q\in\{1,2,3\},$ (18) where $C_{1}$ is passive, and $C_{2}$ and $C_{3}$ show increase shortage of passivity. [...]
  § V Conclusions: We have discussed a new data-driven approach for passive iFIR controllers. Their design is based on convex optimization, combining virtual reference feedback tuning with passivity constraints. Our approach does not require any plant model or large datasets, and the plant can be nonlinear. For passive plants, the stability of the closed loop is guaranteed by construction. Future work will extend the design to MIMO systems and to nonlinear controllers.
[2] arXiv:1507.01146v1 | Passivity-based PI control of first-order systems with I/O communication delays: A complete sigma-stability analysis
  The PI control of first-order linear passive systems through a delayed communication channel is revisited in light of the relative stability concept called sigma-stability. Treating the delayed communication channel as a transport PDE, the passivity of the overall control-loop is guaranteed, resulting in a closed-loop system of neutral nature. Spectral methods are then applied to the system to obt
  Full text (https://arxiv.org/html/1507.01146v1), excerpts of its own sections:
  § 1 Introduction: Passivity-based control relies on the fact that the power-preserving interconnection of two passive subsystems yields again a passive system ( Ortega et al., 1998 ) . Lyapunov stability of the interconnected system follows from passivity while asymptotic stability is usually achieved by adding appropriate damping. Due to its simplicity and robustness, passivity-based control has attracted researchers and practitioners in the control community for several decades, e.g. ( Youla et al., 1959 ; Willems, 1972a ; Willems, 1972b ; Hill and Moylan, 1976 ; Byrnes et al., 1991 ; van der Schaft, 2000 ) . However, if a delayed communication channel stands between the plant and the controller, as in a typical control scenario, passivity arguments fail due to non-passive properties of the channel. Here, the loss of passivity follows from the fact that the Nyquist plot of a pure delay does not lie in the right-hand side of the complex plane. [...]
  § 2 Problem statement: Consider a first-order linear system of the form $\displaystyle\dot{x}$ $\displaystyle=-ax+bu_{1}\;,$ (1a) $\displaystyle y_{1}$ $\displaystyle=x\;,$ (1b) where $u_{1}$ , $y_{1}$ and $x$ $\in\mathbb{R}$ are the input, output and state, respectively. The parameters $a$ and $b$ are assumed to be non negative, which ensures passivity with storage function $V_{1}(x)=x^{2}/(2b)$ . Consider the PI controller $\displaystyle\dot{\xi}$ $\displaystyle=u_{0}\;,$ (2a) $\displaystyle y_{0}$ $\displaystyle=k_{p}u_{0}+k_{i}\xi\;,$ (2b) where $u_{0}$ , $y_{0}$ , $\xi$ $\in\mathbb{R}$ are the controller input, output and state, respectively. The proportional and integral gains $k_{p}$ and $k_{i}$ are assumed to be positive, so the controller is also passive. [...]
  § 2.1 Performance degradation as a result of delays: As a preliminary step for the characterization of the maximum decay rate, we begin with the decomposition of the $(k_{p},k_{i})$ -plane. Besides pure stability, we will be concerned with the exponential decay of system solutions with a given degree $\sigma$ , that is, with the $\sigma$ -stability of the system. This happens only if all the roots of the characteristic quasipolynomial have real parts less than $-\sigma$   ( Gu et al., 2003 ) . Then, we will determine the set of all $(k_{p},k_{i})$ points for which the closed-loop system is $\sigma$ -stable. Following the $\mathcal{D}$ -subdivision method, we equate ( 4 ) to zero and set $s=-\sigma$ , which gives the boundary $k_{i}=\sigma k_{p}+\frac{\sigma a_{\sigma}}{be^{h\sigma}}\;. [...]
  § 4 Concluding Remarks: A simple instance of the use of the scattering transformation in passivity-based control has been analyzed from the classical (i.e., frequency-domain) perspective of time-delay systems. The exponential decay rate of the closed-loop system was chosen as a criterion to asses the performance of different control schemes. This criterion leads to an optimal choice on the design parameter of the scattering transformation. Quite remarkably, the optimal choice is independent of the plant parameters and the delays in the communication channel. With the optimal choice, it is possible to attain exponential decay ratios that are almost twice as large as those obtained by setting the design parameter at the value suggested in the literature. A theoretical limit on the exponential decay rate has been found. The limit does depend on the total delay but, quite remarkably as well, it is independent of the plant parameters. [...]
[3] arXiv:2208.05694v3 | Sampled-data control design for systems with quantized actuators
  This paper deals with the problem of designing a sampled-data state feedback control law for continuous-time linear control systems subject to uniform input quantization. The sampled-data state feedback is designed to ensure the uniform global asymptotic stability (UGAS) of an attractor surrounding the origin. The closed-loop system is rewritten as a hybrid dynamical system. To do this, an auxilia
  Full text (https://arxiv.org/html/2208.05694v3), excerpts of its own sections:
  § 1 Introduction: The design of a new generation of control systems combining physical interactions with computational and communication abilities presents strong advantages in terms of scalability, maintenance, and computational resources, for example for transportation systems, autonomous robotics, and energy delivery systems ( Murray et al. (2002) ). This paper focuses on one of these digital elements, namely, quantization, which is typically used to reduce data traffic load in communication channels to comply with limited bandwidth constraints. As a side effect, quantization induces a nonlinear behavior into the closed loop. See, for example, Delchamps (1990) , Ceragioli et al. (2011) , Liberzon (2003b) , Tarbouriech and Gouaisbaut (2012) . Most of the works dealing with quantized control systems focus either on continuous-time systems ( Brockett and Liberzon (2000) , Liberzon (2003a) , Fridman and Dambrine (2009) , Ferrante et al. (2015) , Ferrante et al. (2020) ), or on discrete-time systems, ( Picasso and Colaneri (2008) , Fu and Xie (2009) , Campos et al. (2018) , Ichihara et al. (2018) ). [...]
  § Notation: The symbol $\mathbb{N}$ denotes the set of nonnegative integers, $\mathbb{N}_{>0}$ is the set of positive integers, $\mathbb{R}$ represents the set of real numbers, $\mathbb{R}^{n}$ is the $n$ -dimensional Euclidean space, $\mathbb{R}^{n}_{>0}$ is the positive (open) orthant in $\mathbb{R}^{n}$ , $\mathbb{R}^{n\times m}$ represents the set of $n\times m$ real matrices, $\mathbb{Z}$ is the set of relative integers, and $\mathbb{B}$ is the closed unitary ball in the Euclidean norm. Given $\delta>0$ , $\delta\mathbb{Z}\coloneqq\{\delta k\colon k\in\mathbb{Z}\}$ . The symbol $\mathbb{S}_{+}^{n}$ ( $\mathbb{S}_{++}^{n}$ ) stands for the set of $n\times n$ symmetric positive semidefinite (definite) matrices, $\mathbb{D}_{+}^{n}$ ( $\mathbb{D}_{++}^{n}$ ) denotes the set of $n\times n$ diagonal positive semidefinite (definite) matrices. For a vector $x\in\mathbb{R}^{n}$ (a matrix $A\in\mathbb{R}^{n\times m}$ ) $x^{\top}$ ( $A^{\top}$ ) denotes the transpose of $x$ ( $A$ ). The notation $\|A\|$ indicates the spectral norm of the matrix $A$ . [...]
  § 2.1 Problem setup: We consider the following continuous-time plant with quantized actuation: $\displaystyle\dot{x}_{p}=A_{p}x_{p}+B_{p}\q_{\Delta}(u_{p})$ (1) where $x_{p}\in\mathbb{R}^{n_{p}}$ and $u_{p}\in\mathbb{R}^{n_{u}}$ are, respectively, the plant state and control input. [...]
  § 6 Conclusion: The problem of designing a sampled-data state feedback control law for continuous-time linear control systems subject to uniform input quantization was addressed. The main goal was to design a sampled-data state feedback to ensure uniform global asymptotic stability (UGAS) of a compact set containing the origin of the plant substate. The closed loop was augmented with an auxiliary clock variable triggering the occurrence of sampling events and modeled as a hybrid dynamical system. Sufficient conditions for stability in the form of bilinear matrix inequalities were proposed. An iterative algorithm based on the use of the convex-concave decomposition approach was proposed to design an optimal controller with the objective of minimizing the size of the closed-loop attractor. Under some mild conditions on the open-loop system, the proposed design algorithm was shown to be deadlock free. The interest of the proposed methodology was illustrated through a numerical example. This work paves the ways for future research on quantized sampled-data control design. [...]
[4] arXiv:2601.17683v3 | Composite Adaptive Control Barrier Functions for Safety-Critical Systems with Parametric Uncertainty
  Control barrier functions guarantee safety but require accurate system models; parametric uncertainty invalidates these guarantees. Existing robust methods maintain safety via worst-case bounds at the cost of performance, while modular learning schemes decouple estimation from safety and risk constraint violations during transients. This paper presents the composite adaptive control barrier functi
  Full text (https://arxiv.org/html/2601.17683v3), excerpts of its own sections:
  § 1 Introduction: Control barrier functions (CBFs) provide a mathematical mechanism for enforcing safety in autonomous systems [ 1 , 2 ] . By acting as a pointwise filter, a CBF monitors a nominal control signal and modulates it only when the system approaches the boundary of a safe set. This operation renders the safe set forward invariant if the underlying mathematical model accurately represents the physical system. However, physical systems inevitably deviate from their models due to parametric uncertainties, such as variable payloads, unmodeled friction, or aerodynamic drag. This discrepancy challenges the formal safety guarantees of standard CBFs. When the model parameters are incorrect, the calculated safe control input may drive the system into the unsafe region. This uncertainty is typically addressed through two primary paradigms: robust control, bounding the uncertainty, or adaptive control, estimating the parameters. Robust formulations, such as those established by Jankovic [ 3 ] and Zhao et al. [...]
  § 2 Problem Formulation: Consider the nonlinear control-affine system subject to linear parametric uncertainty given by $\dot{x}(t)=f(x(t))+F(x(t))\theta_{*}+G(x(t))u(t),$ (1) where, for all $t\geq 0$ , $x(t)\in\mathcal{X}\subseteq{\mathbb{R}}^{n}$ is the state, and $u(t)\in\mathcal{U}\subseteq{\mathbb{R}}^{m}$ is the control input. The functions $f\colon\mathcal{X}\to{\mathbb{R}}^{n}$ , $F\colon\mathcal{X}\to{\mathbb{R}}^{n\times p}$ , and $G\colon\mathcal{X}\to{\mathbb{R}}^{n\times m}$ are known and continuously differentiable, while $\theta_{*}\in{\mathbb{R}}^{p}$ represents a vector of constant, unknown parameters. We impose the following assumption: (A1) There exists a known constant $\theta_{\max}>0$ such that $\|\theta_{*}\|\leq\theta_{\max}$ . Assumption (A1) implies the existence of a known compact convex set $\Theta\triangleq\{\theta\in{\mathbb{R}}^{p}\colon\|\theta\|\leq\theta_{\max}\}$ (2) such that $\theta_{*}\in\Theta$ . Remark 2.1 . [...]
  § 3 Composite Adaptive Control Barrier Functions: In this section, we develop the composite adaptive control barrier function (CaCBF) framework. Unlike robust approaches that rely on static, worst-case bounds, we design an adaptation law that dynamically reduces conservatism while guaranteeing safety. [...]
  § 7 Conclusion and Future Work: This paper introduced the composite adaptive control barrier function (CaCBF) framework for safety-critical control of nonlinear systems with linear parametric uncertainty. By deriving the adaptation law from a composite energy function that integrates a logarithmic safety barrier, a control Lyapunov function, and a quadratic parameter-error term, CaCBF couples estimation directly to safety. The resulting closed-loop system is formally shown to be: (i) safe, in the sense that the safe set $\mathcal{C}$ is forward invariant for all bounded parameters (Theorem  4.7 ); (ii) noise-robust, in the sense that the safety guarantee survives bounded state-derivative measurement errors (Theorem  4.24 ); and (iii) uniformly ultimately bounded (Theorem  4.12 ). When the regressor is persistently exciting, the parameter estimates additionally converge to the true value exponentially (Proposition  4.22 ). The framework is strictly less conservative than robust CBF in the sense that its admissible control set always contains the robust set as a proper subset (Theorem  5.1 ). [...]
[5] arXiv:2301.04943v3 | Robust Nonlinear Optimal Control via System Level Synthesis
  This paper addresses the problem of finite horizon constrained robust optimal control for nonlinear systems subject to norm-bounded disturbances. To this end, the underlying uncertain nonlinear system is decomposed based on a first-order Taylor series expansion into a nominal system and an error (deviation) described as an uncertain linear time-varying system. This decomposition allows us to lever
  Full text (https://arxiv.org/html/2301.04943v3), excerpts of its own sections:
  § I Introduction: Robust nonlinear optimal control represents one of the central problems, arising, e.g., in trajectory optimization or model predictive control, in many safety-critical applications, involving, e.g., robotic systems, drones, spacecraft, and many others. While this problem has been extensively studied in the literature [ 1 ] , and rigorous constraint satisfaction properties can be derived in the presence of disturbances (see robust predictive control formulations, e.g., [ 2 , 3 , 4 , 5 ] ), this is commonly achieved at the cost of introducing conservativeness. Figure 1 : Decomposition of the uncertain nonlinear dynamics into nominal nonlinear dynamics, linear time-varying dynamics (Section III-B ), and an error term composed of the disturbance and dynamic linearization error (Section III-A ), facilitating linear error feedback optimization with robust constraint satisfaction for the constrained nonlinear uncertain system (Section III-C ). [...]
  § Contribution: We propose a novel approach for optimal control of nonlinear systems with robust constraint satisfaction. As shown in Fig. 1 , the nonlinear system is expressed as a linear time-varying error system constructed around a jointly optimized nominal trajectory. This formulation includes a jointly optimized error term corresponding to the linearization error. The presented method has the following advantages compared to the literature: • The nominal nonlinear trajectory, the affine error feedback and the dynamic linearization error over-bounds are jointly optimized for robust constraint satisfaction, leading to reduced conservativeness. This formulation leverages and extends system level synthesis to the nonlinear constrained case. • The reachable set used for robust constraint satisfaction is tight for linear systems with affine feedback. [...]
  § Notation: We define the set $\mathbb{N}_{T}\vcentcolon=\{0,\dots,T-1\}$ where $T$ is a natural number. We denote stacked vectors or matrices by $\left(a,b\right)=[a^{\top}\penalty\ b^{\top}]^{\top}$ . For a vector $r\in\mathbb{R}^{n}$ , we denote its $i^{\text{th}}$ component by $r_{i}$ . Let $\mathbb{R}$ be the set of real numbers, $0_{p,q}\in\mathbb{R}^{p\times q}$ be a matrix of zeros, and $0_{m}\in\mathbb{R}^{m}$ be a vector of zeros. [...]
  § IV-C Results: Figure 3 : Comparison between the reachable set of the proposed robust nonlinear optimal control ( 27a ) (a), and the (reduced-horizon) open-loop robust nonlinear optimal control (b), shown with an exemplary trajectory subject to disturbances (red).
  § V Conclusion: We proposed a novel approach to solve finite horizon constrained robust optimal control problems for nonlinear systems subject to additive disturbances, as e.g. commonly encountered in trajectory optimization or MPC. One of the main novelties lies in the joint optimization of a nonlinear nominal trajectory, an affine error feedback and dynamic over-bounds of the linearization error, ensuring robust constraint satisfaction. We showcased the method for the control of a rigid body in rotation with constraints on the states and inputs, and demonstrated reduced conservatism of our method compared to (nonlinear) open-loop robust and existing linear approaches jointly optimizing the nominal trajectory and error feedback. Considering a receding horizon implementation, as is typical in robust MPC, including a corresponding recursive feasibility and stability analysis, is an important direction for future work. We recently extended the proposed method to handle parametric uncertainties [ 38 ] .
[6] arXiv:2104.01704v1 | Safe Control Synthesis via Input Constrained Control Barrier Functions
  This paper introduces the notion of an Input Constrained Control Barrier Function (ICCBF), as a method to synthesize safety-critical controllers for non-linear control affine systems with input constraints. The method identifies a subset of the safe set of states, and constructs a controller to render the subset forward invariant. The feedback controller is represented as the solution to a quadrat
  Full text (https://arxiv.org/html/2104.01704v1), excerpts of its own sections:
  § I Introduction: Many cyber-physical systems are safety critical, that is, they require guarantees that safety constraints are not violated during operation. Safety is often modeled by defining a safe subset of the state space for a given system, within which the state trajectories must always evolve. Recently, set-theoretic methods, such as Control Barrier Functions (CBFs) have become increasingly popular as a means of constructing and verifying such controllers  [ 1 , 2 , 3 , 4 ] . Quadratic Programs (QPs) enforcing CBF conditions have become popular for synthesizing low-level controllers to ensure that system trajectories remain within the safe set. These QPs can be solved in real-time at the current state, enabling safety-critical controllers for a wide range of non-linear systems to be computed efficiently during operation. Prior work on CBFs has largely focused on systems where a sufficiently large control authority is available to ensure forward invariance of the safe set. However in the presence of input constraints, only a subset of the safe set may be rendered forward invariant. [...]
  § II-A Notation: We denote the set of real numbers $\mathbb{R}$ and non-negative reals $\mathbb{R}_{+}$ . A continuous function $\alpha:[0,a)\rightarrow[0,\infty)$ is class- $\mathcal{K}$ if it is strictly increasing on the domain, and $\alpha(0)=0$ . It is class- $\mathcal{K}_{\infty}$ if $a=\infty$ and $\lim_{r\rightarrow\infty}\alpha(r)=\infty$ . A continuous function $\alpha:(-b,a)\rightarrow(-\infty,\infty)$ is an extended class- $\mathcal{K}$ function, if for some $a,b>0$ , if it is strictly increasing and $\alpha(0)=0$ . [...]
  § III-A Motivation: Fig. 1: Visual representation of ICCBF method. The safe set $\mathcal{S}$ and two intermediate sets $\mathcal{C}_{1}$ and $\mathcal{C}_{2}$ are drawn. The final inner safe set $\mathcal{C}^{*}$ is the intersection of each of these sets, and can be rendered forward invariant. Suppose the safe set $\mathcal{S}$ associated with $h$ cannot be rendered forward invariant by any controller $u\in\mathcal{U}$ . Then we define a function $b_{1}:\mathcal{X}\rightarrow\mathbb{R}$ and a set $\mathcal{C}_{1}$ (visualised in Figure  1 ) as follows $\displaystyle b_{1}(x)$ $\displaystyle=\inf_{u\in\mathcal{U}}[\dot{h}(x,u)+\alpha_{0}(h(x))]$ (7) $\displaystyle\mathcal{C}_{1}$ $\displaystyle=\{x\in\mathcal{X}:b_{1}(x)\geq 0\}$ (8) where $\alpha_{0}$ is some user specified extended class- $\mathcal{K}$ function and the shorthand $\dot{h}(x,u)=L_{f}h(x)+L_{g}h(x)u$ is used. Notice that since an infimum over $\mathcal{U}$ is taken, $b_{1}$ is only dependent on the state $x$ , and not the input $u$ . [...]
  § V Conclusion: In this paper, we have presented a framework that allows input constraints to be explicitly included in the construction of control barrier functions and to guarantee that safety is maintained with an input-constrained controller. The construction identifies an inner safe set and a feedback controller to render the subset safe. The method was demonstrated in two cases, an adaptive cruise control problem and a spacecraft rendezvous control problem. An optimization based method was used to verify the conditions of the ICCBF. Directions for future work include investigating numerically efficient methods to automate the search of ICCBFs, and to compare the complexity with other reachability methods, in particular for systems with high-dimensional states. Finally, the robustness of this controller to noise and model mismatch could also be investigated.
[7] arXiv:2305.07875v3 | On $\ell_2$-performance of weakly-hard real-time control systems
  This paper considers control systems with failures in the feedback channel, that occasionally lead to loss of the control input signal. A useful approach for modeling such failures is to consider window-based constraints on possible loss sequences, for example that at least r control attempts in every window of s are successful. A powerful framework to model such constraints are weakly-hard real-t
  Full text (https://arxiv.org/html/2305.07875v3), excerpts of its own sections:
  § I INTRODUCTION: In control systems with an unreliable feedback channel, failures can lead to the occasional loss of the control input signal. Such losses appear for example in Networked Control Systems (NCS), where the feedback loop is closed via a communication channel that is subject to packet loss [ 1 ] . [...]
  § III-B $\ell_{2}$ -performance analysis result: Given the previous graph definition, we can now state our first result. We use [ 17 , Theorem 2] as a basis and modify it to account for the constrained switching. Theorem 1 ( $\ell_{2}$ -performance analysis) The CSS ( 4 ), whose switching is captured by a graph $\mathcal{G}$ according to Definition  8 , has $\ell_{2}$ -performance with gain $\gamma$ if there exist symmetric matrices $S_{i}\in\mathbb{R}^{n\times n}$ and matrices $G_{i}\in\mathbb{R}^{n\times n}$ , $i=1,...,n_{\mathcal{V}}$ , such that $\displaystyle\begin{bmatrix}G_{i}+G_{i}^{\top}-S_{i}&\ast&\ast&\ast\\ 0&\gamma I&\ast&\ast\\ \mathcal{A}_{l}^{\mathrm{cl}}G_{i}&\mathcal{B}_{l}^{w}&S_{j}&\ast\\ \mathcal{C}_{l}^{\mathrm{cl}}G_{i}&\mathcal{D}_{l}^{w}&0&\gamma I\end{bmatrix}\succ 0\quad\forall(i,j,l)\in\mathcal{E}.$ (8) A Lyapunov function is then given by $\displaystyle V(x_{k})=x_{k}^{\top}\left(\sum_{i=1}^{n_{\mathcal{V}}}\eta_{i}(k)S_{i}^{-1}\right)x_{k}.$ (9) Proof: Since every node has at least one incoming and one outgoing edge, ( 8 ) guarantees $S_{i}^{-1}\succ 0~\forall i$ . [...]
  § IV-A Main idea and lifting: The fundamental concept is to “discretize” the system at time instants of successful control attempts, similarly as in [ 9 ] . This approach was called alternative discretization and constitutes a special case of the lifting presented in this section, which is adapted from [ 19 ] . To formalize, define $\tau\coloneqq(\tau_{\tilde{k}})_{\tilde{k}\in\mathbb{N}_{0}}$ as in [ 9 ] as the sequence of time indices of successful control attempt instants $k$ , and $\alpha\coloneqq(\alpha_{\tilde{k}})_{\tilde{k}\in\mathbb{N}_{0}}$ as the sequence counting the number of losses between two successful control attempts. The sequence $\alpha$ plays an important role in the lifting and its elements take values in the finite set $\{0,...,s-1\}$ , since we assumed $s$ to be bounded and hence there can only be a finite amount of consecutive losses. As an example, for $\mu=(1\,0\,1\,1\,0\,0\,1...)$ the corresponding sequences for the lifting are $\tau=(0\,2\,3\,6...)$ and $\alpha=(1\,0\,2...)$ . [...]
  § VII CONCLUSIONS: In this paper, we considered the $\ell_{2}$ -performance of linear plants with unreliable feedback, i.e., the control signal can be lost, which is modeled by a WHRT constraint. We presented sufficient LMI conditions under which such systems have $\ell_{2}$ -performance with a certain gain $\gamma$ . Moreover, we proposed an approach for the synthesis of state-feedback controller that ensures that the WHRT control system has $\ell_{2}$ -performance with gain $\gamma$ . This was made possible by lifting the system, which in addition typically reduces the computational complexity of the respective LMI conditions for the $\ell_{2}$ -performance analysis. The resulting controller can be a non-switched, loss sequence independent one for NCS without acknowledgment mechanisms, or designed as a switched controller, that switches depending on the past loss sequence. As a side result, we also obtained an $\ell_{2}$ -performance analysis result for general switched systems with constrained switching that can be captured by a graph. [...]
[8] arXiv:2309.04378v1 | On the relationship between control barrier functions and projected dynamical systems
  In this paper, we study the relationship between systems controlled via Control Barrier Function (CBF) approaches and a class of discontinuous dynamical systems, called Projected Dynamical Systems (PDSs). In particular, under appropriate assumptions, we show that the vector field of CBF-controlled systems is a Krasovskii-like perturbation of the set-valued map of a differential inclusion, that abs
  Full text (https://arxiv.org/html/2309.04378v1), excerpts of its own sections:
  § 1 Introduction: Control Barrier Functions (CBFs) have been introduced as a systematic methodology to impose safety on control systems [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ] . Typically, given a nominal controller 1 1 1 Alternatively, a Control Lyapunov Function (CLF, see [ 1 ] ) is given, and the controller is designed by employing both the CBF and the CLF. , which asymptotically stabilizes a given system, a modified version of it is designed, such that the system’s trajectories never leave a safe set. The safe controller is specified as the solution of a Quadratic Program (QP), with its constraint, termed the CBF constraint, preventing leaving the safe set. The cost matrix in the QP’s objective function is subject to design. [...]
  § 3.1 Main result: The main result of this work, Theorem 3.1 below, indicates that ( 2 ) and ( 5 ) are intimately related: $f_{\mathrm{cbf},a}$ belongs in a Krasovskii-like perturbation of the set-valued map $F$ . Theorem 3.1 . Let Assumptions 1 and 2 hold. For an arbitrarily small $\epsilon$ , such that $0 $a_{*}=\frac{\max_{z\in\mathcal{S}}|\mathcal{L}_{f}h(z)|}{\gamma^{-1}\Big(\frac{\min_{z\in\partial\mathcal{S}}\|\nabla h(z)\|-\epsilon}{L_{\nabla h}}\Big)}$ Moreover, denote $\displaystyle M_{1}:=\min_{z\in\partial\mathcal{S}}\|\nabla h(z)\|$ $\displaystyle M_{2}:=\max_{z\in\partial\mathcal{S}}\|\nabla h(z)\|$ $\displaystyle M_{3}:=M_{2}+L_{\nabla h}\gamma(\frac{1}{a_{*}}\max_{z\in\mathcal{S}}|\mathcal{L}_{f}h(z)|)$ $\displaystyle L_{1}:=\frac{\overline{\lambda}(P)}{\underline{\lambda}(P)\epsilon^{2}}L_{\nabla h}\biggl[1+\frac{M_{2}\overline{\lambda}(P)\Big(M_{2}+M_{3}\Big)}{\underline{\lambda}(P)M_{1}^{2}}\bigg]$ Finally, define $\displaystyle\sigma(a,x):=\max\bigg\{$ $\displaystyle\gamma(\frac{1}{a}|\mathcal{L}_{f}h(x)|),$ [...]
  § 5 Conclusion and Future Work: We have proven that CBF-controlled systems are Krasovskii-like perturbations of PDSs, and provided a quantitative bound on that perturbation. This provides novel perspectives on analyzing and designing CBF-based controllers for safe stabilization. In the simple scenario of convex safe sets and complete control over the dynamics $\dot{x}=f(x)+u$ , we have demonstrated how it can be used to design safe CBF-based controllers that preserve asymptotic stability of the origin and do not introduce undesired equilibria or limit cycles. Future work will focus on formalizing the design method of Section 4 , and extending it to more general dynamics and safe sets. Finally, the implications of Theorem 3.1 extend beyond the design of CBF-based controllers. Following steps similar to [ 11 ] , it can be shown that trajectories of the CBF-controlled system ( 2 ) uniformly converge to trajectories of the PDS ( 4 ). Thus, CBF-controlled systems may serve as continuous implementations/approximations of discontinuous PDSs. [...]
  § Appendix: Technical Lemmas and Proof of Theorem 3.1: In the following, we denote $U_{\mathrm{cbf},a}:=\{z\in\mathcal{S}\mid\mathcal{L}_{f}h(z)+ah(z)\leq 0\}$ . To prove Theorem 3.1 , we make use of the following Lemmas: Lemma 5.1 . Given $a>0$ , consider any $x\in U_{\mathrm{cbf},a}$ and any $y\in\mathrm{proj}_{\partial\mathcal{S}}(x)$ . It holds that $\|x-y\|\leq\gamma(\frac{1}{a}|\mathcal{L}_{f}h(x)|)$ Proof of Lemma 5.1 . It is proven by combining Assumption 1 item 4 with the fact that $0\leq h(x)\leq-\frac{1}{a}\mathcal{L}_{f}h(x)$ . ∎ Lemma 5.2 . For any $a\geq a_{*}$ , for all $x\in U_{\mathrm{cbf},a}$ , we have $0 Proof of Lemma 5.2 . It is proven by combining Assumption 1 item 2 , the triangle inequality and Lemma 5.1 . ∎ Lemma 5.3 . [...]
[9] QNFO: Passive Signal as Passive Controller: A Systems-Theoretic Feasibility Analysis of the Signal‑Worker Ontology | https://papers.qnfo.org/papers/passive-signal-as-passive-controller-a-systems-theoretic-feasibility-analysis-of
  The Signal‑Worker (S‑W) ontology interprets the boson as a *signal*—a delocalized field instruction—and the fermion as a *worker*—the localized state that performs work, proposing that passive, structure‑encoded control is thermodynamically superior to active, energy‑intensive control. This paper bridges the ontological claim to control‑theoretic certification by treating the Signal as a discrete‑
  Full text (https://papers.qnfo.org/papers/passive-signal-as-passive-controller-a-systems-theoretic-feasibility-analysis-of), excerpts of its own sections:
  § 1. Introduction: Engineers who must stabilize fragile quantum or mesoscopic states—such as superconducting devices, driven materials, or biological energy‑transfer structures—currently face a trade‑off between two control paradigms. Active control continuously injects energy, achieving stabilization at high thermodynamic cost and loss of stability when the drive is removed. [...]
  § 5. Results: All results are direct outputs of the derivations in Section 4. * **R1 (integrator passivity).** The pure integrator is exactly passive under \(y_k = x_k + \tfrac{1}{2}u_k\); supply equals storage change identically (Section 4.1). * **R2 (leaky integrator passivity).** For any \(\alpha\in(0,1]\) the leaky integrator is strictly passive under \(y_k = (1-\alpha)x_k + \tfrac{1}{2}u_k\) with dissipation rate \(\delta = \alpha - \tfrac{\alpha^{2}}{2}\). At \(\alpha=0.1\) the margin is \(-0.095\,x_k^{2}\) (Section 4.2). The naive output \(y_k = x_k\) fails, with counterexample margin \(+0.505\) (Section 4.2). * **R3 (quantization budget).** With \(q=0.1\), \(|u_k|\le1\), and \(N=100\), the worst‑case cumulative passivity degradation is \(\Delta_{\text{quant}} = 5.0\) energy units (Section 4.3). States larger than \(0.726\) in magnitude keep the net margin non‑positive. * **R4 (delay margin, illustrative).** Delay phase lag \(0.5\ \text{rad}\approx28.65^{\circ}\); safety ratio \(\rho \approx 4.71\) (Section 4.4). [...]
  § 6. Discussion: **What the framing buys.** By recasting the Signal as a passive controller, the ontological claim becomes a checkable dissipation inequality. This connects to design templates where passivity is enforced by construction ([1]), preserved across transport delays ([2]), and compatible with quantized sampled delivery ([3]). The derivations demonstrate that the framing yields concrete, arithmetic‑checkable quantities (R1–R7). **The corpus connection.** The dissipation rate \(\delta = \alpha - \tfrac{\alpha^{2}}{2}\) operationalizes the corpus’s passive‑versus‑driven distinction. In the corpus’s terms [10], an actively driven system requires continuous external energy (effectively \(\delta\approx0\)), whereas a leaky Signal with \(\alpha>0\) dissipates stored instruction even without supply, matching the passive structural control described in the ontology. The mapping is structural; the corpus supplies no numerical LCI values, so calibration remains open. **Limitations and failure modes.** 1. [...]
  § 9. Conclusion: We have completed the feasibility arc for the Signal‑Worker ontology's central engineering question. The Signal, modeled as a discrete‑time controller block, is exactly passive as a pure integrator under the output map $y_k = x_k + \frac{1}{2}u_k$ and strictly passive as a leaky integrator under $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \frac{\alpha^{2}}{2}$ — a result that fails under the naive state output, with counterexample margin $+0.505$. Output quantization degrades the passivity budget by at most $N\,U_{\max}\,q/2$, which is $5.0$ energy units at the stated operating point. A labeled illustrative example quantifies the delay margin ($\rho \approx 4.71$), quantization energy cost ($2.5\%$ per packet), attractor radius ($r_q = 0.05$), and robustness budget ($16.7\%$ margin erosion tolerance). The dissipation rate $\delta$ gives the corpus's passive‑versus‑driven distinction a tunable control‑theoretic analogue, though the mapping remains uncalibrated because the corpus supplies no dynamical equations or numerical complexity values. [...]
[10] QNFO: Structural vs Driven Quantum Coherence | https://papers.qnfo.org/papers/structural-vs-driven-quantum-coherence
  The pursuit of ambient superconductivity is hampered by a fundamental trade-off between active, energy-intensive control and passive, structural stability. Current literature lacks a unified framework that connects the thermodynamic costs of information, substrate complexity, and the disparate mechanisms of high-Tc superconductivity. This paper **proposes** a ‘Signal-Worker’ ontology to unify biol
  Full text (https://papers.qnfo.org/papers/structural-vs-driven-quantum-coherence), excerpts of its own sections:
  § 2.7 Summary of Theoretical: Framework In summary, the theoretical framework of this paper is a multi-pillar synthesis designed to create a predictive science of quantum architectonics. It begins with the foundational concept from thermodynamics that information is physical and that maintaining the order of a quantum state has an irreducible energy cost, as quantified by Landauer’s principle. This establishes thermodynamic efficiency as the ultimate metric for the success of any stabilization mechanism. To analyze the systems, we introduced two distinct complexity metrics. Krylov complexity serves as our tool for quantifying the dynamical complexity of the quantum state itself—the ‘Worker’—allowing us to distinguish stable, low-complexity dynamics from unstable, chaotic ones. The Lossless Complexity Index (LCI) serves as our tool for quantifying the structural complexity of the environment—the ‘Signal’ or scaffold—allowing us to distinguish between simple, chaotic, and usefully complex architectures. [...]
  § 4.7 Section Summary: In this section, we have applied the Signal-Worker ontology to analyze the current frontier of actively driven quantum systems. We have shown that light-induced superconductivity (Hu et al., 2014), high-pressure hydrides (Song et al., 2025), and dynamical instabilities (Huang et al., 2026) all share a common architectural motif: the reliance on an external, energy-intensive Signal to organize the Worker subsystem. This commonality supports our first hypothesis (H1) regarding the unifying power of the framework. Our analysis has revealed that this architectural choice leads to unavoidable consequences: thermodynamic inefficiency, transience, and dynamical instability. We have linked these failures to a lack of structural complexity (low LCI) in the substrate, providing initial support for our second hypothesis (H2). The systems lack the intrinsic information required to stabilize the quantum state against the environment. [...]
  § 5.7 Section Summary: In this section, we have explored the paradigm of passive structural control through the lens of the Signal-Worker ontology. We have shown that proximity effects (Ideta et al., 2025), Moiré engineering (Kim et al., 2025), and biological scaffolds (Quni-Gudzinas, 2026a) all rely on the same principle: an intrinsic, architectural Signal. This confirms the unifying power of our framework (H1). We have argued that this paradigm offers a fundamental solution to the thermodynamic inefficiency and instability of active control. By encoding information in structure, we achieve high stability with minimal energy cost. We have linked this performance to the hypothesized structural complexity of the scaffold, providing strong qualitative support for the Complexity-Efficiency Hypothesis (H2). The analysis of the FMO complex has provided a concrete target for design: the ‘phononic scaffold.’ It shows that room-temperature coherence is not forbidden by physics but requires a specific kind of structural environment—one that filters and shapes the thermal bath. [...]
  § 6.0 Synthesis and Discussion: This section synthesizes the parallel analyses of active and passive control systems to formally evaluate the three central hypotheses of this paper. By integrating the findings from Sections 4 and 5, we explore the unifying power of the Signal-Worker ontology, discuss the proposed Complexity-Efficiency relationship, and examine the framework’s generalizability. [...]