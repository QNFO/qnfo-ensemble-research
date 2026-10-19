# Hindsight Hierarchies for Reasoning Models: A Quantitative Yield and Trajectory Analysis of the Reverse-Engineering Self-Improvement Loop

## Abstract

Reasoning models for formal mathematics hit a data wall: training corpora consist of problems paired with machine-checked solutions, so problems beyond a model's current ability yield no solved examples, and the corpus stops growing exactly where improvement is needed. The hindsight-hierarchies proposal of arXiv:2610.12168 addresses this by jointly training one model to predict solution ideas from problems alone, to reverse-engineer ideas from problems with supplied solutions, and to solve problems using provided ideas; however, that work supplies a formal specification and a Lean instantiation while stating that empirical evaluation remains future work, so the loop's data economics are unquantified. This paper provides the missing quantitative layer. We formalize the loop as a discrete dynamical system over a solved-problem corpus and an idea-supervision corpus, parameterized by ideas per solution $m$, extraction recall $r$, extraction precision $p$, and solve rate $\sigma$. Under stated assumptions ($m=5$, $r=0.6$, $p=0.8$, $\sigma=0.1$, pool $P=10^4$, seed corpus $N_0=10^3$), we derive a per-round clean idea amplification $A = mrp = 2.4$, a trajectory reaching $N_5 = 4685.59$ solved problems after five rounds, a cumulative $42791.26$ clean idea pairs ($42.79\times$ the seed corpus), and a model-generated corpus fraction of $78.66\%$ by round five, making extraction precision, not solve rate, the binding quantity; the break-even precision against direct fine-tuning on solutions is $p > 1/3$. The analysis converts an untested proposal into a falsifiable projection with explicit failure conditions.

## 1. Introduction

Teams building reasoning models for formal mathematics face a concrete bottleneck that grows worse as the models improve. Training data for such systems consists of problems paired with machine-checked solutions; a problem the current model cannot solve contributes no solution, hence no new supervision. The corpus therefore expands fastest where the model is already competent and stalls precisely at the difficulty frontier where capability gains are sought. Today this blocks the practical path of self-improvement for interactive theorem proving: a lab with a seed corpus of verified proofs and a large pool of unproved statements has no principled procedure for converting compute into new verified training examples at the frontier, and must instead rely on scarce human expert proofs, whose cost limits corpus growth. Every training iteration on self-generated data is capped by the fraction of the corpus the model can close unaided, and scaling compute does not manufacture solutions to problems beyond the current frontier. A procedure that reliably converts supplied solutions at any difficulty into reusable supervision would change a specific design decision: instead of paying experts to prove frontier problems, one pays them to solve a smaller sample and lets the training loop propagate the solution ideas, so that the frontier of automatically provable statements advances at a rate set by the supply of human-written proofs rather than by the model's current solve rate.

The hindsight-hierarchies proposal [1], [2] is a candidate for exactly this role. Its central observation, stated in its abstract, is that even when a problem exceeds the model's solving ability, a supplied solution might enable the model to extract useful solution ideas in hindsight. It operationalizes this by jointly training the same model on three capabilities: predicting solution ideas from problems alone, reverse-engineering ideas from problems with known solutions, and solving problems using provided ideas. The loop alternates between reverse-engineering ideas from problems with supplied solutions and using those ideas as additional supervision for joint training of all three capabilities. The authors give a formal specification and a concrete instantiation for interactive theorem proving in the Lean theorem prover, and state explicitly that empirical evaluation remains future work. Two details of their specification matter for the analysis that follows. First, in a verifiable problem domain they assume a deterministic procedure $\mathsf{Verify}\colon\mathcal{X}\times\mathcal{Y}\to\{0,1\}$ that returns $1$ if and only if $y$ is a valid solution for $x$, which can be queried repeatedly [1]; this verification gate is what keeps the solved-problem corpus free of unsound examples. Second, their $\mathsf{ConstructTriple}$ procedure samples several hindsight-derived hierarchies and selects among them using an estimate of usefulness, together with a penalty encouraging the intended levels of granularity [1]; this verifier-guided selection is a concrete mechanism by which the extraction precision $p$ introduced below can be engineered upward.

What is missing, and what blocks any decision to invest in building the loop, is a quantitative account of its data economics. Without one, a practitioner cannot answer the questions that determine whether the loop is worth building: how much new supervision does one round yield per unit of supplied solution, at what extraction quality does the loop help rather than poison its own training signal, and how fast does the solved-problem corpus grow as a function of the solve rate on previously unsolved problems? A prior version of this analysis exists as a QNFO corpus paper [9]; the present text is its revision, with the derivations restated in full and the literature discussion rebuilt so that every statement about a cited work rests on that work's own text. We model the loop as a discrete dynamical system, derive its growth law in closed form, compute a worked trajectory under explicitly stated parameter assumptions, identify which parameter the result is most sensitive to, and state the measurement that would confirm or refute the model. All numerical results are projections under stated assumptions, not measurements; their role is to make the proposal falsifiable before any training run is funded.

Contributions:

- A dynamical-systems formalization of the hindsight-hierarchy loop over two coupled corpora (solved problems and idea-supervision pairs), with the growth law $N_{t+1} = N_t + \sigma(P - N_t)$ and its closed-form solution $N_t = P - (P - N_0)(1-\sigma)^t$, derived in Section 3 and Section 4.
- A derivation of the clean idea-amplification factor $A = mrp$ and the cumulative amplification over five rounds, computed as $A = 2.4$ per round and $42.79\times$ cumulative under stated assumptions, in Section 4.
- A break-even condition against direct fine-tuning on solutions, $mrp > 1$, giving a break-even precision of $p > 1/3$ at the stated $m$ and $r$, derived in Section 4.
- Identification of the noise-accumulation boundary: the model-generated corpus fraction reaches $78.66\%$ by round five under the same assumptions, implying extraction precision $p$ is the binding parameter, derived in Section 4 and analyzed in Section 6.
- A translation of these results into engineering guidance: which parameter to measure first, what the smallest de-risking experiment is, and which constraints bind first, in Section 7.

## 2. Background and Related Work

The direct object of this analysis is the hindsight-hierarchies work itself, which appears in the bibliography as two entries with identical content. Entry [1] supplies the full abstract: the self-improvement loop rests on the observation that a supplied solution can enable extraction of useful solution ideas even when the problem exceeds the model's current solving ability; the method jointly trains one model on three capabilities (predicting ideas from problems alone, reverse-engineering ideas from problems and known solutions, and solving problems using provided ideas); the loop alternates reverse-engineering with joint retraining; and the paper gives a formal specification plus a Lean instantiation while stating that empirical evaluation remains future work. Entry [2] is the same work under its arXiv identifier 2610.12168v1; we cite [2] when referring to the work by identifier and [1] when quoting its stated scope. Beyond the abstract, the full text of [1] makes three points this paper uses. In its section on language models for interactive theorem proving, it states that its Lean instantiation builds on language-model-guided proof search, conditioning tactic generation on learned hierarchies of proof ideas, and that recent Lean provers explore large-scale synthetic proof data and reinforcement learning from proof assistant feedback. In its verifiable-problem-domains section, it defines the deterministic $\mathsf{Verify}$ procedure whose existence without further domain assumptions is, by its own remark, the key requirement of the setting. In its Lean example, it restricts the tactic set to tactics that do not admit unproved obligations or introduce disallowed axioms, explicitly excluding $\mathsf{sorry}$ and $\mathsf{admit}$; this restriction is the formal counterpart of the soundness gate our noise analysis in Section 4.4 relies on. Because the abstract states no empirical numbers, every quantitative claim about the loop in this paper is our own derivation, not a report of a result from [1] or [2].

The closest methodological antecedent with quantitative content is hindsight-based control. Entry [6], "Learning from the Hindsight Plan -- Episodic MPC Improvement" (arXiv:1609.09001v2), states that model predictive control performs re-planning at every time step with a limited horizon due to computational and real-time constraints and often for robustness to model errors, and that the limited horizon leads to suboptimal performance; the work introduces a policy-improvement method that employs an online MPC policy and suggests improved actions based on an offline hindsight calculation once an episode has ended, rather than using value functions or policy gradients. Its experiments give numbers that show a hindsight-reuse loop can pay off in practice: on a real PR2 peg insertion task, the authors constructed a GMM dynamics prior from $40{,}000$ samples of actions in free space, collected by running iLQG for $30$ minutes, used a shorter hindsight horizon $\bar{H}=30$ to account for less accurate dynamics, and report that HIMPC inserts the peg faster and with better precision than baseline MPC after $3$ episodes of learning. The structural correspondence with [1] is exact: both treat the output of a planning or solving episode as an input to improving the next episode, and both face the question of how much quality in the reused artifact the improvement loop tolerates. Our analysis imports this framing but differs in the object reused: [6] reuses hindsight plans of a known dynamical system, while [1] reuses supplied solutions as sources of transferable ideas, which introduces the extraction-precision parameter $p$ that has no analogue in the control setting and that our sensitivity analysis in Section 4.5 identifies as binding.

On the data-supply side, the loop competes with and complements procedural generation. Entry [8], "Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training" (arXiv:2603.02208v1), states that training on verifiable symbolic data is a promising way to expand the reasoning frontier of language models beyond standard pre-training corpora, that existing procedural generators often rely on fixed puzzles or templates and do not deliver the distributional breadth needed at scale, and that Reasoning Core procedurally generates verifiable symbolic reasoning data with external solver verification and continuous difficulty control. Its full text gives scale figures that calibrate what "large pool" means in current practice: the suite releases $10\,\text{M}$ examples ($5\,\text{B}$ tokens) for pre-training and $1\,\text{M}$ examples ($1\,\text{B}$ tokens) for post-training, and generating each subset took about $3$ days with $48$ threads on an Intel Xeon Gold 5320. Its zero-shot evaluation of the GPT-5 family, with $200$ samples per task and difficulty, found all tasks sufficiently challenging even for frontier models, with higher failure rates in hard mode. This matters for our model in two ways. Procedural generation and hindsight extraction are complementary supply channels: [8] generates problems from parameterized task distributions, while the loop of [1] converts solved problems into idea supervision. Our corpus-growth model in Section 3 treats the problem pool $P$ as exogenous; a generator of the kind [8] describes is one mechanism that could enlarge $P$ at a compute cost of days on a multi-threaded server, and we flag the coupling as an open question rather than modeling it. The observation that frontier models fail on hard generated tasks also supports the premise that an unsolved pool of realistic size will exist in any deployment.

Whether the three jointly trained capabilities of [1] transfer positively across one shared model is an open empirical question, and the transfer-learning literature frames it precisely. Entry [7], "Transfer Learning with Pre-trained Conditional Generative Models" (arXiv:2204.12833v3), states that current transfer learning methods always assume at least one of (i) source and target task label spaces overlap, (ii) source datasets are available, and (iii) target network architectures are consistent with source ones, and that holding these assumptions is difficult in practical settings. The work proposes a method composed of pseudo pre-training (PP), which yields initial weights of a target architecture from generated samples, and pseudo semi-supervised learning (P-SSL), which treats samples from the source generative model as an unlabeled dataset for the target task; its experiments compare against scratch training and knowledge distillation across multiple target architectures and datasets, and its stated limitation is the difficulty of improving target models when the gap between source and target is too large. The three capabilities of [1] share one model across tasks whose label spaces differ (problems, problem-solution pairs, problem-idea pairs), so the setting of [7] — transfer without label-space overlap and without source datasets — is the relevant template, and its limitation warns that a large gap between, say, idea prediction and solving could make joint training counterproductive. We treat positive transfer as an assumption of our model and list it in Section 6.

A second control-theoretic and epistemological caution comes from the general question of why training procedures work at all. Entry [5], "Why & When Deep Learning Works: Looking Inside Deep Learnings" (arXiv:1705.03921v1), states that the Intel Collaborative Research Institute for Computational Intelligence, supporting machine learning and deep learning research since its foundation in 2012, asked six leading ICRI-CI deep-learning researchers to address the challenge of why and when deep learning works, with the goal of looking inside deep learning and providing insights on how deep networks function. We cite it as evidence that interpretive questions about why a training procedure succeeds remain open at the field level, which supports our decision to give the loop of [1] a falsifiable analytical model rather than a mechanistic claim about why joint training of the three capabilities would work.

Two entries concern reasoning formalisms and human factors adjacent to, but distinct from, the loop. Entry [4], "Reasoning with Justifiable Exceptions in Contextual Hierarchies (Appendix)" (arXiv:1808.01874v1), is an appendix to the paper by Bozzato, Serafini and Eiter (2018) providing further details on the language, the complexity results and the Datalog translation introduced in the main paper; its full text presents the syntax and semantics of $\mathcal{SROIQ}$ operators and axioms and proves complexity results for contextual knowledge representation systems, including that deciding whether a CAS-interpretation of a sCKR is a CKR-model is coNP-complete under data complexity, by a reduction from a variant of UNSAT, and that $\mathsf{c}$-entailment for a ranked sCKR with profile-based preference is $\Delta^{p}_{2}$-complete. Its subject, hierarchical reasoning with exceptions in a symbolic representation, is terminologically adjacent to "hindsight hierarchies" while being a knowledge-representation line of work rather than a training method; the complexity results are a reminder that reasoning over hierarchies carries computational cost even in purely symbolic settings, and we draw no technical content from it for the training loop itself. Entry [3], "Navigating the State of Cognitive Flow: Context-Aware AI Interventions for Effective Reasoning Support" (arXiv:2504.16021v1), states that flow theory describes an optimal psychological state of deep focus and intrinsic motivation when a task's difficulty aligns with the individual's skill level, that in AI-augmented reasoning interventions disrupting cognitive flow can hinder rather than enhance decision-making, and it proposes a context-aware cognitive augmentation framework that adapts interventions based on inferred cognitive state, using behavioral cues to distinguish deep engagement, cognitive overload, and disengagement due to insufficient challenge. Its relevance is a design caution for human-facing deployment: if the loop is used to select which problems and hints to show a human mathematician, supplying ideas for problems far above the user's skill level is precisely the difficulty-skill mismatch the flow framing warns against, and a context-aware selection layer of the kind [3] advocates would be the mitigation. The entry reports no empirical measurements, so this remains a caution, not a quantified constraint.

Finally, two QNFO corpus entries bear on this paper directly and methodologically. Entry [9] is the prior version of the present analysis in the QNFO corpus, "Hindsight Hierarchies for Reasoning Models: A Quantitative Yield and Trajectory Analysis of the Reverse-Engineering Self-Improvement Loop"; its full text states the same assumption register ($P = 10^4$, $N_0 = 10^3$, $m = 5$, $r = 0.6$, $p = 0.8$, $\sigma = 0.1$), the same growth law reaching $N_5 = 4685.59$, the same cumulative amplification $A_5 = 42.79\times$, and the same break-even $p > 1/3$, and its discussion already identifies the qualitatively different failure mode in which extracted ideas are so generic that supplying them does not condition the solver. The present paper is a revision of [9]: the derivations are restated with full arithmetic, and the related-work discussion is rebuilt so that each cited work is discussed through specific points of its own text. Entry [10], "QNFO: Impact of Cognitive Linearity on Epistemic Modeling," argues that linearity serves as a pragmatic abstraction — a necessary cognitive and technical simplification that enables coordination and control — but that through the Reification Fallacy these abstractions are frequently mistaken for the underlying reality, and that linear strategies work efficiently within narrow local bounds while accruing epistemic debt over time, with engineering succeeding by explicitly taming nonlinear dynamics through stochastic methods and feedback loops. This is a methodological caution aimed at this paper itself: our growth law $N_{t+1} = N_t + \sigma(P-N_t)$ is exactly such a pragmatic linear abstraction, valid in the local regime where the parameters are constant, and the reification risk is to read the geometric trajectory as a property of the loop rather than of the model. Section 6 carries this caution into the limitations list.

In summary, the literature establishes the hindsight-reuse precedent with quantitative evidence in control [6], the verifiable-symbolic-data substrate and its scale [8], the transfer-learning template and its gap limitation [7], open mechanistic questions at the field level [5], adjacent symbolic-hierarchy formalisms with their own complexity costs [4], a human-factors caution for deployment [3], the prior version of this analysis [9], and a methodological warning against reifying linear models [10]. None of these entries quantifies the data economics of the loop of [1]; that is the gap this paper fills.

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

"Solution idea" is the term of art of [1]; we operationalize it as any reusable intermediate representation extracted from a solution that can be supplied as conditioning to the solving capability. In the Lean instantiation of [1], a solution is a machine-checked proof, and the tactic set is restricted to tactics that do not admit unproved obligations or introduce disallowed axioms, excluding $\mathsf{sorry}$ and $\mathsf{admit}$ [1]; a newly produced solution enters the corpus only if the prover accepts it. This verification gate is what keeps the solved-problem corpus free of unsound examples and is central to the noise analysis of Section 4.4.

### 3.2 The loop as a discrete dynamical system

One round of the loop, following the alternation stated in [1] (reverse-engineer ideas from problems with supplied solutions, then use these ideas as additional supervision for joint training of all three capabilities), induces the following update:

1. Idea extraction: from the $N_t$ solved problems, extract idea-supervision pairs at rate $mr$ per solution, with precision $p$.
2. Joint retraining: retrain the single model on the three capabilities using the accumulated idea pairs and solved problems.
3. Solving: deploy the retrained model on the $U_t$ unsolved problems with predicted ideas as conditioning; a fraction $\sigma$ of attempts succeeds and passes machine verification, adding $\sigma U_t$ new solved problems.

The solved-problem corpus therefore obeys:

$$N_{t+1} = N_t + \sigma (P - N_t).$$

The idea-supervision corpus accumulates across rounds. Let $M_t$ denote the cumulative number of extracted idea pairs after round $t$:

$$M_t = \sum_{\tau=0}^{t} N_\tau \, mr,$$

of which the clean fraction is $p$, so the cumulative clean idea pairs are:

$$C_t = p \, M_t = \sum_{\tau=0}^{t} N_\tau \, mrp.$$

### 3.3 Closed-form growth law

The update equation is affine in $N_t$. Define the deficit $D_t = P - N_t$. Then:

$$D_{t+1} = P - N_{t+1} = P - N_t - \sigma(P - N_t) = (1-\sigma) D_t,$$

so $D_t = D_0 (1-\sigma)^t$ with $D_0 = P - N_0$, giving:

$$N_t = P - (P - N_0)(1-\sigma)^t. \tag{1}$$

This is the discrete logistic approach to saturation: growth is fastest at $t=0$ when the unsolved pool is largest, and the marginal yield per round decays geometrically at rate $(1-\sigma)$. Following the caution of [10], this law is a pragmatic linear abstraction: it is exact under the model's assumptions and a local description of the real loop only in the regime where the parameters do not drift.

### 3.4 Amplification factors and break-even

We define two amplification quantities. The per-round clean idea amplification per solved problem is:

$$A = mrp. \tag{2}$$

The cumulative clean idea amplification after $T$ rounds relative to the seed corpus size $N_0$ is:

$$A_T = \frac{C_T}{N_0} = \frac{mrp}{N_0} \sum_{\tau=0}^{T} N_\tau. \tag{3}$$

Substituting (1) and using the geometric sum $\sum_{\tau=0}^{T} (1-\sigma)^\tau = \frac{1 - (1-\sigma)^{T+1}}{\sigma}$:

$$\sum_{\tau=0}^{T} N_\tau = (T+1) P - (P - N_0) \cdot \frac{1 - (1-\sigma)^{T+1}}{\sigma}. \tag{4}$$

The break-even condition against direct fine-tuning on solutions follows from comparing amplification factors. Direct fine-tuning produces exactly $1$ usable supervision example per machine-checked solution. The loop is worth its additional reverse-engineering cost only if its clean yield per solved problem exceeds $1$:

$$A = mrp > 1 \quad \Longleftrightarrow \quad p > \frac{1}{mr}. \tag{5}$$

Equation (5) is evaluated numerically in Section 4.3.

### 3.5 Model-generated fraction

The fraction of the corpus at round $t$ that was produced by the model itself (rather than supplied in the seed) is:

$$f_t = 1 - \frac{N_0}{N_t}. \tag{6}$$

This quantity governs error-compounding risk: although each new solution is machine-verified for soundness (the Lean gate of [1], with $\mathsf{sorry}$ and $\mathsf{admit}$ excluded), the ideas extracted from model-generated solutions inherit the idiosyncrasies of model-generated proofs, and the idea labels produced by reverse-engineering are noisy at rate $1-p$ regardless of provenance.

### 3.6 Assumption register

All numerical results below are projections under the following assumptions, chosen as illustrative mid-range values because the abstracts of [1], [2] state no empirical numbers: $P = 10^4$ problems in the pool, a plausible size for a formalized statement collection in one domain and small relative to the $10^7$-example releases reported by [8]; $N_0 = 10^3$ solved problems in the seed corpus, one tenth of the pool so that the loop has room to grow; $m = 5$ extractable ideas per solution, a mid-range count for reusable intermediate steps in a proof; $r = 0.6$ extraction recall, meaning the reverse-engineering capability recovers three of five ideas; $p = 0.8$ extraction precision, meaning four of five recovered ideas are judged correct and relevant; and $\sigma = 0.1$ per-round solve rate on previously unsolved problems, a conservative starting competence. Each value is an assumption, not a measurement, and Section 6 lists the sensitivity of the results to each.

## 4. Analysis

### 4.1 The growth trajectory

With $P = 10^4$, $N_0 = 10^3$, and $\sigma = 0.1$, the deficit is $D_0 = P - N_0 = 9000$ and decays as $D_t = 9000 \cdot 0.9^t$. Applying Equation (1), $N_t = 10^4 - 9000 \cdot 0.9^t$:

- $N_0 = 10^4 - 9000 \cdot 1 = 1000$.
- $N_1 = 10^4 - 9000 \cdot 0.9 = 10^4 - 8100 = 1900$.
- $N_2 = 10^4 - 9000 \cdot 0.81 = 10^4 - 7290 = 2710$.
- $N_3 = 10^4 - 9000 \cdot 0.729 = 10^4 - 6561 = 3439$.
- $N_4 = 10^4 - 9000 \cdot 0.6561 = 10^4 - 5904.9 = 4095.1$.
- $N_5 = 10^4 - 9000 \cdot 0.59049 = 10^4 - 5314.41 = 4685.59$.

Each round adds $\sigma U_t = 0.1 (10^4 - N_t)$ new solved problems: $900$, $810$, $729$, $656.1$, $590.49$ in rounds $1$ through $5$ respectively, a geometric decay at rate $1-\sigma = 0.9$. The round-five corpus of $N_5 = 4685.59$ solved problems is $4.69\times$ the seed corpus, computed as $4685.59 / 1000 = 4.68559$.

The number of rounds to reach a target corpus fraction $\phi$ of the pool follows from $(1-\sigma)^t = (P - \phi P)/(P - N_0)$. For $\phi = 0.9$: $0.9^t = 1000/9000 = 1/9$, so $t = \ln(1/9)/\ln(0.9) = (-2.19722)/(-0.10536) = 20.85$, i.e. $21$ rounds. At $\sigma = 0.1$, saturation is slow: half the pool satisfies $0.9^t = (P - 0.5P)/(P - N_0) = 5000/9000 = 5/9$, so $t = \ln(5/9)/\ln(0.9) = (-0.587787)/(-0.105361) = 5.5788$, i.e. round $6$.

### 4.2 Cumulative amplification

The per-round clean idea amplification is, from Equation (2):

$$A = mrp = 5 \times 0.6 \times 0.8 = 2.4.$$

Each machine-checked solution thus yields on average $2.4$ clean idea-supervision pairs per round of extraction. The cumulative sum of solved problems over rounds $0$ through $5$ is, from Equation (4):

$$\sum_{\tau=0}^{5} N_\tau = 6 \times 10^4 - 9000 \times \frac{1 - 0.9^6}{0.1}.$$

Since $0.9^6 = 0.531441$, we get $\frac{1 - 0.531441}{0.1} = 4.68559$, so:

$$\sum_{\tau=0}^{5} N_\tau = 60000 - 9000 \times 4.68559 = 60000 - 42170.31 = 17829.69.$$

Cross-check by direct addition: $1000 + 1900 + 2710 + 3439 + 4095.1 + 4685.59 = 17829.69$, matching. The cumulative clean idea pairs are:

$$C_5 = mrp \sum_{\tau=0}^{5} N_\tau = 2.4 \times 17829.69 = 42791.256 \approx 42791.26.$$

The cumulative amplification relative to the seed corpus is, from Equation (3):

$$A_5 = \frac{C_5}{N_0} = \frac{42791.256}{1000} = 42.791256 \approx 42.79\times.$$

Five rounds of the loop therefore manufacture the equivalent of roughly $42.79$ seed corpora of clean idea supervision, under the stated assumptions.

### 4.3 Break-even against direct fine-tuning

Direct fine-tuning on machine-checked solutions yields exactly $1$ usable supervision example per solution. From Equation (5), the loop beats this when $mrp > 1$. At $m = 5$ and $r = 0.6$:

$$p > \frac{1}{mr} = \frac{1}{5 \times 0.6} = \frac{1}{3} \approx 0.3333.$$

The stated $p = 0.8$ exceeds this threshold by a factor of $2.4$, since $A = 2.4 > 1$. The margin is the ratio $A/1 = mrp$, so the loop tolerates a precision as low as $0.3333$ before its clean yield per solution falls below direct fine-tuning. Equivalently, at $p = 0.8$ the loop tolerates recall