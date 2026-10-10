# Geometric Confinement as a G-Only Baseline for Superconducting Device Phenomenology: A Re-Entry Analysis of the QNFO Geometric Unification Framework

## Abstract

This paper develops a "G-only" baseline: a minimal, geometry-only description of superconducting device phenomenology in which every field-scale quantity is set by geometric confinement factors rather than by material-specific pairing physics. The baseline is motivated by the QNFO Geometric Unification Framework (DOI 10.5281/zenodo.17074726) and its companion corpus, the QNFO Superconductivity Quadrangle (DOI 10.5281/zenodo.18496889), and is constructed as a remediation re-entry of the framework into the device literature. We survey eight arXiv works spanning unconventional pairing, microwave nonlinearity in cuprate resonators, dielectric-function treatments of SrTiO$_3$, quasi-one-dimensional population-imbalanced systems, multi-band Lifshitz physics, copper waveguide cavities for qubits, two-tone mixing in Superconducting Quantum Interference Filters, and geometrical barriers to flux-dome growth in thin disks. From this survey we extract three device-level observables that a geometry-only model can address: intermodulation frequencies, flux-dome growth in thin disks, and field-participation-limited loss in confined cavities. We derive each observable with fully shown arithmetic under explicitly stated assumptions, obtaining for example a dome radius $b/R = (\mu_0 H_a/B^*)^{1/3}$ under a stated confinement law, a vortex count $N \approx 3.80\times10^{5}$ for a $100\,\mu\text{m}$ disk at $0.025\,\text{T}$, and a confinement loss-suppression factor of $1.89$ for a cavity with field-decay parameter $\eta = 0.05$. The baseline is a null hypothesis: any claim that material pairing physics is essential must beat it.

## 1. Introduction

The central question of this paper is deliberately narrow: how much of superconducting device phenomenology can be reproduced by geometry alone? We call this the geometric-confinement-only, or "G-only," baseline. The question originates in the QNFO research program, recorded as a re-entry from the Superconductivity Quadrangle corpus (DOI 10.5281/zenodo.18496889) under the heading "geometric confinement (G-only baseline)," and grounded in the companion Geometric Unification Framework (DOI 10.5281/zenodo.17074726). Neither corpus record supplies a summary text in the grounding block; we therefore treat them as framing documents whose specific content we do not assert beyond their titles and identifiers, and we build the baseline from first principles here.

The motivation for a G-only baseline is methodological. Superconducting devices — resonators, cavities, interferometric filters, thin-film disks — exhibit phenomenology (threshold fields, flux distributions, nonlinear mixing frequencies, loss budgets) that is strongly shaped by the geometry of the superconductor and of the electromagnetic field distribution. If a geometry-only model already reproduces a given observable to within its experimental tolerance, then that observable cannot be used as evidence for a specific microscopic pairing mechanism. Conversely, observables that demonstrably resist a G-only description are the ones that carry information about the condensate itself. The baseline thus functions as a null hypothesis against which material-specific claims must be tested.

We restrict ourselves to what the supplied literature entries actually state. The eight arXiv works in the bibliography are described only by their titles and abstract excerpts; we cite each for exactly what its excerpt asserts and no more. Where an excerpt is truncated or thin, we say so explicitly and use the work only at the level of its stated scope. All quantitative content in this paper is either (i) arithmetic performed in Section 4 from inputs stated there, or (ii) a projection under explicitly labeled assumptions with stated uncertainty bounds. We report no experimental measurements of our own and no simulation results.

The paper is organized as follows. Section 2 reviews the eight arXiv works and the two QNFO corpus records. Section 3 defines the G-only baseline formally. Section 4 carries out the derivations with full arithmetic. Section 5 reports the computed results. Section 6 discusses limitations, failure modes, and falsification criteria. Section 7 concludes.

## 2. Background and Related Work

We discuss each bibliography entry in its exact supplied numbering, restricting every statement to what the entry's own title and summary text support.

**[1] arXiv:1603.03851v3 — Superconductivity driven by pairing of the coherent parts of the physical electrons.** The summary states that how superconductivity in unconventional superconductors emerges from diverse mother normal states is "still a big puzzle," and that whatever the mother normal states are, the superconductivity is *normal*, with BCS-like behaviors of the paired quasiparticles in condensation; the authors revisit the problem to reconcile the diverse mother states with this normal superconductivity. For our purposes this is the canonical statement of the universality puzzle: many distinct normal states feed into one BCS-like condensate phenomenology. A G-only baseline is a complementary reduction at the device level — it asks whether even the device phenomenology is more universal than the materials suggest.

**[2] arXiv:1608.06329v2 — Relaxation of Microwave Nonlinearity in a Cuprate Superconducting Resonator.** The summary reports that the second- and third-order nonlinear microwave response of a superconducting YBa$_2$Cu$_3$O$_7$ thin-film resonator was synchronously measured using three input tones, that this permits local measurement and hence mapping of intermodulation distortion (IMD) inside the resonator, and that second- and third-order IMD measured with a fixed probe relaxed in remarkably different ways after removal of a static magnet. This is directly relevant to our baseline: IMD is a device-level nonlinear observable, and its spatial map is exactly the kind of quantity a geometry-only model would attempt to reproduce from the resonator's field geometry alone. The reported differential relaxation of second- versus third-order IMD is a candidate observable that may resist a G-only description, since it tracks a memory of magnetic history rather than instantaneous geometry.

**[3] arXiv:1811.11656v1 — Superconductivity in SrTiO$_3$: dielectric function method for non-parabolic bands.** The summary states that the dielectric function method for superconductivity was applied to SrTiO$_3$ accounting for the non-parabolic dispersion of charge carriers in the conduction band and for the dispersion of optical phonons based on density functional theory calculations, and that the obtained critical temperatures agree with experiments in the density regime (the excerpt truncates here). The entry supplies no numerical critical temperatures, so we cite it only as an example of a band-structure-sensitive pairing calculation; it plays no role in our arithmetic.

**[4] arXiv:1710.01668v1 — Phase transitions in quasi-one dimensional system with unconventional superconductivity.** The summary describes a study of superconducting properties of population-imbalanced fermionic mixtures in quasi-one-dimensional optical lattices, effectively described by an attractive Hubbard model with a Zeeman magnetic field term, with the ground-state phase diagram investigated as a function of chemical potential and magnetic field (the excerpt truncates). Quasi-one-dimensionality is itself a geometric confinement; the entry supports citing this work as a setting where reduced dimensionality — a purely geometric attribute — controls the phase diagram, which is the qualitative spirit of the G-only hypothesis.

**[5] arXiv:1712.06027v2 — Lifshitz transitions in multi-band Hubbard models for topological superconductivity in complex quantum matter.** The summary frames the resistance of macroscopic quantum coherence to decoherence as a major 21st-century challenge, notes that the Superstripes 2017 conference held in Ischia in June 2017 focused on the new physics of high-$T_c$ superconductors made of complex quantum matter, and discusses the standard model of high-$T_c$ superconductivity (the excerpt truncates mid-sentence). The supplied text gives no specific Lifshitz-transition results, so we cite it only for its stated framing of coherence-versus-decoherence and complex quantum matter; no technical content is attributed to it.

**[6] arXiv:1409.3245v1 — Copper waveguide cavities with reduced surface loss for coupling to superconducting qubits.** The summary states that significant improvements in superconducting qubit coherence times have been achieved with three-dimensional microwave waveguide cavities coupled to transmon qubits, that many measurements used superconducting aluminum cavities, and that other work involved qubits coupled to copper cavities with coherence times approaching $0.1\,\text{ms}$ (the excerpt truncates). This is a key device entry for our baseline: three-dimensional cavity geometry is precisely a geometric confinement of the microwave field, and the reported coherence improvement is the kind of observable a field-participation model (Section 4.3) addresses. The $0.1\,\text{ms}$ figure is quoted from the entry, not derived by us.

**[7] arXiv:cond-mat/0608562v1 — Two tone response in Superconducting Quantum Interference Filters.** The summary reports that the parabolic shape of the dc voltage output dip around $B=0$ of a Superconducting Quantum Interference Filter (SQIF) was exploited to mix weak external rf signals, and that the two-tone response of weak time-harmonic fields was detected on the spectral voltage output at frequency $f_0 = f_1 - f_2$, for various $f_1$ and $f_2$ ranging from a few MHz up to $20\,\text{GHz}$. The stated mixing relation $f_0 = f_1 - f_2$ is a device-level algebraic identity, independent of microscopic pairing physics; we use it in Section 4.1 as the cleanest example of a G-only observable.

**[8] arXiv:0807.5129v1 — Geometrical barriers and the growth of flux domes in thin ideal superconducting disks.** The summary states that when an ideal (no bulk pinning) flat type-II superconducting disk is subjected to a perpendicular magnetic field $H_a$, the first vortex nucleates at the rim when $H_a = H_0$, the threshold field, and moves quickly to the center; as $H_a$ increases above $H_0$, additional vortices join and produce a domelike field distribution of radius $b$, and the paper presents an analysis (the excerpt truncates). This is the most directly geometric entry in the bibliography: the entire phenomenology — rim nucleation, threshold field $H_0$, dome radius $b$ — is named after geometrical barriers. It anchors our flux-dome model in Section 4.2. The entry supplies no numerical values for $H_0$ or $b$, so our dome calculations are model projections, not reproductions of this work's numbers.

**[9] QNFO: Superconductivity Quadrangle (DOI 10.5281/zenodo.18496889).** The grounding block supplies only the title and DOI; no summary text is provided. We therefore cite it solely as the corpus from which the research idea ("re-entry ... geometric confinement (G-only baseline)") originates, and assert nothing about its internal content.

**[10] QNFO: Geometric Unification Framework (DOI 10.5281/zenodo.17074726).** Likewise, only the title and DOI are supplied. We cite it as the named framework that motivates the G-only hypothesis — the title itself asserts a geometric unification — and we do not attribute any specific result, formula, or dataset to it, because the supplied entry contains none.

Taken together, the bibliography supports a three-tier structure: microscopic pairing universality [1], [3], [4], [5]; device-level nonlinear and loss phenomenology [2], [6], [7]; and explicitly geometric flux phenomenology [8]. The G-only baseline is an attempt to connect the second and third tiers without importing the first.

## 3. Methods

### 3.1 Definition of the G-only baseline

We define a device observable $O$ to be *G-reproducible* if there exists a function of geometry alone, $O = F_G(\mathcal{G})$, where $\mathcal{G}$ denotes the set of geometric parameters (radii, thicknesses, aspect ratios, boundary shapes), that reproduces $O$ within a stated tolerance. The G-only baseline for a device class is the family of all such $F_G$ constructed without material pairing parameters. Formally, for a candidate observable $O$ with material-dependent parameters $\mathcal{M}$, the baseline asserts

$$O = F_G(\mathcal{G}) + \Delta_{\mathcal{M}}, \qquad |\Delta_{\mathcal{M}}| \le \epsilon,$$

where $\epsilon$ is the experimental tolerance. The scientific use of the baseline is falsification: if $|\Delta_{\mathcal{M}}| > \epsilon$ is demonstrated, the observable carries material information.

### 3.2 Model classes

We construct three minimal G-only models corresponding to three device classes represented in the bibliography:

1. **Algebraic mixing (SQIF-type, after [7]).** The two-tone output frequency is $f_0 = f_1 - f_2$. This is geometry-independent in the strongest sense — it is fixed by the input tones and the mixing nonlinearity's leading order — and serves as the trivially G-reproducible case.

2. **Flux-dome growth (disk-type, after [8]).** For an ideal thin type-II disk of radius $R$ under perpendicular applied field $H_a$, we posit a confinement law for the mean induction inside the dome,

$$B_d = B^* \left(\frac{b}{R}\right)^{\gamma},$$

with $B^*$ the induction at which the dome reaches the rim ($b = R$) and $\gamma > 0$ a geometric exponent. Flux conservation (all applied flux confined within the dome) gives $\mu_0 H_a \pi R^2 = B_d \pi b^2$. Both $\gamma$ and $B^*$ are stated assumptions of the model, not measurements.

3. **Field-participation loss (cavity-type, after [6]).** For a cavity confining microwave field energy with a fraction $p_s$ in the lossy surface region and $1 - p_s$ elsewhere, the effective loss rate is

$$\kappa_{\text{eff}} = p_s\,\kappa_s + (1 - p_s)\,\kappa_c,$$

with $\kappa_s$ the surface loss rate and $\kappa_c$ the (much smaller) bulk/conductor loss rate. The participation $p_s$ is set by geometry through a field-decay parameter $\eta$: we assume the field energy outside the ideal confinement volume is a fraction $\eta$ of the inside energy, so $p_s = 1/(1 + \eta)$.

### 3.3 Constants and inputs

All arithmetic uses the following inputs, stated here once. The flux quantum is taken as $\Phi_0 = 2.07\times10^{-15}\,\text{Wb}$ (assumed constant of the model). Disk radius $R = 100\,\mu\text{m} = 1.00\times10^{-4}\,\text{m}$. Applied fields $\mu_0 H_a \in \{0.025, 0.050, 0.100\}\,\text{T}$. Confinement exponent $\gamma = 1$ and rim induction $B^* = 0.100\,\text{T}$ (assumed). Cavity field-decay parameter $\eta \in \{0.05, 0.20\}$ and loss-rate ratio $\kappa_s/\kappa_c = 100$ (assumed). Mixing tones $f_1 = 5.00\,\text{GHz}$, $f_2 = 4.99\,\text{GHz}$ (within the few-MHz-to-$20\,\text{GHz}$ range stated in [7]).

## 4. Analysis

### 4.1 Mixing frequency (input: [7], stated relation $f_0 = f_1 - f_2$)

Inputs: $f_1 = 5.00\times10^{9}\,\text{Hz}$, $f_2 = 4.99\times10^{9}\,\text{Hz}$.

$$f_0 = f_1 - f_2 = 5.00\times10^{9} - 4.99\times10^{9} = 1.00\times10^{7}\,\text{Hz} = 10.0\,\text{MHz}.$$

This is exact arithmetic on the stated relation; no model assumption beyond the mixing order is involved.

### 4.2 Flux-dome growth (model of Section 3.2, item 2)

Step 1 — solve for the dome radius. Substituting $B_d = B^*(b/R)^{\gamma}$ into flux conservation $\mu_0 H_a R^2 = B_d\, b^2$:

$$\mu_0 H_a R^2 = B^*\left(\frac{b}{R}\right)^{\gamma} b^2 = B^*\, b^{\gamma+2}\, R^{-\gamma}.$$

Solving for $b$:

$$b^{\gamma+2} = \frac{\mu_0 H_a}{B^*} R^{\gamma+2} \quad\Longrightarrow\quad \frac{b}{R} = \left(\frac{\mu_0 H_a}{B^*}\right)^{1/(\gamma+2)}.$$

With the assumed $\gamma = 1$, the exponent is $1/(\gamma+2) = 1/3$.

Step 2 — evaluate at each stated field.

- $\mu_0 H_a = 0.025\,\text{T}$: $\mu_0 H_a / B^* = 0.025/0.100 = 0.250$; $(0.250)^{1/3} = 0.6300$. Check: $0.6300^3 = 0.6300 \times 0.6300 = 0.3969$; $0.3969 \times 0.6300 = 0.2501 \approx 0.250$. So $b = 0.630\,R = 6.30\times10^{-5}\,\text{m} = 63.0\,\mu\text{m}$.
- $\mu_0 H_a = 0.050\,\text{T}$: ratio $= 0.500$; $(0.500)^{1/3} = 0.7937$. Check: $0.7937^3 = 0.7937\times0.7937 = 0.6300$; $0.6300\times0.7937 = 0.5000$. So $b = 79.4\,\mu\text{m}$.
- $\mu_0 H_a = 0.100\,\text{T}$: ratio $= 1.000$; $(1.000)^{1/3} = 1.000$, so $b = R = 100\,\mu\text{m}$: the dome reaches the rim, consistent with the definition of $B^*$.

Step 3 — vortex count. The number of vortices inside the dome, assuming each carries flux $\Phi_0$ and the dome induction is uniform at $B_d$:

$$N = \frac{B_d\,\pi b^2}{\Phi_0}.$$

By flux conservation $B_d \pi b^2 = \mu_0 H_a \pi R^2$, so $N = \mu_0 H_a \pi R^2 / \Phi_0$ independent of $\gamma$. At $\mu_0 H_a = 0.025\,\text{T}$:

$$\mu_0 H_a \pi R^2 = 0.025 \times 3.14159 \times (1.00\times10^{-4})^2 = 0.025 \times 3.14159 \times 1.00\times10^{-8} = 7.854\times10^{-10}\,\text{Wb},$$

$$N = \frac{7.854\times10^{-10}}{2.07\times10^{-15}} = 3.794\times10^{5}.$$

Check: $2.07\times10^{-15} \times 3.794\times10^{5} = 7.854\times10^{-10}$. So $N \approx 3.79\times10^{5}$ vortices at $0.025\,\text{T}$; scaling linearly, $N \approx 7.59\times10^{5}$ at $0.050\,\text{T}$ and $N \approx 1.52\times10^{6}$ at $0.100\,\text{T}$ (each is exactly double the previous, since $N \propto H_a$).

Step 4 — dome mean induction. At $\mu_0 H_a = 0.025\,\text{T}$, $b/R = 0.6300$, so $B_d = B^*(b/R) = 0.100 \times 0.6300 = 0.0630\,\text{T}$. Cross-check via flux conservation: $B_d = \mu_0 H_a (R/b)^2 = 0.025 \times (1/0.6300)^2 = 0.025 \times 2.5195 = 0.0630\,\text{T}$. The two routes agree.

### 4.3 Field-participation loss (model of Section 3.2, item 3)

Inputs: $\kappa_s/\kappa_c = 100$; $\eta \in \{0.05, 0.20\}$; $p_s = 1/(1+\eta)$.

Case $\eta = 0.05$: $p_s = 1/1.05 = 0.95238$; $1 - p_s = 0.04762$.

$$\frac{\kappa_{\text{eff}}}{\kappa_c} = p_s \cdot 100 + (1 - p_s) = 95.238 + 0.04762 = 95.286.$$

Case $\eta = 0.20$: $p_s = 1/1.20 = 0.83333$; $1 - p_s = 0.16667$.

$$\frac{\kappa_{\text{eff}}}{\kappa_c} = 83.333 + 0.16667 = 83.500.$$

Reference case (no geometric confinement, field energy split equally): $p_s = 0.5$, giving $\kappa_{\text{eff}}/\kappa_c = 50 + 0.5 = 50.5$.

Suppression factor relative to the unconfined case:

$$S_{0.05} = \frac{50.5}{95.286} = 0.5298, \qquad S_{0.20} = \frac{50.5}{83.500} = 0.6048.$$

Equivalently, the unconfined-to-confined loss ratio is $95.286/50.5 = 1.887$ for $\eta = 0.05$ and $83.500/50.5 = 1.653$ for $\eta = 0.20$. Check: $50.5 \times 1.887 = 95.29 \approx 95.286$; $50.5 \times 1.653 = 83.48 \approx 83.500$ (rounding at the third digit).

### 4.4 Sensitivity of the dome exponent

The exponent $1/(\gamma+2)$ depends on the assumed $\gamma$. For $\gamma = 0$ (uniform induction, no confinement gradient) the exponent is $1/2$: at $\mu_0 H_a = 0.025\,\text{T}$, $(0.250)^{1/2} = 0.5000$, giving $b = 50.0\,\mu\text{m}$ instead of $63.0\,\mu\text{m}$. For $\gamma = 2$ the exponent is $1/4$: $(0.250)^{1/4} = 0.7071$, giving $b = 70.7\,\mu\text{m}$. The spread across $\gamma \in \{0,1,2\}$ at fixed field is $50.0$–$70.7\,\mu\text{m}$, i.e., roughly $\pm 20\%$ about the $\gamma=1$ value; we carry this as the uncertainty band of the projection.

## 5. Results

All numbers below are computed in Section 4 or are labeled projections with stated assumptions.

**R1 (exact, from the relation stated in [7]).** For input tones $f_1 = 5.00\,\text{GHz}$ and $f_2 = 4.99\,\text{GHz}$, the two-tone output frequency is $f_0 = 10.0\,\text{MHz}$. This observable is G-reproducible trivially: it depends only on the input tones.

**R2 (projection, assumptions: confinement law $B_d = B^*(b/R)^{\gamma}$ with $\gamma = 1$, $B^* = 0.100\,\text{T}$; flux conservation).** For a thin ideal disk of radius $R = 100\,\mu\text{m}$:

| $\mu_0 H_a$ (T) | $b/R$ | $b$ ($\mu\text{m}$) | $B_d$ (T) | $N$ |
|---|---|---|---|---|
| $0.025$ | $0.630$ | $63.0$ | $0.0630$ | $3.79\times10^{5}$ |
| $0.050$ | $0.794$ | $79.4$ | $0.0794$ | $7.59\times10^{5}$ |
| $0.100$ | $1.000$ | $100.0$ | $0.100$ | $1.52\times10^{6}$ |

Uncertainty band from the exponent sensitivity of Section 4.4: at $\mu_0 H_a = 0.025\,\text{T}$, $b \in [50.0, 70.7]\,\mu\text{m}$ for $\gamma \in [0, 2]$. The vortex count $N$ is independent of $\gamma$ (shown in Section 4.2, Step 3) and inherits only the uncertainty of $\Phi_0$, $R$, and $H_a$ as stated inputs.

**R3 (projection, assumptions: $p_s = 1/(1+\eta)$, $\kappa_s/\kappa_c = 100$).** Cavity loss suppression under geometric confinement:

| $\eta$ | $p_s$ | $\kappa_{\text{eff}}/\kappa_c$ | Suppression vs. unconfined ($p_s = 0.5$) |
|---|---|---|---|
| $0.05$ | $0.952$ | $95.29$ | factor $1.89$ lower loss |
| $0.20$ | $0.833$ | $83.50$ | factor $1.65$ lower loss |

**R4 (classification).** Under the G-only baseline, the mixing frequency (R1) is exactly geometry-independent; the flux-dome radius and vortex count (R2) are reproducible by a two-parameter geometric law; the cavity loss budget (R3) is reproducible by a one-parameter participation model. None of these three observables, at the level of the quantities computed here, requires a material pairing parameter.

## 6. Discussion

**Limitations of the models.** The flux-dome model of R2 is a two-parameter fit ($\gamma$, $B^*$) whose parameters we assumed, not derived from [8] or measured. The supplied summary of [8] describes rim nucleation at a threshold $H_0$ and domelike growth qualitatively but gives no functional form for $b(H_a)$; our power law is one admissible ansatz among many, and the $\pm 20\%$ band from exponent sensitivity (Section 4.4) is almost certainly an underestimate of the true model uncertainty, since it varies only $\gamma$ and holds $B^*$ fixed. In particular, the summary of [8] states that the first vortex nucleates at the rim at $H_a = H_0$; our model has no explicit $H_0$ and therefore cannot predict the threshold itself — a clear gap between the G-only ansatz and the phenomenon as described.

**Failure modes.** Three ways the baseline can fail: (i) *Nonlinear memory.* The summary of [2] reports that second- and third-order intermodulation in a cuprate resonator relaxed in remarkably different ways after removal of a static magnet. A purely geometric instantaneous model has no memory variable and cannot produce differential relaxation; this is the strongest candidate in our survey for an observable that resists G-only description. (ii) *Material-set thresholds.* The threshold field $H_0$ in [8] and the critical temperatures in [3] are quantities where material physics plausibly enters; our baseline does not address them. (iii) *Participation-model oversimplification.* R3 assumes a single lossy surface region and a fixed ratio $\kappa_s/\kappa_c = 100$; real cavities have distributed losses, and the summary of [6] attributes coherence improvements to reduced surface loss in three-dimensional cavities without giving loss ratios, so the factor-$1.89$ suppression is a model output, not a comparison with any measured value.

**What would falsify the claims.** The central claim — that the three observables computed here are G-reproducible — would be falsified if: for R1, a device were shown to mix at a frequency not equal to $f_1 - f_2$ (or its higher-order combinations) at the same drive conditions; for