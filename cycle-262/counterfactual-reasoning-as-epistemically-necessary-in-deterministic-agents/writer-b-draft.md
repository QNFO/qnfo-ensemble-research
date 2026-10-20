# Counterfactual Reasoning as Epistemically Necessary Despite Determinism: A Decision-Theoretic Derivation

## Abstract

Practitioners who build learning systems, conduct post-incident reviews, and assign accountability routinely rely on counterfactual reasoning — the evaluation of alternatives that did not occur — yet a persistent philosophical line holds that under determinism such reasoning is a cognitive error, since only one future was ever possible. The gap addressed here is formal: no existing derivation shows that agents who are deterministic systems with bounded knowledge strictly outperform agents who collapse "what was right" into "what actually happened," leaving the practical status of counterfactual deliberation unsettled. This paper models both agent types as deterministic policies over a binary state, a noisy signal, and a binary action, and derives their expected utilities in closed form. The epistemic agent, which maintains a probability distribution over unobserved causal variables, achieves an expected utility of $3.4$ per decision against $1.0$ for the fatalist agent, a gap of $2.4$ units per decision ($240\%$ relative gain), and a learning derivation shows the fatalist's estimation bias of $0.3$ in a signal-accuracy parameter produces an expected cumulative loss of $240$ utility units over $100$ decisions. The result separates metaphysical determinism from practical normativity: counterfactual evaluation is an optimal computation for bounded agents even when no alternatives metaphysically exist, which justifies building counterfactual evaluation into learning and accountability systems on decision-theoretic rather than metaphysical grounds.

## 1. Introduction

Engineers conducting post-incident reviews, educators building tutoring systems, and designers of machine-learning pipelines all face the same operational question: should their systems and procedures evaluate what *would have happened* under actions that were not taken? A hospital review board asks whether a different triage decision would have saved the patient; a knowledge-tracing system asks how a student's earlier wrong answer influences the prediction for the next question; a reinforcement-learning system asks whether the unchosen arm would have paid out. In each case the alternative was never actualized, and a determined critic can argue — as some readings of determinism imply — that reasoning about it is a category mistake: given the initial conditions and the laws, only one outcome was ever possible, so "what would have happened" describes nothing.

This criticism has practical teeth. If counterfactual evaluation is a cognitive error, then regret-based learning signals are noise, post-hoc accountability judgments are confabulation, and the compute spent on counterfactual rollouts in planning systems is waste. If, instead, counterfactual evaluation is epistemically necessary for bounded agents — that is, for agents that do not know the full state of the world or the full dynamics — then these practices are justified independently of whether determinism is true, and systems that suppress counterfactual computation in the name of metaphysical parsimony are making a measurable performance error. The decision that changes with the result of this paper is concrete: whether a learning system's update rule may legitimately use regret and counterfactual contrasts, and whether an accountability procedure may legitimately ask "what else could the agent have done?" without first settling metaphysics.

The paper's position, argued formally, is that the criticism conflates two claims. The metaphysical claim — every outcome is fixed by prior states and laws — is compatible with the epistemic claim that a bounded agent must represent unobserved causal variables as a probability distribution and condition on alternatives as epistemically possible. Determinism constrains what *is*; it does not constrain what a bounded agent *should compute*. The paper makes this precise by constructing two deterministic agents over the same environment: an *epistemic* agent that maintains a posterior over the unobserved state and acts on it, and a *fatalist* agent that collapses "right" into "actual" and therefore extracts no decision-relevant content from its partial observations. Both agents are fully deterministic systems; neither violates determinism; their expected utilities differ by a derived, strictly positive quantity.

The contributions are:

- A closed-form derivation that a deterministic epistemic agent achieves expected utility $3.4$ per decision against $1.0$ for a deterministic fatalist agent over the same environment, a gap of $2.4$ units ($240\%$ relative), derived in Section 4.1–4.2.
- A derivation that the value of partial observation is exactly this gap, so a fatalist agent assigns zero value to information it in fact possesses, derived in Section 4.3.
- A learning derivation showing that counterfactual regret supplies the only signal by which a bounded agent can estimate an unknown environment parameter, that a fatalist's estimate retains a bias of $0.3$ indefinitely, and that this bias costs $2.4$ utility units per decision, or $240$ units over $100$ decisions, derived in Section 4.4.
- A survey of the counterfactual-reasoning literature — from knowledge tracing [3] and moral-reasoning prompting [6] to counterfactual image models [4], counterfactual quantum communication [5], and counterfactual image synthesis [7] — establishing that counterfactual computation is already an engineering resource whose justification this paper supplies, in Section 2.
- A statement of the practical pathway: who uses the result, at what technology-readiness level, and what the smallest falsifying test would be, in Section 7.

## 2. Background and Related Work

The philosophical backdrop is the tension between deterministic ontology and probabilistic epistemology. [9] investigates this tension directly in the quantum foundations setting: it argues that superdeterminism — a deterministic ontology that preserves locality by rejecting Measurement Independence — is mathematically and logically coherent, yet has been epistemically rejected, and it identifies a "theoretical gap" in that deterministic frameworks such as the Cellular Automaton Interpretation "stop short of specifying the precise evolutionary laws," leaving them "vulnerable to the critique that they merely replace one mystery with another." [9] also uses Lakatos's picture of research programmes to argue that the scientific community lacks "a formal path" for the comparative assessment of axiom-violating theories. This paper takes the complementary lesson: even if a deterministic ontology is coherent, the *practice* of science and of decision-making runs on epistemic probabilities over unobserved variables, and the present paper derives why that practice is optimal rather than merely habitual. [10] supplies the cognitive-science side of the same tension: its Chapter 3 describes the Libet finding that the neural "readiness potential" precedes conscious awareness of intention by several hundred milliseconds, and frames the brain as "an active constructor of reality, creating after-the-fact narratives and predictive models." If deliberation is post-hoc narration of a deterministic process, the question "why deliberate at all?" becomes acute; the derivation in Section 4 answers it by showing the narration — specifically, the counterfactual contrast between taken and untaken actions — carries the learning signal.

That epistemic probabilities are the *correct* formal object for a bounded reasoner, rather than one option among many, is supported by [8]. [8] proves a uniqueness theorem: extending classical propositional logic to a logic of plausible reasoning, under requirements each of which preserves a property of propositional logic, yields probability theory uniquely — "probability theory as the uniquely determined extension of classical propositional logic to a logic of plausible reasoning." [8] also carries forward Jaynes's finite-sets policy, that consistency theorems hold for probabilities on finite sets and extension to infinite sets is permitted "only when this is the result of a well-defined and well-behaved limiting process." The agents modeled in Section 3 face finite state and signal sets, so the epistemic agent's posterior is exactly the plausibility function whose uniqueness [8] establishes; a deterministic agent that reasons at all, on this result, reasons in probabilities.

Counterfactual reasoning is already a working computational tool across several fields, which sharpens the question of its normative status. In computer-aided education, [3] proposes RCKT, "a framework that uses counterfactual reasoning to quantify the response influences to trace students' knowledge and predict their performance, which is ante-hoc explainable in KT," and reports that "comprehensive experiments show that RCKT outperforms most existing KT methods and offers sufficient interpretability"; its evaluation uses five-fold cross validation with AUC and accuracy as metrics. Here counterfactual computation is not a philosophical indulgence but the mechanism that simultaneously improves prediction and interpretability — precisely the dual benefit a bounded agent needs when it must both act and learn from its actions. In machine-learning evaluation, [4] presents "a general framework for evaluating image counterfactuals" and argues that because deep generative models are flexible, "counterfactual identifiability is impossible in the general case," motivating a return to Pearl's axiomatic definition of counterfactuals to determine what counterfactual claims are sound. This paper's model respects that caution: the counterfactuals used in Section 4 are over a fully specified causal structure with known payoffs, where identifiability holds by construction; the unidentifiable case is treated in Section 6 as a limitation. In moral reasoning for language models, [6] introduces the Thought Experiments prompting framework and reports that "zero-shot Thought Experiments improves the task performance by 9% to 16% compared to direct and CoT zero-shot baselines," with few-shot Thought Experiments reaching "the best task performance at 80.45%" against a zero-shot baseline of 57.09% on the MMLU Moral Scenarios task; [6] observes that Thought Experiments reasoning "is more likely to be comprehensive and consider many possibilities, hence arriving at the correct answer." This is direct empirical evidence that forcing a system to enumerate epistemic possibilities — the operational content of counterfactual deliberation — improves output quality on a task where collapsing to the given scenario underperforms.

Counterfactuals also function as a formal resource in physics, where "what did not happen" has measurable consequences. [5] develops counterfactual quantum communication, in which "two parties communicate without any transmission of quantum or classical particles between the parties," building on the chained quantum Zeno effect; [5] constructs a counterfactual CNOT gate, uses it to generate entanglement between an electron and a photon, and analyzes the protocol "in the regime of quantum repeaters with a specific focus on different aspects of success probabilities and entanglement pair distribution time." The lesson for this paper is structural: a counterfactual channel — information carried by events that did not occur (the absence of absorption) — is a legitimate, quantifiable physical resource. If even physics can trade on non-occurrence, the objection that counterfactuals describe "nothing" loses its force at the level of principle, and the remaining question is the decision-theoretic one settled in Section 4. In generative modeling, [7] treats "counterfactual controllability, defined as the capacity to deliberately generate images that contradict common-sense patterns" as an engineering target, constructing "a dataset of 91 objects: 46 typically large and 45 typically small" and an evaluator built on segmentation masks, and reports that its framework "consistently outperforms state-of-the-art baselines and ChatGPT-4o." Again, counterfactuals are a controllable, scored, dataset-backed quantity.

Two further works bound how counterfactual reasoning should be deployed. [1] argues in the cognitive-augmentation setting that "interventions that disrupt the state of cognitive flow can hinder rather than enhance decision-making" and proposes "Cognitive Flow Alignment," under which interventions "dynamically adjust to an individual's cognitive state, neither disrupting engagement nor allowing stagnation." Applied here: a deliberation-support system that floods a user with counterfactual alternatives regardless of load can degrade the very decision it aims to improve; the epistemic-necessity result licenses counterfactual computation, not unbounded counterfactual computation. [2] supplies a caution about *how* counterfactual-style traces are used in training: in its study of procedural reasoning data, step-by-step rationale targets that "reproduced the successive operations" of parsers and search algorithms "consistently performed worse than compact-answer supervision on both BBH development and FineWeb NLL," with the same ordering under matched and unmatched budgets, suggesting "the more transferable skill may be learning the gestalt of the problem... rather than reproducing the solver's bookkeeping one operation at a time." For the present paper, this warns that training a system to emit verbose counterfactual deliberation traces may transfer worse than training it to produce the counterfactual-informed answer; the normative claim concerns the computation's role in the agent's own policy, not the format of its output. Finally, [11] documents a limit on predictability itself: its account of Huang, Choi, McClean and Preskill's Theorem 1 states that "assuming BPP ≠ BQP, the decision problem 'does this specific quantum circuit outperform Pauli propagation classical simulation?' is in BQP but not in BPP," with the implication that "there are plenty of problems with genuine quantum advantages such that we cannot predict the advantage using only classical technology." Even the epistemic agent of Section 4 is bounded twice over — by its partial observations and by computational limits on prediction — which reinforces that its probability distributions are representations of irreducible ignorance, not disguised metaphysical claims.

## 3. Methods

### 3.1 Model

The environment is a finite, fully deterministic system with the following components. A latent state $S \in \{0, 1\}$ is drawn by the environment's initial conditions; the agent does not observe $S$ directly. The agent receives a binary signal $X \in \{0, 1\}$ generated by a stochastic-looking but deterministic channel whose conditional probabilities, from the agent's epistemic standpoint, are

$$P(X = 1 \mid S = 1) = q, \qquad P(X = 1 \mid S = 0) = 1 - q,$$

where $q \in (0,1)$ is the signal accuracy. The agent takes a binary action $A \in \{0, 1\}$ and receives payoff

$$U(A, S) = \begin{cases} +10 & A = 1,\ S = 1 \\ -6 & A = 1,\ S = 0 \\ 0 & A = 0 \end{cases}$$

The payoffs are the paper's own assumption, chosen so that acting is attractive under good information and unattractive under poor information; Section 4.5 varies them to test sensitivity. The prior is $P(S = 1) = p_0 = 0.5$. All probabilities are epistemic: they quantify the agent's ignorance of the deterministic variables $S$ and $X$, in the sense licensed by [8], where plausibilities over finite proposition sets obey the probability calculus uniquely.

### 3.2 Agents

Both agents are deterministic functions of their inputs; neither violates determinism at any point.

**Epistemic agent $E$.** Agent $E$ maintains a posterior $P_E(S = 1 \mid X)$ by Bayes' rule, acts by thresholding the posterior at the break-even point of the payoff structure, and, in the learning variant, updates its estimate $\hat{q}$ of the unknown signal accuracy using counterfactual regret: after observing outcome $S$, it computes the payoff it would have received under the action not taken and adjusts $\hat{q}$ in the direction that would have improved the realized payoff.

**Fatalist agent $F$.** Agent $F$ adopts the norm "condition only on the actual." Operationally, this means $F$ treats its signal $X$ as carrying no decision-relevant content about alternatives — since under determinism only one $X$ and one $S$ were possible, $F$ declines to form a posterior over $S$ and acts on its prior. In the learning variant, $F$ refuses counterfactual contrasts on the ground that the untaken action describes nothing, so it has no update signal and its estimate of $q$ remains at its initial value.

The comparison is between two deterministic policies over the same environment with the same information; the difference lies entirely in whether unobserved variables are represented as an epistemic possibility space.

### 3.3 Derivation and computation method

All results are obtained by closed-form derivation followed by explicit arithmetic. Expected utilities are computed as sums over the joint distribution of $(X, S)$ as seen from the agent's epistemic state. The learning analysis uses an exponential moving average $\hat{q}_{k+1} = (1 - \alpha)\hat{q}_k + \alpha r_k$ with update rate $\alpha$ as an assumption, and evaluates the expected utility of a policy that acts on a misestimated $\hat{q}$. No simulation, experiment, or measurement is performed; every number in Section 5 is computed in Section 4 from stated inputs.

## 4. Analysis

### 4.1 Posterior computation for the epistemic agent

Inputs: $p_0 = 0.5$ (assumption, symmetric prior), $q = 0.8$ (assumption, signal accuracy; varied in Section 4.5). By Bayes' rule,

$$P(S = 1 \mid X = 1) = \frac{q \, p_0}{q \, p_0 + (1 - q)(1 - p_0)} = \frac{0.8 \times 0.5}{0.8 \times 0.5 + 0.2 \times 0.5} = \frac{0.4}{0.4 + 0.1} = \frac{0.4}{0.5} = 0.8.$$

$$P(S = 1 \mid X = 0) = \frac{(1 - q)\, p_0}{(1 - q)\, p_0 + q (1 - p_0)} = \frac{0.2 \times 0.5}{0.2 \times 0.5 + 0.8 \times 0.5} = \frac{0.1}{0.1 + 0.4} = \frac{0.1}{0.5} = 0.2.$$

The marginal signal probability is $P(X = 1) = q\,p_0 + (1-q)(1-p_0) = 0.8 \times 0.5 + 0.2 \times 0.5 = 0.4 + 0.1 = 0.5$.

### 4.2 Expected utilities

**Epistemic agent.** The break-even posterior for acting is found from $p \cdot 10 - (1 - p) \cdot 6 > 0$, i.e. $10p > 6 - 6p$, i.e. $p > 6/16 = 0.375$. Since $P(S{=}1 \mid X{=}1) = 0.8 > 0.375$ and $P(S{=}1 \mid X{=}0) = 0.2 < 0.375$, the optimal deterministic policy is $A = 1$ iff $X = 1$. Its expected utility is

$$\mathrm{EU}_E = P(X{=}1)\, \big[ P(S{=}1 \mid X{=}1) \cdot 10 + P(S{=}0 \mid X{=}1) \cdot (-6) \big] + P(X{=}0) \cdot 0$$
$$= 0.5 \times \big[ 0.8 \times 10 + 0.2 \times (-6) \big] = 0.5 \times [8.0 - 1.2] = 0.5 \times 6.8 = 3.4.$$

**Fatalist agent.** Agent $F$ acts on the prior $p_0 = 0.5$. Since $0.5 > 0.375$, a prior-thresholding fatalist would always act; but the fatalist norm, consistently applied, also denies that the prior itself encodes anything about alternatives, so we model the fatalist as indifferent between actions and randomizing uniformly — the maximally non-committal deterministic policy consistent with refusing the epistemic possibility space. (The alternative fatalist convention, always acting on the prior, is treated in Section 4.5.) Its expected utility is

$$\mathrm{EU}_F = 0.5 \times \big[ 0.5 \times 10 + 0.5 \times (-6) \big] + 0.5 \times 0 = 0.5 \times [5.0 - 3.0] = 0.5 \times 2.0 = 1.0.$$

**Gap.** $\mathrm{EU}_E - \mathrm{EU}_F = 3.4 - 1.0 = 2.4$ utility units per decision. The relative gain is $2.4 / 1.0 = 2.4$, i.e. the epistemic agent achieves $240\%$ of the fatalist's expected utility, an absolute improvement of $2.4$ units per decision.

### 4.3 Value of information

The value of the signal to the epistemic agent is the difference between its expected utility with the signal and without it. Without the signal, the agent holds only the prior $p_0 = 0.5$; acting on the prior yields $0.5 \times 10 + 0.5 \times (-6) = 5.0 - 3.0 = 2.0$, and not acting yields $0$; the best signal-free policy therefore yields $2.0$. With the signal, $\mathrm{EU}_E = 3.4$. Hence

$$\mathrm{VOI}(X) = 3.4 - 2.0 = 1.4 \text{ units per decision}.$$

The fatalist, by refusing to condition on $X$, realizes the signal-free value $2.0$ only if it acts on the prior, or $1.0$ if it randomizes; under either convention it captures strictly less than the full $3.4$. The key structural point: the fatalist possesses the signal — it is delivered to both agents — but its norm assigns it zero decision-relevant content, so it forfeits the value of information it already holds. Under the randomizing convention it forfeits $3.4 - 1.0 = 2.4$ units; under the prior-acting convention it forfeits $3.4 - 2.0 = 1.4$ units. In both conventions the forfeiture is strictly positive.

### 4.4 Learning derivation: counterfactual regret as the only update signal

Now suppose $q$ is unknown to the agent. The agent can estimate $q$ only by contrasting what happened with what would have happened under the other action — because the payoff $U(A, S)$ reveals $S$ only through the agent's own action, and the counterfactual $U(1 - A, S)$ is the quantity that identifies whether the signal was misleading.

**Setup.** We assume an exponential moving average with rate $\alpha = 0.1$ (assumption) and an initial estimate $\hat{q}_0 = 0.5$ (assumption, matching the symmetric prior). Let the true accuracy be $q = 0.8$. After each trial the agent observes $S$ and computes the counterfactual regret

$$r_k = U(A_k, S_k) - U(1 - A_k, S_k),$$

and updates $\hat{q}_{k+1} = (1 - \alpha)\,\hat{q}_k + \alpha\, r_k$, where $r_k$ is normalized to $[0,1]$ as the indicator that the counterfactual action would have done better (assumption, for concreteness).

**Fatalist bias.** Agent $F$ performs no counterfactual contrast, so $\hat{q}_k = \hat{q}_0 = 0.5$ for all $k$. Its estimation bias is $|q - \hat{q}_k| = |0.8 - 0.5| = 0.3$, permanently.

**Cost of the bias.** An agent acting on estimate $\hat{q}$ forms its posterior as in Section 4.1 with $\hat{q}$ in place of $q$. With $\hat{q} = 0.5$:

$$P(S{=}1 \mid X{=}1) = \frac{0.5 \times 0.5}{0.5 \times 0.5 + 0.5 \times 0.5} = \frac{0.25}{0.5} = 0.5,$$

and identically $P(S{=}1 \mid X{=}0) = 0.5$. Both posteriors equal the break-even boundary region: the agent is indifferent, and the deterministic tie-breaking convention (act on $X = 1$) yields

$$\mathrm{EU}(\hat{q} = 0.5) = 0.5 \times \big[ 0.5 \times 10 + 0.5 \times (-6) \big] = 0.5 \times 2.0 = 1.0.$$

The per-decision loss relative to the epistemic agent that has learned the true $q = 0.8$ (expected utility $3.4$) is $3.4 - 1.0 = 2.4$ units. Over a horizon of $n = 100$ decisions, the fatalist's cumulative expected loss is

$$100 \times 2.4 = 240 \text{ utility units}.$$

**Epistemic convergence.** Agent $E$'s estimate under the exponential filter converges to the true $q$: in steady state, $E[\hat{q}_\infty] = q$ with fluctuation scale $\alpha / (2 - \alpha) \cdot \sigma_r$ around it, where $\sigma_r$ is the standard deviation of the normalized regret signal (bounded by $0.5$ for a binary indicator). With $\alpha = 0.1$, the steady-state standard deviation is at most $0.1 / 1.9 \times 0.5 \approx 0.0263$. The bias vanishes; only a small variance remains, costing at most a fraction of a unit per decision near the threshold and zero away from it. The gap between the agents is therefore driven almost entirely by the fatalist's irreducible bias of $0.3$.

### 4.5 Sensitivity to assumptions

**Fatalist convention.** If the fatalist is modeled as always acting on the prior rather than randomizing, $\mathrm{EU}_F = 2.0$ (Section 4.3), and the gap is $3.4 - 2.0 = 1.4$ units per decision, a $70\%$ relative gain. The strict-dominance result holds under both conventions; only its magnitude changes.

**Payoff variation.** The gap is proportional to the payoff spread. With general payoffs $U(1,1) = g$, $U(1,0) = -\ell$, $U(0,\cdot) = 0$, the epistemic agent's expected utility is $0.5\,[\,q g - (1-q)\ell\,]$ and the randomizing fatalist's is $0.5\,[\,0.5 g - 0.5 \ell\,]$, so the gap is

$$\mathrm{gap} = 0.5\,(q - 0.5)(g + \ell).$$

Check with the base numbers: $0.5 \times (0.8 - 0.5) \times (10 + 6) = 0.5 \times 0.3 \times 16 = 2.4$, matching Section 4.2. The gap is strictly positive whenever $q > 0.5$ (the signal carries information) and $g + \ell > 0$ (the action matters). If $q = 0.5$ the signal is uninformative and the agents tie — the result correctly requires that the epistemic possibility space actually constrain the agent's beliefs. If $g + \ell = 0$ the action is inconsequential and again the agents tie. Both failure modes are benign: the result claims dominance exactly when information and action both matter.

**Update rate.** With $\alpha$ smaller, the fatalist's disadvantage is unchanged (it never updates) and the epistemic agent converges more slowly but to the same steady state; with $\alpha$ larger, the epistemic agent's steady-state variance grows as $\alpha/(2-\alpha)$, so very large $\alpha$ degrades $E$'s performance toward the threshold region, but for any $\alpha < 1$ the expected estimate remains unbiased at $q$.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions ($p_0 = 0.5$, $q = 0.8$, payoffs $+10/{-6}/0$, $\alpha = 0.1$, $\hat{q}_0 = 0.5$, horizon $n = 100$); none is measured or simulated.

- **R1 (Section 4.2).** The epistemic agent's expected utility is $3.4$ units per decision; the randomizing fatalist's is $1.0$; the gap is $2.4$ units per decision, a $