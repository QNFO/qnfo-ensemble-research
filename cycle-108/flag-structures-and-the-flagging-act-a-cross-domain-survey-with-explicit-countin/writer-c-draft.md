# Flagging as an Epistemic Operator: Flag Structures Across Mathematics and the Open Question of Re-Entry 10.5281/zenodo.23159238

## Abstract

The word "flag" names a family of mathematically precise objects — chains of nested subspaces (flag varieties), nested-set systems with exchange axioms (flag matroids), asymptotic inequality certificates (flag algebras), and curvature invariants of Finsler spaces — and, in ordinary research practice, a marker attached to an unresolved issue. This paper treats "flagging" as a single epistemic operator that both carries mathematical content and performs the act of marking a claim's status. We survey eight strands of flag mathematics from the supplied literature, from representability of flag matroids over $\mathbb{F}_2$ and $\mathbb{F}_3$ to machine-checked flag algebra proofs in Lean, and connect them to the QNFO critique programme, which questions the qubit-gate ontology of quantum computation and audits claimed quantum advantage results. We then formalize the act of flagging a research output as a three-valued status assignment (result / open question / flagged-for-remediation) and derive concrete combinatorial quantities: the number of complete flags in $\mathbb{F}_2^3$ is $21$, in $\mathbb{F}_2^4$ is $315$, and the number of labeled graph types on $k=4$ vertices available to a flag-algebra certificate is at most $2^{\binom{4}{2}} = 64$. The specific re-entry associated with DOI 10.5281/zenodo.23159238 is flagged here as an open question rather than a result, and we state explicitly what evidence would promote or demote that flag.

## 1. Introduction

Research communities need two things from the word "flag". First, they need flag *objects*: in algebraic geometry, a complete flag in an $n$-dimensional vector space is a chain of subspaces $V_1 \subset V_2 \subset \cdots \subset V_{n-1} \subset V_n$ with $\dim_{\mathbb{}}V_k = k$; flag varieties parametrize such chains and support Schubert calculus, standard monomial theory, and total-positivity structures. Second, they need flag *acts*: the deliberate marking of a claim, a proof, or a dataset with a status label — verified, contested, or open. The present paper argues that these two senses are not merely homonymous. In both cases, a flag is a nested structure imposed on an underlying space that records which regions of that space are accessible, and in both cases the flag's value lies in making the boundary between the accessible and the inaccessible explicit.

Our motivating instance of the second sense is narrow and specific. The grounding material for this paper states, verbatim: "Re-entry from 10.5281/zenodo.23159238: We flag this as an open question rather than a result." That sentence performs a flagging act on a document we do not otherwise have access to. We therefore cannot and do not report any content of that document. What we can do — and what this paper does — is (i) build a precise framework in which such a flagging act is a well-defined operation with a well-defined state space, (ii) survey the flag-structured mathematics that supplies the vocabulary, and (iii) derive the combinatorial quantities that determine how much information a flagging scheme of a given granularity can carry.

The paper is organized as follows. Section 2 reviews the supplied literature: six works on flag structures in pure mathematics, one on generally capable learning agents, one on guaranteed posterior inference, and four QNFO programme documents that critique the quantum-computing mainstream. Section 3 defines the flagging operator $\Phi_{\mathcal{S}}$ on a corpus $\mathcal{S}$ and its state space. Section 4 carries out the explicit derivations, including counts of complete flags over $\mathbb{F}_2$ and type counts relevant to flag-algebra certificates. Section 5 reports only those computed values. Section 6 discusses limitations and failure modes, including the central honesty constraint of this paper: the re-entry document itself is unavailable, so every statement about it is a statement about its flag status, not its content.

## 2. Background and Related Work

We discuss all twelve supplied works, in bibliography order. For each, we state only what its supplied entry supports.

**[1] Representability of Flag Matroids (arXiv:2504.00267v2).** This work provides a new axiom system for flag matroids, characterizes representability of uniform flag matroids, and gives forbidden-minor characterizations of full flag matroids representable over $\mathbb{F}_2$ and $\mathbb{F}_3$, along with regular full flag matroids and equivalent characterizations of regularity. For our framework, this is the purest example of flagging as a *classifiability* question: the entry's forbidden-minor characterizations are exactly a finite set of obstructions that flag the boundary between representable and non-representable flag matroids over a fixed field. A flagging scheme, we argue in Section 3, plays the same role for epistemic status: a finite set of marked counterexamples delimiting which claims fall in which status class.

**[2] Even dimensional homogeneous Finsler spaces with positive flag curvature (arXiv:1407.3582v2).** This paper uses Finslerian submersion to deduce a flag curvature formula for homogeneous Finsler spaces and, based on that formula, gives a complete classification of even-dimensional smooth coset spaces $G/H$ admitting $G$-invariant Finsler metrics with positive flag curvature, noting that the classification list coincides with that of the even-dimensional homogeneous Riemannian case (the entry's text is cut off at this point). Flag curvature here is a directional invariant: curvature assigned to a flagged 2-plane direction. This supplies our second mathematical metaphor — a flag as a *directional probe* whose value varies over the space of directions, exactly as an epistemic flag's value varies over the space of claims.

**[3] Formalizing Flag Algebras in Lean (arXiv:2607.23500v1).** Razborov's flag algebra method is described in the entry as a powerful tool for proving asymptotic inequalities in extremal graph theory, often reducing the task to finding a finite certificate by semidefinite programming. The work presents a machine-checked formalization of the method for finite simple graphs, together with a certificate-to-proof compiler that turns externally generated certificate data into algebraic proofs that are checked (the entry's text is truncated mid-sentence). This is the closest existing analogue to our flagging operator as a *verification gate*: an externally produced certificate is admitted into a trusted proof system only after mechanical checking. Our Section 3 borrows this certificate-gate structure for status assignment.

**[4] Total positivity in twisted product of flag varieties (arXiv:2211.11168v2).** The entry states that the totally nonnegative part of the twisted product of flag varieties of a Kac-Moody group admits a cellular decomposition, that the closure of each cell is a topological manifold with boundary, and that explicit parameterizations of each totally positive cell are established; for double flag varieties and braid varieties the totally nonnegative parts are regular (text truncated). The cell decomposition with manifold-with-boundary closures is our model for the *topology of status space*: epistemic statuses, like totally positive cells, should have closures whose boundaries are themselves meaningful — the boundary of the "result" cell is precisely where "open question" flags live.

**[5] Standard monomial theory and toric degenerations of Richardson varieties in flag varieties (arXiv:2103.16197v2).** This work studies standard monomial bases for Richardson varieties inside the flag variety. The entry notes that writing down such a basis in general is challenging, involving so-called defining chains or key tableaux, but that for a family of Richardson varieties indexed by compatible permutations, a very direct and straightforward combinatorial rule is provided (text truncated). We read this as a lesson about *explicitness*: a flag structure (here, a basis) is only useful when an explicit rule generates it — the same demand we place on a flagging scheme's decision procedure.

**[6] Bioriented flags and resolutions of Schubert varieties (arXiv:1810.05604v2).** The entry states that incidence relations running in two directions are used to construct a Kempf-Laksov type resolution for any Schubert variety of the complete flag manifold and an embedded resolution for any Schubert variety in the Grassmannian, as alternatives to Bott-Samelson resolutions, and that the second process led to the introduction of W-flag varieties. The bioriented structure — incidence relations running in two directions — motivates our treatment of a flag as a *directed edge* in a citation-and-status graph, pointing both from a claim to its evidence and from evidence back to the claim.

**[7] Open-Ended Learning Leads to Generally Capable Agents (arXiv:2107.12808v2).** This work creates agents that perform well beyond a single individual task, exhibiting wide generalisation of behaviour across a massive, rich space of challenges; the authors define a universe of tasks within an environment domain and demonstrate agents that are generally capable across this space and beyond, in a natively multi-agent environment (the entry's text is truncated). We use this entry only for its structural claim — that defining a *universe of tasks* and demonstrating capability across it is a coherent methodology — which parallels our definition of a universe of claims $\mathcal{S}$ over which a flagging operator must be uniformly defined rather than case-by-case.

**[8] Guaranteed inference in topic models (arXiv:1512.03308v2).** The entry identifies posterior estimation for individual texts, especially in data streams, as important but often worst-case intractable, so that existing methods are approximate and lack guarantees (the entry's text is truncated before stating which guarantees). This supplies the statistical face of our problem: status assignment under a stream of incoming documents is an inference problem, and the entry's framing — approximate inference without guarantees as the default state — is exactly the deficiency a flagging operator is meant to mitigate by making the *absence* of a guarantee itself an explicit flag.

**[9] QNFO: The Valuation Reading of the Qubit Delusion (DOI context: Qubit Delusion is 10.5281/zenodo.21254143).** The entry states that the Qubit Delusion argues that the qubit-gate-circuit model of quantum computation imports a particle ontology inconsistent with quantum field theory, and that the field's failure to deliver commercially viable hardware after $35$ billion of investment is an epistemic crisis (entry text truncated). The figure of $35$ billion is the only quantitative claim we take from this entry, and we use it in Section 4 only as a stated input, not as an independently verified fact. Within our framework, the Qubit Delusion is itself a large-scale flagging act: a document that flags an entire research programme's ontology as contested.

**[10] QNFO: Vanishing ZBW Signal (ZBW-Majorana hypothesis, P1–P4).** The entry states that the hypothesis, developed across four companion papers, establishes that Zitterbewegung (ZBW) — the rapid trembling motion of Dirac fermions at the Compton scale — is a $\mathbb{Z}_2$ topological observable that distinguishes Dirac from Majorana fermions at the hardware level (text truncated). The $\mathbb{Z}_2$ structure is notable for us: a two-valued topological invariant is the minimal nontrivial flagging scheme, and the entry's claim that this invariant operates "at the hardware level" makes it a proposed physical instantiation of a binary status bit.

**[11] QNFO: The Vast World of Quantum Advantage — A Full-Spectrum Audit.** The entry describes a full-spectrum audit of Huang, Choi, McClean and Preskill (2025), "The vast world of quantum advantage" (arXiv:2508.05720), subjecting both the Huang et al. five-keystone framework and QNFO's own prior critiques to symmetric scrutiny, with the key finding that Theorem 1 is the most sophisticated challenge to QNFO's extant position (text truncated). Methodologically this is the most important entry for us: symmetric scrutiny — applying the same audit standard to one's own prior flags as to the audited work — is precisely the reflexivity our flagging operator requires, and we adopt it as an axiom in Section 3.

**[12] QNFO: The Adelic ZBW Programme.** The entry states that the structural underdetermination of the position operator in relativistic quantum mechanics — manifested at the Archimedean place as zitterbewegung (the Newton-Wigner no-go) and at $p$-adic places as a discrete Bruhat-Tits observable — arises from a single representation-theoretic origin (the entry names "the Silen…" and is truncated). This supplies the final ingredient: a claim that one mechanism generates flag-like distinctions at multiple "places", which we mirror in the claim that one operator $\Phi_{\mathcal{S}}$ generates status distinctions across heterogeneous corpora.

## 3. Methods

### 3.1 The flagging operator

Let $\mathcal{S}$ be a corpus of research outputs (papers, theorems, datasets, DOIs). Define the *flagging operator*

$$\Phi_{\mathcal{S}} : \mathcal{S} \to \{R, Q, F\} \times \mathcal{D},$$

where the first component is a status in the three-element set $\{R, Q, F\}$ — $R$ = result, $Q$ = open question, $F$ = flagged for remediation — and $\mathcal{D}$ is a set of justifying documents. The operator is *certificate-gated* in the sense of [3]: a status change from $Q$ to $R$ requires a certificate that passes a mechanical or referee-level check; a status change from $R$ to $F$ requires a documented failure mode. This mirrors the entry-level structure of [3], in which externally generated certificate data is admitted only after being turned into checkable algebraic proofs.

### 3.2 Axioms

We adopt three axioms, motivated in Section 2.

**A1 (Uniformity, after [7]).** $\Phi_{\mathcal{S}}$ is defined on all of $\mathcal{S}$, not on a hand-picked subset; every element of the corpus carries exactly one status.

**A2 (Symmetric scrutiny, after [11]).** The same audit standard that demotes an external claim to $F$ applies to the flagging authority's own prior outputs.

**A3 (Two-directional incidence, after [6]).** Each flag carries pointers in two directions: from the flagged item to its justifying documents, and from those documents back to every item whose status they affect.

### 3.3 Status space topology

Following the cellular picture of [4], we impose on the status simplex $\{R, Q, F\}$ the convention that transitions are continuous paths through an underlying evidence parameter $e \in [0,1]$, with thresholds $e_{Q \to R}$ and $e_{R \to F}$ to be set by the community, not by this paper. We do not estimate these thresholds from data; we only note that the boundary of the $R$ cell is where $Q$ flags accumulate, in direct analogy with the manifold-with-boundary structure of totally positive cells in [4].

### 3.4 Instantiation to the grounding case

The grounding block supplies exactly one flagging act: the sentence "Re-entry from 10.5281/zenodo.23159238: We flag this as an open question rather than a result." Under $\Phi_{\mathcal{S}}$, this assigns status $Q$ to the item identified by DOI 10.5281/zenodo.23159238, with the grounding block itself as the justifying document $d \in \mathcal{D}$. Because the document's content is not supplied to us, no claim about its content enters this paper; the flag is about status, not substance. This is the honest core of the paper and we return to it in Section 6.

## 4. Analysis

All numbers in this section are derived here from stated inputs. No empirical measurement is reported anywhere in this paper.

### 4.1 Count of complete flags over $\mathbb{F}_2$

**Input 1 (definition).** A complete flag in an $n$-dimensional vector space over a finite field $\mathbb{F}_q$ is a chain $V_1 \subset \cdots \subset V_n$ with $\dim_{\mathbb{}}V_k = k$. The number of such flags is the product over $k = 1, \dots, n$ of the number of $k$-dimensional choices given a fixed $(k-1)$-dimensional subspace, i.e. the number of lines in the quotient $\mathbb{F}_q^n / V_{k-1} \cong \mathbb{F}_q^{n-k+1}$, which is $\frac{q^{\,n-k+1} - 1}{q - 1}$. Hence

$$N_{\text{flag}}(q, n) = \prod_{k=1}^{n} \frac{q^{\,n-k+1} - 1}{q - 1} = \prod_{j=1}^{n} \frac{q^{\,j} - 1}{q - 1}.$$

**Derivation for $q = 2$, $n = 3$** (the field $\mathbb{F}_2$ is chosen because [1] gives forbidden-minor characterizations over $\mathbb{F}_2$):

$$N_{\text{flag}}(2, 3) = \frac{2^1 - 1}{2 - 1} \cdot \frac{2^2 - 1}{2 - 1} \cdot \frac{2^3 - 1}{2 - 1} = 1 \cdot 3 \cdot 7 = 21.$$

**Derivation for $q = 2$, $n = 4$:**

$$N_{\text{flag}}(2, 4) = 1 \cdot 3 \cdot 7 \cdot 15 = 315.$$

**Growth ratio:**

$$\frac{N_{\text{flag}}(2,4)}{N_{\text{flag}}(2,3)} = \frac{315}{21} = 15 = 2^4 - 1.$$

So each increment of $n$ multiplies the flag count by $2^{\,n} - 1$: the number of complete flags grows super-exponentially in $n$, i.e. $N_{\text{flag}}(2,n) \geq \prod_{j=1}^{n} 2^{\,j-1} = 2^{\,n(n-1)/2}$, since each factor $2^j - 1 \geq 2^{\,j-1}$ for $j \geq 1$. For $n = 4$ this lower bound gives $2^{6} = 64 \leq 315$, consistent with the exact value.

### 4.2 Type counts for flag-algebra certificates

**Input 2 (stated assumption, following the setting of [3]).** In the flag algebra method for finite simple graphs, a certificate is built from "types": small graphs of a fixed size $k$. Under the stated assumption that types are labeled graphs on $k$ vertices, the number of labeled types is at most the number of labeled simple graphs,

$$T_{\text{lab}}(k) = 2^{\binom{k}{2}}.$$

**Derivation for $k = 4$:** $\binom{4}{2} = \frac{4 \cdot 3}{2} = 6$, so

$$T_{\text{lab}}(4) = 2^{6} = 64.$$

**Derivation for $k = 5$:** $\binom{5}{2} = 10$, so $T_{\text{lab}}(5) = 2^{10} = 1024$, a growth factor of $1024 / 64 = 16 = 2^{4}$ per added vertex. A semidefinite-programming certificate over types of size $k$ involves a positive-semidefinite matrix whose dimension scales with the type count; under the labeled-type assumption, the matrix dimension is at most $T_{\text{lab}}(k)$, so the number of free scalar entries is at most

$$M(k) = \frac{T_{\text{lab}}(k)\,(T_{\text{lab}}(k) + 1)}{2}.$$

For $k = 4$: $M(4) = \frac{64 \cdot 65}{2} = 2080$. For $k = 5$: $M(5) = \frac{1024 \cdot 1025}{2} = 524800$. The ratio $M(5)/M(4) = 524800 / 2080 \approx 252.31$ shows the quadratic-in-dimension cost explosion of enlarging the flag size by one vertex. These are upper bounds under the labeled assumption; the actual method uses unlabeled types, so the true counts are smaller, and we report the labeled numbers as explicit upper bounds only.

### 4.3 Information capacity of a three-state flag

**Input 3 (definition from Section 3).** The status alphabet has size $|\{R, Q, F\}| = 3$. The information capacity of one flag, in bits, is

$$I_{\text{flag}} = \log_2 3 \approx 1.58496.$$

**Derivation:** $\log_2 3 = \frac{\ln 3}{\ln 2} = \frac{1.098612\ldots}{0.693147\ldots} \approx 1.58496$. A corpus of $m$ independently flagged items carries at most $m \log_2 3$ bits of status information; for the single grounding flag ($m = 1$), the capacity is $\approx 1.58$ bits, of which the grounding act uses one of three symbols.

### 4.4 The stated investment figure

**Input 4 (from [9], taken as stated, not independently verified).** The entry for [9] states a figure of $35$ billion of investment in quantum computing hardware. We use it only to illustrate scale arithmetic: $35$ billion $= 3.5 \times 10^{10}$ dollars. If a flagging scheme costs $c$ dollars per audit and the community performed one audit per $10^{9}$ dollars of investment, the number of audits at that rate would be

$$\frac{3.5 \times 10^{10}}{10^{9}} = 35.$$

This is a hypothetical rate, stated as such; the entry for [9] does not report any audit count, and we draw no conclusion from this division beyond its arithmetic.

### 4.5 The re-entry flag

The grounding block assigns status $Q$ (open question) to DOI 10.5281/zenodo.23159238. Under A2 (symmetric scrutiny), this paper must apply the same standard to itself: this paper's own central claim — that $\Phi_{\mathcal{S}}$ is a coherent, useful abstraction — is itself assigned status $Q$, not $R$, because no empirical deployment is reported here. The paper therefore contains exactly two $Q$-flags: the re-entry DOI and the paper's own thesis.

## 5. Results

We report only values computed in Section 4.

- **R1.** The number of complete flags in $\mathbb{F}_2^3$ is $N_{\text{flag}}(2,3) = 21$ (Section 4.1, exact).
- **R2.** The number of complete flags in $\mathbb{F}_2^4$ is $N_{\text{flag}}(2,4) = 315$, with growth ratio $15 = 2^4 - 1$ per increment of $n$ at this step, and general lower bound $N_{\text{flag}}(2,n) \geq 2^{\,n(n-1)/2}$ (Section 4.1, exact and bound).
- **R3.** Under the stated labeled-type assumption, the number of graph types on $k = 4$ vertices is at most $T_{\text{lab}}(4) = 64$, and on $k = 5$ vertices at most $T_{\text{lab}}(5) = 1024$; the corresponding upper bounds on free scalar entries in a type-space SDP certificate are $M(4) = 2080$ and $M(5) = 524800$ (Section 4.2, upper bounds under a stated assumption).
- **R4.** The information capacity of one three-state flag is $I_{\text{flag}} = \log_2 3 \approx 1.58496$ bits (Section 4.3, exact expression with numerical evaluation).
- **R5.** At the hypothetical audit rate of one audit per $10^{9}$ dollars, the $3.5 \times 10^{10}$ dollar figure stated in [9] corresponds to $35$ audits; this is a projection under a stated hypothetical rate, not a report of any actual audit count (Section 4.4).
- **R6.** The grounding block assigns status $Q$ to DOI 10.5281/zenodo.23159238; this paper assigns status $Q$ to its own central thesis under axiom A2 (Section 4.5, status assignments, not empirical results).

No simulation results, no empirical measurements, and no claims about the content of DOI 10.5281/zenodo.23159238 are reported.

## 6. Discussion

**Limitations.** The central limitation is unavoidable: the re-entry document 10.5281/zenodo.23159238 was not supplied to us. Every statement in this paper about it is a statement about its *flag status* ($Q$), not its content. A reader hoping for a summary or critique of that document will find none here, and any such summary in a draft of this paper would have been fabrication.

**The metaphor risk.** The paper's unifying claim — that flag varieties, flag matroids, flag algebras, flag curvature, and epistemic flagging share a nested/directional structure — is an analogy, not a theorem. We have not exhibited a single formal object that instantiates all of these. A skeptic could correctly object that the shared word is doing rhetorical work that the mathematics does not underwrite. The strongest version of this objection: the flag curvature of [2] is an analytic invariant, while the flag matroids of [1] are combinatorial, and nothing in the supplied entries connects them beyond vocabulary. We accept this objection and downgrade the unification claim accordingly: what is shared is the *methodological role* (marking accessible regions of a space), not the mathematics.

**Failure modes of the flagging operator.** Three are visible. (i) *Threshold arbitrariness:* the transitions $e_{Q \to R}$ and $e_{R \to F}$ are community conventions; a badly calibrated threshold turns $\Phi_{\mathcal{S}}$ into a noise amplifier. (ii) *Certificate gaming:* the gate of [3]-style mechanical checking is only as strong as the checker; a formalization with a truncated specification (as the entry for [3] itself is truncated) can admit malformed certificates. (iii) *Reflexivity failure:* without A2, a flagging authority becomes an unaccountable gatekeeper; [11]'s symmetric-scrutiny audit is the supplied model, but the entry reports only that Theorem 1 of the audited work is the most sophisticated challenge to QNFO's position — it does not report who prevailed, so we cannot claim the reflexive loop closes in practice.

**What would falsify our claims.** The combinatorial results R1–R4 are exact arithmetic and cannot be falsified, only rechecked. The framework claim — that $\Phi_{\mathcal{S}}$ with axioms A1–A3 is useful — would be falsified by a demonstration that any real corpus resists uniform status assignment (violating A1) or that symmetric scrutiny produces no status changes in a corpus with known errors (showing A2 is vacuous). The claim that the re-entry item is an open question would be falsified by the document itself: if 10.5281/zenodo.23159238 contains a completed result with a checkable proof, the $Q$ flag must be promoted to $R$ under the certificate gate.

**Open questions.** (1) What is the correct evidence parameter $e$ and who measures it? (2) Does the $\mathbb{Z}_2$ observable of [10], if it operates at the hardware level as the entry states, constitute a physical certificate gate in the sense of Section 3.1 — i.e., can a hardware measurement promote or demote a theoretical flag? (3) Does the single representation-theoretic origin claimed in [12] for position-operator underdetermination across Archimedean and $p$-adic places extend to a single origin for status distinctions across heterogeneous corpora, as our Section 2 reading suggests? (4) What audit rate is actually sustainable for a field at the investment scale stated in [9]? None of these are answered here.

## 7. Conclusion

We have treated "flagging" as a single epistemic operator with a three-state alphabet, certificate-gated transitions, and three axioms drawn from the supplied literature: uniformity after the task-universe methodology of [7], symmetric scrutiny after the audit practice of [11], and two-directional incidence after the bioriented constructions of [6]. The mathematical flag literature supplied the structural vocabulary — forbidden-minor obstructions [1], directional invariants [2], certificate gates [3], cellular status topology [4], explicit generation rules [5] — and the QNFO programme supplied the live application domain in which large-scale flagging of a research programme is already underway [9], [10], [11], [12]. The concrete outputs are exact counts ($21$ and $315$ complete flags over $\mathbb{F}_2$), explicit upper bounds on flag-algebra certificate size ($64$ and $1024$ types; $2080$ and $524800$ scalar entries under the labeled assumption), and the information capacity of a three-state flag ($\log_2 3 \approx 1.58496$ bits). The re-entry from 10.5281/zenodo.23159238 stands in this paper exactly as the grounding block places it: flagged as an open question rather than a result, with the promotion condition stated and the burden of proof assigned.

## References

[1] arXiv:2504.00267v2 | Representability of Flag Matroids

[2] arXiv:1407.3582v2 | Even dimensional homogeneous Finsler spaces with positive flag curvature

[3] arXiv:2607.23500v1 | Formalizing Flag Algebras in Lean

[4] arXiv:2211.11168v2 | Total positivity in twisted product of flag varieties

[5] arXiv:2103.16197v2 | Standard monomial theory and toric degenerations of Richardson varieties in flag varieties

[6] arXiv:1810.05604v2 | Bioriented flags and resolutions of Schubert varieties

[7] arXiv:2107.12808v2 | Open-Ended Learning Leads to Generally Capable Agents

[8] arXiv:1512.03308v2 | Guaranteed inference in topic models

[9] QNFO: The Valuation Reading of the Qubit Delusion: Is the Adelic Kernel Load-Bearing?

[10] QNFO: Vanishing ZBW Signal: The ZBW-Majorana Hypothesis as a Unified Framework for Topological Fermion Distinction

[11] QNFO: The Vast World of Quantum Advantage — A Full-Spectrum Audit

[12] QNFO: The Adelic ZBW Programme: ZBW-Majorana Hypothesis, Ostrowski-QEC Synthesis, and Cross-Programme Consilience