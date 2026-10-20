# Re-Entry Modes in Solid-State Quantum Devices: A Calculus of Distinctions with Fully Shown Quantitative Benchmarks

## Abstract

Sub-kelvin quantum devices — superconducting qubits, mesoscopic transport structures, and low-temperature calorimetry samples — are designed and diagnosed against thermal, transport, and thermodynamic scales that are often quoted qualitatively rather than computed, leaving experimenters without stated numbers against which to size a measurement. The Laws of Form notion of "re-entry," in which a form is re-inserted into the space the form itself creates, offers a unifying description of several such device behaviors, but it has not been given quantitative anchors in solid-state settings. This paper formalizes re-entry as a recursive map on a device's distinction space and classifies three modes: coherent adiabatic re-entry, tunneling re-entry at topological edges, and thermodynamic re-entry in calorimetric anomalies. Using only numbers stated in the cited literature, we compute thermal scales $k_B T = 8.62 \times 10^{-5}$, $8.62 \times 10^{-6}$, and $1.72 \times 10^{-3}$ eV at $1$, $0.1$, and $20$ K; derive the two-level Schottky peak at $x^{*} = \Delta/(k_B T^{*}) \approx 2.3993$ with height $C_{\max} \approx 0.439\,R = 3.65\ \mathrm{J\,mol^{-1}\,K^{-1}}$; and linearize the reported $+90\%$ magnetoresistance of LuNi$_2$B$_2$C at $16$ T and $20$ K to $\eta = 5.625 \times 10^{-2}\ \mathrm{T}^{-1}$. The result is a set of stated scales and falsification conditions that convert a classificatory framework into a design aid for sub-kelvin experiments.

## 1. Introduction

Experimenters working on sub-kelvin solid-state devices face a recurring practical problem: the energy scales, anomaly fingerprints, and transport responses that determine whether a measurement will succeed are scattered across qualitative statements in the literature, and no single worked set of numbers exists against which a new experiment can be sized. A cryogenicist choosing an operating temperature, a calorimetrist deciding whether an observed heat-capacity peak is a two-level Schottky feature or a latent-heat artifact, and a transport researcher comparing magnetoresistance anomalies across materials all need explicit numbers — $k_B T$ at the operating point, the peak position and height of the minimal anomaly model, a comparable figure of merit for a reported response — before committing cryostat time, which is expensive: the refrigeration literature states that reaching the sub-1 K regime currently requires costly cryostats and that solid-state cooling solutions would change the field [3]. If the quantitative anchors derived here hold, the experimenter can decide, before measurement, whether a candidate signal is thermally resolvable at a given temperature, whether its anomaly shape matches the two-level fingerprint, and how a reported transport response compares across platforms.

The conceptual frame is re-entry. In the Laws of Form tradition, a distinction is an act that separates a space into marked and unmarked states, and re-entry is the re-insertion of a form into its own indicational space — the mechanism by which self-referential structure acquires dynamical content. A predecessor treatment formalized re-entry as a recursive map on a device's distinction space and classified three modes in solid-state systems: coherent adiabatic re-entry, tunneling re-entry at edges, and thermodynamic re-entry in anomalies [6]. That treatment, however, left several of its anchors tied to sources it could not fully quote and left the practical pathway implicit. The present paper consolidates the framework against a fixed bibliography, completes the arithmetic, and adds the engineering pathway that the classification implies.

The physics substrate is well documented. Superconductivity is characterized by the complete elimination of electrical resistance below the critical temperature $T_c$, identified as the most important parameter of the field, and solid-state chemists have contributed significantly to it by discovering new compounds in the decades since the copper oxides [1]. Coherent population transfer by adiabatic passage, well known in quantum optics but historically unfamiliar to solid-state physicists, has been introduced to the solid-state community together with applications in superconducting and semiconductor devices, including a three-island Cooper-pair box whose Hamiltonians can be tailored to mimic three-level $\Lambda$ systems [2]. Refrigeration to well below 1 K is the enabling condition for the fundamental excitations such devices use [3]. Calorimetric anomalies — lambda and Schottky anomalies in solid-state phase transitions — have been analyzed and shown to be the latent heat of nucleation-and-growth transitions [5]. And the energy cost of running quantum computing platforms has been benchmarked system-wide in joules per solution, with superconducting platforms leading at $0.05$–$0.71$ J/solution and trapped ions trailing at $16.3$ J/solution [7].

This paper makes no measurements. Its contributions are:

1. A re-entry formalism $\mathcal{R}[d] = d \circ \mathcal{R}[d]$ on a device's distinction space, with three physically realized modes, restated against a fixed bibliography (Section 3).
2. Fully shown derivations of the thermal scales $E_T = k_B T$ at $0.1$, $1$, and $20$ K, the two-level Schottky peak position $x^{*} \approx 2.3993$ and height $C_{\max} \approx 0.439\,R$, the linearized magnetoresistance figure $\eta = 5.625 \times 10^{-2}\ \mathrm{T}^{-1}$ for LuNi$_2$B$_2$C, and the stoichiometric and synthesis scales of the pyrochlore solid solutions (Section 4).
3. A cross-domain energy comparison linking the joules-per-solution benchmark of quantum computing platforms to the sub-kelvin thermal quantum, computed as $\approx 3.6 \times 10^{22}$ thermal quanta per solution (Section 4.7).
4. A falsifiability protocol per mode and an explicit statement of the first measurement each mode requires (Sections 3.5 and 7).

## 2. Background and Related Work

The bibliography available to this paper contains seven works; all seven are discussed here, and the consequence of this restricted set is stated in Section 6.

**Superconducting materials.** The introduction to high-temperature superconductivity for solid-state chemists [1] presents superconductivity as the complete elimination of electrical resistance below the critical temperature $T_c$, identified as the most important parameter in superconductivity, and notes that since the discovery of copper oxide superconductors 39 years before its writing, many solid-state chemists have contributed to the field by discovering new compounds. For the re-entry program, [1] establishes the materials substrate: the boundary between superconducting and normal states is a physically drawn distinction whose position is set by $T_c$, and the historical rate of new-compound discovery indicates that the substrate is actively expanding.

**Coherent control.** The review of adiabatic passage in solid-state devices [2] states that coherent population transfer by adiabatic passage is a well-known method in quantum optics that remained largely unknown to solid-state physicists, and provides an introduction to the basic principles and applications in solid-state systems. Its introduction records that nanotechnology has made it possible to study devices below the micrometer scale, to manipulate single charges and fluxes, and to build small electrical and mechanical resonators, with typical energy scales on the order of $0.1$–$1$ Kelvin, much larger than the smallest temperatures reachable in experiment, so that the discrete nature of the energy spectrum must be taken into account. Its methods section sets up the three-level $\Lambda$ atom with long-lived ground states $|0\rangle$ and $|1\rangle$ coupled to an excited state $|e\rangle$ via laser fields with Rabi frequencies $\Omega_0$, $\Omega_1$ and common detuning $\Delta$, and with no direct coupling between the ground states. Its application section shows that Hamiltonians similar to the atomic ones can be tailored in a superconducting Cooper-pair box with three islands, where islands (1) and (2) are coupled via tunable Josephson junctions to a third island (e). Its conclusions state that adiabatic passage-like techniques may be used to generate simple charge transfers, to detect non-Abelian holonomies, and to control charge transport properties, including an alternative kind of charge pump. Adiabatic passage is the canonical coherent re-entry mode: population is transported along a dark manifold and returned to a state of the same distinction class it began in, with the path drawn by the device's own control parameters.

**Cryogenic enabling technology.** The phonon-blocked junction refrigerator work [3] motivates refrigeration as an important enabler for quantum technology: the very low energy of the fundamental excitations typically utilized in quantum technology devices and systems requires temperatures well below 1 K; expensive cryostats are utilized in reaching the sub-1 K regime; and solid-state cooling solutions would revolutionize the field. The work proposes new electronic micro-coolers based on phonon-blocked semiconductor junctions. For the re-entry program, [3] supplies the thermal operating point: sub-kelvin operation is the regime in which the distinctions drawn by quantum devices are thermally resolvable, quantified via $k_B T$ in Section 4.1.

**Disorder-tuned platforms.** The pyrochlore solid-solution study [4] describes the synthesis and characterization of the solid solutions Y$_2$Ti$_{2-x}$Nb$_x$O$_{7-y}$, Lu$_2$Ti$_{2-x}$Nb$_x$O$_{7-y}$, Y$_2$Ti$_{2-x}$Ta$_x$O$_{7-y}$ and Lu$_2$TiTaO$_{7-y}$ with $-0.4 < y < 0.5$; synthesis at 1600 °C and $10^{-5}$ Torr yields oxygen deficiency in all systems; and all compounds are found to be paramagnetic and semiconducting, with the size of the local moments being less, in some cases substantially less, than expected. This is a disorder-tuned platform in which the boundary between stoichiometric regimes is itself a drawn distinction with a stated tolerance window, which is used arithmetically in Section 4.4.

**Calorimetric anomalies.** The phase-transition study [5] analyzes and illustrates the origin of lambda and Schottky anomalies in solid-state phase transitions and shows them to be the latent heat of nucleation-and-growth phase transitions. This is thermodynamic re-entry in its most direct cited form: the latent heat released by the transition re-enters the heat capacity measured across the transition, producing the anomaly. The two-level Schottky peak is derived explicitly in Section 4.2 as the minimal closed model of this mode.

**The predecessor framework.** The prior statement of this program [6] proposed that the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed, identified re-entry as the re-insertion of a form into its own indicational space, and asked whether re-entry has an operational reading in solid-state devices. Its results section reports the thermal scales $E_T(1\ \mathrm{K}) = 8.62 \times 10^{-5}$ eV, $E_T(0.1\ \mathrm{K}) = 8.62 \times 10^{-6}$ eV, $E_T(20\ \mathrm{K}) = 1.72 \times 10^{-3}$ eV, the Schottky peak at $x^{*} \approx 2.3993$ with $C_{\max} \approx 0.439\,R$, and the linearized magnetoresistance figure for LuNi$_2$B$_2$C; its discussion states that the taxonomy is classificatory, not predictive, and that it fails if any transport anomaly can be relabeled "re-entrant" post hoc. The present paper retains these anchors, rederives them with the arithmetic shown in full, and adds the practical pathway and cross-domain comparison that [6] left open.

**Energy benchmarking.** The JPCUB competitive landscape [7] defines the joules-per-solution metric $J_S(T,\varepsilon)$ — the total system-level energy consumed by system $S$ to produce a solution to computational task $T$ at correctness threshold $\varepsilon$ — as a physics-grounded benchmark, with components $E_{\text{comp}} + E_{\text{mem}} + \ldots$. Its results table ranks 13 gate-model platforms, with Google Willow at $0.05$ J/solution ($25.0$ kW system power, $30$ ns two-qubit gates, $99.95\%$ fidelity) down to Rigetti Aspen-M-3 at $0.71$ J/solution, and Quantinuum trapped-ion systems at $8.5$ and $9.6$ J/solution. Its thermodynamic-inversion summary concludes that for every task current machines can run they are $10^6$–$10^7$ times worse than classical in energy, and that for symmetric cryptography a quantum attack is thermodynamically impossible. For the re-entry program, [7] supplies the system-level energy scale against which the sub-kelvin thermal quantum of [3] can be compared; the comparison is computed in Section 4.7.

## 3. Methods

### 3.1 Distinctions and re-entry

Following the Laws of Form tradition as carried into the quantum setting by [6], a distinction is an act that separates a space into marked and unmarked states. We model a solid-state device's distinction space as a set $\mathcal{D}$ of operational distinctions, each a binary observable $d_i$ with marked state $d_i^{+}$ and unmarked state $d_i^{-}$. Re-entry is defined as a recursive composition: a distinction $d$ is re-entrant when the value taken by $d$ determines the boundary condition under which $d$ itself is evaluated. Formally,

$$\mathcal{R}[d] = d \circ \mathcal{R}[d],$$

i.e., the evaluation of $d$ requires an evaluation of $d$. In physical terms, $\mathcal{R}$ is realized whenever a device Hamiltonian $H(\lambda)$ depends on a control parameter $\lambda$ that is itself a function of the state generated under $H(\lambda)$:

$$H = H\big(\lambda[\psi]\big), \qquad H|\psi\rangle = E|\psi\rangle.$$

This self-consistency structure is the solid-state realization of re-entry. It is deliberately general; the three modes below are its concrete realizations in the cited literature.

### 3.2 Mode I: coherent adiabatic re-entry

In adiabatic passage [2], a system with instantaneous eigenstates $|n(\lambda)\rangle$ is transported along a path $\lambda(t)$ such that the population remains in a connected dark or adiabatically following manifold. In the three-level $\Lambda$ configuration of [2], the two long-lived ground states $|0\rangle$ and $|1\rangle$ are coupled to $|e\rangle$ with no direct ground-state coupling, so a dark state exists that connects $|0\rangle$ to $|1\rangle$ without populating $|e\rangle$. The re-entry condition is that the final state $|\psi_f\rangle$ lies in the same distinction class as the initial state $|\psi_i\rangle$:

$$|\langle \alpha | \psi_f \rangle|^{2} \approx 1 \quad \text{for the same label } \alpha \text{ at } t=0 \text{ and } t=T_{\mathrm{pass}},$$

while the intermediate path visits a distinct manifold. The adiabaticity condition is the standard one,

$$\left|\frac{\langle m(t)|\dot{H}(t)|n(t)\rangle}{E_m(t) - E_n(t)}\right| \ll 1 \quad (m \neq n),$$

which links the passage time $T_{\mathrm{pass}}$ to the minimum gap $\Delta_{\min}$ as a design constraint.

### 3.3 Mode II: tunneling re-entry at boundaries

For a mesoscopic conductor, the boundary itself is the distinction (device interior versus lead or vacuum), and tunneling of amplitude into or across that boundary is re-entry: the quasiparticle, defined by the bulk, acts on the boundary that defines it. The charge-transfer and charge-pump applications of adiabatic passage in superconducting and semiconductor systems [2] instantiate this mode in its coherent form; the magnetoresistance anomaly of LuNi$_2$B$_2$C discussed below instantiates a transport analogue in which the carrier response re-enters the resistive tensor. The quantitative signature of the mode is a response exponent or figure of merit, and discriminating among candidate mechanisms is the program by which the mode is tested.

### 3.4 Mode III: thermodynamic re-entry (anomalies)

For a phase transition [5], the latent heat of the nucleation-and-growth process re-enters the calorimetric observable: the heat capacity $C(T)$ across the transition contains the heat released by the transition itself. The minimal closed model is the two-level Schottky system with level splitting $\Delta$, whose partition function is

$$Z = 1 + e^{-\beta \Delta}, \qquad \beta = \frac{1}{k_B T},$$

and whose heat capacity per mole of independent two-level units is

$$\frac{C}{R} = \frac{x^{2}\, e^{x}}{\left(1 + e^{x}\right)^{2}} = \frac{x^{2}}{4 \cosh^{2}(x/2)}, \qquad x \equiv \frac{\Delta}{k_B T}.$$

We derive the peak of this function in Section 4.2; it is the quantitative anchor for the anomaly mode of [5].

### 3.5 Falsifiability protocol

Following the discipline of the predecessor framework [6], any re-entry claim attached to a platform must be registered as a measurable accept/reject statement. For each mode we state: (i) the observable, (ii) the scale computed in Section 4, and (iii) the rejection condition. Mode I rejects if adiabatic return fidelity falls below the thermal noise floor at the operating temperature; Mode II rejects if the transport figure of merit is indistinguishable across candidate mechanisms; Mode III rejects if the anomaly shape is inconsistent with the two-level prediction derived below.

## 4. Analysis

All input numbers are stated with their sources; every arithmetic step is shown.

### 4.1 Thermal energy scales (inputs from [2], [3])

**Input 1.** Boltzmann's constant $k_B = 8.617333 \times 10^{-5}\ \mathrm{eV/K}$ (physical constant, stated here as the input).

**Input 2.** The sub-1 K operating regime of quantum devices, from [3]: temperatures "well below 1 K." We take the representative values $T_1 = 1\ \mathrm{K}$ and $T_2 = 0.1\ \mathrm{K}$. These coincide with the device energy-scale window of [2], which states typical nanodevice energy scales on the order of $0.1$–$1$ Kelvin.

**Input 3.** The transport-anomaly temperature of the LuNi$_2$B$_2$C Hall-effect study cited in the predecessor framework [6]: $T_3 = 20\ \mathrm{K}$, at which a magnetoresistance of $+90\%$ at $\mu_0 H = 16$ T is reported.

**Derivation.** The thermal energy is $E_T(T) = k_B T$.

$$E_T(T_1) = \left(8.617333 \times 10^{-5}\ \mathrm{eV/K}\right)(1\ \mathrm{K}) = 8.617333 \times 10^{-5}\ \mathrm{eV} \approx 8.62 \times 10^{-5}\ \mathrm{eV}.$$

$$E_T(T_2) = \left(8.617333 \times 10^{-5}\ \mathrm{eV/K}\right)(0.1\ \mathrm{K}) = 8.617333 \times 10^{-6}\ \mathrm{eV} \approx 8.62 \times 10^{-6}\ \mathrm{eV}.$$

$$E_T(T_3) = \left(8.617333 \times 10^{-5}\ \mathrm{eV/K}\right)(20\ \mathrm{K}) = 1.723467 \times 10^{-3}\ \mathrm{eV} \approx 1.72 \times 10^{-3}\ \mathrm{eV}.$$

**Interpretation.** A distinction whose level splitting is $\Delta$ is thermally resolved only if $\Delta \gtrsim E_T$. At $T_2 = 0.1$ K the resolvable scale is $\approx 8.62 \times 10^{-6}$ eV, i.e., $10.0\times$ finer than at 1 K, since $E_T(T_1)/E_T(T_2) = 8.617333 \times 10^{-5} / 8.617333 \times 10^{-6} = 10.0$ exactly ($E_T$ is linear in $T$). This is the quantitative content of the statement in [3] that sub-1 K operation is required: each decade of temperature buys one decade of resolvable splitting. It is also the quantitative content of the observation in [2] that nanodevice energy scales of $0.1$–$1$ K are "much larger than the smallest temperatures that can be reached in an experiment": the device splittings sit at or above the $k_B T$ values computed here, so the discrete spectrum is thermally resolvable.

### 4.2 Schottky-anomaly peak (minimal model of [5])

**Input.** The two-level heat capacity derived in Section 3.4:

$$\frac{C(x)}{R} = \frac{x^{2}}{4 \cosh^{2}(x/2)}, \qquad x = \frac{\Delta}{k_B T}.$$

**Derivation of the peak position.** Set $d(C/R)/dx = 0$. With $f(x) = x^{2} \sech^{2}(x/2)/4$,

$$f'(x) \propto 2x \sech^{2}(x/2) - x^{2} \sech^{2}(x/2) \tanh(x/2) = x \sech^{2}(x/2)\left[2 - x \tanh(x/2)\right].$$

For $x > 0$, the bracket must vanish:

$$\frac{2}{x} = \tanh\!\left(\frac{x}{2}\right).$$

Solve by fixed-point evaluation. Start $x_0 = 2.4$:

- $\tanh(1.2) = 0.833655\ldots$; $2/x_0 = 2/2.4 = 0.833333\ldots$. Since $\tanh(x/2) > 2/x$, the root lies slightly below $2.4$.
- Try $x_1 = 2.399$: $\tanh(1.1995) = 0.833562\ldots$; $2/2.399 = 0.833681\ldots$. Now $\tanh(x/2) < 2/x$, so the root lies between $2.399$ and $2.400$.
- Interpolating: the bracket $g(x) = \tanh(x/2) - 2/x$ changes from $0.833562 - 0.833681 = -1.19 \times 10^{-4}$ at $x = 2.399$ to $0.833655 - 0.833333 = +3.22 \times 10^{-4}$ at $x = 2.400$. Linear interpolation gives the root at

$$x^{*} = 2.399 + 0.001 \times \frac{1.19 \times 10^{-4}}{1.19 \times 10^{-4} + 3.22 \times 10^{-4}} = 2.399 + 0.001 \times \frac{1.19}{4.41} = 2.399 + 0.00027 \approx 2.3993.$$

So $x^{*} \approx 2.3993$, i.e., the Schottky peak occurs at

$$T^{*} \approx \frac{\Delta}{2.3993\, k_B}.$$

**Derivation of the peak height.** At $x^{*} = 2.3993$, $x^{*}/2 = 1.19965$:

- $\cosh(1.2) = (e^{1.2} + e^{-1.2})/2 = (3.320117 + 0.301194)/2 = 3.621311/2 = 1.810655$.
- $\sinh(1.2) = (3.320117 - 0.301194)/2 = 1.509462$; adjusting for $\delta = -0.00035$: $\cosh(1.19965) \approx 1.810655 - 0.00035 \times 1.509462 = 1.810655 - 0.000528 = 1.810127$.
- $\cosh^{2}(x^{*}/2) = (1.810127)^{2} = 3.276560$.
- $4 \cosh^{2}(x^{*}/2) = 13.106239$.
- $(x^{*})^{2} = (2.3993)^{2} = 5.756640$.

$$\frac{C_{\max}}{R} = \frac{5.756640}{13.106239} = 0.43920 \approx 0.439.$$

With $R = 8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$:

$$C_{\max} = 0.43920 \times 8.314 = 3.6515\ \mathrm{J\,mol^{-1}\,K^{-1}} \approx 3.65\ \mathrm{J\,mol^{-1}\,K^{-1}},$$

occurring at $k_B T^{*} \approx \Delta / 2.3993$, i.e., $T^{*} \approx 0.4168\, \Delta / k_B$ (since $1/2.3993 = 0.41679$).

**Worked example.** A splitting $\Delta = 1.72 \times 10^{-3}$ eV (the $20$ K thermal scale of Section 4.1) places the Schottky peak at

$$T^{*} = \frac{20\ \mathrm{K}}{2.3993} = 8.3357\ \mathrm{K} \approx 8.3\ \mathrm{K}.$$

**Connection to [5].** The cited work shows lambda and Schottky anomalies to be the latent heat of nucleation-and-growth transitions [5]. The two-level result above is the minimal closed form of the Schottky branch of that statement: it gives the experimenter the two numbers — peak position $x^{*} \approx 2.3993$ and peak height $0.439\,R$ — against which an observed anomaly in a solid-state device can be tested for two-level (re-entrant latent-heat) origin versus other mechanisms.

### 4.3 Magnetoresistance figure of merit (input carried by [6])

**Input.** The predecessor framework [6] reports, from the LuNi$_2$B$_2$C Hall-effect literature it cites, a magnetoresistance reaching $+90\%$ for $\mu_0 H = 16$ T at $T = 20$ K, in a response the same source describes as nonlinear in field.

**Derivation.** A magnetoresistance of $+90\%$ means

$$\frac{\rho_{xx}(16\ \mathrm{T}) - \rho_{xx}(0)}{\rho_{xx}(0)} = 0.90 \quad \Rightarrow \quad \frac{\rho_{xx}(16\ \mathrm{T})}{\rho_{xx}(0)} = 1.90.$$

We define a linearized figure of merit (explicitly a linearization, not a claim that the response is linear):

$$\eta \equiv \frac{0.90}{16\ \mathrm{T}} = 5.625 \times 10^{-2}\ \mathrm{T}^{-1}.$$

Equivalently, per tesla the resistive ratio changes by $\approx 5.6 \times 10^{-2}$ on average across $0 \le \mu_0 H \le 16$ T at $T = 20$ K. This number is a bookkeeping device for comparing transport anomalies across platforms; the reported nonlinearity means $\eta$ is an average, not a local slope.

### 4.4 Stoichiometric tolerance window (input from [4])

**Input.** From [4]: the oxygen-deficiency parameter spans $-0.4 < y < 0.5$.

**Derivation.** Window width:

$$\Delta y = 0.5 - (-0.4) = 0.9.$$

Window midpoint:

$$y_{\mathrm{mid}} = \frac{0.5 + (-0.4)}{2} = \frac{0.1}{2} = 0.05.$$

The window is asymmetric about stoichiometry $y = 0$: it extends $0.5$ in the oxygen-excess direction ($y > 0$) and $0.4$ in the oxygen-deficiency direction ($y < 0$), i.e., the excess side is larger by $0.5 - 0.4 = 0.1$, or $(0.1/0.9) \times 100\% \approx 11.1\%$ of the window width. This asymmetry is consistent with the report in [4] that synthesis at 1600 °C and $10^{-5}$ Torr yields oxygen deficiency in all systems: the accessible window is biased toward oxygen excess relative to the deficiency side, meaning the deficiency side is the narrower of the two.

### 4.5 Synthesis scales (input from [4])

**Input.** From [4]: synthesis at 1600 °C and $10^{-5}$ Torr.

- Temperature conversion: $T = 1600 + 273.15 = 1873.15\ \mathrm{K}$.
- Thermal energy: $k_B T = 8.617333 \times 10^{-5}\ \mathrm{eV/K} \times 1873.15\ \mathrm{K}$. Compute: $8.617333 \times 1.87315 = 16.1416$ (since $8.617333 \times 1.8 = 15.5112$ and $8.617333 \times 0.07315 = 0.63036$; sum $16.14156$). Hence $k_B T = 0.16142\ \mathrm{eV