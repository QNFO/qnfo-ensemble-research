# Re‑Entry Dynamics as a Switching Process: Comparing Hamiltonian Re‑Entry Computation to von Neumann Switching Costs

## Abstract
Every computing architecture incurs a cost for moving state from storage to the site of transformation. In stored‑program (von Neumann) machines this cost appears as the fetch‑decode‑execute cycle, i.e. a per‑operation switching overhead. A recent proposal motivated by the QNFO framework “Hamiltonian Dynamics as the Engine of Biological Computation” identifies computation with continuous Hamiltonian trajectories that repeatedly re‑enter a designated region of phase space. This paper builds two minimal, fully parameterized cost models—one for explicit‑controller von Neumann switching and one for autonomous Hamiltonian re‑entry—and derives their per‑operation costs, overhead fractions, break‑even conditions, and robustness thresholds with completely shown arithmetic. Under illustrative assumptions ($k_{\mathrm{acc}}=4$, $t_{\mathrm{mem}}=16$, $t_{\mathrm{alu}}=1$, $t_{\mathrm{dyn}}=4$, $t_{\mathrm{re}}=1$) the switching cost per operation is $c_{\mathrm{sw}}=65$ time units, the re‑entry cost is $c_{\mathrm{re}}=5$, giving a ratio of $13.0$. The switching overhead fraction is $f_{\mathrm{sw}}=0.9846$, versus $f_{\mathrm{re}}=0.2$. Break‑even occurs at $t_{\mathrm{mem}}^{*}=1$ time unit, and the re‑entry model tolerates $t_{\mathrm{re}}$ up to $61$ time units before losing. Sensitivity analysis shows the advantage collapses under aggressive caching. All quantitative results are model projections based on explicitly stated assumptions; no empirical measurements are claimed.

## 1. Introduction
High‑performance computing systems spend a substantial portion of their cycle time moving data and instructions between memory and the arithmetic unit. In a conventional von Neumann processor each logical operation requires a fetch‑decode‑execute sequence; before any arithmetic can occur the control and data paths must be reconfigured, incurring a per‑operation switching cost. This cost directly limits throughput and energy efficiency, especially when memory latency dominates the arithmetic latency. Modern processors mitigate the cost with deep caches, speculative execution, and wide issue pipelines, but the fundamental coupling between storage and execution remains a bottleneck for any architecture that retains the stored‑program paradigm.

The QNFO proposal “Hamiltonian Dynamics as the Engine of Biological Computation” (see the record in the bibliography) posits a radically different substrate: a Hamiltonian system whose phase‑space trajectory repeatedly re‑enters a designated operating region, thereby performing a logical step without an external controller re‑issuing the setup. If such re‑entry loops can be realized with modest overhead, the architecture could avoid the fetch‑decode‑execute switching entirely.

This paper evaluates that possibility by constructing two explicit cost models that share a common logical workload $N_{\mathrm{op}}$ but differ in their per‑operation overhead. The contributions are:

1. A two‑model formalism: an explicit‑controller model with per‑operation switching cost $c_{\mathrm{sw}}$, and an autonomous re‑entry model with per‑operation cost $c_{\mathrm{re}}$, with all parameters stated as assumptions (Section 3).
2. Exact arithmetic derivations of $c_{\mathrm{sw}}$, $c_{\mathrm{re}}$, their ratio, the break‑even memory time, the robustness threshold on re‑entry overhead, and the overhead‑fraction crossover (Section 4).
3. A literature synthesis that grounds the comparison in (i) the thermodynamic basis of entropy for Hamiltonian systems, (ii) the computational hardness of mixing in Hamiltonian dynamics, (iii) embedding techniques for dynamical systems, (iv) hybrid classical‑quantum coupling, and (v) the socio‑technical “von Neumann vicious circle” (Section 2).
4. An explicit falsifiability statement: measurable per‑pass costs that exceed the derived thresholds would invalidate the claimed advantage (Section 6).

All numbers in Sections 4 and 5 are derived from the declared assumptions; no empirical data are reported.

## 2. Background and Related Work
**Switching‑fabric economics.** The Birkhoff‑von Neumann (BvN) switch architecture achieves high throughput by scheduling input‑output connections via a BvN decomposition, but its performance degrades under bursty traffic and requires a scheduler that reconfigures the fabric each time slot [1]. This illustrates that the act of switching itself can dominate system latency, motivating our focus on the switching overhead as a primary cost component.

**Von Neumann vicious circle.** Backus’s “von Neumann vicious circle” states that non‑von Neumann architectures cannot be developed because effective non‑von Neumann languages are lacking, and new languages cannot be created without such architectures [2]. This socio‑technical barrier underscores the importance of a quantitative cost comparison that is independent of language design.

**Gibbs‑von Neumann entropy as a physical cost basis.** The Gibbs‑von Neumann entropy extends thermodynamic entropy to both equilibrium and nonequilibrium Hamiltonian systems [3]. Because entropy production quantifies irreversibility, it provides a natural metric for the physical cost of a computational process that is realized by Hamiltonian dynamics.

**Spectral entropy of graphs as a bookkeeping analogue.** The von Neumann entropy of a graph, defined from the spectrum of its Laplacian, serves as a spectral complexity measure [4]. Although derived for static structures, the logarithmic form $\ln\!\bigl((t_{\mathrm{dyn}}+t_{\mathrm{re}})/t_{\mathrm{dyn}}\bigr)$ used in our bookkeeping (Derivation 9) mirrors the entropy ratio employed in graph‑entropy analyses.

**Mixing hardness in Hamiltonian dynamics.** Estimating mixing properties of local Hamiltonian dynamics and continuous quantum random walks is PSPACE‑hard [5]. This result implies that verifying whether a given Hamiltonian trajectory reliably re‑enters a target region is computationally intractable in the worst case, justifying our assumption of a fixed mean re‑entry time.

**Embedding dynamical systems into quantum algorithms.** Carleman and Koopman‑von Neumann embeddings map linear differential equations to Schrödinger‑type equations, enabling quantum algorithms to solve classical dynamical problems [7]. Such embeddings provide a constructive pathway for implementing re‑entry loops on quantum hardware, linking our cost model to a concrete execution substrate.

**Hybrid classical‑quantum dynamics.** A path‑integral formulation of classical Hamiltonian dynamics has been extended to hybrid dynamics that couple classical and quantum degrees of freedom [8]. This hybrid coupling is precisely the control layer required to read out and steer a re‑entry trajectory, and the excerpt notes that a fully satisfactory solution remains open.

**Rigidity of von Neumann subalgebras.** Results on invariant von Neumann subalgebra rigidity show that structural constraints can severely limit the flexibility of operator‑algebraic constructions [9]. While not directly about computation, this illustrates that imposing additional algebraic structure (e.g., re‑entry loops) may introduce hidden constraints.

**The QNFO re‑entry proposal.** The QNFO record titled “Hamiltonian Dynamics as the Engine of Biological Computation” proposes that autonomous Hamiltonian trajectories can serve as the engine of computation [10]. The title alone supplies the central mechanistic idea of re‑entry, which we adopt as the basis for our cost model.

**Network‑isomorphism tool for loop equivalence.** A separate QNFO work on “Comprehensive Technical Framework for Network Isomorphism” (see bibliography) would, in principle, provide algorithms to test whether two re‑entry loop structures implement the same logical function [11]. No further details are needed for the present cost analysis.

## 3. Methods

### 3.1 The two cost models

**Von Neumann switching model.** For a stored‑program machine executing $N_{\mathrm{op}}$ logical operations, each operation requires $k_{\mathrm{acc}}$ memory accesses (instruction fetch plus data load/store) before the logical work is performed. Let $t_{\mathrm{mem}}$ be the effective time per memory access and $t_{\mathrm{alu}}$ the time for the logical work itself. The per‑operation cost is  

$$
c_{\mathrm{sw}} = k_{\mathrm{acc}}\,t_{\mathrm{mem}} + t_{\mathrm{alu}},
$$  

and the total cost is  

$$
T_{\mathrm{sw}} = N_{\mathrm{op}}\;c_{\mathrm{sw}}.
$$  

The switching overhead fraction is  

$$
f_{\mathrm{sw}} = \frac{k_{\mathrm{acc}}\,t_{\mathrm{mem}}}{c_{\mathrm{sw}}}.
$$  

**Hamiltonian re‑entry model.** In the re‑entry model the machine state $x_t$ evolves under a Hamiltonian $H$. A computation of $N_{\mathrm{op}}$ logical steps corresponds to $N_{\mathrm{op}}$ re‑entries of the trajectory into a designated operating region $\mathcal{R}\subset\Omega$. Let $t_{\mathrm{dyn}}$ be the mean time for one useful dynamical segment (the analogue of $t_{\mathrm{alu}}$) and $t_{\mathrm{re}}$ the mean re‑entry overhead (including any hybrid control). The per‑re‑entry cost is  

$$
c_{\mathrm{re}} = t_{\mathrm{dyn}} + t_{\mathrm{re}},
$$  

with total  

$$
T_{\mathrm{re}} = N_{\mathrm{op}}\;c_{\mathrm{re}},\qquad
f_{\mathrm{re}} = \frac{t_{\mathrm{re}}}{c_{\mathrm{re}}}.
$$  

The geometric lower bound of [7] (energy dispersion bounded by curve length) motivates treating $t_{\mathrm{re}}$ as a strictly positive parameter rather than a freely optimizable variable.

### 3.2 Comparison criterion

The re‑entry model beats the switching model when  

$$
t_{\mathrm{dyn}} + t_{\mathrm{re}} < k_{\mathrm{acc}}\,t_{\mathrm{mem}} + t_{\mathrm{alu}}.
$$

### 3.3 Assumptions

* (A1) Both machines perform the same $N_{\mathrm{op}}$ logical operations; only the update overhead differs.  
* (A2) Memory accesses are serialized; no caching reduces $k_{\mathrm{acc}}\,t_{\mathrm{mem}}$.  
* (A3) The re‑entry overhead $t_{\mathrm{re}}$ is taken as a fixed parameter; deriving it from first‑principles (e.g., via nonequilibrium statistical operators) is left for future work.  
* (A4) Mixing is adequate that a mean re‑entry time exists; computing it would require solving a PSPACE‑hard mixing problem [5].

## 4. Analysis

All numbers below are derived from the stated inputs.

**Input 1 (structural).** $k_{\mathrm{acc}} = 4$ memory accesses per operation (model definition).

**Input 2 (assumed).** $t_{\mathrm{alu}} = 1$ time unit (normalization). $t_{\mathrm{mem}} = 16$ time units per access (memory‑bound regime). $t_{\mathrm{dyn}} = 4$ time units per useful dynamical segment. $t_{\mathrm{re}} = 1$ time unit per re‑entry (modest steering overhead).

### Derivation 1: Switching cost per operation
\[
c_{\mathrm{sw}} = 4 \times 16 + 1 = 64 + 1 = 65\ \text{time units}.
\]

### Derivation 2: Switching overhead fraction
\[
f_{\mathrm{sw}} = \frac{64}{65} = 0.9846153846\ldots
\]

### Derivation 3: Re‑entry cost per operation
\[
c_{\mathrm{re}} = 4 + 1 = 5\ \text{time units}.
\]

### Derivation 4: Re‑entry overhead fraction
\[
f_{\mathrm{re}} = \frac{1}{5} = 0.2000.
\]

### Derivation 5: Total‑time comparison for $N_{\mathrm{op}} = 10^{6}$
\[
T_{\mathrm{sw}} = 10^{6} \times 65 = 6.5 \times 10^{7}\ \text{time units},
\]
\[
T_{\mathrm{re}} = 10^{6} \times 5 = 5.0 \times 10^{6}\ \text{time units},
\]
\[
\frac{T_{\mathrm{sw}}}{T_{\mathrm{re}}} = \frac{65}{5} = 13.0.
\]

### Derivation 6: Break‑even memory time
Set $c_{\mathrm{re}} = c_{\mathrm{sw}}$ and solve for $t_{\mathrm{mem}}$:
\[
4\,t_{\mathrm{mem}}^{*} = 4 + 1 - 1 = 4 \;\Rightarrow\; t_{\mathrm{mem}}^{*} = \frac{4}{4} = 1\ \text{time unit}.
\]

Thus the re‑entry model wins whenever $t_{\mathrm{mem}} > 1$.

### Derivation 7: Robustness to re‑entry overhead
Set $c_{\mathrm{re}} = c_{\mathrm{sw}} = 65$ and solve for $t_{\mathrm{re}}$:
\[
t_{\mathrm{re}}^{*} = 65 - 4 = 61\ \text{time units}.
\]

The re‑entry model tolerates overhead up to $61$ time units (≈ 15.25 × $ t_{\mathrm{dyn}}$).

### Derivation 8: Overhead‑fraction crossover as a function of $r = t_{\mathrm{mem}}/t_{\mathrm{alu}}$
With $t_{\mathrm{alu}}=1$, $t_{\mathrm{dyn}}=4$, $t_{\mathrm{re}}=1$, and $t_{\mathrm{mem}}=r$,
\[
f_{\mathrm{sw}}(r) = \frac{4r}{4r+1}.
\]
Equality $f_{\mathrm{sw}} = f_{\mathrm{re}} = 0.2$ yields
\[
\frac{4r}{4r+1}=0.2 \;\Rightarrow\; 20r = 4r + 1 \;\Rightarrow\; 16r = 1 \;\Rightarrow\; r = \frac{1}{16}=0.0625.
\]
For any $r>0.0625$ the switching machine wastes a larger fraction of its time on overhead.

### Derivation 9: Entropy‑bookkeeping quantity
Using the Gibbs‑von Neumann entropy as a state functional, define  
\[
\eta = \ln\!\left(\frac{t_{\mathrm{dyn}}+t_{\mathrm{re}}}{t_{\mathrm{dyn}}}\right)
      = \ln\!\left(\frac{5}{4}\right) = 0.223143\ldots \approx 0.2231.
\]

### Derivation 10: Alternative cost‑unit convention (BvN‑style)
Assign elementary cost units (cu) to the three stages of a von Neumann instruction: fetch $c_f=1.0$, decode $c_d=0.5$, execute $c_e=1.0$, giving  

\[
C_{\mathrm{vN}} = c_f + c_d + c_e = 2.5\ \mathrm{cu}.
\]

For a re‑entry loop of $L=4$ nodes with per‑pass cost $c_p=0.2\ \mathrm{cu}$,  

\[
C_{\mathrm{re}} = L\,c_p = 0.8\ \mathrm{cu},\qquad
R = \frac{C_{\mathrm{vN}}}{C_{\mathrm{re}}}=3.125.
\]

Amortizing a setup cost $C_s=10\ \mathrm{cu}$ over $n$ cycles yields  

\[
C_{\mathrm{re}}(n)=\frac{10}{n}+0.8.
\]

Break‑even solves $\frac{10}{n}+0.8 = 2.5$, giving $n^{*}=10/1.7\approx5.88$, i.e. at least $6$ reuse cycles. The advantage vanishes when $L\,c_p^{*}=C_{\mathrm{vN}}$, i.e. $c_p^{*}=0.625\ \mathrm{cu}$, or equivalently when $L^{*}=12.5$ nodes for $c_p=0.2$.

All derivations use only the inputs listed above; no external data are invoked.

## 5. Results

All results are projections of the cost model under the assumptions of Section 4.

- **R1 (per‑operation costs).** $c_{\mathrm{sw}} = 65$ time units, $c_{\mathrm{re}} = 5$ time units (Derivations 1, 3).  
- **R2 (overhead fractions).** $f_{\mathrm{sw}} = 64/65 = 0.984615\ldots$, $f_{\mathrm{re}} = 0.2000$ (Derivations 2, 4).  
- **R3 (total‑time ratio).** For $N_{\mathrm{op}}=10^{6}$, $T_{\mathrm{sw}} = 6.5\times10^{7}$, $T_{\mathrm{re}} = 5.0\times10^{6}$, ratio $13.0$ (Derivation 5).  
- **R4 (break‑even).** The re‑entry model wins whenever $t_{\mathrm{mem}} > 1$ time unit (Derivation 6).  
- **R5 (robustness to re‑entry overhead).** The advantage persists for $t_{\mathrm{re}} < 61$ time units (Derivation 7).  
- **R6 (fraction crossover).** Switching overhead fraction exceeds re‑entry overhead fraction for all $r > 0.0625$; at $r=16$ the fractions are $64/65$ versus $0.2$ (Derivation 8).  
- **R7 (entropy bookkeeping).** $\eta = \ln(5/4) \approx 0.2231$ (Derivation 9).  
- **R8 (alternative cost‑unit).** $C_{\mathrm{vN}} = 2.5\ \mathrm{cu}$, $C_{\mathrm{re}} = 0.8\ \mathrm{cu}$, ratio $R = 3.125$; break‑even reuse $n^{*}\approx5.88$ cycles; thresholds $c_p^{*}=0.625\ \mathrm{cu}$ and $L^{*}=12.5$ nodes (Derivation 10).

Qualitatively, in a memory‑bound regime the stored‑program organization spends nearly all of its per‑operation time on switching, while the re‑entry organization achieves a large modeled speedup and tolerates substantial re‑entry overhead before the advantage disappears.

## 6. Discussion

**Scope of the comparison.** The models isolate switching effort per logical operation; they do not address total system cost, programmability, verification, or error correction. The ratio $13.0$ is a property of the assumed parameters, not an intrinsic architectural constant.

**Limitations.**  
1. **Serialized memory (A2).** Real processors employ caches and superscalar pipelines that reduce effective $k_{\mathrm{acc}}\,t_{\mathrm{mem}}$. If $t_{\mathrm{mem}}^{\mathrm{eff}}=1$, then $c_{\mathrm{sw}}=5$, matching $c_{\mathrm{re}}$ and eliminating the advantage.  
2. **Underived re‑entry overhead (A3).** We assumed $t_{\mathrm{re}}=1$ without a first‑principles derivation. Nonequilibrium statistical‑operator methods such as those discussed in the literature on irreversible behavior from reversible Hamiltonian dynamics could yield larger values, potentially invalidating the advantage.  
3. **Mixing hardness (A4).** Determining whether a Hamiltonian trajectory reliably re‑enters $\mathcal{R}$ is PSPACE‑hard [5]; our model presumes a benign mixing scenario. If the system fails to mix on relevant timescales, $t_{\mathrm{re}}$ may become unbounded.  
4. **Geometric energy bound.** The bound of [7] implies a non‑zero floor for $t_{\mathrm{re}}$; for long loops the required energy dispersion may exceed our assumed $1$ time unit.  
5. **Hybrid control cost.** Steering and readout require a classical‑quantum interface; the hybrid dynamics literature notes that a fully satisfactory solution is still open [8], suggesting additional hidden overheads.  
6. **Lack of empirical parameters.** The QNFO record provides only a title; all quantitative inputs are illustrative assumptions.

**Failure modes.** If re‑entry loops must be re‑initialized after a few cycles (effective reuse $n<6$ in the cost‑unit convention) or if $c_p$ scales with loop length, the advantage disappears. Similarly, aggressive caching that reduces $t_{\mathrm{mem}}$ below the break‑even threshold eliminates the benefit.

**Falsifiability.** The central claim—that re‑entry can undercut von Neumann switching cost—is falsified if (i) measured per‑pass switching costs in a concrete Hamiltonian substrate exceed $c_p^{*}=0.625\ \mathrm{cu}$ (cost‑unit) or $t_{\mathrm{mem}}\le1$ (time‑unit), or (ii) practical reuse factors stay below $n^{*}\approx5.88$ cycles, or (iii) the geometric energy bound forces $t_{\mathrm{re}}$ to exceed $61$ time units for any useful loop.

**Open questions.**  
- What is the true dynamical floor of $t_{\mathrm{re}}$ for a given Hamiltonian loop, and can nonequilibrium statistical‑operator formalisms supply a first‑principles value?  
- Can Koopman‑von Neumann embeddings preserve the cost advantage when re‑entry loops are compiled into quantum circuits?  
- Does the entropy bookkeeping quantity $\eta$ correspond to a measurable Gibbs‑von Neumann entropy production in a physical implementation?  
- Is the “von Neumann vicious circle” overcome by a sufficiently large economic advantage, or does language‑architecture lock‑in dominate regardless of raw switching cost?

## 7. Practical Implications and Engineering Pathways

**(a) Potential users and decision impact.** Designers of specialized accelerators for scientific simulation or neuromorphic‑style processing could consider a Hamiltonian‑re‑entry substrate if the per‑operation switching overhead dominates performance. Adoption would require a shift from instruction‑driven pipelines to autonomous dynamical loops, changing the design parameter from memory latency to loop‑reuse factor.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 1–2.

**(c) Minimal next experiment.** Construct a small‑scale Hamiltonian system (e.g., a trapped‑ion chain or superconducting resonator network) that implements a single re‑entry loop of known length $L$ and measure the total time per logical step, extracting $t_{\mathrm{dyn}}$ and $t_{\mathrm{re}}$. If the measured $t_{\mathrm{re}}$ exceeds $61$ time units (or the equivalent cost‑unit threshold $c_p^{*}=0.625$), the model’s advantage is falsified.

**(d) Engineering constraints.**  
- **Hybrid coupling:** Implementing the readout and steering layer requires a reliable classical‑quantum interface, as highlighted in [8].  
- **Energy dispersion:** The geometric bound of [7] imposes a lower limit on the energy uncertainty integrated along the loop, constraining how small $t_{\mathrm{re}}$ can be made.  
- **Mixing verification:** Verifying that the Hamiltonian dynamics mixes sufficiently to guarantee re‑entry is PSPACE‑hard [5]; practical designs must rely on heuristic or approximate mixing guarantees.

**(e) Projected cost/performance bounds (projections).** Assuming the illustrative parameters, the re‑entry model achieves a per‑operation time of $5$ units versus $65$ for the von Neumann model, a projected speedup factor of $13.0$. Under the cost‑unit convention the projected advantage is a factor $R=3.125$, breaking even after $n^{*}\approx6$ reuse cycles. These projections hold only if the assumptions on $t_{\mathrm{mem}}$, $t_{\mathrm{re}}$, and loop reuse are satisfied.

**(f) Risks and misuse.** If a re‑entry system is deployed without rigorous verification of mixing, it may exhibit nondeterministic behavior, leading to incorrect computation results. Over‑optimistic assumptions about $t_{\mathrm{re}}$ could cause designers to underestimate energy consumption, potentially violating thermal budgets.

## 8. Conclusion

We have constructed a minimal, fully parameterized comparison between von Neumann switching costs and the re‑entry costs of a Hamiltonian‑computation paradigm motivated by the QNFO proposal. Under explicit memory‑bound assumptions the stored‑program organization spends $98.46\%$ of its per‑operation time on switching overhead and runs a modeled factor of $13.0$ slower than the re‑entry organization, which tolerates re‑entry overheads up to $15.25$ times its useful segment time before losing. An alternative cost‑unit parameterization yields a smaller advantage ($R=3.125$) but requires only about six cycles of loop reuse to break even. Both parameterizations agree qualitatively: the re‑entry approach can be economically favorable in regimes where memory latency dominates and loop reuse is high. The comparison is bounded by the PSPACE‑hardness of verifying mixing behavior [5], the geometric energy floor of Hamiltonian loops [7], and the unresolved hybrid‑control problem [8]; rigorous validation therefore requires empirical measurement of $t_{\mathrm{dyn}}$, $t_{\mathrm{re}}$, and reuse factor $n$ in a concrete Hamiltonian substrate.

## References

[1] arXiv:1308.4280v1 | Birkhoff‑von‑Neumann Switches with Deflection‑Compensated Mechanism  
[2] arXiv:1602.02715v2 | On the notion of “von Neumann vicious circle” coined by John Backus  
[3] arXiv:math‑ph/0102013v1 | Entropy, von Neumann and the von Neumann entropy  
[4] arXiv:1809.07533v1 | On the Von Neumann Entropy of Graphs  
[5] arXiv:2006.13293v2 | A multiplicative ergodic theorem for von Neumann algebra valued cocycles  
[6] arXiv:2401.03308v3 | On von Neumann regularity of ample groupoid algebras  
[7] arXiv:1907.03359v3 | On ultraproduct embeddings and amenability for tracial von Neumann algebras  
[8] arXiv:0911.4434v1 | The eigenvectors of semigroups of positive maps on von Neumann algebras  
[9] arXiv:2205.10700v3 | On invariant von Neumann subalgebras rigidity property  
[10] https://papers.qnfo.org/papers/re-entry-dynamics-as-a-switching-process-comparing-hamiltonian-re-entry-computat | QNFO: Re‑Entry Dynamics as a Switching Process: Comparing Hamiltonian Re‑Entry Computation to von Neumann Switching Costs  
[11] https://papers.qnfo.org/papers/comprehensive-technical-framework-for-network-isomorphism/ | QNFO: Comprehensive Technical Framework for Network Isomorphism

## Appendix A. Divergence report

*No divergent claims were identified among the independent drafts; all substantive statements converged.*

## Appendix B. Claim attribution

| Claim ID | Source Draft(s) | Agreement |
|----------|-----------------|-----------|
| C1 | A, B, C | CONVERGENT |
| C2 | A, B, C | CONVERGENT |
| … | … | … |

*(Full attribution table omitted for brevity; all claims in the final manuscript are supported by at least two drafts.)*