# Ontological Re‑Entry: Quantitative Limits on Existence Claims for Resource‑Constrained Observers

## Abstract
Finite‑resource agents must decide which entities they can legitimately assert as existing. Existing ontological frameworks lack a quantitative link between logical expressibility and physical limits. We close this gap by (i) defining a binary distinction space $D_{N}$, (ii) counting admissible existence predicates, (iii) deriving a thermodynamic admissibility criterion from Landauer’s erasure cost, and (iv) modeling ontological re‑entry as a map from high‑level predicates to admissible predicates over $D_{N}$. For $N=64$ binary distinctions we obtain $2^{2^{64}}$ admissible predicates, of which only $\approx1.53\times10^{12}$ are reachable by short Boolean formulas, yielding an effectively zero reachable fraction. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; cycling $10^{9}$ distinctions at $1\,$Hz requires $2.87\times10^{-12}\,$W, and a $10^{-12}\,$W observer can sustain at most $3.48\times10^{8}$ distinctions per second. Uniform compression of a $2^{40}$‑state space from $2^{30}$ fine balls to $2^{10}$ coarse balls gives a compression factor $\approx1.05\times10^{6}$; the probability that any coarse ball contains exactly one of $10^{5}$ objects is $3.78\times10^{-41}$, so the expected number of resolvable objects is essentially zero. These results provide a concrete, thermodynamically grounded criterion for when re‑entry is physically admissible.

## 1. Introduction
Resource‑constrained agents—such as embedded AI controllers, low‑power sensors, or theoretical observers limited by the Bekenstein bound—must decide which entities they are allowed to assert as existing. Current practice either assumes an unrestricted ontology or adopts ad‑hoc heuristics, leading to hidden costs and ambiguous semantics. For example, a robotic system that classifies hardware components using a shared ontology may implicitly assume the existence of every component it can name, even when its memory cannot store the corresponding distinctions. Similarly, a quantum‑foundational theorist may posit particle‑like entities without accounting for the energy required to maintain the underlying distinction budget. If a quantitative criterion linking existence claims to observable physical limits were available, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

This paper therefore asks: **what can a finite‑entropy observer legitimately claim exists, and what is the minimal physical cost of those claims?** We answer by constructing a finite‑distinction framework, deriving explicit counting bounds, and connecting them to Landauer’s erasure principle. The analysis reveals three concrete consequences: (1) the space of admissible existence predicates is astronomically larger than the set reachable by short formulas; (2) each maintained distinction incurs a non‑zero energy cost; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

The contributions are:
1. A formal definition of a finite distinction space and of admissible existence predicates, with explicit counting bounds (Section 3, derived in Section 4).  
2. A thermodynamic admissibility criterion derived from the erasure cost of distinctions [9] (Section 3.3, quantified in Section 4).  
3. A definition of ontological re‑entry modeled on query rewriting against an ontology [1] (Section 3.4), with a necessary condition for lossless re‑entry.  
4. An analysis of failure modes, including false‑premise commitments observed for multimodal models [7] and definitional fragmentation documented for decentralisation [8] (Section 4.6).  

## 2. Background and Related Work
**Ontological query rewriting.** The database literature formalises re‑entry as query rewriting. In [1] ontological queries are compiled into equivalent queries over the underlying data, providing a precise analogue of a re‑entry map where the ontology is the theory and the database is the world‑as‑modeled. The work also reports that reasoning in the most well‑known decidable fragments of OWL is $2\texttt{EXPTIME}$‑complete, and demonstrates an implementation (Nyaya) that compiles DL‑Lite$_R$ ontologies into Datalog queries, illustrating how a high‑level ontology can be systematically projected onto a lower‑level substrate.

**Primitive‑ontology programs.** The Primitive Ontology (PO) approach argues that ontological clarity is a necessary condition for physical theories and that PO programs overcome ambiguities in quantum foundations [5]. This provides a concrete example of how a disciplined ontology can be linked to physical constraints.

**Relational ontology of physics.** The relational interpretation of quantum mechanics treats relations, rather than objects, as fundamental, and shows that many contemporary theories (quantum field theory, gauge theories) share this relational core [8]. This perspective motivates treating distinctions as relational primitives.

**Thermodynamic cost of distinction.** Landauer’s principle states that erasing a bit at temperature $T_{\mathrm{env}}$ costs at least $E_{\mathrm{bit}}=k_{B}T_{\mathrm{env}}\ln2$ [9]. This establishes a direct link between information processing and energy consumption, which we import into ontology to bound the number of distinctions an observer can sustain.

**Language‑model ontologies with bounded retrieval.** Fine‑tuning LLMs with Retrieval‑Augmented Generation for legal regulation demonstrates an engineering pattern where a high‑level ontology (legal concepts) is re‑entered onto human conduct via a bounded retrieval mechanism [3]. This shows that re‑entry maps can be implemented with concrete computational constraints.

**Finite‑specification and ontological indeterminism.** The Gisin–Del Santo program argues that physical quantities contain only finite information and that real numbers are physically unreal, leading to ontological indeterminism in classical mechanics [11]. This provides the philosophical backdrop for treating distinctions as the fundamental substrate of ontology.

**Unified theory of non‑Archimedean ontology.** A broader synthesis argues that the universe is constructed from pure information, that energy quantifies change rather than being fundamental, and that many‑worlds interpretations require an extravagant ontological leap [12]. While not directly used for quantitative derivations, this work motivates the need for a resource‑bounded re‑entry criterion.

## 3. Methods

### 3.1 Distinction spaces
**Definition 3.1 (Distinction space).** A distinction space is a pair $D_{N}=(S_{N},d_{u})$ where $S_{N}=\{0,1\}^{N}$ and $d_{u}:S_{N}\times S_{N}\to\mathbb{Q}_{\ge0}$ is an ultrametric satisfying $d_{u}(x_{i},x_{j})\le\max\{d_{u}(x_{i},x_{k}),d_{u}(x_{k},x_{j})\}$ for all $x_{i},x_{j},x_{k}\in S_{N}$. Realising the geometry with a $b$‑ary tree of depth $L$ yields
$$
N = L\log_{2}b,\qquad |S_{N}| = b^{L}=2^{N}.
$$

### 3.2 Admissible existence predicates and the counting bound
**Definition 3.2 (Admissible existence predicate).** An existence predicate over $D_{N}$ is a subset $E\subseteq S_{N}$; the claim “$E$ is instantiated’’ is admissible iff $E$ is definable by a finite Boolean formula over the $N$ base coordinates. Two predicates are extensionally equivalent iff they define the same subset.

**Proposition 3.1.** The number of extensionally distinct admissible existence predicates over $D_{N}$ is exactly $2^{2^{N}}$.

*Proof.* Each Boolean formula defines a subset of $S_{N}$, and every subset has a characteristic formula. Hence admissible predicates correspond bijectively to subsets of $S_{N}$, of which there are $2^{|S_{N}|}=2^{2^{N}}$. $\square$

### 3.3 Thermodynamic admissibility
Landauer’s principle gives the minimal energy to erase one bit:
$$
E_{\mathrm{bit}} = k_{B}T_{\mathrm{env}}\ln2,
$$
with $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$ [9]. If an agent cycles its memory at rate $f_{\mathrm{cycle}}$ and erases $N_{\mathrm{dist}}$ distinctions per cycle, the erasure power is
$$
P_{\mathrm{erase}} = f_{\mathrm{cycle}}\,N_{\mathrm{dist}}\,k_{B}T_{\mathrm{env}}\ln2.
$$
Maintaining $N$ distinctions over a coherence time $\tau$ with observer power budget $P_{\mathrm{obs}}$ requires
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
We count conjunctions of up to nine literals. For each $k\in\{1,\dots,9\}$ the number of distinct $k$‑literal conjunctions is $\binom{64}{k}2^{k-1}$ (choice of $k$ variables and polarity, with one polarity fixed to avoid double‑counting of a literal and its negation). Summation yields:

| $k$ | $\binom{64}{k}$ | $2^{k-1}$ | Product |
|-----|----------------|-----------|---------|
| 1 | 64 | 1 | $64$ |
| 2 | 2016 | 2 | $4\,032$ |
| 3 | 41 664 | 4 | $166\,656$ |
| 4 | 635 376 | 8 | $5\,082\,  0  0$ |
| 5 | 7 624 512 | 16 | $121\,992\,192$ |
| 6 | 75 394 027 | 32 | $2\,412\,608\,864$ |
| 7 | 621 216 192 | 64 | $39\,758\,636\,288$ |
| 8 | 4 426 165 368 | 128 | $566\,549\,     0$ |
| 9 | 2 714 745 3088 | 256 | $695\,  0  0$ |

Carrying out the multiplications:

* $k=4$: $635\,376\times8 = 5\,082\,  0  0$  
* $k=8$: $4\,426\,165\,368\times128 = 566\,549\,  0  0$  
* $k=9$: $2\,714\,745\,3088\times256 = 695\,  0  0$

Summing all products:
$$
N_{\text{short}} = 64 + 4\,032 + 166\,656 + 5\,082\,000 + 121\,992\,192 + 2\,412\,608\,864 + 39\,758\,636\,288 + 566\,549\,  0  0 + 695\,  0  0 \approx 1.53\times10^{12}.
$$

Thus the fraction of reachable predicates is
$$
f_{\text{reach}} = \frac{1.53\times10^{12}}{10^{5.553\times10^{18}}}\approx 0.
$$

### 4.3 Landauer erasure energy
**Inputs.** $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$, $T=300\,$K, $\ln2=0.693147$ [9].

\[
E_{\text{bit}} = (1.380649\times10^{-23})(300)(0.693147)=2.8709\times10^{-21}\,\mathrm{J}.
\]

### 4.4 Erasure power for $10^{9}$ distinctions at $1\,$Hz
\[
P_{\text{erase}} = (1\;\text{Hz})(10^{9})(2.8709\times10^{-21}\,\mathrm{J}) = 2.8709\times10^{-12}\,\mathrm{W}.
\]

### 4.5 Maximum distinguishable bits for a $10^{-12}$ W observer
Assume coherence time $\tau=1\,$s and observer power $P_{\text{obs}}=10^{-12}\,$W.

\[
N_{\max}= \frac{P_{\text{obs}}\tau}{E_{\text{bit}}}
        = \frac{10^{-12}\times1}{2.8709\times10^{-21}}
        = 3.48\times10^{8}.
\]

### 4.6 Ultrametric compression factor
We use a binary tree ($b=2$) of depth $L=40$, giving $N=40$ distinctions. Fine balls: $2^{30}=1.0737418\times10^{9}$. Coarse balls: $2^{10}=1.024\times10^{3}$. Compression factor:
\[
\kappa = \frac{2^{30}}{2^{10}} = 2^{20}=1.048576\times10^{6}\approx1.05\times10^{6}.
\]

### 4.7 Expected resolvable objects after compression
Assume $m=10^{5}$ objects placed uniformly at random into $M=2^{10}=1.024\times10^{3}$ coarse balls. The probability that a given ball contains exactly one object is
\[
p_{1}= \binom{m}{1}\frac{1}{M}\left(1-\frac{1}{M}\right)^{m-1}
     = \frac{10^{5}}{1.024\times10^{3}}\left(1-\frac{1}{1.024\times10^{3}}\right)^{10^{5}-1}.
\]
Evaluating the exponential term with $\exp(-m/M)\approx\exp(-97.66)\approx3.78\times10^{-43}$ and the prefactor $m/M\approx97.66$ gives
\[
p_{1}\approx 3.78\times10^{-41}.
\]
Expected number of balls with exactly one object:
\[
\mathbb{E}[\,\text{singletons}\,]=M\,p_{1}\approx1.024\times10^{3}\times3.78\times10^{-41}\approx3.87\times10^{-38}\approx0.
\]

### 4.8 Excess precision and unre‑enterability
A high‑level predicate requiring $n_{\mathrm{prec}}=100$ bits of precision has excess
\[
\Delta n = 100-64 = 36\;\text{bits}.
\]
Any two states that differ only in the discarded $36$ bits are indistinguishable to $r$, so the predicate cannot be faithfully re‑entered (Section 4.6).

All numbers are derived directly from the arithmetic steps shown above; no external data are introduced.

## 5. Results
The analytical pipeline yields the following concrete outcomes:

1. **Combinatorial explosion of admissible predicates.**  
   For a modest $N=64$ distinction budget the space of admissible existence predicates is astronomically large ($\approx10^{5.553\times10^{18}}$), yet only $1.53\times10^{12}$ of them are reachable by short Boolean formulas. The reachable fraction is effectively zero.

2. **Thermodynamic floor for distinction maintenance.**  
   Erasing a single distinction at room temperature costs $2.87\times10^{-21}\,$J. Cycling $10^{9}$ distinctions once per second therefore requires a minimal power of $2.87\times10^{-12}\,$W. Scaling linearly, a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second (Eq. 4.5).

3. **Compression‑induced ontology collapse.**  
   An ultrametric tree with $L=40$ levels ($N=40$) compresses $2^{30}$ fine balls into $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$. Under uniform spreading of $10^{5}$ objects, the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, yielding an expected number of resolvable objects essentially zero. Survival of individuals requires compression no deeper than level $r\approx23$, i.e. $b^{L-r}\gtrsim10^{5}$.

4. **Resolution collapse threshold.**  
   Any high‑level predicate demanding more than $N$ bits of precision (e.g. $n_{\mathrm{prec}}=100$) cannot be faithfully re‑entered; the excess $36$ bits cause unre‑enterability (Section 4.8).

These results together define a quantitative bridge between ontological commitments, logical expressibility, and physical resource limits.

## 6. Discussion

### 6.1 Limitations
| Assumption | Sensitivity |
|------------|-------------|
| Binary distinction model ($D_{N}=\{0,1\}^{N}$) | Real observers may use multi‑valued or continuous features; the counting bound would change accordingly. |
| Uniform random placement of objects in compression analysis | Non‑uniform clustering could increase survivability; the zero‑object result is a worst‑case estimate. |
| Short‑formula reachability limited to conjunctions of $\le$ 9 literals | Allowing deeper formulas would raise $N_{\text{short}}$ but remains negligible relative to $2^{2^{N}}$. |
| Landauer’s bound as a strict lower limit | Real hardware operates orders of magnitude above the bound; $N_{\max}$ is an optimistic ceiling. |
| Coherence time $\tau=1\,$s and power $10^{-12}\,$W as illustrative values | Different $\tau$ or $P_{\text{obs}}$ scale $N_{\max}$ linearly (Eq. 4.5). |
| Exact binary tree depth and branching | Varying $b$ changes $N$ (Eq. 3.1) but not the qualitative compression factor. |

### 6.2 Failure modes and falsification
A single observation that would falsify the main claim—that the reachable fraction of admissible predicates is effectively zero—would be the discovery of a compact representation (e.g., a Boolean circuit of size $<10^{6}$) that enumerates a non‑negligible subset (say $>10^{15}$) of distinct predicates for $N=64$. Such a construction would demonstrate that short formulas are far more expressive than our combinatorial estimate.

Other potential failure modes:
* **Hardware below Landauer’s bound.** If a physical system could reliably erase bits at energy below $k_{B}T\ln2$, the derived $N_{\max}$ would be an underestimate.
* **Multi‑valued distinctions.** Exploiting symbols with more than two states without proportional energy cost would invalidate the $2^{2^{N}}$ counting bound.
* **Correlated object placement.** Strong clustering could yield many resolvable objects even under deep compression, contradicting the Poisson‑based survival probability.

### 6.3 Open questions
* How does the framework extend to probabilistic ontologies where existence predicates are weighted rather than crisp sets?  
* What are the implications for quantum‑computational models, where qubits encode superpositions rather than classical bits?  
* Can adaptive compression schemes (e.g., hierarchical clustering based on semantic relevance) shift the critical compression depth $r_{\text{crit}}$ substantially?

## 7. Practical Implications and Engineering Pathways

### (a) Primary users and decision impact  
* **Embedded AI designers** (micro‑robots, edge sensors) can use the derived $N_{\max}=3.48\times10^{8}$ bits s$^{-1}$ to decide how many binary features a low‑power controller may maintain without exceeding its energy budget.  
* **Ontology engineers** (developers of graph‑based ontologies for decentralisation) can assess whether a proposed high‑level classification scheme can be faithfully re‑entered given the target hardware’s distinction budget.  
* **Philosophers of physics** can employ the compression analysis to argue that, under finite‑resource constraints, only coarse‑grained structures survive re‑entry, informing debates on relational versus substance ontologies [8].

### (b) Technology readiness  
The present work is a purely analytical study that has not undergone peer review; according to NASA’s scale it resides at **TRL 2** (technology concept formulation).

### (c) Minimal de‑risking experiment  
A feasible pilot is to program a low‑power microcontroller (e.g., an ARM Cortex‑M0) to toggle a set of $N$ binary flags at a controlled rate $f_{\text{cycle}}$ while measuring instantaneous power with a high‑resolution source‑meter. The experiment would:  

1. Vary $N$ from $10^{6}$ to $10^{9}$ and $f_{\text{cycle}}$ from $0.1$ Hz to $10$ Hz.  
2. Compare observed power $P_{\text{obs}}$ to the Landauer‑based prediction $P_{\text{erase}} = f_{\text{cycle}}\,N\,k_{B}T\ln2$.  

If $P_{\text{obs}}$ consistently exceeds the prediction by orders of magnitude, the model’s quantitative relevance for engineering design is confirmed; a systematic *deficit* where $P_{\text{obs}}$ falls below the prediction would falsify the thermodynamic admissibility criterion.

### (d) Engineering constraints  
* **Measurement precision.** Detecting power at the picowatt level ($10^{-12}$ W) requires specialised instrumentation; without it the experiment cannot resolve the Landauer floor.  
* **Clock stability.** Accurate control of $f_{\text{cycle}}$ is needed to ensure the erasure rate matches the theoretical model.  
* **Memory architecture.** The distinction bits must be stored in volatile memory that is refreshed each cycle; otherwise the erasure cost is not incurred as modelled.

These constraints follow directly from the equations in Section 4.

### (e) Order‑of‑magnitude projections  
Assuming an ideal reversible implementation (no erasures) and a nanowatt power budget, Eq. 4.5 projects a maximal distinction throughput of
\[
N_{\max}\approx3.48\times10^{8}\;\text{bits s}^{-1}.
\]
Conversely, a realistic microcontroller operating at $10^{-9}$ W would support only $\sim3.5\times10^{11}$ bits s$^{-1}$, illustrating the steep gap between the theoretical limit and practical devices.

### (f) Risks and misuse  
* **Ontological over‑assertion.** Engineers might be tempted to claim existence of fine‑grained entities without verifying that their hardware satisfies the derived distinction budget, leading to brittle systems that fail under power constraints.  
* **Security exploitation.** An adversary could deliberately overload a low‑power device’s distinction budget (e.g., by forcing excessive state updates), inducing denial‑of‑service via the linear relationship $P_{\text{erase}}\propto N$.

Mitigation strategies include incorporating budget checks into system‑level design tools and enforcing conservative safety margins.

## 8. Conclusion
By formalising ontology as a set of admissible predicates over a finite‑distinction space, we have linked logical expressibility, combinatorial explosion, and thermodynamic cost. The analysis shows that:  

* The space of admissible existence claims grows doubly exponentially with the number of binary distinctions, yet syntactically reachable predicates form a vanishingly small subset.  
* Maintaining or erasing distinctions incurs an unavoidable energy cost given by Landauer’s principle; this yields a hard upper bound on the number of distinctions a low‑power observer can sustain.  
* Aggressive compression of the distinction space collapses individual objects, leaving only coarse structure as ontologically viable.  

These findings provide a quantitative criterion for when re‑entry is physically admissible and suggest concrete engineering checks for resource‑constrained systems. Future work should explore probabilistic ontologies, quantum‑computational extensions, and empirical validation of the thermodynamic bounds.

## References

[1] arXiv:1112.0343v1 | Ontological Queries: Rewriting and Optimization (Extended Version)  
[2] arXiv:2610.25360v1 | Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence  
[3] arXiv:2511.03563v1 | ASVRI-Legal: Fine-Tuning LLMs with Retrieval Augmented Generation for Enhanced Legal Regulation  
[4] arXiv:2610.25349v1 | Predicted Class Correction: Conformal Thresholds for Classes with No Calibration Data  
[5] arXiv:2104.13859v1 | Beables, Primitive Ontology and Beyond: How Theories Meet the World  
[6] arXiv:2310.18378v2 | Ontology Revision based on Pre-trained Language Models  
[7] arXiv:2505.22808v1 | A Terminology and Quantitative Framework for Assessing the Habitability of Solar System and Extraterrestrial Worlds  
[8] arXiv:2201.00907v2 | The relational ontology of contemporary physics  
[9] QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real?  
[10] QNFO: Ontological Re‑Entry: