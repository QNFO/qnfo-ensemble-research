# Phononic Crystal Scaffolds as Frozen Floquet Drives: An Isomorphism Between Protein-Noise-Assisted and Engineered Room-Temperature Quantum Transport

## Abstract

Environment-assisted quantum transport (ENAQT) shows that structured vibrational noise can enhance, rather than destroy, quantum transport, and photosynthetic protein scaffolds are the biological proof of principle. What is missing is a design route that imports this mechanism into solid-state devices without external laser driving or cryogenics. We derive an explicit isomorphism between (i) transport on a network dephased by a static, structured phonon spectral density and (ii) transport on the same network driven by a periodic Floquet field, and we show that the isomorphism fixes the scaffold specification: a phononic crystal whose spectral density matches a protein-like Lorentzian at the network's transition frequency. For a dimer with coupling $J = 100\ \mathrm{cm^{-1}}$ and detuning $\Delta = 50\ \mathrm{cm^{-1}}$, the optimal dephasing rate equals $\Delta$, giving a transfer time of $0.167\ \mathrm{ps}$; the equivalent Floquet drive amplitude is $63.2\ \mathrm{cm^{-1}}$. At $300\ \mathrm{K}$ the thermal occupation of a $100\ \mathrm{cm^{-1}}$ mode is $\bar{n} = 1.63$, so thermal phonons populate the target band. With an assumed acoustic velocity of $2\times10^{4}\ \mathrm{m\,s^{-1}}$, a $3.0\ \mathrm{THz}$ bandgap requires a hole pitch of $3.3\ \mathrm{nm}$, about $9.2\times10^{4}$ holes per $\mu\mathrm{m}^{2}$, within electron-beam lithography reach. The result converts thermal noise from a liability into a designable signal and yields concrete geometry rules for ambient-temperature quantum transport devices.

## 1. Introduction

Room-temperature quantum technologies are blocked by a thermal problem: at $300\ \mathrm{K}$ the thermal phonon bath destroys the phase coherence on which quantum transport, quantum sensing and candidate quantum computing substrates depend, so today's devices are operated either at cryogenic temperatures or under continuous external driving, both of which carry severe energy, cost and scaling penalties. The engineers who face this problem are designers of quantum devices — superconducting circuits, coherent electronic interconnects, quantum-dot and excitonic transport structures — who must currently choose between expensive cooling infrastructure and power-hungry active control. A design capability that let a device exploit its own thermal environment, instead of fighting it, would change that choice: it would replace cryostats and drive lasers with a lithographic pattern.

Biology already demonstrates that the choice exists. Photosynthetic pigment–protein complexes transport excitation energy at ambient temperature with near-unity efficiency, and the accepted mechanism is environment-assisted quantum transport (ENAQT): a structured vibrational environment, shaped by the protein scaffold, dephases the excitation at a rate that suppresses disorder-induced localization without destroying coherence between strongly coupled sites. The protein is, in this reading, a programmable phonon source whose spectral density is the control object. The research program this paper belongs to formalizes that reading as a "Signal-Worker" ontology, in which bosonic degrees of freedom (photons, phonons) act as informational signals that structure the landscape traversed by fermionic workers (electrons, excitons) [10], and analyzes the thermodynamic contrast between actively driven systems, which pay a continuous energy cost, and passively structured systems, which encode the signal in geometry [11]. That program has proposed, but not yet executed, the decisive solid-state test: a graphene/h-BN moiré heterostructure patterned with a phononic bandgap designed to resonate with the transport energy, fabricated by electron-beam lithography, with the critical temperature or transport efficiency measured as a function of scaffold geometry [10].

What is missing between the biological observation and such a device is a quantitative mapping. Given a target spectral density — the protein's phonon spectrum — what exactly must a synthetic scaffold do, and what does "replacing a drive by a structure" mean mathematically? This paper supplies that mapping. We prove an isomorphism between a static, structured phonon spectral density and a Floquet (periodic) drive: both enter the transport dynamics as the same object, a structured rate kernel at the transition frequency, and we derive the parameter correspondence that makes a passive scaffold equivalent to an active drive of a specified amplitude. We then translate the target spectral density into lithographic geometry.

The contributions are:

- A derivation of the ENAQT optimum for a disordered dimer, showing that the optimal dephasing rate equals the site detuning $\Gamma^{*} = \Delta$ and that the maximal transfer rate is $k_{\max} = J^{2}/\Delta$, evaluated for protein-scale parameters ($J = 100\ \mathrm{cm^{-1}}$, $\Delta = 50\ \mathrm{cm^{-1}}$) to give a $0.167\ \mathrm{ps}$ transfer time (Section 4.1).
- A derivation of the static-spectral-density/Floquet-drive isomorphism, including the amplitude correspondence $A = 0.632\,\hbar\omega_{0}$ for a drive whose first sideband carries 10% of the transport weight, so that a passive scaffold is quantitatively equivalent to a $63.2\ \mathrm{cm^{-1}}$ drive at $\omega_{0} = 100\ \mathrm{cm^{-1}}$ (Section 4.2).
- A thermal-population calculation showing $\bar{n} = 1.63$ at $300\ \mathrm{K}$ for a $100\ \mathrm{cm^{-1}}$ target mode, establishing that no cryogenics is needed for the mechanism to operate (Section 4.3).
- A translation of the target spectral density into phononic-crystal geometry: a $3.3\ \mathrm{nm}$ hole pitch and $\approx 9.2\times10^{4}$ holes per $\mu\mathrm{m}^{2}$ for a $3.0\ \mathrm{THz}$ bandgap, under a stated velocity assumption (Section 4.4).
- A design-rule set (modularity, resonance tuning by geometric doping, phononic insulation) and a falsifiable experimental proposal built on the scaffold-fabrication protocol already outlined in the literature (Section 7).

## 2. Background and Related Work

The closest antecedent to this work is the Signal-Worker analysis of photosynthetic energy transduction [10]. That manuscript argues that photosynthesis is a mature "boson-engineered system": the exciton is the localized worker and the protein-derived phonon field is the programmable signal, so that robust ambient-temperature quantum transport is achieved by vibronic engineering rather than by exotic long-lived coherence. Its Section 4.9 draws the parallel condensed-matter lesson from light-induced superconductivity: the bosonic signal can induce quantum order at ambient temperature, but maintaining a non-equilibrium state by external driving is thermodynamically unsustainable, and the way forward is to "design better workplaces — lattices that structurally encode the signal." Its Section 10.3 makes the proposal this paper quantifies: fabricate a graphene/h-BN moiré heterostructure with electron-beam-lithographed phonon cavities creating a structured noise environment $J(\omega)$ analogous to the protein spectral density, and measure the superconducting critical temperature $T_{c}$ as a function of scaffold geometry. Our contribution is the derivation that turns that proposal into numbers: the isomorphism between $J(\omega)$ and a Floquet drive, and the pitch, occupation and rate arithmetic the scaffold must satisfy.

The framework paper on structural versus driven coherence [11] supplies the classification this paper exploits. It distinguishes active systems — light-induced superconductivity, high-pressure hydrides, dynamical instabilities — which share the motif of an external, energy-intensive signal and consequently suffer thermodynamic inefficiency, transience and instability, from passive systems — proximity effects, moiré engineering, biological scaffolds — which encode the signal in intrinsic architecture and achieve stability at minimal energy cost. It further introduces two complexity metrics, Krylov complexity for the dynamical state and a Lossless Complexity Index (LCI) for the structural environment, and concludes from its analysis of the FMO complex that "room-temperature coherence is not forbidden by physics but requires a specific kind of structural environment — one that filters and shapes the thermal bath." Our isomorphism is the concrete design rule that the LCI-style structural filtering must implement: the filter's spectral density must place its weight at the network's transition frequency, with the width and height fixed by the ENAQT optimum derived in Section 4.1.

On the device side, the Quantum Abacus work [9] demonstrates the passive-control philosophy in a fermionic setting: using a 1D tight-binding model parameterized for the Weyl semimetal TaAs, it shows that achievable strain gradients of 0–5% can form isolated quantum registers and exponentially modulate fermionic hopping integrals, with operations claimed near the Landauer limit, in an architecture designed to avoid the "Thermodynamic Wall" of active control electronics. Our scaffold plays the same role as its static strain field — a frozen-in control pattern that requires no continuous power — but acts through the spectral density of the thermal bath rather than through a static gauge field; the two are complementary control channels on the same passive-hardware thesis.

The philosophical grounding for treating noise as signal is stated in the deterministic process-ontology manuscript [12], which argues that variance attributed to "systemic noise" is often the system expressing structured, deterministic complexity, and that "we must learn to read the noise rather than simply filtering it out." Our formal result is precisely that instruction made quantitative: the component of the thermal noise at the transition frequency is the useful signal, and the scaffold's job is to reshape its distribution.

Turning to the experimental platform, phononic crystals are a demonstrated technology for controlling thermal phonon transport in fabricated structures. MEMS bolometers on GaAs doubly-clamped beams patterned with two-dimensional phononic crystals show a reduction in the thermal conductance of the beams and, as a result, thermal sensitivities 2–3 times larger than unpatterned references [1]. Two aspects of that result matter here: it shows that lithographic periodicity can suppress unwanted phonon heat flow (the "phononic insulation" design rule of Section 4.4), and it demonstrates the fabrication and readout chain — patterning, thermal characterization, sensitivity comparison — that a scaffold-transport experiment would reuse.

The target spectral densities come from protein structures, and the structural database for extracting them is expanding rapidly. AlphaFold has predicted previously unknown three-dimensional structures of thousands of proteins, and algorithmic analysis of the high-confidence subset has uncovered rare backbone topologies including a $7_{1}$-knot, the most complex protein knot found [2]. For this program the significance is that a large, confidence-scored library of scaffold geometries exists from which vibrational spectral densities can be computed systematically, enabling the modularity design rule: pick a scaffold whose computed $J(\omega)$ matches the device's transition frequency. Complementary computational tools assess how mutations change protein stability — potential-like methods for predicting stability changes upon single-point mutation, recently improved by a mass-balance approximation of unfolding [6] — which is the screening tool for the geometric-doping design rule, since resonance tuning by scaffold mutation must not destabilize the structure.

The host materials for the transport layer are equally accessible. Room-temperature superconductivity remains an open and partly controversial search problem, and a recent survey proposes ten feasible research directions for it [3]; the scaffold mechanism of this paper is a candidate addition to that list, since it addresses the pairing or transport environment rather than the pairing interaction alone. Whichever host is chosen, single-crystal quality is a binding constraint, and the crystal-growth literature shows the required capabilities: large single crystals of the non-centrosymmetric superconductor Ru$_7$B$_3$ have been grown by the floating zone technique with a superconducting transition at $\sim 2.6\ \mathrm{K}$, at slow growth rates of around 3 mm/h [5]; complete single-crystalline rods of SrFeO$_{3-\delta}$, 8 mm in diameter and up to 10 cm in length, have been grown and annealed under controlled oxygen partial pressures specifically to enable neutron-scattering study of magnetic excitations [7] — the same scattering methodology that would verify a scaffold's phonon spectral density; and CoP$_3$ single crystals have been grown from stoichiometric melts under 3.5 GPa in a cubic-anvil apparatus, yielding single-phase boules with lattice constant $a = 7.7067$ Å, demonstrating that pressure is an additional handle for accessing congruent-melting growth windows [8]. Finally, the growth of structured periodic scaffolds itself has anisotropic kinetics: phase-field-crystal modeling of body-centered-cubic growth shows the velocity ordering $V_{\langle 100\rangle} > V_{\langle 111\rangle} > V_{\langle 110\rangle}$, in agreement with the Bravais law that faces with lower reticular density grow faster, and shows that insufficient local relaxation time produces disordered structure under high driving force [4]. For scaffold fabrication this is a direct warning: patterning at nanometer pitch must respect the crystal's anisotropic growth and relaxation kinetics or the intended periodicity disorders.

## 3. Methods

This paper is theoretical: it performs no experiment, simulation on hardware, or measurement. Its method is analytical derivation plus arithmetic evaluation, structured in four steps.

**Model.** We use the standard ENAQT model (Haken–Strobl–Reineker class). A network of sites with Hamiltonian

$$H_{S} = \sum_{m} \epsilon_{m} \ket{m}\bra{m} + \sum_{m \neq n} J_{mn} \ket{m}\bra{n}$$

is coupled to a thermal phonon bath through a system–bath interaction $V = \sum_{m} \ket{m}\bra{m} \otimes B_{m}$, fully characterized by the spectral density

$$J_{s}(\omega) = \sum_{\alpha} c_{\alpha}^{2}\, \delta(\omega - \omega_{\alpha})$$

smeared, for a structured environment, into peaks of finite width. In the weak-coupling (Redfield) limit the dephasing rate between sites $m,n$ is

$$\Gamma_{mn} = 2\pi \big(c_{m} - c_{n}\big)^{2} J_{s}(\omega_{mn}),$$

where $\omega_{mn} = (\epsilon_{m} - \epsilon_{n})/\hbar$. This equation is the pivot of the paper: the environment enters the dynamics only through $J_{s}$ evaluated at the transition frequency.

**Isomorphism.** We compare this to the same network under a periodic drive $H_{d}(t) = A\cos(\omega_{0} t)\,V$, treated in Floquet theory: the drive generates quasienergy sidebands with weights given by Bessel functions $w_{n} = \mathcal{J}_{n}(A/\hbar\omega_{0})^{2}$, and transport proceeds through photon-assisted channels at frequencies $\omega_{mn} \pm n\omega_{0}$. We derive the correspondence between the static spectral density $J_{s}(\omega)$ and the drive parameters $(A, \omega_{0})$ under which both produce the same effective transport rate.

**Evaluation.** We evaluate all derived expressions in closed form and then substitute numbers, showing every arithmetic step in Section 4. Protein-scale parameters are taken as $J = 100\ \mathrm{cm^{-1}}$ and $\Delta = 50\ \mathrm{cm^{-1}}$; these are stated assumptions representative of strongly coupled pigment networks, not measurements. Temperature is $T = 300\ \mathrm{K}$. The acoustic velocity used for geometry is an assumption, $v_{s} = 2\times10^{4}\ \mathrm{m\,s^{-1}}$, representative of covalent thin-film media. Unit conversions used throughout: $1\ \mathrm{cm^{-1}}$ corresponds to $c \times 100\ \mathrm{m^{-1}} = 2.998\times10^{10}\ \mathrm{Hz}$; $\hbar\omega/k_{B} = 1.4388\ \mathrm{cm\,K}$ per wavenumber.

**Scope.** The derivation is restricted to weak system–bath coupling, a two-site reduced network embedded in a larger one, and a classical-stationary bath. Limitations following from these restrictions are examined in Section 6.

## 4. Analysis

### 4.1 The ENAQT optimum for a disordered dimer

Consider two sites with detuning $\Delta = \epsilon_{1} - \epsilon_{2}$, coupling $J$, and Markovian dephasing at rate $\Gamma$ (in energy units, i.e. $\Gamma = \hbar/\tau_{\phi}$). In the fast-dephasing (adiabatic) limit, the coherent oscillation between sites is interrupted on a timescale $\hbar/\Gamma$, and each interruption randomizes the phase, allowing a diffusive hop. The standard Haken–Strobl result for the population transfer rate is

$$k(\Gamma) = \frac{2 J^{2} \Gamma}{\Gamma^{2} + \Delta^{2}}.$$

Derivation sketch: the dephasing broadens the energy mismatch $\Delta$ into a Lorentzian of half-width $\Gamma$; the coherent coupling $J$ transfers population across this broadened line, giving the Lorentzian-weighted rate above. We optimize over $\Gamma$:

$$\frac{dk}{d\Gamma} = 2J^{2}\,\frac{(\Gamma^{2} + \Delta^{2}) - \Gamma \cdot 2\Gamma}{(\Gamma^{2} + \Delta^{2})^{2}} = 2J^{2}\,\frac{\Delta^{2} - \Gamma^{2}}{(\Gamma^{2} + \Delta^{2})^{2}}.$$

Setting the numerator to zero gives $\Gamma^{2} = \Delta^{2}$, hence

$$\Gamma^{*} = |\Delta|, \qquad k_{\max} = k(\Gamma^{*}) = \frac{2J^{2}|\Delta|}{\Delta^{2} + \Delta^{2}} = \frac{J^{2}}{|\Delta|}.$$

This is the ENAQT optimum: the structured environment helps most when its dephasing rate exactly matches the energetic disorder it must overcome. Too little dephasing leaves the excitation localized by disorder; too much destroys the coherence that couples the sites.

**Numerical evaluation.** With the stated assumptions $J = 100\ \mathrm{cm^{-1}}$ and $\Delta = 50\ \mathrm{cm^{-1}}$:

$$k_{\max} = \frac{(100\ \mathrm{cm^{-1}})^{2}}{50\ \mathrm{cm^{-1}}} = \frac{10^{4}}{50}\ \mathrm{cm^{-1}} = 200\ \mathrm{cm^{-1}}.$$

Converting to a frequency: $200\ \mathrm{cm^{-1}} \times 2.998\times10^{10}\ \mathrm{Hz\,cm} = 5.996\times10^{12}\ \mathrm{Hz} = 5.996\ \mathrm{THz}$. The corresponding transfer time is

$$\tau_{\mathrm{tr}} = \frac{1}{5.996\times10^{12}\ \mathrm{s^{-1}}} = 1.668\times10^{-13}\ \mathrm{s} = 0.167\ \mathrm{ps}.$$

The optimal dephasing rate itself is $\Gamma^{*} = 50\ \mathrm{cm^{-1}}$, i.e. $1.499\ \mathrm{THz}$, a phase-randomization time of $1/1.499\times10^{12}\ \mathrm{s^{-1}} = 0.667\ \mathrm{ps}$.

### 4.2 The static-spectral-density / Floquet-drive isomorphism

**Static side.** By the Redfield expression of Section 3, a static structured bath with spectral density $J_{s}(\omega)$ produces inter-site dephasing

$$\Gamma = 2\pi\, c^{2}\, J_{s}(\Delta/\hbar),$$

where $c$ is the system–bath coupling amplitude and $J_{s}$ is now a smooth function. If the scaffold is engineered so that $J_{s}$ has a Lorentzian peak centered at the transition frequency $\omega_{0} = \Delta/\hbar$ with half-width $\gamma$ and peak height $S_{0}$,

$$J_{s}(\omega) = \frac{S_{0}\,\gamma^{2}}{(\omega - \omega_{0})^{2} + \gamma^{2}},$$

then at resonance $J_{s}(\omega_{0}) = S_{0}$ and $\Gamma = 2\pi c^{2} S_{0}$. The scaffold design condition is therefore simply

$$2\pi\, c^{2}\, S_{0} = \Gamma^{*} = \Delta/\hbar \quad \Longleftrightarrow \quad S_{0} = \frac{\Delta}{2\pi\, \hbar\, c^{2}}.$$

The bath is fully specified by three numbers: center $\omega_{0}$ (set by the network), width $\gamma$ (set by the desired robustness to detuning fluctuations; $\gamma \gtrsim \Delta$ keeps the rate within a factor of 2 of optimum, since $k(\Gamma)$ falls as $(\Gamma/\Delta + \Delta/\Gamma)^{-1}$), and height $S_{0}$ (set by the coupling and the optimum above).

**Floquet side.** Apply a periodic drive $H_{d}(t) = A\cos(\omega_{0} t)\,V$ with $V$ the same system–bath-type operator. Floquet theory gives quasienergy sidebands separated by $\hbar\omega_{0}$, with the $n$-th sideband's effective coupling weighted by

$$w_{n} = \mathcal{J}_{n}\!\left(\frac{A}{\hbar\omega_{0}}\right)^{2},$$

where $\mathcal{J}_{n}$ is the Bessel function of the first kind. Transport through the first sideband ($n = 1$) proceeds at effective coupling $J_{\mathrm{eff}} = J\,\mathcal{J}_{1}(A/\hbar\omega_{0})$. For small argument, $\mathcal{J}_{1}(x) \approx x/2$.

**Isomorphism.** Both mechanisms enter the transport equation as a structured rate kernel at the transition frequency: the static bath through $J_{s}(\Delta/\hbar)$, the drive through the sideband weights $\mathcal{J}_{n}(A/\hbar\omega_{0})^{2}$. The two are equivalent when they produce the same optimal transfer rate $k_{\max} = J^{2}/\Delta$. For the drive, the sideband-enhanced rate is $k_{F} = 2 J_{\mathrm{eff}}^{2}\Gamma_{0}/(\Gamma_{0}^{2} + \Delta^{2})$ with $\Gamma_{0}$ any residual dephasing; matching $k_{F} = k_{\max}$ with the same $\Gamma$-optimality requires $J_{\mathrm{eff}} = J$, i.e. the drive must supply the full coupling through its sidebands, or, in the partial-drive regime, a fraction $f$ of the transport weight:

$$f = \mathcal{J}_{1}(x)^{2}, \qquad x = \frac{A}{\hbar\omega_{0}}.$$

**Numerical evaluation.** Take the representative design point $f = 0.1$ (the drive's first sideband carries 10% of the transport weight). With $\mathcal{J}_{1}(x) \approx x/2$:

$$\frac{x^{2}}{4} = 0.1 \quad \Rightarrow \quad x^{2} = 0.4 \quad \Rightarrow \quad x = 0.6325.$$

With $\omega_{0} = 100\ \mathrm{cm^{-1}}$ (i.e. $\hbar\omega_{0} = 100\ \mathrm{cm^{-1}}$ in energy units):

$$A = 0.6325 \times 100\ \mathrm{cm^{-1}} = 63.2\ \mathrm{cm^{-1}}.$$

Interpretation: a passive scaffold whose spectral density supplies the corresponding weight at $\omega_{0}$ plays the role of an active drive of amplitude $63.2\ \mathrm{cm^{-1}}$ at $3.0\ \mathrm{THz}$ — but requires zero continuous input power, because the thermal bath provides the energy. This is the precise content of