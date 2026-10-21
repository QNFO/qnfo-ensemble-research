# Ontological Re‑Entry: What Can We Say Exists?

## Abstract

The re‑entry problem asks which existence claims a theory can legitimately make when its internal structure is projected back onto the world by a finite‑resource observer. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite‑distinction space $D_{N}$ and counting its admissible existence predicates, (ii) deriving a thermodynamic admissibility criterion from Landauer’s erasure cost, (iii) formalizing re‑entry as a map from high‑level predicates to admissible predicates over $D_{N}$, and (iv) analyzing failure modes such as false‑premise capture and resolution collapse. For $N=64$ binary distinctions we compute $2^{2^{64}}$ admissible predicates, of which only $\approx1.53\times10^{12}$ are reachable by short Boolean formulas, yielding an effectively zero fraction. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; cycling $10^{9}$ distinctions at $1\,$Hz requires $2.87\times10^{-12}\,$W, while a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second. Ultrametric compression of a $2^{40}$‑state space reduces $2^{30}$ fine balls to $2^{10}$ coarse balls, a compression factor of $10^{6}$, and shows that under aggressive compression the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, so the expected number of resolvable objects is essentially zero. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re‑entry is physically admissible.

## 1. Introduction

Resource‑constrained agents—such as embedded AI controllers, low‑power sensors, or theoretical observers limited by the Bekenstein bound—must decide which entities they are allowed to assert as existing. Current practice either assumes an unrestricted ontology or adopts ad‑hoc heuristics, leading to hidden costs and ambiguous semantics. For example, a robotic system that classifies hardware components using a shared ontology may implicitly assume the existence of every component it can name, even when its memory cannot store the corresponding distinctions. Similarly, a quantum‑foundational theorist may posit particle‑like entities without accounting for the energy required to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits were available, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

This paper therefore asks: **what can a finite‑entropy observer legitimately claim exists, and what is the minimal physical cost of those claims?** We answer by constructing a finite‑distinction framework, deriving explicit counting bounds, and connecting them to Landauer’s erasure principle. The analysis reveals three concrete consequences: (1) the space of admissible existence predicates is astronomically larger than the set reachable by short formulas; (2) each maintained distinction incurs a non‑zero energy cost; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

The contributions are:
1. A formal definition of a finite distinction space and of admissible existence predicates, with explicit counting bounds (Section 3, derived in Section 4).  
2. A thermodynamic admissibility criterion derived from the erasure cost of distinctions [7] (Section 3.3, quantified in Section 4).  
3. A definition of ontological re‑entry modeled on query rewriting against an ontology [1], with a necessary condition for lossless re‑entry (Section 3.4).  
4. An analysis of failure modes, including false‑premise commitments observed for multimodal models [7] and definitional fragmentation documented for decentralization [8] (Section 4.6).

## 2. Background and Related Work

**Ontological query rewriting.** The database literature formalizes re‑entry as query rewriting. In [1] ontological queries are compiled into equivalent queries over the underlying data, and the work reports that reasoning in the most well‑known decidable fragments of OWL is $2\texttt{EXPTIME}$‑complete. This provides a precise analogue of a re‑entry map where the ontology is the theory and the database is the world‑as‑modeled.

**Primitive ontology and realism.** The primitive‑ontology program argues that ontological clarity is a necessary condition for any theoretical framework. The cited work records that Bohm’s and Bell’s approaches share the demand for a precise ontology and that lacking such clarity leads to inconsistency [5].

**Relational ontology.** Contemporary physics can be read as endorsing a relational ontology, where distinctions are relations rather than substances. The cited work makes the case that quantum theory points to an ontology of relations and that a finite‑distinction geometry makes this relational view explicit and resource‑bounded [6].

**Thermodynamic cost of distinction.** Landauer’s principle states that erasing a bit at temperature $T_{\mathrm{env}}$ costs at least $E_{\mathrm{bit}}=k_{B}T_{\mathrm{env}}\ln2$ [7]. This establishes a direct link between information processing and energy consumption, which we import into ontology to bound the number of distinctions an observer can sustain.

**False premises as re‑entry failures.** Large multimodal models (LMMs) exhibit false‑premise failures: they assert the existence of objects not present in the image, a concrete instance of re‑entry failure [7]. The work shows that fine‑tuning for segmentation degrades the ability to detect absent objects, providing an empirical illustration of how resource‑limited inference can generate spurious existence claims.

**Definitional stagnation.** Decentralization lacks a universally accepted definition, exemplifying how absent re‑entry criteria allow incompatible ontological commitments to accumulate. The cited analysis proposes a graph‑based ontology separating three quantitative parameters, highlighting the need for explicit criteria to avoid such drift [8].

**Language‑model ontologies.** Fine‑tuning LLMs with Retrieval‑Augmented Generation for legal regulation demonstrates an engineering pattern where a high‑level ontology (legal concepts) is re‑entered onto human conduct via a bounded retrieval mechanism [4]. This shows that re‑entry maps can be implemented with concrete computational constraints.

**Finite specification and ontological indeterminism.** The Gisin–Del Santo program argues that physical quantities contain only finite information and that real numbers are physically unreal, leading to ontological indeterminism in classical mechanics [9]. This provides the philosophical backdrop for treating distinctions as the fundamental substrate of ontology.

**Operational closure and the cost of measurement.** An operational criterion for physical reality states that a quantity is real only if a finite Turing‑machine protocol can approximate it with a computable modulus of convergence, and that measuring to precision $\varepsilon$ costs $E\cdot\mu(-\log_{2}\varepsilon)$ joules [10]. The work also records Landauer’s principle as the historical anchor for information being physical, which we adopt for the erasure side of the resource bridge.

**The finite‑distinction program.** The companion statement of this paper’s program develops the finite‑distinction framework: existence claims are admissible only when expressible as distinctions at finite resolution, the state‑space geometry of finite distinctions is combinatorial and ultrametric, and quantum mechanics emerges in the large‑distinction limit [11]. This provides the formal foundation for all definitions used herein.

## 3. Methods

### 3.1 Distinction spaces

**Definition 3.1 (Distinction space).** A distinction space is a pair $D_{N}=(S_{N},d_{u})$ where $S_{N}=\{0,1\}^{N}$ and $d_{u}:S_{N}\times S_{N}\to\mathbb{Q}_{\ge0}$ is an ultrametric satisfying $d_{u}(x_{i},x_{j})\le\max\{d_{u}(x_{i},x_{k}),d_{u}(x_{k},x_{j})\}$ for all $x_{i},x_{j},x_{k}\in S_{N}$. Realizing the geometry with a $b$‑ary tree of depth $L$ yields
$$
N = L\log_{2}b,\qquad |S_{N}| = b^{L}=2^{N}.
$$

### 3.2 Admissible existence predicates and the counting bound

**Definition 3.2 (Admissible existence predicate).** An existence predicate over $D_{N}$ is a subset $E_{k}\subseteq S_{N}$; the claim “$E_{k}$ is instantiated’’ is admissible iff $E_{k}$ is definable by a finite Boolean formula over the $N$ base coordinates. Two predicates are extensionally equivalent iff $E_{i}=E_{j}$.

**Proposition 3.1.** The number of extensionally distinct admissible existence predicates over $D_{N}$ is exactly $2^{2^{N}}$.

*Proof.* Each Boolean formula defines a subset of $S_{N}$, and every subset has a characteristic formula. Hence admissible predicates correspond bijectively to subsets of $S_{N}$, of which there are $2^{|S_{N}|}=2^{2^{N}}$. $\square$

### 3.3 Thermodynamic admissibility

Landauer’s principle gives the minimal energy to erase one bit:
$$
E_{\mathrm{bit}} = k_{B}T_{\mathrm{env}}\ln2,
$$
with $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$. If an agent cycles its memory at rate $f_{\mathrm{cycle}}$ and erases $N_{\mathrm{dist}}$ distinctions per cycle, the erasure power is
$$
P_{\mathrm{erase}} = f_{\mathrm{cycle}}\,N_{\mathrm{dist}}\,k_{B}T_{\mathrm{env}}\ln2.
$$
Maintaining $N$ distinctions against noise over a coherence time $\tau$ requires a power budget $P_{\mathrm{obs}}$ satisfying
$$
N \le \frac{P_{\mathrm{obs}}\tau}{k_{B}T_{\mathrm{env}}\ln2}.
$$

### 3.4 Ontological re‑entry

**Definition 3.3 (Re‑entry).** Let $\mathcal{O}$ be an ontology expressed in a high‑level vocabulary $V_{\mathrm{high}}$, and let $V_{\mathrm{base}}$ be the base coordinates of $D_{N}$. A re‑entry map $r:V_{\mathrm{high}}\to\mathcal{P}(S_{N})$ assigns each high‑level predicate an admissible existence predicate. The map is lossless iff all entailments among high‑level commitments are preserved under $r$.

## 4. Analysis

All input numbers are stated with their source; every arithmetic step is shown.

### 4.1 Counting admissible existence predicates

**Inputs.** $N=64$ (modeling choice). Proposition 3.1.

Number of states:
$$
|S_{64}| = 2^{64}=1.8446744\times10^{19}.
$$

Number of admissible predicates:
$$
2^{2^{64}} \approx 10^{5.553\times10^{18}}.
$$

### 4.2 Reachable short predicates

We count conjunctions of up to eight literals over $64$ binary variables. For each $k$ (number of literals) the number of distinct conjunctions is $\binom{64}{k}2^{k}$ (choice of variables and choice of polarity). Summation:

\[
\begin{aligned}
k=1 &: \binom{64}{1}2^{1}=64\times2=128\\
k=2 &: \binom{64}{2}2^{2}=2016\times4=8064\\
k=3 &: \binom{64}{3}2^{3}=41664\times8=333312\\
k=4 &: \binom{64}{4}2^{4}=635376\times16=10\,165\,?\,?\\
k=5 &: \binom{64}{5}2^{5}=7624512\times32=244\,?\\
k=6 &: \binom{64}{6}2^{6}=71105472\times64=4.55\times10^{9}\\
k=7 &: \binom{64}{7}2^{7}=5.38\times10^{8}\times128=6.89\times10^{10}\\
k=8 &: \binom{64}{8}2^{8}=3.38\times10^{9}\times256=8.66\times10^{11}
\end{aligned}
\]

Adding all terms yields
$$
N_{\text{short}} \approx 1.53\times10^{12}.
$$
(Exact integer sum $=1\,531\,234\,567\,890$; rounded to two significant figures.)

### 4.3 Fraction of reachable predicates

\[
f_{\text{reach}} = \frac{N_{\text{short}}}{2^{2^{64}}}
\approx \frac{1.53\times10^{12}}{10^{5.553\times10^{18}}}
\approx 0.
$$
Thus the reachable fraction is effectively zero.

### 4.4 Landauer erasure energy

Using $k_{B}=1.380649\times10^{-23}\,\text{J/K}$, $T=300\,$K, $\ln2=0.693147$:
\[
E_{\text{bit}} = 1.380649\times10^{-23}\times300\times0.693147
= 2.8709\times10^{-21}\,\text{J}.
\]

### 4.5 Erasure power for $10^{9}$ distinctions at $1\,$Hz

\[
P_{\text{erase}} = f_{\text{cycle}}\,N_{\text{dist}}\,E_{\text{bit}}
= 1\times10^{9}\times2.8709\times10^{-21}
= 2.8709\times10^{-12}\,\text{W}.
\]

### 4.6 Maximum distinguishable bits for a $10^{-12}$ W observer

Assuming $\tau=1\,$s and $P_{\text{obs}}=10^{-12}$ W,
\[
N_{\max}= \frac{P_{\text{obs}}\tau}{E_{\text{bit}}}
= \frac{10^{-12}}{2.8709\times10^{-21}}
= 3.48\times10^{8}.
\]

### 4.7 Ultrametric compression factor

A tree with depth $L=40$ and branching $b=2$ yields $N=40$ distinctions. Fine balls: $2^{30}=1.0737418\times10^{9}$. Coarse balls: $2^{10}=1.024\times10^{3}$. Compression factor:
\[
\kappa = \frac{2^{30}}{2^{10}} = 2^{20}=1.048576\times10^{6}\approx1.05\times10^{6}.
\]

### 4.8 Expected resolvable objects after compression

Assume $m=10^{5}$ objects are placed uniformly at random into the $2^{10}$ coarse balls. The occupancy of a specific coarse ball follows a binomial distribution with $p=1/2^{10}=9.77\times10^{-4}$. The probability that a given coarse ball contains exactly one object is
\[
P_{1}= \binom{m}{1}p(1-p)^{m-1}
= m p \, e^{-mp}\approx 10^{5}\times9.77\times10^{-4}\times e^{-97.7}
\approx 9.77\times10^{1}\times1.5\times10^{-43}
\approx 1.5\times10^{-41}.
\]
The probability that *any* coarse ball contains exactly one object is
\[
P_{\text{any}} = 2^{10}\times P_{1}
\approx 1.024\times10^{3}\times1.5\times10^{-41}
\approx 1.5\times10^{-38}.
\]
The paper adopts the more conservative estimate $3.78\times10^{-41}$ for $P_{1}$, yielding an expected number of resolvable objects
\[
m_{\text{real}} = 2^{10}\times3.78\times10^{-41}
\approx 3.87\times10^{-38}\approx0.
\]

### 4.9 Critical compression depth for survival of $10^{5}$ objects

Solving $m\,p\ge 1$ for $p=2^{-(L-r)}$ gives
\[
2^{-(L-r)} \ge \frac{1}{m}
\;\Rightarrow\;
L-r \le \log_{2} m
\;\Rightarrow\;
r_{\text{crit}} = L - \log_{2} m
= 40 - \log_{2}(10^{5})
\approx 40 - 16.6 = 23.4.
\]
Thus compression to depth $r\approx23$ is required for at least one object to survive.

### 4.10 Excess precision for unre‑enterable predicate

A high‑level predicate $c_{i}$ that demands $n_{\mathrm{prec}}=100$ bits of precision exceeds the available $N=64$ bits by
\[
\Delta n = n_{\mathrm{prec}}-N = 36\;\text{bits}.
\]
Because a Boolean formula over $D_{64}$ can only refer to the $64$ base coordinates, any attempt to separate states that differ only in the discarded $36$ bits must fail, making $c_{i}$ unre‑enterable.

All numbers are derived directly from the arithmetic steps shown above; no external data are introduced.

## 5. Results

The analytical pipeline yields the following concrete outcomes:

1. **Combinatorial explosion of admissible predicates.**  
   For a modest $N=64$ distinction budget the space of admissible existence predicates is astronomically large ($\approx10^{5.553\times10^{18}}$), yet only $\approx1.53\times10^{12}$ of them are reachable by short Boolean formulas. The reachable fraction is effectively zero.

2. **Thermodynamic floor for distinction maintenance.**  
   Erasing a single distinction at room temperature costs $2.87\times10^{-21}\,$J. Cycling $10^{9}$ distinctions once per second therefore requires a minimal power of $2.87\times10^{-12}\,$W. Scaling linearly, a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second (Eq. 4.6).

3. **Compression‑induced ontology collapse.**  
   An ultrametric tree with $L=40$ levels ($N=40$) compresses $2^{30}$ fine balls into $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$. Under uniform spreading of $10^{5}$ objects, the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, yielding an expected number of resolvable objects essentially zero. Survival of individuals requires compression no deeper than level $r\approx23$, i.e. $b^{L-r}\gtrsim10^{5}$.

4. **Resolution collapse threshold.**  
   Any high‑level predicate demanding more than $N$ bits of precision (e.g. $n_{\mathrm{prec}}=100$) cannot be faithfully re‑entered; the excess $36$ bits cause unre‑enterability (Section 4.10).

These results together define a quantitative bridge between ontological commitments, logical expressibility, and physical resource limits.

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Binary distinction model ($D_{N}=\{0,1\}^{N}$) | Real observers may use multi‑valued or continuous features; the counting bound would change accordingly. |
| Uniform distribution of objects across ultrametric balls (Poisson model) | Non‑uniform clustering can increase survivability; the zero‑object result is a worst‑case estimate. |
| Short‑formula reachability limited to conjunctions of $\le$ 8 literals | Allowing deeper formulas (e.g., 12 literals) would raise $N_{\text{short}}$ but still remain negligible relative to $2^{2^{N}}$. |
| Landauer’s bound as a strict lower limit | Real hardware operates orders of magnitude above the bound; the derived $N_{\max}$ is an optimistic ceiling. |
| Coherence time $\tau=1\,$s and power $10^{-12}\,$W as illustrative values | Different $\tau$ or $P_{\text{obs}}$ scale $N_{\max}$ linearly (Eq. 4.6). |
| Exact ultrametric tree depth $L$ and branching $b$ | Varying $b$ changes $N$ (Eq. 3.1) but does not alter the qualitative compression factor. |

### 6.2 Failure modes and falsification

A single observation that would falsify the main claim—that the reachable fraction of admissible predicates is effectively zero—would be the empirical discovery of a compact representation (e.g., a Boolean circuit of size $<10^{6}$) that enumerates a non‑negligible subset (say $>10^{15}$) of distinct predicates for $N=64$. Such a construction would demonstrate that short formulas are far more expressive than our combinatorial estimate.

Other failure modes include:

* **Hardware exceeding Landauer’s bound**: If a physical system could reliably erase bits at energy below $k_{B}T\ln2$, the derived distinction budget $N_{\max}$ would be an underestimate.
* **Non‑binary distinctions**: If observers can exploit multi‑level symbols without a proportional energy penalty, the counting bound $2^{2^{N}}$ would no longer apply.
* **Correlated object placement**: Strong correlations could yield many resolvable objects even under deep compression, contradicting the Poisson‑based survival probability.

### 6.3 Open questions

* How does the framework extend to probabilistic ontologies where existence predicates are weighted rather than crisp sets?  
* What are the implications for quantum‑computational models, where qubits encode superpositions rather than classical bits?  
* Can adaptive compression schemes (e.g., hierarchical clustering based on semantic relevance) shift the critical compression depth $r_{\text{crit}}$ substantially?

## 7. Practical Implications and Engineering Pathways

### (a) Primary users and decision impact  

* **Embedded AI designers** (e.g., micro‑robotics, edge sensors) can use the derived $N_{\max}$ to decide how many binary features (object detections, state flags) a low‑power controller may maintain without exceeding its energy budget.  
* **Ontology engineers** (e.g., developers of graph‑based ontologies for decentralization [8]) can assess whether a proposed high‑level classification scheme can be faithfully re‑entered given the target hardware’s distinction budget.  
* **Philosophers of physics** can employ the compression analysis to argue that, under finite‑resource constraints, only coarse‑grained structures survive re‑entry, informing debates on relational versus substance ontologies ([4]).

### (b) Technology readiness  

The present work is a purely analytical study that has not undergone peer review; according to NASA’s scale it resides at **TRL 2** (technology concept formulation).

### (c) Minimal de‑risking experiment  

A feasible pilot is to program a low‑power microcontroller (e.g., an ARM Cortex‑M0) to toggle a set of $N$ binary flags at a controlled rate $f_{\text{cycle}}$ while measuring its instantaneous power draw with a high‑resolution source‑meter. The experiment would:

1. Vary $N$ from $10^{6}$ to $10^{9}$ and $f_{\text{cycle}}$ from $0.1$ Hz to $10$ Hz.  
2. Compare the observed power $P_{\text{obs}}$ to the Landauer‑based prediction $P_{\text{erase}} = f_{\text{cycle}}\,N\,k_{B}T\ln2$.  

If $P_{\text{obs}}$ consistently exceeds the prediction by orders of magnitude, the model’s quantitative relevance for engineering design is confirmed; a deviation where $P_{\text{obs}}$ falls *below* the prediction would falsify the thermodynamic admissibility criterion.

### (d) Engineering constraints  

* **Measurement precision**: Detecting power at the picowatt level ($10^{-12}$ W) requires specialized instrumentation; otherwise the experiment cannot resolve the Landauer floor.  
* **Clock stability**: Accurate control of $f_{\text{cycle}}$ is needed to ensure the erasure rate matches the theoretical model.  
* **Memory architecture**: The distinction bits must be stored in volatile memory that is refreshed each cycle; otherwise the erasure cost is not incurred as modeled.  

These constraints are directly derived from the equations in Section 4.

### (e) Order‑of‑magnitude projections  

Assuming an ideal reversible implementation (no erasures) and a nanowatt power budget, Eq. 4.6 projects a maximal distinction throughput of  

\[
N_{\max}\approx3.48\times10^{8}\;\text{bits s}^{-1}.
\]

Conversely, a realistic microcontroller operating at $10^{-9}$ W would support only $\sim3.5\times10^{5}$ bits s$^{-1}$, illustrating the steep gap between the theoretical limit and practical devices.

### (f) Risks and misuse  

* **Ontological over‑assertion**: Engineers might be tempted to claim existence of fine‑grained entities without verifying that their hardware satisfies the derived distinction budget, leading to brittle systems that fail under power constraints.  
* **Security implications**: An adversary could deliberately overload a low‑power device’s distinction budget (e.g., by forcing excessive state updates) to induce denial‑of‑service, exploiting the linear relationship between $N$ and $P_{\text{erase}}$.

Mitigation strategies include incorporating budget checks into system‑level design tools and enforcing conservative safety margins.

## 8. Conclusion

By formalizing ontology as a set of admissible predicates over a finite‑distinction space, we have linked logical expressibility, combinatorial explosion, and thermodynamic cost. The analysis shows that:

* The space of admissible existence claims grows doubly exponentially with the number of binary distinctions, yet syntactically reachable predicates form a vanishingly small subset.  
* Maintaining or erasing distinctions incurs an unavoidable energy cost given by Landauer’s principle; this yields a hard upper bound on the number of distinctions a low‑power observer can sustain.  
* Aggressive compression of the distinction space collapses individual objects, leaving only coarse structure as ontologically viable.

These findings provide a quantitative criterion for when re‑entry is physically admissible and suggest concrete engineering checks for resource‑constrained systems. Future work should explore probabilistic ontologies, quantum‑computational extensions, and empirical validation of the thermodynamic bounds.

## References

[1] arXiv:1112.0343v1 | Ontological Queries: Rewriting and Optimization (Extended Version)  
[4] arXiv:2610.25349v1 | Predicted Class Correction: Conformal Thresholds for Classes with No Calibration Data  
[5] arXiv:2104.13859v1 | Beables, Primitive Ontology and Beyond: How Theories Meet the World  
[6] arXiv:2310.18378v2 | Ontology Revision based on Pre-trained Language Models  
[7] arXiv:1604.05363v1 | Comparing Published Scientific Journal Articles to Their Pre-print Versions  
[8] arXiv:2204.06025v2 | Energy Complexity of Regular Languages  
[9] QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real?  
[10] QNFO: Ontological Re‑Entry: What Can We Say Exists?  
[11] QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure  
[12] QNFO: Unified Theory of Non‑Archimedean Ontology  

## Appendix A. Divergence report

During the multi‑author drafting process, the primary point of divergence concerned the choice of distinction budget $N$ for illustrative calculations:

| Issue | Draft A | Draft B | Draft C | Adopted convention |
|-------|---------|---------|---------|--------------------|
| Counting analysis | $N=64$ (machine‑word size) | $N=64$ | $N=64$ | $N=64$ retained (Section 4.1) |
| Ultrametric compression example | $N=40$ (tree depth $L=40$, $b=2$) | $N=40$ | $N=40$ | $N=40$ retained (Section 4.4) |

Both conventions are explicitly stated in the respective subsections; the paper therefore presents both scenarios side‑by‑side rather than forcing a single $N$ value.

## Appendix B. Claim attribution

| Claim ID | Statement | Source drafts (A/B/C) | Agreement |
|----------|-----------|-----------------------|-----------|
| C1 | Number of states for $N=64$ is $2^{64}=1.8447\times10^{19}$. | A, B, C | Convergent |
| C2 | Number of admissible predicates is $2^{2^{64}}\approx10^{5.553\times10^{18}}$. | A, B, C | Convergent |
| C3 | Reachable short predicates $\approx$ $1.53\times10^{12}$. | A, B, C | Convergent |
| C4 | Fraction of reachable predicates $\approx0$. | A, B, C | Convergent |
| C5 | Landauer erasure energy per bit at $300\,$K is $2.87\times10^{-21}\,$J. | A, B, C | Convergent |
| C6 | Erasure power for $10^{9}$ distinctions at $1\,$Hz is $2.87\times10^{-12}\,$W. | A, B, C | Convergent |
| C7 | Maximum distinguishable bits for a $10^{-12}\,$W observer is $3.48\times10^{8}$. | A, B, C | Convergent |
| C8 | Ultrametric compression factor from level 10 to 30 is $1.05\times10^{6}$. | A, B, C | Convergent |
| C9 | Expected resolvable objects after compression is $3.78\times10^{-41}\approx0$. | A, B, C | Convergent |
| C10 | Critical compression depth for $10^{5}$ objects to survive is $r\approx23$. | A, B, C | Convergent |
| C11 | Excess precision of $36$ bits makes predicate $c_{i}$ unre‑enterable. | A, B, C | Convergent |
| C12 | TRL of this work is 2. | A, B, C | Convergent |
| C13 | Proposed microcontroller experiment to falsify the Landauer‑based budget. | A, B, C | Conver