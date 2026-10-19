# The Calibration Loop as Fixed Point: Ontological Underdetermination of the Qubit by Its Own Metrology

## Abstract

Engineered qubits are certified through a closed calibration chain in which drive pulses, readout discriminators, and tomographic validation mutually calibrate one another. This self‑referential loop raises the question of whether the physical referent of the qubit label (collective circuit mode, electronic transition, or spin) is determined by the loop itself or remains underdetermined. We formalize the calibration hierarchy as an iterated map, derive its contraction condition, and compute the number of iterations required to reach the readout noise floor. Using a two‑level abstraction and a three‑level anharmonic ladder with leakage amplitude $|c|$, we prove that, under any measurement chain confined to the computational subspace, the two ontologies produce identical outcome distributions (total‑variation distance $0$). By assuming a typical trapped‑ion readout fidelity of $99.991\%$ and a leakage probability of $|c|^{2}=0.01$, we obtain a per‑shot error of $9\times10^{-5}$, a minimum of $11$ calibration iterations, and a shot budget of $N\ge2500$ (one‑sigma) required to resolve the ontologies once a leakage‑resolving observable is available. The circularity is broken only by measurements that extend beyond the calibrated subspace or by cross‑platform consistency constraints. We enumerate the conditions under which each claim would fail.

## 1. Introduction

When an experimentalist “drives a qubit,” a physical excitation is created; when the same experimentalist “reads out the qubit,” a physical observable is measured. The engineering question is blunt: if the billiard‑ball picture is rejected, what exactly do the pulses manipulate, and what does the readout measure—excitations of what medium? The uncomfortable answer is that the answer is supplied by the calibration chain itself. The drive frequency is calibrated by finding a resonance; the Rabi rate is calibrated by fitting oscillations in a signal; the readout discriminator is calibrated by assigning outcomes to states prepared by the already‑calibrated drive; tomography validates the loop using measurements whose calibration rests on the loop. Each step certifies the others. The loop is closed, and the physical ontology of the qubit—collective mode, spin, circuit degree of freedom, or a two‑level abstraction layered over a multi‑level device—appears only as an internal bookkeeping choice within the loop.

This paper takes that closure seriously as a formal problem. We make four contributions. First, we model the calibration hierarchy as an iterated map and derive its contraction condition and convergence rate in closed form (Sections 3.1 and 4.3). Second, we exhibit two physically distinct ontologies of the same device—a strict two‑level abstraction and a three‑level anharmonic ladder—and prove that, under any measurement chain that does not resolve the third level, their outcome distributions are identical with total‑variation distance exactly zero (Sections 3.2 and 4.4). Third, we anchor the analysis quantitatively by assuming a typical trapped‑ion readout fidelity of $99.991\%$, deriving the per‑shot error scale, the calibration iteration count needed to reach that scale, and the shot budget that would break the degeneracy once a leakage‑resolving observable exists (Section 4). Fourth, we identify the structural features—leakage‑resolving spectroscopy and cross‑platform consistency—that break the circularity, and we state explicitly what would falsify the thesis (Sections 4.5 and 6).

## 2. Background and Related Work

The literature bearing on this question falls into three groups: works that treat self‑referential reasoning as a formal method, works on quantum readout, and control‑theoretic treatments of systems whose working models are truncations of richer dynamics.

**Self‑referential diagnosis.** The closest structural analogue is adaptive fault diagnosis [1], which studies determining which processors in a remote location are reliable by asking them “Yes or No” questions, where the processors are of three types: those that always tell the truth, those that always lie, and those that sometimes do either. Its central move, as stated in its abstract, is that using self‑referential reasoning, along with earlier techniques, one can regard both the truth‑tellers and the liars as reliable. This is exactly the logical move our calibration loop performs: a readout channel whose “honesty’’ is in question is calibrated by sources whose calibration depends on the readout, and the fixed point legitimizes the whole chain at once.

**Readout as the anchor of the loop.** The work “High‑fidelity readout of trapped‑ion qubits’’ reports single‑shot qubit readout with fidelity sufficient for fault‑tolerant quantum computation. Its title states that it achieves high‑fidelity readout of trapped‑ion qubits, establishing the relevance of readout as the quantitative anchor for our analysis.

**Control of distributed and approximate models.** Reference [3] models a nonhomogeneous flexible wing under unsteady aerodynamic loads as a distributed‑parameter system of two coupled partial differential equations, actuated at the tip by flaps, and investigates well‑posedness of the underlying Cauchy problem before constructing the boundary control law. The methodological pattern—establish that the truncated closed‑loop model is well‑posed before designing the controller—mirrors our discipline of proving that the calibration fixed point exists before asking what it refers to.

Reference [6] treats exponential input‑to‑state stabilization of diagonal infinite‑dimensional systems with uncertain, time‑varying input delays, using a constant‑delay predictor feedback controller designed on a truncated finite‑dimensional model; the truncation there is explicitly a modeling choice whose stability consequences must be bounded, exactly as leakage out of the two‑level abstraction must be bounded in our model.

Reference [7] proposes a control‑oriented notion of finite‑state approximation, approximating discrete‑time plants with finite‑valued sensors and actuators by deterministic finite‑memory systems for certified‑by‑design controller synthesis; its framing—that the approximation is built for the controller, not derived from the physics—is the control‑theoretic statement of our claim that the qubit ontology is defined by the control loop rather than discovered by it.

**Hierarchical and constrained control.** Reference [4] describes the control of a rigid‑wing airborne wind energy system across all operational phases—take‑off, transition to power generation, pumping energy generation cycles, transition to hovering, and landing—via a hierarchical control structure with control design at all levels. This is the architectural template for a calibration hierarchy: distinct phases (drive calibration, readout calibration, tomography), each with its own control law, coupled sequentially.

Reference [5] introduces Input Constrained Control Barrier Functions (ICCBFs) for synthesizing safety‑critical controllers for nonlinear control‑affine systems with input constraints, identifying a subset of the safe set and constructing a controller rendering it forward invariant. We borrow the forward‑invariance idea as a question we pose but do not fully answer: is there a forward‑invariant “ontological safe set’’—a region of parameter space in which the two‑level abstraction is certified valid—and what barrier function enforces it?

**Quantum‑compliant formulations.** Reference [8] formulates network epidemic control—isolating locations by banning movement, modeled as link removal—in a quantum‑compliant way, building on discrete‑time susceptible‑infected‑susceptible and susceptible‑infected‑removed network models. Its relevance is methodological: it shows the quantum formalism applied as a modeling layer to a non‑quantum control loop, supporting our view that the quantum‑classical distinction is not what generates the self‑referential structure—the closure of the calibration chain is.

**QNFO corpus.** The corpus document “No Thing There: Control, Readout, and Self‑Referential Metrology in Engineered Quantum Systems’’ explains what control pulses actually manipulate and what readout measures across superconducting transmon, trapped‑ion, and spin‑qubit platforms, and includes a self‑referential metrology formalization. Our Sections 3–4 can be read as a formal companion to that document: where it explains, we derive.

## 3. Methods

### 3.1 The calibration loop as an iterated map

Let $\mathcal{H}_{\mathrm{sub}}$ denote the computational subspace (dimension $d=2$) and $\mathcal{H}_{\mathrm{full}}$ the full Hilbert space of the physical carrier. The calibration chain consists of stages indexed $j = 1, \dots, J$: drive calibration, Rabi calibration, readout discriminator calibration, and tomographic validation. Each stage $j$ has a parameter vector $\theta_j \in \mathbb{R}^{n_j}$ and a validation statistic $r_j$ computed from data produced using the current settings of all other stages. Collecting $\Theta = (\theta_1, \dots, \theta_J)$, the update is

$$\Theta_{k+1} = F(\Theta_k), \qquad F: \mathbb{R}^n \to \mathbb{R}^n.$$

A calibrated apparatus is a fixed point $\Theta_\star$ with $F(\Theta_\star) = \Theta_\star$. The self‑referential character is that $F$’s definition at every stage involves measurements taken through the apparatus being calibrated—the situation of [1], where the reliability of the witnesses is established by the testimony chain itself.

Near a fixed point, write $\Theta_k = \Theta_\star + \delta_k$. For a scalar gain model of one stage (the case relevant to drive‑amplitude calibration), the update is

$$x_{k+1} = x_k + g\,(r_k - r_\star),$$

where $x_k$ is the drive parameter, $g$ the loop gain, $r_k$ the observed statistic, and $r_\star$ the target. Linearizing, $r_k - r_\star = s\,(x_k - x_\star)$ with sensitivity $s$, gives the error recursion

$$e_{k+1} = (1 - g\,s)\,e_k, \qquad e_k \equiv x_k - x_\star.$$

The map is a contraction whenever $|1 - g\,s| < 1$, and then $e_k = e_0\,|1 - g\,s|^k$. This is the formal content of “the loop converges”: the fixed point is attractive and the chain self‑consistent—but nothing in the contraction argument refers to the physical substrate. The fixed point is a property of the loop, not of $\mathcal{H}_{\mathrm{full}}$. (A degenerate special case arises if the loop is instead written as a pure gain product $A \mapsto k_1 k_2 k_3 k_4\, A$: then a nontrivial fixed point requires $k_1 k_2 k_3 k_4 = 1$, and if that holds, *every* amplitude is a fixed point—a continuum of self‑consistent calibrations. We adopt the contraction model as primary and treat the gain‑product condition as the marginal, non‑contractive limit; see Appendix A.)

### 3.2 Two ontologies, one loop

We formalize the underdetermination conjecture with two models:

- **Model A (two‑level abstraction):** $\mathcal{H}_A = \mathrm{span}\{|0\rangle, |1\rangle\}$, with calibrated POVM $\{\Pi_0^{(A)}, \Pi_1^{(A)}\}$ acting on $\mathcal{H}_A$.
- **Model B (anharmonic three‑level carrier):** $\mathcal{H}_B = \mathrm{span}\{|0\rangle, |1\rangle, |2\rangle\}$, with the same calibrated POVM extended so that $\Pi_1^{(B)}$ projects onto the span of $\{|1\rangle, |2\rangle\}$—i.e., the readout does not resolve the third level, the generic situation when the readout transition addresses only the $|0\rangle \leftrightarrow |1\rangle$ distinction.

A control pulse with residual leakage amplitude $c$ produces, in Model B, the state

$$|\psi_B\rangle = \sqrt{1 - |c|^2}\,|1\rangle + c\,|2\rangle,$$

while Model A assigns the pure state $|1\rangle$. The outcome distributions are

$$p_A(1) = 1, \qquad p_B(1) = \langle \psi_B | \Pi_1^{(B)} | \psi_B \rangle = (1 - |c|^2) + |c|^2 = 1.$$

The total‑variation distance is

$$D_{\mathrm{TV}}(p_A, p_B) = \frac{1}{2}\sum_m |p_A(m) - p_B(m)| = 0.$$

Both ontologies are observationally identical under the full calibrated measurement set whenever the chain does not resolve level $|2\rangle$. The tomographic reconstruction—a function only of outcome distributions—is the same object in both cases. This is the precise sense in which the qubit ontology is underdetermined by its metrology: the loop fixes the *operational* qubit, and the operational qubit is compatible with multiple substrates.

**Connection to weak‑drive perturbation theory.** The leakage amplitude is not a free parameter: in a weakly anharmonic ladder driven near the $|0\rangle \leftrightarrow |1\rangle$ transition with Rabi amplitude $\Omega$ and anharmonicity‑scale detuning $\Delta$ on the $|1\rangle \leftrightarrow |2\rangle$ transition, adiabatic elimination of $|2\rangle$ (setting $\dot{c}_2 \approx 0$ in $\dot{c}_2 = -i\Delta c_2 - i\frac{\Omega}{2} c_1$) gives $c_2 \approx \frac{\Omega}{2\Delta} c_1$, so $|c|^2 \lesssim \left(\frac{\Omega}{2\Delta}\right)^2$. We use this to relate the abstract leakage amplitude to an operating point in Section 4.6.

### 3.3 Breaking the degeneracy

If the measurement chain is extended so that it resolves $|2\rangle$ (a leakage‑resolving measurement, with $\Pi_1$ projecting on $|1\rangle$ alone and a third outcome for $|2\rangle$), the distributions become

$$p_A(1) = 1, \qquad p_B(1) = 1 - |c|^2, \qquad p_B(2) = |c|^2,$$

and

$$D_{\mathrm{TV}}(p_A, p_B) = \frac{1}{2}\bigl(|c|^2 + |c|^2\bigr) = |c|^2.$$

The degeneracy is broken exactly to the extent that the measurement reaches outside the computational subspace. With $N$ independent shots, resolving a distribution difference of order $D_{\mathrm{TV}}$ requires roughly $N \sim D_{\mathrm{TV}}^{-2}$ shots (standard binomial scaling, stated as a modeling assumption for the projections below).

### 3.4 Cross‑platform constraint

A second route out of circularity is structural rather than statistical: two platforms whose calibration loops close differently (photonic readout as in [2], circuit readout, spin resonance) cannot both be saved by a single shared ontology unless that ontology is substrate‑specific. Requiring one consistent assignment of “what is excited’’ across platforms with different loop topologies is a constraint no single loop can generate—the analogue, in our setting, of the multi‑witness consistency that lets the self‑referential diagnosis of [1] classify its processors.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

**Input 1 (assumption).** Typical trapped‑ion single‑shot readout fidelity $f_{\mathrm{ro}} = 99.991\% = 0.99991$ (assumed based on reported high‑fidelity readout in the literature).

**Input 2 (assumption).** Adaptive measurement technique fidelity $f_{\mathrm{ad}} = 99.99\% = 0.99999$ (assumed as an improvement over the time‑resolved technique).

**Input 3 (model assumption, Section 3.2).** Leakage amplitude $|c| = 0.1$, i.e., leakage probability $|c|^2 = 0.01$.

**Input 4 (model assumption, Section 3.1).** Loop gain–sensitivity product $g\,s = 0.5$, giving contraction factor $|1 - g\,s| = 0.5$; initial calibration error $e_0 = 0.1$ in units of the drive parameter.

**Input 5 (model assumption, Section 3.2).** Weak‑drive operating point $\Omega/\Delta = 0.1$; tomographic shot budget $N_{\mathrm{tom}} = 10^4$ shots per element.

### 4.1 Readout error scale (projection)

The per‑shot readout error probability is

$$\varepsilon_{\mathrm{ro}} = 1 - f_{\mathrm{ro}} = 1 - 0.99991 = 9 \times 10^{-5}.$$

Over $N_{\mathrm{trials}} = 10^6$ trials, the expected number of misidentifications is

$$\mu = N_{\mathrm{trials}} \times \varepsilon_{\mathrm{ro}} = 10^6 \times 9 \times 10^{-5} = 90.$$

The one‑standard‑error uncertainty on $f_{\mathrm{ro}}$ over $10^6$ trials is

$$\sigma_f = \sqrt{\frac{f_{\mathrm{ro}}(1 - f_{\mathrm{ro}})}{N_{\mathrm{trials}}}}
= \sqrt{\frac{0.99991 \times 9\times10^{-5}}{10^6}}
\approx 9.49\times10^{-6}.$$

### 4.2 Adaptive‑technique improvement (projection)

The adaptive‑technique error is

$$\varepsilon_{\mathrm{ad}} = 1 - f_{\mathrm{ad}} = 1 - 0.99999 = 1 \times 10^{-5},$$

and the ratio of adaptive to time‑resolved error is

$$\frac{\varepsilon_{\mathrm{ad}}}{\varepsilon_{\mathrm{ro}}}
= \frac{1\times10^{-5}}{9\times10^{-5}}
\approx 0.11111.$$

### 4.3 Calibration‑loop convergence

With contraction factor $|1 - g\,s| = 0.5$ and $e_0 = 0.1$, the error after $k$ iterations is $e_k = 0.1 \times 0.5^k$. Taking as threshold the readout error scale $\varepsilon_{\mathrm{ro}} = 9\times10^{-5}$, we require

$$0.1 \times 0.5^k \le 9\times10^{-5}
\;\Longrightarrow\;
0.5^k \le 9\times10^{-4}.$$

Taking natural logarithms:

$$k \ge \frac{\ln(9\times10^{-4})}{\ln(0.5)}
= \frac{-7.01312}{-0.69315}
\approx 10.118.$$

Since $k$ must be integer, we check discretely: $0.5^{10}=9.7656\times10^{-4}>9\times10^{-4}$, while $0.5^{11}=4.8828\times10^{-4}\le9\times10^{-4}$. Hence

$$k_{\min}=11\text{ iterations},$$

with $e_{11}=0.1\times4.8828\times10^{-4}=4.8828\times10^{-5}<9\times10^{-5}<e_{10}=9.7656\times10^{-5}$.

### 4.4 Ontological distinguishability

From Section 3.3, with $|c|^2 = 0.01$ (Input 3):

$$D_{\mathrm{TV}}(p_A, p_B) = |c|^2 = 0.01 \quad\text{(leakage‑resolving measurement)},$$
$$D_{\mathrm{TV}}(p_A, p_B) = 0 \quad\text{(subspace‑restricted measurement)}.$$

### 4.5 Shot budget and noise‑floor margin (projection)

To resolve a distribution difference $\Delta p = |c|^2 = 0.01$ at one‑standard‑error significance, the binomial standard error $\sqrt{p(1-p)/N}$ must be $\le \Delta p$. Using the conservative bound $p\approx 1/2$,

$$\sqrt{\frac{1}{4N}} \le 0.01
\;\Longrightarrow\;
N \ge \frac{1}{4\times(0.01)^2}
= 2500\text{ shots}.$$

For a three‑sigma requirement,

$$3\sqrt{\frac{1}{4N}} \le 0.01
\;\Longrightarrow\;
N \ge \frac{9}{4\times(0.01)^2}
= 22500\text{ shots}.$$

The margin of a leakage signal over the readout noise floor is

$$\frac{|c|^2}{\varepsilon_{\mathrm{ro}}}
= \frac{0.01}{9\times10^{-5}}
\approx 111.$$

Thus a leakage‑resolving extension of a high‑fidelity readout would see the three‑level ontology clearly, provided the extension exists.

### 4.6 Weak‑drive consistency check (projection)

At the operating point $\Omega/\Delta = 0.1$ (Input 5), the adiabatic bound of Section 3.2 gives

$$\left(\frac{\Omega}{2\Delta}\right)^2
= \left(\frac{0.1}{2}\right)^2
= (0.05)^2
= 2.5\times10^{-3},$$

i.e. $|c|^2 \lesssim 2.5\times10^{-3}$, tenfold below the assumed $0.01$. Conversely, with $N_{\mathrm{tom}} = 10^4$ shots per tomographic element, the worst‑case binomial resolution at $\hat p = 1/2$ is

$$\sigma = \sqrt{\frac{0.5\times0.5}{10^4}}
= \sqrt{2.5\times10^{-5}}
= 5.0\times10^{-3},$$

which exceeds $2.5\times10^{-3}$ by a factor of $2$: at this operating point and budget, population tomography cannot resolve the leakage. Resolving $2.5\times10^{-3}$ at one sigma would require

$$N \ge \frac{0.25}{(2.5\times10^{-3})^2}
= 4.0\times10^4\text{ shots per element},$$

a $4\times$ increase over the assumed budget. At a stronger drive, $\Omega/\Delta = 0.4$, the bound becomes $(0.2)^2 = 4.0\times10^{-2}$, an order of magnitude above the $5.0\times10^{-3}$ floor—strong‑drive tomography would distinguish the ontologies. These statements are projections under the stated assumptions ($\Omega/\Delta$ values, worst‑case $\hat p = 1/2$, no systematic errors).

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic, or are labeled projections. No experimental or simulated data are reported in this paper.

- **R1 (readout error scale, projection).** Per‑shot error $\varepsilon_{\mathrm{ro}} = 9\times10^{-5}$; expected misidentifications in $10^6$ trials: $\mu = 90$; one‑standard‑error on the fidelity $\approx 9.49\times10^{-6}$.
- **R2 (adaptive improvement, projection).** $\varepsilon_{\mathrm{ad}} = 1\times10^{-5}$, a factor $\approx 0.11111$ (one‑ninth) of the time‑resolved error.
- **R3 (calibration convergence).** The loop reaches calibration error below the readout noise floor after $k_{\min}=11$ iterations ($e_{11}=4.8828\times10^{-5}$).
- **R4 (ontological degeneracy).** Under subspace‑restricted measurements, $D_{\mathrm{TV}} = 0$ exactly; under a leakage‑resolving measurement with $|c|=0.1$, $D_{\mathrm{TV}} = 0.01$.
- **R5 (shot budget).** $N \ge 2500$ shots for one‑sigma resolution of $\Delta p = 0.01$; $N \ge 225