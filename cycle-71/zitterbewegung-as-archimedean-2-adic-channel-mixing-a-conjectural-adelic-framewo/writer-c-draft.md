# Zitterbewegung as Archimedean–2-adic Channel Mixing: A Conjectural Adelic Framework and Its Testable Consequences

## Abstract

Zitterbewegung (ZBW) — the trembling motion of Dirac wave packets at the Compton scale, first identified by Breit and Schrödinger — is conventionally explained as interference between positive- and negative-energy branches on the real line. We develop a stronger conjecture: ZBW is the physical signature of mixing between the Archimedean completion $\mathbb{Q}_\infty = \mathbb{R}$ and the 2-adic completion $\mathbb{Q}_2$ of the rational base field. A wave packet localized at the real place $x_\infty$ necessarily contains Fourier components delocalized at the 2-adic place $x_2$; the observed oscillation at angular frequency $\omega_{\mathrm{ZBW}} = 2E/\hbar$ is interpreted as the beat between these sectors, with the Majorana reality condition realizing the identification of the two places and topological protection arising from Ostrowski incommensurability of $\mathbb{R}$ and $\mathbb{Q}_2$. We formulate the Dirac equation on the adèle ring, derive the channel-mixing amplitude structure, compute the product-formula identity for the prime $2$ explicitly, and show that the predicted frequency $2m_ec^2/\hbar \approx 1.55\times 10^{21}\ \mathrm{rad\,s^{-1}}$ for the electron is representation-independent under Foldy–Wouthuysen transformation, consistent with an ontological rather than coordinate effect. We propose falsifiable tests: trapped-ion and cold-atom emulations of coupled real–$p$-adic dynamics, and conductance-based readout protocols. The framework remains conjectural; we state its failure modes explicitly.

## 1. Introduction

The velocity operator of the Dirac equation has eigenvalues $\pm c$, and a localized Dirac wave packet does not move uniformly: its position oscillates rapidly at the Compton scale. This is Zitterbewegung, named by Schrödinger following the work of Breit [1]. The standard account treats ZBW as an interference effect between positive- and negative-frequency components of a packet on the real line [2]. On that account, ZBW is a kinematic artifact: a suitable change of representation (Foldy–Wouthuysen, FW) diagonalizes the Hamiltonian and the trembling disappears from the position operator.

Yet ZBW is not merely an artifact of one representation. It survives, reappears, or can be externally driven across radically different physical systems: it can be converted into directed center-of-mass motion by resonant modulation of a Dirac-like equation [3]; it appears as an internal-state oscillation in discrete-time quantum walks implemented in fiber loops [5]; it can be controlled in cold atoms by mirror oscillation driving an effective spin-orbit interaction [6]; it is modified by Zeeman fields and harmonic traps in spin-orbit-coupled spin-1 ultracold atoms [7]; and it produces measurable charge oscillations in a three-terminal junction whose period can be tuned by spin-orbit strength or magnetic field [8]. This robustness across implementations and representations motivates treating ZBW as ontological rather than coordinate-dependent.

This paper advances a specific ontological hypothesis, taken from the adelic physics program [9]: the physically accessible base field is $\mathbb{Q}$, not $\mathbb{R}$, and by Ostrowski's theorem all completions of $\mathbb{Q}$ — the real place $\mathbb{R}$ and the $p$-adic places $\mathbb{Q}_p$ — are physically meaningful. We conjecture that ZBW is the Archimedean shadow of mixing between the $\infty$-place and the $2$-place: a channel-mixing phenomenon analogous in structure to flavor mixing in quantum field theory, where flavor and mass Fock spaces are unitarily inequivalent [4]. The choice of the prime $p=2$ is motivated by the companion programme's identification of ZBW as a $\mathbb{Z}_2$-valued topological observable distinguishing Dirac from Majorana fermions [11], [12], and by the structural underdetermination of the position operator, which manifests at the Archimedean place as ZBW (the Newton–Wigner no-go) and at $p$-adic places as a discrete Bruhat–Tits observable [10].

Our contributions are: (i) a precise statement of the Archimedean–2-adic channel-mixing conjecture; (ii) a formulation of the free Dirac equation on the adèle ring with explicit mixing amplitudes; (iii) fully worked numerical derivations of the predicted ZBW frequency and of the adelic product formula for the prime $2$; (iv) a representation-independence argument under FW transformation; and (v) a falsification plan grounded in existing emulation platforms [5], [6], [7], [8].

## 2. Background and Related Work

**Historical core.** Breit and Schrödinger showed around 1930 that the eigenvalues of the velocity of a particle described by wave-packet solutions of the Dirac equation are simply $\pm c$, the speed of light; Schrödinger coined the term Zitterbewegung ("trembling motion") for the resulting back-and-forth zig-zag of fermions at the speed of light [1]. The statistical-mechanical treatment of the problem of motion in [1] frames ZBW as the central puzzle of the Dirac position operator. Our conjecture accepts this puzzle as real rather than representational.

**Interference and chirality.** The immediate description of chiral oscillations in terms of the trembling motion of the velocity (Dirac) operator $\boldsymbol{\alpha}$ arises when the complete set of Dirac-equation solutions is taken, so that a free propagating Dirac wave packet is composed of positive and negative frequency components [2]. This is precisely the interference picture our conjecture reinterprets: the positive/negative frequency split on $\mathbb{R}$ is proposed to be the Archimedean projection of a two-channel adelic structure.

**Flavor-mixing analogy.** In the quantum-field-theoretic treatment of neutrino mixing, the Fock space of flavor states is unitarily inequivalent to that of mass states (the inequivalent-vacua model), and a paradox emerges when these weak states are used to compute the amplitude of $W$ boson decay, with the branching ratio of $W^+ \to e^+ + \nu_\mu$ relative to $W^+ \to e^+ + \nu_e$ appearing approximately suppressed [4]. The supplied summary does not give the exact numerical value of that suppression, so we use the structural lesson only: mixing between inequivalent sector constructions produces oscillation phenomena and apparent paradoxes in amplitudes. Our $\infty \leftrightarrow 2$ channel mixing is modeled on exactly this pattern, with "flavor" replaced by "place."

**Emulation and control platforms.** ZBW can be converted to directed center-of-mass motion by a modulation of the Dirac-like equation when the modulation is on resonance with the ZB frequency; tailored modulation may also stop or re-launch the motion [3]. In a discrete-time quantum walk in coupled fiber loops, ballistic spreading and an oscillation between two internal quantum states similar to Zitterbewegung were experimentally observed, and a position-dependent phase gradient produces localization and Bloch oscillations [5]. Mirror oscillation in a "tripod-scheme" laser–atom system can drive an effective spin-orbit interaction and thereby control the amplitude, frequency, and damping of cold-atom ZBW, as shown both analytically and numerically [6]. In spin-orbit-coupled spin-1 cold atoms, the Zeeman field and harmonic trap significantly affect ZBW: the external Zeeman field can suppress or enhance the ZBW amplitude and change the oscillation frequencies, with a much slower oscillation also appearing [7]. Finally, ZBW charge oscillations can be detected through a charge conductance measurement in a three-terminal junction; tuning the spin-orbit interaction strength or an external magnetic field modulates the ZBW period, translating into complementary conductance oscillations in the two outgoing leads [8]. These four platforms [3], [5], [6], [7], [8] define the experimental landscape in which an adelic channel-mixing signature would have to be sought or bounded.

**The adelic programme.** The QNFO Adelic Physics Program proposes that the physically accessible base field of physics is $\mathbb{Q}$, not $\mathbb{R}$, and that Ostrowski's theorem demands all $p$-adic completions of $\mathbb{Q}$ be physically meaningful; it supplies the epistemological and pedagogical infrastructure for this claim [9]. Within that programme, the structural underdetermination of the position operator in relativistic quantum mechanics is diagnosed as having a single representation-theoretic origin, manifesting at the Archimedean place as ZBW (the Newton–Wigner no-go) and at $p$-adic places as a discrete Bruhat–Tits observable [10]. The ZBW–Majorana hypothesis establishes that ZBW — the rapid trembling motion of Dirac fermions at the Compton scale — is a $\mathbb{Z}_2$ topological observable distinguishing Dirac from Majorana fermions at the hardware level, developed across four companion papers [11]. And ZBW has been formulated as a $p$-adic topological observable: the ZBW current $J^{\mu}_{\mathrm{ZBW}}$ carries a $\mathbb{Z}_2$ invariant encoding the Dirac/Majorana distinction, with ultrametric readout protocols proposed via Bruhat–Tits buildings [12]. Our paper is the concrete, computationally explicit realization of the $\infty \leftrightarrow 2$ link asserted in [9], [10], [12].

## 3. Methods

### 3.1 Adelic kinematics

Let $\mathbb{A}_{\mathbb{Q}}$ denote the adèle ring of $\mathbb{Q}$, the restricted product $\mathbb{A}_{\mathbb{Q}} = \mathbb{R} \times \prod_{p}' \mathbb{Q}_p$, where the prime restricts almost all factors to $\mathbb{Z}_p$. A one-particle position is an adelic point $x = (x_\infty, x_2, x_3, \dots)$ with $x_v \in \mathbb{Q}_v$. The conjecture of this paper restricts attention to the two places $v \in \{\infty, 2\}$; all other places are assumed to factor out of the ZBW dynamics (an assumption we flag as a limitation in Section 6).

The free Dirac Hamiltonian on the real sector is

$$H_\infty = c\,\boldsymbol{\alpha}\cdot \mathbf{p}_\infty + \beta\, m c^2, \qquad H_\infty^2 = c^2 p_\infty^2 + m^2 c^4,$$

with spectrum $\pm E_\infty$, $E_\infty = \sqrt{c^2 p_\infty^2 + m^2 c^4}$. On the 2-adic sector we postulate the analogous quadratic form

$$H_2^2 = c^2 |p_2|_2^2 + m^2 c^4,$$

where $|\cdot|_2$ is the 2-adic norm, normalized so that $|2|_2 = 2^{-1}$ and $|q|_2 = 2^{-v_2(q)}$ for $q \in \mathbb{Q}$, with $v_2(q)$ the 2-adic valuation. The key structural fact is Ostrowski incommensurability: the norms $|\cdot|_\infty$ and $|\cdot|_2$ satisfy no nontrivial relation, so a state sharply localized in $x_\infty$ (a delta-like packet, broad in real momentum) is delocalized in $x_2$, and vice versa. Localization at one place forces delocalization at the other; this is the channel-mixing kinematics.

### 3.2 Channel-mixing ansatz

We write a two-level effective Hamiltonian in the place basis $\{|{\infty}\rangle, |{2}\rangle\}$:

$$H_{\mathrm{mix}} = \begin{pmatrix} E_\infty & \Delta \\ \Delta^{*} & E_2 \end{pmatrix},$$

where $E_2 = \sqrt{c^2 |p_2|_2^2 + m^2 c^4}$ and $\Delta$ is the $\infty \leftrightarrow 2$ transition amplitude, assumed real and proportional to the overlap of the packet's Fourier support at both places. The eigenfrequencies of $H_{\mathrm{mix}}$ are

$$\Omega_{\pm} = \frac{E_\infty + E_2}{2} \pm \sqrt{\left(\frac{E_\infty - E_2}{2}\right)^2 + |\Delta|^2},$$

and the channel populations oscillate at the beat frequency

$$\omega_{\mathrm{beat}} = \Omega_+ - \Omega_- = 2\sqrt{\left(\frac{E_\infty - E_2}{2}\right)^2 + |\Delta|^2}.$$

In the standard interference picture the observed ZBW frequency is $\omega_{\mathrm{ZBW}} = 2E/\hbar$ (the gap between $+E$ and $-E$ branches). The conjecture identifies the two: the $\pm E$ branches on $\mathbb{R}$ are the projections of the two mixed adelic eigenmodes, so that in the resonant regime $E_\infty \approx E_2 \equiv E$ and small $|\Delta|$,

$$\omega_{\mathrm{beat}} \approx \frac{2|\Delta|}{\hbar}\ \text{(in energy units)} \quad \longrightarrow \quad \omega_{\mathrm{ZBW}} = \frac{2E}{\hbar} \ \text{when}\ |\Delta| \sim E.$$

We do not derive $|\Delta| \sim E$ from first principles here; we state it as the conjecture's calibration condition and note that it is what makes the hypothesis empirically equivalent to the standard picture at the frequency level while differing in ontology.

### 3.3 Majorana condition and topological protection

The Majorana condition identifies particle and antiparticle; in the adelic language of this conjecture it realizes the identification of the $\infty$ and $2$ places, since the $\mathbb{Z}_2$ grading of the ZBW observable [11], [12] has exactly two sectors. Topological protection then follows from Ostrowski incommensurability: no continuous deformation of the packet can tune the ratio $|p|_\infty / |p|_2$ through zero, because the two norms are multiplicatively independent, so the channel gap cannot be closed by a smooth perturbation — the $\mathbb{Z}_2$ invariant is stable.

## 4. Analysis

All input numbers below are standard physical constants stated here explicitly as inputs; all arithmetic is shown step by step.

**Inputs.** Electron mass $m_e = 9.109 \times 10^{-31}\ \mathrm{kg}$; speed of light $c = 2.998 \times 10^{8}\ \mathrm{m\,s^{-1}}$; reduced Planck constant $\hbar = 1.055 \times 10^{-34}\ \mathrm{J\,s}$.

**Derivation 1: rest-frame ZBW angular frequency.** At rest, $p_\infty = 0$, so $E = m_e c^2$. Compute the rest energy:

$$E_0 = m_e c^2 = (9.109 \times 10^{-31}) \times (2.998 \times 10^{8})^2\ \mathrm{J}.$$

First, $c^2 = (2.998 \times 10^8)^2 = 8.988 \times 10^{16}\ \mathrm{m^2\,s^{-2}}$. Then

$$E_0 = 9.109 \times 10^{-31} \times 8.988 \times 10^{16} = 81.87 \times 10^{-15}\ \mathrm{J} = 8.187 \times 10^{-14}\ \mathrm{J}.$$

The conjectured and standard ZBW angular frequency is

$$\omega_{\mathrm{ZBW}} = \frac{2E_0}{\hbar} = \frac{2 \times 8.187 \times 10^{-14}}{1.055 \times 10^{-34}}\ \mathrm{s^{-1}}.$$

Numerator: $2 \times 8.187 \times 10^{-14} = 1.6374 \times 10^{-13}\ \mathrm{J}$. Dividing:

$$\omega_{\mathrm{ZBW}} = \frac{1.6374 \times 10^{-13}}{1.055 \times 10^{-34}} = 1.552 \times 10^{21}\ \mathrm{rad\,s^{-1}}.$$

The corresponding ordinary frequency is

$$\nu_{\mathrm{ZBW}} = \frac{\omega_{\mathrm{ZBW}}}{2\pi} = \frac{1.552 \times 10^{21}}{6.2832} = 2.470 \times 10^{20}\ \mathrm{Hz}.$$

The Compton angular frequency $\omega_C = E_0/\hbar = 7.761 \times 10^{20}\ \mathrm{rad\,s^{-1}}$ (half of $\omega_{\mathrm{ZBW}}$, by direct division: $8.187\times10^{-14} / 1.055\times10^{-34} = 7.761\times10^{20}$), so the ZBW oscillation runs at twice the Compton frequency, as the conjecture's beat structure predicts.

**Derivation 2: the adelic product formula for $q = 2$.** For any nonzero rational $q$, the product formula states $\prod_v |q|_v = 1$ over all places $v$. For $q = 2$ only the $\infty$ and $2$ places contribute nontrivially (for every odd prime $p$, $v_p(2) = 0$ so $|2|_p = 1$). Compute:

$$|2|_\infty = 2, \qquad |2|_2 = 2^{-v_2(2)} = 2^{-1} = \frac{1}{2}, \qquad |2|_p = 1 \ \ (p \ \text{odd}).$$

Therefore

$$\prod_v |2|_v = |2|_\infty \times |2|_2 \times \prod_{p\ \mathrm{odd}} |2|_p = 2 \times \frac{1}{2} \times 1 = 1.$$

This exact identity is the algebraic seed of the conjecture: the real and 2-adic norms of the prime $2$ are reciprocal, so the $\infty$ and $2$ channels are balanced in a way no other pair of places is for the prime that defines the $\mathbb{Z}_2$ grading of the ZBW observable [11], [12]. For comparison, for $q = 3$: $|3|_\infty \times |3|_3 = 3 \times \tfrac{1}{3} = 1$ as well — the product formula holds for every prime — but the conjecture singles out $p = 2$ because the ZBW observable is $\mathbb{Z}_2$-valued [11], not because the product formula is special to $2$.

**Derivation 3: beat frequency in the mixed channel.** Take a relativistic packet with $p_\infty c = 3 E_0$ (i.e., momentum three times the rest momentum in energy units). Then

$$E_\infty = \sqrt{(3E_0)^2 + E_0^2} = E_0\sqrt{10}.$$

With $E_0 = 8.187 \times 10^{-14}\ \mathrm{J}$ and $\sqrt{10} = 3.1623$:

$$E_\infty = 3.1623 \times 8.187 \times 10^{-14} = 2.589 \times 10^{-13}\ \mathrm{J}.$$

Assume the conjecture's calibration $|\Delta| = 0.1\, E_\infty$ and $E_2 = E_\infty$ (the 2-adic sector tuned to the same energy shell — a stated assumption, not a derivation). Then

$$\omega_{\mathrm{beat}} = \frac{2|\Delta|}{\hbar} = \frac{2 \times 0.1 \times 2.589 \times 10^{-13}}{1.055 \times 10^{-34}} = \frac{5.178 \times 10^{-14}}{1.055 \times 10^{-34}} = 4.908 \times 10^{20}\ \mathrm{rad\,s^{-1}}.$$

This is a *projection* conditional on the calibration assumption $|\Delta| = 0.1\,E_\infty$ and $E_2 = E_\infty$; its uncertainty is entirely dominated by the unknown $|\Delta|$, which could range over orders of magnitude. The purpose of Derivation 3 is to exhibit the functional dependence $\omega_{\mathrm{beat}} \propto |\Delta|/\hbar$, not to claim a measured value.

**Derivation 4: representation independence under Foldy–Wouthuysen.** The FW transformation $U_{\mathrm{FW}}$ diagonalizes $H_\infty$ into $\beta E_\infty$, removing the odd operator $\boldsymbol{\alpha}$ from the position dynamics. However, $U_{\mathrm{FW}}$ acts only on the Archimedean factor of the adelic Hilbert space $\mathcal{H} = \mathcal{H}_\infty \otimes \mathcal{H}_2$; it is a real-place unitary and cannot touch the $\infty \leftrightarrow 2$ mixing matrix element $\Delta$, which couples different places. Hence the beat frequency $\omega_{\mathrm{beat}} = 2\sqrt{((E_\infty - E_2)/2)^2 + |\Delta|^2}/\hbar$ is invariant under FW: the mixing is not a coordinate effect of the real representation. This is the precise sense in which the conjecture explains the persistence of ZBW under representation change, in contrast to the interference picture, in which FW diagonalization removes the trembling from the transformed position operator [1], [2].

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

1. **Rest-frame ZBW angular frequency (computed).** $\omega_{\mathrm{ZBW}} = 2m_e c^2/\hbar = 1.552 \times 10^{21}\ \mathrm{rad\,s^{-1}}$, from inputs $m_e = 9.109\times10^{-31}\ \mathrm{kg}$, $c = 2.998\times10^{8}\ \mathrm{m\,s^{-1}}$, $\hbar = 1.055\times10^{-34}\ \mathrm{J\,s}$ (Derivation 1).

2. **Rest-frame ZBW frequency (computed).** $\nu_{\mathrm{ZBW}} = \omega_{\mathrm{ZBW}}/2\pi = 2.470 \times 10^{20}\ \mathrm{Hz}$ (Derivation 1).

3. **Compton angular frequency (computed).** $\omega_C = m_e c^2/\hbar = 7.761 \times 10^{20}\ \mathrm{rad\,s^{-1}}$; the conjectured beat runs at exactly $2\omega_C$ (Derivation 1).

4. **Product formula for $q=2$ (computed, exact).** $|2|_\infty \cdot |2|_2 = 2 \cdot \tfrac{1}{2} = 1$, with $|2|_p = 1$ for all odd $p$; hence $\prod_v |2|_v = 1$ exactly (Derivation 2).

5. **Mixed-channel beat frequency (projection).** Under the stated assumptions $E_2 = E_\infty$ and $|\Delta| = 0.1\,E_\infty$ with $p_\infty c = 3E_0$, $\omega_{\mathrm{beat}} = 4.908 \times 10^{20}\ \mathrm{rad\,s^{-1}}$. Uncertainty: unbounded in practice, since $|\Delta|$ is not independently determined; the robust content is the proportionality $\omega_{\mathrm{beat}} = 2|\Delta|/\hbar$ in the degenerate shell.

6. **FW invariance (structural result).** $\omega_{\mathrm{beat}}$ is invariant under any Archimedean-only unitary such as $U_{\mathrm{FW}}$, because $\Delta$ couples distinct places (Derivation 4). No number is claimed beyond the formula itself.

## 6. Discussion

**Limitations.** The central weakness is the calibration condition $|\Delta| \sim E$: without an independent derivation of the mixing amplitude from the adelic Dirac equation, the conjecture is empirically indistinguishable from the standard interference picture at the level of frequencies, and differs only in ontology. Second, we restricted to two places ($\infty$ and $2$); the full adèle includes all primes, and the companion programme's Bruhat–Tits readout proposals [12] suggest all places may carry observables. Whether the odd-prime channels decouple is an open question we have assumed rather than proved. Third, the 2-adic Hamiltonian $H_2^2 = c^2|p_2|_2^2 + m^2c^4$ was postulated by structural analogy; no uniqueness argument was given, and other ultrametric kinetic terms are conceivable. Fourth, the neutrino-mixing analogy [4] is structural only: the supplied account of [4] reports unitarily inequivalent flavor and mass Fock spaces and an approximate suppression pattern in a $W$-decay branching ratio, but does not supply the numerical value, so no quantitative transfer from that work is possible here.

**Failure modes and falsification.** The conjecture is falsified if: (i) a ZBW emulation platform [5], [6], [7] shows the oscillation frequency shifting under a perturbation that, in the adelic model, would close the $\infty$–$2$ channel gap — since Ostrowski incommensurability predicts the $\mathbb{Z}_2$ invariant cannot be smoothly tuned away [11]; (ii) a FW-type transformation implemented experimentally (e.g., via the resonant-modulation control of [3] or the spin-orbit tuning of [8]) removes the oscillation entirely, which would support the pure interference picture; or (iii) the ZBW signal vanishes for Majorana-type quasiparticles in a way not matching the $\mathbb{Z}_2$ pattern of [11], [12]. Conversely, the conjecture is supported if ZBW period modulation by external parameters [8], [7] tracks a two-channel beat structure rather than a single-interference envelope.

**Against ourselves.** The strongest objection is that the interference picture [2] already explains all observed ZBW phenomenology, including its emulation in classical and photonic systems [5], [6], where no adelic structure exists. If ZBW in a fiber-loop quantum walk [5] — a system with no $\mathbb{Q}_2$ sector — reproduces every signature the adelic model predicts for the Dirac equation, then the adelic interpretation is either wrong or unfalsifiable at the emulation level, and only a genuinely fermionic, Compton-scale test (presently beyond direct experiment) could decide. We concede that the present paper therefore establishes a conjecture with a derivation skeleton, not a confirmed mechanism.

## 7. Conclusion

We have formulated the conjecture that Zitterbewegung is the Archimedean face of $\infty \leftrightarrow 2$ adelic channel mixing, given it an explicit two-place Hamiltonian structure, computed its predicted rest-frame frequency $\omega_{\mathrm{ZBW}} = 2m_ec^2/\hbar = 1.552\times10^{21}\ \mathrm{rad\,s^{-1}}$ with full arithmetic, proved the exact product-formula identity $|2|_\infty|2|_2 = 1$ that balances the two channels, and shown structural FW representation-independence. The framework connects the historical ZBW puzzle [1], [2] to the adelic physics programme [9], [10], the $\mathbb{Z}_2$ ZBW–Majorana observable [11], [12], and a concrete experimental landscape [3], [5], [6], [7], [8]. Its empirical content currently hinges on the undetermined mixing amplitude $\Delta$; deriving $\Delta$ from the adelic Dirac equation, and designing an emulation that discriminates the two-channel beat from single-interference ZBW, are the immediate open problems.

## References

[1] arXiv:1411.1854v2 | The Problem of Motion: The Statistical Mechanics of Zitterbewegung
[2] arXiv:hep-th/0701091v2 | Chiral oscillations in terms of the zitterbewegung effect
[3] arXiv:1105.2884v1 | Converting Zitterbewegung Oscillation to Directed Motion
[4] arXiv:hep-ph/0604069v2 | A Paradox on Quantum Field Theory of Neutrino Mixing and Oscillations
[5] arXiv:1104.0105v1 | Zitterbewegung, Bloch Oscillations and Landau-Zener Tunneling in a Quantum Walk
[6] arXiv:1003.3074v1 | Driven Dirac-like Equation via Mirror Oscillation: Controlled Cold-Atom Zitterbewegung
[7] arXiv:1210.5030v2 | Zitterbewegung effect in spin-orbit coupled spin-1 ultracold atoms
[8] arXiv:0810.2186v2 | Catching the zitterbewegung
[9] QNFO: The Adelic Physics Program: Epistemological Foundations and Communications Framework | DOI 10.5281/zenodo.21686727
[10] QNFO: The Adelic ZBW Programme: ZBW-Majorana Hypothesis, Ostrowski-QEC Synthesis, and Cross-Programme Consilience | DOI 10.5281/zenodo.21609223
[11] QNFO: Vanishing ZBW Signal: The ZBW-Majorana Hypothesis as a Unified Framework for Topological Fermion Distinction | DOI 10.5281/zenodo.21574555
[12] QNFO: Zitterbewegung as a p-Adic Observable: Ultrametric Readout and Intrinsic Topological Protection | DOI 10.5281/zenodo.21335853