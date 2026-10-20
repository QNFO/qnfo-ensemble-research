# Ontological Re-Entry: What Can We Say Exists?

## Abstract

The re‑entry problem asks which existence claims a theory can legitimately make when its internal structure is projected back onto the world by a finite‑resource observer. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite‑distinction space $D_{N}$ and counting its admissible existence predicates, (ii) deriving a thermodynamic admissibility criterion from Landauer’s erasure cost, (iii) formalizing re‑entry as a map from high‑level predicates to admissible predicates over $D_{N}$, and (iv) analyzing failure modes such as false‑premise capture and resolution collapse. For $N=64$ binary distinctions we compute $2^{2^{64}}$ admissible predicates, of which only $\approx1.5\times10^{12}$ are reachable by short Boolean formulas, yielding an effectively zero fraction. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; cycling $10^{9}$ distinctions at $1\,$Hz requires $2.87\times10^{-12}\,$W, while a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second. Ultrametric compression of a $2^{40}$‑state space reduces $2^{30}$ fine balls to $2^{10}$ coarse balls, a compression factor of $10^{6}$, and shows that under aggressive compression individual objects disappear from the ontology. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re‑entry is physically admissible.

## 1. Introduction

Resource‑constrained agents—such as embedded AI controllers, low‑power sensors, or theoretical observers limited by the Bekenstein bound—must decide which entities they are allowed to assert as existing. Current practice either assumes an unrestricted ontology or adopts ad‑hoc heuristics, leading to hidden costs and ambiguous semantics. For example, a robotic system that classifies hardware components using a shared ontology may implicitly assume the existence of every component it can name, even when its memory cannot store the corresponding distinctions. Similarly, a quantum‑foundational theorist may posit particle‑like entities without accounting for the energy required to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits were available, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

This paper therefore asks: **what can a finite‑entropy observer legitimately claim exists, and what is the minimal physical cost of those claims?** We answer by constructing a finite‑distinction framework, deriving explicit counting bounds, and connecting them to Landauer’s erasure principle. The analysis reveals three concrete consequences: (1) the space of admissible existence predicates is astronomically larger than the set reachable by short formulas; (2) each maintained distinction incurs a non‑zero energy cost; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

The contributions are:
1. A formal definition of a finite distinction space and of admissible existence predicates, with explicit counting bounds (Section 3, derived in Section 4).  
2. A thermodynamic admissibility criterion derived from the erasure cost of distinctions [7] (Section 3.3, quantified in Section 4).  
3. A definition of ontological re‑entry modeled on query rewriting against an ontology [1], with a necessary condition for lossless re‑entry (Section 3.4).  
4. An analysis of failure modes, including false‑premise commitments observed for multimodal models [5] and definitional fragmentation documented for decentralization [6] (Section 4.6).

## 2. Background and Related Work

**Ontological queries and rewriting.** The database literature formalizes re‑entry as query rewriting. In [1] ontological queries are compiled into equivalent queries over the underlying data, providing a precise analogue of a re‑entry map where the ontology is the theory and the database is the world‑as‑modeled.

**Engineering ontologies.** The ReApp architecture for industrial robotics combines model‑driven engineering with semantic technologies, performing re‑entry from a design ontology onto running robot components [8]. This illustrates that re‑entry maps are not unique and that multiple classification systems can coexist.

**Primitive ontology and realism.** Primitive‑ontology programs argue that ontological clarity is a necessary condition for any theoretical framework [3]. Our work operationalizes this necessity by quantifying the resources required for clarity.

**Relational ontology.** Contemporary physics can be read as endorsing a relational ontology, where distinctions are relations rather than substances [4]. The finite‑distinction geometry we adopt makes this relational view explicit and resource‑bounded.

**Thermodynamic cost of distinction.** Landauer’s principle states that erasing a bit at temperature $T_{\mathrm{env}}$ costs at least $E_{\mathrm{bit}}=k_{B}T_{\mathrm{env}}\ln2$ [7]. This establishes a direct link between information processing and energy consumption, which we import into ontology.

**False premises as re‑entry failures.** Large multimodal models (LMMs) exhibit false‑premise failures: they assert the existence of objects not present in the image, a concrete instance of re‑entry failure [5].

**Definitional stagnation.** Decentralization lacks a universally accepted definition, exemplifying how absent re‑entry criteria allow incompatible ontological commitments to accumulate [6].

**Language‑model ontologies.** Fine‑tuning LLMs with Retrieval‑Augmented Generation for legal regulation demonstrates an engineering pattern where a high‑level ontology (legal concepts) is re‑entered onto human conduct via a bounded retrieval mechanism [2].

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

1. $|S_{N}| = 2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.8447\times10^{19}$.
2. Number of admissible predicates:
   $$
   2^{2^{64}}.
   $$
   $\log_{10}(2^{2^{64}})=2^{64}\log_{10}2\approx1.8447\times10^{19}\times0.30103\approx5.553\times10^{18},
   $$
   so the count is $\approx10^{5.553\times10^{18}}$.

3. **Syntactic reachability.** Assume short formulas are conjunctions of at most $k_{\mathrm{lit}}=8$ literals chosen from $2N=128$ literals.
   \[
   \binom{128}{8}= \frac{128\cdot127\cdot126\cdot125\cdot124\cdot123\cdot122\cdot121}{8!}
   =\frac{57\,645\,610\,944\,768\,000}{40\,320}\approx1.4298\times10^{12}.
   \]
   Adding lower‑order terms $\sum_{j=0}^{7}\binom{128}{j}$ multiplies by a factor $\approx1.07$, giving a total of $\approx1.53\times10^{12}$ short conjunctions.

**Conclusion 4.1.** The fraction of admissible predicates reachable by short formulas is
\[
\frac{1.53\times10^{12}}{10^{5.553\times10^{18}}}\approx0,
\]
i.e. effectively zero.

### 4.2 Erasure cost of a distinction

**Inputs.** $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$, $T_{\mathrm{env}}=300\,\mathrm{K}$, $\ln2=0.693147$.

1. $k_{B}T_{\mathrm{env}} = 1.380649\times10^{-23}\times300 = 4.141947\times10^{-21}\,\mathrm{J}$.
2. $E_{\mathrm{bit}} = 4.141947\times10^{-21}\times0.693147 = 2.8709\times10^{-21}\,\mathrm{J}$.

**Cycling cost.** Assume $N_{\mathrm{dist}}=10^{9}$ distinctions, $f_{\mathrm{cycle}}=1\,\mathrm{s^{-1}}$.
\[
P_{\mathrm{erase}} = 1\times10^{9}\times2.8709\times10^{-21}=2.8709\times10^{-12}\,\mathrm{W}.
\]

**Scaling projection.** For $10^{20}$ distinctions cycled at $10^{9}\,\mathrm{s^{-1}}$:
\[
P_{\mathrm{erase}} = 10^{20}\times10^{9}\times2.8709\times10^{-21}=2.87\times10^{8}\,\mathrm{W}.
\]

**Conclusion 4.2.** The minimal erasure power grows linearly with both the number of distinctions and the cycle rate.

### 4.3 Distinction budget from a power budget

**Inputs.** $P_{\mathrm{obs}}=10^{-12}\,\mathrm{W}$, $\tau=1\,\mathrm{s}$, $k_{B}T\ln2=2.8709\times10^{-21}\,\mathrm{J}$.

\[
N_{\max} = \frac{P_{\mathrm{obs}}\tau}{k_{B}T\ln2}
          = \frac{10^{-12}}{2.8709\times10^{-21}}
          = 3.4832\times10^{8}.
\]

**Conclusion 4.3.** A nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second.

### 4.4 Ultrametric ball counting and compression

**Inputs.** $b=2$, $L=40$ $\Rightarrow N=40$.

1. $|S_{N}| = 2^{40}=1\,099\,511\,627\,776\approx1.10\times10^{12}$.
2. Entropy $S = Nk_{B}\ln2 = 40\times1.380649\times10^{-23}\times0.693147
   = 3.82785\times10^{-22}\,\mathrm{J/K}$.
3. Erasure energy at $T=300\,\mathrm{K}$:
   $E_{\mathrm{erase}} = S\times T = 3.82785\times10^{-22}\times300
   = 1.14836\times10^{-19}\,\mathrm{J}$.
4. Number of balls at radius level $r$ is $b^{L-r}$.
   - $r=10$: $2^{30}=1.0737\times10^{9}$ fine balls.
   - $r=30$: $2^{10}=1.024$ coarse balls.
5. Compression factor:
   \[
   \frac{2^{30}}{2^{10}} = 2^{20}=1\,048\,576\approx1.05\times10^{6}.
   \]

**Conclusion 4.4.** Compressing from level 10 to level 30 reduces the number of distinguishable regions by a factor of about one million.

### 4.5 Re‑entry classification under compression

**Inputs.** Theory posits $m=10^{5}$ objects uniformly spread over the $2^{30}$ fine balls. Coarse balls at level 30 number $2^{10}=1\,024$.

Average occupancy per coarse ball:
\[
\lambda = \frac{m}{2^{10}} = \frac{100\,000}{1\,024}=97.65625.
\]

Assuming a Poisson model, the probability that a coarse ball contains exactly one object is
\[
p_{1}= \lambda e^{-\lambda}
      =97.65625\times e^{-97.65625}.
\]
Since $e^{-97.65625}=10^{-97.65625/\ln10}=10^{-42.410}\approx3.87\times10^{-43}$,
\[
p_{1}\approx97.65625\times3.87\times10^{-43}\approx3.78\times10^{-41}.
\]

Expected number of resolvable objects:
\[
m_{\mathrm{real}} = m\times p_{1}
                 \approx10^{5}\times3.78\times10^{-41}
                 =3.78\times10^{-36}\approx0.
\]

**Scaling of the survival threshold.** For individuals to survive we need $\lambda\lesssim1$, i.e. $m\lesssim b^{L-r}$. Solving $b^{L-r}=10^{5}$ for $r$:
\[
L-r = \log_{2}10^{5}= \frac{5\ln10}{\ln2}=16.6096,
\qquad
r = 40-16.6096 = 23.39.
\]
Thus compression to level $\approx23$ still permits $10^{5}$ individuals; deeper compression eliminates them.

**Conclusion 4.5.** Under aggressive compression (level 30) the ontology collapses to coarse structure; individual objects cease to be ontologically real.

### 4.6 Resolution collapse

**Inputs.** High‑level predicate $c_{i}$ requires $n_{\mathrm{prec}}=100$ bits of precision, while the observer’s distinction budget is $N=64$.

The excess precision is
\[
\Delta = n_{\mathrm{prec}} - N = 100 - 64 = 36\ \text{bits}.
\]

Any admissible predicate over $D_{64}$ can depend on at most $64$ base coordinates; therefore it can distinguish at most $2^{64}$ equivalence classes. Predicate $c_{i}$ distinguishes $2^{100}$ classes, exceeding the expressive capacity of $D_{64}$ by a factor $2^{36}\approx6.87\times10^{10}$. Consequently no map $r$ can assign an admissible $E\subseteq S_{64}$ that preserves the extension of $c_{i}$.

**Conclusion 4.6.** When the required precision exceeds the distinction budget, re‑entry fails outright (resolution collapse). The excess $\Delta$ quantifies the minimal number of additional distinctions that would be needed for lossless re‑entry.

## 5. Results

The quantitative outcomes of the analysis are:

| # | Quantity | Value | Interpretation |
|---|----------|-------|----------------|
| R1 | Number of states for $N=64$ | $2^{64}=1.8447\times10^{19}$ | Size of the distinction space |
| R2 | Number of admissible predicates | $2^{2^{64}}\approx10^{5.553\times10^{18}}$ | Upper bound on ontological expressiveness |
| R3 | Reachable short conjunctions | $1.53\times10^{12}$ | Subset of predicates definable by ≤8 literals |
| R4 | Fraction reachable | $\approx0$ | Syntax bottleneck |
| R5 | Energy to erase one distinction | $2.8709\times10^{-21}\,$J | Landauer limit at 300 K |
| R6 | Erasure power for $10^{9}$ distinctions at 1 Hz | $2.8709\times10^{-12}\,$W | Minimal power consumption |
| R7 | Max distinctions for $10^{-12}$ W | $3.48\times10^{8}$ | Distinction budget from a nanowatt observer |
| R8 | Ultrametric fine balls ($r=10$) | $1.07\times10^{9}$ | Number of distinguishable regions before compression |
| R9 | Coarse balls ($r=30$) | $1.024\times10^{3}$ | Number after compression |
| R10 | Compression factor | $1.05\times10^{6}$ | Ratio of fine to coarse balls |
| R11 | Expected resolvable objects under compression | $\approx0$ | Ontology collapses to structure |
| R12 | Compression depth allowing $10^{5}$ objects | $r\approx23$ | Threshold for survival of individuals |
| R13 | Excess precision causing resolution collapse | $\Delta=36$ bits | Minimum additional distinctions required |

All numbers arise from the explicit arithmetic in Section 4.

## 6. Discussion

### 6.1 Limitations

| Limitation | Description | Sensitivity |
|------------|-------------|-------------|
| L1 | Choice of $N$ (e.g., $64$ or $40$) is modeling‑driven, not empirically fixed. | Results scale exponentially with $N$; changing $N$ alters all quantitative bounds. |
| L2 | Short‑formula model assumes at most $8$ literals; other syntactic restrictions would change the reachable count. | The fraction in R4 is highly sensitive to $k_{\mathrm{lit}}$. |
| L3 | Uniform distribution of objects across fine balls is an idealization; real ontologies may be highly non‑uniform. | The expected resolvable objects (R11) could be larger under clustering. |
| L4 | Landauer’s bound is a theoretical minimum; actual hardware incurs additional overhead. | Real erasure power will be higher than R6, making the admissibility criterion stricter. |
| L5 | Poisson model for object occupancy assumes independence; correlations would modify $p_{1}$. | Small changes in $\lambda$ produce exponential changes in $p_{1}$. |
| L6 | Temperature $T_{\mathrm{env}}=300\,$K is a modeling choice; lower temperatures reduce $E_{\mathrm{bit}}$ linearly. | Energy costs scale linearly with $T$. |
| L7 | The analysis treats distinctions as binary; multi‑valued distinctions would alter $|S_{N}|$ and counting formulas. | Counting bounds would need recomputation. |
| L8 | The re‑entry map is defined abstractly; constructing it for concrete theories may be computationally intractable. | Practical applicability depends on algorithmic tractability. |

### 6.2 Falsification Conditions

A single observation that would falsify the main claim—that thermodynamic costs bound ontological expressiveness—is:

- **Measured erasure energy per bit at $300\,$K significantly exceeds $2.87\times10^{-21}\,$J** (the Landauer limit). If empirical measurements consistently show a lower bound, the derived admissibility criterion would be invalid.

Additional falsification routes include:

- Empirical detection of individual objects surviving compression depths beyond the threshold $r\approx23$ predicted by the Poisson model.
- Observation of a high‑level predicate requiring $n_{\mathrm{prec}}=100$ bits being faithfully re‑entered into a $64$‑bit distinction space without loss, contradicting the resolution‑collapse analysis.

### 6.3 Open Questions

- How do non‑binary distinction alphabets affect the counting bounds?
- Can adaptive compression schemes preserve more individual objects than uniform ultrametric compression?
- What is the impact of quantum‑coherent memory on the erasure cost?
- How does the presence of error‑correcting codes modify the effective distinction budget?

## 7. Practical Implications and Engineering Pathways

### 7.1 Intended users and decision impact

- **Embedded AI designers** can use the derived distinction budget to decide how many binary features a low‑power controller may maintain while remaining thermodynamically admissible.
- **Quantum‑foundations researchers** can apply the compression threshold to evaluate whether particle‑like ontologies survive under a finite‑distinction budget.
- **Database system architects** can map ontological query rewriting costs to distinction budgets, informing optimizer design for resource‑constrained deployments.

If the result holds, designers will replace unconstrained ontology specifications with budgets that guarantee both logical consistency and physical feasibility.

### 7.2 Technology Readiness Level

The work is purely analytical, has not undergone peer review, and therefore resides at **TRL 2** (technology concept formulation).

### 7.3 Minimal next experiment

A feasible prototype is a **single‑bit erasure circuit** operating at $300\,$K with a calibrated calorimetric measurement of the released heat. The experiment would:

1. Initialize a bistable element (e.g., a CMOS inverter) in a known state.
2. Force a transition that erases the stored bit.
3. Measure the energy dissipated with sub‑femtojoule resolution.

**Falsification criterion:** If the measured energy is **significantly lower** than $2.87\times10^{-21}\,$J, the Landauer‑based admissibility bound is violated, falsifying the main claim.

### 7.4 Engineering constraints

- **Temperature control** to maintain $300\,$K within $\pm0.5\,$K, because $E_{\mathrm{bit}}$ scales linearly with $T$.
- **Energy measurement precision** better than $10^{-22}\,$J to resolve the Landauer limit.
- **Isolation from environmental noise** to avoid spurious heat flow.
- **Circuit design** that minimizes parasitic capacitance and leakage, ensuring that the dominant dissipation is the erasure event.

These constraints are directly derived from the thermodynamic model in Section 3.3 and the numerical values in Section 4.2.

### 7.5 Projected cost and performance bounds

Assuming the Landauer limit holds:

- Maintaining $10^{9}$ distinctions at $1\,$Hz costs $2.87\times10^{-12}\,$W (Result R6).  
- Scaling to $10^{20}$ distinctions at $10^{9}\,$Hz would require $2.87\times10^{8}\,$W (Result R12), comparable to the power consumption of a small data center.  

These projections illustrate the steep energy penalty of large‑scale ontological commitments.

### 7.6 Risks and misuse

- **Over‑restriction:** Engineers might prematurely discard useful high‑level predicates because the budget appears insufficient, potentially limiting system functionality.
- **Misinterpretation:** Policymakers could cite the energy bound as a universal physical law, ignoring the idealized assumptions (e.g., reversible computation, binary distinctions).

Mitigation requires clear communication of the model’s assumptions (Section 6.1) and the distinction between theoretical minima and practical engineering realities.

## 8. Conclusion

By uniting finite‑distinction geometry, combinatorial counting, and Landauer’s thermodynamic principle, we have derived a quantitative criterion linking ontological expressiveness to physical resources. The analysis shows that (i) the space of admissible existence predicates is astronomically larger than the set reachable by short formulas, (ii) each maintained distinction incurs a non‑zero energy cost, and (iii) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure. These results provide a concrete foundation for evaluating ontological commitments in resource‑constrained settings, from embedded AI to foundational physics. Future work will explore richer distinction alphabets, adaptive compression strategies, and experimental validation of the erasure cost bound.

## References

[1] arXiv:1112.0343v1 | Ontological Queries: Rewriting and Optimization (Extended Version)  
[2] arXiv:2610.25360v1 | Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence  
[3] arXiv:2610.25349v1 | Predicted Class Correction: Conformal Thresholds for Classes with No Calibration Data  
[4] arXiv:2511.03563v1 | ASVRI-Legal: Fine-Tuning LLMs with Retrieval Augmented Generation for Enhanced Legal Regulation  
[5] arXiv:2104.13859v1 | Beables, Primitive Ontology and Beyond: How Theories Meet the World  
[6] arXiv:2201.00907v2 | The relational ontology of contemporary physics  
[7] arXiv:2312.08366v1 | See, Say, and Segment: Teaching LMMs to Overcome False Premises  
[8] arXiv:2608.09748v2 | Defining Decentralization: An Ontological Perspective  
[9] QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure  
[10] QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real?  
[11] QNFO: Ontological Re-Entry: What Can We Say Exists?  
[12] QNFO: Unified Theory of Non-Archimedean Ontology  

## Appendix A. Divergence report

*No divergent claims were identified among the source drafts; all substantive statements converge.*

## Appendix B. Claim attribution

| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | $|S_{64}| = 2^{64} = 1.8447\times10^{19}$ | A, B, C | Convergent |
| C2 | Number of admissible predicates $2^{2^{64}} \approx 10^{5.553\times10^{18}}$ | A, B, C | Convergent |
| C3 | Reachable short conjunctions $\approx1.53\times10^{12}$ | A, B, C | Convergent |
| C4 | Fraction reachable $\approx0$ | A, B, C | Convergent |
| C5 | $E_{\mathrm{bit}} = 2.8709\times10^{-21}\,$J | A, B, C | Convergent |
| C6 | $P_{\mathrm{erase}}$ for $10^{9}$ distinctions at 1 Hz = $2.8709\times10^{-12}\,$W | A, B, C | Convergent |
| C7 | $N_{\max}=3.48\times10^{8}$ for $10^{-12}$ W budget | A, B, C | Convergent |
| C8 | Ultrametric fine balls $2^{30}=1.07\times10^{9}$, coarse balls $2^{10}=1.024\times10^{3}$ | A, B, C | Convergent |
| C9 | Compression factor $2^{20}=1.05\times10^{6}$ | A, B, C | Convergent |
| C10 | Expected resolvable objects $\approx0$ under uniform compression | A, B, C | Convergent |
| C11 | Compression depth allowing $10^{5}$ objects $r\approx23$ | A, B, C | Convergent |
| C12 | Resolution collapse excess $\Delta=36$ bits | A, B, C | Convergent |