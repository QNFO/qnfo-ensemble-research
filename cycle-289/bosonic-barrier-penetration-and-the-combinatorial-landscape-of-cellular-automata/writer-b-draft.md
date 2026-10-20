# Bosonic Barrier Penetration and Ultraviolet Cellular Communication: A Quantitative Test of a Bosonic-Transport Conjecture

## Abstract

Intercellular signaling at ultraviolet frequencies has been proposed as a physical channel between cells, with the conjecture that photons penetrate biological barriers precisely because bosons are exempt from the Pauli exclusion principle that renders fermionic matter impenetrable. The specific gap addressed here is quantitative: no published derivation compares the transmission of an ultraviolet photon through a cellular membrane and cytoplasm with the transmission of a fermionic particle through the same barriers, so the conjectured bosonic advantage has never been given a number. This paper models photon propagation with the Beer–Lambert attenuation law and fermionic transport with the Wentzel–Kramers–Brillouin tunneling formula, using explicitly stated assumptions for absorption coefficient, barrier height, and geometry. The principal results are: a single 5 nm lipid membrane transmits 280 nm photons with probability $T_m = 0.995$, a 10 μm cytoplasmic crossing transmits with probability $T_c = 4.54 \times 10^{-5}$, a proton tunneling through the same membrane has probability $\approx 10^{-953}$, and the resulting bosonic–fermionic transmission ratio is approximately $10^{953}$ at the membrane barrier. However, the analysis shows the advantage originates in the photon's vanishing rest mass and absence of a Coulomb barrier, not in Bose statistics, and cytoplasmic absorption limits any signaling channel to roughly one detectable photon per 22 s at an assumed emission rate of $10^3$ photons/s. The conjecture is therefore supported only in a restricted, short-range form.

## 1. Introduction

Researchers attempting to establish whether cells communicate through endogenous ultraviolet photons face a decision problem with no quantitative answer available. If ultraviolet light crosses cellular boundaries efficiently, then optical signaling between cells is physically plausible and instruments should be built to look for it; if cytoplasmic absorption suppresses transmission by many orders of magnitude, then the search should be redirected to sub-cellular distances or to cooperative effects that modify absorption. Today neither branch can be chosen, because the conjecture that motivates the search — that bosons penetrate matter where fermions cannot, an idea articulated in the quantum-biophysics literature [9], [10] — has never been converted into a transmission probability that can be compared against an experiment. The cost of this gap is concrete: experimental programs are proposed without a photon budget, and negative results cannot be interpreted because no threshold prediction exists to fail against.

The conjecture under test has a specific logical structure. Photons are bosons and are exempt from the Pauli exclusion principle; ordinary matter is fermionic, and the argument runs that the exclusion principle is what makes matter "impenetrable," so bosons should cross matter freely [9], [10]. This paper tests that argument by computing both sides of the comparison. On the bosonic side, photon transmission through a lipid membrane and through cytoplasm is computed from the Beer–Lambert law with an assumed absorption coefficient. On the fermionic side, the probability that a proton tunnels through the same membrane is computed from the Wentzel–Kramers–Brillouin (WKB) formula. The ratio of the two transmissions is the quantitative content of the "bosonic advantage."

The physics literature on wave penetration into lossy media offers an instructive engineering analogue at another frequency: millimeter-wave cellular systems suffer penetration loss so severe that a human body blocking the line-of-sight path terminates high-rate transmission, and blockage models must be built to predict it [5]. The same modeling discipline — a transmission probability per barrier, a path budget, and a detectability threshold — is applied here at optical frequencies inside tissue.

The paper also confronts an epistemic hazard specific to this topic. Cognitive systems detect patterns where none exist, and indiscriminate pattern application underlies superstition and conspiracy theorizing [11]; a conjecture connecting quantum statistics to cell biology must therefore be held to an explicit falsifiable numerical standard, which Sections 4–6 supply.

The contributions are:

- A derivation of ultraviolet photon transmission through a single 5 nm lipid membrane, $T_m = 0.995$, and through a 10 μm cytoplasmic layer, $T_c = 4.54 \times 10^{-5}$, from the Beer–Lambert law with stated absorption assumptions (Section 4.1–4.2).
- A WKB derivation of fermionic tunneling through the same membrane, $T_p \approx 10^{-953}$, and the resulting bosonic–fermionic ratio of approximately $10^{953}$ orders of magnitude, with the finding that the ratio is driven by mass and charge, not by exchange symmetry (Section 4.3–4.4).
- A photon-budget calculation showing that at an assumed emission rate of $10^3$ photons/s and a detection efficiency of 0.1, a 10 μm cytoplasmic channel delivers one detected photon per 220 s, which constrains any ultraviolet signaling scheme to short ranges or to mechanisms that defeat bulk absorption (Section 4.5).
- A falsification criterion: measurement of 280 nm transmission through a 10 μm protein-rich layer that substantially exceeds $e^{-10}$ would refute the absorption assumption, while failure to detect crossing photons at the computed rates would falsify the signaling conjecture in its long-range form (Sections 5 and 6).

## 2. Background and Related Work

The conjecture under test originates in a body of quantum-biophysics writing that proposes endogenous ultraviolet light as a functional signal in neural tissue. That literature describes a "tryptophan mega-network" whose optical dynamics are proposed as a substrate for brain-scale synchronization operating far faster than chemical signaling allows, and it explicitly frames the brain as containing a biological laser whose flashes would need dedicated instrumentation to observe [9]. The same body of work states the specific mechanistic link relevant here: the theoretical connection between ultraviolet photon emission and the modulation of voltage-gated ion channels is identified as a claim that must be empirically verified through targeted biophysical experiments, alongside proposed in vivo detection of microtubule superradiance [10]. That source also reports, as attributed prior work, that modified magnetic-resonance imaging sequences designed to isolate zero-quantum coherence detected signal bursts correlated with heartbeat-evoked potentials and conscious awareness, which disappeared when subjects fell asleep [10]. These are the observational anchors to which any transmission calculation must ultimately connect; none of them, however, supplies a penetration probability, which is the quantity derived in Section 4.

The engineering literature on high-frequency wireless transmission supplies the methodological template. A three-dimensional human-body blockage model for outdoor millimeter-wave cellular communication demonstrates the discipline of treating a body as an attenuating obstacle with computable consequences: that work notes that millimeter-wave systems suffer significantly higher path loss and penetration loss than lower-frequency systems, that line-of-sight channels blocked by a user or pedestrian fail entirely, and that only short-distance line-of-sight links deliver satisfactory signal-to-noise ratio [5]. Its case studies quantify the impacts of pedestrian density, frame length, and access-point height on line-of-sight availability, with numerical computations under different configurations [5]. The present paper imports exactly this structure — obstacle, per-barrier transmission, link budget — into the cellular interior, with the lipid membrane and the cytoplasm playing the roles of blocker and path.

Modeling photon transport through a cellular lattice of absorbing and scattering obstacles is naturally cast as a stochastic cellular automaton, and the cellular-automata literature supplies the needed formal machinery. Stochastic cellular automata are used precisely where the phenomenon under study is stochastic or its exact rules are imperfectly known, including in chemistry, biology, and medicine; two analysis tools are established for them: a stochastic-mixture representation that yields cell-wise probability distributions showing the average state of each cell during evolution, and a continuous cellular-automaton polynomial representation that uncovers average behavior quickly [7]. The same source defines the underlying discrete framework — cells assigned states from a finite set by local rules depending on neighbors, with configurations evolving on a lattice with periodic boundaries [7]. For the transport model of Section 3, the cell-wise probability distribution tool of [7] is the direct analogue of a photon fluence map: the probability that a lattice cell contains a photon is exactly what the Beer–Lambert law computes in closed form for the one-dimensional case.

The lattice structure of the transport model raises the question of neighborhood geometry. Probabilistic cellular automata with a modified Margolus neighborhood — 2×2 blocks shifted one cell between iterations — have been used to simulate granular flow in an hourglass, with transition probabilities acting as an adjustable friction-like interaction that produces elongated piles and longer settling times as toppling probability decreases [8]. That work reports per-iteration computation of a few milliseconds on a 61×61 grid and argues the approach balances fast computation against realistic flow even at high resolution [8]. The Margolus scheme is a candidate lattice update rule for a two-dimensional photon-transport simulation because it is computationally cheap and its probabilistic transitions can encode absorption; the one-dimensional analysis of Section 4 is the closed-form limit of such a scheme.

Update timing is a further modeling choice. A survey of asynchronous cellular automata distinguishes fully asynchronous updating, in which one cell per step is chosen uniformly at random, from $\alpha$-asynchronous updating, in which each cell applies its rule with probability $\alpha$ and holds state with probability $1-\alpha$, and notes that asynchrony may break the complexity of a rule and render it simpler to study [6]. Photon absorption events in tissue are asynchronous in exactly this sense — each lattice site absorbs independently — so the $\alpha$-asynchronous scheme of [6] is the natural update discipline, with $\alpha$ playing the role of the per-site survival probability.

Directional symmetry of the transport rule matters because photon propagation in homogeneous media is isotropic. The iso-rule paradigm was introduced on the argument that cellular-automata models of self-organisation should respect the isotropy underlying physics, providing a lookup-table over isotropic neighborhood groups in one, two, and three dimensions, with rule-table sizes ordered as $S_r > S_i > S_k > S_t$ between full rules, iso-rules, and totalistic families [3]. An isotropic transport rule avoids injecting artificial directional bias into a fluence map; the iso-rule formalism of [3] is the systematic way to enforce this. Relatedly, the X-rule search demonstrates the discovery method for structured dynamics in rule space: an exhaustive search over an entropy-classified scatter-plot of more than 93,000 rules shortlisted about 70 rules with gliders and stable structures, from which rules propagating both orthogonally and diagonally were selected [2]. That search strategy — classify the rule space, then search the ordered sector for propagating structures — is the analogue of scanning absorption-parameter space for regimes where propagating photon modes survive, and the X-rule's glider-guns show that sustained signal generation can emerge from local rules, a structural analogy for repetitive cellular emission [2].

Finally, two cautionary results from the cellular-automata literature bound what such models can prove. Classifications of elementary cellular automata are subject to undecidability: Culik II and Yu proved in 1988 that such classifications are undecidable, even as novel classification techniques continue to appear, and memory-composed rules can shift a chaotic rule into complex behavior [1]. And the first-order theory of the phase space of one-dimensional cellular automata is decidable — Sutner proved model-checking decidable in first-order logic with equality, using $\zeta$-Büchi automata reading bi-infinite words, with subsequent work showing cellular-automaton graphs are $\omega$-automatic [4]. The practical import for this paper is that global claims about a transport automaton (for example, "photons percolate across the tissue") are the kind of property whose algorithmic decidability is delicate [1], [4], which is why Section 4 reduces the problem to a closed-form one-dimensional calculation rather than resting conclusions on simulated automaton behavior.

Information-theoretic bounds supply a ceiling on what any successful channel could carry. The Bekenstein bound defines the maximum amount of information contained in a finite region of space [12], and it is applied in Section 4.6 as an upper envelope on the information a detected-photon channel could convey. The broader epistemic framework in which this paper operates — that representational models differ from their territory and that confusing the two produces categorical errors [11] — motivates the strict separation, maintained throughout, between the computed transmission numbers and the conjectured biological interpretation of them.

## 3. Methods

### 3.1 Scope and approach

The paper's method is analytical derivation from two standard transport formulas, with all biological parameters stated as explicit assumptions because no source in the literature consulted supplies measured optical constants for the intracellular environment at 280 nm. No experiment, simulation on hardware, or measurement was performed; every number in Sections 4 and 5 is either computed here from stated inputs or labeled a projection.

### 3.2 Bosonic (photon) transport model

Photon propagation through a homogeneous absorbing layer of thickness $d$ follows the Beer–Lambert law,

$$T(d) = \frac{I(d)}{I_0} = e^{-\mu d},$$

where $I_0$ is the incident intensity, $I(d)$ the transmitted intensity, and $\mu$ the absorption coefficient. This law is the continuum limit of the stochastic cellular-automaton transport picture of Section 2: on a one-dimensional lattice of cells with absorption probability per cell $p_{\mathrm{abs}}$, the $\alpha$-asynchronous update discipline of [6] with $\alpha = 1 - p_{\mathrm{abs}}$ yields a cell-wise survival probability whose product across $n$ cells is $e^{-\mu d}$ in the continuum limit, matching the cell-wise probability-distribution formalism of [7]. The model treats the membrane and the cytoplasm as two absorbing layers in series, so the total transmission is the product

$$T_{\mathrm{tot}} = T_m \, T_c = e^{-\mu_m d_m} e^{-\mu_c d_c}.$$

Isotropy of the underlying propagation is assumed, consistent with the requirement that transport models of natural systems carry no directional bias [3]; in one dimension this assumption is automatically satisfied.

### 3.3 Fermionic transport model

For a fermionic particle of mass $m_p$ and energy $E$ incident on a rectangular barrier of height $V > E$ and width $d_m$, the WKB transmission probability is

$$T_f = e^{-2 \kappa d_m}, \qquad \kappa = \frac{\sqrt{2 m_p (V - E)}}{\hbar}.$$

The proton is chosen as the fermionic probe because it is the dominant fermionic constituent attempting to cross membranes in any transport sense (ions), and because its mass makes the tunneling suppression representative of matter transport generally.

### 3.4 Photon budget model

A source cell emitting photons at rate $R$ produces a detected crossing rate

$$r_{\mathrm{det}} = R \, T_{\mathrm{tot}} \, \eta,$$

where $\eta$ is the detection (absorption-triggering) efficiency at the receiving cell. The mean inter-detection interval is $\tau = 1 / r_{\mathrm{det}}$. The minimum emission count for at least one crossing photon is $N_{\min} = 1 / T_{\mathrm{tot}}$.

### 3.5 Assumption register

All inputs not supplied by the cited literature are stated here as assumptions:

- $A_1$: wavelength $\lambda = 280\ \mathrm{nm}$ (the tryptophan absorption band implied by the tryptophan-network proposal of [9]).
- $A_2$: cytoplasmic absorption coefficient $\mu_c = 10^4\ \mathrm{cm}^{-1}$ at $\lambda = 280\ \mathrm{nm}$, representative of dense proteinaceous media; sensitivity to $10^3$–$10^5\ \mathrm{cm}^{-1}$ is computed in Section 4.6.
- $A_3$: membrane absorption coefficient $\mu_m = 10^4\ \mathrm{cm}^{-1}$ at 280 nm (lipid membranes are largely transparent at this wavelength relative to protein; the same value is used conservatively for both layers).
- $A_4$: membrane thickness $d_m = 5\ \mathrm{nm} = 5 \times 10^{-7}\ \mathrm{cm}$.
- $A_5$: cytoplasmic crossing distance $d_c = 10\ \mathrm{\mu m} = 10^{-3}\ \mathrm{cm}$ (a typical cell diameter).
- $A_6$: proton barrier parameters $\Delta E = V - E = 1\ \mathrm{eV} = 1.602 \times 10^{-19}\ \mathrm{J}$, $m_p = 1.6726 \times 10^{-27}\ \mathrm{kg}$, $\hbar = 1.0546 \times 10^{-34}\ \mathrm{J \cdot s}$.
- $A_7$: emission rate $R = 10^3\ \mathrm{photons/s}$ per source cell.
- $A_8$: detection efficiency $\eta = 0.1$.

## 4. Analysis

### 4.1 Single-membrane photon transmission

From $A_2$, $A_3$, $A_4$:

$$\mu_m d_m = (10^4\ \mathrm{cm}^{-1})(5 \times 10^{-7}\ \mathrm{cm}) = 5 \times 10^{-3}.$$

$$T_m = e^{-5 \times 10^{-3}} = 0.99501.$$

Arithmetic: $e^{-0.005} = 1 - 0.005 + 0.005^2/2 - \cdots = 1 - 0.005 + 0.0000125 = 0.99501$ (higher terms below $10^{-7}$). A single lipid membrane therefore transmits 280 nm photons with probability $T_m = 0.995$, i.e. 99.5 %.

### 4.2 Cytoplasmic crossing

From $A_2$, $A_5$:

$$\mu_c d_c = (10^4\ \mathrm{cm}^{-1})(10^{-3}\ \mathrm{cm}) = 10.$$

$$T_c = e^{-10} = 4.539993 \times 10^{-5}.$$

Arithmetic: $e^{-10} = e^{-1 \times 10}$; $e^{-1} = 0.367879$, so $e^{-10} = (0.367879)^{10}$. Computing directly: $e^{10} = 22026.47$, hence $e^{-10} = 1/22026.47 = 4.539993 \times 10^{-5}$.

Total cell-to-cell transmission through one membrane exit and the cytoplasm:

$$T_{\mathrm{tot}} = T_m \times T_c = 0.99501 \times 4.539993 \times 10^{-5} = 4.5173 \times 10^{-5}.$$

Arithmetic: $4.539993 \times 0.99501 = 4.539993 - 4.539993 \times 0.00499 = 4.539993 - 0.022654 = 4.517339 \times 10^{-5}$.

### 4.3 Fermionic (proton) tunneling through the same membrane

From $A_6$, $A_4$ (with $d_m = 5 \times 10^{-9}\ \mathrm{m}$ in SI units):

Step 1 — the exponent argument:

$$2 m_p \Delta E = 2 \times (1.6726 \times 10^{-27}\ \mathrm{kg}) \times (1.602 \times 10^{-19}\ \mathrm{J}) = 5.3591 \times 10^{-46}\ \mathrm{kg^2\,m^2\,s^{-2}}.$$

Arithmetic: $2 \times 1.6726 = 3.3452$; $3.3452 \times 1.602 = 5.3591$; exponents $10^{-27} \times 10^{-19} = 10^{-46}$.

Step 2 — the decay constant:

$$\sqrt{5.3591 \times 10^{-46}} = 2.3150 \times 10^{-23}\ \mathrm{kg\,m\,s^{-1}}.$$

Arithmetic: $\sqrt{5.3591} = 2.3150$ (since $2.3150^2 = 5.3592$); $\sqrt{10^{-46}} = 10^{-23}$.

$$\kappa = \frac{2.3150 \times 10^{-23}}{1.0546 \times 10^{-34}} = 2.1951 \times 10^{11}\ \mathrm{m}^{-1}.$$

Arithmetic: $2.3150 / 1.0546 = 2.1951$; $10^{-23} / 10^{-34} = 10^{11}$.

Step 3 — the transmission exponent:

$$2 \kappa d_m = 2 \times (2.1951 \times 10^{11}\ \mathrm{m}^{-1}) \times (5 \times 10^{-9}\ \mathrm{m}) = 2.1951 \times 10^{3}.$$

Step 4 — the transmission probability:

$$T_f = e^{-2195.1}.$$

In base 10:

$$\log_{10} T_f = \frac{-2195.1}{\ln 10} = \frac{-2195.1}{2.302585} = -953.3.$$

Arithmetic: $2.302585 \times 953 = 2194.36$; remainder $2195.1 - 2194.36 = 0.74$; $0.74 / 2.302585 = 0.32$; total $953.32$. Hence

$$T_f \approx 10^{-953}.$$

### 4.4 The bosonic–fermionic ratio

The ratio of photon transmission to proton transmission through the same 5 nm membrane:

$$\frac{T_m}{T_f} = \frac{0.99501}{10^{-953.3}} \approx 10^{953.3}.$$

Arithmetic: $\log_{10}(T_m / T_f) = \log_{10} 0.99501 + 953.3 = -0.00217 + 953.3 = 953.3$. The photon crosses the membrane roughly $10^{953}$ times more probably than the proton.

Decomposition of the ratio: the WKB exponent $2\kappa d_m$ contains $\sqrt{m_p}$ and the barrier height $\Delta E$; neither term involves exchange symmetry. Setting $m_p \to 0$ (massless probe) sends $\kappa \to 0$ and $T_f \to 1$ regardless of statistics. The $10^{953}$ advantage is therefore attributable to the photon's zero rest mass and its lack of a Coulomb barrier, not to Bose statistics; two co-propagating photons would not exclude one another, but the single-photon transmission probability is unchanged by that fact. This is the central interpretive finding against the conjecture's stated mechanism.

### 4.5 Photon budget for signaling

Minimum photons for one crossing (from $T_{\mathrm{tot}}$ of Section 4.2):

$$N_{\min} = \frac{1}{T_{\mathrm{tot}}} = \frac{1}{4.5173 \times 10^{-5}} = 2.2137 \times 10^{4}\ \mathrm{photons}.$$

Arithmetic: $1 / 4.5173 = 0.22137$; $10^{5} \times 0.22137 = 2.2137 \times 10^4$.

With detection efficiency $\eta = 0.1$ ($A_8$), the minimum for one detected crossing is

$$N_{\min}^{(\eta)} = \frac{N_{\min}}{\eta} = 2.2137 \times 10^{5}\ \mathrm{photons}.$$

Detected-crossing rate at the assumed emission rate $R = 10^3\ \mathrm{s^{-1}}$ ($A_7$):

$$r_{\mathrm{det}} = R \, T_{\mathrm{tot}} \, \eta = 10^3 \times 4.5173 \times 10^{-5} \times 0.1 = 4.5173 \times 10^{-3}\ \mathrm{s^{-1}}.$$

Mean inter-detection interval:

$$\tau = \frac{1}{r_{\mathrm{det}}} = \frac{1}{4.5173 \times 10^{-3}} = 221.4\ \mathrm{s}.$$

Arithmetic: $1/4.5173 = 0.22137$; $0.22137 \times 10^3 = 221.37\ \mathrm{s}$.

A 10 μm cytoplasmic channel at these assumptions delivers one detected photon roughly every 221 s — far slower than any known intercellular signaling timescale, which operates on the scale of milliseconds to seconds.

### 4.6 Sensitivity analysis

Varying $\mu_c$ over $10^3$–$10^5\ \mathrm{cm}^{-1}$ at fixed $d_c = 10^{-3}\ \mathrm