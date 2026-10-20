# Error-Budget Arithmetic for Planar Fluxonium-Controlled Bosonic Error Correction: A Derived-Metric Reassessment with Literature Benchmarks

## Abstract

Bosonic quantum error correction (QEC) encodes one logical qubit into a single oscillator mode, promising fault tolerance with far fewer physical components than qubit-based surface codes, yet superconducting demonstrations have historically been limited by the short bit-flip lifetimes of the transmon ancillas that control centimeter-scale 3D cavities. A gap remains between the architectural promise of bosonic codes and a quantitative account of what changes when the control ancilla is a heavy fluxonium with a bit-flip lifetime of $451 \pm 70~\mu\mathrm{s}$ on a fully planar chip. This paper performs a derived-metric analysis of the fluxonium-based demonstration documented in the literature: from the reported bit-flip lifetime and logical lifetime extension factor $F = 1.59 \pm 0.05$ we derive, with all arithmetic shown, an ancilla bit-flip rate $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34) \times 10^{3}~\mathrm{s}^{-1}$, a fractional removal of $0.371 \pm 0.020$ of the logical decay rate, a per-cycle ancilla error probability of $0.0219 \pm 0.0034$ at an assumed $10~\mu\mathrm{s}$ cycle time, and the structural result that the steady-state ancilla-induced logical error rate equals $\eta\,\Gamma_{\mathrm{bf}}$ independent of cycle speed. Benchmarked against the surface-GKP threshold literature and resource comparisons, the result identifies fluxonium dephasing, finite-energy GKP squeezing, reset latency, and spiral-resonator loss as the four measurable failure modes that will decide whether planar bosonic QEC scales.

## 1. Introduction

Superconducting quantum processors face a scaling problem that is fundamentally about error-correction overhead. Qubit-based surface codes demand thousands of physical qubits per logical qubit, and this resource overhead blocks near-term deployment of error-corrected algorithms and inflates the cost of quantum processors [13]. Bosonic QEC offers an alternative economy: one logical qubit is encoded into the large Hilbert space of a single oscillator mode, and several bosonic codes have reached break-even operation, where the logical qubit outlives an unprotected physical qubit in the same system [11]. The practical obstacle has been an asymmetry inside the hardware itself: the oscillator (historically a 3D microwave cavity) is long-lived, while the control qubit that prepares, stabilizes, and measures the bosonic code is the weak link, with bit-flip times that cap the logical lifetime no matter how good the code is.

A recent fluxonium-based demonstration, analyzed quantitatively in [12], attacks exactly this asymmetry. Heavy fluxonium — a superconducting artificial atom with a large shunt capacitance and an inductive loop whose low-frequency transitions suppress relaxation matrix elements — achieves a bit-flip lifetime of $T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$, and controls an on-chip Archimedean spiral resonator, a planar structure whose mode volume is orders of magnitude smaller than a centimeter-scale 3D cavity. The protocol combines finite-energy Gottesman–Kitaev–Preskill (GKP) state preparation, measurement-free (feedback-free) stabilization, and rapid fluxonium reset, and reports a logical lifetime extension factor of $F = 1.59 \pm 0.05$ [12]. If the error-budget arithmetic behind these numbers holds up under scrutiny, the design decision it changes is concrete: QEC architects can treat the ancilla bit-flip channel as a secondary term rather than the dominant one, and fabrication planners can route bosonic QEC through planar chip processes instead of 3D cavity packaging.

This paper is a derived-metric reassessment, not a replication. It performs no simulation and reports no new measurements; every quantitative claim is either arithmetic on numbers reported in [12] and reused in [13], or an explicitly labeled projection with stated assumptions. The contributions are:

1. **Error-budget arithmetic.** From $T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ and $F = 1.59 \pm 0.05$ we derive the ancilla bit-flip rate with propagated uncertainty, the fractional removal of the logical decay rate, and per-cycle ancilla error probabilities under a stated cycle-time assumption, with every step shown (Section 4, results in Section 5).
2. **A steady-state structural result.** We show that the ancilla-induced logical error rate in steady state equals $\eta\,\Gamma_{\mathrm{bf}}$ (with $\eta$ the flip-to-logical conversion factor) independent of cycle speed, so reset speed governs tracking of oscillator errors but not the ancilla floor (Section 4.4).
3. **Literature benchmarking.** We place the derived numbers against the bosonic-QEC review literature [1], [6], the surface-GKP threshold analysis [10], squeezing-threshold results for continuous-variable architectures [5], [7], and alternative bosonic encodings [2], [3], [4], [8], [9], [11] (Section 2 and Section 4.5).
4. **Falsifiability and engineering pathway.** We state which measurements would undermine the assessment that planar fluxonium-GKP is the leading route to scalable bosonic QEC (Section 6), and translate the result into a concrete readiness level, user set, and smallest next experiment (Section 7).

## 2. Background and Related Work

**The object of analysis.** Reference [12] documents the planar fluxonium-based bosonic error-correction demonstration and its quantitative reassessment: a heavy fluxonium ancilla with $T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ controls an Archimedean spiral resonator, finite-energy GKP states are stabilized by measurement-free error correction with rapid fluxonium reset, and the measured logical lifetime extension is $F = 1.59 \pm 0.05$. Reference [12] further derives the ancilla bit-flip rate $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34) \times 10^{3}~\mathrm{s}^{-1}$, the per-cycle ancilla error probability $p_{\mathrm{bf}}^{\mathrm{flx}} = 0.0219 \pm 0.0034$ at an assumed cycle time $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$, and the finding that $62.9\% \pm 2.0\%$ of the logical decay rate remains uncorrected. This paper re-derives those quantities independently, extends the analysis with a steady-state structural result, and benchmarks it against the wider literature.

**A second use of the same numbers.** Reference [13] consumes the fluxonium error budget for a different purpose: it extracts $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$ and the same $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$ assumption, computes an effective physical error probability per cycle $p_{\mathrm{phys}} = 2.19 \times 10^{-2}$, and derives a falsifiable separation between geometrically inspired QEC codes and the surface code — a logical error rate of $p_L^{\mathrm{geom}} = 7.1 \times 10^{-5}$ for a distance-5 geometric code versus $p_L^{\mathrm{SC}} = 5.1 \times 10^{-9}$ for the surface code under identical parameters. The fact that two independent analyses converge on the same per-cycle error probability from the same inputs is a consistency check we exploit in Section 4.3. Reference [13] also states the motivation we adopt: surface-code overhead "blocks near-term deployment of error-corrected algorithms and inflates the cost of quantum processors."

**The bosonic-QEC architectural frame.** Reference [1] reviews bosonic error correction for superconducting devices with emphasis on the GKP qubit, defining the field's core object: the representation of a qubit as a two-dimensional subspace of an oscillator, together with error correction on that qubit and a suite of techniques for universal computation. Its preliminaries fix the phase-space formalism ($\hat{q} = (\hat{a} + \hat{a}^\dagger)/\sqrt{2}$, $\hat{p} = i(\hat{a}^\dagger - \hat{a})/\sqrt{2}$, $[\hat{q}, \hat{p}] = i$) that underlies the shift-error model used throughout this paper, and its treatment of the noise-biased cat qubit shows how engineered dissipation ($\kappa_{2\mathrm{ph}}$ two-photon loss stabilizing $\ket{\pm\alpha}$) can itself perform part of the correction — the same logic family as the measurement-free stabilization in the fluxonium demonstration [12]. Reference [6] complements this with the architectural inversion that motivates the whole field: in the qubit-based architecture quantum information lives on qubits while oscillators couple and read them out, whereas in the bosonic architecture information lives in the bosonic modes and qubits supply the nonlinearity for control and readout. Reference [6] also catalogs GKP, cat, and binomial codes on a single mode with their experimental progress, and its outlook identifies the challenges — extensions of current bosonic systems and demonstrations of quantum advantage — that the fluxonium result addresses on the ancilla side.

**Thresholds and squeezing budgets.** Reference [10] analyzes the surface-GKP code — GKP qubits concatenated with the rotated surface code requiring $d^2$ data qubits and $d^2 - 1$ syndrome qubits — and simulates the full error-correction protocol with independent noise parameters $\sigma_{\mathrm{gkp}}$ and $\sigma$. Its threshold table gives, for the gate-based surface-GKP code, a fault-tolerance threshold of $\sigma_{\mathrm{gkp}}^{\star} = 0.194$, corresponding to $11.2$ dB of GKP squeezing with no post-selection. This number is the benchmark against which any finite-energy GKP implementation, including the fluxonium-controlled spiral resonator, must be measured: if the achievable squeezing falls below the level at which photon-loss-induced shifts remain correctable, the ancilla improvements derived in Section 4 become irrelevant. Reference [5] supplies the squeezing context from the optical side: its continuous-variable quantum-repeater architecture based on GKP error correction and teleportation outperforms direct one-way transmission only when the squeezing level exceeds 15 dB, and it notes that a full-scale repeater node needs multiple GKP ancilla modes. Reference [7] independently states the threshold regime for measurement-based computing with continuous-variable cluster states: fault tolerance requires measured squeezing of 15–17 dB, supplemented with high-quality bosonic qubits. Reference [2] reports that the current experimental squeezing record stands at 15 dB, which bounds what any GKP-type scheme can assume today. Together [2], [5], [7], and [10] bracket the squeezing budget between a 11.2 dB gate-based threshold and a 15 dB hardware record — a narrow margin that Section 6 identifies as a first-order risk.

**Alternative encodings as comparators.** Reference [4] constructs an error-correction code from squeezed Fock states, showing that the first squeezed Fock state corrects both photon loss and dephasing better than higher-order states, and that the approximate Knill–Laflamme conditions are satisfied for squeezed Fock states with arbitrary occupation number $n$, with orthogonality conditions met as squeezing tends to infinity. Reference [3] develops the comparison quantitatively using the Knill–Laflamme cost function $C_{\mathrm{KL}} = \sum_{a,b} |f_{00ab} - f_{11ab}|^2 + |f_{01ab}|^2$ and the Petz map fidelity, finding that the second squeezed Fock state is the most appropriate of its family for protecting information in a channel with particle loss and dephasing. Reference [2] extends the family to codes built from particle-number measurements on two-mode Gaussian states, showing that states from measuring an even number of particles are preferable for particle-loss correction and that larger measured particle numbers are more advantageous; its feasibility analysis reports generation probabilities for the optimal codeword pairs in the range $1.2\%$ to $2.2\%$. These works matter here because they define the comparator space: if fluxonium-GKP stabilization stalls, squeezed-Fock-state codes with explicit Knill–Laflamme cost metrics are the nearest alternative on the same oscillator hardware.

**Application-side demand.** Reference [8] analyzes quantum repeaters with binomial codes in microwave cavities, finding that both the lower and higher binomial codes outperform unencoded schemes at equal memory coherence times, that the higher binomial code surpasses unencoded protocols even with lower coherence times, and that multiple-error correction yields a better secret key fraction than single-error correction. Reference [9] quantifies an all-optical memory in which a GKP-encoded qubit is stored in a fiber loop modeled as a pure-loss channel and periodically stabilized by teleportation-based correction. Reference [11] identifies the two-mode controlled-rotation (CROT) gate as the critical correction primitive for rotation-symmetric bosonic codes such as cat codes, and derives a single-tone transmon-drive scheme that amplifies the effective cross-Kerr interaction to implement it with code-agnostic error propagation. These three works establish that demand for oscillator-level correction exists across repeaters, memories, and gate primitives — so improvements to the ancilla side of bosonic QEC propagate into multiple application stacks.

**Measurement finitude as a reporting convention.** Reference [14] argues that all physical measurements produce finite-precision rational numbers, citing the Bekenstein bound, the Holevo bound, and thermal noise as independent physical bounds on infinite-precision measurement. We adopt the operational consequence for this paper: reported values such as $451~\mu\mathrm{s}$ and $1.59$ are treated as finite-precision decimals carrying their stated uncertainties, and derived quantities are quoted with no more precision than the propagation supports.

## 3. Methods

The method is derived-metric analysis: a small set of reported numbers is propagated through standard QEC error-budget relations to obtain quantities the experiment implies but does not state directly. No simulation is performed; every result is either exact arithmetic on reported inputs or a labeled projection with stated assumptions.

**Inputs.**

- $I_1$: ancilla bit-flip lifetime $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$, uncertainty $\pm 70~\mu\mathrm{s}$ (reported in [12], reused in [13]).
- $I_2$: logical lifetime extension factor $F = 1.59$, uncertainty $\pm 0.05$ (reported in [12]).
- $I_3$: assumed correction cycle time $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$ (an assumption, used identically in [12] and [13]; not a reported measurement).
- $I_4$: assumed transmon baseline bit-flip lifetime $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s}$, representative of the fixed-frequency transmons used in prior 3D-cavity bosonic demonstrations; labeled an assumption.
- $I_5$: assumed flip-to-logical conversion factor $\eta = 0.1$, the fraction of ancilla flips that corrupt the logical state; labeled an assumption.
- $I_6$: squeezing thresholds and records from the literature: $11.2$ dB gate-based surface-GKP threshold [10], 15 dB record [2], 15–17 dB measurement-based fault-tolerance regime [7], $> 15$ dB repeater advantage threshold [5].

**Defining relations.**

1. *Ancilla bit-flip rate:* $\Gamma_{\mathrm{bf}} = 1 / T_1^{\mathrm{bf}}$.
2. *Corrected and uncorrected logical lifetimes:* with extension factor $F$, $T_L^{(1)} = F\, T_L^{(0)}$ and $\Gamma_L^{(1)} = \Gamma_L^{(0)} / F$.
3. *Per-cycle bit-flip probability* under a Poisson model with rate $\Gamma_{\mathrm{bf}}$:
$$p_{\mathrm{bf}}(T_{\mathrm{cyc}}) = 1 - e^{-\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}} \approx \Gamma_{\mathrm{bf}} T_{\mathrm{cyc}} \quad \text{for } \Gamma_{\mathrm{bf}} T_{\mathrm{cyc}} \ll 1.$$
4. *Steady-state ancilla-induced logical rate:* if each ancilla flip corrupts the logical state with probability $\eta$, and cycles occur at rate $1/T_{\mathrm{cyc}}$, the ancilla-induced logical error rate per unit time is $\eta\,\Gamma_{\mathrm{bf}}$; the derivation is given in Section 4.4.
5. *Uncertainty propagation:* for $q = f(I_1, I_2)$ with independent inputs,
$$\sigma_q^2 = \left(\frac{\partial f}{\partial I_1}\right)^2 \sigma_{I_1}^2 + \left(\frac{\partial f}{\partial I_2}\right)^2 \sigma_{I_2}^2.$$

**Scope convention.** Following the measurement-finitude convention of [14], all inputs are finite-precision decimals; derived values are rounded so that quoted precision never exceeds what the propagated uncertainty supports. The absolute uncorrected logical lifetime $T_L^{(0)}$ is not among the inputs, so all lifetime results are reported either as ratios or as functions of the assumed $\eta$.

## 4. Analysis

### 4.1 Ancilla bit-flip rate

**Input $I_1$** ([12], reused in [13]): $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s} = 451 \times 10^{-6}~\mathrm{s} = 4.51 \times 10^{-4}~\mathrm{s}$.

$$\Gamma_{\mathrm{bf}} = \frac{1}{T_1^{\mathrm{bf}}} = \frac{1}{4.51 \times 10^{-4}~\mathrm{s}} = 2.2173 \times 10^{3}~\mathrm{s}^{-1}.$$

Step check: $1 / 4.51 \times 10^{-4} = 10^{4} / 4.51 = 2217.29~\mathrm{s}^{-1}$, so $\Gamma_{\mathrm{bf}} \approx 2.2173 \times 10^{3}~\mathrm{s}^{-1}$, i.e., about $2.2173$ bit flips per millisecond of exposure.

**Uncertainty.** With $\sigma_T = 70~\mu\mathrm{s} = 7.0 \times 10^{-5}~\mathrm{s}$ and $f(T) = 1/T$, $\partial f/\partial T = -1/T^2$, so

$$\sigma_{\Gamma} = \frac{\sigma_T}{T^2} = \frac{7.0 \times 10^{-5}}{(4.51 \times 10^{-4})^2}.$$

Compute the denominator: $(4.51 \times 10^{-4})^2 = 20.3401 \times 10^{-8} = 2.03401 \times 10^{-7}~\mathrm{s}^2$. Then

$$\sigma_{\Gamma} = \frac{7.0 \times 10^{-5}}{2.03401 \times 10^{-7}} = 344.1~\mathrm{s}^{-1}.$$

Thus $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34) \times 10^{3}~\mathrm{s}^{-1}$. The relative uncertainty is $344.1 / 2217.3 = 0.1552$, i.e., $15.5\%$, which equals the relative uncertainty of $T_1^{\mathrm{bf}}$ itself ($70/451 = 0.15521$), as required for a reciprocal quantity.

### 4.2 Fractional reduction in logical decay rate

**Input $I_2$** ([12]): $F = 1.59 \pm 0.05$.

The corrected logical decay rate is

$$\Gamma_L^{(1)} = \frac{\Gamma_L^{(0)}}{F} = \frac{\Gamma_L^{(0)}}{1.59} = 0.62893\,\Gamma_L^{(0)}.$$

Step check: $1/1.59 = 0.628931\ldots$ The fractional reduction in logical decay rate is

$$1 - \frac{1}{F} = 1 - 0.62893 = 0.37107,$$

i.e., the correction removes approximately $37.1\%$ of the logical decay rate, and the residual (uncorrected) fraction of the logical error budget is $1/F = 0.6289 \approx 62.9\%$.

**Uncertainty.** With $f(F) = 1/F$, $\partial f/\partial F = -1/F^2 = -1/(1.59)^2$. Compute $1.59^2 = 2.5281$, so $|\partial f/\partial F| = 1/2.5281 = 0.39555$. Then

$$\sigma_{1/F} = 0.39555 \times 0.05 = 0.01978 \approx 0.020.$$

The residual fraction is $0.629 \pm 0.020$, and the removed fraction is $0.371 \pm 0.020$.

### 4.3 Per-cycle ancilla bit-flip probability

The measurement-free protocol relies on the fluxonium returning to its ground state via rapid reset between correction interactions. During one correction cycle of duration $T_{\mathrm{cyc}}$, the probability that the ancilla has flipped is, under the Poisson model,

$$p_{\mathrm{bf}}(T_{\mathrm{cyc}}) = 1 - e^{-\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}}.$$

The small-argument expansion requires $\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}} \ll 1$, i.e., $T_{\mathrm{cyc}} \ll 1/\Gamma_{\mathrm{bf}} = 4.51 \times 10^{-4}~\mathrm{s} = 451~\mu\mathrm{s}$.

**Worked example at the assumed $T_{\mathrm{cyc}} = 10~\mu\mathrm{s} = 1.0 \times 10^{-5}~\mathrm{s}$** (input $I_3$; an assumption, not a reported number):

$$\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}} = (2.2173 \times 10^{3}~\mathrm{s}^{-1})(1.0 \times 10^{-5}~\mathrm{s}) = 2.2173 \times 10^{-2}.$$

$$p_{\mathrm{bf}} = 1 - e^{-0.022173}.$$

Compute the exponential by series: $e^{-0.022173} \approx 1 - 0.022173 + 0.022173^2/2 - 0.022173^3/6 = 1 - 0.022173 + 0.00024582 - 0.00000182 = 0.978071$. Hence

$$p_{\mathrm{bf}}^{\mathrm{flx}} = 1 - 0.978071 = 0.021929 \approx 0.0219 \; (2.19\%).$$

This value matches the $p_{\mathrm{phys}} = 2.19 \times 10^{-2}$ independently computed in [13] from the same inputs, and the $p_{\mathrm{bf}}^{\mathrm{flx}} = 0.0219 \pm 0.0034$ derived in [12] — a two-way consistency check on the arithmetic.

**Transmon baseline comparison** (input $I_4$, assumption). A transmon with $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s} = 3.0 \times 10^{-5}~\mathrm{s}$ gives

$$\Gamma_{\mathrm{bf}}^{\mathrm{tm}} = \frac{1}{3.0 \times 10^{-5}~\mathrm{s}} = 3.3333 \times 10^{4}~\mathrm{s}^{-1},$$

$$\Gamma_{\mathrm{bf}}^{\mathrm{tm}} T_{\mathrm{cyc}} = (3.3333 \times 10^{4})(1.0 \times 10^{-5}) = 0.33333,$$

$$p_{\mathrm{bf}}^{\mathrm{tm}} = 1 - e^{-0.33333}.$$

Compute: $e^{-0.33333} \approx 1 - 0.33333 + 0.055556 - 0.0061728 + 0.00051440 - 0.0000343 = 0.716534$. Hence $p_{\mathrm{bf}}^{\mathrm{tm}} = 0.283466 \approx 28.3\%$.

The ratio of per-cycle ancilla error probabilities is

$$\frac{p_{\mathrm{bf}}^{\mathrm{tm}}}{p_{\mathrm{bf}}^{\mathrm{flx}}} = \frac{0.283466}{0.021929} = 12.927 \approx 12.9.$$

The ratio of rates is the ratio of lifetimes:

$$\frac{\Gamma_{\mathrm{bf}}^{\mathrm{tm}}}{\Gamma_{\mathrm{bf}}^{\mathrm{flx}}} = \frac{T_1^{\mathrm{bf}}}{T_1^{\mathrm{tm}}} = \frac{451}{30} = 15.033 \approx 15.0.$$

The two ratios differ ($12.9$ vs $15.0$) because the transmon case is not deep in the $\Gamma T \ll 1$ regime at $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$; the probability ratio is the operationally relevant one.

**Uncertainty on $p_{\mathrm{bf}}^{\mathrm{flx}}$ at $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$.** With $f(T) = 1 - e^{-T_{\mathrm{cyc}}/T}$,

$$\frac{\partial f}{\partial T} = \frac{T_{\mathrm{cyc}}}{T^2}\, e^{-T_{\mathrm{cyc}}/T}.$$

Compute each factor: $T^2 = 2.03401 \times 10^{-7}~\mathrm{s}^2$; $T_{\mathrm{cyc}}/T^2 = 10^{-5} / 2.03401 \times 10^{-7} = 49.164~\mathrm{s}^{-1}$; $e^{-T_{\mathrm{cyc}}/T} = 0.978071$. Product: $49.164 \times 0.978071 = 48.086~\mathrm{s}^{-1}$. Then

$$\sigma_p = 48.086 \times 7.0 \times 10^{-5} = 3.366 \times 10^{-3}.$$

So $p_{\mathrm{bf}}^{\mathrm{flx}} = 0.0219 \pm 0.0034$ at $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$.

### 4.4 Steady-state ancilla-induced logical error rate

Let each ancilla flip during a cycle corrupt the logical state with probability $\eta$ (the flip-to-logical conversion factor, a property of the GKP code's finite-energy envelope; input $I_5$, assumption). With $N_{\mathrm{cyc}} = T_{\mathrm{obs}}/T_{\mathrm{cyc}}$ cycles in an observation time $T_{\mathrm{obs}}$, the expected number of corrupting flips is

$$N_{\mathrm{corr}} = \eta \, p_{\mathrm{bf}}(T_{\mathrm{cyc}}) \, N_{\mathrm{cyc}} = \eta \left(1 - e^{-\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}}\right) \frac{T_{\mathrm{obs}}}{T_{\mathrm{cyc}}}.$$

In the limit $T_{\mathrm{cyc}} \to 0$, $1 - e^{-\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}} \to \Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}$, so

$$N_{\mathrm{corr}} \to \eta \, \Gamma_{\mathrm{bf}} T_{\mathrm{cyc}} \cdot \frac{T_{\mathrm{obs}}}{T_{\mathrm{cyc}}} = \eta\, \Gamma_{\mathrm{bf}}\, T_{\mathrm{obs}}.$$

The $T_{\mathrm{cyc}}$ factors cancel exactly. This is the key structural result: in steady state, the ancilla-induced logical error rate is $\eta\,\Gamma_{\mathrm{bf}}$, independent of cycle speed. Faster reset improves the transient behavior and the ability to track oscillator-side errors, but it does not lower the ancilla floor — the floor is set by $\Gamma_{\mathrm{bf}}$ itself.

Setting $\Gamma_L^{(1)} = \eta\,\Gamma_{\mathrm{bf}}$, the ancilla-limited corrected logical lifetime is

$$T_L^{(1)} = \frac{1}{\eta\,\Gamma_{\mathrm{bf}}} = \frac{T_1^{\mathrm{bf}}}{\eta} = \frac{4.51 \times 10^{-4}~\mathrm{s}}{\eta}.$$

For $\eta = 0.1$ (input $I_5$, assumption):

$$T_L^{(1)} = \frac{4.51 \times 10^{-4}}{0.1}~\mathrm{s} = 4.51 \times 10^{-3}~\mathrm{s} = 4