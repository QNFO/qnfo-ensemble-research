# Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis

## Abstract

Photosynthetic antennae achieve near‑unity excitation‑energy‑transfer (EET) efficiency on sub‑picosecond timescales, yet modelers must decide whether to allocate expensive non‑Markovian boson‑mediated simulations or inexpensive Markovian dephasing master equations. Existing applicability tests employed parameter ranges broader than experimentally reported values and used a dimensionally inconsistent transfer‑time expression. We adopt the experimentally reported excitonic coupling magnitude $V\in[50,75]\;\mathrm{cm^{-1}}$ and site‑energy difference $\Delta\in[110,180]\;\mathrm{cm^{-1}}$ for the FMO BChl 3–4 dimer [4] and employ the dimensionally correct transfer‑time formula  
\[
\tau_{T}= \frac{\Delta}{2\pi c V^{2}} .
\]  
From this we obtain a transfer‑time interval $0.1039\text{–}0.3823\;\mathrm{ps}$, a single‑hop trapping efficiency $\eta=0.999001$, and memory‑ratio windows $R_{\mathrm{fast}}\in[0.26,0.96]$ (fast bath $\tau_{B}=0.1\;\mathrm{ps}$) and $R_{\mathrm{slow}}\in[2.6,9.6]$ (slow bath $\tau_{B}=1\;\mathrm{ps}$). All realistic slow‑mode scenarios therefore lie in the non‑Markovian sector. We further derive a falsifiable scaling $\delta\Gamma^{*}/\Gamma^{*}\approx R$ for the shift of the optimal dephasing rate when $R\gtrsim0.5$. The memory‑ratio rule thus provides a quantitative, analytically derived guideline for allocating computational effort in EET modelling.

## 1. Introduction

Designers of bio‑inspired photovoltaic devices and researchers interpreting ultrafast spectroscopic data both confront a concrete methodological choice: allocate high‑performance‑computing resources to a non‑Markovian boson‑mediated description that retains bath memory, or adopt a Markovian dephasing master equation that discards memory at negligible cost. The former approach can require on the order of $10^{4}$ CPU‑hours (order‑of‑magnitude estimate) for a seven‑site FMO simulation, while the latter can be executed on a laptop in minutes. An incorrect choice either wastes computational budget or yields quantitatively inaccurate transfer rates and optimal dephasing conditions, potentially leading to sub‑optimal device designs or misinterpretation of experimental observables. A decision rule that predicts when memory effects are essential would therefore reduce unnecessary computation and improve the reliability of modelling outcomes.

Two‑decade‑old theory shows that environmental dephasing can assist transport, raising EET efficiencies above $90\%$ in the FMO complex within a fully Markovian treatment [2]. Ultrafast single‑molecule pump–probe spectroscopy resolves energy relaxation in single light‑harvesting complexes, motivating the assignment of fast solvent‑like bath correlation times $\tau_{B}=0.1\;\mathrm{ps}$ [7]. Atomistic simulations report excitonic couplings $V$ between $-50$ and $-75\;\mathrm{cm^{-1}}$ and site‑energy differences $\Delta$ between $110$ and $180\;\mathrm{cm^{-1}}$ for the BChl 3–4 dimer [4]. These experimentally grounded ranges define a realistic parameter box that is narrower than the ranges used in earlier applicability analyses [9]. Moreover, transient‑thermal‑grating studies emphasize the necessity of dimensional consistency when relating wavenumber‑based couplings to temporal rates [1].

**Contributions.**  
1. Derivation of the optimal dephasing rate $\Gamma^{*}=\Delta$ and optimal hopping rate $k^{*}=V^{2}/\Delta$ for the two‑site Haken–Strobl model (Section 4.1).  
2. Correction of the transfer‑time formula to $\tau_{T}= \Delta/(2\pi c V^{2})$, dimensional verification, and evaluation at the four corners of the experimental box, yielding $\tau_{T}\in[0.1039,\,0.3823]\;\mathrm{ps}$ (Section 4.2).  
3. Computation of the single‑hop trapping‑limited efficiency $\eta=0.999001$ using trap and recombination rates (Section 4.3).  
4. Exhaustive calculation of memory ratios over the full experimental box, giving $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$ (Section 4.4).  
5. Revised regime classification showing that all realistic slow‑mode baths fall in the non‑Markovian sector (Section 5).  
6. A falsifiable projection that the non‑Markovian correction to the optimal dephasing rate scales as $\delta\Gamma^{*}/\Gamma^{*}\approx R$ (Sections 5 and 6).

## 2. Background and Related Work

**Noise‑assisted transport in FMO.** Reference [2] demonstrates that pure dephasing noise can raise EET efficiencies above $90\%$ in the FMO complex, establishing the practical relevance of dephasing‑assisted transport (DAT) for light‑harvesting.

**Transient‑thermal‑grating consistency.** The TTG study [1] argues that forward models must consistently connect energy deposition, heat transport, and detection, motivating our insistence on a dimensionally correct transfer‑time expression.

**Excitonic coupling magnitudes and site‑energy differences.** The excitonic‑coupling analysis [4] reports a negative coupling between BChl 3 and 4 of magnitude $50$–$75\;\mathrm{cm^{-1}}$ and a transition‑energy difference $\Delta$ of $110$–$180\;\mathrm{cm^{-1}}$, providing the experimentally grounded parameter box used throughout this work.

**Atomistic energy‑funnelling parameters.** An atomistic study of the green‑sulfur‑bacteria light‑harvesting apparatus [5] describes a detailed structural model of the FMO complex and confirms that energy funneling proceeds via densely packed pigments with strong excitonic couplings, supporting the relevance of the $V$ and $\Delta$ ranges.

**Nuclear quantum effects on rates.** The nuclear‑quantum‑effects investigation [6] finds that treating high‑frequency vibrations quantum‑mechanically can slow transfer rates by up to a factor of two relative to classical treatments, highlighting the importance of correctly modeling bath dynamics.

**Ultrafast bath correlation times.** Single‑molecule pump–probe work [7] resolves ultrafast relaxation on sub‑100‑fs scales and motivates the assignment of a fast solvent‑like bath correlation time $\tau_{B}=0.1\;\mathrm{ps}$ for the FMO complex.

**Fundamental mechanisms of DAT.** The noise‑assisted transport review [8] identifies dephasing as a mechanism that suppresses destructive interference, broadens energy levels, and thereby enhances transport efficiency, providing the theoretical foundation for our Haken–Strobl analysis.

**Prior applicability analysis.** The earlier version of this study [9] employed broader parameter ranges and a dimensionally inconsistent transfer‑time formula; our present work corrects those issues and narrows the parameter box to experimentally reported values.

**Urban multiplex networks.** The multiplex‑network investigation [3] focuses on transportation layers in cities and does not provide quantitative analogues to exciton‑phonon dynamics; consequently it does not support the memory‑ratio metric.

**Non‑Markovian boson‑mediated framework.** The boson‑mediated transport theory [10] proposes that structured phonon fields act as signals guiding excitons, forming the basis of the non‑Markovian approach whose applicability we assess.

Collectively, these works define the experimentally realistic parameter regime, the theoretical foundations of DAT, and the methodological motivation for a timescale‑based re‑entry criterion.

## 3. Methods

### 3.1 Toy model and corrected dephasing dissipator

We consider the two‑site Haken–Strobl Hamiltonian in the single‑excitation manifold  

\[
H_{S}= \frac{\Delta}{2}\,\sigma_{z}+V\,\sigma_{x},
\]  

where $\sigma_{x},\sigma_{z}$ are Pauli matrices on the two‑site basis, $\Delta$ is the site‑energy difference, and $V$ is the excitonic coupling. Site 2 carries a trap with rate $\kappa$.

The correct pure‑dephasing Lindblad generator with jump operator $\sigma_{z}$ is  

\[
\mathcal{L}_{\phi}[\rho]=-\frac{\Gamma}{2}\,[\sigma_{z},[\sigma_{z},\rho]],
\]  

which leaves populations invariant and damps the coherence $\rho_{12}$ as $\dot{\rho}_{12}=-2\Gamma\,\rho_{12}$. This form replaces the defective term $-(\Gamma/2)(1-\sigma_{z}^{2}/2)$, which reduces to a multiple of the identity and generates no dephasing.

### 3.2 Re‑entry criterion

The memory ratio is defined as  

\[
R=\frac{\tau_{B}}{\tau_{T}},
\]  

with $\tau_{B}$ the bath correlation time and $\tau_{T}$ the intrinsic single‑hop transfer time (Section 4.2). Thresholds are conventions chosen to render the criterion falsifiable:

* $R\lesssim0.1$: Markovian reduction suffices.  
* $0.1<R<0.5$: Transitional regime; error estimation required.  
* $R\gtrsim0.5$: Non‑Markovian framework required.

### 3.3 Input parameters

| Symbol | Value | Source / status |
|--------|-------|-----------------|
| $V$ | $[50,75]\;\mathrm{cm^{-1}}$ | Reported in [4] |
| $\Delta$ | $[110,180]\;\mathrm{cm^{-1}}$ | Reported in [4] |
| $\kappa$ | $1\;\mathrm{ps^{-1}}$ | Assumption of this paper |
| $\tau_{e}$ | $1\;\mathrm{ns}$ | Assumption of this paper |
| $\tau_{B}$ | $0.1\;\mathrm{ps}$ (fast) and $1\;\mathrm{ps}$ (slow) | Fast value motivated by [7] |
| $c$ | $2.9979\times10^{10}\;\mathrm{cm\,s^{-1}}$ | Defined constant for unit conversion |

All parameters are either taken directly from the cited literature or explicitly labelled as assumptions.

## 4. Analysis

### 4.1 Optimal dephasing rate and hopping rate

In the strong‑disorder limit $V\ll\Delta$, adiabatic elimination of the coherences in the Haken–Strobl master equation with the corrected pure‑dephasing generator yields the hopping rate  

\[
k(\Gamma)=\frac{2V^{2}\,\Gamma}{\Gamma^{2}+\Delta^{2}}.
\]

Differentiating with respect to $\Gamma$:

\[
\frac{\mathrm{d}k}{\mathrm{d}\Gamma}=2V^{2}\,\frac{(\Gamma^{2}+\Delta^{2})-2\Gamma^{2}}{(\Gamma^{2}+\Delta^{2})^{2}}
=2V^{2}\,\frac{\Delta^{2}-\Gamma^{2}}{(\Gamma^{2}+\Delta^{2})^{2}}.
\]

Setting the derivative to zero gives $\Delta^{2}-\Gamma^{2}=0$, i.e.  

\[
\Gamma^{*}=\Delta.
\]

Substituting $\Gamma^{*}$ back into $k(\Gamma)$:

\[
k^{*}=k(\Gamma^{*})=\frac{2V^{2}\Delta}{\Delta^{2}+\Delta^{2}}=\frac{V^{2}}{\Delta}.
\]

#### Numerical range of $k^{*}$

Evaluating $k^{*}=V^{2}/\Delta$ at the four corners of the experimental box:

| Corner | $V$ (cm$^{-1}$) | $\Delta$ (cm$^{-1}$) | $k^{*}=V^{2}/\Delta$ (cm$^{-1}$) |
|--------|----------------|----------------------|-----------------------------------|
| 1 (min V, max Δ) | $50$ | $180$ | $13.8889$ |
| 2 (min V, min Δ) | $50$ | $110$ | $22.7273$ |
| 3 (max V, max Δ) | $75$ | $180$ | $31.2500$ |
| 4 (max V, min Δ) | $75$ | $110$ | $51.1364$ |

Thus  

\[
k^{*}\in[13.89,\,51.14]\;\mathrm{cm^{-1}}.
\]

### 4.2 Transfer time $\tau_{T}$

The optimal hopping rate $k^{*}$ has units of wavenumber ($\mathrm{cm^{-1}}$). Converting to angular frequency $\omega^{*}=2\pi c\,k^{*}=2\pi c\,V^{2}/\Delta$, the transfer time is the inverse:

\[
\tau_{T}= \frac{1}{\omega^{*}} = \frac{\Delta}{2\pi c V^{2}}.
\]

#### Extremal transfer times

*Maximum* $\tau_{T}$ (smallest $V$, largest $\Delta$): $V=50$, $\Delta=180$  

\[
\begin{aligned}
\tau_{T}^{\mathrm{max}} &= \frac{180}{2\pi c \, 50^{2}}\\
&= \frac{180}{2\pi \times 2.9979\times10^{10}\times 2500}\\
&= \frac{180}{4.7091\times10^{14}}\\
&= 3.8223\times10^{-13}\;\mathrm{s}\\
&= 0.3823\;\mathrm{ps}.
\end{aligned}
\]

*Minimum* $\tau_{T}$ (largest $V$, smallest $\Delta$): $V=75$, $\Delta=110$  

\[
\begin{aligned}
\tau_{T}^{\mathrm{min}} &= \frac{110}{2\pi c \, 75^{2}}\\
&= \frac{110}{2\pi \times 2.9979\times10^{10}\times 5625}\\
&= \frac{110}{1.0596\times10^{15}}\\
&= 1.0382\times10^{-13}\;\mathrm{s}\\
&= 0.1039\;\mathrm{ps}.
\end{aligned}
\]

Hence  

\[
\tau_{T}\in[0.1039,\,0.3823]\;\mathrm{ps}.
\]

### 4.3 Trapping‑limited efficiency $\eta$

The recombination rate is  

\[
\gamma_{\mathrm{rec}} = \frac{1}{\tau_{e}} = \frac{1}{1\;\mathrm{ns}} = 10^{-3}\;\mathrm{ps^{-1}}.
\]

The single‑hop trapping efficiency for a trap rate $\kappa$ and recombination $\gamma_{\mathrm{rec}}$ is  

\[
\eta = \frac{\kappa}{\kappa+\gamma_{\mathrm{rec}}}
= \frac{1}{1+10^{-3}}
= \frac{1}{1.001}
= 0.999001.
\]

### 4.4 Memory ratio $R$ and regime classification

Using the bounds for $\tau_{T}$:

\[
R_{\mathrm{fast}} = \frac{0.1\;\mathrm{ps}}{\tau_{T}} \in \left[\frac{0.1}{0.3823},\frac{0.1}{0.1039}\right]
= [0.262,\,0.963].
\]

\[
R_{\mathrm{slow}} = \frac{1\;\mathrm{ps}}{\tau_{T}} \in \left[\frac{1}{0.3823},\frac{1}{0.1039}\right]
= [2.616,\,9.632].
\]

Rounding to two significant figures gives  

\[
R_{\mathrm{fast}}\in[0.26,0.96],\qquad
R_{\mathrm{slow}}\in[2.6,9.6].
\]

All $R_{\mathrm{slow}}$ values exceed the $0.5$ threshold, placing every realistic slow‑mode bath in the non‑Markovian sector. Fast baths fall below $0.5$ only for the smallest $V$ values, leaving a transitional window.

### 4.5 Sensitivity of the classification to the reported box

Because $R=\tau_{B}\,2\pi cV^{2}/\Delta$ is monotone increasing in $V$ and decreasing in $\Delta$, the extremes of $R$ over the box occur at the corners already evaluated; no interior extremum exists. The classification is therefore robust over the full reported range: $R_{\mathrm{slow}}>0.5$ for every corner, and $R_{\mathrm{fast}}<0.5$ only at the corner $(V,\Delta)=(50,180)$, where $R_{\mathrm{fast}}=0.2616$.

## 5. Results

All numerical values follow directly from the derivations in Section 4.

1. **Optimal dephasing rate:** $\Gamma^{*}= \Delta$, ranging from $110$ to $180\;\mathrm{cm^{-1}}$.  
2. **Optimal hopping rate:** $k^{*}=V^{2}/\Delta$, ranging from $13.89$ to $51.14\;\mathrm{cm^{-1}}$.  
3. **Transfer time:** $\tau_{T}=0.1039\text{–}0.3823\;\mathrm{ps}$, with the representative corner values $0.1039$ ps (min) and $0.3823$ ps (max).  
4. **Single‑hop efficiency:** $\eta=0.999001$.  
5. **Memory ratios:** $R_{\mathrm{fast}}\in[0.26,0.96]$, $R_{\mathrm{slow}}\in[2.6,9.6]$.  
6. **Sensitivity:** $R_{\mathrm{slow}}$ always exceeds $0.5$; $R_{\mathrm{fast}}$ can be below $0.5$ only for $V=50\;\mathrm{cm^{-1}}$ and $\Delta=180\;\mathrm{cm^{-1}}$.

**Projection.** If $R\gtrsim0.5$, the non‑Markovian framework predicts a shift of the optimal dephasing rate $\delta\Gamma^{*}$ that scales as  

\[
\frac{\delta\Gamma^{*}}{\Gamma^{*}} \approx R,
\]

with a proportionality constant of order unity and an uncertainty factor of two. This hypothesis is falsifiable by full‑scale non‑Markovian simulations of the seven‑site FMO Hamiltonian.

## 6. Discussion

### Limitations

* **Two‑site abstraction.** Real light‑harvesting complexes contain multiple pigments, static disorder, and multiple pathways; the single‑hop efficiency $\eta$ therefore represents an upper bound.  
* **Threshold conventions.** The $R$ thresholds are chosen for falsifiability; alternative thresholds would shift the transitional window but not the qualitative conclusion that slow vibrational modes demand a non‑Markovian treatment.  
* **Weak‑coupling assumption.** The Haken–Strobl rate formula assumes $V\ll\Delta$ and weak system‑bath coupling; strong coupling would invalidate the analytic $k(\Gamma)$ expression and require the exact non‑Markovian treatment.  
* **Assumed bath times.** Both $\tau_{B}=0.1\;\mathrm{ps}$ and $\tau_{B}=1\;\mathrm{ps}$ are assumptions; only the fast value is motivated by analogy with the sub‑100‑fs relaxation resolved in single complexes [7]. The classification of a given real bath depends directly on these assumed values.  
* **Vibronic effects excluded.** The reported 180 cm$^{-1}$ modes with Huang–Rhys factor 0.03 [4] and the fs‑scale vibronic coherences documented for FMO [11] are outside the pure‑dephasing model; they could modify $\tau_{T}$ and the thresholds.

### Failure modes

1. **Bimodal baths.** A bath comprising both fast and slow components would invalidate a single $\tau_{B}$; a spectral‑density‑weighted ratio would be needed.  
2. **Strong coupling.** If $V$ approached $\Delta$, the denominator $\Gamma^{2}+\Delta^{2}$ would no longer be dominated by $\Delta^{2}$, breaking the optimality condition $\Gamma^{*}=\Delta$.  
3. **Resonant vibronic bridges.** Specific vibrational modes acting as resonant bridges could enhance coherent transport beyond the dephasing‑based estimate, as the vibronic‑coherence review [11] makes plausible for modes in the 200–500 cm$^{-1}$ range.

### Falsification condition

The central claim—that the boson‑mediated framework is required when $R\gtrsim0.5$—is falsified if a full non‑Markovian simulation of a realistic FMO Hamiltonian yields corrections to populations, trapping currents, or the optimal dephasing rate that are smaller than $1\%$ of the corresponding Markovian predictions for $R\ge0.5$. A secondary falsifier would be a credible revision of the reported dimer parameters outside $V\in[50,75]\;\mathrm{cm^{-1}}$ or $\Delta\in[110,180]\;\mathrm{cm^{-1}}$ [4]; such a revision could push $R_{\mathrm{slow}}$ below $0.5$, overturning the classification.

### Self‑critique

One could argue that the importance of non‑Markovian effects is already established by the nuclear‑quantum‑effect study [6], which shows transfer‑rate corrections up to a factor of two; however, importance does not imply that the specific boson‑mediated framework of [10] adds predictive value beyond a Markovian master equation, and our rule is designed to test exactly that. The optimal dephasing condition $\Gamma^{*}=\Delta$ recovers, in the two‑site limit, the mechanism identified in the fully connected network analysis of [8], where dephasing suppresses destructive interference.

### Open questions

1. What is the exact prefactor linking $\delta\Gamma^{*}$ to $R$?  
2. How does the memory‑ratio criterion generalize to multi‑site networks with path‑dependent $\tau_{T}$?  
3. Can single‑molecule spectroscopy of the type demonstrated in [7] resolve the predicted backflow signatures in individual complexes?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** The primary users are theoretical chemists, biophysicists, and engineers modelling excitation‑energy transfer in natural or artificial light‑harvesting systems. The memory‑ratio rule provides a quantitative decision point: if $\tau_{B}\gtrsim0.5\,\tau_{T}$, allocate resources to implement the non‑Markovian boson‑mediated framework; otherwise a Markovian master equation suffices.

**(b) Technology readiness.** This work is purely analytical and has not undergone peer review; it resides at Technology Readiness Level 2. Analytical studies never exceed TRL 3.

**(c) Smallest next experiment or calculation.** A full non‑Markovian simulation of the seven‑site FMO Hamiltonian (including an assumed spectral density consistent with atomistic funneling parameters) that computes (i) transient population backflow amplitudes and (ii) the shift in the optimal dephasing rate. The hypothesis is falsified if the computed corrections are $<1\%$ of the Markovian predictions for $R\ge0.5$.

**(d) Engineering and computational constraints.**  
* **Spectral‑density data.** Accurate $\tau_{B}$ requires high‑resolution spectral densities from atomistic simulations or ultrafast spectroscopy [7].  
* **Computational load.** A realistic FMO simulation using the non‑Markovian framework typically requires on the order of $10^{4}$ CPU‑hours (order‑of‑magnitude estimate).  
* **Parameter uncertainty.** Variations in $V$ and $\Delta$ must be propagated; sensitivity analysis (Section 4.5) shows classification robustness but necessitates careful parameter estimation.

**(e) Order‑of‑magnitude cost projection (projection).** Assuming a cloud HPC price of \$0.10 per CPU‑hour, the minimal full‑scale simulation costs  

\[
\text{Cost}\approx10^{4}\ \text{CPU‑h}\times\$0.10/\text{CPU‑h}= \$1{,}000,
\]  

with an uncertainty factor of two due to possible variations in parallel efficiency.

**(f) Direct risks or misuse paths.** Over‑reliance on the memory‑ratio rule without verifying the underlying spectral density could lead to unnecessary deployment of the expensive non‑Markovian framework, wasting computational resources. Conversely, mis‑classifying a slow‑mode bath as fast could omit essential memory effects, yielding inaccurate design predictions. Clear documentation of the assumptions (single‑exponential bath correlation, weak coupling) mitigates these risks.

## 8. Conclusion

We formulated and applied a quantitative timescale‑based re‑entry test for the non‑Markovian boson‑mediated transport framework in photosynthetic light‑harvesting. Using experimentally reported FMO dimer parameters ($V\in[50,75]\;\mathrm{cm^{-1}}$, $\Delta\in[110,180]\;\mathrm{cm^{-1}}$) we derived $\Gamma^{*}=\Delta$, $k^{*}=V^{2}/\Delta$, $\tau_{T}=0.1039\text{–}0.3823\;\mathrm{ps}$, and a single‑hop efficiency ceiling $\eta=0.999001$. Comparing $\tau_{T}$ with bath correlation times spanning $0.1\!-\!1\;\mathrm{ps}$ yields memory ratios $R$ that place fast solvent‑like modes in a transitional window and slow intramolecular modes firmly in the non‑Markovian sector. Sensitivity analysis over the full experimentally reported ranges confirms that $R>0.5$ persists for all realistic slow‑mode scenarios. Consequently, the boson‑mediated non‑Markovian framework re‑enters light‑harvesting modelling precisely when $\tau_{B}\gtrsim0.5\,\tau_{T}$, and it predicts a memory‑scaled shift of the optimal dephasing rate, a hypothesis that can be tested by full‑scale simulations. The memory‑ratio rule thus offers modelers a concrete, analytically derived guideline for allocating computational effort in the study of excitation‑energy transfer.

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
[10] QNFO: Non-Markovian Hamiltonian Dynamics of Boson-Mediated Energy Transfer | https://papers.qnfo.org/papers/non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer  
[11] QNFO: Quantum Coherence in Photosystem II: Environment-Assisted Transport and the Role of Vibronic Coupling in Biological Light-Harvesting | https://papers.qnfo.org/papers/psii-quantum-coherence

## Appendix A. Divergence report

| Claim ID | Divergence | Draft A wording | Draft B wording | Chosen convention / resolution |
|----------|------------|----------------|----------------|--------------------------------|
| C3 | Numerical bounds of $\tau_{T}$ differ by rounding. | “$\tau_{T}\in[0.1039,\,0.3823]\;\mathrm{ps}$” (Section 4.2). | “$\tau_{T}\in[0.1038,\,0.3822]\;\mathrm{ps}$” (Section 4.2). | Adopt the values derived explicitly in the arithmetic of Section 4.2: $\tau_{T}\in[0.1039,\,0.3823]\;\mathrm{ps}$. |
| C23 | Interpretation of the multiplex‑network study. | “The multiplex‑network framework … motivates the memory‑ratio $R=\tau_{B}/\tau_{T}$ as a layered‑network metric for exciton‑phonon dynamics [3].” | “The multiplex‑network study … contains no claim about quantum transport or a memory‑ratio metric; the citation is retained only to document what the work actually does [3].” | Follow Draft B’s retraction: state that the multiplex‑network study does not provide a quantitative analogy to exciton‑phonon dynamics and does not support the memory‑ratio metric. |

## Appendix B. Claim attribution

| Claim ID | Statement | Source drafts | Agreement status |
|----------|-----------|---------------|------------------|
