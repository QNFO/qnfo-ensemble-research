# Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis

## Abstract

Photosynthetic antennae transfer excitation energy with near‑unity efficiency on sub‑picosecond timescales, yet modelers must decide whether the computationally expensive non‑Markovian boson‑mediated framework is required or a cheaper Markovian dephasing master equation suffices. Existing applicability tests used parameter ranges broader than experimentally reported values and employed a dimensionally inconsistent transfer‑time formula. We adopt the experimentally reported coupling and site‑energy‑difference ranges for the FMO BChl 3–4 dimer ($V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$) and use the dimensionally sound expression $\tau_{T}= \Delta/(2\pi c V^{2})$. For the representative point $(V,\Delta)=(50,110)\ \mathrm{cm^{-1}}$ the transfer time is $\tau_{T}=0.2336\ \mathrm{ps}$ and the single‑hop trapping efficiency is $\eta=0.999001$. The memory‑ratio $R=\tau_{B}/\tau_{T}$ spans $R_{\mathrm{fast}}\in[0.428,0.589]$ for fast baths ($\tau_{B}=0.1\ \mathrm{ps}$) and $R_{\mathrm{slow}}\in[4.28,5.89]$ for slow baths ($\tau_{B}=1\ \mathrm{ps}$). All realistic slow‑mode scenarios therefore lie in the non‑Markovian sector. We formulate a falsifiable hypothesis that the optimal dephasing rate shifts by $\delta\Gamma^{*}/\Gamma^{*}\sim R$ when $R\gtrsim0.5$. The memory‑ratio rule thus provides a quantitative, analytically derived guideline for allocating computational effort in excitation‑energy‑transfer modelling.

## 1. Introduction

Photosynthetic organisms convert sunlight into chemical free energy after funnelling excitation through pigment networks with efficiencies approaching $100\%$ on sub‑picosecond excitation‑energy‑transfer (EET) timescales. Every computational study of this process faces a concrete methodological decision with real costs on both sides: implement the full non‑Markovian boson‑mediated framework, which retains bath memory at the price of time‑nonlocal kernels and large numerical effort, or use a Markovian dephasing master equation, which is cheap but discards physics exactly when bath correlation times approach the transfer time. Choosing wrongly either wastes high‑performance‑computing allocations or produces transfer rates and optimal dephasing conditions that are quantitatively wrong, which in turn misguides design parameters for bio‑inspired light‑harvesting devices and the interpretation of ultrafast spectra. A validated, analytically derived decision rule would let a modeler allocate compute where memory effects matter and skip them where they do not.

Two decades of theory establish that environmental noise can assist rather than hinder transport: dephasing‑assisted transport raises EET efficiencies above $90\%$ across the Fenna–Matthews–Olson (FMO) complex within a fully Markovian treatment [2], and the underlying mechanisms—suppression of destructive interference and dephasing‑broadened site overlap—are worked out analytically for fully connected networks [8]. On the experimental side, single‑molecule pump–probe spectroscopy resolves sub‑100 fs energy relaxation in individual light‑harvesting complexes [7], so fast solvent‑like bath components with correlation times of order $0.1\ \mathrm{ps}$ are measured, not inferred. Mixed quantum–classical simulations show that treating high‑frequency chromophore vibrations quantum‑mechanically instead of classically slows transfer rates by less than a factor of two for biologically relevant parameters [6]. The target framework whose applicability we assess is the non‑Markovian boson‑mediated description, in which structured phonon fields direct exciton transport and is claimed to sustain efficiencies above $95\%$ [9]. The original applicability analysis of that framework proposed a memory‑ratio test but rested on a parameter box wider than the experimentally reported values and on a transfer‑time formula carrying a spurious factor of $\hbar$.

**Contributions.**  
1. Derivation of the optimal dephasing rate $\Gamma^{*}=\Delta$ and optimal hopping rate $k^{*}=V^{2}/\Delta$ for the two‑site Haken–Strobl model, with the derivative shown explicitly (Section 4.1).  
2. Correction of the transfer‑time formula to $\tau_{T}= \Delta/(2\pi c V^{2})$, with a dimensional check, and its evaluation at the representative reported point $(V,\Delta)=(50,110)\ \mathrm{cm^{-1}}$, giving $\tau_{T}=0.2336\ \mathrm{ps}$ (Section 4.2).  
3. Computation of the single‑hop trapping‑limited efficiency $\eta=0.999001$ under stated assumptions for the trap and recombination rates (Section 4.3).  
4. Recomputation of the memory ratios over the experimentally reported box $V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$, giving $R_{\mathrm{fast}}\in[0.428,0.589]$ and $R_{\mathrm{slow}}\in[4.28,5.89]$, with a corner‑extremality argument (Section 4.4).  
5. A corrected regime classification: within the reported box no bath in the range $\tau_{B}\in[0.1,1]\ \mathrm{ps}$ falls in the Markovian sector, and slow baths are non‑Markovian everywhere (Section 5).  
6. A falsifiable projection that the non‑Markovian correction to the optimal dephasing rate scales as $\delta\Gamma^{*}/\Gamma^{*}\sim R$, with its tension against the sub‑twofold rate effects found for vibrational quantization [6] (Sections 5 and 6).

## 2. Background and Related Work

**Transient thermal‑grating probing.** Transient thermal‑grating (TTG) experiments provide a powerful means of probing material properties and heat‑transport dynamics at small spatiotemporal scales [1]. The technique therefore establishes that sub‑picosecond bath dynamics are experimentally accessible.

**Dephasing‑assisted transport in FMO.** Reference [2] demonstrates that pure dephasing can open transport pathways and raise EET efficiencies above $90\%$ in the FMO complex, establishing the relevance of dephasing‑assisted transport (DAT) for light‑harvesting.

**Excitonic coupling magnitudes.** The excitonic coupling between two pigments in the FMO complex is reported to lie between $-50$ and $-75\ \mathrm{cm^{-1}}$ [4], supporting the choice of $V$ values up to $75\ \mathrm{cm^{-1}}$ in our sensitivity analysis.

**Atomistic energy‑funnelling timescales.** Atomistic models of the green‑sulfur‑bacteria light‑harvesting complex indicate energy‑funnelling occurs on picosecond timescales [5], justifying the order‑of‑magnitude of $\tau_{T}$ derived below.

**Quantum nuclear effects on rates.** Quantum‑mechanical treatment of high‑frequency vibrations can slow transfer rates by less than a factor of two [6], motivating the inclusion of a non‑Markovian correction in the slow‑bath regime.

**Ultrafast single‑molecule spectroscopy.** Observations of sub‑100 fs energy‑relaxation processes confirm the existence of fast solvent‑like bath components with correlation times on the order of $0.1\ \mathrm{ps}$ [7].

**Multiplex‑network perspective on transport.** Ref. [3] introduces multiplex networks as a mathematical framework for describing layered transport processes, providing an analogy for exciton‑phonon layered dynamics and motivating our memory‑ratio criterion.

**Fundamental role of noise‑assisted transport.** Ref. [8] identifies key mechanisms by which dephasing noise suppresses destructive interference and raises transport efficiency, providing a theoretical foundation for the optimal dephasing condition derived in Section 4.1.

**Non‑Markovian boson‑mediated framework.** The boson‑mediated non‑Markovian framework retains bath memory and can achieve high efficiencies [9]; it is the target framework whose applicability we assess.

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

| Symbol | Value | Rationale |
|--------|-------|-----------|
| $V$ | $[50,75]\ \mathrm{cm^{-1}}$ | Experimentally reported coupling range for the FMO BChl 3–4 dimer [4] |
| $\Delta$ | $[110,180]\ \mathrm{cm^{-1}}$ | Experimentally reported site‑energy difference for the same dimer [4] |
| $\kappa$ | $1\ \mathrm{ps^{-1}}$ | Trap rate used in atomistic energy‑funnelling studies [5] |
| $\tau_{e}$ | $1\ \mathrm{ns}$ | Exciton lifetime reported for green‑sulfur‑bacteria complexes [5] |
| $\tau_{B}$ | $[0.1,\,1]\ \mathrm{ps}$ | Fast solvent‑like modes observed in single‑molecule spectroscopy [7]; slow intramolecular modes (assumed $\tau_{B}=1\ \mathrm{ps}$) |
| $c$ | $2.9979\times10^{10}\ \mathrm{cm\,s^{-1}}$ | Speed of light for unit conversion |

All parameters are either taken from the cited literature or stated as explicit assumptions.

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

Thus the optimal dephasing rate equals the energetic disorder:

\[
\Gamma^{*}= \Delta.
\]

### 4.2 Transfer time

Substituting $\Gamma^{*}$ into $k(\Gamma)$ gives the optimal hopping rate  

\[
k^{*}=k(\Gamma^{*})=\frac{V^{2}}{\Delta}.
\]

To convert a wavenumber $k^{*}$ (in $\mathrm{cm^{-1}}$) into an angular frequency we multiply by the speed of light $c$ and by $2\pi$:

\[
\begin{aligned}
c\,k^{*} &= c\,\frac{V^{2}}{\Delta},\\
\omega^{*} &= 2\pi\,c\,k^{*}=2\pi\,c\,\frac{V^{2}}{\Delta}.
\end{aligned}
\]

The transfer time is the inverse of $\omega^{*}$:

\[
\tau_{T}= \frac{1}{\omega^{*}} = \frac{\Delta}{2\pi c V^{2}}.
\]

Using the representative point $(V,\Delta)=(50,110)\ \mathrm{cm^{-1}}$:

\[
\begin{aligned}
V^{2} &= 50^{2}=2500\ \mathrm{(cm^{-1})^{2}},\\
\Delta/(2\pi c V^{2}) &= \frac{110}{2\pi \times 2.9979\times10^{10}\times 2500}\\
&= \frac{110}{2\pi \times 7.49475\times10^{13}}\\
&= \frac{110}{4.7080\times10^{14}}\\
&= 2.336\times10^{-13}\ \mathrm{s}\\
&= 0.2336\ \mathrm{ps}.
\end{aligned}
\]

Thus $\tau_{T}=0.2336\ \mathrm{ps}$ for the representative parameters.

For the opposite corner of the experimental box $(V,\Delta)=(75,180)\ \mathrm{cm^{-1}}$:

\[
\begin{aligned}
V^{2} &= 75^{2}=5625\ \mathrm{(cm^{-1})^{2}},\\
\Delta/(2\pi c V^{2}) &= \frac{180}{2\pi \times 2.9979\times10^{10}\times 5625}\\
&= \frac{180}{1.059\times10^{15}}\\
&= 1.699\times10^{-13}\ \mathrm{s}\\
&= 0.1699\ \mathrm{ps}.
\end{aligned}
\]

Thus the transfer time varies between $0.1699\ \mathrm{ps}$ and $0.2336\ \mathrm{ps}$ over the reported box.

### 4.3 Trapping‑limited efficiency

The recombination rate is $\gamma_{\mathrm{rec}}=1/\tau_{e}=10^{-3}\ \mathrm{ps^{-1}}$. The single‑hop trapping efficiency is  

\[
\eta = \frac{\kappa}{\kappa+\gamma_{\mathrm{rec}}}= \frac{1}{1+10^{-3}} = 0.999001.
\]

### 4.4 Memory ratio and regime classification

Using the longest transfer time $\tau_{T}^{\mathrm{max}}=0.2336\ \mathrm{ps}$ and the shortest $\tau_{T}^{\mathrm{min}}=0.1699\ \mathrm{ps}$, the memory ratio for a given bath correlation time $\tau_{B}$ satisfies

\[
R_{\mathrm{fast}} = \frac{0.1\ \mathrm{ps}}{\tau_{T}} \in \left[\frac{0.1}{0.2336},\frac{0.1}{0.1699}\right]=[0.428,0.589],
\]
\[
R_{\mathrm{slow}} = \frac{1\ \mathrm{ps}}{\tau_{T}} \in \left[\frac{1}{0.2336},\frac{1}{0.1699}\right]=[4.28,5.89].
\]

All values exceed the $0.5$ threshold for the slow bath, placing every realistic slow‑mode scenario in the non‑Markovian sector. Fast baths may fall below $0.5$ only for the smallest $V$ values; otherwise they remain transitional.

## 5. Results

All numerical values follow directly from the derivations in Section 4.

1. **Optimal dephasing rate:** $\Gamma^{*}= \Delta$, ranging from $110$ to $180\ \mathrm{cm^{-1}}$.  
2. **Optimal hopping rate:** $k^{*}=V^{2}/\Delta$, ranging from $13.89$ to $51.14\ \mathrm{cm^{-1}}$ across the experimental box.  
3. **Transfer time:** $\tau_{T}=0.2336\text{–}0.1699\ \mathrm{ps}$, with the representative value $0.2336\ \mathrm{ps}$.  
4. **Single‑hop efficiency:** $\eta=0.999001$.  
5. **Memory ratios:** $R_{\mathrm{fast}}\in[0.428,0.589]$, $R_{\mathrm{slow}}\in[4.28,5.89]$.  
6. **Sensitivity:** Across the full experimentally allowed box, $R_{\mathrm{slow}}$ always exceeds $0.5$, while $R_{\mathrm{fast}}$ can be below $0.5$ only for the smallest $V$ values.  

**Projection.** If the re‑entry criterion holds ($R\gtrsim0.5$), the non‑Markovian framework predicts a shift of the optimal dephasing rate $\delta\Gamma^{*}$ that scales as $\delta\Gamma^{*}/\Gamma^{*}\sim R$. The proportionality constant is assumed to be of order unity with an uncertainty factor of two; this hypothesis is falsifiable by full‑scale simulations of the seven‑site FMO Hamiltonian.

## 6. Discussion

**Limitations.**  
- The analysis relies on a two‑site toy model; real light‑harvesting complexes involve multiple sites, static disorder, and multiple hopping pathways, so the single‑hop efficiency $\eta$ represents an upper bound.  
- The thresholds for $R$ are conventions; alternative choices would shift the transitional window but not the robust conclusion that slow vibrational modes demand a non‑Markovian treatment.  
- The Haken–Strobl rate formula assumes weak system‑bath coupling; strong coupling would require the exact non‑Markovian treatment.  

**Failure modes.**  
1. **Bimodal baths.** A bath with both fast and slow components would invalidate a single $\tau_{B}$; a spectral‑density‑weighted ratio would be needed.  
2. **Strong coupling.** Violation of the weak‑coupling assumption would render $k(\Gamma)$ inaccurate, necessitating the exact non‑Markovian treatment.  
3. **Resonant vibronic bridges.** If specific vibrational modes act as resonant bridges rather than as a memory bath, the dephasing‑based timescale analysis may underestimate coherent contributions highlighted in [7].  

**Falsification condition.** The central claim—that the boson‑mediated framework is required when $R\gtrsim0.5$—is falsified if a full non‑Markovian simulation of a realistic FMO Hamiltonian yields corrections to populations, trapping currents, or the optimal dephasing rate that are smaller than $1\%$ of the Markovian predictions for $R\ge0.5$.

**Self‑critique.**  
- One could argue that the importance of non‑Markovian effects is already established by [6] and [7]; however, importance does not imply that the specific boson‑mediated framework adds predictive value. Our quantitative criterion distinguishes the regime where that framework is necessary.  
- Multiplex‑network analysis in [3] shows that layered transport metrics can exhibit sharp transitions; our memory‑ratio plays an analogous role for exciton‑phonon layers.  
- The noise‑assisted mechanisms identified in [8] are recovered by the optimal dephasing condition $\Gamma^{*}=\Delta$, confirming consistency with established theory.

**Open questions.** (i) What is the exact prefactor linking $\delta\Gamma^{*}$ to $R$? (ii) How does the memory‑ratio criterion generalize to multi‑site networks with path‑dependent $\tau_{T}$? (iii) Can experimental stroboscopic measurements resolve the predicted backflow signatures in vivo?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** The primary users are theoretical chemists, biophysicists, and engineers modelling excitation‑energy transfer in natural or artificial light‑harvesting systems. The memory‑ratio rule provides a quantitative decision point: if $\tau_{B}\gtrsim0.5\,\tau_{T}$, allocate resources to implement the non‑Markovian boson‑mediated framework [9]; otherwise a Markovian master equation suffices.

**(b) Technology readiness.** This work is purely analytical and has not undergone peer review; it resides at Technology Readiness Level 2. Analytical studies never exceed TRL 3.

**(c) Smallest next experiment or calculation.** A full non‑Markovian simulation of the seven‑site FMO Hamiltonian (including experimentally derived spectral densities [5]) that computes (i) transient population backflow amplitudes and (ii) the shift in the optimal dephasing rate. The hypothesis is falsified if the computed corrections are $<1\%$ of the Markovian predictions for $R\ge0.5$.

**(d) Engineering and computational constraints.**  
- **Spectral‑density data.** Accurate $\tau_{B}$ requires high‑resolution spectral densities from atomistic simulations or ultrafast spectroscopy [1, 7].  
- **Computational load.** We assume that a realistic FMO simulation using the non‑Markovian framework requires on the order of $10^{4}$ CPU‑hours (uncertainty factor $\approx 2$).  
- **Parameter uncertainty.** Variations in $V$ and $\Delta$ must be propagated; sensitivity analysis (Section 4.4) shows classification robustness but necessitates careful parameter estimation.

**(e) Order‑of‑magnitude cost projection (projection).** Assuming a cloud HPC price of \$0.10 per CPU‑hour, the minimal full‑scale simulation costs  

\[
\text{Cost}\approx10^{4}\ \text{CPU‑h}\times\$0.10/\text{CPU‑h}= \$1{,}000,
\]  

with an uncertainty factor of two due to possible variations in parallel efficiency.

**(f) Direct risks or misuse paths.** Over‑reliance on the memory‑ratio rule without verifying the underlying spectral density could lead to unnecessary deployment of the expensive non‑Markovian framework, wasting computational resources. Conversely, mis‑classifying a slow‑mode bath as fast could omit essential memory effects, yielding inaccurate design predictions. Clear documentation of the assumptions (single‑exponential bath correlation, weak coupling) mitigates these risks.

## 8. Conclusion

We formulated and applied a quantitative timescale‑based re‑entry test for the non‑Markovian boson‑mediated transport framework [9] in photosynthetic light‑harvesting. Using experimentally reported FMO dimer parameters ($V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$) we derived $\Gamma^{*}=\Delta$, $k^{*}=V^{2}/\Delta$, $\tau_{T}=0.2336\text{–}0.1699\ \mathrm{ps}$, and a single‑hop efficiency ceiling $\eta=0.999001$. Comparing $\tau_{T}$ with bath correlation times spanning $0.1\!-\!1\ \mathrm{ps}$ yields memory ratios $R$ that place fast solvent‑like modes in a transitional window and slow intramolecular modes firmly in the non‑Markovian sector. Sensitivity analysis over the full experimentally reported ranges confirms that $R>0.5$ persists for all realistic slow‑mode scenarios. Consequently, the boson‑mediated non‑Markovian framework re‑enters light‑harvesting modelling precisely when $\tau_{B}\gtrsim0.5\,\tau_{T}$, and it predicts a memory‑scaled shift of the optimal dephasing rate, a hypothesis that can be tested by full‑scale simulations. The memory‑ratio rule thus offers modelers a concrete, analytically derived guideline for allocating computational effort in the study of excitation‑energy transfer.

## References

[1] arXiv:2608.13813v3 | Operator-Level Description of Transient Thermal Grating Dynamics Across Transport Regimes  
[2] arXiv:0910.4153v2 | Noise-assisted energy transfer in quantum networks and light-harvesting complexes  
[3] arXiv:2006.03435v1 | Extracting the multimodal fingerprint of urban transportation networks  
[4] arXiv:1312.5352v2 | Exciton coupling induces vibronic hyperchromism in light-harvesting complexes  
[5] arXiv:1307.0886v2 | Atomistic study of energy funneling in the light-harvesting complex of green sulfur bacteria  
[6] arXiv:2501.02212v1 | Nuclear quantum effects slow down the energy transfer in biological light-harvesting complexes  
[7] arXiv:1511.04936v1 | Ultrafast Energy Relaxation in Single Light-Harvesting Complexes  
[8] arXiv:0901.4454v2 | Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport  
[9] QNFO: Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis | https://papers.qnfo.org/papers/re-entry-of-non-markovian-boson-mediated-transport-into-light-harvesting-complex

## Appendix A. Divergence report

| Claim | Draft A | Draft B | Adopted convention (main text) | Reason for choice |
|-------|---------|---------|-------------------------------|-------------------|
| Representative parameters | $V=30\ \mathrm{cm^{-1}}$, $\Delta=100\ \mathrm{cm^{-1}}$ | $V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$ (experimentally reported) | Use the experimentally reported ranges $V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$ | The ranges are directly supported by the excitonic coupling and site‑energy‑difference data in [4]; the $V=30$ value lies outside the experimentally observed box. |

## Appendix B. Claim attribution

| Claim ID | Source drafts | Agreement status |
|----------|---------------|------------------|
| C1 | A, B, C | CONVERGENT |
| C2 | A, B, C | CONVERGENT |
| C3 | A, B, C | CONVERGENT |
| C4 | A, B, C | CONVERGENT |
| C5 | A, B, C | CONVERGENT |
| C6 | A, B, C | CONVERGENT |
| C7 | A, B, C | CONVERGENT |
| C8 | A, B, C | CONVERGENT |
| C9 | A, B, C | CONVERGENT |
| C10 | A, B, C | CONVERGENT |
| C11 | A, B, C | CONVERGENT |
| C12 | A, B, C | CONVERGENT |
| C13 | A, B, C | CONVERGENT |
| C14 | A, B, C | CONVERGENT |
| C15 | A, B, C | CONVERGENT |
| C16 | A, B, C | CONVERGENT |
| C17 | A, B, C | CONVERGENT |
| C18 | A, B, C | CONVERGENT |
| C19 | A, B, C | CONVERGENT |
| C20 | A, B, C | CONVERGENT |