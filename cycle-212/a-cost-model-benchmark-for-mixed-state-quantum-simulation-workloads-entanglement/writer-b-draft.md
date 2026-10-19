# A Cost-Model Benchmark for Mixed-State Quantum Simulation Workloads: Entanglement‑Cost Anchors and Reuse‑Aware Re‑Entry Metrics

## Abstract
Classical simulation of quantum circuits is increasingly organized as repeated‑run workloads—variational‑parameter sweeps, noisy multishot studies, and error‑correction cycles—so that the cost of a workload, not a single circuit, determines feasibility. Mixed‑state targets arise from noise channels, thermal ensembles, and decohered registers, yet most existing benchmarks address only pure‑state workloads and therefore underestimate difficulty. This paper fills the gap by defining a benchmark specification that (i) selects a family of mixed‑state anchors whose entanglement cost is exactly known via the additivity of entanglement of formation on two‑Bell‑state mixtures [5]; (ii) computes those anchor costs with full arithmetic; and (iii) embeds the anchors in a three‑layer memory‑and‑energy cost model that scales the representation overhead as $R_n=2^{n}$ and projects energy consumption using a DRAM‑traffic coefficient and an orchestration factor [10]. The exact anchor values are $E_F=1.000000$, $0.811278$, and $0.468996$ ebits at mixing parameters $p=0.5$, $0.25$, and $0.9$, respectively, with zero sensitivity at $p=0.5$. For a 10‑qubit register the mixed‑state memory overhead is $1024\times$ (16 MiB vs 16 KiB) and the projected energy per $10^{4}$‑step workload is $33.554432$ J under the stated assumptions. By anchoring benchmark difficulty to provable information‑theoretic quantities, the specification enables future work on more complex mixed states to be measured against a rigorously defined baseline.

## 1. Introduction
Quantum‑algorithm developers, high‑performance‑computing (HPC) centers, and hardware vendors face a concrete obstacle: classical simulators must allocate memory and energy that grow dramatically when the target state is mixed rather than pure, but existing benchmark suites report only pure‑state costs. For a 10‑qubit simulation, a pure‑state vector requires $2^{10}=1024$ complex amplitudes (≈ 16 KiB in double precision), whereas a full density matrix needs $4^{10}=1{,}048{,}576$ amplitudes (≈ 16 MiB). The resulting factor‑1024 memory increase can dominate procurement budgets and dictate whether a workload fits on a given node. Moreover, mixed‑state workloads appear in variational quantum eigensolver (VQE) sweeps, noisy multishot studies, and quantum error‑correction (QEC) cycles, all of which are central to near‑term quantum‑software stacks. If a benchmark could quantify the *information‑theoretic* difficulty of such workloads, designers could decide whether to invest in larger memory systems, redesign algorithms to reduce mixedness, or adopt alternative simulation techniques.

The “so what?” is that without a rigorously anchored mixed‑state benchmark, performance claims remain incomparable and hardware procurement decisions are based on optimistic pure‑state estimates. By providing exact entanglement‑cost anchors and a transparent scaling model, this work enables stakeholders to (i) compare simulators on a common difficulty scale, (ii) forecast memory and energy budgets for realistic mixed‑state workloads, and (iii) plan incremental improvements that are provably beneficial.

**Contributions.**  
1. Derivation of exact entanglement‑of‑formation values for the two‑Bell‑state family $\rho_p$ and proof that $E_C(\rho_p)=E_F(\rho_p)$ [5] (Section 4.1).  
2. Closed‑form representation‑overhead ratio $R_n=2^{n}$ for density‑matrix versus state‑vector simulation (Section 4.2).  
3. Composite difficulty score $\Sigma(n)=R_n\overline{E_F}$ and energy projection $E_{\text{workload}}$ under explicit DRAM‑traffic and orchestration assumptions (Section 4.4).  
4. Specification of a workload‑level benchmark that combines anchor costs, representation overhead, and three‑layer energy budgeting (Section 3).  
5. Practical pathway for experimental validation and assessment of the benchmark’s assumptions (Section 7).

## 2. Background and Related Work
The benchmark design draws on structural analogies, methodological precedents, and quantitative insights from the supplied bibliography.

* The elasticity Hilbert complex with mixed boundary conditions proves closure and compactness via abstract functional analysis and regular decompositions [1]. This mirrors our two‑step approach: first fix exact anchor costs (closure), then derive quantitative scaling (compactness).  
* Estimation‑aware optimal control of mobile sensors incorporates uncertainty about the target state into trajectory planning [2]. We adopt the same principle by embedding the *uncertainty* of the mixed state (its entanglement cost) into the benchmark’s workload model.  
* Ullemar’s Jacobian formula converts a conjectured relationship into an exact closed‑form expression [3]. Our use of the exact entanglement‑cost formula for two‑Bell‑state mixtures follows the same epistemic upgrade from heuristic to theorem.  
* The biharmonic Hilbert complex extends the elasticity results, illustrating a program of successive re‑entry where each new complex re‑uses abstract machinery from the previous one [4]. Our benchmark similarly re‑uses the entanglement‑cost result as a base for higher‑level cost layers.  
* The core mathematical result that the entanglement cost of arbitrary mixtures of two Bell states equals their entanglement of formation, because of additivity on the supporting subspace, provides the exact anchor values [5].  
* The de Rham Hilbert complex establishes a base case of pure‑state simulation, which our mixed‑state benchmark extends by adding a representation‑overhead layer [6].  
* The defect‑relation bookkeeping in second‑main‑theorem holomorphic maps counts how much of a budget each constraint consumes [7]. We similarly allocate the total difficulty into information, memory, and orchestration components.  
* Quantitative cohomology shows how scalar invariants can stratify qualitative properties of manifolds [8]. Our scalar invariant $E_F$ stratifies mixed states by simulation difficulty.  
* Workload‑level reuse planning (QuWARP) argues that benchmarking must be performed at the workload granularity rather than per circuit [9]. Our benchmark follows this framing.  
* The three‑layer thermodynamic budgeting model separates compute, memory, and orchestration energy, and explicitly acknowledges that the latter can dominate [10]. We adopt this separation for our energy projections.

## 3. Methods

### 3.1 Design goals
The benchmark specification comprises three tightly coupled components:

1. **Anchor states.** A parametric family $\rho_p$ of two‑qubit mixed states whose asymptotic entanglement cost $E_C(\rho_p)$ is exactly known by the additivity theorem of [5].  
2. **Workload wrapper.** A repeated‑run workload that sweeps the mixing parameter $p$ (analogous to a VQE parameter sweep) and repeats each $p$ value for a fixed number of shots $S$ (analogous to noisy multishot studies). The workload‑level framing follows [9].  
3. **Cost model.** A three‑layer model (compute, representation, orchestration) that (i) counts memory entries, (ii) multiplies by the anchor ebit value, and (iii) adds an energy factor derived from DRAM traffic and an orchestration multiplier, as prescribed in [10].

### 3.2 Anchor family
Define the two orthogonal Bell states
\[
\lvert\Phi^{+}\rangle = \frac{1}{\sqrt{2}}(\lvert00\rangle+\lvert11\rangle),\qquad
\lvert\Phi^{-}\rangle = \frac{1}{\sqrt{2}}(\lvert00\rangle-\lvert11\rangle),
\]
and the mixed state
\[
\rho_p \;=\; p\,\lvert\Phi^{+}\rangle\langle\Phi^{+}\rvert \;+\; (1-p)\,\lvert\Phi^{-}\rangle\langle\Phi^{-}\rvert,\qquad p\in[0,1].
\]
For this family the entanglement of formation reduces to the binary entropy of the larger eigenvalue, and by the additivity result of [5] the entanglement cost equals the entanglement of formation:
\[
E_C(\rho_p)=E_F(\rho_p)=h_2\!\bigl(\lambda_{\max}(p)\bigr),\qquad
\lambda_{\max}(p)=\max(p,1-p).
\]

### 3.3 Scaling model
For an $n$‑qubit register a pure‑state simulation stores $2^{n}$ complex amplitudes; a full density matrix stores $4^{n}=2^{2n}$ amplitudes. The representation‑overhead ratio is therefore
\[
R_n \;=\; \frac{4^{n}}{2^{n}} \;=\; 2^{n}.
\]
We treat $R_n$ as the *memory‑layer* multiplier. The *information‑layer* multiplier is the average anchor ebit $\overline{E_F}$ (Section 4.4). The *orchestration‑layer* multiplier $f_{\text{orch}}$ is taken from [10] as a constant factor that captures control‑stack overhead.

### 3.4 Energy coefficients
The energy projection uses two explicit coefficients:
* DRAM traffic energy per byte $e_{\text{DRAM}} = 10^{-10}\,\text{J/byte}$ (modeling assumption).  
* Orchestration factor $f_{\text{orch}} = 2$ (modeling assumption from [10]).

All other quantities are derived analytically.

## 4. Analysis

Every input number below is either a definition, a standard constant, or taken from a cited source. All arithmetic is shown.

### 4.1 Entanglement of formation of $\rho_p$

**Step 1 (Spectrum).** $\rho_p$ is a convex combination of two orthogonal rank‑one projectors, so its eigenvalues are $p$ and $1-p$. Define $\lambda_{\max}=\max(p,1-p)$.

**Step 2 (Binary entropy).** For a two‑eigenvalue distribution the binary entropy is
\[
h_2(x) = -x\log_2 x -(1-x)\log_2(1-x).
\]
Because each eigenvector is a maximally entangled Bell state, the entanglement of formation equals $h_2(\lambda_{\max})$.

**Step 3 (Evaluation at $p=0.5$).**  
\[
\lambda_{\max}=0.5,\qquad
E_F(\rho_{0.5}) = -0.5\log_2 0.5 -0.5\log_2 0.5 = 1.000000\ \text{ebits}.
\]

**Step 4 (Evaluation at $p=0.25$).**  
\[
\lambda_{\max}=0.75,\qquad
E_F(\rho_{0.25}) = -0.75\log_2 0.75 -0.25\log_2 0.25.
\]
Compute:
\[
\log_2 0.75 = \frac{\ln 0.75}{\ln 2} \approx -0.415037,\qquad
\log_2 0.25 = -2.
\]
Thus
\[
E_F(\rho_{0.25}) = -0.75(-0.415037) -0.25(-2) = 0.311278 + 0.500000 = 0.811278\ \text{ebits}.
\]

**Step 5 (Evaluation at $p=0.9$).**  
\[
\lambda_{\max}=0.9,\qquad
\log_2 0.9 = \frac{\ln 0.9}{\ln 2} \approx -0.152003,\qquad
\log_2 0.1 = \frac{\ln 0.1}{\ln 2} \approx -3.321928.
\]
Then
\[
E_F(\rho_{0.9}) = -0.9(-0.152003) -0.1(-3.321928) = 0.136803 + 0.332193 = 0.468996\ \text{ebits}.
\]

**Step 6 (Sensitivity).** For $p\ge 0.5$, $E_F(p)=h_2(p)$ and
\[
\frac{dE_F}{dp}= \log_2\!\frac{1-p}{p}.
\]
At $p=0.5$ the argument of the logarithm is $1$, so $\frac{dE_F}{dp}\big|_{p=0.5}=0$ ebits per unit $p$.

### 4.2 Representation overhead

Input: $n=10$ qubits.  
\[
R_{10}=2^{10}=1024.
\]
Pure‑state storage: $2^{10}$ amplitudes $\times 16$ bytes per complex double = $16\,384$ bytes = $16$ KiB.  
Density‑matrix storage: $4^{10}=1{,}048{,}576$ amplitudes $\times 16$ bytes = $16\,777\,216$ bytes = $16$ MiB.

### 4.3 Workload‑level sweep footprint

A sweep over $K$ values of $p$, each stored as a full density matrix on $n$ qubits, occupies
\[
M_{\text{sweep}}(K,n)=K\cdot 4^{n}\cdot 16\ \text{bytes}.
\]
With $K=21$ (grid $p\in\{0,0.05,\dots,1.0\}$) and $n=10$:
\[
M_{\text{sweep}} = 21 \times 1{,}048{,}576 \times 16
= 21 \times 16{,}777{,}216
= 352{,}321{,}536\ \text{bytes} \approx 352\ \text{MB}.
\]

### 4.4 Composite difficulty score and energy projection

The average anchor ebit is
\[
\overline{E_F}= \frac{E_F(\rho_{0.25})+E_F(\rho_{0.5})+E_F(\rho_{0.9})}{3}
= \frac{0.811278+1.000000+0.468996}{3}
= 0.760091\ \text{ebits}.
\]

The composite score for $n$ qubits is
\[
\Sigma(n)=R_n \times \overline{E_F}.
\]
For $n=10$:
\[
\Sigma(10)=1024 \times 0.760091 = 778.333\ \text{weighted ebit‑units}.
\]

**Energy per sweep step.**  
Memory traffic per step: $4^{n}\times 16$ bytes.  
\[
E_{\text{step}} = 4^{10}\times 16 \times e_{\text{DRAM}} \times f_{\text{orch}}
= 1{,}048{,}576 \times 16 \times 10^{-10} \times 2
= 3.3554432 \times 10^{-3}\ \text{J}.
\]

**Energy for a multishot workload.**  
With $S=10^{4}$ steps:
\[
E_{\text{workload}} = S \times E_{\text{step}}
= 10^{4} \times 3.3554432 \times 10^{-3}
= 33.554432\ \text{J}.
\]

All numbers above are direct consequences of the definitions and the two explicit modeling assumptions.

## 5. Results

All values below are either computed in Section 4 with shown arithmetic or explicitly labeled projections.

| $p$ | $E_F(\rho_p)$ (ebits) |
|-----|-----------------------|
| $0.25$ | $0.811278$ |
| $0.5$  | $1.000000$ |
| $0.9$  | $0.468996$ |

*By the additivity theorem of [5], these equal the asymptotic entanglement cost $E_C(\rho_p)$ for the anchor states.*

* Sensitivity at $p=0.5$: $\displaystyle\frac{dE_F}{dp}\big|_{p=0.5}=0$ ebits per unit $p$ (Section 4.1, Step 6).  
* Representation overhead at $n=10$: $R_{10}=1024$, giving a memory ratio of $1024\times$ (Section 4.2).  
* Sweep footprint for $K=21$ grid points: $352{,}321{,}536$ bytes ≈ 352 MB (Section 4.3).  
* Composite difficulty score: $\Sigma(10)=778.333$ weighted ebit‑units (Section 4.4).  
* Energy projection for $10^{4}$ steps: $E_{\text{workload}}=33.554432$ J (Section 4.4).  
* Uncertainty: a factor‑3 variation in $e_{\text{DRAM}}$ propagates linearly, yielding a plausible range $11$–$101$ J.

All reported numbers are either exact (anchor ebits, overhead ratio) or projections under the stated coefficients.

## 6. Discussion

### Limitations
1. **Anchor family scope.** The benchmark anchors are limited to mixtures of two Bell states, a two‑dimensional family. Realistic mixed states (e.g., thermal states of many qubits) lie outside this family, and the additivity proof of [5] does not extend to them.  
2. **Weighting convention.** The composite score $\Sigma$ multiplies an information measure by a memory‑overhead factor. This is a design choice; alternative additive or normalized combinations would yield different numeric values.  
3. **Energy coefficients.** The DRAM‑energy coefficient $e_{\text{DRAM}}=10^{-10}$ J/byte and orchestration factor $f_{\text{orch}}=2$ are modeling assumptions, not measured quantities. Their true values depend on hardware architecture and software stack.  
4. **Full density‑matrix assumption.** The memory overhead $R_n=2^{n}$ assumes a naïve full density‑matrix representation. Simulators that exploit tensor‑network compression, stabilizer techniques, or stochastic sampling may experience lower overhead, causing the benchmark to mis‑rank such methods.

### Failure modes
If a simulator implements a representation that does not store all $4^{n}$ entries (e.g., a low‑rank approximation), the memory‑layer prediction will overestimate actual usage, leading to an unfair penalty. Conversely, if a simulator stores the full matrix but uses hardware with a DRAM energy coefficient an order of magnitude larger than $10^{-10}$ J/byte, the energy projection will underestimate real consumption.

### What would falsify the claims
The claim that $E_C(\rho_p)=E_F(\rho_p)$ for the anchor family would be falsified by a rigorous re‑examination of the additivity proof in [5] that shows a counterexample within the two‑Bell‑state mixture space. The claim that mixed‑state workloads are uniformly harder than pure‑state workloads would be falsified by an empirical demonstration that a mixed‑state simulator achieves lower total energy than a pure‑state simulator for the same $n$ under identical hardware, contradicting the composite score’s monotonicity.

### Open questions
1. Can exact entanglement‑cost anchors be constructed for mixtures of three or more Bell states, or for states with non‑maximally entangled support?  
2. How should the composite score be normalized across different register sizes $n$ to enable fair cross‑scale comparisons?  
3. What is the empirically correct orchestration factor $f_{\text{orch}}$ for pure‑simulation workloads that lack a quantum processing unit?  
4. How do the empty‑summary entries [11] and [12] contribute relevant benchmarking or coherence‑taxonomy material once their full texts become available?

## 7. Practical Implications and Engineering Pathways

### (a) Primary users and decision impact
* **Quantum‑software developers** can use the benchmark to decide whether to target mixed‑state simulation or to redesign algorithms to reduce mixedness, based on a quantified memory and energy budget.  
* **HPC system architects** can assess whether existing node memory (e.g., 256 GiB) suffices for a planned mixed‑state workload of a given qubit count, using the $R_n$ factor.  
* **Benchmark designers** can adopt the anchor‑cost specification as a baseline when extending benchmarks to more complex mixed states.

If the benchmark’s predictions hold, a decision to allocate additional memory resources (e.g., moving from 64 GiB to 256 GiB nodes) would be justified for workloads exceeding $n\approx12$ qubits, where $R_n$ exceeds $4096$.

### (b) Technology readiness
The work is purely analytical, has not undergone peer review, and therefore resides at **TRL 2** (concept formulation). No hardware or software implementation has been demonstrated, so higher TRLs are not claimed.

### (c) Minimal next experiment
Implement a reference density‑matrix simulator for $n=10$ qubits, store a single $\rho_{0.5}$ state, and measure:
1. Actual memory consumption (bytes).  
2. DRAM traffic during one update step (bytes).  
If measured memory equals $16{,}777{,}216$ bytes (within 5 %) and measured DRAM energy per step is within a factor of 2 of $3.355\times10^{-3}$ J, the analytical model is validated. A deviation beyond these bounds would falsify the model’s assumptions.

### (d) Engineering constraints
* **Memory capacity**: The $R_n=2^{n}$ factor directly bounds the maximum $n$ that fits on a node with a given RAM size.  
* **DRAM energy coefficient**: The projection hinges on $e_{\text{DRAM}}$; accurate measurement of this coefficient on the target platform is required.  
* **Orchestration overhead**: The factor $f_{\text{orch}}$ captures control‑stack energy; its value depends on software stack design and must be profiled.  
* **Precision format**: The analysis assumes double‑precision complex numbers (16 bytes per entry). Using single precision would halve memory and energy but alter the benchmark definition.

### (e) Order‑of‑magnitude cost and performance bounds (projections)
Assuming a DRAM cost of \$0.05 per GB and a node with 256 GiB RAM, the memory cost for a 10‑qubit mixed‑state simulation is approximately:
\[
\text{Memory cost} \approx \frac{16\ \text{MiB}}{1024\ \text{MiB/GB}} \times \$0.05 \approx \$0.00078.
\]
The projected energy per $10^{4}$‑step workload is $33.55$ J. On a server with a 500 W power envelope, this corresponds to a runtime of $0.067$ s, i.e., negligible compared to the memory cost but indicative of the scaling trend as $n$ grows.

### (f) Direct risks and misuse paths
* **Overreliance on the benchmark**: Treating the composite score as an absolute performance metric could discourage exploration of algorithmic techniques (e.g., tensor‑network compression) that break the $R_n$ scaling.  
* **Misinterpretation of projections**: The DRAM‑energy coefficient is a modeling assumption; using the projected energy values as design specifications without empirical validation could lead to under‑provisioned power supplies.  
* **Benchmark fixation**: Future works might tune simulators to minimize $\Sigma$ without improving actual scientific capability, leading to “benchmark‑gaming” rather than genuine performance gains.

## 8. Conclusion
We have introduced a rigorously anchored benchmark for mixed‑state quantum simulation workloads. By leveraging the exact entanglement‑cost results for two‑Bell‑state mixtures [5], deriving a closed‑form memory‑overhead factor $R_n=2^{n}$, and projecting energy consumption under a three‑layer model [10], the specification provides a transparent, quantitative baseline. The benchmark highlights the dramatic memory increase (factor $2^{n}$) and non‑trivial energy cost associated with mixed‑state simulation, thereby informing hardware procurement, algorithm design, and future benchmark development. Extensions to richer mixed‑state families and empirical validation of the modeling coefficients constitute clear next steps.

## References
[1] arXiv:2108.10792v1 | Hilbert Complexes with Mixed Boundary Conditions -- Part 2: Elasticity Complex  
[2] arXiv:2610.06654v1 | Continuous-Time Estimation-Aware Optimal Control of Mobile Sensors for Target Tracking  
[3] arXiv:math/0306324v1 | Ullemar's formula for the Jacobian of the complex moment mapping  
[4] arXiv:2207.11778v3 | Hilbert Complexes with Mixed Boundary Conditions -- Part 3: Biharmonic Complexes  
[5] arXiv:quant-ph/0112131v4 | Entanglement cost of mixed states  
[6] arXiv:2106.03448v6 | Hilbert Complexes with Mixed Boundary Conditions -- Part 1: De Rham Complex  
[7] arXiv:2112.12972v2 | Holomorphic maps from complex discs intersecting families of hypersurfaces  
[8] arXiv:1612.04764v1 | Cohomological aspects on complex and symplectic manifolds  
[9] QNFO: QuWARP Reconciled: An Analytical Cost-Model Assessment of Workload-Level Reuse Planning for Quantum Circuit Simulation  
[10] QNFO: Thermodynamic Budgeting for Hybrid Quantum-Classical Computing: A Three-Layer Energy Model with Explicit Arithmetic and a 15-Month Validation Roadmap  

## Appendix A. Divergence report
*No divergent claims were identified among the independent drafts; all substantive statements converged.*

## Appendix B. Claim attribution
| ID | Claim | Source drafts | Agreement |
|----|-------|---------------|-----------|
| C1 | Mixed‑state workloads dominate modern quantum‑simulation use cases. | A, B, C | Convergent |
| C2 | Entanglement cost of two‑Bell‑state mixtures equals entanglement of formation via additivity. | A, B, C | Convergent |
| C3 | $E_F(\rho_{0.5})=1.000000$ ebits. | A, B, C | Convergent |
| C4 | $E_F(\rho_{0.25})=0.811278$ ebits. | A, B, C | Convergent |
| C5 | $E_F(\rho_{0.9})=0.468996$ ebits. | A, B, C | Convergent |
| C6 | $\frac{dE_F}{dp}\big|_{p=0.5}=0$. | A, B, C | Convergent |
| C7 | Representation overhead $R_n=2^{n}$. | A, B, C | Convergent |
| C8 | $R_{10}=1024$ and memory ratio 16 MiB vs 16 KiB. | A, B, C | Convergent |
| C9 | Sweep footprint $352{,}321{,}536$ bytes for $K=21$, $n=10$. | A, B, C | Convergent |
| C10 | Composite score $\Sigma(10)=778.333$ weighted ebit‑units. | A, B, C | Convergent |
| C11 | Energy per step $3.3554432\times10^{-3}$ J under assumptions. | A, B, C | Convergent |
| C12 | Energy for $10^{4}$ steps $33.554432$ J. | A, B, C | Convergent |
| C13 | Limitations: anchor family, weighting convention, energy coefficients, full density‑matrix assumption. | A, B, C | Convergent |
| C14 | Practical users: quantum‑software developers, HPC architects, benchmark designers. | A, B, C | Convergent |
| C15 | TRL level statement (TRL 2). | A, B, C | Convergent |
| C16 | Minimal next experiment: implement 10‑qubit density‑matrix simulator and measure memory/energy. | A, B, C | Convergent |
| C17 | Engineering constraints: memory capacity, DRAM coefficient, orchestration factor, precision format. | A, B, C | Convergent |
| C18 | Order‑of‑magnitude cost projection for 10‑qubit memory ($\$0.00078$). | A, B, C | Convergent |
| C19 | Risks of overreliance and misuse. | A, B, C | Convergent |