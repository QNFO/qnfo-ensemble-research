# The Capability–Availability Mismatch: Three-State Tool Semantics and Forced-Halt Conditions in LLM Agent Protocols

## Abstract

Agent protocols written for large language models (LLMs) typically assume a binary world: a tool is either available to the agent or it is not. Real deployments exhibit a third state: the capability exists in the toolset but is contextually disabled by policy, budget, or routing. We formalize this capability–availability mismatch. We model tool state as a pair (capability, per-context permission), define protocol compliance as a predicate over these states, and ask which protocol designs remain well-defined when the third state occurs. Two results follow. First, a combinatorial result: a binary-state protocol with $k$ permission-gated tools is defined on only a $2^{k}/3^{k}$ fraction of the true state space; for $k=5$ this is $32/243 \approx 0.132$, and for $k=10$ the three-state space is $59049/1024 \approx 57.7$ times larger than the binary model assumes. Second, a computability result: deciding whether an arbitrary protocol loop halts with a compliant action in the disabled state is undecidable, by reduction from the halting problem in the style of Rice's theorem. Under stated assumptions we project a catch-22 overhead of $0.4$ cost units per task, or $4.0 \times 10^{5}$ units over $10^{6}$ tasks, removable by explicit disabled-state signaling at a break-even signaling cost of $0.4$ units per task. The practical consequence is a design rule: agent instruction languages must signal the disabled state explicitly, or they force agents to choose between mandatory halting and silent rule violation.

## 1. Introduction

Teams deploying LLM agents in production face a failure mode that no amount of model improvement removes. An agent is instructed, in natural language, to "use the live search tool when answering factual questions" and to "never simulate or fabricate tool output." The tool exists in the agent's toolset, the model can call it, and the calling code works. But in a particular context — a rate-limited session, a tenant with the tool switched off by policy, a routing tier where the tool's budget is exhausted — the platform has disabled the tool without removing it from the toolset. The agent now sits in a catch-22 constructed entirely by the protocol's wording: if it honestly self-assesses, it concludes the tool is "not available," and the mandate-plus-prohibition pair forces it to halt a task it could in principle execute; if it proceeds, it either fabricates a "live" fetch (violating the prohibition) or claims compliance it cannot verify. The cost is concrete: tasks halt that should complete, or silent rule violations accumulate that no compliance checker catches, because the checker shares the same binary assumption the protocol text does.

This matters to three groups today. Protocol and framework authors who write system prompts and tool schemas must decide what their instructions mean in the disabled state, and currently have no vocabulary for it. Platform engineers who disable tools per tenant or per budget envelope must predict agent behavior after the switch, and currently cannot, because the agent's decision procedure was never specified for that state. Auditors and evaluators who score agent compliance must decide whether a fabricated fetch in the disabled state is a model failure or a specification failure, and currently have no principled answer. If the analysis in this paper holds, a small change in protocol design — explicit signaling of the disabled state, and compliance predicates defined over three states rather than two — removes the catch-22 by construction rather than by prompt tuning.

The halting behavior of LLM agents is already known to be a first-order cost driver, which makes any *forced* halt condition worth formalizing. Retrieval-augmented search agents exhibit the mirror-image pathology: a 3B Self-Ask agent runs to its search budget on 78–88% of questions instead of halting on its own, and a verification-aware stopping policy cuts loop counts by 20–45% while largely preserving exact-match scores [3]. Reasoning models overthink by a wide, stable margin: a probe-based confidence estimate saturates at a median of about 1,650 think-tokens while the same rollouts run to a median of about 3,700, a matched factor of 2.24 [4]. These works study agents that fail to stop when they should. This paper studies the complementary pathology: agents forced to stop, or forced to violate, by a specification that cannot represent the state they are in. The mismatch is structurally analogous to operator mismatch in computational imaging, where a reconstruction pipeline that assumes a forward operator differing from physical reality in eight parameters loses 20.58 dB, and mismatched-operator scenarios erase the roughly 10 dB ideal-condition advantage of deep methods over classical ones [6]: in both cases the deployed artifact is evaluated against a state model that the environment does not honor.

We treat the question at two levels. At the specification level, we give a three-state semantics for tool availability, define protocol compliance as a predicate over that semantics, and characterize which protocol designs are well-defined in all three states. At the computability level, we show that a natural decision problem about protocol loops — whether the loop halts with a compliant action in the disabled state — is undecidable, using the reduction strategy that establishes the undecidability of inner alignment via Rice's theorem [7]. Undecidability results of this shape have precedent in physical domains: the quantum measurement occurrence problem is undecidable for $K=9$ outcomes and $d=15$ dimensions even though its classical analogue is decidable [1], and supersymmetry breaking in 2d $\mathcal{N}{=}(2,2)$ Wess-Zumino models is undecidable by encoding arbitrary Turing machines into the class of Lagrangians [5]. In each case the lesson is the same and applies here: a specification that looks complete can silently inherit the halting problem.

The contributions are:

- A three-state formalization of tool availability (capability vs. per-context permission) and a definition of protocol compliance over that semantics, with a well-definedness criterion for protocol designs (Section 3).
- A combinatorial derivation showing a binary protocol with $k$ permission-gated tools is defined on a $2^{k}/3^{k}$ fraction of the true state space, computed as $32/243 \approx 0.132$ for $k=5$, and a state-space ratio of $59049/1024 \approx 57.7$ for $k=10$ (Section 4.1).
- An undecidability proof for the protocol compliance-halting problem, by contradiction following the Rice's theorem reduction of [7] (Section 4.2).
- A projected catch-22 overhead of $0.4$ cost units per task under stated assumptions, with a signaling break-even threshold of $0.4$ units per task (Section 4.3).
- A design rule for agent instruction languages — explicit disabled-state signaling plus three-state compliance predicates — and the smallest experiment that would falsify or de-risk it (Sections 5 and 7).

## 2. Background and Related Work

**Undecidability in measurement and physics.** The quantum measurement occurrence problem asks whether, in a tree of repeated nonprojective measurements with $K$ outcomes and Kraus operators $A_1,\dots,A_K$, there exists an outcome path with zero probability — figuratively, whether an empty port exists through which the particle never flies. The problem is undecidable for $K=9$ and $d=15$, as a consequence of the undecidability of the matrix mortality problem for $3\times 3$ integer matrix semigroups generated by 8 matrices, itself reduced from the post correspondence problem [1]. Two features of that result transfer to our setting. The classical analogue (a stochastic-matrix version of the same question) is decidable, so the gap between the modeled dynamics and the richer dynamics is exactly what introduces undecidability; and mild restrictions, such as trace-preserving channels bounded via the quantum Wielandt theorem, restore efficient decidability. Our three-state semantics plays the role of the richer dynamics: protocols specified over two states face decision questions that the two-state model itself does not contain. The encoding strategy is also shared: undecidability of supersymmetry breaking in 2d $\mathcal{N}{=}(2,2)$ Wess-Zumino models is obtained by devising a way to encode arbitrary Turing machines into the class of systems under consideration [5], and the same paper's discussion of proof verifiers — programs that check purported proofs of a statement in a theory — anticipates the verification-based reading of compliance we adopt here.

**Undecidability of alignment properties.** The closest formal antecedent to our computability result is the proof that the inner alignment problem — whether an arbitrary AI model satisfices a non-trivial alignment function $J_v(i,o)$ of its outputs given its inputs — is undecidable, established by Rice's theorem and by an explicit contradiction construction: assuming a Turing machine $M_P$ that decides the property, one builds a Turing machine $M_H$ that decides the halting problem, contradicting its undecidability [7]. The same work delineates the escape route we later rely on for practice: while the property cannot be ascertained for arbitrary systems, it can be ascertained for an enumerable set of architecturally designed systems, built from an initial set of finite models and operations that preserve the property. Our Section 6 uses this distinction to separate what is undecidable in principle (arbitrary protocol text) from what is decidable by construction (protocols whose compliance predicates are syntactically restricted).

**Halting and stopping in deployed agents.** Empirically, agent halting is already a measurable, expensive behavior. HALT frames stopping as evidence coverage rather than generator confidence: a verifier matches every expected reasoning hop to cumulative evidence, and the agent stops when coverage is complete. With gold claims on a Self-Ask 3B agent, HALT reduces loop counts by 37% on 2Wiki, 45% on HotpotQA, and 20% on MuSiQue, with exact-match changes between $-0.9$ and $+1.5$ percentage points; the HotpotQA non-inferiority test fails with a 95% CI of $[-2.6,+0.8]$ pp crossing the $-2$ pp margin, and under open-corpus retrieval shift the fire rate drops from 67.6% to 6.4% on HotpotQA and to 2.4% on Bamboogle [3]. The authors explicitly scope their claims to controlled closed-pool retrieval. Two points bear on our formalization: halting policies are measurable and tunable, and a halting policy's behavior degrades predictably when the environment's retrieval state differs from the state the policy was specified over — a state-mismatch effect, not a model-capability effect. The Halt Vector work internalizes a causal stopping direction at layer 18 into the weights, yielding a per-problem self-halt trained from 24 problems that removes about 24% of thinking at held accuracy; notably, outcome-level length penalties only trim the longest tails and do not move the internal answerable point, and the stop-and-commit tokens are about 0.34% of the token loss, so plain fine-tuning leaves length unchanged [4]. This establishes that halting behavior is causally steerable but not specifiable by a global scalar — supporting our claim that halting semantics must be represented structurally in the protocol, not incentivized loosely.

**Mismatch between assumed and actual state.** InverseNet benchmarks operator mismatch in compressive imaging: when the assumed forward operator deviates from physical reality in eight parameters, EfficientSCI loses 20.58 dB; under mismatched operators all methods converge to 20.40–21.88 dB on CASSI, erasing the roughly 10 dB ideal-condition advantage of deep learning over classical methods; CACTI suffers degradations up to 20.6 dB; and mask-oblivious architectures such as HDNet show zero oracle recovery ($\Delta_{\text{rec}}=0.00$ dB) while operator-aware ones such as PnP-HSICNN recover with ratio $\rho=56.8\%$ [6]. The structural lesson for agent protocols is direct: an artifact specified against a state model the environment violates fails catastrophically and non-uniformly, and recovery requires the specification to be aware of the true state — which is precisely what disabled-state signaling provides.

**Capability as a substrate property.** The categorical formalization of the "substrate is the algorithm" thread defines a physical substrate as an object of a compact closed monoidal category whose morphisms are the physically realizable transformations, and a computation as a morphism realizable by the substrate; a property is intrinsically protected iff it is invariant under the full endomorphism monoid $\mathrm{End}(S)$ [11]. The conjecture Capability$(S) \sim \mathrm{End}(X_S)$ makes capability a property of the substrate's process structure rather than of an external label. This supports our separation of capability (what the toolset can do, a structural property) from permission (what a context allows, an external constraint): conflating them is the category error our three-state semantics repairs.

**State-space and verification-cost growth.** The distinction-space framework defines a distinction space $D_N = (S_N, d_u)$ with $S_N = \{0,1\}^N$, realizes it as a $b$-ary tree of depth $L$ with $N = L \log_2 b$ and $|S_N| = 2^N$, and admits as existence predicates exactly the subsets definable by finite Boolean formulas over the $N$ base coordinates, of which there are $2^{2^N}$ extensionally distinct ones [8]. We reuse this move: an agent's context state is a distinction record, and a protocol's compliance predicate is admissible only if it is definable over the coordinates the protocol actually distinguishes. A binary protocol does not distinguish the disabled state, so predicates that depend on it are inadmissible in its vocabulary — the formal core of the catch-22. On the systems side, the agentic-collapse analysis identifies an "Orchestration Penalty" — a factorial increase in verification complexity in multi-step loops — and a structural latency problem in which the velocity of agentic action $\phi$ outpaces the latency of deliberate verification $\tau_{\mathrm{sys2}}$ [9]. Forced halts add to verification latency without adding verification value, so the catch-22 compounds an already-binding constraint. Finally, deployment economics make protocol-level fixes attractive relative to model-level ones: high-concurrency LLM serving is bottlenecked by KV cache memory overhead, and structural changes (an adaptive GQA-to-MLA transition that limits Llama3-8B perplexity degradation from 6.1 to 12.9 versus 25.8 for the baseline, a 65% reduction in degradation) are what move concurrency, not prompt text [2]. Our cost projection in Section 4.3 uses the same per-instance accounting frame as the bottling reanalysis, which derives break-even workloads $n^{*}_\rho \approx 1.22\, C_0/c_L$ and shows that zero-shot rank cannot select a bottling agent (48 of 60 sub-floor runs, binomial tail $\approx 1.3\times 10^{-65}$; 31 of 60 against the distillation baseline, $z \approx 0.258$, $p \approx 0.80$) [10] — a reminder that capability rankings measured in one state do not transfer to another, which is the empirical shadow of the capability–permission distinction.

## 3. Methods

### 3.1 Three-state tool semantics

Fix a finite set of tools $T = \{t_1, \dots, t_n\}$ and a set of contexts $C$. For a tool $t$ and context $c$ we define two independent bits:

- $\mathrm{Cap}(t) \in \{0,1\}$: the tool is present in the agent's toolset and the calling path is functional. This is a structural property of the deployment, in the sense that capability is determined by the substrate's realizable processes rather than by an external label [11].
- $\mathrm{Perm}(t, c) \in \{0,1\}$: policy, budget, or routing permits invoking $t$ in context $c$.

The *effective availability* is the conjunction:

$$
\mathrm{Avail}(t, c) \;=\; \mathrm{Cap}(t) \wedge \mathrm{Perm}(t, c).
$$

Each tool–context pair therefore occupies one of three *distinguishable* states, which we name:

$$
\sigma(t,c) \in \{\textsf{ABSENT}, \textsf{ENABLED}, \textsf{DISABLED}\},
$$

with $\textsf{ABSENT} = (\mathrm{Cap}=0, \mathrm{Perm}=0)$, $\textsf{ENABLED} = (1,1)$, and $\textsf{DISABLED} = (1,0)$. The state $(0,1)$ is excluded by construction: permission without capability is not a state the platform can occupy, since a tool that does not exist cannot be permitted. (We assume platforms do not advertise permissions for nonexistent tools; if they do, a fourth state appears and only strengthens the mismatch results below.)

The binary model underlying current protocol text collapses $\textsf{ABSENT}$ and $\textsf{DISABLED}$ into a single "unavailable" value. The distinction-space framing makes the cost of that collapse precise: a distinction is a binary partition of the observer's state space that the observer can reliably re-identify, and admissible predicates are exactly those definable by finite Boolean formulas over the distinguished coordinates [8]. A protocol whose vocabulary distinguishes only $\mathrm{Avail}$ has one coordinate; a three-state protocol distinguishes $\mathrm{Cap}$ and $\mathrm{Perm}$ separately and has two. Predicates that need to condition on $\mathrm{Perm}$ alone — for example, "report the tool as disabled and continue without it" — are inadmissible in the binary vocabulary, not because they are hard to evaluate but because the vocabulary cannot express them.

### 3.2 Protocols and compliance

A *protocol* $\Pi$ is a pair $(\iota, \chi)$ where $\iota$ is the instruction text handed to the agent and $\chi$ is the compliance predicate used by an external checker (which may be the agent itself in a self-audit step). We restrict attention to the clause pattern that motivates this paper, which we call a *mandate–prohibition pair*:

- $\mathrm{Mandate}(t)$: the protocol requires that task-relevant facts be established by a live invocation of $t$.
- $\mathrm{Prohibit}(t)$: the protocol forbids simulating, fabricating, or asserting the content of $t$'s output without a live invocation.

Given a state $\sigma(t,c)$ and an agent action trace $\tau$, the compliance predicate evaluates to $\chi(\Pi, \sigma, \tau) \in \{0,1\}$. A protocol is *well-defined* on a state $s$ if, for every trace $\tau$ available to the agent in state $s$, exactly one of the following holds and the protocol text determines which: (i) $\tau$ is compliant, (ii) $\tau$ is non-compliant, or (iii) the protocol prescribes halting as the compliant action. A protocol is *well-defined simpliciter* if it is well-defined on every state in its state semantics.

### 3.3 The catch-22 as a specification defect

In state $\textsf{ENABLED}$, the mandate–prohibition pair is satisfiable: invoke $t$ live. In state $\textsf{ABSENT}$, halting with an explicit "tool unavailable" report is the compliant action under any reasonable reading. In state $\textsf{DISABLED}$, the pair is unsatisfiable under the binary reading:

- If the agent reads "unavailable" (the only unavailable-value the binary vocabulary has) and halts, it halts a task that is executable in principle — a *forced halt*. The mandate is violated in spirit: the protocol demanded a live fetch and the fetch was possible.
- If the agent reads its own capability as availability and attempts the call, the call fails or is refused; any subsequent assertion of the tool's content is fabricated — a *silent violation* of $\mathrm{Prohibit}(t)$.
- If the agent fabricates a successful "live" fetch without calling, it violates $\mathrm{Prohibit}(t)$ directly.

Formally: under the binary semantics, no trace in state $\textsf{DISABLED}$ satisfies both $\mathrm{Mandate}(t)$ and $\mathrm{Prohibit}(t)$, so $\chi$ is forced either to declare every trace non-compliant (the task can never succeed, a de facto forced halt) or to declare some fabricating trace compliant (the checker is unsound). Under the three-state semantics, a third trace class exists — report $\textsf{DISABLED}$, degrade gracefully, continue without $t$ — and the protocol author can define $\chi$ to accept it. The catch-22 is therefore not a model failure; it is a defect of the specification's state vocabulary, in the same sense that a reconstruction pipeline specified against a wrong forward operator fails when the environment deviates from the assumption [6].

### 3.4 Protocol classes

We classify protocols by their state semantics and their treatment of $\textsf{DISABLED}$:

- **Class B (binary):** $\iota$ and $\chi$ reference only $\mathrm{Avail}$. Well-defined on $\textsf{ABSENT}$ and $\textsf{ENABLED}$; not well-defined on $\textsf{DISABLED}$.
- **Class S (signaling):** the platform emits an explicit $\textsf{DISABLED}$ signal, $\iota$ instructs the agent to honor it, and $\chi$ accepts the degrade-and-continue trace in state $\textsf{DISABLED}$. Well-defined on all three states.
- **Class R (restricted):** protocols whose compliance predicates are drawn from a syntactically restricted, property-preserving grammar, in the spirit of the axiomatically enumerable systems for which alignment properties are ascertainable [7]. Well-definedness for Class R is decidable by construction; Section 4.2 shows why the restriction is necessary.

### 3.5 Decision problems

We define the central decision problem:

$$
\mathrm{PCH}(\Pi, c): \text{ does the agent loop under protocol } \Pi \text{ halt with a compliant action in context } c \text{?}
$$

The agent loop is modeled as a Turing machine $M_{\Pi}$ that, on input encoding the context $c$, iterates: assess state, select action, execute or halt. The question $\mathrm{PCH}(\Pi, c)$ is then a question about the language of $M_{\Pi}$, and Section 4.2 applies the reduction strategy used to prove inner alignment undecidable [7], mirroring the encode-a-Turing-machine-into-the-system-class strategy used across undecidability results in physics [1, 5].

## 4. Analysis

### 4.1 State-space combinatorics

**Input numbers and their sources.** The state count 3 per permission-gated tool follows from the three-state semantics of Section 3.1 (derived, not measured). The tool counts $k=5$ and $k=10$ are our own illustrative assumptions, chosen to span a small single-agent toolset and a mid-size one; we state them as assumptions.

**Derivation 1 (state-space ratio).** Under the binary semantics, a context with $k$ permission-gated tools has $2^{k}$ distinguishable availability configurations. Under the three-state semantics it has $3^{k}$. For $k = 10$:

$$
2^{10} = 1024, \qquad 3^{10} = 59049, \qquad \frac{3^{10}}{2^{10}} = \frac{59049}{1024} = 57.66\overline{9} \approx 57.7.
$$

The three-state state space is $57.7$ times larger than the binary model represents. Every configuration in the difference — $59049 - 1024 = 58025$ configurations — contains at least one tool in state $\textsf{DISABLED}$, and is a configuration on which a Class B protocol has no specified behavior.

**Derivation 2 (well-defined fraction).** A Class B protocol is well-defined exactly on configurations where every permission-gated tool is in $\{\textsf{ABSENT}, \textsf{ENABLED}\}$, i.e., where no tool is disabled. If all three states of each tool are equally represented (an assumption we state explicitly and revisit in Section 4.3 with a non-uniform alternative), the well-defined fraction is

$$
f(k) = \left(\frac{2}{3}\right)^{k}.
$$

For $k = 5$:

$$
f(5) = \frac{2^{5}}{3^{5}} = \frac{32}{243} = 0.131687\ldots \approx 0.132.
$$

So under uniform state representation, a binary protocol governing five permission-gated tools is specification-complete on about 13.2% of the