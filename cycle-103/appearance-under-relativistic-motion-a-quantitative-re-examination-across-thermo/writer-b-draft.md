# Appearance Invariance Under Relativistic Motion: A Quantitative Re-Examination of How Moving Systems Present to Moving Observers

## Abstract

A recurring question in relativistic physics is whether a physical system "appears" the same, or in any sense invariant, to an observer moving at relativistic speed relative to it. We re-frame this question operationally: invariance of what quantity, under which measurement protocol? We analyze three concrete appearance channels — thermodynamic appearance (apparent temperature of a moving gas and of a blackbody radiation field), radiative appearance (Doppler factor and radiation pressure on a moving mirror), and structural appearance (diffraction and jet morphology) — using only special-relativistic kinematics with fully shown arithmetic. For a representative speed $\beta_1 = 0.8$ we compute the Doppler factors $D_{+} = 3$ and $D_{-} = 1/3$, the two candidate temperature transformation outcomes $T_0/\gamma_1 = 0.6\,T_0$ and $\gamma_1 T_0 = 1.667\,T_0$, and the solid-angle-averaged apparent temperature of an isotropic blackbody field, $\bar{T} = 0.824\,T_0$, i.e. a net cooling of $17.6\%$. We also compute the idealized radiation pressure on a receding perfect mirror, $F_1/A = 0.1778\,u_0$, versus the static value $2u_0$, and a Jüttner tail suppression factor of $4.54\times10^{-5}$. Our conclusion: appearance is generically *not* invariant; only properly defined rest-frame quantities are. The literature supports this asymmetry from thermodynamic, field-theoretic, optical, and astrophysical directions.

## 1. Introduction

The question motivating this paper, posed in the grounding research idea, is whether a system can "appear invariant to an observer moving at relativistic speeds." The phrase "appear invariant" is ambiguous, and the ambiguity is the source of much confusion in discussions of relativistic thermodynamics and observation. An observer moving at speed $v_1 = \beta_1 c$ relative to a system receives signals that are Doppler shifted, time-dilated, aberrated, and — for extended objects — distorted by light-travel-time effects. Whether the system "appears" invariant therefore depends on which observable the observer extracts: a photon frequency, a fitted temperature, a shape, an entanglement entropy, or an apparent velocity.

Special relativity guarantees invariance of scalar quantities defined in the rest frame of the measured system, such as the proper temperature $T_0$ that a comoving thermometer would read. It does *not* guarantee that the quantities an observer actually reconstructs from received signals equal those rest-frame values. Indeed, a substantial literature exists precisely because they do not: numeric simulations of relativistic gases conclude that a moving system appears cooler [1]; field-theoretic models have been built for thermal environments that are themselves moving [2]; drag forces arise on mirrors moving relative to blackbody radiation [3]; light-matter interaction calculations become challenging when the object moves relativistically relative to the source [4]; diffraction patterns of moving apertures change [5]; particle acceleration timescales depend on the flow frame in relativistic shear flows [6]; entanglement between spins can change under a boost unless momenta are appropriately entangled [7]; and the apparent velocity and Doppler factor of relativistic jets depend strongly on collimation and viewing geometry [8].

This paper makes a narrow, verifiable contribution: we state explicit measurement protocols, derive the apparent observables with every arithmetic step shown, and quantify the departure from invariance at a fixed representative speed. We do not claim new physics; we claim a clarified and quantified answer to the appearance-invariance question, assembled from standard kinematics and consistent with the cited literature.

## 2. Background and Related Work

We discuss the eight arXiv works in the supplied bibliography. Four QNFO entries [9], [10], [11], [12] are supplied with empty summary text; we note that no substantive content from them can be used here, and we rely on them only as context labels for the broader ontological program (competing ontological frameworks of spacetime, mass, and gravity [9]; relativistic topological superfluids [10]; self-proving theorem universes [11]; winding numbers and strange loops [12]).

**[1] Numeric Experiments in Relativistic Thermodynamics: A Moving System Appears Cooler (arXiv:0804.3836v3).** This work simulates a two-dimensional relativistic ideal gas using a relativistic elastic binary collision algorithm, shows that the simulated gas faithfully obeys Jüttner's speed distribution function, and — combining the simulation with the energy equipartition theorem for a relativistic gas — concludes that a moving system appears cooler. This is the closest existing answer to our motivating question on the thermodynamic channel: the appearance (fitted temperature) of a moving gas is *not* invariant but reduced. Our Section 4 derives the corresponding kinematic factors analytically for a blackbody field and shows the same sign of effect (net cooling on angular average).

**[2] Feynman-Vernon model of a moving thermal environment (arXiv:1803.10300v1).** This paper reviews the Feynman-Vernon formulation of linear dissipative systems for a Brownian particle in an external potential $V(x,t)$ and introduces a generalized oscillator model of a Brownian particle coupled to a thermal environment moving with velocity $v_{\mathrm{env}}$. The relevance to our question is structural: if the thermal environment itself must be assigned a velocity $v_{\mathrm{env}}$ in the dissipative dynamics, then the environment's state as seen by the particle is frame-dependent — the moving environment does not appear thermally identical to a resting one. The supplied summary is truncated and gives no quantitative results, so we use it only as evidence that moving-thermal-environment models are an active formulation problem.

**[3] Blackbody radiation drag on a relativistically moving mirror (arXiv:0907.2311v1).** The authors compute the drag force on a mirror moving at relativistic velocity relative to a blackbody radiation background. This establishes that even the mechanical response of a body to an isotropic thermal field is appearance-dependent: in the mirror's frame the radiation field is anisotropic and exerts a net retarding force. Our Section 4 computes an idealized unidirectional-beam version of this effect with full arithmetic, obtaining a pressure strongly reduced from the static value at $\beta_1 = 0.8$.

**[4] Computing the interaction of light pulses with objects moving at relativistic speeds (arXiv:2404.05117v1).** This work addresses polychromatic light-matter interaction when the object moves at constant relativistic speed relative to the light source, motivated by optical traps, optical tweezers, and light sails, where relative speeds should reach the relativistic regime. It confirms that the optical appearance of an object (its response to incident light) is velocity-dependent and computationally nontrivial; the supplied summary is truncated before quantitative results, so we cite it as motivation for the optical channel of our analysis.

**[5] Rayleigh-Sommerfeld scalar diffraction by apertures moving at relativistic speeds (arXiv:2010.02547v2).** The authors analytically obtain Rayleigh-Sommerfeld scalar diffraction results for single-slit, double-slit, grating, and circular apertures moving at relativistic speeds with velocity perpendicular to the direction of incidence, and also study an oscillatory-shutter single slit. This is direct evidence that the *structural* appearance of an object (its diffraction signature) is not invariant under transverse relativistic motion. The summary is truncated before specific formulas, so we do not attribute numerical results to it.

**[6] Particle acceleration timescales in relativistic shear flows (arXiv:astro-ph/0506719v1).** This review discusses acceleration of energetic particles in relativistic astrophysical jets with significant velocity shear, the possible formation of power-law momentum spectra, and typical acceleration timescales for parallel and azimuthal shear flows, with special attention to parallel shear. It shows that even the *effective particle spectrum* produced by a flow is frame- and profile-dependent: the appearance of an acceleration environment differs across frames. The summary is truncated, so we use it qualitatively only.

**[7] Relativistic-invariant quantum entanglement between the spins of moving bodies (arXiv:quant-ph/0211159v2).** Building on the observation (attributed in the entry to Gingrich and Adami, Phys. Rev. Lett. 89, 270402 (2002)) that spin-momentum mixing can change spin entanglement for a moving observer, this paper shows that if the momenta are appropriately entangled, the entanglement between the spins of Bell states can remain maximal when viewed by any moving observer. This is the one clear *positive* invariance result in our bibliography — and it is instructive: invariance is achieved not for free but by a specific preparation condition (momentum entanglement). Appearance invariance, where it exists, is engineered, not generic.

**[8] The influence of collimation on the appearance of relativistic jets (arXiv:1010.5895v1).** The authors numerically compute the apparent velocity and Doppler factor of a non-homokinetic jet under different velocity profiles to study the effect of collimation on jet appearance, arguing that if the motion is relativistic, the high-... (summary truncated). Even truncated, the entry establishes that "appearance" quantities for relativistic motion (apparent velocity, Doppler factor) depend on the internal velocity distribution and collimation — i.e., appearance is a function of structure, not a frame-convention artifact alone.

**Synthesis.** Across thermodynamics [1], open quantum systems [2], mechanical drag [3], optical interaction [4], diffraction [5], astrophysical acceleration [6], quantum information [7], and jet astronomy [8], the consistent picture is: rest-frame quantities are invariant; received/reconstructed appearance quantities are not, except under special preparations [7]. Our contribution is to quantify the generic departure at a fixed speed with fully explicit arithmetic.

## 3. Methods

**Protocol definition.** We define an "appearance observable" $X_{\mathrm{app}}$ as any quantity an observer reconstructs from received signals (photon frequencies, fitted temperatures, pressures, diffraction patterns), and an "invariant observable" $X_{\mathrm{inv}}$ as a quantity defined in the system's rest frame (proper temperature $T_0$, proper length $L_0$, proper pressure). The invariance question is whether $X_{\mathrm{app}} = X_{\mathrm{inv}}$ for a moving observer.

**Kinematic inputs.** All derivations use only: (i) the Lorentz factor $\gamma(\beta) = (1-\beta^2)^{-1/2}$; (ii) the relativistic Doppler factor for a source/observer with line-of-sight velocity component $\beta_{\parallel}$, $D = 1/[\gamma(1-\beta_{\parallel})]$; (iii) photon number/momentum conservation at a moving mirror; (iv) the Jüttner exponential weight $\exp[-(\gamma_{\mathrm{p}}-1)mc^2/(k_B T)]$ for a particle of Lorentz factor $\gamma_{\mathrm{p}}$, which reference [1] reports their simulated gas obeys.

**Representative speed.** We fix $\beta_1 = 0.8$ throughout, a standard relativistic benchmark, and additionally compute the speed at which the forward Doppler factor reaches $D = 10$.

**Scope.** We treat flat spacetime only, inertial frames only, and idealized objects (perfect mirror, isotropic blackbody field, unidirectional monochromatic beam). All quantitative results in Section 5 are computed in Section 4; no simulation or experimental data are reported.

## 4. Analysis

All arithmetic is shown explicitly. We use $\beta_1 = 0.8$.

**A. Lorentz factor.**
$$\gamma_1 = \frac{1}{\sqrt{1-\beta_1^2}} = \frac{1}{\sqrt{1-0.64}} = \frac{1}{\sqrt{0.36}} = \frac{1}{0.6} = \frac{5}{3} \approx 1.6667.$$

**B. Doppler factors (longitudinal).** For motion directly toward the observer ($\beta_{\parallel} = -\beta_1$, approaching):
$$D_{+} = \frac{1}{\gamma_1(1-\beta_1)} = \frac{1}{(5/3)(0.2)} = \frac{1}{1/3} = 3.$$
For receding motion ($\beta_{\parallel} = +\beta_1$):
$$D_{-} = \frac{1}{\gamma_1(1+\beta_1)} = \frac{1}{(5/3)(1.8)} = \frac{1}{3}.$$
For transverse observation ($\beta_{\parallel} = 0$): $D_{\perp} = 1/\gamma_1 = 0.6$ (transverse Doppler redshift).

**C. Candidate temperature transformations.** Two candidate rules appear in the relativistic-thermodynamics literature; we compute both at $\beta_1 = 0.8$ for a rest temperature $T_0$:
$$T_{\mathrm{cool}} = \frac{T_0}{\gamma_1} = 0.6\,T_0, \qquad T_{\mathrm{hot}} = \gamma_1 T_0 = 1.6667\,T_0.$$
The ratio between the two candidates is $\gamma_1^2 = 25/9 \approx 2.778$. Reference [1] concludes the cooler branch is realized for a moving gas; our blackbody calculation below independently yields a net-cooling result on angular average.

**D. Apparent temperature of an isotropic blackbody field.** An observer moving at $\beta_1$ through an isotropic blackbody field of rest temperature $T_0$ measures, in a direction making angle $\theta$ with the velocity (photons arriving from direction $\theta$), an apparent temperature
$$T_{\mathrm{app}}(\theta) = \frac{T_0}{\gamma_1(1-\beta_1\cos\theta)}.$$
Forward direction ($\theta = 0$): $T_{\mathrm{app}} = T_0/[\gamma_1(1-\beta_1)] = 3T_0$. Backward ($\theta = \pi$): $T_{\mathrm{app}} = T_0/3$. The field therefore appears strongly anisotropic — not invariant.

Solid-angle average: with $\mu = \cos\theta$,
$$\langle D \rangle = \frac{1}{4\pi}\int \frac{d\Omega}{\gamma_1(1-\beta_1\mu)} = \frac{1}{\gamma_1}\cdot\frac{1}{2}\int_{-1}^{1}\frac{d\mu}{1-\beta_1\mu}.$$
The integral: $\int_{-1}^{1} \frac{d\mu}{1-\beta_1\mu} = \left[-\frac{1}{\beta_1}\ln(1-\beta_1\mu)\right]_{-1}^{1} = \frac{1}{\beta_1}\ln\frac{1+\beta_1}{1-\beta_1} = \frac{2}{\beta_1}\operatorname{atanh}\beta_1.$
So $\langle D \rangle = \frac{\operatorname{atanh}\beta_1}{\gamma_1\beta_1}$ and
$$\bar{T} = \frac{T_0\,\operatorname{atanh}\beta_1}{\gamma_1\beta_1}.$$
Numerically: $\operatorname{atanh}(0.8) = \tfrac{1}{2}\ln\frac{1.8}{0.2} = \tfrac{1}{2}\ln 9 = 1.0986$; $\gamma_1\beta_1 = (5/3)(0.8) = 4/3 \approx 1.3333$;
$$\bar{T} = T_0 \times \frac{1.0986}{1.3333} = 0.8240\,T_0.$$
The angularly averaged appearance of the field is *cooler* by $1 - 0.8240 = 0.1760$, i.e. $17.6\%$, in qualitative agreement with the "moving system appears cooler" conclusion of [1].

**E. Radiation pressure on a receding perfect mirror (idealized unidirectional beam).** Let a beam of energy density $u_0$ (in the source frame) strike a perfect mirror receding at $\beta_1$ along the beam. Photon arrival rate per unit mirror area is reduced by $(1-\beta_1)$; each photon of energy $h\nu$ reflects with frequency redshifted by the mirror Doppler factor $\nu_r/\nu = \frac{1-\beta_1}{1+\beta_1}$. Momentum transfer per photon:
$$\Delta p = \frac{h\nu}{c}\left(1 - \frac{\nu_r}{\nu}\right) = \frac{h\nu}{c}\left(1 - \frac{1-\beta_1}{1+\beta_1}\right) = \frac{h\nu}{c}\cdot\frac{2\beta_1}{1+\beta_1}.$$
Force per area:
$$\frac{F}{A} = u_0(1-\beta_1)\cdot\frac{2\beta_1}{1+\beta_1} = u_0\cdot\frac{2\beta_1(1-\beta_1)}{1+\beta_1}.$$
At $\beta_1 = 0.8$: numerator $2(0.8)(0.2) = 0.32$; denominator $1.8$;
$$\frac{F_1}{A} = u_0 \times \frac{0.32}{1.8} = 0.1778\,u_0.$$
For a static mirror ($\beta = 0$), $F_0/A = 2u_0$. The appearance of the beam's mechanical effect is therefore suppressed by a factor $0.1778/2 = 0.0889$ — an $89.1\%$ reduction. This idealized calculation is consistent in spirit with the full blackbody-drag computation of [3] (drag exists and is velocity-dependent); we do not claim numerical equality with that work's result, which its summary does not state.

**F. Jüttner tail suppression.** Reference [1] reports that a relativistic gas obeys Jüttner's speed distribution, whose Boltzmann weight for a particle of Lorentz factor $\gamma_{\mathrm{p}}$ is $\exp[-(\gamma_{\mathrm{p}}-1)mc^2/(k_B T_0)]$. For a cold gas with $k_B T_0 = 0.1\,mc^2$, the relative weight of particles at $\gamma_{\mathrm{p}} = 2$ versus $\gamma_{\mathrm{p}} = 1$ is
$$\frac{w(2)}{w(1)} = \exp\left[-\frac{(2-1)mc^2}{0.1\,mc^2}\right] = e^{-10} = 4.5400\times10^{-5}.$$
A moving observer fitting a temperature from such a distribution samples Doppler-shifted energies; the fitted value inherits the frame dependence demonstrated in D.

**G. Speed for $D = 10$.** For longitudinal approach, $D = \sqrt{\frac{1+\beta}{1-\beta}}$. Setting $D = 10$: $100 = \frac{1+\beta}{1-\beta} \Rightarrow 100 - 100\beta = 1 + \beta \Rightarrow \beta = \frac{99}{101} \approx 0.9802.$

## 5. Results

All numbers below are computed in Section 4 at $\beta_1 = 0.8$ unless stated.

1. **Doppler appearance factors:** $D_{+} = 3$ (approaching), $D_{-} = 1/3$ (receding), $D_{\perp} = 0.6$ (transverse). The forward/backward apparent-temperature ratio is $9$.
2. **Temperature-transformation candidates:** $T_0/\gamma_1 = 0.6\,T_0$ versus $\gamma_1 T_0 = 1.667\,T_0$; the candidates differ by a factor $\gamma_1^2 \approx 2.778$. The literature simulation [1] supports the cooler branch.
3. **Angularly averaged apparent temperature of an isotropic blackbody field:** $\bar{T} = 0.8240\,T_0$, a net cooling of $17.6\%$; locally, the field appears at $3T_0$ forward and $T_0/3$ backward.
4. **Idealized receding-mirror radiation pressure:** $F_1/A = 0.1778\,u_0$, versus $F_0/A = 2u_0$ at rest — a suppression factor of $0.0889$ ($89.1\%$ reduction).
5. **Jüttner tail suppression** for $k_B T_0 = 0.1\,mc^2$ at $\gamma_{\mathrm{p}} = 2$: $4.5400\times10^{-5}$.
6. **Speed for forward Doppler factor $D = 10$:** $\beta = 99/101 \approx 0.9802$.

**Projection (labeled as such).** If the angular-average cooling factor $\bar{T}/T_0 = \operatorname{atanh}\beta/(\gamma\beta)$ is taken as a proxy for thermodynamic appearance across speeds, then at $\beta = 0.5$ ($\gamma = 1.1547$, $\operatorname{atanh} 0.5 = 0.5493$): $\bar{T} = 0.5493/(1.1547\times0.5)\,T_0 = 0.9513\,T_0$ (cooling $4.9\%$); at $\beta = 0.99$ ($\gamma = 7.0888$, $\operatorname{atanh} 0.99 = 2.6467$): $\bar{T} = 2.6467/(7.0888\times0.99)\,T_0 = 0.3776\,T_0$ (cooling $62.2\%$). These are kinematic projections of the stated formula, not simulation results; their validity as thermodynamic appearance measures is an assumption, and the uncertainty is dominated by that assumption, not by arithmetic.

## 6. Discussion

**Main claim.** Appearance is generically not invariant under relativistic motion. Every channel examined — thermodynamic fit [1], dissipative environment response [2], mechanical radiation pressure [3], optical interaction [4], diffraction [5], acceleration environment [6], jet morphology [8] — is frame-dependent. The single positive invariance result in our corpus [7] required a special preparation (momentum entanglement), reinforcing that invariance is conditional, not generic.

**Limitations and failure modes.** (i) Our blackbody angular average (Result 3) is a specific protocol choice; a different weighting (e.g., energy-density-weighted rather than solid-angle-averaged temperature) gives a different number, so the "17.6% cooling" is protocol-relative. (ii) The mirror calculation (Result 4) uses a unidirectional monochromatic beam, not the isotropic blackbody background of [3]; the true drag on a mirror in an isotropic field involves angular integrals we did not perform, and our $0.1778\,u_0$ should not be compared numerically to that work. (iii) The identification of $\bar{T}$ with the thermodynamic "appears cooler" statement of [1] is an interpretive bridge, not a derivation: [1] used a collision-algorithm simulation and equipartition, a different route. (iv) We treated only inertial frames and flat spacetime; acceleration, gravity, and the ontological questions raised in the QNFO program [9], [10], [11], [12] (whose supplied summaries contain no usable content) are out of scope.

**What would falsify the claims.** A controlled simulation showing that a moving observer's fitted temperature of a relativistic gas equals $T_0$ to within statistical errors would falsify the cooling claim on the thermodynamic channel. A demonstration that the solid-angle-averaged Doppler factor equals unity at some $\beta > 0$ would falsify our formula — but the formula is elementary, so falsification would more plausibly target the *interpretation* (that the average is the relevant appearance observable). If entanglement-assisted invariance [7] generalized to thermodynamic quantities without special preparation, the framing of this paper would need revision.

**Open questions.** Which appearance observable, if any, is canonical? Does the cooling factor $\operatorname{atanh}\beta/(\gamma\beta)$ correspond to what an actual calorimetric measurement would yield? How do the diffraction results of [5] combine with the thermodynamic results of [1] for a moving, finite-temperature, structured object?

## 7. Conclusion

We asked whether a system appears invariant to a relativistically moving observer and answered quantitatively: no, on every channel examined, with the exception of specially prepared quantum states. At $\beta_1 = 0.8$, Doppler factors span $1/3$ to $3$, the angularly averaged apparent temperature of an isotropic field is $0.8240\,T_0$ (a $17.6\%$ cooling), and the idealized mechanical appearance of a light beam on a receding mirror is suppressed by a factor $0.0889$. Appearance invariance, where achievable, is engineered — as in the momentum-entangled Bell states of [7] — not automatic. The proper quantities of a system remain invariant; what an observer reconstructs from signals does not.

## References

[1] arXiv:0804.3836v3 | Numeric Experiments in Relativistic Thermodynamics: A Moving System Appears Cooler
[2] arXiv:1803.10300v1 | Feynman-Vernon model of a moving thermal environment
[3] arXiv:0907.2311v1 | Blackbody radiation drag on a relativistically moving mirror
[4] arXiv:2404.05117v1 | Computing the interaction of light pulses with objects moving at relativistic speeds
[5] arXiv:2010.02547v2 | Rayleigh-Sommerfeld scalar diffraction by apertures moving at relativistic speeds
[6] arXiv:astro-ph/0506719v1 | Particle acceleration timescales in relativistic shear flows
[7] arXiv:quant-ph/0211159v2 | Relativistic-invariant quantum entanglement between the spins of moving bodies
[8] arXiv:1010.5895v1 | The influence of collimation on the appearance of relativistic jets
[9] QNFO: Critical Examination of Spacetime, Mass, and Gravity through Competing Ontological Frameworks
[10] QNFO: Relativistic Topological Superfluid
[11] QNFO: Universe as Self-Proving Theorem
[12] QNFO: WINDING NUMBERS AND STRANGE LOOPS