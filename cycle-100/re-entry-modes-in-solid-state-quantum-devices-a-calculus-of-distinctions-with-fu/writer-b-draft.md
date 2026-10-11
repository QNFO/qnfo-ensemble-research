# Re-entrant Modes in Solid-State Quantum Devices: A Laws-of-Form Reading with Quantitative Benchmarks

## Abstract

Spencer-Brown's *Laws of Form* introduced "re-entry" — the return of a form into its own distinction — as a primitive of self-referential structure. This paper asks whether re-entry is a useful organizing concept for solid-state quantum devices, and answers by cataloguing re-entrant motifs across eight device- and material-physics settings drawn from a fixed bibliography: Andreev reflection at paired fractional-quantum-Hall edges, adiabatic population passage, phonon-blocked junction refrigeration, pyrochlore solid solutions with suppressed local moments, lambda- and Schottky-anomalous phase transitions, and Hall scaling in a borocarbide superconductor. We formalize re-entry as a map from a device's excitation sector back into itself and supply explicit quantitative benchmarks: the Schottky-anomaly peak position $x^{\ast} = \Delta/(k_B T) = 2.3993$ and peak height $C_{\max} = 0.4393\,R = 3.653\ \mathrm{J\,mol^{-1}\,K^{-1}}$, derived here by Newton iteration; thermal scales $k_B T = 8.617\times 10^{-5}\ \mathrm{eV}$ at $1\ \mathrm{K}$ and $0.1614\ \mathrm{eV}$ at the $1873.15\ \mathrm{K}$ synthesis temperature of pyrochlore solid solutions; and a magnetoresistance ratio of $1.90$ at $\mu_0 H = 16\ \mathrm{T}$, $T = 20\ \mathrm{K}$ in LuNi$_2$B$_2$C. We argue that re-entry is a classificatory lens, not yet a predictive theory, and state the conditions under which that claim would fail.

## 1. Introduction

The research question addressed here originates in a remediation note attached to the QNFO (Quantum Laws of Form) corpus: *re-entry from the Laws of Form tradition — these modes in solid-state devices?* In Spencer-Brown's formalism, as summarized in the QNFO consolidation [9], the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics are to be constructed; "re-entry" is the configuration in which a form crosses back into the space it itself distinguishes, producing a self-referential, recursively closed structure. The QNFO program [9] synthesizes known quantum correspondences to this formalism, identifies 7 open problem categories, and proposes 4 extensions; a companion register [10] organizes sixteen records from a single research program, spanning December 2025 to August 2026, into one testable claim about ultrametric ($p$-adic) structure in trapped-ion quantum dynamics.

The present paper takes the re-entry concept seriously as a *classificatory* hypothesis about solid-state devices: that a recognizable family of device behaviors — quasiparticle conversion that returns an excitation as its own conjugate, population transfer that closes a loop back onto its initial state, heat flow that is blocked and thereby re-routed into the electronic sector, anomalous heat capacity that encodes a transition's latent heat inside the transition itself — can be uniformly described as re-entrant maps on the excitation sector. We do not claim that this reading is unique or that it predicts new effects; we claim it is falsifiable as a *taxonomy*: if the re-entrant description of these settings generates no shared quantitative invariant beyond notation, the lens has failed.

Our method is deliberately conservative. Every claim about the outside world is anchored in a fixed bibliography of ten entries [1]–[10]; every number is either quoted from those entries, converted by shown arithmetic, or derived here from first principles of statistical mechanics with every step displayed. Section 2 reviews the bibliography. Section 3 defines the formal re-entry map. Section 4 performs the derivations. Section 5 reports only computed numbers. Section 6 discusses limitations and failure modes, and Section 7 concludes.

## 2. Background and Related Work

We discuss all ten bibliography entries, in their given order, restricting ourselves to what each supplied summary states.

**[1] High-temperature superconductivity for solid-state chemists.** This introduction to superconductivity states that electrical resistance is completely eliminated below the critical temperature $T_c$, identified as the most important parameter in the field, and notes that since the discovery of copper oxide superconductors 39 years ago (relative to the entry's writing) solid-state chemists have contributed significantly by discovering new compounds. For our purposes, the superconducting condensate supplies the cleanest physical re-entry channel: an excitation crossing into the condensate can return as its conjugate, the mechanism treated quantitatively in [2].

**[2] Tunneling in paired fractional quantum Hall states.** This work studies edge transport of paired fractional quantum Hall (FQH) states — the Haldane–Rezayi (HR), Moore–Read (Pfaffian), and Halperin (331) states — and gives a table of exponents for tunneling between the edges of paired FQH states in gated 2D structures and for tunneling into the edge from a normal Fermi liquid (N); it reports that HR, Pfaffian, and 331 states have (the summary truncates here). The Andreev-reflection process named in the title — where a normal-metal electron enters a paired medium and returns as a hole — is the paradigm case of the re-entrant excitation map we formalize in Section 3. The supplied summary gives no exponent values, so we use the work only at the level of process identification.

**[3] Applications of adiabatic passage in solid-state devices.** This paper introduces coherent population transfer by adiabatic passage — described as a well-known quantum-optics method that remained largely unknown to solid-state physicists — and discusses applications in solid-state systems. Adiabatic passage is re-entrant in our sense when the transfer path returns population to a state connected to the origin, closing a loop in Hilbert space; the adiabaticity condition itself is a quantitative constraint we state symbolically in Section 3.

**[4] Residual interactions among Laughlin quasiparticles.** Using exact numerical diagonalization of small systems, this work extracts pseudopotentials $V_{\mathrm{QP}}(R)$ describing the interaction energy of quasielectrons (QE) or quasiholes (QH) as a function of their relative angular momentum $R$, and finds that these pseudopotentials cannot support Laughlin correlations at certain quasiparticle filling factors (e.g., $\nu_{\mathrm{QE}} = 1/3$ and $\nu_{\mathrm{QH}} = 1/5$), motivating novel hierarchy states. This is a re-entry of interactions into the very sector they stabilize: the quasiparticles' own residual interactions destabilize the Laughlin state that defines them.

**[5] Phonon-blocked junction refrigerators.** This work addresses refrigeration as an enabler of quantum technology, noting that the very low energy of fundamental excitations in quantum devices requires temperatures well below $1\ \mathrm{K}$, that expensive cryostats are currently used in the sub-1 K regime, and that new electronic micro-coolers based on phonon-blocked semiconductors (summary truncates) are proposed as solid-state cooling solutions. Phonon blocking is re-entrant heat management: the lattice heat channel is closed so that heat is forced back through the electronic junction, the sector the device actively controls.

**[6] Pyrochlore solid solutions (Y,Lu)$_2$Ti$_{2-x}$(Nb,Ta)$_x$O$_{7\pm y}$.** This entry describes synthesis and characterization of the pyrochlore solid solutions Y$_2$Ti$_{2-x}$Nb$_x$O$_{7-y}$, Lu$_2$Ti$_{2-x}$Nb$_x$O$_{7-y}$, Y$_2$Ti$_{2-x}$Ta$_x$O$_{7-y}$ and Lu$_2$TiTaO$_{7-y}$ with $-0.4 < y < 0.5$; synthesis at $1600\ ^\circ\mathrm{C}$ and $10^{-5}$ Torr yields oxygen deficiency in all systems, and all compounds are found to be paramagnetic and semiconducting, with local moments smaller — in some cases substantially smaller — than the expected (summary truncates). Suppressed moments relative to expectation are a re-entrant magnetic signature: the moment the lattice expects to see is returned reduced, i.e., screened by the itinerant sector.

**[7] Lambda- and Schottky-anomalies in solid-state phase transitions.** This analysis shows that lambda and Schottky anomalies in solid-state phase transitions are the latent heat of nucleation-and-growth phase transitions. This is the most direct re-entry of the set: the anomaly is the transition's own latent heat re-entering the thermodynamic response function, and it admits the sharpest quantitative treatment in this paper (Section 4.1).

**[8] Hall effect in LuNi$_2$B$_2$C.** The Hall resistivity $\rho_{xy}$ of LuNi$_2$B$_2$C is negative in both the normal and mixed state and shows no sign reversal of the type typical for high-$T_c$ superconductors; a distinct nonlinearity in $\rho_{xy}(H)$ was found in the normal state for $T < 40\ \mathrm{K}$, accompanied by a large magnetoresistance reaching $+90\%$ for $\mu_0 H = 16\ \mathrm{T}$ at $T = 20\ \mathrm{K}$; a scaling relation $\rho_{xy} \sim \rho_{xx}^{\,\beta}$ is discussed (summary truncates). Self-similar power-law scaling between two transport coefficients is a re-entrant, scale-free relation; we compute the implied resistance ratio in Section 4.3.

**[9] QNFO: Quantum Laws of Form.** This consolidation records that Spencer-Brown's *Laws of Form* (1969) proposed drawing a distinction as the primitive operation from which logic, mathematics, and physics can be constructed, synthesizes known quantum correspondences, identifies 7 open problem categories, and proposes 4 extensions. It supplies the conceptual vocabulary ("distinction," "re-entry") used throughout this paper; the summary does not enumerate the correspondences or the extensions, so we rely on it only for the framework claim.

**[10] QNFO: The Trapped-Ion Ultrametric Testbed.** This register organizes sixteen published records from a single research program, spanning December 2025 to August 2026, into one testable claim: that trapped-ion quantum simulators are the first near-term platform on which ultrametric ($p$-adic) structure in quantum dynamics can be accepted or rejected by measurement. It is the methodological model for this paper: a single falsifiable claim, a fixed register of evidence, and explicit acceptance/rejection criteria. Our Section 6 adopts the same falsifiability discipline for the re-entry taxonomy.

## 3. Methods

### 3.1 The re-entry map

Let $\mathcal{H}_{\mathrm{ex}}$ denote the excitation sector of a device — the subspace of its Hilbert or state space carrying mobile, controllable excitations — and let $\mathcal{D}$ denote the distinction the device draws (junction, edge, interface, or order parameter). We define a **re-entrant mode** as a process $M: \mathcal{H}_{\mathrm{ex}} \to \mathcal{H}_{\mathrm{ex}}$ with the property that the returning excitation is *constitutively related* to the emitted one: same quasiparticle re-scattered, conjugate returned (Andreev), population returned to a loop-closed state (adiabatic passage), or response function containing the transition's own latent heat (anomaly). Formally, $M$ is re-entrant if there exists a nontrivial involution or self-map $\sigma$ on $\mathcal{H}_{\mathrm{ex}}$ such that

$$
M = \sigma \circ \iota, \qquad \sigma^2 = \mathbb{1}_{\mathcal{H}_{\mathrm{ex}}},
$$

where $\iota$ is injection across the distinction $\mathcal{D}$ and $\sigma$ is the return map. For Andreev reflection, $\sigma$ exchanges electron and hole; for adiabatic passage, $\sigma$ is the identity on population with a geometric phase; for the Schottky anomaly, $\sigma$ maps the ordered phase's latent heat into the heat-capacity response.

### 3.2 Quantitative instruments

Three standard results are used as instruments; each is derived, not asserted, in Section 4:

1. **Two-level Schottky anomaly.** For a two-level system with splitting $\Delta$, the heat capacity per two-level system is
$$
C(x) = R\, x^2 \frac{e^{x}}{\left(1 + e^{x}\right)^2}, \qquad x \equiv \frac{\Delta}{k_B T},
$$
where $R$ is the gas constant. The peak location $x^{\ast}$ and height $C(x^{\ast})$ are derived in Section 4.1.

2. **Thermal scale.** $k_B = 1.380649 \times 10^{-23}\ \mathrm{J\,K^{-1}} = 8.617333 \times 10^{-5}\ \mathrm{eV\,K^{-1}}$, so the thermal energy at temperature $T$ is $k_B T = (8.617333 \times 10^{-5}\ \mathrm{eV\,K^{-1}})\, T$.

3. **Adiabaticity.** For a passage driven through an avoided crossing with minimum gap $\Omega$ and sweep rate $|\dot{\theta}|$ of the mixing angle, adiabaticity requires
$$
\gamma \equiv \frac{\Omega^2}{|\dot{\theta}|} \gg 1,
$$
a condition stated in [3] at the level of principle; no numerical gap or sweep values are supplied by the bibliography, so we keep $\gamma$ symbolic.

### 3.3 Evidence discipline

Following the register model of [10], we fix the bibliography as the sole evidence base, distinguish (i) quoted numbers, (ii) unit conversions, (iii) derivations from stated instruments, and (iv) labeled projections, and report in Section 5 only categories (i)–(iii), plus (iv) with explicit assumptions and bounds.

## 4. Analysis

### 4.1 Schottky-anomaly peak: full derivation

**Input:** the two-level heat-capacity formula of Section 3.2, with $R = 8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$ (fundamental constant). The connection to [7] is qualitative: [7] establishes that Schottky anomalies are latent heat of nucleation-and-growth transitions; we derive the anomaly's shape parameters as the quantitative fingerprint such a re-entry leaves.

Maximize $f(x) = x^2 e^x/(1+e^x)^2$. Taking the logarithmic derivative:

$$
\frac{d \ln f}{dx} = \frac{2}{x} + 1 - \frac{2 e^x}{1 + e^x} = \frac{2}{x} - \tanh\!\left(\frac{x}{2}\right).
$$

Setting this to zero gives the peak condition

$$
x \tanh\!\left(\frac{x}{2}\right) = 2.
$$

**Newton iteration.** Let $g(x) = x \tanh(x/2) - 2$. Start at $x_0 = 2.4$:
- $\tanh(1.2) = 0.833655$, so $g(2.4) = 2.4 \times 0.833655 - 2 = 2.000772 - 2 = 0.000772$.
- $g'(x) = \tanh(x/2) + (x/2)\,\mathrm{sech}^2(x/2)$; $\mathrm{sech}^2(1.2) = 1 - 0.833655^2 = 1 - 0.694981 = 0.305019$; $g'(2.4) = 0.833655 + 1.2 \times 0.305019 = 0.833655 + 0.366023 = 1.199678$.
- $x_1 = 2.4 - 0.000772/1.199678 = 2.4 - 0.000644 = 2.399356$.

Residual check: $\tanh(1.199678) = 0.833621$; $2.399356 \times 0.833621 = 2.000015$; one more step gives $x^{\ast} = 2.399343$. We adopt

$$
x^{\ast} = 2.3993.
$$

**Peak height.** With $x^{\ast} = 2.399343$: $e^{x^{\ast}} = e^{2.4} \cdot e^{-0.000657} = 11.023176 \times 0.999343 = 11.015885$. Then

$$
f(x^{\ast}) = \frac{(2.399343)^2 \times 11.015885}{(1 + 11.015885)^2} = \frac{5.756847 \times 11.015885}{(12.015885)^2} = \frac{63.4137}{144.3815} = 0.43930.
$$

Thus

$$
C_{\max} = 0.43930 \times R = 0.43930 \times 8.314 = 3.6526\ \mathrm{J\,mol^{-1}\,K^{-1}}
$$

per mole of two-level systems.

**Projection (labeled).** If a Schottky anomaly is observed to peak at temperature $T_{\mathrm{peak}}$, the implied splitting is $\Delta = x^{\ast} k_B T_{\mathrm{peak}} = 2.3993\, k_B T_{\mathrm{peak}}$. For illustration, assuming $\Delta = k_B \times 1\ \mathrm{K}$ (i.e., $\Delta = 8.617 \times 10^{-5}\ \mathrm{eV}$), the peak would occur at $T_{\mathrm{peak}} = 1/2.3993 = 0.4168\ \mathrm{K}$ — inside the sub-1 K regime that [5] identifies as the operating range of quantum-technology refrigeration. This is a projection conditional on the assumed $\Delta$; no measurement is claimed.

### 4.2 Thermal and synthesis scales

**Input (from [6]):** synthesis at $1600\ ^\circ\mathrm{C}$ and $10^{-5}$ Torr.

- Temperature conversion: $T = 1600 + 273.15 = 1873.15\ \mathrm{K}$.
- Thermal energy: $k_B T = 8.617333 \times 10^{-5}\ \mathrm{eV\,K^{-1}} \times 1873.15\ \mathrm{K}$. Compute: $8.617333 \times 1.87315 = 16.1416$ (since $8.617333 \times 1.8 = 15.5112$ and $8.617333 \times 0.07315 = 0.63036$; sum $16.14156$). Hence $k_B T = 0.16142\ \mathrm{eV}$.
- Pressure conversion: $1\ \mathrm{Torr} = 133.322\ \mathrm{Pa}$, so $P = 10^{-5} \times 133.322 = 1.33322 \times 10^{-3}\ \mathrm{Pa}$.

**Input (from [5]):** operating regime "well below $1\ \mathrm{K}$." At $T = 1\ \mathrm{K}$:

$$
k_B T = 8.617333 \times 10^{-5}\ \mathrm{eV} = 1.380649 \times 10^{-23}\ \mathrm{J}.
$$

**Input (from [8]):** magnetoresistance $+90\%$ at $\mu_0 H = 16\ \mathrm{T}$, $T = 20\ \mathrm{K}$. The ratio implied is

$$
\frac{\rho_{xx}(16\ \mathrm{T},\,20\ \mathrm{K})}{\rho_{xx}(0)} = 1 + 0.90 = 1.90.
$$

The thermal scale at the measurement temperature: $k_B T = 8.617333 \times 10^{-5} \times 20 = 1.7235 \times 10^{-3}\ \mathrm{eV}$ at $T = 20\ \mathrm{K}$, and the nonlinearity threshold $T < 40\ \mathrm{K}$ corresponds to $k_B T < 8.617333 \times 10^{-5} \times 40 = 3.4469 \times 10^{-3}\ \mathrm{eV}$.

### 4.3 Re-entry classification of the bibliography

Applying the map $M = \sigma \circ \iota$ of Section 3.1:

| Setting | Source | Distinction $\mathcal{D}$ | Return map $\sigma$ |
|---|---|---|---|
| Andreev reflection at paired-FQH edges | [2] | normal/paired-medium interface | electron $\leftrightarrow$ hole |
| Adiabatic passage loop | [3] | drive-controlled level crossing | identity + geometric phase |
| Quasiparticle pseudopotential feedback | [4] | Laughlin state vs. its quasiparticles | interaction re-enters its own carriers |
| Phonon-blocked refrigeration | [5] | lattice vs. electronic heat channels | heat re-routed into junction |
| Moment suppression in pyrochlores | [6] | localized vs. itinerant magnetism | moment returned screened |
| Lambda/Schottky anomaly | [7] | ordered vs. nucleating phase | latent heat re-enters $C(T)$ |
| Hall scaling $\rho_{xy} \sim \rho_{xx}^{\beta}$ | [8] | longitudinal vs. transverse response | one coefficient re-expressed through the other |

The superconducting background of [1] and the formal vocabulary of [9] supply the substrate and the language respectively; [10] supplies the falsifiability template.

## 5. Results

All numbers below are quoted, converted, or derived in Section 4; nothing else is reported.

1. **Schottky peak position** (derived, Section 4.1): $x^{\ast} = \Delta/(k_B T_{\mathrm{peak}}) = 2.3993$, from solving $x \tanh(x/2) = 2$ by Newton iteration ($x_0 = 2.4 \to x_1 = 2.399356 \to x^{\ast} = 2.399343$).
2. **Schottky peak height** (derived): $C_{\max} = 0.43930\,R = 3.653\ \mathrm{J\,mol^{-1}\,K^{-1}}$ per mole of two-level systems.
3. **Splitting–peak relation** (projection, labeled): $\Delta = 2.3993\, k_B T_{\mathrm{peak}}$; under the stated assumption $\Delta = k_B \times 1\ \mathrm{K}$, $T_{\mathrm{peak}} = 0.4168\ \mathrm{K}$. Uncertainty in this projection is entirely that of the assumed $\Delta$; the conversion factor $2.3993$ itself carries only iteration truncation ($< 10^{-4}$ relative).
4. **Pyrochlore synthesis scale** (converted from [6]): $T = 1873.15\ \mathrm{K}$, $k_B T = 0.16142\ \mathrm{eV}$, $P = 1.33322 \times 10^{-3}\ \mathrm{Pa}$.
5. **Refrigeration regime scale** (converted from [5]'s "well below 1 K"): at $T = 1\ \mathrm{K}$, $k_B T = 8.617 \times 10^{-5}\ \mathrm{eV} = 1.3806 \times 10^{-23}\ \mathrm{J}$.
6. **LuNi$_2$B$_2$C magnetoresistance ratio** (quoted/converted from [8]): $\rho_{xx}(16\ \mathrm{T})/\rho_{xx}(0) = 1.90$ at $T = 20\ \mathrm{K}$; thermal scale $k_B T = 1.7235 \times 10^{-3}\ \mathrm{eV}$; nonlinearity window $T < 40\ \mathrm{K}$ corresponds to $k_B T < 3.4469 \times 10^{-3}\ \mathrm{eV}$.
7. **Classification** (qualitative): seven of the ten bibliography entries instantiate a re-entrant map of the form $M = \sigma \circ \iota$ with the assignments of Section 4.3.

## 6. Discussion

**Limitations.** The re-entry taxonomy is classificatory, not predictive: it organizes known behaviors but, as presented, generates no new numerical prediction beyond the standard Schottky fingerprint. The bibliography summaries are truncated for [2], [4], [5], [6], and [8]; in each case we used only what the supplied text states and explicitly avoided importing exponent values, moment magnitudes, or cooler performance figures from memory. The formal apparatus of [9] is used only at the level its summary supports (distinction as primitive; re-entry as a recognized configuration); the QNFO consolidation's 7 open problem categories and 4 extensions are not enumerated in the supplied text and are therefore not engaged here. Likewise, the ultrametric claim of [10] is used as a methodological template only; no $p$-adic analysis is performed in this paper.

**Failure modes.** The taxonomy fails if the assignments of Section 4.3 are not exclusive or principled — e.g., if any transport anomaly can be relabeled "re-entrant" post hoc, the concept explains nothing. A guard against this is the involution requirement $\sigma^2 = \mathbb{1}$: a candidate mode must exhibit a concrete return map, not merely a loop metaphor. It also fails if the Schottky/lambda identification of [7] does not extend to the two-level fingerprint computed here; the derivation of Section 4.1 is standard statistical mechanics, but its *application* to nucleation-and-growth latent heat in a specific material is an assumption of this paper.

**What would falsify the claims.** (i) A device setting in the bibliography's domain where the excitation return is demonstrably not describable by $M = \sigma \circ \iota$ with $\sigma^2 = \mathbb{1}$, yet is still naturally called re-entrant in the Laws-of-Form sense — this would show the formalization is too narrow. (ii) A measured heat-capacity anomaly attributed to a Schottky mechanism whose peak position violates $\Delta = 2.3993\, k_B T_{\mathrm{peak}}$ after independent determination of $\Delta$ — this would falsify the instrument, though not the taxonomy. (iii) Demonstration that the seven classifications of Section 4.3 reduce to two or fewer independent mechanisms with no shared structure — this would reduce re-entry to a synonym for "feedback" and strip it of content.

**Open questions.** Does the scaling exponent $\beta$ in $\rho_{xy} \sim \rho_{xx}^{\beta}$ of [8] admit a re-entrant (self-similar) interpretation, and is it universal across borocarbides? The summary truncates before giving $\beta$'s value or scope. Can adiabatic passage [3] be engineered to realize a literal Laws-of-Form re-entry — a drive whose path crosses its own distinction — and would the geometric phase then serve as the formal "mark"? Finally, does the trapped-ion ultrametric program [10], with its sixteen-record register, intersect the re-entry taxonomy: is ultrametric hierarchy itself a re-entrant nesting of distinctions? Both questions are stated as hypotheses, not results.

## 7. Conclusion

We have examined whether the Laws-of-Form notion of re-entry — the return of a form into its own distinction — organizes a real cross-section of solid-state quantum device physics. Using a fixed ten-entry bibliography and a strict evidence discipline modeled on an existing falsifiability register, we classified seven settings (Andreev reflection at paired-FQH edges, adiabatic passage, quasiparticle pseudopotential feedback, phonon-blocked refrigeration, moment suppression in pyro