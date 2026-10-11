# No Thing There: Observational Equivalence of Qubit Ontologies under Self-Referential Calibration Metrology

## Abstract

A working quantum engineer manipulates control pulses and records readout outcomes, but the physical referent of those operations — a spin, a collective mode, a circuit degree of freedom, or a deliberately abstracted two-level system — is never measured directly. It is fixed only by the calibration chain itself: drive calibration feeds Rabi calibration, which feeds dispersive readout calibration, which feeds tomography. This paper formalizes that chain as a self-consistent fixed-point problem and asks whether the qubit's ontology is underdetermined by the metrology that certifies it. We model calibration as a contractive iteration and derive its convergence condition ($0<g<2$ for a proportional update with gain $g$) and iteration count explicitly. We then construct a two-ontology comparison: a strict two-level abstraction versus a three-level anharmonic ladder, and derive, by adiabatic elimination, that their tomographically reconstructed populations differ by at most $(\Omega/2\Delta)^2$, where $\Omega$ is the drive Rabi amplitude and $\Delta$ the anharmonicity-scale detuning. For $\Omega/\Delta = 0.1$ the bound is $2.5\times 10^{-3}$, below the shot-noise resolution $\approx 5\times 10^{-3}$ of $10^4$ readout shots even at the $99.991\%$ single-shot fidelity reported for trapped-ion readout. We conclude that tomography alone cannot pin the qubit's substrate, and identify what would break the circularity: cross-platform consistency checks and Hamiltonian-tomography constraints that are sensitive to leakage rather than to populations alone.

## 1. Introduction

When an experimentalist "drives a qubit," something physical is excited; when the same experimentalist "reads out the qubit," something physical is measured. The engineering question posed in the source idea for this paper is blunt: if the billiard-ball picture is rejected, what exactly do the pulses manipulate, and what does the readout measure — excitations of what medium? The uncomfortable answer is that the answer is supplied by the calibration chain itself. The drive frequency is calibrated by finding a resonance; the Rabi rate is calibrated by fitting oscillations in a signal; the readout is calibrated by assigning measurement outcomes using states prepared by the already-calibrated drive; tomography is calibrated against all of the above. Each step certifies the others. The loop is closed, and the physical ontology of the qubit — collective mode, spin, circuit degree of freedom, or a two-level abstraction layered over a multi-level device — appears only as an internal bookkeeping choice within the loop.

This paper takes that observation seriously and formalizes it. We make three contributions. First, we model the calibration hierarchy as a discrete fixed-point iteration and derive its contraction condition and convergence rate in closed form (Section 4.1). Second, we show that two physically distinct ontologies of the same device — a strict two-level abstraction and a three-level anharmonic ladder — produce tomographic reconstructions that differ by a controllable, explicitly derived bound proportional to $(\Omega/2\Delta)^2$, and we evaluate that bound numerically against realistic readout statistics (Sections 4.2–4.3). Third, we argue that this observational equivalence is not a defect of any particular experiment but a structural feature of closed-loop metrology, and we derive what class of additional measurements would break the circularity (Section 4.4).

The epistemic status of our claims is deliberately modest: everything quantitative in this paper is derived here from stated assumptions, or is a clearly labeled projection. We do not claim that any real experiment is ontologically confused; we claim that the standard certification pipeline, taken on its own terms, cannot distinguish certain ontologies, and we quantify exactly how indistinguishable they are.

## 2. Background and Related Work

The literature that bears on this question splits into three groups: works that treat self-referential reasoning as a formal method, works in classical control theory whose structural moves we import, and works on quantum readout and quantum-adjacent control.

**Self-referential diagnosis.** The closest methodological antecedent is the adaptive fault diagnosis literature. Reference [1] studies the problem of determining which processors in a remote location are reliable by asking "Yes or No" questions, where the processors are of three types: those that always tell the truth, those that always lie, and those that sometimes tell the truth and sometimes lie. Its central move, as stated in its abstract, is that using self-referential reasoning, along with earlier techniques, one can regard both the truth-tellers and the liars as reliable. This is precisely the structure of calibration-loop metrology: a measurement channel whose own reliability is established by the very outcomes it reports can still be usable, provided the loop of mutual certifications closes consistently. We import this framing wholesale: the qubit's readout is a "processor" whose truthfulness is established self-referentially, and the open question is whether self-referential consistency fixes the *referent* of the reports, not merely their reliability.

**Quantum readout as the anchor measurement.** Reference [2] demonstrates single-shot qubit readout with fidelity sufficient for fault-tolerant quantum computation, for two types of qubit stored in single trapped calcium ions; for an optical qubit stored in the $(4S_{1/2}, 3D_{5/2})$ levels of $\,^{40}\mathrm{Ca}^+$ the authors achieve $99.991(1)\%$ average readout fidelity in one million trials using time-resolved photon counting, and an adaptive measurement technique allows $99.99\%$ fidelity. We use this work twice: as the source of the readout-fidelity figure that sets the noise floor in our observational-equivalence analysis (Section 4.3), and as a reminder that even a near-perfect readout channel is calibrated against state preparation, i.e., against the control loop. The abstract of [2] reports the fidelity; it does not report how the assignment map was calibrated, which is exactly the gap our formalization targets.

**Hierarchical and boundary control.** The calibration hierarchy we formalize is structurally a hierarchical control system. Reference [4] describes the control design of an airborne wind energy system with rigid aircraft across all operational phases — take-off, transition to power generation, pumping energy generation cycles, transition to hovering, and landing — via a hierarchical control structure in which control design at all hierarchical levels is described. Our calibration stack (drive → Rabi → readout → tomography) is the same shape: layers with distinct time constants, each stabilizing the layer below. Reference [3] treats boundary control of a nonhomogeneous flexible wing with bounded input disturbances, modeled as a distributed parameter system of two coupled partial differential equations actuated at its tip by flaps, with well-posedness of the underlying Cauchy problem investigated first. This matters to us because a qubit coupled to a readout resonator is likewise a distributed (field) system actuated at a boundary; the lesson of [3] — establish well-posedness of the closed-loop problem before designing the controller — is the lesson of Section 3: establish that the calibration fixed point exists before asking what it refers to. Reference [6] extends this line to exponential input-to-state stabilization of diagonal infinite-dimensional systems with uncertain, time-varying delays, using a constant-delay predictor feedback controller designed on a truncated finite-dimensional model. The phrase "truncated finite-dimensional model" is the crux: every qubit ontology is such a truncation, and [6] supplies the control-theoretic language (stabilization of the truncated model against disturbances of the full system) in which our two-ontology comparison is naturally stated.

**Safety and approximation constraints.** Reference [5] introduces Input Constrained Control Barrier Functions (ICCBFs) for synthesizing safety-critical controllers for nonlinear control-affine systems with input constraints, identifying a subset of the safe set and constructing a controller rendering it forward invariant, with the feedback controller given as the solution to a quadratic program. We use this as the template for a question we pose but do not fully answer: is there a forward-invariant "ontological safe set" — a region of parameter space in which the two-level abstraction is certified valid — and what barrier function enforces it? Reference [7] proposes a control-oriented notion of finite state approximation for approximating discrete-time plants with finite-valued sensors and actuators by deterministic finite memory systems, for certified-by-design controller synthesis, building on robust control ideas. This is the most directly relevant classical result to our thesis: the two-level qubit *is* a finite state approximation, and [7] frames exactly when such an approximation is certified for control purposes — certification for control, we emphasize, is weaker than certification of ontology.

**Quantum-compliant formulations.** Reference [8] formulates network epidemic control — isolating locations by banning movement, modeled as link removal in susceptible-infected-susceptible and susceptible-infected-removed discrete-time network models — as a quantum-compliant optimization problem. Its relevance is methodological: it shows control problems being re-expressed in quantum formalism for tractability, a reminder that the quantum formalism itself is a modeling layer whose physical interpretation is supplied externally. Finally, the QNFO corpus document [9], "No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems," is a pedagogical bridge between the qubit ontology critique and working physics, explaining what control pulses actually manipulate and what readout measures across superconducting transmon, trapped-ion, and spin qubit platforms, and including an electrical seesaw analogy and a self-referential metrology formalization. This paper is the formal companion to [9]: where [9] explains, we derive. Two further corpus entries, [10] on stabilization of Gottesman–Kitaev–Preskill states and [11] on a pre-registered falsification of deterministic measurement-triggered relaxation, are supplied with summaries too thin to support substantive statements; we note their topics only as adjacent corpus context and draw no claims from them.

## 3. Methods

### 3.1 The calibration loop as a fixed-point problem

Let $c \in \mathbb{R}^k$ denote the calibration vector: drive frequency, drive amplitude (Rabi rate), readout discriminator threshold, and measurement assignment weights. Each calibration stage is a map $\Phi_i: \mathbb{R}^k \to \mathbb{R}^k$, and the full chain is

$$
\Phi = \Phi_{\mathrm{tom}} \circ \Phi_{\mathrm{ro}} \circ \Phi_{\mathrm{Rabi}} \circ \Phi_{\mathrm{drive}},
$$

with the operational requirement that the deployed calibration $c^*$ satisfy

$$
c^* = \Phi(c^*).
$$

The self-referential character is that $\Phi_{\mathrm{ro}}$ (readout calibration) consumes state-preparation statistics produced using the output of $\Phi_{\mathrm{Rabi}}$ and $\Phi_{\mathrm{drive}}$, and $\Phi_{\mathrm{tom}}$ consumes all of them. No stage accesses the physical referent directly; each accesses only the outputs of the others.

### 3.2 Convergence model

We model each stage's iterative calibration as a proportional update on a scalar error $\delta_n$ (e.g., drive-frequency detuning from the true resonance in MHz):

$$
\delta_{n+1} = (1 - g)\,\delta_n,
$$

where $g > 0$ is the feedback gain. The fixed point $\delta^* = 0$ is contractive iff $|1 - g| < 1$, i.e., $0 < g < 2$. The residual after $n$ iterations is

$$
|\delta_n| = |1-g|^n\,|\delta_0|.
$$

### 3.3 Two-ontology device model

We compare two ontologies of the same driven device.

**Ontology A (two-level abstraction).** States $\{|0\rangle, |1\rangle\}$, drive couples them with Rabi amplitude $\Omega$. In the rotating frame the excited-state population under a resonant square pulse of duration $t$ is

$$
P_1^{(A)}(t) = \sin^2\!\left(\frac{\Omega t}{2}\right).
$$

**Ontology B (three-level anharmonic ladder).** States $\{|0\rangle, |1\rangle, |2\rangle\}$; the drive couples $|0\rangle \leftrightarrow |1\rangle$ with Rabi amplitude $\Omega$ on resonance, and couples $|1\rangle \leftrightarrow |2\rangle$ off-resonantly with detuning $\Delta$ (the anharmonicity scale). This is the standard truncation picture: ontology A is ontology B with the $|2\rangle$ level projected out.

### 3.4 Observational-equivalence criterion

Two ontologies are *tomographically indistinguishable at confidence* $\sigma$ if, for every tomographically reconstructed population $p$, the model predictions differ by less than the statistical resolution of the reconstruction:

$$
\left| P^{(A)}(t) - P^{(B)}(t) \right| < \sigma \quad \text{for all } t \text{ in the calibrated pulse set}.
$$

Here $\sigma$ is set by readout statistics: with single-shot assignment fidelity $F$ and $N$ shots per tomographic element, the binomial standard error of an estimated population $\hat{p}$ is

$$
\sigma = \sqrt{\frac{\hat{p}(1-\hat{p})}{N}},
$$

with a worst case at $\hat{p} = 1/2$. Assignment error from finite fidelity is $\epsilon = 1 - F$; we require $\epsilon < \sigma$ for the statistical floor to dominate, and we compare the ontology-separation bound to $\max(\sigma, \epsilon)$.

## 4. Analysis

### 4.1 Calibration fixed point: existence, contraction, and iteration count

**Input numbers.** Initial drive-frequency error $|\delta_0| = 10\ \mathrm{MHz}$ (a typical order of magnitude for a cold-start resonance search; stated as an assumption of this analysis, not a measurement). Feedback gain $g = 0.5$ (chosen mid-range within the stability window derived below). Target tolerance $|\delta_{\mathrm{tol}}| = 10^{-3}\ \mathrm{MHz} = 1\ \mathrm{kHz}$.

**Derivation 1 (stability window).** From $\delta_{n+1} = (1-g)\delta_n$, the iteration is a contraction iff $|1-g| < 1$. Solving: $-1 < 1 - g < 1$, i.e., $0 < g < 2$. With $g = 0.5$, $|1-g| = 0.5 < 1$: contractive. ∎

**Derivation 2 (iterations to tolerance).** Require $|1-g|^n |\delta_0| \le \delta_{\mathrm{tol}}$:

$$
0.5^n \times 10 \le 10^{-3}
\;\Rightarrow\;
0.5^n \le 10^{-4}
\;\Rightarrow\;
n \ge \frac{\ln(10^{-4})}{\ln(0.5)} = \frac{-9.21034}{-0.69315} = 13.288.
$$

Since $n$ is an integer, $n = 14$ iterations suffice. Check: $0.5^{14} = 6.1035\times 10^{-5}$, so $|\delta_{14}| = 10 \times 6.1035\times 10^{-5} = 6.10\times 10^{-4}\ \mathrm{MHz} = 610\ \mathrm{Hz} \le 1\ \mathrm{kHz}$. ∎

This establishes that the closed calibration loop is a well-posed contraction under mild conditions — the analogue, in our setting, of the well-posedness-first discipline of [3] — but note what the fixed point certifies: only internal consistency of the loop, not the ontology of the states it references.

### 4.2 Ontology separation by adiabatic elimination

**Setup.** In ontology B, the drive on the $|1\rangle \leftrightarrow |2\rangle$ transition is detuned by $\Delta \gg \Omega$. To second order in $\Omega/\Delta$, the off-resonant level $|2\rangle$ can be adiabatically eliminated: its steady amplitude tracks the $|1\rangle$ amplitude as

$$
c_2(t) \approx \frac{\Omega}{2\Delta}\, c_1(t),
$$

which follows from the equation of motion $\dot{c}_2 = -i\Delta c_2 - i\frac{\Omega}{2} c_1$ in the rotating frame: setting $\dot{c}_2 \approx 0$ gives $c_2 \approx \frac{\Omega}{2\Delta} c_1$. Hence the leakage population is

$$
P_2(t) = |c_2(t)|^2 \approx \left(\frac{\Omega}{2\Delta}\right)^2 P_1(t)
\;\le\;
\left(\frac{\Omega}{2\Delta}\right)^2,
$$

since $P_1(t) \le 1$. The two ontologies' predicted total excited-block populations differ by exactly this leakage:

$$
\left| P^{(A)}_{\mathrm{block}}(t) - P^{(B)}_{\mathrm{block}}(t) \right| = P_2(t) \le \left(\frac{\Omega}{2\Delta}\right)^2.
$$

**Input numbers.** We take $\Omega/\Delta = 0.1$ as the operating point (a weak-drive regime; stated as an assumption of this analysis). Then

$$
\left(\frac{\Omega}{2\Delta}\right)^2 = \left(\frac{0.1}{2}\right)^2 = (0.05)^2 = 2.5\times 10^{-3}.
$$

**Derivation 3 (separation bound).** $D_{\mathrm{ont}} \equiv \max_t |P^{(A)} - P^{(B)}| \le 2.5\times 10^{-3}$. ∎

### 4.3 Comparison against the readout noise floor

**Input numbers.** From [2], single-shot readout fidelity $F = 0.99991$ (the $99.991(1)\%$ figure for the optical qubit in $\,^{40}\mathrm{Ca}^+$), so the assignment error is

$$
\epsilon = 1 - F = 1 - 0.99991 = 9\times 10^{-5}.
$$

Shot number per tomographic element: $N = 10^4$ (assumption of this analysis, typical of tomographic budgets).

**Derivation 4 (statistical resolution).** Worst-case binomial standard error at $\hat{p} = 1/2$:

$$
\sigma = \sqrt{\frac{0.5 \times 0.5}{10^4}} = \sqrt{\frac{0.25}{10^4}} = \sqrt{2.5\times 10^{-5}} = 5.0\times 10^{-3}.
$$

**Derivation 5 (observational equivalence).** The effective discrimination floor is $\max(\sigma, \epsilon) = \max(5.0\times 10^{-3},\, 9\times 10^{-5}) = 5.0\times 10^{-3}$. The ontology separation is $D_{\mathrm{ont}} \le 2.5\times 10^{-3} < 5.0\times 10^{-3}$. Therefore, at this operating point and shot budget, ontologies A and B are tomographically indistinguishable: the leakage signature is buried at a factor

$$
\frac{\sigma}{D_{\mathrm{ont}}} = \frac{5.0\times 10^{-3}}{2.5\times 10^{-3}} = 2
$$

below the statistical floor even before systematic readout errors are considered. ∎

**Projection (labeled).** To *resolve* the distinction at $1\sigma$ would require the shot budget satisfying $\sqrt{0.25/N} \le 2.5\times 10^{-3}$, i.e., $N \ge 0.25/(2.5\times 10^{-3})^2 = 0.25/6.25\times 10^{-6} = 4.0\times 10^4$ shots per element — a $4\times$ increase over the assumed budget, under the stated assumptions ($\Omega/\Delta = 0.1$, worst-case $\hat{p}=1/2$, no systematic errors). This is a projection, not a measurement.

### 4.4 What would break the circularity

The equivalence above is a statement about *population* tomography, which is blind to coherence in the eliminated subspace. Two classes of measurement escape it, by construction of the model:

1. **Leakage-sensitive spectroscopy.** A measurement that couples to $|2\rangle$ directly (e.g., a probe resonant with the $|1\rangle \leftrightarrow |2\rangle$ transition) reads $P_2$ without reference to the qubit assignment map. In the model, this measures the ratio $\Omega/(2\Delta)$ against an independently calibrated $\Omega$, breaking the loop because the referent of the probe is fixed outside the qubit's own calibration chain.
2. **Cross-platform consistency.** If two devices with different anharmonicity ratios $\Delta_1 \neq \Delta_2$ are calibrated by the same self-referential protocol yet must agree on shared tomographic predictions, the leakage terms $(\Omega/2\Delta_1)^2 \neq (\Omega/2\Delta_2)^2$ become observable in the disagreement. The circularity is broken by requiring one ontology to explain two loops.

Both are, at present, structural arguments within the model of Section 3.3, not empirical claims.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic, or are labeled projections.

- **R1 (calibration convergence).** The proportional calibration update $\delta_{n+1} = (1-g)\delta_n$ is contractive iff $0 < g < 2$ (Derivation 1). For $g = 0.5$, $|\delta_0| = 10\ \mathrm{MHz}$, and tolerance $10^{-3}\ \mathrm{MHz}$, convergence takes $n = 14$ iterations, leaving residual $|\delta_{14}| = 6.10\times 10^{-4}\ \mathrm{MHz}$ (Derivation 2).
- **R2 (ontology separation bound).** Under adiabatic elimination of the third level, the maximum population discrepancy between the two-level and three-level ontologies is $D_{\mathrm{ont}} \le (\Omega/2\Delta)^2 = 2.5\times 10^{-3}$ at $\Omega/\Delta = 0.1$ (Derivation 3).
- **R3 (noise floor).** With readout fidelity $F = 0.99991$ from [2] and $N = 10^4$ shots per element, the discrimination floor is $\max(\sigma, \epsilon) = 5.0\times 10^{-3}$, with $\sigma = 5.0\times 10^{-3}$ and $\epsilon = 9\times 10^{-5}$ (Derivations 4–5).
- **R4 (observational equivalence).** Since $D_{\mathrm{ont}} = 2.5\times 10^{-3} < 5.0\times 10^{-3}$, the two ontologies are tomographically indistinguishable at the stated operating point; the separation sits a factor of $2$ below the statistical floor (Derivation 5).
- **R5 (projection).** Resolving the distinction at $1\sigma$ requires $N \ge 4.0\times 10^4$ shots per element, a $4\times$ increase, under the stated assumptions. Labeled projection; uncertainty is dominated by the assumed operating point $\Omega/\Delta = 0.1$ and by neglected systematic errors, which would raise the required $N$.

No experimental or simulated data are reported in this paper.

## 6. Discussion

**What the result does and does not show.** R4 shows that a specific pair of ontologies is indistinguishable by a specific measurement class (population tomography) at a specific operating point. It does not show that qubit ontology is unknowable, nor that all ontologies are equivalent. The equivalence is quantitative and degrades predictably: at larger $\Omega/\Delta$ the leakage grows as $(\Omega/2\Delta)^2$, and at $\Omega/\Delta = 0.4$ the bound would be $(0.2)^2 = 4.0\times 10^{-2}$, an order of magnitude above the floor of R3 — strong-drive tomography would distinguish the ontologies. The underdetermination is therefore a statement about the weak-drive, high-fidelity regime that fault-tolerant operation favors, not a universal claim.

**Limitations of the model.** The adiabatic-elimination step (Section 4.2) is a second-order approximation valid for $\Omega \ll \Delta$; it neglects counter-rotating terms, pulse-shape effects (a shaped pulse has a different leakage spectrum than a square pulse), and higher levels beyond $|2\rangle$. The calibration model of Section 3.2 is scalar and linear; a real calibration vector has cross-couplings between stages, and the contraction analysis of Derivation 1 does not establish uniqueness of the fixed point in the coupled case. The noise-floor comparison treats assignment error $\epsilon$ and shot noise $\sigma$ as independent; correlated errors (e.g., drift during the tomography run) would inflate the floor, strengthening R4, but we have not modeled them.

**Failure modes of the thesis.** The claim "tomography cannot pin the referent" would be falsified by a demonstration that standard population tomography, at ordinary shot budgets, systematically distinguishes the two-level and three-level ontologies — i.e., if measured leakage residuals exceeded $(\Omega/2\Delta)^2$ by an unmodeled mechanism. It would also be weakened if the calibration loop were shown to have observable consequences that depend on ontology — for instance, if the fixed point $c^*$ itself differed between ontologies A and B in a way that survives the noise floor. We have not analyzed the ontology-dependence of $c^*$; this is an open question.

**Against ourselves.** A defender of operationalism could argue that the underdetermination is trivial: science routinely underdetermines ontology, and the qubit is no worse off than the electron. Our reply is that the situation is sharper here because the certification chain is closed — there is no measurement of the qubit that is not calibrated through the qubit — whereas, e.g., in [1]'s fault-diagnosis setting, self-referential reasoning suffices to identify *reliable reporters* but the papers' own framing leaves the identity of the reporters as given. Whether an analogous "reliability without referent" result can be proven for the full calibration hierarchy, rather than argued by analogy, is the central open question this paper poses. A second self-criticism: our escape routes (Section 4.4) presuppose that some measurement exists whose referent is fixed outside the loop; a strict operationalist would deny this, and we have no model that adjudicates.

**Relation to the classical control literature.** The truncation at the heart of ontology A is the same move as the "truncated finite-dimensional model" of [6], and the certification question is the one [7] poses for finite state approximation: certified for control is not certified as ontology. The barrier-function framing of [5] suggests a concrete formalization of the "ontological safe set" — the parameter region where $D_{\mathrm{ont}} < \max(\sigma,\epsilon)$ — as a forward-invariant set under drift in $\Omega/\Delta$; constructing that barrier is open. The hierarchical structure of [4] and the boundary-actuation picture of [3] supply the structural vocabulary but no quantum-specific content, and we have used them only at that level. Reference [8]'s re-expression of a classical control problem in quantum formalism is a caution in both directions: the formalism is a layer, and so is our ontology debate.

## 7. Conclusion

We formalized qubit calibration as a closed, self-referential fixed-point problem, showed it is contractive under a mild gain condition ($0 < g < 2$, with a worked convergence of 14 iterations from a 10 MHz error to 610 Hz), and derived an explicit observational-equivalence bound between a two-level and a three-level ontology of the same device: $D_{\mathrm{ont}} \le (\Omega/2\Delta)^2 = 2.5\times 10^{-3}$ at $\Omega/\Delta = 0.1$, below the $5.0\times 10^{-3}$ statistical floor of $10^4$-shot tomography even against a $99.991\%$ readout fidelity. The conclusion is not that qubits have no ontology, but that the standard certification pipeline — the only access the engineer has — underdetermines it, with a quantified gap. Breaking the circularity requires measurements whose referent is fixed outside the qubit's own loop: leakage-sensitive probes or cross-platform consistency constraints. Quantifying how much circularity such measurements remove, and whether the calibration fixed point $c^*$ itself carries ontology-dependent content, are the open problems this paper hands forward.

## References

[1] arXiv:1407.6255v1 | Adaptive Fault Diagnosis using Self-Referential Reasoning
[2] arXiv:0802.1684v2 | High-fidelity readout of trapped-ion qubits
[3] arXiv:1709.00759v2 | Boundary Control of a Nonhomogeneous Flexible Wing with Bounded Input Disturbances
[4] arXiv:2006.11141v1 | Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases
[5] arXiv:2104.01704v1 | Safe Control Synthesis via Input Constrained Control Barrier Functions
[6] arXiv:2003.05711v1 | Exponential input-to-state stabilization of a class of diagonal boundary control systems with delay boundary control
[7] arXiv:1105.3788v3 | A Control-Oriented Notion of Finite State Approximation
[8] arXiv:2509.00337v1 | A Quantum-Compliant Formulation for Network Epidemic Control
[9] QNFO: No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems
[10] QNFO: Stabilization of Gottesman-Kitaev-Preskill States
[11] QNFO: A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation