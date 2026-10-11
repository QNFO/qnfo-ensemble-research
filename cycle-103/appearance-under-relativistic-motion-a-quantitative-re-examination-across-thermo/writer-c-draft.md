# Apparent Invariance of Atmospheric Re-Entry Under Relativistic Observer Motion: A Kinematic and Thermodynamic Analysis

## Abstract

We ask whether the phenomenology of atmospheric re-entry — the heating of a body entering a planetary atmosphere at high speed — appears invariant to an observer moving at relativistic speeds relative to the re-entry frame. We model re-entry as a moving thermal system characterized by an emitted temperature $T_0$, a radiating surface, and a finite event duration, and we transform each observable to a boosted observer frame using standard special-relativistic kinematics: the Doppler factor, bolometric beaming, and time dilation. We show analytically and numerically that the apparent temperature is strongly direction-dependent: for an observer at $\beta = 0.9$, the Doppler factor ranges from $D_{\mathrm{app}} \approx 4.36$ (approaching) to $D_{\mathrm{rec}} \approx 0.230$ (receding), a ratio of exactly $(1+\beta)/(1-\beta) = 19$, and the unresolved bolometric flux ratio scales as $D^4$, giving $\approx 361$ between the two directions. We further connect the result to the thermodynamic result that a moving system appears cooler [1], to drag on relativistically moving bodies in thermal radiation [3], and to the broader literature on relativistic appearance [5], [8]. We conclude that re-entry is not observer-invariant in any of its apparent (radiative, thermal, or temporal) observables; only Lorentz-invariant scalar combinations of the event parameters are observer-independent.

## 1. Introduction

The question motivating this paper, posed in the research idea underlying this preprint (re-entry from DOI 10.5281/zenodo.17861575), is whether the phenomenon of atmospheric re-entry appears invariant to an observer moving at relativistic speeds. "Re-entry" here denotes the passage of a body through a planetary atmosphere at high velocity, during which kinetic energy is dissipated as heat and radiation. "Appears invariant" means: does every observer, regardless of their own state of motion, measure the same values for the observable descriptors of the event — its apparent temperature, its radiative flux, its duration, and its directionality?

The question is well posed because special relativity guarantees invariance only for Lorentz scalars, not for observables that are components of four-vectors or tensors. Apparent temperature, apparent flux, and apparent duration are all frame-dependent quantities. The literature already contains strong evidence for this frame dependence in adjacent systems: numeric experiments in relativistic thermodynamics conclude that a moving thermal system appears cooler [1]; the drag force on a mirror moving relativistically through blackbody radiation is explicitly computed and is manifestly frame-dependent [3]; and the apparent velocity and Doppler factor of relativistic jets are known to depend strongly on viewing geometry [8]. Our contribution is to assemble these frame-dependent pieces into a single coherent account of re-entry as seen by a boosted observer, with explicit arithmetic.

We proceed as follows. Section 2 reviews the related literature. Section 3 defines the model: a re-entry event parameterized by an emitted temperature $T_0$, an event proper duration $\Delta \tau$, and a radiating area $A$, observed by an observer moving at speed $v = \beta c$ at viewing angle $\theta$ relative to the line of sight. Section 4 carries out the derivations with full arithmetic for a representative boost $\beta = 0.9$. Section 5 reports the computed results. Section 6 discusses limitations and failure modes, and Section 7 concludes.

## 2. Background and Related Work

We discuss eight works from the bibliography, in its numbering.

[1] presents numeric simulations of a two-dimensional relativistic ideal gas using a relativistic elastic binary collision algorithm, shows that the gas obeys Jüttner's speed distribution function, and — combining the simulation with the energy equipartition theorem for a relativistic gas — concludes that a moving system appears cooler. This is the central thermodynamic input to our analysis: if a moving thermal system appears cooler by a well-defined transformation, then the hot plasma sheath generated during re-entry cannot have an observer-invariant temperature. We adopt the qualitative conclusion of [1] (motion lowers apparent temperature) and combine it with the Doppler analysis of Section 4, which governs the directional (line-of-sight) part of the apparent temperature.

[2] reviews the Feynman-Vernon formulation of linear dissipative systems for a Brownian particle in an external potential $V(x,t)$ and introduces a generalized oscillator model of a Brownian particle coupled to a thermal environment moving with a given velocity $v_{env}$. This is directly relevant to re-entry: the re-entering body is, in effect, a particle coupled to a moving thermal environment (the atmosphere). The entry's summary is truncated mid-sentence and gives no further quantitative detail, so we use it only to establish that dissipation in a moving thermal environment is an actively studied formulation problem, and that the environment's velocity $v_{env}$ enters the model explicitly — which is precisely the frame-dependence we quantify.

[3] computes the drag force on a mirror moving at relativistic velocity relative to a blackbody radiation background. Although a mirror in a radiation bath is not an atmosphere, the structural lesson transfers: a body moving relativistically relative to a thermal field experiences a drag that exists only because of the relative motion, and whose magnitude is frame-dependent. Re-entry heating is the material-medium analogue: the "drag" is atmospheric, and the heating is the dissipative channel. The summary of [3] states the computation but supplies no numbers, so we cite it for the existence and frame-dependence of the effect only.

[4] addresses the interaction of short light pulses with objects moving at relativistic speeds, noting that polychromatic light-matter interaction is challenging to describe when the object moves with constant speed relative to the source, with light sails as a motivating application. For our problem, [4] establishes that even the illumination side of a relativistic encounter is nontrivial: a re-entering body observed from a relativistically moving platform is illuminated (and emits) polychromatically, and the apparent spectrum is shifted. The summary is truncated and gives no formulas, so we rely on it only for the problem statement.

[5] analytically obtains Rayleigh-Sommerfeld scalar diffraction results for apertures — single-slit, double-slit, grating, and circular — moving at relativistic speeds with velocities perpendicular to the direction of incidence, and also studies an oscillatory shutter. This matters for "appearance": if an observer at relativistic speed images the re-entry event through an aperture, the diffraction pattern itself is modified by the aperture's motion. The summary states the analytic results exist but is truncated before giving them, so we cite [5] as evidence that even the imaging channel is frame-dependent, without importing specific results.

[6] reviews particle acceleration in relativistic astrophysical jets with significant velocity shear, discusses the possible formation of power-law momentum spectra, and determines typical acceleration timescales for parallel and azimuthal shear flows. The relevance is structural: relativistic shear flows are the astrophysical cousin of the velocity-sheared flow around a re-entering body, and [6] shows that timescales measured in such flows are condition-dependent rather than invariant. The summary is truncated; we use only the stated scope.

[7] shows that although spin-momentum mixing under a boost can change the entanglement between spins of moving bodies (citing Gingrich and Adami), if the momenta are appropriately entangled, the entanglement between the spins of Bell states can remain maximal when viewed by any moving observer. This is the one clear counterexample in our bibliography to naive frame-dependence: with the right state preparation, a quantity can be made invariant for all moving observers. We invoke [7] to sharpen our claim: re-entry observables are not analogously protectable, because temperature, flux, and duration are not state-preparation-dependent discrete quantities but continuous thermodynamic and kinematic ones.

[8] numerically computes the apparent velocity and Doppler factor of a non-homokinetic jet under different velocity profiles to study the effect of collimation on the appearance of relativistic jets, arguing that if the motion is relativistic, the high (summary truncated). This is the closest methodological template for our work: [8] computes apparent observables of a relativistic system as a function of viewing geometry, exactly as we do for re-entry. The truncation prevents us from importing its specific conclusions; we use it to justify the Doppler-factor methodology of Section 4.

The four QNFO corpus entries — [9] Critical Examination of Spacetime, Mass, and Gravity through Competing Ontological Frameworks, [10] Relativistic Topological Superfluid, [11] Universe as Self-Proving Theorem, and [12] Winding Numbers and Strange Loops — are supplied with empty summaries. Their supplied text gives no further detail beyond the titles, so we cannot state what they contain or find. We note only that their titles indicate the corpus context in which this question was posed (competing ontological frameworks for spacetime, and relativistic matter systems), and we make no claim about their content.

## 3. Methods

### 3.1 Model of the re-entry event

We model the re-entry event in its rest frame (the frame in which the atmosphere is at rest, which we take as the "re-entry frame" $S$) by three parameters, all treated as free model parameters rather than measured values:

- $T_0$: the characteristic emitted temperature of the hot plasma sheath in frame $S$;
- $\Delta \tau$: the proper duration of the significant heating phase as measured in $S$;
- $A$: the effective radiating area of the sheath in $S$.

The observer moves at speed $v = \beta c$ relative to $S$, with Lorentz factor

$$\gamma = \frac{1}{\sqrt{1 - \beta^2}},$$

and views the event at angle $\theta$ between the observer's velocity and the line of sight to the event, measured in the observer's frame.

### 3.2 Observable transformations

We use three standard special-relativistic transformations, stated here as the model's rules:

1. **Apparent (Doppler) temperature.** The apparent temperature of a resolved thermal source is multiplied by the Doppler factor

$$D(\beta, \theta) = \frac{1}{\gamma (1 - \beta \cos\theta)}.$$

2. **Unresolved bolometric flux.** For an unresolved source, the observed bolometric flux gains a beaming factor $D^4$ relative to the flux that would be measured at rest at the same distance:

$$F_{\mathrm{obs}} = D^4 F_0.$$

3. **Duration.** The observed duration of the event is time-dilated:

$$\Delta t_{\mathrm{obs}} = \gamma \, \Delta \tau.$$

Additionally, per the conclusion of [1], a moving thermal system appears cooler; we treat this as the thermodynamic (equipartition) channel of temperature transformation, complementary to the Doppler (spectral) channel above. We do not assign a specific numerical coefficient from [1], since its summary states the conclusion but not the formula.

### 3.3 Invariance criterion

We declare the re-entry appearance "invariant" for a given observable $X$ if $X_{\mathrm{obs}}(\beta, \theta)$ is independent of $\beta$ and $\theta$. We test this for apparent temperature ($D$), flux ($D^4$), and duration ($\gamma$).

## 4. Analysis

All inputs in this section are either model parameters (declared as assumptions) or standard formulas stated in Section 3. No number is imported from an external measurement.

**Input 1 (assumption):** representative boost $\beta = 0.9$.

**Input 2 (assumption):** representative emitted temperature $T_0 = 2000\ \mathrm{K}$ (a model parameter; the qualitative conclusions below hold for any $T_0 > 0$).

**Input 3 (assumption):** representative proper duration $\Delta \tau = 100\ \mathrm{s}$ (model parameter).

**Step 1: Lorentz factor.**

$$\gamma = \frac{1}{\sqrt{1 - 0.9^2}} = \frac{1}{\sqrt{1 - 0.81}} = \frac{1}{\sqrt{0.19}} = \frac{1}{0.43589} \approx 2.2942.$$

**Step 2: Doppler factor, approaching ($\theta = 0$, $\cos\theta = 1$).**

$$D_{\mathrm{app}} = \frac{1}{\gamma(1 - \beta)} = \frac{1}{2.2942 \times (1 - 0.9)} = \frac{1}{2.2942 \times 0.1} = \frac{1}{0.22942} \approx 4.3589.$$

**Step 3: Doppler factor, receding ($\theta = \pi$, $\cos\theta = -1$).**

$$D_{\mathrm{rec}} = \frac{1}{\gamma(1 + \beta)} = \frac{1}{2.2942 \times 1.9} = \frac{1}{4.3589} \approx 0.22942.$$

Note the exact duality $D_{\mathrm{app}} = 1/D_{\mathrm{rec}}$, which follows because $\gamma^2 (1-\beta)(1+\beta) = \gamma^2(1-\beta^2) = 1$.

**Step 4: Anisotropy ratio of apparent temperature.**

$$\frac{T_{\mathrm{app}}}{T_{\mathrm{rec}}} = \frac{D_{\mathrm{app}} T_0}{D_{\mathrm{rec}} T_0} = \frac{D_{\mathrm{app}}}{D_{\mathrm{rec}}} = \frac{1+\beta}{1-\beta} = \frac{1.9}{0.1} = 19.$$

This ratio is exact and independent of $T_0$: the approaching observer sees the re-entry plasma 19 times hotter, in apparent temperature, than the receding observer at the same speed.

**Step 5: Apparent temperatures.**

$$T_{\mathrm{app}} = D_{\mathrm{app}} T_0 = 4.3589 \times 2000\ \mathrm{K} = 8717.8\ \mathrm{K},$$

$$T_{\mathrm{rec}} = D_{\mathrm{rec}} T_0 = 0.22942 \times 2000\ \mathrm{K} = 458.8\ \mathrm{K}.$$

**Step 6: Bolometric flux anisotropy.**

$$\frac{F_{\mathrm{app}}}{F_{\mathrm{rec}}} = \frac{D_{\mathrm{app}}^4}{D_{\mathrm{rec}}^4} = \left(\frac{1+\beta}{1-\beta}\right)^4 = 19^4 = 130321.$$

Compute $19^2 = 361$; $361^2 = 130321$. The unresolved bolometric flux differs by a factor of $1.30321 \times 10^5$ between the approaching and receding directions.

**Step 7: Absolute beaming factor (approaching).**

$$D_{\mathrm{app}}^4 = 4.3589^4 = (4.3589^2)^2 = 19.0000^2 = 361.00.$$

(Here $4.3589^2 = 19.0000$ exactly, since $D_{\mathrm{app}}^2 = 1/[\gamma^2(1-\beta)^2] = (1+\beta)/(1-\beta) = 19$.) So the approaching observer measures a bolometric flux $\approx 361$ times the rest-frame-equivalent value.

**Step 8: Duration dilation.**

$$\Delta t_{\mathrm{obs}} = \gamma \Delta \tau = 2.2942 \times 100\ \mathrm{s} = 229.42\ \mathrm{s}.$$

**Step 9: Transverse viewing ($\theta = \pi/2$, $\cos\theta = 0$).**

$$D_{\perp} = \frac{1}{\gamma} = \sqrt{1 - \beta^2} = \sqrt{0.19} \approx 0.43589,$$

$$T_{\perp} = 0.43589 \times 2000\ \mathrm{K} = 871.8\ \mathrm{K}.$$

**Step 10: Invariance test.** Since $D$ ranges over $[0.22942, 4.3589]$ as $\theta$ ranges over $[0, \pi]$ at fixed $\beta = 0.9$, and $D^4$ over $[2.77 \times 10^{-3}, 361.0]$ (with $0.22942^4 = (0.22942^2)^2 = 0.052634^2 \approx 2.77 \times 10^{-3}$), and $\gamma = 2.2942 \neq 1$, none of the three observables is independent of $(\beta, \theta)$. The re-entry appearance is not invariant.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions ($\beta = 0.9$, $T_0 = 2000\ \mathrm{K}$, $\Delta \tau = 100\ \mathrm{s}$); they scale with those parameters as indicated.

1. **Apparent temperature is not invariant.** At $\beta = 0.9$: $T_{\mathrm{app}} = 8717.8\ \mathrm{K}$ (approaching), $T_{\perp} = 871.8\ \mathrm{K}$ (transverse), $T_{\mathrm{rec}} = 458.8\ \mathrm{K}$ (receding). The approaching-to-receding ratio is exactly $19$, independent of $T_0$.

2. **Unresolved bolometric flux is not invariant.** The beaming factor $D^4$ spans $[2.77 \times 10^{-3}, 361.0]$ at $\beta = 0.9$; the directional flux ratio is $19^4 = 130321$.

3. **Duration is not invariant.** $\Delta t_{\mathrm{obs}} = \gamma \Delta \tau = 229.42\ \mathrm{s}$ for $\Delta \tau = 100\ \mathrm{s}$, i.e., a factor $\gamma = 2.2942$.

4. **Projection (stated assumptions):** for any other boost speed $\beta'$, the same formulas give a temperature anisotropy ratio $(1+\beta')/(1-\beta')$ and a flux ratio $[(1+\beta')/(1-\beta')]^4$; e.g., at $\beta' = 0.5$ the temperature ratio is $3$ and the flux ratio is $81$. These are exact algebraic consequences of the model rules in Section 3.2, not empirical projections.

5. **Qualitative result:** no apparent observable of the re-entry event (temperature, flux, duration) is invariant under relativistic observer motion; only Lorentz-scalar combinations of the event parameters would be, and none of the apparent observables studied here is a Lorentz scalar.

## 6. Discussion

**Limitations.** First, our model treats the re-entry sheath as a single-temperature thermal emitter observed via a simple Doppler factor. Real re-entry plasmas are optically thick in places, spatially structured, and non-equilibrium; the mapping from a sheath model to what an imager records would require radiative transfer that we have not performed, and works such as [4] and [5] indicate that even the polychromatic illumination and diffraction channels are nontrivial for relativistically moving objects. Second, the conclusion of [1] that a moving system appears cooler is stated in its summary as a conclusion from simulation plus equipartition, without the transformation formula; we therefore used it only qualitatively and relied on the Doppler channel for numbers. If the thermodynamic and Doppler temperature transformations conflict for some observer configuration, our two-channel treatment would need reconciliation — this is an open question. Third, our "re-entry" is a three-parameter abstraction ($T_0$, $\Delta \tau$, $A$); we make no claim about specific vehicles, planets, or missions, since the grounding input supplies none.

**Failure modes and falsification.** The central claim — non-invariance of apparent temperature, flux, and duration — would be falsified if one could exhibit an observer motion $(\beta, \theta)$-dependence-free definition of these observables that is also operationally measurable. The ratio $D_{\mathrm{app}}/D_{\mathrm{rec}} = (1+\beta)/(1-\beta)$ is exact algebra within the stated model, so falsification must attack the model rules (Section 3.2), e.g., by showing that the operationally defined apparent temperature of an extended, structured source does not transform with the point-source Doppler factor. A second falsification route: if the thermodynamic temperature transformation of [1] were found to exactly cancel the Doppler factor in all directions, the net apparent temperature could become invariant; our analysis shows the Doppler factor is strongly direction-dependent, so such an exact cancellation would itself be a remarkable directional result requiring proof.

**Against ourselves.** One might argue that "appearance invariance" should mean invariance of the underlying Lorentz-scalar description (four-momentum, invariant mass of the sheath, proper time), not of apparent observables — under that reading, re-entry is trivially "invariant" in the same sense all events are. We reject this reading as vacuous for the question posed, which is about what a moving observer *sees*; but we acknowledge the terminological risk. Another objection: the observer at $\beta = 0.9$ relative to a planet's atmosphere is a physically extreme scenario; we agree the scenario is idealized, but the question as posed is kinematic, and the algebra is speed-independent in form. Finally, [7] shows that in quantum information settings, appropriate state preparation can protect a quantity (spin entanglement of Bell states) from all moving observers; no analogous protection mechanism is available for continuous thermodynamic observables, but we cannot rule out that a cleverly defined re-entry observable (e.g., a specific spectral-line ratio) could be constructed to be boost-invariant — we flag this as an open question rather than a claim.

**Open questions.** (i) What is the exact transformation formula for the equipartition temperature derived in [1], and how does it compose with the Doppler factor? (ii) How do the results of [2] on a Brownian particle in an environment moving at $v_{env}$ quantify the dissipation channel for an atmospheric medium? (iii) Do the shear-flow timescales of [6] provide a useful analogue for the duration of the heating phase in a sheared sheath? The truncated summaries of [2], [4], [5], [6], and [8] prevent us from answering these from the supplied material.

## 7. Conclusion

Using standard relativistic transformations with fully shown arithmetic, we find that atmospheric re-entry, modeled as a thermal event with emitted temperature $T_0$, is not apparent-invariant to a relativistically moving observer: at $\beta = 0.9$ the apparent temperature varies by an exact factor of $19$ between approaching and receding lines of sight, the unresolved bolometric flux by a factor of $130321$, and the event duration by a factor of $\gamma = 2.2942$. This non-invariance is consistent with the frame-dependence found across the relativistic-appearance literature [1], [3], [5], [8], while the protected-entanglement result of [7] marks the boundary condition under which invariance can be engineered. We conclude that the answer to the motivating question is negative for all apparent observables studied, with the residual open question being whether some derived observable could be constructed to be invariant by design.

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