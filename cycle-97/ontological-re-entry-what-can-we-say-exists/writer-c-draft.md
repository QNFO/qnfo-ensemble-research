# Ontological Re-Entry: What Can We Say Exists?

## Abstract

This paper addresses the "re-entry" problem in ontology: given a formal account of what exists, what can be coherently said — and computed — about existence itself when the describing system is finite? We develop a finite-distinction framework in which existence claims are admissible only when they are expressible as distinctions at finite resolution, and we connect this framework to three literatures that rarely speak to one another: ontological query rewriting in databases, primitive-ontology and relational readings of quantum mechanics, and the thermodynamic cost of information erasure. We formalize an ontology as a finite ultrametric distinction space and derive a counting bound on admissible existence predicates: a system of $N$ binary distinctions supports at most $2^{N}$ states and at most $2^{2^{N}}$ extensionally distinct existence predicates. We compute the minimal thermodynamic cost of maintaining or forgetting a distinction, $k_{B}T\ln 2 \approx 2.87 \times 10^{-21}\,\mathrm{J}$ at $T = 300\,\mathrm{K}$, and use it to bound the physical realizability of ontological commitment. We then define "ontological re-entry" as the operation by which a theory's existence claims are re-expressed inside the same finite distinction budget that generates them, and show that re-entry is well-defined exactly when the ontology admits a rewriting into queries over its own base distinctions, in analogy with ontological query compilation. The framework is illustrated against relational and primitive-ontology readings of quantum theory, and its failure modes — false-premise commitments, resolution collapse, and unpayable erasure costs — are analyzed explicitly.

## 1. Introduction

Every theory, formal or informal, carries commitments about what exists. The question "what can we say exists?" is therefore not a request for an inventory but for a criterion: under what conditions is an existence claim admissible, and what does answering it cost? This paper proposes that the criterion is finitary and the cost is literal. A finite observer — a database, a language model, a physical measuring device — can hold only finitely many distinctions. Anything it can say exists must be built from those distinctions. We call the operation of turning this observation back onto ontology itself *ontological re-entry*: the theory of existence is written using the same finite alphabet of distinctions whose existence it licenses.

The re-entry framing generates three questions that structure the paper. First, the *representational* question: what is the geometry of a space built only from finite distinctions, and how many distinct existence claims can it support? Second, the *physical* question: what does it cost, in thermodynamic terms, to hold or erase a distinction, and when does an ontological commitment become physically unpayable? Third, the *logical* question: when can an ontology's high-level existence claims be rewritten into statements over its own base distinctions without loss — the re-entry condition — and when does rewriting fail, leaving commitments that float free of the base?

These questions are not asked in a vacuum. Database research has a mature theory of evaluating and optimizing queries that are answered against an ontology rather than directly against data [1]; robotics software engineering composes ontological classification systems to make hardware and software components mutually intelligible [8]; and the concept of decentralization has been given an explicitly ontological analysis precisely because no cross-domain definition had stabilized [6]. On the physical side, the Primitive Ontology program and its relatives insist that ontological clarity is a necessary condition on any theoretical framework [3], while a relational reading finds support for an ontology of relations across classical mechanics, gauge theories, general relativity, quantum field theory, and tentative quantum gravity [4]. On the computational side, erasing a bit of information carries an intrinsic energy cost, and real-time finite automata pay a complexity price for forgetting [7]. Our own prior work supplies the finite-distinction setting: a finite-entropy world is a finite-distinction world in which uncountable precision is unphysical while computable depth and $p$-adic valuation remain physically real [11], with a companion constructive program for post-particle computation [12] and a broader non-Archimedean ontology [9][10].

The contributions are: (i) a formal definition of a finite distinction space and of admissible existence predicates over it, with explicit counting bounds (Section 3, computed in Section 4); (ii) a thermodynamic admissibility criterion derived from the erasure cost of distinctions [7]; (iii) a definition of ontological re-entry modeled on query rewriting against an ontology [1], with a necessary condition for re-entry to be lossless; and (iv) an analysis of failure modes, including false-premise commitments in the sense observed for multimodal models [5] and the definitional fragmentation documented for decentralization [6].

## 2. Background and Related Work

**Ontological queries in databases.** Ontological queries are evaluated against an ontology rather than directly on a database, and their evaluation and optimization constitute a distinct research problem; query rewriting compiles an ontological query into an equivalent query against the underlying data [1]. This is the closest formal precedent for our re-entry condition: [1] establishes that existence-flavored commitments encoded in an ontology can, in favorable cases, be compiled away into base-level queries. We borrow the rewriting/optimization split — first rewrite, then optimize — as the template for Section 3.4, and note where the analogy is exact and where it breaks (ontologies of existence have no "underlying database" other than the distinction space itself).

**Ontological clarity in physics.** The Primitive Ontology tradition, together with Bohm's and Bell's approaches and the minimalist ontology of Esfeld and Deckert, treats ontological clarity as a necessary condition on every theoretical framework, promotes scientific realism in the quantum domain, and aims to strengthen explanatory power [3]. Our admissibility criterion is a finitary sharpening of this demand: clarity is not only a desideratum but a countable and priced property. Separately, the relational ontology program argues that quantum theory points to an ontology of relations, observing that relationality is ubiquitous in contemporary fundamental physics including classical mechanics, gauge theories, general relativity, quantum field theory, and tentative quantum gravity [4]. In our terms, a relational ontology is the claim that the base distinctions are distinctions *between* entities rather than monadic predicates — a claim our framework can represent but not adjudicate; we return to it in Section 6.

**Ontologies in engineering practice.** The ReApp architecture synthesizes model-driven engineering with semantic technologies for industrial robotics control software, showing how different ontological classification systems for hardware and software components can be combined to support development and reuse [8]. This matters for us as evidence that ontologies are operational artifacts whose commitments are executed, not merely stated; an existence claim in a deployed robot controller is a commitment with runtime consequences. The supplied summary of [8] gives no further quantitative detail, and we use it only at this level.

**Definitional fragmentation.** Decentralization has existed as a concept in computer science for over half a century and plays a fundamental role across security, distributed computing, artificial intelligence, cloud infrastructures, and IoT architectures, yet no universally accepted cross-domain definition exists [6]. The supplied summary indicates this has become a recognized problem; for our purposes, [6] is a case study in what happens when a community maintains an ontology without an admissibility criterion: the term persists while its extension drifts. The summary supplied gives no further detail on the proposed remedy, and we do not attribute one to it.

**False premises.** Open-source Large Multimodal Models excel at open-vocabulary grounding and segmentation but suffer under false premises — queries that imply the existence of something not actually present in the image — and fine-tuning an LMM to segment images significantly degrades its ability to reliably determine whether an object is present [5]. This is an empirical instance of our central failure mode: a system whose output grammar presupposes existence can be induced to affirm nonexistent entities. The summary supplied cuts off before describing the proposed remedy, so we cite [5] only for the observed degradation phenomenon.

**Thermodynamic cost of distinction.** Each computational step that results in a bit of information being forgotten has an intrinsic energy cost; any Turing machine can be rewritten to be thermodynamically reversible without changing the recognized language, but finite automata restricted to scan their input once in real-time fashion recognize only a proper subset of the regular languages [7]. Two consequences feed directly into our framework: reversibility is always available in principle at the price of keeping distinctions (never erasing them), and forgetting is not free — it is precisely what partitions the expressible from the efficiently expressible. Our Section 4.2 prices a single erasure event.

**The finite-distinction program.** Our prior work states that a finite-entropy world is a finite-distinction world: uncountable precision is unphysical, while computable depth and $p$-adic valuation remain physically real, and the state-space geometry of finite distinctions is combinatorial and ultrametric; quantum mechanics read as thermodynamics is a stochastic theory whose unitary evolution and superposition emerge as the large-distinction limit [11]. The present paper is the ontological companion: [11] supplies the geometry and the thermodynamic reading of quantum theory; here we ask what existence claims that geometry can carry. The companion constructive program [12] argues that if the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto relational, field-theoretic reality — the constructive response is to strip quantum mechanics to its minimal ontological commitments; [12] is a companion paper to "The Qubit Delusion" (v1.1, 10.5281/zenodo.21254143). We use [12] as the computational downstream of the ontology developed here. Finally, the broader QNFO program [9] and its "Super-Universe" extension [10] are supplied as titles without abstracts; the summaries give no further detail, and we cite them only as the umbrella under which the non-Archimedean setting of [11] sits, making no claims about their contents beyond their titles.

**Language-model regulation, briefly.** Fine-tuning LLMs with curated supervised legal-domain data and retrieval-augmented generation has been explored to support policymakers in understanding, analyzing, and crafting legal regulations [2]. The supplied summary cuts off before reporting results; we invoke [2] only as an instance of a system whose outputs constitute de facto existence claims about legal entities — a domain where false-premise costs are institutional rather than perceptual — and draw no findings from it.

## 3. Methods

### 3.1 Distinction spaces

**Definition 3.1 (Distinction space).** A *distinction space* is a pair $D_{N} = (S_{N}, d_{u})$ where $S_{N} = \{0,1\}^{N}$ is the set of $N$-bit distinction records and $d_{u}: S_{N} \times S_{N} \to \mathbb{Q}_{\geq 0}$ is an ultrametric, i.e., $d_{u}(x_{i}, x_{j}) \leq \max\left(d_{u}(x_{i}, x_{k}), d_{u}(x_{k}, x_{j})\right)$ for all $x_{i}, x_{j}, x_{k} \in S_{N}$. The ultrametric requirement implements the finite-distinction geometry of [11]: balls in $D_{N}$ are hierarchically nested, mirroring the combinatorial, $p$-adic structure in which depth of distinction, not metric distance, carries the physical content.

**Definition 3.2 (Admissible existence predicate).** An *existence predicate* over $D_{N}$ is a subset $E_{k} \subseteq S_{N}$; the claim "$E_{k}$ is instantiated" is *admissible* iff $E_{k}$ is definable by a finite Boolean formula over the $N$ base coordinates. Two predicates are *extensionally equivalent* iff $E_{i} = E_{j}$ as sets.

### 3.2 Counting bound

**Proposition 3.1.** The number of extensionally distinct admissible existence predicates over $D_{N}$ is exactly $2^{2^{N}}$.

*Proof.* Each Boolean formula over $N$ coordinates defines a subset of $S_{N}$, and every subset of $S_{N}$ is defined by its characteristic formula (a disjunction over its members). Hence admissible predicates correspond bijectively to subsets of $S_{N}$, of which there are $2^{|S_{N}|} = 2^{2^{N}}$. $\square$

The bound is tight but syntactically unreachable: the number of *short* formulas is far smaller, and Section 4.1 quantifies the gap for a concrete budget.

### 3.3 Thermodynamic admissibility

Following [7], a step that forgets a bit has an intrinsic energy cost. We adopt the standard Landauer form as a modeling assumption (not derived here): erasing one bit at temperature $T_{\mathrm{env}}$ costs at least

$$E_{\mathrm{bit}} = k_{B} T_{\mathrm{env}} \ln 2,$$

where $k_{B}$ is Boltzmann's constant. A commitment is *thermodynamically admissible* for an agent with erasure budget $E_{\mathrm{budget}}$ and lifetime $\tau_{\mathrm{life}}$ if the distinctions it requires can be maintained without erasure exceeding budget; if the agent must cycle its memory at rate $f_{\mathrm{cycle}}$, the erasure power is

$$P_{\mathrm{erase}} = f_{\mathrm{cycle}} \, N_{\mathrm{dist}} \, k_{B} T_{\mathrm{env}} \ln 2,$$

with $N_{\mathrm{dist}}$ the number of distinctions cycled per cycle. Reversibility, per [7], removes the erasure cost but forces the agent to retain all distinctions — trading power for unbounded memory growth.

### 3.4 Ontological re-entry

**Definition 3.3 (Re-entry).** Let $\mathcal{O}$ be an ontology whose commitments are expressed in a high-level vocabulary $V_{\mathrm{high}}$, and let $V_{\mathrm{base}}$ be the base coordinates of $D_{N}$. *Re-entry* is a map $r: V_{\mathrm{high}} \to \mathcal{P}(S_{N})$ assigning each high-level predicate an admissible existence predicate. Re-entry is *lossless* iff for every pair of commitments $c_{i}, c_{j} \in \mathcal{O}$, all entailments among them are preserved under $r$.

This mirrors the compilation of an ontological query into an equivalent query against the underlying data [1], with $D_{N}$ playing the role of the underlying data. The re-entry condition fails when $V_{\mathrm{high}}$ contains predicates whose extension depends on precision beyond the $N$-bit budget — the "uncountable precision is unphysical" clause of [11].

## 4. Analysis

Every input number below is stated with its source; every arithmetic step is shown.

### 4.1 Counting admissible existence predicates

**Inputs.** $N = 64$ binary distinctions (a chosen illustrative budget, equal to one 64-bit machine word; source: this paper's modeling choice). Formula: Proposition 3.1.

**Step 1.** $|S_{N}| = 2^{N} = 2^{64} = 18{,}446{,}744{,}073{,}709{,}551{,}616 \approx 1.8447 \times 10^{19}$ states.

**Step 2.** Number of admissible predicates: $2^{2^{N}} = 2^{2^{64}} = 2^{18{,}446{,}744{,}073{,}709{,}551{,}616}$. In base-10 logarithms:

$$\log_{10}\left(2^{2^{64}}\right) = 2^{64} \log_{10} 2 \approx 1.8447 \times 10^{19} \times 0.30103 \approx 5.553 \times 10^{18}.$$

So there are $\approx 10^{5.553 \times 10^{18}}$ extensionally distinct existence predicates — combinatorially vast but finite.

**Step 3 (syntactic reachability).** Assume formulas are conjunctions of at most $k_{\mathrm{lit}} = 8$ literals chosen from $2N = 128$ literals (modeling choice). The number of conjunctions is at most

$$\binom{128}{8} + \binom{128}{7} + \cdots + \binom{128}{0}.$$

Compute the dominant term: $\binom{128}{8} = \dfrac{128!}{8! \, 120!}$. Stepwise: $\binom{128}{8} = \binom{128}{120} = \dfrac{128 \times 127 \times 126 \times 125 \times 124 \times 123 \times 122 \times 121}{40320}$.

Numerator, pairwise: $128 \times 127 = 16256$; $16256 \times 126 = 2{,}048{,}256$; $\times 125 = 256{,}032{,}000$; $\times 124 = 31{,}747{,}968{,}000$; $\times 123 = 3{,}905{,}000{,}064{,}000$; $\times 122 = 476{,}410{,}007{,}808{,}000$; $\times 121 = 5.7646 \times 10^{16}$ (precisely $476{,}410{,}007{,}808{,}000 \times 121 = 57{,}645{,}610{,}944{,}768{,}000$).

Divide: $57{,}645{,}610{,}944{,}768{,}000 / 40320 \approx 1.4298 \times 10^{12}$. The remaining terms $\sum_{j=0}^{7}\binom{128}{j}$ are smaller by factors of at least $121/8 \approx 15$ each, so the total is $\approx 1.43 \times 10^{12} \times (1 + 1/15 + \cdots) \approx 1.53 \times 10^{12}$ short conjunctions.

**Conclusion 4.1.** With $N = 64$, the fraction of admissible predicates reachable by short formulas is $\approx 1.53 \times 10^{12} / 10^{5.553 \times 10^{18}}$, i.e., effectively zero relative to the full space. Ontological expressiveness is therefore bottlenecked by *syntax*, not by the state space: re-entry must route through structured (hierarchical, ultrametric) definitions, consistent with the nested-ball geometry of [11].

### 4.2 Erasure cost of a distinction

**Inputs.** $k_{B} = 1.380649 \times 10^{-23}\,\mathrm{J\,K^{-1}}$ (SI defined value); $T_{\mathrm{env}} = 300\,\mathrm{K}$ (room-temperature modeling choice); $\ln 2 = 0.693147$ (mathematical constant). Formula: $E_{\mathrm{bit}} = k_{B} T_{\mathrm{env}} \ln 2$ [7].

**Step 1.** $k_{B} T_{\mathrm{env}} = 1.380649 \times 10^{-23} \times 300 = 4.141947 \times 10^{-21}\,\mathrm{J}$.

**Step 2.** $E_{\mathrm{bit}} = 4.141947 \times 10^{-21} \times 0.693147 = 2.8709 \times 10^{-21}\,\mathrm{J}$.

**Step 3 (cycling cost).** Assume an agent maintains $N_{\mathrm{dist}} = 10^{9}$ distinctions and rewrites (erases-and-replaces) each once per second, $f_{\mathrm{cycle}} = 1\,\mathrm{s^{-1}}$ (modeling choices). Then

$$P_{\mathrm{erase}} = 1 \times 10^{9} \times 2.8709 \times 10^{-21} = 2.8709 \times 10^{-12}\,\mathrm{W}.$$

**Conclusion 4.2.** At $10^{9}$ distinctions cycled at $1\,\mathrm{s^{-1}}$, the minimal erasure power is $\approx 2.87 \times 10^{-12}\,\mathrm{W}$ — negligible for silicon-scale hardware but a hard floor that scales linearly in both $N_{\mathrm{dist}}$ and $f_{\mathrm{cycle}}$; an agent cycling $10^{20}$ distinctions at $10^{9}\,\mathrm{s^{-1}}$ would require $P_{\mathrm{erase}} = 10^{20} \times 10^{9} \times 2.8709 \times 10^{-21} = 2.87 \times 10^{8}\,\mathrm{W}$, which is physically prohibitive. Thermodynamic admissibility thus bites at the large-distinction limit that [11] identifies with quantum-mechanical behavior.

### 4.3 Resolution collapse and re-entry failure

**Inputs.** A high-level predicate $c_{i}$ requires distinguishing states differing in the $m$-th coordinate at depth $d_{m}$; the budget $N = 64$ (Section 4.1). Suppose $c_{i}$'s extension depends on $n_{\mathrm{prec}} = 100$ bits of precision (modeling choice: the predicate separates states that agree on the first $64$ coordinates). Then $n_{\mathrm{prec}} > N$ and no admissible predicate over $D_{64}$ separates them: re-entry for $c_{i}$ fails by Definition 3.3, since $r(c_{i})$ cannot be defined. The fraction of predicate pairs affected grows with the precision demand; for predicates demanding $n_{\mathrm{prec}}$ bits, the required state space is $2^{n_{\mathrm{prec}}}$, and the excess factor is

$$\frac{2^{n_{\mathrm{prec}}}}{2^{N}} = 2^{n_{\mathrm{prec}} - N} = 2^{36} \approx 6.872 \times 10^{10}$$

for $n_{\mathrm{prec}} = 100$, $N = 64$: the predicate's extension lives in a space $6.872 \times 10^{10}$ times finer than the budget supports. This is the formal content of "uncountable precision is unphysical" [11] rendered as a re-entry failure.

## 5. Results

All numbers below are those computed in Section 4; no empirical measurements are reported.

**R1 (Counting bound).** A distinction space with $N = 64$ base distinctions supports $2^{64} = 18{,}446{,}744{,}073{,}709{,}551{,}616 \approx 1.8447 \times 10^{19}$ states and exactly $2^{2^{64}} \approx 10^{5.553 \times 10^{18}}$ extensionally distinct admissible existence predicates (Proposition 3.1, Section 4.1).

**R2 (Syntactic bottleneck).** Under the stated assumption of conjunctions of at most $8$ literals from $128$ literals, only $\approx 1.53 \times 10^{12}$ short conjunctions are available — a vanishing fraction of the admissible space (Section 4.1, Conclusion 4.1). Ontological re-entry must therefore exploit hierarchical structure rather than flat enumeration.

**R3 (Erasure floor).** The minimal energy to erase one distinction at $T_{\mathrm{env}} = 300\,\mathrm{K}$ is $E_{\mathrm{bit}} = 2.8709 \times 10^{-21}\,\mathrm{J}$ (Section 4.2). Cycling $10^{9}$ distinctions at $1\,\mathrm{s^{-1}}$ costs $P_{\mathrm{erase}} = 2.8709 \times 10^{-12}\,\mathrm{W}$; scaling to $10^{20}$ distinctions at $10^{9}\,\mathrm{s^{-1}}$ costs $2.87 \times 10^{8}\,\mathrm{W}$, which we label a *projection* under the stated linear-scaling assumption and constant temperature.

**R4 (Re-entry failure threshold).** A predicate requiring $n_{\mathrm{prec}} = 100$ bits of precision against a $64$-bit budget is non-re-enterable; its extension demands a state space finer by a factor $2^{36} \approx 6.872 \times 10^{10}$ (Section 4.3). This is a structural result under the stated modeling choices, not an empirical measurement.

## 6. Discussion

**Limitations.** The counting bound of Proposition 3.1 is exact but uninformative about *useful* predicates; the syntactic-reachability figure in R2 depends entirely on the chosen formula class (conjunctions of $\leq 8$ literals), and a different class — e.g., allowing nested ultrametric ball definitions per [11] — would change the count by many orders of magnitude. The thermodynamic analysis adopts the Landauer form as an assumption imported from the erasure-cost premise of [7]; we did not derive it, and any challenge to that premise propagates directly to R3. The cycling-cost projection assumes linear scaling and constant $T_{\mathrm{env}}$; real agents have hierarchical memory with vastly different cycling rates per level.

**Failure modes.** Three are structural. (i) *False-premise capture*: a system whose output grammar presupposes existence — as observed for LMMs under false-premise queries, where segmentation fine-tuning degraded presence-detection [5] — will affirm nonexistent entities; our framework flags this as a re-entry violation (the presupposed entity has no admissible extension), but does not yet provide a detection procedure. (ii) *Definitional drift*: without an admissibility criterion, terms persist while their extensions drift, as the half-century-long absence of a cross-domain definition of decentralization illustrates [6]. (iii) *Unpayable commitment*: commitments whose maintenance erasure cost exceeds the agent's power budget are physically inadmissible regardless of logical coherence (R3 projection).

**Against ourselves.** The strongest objection is that re-entry may be too weak: lossless rewriting, in the database setting [1], is a special-case luxury, and most interesting ontologies may simply fail re-entry, leaving the framework with a criterion that classifies almost everything as inadmissible. A second objection is that the relational ontology of [4] suggests base distinctions are themselves derived from relations, which would invert our direction of analysis: if relations are primitive, the coordinates of $D_{N}$ are not the base but an encoding. We can represent this (relational bases are still finite), but our counting results do not distinguish monadic from relational bases. Third, the Primitive Ontology demand for ontological clarity [3] may be satisfiable without finitary pricing; our thermodynamic admissibility criterion is a strengthening, not a consequence, and a reader may reject the strengthening while accepting the clarity demand. Fourth, the engineering evidence of [8] shows ontologies operating successfully in deployed systems, suggesting that in practice re-entry failures are tolerated and patched rather than fatal; our framework currently has no account of *partial* re-entry. Finally, the legal-domain LLM work [2] hints that institutional existence claims (legal entities) may follow different admissibility rules than perceptual ones; the supplied summary reports no results, so this remains an open question we cannot settle here.

**What would falsify the claims.** R1 and R4 are mathematical consequences of the definitions and can only be falsified by rejecting the definitions (e.g., by admitting non-finitary existence predicates). R3 is falsifiable empirically: an erasure event demonstrably costing less than $k_{B}T_{\mathrm{env}}\ln 2$ at the stated conditions would break the admissibility criterion. The claim that re-entry must route through hierarchical structure (R2) is falsified by exhibiting a natural predicate class whose flat enumeration covers a non-negligible fraction of the admissible space.

**Open questions.** Does lossless re-entry admit an algorithmic characterization analogous to the rewriting and optimization split of [1]? What is the correct formula class for ultrametric-structured predicates, and what is the resulting reachability count? How do the post-particle constructive paradigms of [12] constrain $V_{\mathrm{base}}$? And do the broader frameworks of [9][10] — whose supplied summaries contain no detail beyond their titles — impose additional structure on the distinction budget?

## 7. Conclusion

We have framed the question "what can we say exists?" as a problem of finite distinction budgets, thermodynamic pricing, and lossless rewriting. A system with $N$ binary distinctions supports exactly $2^{2^{N}}$ admissible existence predicates but can reach only a syntactically negligible fraction of them with flat formulas; holding or forgetting distinctions carries a computable energy floor, $2.8709 \times 10^{-21}\,\mathrm{J}$ per bit at $300\,\mathrm{K}$; and a high-level existence claim re-enters its own base losslessly only when its precision demand fits the budget. The framework unifies database-style ontological rewriting [1], the ontological-clarity demands of foundational physics [3][4], documented failure modes in learned systems [5][6], and the thermodynamics of forgetting [7], within the finite-distinction program [11][12]. Its principal virtue is that it makes ontological commitment countable and priced; its principal risk is that the re-entry condition may be too strict for the ontologies that matter most.

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