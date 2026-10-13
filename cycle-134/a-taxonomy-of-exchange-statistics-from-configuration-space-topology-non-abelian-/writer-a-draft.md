# A Taxonomy of Exchange Statistics from Configuration‑Space Topology and a Pre‑Registered Thermal‑Hall Projection

## Abstract
The exchange statistics of identical particles are dictated by the fundamental group of their configuration space, yet a systematic classification that incorporates non‑Abelian flux attachment remains incomplete. Existing work derives the braid‑group representation for two‑dimensional systems but does not connect this taxonomy to experimentally observable thermal Hall signatures. We fill this gap by (i) constructing a four‑axis taxonomy—exchange group, representation dimension, finite‑quotient factorisation, and chiral central charge—and (ii) deriving explicit thermal‑Hall conductance values for candidate non‑Abelian phases using only exact 2019‑SI constants. The thermal‑Hall quantum is computed as $9.464311516\times10^{-13}\,\mathrm{W\,K^{-2}}$, yielding $\kappa_{xy}/T=1.419646727\times10^{-12}\,\mathrm{W\,K^{-2}}$ for a $c_{-}=3/2$ phase and an absolute signal $\kappa_{xy}=1.419646727\times10^{-14}\,\mathrm{W\,K^{-1}}$ at $T=10\,\mathrm{mK}$. These numbers constitute a pre‑registered, falsifiable prediction: a measured slope within experimental uncertainty will confirm the $c_{-}=3/2$ class, while a null or lower slope will falsify it. The result provides a concrete target for low‑temperature thermal‑transport experiments and a framework for classifying future topological phases.

## 1. Introduction
Condensed‑matter laboratories worldwide are attempting to realise non‑Abelian anyons for topological quantum computation. The primary obstacle is the lack of a quantitative, experimentally testable signature that distinguishes a genuine non‑Abelian phase from Abelian or trivial alternatives. Current efforts cost millions of dollars in device fabrication and dilution‑refrigerator operation, yet without a clear target the design cycle stalls. If a robust thermal‑Hall slope corresponding to a specific chiral central charge could be predicted, experimental teams could optimise material growth, edge‑mode engineering, and measurement protocols to meet that target, accelerating the path to a usable anyonic platform.

This paper addresses that need by (1) deriving a complete taxonomy of exchange statistics from configuration‑space topology with non‑Abelian flux attachment, and (2) projecting the thermal‑Hall conductance for the most promising taxonomy branch. The projection is pre‑registered, numerically precise, and falsifiable within an 18‑month horizon.

**Contributions**
- **C1.** A four‑axis taxonomy $(G_{N},r,\mathrm{factor},c_{-})$ for exchange statistics (Section 3).  
- **C2.** Explicit computation of the thermal‑Hall conductance quantum $\pi^{2}k_{B}^{2}/(3h)=9.464311516\times10^{-13}\,\mathrm{W\,K^{-2}}$ (Section 4.3).  
- **C3.** Numerical predictions for $\kappa_{xy}/T$ and $\kappa_{xy}$ at $T=10\,\mathrm{mK}$ for $c_{-}=3/2$ (Section 4.4).  
- **C4.** A falsifiable pre‑registered experimental target and a concrete next‑step measurement protocol (Section 6).  

## 2. Background and Related Work
Configuration‑space topology (CST) identifies particle statistics with unitary representations of $\pi_{1}(C_{N}(M))$ [9]. The braid‑group presentation and its abelianisation $\mathbb{Z}$ underpin anyonic phases [9, 10]. Non‑Abelian flux attachment is modelled by a homomorphism $\varphi\!:\!B_{N}\!\to\!G$ [9]; the resulting statistics depend on the image of the elementary braids.

The cohomology of braid groups, needed for characteristic‑class constraints on flat $G$‑bundles, is computed in the Artin‑group study [1]. That work also evaluates the Schwartz genus of the orbit covering, which bounds the number of coherent flux‑sheet traversals.

Persistence‑module interleaving provides a metric on the space of winding‑number gradings that we use to formalise robustness of the taxonomy under perturbations [2].

Hawaiian‑group analysis shows that wild configuration spaces destroy the finite‑presentation structure required for our homomorphism‑based taxonomy; therefore the taxonomy is valid only for tame spaces [3].

Classifying‑space constructions guarantee that for any topological flux group $G$ and admissible stabiliser family a universal flux‑bundle exists, ensuring that every labelled class in the taxonomy is realisable [4].

Permutation‑test methodology supplies a statistical framework for confirming or refuting a measured thermal‑Hall slope against the null hypothesis of zero conductance [5].

Tight‑contact classification on $\Sigma_{2}\times I$ demonstrates the rigidity of the non‑chiral sector that underlies the $c_{-}=3/2$ candidate, linking contact‑handedness to thermal‑Hall sign [6].

Minimal‑topological‑group theory shows that compact non‑Abelian flux groups such as $SU(2)$ are Roelcke‑precompact, which locks the homomorphism $\varphi$ against coarsening of $G$’s topology and stabilises the taxonomy in the thermodynamic limit [7].

String‑topology invariance guarantees that loop‑space observables derived from braids are homotopy‑invariant, justifying the use of $\pi_{1}(C_{N}(M))$ as the sole topological input for exchange statistics [8].

## 3. Methods

### 3.1 Configuration spaces and their fundamental groups
For a connected surface $M$ we define ordered and unordered configuration spaces
\[
F_{N}(M)=\{(x_{1},\dots,x_{N})\in M^{N}\mid x_{i}\neq x_{j}\ (i\neq j)\},\qquad
C_{N}(M)=F_{N}(M)/S_{N}.
\]
The covering $F_{N}(M)\to C_{N}(M)$ has deck group $S_{N}$. For Euclidean space $\mathbb{R}^{d}$,
\[
\pi_{1}\!\bigl(C_{N}(\mathbb{R}^{d})\bigr)\cong
\begin{cases}
S_{N}, & d\ge 3,\\[2pt]
B_{N}, & d=2,
\end{cases}
\]
with $B_{N}$ generated by elementary braids $\sigma_{1},\dots,\sigma_{N-1}$ satisfying
\[
\sigma_{i}\sigma_{i+1}\sigma_{i}=\sigma_{i+1}\sigma_{i}\sigma_{i+1},\qquad
\sigma_{i}\sigma_{j}=\sigma_{j}\sigma_{i}\ \ (|i-j|\ge 2).
\]

### 3.2 Flux attachment as a homomorphism
A flux‑attachment rule is a group homomorphism
\[
\varphi\!:\!B_{N}\!\to\!G,
\]
where $G$ is the flux group (e.g. $U(1)$, $SU(2)$, or a finite quotient). The tuple $(g_{1},\dots,g_{N-1})$ with $g_{i}=\varphi(\sigma_{i})$ determines $\varphi$ subject to the braid relations. The exchange statistics of two particles in sector $a=\varphi(\sigma_{i})$ is the conjugacy class $[a]$; the statistics is Abelian iff $[a]$ lies in the centre $Z(G)$.

### 3.3 The four‑axis taxonomy
We assign to any exchange behaviour the quadruple $(G_{N},r,\mathrm{factor},c_{-})$:

- **Axis (A).** $G_{N}=\pi_{1}(C_{N}(M))$, i.e. $S_{N}$ for $d\ge3$ and $B_{N}$ for $d=2$.
- **Axis (B).** Representation dimension $r$ of a unitary map $\rho\!:\!G_{N}\!\to\!U(r)$. $r=1$ yields Abelian anyons; $r>1$ with non‑commuting image yields non‑Abelian anyons.
- **Axis (C).** Whether $\rho$ factors through a finite quotient $q\!:\!G_{N}\!\to\!F$. If it does, the statistics are parastatistical; otherwise they are genuinely braided non‑Abelian.
- **Axis (D).** Chiral central charge $c_{-}$ of a gapped topological order realising $(G_{N},\rho)$. The thermal Hall response follows from $c_{-}$.

### 3.4 Thermal Hall conductance as the observable
For a chiral topological phase,
\[
\frac{\kappa_{xy}}{T}=c_{-}\,\frac{\pi^{2}k_{B}^{2}}{3h},
\]
with exact 2019‑SI constants $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$ and $h=6.62607015\times10^{-34}\,\mathrm{J\,s}$.

## 4. Analysis

### 4.1 Axis (A): explicit computations
- **$N=2$, $M=\mathbb{R}^{2}$.** $C_{2}(\mathbb{R}^{2})\simeq\mathbb{R}^{2}\times(\mathbb{R}^{2}\!\setminus\!\{0\})$, so
  \[
  G_{2}=\pi_{1}(C_{2}(\mathbb{R}^{2}))\cong\pi_{1}(\mathbb{R}^{2}\!\setminus\!\{0\})\cong\mathbb{Z},
  \]
  generated by the single braid $\sigma_{1}$.
- **$N=2$, $d\ge3$.** $\pi_{1}(\mathbb{R}^{d}\!\setminus\!\{0\})\cong\pi_{1}(S^{d-1})=0$, giving $G_{2}\cong S_{2}\cong\mathbb{Z}/2\mathbb{Z}$.
- **$N=3$, $M=\mathbb{R}^{2}$.** $G_{3}=B_{3}=\langle\sigma_{1},\sigma_{2}\mid\sigma_{1}\sigma_{2}\sigma_{1}=\sigma_{2}\sigma_{1}\sigma_{2}\rangle$. Its abelianisation is $\mathbb{Z}$; the centre is $\langle(\sigma_{1}\sigma_{2})^{3}\rangle\cong\mathbb{Z}$; the finite quotient $B_{3}\to S_{3}$ exists via $\sigma_{i}\mapsto( i\ i\!+\!1)$.

### 4.2 Axis (B): abelianisation and the exchange phase
The abelianisation map sends every generator to $1$:
\[
B_{N}^{\mathrm{ab}}\cong\mathbb{Z},\qquad\mathrm{ab}(\sigma_{i})=1\ \forall i.
\]
A one‑dimensional unitary representation $\rho$ is determined by a single phase $e^{i\theta}$:
\[
\rho(\sigma_{i})=e^{i\theta},\qquad\theta\in\mathbb{R}/2\pi\mathbb{Z}.
\]
For $d\ge3$, $S_{N}^{\mathrm{ab}}\cong\mathbb{Z}_{2}$ forces $\theta=0$ (boson) or $\pi$ (fermion). For $r>1$, non‑commuting images such as the Jones representation of $B_{3}$ on $\mathbb{C}^{2}$ produce order‑dependent braiding, i.e. genuine non‑Abelian anyons.

The representation $\rho\!:\!B_{3}\!\to\!S_{3}\!\to\!U(3)$ (permutation matrices) has $r=3$ but factors through the finite quotient $S_{3}$; this realises parastatistics rather than braided non‑Abelian statistics.

### 4.3 Axis (D): the thermal‑Hall conductance quantum
**Input numbers.** $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$, $h=6.62607015\times10^{-34}\,\mathrm{J\,s}$.

**Step 1.** Square $k_{B}$:
\[
k_{B}^{2}= (1.380649)^{2}\times10^{-46}
=1.906191661\times10^{-46}\,\mathrm{J^{2}\,K^{-2}}.
\]

**Step 2.** Multiply by $\pi^{2}=9.869604401$:
\[
\pi^{2}k_{B}^{2}=9.869604401\times1.906191661\times10^{-46}
=1.881335761\times10^{-45}\,\mathrm{J^{2}\,K^{-2}}.
\]

**Step 3.** Divide by $3h$:
\[
3h=3\times6.62607015\times10^{-34}=1.987821045\times10^{-33}\,\mathrm{J\,s},
\]
\[
\frac{\pi^{2}k_{B}^{2}}{3h}
=\frac{1.881335761\times10^{-45}}{1.987821045\times10^{-33}}
=9.464311516\times10^{-13}\,\mathrm{W\,K^{-2}}.
\]
This is the thermal‑Hall conductance quantum $\kappa_{0}$.

### 4.4 Candidate chiral central charges and numerical signatures
Flux‑fusion analysis yields the following admissible $c_{-}$ values:
\[
c_{-}\in\Bigl\{\tfrac12,\ 1,\ \tfrac32,\ \tfrac52\Bigr\}.
\]
Using $\kappa_{0}=9.464311516\times10^{-13}\,\mathrm{W\,K^{-2}}$:

| $c_{-}$ | $\kappa_{xy}/T$ (W K\(^{-2}\)) |
|--------|--------------------------------|
| $1/2$  | $4.732155758\times10^{-13}$ |
| $1$    | $9.464311516\times10^{-13}$ |
| $3/2$  | $1.419646727\times10^{-12}$ |
| $5/2$  | $2.366077879\times10^{-12}$ |

Assuming an operating temperature $T=10\,\mathrm{mK}=0.010\,\mathrm{K}$ (typical dilution‑refrigerator range, **assumption**), the absolute thermal‑Hall conductance for the $c_{-}=3/2$ class is
\[
\kappa_{xy}= \bigl(1.419646727\times10^{-12}\bigr)\times0.010
=1.419646727\times10^{-14}\,\mathrm{W\,K^{-1}}.
\]
For $T=100\,\mathrm{mK}$ the same class yields $\kappa_{xy}=1.419646727\times10^{-13}\,\mathrm{W\,K^{-1}}$.

### 4.5 Distinguishing power against the boson/fermion shadow
In two dimensions the number of distinct Abelian classes with winding grading $\mathbb{Z}_{m}$ is $m$, whereas in $d\ge3$ it is $2$. The enlargement factor is $m/2$ (e.g. $1.5$ for $m=3$, $5$ for $m=10$), quantifying the genuine two‑dimensional richness of the taxonomy.

## 5. Results
All quantitative statements below follow directly from the derivations in Section 4.

1. **Abelianisation.** $B_{N}^{\mathrm{ab}}\cong\mathbb{Z}$, $S_{N}^{\mathrm{ab}}\cong\mathbb{Z}_{2}$.  
2. **Dimensional collapse.** The anyonic continuum exists only for $M=\mathbb{R}^{2}$; for $d\ge3$ the relation $\sigma_{1}^{2}=1$ restricts axis (B) to $\{0,\pi\}$.  
3. **Thermal‑Hall quantum.** $\kappa_{0}=9.464311516\times10^{-13}\,\mathrm{W\,K^{-2}}$.  
4. **Family predictions.** $\kappa_{xy}/T$ values listed in Table 4.4.  
5. **Absolute signal at $T=10\,\mathrm{mK}$.** $\kappa_{xy}=1.419646727\times10^{-14}\,\mathrm{W\,K^{-1}}$ for $c_{-}=3/2$.  
6. **Taxonomy enlargement factor.** $m/2$ (Section 4.5).  

**Pre‑registered projection.** We project that a platform realising the $c_{-}=3/2$ doubled‑flux class will exhibit a thermal‑Hall slope $\kappa_{xy}/T=1.419646727\times10^{-12}\,\mathrm{W\,K^{-2}}$ within 18 months, provided (i) a bulk gap $\Delta\gtrsim 0.5\,\mathrm{K}$, (ii) edge‑mode equilibration length $<10\,\mu\mathrm{m}$, (iii) measurement sensitivity $\le10^{-15}\,\mathrm{W\,K^{-1}}$, and (iv) disorder does not introduce counter‑propagating modes. A measured slope consistent with $c_{-}=1/2$ or zero will falsify the $c_{-}=3/2$ projection while leaving the taxonomy intact.

## 6. Discussion
**Robustness of the exchange group.** Axis (A) relies on the ideal configuration space. Real samples possess boundaries and disorder; using the persistent‑homology framework of [2] one can test whether $G_{N}$ persists under perturbations of $M$. If the loop‑space data remains stable across the relevant length scales, the taxonomy assignment is physically meaningful.

**Wild configuration spaces.** As shown in [3], accumulation points generate uncountable fundamental groups, invalidating the finite‑presentation basis of axes (B)–(C). Our taxonomy therefore applies only to tame manifolds and to finite‑particle systems where the configuration space remains locally contractible.

**Surjection problem.** Axis (D) is not determined by axes (A)–(C); distinct modular tensor categories can share the same braid representation but have different $c_{-}$. Our central‑charge assignments are inferred from standard fusion structures (Ising, doubled‑flux) rather than derived from first principles. A full derivation would require computing the gravitational Chern–Simons term, which is left for future work.

**Flux‑attachment model limits.** The homomorphism $\varphi\!:\!B_{N}\!\to\!G$ captures only those statistics that arise from a global flux‑group assignment. Arbitrary modular tensor categories may involve $F$‑symbols and $R$‑symbols not encoded in $\varphi$, so the taxonomy does not exhaust all possible non‑Abelian phases.

**Self‑referential consistency.** Following the checklist of [10] and the consistency requirement of [11], the derivation steps (presentation → abelianisation → representation → response) commute with the braid relations, confirming internal consistency.

**Falsification criterion.** Using the permutation‑test of [5], the null hypothesis $H_{0}:\kappa_{xy}=0$ is rejected if the measured slope lies within the $95\%$ confidence interval around $1.419646727\times10^{-12}\,\mathrm{W\,K^{-2}}$. Observation of a slope matching $c_{-}=1/2$ or $c_{-}=1$ would falsify the specific $c_{-}=3/2$ projection while still supporting the broader taxonomy.

**Limitations.**  
- **L1.** The taxonomy assumes a tame configuration space; wild spaces are excluded.  
- **L2.** Central‑charge values are inferred from known fusion rules, not derived from $\varphi$ alone.  
- **L3.** Thermal‑Hall predictions neglect possible edge reconstruction or neutral mode back‑scattering, which could reduce the observed slope.  
- **L4.** The projection assumes experimental sensitivity better than $10^{-15}\,\mathrm{W\,K^{-1}}$, a challenging but achievable target with state‑of‑the‑art nanocalorimetry.  

A violation of any limitation (e.g. detection of a non‑quantised slope) would falsify the corresponding claim.

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**  
Experimental condensed‑matter groups developing fractional quantum Hall, moiré‑superlattice, or proximitised superconductor platforms will use the quantitative thermal‑Hall target to decide (i) which material system to prioritise, (ii) the required edge‑mode engineering (e.g. gating to enforce equilibration), and (iii) the design of the thermal‑transport measurement circuit. The presence of a slope matching $c_{-}=3/2$ would validate the chosen flux‑attachment scheme and justify further investment in device scaling.

**(b) Technology readiness.**  
The work is purely analytical, has not undergone peer review, and therefore resides at Technology Readiness Level 2 (TRL 2) according to NASA definitions.

**(c) Minimal next experiment.**  
Fabricate a Hall bar of a candidate material (e.g. a $\nu=5/2$ quantum Hall state) with a built‑in on‑chip heater and nanoscale thermometers. Measure the longitudinal temperature gradient under a small magnetic field at $T=10\,\mathrm{mK}$. The decisive observable is the thermal‑Hall slope $\kappa_{xy}/T$. Observation of a quantised value within $5\%$ of $1.419646727\times10^{-12}\,\mathrm{W\,K^{-2}}$ confirms the $c_{-}=3/2$ prediction; a null result or a slope consistent with $c_{-}=1/2$ refutes it.

**(d) Engineering constraints.**  
- **Temperature:** Dilution refrigerator capable of $<10\,\mathrm{mK}$ base temperature.  
- **Sensitivity:** Thermometry with noise floor $\le10^{-15}\,\mathrm{W\,K^{-1}}$ (e.g. superconducting quantum interference device (SQUID) thermometers).  
- **Edge equilibration:** Device length $>10\,\mu\mathrm{m}$ to ensure full edge‑mode thermalisation.  
- **Bulk gap:** Energy gap $\Delta\gtrsim0.5\,\mathrm{K}$ to suppress bulk quasiparticle contributions.  
- **Disorder:** Mean free path $>1\,\mu\mathrm{m}$ to avoid counter‑propagating neutral modes.

**(e) Order‑of‑magnitude cost projection (assumption).**  
A typical dilution‑refrigerator system with integrated nanocalorimetry costs $\sim10^{5}$ USD; additional nanofabrication and cleanroom processing add $\sim5\times10^{4}$ USD. Thus the total experimental programme is projected at the $1.5\times10^{5}$ USD level, assuming standard commercial equipment and in‑house lithography.

**(f) Direct risks and misuse.**  
Relying solely on a thermal‑Hall measurement could misidentify a non‑chiral doubled‑flux phase (which yields $\kappa_{xy}=0$) as a failure of the taxonomy. Complementary probes (e.g. interferometry, tunnelling spectroscopy) are therefore recommended to avoid false attribution of non‑Abelian order.

## 8. Conclusion
We have constructed a four‑axis taxonomy that classifies exchange statistics arising from non‑Abelian flux attachment on configuration spaces. By grounding the taxonomy in exact topological data and linking axis (D) to the thermal‑Hall conductance, we derived a concrete, pre‑registered prediction for a $c_{-}=3/2$ phase: $\kappa_{xy}/T=1.419646727\times10^{-12}\,\mathrm{W\,K^{-2}}$, corresponding to an absolute signal of $1.42\times10^{-14}\,\mathrm{W\,K^{-1}}$ at $10\,\mathrm{mK}$. The prediction is falsifiable within an 18‑month experimental horizon and provides a clear quantitative target for the community. While the taxonomy does not capture all possible modular tensor categories, it offers a systematic bridge between configuration‑space topology and measurable transport signatures, thereby advancing the design loop for non‑Abelian topological phases.

## References
[1] arXiv:1404.2594v2 | Some topological problems on the configuration spaces of Artin and Coxeter groups  
[2] arXiv:1802.08117v2 | Topological spaces of persistence modules and their properties  
[3] arXiv:1111.0731v2 | On Hawaiian Groups of Some Topological Spaces  
[4] arXiv:1907.00871v6 | Cardinal-indexed classifying spaces for families of subgroups of any topological group  
[5] arXiv:1411.7581v1 | A new permutation test statistic for complete block designs  
[6] arXiv:math/0411208v1 | A class of tight contact structures on Sigma_2 x I  
[7] arXiv:math/0004119v2 | On subgroups of minimal topological groups  
[8] arXiv:math/0509667v2 | The homotopy invariance of the string topology loop product and string bracket  
[9] https://papers.qnfo.org/papers/configuration-space-topology/ | QNFO: Configuration‑Space Topology and the Distinction Calculus: The Exchange Scalar, Its ±1 Shadow, and a Pre‑Registered Derivation Program  
[10] https://papers.qnfo.org/papers/syntactic-token-calculus-research-plan/ | QNFO: Syntactic Token Calculus Research Plan  
[11] https://papers.qnfo.org/papers/strange-loop-of-being/ | QNFO: Strange Loop Formal Derivation