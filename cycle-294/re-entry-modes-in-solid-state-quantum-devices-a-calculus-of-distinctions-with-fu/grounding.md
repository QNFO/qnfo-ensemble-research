# Grounding block - source: rem-969223b0-4809-4792-bd40-c8cf3f39e336

## Research idea

Re-entry from 10.5281/zenodo.18222364: these modes in solid-state devices?

## Existing paper under revision (remediation only)

# Re-Entry Modes in Solid-State Quantum Devices: A Calculus of Distinctions with Fully Shown Quantitative Benchmarks

## Abstract

Laws of Form proposed that the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed, and identified "re-entry" — the re-insertion of a form into its own indicational space — as the mechanism by which self-referential structure acquires dynamical content. This paper asks whether re-entry has an operational reading in solid-state devices, where a device degree of freedom is coupled back onto the very boundary condition that defines it. We formalize re-entry as a recursive map on a device's distinction space and classify three re-entry modes: coherent adiabatic re-entry (population returned to its originating manifold), tunneling re-entry (quasiparticle amplitude re-entering an edge it defines), and thermodynamic re-entry (anomalies in which latent heat re-enters the order parameter's own heat capacity). Using only numbers stated in the source literature and derivations shown in full, we compute thermal energy scales $k_B T$ at $0.1$ K, $1$ K, and $20$ K; derive the Schottky-anomaly peak position $x^{*} = \Delta/(k_B T^{*}) \approx 2.3993$ and peak height $C_{\max} \approx 0.439\,R = 3.653\ \mathrm{J\,mol^{-1}\,K^{-1}}$ for a two-level system; and linearize the reported $+90\%$ magnetoresistance of LuNi$_2$B$_2$C at $\mu_0 H = 16$ T, $T = 20$ K to an average figure of merit $\eta = 5.625 \times 10^{-2}\ \mathrm{T}^{-1}$. We argue that solid-state platforms — including trapped-ion simulators registered as a falsifiability testbed for ultrametric structure — are natural settings in which re-entry claims become measurable, and we state the conditions under which the framework would be falsified.

## 1. Introduction

The research question addressed here is direct: re-entry, as formalized in the Laws of Form tradition, is a mode of self-reference in which a distinction is drawn inside the space that the distinction itself creates. Can this mode be given operational content in solid-state devices, where boundaries, edges, and population manifolds are physical rather than notational objects?

The motivation is threefold. First, the Laws of Form consolidation known as QNFO synthesizes known quantum correspondences of the indicational calculus and identifies open problem categories, providing a standing register of where the formalism touches physics [9]. Second, a companion register organizes sixteen published records from a single research program into one testable claim: that trapped-ion quantum simulators are the first near-term platform on which ultrametric ($p$-adic) structure in quantum dynamics can be accepted or rejected by measurement [10]. If self-referential structure is to be tested anywhere in the near term, that register identifies where. Third, the solid-state literature already contains phenomena that are naturally described as a degree of freedom acting back on its own defining boundary: coherent population transfer that returns a system to a manifold it started in [3], edge tunneling in which quasiparticle amplitude re-enters the edge whose topological order defines it [2], and phase-transition anomalies in which latent heat re-enters the thermal response of the transitioning system itself [7].

This paper makes no new measurements. Its contribution is a classification and a set of fully shown derivations that convert qualitative claims from the cited literature into quantitative anchors, so that future re-entry experiments in solid-state devices have stated scales against which to be designed. We proceed as follows: Section 2 reviews the cited works strictly within what their supplied summaries state; Section 3 defines the re-entry formalism and the three modes; Section 4 performs all arithmetic explicitly; Section 5 reports only computed numbers; Section 6 discusses limitations and falsification; Section 7 concludes.

## 2. Background and Related Work

We discuss each cited work using only the content of its supplied summary; where a summary is thin, we say so and relate the work to our argument only through what the summary states.

**Superconductivity and materials platforms.** The introduction to high-temperature superconductivity for solid-state chemists [1] presents superconductivity as the complete elimination of electrical resistance below the critical temperature $T_c$, identified as the most important parameter of the field, and notes that since the discovery of copper oxide superconductors 39 years before its writing, solid-state chemists have contributed significantly by discovering new compounds. For our purposes, [1] establishes the materials-discovery substrate on which any solid-state re-entry device would be built: the distinction between superconducting and normal states is a physically drawn boundary whose position is set by $T_c$. The Hall-effect study of LuNi$_2$B$_2$C [8] reports that the Hall resistivity $\rho_{xy}$ is negative in both the normal and mixed states, with no sign reversal of the type typical for high-$T_c$ superconductors, and that a distinct nonlinearity in $\rho_{xy}(H)$ appears in the normal state for $T < 40$ K, accompanied by a large magnetoresistance reaching $+90\%$ for $\mu_0 H = 16$ T at $T = 20$ K; a scaling relation of the form $\rho_{xy} \sim \rho_{xx}^{\beta}$ is discussed. This gives us a concrete, numerically anchored transport anomaly in which the carrier response re-enters the resistive tensor — a candidate transport re-entry mode quantified in Section 4.

**Fractional quantum Hall edges and quasiparticles.** The tunneling study of paired fractional quantum Hall states [2] examines the edge transport properties of the Haldane-Rezayi (HR), Moore-Read (Pfaffian), and Halperin (331) states, provides a table of exponents for tunneling between the edges of paired FQH states in gated 2D structures and for tunneling into the edge from a normal Fermi liquid, and reports findings on the conductance and Andreev reflection of non-Abelions; the supplied summary is truncated at the point where the comparison among HR, Pfaffian, and 331 states is concluded, so the specific conclusion of that comparison is not available to us. We use [2] as the canonical instance of tunneling re-entry: an edge is the boundary that defines the topological phase, and tunneling into or across it is amplitude re-entering the boundary's own indicational space. The hierarchy-state study [4] obtains residual interactions between Laughlin quasiparticles from exact numerical diagonalization of small systems, and reports that the pseudopotentials $V_{\mathrm{QP}}(R)$, describing the interaction energy as a function of relative angular momentum $R$, cannot support Laughlin correlations at certain quasiparticle filling factors (the summary cites examples $\nu_{\mathrm{QE}} = 1/3$ and $\nu_{\mathrm{QH}} = 1/5$), which motivates novel hierarchy states. This is re-entry at the level of effective theory: the quasiparticles generated by a parent state interact through pseudopotentials that then determine whether the parent's correlation structure can be re-entered at a new filling.

**Coherent control.** The review of adiabatic passage in solid-state devices [3] states that coherent population transfer by adiabatic passage is well known in quantum optics but remained largely unknown to solid-state physicists, and provides an introduction to the basic principles together with applications in solid-state systems. Adiabatic passage is our canonical coherent re-entry mode: population is transported along a dark manifold and returned to a state of the same form it began in, with the path itself drawn by the device's control parameters.

**Cryogenic enabling technology.** The phonon-blocked junction refrigerator work [5] motivates refrigeration as an important enabler for quantum technology: the very low energy of fundamental excitations in quantum devices requires temperatures well below 1 K, expensive cryostats are currently used to reach the sub-1 K regime, and solid-state cooling solutions would revolutionize the field; the work proposes new electronic micro-coolers based on phonon-blocked semiconductor junctions. For a re-entry program, [5] supplies the thermal operating point: sub-kelvin operation is the regime in which the distinctions drawn by quantum devices are thermally resolvable, which we quantify via $k_B T$ in Section 4.

**Magnetism, disorder, and anomalies.** The pyrochlore solid-solution study [6] describes synthesis and characterization of $(\mathrm{Y},\mathrm{Lu})_2\mathrm{Ti}_{2-x}(\mathrm{Nb},\mathrm{Ta})_x\mathrm{O}_{7\pm y}$ solid solutions with $-0.4 < y < 0.5$; synthesis at 1600 °C and $10^{-5}$ Torr yields oxygen deficiency in all systems, and all compounds are found to be paramagnetic and semiconducting, with local moments smaller — in some cases substantially smaller — than expected (the summary truncates before stating the expected values). This is a disorder-tuned platform in which the boundary between stoichiometric regimes is itself a drawn distinction with a stated tolerance range, which we use arithmetically in Section 4. The phase-transition study [7] analyzes and illustrates the origin of lambda and Schottky anomalies in solid-state phase transitions and shows them to be the latent heat of nucleation-and-growth transitions. This is thermodynamic re-entry in its purest cited form: the latent heat released by the transition re-enters the heat capacity measured across the transition, producing the anomaly. We derive the two-level Schottky peak explicitly in Section 4 as the minimal model of this mode.

**Formal registers.** The QNFO consolidation [9] records that George Spencer-Brown's Laws of Form (1969) proposed the act of drawing a distinction as the primitive operation from which logic, mathematics, and physics can be constructed, and that the consolidation synthesizes known quantum correspondences, identifies 7 open problem categories, and proposes 4 extensions. The trapped-ion ultrametric testbed [10] organizes sixteen published records from a single research program, spanning December 2025 to August 2026, into one testable claim: trapped-ion quantum simulators are the first near-term platform on which ultrametric ($p$-adic) structure in quantum dynamics can be accepted or rejected by measurement. Together, [9] and [10] supply the formal vocabulary (distinction, re-entry) and the falsifiability discipline (a registered, measurable claim) within which the present classification is offered.

## 3. Methods

### 3.1 Distinctions and re-entry

Following the Laws of Form tradition as recorded in [9], a distinction is an act that separates a space into marked and unmarked states. We model a solid-state device's distinction space as a set $\mathcal{D}$ of operational distinctions, each a binary observable $d_i$ with marked state $d_i^{+}$ and unmarked state $d_i^{-}$. Re-entry is then defined as a recursive composition: a distinction $d$ is re-entrant when the value taken by $d$ determines the boundary condition under which $d$ itself is evaluated. Formally, we write the re-entry operator as

$$\mathcal{R}[d] = d \circ \mathcal{R}[d],$$

i.e., the evaluation of $d$ requires an evaluation of $d$. In physical terms, $\mathcal{R}$ is realized whenever a device Hamiltonian $H(\lambda)$ depends on a control parameter $\lambda$ that is itself a function of the state generated under $H(\lambda)$:

$$H = H\big(\lambda[\psi]\big), \qquad H|\psi\rangle = E|\psi\rangle.$$

This self-consistency structure is the solid-state avatar of re-entry. It is deliberately general; the modes below are its three concrete realizations in the cited literature.

### 3.2 Mode I: coherent adiabatic re-entry

In adiabatic passage [3], a system with instantaneous eigenstates $|n(\lambda)\rangle$ is transported along a path $\lambda(t)$ such that the population remains in a connected dark or adiabatically following manifold. The re-entry condition is that the final state $|\psi_f\rangle$ lies in the same distinction class as the initial state $|\psi_i\rangle$,

$$|\langle \alpha | \psi_f \rangle|^{2} \approx 1 \quad \text{for the same label } \alpha \text{ at } t=0 \text{ and } t=T_{\mathrm{pass}},$$

while the intermediate path visits a distinct manifold. The adiabaticity condition is the standard one,

$$\left|\frac{\langle m(t)|\dot{H}(t)|n(t)\rangle}{E_m(t) - E_n(t)}\right| \ll 1 \quad (m \neq n),$$

which we state as the design constraint linking passage time $T_{\mathrm{pass}}$ to the minimum gap $\Delta_{\min}$.

### 3.3 Mode II: tunneling re-entry at edges

For a fractional quantum Hall edge [2], the edge itself is the distinction (bulk topological order versus vacuum). Tunneling of amplitude into or across that edge is re-entry: the quasiparticle, defined by the bulk, acts on the boundary that defines it. The cited work parameterizes this by tunneling exponents, tabulated for edge-to-edge tunneling in gated 2D structures and for tunneling from a normal Fermi liquid into the edge [2]. We do not reproduce the exponent table — the supplied summary does not give its values — but we adopt the structural claim that the exponent is the quantitative signature of the re-entry mode, and that comparing HR, Pfaffian, and 331 states is the program by which the mode is discriminated.

### 3.4 Mode III: thermodynamic re-entry (anomalies)

For a phase transition [7], the latent heat of the nucleation-and-growth process re-enters the calorimetric observable: the heat capacity $C(T)$ across the transition contains the heat released by the transition itself. The minimal closed model is the two-level Schottky system with level splitting $\Delta$, whose partition function is

$$Z = 1 + e^{-\beta \Delta}, \qquad \beta = \frac{1}{k_B T},$$

and whose heat capacity per two-level unit is

$$\frac{C}{R} = \frac{x^{2}\, e^{x}}{\left(1 + e^{x}\right)^{2}} = \frac{x^{2}}{4 \cosh^{2}(x/2)}, \qquad x \equiv \frac{\Delta}{k_B T}.$$

We derive the peak of this function in Section 4; it is the quantitative anchor for the anomaly mode of [7].

### 3.5 Falsifiability protocol

Following the discipline of [10], any re-entry claim attached to a platform must be registered as a measurable accept/reject statement. For each mode we therefore state: (i) the observable, (ii) the scale computed in Section 4, and (iii) the rejection condition. Mode I rejects if adiabatic return fidelity falls below the thermal noise floor at the operating temperature; Mode II rejects if the tunneling exponent is indistinguishable across the paired states compared in [2]; Mode III rejects if the anomaly shape is inconsistent with the two-level prediction derived below.

## 4. Analysis

All input numbers below are stated with their sources; every arithmetic step is shown.

### 4.1 Thermal energy scales (inputs from [5], [8])

**Input 1.** Boltzmann's constant $k_B = 8.617333 \times 10^{-5}\ \mathrm{eV/K}$ (physical constant, stated here as the input).

**Input 2.** The sub-1 K operating regime of quantum devices, from [5]: "temperature well below 1 K." We take the representative values $T_1 = 1\ \mathrm{K}$ and $T_2 = 0.1\ \mathrm{K}$.

**Input 3.** The transport-anomaly temperature from [8]: $T_3 = 20\ \mathrm{K}$.

**Derivation.** The thermal energy is $E_T(T) = k_B T$.

$$E_T(T_1) = \left(8.617333 \times 10^{-5}\ \mathrm{eV/K}\right)(1\ \mathrm{K}) = 8.617333 \times 10^{-5}\ \mathrm{eV} \approx 8.62 \times 10^{-5}\ \mathrm{eV}.$$

$$E_T(T_2) = \left(8.617333 \times 10^{-5}\ \mathrm{eV/K}\right)(0.1\ \mathrm{K}) = 8.617333 \times 10^{-6}\ \mathrm{eV} \approx 8.62 \times 10^{-6}\ \mathrm{eV}.$$

$$E_T(T_3) = \left(8.617333 \times 10^{-5}\ \mathrm{eV/K}\right)(20\ \mathrm{K}) = 1.723467 \times 10^{-3}\ \mathrm{eV} \approx 1.72 \times 10^{-3}\ \mathrm{eV}.$$

**Interpretation.** A distinction whose level splitting is $\Delta$ is thermally resolved only if $\Delta \gtrsim E_T$. At $T_2 = 0.1$ K the resolvable scale is $\approx 8.62 \times 10^{-6}$ eV, i.e., $10.0\times$ finer than at 1 K (ratio $E_T(T_1)/E_T(T_2) = 8.617333 \times 10^{-5} / 8.617333 \times 10^{-6} = 10.0$, exactly, since $E_T$ is linear in $T$). This is the quantitative content of the claim in [5] that sub-1 K operation is required: each decade of temperature buys one decade of resolvable splitting.

### 4.2 Schottky-anomaly peak (minimal model of [7])

**Input.** The two-level heat capacity derived in Section 3.4:

$$\frac{C(x)}{R} = \frac{x^{2}}{4 \cosh^{2}(x/2)}, \qquad x = \frac{\Delta}{k_B T}.$$

**Derivation of the peak position.** Set $d(C/R)/dx = 0$. Write $f(x) = x^{2} \sech^{2}(x/2)/4$. Then

$$f'(x) \propto 2x \sech^{2}(x/2) - x^{2} \sech^{2}(x/2) \tanh(x/2) = x \sech^{2}(x/2)\left[2 - x \tanh(x/2)\right].$$

For $x > 0$, the bracket must vanish:

$$\frac{2}{x} = \tanh\!\left(\frac{x}{2}\right).$$

Solve by fixed-point iteration. Start $x_0 = 2.4$:

- $\tanh(1.2) = 0.833655\ldots$; $2/x_0 = 2/2.4 = 0.833333\ldots$. Since $\tanh(x/2) > 2/x$, the root lies slightly below $2.4$.
- Try $x_1 = 2.399$: $\tanh(1.1995) = 0.833562\ldots$; $2/2.399 = 0.833681\ldots$. Now $\tanh(x/2) < 2/x$, so the root lies between $2.399$ and $2.400$.
- Interpolating: the bracket $g(x) = \tanh(x/2) - 2/x$ changes from $0.833562 - 0.833681 = -1.19 \times 10^{-4}$ at $x = 2.399$ to $0.833655 - 0.833333 = +3.22 \times 10^{-4}$ at $x = 2.400$. Linear interpolation gives the root at

$$x^{*} = 2.399 + 0.001 \times \frac{1.19 \times 10^{-4}}{1.19 \times 10^{-4} + 3.22 \times 10^{-4}} = 2.399 + 0.001 \times \frac{1.19}{4.41} = 2.399 + 0.00027 \approx 2.3993.$$

So $x^{*} \approx 2.3993$, i.e., the Schottky peak occurs at

$$T^{*} \approx \frac{\Delta}{2.3993\, k_B}.$$

**Derivation of the peak height.** At $x^{*} = 2.3993$, $x^{*}/2 = 1.19965$:

- $\cosh(1.19965)$: $\cosh(1.2) = (e^{1.2} + e^{-1.2})/2 = (3.320117 + 0.301194)/2 = 3.621311/2 = 1.810655$. Adjusting for $\delta = -0.00035$: $\sinh(1.2) = (3.320117 - 0.301194)/2 = 1.509462$, so $\cosh(1.19965) \approx 1.810655 - 0.00035 \times 1.509462 = 1.810655 - 0.000528 = 1.810127$.
- $\cosh^{2}(x^{*}/2) = (1.810127)^{2} = 3.276560$.
- $4 \cosh^{2}(x^{*}/2) = 13.106239$.
- $(x^{*})^{2} = (2.3993)^{2} = 5.756640$.

$$\frac{C_{\max}}{R} = \frac{5.756640}{13.106239} = 0.43920 \approx 0.439.$$

So the maximal Schottky heat capacity is $C_{\max} \approx 0.439\,R$ per mole of independent two-level units. With $R = 8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$:

$$C_{\max} = 0.43920 \times 8.314 = 3.6515\ \mathrm{J\,mol^{-1}\,K^{-1}} \approx 3.65\ \mathrm{J\,mol^{-1}\,K^{-1}},$$

occurring at $k_B T^{*} \approx \Delta / 2.3993$, i.e., $T^{*} \approx 0.4168\, \Delta / k_B$ (since $1/2.3993 = 0.41679$).

**Connection to [7].** The cited work shows lambda and Schottky anomalies to be the latent heat of nucleation-and-growth transitions [7]. The two-level result above is the minimal closed form of the Schottky branch of that statement: it gives the experimenter the two numbers — peak position $x^{*} \approx 2.3993$ and peak height $0.439\,R$ — against which an observed anomaly in a solid-state device can be tested for two-level (re-entrant latent-heat) origin versus other mechanisms.

### 4.3 Magnetoresistance figure of merit (input from [8])

**Input.** From [8]: magnetoresistance reaching $+90\%$ for $\mu_0 H = 16$ T at $T = 20$ K.

**Derivation.** A magnetoresistance of $+90\%$ means

$$\frac{\rho_{xx}(16\ \mathrm{T}) - \rho_{xx}(0)}{\rho_{xx}(0)} = 0.90 \quad \Rightarrow \quad \frac{\rho_{xx}(16\ \mathrm{T})}{\rho_{xx}(0)} = 1.90.$$

We define a linearized figure of merit (explicitly a linearization, not a claim that the response is linear — [8] states the Hall resistivity response is nonlinear in field):

$$\eta \equiv \frac{0.90}{16\ \mathrm{T}} = 5.625 \times 10^{-2}\ \mathrm{T}^{-1}.$$

Equivalently, per tesla the resistive ratio changes by $\approx 5.6 \times 10^{-2}$ on average across $0 \le \mu_0 H \le 16$ T at $T = 20$ K. This number is a bookkeeping device for comparing transport anomalies across platforms; the nonlinearity reported in [8] means $\eta$ is an average, not a local slope.

### 4.4 Stoichiometric tolerance window (input from [6])

**Input.** From [6]: the oxygen-deficiency parameter spans $-0.4 < y < 0.5$.

**Derivation.** Window width:

$$\Delta y = 0.5 - (-0.4) = 0.9.$$

Window midpoint:

$$y_{\mathrm{mid}} = \frac{0.5 + (-0.4)}{2} = \frac{0.1}{2} = 0.05.$$

The window is asymmetric about stoichiometry $y = 0$: it extends $0.5$ in the oxygen-excess direction ($y > 0$) and $0.4$ in the oxygen-deficiency direction ($y < 0$), i.e., the excess side is larger by $0.5 - 0.4 = 0.1$, or $(0.1/0.9) \times 100\% \approx 11.1\%$ of the window width. This asymmetry is consistent with the report in [6] that synthesis at 1600 °C and $10^{-5}$ Torr yields oxygen deficiency in all systems: the accessible window is biased toward oxygen excess relative to the deficiency side, meaning the deficiency side is the narrower of the two.

### 4.5 Synthesis scales (input from [6])

**Input.** From [6]: synthesis at 1600 °C and $10^{-5}$ Torr.

- Temperature conversion: $T = 1600 + 273.15 = 1873.15\ \mathrm{K}$.
- Thermal energy: $k_B T = 8.617333 \times 10^{-5}\ \mathrm{eV/K} \times 1873.15\ \mathrm{K}$. Compute: $8.617333 \times 1.87315 = 16.1416$ (since $8.617333 \times 1.8 = 15.5112$ and $8.617333 \times 0.07315 = 0.63036$; sum $16.14156$). Hence $k_B T = 0.16142\ \mathrm{eV}$.
- Pressure conversion: $1\ \mathrm{Torr} = 133.322\ \mathrm{Pa}$, so $P = 10^{-5} \times 133.322 = 1.33322 \times 10^{-3}\ \mathrm{Pa}$.

### 4.6 Record cadence of the falsifiability register (input from [10])

**Input.** From [10]: sixteen published records spanning December 2025 to August 2026.

**Derivation.** The span December 2025 through August 2026 covers 9 calendar months (Dec, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug). Mean cadence:

$$\frac{16\ \text{records}}{9\ \text{months}} = 1.777\ldots \approx 1.78\ \text{records/month}.$$

At this cadence, a 12-month extension would add $1.78 \times 12 \approx 21$ records (projection, assuming constant cadence; uncertainty is unquantified in the source summary, so this projection carries an unbounded error bar and is offered only as an order-of-magnitude planning figure).

### 4.7 Mode I design constraint (structural, no external numbers)

The adiabaticity condition of Section 3.2 requires

$$T_{\mathrm{pass}} \gg \frac{\max_n |\langle m|\partial_\lambda H|n\rangle|}{\Delta_{\min}^{2}}.$$

No numerical value is computable from the supplied summaries (none of them states a gap or matrix element), so we state the constraint symbolically and flag it as the quantity a Mode I experiment must measure first.

## 5. Results

We report only numbers computed in Section 4, plus the clearly labeled projection.

1. **Thermal energy scales.** $E_T(1\ \mathrm{K}) = 8.62 \times 10^{-5}\ \mathrm{eV}$; $E_T(0.1\ \mathrm{K}) = 8.62 \times 10^{-6}\ \mathrm{eV}$; $E_T(20\ \mathrm{K}) = 1.72 \times 10^{-3}\ \mathrm{eV}$. Each decade of cooling buys exactly one decade ($10.0\times$) of thermally resolvable level splitting, since $E_T = k_B T$ is linear in $T$.

2. **Schottky peak (Mode III anchor).** For the two-level model, the peak occurs at $x^{*} = \Delta/(k_B T^{*}) \approx 2.3993$, i.e., $T^{*} \approx 0.4168\, \Delta/k_B$, with peak height $C_{\max} \approx 0.439\,R = 3.65\ \mathrm{J\,mol^{-1}\,K^{-1}}$ per mole of two-level units. Example: a splitting $\Delta = 1.72 \times 10^{-3}$ eV (the $20$ K thermal scale of [8]) would place its Schottky peak at $T^{*} = 20/2.3993 = 8.336\ \mathrm{K} \approx 8.3\ \mathrm{K}$ (arithmetic: $20/2.3993 = 8.3357$).

3. **Transport figure of merit (Mode II-adjacent anchor).** The LuNi$_2$B$_2$C magnetoresistance reported in [8] linearizes to $\eta = 5.625 \times 10^{-2}\ \mathrm{T}^{-1}$ between $0$ and $16$ T at $20$ K, with resistive ratio $1.90$ at $16$ T. This is an average over a response that [8] reports as nonlinear.

4. **Stoichiometric window (platform tolerance).** The pyrochlore solid-solution window of [6] has width $\Delta y = 0.9$, midpoint $y_{\mathrm{mid}} = 0.05$, and an oxygen-excess side larger than the deficiency side by $0.1$, i.e., $\approx 11.1\%$ of the window width.

5. **Synthesis scales.** From [6]: $T = 1873.15\ \mathrm{K}$, $k_B T = 0.16142\ \mathrm{eV}$, $P = 1.33322 \times 10^{-3}\ \mathrm{Pa}$.

6. **Register cadence (program metric).** The trapped-ion ultrametric register [10] contains 16 records over 9 months, i.e., $\approx 1.78$ records/month.

7. **Projection (labeled).** If the cadence of item 6 held constant, a 12-month extension of the register would accumulate $\approx 21$ additional records. Assumptions: constant cadence, no gaps in the program; uncertainty unquantified in the source, so this is an order-of-magnitude planning figure only.

8. **Non-computed quantity (flagged).** The adiabatic-passage design constraint $T_{\mathrm{pass}} \gg |\langle m|\partial_\lambda H|n\rangle| / \Delta_{\min}^{2}$ is stated symbolically; no numerical value is derivable from the supplied summaries.

## 6. Discussion

**Limitations.** The re-entry taxonomy is classificatory, not predictive: it organizes known behaviors but, as presented, generates no new numerical prediction beyond the standard Schottky fingerprint. The bibliography summaries are truncated for [2], [4], [5], [6], and [8]; in each case we used only what the supplied text states and explicitly avoided importing exponent values, moment magnitudes, or cooler performance figures from memory. The formal apparatus of [9] is used only at the level its summary supports (distinction as primitive; re-entry as a recognized configuration); the QNFO consolidation's 7 open problem categories and 4 extensions are not enumerated in the supplied text and are therefore not engaged here. Likewise, the ultrametric claim of [10] is used as a methodological template only; no $p$-adic analysis is performed in this paper.

**Failure modes.** The taxonomy fails if the mode assignments of Section 3 are not exclusive or principled — e.g., if any transport anomaly can be relabeled "re-entrant" post hoc, the concept explains nothing. A guard against this is the recursion requirement $\mathcal{R}[d] = d \circ \mathcal{R}[d]$: a candidate mode must exhibit a concrete self-consistency structure, not merely a loop metaphor. It also fails if the Schottky/lambda identification of [7] does not extend to the two-level fingerprint computed here; the derivation of Section 4.2 is standard statistical mechanics, but its *application* to nucleation-and-growth latent heat in a specific material is an assumption of this paper.

**What would falsify the claims.** (i) A device setting in the bibliography's domain where the excitation return is demonstrably not describable by a self-consistent re-entry map, yet is still naturally called re-entrant in the Laws-of-Form sense — this would show the formalization is too narrow. (ii) A measured heat-capacity anomaly attributed to a Schottky mechanism whose peak position violates $\Delta = 2.3993\, k_B T^{*}$ after independent determination of $\Delta$ — this would falsify the instrument, though not the taxonomy. (iii) Demonstration that the three modes reduce to one mechanism with a single observable signature — for example, that adiabatic return, edge tunneling, and calorimetric anomalies all follow from one self-consistency equation with no mode-distinct parameter — which would collapse the taxonomy into a relabeling and remove its explanatory content. Each of these falsifiers is stated so that a future experiment can target it directly.

## 7. Conclusion

We asked whether re-entry, the self-referential operation identified in the Laws of Form tradition as recorded in [9], has operational content in solid-state devices. Our answer is a classification and a set of fully shown quantitative anchors. Re-entry was formalized as a recursive map $\mathcal{R}[d] = d \circ \mathcal{R}[d]$ on a device's distinction space and realized in three modes: coherent adiabatic re-entry (population returned to its originating manifold, per [3]), tunneling re-entry (quasiparticle amplitude re-entering the edge that defines it, per [2]), and thermodynamic re-entry (latent heat re-entering the heat capacity across a transition, per [7]). The computed anchors are: thermal scales $E_T = k_B T$ of $8.62 \times 10^{-5}$ eV, $8.62 \times 10^{-6}$ eV, and $1.72 \times 10^{-3}$ eV at $1$ K, $0.1$ K, and $20$ K respectively, quantifying the sub-kelvin operating requirement of [5]; the two-level Schottky peak at $x^{*} \approx 2.3993$ with height $C_{\max} \approx 0.439\,R \approx 3.65\ \mathrm{J\,mol^{-1}\,K^{-1}}$, the minimal fingerprint of the anomaly mode of [7]; the linearized magnetoresistance figure $\eta = 5.625 \times 10^{-2}\ \mathrm{T}^{-1}$ for LuNi$_2$B$_2$C at $16$ T and $20$ K from [8]; and the stoichiometric window and synthesis scales of [6]. The falsifiability discipline of [10] supplies the protocol by which each mode's accept/reject condition is registered. The taxonomy is classificatory, not predictive, and its value rests on whether the recursion requirement excludes post-hoc relabeling; the falsifiers of Section 6 state how this would be tested. The immediate next step is the one flagged in Section 4.7: a Mode I experiment must first measure the gap $\Delta_{\min}$ and matrix element $|\langle m|\partial_\lambda H|n\rangle|$ that no supplied summary provides.

## References

[1] Introduction to High-Temperature Superconductivity for Solid State Chemists. arXiv:2602.12608v2. https://arxiv.org/abs/2602.12608v2
[2] Tunneling in Paired Fractional Quantum Hall States: Conductance and Andreev Reflection of Non-Abelions. arXiv:cond-mat/9805224v2. https://arxiv.org/abs/cond-mat/9805224v2
[3] Applications of adiabatic passage in solid-state devices. arXiv:cond-mat/0506412v1. https://arxiv.org/abs/cond-mat/0506412v1
[4] Residual interactions and correlations among Laughlin quasiparticles: Novel hierarchy states. arXiv:cond-mat/0402326v1. https://arxiv.org/abs/cond-mat/0402326v1
[5] Phonon-blocked junction refrigerators for cryogenic quantum devices. arXiv:2209.07275v1. https://arxiv.org/abs/2209.07275v1
[6] Structural and Magnetic Properties of Pyrochlore Solid Solutions (Y,Lu)2Ti2-x(Nb,Ta)xO7+/-y. arXiv:0803.3568v1. https://arxiv.org/abs/0803.3568v1
[7] Lambda- and Schottky-anomalies in solid-state phase transitions. arXiv:1104.4637v1. https://arxiv.org/abs/1104.4637v1
[8] Hall-effect in LuNi_2B_2C in normal and superconducting mixed states. arXiv:cond-mat/9811273v1. https://arxiv.org/abs/cond-mat/9811273v1
[9] QNFO: Quantum Laws of Form
[10] QNFO: The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2602.12608v2 | Introduction to High-Temperature Superconductivity for Solid State Chemists
arXiv:cond-mat/0506412v1 | Applications of adiabatic passage in solid-state devices
arXiv:2209.07275v1 | Phonon-blocked junction refrigerators for cryogenic quantum devices
arXiv:0803.3568v1 | Structural and Magnetic Properties of Pyrochlore Solid Solutions (Y,Lu)2Ti2-x(Nb,Ta)xO7+/-y
arXiv:1104.4637v1 | Lambda- and Schottky-anomalies in solid-state phase transitions

## QNFO corpus context (Vectorize)

QNFO: Re-Entry Modes in Solid-State Quantum Devices: A Calculus of Distinctions with Fully Shown Quantitative Benchmarks | https://papers.qnfo.org/papers/re-entry-modes-in-solid-state-quantum-devices-a-calculus-of-distinctions-with-fu
QNFO: JPCUB Competitive Landscape v2.0: System-Level Joules-per-Solution Estimates for 17 Quantum Computing Platforms from Published Specifications | https://papers.qnfo.org/papers/jpcub-competitive-landscape

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2602.12608v2 | Introduction to High-Temperature Superconductivity for Solid State Chemists
  Superconductivity is one of the most amazing properties that metallic conductors exhibit. Electrical resistance is completely eliminated below the critical temperature (Tc), which is the most important parameter in superconductivity. Since the discovery of copper oxide superconductors 39 years ago, many solid state chemists have made significant contributions to the field by discovering new compou
  Full text (https://ar5iv.labs.arxiv.org/html/2602.12608v2), excerpts of its own sections:
  § Submission history: From: Zenji Hiroi [ view email ] [v1] Fri, 13 Feb 2026 04:27:46 UTC (8,811 KB) [v2] Sun, 24 May 2026 22:51:32 UTC (8,733 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Introduction to High-Temperature Superconductivity for Solid State Chemists, by Zenji Hiroi View PDF view license
  § Current browse context:: cond-mat.supr-con < prev | next > new | recent | 2026-02 Change to browse by: cond-mat
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[2] arXiv:cond-mat/0506412v1 | Applications of adiabatic passage in solid-state devices
  Coherent population transfer by adiabatic passage is a well-known method in quantum optics. This remarkable technique which is based on simple ideas has remained largely unknown to solid-state physicists. Here we provide an introduction to the basic principles of this method and discuss also some applications in solid-state systems.
  Full text (https://arxiv.org/html/cond-mat/0506412v1), excerpts of its own sections:
  § 1 Introduction: Traditionally solid-state physics is focused on systems with quasi-continuous energy spectra for the various elementary excitations present in macroscopic solids. During the past decade, however, the successful development of nanotechnology has made it possible to study devices below the micrometer scale, to manipulate single charges and fluxes, or to build small electrical and mechanical resonators. The typical energy scales for such devices are, say, on the order of 0.1 …1 Kelvin and therefore much larger than the smallest temperatures that can be reached in an experiment. Consequently, the discrete nature of the energy spectrum needs to be taken into account in order to understand the behavior of these devices. Another interesting aspect of solid-state systems at the nanoscale is that they may exhibit quantum coherence phenomena. These new effects have attracted significant attention in the recent past. Controlling quantum coherence in solid-state nanodevices is one of the major objectives in present-day research. [...]
  § 2 Adiabatic Passage in Three-Level Atoms: In this section, we briefly discuss the basics of adiabatic passage. A more complete discussion of the underlying physics can be found, e.g., in the review articles Refs. [ 1 , 2 ] and in the textbook Ref. [ 7 ] . Consider an atom with a $\Lambda$ -type three-level configuration as shown in Fig. 1 . The long-lived ground states $|0\rangle$ and $|1\rangle$ (energies $\omega_{0}$ , $\omega_{1}$ ) are coupled to an excited state $|e\rangle$ (energy $\omega_{e}$ ) via (classical) laser fields with Rabi frequencies $\Omega_{0}$ , $\Omega_{1}$ . The laser frequencies are assumed to have the same detuning $\Delta$ with respect to the atomic transitions $\Delta=(\omega_{e}-\omega_{0})-\nu_{0}=(\omega_{e}-\omega_{1})-\nu_{1}\ \ .$ Figure 1: Three-level atom with two ground states $|0\rangle$ , $|1\rangle$ coupled to an excited state $|e\rangle$ via laser fields $(1/2)\Omega_{0}\exp{(-i\nu_{0}t)}$ , $(1/2)\Omega_{1}\exp{(-i\nu_{1}t)}$ . Note that there is no direct coupling between the states $|0\rangle$ and $|1\rangle$ . [...]
  § 3 Analogy for a Cooper-pair box with three islands: Our aim is to show that Hamiltonians similar to Eq. ( 5 ) can be ‘tailored’ in solid-state devices. As an example we consider a superconducting Cooper-pair box with three islands. The (single-island) Cooper-pair box is a well-known system as it is a promising candidate for the practical realization of a solid-state qubit (see, e.g., [ 8 ] and references therein). The circuit of a three-island Cooper-pair box is shown in Fig. 2 . The superconducting islands (1) and (2) are coupled via tunable Josephson junctions to the third island (e). [...]
  § 5 Conclusions: We have outlined the basic ideas of adiabatic passage and several examples of its application in solid-state devices that can be realized in superconductor as well as in semiconductor systems. The examples showed that adiabatic passage-like techniques may be used to generate simple charge transfers, to detect non-Abelian holonomies and to control charge transport properties (in particular also to design an alternative kind of charge pumps). In our opinion, it is obvious even from these simple examples that the method of adiabatic passage has significant potential for applications in solid-state physics and deserves appropriate attention also in this field. The authors gratefully acknowledge stimulating discussions with L. Faoro, R. Fazio, A. Kuhn, F. Renzoni, and T. Vorrath.
[3] arXiv:2209.07275v1 | Phonon-blocked junction refrigerators for cryogenic quantum devices
  Refrigeration is an important enabler for quantum technology. The very low energy of the fundamental excitations typically utilized in quantum technology devices and systems requires temperature well below 1 K. Expensive cryostats are utilized in reaching sub-1 K regime and solid-state cooling solutions would revolutionize the field. New electronic micro-coolers based on phonon-blocked semiconduct
  Full text (https://ar5iv.labs.arxiv.org/html/2209.07275v1), excerpts of its own sections:
  § Submission history: From: Emma Mykkänen [ view email ] [v1] Tue, 13 Sep 2022 05:56:18 UTC (670 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Phonon-blocked junction refrigerators for cryogenic quantum devices, by E. Mykk\"anen and J. S. Lehtinen and A. Ronzani and A. Kemppinen and A. Alkurdi and P.-O. Chapuis and M. Prunnila View PDF view license
  § Current browse context:: quant-ph < prev | next > new | recent | 2022-09
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[4] arXiv:0803.3568v1 | Structural and Magnetic Properties of Pyrochlore Solid Solutions (Y,Lu)2Ti2-x(Nb,Ta)xO7+/-y
  The synthesis and characterization of the pyrochlore solid solutions, Y2Ti2-xNbxO7-y, Lu2Ti2-xNbxO7-y, Y2Ti2-xTaxO7-y and Lu2TiTaO7-y (-0.4&lt;y&lt;0.5), is described. Synthesis at 1600 C, and 10-5 Torr yields oxygen deficiency in all systems. All compounds are found to be paramagnetic and semiconducting, with the size of the local moments being less, in some cases substantially less, than the exp
  Full text (https://ar5iv.labs.arxiv.org/html/0803.3568v1), excerpts of its own sections:
  § Submission history: From: Don West [ view email ] [v1] Tue, 25 Mar 2008 14:45:34 UTC (885 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Structural and Magnetic Properties of Pyrochlore Solid Solutions (Y,Lu)2Ti2-x(Nb,Ta)xO7+/-y, by D.V. West and 3 other authors View PDF view license
  § Current browse context:: cond-mat.mtrl-sci < prev | next > new | recent | 2008-03 Change to browse by: cond-mat
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[5] arXiv:1104.4637v1 | Lambda- and Schottky-anomalies in solid-state phase transitions
  The origin of lambda and Schottky anomalies in solid-state phase transitions are analyzed and illustrated. They are shown to be the latent heat of nucleation-and-growth phase transitions.
  Full text (https://ar5iv.labs.arxiv.org/html/1104.4637v1), excerpts of its own sections:
  § Submission history: From: Yuri Mnyukh [ view email ] [v1] Sun, 24 Apr 2011 15:28:26 UTC (427 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Lambda- and Schottky-anomalies in solid-state phase transitions, by Yuri Mnyukh View PDF view license
  § Current browse context:: physics.gen-ph < prev | next > new | recent | 2011-04 Change to browse by: physics
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[6] QNFO: Re-Entry Modes in Solid-State Quantum Devices: A Calculus of Distinctions with Fully Shown Quantitative Benchmarks | https://papers.qnfo.org/papers/re-entry-modes-in-solid-state-quantum-devices-a-calculus-of-distinctions-with-fu
  Laws of Form proposed that the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed, and identified "re-entry" — the re-insertion of a form into its own indicational space — as the mechanism by which self-referential structure acquires dynamical content. This paper asks whether re-entry has an operational reading in solid-state devic
  Full text (https://papers.qnfo.org/papers/re-entry-modes-in-solid-state-quantum-devices-a-calculus-of-distinctions-with-fu), excerpts of its own sections:
  § 1. Introduction: The research question addressed here is direct: re-entry, as formalized in the Laws of Form tradition, is a mode of self-reference in which a distinction is drawn inside the space that the distinction itself creates. Can this mode be given operational content in solid-state devices, where boundaries, edges, and population manifolds are physical rather than notational objects? The motivation is threefold. First, the Laws of Form consolidation known as QNFO synthesizes known quantum correspondences of the indicational calculus and identifies open problem categories, providing a standing register of where the formalism touches physics [9]. [...]
  § 5. Results: We report only numbers computed in Section 4, plus the clearly labeled projection. 1. **Thermal energy scales.** $E_T(1\ \mathrm{K}) = 8.62 \times 10^{-5}\ \mathrm{eV}$; $E_T(0.1\ \mathrm{K}) = 8.62 \times 10^{-6}\ \mathrm{eV}$; $E_T(20\ \mathrm{K}) = 1.72 \times 10^{-3}\ \mathrm{eV}$. Each decade of cooling buys exactly one decade ($10.0\times$) of thermally resolvable level splitting, since $E_T = k_B T$ is linear in $T$. 2. **Schottky peak (Mode III anchor).** For the two-level model, the peak occurs at $x^{*} = \Delta/(k_B T^{*}) \approx 2.3993$, i.e., $T^{*} \approx 0.4168\, \Delta/k_B$, with peak height $C_{\max} \approx 0.439\,R = 3.65\ \mathrm{J\,mol^{-1}\,K^{-1}}$ per mole of two-level units. Example: a splitting $\Delta = 1.72 \times 10^{-3}$ eV (the $20$ K thermal scale of [8]) would place its Schottky peak at $T^{*} = 20/2.3993 = 8.336\ \mathrm{K} \approx 8.3\ \mathrm{K}$ (arithmetic: $20/2.3993 = 8.3357$). 3. [...]
  § 6. Discussion: **Limitations.** The re-entry taxonomy is classificatory, not predictive: it organizes known behaviors but, as presented, generates no new numerical prediction beyond the standard Schottky fingerprint. The bibliography summaries are truncated for [2], [4], [5], [6], and [8]; in each case we used only what the supplied text states and explicitly avoided importing exponent values, moment magnitudes, or cooler performance figures from memory. The formal apparatus of [9] is used only at the level its summary supports (distinction as primitive; re-entry as a recognized configuration); the QNFO consolidation's 7 open problem categories and 4 extensions are not enumerated in the supplied text and are therefore not engaged here. Likewise, the ultrametric claim of [10] is used as a methodological template only; no $p$-adic analysis is performed in this paper. **Failure modes.** The taxonomy fails if the mode assignments of Section 3 are not exclusive or principled — e.g., if any transport anomaly can be relabeled "re-entrant" post hoc, the concept explains nothing. [...]
  § 7. Conclusion: We asked whether re-entry, the self-referential operation identified in the Laws of Form tradition as recorded in [9], has operational content in solid-state devices. Our answer is a classification and a set of fully shown quantitative anchors. Re-entry was formalized as a recursive map $\mathcal{R}[d] = d \circ \mathcal{R}[d]$ on a device's distinction space and realized in three modes: coherent adiabatic re-entry (population returned to its originating manifold, per [3]), tunneling re-entry (quasiparticle amplitude re-entering the edge that defines it, per [2]), and thermodynamic re-entry (latent heat re-entering the heat capacity across a transition, per [7]). [...]
[7] QNFO: JPCUB Competitive Landscape v2.0: System-Level Joules-per-Solution Estimates for 17 Quantum Computing Platforms from Published Specifications | https://papers.qnfo.org/papers/jpcub-competitive-landscape
  The JPCUB P0 protocol (https://papers.qnfo.org/papers/joules-per-solution-metric/) defines the joules-per-solution metric — total system energy per correct answer — as a universal, physics-grounded benchmark for computational platforms. The qwav.tech competitive landscape displays six platforms with one published measurement (IBM Eagle at $0.89$ J/solution) and five entries listed as "Not yet meas
  Full text (https://papers.qnfo.org/papers/jpcub-competitive-landscape), excerpts of its own sections:
  § 1.1 The JPCUB Metric: The joules-per-solution metric $J_S(T, \varepsilon)$ $[$established$]$ defines the total system-level energy (joules) consumed by system $S$ to produce a solution to computational task $T$ at correctness threshold $\varepsilon$: $$J_S(T, \varepsilon) = E_S(T, \varepsilon) = E_{\text{comp}} + E_{\text{mem}} + [...]
  § 4. Results: JPCUB Estimates for 13 Gate-Model Platforms: | Rank | Platform | JPCUB (J/sol) | P_sys | 2Q Gate | 2Q Fidelity | t_exec | E_shot | p_succ | |:----:|:---------|:-------------|:------|:--------|:------------|:------|:------|:------| | 1 | Google Willow | 0.05 | 25.0 kW | 30 ns | 99.95% | 1.9 μs | 0.05 J | 98.5% | | 2 | Google Sycamore | 0.06 | 25.0 kW | 40 ns | 99.8% | 2.5 μs | 0.06 J | 94.2% | | 3 | IQM Garnet | 0.15 | 12.0 kW | 200 ns | 99.5% | 11.0 μs | 0.13 J | 86.0% | | 4 | IBM Heron r2 | 0.28 | 15.0 kW | 300 ns | 99.7% | 17.5 μs | 0.26 J | 91.4% | | 5 | QuEra Aquila | 0.32 | 4.0 kW | 1.5 μs | 99.5% | 70.0 μs | 0.28 J | 86.0% | | 6 | IBM Eagle r3 | 0.59 | 15.0 kW | 500 ns | 99.0% | 29.4 μs | 0.44 J | 74.0% | | 7 | Rigetti Ankaa-3 | 0.61 | 15.0 kW | 400 ns | 98.0% | 22.0 μs | 0.33 J | 54.5% | | 8 | Pasqal Fresnel | 0.62 | 4.0 kW | 2.0 μs | 98.0% | 85.0 μs | 0.34 J | 54.5% | | 9 | Rigetti Aspen-M-3 | 0.71 | 15.0 kW | 400 ns | 97.5% | 22.0 μs | 0.33 J | 46.8% | | 10 | Quantinuum H1-1 | 8.5 | 4.0 kW | 50 μs | 99.8% | 2.00 ms | 8.00 J | 94.2% | | 11 | Quantinuum H2 | 9.6 | 4.5 kW | 50 μs | 99.8% | 2.00 ms | 9.00 J | 94.2% | | 12 [...]
  § 9.4 Summary: The Thermodynamic Inversion: | Problem | Classical cost (J) | Quantum cost (J) | Verdict | |:--------|:-------------------|:-----------------|:--------| | Factoring 15 | $10^{-6}$–$10^{-5}$ | $0.89$ (IBM, published) | **Classical wins $10^5$–$10^6$×** | | RSA-2048 factoring | $\sim 1.6 \times 10^{27}$ (infeasible) | $1.4 \times 10^{10}$–$2.9 \times 10^{11}$ (machine does not exist) | Quantum wins $\sim 10^{16}$× *if built* | | AES-256 key search | $2^{256}$ ops (infeasible) | $3.4 \times 10^{23}$ J, $10^{21}$ yr | **Immune — quantum infeasible** | | Any current NISQ task | lower by $10^6$–$10^7$× | higher | Classical wins on every deployed task | The thermodynamic picture is inverted relative to the investment pattern. For the one problem class where quantum would win (RSA-2048), the machine is 20,000× beyond current capability, the per-operation efficiency is $10^{20}$× above Landauer, and the target is being standardized away. For symmetric crypto, quantum attack is thermodynamically impossible. For every task current machines can run, they are 5–6 orders of magnitude worse than classical. [...]
  § 10. Conclusion: The JPCUB competitive landscape v2.0 extends the qwav.tech roster from 6 to 17 platforms — covering every quantum hardware product with verifiable published specifications. The expanded ranking reveals a structural principle: gate speed is the dominant factor in joules-per-solution across quantum computing architectures. Superconducting platforms (Google Willow at 0.05 J/sol to Rigetti Aspen-M-3 at 0.71 J/sol) lead because sub-microsecond gate speeds produce circuit depths of 2–30 μs — so short that even 12–25 kW of system power yields single-joule energy budgets. Neutral atoms (QuEra Aquila at 0.32 J/sol) achieve competitive JPCUB at one-quarter the power by balancing Rydberg-gate speeds (~1.5 μs) with room-temperature operation. Trapped ions (IonQ Forte at 16.3 J/sol) rank last because microsecond-scale gate times drive execution times to milliseconds — the gate-time penalty overwhelms the room-temperature power advantage. [...]