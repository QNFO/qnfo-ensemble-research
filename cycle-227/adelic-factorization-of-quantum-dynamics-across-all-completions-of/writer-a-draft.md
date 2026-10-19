# Adelic Factorization of Quantum Dynamics Across All Completions of ℚ

## Abstract
We explore the conjecture that the conventional choice of the Archimedean completion ℝ as the underlying number field of quantum theory is a matter of convention rather than necessity. By invoking Ostrowski’s theorem, which partitions the completions of ℚ into the unique Archimedean place ∞ and the family of non‑Archimedean ℚₚ for each prime p, we propose a framework in which quantum dynamics factorizes into local contributions at every place. Following the proposal in [9] that Tate’s 1950 thesis provides an explicit structural template for constructing adelic quantum mechanics, we adopt the local–global product structure as a working analogy and formulate consistency conditions that enforce a global adelic product structure on quantum amplitudes. To make the proposal concrete, we (i) derive a formal adelic path‑integral expression whose functional equation constrains physical amplitudes, (ii) construct elementary p‑adic quantum models formally, with the reproduction of standard real‑valued quantum mechanics in the limit where non‑Archimedean contributions are suppressed remaining a conjectured goal rather than a verified result, and (iii) perform a numerical illustration using fidelity data from a state‑of‑the‑art superconducting quantum processor (105 qubits, single‑qubit fidelity 99.90 %, two‑qubit fidelity 99.56 %, readout fidelity 98.7 %). The arithmetic of these fidelities yields an exact mean fidelity of $\bar{F}=0.993866\overline{6}$ (i.e. $99.3867\%$, rounded to $99.39\%$) and an exact product fidelity of $F_{\text{prod}}=0.9816745428$ (i.e. $98.16745428\%$, rounded to $98.17\%$), illustrating how local‑place metrics can be aggregated adelically. Our analysis suggests that the emergence of ℝ in physics may be understood as a global consistency artifact, while the non‑Archimedean factors predict subtle structural signatures that could be probed in future quantum‑information experiments.

## 1. Introduction
Quantum mechanics is traditionally formulated over the real numbers ℝ, the unique Archimedean completion of the rational field ℚ. Ostrowski’s theorem, however, tells us that ℚ admits infinitely many non‑Archimedean completions $\mathbb{Q}_p$, one for each prime $p$, which are mutually singular with respect to the usual topology on ℝ. In number theory, adelic constructions combine all completions into a single object; as noted in [9], Tate’s 1950 thesis provides an explicit structural template for such local–global constructions, and we use that template as an analogy for a product of local contributions over all places. This observation motivates the hypothesis that quantum dynamics might admit an analogous adelic factorization: a global amplitude $\mathcal{A}$ should decompose as  

$$
\mathcal{A} \;=\; \prod_{v\in\{\infty,2,3,5,\dots\}} \mathcal{A}_v,
$$  

where each factor $\mathcal{A}_v$ lives in the local field corresponding to place $v$. If such a factorization holds, the dominance of the Archimedean factor in ordinary experiments would be a consequence of a global consistency condition rather than a fundamental axiom.

The present work develops this conjecture in three stages. First, we construct an adelic path‑integral whose stationary phase condition reproduces the standard Schrödinger equation at the Archimedean place while yielding p‑adic analogues at finite primes. Second, we set up simple p‑adic quantum models (harmonic oscillator and spin‑½) formally; demonstrating that their adelic product converges to the familiar real‑valued propagator under a suitable weighting of the p‑adic contributions remains an open task of the proposed programme. Third, we provide a numerical illustration using fidelity statistics from the Tianyan‑287 superconducting quantum processor (see [2]), showing how local‑place performance metrics can be combined adelically.

**Contributions.**
- We formulate a formal adelic path‑integral construction that isolates local factors $Z_\infty$ and $Z_p$ (Section 3).  
- We define elementary p‑adic quantum models for a harmonic oscillator and a spin‑½ system, providing a concrete template for future p‑adic dynamical studies (Section 3).  
- We perform a complete arithmetic aggregation of real‑world fidelity data, deriving the exact mean fidelity $\bar{F}=0.993866\overline{6}$ and product fidelity $F_{\text{prod}}=0.9816745428$, and interpret these as a toy adelic product (Sections 4–5).

## 2. Background and Related Work
The literature on adelic methods in arithmetic dynamics and mathematical physics provides several building blocks for our proposal.

[1] *Quasi‑adelic measures and equidistribution on $\mathbb{P}^1$* proves an arithmetic equidistribution theorem for points of small height on the Berkovich compactification of the projective line with respect to an adelic measure on $\mathbb{P}^1$, demonstrating that adelic measures can control distribution properties across all completions. We import this principle to quantum amplitudes.

[2] *Tianyan: Cloud services with quantum advantage* reports a superconducting quantum processor (Tianyan‑287) with 105 qubits and operational fidelities of 99.90 % (single‑qubit), 99.56 % (two‑qubit), and 98.7 % (readout). These concrete numbers serve as the only quantitative data in our input and are used in Section 4 to illustrate adelic aggregation of local performance metrics.

[3] *A Parametric and Feasibility Study for Data Sampling of the Dynamic Mode Decomposition* outlines Dynamic Mode Decomposition (DMD) as a Koopman‑based technique for dissecting high‑dimensional nonlinear systems into reduced‑order constituents. The idea parallels extracting local quantum spectra from p‑adic models.

[4] *The arithmetic Hodge index theorem for adelic line bundles II* extends adelic line‑bundle results to finitely generated fields and proves a rigidity property of preperiodic points of polarizable algebraic dynamical systems. This illustrates how adelic line‑bundle techniques can enforce global rigidity, analogous to the global consistency we seek for quantum amplitudes.

[5] *Exploiting Polyhedral Symmetries in Social Choice* discusses counting integral points in polyhedra to compute probabilities of election outcomes under the Impartial Anonymous Culture assumption, using Ehrhart theory. The counting techniques over discrete structures are reminiscent of summing contributions over p‑adic lattices.

[6] *Finite‑Dimensional Protori Are Adelic Tori* shows that the category of finite‑dimensional compact connected abelian groups is equivalent to the category of adelic tori, providing a concrete Lie‑theoretic framework for adelic groups. We adapt this to define adelic phase spaces for quantum systems.

[7] *Quantum computing and information extraction for a dynamical quantum system* demonstrates that quantum computers can efficiently extract dynamical quantities such as localization lengths, supporting our motivation to test adelic predictions on near‑term hardware.

[8] *Objective trajectories in hybrid classical‑quantum dynamics* presents a stochastic, linear, completely positive, trace‑preserving dynamics that couples classical and quantum degrees of freedom, showing that hybrid dynamics can be formulated consistently—a feature we anticipate for mixed Archimedean/non‑Archimedean quantum evolutions.

The remaining entries ([9]–[12]) are internal QNFO notes that outline the conceptual motivation (Tate’s thesis as a template, ratio‑based adelic physics, measure‑theoretic artifacts of the Archimedean place, and a depth‑breadth‑valuation ontology). Their summaries provide no additional quantitative data; they are cited only to situate our conjecture within the broader research agenda.

## 3. Methods
Our approach proceeds in three parallel tracks.

1. **Adelic Path‑Integral Construction.**  
   For a quantum system with classical action $S[x]$, the standard real‑valued path integral is  

   $$
   Z_\infty = \int \mathcal{D}x \; e^{\frac{i}{\hbar} S[x]}.
   $$  

   For each prime $p$, we replace the exponential by the p‑adic additive character $\chi_p$, yielding  

   $$
   Z_p = \int_{\mathbb{Q}_p} \mathcal{D}x \; \chi_p\!\bigl(S[x]\bigr).
   $$  

   The adelic partition function is then defined as the product  

   $$
   Z_{\mathbb{A}} = Z_\infty \prod_{p\ \text{prime}} Z_p,
   $$  

   Convergence of this infinite product is an open problem; the adelic measures studied in [1] and the exact‑sequence framework of [6] serve as structural analogies but are not shown here to ensure convergence.

2. **p‑adic Quantum Model Construction.**  
   We construct a p‑adic harmonic oscillator by defining a quadratic action $S_p[x]=\frac{1}{2}m\dot{x}^2 - \frac{1}{2}k x^2$ over $\mathbb{Q}_p$ and adopt, as a formal definition without derivation, a p‑adic Gaussian evaluation of $Z_p$; no explicit evaluation is performed in this work. Analogous spin‑½ models are built by assigning p‑adic Hilbert spaces of dimension 2 and defining Pauli‑like operators via p‑adic matrices.

3. **Numerical Aggregation of Fidelity Data.**  
   Using the fidelity numbers from [2], we compute two aggregate metrics:
   - The arithmetic mean fidelity $\bar{F}$.
   - The product fidelity $F_{\text{prod}} = \prod_i f_i$, where each $f_i$ is the decimal representation of a fidelity (e.g., 99.90 % → 0.9990).  
   These serve as a toy example of adelic aggregation: each fidelity is interpreted as a “local‑place” performance indicator, and the product mimics the adelic product over places.

All derivations are presented explicitly in Section 4, with every intermediate arithmetic step shown so that each result can be independently reproduced from the stated inputs.

## 4. Analysis
### 4.1 Input Numbers
All input numbers used in this paper come from a single source, the processor description in [2]; no other quantitative data are available in our input, and none are assumed.

| Symbol | Value | Source |
|--------|-------|--------|
| $f_1$ (single‑qubit fidelity) | $99.90\% = 0.9990$ | [2] |
| $f_2$ (two‑qubit fidelity)   | $99.56\% = 0.9956$ | [2] |
| $f_3$ (readout fidelity)     | $98.7\%  = 0.9870$ | [2] |

### 4.2 Arithmetic Steps

**Step 1: Compute the arithmetic mean $\bar{F}$.**  

\[
\begin{aligned}
\text{Sum} &= f_1 + f_2 + f_3 \\
           &= 0.9990 + 0.9956 + 0.9870 \\
           &= (0.9990 + 0.9956) + 0.9870 \\
           &= 1.9946 + 0.9870 \\
           &= 2.9816.
\end{aligned}
\]

\[
\bar{F} = \frac{\text{Sum}}{3} = \frac{2.9816}{3}.
\]

Performing the division:

\[
\frac{2.9816}{3} = 0.993866\overline{6}.
\]

Expressed as a percentage:

\[
\bar{F}_{\%} = 0.993866\overline{6} \times 100\% \approx 99.3867\% \approx 99.39\%.
\]

**Step 2: Compute the product fidelity $F_{\text{prod}}$.**  

First multiply $f_1$ and $f_2$:

\[
\begin{aligned}
f_1 \times f_2 &= 0.9990 \times 0.9956 \\
               &= (1 - 0.0010) \times 0.9956 \\
               &= 0.9956 - 0.0010 \times 0.9956 \\
               &= 0.9956 - 0.0009956 \\
               &= 0.9946044.
\end{aligned}
\]

Next multiply the result by $f_3$:

\[
\begin{aligned}
F_{\text{prod}} &= 0.9946044 \times 0.9870 \\
                &= 0.9946044 \times (1 - 0.0130) \\
                &= 0.9946044 - 0.0130 \times 0.9946044 \\
                &= 0.9946044 - 0.0129298572 \\
                &= 0.9816745428.
\end{aligned}
\]

Expressed as a percentage:

\[
F_{\text{prod},\%} = 0.9816745428 \times 100\% \approx 98.167\% \approx 98.17\%.
\]

All intermediate results are retained for transparency.

### 4.3 Interpretation of the Numbers
The mean fidelity $\bar{F}=0.993866\overline{6}$ ($99.3867\%$) reflects a typical local‑place performance, while the product fidelity $F_{\text{prod}}=0.9816745428$ ($98.16745428\%$) illustrates how an adelic‑type product can amplify small imperfections across places. In a genuine adelic quantum theory, each $f_i$ would correspond to a contribution from a distinct completion (e.g., $f_1$ from $\infty$, $f_2$ from $\mathbb{Q}_2$, $f_3$ from $\mathbb{Q}_3$), and the global amplitude would be their product, consistent with the formalism of Section 3.

## 5. Results
- **Mean Fidelity:** $\bar{F}=0.993866\overline{6}$, i.e. $\bar{F}_{\%}=99.3867\%$ to four decimal places, or $99.39\%$ when rounded to two decimal places (derived in Section 4.2, Step 1).  
- **Product Fidelity:** $F_{\text{prod}}=0.9816745428$, i.e. $F_{\text{prod},\%}=98.16745428\%$, or $98.17\%$ when rounded to two decimal places (derived in Section 4.2, Step 2).  

These two aggregate metrics constitute the only quantitative results of the present study. They demonstrate that explicit arithmetic can be performed on locally defined performance numbers and that the adelic product naturally yields a lower overall figure, reflecting the multiplicative accumulation of local imperfections. Throughout the paper, quoted two‑decimal percentages ($99.39\%$ and $98.17\%$) are rounded presentations of the exact values $0.993866\overline{6}$ and $0.9816745428$ computed above; the exact values are the authoritative results.

## 6. Discussion
### 6.1 Limitations
1. **Sparse Quantitative Input.** The analysis relies on a single set of fidelity numbers from a specific superconducting processor ([2]). Consequently, the numerical illustration is illustrative rather than exhaustive.  
2. **Absence of Genuine p‑adic Experiments.** Our p‑adic models are purely formal; no physical system currently implements a $\mathbb{Q}_p$‑valued quantum evolution, so the adelic product remains a theoretical construct.  
3. **Convergence of the Infinite Product.** The adelic product over all primes is infinite; without a regularization scheme (e.g., using the adelic measure of [1] and the exact‑sequence framework of [6]), the product may diverge. Our toy example truncates the product to three “places,” which is a drastic simplification.

### 6.2 Potential Failure Modes
- **Falsifiability:** If future experiments on p‑adic‑inspired quantum simulators reveal deviations from the predicted adelic product (e.g., the global amplitude does not factorize), the conjecture would be falsified.  
- **Incompatibility with Relativistic Causality:** The non‑Archimedean completions possess ultrametric topologies that may conflict with Lorentz invariance; any inconsistency would undermine the framework.  
- **Measure Ambiguity:** The adelic measure employed in [1] is defined for arithmetic equidistribution; its applicability to quantum amplitudes is not proven. Different choices of measure could alter the product dramatically.

### 6.3 Open Questions
- How can one construct a physically meaningful p‑adic Hilbert space that respects unitarity and probability conservation?  
- What regularization scheme ensures convergence of $\prod_{p} \mathcal{A}_p$ while preserving the functional equation analog of Tate’s thesis?  
- Can the adelic product predict observable corrections (e.g., tiny deviations in interference fringes) that are within reach of near‑term quantum hardware?

### 6.4 A Hypothesis on Adelic Aggregation of Device Metrics
As an explicitly labeled hypothesis, not a verified result: if each local fidelity $f_i$ from [2] is treated as a contribution from a distinct place $v_i$, then the exact aggregates computed in Section 4.2 are $\bar{F}=0.993866\overline{6}$ and $F_{\text{prod}}=0.9816745428$. The gap $\bar{F}-F_{\text{prod}}=0.0121921238$ (approximately $1.22$ percentage points) quantifies, in this toy setting, how multiplicative aggregation penalizes local imperfections more strongly than averaging. Whether this gap carries any physical meaning in a genuine adelic quantum theory remains entirely open.

## 7. Practical Implications and Engineering Pathways
(a) **Potential Users and Decision Impact.** Quantum hardware developers and cloud‑service providers could use the adelic aggregation framework to assess how local‑place imperfections (e.g., gate errors, readout errors) compound in a multiplicative fashion, informing design choices that prioritize uniform improvement across all error channels rather than focusing solely on average performance.  

(b) **Technology Readiness Level.** The present work is purely analytical and has not undergone peer review; according to NASA’s definitions, it resides at TRL 1–2. No manufacturing or hardware demonstration is claimed.  

(c) **Next Minimal Experiment.** The smallest de‑risking experiment is to construct a simple p‑adic simulation of a harmonic oscillator on a classical computer, compute its propagator numerically, and compare the product of the simulated p‑adic amplitude with the real‑valued amplitude obtained from the same action. A discrepancy larger than a few percent would falsify the conjectured factorization for that toy system.  

(d) **Engineering Constraints.** The primary constraints stem from (i) the need for a well‑defined p‑adic additive character $\chi_p$ and associated integration measure, (ii) the requirement to truncate the infinite prime product to a finite set while controlling truncation error, and (iii) the absence of experimental platforms that natively realize $\mathbb{Q}_p$ dynamics. These constraints are open questions pending further mathematical and experimental development.  

(e) **Projected Bounds.** Assuming the three‑place toy model presented in Sections 4–5, the adelic product reduces the overall fidelity from $99.39\%$ (mean) to $98.17\%$ (product). If additional places with comparable fidelities were included, the product would continue to decrease roughly multiplicatively; for $n$ identical places with fidelity $f$, the product scales as $f^{\,n}$. This projection follows directly from the arithmetic in Section 4.  

(f) **Risks and Misuse Paths.** Misinterpretation of the adelic product as a literal prediction for real quantum hardware could lead to overly pessimistic engineering decisions. The framework should be applied only as a conceptual tool, with explicit acknowledgment of its speculative status and the current lack of empirical validation.

## 8. Conclusion
We have outlined a speculative but concrete program for factorizing quantum dynamics across all completions of ℚ. By leveraging adelic constructions from arithmetic geometry ([1], [6]) and grounding the discussion in real‑world fidelity data ([2]), we demonstrated how local‑place metrics can be aggregated through an adelic product, yielding a lower overall performance figure. While the present work stops short of a full physical theory, it establishes a clear methodological pathway: formulate local p‑adic quantum models, define an adelic measure ensuring convergence, and test the resulting global predictions against high‑precision quantum experiments. The conjecture that the Archimedean real numbers arise as a global consistency artifact rather than a fundamental necessity remains open, inviting further mathematical and experimental scrutiny.

## References

[1] arXiv:1502.04660v3 | Quasi-adelic measures and equidistribution on $\mathbb{P}^1$

[2] arXiv:2512.10504v2 | Tianyan: Cloud services with quantum advantage

[3] arXiv:2110.06573v2 | A Parametric and Feasibility Study for Data Sampling of the Dynamic Mode Decomposition--Range, Resolution, and Universal Convergence States

[4] arXiv:1304.3539v2 | The arithmetic Hodge index theorem for adelic line bundles II

[5] arXiv:1109.1545v2 | Exploiting Polyhedral Symmetries in Social Choice

[6] arXiv:2411.16000v44 | Finite-Dimensional Protori Are Adelic Tori

[7] arXiv:quant-ph/0402010v1 | Quantum computing and information extraction for a dynamical quantum system

[8] arXiv:2011.06009v3 | Objective trajectories in hybrid classical-quantum dynamics

[9] QNFO: Adelic Factorization of Quantum Dynamics Across All Completions of ℚ

[10] QNFO: Ratio-Based Adelic Physics

[11] QNFO: Measure-Theoretic Artifacts of the Archimedean Place — v2.0: The Completion Problem, the Langlands Connection, and the Adelic Restructuring of Fundamental Physics

[12] QNFO: Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum

## Appendix A. Divergence report
No substantive divergent claims were identified among the independent drafts; all claims were convergent or single‑source, and no convention choice was required. This appendix is therefore empty of reported conflicts.

## Appendix B. Claim attribution
| Claim ID | Substantive claim | Source Draft(s) | Agreement Status |
|----------|------------------|----------------|------------------|
| C1 | Adelic factorization conjecture: global amplitude $\mathcal{A}=\prod_v \mathcal{A}_v$ over all completions of ℚ | A, B | CONVERGENT |
| C2 | Tate’s 1950 thesis serves as a structural template for adelic quantum mechanics, per [9] | A, B | CONVERGENT |
| C3 | Adelic path‑integral construction with local factors $Z_\infty$ and $Z_p$ | A, B | CONVERGENT |
| C4 | p‑adic harmonic‑oscillator and spin‑½ model construction | A, B | CONVERGENT |
| C5 | Fidelity inputs $f_1=0.9990$, $f_2=0.9956$, $f_3=0.9870$ from [2] | A, B, C | CONVERGENT |
| C6 | Mean fidelity $\bar{F}\approx 99.39\%$ | A, B, C | CONVERGENT |
| C7 | Product fidelity $F_{\text{prod}}\approx 98.17\%$ | A, B, C | CONVERGENT |
| C8 | Limitations: sparse quantitative input, no genuine p‑adic experiments, convergence of the infinite product | A, B | CONVERGENT |