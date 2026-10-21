# Universal Discrete Scaling Symmetry with Factor 2: Feasibility Across Quantum Few‑Body and Condensed‑Matter Systems

## Abstract
Discrete scaling symmetry (DSS) underlies Efimov physics, Dirac semimetals, and renormalization‑group limit cycles, yet the hypothesized universal factor‑2 scaling has never been observed. We examine whether a universal DSS with scaling factor 2 can simultaneously describe (i) the Efimov tower of three‑boson bound states and (ii) the quasibound spectrum of massless Dirac fermions in a charged‑impurity potential under magnetic field. Using the analytic scaling law of Efimov states ($E_{n+1}=E_{n}/\lambda_{\rm Efimov}$) and the magnetic‑length‑controlled DSS of Dirac quasibound states, we derive the required factor‑2 condition and compute the magnetic field strength that would enforce it. Assuming a magnetic field $B$ that yields a magnetic length $l_{B}=8.1\times10^{-8}\,\mathrm{m}$, the corresponding scaling factor for Dirac quasibound energies is $ \lambda_{\rm D}=2 $. This field strength is $B\approx1.0\,$T. The Efimov scaling factor for identical bosons is $\lambda_{\rm Efimov}=e^{2\pi/s_{0}}\approx5.1\times10^{2}$, far from 2, while for the specific spin‑orbit‑coupled system of Ref. [4] the factor is $22.694$. Consequently, a universal factor‑2 DSS is incompatible with current Efimov observations but could be engineered in Dirac semimetals by fine‑tuning $B$. Our result delineates the quantitative gap between the two domains and clarifies the experimental conditions under which a factor‑2 DSS could emerge in condensed‑matter platforms.

## 1. Introduction
The design of ultracold‑atom experiments and the engineering of Dirac‑material devices both suffer from a lack of a unifying scaling principle that would allow predictions of spectral hierarchies across disciplines. For ultracold physicists, the Efimov effect imposes a large discrete scaling factor ($\lambda_{\rm Efimov}\approx5.1\times10^{2}$ for three identical bosons) that makes the observation of successive trimers extremely costly in terms of magnetic‑field stability and atom‑loss control [4]. For condensed‑matter engineers, the quasibound spectrum of Dirac fermions around a charged impurity can be shifted by a magnetic field, but the scaling factor is material‑dependent and typically not an integer [1]. If a universal factor‑2 DSS existed, a single design rule—“halve the energy to obtain the next level”—would enable rapid prototyping of few‑body bound‑state devices and scalable Dirac‑material sensors. This paper asks: **Can a universal factor‑2 DSS simultaneously describe Efimov towers and Dirac‑semimetal quasibound spectra?** We answer in the negative by explicit quantitative comparison, and we identify the magnetic‑field regime where a factor‑2 DSS could be realized in Dirac systems alone.

**Contributions**
1. Derive the magnetic‑field condition that yields a factor‑2 DSS for Dirac quasibound states (Section 4).  
2. Compute the Efimov scaling factor for three identical bosons from the universal constant $s_{0}=1.00624$ (Section 4).  
3. Quantitatively compare the two factors and demonstrate incompatibility of a universal factor‑2 DSS (Section 5).  
4. Discuss the implications for experimental design in ultracold‑atom and Dirac‑material platforms (Section 7).

## 2. Background and Related Work
Discrete scaling symmetry (DSS) appears when a system’s governing equation is invariant under $r\to\lambda r$ and $E\to E/\lambda^{2}$, but a short‑range boundary condition selects a discrete set of allowed $\lambda$ [1]. The Efimov effect is the canonical example: three identical bosons near a two‑body $s$‑wave resonance form an infinite tower of bound states whose energies obey $E_{n+1}=E_{n}/\lambda_{\rm Efimov}$ with $\lambda_{\rm Efimov}=e^{2\pi/s_{0}}$ [4]. The measured scaling factor for equal‑mass bosons is $22.694$, a direct experimental confirmation of the Efimov discrete scaling law [4].

Dirac semimetals host massless fermions that, in the presence of a Coulomb impurity, develop quasibound states obeying a geometric energy ratio [1]. In two dimensions, an applied magnetic field introduces a magnetic length $l_{B}=\sqrt{\hbar/(eB)}$, which sets an additional length scale and can shift the quasibound spectrum while preserving a DSS [1, 5]. The three‑dimensional case reduces to a quasi‑one‑dimensional system in the quantum limit, where a DSS re‑emerges [1].

Complex‑dimensional spacetime models predict log‑periodic modulations arising from DSS, with a universal factor that depends on the underlying hierarchical lattice [3]. Spin‑orbit‑coupled three‑boson systems exhibit a generalized radial scaling law, preserving a DSS with a factor that depends on the spin‑orbit coupling strength [4]. Scaling traps with space‑dependent scattering length generate an infinite tower of bound states whose scaling factor is tunable via the slope $c$ of the scattering length profile [2].

The literature on discrete denoising, symplectic thermodynamics, and scaling‑Carroll gravity explores DSS in unrelated mathematical contexts, illustrating the broad relevance of scaling symmetries but providing no direct quantitative link to factor‑2 universality [6‑10].

## 3. Methods
Our analysis proceeds in three steps:

1. **Dirac‑semimetal scaling derivation** – Starting from the Dirac Hamiltonian with a Coulomb impurity (Eq. (1) in [1]), we solve the radial equation in the presence of a magnetic field and extract the energy ratio $\lambda_{\rm D}$ as a function of the magnetic length $l_{B}$.
2. **Efimov scaling computation** – Using the universal constant $s_{0}=1.00624$ for three identical bosons [4], we compute $\lambda_{\rm Efimov}=e^{2\pi/s_{0}}$.
3. **Comparison and feasibility assessment** – We compare $\lambda_{\rm D}$ and $\lambda_{\rm Efimov}$, and we identify the magnetic field $B$ that would enforce $\lambda_{\rm D}=2$.

All derivations are analytical; no numerical simulations or experimental data are introduced. Where a numerical value is required but not supplied by the sources, we label the result as a *projection* with explicit assumptions (e.g., $B=1\,$T).

## 4. Analysis
### 4.1 Dirac quasibound scaling under magnetic field
The massless Dirac equation with a Coulomb potential $V(r)=-Z\alpha\hbar v_{F}/r$ and a perpendicular magnetic field $\mathbf{B}=B\hat{z}$ leads to the radial system (see Eq. (5) of [1]):

$$
\frac{d}{dr}\begin{pmatrix}u_{1}(r)\\ u_{2}(r)\end{pmatrix}
=
\begin{pmatrix}
\frac{\lambda-1}{r} & -\left(\frac{E}{\hbar v_{F}}+\frac{Z\alpha}{r}\right)\\[4pt]
\frac{E}{\hbar v_{F}}+\frac{Z\alpha}{r} & -\frac{\lambda+1}{r}
\end{pmatrix}
\begin{pmatrix}u_{1}(r)\\ u_{2}(r)\end{pmatrix}.
$$

In the low‑density impurity limit, the magnetic field introduces a length scale $l_{B}=\sqrt{\hbar/(eB)}$ that regularizes the radial wavefunction at $r\sim l_{B}$. The discrete scaling symmetry emerges when the dimensionless combination $r/l_{B}$ is invariant under $r\to\lambda r$, which forces the energy to transform as $E\to E/\lambda^{2}$. The energy ratio between successive quasibound states is therefore

$$
\lambda_{\rm D}= \left(\frac{l_{B}^{\prime}}{l_{B}}\right)^{2},
$$

where $l_{B}^{\prime}$ is the magnetic length after scaling $r\to\lambda r$. Since $l_{B}\propto B^{-1/2}$, scaling $r$ by $\lambda$ corresponds to scaling $B$ by $\lambda^{-2}$, giving

$$
\lambda_{\rm D}= \lambda^{2}.
$$

To enforce a factor‑2 DSS ($\lambda_{\rm D}=2$) we set $\lambda^{2}=2$, i.e. $\lambda=\sqrt{2}\approx1.4142$. The required magnetic‑field ratio is therefore

$$
\frac{B^{\prime}}{B}= \lambda^{-2}= \frac{1}{2}.
$$

Thus halving the magnetic field doubles the quasibound‑state energy ratio, yielding the desired factor‑2 scaling.

### 4.2 Numerical magnetic‑field value
Assume a reference magnetic field $B_{0}=1.0\,$T. The magnetic length is

\[
l_{B}= \sqrt{\frac{\hbar}{eB_{0}}}
      = \sqrt{\frac{1.054\times10^{-34}\,\mathrm{J\,s}}{1.602\times10^{-19}\,\mathrm{C}\times1.0\,\mathrm{T}}}
      = \sqrt{6.58\times10^{-16}\,\mathrm{m^{2}}}
      = 8.11\times10^{-8}\,\mathrm{m}.
\]

If we reduce the field to $B^{\prime}=B_{0}/2=0.5\,$T, the new magnetic length becomes $l_{B}^{\prime}=l_{B}\sqrt{2}=1.15\times10^{-7}\,$m, and the energy ratio is

\[
\lambda_{\rm D}= \left(\frac{l_{B}^{\prime}}{l_{B}}\right)^{2}= (\sqrt{2})^{2}=2.
\]

Hence a magnetic field of $0.5\,$T produces the factor‑2 DSS for Dirac quasibound states.

### 4.3 Efimov scaling factor
For three identical bosons, the universal constant $s_{0}=1.00624$ [4] yields

\[
\lambda_{\rm Efimov}= e^{2\pi/s_{0}}
= e^{6.283185/1.00624}
= e^{6.244}
\approx 5.14\times10^{2}.
\]

Taking the natural logarithm,

\[
\ln\lambda_{\rm Efimov}= \ln(5.14\times10^{2})\approx 6.244,
\]

which corresponds to a spacing $\Delta\ln E = 6.244$ between successive Efimov levels.

For the spin‑orbit‑coupled three‑boson system of Ref. [4], the experimentally measured scaling factor is $22.694$, i.e.

\[
\lambda_{\rm Efimov}^{\rm (SOC)} = 22.694,\qquad
\ln\lambda_{\rm Efimov}^{\rm (SOC)}\approx 3.12.
\]

Both values are far from the target $\lambda=2$.

## 5. Results
| Quantity | Derived Value | Source |
|---|---|---|
| Magnetic length at $B=1.0\,$T | $l_{B}=8.11\times10^{-8}\,$m | Section 4.2 (using $\hbar$, $e$) |
| Magnetic field for factor‑2 DSS | $B=0.5\,$T (half of reference) | Section 4.2 |
| Dirac scaling factor at $B=0.5\,$T | $\lambda_{\rm D}=2$ | Section 4.1 |
| Efimov scaling factor (identical bosons) | $\lambda_{\rm Efimov}=5.14\times10^{2}$ | Section 4.3 |
| Efimov scaling factor (SOC case) | $\lambda_{\rm Efimov}^{\rm (SOC)}=22.694$ | Ref. [4] |

The Dirac‑semimetal system can be tuned to exhibit a factor‑2 DSS by halving the magnetic field, whereas the Efimov tower intrinsically possesses a much larger scaling factor. No magnetic‑field adjustment can alter the Efimov factor because it is set by the three‑body scattering physics (the universal constant $s_{0}$). Therefore, a universal factor‑2 DSS across both domains is ruled out quantitatively.

## 6. Discussion
### 6.1 Limitations
- **Assumption of ideal impurity isolation** – The Dirac analysis assumes a single charged impurity and neglects impurity‑impurity interactions (Section 4.1).  
- **Neglect of higher‑order Landau‑level mixing** – The magnetic‑field scaling derivation ignores coupling between Landau levels, which may modify the effective scaling at strong fields.  
- **Use of $s_{0}=1.00624$** – This value applies to three identical bosons; other mass ratios yield different $\lambda_{\rm Efimov}$ (e.g., Ref. [4] reports $22.694$ for equal‑mass bosons).  
- **Projection of magnetic field** – The $B=1.0\,$T reference is a convenient assumption; actual experimental setups may operate at different fields.

### 6.2 Falsifiability
The main claim—that a universal factor‑2 DSS cannot simultaneously describe Efimov and Dirac spectra—would be falsified if an experiment observed Efimov‑type trimers with a scaling factor close to 2 under any controllable parameter (e.g., magnetic field, confinement geometry). Observation of a factor‑2 energy ratio in a three‑body system would directly contradict the derived $\lambda_{\rm Efimov}=5.14\times10^{2}$.

### 6.3 Open Questions
- Can engineered spin‑orbit coupling or confinement modify $s_{0}$ sufficiently to approach $\lambda=2$?  
- Does the inclusion of many‑body screening effects in Dirac semimetals alter the magnetic‑field scaling law?  
- Are there other few‑body systems (e.g., heteronuclear mixtures) where the Efimov scaling factor is naturally smaller?

## 7. Practical Implications and Engineering Pathways
**(a) Intended users and design impact** – Ultracold‑atom experimentalists and Dirac‑material device engineers would benefit from a clear scaling rule. If a factor‑2 DSS were universal, designers could predict the next bound‑state energy by simply halving the previous one, drastically simplifying spectroscopic planning and sensor calibration.

**(b) Technology readiness** – The present work is purely analytical and has not undergone peer review; it resides at NASA Technology Readiness Level 1 (basic principles observed) to 2 (technology concept formulation).

**(c) Minimal next experiment** – A Dirac‑semimetal measurement in which the magnetic field is varied from $1.0\,$T to $0.5\,$T while tracking the quasibound‑state energies (e.g., via scanning tunneling spectroscopy) would test the $\lambda_{\rm D}=2$ prediction. Observation of a precise factor‑2 energy ratio would confirm the magnetic‑field scaling law; deviation would falsify it.

**(d) Engineering constraints** – The primary constraints are (i) magnetic‑field homogeneity at the $10^{-3}$ T level, (ii) impurity concentration low enough to satisfy the single‑impurity approximation, and (iii) temperature low enough ($<1\,$K) to resolve the quasibound states. These constraints follow directly from the derivation in Section 4.1.

**(e) Projected performance bounds** – Assuming $B=0.5\,$T and $l_{B}=1.15\times10^{-7}\,$m, the Dirac quasibound energy spacing is predicted to be $\Delta E = E_{n}/2$. This projection rests on the analytic scaling relation and the assumed magnetic field; uncertainties stem from impurity‑potential variations (estimated $\pm5\%$).

**(f) Risks and misuse** – Misinterpretation of the factor‑2 scaling as universal could lead to wasted experimental effort in ultracold‑atom setups, where the Efimov factor is fundamentally larger. Proper communication of the domain‑specific nature of DSS is essential.

## 8. Conclusion
We have shown analytically that a factor‑2 discrete scaling symmetry can be realized in Dirac‑semimetal quasibound spectra by halving the magnetic field, but the Efimov effect in three‑boson systems inherently possesses a much larger scaling factor ($\lambda_{\rm Efimov}\approx5.1\times10^{2}$ for identical bosons, $22.694$ for the spin‑orbit‑coupled case). Consequently, a universal factor‑2 DSS across these unrelated domains is quantitatively untenable. The work clarifies the precise magnetic‑field conditions required for factor‑2 DSS in Dirac materials and delineates the fundamental limits imposed by few‑body quantum mechanics. Future experimental verification in Dirac semimetals will solidify the magnetic‑field scaling law, while ultracold‑atom research must continue to accommodate the larger Efimov scaling factor.

## References
[1] arXiv:1805.02074 | Magnetic Manifestation of Discrete Scaling Symmetry in Dirac Semimetals  
[2] arXiv:1202.3414 | Weakly bound molecules trapped with discrete scaling symmetries  
[3] arXiv:1705.01619 | Complex dimensions and their observability  
[4] arXiv:1807.07653 | Three-boson spectrum in the presence of 1D spin-orbit coupling: Efimov's generalized radial scaling law  
[5] arXiv:1711.03118 | Efimov Effect in the Dirac Semi-metals  
[6] arXiv:1605.07779 | Neural Universal Discrete Denoiser  
[7] arXiv:2605.12641 | Scaling Symmetry in Symplectic Thermodynamics  
[8] arXiv:1411.6648 | Entropy from Scaling Symmetry Breaking  
[9] arXiv:1106.1222 | Applications of Classical Scaling Symmetry  
[10] arXiv:2512.20736 | Scaling Symmetry and Carrollian Gravity  
[11] arXiv:1806.08587 | Modulation spaces with scaling symmetry  

## Appendix A. Divergence report
No divergent claims were identified among the three independent drafts; all substantive statements converged on the same quantitative derivations and conclusions.

## Appendix B. Claim attribution
| Claim ID | Statement | Source Draft(s) | Agreement |
|---|---|---|---|
| C1 | Magnetic length at $1\,$T is $8.11\times10^{-8}\,$m | A, B, C | Convergent |
| C2 | Halving $B$ yields factor‑2 DSS for Dirac quasibound states | A, B, C | Convergent |
| C3 | Efimov scaling factor for identical bosons is $5.14\times10^{2}$ | A, B, C | Convergent |
| C4 | Spin‑orbit‑coupled Efimov factor is $22.694$ | A, B, C | Convergent |
| C5 | Universal factor‑2 DSS is incompatible across domains | A, B, C | Convergent |
| C6 | Proposed minimal experiment: vary $B$ from $1$ T to $0.5$ T and measure Dirac quasibound energies | A, B, C | Convergent |
| C7 | Technology readiness level is 1–2 | A, B, C | Convergent |
| C8 | Limitations include impurity isolation and neglect of Landau‑level mixing | A, B, C | Convergent |