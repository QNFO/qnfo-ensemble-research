# Grounding block - source: rem-rev-3fabef67-100f-4188-82ec-44771bd3ca90

## Research idea

Re-entry from 10.5281/zenodo.18382696: in light-harvesting complexes?

Post-publication revision of the published paper "Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis" (version 2.4.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 9 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 9, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. The sensitivity box V ∈ [20,75] cm⁻¹ is 'the full experimentally reported range' sourced to [1] (Sections 3.3, 4.5, Abstract). (confirmed by a second model)
2. Section 4.5 states the transfer time as τ_T = ħΔ/(2πcV²). (confirmed by a second model)
3. Abstract: 'the memory ratio R=τ_B/τ_T spans 0.17–1.70' and 'fast baths in a transitional window'. (confirmed by a second model)
4. Section 6.2 cites [3] (urban transportation multiplex networks) as mirroring the R-sensitivity result. (confirmed by a second model)
5. Abstract: 'The memory-ratio R = τ_B/τ_T spans [0.26,0.96] for fast baths (τ_B = 0.1 ps) and [2.6,9.6] for slow baths (τ_B = 1 ps).' (confirmed by a second model)
6. The Lindblad dephasing term is '−(Γ/2)(1 − σ_z²/2)' (Section 3.1). (confirmed by a second model)

## Existing paper under revision (remediation only)

# Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis

## Abstract

Photosynthetic antennae transfer excitation energy with near‑unity efficiency on sub‑picosecond timescales, and modelers must decide whether the computationally expensive non‑Markovian boson‑mediated framework is required or a cheaper Markovian dephasing master equation suffices. Existing applicability tests used parameter ranges broader than experimentally reported values and employed a dimensionally inconsistent transfer‑time formula. We adopt the experimentally reported coupling and site‑energy‑difference ranges for the FMO BChl 3–4 dimer ($V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$) and use the dimensionally sound expression $\tau_{T}= \Delta/(2\pi c V^{2})$. For the representative point $(V,\Delta)=(50,110)\ \mathrm{cm^{-1}}$ the transfer time is $\tau_{T}=0.2336\ \mathrm{ps}$ and the single‑hop trapping efficiency is $\eta=0.999001$. The memory‑ratio $R=\tau_{B}/\tau_{T}$ spans $R_{\mathrm{fast}}\in[0.26,0.96]$ for fast baths ($\tau_{B}=0.1\ \mathrm{ps}$) and $R_{\mathrm{slow}}\in[2.6,9.6]$ for slow baths ($\tau_{B}=1\ \mathrm{ps}$), placing all realistic slow‑mode scenarios firmly in the non‑Markovian sector. We formulate a falsifiable hypothesis that the optimal dephasing rate shifts by $\delta\Gamma^{*}/\Gamma^{*}\sim R$ when $R\gtrsim0.5$. The memory‑ratio rule thus offers a quantitative, analytically derived guideline for allocating computational effort in excitation‑energy‑transfer modelling.

## 1. Introduction

Photosynthetic organisms convert sunlight into chemical free energy after funnelling excitation through pigment networks with efficiencies approaching $100\%$ on sub‑picosecond excitation‑energy‑transfer (EET) timescales. Every computational study of this process faces a concrete methodological decision with real costs on both sides: implement the full non‑Markovian boson‑mediated framework, which retains bath memory at the price of time‑nonlocal kernels and large numerical effort, or use a Markovian dephasing master equation, which is cheap but discards physics exactly when bath correlation times approach the transfer time. Choosing wrongly either wastes high‑performance‑computing allocations or produces transfer rates and optimal dephasing conditions that are quantitatively wrong, which in turn misguides design parameters for bio‑inspired light‑harvesting devices and the interpretation of ultrafast spectra. A validated, analytically derived decision rule would let a modeler allocate compute where memory effects matter and skip them where they do not.

Two decades of theory establish that environmental noise can assist rather than hinder transport: dephasing‑assisted transport raises EET efficiencies above $90\%$ across the Fenna–Matthews–Olson (FMO) complex within a fully Markovian treatment [2], and the underlying mechanisms—suppression of destructive interference and dephasing‑broadened site overlap—are worked out analytically for fully connected networks [8]. On the experimental side, single‑molecule pump–probe spectroscopy resolves sub‑100 fs energy relaxation in individual light‑harvesting complexes [7], so fast solvent‑like bath components with correlation times of order $0.1\ \mathrm{ps}$ are measured, not inferred. Mixed quantum–classical simulations show that treating high‑frequency chromophore vibrations quantum‑mechanically instead of classically slows transfer rates by less than a factor of two for biologically relevant parameters [6]. The target framework whose applicability we assess is the non‑Markovian boson‑mediated description, in which structured phonon fields direct exciton transport and is claimed to sustain efficiencies above $95\%$ [9]. The original applicability analysis of that framework proposed a memory‑ratio test but rested on a parameter box wider than the experimentally reported values and on a transfer‑time formula carrying a spurious factor of $\hbar$.

**Contributions.**  
1. Derivation of the optimal dephasing rate $\Gamma^{*}=\Delta$ and optimal hopping rate $k^{*}=V^{2}/\Delta$ for the two‑site Haken–Strobl model, with the derivative shown explicitly (Section 4.1).  
2. Correction of the transfer‑time formula to $\tau_{T}= \Delta/(2\pi c V^{2})$, with a dimensional check, and its evaluation at the representative reported point $(V,\Delta)=(50,110)\ \mathrm{cm^{-1}}$, giving $\tau_{T}=0.2336\ \mathrm{ps}$ (Section 4.2).  
3. Computation of the single‑hop trapping‑limited efficiency $\eta=0.999001$ under stated assumptions for the trap and recombination rates (Section 4.3).  
4. Recomputation of the memory ratios over the experimentally reported box $V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$, giving $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$, with a corner‑extremality argument (Section 4.4).  
5. A corrected regime classification: within the reported box no bath in the range $\tau_{B}\in[0.1,1]\ \mathrm{ps}$ falls in the Markovian sector, and slow baths are non‑Markovian everywhere (Section 5).  
6. A falsifiable projection that the non‑Markovian correction to the optimal dephasing rate scales as $\delta\Gamma^{*}/\Gamma^{*}\sim R$, with its tension against the sub‑twofold rate effects found for vibrational quantization [6] (Sections 5 and 6).

## 2. Background and Related Work

**Transient thermal‑grating probing.** Transient thermal‑grating (TTG) experiments provide a powerful means of probing material properties and heat‑transport dynamics at small spatiotemporal scales [1]. The technique therefore establishes that sub‑picosecond bath dynamics are experimentally accessible.

**Dephasing‑assisted transport in FMO.** Reference [2] demonstrates that pure dephasing can open transport pathways and raise EET efficiencies above $90\%$ in the FMO complex, establishing the relevance of dephasing‑assisted transport (DAT) for light‑harvesting.

**Excitonic coupling magnitudes.** We assume $V\in[50,75]\ \mathrm{cm^{-1}}$ for the coupling magnitude, consistent with the range used in our analysis.

**Atomistic energy‑funnelling timescales.** Atomistic models of the green‑sulfur‑bacteria light‑harvesting complex indicate sub‑picosecond energy‑funnelling timescales [5], justifying the order‑of‑magnitude of $\tau_{T}$ derived below.

**Quantum nuclear effects on rates.** Quantum‑mechanical treatment of high‑frequency vibrations can affect transfer rates for biologically relevant parameters [6], motivating the inclusion of a non‑Markovian correction in the slow‑bath regime.

**Ultrafast single‑molecule spectroscopy.** Observations of sub‑100 fs energy‑relaxation processes confirm the existence of fast solvent‑like bath components with correlation times on the order of $0.1\ \mathrm{ps}$ [7].

**Multiplex‑network perspective on transport.** Ref. [3] introduces multiplex networks as a mathematical framework for describing layered transport processes, providing an analogy for exciton‑phonon layered dynamics and motivating our memory‑ratio criterion.

**Fundamental role of noise‑assisted transport.** Ref. [8] identifies key mechanisms by which dephasing noise suppresses destructive interference and raises transport efficiency, providing a theoretical foundation for the optimal dephasing condition derived in Section 4.1.

**Non‑Markovian boson‑mediated framework.** The boson‑mediated non‑Markovian framework retains bath memory and is the target framework whose applicability we assess.

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
| $V$ | $[50,75]\ \mathrm{cm^{-1}}$ | Assumed coupling range for the FMO BChl 3–4 dimer |
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
&= \frac{110}{4.7080\times10^{14}}\\
&= 2.336\times10^{-13}\ \mathrm{s}\\
&= 0.2336\ \mathrm{ps}.
\end{aligned}
\]

Thus $\tau_{T}=0.2336\ \mathrm{ps}$ for the representative parameters.

The longest transfer time occurs at the smallest coupling and largest energy gap ($V=50\ \mathrm{cm^{-1}}$, $\Delta=180\ \mathrm{cm^{-1}}$):

\[
\begin{aligned}
\tau_{T}^{\mathrm{max}} &= \frac{180}{2\pi c \, 50^{2}}\\
&= \frac{180}{4.7080\times10^{14}}\\
&= 3.823\times10^{-13}\ \mathrm{s}\\
&= 0.3823\ \mathrm{ps}.
\end{aligned}
\]

The shortest transfer time occurs at the largest coupling and smallest energy gap ($V=75\ \mathrm{cm^{-1}}$, $\Delta=110\ \mathrm{cm^{-1}}$):

\[
\begin{aligned}
\tau_{T}^{\mathrm{min}} &= \frac{110}{2\pi c \, 75^{2}}\\
&= \frac{110}{1.059\times10^{15}}\\
&= 1.039\times10^{-13}\ \mathrm{s}\\
&= 0.1039\ \mathrm{ps}.
\end{aligned}
\]

### 4.3 Trapping‑limited efficiency

The recombination rate is $\gamma_{\mathrm{rec}}=1/\tau_{e}=10^{-3}\ \mathrm{ps^{-1}}$. The single‑hop trapping efficiency is  

\[
\eta = \frac{\kappa}{\kappa+\gamma_{\mathrm{rec}}}= \frac{1}{1+10^{-3}} = 0.999001.
\]

### 4.4 Memory ratio and regime classification

Using the bounds $\tau_{T}^{\mathrm{max}}=0.3823\ \mathrm{ps}$ and $\tau_{T}^{\mathrm{min}}=0.1039\ \mathrm{ps}$, the memory ratio for a given bath correlation time $\tau_{B}$ satisfies

\[
R_{\mathrm{fast}} = \frac{0.1\ \mathrm{ps}}{\tau_{T}} \in \left[\frac{0.1}{0.3823},\frac{0.1}{0.1039}\right]=[0.262,0.962],
\]

\[
R_{\mathrm{slow}} = \frac{1\ \mathrm{ps}}{\tau_{T}} \in \left[\frac{1}{0.3823},\frac{1}{0.1039}\right]=[2.615,9.62].
\]

Rounded to two significant figures,  

\[
R_{\mathrm{fast}}\in[0.26,0.96],\qquad
R_{\mathrm{slow}}\in[2.6,9.6].
\]

All values exceed the $0.5$ threshold for the slow bath, placing every realistic slow‑mode scenario in the non‑Markovian sector. Fast baths may fall below $0.5$ only for the smallest $V$ values; otherwise they remain transitional.

## 5. Results

All numerical values follow directly from the derivations in Section 4.

1. **Optimal dephasing rate:** $\Gamma^{*}= \Delta$, ranging from $110$ to $180\ \mathrm{cm^{-1}}$.  
2. **Optimal hopping rate:** $k^{*}=V^{2}/\Delta$, ranging from $13.89$ to $51.14\ \mathrm{cm^{-1}}$ across the experimental box.  
3. **Transfer time:** $\tau_{T}=0.1039\text{–}0.3823\ \mathrm{ps}$, with the representative value $0.2336\ \mathrm{ps}$.  
4. **Single‑hop efficiency:** $\eta=0.999001$.  
5. **Memory ratios:** $R_{\mathrm{fast}}\in[0.26,0.96]$, $R_{\mathrm{slow}}\in[2.6,9.6]$.  
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

We formulated and applied a quantitative timescale‑based re‑entry test for the non‑Markovian boson‑mediated transport framework [9] in photosynthetic light‑harvesting. Using experimentally reported FMO dimer parameters ($V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$) we derived $\Gamma^{*}=\Delta$, $k^{*}=V^{2}/\Delta$, $\tau_{T}=0.1039\text{–}0.3823\ \mathrm{ps}$, and a single‑hop efficiency ceiling $\eta=0.999001$. Comparing $\tau_{T}$ with bath correlation times spanning $0.1\!-\!1\ \mathrm{ps}$ yields memory ratios $R$ that place fast solvent‑like modes in a transitional window and slow intramolecular modes firmly in the non‑Markovian sector. Sensitivity analysis over the full experimentally reported ranges confirms that $R>0.5$ persists for all realistic slow‑mode scenarios. Consequently, the boson‑mediated non‑Markovian framework re‑enters light‑harvesting modelling precisely when $\tau_{B}\gtrsim0.5\,\tau_{T}$, and it predicts a memory‑scaled shift of the optimal dephasing rate, a hypothesis that can be tested by full‑scale simulations. The memory‑ratio rule thus offers modelers a concrete, analytically derived guideline for allocating computational effort in the study of excitation‑energy transfer.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix A. Divergence report. references 10 -> 8. length 3328 -> 2515 words.
- Version 2.1.0 (2026-10-20, from 2.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples; Appendix B. Claim attribution. references 8 -> 10. length 2555 -> 3312 words.
- Version 2.2.0 (2026-10-20, from 2.1.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Extended Derivations and Worked Examples. references 10 -> 9. length 3387 -> 2798 words.
- Version 2.3.0 (2026-10-20, from 2.2.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Appendix B. Claim attribution. references 9 -> 9. length 2906 -> 2755 words.
- Version 2.4.0 (2026-10-20, from 2.3.0): revised against the current literature, re-reviewed and re-verified. new sections: Appendix B. Claim attribution. references 9 -> 9. length 2895 -> 3015 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.0-refs-extend). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 7 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Operator-Level Description of Transient Thermal Grating Dynamics Across Transport Regimes. arXiv:2608.13813v3. https://arxiv.org/abs/2608.13813v3
[2] Noise-assisted energy transfer in quantum networks and light-harvesting complexes. arXiv:0910.4153v2. https://arxiv.org/abs/0910.4153v2
[3] Extracting the multimodal fingerprint of urban transportation networks. arXiv:2006.03435v1. https://arxiv.org/abs/2006.03435v1
[4] Exciton coupling induces vibronic hyperchromism in light-harvesting complexes. arXiv:1312.5352v2. https://arxiv.org/abs/1312.5352v2
[5] Atomistic study of energy funneling in the light-harvesting complex of green sulfur bacteria. arXiv:1307.0886v2. https://arxiv.org/abs/1307.0886v2
[6] Nuclear quantum effects slow down the energy transfer in biological light-harvesting complexes. arXiv:2501.02212v1. https://arxiv.org/abs/2501.02212v1
[7] Ultrafast Energy Relaxation in Single Light-Harvesting Complexes. arXiv:1511.04936v1. https://arxiv.org/abs/1511.04936v1
[8] Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport. arXiv:0901.4454v2. https://arxiv.org/abs/0901.4454v2
[9] https://papers.qnfo.org/papers/re-entry-of-non-markovian-boson-mediated-transport-into-light-harvesting-complex. QNFO: Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis.

## Appendix A. Divergence report

| Claim | Draft A | Draft B | Adopted convention (main text) | Reason for choice |
|-------|---------|---------|-------------------------------|-------------------|
| Abstract memory‑ratio numbers | $R_{\mathrm{fast}}\in[0.26,0.96]$, $R_{\mathrm{slow}}\in[2.6,9.6]$ | $R_{\mathrm{fast}}\in[0.428,0.589]$, $R_{\mathrm{slow}}\in[4.28,5.89]$ | $R_{\mathrm{fast}}\in[0.26,0.96]$, $R_{\mathrm{slow}}\in[2.6,9.6]$ | The broader ranges follow from the true extrema of $\tau_T$ across the experimentally reported box (Section 4.4). |
| Section 4.4 memory‑ratio ranges | $[0.26,0.96]$ and $[2.6,9.6]$ | $[0.428,0.589]$ and $[4.28,5.89]$ | $[0.26,0.96]$ and $[2.6,9.6]$ | Same reasoning as above; calculations using $\tau_T^{\mathrm{min}}$ and $\tau_T^{\mathrm{max}}$ give the adopted values. |
| Section 5 transfer‑time range | $0.2336\text{–}0.3823\ \mathrm{ps}$ | $0.2336\text{–}0.1699\ \mathrm{ps}$ | $0.1039\text{–}0.3823\ \mathrm{ps}$ | The full range must include both the minimum (0.1039 ps) and maximum (0.3823 ps) transfer times derived in Section 4.2. |

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

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:physics/9904052 | Incoherent Energy Transfer within Light-harvesting Complexes
arXiv:1111.5443 | Superradiance Transition in Photosynthetic Light-Harvesting Complexes
arXiv:0905.3787 | Quantum entanglement in photosynthetic light harvesting complexes
arXiv:1804.09711 | Delocalized excitons in natural light harvesting complexes
arXiv:1012.4059 | Quantum entanglement phenomena in photosynthetic light harvesting complexes
arXiv:1511.04936 | Ultrafast Energy Relaxation in Single Light-Harvesting Complexes
arXiv:0912.5112 | Identifying the quantum correlations in light-harvesting complexes
arXiv:1002.0496 | Dimerization-assisted energy transport in light-harvesting complexes
arXiv:1408.2726 | Bloch-Redfield equations for modeling light-harvesting complexes
arXiv:1312.5352 | Exciton coupling induces vibronic hyperchromism in light-harvesting complexes
arXiv:1801.04924 | Single-photon absorption by single photosynthetic light-harvesting complexes

## QNFO corpus context (Vectorize)

QNFO: Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis | https://papers.qnfo.org/papers/re-entry-of-non-markovian-boson-mediated-transport-into-light-harvesting-complex
QNFO: Non-Markovian Hamiltonian Dynamics of Boson-Mediated Energy Transfer | https://papers.qnfo.org/papers/non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:physics/9904052 | Incoherent Energy Transfer within Light-harvesting Complexes
  Rate equations are used to model spectroscopic observation of incoherent energy transfer in light-harvesting antenna systems based upon known structures. A two-parameter two-dimensional model is proposed. The transfer rates obtained, by matching the fluorescent decay, are self-consistent within our model.
  Full text (https://arxiv.org/html/physics/9904052), excerpts of its own sections:
  § I Introduction: We have had a reasonably complete picture of the bacterial light-harvesting (LH) system recently  [ 1 , 2 ] . Both the inner antenna, LH1, and the outer antenna, LH2, are assembled from the same modules to form rings. Each module consists of two short $\alpha$ -helical polypeptides coordinate one carotenoid and three bacteriochlorophylls (BChls). The LH2 is composed of 9 units, for Rhodopseudomonas acidophila   [ 3 ] , resemble a cylinder, with an inner diameter $36\AA$ and an outer diameter $68\AA$ , while the LH1 is composed of 16 units, for Rhodospirillum rubrum   [ 4 ] , in order to accommodate the reaction center (RC). The later has an outer diameter $116\AA$ and a central diameter $68\AA$ . However, the exact numbers of both complexes are variable  [ 1 , 4 , 5 ] . Furthermore, the LH2 B850 BChl $a$ form a complete over-lapping ring in a hydrophobic environment, which reduces the dielectric constant, while the B800 BChl $a$ are well separated and are in a polar environment. When a BChl molecule is excited by light, the energy can reach equilibrium within about $10ps$   [ 6 ] . [...]
  § II model: With the known periodical structure, shown in Fig. 1 , we can built, from chemical rate equation, the following phenomenological model of energy transfer, $\displaystyle{{dE}\over{dt}}$ $\displaystyle=$ $\displaystyle{k^{{}^{\prime}}}A_{1}-(k^{{}^{\prime\prime}}+k_{E})E\;,$ (1) $\displaystyle{{dA_{1}}\over{dt}}$ $\displaystyle=$ $\displaystyle kA_{16}-2kA_{1}+kA_{2}-k^{{}^{\prime}}A_{1}+k^{{}^{\prime\prime}}E\;,$ (2) $\displaystyle{{dA_{n}}\over{dt}}$ $\displaystyle=$ $\displaystyle kA_{n-1}-2kA_{n}+kA_{n+1}\;,\qquad n=2...15\;,$ (3) $\displaystyle{{dA_{16}}\over{dt}}$ $\displaystyle=$ $\displaystyle kA_{15}-2kA_{16}+kA_{1}\;,$ (4) in which $A_{n}$ s denote the excited BChl dimer, $E\equiv P^{*}BH$ is the excited state, with B representing the chlorophyll monomer within the RC, and $P^{*}$ is the excited special pair of BChl molecules. It is a set of 17 coupled linear differential equations. The symmetry of this system is broken due to $k^{{}^{\prime}}\neq k^{{}^{\prime\prime}}$ . A similar model has been proposed by Skála et al.   [ 15 ] . [...]
  § III spectrometry comparison: We can verify our model against experiments: The pump-probe spectroscopy measures the difference between two beams, with $\Delta D=\Delta\epsilon_{A}\sum_{n}A_{n}+\Delta\epsilon_{E}E\;,$ (11) being the signal measured. The symbol $\Delta\epsilon$  s are the differences in dielectrical constants between pump and probe beams of the corresponding pigments. [...]
  § IV Conclusion: In summary, a physicist’s approach [ 23 ] of incoherent energy transfer within an antenna ring is taken by considering a two-parameter two-dimensional model. This model differs from the one presented by Skála et al. . The reality might be somewhere between these two models. In our model, we numerically found $k$ has to be equal to $k^{{}^{\prime}}$ . Furthermore, we are able to calculate analytically some of the eigenvalues and demonstrate explicitly that there is a mode for decaying to the RC and other three modes. However, this result of mode separation depends upon the exact number of unit involved in the ring. Therefore should not be important. Perhaps we should interpret the finding as: $P_{16}^{1}$ , $P_{16}^{2}$ , $P_{16}^{3}$ are redundant, since $P_{16}^{4}$ contains $k_{E}$ which should be important. A ring of $16$ units is huge. The only purpose for such a large antenna is to accommodate the $RC$ . [...]
[2] arXiv:1111.5443 | Superradiance Transition in Photosynthetic Light-Harvesting Complexes
  We investigate the role of long-lasting quantum coherence in the efficiency of energy transport at room temperature in Fenna-Matthews-Olson photosynthetic complexes. The excitation energy transfer due to the coupling of the light harvesting complex to the reaction center ("sink") is analyzed using an effective non-Hermitian Hamiltonian. We show that, as the coupling to the reaction center is varie
  Full text (https://arxiv.org/html/1111.5443), excerpts of its own sections:
  § I Introduction: The annual amount of energy humans currently use is delivered to Earth by the Sun in a few hours! Since solar energy is very dilute, it is essential to transport the captured energy efficiently. Most natural photosynthetic systems consist of antenna complexes, which capture photons from the Sun and transport energy to a reaction center (RC). There, it is transformed into chemical energy via charge separation. Antenna complexes are able to transfer excitations to RCs with an efficiency exceeding $95\%$ . For a long time, it was thought that energy transfer in photosynthetic light-harvesting complexes occurs through classical processes, similar to random walks of the exciton to the RC. However, surprising evidence of coherent quantum energy transfer has been found recently [ 1 , 2 ] . These findings raise two basic questions. How can coherence be maintained in complex biological systems at room temperature? Why is quantum coherence relevant to the efficiency of energy transfer? The first question has been addressed in [ 3 , 4 ] . We consider here the second one. [...]
  § II The Model for Superradiance transition: The FMO complex is a trimer, composed of identical subunits, each of which contains seven bacteriochlorophylls (BChl) [ 21 ] . Each subunit acts independently and can be modelled using a tight-binding Hamiltonian, $H_{0}=\sum_{i=1}^{7}E_{i}|i\rangle\langle i|+\sum_{i,j}(J_{i,j}|i\rangle\langle j|+h.c.).$ (1) Here, $|i\rangle$ is the state in which the $i$ -th site is excited and the others are in the ground state. Since the solar energy is very dilute, we limit the description to a single excitation in the complex, as is commonly done in the literature. The numerical values of $E_{i}$ and $J_{i,j}$ have been taken from Ref.  [ 3 ] . [...]
  § III Superradiance transition: ST can be analyzed by studying the complex eigenvalues, ${\cal E}_{r}=E_{r}-i\Gamma_{r}/2$ of $H_{\rm eff}$ , defined in ( 4 ). As the coupling between the excitonic states and the RC increases, one observes a rearrangement of the widths, $\Gamma_{r}$ (the “superradiance” transition [ 16 ] ). We show this effect in Fig.  1 (left panel), where the largest width (red dashed curve) and the average of the $7-1=6$ smallest widths (black full curve) are plotted as functions of $T_{1r}$ . For weak coupling to RC (large $T_{1r}$ ) the widths of all states increase as $T_{1r}$ decreases. [...]
  § VII Conclusion: We have analyzed energy transport in the FMO system with the aid of a non-Hermitian Hamiltonian approach. This allows us to take into account the effect of the coupling of the FMO system to the reaction center in a consistent way, not merely phenomenologically, as is usually done in the literature. We have shown that by increasing the strength of the coupling to the reaction center, a superradiance transition occurs. This transition occurs at approximately the same value of the coupling for which energy transport efficiency is maximal. Indeed, the superradiance transition is due to coherent constructive interference between the paths to the RC, and this effect enhances the rate of energy transfer. Since the ST effect is due to quantum coherence, one might expect that any consequences of ST would disappear in the presence of dephasing and relaxation provided by the thermal bath. On the contrary, we have shown that the effect of superradiance survives in the presence of the thermal bath, and the maximal efficiency only depends weakly on temperature. [...]
[3] arXiv:0905.3787 | Quantum entanglement in photosynthetic light harvesting complexes
  Light harvesting components of photosynthetic organisms are complex, coupled, many-body quantum systems, in which electronic coherence has recently been shown to survive for relatively long time scales despite the decohering effects of their environments. Within this context, we analyze entanglement in multi-chromophoric light harvesting complexes, and establish methods for quantification of entan
  Full text (https://arxiv.org/html/0905.3787), excerpts of its own sections:
  § I Light harvesting complexes and entanglement: Recent ultrafast spectroscopic studies have revealed the presence of quantum coherence at picosecond timescales in biological structures, specifically, in light harvesting complexes [ 10 , 11 , 12 , 13 ] . These studies demonstrate that in moderately strongly coupled, non-equilibrium systems, quantum features can be observed even in the presence of a poorly controlled, decohering environment. During the initial stage of photosynthesis, light is captured by pigment-protein antennas, known as light harvesting complexes, and the excitation energy is then transferred through these antennas to reaction centers where photosynthetic chemical reactions are initiated. Different LHCs vary in their detailed structure but all consist of densely packed units of pigment molecules, and all are spectacularly efficient at transporting excitation energy in disordered environments [ 14 ] . Average inter-chromophore separations on the scale of $\sim 15\mathrm{\AA}$ are fairly common in LHCs. [...]
  § II Entanglement dynamics in the FMO complex: A commonly studied LHC is the Fenna-Matthews-Olson (FMO) protein from green sulfur bacteria, such as Chlorobium tepidum [ 21 ] . The FMO complex is a trimer formed by three identical monomers that each bind seven bacteriochlorophyll- a (BChl a ) molecules. We will restrict our study to a single monomer, which is shown in Fig. 1, since the monomers function independently. The site energies of the BChl a molecules and coupling between molecules are well characterized; we use the Chlorobium tepidum site energies and coupling strengths from Ref. [ 22 ] to form a Hamiltonian that describes the closed-system dynamics of an FMO monomer excitation (see the Supplementary Information for details). The structure of the Hamiltonian indicates that some pairs of chromophores are moderately strongly coupled (due to their close proximity and favorable dipole orientations) and hence effectively form dimers . The wavefunctions of the system’s energy eigenstates, usually called Frenkel excitons , are primarily delocalized across these dimers. [...]
  § III Significance and implications of LHC entanglement: The previous section presented numerical evidence for the existence of entanglement in the FMO complex for picosecond timescales – essentially until the excitation is trapped by the reaction center. This is remarkable in a biological or disordered system at physiological temperatures. It illustrates that non-equilibrium multipartite entanglement can exist for relatively long times, even in highly decoherent environments. While the length scales over which entanglement was shown to persist were restricted to $\lesssim 30\mathrm{\AA}$ because of the relatively small size of the FMO complex, we expect that such long-lived, non-equilibrium entanglement will also be present in larger light harvesting antenna complexes, such as LH1 and LH2 in purple bacteria. This is because they contain the key necessary ingredient; moderately strongly coupled chromophores that can lead to significant coherent delocalization of electronic excitations [ 25 , 16 ] . [...]
  § IV.1 Measures of entanglement in LHCs: The single excitation assumption valid for many light harvesting complexes allows us to formulate simple measures of entanglement in these systems. First, note that if $\rho$ represents a single excitation state in the site basis, we have the following: Proposition 1: $\rho$ entangled $\iff\rho_{ij}\neq 0$ for some $i\neq j$ . Here, the right hand side simply means that $\rho$ has some coherence. [...]
[4] arXiv:1804.09711 | Delocalized excitons in natural light harvesting complexes
  Natural organisms such as photosynthetic bacteria, algae, and plants employ complex molecular machinery to convert solar energy into biochemical fuel. An important common feature shared by most of these photosynthetic organisms is that they capture photons in the form of excitons typically delocalized over a few to tens of pigment molecules embedded in protein environments of light harvesting comp
  Full text (https://arxiv.org/html/1804.09711), excerpts of its own sections:
  § I Introduction: The energy for life on earth begins with harvesting of photons from sunlight. To perform this quantum mechanical process, photosynthetic organisms have developed a wide range of highly tuned forms of light harvesting complexes (LHCs) [ 14 , 20 , 117 , 58 ] , while utilizing surprisingly few kinds of pigment molecules [ 20 , 63 ] as primary units that absorb photons and create electronic excitations (excitons) [ 73 , 11 ] . Most LHCs consist of about $10-100$ pigment molecules held by protein scaffolds, with typical inter-pigment distances $\gtrsim 1{\rm nm}$ , and harness excitons that are typically delocalized over a few to tens of such pigment molecules. In general, the light harvesting unit of a specific photosynthetic organism is formed by aggregates or super-complexes of those LHCs. Each LHC exhibits unique structural and energetic features realized through specific arrangement of pigment molecules with finely tuned excitation energies [ 20 ] , which in turn determine the energetics and the dynamics of delocalized excitons. [...]
  § II Overview of major light harvesting complexes: Figure 2: A schematic of three domains constituting photosynthesis, performing light harvesting (LH), charge separation (CS), and biochemical reaction (BR). Their respective time scales are denoted as $\tau_{LH}$ , $\tau_{CS}$ , and $\tau_{BR}$ . The length scales of these domains are denoted as $l_{LH}$ , $l_{CS}$ , and $l_{BR}$ , respectively. [...]
  § VII Discussion: LHCs have characteristics and challenges that are distinctively different from any other biological complexes in relation to their specific function. While the importance of structural information for LHCs is inarguable, it is necessary to recognize that the functionality of an LHC is determined by how and where excitons are formed and how fast and efficiently the excitons move from one region to another, while conserving their energies as much as possible even in the presence of disorder and fluctuations. Elucidating these details require reliable information on the energetics and the dynamics of excitons in the excited potential energy surfaces. In addition to structural data, a comprehensive collection of spectroscopic and computational data are needed even for establishing a Hamiltonian that can represent the behavior of excitons with reasonable accuracy. Calculation and simulation of quantum dynamical evolution of excitons in these systems are equally challenging due to their complexity and sizes. [...]
  § VIII Conclusion and Outlook: Experimental and theoretical evidences cumulated so far support that the majority of excitons residing in pigment molecules of LHCs can be well described by the Frenkel exciton theory. This is in contrast to the excitons found in most man-made solar energy conversion systems. For example, excitons created in the first generation semiconductor-based materials are dominantly Wannier excitons. Even for organic photovoltaic devices consisting of conjugated organic molecules, excitons tend to have intermediate character and cannot be represented by simple Frenkel exciton Hamiltonians. Why nature takes special advantage of Frenkel excitons, which have been difficult to utilize in man-made systems so far, is an interesting issue to investigate. A possible explanation based on current experimental and theoretical evidences is that it is related to the properties of proteins as insulating media and to their superb capability to fine tune excitation energies and spatial arrangement of pigment molecules. [...]
[5] arXiv:1012.4059 | Quantum entanglement phenomena in photosynthetic light harvesting complexes
  We review recent theoretical calculations of quantum entanglement in photosynthetic light harvesting complexes. These works establish, for the first time, a manifestation of this characteristically quantum mechanical phenomenon in biologically functional structures. We begin by summarizing calculations on model biomolecular systems that aim to reveal non-trivial characteristics of quantum entangle
  Full text (https://arxiv.org/html/1012.4059), excerpts of its own sections:
  § I Introduction: Entanglement, the non-local correlations between distinct quantum systems, was referred to by Schrödinger in his 1935 discussion of the issues raised by the paradox of Einstein, Podolsky and Rosen (EPR) [ 1 ] , as “the characteristic trait of quantum mechanics, the one that enforces its entire departure from classical lines of thought” [ 2 ] . The phenomenon is uniquely quantum in that, unlike wave-like evolutions, there is no classical analogue. The non-local correlations derive from the structure of the quantum states of the combined system. The fact that these quantum correlations in the composite system are independent of the spatial separation of the constituents, so that in some sense these appear to behave as a single system, results in violation of local realism, leading to the difficulties posed by EPR [ 1 ] . [...]
  § II Entanglement in model systems: Dimeric models provide the smallest systems in which features of entanglement can be studied. While energy transport is unrealistically restricted, analysis of excitonic dynamics in dimeric systems has revealed a number of insights into bipartite entanglement and how it may be affected by the biological environment. The first study of entanglement in a dimer of chromophores was made by Thorwart et al., [ 15 ] who used a spin-boson Hamiltonian model for each chromophore together with dipole-dipole interchromophore coupling and an ohmic bath with variable frequency cutoff. Using the real time path integral approach to simulate the excitonic dynamics, these authors evaluated the time dependence of the negativity measure of bipartite entanglement, $N(t)=\max\left[0,-2\xi_{\rm min}(t)\right]$ ( $\xi_{\rm min}$ is the smallest eigenvalue of the partial transpose reduced density operator of one chromophore) [ 16 ] and investigated the behavior of this as the bath frequency cut off, and hence the timescale of the bath response, varies. [...]
  § III Entanglement in the Fenna-Matthews-Olson complex: Most theoretical studies of non-classical phenomena in light harvesting structures to date have focused on the FMO complex of green sulfur bacterium [ 34 , 35 , 36 ] because this is an extremely well characterized pigment-protein structure. FMO does not directly absorb sunlight, but acts instead as a “quantum wire” to transmit electronic excitation from the light harvesting antenna that actually absorbs photons, to the reaction center where charge separation then occurs. Fig. [...]
  § V Discussion: The theoretical studies summarized here present convincing evidence for creation and robust evolution of quantum correlations in the natural functioning of pigment-protein structures such as light harvesting complexes. The quantum non-local correlations associated with entanglement of distinct physical entities are seen to be naturally generated by the time evolution of excitonic energy through light harvesting structures and to be present both over relatively large distances of several nm and to be globally distributed over multiple chromophoric units. Furthermore, the studies of the FMO and LHCII light harvesting systems made using realistic dynamical simulations incorporating the environmental dynamics on their natural timescales [ 27 , 28 ] show that the entanglement is remarkably robust and persistent, achieving a significant long time, steady state value in both instances. [...]
[6] arXiv:1511.04936 | Ultrafast Energy Relaxation in Single Light-Harvesting Complexes
  Energy relaxation in light-harvesting complexes has been extensively studied by various ultrafast spectroscopic techniques, the fastest processes being in the sub-100 fs range. At the same time much slower dynamics have been observed in individual complexes by single-molecule fluorescence spectroscopy (SMS). In this work we employ a pump-probe type SMS technique to observe the ultrafast energy rel
  Full text (https://arxiv.org/html/1511.04936), excerpts of its own sections:
  § Introduction: Time-resolved studies of primary events in photosynthetic light harvesting have a decades-long tradition. Usually, the fastest processes observed correspond to the time resolution of the experimental techniques available at the time. Recently, the most popular tool to study ultrafast excitation energy transfer with sub-100 fs resolution is two-dimensional electronic spectroscopy (2DES). This technique has been used to study various light-harvesting complexes such as LH2 and LH1 antennas of purple bacteria [ 1 , 2 ] , the FMO protein of green sulphur bacteria [ 3 , 4 ] and the major antenna complex LHCII of higher plants [ 5 ] . It was shown that after an ultrafast excitation of photosynthetic light-harvesting complexes (LHCs) the electronic excitation evolves in a coherent fashion on a 100 fs timescale. These observations sparked a still ongoing debate on the role of quantum coherence in energy transfer in LHCs. However powerful the ultrafast techniques have become, they are fundamentally limited by ensemble averaging. [...]
  § The measurement: The SM2P principle is based on exciting the system by a near-saturating laser pulse and giving it a time window to relax to some off-resonant state before applying a second pulse. By such relaxation the excitation in the system can be saved from the stimulated emission caused by the second pulse, and the overall excitation probability therefore rises with the pulse delay. [...]
  § Conclusions: We have successfully applied the SM2P technique to LH2 complexes of purple bacteria. We have demonstrated that it is possible to observe ultrafast energy relaxation in individual light-harvesting complexes. As such, our work highlights a new possible way to study photosynthetic light-harvesting. We have shown how the relaxation time distribution changes when tuning the excitation wavelength. The observed behaviour can be explained by varying influence of the B800 and B850* states of the LH2 rings, in agreement with previous ultrafast spectroscopy studies. By a numerical calculation we were able to qualitatively explain the shape of the relaxation time distribution as a result of the energetic disorder of the LH2 pigments. The extent of disorder corresponds to the values commonly used in bulk spectroscopy modelling. Our method can be extended to include a detailed excitation wavelength scan, which would enable us to study energy transfer dynamics of single LH2 complexes to an extent similar to bulk transient absorption measurements. [...]
  § Experimental setup: The experimental setup is similar to the one in Ref. [ 8 ] , briefly a 76 MHz Ti:Sapphire laser (Mira 900F, Coherent) is used as a source of 200-250 fs, 4-5 nm spectrally wide pulses centered at 800 nm. By tuning the laser cavity the wavelength can be tuned approx. from 750 nm to 850 nm. The repetition rate is decreased to 2 MHz by a pulse-picker (PulseSelect, APE) to increase the survival time of the complexes and eliminate long-living dark states such as triplet states. The absence of the triplet states is verified by checking the signal drops to half when halving the repetition rate. The two pulses are produced by a home-built Michelson interferometer, the delay between them is scanned by a delay line (Newport) in one of the interferometer arms. The pulse length before the microscope is measured by fringe-resolved autocorrelation [ 30 ] using the same interferometer and focusing the pulses into a BBO crystal (Eksma optics). The pulse spectrum is measured by a spectrometer (OceanOptics). Technical details can be found in the SI. [...]
[7] arXiv:0912.5112 | Identifying the quantum correlations in light-harvesting complexes
  One of the major efforts in the quantum biological program is to subject biological systems to standard tests or measures of quantumness. These tests and measures should elucidate if non-trivial quantum effects may be present in biological systems. Two such measures of quantum correlations are the quantum discord and the relative entropy of entanglement. Here, we show that the relative entropy of 
  Full text (https://arxiv.org/html/0912.5112), excerpts of its own sections:
  § I Introduction: Quantum biology aims to understand if, how, and why biological systems exploit quantum-mechanical effects for their functionality or for an evolutionary advantage [ 1 , 2 , 3 , 4 ] . Exemplary biological systems that may exploit quantum effects vary from photosynthetic light-harvesting complexes [ 5 ] , to the avian compass for bird navigation [ 6 ] , to the olfactory system [ 7 ] . Ongoing theoretical research indicates that light-harvesting complexes exploit an environment-assisted quantum-walk like effect to enhance energy transport [ 8 , 9 , 11 , 10 ] , the avian compass exploits a radical ion-pair mechanism for increased sensitivity of the earth’s geomagnetic field [ 12 , 13 , 14 ] , and the olfactory system may exploit phonon-assisted tunneling for enhanced detection of smell [ 7 ] . Light-harvesting complexes seem particularly suitable as biological systems to harness quantum-mechanical effects. [...]
  § II.1 FMO Complex Dynamics: The FMO protein complex is the crucial, light-harvesting component of the green sulfur bacteria prosthecochloris aestuarii , that develop in dimly-lit, anoxic environments such as stratified lakes or sulfur springs [ 37 ] . It is a trimer, consisting of three identical subunits. We study one unit of the trimer, consisting of seven bacteriochlorophyll sites that act as a “molecular wire,” transferring energetic excitations from a photon-receiving antenna to a reaction center. A photon impinges on the antenna, producing an electronic excitation, dubbed an exciton, that then proceeds to the unit with seven sites. [...]
  § IV Simulation Results: We conducted several simulations at both cryogenic temperature (77 ∘ K) and physiological temperature (300 ∘ K) and for the initial state being a pure state at site one, six, and the mixture of the previous two. These simulations calculate both the quantum mutual information, quantum discord, and single-excitation relative entropy of entanglement with respect to several “bipartite cuts” of the sites in the FMO complex. Throughout this section, we refer to quantum discord, but all our simulations indicated that the single-excitation relative entropy of entanglement is equal to the quantum discord. These results provide strong evidence that the quantum discord is equal to the formula in Theorem  1 for these cases, but a general proof of this conjecture eludes us for now. Our different simulation cases are as follows: 1. We first considered the cut where system $A$ consists of site three and system $B$ consists of sites one and six. [...]
  § VI Conclusions: We presented results quantifying the quantum correlations present in a biological system at cryogenic and physiological temperature. Theorem  1 proves that the single-excitation relative entropy of entanglement admits a simple form. We then simulated the dynamics of the FMO complex and calculated the quantum discord and the quantum mutual information for various phenomenologically motivated bipartite cuts of the sites in the FMO protein complex. It is surprising that the quantum discord and the single-excitation relative entropy of entanglement are equivalent for these simulations, but we have not been able to find a general proof that the quantum discord of this system is equivalent to the formula in Theorem  1 . The results of our simulations indicate that quantum correlations contribute a significant fraction of the total correlation during the first picosecond of dynamics in many cases. [...]
[8] arXiv:1002.0496 | Dimerization-assisted energy transport in light-harvesting complexes
  We study the role of the dimer structure of light-harvesting complex II (LH2) in excitation transfer from the LH2 (without a reaction center (RC)) to the LH1 (surrounding the RC), or from the LH2 to another LH2. The excited and un-excited states of a bacteriochlorophyll (BChl) are modeled by a quasi-spin. In the framework of quantum open system theory, we represent the excitation transfer as the t
  Full text (https://arxiv.org/html/1002.0496), excerpts of its own sections:
  § I Introduction: To face the present and forthcoming global energy crisis, human should search for clean and effective energy source. Recently the investigations on the basic energy science for this purpose has received great attention and experienced impressive progress based on the fundamental physics [ 1 , 2 ] . In photosynthetic process, the structural elegance and chemical high efficiency of the natural system based on pigment molecules in transferring the energy of sunlight have stimulated a purpose driven investigation [ 3 , 4 , 5 , 8 , 9 , 6 , 10 , 11 , 7 , 12 , 13 ] , finding artificial analogs of porphyrin-based chromophores. These artificial systems replicate the natural process of photosynthesis [ 2 ] so that the much higher efficiencies could be gained than that obtained in the conventional solid systems [ 2 ] . It is because one of the most attractive features of photosynthesis is that the light energy can be captured and transported to the reaction center (RC) within about 100ps and with more than 95% efficiency [ 4 , 14 ] . [...]
  § II Model setup: The simplified model of LH2 is shown in Fig. 1 . All the bacteriochlorophylls (big and small green squares) are modeled by the two-level systems with excited state $|e_{j}^{[c]}\rangle$ , ground state $|g_{j}^{[c]}\rangle$ , and energy level spacing $\Omega_{c}$ . The raising and lowering quasi-spin operators of the $j$ th two-level system on the $[c]$ ring is expressed as $\sigma_{j}^{+[c]}=|e_{j}^{[c]}\rangle\langle g_{j}^{[c]}|\text{, }\sigma_{j}^{-\left[c\right]}=|g_{j}^{[c]}\rangle\langle e_{j}^{[c]}|,$ (1) where $[c]=$ $\left[a\right]$ ( $\left[b\right]$ ) denotes the B800 (B850) BChl ring. Approximately, all the couplings are supposed to be of XY type [ 5 ] . This simplification enjoys the main feature of excitation transfer. [...]
  § III Transfer efficiency and average transfer time via the master equation: Next we consider the energy transfer from an initial state $\widehat{\rho}\left(0\right)=\sum_{j,l}\rho_{Aj,Al}\left(0\right)\left|A,j\right\rangle\left\langle A,l\right|,$ (10) which is a coherent superposition or a mixture of those local states $\left|A,j\right\rangle$ on the B800 ring. As time goes by, the initial state will evolves a state distributing around both the B800 and the B850 rings. Since there exists a difference of chemical potential. $\Delta\Omega=\Omega_{a}-\Omega_{b}$ , energy is transferred between the two rings during the time evolution. [...]
  § VII Conclusion: In summary, we have studied the craggy transfer in light-harvesting complex with dimerization. We employed the open quantum system approach to show that the dimerization of the B850 BChl ring can enhance the transfer efficiency and shorten the average transfer time for different initial states with various quantum superposition properties. Actually our present investigation only focuses on a crucial stage in photosynthesis – the energy transfer, which is carried by the coherent excitations in the typical light-harvesting complex II (LH2). Here the LH2 is modeled as two coupled bacteriochlorophyll (BChl) rings. With this modeling, the ordinary photosynthesis is roughly described as three basic steps: 1) stimulate an excitation in LH2; 2) transfer it to another LH2 or LH1; 3) the energy causes the chemical reaction that converts carbon dioxide into organic compounds. Namely, the excitations are transferred to the RC through B800 (LH2) $\rightarrow$ B850 (LH2) $\rightarrow$ B850 (another LH2) $\rightarrow\cdots\rightarrow$ B875 (LH1) $\rightarrow$ RC. [...]
[9] arXiv:1408.2726 | Bloch-Redfield equations for modeling light-harvesting complexes
  We challenge the misconception that Bloch-Redfield equations are a less powerful tool than phenomenological Lindblad equations for modeling exciton transport in photosynthetic complexes. This view predominantly originates from an indiscriminate use of the secular approximation. We provide a detailed description of how to model both coherent oscillations and several types of noise, giving explicit 
  Full text (https://arxiv.org/html/1408.2726), excerpts of its own sections:
  § I Introduction: Following experimental evidence of long-lived oscillatory features in the dynamical response of several photosynthetic systems [ 1 , 2 , 3 ] , there have been many studies analyzing quantum coherence and the effects of decoherence in light harvesting complexes (LHCs) [ 4 ] . A complete understanding of the coherence properties and the spectral response of this type of molecular aggregates has been shown to require the inclusion of non-Markovian effects [ 5 , 6 , 7 , 8 , 9 , 10 ] and/or the use of numerically exact methods [ 11 , 12 , 13 , 14 ] . However, Markovian master equations, such as Lindblad or Bloch-Redfield equations, still provide powerful insight and generally serve as the initial test-bed from which more accurate descriptions can be built up [ 15 , 16 , 17 , 18 , 19 , 20 , 21 ] . While the Bloch-Redfield approach has been successfully used by several groups [ 22 , 23 , 24 , 25 , 26 , 27 , 28 ] to describe excitonic dynamics in LHCs, there have also been many publications emphasizing its shortcomings [ 29 , 30 , 18 , 7 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 ] . [...]
  § II Lindblad vs. Bloch-Redfield equations: In light-harvesting complexes the system Hamiltonian $H_{s}$ describes the system and all its quantum coherent features, typically the electronic degrees of freedom. In terms of the states $\left|j\right\rangle$ which describe an excitation on the spatial site $j$ , the system Hamiltonian is typically of the form $H_{s}=\sum_{j}\epsilon_{j}\left|j\right\rangle\left\langle j\right|+\sum_{j\neq k}g_{jk}(\left|j\right\rangle\left\langle k\right|+\left|k\right\rangle\left\langle j\right|$ , where the first term describes the sites at energy $\epsilon_{j}$ and the second term the dipolar couplings between sites $g_{jk}$ . To then model the noise influence and incoherent dynamics due to electron-phonon coupling resulting from the phonon environment of intramolecular and protein vibrations a master equation approach is often used. The Lindblad equations are a popular tool for this because their mathematical form guarantees a time evolution that is linear trace preserving and positive (completely positive, to be precise, as we will discuss in section IV ), restricting the populations, i.e. [...]
  § II.1 Measurement basis and oscillations: In light-harvesting complexes there are typically two different types of evolution that are being modelled: different spectroscopy experiments in the lab on the one hand and the excitation dynamics as it occurs in nature and facilitates transport towards the reaction centre on the [...]
  § VI Conclusions: We have presented how the Bloch-Redfield equations can be utilised to model excitation transfer dynamics in chromophoric aggregates or light-harvesting complexes in a consistent manner. The equations link back generally to a physical model of system-environment interaction Hamiltonian and spatial-temporal correlations contained in the spectral function, giving more flexible and adaptable modeling options than a phenomenological Lindblad approach. We have shown how issues of non-positivity and non-physicality or the loss of coherent oscillations are not inherent to the Bloch-Redfield formalism, and can be ruled out by an underpinning consistent physical model. If the secular approximation is applied, it needs to be based on the occurrence of different scales and applied carefully for the respective system at hand. Given these conditions, the secular approximation will not significantly alter the equations but merely simplify them by setting negligible elements to zero. [...]
[10] arXiv:1312.5352 | Exciton coupling induces vibronic hyperchromism in light-harvesting complexes
  The recently suggested possibility that weak vibronic transitions can be excitonically enhanced in light-harvesting complexes is studied in detail. A vibronic exciton dimer model which includes ground state vibrations is investigated using multi-configuration time-dependent Hartree method with a parameter set typical to photosynthetic light-harvesting complexes. Absorption spectra are discussed in
  Full text (https://arxiv.org/html/1312.5352), excerpts of its own sections:
  § 1 Introduction: In photosynthesis light absorption and charge separation take place in specialised multi-chromophoric systems. While the reaction centre (RC) complexes, where the primary charge separation occurs, are very similar in different photosynthetic systems, the light-harvesting antennas show a wide variety [ 1 ] . Clearly, it is possible to optimise absorption of light and make excitation transport to RC efficient in many different ways. One of the strategies used in most of the photosynthetic systems is to organise the pigments energetically in an energy funnel with the RC in the bottom of the sink [ 2 ] . In addition, the pigment molecules are usually close enough to enable sufficient resonant interaction and thereby fast excitation transport. Such general optimisation strategies are widely reported and well understood in photosynthetic antenna systems. A result of the relatively dense packing of the pigment molecules in the antenna complexes is the emergence of delocalised Frenkel exciton states  [ 3 , 4 , 5 , 6 ] . [...]
  § 2.1 Frenkel Exciton Hamiltonian: In the following we will use the Frenkel exciton Hamiltonian describing coupled electronic (zero, $|0\rangle$ , and one-exciton, $|m\rangle$ , space) and nuclear degrees of freedom, $\mathbf{Q}=\{\mathbf{Q}_{m}\}$ , [ 3 ] $\displaystyle H_{\rm agg}(\mathbf{Q})$ $\displaystyle=$ $\displaystyle H^{(0)}(\mathbf{Q})+H^{(1)}(\mathbf{Q})\,,$ (1) $\displaystyle H^{(0)}(\mathbf{Q})$ $\displaystyle=$ [...]
  § 3 Results and Discussion: In the following application the case of two sites (vibronic heterodimer, $m=(D,A)$ ) will be considered. The parameters are chosen to mimic the situation in the FMO complex. A number of studies have proposed electronic Hamiltonian of the complex, based on modelling of a set of spectroscopic observables. For a review see [ 54 ] . There is a general agreement that the BChl 3 and 4 have the lowest site energies. The transition energy difference is proposed to be from about 110 to 180 cm -1  . Excitonic coupling between these two molecules is negative with values from about -50 to -75 cm -1   [ 29 ] . Fluorescence line narrowing spectroscopy has revealed that at around 180 cm -1  there are a few vibrational modes in the FMO lowest energy BChl with a total Huang-Rhys factor 0.03 [ 27 ] . We point out that the analogous experiments with BChl in triethylamine give a somewhat higher value of 0.04 [ 28 ] . Having these parameters in mind we formulate our vibronic dimer as follows. [...]
  § 4 Summary: We have carried out a thorough comparison of OPA and exact calculations of vibronic excitons in a dimer model. We found that the general behaviour of the calculated absorption spectra are surprisingly similar despite of the radically different energy level structure in the two models. Multi-mode effects have been discussed in dependence on the mode parameters. In the case of negative coupling, which is relevant for the FMO complex, most oscillator strength is concentrated in a transition to a state of essentially electronic character such that no pronounced effect on the spectrum arises. Calculations of the fluorescence spectra show that the Huang Rhys factors obtained from fluorescence spectroscopy of light-harvesting complexes with significant excitonic couplings, need to be corrected. Depending on the excitonic coupling strength and detuning, the correction can be as large as 100%. At the same time, the observed frequencies are not affected if measured at low temperature where the transitions from higher energy levels are not giving any significant contribution.
[11] arXiv:1801.04924 | Single-photon absorption by single photosynthetic light-harvesting complexes
  We provide a unified theoretical approach to the quantum dynamics of absorption of single photons and subsequent excitonic energy transfer in photosynthetic light-harvesting complexes. Our analysis combines a continuous mode -photon quantum optical master equation for the chromophoric system with the hierarchy of equations of motion describing excitonic dynamics in presence of non-Markovian coupli
  Full text (https://arxiv.org/html/1801.04924), excerpts of its own sections:
  § I Introduction: Photosynthetic light harvesting of plants and bacteria in vivo is characterized by the remarkable capability of reaching near unit yield of electron-hole pairs from electronic excitations produced by absorption of a photon. Plants usually only operate with such high efficiency under weak illumination conditions and also possess the ability to modify this quantum efficiency in real time to respond to changes in environmental conditions, in particular to reduce it when the intensity of incident light becomes high enough to cause damage to the photosynthetic apparatus. The yield of electron-hole pairs from absorbed photons is commonly referred to as the “quantum efficiency” of light harvesting and the upper limit of unity is often referred to as implying the transfer of a single photon to a single electron-hole pair, although it is extracted from bulk kinetic measurements of fluorescence. However this efficiency does not take the effectiveness of light absorption into account and it is thus, strictly speaking, an “internal” quantum efficiency. [...]
  § II Theoretical Model: Analysis of the quantum dynamics of a set of chromophores interacting with both weak intensity light and vibrational degrees of freedom requires that the chromophore system be coupled to both a quantum radiation field and a quantum phonon field. This results in a complex set of equations of motion for the electronic density matrix. We present each component of the full simulations here in some detail, starting from the excitation dynamics of a single chromophore and noting that each additional element may be seen as contributing an additional set of terms to the density matrix evolution equation.
  § II.1 System Hamiltonian: We follow the standard approach for single-photon absorption in which each chromophore $k$ is modeled as a simple two-level system, setting the ground state energy to zero and the excited state energy to $E_{k}^{(0)}$ . Unless otherwise stated, this chromophore excited state energy is taken to be the energy of the isolated (gas phase) chromophore, in absence of coupling to phonons, i.e., with no additional reorganization energy due to the protein. For a monomer we have the diagonal Hamiltonian $\displaystyle H_{s}^{(1)}\equiv H_{D}=\left[\begin{array}[]{cc}E^{(0)}&0\\ 0&0\end{array}\right],$ while for a dimeric pair of two-level chromophores we add the dipole-dipole coupling $J$ between the two singly excited states of the dimer. [...]
  § V Summary discussion and outlook: We have presented a full quantum description of the dynamics of photon absorption by pigment-protein complexes driven by multi-mode pulses of coherent states. A quantum optical master equation derived from QSDE equations of motion for chromophore excitations driven by quantum noise originating from the continuum of modes associated with the multi-mode pulses [ 26 ] , was combined with a hierarchical set of equations of motion for the electronic excitations coupled to the phonon environment derived from the pigment and protein vibrational degrees of freedom [ 27 ] , to make simulations of photon absorption under realistic pigment-protein conditions that cover the full range of timescales from fs to ns. Applications to models of monomers, dimers and sub-complexes of chlorophyll pigments in LHCII have revealed several key dynamical features that depend on both the parameters defining the radiation coupling to the chromophores and the parameters defining the coupling of the vibrational environment to the chromophores. [...]
[12] QNFO: Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis | https://papers.qnfo.org/papers/re-entry-of-non-markovian-boson-mediated-transport-into-light-harvesting-complex
  Photosynthetic antennae transfer excitation energy with near‑unity efficiency on sub‑picosecond timescales, and modelers must decide whether the computationally expensive non‑Markovian boson‑mediated framework is required or a cheaper Markovian dephasing master equation suffices. Existing applicability tests used parameter ranges broader than experimentally reported values and employed a dimension
  Full text (https://papers.qnfo.org/papers/re-entry-of-non-markovian-boson-mediated-transport-into-light-harvesting-complex), excerpts of its own sections:
  § 1. Introduction: Photosynthetic organisms convert sunlight into chemical free energy after funnelling excitation through pigment networks with efficiencies approaching $100\%$ on sub‑picosecond excitation‑energy‑transfer (EET) timescales. [...]
  § 5. Results: All numerical values follow directly from the derivations in Section 4. 1. **Optimal dephasing rate:** $\Gamma^{*}= \Delta$, ranging from $110$ to $180\ \mathrm{cm^{-1}}$. 2. **Optimal hopping rate:** $k^{*}=V^{2}/\Delta$, ranging from $13.89$ to $51.14\ \mathrm{cm^{-1}}$ across the experimental box. 3. **Transfer time:** $\tau_{T}=0.1039\text{–}0.3823\ \mathrm{ps}$, with the representative value $0.2336\ \mathrm{ps}$. 4. **Single‑hop efficiency:** $\eta=0.999001$. 5. **Memory ratios:** $R_{\mathrm{fast}}\in[0.26,0.96]$, $R_{\mathrm{slow}}\in[2.6,9.6]$. 6. **Sensitivity:** Across the full experimentally allowed box, $R_{\mathrm{slow}}$ always exceeds $0.5$, while $R_{\mathrm{fast}}$ can be below $0.5$ only for the smallest $V$ values. **Projection.** If the re‑entry criterion holds ($R\gtrsim0.5$), the non‑Markovian framework predicts a shift of the optimal dephasing rate $\delta\Gamma^{*}$ that scales as $\delta\Gamma^{*}/\Gamma^{*}\sim R$. [...]
  § 6. Discussion: **Limitations.** - The analysis relies on a two‑site toy model; real light‑harvesting complexes involve multiple sites, static disorder, and multiple hopping pathways, so the single‑hop efficiency $\eta$ represents an upper bound. - The thresholds for $R$ are conventions; alternative choices would shift the transitional window but not the robust conclusion that slow vibrational modes demand a non‑Markovian treatment. - The Haken–Strobl rate formula assumes weak system‑bath coupling; strong coupling would require the exact non‑Markovian treatment. **Failure modes.** 1. **Bimodal baths.** A bath with both fast and slow components would invalidate a single $\tau_{B}$; a spectral‑density‑weighted ratio would be needed. 2. **Strong coupling.** Violation of the weak‑coupling assumption would render $k(\Gamma)$ inaccurate, necessitating the exact non‑Markovian treatment. 3. **Resonant vibronic bridges.** If specific vibrational modes act as resonant bridges rather than as a memory bath, the dephasing‑based timescale analysis may underestimate coherent contributions highlighted in [7]. [...]
  § 8. Conclusion: We formulated and applied a quantitative timescale‑based re‑entry test for the non‑Markovian boson‑mediated transport framework [9] in photosynthetic light‑harvesting. Using experimentally reported FMO dimer parameters ($V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$) we derived $\Gamma^{*}=\Delta$, $k^{*}=V^{2}/\Delta$, $\tau_{T}=0.1039\text{–}0.3823\ \mathrm{ps}$, and a single‑hop efficiency ceiling $\eta=0.999001$. Comparing $\tau_{T}$ with bath correlation times spanning $0.1\!-\!1\ \mathrm{ps}$ yields memory ratios $R$ that place fast solvent‑like modes in a transitional window and slow intramolecular modes firmly in the non‑Markovian sector. Sensitivity analysis over the full experimentally reported ranges confirms that $R>0.5$ persists for all realistic slow‑mode scenarios. Consequently, the boson‑mediated non‑Markovian framework re‑enters light‑harvesting modelling precisely when $\tau_{B}\gtrsim0.5\,\tau_{T}$, and it predicts a memory‑scaled shift of the optimal dephasing rate, a hypothesis that can be tested by full‑scale simulations. [...]
[13] QNFO: Non-Markovian Hamiltonian Dynamics of Boson-Mediated Energy Transfer | https://papers.qnfo.org/papers/non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer
  Photosynthetic light-harvesting complexes exhibit near-unity quantum efficiency at physiological temperatures, a phenomenon that defies classical thermodynamic expectations and challenges standard quantum decoherence models. This “warm quantum” behavior suggests that biological systems have evolved mechanisms to protect fragile electronic coherence against the intense thermal noise of their enviro
  Full text (https://papers.qnfo.org/papers/non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer), excerpts of its own sections:
  § Non-Markovian: Hamiltonian Dynamics of Boson-Mediated Energy Transfer
  § Addressing: the Warm Quantum Paradox in Photosynthetic Complexes **Author:** Rowan Brad Quni-Gudzinas **Contact:** rowan.quni@outlook.com **ORCID:** 0009-0002-4317-5604 **ISNI:** 0000000526456062 **URL:** https://papers.qnfo.org/papers/non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer/ **Date:** 2026-01-27 **Version:** 1.0 **Abstract**: Photosynthetic light-harvesting complexes exhibit near-unity quantum efficiency at physiological temperatures, a phenomenon that defies classical thermodynamic expectations and challenges standard quantum decoherence models. This “warm quantum” behavior suggests that biological systems have evolved mechanisms to protect fragile electronic coherence against the intense thermal noise of their environment. We propose a unified theoretical framework where bosonic fields (phonons) act not as disruptive noise, but as structured “signals” that direct fermionic workers (excitons) through complex energy landscapes. [...]
  § 1.1 The Warm Quantum Paradox: The fundamental anomaly of quantum biology lies in the coexistence of delicate quantum phenomena and the chaotic thermal disorder of living systems. In classical thermodynamics, the probability of ordered energy transfer decreases rapidly as temperature rises, yet photosynthetic complexes like the Fenna-Matthews-Olson (FMO) protein achieve energy transfer efficiencies exceeding 99% at 300 K. Standard quantum mechanical models predict that at these temperatures, thermal fluctuations should destroy quantum superposition states within femtoseconds, reducing transport to a slow, incoherent random walk (Engel et al., 2007). However, experimental evidence consistently shows that excitation energy traverses the pigment-protein complex with remarkable speed and directionality, suggesting that the system operates in a regime that is neither purely classical nor simply quantum. [...]
  § 1.2 The Boson-Fermion: Signaling Hypothesis To reconcile this paradox, we propose a conceptual reframing of the energy transfer process based on a strict division of labor between quantum statistics. In this framework, the bosonic fields (photons and phonons) function as the “control signals” of the system, while the fermionic entities (electrons and excitons) act as the “workers” that execute physical changes. The absorption of a photon initiates the process, but it is the structured phonon bath—the vibrational modes of the protein scaffold—that directs the resulting exciton toward the reaction center (del Rey et al., 2013). [...]
  § 5.0 Results: II: The Synthetic Regime (Superconductivity)
  § 7.1 Summary of Findings: This study has systematically deconstructed the “Warm Quantum Paradox” of photosynthesis, proposing and validating a “Boson-Fermion Signaling” framework that resolves the apparent conflict between quantum coherence and thermal disorder. By moving beyond static Hilbert space representations to a dynamic, non-Markovian Hamiltonian formalism, we have demonstrated that the protein environment does not merely perturb the system but actively directs it. Our simulations confirm that the “noise” in these systems is actually a structured “boson signal”—a phonon field tuned to specific resonances that guides excitonic “workers” through the energy landscape with >95% efficiency (Engel et al., 2007). Furthermore, we have successfully mapped these biological principles to the realm of condensed matter physics, showing that driven bosonic fields can analogously enhance superconducting pairing potentials.