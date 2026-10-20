# Ontological Re-Entry: What Can We Say Exists?

## Abstract

This paper addresses the re-entry problem in ontology: given a theory built over a primitive vocabulary, what can we legitimately say exists when we project that structure back onto the world, and what does answering the question cost a physically bounded observer? Existing treatments state the demand for ontological clarity as a norm but supply no quantitative criterion that a resource-bounded observer could apply. We develop a finite-distinction framework in which existence claims are admissible only when expressible as distinctions at finite resolution. A system of $N$ binary distinctions supports $2^{N}$ states and exactly $2^{2^{N}}$ extensionally distinct existence predicates, of which only a vanishing fraction is reachable by short formulas: at $N = 64$, roughly $1.53 \times 10^{12}$ short conjunctions against $\approx 10^{5.553 \times 10^{18}}$ predicates. Erasing one distinction at $T = 300\ \mathrm{K}$ costs at least $2.87 \times 10^{-21}\ \mathrm{J}$, converting power budgets into distinction budgets; a nanowatt observer with $1\ \mathrm{s}$ coherence sustains at most $3.48 \times 10^{8}$ bit-distinctions per second. We define re-entry as the rewriting of a theory's high-level existence claims into predicates over its own base distinctions, modeled on ontological query compilation, and derive its failure modes: false-premise capture, resolution collapse, and unpayable erasure cost. Worked examples for budgets from $2^{40}$ to $2^{64}$ states show that under aggressive ultrametric compression the surviving ontology is structure, not individuals. The framework turns ontological clarity into an auditable budget calculation.

## 1. Introduction

Every deployed model of the world — a physics theory, a legal knowledge base, a robot's component ontology, a vision-language system — must eventually answer the question: what, according to this structure, exists? The people who face this question concretely are the engineers and scientists who must make their systems' commitments auditable. A database architect compiling an ontology-backed query must know which entities the answer actually ranges over [1]. A builder of legal-language systems whose model drafts regulation must know which obligations the output commits institutions to enforce [4]. A robotics engineer combining several hardware classification systems must know which components exist under which vocabulary [1], [8]. A perception-system developer whose segmentation model confidently masks objects that are not in the image has shipped a system that asserts existence the world does not support [7]. Today these questions are answered case by case, by intuition, and the failures — false-premise segmentation, definitional drift, ontologically obscure theories — are documented across fields [7], [8], [5]. What is missing is a criterion: a procedure that, given a theory and an observer with finite resources, outputs the set of existence claims the observer is entitled to make, together with the cost of making them. If such a criterion holds, an engineer could compute, before deployment, which of a system's ontological commitments survive its resource budget, and a physicist could state exactly which entities a theory's re-entry map licenses at a given resolution.

This paper proposes such a criterion. Its core commitment, taken from the finite-distinction program [11], [12], is that a finite-entropy world is a finite-distinction world: uncountable precision is unphysical, while computable depth and $p$-adic valuation remain physically real [9], [10]. If the world presents only finitely many distinctions to any finite observer, then the raw material of ontology is not substance but *difference*, and the state-space geometry of differences is combinatorial and ultrametric rather than Euclidean [11].

Three consequences follow. First, existence is graded: an object exists *at distinction depth $d$* for an observer with budget $N$ if it is invariant under the compression that the budget forces. Second, re-entry is a thermodynamic act with a price: maintaining and erasing distinctions costs energy, connecting ontology to the physics of computation [10]. Third, the classical ontological disputes — particle versus field, substance versus relation, primitive versus structural — can be re-read as disputes about where in the distinction hierarchy re-entry is performed. The relational ontology of contemporary physics [6] and the primitive-ontology programs surveyed in [5] then appear not as rivals but as different re-entry conventions, and the framework supplies the vocabulary in which that choice is made explicit.

The framing generates three questions that structure the paper. The *representational* question: what is the geometry of a space built only from finite distinctions, and how many distinct existence claims can it support? The *physical* question: what does it cost, in thermodynamic terms, to hold or erase a distinction, and when does an ontological commitment become physically unpayable? The *logical* question: when can an ontology's high-level existence claims be rewritten into statements over its own base distinctions without loss — the re-entry condition — and when does rewriting fail?

These questions are not asked in a vacuum. Database research has a mature theory of evaluating and optimizing queries answered against an ontology rather than directly against data [1]. Machine-learning evaluation has recently isolated a failure that is structurally a re-entry failure: a trajectory scorer can rank plausible futures almost perfectly while remaining blind to which dynamical rule is in force, a failure the authors of [2] call operator-blindness and prove invisible to generic top-1 ranking. Conformal prediction supplies calibrated thresholds per class, but a class with no calibration examples receives either no threshold or a shared marginal one [3] — an existence claim with no evidential support at the observer's resolution. On the physical side, the Primitive Ontology program insists that ontological clarity is a necessary condition on any theoretical framework [5], while a relational reading finds support across classical mechanics, gauge theories, general relativity, quantum field theory, and tentative quantum gravity [6]. On the computational side, erasing information carries an intrinsic energy cost, and the Autaxys Ontological Closure criterion makes the thermodynamic cost of measurement explicit through the modulus of convergence [10]. Multimodal models that fail under false premises [7] and the definitional stagnation of decentralization [8] supply engineering and conceptual instances of ontological commitment in deployed systems.

The contributions are:

- A formal definition of a finite distinction space and of admissible existence predicates over it, with the exact counting bound $2^{2^{N}}$ and an explicit computation of the syntactic bottleneck at $N = 64$ (defined in Section 3, computed in Section 4).
- A thermodynamic admissibility criterion derived from the erasure cost of distinctions, giving the numerical floor $2.87 \times 10^{-21}\ \mathrm{J}$ per bit at $300\ \mathrm{K}$ and the budget conversion $N_{\max} = P_{\mathrm{obs}}\tau / (k_{B}T\ln 2)$ (Section 3.3, computed in Section 4).
- A definition of ontological re-entry modeled on query rewriting against an ontology [1], with a necessary condition for re-entry to be lossless and a quantitative survival analysis under ultrametric compression showing that at compression level $r = 30$ of a depth-$40$ binary tree, $10^{5}$ uniformly spread objects leave an expected $3.78 \times 10^{-36}$ resolvable individuals (Sections 3.4 and 4).
- An analysis of failure modes — false-premise capture in the sense observed for multimodal models [7], resolution collapse, and unpayable erasure cost — with the falsification conditions stated in Section 6.

## 2. Background and Related Work

**Ontological queries and rewriting.** The database literature has formalized a precise version of re-entry. [1] studies ontological query processing: a query against an ontology on top of a relational database is compiled into a direct query against that database, together with optimization so as to obtain possibly small and efficient compiled queries. The same work notes that ontological reasoning and query answering in the most well-known decidable fragments of OWL is typically $2\texttt{EXPTIME}$-complete, and reports an implementation, the prototype system Nyaya built on the IRIS Datalog engine extended to support existential head variables and negative constraints, tested on DL-Lite$_R$ ontologies. This is a re-entry map in miniature: the ontology is the theory, the database is the world-as-modeled, and the rewriting is the rule for projecting existence claims down to what the substrate can answer. We borrow the rewriting/optimization split — first rewrite, then optimize — as the template for Section 3.4, noting where the analogy is exact and where it breaks: ontologies of existence have no underlying database other than the distinction space itself.

**Operator-blindness as mis-targeted re-entry.** [2] formalizes a failure of world models that is structurally an existence failure at the wrong level. The work defines operator-blindness and proves that generic top-1 ranking cannot detect it whenever the candidate set excludes wrong-operator futures; its objective, Operator-Mismatch Contrastive learning, uses wrong-operator hard negatives and, on synthetic IID/OOD operator parameters, two backbones, and feature-level CoPhy, lifts operator-sensitive metrics well above a baseline that retains $\approx 0.99$ generic top-1. Its conclusion states the principle directly: plausibility is not coherence. In re-entry terms, a scorer that answers "is this future plausible?" has committed to existence at the level of trajectories, while the physically load-bearing commitment is at the level of operators — which world is in force. The lesson for Section 3.4 is that a re-entry map must be indexed by the operator (the rule structure), not only by the state space, or it licenses commitments at the wrong depth.

**Existence claims without calibration data.** [3] studies class-conditional conformal prediction, which calibrates a separate score threshold for every class and therefore requires labelled calibration examples of every class; in long-tailed deployments rare classes are left with few or no held-out examples, and existing methods are either undefined for them or fall back to the shared marginal threshold. The reported mechanism is concrete: for an ImageNet class held out entirely, a descriptor-based correction moves the threshold from $\hat{q} = 0.9657$ to $0.9812$ and coverage of the class from $0.658$ to $0.750$, against $0.803$ for an oracle given the test labels; across $412$ configurations, PCC improves worst-class coverage on zero-calibration classes by $0.058$ $[0.006, 0.110]$ at matched average set size and is the only one of nine methods whose interval excludes zero. This is a graded, calibrated substitute for an existence predicate: a class with no calibration data is a predicate whose extension the observer cannot yet resolve, and the conformal threshold is the resolution at which the claim "this class is instantiated here" becomes admissible. Section 3.2's admissibility condition is the discrete, budget-indexed analogue of this threshold.

**Language-model ontologies in institutions.** [4] fine-tunes Large Language Models with a curated supervised legal dataset and integrates Retrieval-Augmented Generation to support policymakers in understanding, analyzing, and crafting legal regulations. Its relevance here is structural: a legal regulation is an ontology enforced by re-entry onto human conduct, and RAG is a retrieval-bounded re-entry mechanism whose false-premise costs are institutional rather than perceptual. We cite it for the architectural pattern — commitment mediated by a bounded retrieval channel — and draw no performance findings from it.

**Primitive ontology and realism.** In foundations of physics, [5] traces how Bohm's and Bell's approaches share notable features with the contemporary Primitive Ontology perspective and with Esfeld's and Deckert's minimalist ontology: all these programs consider ontological clarity a necessary condition to be met by every theoretical framework, promote scientific realism also in the quantum domain, and strengthen explanatory power. The same work records Bohm's complaint that quantum theory excludes a precise characterization of individual systems without proving that such a renunciation is necessary, and Bell's diagnosis that the lack of ontological clarity in QM was the source of its inconsistency — the dynamical laws, the Schrödinger equation and the collapse postulate, contradict each other — and of its redundancy. The stated position, ontological clarity as a necessary condition on theories, is precisely the normative stance this paper operationalizes. Where [5] demands clarity, we supply a quantitative criterion for it.

**Relational ontology.** Against substance-first readings, [6] argues that quantum theory can be understood as pointing to an ontology of relations, supported by the ubiquity of relationality in contemporary fundamental physics, including classical mechanics, gauge theories, general relativity, quantum field theory, and tentative theories of quantum gravity. Its central move is to take discreteness and indetermination at face value rather than bending them into an underlying continuous and determined reality; in the relational interpretation, when a self-adjoint operator assumes an eigenvalue, this corresponds to an element of reality — a fact or event — and subjectivity plays no role. The work concludes that even the particles of quantum field theory, which an ontology of objects would call fundamental, are relative, not absolute, entities. A distinction-based ontology is naturally relational: a distinction is a difference, and differences are relations. Our framework can thus be read as a resource-bounded refinement of the relational thesis of [6], though Section 6 notes an objection that would invert our direction of analysis.

**False premises as re-entry failures.** In machine perception, [7] reports that open-source Large Multimodal Models excel at open-vocabulary grounding and segmentation but suffer under false premises when queries imply the existence of something not actually present in the image, and that fine-tuning an LMM to segment images significantly degrades its ability to reliably determine whether an object is present. Its remedy is architectural: the SESAME system uses model chaining and joint training, a purpose-built false-premise referring segmentation dataset FP-RefCOCO(+/g) built from refCOCO with LLM-generated paired corrections, and demonstrates robustness to false premises together with the ability to suggest relevant objects when a similar instance is present. This is an empirical instance of re-entry failure: the model's internal structure licenses an existence claim the world does not support, and the observed trade-off — segmentation ability bought at the price of presence-detection — is a resource trade-off of exactly the kind our budget formalism predicts.

**Definitional stagnation.** [8] documents the Decentralization Problem: despite over half a century of use across security, distributed computing, artificial intelligence, cloud infrastructures, and IoT architectures, there is no universally accepted definition of decentralization applicable across computer communication systems. The work shows that what repeatedly becomes rigorous in the literature is an associated property — connectivity, fault tolerance, consistency, intermediary removal, resource dispersion, or control — while decentralization itself remains largely descriptive, context-bound, or inferred from those proxies. Its remedy is a formal graph-based ontology separating three questions: how many realization particulars exist ($\delta$), across how many vertices they are placed ($\lambda$), and how many center regions they reach under an anchor such as ownership or authority ($\mu$), thereby demonstrating that structurally identical topologies may exhibit different decentralization properties depending on the subject. We take this as a cautionary case study with a constructive counterpart: a concept in wide cross-domain use without an explicit re-entry criterion accumulates incompatible ontological commitments, and the repair is exactly the kind of parameterized ontology [8] builds. The same risk attaches to "existence" itself, which is our target concept.

**Finite specification and ontological indeterminism.** [9] examines the Gisin–Del Santo program on finite-precision physics, whose three claims are that physical quantities contain only finite information, that real numbers are physically unreal — de facto hidden variables of classical mechanics — and that consequently classical mechanics is ontologically indeterminate. The work also reports its own strongest red-team finding, R5: neither the Gisin–Del Santo program nor the Ontological Closure framework has produced a differential empirical prediction, something observed if the framework is correct but not if standard physics is correct, and positions the program as foundations of physics whose value is theoretical unification and consilience. This caveat transfers directly: our framework inherits the same exposure, and Section 6 states the observations that would falsify it rather than claiming differential empirical content.

**Operational closure and the cost of measurement.** [10] proposes an operational criterion for physical reality: a quantity is physically real only if there exists a finite Turing-machine protocol that approximates it with a computable modulus of convergence, yielding measurement-distinguishable predictions; if no finite protocol can converge to a quantity's value, it is operationally indistinguishable from a quantity that does not exist. The same work records Landauer's principle — erasing a bit costs $k_{B}T\ln 2$ — as the historical anchor for information being physical, and translates the modulus-of-convergence requirement into resource estimates: if measuring a quantity $Q$ to precision $\varepsilon$ requires $\mu(-\log_2 \varepsilon)$ steps and each step costs $E$ joules, the total energy cost is $E \cdot \mu(n)$. Section 3.3 adopts exactly this bridge, in the erasure direction, as the thermodynamic admissibility criterion.

**The finite-distinction program.** [11], the companion statement of this paper's program, develops the finite-distinction framework: existence claims are admissible only when expressible as distinctions at finite resolution, the state-space geometry of finite distinctions is combinatorial and ultrametric, and quantum mechanics is read as a stochastic theory whose unitary evolution and superposition emerge in the large-distinction limit. [12] supplies the umbrella ontology: the universe is constructed not from matter or energy but from pure information, physical objects are emergent properties of underlying data structures, energy is an abstraction quantifying the magnitude of change rather than a fundamental constituent, and the Many-Worlds Interpretation is criticized as requiring an extravagant ontological leap that misunderstands the true structure of existence. Our re-entry criterion is the tool the constructive task of [12] requires: it says exactly which commitments survive a given observer budget.

## 3. Methods

### 3.1 Distinction spaces

**Definition 3.1 (Distinction space).** A *distinction space* is a pair $D_{N} = (S_{N}, d_{u})$ where $S_{N} = \{0,1\}^{N}$ is the set of $N$-bit distinction records and $d_{u}: S_{N} \times S_{N} \to \mathbb{Q}_{\geq 0}$ is an ultrametric, i.e., $d_{u}(x_{i}, x_{j}) \leq \max\{ d_{u}(x_{i}, x_{k}), d_{u}(x_{k}, x_{j}) \}$ for all $x_{i}, x_{j}, x_{k} \in S_{N}$. A *distinction* $d_i$ is a binary partition of the observer's state space; maintaining it means the observer can reliably re-identify which side of the partition the world is on. The ultrametric requirement implements the finite-distinction geometry of [11]: balls in $D_{N}$ are hierarchically nested, mirroring the combinatorial, $p$-adic structure in which depth of distinction, not metric distance, carries the physical content. We realize the geometry by a $b$-ary tree of depth $L$ with branching factor $b$, so that

$$
N = L \log_2 b, \qquad |S_{N}| = b^{L} = 2^{N}.
$$

### 3.2 Admissible existence predicates and the counting bound

**Definition 3.2 (Admissible existence predicate).** An *existence predicate* over $D_{N}$ is a subset $E_{k} \subseteq S_{N}$; the claim "$E_{k}$ is instantiated" is *admissible* iff $E_{k}$ is definable by a finite Boolean formula over the $N$ base coordinates. Two predicates are *extensionally equivalent* iff $E_{i} = E_{j}$ as sets.

**Proposition 3.1.** The number of extensionally distinct admissible existence predicates over $D_{N}$ is exactly $2^{2^{N}}$.

*Proof.* Each Boolean formula over $N$ coordinates defines a subset of $S_{N}$, and every subset of $S_{N}$ is defined by its characteristic formula (a disjunction over its members). Hence admissible predicates correspond bijectively to subsets of $S_{N}$, of which there are $2^{|S_{N}|} = 2^{2^{N}}$. $\square$

The bound is tight but syntactically unreachable: the number of *short* formulas is far smaller, and Section 4.1 quantifies the gap for a concrete budget. The gap matters because an observer does not command all $2^{2^{N}}$ predicates; it commands the ones its syntax and training reach, and re-entry failures occur precisely when a deployed predicate is outside the reachable set but treated as if inside it — the situation [2] isolates when a scorer with $\approx 0.99$ generic top-1 remains blind to the operator in force.

### 3.3 Thermodynamic admissibility

Following the resource bridge made explicit in [10], a step that erases information has an intrinsic energy cost. We adopt the standard Landauer form as a modeling assumption (not derived here): erasing one bit at temperature $T_{\mathrm{env}}$ costs at least

$$
E_{\mathrm{bit}} = k_{B} T_{\mathrm{env}} \ln 2,
$$

where $k_{B}$ is Boltzmann's constant. A commitment is *thermodynamically admissible* for an agent with erasure budget $E_{\mathrm{budget}}$ if the distinctions it requires can be maintained without erasure exceeding budget. If the agent must cycle its memory at rate $f_{\mathrm{cycle}}$, the erasure power is

$$
P_{\mathrm{erase}} = f_{\mathrm{cycle}} \, N_{\mathrm{dist}} \, k_{B} T_{\mathrm{env}} \ln 2,
$$

with $N_{\mathrm{dist}}$ the number of distinctions cycled per cycle. Symmetrically, maintaining $N$ distinctions against noise over a coherence time $\tau$ requires refreshing them, so an observer's power budget $P_{\mathrm{obs}}$ bounds

$$
N \le \frac{P_{\mathrm{obs}} \, \tau}{k_{B} T_{\mathrm{env}} \ln 2}.
$$

This inequality is the bridge between physics and ontology: it converts a power budget into a distinction budget, and hence into an existence criterion. It is the erasure-side dual of the measurement-side estimate of [10], in which measuring to precision $\varepsilon$ costs $E \cdot \mu(-\log_2 \varepsilon)$; both directions make the same point, that ontological and operational commitments are energy accounting. Reversibility removes the erasure cost but forces the agent to retain all distinctions — trading power for unbounded memory growth.

### 3.4 Ontological re-entry

**Definition 3.3 (Re-entry).** Let $\mathcal{O}$ be an ontology whose commitments are expressed in a high-level vocabulary $V_{\mathrm{high}}$, and let $V_{\mathrm{base}}$ be the base coordinates of $D_{N}$. *Re-entry* is a map $r: V_{\mathrm{high}} \to \mathcal{P}(S_{N})$ assigning each high-level predicate an admissible existence predicate. Re-entry is *lossless* iff for every pair of commitments $c_{i}, c_{j} \in \mathcal{O}$, all entailments among them are preserved under $r$.

This mirrors the compilation of an ontological query into an equivalent query against the underlying data [1], with $D_{N}$ playing the role of the underlying data. The re-entry condition fails when $V_{\mathrm{high}}$ contains predicates whose extension depends on precision beyond the $N$-bit budget — the "uncountable precision is unphysical" clause of the finite-specification program [9], [11]. Three failure modes are analyzed in Section 4:

1. *False-premise capture*: $r(c_{i})$ is defined but has empty or near-empty extension, while the deploying system treats $c_{i}$ as instantiated — the pattern [7] documents for multimodal segmentation and [3] documents as a class with no calibration data receiving a threshold it did not earn.
2. *Resolution collapse*: $r(c_{i})$ cannot be defined at all at budget $N$ because $c_{i}$'s extension separates states that agree on all $N$ coordinates.
3. *Unpayable erasure cost*: $r(c_{i})$ is definable but the distinctions it requires exceed the observer's thermodynamic budget of Section 3.3.

## 4. Analysis

Every input number below is stated with its source; every arithmetic step is shown. No empirical data are used. Two illustrative budgets appear: $N = 64$ (one machine word) for the counting analysis and $N = 40$ ($b = 2$, $L = 40$) for the ultrametric tree scenario; both are modeling choices of this paper.

### 4.1 Counting admissible existence predicates

**Inputs.** $N = 64$ binary distinctions (modeling choice). Formula: Proposition 3.1.

**Step 1.** $|S_{N}| = 2^{N} = 2^{64} = 18{,}446{,}744{,}073{,}709{,}551{,}616 \approx 1.8447 \times 10^{19}$ states.

**Step 2.** Number of admissible predicates: $2^{2^{N}} = 2^{2^{64}}$. In base-10 logarithms:

$$
\log_{10}\left(2^{2^{64}}\right) = 2^{64} \log_{10} 2 \approx 1.8447 \times 10^{19} \times 0.30103 \approx 5.553 \times 10^{18}.
$$

So there are $\approx 10^{5.553 \times 10^{18}}$ extensionally distinct existence predicates — combinatorially vast but finite.

**Step 3 (syntactic reachability).** Assume formulas are conjunctions of at most $k_{\mathrm{lit}} = 8$ literals chosen from $2N = 128$ literals (modeling choice). The dominant term is $\binom{128}{8} = \frac{128 \times 127 \times 126 \times 125 \times 124 \times 123 \times 122 \times 121}{40320}$. Numerator, stepwise: $128 \times 127 = 16{,}256$; $\times\,126 = 2{,}048{,}256$; $\times\,125 = 256{,}032{,}000$; $\times\,124 = 31{,}747{,}968{,}000$; $\times\,123 = 3{,}905{,}000{,}064{,}000$; $\times\,122 = 476{,}410{,}007{,}808{,}000$; $\times\,121 = 57{,}645{,}610{,}944{,}768{,}000$. Dividing: $57{,}645{,}610{,}944{,}768{,}000 / 40{,}320 \approx 1.4298 \times 10^{12}$. The remaining terms $\sum_{j=0}^{7}\binom{128}{j}$ are smaller by factors of at least $121/8 \approx 15$ each, so the total is $\approx 1.43 \times 10^{12} \times (1 + 1/15 + \cdots) \approx 1.53 \times 10^{12}$ short conjunctions.

**Conclusion 4.1.** With $N = 64$, the fraction of admissible predicates reachable by short formulas is $\approx 1.53 \times 10^{12} / 10^{5.553 \times 10^{18}}$, i.e., effectively zero relative to the full space. Ontological expressiveness is therefore bottlenecked by *syntax*, not by the state space: re-entry must route through structured (hierarchical, ultrametric) definitions, consistent with the nested-ball geometry of [11].

### 4.2 Erasure cost of a distinction

**Inputs.** $k_{B} = 1.380649 \times 10^{-23}\ \mathrm{J\,K^{-1}}$ (SI defined value); $T_{\mathrm{env}} = 300\ \mathrm{K}$ (room-temperature modeling choice); $\ln 2 = 0.693147$ (mathematical constant). Formula: $E_{\mathrm{bit}} = k_{B} T_{\mathrm{env}} \ln 2$, the Landauer cost as recorded in [10].

**Step 1.** $k_{B} T_{\mathrm{env}} = 1.380649 \times 10^{-23} \times 300 = 4.141947 \times 10^{-21}\ \mathrm{J}$.

**Step 2.** $E_{\mathrm{bit}} = 4.141947 \times 10^{-21} \times 0.693147 = 2.8709 \times 10^{-21}\ \mathrm{J}$.

**Step 3 (cycling cost).** Assume an agent maintains $N_{\mathrm{dist}} = 10^{9}$ distinctions and rewrites (erases-and-replaces) each once per second, $f_{\mathrm{cycle}} = 1\ \mathrm{s^{-1}}$ (modeling choices). Then

$$
P_{\mathrm{erase}} = 1 \times 10^{9} \times 2.8709 \times 10^{-21} = 2.8709 \times 10^{-12}\ \mathrm{W}.
$$

**Step 4 (scaling projection).** Under the stated linear-scaling assumption and constant $T_{\mathrm{env}}$, an agent cycling $10^{20}$ distinctions at $10^{9}\ \mathrm{s^{-1}}$ would require $P_{\mathrm{erase}} = 10^{20} \times 10^{9} \times 2.8709 \times 10^{-21} = 2.87 \times 10^{8}\ \mathrm{W}$, which is physically prohibitive. This is a labeled projection, not a measurement.

**Conclusion 4.2.** At $10^{9}$ distinctions cycled at $1\ \mathrm{s^{-1}}$, the minimal erasure power is $\approx 2.87 \times 10^{-12}\ \mathrm{W}$ — negligible for silicon-scale hardware but a hard floor scaling linearly in both $N_{\mathrm{dist}}$ and $f_{\mathrm{cycle}}$. Thermodynamic admissibility bites at the large-distinction limit that [11] identifies with quantum-mechanical behavior.

### 4.3 Distinction budget from a power budget

**Inputs.** Power $P_{\mathrm{obs}} = 10^{-12}\ \mathrm{W}$ (illustrative nanowatt-scale bound, modeling choice), coherence time $\tau = 1\ \mathrm{s}$, $T = 300\ \mathrm{K}$. From Step 2 of Section 4.2, $k_{B} T \ln 2 = 2.8709 \times 10^{-21}\ \mathrm{J/bit}$.

$$
N_{\max} = \frac{P_{\mathrm{obs}} \tau}{k_{B} T \ln 2} = \frac{10^{-12}}{2.8709 \times 10^{-21}} = 3.4832 \times 10^{8}.
$$

So a nanowatt observer with $1\ \mathrm{s}$ coherence can in principle sustain at most $N_{\max} \approx 3.48 \times 10^{8}$ bit-distinctions per second against the erasure floor. This is an upper bound on *refresh rate*, not on stored distinctions; we use it as the budget ceiling in the re-entry criterion, noting that real devices operate far above the Landauer bound, so the true budget is smaller by an unquantified efficiency factor.

### 4.4 Ultrametric ball counting and compression

**Inputs.** $b = 2$, $L = 40$ (modeling choices; any $b, L$ work). Then $N = L \log_2 b = 40 \times 1 = 40$ and

$$
|S_{N}| = 2^{40} = 1{,}099{,}511{,}627{,}776 \approx 1.10 \times 10^{12}.
$$

The entropy of a uniform distribution over $S_{N}$ is $H = N$ bits, so the thermodynamic entropy is

$$
S = N k_{B} \ln 2 = 40 \times 1.380649 \times 10^{-23} \times 0.693147.
$$

Step 1: $1.380649 \times 10^{-23} \times 0.693147 = 9.56963 \times 10^{-24}\ \mathrm{J/K}$ (since $1.380649 \times 0.693147 = 0.956963$). Step 2: $S = 40 \times 9.56963 \times 10^{-24} = 3.82785 \times 10^{-22}\ \mathrm{J/K}$. The full erasure cost at $T = 300\ \mathrm{K}$ is

$$
E_{\mathrm{erase}} = S \cdot T = 3.82785 \times 10^{-22} \times 300 = 1.14836 \times 10^{-19}\ \mathrm{J}.
$$

In a $b$-ary ultrametric tree of