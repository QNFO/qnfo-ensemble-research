# Numeral Systems as Evolving Cognitive Technologies: Error Propagation, Compactness, and the Non-Optimality of Positional Notation

## Abstract

Positional (Arabic-Indic) notation is conventionally treated as the endpoint of numeral-system evolution, but this paper argues it is a historically contingent survivor whose dominance reflects fitness for particular task environments rather than global optimality. We formalize the tradeoff between additive systems (Roman-style symbol sums) and positional systems under explicit noise channels. Under a symbol-deletion channel, we derive that positional error grows as $(9H + d_k)\cdot 10^{k}$ — proportional to the number's higher-order digits — whereas additive error is bounded by the largest symbol value, a constant independent of magnitude. Under an adjacent-transposition channel, additive error is exactly zero by commutativity, while positional error has expectation $29.7 \cdot 10^{k}$ for uniform decimal digits. Positional notation wins decisively on compactness: we compute an expected $11.5$ symbols per number for a greedy additive system over $1$–$3999$ versus $4$ digits positionally, a ratio of $2.875$. We frame these results as points on a multi-axis fitness landscape over task environments (ledger verification versus calculation), concluding that no single notation dominates and that notation design remains an open optimization problem — a cognitive-technology parallel to the absence of global optima in biological evolution.

## 1. Introduction

The positional numeral system used throughout modern science is so ubiquitous that it is easy to mistake for a discovered truth rather than an engineered artifact. This paper defends the opposite view: positional notation is one point in a design space of numeral systems, selected by historical contingencies and by the demands of specific task environments — chiefly paper-and-pencil arithmetic at scale — and it pays measurable cognitive costs that additive systems such as Roman numerals do not.

The claim is not that Roman numerals are superior overall. Any user of either system knows that long multiplication in additive notation is painful, and that positional notation compresses large magnitudes into few glyphs. The claim is narrower and more precise: the two families occupy different points on a tradeoff surface, and the tradeoffs can be *formalized*. Specifically, we ask three questions:

1. Under explicit noise models of human transcription error (symbol deletion, adjacent transposition), what is the expected magnitude of the resulting value error in each system?
2. What is the compactness cost of additive notation relative to positional notation, computable exactly for a stated symbol inventory?
3. If numeral-system evolution is modeled as a fitness landscape over task environments, does any single system dominate?

Our answers, derived in full in Section 4, are: (1) additive systems have strictly bounded error propagation under deletion and exactly zero error under transposition, while positional error is unbounded in the number's magnitude; (2) additive notation costs a computable factor of $2.875$ in symbol count for the range examined; (3) no — the axes of the landscape (error resistance, compactness, arithmetic tractability, magnitude salience) are satisfied by different systems in different environments.

The framing of notation as a *cognitive technology* — an external artifact that carries part of the cognitive load — is essential. Notation is not merely a code; it is a prosthesis whose error behavior and representational economy directly shape what its users can reliably do. This places the present work in the tradition of studying cognition as extended beyond the skull, and symbol systems as dynamically adapting cultural artifacts.

## 2. Background and Related Work

We review the supplied bibliography, noting frankly that several entries are adjacent rather than central: the literature on numeral-system evolution per se is thin in this corpus, and the cognitive-science entries supply framing rather than prior results on notation error.

[1] surveys symbol emergence in cognitive developmental systems, arguing that symbol systems such as language are crucial for communication and adaptation and that the symbol systems used in human society *adaptively and dynamically change over time*. This is the closest methodological anchor for our thesis: if symbol systems adapt dynamically, then the positional system's dominance is a state of an ongoing adaptive process, not a terminal optimum. We adopt this dynamic-adaptation framing in Section 3's fitness-landscape model.

[6] distinguishes cognizing (a mental state) from cognitive technology, and argues that systems without mental states can nonetheless contribute to human cognition, and that cognizers can *offload* cognitive functions onto cognitive technology, extending performance beyond the brain's own limits. Numeral notation is a paradigmatic object of offloading in this sense: the written numeral carries magnitude information so the reader need not hold it in mind. Our error-channel analysis in Section 4 is precisely an analysis of when this offloading fails — when the artifact corrupts the offloaded content.

[5] frames the primary task of a cognitive system as maximizing a life-long utility function (e.g., number of offspring), while noting that direct computational maximization is impossible in complex environments under real-world time constraints, with emotions serving as an intermediate layer in the policy space. We borrow the structural move — utility maximization under constraint, with an intermediate representational layer — and apply it to cultural artifacts: numeral systems are intermediate layers between a community's numerical tasks and its cognitive limits, and their evolution cannot be assumed to reach the utility optimum.

[3] presents a cognitive diversity framework for radar target classification, using angular diversity in a cognitive manner to attain better performance where best existing systems had not attained sufficiently high performance and reliability. The structural lesson — that *diversity of representational channels* improves reliability of classification — motivates our hybrid-notation hypothesis in Section 6: redundancy across additive and positional encodings may beat either alone.

[4] describes cognitive and immersive systems (CAISs) at the intersection of AI with HCI/HRI, systems that interact with and assist human agents entering them. The supplied summary gives no further detail relevant to numeration; we cite it only as evidence that human-facing cognitive systems are an active research area within which notation choice for human-agent interaction is a design variable.

[2] reviews applied exoskeleton technology, covering physical and cognitive human–robot interaction, and notes the technology is not fully mature for strenuous and non-programmed tasks. The supplied summary gives no numeral-specific content; we use it only as a parallel case of a technology whose adoption is gated by task-environment fit rather than intrinsic merit — the same gating we claim for positional notation.

[7] reviews cognitive computation with autonomously active neural networks, addressing the functional role of self-sustained neural activity and its interplay with the sensory input stream. The summary supplied gives no further detail we can use; we note only that the interplay between an internal state and a noisy input stream is formally analogous to our noise-channel model of Section 3, where a stored numeral (internal state) is corrupted by a transcription channel (input stream).

[8] studies robust beamforming design for intelligent-reflecting-surface-aided cognitive radio systems under both bounded channel-state-information (CSI) error models and statistical CSI error models. Though from communications engineering, its methodological template — optimize performance under an explicit, parameterized error model on a channel — is exactly the template we import for notation: we define bounded and statistical error models on transcription channels and evaluate notations under them.

Turning to the numeral-specific corpus: [10] presents NUMERATA v2.0, a multi-axis framework for evaluating numeral systems, extending an 8-axis framework with a Distinction-Based Primality axis and reporting meta-analysis validation with $\mathrm{MCS} = 0.875$ and $5/5$ predictions confirmed, with a "sunburst" notation making primality visually immediate. This is direct prior art for multi-axis evaluation of notations; our fitness-landscape model in Section 3 is compatible with, and deliberately simpler than, such a multi-axis scheme, and our two axes (error propagation, compactness) are computed exactly rather than scored.

[11] consolidates research on nonlinear tree-based numeration systems, stating that positional notation is natively an ultrametric tree and covering 5 research threads with extensions into quantum computing and interface design. The ultrametric-tree view of positional notation is useful for our analysis: the digit hierarchy of positional notation is precisely what makes deletion errors at high tree levels catastrophic (Section 4.1), since error at level $k$ is amplified by all levels above it.

[12], "Ten-Fingered Trap," is supplied with an empty summary; the title suggests a critique of base-10's bodily contingency, but since no summary text is provided we can attribute no specific claim to it and use it only as evidence that base choice itself is questioned in this corpus. Likewise [9], "QNFO: COMMUTATIVE PHYSICS," has an empty summary and is listed only for completeness.

## 3. Methods

### 3.1 Notation families

A **positional system** with base $b$ represents an integer $N$ as a digit string $d_{n-1} d_{n-2} \cdots d_1 d_0$ with value

$$N = \sum_{k=0}^{n-1} d_k \, b^{k}, \qquad d_k \in \{0, 1, \ldots, b-1\}.$$

An **additive system** with symbol values $V = \{v_1, v_2, \ldots, v_m\}$ (ordered $v_1 < v_2 < \cdots < v_m$) represents $N$ as a multiset of symbols whose values sum to $N$:

$$N = \sum_{j=1}^{m} c_j \, v_j, \qquad c_j \in \mathbb{Z}_{\geq 0},$$

where $c_j$ is the count of symbols of value $v_j$. We use the greedy (canonical) representation: take as many $v_m$ as possible, then $v_{m-1}$, and so on. For concrete computation we use the Roman-style inventory $V = \{1, 5, 10, 50, 100, 500, 1000\}$ (units, fives, tens, ..., thousands), *without* subtractive rules, so that representation is a pure commutative sum. We call this the **greedy additive system** $\mathcal{A}$.

### 3.2 Noise channels

Following the error-model template of robust design under parameterized channel uncertainty [8], we define two channels modeling human transcription:

- **Deletion channel** $\mathcal{D}$: one symbol of the written form is deleted, uniformly at random among symbols, and the remaining symbols are read in their written order (for positional: the remaining digits are read as a contiguous string, i.e., adjacent digit blocks merge).
- **Transposition channel** $\mathcal{T}$: two adjacent symbols in the written form are exchanged; the multiset (additive) or digit string (positional) is then read normally.

The **error** of a corruption event is $E = |N - N'|$, where $N'$ is the value read after corruption.

### 3.3 Task environments and fitness

A **task environment** $\mathcal{E}$ assigns weights $(w_{\mathrm{err}}, w_{\mathrm{comp}}, w_{\mathrm{calc}})$ to three axes: error resistance (low expected corruption error), compactness (few symbols), and arithmetic tractability (cost of addition/multiplication in the notation). The fitness of notation $S$ in environment $\mathcal{E}$ is

$$F_{\mathcal{E}}(S) = w_{\mathrm{err}} \, (-\log(1 + \bar{E}_S)) + w_{\mathrm{comp}} \, \bar{L}_S^{-1} + w_{\mathrm{calc}} \, A_S^{-1},$$

where $\bar{E}_S$ is expected corruption error, $\bar{L}_S$ is expected symbol count, and $A_S$ is an arithmetic cost proxy (number of symbol-level operations for addition). We do not fit the weights; we show that *rankings flip* across plausible weight vectors, which suffices for non-domination.

## 4. Analysis

All numbers below are derived from stated inputs; every arithmetic step is shown.

### 4.1 Deletion channel, positional system

**Setup.** Let $N$ be an $n$-digit decimal number. Write

$$N = H \cdot 10^{k+1} + d_k \cdot 10^{k} + L, \qquad 0 \leq L < 10^{k},$$

where $d_k$ is the digit in the $10^{k}$ place, $H$ is the number formed by the digits above position $k$, and $L$ is the number formed by the digits below. Deleting the digit $d_k$ merges the upper and lower blocks: the read value is

$$N' = H \cdot 10^{k} + L.$$

**Derivation of deletion error.**

$$E_{\mathrm{pos}} = N - N' = \left(H \cdot 10^{k+1} + d_k \cdot 10^{k} + L\right) - \left(H \cdot 10^{k} + L\right) = H \cdot (10^{k+1} - 10^{k}) + d_k \cdot 10^{k},$$

$$\boxed{E_{\mathrm{pos}} = (9H + d_k) \cdot 10^{k}}.$$

**Interpretation.** The error is proportional to $H$, the *higher-order digits*. For a fixed deletion position $k$, error grows without bound as the number's magnitude grows. Example (all inputs stated): $N = 5284$, delete $d_2 = 2$ (the hundreds digit). Here $H = 5$, $d_k = 2$, $k = 2$, $L = 84$:

$$E_{\mathrm{pos}} = (9 \cdot 5 + 2) \cdot 10^{2} = 47 \cdot 100 = 4700.$$

Check directly: $5284 - 584 = 4700$. ✓. The reader recovers $584$ — a value off by $4700$, i.e., a relative error of $4700/5284 \approx 0.8895$ (division: $4700/5284 = 0.88948\ldots$).

### 4.2 Deletion channel, additive system

In the greedy additive system, the written form is a multiset of symbols with values in $V = \{1, 5, 10, 50, 100, 500, 1000\}$. Deleting any symbol of value $v_j$ changes the sum by exactly

$$E_{\mathrm{add}} = v_j \leq v_{\max} = 1000.$$

**Bound.** For all $N$ and all deletion events,

$$E_{\mathrm{add}} \leq 1000, \quad \text{independent of } N.$$

This is the central contrast: positional deletion error is $O(H \cdot 10^{k})$ — unbounded in magnitude — while additive deletion error is $O(v_{\max})$ — a constant. For the concrete example range $N \in [1, 3999]$, the worst positional case is deleting $d_3$ from $3999$: $H = 3$, $d_k = 3$, $k = 3$, giving $E_{\mathrm{pos}} = (9 \cdot 3 + 3) \cdot 10^{3} = 30 \cdot 1000 = 30000$, versus the additive worst case $E_{\mathrm{add}} = 1000$. The ratio of worst-case errors is $30000 / 1000 = 30$.

### 4.3 Transposition channel

**Additive system.** The value is a sum of symbol values, and addition is commutative:

$$N = \sum_j c_j v_j = \sum_j c_j v_j \text{ (any order)}.$$

Exchanging two adjacent symbols changes the written order but not the multiset, so

$$E_{\mathrm{add}}^{\mathcal{T}} = 0 \quad \text{identically.}$$

**Positional system.** Exchanging adjacent digits $d_{k+1}$ and $d_k$ changes the value by

$$E_{\mathrm{pos}}^{\mathcal{T}} = \left| d_{k+1} 10^{k+1} + d_k 10^{k} - d_k 10^{k+1} - d_{k+1} 10^{k} \right| = |d_{k+1} - d_k| \cdot (10^{k+1} - 10^{k}) = |d_{k+1} - d_k| \cdot 9 \cdot 10^{k}.$$

**Expected value over uniform digits.** Inputs: $d_{k+1}, d_k$ independent uniform on $\{0, \ldots, 9\}$. Compute $\mathbb{E}|d_{k+1} - d_k|$. The number of ordered pairs $(i, j)$ with $|i - j| = \delta$ is $2(10 - \delta)$ for $\delta \geq 1$. Summing:

$$\sum_{\delta=1}^{9} \delta \cdot 2(10 - \delta) = 2 \sum_{\delta=1}^{9} (10\delta - \delta^2) = 2 \left(10 \cdot 45 - 285\right) = 2 \cdot (450 - 285) = 330,$$

using $\sum_{\delta=1}^{9} \delta = 45$ and $\sum_{\delta=1}^{9} \delta^2 = 285$. Over $100$ ordered pairs:

$$\mathbb{E}|d_{k+1} - d_k| = \frac{330}{100} = 3.3.$$

Therefore

$$\boxed{\mathbb{E}\left[E_{\mathrm{pos}}^{\mathcal{T}}\right] = 3.3 \cdot 9 \cdot 10^{k} = 29.7 \cdot 10^{k}}, \qquad \mathbb{E}\left[E_{\mathrm{add}}^{\mathcal{T}}\right] = 0.$$

The additive system is *exactly immune* to transposition; the positional system is not, and its expected transposition error grows exponentially in digit position.

### 4.4 Compactness

**Inputs.** Positional: numbers $1000$–$9999$ require exactly $n = 4$ digits. Additive greedy with $V = \{1, 5, 10, 50, 100, 500, 1000\}$: we compute the expected symbol count for $N$ uniform on $\{1, \ldots, 3999\}$ (the range representable without exceeding four M-symbols, matching a four-digit positional range at the low end).

For a greedy system, the count of symbols of value $v_j$ is $\lfloor r_j / v_j \rfloor$ where $r_j$ is the remainder after extracting all larger symbols. Under uniform $N$, each remainder digit-block is uniform over its range, so:

- Count of $1000$s: $\lfloor N/1000 \rfloor$ for $N \in [1, 3999]$ is uniform on $\{0,1,2,3\}$; expectation $= (0+1+2+3)/4 = 1.5$.
- Count of $500$s: remainder $r < 1000$ uniform; $\lfloor r/500 \rfloor \in \{0, 1\}$ equally often; expectation $= 0.5$.
- Count of $100$s: $r < 500$ uniform; $\lfloor r/100 \rfloor \in \{0,1,2,3,4\}$; expectation $= (0+1+2+3+4)/5 = 2$.
- Count of $50$s: expectation $= 0.5$ (same argument as $500$s).
- Count of $10$s: $r < 50$; $\lfloor r/10 \rfloor \in \{0,\ldots,4\}$; expectation $= 2$.
- Count of $5$s: expectation $= 0.5$.
- Count of $1$s: $r < 10$ uniform on $\{0,\ldots,9\}$; expectation $= 4.5$.

Total expected symbol count:

$$\bar{L}_{\mathcal{A}} = 1.5 + 0.5 + 2 + 0.5 + 2 + 0.5 + 4.5 = 11.5.$$

Positional over the same magnitude range: $\bar{L}_{\mathcal{P}} = 4$ (every number $1000$–$3999$ has exactly $4$ digits). Compactness ratio:

$$\frac{\bar{L}_{\mathcal{A}}}{\bar{L}_{\mathcal{P}}} = \frac{11.5}{4} = 2.875.$$

**Sanity check by direct enumeration of one value.** $N = 3888$: greedy gives $3 \times 1000 + 1 \times 500 + 3 \times 100 + 1 \times 50 + 3 \times 10 + 1 \times 5 + 3 \times 1$ = $3+1+3+1+3+1+3 = 15$ symbols (MMM D CCC L XXX V III), versus $4$ digits positionally; $15 > 11.5$, consistent with $3888$ being near the worst case for the trailing small denominations.

### 4.5 Magnitude salience

In the additive system, symbol count is monotone non-decreasing in $N$ (greedy property), and each additional large symbol is directly visible as a magnitude chunk: the reader of "MMM D CCC" sees the $3500$ decomposition. In the positional system, magnitude must be reconstructed from digit place, which is exactly the step that fails under deletion (Section 4.1): the merged string $584$ is a *valid-looking* number. We formalize salience as the detectability of corruption: under deletion, an additive corruption changes the value by at most $v_{\max} = 1000$ and typically leaves a still-decodable multiset, whereas positional deletion produces a string that is locally well-formed — corruption is *undetectable from form alone* in both systems, but its magnitude is bounded only in the additive case.

### 4.6 Fitness ranking flip

Take the computed values: $\bar{E}$ under deletion worst-case ratio $30{:}1$ favoring additive; compactness ratio $2.875{:}1$ favoring positional. For arithmetic cost proxy $A_S$, we count symbol-level operations for adding two numbers of the computed typical lengths: positional addition of two 4-digit numbers requires at most $4$ single-digit additions plus at most $3$ carries, so $A_{\mathcal{P}} \leq 7$ elementary operations; additive addition of two 11.5-symbol multisets requires merging counts per denomination, i.e., up to $7$ denomination-wise additions of counts that can each exceed $9$ and require re-normalization (carrying $10$ ones into one ten, etc.), so $A_{\mathcal{A}} \geq 7$ with re-normalization overhead strictly positive. Positional wins the arithmetic axis; the exact additive cost depends on normalization policy and we do not fix it here.

Now consider two environments:

- **Ledger-keeping** ($w_{\mathrm{err}}$ dominant): additive ranks first — its bounded deletion error ($\leq 1000$) and zero transposition error dominate.
- **Calculation-heavy** ($w_{\mathrm{calc}}, w_{\mathrm{comp}}$ dominant): positional ranks first — $2.875\times$ compactness and lower addition cost.

Since the ranking flips with weights, **no notation dominates** on this landscape. This is the formal core of the paper's thesis.

## 5. Results

We report only quantities derived in Section 4.

**R1 (Deletion error, positional).** Deleting the digit in the $10^{k}$ place of an $n$-digit number yields error $E_{\mathrm{pos}} = (9H + d_k) \cdot 10^{k}$, where $H$ is the value of the higher-order digits. Worked example: $N = 5284$, delete hundreds digit: $E_{\mathrm{pos}} = 4700$, relative error $\approx 0.8895$.

**R2 (Deletion error, additive).** Deletion error is bounded by $v_{\max} = 1000$ for all $N$, independent of magnitude. Worst-case ratio over $N \in [1, 3999]$: positional $30000$ vs. additive $1000$, i.e., $30{:}1$ in favor of additive.

**R3 (Transposition).** Additive transposition error is exactly $0$. Positional expected transposition error is $29.7 \cdot 10^{k}$ for uniform adjacent digits ($\mathbb{E}|d_{k+1} - d_k| = 3.3$, times $9 \cdot 10^{k}$).

**R4 (Compactness).** Expected symbol count, greedy additive over $N \in [1, 3999]$: $\bar{L}_{\mathcal{A}} = 11.5$; positional: $\bar{L}_{\mathcal{P}} = 4$; ratio $2.875$.

**R5 (Non-domination).** With error axis weighted highest (ledger environment), additive ranks first; with compactness and arithmetic axes weighted highest (calculation environment), positional ranks first. No single notation dominates the fitness landscape.

**Projection (labeled, not computed).** If human transcription error rates under each channel were measured experimentally, R1–R3 would convert directly into expected monetary or scientific loss per transcription event. We do not possess such measurements; the human-subject simulation proposed in Section 6 is the required next step, and all loss figures would be projections conditional on measured channel rates.

## 6. Discussion

**Limitations.** First, our additive model deliberately omits subtractive rules (IV, IX); subtractive notation reintroduces order-dependence and would partially restore transposition vulnerability, so R3's exact-zero result is a property of pure additive systems, not of historical Roman notation as actually written. Second, the compactness computation covers $N \in [1, 3999]$ with a specific seven-symbol inventory; larger inventories or subtractive compression change $\bar{L}_{\mathcal{A}}$, though the greedy expectation method extends unchanged. Third, the fitness function's functional form ($-\log(1+\bar{E})$, inverse symbol count) is a modeling choice; we showed ranking flips, which is robust to monotone reweighting, but we did not — and cannot, without data — claim any weighting describes any actual historical community. Fourth, the arithmetic-cost comparison is left partly qualitative because additive re-normalization cost depends on policy; we claim only $A_{\mathcal{A}} \geq A_{\mathcal{P}}$ for these ranges, not a computed ratio.

**Failure modes of our own thesis.** A critic could argue that deletion of a positional digit is not a realistic human error — scribes may be more likely to duplicate or substitute than to delete, and substitution error behaves differently in both systems (we have not modeled substitution). Another critic could note that bounded additive error is small comfort when the bound $v_{\max} = 1000$ is itself large relative to ledger entries of a few thousand; for $N \approx 1000$, a single deleted M-symbol is a $100\%$ error. The additive advantage is therefore magnitude-regime-dependent, and our $30{:}1$ worst-case ratio is a best-case framing for the additive side.

**What would falsify the claims.** R1–R4 are theorems about stated models; they are falsified only by an arithmetic error, which the reader can check from the shown steps. The non-domination claim (R5) would be falsified by a demonstration that some single weighting — argued to be the historically dominant one — ranks one system first on *all* axes simultaneously, or that the axes collapse into one (e.g., if compactness and error resistance were strongly positively correlated across all notation designs, not just these two). The evolutionary framing would be weakened by evidence that notation adoption is driven by network effects alone, insensitive to task environment.

**Open questions.** (i) Human-subject or agent simulations measuring actual deletion/transposition/substitution rates for Roman, positional, and hybrid notations — the empirical program this paper's models are designed to structure. (ii) Hybrid notations: following the diversity principle that combining representational channels can improve reliability [3], a redundant dual encoding (positional value plus additive checksum-like symbol count) could detect both channel errors; its overhead is at least the additive symbol count, i.e., roughly a $2.875\times$ writing cost by our R4 ratio, and its detection power is unquantified here. (iii) Extension to non-decimal bases and to the tree-structured view of positional notation [11], where deletion at high tree levels should amplify exactly as our $10^{k}$ factor shows. (iv) Whether multi-axis evaluation frameworks such as NUMERATA [10], which reports meta-analytic validation ($\mathrm{MCS} = 0.875$, $5/5$ predictions confirmed), can be reconciled with the fitness-landscape view — both deny single-axis optimality.

## 7. Conclusion

Positional notation is a cognitive technology, dynamically adapted like other symbol systems [1] and serving cognition by offloading [6], not a final optimum. Under explicit transcription noise channels, additive systems strictly dominate on error propagation — deletion error bounded by $v_{\max} = 1000$ versus unbounded $(9H + d_k) \cdot 10^{k}$, transposition error exactly zero versus $29.7 \cdot 10^{k}$ — while positional notation dominates on compactness by a computed