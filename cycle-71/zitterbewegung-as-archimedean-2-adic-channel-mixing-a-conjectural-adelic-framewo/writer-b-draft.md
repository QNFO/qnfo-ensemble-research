# Zitterbewegung as Archimedean–2-adic Channel Mixing: A Toy Adelic Model of the Dirac Trembling Motion

## Abstract

Zitterbewegung (ZBW) — the Compton-frequency trembling of the Dirac velocity operator — is conventionally read as interference between positive- and negative-energy branches on the real line. This paper develops a conjecture, motivated by the adelic physics program, that ZBW is instead (or additionally) the observable signature of mixing between the Archimedean completion $\mathbb{R} = \mathbb{Q}_\infty$ and the 2-adic completion $\mathbb{Q}_2$ of the rationals: a packet localized at $x_\infty$ necessarily contains Fourier components delocalized at $x_2$, and the trembling motion is the beat pattern of this cross-place channel. We formalize this as a two-channel toy model in which the standard ZBW frequency $\omega_{\mathrm{ZBW}} = 2E/\hbar$ emerges as the beat frequency of the $\infty \leftrightarrow 2$ channel pair, we verify the arithmetic of the predicted electron-scale numbers ($\omega_{\mathrm{ZBW}} \approx 1.553 \times 10^{21}\ \mathrm{s^{-1}}$, $T_{\mathrm{ZBW}} \approx 4.05 \times 10^{-21}\ \mathrm{s}$), and we show that the adelic product formula and Ostrowski incommensurability supply a mechanism for the persistence of ZBW under Foldy–Wouthuysen transformation. We propose a falsifiable simulation protocol coupling a $p$-adic Schrödinger sector to a real sector, and we state explicitly which parts of the program are derived, which are conjectural, and what observations would refute the hypothesis.

## 1. Introduction

The velocity operator of a relativistic Dirac particle does not behave like a classical velocity. As recapped in the historical survey of Breit and Schrödinger's results [1], the eigenvalues of the velocity of a wave-packet solution of the Dirac equation are $\pm c$, and Schrödinger coined the term *Zitterbewegung* ("trembling motion") for the resulting rapid oscillation of the particle position at the Compton scale. The standard explanation is interference: a localized packet necessarily mixes positive- and negative-energy branches, and the cross terms oscillate at the beat frequency $2E/\hbar$.

This paper takes seriously a different reading, drawn from the adelic physics program [9]: the base field of physics is $\mathbb{Q}$, not $\mathbb{R}$, and Ostrowski's theorem then demands that *all* completions of $\mathbb{Q}$ — the Archimedean place $\mathbb{Q}_\infty = \mathbb{R}$ and every $p$-adic place $\mathbb{Q}_p$ — be physically meaningful. Under this reading, "localized on $\mathbb{R}$" and "localized on $\mathbb{Q}_2$" are not two descriptions of the same state but two channels of one adelic state, and a packet forced to be localized at the Archimedean place $x_\infty$ must carry compensating delocalization at the 2-adic place $x_2$. The conjecture of this paper is that ZBW is the physical beat pattern of this $\infty \leftrightarrow 2$ channel mixing.

The conjecture matters for three reasons. First, it would give an observable, Compton-scale empirical handle on whether $p$-adic sectors of the adele ring enter physics at all, converting a question of mathematical formalism into an experimental program. Second, it would explain a well-known puzzle: ZBW survives the Foldy–Wouthuysen (FW) transformation, which was designed to remove the trembling from the position operator, reappearing in other observables — suggesting an ontological rather than coordinate effect. Third, it connects to a developing literature that already treats ZBW as a topological, place-sensitive observable [10][11][12].

Our contribution is deliberately modest and explicit. We do not claim a complete adelic Dirac theory. We (i) construct a two-channel toy model in which the standard ZBW frequency is recovered as a beat frequency, (ii) show with explicit arithmetic that the adelic product formula and Ostrowski incommensurability of $\mathbb{R}$ and $\mathbb{Q}_2$ give a representation-independent mechanism for the persistence of the oscillation, (iii) derive the electron-scale numbers, and (iv) specify a simulation protocol and the observations that would falsify the hypothesis. All quantitative claims are either computed here with shown arithmetic or explicitly labeled projections with stated assumptions.

## 2. Background and Related Work

**Historical and theoretical ZBW.** Reference [1] situates the origin of the field: around 1930, Breit and Schrödinger showed that the eigenvalues of the velocity of wave-packet solutions to the Dirac equation are simply $\pm c$, and Schrödinger coined "Zitterbewegung" for the resulting back-and-forth zig-zag of fermions at the speed of light. The supplied summary of [1] is truncated before its later results, so we use it only for this historical framing. Reference [2] seeks the *immediate* description of chiral oscillations in terms of the trembling motion of the velocity (Dirac) operator $\boldsymbol{\alpha}$, taking the complete set of Dirac solutions so that a free propagating packet is composed of positive- and negative-frequency components; this is precisely the interference picture that our adelic model must reproduce in the Archimedean limit, and it supplies the mathematical template (complete-solution packets, cross-frequency beats) that Section 3 formalizes.

**Manipulation and control of ZBW.** Reference [3] shows that ZB can be converted into directed center-of-mass motion by modulating a Dirac-like equation when the modulation is on resonance with the ZB frequency, and that tailored modulation can also stop or re-launch the motion. This is important for us because it demonstrates that the ZB frequency is an experimentally addressable channel carrier: if ZBW were an adelic cross-place beat, resonance modulation [3] would be the natural knob for driving population between the $\infty$ and $2$ channels. Reference [6] studies mirror oscillation in a "tripod-scheme" laser–atom system and shows, analytically and numerically, that the driven effective spin–orbit interaction controls the amplitude, frequency, and damping of cold-atom ZBW — establishing that all three parameters our toy model predicts to be place-mixing dependent are in principle externally tunable. Reference [7] investigates ZBW in spin–orbit coupled spin-1 cold atoms under a Zeeman field and harmonic trap, showing that these external fields can suppress or enhance the ZBW amplitude and change the oscillation frequencies, with a much slower oscillation component appearing; the sensitivity of ZBW to external parameters is consistent with a mixing picture in which the external fields renormalize the effective channel-coupling.

**Detection proposals.** Reference [8] demonstrates how zitterbewegung charge oscillations can be detected through a conductance measurement in a three-terminal junction, with the ZB period modulated by tuning spin–orbit strength or an external magnetic field, producing complementary conductance oscillations in the two outgoing leads. The two-lead complementary-signal structure of [8] is structurally analogous to our two-channel ($\infty$/$2$) readout: the adelic conjecture predicts that the "trembling" signal should appear as complementary oscillations in observables naturally attached to the two places. Reference [5] reports an experimental discrete-time quantum walk in coupled fiber loops observing ballistic spreading and an oscillation between two internal quantum states similar to Zitterbewegung, plus localization and Bloch oscillations under a position-dependent phase gradient; this shows that ZBW-like two-state beating is realizable and measurable in synthetic systems, which is the platform class our simulation protocol in Section 3 targets.

**Mixing analogies and caveats.** Reference [4] studies neutrino mixing and oscillations in quantum field theory, where the Fock space of flavor states is unitarily inequivalent to that of mass states (inequivalent vacua), and reports a paradox in which weak-state amplitudes for $W$-boson decay give an apparently wrong branching ratio for $W^{+} \to e^{+} + \nu_\mu$ versus $W^{+} \to e^{+} + \nu_e$. The analogy is instructive and cautionary: mixing between sectors with inequivalent vacuum structures — exactly the situation our $\infty$/$2$ channels face, since the supplied summary of [4] shows that QFT mixing across inequivalent Fock spaces can generate apparent paradoxes in decay amplitudes — requires care in defining cross-channel amplitudes, and any adelic mixing amplitude must be checked against such consistency conditions.

**The adelic program.** Reference [9] proposes that the physically accessible base field is $\mathbb{Q}$, not $\mathbb{R}$, and that Ostrowski's theorem demands all $p$-adic completions of $\mathbb{Q}$ be physically meaningful, providing the epistemological and pedagogical infrastructure of the program; this is the axiom from which our channel picture descends. Reference [10] argues that the structural underdetermination of the position operator in relativistic quantum mechanics — manifested at the Archimedean place as zitterbewegung (the Newton–Wigner no-go) and at $p$-adic places as a discrete Bruhat–Tits observable — arises from a single representation-theoretic origin; this is the closest existing statement to our thesis, and our toy model can be read as a concrete two-place instantiation of it. Reference [11] establishes, across companion papers, that ZBW is a $\mathbb{Z}_2$ topological observable distinguishing Dirac from Majorana fermions at the hardware level, with a vanishing ZBW signal for the Majorana case; in our channel language, the Majorana condition is the self-conjugacy that identifies the $\infty$ and $2$ places, killing the beat. Reference [12] formulates ZBW as a $p$-adic topological observable, establishes that the ZBW current $J^{\mu}_{\mathrm{ZBW}}$ carries a $\mathbb{Z}_2$ invariant encoding the Dirac/Majorana distinction, and proposes ultrametric readout protocols via Bruhat–Tits buildings; this supplies the candidate readout geometry for the $x_2$ channel.

## 3. Methods

### 3.1 The two-channel toy model

Let $\mathcal{H} = \mathcal{H}_\infty \oplus \mathcal{H}_2$ be a formal two-channel Hilbert space, with $\mathcal{H}_\infty$ the usual Archimedean Dirac sector and $\mathcal{H}_2$ a 2-adic sector whose position observable $x_2$ takes values in $\mathbb{Q}_2$ (ultrametric; see [12] for the Bruhat–Tits readout geometry). We write the free channel Hamiltonian as

$$
H_0 = E_\infty \, \sigma_z \otimes \mathbf{1} + E_2 \, \mathbf{1} \otimes \sigma_z ,
$$

where $\sigma_z$ distinguishes the positive/negative energy branches within each channel and $E_\infty = E_2 \equiv E$ is the mean packet energy (we assume place-independence of the energy eigenvalue, which is the minimal consistency condition for a single adelic state). The channel-mixing perturbation is

$$
H_{\mathrm{mix}} = \Delta \, (\sigma_x \otimes \tau_x),
$$

with $\tau_x$ flipping between the $\infty$ and $2$ channels and $\Delta$ the (conjectural, undetermined) mixing matrix element. The physical claim under test is that a state prepared "localized at $x_\infty$" — i.e., in the $\mathcal{H}_\infty$ channel — is not an energy eigenstate of the full adelic Hamiltonian, and its evolution contains a cross-channel beat.

### 3.2 Recovery of the standard ZBW frequency

Within $\mathcal{H}_\infty$ alone, the standard derivation [1][2] is: a localized packet is a superposition of positive- and negative-energy branches $\lvert +E \rangle$ and $\lvert -E \rangle$. The velocity operator expectation contains the cross term

$$
\langle \boldsymbol{\alpha} \rangle (t) \supset \langle +E \rvert \boldsymbol{\alpha} \lvert -E \rangle \, e^{-i(E - (-E))t/\hbar} + \mathrm{c.c.} = \boldsymbol{\alpha}_{+-} \, e^{-i \omega_{\mathrm{ZBW}} t} + \mathrm{c.c.},
$$

with beat frequency

$$
\omega_{\mathrm{ZBW}} = \frac{2E}{\hbar}.
$$

In the two-channel model, the identical beat structure arises from the pair of channel-branch states $\lvert +E, \infty \rangle$ and $\lvert -E, 2 \rangle$: the cross term between a branch in one place and the conjugate branch in the other place oscillates at the same difference frequency $2E/\hbar$, because we have assumed $E_\infty = E_2 = E$. The toy model therefore reproduces the empirically robust frequency [3][5][6][7][8] while reinterpreting its origin: the oscillation is a *cross-place* beat, not merely a cross-energy beat on $\mathbb{R}$.

### 3.3 Persistence under Foldy–Wouthuysen as an adelic effect

The FW transformation diagonalizes the Dirac Hamiltonian and removes the trembling from the *Archimedean* position operator; yet ZBW signatures persist in other observables. In the channel picture this is expected: the FW transformation is a unitary rotation *within* $\mathcal{H}_\infty$ and cannot touch the $\mathcal{H}_2$ channel or the mixing term $\Delta$. Formally, if $U_{\mathrm{FW}}$ acts as $U_{\mathrm{FW}} \otimes \mathbf{1}_2$, then

$$
U_{\mathrm{FW}} H_{\mathrm{mix}} U_{\mathrm{FW}}^{\dagger} = (U_{\mathrm{FW}} \sigma_x U_{\mathrm{FW}}^{\dagger}) \otimes \tau_x ,
$$

which is a nonzero, merely re-phased mixing. The beat frequency $\omega_{\mathrm{ZBW}} = 2E/\hbar$ is invariant because it is a difference of eigenvalues, which no unitary changes. This is the precise sense in which the conjecture explains ZBW's persistence as ontological rather than coordinate-dependent.

### 3.4 The 2-adic side and topological protection

On $\mathbb{Q}_2$, the absolute value is $\lvert 2 \rvert_2 = 1/2$ and more generally $\lvert 2^{n} \rvert_2 = 2^{-n}$. The Archimedean and 2-adic norms are Ostrowski-incommensurable: for the same rational number the two norms diverge in opposite directions, so no re-scaling of one place mimics the other. This incommensurability is the proposed source of topological protection: a perturbation that is small in the Archimedean sense ($\lvert \delta \rvert_\infty \ll 1$) can be large or trivial in the 2-adic sense, and vice versa, so the channel distinction cannot be erased by Archimedean noise alone. The Majorana condition, following [11][12], is modeled as the self-conjugacy constraint that identifies the two channels; when the identification is exact, the cross-channel beat term cancels and the ZBW signal vanishes — the $\mathbb{Z}_2$ Dirac/Majorana distinction.

### 3.5 Simulation protocol

Following the demonstrated controllability of ZBW in synthetic systems [5][6][7] and its electrical detectability [8], we propose a simulation in which a discrete dynamics emulating a $p$-adic (ultrametric) position space is coupled to a continuous real-space sector, with a tunable coupling $\Delta$. The predicted signatures are: (i) an oscillation at $\omega_{\mathrm{ZBW}} = 2E/\hbar$ (in scaled simulator units, $2\tilde{E}/\hbar_{\mathrm{eff}}$) that survives diagonalization of the real-sector Hamiltonian; (ii) complementary oscillations in two readout channels attached to the two places, in analogy with the two-lead conductance signals of [8]; (iii) suppression of the oscillation when the Majorana identification constraint is imposed.

## 4. Analysis

All numerical inputs are declared here. Physical constants used (standard values, stated as inputs): electron rest energy $m_e c^2 = 5.1099895 \times 10^{5}\ \mathrm{eV}$; reduced Planck constant $\hbar = 6.582119569 \times 10^{-16}\ \mathrm{eV \cdot s}$; speed of light $c = 2.99792458 \times 10^{8}\ \mathrm{m/s}$; reduced Compton wavelength factor $\hbar c = 197.3269804\ \mathrm{eV \cdot nm}$.

**Derivation 1: ZBW angular frequency for the electron.** Setting $E = m_e c^2$ in $\omega_{\mathrm{ZBW}} = 2E/\hbar$:

$$
\omega_{\mathrm{ZBW}} = \frac{2 \, m_e c^2}{\hbar} = \frac{2 \times 5.1099895 \times 10^{5}\ \mathrm{eV}}{6.582119569 \times 10^{-16}\ \mathrm{eV \cdot s}}.
$$

Numerator: $2 \times 5.1099895 \times 10^{5} = 1.0219979 \times 10^{6}\ \mathrm{eV}$. Dividing:

$$
\omega_{\mathrm{ZBW}} = \frac{1.0219979 \times 10^{6}}{6.582119569 \times 10^{-16}}\ \mathrm{s^{-1}} = 1.5527 \times 10^{21}\ \mathrm{s^{-1}},
$$

since $1.0219979 / 6.582119569 = 0.15527$ and $10^{6} / 10^{-16} = 10^{22}$, giving $0.15527 \times 10^{22} = 1.5527 \times 10^{21}\ \mathrm{s^{-1}}$.

**Derivation 2: ZBW period.**

$$
T_{\mathrm{ZBW}} = \frac{2\pi}{\omega_{\mathrm{ZBW}}} = \frac{6.283185307}{1.5527 \times 10^{21}\ \mathrm{s^{-1}}} = 4.046 \times 10^{-21}\ \mathrm{s},
$$

since $6.283185307 / 1.5527 = 4.0465$.

**Derivation 3: reduced Compton wavelength (the spatial scale of one ZBW cycle).**

$$
\bar{\lambda}_C = \frac{\hbar c}{m_e c^2} = \frac{197.3269804\ \mathrm{eV \cdot nm}}{5.1099895 \times 10^{5}\ \mathrm{eV}} = 3.8616 \times 10^{-4}\ \mathrm{nm} = 3.8616 \times 10^{-13}\ \mathrm{m},
$$

since $197.3269804 / 510998.95 = 3.8616 \times 10^{-4}$.

**Derivation 4: the adelic product formula on explicit rationals.** For $x = 2$: $\lvert 2 \rvert_\infty = 2$ and $\lvert 2 \rvert_2 = 1/2$, so

$$
\lvert 2 \rvert_\infty \cdot \lvert 2 \rvert_2 = 2 \times \frac{1}{2} = 1.
$$

For $x = 12 = 2^2 \cdot 3$: $\lvert 12 \rvert_\infty = 12$, $\lvert 12 \rvert_2 = 2^{-2} = 1/4$, $\lvert 12 \rvert_3 = 3^{-1} = 1/3$, and all other places give $1$; hence

$$
\lvert 12 \rvert_\infty \lvert 12 \rvert_2 \lvert 12 \rvert_3 = 12 \times \frac{1}{4} \times \frac{1}{3} = \frac{12}{12} = 1.
$$

This is the identity that, in the conjecture, enforces the bookkeeping between Archimedean localization and 2-adic delocalization: whatever amplitude is concentrated at one place is compensated at the others.

**Derivation 5: Ostrowski incommensurability, explicit.** For $n = 10$: $\lvert 2^{10} \rvert_\infty = \lvert 1024 \rvert_\infty = 1024$, while

$$
\lvert 2^{10} \rvert_2 = 2^{-10} = \frac{1}{1024} = 9.765625 \times 10^{-4}.
$$

The product is again $1024 \times 9.765625 \times 10^{-4} = 1$. As $n \to \infty$, $\lvert 2^{n} \rvert_\infty \to \infty$ while $\lvert 2^{n} \rvert_2 \to 0$: the two norms are monotone opposites on the same sequence, which is the precise sense in which no Archimedean perturbation can be relabeled as a 2-adic one.

**Derivation 6: FW invariance of the beat frequency.** The beat frequency is a difference of eigenvalues of $H_0$: $\omega = (E - (-E))/\hbar = 2E/\hbar$. Under any unitary $U$, the spectrum is unchanged, so $\omega_{\mathrm{ZBW}}$ is invariant. For the electron this is the value of Derivation 1, $1.5527 \times 10^{21}\ \mathrm{s^{-1}}$, independent of representation — including the FW frame.

**Derivation 7: cross-channel beat amplitude (labeled projection).** If the initial state is $\lvert \psi(0) \rangle = \lvert +E, \infty \rangle$ and the mixing Hamiltonian is $H_{\mathrm{mix}} = \Delta (\sigma_x \otimes \tau_x)$, first-order perturbation theory gives the population of the partner channel-branch state $\lvert -E, 2 \rangle$ as a projection with stated assumptions:

$$
P_{2}(t) \approx \left( \frac{\Delta}{2E} \right)^{2} \sin^{2}\!\left( \frac{2Et}{\hbar} \right),
$$

under the assumptions that $\Delta \ll E$ (weak mixing), that the two-level reduction is valid, and that $\Delta$ is a free parameter to be fixed by the proposed simulation. The observable ZBW modulation depth in an Archimedean detector is then proportional to $P_2$; since $\Delta$ is undetermined, we report only the *structure* $P_2 \propto (\Delta/2E)^2$ and not a numerical depth. This is an explicit limitation, not a result.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; no empirical or simulated data are reported.

1. **Predicted ZBW angular frequency (electron, $E = m_e c^2$):** $\omega_{\mathrm{ZBW}} = 2 m_e c^2 / \hbar = 1.5527 \times 10^{21}\ \mathrm{s^{-1}}$ (Derivation 1).
2. **Predicted ZBW period:** $T_{\mathrm{ZBW}} = 2\pi/\omega_{\mathrm{ZBW}} = 4.046 \times 10^{-21}\ \mathrm{s}$ (Derivation 2).
3. **Spatial scale:** $\bar{\lambda}_C = \hbar c / m_e c^2 = 3.8616 \times 10^{-13}\ \mathrm{m}$ (Derivation 3).
4. **Product-formula identities:** $\lvert 2 \rvert_\infty \lvert 2 \rvert_2 = 1$ and $\lvert 12 \rvert_\infty \lvert 12 \rvert_2 \lvert 12 \rvert_3 = 1$ (Derivation 4).
5. **Incommensurability witness:** $\lvert 1024 \rvert_\infty = 1024$ versus $\lvert 1024 \rvert_2 = 9.765625 \times 10^{-4}$ (Derivation 5).
6. **Representation independence:** $\omega_{\mathrm{ZBW}}$ is a spectral difference and equals $1.5527 \times 10^{21}\ \mathrm{s^{-1}}$ in every frame, including FW (Derivation 6).
7. **Projected mixing signature (projection, assumptions stated):** $P_2(t) \approx (\Delta/2E)^2 \sin^{2}(2Et/\hbar)$ with $\Delta \ll E$ and $\Delta$ undetermined; no numerical depth is claimed (Derivation 7).

The falsifiable core is items 1, 2, 6, and 7: the frequency and period are fixed by known constants; the FW-invariance is a structural prediction; and the mixing law $P_2 \propto (\Delta/2E)^2$ with its Majorana-suppression corollary is testable in the simulator platforms of [5][6][7] and the junction geometry of [8].

## 6. Discussion

**Limitations.** The central weakness of this paper is that the channel-mixing amplitude $\Delta$ is a free parameter with no derivation from first principles; without it, the model predicts the *frequency structure* of ZBW (which the standard interference picture already predicts) but no new *magnitude*. The identification $E_\infty = E_2$ is assumed, not derived; a derivation from an adelic Dirac operator on the full adele ring is the missing mathematical step, and the inequivalent-vacuum lessons of neutrino mixing [4] warn that cross-sector amplitudes in QFT can be subtle or even paradoxical when the sector Fock spaces differ. The claim that the Majorana condition "identifies the $\infty$ and $2$ places" is here only a formal ansatz consistent with the $\mathbb{Z}_2$ structure reported in [11][12]; we have not derived the vanishing of the ZBW signal from it, only asserted consistency with it.

**Failure modes.** The conjecture would be falsified if: (i) a complete Archimedean account reproduced every ZBW observable including its behavior under external driving [3][6][7] with no residual place-mixing parameter, Occam-cutting the second channel; (ii) the proposed simulator showed ZBW-like beats with *no* dependence on any ultrametric-sector coupling, i.e., the beat survived when $\Delta \to 0$; (iii) the FW frame exhibited a frame-dependent ZBW frequency, contradicting the spectral-difference argument of Derivation 6. Conversely, confirmation would require observing the complementary two-channel oscillation structure analogous to [8] in a system with a genuinely ultrametric sector — a demanding requirement, since no existing experiment cited here includes a $p$-adic sector.

**Against ourselves.** A skeptic should note that everything computed here (items 1–3) is standard Dirac theory; the adelic reinterpretation adds no new Archimedean number. Its content is entirely in the untested structural claims (channel complementarity, Majorana identification, topological protection via incommensurability). The strongest counterargument is that the toy model is unfalsifiable as it stands because $\Delta$ can always be tuned to zero post hoc; the remedy is the pre-registration of the simulator signature (iii) in Section 3.5: if the beat persists at $\Delta = 0$, the channel picture is dead. We also flag that the epistemological axiom of [9] — that all completions of $\mathbb{Q}$ are physically meaningful — is itself contested; if only $\mathbb{R}$ is physical, the conjecture collapses to a relabeling.

**Open questions.** Can $\Delta$ be computed from an adelic Dirac action? Does the product formula fix a normalization of the cross-channel amplitude (Derivation 4 suggests a bookkeeping constraint but not a dynamics)? What is the precise Bruhat–Tits readout map of [12] in simulator terms? Is the slow oscillation component seen in spin-1 cold atoms [7] reproducible as a multi-place beat?

## 7. Conclusion

We have formulated Zitterbewegung as a candidate Archimedean–2-adic channel-mixing phenomenon, built a two-channel toy model that recovers the standard beat frequency $\omega_{\mathrm{ZBW}} = 2E