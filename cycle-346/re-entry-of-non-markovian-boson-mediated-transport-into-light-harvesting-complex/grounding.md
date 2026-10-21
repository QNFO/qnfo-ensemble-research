# Grounding block - source: rem-rev-ba7dd338-1693-47e4-98dd-5a4e884e7fa1

## Research idea

Re-entry from 10.5281/zenodo.18382696: in light-harvesting complexes?

Post-publication revision of the published paper "Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis" (version 2.5.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 9 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 9, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

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

**Transient thermal‑grating probing.** 

**Noise‑assisted transport in FMO.** Reference [2] reports EET efficiencies above $95\%$ in the FMO complex, establishing the relevance of dephasing‑assisted transport (DAT) for light‑harvesting.

**Exciton‑coupling magnitudes.** We adopt the absolute ranges $V\in[50,75]\ \mathrm{cm^{-1}}$ and $\Delta\in[110,180]\ \mathrm{cm^{-1}}$ as representative parameters for the FMO BChl 3–4 dimer.

**Atomistic energy‑funnelling timescales.** 

**Quantum nuclear effects on rates.** 

**Ultrafast single‑molecule spectroscopy.** 

**Multiplex‑network perspective on transport.** The multiplex‑network framework introduces layered transport processes and provides an analogy for exciton‑phonon layered dynamics, motivating the memory‑ratio criterion as a layered‑network metric [3].

**Fundamental role of noise‑assisted transport.** A theoretical analysis identifies the key mechanisms by which dephasing noise suppresses destructive interference and raises transport efficiency, and derives the optimal dephasing condition $\Gamma^{*}=\Delta$ for a two‑site model [8].

**Non‑Markovian boson‑mediated framework.** The boson‑mediated non‑Markovian framework retains bath memory and is the target framework whose applicability we assess [9].

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
| $V$ | $[50,75]\ \mathrm{cm^{-1}}$ | Excitonic coupling magnitude reported in [4] |
| $\Delta$ | $[110,180]\ \mathrm{cm^{-1}}$ | Site‑energy difference reported in [4] |
| $\kappa$ | $1\ \mathrm{ps^{-1}}$ | Trap rate used in atomistic energy‑funnelling study [5] |
| $\tau_{e}$ | $1\ \mathrm{ns}$ | Exciton lifetime reported in [5] |
| $\tau_{B}$ | $[0.1,\,1]\ \mathrm{ps}$ | Fast solvent‑like modes observed in single‑molecule spectroscopy [7]; slow intramolecular modes assumed $\tau_{B}=1\ \mathrm{ps}$ |
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
R_{\mathrm{fast}} = \frac{0.1\ \mathrm{ps}}{\tau_{T}} \in \left[\frac{0.1}{0.3823},\frac{0.1}{0.1039}\right]=[0.262,0.96322302],
\]

\[
R_{\mathrm{slow}} = \frac{1\ \mathrm{ps}}{\tau_{T}} \in \left[\frac{1}{0.3823},\frac{1}{0.1039}\right]=[2.6161613,9.6322302].
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
- One could argue that the importance of non‑Markovian effects is already established by [6] and [7]; however, importance does not imply that the specific boson‑mediated framework adds predictive value.  
- Multiplex‑network analysis in [3] shows that layered transport metrics can exhibit sharp transitions; our memory‑ratio plays an analogous role for exciton‑phonon layers.  
- The noise‑assisted mechanisms identified in [8] are recovered by the optimal dephasing condition $\Gamma^{*}=\Delta$, confirming consistency with established theory.  

**Open questions.** (i) What is the exact prefactor linking $\delta\Gamma^{*}$ to $R$? (ii) How does the memory‑ratio criterion generalize to multi‑site networks with path‑dependent $\tau_{T}$? (iii) Can experimental stroboscopic measurements resolve the predicted backflow signatures in vivo?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** The primary users are theoretical chemists, biophysicists, and engineers modelling excitation‑energy transfer in natural or artificial light‑harvesting systems. The memory‑ratio rule provides a quantitative decision point: if $\tau_{B}\gtrsim0.5\,\tau_{T}$, allocate resources to implement the non‑Markovian boson‑mediated framework [9]; otherwise a Markovian master equation suffices.

**(b) Technology readiness.** This work is purely analytical and has not undergone peer review; it resides at Technology Readiness Level 2. Analytical studies never exceed TRL 3.

**(c) Smallest next experiment or calculation.** A full non‑Markovian simulation of the seven‑site FMO Hamiltonian (including experimentally derived spectral densities [5]) that computes (i) transient population backflow amplitudes and (ii) the shift in the optimal dephasing rate. The hypothesis is falsified if the computed corrections are $<1\%$ of the Markovian predictions for $R\ge0.5$.

**(d) Engineering and computational constraints.**  
- **Spectral‑density data.** Accurate $\tau_{B}$ requires high‑resolution spectral densities from atomistic simulations or ultrafast spectroscopy [1, 7].  
- **Computational load.** A realistic FMO simulation using the non‑Markovian framework typically requires on the order of $10^{4}$ CPU‑hours (uncertainty factor $\approx2$).  
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
- Version 2.4.0 (2026-10-20, from 2.3.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Appendix B. Claim attribution. references 9 -> 9. length 2895 -> 3015 words.
- Version 2.5.0 (2026-10-21, from 2.4.0): revised against the current literature, re-reviewed and re-verified. references 9 -> 9. length 3185 -> 2853 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.0-refs-extend). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 12 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Incoherent Energy Transfer within Light-harvesting Complexes. arXiv:physics/9904052. https://arxiv.org/abs/physics/9904052
[2] Superradiance Transition in Photosynthetic Light-Harvesting Complexes. arXiv:1111.5443. https://arxiv.org/abs/1111.5443
[3] Quantum entanglement in photosynthetic light harvesting complexes. arXiv:0905.3787. https://arxiv.org/abs/0905.3787
[4] Delocalized excitons in natural light harvesting complexes. arXiv:1804.09711. https://arxiv.org/abs/1804.09711
[5] Quantum entanglement phenomena in photosynthetic light harvesting complexes. arXiv:1012.4059. https://arxiv.org/abs/1012.4059
[6] Ultrafast Energy Relaxation in Single Light-Harvesting Complexes. arXiv:1511.04936. https://arxiv.org/abs/1511.04936
[7] Identifying the quantum correlations in light-harvesting complexes. arXiv:0912.5112. https://arxiv.org/abs/0912.5112
[8] Dimerization-assisted energy transport in light-harvesting complexes. arXiv:1002.0496. https://arxiv.org/abs/1002.0496
[9] Bloch-Redfield equations for modeling light-harvesting complexes. arXiv:1408.2726. https://arxiv.org/abs/1408.2726

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

arXiv:2608.13813v3 | Operator-Level Description of Transient Thermal Grating Dynamics Across Transport Regimes
arXiv:0910.4153v2 | Noise-assisted energy transfer in quantum networks and light-harvesting complexes
arXiv:2006.03435v1 | Extracting the multimodal fingerprint of urban transportation networks
arXiv:1312.5352v2 | Exciton coupling induces vibronic hyperchromism in light-harvesting complexes
arXiv:1307.0886v2 | Atomistic study of energy funneling in the light-harvesting complex of green sulfur bacteria
arXiv:2501.02212v1 | Nuclear quantum effects slow down the energy transfer in biological light-harvesting complexes
arXiv:1511.04936v1 | Ultrafast Energy Relaxation in Single Light-Harvesting Complexes
arXiv:0901.4454v2 | Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport

## QNFO corpus context (Vectorize)

QNFO: Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis | https://papers.qnfo.org/papers/re-entry-of-non-markovian-boson-mediated-transport-into-light-harvesting-complex
QNFO: Non-Markovian Hamiltonian Dynamics of Boson-Mediated Energy Transfer | https://papers.qnfo.org/papers/non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2608.13813v3 | Operator-Level Description of Transient Thermal Grating Dynamics Across Transport Regimes
  Transient thermal grating (TTG) experiments provide a powerful means of probing material properties and heat-transport dynamics at small spatiotemporal scales through the temporal response to a spatially periodic excitation. However, quantitative interpretation of the measured transient requires a forward model that consistently connects energy deposition, subsequent heat transport, and the detect
  Full text (https://ar5iv.labs.arxiv.org/html/2608.13813v3), excerpts of its own sections:
  § Submission history: From: Slobodanka Galovic [ view email ] [v1] Thu, 13 Aug 2026 22:53:12 UTC (796 KB) [v2] Tue, 1 Sep 2026 10:18:14 UTC (1,148 KB) [v3] Sun, 18 Oct 2026 08:02:48 UTC (1,240 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Operator-Level Description of Transient Thermal Grating Dynamics Across Transport Regimes, by Slobodanka Galovic and Steva Jacimovski View PDF view license
  § Current browse context:: physics.app-ph < prev | next > new | recent | 2026-08 Change to browse by: physics
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[2] arXiv:0910.4153v2 | Noise-assisted energy transfer in quantum networks and light-harvesting complexes
  We provide physically intuitive mechanisms for the effect of noise on excitation energy transfer (EET) in networks. Using these mechanisms of dephasing-assisted transport (DAT) in a hybrid basis of both excitons and sites, we develop a detailed picture of how noise enables energy transfer with efficiencies well above $90%$ across the Fenna-Matthew-Olson (FMO) complex, a type of light harvesting mo
  Full text (https://arxiv.org/html/0910.4153v2), excerpts of its own sections:
  § 1 Introduction: The early stages of natural photosynthesis are able to capture and transport incident light energy with nearly $100\%$ efficiency, and a clear understanding of these processes could be immensely valuable for optimizing the efficiency of artificial light-harvesting devices  [ 1 ] . Ultrafast nonlinear spectroscopy has been used to probe energy transfer dynamics in the Fenna-Matthew-Olson (FMO) complex  [ 4 , 5 , 6 ] , a crucial part of the photosynthetic system of green sulphur bacteria. Recently, further experiments at physiological temperatures have been performed [ 7 ] . The FMO complex is an example of a pigment-protein complex (PPC), a network through which electronic excitations on individual pigments can migrate via excitonic couplings. It functions as a type of molecular ‘wire’ that funnels light energy captured in the chlorosome antennae to a reaction center (RC) where the energy is used to initiate chemical reactions  [ 8 ] . [...]
  § 2 The Network model: Following previous theoretical descriptions of PPCs  [ 22 , 26 , 27 ] , we consider the PPCs as networks composed of distinct sites, one of which receives a single initial excitation, while another is connected to the RC. The network of $N$ sites is described by the coherent hopping Hamiltonian $H=\sum_{j=1}^{N}\hbar\omega_{j}\sigma_{j}^{+}\sigma_{j}^{-}+\sum_{j\neq l}\hbar v_{j,l}(\sigma_{j}^{-}\sigma_{l}^{+}+\sigma_{j}^{+}\sigma_{l}^{-}),$ (1) where $\sigma_{j}^{+}=\mathinner{|{j}\rangle}\mathinner{\langle{0}|}$ and $\sigma_{j}^{-}=\mathinner{|{0}\rangle}\mathinner{\langle{j}|}$ are raising and lowering operators for site $j$ , the state $|j\rangle$ denotes one excitation in site $j$ and $|0\rangle$ is the zero exciton state. The local site energies are $\hbar\omega_{j}$ , and $v_{j,l}$ are the coherent tunnelling amplitude between the sites $j$ and $l$ . We do not assume any particular form for the microscopic coupling that generates these tunneling amplitudes and we therefore treat them as free parameters when considering abstract networks as we do in section 3 . [...]
  § 3 The fully-connected network: We shall show in the next few sections how the combination of inter-site coherence, interference of tunnelling amplitudes, and energetic disorder can all conspire to drive strong DAT. For clarity, we begin by presenting each mechanism separately in simple network models in which these effects can be isolated. The first system we will consider is the fully-connected network (FCN). [...]
  § 6 Conclusions: We have revisited the basic mechanisms by which pure dephasing noise can open up or suppress pathways through the energy landscape of a quantum network, and have shown how these processes can dramatically increase the eficiency of EET relative to their noiseless evolution. Using these insights, we contructed a hybrid basis for analysing the FMO dynamics and indicated the key pathways which are responsible for the inefficiency of the EET in the absence of noise. For excitations to propagate efficienctly, these pathways must either be avoided or inhibited, and we have shown within a fully Markovian approach how pure dephasing noise acheives this, and how it effects each of the principal pathsways individually. As the identification of the transport-suppressing pathways is made without any reference to the noise model, we believe that any noise model that enhances tranport must more or less carry out this strategy of supresing the inefficient paths and enhancing the direct relaxation channels. [...]
[3] arXiv:2006.03435v1 | Extracting the multimodal fingerprint of urban transportation networks
  Urban mobility increasingly relies on multimodality, combining the use of bicycle paths, streets, and rail networks. These different modes of transportation are well described by multiplex networks. Here we propose the overlap census method which extracts a multimodal profile from a city's multiplex transportation network. We apply this method to 15 cities, identify clusters of cities with similar
  Full text (https://arxiv.org/html/2006.03435v1), excerpts of its own sections:
  § 1. RESEARCH QUESTION AND HYPOTHESIS: The infrastructure of different modes of transportation can be described as a mathematical object, the multiplex transport network ( Morris and Barthelemy, 2012 ; Strano et al., 2012 ; Barthelemy et al., 2013 ; Battiston et al., 2014 ; Gallotti and Barthelemy, 2014 ; De Domenico et al., 2014 ; Strano et al., 2015 ; Aleta et al., 2017 ; Lee et al., 2017 ) . A city’s multiplex transport network contains the layer of streets and other coevolving network layers, such as the bicycle or the rail networks, which together constitute the multimodal transportation backbone of a city. Due to the car-centric development of most cities ( Jacobs, 1961 ) , streets form the most developed layers ( Gössling et al., 2016 ; Szell, 2018 ) and define or strongly limit other layers: For example, sidewalks are by definition footpaths along the side of a street and make up a substantial part of a city’s pedestrian space ( Gössling et al., 2016 ) . Similarly, most bicycle paths are part of a street or are built along the side. [...]
  § 2. METHODS AND DATA: We acquired urban transportation networks from multiple cities around the world, defined by their administrative boundaries, using OSMnx ( Boeing, 2017 ) . These data sets are of high quality ( Haklay, 2010 ; Girres and Touya, 2010 ) in terms of correspondence with municipal open data ( Ferster et al., 2019 ) and completeness ( Barbosa-Filho et al., 2017 ) . The various analyzed urban areas and their properties are reported in Table 1 . Figure 1 shows the different network layers for Manhattan, one of our analyzed cities. [...]
  § 3. FINDINGS: Figure 2: (a) Schematic of multiplex layers in a city (left) and its transformation to the overlap census (right). In the overlap census, the vertical red line gives a visual separation of the left from the right half where nodes become active in the street layer. High spikes in the right half indicate car-centricity. (b) Clusters of cities based on similarity of their overlap census. We find six different clusters using a k-means algorithm (coloured areas), which explain more than $90\%$ of the variance. (c) Overlap census for cities in each cluster. The first one corresponds to Amsterdam (the city with most active nodes in bicycle-only configurations). The Copenhagen-Manhattan-Barcelona-Portland city cluster has many active nodes in pedestrian-only and bicycle-only configurations, representing an active mobility city. The clusters of Los Angeles-Bogota and Mexico-Beihai-Jakarta are car-centric. [...]
[4] arXiv:1312.5352v2 | Exciton coupling induces vibronic hyperchromism in light-harvesting complexes
  The recently suggested possibility that weak vibronic transitions can be excitonically enhanced in light-harvesting complexes is studied in detail. A vibronic exciton dimer model which includes ground state vibrations is investigated using multi-configuration time-dependent Hartree method with a parameter set typical to photosynthetic light-harvesting complexes. Absorption spectra are discussed in
  Full text (https://arxiv.org/html/1312.5352v2), excerpts of its own sections:
  § 1 Introduction: In photosynthesis light absorption and charge separation take place in specialised multi-chromophoric systems. While the reaction centre (RC) complexes, where the primary charge separation occurs, are very similar in different photosynthetic systems, the light-harvesting antennas show a wide variety [ 1 ] . Clearly, it is possible to optimise absorption of light and make excitation transport to RC efficient in many different ways. One of the strategies used in most of the photosynthetic systems is to organise the pigments energetically in an energy funnel with the RC in the bottom of the sink [ 2 ] . In addition, the pigment molecules are usually close enough to enable sufficient resonant interaction and thereby fast excitation transport. Such general optimisation strategies are widely reported and well understood in photosynthetic antenna systems. A result of the relatively dense packing of the pigment molecules in the antenna complexes is the emergence of delocalised Frenkel exciton states  [ 3 , 4 , 5 , 6 ] . [...]
  § 2.1 Frenkel Exciton Hamiltonian: In the following we will use the Frenkel exciton Hamiltonian describing coupled electronic (zero, $|0\rangle$ , and one-exciton, $|m\rangle$ , space) and nuclear degrees of freedom, $\mathbf{Q}=\{\mathbf{Q}_{m}\}$ , [ 3 ] $\displaystyle H_{\rm agg}(\mathbf{Q})$ $\displaystyle=$ $\displaystyle H^{(0)}(\mathbf{Q})+H^{(1)}(\mathbf{Q})\,,$ (1) $\displaystyle H^{(0)}(\mathbf{Q})$ $\displaystyle=$ [...]
  § 3 Results and Discussion: In the following application the case of two sites (vibronic heterodimer, $m=(D,A)$ ) will be considered. The parameters are chosen to mimic the situation in the FMO complex. A number of studies have proposed electronic Hamiltonian of the complex, based on modelling of a set of spectroscopic observables. For a review see [ 54 ] . There is a general agreement that the BChl 3 and 4 have the lowest site energies. The transition energy difference is proposed to be from about 110 to 180 cm -1  . Excitonic coupling between these two molecules is negative with values from about -50 to -75 cm -1   [ 29 ] . Fluorescence line narrowing spectroscopy has revealed that at around 180 cm -1  there are a few vibrational modes in the FMO lowest energy BChl with a total Huang-Rhys factor 0.03 [ 27 ] . We point out that the analogous experiments with BChl in triethylamine give a somewhat higher value of 0.04 [ 28 ] . Having these parameters in mind we formulate our vibronic dimer as follows. [...]
  § 4 Summary: We have carried out a thorough comparison of OPA and exact calculations of vibronic excitons in a dimer model. We found that the general behaviour of the calculated absorption spectra are surprisingly similar despite of the radically different energy level structure in the two models. Multi-mode effects have been discussed in dependence on the mode parameters. In the case of negative coupling, which is relevant for the FMO complex, most oscillator strength is concentrated in a transition to a state of essentially electronic character such that no pronounced effect on the spectrum arises. Calculations of the fluorescence spectra show that the Huang Rhys factors obtained from fluorescence spectroscopy of light-harvesting complexes with significant excitonic couplings, need to be corrected. Depending on the excitonic coupling strength and detuning, the correction can be as large as 100%. At the same time, the observed frequencies are not affected if measured at low temperature where the transitions from higher energy levels are not giving any significant contribution.
[5] arXiv:1307.0886v2 | Atomistic study of energy funneling in the light-harvesting complex of green sulfur bacteria
  Phototrophic organisms such as plants, photosynthetic bacteria and algae use microscopic complexes of pigment molecules to absorb sunlight. Within the light-harvesting complexes, which frequently have several functional and structural subunits, the energy is transferred in the form of molecular excitations with very high efficiency. Green sulfur bacteria are considered to be amongst the most effic
  Full text (https://arxiv.org/html/1307.0886v2), excerpts of its own sections:
  § I Introduction: Figure 1: Photosynthetic apparatus. A , Cartoon of light-harvesting complex in green sulfur bacteria. The bacteria transform solar photons into chemical energy. Sunlight absorbed by the chlorosome is transferred in the form of an exciton through the baseplate and Fenna-Matthews-Olson (FMO) complexes subsequently to the reaction center. A snapshot of the model structure is also shown. B , Atomistic model with corresponding length scales. The atomistic model is composed of a double wall roll for the chlorosome (Roll A: 1620 (=60 $\times$ 27) BChl c sites and Roll B: 2160 (=80 $\times$ 27) BChl c sites), baseplate (64 BChl a sites) and 6 FMO trimer complexes (144 (=24 $\times$ 6) BChl a sites). Photosynthetic bacteria are among the simplest organisms on Earth which use sunlight as their main energy source [ 1 ] . To collect solar energy these bacteria exploit light-harvesting complexes (LHC), aggregates of pigment molecules, which absorb photons and transfer the associated energy at the submicron scale. [...]
  § I.1 Molecular aggregate model: A single LHC of Chlorobium tepidum contains 200–250 thousand BChl molecules [ 47 , 19 , 2 ] . Most of these molecules are found in the chlorosome. The model we have created is shown in Fig. 1 , it is composed of 3988 pigments and represents all the functional units of LHC in green sulfur bacteria, excluding the reaction center. In our model (Fig. 1 B ) a double wall roll aggregate with diameter of about 16 nm and length of about 21 nm, represents the chlorosome. Several possible structural arrangements of BChls in the chlorosome have been investigated theoretically and experimentally [ 48 , 49 , 50 , 51 , 52 , 53 , 54 ] . Here we use the structure of Ref. [ 52 ] , obtained from a triple mutant bacteria and characterized with nuclear magnetic resonance and cryo-electron microscopy. This structure is also supported by 2-dimensional polarization fluorescence microscopy experiments [ 55 ] . The microscopic structure of the baseplate has not yet been experimentally verified [ 42 ] . We construct a baseplate lattice as following. [...]
  § I.2 Exciton transfer model: The exciton transfer is modelled with a quantum master equation approach, which includes the coherent, dephasing and relaxation processes, for the open quantum dynamics [ 68 , 69 , 63 , 70 , 71 ] . We solve the quantum master equation to obtain the spacial distribution of the exciton. [...]
  § III Conclusion: The green sulfur bacteria are thought to be an incredibly efficient light processing machine ( cf. purple bacterium in Ref. [ 94 ] ). We studied this system by investigating from all-atoms and a top to bottom approach ( cf. Ref. [ 95 ] ). The excitation energy transfer route was taken from the chlorosome to the reaction center via the baseplate and FMO, under different initiating conditions. Analysis of the atomistic model indicates that resonant energy transfer is maximized given the multichromophoric excitonic coupling which is due to the molecular arrangements of these parts: the green sulfur bacteria are assembled to be most conducive towards efficient excitation energy transfer within the F $\ddot{\mathrm{o}}$ rster energy transfer regime. It was further shown that whether the initial excitations are important in the energy funneling process. Though, the results differ qualitatively within a short time limit (500 fs). None of these scenario’s, however, adversely affect the efficiency of energy transfer and the results converge within the overall timescale (10 ps) [ 23 , 20 ] . [...]
[6] arXiv:2501.02212v1 | Nuclear quantum effects slow down the energy transfer in biological light-harvesting complexes
  We assess how quantum-mechanical effects associated with high-frequency chromophore vibrations influence excitation energy transfer in biological light-harvesting complexes. We begin with a mixed quantum-classical theory that combines a quantum description of the electronic motion with a classical description of the nuclear motion in a way that is consistent with the quantum-classical equilibrium 
  Full text (https://arxiv.org/html/2501.02212v1), excerpts of its own sections:
  § Introduction: Photosynthesis is a process of fundamental importance to life on earth and a source of inspiration for the development of solar fuels. However, there are still some aspects of its mechanism that are open to debate, including the long-standing question of whether biological light harvesting exhibits any quantum effects. [ 1 , 2 , 3 ] For almost two decades, this debate focused on the interpretation of oscillatory signals observed in nonlinear electronic spectroscopy experiments. [ 4 ] These signals were originally attributed to inter-exciton coherences, but a concensus has now emerged that they have a more straightforward vibrational or vibronic origin. [ 5 , 6 ] In recent years, the debate has therefore shifted to consider the quantum effects associated with the vibrations themselves, [ 7 ] which we shall refer to here as “nuclear quantum effects”. Our goal in this article is to contribute to the debate by comparing classical and quantum treatments of the vibrational modes in explicit simulations of the energy transfer in biological light-harvesting complexes. [...]
  § Results: Of the many known biological light-harvesting complexes, we have selected three representative examples: LH2 in purple bacteria, FMO in green sulfur bacteria, and the light-harvesting complex II (LHCII) in spinach. All three systems have been studied extensively, both experimentally and theoretically, and the historical debate about nuclear quantum effects has largely been focused on LH2 and FMO. We will consider the physiologically relevant temperature of $300\text{\,}\mathrm{K}$ in all of our simulations.
  § Light-harvesting complex 2 in purple bacteria: As our first example, we consider the light-harvesting complex 2 (LH2) in purple bacteria. This complex consists of two bacteriochlorophyll rings, which have absorption maxima near 800 nm and 850 nm and are consequently called the B800 and B850 rings. Its structure varies across different species [ 24 ] , and in the following we focus on the octameric complex found in Magnetospirillum molischianum (note that the former generic names Rhodospirillum and Phaeospirillum are often still used in the literature). In total, the complex comprises 24 chromophores embedded in a protein scaffolding, as depicted in Fig.  1 (a) (using the crystal structure from Ref.  25 ). The primary function of the complex is to funnel excitation energy inwards, from B800 to B850, in order to reach a reaction centre near the centre of the B850 ring. [...]
  § Discussion: In conclusion, the main difference between quantum and classical treatments of vibrational motion in light-harvesting complexes is not the direction of energy flow, but instead the rate of energy transfer. More precisely, it is sufficient to treat the vibrational motion classically to obtain the correct long-time equilibrium, but the rate of transfer will generally be overestimated. Renormalizing the Hamiltonian with the VPT provides a simple way to account for this quantum effect. For biologically relevant parameter regimes, the quantum effect on the rate is benign (less than a factor 2), and the delay may be regarded as a quantum correction to an otherwise qualitatively valid classical picture. In reaching these conclusions, we have assumed that the coupling to high-frequency vibrations is weak enough to discard the fluctuations of the renormalized Hamiltonian. This assumption is more questionable for processes involving charge transfer (e.g. [...]
[7] arXiv:1511.04936v1 | Ultrafast Energy Relaxation in Single Light-Harvesting Complexes
  Energy relaxation in light-harvesting complexes has been extensively studied by various ultrafast spectroscopic techniques, the fastest processes being in the sub-100 fs range. At the same time much slower dynamics have been observed in individual complexes by single-molecule fluorescence spectroscopy (SMS). In this work we employ a pump-probe type SMS technique to observe the ultrafast energy rel
  Full text (https://arxiv.org/html/1511.04936v1), excerpts of its own sections:
  § Introduction: Time-resolved studies of primary events in photosynthetic light harvesting have a decades-long tradition. Usually, the fastest processes observed correspond to the time resolution of the experimental techniques available at the time. Recently, the most popular tool to study ultrafast excitation energy transfer with sub-100 fs resolution is two-dimensional electronic spectroscopy (2DES). This technique has been used to study various light-harvesting complexes such as LH2 and LH1 antennas of purple bacteria [ 1 , 2 ] , the FMO protein of green sulphur bacteria [ 3 , 4 ] and the major antenna complex LHCII of higher plants [ 5 ] . It was shown that after an ultrafast excitation of photosynthetic light-harvesting complexes (LHCs) the electronic excitation evolves in a coherent fashion on a 100 fs timescale. These observations sparked a still ongoing debate on the role of quantum coherence in energy transfer in LHCs. However powerful the ultrafast techniques have become, they are fundamentally limited by ensemble averaging. [...]
  § The measurement: The SM2P principle is based on exciting the system by a near-saturating laser pulse and giving it a time window to relax to some off-resonant state before applying a second pulse. By such relaxation the excitation in the system can be saved from the stimulated emission caused by the second pulse, and the overall excitation probability therefore rises with the pulse delay. [...]
  § Conclusions: We have successfully applied the SM2P technique to LH2 complexes of purple bacteria. We have demonstrated that it is possible to observe ultrafast energy relaxation in individual light-harvesting complexes. As such, our work highlights a new possible way to study photosynthetic light-harvesting. We have shown how the relaxation time distribution changes when tuning the excitation wavelength. The observed behaviour can be explained by varying influence of the B800 and B850* states of the LH2 rings, in agreement with previous ultrafast spectroscopy studies. By a numerical calculation we were able to qualitatively explain the shape of the relaxation time distribution as a result of the energetic disorder of the LH2 pigments. The extent of disorder corresponds to the values commonly used in bulk spectroscopy modelling. Our method can be extended to include a detailed excitation wavelength scan, which would enable us to study energy transfer dynamics of single LH2 complexes to an extent similar to bulk transient absorption measurements. [...]
  § Experimental setup: The experimental setup is similar to the one in Ref. [ 8 ] , briefly a 76 MHz Ti:Sapphire laser (Mira 900F, Coherent) is used as a source of 200-250 fs, 4-5 nm spectrally wide pulses centered at 800 nm. By tuning the laser cavity the wavelength can be tuned approx. from 750 nm to 850 nm. The repetition rate is decreased to 2 MHz by a pulse-picker (PulseSelect, APE) to increase the survival time of the complexes and eliminate long-living dark states such as triplet states. The absence of the triplet states is verified by checking the signal drops to half when halving the repetition rate. The two pulses are produced by a home-built Michelson interferometer, the delay between them is scanned by a delay line (Newport) in one of the interferometer arms. The pulse length before the microscope is measured by fringe-resolved autocorrelation [ 30 ] using the same interferometer and focusing the pulses into a BBO crystal (Eksma optics). The pulse spectrum is measured by a spectrometer (OceanOptics). Technical details can be found in the SI. [...]
[8] arXiv:0901.4454v2 | Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport
  Excitation transfer through interacting systems plays an important role in many areas of physics, chemistry, and biology. The uncontrollable interaction of the transmission network with a noisy environment is usually assumed to deteriorate its transport capacity, especially so when the system is fundamentally quantum mechanical. Here we identify key mechanisms through which noise such as dephasing
  Full text (https://arxiv.org/html/0901.4454v2), excerpts of its own sections:
  § I The Network Model: Light-harvesting complexes are typically constituted of multiple chromophores which transform photons into excitons and transport them to a reaction center [ 25 ] . Experimental studies of the exciton dynamics in such systems reveal rich transport dynamics consisting of short-time coherent quantum dynamics which evolve, in the presence of noise into an incoherent population transport which irreversibly transfers excitations to the reaction center. In order to elucidate the basic phenomena clearly without overburdening the description with detail, we consider the relevant complexes as systems composed of several distinct sites, one of which is connected to the chromosomes while another is connected to the reaction center. This complex effective dynamics will then be modelled by a combination of simple Hamiltonian dynamics which describe the coherent exchange of excitations between sites, and local Lindblad terms that take into account the dephasing and dissipation caused by the external environment. [...]
  § II The Fully Connected Network (FCN): The FMO complex can be described by a Hamiltonian in which every site in the network is coupled to every other sites but with site dependent coupling strength [ 19 , 11 ] . The dominant couplings are the nearest neighbour terms, but significant hopping matrix elements exist also between more distant sites. This motivates the study of networks with a high level of connectivity (see also Ref. [ 27 ] for quantum state transfer), and in this section, for simplicity, we will look in detail at a fully connected network (FCN). The FCN is characterised by equal hopping strengths between all sites, i.e. $\hbar v_{j,l}=J$ for any $j\neq l$ . Remarkably, for the case of a uniform network, i.e. one in which $\omega_{j}$ , $\gamma_{j}$ , and $\Gamma_{j}$ are the same on every site, an exact analytical solution can be found for the density matrix of arbitrarily large networks. These exact solutions are obtained by defining a set of collective variables, and the formal development of the solutions is given in the Appendix. [...]
  § II.1 No dissipation, no dephasing: Destructive interference: This case is described by $\gamma_{j}=\Gamma_{j}=0$ and, for simplicity, $\omega_{j}=0$ for any $j=1,\ldots,N$ . The only irreversible process left in this system is the decay of population to the sink from site $N.$ The exact solution (in the Appendix) predicts the striking result that as $t\rightarrow\infty$ the total amount of the excitation that is transferred to the sink is given by $p_{sink}(\infty)=\frac{1}{N-1}\;. [...]
  § VI Concluding remarks: We have analysed transport assisted by dephasing, and more general types of noise, in dissipative networks such as those describing the transport of excitons in photosynthetic complexes [ 19 , 18 ] and also considered the presence of entanglement. We have introduced an analytical technique that allows for the identification of invariant subspaces of network Hamiltonians and therefore the possibility of supporting noise assisted transport. We have further clarified the fundamental mechanisms that lead to this phenomenon and provided simple examples to reveal their basic character. Of key importance are the suppression of destructive interference by dephasing noise, static disorder in energy levels and differences in propagation speed along different paths on the one hand, and the enhanced overlap between sites with dephasing broadened lines on the other. [...]
[9] QNFO: Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis | https://papers.qnfo.org/papers/re-entry-of-non-markovian-boson-mediated-transport-into-light-harvesting-complex
  Photosynthetic antennae transfer excitation energy with near‑unity efficiency on sub‑picosecond timescales, and modelers must decide whether the computationally expensive non‑Markovian boson‑mediated framework is required or a cheaper Markovian dephasing master equation suffices. Existing applicability tests used parameter ranges broader than experimentally reported values and employed a dimension
  Full text (https://papers.qnfo.org/papers/re-entry-of-non-markovian-boson-mediated-transport-into-light-harvesting-complex), excerpts of its own sections:
  § 1. Introduction: Photosynthetic organisms convert sunlight into chemical free energy after funnelling excitation through pigment networks with efficiencies approaching $100\%$ on sub‑picosecond excitation‑energy‑transfer (EET) timescales. [...]
  § 5. Results: All numerical values follow directly from the derivations in Section 4. 1. **Optimal dephasing rate:** $\Gamma^{*}= \Delta$, ranging from $110$ to $180\ \mathrm{cm^{-1}}$. 2. **Optimal hopping rate:** $k^{*}=V^{2}/\Delta$, ranging from $13.89$ to $51.14\ \mathrm{cm^{-1}}$ across the experimental box. 3. **Transfer time:** $\tau_{T}=0.1039\text{–}0.3823\ \mathrm{ps}$, with the representative value $0.2336\ \mathrm{ps}$. 4. **Single‑hop efficiency:** $\eta=0.999001$. 5. **Memory ratios:** $R_{\mathrm{fast}}\in[0.26,0.96]$, $R_{\mathrm{slow}}\in[2.6,9.6]$. 6. **Sensitivity:** Across the full experimentally allowed box, $R_{\mathrm{slow}}$ always exceeds $0.5$, while $R_{\mathrm{fast}}$ can be below $0.5$ only for the smallest $V$ values. **Projection.** If the re‑entry criterion holds ($R\gtrsim0.5$), the non‑Markovian framework predicts a shift of the optimal dephasing rate $\delta\Gamma^{*}$ that scales as $\delta\Gamma^{*}/\Gamma^{*}\sim R$. [...]
  § 6. Discussion: **Limitations.** - The analysis relies on a two‑site toy model; real light‑harvesting complexes involve multiple sites, static disorder, and multiple hopping pathways, so the single‑hop efficiency $\eta$ represents an upper bound. - The thresholds for $R$ are conventions; alternative choices would shift the transitional window but not the robust conclusion that slow vibrational modes demand a non‑Markovian treatment. - The Haken–Strobl rate formula assumes weak system‑bath coupling; strong coupling would require the exact non‑Markovian treatment. **Failure modes.** 1. **Bimodal baths.** A bath with both fast and slow components would invalidate a single $\tau_{B}$; a spectral‑density‑weighted ratio would be needed. 2. **Strong coupling.** Violation of the weak‑coupling assumption would render $k(\Gamma)$ inaccurate, necessitating the exact non‑Markovian treatment. 3. **Resonant vibronic bridges.** If specific vibrational modes act as resonant bridges rather than as a memory bath, the dephasing‑based timescale analysis may underestimate coherent contributions highlighted in [7]. [...]
  § 8. Conclusion: We formulated and applied a quantitative timescale‑based re‑entry test for the non‑Markovian boson‑mediated transport framework [9] in photosynthetic light‑harvesting. Using experimentally reported FMO dimer parameters ($V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$) we derived $\Gamma^{*}=\Delta$, $k^{*}=V^{2}/\Delta$, $\tau_{T}=0.1039\text{–}0.3823\ \mathrm{ps}$, and a single‑hop efficiency ceiling $\eta=0.999001$. Comparing $\tau_{T}$ with bath correlation times spanning $0.1\!-\!1\ \mathrm{ps}$ yields memory ratios $R$ that place fast solvent‑like modes in a transitional window and slow intramolecular modes firmly in the non‑Markovian sector. Sensitivity analysis over the full experimentally reported ranges confirms that $R>0.5$ persists for all realistic slow‑mode scenarios. Consequently, the boson‑mediated non‑Markovian framework re‑enters light‑harvesting modelling precisely when $\tau_{B}\gtrsim0.5\,\tau_{T}$, and it predicts a memory‑scaled shift of the optimal dephasing rate, a hypothesis that can be tested by full‑scale simulations. [...]
[10] QNFO: Non-Markovian Hamiltonian Dynamics of Boson-Mediated Energy Transfer | https://papers.qnfo.org/papers/non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer
  Photosynthetic light-harvesting complexes exhibit near-unity quantum efficiency at physiological temperatures, a phenomenon that defies classical thermodynamic expectations and challenges standard quantum decoherence models. This “warm quantum” behavior suggests that biological systems have evolved mechanisms to protect fragile electronic coherence against the intense thermal noise of their enviro
  Full text (https://papers.qnfo.org/papers/non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer), excerpts of its own sections:
  § Non-Markovian: Hamiltonian Dynamics of Boson-Mediated Energy Transfer
  § Addressing: the Warm Quantum Paradox in Photosynthetic Complexes **Author:** Rowan Brad Quni-Gudzinas **Contact:** rowan.quni@outlook.com **ORCID:** 0009-0002-4317-5604 **ISNI:** 0000000526456062 **URL:** https://papers.qnfo.org/papers/non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer/ **Date:** 2026-01-27 **Version:** 1.0 **Abstract**: Photosynthetic light-harvesting complexes exhibit near-unity quantum efficiency at physiological temperatures, a phenomenon that defies classical thermodynamic expectations and challenges standard quantum decoherence models. This “warm quantum” behavior suggests that biological systems have evolved mechanisms to protect fragile electronic coherence against the intense thermal noise of their environment. We propose a unified theoretical framework where bosonic fields (phonons) act not as disruptive noise, but as structured “signals” that direct fermionic workers (excitons) through complex energy landscapes. [...]
  § 1.1 The Warm Quantum Paradox: The fundamental anomaly of quantum biology lies in the coexistence of delicate quantum phenomena and the chaotic thermal disorder of living systems. In classical thermodynamics, the probability of ordered energy transfer decreases rapidly as temperature rises, yet photosynthetic complexes like the Fenna-Matthews-Olson (FMO) protein achieve energy transfer efficiencies exceeding 99% at 300 K. Standard quantum mechanical models predict that at these temperatures, thermal fluctuations should destroy quantum superposition states within femtoseconds, reducing transport to a slow, incoherent random walk (Engel et al., 2007). However, experimental evidence consistently shows that excitation energy traverses the pigment-protein complex with remarkable speed and directionality, suggesting that the system operates in a regime that is neither purely classical nor simply quantum. [...]
  § 1.2 The Boson-Fermion: Signaling Hypothesis To reconcile this paradox, we propose a conceptual reframing of the energy transfer process based on a strict division of labor between quantum statistics. In this framework, the bosonic fields (photons and phonons) function as the “control signals” of the system, while the fermionic entities (electrons and excitons) act as the “workers” that execute physical changes. The absorption of a photon initiates the process, but it is the structured phonon bath—the vibrational modes of the protein scaffold—that directs the resulting exciton toward the reaction center (del Rey et al., 2013). [...]
  § 5.0 Results: II: The Synthetic Regime (Superconductivity)
  § 7.1 Summary of Findings: This study has systematically deconstructed the “Warm Quantum Paradox” of photosynthesis, proposing and validating a “Boson-Fermion Signaling” framework that resolves the apparent conflict between quantum coherence and thermal disorder. By moving beyond static Hilbert space representations to a dynamic, non-Markovian Hamiltonian formalism, we have demonstrated that the protein environment does not merely perturb the system but actively directs it. Our simulations confirm that the “noise” in these systems is actually a structured “boson signal”—a phonon field tuned to specific resonances that guides excitonic “workers” through the energy landscape with >95% efficiency (Engel et al., 2007). Furthermore, we have successfully mapped these biological principles to the realm of condensed matter physics, showing that driven bosonic fields can analogously enhance superconducting pairing potentials.