# Observing Ignorance: A Formal Account of the Information Awareness Spectrum

## Abstract

Understanding what we do not know is usually treated as a phenomenological question, yet decisions are routinely made by agents whose ignorance of their own ignorance is never quantified. The specific gap addressed here is the absence of any bridge between the four classical states of information awareness—unconscious incompetence, conscious incompetence, conscious competence, and unconscious competence—and the formal decision theory that describes behavior when beliefs cannot be represented as probabilities. This paper supplies that bridge in three steps. First, it defines an awareness level as a pair (k, m) of domain knowledge and meta-knowledge and shows that the four states correspond to the four corners of the unit square spanned by k and m. Second, it derives the cost of unawareness in a decision under ignorance in the style of games played under coarse subset beliefs: for a two-state worked example, a maximin agent who cannot represent probabilities incurs an expected utility loss of 12p − 6 whenever the true state probability p exceeds 0.6, reaching 4.8 utility units at p = 0.9. Third, it reads three formal literatures—multi-stage search ranking, collaborative information bottleneck coding, and information dimension of Gaussian processes—as quantitative templates for measuring awareness gains, gap pooling, and the ignorance of continuous structure. The practical result is a checklist for auditing when unawareness, rather than lack of knowledge alone, is the binding constraint on decision quality.

## 1. Introduction

### 1.1 The problem

Every agent—human or machine—acts on the basis of what it knows. But decision quality is damaged twice over by ignorance: once by the missing knowledge itself, and a second time by the agent's failure to represent that it is missing something. The second damage is the dangerous one, because an agent that does not represent its gap will not seek information, will not hedge, and will not defer. The question "how aware are we of what we know and, more importantly, what we don't know?" is therefore not merely a question about subjective experience; it is a question about when unawareness, rather than absence of knowledge alone, becomes the binding constraint on performance.

### 1.2 The gap

The four states of information awareness—unconscious incompetence, conscious incompetence, conscious competence, and unconscious competence—are well established as a phenomenological description of the journey from ignorance to expertise [6]. Chapter 2 of the same corpus complements this picture by describing the social, cultural, and technological forces that shape which gaps an agent is born into and which it can escape [7]. What neither account provides, and what the broader formal literature does not yet connect to them, is a quantitative statement of when the transition from unconscious to conscious incompetence changes behavior, and how much that transition is worth in decision-theoretic terms. Games played under the veil of ignorance, where players hold coarse beliefs represented as subsets of opponents' actions and follow maximin or maximax criteria identified with pessimistic or optimistic attitudes [2], describe exactly the behavior of an agent at the conscious-incompetence boundary—but this connection has not been drawn. Likewise, the engineering literatures on multi-stage search ranking [1], collaborative information bottleneck coding [4], and information dimension of stochastic processes [5] contain quantitative templates for measuring awareness gains, pooling partial knowledge, and quantifying the ignorance of continuous structure, none of which have been read as instruments for observing ignorance.

### 1.3 Contributions

- A formal definition of the awareness level as a pair (k, m) of domain knowledge and meta-knowledge, from which the four classical states are derived as the corners of the unit square (Section 3).
- A derivation of the expected cost of unawareness in a decision under ignorance, with explicit arithmetic: a maximin agent incurs a loss of 12p − 6 for p > 0.6 in the worked example, reaching 4.8 units at p = 0.9 (Section 4).
- Readings of three formal literatures as quantitative templates for observing ignorance: multi-stage search ranking as a measured awareness gain [1], collaborative information bottleneck as gap pooling [4], and information dimension as quantified ignorance of continuous structure [5] (Section 5).
- An audit procedure and falsifiability conditions (Sections 6 and 7).

## 2. Background and Related Work

### 2.1 The phenomenological corpus

The source account of the information spectrum describes awareness as a dimmer rather than a light switch, moving through unconscious incompetence (the unknown unknown), conscious incompetence (awareness of the gap without the knowledge), conscious competence (effortful acquisition), and unconscious competence (ingrained mastery) [6]. It further emphasizes that the spectrum is multi-dimensional—peaking and valleying across domains—and dynamic, shifting as the agent learns [6]. The companion account of the shaping of unawareness argues that agents are born into pre-existing information ecosystems—family, community, cultural norms, language—that determine which gaps exist and which remain invisible [7]. These two accounts fix the conceptual vocabulary used throughout this paper; the present work adds the formal layer they presuppose.

### 2.2 Decisions under ignorance

The formal theory of strategic interaction under ignorance studies players who cannot describe their beliefs via any probability measure, so that the interaction lies outside the Bayesian paradigm; such players hold coarse beliefs as subsets of opponents' actions and follow maximin (pessimistic) or maximax (optimistic) criteria [2]. The paper characterizes when players follow each criterion and relates optimism to wishful thinking [2]. This is precisely the formal situation of an agent at the conscious-incompetence boundary: the agent knows the set of possibilities (the subset belief) but not the distribution over it. The present paper uses this structure to price the difference between the unconscious and conscious states.

### 2.3 The observer and the observed

A foundational essay argues that in certain regimes it is a step forward to reverse the arrow of fundamentality, starting from the first-person perspective and treating the emergent notion of world as derived rather than primitive [3]. The essay notes that the orthodox physicalist view applies perfectly to a small universe in which powerful technology and quantum theory can be ignored, and that self-correction—adapting views to new evidence, reproducing experiments, testing findings against others—is what makes science trustworthy [3]. This matters for observing ignorance because the four states of awareness are states of an observer, not of the world: the same physical situation supports different awareness levels depending on the observer's representational resources. The reversal proposed in [3] licenses treating the observer's awareness state as the primary object of analysis, with the "information landscape" as the emergent description.

### 2.4 Quantitative templates

Three formal literatures supply measurement templates. In multi-stage search ranking, a Journey Ranker model that explicitly represents the long exploratory search journey achieved a statistically significant offline improvement of +0.48% NDCG over the baseline with a +9.2% increase in trainable parameters, and drove a +0.61% gain in uncancelled bookers in online A/B experiments with p-values below 0.01 [1]. In multi-terminal source coding under logarithmic loss, several encoders must cooperatively build rate-limited descriptions of their sources to maximize relevance, with achievable tuples characterized by rate and relevance inequalities such as R₁ ≥ I(X₁;V₁|X₂) and μ ≤ I(Y;V₁V₂) [4]. In stochastic process theory, the Rényi information dimension rate of an L-variate stationary process is defined as the entropy rate of the uniformly quantized process divided by log m as the quantizer step 1/m vanishes, is bounded when the coarsely quantized process has finite entropy, and for Gaussian processes is computed from the spectral distribution [5]. Each template is deployed in Section 5.

## 3. Methods I: The Awareness Square

### 3.1 Definitions

Fix a domain d. Define:

- Domain knowledge k ∈ [0,1]: the fraction of the domain's decision-relevant content the agent can correctly apply.
- Meta-knowledge m ∈ [0,1]: the probability that, presented with a gap in domain d, the agent represents the gap as a gap (seeks information, hedges, or defers).

The awareness level of the agent in domain d is the pair a(d) = (k, m).

### 3.2 Derivation of the four states

The four classical states are recovered as the corners of the unit square spanned by k and m:

- Unconscious incompetence: k < 0.5, m < 0.5. The agent lacks the knowledge and does not represent the lack. This is the unknown unknown [6].
- Conscious incompetence: k < 0.5, m > 0.5. The agent lacks the knowledge but represents the lack; this awareness motivates learning [6].
- Conscious competence: k > 0.5, m > 0.5. The agent has the knowledge and applies it effortfully, still monitoring for errors [6].
- Unconscious competence: k > 0.5, m < 0.5. The agent has ingrained mastery and no longer monitors; performance is automatic [6].

Two consequences follow. First, awareness is not monotone in m along the journey: m rises from unconscious incompetence to conscious incompetence and again through conscious competence, then falls at unconscious competence, where monitoring is deliberately surrendered. Second, the multi-dimensional character of the spectrum [6] is captured by letting a vary over domains d: a history professor and a furniture assembler are the same agent at different corners for different d. The shaping forces of Chapter 2 [7] act on this map by determining the prior distribution of (k, m) the agent is born into—family, community, and language set which corners are reachable and which corners the agent does not know exist.

### 3.3 The transition condition

The phenomenologically important transition is from unconscious to conscious incompetence: the moment m crosses 0.5 for a domain where k < 0.5. Section 4 prices this transition in decision-theoretic terms.

## 4. Methods II: Pricing the Transition from Unconscious to Conscious Incompetence

### 4.1 Setup

Consider a decision-maker interacting under ignorance in the sense of [2]: the opponent's action set is A₋ᵢ = {a₁, a₂}, and the decision-maker's belief is the coarse subset {a₁, a₂} with no probability measure over it—the defining situation of a game under the veil of ignorance [2]. The decision-maker chooses x or y. Utilities are:

- If the opponent plays a₁: x yields 10, y yields 4.
- If the opponent plays a₂: x yields 0, y yields 6.

### 4.2 Behavior at the two awareness states

An agent at the conscious-incompetence boundary (k < 0.5, m > 0.5) knows it cannot assign probabilities and therefore follows a maximin criterion, the pessimistic attitude formalized in [2]. The maximin values are:

- maximin(x) = min(10, 0) = 0.
- maximin(y) = min(4, 6) = 4.

Since 4 > 0, the maximin agent chooses y, guaranteeing utility 4 regardless of the opponent's action.

An agent at unconscious incompetence (k < 0.5, m < 0.5) does not represent the gap; it behaves as if its situation were fully described. We model this as the agent following the maximax criterion—the optimistic attitude of [2]—without representing that optimism is a choice:

- maximax(x) = max(10, 0) = 10.
- maximax(y) = max(4, 6) = 6.

Since 10 > 6, the maximax agent chooses x, exposed to utility 0 if the opponent plays a₂.

### 4.3 The cost of unawareness

Let p be the true probability that the opponent plays a₁. The expected utilities are:

- E[u(x)] = 10p + 0(1 − p) = 10p.
- E[u(y)] = 4p + 6(1 − p) = 6 − 2p.

The optimal choice is x when 10p > 6 − 2p, i.e., p > 0.6, and y otherwise. The maximin agent (conscious incompetence) always chooses y, so its expected loss relative to the optimal policy is:

- L(p) = max(0, 10p − (6 − 2p)) = max(0, 12p − 6).

At p = 0.9: L = 12(0.9) − 6 = 10.8 − 6 = 4.8. At p = 0.7: L = 8.4 − 6 = 2.4. At p = 0.6: L = 0.

The maximax agent (unconscious incompetence) always chooses x, so its expected loss is:

- L'(p) = max(0, (6 − 2p) − 10p) = max(0, 6 − 12p).

At p = 0.3: L' = 6 − 3.6 = 2.4. At p = 0.1: L' = 6 − 1.2 = 4.8. At p = 0.5: L' = 0.

### 4.4 Interpretation

The two unawareness-driven policies bracket the optimum from opposite sides, and the loss is linear in the distance of p from 0.6 with slope 12 in both directions. Three conclusions follow. First, the transition from unconscious to conscious incompetence is not automatically an improvement: the maximin agent outperforms the maximax agent exactly when p > 0.6 and underperforms when p < 0.6. What the transition buys is not lower loss but representational capacity—the ability to notice that p is unknown and to seek it. Second, the value of information about p is at most 4.8 utility units in this example (the maximum of L and L'), which is the price an agent should be willing to pay to move from the subset belief {a₁, a₂} to a probability measure—the move that takes the interaction out of the veil-of-ignorance regime and into the Bayesian one [2]. Third, the pessimism–optimism attitudes of [2] are here not personality traits but consequences of awareness state: the same agent is maximax at one corner of the awareness square and maximin at another.

## 5. Results: Three Quantitative Templates for Observing Ignorance

### 5.1 Template 1: Measured awareness gains in multi-stage ranking

The Journey Ranker result supplies a measured instance of an awareness gain at the system level. The baseline ranker treated each search impression in isolation; the Journey Ranker explicitly represents the multi-stage journey—weeks of exploration before a reservation request, with possible rejection or cancellation by the host [1]. Representing the journey is a form of meta-knowledge: the system now represents that impressions are stages of a longer process whose outcome it does not control. The measured returns are: +0.48% NDCG offline (95% confidence interval ±0.05%) with +9.2% parameters, against a reference point where +0.3% offline is considered promising for a significant online booking gain and where a +50% parameter increase through network depth or width yields only about 0.05–0.1% offline NDCG [1]. Online, the model drove +0.61% uncancelled bookers, +0.14% searchers-to-clickers, and +0.48% clickers-to-uncancelled-bookers, all with p-values < 0.01 [1]. The instructive comparison is structural: representing the journey (a meta-knowledge investment of +9.2% parameters) outperformed representing more of the same stage (+50% parameters for 0.05–0.1% NDCG) by roughly an order of magnitude in offline return per parameter. In the vocabulary of Section 3, raising m outperformed raising k.

### 5.2 Template 2: Pooling partial knowledge in the collaborative information bottleneck

The collaborative information bottleneck formalizes the situation of several agents, each holding partial knowledge, who must cooperatively build rate-limited descriptions to maximize relevance [4]. The achievable region for the single-relevance case is characterized by inequalities of the form R₁ ≥ I(X₁;V₁|X₂), R₂ ≥ I(X₂;V₂|V₁), R₁ + R₂ ≥ I(X₁X₂;V₁V₂), and μ ≤ I(Y;V₁V₂), with Markov conditions V₁ − X₁ − (X₂,Y) and V₂ − (V₁,X₂) − (X₁,Y) [4]. Read as a template for observing ignorance: each encoder's description V is a partial representation of one agent's knowledge X; the relevance μ is what the pooled representation supports about the target Y; and the rate inequalities price how much description each agent must contribute given what the others contribute. The Markov condition V₂ − (V₁,X₂) − (X₁,Y) states that the second agent's contribution may depend on the first agent's description—ignorance is observed and compensated sequentially, not assumed away. This is the formal counterpart of the societal claim that information inequality arises from disparities in access and systemic bias [6]: the bottleneck inequalities quantify exactly how much relevance is lost when one encoder's knowledge is unavailable or its description is rate-limited.

### 5.3 Template 3: Quantified ignorance of continuous structure

The information dimension rate supplies a template for measuring how ignorant a discrete representation is of continuous structure. For an L-variate stationary process, the rate is d = H′([Xₜ]ₘ)/log m as m → ∞, where [Xₜ]ₘ is the process quantized at step 1/m [5]. The rate is bounded when the coarsely quantized process [X₁]₁ has finite entropy, is invariant under scaling and translation, and for Gaussian processes is computed from the matrix-valued spectral distribution; normalizing component processes to unit variance does not affect it [5]. Read as a template for observing ignorance: an agent whose representations are always coarsely quantized at some finite m holds a description whose information content about the underlying process is measured by d. The gap between d and the dimension the agent's model assumes is a quantified unknown unknown at the representational level: the agent cannot detect the gap from within its own quantization, exactly as the awareness square's m < 0.5 corner describes at the agent level. The invariance under scaling and translation [5] is the formal statement that some gaps are invisible from within: changing the units of the agent's representation does not change what the representation is ignorant of.

### 5.4 Synthesis

The three templates cover the three measurement questions the awareness square raises. Template 1 measures the return on raising m (representing the gap) versus raising k (representing more content), with the journey result suggesting m-returns exceed k-returns per parameter invested [1]. Template 2 measures the relevance cost of gaps in a collective, giving the societal layer of the spectrum a quantitative form [4]. Template 3 measures the ignorance of a representation about the structure it discretizes, giving the unknown unknown a number [5]. Together they convert the phenomenological spectrum of [6] and the shaping forces of [7] into measurable quantities.

## 6. Discussion

### 6.1 What the formal account adds and what it cannot claim

The formal account adds three things to the phenomenological corpus: a two-variable state definition from which the four states follow; a priced transition showing that moving from unconscious to conscious incompetence changes the agent's decision criterion from maximax to maximin and is worth at most 4.8 utility units of information about the unknown probability in the worked example; and three measurement templates. It cannot claim that the 4.8-unit figure generalizes—the number is specific to the worked example's utility table, and the linear loss structure follows from the two-state, two-action setup. It also cannot claim that the maximax model of unconscious incompetence is the only model: an agent at that corner might equally follow a habit policy or a copied policy, and the bracketing result would need rederivation. The claim retained is the structural one: the awareness state determines the decision criterion, and the criterion determines the loss profile.

### 6.2 Falsifiability

The main result is falsifiable in three ways. First, if agents at the unconscious-incompetence corner systematically follow maximin rather than maximax-style unrepresented optimism in tasks structurally like the worked example, the claim that awareness state determines criterion is wrong. Second, if the offline return of journey-representing architectures were not an order of magnitude above content-deepening architectures per parameter in replication, the m-outperforms-k reading of Template 1 fails. Third, if the loss L(p) = max(0, 12p − 6) were not recovered in behavioral experiments with the Section 4.1 utility table—agents at the conscious corner choosing y and losing 4.8 expected units at p = 0.9—the pricing derivation is empirically wrong.

### 6.3 Limitations

- The awareness square uses binary thresholds (k, m relative to 0.5); the corpus describes a continuous dimmer [6], and the corner derivation is an idealization whose thresholds are modeling choices, not measurements.
- The pricing derivation assumes the agent's criterion set is exactly {maximin, maximax}; [2] characterizes when players follow each criterion in general games, and multi-action or multi-state extensions change the loss slopes.
- The m-outperforms-k reading of Template 1 rests on one industrial result [1]; the comparison of +9.2% journey parameters against +50% depth parameters is a per-parameter comparison across different architecture families and should be treated as suggestive, not established.
- Template 3 is an analogy at the representational level; no derivation connects an agent's quantization step to its meta-knowledge m, and the mapping from d to the awareness square is asserted, not proven.
- The societal reading of Template 2 maps rate-relevance inequalities onto information inequality qualitatively [4], [6]; no quantitative societal dataset is analyzed here.

## 7. Practical Implications and Engineering Pathways

### 7.1 An awareness audit

The account yields a four-question audit for any decision context, human or machine:

1. Which domain d is the decision in, and what is the agent's k there?
2. Does the agent represent gaps in d—what is m, operationally: does it seek, hedge, or defer when a gap is presented?
3. Is the agent's criterion maximin-style (gap represented) or maximax-style (gap unrepresented)? The criterion is observable from choice behavior, per Section 4.
4. What is the maximum willingness-to-pay for information that moves the agent from a subset belief to a probability measure—in the worked example, at most 4.8 units?

### 7.2 Engineering pathways

- System level: prefer architectures that represent the process structure (journeys, stages, feedback loops) over architectures that deepen within one stage; the measured reference is +9.2% parameters for +0.48% NDCG offline and +0.61% uncancelled bookers online against +50% parameters for 0.05–0.1% NDCG [1].
- Collective level: when pooling partial knowledge, budget each contributor's description rate against the bottleneck inequalities—R₁ ≥ I(X₁;V₁|X₂) and μ ≤ I(Y;V₁V₂) price each contribution given the others [4]; apply this to audit which contributor's gap costs the most relevance.
- Representational level: report the information content of a representation relative to the structure it discretizes, using the dimension-rate definition d = H′([Xₜ]ₘ)/log m [5]; a representation whose assumed dimension exceeds its measured d is ignorant of structure it cannot detect from within.
- Societal level: the shaping forces of family, community, culture, and language [7] determine the prior over (k, m); interventions should target m (gap representation—media literacy, exposure to diverse perspectives [7]) as well as k (content delivery), since the journey result suggests m-returns can exceed k-returns per unit invested [1].

### 7.3 What would change practice

A measured replication of the m-versus-k comparison across architecture families, or a behavioral confirmation of the L(p) loss profile, would convert the audit of Section 7.1 from a checklist into a calibrated instrument. Until then, the audit's questions are answerable qualitatively, and the numbers in this paper serve as worked reference points, not calibrated constants.

## 8. Conclusion

Observing ignorance is possible because the awareness state leaves traces in choice behavior: an agent that cannot represent its gaps follows unrepresented optimism, and an agent that can follows guaranteed-value pessimism, with the loss between them linear in the unknown probability and worth at most 4.8 utility units in the worked example. The four states of the information spectrum are the corners of a two-variable state space, the transition between them is priced by decision theory under coarse subset beliefs, and three formal literatures supply the measurement templates for raising meta-knowledge, pooling partial knowledge, and quantifying the ignorance of continuous structure. The journey through the spectrum is not about reaching complete knowledge; it is about knowing which corner of the square one occupies, and what it would cost to move.

## References

[1] arXiv:2305.18431v1 — Optimizing Airbnb Search Journey with Multi-task Learning.
[2] arXiv:2103.08319v4 — Optimism and Pessimism in Strategic Interactions under Ignorance.
[3] arXiv:1812.08594v1 — Mind before matter: reversing the arrow of fundamentality.
[4] arXiv:1604.01433v4 — Collaborative Information Bottleneck.
[5] arXiv:1712.07863v1 — On the Information Dimension of Multivariate Gaussian Processes.
[6] QNFO: Part I: Observing Ignorance — https://papers.qnfo.org/papers/chapter-1.
[7] QNFO: 2. The Shaping of Unawareness — https://papers.qnfo.org/papers/chapter-2.