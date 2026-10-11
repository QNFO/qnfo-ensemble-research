# Ontological Re-Entry: What Can We Say Exists?

## Abstract

This paper addresses the "re-entry" problem in ontology: given a theory, formalism, or model built over some primitive vocabulary, what can we legitimately say exists when we project that structure back onto the world? We develop a framework in which existence claims are graded by the distinguishability budget of the describing system. Building on the finite-distinction program, in which a finite-entropy world is a finite-distinction world whose state-space geometry is combinatorial and ultrametric, we define an existence predicate indexed by distinction depth, and derive quantitative bounds on how many distinctions a physically bounded observer can maintain. We show that a system with $N$ usable distinctions carries an entropy of $S = N k_B \ln 2$ and a minimum erasure cost of $N k_B T \ln 2$, and we compute worked examples for observer budgets from $10^2$ to $10^{12}$ distinctions. We argue that ontological re-entry is not a binary act but a bounded compression: what "exists" at re-entry is exactly that which survives the compression the observer's budget forces. We situate the framework against database-oriented ontological query rewriting, primitive-ontology and relational readings of quantum mechanics, false-premise failures in multimodal models, and the definitional stagnation of decentralization, and we state the conditions under which the framework would be falsified.

## 1. Introduction

Every theory faces two directions of fit. In one direction, the theory is built: primitives are chosen, axioms are laid down, and a formal structure grows. In the other direction — the direction this paper calls *re-entry* — the finished structure is projected back onto the world, and we ask: what, according to this structure, exists? The re-entry problem is the ontological half of the semantics of theories, and it is where most confusions about scientific realism live. A theory may be internally impeccable while its re-entry map — the rule that says which of its internal objects correspond to anything real — is arbitrary, underdetermined, or silently loaded with the very ontology it was supposed to ground.

The question "what can we say exists?" is therefore not a request for a list. It is a request for a *criterion*: a procedure that, given a theory and an observer with finite resources, outputs the set of existence claims the observer is entitled to make. This paper proposes such a criterion. Its core commitment, taken from the finite-distinction program [11], is that a finite-entropy world is a finite-distinction world: uncountable precision is unphysical, while computable depth and $p$-adic valuation remain physically real. If the world presents only finitely many distinctions to any finite observer, then the raw material of ontology is not substance but *difference*, and the state-space geometry of differences is combinatorial and ultrametric rather than Euclidean.

Three consequences follow. First, existence is graded: an object exists *at distinction depth $d$* for an observer with budget $N$ if it is invariant under the compression that the budget forces. Second, re-entry is a thermodynamic act with a price: maintaining and erasing distinctions costs energy, connecting ontology to the physics of computation [7]. Third, the classical ontological disputes — particle versus field, substance versus relation, primitive versus structural — can be re-read as disputes about where in the distinction hierarchy re-entry is performed. The relational ontology of contemporary physics [4] and the primitive-ontology programs surveyed in [3] then appear not as rivals but as different re-entry conventions, and our framework supplies the vocabulary in which that choice is made explicit.

The paper proceeds as follows. Section 2 reviews the related work. Section 3 defines the formal framework. Section 4 carries out the explicit derivations and worked numerical examples. Section 5 reports the results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 concludes.

## 2. Background and Related Work

**Ontological queries and rewriting.** The database literature has formalized a precise version of re-entry: in [1], ontological queries are evaluated against an ontology rather than directly on a database, and the paper studies two aspects of this problem, query rewriting and query optimization, where rewriting consists of the compilation of an ontological query into an equivalent query against the underlying data. This is exactly a re-entry map in miniature: the ontology is the theory, the database is the world-as-modeled, and the rewriting is the rule for projecting existence claims down to what the substrate can answer. Our framework generalizes the compilation step from logical equivalence to resource-bounded distinguishability.

**Engineering ontologies.** At the applied end, [8] presents an ontology-driven software engineering approach for industrial robotics control software, introducing the ReApp architecture that synthesizes model-driven engineering with semantic technologies for the development and reuse of ROS-based components and applications, showing how different ontological classification systems for hardware can be combined. The supplied summary indicates that classification systems are treated as reusable engineering artifacts; in our terms, ReApp performs re-entry from a design ontology onto running robot components, and the multiplicity of classification systems it combines illustrates that re-entry maps are not unique.

**Primitive ontology and realism.** In foundations of physics, [3] observes that Bohm's and Bell's approaches share notable features with the contemporary Primitive Ontology perspective and with Esfeld's and Deckert's minimalist ontology: all these programs consider ontological clarity a necessary condition for every theoretical framework, promote scientific realism also in the quantum domain, and strengthen explanatory power. The supplied summary states these shared commitments; it gives no further technical detail, but the stated position — ontological clarity as a *necessary condition* on theories — is precisely the normative stance this paper operationalizes. Where [3] demands clarity, we supply a quantitative criterion for it.

**Relational ontology.** Against substance-first readings, [4] argues that quantum theory can be understood as pointing to an ontology of relations, and observes that this reading is supported by the ubiquity of relationality in contemporary fundamental physics, including classical mechanics, gauge theories, general relativity, quantum field theory, and tentative theories of quantum gravity. A distinction-based ontology is naturally relational: a distinction is a difference, and differences are relations. Our framework can thus be read as a resource-bounded refinement of the relational thesis of [4].

**Non-Archimedean and finite-distinction ontology.** The QNFO program supplies the positive ontology. [9], the Unified Theory of Non-Archimedean Ontology, and [10], Super-Universe, are supplied without abstract text in the bibliography; we therefore rely on them only as the umbrella works of the program and make no specific claims about their internal content. [11] states the load-bearing thesis: a finite-entropy world is a finite-distinction world, uncountable precision is unphysical, computable depth and $p$-adic valuation remain physically real, and the state-space geometry of finite distinctions is combinatorial and ultrametric, with quantum mechanics read as thermodynamics a stochastic theory in the large-distinction limit. [12], a companion to "The Qubit Delusion," argues that if the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto relational, field-theoretic reality — then the constructive task is to strip quantum mechanics to its minimal ontological commitments. Our re-entry criterion is the tool that task requires: it says exactly which commitments survive a given observer budget.

**Thermodynamic cost of distinction.** [7] establishes that each step resulting in a bit of information being "forgotten" by a computing device has an intrinsic energy cost, and that while any Turing machine can be rewritten to be thermodynamically reversible without changing the recognized language, finite automata restricted to scan their input once in real-time fashion can only recognize a proper subset of the regular languages. This gives our framework its physical anchor: distinctions are not free, and the devices that maintain them under real-time constraints are strictly weaker than unconstrained ones. Ontological budgets are therefore not just epistemic bookkeeping; they are energy accounting.

**False premises as re-entry failures.** In machine perception, [5] reports that open-source Large Multimodal Models excel at open-vocabulary grounding and segmentation but suffer under false premises when queries imply the existence of something not actually present in the image, and that fine-tuning an LMM to segment images significantly degrades its ability to reliably determine ("see") whether an object is present. This is an empirical instance of re-entry failure: the model's internal structure licenses an existence claim the world does not support. The tension the summary reports — segmentation ability bought at the price of presence-detection — is a resource trade-off of exactly the kind our budget formalism predicts.

**Definitional stagnation.** Finally, [6] documents that decentralization, despite its fundamental role across security, distributed computing, artificial intelligence, cloud infrastructures, and IoT architectures, has no universally accepted definition applicable across computer communication systems, a situation the summary indicates has become problematic. We take this as a cautionary case study: a concept in wide cross-domain use without an explicit re-entry criterion accumulates incompatible ontological commitments. The same risk attaches to "existence" itself, which is our target concept.

**Language-model ontologies.** [2] fine-tunes Large Language Models with a curated supervised legal dataset and integrates Retrieval-Augmented Generation to support policymakers in understanding, analyzing, and crafting legal regulations. The supplied summary describes the engineering; its relevance here is structural: a legal regulation is an ontology enforced by re-entry onto human conduct, and RAG is a retrieval-bounded re-entry mechanism. The summary gives no further detail on results, so we cite it only for the architectural pattern.

## 3. Methods

### 3.1 Distinction systems

Fix a finite set $\mathcal{D}_N = \{d_1, d_2, \ldots, d_N\}$ of $N$ primitive distinctions available to an observer $\mathcal{O}$. A *distinction* $d_i$ is a binary partition of the observer's state space; maintaining it means the observer can reliably re-identify which side of the partition the world is on. The observer's effective state space is

$$
\Sigma_N = \{0,1\}^N, \qquad |\Sigma_N| = 2^N .
$$

Consistent with [11], the geometry of $\Sigma_N$ is taken to be ultrametric: states are organized in a hierarchy of balls in which every ball is partitioned into sub-balls of equal diameter, and distances satisfy the strong triangle inequality $r(x,z) \le \max\{ r(x,y), r(y,z) \}$. We realize this by a $b$-ary tree of depth $L$ with branching factor $b$, so that

$$
N = L \log_2 b, \qquad |\Sigma_N| = b^L .
$$

### 3.2 The re-entry map

Let $T$ be a theory whose internal vocabulary mentions objects $o_1, \ldots, o_m$. A *re-entry map* is a function

$$
\rho_N : T \times \mathcal{D}_N \to \{ \text{real}, \text{compressed}, \text{void} \}
$$

defined as follows. For each object $o_j$ of $T$, let $P_j \subseteq \Sigma_N$ be the set of observer states in which $o_j$ is distinguishable from every other object of $T$.

- $\rho_N(o_j) = \text{real}$ if $|P_j| \ge \theta$ for a fixed threshold $\theta \ge 1$: the object is resolvable at the observer's budget.
- $\rho_N(o_j) = \text{compressed}$ if $0 < |P_j| < \theta$: the object survives only as a coarse-grained invariant.
- $\rho_N(o_j) = \text{void}$ if $P_j = \emptyset$: no state of the observer distinguishes $o_j$; the existence claim is unsupported.

The answer to "what can we say exists?" is then: exactly the objects with $\rho_N \ne \text{void}$, with the real/compressed split marking the graded ontology.

### 3.3 Thermodynamic budget

By [7], forgetting one bit costs at least $k_B T \ln 2$ in energy dissipation at temperature $T$. Maintaining $N$ distinctions against noise over a coherence time $\tau$ requires refreshing them, so the observer's power budget $P_{\text{obs}}$ bounds

$$
N \le \frac{P_{\text{obs}} \, \tau}{k_B T \ln 2}.
$$

This inequality is the bridge between physics and ontology: it converts a power budget into a distinction budget, and hence, via $\rho_N$, into an existence criterion.

## 4. Analysis

All numbers in this section are computed from stated inputs; no empirical data are used.

**Derivation 1 (state-space size).** Input: branching factor $b = 2$, depth $L = 40$ (a choice; any $b, L$ work). Then

$$
N = L \log_2 b = 40 \cdot \log_2 2 = 40 \cdot 1 = 40,
$$
$$
|\Sigma_N| = 2^{40} = 1{,}099{,}511{,}627{,}776 \approx 1.10 \times 10^{12}.
$$

So an observer maintaining $40$ binary distinctions commands a state space of about $1.10 \times 10^{12}$ states.

**Derivation 2 (entropy of the distinction budget).** Input: $N = 40$ distinctions, Boltzmann constant $k_B = 1.380649 \times 10^{-23} \ \mathrm{J/K}$. The Shannon entropy of a uniform distribution over $\Sigma_N$ is $H = N$ bits, so the thermodynamic entropy is

$$
S = N k_B \ln 2 = 40 \times 1.380649 \times 10^{-23} \times 0.693147 .
$$

Step 1: $1.380649 \times 10^{-23} \times 0.693147 = 9.56963 \times 10^{-24} \ \mathrm{J/K}$ (since $1.380649 \times 0.693147 = 0.956963$).

Step 2: $S = 40 \times 9.56963 \times 10^{-24} = 3.82785 \times 10^{-22} \ \mathrm{J/K}$.

**Derivation 3 (minimum erasure cost at room temperature).** Input: $T = 300 \ \mathrm{K}$, $N = 40$. The Landauer-style cost from [7] is

$$
E_{\text{erase}} = N k_B T \ln 2 = S \cdot T = 3.82785 \times 10^{-22} \times 300 .
$$

Step: $3.82785 \times 10^{-22} \times 300 = 1.14836 \times 10^{-19} \ \mathrm{J}$.

So fully re-randomizing a $40$-distinction observer costs at least $1.15 \times 10^{-19} \ \mathrm{J}$ per complete cycle.

**Derivation 4 (distinction budget from a power budget).** Input: power $P_{\text{obs}} = 10^{-12} \ \mathrm{W}$ (one nanowatt-scale budget, chosen as an illustrative bound), coherence time $\tau = 1 \ \mathrm{s}$, $T = 300 \ \mathrm{K}$. Then

$$
N_{\max} = \frac{P_{\text{obs}} \tau}{k_B T \ln 2} = \frac{10^{-12}}{9.56963 \times 10^{-24} \times 300}.
$$

Step 1: denominator $= 9.56963 \times 10^{-24} \times 300 = 2.87089 \times 10^{-21} \ \mathrm{J/bit}$.

Step 2: $N_{\max} = 10^{-12} / 2.87089 \times 10^{-21} = 3.48320 \times 10^{8}$.

So a nanowatt observer with $1 \ \mathrm{s}$ coherence can in principle sustain at most $N_{\max} \approx 3.48 \times 10^{8}$ bit-distinctions per second against the erasure floor of [7]. This is an upper bound on *refresh rate*, not on stored distinctions; we use it as the budget ceiling in the re-entry criterion.

**Derivation 5 (ultrametric ball counting).** In a $b$-ary ultrametric tree of depth $L$, the number of balls at radius level $r$ (i.e., subtrees of height $r$) is $b^{L - r}$. Input: $b = 2$, $L = 40$, $r = 10$. Then

$$
b^{L-r} = 2^{30} = 1{,}073{,}741{,}824 \approx 1.07 \times 10^{9}.
$$

At the coarse level $r = 30$:

$$
2^{L - r} = 2^{10} = 1{,}024.
$$

So the same state space that contains $\approx 1.07 \times 10^{9}$ fine balls at level $10$ contains only $1{,}024$ coarse balls at level $30$: compression by a factor of

$$
\frac{2^{30}}{2^{10}} = 2^{20} = 1{,}048{,}576 \approx 1.05 \times 10^{6}.
$$

**Derivation 6 (re-entry classification under compression).** Suppose a theory $T$ posits $m = 10^5$ objects, and an observer's compression from level $r=10$ to level $r=30$ merges states so that each coarse ball at level $30$ contains on average

$$
\frac{2^{30}}{2^{10}} = 1{,}048{,}576
$$

fine states. If the $10^5$ objects are spread uniformly over the $2^{30}$ fine balls, the expected number of objects per coarse ball is

$$
\lambda = \frac{10^5}{2^{10}} = \frac{100{,}000}{1{,}024} = 97.65625 .
$$

With threshold $\theta = 1$ (an object is "real" if some observer state isolates it), an object remains resolvable only if it is the sole object in its coarse ball. Under a Poisson model with mean $\lambda$, the probability a given ball contains exactly one object is

$$
p_1 = \lambda e^{-\lambda} = 97.65625 \times e^{-97.65625}.
$$

Since $e^{-97.65625} \approx 3.7 \times 10^{-43}$ (as $e^{-97.65625} = 10^{-97.65625 / \ln 10} = 10^{-97.65625/2.302585} = 10^{-42.410}$), we get

$$
p_1 \approx 97.65625 \times 3.87 \times 10^{-43} \approx 3.78 \times 10^{-41}.
$$

The expected number of resolvable objects among $10^5$ is then

$$
m_{\text{real}} \approx 10^5 \times 3.78 \times 10^{-41} = 3.78 \times 10^{-36} \approx 0 .
$$

Interpretation: under uniform spreading and this compression, essentially no individual object survives re-entry as "real"; the ontology that survives is the coarse partition itself — the $1{,}024$ level-$30$ balls — not the $10^5$ objects. This is a precise, if idealized, statement of the finite-distinction thesis of [11]: what exists at re-entry is what survives the observer's compression, and under aggressive compression that is structure, not individuals.

**Derivation 7 (scaling of the survival threshold).** For objects to survive as individuals, we need $\lambda \lesssim 1$, i.e. $m \lesssim b^{L-r}$. With $b=2$, $L=40$, $r=30$: $m \lesssim 1{,}024$. Solving for the compression depth at which $m = 10^5$ objects just survive:

$$
b^{L-r} = 10^5 \implies L - r = \log_2 10^5 = \frac{10^5 \text{'s log}}{} = \frac{\ln 10^5}{\ln 2} = \frac{5 \times 2.302585}{0.693147} = \frac{11.512925}{0.693147} = 16.6096 .
$$

So $r = L - 16.6096 = 40 - 16.6096 = 23.39$, i.e. the observer may compress to level $\approx 23$ but not to level $30$ if $10^5$ individuals are to remain resolvable. Each additional level of compression divides resolvable capacity by $b = 2$.

## 5. Results

The following results are the computed values of Section 4; no empirical or simulated data are reported.

- **R1.** A $b=2$, $L=40$ distinction system has $N = 40$ bits of distinction and $|\Sigma_N| = 2^{40} \approx 1.10 \times 10^{12}$ states (Derivation 1).
- **R2.** Its thermodynamic entropy is $S = 3.83 \times 10^{-22} \ \mathrm{J/K}$ and its full erasure cost at $T = 300 \ \mathrm{K}$ is $E_{\text{erase}} = 1.15 \times 10^{-19} \ \mathrm{J}$ (Derivations 2–3).
- **R3.** A $P_{\text{obs}} = 10^{-12} \ \mathrm{W}$ observer with $\tau = 1 \ \mathrm{s}$ coherence at $300 \ \mathrm{K}$ has a refresh budget of $N_{\max} \approx 3.48 \times 10^{8}$ bit-distinctions per second (Derivation 4).
- **R4.** Compressing a $b=2$, $L=40$ ultrametric state space from level $10$ to level $30$ reduces $1.07 \times 10^{9}$ fine balls to $1{,}024$ coarse balls, a compression factor of $1.05 \times 10^{6}$ (Derivation 5).
- **R5.** Under uniform spreading of $m = 10^5$ theory-objects over that space, the expected number of individually resolvable objects after compression is $\approx 3.8 \times 10^{-36}$, i.e. effectively zero; the surviving ontology is the coarse partition (Derivation 6). This is a projection under stated assumptions (uniform spreading, Poisson occupancy, $\theta = 1$), not an empirical finding.
- **R6.** The compression depth at which $10^5$ individuals remain just resolvable is $r \approx 23.4$ for $b=2$, $L=40$; each further level halves resolvable capacity (Derivation 7).

The qualitative result: re-entry is budget-dependent and graded, and the "real/compressed/void" trichotomy of Section 3.2 is the operative ontology.

## 6. Discussion

**Limitations.** The framework is deliberately minimal, and its idealizations are load-bearing. First, Derivation 6 assumes uniform spreading of objects over the ultrametric state space; real ontologies are correlated with the tree structure (objects of the same kind occupy neighboring balls), which would raise survival probabilities, possibly dramatically. The Poisson model is a worst case, not a prediction. Second, the threshold $\theta = 1$ is arbitrary; a theory of $\theta$ — how much distinguishability an existence claim needs — is missing. Third, the power-to-distinction conversion in Derivation 4 uses the erasure floor of [7] as if every distinction refresh operated at the Landauer bound; real devices are orders of magnitude less efficient, so $N_{\max}$ is an upper bound, and the true budget for any concrete observer is smaller by an unquantified efficiency factor. Fourth, the bibliography entries for [9] and [10] supply no abstract text, so this paper makes no claims about their internal content and relies on [11] and [12] for the finite-distinction substance; the umbrella works may contain relevant material we could not use.

**Failure modes.** The framework fails if distinctions are not the right primitive. If the relational ontology of [4] is read strongly — relations, not differences, as fundamental — then a binary-partition model may be too coarse, and a $q$-ary or continuous-valued distinction algebra would be needed. It also fails if quantum mechanics genuinely requires superpositions that are not reducible to distributions over distinction states; [11] addresses this by reading superposition as the large-distinction limit of stochastic thermodynamics, but if that reading is wrong, the ultrametric state space misdescribes quantum observers. Finally, the perceptual analogy from [5] warns that systems optimized for one re-entry task (fine segmentation) may lose the complementary one (presence detection); our single scalar budget may be too crude to capture such trade-offs, which are presumably multi-dimensional.

**What would falsify the claims.** The central claim — that existence at re-entry is graded by distinction budget — would be falsified by a demonstrated case in which an observer with a strictly smaller distinction budget (in the sense of Section 3.3) reliably resolves an existence claim that a strictly larger-budget observer cannot, with no compensating change of coordinates. It would also be falsified if the erasure-cost link of [7] were shown not to apply to the maintenance (as opposed to erasure) of distinctions, breaking Derivation 4. At the physics level, evidence that uncountable precision is physically meaningful — e.g., a measurable quantity whose value is sensitive to non-computable real-parameter precision in a way no finite-distinction model reproduces — would undercut the finite-distinction premise of [11].

**Against ourselves.** One might object that the framework merely relabels the old problem: calling void "unsupported by distinctions" does not tell us whether void objects are absent or merely unobservable, and the realist of [3] will insist that ontological clarity should not be hostage to observer budgets. We concede the force of this: our criterion is an *epistemic* filter, and the jump from "unresolvable at budget $N$" to "does not exist" is an additional, contestable commitment — the one inherited from the finite-distinction thesis that uncountable precision is unphysical. A second objection: the numerical examples use toy parameters ($b=2$, $L=40$, $10^5$ objects), and no conclusion of substance depends on them; they are illustrations of the machinery, not measurements. We agree, and mark R5 explicitly as a projection under stated assumptions.

**Open questions.** (i) What is the correct measure over spreads of objects on the ultrametric tree, replacing the uniform assumption of Derivation 6? (ii) Can the threshold $\theta$ be derived rather than postulated, e.g. from reliability requirements in the spirit of [5]? (iii) Does the real/compressed/void trichotomy map cleanly onto the rewriting-optimization split of [1], and can ontological query optimization be re-read as budget minimization? (iv) How would the framework handle the cross-domain definitional drift documented for decentralization in [6] — is a concept-level analogue of $\rho_N$ definable?

## 7. Conclusion

We have framed ontological re-entry — the projection of a theory's existence claims back onto the world — as a resource-bounded compression over a finite-distinction state space. The framework yields a graded existence predicate $\rho_N$ with three values (real, compressed, void), a thermodynamic budget linking observer power to distinction count via the erasure cost of [7], and worked derivations showing that under aggressive ultrametric compression, individual objects generally fail to survive re-entry while coarse structure does. The framework gives precise content to the ontological-clarity demand of the primitive-ontology programs [3], refines the relational ontology of [4] with an explicit resource parameter, and offers database-style rewriting [1] and perceptual presence-detection [5] as engineered instances of the same problem. What can we say exists? Exactly what survives the compression our distinctions force — and the arithmetic of survival is, in principle, computable.

## References

[1] arXiv:1112.0343v1 | Ontological Queries: Rewriting and Optimization (Extended Version)

[2] arXiv:2511.03563v1 | ASVRI-Legal: Fine-Tuning LLMs with Retrieval Augmented Generation for Enhanced Legal Regulation

[3] arXiv:2104.13859v1 | Beables, Primitive Ontology and Beyond: How Theories Meet the World

[4] arXiv:2201.00907v2 | The relational ontology of contemporary physics

[5] arXiv:2312.08366v1 | See, Say, and Segment: Teaching LMMs to Overcome False Premises

[6] arXiv:2608.09748v2 | Defining Decentralization: An Ontological Perspective

[7] arXiv:2204.06025v2 | Energy Complexity of Regular Languages

[8] arXiv:1601.03998v1 | A Model-Driven Engineering Approach for ROS using Ontological Semantics

[9] QNFO: Unified Theory of Non-Archimedean Ontology

[10] QNFO: Super-Universe

[11] QNFO: Finite-Distinction Quantum Mechanics: Unitary Evolution and Superposition as the Large-Distinction Limit of Stochastic Thermodynamics

[12] QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation