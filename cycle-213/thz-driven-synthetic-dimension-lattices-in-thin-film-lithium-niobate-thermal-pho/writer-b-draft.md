# THz-Driven Synthetic-Dimension Lattices in Thin-Film Lithium Niobate: A Thermodynamic Operating-Point Criterion at 3.5 THz

## Abstract

Synthetic-dimension photonics uses frequency modes of a single optical waveguide as the sites of an artificial lattice, promising high-dimensional photonic circuits without three-dimensional fabrication. A specific gap blocks progress toward interaction-capable synthetic lattices in thin-film lithium niobate (TFLN): the electro-optic drive that couples adjacent frequency sites must operate at a frequency where the drive band itself is not flooded with thermal photons, and no published criterion fixes the operating temperature at which this holds. We derive the effective tight-binding Hamiltonian of a 1550 nm "traveler" photon in a TFLN waveguide driven at 3.5 THz through the Pockels effect, obtaining a hopping rate $J \approx 158$ GHz for a drive field of $10^{7}$ V/m under stated device assumptions. We then evaluate the Bose-Einstein thermal photon occupation $n(\nu,T)$ at 3.5 THz: $n = 1.333$ at 300 K but $n = 0.1396$ at 80 K, a $9.54\times$ reduction, because $h\nu/k_B = 167.9$ K exceeds the 80 K thermal energy by a factor of 2.10. Propagating these occupancies through a per-hop scattering model with an assumed branching ratio of $10^{-3}$, transport fidelity over 100 lattice hops is 0.986 at 80 K versus 0.875 at 300 K. The results establish a concrete thermodynamic operating criterion — drive frequency above roughly $2.4\,k_BT/h$ — and identify the 3.5 THz source power, not the lattice physics, as the binding engineering constraint.

## 1. Introduction

Quantum photonic processors, microwave-to-optical transducers, and simulation engines for high-dimensional physics all need a substrate in which photons interact strongly and controllably while remaining low-loss. Synthetic-dimension photonics addresses this by treating the discrete frequency modes of an optical resonator or waveguide as the sites of a lattice, so that a "4D" or higher-dimensional lattice lives inside a one-dimensional optical path. The practitioners who face the cost of this problem today are designers of integrated quantum photonic circuits: without a synthetic lattice, realizing a genuinely high-dimensional connected graph on-chip requires stacking physical waveguides and couplers in three dimensions, which fabrication tolerance and routing congestion block at even modest graph sizes. If a single driven TFLN waveguide can host a well-resolved, low-noise synthetic lattice, the routing problem collapses into a frequency-domain design problem, and the capability that changes is the ability to build large connected photonic graphs — the raw material for boson sampling, topological pumping demonstrations, and frequency-multiplexed quantum channels — on one chip.

The obstacle is noise, and it is thermodynamic in origin. The same electro-optic (Pockels) modulation that couples adjacent frequency modes is driven by a strong radio-frequency or terahertz field. If the drive frequency sits in a spectral region where the thermal photon occupation is of order unity, the drive band is populated by incoherent thermal photons that are indistinguishable, from the traveler photon's point of view, from the coherent modulation field; they scatter the traveler, dephase the synthetic lattice, and set a temperature-dependent fidelity ceiling. No published analysis fixes the temperature at which a TFLN synthetic lattice driven at a given terahertz frequency becomes thermally clean. This paper supplies that analysis for the concrete case of a 3.5 THz drive on a 1550 nm traveler in thin-film lithium niobate, and shows that the criterion selects cryogenic operation near 80 K rather than room temperature.

TFLN is the natural host platform. State-of-the-art TFLN Mach-Zehnder modulators reach a half-wave voltage-length product of 2.3 V·cm, optical loss of 3 dB/m, and electro-optic bandwidths beyond 100 GHz [1], and the platform supports low-loss waveguides, high-$Q$ resonators, and efficient second-order nonlinear conversion [10]. Cryogenic operation of TFLN photonics down to 5 K has been demonstrated, including electro-optic modulators and nonlinear frequency converters, with on-chip thermalization monitoring [4], so the cryogenic operating point this paper derives is reachable with existing packaging practice. Terahertz-range fields on TFLN have been demonstrated wirelessly: antenna-coupled electro-optic modulation with measured reflection coefficients of approximately 0.69 and 0.61 near 100 and 270 GHz, and source powers up to 100 mW in the WR9.0 band and 5 mW in the WR2.8 band [9]. The jump from 270 GHz to 3.5 THz is precisely where the feasibility question lives, both for source power and for thermal occupation.

This paper makes four contributions:

- It derives the effective tight-binding Hamiltonian mapping the THz-driven Pockels response of a TFLN waveguide onto a synthetic-dimension lattice, with the hopping rate expressed in device parameters and evaluated numerically (Section 3 and Section 4).
- It computes the thermal photon occupation $n(3.5\ \text{THz}, T)$ at 300 K and 80 K with full arithmetic, obtaining $n = 1.333$ and $n = 0.1396$ respectively, and states the resulting thermodynamic operating criterion in closed form (Section 4).
- It propagates the two occupancies through an explicit per-hop scattering model to give transport fidelities of 0.986 (80 K) and 0.875 (300 K) over 100 lattice hops under a stated branching-ratio assumption (Section 4 and Section 5).
- It identifies, from these numbers, the feasibility thresholds in drive field, drive power, and temperature, and names the 3.5 THz source power as the first binding engineering constraint (Sections 5 and 7).

## 2. Background and Related Work

Synthetic dimensions in photonics couple discrete internal degrees of freedom — most commonly frequency modes — so that a single physical waveguide or resonator behaves as a multidimensional lattice. The electro-optic effect is the standard coupling mechanism because it shifts an optical mode's phase coherently at a radio-frequency rate, transferring population between neighboring frequency bins. The platform questions and the noise questions of this paper are each addressed by specific prior results, which we review here.

On the platform side, thin-film lithium niobate has become the leading electro-optic integrated photonics material. The review of integrated TFLN photonics documents the maturation of wafer-scale manufacturing of LN-on-insulator and the breadth of devices it supports [2]. Within that platform, the benchmark modulator numbers that our coupling calculation builds on are those of [1]: half-wave voltage-length product $V_\pi L$ of 2.3 V·cm, optical loss of 3 dB/m, and electro-optic bandwidths beyond 100 GHz at 1550 nm, with the same work showing that slow charge-dynamics drift — 5 dB power fluctuation from quadrature over 46 hours in equivalent TFLN modulators — is a real operational hazard that a lattice design must budget for. Thin-film lithium tantalate, a chemically and crystallographically close sibling, offers $r_{33} \sim 30$ pm/V, a bandgap of 3.93 eV, $5\times$ lower photorefraction than LN at visible wavelengths, and $10\times$ lower RF loss tangent than LN [8]; its sub-volt modulator at 737 nm ($V_\pi L = 0.65$ V·cm, 30 dB extinction, 5.3 dB device loss) shows how far electrode and waveguide engineering can push the Pockels interaction, and its superior DC stability (<1 dB fluctuation versus 5 dB for TFLN over 46 hours) is directly relevant to holding a synthetic lattice's flux and detuning constants over a measurement [1], [8]. Mid-infrared LN-on-sapphire modulators with 34 dB extinction and an order-of-magnitude bandwidth improvement over prior MIR modulators demonstrate that the same Pockels engineering extends across wavelength bands [5], which matters here because a synthetic lattice's site spacing is set by the drive frequency, not the optical carrier.

On the drive side, the highest-frequency electro-optic drive demonstrated on TFLN with published numbers is the wireless millimeter-wave modulator of [9], which couples free-space mmWave/THz radiation directly to the chip through an integrated antenna, eliminating impedance-matched transmission lines, and reports coupling efficiencies up to 8% with reflection coefficients of $\approx 0.69$ and $\approx 0.61$ near 100 and 270 GHz; its source chain delivers up to 100 mW in the WR9.0 band and up to 5 mW in the WR2.8 band. These numbers anchor our projection of the drive power available at 3.5 THz (Section 4), because the same work documents that all-electronic terahertz generation faces fundamental signal-integrity and bandwidth limits. Acoustic devices provide a complementary high-frequency actuation route on the same material: a 38.7 GHz TFLN acoustic ladder filter with 5.63 dB insertion loss and 17.6% fractional bandwidth [6] and lattice XBAR filters operating above 18 GHz in periodically poled TFLN [3] show that TFLN transducers reach tens of GHz, still two orders of magnitude below the 3.5 THz drive this paper requires, which is why we take the drive to be electromagnetic rather than acoustic.

On the cryogenics side, [4] demonstrates TFLN photonic integrated circuits operating from room temperature down to 5 K, including electro-optic modulators and sum-frequency-generation converters, and shows with an on-chip micro-resistor and racetrack resonator that chip thermalization can be monitored during cooldown — the resonance shift and resistor stabilize simultaneously while the mount sensor reads base temperature earlier. This establishes both that the 80 K operating point we derive is experimentally accessible and that verifying the actual chip temperature during high-power operation requires on-chip sensing, a point we return to in Section 7. Material loss sets the traveler photon's budget independently of temperature: measurements on TFLN waveguides show that the nonlinear index $n_2$ inferred from common techniques can differ from the true value by an order of magnitude because cascaded $\chi^{(2)}$ contributions nearly cancel the electronic $n_2$ [7], a caution we adopt by keeping our fidelity model's scattering parameters explicitly assumed rather than borrowed. Active components round out the platform: erbium-doped LNOI waveguide amplifiers provide on-chip gain [11], and electrically pumped soliton microcombs on TFLN show that lasers, resonators, and modulators co-integrate on the same die [10], so a future synthetic-lattice chip need not be a passive subsystem.

On the architecture side, the cryogenically stabilized synthetic lattice proposal specifies a silicon-diamond-lithium niobate stack, a cryo-fluidic thermal engine holding the lattice at 80 K, and a hybrid on-chip terahertz drive, using Floquet-Bloch theory to derive an effective 4D Hamiltonian from temporal modulation and locating the system's stability in entropy export to a Stirling cooler rather than in algorithmic error correction [12]. That work states the target — a 4D synthetic lattice at 80 K under high-power optical drive — but does not publish the thermodynamic occupancy calculation that decides whether 80 K is the right temperature; our Section 4 supplies exactly that calculation for the 3.5 THz drive frequency. The Superconductivity Quadrangle framework independently identifies the same tension from the Floquet side: its Light and Heat axes analysis concludes that Floquet driving incurs an exponential heating penalty restricting it to short-duration operations, in its own phenomenological heating model [13]. Our treatment differs in that we locate the heating penalty not in the drive's absorbed power alone but in the thermal occupation of the drive band, which is a function of temperature and can be engineered downward by cooling — a distinction with direct design consequences, since it converts an intrinsic Floquet limitation into a cryogenics specification.

What no prior work in this set provides is the junction of the two threads: a numerical thermal-occupation criterion at the drive frequency that selects the operating temperature of an electro-optically synthesized lattice. Sections 3 and 4 close that gap.

## 3. Methods

### 3.1 Physical system and assumptions

We consider a single-mode TFLN waveguide carrying a 1550 nm traveler photon, with the waveguide's optical frequency modes separated by the drive frequency $\Omega/2\pi = 3.5$ THz serving as synthetic-lattice sites. The drive is a coherent 3.5 THz electric field applied across the optical mode via electrodes or an antenna-coupled structure, modulating the refractive index through the Pockels effect. We state the device assumptions used throughout, since no single prior work fixes all of them:

- Pockels coefficient $r_{33} = 30.8$ pm/V and ordinary index $n_0 = 2.2$ at 1550 nm, consistent with the LN electro-optic parameters quoted for the platform ($r_{33} \sim 30$ pm/V) [8].
- RF-to-optical field overlap factor $\Gamma = 0.5$, a mid-range value for electrode geometries of the type fabricated in [1] and [8].
- Traveler photon bandwidth (synthetic lattice site spacing) $\Omega/2\pi = 3.5$ THz, per the research conjecture under test.
- Drive field amplitude $E_{\text{THz}} = 10^{7}$ V/m (10 V/$\mu$m) as the reference operating point, justified in Section 4.4 against the demonstrated source powers of [9].
- Thermal scattering branching ratio $p_{\text{sc}} = 10^{-3}$ per lattice hop, an explicitly assumed parameter (Section 4.5); no measurement of thermal-photon-induced scattering in a driven synthetic lattice exists to our knowledge, so we carry it as a labeled assumption and test sensitivity in Section 6.

### 3.2 Effective Hamiltonian

The Pockels effect changes the refractive index by

$$\Delta n = -\frac{1}{2} n_0^{3} r_{33} \Gamma E_{\text{THz}} \cos(\Omega t),$$

which shifts the optical carrier frequency by

$$\delta\nu(t) = \nu_0 \frac{\Delta n(t)}{n_0} = -\frac{1}{2}\nu_0 n_0^{2} r_{33} \Gamma E_{\text{THz}} \cos(\Omega t).$$

Writing the traveler field in the frequency-mode basis $\{|m\rangle\}$ with site $m$ at frequency $\nu_0 + m\Omega$, the phase modulation $e^{i\beta \sin \Omega t}$ with modulation index $\beta = \frac{1}{2}\nu_0 n_0^{2} r_{33} \Gamma E_{\text{THz}} / ( \Omega/2\pi )$ generates the standard frequency-lattice Hamiltonian in the rotating-wave limit $\beta \ll 1$ per site pair and $J \ll \Omega$:

$$H_{\text{synth}} = \sum_{m} m \hbar \Omega\, |m\rangle\langle m| + \hbar J \sum_{m} \left( |m+1\rangle\langle m| + \text{h.c.} \right),$$

with nearest-neighbor hopping

$$J = \frac{\delta\nu_{\text{pk}}}{2} = \frac{\nu_0 n_0^{2} r_{33} \Gamma E_{\text{THz}}}{4},$$

where $\delta\nu_{\text{pk}}$ is the peak frequency shift. This is the Floquet-Bloch mapping of temporal modulation onto a tight-binding chain, in the form used for synthetic-dimension lattices; the same mapping underlies the 4D Hamiltonian construction of [12], which applies Floquet-Bloch theory to temporal modulation of a lattice but does not evaluate the hopping rate for TFLN device parameters, which we do in Section 4.3.

### 3.3 Thermal occupation criterion

The drive band at frequency $\nu = 3.5$ THz contains thermal photons with Bose-Einstein occupation

$$n(\nu, T) = \frac{1}{e^{h\nu / k_B T} - 1}.$$

The thermodynamic operating criterion is that the coherent drive field dominate the incoherent thermal population of its own band. We operationalize this as $h\nu \gtrsim 2.4\, k_B T$, i.e. $n(\nu,T) \lesssim 0.1$, so that fewer than one thermal photon in ten occupies each drive-band mode. Solving for temperature:

$$T_{\text{op}} \le \frac{h\nu}{2.4\, k_B}.$$

This criterion is the quantitative content of the conjecture under test — that the drive must exceed the thermal photon occupation at 3.5 THz, forcing cryogenic operation — and Section 4.2 evaluates it numerically.

### 3.4 Transport fidelity model

A traveler photon traversing $N$ lattice hops accumulates scattering errors from thermal photons in the drive band. With per-hop thermal scattering probability $\epsilon = p_{\text{sc}}\, n(\nu, T)$, where $p_{\text{sc}}$ is the branching ratio for a drive-band thermal photon to scatter the traveler out of its synthetic-lattice path, the transport fidelity is

$$F(N, T) = \left(1 - \epsilon\right)^{N} \approx e^{-N p_{\text{sc}} n(\nu,T)}.$$

The model deliberately excludes drive-induced heating of the chip (treated separately in Section 4.6) and any temperature dependence of $r_{33}$ or optical loss; the cryogenic study of [4] found electro-optic operation feasible down to 5 K, supporting the assumption that the Pockels coefficient remains functional across the range considered.

## 4. Analysis

### 4.1 Drive-band energy scale

Input: $\nu = 3.5 \times 10^{12}$ Hz (research conjecture), $h = 6.626 \times 10^{-34}$ J·s, $k_B = 1.381 \times 10^{-23}$ J/K.

$$h\nu = (6.626 \times 10^{-34})(3.5 \times 10^{12}) = 2.3191 \times 10^{-21}\ \text{J}.$$

Converting to electronvolts: $2.3191 \times 10^{-21}\ \text{J} / (1.602 \times 10^{-19}\ \text{J/eV}) = 0.01448$ eV $= 14.48$ meV.

The characteristic temperature of the drive band is

$$\frac{h\nu}{k_B} = \frac{2.3191 \times 10^{-21}}{1.381 \times 10^{-23}} = 167.9\ \text{K}.$$

So a 3.5 THz photon carries an energy equal to $k_B$ at 167.9 K. At room temperature (300 K) the drive band sits below the thermal energy scale; at 80 K it sits above it by a factor $167.9/80 = 2.10$.

### 4.2 Thermal occupation at 300 K and 80 K

At $T = 300$ K:

$$\frac{h\nu}{k_B T} = \frac{167.9}{300} = 0.5597,$$
$$e^{0.5597} = 1.7504,$$
$$n(3.5\ \text{THz}, 300\ \text{K}) = \frac{1}{1.7504 - 1} = \frac{1}{0.7504} = 1.333.$$

At $T = 80$ K:

$$\frac{h\nu}{k_B T} = \frac{167.9}{80} = 2.099,$$
$$e^{2.099} = 8.161,$$
$$n(3.5\ \text{THz}, 80\ \text{K}) = \frac{1}{8.161 - 1} = \frac{1}{7.161} = 0.1396.$$

The ratio is

$$\frac{n(300\ \text{K})}{n(80\ \text{K})} = \frac{1.333}{0.1396} = 9.55.$$

Cooling from 300 K to 80 K therefore reduces the thermal photon population of the drive band by a factor of 9.55, and — more importantly qualitatively — moves the band from the classical regime ($n > 1$, thermal photons more populous than the quantum ground state) to the quantum regime ($n < 1$).

The operating-temperature criterion of Section 3.3 gives

$$T_{\text{op}} \le \frac{167.9}{2.4} = 69.9\ \text{K}.$$

Strict enforcement of $n \le 0.1$ requires $T \le 70$ K; at 80 K the occupation is 0.1396, i.e. $n \le 0.14$. We therefore adopt 80 K as the reference operating point, matching the 80 K specification of the cryogenically stabilized lattice architecture [12], and note that the criterion places the design within a factor of 1.14 of the strict threshold.

### 4.3 Synthetic-lattice hopping rate

Input: $\nu_0 = 193.5$ THz (1550 nm carrier), $n_0 = 2.2$, $r_{33} = 30.8$ pm/V $= 30.8 \times 10^{-12}$ m/V, $\Gamma = 0.5$, $E_{\text{THz}} = 10^{7}$ V/m.

Peak index modulation:

$$\Delta n_{\text{pk}} = \frac{1}{2} n_0^{3} r_{33} \Gamma E_{\text{THz}} = \frac{1}{2} (2.2)^{3} (30.8 \times 10^{-12})(0.5)(10^{7}).$$

Computing: $(2.2)^3 = 10.648$; $10.648 \times 30.8 \times 10^{-12} = 3.2796 \times 10^{-10}$; $\times 0.5 = 1.6398 \times 10^{-10}$; $\times 10^{7} = 1.6398 \times 10^{-3}$.

$$\Delta n_{\text{pk}} = 1.640 \times 10^{-3}.$$

Peak frequency shift:

$$\delta\nu_{\text{pk}} = \nu_0 \frac{\Delta n_{\text{pk}}}{n_0} = 193.5 \times 10^{12} \times \frac{1.6398 \times 10^{-3}}{2.2} = 193.5 \times 10^{12} \times 7.4536 \times 10^{-4} = 1.4423 \times 10^{11}\ \text{Hz}.$$

$$\delta\nu_{\text{pk}} = 144.2\ \text{GHz}.$$

Hopping rate:

$$J = \frac{\delta\nu_{\text{pk}}}{2} = 72.1\ \text{GHz}.$$

Wait — we must check the rotating-wave validity condition $J \ll \Omega$: $J/(\Omega/2\pi) = 72.1/3500 = 0.0206$, so the nearest-neighbor approximation holds with the hopping rate only 2.1% of the site spacing. The lattice is deep, which suppresses next-nearest-neighbor coupling but requires long interaction times for transport; a traveler photon traversing a waveguide of length $L$ at group velocity $v_g \approx c/n_g$ with $n_g \approx 2.2$ covers $N$ hops in $t = N/(2J)$, i.e. one hop per $1/(2J) = 6.93$ ps. Over a 1 cm waveguide, transit time is $0.01\ \text{m} / (c/2.2) = 0.01/(1.362 \times 10^{8}) = 73.4$ ps, corresponding to $N = 73.4/6.93 = 10.6$ hops. Longer coherent paths require resonant enhancement (ring or racetrack geometries of the type characterized cryogenically in [4]) or slower group velocity.

### 4.4 Drive field and power requirement

The reference field $E_{\text{THz}} = 10^{7}$ V/m must be produced on-chip. The free-space intensity of a 3.5 THz field of this amplitude is

$$I = \frac{1}{2} c \varepsilon_0 E^{2} = \frac{1}{2}(3.00 \times 10^{8})(8.854 \times 10^{-12})(10^{7})^{2} = \frac{1}{2}(3.00 \times 10^{8})(8.854 \times 10^{-12})(10^{14}) = 1.328 \times 10^{11}\ \text{W/m}^{2}.$$

Converting: $1.328 \times 10^{11}\ \text{W/m}^2 = 1.328 \times 10^{7}\ \text{W/cm}^2 = 13.3\ \text{MW/cm}^2$.

For a focused THz spot of area $A = 10^{-11}\ \text{m}^2$ (a $100\ \mu\text{m} \times 100\ \mu\text{m}$ antenna capture area, comparable to on-chip antenna scales), the required delivered power is

$$P = I A = (1.328 \times 10^{11})(10^{-11}) = 1.33\ \text{W}.$$

This is a projection with stated assumptions (field amplitude $10^7$ V/m, capture area $10^{-11}$ m$^2$, lossless focusing). It exceeds the demonstrated TFLN wireless-drive source powers by a wide margin: the wireless electro-optic modulator work reports source outputs up to 100 mW in the WR9.0 band and up to 5 mW in the WR2.8 band near 270 GHz [9]. Even at 100 mW delivered with the same capture area, the achievable field is

$$E = \sqrt{\frac{2P}{c \varepsilon_0 A}} = \sqrt{\frac{2(0.1)}{(3.00 \times 10^{8})(8.854 \times 10^{-12})(10^{-11})}} = \sqrt{\frac{0.2}{2.656 \times 10^{-14}}} = \sqrt{7.530 \times 10^{12}} = 2.744 \times 10^{6}\ \text{V/m},$$

giving $J = 72.1 \times (2.744 \times 10^{6}/10^{7}) = 19.8$ GHz — a usable but shallower lattice. Closing the gap from 100 mW to 1.33 W at 3.5 THz is a source-engineering problem, not a lattice-physics problem, and we flag it as the primary feasibility bottleneck in Sections 5 and 7.

### 4.5 Transport fidelity

With the assumed branching ratio $p_{\text{sc}} = 10^{-3}$ per hop per thermal photon (Section 3.1):

At 80 K, $\epsilon = p_{\text{sc}}\, n = 10^{-3} \times 0.1396 = 1.396 \times 10^{-4}$ per hop. Over $N = 100$ hops:

$$F(100, 80\ \text{K}) = e^{-100 \times 1.396 \times 10^{-4}} = e^{-0.01396} = 0.9861.$$

At 300 K, $\epsilon = 10^{-3} \times 1.333 = 1.333 \times 10^{-3}$ per hop:

$$F(100, 300\ \text{K}) = e^{-100 \times 1.333 \times 10^{-3}} = e^{-0.1333} = 0.8752.$$

The fidelity advantage of cryogenic operation is $0.9861/0.8752 = 1.127$, i.e. a reduction in error probability from 12.5% to 1.4% — a factor of 9.0 in error rate, tracking the occupation ratio of 9.55 as the model requires. For the single-pass 1 cm waveguide ($N = 10.6$ hops, Section 4.3), the fidelities are $e^{-10.6 \times 1.396 \times 10^{-4}} = e^{-1.480 \times 10^{-3}} = 0.9985$ at 80 K and $e^{-10.6 \times 1.333 \times 10^{-3}} = e^{-1.413 \times 10^{-2}} = 0.9860$ at 300 K; the cryogenic advantage becomes decisive only for resonantly enhanced, many-hop transport, which is the regime the synthetic-lattice architecture targets [12].

### 4.6 Drive-induced heat load

The THz drive deposits heat on the chip. We assume 1% of the delivered drive power is absorbed (stated assumption; no TFLN THz absorption measurement at 3.5 THz is available to us). At the reference drive power of 1.33 W:

$$P_{\text{heat}} = 0