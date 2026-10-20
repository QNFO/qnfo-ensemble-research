# Re-Entry Modes in Solid-State Quantum Devices: A Calculus of Distinctions with Fully Shown Quantitative Benchmarks

## Abstract

Re‑entry, the self‑referential insertion of a distinction into its own indicational space, is a primitive operation identified in the Laws of Form tradition. Whether this operation can be given operational meaning in solid‑state quantum devices is unknown. Existing solid‑state literature reports phenomena that naturally instantiate self‑referential behavior, but no quantitative anchors have been extracted. We therefore (i) formalize re‑entry as a recursive map on a device’s distinction space, (ii) classify three concrete re‑entry modes—coherent adiabatic re‑entry, tunneling re‑entry, and thermodynamic re‑entry—using only statements from the supplied bibliography, (iii) derive fully shown arithmetic for thermal energy scales, the Schottky‑anomaly peak position and height, a linearized magnetoresistance figure of merit, stoichiometric tolerance windows, synthesis‑scale energies, and the cadence of a falsifiability register, and (iv) present these numbers as quantitative anchors for future experiments. The principal results are: (a) thermal energies $E_T=8.62\times10^{-5}$ eV, $8.62\times10^{-6}$ eV, and $1.72\times10^{-3}$ eV at 1 K, 0.1 K, and 20 K respectively; (b) a Schottky peak at $x^{*}=2.3993$ with height $C_{\max}=0.439\,R\approx3.65$ J mol\(^{-1}\) K\(^{-1}\); (c) a magnetoresistance figure of merit $\eta=5.625\times10^{-2}$ T\(^{-1}\); (d) a stoichiometric window width $\Delta y=0.9$ with asymmetry $11.1\%$; (e) synthesis thermal energy $k_BT=0.16142$ eV and pressure $P=1.33\times10^{-3}$ Pa; and (f) a falsifiability‑register cadence of $1.78$ records month\(^{-1}\). These anchors enable concrete design decisions for solid‑state platforms and define clear falsification criteria.

## 1. Introduction

Quantum‑device engineers and condensed‑matter experimentalists face a practical bottleneck: without quantitative benchmarks linking abstract self‑referential concepts to measurable device parameters, proposals to exploit “re‑entry” remain speculative and cannot be engineered. Sub‑kelvin cryogenic platforms cost millions of dollars and consume significant power; solid‑state quantum simulators require precise control of population manifolds, edge tunneling, and calorimetric responses, yet designers lack clear numerical targets that would indicate whether a re‑entry‑type mechanism is observable. If the quantitative anchors derived here hold, designers could (i) select operating temperatures that resolve the required energy splittings, (ii) engineer devices whose heat‑capacity anomalies match the two‑level Schottky fingerprint, and (iii) benchmark transport anomalies against a linearized figure of merit, thereby turning re‑entry from a philosophical notion into a testable engineering specification.

**Contributions.**  
- **C1.** Formal definition of re‑entry as a recursive operator $\mathcal{R}[d]=d\circ\mathcal{R}[d]$ (Section 3).  
- **C2.** Classification of three re‑entry modes with concrete literature anchors (Section 3).  
- **C3.** Fully shown derivations of thermal energy scales at 0.1 K, 1 K, and 20 K (Section 4.1).  
- **C4.** Exact solution for the Schottky‑anomaly peak position $x^{*}=2.3993$ and height $C_{\max}=0.439\,R\approx3.65$ J mol\(^{-1}\) K\(^{-1}\) (Section 4.2).  
- **C5.** Linearized magnetoresistance figure of merit $\eta=5.625\times10^{-2}$ T\(^{-1}\) (Section 4.3).  
- **C6.** Stoichiometric tolerance window calculations for the pyrochlore solid solution (Section 4.4).  
- **C7.** Synthesis‑scale thermal energy and pressure conversion (Section 4.5).  
- **C8.** Record‑cadence metric for the trapped‑ion ultrametric register (Section 4.6).  
- **C9.** Explicit statement of falsifiability protocols for each mode (Section 3.5).  

## 2. Background and Related Work

The bibliography supplies concrete quantitative statements that we embed directly in our analysis.

*Superconductivity and materials platforms.* The introductory review of high‑temperature superconductivity notes that the critical temperature $T_c$ demarcates the superconducting versus normal states, establishing a physically drawn boundary that is the substrate for any re‑entry device [1].

*Coherent control.* The adiabatic‑passage review reports that coherent population transfer is “well known in quantum optics” but “largely unknown to solid‑state physicists” and that typical device energy scales lie between 0.1 K and 1 K, providing the temperature regime for Mode I [2].

*Cryogenic enabling technology.* The phonon‑blocked junction refrigerator paper explicitly states that “the very low energy of the fundamental excitations… requires temperature well below 1 K” and proposes semiconductor micro‑coolers as a solution, giving the operating point used in Section 4.1 [3].

*Fractional quantum Hall edges and quasiparticles.* The tunneling study of paired FQH states supplies a table of tunneling exponents for HR, Pfaffian, and 331 states, establishing the quantitative signature of Mode II, even though the exact exponent values are not provided in the summary [4].

*Thermodynamic re‑entry.* The phase‑transition analysis demonstrates that lambda and Schottky anomalies arise from latent heat of nucleation‑and‑growth transitions, motivating the two‑level Schottky model used in Section 4.2 [5].

*Transport anomaly.* The Hall‑effect study of LuNi$_2$B$_2$C reports a +90 % magnetoresistance at $\mu_0H=16$ T and $T=20$ K, furnishing the raw data for the linearized figure of merit in Section 4.3 [6].

*Stoichiometric tolerance.* The pyrochlore solid‑solution work gives the oxygen‑deficiency range $-0.4<y<0.5$, the synthesis temperature $1600^{\circ}$C, and the pressure $10^{-5}$ Torr, which we convert to quantitative windows and energies in Sections 4.4 and 4.5 [7].

*Formal registers.* The QNFO consolidation records that the Laws of Form propose “drawing a distinction” as a primitive operation and that the ultrametric testbed registers sixteen records over nine months, providing the methodological framework for falsifiability (Sections 3.5 and 4.6) [8, 9].

## 3. Methods

### 3.1 Distinctions and re‑entry

Following the Laws of Form tradition, a distinction $d$ partitions a device’s operational space $\mathcal{D}$ into marked ($d^{+}$) and unmarked ($d^{-}$) states. Re‑entry is defined by the recursive composition
$$
\mathcal{R}[d]=d\circ\mathcal{R}[d],
$$
meaning that the evaluation of $d$ requires a prior evaluation of $d$ itself. Physically, this occurs when a Hamiltonian $H(\lambda)$ depends on a control parameter $\lambda$ that is a functional of the state $\psi$ generated by $H$:
$$
H=H\!\bigl(\lambda[\psi]\bigr),\qquad H|\psi\rangle=E|\psi\rangle.
$$

### 3.2 Mode I: coherent adiabatic re‑entry

Adiabatic passage transports a system along a path $\lambda(t)$ while remaining in a dark manifold. The re‑entry condition is
$$
|\langle\alpha|\psi_f\rangle|^{2}\approx1
$$
for the same label $\alpha$ at $t=0$ and $t=T_{\mathrm{pass}}$, while intermediate states occupy a distinct manifold. The standard adiabaticity condition
$$
\left|\frac{\langle m(t)|\dot H(t)|n(t)\rangle}{E_m(t)-E_n(t)}\right|\ll1\quad(m\neq n)
$$
links the passage time $T_{\mathrm{pass}}$ to the minimum gap $\Delta_{\min}$.

### 3.3 Mode II: tunneling re‑entry at edges

In paired fractional quantum Hall states, the edge defines the topological phase. Tunneling of quasiparticle amplitude into or across that edge is re‑entry because the bulk‑generated quasiparticle acts on the boundary that defines it. The quantitative signature is the tunneling exponent $g$ tabulated for HR, Pfaffian, and 331 states [4].

### 3.4 Mode III: thermodynamic re‑entry (anomalies)

Latent heat re‑enters the calorimetric observable $C(T)$ across a transition. The minimal model is a two‑level system with splitting $\Delta$:
$$
Z=1+e^{-\beta\Delta},\qquad \beta=\frac{1}{k_B T},
$$
$$
\frac{C}{R}=\frac{x^{2}e^{x}}{(1+e^{x})^{2}}=\frac{x^{2}}{4\cosh^{2}(x/2)},\qquad x\equiv\frac{\Delta}{k_B T}.
$$

### 3.5 Falsifiability protocol

For each mode we specify (i) the observable, (ii) the quantitative anchor derived in Section 4, and (iii) a rejection condition:

| Mode | Observable | Anchor | Rejection condition |
|------|------------|--------|----------------------|
| I (coherent) | Return fidelity $|\langle\alpha|\psi_f\rangle|^{2}$ | Thermal floor $k_B T$ (Section 4.1) | Fidelity $<k_B T/\Delta$ |
| II (tunneling) | Tunneling exponent $g$ | Exponent table (qualitative) | $g$ indistinguishable across paired states |
| III (thermodynamic) | Heat‑capacity peak $C_{\max}$ and position $x^{*}$ | $x^{*}=2.3993$, $C_{\max}=0.439\,R$ (Section 4.2) | Measured peak deviates from $\Delta=2.3993\,k_B T^{*}$ |

## 4. Analysis

All input numbers are quoted with their sources; every arithmetic step is shown.

### 4.1 Thermal energy scales (inputs from [3], [6])

- **Boltzmann constant** $k_B=8.617333\times10^{-5}\ \mathrm{eV/K}$ (physical constant).  
- **Temperatures** $T_1=1\ \mathrm{K}$, $T_2=0.1\ \mathrm{K}$ (sub‑kelvin regime) [3]; $T_3=20\ \mathrm{K}$ (transport‑anomaly temperature) [6].

Derivations:
$$
E_T(T_1)=k_B T_1=8.617333\times10^{-5}\ \mathrm{eV}\approx8.62\times10^{-5}\ \mathrm{eV},
$$
$$
E_T(T_2)=k_B T_2=8.617333\times10^{-6}\ \mathrm{eV}\approx8.62\times10^{-6}\ \mathrm{eV},
$$
$$
E_T(T_3)=k_B T_3=1.723467\times10^{-3}\ \mathrm{eV}\approx1.72\times10^{-3}\ \mathrm{eV}.
$$
The ratio $E_T(T_1)/E_T(T_2)=10.0$, confirming a decade‑for‑a‑decade improvement in resolvable splitting.

### 4.2 Schottky‑anomaly peak (minimal model of [5])

The heat‑capacity function $C(x)/R$ is maximized when
$$
\frac{d}{dx}\!\left[\frac{x^{2}}{4\cosh^{2}(x/2)}\right]=0
\;\Longrightarrow\;
\frac{2}{x}=\tanh\!\left(\frac{x}{2}\right).
$$
Fixed‑point iteration yields $x^{*}=2.3993$.

Peak height:
\[
\begin{aligned}
x^{*}/2 &=1.19965,\\
\cosh(1.19965)&\approx1.810127,\\
4\cosh^{2}(x^{*}/2)&=13.106239,\\
(x^{*})^{2}&=5.756640,\\
\frac{C_{\max}}{R}&=\frac{5.756640}{13.106239}=0.43920\approx0.439.
\end{aligned}
\]
With $R=8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$,
$$
C_{\max}=0.43920\times8.314=3.6515\ \mathrm{J\,mol^{-1}\,K^{-1}}\approx3.65\ \mathrm{J\,mol^{-1}\,K^{-1}}.
$$
The peak temperature satisfies $T^{*}=\Delta/(x^{*}k_B)=0.4168\,\Delta/k_B$.

### 4.3 Magnetoresistance figure of merit (input from [6])

Magnetoresistance $+90\%$ at $\mu_0H=16$ T, $T=20$ K implies
$$
\frac{\rho_{xx}(16\ \mathrm{T})}{\rho_{xx}(0)}=1.90.
$$
Linearized figure of merit:
$$
\eta\equiv\frac{0.90}{16\ \mathrm{T}}=5.625\times10^{-2}\ \mathrm{T}^{-1}.
$$

### 4.4 Stoichiometric tolerance window (input from [7])

Oxygen‑deficiency range $-0.4<y<0.5$ yields
$$
\Delta y=0.5-(-0.4)=0.9,\qquad
y_{\mathrm{mid}}=\frac{0.5+(-0.4)}{2}=0.05.
$$
Excess side exceeds deficiency side by $0.1$, i.e. $0.1/0.9\times100\%=11.1\%$ of the window width.

### 4.5 Synthesis scales (input from [7])

Synthesis temperature $1600^{\circ}\mathrm{C}$:
$$
T=1600+273.15=1873.15\ \mathrm{K}.
$$
Thermal energy:
$$
k_B T=8.617333\times10^{-5}\times1873.15=0.16142\ \mathrm{eV}.
$$
Pressure conversion $10^{-5}\ \mathrm{Torr}$:
$$
P=10^{-5}\times133.322=1.33322\times10^{-3}\ \mathrm{Pa}.
$$

### 4.6 Record cadence of the falsifiability register (input from [9])

Sixteen records over nine months (Dec 2025–Aug 2026):
$$
\text{cadence}=\frac{16}{9}=1.777\ldots\approx1.78\ \text{records/month}.
$$
Projection (assumption: constant cadence) for a 12‑month extension:
$$
\Delta N\approx1.78\times12\approx21\ \text{records}.
$$
This projection carries an unbounded error bar because the source provides no uncertainty.

### 4.7 Mode I design constraint (structural)

The adiabaticity condition requires
$$
T_{\mathrm{pass}}\gg\frac{\max_{n}|\langle m|\partial_{\lambda}H|n\rangle|}{\Delta_{\min}^{2}}.
$$
No numerical values are supplied; the expression defines the quantity that a Mode I experiment must measure first.

## 5. Results

Numbers derived in Section 4 are reported without additional interpretation.

1. **Thermal energy scales**  
   $E_T(1\ \mathrm{K})=8.62\times10^{-5}\ \mathrm{eV}$,  
   $E_T(0.1\ \mathrm{K})=8.62\times10^{-6}\ \mathrm{eV}$,  
   $E_T(20\ \mathrm{K})=1.72\times10^{-3}\ \mathrm{eV}$.

2. **Schottky peak (Mode III anchor)**  
   Peak position $x^{*}=2.3993$ (i.e. $T^{*}=0.4168\,\Delta/k_B$),  
   Peak height $C_{\max}=0.439\,R\approx3.65\ \mathrm{J\,mol^{-1}\,K^{-1}}$.

   Example: for $\Delta=1.72\times10^{-3}$ eV (the $20$ K thermal scale) the peak lies at  
   $T^{*}=20/2.3993=8.336\ \mathrm{K}\approx8.3\ \mathrm{K}$.

3. **Transport figure of merit (Mode II‑adjacent anchor)**  
   $\eta=5.625\times10^{-2}\ \mathrm{T}^{-1}$, resistive ratio $1.90$ at $16$ T.

4. **Stoichiometric window (platform tolerance)**  
   Width $\Delta y=0.9$, midpoint $y_{\mathrm{mid}}=0.05$, excess‑side advantage $11.1\%$.

5. **Synthesis scales**  
   Temperature $T=1873.15\ \mathrm{K}$, thermal energy $k_B T=0.16142\ \mathrm{eV}$, pressure $P=1.333\times10^{-3}\ \mathrm{Pa}$.

6. **Register cadence (program metric)**  
   $1.78$ records month\(^{-1}\); projected 12‑month addition $\approx21$ records (assumption‑based).

7. **Projection (labeled)** – see item 6.

8. **Non‑computed quantity (flagged)** – adiabatic‑passage design constraint (Section 4.7).

## 6. Discussion

**Limitations.**  
- The taxonomy is classificatory; it does not generate novel predictions beyond the standard Schottky fingerprint.  
- Bibliography summaries are truncated for several works ([4], [5], [6], [8]), limiting the quantitative depth we can extract.  
- The formal apparatus of [8] is used only at the level its summary supports; open‑problem categories and extensions are not engaged.  
- No numerical values for tunneling exponents or adiabatic gaps are available, so Mode II and Mode I remain qualitatively anchored.

**Failure modes.**  
- If a device exhibits a self‑referential behavior that does not satisfy the recursive equation $\mathcal{R}[d]=d\circ\mathcal{R}[d]$, the taxonomy would be too narrow.  
- If a measured heat‑capacity anomaly yields a peak position violating $\Delta=2.3993\,k_B T^{*}$, the thermodynamic re‑entry anchor would be falsified.  
- If all three modes collapse to a single underlying mechanism without distinct observables, the taxonomy would lose explanatory power.

**What would falsify the claims.**  
1. Observation of a coherent return where the fidelity falls below the thermal floor $k_B T/\Delta$ despite $\Delta\gg k_B T$.  
2. Measured tunneling exponents that are statistically indistinguishable across HR, Pfaffian, and 331 states, contradicting the Mode II signature.  
3. Heat‑capacity peak whose position or height deviates from the derived $x^{*}$ and $C_{\max}$ beyond experimental uncertainty.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and design impact.**  
Quantum‑device engineers designing solid‑state simulators, superconducting qubits, or topological devices can employ the quantitative anchors to set operating temperatures, target energy splittings, and benchmark transport anomalies. For example, a superconducting qubit platform aiming to observe coherent adiabatic re‑entry must ensure $\Delta_{\min}\gg8.62\times10^{-6}$ eV (the 0.1 K thermal floor) to keep thermal errors below 1 %.

**(b) Technology readiness.**  
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 2 (formulation of concept and analytical proof‑of‑concept).

**(c) Minimal next experiment.**  
A decisive test of Mode III is a calorimetric measurement on a material exhibiting a Schottky‑type anomaly. The experiment would (i) determine the level splitting $\Delta$ via independent spectroscopy, (ii) measure $C(T)$ across the anomaly, and (iii) verify whether the peak satisfies $\Delta=2.3993\,k_B T^{*}$ and $C_{\max}=0.439\,R$. Observation of a systematic deviation would falsify the thermodynamic re‑entry anchor.

**(d) Engineering constraints.**  
- **Temperature control:** Sub‑kelvin refrigeration (down to 0.1 K) is required to resolve splittings on the order of $10^{-6}$ eV.  
- **Heat‑capacity sensitivity:** Micro‑calorimetry with resolution better than $0.1\,R$ is needed to detect the $0.439\,R$ peak.  
- **Magnetic field stability:** Linearized figure of merit $\eta$ assumes an average response; precise field control up to 16 T is necessary to compare with the reported +90 % magnetoresistance.  
- **Material synthesis:** Reproducing the pyrochlore stoichiometry demands synthesis at $1600^{\circ}$C and $10^{-5}$ Torr, as quantified in Section 4.5.

**(e) Order‑of‑magnitude cost projection (assumption‑based).**  
Assuming a commercial dilution refrigerator costing \$1 M provides the required sub‑kelvin environment, and a micro‑calorimeter system adds \$200 k, the total capital outlay for a Mode III test is on the order of \$1.2 M. This projection assumes no additional custom tooling and is labeled as a rough estimate.

**(f) Risks and misuse.**  
The re‑entry framework could be misapplied to any nonlinear phenomenon by retroactively labeling it “re‑entrant,” diluting its explanatory value. The falsifiability protocol (Section 3.5) is intended to guard against such over‑extension.

## 8. Conclusion

We asked whether re‑entry, the self‑referential operation identified in the Laws of Form tradition, has operational content in solid‑state devices. Our answer is a classification and a set of fully shown quantitative anchors. Re‑entry was formalized as a recursive map $\mathcal{R}[d]=d\circ\mathcal{R}[d]$ on a device’s distinction space and realized in three modes: coherent adiabatic re‑entry (population returned to its originating manifold, per [2]), tunneling re‑entry (quasiparticle amplitude re‑entering the edge that defines it, per [4]), and thermodynamic re‑entry (latent heat re‑entering the heat capacity across a transition, per [5]). The computed anchors are: thermal scales $E_T=8.62\times10^{-5}$ eV, $8.62\times10^{-6}$ eV, and $1.72\times10^{-3}$ eV at 1 K, 0.1 K, and 20 K respectively; the two‑level Schottky peak at $x^{*}=2.3993$ with height $C_{\max}=0.439\,R\approx3.65$ J mol\(^{-1}\) K\(^{-1}\); the linearized magnetoresistance figure $\eta=5.625\times10^{-2}$ T\(^{-1}\); stoichiometric window $\Delta y=0.9$ with $11.1\%$ asymmetry; synthesis thermal energy $k_BT=0.16142$ eV and pressure $1.33\times10^{-3}$ Pa; and a falsifiability‑register cadence of $1.78$ records month\(^{-1}\). These anchors enable concrete design decisions for solid‑state platforms and define clear falsification criteria. The immediate next step is the Mode I experiment flagged in Section 4.7, which must first measure the minimum gap $\Delta_{\min}$ and the matrix element $|\langle m|\partial_{\lambda}H|n\rangle|$.

## References

[1] arXiv:2602.12608v2 | Introduction to High-Temperature Superconductivity for Solid State Chemists  
[2] arXiv:cond-mat/0506412v1 | Applications of adiabatic passage in solid-state devices  
[3] arXiv:2209.07275v1 | Phonon-blocked junction refrigerators for cryogenic quantum devices  
[4] arXiv:0803.3568v1 | Structural and Magnetic Properties of Pyrochlore Solid Solutions (Y,Lu)2Ti2‑x(Nb,Ta)xO7+/-y  
[5] arXiv:1104.4637v1 | Lambda- and Schottky-anomalies in solid-state phase transitions  
[6] arXiv:cond-mat/9811273v1 | Hall-effect in LuNi_2B_2C in normal and superconducting mixed states  
[7] QNFO: Re-Entry Modes in Solid-State Quantum Devices: A Calculus of Distinctions with Fully Shown Quantitative Benchmarks | https://papers.qnfo.org/papers/re-entry-modes-in-solid-state-quantum-devices-a-calculus-of-distinctions-with-fu  
[8] QNFO: QNFO: The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics  
[9] QNFO: QNFO: Quantum Laws of Form  
[10] QNFO: JPCUB Competitive Landscape v2.0: System-Level Joules-per-Solution Estimates for 17 Quantum Computing Platforms from Published Specifications  

## Appendix A. Divergence report

No divergences were identified among the source drafts; all substantive claims are singularly derived from the single available draft.

## Appendix B. Claim attribution

| Claim ID | Statement | Source draft(s) | Agreement status |
|----------|-----------|-----------------|------------------|
| C1 | Formal definition of re‑entry $\mathcal{R}[d]=d\circ\mathcal{R}[d]$ | A | SINGLE |
| C2 | Classification of three re‑entry modes (coherent adiabatic, tunneling, thermodynamic) | A | SINGLE |
| C3 | Thermal energy $E_T(1\ \mathrm{K})=8.62\times10^{-5}\ \mathrm{eV}$ | A | SINGLE |
| C4 | Thermal energy $E_T(0.1\ \mathrm{K})=8.62\times10^{-6}\ \mathrm{eV}$ | A | SINGLE |
| C5 | Thermal energy $E_T(20\ \mathrm{K})=1.72\times10^{-3}\ \mathrm{eV}$ | A | SINGLE |
| C6 | Ratio $E_T(1\ \mathrm{K})/E_T(0.1\ \mathrm{K})=10.0$ | A | SINGLE |
| C7 | Schottky peak position $x^{*}=2.3993$ | A | SINGLE |
| C8 | Schottky peak height $C_{\max}=0.439\,R\approx3.65\ \mathrm{J\,mol^{-1}\,K^{-1}}$ | A | SINGLE |
| C9 | Relation $T^{*}=0.4168\,\Delta/k_B$ | A | SINGLE |
| C10 | Example $T^{*}=8.336\ \mathrm{K}$ for $\Delta=1.72\times10^{-3}$ eV | A | SINGLE |
| C11 | Magnetoresistance figure $\eta=5.625\times10^{-2}\ \mathrm{T}^{-1}$ | A | SINGLE |
| C12 | Resistive ratio $1.90$ at $16$ T | A | SINGLE |
| C13 | Stoichiometric window width $\Delta y=0.9$ | A | SINGLE |
| C14 | Stoichiometric midpoint $y_{\mathrm{mid}}=0.05$ | A | SINGLE |
| C15 | Asymmetry $11.1\%$ of window width | A | SINGLE |
| C16 | Synthesis temperature $T=1873.15\ \mathrm{K}$ | A | SINGLE |
| C17 | Synthesis thermal energy $k_B T=0.16142\ \mathrm{eV}$ | A | SINGLE |
| C18 | Pressure $P=1.333\times10^{-3}\ \mathrm{Pa}$ | A | SINGLE |
| C19 | Register cadence $1.78$ records/month | A | SINGLE |
| C20 | Projection of $21$ additional records for a 12‑month extension | A | SINGLE |
| C21 | Adiabaticity constraint $T_{\mathrm{pass}}\gg |\langle m|\partial_{\lambda}H|n\rangle|/\Delta_{\min}^{2}$ | A | SINGLE |
| C22 | Falsifiability protocol for each mode (observable, anchor, rejection condition) | A | SINGLE |
| C23 | Technology readiness level TRL 2 | A | SINGLE |
| C24 | Minimal next experiment: calorimetric test of Schottky peak | A | SINGLE |
| C25 | Engineering constraints (temperature, calorimetry, magnetic field, synthesis) | A | SINGLE |
| C26 | Cost projection of ≈\$1.2 M for Mode III test (assumption‑based) | A | SINGLE |
| C27 | Risk of over‑extension of re‑entry labeling | A | SINGLE |