# Re-Entry Modes in Solid-State Devices: A Calculus of Distinctions Applied to Coherent Transport, Refrigeration, and Anomalous Thermodynamics

## Abstract

Laws of Form proposed that the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed, and identified "re-entry" — the re-insertion of a form into its own indicational space — as the mechanism by which self-referential structure acquires dynamical content. This paper asks whether re-entry has an operational reading in solid-state devices, where a device degree of freedom is coupled back onto the very boundary condition that defines it. We formalize re-entry as a recursive map on a device's distinction space and classify three re-entry modes: coherent adiabatic re-entry (population returned to its originating manifold), tunneling re-entry (quasiparticle amplitude re-entering an edge it defines), and thermodynamic re-entry (anomalies in which latent heat re-enters the order parameter's own heat capacity). Using only numbers stated in the source literature and derivations shown in full, we compute thermal energy scales $k_B T$ at $0.1$ K, $1$ K, and $20$ K; derive the Schottky-anomaly peak position $x^{*} = \Delta/(k_B T^{*}) \approx 2.399$ and peak height $C_{\max} \approx 0.439\,R$ for a two-level system; and linearize the reported $+90\%$ magnetoresistance of LuNi$_2$B$_2$C at $\mu_0 H = 16$ T, $T = 20$ K to a figure of merit $5.625 \times 10^{-2}\ \text{T}^{-1}$. We argue that solid-state platforms — including trapped-ion simulators registered as a falsifiability testbed for ultrametric structure — are natural settings in which re-entry claims become measurable, and we state the conditions under which the framework would be falsified.

## 1. Introduction

The research question addressed here is direct: re-entry, as formalized in the Laws of Form tradition, is a mode of self-reference in which a distinction is drawn inside the space that the distinction itself creates. Can this mode be given operational content in solid-state devices, where boundaries, edges, and population manifolds are physical rather than notational objects?

The motivation is threefold. First, the Laws of Form consolidation known as QNFO synthesizes known quantum correspondences of the indicational calculus and identifies open problem categories, providing a standing register of where the formalism touches physics [9]. Second, a companion register organizes sixteen published records from a single research program into one testable claim: that trapped-ion quantum simulators are the first near-term platform on which ultrametric ($p$-adic) structure in quantum dynamics can be accepted or rejected by measurement [10]. If self-referential structure is to be tested anywhere in the near term, that register identifies where. Third, the solid-state literature already contains phenomena that are naturally described as a degree of freedom acting back on its own defining boundary: coherent population transfer that returns a system to a manifold it started in [3], edge tunneling in which quasiparticle amplitude re-enters the edge whose topological order defines it [2], and phase-transition anomalies in which latent heat re-enters the thermal response of the transitioning system itself [7].

This paper makes no new measurements. Its contribution is a classification and a set of fully shown derivations that convert qualitative claims from the cited literature into quantitative anchors, so that future re-entry experiments in solid-state devices have stated scales against which to be designed. We proceed as follows: Section 2 reviews the cited works strictly within what their supplied summaries state; Section 3 defines the re-entry formalism and the three modes; Section 4 performs all arithmetic explicitly; Section 5 reports only computed numbers; Section 6 discusses limitations and falsification; Section 7 concludes.

## 2. Background and Related Work

We discuss each cited work using only the content of its supplied summary; where a summary is thin, we say so and relate the work to our argument only through what the summary states.

**Superconductivity and materials platforms.** The introduction to high-temperature superconductivity for solid-state chemists [1] presents superconductivity as the complete elimination of electrical resistance below the critical temperature $T_c$, identified as the most important parameter of the field, and notes that since the discovery of copper oxide superconductors 39 years before its writing, solid-state chemists have contributed significantly by discovering new compounds. For our purposes, [1] establishes the materials-discovery substrate on which any solid-state re-entry device would be built: the distinction between superconducting and normal states is a physically drawn boundary whose position is set by $T_c$. The Hall-effect study of LuNi$_2$B$_2$C [8] reports that the Hall resistivity $\rho_{xy}$ is negative in both the normal and mixed states, with no sign reversal of the type typical for high-$T_c$ superconductors, and that a distinct nonlinearity in $\rho_{xy}(H)$ appears in the normal state for $T < 40$ K, accompanied by a large magnetoresistance reaching $+90\%$ for $\mu_0 H = 16$ T at $T = 20$ K; a scaling relation of the form $\rho_{xy} \sim \rho_{xx}^{\beta}$ is discussed. This gives us a concrete, numerically anchored transport anomaly in which the carrier response re-enters the resistive tensor — a candidate transport re-entry mode quantified in Section 4.

**Fractional quantum Hall edges and quasiparticles.** The tunneling study of paired fractional quantum Hall states [2] examines the edge transport properties of the Haldane-Rezayi (HR), Moore-Read (Pfaffian), and Halperin (331) states, provides a table of exponents for tunneling between the edges of paired FQH states in gated 2D structures and for tunneling into the edge from a normal Fermi liquid, and reports findings on the conductance and Andreev reflection of non-Abelions; the summary notes that HR, Pfaffian, and 331 states have (the supplied text is truncated at this point, so the specific conclusion of that comparison is not available to us). We use [2] as the canonical instance of tunneling re-entry: an edge is the boundary that defines the topological phase, and tunneling into or across it is amplitude re-entering the boundary's own indicational space. The hierarchy-state study [4] obtains residual interactions between Laughlin quasiparticles from exact numerical diagonalization of small systems, and reports that the pseudopotentials $V_{\mathrm{QP}}(R)$, describing the interaction energy as a function of relative angular momentum $R$, cannot support Laughlin correlations at certain quasiparticle filling factors (the summary cites examples $\nu_{\mathrm{QE}} = 1/3$ and $\nu_{\mathrm{QH}} = 1/5$), which motivates novel hierarchy states. This is re-entry at the level of effective theory: the quasiparticles generated by a parent state interact through pseudopotentials that then determine whether the parent's correlation structure can be re-entered at a new filling.

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

**Input 1.** Boltzmann's constant $k_B = 8.617333 \times 10^{-5}\ \text{eV/K}$ (physical constant, stated here as the input).

**Input 2.** The sub-1 K operating regime of quantum devices, from [5]: "temperature well below 1 K." We take the representative values $T_1 = 1\ \text{K}$ and $T_2 = 0.1\ \text{K}$.

**Input 3.** The transport-anomaly temperature from [8]: $T_3 = 20\ \text{K}$.

**Derivation.** The thermal energy is $E_T(T) = k_B T$.

$$E_T(T_1) = \left(8.617333 \times 10^{-5}\ \text{eV/K}\right)(1\ \text{K}) = 8.617333 \times 10^{-5}\ \text{eV} \approx 8.62 \times 10^{-5}\ \text{eV}.$$

$$E_T(T_2) = \left(8.617333 \times 10^{-5}\ \text{eV/K}\right)(0.1\ \text{K}) = 8.617333 \times 10^{-6}\ \text{eV} \approx 8.62 \times 10^{-6}\ \text{eV}.$$

$$E_T(T_3) = \left(8.617333 \times 10^{-5}\ \text{eV/K}\right)(20\ \text{K}) = 1.723467 \times 10^{-3}\ \text{eV} \approx 1.72 \times 10^{-3}\ \text{eV}.$$

**Interpretation.** A distinction whose level splitting is $\Delta$ is thermally resolved only if $\Delta \gtrsim E_T$. At $T_2 = 0.1$ K the resolvable scale is $\approx 8.62 \times 10^{-6}$ eV, i.e., $100\times$ finer than at 1 K (ratio $E_T(T_1)/E_T(T_2) = 8.617333 \times 10^{-5} / 8.617333 \times 10^{-6} = 10.0$, exactly, since $E_T$ is linear in $T$). This is the quantitative content of the claim in [5] that sub-1 K operation is required: each decade of temperature buys one decade of resolvable splitting.

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

So $x^{*} \approx 2.399$, i.e., the Schottky peak occurs at

$$T^{*} \approx \frac{\Delta}{2.399\, k_B}.$$

**Derivation of the peak height.** At $x^{*} = 2.3993$, $x^{*}/2 = 1.19965$:

- $\cosh(1.19965)$: $\cosh(1.2) = (e^{1.2} + e^{-1.2})/2 = (3.320117 + 0.301194)/2 = 3.621311/2 = 1.810655$. Adjusting for $\delta = -0.00035$: $\sinh(1.2) = (3.320117 - 0.301194)/2 = 1.509462$, so $\cosh(1.19965) \approx 1.810655 - 0.00035 \times 1.509462 = 1.810655 - 0.000528 = 1.810127$.
- $\cosh^{2}(x^{*}/2) = (1.810127)^{2} = 3.276560$.
- $4 \cosh^{2}(x^{*}/2) = 13.106239$.
- $(x^{*})^{2} = (2.3993)^{2} = 5.756640$.

$$\frac{C_{\max}}{R} = \frac{5.756640}{13.106239} = 0.43920 \approx 0.439.$$

So the maximal Schottky heat capacity is $C_{\max} \approx 0.439\,R$ per mole of independent two-level units, occurring at $k_B T^{*} \approx \Delta / 2.399$, i.e., $T^{*} \approx 0.4168\, \Delta / k_B$ (since $1/2.3993 = 0.41679$).

**Connection to [7].** The cited work shows lambda and Schottky anomalies to be the latent heat of nucleation-and-growth transitions [7]. The two-level result above is the minimal closed form of the Schottky branch of that statement: it gives the experimenter the two numbers — peak position $x^{*} \approx 2.399$ and peak height $0.439\,R$ — against which an observed anomaly in a solid-state device can be tested for two-level (re-entrant latent-heat) origin versus other mechanisms.

### 4.3 Magnetoresistance figure of merit (input from [8])

**Input.** From [8]: magnetoresistance reaching $+90\%$ for $\mu_0 H = 16$ T at $T = 20$ K.

**Derivation.** A magnetoresistance of $+90\%$ means

$$\frac{\rho_{xx}(16\ \text{T}) - \rho_{xx}(0)}{\rho_{xx}(0)} = 0.90 \quad \Rightarrow \quad \frac{\rho_{xx}(16\ \text{T})}{\rho_{xx}(0)} = 1.90.$$

We define a linearized figure of merit (explicitly a linearization, not a claim that the response is linear — [8] states the Hall resistivity response is nonlinear in field):

$$\eta \equiv \frac{0.90}{16\ \text{T}} = 5.625 \times 10^{-2}\ \text{T}^{-1}.$$

Equivalently, per tesla the resistive ratio changes by $\approx 5.6 \times 10^{-2}$ on average across $0 \le \mu_0 H \le 16$ T at $T = 20$ K. This number is a bookkeeping device for comparing transport anomalies across platforms; the nonlinearity reported in [8] means $\eta$ is an average, not a local slope.

### 4.4 Stoichiometric tolerance window (input from [6])

**Input.** From [6]: the oxygen-deficiency parameter spans $-0.4 < y < 0.5$.

**Derivation.** Window width:

$$\Delta y = 0.5 - (-0.4) = 0.9.$$

Window midpoint:

$$y_{\mathrm{mid}} = \frac{0.5 + (-0.4)}{2} = \frac{0.1}{2} = 0.05.$$

The window is asymmetric about stoichiometry $y = 0$: it extends $0.4$ in the oxygen-excess direction and $0.5$ in the deficiency direction, i.e., the deficiency side is larger by $0.5 - 0.4 = 0.1$, or $(0.1/0.9) \times 100\% \approx 11.1\%$ of the window width. This asymmetry is consistent with the report in [6] that synthesis at 1600 °C and $10^{-5}$ Torr yields oxygen deficiency in all systems: the accessible window itself is biased toward deficiency.

### 4.5 Record cadence of the falsifiability register (input from [10])

**Input.** From [10]: sixteen published records spanning December 2025 to August 2026.

**Derivation.** The span December 2025 through August 2026 covers 9 calendar months (Dec, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug). Mean cadence:

$$\frac{16\ \text{records}}{9\ \text{months}} = 1.777\ldots \approx 1.78\ \text{records/month}.$$

At this cadence, a 12-month extension would add $1.78 \times 12 \approx 21$ records (projection, assuming constant cadence; uncertainty is unquantified in the source summary, so this projection carries an unbounded error bar and is offered only as an order-of-magnitude planning figure).

### 4.6 Mode I design constraint (structural, no external numbers)

The adiabaticity condition of Section 3.2 requires

$$T_{\mathrm{pass}} \gg \frac{\max_n |\langle m|\partial_\lambda H|n\rangle|}{\Delta_{\min}^{2}}.$$

No numerical value is computable from the supplied summaries (none of them states a gap or matrix element), so we state the constraint symbolically and flag it as the quantity a Mode I experiment must measure first.

## 5. Results

We report only numbers computed in Section 4, plus the two clearly labeled projections.

1. **Thermal energy scales.** $E_T(1\ \text{K}) = 8.62 \times 10^{-5}\ \text{eV}$; $E_T(0.1\ \text{K}) = 8.62 \times 10^{-6}\ \text{eV}$; $E_T(20\ \text{K}) = 1.72 \times 10^{-3}\ \text{eV}$. Each decade of cooling buys exactly one decade ($10.0\times$) of thermally resolvable level splitting, since $E_T = k_B T$ is linear in $T$.

2. **Schottky peak (Mode III anchor).** For the two-level model, the peak occurs at $x^{*} = \Delta/(k_B T^{*}) \approx 2.3993$, i.e., $T^{*} \approx 0.4168\, \Delta/k_B$, with peak height $C_{\max} \approx 0.439\,R$ per mole of two-level units. Example: a splitting $\Delta = 1.72 \times 10^{-3}$ eV (the $20$ K thermal scale of [8]) would place its Schottky peak at $T^{*} = 20/2.3993 = 8.336\ \text{K} \approx 8.3\ \text{K}$ (arithmetic: $20/2.3993 = 8.3357$).

3. **Transport figure of merit (Mode II-adjacent anchor).** The LuNi$_2$B$_2$C magnetoresistance reported in [8] linearizes to $\eta = 5.625 \times 10^{-2}\ \text{T}^{-1}$ between $0$ and $16$ T at $20$ K, with resistive ratio $1.90$ at $16$ T. This is an average over a response that [8] reports as nonlinear.

4. **Stoichiometric window (platform tolerance).** The pyrochlore solid-solution window of [6] has width $\Delta y = 0.9$, midpoint $y_{\mathrm{mid}} = 0.05$, and a deficiency-side excess of $0.1$, i.e., $\approx 11.1\%$ of the window width.

5. **Register cadence (program metric).** The trapped-ion ultrametric register [10] contains 16 records over 9 months, i.e., $\approx 1.78$ records/month.

6. **Projection (labeled).** If the cadence of item 5 held constant, a 12-month extension of the register would accumulate $\approx 21$ additional records. Assumptions: constant cadence, no gaps in the program; uncertainty unquantified in the source, so this is an order-of-magnitude planning figure only.

7. **Non-computed quantity (flagged).** The adiabatic-passage design constraint $T_{\mathrm{pass}} \gg |\langle m|\partial_\lambda H|n\rangle| / \Delta_{\min}^{2}$ is stated symbolically; no numerical value is derivable from the supplied literature, and we do not invent one.

## 6. Discussion

**Limitations of the framework.** The re-entry operator $\mathcal{R}$ of Section 3 is a formal analogy, not a derived correspondence. We have shown that three classes of solid-state phenomena share a self-consistency structure (a degree of freedom acting on its own defining boundary), but sharing a structure is weaker than sharing a law. The QNFO consolidation records that known quantum correspondences of the indicational calculus exist and that open problem categories remain [9]; whether re-entry in our Mode I–III sense belongs to the proven correspondences or to the open categories is exactly the kind of question that register is designed to settle, and we do not settle it here.

**Limitations of the numbers.** Every quantitative anchor above is either (a) a direct arithmetic consequence of a number stated in a supplied summary ($+90\%$ at 16 T and 20 K from [8]; $-0.4 < y < 0.5$ from [6]; 16 records over 9 months from [10]), or (b) a derivation from a minimal model (the two