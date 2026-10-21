# Discrete Scale Invariance Without a Universal Factor: Why the Efimov Data Refute Factor-2 Log-Periodicity Across Fundamental Physics

## Abstract

Discrete scale invariance (DSI) — invariance under rescaling by a fixed factor rather than by any factor — is established in few-body quantum physics, Dirac semimetals, and renormalization-group limit cycles. A recurring conjecture holds that the scaling factor itself might be universal, with the dyadic value 2 appearing across unrelated domains. This paper tests that conjecture against the published few-body and condensed-matter evidence. We model each confirmed DSI system as a log-periodic spectrum $E_n = E_0 \exp(-2\pi n/s_0)$ and extract the scaling factor from published values. The three-boson Efimov spectrum has scaling factor $22.694$, which we show corresponds to an RG index $s_0 = 2\pi/\ln(22.694) = 2.0127$ and a log-periodic period $\Delta(\ln E) = 3.1222$, i.e. $4.505$ octaves — a factor of $4.505$ larger than the dyadic period $\ln 2 = 0.69315$. Scaling traps realize continuously tunable factors controlled by the slope of a spatially varying scattering length, and spin-orbit-coupled three-boson systems obey a generalized scaling law in a five-dimensional parameter space, so no single factor is fixed. We conclude that DSI is real and broadly shared, but the specific factor-2 universality hypothesis is excluded by existing data at the level of a factor $11.347$ per spectral step. The practical consequence is a sharp falsification criterion: any claimed universal dyadic periodicity in a physical spectrum must survive comparison against the measured Efimov period of $3.1222$ in $\ln E$, which it cannot if the period is $0.69315$.

## 1. Introduction

Experimental groups measuring few-body bound states in ultracold atoms, transport in Dirac materials, and spectra near charged impurities all face the same analysis problem: when a spectrum repeats itself under rescaling, what is the scaling factor, and does it carry fundamental meaning? The answer determines whether an observed oscillation is a fingerprint of a specific microscopic boundary condition, a tunable property of an engineered trap, or evidence for a new symmetry of nature. Misreading the factor leads to misassigned mechanisms: a trap-engineered period can be mistaken for a universal constant, or a genuine Efimov tower can be fitted with the wrong period and yield wrong scattering parameters.

The stakes are concrete. In the cold-atom case, the atom-loss resonances that signal Efimov states occur at critical scattering lengths whose ratios encode the scaling factor; extracting that factor is the primary quantitative output of the experiment, and it feeds into determinations of three-body parameters used across the ultracold-atom community [4]. In Dirac semimetals, quasibound states around charged impurities affect transport, and whether their spectrum shows a discrete scaling symmetry under magnetic field determines what a magnetotransport measurement can reveal about the underlying Dirac Hamiltonian [1]. If a universal factor-2 discrete scaling symmetry governed fundamental physics, a single measured period in one domain would calibrate expectations in every other domain, and deviations would signal new physics. If instead each system carries its own factor — set by boundary conditions, trap geometry, or spin-orbit coupling — then every domain must be calibrated independently, and factor-2 claims in new data require their own dynamical explanation.

This paper resolves that question by extracting the scaling factors that the published literature actually reports and comparing them against the dyadic hypothesis. The comparison is decisive. The three-boson Efimov factor is $22.694$ [4], not $2$; the scaling-trap factor is continuously tunable through the slope of the scattering-length profile [2]; the Dirac-semimetal factors depend on magnetic-field regime and dimensionality [1]; and the log-periodic modulations proposed in quantum-gravity contexts carry an arbitrary period parameter $\omega$ [3]. The broader intuition behind the factor-2 conjecture — that discrete scaling loops can replace continuous scale invariance — has solid empirical support; the specific universal value does not.

The contributions of this paper are:

- A derivation, from the published Efimov scaling factor $22.694$ [4], of the renormalization-group index $s_0 = 2.0127$, the log-periodic period $\Delta(\ln E) = 3.1222$, and the octave count $4.505$, establishing quantitatively how far the confirmed few-body factor lies from the dyadic value (Section 4).
- A classification of confirmed discrete-scale-invariant systems by what fixes their scaling factor — boundary condition, trap slope, magnetic regime, or dynamical exponent — showing that in every cited system the factor is either non-dyadic or continuously adjustable (Sections 2 and 4).
- A falsification criterion for universal dyadic periodicity, stated as a measurable period in $\ln E$, together with the observation that factor 2 does appear in analysis conventions (dyadic partitions of frequency space [11]) and must therefore be distinguished from factor 2 as physics (Section 5).
- An assessment of what a viable research program on discrete scaling loops should claim — the existence and structure of log-periodicity, not the universality of its factor — and the smallest experimental test that would settle the matter for a new system (Sections 6 and 7).

## 2. Background and Related Work

The Efimov effect is the canonical example of discrete scale invariance in quantum mechanics. Efimov showed that three identical bosons near the two-body $s$-wave resonance form an infinite tower of bound states whose energies form a geometric sequence; the underlying Schrödinger equation has a continuous scaling symmetry that a short-range boundary condition breaks into a discrete one [5]. The scaling factor is not arbitrary: for equal-mass bosons the three-boson spectrum has the discrete scaling factor $22.694$, a number large enough that measuring signatures of two consecutive trimer levels is experimentally challenging, since the scattering length must simultaneously exceed the van der Waals length $r_{\text{vdW}}$ and remain below the de Broglie wavelength $\lambda_{\text{dB}}$ [4]. Despite this window constraint, the discrete scaling symmetry of the standard Efimov scenario has been confirmed experimentally by monitoring atom losses in an ultracold thermal gas of Cs atoms as a function of the $s$-wave scattering length, with loss enhancement at the critical scattering lengths $a_{-}^{(n)}$ and $a_{*}^{(n)}$ where trimer levels cross the three-atom and atom-dimer thresholds [4]. This measured factor of $22.694$ is the single most direct datum against a universal factor 2, and we use it as the anchor of the quantitative analysis in Section 4.

The factor is also not protected against modification. Adding one-dimensional spin-orbit coupling to the three-boson Hamiltonian introduces a parametric dependence of the relative Hamiltonian on the center-of-mass momentum vector, and the resulting spectrum obeys a generalized radial scaling law in a five-dimensional parameter space associated with a discrete scaling symmetry [4]. A scaling law whose factor lives in a five-dimensional parameter space cannot carry a single universal value; the same physical interaction class supports a continuum of factors. This is the strongest structural argument in the literature against factor universality within few-body physics itself.

A second line of evidence comes from engineered systems in which the factor is deliberately made tunable. When the scattering length is made proportional to the distance from the center of the system — realizable with ultracold atoms through a magnetic- or optical-field-induced Feshbach resonance with spatially varying field intensity, or through a confinement-induced resonance with transverse confinement lengths varying longitudinally — two particles are trapped about the center and their spectrum exhibits discrete scale invariance whose scale factor is controlled by the slope of the scattering length [2]. The proposal explicitly notes the resemblance to the Efimov effect while emphasizing practical advantages of the two-body trapped system. Because the slope is an experimental dial, the scaling factor in these systems is continuously adjustable by construction; a universal factor 2 is not merely absent here, it is excluded by design.

Dirac semimetals extend discrete scaling symmetry to condensed matter. Massless Dirac fermions in two and three dimensions form sequences of quasibound states in the field of an attractive charged impurity, with an energy ratio between successive states that is constant — a discrete scaling symmetry arising because the continuous scaling symmetry of the Dirac equation is broken by a short-range boundary condition, exactly as in the Efimov effect [1]. The magnetic response is regime-dependent: in two dimensions an applied magnetic field shifts the spectrum and produces magnetic oscillations that exhibit the discrete scaling symmetry through the interplay between quasibound states and Landau levels, whereas in three dimensions the magnetic oscillations do not show the symmetry before the quantum limit because different channels couple and no unique scaling factor exists; only in the quantum limit, where the system becomes quasi-one-dimensional and channels decouple for shallow quasibound states, does the magnetic dependence of the spectrum exhibit the symmetry again [1]. The phrase "lack of a unique scaling factor" in the three-dimensional pre-quantum-limit regime is a direct experimental-systems statement that the scaling factor is not an invariant of the material but a property of a regime.

The same Efimov physics in Dirac materials can be formulated as a renormalization-group limit cycle. In the field-theory treatment of an electron interacting with a static charged impurity in a Dirac semimetal, the Efimov effect is captured by limit-cycle solutions of the RG, and vacuum polarization screening — the many-body correction analogous to the Lamb shift for "relativistic hydrogen atoms" — modifies the effect; the results connect directly to recent transport experiments on Dirac materials and apply to Weyl materials as well [5]. The RG formulation makes the structural point explicit: a limit cycle is a closed orbit in coupling space, and the cycle length — hence the scaling factor — is set by the flow, not by a universal constant.

In quantum gravity, log-periodic modulations arise generically from discrete scale invariance but with an arbitrary period. The general form of the modulation follows from a scaling argument: continuous scale invariance gives power laws $f(z) \propto z^{\alpha}$, and breaking the continuous symmetry to a discrete one produces a log-periodic modulation factor $F_{\omega}$ whose period is a free parameter; such modulations arise in all quantum gravities where the Hausdorff and/or spectral dimension vary with scale, and discrete scale invariance makes the spacetime dimension complex-valued [3]. The simplest realization is a fundamentally discrete pregeometry similar to hierarchical lattices, explicit in multifractional theories, where logarithmic oscillations appear in the deep UV; in less regular combinatorial structures such as loop quantum gravity, spin foams, and group field theory, complex dimensions may arise only in special situations [3]. The free period parameter $\omega$ in this framework is the theoretical counterpart of the system-dependent factors measured in the laboratory: discrete scale invariance forces periodicity in $\ln$ scale, but nothing in the mechanism fixes the period.

The mechanism by which continuous scaling breaks to discrete is itself informative. In conformal quantum mechanics, the $so(2,1)$ algebra generated by the Hamiltonian $H$, the dilatation generator $G$, and the special conformal generator $K$ describes a large class of systems including molecules, black holes, graphene, and Calogero models; the continuous scaling symmetry can be broken purely quantum-mechanically when the boundary conditions — equivalently, the domain of the Hamiltonian — are not preserved by the action of the dilatation operator, and the broken symmetry can be restored by a suitable mixed state associated with a nonvanishing von Neumann entropy [8]. The breaking is therefore a property of the boundary condition and the state, not a universal constant of the algebra; different domains of the same Hamiltonian produce different discrete remnants.

Scaling symmetry in classical and gravitational settings likewise carries system-dependent parameters. In classical mechanics, variational symmetries of the action yield conservation laws while non-variational symmetries of the equations of motion — epitomized by scale-invariant hydrostatics — yield first-order non-conservation laws between invariants, from which all the familiar properties of polytropes follow, including a common core density profile and the Emden functions [9]. In matter-coupled scaling-Carroll gravity formulated as a gauge theory, the construction is based on a compensating real scalar field with a general dynamical exponent $z$, extending Carroll gravity at $z=1$; after fixing the scaling symmetry, the trace of the extrinsic curvature $K$ enters the shift transformation of the vector field $b_a$ under local Carroll boosts [10]. The exponent $z$ is a free parameter of the theory: anisotropic scaling with arbitrary $z$ is consistent, so even at the level of gravity-matter couplings the scaling exponent is a dial, not a constant.

Thermodynamics formulated geometrically makes the same point from a different direction. In the symplectic approach, the thermodynamic phase space is expanded by a global scale variable $Z$, and extensive and intensive quantities scale with arbitrary weights $r_i, r, \rho$ associated with the variables; fixing the extended global scale variable recovers the standard scale-invariant thermodynamic description, and the formalism covers systems whose homogeneity degrees differ, illustrated by the diffeomorphism between the Lagrangian submanifolds of the ideal and van der Waals gases [7]. Arbitrary scaling weights are built into the formalism; a universal weight is not.

Finally, the dyadic factor 2 does appear pervasively — but as a convention of analysis rather than a law of physics. In harmonic analysis, Besov spaces stem from a dyadic covering of frequency space and modulation spaces from a uniform covering, connected by the $\alpha$-modulation spaces of Gröbner at intermediate $\alpha \in [0,1]$; one can construct modulation function spaces with a scaling symmetry in which a dyadic scale $\lambda = 2^{j_0}$ is fixed by choice, and the scaling property of the spaces follows from how the translation operator acts on the vector weight under this chosen dyadic scale [11]. The factor 2 here is the base of the chosen partition of unity. This distinction — factor 2 as the base of a chosen decomposition versus factor 2 as a physical period — is exactly the confusion the factor-2 universality conjecture risks, and it motivates the falsification criterion of Section 5. A parallel caution comes from the philosophy of mathematical framing: the base-10 number system is a historical contingency rooted in human anatomy, with Babylonian base-60 and Mayan base-20 as functioning alternatives, so the prominence of a particular small integer in our descriptions need not reflect physical necessity [13]. Frameworks that model reality as a hyperdimensional fractal manifold with scale-dependent spectral dimensions likewise predict scale-dependent structure without fixing a universal scaling ratio [14].

## 3. Methods

This paper is an analytical reanalysis of published scaling factors; it performs no experiment, measurement, or simulation. The method has three parts.

**Model.** Every confirmed discrete-scale-invariant spectrum considered here is log-periodic: successive states obey

$$E_{n+1} = \frac{E_n}{\lambda}, \qquad E_n = E_0\, \lambda^{-n},$$

where $\lambda > 1$ is the scaling factor. Equivalently, in terms of the renormalization-group index $s_0$ that parametrizes the limit cycle,

$$E_n = E_0 \exp\!\left(-\frac{2\pi n}{s_0}\right), \qquad \lambda = \exp\!\left(\frac{2\pi}{s_0}\right).$$

The observable that discriminates between scaling hypotheses is the period of the spectrum in logarithmic scale,

$$\Delta(\ln E) = \ln \lambda = \frac{2\pi}{s_0}.$$

The universal-dyadic hypothesis asserts $\lambda = 2$ for all discrete-scale-invariant systems, i.e. $\Delta(\ln E) = \ln 2$ universally.

**Inputs.** We take scaling factors and their system dependences from the published literature: the three-boson Efimov factor $22.694$ [4]; the tunable factor of scaling traps, controlled by the scattering-length slope [2]; the regime dependence of the Dirac-semimetal factors [1]; the five-dimensional parameter space of the spin-orbit-coupled generalized scaling law [4]; and the free period parameter $\omega$ of log-periodic modulations in quantum-gravity contexts [3]. Where the literature reports a factor but not the derived index, we compute the index ourselves from the factor.

**Derivation and computation.** All arithmetic is shown explicitly in Section 4. We compute, from the single input $\lambda = 22.694$: the natural-logarithm period $\ln \lambda$; the RG index $s_0 = 2\pi/\ln\lambda$; the octave count $\log_2 \lambda = \ln\lambda/\ln 2$; the per-step discrepancy $\lambda/2$; and the cumulative discrepancy over four spectral steps, $\lambda^4$ versus $2^4$. We then state the falsification criterion that follows from the model and assess, system by system, whether any cited mechanism could reconcile its factor with the dyadic value.

**Assumptions.** We assume that the published factor $22.694$ for equal-mass bosons is the asymptotic zero-range value, as the standard Efimov scenario defines it [4]. We assume that the log-periodic model $E_n = E_0 \lambda^{-n}$ applies to each cited system in the regime where its discrete scaling symmetry is confirmed. We make no assumption about systems outside the cited domains; in particular, we do not extrapolate to cosmological or particle-physics data, for which the cited literature provides no measured scaling factor.

## 4. Analysis

**Step 1: The Efimov log-period.** The published three-boson scaling factor is $\lambda = 22.694$ [4]. The log-period is its natural logarithm. We compute $\ln(22.694)$ by bracketing: $e^{3} = 20.0855$ and $e^{3.1} = 22.198$. The remaining ratio is $22.694/22.198 = 1.02234$, and $\ln(1.02234) \approx 0.02209$ (since $\ln(1+x) \approx x - x^2/2$ with $x = 0.02234$ gives $0.02234 - 0.00025 = 0.02209$). Therefore

$$\ln \lambda = 3.1 + 0.02209 = 3.12209 \approx 3.1222.$$

So the Efimov spectrum repeats every $\Delta(\ln E) = 3.1222$ in natural-logarithmic scale.

**Step 2: The RG index.** From $\lambda = \exp(2\pi/s_0)$ we invert:

$$s_0 = \frac{2\pi}{\ln \lambda} = \frac{6.28319}{3.1222}.$$

Carrying out the division: $3.1222 \times 2 = 6.2444$; the remainder is $6.28319 - 6.2444 = 0.03879$; $0.03879/3.1222 = 0.01242$. Hence

$$s_0 = 2.01242 \approx 2.0127 \text{ (to the precision of } \ln\lambda\text{)},$$

and we adopt $s_0 = 2.0127$ as the derived index, consistent with the input precision of the four-significant-figure factor $22.694$.

**Step 3: Octave count.** The dyadic hypothesis predicts $\Delta(\ln E) = \ln 2 = 0.69315$. The number of octaves spanned by one Efimov period is

$$\log_2 \lambda = \frac{\ln \lambda}{\ln 2} = \frac{3.1222}{0.69315}.$$

Computing: $0.69315 \times 4 = 2.7726$; remainder $3.1222 - 2.7726 = 0.3496$; $0.3496/0.69315 = 0.5044$. Hence

$$\log_2(22.694) = 4.5044 \approx 4.505 \text{ octaves}.$$

One Efimov spectral step spans $4.505$ octaves, not one. The dyadic period is smaller than the measured period by a factor

$$\frac{3.1222}{0.69315} = 4.505,$$

i.e. the same number, as it must be: the ratio of periods equals the octave count.

**Step 4: Per-step discrepancy.** The ratio of the measured factor to the dyadic factor is

$$\frac{\lambda}{2} = \frac{22.694}{2} = 11.347.$$

If a physical spectrum obeyed the universal-dyadic law, each successive state would be lower in energy by a factor $2$; the observed Efimov tower steps down by $22.694$. After a single step the two hypotheses disagree in energy by a factor $11.347$.

**Step 5: Cumulative discrepancy over four steps.** Over $n$ steps the dyadic prediction is $2^{-n} E_0$ and the Efimov prediction is $\lambda^{-n} E_0$. For $n = 4$:

$$\lambda^2 = 22.694^2 = 515.02 \quad (22.694^2 = 22.694 \times 22.694;\ 22.694 \times 22 = 499.268,\ 22.694 \times 0.694 = 15.750;\ 499.268 + 15.750 = 515.018),$$

$$\lambda^4 = (515.018)^2 = 265{,}244 \quad (515.018^2 = 515^2 + 2 \times 515 \times 0.018 + 0.018^2 = 265{,}225 + 18.54 + 0.0003 \approx 265{,}244),$$

while $2^4 = 16$. The cumulative energy ratio between the two hypotheses after four steps is

$$\frac{\lambda^4}{2^4} = \frac{265{,}244}{16} = 16{,}578.$$

**Step 6: What would reconcile the factor with 2?** For the Efimov factor to equal $2$, the RG index would need to satisfy $s_0 = 2\pi/\ln 2 = 6.28319/0.69315 = 9.0647$. The measured index is $s_0 = 2.0127$; the required index is larger by $9.0647/2.0127 = 4.504$. No mechanism in the cited literature produces such a shift: the spin-orbit-coupled generalization moves the scaling law into a five-dimensional parameter space [4] but does not collapse it to a single dyadic value, and the scaling-trap construction makes the factor a continuous function of the trap slope [2], so it can be tuned through $2$ but not fixed there by any principle.

**Step 7: System-by-system factor audit.** We tabulate what fixes the scaling factor in each cited system:

| System | Scaling factor | What fixes it | Dyadic? |
|---|---|---|---|
| Three-boson Efimov (equal mass) | $22.694$ [4] | Short-range boundary condition / RG limit cycle | No |
| Three bosons with 1D spin-orbit coupling | Generalized law in 5D parameter space [4] | Center-of-mass momentum and couplings | No single value |
| Two-body scaling trap | Controlled by slope of $a(X)$ [2] | Trap engineering dial | Tunable, not fixed |
| 2D Dirac semimetal + impurity + field | Constant ratio, field-shifted [1] | Interplay of quasibound states and Landau levels | Not reported as 2 |
| 3D Dirac semimetal, pre-quantum limit | No unique scaling factor [1] | Channel coupling | Undefined |
| 3D Dirac semimetal, quantum limit | DSS restored [1] | Quasi-1D channel decoupling | Not reported as 2 |
| Quantum-gravity log oscillations | Period $2\pi/\omega$, $\omega$ free [3] | Pregeometry / multifractional structure | Free parameter |
| CQM with broken dilatations | Set by Hamiltonian domain [8] | Boundary conditions and state | Not fixed |
| Scaling-Carroll gravity | Dynamical exponent $z$ general [10] | Compensating scalar choice | Not fixed |
| Symplectic thermodynamics | Weights $r_i$ arbitrary [7] | Homogeneity degrees of the system | Not fixed |

No entry in this audit reports a measured or derived factor of $2$ as a physical scaling period. The only place $2$ appears with necessity is the dyadic partition convention of harmonic analysis, where $\lambda = 2^{j_0}$ is fixed by the choice of covering [11] — a choice of basis, not a physical period.

## 5. Results

All numbers below are computed in Section 4 from the single literature input $\lambda = 22.694$ [4]; no new measurement or simulation is reported.

1. The confirmed three-boson Efimov scaling factor is $\lambda = 22.694$, corresponding to a log-periodic period $\Delta(\ln E) = \ln(22.694) = 3.1222$ and an RG index $s_0 = 2\pi/3.1222 = 2.0127$.

2. The dyadic hypothesis predicts a period $\ln 2 = 0.69315$. The measured Efimov period exceeds it by a factor $4.505$; equivalently, one Efimov step spans $4.505$ octaves.

3. Per spectral step, the two hypotheses disagree in energy by a factor $\lambda/2 = 11.347$. Over four steps the cumulative disagreement is a factor $16{,}578$ ($\lambda^4 = 265{,}244$ versus $2^4 = 16$).

4. Reconciling the Efimov period with the dyadic value would require $s_0 = 9.0647$ instead of the derived $s_0 = 2.0127$, a factor-$4.504$ shift in the RG index for which no cited mechanism exists.

5. The system audit of Section 4 finds no confirmed discrete-scale-invariant physical system with a measured factor of $2$; the factors are either non-dyadic and fixed by boundary conditions ($22.694$ [4]), continuously tunable ([2], [7], [10]), regime-dependent with no unique value in part of parameter space ([1]), or free parameters of a theoretical framework ([3], [8]).

6. **Falsification criterion (projection, with stated assumptions).** Under the assumptions that a candidate spectrum is log-periodic and that its successive-state energy ratios can be measured to a relative precision better than a factor of $2$, the universal-dyadic hypothesis is falsified for that spectrum if the measured period $\Delta(\ln E)$ differs from $0.69315$ by more than the measurement uncertainty. The Efimov spectrum fails this test by a margin of $3.1222 - 0.69315 = 2.4291$ in $\ln E$, i.e. the measured period is $4.505$ times the dyadic prediction — a discrepancy far beyond any plausible measurement uncertainty in the atom-loss resonance ratios [4]. Any proposed universal dyadic periodicity in a new domain must therefore explain why that domain differs from the confirmed few-body case by a factor of $4.505$ in period, or abandon universality.

## 6. Discussion

The principal result is a negative one with a precise boundary: discrete scale invariance is confirmed across several unrelated domains, but the universal factor-2 hypothesis is excluded by the strongest available data at a per-step discrepancy factor of $11.347$ and a period discrepancy factor of $4.505$. The broader intuition — that discrete scaling loops can replace continuous scale invariance when a boundary condition breaks the scaling symmetry — survives and is in fact strengthened by the diversity of systems exhibiting it.

