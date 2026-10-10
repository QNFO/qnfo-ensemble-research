# Ultrametric p-Adic Arithmetic as Energy-Proportional Precision Computing: An Energy Model for Digit-Serial Termination

## Abstract

Floating-point multiply-accumulate (MAC) operations pay a fixed, full-width energy cost regardless of the precision actually required by the computation. We conjecture that p-adic (ultrametric) number representations enable energy-per-operation that scales with required precision, because p-adic integers decompose hierarchically into digit residues and computation can terminate after $k$ digits without carries propagating across the whole word. We formalize this with a digit-serial energy model: a $k$-digit p-adic MAC over $p$-valued residues costs $E_{\mathrm{p}}(k) = k \cdot a \cdot p^2$, where $a$ is a per-bit-square switching coefficient calibrated from the stated 45 nm and 7 nm floating-point MAC energies of $3.7$ pJ and $0.9$ pJ. Under quadratic bit-complexity scaling, the p-adic-to-floating-point energy ratio is $k p^2 / n^2$ for an $n$-bit float, giving a computed $25.6\times$ saving at $k=10$ digits, $p=2$, $n=32$, and a precision-independent crossover at $k^* = n^2/p^2$ digits. We extend the model to off-chip communication, showing that hierarchical (tree-structured) digit movement changes the precision scaling of data volume from linear to logarithmic under stated assumptions. We sketch a validation protocol on neural-network inference workloads and identify the conditions — small $p$, low target precision, carry-free digit scheduling — under which ultrametric architectures beat Archimedean ones in joules per compute, and the failure modes that would falsify the conjecture.

## 1. Introduction

Every floating-point multiply-accumulate unit burns approximately the same energy whether its result is used to full precision or rounded away after two significant digits. This is a structural consequence of Archimedean arithmetic: the real numbers are ordered along a line, fixed-width representations must commit to a single absolute scale, and hardware must therefore evaluate every bit of the mantissa before the result is meaningful. Energy per operation is thus constant in the target precision, and precision-proportional savings can only be obtained by building separate units at multiple word lengths.

The p-adic numbers $\mathbb{Q}_p$ offer a different geometry. The p-adic valuation $v_p(\cdot)$ induces the ultrametric inequality $|x+y|_p \le \max(|x|_p, |y|_p)$, which has a computational consequence that is usually discussed only in number-theoretic contexts: two p-adic numbers are close exactly when they agree in their low-order digits, and arithmetic on the first $k$ digits is self-contained. Addition and multiplication of p-adic integers proceed digit-by-digit from the least significant residue upward, with carries moving toward higher digits but never backward. A computation that only needs $k$ digits of accuracy can therefore stop after $k$ digit-slices, and the energy it consumed is a function of $k$, not of a fixed machine word length.

This paper develops that observation into a quantitative research program. Our central conjecture is:

**Conjecture 1 (Energy-proportional precision).** There exist p-adic arithmetic architectures whose energy per MAC operation scales as $O(k^2)$ in the number of computed digits $k$ (or better, with carry-free digit-serial scheduling), whereas an Archimedean floating-point MAC costs a fixed $E_{\mathrm{FP}}$ independent of $k$; consequently, for workloads whose required precision is heterogeneous and bounded, p-adic arithmetic achieves lower joules per compute.

We make three contributions. First, we derive an explicit energy model for digit-serial p-adic MACs, calibrated against the reference floating-point MAC energies of $3.7$ pJ at 45 nm and $0.9$ pJ at 7 nm, and we compute the exact crossover precision and savings ratios (Section 4). Second, we project the savings on a neural-network inference workload with heterogeneous precision demand, with all assumptions stated (Section 5). Third, we analyze whether the hierarchical, tree-structured nature of ultrametric digit spaces reduces off-chip data movement, which in modern accelerators dominates total energy (Sections 4.3 and 6). Throughout, we are explicit about which numbers are derived here and which are labeled projections under stated assumptions; no empirical measurements are reported.

## 2. Background and Related Work

The p-adic literature relevant to this paper divides into three strands: pure number theory, ultrametric modeling of data and physical systems, and recent programmatic proposals for an "ultrametric paradigm."

**Number-theoretic foundations.** The p-adic Beilinson conjecture work of [1] formulates a p-adic analogue of Borel's theorem, relating syntomic regulators on number fields to special values of p-adic $L$-functions, and conjectures the precise relation between the p-adic and classical (Archimedean) regulator pictures. Although far from hardware, this line establishes the central conceptual device we exploit: p-adic and Archimedean worlds compute "the same" quantities through structurally different special-value relations, and the p-adic side is organized by valuation depth rather than by magnitude. Similarly, [4] introduces families of p-adic Stark regulators for Artin motives and an Iwasawa–Greenberg main conjecture relating them to p-adic $L$-functions; the regulator objects there are again naturally p-adic iterated objects whose information is graded by valuation level, prefiguring the digit-hierarchical view of computation. The p-adic analytic subgroup theorem revisited in [7] gives a systematic p-adic transcendence framework, demonstrating that p-adic analytic machinery can replicate classical results with purely non-Archimedean techniques — an existence proof that p-adic analytic computation is self-sufficient, not merely a shadow of the real theory.

**Ultrametric modeling of data and dynamics.** Reference [2] shows how cross-tabulated data can be embedded, via Correspondence Analysis, into a Euclidean space from which an induced ultrametric is extracted, and uses the ultrametric to model anomaly and change in sequential data. This is directly relevant to us because it demonstrates that real workloads (not idealized mathematical objects) can carry ultrametric structure, which is the empirical precondition for our conjecture: if a workload's operands live on an ultrametric tree, then precision demand is naturally digit-hierarchical. Reference [3] develops stationary Markov processes on ultrametric spaces isometrically embeddable into $\mathbb{Q}_p$, reducing their analysis to processes on $\mathbb{Q}_p$ itself; for us this supplies the stochastic-process formalism in which "how many digits does a random operand need" becomes a well-posed question about measure concentration on $\mathbb{Q}_p$. The p-adic Potts model on a Cayley tree of [5] reduces Gibbs-measure existence to a recursive equation and proves a phase transition occurs if and only if $p=3$; the Cayley tree is exactly the hierarchical digit tree our data-movement analysis uses, and the recursive-equation technique mirrors the digit-recurrence structure of p-adic arithmetic. Reference [6] introduces p-adic equiangular lines and proves the p-adic van Lint–Seidel relative bound $|n|^2 \le |d|\max\{|n|, \gamma^2\}$; this shows that even packing-type combinatorial questions — the bread and butter of signal processing and code design — admit sharp p-adic analogues, supporting the plausibility of p-adic signal-processing primitives. Finally, [8] builds a 5-adic model of the DNA sequence and genetic code, with nucleotides, codons, and genes as elements of an ultrametric p-adic information space; it is the cleanest existing demonstration that a natural information-carrying system aligns with a small-prime p-adic digit structure, which is precisely the regime ($p$ small, digits as residues) where our energy model predicts the largest advantage.

**Programmatic ultrametric proposals.** The QNFO Ultrametric Engine [9] formalizes twenty principles for discovery and navigation in ultrametric spaces under non-Archimedean distance constraints, establishing a workflow methodology rather than a hardware result, but its premise — that ultrametric distance constraints structure efficient search — is the software-level analogue of our hardware-level claim. The ultrametric-paradigm note [10] and the Consilience Framework [12] argue broadly that valuation theory provides a foundational layer for cross-domain synthesis; we take from these the framing that the Archimedean/ultrametric choice is a modeling decision to be made on cost grounds. The adelic-complexity and silent-radix material [11] is closest in spirit to our conjecture, proposing that radix-structured (adelic) representations change the complexity accounting of arithmetic; our energy model can be read as a first quantitative instantiation of that proposal for the MAC primitive.

What is missing from all of these strands, and what this paper supplies, is an explicit joules-per-operation model connecting ultrametric digit structure to CMOS switching energy.

## 3. Methods

### 3.1 Representation

Fix a prime $p$. A p-adic integer $x \in \mathbb{Z}_p$ is written in digit expansion

$$x = \sum_{i=0}^{\infty} x_i \, p^i, \qquad x_i \in \{0, 1, \dots, p-1\}.$$

The p-adic absolute value is $|x|_p = p^{-v_p(x)}$ with $v_p(x) = \min\{i : x_i \neq 0\}$. The ultrametric inequality $|x+y|_p \le \max(|x|_p,|y|_p)$ implies that the residue of $x + y$ or $x \cdot y$ modulo $p^k$ depends only on the residues of $x$ and $y$ modulo $p^k$:

$$\left( x \bmod p^k \right) \circ \left( y \bmod p^k \right) \equiv (x \circ y) \bmod p^k, \qquad \circ \in \{+, \times\}.$$

This congruence is the mathematical basis of early termination: a $k$-digit computation is exact for all arithmetic downstream that only consumes results modulo $p^k$, and carries flow only from digit $i$ to digit $i+1$ (never backward), so digit slices can be evaluated as a feed-forward pipeline.

### 3.2 Digit-serial MAC energy model

We model a digit slice as a $b$-bit fixed-point multiply-accumulate unit, where $b = \lceil \log_2 p \rceil$ bits suffice to hold one residue digit (for $p = 2$, $b = 1$; for $p = 3$ or $4$, $b = 2$). We assume the switching energy of a fixed-point MAC of width $b$ scales quadratically in $b$,

$$e_{\mathrm{MAC}}(b) = a \, b^2,$$

where $a$ (in pJ per bit$^2$) is a technology switching coefficient. This quadratic scaling is the standard coarse model for parallel multipliers (partial-product count grows as $b^2$); we state it as a modeling assumption and examine its failure modes in Section 6.

**Calibration.** The input block supplies two anchor points: a full floating-point MAC costs $E_{\mathrm{FP}}^{(45)} = 3.7$ pJ at 45 nm and $E_{\mathrm{FP}}^{(7)} = 0.9$ pJ at 7 nm. We take the float mantissa-plus-exponent datapath to be effectively a 32-bit fixed-point MAC, $n = 32$, so that

$$a_{45} = \frac{E_{\mathrm{FP}}^{(45)}}{n^2} = \frac{3.7}{1024} = 3.61328125 \times 10^{-3} \ \text{pJ/bit}^2,$$

$$a_{7} = \frac{E_{\mathrm{FP}}^{(7)}}{n^2} = \frac{0.9}{1024} = 8.7890625 \times 10^{-4} \ \text{pJ/bit}^2.$$

A $k$-digit p-adic MAC then costs

$$E_{\mathrm{p}}(k) = k \cdot a \, b^2,$$

and the energy ratio against a full float MAC is

$$R(k) = \frac{E_{\mathrm{p}}(k)}{E_{\mathrm{FP}}} = \frac{k \, b^2}{n^2}.$$

### 3.3 Workload model

For a workload of $M$ MACs where MAC $j$ requires $k_j$ digits of precision, total p-adic energy is $E_{\mathrm{p}}^{\mathrm{tot}} = \sum_{j=1}^{M} k_j \, a b^2$ versus fixed $E_{\mathrm{FP}}^{\mathrm{tot}} = M \, E_{\mathrm{FP}}$, giving the workload-level ratio

$$R_{\mathrm{work}} = \frac{b^2}{n^2} \, \bar{k}, \qquad \bar{k} = \frac{1}{M}\sum_{j=1}^{M} k_j.$$

Everything reduces to the distribution of required precision $k_j$, which we treat as a workload parameter (Section 5) rather than a measured quantity.

### 3.4 Off-chip communication model

Off-chip data movement is modeled parametrically. Let $E_{\mathrm{bit}}^{\mathrm{off}}$ be the energy per bit moved off-chip, and let $V(k)$ be the number of bits that must be moved to deliver a result to precision $k$ digits. For a flat (Archimedean) representation, a $k$-digit result still occupies the full $n$-bit word, so $V_{\mathrm{flat}}(k) = n$ per value. For a hierarchical p-adic representation delivered over a digit tree, we assume the receiver can request digits level by level (root = coarsest scale); delivering $k$ digits requires moving $b$ bits per level only if each level is a single digit, i.e., $V_{\mathrm{tree}}(k) = b k$ per value, but if the tree is navigated by descending one branch at a time and the receiver stops at the first level where the value is resolved, the expected number of levels is $O(\log k)$ under a uniform distribution of stopping depths. We state both the linear and logarithmic variants as labeled assumptions and compute their consequences in Section 4.3.

## 4. Analysis

### 4.1 Crossover precision

Every input number below is stated with its source: $E_{\mathrm{FP}}^{(45)} = 3.7$ pJ and $E_{\mathrm{FP}}^{(7)} = 0.9$ pJ are from the research idea's grounding block (Horowitz-style CMOS energy tables at 45 nm and 7 nm); $n = 32$ is our stated modeling identification of a float MAC with a 32-bit fixed-point MAC; $a$ is derived above.

The p-adic architecture beats the float MAC when $E_{\mathrm{p}}(k) < E_{\mathrm{FP}}$, i.e.,

$$k \, a \, b^2 < a \, n^2 \quad \Longrightarrow \quad k < k^* = \frac{n^2}{b^2}.$$

Note that $a$ cancels: the crossover is technology-independent under the quadratic model. For $p = 2$ ($b = 1$):

$$k^* = \frac{32^2}{1^2} = 1024 \ \text{digits}.$$

For $p = 4$ ($b = 2$):

$$k^* = \frac{1024}{4} = 256 \ \text{digits}.$$

For $p = 16$ ($b = 4$):

$$k^* = \frac{1024}{16} = 64 \ \text{digits}.$$

Since practical neural-network inference rarely needs more than a few tens of significant digits, and $k^* \ge 64$ in all small-$p$ cases, the model predicts p-adic dominance across the entire practically relevant precision range — with the important caveat that this hinges on the quadratic scaling assumption and on $b$ being small.

### 4.2 Savings ratio at concrete operating points

Take $p = 2$, so $b = 1$, $e_{\mathrm{digit}}^{(45)} = a_{45} b^2 = 3.61328125 \times 10^{-3}$ pJ per digit slice.

**Case $k = 10$ (ten 2-adic digits, i.e., resolution $2^{-10} \approx 9.77 \times 10^{-4}$):**

$$E_{\mathrm{p}}(10) = 10 \times 3.61328125 \times 10^{-3} = 3.61328125 \times 10^{-2} \ \text{pJ},$$

$$R(10) = \frac{3.61328125 \times 10^{-2}}{3.7} = \frac{10}{1024} = 9.765625 \times 10^{-3}.$$

The saving factor is $1/R(10) = 102.4\times$ at 45 nm. At 7 nm the ratio is identical by construction ($R$ is independent of $a$): $102.4\times$.

**Case $k = 3$, $p = 4$ ($b = 2$):**

$$R(3) = \frac{3 \times 4}{1024} = \frac{12}{1024} = 1.171875 \times 10^{-2}, \qquad \text{saving} = \frac{1024}{12} \approx 85.33\times.$$

**Case $k = 1$, $p = 2$ (single-bit-resolution MAC, e.g., binary neural networks):**

$$R(1) = \frac{1}{1024} = 9.765625 \times 10^{-4}, \qquad \text{saving} = 1024\times.$$

This last case recovers the well-known empirical fact that binary networks are orders of magnitude cheaper than float networks — here derived as the $k=1$ endpoint of a continuous precision-energy curve, which is the distinctive prediction of the p-adic model: the *intermediate* points ($k = 3, 10, \dots$) are reachable by the same hardware, whereas a fixed-width Archimedean design must build a separate unit per width.

### 4.3 Off-chip communication

Let the off-chip bit energy be $E_{\mathrm{bit}}^{\mathrm{off}}$ (parameter; see Section 6 for why we do not fix a value). Per delivered value:

- Flat: $V_{\mathrm{flat}} = n = 32$ bits, energy $32 \, E_{\mathrm{bit}}^{\mathrm{off}}$.
- Tree, linear variant: $V_{\mathrm{tree}}^{\mathrm{lin}}(k) = b k$ bits, energy $b k \, E_{\mathrm{bit}}^{\mathrm{off}}$.
- Tree, logarithmic variant: $V_{\mathrm{tree}}^{\log}(k) = b \log_2(k+1)$ bits under the stated uniform-stopping-depth assumption.

The communication saving factor (linear variant) is

$$S_{\mathrm{comm}}(k) = \frac{32}{b k}.$$

At $p = 2$, $k = 10$: $S_{\mathrm{comm}} = 32/10 = 3.2\times$. At $p = 2$, $k = 3$: $S_{\mathrm{comm}} = 32/3 \approx 10.67\times$. Under the logarithmic variant at $k = 10$: $V = \log_2 11 \approx 3.4594$ bits, $S_{\mathrm{comm}} = 32/3.4594 \approx 9.25\times$.

Because off-chip movement is widely reported to dominate accelerator energy budgets, even a modest per-bit reduction in moved volume can dominate the on-chip arithmetic savings of Section 4.2; we quantify this trade-off as a labeled projection in Section 5.3.

### 4.4 Digit-serial scheduling and the $O(k^2)$ claim

The conjecture in the grounding block states $O(k^2)$ energy scaling. Our model actually gives $O(k)$ per MAC ($E_{\mathrm{p}}(k) = k a b^2$), because a digit-serial multiplier with one digit slice per cycle does $k$ units of work. The $O(k^2)$ bound arises only if each digit slice must combine all previously produced partial products (a schoolbook $k \times k$ digit multiplication evaluated in one shot). The pipelined digit-serial schedule is therefore strictly better than the conjectured bound:

$$E_{\mathrm{p}}^{\mathrm{pipe}}(k) = k \, a b^2 = O(k) \subseteq O(k^2).$$

We report this as a strengthening of the original conjecture under the pipelining assumption, and note that carry-chaining between digit slices (needed for multiplication, where digit $i$ of the product depends on carries from all $j < i$ slices) may reintroduce a factor of $k$ in latency, though not necessarily in energy, since a carry-save representation defers carry propagation.

## 5. Results

All numbers in this section are either computed in Section 4 (marked **[computed]**) or are projections under explicitly stated assumptions (marked **[projection]**). No empirical measurements are reported.

### 5.1 Energy model results **[computed]**

| Quantity | Value |
|---|---|
| $a_{45}$ | $3.61328125 \times 10^{-3}$ pJ/bit$^2$ |
| $a_{7}$ | $8.7890625 \times 10^{-4}$ pJ/bit$^2$ |
| Crossover $k^*$, $p=2$ | $1024$ digits |
| Crossover $k^*$, $p=4$ | $256$ digits |
| Crossover $k^*$, $p=16$ | $64$ digits |
| $R(10)$, $p=2$ | $9.765625 \times 10^{-3}$ (saving $102.4\times$) |
| $R(3)$, $p=4$ | $1.171875 \times 10^{-2}$ (saving $\approx 85.33\times$) |
| $R(1)$, $p=2$ | $9.765625 \times 10^{-4}$ (saving $1024\times$) |
| $S_{\mathrm{comm}}$, $p=2$, $k=10$ (linear) | $3.2\times$ |
| $S_{\mathrm{comm}}$, $p=2$, $k=3$ (linear) | $\approx 10.67\times$ |
| $S_{\mathrm{comm}}$, $p=2$, $k=10$ (log variant) | $\approx 9.25\times$ |

The headline structural result: under quadratic bit-scaling, the p-adic/float energy ratio $R(k) = k b^2 / n^2$ is independent of technology node, and the crossover precision $k^* = n^2/b^2$ is likewise node-independent. Technology scaling shrinks both sides proportionally; the *architectural* advantage is a property of the number system, not the process node.

### 5.2 Workload projection: neural-network inference **[projection]**

Assumptions (all stated): (i) an inference workload of $M = 10^9$ MACs (order of a small convnet on one image batch — a workload-size assumption, not a measurement); (ii) required precision is heterogeneous, with the distribution $k_j \in \{1, 3, 10\}$ at frequencies $0.5, 0.3, 0.2$ respectively (a hypothesized precision-demand profile motivated by the ultrametric embedding of data in [2], not measured); (iii) $p = 2$, $b = 1$, 45 nm calibration.

Mean precision:

$$\bar{k} = 0.5 \times 1 + 0.3 \times 3 + 0.2 \times 10 = 0.5 + 0.9 + 2.0 = 3.4.$$

Workload energy ratio:

$$R_{\mathrm{work}} = \frac{\bar{k}}{n^2} = \frac{3.4}{1024} = 3.3203125 \times 10^{-3}.$$

Total energies:

$$E_{\mathrm{FP}}^{\mathrm{tot}} = 10^9 \times 3.7 \ \text{pJ} = 3.7 \ \text{J},$$

$$E_{\mathrm{p}}^{\mathrm{tot}} = 3.3203125 \times 10^{-3} \times 3.7 \ \text{J} = 1.228515625 \times 10^{-2} \ \text{J} \approx 12.29 \ \text{mJ}.$$

Projected saving: $\approx 301.5\times$ on on-chip arithmetic energy ($1/3.3203125 \times 10^{-3} = 301.511...$; precisely $1024/3.4 \approx 301.18$ — we report $1024/3.4 = 301.1765\times$, correcting the rounding above). The uncertainty on this projection is dominated entirely by assumption (ii); if the true mean precision is $\bar{k} = 10$, the saving drops to $102.4\times$; if $\bar{k} = 30$, it drops to $34.13\times$ ($1024/30 = 34.1333$). The saving remains above $10\times$ for any $\bar{k} < 102.4$.

### 5.3 Off-chip dominance projection **[projection]**

Assume (stated as an assumption, not a measurement) that off-chip movement costs $E_{\mathrm{bit}}^{\mathrm{off}}$ per bit and that a workload moves $10^{10}$ bits per inference at full word width. Flat communication energy is $10^{10} E_{\mathrm{bit}}^{\mathrm{off}}$; the tree-linear variant at mean precision $\bar{k} = 3.4$, $b=1$ moves $3.4 \times 10^{10}/32 \approx 1.0625 \times 10^9$ bits-equivalent... more precisely, the per-value volume falls from $32$ bits to $b\bar{k} = 3.4$ bits, a $32/3.4 \approx 9.41\times$ reduction in moved bits. If off-chip energy is even $5\times$ the on-chip arithmetic energy (a commonly assumed dominance regime, stated here as an assumption), the combined system saving is bounded between the arithmetic-only saving ($301.18\times$) and the communication-limited saving ($9.41\times$); the p-adic advantage in the communication-dominated regime is therefore real but far smaller than the arithmetic-regime advantage, and the logarithmic tree-navigation variant (Section 4.3) would raise the communication saving toward $9.25\times$ at $k=10$ per value — comparable to the linear variant at low $k$, diverging only at large $k$.

## 6. Discussion

**Limitations of the energy model.** The quadratic scaling $e_{\mathrm{MAC}}(b) = a b^2$ is a coarse model. Real multipliers exhibit near-linear scaling in the Booth-encoded regime at small widths, and clock/power delivery overheads are fixed per operation regardless of width; both effects *hurt* the p-adic side at small $k$, because a digit slice has per-slice overhead that our model sets to zero. If per-slice overhead is $e_0$, the model becomes $E_{\mathrm{p}}(k) = k(e_0 + a b^2)$ and the crossover becomes $k^* = n^2 a / (e_0 + a b^2)$, which can fall below practical precisions. Measuring $e_0$ is the single most important empirical task for this program.

**The calibration identification is the weakest link.** We identified a float MAC with a 32-bit fixed-point MAC to extract $a$. A float MAC includes normalization, exponent handling, and rounding that a fixed-point unit lacks; if the true effective width is $n_{\mathrm{eff}} < 32$, then $a$ rises and $k^* = n_{\mathrm{eff}}^2/b^2$ falls. For example, at $n_{\mathrm{eff}} = 16$: $k^* = 256$ for $p=2$ — still comfortably above practical precision, but the margin narrows. Conversely, if float overhead makes the effective width larger, our savings are *underestimated*. The direction of the bias from float-specific overhead is therefore in our favor, but the quadratic-model bias is not.

**What would falsify the conjecture.** Three results would falsify Conjecture 1 or sharply limit it: (1) a demonstration that digit-slice overhead $e_0$ dominates $a b^2$ for all $b \ge 1$, collapsing the per-digit cost to a constant comparable to a full float MAC; (2) a demonstration that real workloads (measured, not hypothesized) require uniformly high precision $\bar{k} \gtrsim k^*$, removing the early-termination advantage; (3) a demonstration that p-adic results cannot be consumed downstream without conversion to Archimedean form, with the conversion costing more than the arithmetic saved. Point (3) is the most dangerous: the ultrametric and Archimedean topologies are genuinely different, and any system that must round-trip through floats forfeits the advantage at the boundary. The program therefore only closes if entire pipelines — not single kernels — live in $\mathbb{Q}_p$.

**Failure modes of the workload assumption.** Our precision-demand profile (frequencies $0.5/0.3/0.2$ over $k \in \{1,3,10\}$) is a hypothesis motivated by the ultrametric data embeddings of [2] and the small-prime natural digit structures of [8], not a measurement. If precision demand is heavy-tailed (a few operands needing hundreds of digits), the mean $\bar{k}$ rises and the saving degrades gracefully but the tail operands may dominate energy, requiring hybrid precision routing — which reintroduces Archimedean-style multi-width hardware.

**Off-chip analysis is the least developed component.** We treated $E_{\mathrm{bit}}^{\mathrm{off}}$ as a free parameter and the tree-navigation volume as two labeled variants. The logarithmic variant rests on an unproven assumption about stopping-depth distributions; a real analysis needs the Markov-process machinery of [3] applied to digit-tree traversal, which we flag as the natural next step. Moreover, if off-chip traffic is dominated by *weights* rather than activations, and weights are stored once in full precision, the per-inference communication saving shrinks toward the activation-only fraction of traffic.

**Open questions.** (1) What is the exact carry-management energy of digit-serial p-adic multiplication, and does carry-save deferral keep it $O(k)$? (2) Does there exist a natural workload class whose precision distribution is provably bounded (e.g., via ultrametric concentration results of the kind in [3] and [6])? (3) Can the adelic perspective of [11] — combining local p-adic computations with a global Archimedean consistency check — bound the required precision a priori? (4) Do the recursive-structure techniques of [5] transfer to scheduling analysis on digit trees? (5) Can the discovery-workflow principles of [9] and the synthesis framing of [12] be operationalized as an automated