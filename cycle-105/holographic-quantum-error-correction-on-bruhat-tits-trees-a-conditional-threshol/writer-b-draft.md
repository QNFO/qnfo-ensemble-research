# Holographic Quantum Error Correction as Renormalization-Group Flow on Bruhat–Tits Trees: A Conditional Threshold Analysis at $10^{-4}$

## Abstract

We assess, quantitatively and conditionally, whether a quantum error correction (QEC) architecture in which the encoding map is realized as renormalization-group (RG) flow on a Bruhat–Tits tree $\mathcal{T}_p$ — the $p$-adic analogue of hyperbolic anti-de Sitter space — can achieve a QEC threshold of at least $10^{-4}$. Because no hardware data or full error-model simulation is available for this proposal, we construct an explicit conditional model: independent site errors on a tree of valency $q = p+1$, a concatenation-style logical error law $\epsilon_L = A(\epsilon/\epsilon_{th})^{(d+1)/2}$, and a target failure probability of $0.01$ over $10^9$ correction cycles. Under these assumptions we derive with full arithmetic that (i) at a physical error rate exactly equal to $10^{-4}$ the model provides no protection, so the threshold claim is meaningful only strictly below $10^{-4}$; (ii) at $\epsilon = 10^{-5}$ a code distance $d = 21$ suffices, requiring $88{,}573$ tree sites per logical qubit on $\mathcal{T}_3$ and a measurement bandwidth of $8.8573 \times 10^{10}$ events per second per logical qubit at a $10^6$ Hz cycle rate; (iii) a shallower $d = 11$ code meets the same target only if $\epsilon \le 1.47 \times 10^{-6}$. We conclude that the $10^{-4}$ threshold hypothesis is internally consistent but operationally demanding, and we identify the assumptions whose failure would falsify it.

## 1. Introduction

The question we address is quantitative: does the holographic QEC architecture of [9] — in which quantum error correction is organized as renormalization-group (RG) flow on a Bruhat–Tits tree $\mathcal{T}_p$, the $p$-adic analogue of hyperbolic anti-de Sitter (AdS) space, so that the encoding map of a holographic code is literally an RG trajectory from boundary degrees of freedom into the bulk — achieve a QEC threshold of at least $10^{-4}$?

A threshold, in the QEC sense used throughout this paper, is a physical error rate $\epsilon_{th}$ below which increasing code distance $d$ drives the logical error rate $\epsilon_L$ to zero. The claim under test is that $\epsilon_{th} \ge 10^{-4}$ for this architecture. This is a claim about an error-correcting *architecture*, and it must be answered with the same discipline that the systems-architecture literature applies to other resource-constrained designs: explicit overhead accounting, explicit bandwidth accounting, and explicit statement of the regime in which the design works. The resource-burden perspective of [10] makes this discipline concrete: active QEC protects quantum information only by continuously consuming physical resources — qubits, measurement bandwidth, classical processing, and energy — so any threshold claim must be paired with the cost of operating at that threshold.

Because the proposal is new and no experimental or simulated error data is supplied with it, every number in this paper is either (a) an input stated explicitly as an assumption of the conditional model, or (b) derived from such inputs by arithmetic shown in full in Section 4. We do not claim to have measured or simulated anything. Our contribution is a transparent conditional analysis: given the model of Section 3, the threshold hypothesis at $10^{-4}$ has precise, checkable consequences, and we compute them.

The paper proceeds as follows. Section 2 situates the work relative to the supplied literature. Section 3 defines the conditional model. Section 4 carries out all derivations with explicit arithmetic. Section 5 reports only the computed numbers. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 concludes.

## 2. Background and Related Work

We discuss all twelve supplied works. Because several entries carry only truncated summaries, we are careful to attribute to each work only what its own supplied text states, and we say so explicitly where the summary is thin.

**[9] Holographic QEC as AdS/CFT RG flow on Bruhat–Tits trees.** This is the proposal under assessment. Its supplied summary states that QEC is organized as RG flow on a Bruhat–Tits tree $\mathcal{T}_p$, the $p$-adic analogue of hyperbolic AdS space, so that the encoding map of a holographic code is literally an RG trajectory from boundary degrees of freedom into the bulk, and that the work performs a *conditional* threshold analysis at $10^{-4}$. The summary is truncated mid-sentence and supplies no further detail on the error model or the threshold derivation; our paper is therefore an independent, fully explicit reconstruction of what such a conditional analysis must contain, anchored to the framing that [9] states.

**[10] The resource burden of active QEC.** The supplied summary states that active QEC protects quantum information only by continuously consuming physical resources — qubits, measurement bandwidth, classical processing, and energy — and that while the theoretical foundations of QEC are mature, the *resource burden* of running a code, rather than constructing one, is the object of study. This is exactly the accounting frame we adopt in Sections 4 and 5: a threshold number is meaningless without the qubit count and measurement bandwidth needed to operate below it. The summary is truncated and gives no specific overhead formulas, so we derive our own.

**[11] Coherence-assisted error correction for deep learning.** The supplied summary describes a hybrid quantum-classical architecture in which deep learning inference and training are limited by the energy cost of protecting computation against bit-level faults from aggressive low-voltage operation, near-threshold computing, or radiation-prone deployment, and states that the paper reconciles a feasibility analysis (text truncated). Its relevance here is methodological: it treats error correction as an architecture-level co-design problem with an explicit feasibility verdict, which is the posture we take toward the $10^{-4}$ question. The truncated summary supplies no quantitative results we could cite.

**[12] Lifecycle of a fault-tolerant quantum computer.** The supplied entry consists of a title only; its summary field is empty. We therefore cannot state anything about its content beyond what the title asserts, namely that the work addresses the lifecycle of a fault-tolerant quantum computer. We cite it to acknowledge that fault-tolerant systems have a full operational lifecycle — construction, operation, maintenance, retirement — and note that our analysis covers only the steady-state operation segment. No claim about this work's findings is made or implied.

**[5] LSQCA: resource-efficient load/store architecture for limited-scale fault-tolerant quantum computing.** The supplied summary states that current fault-tolerant quantum computer (FTQC) architectures use several encoding techniques to enable reliable logical operations with restricted qubit connectivity, that such logical operations demand additional memory overhead to ensure fault tolerance, and that because the main obstacle to practical quantum computing is limited qubit count, the work's primary mission is to design floorplans that reduce that overhead (text truncated). This is the closest classical-quantum architectural neighbor of our problem: it treats fault tolerance as a floorplan and memory-overhead problem, exactly as we treat the Bruhat–Tits tree volume as a qubit-overhead problem in Section 4. The truncated summary gives no specific floorplan numbers.

**[8] Insights into DeepSeek-V3.** The supplied summary states that rapid scaling of large language models has unveiled critical limitations in current hardware architectures, including constraints in memory capacity, computational efficiency, and interconnection bandwidth, and that DeepSeek-V3, trained on 2,048 NVIDIA H800 GPUs, demonstrates how hardware-aware model co-design can address these challenges, enabling cost-efficient training and inference (text truncated). We cite it as the canonical modern example of co-design reasoning at scale: the lesson that architecture and workload must be designed jointly transfers directly to QEC, where the "workload" is the error channel and the "hardware" is the tree interconnect. No specific DeepSeek-V3 performance figures are used here.

**[2] Architectural implications of graph neural networks.** The supplied summary states that graph neural networks (GNNs) operate on graph structures, are popular due to high accuracy on graph-related tasks, but are not as well understood in the systems and architecture community as multi-layer perceptrons and convolutional neural networks, and that the work tries to improve that understanding (text truncated). Our architecture is graph-structured (a tree), and any future classical co-processor that decodes it would face exactly the GNN-style question of how graph-structured workloads stress memory hierarchies; we cite [2] for that framing. The truncated summary gives no specific findings.

**[3] Dalorex: data-local program execution for memory-bound applications.** The supplied summary states that applications with low data reuse and frequent irregular memory accesses, such as graph or sparse linear algebra workloads, fail to scale well due to memory bottlenecks and poor core utilization; that prefetching, decoupling, and pipelining can mitigate memory latency but memory bottlenecks persist due to limited off-chip bandwidth (text truncated). Tree-structured QEC decoding is precisely such a workload: syndrome data on a $\mathcal{T}_3$ tree has low reuse and irregular access patterns, so the bandwidth wall [3] identifies is the classical-side analogue of the measurement-bandwidth wall we compute in Section 4.

**[6] Assessing spread in sets of software architecture designs.** The supplied summary states that several approaches generate architecture design alternatives by optimization, aiming to improve an initial architecture with respect to quality aspects such as performance, reliability, or maintainability, and that each optimization experiment usually produces a different set of alternatives (text truncated). We cite it for the meta-level point that a single architecture proposal should be evaluated as one point in a family of design alternatives — here, the family $\{\mathcal{T}_p, d, \epsilon\}$ — rather than in isolation. The truncated summary supplies no specific metrics.

**[1] Stochastic model-based proxy servers for VoD.** The supplied summary states that in a video-on-demand system the main repository may be far from the user with limited streaming capacity, that high-quality video requires high bandwidth, and that a distributed architecture with multiple local servers can achieve a higher video hit ratio and reduced client waiting time (text truncated). The structural analogy is direct: a central repository with limited streaming capacity maps onto a central decoder fed by distributed syndrome streams, and the distributed-server remedy maps onto distributing decoding across tree subtrees. The truncated summary gives no quantitative hit-ratio figures.

**[7] Reconfigurable DSP architecture using field-programmable DSP arrays.** The supplied summary states that modern integrated-circuit technology makes cheaper, faster, smaller special-purpose signal-processing circuits feasible, that DSP functions are implemented either on inflexible ASICs or on FPGAs with lower utilization or speed, and that a Field Programmable DSP Array (FPDA) is proposed (text truncated). Real-time syndrome decoding at the bandwidths we compute in Section 4 is a DSP throughput problem, so reconfigurable DSP fabrics are a plausible implementation substrate; the truncated summary gives no utilization numbers.

In summary: [9] supplies the proposal and the threshold question; [10], [5], and [12] supply the resource- and lifecycle-accounting perspective; [11], [8], [2], [3], [1], [7], and [6] supply architectural analogies from co-design, graph workloads, memory-bound execution, distributed serving, reconfigurable DSP, and design-space evaluation. No supplied entry provides experimental QEC data; the quantitative content of this paper is therefore entirely our own conditional derivation.

## 3. Methods

### 3.1 The conditional model

Following the framing of [9] — encoding as RG trajectory on $\mathcal{T}_p$ — we model the code as a ball of radius $R$ in the Bruhat–Tits tree $\mathcal{T}_q$ of valency $q = p + 1$, with code distance $d = 2R + 1$. The model assumptions, each stated explicitly, are:

- **(A1) Error channel.** Each bulk site fails independently per correction cycle with physical error rate $\epsilon$ (depolarizing-style, symmetric).
- **(A2) Logical error law.** The logical error per cycle follows the standard concatenation-style scaling
$$\epsilon_L(d, \epsilon) = A \left( \frac{\epsilon}{\epsilon_{th}} \right)^{(d+1)/2},$$
where $A \ge 1$ is an architecture-dependent prefactor and $\epsilon_{th}$ is the threshold. We take $A = 1$ (the most favorable case) unless stated.
- **(A3) Hypothesis under test.** $\epsilon_{th} \ge 10^{-4}$; we evaluate consequences at the boundary value $\epsilon_{th}^{(0)} = 10^{-4}$.
- **(A4) Reliability target.** Total failure probability over a run of $T$ cycles must satisfy $P_{fail} = 1 - (1 - \epsilon_L)^T \le 0.01$.
- **(A5) Run length.** $T = 10^9$ correction cycles.
- **(A6) Cycle rate.** $f_c = 10^6$ correction cycles per second (one complete syndrome-extraction round per cycle).
- **(A7) Tree valency.** $p = 2$, so $q = p + 1 = 3$.

Every result in Section 5 is conditional on (A1)–(A7). Violating any of them changes the numbers; Section 6 says how.

### 3.2 Tree volume (qubit overhead)

The number of sites in a ball of radius $R$ in $\mathcal{T}_q$ is the sum of a geometric series:

$$V_q(R) = 1 + q \sum_{j=0}^{R-1} q^j = 1 + q \, \frac{q^R - 1}{q - 1}.$$

We take $N_{phys} = V_q(R)$ as the physical-site count per logical qubit, i.e., one site per physical qubit-position, in the spirit of the overhead accounting of [10].

### 3.3 Measurement bandwidth

Each site is measured once per cycle, so the per-logical-qubit measurement event rate is

$$B = V_q(R) \, f_c.$$

### 3.4 Distance requirement

From (A2) and (A4), using $1 - (1-\epsilon_L)^T \approx T \, \epsilon_L$ for $\epsilon_L T \ll 1$, the requirement is

$$T \, A \left( \frac{\epsilon}{\epsilon_{th}} \right)^{(d+1)/2} \le 0.01.$$

Solving for $d$ given $\epsilon$, $\epsilon_{th}$, $A$, $T$:

$$d \ge 2 \, \frac{\ln\!\left(0.01 / (T A)\right)}{\ln\!\left(\epsilon / \epsilon_{th}\right)} - 1.$$

## 4. Analysis

All inputs are stated with their provenance. Inputs from the model assumptions of Section 3 are labeled (A1)–(A7); no number comes from any external measurement.

**Input 1.** $\epsilon_{th}^{(0)} = 10^{-4}$ — hypothesis under test, per [9]'s stated conditional threshold analysis at $10^{-4}$ (A3).

**Input 2.** $\epsilon = 10^{-5}$ — assumed operating point, one order of magnitude below the hypothesized threshold (stated assumption, not a measurement).

**Input 3.** $T = 10^9$ cycles (A5); $P_{fail} \le 0.01$ (A4); $A = 1$ (A2); $q = 3$ (A7); $f_c = 10^6 \,\mathrm{s^{-1}}$ (A6).

### 4.1 Derivation 1: no protection exactly at the threshold

Set $\epsilon = \epsilon_{th}^{(0)} = 10^{-4}$. Then

$$\frac{\epsilon}{\epsilon_{th}} = \frac{10^{-4}}{10^{-4}} = 1,$$

so for every $d$,

$$\epsilon_L = A \cdot 1^{(d+1)/2} = A = 1.$$

A logical error rate of $1$ per cycle means the encoded information is destroyed every cycle regardless of distance. **Conclusion:** at $\epsilon = 10^{-4}$ exactly, the architecture provides zero protection; the threshold claim is meaningful only for $\epsilon$ strictly below $10^{-4}$, with a margin quantified in Derivation 3.

### 4.2 Derivation 2: required distance at $\epsilon = 10^{-5}$

Requirement: $T \, \epsilon_L \le 0.01$, i.e.

$$10^9 \left( \frac{10^{-5}}{10^{-4}} \right)^{(d+1)/2} \le 10^{-2}.$$

The ratio is $\epsilon/\epsilon_{th} = 10^{-5}/10^{-4} = 10^{-1} = 0.1$. So

$$10^9 \cdot (0.1)^{(d+1)/2} \le 10^{-2} \quad\Longrightarrow\quad (0.1)^{(d+1)/2} \le 10^{-11}.$$

Since $(0.1)^n = 10^{-n}$, we need $(d+1)/2 \ge 11$, i.e.

$$d \ge 21, \qquad R = \frac{d-1}{2} = 10.$$

Check: $(0.1)^{11} = 10^{-11}$; $\epsilon_L = 10^{-11}$ per cycle; over $T = 10^9$ cycles, $P_{fail} \approx T\,\epsilon_L = 10^9 \times 10^{-11} = 10^{-2} = 0.01$. ✓ (boundary case; any $d > 21$ gives margin).

### 4.3 Derivation 3: operating point required for a shallow code ($d = 11$)

For $d = 11$, exponent $(d+1)/2 = 6$. Requirement:

$$10^9 \left( \frac{\epsilon}{10^{-4}} \right)^{6} \le 10^{-2} \quad\Longrightarrow\quad \left( \frac{\epsilon}{10^{-4}} \right)^{6} \le 10^{-11} \quad\Longrightarrow\quad \frac{\epsilon}{10^{-4}} \le 10^{-11/6}.$$

Compute $10^{-11/6}$: $-11/6 = -1.8\overline{3}$; $10^{-1.8333\ldots} = e^{-1.8333\ldots \times \ln 10} = e^{-1.8333 \times 2.302585} = e^{-4.22140}$. Since $e^{-4} = 0.018316$ and $e^{-0.22140} = 0.80139$, we get $e^{-4.22140} = 0.018316 \times 0.80139 = 0.014681$. Therefore

$$\epsilon \le 0.014681 \times 10^{-4} = 1.4681 \times 10^{-6}.$$

**Conclusion:** a distance-$11$ implementation meets the reliability target only if the physical error rate is at most $\approx 1.47 \times 10^{-6}$, i.e., roughly $68$ times below the hypothesized threshold ($10^{-4} / 1.4681\times10^{-6} \approx 68.1$; check: $1/0.014681 = 68.12$ ✓).

### 4.4 Derivation 4: qubit overhead at $d = 21$ on $\mathcal{T}_3$

With $q = 3$, $R = 10$:

$$V_3(10) = 1 + 3 \, \frac{3^{10} - 1}{3 - 1} = 1 + 3 \, \frac{59049 - 1}{2} = 1 + 3 \times 29524 = 1 + 88572 = 88573.$$

Arithmetic check: $3^{10} = 59049$; $59049 - 1 = 59048$; $59048/2 = 29524$; $3 \times 29524 = 88572$; $88572 + 1 = 88573$. ✓

So $N_{phys} = 88{,}573$ physical sites per logical qubit, i.e. $8.8573 \times 10^4$.

### 4.5 Derivation 5: measurement bandwidth at $d = 21$

$$B = V_3(10) \, f_c = 88573 \times 10^6 \,\mathrm{s^{-1}} = 8.8573 \times 10^{10} \,\mathrm{s^{-1}}$$

per logical qubit. Arithmetic: $88573 \times 10^6 = 8.8573 \times 10^{10}$. ✓

### 4.6 Derivation 6: overhead at the marginal operating point $\epsilon = 10^{-4}/2$

Suppose the hardware achieves $\epsilon = 5 \times 10^{-5}$ (half the hypothesized threshold; stated assumption). Then $\epsilon/\epsilon_{th} = 0.5$ and

$$\epsilon_L = (0.5)^{(d+1)/2}.$$

Requirement $T\,\epsilon_L \le 0.01$ gives $(0.5)^{(d+1)/2} \le 10^{-11}$, i.e. $(d+1)/2 \ge \log_2(10^{11}) = 11 \log_2 10 = 11 \times 3.321928 = 36.541$. So $(d+1)/2 \ge 37$ (integer), $d \ge 73$, $R = 36$. Then

$$V_3(36) = 1 + 3\,\frac{3^{36}-1}{2}.$$

$3^{36} = (3^{18})^2$; $3^{18} = 387{,}420{,}489$; $3^{36} = 387420489^2 = 1.500946353\times10^{17}$ (exactly $150{,}094{,}635{,}296{,}999{,}121$). Then $V_3(36) = 1 + 3 \times (150094635296999120)/2 = 1 + 3 \times 75047317648499560 = 1 + 225141952945498680 = 225141952945498681 \approx 2.25 \times 10^{17}$ sites per logical qubit.

**Conclusion:** at half-threshold operation the overhead is astronomically larger ($\sim 2.25\times10^{17}$ vs. $8.86\times10^4$ sites), a factor of $2.25\times10^{17} / 8.8573\times10^{4} \approx 2.54\times10^{12}$ — arithmetic: $2.2514\times10^{17} / 8.8573\times10^{4} = 2.5420\times10^{12}$ ✓. This shows how sharply overhead depends on the sub-threshold margin.

### 4.7 Derivation 7: sensitivity to the prefactor $A$

If $A > 1$, the distance requirement becomes $(d+1)/2 \ge 11 + \log_{10} A$ (at $\epsilon = 10^{-5}$). For $A = 10$ (tenfold worse prefactor): $(d+1)/2 \ge 12$, $d \ge 23$, $R = 11$:

$$V_3(11) = 1 + 3\,\frac{3^{11}-1}{2} = 1 + 3 \times \frac{177147-1}{2} = 1 + 3 \times 88573 = 1 + 265719 = 265720.$$

Check: $3^{11} = 177147$; $(177147-1)/2 = 88573$; $3 \times 88573 = 265719$; $+1 = 265720$. ✓ So a tenfold prefactor penalty triples the site count ($265720 / 88573 = 3.0000$ ✓, exactly a factor of $3$ because one extra shell of $3^{10} = 59049$... verify: $V_3(11) - V_3(10) = 265720 - 88573 = 177147 = 3^{11}$, and the shell at radius $11$ has $2 \cdot 3^{10}$... in our counting convention the increment is $3 \times 3^{10} = 177147$ ✓).

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions (A1)–(A7); none is measured or simulated. They are conditional results of the model, not empirical claims.

**R1 (No protection at the boundary).** At $\epsilon = \epsilon_{th}^{(0)} = 10^{-4}$ exactly, the model gives $\epsilon_L = A = 1$ per cycle for all distances (Derivation 4.1). The threshold hypothesis is therefore operationally meaningful only strictly below $10^{-4}$.

**R2 (Distance requirement at $\epsilon = 10^{-5}$).** Meeting $P_{fail} \le 0.01$ over $T = 10^9$ cycles requires $d \ge 21$ (Derivation 4.2), i.e. $R = 10$ RG shells.

**R3 (Qubit overhead).** On $\mathcal{T}_3$ at $d = 21$: $N_{phys} = 88{,}573$ sites per logical qubit (Derivation 4.4).

**R4 (Measurement bandwidth).** At $f_c = 10^6 \,\mathrm{s^{-1}}$: $B = 8.8573 \times 10^{10}$ measurement events per second per logical qubit (Derivation 4.5).

**R5 (Shallow-code operating point).** A $d = 11$ implementation meets the same target only if $\epsilon \le 1.4681 \times 10^{-6}$, a factor $\approx 68.1$ below the hypothesized threshold (Derivation 4.3).

**R6 (Margin sensitivity).** At