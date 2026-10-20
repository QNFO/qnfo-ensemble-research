# Is the Harmonic Oscillator an Infrared Attractor in All Places? A Place‑Resolved Analysis of the Harmonic Paradigm

## Abstract

The universal infrared (IR) attractor claim for the quantum harmonic oscillator (HO) has only been examined over the Archimedean absolute value on ℚ. This work asks whether the attractor status survives under the non‑Archimedean $p$‑adic and adelic norms. We construct a place‑resolved renormalization‑group (RG) framework, define a dimensionless distance $\alpha_v$ from a flowing bosonic system to the HO fixed point for each place $v$, and adopt a geometric $p$‑adic spectrum $E^{(p)}_n=E_0\,p^{-n}$ organized on Bruhat–Tits tree levels. Explicit derivations include (i) verification of the adelic product formula for $x=2/3$, (ii) counting of tree vertices, (iii) comparison of constant Archimedean gaps with geometric $p$‑adic gaps, (iv) exponential RG decay $\alpha_v(\ell)=e^{-\gamma_v\ell}$ with illustrative $\gamma_v=0.1$, and (v) testing a product‑of‑distances linkage hypothesis. The principal result is that attraction can occur in every place but with spectrally distinct fixed points; the adelic product formula constrains amplitudes, not spectra, so no strong spectral linkage exists. Consequently, the Harmonic Paradigm’s attractor thesis is not an Archimedean artifact but also not place‑invariant in a strong sense.

## 1. Introduction

Quantum engineers and theorists rely on the Harmonic Paradigm’s claim that the quantum harmonic oscillator (HO) is the universal infrared (IR) attractor of bosonic systems: generic bosonic models flow toward oscillator‑like behavior at long wavelengths, simplifying design of bosonic error‑correcting codes and quantum batteries. The claim underpins resource‑advantage arguments for bosonic encodings, which report 5–40 × fewer photons and ≈100 × fewer modes than surface‑code alternatives at a logical error rate $p_L=10^{-6}$ [12]. However, the attractor statement implicitly quantifies over a number field equipped with an absolute value. By Ostrowski’s theorem, ℚ admits the usual real absolute value and a family of $p$‑adic absolute values $|\cdot|_p$. The Paradigm’s literature tests only the Archimedean place; its red‑team assessment notes that $p$‑adic structures appear only in the bibliography, not in the core mechanisms [14]. The sharp question is: does the HO remain an IR attractor (a) unchanged, (b) reversed, or (c) structurally transformed when the underlying place changes?

We answer by (i) defining a place‑resolved distance $\alpha_v$ from a flowing system to the HO fixed point, (ii) deriving RG flows toward each fixed point, and (iii) testing whether the adelic product formula imposes a non‑trivial linkage between places. Our conclusion is option (c): attraction exists in every place but with spectrally different fixed points, and adelic constraints bind only amplitudes, not spectra.

## 2. Background and Related Work

**Adelic oscillator.** The adelic program formulates quantum mechanics over the adele ring and introduces an adelic HO whose uncertainty relation is softened; this establishes that an oscillator can be defined adelically, but the supplied summary gives no explicit level formula [8].

**Bicomplex oscillator.** Solving the HO over bicomplex numbers yields eigenvalues and eigenkets, demonstrating that the algebraic oscillator construction survives in a commutative ring with zero divisors [6].

**Non‑commutative oscillator.** Dynamical symmetries and physical equivalence of non‑commutative systems sharing the same spectrum are classified, showing that identical spectra do not guarantee physical equivalence [5].

**Damped oscillator.** A complete solution of the quantum damped HO is provided, establishing dynamical completeness of the solution family, a prerequisite for any fixed‑point language [1].

**Anti‑PT‑symmetric oscillator.** Replacing $\omega\to i\omega$ to obtain the inverted oscillator leads to unbounded eigenvectors and unclear redefinitions, warning that repulsive sectors are delicate [7].

**Semi‑classical measures.** The structure of semi‑classical measures for coupled HO eigenfunctions depends strongly on arithmetic relations between frequencies, indicating that arithmetic (hence place) matters for attractor structure [4].

**Propagator–Fourier equivalence.** Harmonic‑oscillator propagators and fractional Fourier transforms are essentially the same, providing a function‑analytic tool that could be transplanted to $p$‑adic modulation spaces [3].

**Universal attractor template.** Studies of universal attractors in heavy‑ion collisions show that solutions become insensitive to initial conditions, supplying the template for our $\alpha_v(\ell)$ construction [9].

**Universal bosonic mass scale.** A universal mass scale for all $q$‑form fields is reported, illustrating a parallel universality claim in the bosonic sector [11].

**Bosonic code resources.** At $p_L=10^{-6}$, bosonic codes require 5–40 × fewer photons and ≈100 × fewer modes than surface codes, a resource advantage that rests on the attractor premise [12].

**Adelic Cross‑Domain Program.** The program maps physical architecture onto Bruhat–Tits trees, connecting the fine‑structure constant, RG, quantum error correction, and the Efimov effect, providing the geometric setting for our $p$‑adic analysis [13].

**Red‑team assessment.** The assessment notes that the Paradigm’s bibliography invokes Ostrowski’s theorem and $p$‑adic structures, but its core mechanisms are confined to the Archimedean place [14].

## 3. Methods

### 3.1 Places and absolute values

A place $v$ of ℚ is an equivalence class of absolute values. We write $v=\infty$ for the Archimedean place with $|x|_\infty$ the usual absolute value, and $v=p$ for a $p$‑adic place, where $|p^k m|_p=p^{-k}$ for $m$ coprime to $p$. The adelic product formula states
$$
\prod_v |x|_v \;=\; |x|_\infty \prod_{p} |x|_p \;=\;1,
$$
for every non‑zero rational $x$.

### 3.2 The two oscillator fixed points

**Archimedean fixed point.** The standard HO Hamiltonian $H_\infty=\frac{\hat P^2}{2m}+\frac{m\omega^2\hat X^2}{2}$ has spectrum
$$
E^{(\infty)}_n=\hbar\omega\!\left(n+\tfrac12\right),\qquad n=0,1,2,\ldots
$$
with constant spacing $\Delta E_\infty=\hbar\omega$.

**$p$‑adic fixed point (model).** Guided by the tree‑organized picture of the adelic program [8,13], we adopt the geometric ladder
$$
E^{(p)}_n = E_0\,p^{-n},\qquad n=0,1,2,\ldots
$$
as a modeling assumption. The adjacent gap is
$$
\Delta E^{(p)}_n = E^{(p)}_n - E^{(p)}_{n+1}
               = E_0\,p^{-n}\!\left(1-\frac1p\right),
$$
so the gap ratio $\Delta E^{(p)}_n/\Delta E^{(p)}_{n+1}=p$.

The degeneracy of level $n$ equals the number of vertices at distance $n$ from a base vertex on the $(p+1)$‑regular Bruhat–Tits tree:
$$
g_p(0)=1,\qquad g_p(n)=(p+1)p^{\,n-1}\;\;(n\ge1).
$$

### 3.3 Place‑resolved RG flow and attractor distance

For each place $v$, let $\omega_v(\ell)$ be the effective oscillator frequency at RG scale $\ell$, and $\omega_{v,*}$ the fixed‑point value. Linearizing about the fixed point,
$$
\frac{d\omega_v}{d\ell}
   = -\gamma_v\bigl(\omega_v-\omega_{v,*}\bigr),
$$
with solution
$$
\omega_v(\ell)=\omega_{v,*}
               +\bigl(\omega_v(0)-\omega_{v,*}\bigr)
                 e^{-\gamma_v\ell}.
$$
The dimensionless distance from the attractor is
$$
\alpha_v(\ell)\equiv
\frac{|\omega_v(\ell)-\omega_{v,*}|}{\omega_{v,*}}
               =\alpha_v(0)\,e^{-\gamma_v\ell}.
$$
Attraction requires $\gamma_v>0$; repulsion $\gamma_v<0$; structural transformation means $\gamma_v>0$ in both places but the spectra differ in kind.

### 3.4 Adelic linkage test

A strong place‑invariance would demand a product constraint on the distances,
$$
\prod_v \alpha_v(\ell)=\text{const},
$$
for all $\ell$. We test whether the adelic product formula forces such a relation, and we also identify the quantity on which the product formula does bind (amplitudes).

## 4. Analysis

All numbers below are derived from the stated inputs; no external data are used.

**A1. Product formula verification.** Input: $x=2/3$, with $p=2$ and $p=3$.
\[
|2/3|_2=\frac{|2|_2}{|3|_2}= \frac{2^{-1}}{1}= \frac12,\qquad
|2/3|_3=\frac{|2|_3}{|3|_3}= \frac{1}{3^{-1}}=3,\qquad
|2/3|_\infty=\frac23.
\]
Product:
\[
\frac12\times3\times\frac23 = 1.
\]

**A2. Bruhat–Tits vertex counts.** For $p=2$,
\[
N_1=3,\; N_2=3\!\times\!2=6,\; N_3=3\!\times\!4=12,\; N_4=3\!\times\!8=24,
\]
cumulative $S_2(4)=1+3+6+12+24=46$. Closed form $S_p(N)=1+(p+1)\frac{p^{N}-1}{p-1}$ gives $S_2(4)=3\cdot2^{4}-2=46$.

For $p=3$, $N_1=4$, $N_2=12$, $N_3=36$, cumulative $S_3(3)=1+4+12+36=53$.

**A3. Spectral gap comparison.** Normalizing $\hbar\omega=E_0=1$,
\[
\Delta E^{(\infty)}_n = 1\quad\forall n,
\]
\[
\Delta E^{(2)}_0 = \tfrac12,\;
\Delta E^{(2)}_1 = \tfrac14,\;
\Delta E^{(2)}_2 = \tfrac18,\;
\Delta E^{(2)}_3 = \tfrac1{16},
\]
with ratio $2=p$. For $p=3$, gaps are $2/3$, $2/9$, $2/27$, ratio $3$.

**A4. RG decay of $\alpha_v$.** Assume $\gamma_v=0.1$, $\alpha_v(0)=1$.
\[
\alpha_v(20)=e^{-0.1\times20}=e^{-2}\approx0.135335283,
\]
\[
\alpha_v(40)=e^{-4}\approx0.018315639,\qquad
\alpha_v(60)=e^{-6}\approx0.002478752.
\]

**A5. Product‑of‑distances linkage.** With two places $v=\infty$ and $v=2$, equal $\gamma=0.1$ and $\alpha_\infty(0)=\alpha_2(0)=1$,
\[
\prod_v\alpha_v(\ell)=e^{-0.2\ell},
\]
which varies with $\ell$. Constancy would require $\sum_v\gamma_v=0$, e.g. $\gamma_\infty=+0.1$, $\gamma_2=-0.1$, a fine‑tuned scenario not implied by the adelic product formula.

**A6. Amplitude‑level adelic constraint.** For an adelic wavefunction $\Psi(x)$ evaluated at rational $x$, the local amplitudes satisfy
\[
\prod_v |\Psi(x)|_v = 1,
\]
mirroring A1. This binds amplitudes, not eigenvalues, allowing constant Archimedean gaps and geometric $p$‑adic gaps to coexist.

## 5. Results

*R1 (exact).* The adelic product formula holds for $x=2/3$ (A1).

*R2 (exact, model‑based).* Under $E^{(p)}_n=E_0p^{-n}$, the $p$‑adic gap ratio equals $p$ (A3), distinct from the constant Archimedean gap.

*R3 (exact, model‑based).* Vertex counts grow as $(p+1)p^{n-1}$; for $p=2$ the cumulative count through level 4 is 46, for $p=3$ through level 3 is 53 (A2).

*R4 (exact, conditional).* With $\gamma_v=0.1$, $\alpha_v(\ell)=e^{-0.1\ell}$ yields $\alpha_v(20)\approx0.135335$, $\alpha_v(40)\approx0.018316$, $\alpha_v(60)\approx0.002479$ (A4). These are projections based on the assumed linearized flow.

*R5 (exact).* The product‑of‑distances hypothesis fails for generic $\gamma_v$; constancy would require $\sum_v\gamma_v=0$, which the adelic product formula does not enforce (A5).

*R6 (structural).* The adelic product formula constrains amplitudes (A6) but not spectra; thus attraction can exist in each place with spectrally different fixed points, supporting option (c): structural transformation.

## 6. Discussion

**Limitations.** The $p$‑adic level formula $E^{(p)}_n=E_0p^{-n}$ is a modeling assumption; the literature confirms existence of an adelic oscillator and a softened uncertainty relation [8] but provides no explicit spectrum. Consequently, all quantitative statements that depend on this ladder (R2, R3) inherit this status. The linearized RG flow with $\gamma_v=0.1$ is illustrative; real systems may exhibit non‑exponential behavior. The linkage test examined only a two‑place product of distances; richer adelic constraints (e.g., involving local $L$‑factors) remain unexplored.

**Failure modes and self‑critique.** If the true $p$‑adic spectrum possessed constant gaps, R2 would collapse and the verdict would shift toward preservation (option a). If generic $p$‑adic systems exhibited $\gamma_p<0$, the verdict would move toward mixed preservation/repulsion (option b). The inverted‑oscillator caution [7] underscores that repulsive sectors can be subtle. The episode [10] where an oscillator‑based claim to beat the Heisenberg limit proved invalid reminds us to avoid over‑reaching universality claims. The non‑commutative result that identical spectra need not imply physical equivalence [5] warns that even a confirmed spectral match across places would not guarantee full physical equivalence of the attractors.

**What would falsify the claims.**  
(i) An exact $p$‑adic spectrum with constant gaps would falsify R2.  
(ii) A derivation forcing $\sum_v\gamma_v=0$ from adelic dynamics would falsify R5 and revive a strong place‑invariance claim.  
(iii) Evidence that the semi‑classical measure structure of [4] becomes place‑independent would undermine the premise that arithmetic (hence place) matters for attractor structure.

**Open questions.**  
* Does the propagator–fractional‑Fourier equivalence of [3] admit a $p$‑adic analogue on $p$‑adic modulation spaces?  
* Do the damped‑oscillator solutions of [1] possess $p$‑adic counterparts with the same dynamical completeness?  
* Does the universal bosonic mass scale of [11] admit a place‑resolved version?  
* Does the resource advantage of bosonic codes [12] survive if the native‑encoding argument must be restated place by place?

## 7. Practical Implications and Engineering Pathways

**(a) Users and decision impact.** The result is directly relevant to quantum information theorists and architects of bosonic quantum hardware. If the HO is an IR attractor in each place, design tools that rely on oscillator‑like effective models (e.g., bosonic error‑correcting code performance estimators) remain valid, but must incorporate place‑specific spectral features when extending to $p$‑adic‑inspired theoretical frameworks or adelic simulations.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions, it resides at TRL 1–2 (basic principles observed) and does not exceed TRL 3 (analytical proof‑of‑concept).

**(c) Smallest next experiment.** A concrete next step is a numerical computation of the Vladimirov–Volovich–Zelenov $p$‑adic Hamiltonian eigenvalues, using established $p$‑adic spectral methods. The experiment would measure the actual $p$‑adic level spacing; observation of a geometric gap ratio equal to $p$ would support the modeling assumption, while any deviation (e.g., constant gaps) would falsify R2.

**(d) Engineering constraints.**  
* **Mathematical tools:** Accurate $p$‑adic functional analysis libraries are required.  
* **Computational resources:** High‑precision arithmetic for $p$‑adic numbers may be needed to resolve deep tree levels.  
* **Modeling assumptions:** The adopted tree regularity $(p+1)$‑regular must be justified for the specific $p$‑adic quantum system under study.  
All other constraints (materials, fabrication, cost) are open questions because the present work does not involve hardware.

**(e) Cost/performance projections.** No quantitative cost or performance bounds are presented, as all numerical results are derived analytically or as projections conditioned on stated assumptions.

**(f) Risks and misuse.** Misinterpreting the structural transformation as a claim that all bosonic technologies automatically inherit $p$‑adic advantages could lead to over‑optimistic engineering roadmaps. The result should be used as a theoretical guide, not as a guarantee of performance gains in practical devices.

## 8. Conclusion

We asked whether the harmonic oscillator’s status as an IR attractor is place‑invariant. Within a place‑resolved RG framework, with explicit derivations and clearly labeled modeling assumptions, we find that the oscillator can attract in each place but with spectrally different fixed points—constant gaps in ℝ versus geometric gaps in ℚₚ organized on Bruhat–Tits tree levels. The adelic product formula constrains amplitudes, not spectra, imposing no linkage between place‑wise attractor distances. Thus the Harmonic Paradigm’s attractor thesis is not an Archimedean artifact (attraction is not reversed) but also not strongly place‑invariant; it is structurally transformed. The most urgent open task is the exact computation of the $p$‑adic oscillator spectrum, which would turn the present model‑based conclusions into rigorous theorems.

## References

[1] arXiv:2401.07238v1 | Coherently Driven Quantum Harmonic Oscillator Battery  
[2] arXiv:2111.09575v5 | Fractional Fourier transforms, harmonic oscillator propagators and Strichartz estimates on Pilipovic and modulation spaces  
[3] arXiv:2010.13436v2 | Localization and delocalization of eigenmodes of Harmonic Oscillators  
[4] arXiv:hep-th/0301066v2 | Harmonic oscillator on noncommutative spaces  
[5] arXiv:1001.1149v3 | The Bicomplex Quantum Harmonic Oscillator  
[6] arXiv:2204.10780v1 | Anti-PT-symmetric harmonic oscillator and its relation to the inverted harmonic oscillator  
[7] arXiv:1409.2468v3 | Harmonic Oscillators, Heisenberg's Uncertainty Principle and Simultaneous Measurement Precision for Position and Momentum  
[8] arXiv:hep-th/0402193v1 | Adelic Model of Harmonic Oscillator  
[9] arXiv:1907.08101v2 | What attracts to attractors?  
[10] arXiv:1409.2468v3 | Harmonic Oscillators, Heisenberg's Uncertainty Principle and Simultaneous Measurement Precision for Position and Momentum  
[11] arXiv:2009.07197v4 | Universal Mass Scale for Bosonic Fields in Multi-Brane Worlds  
[12] DOI pending. QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes.  
[13] https://papers.qnfo.org/papers/adelic-cross-domain-program/. QNFO: The Adelic Cross‑Domain Program v5.0: From the Fine‑Structure Constant to the Standard Model Mass Spectrum via Bruhat–Tits Trees.  
[14] https://papers.qnfo.org/papers/harmonic-adelic-completions/. QNFO: The Adelic Completion of the Harmonic Paradigm: A Five‑Pillar Red‑Team Assessment.

## Appendix A. Divergence report

**D1. $p$‑adic spectrum model.** Two drafts adopted the geometric ladder $E^{(p)}_n=E_0\,p^{-n}$ (energies decreasing with tree level). One draft used an alternative $E^{(p)}_n=E_0\,p^{\gamma n}$ with $\gamma=1$ (energies increasing). The disagreement concerns whether tree level indexes energy upward or downward. *Chosen convention:* the decreasing ladder $E^{(p)}_n=E_0\,p^{-n}$, because it yields an IR‑direction consistent with a shrinking gap hierarchy and is used by the majority of drafts.

**D2. Verdict on the attractor trichotomy.** One draft concluded repulsion in the $p$‑adic place by assigning a negative RG coefficient; the other two concluded structural transformation (attraction in both places but spectrally distinct). *Chosen convention:* the structural‑transformation verdict, as it follows from the derived spectra and does not rely on an ad‑hoc sign choice for $\gamma_p$.

**D3. Adelic linkage test design.** One draft tested linkage by forming a numerical product of matched Archimedean and $p$‑adic energy values; the other two tested a product‑of‑distances hypothesis on the RG flow. *Chosen convention:* the product‑of‑distances test, because the attractor claim concerns flow behavior rather than a dimensionful product of energies.

## Appendix B. Claim attribution

| Claim ID | Statement | Source Section(s) | Agreement |
|----------|-----------|-------------------|-----------|
| C1 | The adelic product formula holds for $x=2/3$. | A1 (Analysis) | Convergent |
| C2 | Bruhat–Tits tree vertex count formula $g_p(n)=(p+1)p^{n-1}$. | A2 (Analysis) | Convergent |
| C3 | $p$‑adic spectral gaps shrink geometrically with ratio $p$. | A3 (Analysis) | Convergent |
| C4 | Exponential RG decay $\alpha_v(\ell)=e^{-\gamma_v\ell}$ with $\gamma_v=0.1$ yields $\alpha_v(20)\approx0.135335$, etc. | A4 (Analysis) | Convergent |
| C5 | Product‑of‑distances $\prod_v\alpha_v(\ell)$ is $\ell$‑dependent unless $\sum_v\gamma_v=0$. | A5 (Analysis) | Convergent |
| C6 | Adelic product formula constrains amplitudes $|\Psi(x)|_v$ pointwise. | A6 (Analysis) | Convergent |
| C7 | The adelic oscillator exists and softens the uncertainty relation. | Background (Section 2) citing [8] | Convergent |
| C8 | Bicomplex oscillator eigenvalues and eigenkets are found. | Background citing [6] | Convergent |
| C9 | Non‑commutative oscillator spectra can be physically inequivalent. | Background citing [5] | Convergent |
| C10 | General solution of the quantum damped HO is given. | Background citing [1] | Convergent |
| C11 | Anti‑PT‑symmetric oscillator replacement $\omega\to i\omega$ leads to unbounded eigenvectors. | Background citing [7] | Convergent |
| C12 | Semi‑classical measures depend on arithmetic frequency relations. | Background citing [4] | Convergent |
| C13 | Harmonic‑oscillator propagators equal fractional Fourier transforms. | Background citing [3] | Convergent |
| C14 | Universal attractor template from heavy‑ion collisions. | Background citing [9] | Convergent |
| C15 | Universal bosonic mass scale for $q$‑forms reported. | Background citing [11] | Convergent |
| C16 | Bosonic codes require 5–40 × fewer photons and ≈100 × fewer modes at $p_L=10^{-6}$. | Background citing [12] | Convergent |
| C17 | Adelic Cross‑Domain Program maps physics onto Bruhat–Tits trees. | Background citing [13] | Convergent |
| C18 | Red‑team assessment notes Paradigm’s mechanisms confined to Archimedean place. | Background citing [14] | Convergent |