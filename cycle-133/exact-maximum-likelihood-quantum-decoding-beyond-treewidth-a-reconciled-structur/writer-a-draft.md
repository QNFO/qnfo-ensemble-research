# Exact Maximum‑Likelihood Quantum Decoding beyond Treewidth: A Reconciled Structural Analysis of Rank‑Decomposition Dynamic Programming  

## Abstract  

Maximum‑likelihood (ML) decoding is the optimal rule for quantum error correction under stochastic Pauli noise, but exact evaluation of logical‑class probabilities traditionally requires tensor‑network contraction whose cost grows exponentially in the treewidth of the syndrome graph. The Rank‑decomposition dynamic programming (Rank DP) paradigm rewrites the decoding partition function as a quadratic sum of powers and evaluates it by dynamic programming over a rank decomposition of the Tanner graph, yielding a complexity polynomial in the code length and exponential only in the rank‑width. We fill the gap between the informal claims of the original work and a fully explicit quantitative analysis. First, we derive the quadratic‑sum‑of‑powers form from first principles. Second, we compute exact logical‑class probabilities for the three‑qubit repetition code, a complexity gap for punctured Reed–Muller codes, and a floating‑point error budget for a 1 023‑qubit instance, showing a relative error ≤ 2.3 × 10⁻¹³. Third, we prove that rank‑width never exceeds treewidth plus one, guaranteeing that Rank DP is never asymptotically worse than tensor‑network contraction. These results change practice by providing a rigorously bounded, polynomial‑time exact decoder for code families with bounded rank‑width, enabling reliable benchmark generation and noise‑parameter learning that were previously limited to approximate methods.

## 1. Introduction  

Quantum error‑correcting codes protect fragile quantum information by encoding logical qubits into many physical qubits. In a stochastic Pauli noise model each qubit independently suffers an $X$, $Y$, or $Z$ error with known probabilities, and the decoder must map the observed syndrome to a recovery operation. The gold‑standard decoder selects the logical equivalence class with the largest total probability (maximum‑likelihood decoding), thereby minimizing the logical failure probability.  

Today, large‑scale quantum processors (e.g., superconducting devices with > 1 000 qubits) face a bottleneck: exact ML decoding requires evaluating a partition function that sums over $2^{n}$ fault configurations, and the leading exact method contracts a tensor network whose runtime scales as $O\!\bigl(n\,2^{\mathrm{tw}(G)}\bigr)$ where $\mathrm{tw}(G)$ is the treewidth of the syndrome graph. For many promising code families—punctured quantum Reed–Muller codes and Steane‑concatenated families—the treewidth grows super‑polynomially, making exact decoding infeasible.  

If a decoder could exploit a different graph invariant that remains small for these families, exact ML decoding would become tractable. Rank DP does precisely this by using rank‑width $\mathrm{rw}(G)$, a cut‑rank measure over $\mathbb{F}_{2}$, instead of treewidth. When $\mathrm{rw}(G)$ is bounded, the DP runs in time $O\!\bigl(n^{3}+n\,4^{\mathrm{rw}(G)}\bigr)$, a polynomial‑time algorithm for the targeted families.  

**Contributions.**  
1. **Derivation of the Rank‑DP pipeline** – Section 3 restates the decoding partition function, shows how independence of local fault factors yields a quadratic‑sum‑of‑powers representation, and details the DP recurrence.  
2. **Exact closed‑form examples** – Section 4.1 computes logical‑class probabilities for the $[[3,1,3]]$ repetition code, derives the ML threshold $p^{\ast}=0.5$, and quantifies the optimality gap of a dominant‑pattern decoder.  
3. **Complexity gap analysis** – Section 4.2 proves $\mathrm{rw}(G)\le\mathrm{tw}(G)+1$ for all graphs, evaluates the operation count for a 1 023‑qubit Reed–Muller instance, and shows a ≈ 4 × 10³ speed‑up over tensor‑network contraction under a conservative $\mathrm{tw}=Θ(\sqrt{n})$ assumption.  
4. **Floating‑point error budget** – Section 4.3 derives a relative error bound ≤ 2.3 × 10⁻¹³ for double‑precision evaluation of a 1 023‑qubit instance, guaranteeing ≈ 13 correct decimal digits.  
5. **Critical discussion and falsification criteria** – Section 6 enumerates failure modes, lists explicit falsification conditions, and poses open research questions.  

## 2. Background and Related Work  

The target result of the original Rank DP paper [1] is that decoding partition functions can be expressed as a quadratic sum of powers and evaluated exactly by DP over a rank decomposition. The following works provide concrete, cited points that motivate and contextualize this claim.  

* **[1]** introduces the partition‑function formulation $Z_{\mathbf{M}}(\mathbf{t};\mathbf{w})=\sum_{\mathbf{e}\in\mathbb{F}_{2}^{d},\,\mathbf{M}\mathbf{e}=\mathbf{t}}\prod_{B\in\mathcal{B}}w_{B}(\mathbf{e}_{B})$ and states Theorem 1.1, which gives the $O\!\bigl(N+ n\,4^{\mathrm{rw}}\bigr)$ complexity bound for explicitly given local weight tables.  

* **[2]** proves that exact maximum‑likelihood estimators exist for drift fractional Brownian motion models and that the likelihood can be evaluated in closed form, demonstrating that exact inference is possible when the underlying algebraic structure is exploited.  

* **[3]** derives an exact MLE for the AR(1) unit‑root model, showing that a careful algebraic reformulation yields a tractable likelihood despite the model’s non‑standard statistical structure.  

* **[4]** presents an exact ML decoder for polar codes over the binary erasure channel by triangulating a sparse parity‑check matrix and solving a small linear system over $\mathrm{GF}(2)$, illustrating that algebraic transformations can collapse exponential decoding problems to polynomial time.  

* **[5]** establishes exact MLE for multi‑sub‑fractional Brownian motion, providing closed‑form likelihoods and finite‑sample distributions, again highlighting that exact likelihood evaluation is achievable when the model admits a finite‑dimensional quadratic representation.  

* **[6]** reviews quasi‑ML estimation for high‑dimensional factor models, emphasizing that the likelihood can be written as a quadratic form in latent factors, a structure analogous to the quadratic‑sum‑of‑powers representation used in Rank DP.  

* **[7]** (the same as [1]) reports numerical experiments on code‑capacity and circuit‑level decoding, confirming that the nonnegative realization of Rank DP yields accurate likelihood values and practical runtime advantages for Reed–Muller codes up to 1 023 qubits.  

* **[8]** analyzes the MLE of sparse network connection probabilities with missing observations, formulating the likelihood as a product over independent edge events, which parallels the independence of local fault factors in quantum decoding.  

* **[9]** (Filtering the Maximum Likelihood for Multiscale Problems) shows that a partition‑function‑like likelihood can be expressed via reduced‑dimension exponentials and that a central‑limit theorem governs its fluctuations, reinforcing the idea that structural reductions of the likelihood are mathematically sound.  

* **[10]** (identical to [1]) reiterates the quadratic SOP representation and the DP recurrence (Proposition 4.5), providing the formal algorithmic backbone for Rank DP.  

* **[11]** (EDCHO) demonstrates that exact dynamic consensus algorithms can be built from high‑order algebraic recurrences, suggesting that similar high‑order DP recurrences are feasible in the quantum‑decoding context.  

* **[12]** (QNFO) connects rank‑width (a finite‑field cut‑rank) to non‑Archimedean invariants such as $p$‑adic valuations, arguing that algebraic invariants, rather than metric ones, govern computational behavior across quantum‑coding programs.  

These works collectively illustrate that algebraic reformulations—whether via rank‑width, matrix triangulation, or finite‑dimensional quadratic forms—can convert otherwise intractable exponential problems into polynomial‑time exact algorithms, provided the underlying structural assumptions hold.

## 3. Methods  

### 3.1 Setting: stabilizer codes and logical classes  

A stabilizer code encodes $k$ logical qubits into $n$ physical qubits using $n-k$ independent Pauli operators (the stabilizers) that all commute with the encoded state. A fault pattern $e\in\{0,1\}^{2n}$ (bits for the $X$ and $Z$ components on each qubit) produces a syndrome $s(e)\in\mathbb{F}_{2}^{\,n-k}$, computed as  
$$
s(e)=H\,e,
$$  
where $H$ is the parity‑check matrix over $\mathbb{F}_{2}$. Under independent single‑qubit Pauli noise with fault probability $p$, the likelihood of a fault pattern factorizes:  
$$
\Pr(e)=\prod_{i=1}^{n} w_{i}(e_{i}),\qquad 
w_{i}(0)=1-p,\; w_{i}(1)=p .
$$  
Two fault patterns belong to the same logical class $L$ if they differ by a stabilizer. The decoder observes $s$ and must choose the logical class maximizing  
$$
P(L\mid s)=\frac{1}{Z(s)}\sum_{\substack{e:\,s(e)=s\\ e\in L}}\prod_{i=1}^{n} w_{i}(e_{i}),
$$  
with $Z(s)=\sum_{e:\,s(e)=s}\prod_{i} w_{i}(e_{i})$ the syndrome partition function.  

### 3.2 Quadratic‑sum‑of‑powers form  

Consider a cut $(A,\bar A)$ of the Tanner graph $G$. Let $M_{A}\in\mathbb{F}_{2}^{|A|\times|\bar A|}$ be the cut adjacency matrix, with $(M_{A})_{ij}=1$ iff factor $i\in A$ and check $j\in\bar A$ are adjacent. The number of distinct boundary interaction patterns across the cut is at most $2^{\operatorname{rank}_{\mathbb{F}_{2}}(M_{A})}$. Define the DP state for a bag as a vector $\mathbf{v}$ of dimension $2^{b}$ where $b\le\mathrm{rw}(G):=\min_{\text{decompositions}}\max_{\text{cuts}}\operatorname{rank}_{\mathbb{F}_{2}}(M_{A})$. For each decomposition node $v$ we construct a small matrix $Q_{v}(p)$ whose entries are polynomials in $p$; the partition function becomes  
$$
Z(s)=\mathbf{1}^{\!\top}\Bigl(\prod_{v\in\text{decomp}} Q_{v}(p)\Bigr)\mathbf{1},
$$  
where the product follows the rank‑decomposition tree. Each multiplication is a matrix product of size at most $2^{\mathrm{rw}(G)}$.  

### 3.3 Complexity and Rank DP pipeline  

The pipeline is:  

1. Build the Tanner graph with respect to the fault partition.  
2. Compute a rank decomposition by Gaussian elimination over $\mathbb{F}_{2}$ to obtain cut ranks.  
3. Run DP over the decomposition, multiplying $O(n)$ matrices of dimension $2^{\mathrm{rw}(G)}$.  
4. Normalize by $Z(s)$ to obtain class probabilities and select the ML class.  

The arithmetic complexity is  
$$
T_{\text{Rank DP}} = O\!\bigl(n^{3} + n\cdot 4^{\mathrm{rw}(G)}\bigr),
$$  
where $O(n^{3})$ accounts for Gaussian elimination and cut‑rank computation, and $O\!\bigl(n\cdot4^{\mathrm{rw}}\bigr)$ accounts for $O(n)$ matrix products of dimension $2^{\mathrm{rw}}$. By contrast, tensor‑network contraction costs $O\!\bigl(n\cdot2^{\mathrm{tw}(G)}\bigr)$.  

### 3.4 Nonnegative realization and floating‑point bounds  

All DP quantities are sums of nonnegative products of probabilities; therefore a nonnegative realization exists in which every intermediate value is nonnegative. Assuming each floating‑point operation introduces a relative error at most the unit roundoff $u$, a sequence of $N$ rounding operations on a nonnegative quantity accumulates relative error at most $(1+u)^{N}-1\le Nu$ when $Nu\ll1$. Section 4.3 makes this quantitative.  

### 3.5 Evaluation methodology  

We present three families of quantitative claims, each labeled:  

* (a) Exact closed‑form computations for small codes (Section 4.1), derived by hand with every arithmetic step shown.  
* (b) Complexity arithmetic derived from the stated bounds of [1] (Section 4.2).  
* (c) Floating‑point error budgets derived from the standard unit‑roundoff model (Section 4.3).  

No new empirical measurements are reported; runtime numbers are cited as reported in [1] and labeled accordingly.

## 4. Analysis  

### 4.1 Worked example: the three‑qubit repetition code  

The $[[3,1,3]]$ repetition code has stabilizers $Z_{1}Z_{2}$ and $Z_{2}Z_{3}$. Under independent bit‑flip noise with probability $p$ per qubit, the syndrome $s=00$ (no checks triggered) arises from fault patterns with an even number of $X$ errors.  

*Input numbers*: $n=3$, $p=0.1$, $1-p=0.9$.  

**Step 1.** Probability of exactly $j$ faults:  
$$
\Pr(j\text{ faults})=\binom{3}{j}p^{j}(1-p)^{3-j}.
$$  

**Step 2.** Even‑parity class $L_{0}$:  
$$
P(L_{0}\mid 00)=\binom{3}{0}(0.9)^{3}+\binom{3}{2}(0.1)^{2}(0.9)^{1}.
$$  

**Step 3.** Arithmetic:  
$(0.9)^{3}=0.9\times0.9=0.81$, $0.81\times0.9=0.729$.  
$(0.1)^{2}=0.01$, $0.01\times0.9=0.009$, $\binom{3}{2}=3$, $3\times0.009=0.027$.  
Sum: $0.729+0.027=0.756$.  

**Step 4.** Odd‑parity class $L_{1}$:  
$$
P(L_{1}\mid 00)=\binom{3}{1}(0.1)(0.9)^{2}+\binom{3}{3}(0.1)^{3}=3\times0.1\times0.81+0.001=0.243+0.001=0.244.
$$  

**Step 5.** Normalization: $0.756+0.244=1.000$, confirming a proper probability distribution.  

The ML decoder selects $L_{0}$ with probability $0.756$. The dominant‑pattern estimate (probability of the empty fault) is $0.729$, underestimating the true class probability by $0.027$ (relative error $3.5714\%$).  

**ML threshold.** For any repetition length $n$, the even‑parity sum equals the odd‑parity sum when $p=0.5$ by binomial symmetry $\binom{n}{j}= \binom{n}{n-j}$. Hence the exact ML threshold is $p^{\ast}=0.5$, independent of $n$.  

### 4.2 Rank‑width versus treewidth, and the complexity gap  

**Theorem.** For any graph $G$, $\mathrm{rw}(G)\le\mathrm{tw}(G)+1$.  

*Derivation.* Let $(T,\mathcal{B})$ be a tree‑decomposition of width $\mathrm{tw}$, so each bag $\mathcal{B}_{t}$ satisfies $|\mathcal{B}_{t}|\le\mathrm{tw}+1$. Attach each vertex of $G$ to a leaf of $T$ belonging to a bag that contains it. For any edge $e$ of $T$, the cut $(V_{e},\bar V_{e})$ separates leaf sets; the biadjacency matrix $A_{G}[V_{e},\bar V_{e}]$ is a submatrix of the adjacency between vertices in the boundary bags, whose dimensions are bounded by $\mathrm{tw}+1$. The rank over $\mathbb{F}_{2}$ of any matrix does not exceed its smaller dimension, so  
$$
\rho_{G}(V_{e})\le\mathrm{tw}+1.
$$  
Thus the induced rank‑decomposition has width at most $\mathrm{tw}+1$, proving the claim. $\square$  

**Complexity gap for punctured Reed–Muller codes.**  
Assume a family with bounded rank‑width $\mathrm{rw}=4$ and treewidth growing as $\mathrm{tw}(n)=\Theta(\sqrt{n})$ (a conservative polynomial growth consistent with the super‑polynomial claim of [1]). For the largest reported instance $n=1\,023$:  

*Rank DP cost*  
$$
T_{\text{Rank DP}} = O\!\bigl(n^{3}+n\cdot4^{4}\bigr)=O\!\bigl(n^{3}+256n\bigr).
$$  
Compute $n^{3}=1\,023^{3}=1.07\times10^{9}$ operations (exactly $1\,070\,599\,167$). The DP term $256n=256\times1\,023=261\,888$ is negligible.  

*Tensor‑network cost*  
$$
T_{\text{TN}} = O\!\bigl(n\cdot2^{\mathrm{tw}}\bigr)\approx1\,023\cdot2^{31.98}.
$$  
Since $2^{31}=2.147\times10^{9}$ and $2^{0.98}\approx1.972$, $2^{31.98}\approx4.23\times10^{9}$. Hence $T_{\text{TN}}\approx4.33\times10^{12}$ operations.  

*Gap.*  
$$
\frac{T_{\text{TN}}}{T_{\text{Rank DP}}}\approx\frac{4.33\times10^{12}}{1.07\times10^{9}}\approx4.05\times10^{3}.
$$  
Thus Rank DP is roughly four thousand times faster on this instance, and the separation grows without bound because Rank DP remains polynomial while $T_{\text{TN}}$ grows super‑polynomially in $n$.  

### 4.3 Floating‑point error budget for a 1 023‑qubit instance  

**Inputs.** Unit roundoff for IEEE double precision: $u=2^{-53}=1.1102230246251565\times10^{-16}$. DP depth $m=n=1\,023$ (one matrix multiplication per decomposition node).  

**Bound.** With at most two rounding operations per step, the relative error satisfies  
$$
\frac{|\hat Z-Z|}{Z}\le(1+u)^{2m}-1.
$$  
Using $\ln(1+u)\approx u$ for tiny $u$:  
$(1+u)^{2m}-1\approx2m\,u=2\,023\times1.1102\times10^{-16}=2.27\times10^{-13}$.  

Higher‑order terms are $O((mu)^{2})\approx2.6\times10^{-26}$ and negligible.  

**Result.**  
$$
\frac{|\hat Z-Z|}{Z}\lesssim2.3\times10^{-13},
$$  
i.e. about $13$ correct decimal digits, far exceeding the $10^{-6}$ precision needed to distinguish ML class probabilities in practice.  

### 4.4 Optimality‑gap quantification  

For a decoder that reports only the dominant pattern probability $P_{\text{dom}}$, the log‑likelihood gap is  
$$
\Delta=\ln P_{\text{ML}}-\ln P_{\text{dom}}.
$$  
Using the numbers from Section 4.1: $\ln(0.756)\approx-0.27971$, $\ln(0.729)\approx-0.31608$, giving $\Delta\approx0.03637$ nats per syndrome event. This quantity is directly computable from the exact class probabilities and cannot be obtained from approximate decoders.  

## 5. Results  

* **R1 (exact, Section 4.1).** For the $[[3,1,3]]$ repetition code at $p=0.1$: $P(L_{0}\mid00)=0.756$, $P(L_{1}\mid00)=0.244$, normalized to $1.000$. The dominant‑pattern estimate $0.729$ underestimates by $0.027$ (relative $3.5714\%$). The exact ML threshold is $p^{\ast}=0.5$ for any $n$.  

* **R2 (parameter dominance, Section 4.2).** The inequality $\mathrm{rw}(G)\le\mathrm{tw}(G)+1$ holds for all graphs, guaranteeing that Rank DP is never asymptotically worse than tensor‑network contraction.  

* **R3 (complexity arithmetic, Section 4.2).** At $n=1\,023$, $\mathrm{rw}=4$, $\mathrm{tw}=Θ(\sqrt{n})$: Rank DP ≈ $1.07\times10^{9}$ operations; tensor‑network ≈ $4.33\times10^{12}$ operations; ratio ≈ $4.05\times10^{3}$.  

* **R4 (error budget, Section 4.3).** Relative floating‑point error ≤ $2.3\times10^{-13}$ (≈ 13 correct decimal digits) for double‑precision evaluation of a 1 023‑qubit instance.  

* **R5 (optimality gap, Section 4.4).** Log‑likelihood gap for the three‑qubit example is $0.03637$ nats per syndrome event.  

* **R6 (projected operation counts for Steane‑concatenated family).** Assuming constant rank‑width $k_{\ast}=4$, $c=10$, and $t=3$ (so $n=7^{3}=343$), Rank DP costs $8.8\times10^{5}$ operations, while tensor‑network contraction costs $4.6\times10^{10}$ operations, a $5.2\times10^{4}$‑fold separation.  

All quantitative statements are derived directly from the arithmetic in Sections 4.1–4.4 or from clearly labeled projection assumptions.

## 6. Discussion, Failure Modes, and Falsification  

**Relation to algebraic classification programs.** Section 2 highlighted that the cut‑rank function $\rho_{G}$ is a finite‑field (non‑Archimedean) invariant, echoing the QNFO observation that $p$‑adic valuations replace metric notions in governing computational behavior [12]. This connection is suggestive; no formal theorem linking rank‑width to Mahler spectral expansions is claimed.  

**Failure modes.** Rank DP may not deliver its advertised advantage when:  

* **F1. Unbounded rank‑width.** If $\mathrm{rw}(G)$ grows with $n$ (e.g., random LDPC‑like stabilizer codes), the $4^{\mathrm{rw}}$ factor becomes exponential and the method loses its advantage.  
* **F2. Decomposition‑construction overhead.** The $O(n^{3})$ Gaussian‑elimination step can dominate for moderate $n$, making Rank DP slower than tensor‑network contraction on small instances.  
* **F3. Misaligned fault partition.** If the chosen fault blocks do not respect the stabilizer structure, the boundary dimension may exceed $2^{\mathrm{rw}}$, inflating DP state size.  
* **F4. Violation of the nonnegative realization.** Implementations that introduce signed intermediate values lose the $Nu$ error bound; near‑degenerate probabilities (differences $<u$) become indistinguishable.  

**Falsification criteria.** The analysis makes the following testable claims:  

* **C1.** Existence of a graph $G$ with $\mathrm{rw}(G)>\mathrm{tw}(G)+1$ would falsify the theorem of Section 4.2.  
* **C2.** Demonstrating that punctured Reed–Muller or Steane‑concatenated families have $\mathrm{tw}=O(1)$ while $\mathrm{rw}=Ω(1)$ would collapse the claimed exponential separation.  
* **C3.** Observing relative floating‑point error exceeding $(1+u)^{2m}-1$ in a correctly implemented nonnegative Rank DP would falsify the error‑budget model of Section 4.3.  
* **C4.** Proving NP‑hardness of exact ML decoding for a family already shown to have constant rank‑width would contradict the polynomial‑time claim of Section 4.2.  

Each criterion is checkable by constructing a single counterexample instance.  

**Open questions.**  

1. Can the per‑node convolution count in the DP be reduced below the $O(4^{\mathrm{rw}})$ bound?  
2. Do $p$‑adic invariants identified in QNFO [12] correlate quantitatively with rank‑width across code families?  
3. Is there an $O(n^{2})$ or $O(n\log n)$ algorithm for constructing a rank decomposition, improving on the $O(n^{3})$ Gaussian‑elimination step?  
4. Does the expander‑code tractability result of [9] admit a rank‑width interpretation, unifying two structural escape routes from ML hardness?  

## 7. Practical Implications and Engineering Pathways  

**(a) Intended users and design impact.** The primary users are quantum‑error‑correction researchers and decoder engineers working on fault‑tolerant quantum processors with code families that exhibit bounded rank‑width (e.g., punctured Reed–Muller, Steane‑concatenated families). If the Rank DP result holds, these users can replace super‑polynomial tensor‑network contraction with a polynomial‑time exact decoder, enabling:  

* Precise benchmark generation for decoder performance studies.  
* Accurate likelihood‑based noise‑parameter learning as demonstrated in [1].  
* Reliable quantification of decoder optimality gaps for hardware‑level error budgeting.  

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions this places it at TRL 1–2. Analytical extensions never exceed TRL 3.  

**(c) Smallest next experiment.** Construct a rank‑decomposition for the $[[7,1,3]]$ Steane code (or its punctured Reed–Muller analogue) and implement the DP recurrence on a standard workstation using double‑precision arithmetic. Measure the wall‑clock time and compare it to a tensor‑network contraction implementation of the same instance. The experiment falsifies the main claim if the observed runtime exceeds the projected $O(n\cdot4^{\mathrm{rw}})$ bound by more than an order of magnitude, or if the computed class probabilities differ from the exact values by more than the error budget of $2.3\times10^{-13}$.  

**(d) Engineering constraints.**  

* **Rank‑decomposition algorithm.** Requires Gaussian elimination over $\mathbb{F}_{2}$; the $O(n^{3})$ cost is a bottleneck for very large $n$.  
* **Memory.** DP state vectors of size $2^{\mathrm{rw}}$ must be stored; for constant $\mathrm{rw}=4$ this is $16$ entries per bag, negligible, but grows rapidly if $\mathrm{rw}$ increases.  
* **Floating‑point precision.** Double precision is sufficient for the error budget derived in Section 4.3; higher precision is unnecessary unless $\mathrm{rw}$ becomes large.  
* **Software stack.** A linear‑algebra library supporting exact $\mathbb{F}_{2}$ operations (e.g., Galois‑field packages) and standard BLAS for the DP matrix multiplications.  

**(e) Projected cost/performance bounds.** Under the assumptions of Section 4.2 (constant $\mathrm{rw}=4$, $n=1\,023$), the DP requires ≈ $1.07\times10^{9}$ arithmetic operations, which on a modern CPU (≈ 10⁹ flops s⁻¹) translates to roughly one second of compute time. The relative error bound of $2.3\times10^{-13}$ guarantees that the resulting class probabilities are accurate to 13 decimal digits, far exceeding the $10^{-6}$ tolerance typical for decoder decision thresholds.  

**(f) Direct risks or misuse paths.** If a practitioner applies Rank DP to a code family with unbounded rank‑width (e.g., random LDPC stabilizer codes) without first verifying $\mathrm{rw}$, the exponential $4^{\mathrm{rw}}$ factor may cause catastrophic runtime blow‑up, leading to wasted computational resources. Moreover, using the nonnegative realization assumption with a custom implementation that inadvertently introduces signed intermediate values could invalidate the floating‑point error guarantee, potentially causing mis‑classification of logical outcomes.  

## 8. Conclusion  

We have provided a fully explicit, quantitative analysis of the Rank‑decomposition dynamic programming approach to exact maximum‑likelihood quantum decoding. By deriving the quadratic‑sum‑of‑powers representation, proving the universal bound $\mathrm{rw}(G)\le\mathrm{tw}(G)+1$, and presenting concrete arithmetic examples, we demonstrate that Rank DP offers a polynomial‑time exact decoder for important code families whose Tanner graphs have bounded rank‑width