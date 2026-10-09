# Decoherence as the Ultimate Consequence of Linear Accumulation

## Abstract

We argue that quantum decoherence, usually treated as a primitive postulate of open-system dynamics, can be derived as the inevitable long-time consequence of a single structural assumption: that small environmental perturbations accumulate linearly in the phase space of a system-environment composite. We formalize this claim with a discrete kick model in which each system-environment interaction deposits an independent phase perturbation of characteristic magnitude $\sigma_\phi$. Linear accumulation of the perturbation variance yields an exponential decay of coherence, $C(t) = \exp(-N\sigma_\phi^2/2)$, with a fully explicit derivation and worked numerical examples: for $\sigma_\phi = 10^{-3}\,\mathrm{rad}$ delivered at a rate of $10^4\,\mathrm{s^{-1}}$, coherence falls to $1/e$ after $2\times10^6$ kicks, i.e. $t_{1/e} = 200\,\mathrm{s}$. We contrast this with coherent (systematic) accumulation, which grows quadratically in the kick number and is therefore qualitatively more dangerous but structurally fragile. We situate the result within the QNFO research program on deterministic relaxation and fault-tolerant lifecycles, and we draw supporting analogies from detector radiation damage, precision spectroscopy, accelerator accumulation, and cumulative error in astronomical distance ladders. The framework makes falsifiable predictions about the scaling of decoherence with interaction rate and kick magnitude, and we state the conditions under which it would be refuted.

## 1. Introduction

Decoherence is the process by which a quantum system loses the phase relations between components of its state superposition owing to entanglement with an environment. In textbook treatments it is imported as an axiom: one writes down a Lindblad master equation, postulates a Markovian bath, and reads off a decay constant $T_2$. What is usually not asked is why the decay is exponential in the first place, and why the relevant accumulation of environmental influence is linear rather than quadratic in the number of interactions.

This paper takes the opposite route. We assume only that each elementary system-environment interaction deposits a small, approximately independent perturbation, and that these perturbations add linearly in the sense that the *variance* of the accumulated perturbation grows linearly with the number of interactions $N$. From this single structural assumption we derive exponential decoherence as a theorem, with a computable rate. Decoherence is thus not a primitive but the ultimate, long-time consequence of linear accumulation: any system coupled to an environment that satisfies the linearity-of-variance condition must decohere, regardless of the microscopic details of the coupling.

The claim matters for three reasons. First, it unifies decoherence with other cumulative-degradation phenomena in physics and engineering, from radiation damage in silicon pixel detectors to systematic-error budgets in cosmological distance ladders. Second, it gives a sharp falsification criterion: if one could engineer an environment whose perturbations accumulate sub-linearly in variance, the resulting coherence time would exceed the linear-accumulation prediction in a quantifiable way. Third, it connects to the QNFO program's pre-registered falsification of deterministic measurement-triggered relaxation [10]: our framework predicts that relaxation statistics depend only on the accumulated perturbation distribution, not on any trigger semantics of measurement, which is precisely the hypothesis under test in [10].

The paper is organized as follows. Section 2 reviews related work. Section 3 defines the kick-accumulation model. Section 4 contains the derivations with all arithmetic shown. Section 5 reports the computed results. Section 6 discusses limitations and failure modes, and Section 7 concludes.

## 2. Background and Related Work

The bibliography available for this preprint is drawn from adjacent fields rather than from the decoherence literature proper; we use each work for the structural feature it exemplifies, and we flag this limitation explicitly in Section 6.

The ATLAS Pixel Project [2] describes segmented silicon trackers with $40\,\mathrm{MHz}$ radiation-hard readout electronics at the interaction point of the LHC. The relevance is direct: radiation damage in silicon is a paradigm of *linear accumulation*, where displacement damage accumulates particle by particle, and the detector's degradation over its lifetime is the integral of many individually negligible events — exactly the regime our model formalizes. The follow-up ATLAS Planar Pixel Sensor R&D work [6] studies the same problem under the High Luminosity LHC, where a factor of $5$–$10$ increase in peak luminosity proportionally increases the rate of damaging interactions; this is a concrete instance of our prediction that degradation time scales inversely with interaction rate (Section 4).

The ALPHA antihydrogen experiment [3] pursues precision spectroscopy of trapped antihydrogen to test CPT symmetry, and the companion paper [5] discusses the particle-physics reach of such measurements. Both works illustrate the engineering *opposite* of linear accumulation: the entire experimental design is aimed at suppressing environmental perturbation rates so that the residual accumulation of phase-disturbing interactions is slow enough for spectroscopy. They thus serve as a benchmark for how strongly decoherence times respond to reductions in the kick rate $\Gamma_{\mathrm{kick}}$.

The Araucaria Project volume [1] documents two decades of work on the cosmic distance scale. The distance ladder is a chain of calibrations in which fractional errors accumulate step by step; the project's methodological emphasis on controlling each link is a macroscopic analogue of managing the kick distribution $\{\delta\phi_k\}$ in our model, and motivates our distinction between independent (linear-variance) and systematic (quadratic) error accumulation.

Wheatland-style self-consistent nonlinear force-free field reconstruction from weighted boundary conditions [4] addresses a structurally similar problem: boundary data inconsistent with the model assumption are iteratively relaxed toward consistency. We borrow this logic methodologically — our model treats the "inconsistency" between unitary ideal dynamics and environmental perturbation as something to be absorbed by an accumulation law rather than by an ad hoc bath postulate.

The optics study of a Muon Accumulator Ring based on FFA cells [7] concerns the accumulation of many muon passes in a ring while preserving low emittance. Emittance growth in such a ring is a beam-physics instance of variance accumulation: each pass through the lattice contributes a small perturbation, and the design goal is to keep the accumulated variance below a tolerance — the same inequality we solve for quantum coherence in Section 4.

Finally, the pedagogic simulation of sustainability in complex projects [8] studies long-horizon depletion of resources under continuously acting drivers. While far from quantum physics, it supplies the conceptual vocabulary of slow, compounding, individually negligible depletions that dominate only in the long-time limit — the qualitative heart of our thesis. Within the QNFO corpus, the Alpha Pi Project [9] provides the archival context for this line of work, the pre-registered falsification of deterministic measurement-triggered relaxation [10] supplies the experimental hypothesis our model must be consistent with, Monistic Reality [11] frames the ontological position that measurement is not a primitive, and the Lifecycle of a Fault-Tolerant Quantum Computer [12] treats the engineering consequence: fault-tolerance thresholds exist precisely because physical error rates per gate must sit below a critical value, which our model identifies with the per-kick magnitude $\sigma_\phi$.

## 3. Methods

### 3.1 The kick-accumulation model

Consider a two-level system with basis $\{|0\rangle, |1\rangle\}$ interacting sequentially with $N$ environmental degrees of freedom (modes), one per elementary interaction. The joint unitary for the $k$-th interaction is

$$U_k = \exp\left(-i\,\frac{\delta\phi_k}{2}\,\sigma_z \otimes \mathbb{1}_{E}\right),$$

where $\sigma_z$ is the Pauli-$z$ operator, $\mathbb{1}_{E}$ the environment identity, and $\delta\phi_k$ the phase kick delivered by the $k$-th mode. The system's reduced density matrix after tracing out the environment has off-diagonal (coherence) element

$$\rho_{01}^{(N)} = \rho_{01}^{(0)} \prod_{k=1}^{N} \langle e^{i\delta\phi_k}\rangle_E,$$

where $\langle\cdot\rangle_E$ denotes the average over environmental states. We assume the kicks are independent, identically distributed, zero-mean random variables with variance

$$\sigma_\phi^2 = \langle \delta\phi_k^2\rangle_E - \langle\delta\phi_k\rangle_E^2,$$

and that each kick is small, $|\delta\phi_k| \ll 1\,\mathrm{rad}$.

### 3.2 The linear-accumulation postulate

The single structural assumption of this paper is:

**Postulate (linear accumulation).** The variance of the *sum* of $N$ independent kicks equals the sum of the variances:

$$\mathrm{Var}\!\left(\sum_{k=1}^{N}\delta\phi_k\right) = \sum_{k=1}^{N}\mathrm{Var}(\delta\phi_k) = N\sigma_\phi^2.$$

This is the standard additivity of variance for independent variables; "linear" refers to the growth of the accumulated variance in $N$, in contrast to the quadratic growth $\propto N^2$ that would occur if the kicks were perfectly correlated (systematic).

### 3.3 Kick rate and physical time

If kicks arrive at a rate $\Gamma_{\mathrm{kick}}$ (kicks per second), then after wall-clock time $t$ the number of accumulated kicks is

$$N(t) = \Gamma_{\mathrm{kick}}\, t.$$

All time-domain statements below follow from substituting $N(t)$ into the coherence expression derived in Section 4.

## 4. Analysis

### 4.1 Derivation of the coherence decay law

For a zero-mean kick with $|\delta\phi_k| \ll 1$, expand the environmental average to second order:

$$\langle e^{i\delta\phi_k}\rangle_E = \left\langle 1 + i\delta\phi_k - \frac{\delta\phi_k^2}{2} + \mathcal{O}(\delta\phi_k^3)\right\rangle_E = 1 - \frac{\sigma_\phi^2}{2} + \mathcal{O}(\sigma_\phi^3),$$

using $\langle\delta\phi_k\rangle_E = 0$ and $\langle\delta\phi_k^2\rangle_E = \sigma_\phi^2$. The product over $N$ kicks is therefore

$$\prod_{k=1}^{N}\langle e^{i\delta\phi_k}\rangle_E = \left(1 - \frac{\sigma_\phi^2}{2}\right)^{N}.$$

Taking the logarithm and using $\ln(1 - x) = -x + \mathcal{O}(x^2)$ with $x = \sigma_\phi^2/2$:

$$\ln C_N = N \ln\!\left(1 - \frac{\sigma_\phi^2}{2}\right) \approx -\frac{N\sigma_\phi^2}{2},$$

so the coherence factor is

$$C_N \equiv \left|\frac{\rho_{01}^{(N)}}{\rho_{01}^{(0)}}\right| = \exp\!\left(-\frac{N\sigma_\phi^2}{2}\right).$$

Substituting $N(t) = \Gamma_{\mathrm{kick}}\,t$:

$$C(t) = \exp\!\left(-\frac{\Gamma_{\mathrm{kick}}\,\sigma_\phi^2}{2}\, t\right) \equiv e^{-t/T_2}, \qquad T_2 = \frac{2}{\Gamma_{\mathrm{kick}}\,\sigma_\phi^2}.$$

This is the main analytic result: the exponential decoherence law and the dephasing time $T_2$ follow from linear accumulation of kick variance alone.

### 4.2 Worked numerical example (fully explicit)

**Inputs.** (i) Kick magnitude $\sigma_\phi = 10^{-3}\,\mathrm{rad}$ — a representative small-perturbation value chosen so that the expansion in Section 4.1 is valid ($\sigma_\phi^2/2 = 5\times10^{-7} \ll 1$); (ii) kick rate $\Gamma_{\mathrm{kick}} = 10^{4}\,\mathrm{s^{-1}}$ — chosen to sit in the range of environmental interaction rates for a mesoscopic solid-state-like system; these are illustrative model parameters, not measured values.

**Step 1.** Variance per kick: $\sigma_\phi^2 = (10^{-3})^2 = 10^{-6}\,\mathrm{rad^2}$.

**Step 2.** Accumulated variance after $N$ kicks: $N\sigma_\phi^2 = N \times 10^{-6}\,\mathrm{rad^2}$.

**Step 3.** Coherence after $N = 10^6$ kicks:

$$C_{10^6} = \exp\!\left(-\frac{10^6 \times 10^{-6}}{2}\right) = \exp(-0.5) \approx 0.6065.$$

**Step 4.** Elapsed time for $10^6$ kicks: $t = N/\Gamma_{\mathrm{kick}} = 10^6 / 10^{4}\,\mathrm{s^{-1}} = 100\,\mathrm{s}$.

**Step 5.** The $1/e$ coherence time: set $N\sigma_\phi^2/2 = 1$, giving

$$N_{1/e} = \frac{2}{\sigma_\phi^2} = \frac{2}{10^{-6}} = 2\times10^{6}\ \text{kicks},$$

$$t_{1/e} = \frac{N_{1/e}}{\Gamma_{\mathrm{kick}}} = \frac{2\times10^{6}}{10^{4}\,\mathrm{s^{-1}}} = 200\,\mathrm{s},$$

and equivalently $T_2 = 2/(\Gamma_{\mathrm{kick}}\sigma_\phi^2) = 2/(10^{4}\times10^{-6})\,\mathrm{s} = 200\,\mathrm{s}$, consistent with Step 4.

**Step 6.** Rate scaling. If the kick rate is reduced tenfold to $\Gamma_{\mathrm{kick}}' = 10^{3}\,\mathrm{s^{-1}}$ (the strategy exemplified by the trapping and suppression engineering of [3], [5]), then

$$T_2' = \frac{2}{10^{3}\times10^{-6}}\,\mathrm{s} = 2000\,\mathrm{s},$$

a tenfold improvement — decoherence time scales exactly inversely with kick rate, the same proportionality by which a $5$–$10\times$ luminosity increase in [6] proportionally shortens detector degradation times.

### 4.3 Contrast with quadratic (systematic) accumulation

If instead the kicks are perfectly correlated — the same systematic phase error $\delta\phi_{\mathrm{sys}}$ repeated every kick — the accumulated phase is $N\delta\phi_{\mathrm{sys}}$ and the coherence factor becomes

$$C_N^{\mathrm{sys}} = \cos\!\left(\frac{N\delta\phi_{\mathrm{sys}}}{2}\right),$$

which does not decay exponentially but oscillates, and whose envelope degradation scales as $(N\delta\phi_{\mathrm{sys}})^2$ in fidelity terms — quadratic in $N$. For the same per-kick magnitude $\delta\phi_{\mathrm{sys}} = 10^{-3}\,\mathrm{rad}$, the phase reaches $1\,\mathrm{rad}$ after only

$$N_{\mathrm{sys}} = \frac{1}{10^{-3}} = 10^{3}\ \text{kicks}, \qquad t_{\mathrm{sys}} = \frac{10^{3}}{10^{4}\,\mathrm{s^{-1}}} = 0.1\,\mathrm{s},$$

i.e. $2000\times$ faster degradation than the independent-kick case ($200\,\mathrm{s}$). This is the precise sense in which systematic errors are more dangerous than stochastic ones, and why experimental programs such as the distance-ladder work of [1] and the self-consistency procedures of [4] invest heavily in identifying and removing correlated error components.

### 4.4 Connection to fault-tolerance thresholds

The Lifecycle of a Fault-Tolerant Quantum Computer [12] frames fault tolerance around a threshold physical error rate $p_{\mathrm{th}}$ below which concatenated error correction suppresses logical errors. In our model the per-kick coherence loss is

$$p_{\mathrm{kick}} = 1 - e^{-\sigma_\phi^2/2} \approx \frac{\sigma_\phi^2}{2}.$$

For $\sigma_\phi = 10^{-3}\,\mathrm{rad}$: $p_{\mathrm{kick}} \approx 5\times10^{-7}$ per kick. If one kick corresponds to one gate epoch, the requirement $p_{\mathrm{kick}} < p_{\mathrm{th}}$ becomes a bound on the admissible kick magnitude; for a commonly quoted threshold order of magnitude $p_{\mathrm{th}} \sim 10^{-4}$ (a projection, not a measurement, used here only for scale), the model requires $\sigma_\phi < \sqrt{2p_{\mathrm{th}}} = \sqrt{2\times10^{-4}} \approx 1.41\times10^{-2}\,\mathrm{rad}$, comfortably satisfied by the illustrative parameter. The structural point is that the threshold condition is a condition on the *per-interaction* perturbation, exactly as linear accumulation predicts.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs ($\sigma_\phi = 10^{-3}\,\mathrm{rad}$, $\Gamma_{\mathrm{kick}} = 10^{4}\,\mathrm{s^{-1}}$); none are empirical measurements.

- **R1 (coherence law).** $C(t) = \exp(-\Gamma_{\mathrm{kick}}\sigma_\phi^2 t/2)$, with $T_2 = 2/(\Gamma_{\mathrm{kick}}\sigma_\phi^2)$ (Section 4.1).
- **R2 (illustrative coherence).** After $N = 10^6$ kicks ($t = 100\,\mathrm{s}$), $C = e^{-0.5} \approx 0.6065$ (Section 4.2, Step 3).
- **R3 ($1/e$ time).** $N_{1/e} = 2\times10^{6}$ kicks and $t_{1/e} = T_2 = 200\,\mathrm{s}$ (Section 4.2, Step 5).
- **R4 (rate scaling).** Reducing $\Gamma_{\mathrm{kick}}$ from $10^{4}\,\mathrm{s^{-1}}$ to $10^{3}\,\mathrm{s^{-1}}$ extends $T_2$ from $200\,\mathrm{s}$ to $2000\,\mathrm{s}$: exact inverse proportionality (Section 4.2, Step 6).
- **R5 (systematic-error penalty).** Perfectly correlated kicks of the same magnitude degrade coherence on a timescale $t_{\mathrm{sys}} = 0.1\,\mathrm{s}$, a factor of $2000$ faster than the stochastic case (Section 4.3).
- **R6 (per-kick error).** $p_{\mathrm{kick}} \approx \sigma_\phi^2/2 = 5\times10^{-7}$ per kick for the illustrative parameters (Section 4.4).

**Projection (labeled as such).** If the kick model applies to a fault-tolerant architecture with threshold $p_{\mathrm{th}} \sim 10^{-4}$ (order-of-magnitude assumption from the standard threshold folklore, not derived here), the model tolerates kick magnitudes up to $\sigma_\phi \lesssim 1.41\times10^{-2}\,\mathrm{rad}$. Uncertainty: this projection inherits at least an order-of-magnitude uncertainty from $p_{\mathrm{th}}$ itself and is valid only within the small-kick expansion $\sigma_\phi^2/2 \ll 1$.

## 6. Discussion

**Limitations.** The model assumes independent, identically distributed, zero-mean kicks. Real environments exhibit correlations (colored noise), non-Gaussian tails, and non-Markovian memory, any of which can break the variance-additivity postulate and modify the decay from exponential to Gaussian or stretched-exponential form. The small-kick expansion requires $\sigma_\phi^2/2 \ll 1$; for strong individual kicks the product formula must be evaluated exactly and the exponential law can fail at short times. The numerical parameters are illustrative, not measured; the *scaling* results (R1, R4, R5) are the robust outputs, not the absolute times.

**Failure modes and falsification.** The thesis — decoherence as the ultimate consequence of linear accumulation — would be falsified if (i) a physical system exhibited coherence times growing faster than $1/\Gamma_{\mathrm{kick}}$ as the kick rate is varied at fixed $\sigma_\phi$, contradicting R4; or (ii) an environment could be engineered whose perturbation variance accumulates sub-linearly in $N$ without being merely a correlated (quadratic) case. The pre-registered falsification program of [10] is directly relevant: if deterministic measurement-triggered relaxation were confirmed, relaxation statistics would depend on measurement semantics rather than on the accumulated perturbation distribution, breaking the model's central claim that only the kick statistics matter. Conversely, confirmation of the null hypothesis in [10] would be consistent with, though not proof of, the accumulation picture.

**Arguing against ourselves.** A critic may object that deriving $e^{-t/T_2}$ from variance additivity is elementary and well known in the dephasing literature, so the paper's contribution is framing rather than physics. We concede the derivation's simplicity but argue the framing has content: it demotes decoherence from postulate to corollary, and it makes the ontological position of [11] — that measurement is not a primitive — operationally precise, since "measurement" becomes just a kick-accumulation event with an effectively irreversible variance ledger. A second objection: the analogy corpus ([1]–[8]) is drawn from adjacent fields, and analogies do not constitute evidence. This is a genuine limitation; the bibliography available for this preprint contains no primary decoherence literature, and the paper should be read as a framework proposal whose empirical tests must come from dedicated experiments of the kind pre-registered in [10] and from threshold analyses in the style of [12]. A third objection: the quadratic case (Section 4.3) shows that accumulation is not always benign, so "linear accumulation" is not the universal rule. We agree — the paper's claim is that *when* accumulation is linear in variance, decoherence follows necessarily; the correlated case is a distinct regime that dynamical-decoupling and calibration techniques target precisely because it is structurally fragile and correctable.

**Open questions.** What is the minimum environmental correlation structure that preserves variance linearity? How does the kick picture extend to non-commuting perturbation operators, where kicks do not simply add as phases? Can the $2000\times$ systematic-vs-stochastic penalty (R5) be turned into a design rule for the architectures of [12]?

## 7. Conclusion

We have shown that exponential decoherence follows from a single structural assumption — linear accumulation of independent perturbation variance — via an explicit derivation with fully shown arithmetic. For illustrative parameters ($\sigma_\phi = 10^{-3}\,\mathrm{rad}$, $\Gamma_{\mathrm{kick}} = 10^{4}\,\mathrm{s^{-1}}$), the model yields $T_2 = 200\,\mathrm{s}$, exact inverse scaling of $T_2$ with kick rate, a $2000\times$ penalty for correlated versus stochastic kicks, and a per-kick error of $5\times10^{-7}$. Decoherence is thereby recast as the ultimate, unavoidable consequence of linear accumulation, with falsifiable scaling predictions and a direct connection to the pre-registered falsification program of the QNFO corpus.

## References

[1] arXiv:2305.17247v1 | The Araucaria Project: Improving the cosmic distance scale

[2] arXiv:hep-ex/9903035v1 | The ATLAS Pixel Project

[3] arXiv:1104.4661v1 | Alpha Antihydrogen Experiment

[4] arXiv:2004.12510v1 | Self-consistent Nonlinear Force-free Field Reconstruction from Weighted Boundary Conditions

[5] arXiv:0805.4082v1 | Particle Physics Aspects of Antihydrogen Studies with ALPHA at CERN

[6] arXiv:1109.5944v1 | Recent progress of the ATLAS Planar Pixel Sensor R&D Project

[7] arXiv:2011.11701v1 | Optics studies of a Muon Accumulator Ring based on FFA cells

[8] arXiv:2104.04068v2 | Embedding Sustainability in Complex Projects: A Pedagogic Practice Simulation Approach

[9] QNFO: Alpha Pi Project | DOI 10.5281/zenodo.19479493

[10] QNFO: A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation | DOI 10.5281/zenodo.22144215

[11] QNFO: Monistic Reality | DOI 10.5281/zenodo.17410796

[12] QNFO: Lifecycle of a Fault-Tolerant Quantum Computer | DOI 10.5281/zenodo.18000790