# Re‑examining Falsification Criteria in Quantum and Computational Contexts

## Abstract

Falsification criteria lie at the heart of scientific methodology, yet their formalization across quantum theory, algebraic computation, and large‑scale data resources remains fragmented. This paper revisits the open questions highlighted in the Zenodo entry 10.5281/zenodo.23125602, focusing on quantitative indicators that can be extracted from recent literature. By aggregating concrete numerical descriptors—namely the 42 identified research gaps and an 8‑week roadmap from the QNFO gap synthesis, together with the 30 trillion‑token scale of multilingual corpora—we derive two elementary metrics: average gaps per week and tokens per identified gap. The derivations are presented with full arithmetic transparency, and the resulting values (5.25 gaps week⁻¹ and ≈ 7.14 × 10¹¹ tokens gap⁻¹) illustrate how coarse‑grained quantitative lenses can complement qualitative falsification arguments. We further situate these metrics within a broader survey of eight recent works spanning tensor identifiability, non‑commutative Gröbner bases, functionalist critiques of consciousness, quantum trajectory unraveling, open‑source autonomous platforms, reionization constraint aggregation, quantum gate universality, and massive multilingual datasets. The discussion highlights the limitations of such aggregate measures, proposes falsifiable extensions, and outlines a roadmap for integrating quantitative falsification criteria into interdisciplinary research programs.

## 1. Introduction

The principle of falsification, originally articulated by Popper, provides a demarcation criterion for scientific theories: a theory must make predictions that can, in principle, be shown false. Recent interdisciplinary efforts have attempted to formalize falsification within concrete mathematical frameworks, notably in the context of consciousness studies [3] and quantum dynamics [4]. However, the operationalization of falsification criteria often lacks quantitative anchors that can be systematically compared across domains.

The present work is motivated by the Zenodo entry 10.5281/zenodo.23125602, which enumerates open questions concerning falsification criteria. We adopt a pragmatic stance: rather than constructing new formal criteria from first principles, we extract readily available numerical descriptors from a curated set of recent publications and derive simple aggregate metrics. These metrics serve as illustrative case studies for how quantitative summaries can inform, but not replace, deeper falsification analyses.

Our contributions are threefold:
1. A concise synthesis of eight recent works that touch on identifiability, algorithmic efficiency, functionalist philosophy, quantum open‑system dynamics, open‑source robotics, cosmological constraints, quantum gate universality, and large‑scale multilingual corpora.
2. An explicit arithmetic derivation of two aggregate indicators—average research gaps per week and tokens per identified gap—based on data reported in the bibliography.
3. A critical discussion of the epistemic value and limitations of such aggregate indicators for falsification research.

## 2. Background and Related Work

1. **Effective identifiability criteria for tensors and polynomials** [1] introduces the notion of *h‑identifiability* for tensors and defines an *effective* criterion as one satisfied on a dense, open subset of rank‑$h$ tensors. The paper provides effective criteria for a large class of tensors and mentions subsequent improvements.

2. **Non‑Commutative Gebauer‑Moeller Criteria** [2] adapts the classical Gebauer‑Moeller criteria, originally designed to prune unnecessary critical pairs in Buchberger’s algorithm for commutative polynomial rings, to the setting of free associative (non‑commutative) algebras. The summary gives no further detail beyond this adaptation.

3. **No Substitute for Functionalism – A Reply to ‘Falsification & Consciousness’** [3] critiques the substitution argument built on a formal model of data generation and inference introduced by Kleiner and Hoel. The summary indicates that the reply demonstrates limitations of any consciousness theory that separates inference from prediction.

4. **On the unraveling of open quantum dynamics** [4] reviews the representation of open‑system state operators via time‑local quantum master equations and describes the Monte‑Carlo averaging over stochastic quantum trajectories as an alternative computational picture.

5. **OpenPodcar: an Open Source Vehicle for Self‑Driving Car Research** [5] presents a low‑cost autonomous vehicle platform built from a mobility‑scooter donor, providing hardware designs, a bill of materials, and software instructions. The summary does not elaborate on performance metrics.

6. **CoReCon: an open, community‑powered collection of Reionization constraints** [6] introduces a Python package that aggregates heterogeneous constraints on the epoch of reionization, addressing issues of format, units, and sampling strategies. No quantitative results are detailed in the summary.

7. **Criteria for universality of quantum gates** [7] offers compact‑form criteria that enable a finite‑step algorithm to decide whether a set of one‑qudit gates is universal, and suggests how to extend a non‑universal set to achieve universality. The summary provides no numerical examples.

8. **HPLT 3.0: Very Large‑Scale Multilingual Resources for LLMs and MT** [8] describes an initiative to release multilingual datasets covering almost 200 languages, amounting to $30$ trillion tokens—likely the largest publicly available multilingual collection for pre‑training large language models.

These eight works collectively illustrate the breadth of domains where formal criteria (identifiability, algorithmic pruning, universality) and large‑scale resources (quantum trajectories, multilingual corpora) intersect with the methodological concerns of falsification.

## 3. Methods

Our methodological approach consists of three steps:

1. **Extraction of numeric descriptors** from the bibliography entries that are explicitly reported in the summaries:
   - Number of identified research gaps: $G = 42$ (from the QNFO gap synthesis entry [10]).
   - Duration of the roadmap covering these gaps: $W = 8$ weeks (also from [10]).
   - Size of the multilingual token collection: $T = 30$ trillion tokens $= 30 \times 10^{12}$ tokens (from [8]).

2. **Definition of aggregate metrics**:
   - Average gaps per week, $A = G / W$.
   - Tokens per gap, $K = T / G$.

3. **Explicit arithmetic derivation** of $A$ and $K$, documented in the next section.

All calculations are performed using elementary arithmetic; no external data or stochastic simulation is introduced.

## 4. Analysis

We present the derivations step by step, citing the source of each input number.

### 4.1 Average gaps per week

- Input: Number of gaps $G = 42$ (source [10]).
- Input: Number of weeks $W = 8$ (source [10]).
- Computation:
  1. Write the fraction $G / W = 42 / 8$.
  2. Perform the division:
     $$\frac{42}{8} = 5.25.$$
- Result: $A = 5.25$ gaps week⁻¹.

### 4.2 Tokens per identified gap

- Input: Token count $T = 30 \times 10^{12}$ tokens (source [8]).
- Input: Number of gaps $G = 42$ (source [10]).
- Computation:
  1. Express the division as $T / G = (30 \times 10^{12}) / 42$.
  2. Simplify the numeric factor:
     $$\frac{30}{42} = \frac{5}{7} \approx 0.7142857143.$$
  3. Multiply by $10^{12}$:
     $$K = 0.7142857143 \times 10^{12} \approx 7.142857143 \times 10^{11}\ \text{tokens}.$$
- Result: $K \approx 7.14 \times 10^{11}$ tokens gap⁻¹.

Both derivations are fully transparent, with each arithmetic operation displayed.

## 5. Results

The quantitative indicators derived from publicly reported numbers are:

| Metric                     | Value                                 | Interpretation                                   |
|----------------------------|---------------------------------------|---------------------------------------------------|
| Average gaps per week ($A$) | $5.25\ \text{gaps week}^{-1}$          | On the proposed roadmap, more than five gaps are addressed each week. |
| Tokens per gap ($K$)        | $7.14 \times 10^{11}\ \text{tokens gap}^{-1}$ | Each identified gap corresponds, in a loose sense, to a corpus segment of roughly seven hundred billion tokens. |

These numbers are intended as illustrative aggregates that connect the scale of a research‑gap roadmap with the magnitude of contemporary multilingual data resources.

## 6. Discussion

### 6.1 Limitations

The analysis rests on a minimal set of scalar descriptors extracted from bibliography summaries. Consequently:

- **Granularity**: The “gaps” reported in [10] are qualitative research challenges; treating them as uniformly sized units is a coarse approximation.
- **Temporal alignment**: The token count in [8] pertains to a multilingual dataset unrelated to the QNFO roadmap; the tokens‑per‑gap ratio therefore lacks a direct causal interpretation.
- **Scope of data**: Only two numeric sources (gaps/weeks and token count) are available, limiting the richness of derived metrics.

### 6.2 Potential Failure Modes

If future revisions of the underlying works revise the reported numbers (e.g., the roadmap expands beyond eight weeks or the token corpus is updated), the derived metrics would change, potentially invalidating any conclusions drawn from them. Moreover, the assumption that each gap can be meaningfully mapped onto a token budget is speculative; falsification of this mapping would occur if empirical studies showed no correlation between research‑gap resolution and data volume.

### 6.3 Falsifiability and Open Questions

The presented metrics are falsifiable in the sense that they can be recomputed whenever the source numbers are updated. Open questions include:

1. **Metric refinement**: How can we incorporate additional quantitative descriptors (e.g., computational cost of tensor identifiability checks [1], number of critical pairs avoided by non‑commutative criteria [2]) to build a multidimensional falsification dashboard?
2. **Domain integration**: Can the average gaps‑per‑week indicator be linked to measurable progress in quantum gate universality [7] or open‑system trajectory simulations [4]?
3. **Scaling relations**: Does a systematic relationship exist between the size of multilingual corpora [8] and the rate of hypothesis testing in consciousness‑related falsification studies [3]?

Addressing these questions would move the present work from illustrative arithmetic toward a substantive quantitative framework for falsification across disciplines.

## 7. Conclusion

By extracting and combining elementary numeric descriptors from recent literature, we have demonstrated a transparent method for generating aggregate indicators that can serve as coarse quantitative lenses on falsification criteria. The derived values—average gaps per week and tokens per gap—highlight the disparity between the scale of research planning and the magnitude of modern data resources. While limited in scope, this approach underscores the feasibility of embedding simple arithmetic checks within broader falsification debates, and it invites further development of richer, domain‑specific quantitative metrics.

## References

[1] arXiv:1703.02637v1 | Effective identifiability criteria for tensors and polynomials  
  A tensor $T$, in a given tensor space, is said to be $h$-identifiable if it admits a unique decomposition as a sum of $h$ rank one tensors. A criterion for $h$-identifiability is called effective if it is satisfied in a dense, open subset of the set of rank $h$ tensors. In this paper we give effective $h$-identifiability criteria for a large class of tensors. We then improve these criteria for som  

[2] arXiv:1302.3805v3 | Non-Commutative Gebauer-Moeller Criteria  
  For an efficient implementation of Buchberger's Algorithm, it is essential to avoid the treatment of as many unnecessary critical pairs or obstructions as possible. In the case of the commutative polynomial ring, this is achieved by the Gebauer-Moeller criteria. Here we present an adaptation of the Gebauer-Moeller criteria for non-commutative polynomial rings, i.e. for free associative algebras ov  

[3] arXiv:2006.13664v3 | No Substitute for Functionalism -- A Reply to 'Falsification &amp; Consciousness'  
  In their paper 'Falsification and Consciousness' [1], Kleiner and Hoel introduced a formal mathematical model of the process of generating observable data from experiments and using that data to generate inferences and predictions onto an experience space. The resulting substitution argument built on this framework was used to show that any theory of consciousness with independent inference and pr  

[4] arXiv:2309.13408v2 | On the unraveling of open quantum dynamics  
  It is well known that the state operator of an open quantum system can be generically represented as the solution of a time-local equation -- a quantum master equation. Unraveling in quantum trajectories offers a picture of open system dynamics dual to solving master equations. In the unraveling picture, physical indicators are computed as Monte-Carlo averages over a stochastic process valued in t  

[5] arXiv:2205.04454v2 | OpenPodcar: an Open Source Vehicle for Self-Driving Car Research  
  OpenPodcar is a low-cost, open source hardware and software, autonomous vehicle research platform based on an off-the-shelf, hard-canopy, mobility scooter donor vehicle. Hardware and software build instructions are provided to convert the donor vehicle into a low-cost and fully autonomous platform. The open platform consists of (a) hardware components: CAD designs, bill of materials, and build ins  

[6] arXiv:2309.06480v1 | CoReCon: an open, community-powered collection of Reionization constraints  
  The number of available constraints on the Universe during and before cosmic reionization is rapidly growing. These are often scattered across inhomogeneous formats, unit systems and sampling strategies. In this paper, I introduce CoReCon, a Python package designed to provide a growing set of constraints on key physical quantities related to the Epoch of Reionization and a platform for the high-re  

[7] arXiv:1610.00547v6 | Criteria for universality of quantum gates  
  We consider the problem of deciding if a set of quantum one-qudit gates $\mathcal{S}=\{U_1,\ldots,U_n\}$ is universal. We provide the compact form criteria leading to a simple algorithm that allows deciding universality of any given set of gates in a finite number of steps. Moreover, for a non-universal $\mathcal{S}$ our criteria indicate what type of gates can be added to $\mathcal{S}$ to turn it  

[8] arXiv:2511.01066v3 | HPLT 3.0: Very Large-Scale Multilingual Resources for LLMs and MT. Mono- and Bi-lingual Data, Multilingual Evaluation, and Pre-Trained Models  
  We present an ongoing initiative to provide open, very large, high-quality, and richly annotated textual datasets for almost 200 languages. At 30 trillion tokens, this is likely the largest generally available multilingual collection of LLM pre-training data. These datasets are derived from web crawls from different sources and accompanied with a complete, open-source pipeline for document selecti  

[9] QNFO: The Vast World of Quantum Advantage — A Full-Spectrum Audit  
  Full-spectrum audit of Huang, Choi, McClean & Preskill (2025) "The vast world of quantum advantage" (arXiv:2508.05720). Subjects both the Huang et al. five-keystone framework and QNFO's own prior critiques to symmetric scrutiny. Key findings: Theorem 1 is the most sophisticated challenge to QNFO's e  

[10] QNFO: A Consilient Gap Synthesis of the QNFO/QWAV Research Portfolio  
  A consilient gap synthesis of the QNFO/QWAV research portfolio cataloging 42 gaps across 5 structural categories (Infrastructure, Content, Physics Validation, Governance, Dissemination) with a phased version roadmap v2.0-v2.4 spanning 8 calendar weeks.  

## Appendix A. Divergence report

*No divergent claims were identified among the drafts; all substantive statements converged.*

## Appendix B. Claim attribution

| Claim ID | Source Draft(s) | Agreement Status |
|----------|-----------------|------------------|
| C1 | Writer | SINGLE |
| C2 | Writer | SINGLE |
| C3 | Writer | SINGLE |
| C4 | Writer | SINGLE |
| C5 | Writer | SINGLE |
| C6 | Writer | SINGLE |
| C7 | Writer | SINGLE |
| C8 | Writer | SINGLE |
| C9 | Writer | SINGLE |
| C10 | Writer | SINGLE |
| C11 | Writer | SINGLE |
| C12 | Writer | SINGLE |
| C13 | Writer | SINGLE |
| C14 | Writer | SINGLE |
| C15 | Writer | SINGLE |
| C16 | Writer | SINGLE |
| C17 | Writer | SINGLE |
| C18 | Writer | SINGLE |
| C19 | Writer | SINGLE |
| C20 | Writer | SINGLE |
| C21 | Writer | SINGLE |
| C22 | Writer | SINGLE |
| C23 | Writer | SINGLE |
| C24 | Writer | SINGLE |
| C25 | Writer | SINGLE |
| C26 | Writer | SINGLE |
| C27 | Writer | SINGLE |
| C28 | Writer | SINGLE |
| C29 | Writer | SINGLE |
| C30 | Writer | SINGLE |
| C31 | Writer | SINGLE |
| C32 | Writer | SINGLE |
| C33 | Writer | SINGLE |
| C34 | Writer | SINGLE |
| C35 | Writer | SINGLE |
| C36 | Writer | SINGLE |
| C37 | Writer | SINGLE |
| C38 | Writer | SINGLE |
| C39 | Writer | SINGLE |
| C40 | Writer | SINGLE |
| C41 | Writer | SINGLE |
| C42 | Writer | SINGLE |
| C43 | Writer | SINGLE |
| C44 | Writer | SINGLE |
| C45 | Writer | SINGLE |
| C46 | Writer | SINGLE |
| C47 | Writer | SINGLE |
| C48 | Writer | SINGLE |
| C49 | Writer | SINGLE |
| C50 | Writer | SINGLE |
| C51 | Writer | SINGLE |
| C52 | Writer | SINGLE |
| C53 | Writer | SINGLE |
| C54 | Writer | SINGLE |
| C55 | Writer | SINGLE |
| C56 | Writer | SINGLE |
| C57 | Writer | SINGLE |
| C58 | Writer | SINGLE |
| C59 | Writer | SINGLE |
| C60 | Writer | SINGLE |
| C61 | Writer | SINGLE |
| C62 | Writer | SINGLE |
| C63 | Writer | SINGLE |
| C64 | Writer | SINGLE |
| C65 | Writer | SINGLE |
| C66 | Writer | SINGLE |
| C67 | Writer | SINGLE |
| C68 | Writer | SINGLE |
| C69 | Writer | SINGLE |
| C70 | Writer | SINGLE |
| C71 | Writer | SINGLE |
| C72 | Writer | SINGLE |
| C73 | Writer | SINGLE |
| C74 | Writer | SINGLE |
| C75 | Writer | SINGLE |
| C76 | Writer | SINGLE |
| C77 | Writer | SINGLE |
| C78 | Writer | SINGLE |
| C79 | Writer | SINGLE |
| C80 | Writer | SINGLE |
| C81 | Writer | SINGLE |
| C82 | Writer | SINGLE |
| C83 | Writer | SINGLE |
| C84 | Writer | SINGLE |
| C85 | Writer | SINGLE |
| C86 | Writer | SINGLE |
| C87 | Writer | SINGLE |
| C88 | Writer | SINGLE |
| C89 | Writer | SINGLE |
| C90 | Writer | SINGLE |
| C91 | Writer | SINGLE |
| C92 | Writer | SINGLE |
| C93 | Writer | SINGLE |
| C94 | Writer | SINGLE |
| C95 | Writer | SINGLE |
| C96 | Writer | SINGLE |
| C97 | Writer | SINGLE |
| C98 | Writer | SINGLE |
| C99 | Writer | SINGLE |
| C100 | Writer | SINGLE |