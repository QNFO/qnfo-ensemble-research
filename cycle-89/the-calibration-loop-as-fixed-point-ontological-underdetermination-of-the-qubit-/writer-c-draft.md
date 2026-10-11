# The Calibration Loop as Fixed Point: Ontological Underdetermination of the Qubit by Its Own Metrology

## Abstract

We formalize the operational loop formed by qubit control and readout as a self-consistent fixed-point problem. In every engineered qubit platform, the drive pulses used for control are calibrated by readout, and the readout is calibrated by control pulses; the physical referent of the qubit label — a collective circuit mode, an electronic level structure, a spin — is never fixed by any single measurement but only by the closure of this calibration chain. We ask whether the qubit's ontology is underdetermined by its own metrology. We construct a minimal formal model of the calibration hierarchy (drive, Rabi calibration, dispersive or state-dependent readout, tomography) as an iterated map, derive its contraction behavior, and show that two distinct physical ontologies — a strict two-level abstraction and a three-level anharmonic extension with leakage amplitude $c$ — yield observationally identical tomographic reconstructions whenever the measurement chain does not resolve the third level, with total-variation distance exactly zero, and distance $|c|^2$ when it does. Using the readout fidelity of $99.991(1)\%$ reported for trapped-ion qubits, we derive the shot budget $N \approx 10^4$ required to break the degeneracy at $|c|^2 = 0.01$. We conclude that circularity is broken only by measurements that reach outside the calibrated computational subspace, and we identify cross-platform consistency as the remaining external constraint.

## 1. Introduction

A working quantum information processor contains qubits whose existence is operationally defined: a control pulse is applied, a readout signal is acquired, and a binary outcome is assigned. The engineering practice treats the qubit as a real physical object — a billiard ball with two states. Yet the practitioner's own calibration procedure tells a subtler story. The drive amplitude is calibrated by observing Rabi oscillations in the readout signal; the readout discriminator is calibrated by preparing states produced by those same drives; tomography validates the whole loop by reconstructing a state using measurements whose calibration itself rests on the loop. The chain is closed. This paper takes that closure seriously as a formal problem: if the only access to the qubit is through the loop, what fixes the qubit's physical referent — the claim that the excitation lives in a specific collective mode, a specific electronic transition, a specific spin?

The conjecture we formalize is that the referent is underdetermined: distinct physical ontologies can be observationally identical under the full calibrated measurement set. This is not a skeptical paradox but a precise metrological statement with a precise resolution condition. We model the calibration hierarchy as a fixed-point problem, prove (in a minimal model) that the fixed point exists and is reached by contraction, and then exhibit two ontologies that share the same fixed point. We then derive what breaks the degeneracy: any measurement that resolves degrees of freedom outside the computational subspace, or any consistency requirement imposed across platforms whose loop closures differ.

Our contributions are: (i) a formalization of the calibration chain as an iterated map with an explicit contraction bound; (ii) a two-model comparison showing exact observational equivalence of a two-level and a three-level ontology under subspace-restricted measurements, with the distinguishability computed as a function of the leakage amplitude; (iii) a shot-budget derivation, anchored to the readout fidelity reported in the trapped-ion literature, quantifying when the degeneracy becomes empirically resolvable; and (iv) a discussion of which structural features of real platforms — cross-platform comparison, Hamiltonian-level constraints — can pin the referent to a substrate.

## 2. Background and Related Work

The literature relevant to this paper falls into three groups: self-referential reasoning, high-fidelity readout, and control-theoretic treatments of systems whose models are approximations of richer dynamics.

**Self-referential diagnosis.** The closest structural analogue to our problem appears in adaptive fault diagnosis [1], which studies the problem of determining which processors in a remote location are reliable by asking them "Yes or No" questions, where the processors are of three types: those that always tell the truth, those that always lie, and those that sometimes tell the truth and sometimes lie. The entry states that using self-referential reasoning, along with earlier techniques, one can regard both the truth-tellers and the liars as reliable. This is exactly the logical move our calibration loop performs: a readout channel whose "honesty" is in question is calibrated by sources whose calibration depends on the readout, and the fixed point legitimizes the whole chain at once. The supplied summary of [1] gives no further technical detail, but the structural parallel — reliability of witnesses established by a closed chain of testimony — is the core of our Section 3.

**Readout as the anchor of the loop.** The trapped-ion readout demonstration of [2] is our principal quantitative anchor. The work demonstrates single-shot qubit readout with fidelity sufficient for fault-tolerant quantum computation, for two types of qubit stored in single trapped calcium ions; for an optical qubit stored in the $(4S_{1/2}, 3D_{5/2})$ levels of $^{40}\mathrm{Ca}^+$ it achieves $99.991(1)\%$ average readout fidelity in one million trials using time-resolved photon counting, and an adaptive measurement technique allows $99.99\%$ fidelity. Two features matter for us. First, the readout is photonic: the measured medium (scattered photons) is visibly distinct from the qubit carrier (electronic levels), which is precisely the kind of referent-resolving structure whose absence in other platforms motivates our underdetermination question. Second, the quoted fidelities supply the error scale we use in Section 4 to convert an ontology-distinguishing signal into a shot budget.

**Control of distributed and approximate models.** A second group of works treats control of systems whose working model is a truncation of a richer physical reality — the same epistemic situation as the two-level abstraction of a transmon. The flexible-wing boundary control paper [3] models a nonhomogeneous flexible wing under unsteady aerodynamic loads as a distributed parameter system of two coupled partial differential equations, actuated at the tip by flaps, and first investigates well-posedness of the underlying Cauchy problem before constructing the boundary control law. The methodological pattern — prove the truncated model well-posed, then control it — mirrors our treatment of the computational subspace as a well-posed abstraction of a larger Hilbert space. The delay-boundary-control paper [6] treats exponential input-to-state stabilization of diagonal infinite-dimensional systems with uncertain, time-varying input delays, using a constant-delay predictor feedback controller designed on a truncated finite-dimensional model; the truncation there is explicitly a modeling choice whose consequences for stability must be bounded, exactly as leakage out of the two-level abstraction must be bounded in our model. The finite-state approximation work [7] approximates discrete-time plants with finite-valued sensors and actuators by deterministic finite memory systems for certified-by-design controller synthesis, proposing a control-oriented notion of finite state approximation; its framing — the approximation is built for the controller, not derived from the physics — is the control-theoretic statement of our claim that the qubit ontology is defined by the control loop rather than discovered by it.

**Hierarchical and constrained control.** The airborne wind energy system of [4] implements a hierarchical control structure addressing all operational phases — take-off, transition to power generation, pumping energy generation cycles, transition to hovering, and landing — with control design at all hierarchical levels. This is the architectural template for a calibration hierarchy: distinct phases (drive calibration, readout calibration, tomography) each with their own control law, coupled sequentially. The input-constrained control barrier function framework of [5] introduces the ICCBF notion for synthesizing safety-critical controllers for nonlinear control-affine systems with input constraints, identifying a subset of the safe set and constructing a controller rendering it forward invariant, with the feedback controller given as the solution to a quadratic program. We borrow the forward-invariance idea in Section 3: the computational subspace plays the role of the safe set, and the calibration loop is the controller that must keep the operational description within it.

**Quantum-compliant control formulations.** Finally, the network epidemic control work [8] builds on susceptible-infected-susceptible and susceptible-infected-removed discrete-time network models, encapsulating a control action (mobility bans via link removal), and formulates the control problem in a quantum-compliant way. Its relevance is methodological: it demonstrates that quantum formalism can be applied to non-quantum control loops, supporting our view that the quantum-classical distinction is not what generates the self-referential structure — the closure of the calibration chain is.

**QNFO corpus.** The QNFO document "No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems" [9] is a pedagogical bridge between qubit ontology critique and working physics, explaining what control pulses actually manipulate and what readout measures across superconducting transmon, trapped-ion, and spin qubit platforms, and including an electrical seesaw analogy and a self-referential metrology formalization. Our Sections 3–4 can be read as a formalization of the program sketched there. Two further QNFO entries, "Stabilization of Gottesman-Kitaev-Preskill States" [10] and "A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation" [11], have no supplied summary text; we therefore cite them only as corpus context and draw no substantive claims from them, noting this limitation explicitly in Section 6.

## 3. Methods

### 3.1 The calibration loop as an iterated map

Let $\mathcal{H}_{\mathrm{sub}}$ denote the computational subspace (dimension $d=2$) and $\mathcal{H}_{\mathrm{full}}$ the full Hilbert space of the physical carrier. The calibration chain consists of stages indexed $j = 1, \dots, J$: drive calibration, Rabi calibration, readout discriminator calibration, and tomographic validation. Each stage $j$ has a parameter vector $\theta_j \in \mathbb{R}^{n_j}$ and a validation statistic $r_j$ computed from data produced using the current settings of all other stages. We collect $\Theta = (\theta_1, \dots, \theta_J)$ and write the update abstractly as

$$\Theta_{k+1} = F(\Theta_k), \qquad F: \mathbb{R}^n \to \mathbb{R}^n.$$

A calibrated apparatus is a fixed point $\Theta_\star$ with $F(\Theta_\star) = \Theta_\star$. The self-referential character is that $F$'s definition at every stage involves measurements taken through the apparatus being calibrated — the situation of [1], where the reliability of the witnesses is established by the testimony chain itself.

Near a fixed point, write $\Theta_k = \Theta_\star + \delta_k$. For a scalar gain model of one stage (the case relevant to drive-amplitude calibration), the update is

$$x_{k+1} = x_k + g\,(r_k - r_\star),$$

where $x_k$ is the drive parameter, $g$ is the loop gain, $r_k$ is the observed statistic, and $r_\star$ the target. Linearizing the statistic, $r_k - r_\star = s\,(x_k - x_\star)$ with sensitivity $s$, gives the error recursion

$$e_{k+1} = (1 - g\,s)\,e_k, \qquad e_k \equiv x_k - x_\star.$$

The map is a contraction whenever $|1 - g\,s| < 1$, and then

$$e_k = e_0\,|1 - g\,s|^k.$$

This is the formal content of "the loop converges": the fixed point is attractive, and the calibration chain is self-consistent — but note that nothing in the contraction argument refers to the physical substrate. The fixed point is a property of the loop, not of $\mathcal{H}_{\mathrm{full}}$.

### 3.2 Two ontologies, one loop

We now formalize the underdetermination conjecture. Define two models:

- **Model A (two-level abstraction):** $\mathcal{H}_A = \mathrm{span}\{|0\rangle, |1\rangle\}$, with the calibrated POVM $\{\Pi_0^{(A)}, \Pi_1^{(A)}\}$ acting on $\mathcal{H}_A$.
- **Model B (anharmonic three-level carrier):** $\mathcal{H}_B = \mathrm{span}\{|0\rangle, |1\rangle, |2\rangle\}$, with the same calibrated POVM extended so that $\Pi_1^{(B)}$ projects onto the span of $\{|1\rangle, |2\rangle\}$ — i.e., the readout does not resolve the third level, which is the generic situation when the readout transition addresses only the $|0\rangle \leftrightarrow |1\rangle$ distinction.

A control pulse prepared with residual leakage amplitude $c$ produces, in Model B, the state

$$|\psi_B\rangle = \sqrt{1 - |c|^2}\,|1\rangle + c\,|2\rangle,$$

while Model A assigns the pure state $|1\rangle$. The outcome distributions are

$$p_A(1) = 1, \qquad p_B(1) = \langle \psi_B | \Pi_1^{(B)} | \psi_B \rangle = (1 - |c|^2) + |c|^2 = 1.$$

The total-variation distance is

$$D_{\mathrm{TV}}(p_A, p_B) = \frac{1}{2}\sum_m |p_A(m) - p_B(m)| = 0.$$

Both ontologies are observationally identical under the full calibrated measurement set whenever the measurement chain does not resolve level $|2\rangle$. The tomographic reconstruction — a function only of the outcome distributions — is the same object in both cases. This is the precise sense in which the qubit ontology is underdetermined by its metrology: the loop fixes the *operational* qubit, and the operational qubit is compatible with multiple substrates.

### 3.3 Breaking the degeneracy

If the measurement chain is extended so that it resolves $|2\rangle$ (a leakage-resolving measurement, with $\Pi_1$ projecting on $|1\rangle$ alone and a third outcome for $|2\rangle$), the distributions become

$$p_A(1) = 1, \qquad p_B(1) = 1 - |c|^2, \qquad p_B(2) = |c|^2,$$

and

$$D_{\mathrm{TV}}(p_A, p_B) = \frac{1}{2}\left(|c|^2 + |c|^2\right) = |c|^2.$$

The degeneracy is broken exactly to the extent that the measurement reaches outside the computational subspace. With $N$ independent shots, the statistical resolution of a distribution difference of order $D_{\mathrm{TV}}$ requires roughly $N \sim D_{\mathrm{TV}}^{-2}$ shots (the standard binomial scaling, stated here as a modeling assumption for the projection in Section 5). The external anchor for the achievable per-shot error is the readout fidelity of [2].

### 3.4 Cross-platform constraint

A second route out of circularity is structural rather than statistical: two platforms whose calibration loops close differently (photonic readout as in [2], circuit readout, spin resonance) cannot both be saved by a single shared ontology unless that ontology is substrate-specific. Requiring one consistent assignment of "what is excited" across platforms with different loop topologies is a constraint no single loop can generate — the analogue, in our setting, of the multi-witness consistency that lets the self-referential diagnosis of [1] classify its processors.

## 4. Analysis

We now carry out the explicit derivations. Every input number is stated with its source; every arithmetic step is shown.

**Input 1 (from [2]):** average readout fidelity $f_{\mathrm{ro}} = 99.991\% = 0.99991$ for the optical qubit in $^{40}\mathrm{Ca}^+$, over $N_{\mathrm{trials}} = 10^6$ trials.

**Input 2 (from [2]):** the adaptive measurement technique allows fidelity $f_{\mathrm{ad}} = 99.99\% = 0.99999$.

**Input 3 (model assumption of this paper, Section 3.2):** leakage amplitude $|c| = 0.1$, i.e., leakage probability $|c|^2 = 0.01$.

**Input 4 (model assumption of this paper, Section 3.1):** loop gain–sensitivity product $g\,s = 0.5$, giving contraction factor $|1 - g\,s| = 0.5$; initial calibration error $e_0 = 0.1$ in units of the drive parameter.

**Derivation 1: readout error scale.** The per-shot readout error probability is

$$\varepsilon_{\mathrm{ro}} = 1 - f_{\mathrm{ro}} = 1 - 0.99991 = 9 \times 10^{-5}.$$

Over $N_{\mathrm{trials}} = 10^6$ trials, the expected number of misidentifications is

$$\mu = N_{\mathrm{trials}} \times \varepsilon_{\mathrm{ro}} = 10^6 \times 9 \times 10^{-5} = 90.$$

This is consistent with the reported precision of $99.991(1)\%$: one standard error on $f_{\mathrm{ro}}$ over $10^6$ trials is $\sqrt{f_{\mathrm{ro}}(1-f_{\mathrm{ro}})/N_{\mathrm{trials}}} = \sqrt{0.99991 \times 9\times10^{-5} / 10^6} = \sqrt{9.0\times10^{-11}} \approx 9.49\times10^{-6}$, i.e., about $10^{-6}$ in fidelity units, matching the "(1)" in the last quoted digit.

**Derivation 2: adaptive versus time-resolved error ratio.** The adaptive-technique error is

$$\varepsilon_{\mathrm{ad}} = 1 - f_{\mathrm{ad}} = 1 - 0.99999 = 1 \times 10^{-5}.$$

The ratio of adaptive to time-resolved error is

$$\frac{\varepsilon_{\mathrm{ad}}}{\varepsilon_{\mathrm{ro}}} = \frac{1\times10^{-5}}{9\times10^{-5}} = \frac{1}{9} \approx 0.1111.$$

The adaptive technique reduces the error to roughly one-ninth of the time-resolved value, per the two fidelities quoted in [2].

**Derivation 3: calibration-loop convergence.** With contraction factor $|1 - g\,s| = 0.5$ and $e_0 = 0.1$, the error after $k$ iterations is $e_k = 0.1 \times 0.5^k$. To drive the calibration error below the readout error scale $\varepsilon_{\mathrm{ro}} = 9\times10^{-5}$ (the natural threshold: calibration error should not exceed the noise floor it is calibrated against), we require

$$0.1 \times 0.5^k \le 9\times10^{-5} \quad\Longrightarrow\quad 0.5^k \le 9\times10^{-4}.$$

Taking logarithms:

$$k \ge \frac{\ln(9\times10^{-4})}{\ln(0.5)} = \frac{\ln 9 + \ln 10^{-3}}{-\ln 2} = \frac{2.19722 - 6.90776}{-0.69315} = \frac{-4.71054}{-0.69315} \approx 6.796.$$

Since $k$ must be an integer, $k = 7$ iterations suffice. Check: $e_7 = 0.1 \times 0.5^7 = 0.1 \times 0.0078125 = 7.8125\times10^{-4}$. This exceeds $9\times10^{-5}$ — so we recheck. $0.5^7 = 7.8125\times10^{-3}$, so $e_7 = 7.8125\times10^{-4} > 9\times10^{-5}$: the inequality is not yet satisfied at $k=7$. Continue: $e_8 = 0.1 \times 0.5^8 = 3.90625\times10^{-4}$, still $> 9\times10^{-5}$. $e_9 = 0.1\times0.5^9 = 1.953125\times10^{-4}$, still $> 9\times10^{-5}$. $e_{10} = 0.1\times0.5^{10} = 9.765625\times10^{-5}$, still marginally $> 9\times10^{-5}$. $e_{11} = 0.1\times0.5^{11} = 4.8828125\times10^{-5} < 9\times10^{-5}$. The logarithmic bound of $6.796$ was computed against the wrong threshold direction; the correct requirement is $0.5^k \le 9\times10^{-4}$, and indeed $0.5^{10} = 9.7656\times10^{-4} > 9\times10^{-4}$ while $0.5^{11} = 4.8828\times10^{-4} \le 9\times10^{-4}$. Hence

$$k_{\min} = 11 \text{ iterations},$$

and the logarithmic estimate should read $k \ge \ln(9\times10^{-4})/\ln(0.5)$ with the ceiling taken after verifying the discrete inequality; the discrete check gives $k_{\min} = 11$. (The discrepancy arises because $6.796$ rounds to $7$, but $0.5^7 = 7.8\times10^{-3} \gg 9\times10^{-4}$; the correct continuous solution is $k \ge 10.11$, since $\ln(9\times10^{-4}/0.1) = \ln(9\times10^{-3}) = -4.71054$ and $-4.71054/\ln 0.5 = 6.796$ — we note that $\ln(9\times10^{-3}) = \ln 9 - \ln 1000 \cdot$ ... recompute directly: $9\times10^{-3}$, $\ln(9\times10^{-3}) = \ln 9 + \ln(10^{-3}) = 2.19722 - 6.90776 = -4.71054$; but the threshold on $0.5^k$ is $9\times10^{-4}$, so $k \ge \ln(9\times10^{-4})/\ln 0.5 = (\ln 9 - 9.21034)/(-0.69315) = (2.19722 - 9.21034)/(-0.69315) = (-7.01312)/(-0.69315) = 10.118$. The earlier use of $\ln(10^{-3}) = -6.90776$ was the error; $\ln(10^{-4}) = -9.21034$.) Therefore

$$k_{\min} = \lceil 10.118 \rceil = 11,$$

in agreement with the discrete check $e_{11} = 4.88\times10^{-5} < 9\times10^{-5} < e_{10} = 9.77\times10^{-5}$.

**Derivation 4: ontological distinguishability.** From Section 3.3, with $|c|^2 = 0.01$ (Input 3):

$$D_{\mathrm{TV}}(p_A, p_B) = |c|^2 = 0.01 \quad \text{(leakage-resolving measurement)},$$
$$D_{\mathrm{TV}}(p_A, p_B) = 0 \quad \text{(subspace-restricted measurement)}.$$

**Derivation 5: shot budget.** To resolve a distribution difference $\Delta p = |c|^2 = 0.01$ at the level of a single outcome probability with one-standard-error significance, the binomial standard error $\sqrt{p(1-p)/N}$ must be $\le \Delta p$. Taking the conservative $p \approx 1/2$ bound, $\sqrt{1/(4N)} \le 0.01$ gives

$$N \ge \frac{1}{4 \times (0.01)^2} = \frac{1}{4\times10^{-4}} = 2500 \text{ shots}.$$

For a three-sigma requirement, $3\sqrt{1/(4N)} \le 0.01$ gives

$$N \ge \frac{9}{4\times10^{-4}} = 22500 \text{ shots}.$$

Both figures are far below the $10^6$ trials already demonstrated in [2], so the shot budget is not the obstacle; the obstacle is whether the measurement chain *implements* a leakage-resolving observable at all.

**Derivation 6: leakage-resolving measurement versus readout noise floor.** A leakage signal of $|c|^2 = 0.01$ must exceed the readout error scale $\varepsilon_{\mathrm{ro}} = 9\times10^{-5}$ to be visible above the noise floor of a [2]-class readout. The margin is

$$\frac{|c|^2}{\varepsilon_{\mathrm{ro}}} = \frac{0.01}{9\times10^{-5}} = \frac{10^{-2}}{9\times10^{-5}} = 111.1\overline{1} \approx 111.$$

The leakage signal is about $111$ times larger than the per-shot readout error probability, so a leakage-resolving extension of a [2]-class readout would see the three-level ontology clearly, provided the extension exists.

## 5. Results

We report only quantities derived in Section 4, plus clearly labeled projections.

1. **Readout error scale (computed, from [2]).** Per-shot error $\varepsilon_{\mathrm{ro}} = 9\times10^{-5}$; expected misidentifications in $10^6$ trials: $\mu = 90$; the reported precision "(1)" is consistent with a one-standard-error of $\approx 9.5\times10^{-6}$ in fidelity units.

2. **Adaptive-technique improvement (computed, from [2]).** $\varepsilon_{\mathrm{ad}} = 1\times10^{-5}$, a factor $\approx 0.111$ (one-ninth) of the time-resolved error.

3. **Calibration-loop convergence (computed, under stated model assumptions $g\,s = 0.5$, $e_0 = 0.1$).** The loop reaches calibration error below the readout noise floor $\varepsilon_{\mathrm{ro}}$ after $k_{\min} = 11$ iterations ($e_{11} = 4.88\times10^{-5}$).

4. **Ontological degeneracy (computed, under stated model assumptions).** Under subspace-restricted measurements, $D_{\mathrm{TV}} = 0$ exactly: the two-level and three-level ontologies are observationally identical, and tomography cannot distinguish them. Under a leakage-resolving measurement with $|c| = 0.1$, $D_{\mathrm{TV}} = 0.01$.

5. **Shot budget (computed, binomial scaling assumption).** $N \ge 2500$ shots for one-sigma resolution of $\Delta p = 0.01$; $N \ge 22500$ shots for three-sigma.

6. **Signal-to-noise margin (computed).** $|c|^2/\varepsilon_{\mathrm{ro}} \approx 111$ for a [2]-class readout extended to resolve leakage.

7. **Projection (labeled).** If a platform's full calibrated measurement set is confined to the computational subspace — the generic case for dispersive readout used only for qubit-state discrimination — then we project that *no* finite shot budget distinguishes the two ontologies on that platform alone, because $D_{\mathrm{TV}} = 0$ identically. The uncertainty in this projection is zero given the model; its empirical risk lies in whether real readout chains are truly subspace-confined, which is a platform-specific question we do not settle here.

## 6. Discussion

**What the model claims and what it does not.** The formal result — exact observational equivalence of two ontologies under subspace-restricted measurements — is a statement about a minimal model, not a theorem about transmons. Real readout chains are rarely perfectly subspace-confined: dispersive readout in circuit QED, for instance, acquires its signal from a mode whose frequency shift depends on the full level structure, so traces of the third level can leak into the discriminator. Our claim is therefore best read as: the *calibrated, tomographically validated* measurement set is what underdetermines the ontology, and any residual substrate sensitivity that has not been explicitly calibrated into the loop does not count as evidence for one ontology over another.

**Limitations.** First, the contraction analysis (Derivation 3) assumes a scalar, linearized stage with constant gain; real calibration hierarchies have coupled stages, and the joint map $F$ need not be a contraction, so $k_{\min} = 11$ is a model-bound illustration, not a platform prediction. Second, the leakage amplitude $|c| = 0.1$ is an assumption of the paper, not a measured value; the distinguishability scales as $|c|^2$, so a platform with much smaller leakage is harder to resolve, and the shot budget scales as $|c|^{-4}$ (since $N \sim \Delta p^{-2}$ with $\Delta p = |c|^2$). Third, the binomial shot-budget scaling assumes independent shots and a known sign of the deviation; systematic errors in the leakage-resolving extension could dominate. Fourth, the bibliography available to this paper is skewed toward classical control theory [3]–[8]; the entries [3], [4], [5], [6], [7], [8] supply structural analogies (truncation, hierarchy, forward invariance, certification) but no quantum-specific results, and the QNFO entries [10] and [11] carry no supplied summary text at all, so we could extract no substantive claims from them — a genuine limitation of the literature base for this preprint.

**Failure modes and falsification.** The central claim — underdetermination of the qubit ontology by the calibration loop — would be falsified by a demonstration that the *standard, unextended* calibrated measurement set of some platform already distinguishes the two-level from the three-level description, i.e., that $D_{\mathrm{TV}} > 0$ for subspace-restricted tomography in a real chain. Conversely, our claim that extension breaks the degeneracy would be falsified if a leakage-res