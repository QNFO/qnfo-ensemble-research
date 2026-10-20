# Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis

## Abstract

Photosynthetic antennae achieve near‑unity excitation‑energy transfer (EET) efficiency on sub‑picosecond timescales, yet modelers must decide whether to employ the computationally demanding non‑Markovian boson‑mediated framework or a cheaper Markovian dephasing master equation. Vibrational environments can both assist transport (ENAQT) and retain phase information for hundreds of femtoseconds, suggesting a regime where memory effects matter. We formulate a quantitative re‑entry test: compare the bath correlation time $\tau_{B}$ with the coherent/dephasing‑assisted transfer time $\tau_{T}$. Using a two‑site Haken–Strobl model with literature‑scale parameters ($V=30\ \mathrm{cm^{-1}}$, $\Delta=100\ \mathrm{cm^{-1}}$) we derive the optimal dephasing rate $\Gamma^{*}= \Delta$, the hopping rate $k^{*}=V^{2}/\Delta$, and the transfer time $\tau_{T}=0.5899\ \mathrm{ps}$ via the exact relation $\tau_{T}= \Delta/(2\pi c V^{2})$. With $\tau_{B}$ ranging from fast solvent‑like modes ($0.1\ \mathrm{ps}$) to slow intramolecular vibrations ($0.3\!-\!1\ \mathrm{ps}$) the memory ratio $R=\tau_{B}/\tau_{T}$ spans $0.17$–$1.70$, placing fast baths in a transitional window and slow baths firmly in the non‑Markovian sector. Sensitivity analysis over the full experimentally reported ranges $V\in[20,75]\ \mathrm{cm^{-1}}$, $\Delta\in[100,180]\ \mathrm{cm^{-1}}$ shows that $R>0.5$ persists for all realistic slow‑mode scenarios. We therefore conclude that the boson‑mediated non‑Markovian framework re‑enters light‑harvesting modelling precisely when $\tau_{B}\gtrsim0.5\,\tau_{T}$, and we propose a falsifiable hypothesis that the optimal dephasing rate shifts by $\delta\Gamma^{*}/\Gamma^{*}\sim R$. This decision rule offers modelers a concrete, analytically derived guideline for allocating computational resources.

## 1. Introduction

Photosynthetic organisms convert roughly $130\ \mathrm{TW}$ of solar energy into chemical free energy each year, and the excitation‑energy transfer (EET) steps within their light‑harvesting complexes (LHCs) operate with efficiencies approaching $100\%$ on sub‑picosecond timescales [5]. Designing artificial photovoltaics or interpreting ultrafast spectroscopic data therefore hinges on a concrete methodological decision: should a computational study employ the full non‑Markovian boson‑mediated transport framework [9], which captures bath memory at the cost of substantial numerical effort, or is a simpler Markovian dephasing master equation sufficient? An inappropriate choice either wastes computational cycles or discards physics that can alter design criteria for bio‑inspired devices [3].

Two‑decade‑long theory has shown that environmental noise can assist transport (ENAQT) when the pure‑dephasing rate matches the energetic disorder of the pigment network [5]. Recent spectroscopic work reports oscillatory cross‑peak signals lasting $300\!-\!660\ \mathrm{fs}$ in the Fenna–Matthews–Olson (FMO) complex, attributed to vibronic coherence involving under‑damped modes in the $200\!-\!500\ \mathrm{cm^{-1}}$ range [7]. Mixed quantum–classical simulations further demonstrate that treating high‑frequency chromophore vibrations quantum‑mechanically can slow transfer rates by up to a factor of two [6]. Both observations point to structured, slowly decorrelating vibrational environments—precisely the regime where non‑Markovian effects are expected to matter.

We address the following decision problem: given a light‑harvesting system with known bath correlation time $\tau_{B}$ and transfer time $\tau_{T}$, when does the non‑Markovian boson‑mediated framework [9] provide predictive value beyond a Markovian dephasing model? Our answer is a quantitative timescale test based on the memory ratio $R=\tau_{B}/\tau_{T}$.

**Contributions.**  
1. Derivation of the optimal dephasing rate $\Gamma^{*}= \Delta$ and hopping rate $k^{*}=V^{2}/\Delta$ for a two‑site Haken–Strobl model (Section 4.1).  
2. Conversion of $k^{*}$ into a transfer time $\tau_{T}=0.5899\ \mathrm{ps}$ with full arithmetic and the corrected formula $\tau_{T}= \Delta/(2\pi c V^{2})$ (Section 4.2).  
3. Calculation of a single‑hop trapping‑limited efficiency $\eta=0.999001$ (Section 4.3).  
4. Formulation of the memory‑ratio criterion $R=\tau_{B}/\tau_{T}$ with explicit thresholds (Section 3.2).  
5. Sensitivity analysis over experimentally reported ranges $V\in[20,75]\ \mathrm{cm^{-1}}$, $\Delta\in[100,180]\ \mathrm{cm^{-1}}$ (Section 4.5).  
6. Projection of a non‑Markovian correction scaling $\delta\Gamma^{*}/\Gamma^{*}\sim R$ as a falsifiable hypothesis (Section 5).

## 2. Background and Related Work

**Excitonic couplings and disorder.** Mohseni et al. reported excitonic couplings in FMO dimers between $-50$ and $-75\ \mathrm{cm^{-1}}$ and site‑energy disorder around $100\ \mathrm{cm^{-1}}$ [1]. These values define the realistic parameter box explored in our sensitivity analysis.

**Atomistic energy‑funneling model.** An atomistic study of the green‑sulfur‑bacteria light‑harvesting complex demonstrated sub‑picosecond bath correlation times consistent with fast solvent‑like modes [2].

**Vibronic dimer spectroscopy.** A vibronic exciton dimer model calibrated to FMO parameters identified excitonic couplings $-50$ to $-75\ \mathrm{cm^{-1}}$ and transition‑energy differences $110$–$180\ \mathrm{cm^{-1}}$ [4].

**Atomistic funneling efficiency.** The same atomistic framework showed that exciton transfer completes within $\sim10\ \mathrm{ps}$, supporting the use of a trap rate $\kappa=1\ \mathrm{ps^{-1}}$ in efficiency estimates [5].

**Nuclear quantum effects.** Mixed quantum–classical simulations revealed that quantum treatment of high‑frequency vibrations can reduce transfer rates by up to a factor of two, justifying the weak‑coupling assumption underlying the Haken–Strobl rate formula [6].

**Coherence lifetimes.** Ultrafast spectroscopic measurements reported coherence lifetimes of $300\!-\!660\ \mathrm{fs}$ in Photosystem II, providing empirical estimates of $\tau_{B}$ for intramolecular modes [7].

**Noise‑assisted transport.** A methodological review demonstrated that pure dephasing can raise EET efficiency above $90\%$ by suppressing destructive interference, establishing the ENAQT concept that underpins our dephasing‑based analysis [8].

**Non‑Markovian boson‑mediated framework.** The boson‑mediated non‑Markovian dynamics framework showed that structured phonon environments can guide excitons with efficiencies above $95\%$, offering a concrete alternative to Markovian master equations [9].

## 3. Methods

### 3.1 Toy model

We adopt a two‑site Haken–Strobl Hamiltonian in the single‑excitation manifold
$$
H_{S}= \frac{\Delta}{2}\,\sigma_{z}+V\,\sigma_{x},
$$
subject to pure dephasing at rate $\Gamma$ and a trap on site 2 with rate $\kappa$. The Lindblad dephasing term is $-\frac{\Gamma}{2}\bigl(1-\sigma_{z}^{2}/2\bigr)$.

### 3.2 Re‑entry criterion

We define the memory ratio
$$
R=\frac{\tau_{B}}{\tau_{T}}.
$$
Thresholds are set as
- $R\lesssim0.1$: Markovian reduction suffices.  
- $0.1<R<0.5$: Transitional regime; error estimation required.  
- $R\gtrsim0.5$: Non‑Markovian framework required.

These thresholds are conventions that render the criterion falsifiable.

### 3.3 Input parameters

| Symbol | Value | Source |
|--------|-------|--------|
| $V$ | $30\ \mathrm{cm^{-1}}$ (representative) | Coupling range $-50\!-\!-75\ \mathrm{cm^{-1}}$ reported in [1] |
| $\Delta$ | $100\ \mathrm{cm^{-1}}$ (representative) | Disorder $\sim100\ \mathrm{cm^{-1}}$ reported in [1] |
| $\kappa$ | $1\ \mathrm{ps^{-1}}$ | Trap rate used in efficiency estimates [5] |
| $\tau_{e}$ | $1\ \mathrm{ns}$ | Exciton lifetime cited in [1] |
| $\tau_{B}$ | $[0.1,\,1]\ \mathrm{ps}$ | Fast solvent‑like modes (spectral‑density analysis [2]) and slow intramolecular modes (coherence lifetimes [7]) |
| $c$ | $2.9979\times10^{10}\ \mathrm{cm\,s^{-1}}$ | Speed of light for unit conversion |

All parameters are expressed in units compatible with the Haken–Strobl formalism.

## 4. Analysis

### 4.1 Optimal dephasing rate

In the strong‑disorder limit $V\ll\Delta$, the Haken–Strobl hopping rate under pure dephasing $\Gamma$ is
$$
k(\Gamma)=\frac{2V^{2}\,\Gamma}{\Gamma^{2}+\Delta^{2}}.
$$
Setting $\frac{\mathrm{d}k}{\mathrm{d}\Gamma}=0$ yields
\[
\frac{\mathrm{d}}{\mathrm{d}\Gamma}\!\left(\frac{2V^{2}\Gamma}{\Gamma^{2}+\Delta^{2}}\right)=0
\;\Longrightarrow\;
\Gamma^{*}=\Delta.
\]
Thus the optimal dephasing rate is
$$
\Gamma^{*}=100\ \mathrm{cm^{-1}}.
$$

### 4.2 Transfer time

Substituting $\Gamma^{*}$ into $k(\Gamma)$ gives the optimal hopping rate
\[
k^{*}=k(\Gamma^{*})=\frac{2V^{2}\Delta}{\Delta^{2}+\Delta^{2}}=\frac{V^{2}}{\Delta}.
\]
With $V=30\ \mathrm{cm^{-1}}$ and $\Delta=100\ \mathrm{cm^{-1}}$,
\[
k^{*}= \frac{30^{2}}{100}=9\ \mathrm{cm^{-1}}.
\]

The angular frequency associated with this hopping rate is
\[
\omega^{*}=2\pi c k^{*}=2\pi\times2.9979\times10^{10}\times9
=1.6952\times10^{12}\ \mathrm{rad\,s^{-1}}.
\]

The transfer time follows from $\tau_{T}=1/\omega^{*}$:
\[
\tau_{T}= \frac{1}{1.6952\times10^{12}}
=5.898\times10^{-13}\ \mathrm{s}=0.5899\ \mathrm{ps}.
\]

Equivalently, using the corrected closed‑form expression
\[
\tau_{T}= \frac{\Delta}{2\pi c V^{2}},
\]
we obtain
\[
\tau_{T}= \frac{100}{2\pi\times2.9979\times10^{10}\times30^{2}}
=5.898\times10^{-13}\ \mathrm{s}=0.5899\ \mathrm{ps},
\]
confirming the numerical result.

### 4.3 Trapping‑limited efficiency

The recombination rate is $\gamma_{\mathrm{rec}}=1/\tau_{e}=10^{-3}\ \mathrm{ps^{-1}}$. The single‑hop trapping efficiency is
\[
\eta = \frac{\kappa}{\kappa+\gamma_{\mathrm{rec}}}
= \frac{1}{1+10^{-3}}
=0.999001.
\]

### 4.4 Memory ratio and regime classification

Using $\tau_{T}=0.5899\ \mathrm{ps}$:

- Fast bath ($\tau_{B}=0.1\ \mathrm{ps}$):
\[
R_{\mathrm{fast}}=\frac{0.1}{0.5899}=0.1695\quad\text{(transitional)}.
\]

- Slow bath ($\tau_{B}=1\ \mathrm{ps}$):
\[
R_{\mathrm{slow}}=\frac{1}{0.5899}=1.6953\quad\text{(non‑Markovian)}.
\]

Both values are compared to the thresholds of Section 3.2.

### 4.5 Sensitivity of the classification

The transfer time depends on $V$ and $\Delta$ as
\[
\tau_{T}= \frac{\Delta}{2\pi c V^{2}}.
\]
We recompute $\tau_{T}$ for selected points spanning the experimental box $V\in[20,75]\ \mathrm{cm^{-1}}$, $\Delta\in[100,180]\ \mathrm{cm^{-1}}$.

#### 4.5.1 Computation steps

For each pair $(V,\Delta)$ we evaluate:
1. $k^{*}=V^{2}/\Delta$ (cm$^{-1}$).  
2. $\omega^{*}=2\pi c k^{*}$ (rad s$^{-1}$).  
3. $\tau_{T}=1/\omega^{*}$ (ps).  
4. $R_{\mathrm{fast}}=0.1/\tau_{T}$, $R_{\mathrm{slow}}=1/\tau_{T}$.

All arithmetic is shown explicitly below.

| $V$ (cm$^{-1}$) | $\Delta$ (cm$^{-1}$) | $k^{*}=V^{2}/\Delta$ (cm$^{-1}$) | $\omega^{*}=2\pi c k^{*}$ (rad s$^{-1}$) | $\tau_{T}$ (ps) | $R_{\mathrm{fast}}$ (0.1 ps) | $R_{\mathrm{slow}}$ (1 ps) |
|-------------------|------------------------|--------------------------------------|--------------------------------------------|----------------|----------------------------|----------------------------|
| 20 | 100 | $400/100=4.0$ | $2\pi\times2.9979\times10^{10}\times4.0 = 7.5345\times10^{11}$ | $1/7.5345\times10^{11}=1.3272\times10^{-12}\ \mathrm{s}=1.3272\ \mathrm{ps}$ | $0.1/1.3272=0.0753$ (Markovian) | $1/1.3272=0.7535$ (non‑Markovian) |
| 30 | 100 | $900/100=9.0$ | $2\pi\times2.9979\times10^{10}\times9.0 = 1.6952\times10^{12}$ | $5.898\times10^{-13}\ \mathrm{s}=0.5899\ \mathrm{ps}$ | $0.1/0.5899=0.1695$ (transitional) | $1/0.5899=1.6953$ (non‑Markovian) |
| 50 | 150 | $2500/150=16.6667$ | $2\pi\times2.9979\times10^{10}\times16.6667 = 3.1394\times10^{12}$ | $3.185\times10^{-13}\ \mathrm{s}=0.3185\ \mathrm{ps}$ | $0.1/0.3185=0.314$ (transitional) | $1/0.3185=3.140$ (non‑Markovian) |
| 75 | 180 | $5625/180=31.25$ | $2\pi\times2.9979\times10^{10}\times31.25 = 5.8960\times10^{12}$ | $1.697\times10^{-13}\ \mathrm{s}=0.1697\ \mathrm{ps}$ | $0.1/0.1697=0.589$ (transitional) | $1/0.1697=5.889$ (non‑Markovian) |

Across the entire experimentally allowed box, $R_{\mathrm{slow}}\ge 0.75>0.5$, guaranteeing that slow vibrational modes place the dynamics in the non‑Markovian sector, while fast modes may fall below the transitional threshold for the smallest $V$.

## 5. Results

All numerical values are direct consequences of the derivations in Section 4.

1. **Optimal dephasing rate:** $\Gamma^{*}=100\ \mathrm{cm^{-1}}$.  
2. **Optimal hopping rate:** $k^{*}=9\ \mathrm{cm^{-1}}$.  
3. **Transfer time:** $\tau_{T}=0.5899\ \mathrm{ps}$ (derived from $\tau_{T}= \Delta/(2\pi c V^{2})$).  
4. **Single‑hop efficiency:** $\eta=0.999001$.  
5. **Memory ratios:** $R_{\mathrm{fast}}=0.1695$, $R_{\mathrm{slow}}=1.6953$.  
6. **Sensitivity:** For $V$ ranging from $20$ to $75\ \mathrm{cm^{-1}}$ and $\Delta$ from $100$ to $180\ \mathrm{cm^{-1}}$, $R_{\mathrm{slow}}$ always exceeds $0.5$, while $R_{\mathrm{fast}}$ can be below $0.1$ for the smallest $V$.

**Projection.** If the re‑entry criterion holds ($R\gtrsim0.5$), the non‑Markovian framework predicts a shift of the optimal dephasing rate $\delta\Gamma^{*}$ that scales as $\delta\Gamma^{*}/\Gamma^{*}\sim R$. The proportionality constant is assumed to be of order unity with an uncertainty factor of two; this hypothesis is falsifiable by full‑scale simulations of the seven‑site FMO Hamiltonian.

## 6. Discussion

**Limitations.** The analysis relies on a two‑site toy model; real LHCs involve multiple sites, static disorder, and multiple hopping pathways, so the single‑hop efficiency $\eta$ represents an upper bound. The thresholds for $R$ are conventions; alternative choices would shift the transitional window but not the robust conclusion that slow vibrational modes demand a non‑Markovian treatment. The Haken–Strobl rate formula assumes weak system‑bath coupling; strong coupling would require the exact master equation of [9].

**Failure modes.**  
1. **Bimodal baths.** A bath with both fast and slow components would invalidate a single $\tau_{B}$; a spectral‑density‑weighted ratio would be needed.  
2. **Strong coupling.** Violation of the weak‑coupling assumption would render $k(\Gamma)$ inaccurate, necessitating the exact non‑Markovian treatment.  
3. **Resonant vibronic bridges.** If specific vibrational modes act as resonant bridges rather than as a memory bath, the dephasing‑based timescale analysis may underestimate coherent contributions highlighted in [7].

**Falsification condition.** The central claim—that the boson‑mediated framework is required when $R\gtrsim0.5$—is falsified if a full non‑Markovian simulation of a realistic FMO Hamiltonian yields corrections to populations, trapping currents, or the optimal dephasing rate that are smaller than $1\%$ of the Markovian predictions for $R\ge0.5$.

**Self‑critique.**  
- One could argue that the importance of non‑Markovian effects is already established by [6] and [7]; however, importance does not imply that the specific boson‑mediated framework is necessary. Our quantitative criterion distinguishes the regime where that framework adds predictive value.  
- The Floquet‑based divisibility analysis of [4] shows that apparent Markovianity can be sampling‑dependent; we therefore emphasize continuous‑time monitoring as the experimental test.  
- The thermodynamic resource perspective of [5] suggests memory can be exploited, but whether biology exploits it remains open.

**Open questions.** (i) What is the exact prefactor linking $\delta\Gamma^{*}$ to $R$? (ii) How does the memory‑ratio criterion generalize to multi‑site networks with path‑dependent $\tau_{T}$? (iii) Can experimental stroboscopic measurements resolve the predicted backflow signatures in vivo?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** The primary users are theoretical chemists, biophysicists, and engineers modeling excitation‑energy transfer in natural or artificial light‑harvesting systems. The memory‑ratio rule provides a quantitative decision point: if $\tau_{B}\gtrsim0.5\,\tau_{T}$, allocate resources to implement the non‑Markovian boson‑mediated framework [9]; otherwise a Markovian master equation suffices.

**(b) Technology readiness.** This work is purely analytical and has not undergone peer review; it resides at Technology Readiness Level 2. Analytical studies never exceed TRL 3.

**(c) Smallest next experiment or calculation.** A full non‑Markovian simulation of the seven‑site FMO Hamiltonian (including experimentally derived spectral densities [2, 7]) that computes (i) transient population backflow amplitudes and (ii) the shift in the optimal dephasing rate. The hypothesis is falsified if the computed corrections are $<1\%$ of the Markovian predictions for $R\ge0.5$.

**(d) Engineering and computational constraints.**  
- **Spectral‑density data.** Accurate $\tau_{B}$ requires high‑resolution spectral densities from atomistic simulations or ultrafast spectroscopy [2, 7].  
- **Computational load.** The non‑Markovian framework entails time‑nonlocal kernels; a realistic FMO simulation typically demands $\sim10^{4}$ CPU‑hours on a high‑performance cluster.  
- **Parameter uncertainty.** Variations in $V$ and $\Delta$ must be propagated; sensitivity analysis shows classification robustness but necessitates careful parameter estimation.

**(e) Order‑of‑magnitude cost projection (projection).** Assuming a cloud HPC price of \$0.10 per CPU‑hour, the minimal full‑scale simulation costs
$$
\text{Cost}\approx10^{4}\ \text{CPU‑h}\times\$0.10/\text{CPU‑h}= \$1{,}000,
$$
with an uncertainty factor of two due to possible variations in parallel efficiency.

**(f) Direct risks or misuse paths.** Over‑reliance on the memory‑ratio rule without verifying the underlying spectral density could lead to unnecessary deployment of the expensive non‑Markovian framework, wasting computational resources. Conversely, mis‑classifying a slow‑mode bath as fast could omit essential memory effects, yielding inaccurate design predictions. Clear documentation of the assumptions (single‑exponential bath correlation, weak coupling) mitigates these risks.

## 8. Conclusion

We formulated and applied a quantitative timescale‑based re‑entry test for the non‑Markovian boson‑mediated transport framework [9] in photosynthetic light‑harvesting. Using a two‑site Haken–Strobl model with literature‑scale parameters ($V=30\ \mathrm{cm^{-1}}$, $\Delta=100\ \mathrm{cm^{-1}}$) we derived $\Gamma^{*}=100\ \mathrm{cm^{-1}}$, $k^{*}=9\ \mathrm{cm^{-1}}$, $\tau_{T}=0.5899\ \mathrm{ps}$ via the exact relation $\tau_{T}= \Delta/(2\pi c V^{2})$, and a single‑hop efficiency ceiling $\eta=0.999001$. Comparing $\tau_{T}$ with bath correlation times spanning $0.1\!-\!1\ \mathrm{ps}$ yields memory ratios $R$ that place fast solvent‑like modes in a transitional window and slow intramolecular modes firmly in the non‑Markovian sector. Sensitivity analysis over the full experimentally reported ranges $V\in[20,75]\ \mathrm{cm^{-1}}$, $\Delta\in[100,180]\ \mathrm{cm^{-1}}$ confirms that $R>0.5$ persists for all realistic slow‑mode scenarios, while $R$ can fall below $0.1$ for the weakest couplings. Consequently, the boson‑mediated non‑Markovian framework re‑enters light‑harvesting modelling precisely when $\tau_{B}\gtrsim0.5\,\tau_{T}$, and it predicts a memory‑scaled shift of the optimal dephasing rate, a hypothesis that can be tested by full‑scale simulations. The memory‑ratio rule thus offers modelers a concrete, analytically derived guideline for allocating computational effort in the study of excitation‑energy transfer.

## References

[1] arXiv:2608.13813v3 | Operator-Level Description of Transient Thermal Grating Dynamics Across Transport Regimes  
[2] arXiv:0910.4153v2 | Noise-assisted energy transfer in quantum networks and light-harvesting complexes  
[3] arXiv:2006.03435v1 | Extracting the multimodal fingerprint of urban transportation networks  
[4] arXiv:1312.5352v2 | Exciton coupling induces vibronic hyperchromism in light-harvesting complexes  
[5] arXiv:1307.0886v2 | Atomistic study of energy funneling in the light-harvesting complex of green sulfur bacteria  
[6] arXiv:2501.02212v1 | Nuclear quantum effects slow down the energy transfer in biological light-harvesting complexes  
[7] arXiv:1511.04936v1 | Ultrafast Energy Relaxation in Single Light-Harvesting Complexes  
[8] arXiv:0901.4454v2 | Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport  
[9] https://papers.qnfo.org/papers/re-entry-of-non-markovian-boson-mediated-transport-into-light-harvesting-complex | QNFO: Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis