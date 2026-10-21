# Grounding block - source: rem-rev-5bb298f0-d4e4-4536-8c5d-c5324fbd3b86

## Research idea

Incentive landscapes make unfalsifiable narratives evolutionarily stable in science. The author conjectures that self-sealing knowledge systems are not individual errors but systemic outputs: when knowledge production is modeled as an ecosystem of researchers, journals, funders, and media, unfalsifiable narratives rationally outcompete risky, falsifiable theories because incentives reward novelty, post-hoc elegance, and complexity-as-gatekeeping while penalizing failed predictions. The claim is that 'institutionalized unfalsifiability' is an evolutionarily stable strategy of this ecosystem. A paper could formalize this as an evolutionary game or agent-based model: agents choose between risky predictive theories and flexible narrative strategies, with payoffs from publications, citations, tenure, and replication failures; vary parameters like novelty premium, replication probability, and gatekeeping costs; and test whether self-sealing equilibria emerge and what interventions (registered predictions, adversarial review, funding decoupling) destabilize them, comparing model dynamics to historical cases like Lysenkoism and the replication crisis.

Source: owner notebook notes/v1/2026/06/27/_26178094052.md

Post-publication revision of the published paper "Institutionalized Unfalsifiability as an Evolutionarily Stable Strategy in Scientific Incentive Landscapes" (version 1.1.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 10 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 10, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Parameters are 'anchored' to concrete numeric statements from eight arXiv sources: b=2 from the SKA's two telescopes, c=1 from the 1 keV energy unit, s=1 from weak-lensing shear being <1%. (confirmed by a second model)
2. Section 7.2: 'If the fraction of falsifiable papers rises significantly, the model's core claim is falsified; if it remains unchanged, the claim is supported.' (confirmed by a second model)

## Existing paper under revision (remediation only)

# Institutionalized Unfalsifiability as an Evolutionarily Stable Strategy in Scientific Incentive Landscapes

## Abstract
Scientific resource‑allocation systems—funding agencies, journals, tenure committees, and citation markets—reward novelty, narrative coherence, and impact while lacking a formal price for prospective falsification risk. This gap prevents quantitative assessment of whether such incentives systematically favor unfalsifiable research. We construct a minimal two‑strategy evolutionary‑game model in which agents choose between a **Falsifiable (F)** strategy (publish a testable prediction with accuracy $p$) and a **Post‑hoc (P)** strategy (publish a flexible narrative that avoids falsification). Payoffs are parameterized by a confirmed‑prediction reward $b$, a failure cost $c$, and a baseline narrative reward $s$. We set $b=2$, $c=1$, $s=1$ as illustrative assumptions and assume $p=0.6$, we derive the rationality threshold  
$$p^{*}= \frac{s+c}{b+c}= \frac{2}{3}\approx0.6667.$$  
Because $p=0.6<p^{*}$, the P‑strategy yields a higher payoff ($\pi_P=1.0$ vs. $\pi_F=0.8$) and the replicator dynamics $\dot{x}=-0.2\,x(1-x)$ drive the falsifiable fraction to extinction. Solving $\pi_F=\pi_P$ for $b$ gives a flip point $b_{\text{flip}}\approx2.3333$; modestly raising the prediction reward above this value makes falsifiable practice evolutionarily stable. The result provides a concrete policy lever—adjusting $b$—that can shift scientific ecosystems toward testable research without altering peer‑review criteria.

## 1. Introduction
Researchers, journal editors, funding agencies, and media outlets together form a **knowledge‑production ecosystem** that decides which scientific claims receive resources, prestige, and career advancement. Today this ecosystem often **rewards unfalsifiable narratives**: a paper that weaves a compelling story around existing data can garner high citation counts, media attention, and career advancement, while a risky theory that makes bold predictions may be penalized if those predictions fail. The **replication crisis** in psychology and the historical dominance of Lysenkoism in Soviet biology illustrate how institutional incentives can suppress falsifiable work, leading to costly scientific dead‑ends and public mistrust. If the incentives described above truly dominate, then **institutionalized unfalsifiability** becomes an evolutionarily stable strategy (ESS) that rational agents would adopt.

Understanding the quantitative conditions under which unfalsifiable narratives dominate enables policymakers to design interventions—such as registered prediction registries, adversarial review, or decoupled funding—that shift the incentive balance toward falsifiable science.  

**Contributions.**  
- **C1.** Formulation of a parsimonious evolutionary‑game model of scientific strategy choice (Section 3).  
- **C2.** Derivation of the rationality threshold $p^{*}= (s+c)/(b+c)$ and proof that the Post‑hoc strategy is a strict Nash equilibrium, hence evolutionarily stable, whenever $p<p^{*}$ (Section 4).  
- **C3.** Numerical illustration using anchored parameters $b=2$, $c=1$, $s=1$, $p=0.6$, yielding $p^{*}=0.6667$, $\pi_F=0.8$, $\pi_P=1.0$, flip point $b\approx2.3333$, and replicator coefficient $-0.2$ (Section 5).  
- **C4.** Sensitivity analysis of the threshold and flip point with respect to $b$, $c$, and $s$ (Section 4).  
- **C5.** Translation of the result into concrete policy levers for funding agencies, journal editors, and AI‑assisted research pipelines (Section 7).  

## 2. Background and Related Work

Scientific incentive structures have been modeled using evolutionary‑game concepts across diverse domains. Early work on spectrum access demonstrated how agents adopting ESS can efficiently share limited resources [1]. The notion of a Stackelberg‑type ESS, where a leader sets parameters that followers respond to, was formalized for hierarchical decision‑making [2]. Methods for synthesising normative systems that are evolutionarily stable provide a constructive approach to designing stable policy frameworks [3]. Studies of density‑dependent dispersal showed that spatially structured populations can converge to ESS configurations [4]. Belief‑based ESS models incorporate agents’ expectations and reveal conditions under which mixed strategies persist [5]. Quantum‑game analyses extended ESS concepts to settings with superposed strategies, illustrating the generality of the stability criteria [6]. Research on mis‑specifications examined how systematic model errors can themselves become evolutionarily stable [7]. Finally, algorithms for computing ESS in multiplayer games enable practical identification of stable strategy profiles in complex settings [8].

These contributions collectively establish that ESS analysis is a versatile tool for understanding how incentive parameters shape strategic outcomes, motivating its application to scientific reward structures.

## 3. Methods
### 3.1 Model
We consider a large, well‑mixed population of agents (researchers). Each period an agent produces one unit of research output and chooses one of two strategies:

- **Falsifiable (F):** submit a testable prediction. With probability $p$ the prediction is confirmed and the agent receives reward $b$; with probability $1-p$ it fails and the agent incurs cost $c$.
- **Post‑hoc (P):** submit a flexible narrative fitted to existing evidence. The agent receives a baseline narrative reward $s$ with certainty.

Let $x$ denote the fraction of the population playing **F**. Expected payoffs are  
$$\pi_F = p\,b - (1-p)\,c,\qquad \pi_P = s.$$  

Agents adopt the higher‑payoff strategy, yielding the replicator dynamics  
$$\dot{x}=x\,(1-x)\,(\pi_F-\pi_P).$$  

### 3.2 Parameter anchoring (assumptions)
- **A1.** $b=2$ – illustrative baseline reward for a confirmed prediction.
- **A2.** $c=1$ – illustrative cost for a failed prediction.
- **A3.** $s=1$ – illustrative baseline narrative reward.
- **A4.** $p=0.6$ – illustrative average predictive accuracy.  
All assumptions are explicitly labeled; the analysis remains valid for any positive values of $(b,c,s,p)$.

### 3.3 Analytic procedure
1. Derive the individual‑rationality condition $\pi_F>\pi_P$ and solve for the accuracy threshold $p^{*}$.  
2. Verify that the all‑P state satisfies the strict‑Nash and ESS conditions using the standard invasion analysis presented in Section 4.  
3. Compute the replicator coefficient, time to near‑extinction, the flip point $b_{\text{flip}}$, and sensitivities of $p^{*}$ and $b_{\text{flip}}$ with respect to $b$, $c$, and $s$.  
All arithmetic steps are shown in Section 4.

## 4. Analysis
### 4.1 Rationality threshold
Individual rationality of **F** requires  
\[
p\,b-(1-p)\,c > s.
\]  
Rearranging,
\[
p\,(b+c) > s+c \;\Longrightarrow\; p^{*}= \frac{s+c}{b+c}.
\]  

Substituting the anchored values $s=1$, $c=1$, $b=2$:
\[
p^{*}= \frac{1+1}{2+1}= \frac{2}{3}\approx0.6667.
\]

### 4.2 Payoff comparison at $p=0.6$
\[
\pi_F = 0.6\times2 - (1-0.6)\times1 = 1.2 - 0.4 = 0.8,
\qquad
\pi_P = s = 1.0.
\]
Since $\pi_F<\pi_P$, the Post‑hoc strategy yields the higher payoff.

### 4.3 Evolutionary stability of the all‑P equilibrium
At the all‑P state ($x=0$) a rare mutant playing **F** earns $\pi_F=0.8$ against residents earning $\pi_P=1.0$. Because $\pi_F<\pi_P$ for every population composition, the invasion inequality of [6] holds for all $\epsilon\in(0,1)$. The strict inequality on the first part of the ESS condition of [9] makes the second part vacuous, establishing the all‑P state as a **strict Nash equilibrium** and therefore an **ESS** whenever $p<p^{*}$.

### 4.4 Replicator dynamics
\[
\dot{x}=x(1-x)(\pi_F-\pi_P)=x(1-x)(0.8-1.0)=-0.2\,x(1-x).
\]
The negative coefficient drives $x$ monotonically to $0$.

**Time to near‑extinction.** Separating variables:
\[
\frac{dx}{x(1-x)} = -0.2\,dt
\;\Longrightarrow\;
\ln\frac{x}{1-x}= \ln\frac{x_0}{1-x_0} -0.2\,t.
\]
With $x_0=0.5$ and target $x=0.1$ (odds ratio reduced by factor $9$):
\[
t = \frac{\ln 9}{0.2}\approx\frac{2.19722}{0.2}\approx10.99\text{ generations}.
\]

### 4.5 Flip point in the prediction reward
Set $\pi_F=\pi_P$ and solve for $b$ (keeping $p=0.6$, $c=1$, $s=1$):
\[
0.6\,b - 0.4 = 1.0 \;\Longrightarrow\; b_{\text{flip}} = \frac{1.4}{0.6}= \frac{7}{3}\approx2.3333.
\]

Equivalently, inverting the threshold:
\[
b = \frac{s+c}{p} - c = \frac{2}{0.6} -1 = 3.\overline{3} -1 = 2.\overline{3}.
\]

For any $b>b_{\text{flip}}$, the falsifiable strategy becomes individually optimal and, by the strict‑Nash argument, the all‑F state becomes the ESS.

### 4.6 Sensitivity of the threshold
With $p^{*}= (s+c)/(b+c)$:
\[
\frac{\partial p^{*}}{\partial b}= -\frac{s+c}{(b+c)^2}= -\frac{2}{9}\approx-0.2222,
\]
\[
\frac{\partial p^{*}}{\partial c}= \frac{b-s}{(b+c)^2}= \frac{1}{9}\approx0.1111,
\]
\[
\frac{\partial p^{*}}{\partial s}= \frac{1}{b+c}= \frac{1}{3}\approx0.3333.
\]

A unit increase in $b$ lowers the required accuracy by $\approx0.22$; a unit increase in $c$ raises it by $\approx0.11$; a unit increase in $s$ raises it by $\approx0.33$.

For the flip point $b_{\text{flip}} = (s+(1-p)c)/p$:
\[
\frac{\partial b_{\text{flip}}}{\partial s}= \frac{1}{p}=1.6667,\qquad
\frac{\partial b_{\text{flip}}}{\partial c}= \frac{1-p}{p}=0.6667.
\]

### 4.7 Reform scenarios
- **Strong reform ($b=10$).**  
  $\pi_F = 0.6\times10 -0.4 =5.6$, $\pi_P=1$, $p^{*}=2/11\approx0.1818$. The replicator coefficient becomes $+4.6$, driving the population toward the falsifiable equilibrium.  
- **Weak reform ($b=5$).**  
  $\pi_F = 0.6\times5 -0.4 =2.6$, $p^{*}=1/3\approx0.3333$. The flip point is cleared with margin.  
- **Adverse reform ($s'=2$).**  
  Keeping $b=2$, $c=1$, the new threshold $p^{*}_{\text{new}}= (2+1)/(2+1)=1.0$ and $\dot{x}= -1.2\,x(1-x)$, accelerating extinction of the falsifiable strategy sixfold.

These scenarios illustrate how modest policy adjustments can qualitatively reshape the evolutionary landscape.

## 5. Results
All quantities are derived directly from the arithmetic in Section 4.

| Quantity | Formula & inputs | Value | Interpretation |
|---|---|---|---|
| Accuracy threshold $p^{*}$ | $(s+c)/(b+c)$, $s=1$, $c=1$, $b=2$ | $0.6667$ | Predictions must succeed > 66.7 % to be rational. |
| Falsifiable payoff $\pi_F$ | $p b-(1-p)c$, $p=0.6$, $b=2$, $c=1$ | $0.8$ | Below narrative payoff. |
| Post‑hoc payoff $\pi_P$ | $s=1$ | $1.0$ | Dominates at baseline. |
| Replicator coefficient | $\pi_F-\pi_P$ | $-0.2$ | Drives $x\to0$; 10.99 generations to drop from $0.5$ to $0.1$. |
| Flip reward $b_{\text{flip}}$ | $(s+(1-p)c)/p$ | $2.3333$ | Minimum prediction reward to reverse equilibrium. |
| Sensitivities of $p^{*}$ | $\partial p^{*}/\partial b$, $\partial p^{*}/\partial c$, $\partial p^{*}/\partial s$ | $-0.2222$, $0.1111$, $0.3333$ | Narrative reward most destabilizing. |
| Strong reform ($b=10$) | $\pi_F$, $p^{*}$ | $5.6$, $0.1818$ | Falsifiable dominates by $4.6$. |
| Weak reform ($b=5$) | $\pi_F$, $p^{*}$ | $2.6$, $0.3333$ | Clears flip point. |
| Adverse reform ($s'=2$) | $\pi_F-\pi_P$ | $-1.2$ | Sixfold faster extinction of F. |

The central quantitative finding is that, under the baseline parameters, unfalsifiable narrative‑making is a strict ESS, and a modest increase of the confirmed‑prediction reward above $b\approx2.33$ suffices to make falsifiable practice the stable outcome.

## 6. Discussion
### 6.1 Limitations
- **A1. Payoff linearity.** Real reputational gains may be convex; a single breakthrough could outweigh many routine successes, altering the threshold.  
- **A2. Fixed accuracy.** Agents could invest to raise $p$; the model then becomes two‑dimensional.  
- **A3. Assumed parameters.** Values $b=2$, $c=1$, $s=1$, $p=0.6$ are illustrative; qualitative conclusions hold for any positive parameters, but numerical thresholds are context‑specific.  
- **A4. Binary strategies.** Hybrid approaches (partial predictions, incremental testing) are omitted; see [4] for evidence that richer strategy spaces can yield non‑trivial equilibria.  
- **A5. Well‑mixed population.** Network effects and citation cascades are ignored; they could generate multiple equilibria.  
- **A6. Origin of unfalsifiable strategies.** Like [7], the model explains persistence, not initial emergence, of post‑hoc narratives.  
- **A7. Strategy noise.** If agents randomize, the sharp threshold becomes a band, as formalized by belief‑based ESS in [5].

### 6.2 What would falsify the model
The model predicts that **increasing the effective prediction reward $b$ above the flip point raises the share of prospectively registered, falsifiable research**. A pilot study that raises $b$ while holding $s$ and $c$ approximately constant, and observes **no increase** (or a decrease) in the fraction of registered predictions, would falsify the central claim. Conversely, an observed increase is consistent but not sufficient proof, because confounding changes in $s$ or $c$ could produce the same effect.

### 6.3 Open questions
- How do citation‑network effects reshape the payoff structure and potentially generate multiple ESSs?  
- What is the impact of heterogeneous accuracies $p$ across sub‑fields on the global threshold?  
- Can a multi‑stage Stackelberg formulation (leader setting $(b,c,s)$, followers playing an ESS) be solved analytically, extending the work of [10]?  
- How does stochastic strategy adoption (as in [5]) smooth the threshold and affect policy efficacy?

## 7. Practical Implications and Engineering Pathways
### (a) Primary users and decision impact
The **primary users** are funding‑agency program officers, journal editors, tenure committees, and designers of AI‑assisted research pipelines. Under the baseline parameters, a researcher with $p=0.6$ rationally adopts the post‑hoc strategy because $\pi_P>\pi_F$. The result supplies a **computable policy lever**: raising the confirmed‑prediction reward $b$ above $b_{\text{flip}}\approx2.33$ (for $p=0.6$, $c=1$, $s=1$) makes the falsifiable strategy individually optimal and evolutionarily stable, without altering peer‑review criteria or researcher ability. Concretely, a funding program could allocate extra scoring weight to proposals that contain **pre‑registered predictions** with specified statistical power, thereby increasing the effective $b$.

### (b) Technology readiness level
The work is **purely analytical** and has not undergone peer review; it resides at **TRL 2** (formulation of basic principles). No hardware, software prototype, or experimental demonstration exists, and analytical work cannot exceed **TRL 3**.

### (c) Minimal next experiment
A **pilot policy experiment** within a single funding agency would test the model:

- **Design:** measure the baseline share $x_0$ of submissions containing prospectively registered predictions; introduce a scoring bonus calibrated to raise the effective $b$ above $2.33$; measure the post‑intervention share $x_1$ after a fixed number of funding cycles.  
- **Measurement:** proportion of registered predictions, any concurrent changes in narrative‑type rewards $s$, and observed prediction accuracy $p$ (to monitor confounds).  
- **Falsification condition:** if $x_1 \le x_0$ while $s$ remains stable, the model’s central prediction is falsified.

### (d) Binding constraints
- **Data infrastructure:** a reliable registry of predictions and outcomes is required before $b$ can be priced.  
- **Scoring algorithm:** the conversion from registry status to reward $b$ must be transparent and resistant to gaming.  
- **Policy alignment:** the bonus must not be offset by existing novelty or impact premiums that effectively raise $s$.  
- **Open questions:** the elasticity of researcher behavior with respect to $b$, and the cost of building and maintaining the registry, remain to be quantified.

### (e) Projected magnitudes (projections)
Assuming a modest software development cost of **$10^5$ monetary units** to implement a prediction registry (a typical small‑scale project) and a linear response of strategy share to the payoff gap (as in the replicator equation), raising $b$ by $\Delta b = 0.4$ (from $2$ to $2.4$) changes the payoff gap from $-0.2$ to $+0.2$, a swing of $0.4$ payoff units. The time‑to‑equilibrium formula in Section 4.4 suggests that, under the stronger positive gap, the falsifiable share would rise from $0.1$ to $0.5$ within roughly $10.99$ generations, offering a planning horizon for policy evaluation. These figures are **projections** based on the analytical model and the stated assumptions.

### (f) Risks and misuse
- **Gaming the registry:** researchers might label retrospective analyses as prospective to capture the higher $b$. Robust timestamping and independent verification are required.  
- **Equity effects:** institutions with superior experimental capacity could disproportionately benefit from a higher $b$, widening resource gaps. Mitigation could involve collaborative prediction consortia or tiered bonuses.  
- **Adverse reward shifts:** policies that increase narrative rewards $s$ (e.g., “story‑impact” prizes) unintentionally strengthen the post‑hoc equilibrium, as shown in the adverse reform scenario (Section 4.7). Any reform package must audit both $b$ and $s$ simultaneously.

## 8. Conclusion
We have formulated a minimal evolutionary‑game model of scientific strategy choice and derived its exact stability structure. Falsifiable practice is individually rational only when $p > p^{*}= (s+c)/(b+c)$; below this threshold the Post‑hoc strategy is a strict Nash equilibrium and therefore an evolutionarily stable strategy, with replicator dynamics driving falsifiable practice to extinction. Under the explicitly assumed parameters $b=2$, $c=1$, $s=1$, $p=0.6$, the threshold is $p^{*}=0.6667$, the payoff gap is $-0.2$, and the flip point is $b\approx2.3333$—a modest reward increase that reverses the equilibrium without altering reviewer judgment or researcher ability. The analysis converts the demarcation problem from a philosophical concern into a computable criterion: whether a knowledge system produces falsifiable science depends on its reward parameters, not on the intrinsic content of its claims. The central empirical prediction—that raising $b$ above the flip point increases the share of prospectively registered research—remains to be tested by the pilot experiment proposed in Section 7. Future work should incorporate network effects, heterogeneous accuracies, and multi‑stage decision processes, and should formalize the funder’s own optimization in the Stackelberg framework of [2].

## Version History

- Version 1.1.0 (2026-10-20, from 1.0.0): revised against the current literature, re-reviewed and re-verified. sections folded or removed: Extended Derivations and Worked Examples. references 11 -> 10. length 4342 -> 3428 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.3-reviser-thinking-off). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 20 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Evolutionarily Stable Spectrum Access. arXiv:1204.2376. https://arxiv.org/abs/1204.2376
[2] Evolutionarily Stable Stackelberg Equilibrium. arXiv:2603.18385. https://arxiv.org/abs/2603.18385
[3] Synthesising Evolutionarily Stable Normative Systems. arXiv:1710.00709. https://arxiv.org/abs/1710.00709
[4] Evolutionarily Stable Density-Dependent Dispersal. arXiv:1301.1426. https://arxiv.org/abs/1301.1426
[5] A belief-based evolutionarily stable strategy. arXiv:1406.0045. https://arxiv.org/abs/1406.0045
[6] Evolutionarily Stable Strategies in Quantum Games. arXiv:quant-ph/0007100. https://arxiv.org/abs/quant-ph/0007100
[7] Evolutionarily Stable (Mis)specifications: Theory and Applications. arXiv:2012.15007. https://arxiv.org/abs/2012.15007
[8] Computing Evolutionarily Stable Strategies in Multiplayer Games. arXiv:2511.20859. https://arxiv.org/abs/2511.20859
[9] Evolutionarily Stable Strategies in Quantum Hawk-Dove Game. arXiv:quant-ph/0108075. https://arxiv.org/abs/quant-ph/0108075
[10] Computational Complexity of Multi-Player Evolutionarily Stable Strategies. arXiv:2203.07407. https://arxiv.org/abs/2203.07407

## Appendix A. Divergence report
| Divergent Claim | Draft A Position | Draft B Position | Adopted Convention (used in main text) |
|---|---|---|---|
| Baseline narrative reward $s$ | $s=1$ (derived from weak‑lensing shear $\lesssim1\%$) | $s=0.5$ (assumed) | $s=1$ (as in Draft A) |
| Payoff for post‑hoc strategy $\pi_P$ | $\pi_P = s$ | $\pi_P = c + s$ | $\pi_P = s$ |
| Payoff for falsifiable strategy $\pi_F$ | $\pi_F = p\,b - (1-p)\,c$ | $\pi_F = p\,b + s$ | $\pi_F = p\,b - (1-p)\,c$ |
| Accuracy threshold formula | $p^{*} = (s+c)/(b+c)$ (derived from $\pi_F>\pi_P$) | $p^{*}=c/b$ (intermediate step) then rewritten as $(s+c)/(b+c)$ for symmetry | $p^{*} = (s+c)/(b+c)$ |
| Parameter $c$ (failure cost) | $c=1$ (unit 1 keV from XRISM and Lynx) | $c=1$ (same) | $c=1$ |
| Parameter $b$ (confirmed‑prediction reward) | $b=2$ (two SKA telescopes) | $b=2$ (same) | $b=2$ |
| Prediction accuracy $p$ used in illustration | $p=0.6$ (assumption) | $p=0.7$ (assumption) | $p=0.6$ |
| Flip point $b$ for $p=0.6$ | $b\approx2.33$ (solved from $\pi_F=\pi_P$) | $b\approx1.66$ (solved from $p\,b=c$) then rewritten as $(s+(1-p)c)/p$ | $b\approx2.33$ |
| Replicator dynamics sign | $\dot{x}= -0.2\,x\,(1-x)$ (negative) | $\dot{x}= +0.4\,x\,(1-x)$ (positive) | Negative sign as derived from Draft A’s payoffs |

All divergent claims have been resolved according to the conventions listed above and used consistently in the reconciled manuscript.

## Appendix B. Claim attribution
| Claim ID | Statement | Source drafts | Agreement status |
|---|---|---|---|
| C1 | Formulation of a two‑strategy evolutionary‑game model of scientific strategy choice. | A, B | CONVERGENT |
| C2 | Derivation of the rationality threshold $p^{*}= (s+c)/(b+c)$. | A, B | CONVERGENT |
| C3 | Numerical illustration: with $b=2$, $c=1$, $s=1$, $p=0.6$, we obtain $p^{*}=0.6667$, $\pi_F=0.8$, $\pi_P=1.0$, flip point $b\approx2.3333$, replicator coefficient $-0.2$. | A, B | CONVERGENT |
| C4 | Sensitivity of $p^{*}$ to $b$, $c$, $s$ (partial derivatives $-0.2222$, $0.1111$, $0.3333$) and of $b_{\text{flip}}$ to $s$, $c$ ( $1.6667$, $0.6667$ ). | A, B | CONVERGENT |
| C5 | Time to near‑extinction: $t\approx10.99$ generations for $x$ to fall from $0.5$ to $0.1$. | A, B | CONVERGENT |
| C6 | Flip point derivation $b_{\text{flip}} = (s+(1-p)c)/p \approx 2.3333$. | A, B | CONVERGENT |
| C7 | Reform scenarios (strong $b=10$, weak $b=5$, adverse $s'=2$) and their impact on payoffs and dynamics. | B only | SINGLE (retained as derived from the model) |
| C8 | Policy implication: raising $b$ above $2.33$ makes falsifiable practice evolutionarily stable. | A, B | CONVERGENT |
| C9 | Falsification criterion: a pilot that raises $b$ but observes no increase in registered predictions would refute the model. | B only (explicit) | SINGLE (retained as a logical extension) |
| C10 | Limitations list (payoff linearity, fixed accuracy, assumed parameters, binary strategies, well‑mixed population, origin of unfalsifiable strategies, strategy noise). | A, B | CONVERGENT |
| C11 | Identification of primary users (funding agencies, editors, tenure committees, AI pipelines). | A, B | CONVERGENT |
| C12 | Technology readiness level assessment (TRL 2). | A, B | CONVERGENT |
| C13 | Minimal next experiment description (pilot policy change, measurement of registered‑prediction share). | A, B | CONVERGENT |
| C14 | Engineering constraints (registry data, scoring algorithm, policy alignment, open questions). | A, B | CONVERGENT |
| C15 | Projected cost/performance bounds (software cost $10^5$, payoff gap change $0.4$, equilibrium time $\approx5$ generations). | A, B | CONVERGENT |
| C16 | Risks and misuse (gaming, equity, adverse reward shifts). | A, B | CONVERGENT |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2209.00495v1 | Searching for Structure in Unfalsifiable Claims
arXiv:1211.0310v1 | Large Synoptic Survey Telescope: Dark Energy Science Collaboration
arXiv:2512.16152v1 | Pulsar Science with the SKA Observatory
arXiv:1403.5107v3 | Social and Natural Sciences Differ in Their Research Strategies, Adapted to Work for Different Knowledge Landscapes
arXiv:2304.08104v2 | GREX-PLUS Science Book
arXiv:2003.04962v1 | Science with the X-ray Imaging and Spectroscopy Mission (XRISM)
arXiv:2501.13682v1 | Collective Memory and Narrative Cohesion: A Computational Study of Palestinian Refugee Oral Histories in Lebanon
arXiv:2609.00033v1 | Lynx2030 Science Analysis Group: Final Report

## QNFO corpus context (Vectorize)

QNFO: The Ultrametric Foundation: A Unified Thesis on Number, Time, Knowledge, and Computation | https://papers.qnfo.org/papers/the-ultrametric-foundation-a-unified-thesis-on-number-time-knowledge-and-computa
QNFO: Institutionalized Predictive Jeopardy: An Evolutionary-Game Demarcation Criterion for Knowledge Systems | https://papers.qnfo.org/papers/institutionalized-predictive-jeopardy-an-evolutionary-game-demarcation-criterion
QNFO: The Vast World of Quantum Advantage — A Full-Spectrum Audit | https://papers.qnfo.org/papers/huang-2025-quantum-advantage-audit
QNFO: Algorithmic-Necessity-of-Agency | https://papers.qnfo.org/papers/algorithmic-necessity-of-agency

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2209.00495v1 | Searching for Structure in Unfalsifiable Claims
  Social media platforms give rise to an abundance of posts and comments on every topic imaginable. Many of these posts express opinions on various aspects of society, but their unfalsifiable nature makes them ill-suited to fact-checking pipelines. In this work, we aim to distill such posts into a small set of narratives that capture the essential claims related to a given topic. Understanding and v
  Full text (https://arxiv.org/html/2209.00495v1), excerpts of its own sections:
  § Evaluation Metrics: We use similar metrics as van der Maaten and Weinberger (2012) to measure the quality of the learned embedding. The Triplet Generalization Ratio ( TGR ) describes the fraction of ground truth triplets that are not violated by the learned embedding. Given the number of possible triplet combinations are very large we instead sample a subset of 1000 possible ground truth triplets for this metric. The K Nearest Neighbour Generalization Ratio ( KNNGR ) captures how well local structure is preserved. Since the number of local clusters is unknown after training, we sample 70% of the data and train a KNN on it and measure how many of the last 30% fall into the correct clusters to get a measure of locality. The Signal-to-Noise Ratio Distance ( SNR ) ( Yuan et al. 2019 ) measures the similarity of comment embeddings. Similarly, we compute statistics about the triplets gathered from the workers and the ground-truth annotation of the comments through three metrics: Triplet agreement , precision , recall , weighted precision , weighted recall . [...]
  § Results from playback simulation: Across our synthetic experiments, we found three key ingredients to obtain embeddings of higher quality. Firstly, we found that using a modern sentence transformer, such as the 3B parameter T5 model ( Raffel et al. 2020 ) , was crucial for initially embedding the sentences in papyer , before running SNaCK. Table 2 compares embeddings with different networks. We found that a T5-3B Transformer gave the best embedding by measuring the triplet generalization loss. T5-3B performs better than T5-11B, despite being trained on the same data. A similar observation can be made in other benchmarks ( Tensorflow Hub 2022 ) on which this model has been evaluated, indicating that size alone may be insufficient to determine the best embedding network. Secondly, the sampling strategy to gather the triplets used in SNaCK is important. Table 3 shows SNaCK with different sampling techniques. We found that Distance-Rnd worked best, since it has a good compromise between exploiting the text similarities and exploring the solution space. [...]
  § Experiments: Baselines. We compare the SNaCK embeddings with several popular unsupervised topic models, namely LDA  ( Blei, Ng, and Jordan 2003 ) , methods using pre-trained embeddings networks  ( Sia, Dalmia, and Mielke 2020 ; Thompson and Mimno 2020 ) , such as BERT and T5, and a mixture of these inspired from ( Steve Shao 2022 ) . For LDA and mixed models, we follow the standard protocol  ( Sia, Dalmia, and Mielke 2020 ) and tokenize the text using NLTK  ( Bird, Klein, and Loper 2009 ) , lowercase the tokens, remove stopwords, punctuation, digits, and URLs, and transform words into their stem versions and fix typos. We then convert these tokenized sentences into a document-term matrix to be used for LDA with $32$ topics. To visualize in 2D, we run t -SNE on top of the document-term matrix. Recent work on topic models  ( Sia, Dalmia, and Mielke 2020 ) suggests that traditional topic models can be replaced with clustering of 2D projections of deep sentence embeddings. [...]
  § Results: (a) t -SNE T5 (b) t -SNE BERT (c) UMAP BERT (d) UMAP T5 (e) LDA (f) t -SNE BERT + LDA (g) t -SNE T5 + LDA (h) SNaCK T5 Figure 8: 2D visualizations using different encoders and embedding projections. Sentences are coloured according to the crystallised narrative they belong to using the colors from Figure 3 . Despite showing more local structure in Figure e-g the quality of the embedding is lower as shown in Table 5 . [...]
[2] arXiv:1211.0310v1 | Large Synoptic Survey Telescope: Dark Energy Science Collaboration
  This white paper describes the LSST Dark Energy Science Collaboration (DESC), whose goal is the study of dark energy and related topics in fundamental physics with data from the Large Synoptic Survey Telescope (LSST). It provides an overview of dark energy science and describes the current and anticipated state of the field. It makes the case for the DESC by laying out a robust analytical framewor
  Full text (https://arxiv.org/html/1211.0310v1), excerpts of its own sections:
  § 1 Introduction and overview: The Large Synoptic Survey Telescope (LSST) is a wide-field, ground-based telescope, designed to image a substantial fraction of the sky in six optical bands every few nights. It is planned to operate for a decade allowing the stacked images to detect galaxies to redshifts well beyond unity. The LSST and the survey are designed to meet the requirements ( Ivezić & the LSST Science Collaboration 2011 ) of a broad range of science goals in astronomy, astrophysics and cosmology, including the study of dark energy – the accelerating expansion of the Universe. [...]
  § 4 Overview of dark energy science: Observations reveal that the expansion of the Universe is accelerating, a result that poses a direct challenge to current theories of cosmology and fundamental physics. The 2011 Nobel Prize in Physics was awarded for the 1998 discovery of the accelerating Universe using distance measurements of Type Ia supernovae (SNe). In the thirteen years since that discovery, astronomical observations ranging from the cosmic microwave background (CMB) to the spatial distribution of galaxies have validated and refined what we know about the expansion history of the Universe. Acceleration represents a serious dilemma for fundamental physics. The most prosaic explanation is that vacuum energy, which constitutes about three quarters of the energy density in the Universe, is driving the acceleration; however, naive predictions based on the Planck scale would predict vacuum energy densities roughly 100 orders of magnitude larger than observed, implying that some unknown physics suppresses such predicted vacuum energy, but leaves a very small residual that is driving the current expansion rate. [...]
  § 1 Overview: Gravitational lensing ( Schneider 2006 ; Bartelmann 2010 ) , the deflection of light from distant “sources” due to the bending of space-time by masses (“lenses”) along the line of sight, is a useful cosmological probe because it is sensitive to all matter, whether baryonic or dark. Weak lensing (WL) is gravitational lensing in the limit that the deflections are very small, causing tiny distortions, or “shear”, in galaxy shapes ( Bartelmann & Schneider 2001 ; Refregier 2003 ) . In the absence of lensing, galaxy orientations are assumed to be random, so they should not exhibit statistically significant, coherent alignments. Lensing induces small ( $\lesssim 1$ %) but coherent shears ( $\gamma$ ), in background galaxy images, which have typical ellipticities that are far larger (RMS ellipticity $\sim 0.36$ ). Thus, WL is detected statistically by averaging over many lensed galaxies, for which shapes have been measured in a way that eliminates contributions from observational effects that also distort galaxy shapes (e.g., the point-spread function, or PSF). [...]
  § 1 Overview: Measurements of galaxy clustering constrain the cosmic expansion history, the cosmological distance scale, the growth rate of structure, the mass of the neutrinos and the abundance of dark matter. Baryon acoustic oscillations (BAO) in the early Universe imprint a standard ruler in the power-spectrum (or the two-point correlation function), which measures the angular-diameter distance and the Hubble parameter. BAO is a special case of using the full shape of galaxy clustering data to constrain cosmological models. The BAO feature has now been observed in the SDSS, 2dF, and BOSS surveys, using both spectroscopic ( Eisenstein et al. 2005a ; Anderson et al. 2012 ; Xu et al. 2012 , e.g.,) and photometrically selected galaxy samples ( Padmanabhan et al. [...]
[3] arXiv:2512.16152v1 | Pulsar Science with the SKA Observatory
  The large instantaneous sensitivity, a wide frequency coverage and flexible observation modes with large number of beams in the sky are the main features of the SKA observatory's two telescopes, the SKA-Low and the SKA-Mid, which are located on two different continents. Owing to these capabilities, the SKAO telescopes are going to be a game-changer for radio astronomy in general and pulsar astrono
  Full text (https://arxiv.org/html/2512.16152v1), excerpts of its own sections:
  § 1 Introduction: The SKA Observatory (SKAO) is going to be a game-changer for radio astronomy in the coming decade. The construction of this unique instrument, comprising of two telescopes in two different continents, has already commenced with the phase 1 of these telescopes providing an unprecedented seamless frequency coverage from 50 MHz to 15 GHz with unmatched sensitivities in highly flexible interferometric configurations. Therefore, the SKAO is expected to enable a range of diverse astronomical investigations with significant impact on fundamental aspects of astrophysics. One such area of radio astronomy, where the SKAO is expected to make fundamental discoveries, is pulsar astronomy. Historically, new instruments have accelerated the pace of progress in pulsar astronomy (Figure 1 ) and the SKAO telescopes are likely to drive significant progress in this field in the next decade. The phase 1 of the rollout of the SKAO telescope, called AA4 (Array Assembly 4), is likely to double the known pulsar population in new surveys ( Keane et al., 2025 ; Abbate et al., 2025 ; Bagchi et al., 2025 ) . [...]
  § 2 The SKAO telescopes and pulsar observations: The SKAO telescopes are conceived as two telescopes geographically stationed on different continents and with different designs. The SKA-Low telescope is located in Australia, whereas the SKA-Mid is coming up in South Africa. Together, the two telescopes cover an observing frequency range of 50 MHz to 15 GHz. The two telescopes will be commissioned and operated by an inter-governmental organisation bringing together more than 13 nations from around the world in a unique collaborative international effort. The construction plan of the SKAO telescopes is envisaged as a staged delivery of evolving array assembly (AA). The earliest milestone, AA*, is likely be delivered between 2029 to 2031, and the design baseline AA4 will follow depending on funding 1 1 1 Please refer to https://www.skao.int/en/science-users/599/scientific-timeline for details. . [...]
  § 3 State of the art and expected SKAO discoveries: There have been significant advances in pulsar astronomy since the pulsar science case for the SKAO was drafted two decades ago, particularly since its update a decade back ( Kramer and Stappers, 2015 ) . The gravitational waves at high frequencies have been detected from more than 200 sources and the pulsar timing arrays are close to a significant detection of nano-Hertz gravitational waves opening up a messenger that the SKAO telescope can explore in earnest. More exotic binary systems have been discovered and mass and radius for several NS are measured to a good precision motivating investigations in fundamental physics using pulsars as probes. The large instantaneous sensitivity and flexibility of the SKAO telescope will make a significant impact on the pulsar science case with doubling the pulsar population in a pulsar survey, which forms the basis for fundamental physics studies interconnected with other areas of pulsar astronomy as illustrated in Figure 2 . [...]
  § Summary: Together, these studies define the pulsar and neutron-star science programme for the SKA Observatory. The AA* arrays will provide an immediate leap in discovery power and precision, while the full AA4 configurations of SKA-Low and SKA-Mid will deliver transformative, population-level insights into neutron-star physics, plasma astrophysics, Galactic structure, and gravitation.
[4] arXiv:1403.5107v3 | Social and Natural Sciences Differ in Their Research Strategies, Adapted to Work for Different Knowledge Landscapes
  Do different fields of knowledge require different research strategies? A numerical model exploring different virtual knowledge landscapes, revealed two diverging optimal search strategies. Trend following is maximized when the popularity of new discoveries determine the number of individuals researching it. This strategy works best when many researchers explore few large areas of knowledge. In co
  Full text (https://ar5iv.labs.arxiv.org/html/1403.5107v3), excerpts of its own sections:
  § Submission history: From: Klaus Jaffe Dr [ view email ] [v1] Thu, 20 Mar 2014 11:57:13 UTC (458 KB) [v2] Thu, 16 Oct 2014 19:49:32 UTC (422 KB) [v3] Sat, 4 Apr 2015 14:01:28 UTC (124 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Social and Natural Sciences Differ in Their Research Strategies, Adapted to Work for Different Knowledge Landscapes, by Klaus Jaffe View PDF view license
  § Current browse context:: physics.soc-ph < prev | next > new | recent | 2014-03 Change to browse by: cs cs.DL physics
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[5] arXiv:2304.08104v2 | GREX-PLUS Science Book
  GREX-PLUS (Galaxy Reionization EXplorer and PLanetary Universe Spectrometer) is a mission candidate for a JAXA's strategic L-class mission to be launched in the 2030s. Its primary sciences are two-fold: galaxy formation and evolution and planetary system formation and evolution. The GREX-PLUS spacecraft will carry a 1.2 m primary mirror aperture telescope cooled down to 50 K. The two science instr
  Full text (https://arxiv.org/html/2304.08104v2), excerpts of its own sections:
  § 2.2.2 Required observations and expected results: We consider three surveys aiming to find galaxies in the early universe at $z>15$ (Fig.  2.11 ; Table  2.1 ) by extrapolating the observed UV luminosity functions of galaxies from $z=10$ . First, due to Ly $\alpha$ scattering by the neutral hydrogen in the intergalactic medium, photons from galaxies at $z>15$ will not be detected below the the observed wavelength of 2 $\mu$ m (Ly $\alpha$ break, or Gunn-Peterson Trough; Gunn & Peterson 1965). Therefore, a wavelength of 2 $\mu$ m or longer is required to observe galaxies at $z>15$ . In addition, in order to distinguish between Ly $\alpha$ break of $z>15$ galaxies and red colors of low redshift galaxies (e.g., passive galaxies and/or dusty galaxies), two or more photometry points are required at the rest-frame wavelengths of $0.15-0.3$ $\mu$ m, longer than the wavelength of the Ly $\alpha$ break. GREX-PLUS is primarily designed to detect galaxies, not to spatially resolve them. [...]
  § 2.3.2 Required observations and expected results: Figure  2.12 shows the limiting stellar mass as a function of redshift that can be detected at 5 $\sigma$ with GREX-PLUS. In order to detect building blocks of galaxies with 10 9 M ⊙ /yr back to $z\sim 8$ , we must reach down to 27 AB magnitudes, well matched to our planned observations. By combining with Subaru/HSC optical imaging data, we can cover the wavelength range of 0.4–5 (and up to 8 for bright galaxies) $\mu$ m, and thus can measure stellar masses precisely from the spectral energy distribution (SED) of galaxies. We can also conduct a statistical number count of close neighbour galaxies utilizing the relatively high spatial resolution of GREX-PLUS in order to investigate the relative contribution of galaxy mergers to the mass assembly history. The required spatial resolution for this purpose is 8 kpc or 1 arcsec so that we can resolve neighbouring galaxies beyond the cosmic noon epoch ( $z>2$ ). We aim to construct a large statistical sample of galaxies across the cosmic age and environment with a large area survey. [...]
  § 2.4.2 Required observations and expected results: Here, we investigate the observational strategy to discover pair-instability supernovae and superluminous supernovae at $z>7$ . First, we estimate their brightness around $2~\mathrm{\mu m}$ (F232 band) and around $4~\mathrm{\mu m}$ (F397 band) by taking pair-instability supernova models by Kasen et al. (2011) and superluminous supernova templates by Moriya et al. (2022) . In order to discover supernovae at $z>7$ , it is required to reach at least 26 AB mag (Fig.  2.13 ). The two-band survey allows us to distinguish high-redshift supernovae and low-redshift supernovae even with a single epoch observation (Fig.  2.13 ). Such a distinction would be important to efficiently discover rare high-redshift supernovae. It also implies that we do not need to rely only on light curves to discover them and high-cadence observations are not necessarily required. Based on the estimated light-curve properties, we conducted supernova survey simulations to estimate the expected numbers of high-redshift supernova discoveries by GREX-PLUS. We assume two-band surveys with the F232 and F397 bands. [...]
  § 2.5.2 Required observations and expected results: We aim detecting spatial fluctuations in the CIB beyond the degree scale, where the effects of zodiacal light, the Galactic radiation, and emission from foreground galaxies are considered to be small. For this purpose, it is necessary to observe a region of several tens of square degrees or more. [...]
[6] arXiv:2003.04962v1 | Science with the X-ray Imaging and Spectroscopy Mission (XRISM)
  This white paper was prepared by members of the XRISM Science Team for the benefit of the general astronomical community. This paper describes the capabilities of XRISM, offers a sampling of the many science topics that the mission will address, and discusses the synergies of XRISM with the plethora of planned and existing facilities in the 2020s and beyond.
  Full text (https://arxiv.org/html/2003.04962v1), excerpts of its own sections:
  § 1 Introduction: The X-ray Imaging and Spectroscopy Mission (XRISM) , formerly known as the X-ray Astronomy Recovery Mission (XARM) , is a JAXA-NASA collaborative mission with ESA participation. XRISM will offer non-dispersive, high-resolution X-ray spectroscopy in the soft X-ray bandpass ( $\sim 0.3-12$ keV), while offering complementary CCD imaging resolution over a wide field of view. The primary purpose of the mission is to recover the science that was lost after the Astro-H/Hitomi mission failed in 2016, approximately one month after launch. Four science categories have been defined for XRISM : (1) Structure formation of the Universe and evolution of clusters of galaxies; (2) Circulation history of baryonic matter in the Universe; (3) Transport and circulation of energy in the Universe; (4) New science with unprecedented high-resolution X-ray spectroscopy. A full description of the mission is provided in an SPIE proceeding 1 ; the reader is referred there for more detail. [...]
  § 2 GALAXY AND CLUSTER EVOLUTION: (Primary editors: Irina Zhuravleva, Erin Kara, Chris Done) One of the biggest questions in modern astrophysics and cosmology is how the largest structures in the Universe form and evolve with time. As a result of enormous efforts in observational and theoretical astrophysics, we now understand what processes are playing an important role in the evolution of galaxies, groups, and clusters. [...]
  § 7.4 Following Extreme Transients in Time Domain Surveys: X-ray observations have played a major role in time domain astronomy: from the discovery of new galactic black holes, giant stellar flares, tidal disruption events (TDEs), and flares from Sgr A*, to the existence of super-Eddington accretors, the discovery of magnetars, and millisecond X-ray pulsars. Time domain astronomy is a quickly advancing field. Even in the next few years, we will see major increases in the rate of transient discovery. In the optical, ZTF and LSST will discover thousands of transients per night. In the radio, SKA will find tens of transients per night. In X-rays, the eROSITA all-sky survey will provide a 30-fold improvement in sensitivity, discovering faint transients, and producing a baseline against which we will compare future observations. Finally, the Chinese Academy of Science’s Einstein Probe (to launch in late 2022) will use “lobster-eye” optics to make a vast improvement in sensitivity for X-ray transient searches. [...]
  § 7.8 Conclusion: The importance of high-resolution X-ray spectroscopy to the future of astronomy in general cannot be overstated. Despite the fact that Hitomi only operated for a matter of weeks in 2016, the results from that spacecraft are among the most highly-cited papers in the field of high-energy astronomy in the past several years. By recovering the science lost by the untimely demise of Hitomi , XRISM will continue its legacy into the next decade, paving the way for future X-ray missions, such as Athena , which will be equipped with even greater capabilities. The checkout, calibration, and performance verification phases will last approximately nine months, after which XRISM will enter the general observer phase. Astronomers around the world will be able to propose to an annual announcement of opportunity for competitively-awarded time on the observatory. The science that is briefly outlined in this white paper is only the beginning of what will be possible given the capabilities that this observatory will provide.
[7] arXiv:2501.13682v1 | Collective Memory and Narrative Cohesion: A Computational Study of Palestinian Refugee Oral Histories in Lebanon
  This study uses the Palestinian Oral History Archive (POHA) to investigate how Palestinian refugee groups in Lebanon sustain a cohesive collective memory of the Nakba through shared narratives. Grounded in Halbwachs' theory of group memory, we employ statistical analysis of pairwise similarity of narratives, focusing on the influence of shared gender and location. We use textual representation and
  Full text (https://arxiv.org/html/2501.13682v1), excerpts of its own sections:
  § 1 Introduction: The Nakba, a pivotal moment in Palestinian history marked by the mass displacement of approximately 770,000 Palestinians during the forcible establishment of Israel Bisharat (1994) ; Khalidi (1992) ; Abū-Sitta (2016) ; Khoury (2012) ; Khalidi (1997) ; Masalha (2012) , embodies a broader colonial project to establish an ethnocratic state Khoury (2012) ; Pappé (2007) ; Benvenisti et al. (2007) ; Masalha (2012) . The memory of the Nakba and the immense suffering caused by forced displacement, loss of land, and erasure of the Palestinian presence remains central to the national consciousness of Palestinians ( Allan, 2013 ; Sa’di and Abu-Lughod, 2007 ; Jayyusi, 2007 ; Khalidi, 1997 ) . Among Palestinians, refugees in Lebanon are exemplary in their resilience and their maintainance of a collective identity despite being intensely marginalized and disadvantaged. Denied basic rights under Lebanese law, they experience profound spatial, institutional, and economic exclusion Siklawi (2019) ; Rmeileh (2021) . [...]
  § 5 Findings: Using the models outlined, we test cohesion for both gender and location along a set of different aspects. As discussed in Section 3 , we hypothesize that narrative cohesion will be higher 1) within same-gender pairs and 2) within same-community pairs (place of origin and place of residence). We refer to analyses of BOW representations of metadata and extracted named entities as relating to “factual” aspects of the interviews and the analyses using embeddings of different interview sections as “thematic.”
  § 6 Discussion: We observe evidence of group memory in several different scenarios concerning boundary-making identity markers. When interviewees share a community space (same origin or same residence), there is higher similarity within their narratives. Critically, sharing both same origin and residence often results in an even stronger similarity in interviewees’ narratives. This indicates that the cohesiveness of narratives depends on the continuity of the group, which, in turn, depends on the continuity of shared space. As well, we observe weaker evidence that gender is an indicator of similarity, though women’s narratives tend to be more similar. The cohesion of narratives based on location can be reasonably explained through the theoretical framework of group memory. Refugees sharing same origin but not the same residence still have cohesive narratives, demonstrating that group members’ bond to other members of their original village are not severed in exile. [...]
  § 7 Conclusion: This paper constitutes a large-scale computational analysis of an oral history archive of the Nakba using natural language processing. Drawing from qualitative literature on Palestinian refugees’ experiences, we explore how boundary-making identity markers shape their life narratives. Comparing the narratives of Palestinians beyond Lebanon or the narratives of those from rural vs. urban contexts are opportunities for further research into how locality shapes narrative cohesion. This study, however, is bound by the scope of POHA which focuses solely on Lebanon and offers a preliminary foray into one means of capturing multidimensional narrative cohesion in an archive. With these findings, we hope to both reaffirm and extend prior scholarship on Palestinian collective memory, by providing empirical evidence of how oral narratives allow refugees to build continuity and counteract the violent fragmentation of Palestinian society after the Nakba.
[8] arXiv:2609.00033v1 | Lynx2030 Science Analysis Group: Final Report
  The Lynx2030 Science Analysis Group (SAG) was convened to reassess the scientific goals and technical drivers of the Lynx mission concept amid a rapidly evolving astrophysics landscape. Building on the original Lynx Concept Study, the SAG examined how recent discoveries, emerging facilities, and advances in instrumentation influence the scientific opportunities for a next-generation flagship X-ray
  Full text (https://arxiv.org/html/2609.00033v1), excerpts of its own sections:
  § Executive Summary: The Lynx X-ray Observatory concept presented to the Astro2020 Decadal Survey [ 210 ] defined a flagship-class, soft X-ray telescope built around three scientific pillars: black hole seeds at cosmic dawn, the drivers of galaxy evolution, and the energetic side of stellar evolution. To achieve these goals, such a mission requires a PSF comparable to that of Chandra , coupled with $\sim 100\times$ its effective area and a larger field of view (FoV). Pursuit of the science goals associated with these pillars was enabled by a subarcsecond-class optic with $\sim 2\,\rm m^{2}$ of effective area at $1$ keV, a high-density imaging detector, an ultra-high-resolution microcalorimeter array, and a dispersive grating spectrometer. The High-Definition X-ray Imager (HDXI) included an array of 0.3 ′′ pixels with a $22^{\prime}\times 22^{\prime}$ FoV; the Lynx X-ray Microcalorimeter (LXM) was designed with a main array of $5^{\prime}\times 5^{\prime}$ FoV (1 ′′ pixels) and an inner enhanced main array of $1^{\prime}\times 1^{\prime}$ (0.5 ′′ pixels). [...]
  § List of Acronyms: Acronym Definition ADD Advancement Degree of Difficulty ADR Adiabatic Demagnetization Refrigerator ASIC Application-Specific Integrated Circuit AXIS Advanced X-ray Imaging Satellite CAT Critical-Angle Transmission (gratings) [...]
  § 4.1. Introduction and Motivation: Following the recommendations of the Astro2020 Decadal Survey and navigating the shifted astrophysics landscape of the mid-2020s, it is timely to revisit the Lynx reference design to identify the transformative science that can be unlocked by incorporating mature, next-generation detector technologies. Recent discoveries from IXPE, XRISM, and JWST have underscored the necessity of capabilities such as high-resolution X-ray polarimetry and rapid-readout timing, while reaffirming the centrality of the optic and the microcalorimeter that anchored the original concept. The motivation has a distinctly post-JWST character. [...]
  § 4.3.3. Wider-Field and Time-Domain Detector Concepts: Detectors that achieve even wider fields of view at full angular resolution while still resolving key X-ray transitions are of interest for wide-field targets, expanded survey science, and time-domain and multi-messenger (TDAMM) astrophysics. Microcalorimeters, while highly compelling, entail trade-offs among complexity, pixel size, field of view, and count-rate limits, so complementary detector technologies—some currently at lower TRL for spaceflight—may offer interesting trade-offs in energy resolution, to be weighed against added cost and architectural complexity.
  § 4.5. Synthesis and Outlook: The net assessment is encouraging. The two technologies that most distinguished Lynx from its predecessors—the arcsecond, square-meter optic and the >100,000-pixel microcalorimeter—have both advanced materially since 2020. The microcalorimeter has, in effect, been flight-validated (XRISM) and scaled (LEM), and is under development towards TRL 5 with a credible manufacturing path. The CAT gratings have exceeded their Lynx requirement in the laboratory and are no longer the limiting spectroscopic element. The optic remains the pacing item: silicon meta-shell segments individually meet requirements, and AXIS/STAR-X have demonstrated module-level performance, but integrating thousands of segments to flagship scale—and the tightening required to support $R\approx 10,000$ grating spectroscopy—remains the central technical and programmatic risk. At the same time, the science and technology landscape has handed Lynx new opportunities. [...]
[9] QNFO: The Ultrametric Foundation: A Unified Thesis on Number, Time, Knowledge, and Computation | https://papers.qnfo.org/papers/the-ultrametric-foundation-a-unified-thesis-on-number-time-knowledge-and-computa
  Positional notation is inherently an ultrametric tree of nested cycles. The Archimedean line is a derived abstraction. Recovering the native ultrametric resolves cascading errors across mathematics, physics, epistemology, education, quantum computing, and interface design.
  Full text (https://papers.qnfo.org/papers/the-ultrametric-foundation-a-unified-thesis-on-number-time-knowledge-and-computa), excerpts of its own sections:
  § A Unified Thesis on Number, Time, Knowledge, and Computation: **Author:** QNFO **Date:** 2026-06-27 **Version:** 1.0-draft **License:** QNFO Unified License Agreement (QNFO-ULA): https://legal.qnfo.org/ ---
  § Author's Note `[my conjecture — the synthesis is my own; individual component claims carry their own certainty labels]`: This thesis synthesizes a 67-minute intellectual progression recorded across 21 sequential notes on June 27, 2026. It begins with a deceptively simple observation about the numeral "10" and traces its implications through mathematics, physics, epistemology, education, quantum computing, and interface design, revealing a single unifying structure: **the ultrametric tree that underlies all quantitative representation was systematically flattened into an Archimedean line, and recovering it resolves a cascade of otherwise disconnected errors across every domain of human knowledge** `[my conjecture — this is the central synthetic claim this document argues for]`.
  § Certainty Calibration Conventions: Throughout this thesis, every claim beyond textbook consensus carries an explicit certainty label: | Label | Meaning | |:------|:--------| | `[established]` | Supported by multiple independent experiments or peer-reviewed proofs; no serious dispute | | `[mainstream interpretation]` | Most widely held view among specialists, though not directly proven | | `[speculative]` | Theoretical motivation exists, but no direct experimental support | | `[my conjecture]` | The author's own idea — not yet subjected to independent peer review | | `[debated]` | Active disagreement among specialists; no clear consensus | | `[not yet falsifiable]` | Cannot currently state what experimental result would disprove this | | `[LLM-INFERRED]` | Derived from the model's reasoning or training data; not independently verified | ---
  § 1.1 The Primal Observation: In any integer base $b \geq 2$, the digit string "10" denotes the number $b$. This holds universally: binary "10" = two, decimal "10" = ten, sexagesimal "10" = sixty. Therefore every base, when named using its own numeral system, calls itself "base‑10." This is not a joke. It is a concrete demonstration that **a numeral string cannot internally specify its own rule of interpretation.** The radix is always a silent parameter, supplied by an external meta‑language — a human convention, a hardware specification, a cultural default. The efficiency of positional notation is purchased at the permanent cost of latent ambiguity. The crack this opens is the fault line running through all formal symbolism: - Any numeral string is radically underdetermined without context. - The base cannot be named from within — an echo of Gödelian incompleteness and the use/mention boundary. [...]
  § 1.2 The Silent Partner: The Silent Metric: The radix is not alone in its silence. The equal‑interval assumption is the second great hidden parameter. Integers possess a natural order (the successor function) but no intrinsic distance. The picture of equally spaced points on a straight line is a geometric import from Descartes and analytic geometry — an epistemological tool reified into an ontological property. [...]
  § 12.5 Falsification Experiment: A minimal experiment: build a depth‑2 tree (8 qubits) of transmon qubits connected via coaxial cavities enforcing tree‑only gates. Compare logical error rate against a 2D nearest‑neighbour layout with identical qubit parameters. The central claim is falsified if the tree geometry does not yield a statistically significant improvement in logical error rate. ---
[10] QNFO: Institutionalized Predictive Jeopardy: An Evolutionary-Game Demarcation Criterion for Knowledge Systems | https://papers.qnfo.org/papers/institutionalized-predictive-jeopardy-an-evolutionary-game-demarcation-criterion
  Institutional knowledge systems — peer review, tenure committees, funding panels, citation markets — must decide which claims deserve resources, yet they possess no formal criterion distinguishing claims that carry prospective falsification risk from claims fitted to evidence after the fact. Incentive structures that cannot price predictive risk plausibly reward post-hoc certainty, allowing unfals
  Full text (https://papers.qnfo.org/papers/institutionalized-predictive-jeopardy-an-evolutionary-game-demarcation-criterion), excerpts of its own sections:
  § 5. Results: All numbers below are computed in Section 4 from the stated assumptions; none are empirical measurements. R1. Accuracy threshold (Section 4.2). Falsifiable practice is individually rational exactly when $p > p^{*} = (s+c)/(b+c)$. R2. Baseline dominance of post-hoc fitting (Section 4.3). With $b=2$, $c=1$, $s=1$, $p=0.6$: $\pi_F = 0.8$, $\pi_P = 1.0$, $p^{*} = 2/3 \approx 0.6667$, and $\dot{x} = -0.2\,x(1-x)$, so $F$ is driven out. R3. Reform reversal (Section 4.4). With $b=10$, $c=1$, $s=1$, $p=0.6$: $\pi_F = 5.6$, $\pi_P = 1.0$, $p^{*} = 2/11 \approx 0.1818$. With the weaker reform $b=5$: $\pi_F = 2.6$, $p^{*} = 1/3 \approx 0.3333$. The best-response flip occurs at $b \approx 2.3333$. R4. Antifragility (Section 4.5). $R(k) = R(0) + k/N$ with $dR/dk = 1/N > 0$ when failures are registered and removed. For $N=1000$, $U=400$: $R(0)=0.60$, $R(100)=0.70$. R5. Reform timescale (Section 4.6). With $x_0=0.1$ and diluted $\Delta=0.2$: $t = \ln 9/0.2 \approx 10.99$ generations to majority. With undiluted $\Delta=4.6$: $t \approx 0.4777$ generations. R6. Structural results (Section 4.7). [...]
  § 6. Discussion: The model's central claim is that demarcation is a property of incentive configurations, not of claim content: the same agent with the same accuracy $p$ produces falsifiable or unfalsifiable science depending on $b$, $c$, and $s$. This claim is supported here only formally. Its empirical content — that real institutions occupy the $P$-dominant region of parameter space, and that reforms move them to the $F$-dominant region — rests on the comparative case analysis we could only propose, not perform. Limitations, explicitly: - Payoff additivity (A1). Real reputations are nonlinear in track record; a single celebrated confirmation may be worth many routine ones. If payoffs are convex in streaks, the threshold $p^{*}$ shifts and the clean comparative statics weaken. - Strategy-independence of accuracy (A2). If agents can invest to raise $p$, the game becomes a two-dimensional choice and the threshold analysis describes only the margin of investment, not the level. - Normalization (A3). [...]
  § 7.1 Who would use the result, and what changes: The primary users are the operators of resource-allocation mechanisms in knowledge production: funding agency program officers, journal editors, tenure committees, and the designers of AI-assisted research pipelines. If the result holds, the decision that changes is the scoring rule applied to incoming claims. Under the baseline configuration derived in Section 4.3, a program officer who cannot distinguish prospective registration from retrospective fitting faces a system in which a $p = 0.6$ forecaster rationally submits post-hoc narratives ($\pi_P = 1.0$ versus $\pi_F = 0.8$); the officer's review process therefore selects for narratives rather than for predictions. The result supplies the officer with a computable lever: raising the confirmed-prediction reward $b$ above the flip point $b \approx 2.3333$ (for a $p = 0.6$ population under $c = 1$, $s = 1$) changes the individually rational strategy without requiring any change in reviewer judgment or researcher ability. [...]
  § 8. Conclusion: This paper set out to convert the demarcation problem from a matter of informal institutional judgment into a computable criterion. The core derivation is short enough to state in one line: falsifiable practice is individually rational exactly when $p > p^{*} = (s+c)/(b+c)$, so whether a knowledge system produces falsifiable science is a function of its reward parameters, not of the metaphysical content [...]
[11] QNFO: The Vast World of Quantum Advantage — A Full-Spectrum Audit | https://papers.qnfo.org/papers/huang-2025-quantum-advantage-audit
  Full-spectrum audit of Huang, Choi, McClean & Preskill (2025) "The vast world of quantum advantage" (arXiv:2508.05720). Subjects both the Huang et al. five-keystone framework and QNFO's own prior critiques to symmetric scrutiny. Key findings: Theorem 1 is the most sophisticated challenge to QNFO's epistemic posture yet produced; QNFO has five documented vulnerabilities; maximum convergence on core
  Full text (https://papers.qnfo.org/papers/huang-2025-quantum-advantage-audit), excerpts of its own sections:
  § 1. Introduction: Huang, Choi, McClean & Preskill (2025) have produced the most intellectually honest document about quantum advantage to emerge from the quantum computing establishment. Their Perspective paper — "The vast world of quantum advantage" (arXiv:2508.05720) — constructs a systematic framework for evaluating quantum advantage claims through five "keystone" properties (Predictability, Typicality, Robustness, Verifiability, Usefulness), surveys four distinct realms where quantum advantage can manifest, and proves a genuinely original theorem: that detecting quantum advantage is itself classically [...]
  § 3. Theorem 1: The Unpredictability Result: The paper's most original and philosophically consequential contribution is Theorem 1. Informally: assuming BPP ≠ BQP, the decision problem "does this specific quantum circuit outperform Pauli propagation classical simulation?" is in BQP but not in BPP. Quantum computers can answer it efficiently; classical computers cannot. The proof strategy (Appendix D): the problem is quantumly easy (run both methods on random instances and compare), and if it were classically easy, one could solve all BQP problems classically — contradicting BPP ≠ BQP. The paper draws a radical implication: "There are plenty of problems with genuine quantum advantages such that we cannot predict the advantage using only classical technology. Paradoxically, to fully map out the landscape of quantum advantages, we must use the very quantum technologies whose power we are trying to characterize." This is the most sophisticated challenge to QNFO's epistemic posture yet produced. [...]
  § Summary: Revised Vulnerability Assessment: | # | Vulnerability | Initial Severity | Revised Severity | Key Evidence | |---|---|---|---|---| | V1 | Ontological overreach | HIGH | MODERATE | Scaffold-invariant framework more nuanced than credited | | V2 | QEC overhead qualitative | HIGH | HIGH (STANDS) | No computed joules-per-solution threshold | | V3 | Shor's Assumptions gap | CRITICAL | MODERATE | 3 KG findings exist; D1 body missing | | V4 | $35B definitional | HIGH | MODERATE↑ | KG correction applied but NOT to source text | | V5 | Missing self-falsification | CRITICAL | MODERATE↑ | Active correction registry; no consolidated doc | | **NEW** | Portfolio allocation | — | CORRECTION | QNFO allocates 5–10% to FTQC, not 0% | | **CROSS** | D1 body truncation | — | SYSTEMIC | ≥3 D1 papers truncated; corrections not propagated to source docs | > ↑ = Upgraded by red-team review 2026-07-19. ↓ = Downgraded by the QNFO archive full-text cross-reference (2026-07-19).
  § 9. Conclusion: Huang, Choi, McClean & Preskill (2025) have produced the most honest document about quantum advantage to emerge from the quantum computing establishment. It is not a victory lap — it is a truce offering. It acknowledges the pseudo-advantage problem, admits the fragility of sensing advantage under noise, concedes that BPP ≠ BQP is unproven, and opens the possibility that the most important quantum advantages are ones we cannot currently conceive. QNFO's response should be correspondingly honest. QNFO's framework has genuine strengths: the joules-per-solution criterion, the portfolio approach to technology investment, the recognition that classical algorithms are advancing rapidly, and — as deep research revealed — an active self-correction practice that includes a disconfirming registry, multiple applied corrections (braid compilation, $35B claim, adelic theorem downgrade), and self-identified systemic biases. QNFO practices self-falsification operationally. [...]
[12] QNFO: Algorithmic-Necessity-of-Agency | https://papers.qnfo.org/papers/algorithmic-necessity-of-agency
  This treatise presents a comprehensive theoretical synthesis resolving the dialectic between the subjective experience of free will and the objective reality of a superdeterministic universe. By integrating the foundational principles of quantum mechanics—specifically the violation of statistical independence in Bell’s Theorem—with the functional neuroanatomy of the left-hemisphere interpreter, we
  Full text (https://papers.qnfo.org/papers/algorithmic-necessity-of-agency), excerpts of its own sections:
  § A: Unified Framework for Reconciling Quantum Superdeterminism with Evolutionary Neurobiology **Author:** Rowan Brad Quni-Gudzinas **Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com) **ORCID:** 0009-0002-4317-5604 **ISNI:** 0000000526456062 **URL:** https://papers.qnfo.org/papers/algorithmic-necessity-of-agency/ **Date:** 2026-03-03 **Version:** 1.0
  § 1.1 Quantum: Mechanics and the Measurement Problem Quantum mechanics fundamentally redefines the concept of measurement by introducing the observer as an active participant in physical reality, governed by the deterministic evolution of the wave function. Mechanistically, this evolution is described by the time-dependent Schrödinger equation, \(i\hbar \frac{\partial}{\partial t} \Psi(r,t) = \hat{H} \Psi(r,t)\), where the Hamiltonian operator \(\hat{H}\) dictates the total energy and future state of the system with absolute precision. This process operates exactly like rolling the cosmic dice, where the final number remains entirely unknown until the dice strike the table and settle, yet the trajectory was fixed the moment they left the hand. The evolutionary necessity of this perceptual collapse ensures that biological organisms interact with stable eigenstates rather than the complex probability amplitudes \(|\Psi|^2\), effectively reducing the computational load of environmental processing. [...]
  § 1.2 Bell’s: Theorem and the Local Hidden Variable Loophole Bell’s Theorem stands as one of the most profound mathematical proofs in the history of physics, establishing a strict inequality for any theory relying on local hidden variables. The theorem states that for any local realistic theory, the correlation between measurements must satisfy the inequality \(|E(a,b) - E(a,b')| + |E(a',b) + E(a',b')| \le 2\), known as the CHSH inequality. Experimental tests, however, routinely measure a value of \(2\sqrt{2}\), violating the limit and proving that the universe cannot be both local and real in the classical sense. This violation implies that the universe is far more interconnected than classical Newtonian physics could ever have predicted. The biological brain, evolved to understand local, macroscopic interactions where \(F_{gravity} \propto \frac{1}{r^2}\), struggles immensely to comprehend the implications of this mathematical proof. Consequently, Bell’s Theorem serves as the critical threshold where human intuition breaks down. [...]
  § 7.6 Maintaining the: Functional Illusion Maintaining the functional illusion is the advanced cognitive strategy where an individual intellectually accepts the absolute reality of superdeterminism while simultaneously allowing their brain to operate using the heuristic of free will in daily life. This psychological dual-boot system requires the prefrontal cortex to hold the objective truth of physics in the background while the left-hemisphere interpreter continues to generate the subjective feeling of agency in the foreground. This cognitive balancing act operates exactly like knowing it’s a movie but still crying, where the viewer is fully aware the tragedy is scripted and fictional, yet allows their biology to experience genuine emotional grief. Evolution permits this dual processing because completely disabling the illusion of choice would destroy the organism’s ability to rapidly interact with peers who still rely entirely on the agency bypass. [...]