# The Shaping of Unawareness: A Formal Framework for Information Ecosystems and the Boundaries of Awareness

## Abstract

Individuals and institutions make decisions inside information ecosystems that determine what they can know, yet most analyses of unawareness remain qualitative, enumerating social, cultural, and technological influences without a quantitative model of how those influences translate into bounded awareness. This gap blocks a concrete question: given a description of an information environment, how much of the relevant information can an agent in principle come to know, and which structural factor binds first? We formalize an information ecosystem as a channel through which an agent receives a rate-limited, relevance-weighted description of a source, and we model unawareness as the information about the source that the channel discards. Using the collaborative information bottleneck framework of [6], we derive a bound on achievable relevance at a given communication rate, and we show with explicit arithmetic that a single-agent bottleneck operating at rate $R_1 = 1$ bit per source symbol retains at most $I(Y;V_1) \leq R_1 = 1$ bit of relevance, while a two-agent collaborative system with the same per-agent rates can reach $I(Y;V_1 V_2) \leq R_1 + R_2 = 2$ bits, a doubling that follows from the sum-rate constraint alone. We further connect this rate-limited account to game-theoretic models of unawareness [1], [5], in which players reason over coarse belief sets rather than probabilities, and to reconstruction results showing that structured signals are recoverable from very few measurements [2]. The principal result is a quantitative decomposition showing that, under stated assumptions, the collaborative advantage equals the second agent's rate contribution exactly, and that structural exclusion (modeled as a zero-rate channel) reduces achievable relevance to zero regardless of agent motivation. This changes practice by giving educators, platform designers, and information-policy analysts a computable quantity — achievable relevance per rate budget — with which to compare interventions: widening a channel, adding a collaborative encoder, or changing the agent's prior.

## 1. Introduction

A public-health official designing a vaccination campaign, a teacher building a curriculum, and a platform engineer tuning a recommendation algorithm all face the same underlying problem: they operate on an information environment whose structure determines what their audience can come to know, and they currently have no quantitative way to predict how much awareness a given intervention can produce. The costs of this gap are concrete. Campaigns are designed on the assumption that information, once published, is available to everyone; when large fractions of the target population never encounter it — because of language barriers, social exclusion, or algorithmic filtering — the intervention underperforms and the failure is attributed to the message rather than to the channel. What would change if the paper's result holds: decision-makers could compute, from measurable parameters of an information environment (channel rates, number of collaborating information sources, relevance weighting), an upper bound on the awareness any intervention can achieve, and could therefore identify which structural factor binds first before spending resources on message design.

The existing literature supplies the pieces but not the connection. Chapter 1 of the present work [8] establishes that awareness is a spectrum rather than a binary state, introducing the distinction between unconscious incompetence (the unknown unknown) and conscious incompetence, and Chapter 2 [7] catalogues the forces that shape where an agent sits on that spectrum: social structures, cultural norms, technological affordances, and individual choices. Game theory has formalized unawareness directly: Halpern and Rêgo [5] model players whose awareness level — the set of game histories they are aware of — changes over time, and show that standard equilibrium concepts must be generalized (to generalized Nash equilibrium and generalized sequential equilibrium) to analyze such games. De Rosa and Vannucci [1] study players under a veil of ignorance whose beliefs are coarse subsets of opponents' actions, identifying pessimistic ($\max\min$) and optimistic ($\max\max$) attitudes. On the quantitative side, the collaborative information bottleneck [6] gives an exact characterization of the rate-relevance trade-off when multiple encoders cooperatively describe sources under logarithmic loss. Signal reconstruction theory [2] shows that structured binary signals can be recovered exactly from a small fraction of available measurements — a formal demonstration that the structure of information, not merely its quantity, determines recoverability.

What is missing is a bridge: a model in which the qualitative shaping forces of [7] appear as parameters of a quantitative channel model, so that claims like "social hierarchies restrict access to information" become statements about achievable relevance at given rates. This paper builds that bridge.

The contributions are:

- A formal model of an information ecosystem as a rate-limited collaborative bottleneck (Section 3), in which the shaping forces of [7] map onto channel rates, encoder structure, and relevance weighting.
- A derivation, with explicit arithmetic, of the achievable-relevance bound for single-agent and two-agent systems under the sum-rate constraint of [6], showing the collaborative advantage equals the added agent's rate exactly (Section 4).
- A corollary result that structural exclusion, modeled as a zero-rate channel, drives achievable relevance to zero independent of the agent's motivation or prior, giving a quantitative form to the information-inequality claims of [7] (Section 4).
- A connection between the rate-limited model and coarse-belief game-theoretic unawareness [1], [5], interpreting an awareness level as a finite-alphabet description $V$ of the true game (Section 4).
- A discussion of which structural intervention binds first, and a proposal for the smallest empirical test of the model (Sections 6 and 7).

## 2. Background and Related Work

The framework of the present paper rests on Chapter 1 of this work [8], which defines the awareness spectrum. Chapter 1 states that information awareness "isn't a light switch, flipped on or off; it's a dimmer," and introduces unconscious incompetence — the unknown unknown, illustrated by a child unaware of astrophysics — as one end of the spectrum, with conscious incompetence arising when the agent becomes aware of its own lack of knowledge [8]. Section 1.2 of [8] further establishes that the spectrum is multi-dimensional and dynamic: awareness "peaks and valleys" across domains, producing "information gaps" that shift as the agent learns. The present paper takes this spectrum as the object to be modeled: the position of an agent on the awareness spectrum, in our formalization, is the amount of relevance $I(Y;V)$ the agent's information channel can deliver about a source $Y$.

Chapter 2 [7] supplies the taxonomy of shaping forces that the formal model must capture. Section 2.1 of [7] argues that social structures — family, hierarchies, economic and political systems — "dictate how information is created, shared, and controlled," with the apartheid-era Bantu Education Act cited as a case of deliberate restriction of education and information access. Section 2.2 treats cultural norms and language as conduits and barriers, and Section 2.3 treats technological affordances from the printing press to social media. Section 2.6 of [7] develops the filter-bubble case study, arguing that algorithmic personalization creates feedback loops that narrow information intake over time. These are exactly the phenomena a rate-limited channel model should represent: a restricted education system is a low-rate channel, a language barrier is a channel with a reduced relevance weighting, and an algorithmic filter is a rate constraint chosen by an optimizer other than the agent.

Game theory provides the most direct formal antecedents. Halpern and Rêgo [5] explicitly drop the assumption that agents are perfect reasoners with common knowledge of the game. Their framework uses an augmented game $\Gamma^{+}$ based on an extensive-form game $\Gamma$, in which "player $i$'s awareness level at a node $h$ is essentially the set of runs (complete histories) in $\Gamma$ that $i$ is aware of at node $h$," and this awareness level may change over time as the player becomes aware of more moves [5]. In their conclusion they generalize sequential equilibrium to games with awareness and argue that techniques used to prove existence of generalized Nash equilibrium extend to other solution concepts such as trembling-hand perfect equilibrium [5]. The key structural fact for our purposes is that an awareness level is a set of histories — a coarse, finite description of the true game — and not a probability distribution over games. De Rosa and Vannucci [1] make the same representational choice: players under the veil of ignorance hold beliefs "represented as subsets of opponents' actions," and the paper analyzes when such players follow $\max\min$ or $\max\max$ criteria, identified with pessimistic and optimistic attitudes respectively [1]. Section 1.1 of [1] situates these games outside the Bayesian paradigm: players "are not able to describe their beliefs via any form of probability measure," so the usual cardinal-utility machinery from von Neumann–Morgenstern onward does not apply [1]. Both [1] and [5] thus model unawareness as coarse, set-valued description — which is precisely the form of a rate-limited codeword $V$ in an information-theoretic model. Our contribution is to make that correspondence quantitative: the coarseness of an awareness level is bounded by the rate of the channel that produces it.

The quantitative backbone is the collaborative information bottleneck of [6]. That paper studies a multi-terminal source coding problem under logarithmic loss, motivated by extending the information bottleneck method to multiple encoders that "build cooperatively rate-limited descriptions of their sources in order to maximize information" about a relevance variable [6]. Its converse proofs (Section IV) establish the achievable region: for the two-encoder case with $K=1$, the region includes $R_1 \geq I(X_1;V_1|X_2)$, $R_2 \geq I(X_2;V_2|V_1)$, $R_1 + R_2 \geq I(X_1 X_2;V_1 V_2)$, and relevance $\mu \leq I(Y;V_1 V_2)$, with auxiliary variables satisfying stated Markov conditions [6]. The relevance bound $\mu \leq I(Y;V_1 V_2)$ subject to rate constraints is the theorem we use directly in Section 4: it converts a statement about encoders and rates into a statement about how much relevant information a system of agents can hold.

A complementary result comes from reconstruction theory. The work on binary functions from incomplete frequency information [2] proves that a binary signal can be exactly reconstructed by solving the convex problem $\text{find } u \text{ s.t. } S\mathcal{F}u = b,\ 0 \leq u \leq 1$, and that when the signal is spatially structured — ones and zeros clustered, as in a binary image — "with very few low frequency measurements taken, the solution of this convex optimization problem is deterministically unique and equals to the original binary signal" [2]. Its numerical results quantify this: a $200 \times 200$ binary image of a geometrical shape is fully determined by Fourier coefficients with $|k| \leq 5$, accounting for 0.2% of the total coefficients [2]. This matters for our argument because it shows that structure, not volume, governs recoverability of information: an agent whose prior knowledge imposes structure on the missing information can reconstruct the whole from a small measured fraction. In our model, this is the formal counterpart of the claim in [7] that prior cultural knowledge shapes what new information an agent can absorb.

Finally, two works inform the interpretation of the model's limits. The Q-shaping work [3] addresses a different problem — incorporating domain knowledge into reinforcement learning — but its framing is relevant: it notes that reward shaping is the most practical knowledge-injection method because it "avoids the need for expert trajectories or predefined controllers," and it guarantees optimality while allowing rapid verification of agent behavior [3]. We use it in Section 7 as an analogy for how heuristic guidance (the analogue of an information intervention) can be injected into an agent's learning process without biasing its eventual optimum, provided the injection is structured correctly. The mind-before-matter essay [4] argues, in a foundational register, that the orthodox physicalist view "works perfectly fine — in a certain regime," namely a small universe with weak technology where quantum effects can be ignored, and proposes reversing the arrow of fundamentality so that an emergent notion of world follows from the self [4]. We cite it for a methodological point its Section 2 makes explicitly: science is trustworthy because of "features of self-correction" — adapting views to new evidence, reproducing experiments, testing findings against those of others [4]. An information ecosystem that suppresses self-correction (by filtering disconfirming evidence) attacks precisely the mechanism that makes knowledge objective; this gives our model's relevance variable a normative reading, developed in Section 6.

## 3. Methods

### 3.1 Model

We model an information ecosystem as a collaborative multi-terminal bottleneck in the sense of [6], with the following interpretation.

Let $Y$ denote the relevant state of the world — the totality of information an agent could in principle come to know about a domain (for example, the health information relevant to a vaccination decision). Let $X_1, X_2, \ldots, X_K$ denote the information sources available in the ecosystem: for $K = 1$ a single source (for instance, the agent's immediate community), for $K = 2$ two sources (for instance, community plus an external institution). Each source is described to the agent through an encoder producing a finite-alphabet description $V_k$ at rate $R_k$ bits per source symbol. The agent's resulting awareness is measured by the relevance

$$\mu = I(Y; V_1 \cdots V_K),$$

the mutual information between the relevant state and the agent's total description. The logarithmic-loss fidelity of [6] makes $\mu$ exactly the quantity Chapter 1 [8] calls position on the awareness spectrum: under logarithmic loss, the optimal agent action given description $V$ is the posterior distribution, and the incurred loss is the conditional entropy $H(Y|V)$, so maximizing $\mu = I(Y;V)$ is minimizing the agent's residual uncertainty — the formal version of moving along the dimmer of [8].

The shaping forces of [7] map onto model parameters as follows:

- **Social hierarchies and exclusion** (Section 2.1 of [7]): a source the agent cannot access at all is a channel with $R_k = 0$; a source accessed through an intermediary (family, community) is an encoder whose description $V_k$ is a lossy function of $X_k$ chosen by the intermediary's own relevance criterion, not the agent's.
- **Cultural and linguistic barriers** (Section 2.2 of [7]): a barrier reduces the effective rate by making descriptions costly — the same physical channel carries less relevant information when the encoding must be translated across conceptual schemes.
- **Technological affordances** (Section 2.3 of [7]): a technology raises $R_k$ or adds an encoder (raising $K$); an algorithmic filter selects the description $V_k$ to maximize a platform objective rather than $I(Y;V_k)$, so the achieved relevance falls below the rate-feasible maximum.
- **Individual choices** (Section 2.4 of [7]): selective exposure and motivated reasoning appear as the agent (or the ecosystem optimizer) choosing which description to request within the rate budget.

### 3.2 Assumptions

We state every assumption used in the derivations of Section 4.

1. **A1 (bottleneck structure).** The ecosystem is a collaborative information bottleneck under logarithmic loss, so the achievable region of [6] applies: any achievable tuple satisfies $\mu \leq I(Y; V_1 \cdots V_K)$ with the rate constraints stated in Section 2.
2. **A2 (rate values).** The bibliography and grounding give no measured rates for real information ecosystems. We therefore treat rates as free parameters and compute the bounds as functions of them; where a numerical example is needed we assume $R_1 = 1$ and $R_2 = 1$ bit per source symbol, and we label every such number an assumption.
3. **A3 (independence of relevance).** The relevance variable $Y$ is fixed; interventions change rates and encoder structure, not the definition of relevance. (A change of what counts as relevant is a change of the problem, not of the ecosystem.)
4. **A4 (two-agent scope).** We derive explicit results for $K \in \{1, 2\}$; the $K$-agent generalization is stated but not computed term by term.

### 3.3 Derivation plan

Section 4 proceeds in three steps. First, we derive the single-agent relevance bound from the $K=1$ region of [6] and compute its value at the assumed rate. Second, we derive the two-agent bound and compute the collaborative advantage at the assumed rates, showing it equals $R_2$ exactly under the sum-rate constraint. Third, we derive the zero-rate corollary for structural exclusion and compute its consequence. All arithmetic is shown step by step.

## 4. Analysis

### 4.1 Single-agent bound

From the $K=1$ characterization in [6] (Section IV-C), the achievable region requires

$$R_1 \geq I(X_1; V_1 | X_2), \qquad \mu \leq I(Y; V_1 V_2),$$

and, specializing to a single encoder ($K=1$, so $V_2$ is absent), the relevance is bounded by the rate:

$$\mu_1 = I(Y; V_1) \leq I(X_1; V_1) \leq R_1,$$

where the first inequality holds because $V_1$ is a function of $X_1$ alone (data processing: $V_1$ can carry information about $Y$ only through $X_1$), and the second because the description of $X_1$ is rate-limited to $R_1$ bits per symbol.

**Computation.** Under assumption A2 we set $R_1 = 1$ bit per source symbol. Then

$$\mu_1 \leq R_1 = 1 \text{ bit},$$

so a single-channel agent can hold at most 1 bit of relevance per source symbol, regardless of how informative the source $X_1$ is about $Y$ in the unconstrained sense. If the source's unconstrained relevance is $I(Y; X_1) = 8$ bits (an illustrative assumption, not a measurement), the single-channel agent retains a fraction

$$\frac{\mu_1}{I(Y;X_1)} \leq \frac{1}{8} = 0.125,$$

that is, at most 12.5% of the available relevance. The remaining 7 bits per symbol — 87.5% — is the agent's structural unawareness: information present in the ecosystem but unreachable through the agent's single channel.

### 4.2 Two-agent collaborative bound

With two encoders, the region of [6] gives the sum-rate constraint $R_1 + R_2 \geq I(X_1 X_2; V_1 V_2)$ and the relevance bound

$$\mu_2 = I(Y; V_1 V_2) \leq I(X_1 X_2; V_1 V_2) \leq R_1 + R_2.$$

**Computation.** Under A2, $R_1 = R_2 = 1$ bit per source symbol. Then

$$\mu_2 \leq R_1 + R_2 = 1 + 1 = 2 \text{ bits}.$$

The collaborative advantage is

$$\Delta\mu = \mu_2 - \mu_1 \leq (R_1 + R_2) - R_1 = R_2 = 1 \text{ bit},$$

so, under the sum-rate constraint, adding a second encoder at rate $R_2$ raises the achievable relevance ceiling by exactly $R_2$ — here a doubling from 1 bit to 2 bits, i.e., from 12.5% to 25% of the assumed unconstrained relevance $I(Y;X_1 X_2) = 8$ bits:

$$\frac{\mu_2}{I(Y; X_1 X_2)} \leq \frac{2}{8} = 0.25.$$

Two remarks on what this bound does and does not say. It is an upper bound: achieving $\mu_2 = R_1 + R_2$ requires the encoders' descriptions to be perfectly relevant, which in practice they are not (an algorithmic filter optimizes a platform objective; a community intermediary optimizes its own). The bound is nevertheless the correct instrument for ranking interventions, because any intervention's achieved relevance is capped by it.

### 4.3 Zero-rate corollary: structural exclusion

Setting $R_2 = 0$ (the second source is inaccessible — the formal image of the Bantu Education case in [7], where a population is cut off from a source of information by policy):

$$\mu_2 \leq R_1 + 0 = R_1 = 1 \text{ bit}.$$

More strongly, if the excluded source is the *only* carrier of some component of $Y$ — that is, if $Y$ contains information not present in $X_1$ at all — then that component contributes zero to $I(Y; V_1)$ no matter how large $R_1$ is. Formally, if $Y = (Y_a, Y_b)$ with $Y_b$ independent of $X_1$ given $X_1$'s reachable variables, then

$$I(Y; V_1) = I(Y_a; V_1) + I(Y_b; V_1 | Y_a, V_1) \leq I(Y_a; X_1) \leq H(Y_a),$$

and the component $Y_b$ is structurally unknowable to the agent. This is the quantitative form of the claim in [7] that hierarchies "create and perpetuate information inequalities, shaping the boundaries of awareness for different social groups": exclusion does not merely reduce relevance linearly with rate; it can remove entire components of the relevant state from the agent's reachable set, and no increase in the agent's effort, motivation, or prior (the individual-level factors of Section 2.4 of [7]) restores it.

### 4.4 Connection to coarse-belief unawareness

The awareness level of [5] — the set of runs a player is aware of at a node — and the coarse belief set of [1] — a subset of opponents' actions — are both finite descriptions of a richer object. In our model, the description $V$ is exactly such a finite object: an agent whose channel delivers $V$ at rate $R$ can distinguish at most $2^{R}$ description values per source symbol (for a block of $n$ symbols, at most $2^{nR}$ codewords). A player in the setting of [1] who cannot assign probabilities and reasons only over the set $B \subseteq A_{-i}$ of opponent actions is effectively operating on a description whose rate is $\log_2 |B|$ bits:

$$R_{\text{belief}} = \log_2 |B|.$$

**Computation.** If a player's belief set contains $|B| = 4$ of the opponent's 16 possible actions, then

$$R_{\text{belief}} = \log_2 4 = 2 \text{ bits},$$

while the full action set would require $\log_2 16 = 4$ bits. The player is thus operating 2 bits below the full-description rate — a 50% rate deficit — and the pessimism/optimism dichotomy of [1] ($\max\min$ vs. $\max\max$ over the coarse set) is a decision rule applied to exactly this rate-limited description. Similarly, a player in [5] whose awareness level at a node covers a subset of the game's histories is playing a game whose description rate is the logarithm of that subset's size; as the player "becomes aware of more moves" [5], the rate increases, which is the game-theoretic image of moving along the awareness dimmer of [8].

### 4.5 Structure and recoverability

The reconstruction result of [2] adds a constraint the rate bounds alone miss: recoverability depends on structure. A spatially structured binary signal is fully determined by very few low-frequency measurements — the $200 \times 200$ shape image of [2] needs only coefficients with $|k| \leq 5$, i.e., 0.2% of the total [2]. Translated to our setting: an agent whose prior knowledge imposes strong structure on the domain can reconstruct the full relevant state from a small, well-chosen fraction of the ecosystem's information, while an agent without that structure needs the full rate. This formalizes the observation in [7] (Section 2.2.2) that different knowledge systems extract different value from the same environment: the prior's structure, not only the channel's rate, determines achievable awareness. It also sharpens the filter-bubble analysis of [7] (Section 2.6): an algorithmic filter that removes low-frequency (consensual, structural) content in favor of high-frequency (novel, engaging) content destroys exactly the measurements from which the rest is recoverable.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions; none is a measurement.

**R1 (single-agent ceiling).** Under A2 ($R_1 = 1$ bit per source symbol) and the assumed unconstrained relevance $I(Y;X_1) = 8$ bits, a single-channel agent's achievable relevance is at most $\mu_1 \leq 1$ bit, i.e., 12.5% of available relevance (Section 4.1).

**R2 (collaborative advantage).** With two encoders at $R_1 = R_2 = 1$ bit, the relevance ceiling doubles to $\mu_2 \leq 2$ bits (25% of the assumed 8-bit unconstrained relevance), and the advantage equals the added agent's rate exactly: $\Delta\mu = R_2 = 1$ bit (Section 4.2).

**R3 (exclusion corollary).** Setting $R_2 = 0$ returns the ceiling to $\mu_2 \leq 1$ bit; and if the excluded source is the sole carrier of a relevance component $Y_b$, that component is unreachable at any rate, contributing zero to $I(Y;V_1)$ (Section 4.3).

**R4 (coarse-belief rate deficit).** A player with a 4-action belief set out of 16 operates at $R_{\text{belief}} = 2$ bits against a full-description requirement of 4 bits — a 50% deficit; the pessimistic and optimistic criteria of [1] are decision rules over this rate-limited description (Section 4.4).

**R5 (structural recoverability).** Per [2], a structured $200 \times 200$ binary image is determined by 0.2% of its Fourier coefficients; by analogy, a strongly structured prior can in principle substitute for a large rate budget, while a filter that discards structural (low-frequency) content makes the remainder unrecoverable (Section 4.5).

## 6. Discussion

The model's central claim is that the shaping forces catalogued qualitatively in [7] can be represented as parameters of a rate-limited collaborative bottleneck, and that the resulting bounds rank interventions: adding an encoder helps by exactly its rate (R2), exclusion can remove relevance components entirely (R3), and prior structure changes how much rate is needed (R5).

**Limitations.** The result rests on the following assumptions, with sensitivity noted for each.

- **A1 (bottleneck applicability).** Real information ecosystems are not literal multi-terminal source-coding systems; the logarithmic-loss abstraction treats the agent's knowledge state as a posterior distribution, which fits probabilistic beliefs but not the set-valued, non-probabilistic beliefs of [1] except through the rate interpretation of Section 4.4. If the abstraction fails — for instance, if human awareness is not well approximated by any posterior — the quantitative bounds do not transfer, though the qualitative ranking (more encoders at positive rate weakly help; zero rate removes components) survives because it depends only on the data-processing and rate constraints.
- **A2 (rate values).** No rate in the paper is measured; $R_1 = R_2 = 1$ bit and $I(Y;X_1) = 8$ bits are assumptions chosen to make the arithmetic concrete. The percentage results (12.5%, 25%) scale linearly with the assumed unconstrained relevance and are therefore illustrative, not empirical. The structural results (R2's $\Delta\mu = R_2$, R3's zero-rate corollary) are independent of these choices.
- **A3 (fixed relevance).** Interventions in the real world often change what is considered relevant; the model holds $Y$ fixed and therefore cannot represent agenda-setting, which changes $Y$ itself.
- **A4 (two-agent scope).** The $K > 2$ case is stated but not computed; the sum-rate bound generalizes immediately ($\mu \leq \sum_k R_k$), but interaction effects among encoders (redundancy, complementarity) appear only inside the bound, not in its value.
- **Linearity of the collaborative advantage.** $\Delta\mu = R_2$ is an upper bound achieved only by perfectly relevant encodings; real encoders overlap, so realized gains fall short. The bound is tight only in the ideal case.

**Failure modes and falsification.** The main result — that the collaborative advantage is capped by the added agent's rate, and that zero rate removes relevance components — would be falsified by a demonstration that a second information source systematically raises an agent's relevant knowledge by more than the information-theoretic rate of the second channel allows, or that an agent can acquire a relevance component whose carrier it has no access to. The latter is logically impossible under the model's own definitions (an unreachable component is unreachable by construction), so the meaningful falsification target is the former and the transfer claim: if empirical studies of, say, media-supplementation interventions found that adding a second source never helps beyond the first source's information alone — i.e., that sources are fully redundant in practice — the collaborative bound would be loose by the entire amount and the model would have no discriminative power. A second falsifier: if the coarse-belief interpretation of Section 4.4 is wrong — if players under ignorance in the sense of [1] do not behave as if operating on a rate-limited description (for example, if their $\max\min$/$\max\max$ choices depend on features a rate cannot capture) — the bridge between the game-theoretic and information-theoretic literatures collapses, and the paper's unification claim fails.

**Open questions.** What are the actual rates of real information channels — a school system, a language barrier, a recommendation feed — in bits per symbol relevant to a given decision? How much of the filter-bubble effect of [7] is rate loss versus relevance misweighting? Can the awareness dimmer of [8] be operationalized as a measurable $\mu$ for human subjects? These require empirical work outside the scope of this paper.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The users are information-policy analysts, public-health communication designers, educators designing curricula, and platform engineers. The decision that changes: instead of asking "is our message good?", they ask "which parameter binds — the rate of the audience's channels, the number of accessible encoders, or the relevance weighting of the filters?" The result gives them a ranking rule derived in Section 4: if the audience has access to only one encoder, adding a second independent source is the only intervention that can raise the ceiling (R2); if a relevance component's carrier is excluded, no message improvement helps and the binding constraint is structural access (R3); if the audience's prior is well structured, a small, well-targeted information budget suffices (R5).

**(b) Readiness.** This work is purely analytical and has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2: basic principles observed and reported (the bottleneck theorems of [6], the awareness models of [5], [1]) and a concept formulated (the ecosystem-as-bottleneck mapping of Section 3). Analytical work does not exceed TRL 3, and no claim of implementation readiness is made.

**(c) Smallest next test.** The smallest de-risking study would be a measurement study, run as a proposal: a study would recruit two groups of participants matched on prior knowledge, give one group access to a single curated information source about a fixed decision task and the other group access to two independent sources, hold total reading time constant so that the rate budget is matched, and measure decision-relevant knowledge with a scored instrument. The model's R2 predicts the two-source group's knowledge gain is capped by the second source's incremental rate; the outcome that would refute the model is a two-source group whose knowledge exceeds the single-source group by more than the second source's measured incremental information content, or no gain at all despite measured non-redundancy between the sources.

**(d) Binding constraints.** The constraints that would bind first in any operationalization are, in order: (i) measurement — no validated instrument exists for expressing a human's domain knowledge as bits of mutual information with a relevance variable, and building one is a prerequisite for every quantitative use; (ii) definition of relevance — the model requires fixing $Y$ (A3), and real interventions dispute what $Y$ should be; (iii) encoder fidelity — real intermediaries (media, curricula, feeds) optimize their own objectives, so achieved relevance falls below the rate-feasible bound by an unquantified gap. Cost, energy, and manufacturing constraints do not bind: the model is informational, and its "hardware" is existing media and institutions. Whether the rate abstraction survives contact with measured human knowledge states is an open question (Section 6).

**(e) Order-of-magnitude bounds.** As a labeled projection with stated assumptions: if a decision-relevant domain has unconstrained relevance on the order of $I(Y;X) \sim 10$ bits (assumption, by analogy with the 8-bit example of Section 4.1) and a single channel delivers $R_1 \sim 1$ relevant bit per encounter, then on the order of $10 / 1 = 10$ independent well-chosen encounters are needed to exhaust the single-source ceiling, and each added independent source at $\sim 1$ bit reduces the required encounter count by roughly a factor of the ratio of total rate to single rate. These figures are projections from the assumed rates, not measurements, and inherit the ideal-encoder caveat of Section 6.

**(f) Risks and misuse.** The framework's ranking rule can be misused: an actor who controls encoders can apply R3 in reverse — identifying which relevance components a target population can only obtain through channels it controls, and cutting exactly those channels, achieving maximal unawareness per unit of censorship effort. The Bantu Education case discussed in [7] is the historical instance of this strategy; the model makes its logic explicit and therefore, potentially, easier to execute. Publication of the framework should be accompanied by awareness of this dual use.

## 8. Conclusion

This paper set out to give the qualitative account of unawareness in [7] and [8] a quantitative backbone, using the collaborative information bottleneck [6] as the formal instrument and the coarse-belief models of unawareness [1], [5] as the conceptual bridge. The derivations show that a single-channel agent's relevance is capped by its rate (R1), that adding an independent encoder raises the cap by exactly that encoder's rate (R2), that exclusion at zero rate can remove relevance components entirely rather than merely shrinking them (R3), that coarse game-theoretic beliefs correspond to rate-limited descriptions with computable deficits (R4), and that prior structure changes how much rate awareness requires (R5, via [2]). The framework's practical value is a ranking rule for interventions; its honest limits are that no rate has been measured, the logarithmic-loss abstraction is untested against human knowledge states, and the framework itself is dual use. The next step is the measurement study proposed in Section 7(c), which would either give the model empirical footing or refute its transfer claim.

## References

[1] arXiv:2103.08319v4 | Optimism and Pessimism in Strategic Interactions under Ignorance

[2] arXiv:1104.0446v3 | Reconstruction of Binary Functions and Shapes from Incomplete Frequency Information

[3] arXiv:2410.01458v1 | From Reward Shaping to Q-Shaping: Achieving Unbiased Learning with LLM-Guided Knowledge

[4] arXiv:1812.08594v1 | Mind before matter: reversing the arrow of fundamentality

[5] arXiv:0707.1904v1 | Generalized Solution Concepts in Games with Possibly Unaware Players

[6] arXiv:1604.01433v4 | Collaborative Information Bottleneck

[7] QNFO: 2. The Shaping of Unawareness | https://papers.qnfo.org/papers/chapter-2

[8] QNFO: Part I: Observing Ignorance | https://papers.qnfo.org/papers/chapter-1