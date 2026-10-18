# Differential Einthoven-Style Readout: Common-Mode Noise Cancellation in Dispersive Qubit Measurement

## Abstract

Single-shot dispersive readout of superconducting qubits is limited by noise that the measurement chain adds after the qubit-state-dependent resonator shift has been imprinted: amplifier gain drift, thermal fluctuations on the output line, and stray coupling appear largely identically on a single measurement channel and cannot be separated from the qubit signal by any post-processing of that channel alone. Readout error at this level is a dominant contributor to the cycle error budget of quantum error correction, where surface-code layouts demand physical-to-logical qubit ratios near 1000:1. We propose a balanced, electrocardiography-inspired readout: the same qubit is probed simultaneously through two phase-opposed resonator channels, and the decision variable is the difference of the two recorded quadrature streams, so that the qubit signal adds while chain-common noise cancels. We derive the signal-to-noise ratio and single-shot fidelity of the difference channel against single-ended boxcar integration for a Gaussian noise model with a common-mode component of relative strength $r$. For $r = 0.5$ and unit separation, the differential channel raises the amplitude SNR from $1.789$ to $2.828$ (a factor of $1.581$), reduces the single-shot error probability from $3.72 \times 10^{-2}$ to $2.34 \times 10^{-3}$, and reduces the estimated logical error rate of a $[[3,1,2]]$ repetition code from $4.15 \times 10^{-3}$ to $1.64 \times 10^{-5}$. We map the gain against channel imbalance and show cancellation survives gain mismatch up to $\delta \approx 3.5$ at $r = 0.5$. The result converts a proven biomedical noise-rejection principle into a quantitative design rule for redundant qubit readout.

## 1. Introduction

Every cycle of a quantum error correction experiment begins with the same operation: measure one or many qubits quickly and accurately, and feed the outcome to a decoder. In superconducting platforms this measurement is dispersive readout, in which a microwave resonator shifts its resonance frequency by an amount set by the qubit state, and the reflected or transmitted probe tone is amplified and integrated to decide between the two states. The fidelity of this decision enters the error-correction cycle multiplicatively: a surface-code machine performing millions of cycles per second multiplies readout errors across data qubits, ancilla qubits, and rounds, so that even percent-level readout error consumes a large fraction of the total logical error budget. Resource estimates for surface codes reach physical-to-logical qubit ratios of roughly 1000:1 [8], and every improvement in per-qubit readout fidelity directly relaxes the code distance, the cycle time, or both that a given logical error target requires.

The noise that limits the decision is not only the irreducible photon-shot noise of the probe, which no hardware trick can remove, but also technical noise added downstream of the resonator: gain drift of the cryogenic and room-temperature amplifiers, thermal fluctuations propagating down the output line, and stray coupling of other control tones into the measurement band. These contributions appear on the recorded quadrature stream with the same statistical character as the qubit signal itself, and a single-ended receiver — one resonator, one amplifier chain, one integrated complex number — has no way to tell them apart. The standard countermeasures are calibration and stabilization: repeated renormalization of the IQ discriminator, temperature stabilization, and careful filtering. Each helps, but each attacks the noise after it has already been mixed into the only available signal channel.

Electrocardiography solved an isomorphic problem a century ago. The cardiac signal of interest is tens of microvolts; the common-mode interference picked up by the body from mains wiring and muscle activity is millivolts, two orders of magnitude larger. The Einthoven limb-lead configuration works because the heart signal appears differentially between electrode pairs while the interference appears largely identically on both, and a differential amplifier rejects the common component by the amplifier's common-mode rejection ratio. The same architectural idea — extract the quantity of interest as a difference between two matched channels that share their noise — appears in gravitational-wave interferometry, where the Michelson is locked to a dark fringe so that all differential signal appears at the output port while common laser intensity and phase fluctuations are reflected back toward the laser [1], and in electromagnetic-compatibility engineering, where lattice networks are used to cancel parasitic common-mode conduction paths, verified by $S$-parameter measurement on prototype circuits [5]. What has not been done is to apply this balanced-differential architecture systematically to dispersive qubit readout, where the "electrodes" are two resonator channels coupled to the same qubit and the "differential amplifier" is a complex subtraction of the two recorded quadrature streams.

If the principle transfers, the payoff is concrete: a readout chain whose decision fidelity is set by the uncorrelated part of the noise alone, with amplifier drift and thermal common-mode fluctuations rejected by construction rather than by calibration. That would change the design target for cryogenic amplification (less stringent gain stability), the calibration cadence in operating quantum processors, and the hardware-fidelity trade-off in redundant readout layouts.

This paper derives the performance of such a differential readout channel from an explicit noise model and quantifies the trade-offs. Our contributions are:

- A two-channel noise model for dispersive readout with phase-opposed signal encoding and a common-mode noise component, and a closed-form derivation of the amplitude SNR of the difference channel versus single-ended integration, giving the gain factor $G_{\mathrm{SNR}} = \sqrt{2(1 + r^{2})}$ in amplitude SNR (Section 4).
- A numerical evaluation of single-shot fidelity for a worked parameter set ($r = 0.5$), showing the single-shot error probability falling from $3.72 \times 10^{-2}$ to $2.34 \times 10^{-3}$, with full arithmetic (Section 4).
- An imbalance analysis showing the differential gain survives gain mismatch, with break-even mismatch $\delta \approx 3.46$ at $r = 0.5$ (Section 4).
- A projection of logical error rate for a $[[3,1,2]]$ repetition code under the derived physical error rates, giving a reduction from $4.15 \times 10^{-3}$ to $1.64 \times 10^{-5}$ under stated independence assumptions (Section 4).
- A discussion of how the differential architecture relates to and combines with existing readout-enhancement strategies, and of the failure modes that bound the gain (Sections 5 and 6).

## 2. Background and Related Work

Dispersive readout and its noise budget. In the dispersive regime the qubit-resonator Hamiltonian contains the term $\chi \sigma_{z} a^{\dagger} a$, so the resonator frequency shifts by a qubit-state-dependent amount and the probe tone acquires a qubit-state-dependent phase [2]. This is the mechanism our differential scheme modifies at the level of the readout chain, not at the level of the qubit-resonator coupling; [2] studies the complementary direction, engineering the coupling itself. There, a mixed coupling of two quadrature pairs suppresses the dispersive shift while retaining a nonzero Kerr shift, so that the photon shot-noise dephasing rate scales as $\bar{n}_{\mathrm{th}}^{2}$ and is suppressed when $\bar{n}_{\mathrm{th}} \ll 1$; the authors demonstrate the required coupling terms in Cooper-pair-transistor and fluxonium-molecule circuits by tuning the imbalance of capacitive and Josephson energies [2]. Our scheme is orthogonal: it leaves the dispersive interaction untouched and instead restructures how the output signal and the chain noise are combined into a decision variable.

Photon-shot noise and dephasing trade-offs. Residual noise photons in the readout resonator dephase the qubit at a rate proportional to the average noise-photon number, $\Gamma_{\phi}^{\mathrm{noise}} = \frac{\kappa_{\mathrm{eff}} \chi_{qc}^{2}}{\kappa_{\mathrm{eff}}^{2} + \chi_{qc}^{2}} \bar{n}_{\mathrm{noise}}$, where $\kappa_{\mathrm{eff}}$ is the resonator linewidth and $\chi_{qc}$ the full dispersive shift [7]. Because the resonator is overcoupled to the waveguide, this dephasing depends only on the noise spectral density in the waveguide and not on the resonator linewidth or the intrinsic bath temperature [7]. The nonlinear Purcell filter of [7] addresses this by automatically reducing the effective linewidth during the readout pulse, decoupling readout speed from photon-noise sensitivity; its authors note it is compatible with large-scale integration because it requires no additional control signals [7]. Our differential chain attacks a different noise term — the technical, chain-common noise added after the resonator — and is compatible with such filter innovations, since the two act on different links of the measurement chain.

Quantum-limited amplification and correlated readout modes. The closest existing readout-enhancement strategy to a two-channel architecture is the two-mode-squeezing scheme of [6]: the readout signal is amplified by a Josephson mixer producing signal and idler modes, and the two output modes are coherently combined so that only the combined quadrature carrying the qubit information is amplified. The measured power-SNR ratio of the combined mode over single-mode phase-preserving readout exceeds unity for all practical gains $G > 1$ dB and added noise $N_{\mathrm{sys}} > 0.5$, and reaches $1.66$ at $G = 8$ dB and $N_{\mathrm{sys}} = 50$ [6]. The authors attribute the gain to quantum correlations between signal and idler modes boosting the combined quadrature more than the accompanying rise in output-chain noise [6]. Our scheme obtains an analogous combining gain from classical channel symmetry rather than from quantum correlations: the two resonator channels are driven in phase opposition so that subtraction adds the signal, and the common-mode technical noise cancels. The two mechanisms are composable in principle, since the differential subtraction can be applied to the combined mode of [6] as well as to a single mode.

Common-mode rejection in interferometry. The gravitational-wave community has long engineered the same signal/noise geometry we propose. In a Fabry-Perot Michelson interferometer the instrument is controlled to hold the anti-symmetric port on a dark fringe, so that all differential signal from the gravitational wave appears at the extraction port while the incident beam, with its intensity and phase fluctuations, is reflected back toward the laser [1]. Analytical calculations of laser noise in resonant-sideband-extraction interferometers show, however, that at high optical power laser noise couples to the detection port not only optically but also by driving mirror motions, and that laser phase noise re-injected through the signal-recycling mirror via arm-length mismatch can exceed quantum noise below roughly 10–20 Hz [1]. The lesson we import is double-edged: differential extraction is powerful, but residual asymmetry between the two arms — the interferometric analogue of channel imbalance in our scheme — converts common noise into differential noise. Our imbalance analysis in Section 4 quantifies exactly this leakage channel for the qubit readout case.

Common-mode noise cancellation in circuits. In the electronics domain, a generalized lattice-network technique cancels the equivalent series inductance of capacitors and is extended to common-mode noise reduction using a common-mode choke; the vertically asymmetric cancellation circuit satisfies the cancellation condition by adjusting a single inductance, and both the asymmetric circuit and its common-mode extension were verified by two-port $S$-parameter measurements on breadboard prototypes with $1\,\mu\mathrm{F}$ capacitors and nanocrystalline-core chokes [5]. This demonstrates that balanced cancellation structures can be tuned with a single adjustable element and validated with standard microwave characterization — directly relevant to how a two-resonator differential readout chain would be trimmed and verified in the laboratory.

Defining noise against a signal. Conceptually, our entire construction rests on the standard statistical definition in which the signal of an experiment is the mean $\langle A \rangle = \sum_{i=1}^{N} P(a_{i}) a_{i}$ of the outcome distribution and noise is the difference between the measured outcome and that mean [3]. The differential readout does not change the qubit's outcome distribution; it changes which part of the deviation-from-mean is correlated between two recordings of the same experiment, and subtraction removes precisely the correlated part.

Noise as a physical resource and a confounder. That measurement outcomes are statistical, with only $P(a_{i})$ accessible, is the shared starting point of classical and quantum noise theory [3]. At the interpretive extreme, [4] argues that there remains considerable evidence that Bell-type inequalities can be violated even by classical systems, so that experiments apparently showing quantum behavior may in some cases be mimicked by noise processes. We cite [4] not for its foundational thesis but as a caution for the simulation methodology of this paper: a Monte Carlo study of readout fidelity must distinguish genuine quantum state-preparation and back-action effects from classical noise statistics, and our model in Section 3 does so by placing all qubit physics in the deterministic dispersive shift and all noise in explicitly classical, chain-referred random variables.

The cardiological analogy. The specific inspiration for this work — transplanting Einthoven's toolkit into quantum measurement — is articulated in [8], which catalogs the cardiological techniques of differential amplification, vector analysis, matched filtering, ensemble averaging, crosstalk mitigation, impulse-response deconvolution, and closed-loop feedback as directly translatable to quantum readout, while arguing that such methods improve fidelity only with diminishing returns because the deeper problem is claimed to be intrinsic to the continuous framework of standard quantum mechanics [8]. Our paper takes the first, practical half of that program seriously and gives it quantitative content: we do not address the ontological claims of [8], but we derive exactly how much fidelity the differential-amplification member of that toolkit buys in a concrete dispersive-readout model, and where its returns diminish (Section 4, imbalance and crosstalk analysis).

## 3. Methods

### 3.1 Readout model

We consider a single qubit dispersively coupled to two readout resonators, $r_{A}$ and $r_{B}$, each with the standard Hamiltonian term $\chi \sigma_{z} a^{\dagger} a$ as in conventional dispersive readout [2]. Each resonator is probed with a microwave tone and its output is amplified by its own amplifier chain and recorded as a complex quadrature stream. The two probe tones are driven in phase opposition: the qubit-state-dependent phase shift acquired by the probe appears with opposite sign in the two channels. This is the qubit-readout analogue of driving the two arms of a Michelson so that the differential quantity appears at the dark port [1].

Let $s \in \mathbb{R}$ denote the per-channel signal amplitude of the qubit-state-dependent component along the decision quadrature, with sign set by the qubit state and by the drive phase convention. We take the two qubit states to produce per-channel decision-quadrature values of $+s$ and $-s$, so that the centroid separation on a single channel is $\Delta = 2s$. Each recorded sample in channel $i \in \{A, B\}$ is modeled as

$$x_{i} = \pm s + c + n_{i},$$

where:

- $c$ is the common-mode noise, identical in both channels: amplifier gain drift, thermal fluctuations common to the shared output line and readout electronics, and stray coupling that enters both paths equally. We model it as a zero-mean Gaussian random variable with variance $\sigma_{c}^{2}$.
- $n_{i}$ is the channel-private noise: amplifier added noise, photon shot noise referred to the channel, and uncorrelated crosstalk. We model $n_{A}, n_{B}$ as independent zero-mean Gaussians with equal variance $\sigma_{n}^{2}$.

All noise is classical and chain-referred; the qubit contributes only the deterministic shift $\pm s$ during the integration window. This follows the signal/noise decomposition in which the signal is the mean of the outcome distribution and noise is the deviation of the measured outcome from that mean [3].

### 3.2 Decision variables

Single-ended (standard) readout uses one channel, say $x_{A}$, integrated over the pulse and thresholded at the midpoint. The differential readout uses

$$d = x_{A} - x_{B} = \pm 2s + n_{A} - n_{B},$$

in which $c$ cancels exactly because it enters both channels with identical sign while the signal enters with opposite sign.

### 3.3 Simulation methodology

We do not rely on simulation for the headline results; all are derived analytically in Section 4 with explicit arithmetic. The model is, however, simple enough to verify by direct Monte Carlo sampling of the Gaussian variables above, and we state the sampling procedure so the derivations can be checked: draw $c$, $n_{A}$, $n_{B}$ from $\mathcal{N}(0, \sigma^{2})$ with the variances of Section 3.1, form $x_{A}$, $x_{B}$, $d$, threshold each at zero, and count misclassifications over $10^{6}$ trials. The analytic and sampled error rates should agree to within the binomial standard error, which for $10^{6}$ trials and $p \approx 0.037$ is $\sqrt{p(1-p)/10^{6}} \approx 1.9 \times 10^{-4}$. As a caution imported from [4], such a Monte Carlo verifies only the classical noise statistics of the model; it contains no quantum dynamics, and any claim about genuine quantum back-action would require a master-equation treatment beyond this paper's scope.

### 3.4 Code-level projection

To translate single-shot fidelity into a code-level quantity, we use the $[[3,1,2]]$ repetition code, which encodes one logical qubit in three physical qubits and corrects any single physical-qubit error. Under the assumption of independent, identical physical error probability $p$, the dominant logical error channel is two simultaneous physical errors, giving the standard leading-order estimate $p_{L} \approx \binom{3}{2} p^{2} = 3p^{2}$. The independence assumption is stated explicitly as a projection assumption; correlated readout errors would modify the combinatorial factor.

## 4. Analysis

### 4.1 SNR of the single-ended channel

The single-ended decision variable is $x_{A} = \pm s + c + n_{A}$. Its noise variance is the sum of the independent contributions:

$$\sigma_{\mathrm{SE}}^{2} = \sigma_{c}^{2} + \sigma_{n}^{2}.$$

The amplitude SNR (centroid offset over noise standard deviation) is

$$\mathrm{SNR}_{\mathrm{SE}} = \frac{s}{\sqrt{\sigma_{c}^{2} + \sigma_{n}^{2}}}.$$

Define the common-mode ratio $r \equiv \sigma_{c}/\sigma_{n}$. Then

$$\mathrm{SNR}_{\mathrm{SE}} = \frac{s}{\sigma_{n}\sqrt{1 + r^{2}}}.$$

### 4.2 SNR of the differential channel

The differential decision variable is $d = \pm 2s + n_{A} - n_{B}$. The common-mode term has cancelled exactly. The variance of $n_{A} - n_{B}$ for independent, equal-variance channels is

$$\mathrm{Var}(n_{A} - n_{B}) = \sigma_{n}^{2} + \sigma_{n}^{2} = 2\sigma_{n}^{2},$$

so

$$\mathrm{SNR}_{\mathrm{diff}} = \frac{2s}{\sqrt{2}\,\sigma_{n}} = \sqrt{2}\,\frac{s}{\sigma_{n}}.$$

### 4.3 SNR gain

The ratio of amplitude SNRs is

$$G_{\mathrm{SNR}} = \frac{\mathrm{SNR}_{\mathrm{diff}}}{\mathrm{SNR}_{\mathrm{SE}}} = \frac{\sqrt{2}\, s/\sigma_{n}}{s/(\sigma_{n}\sqrt{1 + r^{2}})} = \sqrt{2(1 + r^{2})}.$$

This is the central analytic result. Two limiting cases:

- $r = 0$ (no common-mode noise): $G_{\mathrm{SNR}} = \sqrt{2} \approx 1.414$. The differential channel still wins because it coherently combines two signal copies while adding only $\sqrt{2}$ times the private noise — the same combining benefit that drives the two-mode-squeezed readout gain of [6], obtained there from quantum correlations with a reported maximum power-SNR ratio of $1.66$, which corresponds to an amplitude-SNR ratio of $\sqrt{1.66} \approx 1.288$.
- $r \to \infty$ (common-mode dominated): $G_{\mathrm{SNR}} \to \sqrt{2}\, r$, growing without bound; the differential channel removes the entire dominant noise term.

### 4.4 Worked numerical example

We now fix a parameter set and carry every arithmetic step. Take the private noise as the unit, $\sigma_{n} = 1$, a moderate common-mode level $r = 0.5$ so that $\sigma_{c} = 0.5$, and a per-channel signal amplitude $s = 2$ (centroid separation $\Delta = 4$ on a single channel).

Single-ended channel:

$$\sigma_{\mathrm{SE}} = \sqrt{\sigma_{c}^{2} + \sigma_{n}^{2}} = \sqrt{0.5^{2} + 1^{2}} = \sqrt{0.25 + 1} = \sqrt{1.25} = 1.11803.$$

$$\mathrm{SNR}_{\mathrm{SE}} = \frac{s}{\sigma_{\mathrm{SE}}} = \frac{2}{1.11803} = 1.78885.$$

Differential channel:

$$\sigma_{\mathrm{diff}} = \sqrt{2}\,\sigma_{n} = \sqrt{2} = 1.41421.$$

$$\mathrm{SNR}_{\mathrm{diff}} = \frac{2s}{\sigma_{\mathrm{diff}}} = \frac{4}{1.41421} = 2.82843.$$

Gain:

$$G_{\mathrm{SNR}} = \frac{2.82843}{1.78885} = 1.58114,$$

which matches the closed form $\sqrt{2(1 + r^{2})} = \sqrt{2(1 + 0.25)} = \sqrt{2.5} = 1.58114$. ✓

### 4.5 Single-shot fidelity

With Gaussian centroids at $\pm s$ (single-ended) or $\pm 2s$ (differential) and a threshold at zero, the single-shot error probability is the Gaussian tail beyond the threshold:

$$p = \frac{1}{2}\,\mathrm{erfc}\!\left(\frac{\mathrm{SNR}}{\sqrt{2}}\right),$$

and the fidelity is $F = 1 - p$.

Single-ended:

$$\frac{\mathrm{SNR}_{\mathrm{SE}}}{\sqrt{2}} = \frac{1.78885}{1.41421} = 1.26491.$$

$$p_{\mathrm{SE}} = \tfrac{1}{2}\,\mathrm{erfc}(1.26491).$$

Using $\mathrm{erfc}(1.26491)$: $\mathrm{erfc}(1.25) = 0.07710$ and $\mathrm{erfc}(1.30) = 0.06599$; linear interpolation at $1.26491$ gives $\mathrm{erfc} \approx 0.07710 - \frac{0.01491}{0.05}(0.07710 - 0.06599) = 0.07710 - 0.2982 \times 0.01111 = 0.07710 - 0.00331 = 0.07379$. Hence

$$p_{\mathrm{SE}} = 0.03690 \approx 3.69 \times 10^{-2}, \qquad F_{\mathrm{SE}} \approx 0.9631.$$

Differential:

$$\frac{\mathrm{SNR}_{\mathrm{diff}}}{\sqrt{2}} = \frac{2.82843}{1.41421} = 2.00000.$$

$$p_{\mathrm{diff}} = \tfrac{1}{2}\,\mathrm{erfc}(2) = \tfrac{1}{2} \times 0.0046773 = 0.0023387 \approx 2.34 \times 10^{-3}, \qquad F_{\mathrm{diff}} \approx 0.99766.$$

Error-probability ratio:

$$\frac{p_{\mathrm{SE}}}{p_{\mathrm{diff}}} = \frac{0.03690}{0.0023387} = 15.78.$$

So at $r = 0.5$ the differential channel reduces the single-shot error probability by a factor of about $15.8$, raising the fidelity from $0.963$ to $0.998$.

### 4.6 Gain map over common-mode strength

Evaluating $G_{\mathrm{SNR}} = \sqrt{2(1+r^{2})}$ and the corresponding error probabilities over a range of $r$, with $\sigma_n = 1$, $s = 2$ as above:

| $r$ | $\sigma_c$ | $\mathrm{SNR}_{\mathrm{SE}}$ | $\mathrm{SNR}_{\mathrm{diff}}$ | $G_{\mathrm{SNR}}$ | $p_{\mathrm{SE}}$ | $p_{\mathrm{diff}}$ |
|---|---|---|---|---|---|---|
| 0.0 | 0.0 | 2.00000 | 2.82843 | 1.41421 | $2.34\times10^{-2}$ | $2.34\times10^{-3}$ |
| 0.5 | 0.5 | 1.78885 | 2.82843 | 1.58114 | $3.69\times10^{-2}$ | $2.34\times10^{-3}$ |
| 1.0 | 1.0 | 1.41421 | 2.82843 | 2.00000 | $7.87\times10^{-2}$ | $2.34\times10^{-3}$ |
| 2.0 | 2.0 | 0.89443 | 2.82843 | 3.16228 | $1.87\times10^{-1}$ | $2.34\times10^{-3}$ |

Arithmetic checks for the table: at $r=1$, $\sigma_{\mathrm{SE}} = \sqrt{2} = 1.41421$, $\mathrm{SNR}_{\mathrm{SE}} = 2/1.41421 = 1.41421$, $G = 