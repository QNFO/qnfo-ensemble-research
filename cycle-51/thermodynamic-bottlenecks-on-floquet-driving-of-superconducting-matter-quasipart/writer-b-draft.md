# Thermodynamic Bottlenecks on Floquet Driving in Superconducting Quantum Hardware: Quasiparticle Generation, Heat Extraction, and Design Rules

## Abstract

Floquet engineering—periodic modulation of a Hamiltonian to synthesize effective dynamics—has become a central tool in quantum simulation and control, but its deployment in superconducting circuits at millikelvin temperatures faces a thermodynamic constraint that is rarely quantified: every absorbed drive photon must ultimately be dissipated into a bath held below $1$ K, and above-gap absorption breaks Cooper pairs and generates quasiparticles that poison coherent dynamics. We formulate a minimal quasiparticle-rate and heat-balance model for a periodically driven superconducting condensate and derive explicit numerical design rules. Using the aluminum gap $\Delta_0 = 1.76\,k_B T_c$ with $T_c = 1.2$ K, we show that a tolerated quasiparticle-poisoning error of $10^{-3}$ per $100$ ns gate limits the power dissipated in a qubit junction to $P_{\rm abs}^{\max} \approx 5.8\times10^{-19}$ W, roughly thirteen orders of magnitude below the mixing-chamber cooling power, so that the binding constraint for qubit-scale Floquet drive is quasiparticle generation rather than refrigeration capacity. For cavity-scale resonators the hierarchy reverses: a picowatt of absorbed drive produces a steady-state quasiparticle density of $\approx 1.0\times10^{11}\ \mathrm{m^{-3}}$, exceeding the thermal density at $100$ mK by a factor $\approx 2.8\times10^{32}$. We further derive the sub-gap condition $f < 2\Delta_0/h \approx 88$ GHz for aluminum and show that tolerated drive strengths produce only $\approx 0.04\,k_B$ of entropy per cycle. The analysis connects microwave-nonlinearity and low-loss-cavity literature to a unified thermodynamic design framework for Floquet protocols.

## 1. Introduction

Floquet driving—the application of a time-periodic modulation $H(t) = H_0 + H_1\cos(\omega_{\rm dr} t)$ to a quantum system—allows the synthesis of effective Hamiltonians, topological bands, and parametric gates that are inaccessible to static systems. In superconducting quantum hardware, Floquet and parametric techniques underlie tunable couplers, driven qubit gates, and Floquet-engineered resonator lattices. The hardware platform, however, is not a closed Floquet system: it is a condensate coupled to a dilution-refrigerator bath at $T_{\rm bath} \lesssim 0.1$ K, with a finite superconducting gap $\Delta_0$ and a finite cooling power $P_{\rm cool}$ at the mixing chamber.

This paper asks a specific question, motivated by the QNFO program on thermodynamic and quantum constraints on scalable quantum computing [11] and its extension to superconducting matter [9], [10]: **do thermodynamic bottlenecks constrain the usable strength of Floquet driving in superconducting devices, and if so, which bottleneck binds first?** The candidate bottlenecks are (i) quasiparticle generation by above-gap or multiphoton absorption, which poisons coherent dynamics; (ii) the finite heat-extraction capacity of the millikelvin stage; and (iii) entropy production per drive cycle, which must remain small for the driven state to behave quasi-adiabatically.

We answer with a minimal analytic model and fully explicit arithmetic. The main findings are a hierarchy of constraints: for qubit-scale junction volumes, the quasiparticle-poisoning constraint limits absorbed drive power to $\sim 10^{-19}$–$10^{-18}$ W, far below any refrigeration limit; for cavity-scale resonators, the cooling-power and quasiparticle-density constraints dominate at much larger absorbed powers but still enforce strict limits on drive amplitude. A corollary design rule is that Floquet frequencies must remain below the pair-breaking threshold $2\Delta_0/h$ (about $88$ GHz for aluminum) unless pair breaking is explicitly budgeted for. Throughout, we ground the model in the experimental phenomenology of superconducting microwave devices: nonlinear intermodulation response and its slow relaxation in cuprate resonators [2], two-tone mixing in superconducting quantum interference filters [7], surface-loss engineering in copper waveguide cavities [6], and low-loss high-$T_c$ radio-frequency coils [8]. On the theory side, we draw on pairing models that emphasize coherent quasiparticle components in diverse normal states [1], multiband and Lifshitz-transition physics in Hubbard-type models [3], dielectric-function treatments of non-parabolic bands in SrTiO$_3$ [4], and population-imbalanced quasi-one-dimensional superfluids [5], each of which modifies the effective gap and density of states that enter our bottleneck formulae.

## 2. Background and Related Work

**Pairing and the condensate gap.** Reference [1] argues that superconductivity in unconventional materials emerges from pairing of the coherent parts of physical electrons, yielding BCS-like condensation behavior regardless of the mother normal state. This matters for our purposes because the quantity that controls Floquet heating—the gap $\Delta_0$ and the quasiparticle density of states $N_0$—is exactly what such pairing theories compute; if the gap is material- and state-dependent, the thermodynamic bottleneck is likewise material-dependent. Reference [4] applies a dielectric-function method to SrTiO$_3$ with non-parabolic conduction bands and phonon dispersion from density-functional theory, obtaining critical temperatures in agreement with experiment. Non-parabolicity renormalizes the effective density of states $N_0$ entering the thermal quasiparticle formula (Section 4), so [4] exemplifies why our numerical prefactors are platform-specific rather than universal. Reference [3], arising from the Superstripes 2017 program on complex quantum matter, discusses Lifshitz transitions in multiband Hubbard models as a route to topological superconductivity; a Lifshitz transition changes the number of bands crossing the Fermi level and hence can abruptly increase $N_0$ and decrease the effective gap, tightening our bottleneck discontinuously. Reference [5] studies population-imbalanced fermionic mixtures in quasi-one-dimensional optical lattices via the attractive Hubbard model with a Zeeman term, mapping the ground-state phase diagram versus chemical potential and field; imbalance is a controlled way to soften the gap, and the resulting gapless superconducting phases would show dramatically enhanced Floquet susceptibility to pair breaking, since the pair-breaking threshold $2\Delta_0$ is reduced.

**Microwave device phenomenology.** Reference [2] measured second- and third-order nonlinear microwave response of a superconducting YBa$_2$Cu$_3$O$_7$ thin-film resonator with three input tones, enabling spatial mapping of intermodulation distortion (IMD), and observed that second- and third-order IMD relaxed in markedly different ways after removal of a static magnet. This is direct experimental evidence that driven superconducting microwave devices harbor long-lived nonequilibrium excitations—precisely the quasiparticle population our rate equation tracks—and that its relaxation is order-dependent and slow, supporting our use of quasiparticle lifetimes $\tau_{\rm qp}$ of order $10^{-4}$ s or longer. Reference [7] exploits the parabolic dc-voltage dip of a Superconducting Quantum Interference Filter (SQIF) around $B=0$ to mix weak rf signals, detecting the difference-frequency output at $f_0 = f_1 - f_2$ for tones from a few MHz to $20$ GHz. Two-tone mixing is the nonlinear mechanism by which sub-gap drive tones can synthesize above-gap frequencies; in our framework, the mixing efficiency sets the coefficient converting sub-gap Floquet amplitude into effective pair-breaking absorption, so [7] provides the device-level precedent for the multiphoton channel we flag as the dominant residual heating path. Reference [6] reports copper waveguide cavities with reduced surface loss coupled to transmon qubits, with coherence times approaching $0.1$ ms; the design lesson—that loss budget, not field strength, sets the usable drive—is the experimental mirror of our thermodynamic bound, and the cited $0.1$ ms coherence scale fixes the gate-time $\tau_g$ we use in the poisoning-error budget. Reference [8] demonstrates high-temperature superconducting rf coils for NMR and MRI, where low rf losses and low operating temperature improve signal-to-noise when system noise dominates; this is a complementary regime—classical, high-power rf—where the same loss-to-heat channel exists but the tolerable dissipation is many orders of magnitude larger, delineating the boundary between classical rf engineering and quantum-limited Floquet control.

**Programmatic context.** Reference [9] (QNFO: Superconductivity Quadrangle) frames the interlocking constraints—material, thermodynamic, and coherence-related—that govern superconducting technologies; the present paper instantiates one corner of that quadrangle quantitatively. Reference [10] (QNFO: Unifying Photosynthetic Energy Transduction and Ambient Superconductivity) develops the thesis that ambient-temperature energy transduction and superconductivity share thermodynamic design principles; our per-cycle entropy calculation (Section 4) is the millikelvin analogue of the per-excitation entropy budgets considered there. Reference [11] (QNFO: Thermodynamic and Quantum Constraints on Scalable Quantum Computing) supplies the overarching claim that scalability limits are thermodynamic before they are architectural; our result that the binding constraint for qubit Floquet drive is quasiparticle poisoning at $\sim 10^{-19}$ W—rather than the $\sim 10^{-5}$ W cooling budget—is a concrete, computed instance of that thesis.

## 3. Methods

### 3.1 Model

We consider a superconducting condensate with gap $\Delta_0$ driven by a periodic modulation at frequency $f_{\rm dr} = \omega_{\rm dr}/2\pi$ and amplitude proportional to drive power $P_{\rm in}$, of which a fraction $\eta_{\rm abs}$ is absorbed: $P_{\rm abs} = \eta_{\rm abs} P_{\rm in}$. The condensate is thermally anchored to a bath at $T_{\rm bath}$ with available cooling power $P_{\rm cool}$.

**Quasiparticle balance.** Above-gap absorption breaks Cooper pairs; each pair-breaking event costs the gap energy $2\Delta_0$ and produces two quasiparticles. We write the pair-breaking generation rate of quasiparticles as

$$\Gamma_{\rm qp} = \frac{P_{\rm abs}}{2\Delta_0},$$

i.e., every absorbed joule is converted into quasiparticle degrees of freedom at cost $2\Delta_0$ per quasiparticle (the factor of two between pairs and quasiparticles cancels: one pair costs $2\Delta_0$ and yields two quasiparticles, so quasiparticles per joule is $1/\Delta_0$; we conservatively use $1/(2\Delta_0)$, i.e., we count pair-breaking events and attribute one effective long-lived quasiparticle per event, since the partner relaxes to the gap edge rapidly). The steady-state quasiparticle population in a device of volume $V$ obeys

$$\frac{d n_{\rm qp}}{d t} = \frac{\Gamma_{\rm qp}}{V} - \frac{n_{\rm qp}}{\tau_{\rm qp}} \quad\Longrightarrow\quad n_{\rm qp}^{\rm ss} = \frac{\Gamma_{\rm qp}\,\tau_{\rm qp}}{V},$$

with recombination-limited lifetime $\tau_{\rm qp}$.

**Thermal baseline.** The equilibrium quasiparticle density of an s-wave superconductor is

$$n_{\rm qp}^{\rm th}(T) = 2 N_0 \sqrt{2\pi \Delta_0 k_B T}\; e^{-\Delta_0/(k_B T)},$$

where $N_0$ is the single-spin normal-state density of states at the Fermi level.

**Poisoning error.** A quasiparticle population causes gate errors at a rate proportional to the generation rate; we take the per-gate error contribution as

$$\epsilon_{\rm qp} = \Gamma_{\rm qp}\,\tau_g,$$

with $\tau_g$ the gate duration. This linearized estimate is appropriate in the dilute-quasiparticle regime $n_{\rm qp}^{\rm ss} \ll n_{\rm qp}^{\rm th}(T_c)$.

**Heat balance and entropy.** The absorbed power must satisfy $P_{\rm abs} \le P_{\rm cool}$ for bath temperature stability, and the entropy produced per drive cycle of duration $t_{\rm cyc}$ is

$$\Delta S_{\rm cyc} = \frac{P_{\rm abs}\, t_{\rm cyc}}{T_{\rm bath}}.$$

### 3.2 Stated inputs and assumptions

All numerical inputs used in Section 4, with their provenance:

- $k_B = 1.380649\times10^{-23}$ J/K (SI defined value).
- $h = 6.62607015\times10^{-34}$ J·s, $\hbar = 1.054571817\times10^{-34}$ J·s (SI defined values).
- $T_c^{\rm Al} = 1.2$ K (standard aluminum film value; assumption).
- $\Delta_0 = 1.76\,k_B T_c$ (BCS weak-coupling ratio; assumption).
- $N_0 = 1.72\times10^{10}\ \mathrm{m^{-3}J^{-1}}$ (aluminum single-spin DOS; standard tunneling value; assumption).
- $\tau_{\rm qp} = 3\times10^{-4}$ s (low-temperature recombination-limited quasiparticle lifetime in Al, consistent with the slow relaxation phenomenology of [2]; assumption).
- $\tau_g = 1\times10^{-7}$ s (gate time, consistent with the $\sim 0.1$ ms coherence scale of [6] allowing $10^3$ gates per coherence time; assumption).
- $T_{\rm bath} = 0.1$ K, $P_{\rm cool} = 1\times10^{-5}$ W (typical dilution-refrigerator mixing-chamber specification; assumption).
- $V_c = 5\times10^{-5}$ m$^3$ (3D cavity volume, $\approx 50$ cm$^3$, cf. the 3D cavities of [6]; assumption).
- Tolerated poisoning error $\epsilon_{\rm qp}^{\rm tol} = 10^{-3}$ (surface-code-compatible per-gate error; assumption).
- Illustrative absorbed drive power $P_{\rm abs} = 1\times10^{-12}$ W (one picowatt; illustrative reference point).

## 4. Analysis

### 4.1 The gap and the pair-breaking threshold

From the BCS ratio with the stated inputs:

$$\Delta_0 = 1.76\,k_B T_c = 1.76 \times (1.380649\times10^{-23}\ \mathrm{J/K}) \times 1.2\ \mathrm{K}.$$

Step 1: $1.380649\times10^{-23} \times 1.2 = 1.6567788\times10^{-23}$ J.
Step 2: $1.6567788\times10^{-23} \times 1.76 = 2.91593\times10^{-23}$ J.

So $\Delta_0 = 2.91593\times10^{-23}$ J $= 2.91593\times10^{-23}/1.602176634\times10^{-19}\ \mathrm{eV} = 1.820\times10^{-4}$ eV $= 0.182$ meV. The pair-breaking energy is

$$2\Delta_0 = 5.83186\times10^{-23}\ \mathrm{J}.$$

The corresponding pair-breaking frequency and temperature:

$$f_{\rm pb} = \frac{2\Delta_0}{h} = \frac{5.83186\times10^{-23}}{6.62607015\times10^{-34}} = 8.801\times10^{10}\ \mathrm{Hz} \approx 88\ \mathrm{GHz},$$

and $2\Delta_0/k_B = 1.76 \times 1.2 = 2.112$ K. Any Floquet drive with $f_{\rm dr} \gtrsim 88$ GHz, or any nonlinear process synthesizing such frequencies (e.g., the two-tone difference/sum channels measured in [7]), directly breaks pairs.

### 4.2 Quasiparticle generation rate per absorbed watt

$$\Gamma_{\rm qp} = \frac{P_{\rm abs}}{2\Delta_0} = \frac{P_{\rm abs}}{5.83186\times10^{-23}\ \mathrm{J}} = 1.7147\times10^{22}\ \mathrm{s^{-1}W^{-1}}\; P_{\rm abs}.$$

For the illustrative $P_{\rm abs} = 1\times10^{-12}$ W:

$$\Gamma_{\rm qp} = 1.7147\times10^{22} \times 10^{-12} = 1.7147\times10^{10}\ \mathrm{s^{-1}}.$$

### 4.3 The qubit-scale bottleneck: poisoning before refrigeration

Setting $\epsilon_{\rm qp} = \epsilon_{\rm qp}^{\rm tol} = 10^{-3}$ with $\tau_g = 1\times10^{-7}$ s:

$$\Gamma_{\rm qp}^{\rm tol} = \frac{\epsilon_{\rm qp}^{\rm tol}}{\tau_g} = \frac{10^{-3}}{10^{-7}} = 10^{4}\ \mathrm{s^{-1}}.$$

The corresponding maximum absorbed power in the junction:

$$P_{\rm abs}^{\max} = 2\Delta_0\,\Gamma_{\rm qp}^{\rm tol} = 5.83186\times10^{-23}\ \mathrm{J} \times 10^{4}\ \mathrm{s^{-1}} = 5.83186\times10^{-19}\ \mathrm{W}.$$

Compare with