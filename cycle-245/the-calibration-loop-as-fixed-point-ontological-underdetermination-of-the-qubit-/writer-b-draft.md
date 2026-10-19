# The Calibration Loop as Fixed Point: Ontological Underdetermination of the Qubit by Its Own Metrology

## Abstract

Every engineered qubit is certified by a closed calibration chain: drive pulses are calibrated by readout, readout is calibrated against states prepared with those drives, and tomography validates the loop using measurements calibrated within it. The physical referent of the qubit label — a collective circuit mode, an electronic transition, a spin orientation — is never fixed by any single measurement inside the chain, and it is an open question whether the chain fixes it at all. This paper formalizes the calibration hierarchy as a self-consistent fixed-point problem, derives its contraction condition and iteration count in closed form, and exhibits two physically distinct ontologies of the same device — a strict two-level abstraction and a three-level anharmonic carrier with leakage amplitude $|c| = 0.1$ — that are observationally identical, with total-variation distance exactly zero, under any measurement chain confined to the computational subspace. Anchoring the analysis in the trapped-ion readout fidelity of $99.991(1)\%$ over $10^6$ trials carried in the prior version of this work [9], we compute the per-shot error scale $9\times10^{-5}$, the $k_{\min} = 11$ calibration iterations needed to reach that scale under an assumed loop gain product $g\,s = 0.5$, and the shot budgets $N \ge 2500$ (one sigma) and $N \ge 22500$ (three sigma) that would break the degeneracy once a leakage-resolving observable exists, with a signal-to-floor margin of about $111$. The circularity is broken only by measurements reaching outside the calibrated subspace or by cross-platform consistency requirements; within the loop, the qubit's ontology is a bookkeeping choice. We state the conditions under which each claim would fail and the smallest experiment that would test them.

## 1. Introduction

When an experimentalist drives a qubit, something physical is excited; when the same experimentalist reads out the qubit, something physical is measured. The engineering question is blunt: if the billiard-ball picture is rejected, the pulses manipulate the quantum state of some degree of freedom and the readout measures a macroscopic observable correlated with it, and the identity of that degree of freedom — collective circuit mode, electronic levels, spin orientation — is supplied by the calibration chain itself. The drive frequency is calibrated by finding a resonance; the Rabi rate is calibrated by fitting oscillations in a signal; the readout discriminator is calibrated by assigning outcomes to states prepared with the already-calibrated drive; tomography validates the loop using measurements whose calibration rests on the loop. Each step certifies the others. The loop is closed, and the physical ontology of the qubit appears only as an internal bookkeeping choice within it.

This question now carries economic weight. The QNFO analysis of engineered quantum systems reports that by 2026 the global quantum computing industry has absorbed an estimated $35 billion in combined public and private investment with no commercially viable quantum computer in existence, and locates part of the difficulty in a qubit ontology — a constrained two-level subspace of a physical degree of freedom — that is operationally defined but never independently certified [8]. If the certification pipeline cannot distinguish a two-level abstraction from a three-level carrier, then the decision of which physics to put into device models, error models, and scaling projections rests on an assumption no current measurement chain tests. A demonstration that the two ontologies are observationally identical under the standard chain would redirect effort toward leakage-resolving and cross-platform measurements; a refutation would show that the loop carries more ontological information than this paper claims, which would itself be a useful, quantifiable result.

This paper takes the closure of the calibration chain seriously as a formal problem and makes four contributions. First, it models the calibration hierarchy as an iterated map and derives the contraction condition and convergence rate in closed form, computing the iteration count needed to reach a stated readout noise floor (Sections 3.1, 4.3). Second, it exhibits two physically distinct ontologies of the same device — a strict two-level abstraction and a three-level anharmonic ladder — and proves that, under any measurement chain that does not resolve the third level, their outcome distributions are identical with total-variation distance exactly zero (Sections 3.2, 4.4). Third, it anchors the analysis quantitatively in the readout fidelity carried in the prior version of this work [9], deriving the error scale, the calibration iteration count, and the shot budget that would resolve the two ontologies once a leakage-resolving measurement is available (Section 4). Fourth, it identifies the structural features — leakage-resolving spectroscopy, continuous high-dynamic-range readout of the kind argued for in [10], and cross-platform consistency — that break the circularity, and states explicitly what would falsify the thesis (Sections 3.3, 3.4, 6).

The epistemic status of the claims is deliberately modest: everything quantitative is derived here from stated inputs with shown arithmetic, or is a clearly labeled projection. No experiment is performed or reported in this paper. The claim is not that any real experiment is ontologically confused; the claim is that the standard certification pipeline, taken on its own terms, cannot distinguish certain ontologies, and the paper quantifies exactly how indistinguishable they are.

## 2. Background and Related Work

The literature bearing on this question falls into four groups: works that treat self-referential reasoning as a formal method, works on control of systems whose working models are truncations of richer dynamics, works on safe and hierarchical control architecture, and the QNFO corpus on qubit ontology and readout.

**Self-referential diagnosis.** The closest structural analogue is adaptive fault diagnosis [1], which studies determining which processors in a remote location are reliable by asking "Yes or No" questions, where the processors are of three types: those that always tell the truth, those that always lie, and those that sometimes do either. Its central move, stated in its abstract, is that using self-referential reasoning, along with earlier techniques, one can regard both the truth-tellers and the liars as reliable. This is the logical move the calibration loop performs: a readout channel whose reliability is in question is calibrated by sources whose calibration depends on the readout, and the fixed point legitimizes the whole chain at once. The disanalogy is instructive: in [1] the identity of the reporters is given and only their reliability is at issue, whereas the open question here is whether self-referential consistency fixes the referent of the reports at all.

**Control of truncated and approximate models.** A second group treats control of systems whose working model is a truncation of a richer reality — the same epistemic situation as the two-level abstraction of a multi-level device. Reference [2] models a nonhomogeneous flexible wing under unsteady aerodynamic loads as a distributed parameter system of two coupled partial equations, actuated at the tip by flaps, and investigates the well-posedness of the underlying Cauchy problem via semigroup methods before constructing the boundary control law; its conclusion reports that under physical structural constraints both flexible displacements are bounded and converge exponentially to zero for vanishing disturbances. The methodological pattern — establish that the truncated closed-loop model is well-posed before designing the controller — is the discipline this paper applies to the calibration loop: prove the fixed point exists before asking what it refers to. Reference [5] treats exponential input-to-state stabilization of diagonal infinite-dimensional systems with uncertain, time-varying input delays using a constant-delay predictor feedback controller designed on a truncated finite-dimensional model; its Theorem 2 requires the closed-loop matrix $A_{\mathrm{cl}} = A_{N_0} + e^{-D_0 A_{N_0}} B_{N_0} K$ to be Hurwitz, and its conclusion derives an ISS estimate with fading memory of the disturbance. The truncation there is explicitly a modeling choice whose stability consequences must be bounded, exactly as leakage out of the two-level abstraction must be bounded in the model of Section 3.2. Reference [6] proposes a control-oriented notion of finite state approximation, approximating discrete-time plants with finite-valued sensors and actuators by deterministic finite memory systems for certified-by-design controller synthesis; its introduction frames the goal as providing both a lower-complexity model and a rigorous assessment of approximation quality, so that the performance of a controller designed on the approximation can be quantified on the original system. That framing is the control-theoretic statement of this paper's claim that the qubit ontology is defined by the control loop rather than discovered by it: the approximation is built for the controller, and certification for control is weaker than certification of ontology.

**Hierarchical and safe control architecture.** Reference [3] describes the control of a rigid-wing airborne wind energy system across all operational phases — take-off, transition to power generation, pumping cycles, transition to hovering, and landing — via a hierarchical control structure with design at all levels, validated in a simulation suite whose stated next step is testing on a real prototype. This is the architectural template for a calibration hierarchy: distinct phases (drive calibration, readout calibration, tomography), each with its own control law, coupled sequentially. Reference [4] introduces Input Constrained Control Barrier Functions for synthesizing safety-critical controllers for nonlinear control-affine systems with input constraints; the method identifies a subset of the safe set and constructs, via a quadratic program, a controller rendering that subset forward invariant, and it was demonstrated on adaptive cruise control and spacecraft rendezvous problems. This paper borrows the forward-invariance idea as a question it poses but does not answer: whether a forward-invariant "ontological safe set" exists — a region of parameter space in which the two-level abstraction is certified valid — and what barrier function on the leakage amplitude would enforce it.

**Quantum-compliant formulations.** Reference [7] formulates network epidemic control — isolating locations by banning movement, modeled as link removal — on discrete-time susceptible-infected-susceptible and susceptible-infected-removed network models, proves the control problem can be cast as a Quadratic Unconstrained Binary Optimization problem solvable by quantum annealing, and benchmarks four solvers, including a quantum annealer, on an Italian case study with networks of $n = 21$ regions or $n = 107$ provinces calibrated on COVID-19 spreading. Its relevance is methodological: it shows the quantum formalism applied as a modeling and optimization layer to a non-quantum control loop, supporting the view that the quantum-classical distinction is not what generates the self-referential structure — the closure of the calibration chain is.

**The QNFO corpus.** The corpus document "No Thing There" [8] is the pedagogical bridge between the ontology critique and working physics. Its summary states four points this paper uses directly: a qubit is a constrained two-level subspace of a physical degree of freedom — a collective circuit mode (transmon), electronic states (trapped ion), or spin orientation (quantum dot); control pulses manipulate the quantum state of that degree of freedom, coupling in a transmon to the electric dipole of the plasmon mode; readout measures a macroscopic observable that correlates with the qubit state; and self-referential metrology is genuinely circular but has an anchor, namely multi-level spectroscopy of the bare Hamiltonian, which provides an independent reference for the computational subspace. Its discussion of layering also poses the fragility question this paper formalizes: whether the gauge freedoms at the error-model and gate-set-tomography levels compound with the residual circularity of readout calibration, or whether each abstraction level is a protected subspace of the level below. The prior version of this paper [9] established the fixed-point model, the two-ontology construction, and the quantitative anchors (readout error scale, iteration count, shot budgets) that Section 4 recomputes and extends here. Finally, the analysis of Josephson-junction readout in [10] reports a simulation comparison in which a discrete latching readout mechanism introduces a six-fold increase in error relative to continuous monitoring (mean squared error $0.254$ versus $0.042$), with a filtered continuous chain reaching $0.015$, and argues that a superconducting qubit is a continuous analog oscillator restricted to a specific energy manifold rather than a native two-state switch. That result matters here because readout architecture determines what the chain can see: a latching, binary-threshold chain is structurally subspace-confined, while a continuous, high-dynamic-range chain is the natural hardware route to the leakage-resolving observable whose absence produces the degeneracy of Section 3.2.

## 3. Methods

### 3.1 The calibration loop as an iterated map

Let $\mathcal{H}_{\mathrm{sub}}$ denote the computational subspace (dimension $d = 2$) and $\mathcal{H}_{\mathrm{full}}$ the full Hilbert space of the physical carrier. The calibration chain consists of stages indexed $j = 1, \dots, J$: drive calibration, Rabi calibration, readout discriminator calibration, and tomographic validation. Each stage $j$ has a parameter vector $\theta_j \in \mathbb{R}^{n_j}$ and a validation statistic $r_j$ computed from data produced using the current settings of all other stages. Collecting $\Theta = (\theta_1, \dots, \theta_J)$, the update is

$$\Theta_{k+1} = F(\Theta_k), \qquad F: \mathbb{R}^n \to \mathbb{R}^n.$$

A calibrated apparatus is a fixed point $\Theta_\star$ with $F(\Theta_\star) = \Theta_\star$. The self-referential character is that $F$'s definition at every stage involves measurements taken through the apparatus being calibrated — the situation of [1], where the reliability of the witnesses is established by the testimony chain itself.

Near a fixed point, write $\Theta_k = \Theta_\star + \delta_k$. For a scalar gain model of one stage (the case relevant to drive-amplitude calibration), the update is

$$x_{k+1} = x_k + g\,(r_k - r_\star),$$

where $x_k$ is the drive parameter, $g$ the loop gain, $r_k$ the observed statistic, and $r_\star$ the target. Linearizing, $r_k - r_\star = s\,(x_k - x_\star)$ with sensitivity $s$, gives the error recursion

$$e_{k+1} = (1 - g\,s)\,e_k, \qquad e_k \equiv x_k - x_\star.$$

The map is a contraction whenever $|1 - g\,s| < 1$, and then $e_k = e_0\,|1 - g\,s|^k$. This is the formal content of "the loop converges": the fixed point is attractive and the chain self-consistent — but nothing in the contraction argument refers to the physical substrate. The fixed point is a property of the loop, not of $\mathcal{H}_{\mathrm{full}}$. A degenerate special case arises if the loop is instead written as a pure gain product $A \mapsto k_1 k_2 k_3 k_4\, A$: then a nontrivial fixed point requires $k_1 k_2 k_3 k_4 = 1$, and if that holds, every amplitude is a fixed point — a continuum of self-consistent calibrations. The contraction model is adopted as primary and the gain-product condition is treated as the marginal, non-contractive limit.

### 3.2 Two ontologies, one loop

The underdetermination conjecture is formalized with two models:

- **Model A (two-level abstraction):** $\mathcal{H}_A = \mathrm{span}\{|0\rangle, |1\rangle\}$, with calibrated POVM $\{\Pi_0^{(A)}, \Pi_1^{(A)}\}$ acting on $\mathcal{H}_A$.
- **Model B (anharmonic three-level carrier):** $\mathcal{H}_B = \mathrm{span}\{|0\rangle, |1\rangle, |2\rangle\}$, with the same calibrated POVM extended so that $\Pi_1^{(B)}$ projects onto the span of $\{|1\rangle, |2\rangle\}$ — the readout does not resolve the third level, the generic situation when the readout transition addresses only the $|0\rangle \leftrightarrow |1\rangle$ distinction.

A control pulse with residual leakage amplitude $c$ produces, in Model B, the state

$$|\psi_B\rangle = \sqrt{1 - |c|^2}\,|1\rangle + c\,|2\rangle,$$

while Model A assigns the pure state $|1\rangle$. The outcome distributions are

$$p_A(1) = 1, \qquad p_B(1) = \langle \psi_B | \Pi_1^{(B)} | \psi_B \rangle = (1 - |c|^2) + |c|^2 = 1.$$

The total-variation distance is

$$D_{\mathrm{TV}}(p_A, p_B) = \frac{1}{2}\sum_m |p_A(m) - p_B(m)| = 0.$$

Both ontologies are observationally identical under the full calibrated measurement set whenever the chain does not resolve level $|2\rangle$. The tomographic reconstruction — a function only of outcome distributions — is the same object in both cases. This is the precise sense in which the qubit ontology is underdetermined by its metrology: the loop fixes the operational qubit, and the operational qubit is compatible with multiple substrates.

**Connection to weak-drive perturbation theory.** The leakage amplitude is not a free parameter. In a weakly anharmonic ladder driven near the $|0\rangle \leftrightarrow |1\rangle$ transition with Rabi amplitude $\Omega$ and anharmonicity-scale detuning $\Delta$ on the $|1\rangle \leftrightarrow |2\rangle$ transition, adiabatic elimination of $|2\rangle$ (setting $\dot{c}_2 \approx 0$ in $\dot{c}_2 = -i\Delta c_2 - i\frac{\Omega}{2} c_1$) gives $c_2 \approx \frac{\Omega}{2\Delta} c_1$, so

$$|c|^2 \lesssim \left(\frac{\Omega}{2\Delta}\right)^2.$$

This relates the abstract leakage amplitude to an operating point in Section 4.6.

### 3.3 Breaking the degeneracy

If the measurement chain is extended so that it resolves $|2\rangle$ — a leakage-resolving measurement, with $\Pi_1$ projecting on $|1\rangle$ alone and a third outcome for $|2\rangle$ — the distributions become

$$p_A(1) = 1, \qquad p_B(1) = 1 - |c|^2, \qquad p_B(2) = |c|^2,$$

and

$$D_{\mathrm{TV}}(p_A, p_B) = \frac{1}{2}\left(|c|^2 + |c|^2\right) = |c|^2.$$

The degeneracy is broken exactly to the extent that the measurement reaches outside the computational subspace. With $N$ independent shots, resolving a distribution difference of order $D_{\mathrm{TV}}$ requires roughly $N \sim D_{\mathrm{TV}}^{-2}$ shots; this binomial scaling is stated as a modeling assumption for the projections below. Two hardware routes to such an extension are visible in the literature: multi-level spectroscopy of the bare Hamiltonian, identified in [8] as the independent anchor that references the computational subspace from outside the loop, and continuous high-dynamic-range readout chains of the TWPA-plus-filtering type analyzed in [10], whose continuous signal representation preserves information that a binary latching comparator discards.

### 3.4 Cross-platform constraint

A second route out of circularity is structural rather than statistical. Two platforms whose calibration loops close differently — photonic readout, circuit readout, spin resonance — cannot both be saved by a single shared ontology unless that ontology is substrate-specific. Requiring one consistent assignment of what is excited across platforms with different loop topologies is a constraint no single loop can generate; it is the analogue, in this setting, of the multi-witness consistency that lets the self-referential diagnosis of [1] classify its processors.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

**Input 1 (from [9], the prior version of this work):** average readout fidelity $f_{\mathrm{ro}} = 99.991\% = 0.99991$ for the optical qubit in $^{40}\mathrm{Ca}^+$, over $N_{\mathrm{trials}} = 10^6$ trials.

**Input 2 (from [9]):** the adaptive measurement technique allows fidelity $f_{\mathrm{ad}} = 99.99\% = 0.99999$.

**Input 3 (model assumption, Section 3.2):** leakage amplitude $|c| = 0.1$, i.e., leakage probability $|c|^2 = 0.01$.

**Input 4 (model assumption, Section 3.1):** loop gain–sensitivity product $g\,s = 0.5$, giving contraction factor $|1 - g\,s| = 0.5$; initial calibration error $e_0 = 0.1$ in units of the drive parameter.

**Input 5 (model assumption, Section 3.2):** weak-drive operating point $\Omega/\Delta = 0.1$; tomographic shot budget $N_{\mathrm{tom}} = 10^4$ shots per element.

### 4.1 Readout error scale

The per-shot readout error probability is

$$\varepsilon_{\mathrm{ro}} = 1 - f_{\mathrm{ro}} = 1 - 0.99991 = 9 \times 10^{-5}.$$

Over $N_{\mathrm{trials}} = 10^6$ trials, the expected number of misidentifications is

$$\mu = N_{\mathrm{trials}} \times \varepsilon_{\mathrm{ro}} = 10^6 \times 9 \times 10^{-5} = 90.$$

The one-standard-error uncertainty on $f_{\mathrm{ro}}$ over $10^6$ trials is

$$\sigma_f = \sqrt{\frac{f_{\mathrm{ro}}(1 - f_{\mathrm{ro}})}{N_{\mathrm{trials}}}} = \sqrt{\frac{0.99991 \times 9\times10^{-5}}{10^6}} = \sqrt{8.99919\times10^{-11}} \approx 9.4864\times10^{-6},$$

that is, about $10^{-6}$ in fidelity units, consistent with the "(1)" in the last quoted digit of $99.991(1)\%$.

### 4.2 Adaptive-technique improvement

The adaptive-technique error is

$$\varepsilon_{\mathrm{ad}} = 1 - f_{\mathrm{ad}} = 1 - 0.99999 = 1 \times 10^{-5},$$

and the ratio of adaptive to time-resolved error is

$$\frac{\varepsilon_{\mathrm{ad}}}{\varepsilon_{\mathrm{ro}}} = \frac{1\times10^{-5}}{9\times10^{-5}} = \frac{1}{9} \approx 0.11111.$$

The adaptive technique reduces the error to one-ninth of the time-resolved value, per the two fidelities carried in [9].

### 4.3 Calibration-loop convergence

With contraction factor $|1 - g\,s| = 0.5$ and $e_0 = 0.1$, the error after $k$ iterations is $e_k = 0.1 \times 0.5^k$. Taking as threshold the readout error scale $\varepsilon_{\mathrm{ro}} = 9\times10^{-5}$ — calibration error should not exceed the noise floor it is calibrated against — the requirement is

$$0.1 \times 0.5^k \le 9\times10^{-5} \quad\Longrightarrow\quad 0.5^k \le 9\times10^{-4}.$$

Taking logarithms:

$$k \ge \frac{\ln(9\times10^{-4})}{\ln(0.5)} = \frac{-7.01312}{-0.69315} = 10.118.$$

Since $k$ is an integer, the check is discrete: $0.5^{10} = 9.7656\times10^{-4} > 9\times10^{-4}$, while $0.5^{11} = 4.8828\times10^{-4} \le 9\times10^{-4}$. Hence

$$k_{\min} = 11 \text{ iterations},$$

with $e_{11} = 0.1 \times 4.8828\times10^{-4} = 4.8828\times10^{-5} < 9\times10^{-5} < e_{10} = 9.7656\times10^{-5}$.

### 4.4 Ontological distinguishability

From Section 3.3, with $|c|^2 = 0.01$ (Input 3):

$$D_{\mathrm{TV}}(p_A, p_B) = |c|^2 = 0.01 \quad \text{(leakage-resolving measurement)},$$
$$D_{\mathrm{TV}}(p_A, p_B) = 0 \quad \text{(subspace-restricted measurement)}.$$

### 4.5 Shot budget and noise-floor margin

To resolve a distribution difference $\Delta p = |c|^2 = 0.01$ at one-standard-error significance, the binomial standard error $\sqrt{p(1-p)/N}$ must satisfy $\sqrt{p(1-p)/N} \le \Delta p$. Taking the conservative $p \approx 1/2$ bound, $\sqrt{1/(4N)} \le 0.01$ gives

$$N \ge \frac{1}{4 \times (0.01)^2} = \frac{1}{4\times10^{-4}} = 2500 \text{ shots}.$$

For a three-sigma requirement, $3\sqrt{1/(4N)} \le 0.01$ gives

$$N \ge \frac{9}{4\times10^{-4}} = 22500 \text{ shots}.$$

Both figures are far below the $10^6$ trials already carried in [9], so the shot budget is not the obstacle; the obstacle is whether the measurement chain implements a leakage-resolving observable at all. The margin of a leakage signal over the readout noise floor is

$$\frac{|c|^2}{\varepsilon_{\mathrm{ro}}} = \frac{0.01}{9\times10^{-5}} = 111.1\overline{1} \approx 111,$$

so a leakage-resolving extension of a readout chain with the [9] error scale would see the three-level ontology clearly, provided the extension exists.

### 4.6 Weak-drive consistency check

At the operating point $\Omega/\Delta = 0.1$ (Input 5), the adiabatic bound of Section 3.2 gives

$$\left(\frac{\Omega}{2\Delta}\right)^2 = \left(\frac{0.1}{2}\right)^2 = (0.05)^2 = 2.5\times10^{-3},$$

that is, $|c|^2 \lesssim 2.5\times10^{-3}$, a factor of four below the Input-3 value of $0.01$, so the shot budgets of Section 4.5 are conservative for weak drives. Conversely, with $N_{\mathrm{tom}} = 10^4$ shots per tomographic element, the worst-case binomial resolution at $\hat{p} = 1/2$ is

$$\sigma = \sqrt{\frac{0.5 \times 0.5}{10^4}} = \sqrt{2.5\times10^{-5}} = 5.0\times10^{-3},$$

which exceeds $2.5\times10^{-3}$ by a factor of $2$: at this operating point and budget, population tomography cannot resolve the leakage. Resolving $2.5\times10^{-3}$ at one sigma would require

$$N \ge \frac{0.25}{(2.5\times10^{-3})^2} = \frac{0.25}{6.25\times10^{-6}} = 4.0\times10^4 \text{ shots per element},$$

a $4\times$ increase over the assumed budget. At a stronger drive, $\Omega/\Delta = 0.4$, the bound becomes $(0.2)^2 = 4.0\times10^{-2}$, an order of magnitude above the $5.0\times10^{-3}$ floor, so strong-drive tomography would distinguish the ontologies. These are projections under the stated assumptions ($\Omega/\Delta$ values, worst-case $\hat{p} = 1/2$, no systematic errors).

### 4.7 What continuous readout changes

The simulation comparison in [10] reports mean squared errors of $1.089$ for a latching readout at noise standard deviation $\sigma = 2.0$, $0.042$ for raw continuous TWPA output at $\sigma = 0.2$, $0.015$ for TWPA output with Kalman filtering, and $0.254$ for a high-SNR latching control at $\sigma = 0.2$; the latching mechanism itself therefore costs a factor $0.254/0.042 \approx 6.05$ in error relative to continuous monitoring at matched noise. Read in the present framework, a chain whose front end is a one-bit comparator is structurally subspace-confined regardless of shot budget, because the comparator output is a function of the qubit-state-dependent observable alone; a continuous chain with dynamic range across the $|2\rangle$-shifted signal level is the hardware precondition for the