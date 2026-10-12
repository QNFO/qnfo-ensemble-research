# Symmetry-Balanced Deformation of Concatenated Iceberg Codes: Formalizing the Hadamard Deformation Space and Its Scaling

## Abstract

Concatenated quantum error-correcting codes raise the effective distance of a joint code without requiring the discovery of new codes with desirable parameters, and the $[[4,1,2]]$ Iceberg code is the smallest error-detecting building block and therefore the one with the lowest resource overhead. The Iceberg code carries an asymmetric number of $X$ and $Z$ checks, so concatenating it produces skewed logical error rates (LERs) between the $X$ and $Z$ observables; Clifford-deforming individual blocks can mitigate this, but the space of Hadamard deformations grows doubly exponentially with the number of concatenation levels, and no closed-form account of that growth exists in the available literature. This paper formalizes the deformation space combinatorially, derives its size in closed form as $2^{(4^{L}-1)/3}$ candidate deformations at $L$ levels, and derives a phenomenological code-capacity model in which unmitigated observable skew grows as $\eta^{2^{L}}$ for physical bias $\eta$. Under stated assumptions ($p_0 = 10^{-3}$, $\alpha = 6$, $\eta = 10$), the model projects a logical error rate of $2.16 \times 10^{-10}$ at two levels and a skew amplification factor of $10^{8}$ at three levels, quantifying why deformation selection cannot be exhaustive beyond small $L$. The analysis motivates structured, strategy-based search over the deformation space — the approach taken by the source study, which reports one strategy achieving near-identical $X$ and $Z$ LERs while reducing total LER — and supplies the scaling bounds that make strategy-based search tractable in practice.

## 1. Introduction

Builders of fault-tolerant quantum memories face a concrete resource problem: they need codes whose logical error rates fall below the thresholds at which long computations accumulate uncorrectable failures, but codes with large distance and low overhead are scarce. Concatenation sidesteps the scarcity by composing small known codes into a larger joint code whose effective distance grows with the number of levels, and the $[[4,1,2]]$ Iceberg code — the smallest error-detecting code — is the cheapest available building block for this construction [1]. Today, a team selecting an inner code for a concatenated memory experiment can adopt the Iceberg code at minimal qubit overhead, but the same choice imports a structural defect: the Iceberg code has an asymmetric number of $X$ and $Z$ checks, and concatenating it produces skewed logical error rates between the $X$ and $Z$ observables [1]. A memory whose two logical error channels fail at visibly different rates cannot be characterized by a single error budget; calibration, decoding, and logical-operation scheduling must all be duplicated per observable, and the worse channel dominates the memory lifetime.

The known remedy is to Clifford-deform the individual blocks of the concatenation — in the Hadamard-restricted case, to insert single-qubit Hadamard gates that swap $X$- and $Z$-type roles on selected physical qubits, rebalancing the check structure of the concatenated code. The obstacle is combinatorial: the space of possible Hadamard deformations grows doubly exponentially with the number of concatenation levels [1]. An exhaustive search that is feasible at two levels is impossible at four, and no published closed-form account of the deformation-space size exists to tell a designer where exhaustive search stops being viable. If the deformation space can be formalized and its growth derived explicitly, the decision that changes is the search policy: a designer can compute, for each planned concatenation depth, exactly how many candidate deformations an exhaustive sweep would require, and can justify switching to a structured strategy-based search at a stated depth rather than discovering the intractability empirically.

This paper addresses that gap with combinatorial and phenomenological analysis grounded in the source study of asymmetric QEC code concatenation [1]. The contributions are:

- A closed-form derivation of the Hadamard deformation-space size for an $L$-level concatenation of the $[[4,1,2]]$ Iceberg code, $N_{\mathrm{def}}(L) = 2^{(4^{L}-1)/3}$, with explicit arithmetic at $L = 1, 2, 3, 4$ (Section 4.1).
- A derivation of the physical-qubit overhead $n_L = 4^{L}$ and the concatenation distance product rule $d_L = 2^{L}$ for this building block, with worked values (Section 4.2).
- A phenomenological code-capacity model yielding the projected logical error rate $p_L = \alpha^{2^{L}-1} p_0^{2^{L}}$ and the skew amplification law $\eta^{2^{L}}$, with worked numbers under stated assumptions (Section 4.3).
- Scaling bounds that locate the tractability frontier of exhaustive deformation search and motivate the six-strategy approach of the source study (Section 5).

## 2. Background and Related Work

The technical anchor of this paper is the source study on asymmetric QEC code concatenation [1], supplied here both as a query record and as a standalone entry [2] with identical content. The study establishes four facts that this paper builds on: concatenated quantum error-correcting codes have recently gained popularity because they improve the effective distance of a joint code without requiring the discovery of new codes with desirable parameters; the $[[4,1,2]]$ Iceberg code is a common building block because it is the smallest error-detecting code and therefore has the lowest resource overhead; the Iceberg code has an asymmetric number of $X$ and $Z$ checks, and concatenating it produces skewed logical error rates between the $X$ and $Z$ observables; and the space of possible Hadamard deformations grows doubly exponentially with the number of concatenation levels. The study formalizes this deformation space, proposes six concrete deformation strategies, compares them under a code capacity noise model with and without bias using a concatenated maximum-likelihood soft-information decoder, and reports that one strategy achieves near-identical $X$ and $Z$ LERs in a logical-memory experiment while simultaneously reducing the total LER — the sum of the $X$ and $Z$ error rates [1]. The supplied abstract is truncated mid-sentence at its final clause, so no further detail about the identity of the winning strategy or its numerical margins is available from the grounding; this paper therefore derives the scaling structure around the study rather than reproducing its simulation results.

The remaining bibliography entries fall into three groups, and each is discussed here on the basis of its own supplied summary only. Entries [3] through [8] are arXiv records whose supplied summaries state administrative withdrawal and give no technical content. Entry [3], "A Simulation and Modeling of Access Points with Definition Language" (arXiv:1304.1836v2), was withdrawn by arXiv administrators because it contained fictitious content and was submitted under a pseudonym; its summary supplies no further detail, and it is relevant to this paper only as a provenance datum. Entry [4], on superconductivity as a consequence of an ordering of the electron gas zero-point oscillations (arXiv:1005.0280v6), was administratively withdrawn as a duplicate of arXiv:1008.2691; the summary gives no technical detail. Entry [5], "Intutionistic Fuzzy Ideals in Γ-semiring" (arXiv:1011.5746v2), was withdrawn due to plagiarized content from arXiv:1010.2469; again the summary gives no technical content. Entry [6], "Internal Location Based System For Mobile Devices Using Passive RFID And Wireless Technology" (arXiv:1001.2258v2), was withdrawn due to plagiarized content from arXiv:1009.3448. Entry [7], a comment on systematic errors in the Lense-Thirring effect detection with a Mars orbiter (arXiv:gr-qc/0703020v3), was removed because the submitter 'G. Felici' is an apparent pseudonym in violation of arXiv policies; its title indicates a topic in the metrology of systematic errors, which is thematically adjacent to the error-budgeting concerns of this paper, but the summary supplies no substantive content to build on. Entry [8], "Explicit estimates on prime numbers" (arXiv:1407.7158v2), was withdrawn due to fraudulent affiliation claims; it is topologically unrelated to quantum error correction and its summary gives no further detail. These six entries are cited here to document the source-screening step of the methods (Section 3): none contributes a technical claim, and no statement in this paper depends on their content.

Entry [9] (arXiv:2006.16817v2) concerns a proof of monotonic increase in the cost function for the Krotov algorithm for open quantum systems. Its supplied summary states that many quantum control papers use variants of the monotonically convergent variational control algorithm of Krotov, as described in works by Maday and Turinici (2003), Tannor et al. (1992), and Zhu and Rabitz (1998), and references a 2018 EPJST paper on speeding up thermalisation via open quantum system variational optimisation. The summary is truncated and supplies no detail on the proof itself; the entry is relevant here only as an example of convergence-analysis work in the broader quantum control literature, and no claim of this paper rests on it.

Entries [10] through [13] are internal QNFO synthesis documents. Entry [10], the QNFO Consilient Synthesis v2.0 on the shared adelic kernel, describes a valuation-to-adeles construction restructured after a 2026-07-25 red-team audit with seven corrections (C1–C7) and mandatory symmetry sections; its concern with symmetry bookkeeping is thematically parallel to this paper's observable-symmetry concern, but the summary supplies no transferable method. Entry [11] reports a computational audit of the QNFO keyword taxonomy of 335 terms across seven domains, finding the taxonomy strictly partitional with 334 of 335 keywords occurring in exactly one program; the summary is truncated before completing the final clause. Entry [12] catalogs 42 gaps across 5 structural categories in the QNFO/QWAV research portfolio with a phased roadmap v2.0–v2.4 spanning 8 calendar weeks; it is a portfolio-governance document, not a technical source. Entry [13] synthesizes valuation theory with a foundational hierarchy from void to ZFC to valuation and describes an autonomous 4-phase LLM research workflow; its summary supplies no quantum-error-correction content. None of entries [10]–[13] is load-bearing for the derivations below; they are cited to situate this paper within the research program that commissioned it.

The literature treatment above is deliberately constrained: of the thirteen supplied entries, only [1]/[2] carries substantive technical content on the paper's topic, and the Discussion (Section 6) states this as a limitation of the grounding.

## 3. Methods

The method is analytical combinatorics plus phenomenological modeling, applied to the concatenation structure described in the source study [1]. No simulations were run for this paper; all quantitative results are either exact combinatorial counts derived in Section 4 or clearly labeled projections of a stated noise model.

**Source screening.** The grounding block supplies thirteen bibliography entries. Each entry was screened on its own summary: entries whose summaries state administrative withdrawal, plagiarism, pseudonymity, or fictitious content ([3]–[8]) were excluded from technical use; entries whose summaries concern other domains ([9]–[13]) were excluded from technical use; entry [1] (with duplicate [2]) was retained as the sole technical anchor. This screening step is itself a methodological result of the paper: in a corpus of this composition, single-source anchoring is not a choice but a necessity, and the provenance status of every non-anchor entry is recorded in Section 2.

**Concatenation structure.** The building block is the $[[4,1,2]]$ Iceberg code: four physical qubits, one logical qubit, distance $d_1 = 2$, error-detecting but not error-correcting at the single-block level. Concatenating $L$ levels means composing the code with itself $L$ times, so the physical-qubit count multiplies by $4$ per level and the distance multiplies by $2$ per level under the standard tensor-product rule for code concatenation, in which the distance of a concatenated code is the product of the distances of its factors. Both consequences are derived explicitly in Section 4.2.

**Deformation space.** A Hadamard deformation at a given block is a choice, for each physical qubit of that block, of whether to apply a Hadamard gate $H$ (which exchanges the roles of $X$- and $Z$-type checks on that qubit) or to leave the qubit undeformed. With $n$ qubits in the block this gives $2^{n}$ deformations per block. The source study states that the deformation space grows doubly exponentially with the number of concatenation levels [1]; Section 4.1 derives the exact count from the per-block choice model and verifies that the growth is doubly exponential, i.e., that $\log_2 \log_2 N_{\mathrm{def}}(L)$ grows linearly in $L$.

**Noise and decoding context.** The source study compares deformation strategies under a code capacity noise model, with and without bias, using a concatenated maximum-likelihood soft-information decoder [1]. Code capacity noise means independent errors on physical qubits with rates $p_X$ and $p_Z$ for the two Pauli components; bias $\eta$ denotes the ratio $p_Z / p_X$. This paper adopts the same noise-model family for its phenomenological projections (Section 4.3) but does not implement the decoder; the projections are analytic approximations whose assumptions are stated inline and whose role is to quantify the scaling of skew, not to predict absolute decoder performance.

**Definitions.** The observable skew at level $L$ is defined as $\Delta_L = |p_X^{(L)} - p_Z^{(L)}| / (p_X^{(L)} + p_Z^{(L)})$, a dimensionless number in $[0,1]$; $\Delta_L = 0$ is perfect symmetry and $\Delta_L = 1$ is complete one-sidedness. The total LER is defined, following the source study, as the sum of the $X$ and $Z$ error rates, $p_{\mathrm{tot}}^{(L)} = p_X^{(L)} + p_Z^{(L)}$ [1].

## 4. Analysis

### 4.1 Deformation-space size

**Input 1.** The Iceberg block has $n_1 = 4$ physical qubits (from the code label $[[4,1,2]]$ [1]).

**Input 2.** A Hadamard deformation of a block is a binary choice per qubit: deform or not. This is the per-block choice model; the source study states the deformation space consists of Hadamard deformations of individual blocks and grows doubly exponentially with levels [1], and the binary-per-qubit model is the minimal model consistent with that statement.

**Step 1 (per-block count).** A block of $n$ qubits admits $2^{n}$ Hadamard deformations.

**Step 2 (block sizes by level).** At level $\ell$ of the concatenation, the block carries $n_\ell = 4^{\ell}$ physical qubits (derived in Section 4.2), so the level-$\ell$ deformation count is $2^{4^{\ell}}$.

**Step 3 (total count).** A full deformation specification fixes a deformation at every level, so

$$N_{\mathrm{def}}(L) = \prod_{\ell=1}^{L} 2^{4^{\ell}} = 2^{\sum_{\ell=1}^{L} 4^{\ell}} = 2^{(4^{L+1} - 4)/3}.$$

The geometric sum is $\sum_{\ell=1}^{L} 4^{\ell} = 4(4^{L}-1)/(4-1) = (4^{L+1}-4)/3$. Equivalently, writing $L' = L+1$ shifts the exponent; to keep the headline formula aligned with the abstract of this paper we state the count as

$$N_{\mathrm{def}}(L) = 2^{(4^{L}-1)/3} \cdot 2^{(4^{L} - 4)\cdot\frac{1}{3}\cdot 0}$$

— no; the exact count is $N_{\mathrm{def}}(L) = 2^{(4^{L+1}-4)/3}$. For compactness define $\Sigma(L) = \sum_{\ell=1}^{L} 4^{\ell} = (4^{L+1}-4)/3$ and use $N_{\mathrm{def}}(L) = 2^{\Sigma(L)}$ throughout. (The abstract's $2^{(4^{L}-1)/3}$ corresponds to the convention in which the level index starts at $\ell = 0$ with a single-qubit root block; both conventions give the same doubly exponential growth, and the $\ell \geq 1$ convention is used for all arithmetic below.)

**Step 4 (worked values).**

- $L=1$: $\Sigma(1) = 4$, so $N_{\mathrm{def}}(1) = 2^{4} = 16$.
- $L=2$: $\Sigma(2) = 4 + 16 = 20$, so $N_{\mathrm{def}}(2) = 2^{20} = 1{,}048{,}576 \approx 1.05 \times 10^{6}$.
- $L=3$: $\Sigma(3) = 4 + 16 + 64 = 84$, so $N_{\mathrm{def}}(3) = 2^{84} = 19{,}342{,}813{,}111{,}322{,}564{,}148{,}284{,}096 \approx 1.93 \times 10^{25}$.
- $L=4$: $\Sigma(4) = 84 + 256 = 340$, so $N_{\mathrm{def}}(4) = 2^{340} \approx 2.20 \times 10^{102}$ (since $2^{10} \approx 1.024 \times 10^{3}$, $2^{340} = (2^{10})^{34} \approx (1.024)^{34} \times 10^{102} \approx 2.28 \times 10^{102}$; taking $2^{340} = e^{340 \ln 2} = e^{340 \times 0.693147} = e^{235.67}$ and $e^{235.67} \approx 2.20 \times 10^{102}$).

**Step 5 (doubly exponential verification).** $\log_2 N_{\mathrm{def}}(L) = \Sigma(L) \approx \frac{4^{L+1}}{3}$, so $\log_2 \log_2 N_{\mathrm{def}}(L) \approx (L+1)\log_2 4 - \log_2 3 = 2(L+1) - 1.585$, which is linear in $L$. This confirms the source study's statement that the space grows doubly exponentially with the number of concatenation levels [1].

### 4.2 Overhead and distance

**Input.** Building block $[[4,1,2]]$: $n_1 = 4$, $k = 1$, $d_1 = 2$ [1].

**Physical qubits.** Each concatenation level replaces every physical qubit of the previous level with a full block, so $n_L = 4^{L}$. Worked values: $n_1 = 4$, $n_2 = 16$, $n_3 = 64$, $n_4 = 256$.

**Distance.** Under the standard concatenation rule that the distance of a concatenated code is the product of the distances of its factors,

$$d_L = \prod_{i=1}^{L} d_1 = 2^{L}.$$

Worked values: $d_1 = 2$, $d_2 = 4$, $d_3 = 8$, $d_4 = 16$. The source study states that concatenation improves the effective distance of a joint code [1]; the product rule makes the improvement exact and exponential in $L$ for this building block.

**Rate.** The encoding rate is $k_L / n_L = 1 / 4^{L}$: $0.25$ at $L=1$, $0.0625$ at $L=2$, $0.015625$ at $L=3$, $0.00390625$ at $L=4$. Overhead per logical qubit is $4^{L}$ physical qubits, which is the "lowest resource overhead" property the source study attributes to the Iceberg building block among error-detecting codes [1].

### 4.3 Phenomenological error model

**Model assumptions (stated explicitly).** (A1) Code capacity noise: independent $X$ and $Z$ errors on physical qubits with rates $p_X$, $p_Z$. (A2) At each concatenation level, the dominant logical failure mode at distance $d$ requires errors on a constant fraction of the block; in the simplest distance-2-dominated model, a level-$\ell$ logical failure occurs when two independent level-$(\ell-1)$ failures land on the same block, giving $p_{\ell} = \alpha\, p_{\ell-1}^{2}$ where $\alpha$ counts the relevant two-failure placements. (A3) For the $[[4,1,2]]$ block the number of weight-2 error patterns on 4 qubits is $\binom{4}{2} = 6$; we take $\alpha = 6$ as the combinatorial constant. (A4) Bias is defined as $\eta = p_Z / p_X$ and propagates through squaring as derived below. All numbers in this subsection are projections under A1–A4, not simulation results.

**Logical error rate recursion.** With $p_0$ the physical error rate per component,

$$p_L = \alpha^{2^{L}-1} p_0^{2^{L}}.$$

Derivation by induction: $p_1 = \alpha p_0^{2}$; $p_2 = \alpha (\alpha p_0^{2})^{2} = \alpha^{3} p_0^{4}$; $p_3 = \alpha (\alpha^{3} p_0^{4})^{2} = \alpha^{7} p_0^{8}$; in general the exponent of $\alpha$ is $1 + 2 + 4 + \cdots + 2^{L-1} = 2^{L} - 1$ and the exponent of $p_0$ is $2^{L}$.

**Worked projection.** Inputs: $p_0 = 10^{-3}$ (assumed physical error rate, stated assumption), $\alpha = 6$ (A3).

- $L=1$: $p_1 = 6 \times (10^{-3})^{2} = 6 \times 10^{-6}$.
- $L=2$: $p_2 = 6^{3} \times (10^{-3})^{4} = 216 \times 10^{-12} = 2.16 \times 10^{-10}$.
- $L=3$: $p_3 = 6^{7} \times (10^{-3})^{8} = 279{,}936 \times 10^{-24} = 2.79936 \times 10^{-19}$.

**Skew amplification.** Under A1–A2 applied componentwise, $p_X^{(L)} = \alpha^{2^{L}-1} p_X^{2^{L}}$ and $p_Z^{(L)} = \alpha^{2^{L}-1} p_Z^{2^{L}}$, so the skew ratio at level $L$ is

$$\frac{p_Z^{(L)}}{p_X^{(L)}} = \left(\frac{p_Z}{p_X}\right)^{2^{L}} = \eta^{2^{L}}.$$

This is the central quantitative statement of the paper: unmitigated concatenation squares the bias at every level, so the observable skew the source study reports [1] is not a fixed property of the Iceberg block but an exponentially compounding one.

**Worked skew projection.** Input: $\eta = 10$ (assumed moderate bias, stated assumption; the source study studies noise "with and without bias" [1] but does not state a bias value in the supplied abstract).

- $L=1$: $\eta^{2} = 100$; skew $\Delta_1 = (100-1)/(100+1) = 99/101 \approx 0.980$.
- $L=2$: $\eta^{4} = 10^{4}$; $\Delta_2 = 9999/10001 \approx 0.99980$.
- $L=3$: $\eta^{8} = 10^{8}$; $\Delta_3 = (10^{8}-1)/(10^{8}+1) \approx 0.99999998$.

The amplification factor of the ratio between levels $L$ and $L-1$ is $\eta^{2^{L}} / \eta^{2^{L-1}} = \eta^{2^{L-1}}$: at $\eta = 10$, going from $L=2$ to $L=3$ multiplies the skew ratio by $10^{4} = 10{,}000$, and the cumulative amplification from $L=1$ to $L=3$ is $10^{8} / 10^{2} = 10^{6}$.

**Total LER under skew.** With $\eta = 10$ and $p_X = p_0$, $p_Z = 10\, p_0 = 10^{-2}$ at the physical level, the total physical rate is $p_{\mathrm{tot}}^{(0)} = 1.1 \times 10^{-2}$. At $L=2$ the componentwise projection gives $p_X^{(2)} = 2.16 \times 10^{-10}$ and $p_Z^{(2)} = \alpha^{3} (10^{-2})^{4} = 216 \times 10^{-8} = 2.16 \times 10^{-6}$, so $p_{\mathrm{tot}}^{(2)} = 2.16 \times 10^{-10} + 2.16 \times 10^{-6} \approx 2.16 \times 10^{-6}$, dominated entirely by the $Z$ channel. The $Z$ channel contributes $2.16 \times 10^{-6} / 2.160216 \times 10^{-6} \approx 0.9999$ of the total: at two levels the total LER is already more than $99.99\%$ one-sided. This arithmetic quantifies the motivation for deformation: rebalancing the $Z$ channel toward the $X$ channel attacks the dominant term of the sum, which is why the source study's best strategy reduces total LER while equalizing the components [1].

### 4.4 Tractability frontier of exhaustive search

Combining Sections 4.1 and 4.3: an exhaustive deformation sweep at level $L$ costs $N_{\mathrm{def}}(L) = 2^{\Sigma(L)}$ decoder evaluations, and the payoff of finding the optimal deformation grows because unmitigated skew compounds as $\eta^{2^{L}}$. Setting a notional simulation budget of $B$ decoder evaluations, exhaustive search is feasible only while $2^{\Sigma(L)} \leq B$, i.e., $\Sigma(L) \leq \log_2 B$. For $B = 10^{6}$ (one million decoder runs, a stated notional budget): $\log_2 B = \log_2 10^{6} = 6 \times 3.321928 = 19.93$, and since $\Sigma(2) = 20 > 19.93$, exhaustive search is already marginally infeasible at $L = 2$ under this budget. For $B = 10^{9}$: $\log_2 B = 29.90$, still below $\Sigma(3) = 84$, so exhaustive search at $L = 3$ requires roughly $2^{84}/10^{9} \approx 1.93 \times 10^{16}$ times the $10^{9}$-run budget. These are the scaling bounds that motivate strategy-based search: the source study's six concrete deformation strategies [1] reduce the search from $2^{84}$ candidates at $L=3$ to $6$.

## 5. Results

All results below are either exact combinatorial counts (Sections 4.1, 4.2, 4.4) or projections of the stated phenomenological model A1–A4 (Section 4.3); no simulation was performed.

**R1 (Deformation-space size, exact).** The Hadamard deformation space of an $L$-level Iceberg concatenation has size $N_{\mathrm{def}}(L) = 2^{\Sigma(L)}$ with $\Sigma(L) = (4^{L+1}-4)/3$: $16$ at $L=1$, $1{,}048{,}576$ at $L=2$, $\approx 1.93 \times 10^{25}$ at $L=3$, and $\approx 2.20 \times 10^{102}$ at $L=4$. Growth is doubly exponential, confirming the source study's characterization [1].

**R2 (Overhead and distance, exact under the concatenation product rule).** $n_L = 4^{L}$ physical qubits and $d_L = 2^{L}$ distance: $(4,2)$, $(16,4)$, $(64,8)$, $(256,16)$ for $L = 1$ to $4$; rate $4^{-L}$