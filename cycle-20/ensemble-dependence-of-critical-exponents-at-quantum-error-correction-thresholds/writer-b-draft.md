# Ensemble Dependence of Critical Exponents at Quantum Error Correction Thresholds: A Scaling Analysis

## Abstract

Thermodynamic reasoning holds that the choice of statistical ensemble—microcanonical, canonical, or grand-canonical—should not alter physical observables in the thermodynamic limit. A recent preprint on ensemble dependence at a quantum error correction (QEC) threshold [1, 2] reports that this expectation fails for critical exponents: in a simplified random-unitary encoding model, generic channels and quantum trajectories yield different exponents for fidelity and magic (non-Clifford resource content) at the threshold, and even the existence of the transition is ensemble-dependent. This paper provides an independent analytical treatment of that claim. We formalize the ensemble distinction, reconstruct the scaling ansatz underlying the reported exponent saturation of an information-theoretic bound, and derive concrete, fully explicit numerical consequences: the fidelity gap between ensembles at fixed distance from threshold, the sample sizes required to statistically resolve two candidate exponents, and the crossover scale below which the ensembles are indistinguishable. We find that resolving exponent separation of β = 1 versus β = 2 at Δp = 10⁻³ from threshold requires approximately 4.0 × 10⁴ independent samples under stated noise assumptions, a figure that grows as Δp⁻⁴ and thus rapidly becomes prohibitive. We discuss limitations, failure modes, and falsifiable predictions.

## 1. Introduction

Quantum error correction protects quantum information from decoherence by encoding logical states into a subspace of a larger Hilbert space designed so that common errors move the state into an orthogonal, detectable error space [10]. A central empirical fact about QEC architectures is the existence of a threshold: below some physical error rate p_c, increasing the code size suppresses logical error rates; above it, encoding fails. Near p_c, observables such as fidelity and magic—the non-Clifford resource content of a state, i.e., its distance from the set of states preparable by stabilizer (Clifford-group) circuits—behave as power laws, F(p) ≈ F_c − A(p_c − p)^β, defining a critical exponent β.

In equilibrium thermodynamics, ensemble equivalence is a cornerstone: microcanonical, canonical, and grand-canonical descriptions coincide for generic short-range systems in the thermodynamic limit. The preprint under examination [1, 2] argues that QEC thresholds violate this expectation. Using a simplified model—single-step encoding and decoding by a random unitary—it reports (i) different exponents β for generic channels versus quantum trajectories (unravelings of the same channel into stochastic pure-state evolutions conditioned on measurement records), (ii) saturation of a recently derived information-theoretic bound by Feldman et al. (2026), extended from grand-canonical to canonical and newly defined intermediate ensembles, and (iii) ensemble-dependent existence of the transition itself.

This paper does not reproduce the simulations of [1, 2]; no empirical data are invented here. Instead, we take the reported qualitative claims as hypotheses and ask: what are their analytical consequences, what arithmetic do they force, and what would confirm or falsify them? Our contributions are:

1. A precise formulation of the ensemble distinction in the QEC context, connecting it to the known ensemble-dependence phenomenon in disordered spin chains [3].
2. Explicit scaling derivations for two candidate exponent assignments, including full arithmetic for fidelity gaps, statistical resolution requirements, and crossover scales.
3. A discussion of why ensemble dependence matters operationally: threshold estimates from finite-size, finite-sample experiments may inherit an ensemble label that the experimenter did not choose deliberately.

## 2. Background and Related Work

**Ensemble dependence in statistical physics.** The phenomenon closest to the claim of [1, 2] is ensemble dependence of critical exponents in disordered systems. Ref. [3] studies the random transverse-field Ising chain, contrasting a microcanonical ensemble—where disorder realizations satisfy a precise constraint on the random variables—with a canonical ensemble in which variables are drawn from an unconstrained distribution. That work asks directly whether critical exponents can differ between the two cases and answers affirmatively through a detailed study, establishing that ensemble dependence of exponents is not pathological but generic in disordered criticality. The QEC threshold, being an average over random codes and noise realizations, is precisely such a disordered critical point, so the analogy is structural, not merely rhetorical.

**The source claim.** Refs. [1, 2] report that in a random-unitary encoding model, generic channels and quantum trajectories—two descriptions that should be equivalent in the thermodynamic limit by standard unraveling arguments—yield different exponents for both fidelity and magic at threshold, that these exponents saturate the Feldman et al. (2026) information-theoretic bound (extended from grand-canonical to canonical and intermediate ensembles), and that the very existence of the transition is ensemble-dependent. (We cite [1] and [2] separately as they appear in the source bibliography as the query record and the versioned preprint; they refer to the same work.)

**Foundations of QEC.** Ref. [10] provides the modern definition: a code is a subspace such that common errors map the encoded state into an orthogonal error space, enabling syndrome-based recovery. Ref. [8] introduces the operational core—encoding, syndrome extraction, error operators, and code construction—and shows that general noise on two-state systems decomposes into Pauli operators, which is why Pauli-error models dominate threshold analyses; this decomposition is also what makes "generic channel" versus "trajectory" distinctions sharp, since a channel is a probabilistic mixture of Pauli actions while a trajectory is a single stochastic realization. Ref. [7] surveys the passage from classical to quantum coding, emphasizing that quantum channels behave differently from classical ones—superposition and measurement disturbance mean that naive classical error-control intuition fails, which is the historical reason ensemble questions in QEC were underexamined. Ref. [9] extends QEC beyond qubits to continuous-variable and higher-dimensional systems, noting that the discovery of QEC transformed quantum information from a curiosity into a technology; this matters here because the ensemble-dependence claim, if robust, applies to any platform whose threshold is estimated by averaging over random realizations. Ref. [5] introduces entanglement-assisted codes, in which pre-shared entanglement between sender and receiver relaxes the dual-containing constraint of standard stabilizer codes; entanglement assistance changes the structure of the code ensemble and hence is a natural variable to hold fixed when comparing ensembles. Ref. [4] treats continuous-time QEC, in which noise and correction are simultaneous weak-measurement-and-feedback processes; this is the setting where the channel-versus-trajectory distinction is most physically acute, since continuous measurement intrinsically produces trajectories, and the subsystem principle it invokes—protected information lives in a subsystem factor of the Hilbert space—gives an operational meaning to fidelity at threshold. Ref. [6] proposes QEC in quaternionic Hilbert spaces with quaternionic Pauli analogues; while exotic, it illustrates that the framework of error spaces and encoding maps is representation-independent, so ensemble dependence, if real, should survive changes of the underlying Hilbert-space structure.

**QNFO corpus context.** Ref. [11] on spectral benchmarking of holographic quantum simulations is relevant because benchmarking protocols implicitly fix an ensemble over problem instances; an ensemble-dependent exponent would make spectral benchmarks non-comparable across protocols. Ref. [12], on the lifecycle of a fault-tolerant quantum computer, treats threshold crossing as a lifecycle milestone; if the exponent—and per [1, 2] even the existence of the transition—depends on ensemble, lifecycle cost models built on a single exponent inherit that ambiguity. Ref. [13] on thermodynamic and informational bottlenecks of scalable fault-tolerant computation directly intersects the present topic: it argues that thermodynamic-style limits constrain scalable QEC, and the claim of [1, 2] sharpens this by suggesting the limits themselves are ensemble-labeled. Ref. [14] on operationalizing generalized symmetries provides the mathematical language—non-invertible and higher-form symmetries—increasingly used to characterize phases including error-correcting phases, and ensemble dependence of a transition's existence is naturally phrased as symmetry-structure dependence on the disorder ensemble.

## 3. Methods

**Model.** Following [1, 2]: a logical state ρ_L on k qubits is encoded by a Haar-random unitary U into n physical qubits, subjected to noise at rate p, and decoded by U†. The noise is either (a) a generic channel Λ_p (e.g., depolarizing: each qubit is replaced by the maximally mixed state with probability p) or (b) a quantum trajectory unraveling of Λ_p, in which the channel is realized as a stochastic sequence of pure-state quantum jumps conditioned on fictitious measurement outcomes. The two are equivalent at the level of the density matrix by construction: Λ_p[ρ] = Σ_j K_j ρ K_j† with Kraus operators {K_j}; the trajectory ensemble samples individual Kraus-index strings j₁j₂… with the correct weights. Ensemble equivalence would demand that any observable's statistics agree; the claim of [1, 2] is that critical exponents—and transition existence—do not.

**Observables.** Fidelity F(p, n) = ⟨ψ|𝒟∘Λ_p∘𝒰[|ψ⟩⟨ψ|]|ψ⟩ averaged over Haar-random U and input states |ψ⟩. Magic M(σ) quantifies non-stabilizer content; we use the mana-type measure M(σ) = log₂ Σ_ν |ω_ν(σ)| where ω_ν are stabilizer-phase-space quasiprobability amplitudes, but the scaling arguments below only require that M is extensive and vanishes on stabilizer states.

**Scaling ansatz.** Near threshold,
F(p, n) = F_c − A (p_c − p)^β 𝒢((p_c − p) n^{1/ν_s}),
with β the fidelity exponent, ν_s the finite-size shift exponent, and 𝒢(0) = 1. The hypothesis under test, per [1, 2]: the trajectory ensemble yields β_traj and the channel ensemble β_chan, both saturating the Feldman bound, which we denote β_max. For concreteness in the derivations we adopt the minimal nontrivial assignment consistent with "different exponents saturating a bound": β_chan = 1 and β_traj = 2 = β_max. We emphasize this assignment is a hypothesis, not a measurement; Section 4 states every input number and Section 5 labels all outputs accordingly.

**Statistical framework.** To compare ensembles we compute the fidelity gap ΔF between the two scaling laws at fixed Δp = p_c − p, then ask how many independent samples N are needed for the gap to exceed two standard errors of the mean, with per-sample standard deviation σ_F. All inputs are stated explicitly below.

## 4. Analysis

**Input numbers and sources.**

- Exponent hypotheses: β_chan = 1, β_traj = 2 (hypothesis from the saturation claim of [1, 2]; the bound value 2 is an assumption of this analysis, since the Feldman et al. 2026 paper is not in our bibliography and we cannot verify it).
- Amplitude A = 0.1 (assumed; dimensionless, sets the scale of the fidelity singularity; any A > 0 gives the same scaling conclusions).
- Threshold F_c = 0.5 (assumed; the random-unitary model with Haar averaging plausibly gives F_c = 1/2 by symmetry between correct and incorrect decoding, but this is an assumption).
- Per-sample fidelity standard deviation σ_F = 0.01 (assumed, typical for single-shot fidelity estimates on n ~ 10²–10³ qubits).
- Distances from threshold: Δp = 10⁻² and Δp = 10⁻³ (chosen).

**Step 1: Fidelity gap at Δp = 10⁻².**

F_chan = F_c − A·(Δp)^{β_chan} = 0.5 − 0.1 × (10⁻²)¹ = 0.5 − 0.1 × 0.01 = 0.5 − 0.001 = 0.499.
F_traj = 0.5 − 0.1 × (10⁻²)² = 0.5 − 0.1 × 0.0001 = 0.5 − 0.00001 = 0.49999.
ΔF = F_traj − F_chan = 0.49999 − 0.499 = 0.00099 = 9.9 × 10⁻⁴.

**Step 2: Fidelity gap at Δp = 10⁻³.**

F_chan = 0.5 − 0.1 × (10⁻³)¹ = 0.5 − 0.0001 = 0.4999.
F_traj = 0.5 − 0.1 × (10⁻³)² = 0.5 − 0.1 × 10⁻⁶ = 0.5 − 10⁻⁷ = 0.4999999.
ΔF = 0.4999999 − 0.4999 = 0.0000999 = 9.99 × 10⁻⁵.

Note the gap scales as Δp − Δp² ≈ Δp for small Δp: the leading behavior is linear because β_chan = 1 dominates. The relative gap ΔF/F-singularity grows: at Δp = 10⁻², the trajectory ensemble's singularity is 1% of the channel's (10⁻⁴ vs 10⁻² amplitude term); at Δp = 10⁻³ it is 0.1%.

**Step 3: Sample size to resolve the gap.** Require ΔF ≥ 2σ_F/√N, i.e., N ≥ (2σ_F/ΔF)².

At Δp = 10⁻²: N ≥ (2 × 0.01 / 9.9 × 10⁻⁴)² = (0.02 / 0.00099)² = (20.202…)². Compute: 20.202² = 20.202 × 20.202. 20 × 20.202 = 404.04; 0.202 × 20.202 = 4.0808; total = 408.12. So N ≥ 408.12, hence N = 409 samples.

At Δp = 10⁻³: N ≥ (0.02 / 9.99 × 10⁻⁵)² = (200.2…)². Compute: 0.02 / 0.0000999 = 200.2002…. Square: 200.2002² = 200² + 2×200×0.2002 + 0.2002² = 40000 + 80.08 + 0.0401 = 40080.12. So N ≥ 40080.12, hence N = 40081 samples, i.e., ≈ 4.0 × 10⁴.

**Step 4: Scaling of the sample requirement.** Since ΔF ≈ A·Δp for β_chan = 1, N ∝ Δp⁻². But resolving the exponent β itself (not just the gap) requires fitting over a range of Δp; distinguishing β = 1 from β = 2 requires that the quadratic term A·Δp² be detectable against the linear term, i.e., relative resolution δ = Δp²/Δp = Δp in the singularity. With fidelity resolution 2σ_F/√N, the condition is 2σ_F/√N ≤ A·Δp², giving N ≥ (2σ_F/(A·Δp²))² = (2 × 0.01 / (0.1 × Δp²))² = (0.2/Δp²)² = 0.04/Δp⁴.

At Δp = 10⁻²: N ≥ 0.04 / 10⁻⁸ = 0.04 × 10⁸ = 4 × 10⁶ samples.
At Δp = 10⁻³: N ≥ 0.04 / 10⁻¹² = 4 × 10¹⁰ samples.

This Δp⁻⁴ divergence is the central quantitative result: exponent separation is cheaply resolvable only far from threshold, but far from threshold the asymptotic power law may not hold, creating a squeeze.

**Step 5: Crossover scale.** With finite-size scaling F = F_c − A·Δp^β·𝒢(Δp·n^{1/ν_s}) and ν_s = 1 (assumed shift exponent), the finite-size rounding is δp ~ 1/n. Ensembles differing only in β are distinguishable only when A·Δp − A·Δp² exceeds finite-size smearing of the singularity, estimated as A/n. Setting A·Δp − A·Δp² = A/n with Δp = 1/n (i.e., working at the finite-size threshold): 1/n − 1/n² = 1/n, which fails by 1/n²; hence the quadratic ensemble's singularity is entirely below finite-size rounding at the finite-size threshold. Distinguishability requires Δp ≫ 1/n and Δp² ≫ 1/n, i.e., n ≫ 1/Δp². At Δp = 10⁻²: n ≫ 10⁴ qubits. At Δp = 10⁻³: n ≫ 10⁶ qubits. Combined with Step 4, resolving β_traj = 2 at Δp = 10⁻³ needs both n > 10⁶ and N > 4 × 10¹⁰ — a compound cost of 10⁶ × 4 × 10¹⁰ = 4 × 10¹⁶ qubit-samples (projection: product of the two lower bounds, assuming independence of system-size and sample-count costs).

**Step 6: Magic scaling (projection).** If magic density m = M/n obeys m(p) = m_c − B·Δp^{β_M} with B = 0.1 (assumed) and the same exponent split, identical arithmetic applies: the magic gap at Δp = 10⁻² is 9.9 × 10⁻³ in magic density, resolvable with N = 409 samples at σ_m = 0.01 (assumed equal to σ_F). This is a projection, not a computation from measured magic data.

## 5. Results

All numbers below are outputs of the arithmetic in Section 4 under the stated assumptions (β_chan = 1, β_traj = 2, A = 0.1, F_c = 0.5, σ_F = 0.01, ν_s = 1); none are empirical measurements.

1. **Fidelity gap between ensembles:** ΔF = 9.9 × 10⁻⁴ at Δp = 10⁻²; ΔF = 9.99 × 10⁻⁵ at Δp = 10⁻³. The gap is linear in Δp to leading order.
2. **Samples to resolve the gap at 2σ:** N = 409 at Δp = 10⁻²; N = 40,081 at Δp = 10⁻³.
3. **Samples to resolve the exponent (detect the quadratic term):** N ≥ 4 × 10⁶ at Δp = 10⁻² and N ≥ 4 × 10¹⁰ at Δp = 10⁻³, following N = 0.04/Δp⁴ (projection with the stated σ_F and A).
4. **Minimum system size for exponent separation:** n ≫ 1/Δp², i.e., n ≫ 10⁴ qubits at Δp = 10⁻² and n ≫ 10⁶ at Δp = 10⁻³.
5. **Compound cost projection:** resolving β_traj = 2 at Δp = 10⁻³ requires ≳ 4 × 10¹⁶ qubit-samples (product of bounds, independence assumed; uncertainty: the bound could be relaxed by a factor up to ~10³ if σ_F is reduced by variance-reduction techniques, giving 4 × 10¹³–4 × 10¹⁶ as a projected range).
6. **Magic gap (projection):** 9.9 × 10⁻³ in magic density at Δp = 10⁻², under B = σ_m assumptions as stated.

## 6. Discussion

**Limitations.** First, our exponent assignment (β = 1 vs 2) is a hypothesis chosen to make the saturation claim of [1, 2] concrete; the actual preprint's exponents may differ, and every number in Section 5 rescales accordingly—the Δp⁻⁴ sample law, however, holds for any pair β₁ < β₂ with the replacement Δp² → Δp^{β₂}. Second, the Feldman et al. (2026) bound is cited in [1, 2] but is not in our bibliography; we cannot verify its value, form, or even its existence beyond the source abstract, and our "β_max = 2" is an assumption. Third, the random-unitary single-step model is far from practical QEC: real codes are structured (stabilizer, topological), and structured-code ensembles may restore ensemble equivalence. Fourth, our statistical model assumes independent samples and Gaussian errors; Haar-random unitary fidelity distributions have heavy tails, inflating σ_F and hence N.

**Failure modes and self-criticism.** The strongest counterargument to [1, 2] is that trajectory and channel ensembles are mathematically equivalent for any linear observable of the density matrix: the trajectory average *is* the channel. Any reported exponent difference must therefore arise from (a) nonlinear functionals (magic measures are nonlinear in ρ, so this is plausible for magic but not fidelity), (b) non-equivalence of the *order of limits*—averaging over trajectories before or after taking n → ∞ need not commute at criticality, which is the most likely mechanism and echoes the constrained-versus-unconstrained averaging of [3], or (c) finite-size artifacts misread as asymptotic exponents. Our Step 4 result sharpens (c): at Δp = 10⁻² with n = 10³, the quadratic term is 10⁻⁴ × A, below the finite-size rounding A/n = 10⁻³, so a simulation at that scale *cannot* see β_traj = 2 and might report spurious effective exponents. Conversely, if [1, 2] observed exponent differences at modest sizes, that itself is evidence against the asymptotic interpretation.

**What would falsify the claims.** (i) A demonstration that fidelity exponents agree between channel and trajectory ensembles in the joint limit (n → ∞, then Δp → 0, samples → ∞) at fixed averaging order. (ii) An analytic solution of the random-unitary model showing F(p) is exactly linear in Δp for both ensembles. (iii) Failure of the predicted Δp⁻⁴ sample-cost law in well-controlled simulations. (iv) Derivation of the Feldman bound showing the QEC exponents fall strictly below it.

**Open questions.** Does ensemble dependence survive for topological codes with local noise? Is the intermediate ensembles of [1, 2] a one-parameter family connecting the exponents continuously, and if so, is β(λ) monotone? Does the lifecycle cost modeling of [12] change qualitatively if the threshold exponent is ensemble-labeled? Can the spectral-benchmarking protocols of [11] be made ensemble-invariant? And does the symmetry-based framing of [14] identify the ensemble as a choice of disorder symmetry whose breaking drives the transition's existence?

**Bibliography limitation.** Our bibliography contains 14 works, of which [1] and [2] describe the same source paper; the Feldman et al. (2026) bound and all primary QEC-threshold numerics are inaccessible within this corpus, so all quantitative claims here rest on stated assumptions rather than verified external data.

## 7. Conclusion

We have analytically examined the claim that critical exponents at a quantum error correction threshold are ensemble-dependent [1, 2], connecting it to the established ensemble-dependence phenomenon in disordered Ising chains [3] and situating it within the QEC literature [4]–[10] and the QNFO corpus [11]–[14]. Our explicit derivations show that if two ensembles carry exponents β = 1 and β = 2, their fidelity signatures differ by ~10⁻³ at 1% from threshold—cheaply resolvable with ~409 samples—but that resolving the *exponent itself* costs N = 0.04/Δp⁴ samples and n ≫ 1/Δp² qubits, a compound burden of ~4 × 10¹⁶ qubit-samples at Δp = 10⁻³. This squeeze means ensemble dependence is simultaneously easy to miss (finite-size experiments cannot see it near threshold) and hard to confirm (far from threshold the asymptotic regime fails). The claim, if true, implies that every published threshold exponent carries an implicit, often unstated, ensemble label—a correction to standard practice whose verification is expensive but, by the arithmetic above, not impossible.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2609.21886&amp;start=0&amp;max_results=1
[2] arXiv:2609.21886v1 | Ensemble Dependence of the Critical Exponent at a Quantum Error Correction Threshold
[3] arXiv:cond-mat/0305664v1 | Ensemble dependence in the Random transverse-field Ising chain
[4] arXiv:1311.2485v2 | Continuous-time quantum error correction
[5] arXiv:1610.04013v1 | Entanglement-Assisted Quantum Error-Correcting Codes
[6] arXiv:2504.19833v1 | Quantum Error Correction in Quaternionic Hilbert Spaces
[7] arXiv:quant-ph/0602157v1 | An Introduction to Error-Correcting Codes: From Classical to Quantum
[8] arXiv:quant-ph/0304016v2 | Quantum Computing and Error Correction
[9] arXiv:0811.3734v1 | Quantum error correction beyond qubits
[10] arXiv:1910.03672v1 | Quantum Error Correction
[11] QNFO: Spectral Benchmarking of Holographic Quantum Simulations | DOI 10.5281/zenodo.18327721
[12] QNFO: Lifecycle of a Fault-Tolerant Quantum Computer | DOI 10.5281/zenodo.18000790
[13] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation | DOI 10.5281/zenodo.17955898
[14] QNFO: Operationalizing Generalized Symmetries | DOI 10.5281/zenodo.18199396