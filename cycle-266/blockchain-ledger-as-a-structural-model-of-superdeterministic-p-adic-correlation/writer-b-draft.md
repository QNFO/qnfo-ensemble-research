# Hash-Chained Histories and Ultrametric Correlation: A Blockchain Ledger as a Structural Model of Superdeterministic p-adic Dependence

## Abstract

Superdeterminism explains Bell-test correlations by denying the statistical independence of measurement settings and hidden variables, but it is widely criticized as unconstrained because no concrete mathematical structure specifies how settings and hidden variables come to be correlated. We propose and partially formalize a candidate structure: a hash-linked ledger, in which each event-block's state is a deterministic function of its entire prior history, equipped with a p-adic (ultrametric) distance in which shared causal prefix length plays the role of valuation. We construct a mapping from hash-chained ledgers to p-adic integer chains, prove that the ledger's prefix-agreement relation satisfies the strong triangle inequality, and derive two quantitative consequences. First, if a fraction $q$ of measurement-setting pairs are correlated through a shared causal prefix, the CHSH quantity rises linearly from the local bound $S = 2$ to $S = 4$, and reproducing the Tsirelson bound $2\sqrt{2}$ requires $q^{\*} = \sqrt{2} - 1 \approx 0.4142$. Second, for a balanced hash function the model's outcome marginals remain uniform, so the no-signaling constraint is preserved despite the violation. For a binary hash alphabet the expected shared causal prefix between two independent history chains is exactly $1$ digit, and tampering with any single block in a $256$-bit hash chain is detected with probability at least $1 - 2^{-256}$ per verification. The result gives superdeterminism a falsifiable structural template and gives blockchain engineering an unexpected formal analogy worth testing by simulation.

## 1. Introduction

Experimental physicists running Bell tests, philosophers of physics assessing the loopholes in those tests, and theorists attempting to construct explicit hidden-variable models all face the same unresolved problem: superdeterminism — the hypothesis that measurement settings and the hidden variables of a system share a common cause — has no agreed mathematical formalism for the correlation it postulates. The cost of this gap is concrete. Without a structure that says *how* settings and hidden variables are correlated, superdeterministic models are accused of being unfalsifiable "free will" denials rather than physical theories, and working physicists have no template from which to build and test candidate models. A formalism that fixes the correlation structure would change the situation in two ways: it would convert a philosophical position into a class of checkable models, and it would specify a parameter — the degree of setting–history correlation — whose value can be estimated or bounded against experimental data.

This paper addresses that gap with a structural conjecture and a partial derivation. The conjecture is that a superdeterministic universe with p-adic (non-archimedean, hierarchical) correlations is structurally isomorphic to a blockchain ledger: each event-block's state is a deterministic hash of prior history, and the p-adic distance between two histories measures their shared causal prefix. The intuition is direct. Blockchain immutability arises because each block commits to the hash of all previous blocks, so global consistency is enforced by chained local determinism; superdeterministic global correlation arises, on this picture, the same way — every event carries a compressed commitment to the entire past, and two events are correlated exactly to the degree that their pasts coincide. The p-adic tree structure captures the fork-like branching of possible histories, in the same way that a ledger can fork before consensus resolves the fork.

The stakes of the derivation are specific. If the mapping holds, then the strength of Bell-test correlations is controlled by a single geometric quantity — the probability that two measurement events share a causal prefix of a given length — and the observed quantum correlations pin down a numerical value for that probability. If the mapping fails, the failure itself is informative: it would show that prefix-based correlation structures cannot reproduce quantum statistics, narrowing the space of viable superdeterministic formalisms.

The contributions of this paper are:

- A construction (Section 3, formalized in Section 4.1) mapping hash-linked ledger chains to p-adic integer chains, with a proof that the induced prefix distance satisfies the ultrametric (strong triangle) inequality, derived in Section 4.1.
- A statistical derivation (Section 4.2) showing that the expected shared causal prefix between two independent history chains is $E[K] = \frac{1}{p-1}$ digits — exactly $1$ digit for the binary case $p = 2$.
- A quantitative correlation result (Section 4.3): under a two-regime correlation model, the CHSH value is $S(q) = 2 + 2q$, so matching the Tsirelson bound requires the setting-correlation fraction $q^{\*} = \sqrt{2} - 1 \approx 0.4142$, derived in Section 4.3.
- A no-signaling argument (Section 4.4): balanced deterministic outcome functions preserve uniform marginals, so the model violates Bell inequalities without permitting signaling.
- An immutability-to-correspondence result (Section 4.5): single-block tampering in a $256$-bit hash chain is detected with probability $1 - 2^{-256}$ per verification, which fixes the rigidity of the causal structure the correlation model relies on.

## 2. Background and Related Work

This work sits at the intersection of three literatures: the engineering of hash-chained ledgers, the interpretation of superdeterminism, and the mathematics of non-archimedean spaces. We review each for the specific structural elements this paper reuses.

**Hash-chained ledgers.** The ledger model this paper formalizes is described concretely in the distributed-systems literature. [1] states that a blockchain ledger is "an immutable append-only data structure, which contains a sequence of historical transactions grouped into blocks," formed "by chaining the blocks together with hash pointers (i.e., a subsequent block contains the hash of its previous block)," and that any corruption of blocks discovered during integrity verification "leads to significant degradation of the peer functionality." Their LedgerGuard system validates ledgers of $1000$ to $10000$ blocks with $50$ to $150$ transactions per block at $3$ KB per transaction, which establishes that prefix-verification over long chains is a practically implemented operation, not merely a design abstraction. [9] identifies the key characteristics of blockchain systems as "consensus, provenance, immutability and finality" and explains that the "hash" is "a block signature and considers all data and transactions involved" — the property that makes a block a deterministic function of its entire past, which is precisely the property our isomorphism exploits. [10] implements this chaining in a security system where "each block of data is cryptographically linked to the previous one," ensuring "transparency, immutability, and resistance to tampering," and reports that post-quantum signing and encryption overhead is manageable (in-memory encryption of $2$ GB files in $1.3$ s versus $1.2$ s for a classical baseline), showing that the hash-chain primitive survives replacement of the hash family — relevant because our formalism is hash-family-agnostic. [2] quantifies the cost of global consistency: "Given a blockchain system with $n$ nodes, global consensus requirements inherently involve at least $O(n)$ message and storage complexity, with some BFT-like algorithms even demanding $O(n^{3})$," and notes that transaction validation "necessitat[es] tracing the entire blockchain history for confirmation." This full-history-tracing requirement is the computational dual of the superdeterministic claim that every event encodes its whole past. [4] models the ledger as "encrypted linked lists of transaction records" and reports established throughputs of "$7\text{--}15$ transactions per second on Bitcoin and Ethereum," using sharding to parallelize; the shard structure is a graph-theoretic precedent for our fork structure, since shards partition the transaction space the way p-adic balls partition the integer space. [6] studies the interval "between when a transaction is submitted through a wallet and when it is confirmed on-chain," during which "users face uncertainty about if, when, and/or how their transactions will appear on the blockchain," and catalogs preconfirmation protocols that provide earlier guarantees; in our geometric reading, a preconfirmation is a statement about which p-adic ball an event will land in before the fork resolves — an analogy we use in Section 7 to motivate a simulation test.

**Superdeterminism.** [7] attempts to make superdeterminism intuitive "by simulating a deterministic model system, a billiard game," in which "an initial 'bang' correlates all events, just as in the superdeterministic universe," and introduces "the notions of 'strong' and 'soft' superdeterminism." The billiard model is a global-common-cause picture but leaves the correlation structure implicit; our contribution is to make that structure explicit and metric, replacing the undifferentiated "bang" with a graded, prefix-measured degree of common cause. This is the specific gap in the superdeterminism literature that the ledger formalism addresses.

**Structural isomorphism as a method.** Two works in the corpus establish that proving a structural isomorphism is a productive way to transfer results between superficially different formal systems. [5] defines "dimensional stability as the invariance of the dimension of the spline space over structurally isomorphic T-meshes, where a structurally isomorphic map preserves edge intersections and the mutual positions of all edges," and shows that stability "is equivalently determined by the rank stability of the conformality matrix" — a demonstration that properties invariant under a structure-preserving map can be studied once and transferred to every system in the isomorphism class. [8] proves "that the principal types of the closed terms of the affine fragment of $\lambda$-calculus ... are structurally isomorphic to their interpretations, as partial involutions, in a natural Geometry of Interaction model," which explains an otherwise awkward semantic notion "in elementary terms." Both works justify the methodology of Section 3: rather than arguing by analogy, we define the map explicitly and prove the properties we need on one side, transferring them to the other.

**Non-archimedean structure.** [12] proposes that "the universe is constructed not from matter or energy, but from pure information," with "every quantum state function[ing] as a unit of data storage" and interactions "equivalent to calculations"; whatever one makes of the ontological claim, it supplies the informational reading of physical state that a hash-chain ontology requires. [13] works out the spectral consequences of p-adic geometry on Bruhat–Tits trees: for the regular tree with $p = 2$ and depth $D = 6$ it reports "a discrete and bounded spectrum" with "a mean eigenvalue of approximately $\mu \approx 1.984$," consistent with the known confinement of the regular-tree spectrum to $[-2\sqrt{p-1},\, 2\sqrt{p-1}]$, and a multi-base triangulation regression with "$R^2 = 0.998$" and coefficients $\alpha \approx 0.40$, $\beta \approx 0.30$, $\gamma \approx 0.20$ for bases $p = 2, 3, 5$. That the p-adic metric acts as "a robust, multi-dimensional coordinate system" on tree-structured data is the spectral counterpart of the prefix-distance we use. [14] benchmarks p-adic embeddings of hierarchical data against Euclidean and hyperbolic alternatives, using "mean and max distortion" (a perfect embedding has distortion $1.0$) and Spearman's rank correlation, and reports that "the p-adic embedding demonstrated near-perfect fidelity, vastly outperforming both Euclidean and hyperbolic alternatives," plus a simulated linear $O(D)$ scaling for quantum-walk traversal of a Bruhat–Tits tree. This is direct evidence that ultrametric geometry is the natural home for prefix-hierarchical data — the empirical motivation for measuring causal prefix by p-adic distance rather than by an archimedean metric.

We do not cite works on transactional-security applications or on economic critiques of competition, as they support no specific structural point used here.

## 3. Methods

This paper is theoretical: it performs no experiment, measurement, or simulation. Its method is (i) explicit construction of a structure-preserving map, (ii) derivation of statistical and information-theoretic consequences from stated assumptions, and (iii) arithmetic evaluation of every derived quantity. We state the model, the assumptions, and the derivation plan; the derivations themselves, with all arithmetic, are in Section 4.

**Model.** A ledger is a finite or countably infinite sequence of blocks $B_0, B_1, B_2, \ldots$ where each block $B_{t+1}$ contains the hash $h_{t+1} = H(B_{t+1}^{\text{payload}} \| h_t)$ of its payload concatenated with the previous block's hash, following the hash-pointer chaining described in [1] and [9]. We interpret the hash value as a digit string in base $p$ (we take $p = 2$ as the canonical case, since hash outputs are bit strings), so a hash chain defines a p-adic integer: the infinite chain $(h_0, h_1, h_2, \ldots)$ determines the p-adic limit $x = \lim_{t \to \infty} x_t$ where $x_t$ is the integer whose first $t$ base-$p$ digits are fixed by the chain. Two chains are causally related to degree $k$ if they agree on their first $k$ digits, i.e., if they share a causal prefix of length $k$.

**Distance.** We define $d_p(x, y) = p^{-v_p(x - y)}$, where $v_p(\cdot)$ is the p-adic valuation counting leading shared digits, with the convention $d_p(x, x) = 0$. Shared causal prefix of length $k$ therefore corresponds to distance $p^{-k}$.

**Assumptions.** We make four explicit assumptions, each used in a named derivation:

- (A1) *Hash balance.* The hash function $H$ is balanced: over the hash-output space, exactly half of inputs map to each output bit value, so deterministic outcome functions built on $H$ have uniform marginals. This is an idealization of cryptographic hash behavior; we use it only in the no-signaling derivation (Section 4.4).
- (A2) *Hash width.* The hash output is $n = 256$ bits, the width of standard production chains. Used in Section 4.5.
- (A3) *Two-regime correlation.* In a Bell-test embedding of the model, a fraction $q$ of setting pairs are determined by a shared causal prefix (fully correlated regime) and the complementary fraction $1 - q$ are prefix-independent (locally deterministic regime). This is a modeling assumption, not a claim about any experiment; it is the parameterization whose consequences Section 4.3 derives.
- (A4) *Independence of unshared prefixes.* Conditional on not sharing a causal prefix, the two wings' history chains are independent uniform digit sequences. Used in Section 4.2.

**Derivation plan.** Section 4.1 proves the ultrametric property of $d_p$ on the chain space. Section 4.2 computes the distribution and expectation of the shared prefix length $K$ under (A4). Section 4.3 computes the CHSH value $S(q)$ under (A3) and solves for the $q$ reproducing the Tsirelson bound. Section 4.4 derives uniform marginals from (A1). Section 4.5 computes the tamper-detection probability from (A2). Every input number is stated with its source (assumption or cited work) at first use.

## 4. Analysis

### 4.1 The ultrametric property of causal-prefix distance

**Claim.** On the hash-chain space, $d_p(x, y) = p^{-v_p(x-y)}$ satisfies the strong triangle inequality $d_p(x, z) \leq \max\{d_p(x, y),\, d_p(y, z)\}$.

**Derivation.** Let $v_p(x - y) = k_1$ and $v_p(y - z) = k_2$, meaning $x$ and $y$ share their first $k_1$ digits and $y$ and $z$ share their first $k_2$ digits. Then $x$ and $z$ both agree with $y$ on the first $\min(k_1, k_2)$ digits, so $x$ and $z$ agree on at least $\min(k_1, k_2)$ digits: $v_p(x - z) \geq \min(k_1, k_2)$. Exponentiating with base $p > 1$ reverses the inequality:

$$p^{-v_p(x-z)} \leq p^{-\min(k_1, k_2)} = \max\{p^{-k_1}, p^{-k_2}\}.$$

Hence $d_p(x, z) \leq \max\{d_p(x, y), d_p(y, z)\}$, which is stronger than the ordinary triangle inequality $d_p(x,z) \leq d_p(x,y) + d_p(y,z)$ because $\max\{a, b\} \leq a + b$ for non-negative $a, b$. $\blacksquare$

**Worked instance.** Take $p = 2$ and three chains: $x$ begins $0110\ldots$, $y$ begins $0111\ldots$, $z$ begins $1000\ldots$. Then $x$ and $y$ share $3$ digits ($v_2(x-y) = 3$), $y$ and $z$ share $0$ digits, and $x$ and $z$ share $0$ digits. The inequality reads $d_2(x,z) = 2^{0} = 1 \leq \max\{2^{-3}, 2^{0}\} = \max\{0.125, 1\} = 1$. Equality holds, as the inequality permits. Note the structural reading: two events are "close" exactly when their histories coincide deeply, and no chain of intermediaries can make two histories closer than their direct prefix agreement — the formal expression of "no correlation without common cause."

### 4.2 Distribution of shared causal prefix length

**Claim.** Under (A4), the shared prefix length $K$ between two independent chains satisfies $\Pr(K \geq k) = p^{-k}$ and $E[K] = \frac{1}{p-1}$; for $p = 2$, $E[K] = 1$ digit.

**Derivation.** Each digit of an independent chain is uniform over $\{0, \ldots, p-1\}$, so the probability that digit $j$ agrees is $\frac{1}{p}$, independently across digits (A4). Hence

$$\Pr(K \geq k) = \left(\frac{1}{p}\right)^{k} = p^{-k}.$$

The tail-sum formula for the expectation of a non-negative integer-valued random variable gives

$$E[K] = \sum_{k=1}^{\infty} \Pr(K \geq k) = \sum_{k=1}^{\infty} p^{-k} = \frac{p^{-1}}{1 - p^{-1}} = \frac{1}{p - 1}.$$

For $p = 2$: $E[K] = \frac{1}{2-1} = 1$. For $p = 3$: $E[K] = \frac{1}{2} = 0.5$. The geometric decay of $\Pr(K \geq k)$ in $k$ means correlation strength falls by a factor of exactly $p$ per digit of divergent history: for $p = 2$, each digit of independent history halves the residual correlation. This is the quantitative form of the statement that in a hash-chained ontology, common cause is a consumable resource consumed at a fixed rate by divergent history.

### 4.3 CHSH under two-regime correlation

**Claim.** Under (A3), the CHSH value is $S(q) = 2 + 2q$; the Tsirelson bound $2\sqrt{2}$ is reproduced at $q^{\*} = \sqrt{2} - 1 \approx 0.414214$.

**Derivation.** The CHSH quantity is

$$S = \big| E(a, b) - E(a, b') + E(a', b) + E(a', b') \big|,$$

where $a, a'$ and $b, b'$ are the two setting choices at the two wings. In the prefix-independent regime (fraction $1 - q$), the wings share no causal prefix, outcomes are locally deterministic functions of independent chains, and the standard fine-grained bound for locally deterministic models applies: $S_{\text{local}} = 2$. This is the classical CHSH bound; we take it as the established value for the uncorrelated regime and note that it is achieved, for example, by the deterministic assignment $E(a,b) = E(a,b') = E(a',b) = +1$, $E(a',b') = -1$, giving $S = |1 - 1 + 1 - 1 \cdot (-1)|$... we instead use the standard extremal assignment $E(a,b) = 1$, $E(a,b') = 1$, $E(a',b) = 1$, $E(a',b') = -1$, which yields $S = |1 - 1 + 1 + (-1)| = 0$; the correct extremal assignment is $E(a,b) = 1$, $E(a,b') = -1$, $E(a',b) = 1$, $E(a',b') = 1$? We therefore recompute the local extremum explicitly rather than assert it.

*Explicit local extremum.* For deterministic local models, $E(a,b) = A(a)B(b)$ with $A, B \in \{+1, -1\}$. Then

$$S = |A(a)B(b) - A(a)B(b') + A(a')B(b) + A(a')B(b')| = |A(a)\,[B(b) - B(b')] + A(a')\,[B(b) + B(b')]|.$$

Since each of $B(b) - B(b')$ and $B(b) + B(b')$ is in $\{-2, 0, +2\}$ and one of them is always $0$ while the other is $\pm 2$, we get $S \leq |A(a)| \cdot 2 + |A(a')| \cdot 0$ or the symmetric case, i.e. $S \leq 2$ in every case, with equality when, e.g., $B(b) = B(b')$ and $A(a) = A(a') = B(b)$: then $S = |1 \cdot 2 + 1 \cdot 0| = 2$. So $S_{\text{local}} = 2$ exactly. ✓

In the fully prefix-correlated regime (fraction $q$), the two wings' settings and outcomes are both deterministic functions of the same causal prefix, so the model is free to realize any correlation pattern consistent with a single shared hidden variable; the algebraic maximum of CHSH over unconstrained joint distributions is $S_{\text{corr}} = 4$ (realized, e.g., by the PR-box relation $E(a,b) = a \oplus b$ mapped to $\pm 1$ products, giving $|E(a,b) - E(a,b') + E(a',b) + E(a',b')| = |1 + 1 + 1 + 1| = 4$). We assume the correlated regime realizes this maximum; relaxing this to any value $S_{\text{corr}} \leq 4$ only rescales the constant derived below.

Averaging the two regimes with weights $q$ and $1 - q$:

$$S(q) = (1 - q) \cdot 2 + q \cdot 4 = 2 - 2q + 4q = 2 + 2q.$$

Setting $S(q) = 2\sqrt{2}$:

$$2 + 2q = 2\sqrt{2} \;\Rightarrow\; q = \frac{2\sqrt{2} - 2}{2} = \sqrt{2} - 1.$$

Numerically, $\sqrt{2} = 1.41421356\ldots$, so

$$q^{\*} = \sqrt{2} - 1 = 0.41421356\ldots \approx 0.4142.$$

Sanity checks: $S(0) = 2$ (pure local, matches the bound just derived); $S(1) = 4$ (fully correlated, algebraic maximum); $S(0.5) = 3$, which exceeds the Tsirelson bound $2\sqrt{2} = 2.82842712\ldots$ — the model therefore predicts that a superdeterministic universe with binary-prefix correlation at the natural $q = 0.5$ would show *stronger*-than-quantum correlations, and quantum mechanics sits at the specific correlation fraction $q^{\*} \approx 0.4142$. The interpretation of $q^{\*}$ as a derived prediction is developed in Section 5 and Discussion.

### 4.4 No-signaling from hash balance

**Claim.** Under (A1), the model's outcome marginals are uniform, so the marginal statistics at one wing are independent of the setting chosen at the other: no signaling.

**Derivation.** Let $A(a^{\*}, \lambda) \in \{+1, -1\}$ be the deterministic outcome function at wing $A$, where $\lambda$ is the shared history state. By (A1), $H$ is balanced, so over the $\lambda$-space exactly half of the mass maps to $+1$:

$$\Pr(a = +1 \mid a^{\*}) = \sum_{\lambda} \Pr(\lambda)\, \mathbb{1}[A(a^{\*}, \lambda) = +1] = \frac{1}{2}.$$

The marginal does not depend on the other wing's setting $b^{\*}$ because $\lambda$'s distribution is fixed by the shared history and not by $b^{\*}$: in the prefix-correlated regime the *joint* distribution $P(a, b \mid a^{\*}, b^{\*})$ depends on both settings, but each marginal is the balanced sum over $\lambda$ and equals $\frac{1}{2}$ regardless. Hence

$$\Pr(a \mid a^{\*}, b^{\*}) = \Pr(a \mid a^{\*}, b) = \frac{1}{2},$$

which is the no-signaling condition. $\blacksquare$ The mechanism is worth stating: superdeterminism is often suspected of violating no-signaling because settings and hidden variables are correlated; here the correlation is