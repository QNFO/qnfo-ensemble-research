# Gate-Check Convergence: A Benchmark Design and Statistical Framework for Evaluating Cross-Model Agreement on Fringe Physics Claims

## Abstract

When independent large language models (LLMs) evaluate novel or fringe scientific claims, they often appear to reach identical verdicts through strikingly similar reasoning scaffolds — invoking, for example, Bell-type arguments or standard condensed-matter estimates. We call this hypothesized phenomenon *gate-check convergence*: the possibility that models retrieve a shared consensus lattice from overlapping training corpora rather than pattern-matching surface style. We propose a rigorous test of this hypothesis. We design a benchmark of fringe physics claims with known expert verdicts in three classes (falsified, trivial, valid-but-flawed), specify a blinded multi-model evaluation protocol, and derive the statistics needed to quantify inter-model agreement: Cohen's $\kappa$ on verdicts, an argument-structure alignment score, and a coincident-convergence probability under a null model of independent uniform verdicts. All quantitative results in this paper are design projections computed from stated assumptions, not measurements. Under a uniform three-class null, five models agreeing unanimously on a claim has probability $(1/3)^{4} \approx 1.23 \times 10^{-2}$, so a 120-claim benchmark expects roughly $1.5$ coincidental unanimous events — establishing that raw unanimity alone cannot certify genuine gate-checking. We derive the benchmark size ($\approx 48$ claims) needed to separate $\kappa = 0.85$ from $\kappa = 0.50$ at 95% confidence, and specify the falsifiable signature distinguishing consensus retrieval from correlated hallucination.

## 1. Introduction

Large language models are increasingly used to triage scientific-sounding assertions: is this claim falsified by known results, is it a trivial restatement, or is it valid but flawed? We hypothesize a behavior we call *gate-check convergence*: independent LLMs, evaluated blindly on the same fringe physics claim, converge not only on the same verdict but on the same *reasoning scaffold* — the same canonical argument structure (a Bell-type inequality argument, a group-theoretic $SU(2)/SO(3)$ obstruction, a BCS gap-arithmetic estimate). If real, this convergence would suggest that models retrieve from a common lattice of consensus scientific results embedded in overlapping training corpora, rather than independently reasoning or merely imitating stylistic patterns.

The question matters for three reasons. First, if convergence is robust, LLM panels could serve as reliable first-pass filters for the flood of fringe claims, a problem structurally analogous to the fact-checking scalability problem documented for web claims, where the volume of claims exceeds manual capacity by orders of magnitude [6]. Second, if convergence is *not* robust — if models agree only on well-represented consensus results and diverge on frontier questions — then agreement itself becomes a diagnostic of corpus coverage, and low agreement flags claims that genuinely require expert attention. Third, convergence could be spurious: correlated hallucination, where models share training-data errors and agree on wrong verdicts. Distinguishing genuine gate-checking from correlated hallucination requires correlating agreement with accuracy against expert ground truth.

This paper makes four contributions. (i) We formalize the gate-check convergence hypothesis and its null competitor. (ii) We specify a benchmark design: fringe physics claims with expert verdicts in three classes, evaluated blindly by multiple model families under varied prompt framings. (iii) We derive, with full arithmetic, the statistical machinery: Cohen's $\kappa$, its standard error, chance-agreement baselines, coincident-convergence probabilities, and minimum benchmark sizes. (iv) We state the falsifiable signature that separates consensus retrieval from correlated hallucination. Because no benchmark data have yet been collected, every number in Sections 4 and 5 is a design projection computed from explicitly stated assumptions; we are careful to label them as such.

## 2. Background and Related Work

The bibliography supplied for this paper is heterogeneous; several entries bear on our problem only by analogy or by terminological overlap, and we indicate where an entry's supplied summary is too thin to support more than a citation. We discuss all twelve works.

**Verification of claims by automated systems.** The fact-checking literature establishes the scale motivation for our work: the number of claims requiring verification is several orders of magnitude larger than what human fact-checkers can handle, and prior automation efforts have, per the supplied summary of [6], largely ignored a class of claims the authors identify (claims about images, in that work's framing). Our benchmark transfers the same scalability logic from image claims to fringe physics claims, where the expert-verification bottleneck is even sharper. On the LLM side, [2] presents a proof-of-concept framework using large language models to extract predictive value from unstructured text — medical records, adjuster notes, call transcripts — in an actuarial setting where manual processing is described as time-consuming, inconsistent across reviewers, and unscalable. Though domain-remote, [2] directly supports our premise that LLMs can be deployed as claim-processing pipelines, and its observation about reviewer inconsistency motivates measuring inter-model agreement rather than assuming it. Closest in spirit is [8], which studies intra-paper verification for peer review: existing automated novelty assessment compares a paper's claimed contributions against prior literature while implicitly assuming those contributions are realized in the work, whereas human reviewers frequently challenge exactly that assumption. This is precisely the failure mode we worry about in reverse: an LLM gate-checker may accept a claim's framing before checking whether the claimed support exists, and [8] supplies the peer-review-side evidence that such framing-versus-substance gaps are common enough to warrant automated scrutiny.

**Conventions and gate-keeping in physics.** Physics itself maintains explicit gate-check conventions. The supplied summary of [5] argues that the $5\sigma$-convention in particle physics, when applied to ultrashort-lived unstable particles such as a Higgs boson, produces a category mistake in which "pure reasoning is passed off as an observation." Whatever one's view of that argument, it demonstrates that the boundary between accepted and rejected scientific claims is policed by codified statistical conventions — exactly the kind of consensus lattice we hypothesize LLMs retrieve when gate-checking fringe claims. Community consensus formation is documented at scale in [3], whose summary describes the European Particle Physics Strategy Update as a bottom-up process in which the community submits proposals for near-, mid-, and longer-term projects, with inputs from national laboratories; this is the human process that generates the consensus documents an LLM's training corpus would later encode. A concrete artifact of such consensus is [4], a Snowmass '96 report presenting design expectations and the physics program of an $e^+e^-$ linear collider at $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$, reviewing experiments aimed at physics beyond the Standard Model and arguing feasibility of construction. Reports of this type are precisely the documents in which "frontier versus settled" judgments are institutionalized, and they anchor our claim that consensus verdicts have traceable textual sources.

**Terminological collisions.** Two bibliography entries use "claims" and "convergence" in senses unrelated to ours, and we flag this to prevent confusion. [7] studies claims problems in fair division: allocating a finite estate among agents whose total claims exceed resources, integrating the Proportional rule with the Constrained Equal Awards rule, which equalizes awards subject to claim-boundedness. The word "claims" there refers to asserted entitlements, not truth-apt propositions; the connection to our work is only the shared vocabulary. Likewise, [1] surveys compactness and geometric stability conjectures formulated at a 2018 IAS Emerging Topics Workshop on Scalar Curvature and Convergence, focusing on sequences of compact Riemannian manifolds with nonnegative scalar curvature. Its "convergence" is geometric (Gromov–Hausdorff-type limits of manifold sequences), not statistical agreement among evaluators. We cite both to keep the terminology honest: our "convergence" is an empirical agreement statistic, and nothing in [1] or [7] bears on it beyond the name.

**Fringe-adjacent corpus material.** The QNFO entries represent the kind of self-published theoretical material our benchmark would draw fringe claims from. [9] reports that five independent QNFO research programs converge on a single structural insight: that ultrametric (non-Archimedean) mathematics provides the correct state-space geometry for fundamental physics, quantum computation, and optimization. This is an interesting mirror of our hypothesis: a self-declared convergence of research programs, which our framework would treat as a test case — do LLM gate-checkers converge on a verdict about ultrametric state-space claims, and does that verdict match expert assessment? [11], per its summary, is a critical treatise arguing that the theoretical structure surrounding the electron — the most precisely measured particle in physics — rests on load-bearing but rarely interrogated assumptions, including the complex Hilbert-space postulate and the spin-statistics theorem's foundations. Such claims are ideal benchmark items in our "valid-but-flawed" or "trivial" categories: they interrogate real foundational issues but typically overstate the implications. Finally, [10] and [12] are supplied with empty summaries; the provided text gives no further detail about their content, so we relate them to our argument only as additional QNFO corpus items whose claims would be eligible benchmark entries, and we draw no substantive conclusion from them.

## 3. Methods

### 3.1 Benchmark construction

We define a benchmark $\mathcal{B} = \{c_1, \dots, c_N\}$ of $N$ fringe physics claims. Each claim $c_i$ carries an expert verdict $v_i^{\ast} \in \mathcal{V}$, where the verdict set is $\mathcal{V} = \{\text{falsified}, \text{trivial}, \text{valid-but-flawed}\}$, so $|\mathcal{V}| = 3$. Claims are sourced from self-published theoretical material of the QNFO type [9], [10], [11], [12], from fringe-adjacent foundational critiques, and from constructed variants of settled results. Expert verdicts are fixed before any model evaluation by at least two independent domain referees, with disagreements adjudicated by a third.

### 3.2 Evaluation protocol

Each of $k$ models $M_1, \dots, M_k$ from distinct families evaluates every claim under $f$ prompt framings (neutral, adversarial, sympathetic), blinded to expert verdicts and to other models' outputs. Each evaluation yields a verdict $\hat{v}_{i,m,r} \in \mathcal{V}$ and a free-text argument, from which we extract an argument-structure tag set $S_{i,m,r}$ — a labeled set of invoked scaffolds (e.g., Bell-type argument, $SU(2)/SO(3)$ representation obstruction, BCS gap-arithmetic estimate, dimensional-analysis bound).

### 3.3 Statistics

**Verdict agreement.** For each model pair $(m, m')$, observed agreement on verdicts is $p_o^{(m,m')} = \frac{1}{N}\sum_{i=1}^{N} \mathbb{1}[\hat{v}_{i,m} = \hat{v}_{i,m'}]$. Cohen's $\kappa$ corrects for chance:

$$\kappa = \frac{p_o - p_e}{1 - p_e},$$

where under a uniform null over $|\mathcal{V}| = 3$ classes the chance agreement is

$$p_e = \sum_{j=1}^{3} \left(\frac{1}{3}\right)^2 = \frac{1}{3}.$$

**Argument-structure alignment.** For two models' scaffold sets $S_{m}, S_{m'}$ on the same claim, we use the Jaccard index $J = |S_m \cap S_{m'}| / |S_m \cup S_{m'}|$.

**Coincident convergence.** Under the null that each model's verdict is an independent uniform draw from $\mathcal{V}$, the probability that all $k$ models agree on a given claim is

$$P_{\text{coin}}^{(k)} = 3 \cdot \left(\frac{1}{3}\right)^{k} = \left(\frac{1}{3}\right)^{k-1}.$$

**Standard error of $\kappa$.** We use the large-sample approximation

$$\mathrm{SE}(\kappa) \approx \sqrt{\frac{p_o (1 - p_o)}{N (1 - p_e)^2}}.$$

All arithmetic for these quantities appears in Section 4.

## 4. Analysis

Every input number below is either a design assumption (declared) or computed from prior steps. No number is taken from external data.

**A1. Chance agreement (input: $|\mathcal{V}| = 3$, uniform null assumption).**

$$p_e = 3 \times \left(\frac{1}{3}\right)^2 = 3 \times \frac{1}{9} = \frac{1}{3} \approx 0.3333.$$

**A2. $\kappa$ for a hypothesized observed agreement (input: design target $p_o = 0.90$, from A1 $p_e = 1/3$).**

$$\kappa = \frac{0.90 - 0.3333}{1 - 0.3333} = \frac{0.5667}{0.6667} \approx 0.8500.$$

So 90% raw agreement corresponds to $\kappa \approx 0.85$ under the uniform null — near-perfect agreement on Landis–Koch-style conventions, though we note such conventions are themselves community conventions of the kind [5] interrogates.

**A3. Standard error of $\kappa$ at $N = 120$ claims (inputs: $p_o = 0.90$, $p_e = 1/3$, $N = 120$).**

$$\mathrm{SE}(\kappa) = \sqrt{\frac{0.90 \times 0.10}{120 \times (2/3)^2}} = \sqrt{\frac{0.09}{120 \times 0.4444}} = \sqrt{\frac{0.09}{53.3333}} = \sqrt{0.0016875} \approx 0.0411.$$

The 95% half-width is $1.96 \times 0.0411 \approx 0.0806$, giving a projected interval $\kappa \in [0.85 - 0.0806,\ 0.85 + 0.0806] = [0.769,\ 0.931]$ if the true agreement were $p_o = 0.90$.

**A4. Coincident-convergence probability for $k = 5$ models (input: $k = 5$, uniform null).**

$$P_{\text{coin}}^{(5)} = \left(\frac{1}{3}\right)^{4} = \frac{1}{81} \approx 0.01235.$$

**A5. Expected number of coincidental unanimous events in a 120-claim benchmark (inputs: $N = 120$, $P_{\text{coin}}^{(5)} = 1/81$).**

$$\mathbb{E}[\text{events}] = N \times P_{\text{coin}}^{(5)} = \frac{120}{81} \approx 1.4815.$$

**A6. Probability of at least one coincidental unanimous event (inputs: $N = 120$, $P_{\text{coin}}^{(5)} = 1/81$; independence across claims).**

$$P(\geq 1) = 1 - \left(1 - \frac{1}{81}\right)^{120} = 1 - \left(\frac{80}{81}\right)^{120}.$$

Compute: $\ln(80/81) = \ln(0.987654) \approx -0.012422$; multiplied by $120$: $-1.49064$; exponentiating: $e^{-1.49064} \approx 0.2251$. Hence

$$P(\geq 1) \approx 1 - 0.2251 = 0.7749.$$

Under the null, a 120-claim, 5-model benchmark has a $\approx 77\%$ chance of showing at least one fully unanimous claim by pure chance. Unanimity per se is therefore weak evidence of gate-check convergence; the discriminant must be *scaffold alignment plus accuracy*, not verdict agreement alone.

**A7. Benchmark size to separate strong from weak convergence (inputs: target separation $\Delta = |\kappa_1 - \kappa_2| = 0.85 - 0.50 = 0.35$; desired half-width $\leq \Delta/3.92$ so that 95% CIs do not overlap; $p_e = 1/3$).**

Required half-width: $0.35 / 3.92 \approx 0.0893$. At the midpoint $\kappa = 0.675$, the corresponding observed agreement is

$$p_o = p_e + \kappa (1 - p_e) = \frac{1}{3} + 0.675 \times \frac{2}{3} = 0.3333 + 0.4500 = 0.7833.$$

Then $p_o(1 - p_o) = 0.7833 \times 0.2167 \approx 0.1697$. Setting $\mathrm{SE}(\kappa) = 0.0893$ and solving for $N$:

$$N = \frac{p_o (1 - p_o)}{\mathrm{SE}(\kappa)^2 (1 - p_e)^2} = \frac{0.1697}{0.0893^2 \times 0.4444} = \frac{0.1697}{0.007974 \times 0.4444} = \frac{0.1697}{0.003544} \approx 47.9.$$

So $N \approx 48$ claims suffice, under these assumptions, to distinguish $\kappa = 0.85$ from $\kappa = 0.50$ with non-overlapping 95% intervals; we adopt $N = 120$ to leave headroom for stratification across claim categories and framings.

**A8. Illustrative scaffold-alignment statistic (inputs: two models each invoke $|S_1| = |S_2| = 4$ scaffolds from a 6-scaffold taxonomy, with overlap $|S_1 \cap S_2| = 3$).**

$$J = \frac{3}{4 + 4 - 3} = \frac{3}{5} = 0.60.$$

This is a worked example of the metric definition, not a measurement.

## 5. Results

No benchmark data have been collected; all results below are design projections derived in Section 4 from the stated assumptions (three-class verdict space, uniform null, independence across models and claims). Their empirical status is exactly that of assumptions-to-consequences, not measurements.

**R1 (chance baseline).** Under the uniform three-class null, chance agreement between two models is $p_e = 1/3 \approx 0.3333$ (A1).

**R2 (agreement mapping).** Raw agreement $p_o = 0.90$ corresponds to $\kappa \approx 0.85$ (A2).

**R3 (precision projection).** At $N = 120$ claims, the projected standard error of $\kappa$ is $\approx 0.0411$, with a 95% interval half-width $\approx 0.0806$ (A3).

**R4 (coincidence rates).** For $k = 5$ models, the null probability of unanimous agreement on a single claim is $1/81 \approx 1.23 \times 10^{-2}$ (A4); the expected count of such coincidental unanimities over 120 claims is $\approx 1.48$ (A5); and the probability of at least one is $\approx 0.775$ (A6).

**R5 (benchmark size).** Approximately 48 claims are needed to separate $\kappa = 0.85$ from $\kappa = 0.50$ at non-overlapping 95% confidence (A7); the proposed benchmark uses $N = 120$.

**R6 (falsifiable signature).** Genuine gate-check convergence predicts: (a) $\kappa$ significantly above $1/3$-anchored chance, (b) scaffold Jaccard alignment well above the value obtained by randomly drawn scaffold sets, and (c) agreement *positively correlated with accuracy against expert verdicts*, and *higher on well-represented consensus results than on frontier questions*. Correlated hallucination predicts (a) possibly holding but (c) failing: high agreement with low accuracy. If agreement does not track corpus representation of the underlying consensus result, the retrieval model is falsified.

## 6. Discussion

**Limitations.** The uniform null is a convenience, not a fact. Real models have category biases (e.g., over-producing "falsified"), which inflates $p_e$ above $1/3$ and thus *deflates* $\kappa$; conversely, correlated training data mean the independence assumption behind A4–A6 is optimistic, so true coincidental-unanimity rates may exceed our $1/81$ estimate. Both biases push in opposite directions, and neither can be resolved without pilot data. The scaffold taxonomy (6 scaffolds in A8) is illustrative; a real taxonomy requires annotation guidelines and inter-annotator validation, which we have not performed. The SE approximation in A3 is large-sample and may be inaccurate at small $N$ or extreme agreement.

**Failure modes.** The benchmark's expert verdicts are themselves produced by a consensus process subject to the dynamics [3] documents and the convention-dependence [5] highlights; if expert ground truth is wrong on some items, high model agreement with it measures corpus fidelity to consensus, not truth. Claims drawn from QNFO-style material [9], [10], [11], [12] may be systematically easier or harder than the broader fringe population, limiting external validity. Prompt-framing effects could dominate verdicts, confounding model-family comparisons unless framings are analyzed as a blocking factor.

**What would falsify our claims.** If blinded multi-model runs show $\kappa$ near chance ($\approx 0$ to $0.2$) on consensus-heavy claims, the gate-check convergence hypothesis dies. If $\kappa$ is high but accuracy against expert verdicts is low, the correlated-hallucination competitor wins. If agreement is high on frontier questions and low on consensus results — the reverse of the retrieval prediction — the corpus-overlap model is falsified.

**Open questions.** Does scaffold alignment predict verdict agreement at the item level, or only in aggregate? How should citation-quality variance be scored when fringe claims have no canonical citation target? And can the framework extend beyond physics, given that the supplied summaries of [2] and [8] show LLM claim-processing being deployed in actuarial and peer-review settings where ground truth is far softer than in physics?

## 7. Conclusion

We have formalized gate-check convergence — the hypothesis that independent LLMs reach identical verdicts on fringe physics claims via shared reasoning scaffolds retrieved from a common consensus lattice — and specified a benchmark and statistical framework capable of testing it against its null competitors. The central design lesson is quantitative: under a uniform three-class null, unanimity among five models is expected by chance on roughly $1.5$ of 120 claims, with probability $\approx 0.775$ of at least one such event, so verdict agreement alone cannot certify convergence. The discriminative signal must combine Cohen's $\kappa$ (needing $N \approx 48$ claims to separate strong from weak convergence), scaffold-level alignment, and accuracy against expert ground truth. All numbers herein are projections from stated assumptions; the empirical program they specify — blinded, multi-family, multi-framing evaluation against expert-anchored verdicts — is the next step, and its outcomes would either establish gate-check convergence as a measurable property of contemporary LLMs or falsify it in a way that itself maps where the consensus lattice is thin.

## References

[1] arXiv:2103.10093v1 | Conjectures on Convergence and Scalar Curvature

[2] arXiv:2606.06089v1 | Leveraging LLMs for Unstructured Claims Data Analysis

[3] arXiv:1910.11775v2 | Physics Briefing Book

[4] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96

[5] arXiv:1502.01303v3 | A category mistake in observational claims regarding ultrashort-lived unstable particles

[6] arXiv:1908.11722v1 | Fact-Checking Meets Fauxtography: Verifying Claims About Images

[7] arXiv:2605.26948v1 | Integrating Proportionality and Egalitarianism in Claims Problems

[8] arXiv:2607.26066v1 | Do Methods Support the Claims? Intra-Paper Verification for Peer Review

[9] QNFO: Five Pillars, One Structure: Consilient Convergence in QNFO Research | DOI 10.5281/zenodo.21603374

[10] QNFO: The Continuum Critique Trilogy | DOI 10.5281/zenodo.21691415

[11] QNFO: A Critical Treatise on the Load-Bearing Assumptions of Quantum Mechanics, Thermodynamics, and Computation | DOI 10.5281/zenodo.21975507

[12] QNFO: Five Objections, One Standard: An Evidence-Graded Adjudication of a Critique of Post-Quantum Synthesis | DOI 10.5281/zenodo.22010489