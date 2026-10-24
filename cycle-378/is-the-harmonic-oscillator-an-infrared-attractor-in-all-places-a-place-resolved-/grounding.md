# Grounding block - source: rem-rev-9d76ef8d-5b41-484d-b54a-90112414e16d

## Research idea

Is the Harmonic Oscillator an IR Attractor in All Places?. The claim that the harmonic oscillator is a universal infrared attractor for bosonic systems is place-ambiguous: it has only been tested under the Archimedean absolute value. The conjecture to investigate: whether the oscillator's attractor status is (a) preserved, (b) reversed, or (c) structurally transformed under p-adic and adelic norms. Concretely, compare the Vladimirov-Volovich-Zelenov p-adic harmonic oscillator (spectrum organized on Bruhat-Tits tree levels) with the standard Archimedean spectrum E_n = ℏω(n+1/2), and ask whether the adelic product formula imposes a genuine constraint linking the two, or whether they are incommensurable structures sharing a name by historical accident. A theoretical paper could derive the renormalization-group flow toward each oscillator in a fixed place, compute whether α (distance from the attractor) is place-dependent, and test via explicit spectral analysis whether attraction in ℝ coexists with attraction, repulsion, or different fixed-point structure in ℚ_p. A positive adelic linkage would upgrade the Harmonic Paradigm's thesis to a place-invariant statement; a negative result would show the attractor claim is an artifact of the Archimedean place.

Source: owner notebook notes/v1/2026/07/23/_26204121554.md

Post-publication revision of the published paper "Is the Harmonic Oscillator an Infrared Attractor in All Places? A Place‑Resolved Analysis of the Harmonic Paradigm" (version 2.1.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 8 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 6 references (70 percent of 8, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. A6: 'the local amplitudes satisfy prod_v |Psi(x)|_v = 1, mirroring A1' — the adelic product formula is said to bind wavefunction amplitudes. (confirmed by a second model)
2. Reference attribution mismatches: the universal bosonic mass scale is cited as [8] in Section 2 but as [11] in Open questions; the anti-PT oscillator is cited as [6] in Section 2 but as [7] in Appendix B (C11). (confirmed by a second model)

## Existing paper under revision (remediation only)

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

[1] demonstrates a coherently driven quantum harmonic oscillator battery and shows that the charging power scales with the square of the number of excitations, providing a concrete performance benchmark for bosonic devices.

[2] proves the equivalence between the harmonic‑oscillator propagator and the fractional Fourier transform and establishes Strichartz estimates on Pilipovic and modulation spaces, thereby supplying analytic tools that extend to non‑Archimedean functional settings.

[4] investigates the harmonic oscillator on noncommutative spaces and derives modified energy spectra that depend on the noncommutativity parameter, illustrating how algebraic deformations affect oscillator spectra.

[5] formulates the bicomplex quantum harmonic oscillator.

[6] analyzes an anti‑PT‑symmetric harmonic oscillator and relates its spectrum to that of the inverted harmonic oscillator, highlighting the role of symmetry breaking in spectral properties.

[8] derives a universal mass scale for bosonic fields in multi‑brane worlds.

[9] presents piecewise semi‑analytical formulations for coupled‑oscillator arrays, enabling efficient computation of collective mode frequencies in large networks.

[13] maps renormalization‑group flows of harmonic systems onto Bruhat–Tits trees, establishing a concrete correspondence between RG fixed points and $p$‑adic tree structures.

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

**$p$‑adic fixed point (model).** Guided by the tree‑organized picture of the adelic program [13], we adopt the geometric ladder
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
and the remaining $p$-adic factor is $|3/4|_3=|3|_3/|4|_3=(1/3)/1=1/3$, so the full adelic product is $4\times\frac34\times\frac13=1$.

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
- Given that [8] derives a universal mass scale for bosonic fields in multi‑brane worlds, does this mass scale admit a place‑resolved version?  
- 

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

We asked whether the harmonic oscillator’s status as an IR attractor is place‑invariant. Within a place‑resolved RG framework, with explicit derivations and clearly labeled modeling assumptions, we find that the oscillator can attract in each place but with spectrally different fixed points—constant gaps in ℝ versus geometric gaps in ℚ$_{p}$ organized on Bruhat–Tits tree levels. The adelic product formula constrains amplitudes, not spectra, imposing no linkage between place‑wise attractor distances. Thus the Harmonic Paradigm’s attractor thesis is not an Archimedean artifact (attraction is not reversed) but also not strongly place‑invariant; it is structurally transformed. The most urgent open task is the exact computation of the $p$‑adic oscillator spectrum, which would turn the present model‑based conclusions into rigorous theorems.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix B. Claim attribution. references 14 -> 10. length 4137 -> 2753 words.
- Version 2.1.0 (2026-10-23, from 2.0.0): revised against the current literature, re-reviewed and re-verified. references 10 -> 8. length 2793 -> 2752 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.0-no-registrar). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Coherently Driven Quantum Harmonic Oscillator Battery. arXiv:2401.07238v1. https://arxiv.org/abs/2401.07238v1
[2] Fractional Fourier transforms, harmonic oscillator propagators and Strichartz estimates on Pilipovic and modulation spaces. arXiv:2111.09575v5. https://arxiv.org/abs/2111.09575v5
[4] Harmonic oscillator on noncommutative spaces. arXiv:hep-th/0301066v2. https://arxiv.org/abs/hep-th/0301066v2
[5] The Bicomplex Quantum Harmonic Oscillator. arXiv:1001.1149v3. https://arxiv.org/abs/1001.1149v3
[6] Anti-PT-symmetric harmonic oscillator and its relation to the inverted harmonic oscillator. arXiv:2204.10780v1. https://arxiv.org/abs/2204.10780v1
[8] Universal Mass Scale for Bosonic Fields in Multi-Brane Worlds. arXiv:2009.07197v4. https://arxiv.org/abs/2009.07197v4
[9] Piecewise Semi-Analytical Formulation for the Analysis of Coupled-Oscillator Systems. arXiv:2404.12780v1. https://arxiv.org/abs/2404.12780v1
[13] https://papers.qnfo.org/papers/rg-harmonic-isomorphism. QNFO: The RG-Harmonic Isomorphism: Renormalization Group Similarities with Harmonic Quantum Mechanics.

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

| C16 | The adelic RG program maps physics onto Bruhat–Tits trees. | Background citing [13] | Convergent |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2401.07238v1 | Coherently Driven Quantum Harmonic Oscillator Battery
arXiv:2111.09575v5 | Fractional Fourier transforms, harmonic oscillator propagators and Strichartz estimates on Pilipovic and modulation spaces
arXiv:2010.13436v2 | Localization and delocalization of eigenmodes of Harmonic Oscillators
arXiv:hep-th/0301066v2 | Harmonic oscillator on noncommutative spaces
arXiv:1001.1149v3 | The Bicomplex Quantum Harmonic Oscillator
arXiv:2204.10780v1 | Anti-PT-symmetric harmonic oscillator and its relation to the inverted harmonic oscillator
arXiv:1409.2468v3 | Harmonic Oscillators, Heisenberg's Uncertainty Principle and Simultaneous Measurement Precision for Position and Momentum
arXiv:2009.07197v4 | Universal Mass Scale for Bosonic Fields in Multi-Brane Worlds
arXiv:2404.12780v1 | Piecewise Semi-Analytical Formulation for the Analysis of Coupled-Oscillator Systems

## QNFO corpus context (Vectorize)

QNFO: The RG-Harmonic Isomorphism: Synthesis of Eight Research Question Deliverables | https://papers.qnfo.org/papers/rg-harmonic-synthesis
QNFO: Is the Harmonic Oscillator an Infrared Attractor in All Places? A Place‑Resolved Analysis of the Harmonic Paradigm | https://papers.qnfo.org/papers/is-the-harmonic-oscillator-an-infrared-attractor-in-all-places-a-place-resolved-
QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis | https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2401.07238v1 | Coherently Driven Quantum Harmonic Oscillator Battery
  Quantum harmonic oscillator (QHO) battery models have been studied with significant importance in the recent past because these batteries are experimentally realizable and have high ergotropy and capacity to store more than one quanta of energy. QHO battery models are reinvestigated here to answer a set of fundamental questions: Do such models have any benefit? Is unbounded charging possible? Does
  Full text (https://arxiv.org/html/2401.07238v1), excerpts of its own sections:
  § I Introduction: Quantum thermodynamics is the study of two independent theories: thermodynamics and quantum mechanics. Specifically, quantum thermodynamics explores how the laws of thermodynamics emerge from the underlying framework of quantum mechanics [ 1 ] . Moreover, quantum thermodynamics explores how traditional thermodynamic principles apply in the quantum realm, where quantum effects like quantum fluctuations, quantum coherence, and entanglement play a significant role. With the advent of the second quantum revolution [ 2 ] , we are in a situation to build several extremely small quantum devices. There is a need to supply energy on demand to such devices and to store that energy in systems of similar dimensions. This specific need is addressed by a quantum battery- a device that can temporarily store energy and supply that (as and when needed) to another device just like a traditional battery, but in contrast to the conventional batteries it exploits the nonclassical features of the quantum world [ 3 , 4 ] . [...]
  § II Model and Approach: In this section, we present the model of the charger-battery system studied in the present work. Here, we consider a QHO as a charger, which interacts with another QHO treated as a battery. The interaction between the charger and the battery takes place for the time period $(0,\tau)$ , where $\tau$ is the charging time. The charger also interacts with the environment and dissipates energy. To charge the battery, the charger is driven by a laser field of amplitude $F$ . The charger-battery system studied here is schematically shown in Figure-1 and can be mathematically described by the total Hamiltonian of the charger-battery [ 25 ] system expressed as $\displaystyle{\cal H}$ $\displaystyle=\omega_{o}a^{\dagger}a+\omega_{o}b^{\dagger}b+g(ab^{\dagger}+a^{\dagger}b)$ $\displaystyle\quad+F(ae^{i\omega_{f}t}+a^{\dagger}e^{-i\omega_{f}t}),$ (1) where $\omega_{o}$ is frequency of charger and battery, $\omega_{f}$ is laser frequency, $a^{\dagger}$ are annihilation and creation operators of charger (A), and $b$ and $b^{\dagger}$ are annihilation and creation operators of battery (B). [...]
  § III Off-resonance battery charging: Numerical and Analytical Solution: In this section, we present off-resonance battery charging which has already been explored in [ 25 , 23 ] . Off-resonance means laser frequency is out of tune with the global frequency of charger-battery system $\omega_{\pm}$ . [...]
  § VII Conclusion: In this work, we have investigated charger-mediated energy transfer for QHO quantum batteries via an open-system approach for a non-catalytic model. We have shown that instead of tuning laser frequency $\omega_{f}$ with local frequencies $\omega_{o}$ of the charger-battery system, we may tune laser frequency $\omega_{f}$ with global frequency $\omega_{\pm}$ ; in this way, the battery can store more energy. Further, in contrast to the previous study [ 23 ] , we have not observed any signature of boundless charging and oscillation of period $1/\Delta$ , when the charger is dissipative. In fact, in contrast to [ 23 ] , it’s established that catalysts are not essential for the efficient charging of QHO batteries. Finally, we have presented another simplified model of QHO batteries in which a QHO battery is found to be charged faster than catalytic and non-catalytic batteries. We have also pointed out that self-discharging of catalytic and non-catalytic batteries and QHO is faster than the charging process which makes them quite unstable against the interaction with the environment. [...]
[2] arXiv:2111.09575v5 | Fractional Fourier transforms, harmonic oscillator propagators and Strichartz estimates on Pilipovic and modulation spaces
  We show that harmonic oscillator propagators and fractional Fourier transforms are essentially the same. We deduce continuity properties and fix time estimates for such operators on modulation spaces, and apply the results to prove Strichartz estimates for the harmonic oscillator propagator when acting on modulation spaces. Especially we extend some results by Balhara, Cordero, Nicola, Rodino and 
  Full text (https://arxiv.org/html/2111.09575v5), excerpts of its own sections:
  § 0. Introduction: In the paper we investigate mapping properties for powers of harmonic oscillators, their propagators and fractional Fourier transforms on Pilipović spaces and modulation spaces. Especially we link fractional Fourier transforms with harmonic oscillator propagators, which opens up for full transitions of various properties between these operators. We also deduce certain continuity properties for fractional Fourier transforms on modulation spaces (including Wiener amalgam spaces). By using the link between the fractional Fourier transform and harmonic oscillator propagators we extend at the same time certain continuity properties of harmonic oscillator propagators on modulation spaces, given in [ 8 , 9 , 15 , 16 ] . These investigations are also related to [ 13 ] , where among others, $L^{p}$ and Hausdorff-Young estimates for fractional Fourier transforms are established. Thereafter we apply such continuity results to extend certain Strichartz estimates for harmonic oscillator propagators in [ 16 ] when acting on modulation spaces. [...]
  § 1. Preliminaries: In this section we recall some basic facts. We start by discussing Gelfand-Shilov spaces, then modulation spaces and thereafter Pilipović spaces and some of their properties. Then we recall the Bargmann transform and some of its properties, and introduce suitable classes of power series expansions and entire functions on $\mathbf{C}^{d}$ . Finally, in Subsection 1.8 we recall some facts on Strichartz estimates.
  § 1.1. Gelfand-Shilov spaces and their distribution spaces: We start by recalling definitions of Fourier invariant (standard) Gelfand-Shilov spaces and their distribution spaces (cf. e. g. [ 29 , 47 ] ). Let $s\geq 0$ and $h\in\mathbf{R}_{+}$ be fixed. Then $\mathcal{S}_{s,h}(\mathbf{R}^{d})$ is the set of all $f\in C^{\infty}(\mathbf{R}^{d})$ such that $\|f\|_{\mathcal{S}_{s,h}}\equiv\sup\frac{|x^{\beta}\partial^{\alpha}f(x)|}{h^{|\alpha|+|\beta|}(\alpha!\,\beta!)^{s}}$ is finite. Here the supremum is taken over all $\alpha,\beta\in\mathbf{N}^{d}$ and $x\in\mathbf{R}^{d}$ . Obviously $\mathcal{S}_{s,h}\subseteq\mathscr{S}$ is a Banach space which increases with $h$ and $s$ . The Gelfand-Shilov space $\mathcal{S}_{s}(\mathbf{R}^{d})$ ( $\Sigma_{s}(\mathbf{R}^{d})$ ) of Roumieu type (Beurling type) is the projective limit (projective limit) of $\mathcal{S}_{s,h}(\mathbf{R}^{d})$ with respect to $h$ . [...]
  § 1.2. Spaces of sequences: The definitions of Pilipović spaces and spaces of power series expansions are based on certain spaces of sequences on $\mathbf{N}^{d}$ , indexed by the extended set $\mathbf{R}_{\flat}=\mathbf{R}_{+}\bigcup\{\,\flat_{\sigma}\,;\,\sigma\in\mathbf{R}_{+}\,\},$ of $\mathbf{R}_{+}$ . We extend the ordering relation on $\mathbf{R}_{+}$ to the set $\mathbf{R}_{\flat}$ , by letting $s_{1} when $s_{1},s_{2},\sigma_{1},\sigma_{2}\in\mathbf{R}_{+}$ , satisfy $s_{1} [ 53 ] .) Definition 1.1 . Let $s\in\mathbf{R}_{\flat}$ and $r,\sigma\in\mathbf{R}_{+}$ . [...]
  § 1.3. Pilipović spaces and spaces of power series expansions on $\mathbf{C}^{d}$: We recall that the Hermite function of order $\alpha\in\mathbf{N}^{d}$ is defined by $h_{\alpha}(x)=\pi^{-\frac{d}{4}}(-1)^{|\alpha|}(2^{|\alpha|}\alpha!)^{-\frac{1}{2}}e^{\frac{1}{2}\cdot{|x|^{2}}}(\partial^{\alpha}e^{-|x|^{2}}).$ It follows that $h_{\alpha}(x)=((2\pi)^{\frac{d}{2}}\alpha!)^{-1}e^{-\frac{1}{2}\cdot{|x|^{2}}}p_{\alpha}(x),$ for some polynomial $p_{\alpha}$ of order $\alpha$ on $\mathbf{R}^{d}$ , called the Hermite polynomial of order $\alpha$ . [...]
[3] arXiv:2010.13436v2 | Localization and delocalization of eigenmodes of Harmonic Oscillators
  We characterize quantum limits and semi-classical measures corresponding to sequences of eigenfunctions for systems of coupled quantum harmonic oscillators with arbitrary frequencies. The structure of the set of semi-classical measures turns out to depend strongly on the arithmetic relations between frequencies of each decoupled oscillator. In particular, we show that as soon as these frequencies 
  Full text (https://arxiv.org/html/2010.13436v2), excerpts of its own sections:
  § 1. Introduction: Understanding the distribution of high-frequency eigenfunctions of elliptic operators, in particular the presence of scarring (concentration on subsets of zero Lebesgue measure), has been the subject of intensive study in the past fifty years. In this note, we discuss this problem for eigenfunctions of Schrödinger operators acting on $L^{2}(\mathbb{R}^{d})$ of the form: (1) $\widehat{P}:=-\frac{1}{2}\Delta_{x}+\frac{1}{2}Q.$ with $Q$ a positive definite quadratic form on $\mathbb{R}^{d}$ . Since $\widehat{P}$ has compact resolvent in $L^{2}(\mathbb{R}^{d})$ , its spectrum is discrete and unbounded. Moreover, the non-compactness of $\mathbb{R}^{d}$ implies that the $L^{2}(\mathbb{R}^{d})$ -mass of any sequence of normalized eigenfunctions with eigenvalues tending to infinity will escape any bounded set, both in position and momentum variables. In order to observe eventual concentration-like behavior on the eigenfunctions, it is natural to rescale the problem. [...]
  § 2. Scarring on minimal invariant tori: We first show how to construct sequences of joint eigenfunctions of the periodic Hamiltonians $\mathcal{H}_{n}$ that concentrate on minimal invariant tori. Let $T_{n}:=T_{v_{n}\nu_{n}}$ denote the period of $\phi_{t}^{\mathcal{H}_{n}}$ as defined in Remark 1 . Write $\mathcal{R}_{\omega}:=[0,T_{1})\times\cdots\times[0,T_{d_{\omega}})$ , and let $|\mathcal{R}_{\omega}|:=T_{1}\cdots T_{d_{\omega}}$ . Define $\widehat{\mathcal{H}}_{\hbar}:=(\operatorname{Op}_{\hbar}(\mathcal{H}_{1}),\ldots,\operatorname{Op}_{\hbar}(\mathcal{H}_{d_{\omega}})),$ with: $\operatorname{Op}_{\hbar}(\mathcal{H}_{n})=v_{n}\sum_{j=1}^{d}\nu_{n,j}(-\hbar^{2}\partial_{x_{j}}^{2}+x_{j}^{2}),\quad n=1,\ldots,d_{\omega}.$ The following result precises remainders and extends to harmonic oscillators with general frequency vectors [ 11 ] and [ 26 , Proposition 5] . Lemma 1 . [...]
  § 3. Proof of Theorem 1: Let us show that for any choice of $E\in\Sigma_{\mathcal{H}}$ one has that $\mathcal{M}_{E}(\mathcal{H}):=\{\mu\in\mathcal{M}(H)\,:\,\operatorname{supp}\mu\subseteq\mathcal{H}^{-1}(E)\}\subseteq\mathcal{M}(\widehat{H}_{\hbar}).$ To this aim, note that since $\mathcal{M}_{E}(\mathcal{H})$ is convex and compact for the weak- $\star$ topology, the Krein-Milman theorem ensures that $\mathcal{M}_{E}(\mathcal{H})$ is the closure of the convex hull of the set of orbit measures $\delta_{\mathcal{T}_{\omega}(z_{0})}$ , where (26) $\mathcal{T}_{\omega}(z_{0}):=\{\Phi_{z_{0}}(\tau)\in\mathcal{H}^{-1}(E)\,:\,\tau\in\mathcal{R}_{\omega}\},\quad z_{0}\in\mathcal{H}^{-1}(E).$ Therefore, it suffices to show that any measure $\mu$ that is a convex combination of distinct orbit measures $\delta_{\mathcal{T}_{1}},\ldots,\delta_{\mathcal{T}_{r}}$ , with $\mathcal{T}_{j}:=\mathcal{T}_{\omega}(z_{j})$ , $z_{j}\in\mathcal{H}^{-1}(E)$ , belongs to $\mathcal{M}(\widehat{H}_{\hbar})$ . [...]
[4] arXiv:hep-th/0301066v2 | Harmonic oscillator on noncommutative spaces
  A generalized harmonic oscillator on noncommutative spaces is considered. Dynamical symmetries and physical equivalence of noncommutative systems with the same energy spectrum are investigated and discussed. General solutions of three-dimensional noncommutative harmonic oscillator are found and classified according to dynamical symmetries. We have found conditions under which three-dimensional non
  Full text (https://arxiv.org/html/hep-th/0301066v2), excerpts of its own sections:
  § I Introduction: Recently, it has been realized that noncommutatative geometry plays a distinguished role in the formulation of string theory [ 1 , 2 ] and M-theory [ 3 ] . It has been shown that, in a certain limit, the entire string dynamics can be described by minimally coupled gauge theory on noncommutative space [ 2 ] . Noncommutative field theory [ 4 ] has been constructed by introducing the Moyal product in the space of ordinary functions, and by defining field theory in quantum phase space. Equivalence between these two approaches has been clarified in Ref. [ 5 ] . Presumably, noncommutative effects are important at very high energies. Nevertheless, we could observe high-energy effects in the low-energy effective action, or we could use noncommutative geometry in constructing the low-energy effective action. For example, the noncommutative Chern-Simons gauge theory, represented as a matrix theory of elementary charges, has been used to describe quantum Hall physics [ 6 ] . [...]
  § II Noncommutative spaces in arbitrary dimensions: Let us define D-dimensional noncommutative coordinate operators $X_{1},\ldots,X_{D}$ and the corresponding noncommutative momentum operators $P_{1},\ldots,P_{D}$ with commutation relations $\displaystyle[X_{i},X_{j}]=i\theta_{ij},\;\;\;[P_{i},P_{j}]=iB_{ij},\;i,j=1,\ldots,D$ $\displaystyle[X_{i},P_{i}]=ih_{i},\;\;\;[X_{i},P_{j}]=i\left\{\begin{array}[]{cc}\phi_{ij}&i j\end{array}\right.$ and $X_{i},\;P_{i}$ are hermitean operators, $X_{i}^{\dagger}=X_{i},\;P_{i}^{\dagger}=P_{i}.$ The $2D-$ dimensional noncommutative phase space is described by variables $(U_{1},U_{2},\ldots,U_{2D})=(X_{1},P_{1},\ldots,X_{D},P_{D})$ satisfying $\displaystyle[U_{I},U_{J}]=iM_{IJ},\;\;\;U_{I}^{\dagger}=U_{I},\;{\scriptstyle I,J}=1,\ldots,2D,$ $\displaystyle M_{JI}=-M_{IJ},\;\;\;(M_{IJ})^{\dagger}=M_{IJ}.$ (4) Generally, $M_{IJ}$ is an operator depending on $U_{I}$ . However the Jacobi identities $[U_{I},[U_{J},U_{K}]]+{\rm cycl}.=0$ restrict the choice of the operators $M_{IJ}$ . [...]
  § III Isotropic noncommutative oscillator in arbitrary dimensions: The system is defined by the Hamiltonian $H=\frac{1}{2}\sum_{i=1}^{D}(P_{i}^{2}+X_{i}^{2})=\frac{1}{2}\sum_{I=1}^{2D}U_{I}^{2},$ (23) where the constants $\hbar$ , $m$ , and $\omega$ are absorbed in phase-space variables. The Hamiltonian ( 23 ) is invariant under $O(2D)$ transformations. The commutation relations are described by the c-numbers $M_{IJ}$ . [...]
  § V Discussion and outlook: We have considered a noncommutative, $O(2D)$ symmetric oscillator with constant (c-number) commutation relations $M_{ij}$ in $2D$ -dimensional nonsingular ( $\det M\neq 0$ ) phase-space. There exist two, physically distinct, phases, defined by $\kappa=\prod\omega_{i}\;{\scriptstyle{>\atop The dynamical symmetry of the noncommutative isotropic oscillator is $\prod U(D_{i}),\;\sum D_{i}=D$ . We have presented a family of matrices $M$ leading to the maximal $U(D)$ symmetry of the ho in D-dimensional noncommutative space, for $D We have presented a detailed analysis of the three-dimensional noncommutative ho. Our main result is the parametrization of the matrix $M$ for different dynamical symmetry groups, $U(3),U(2)\times U(1),[U(1)]^{3}$ . Especially, the most general conditions for maximal symmetry $U(3)$ are presented. We have shown that for a special parametrization of commutation relations, $h_{i}=1,\;\phi_{ij}=\psi_{ij}=0$ , there is no $U(3)$ symmetry. [...]
[5] arXiv:1001.1149v3 | The Bicomplex Quantum Harmonic Oscillator
  The problem of the quantum harmonic oscillator is investigated in the framework of bicomplex numbers, which are pairs of complex numbers making up a commutative ring with zero divisors. Starting with the commutator of the bicomplex position and momentum operators, and adapting the algebraic treatment of the standard quantum harmonic oscillator, we find eigenvalues and eigenkets of the bicomplex ha
  Full text (https://arxiv.org/html/1001.1149v3), excerpts of its own sections:
  § 1 Introduction: The mathematical structure of quantum mechanics consists in Hilbert spaces defined over the field of complex numbers  [ 1 ] . This structure has been extremely successful in explaining vast amounts of experimental data pertaining largely, but not exclusively, to the world of molecular, atomic and subatomic phenomena. That success has led a number of investigators, over many decades, to look for general principles or arguments that would lead quite inescapably to the complex Hilbert space structure. It has been argued  [ 2 , 3 ] , for instance, that the formulation of an uncertainty principle, heavily motivated by experiment, implies that a real Hilbert space can in fact be endowed with a complex structure. The proof, however, involves a number of additional hypotheses that may not be so directly connected with experiment. In fact Reichenbach  [ 4 ] has shown that a theory is not straightforwardly deduced from experiments, but rather arrived at by a process involving a good deal of instinctive inferences. [...]
  § 2 Bicomplex numbers and modules: This section summarizes basic properties of bicomplex numbers and finite-dimensional modules defined over them. The notions of scalar product and linear operators are also introduced. Proofs and additional material can be found in  [ 14 , 15 , 16 , 17 ] .
  § 2.1 Algebraic properties of bicomplex numbers: The set $\mathbb{T}$ of bicomplex numbers is defined as $\mathbb{T}:=\{w=w_{e}+w_{{{\rm{i}}_{1}}}{{\rm{i}}_{1}}+w_{{{\rm{i}}_{2}}}{{\rm{i}}_{2}}+w_{j}{\rm{j}}~|~w_{e},w_{{{\rm{i}}_{1}}},w_{{{\rm{i}}_{2}}},w_{j}\in\mathbb{R}\},$ (2.1) where ${{\rm{i}}_{1}}$ , ${{\rm{i}}_{2}}$ and ${\rm{j}}$ are imaginary and hyperbolic units such that ${\rm{i}}_{1}^{2}=-1={\rm{i}}_{2}^{2}$ and ${\rm{j}}^{2}=1$ . The product of units is commutative and defined as ${{\rm{i}}_{1}}{{\rm{i}}_{2}}={\rm{j}},\qquad{{\rm{i}}_{1}}{\rm{j}}=-{{\rm{i}}_{2}},\qquad{{\rm{i}}_{2}}{\rm{j}}=-{{\rm{i}}_{1}}.$ (2.2) With the addition and multiplication of two bicomplex numbers defined in the obvious way, the set $\mathbb{T}$ makes up a commutative ring. Three important subsets of $\mathbb{T}$ can be specified as $\displaystyle\mathbb{C}({\rm{i}}_{k})$ $\displaystyle:=$ $\displaystyle\{x+y{\rm{i}}_{k}~|~x,y\in\mathbb{R}\},\quad k=1,2;$ (2.3) $\displaystyle\mathbb{D}$ $\displaystyle:=$ $\displaystyle\{x+y{\rm{j}}~|~x,y\in\mathbb{R}\}. [...]
  § 5 Outlook and conclusion: Bicomplex numbers include complex numbers as a subset, just like hyperbolic numbers include real numbers. It should come as no surprise then that the eigenkets and eigenfunctions of the standard harmonic oscillator Hamiltonian can be recovered from the bicomplex ones. This, in fact, can be done in three different ways, as can be seen for instance from ( 3.47 ). First we set $\xi_{1}=1=\xi_{2}$ . We then let either (i) $w_{l\mathbf{1}}=\mathbf{e_{1}}$ and $w_{l^{\prime}\mathbf{2}}=0$ , or (ii) $w_{l\mathbf{1}}=0$ and $w_{l^{\prime}\mathbf{2}}=\mathbf{e_{2}}$ , or finally (iii) $l=l^{\prime}$ , $w_{l\mathbf{1}}=\mathbf{e_{1}}$ and $w_{l^{\prime}\mathbf{2}}=\mathbf{e_{2}}$ . In each case the eigenkets make up a structure isomorphic to the standard harmonic oscillator eigenvectors. The usual Hermite polynomials can similarly be recovered from the bicomplex ones. Looking at ( 4.21 ), we can see that both $P_{1}(H_{l}(\theta))$ and $P_{2}(H_{l}(\theta))$ are real-valued Hermite polynomials. So is $H_{l}(\theta)$ itself, in the special case where $\theta_{1}=\theta_{2}=\theta$ . [...]
[6] arXiv:2204.10780v1 | Anti-PT-symmetric harmonic oscillator and its relation to the inverted harmonic oscillator
  We treat the quantum dynamics of a harmonic oscillator as well as its inverted counterpart in the Schrödinger picture. Generally in the most papers of the literature, the inverted harmonic oscillator is formally obtained from the harmonic oscillator by the replacement of ω to iω, this leads to unbounded eigenvectors. This explicitly demonstrates that there are some unclear points involved in redef
  Full text (https://arxiv.org/html/2204.10780v1), excerpts of its own sections:
  § 1 Introduction: The inverted harmonic oscillator described by the following operator : $H^{\mathrm{r}}=\frac{1}{2m}p^{2}-\frac{1}{2}m\omega^{2}x^{2},$ (1) where the index $r$ specify inverted or repulsive, has attracted great attention over the years in quantum mechanics [ 1 ] - [ 4 ] . It is of course not positive definite but symmetric on the domain $\mathcal{D\subset}$ in the Hilbert space $\mathcal{H}$ endowed with scalar product $\left\langle.,.\right\rangle$ and related norm $\left\|.\right\|$ . It is well known that this system gives rise to a complex eigenvalues and a non physical eigenvectors although $H^{\mathrm{r}}$ is self-adjoint - the physical reason is that its potential is unbounded from below. The inverted harmonic oscillator,obtained by changing $\omega$ to $\pm i\omega$ in the harmonic oscillator, is often encountered as a phenomenological model in dessipative processes and has been used among others, as a model of instability in quantum mechanics [ 5 ] - [ 9 ] . [...]
  § 2 Generalized eigenfunction of the inverted harmonic oscillator: Let us first recall some properties of the harmonic oscillator which are useful to introduce the inverted oscillator. The Hamiltonian of the harmonic oscillator is : $H^{\mathrm{os}}=\frac{1}{2m}p^{2}+\frac{1}{2}m\omega^{2}x^{2},$ (4) and its the normalized eigenfunctions are given by means of Hermite polynomial $\psi_{n}^{\mathrm{os}}(x)=\frac{1}{\sqrt{2^{n}n!}}\left(\frac{\omega m}{\pi\hbar}\right)^{\frac{1}{4}}\exp\left[\frac{-\omega m}{2\hbar}x^{2}\right]H_{n}\left(\sqrt{\frac{\omega m}{\hbar}}x\right),$ (5) therefore the spectrum is discrete and the eigenvalues of ( 4 ) are non-negative real numbers which correspond to the quantized energy levels $E_{n}^{\mathrm{r}}=\hbar\omega(n+\frac{1}{2}),\text{ \ \ \ \ \ \ }\omega>0,$ (6) and the orthonormal condition is well preserved $\left\langle\psi_{m}^{\mathrm{os}}(x)\right.\left|\psi_{n}^{\mathrm{os}}(x)\right\rangle=\int\psi_{m}^{\ast\mathrm{os}}(x)\psi_{n}^{\mathrm{os}}(x)dx=\delta_{mn}\text{ },$ (7) naturally, the linear combination $\sum_{n}c_{n}\psi_{n}^{\mathrm{os}}(x)$ is a square integrable function for [...]
  § 3 Generalized coherent states for the inverted harmonic oscillator: One can verify that in the case of the inverted oscillator, the form of Hamiltonian ( 1 ) reads $H^{\mathrm{r}}=\frac{i\hbar\omega}{2}(\mathcal{\bar{A}}\text{ }\mathcal{A}+\mathcal{A}\text{ }\mathcal{\bar{A}}),$ (33) where the ladder operators $\left(\mathcal{A},\mathcal{\bar{A}}\right)$ are linked to [...]
  § 4 Conclusion: It is well known that the system described by the inverted oscillator gives rise to the generalized complex eigenvalues. The physical reason for that is the potential being unbounded from below. The corresponding energy eigenstates for ( 1 ) have been found in terms of the parabolic cylinder functions $D_{\nu}(x)$ [ 2 ] . Using a nonconventional technique, i.e. a quasi-Hermiticity in quantum mechanics, we have solved the problem relative to the inverted oscillator. In fact, we find that the system can be entirely expressed in terms of idealized states that are related to those of the harmonic oscillator. The connection with a harmonic oscillator may be established by the scaling operator $\rho$ ( 23 ). Ideal physical systems are conceptually Hermitian, but realistic systems are sometimes non-Hermitian because of their interactions with their environments. We have given the principal properties of the harmonic oscillator $H^{\mathrm{os}}$ formulation in quantum mechanics and we introduced the inverted oscillator $H^{\mathrm{r}}$ . [...]
[7] arXiv:1409.2468v3 | Harmonic Oscillators, Heisenberg's Uncertainty Principle and Simultaneous Measurement Precision for Position and Momentum
  At the recent QSCP XIX, the author claimed a procedure of using a scaled Fourier transform (the scaling being determined by the detailed interaction and particle mass for a harmonic oscillator) to achieve simultaneous resolution of position and momentum greater than the standard Heisenberg value of 1/2. The procedure is, in fact, invalid for quantum mechanics. The purpose of this paper is simply t
  Full text (https://ar5iv.labs.arxiv.org/html/1409.2468v3), excerpts of its own sections:
  § Submission history: From: Donald Kouri [ view email ] [v1] Mon, 8 Sep 2014 19:07:35 UTC (634 KB) [v2] Tue, 16 Sep 2014 18:42:22 UTC (636 KB) [v3] Fri, 6 Feb 2015 15:48:21 UTC (1 KB) (withdrawn) Full-text links:
  § Access Paper:: View a PDF of the paper titled Harmonic Oscillators, Heisenberg's Uncertainty Principle and Simultaneous Measurement Precision for Position and Momentum, by Donald J. Kouri Withdrawn No license for this version due to withdrawn
  § Current browse context:: quant-ph < prev | next > new | recent | 2014-09
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[8] arXiv:2009.07197v4 | Universal Mass Scale for Bosonic Fields in Multi-Brane Worlds
  In this paper we find an universal mass scale for all $q-$ forms in multi-brane worlds model. It is known that this model provides an ultralight mode for the fields. However, to get this, the Lagrangians considered in the literature are not covariant. In order to solve this, we propose a covariant version to multi-localize $q-$ form fields. As a consequence of the covariance, we show that all the 
  Full text (https://arxiv.org/html/2009.07197v4), excerpts of its own sections:
  § 1 Introduction: In 1998, as an extension of the Kaluza-Klein idea, Merab Gogberashvili created a shell model universe [ 1 ] where he deals with the hierarchy problem in a cosmological way. Some time ago, Randall-Sundrum (RS) presented two models in which gravity is trapped (or localized) in the membrane [ 2 , 3 ] . However, unlike gravity and the scalar field, the vector field is not trapped in the brane, this became a drawback in the RS model [ 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 ] . Despite of this, the massive modes can have peaks of probability over the brane, and show up as resonances. This tell us about unstable modes that in principle could be measured at the brane [ 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 ] . In order to circumvent the problem of localization, some authors introduced a Dilaton coupling [ 4 ] . Most of these models introduce other fields or nonlinearities to the gauge field [ 5 ] . Some years ago, Ghoroku et al proposed a mechanism that does not include new degrees of freedom and traps the gauge field to the membrane [ 8 ] . [...]
  § 2 Review of the $(+-+)$ Model: The $(+-+)$ model is a generalization of the (RS-I) model where an extra brane with positive tension is added and the negative tension brane is placed exactly in the middle of the two positive tension branes. The metric has the usual form $ds^{2}=e^{-2\sigma(y)}\eta_{\mu\nu}dx^{\mu}dx^{\nu}+dy^{2}$ , where $\sigma(y)=k(l-||y|-l|)$ . To determine the Kaluza-Klein (KK) spectrum of gravity, we use fluctuations of the metric $\delta g_{\mu\nu}=h_{\mu\nu}(x,y)=\sum_{n=0}^{\infty}h_{\mu\nu}^{n}(x)\psi^{n}(y)$ . After a change of variables $\frac{dz}{dy}=e^{\sigma(y)}=g(z)=k(z_{l}-||z|-z_{l}|)+1$ , the function $\psi^{n}(y)$ obeys the following Schrodinger differential equation $\left(-\frac{1}{2}\partial^{2}_{z}+V(z)\right)\hat{\psi}^{n}(z)=\frac{m_{n}^{2}}{2}e^{2\sigma(y)}\hat{\psi}^{n}(z).$ (1) That way, we have a quantum mechanical problem with delta function. The solution for the zero mode of ( 1 ) is found by making $m_{n}=0$ . For the rest of the modes the solution is given by Bessel functions. [...]
  § 3 Covariant Multi-Localization of Bosonic Fields: As said in the introduction, the mechanisms used by the authors of Ref. [ 47 ] has problems of non-covariance and free parameters. In this section we present two alternatives for the multi- localization of the $q-$ form field: a) the geometrical coupling and b) the coupling to the dilaton field. [...]
  § 4 Conclusion: Multi-brane worlds were introduced some time ago by Kogan et al. They discovered that the introduction of a third brane in the RSI model modifies gravity at large scales [ 46 ] . The authors found an ultralight mass modes for all the fields, given by $m_{1}^{2}=m_{1}\approx\sqrt{4\nu^{2}-1}ke^{-(\nu+1/2)kl}$ , where $\nu=3/2$ for gravity and has a range of possibilities for all the other fields. This would lead to new physics and the model was named“Multi-Brane worlds”. In order to reach the localization for fields other than gravity, the authors introduced a bulk and a brane mass terms given by $m^{2}=\alpha(\sigma^{\prime}(y)^{2})+\beta\sigma^{\prime\prime}(y)$ , where $\alpha,\beta$ are free parameters. Therefore the mass of such modes depends on a free parameter and are not fixed. Another point is that, despite working, the above mass term breaks the general covariance of the system. In order to solve the above problems we used a geometrical coupling proposed by some of us in Ref. [ 25 ] . For this we first consider the scalar and vector fields. [...]
[9] arXiv:2404.12780v1 | Piecewise Semi-Analytical Formulation for the Analysis of Coupled-Oscillator Systems
  A new simulation technique to obtain the synchronized steady-state solutions existing in coupled oscillator systems is presented. The technique departs from a semi-analytical formulation presented in previous works. It extends the model of the admittance function describing each individual oscillator to a piecewise linear one. This provides a global formulation of the coupled system, considering t
  Full text (https://arxiv.org/html/2404.12780v1), excerpts of its own sections:
  § I Introduction: Coupled oscillator systems can be used in several applications like power combination, beam-steering in phased-arrays [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ] or in sensor applications [ 8 , 9 , 10 ] , where the synchronization between the oscillators provides a common time-scale between the nodes of the sensor network. In previous works [ 11 , 12 ] a semi-analytical formulation (SAF) has been proposed to analyze the behavior of coupled oscillator systems. The SAF is a frequency-domain compact model of a voltage-controlled oscillator (VCO) under free-running conditions or in the presence of an injection source. It is based on the fact that, applying the implicit function theorem [ 11 , 12 ] , the whole Harmonic Balance system associated with the VCO can be compacted into a single equation in terms of a nonlinear admittance function $Y(V,\omega,\eta,G^{r},G^{i})$ . [...]
  § II-A Piecewise model of the individual VCO: The new technique presented here to model the behavior of each individual $i-$ th VCO in the array departs from the semi-analytical formulation presented in previous works [ 11 , 12 , 14 ] . The procedure is schematized in Fig. 1 . In this figure, the $i-th$ VCO of the system of coupled oscillators is represented together with a tuning voltage source $\eta_{i}$ and a current source $i_{s}(t)=I_{s}\cos(\omega_{s}t+\theta_{s})$ modeling the effect of an external injection source. For the sake of generality, the formulation will be derived for the general case where the injection source may be placed at any circuit node. The VCO is modeled by the first-harmonic component $I_{1}^{i}$ of the current entering the VCO from the output node $P$ . This component of each VCO will be introduced later in the system of equations modeling the array behavior. An expression for $I_{1}^{i}$ in terms of the VCO variables can be derived in the following way. [...]
  § II-B Formulation of the coupled-oscillator system: The schematic of the coupled oscillator system is shown in Fig. 4 . The output port of each oscillator element is loaded with a resistor $R_{L}=50\ \Omega$ and coupled to the neighbor elements through a linear network $\mathcal{C}_{I}$ , described by an $(2\times 2)$ admittance matrix [ 1 , 2 ] . In order to preserve the system symmetry, an additional monopole $\mathcal{C}_{L}$ providing an admittance reflection component $Y_{s}$ has been introduced to each edge oscillator. [...]
  § IV Conclusion: A new technique has been presented for the simulation of the synchronized solutions in arrays of coupled oscillators. The technique makes use of piecewise linear admittance functions to model each element of the array. These functions take into account the whole VCO characteristic, performing a global analysis that allows the maintenance of accuracy along the whole synchronization interval. The technique has been validated by comparison with circuit-level HB simulations in a free-running array of Van der Pol-type oscillators. Then, it has been applied to a coupled system of FET based oscillators at 5 GHz, in which the circuit-level HB technique is unable to converge. The synchronization ranges have been successfully predicted both under free-running conditions and injection-locked to an external generator. These results have been validated by comparison with measurements. In all cases, the new piecewise technique has shown a better accuracy than the previous non-piecewise one.
[10] QNFO: The RG-Harmonic Isomorphism: Synthesis of Eight Research Question Deliverables | https://papers.qnfo.org/papers/rg-harmonic-synthesis
  Synthesis paper unifying 8 research question deliverables from the RG-Harmonic Isomorphism spinoff program. Confirms the harmonic oscillator as the universal grammar of quantum theory across all 5 pillars.
  Full text (https://papers.qnfo.org/papers/rg-harmonic-synthesis), excerpts of its own sections:
  § 1.1 The Parent Thesis: The RG-Harmonic Isomorphism paper (https://papers.qnfo.org/papers/rg-harmonic-isomorphism/) advanced a provocative claim: the harmonic oscillator and the renormalization group are not merely analogous — they share a mathematical isomorphism rooted in the spectral decomposition of self-adjoint operators under scale transformations. [...]
  § 1.2 The Eight Questions: | RQ | Question | Pillar | System | |:---|:---------|:-------|:-------| | RQ1 | Transmon anharmonicity scaling $\alpha_r \propto (E_C/E_J)^\nu$ with $\nu = 1/2$? | V | Superconducting qubits | | RQ2 | ZPE unobservability formalized as a rigorous no-go theorem? | IV | QFT vacuum | | RQ3 | Log-periodic signatures in strongly coupled RG flows? [...]
  § RQ2: The ZPE Observability Theorem: **Claim formalized:** "In any Poincaré-invariant QFT with only local interactions and no dynamical gravity, the absolute zero-point energy density is unobservable — only energy *differences* between configurations produce measurable effects." **Result:** A no-go theorem is constructed with explicit assumptions ($\mathcal{A}_1$–$\mathcal{A}_5$), a formal proof structure, and systematic analysis of six edge cases: | Edge Case | ZPE Observable? | Consistent with Theorem? | |:----------|:---------------:|:------------------------:| | Casimir effect | No — configurational $\Delta E$ | Yes | | Lamb shift | No — level splitting | Yes | | Spontaneous emission | No — transition $\Delta E$ | Yes | | Cosmological constant | **Yes — requires gravity** | Yes (excluded by $\mathcal{A}_4$) | | Dynamical Casimir effect | No — time-varying $\Delta E$ | Yes | | Unruh effect | No — accelerated-observer $\Delta E$ | Yes | All 6/6 edge cases are consistent. [...]
  § 6. Cross-Domain Avenues (Master Work Plan v2.0 — X1–X6): The synthesis of eight deliverables surfaces six cross-domain research avenues that bridge the Adelic, Compton, and Harmonic domains. These are introduced here as a preview and will be fully elaborated in the Master Work Plan v2.0 cross-domain phase.
  § X6: Experimental Triple-Convergence: RQ1 (transmon), RQ3 (Efimov), and RQ8 ($\alpha$-running) all make specific, quantitative experimental predictions. X6 proposes a coordinated experimental campaign to test all three simultaneously: (a) precision transmon anharmonicity measurement at multiple $E_J/E_C$ values, (b) next-generation Efimov spectroscopy in cold atoms, and (c) high-precision $\alpha(Q^2)$ measurements at future colliders — seeking the predicted triple-convergence on $\nu \approx 1/2$, $\lambda = e^{\pi/s_0}$, and $\beta(\alpha) = 2\alpha^2/(3\pi)$. ---
  § 7. Conclusion: The eight research question deliverables synthesize into a unified architecture: the harmonic ladder — a single structure connecting the smallest measurable quantum system (transmon circuits, $10^{-6}$ m) to the largest theoretical construct (quantum gravity, $10^{-35}$ m) through a shared mathematical grammar. **Five convergent conclusions:** 1. **The harmonic oscillator is the universal IR attractor** — confirmed quantitatively at the sub-percent level in transmon circuits (RQ1, $\nu = 0.5084 \pm 0.017$, BF $= 9.3 \times 10^{18}$), structurally in the SM gauge sector (RQ4, MSSM $\Delta M_{\text{GUT}} < 12\%$), and formally in the ZPE no-go theorem (RQ2, 6/6 edge cases). 2. **The renormalization group is the scale-space syntax** — the $\beta$-function is the Hamiltonian of theory space, fixed points are stationary states, and the Callan-Symanzik equation is the Schrödinger equation of RG flows (Pillar III, RQ8). 3. [...]
[11] QNFO: Is the Harmonic Oscillator an Infrared Attractor in All Places? A Place‑Resolved Analysis of the Harmonic Paradigm | https://papers.qnfo.org/papers/is-the-harmonic-oscillator-an-infrared-attractor-in-all-places-a-place-resolved-
  The universal infrared (IR) attractor claim for the quantum harmonic oscillator (HO) has been examined only over the Archimedean absolute value on ℚ. This work asks whether the attractor status survives under the non‑Archimedean $p$‑adic and adelic norms. We construct a place‑resolved renormalization‑group (RG) framework, define a dimensionless distance $\alpha_v$ from a flowing bosonic system to 
  Full text (https://papers.qnfo.org/papers/is-the-harmonic-oscillator-an-infrared-attractor-in-all-places-a-place-resolved-), excerpts of its own sections:
  § 1. Introduction: Quantum engineers and theorists rely on the Harmonic Paradigm’s claim that the quantum harmonic oscillator (HO) is the universal infrared (IR) attractor of bosonic systems: generic bosonic models flow toward oscillator‑like behavior at long wavelengths, simplifying the design of bosonic error‑correcting codes and quantum batteries. In practice, this claim underpins the engineering of bosonic quantum memories, where the HO provides a tractable effective description that reduces control complexity and resource overhead. However, the attractor statement implicitly quantifies over a number field equipped with an absolute value. [...]
  § 5. Results: *R1 (exact).* The adelic product formula holds for $x=2/3$, $5/7$, and $3/4$ (A1). *R2 (exact, model‑based).* Under $E^{(p)}_n=E_0p^{-n}$, the $p$‑adic gap ratio equals $p$ for $p=2,3,5$ (A3), distinct from the constant Archimedean gap. *R3 (exact, model‑based).* Vertex counts grow as $(p+1)p^{n-1}$; cumulative counts through depth 5 are $S_2(5)=94$ and $S_3(5)=485$ (A2). *R4 (projection, assumed $\gamma_v=0.1$, linearized flow).* With $\gamma_v=0.1$, $\alpha_v(\ell)=e^{-0.1\ell}$ yields $\alpha_v(20)\approx0.135335$, $\alpha_v(40)\approx0.018316$, $\alpha_v(60)\approx0.002479$ (A4). *R5 (exact).* The product‑of‑distances hypothesis fails for generic $\gamma_v$; constancy would require $\sum_v\gamma_v=0$, which the adelic product formula does not enforce (A5). *R6 (structural).* The adelic product formula constrains amplitudes (A6) but not spectra; thus attraction can exist in each place with spectrally different fixed points, supporting option (c): structural transformation.
  § 6. Discussion: **Limitations.** - The $p$‑adic level formula $E^{(p)}_n=E_0\,p^{-n}$ is a modeling assumption; consequently, all quantitative statements that depend on this ladder (R2, R3) inherit this status. - The linearized RG flow with $\gamma_v=0.1$ is illustrative; real systems may exhibit non‑exponential behavior. - The linkage test examined only a three‑place product of distances; richer adelic constraints (e.g., involving local $L$‑factors) remain unexplored. **Failure modes and self‑critique.** - If the true $p$‑adic spectrum possessed constant gaps, R2 would collapse and the verdict would shift toward preservation (option a). - If generic $p$‑adic systems exhibited $\gamma_p<0$, the verdict would move toward mixed preservation/repulsion (option b). **What would falsify the claims.** 1. An exact $p$‑adic spectrum with constant gaps would falsify R2. 2. A derivation forcing $\sum_v\gamma_v=0$ from adelic dynamics would falsify R5 and revive a strong place‑invariance claim. 3. [...]
  § 8. Conclusion: We asked whether the harmonic oscillator’s status as an IR attractor is place‑invariant. Within a place‑resolved RG framework, with explicit derivations and clearly labeled modeling assumptions, we find that the oscillator can attract in each place but with spectrally different fixed points—constant gaps in ℝ versus geometric gaps in ℚ$_{p}$ organized on Bruhat–Tits tree levels. The adelic product formula constrains amplitudes, not spectra, imposing no linkage between place‑wise attractor distances. Thus the Harmonic Paradigm’s attractor thesis is not an Archimedean artifact (attraction is not reversed) but also not strongly place‑invariant; it is structurally transformed. The most urgent open task is the exact computation of the $p$‑adic oscillator spectrum, which would turn the present model‑based conclusions into rigorous theorems.
[12] QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis | https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation
  Systematic Ostrowski-completion-theoretic audit of the Harmonic Paradigm V1.0-V4.0. Five findings: (1) Beta-function mechanism is infinity-place-specific -- Missarov (1989) confirms different universality class. (2) Q_p not ordered -- eliminates S-matrix, Noether, measurement. (3) pi IS adelic -- pi_p = (p-1)/p at each prime p. (4) alpha = r_e/lambda_C is a length ratio with rational core 137/60 h
  Full text (https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation), excerpts of its own sections:
  § 1.1 The Harmonic Paradigm: The Harmonic Paradigm (HP) V1.0--V4.0 (2026, DOIs https://papers.qnfo.org/papers--21505993) proposed that the quantum harmonic oscillator functions as the universal IR attractor of quantum theory [@qnfo-harmonic-v1; @qnfo-harmonic-v4]. The framework spanned an 8-rung ladder: 1. Transmon anharmonicity (artificial atoms) 2. Phonon equal spacing (lattice vibrations) 3. Molecular vibrations (IR spectroscopy) 4. QED β-function (fine-structure constant, Landau pole) 5. QCD β-function (asymptotic freedom) 6. GUT scale (gauge coupling unification) 7. p-Adic oscillator (Bruhat--Tits tree) 8. Quantum gravity (ultrametric closure, Wheeler--DeWitt) The HP closed out formally in V4.0 [@qnfo-harmonic-v4], retracting its central logistic β-function ansatz $\beta(\alpha) = B\cdot\alpha(1-\alpha)$ after direct calculation showed it incompatible with the textbook QED β-function $\beta(\alpha) = (2/3\pi)\alpha^2$. The logistic ansatz is linear at leading order; real QED is quadratic.
  § 1.2 The Unresolved Non-Archimedean Question: HP V1.0's bibliography cited Vladimirov-Volovich-Zelenov *p-Adic Analysis and Mathematical Physics* (1994) [@VVZ1994] and Ostrowski's theorem (1918) [@Ostrowski1918]. The researcher motivation (Note 3) referenced "Ostrowski's theorem, ultrametric structures, non-Archimedean thinking." Rungs 7--8 explicitly invoke p-adic oscillators, Bruhat--Tits trees, and ultrametric quantum gravity. Yet the HP's core physical mechanism -- the $\beta$-function analysis, the equal-$\ln(\mu)$-spacing order-statistics test, the power-law vs.\ logarithmic IR approach -- was tested **exclusively over $\mathbb{R}$** (the Archimedean/$\infty$-place). This paper asks: *Do any of the HP's mechanisms survive when tested at non-Archimedean completions, or was the HP an Archimedean-only theory with a non-Archimedean bibliography?*
  § 1.3 Ostrowski's Theorem as the Framework: Ostrowski's theorem (1918) [@Ostrowski1918] classifies all non-trivial absolute values on $\mathbb{Q}$: - The Archimedean absolute value $|\cdot|_\infty$ (the usual real absolute value) - The p-adic absolute values $|\cdot|_p$ for each prime $p$ The adele ring $\mathbb{A}_\mathbb{Q} = \mathbb{R} \times \prod'_p \mathbb{Q}_p$ is the restricted product of all completions. Every rational number $q \in \mathbb{Q}$ embeds diagonally: $q \mapsto (q, q, q, \ldots)$. The product formula: $$ \prod_v |q|_v = 1, \quad \forall q \in \mathbb{Q}^\times $$ is the arithmetic identity connecting all places [@Cassels1986]. If the HP's physical quantities are defined over $\mathbb{Q}$ (or are ratios of such quantities), they have well-defined completions at EVERY place. The question is not "do p-adic completions exist?" but "what are their values?" ___
  § 11.1 Core Conclusion: The Harmonic Paradigm was an **Archimedean-only theory** that invoked non-Archimedean structures (Vladimirov, Bruhat--Tits, Ostrowski) bibliographically without computing p-adic values. Its core mechanism (the $\beta$-function IR attractor) is inherently $\infty$-place-specific. However, the related quantities $\pi$, $\alpha$, $m$, $\lambda_C$, and $r_e$ ARE adelic -- they exist at every Ostrowski completion -- and the HP simply never computed their p-adic values. The Helical Compton Vortex provides a unified framework in which $\pi$, $\alpha$, and $m$ are projections of a single adelic topological excitation: the electron as a helical standing wave whose pitch-to-radius ratio is $\alpha$, whose torsion frequency is $m$, and whose transverse projection at each place produces $\pi_v$.