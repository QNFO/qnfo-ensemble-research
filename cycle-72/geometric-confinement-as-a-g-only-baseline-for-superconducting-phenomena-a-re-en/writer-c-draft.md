# Geometric Confinement as a G-Only Baseline for Superconducting Phenomena: A Re-Entry Analysis of the QNFO Geometric Unification Framework

## Abstract

We develop a "G-only" baseline for the geometric unification framework catalogued in the QNFO corpus (DOIs 10.5281/zenodo.18496889 and 10.5281/zenodo.17074726), in which superconducting behaviour is re-entered from geometric confinement alone, before any material-specific pairing mechanism is introduced. The baseline isolates a single dimensionless confinement parameter $\Gamma$, built from the ratio of a geometric length scale to the superconducting penetration depth, and asks how much of the observed phenomenology of confined superconductors—vortex nucleation thresholds in thin disks, nonlinear microwave response, and coherence-time-limited resonator operation—can be organised by $\Gamma$ alone. We derive closed-form scaling relations for the confinement parameter, compute a model vortex-entry threshold $H_0^{(G)} = \Phi_0/(\pi R^2)$ for an assumed disk radius, and quantify the frequency span and coherence-time budget implied by published measurements on superconducting quantum interference filters and copper waveguide cavities coupled to qubits. We find that a G-only baseline fixes the geometry-dependent normalisation of observables but cannot, by construction, account for material-dependent quantities such as critical temperature; we quantify this separation explicitly. The baseline provides a controlled null hypothesis against which pairing-driven extensions of the framework must be tested, and we state the conditions under which it would be falsified.

## 1. Introduction

The QNFO corpus frames superconductivity within a "Geometric Unification Framework" (DOI 10.5281/zenodo.17074726) and a companion "Superconductivity Quadrangle" entry (DOI 10.5281/zenodo.18496889). The research idea under study here, "Re-entry from 10.5281/zenodo.18496889: geometric confinement (G-only baseline)", asks a specific methodological question: if one strips the framework down to geometry alone—confinement lengths, boundary shapes, and the ratio of those lengths to intrinsic superconducting length scales—how much of the phenomenology of confined superconducting systems can be reproduced, and where does the baseline necessarily fail?

The motivation for such a null baseline is standard in quantitative science: before attributing an effect to a microscopic mechanism, one should establish what a mechanism-free, geometry-only description predicts. In superconductivity this is particularly pertinent because the literature itself is divided on how much of the phenomenology is universal and how much is material-specific. One line of work argues that whatever the mother normal states are, the superconducting condensate behaves in a BCS-like, "normal" fashion [1]; another line emphasises that the diversity of normal states and of band structures (non-parabolic bands, multi-band systems) is essential [3], [5]. A G-only baseline sits deliberately between these positions: it assumes nothing about pairing, but exploits the fact that geometry—thin films, disks, quasi-one-dimensional lattices, cavity boundaries—constrains the possible states of any condensate regardless of its microscopic origin.

This paper makes three contributions. First, it defines the G-only baseline precisely through a single confinement parameter $\Gamma$ and derives its scaling relations (Section 3). Second, it computes concrete numerical values for the baseline using explicitly stated assumed parameters and published qualitative constraints (Section 4). Third, it maps which published observations the baseline can organise—geometric barriers and flux domes in thin disks [8], two-tone mixing bandwidths in superconducting quantum interference filters [7], coherence-time budgets of cavity-coupled qubits [6]—and which it cannot, namely critical temperatures and pairing-specific nonlinear relaxation [2], [3].

## 2. Background and Related Work

We review the eight arXiv works in the supplied bibliography, in each case restricting ourselves to what the supplied summaries state, and then the two QNFO corpus entries.

**Pairing universality versus material specificity.** Reference [1] (arXiv:1603.03851v3) addresses the puzzle of how superconductivity in unconventional superconductors emerges from diverse mother normal states, and argues that whatever the mother normal states are, the superconductivity is *normal*, with BCS-like behaviours of the paired quasiparticles in condensation. This universality claim is the strongest possible support for a baseline approach: if the condensate side is universal, then the residual variation among materials must live either in the mother normal states or in geometry. The G-only baseline is precisely the geometry-only slice of that residual. Reference [3] (arXiv:1811.11656v1) applies a dielectric function method for superconductivity to SrTiO$_3$, accounting for the non-parabolic dispersion of conduction-band charge carriers and for optical-phonon dispersion based on density functional theory calculations, and reports critical temperatures in agreement with experiments in the density (the supplied summary is truncated at this point, so we cannot cite the specific density regime). This work is the clearest counterweight to a pure baseline: it demonstrates that band-structure detail—explicitly non-geometric—enters the prediction of $T_c$. Our framework treats such band effects as the leading term that the G-only baseline deliberately omits.

**Confinement and dimensionality.** Reference [4] (arXiv:1710.01668v1) studies superconducting properties of population-imbalanced fermionic mixtures in quasi-one-dimensional optical lattices, described by an attractive Hubbard model with a Zeeman magnetic field term, and investigates the ground-state phase diagram as a function of chemical potential and magnetic field. The quasi-one-dimensional geometry is a geometric confinement in our sense; the population imbalance and Zeeman field are non-geometric inputs. The supplied summary is truncated before the phase-diagram findings, so we use this work only as evidence that confined, quasi-one-dimensional geometry is an active setting for superconducting phase structure. Reference [5] (arXiv:1712.06027v2) reports on Lifshitz transitions in multi-band Hubbard models for topological superconductivity in complex quantum matter, in the context of the Superstripes 2017 conference held in Ischia in June 2017, and poses the resistance of macroscopic quantum coherence to decoherence as a major challenge; the summary further indicates that a standard model of high-$T_c$ superconductivity grabbing the physics of complex matter is under discussion (the summary is truncated mid-sentence, so its precise conclusion is not available to us). Multi-band structure and Lifshitz transitions are again material-side inputs that a G-only baseline excludes.

**Microwave response and device physics.** Reference [2] (arXiv:1608.06329v2) synchronously measured the second- and third-order nonlinear microwave response of a superconducting YBa$_2$Cu$_3$O$_7$ thin-film resonator using three input tones, a technique permitting local measurement and hence mapping of intermodulation distortion (IMD) inside the resonator, and found that second- and third-order IMD measured with a fixed probe relaxed in remarkably different ways after removal of a static magnet. The differential relaxation of the two IMD orders is a material- and history-dependent effect; a G-only baseline has nothing to say about it, and we use it in Section 6 as a falsification probe: any claim that geometry dominates nonlinear response must explain why the two IMD orders relax differently after the same geometric configuration is restored. Reference [6] (arXiv:1409.3245v1) reports significant improvements in superconducting qubit coherence times achieved with three-dimensional microwave waveguide cavities coupled to transmon qubits, noting that while many measurements used superconducting aluminum cavities, other work involved qubits coupled to copper cavities with coherence times approaching $0.1$ ms, and that the copper provides a (summary truncated). This is a directly geometric observation: the three-dimensional cavity geometry, independent of whether the cavity itself is superconducting, supports long coherence times. Reference [7] (arXiv:cond-mat/0608562v1) exploits the parabolic shape of the dc voltage output dip around $B=0$ of a Superconducting Quantum Interference Filter (SQIF) to mix weak external rf signals, detecting the two-tone response at the difference frequency $f_0 = f_1 - f_2$ for tones $f_1, f_2$ ranging from a few MHz up to 20 GHz. The parabolic dip around $B=0$ is a geometric interference effect of the loop array, and the enormous frequency span is a bandwidth figure we quantify in Section 4.

**Geometric barriers.** Reference [8] (arXiv:0807.5129v1) analyses an ideal (no bulk pinning) flat type-II superconducting disk in a perpendicular applied field $H_a$: the first vortex nucleates at the rim when $H_a = H_0$, the threshold field, and moves quickly to the center of the disk; as $H_a$ increases above $H_0$, additional vortices join and produce a domelike field distribution of radius $b$, and the paper presents an analysis (summary truncated) of these geometrical barriers. This is the paradigmatic G-only system: with bulk pinning removed, the entire vortex phenomenology is governed by geometry. Our Section 4 builds its model threshold on exactly this picture.

**QNFO corpus.** Reference [9] (QNFO: Superconductivity Quadrangle, DOI 10.5281/zenodo.18496889) and Reference [10] (QNFO: Geometric Unification Framework, DOI 10.5281/zenodo.17074726) are corpus entries whose supplied summaries contain no additional text; we therefore use them only as the identifiers of the framework being re-entered and the source idea of this paper, and draw no substantive claims from them.

## 3. Methods

### 3.1 Definition of the G-only baseline

The G-only baseline retains exactly two classes of input:

1. **Geometric data:** a characteristic confinement length $L_g$ (disk radius $R$, film thickness $d$, lattice period, or cavity dimension) and the boundary shape.
2. **Universal superconducting length scales:** the penetration depth $\lambda_L$, which sets the screening response of any condensate, and the flux quantum $\Phi_0$, which sets the circulation quantum of any charged condensate.

It excludes: pairing interaction strengths, band dispersions, multi-band structure, population imbalance, pinning, and material-specific surface physics.

### 3.2 The confinement parameter

We define the dimensionless confinement parameter

$$\Gamma \equiv \frac{2\lambda_L^2}{d\,L_g},$$

where $d$ is the film thickness and $L_g$ the in-plane confinement length. The factor $2\lambda_L^2/d$ is the thin-film screening length that replaces $\lambda_L$ when $d \ll \lambda_L$; dividing by $L_g$ compares screening strength with confinement. Three regimes follow immediately:

- $\Gamma \ll 1$: screening dominates over confinement; the system behaves as a bulk-like screen of its geometry.
- $\Gamma \sim 1$: screening and confinement compete; geometric barriers are expected to be strongest.
- $\Gamma \gg 1$: confinement dominates; the system is effectively a weak screen and geometric barriers are washed out.

For a thin disk of radius $R$ and thickness $d$, the G-only threshold field for first vortex entry is modelled by equating the flux through the disk area to one flux quantum:

$$H_0^{(G)} = \frac{\Phi_0}{\pi R^2}.$$

This is a deliberately minimal model: it captures only the single-quantum nucleation constraint stated qualitatively in [8], not the full barrier analysis of that work.

### 3.3 Observables

We compute three families of G-only observables: (i) $\Gamma$ for representative thin-film geometries; (ii) $H_0^{(G)}$ as a function of $R$; (iii) two device-level quantities that are purely geometric in origin—the SQIF mixing bandwidth ratio from [7] and the coherence-time phase-space product for cavity-coupled qubits from [6]. All assumed parameter values are stated at point of use and are labelled as assumptions, not measurements.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

**Input A (assumption, stated):** $\lambda_L = 100\ \mathrm{nm} = 1.0\times10^{-7}\ \mathrm{m}$, a representative conventional thin-film penetration depth, used only as an illustrative parameter.

**Input B (assumption, stated):** $d = 50\ \mathrm{nm} = 5.0\times10^{-8}\ \mathrm{m}$, a representative thin-film thickness.

**Input C (assumption, stated):** $R = 1.0\ \mu\mathrm{m} = 1.0\times10^{-6}\ \mathrm{m}$, a representative disk radius for geometric-barrier studies of the type in [8].

**Input D (standard constant, stated):** $\Phi_0 = 2.07\times10^{-15}\ \mathrm{Wb}$.

**Input E (from [6], stated in its summary):** coherence times of qubits coupled to copper cavities approaching $0.1\ \mathrm{ms} = 1.0\times10^{-4}\ \mathrm{s}$.

**Input F (from [7], stated in its summary):** two-tone frequencies $f_1, f_2$ ranging from a few MHz up to 20 GHz; we take the span endpoints as $f_{\min} = 1.0\times10^6\ \mathrm{Hz}$ ("a few MHz", lower bound) and $f_{\max} = 2.0\times10^{10}\ \mathrm{Hz}$.

**Input G (assumption, stated):** a representative qubit-cavity operating frequency $f_q = 5.0\times10^9\ \mathrm{Hz}$, used with Input E.

**Derivation 1: screening length.** With Inputs A and B,

$$\Lambda \equiv \frac{2\lambda_L^2}{d} = \frac{2\times(1.0\times10^{-7}\ \mathrm{m})^2}{5.0\times10^{-8}\ \mathrm{m}} = \frac{2\times10^{-14}}{5.0\times10^{-8}}\ \mathrm{m} = 4.0\times10^{-7}\ \mathrm{m} = 400\ \mathrm{nm}.$$

**Derivation 2: confinement parameter.** With $L_g = R = 1.0\times10^{-6}\ \mathrm{m}$ (Input C),

$$\Gamma = \frac{\Lambda}{R} = \frac{4.0\times10^{-7}}{1.0\times10^{-6}} = 0.40.$$

Since $0.40 < 1$ but is within an order of magnitude of unity, a disk with these parameters sits in the intermediate regime where geometric barriers are expected to be significant, consistent with the qualitative picture of [8] that the rim nucleation threshold and domelike flux growth are governed by the disk geometry.

**Derivation 3: G-only vortex-entry threshold.** With Inputs C and D,

$$H_0^{(G)} = \frac{\Phi_0}{\pi R^2} = \frac{2.07\times10^{-15}\ \mathrm{Wb}}{\pi\times(1.0\times10^{-6}\ \mathrm{m})^2} = \frac{2.07\times10^{-15}}{3.1416\times10^{-12}}\ \mathrm{T} = 6.59\times10^{-4}\ \mathrm{T} \approx 0.66\ \mathrm{mT}.$$

Scaling with radius: since $H_0^{(G)} \propto R^{-2}$, a tenfold larger disk ($R = 10\ \mu\mathrm{m}$) gives

$$H_0^{(G)}(10\ \mu\mathrm{m}) = 6.59\times10^{-4}\times10^{-2}\ \mathrm{T} = 6.59\times10^{-6}\ \mathrm{T} \approx 6.6\ \mu\mathrm{T},$$

i.e. the threshold falls by two orders of magnitude per decade of radius. This steep scaling is the G-only prediction: the entry field is a pure function of geometry.

**Derivation 4: SQIF mixing bandwidth.** With Input F, the ratio of span endpoints is

$$\frac{f_{\max}}{f_{\min}} = \frac{2.0\times10^{10}}{1.0\times10^{6}} = 2.0\times10^{4},$$

corresponding to

$$\log_{10}(2.0\times10^{4}) = \log_{10}2 + 4 = 0.301 + 4 = 4.30$$

orders of magnitude of two-tone mixing bandwidth. Because the SQIF output dip is parabolic around $B=0$ [7], the mixing response is a geometric interference property of the loop array; the G-only baseline therefore predicts that the bandwidth is set by the loop-array geometry and not by the pairing mechanism, though the baseline supplies no model for the absolute mixing efficiency (the summary of [7] gives no efficiency numbers).

**Derivation 5: coherence-time phase-space product.** With Inputs E and G, the number of coherent phase rotations accumulated in one coherence interval is

$$N_\phi = 2\pi f_q \tau = 2\pi\times(5.0\times10^9\ \mathrm{Hz})\times(1.0\times10^{-4}\ \mathrm{s}) = 3.14\times10^{6}.$$

Equivalently, the dimensionless figure of merit $\omega\tau$ with $\omega = 2\pi f_q$:

$$\omega\tau = 3.14\times10^{6}.$$

This is a purely kinematic quantity: it says that a qubit-cavity system with the coherence time reported approaching $0.1$ ms in [6] sustains of order $10^6$ coherent cycles at a 5 GHz operating frequency, regardless of the microscopic decoherence channels. The three-dimensional cavity geometry is the geometric input; the baseline attributes the coherence budget to geometry-supported mode confinement, while explicitly not modelling surface-loss mechanisms (the summary of [6] notes copper provides a surface whose role is truncated in the supplied text).

**Derivation 6: what the baseline cannot fix.** The critical temperature $T_c$ is not a function of $\Gamma$ in the G-only baseline: no pairing scale enters. Reference [3] demonstrates that $T_c$ predictions require band-dispersion input (non-parabolic bands, optical-phonon dispersion), and reference [1] locates the universality in the condensate rather than the normal state. Formally, the G-only prediction set is

$$\mathcal{O}_{G} = \{H_0^{(G)},\ \Gamma\text{-regime},\ \text{bandwidth ratios},\ \omega\tau\},$$

and $T_c \notin \mathcal{O}_{G}$. We quantify the separation by noting that $H_0^{(G)}$ varies by $10^2$ per decade of $R$ (Derivation 3), whereas any $T_c$ variation must come from excluded inputs; the baseline thus predicts geometry-dominated observables to be far more sensitive to geometry than to any parameter it retains.

## 5. Results

All numbers below are those computed in Section 4; no new measurements or simulations are reported.

1. **Screening length (computed):** for the assumed parameters $\lambda_L = 100$ nm and $d = 50$ nm, $\Lambda = 400$ nm.
2. **Confinement parameter (computed):** for $R = 1.0\ \mu$m, $\Gamma = 0.40$, placing the disk in the intermediate screening-confinement regime.
3. **Vortex-entry threshold (computed, model):** $H_0^{(G)} = 6.59\times10^{-4}\ \mathrm{T} \approx 0.66$ mT at $R = 1.0\ \mu$m, scaling as $R^{-2}$; at $R = 10\ \mu$m the model gives $6.59\times10^{-6}\ \mathrm{T} \approx 6.6\ \mu$T. These are model projections of the minimal single-quantum nucleation constraint, not measurements; the full barrier analysis of [8] would modify the prefactor.
4. **SQIF mixing bandwidth (computed from stated span):** the two-tone span from a few MHz to 20 GHz [7] spans a ratio of $2.0\times10^4$, i.e. $4.30$ orders of magnitude.
5. **Coherence phase-space product (computed from stated inputs):** with $\tau \approx 1.0\times10^{-4}$ s [6] and an assumed $f_q = 5$ GHz, $\omega\tau = 3.14\times10^6$ coherent cycles.
6. **Scope result (structural):** the G-only observable set $\mathcal{O}_G$ contains geometry-dominated quantities only; $T_c$ and material-specific nonlinear relaxation are outside it.

**Projection with stated assumptions and uncertainty:** if the disk radius is uncertain by a factor $r_\pm$ and the threshold scales as $R^{-2}$, the threshold uncertainty is a factor $r_\pm^2$; e.g. a $\pm 20\%$ radius uncertainty ($r_\pm = 1.2$) gives a threshold range $[0.66/1.44,\ 0.66\times1.44]$ mT $= [0.46,\ 0.95]$ mT. This is the only uncertainty statement the baseline can make without material input.

## 6. Discussion

**Limitations.** The G-only baseline is deliberately mechanism-free, and this is both its strength and its ceiling. Three limitations are fundamental. First, it cannot predict $T_c$: as the SrTiO$_3$ dielectric-function analysis shows [3], critical temperatures depend on non-parabolic band dispersion and phonon dispersion, inputs the baseline excludes by construction. Second, the minimal threshold model $H_0^{(G)} = \Phi_0/(\pi R^2)$ ignores the full geometrical-barrier physics analysed in [8], where the first vortex nucleates at the rim and subsequent vortices build a domelike distribution of radius $b$; our model captures only the nucleation scale, not the dome growth, and the true threshold prefactor may differ. Third, the assumed parameters ($\lambda_L = 100$ nm, $d = 50$ nm, $R = 1\ \mu$m, $f_q = 5$ GHz) are illustrative; the computed values of $\Gamma$, $H_0^{(G)}$, and $\omega\tau$ scale with these assumptions and should be read as normalisations, not predictions for any specific material system.

**Failure modes and falsification.** The baseline would be falsified in the following ways. (i) If geometric observables such as vortex-entry thresholds were found to depend strongly on material substitution at fixed geometry, the claim that geometry dominates $\mathcal{O}_G$ would fail. (ii) If the differential relaxation of second- and third-order intermodulation distortion after removal of a static magnet, observed in the YBa$_2$Cu$_3$O$_7$ resonator of [2], could be reproduced by a geometry-only model, the baseline would overreach; conversely, since that observation shows two nonlinear orders relaxing "in remarkably different ways" in the same geometry, it is evidence that nonlinear response carries material- and history-dependent content beyond geometry, and we treat it as an explicit out-of-scope phenomenon. (iii) If the universality claim of [1]—BCS-like condensate behaviour independent of mother normal state—were violated, the clean separation between universal condensate physics (which the baseline exploits) and material-specific normal-state physics (which it excludes) would collapse. (iv) If coherence times of cavity-coupled qubits were found independent of cavity geometry, the geometric attribution of the coherence budget in Derivation 5 would fail; the supplied summary of [6] indicates three-dimensional waveguide cavities are associated with significant coherence improvements, but it does not isolate geometry from other cavity properties, so our attribution is a hypothesis, not a demonstrated cause.

**Arguing against ourselves.** A critic could object that the "G-only" label is partly cosmetic: the penetration depth $\lambda_L$ is itself material-dependent, so $\Gamma$ smuggles material physics into a supposedly geometry-only parameter. We concede this partially: $\lambda_L$ is a condensate property, and the baseline is more accurately a "geometry-plus-universal-response" baseline. The honest statement is that $\Gamma$ separates geometric normalisation ($L_g$, $d$) from response normalisation ($\lambda_L$), and only the former is varied in a strict G-only study. A second objection: the SQIF bandwidth and $\omega\tau$ results are kinematic bookkeeping, not predictions—they restate published spans in dimensionless form. This is true, but the re-entry exercise of the QNFO framework asks precisely which observables are fixed by geometry alone, and dimensionless ratios are the cleanest test: they are invariant under changes of units and of pairing mechanism.

**Open questions.** (1) What is the correct prefactor of the vortex-entry threshold when the full barrier analysis of [8] is included, and how does it depend on $\Gamma$? (2) Does the quasi-one-dimensional phase diagram of population-imbalanced mixtures [4] admit a geometric-only normalisation of its phase boundaries, given that the Zeeman term is a non-geometric input? (3) Can the multi-band and Lifshitz-transition physics of [5] be reduced to an effective geometric constraint on the Fermi-surface topology, or is it irreducibly material-specific? (4) The QNFO corpus entries [9], [10] supply no summary text here; the precise formal content of the "geometric unification" must be drawn from those documents directly, and this paper's baseline should be checked against that formalism.

## 7. Conclusion

We have constructed and quantified a G-only baseline for the QNFO geometric unification framework: a description of confined superconducting systems that retains only geometric lengths, the penetration depth, and the flux quantum. The baseline yields a confinement parameter $\Gamma$ (computed: $0.40$ for the assumed $R = 1\ \mu$m, $d = 50$ nm, $\lambda_L = 100$ nm disk), a model vortex-entry threshold $H_0^{(G)} \approx 0.66$ mT scaling as $R^{-2}$, a dimensionless SQIF mixing span of $4.30$ orders of magnitude, and a coherence phase-space product $\omega\tau = 3.14\times10^6$ for cavity-coupled qubits. It deliberately excludes critical temperatures and material-specific nonlinear relaxation, which the literature shows require band-structure and history-dependent inputs. The baseline's value is as a null hypothesis: any pairing-driven or material-driven extension of the geometric framework must beat it on the geometry-dominated observables identified here, and the falsification conditions we state make that test concrete.

## References

[1] arXiv:1603.03851v3 | Superconductivity driven by pairing of the coherent parts of the physical electrons

[2] arXiv:1608.06329v2 | Relaxation of Microwave Nonlinearity in a Cuprate Superconducting Resonator

[3] arXiv:1811.11656v1 | Superconductivity in SrTiO$_{3}$: dielectric function method for non-parabolic bands

[4] arXiv:1710.01668v1 | Phase transitions in quasi-one dimensional system with unconventional superconductivity

[5] arXiv:1712.06027v2 | Lifshitz transitions in multi-band Hubbard models for topological superconductivity in complex quantum matter

[6] arXiv:1409.3245v1 | Copper waveguide cavities with reduced surface loss for coupling to superconducting qubits

[7] arXiv:cond-mat/0608562v1 | Two tone response in Superconducting Quantum Interference Filters

[8] arXiv:0807.5129v1 | Geometrical barriers and the growth of flux domes in thin ideal superconducting disks

[9] QNFO: Superconductivity Quadrangle | DOI 10.5281/zenodo.18496889

[10] QNFO: Geometric Unification Framework | DOI 10.5281/zenodo.17074726