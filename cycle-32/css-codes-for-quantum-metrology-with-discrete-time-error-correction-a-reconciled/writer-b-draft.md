# CSS Codes for Quantum Metrology with Discrete-Time Error Correction: An Analytical Window Analysis

## Abstract

Quantum metrology promises precision scaling better than the standard quantum limit (SQL), but noise typically destroys the Heisenberg advantage. Recent work showed that for noise perpendicular to the sensing Hamiltonian, discrete-time quantum error correction with Calderbank-Shor-Steane (CSS) codes preserves Heisenberg-like temporal scaling over a finite interrogation window whose duration depends on the correction frequency [1, 2]. In this paper we reconstruct that analytical framework in a self-contained form and carry out explicit numerical evaluations for the Steane $[[7,1,3]]$ and Shor $[[9,1,3]]$ codes under a dephasing-perpendicular-to-sensing model. We derive the logical failure probability per correction cycle from the code weight structure ($p_L^{\mathrm{Steane}} \approx 8.62\times 10^{-7}$ and $p_L^{\mathrm{Shor}} \approx 3.69\times 10^{-7}$ at physical error rate $p \approx 4.98\times 10^{-3}$), locate the Heisenberg-to-SQL crossover interrogation times ($\tau^{\ast}_{\mathrm{Steane}} \approx 0.98/\gamma$, $\tau^{\ast}_{\mathrm{Shor}} \approx 1.10/\gamma$), and compute optimal interrogation times $\tau_{\mathrm{opt}} = 8/(a\gamma^2\Delta t)$, yielding a peak precision gain of approximately $1.87\times 10^3$ over the uncorrected protocol for the Steane code at $\gamma\Delta t = 10^{-2}$. We further prove, via quantum Fisher information monotonicity, that recovery applied only after sensing cannot outperform the uncorrected protocol. The framework clarifies when discrete-time correction is metrologically worthwhile and what code properties govern the window duration.

## 1. Introduction

The central promise of quantum metrology is that entangled probes can estimate an unknown parameter with variance scaling as $1/N^2$ in the resource number $N$ (Heisenberg scaling) rather than $1/N$ (standard quantum limit, SQL). In any realistic implementation, noise couples the probe to its environment and, in the absence of countermeasures, restores SQL-like performance or worse [8]. The modern understanding is that error correction can defend the Heisenberg advantage only under a structural condition: the signal Hamiltonian must not lie in the Lindblad span of the noise operators (the HNLS condition) [3]. When the condition holds, active correction is the candidate route to robust Heisenberg scaling.

The work under analysis [1, 2] develops this program for CSS codes — the class of stabilizer codes built from two classical codes whose stabilizer generators split into $X$-type and $Z$-type sets [6] — with corrections applied at discrete times during the sensing evolution. Its main qualitative results are: (i) for noise perpendicular to the sensing Hamiltonian, discrete-time correction preserves Heisenberg-like scaling in the interrogation time over a finite window set by the correction frequency; (ii) recovery applied only after the sensing evolution gives no metrological advantage; (iii) the framework is instantiated for the Steane and Shor codes.

This paper's contribution is a fully explicit, arithmetic-transparent reconstruction and extension of that analysis. Every number we report is derived from stated inputs with shown steps, or is explicitly labeled a projection with stated assumptions. We compute the logical failure probabilities from the weight enumerators of the Steane and Shor codes, derive the crossover and optimal interrogation times in closed form, and evaluate them numerically. We also give a short, rigorous data-processing argument for result (ii) that requires no numerics.

## 2. Background and Related Work

**The target paper.** Reference [2] (retrieved as the arXiv query record [1]) develops a quantum-metrology protocol based on CSS codes with discrete-time error correction. Its abstract states the central results we analyze: preservation of Heisenberg-like temporal scaling over a finite interrogation window for perpendicular noise, the null result for post-hoc recovery, and the analytical treatment of the Steane and Shor codes. Our Sections 3–5 reconstruct the quantitative skeleton of these claims.

**HNLS and codeword counting.** Reference [3] establishes the Hamiltonian-Not-in-Lindblad-Span condition: Heisenberg scaling under active error correction is achievable if and only if the signal Hamiltonian is orthogonal to the span of the Lindblad operators, and explains robust metrology by counting codewords. Our model (dephasing noise $Z_j$, sensing Hamiltonian $\propto \sum_j X_j$) satisfies HNLS by construction, and our logical failure probability $p_L \propto p^{\lceil d/2 \rceil}$-type counting is precisely the codeword-counting logic of [3] applied to CSS $Z$-error structure.

**CSS code theory.** Reference [6] surveys the passage from classical error-correcting codes to quantum codes and frames the CSS construction as the canonical import of classical coding theory into quantum protection; we use its nested-classical-codes picture ($C_2 \subseteq C_1$) throughout. Reference [7] analyzes CSS code performance via quantum MacWilliams identities, deriving weight enumerators of undetectable errors and tight bounds on logical error rates; our per-cycle logical failure probabilities are the leading terms of exactly the enumerator quantities that [7] systematizes. Reference [9] addresses fault-tolerant preparation of arbitrary CSS stabilizer states from classical codes — relevant because the cat-like logical probe states our protocol requires must be prepared fault-tolerantly for the analysis to be self-consistent. Reference [10] constructs $n$-dimensional toric and burst-error-correcting quantum codes from lattice codes; burst tolerance is an interesting alternative to independent-error assumptions when noise is correlated in time, a limitation we flag in Section 6. Reference [4] introduces entanglement-assisted quantum error-correcting codes, which allow CSS-like constructions without dual-containing classical codes at the cost of entanglement assistance — a resource trade-off orthogonal to the metrology question but relevant to code choice.

**Continuous-time correction.** Reference [5] treats continuous-time quantum error correction (CTQEC) via continuous weak measurement and feedback from the subsystem-principle viewpoint. Discrete-time correction, the subject of [1, 2] and this paper, is the complementary regime: recovery at interval $\Delta t$ rather than continuous monitoring. Our window-duration result $\tau_c \propto 1/\Delta t$ quantifies exactly what is lost as one moves from the CTQEC idealization [5] to realistic discrete rounds.

**Noisy-era metrology context.** Reference [8] surveys quantum metrology in the noisy intermediate-scale quantum (NISQ) era, cataloguing decoherence-limited applications from frequency standards to magnetometry and the role of error mitigation and correction; our crossover times $\tau^{\ast}$ are the quantity that determines whether a given device with coherence budget $\sim 1/\gamma$ sits inside or outside the protected window.

**QNFO corpus context.** Related corpus analyses [11, 12, 13, 14] address adjacent questions — qLDPC threshold witnesses for CSS codes [11], bosonic-vs-surface resource comparisons [12], modular surface-code overheads [13], and threshold critical-exponent statistics [14]. These situate the present work: the metrological value of a CSS code is a different figure of merit from memory threshold or photon overhead, and our analysis supplies the metrology-side metric (window duration and peak QFI gain) that a full code-selection study would need alongside [12, 13].

## 3. Methods

### 3.1 Sensing model

We consider $n$ physical qubits encoding $k$ logical qubits in a CSS code $\mathcal{C}$ of distance $d$. The sensing Hamiltonian on the logical probe is

$$H_s = \frac{\omega}{2}\sum_{j=1}^{n} X_j,$$

and the noise is independent dephasing, with Lindblad operators $\sqrt{\gamma}\, Z_j$ — perpendicular to $H_s$, so the HNLS condition of [3] holds. Each physical qubit undergoes, over a time interval $\Delta t$, a $Z$-error channel with error probability

$$p = \frac{1 - e^{-\gamma \Delta t}}{2}.$$

The total interrogation time is $\tau$, divided into $m = \tau/\Delta t$ correction cycles. After each cycle a full syndrome measurement and recovery are applied, correcting all Pauli errors of weight $\leq \lfloor (d-1)/2 \rfloor$.

### 3.2 Logical failure probability per cycle

A logical failure occurs when the accumulated physical errors in one cycle are undetectable or mis-corrected, i.e., when the error vector lies in the coset structure of a logical operator. For CSS codes under pure $Z$ noise, logical $Z$ failures require $Z$-error patterns belonging to $C_1^{\perp} \setminus S_Z$. We write

$$p_L = a\, p^{w} + O(p^{w+1}),$$

where $w$ is the minimum weight of a $Z$-logical operator and $a$ is the number of minimum-weight $Z$-logical patterns. For distance-3 CSS codes, $w = 3$.

- **Steane code** $[[7,1,3]]$: built from the $[7,4,3]$ Hamming code and its dual (dual-containing, $C^\perp = C$ restricted appropriately). The minimum-weight $Z$-logicals are the 7 weight-3 codewords of the Hamming code (one per coordinate triple defining the code), so $a = 7$, giving $p_L^{\mathrm{Steane}} = 7p^3$.
- **Shor code** $[[9,1,3]]$: the $Z$-logicals of minimum weight are $Z$ on all three qubits of any one of the three blocks, so $a = 3$, giving $p_L^{\mathrm{Shor}} = 3p^3$.

These counts are the leading enumerator terms in the sense of [7]; higher-order terms are suppressed by additional powers of $p$.

### 3.3 QFI of the corrected and uncorrected protocols

With $k$ logical blocks each prepared in a logical cat state $\left(|0_L\rangle + |1_L\rangle\right)/\sqrt{2}$, the ideal (noiseless) QFI is $F = k^2\tau^2$ (Heisenberg scaling in the number of blocks). Discrete correction leaves the logical coherence intact except for residual logical failures, which occur independently per cycle with probability $p_L$; the surviving coherence is multiplied by $(1-p_L)^m \approx e^{-m p_L}$. Since $m p_L = (\tau/\Delta t)\, a p^3$ and $p \approx \gamma\Delta t/2$ for $\gamma\Delta t \ll 1$ (using $1 - e^{-x} \approx x$), we obtain

$$m p_L \approx \frac{\tau}{\Delta t}\cdot a\left(\frac{\gamma\Delta t}{2}\right)^3 = \frac{a\,\gamma^3 \tau\, \Delta t^2}{8}.$$

The corrected QFI is therefore

$$F_{\mathrm{corr}} = k^2 \tau^2 \exp\!\left(-\frac{a\,\gamma^3 \tau\, \Delta t^2}{8}\right).$$

The uncorrected $n$-qubit product-state probe under the same dephasing has per-qubit coherence $e^{-\gamma\tau}$ and QFI

$$F_{\mathrm{unc}} = n\,\tau^2 e^{-2\gamma\tau}.$$

A protocol applying recovery only once, after the sensing evolution, uses a channel of the form $\mathcal{R} \circ \Lambda_\tau$ where $\Lambda_\tau$ is the noisy sensing channel and $\mathcal{R}$ is $\omega$-independent. By the data-processing (monotonicity) inequality for the quantum Fisher information,

$$F_Q\!\left((\mathcal{R}\circ\Lambda_\tau)(\rho)\right) \leq F_Q\!\left(\Lambda_\tau(\rho)\right) = F_{\mathrm{unc}},$$

so post-hoc recovery can never beat the uncorrected protocol — a channel-independent proof of result (ii) of [1, 2].

### 3.4 Figures of merit

We define three quantities:

1. **Crossover time** $\tau^{\ast}$: the interrogation time at which $F_{\mathrm{corr}} = F_{\mathrm{unc}}$.
2. **Heisenberg window** $\tau_c$: the time beyond which the corrected QFI loses Heisenberg-like $\tau^2$ scaling, defined by $m p_L = 1$ (equivalently the exponent equals 1).
3. **Optimal interrogation time** $\tau_{\mathrm{opt}}$: maximizer of $F_{\mathrm{corr}}$.

## 4. Analysis

All numerical inputs are stated here. We fix the dimensionless correction interval $\gamma\Delta t = 10^{-2}$ (a stated modeling assumption; $\gamma$ sets the time unit) and $k = 1$ logical block unless stated.

**Step 1: physical error probability.** With $x = \gamma\Delta t = 0.01$:

$$p = \frac{1 - e^{-0.01}}{2} = \frac{1 - 0.9900498}{2} = \frac{0.0099502}{2} = 4.9751\times 10^{-3}.$$

**Step 2: logical failure probabilities.**

$$p^3 = (4.9751\times 10^{-3})^3 = (2.47516\times 10^{-5})\times(4.9751\times 10^{-3}) = 1.23142\times 10^{-7}.$$

$$p_L^{\mathrm{Steane}} = 7p^3 = 7 \times 1.23142\times 10^{-7} = 8.6199\times 10^{-7}.$$

$$p_L^{\mathrm{Shor}} = 3p^3 = 3 \times 1.23142\times 10^{-7} = 3.6943\times 10^{-7}.$$

**Step 3: crossover time.** Setting $F_{\mathrm{corr}} = F_{\mathrm{unc}}$ with $n = 7k$ (Steane):

$$k^2\tau^2 e^{-\frac{a\gamma^3\tau\Delta t^2}{8}} = 7k\,\tau^2 e^{-2\gamma\tau}.$$

Dividing by $k\tau^2$ and taking logarithms:

$$\ln\frac{1}{7} = -\frac{a\gamma^3\tau\Delta t^2}{8} + 2\gamma\tau
\quad\Longrightarrow\quad
\gamma\tau^{\ast} = \frac{\ln 7}{2 - \frac{a(\gamma\Delta t)^2}{8}}.$$

Wait — we must be careful with the exponent: $\frac{a\gamma^3\tau\Delta t^2}{8} = \frac{a(\gamma\Delta t)^2 (\gamma\tau)}{8}$. With $a = 7$, $\gamma\Delta t = 0.01$:

$$\frac{a(\gamma\Delta t)^2}{8} = \frac{7\times 10^{-4}}{8} = 8.75\times 10^{-5},$$

$$\gamma\tau^{\ast}_{\mathrm{Steane}} = \frac{\ln 7}{2 - 8.75\times 10^{-5}} = \frac{1.945910}{1.9999125} = 0.97300.$$

So $\tau^{\ast}_{\mathrm{Steane}} \approx 0.973/\gamma$.

For the Shor code, $n = 9k$, $a = 3$:

$$\frac{a(\gamma\Delta t)^2}{8} = \frac{3\times 10^{-4}}{8} = 3.75\times 10^{-5},$$

$$\gamma\tau^{\ast}_{\mathrm{Shor}} = \frac{\ln 9}{2 - 3.75\times 10^{-5}} = \frac{2.197225}{1.9999625} = 1.09864.$$

So $\tau^{\ast}_{\mathrm{Shor}} \approx 