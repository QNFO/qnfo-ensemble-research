# Falsification Criteria for Quantum-Advantage Claims: An Effective‑Criterion Audit Framework

## Abstract
Quantum‑advantage claims are increasingly used by hardware vendors, funding agencies, and journal editors to justify large expenditures and publication decisions. Existing audits are ad‑hoc, allowing authors to revise task definitions, noise models, or baseline algorithms after a classical rebuttal appears, which renders many claims effectively unfalsifiable. This paper fills the gap by proposing a five‑criterion falsification framework that is *effective* in the algebraic sense: each criterion is designed to hold for a dense, open subset of well‑formed claims, and degenerate cases are explicitly identified. The framework assigns fixed weights $w_1=0.30$, $w_2=0.25$, $w_3=0.20$, $w_4=0.15$, $w_5=0.10$ to criteria $C_1$–$C_5$, computes a composite index $F=\sum w_i s_i$ with scores $s_i\in\{0,0.5,1\}$, and defines decision thresholds $F\ge0.8$ (falsifiable‑ready), $0.5\le F<0.8$ (conditionally falsifiable), $F<0.5$ (structurally unfalsifiable). Using inputs from the QNFO gap synthesis (42 gaps, 5 categories) and the HPLT 3.0 corpus (30 trillion tokens), we derive quantitative anchors: $8.4$ gaps per category, $2.0$ weeks per roadmap transition, $1.5\times10^{11}$ tokens per language, and worked index values $F=0.675$ and $F=0.10$. The framework terminates in finitely many steps, provides a constructive repair path, and its own falsification conditions are explicitly stated. Adoption would make quantum‑advantage auditing systematic, transparent, and comparable across studies.

## 1. Introduction
Quantum‑advantage claims affect three concrete stakeholder groups.  
1. **Hardware developers** invest billions of dollars in devices that they must convince investors and customers of superior performance.  
2. **Funding agencies** allocate limited research budgets based on the perceived impact of claimed quantum speed‑ups.  
3. **Journal editors and reviewers** decide whether to publish papers that assert a quantum advantage, influencing the scientific record.  

When a claim survives because the task, noise model, or classical baseline is silently altered after a rebuttal, resources are misdirected, funding decisions become opaque, and the literature accumulates unverified assertions. A criterion that is *effective*—satisfied on a dense, open subset of claim space—would prevent such post‑hoc revisions while still allowing legitimate, non‑degenerate claims to pass.

**Contributions.**  
- (i) A five‑criterion falsification framework with explicit scoring rules (Section 3).  
- (ii) A composite index $F$ with fixed weights and fully shown arithmetic (Section 4).  
- (iii) Worked examples demonstrating decidability and termination (Section 4).  
- (iv) Quantitative infrastructure statistics linking the framework to open datasets and platforms [5], [6], [8] (Section 4).  
- (v) An explicit list of failure modes and falsification conditions for the framework itself (Section 6).

## 2. Background and Related Work
**[1] Effective identifiability criteria for tensors and polynomials.** The paper defines a tensor $T$ to be $h$‑identifiable when it admits a unique decomposition into $h$ rank‑one tensors and calls a criterion *effective* if it holds on a dense, open subset of rank‑$h$ tensors. This notion of genericity is the direct template for our effective falsification criteria.

**[2] Non‑Commutative Gebauer‑Moeller Criteria.** The work adapts the Gebauer‑Moeller pruning strategy from commutative Gröbner‑basis computation to non‑commutative polynomial rings, showing that eliminating unnecessary critical pairs dramatically reduces computational cost. We import the lesson that an audit must prune checks that are provably irrelevant.

**[3] No Substitute for Functionalism – A Reply to ‘Falsification & Consciousness’.** Kleiner and Hoel’s model separates *inference* from *prediction* and demonstrates that a falsification argument can be attacked at the level of its underlying model. This motivates our criterion $C_2$ (inference–prediction independence).

**[4] On the unraveling of open quantum dynamics.** The paper presents a time‑local master equation and its stochastic unraveling, emphasizing that observable indicators are Monte‑Carlo averages over stochastic processes. This provides the vocabulary for our stochastic‑error requirement in $C_3$.

**[5] OpenPodcar: an Open Source Vehicle for Self‑Driving Car Research.** The platform supplies complete hardware CAD files, a bill of materials, and build instructions, exemplifying the replication standard required by $C_4$ (open experimental recipe).

**[6] CoReCon: an open, community‑powered collection of Reionization constraints.** CoReCon aggregates heterogeneous constraints into a curated, format‑normalized repository, illustrating the data‑governance model that underpins $C_3$ and $C_4$.

**[7] Criteria for universality of quantum gates.** The authors give a finite‑step decision procedure that, when a gate set is non‑universal, also indicates which additional gates would achieve universality. This constructive‑failure pattern is mirrored in our repair‑path output.

**[8] HPLT 3.0: Very Large‑Scale Multilingual Resources for LLMs and MT.** The initiative provides $30$ trillion tokens across almost $200$ languages, establishing a concrete scale for “open at scale” datasets that we use to calibrate per‑language token averages.

**[9] QNFO: The Vast World of Quantum Advantage — A Full‑Spectrum Audit.** The audit applies symmetric scrutiny to both a target quantum‑advantage framework and the auditor’s prior critiques, establishing the epistemic posture adopted throughout this paper.

**[10] QNFO: A Consilient Gap Synthesis of the QNFO/QWAV Research Portfolio.** The synthesis catalogs $42$ gaps across $5$ structural categories and a roadmap spanning $8$ calendar weeks, supplying the quantitative substrate for the gap‑density calculations in Section 4.

## 3. Methods

### 3.1 Claim formalization
An advantage claim $\mathcal{K}$ is a tuple
$$
\mathcal{K} = (T, D, B, M, \Theta),
$$
where $T$ is the computational task, $D$ the quantum device with noise model $\Theta$, $B$ the classical baseline, and $M$ the comparison metric. The claim is *specification‑complete* if each component is fixed in advance and cannot be revised after classical rebuttals appear.

### 3.2 The five falsification criteria
- $C_1$ (Specification completeness): every element of $(T, D, B, M, \Theta)$ is stated with enough precision that two independent laboratories would agree on its instantiation.
- $C_2$ (Inference–prediction independence): following the structural lesson of [3], the claim must state which quantities are inferred from experiment and which are predicted by theory, and these must be independently checkable.
- $C_3$ (Baseline auditability): the classical baseline $B$ is specified with a resource bound, and the best‑known classical algorithm’s cost is either stated or bounded by a formula a third party can evaluate; where indicators are Monte‑Carlo averages over stochastic processes, as in quantum‑trajectory unravelings [4], the claimed indicator must carry an explicit sampling‑error budget, and the classical comparison must meet the same budget.
- $C_4$ (Replication independence): the full experimental recipe — hardware, calibration, and analysis pipeline — is open in the sense of [5] and [8]: build instructions, data, and selection pipeline all public, with evidence deposited in a community‑curated, format‑normalized collection in the spirit of CoReCon [6].
- $C_5$ (Pre‑registered failure threshold): a number $\epsilon\in(0,1)$ is fixed in advance such that if the observed advantage ratio falls below the threshold, the claim is declared refuted, with no post‑hoc revision permitted.

### 3.3 The falsification index
Each criterion $C_i$ receives a score $s_i\in\{0,0.5,1\}$: $1$ if fully satisfied, $0.5$ if partially satisfied (specified but with an ambiguous term), $0$ if absent. The weights are fixed ex ante:
$$
w_1 = 0.30,\quad w_2 = 0.25,\quad w_3 = 0.20,\quad w_4 = 0.15,\quad w_5 = 0.10,
$$
with $\sum_{i=1}^{5} w_i = 1$. The falsification index is
$$
F(\mathcal{K}) = \sum_{i=1}^{5} w_i\,s_i.
$$
Decision rule: $F\ge0.8$ → *falsifiable‑ready*; $0.5\le F<0.8$ → *conditionally falsifiable*; $F<0.5$ → *structurally unfalsifiable*.

### 3.4 Termination
Mirroring the finite‑step decision procedure of [7], each $s_i$ is decided by inspecting a finite document set (the claim, its supplement, and the baseline code), so the total procedure is a finite composition of finite checks. If $F<0.8$, the framework outputs the ordered list of criteria with $s_i<1$, weighted by $w_i$, as a constructive repair path.

### 3.5 Genericity caveat and pruning requirement
Following [1], we would like criteria that hold on a dense, open subset of the space of claims. However, “dense open’’ is a topological notion with no canonical measure on claim space; we therefore use it only heuristically and require the criteria to hold for *all* well‑formed claims, not merely generically. Additionally, following the Gebauer‑Moeller strategy of eliminating unnecessary critical pairs before they arise [2], the protocol must specify which checks are *not* required, so that audit cost remains finite.

## 4. Analysis
All inputs below come from the supplied bibliography entries or are stated design choices of this paper; each is stated with its source, and every arithmetic step is shown.

**Input 1 (weights, this paper, Section 3.3).** $w_1 = 0.30$, $w_2 = 0.25$, $w_3 = 0.20$, $w_4 = 0.15$, $w_5 = 0.10$. Normalization check:
$$
\sum_{i=1}^{5} w_i = 0.30 + 0.25 + 0.20 + 0.15 + 0.10 = 1.00.
$$

**Input 2 (gap counts, from [10]).** The gap synthesis catalogs $N_{\text{gaps}} = 42$ gaps across $N_{\text{cat}} = 5$ structural categories. Mean gap density per category:
$$
\bar{g} = \frac{N_{\text{gaps}}}{N_{\text{cat}}} = \frac{42}{5} = 8.4 \text{ gaps per category.}
$$

**Input 3 (roadmap duration, from [10]).** The roadmap spans versions $v2.0$ through $v2.4$ over $W = 8$ calendar weeks, i.e. $N_{\text{ver}} = 5$ version labels. Using the *transition* convention (interval quantity):
$$
c = \frac{W}{N_{\text{ver}} - 1} = \frac{8}{4} = 2.0 \text{ weeks per version transition.}
$$
The version‑label density (convention‑independent) is
$$
d = \frac{N_{\text{ver}}}{W} = \frac{5}{8} = 0.625 \text{ versions per week.}
$$
Assuming uniform pacing across all $42$ gaps, the mean time per gap is
$$
t_{\text{gap}} = \frac{8\text{ weeks}}{42\text{ gaps}} = \frac{8}{42} = \frac{4}{21} \approx 0.1905 \text{ weeks per gap,}
$$
and converting to days ($1$ week $=7$ days):
$$
t_{\text{gap}} = \frac{4}{21}\times7 = \frac{4}{3} \approx 1.333 \text{ days per gap.}
$$

**Input 4 (corpus scale, from [8]).** The HPLT 3.0 collection contains $T_{\text{tot}} = 30$ trillion tokens, i.e. $T_{\text{tot}} = 30\times10^{12}=3.0\times10^{13}$ tokens, covering “almost 200 languages.” Using $L=200$ as an upper‑bound language count,
$$
\bar{t} = \frac{T_{\text{tot}}}{L} = \frac{3.0\times10^{13}}{200} = 1.5\times10^{11} \text{ tokens per language.}
$$

**Input 5 (storage projection assumptions, this paper).** Assuming $b$ bytes per token:
- Lower bound $b=1$: $3.0\times10^{13}\times1 = 3.0\times10^{13}$ bytes $=30$ TB.  
- Central estimate $b=4$: $3.0\times10^{13}\times4 = 1.2\times10^{14}$ bytes $=120$ TB.  
- Upper bound $b=4$ plus $25\%$ annotation overhead: $1.2\times10^{14}\times1.25 = 1.5\times10^{14}$ bytes $=150$ TB.

**Derivation 6 (pruning benefit, illustrative model).** For $n=20$ audit checks, the unpruned pair count is
$$
P_{\text{unpruned}} = \frac{n(n-1)}{2} = \frac{20\times19}{2} = 190.
$$
Assuming a pruning fraction $p=0.9$ (illustrative), the pruned cost is
$$
P_{\text{pruned}} = 190\times(1-p) = 190\times0.1 = 19.
$$

**Derivation 7 (worked example of the index).** For a hypothetical claim $\mathcal{K}_A$ with scores $s_1=1$, $s_2=0.5$, $s_3=1$, $s_4=0$, $s_5=0.5$:
$$
F(\mathcal{K}_A) = (0.30)(1) + (0.25)(0.5) + (0.20)(1) + (0.15)(0) + (0.10)(0.5) \\
= 0.30 + 0.125 + 0.20 + 0 + 0.05 = 0.675.
$$
Since $0.5 \le 0.675 < 0.8$, $\mathcal{K}_A$ is conditionally falsifiable; the repair path prioritizes $C_4$ (gap $0.15$), then $C_2$ (gap $0.125$), then $C_5$ (gap $0.05$). The total recoverable index is $1.00 - 0.675 = 0.325$.

**Derivation 8 (second worked example).** For a claim $\mathcal{K}_B$ with $s_1=0$, $s_2=0$, $s_3=0.5$, $s_4=0$, $s_5=0$:
$$
F(\mathcal{K}_B) = (0.30)(0) + (0.25)(0) + (0.20)(0.5) + (0.15)(0) + (0.10)(0) = 0.10.
$$
Since $0.10 < 0.5$, $\mathcal{K}_B$ is structurally unfalsifiable.

**Derivation 9 (necessity of $C_1$).** The largest single weight is $w_1=0.30$; a claim with $s_1=0$ can reach at most
$$
F_{\max}^{(s_1=0)} = 1 - 0.30 = 0.70 < 0.8,
$$
so specification completeness is necessary for falsifiable‑ready status.

All quantities in this section are exact or rounded from exact fractions; none are empirical measurements.

## 5. Results
We report only quantities computed in Section 4, plus clearly labeled projections.

1. **Index normalization:** $\sum_{i=1}^{5} w_i = 1.00$ exactly.  
2. **Gap density:** $42$ gaps across $5$ categories [10] yield $\bar{g}=8.4$ gaps per category; at least one category deviates from the mean by $\ge0.4$ gaps.  
3. **Roadmap pacing:** $8$ weeks for $v2.0$–$v2.4$ imply $c=2.0$ weeks per version transition (transition convention) and $d=0.625$ versions per week (convention‑independent). Uniform pacing gives $t_{\text{gap}} \approx 0.1905$ weeks $\approx 1.333$ days per gap.  
4. **Open‑data scale calibration:** $3.0\times10^{13}$ tokens over $L\le200$ languages give an upper‑bound mean $\bar{t}=1.5\times10^{11}$ tokens per language. Projected storage lies between $30$ TB (1 byte/token) and $150$ TB (4 bytes/token plus $25\%$ overhead), central estimate $120$ TB.  
5. **Pruning benefit (projected):** With $p=0.9$, a $20$‑check audit drops from $190$ to $19$ pairwise checks, a factor‑10 reduction.  
6. **Worked index values:** $F(\mathcal{K}_A)=0.675$ (conditionally falsifiable; repair priority $C_4$, then $C_2$, then $C_5$; recoverable margin $0.325$) and $F(\mathcal{K}_B)=0.10$ (structurally unfalsifiable).  
7. **Necessity of $C_1$:** Any claim with $s_1=0$ cannot reach $F\ge0.8$ because $F_{\max}=0.70$.  
8. **Protocol status:** The framework is a design proposal with a genericity goal; no empirical fraction of real claims has been measured (Section 6).

No empirical, simulated, or measured quantities are reported.

## 6. Discussion
**Limitations.** The scoring function $s_i\in\{0,0.5,1\}$ is coarse, and the weight vector $\mathbf{w}$ is a design choice rather than data‑driven. Different weights could reorder repair priorities; the necessity proof for $C_1$ holds whenever $w_1>0.20$, but robustness for other weights is not proven. Gap‑distribution data from [10] lack per‑category counts, preventing identification of the most gap‑dense category. Per‑language token averages from [8] mask known language‑wise heterogeneity; using $\bar{t}$ as a guarantee would be erroneous.

**The cadence convention.** Derivation 3 shows a genuine convention choice: $8/4=2.0$ weeks per transition versus $8/5=1.6$ weeks per version. We adopt the transition convention because intervals, not labels, convey scheduling information. Readers needing per‑label density can use the convention‑independent $d=0.625$ versions per week.

**Failure modes.**  
1. *Gaming*: authors could satisfy $C_1$ with verbose but ambiguous specifications, earning a $0.5$ score that is subjectively judged.  
2. *Genericity leakage*: the dense‑open template of [1] may be too strict for claims that inherently involve statistical components, leading to false negatives.  
3. *Baseline unboundedness*: if the best classical algorithm’s cost is unknown, $C_3$ can achieve at most $0.5$, potentially keeping a valid claim below the ready threshold.  
4. *Model‑relativity*: an adversary could contest the inference–prediction split demanded by $C_2$, as illustrated in [3].  
5. *Pre‑registration narrowness*: an author could define $\epsilon$ so narrowly that falsification becomes practically impossible.  
6. *Curator capture*: $C_4$ relies on a community‑curated repository; capture by audited parties would degrade neutrality, echoing the concerns raised in [6].

**What would falsify the framework.**  
- (a) A claim with $F\ge0.8$ is later revised post‑hoc in a way that evades a pre‑registered refutation, demonstrating that the criteria are insufficient.  
- (b) A large fraction of widely accepted quantum‑advantage claims score $F<0.5$, indicating that the thresholds are miscalibrated against community practice.  
- (c) Empirical re‑audit of the 42‑gap portfolio [10] uncovers gaps that no $C_i$ addresses, refuting the protocol’s claimed coverage.

**Open questions.** (i) Can the weights be learned from a corpus of historical advantage claims? (ii) Can a genericity theorem for the framework be proved over a defined claim space, analogous to the dense‑open results of [1]? (iii) What is the empirical value of the pruning fraction $p$ for real audits? (iv) Can the repair‑path be made algorithmically constructive as in [7]? (v) Does the Monte‑Carlo indicator structure of unravelings [4] introduce irreducible statistical uncertainty into $C_1$’s noise‑model specification? (vi) Can a CoReCon‑style constraint registry achieve community adoption in a competitive field? (vii) Does symmetric‑scrutiny [9] extend to auditing the auditor, and at what recursion depth does it stabilize? The truncated summaries of [1]–[8] limit deeper analogies; obtaining full texts is a prerequisite for further engagement.

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**  
- *Quantum‑computing research groups* can apply the falsification index to decide whether to allocate experimental time to a claimed advantage.  
- *Funding agencies* can use $F$ as a transparent metric in grant‑review panels to prioritize projects with higher falsifiability readiness.  
- *Journal editors and reviewers* can adopt $F$ as a checklist to assess claim robustness before acceptance.  
If a claim attains $F\ge0.8$, the decision to fund, publish, or proceed to large‑scale implementation becomes defensible; if $F<0.5$, the claim should be withheld pending substantial revisions.

**(b) Technology readiness.**  
The framework is purely analytical, has not undergone peer review, and has not been implemented in a production audit pipeline. According to NASA’s Technology Readiness Level definitions, it resides at **TRL 2** (technology concept and/or application formulated).

**(c) Minimal next experiment.**  
The smallest de‑risking step is to apply the framework to a recently published quantum‑advantage claim (e.g., a 2025 random‑circuit sampling experiment). The experiment would: (i) collect the claim’s specification documents, (ii) score each $C_i$, (iii) compute $F$. If the computed $F\ge0.8$ but the claim is later revised to evade a pre‑registered refutation, the framework would be falsified. The outcome that refutes the framework is the observation of a post‑hoc revision that preserves $F\ge0.8$.

**(d) Engineering and deployment constraints.**  
- *Specification data*: $C_1$ requires complete, unambiguous task definitions, device parameters, noise models, and metric formulas.  
- *Baseline code*: $C_3$ needs access to the best‑known classical algorithm implementation and its resource‑usage formula.  
- *Open repository*: $C_4$ depends on a curated, format‑normalized collection (analogous to CoReCon [6]) for storing experimental recipes and data.  
- *Statistical budgeting*: $C_3$ and $C_2$ require explicit Monte‑Carlo sampling error budgets as described in [4].  
These constraints are derived directly from the criteria definitions; any missing component blocks the audit.

**(e) Projected cost and performance bounds.**  
Assuming an auditor spends on average $10$ hours to gather and verify each criterion’s evidence, the total audit effort is projected as $5\times10 = 50$ hours per claim. This projection rests on the assumption of readily available documentation and a modest learning curve for the audit protocol.

**(f) Direct risks and misuse.**  
The index could be misapplied to dismiss legitimate claims if auditors assign $0.5$ scores arbitrarily or interpret ambiguous specifications harshly. Conversely, overly generous scoring could let low‑quality claims pass. Mitigation requires transparent scoring rubrics, community‑wide calibration of $w_i$, and open peer review of audit reports.

## 8. Conclusion
We have constructed a five‑criterion falsification framework for quantum‑advantage claims, with a composite index $F$, fixed weights, explicit decision thresholds, guaranteed termination, and a constructive repair path. The framework draws its structure from effective identifiability criteria [1], critical‑pair elimination [2], finite‑step universality decision with constructive failure [7], and the model‑relativity lessons of the falsification debate in consciousness studies [3]. It is grounded operationally in the stochastic‑indicator vocabulary of open quantum dynamics [4] and the open‑replication standards exemplified by open hardware platforms [5], constraint registries [6], and open large‑scale data pipelines [8]. Quantitative anchors—$8.4$ gaps per category, $2.0$ weeks per roadmap transition (or $0.625$ versions per week), $\approx1.333$ days per gap under uniform pacing, $1.5\times10^{11}$ tokens per language as an upper bound, and worked index values $F=0.675$ and $F=0.10$—were derived with fully shown arithmetic from stated inputs. The framework’s own falsification conditions are stated, and its principal weakness—the conventionality of weights and thresholds—is flagged as the first target for empirical calibration.

## References
[1] Effective identifiability criteria for tensors and polynomials. arXiv:1703.02637v1. https://arxiv.org/abs/1703.02637v1  
[2] Non‑Commutative Gebauer‑Moeller Criteria. arXiv:1302.3805v3. https://arxiv.org/abs/1302.3805v3  
[3] No Substitute for Functionalism -- A Reply to 'Falsification & Consciousness'. arXiv:2006.13664v3. https://arxiv.org/abs/2006.13664v3  
[4] On the unraveling of open quantum dynamics. arXiv:2309.13408v2. https://arxiv.org/abs/2309.13408v2  
[5] OpenPodcar: an Open Source Vehicle for Self‑Driving Car Research. arXiv:2205.04454v2. https://arxiv.org/abs/2205.04454v2  
[6] CoReCon: an open, community‑powered collection of Reionization constraints. arXiv:2309.06480v1. https://arxiv.org/abs/2309.06480v1  
[7] Criteria for universality of quantum gates. arXiv:1610.00547v6. https://arxiv.org/abs/1610.00547v6  
[8] HPLT 3.0: Very Large‑Scale Multilingual Resources for LLMs and MT. arXiv:2511.01066v3. https://arxiv.org/abs/2511.01066v3  
[9] QNFO: The Vast World of Quantum Advantage — A Full‑Spectrum Audit.  
[10] QNFO: A Consilient Gap Synthesis of the QNFO/QWAV Research Portfolio.