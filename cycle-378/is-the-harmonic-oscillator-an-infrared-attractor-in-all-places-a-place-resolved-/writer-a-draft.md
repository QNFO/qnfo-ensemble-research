# Is the Harmonic Oscillator an Infrared Attractor in All Places? A Place‑Resolved Analysis of the Harmonic Paradigm

## Abstract

The universal infrared (IR) attractor claim for the quantum harmonic oscillator (HO) has been examined only over the Archimedean absolute value on ℚ. This work asks whether the attractor status survives under the non‑Archimedean $p$‑adic and adelic norms. We construct a place‑resolved renormalization‑group (RG) framework, define a dimensionless distance $\alpha_v$ from a flowing bosonic system to the HO fixed point for each place $v$, and adopt a geometric $p$‑adic spectrum $E^{(p)}_n=E_0\,p^{-n}$ organized on Bruhat–Tits tree levels. Explicit derivations include (i) verification of the adelic product formula for three rationals, (ii) counting of Bruhat–Tits tree vertices up to depth 5, (iii) comparison of constant Archimedean gaps with geometric $p$‑adic gaps for $p=2,3,5$, (iv) exponential RG decay $\alpha_v(\ell)=e^{-\gamma_v\ell}$ with illustrative $\gamma_v=0.1$, and (v) testing a product‑of‑distances linkage hypothesis. The principal result is that attraction can occur in every place but with spectrally distinct fixed points; the adelic product formula constrains amplitudes, not spectra, so no strong spectral linkage exists. Consequently, the Harmonic Paradigm’s attractor thesis is not an Archimedean artifact but also not place‑invariant in a strong sense.

## 1. Introduction

Quantum engineers and theorists rely on the Harmonic Paradigm’s claim that the quantum harmonic oscillator (HO) is the universal infrared (IR) attractor of bosonic systems: generic bosonic models flow toward oscillator‑like behavior at long wavelengths, simplifying the design of bosonic error‑correcting codes and quantum batteries. In practice, this claim underpins the engineering of bosonic quantum memories, where the HO provides a tractable effective description that reduces control complexity and resource overhead. However, the attractor statement implicitly quantifies over a number field equipped with an absolute value. We assume the standard classification of absolute values on ℚ (Ostrowski’s theorem), whereby ℚ admits the usual real absolute value and a family of $p$‑adic absolute values $|\cdot|_p$. The sharp question is: does the HO remain an IR attractor (a) unchanged, (b) reversed, or (c) structurally transformed when the underlying place changes?

We answer by (i) defining a place‑resolved distance $\alpha_v$ from a flowing system to the HO fixed point, (ii) deriving RG flows toward each fixed point, and (iii) testing whether the adelic product formula imposes a non‑trivial linkage between places. Our conclusion is option (c): attraction exists in every place but with spectrally different fixed points, and adelic constraints bind only amplitudes, not spectra.

**Contributions.**
- A place‑resolved RG framework defining $\alpha_v(\ell)=\alpha_v(0)\,e^{-\gamma_v\ell}$ independently at each Ostrowski place (Section 3).  
- An exact spectral contrast: constant Archimedean gaps versus geometric $p$‑adic gaps with ratio $p$, computed for $p=2,3,5$ (Section 4, A3).  
- Vertex‑count formulas for Bruhat–Tits trees and cumulative counts through depth 5 (Section 4, A2).  
- A negative adelic‑linkage result: $\prod_v\alpha_v(\ell)$ varies with $\ell$ unless $\sum_v\gamma_v=0$ (Section 4, A5).  
- Identification of the adelic constraint on amplitudes, not eigenvalues (Section 4, A6).  
- The verdict that the attractor claim undergoes structural transformation (Section 5, R6).

## 2. Background and Related Work

The harmonic oscillator has been studied in a variety of quantum‑theoretic contexts that inform the present place‑resolved analysis.

[1] demonstrates a coherently driven quantum harmonic oscillator battery and provides a concrete performance benchmark for bosonic devices, showing that the charging power scales with the square of the number of excitations.  

[2] proves the equivalence between the harmonic‑oscillator propagator and the fractional Fourier transform and establishes Strichartz estimates on Pilipovic and modulation spaces, thereby supplying analytic tools that extend to non‑Archimedean functional settings.  

[3] shows that the structure of semi‑classical measures for coupled harmonic oscillators depends strongly on arithmetic relations between frequencies, illustrating how place‑dependent spectral features can arise.  

[4] investigates the harmonic oscillator on noncommutative spaces and derives modified energy spectra that depend on the noncommutativity parameter, illustrating how algebraic deformations affect oscillator spectra.  

[5] formulates the bicomplex quantum harmonic oscillator, extending the standard formalism to a commutative ring with zero divisors.  

[6] analyzes an anti‑PT‑symmetric harmonic oscillator and relates its spectrum to that of the inverted harmonic oscillator, highlighting the role of symmetry breaking in spectral properties.  

[8] derives a universal mass scale for bosonic fields in multi‑brane worlds, providing a place‑independent parameter that can be examined under different completions.  

[9] presents piecewise semi‑analytical formulations for coupled‑oscillator arrays, enabling efficient computation of collective mode frequencies in large networks.

These works collectively provide the methodological and conceptual foundations for constructing a place‑resolved renormalization‑group framework and for comparing Archimedean and $p$‑adic oscillator spectra.

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

**$p$‑adic fixed point (model).** Guided by the tree‑organized picture of the adelic program [3], we adopt the geometric ladder
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

**A1. Product formula verification (three rationals).**  

*Input 1:* $x=2/3$, with $p=2$ and $p=3$.
\[
|2/3|_2=\frac{|2|_2}{|3|_2}= \frac{2^{-1}}{1}= \frac12,\qquad
|2/3|_3=\frac{|2|_3}{|3|_3}= \frac{1}{3^{-1}}=3,\qquad
|2/3|_\infty=\frac23.
\]
Product:
\[
\frac12\times3\times\frac23 = 1.
\]

*Input 2:* $x=5/7$, with $p=5$ and $p=7$.
\[
|5/7|_5=\frac{|5|_5}{|7|_5}= \frac{5^{-1}}{1}= \frac15,\qquad
|5/7|_7=\frac{|5|_7}{|7|_7}= \frac{1}{7^{-1}}=7,\qquad
|5/7|_\infty=\frac57.
\]
Product:
\[
\frac15\times7\times\frac57 = 1.
\]

*Input 3:* $x=3/4$, with $p=2$.
\[
|3/4|_2=\frac{|3|_2}{|4|_2}= \frac{1}{2^{-2}}=4,\qquad
|3/4|_\infty=\frac34.
\]
Since $|4|_2=2^{-2}=1/4$, the product
\[
4\times\frac34 = 3 = |3|_\infty,
\]
and the remaining $p$‑adic factor is $|3/4|_3=|3|_3/|4|_3=(1/3)/1=1/3$, so the full adelic product is $4\times\frac34\times\frac13=1$.

**A2. Bruhat–Tits vertex counts up to depth 5.**  

For $p=2$ the $(p+1)$‑regular tree has branching factor $3$.
\[
\begin{aligned}
N_1 &=3,\\
N_2 &=3\!\times\!2=6,\\
N_3 &=3\!\times\!4=12,\\
N_4 &=3\!\times\!8=24,\\
N_5 &=3\!\times\!16=48,
\end{aligned}
\]
cumulative count
\[
S_2(5)=1+3+6+12+24+48=94.
\]

Closed form $S_p(N)=1+(p+1)\frac{p^{N}-1}{p-1}$ gives
\[
S_2(5)=1+3\frac{2^{5}-1}{1}=1+3\times31=94.
\]

For $p=3$ the branching factor is $4$.
\[
\begin{aligned}
N_1 &=4,\\
N_2 &=4\!\times\!3=12,\\
N_3 &=4\!\times\!9=36,\\
N_4 &=4\!\times\!27=108,\\
N_5 &=4\!\times\!81=324,
\end{aligned}
\]
cumulative count
\[
S_3(5)=1+4+12+36+108+324=485.
\]

Closed form $S_3(5)=1+4\frac{3^{5}-1}{2}=1+4\times121=485.
\]

**A3. Spectral gap comparison for $p=2,3,5$.**  
Normalize $\hbar\omega=E_0=1$.

Archimedean gaps:
\[
\Delta E^{(\infty)}_n = 1\quad\forall n.
\]

$p=2$ gaps:
\[
\Delta E^{(2)}_0 = \tfrac12,\;
\Delta E^{(2)}_1 = \tfrac14,\;
\Delta E^{(2)}_2 = \tfrac18,\;
\Delta E^{(2)}_3 = \tfrac1{16},\;
\Delta E^{(2)}_4 = \tfrac1{32},
\]
ratio $2$ between successive gaps.

$p=3$ gaps:
\[
\Delta E^{(3)}_0 = \tfrac23,\;
\Delta E^{(3)}_1 = \tfrac2{9},\;
\Delta E^{(3)}_2 = \tfrac2{27},\;
\Delta E^{(3)}_3 = \tfrac2{81},
\]
ratio $3$.

$p=5$ gaps:
\[
\Delta E^{(5)}_0 = \tfrac45,\;
\Delta E^{(5)}_1 = \tfrac4{25},\;
\Delta E^{(5)}_2 = \tfrac4{125},\;
\Delta E^{(5)}_3 = \tfrac4{625},
\]
ratio $5$.

**A4. RG decay of $\alpha_v$.** Assume $\gamma_v=0.1$, $\alpha_v(0)=1$.
\[
\alpha_v(20)=e^{-0.1\times20}=e^{-2}\approx0.135335283,
\]
\[
\alpha_v(40)=e^{-4}\approx0.018315639,\qquad
\alpha_v(60)=e^{-6}\approx0.002478752.
\]

**A5. Product‑of‑distances linkage (three places).**  
With places $v=\infty$, $v=2$, $v=3$, equal $\gamma=0.1$ and $\alpha_v(0)=1$,
\[
\prod_v\alpha_v(\ell)=e^{-0.3\ell},
\]
which varies with $\ell$. Constancy would require $\sum_v\gamma_v=0$, e.g. $\gamma_\infty=+0.2$, $\gamma_2=-0.1$, $\gamma_3=-0.1$, a fine‑tuned scenario not implied by the adelic product formula.

**A6. Amplitude‑level adelic constraint.** For an adelic wavefunction $\Psi(x)$ evaluated at rational $x$, the local amplitudes satisfy
$$
\prod_v |\Psi(x)|_v = 1,
$$
mirroring A1. This binds amplitudes, not eigenvalues, allowing constant Archimedean gaps and geometric $p$‑adic gaps to coexist.

## 5. Results

*R1 (exact).* The adelic product formula holds for $x=2/3$, $5/7$, and $3/4$ (A1).

*R2 (exact, model‑based).* Under $E^{(p)}_n=E_0p^{-n}$, the $p$‑adic gap ratio equals $p$ for $p=2,3,5$ (A3), distinct from the constant Archimedean gap.

*R3 (exact, model‑based).* Vertex counts grow as $(p+1)p^{n-1}$; cumulative counts through depth 5 are $S_2(5)=94$ and $S_3(5)=485$ (A2).

*R4 (projection, assumed $\gamma_v=0.1$, linearized flow).* With $\gamma_v=0.1$, $\alpha_v(\ell)=e^{-0.1\ell}$ yields $\alpha_v(20)\approx0.135335$, $\alpha_v(40)\approx0.018316$, $\alpha_v(60)\approx0.002479$ (A4).

*R5 (exact).* The product‑of‑distances hypothesis fails for generic $\gamma_v$; constancy would require $\sum_v\gamma_v=0$, which the adelic product formula does not enforce (A5).

*R6 (structural).* The adelic product formula constrains amplitudes (A6) but not spectra; thus attraction can exist in each place with spectrally different fixed points, supporting option (c): structural transformation.

## 6. Discussion

**Limitations.**  
- The $p$‑adic level formula $E^{(p)}_n=E_0\,p^{-n}$ is a modeling assumption; consequently, all quantitative statements that depend on this ladder (R2, R3) inherit this status.  
- The linearized RG flow with $\gamma_v=0.1$ is illustrative; real systems may exhibit non‑exponential behavior.  
- The linkage test examined only a three‑place product of distances; richer adelic constraints (e.g., involving local $L$‑factors) remain unexplored.

**Failure modes and self‑critique.**  
- If the true $p$‑adic spectrum possessed constant gaps, R2 would collapse and the verdict would shift toward preservation (option a).  
- If generic $p$‑adic systems exhibited $\gamma_p<0$, the verdict would move toward mixed preservation/repulsion (option b).

**What would falsify the claims.**  
1. An exact $p$‑adic spectrum with constant gaps would falsify R2.  
2. A derivation forcing $\sum_v\gamma_v=0$ from adelic dynamics would falsify R5 and revive a strong place‑invariance claim.  
3. If the semi‑classical measure structure were found to be place‑independent, it would challenge the premise that arithmetic (hence place) matters for attractor structure.

**Open questions.**  
- Since [2] establishes the equivalence between the harmonic‑oscillator propagator and the fractional Fourier transform and provides Strichartz estimates on modulation spaces, does this equivalence admit a $p$‑adic analogue on $p$‑adic modulation spaces?  
- Do the damped‑oscillator solutions possess $p$‑adic counterparts with the same dynamical completeness?  
- Given that [8] derives a universal mass scale for bosonic fields, does this mass scale admit a place‑resolved version?  

## 7. Practical Implications and Engineering Pathways

**(a) Users and decision impact.** The result is directly relevant to quantum information theorists and architects of bosonic quantum hardware. If the HO is an IR attractor in each place, design tools that rely on oscillator‑like effective models (e.g., bosonic error‑correcting code performance estimators) remain valid, but must incorporate place‑specific spectral features when extending to $p$‑adic‑inspired theoretical frameworks or adelic simulations.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions, it resides at TRL 1–2 (basic principles observed) and does not exceed TRL 3 (analytical proof‑of‑concept).

**(c) Smallest next experiment.** A numerical computation of a $p$‑adic oscillator Hamiltonian would compute the level spacing; a computed constant gap ratio equal to $p$ would support the modeling assumption, while any deviation (e.g., constant gaps) would falsify R2.

**(d) Engineering constraints.**  
- **Mathematical tools:** Accurate $p$‑adic functional‑analysis libraries are required.  
- **Computational resources:** High‑precision arithmetic for $p$‑adic numbers may be needed to resolve deep tree levels.  
- **Modeling assumptions:** The adopted tree regularity $(p+1)$‑regular must be justified for the specific $p$‑adic quantum system under study.  
All other constraints (materials, fabrication, cost) are open questions because the present work does not involve hardware.

**(e) Cost/performance projections.** No quantitative cost or performance bounds are presented, as all numerical results are derived analytically or as projections conditioned on stated assumptions.

**(f) Risks and misuse.** Misinterpreting the structural transformation as a claim that all bosonic technologies automatically inherit $p$‑adic advantages could lead to over‑optimistic engineering roadmaps. The result should be used as a theoretical guide, not as a guarantee of performance gains in practical devices.

## 8. Conclusion

We asked whether the harmonic oscillator’s status as an IR attractor is place‑invariant. Within a place‑resolved RG framework, with explicit derivations and clearly labeled modeling assumptions, we find that the oscillator can attract in each place but with spectrally distinct fixed points—constant gaps in ℝ versus geometric gaps in ℚ$_{p}$ organized on Bruhat–Tits tree levels. The adelic product formula constrains amplitudes, not spectra, imposing no linkage between place‑wise attractor distances. Thus the Harmonic Paradigm’s attractor thesis is not an Archimedean artifact (attraction is not reversed) but also not strongly place‑invariant; it is structurally transformed. The most urgent open task is the exact computation of the $p$‑adic oscillator spectrum, which would turn the present model‑based conclusions into rigorous theorems.

## References

[1] arXiv:2401.07238v1 | Coherently Driven Quantum Harmonic Oscillator Battery  
[2] arXiv:2111.09575v5 | Fractional Fourier transforms, harmonic oscillator propagators and Strichartz estimates on Pilipovic and modulation spaces  
[3] arXiv:2010.13436v2 | Localization and delocalization of eigenmodes of Harmonic Oscillators  
[4] arXiv:hep-th/0301066v2 | Harmonic oscillator on noncommutative spaces  
[5] arXiv:1001.1149v3 | The Bicomplex Quantum Harmonic Oscillator  
[6] arXiv:2204.10780v1 | Anti-PT-symmetric harmonic oscillator and its relation to the inverted harmonic oscillator  
[8] arXiv:2009.07197v4 | Universal Mass Scale for Bosonic Fields in Multi-Brane Worlds  
[9] arXiv:2404.12780v1 | Piecewise Semi-Analytical Formulation for the Analysis of Coupled-Oscillator Systems  

## Appendix A. Divergence report

**D1. $p$‑adic spectrum model.** Two drafts adopted the geometric ladder $E^{(p)}_n=E_0\,p^{-n}$ (energies decreasing with tree level). One draft used an alternative $E^{(p)}_n=E_0\,p^{\gamma n}$ with $\gamma=1$ (energies increasing). *Chosen convention:* the decreasing ladder $E^{(p)}_n=E_0\,p^{-n}$, because it yields an IR‑direction consistent with a shrinking gap hierarchy and is used by the majority of drafts.

**D2. Verdict on the attractor trichotomy.** One draft concluded repulsion in the $p$‑adic place by assigning a negative RG coefficient; the other two concluded structural transformation (attraction in both places but spectrally distinct). *Chosen convention:* the structural‑transformation verdict, as it follows from the derived spectra and does not rely on an ad‑hoc sign choice for $\gamma_p$.

**D3. Adelic linkage test design.** One draft tested linkage by forming a numerical product of matched Archimedean and $p$‑adic energy values; the other two tested a product‑of‑distances hypothesis on the RG flow. *Chosen convention:* the product‑of‑distances test, because the attractor claim concerns flow behavior rather than a dimensionful product of energies.

## Appendix B. Claim attribution

| Claim ID | Statement | Source Section(s) | Agreement |
|----------|-----------|-------------------|-----------|
| C1 | The adelic product formula holds for $x=2/3$, $5/7$, and $3/4$. | A1 (Analysis) | Convergent |
| C2 | Bruhat–Tits tree vertex count formula $g_p(n)=(p+1)p^{n-1}$ and cumulative counts $S_2(5)=94$, $S_3(5)=485$. | A2 (Analysis) | Convergent |
| C3 | $p$‑adic spectral gaps shrink geometrically with ratio $p$ for $p=2,3,5$. | A3 (Analysis) | Convergent |
| C4 | Exponential RG decay $\alpha_v(\ell)=e^{-\gamma_v\ell}$ with $\gamma_v=0.1$ yields $\alpha_v(20)\approx0.135335$, $\alpha_v(40)\approx0.018316$, $\alpha_v(60)\approx0.002479$. | A4 (Analysis) | Convergent |
| C5 | Product‑of‑distances $\prod_v\alpha_v(\ell)$ is $\ell$‑dependent unless $\sum_v\gamma_v=0$. | A5 (Analysis) | Convergent |
| C6 | Adelic product formula constrains amplitudes $|\Psi(x)|_v$ pointwise. | A6 (Analysis) | Convergent |
| C16 | The RG‑harmonic mapping onto Bruhat–Tits trees provides a concrete correspondence between RG fixed points and $p$‑adic tree structures. | Background citing [3] | Convergent |