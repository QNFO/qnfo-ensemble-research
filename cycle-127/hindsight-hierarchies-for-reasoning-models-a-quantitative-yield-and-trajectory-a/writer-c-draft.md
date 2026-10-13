# Hindsight Hierarchies for Reasoning Models: A Formal Yield Analysis of the Reverse-Engineering Self-Improvement Loop

## Abstract

Reasoning models such as theorem-proving systems hit a data wall: problems beyond a model's current ability yield no solved examples to train on, so the supervision corpus stops growing exactly where improvement is needed. The hindsight-hierarchies proposal of arXiv:2610.12168 addresses this by training one model jointly to predict solution ideas from problems alone, to reverse-engineer ideas from problems with supplied solutions, and to solve problems using provided ideas, alternating idea extraction with joint retraining; however, that work supplies a formal specification and a Lean instantiation while leaving empirical evaluation to future work, so the loop's data-economics are unquantified. This paper provides the missing quantitative layer. We formalize the loop as a discrete dynamical system over a solved-problem corpus and an idea-supervision corpus, parameterized by extraction recall $r$, extraction precision $p$, ideas per solution $m$, and solve-rate $\sigma$. Under stated assumptions ($m=5$, $r=0.6$, $p=0.8$, $\sigma=0.1$, pool $P=10^4$, seed corpus $N_0=10^3$), we derive an idea-amplification factor $A = mrp = 2.4$ clean idea-supervision pairs per solved problem per round, a logistic corpus trajectory reaching $N_5 = 4685.59$ solved problems after five rounds, and a cumulative $42791.26$ clean idea pairs, a $42.79\times$ amplification over the seed corpus. We identify the noise-accumulation boundary: the model-generated fraction of the corpus reaches $78.66\%$ by round five, making extraction precision, not solve rate, the binding quantity. The analysis converts an untested proposal into a falsifiable projection with explicit failure conditions.

## 1. Introduction

Teams building reasoning models for formal mathematics face a concrete bottleneck that grows worse as the models improve. Training data for such systems consists of problems paired with machine-checked solutions; a problem the current model cannot solve contributes no solution, hence no new supervision. The corpus therefore expands fastest where the model is already competent and stalls precisely at the difficulty frontier where capability gains are sought. Today this blocks the practical path of self-improvement for interactive theorem proving: a lab with a seed corpus of verified proofs and a large pool of unproved statements has no principled procedure for converting compute into new verified training examples at the frontier, and must instead rely on scarce human expert proofs, whose cost limits corpus growth. A procedure that reliably converts supplied solutions at any difficulty into reusable supervision would change the design decision of how to allocate annotation effort: instead of paying experts to prove frontier problems, one pays them to solve a smaller sample and lets the loop propagate the solution ideas.

The hindsight-hierarchies proposal [1], [2] is a candidate for exactly this role. Its observation is that even when a problem exceeds the model's solving ability, a supplied solution enables the model to extract useful solution ideas in hindsight. It operationalizes this by jointly training the same model on three capabilities: predicting solution ideas from problems alone, reverse-engineering ideas from problems with known solutions, and solving problems using provided ideas. The loop alternates between reverse-engineering ideas from problems with supplied solutions and using those ideas as additional supervision for joint training of all three capabilities. The authors give a formal specification and a concrete instantiation for interactive theorem proving in the Lean theorem prover, and state that empirical evaluation remains future work.

What is missing, and what blocks any decision to invest in building the loop, is a quantitative account of its data-economics. Without one, a practitioner cannot answer the questions that determine whether the loop is worth building: how much new supervision does one round yield per unit of supplied solution, at what extraction quality does the loop help rather than poison its own training signal, and how fast does the solved-problem corpus grow as a function of the solve rate on previously unsolved problems? This paper supplies that account analytically. We model the loop as a discrete dynamical system, derive its growth law in closed form, compute a worked trajectory under explicitly stated parameter assumptions, and identify which parameter the result is most sensitive to. All numerical results are projections under stated assumptions, not measurements; their role is to make the proposal falsifiable before any training run is funded.

Contributions:

1. A dynamical-systems formalization of the hindsight-hierarchy loop over two coupled corpora (solved problems and idea-supervision pairs), with the growth law $N_{t+1} = N_t + \sigma(P - N_t)$ and its closed-form solution $N_t = P - (P - N_0)(1-\sigma)^t$, derived in Section 3 and Section 4.
2. A derivation of the clean idea-amplification factor $A = mrp$ and the cumulative amplification over $T$ rounds, computed as $A = 2.4$ per round and $42.79\times$ cumulative over five rounds under stated assumptions, in Section 4.
3. Identification of the noise-accumulation boundary: the model-generated corpus fraction reaches $78.66\%$ by round five under the same assumptions, implying extraction precision $p$ is the binding parameter, derived in Section 4 and analyzed in Section 6.
4. A translation of these results into engineering guidance: which parameter to measure first, what the smallest de-risking experiment is, and which constraints bind first, in Section 7.

## 2. Background and Related Work

The direct object of this analysis is the hindsight-hierarchies paper itself, which appears in the bibliography as two entries with identical content. Entry [1] supplies the full abstract: the self-improvement loop rests on the observation that a supplied solution can enable extraction of useful solution ideas even when the problem exceeds the model's current solving ability; the method jointly trains one model on three capabilities (predicting ideas from problems alone, reverse-engineering ideas from problems and known solutions, and solving problems using provided ideas); the loop alternates reverse-engineering with joint retraining; and the paper gives a formal specification plus a Lean instantiation while stating that empirical evaluation remains future work. Entry [2] is the same work under its arXiv identifier 2610.12168v1, with the abstract truncated at the same point; we cite [2] when referring to the work by identifier and [1] when quoting its stated scope. Because the supplied abstracts state no empirical numbers, every quantitative claim about the loop in this paper is our own derivation, not a report of a result from [1] or [2].

The closest methodological ancestor in the supplied bibliography is hindsight reinforcement learning. Entry [3], "Hierarchical Reinforcement Learning with Hindsight" (arXiv:1805.08180v2), states that RL algorithms can suffer from poor sample efficiency when rewards are delayed and sparse, and introduces a solution enabling agents to learn temporally extended actions at multiple levels of abstraction in a sample-efficient and automated fashion, combining universal value functions with hindsight learning so that agents learn policies belonging to different levels. The shared idea with [1] is the relabeling of past experience as supervision: what was an unsuccessful attempt at one goal becomes a successful demonstration of a hindsight goal. Our analysis imports this framing but differs in the object relabeled: [3] relabels achieved states as goals, while [1] relabels supplied solutions as sources of transferable ideas, which introduces the extraction-precision parameter $p$ that has no analogue in the hindsight-goal setting and that our sensitivity analysis in Section 4 identifies as binding.

A second control-theoretic antecedent is entry [7], "Learning from the Hindsight Plan -- Episodic MPC Improvement" (arXiv:1609.09001v2). Its abstract states that model predictive control performs re-planning at every time step with a limited horizon due to computational and real-time constraints and robustness to model errors, that the limited horizon leads to suboptimal performance, and that the work considers the (abstract truncates here). The connection to our argument is structural: both [7] and the loop of [1] treat the output of a planning or solving episode as an input to improving the next episode, i.e., a self-improvement loop whose convergence properties depend on the quality of the reused artifact. The supplied summary of [7] gives no further detail on the mechanism, so we use it only to establish that hindsight-reuse loops have an established precedent in control, not to import any specific result.

Three entries bear on the training substrate rather than the loop. Entry [9], "Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training" (arXiv:2603.02208v1), states that training on verifiable symbolic data is a promising way to expand the reasoning frontier of language models beyond standard pre-training corpora, that existing procedural generators often rely on fixed puzzles or templates and do not deliver distributional breadth at scale, and that Reasoning Core procedurally generates verifiable symbolic reasoning data. This matters to our analysis because procedural generation and hindsight extraction are complementary supply channels for verifiable symbolic supervision: [9] generates problems from templates, while the loop of [1] converts solved problems into idea supervision. Our corpus-growth model in Section 3 treats the problem pool $P$ as exogenous; a generator of the kind [9] describes is one mechanism that could enlarge $P$, and we flag the coupling as an open question rather than modeling it.

Entry [8], "Transfer Learning with Pre-trained Conditional Generative Models" (arXiv:2204.12833v3), states that transfer learning is crucial for training deep networks on new target tasks, that current methods assume at least one of overlapping label spaces, available source datasets, or consistent architectures, and that these assumptions are difficult in practice because the target task (abstract truncates here). Its relevance is that the three jointly trained capabilities in [1] share one model across tasks whose label spaces differ (problems, problem-solution pairs, problem-idea pairs), so the transfer-learning framing of [8] raises the question of whether joint training transfers positively across the three capabilities; the supplied summary states no finding on this, and we treat positive transfer as an assumption of our model, listed in Section 6.

Entry [6], "Why & When Deep Learning Works: Looking Inside Deep Learnings" (arXiv:1705.03921v1), states that the ICRI-CI asked six leading deep-learning researchers to address why and when deep learning works, with the goal of looking inside deep networks and providing insights on how they function (abstract truncates). We cite it as evidence that interpretive questions about why a training procedure succeeds remain open at the field level, which supports our decision to give the loop of [1] a falsifiable analytical model rather than a mechanistic claim about why joint training of the three capabilities would work.

Two entries concern reasoning formalisms adjacent to, but distinct from, the loop. Entry [5], "Reasoning with Justifiable Exceptions in Contextual Hierarchies (Appendix)" (arXiv:1808.01874v1), states that it is an appendix to the paper by Bozzato, Serafini and Eiter (2018) providing further details on the language, the complexity results, and the datalog translation of the main paper. The supplied summary gives no further detail on those results; we note the work here because its subject, hierarchical reasoning with exceptions, is terminologically adjacent to "hindsight hierarchies" while being a symbolic-representation line of work rather than a training method, and we draw no technical content from it. Entry [4], "Navigating the State of Cognitive Flow: Context-Aware AI Interventions for Effective Reasoning Support" (arXiv:2504.16021v1), states that flow theory describes an optimal cognitive state of deep focus and intrinsic motivation when task difficulty aligns with skill level, that interventions disrupting cognitive flow can hinder decision-making in AI-augmented reasoning, and that the paper proposes a context-aware cognitive augmentation framework adapting interventions accordingly. Its relevance is conceptual: the loop of [1] is, for a model, a difficulty-matching mechanism, since supplied ideas lower the effective difficulty of frontier problems in a way loosely analogous to how [4] adapts human-facing intervention to the skill-difficulty gap. We use this only as a framing observation; the supplied summary states nothing about model training.

Finally, three QNFO corpus entries appear in the bibliography. Entry [13], "Structured Cross-Domain Translation as a Testable Consilience Mechanism," states that interdisciplinary analogy-making is usually treated as an ad hoc rhetorical act rather than a reproducible research procedure, and that the paper formalizes a conjecture that systematically translating a single formal object into multiple domain lexicons (abstract truncates). This is methodologically parallel to the loop of [1] at the level of representation transport: both treat the translation of a solution artifact into a reusable intermediate representation as the unit of supervision. Entries [10] ("QNFO: Syntactic Generation"), [11] ("QNFO: Impact of Cognitive Linearity on Epistemic Modeling"), and [12] ("QNFO: Projective Geometric Frameworks for Semantic Structures") are supplied with no summary text; we record that the supplied entries give no further detail, and relate them to our argument only through their titles, as candidate representation frameworks within which "solution ideas" might be formalized.

In summary, the literature supplied establishes (i) the hindsight-reuse precedent in RL and control [3], [7], (ii) the verifiable-symbolic-data substrate [9], (iii) open questions about transfer and mechanism [8], [6], and (iv) adjacent formal and cognitive framings [4], [5], [13]. None of the supplied entries quantifies the data-economics of the loop of [1]; that is the gap this paper fills.

## 3. Methods

### 3.1 Objects and notation

We model the loop of [1] as acting on two coupled corpora. Let:

- $P \in \mathbb{N}$: the total pool of problems available to the system, fixed within the analysis horizon.
- $N_t \in \mathbb{N}$: the number of problems with verified solutions at the start of round $t$, with $N_0$ the seed corpus.
- $U_t = P - N_t$: the number of unsolved problems at round $t$.
- $m \in \mathbb{N}$: the mean number of extractable solution ideas per solution.
- $r \in [0,1]$: extraction recall, the fraction of the $m$ ideas in a supplied solution that the reverse-engineering capability recovers.
- $p \in [0,1]$: extraction precision, the fraction of recovered ideas that are genuinely useful (correct and relevant) rather than spurious.
- $\sigma \in [0,1]$: the per-round solve rate, the probability that the model, equipped with ideas predicted by the idea-prediction capability, solves a previously unsolved problem and has the solution machine-verified.

"Solution idea" is the term of art of [1]; we operationalize it as any reusable intermediate representation extracted from a solution that can be supplied as conditioning to the solving capability. In the Lean instantiation of [1], a solution is a machine-checked proof, so a newly produced solution enters the corpus only if the proof checker accepts it; this verification gate is what keeps the solved-problem corpus free of unsound examples and is central to the noise analysis of Section 4.4.

### 3.2 The loop as a discrete dynamical system

One round of the loop, following the alternation stated in [1] (reverse-engineer ideas from problems with supplied solutions, then use these ideas as additional supervision for joint training of all three capabilities), induces the following update:

1. Idea extraction: from the $N_t$ solved problems, extract idea supervision pairs at rate $m r$ per solution, with precision $p$.
2. Joint retraining: retrain the single model on the three capabilities using the accumulated idea pairs and solved problems.
3. Solving: deploy the retrained model on the $U_t$ unsolved problems with predicted ideas as conditioning; a fraction $\sigma$ of attempts succeeds and passes machine verification, adding $\sigma U_t$ new solved problems.

The solved-problem corpus therefore obeys:

$$N_{t+1} = N_t + \sigma (P - N_t).$$

The idea-supervision corpus accumulates across rounds. Let $M_t$ denote the cumulative number of extracted idea pairs after round $t$:

$$M_t = \sum_{\tau=0}^{t} N_\tau \, m r,$$

of which the clean fraction is $p$, so the cumulative clean idea pairs are:

$$C_t = p \, M_t = \sum_{\tau=0}^{t} N_\tau \, m r p.$$

### 3.3 Closed-form growth law

The update equation is affine in $N_t$. Define the deficit $D_t = P - N_t$. Then:

$$D_{t+1} = P - N_{t+1} = P - N_t - \sigma(P - N_t) = (1-\sigma) D_t,$$

so $D_t = D_0 (1-\sigma)^t$ with $D_0 = P - N_0$, giving:

$$N_t = P - (P - N_0)(1-\sigma)^t. \tag{1}$$

This is the discrete logistic approach to saturation: growth is fastest at $t=0$ when the unsolved pool is largest, and the marginal yield per round decays geometrically at rate $(1-\sigma)$.

### 3.4 Amplification factors

We define two amplification quantities. The per-round clean idea amplification relative to the seed corpus is:

$$A = m r p. \tag{2}$$

The cumulative clean idea amplification after $T$ rounds relative to the seed corpus size $N_0$ is:

$$A_T = \frac{C_T}{N_0} = \frac{m r p}{N_0} \sum_{\tau=0}^{T} N_\tau. \tag{3}$$

Substituting (1) and using the geometric sum $\sum_{\tau=0}^{T} (1-\sigma)^\tau = \frac{1 - (1-\sigma)^{T+1}}{\sigma}$:

$$\sum_{\tau=0}^{T} N_\tau = (T+1) P - (P - N_0) \cdot \frac{1 - (1-\sigma)^{T+1}}{\sigma}, \tag{4}$$

which we evaluate numerically in Section 4.

### 3.5 Model-generated fraction

The fraction of the corpus at round $t$ that was produced by the model itself (rather than supplied in the seed) is:

$$f_t = 1 - \frac{N_0}{N_t}. \tag{5}$$

This quantity governs error-compounding risk: although each new solution is machine-verified for soundness (the Lean gate), the ideas extracted from model-generated solutions inherit the idiosyncrasies of model-generated proofs, and the idea labels produced by reverse-engineering are noisy at rate $1-p$ regardless of provenance.

### 3.6 Assumption register

All numerical results below are projections under the following assumptions, chosen as illustrative mid-range values because the supplied abstracts of [1], [2] state no empirical numbers:

- $P = 10^4$ problems in the pool.
- $N_0 = 10^3$ solved problems in the seed corpus.
- $m = 5$ extractable ideas per solution.
- $r = 0.6$ extraction recall.
- $p = 0.8$ extraction precision.
- $\sigma = 0.1$ per-round solve rate on previously unsolved problems, held constant across rounds (no capability improvement and no degradation within the horizon).
- Verification is perfect: a solution enters the corpus only if machine-checked, so solved-problem labels have precision $1$.
- Joint training transfers positively across the three capabilities (per the discussion of [8] in Section 2, this is an assumption, not a finding).

Sensitivity to each assumption is computed in Section 4.5.

## 4. Analysis

### 4.1 Per-round amplification factor

Inputs (Assumption register, Section 3.6): $m = 5$, $r = 0.6$, $p = 0.8$. From equation (2):

$$A = m r p = 5 \times 0.6 \times 0.8.$$

Step 1: $5 \times 0.6 = 3.0$. Step 2: $3.0 \times 0.8 = 2.4$.

$$A = 2.4.$$

Interpretation: each solved problem in the corpus yields, per round of extraction, $2.4$ clean idea-supervision pairs on average. The noise fraction in the idea labels is $1 - p = 0.2$: one in five extracted idea pairs is spurious.

### 4.2 Corpus trajectory

Inputs: $P = 10^4$, $N_0 = 10^3$, $\sigma = 0.1$. From equation (1), $N_t = 10^4 - 9 \times 10^3 \times (0.9)^t$.

We compute the first six values both by direct iteration of $N_{t+1} = N_t + 0.1(10^4 - N_t)$ and by the closed form, as a cross-check.

Direct iteration:

- $t=0$: $N_0 = 1000$.
- $t=1$: $N_1 = 1000 + 0.1 \times (10^4 - 1000) = 1000 + 0.1 \times 9000 = 1000 + 900 = 1900$.
- $t=2$: $N_2 = 1900 + 0.1 \times (10^4 - 1900) = 1900 + 0.1 \times 8100 = 1900 + 810 = 2710$.
- $t=3$: $N_3 = 2710 + 0.1 \times 7290 = 2710 + 729 = 3439$.
- $t=4$: $N_4 = 3439 + 0.1 \times 6561 = 3439 + 656.1 = 4095.1$.
- $t=5$: $N_5 = 4095.1 + 0.1 \times 5904.9 = 4095.1 + 590.49 = 4685.59$.

Closed-form cross-check at $t=5$: $(0.9)^5 = 0.59049$; $9000 \times 0.59049 = 5314.41$; $10^4 - 5314.41 = 4685.59$. The two methods agree.

$$N_5 = 4685.59 \text{ solved problems (expected-value trajectory; fractional values are expectations).}$$

The corpus grows by a factor $N_5 / N_0 = 4685.59 / 1000 = 4.68559$ over five rounds, i.e., a $4.69\times$ increase (rounded to three significant figures).

### 4.3 Cumulative clean idea pairs

Inputs: the trajectory $\{N_\tau\}$ from Section 4.2 and $m r p = 2.4$ from Section 4.1. From equation (3):

$$C_5 = 2.4 \times \sum_{\tau=0}^{5} N_\tau.$$

Step 1, the sum:

$$\sum_{\tau=0}^{5} N_\tau = 1000 + 1900 + 2710 + 3439 + 4095.1 + 4685.59.$$

Partial sums: $1000 + 1900 = 2900$; $2900 + 2710 = 5610$; $5610 + 3439 = 9049$; $9049 + 4095.1 = 13144.1$; $13144.1 + 4685.59 = 17829.69$.

Step 2, multiply by $2.4$:

$$C_5 = 2.4 \times 17829.69 = 42791.256.$$

Step 3, closed-form cross-check via equation (4): $\sum_{\tau=0}^{5} N_\tau = 6 \times 10^4 - 9000 \times \frac{1 - (0.9)^6}{0.1}$. Now $(0.9)^6 = 0.531441$, so $1 - 0.531441 = 0.468559$, and $\frac{0.468559}{0.1} = 4.68559$. Then $9000 \times 4.68559 = 42170.31$, and $6 \times 10^4 - 42170.31 = 17829.69$. This matches the direct sum.

Step 4, cumulative amplification from equation (3):

$$A_5 = \frac{C_5}{N_0} = \frac{42791.256}{1000} = 42.791256.$$

$$C_5 = 42791.26 \text{ clean idea pairs (rounded to two decimals)}, \quad A_5 = 42.79\times \text{ amplification over the seed corpus}.$$

For comparison, the seed corpus itself contains at most $N_0 \times m = 5000$ idea pairs if every idea in every seed solution were extracted perfectly; the loop's cumulative clean yield of $42791.26$ exceeds this by a factor $42791.256 / 5000 = 8.5582512$, because the corpus itself grows while being re-mined each round.

### 4.4 Noise accumulation and the model-generated fraction

Inputs: $N_0 = 1000$, $N_5 = 4685.59$. From equation (5):

$$f_5 = 1 - \frac{1000}{4685.59}.$$

Step 1: $1000 / 4685.59 = 0.213410...$; more precisely, $4685.59 \times 0.2134 = 999.90$, and refining, $1000/4685.59 = 0.2134106$. Step 2: $f_5 = 1 - 0.2134106 = 0.7865894$.

$$f_5 = 78.66\% \text{ of the corpus is model-generated by round five.}$$

Two distinct noise channels must be separated. Channel 1 (solved-problem labels): each model-generated solution passes the Lean verification gate, so its soundness is not in question; the risk is distributional, that model-generated proofs cluster in styles the model can produce, narrowing the idea distribution. Channel 2 (idea labels): every extracted idea pair, from seed or model-generated solutions, is clean with probability $p = 0.8$, so the idea-supervision corpus of $M_5 = C_5 / p = 42791.256 / 0.8 = 53489.07$ pairs contains $53489.07 - 42791.256 = 10697.814$ spurious pairs. Step check: $42791.256 / 0.8 = 53489.07$; $53489.07 \times 0.2 = 10697.814$. The spurious-pair count grows in proportion to the corpus, so the noise rate does not dilute with loop progress; it is a stationary property of the extraction capability.

### 4.5 Sensitivity analysis

We compute the partial derivative of the two headline quantities with respect to each parameter, evaluated at the assumption values.

Sensitivity of $A = m r p$ (exact, multiplicative): a relative change $\delta$ in any one of $m, r, p$ changes $A$ by the same relative amount, since $\frac{\partial A}{\partial m}\frac{m}{A} = \frac{\partial A}{\partial r}\frac{r}{A} = \frac{\partial A}{\partial p}\frac{p}{A} = 1$. Concretely: raising extraction precision from $p = 0.8$ to $p = 0.9$ gives $A = 5 \times 0.6 \times 0.9 = 2.7$, a $12.5\%$ gain ($0.3/2.4 = 0.125$); lowering it to $p = 0.5$ gives $A = 5 \times 0.6 \times 0.5 = 1.5$, a $37.5\%$ loss ($0.9/2.4 = 0.375$).

Sensitivity of the trajectory to $\sigma$: from equation (1), the five-round corpus size is $N_5 = 10^4 - 9000(1-\sigma)^5$. At $\sigma = 0.05$: $(0.95)^5 = 0.7737809375$, so $N_5 = 10^4 - 9000 \times 0.7737809375 = 10^4 - 6964.0284375 = 3035.9715625$. At $\sigma = 0.2$: $(0.8)^5 = 0.32768$, so $N_5 = 10^4 - 9000 \times 0.32768 = 10^4 - 2949.12 = 7050.88$. Halving $\sigma$ from $0.1$ to $0.05$ cuts the five-round corpus from $4685.59$ to $3035.97$ (a factor $3035.9715625 / 4685.59 = 0.647860...$, i.e., a $35.21\%$ reduction: $1 - 0.647860 = 0.352140$); doubling $\sigma$ to $0.2$ raises it to $7050.88$, a $50.48\%$ increase ($7050.88/4685.59 = 1.504815$; $1.504815 - 1 = 0.504815$).

Sensitivity of $C_5$ to $p$ is twofold, since $p$ enters both the per-pair cleanliness and nothing else in $C_5 = p \cdot m r \sum N_\tau$; the trajectory itself is independent of $p$ under our assumption that solve rate $\sigma$ is exogenous. Thus $C_5$ scales linearly in $p$: at $p = 0.5$, $C_5 = 0.5 \times 3 \times 17829.69 = 26744.535$; at $p = 0.9$, $C_5 = 0.9 \times 3 \times 17829.69 = 48140.163$. Check: $3 \times 17829.69 = 534