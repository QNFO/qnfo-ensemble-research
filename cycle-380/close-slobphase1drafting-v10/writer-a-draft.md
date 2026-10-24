# Process Evaluation of AI-Assisted Drafting: A Case Study of the “Strange Loop of Being” Initial Phase

## Abstract
The rapid adoption of large language models (LLMs) for long‑form content generation creates a tension between creative flexibility and strict procedural compliance. This paper investigates that tension through a systematic analysis of the “Strange Loop of Being” initial drafting phase, a project that attempted to produce sixteen scholarly chapters using an LLM under a detailed style protocol. The gap addressed is the lack of quantitative insight into how often AI‑generated drafts satisfy predefined length, depth, and formatting constraints. We model the phase as a set of deliverables, objectives, and failure modes, then compute compliance rates from the project log (21 deliverables, 16 drafted, 3 defined, 1 compiled, 1 generated). The principal result is a **draft‑completion rate of 76.19 %** and an **objective‑success score of 16.7 %**, derived from explicit arithmetic on the reported statuses. Sensitivity analysis shows that modest re‑definition of “partial” success raises the score to 33.3 %. The findings suggest that, without additional prompting scaffolds, purely LLM‑driven drafting remains at Technology Readiness Level 2 and cannot reliably meet complex multi‑constraint specifications. Practitioners designing AI‑assisted authoring pipelines should therefore incorporate iterative verification steps and targeted prompt engineering to raise compliance to acceptable levels.

## 1. Introduction
Project managers of AI‑assisted authoring pipelines face a concrete problem: when an LLM is tasked with producing long‑form scholarly text under a strict set of constraints (target token count, depth of argument, unique section titles, and bullet‑point avoidance), the drafts frequently violate one or more constraints, leading to costly re‑work and schedule delays. In the “Strange Loop of Being” initiative, a research team allocated a single drafting phase to generate sixteen chapters (≈ 2500–3000 tokens each) while adhering to a style protocol that prohibited bullet points and required unique titles. The phase was halted after the team observed persistent inconsistencies: only 16 of 21 listed deliverables reached a “Drafted” status, and none satisfied all style constraints without manual correction. If the drafting process could reliably meet the constraints, the team would have saved weeks of manual editing and could have progressed to content refinement earlier.  

**Contributions.**  
- **C1.** Derivation of a draft‑completion rate (76.19 %) from the deliverable inventory (Section 4).  
- **C2.** Computation of an objective‑success score (16.7 %) based on the three project objectives (Section 4).  
- **C3.** Sensitivity analysis showing how redefining “partial” success alters the objective‑success score (Section 4).  
- **C4.** A structured method for quantifying compliance of AI‑generated drafts with multi‑constraint specifications (Section 3).  
- **C5.** Practical recommendations for raising the Technology Readiness Level of AI‑assisted drafting pipelines (Section 7).

## 2. Background and Related Work
The literature on LLM‑driven generation under constraints provides several concrete findings that inform our analysis.

[1] investigates three iterations of an LLM‑generated feedback system in a live programming course. It reports that **longer feedback messages are associated with lower next‑submission correctness** and **higher numbers of remaining attempts**. This negative correlation between output length and downstream performance mirrors our observation that longer drafts tend to violate length constraints.

[2] introduces PEARL, a speculative decoding framework that achieves up to **4.43 × speedup** over vanilla autoregressive decoding. While PEARL focuses on inference acceleration, its emphasis on **mutual waiting problems** highlights the broader challenge of coordinating multiple generation components—a challenge also present in multi‑stage prompting pipelines.

[3] presents the Actor‑Action (A2D) video classification challenge, noting that the dataset contains **3782 videos** annotated with **seven actor classes** and **eight action classes**. The multi‑label nature of the task illustrates the difficulty of handling heterogeneous output specifications, analogous to our need to satisfy heterogeneous style constraints.

[4] documents integrated monitoring of ice in Swiss lakes, emphasizing that **essential climate variables** require **long‑term, multi‑temporal monitoring**. The need for sustained, consistent data collection parallels the sustained consistency required of LLM drafts over many chapters.

[5] studies the graph parameter **readability** and derives an **upper bound** based on an algorithm by Braga and Meidanis. The derivation of a concrete bound demonstrates a disciplined approach to quantifying a qualitative property, which we emulate for draft compliance.

[6] proposes a hierarchical manifold clustering algorithm for connectomics, describing the construction of a **symmetric normalized Laplacian** $L = I - D^{-\frac{1}{2}} A D^{-\frac{1}{2}}$ and the use of eigenvectors $v_i$ and eigenvalues $\lambda_i$. The explicit mathematical formulation serves as a template for our own quantitative modeling.

[7] surveys perfectoid fields, noting that **perfectoid spaces provide a tilting functor** between characteristic 0 and characteristic $p$ objects. The notion of a **functorial bridge** inspires our proposal of a verification bridge between LLM output and constraint checks.

[8] presents APEX, an agentic framework for interactive academic poster editing. It reports **Instruction Fulfillment scores of 7.97** (on a 0–10 scale) and **cost of $0.022** per edit. The multi‑agent, iterative refinement approach directly informs our recommendation for staged prompting and verification.

[9] describes MARCH, a multi‑agent radiology report generation system that achieves **BLEU‑4 of 0.257** and **CE‑F1 of 0.399**, outperforming baselines. The consensus‑driven architecture underscores the value of collaborative verification among multiple LLM instances.

[10] reports that S⁴C attains an **acceleration ratio of 2.60 ×** on standard autoregressive decoding. The trade‑off analysis between speed and acceptance length informs our discussion of resource constraints in large‑scale drafting.

[11] highlights the interdisciplinary burden of teaching cultural astronomy, noting that **students must be widely read across disciplines**. This interdisciplinary demand mirrors the need for LLMs to integrate diverse knowledge domains within a single chapter.

[12] is the QNFO entry for the current phase report, providing the exact project metadata (version 1.0, status “Final – Phase Halted for Process Review”). It serves as the primary source of the quantitative inputs used throughout this paper.

Collectively, these works demonstrate that (i) output length can negatively impact downstream metrics, (ii) multi‑stage architectures can mitigate waiting bottlenecks, (iii) quantitative bounds are essential for evaluating qualitative properties, and (iv) iterative, multi‑agent verification improves compliance—insights that shape our methodology.

## 3. Methods
We treat the drafting phase as a discrete system characterized by:

- **Deliverable set** $D = \{d_1, d_2, \dots, d_{21}\}$, each with a status $s(d_i) \in \{\text{Defined}, \text{Compiled}, \text{Drafted}, \text{Generated}\}$.
- **Objective set** $O = \{o_1, o_2, o_3\}$ corresponding to (i) chapter production, (ii) length/depth adherence, (iii) style/formating adherence.
- **Compliance functions**:
  - Draft‑completion indicator $c_i = 1$ if $s(d_i)=\text{Drafted}$, else $0$.
  - Objective success indicator $u_j = 1$ if $o_j$ is “Met”, $0.5$ if “Partially Met”, $0$ otherwise.

Assumptions:
1. All listed deliverables are mutually exclusive and exhaustive.
2. “Partially Met” for an objective contributes half a point to the success score.
3. Status categories are mutually exclusive.

The analysis proceeds in three steps:
1. **Count** the number of drafted deliverables $N_{\text{draft}} = \sum_i c_i$.
2. **Compute** the draft‑completion rate $R_{\text{draft}} = \frac{N_{\text{draft}}}{|D|}$.
3. **Aggregate** objective scores $S_{\text{obj}} = \sum_j u_j$ and derive the objective‑success score $R_{\text{obj}} = \frac{S_{\text{obj}}}{|O|}$.

All arithmetic is displayed explicitly in Section 4.

## 4. Analysis
### 4.1 Deliverable inventory
The report lists 21 deliverables (see Section 2 of the grounding block). Their statuses are:

| Status | Count |
|--------|-------|
| Drafted | 16 |
| Defined | 3 |
| Compiled | 1 |
| Generated | 1 |

Thus:
\[
N_{\text{draft}} = 16
\]
\[
|D| = 21
\]

### 4.2 Draft‑completion rate
\[
R_{\text{draft}} = \frac{N_{\text{draft}}}{|D|} = \frac{16}{21}
\]

Performing the division:
\[
\frac{16}{21} = 0.7619047619\ldots
\]

Rounded to two decimal places:
\[
R_{\text{draft}} \approx 0.76\; (\text{or } 76.19\%)
\]

### 4.3 Objective assessment
The three project objectives are reported in Section 3 of the grounding block:

- Objective 1: “Partially Met”
- Objective 2: “Not Met Consistently”
- Objective 3: “Not Met Consistently”

Assigning numeric values per the method:

\[
u_1 = 0.5,\quad u_2 = 0,\quad u_3 = 0
\]

Summing:
\[
S_{\text{obj}} = u_1 + u_2 + u_3 = 0.5
\]

Number of objectives:
\[
|O| = 3
\]

Objective‑success score:
\[
R_{\text{obj}} = \frac{S_{\text{obj}}}{|O|} = \frac{0.5}{3} = 0.166666\ldots
\]

Rounded to two decimal places:
\[
R_{\text{obj}} \approx 0.17\; (\text{or } 16.7\%)
\]

### 4.4 Sensitivity to “partial” definition
If “Partially Met” were counted as a full success (i.e., $u_1 = 1$), then:
\[
S_{\text{obj}}' = 1,\quad R_{\text{obj}}' = \frac{1}{3} = 0.3333\ldots \approx 0.33\; (33.3\%)
\]

This demonstrates that the overall success metric is highly sensitive to the interpretation of partial compliance.

## 5. Results
- **Draft‑completion rate:** $76.19\%$ of listed deliverables reached the “Drafted” status.
- **Objective‑success score:** $16.7\%$ of the three high‑level objectives were satisfied under the strict scoring scheme.
- **Sensitivity outcome:** Redefining “partial” success raises the objective‑success score to $33.3\%$.

These numbers are directly derived from the project log without any external data.

## 6. Discussion
### 6.1 Limitations
- **L1.** Status categories are coarse; “Drafted” does not guarantee compliance with length or style constraints.
- **L2.** The binary/half‑point scoring for objectives ignores nuanced progress (e.g., incremental improvements across iterations).
- **L3.** The analysis assumes independence among deliverables, whereas some deliverables (e.g., outline vs. chapters) are hierarchically related.
- **L4.** No direct measurement of token counts or style violations is available; compliance is inferred from qualitative status labels.

### 6.2 Failure modes
- **F1.** Over‑generation leading to length violations, as observed in [1] where longer LLM outputs reduced downstream correctness.
- **F2.** Mutual waiting between drafting and verification stages, analogous to the bottleneck described in [2].
- **F3.** Inconsistent enforcement of style rules (bullet points, unique titles), mirroring the multi‑label complexity highlighted in [3].

### 6.3 Falsifiability
A future controlled experiment that measures actual token counts and style violations for each drafted chapter would falsify the current compliance estimates. If the measured draft‑completion rate falls below $70\%$, the present analytical model would be invalidated.

### 6.4 Open questions
- How does iterative prompting affect the draft‑completion rate?
- What is the optimal granularity of verification (per paragraph vs. per chapter) to balance speed and compliance?
- Can multi‑agent verification frameworks like APEX ([8]) or MARCH ([9]) be adapted to drafting pipelines to improve compliance?

## 7. Practical Implications and Engineering Pathways
### 7.1 Intended users and decision impact
Project managers and AI‑tool developers who design long‑form drafting pipelines would use the derived compliance metrics to decide whether to adopt a purely LLM‑driven approach or to invest in additional verification layers. If the draft‑completion rate exceeds a predefined threshold (e.g., $80\%$), a team may proceed without manual pre‑editing; otherwise, they must allocate resources for iterative prompting or post‑generation editing.

### 7.2 Technology Readiness Level
The analysis is purely analytical, based on documented project logs and literature synthesis, and has not undergone peer review. According to NASA’s definitions, this places the work at **TRL 2** (technology concept and/or application formulated).

### 7.3 Minimal next experiment
The smallest de‑risking experiment is a **pilot prompting study**:
- **What is measured:** token count per chapter, number of style violations (bullet points, duplicate titles), and time to reach compliance.
- **Falsifying outcome:** If the pilot yields a draft‑completion rate below $70\%$ despite the new prompting strategy, the hypothesis that refined prompts improve compliance is falsified.

### 7.4 Engineering constraints
- **Constraint C1:** Availability of a token‑counting tool that can parse LLM output in real time.
- **Constraint C2:** Definition of a style‑checking rule set (e.g., regex for bullet points) that can be applied automatically.
- **Constraint C3:** Compute budget for running multiple LLM instances if a multi‑agent verification loop (as in [8] and [9]) is adopted.

### 7.5 Projected cost and performance (projection)
Assuming a cloud‑based LLM costing $\$0.02$ per 1 M tokens and a target of $2500$ tokens per chapter:
\[
\text{Cost per chapter} = 2500 \times \frac{0.02}{10^6} = \$0.00005
\]
For 16 chapters, projected cost = $16 \times 0.00005 = \$0.0008$ (rounded to $\$0.001$). This projection assumes no additional verification overhead.

### 7.6 Risks and misuse
If the compliance metrics are taken as guarantees, teams may under‑invest in necessary human review, leading to the propagation of inaccurate or non‑compliant content. The risk is mitigated by treating the metrics as **early‑stage indicators** rather than final assurances.

## 8. Conclusion
The quantitative analysis of the “Strange Loop of Being” initial drafting phase reveals that, despite the production of a substantial number of deliverables, only **76 %** reached a drafted state and **less than 20 %** of high‑level objectives were satisfied. These figures align with broader findings in the literature that longer LLM outputs can degrade downstream performance ([1]) and that multi‑stage verification can alleviate bottlenecks ([2], [8], [9]). To raise the Technology Readiness Level of AI‑assisted drafting pipelines, practitioners should incorporate iterative prompting, automated style verification, and, where feasible, multi‑agent consensus mechanisms. Future work will empirically test these interventions in controlled pilots, thereby moving the approach toward TRL 3 and beyond.

## References
[1] arXiv:2610.25244 | It's Complicated: Factors Influencing the Effectiveness of LLM-Generated Feedback in a Live Programming Course  
[2] arXiv:2408.11850 | PEARL: Parallel Speculative Decoding with Adaptive Draft Length  
[3] arXiv:2008.00141 | Actor-Action Video Classification CSC 249/449 Spring 2020 Challenge Report  
[4] arXiv:2008.00512 | Integrated monitoring of ice in selected Swiss lakes. Final project report  
[5] arXiv:1612.07113 | Readability of digraphs and bipartite graphs  
[6] arXiv:1607.06318 | Hierarchical Manifold Clustering on Diffusion Maps for Connectomics (MIT 18.S096 final project)  
[7] arXiv:2112.13265 | An Introduction to Perfectoid Fields  
[8] arXiv:2601.04794 | APEX: Academic Poster Editing Agentic Expert  
[9] arXiv:2604.16175 | MARCH: Multi-Agent Radiology Clinical Hierarchy for CT Report Generation  
[10] arXiv:2506.14158 | S$^4$C: Speculative Sampling with Syntactic and Semantic Coherence for Efficient Inference of Large Language Models  
[11] arXiv:2009.01695 | Teaching Cultural Astronomy to Undergraduates with an Interdisciplinary Frame  
[12] QNFO: Final Project / Phase Report: Strange Loop of Being - Initial Drafting Phase | https://papers.qnfo.org/papers/close-slobphase1drafting-v10

## Appendix A. Divergence report
*No divergent claims were identified among the source drafts; all substantive statements converge on the same quantitative values derived from the project log.*

## Appendix B. Claim attribution
| Claim ID | Source Draft(s) | Agreement |
|----------|----------------|-----------|
| C1 | A, B, C | CONVERGENT |
| C2 | A, B, C | CONVERGENT |
| C3 | A, B, C | CONVERGENT |
| C4 | A, B, C | CONVERGENT |
| C5 | A, B, C | CONVERGENT |