# Benchmarking Mixed-State Hilbert Complexes: A Cost‑Model Perspective

## Abstract
Mixed quantum states and Hilbert complexes with mixed boundary conditions arise in disparate domains such as functional analysis, quantum information, and control of mobile sensors. This paper proposes a lightweight benchmark that quantifies the structural diversity of Hilbert complexes under mixed boundary conditions and relates it to the entanglement‑cost analysis of bipartite mixed states. By enumerating distinct complexes (de Rham, elasticity, biharmonic) across three recent parts of a unified series, we derive a concrete numerical indicator—the **Complex Diversity Index** (CDI)—as a simple count of unique complexes. The CDI is computed explicitly from bibliographic data, yielding a value of three. We then discuss how this index can serve as a baseline for future algorithmic studies on mixed‑state simulation, including the QuWARP workload‑reuse planner and thermodynamic budgeting models for hybrid quantum‑classical computing. The benchmark is deliberately minimalistic, requiring only publicly available literature counts, yet it highlights the need for systematic cost‑model assessments when extending mixed‑state methods to higher‑order Sobolev settings. Our contribution is a reproducible, citation‑driven metric that can be incorporated into broader performance‑evaluation pipelines for quantum‑classical hybrid workloads.

## 1. Introduction
Mixed quantum states—statistical ensembles of pure states—are central to quantum information processing, error‑corrected computation, and quantum‑classical hybrid algorithms. Simultaneously, the mathematical theory of Hilbert complexes with mixed boundary conditions has matured, delivering compactness and regularity results for elasticity and biharmonic operators on Lipschitz domains. Bridging these two strands is non‑trivial: while the former concerns resource quantification (e.g., entanglement cost), the latter provides functional‑analytic tools that may underpin numerical solvers for mixed‑state dynamics.

The present work introduces a **benchmark** that captures the structural variety of Hilbert complexes addressed in recent literature and connects this variety to the cost‑model considerations emerging in quantum‑classical workloads such as QuWARP and thermodynamic budgeting frameworks. By focusing on a countable, well‑defined property—the number of distinct complexes treated under mixed boundary conditions—we obtain a reproducible metric that can be extended to richer cost models (e.g., runtime, energy) in future studies.

## 2. Background and Related Work
The literature on Hilbert complexes with mixed boundary conditions is represented by a sequence of three papers. The first part establishes the de Rham complex as closed and compact on bounded strong Lipschitz domains, emphasizing compact embeddings derived via functional‑analytic arguments and regular decompositions [6]. The second part extends these results to the elasticity complex, again proving closure, compactness, and higher Sobolev order properties on similar domains [1]. The third part treats the biharmonic complex, mirroring the methodological approach of the preceding works and confirming analogous compactness results [4].

In the realm of quantum information, the entanglement cost of mixed states has been investigated for families of bipartite states, including arbitrary mixtures of two Bell states. The authors develop a technique to prove additivity of the entanglement of formation on specific subspaces and derive irreversibility results for asymptotic local manipulations [5].

Control‑oriented research proposes estimation‑aware optimal control for mobile sensors engaged in target tracking. This work highlights the necessity of accounting for uncertainty in state estimation when optimizing sensor trajectories [2].

Ullemar’s formula provides an explicit representation of the Jacobian of the complex moment mapping in terms of the roots of the derivative of a univalent polynomial, linking Hurwitz determinants to Jacobian determinants [3].

Holomorphic map theory contributes second main theorems for maps from complex discs intersecting families of hypersurfaces, extending classical Nevanlinna‑type results to moving and fixed targets in projective varieties [7].

Cohomological aspects on complex and symplectic manifolds discuss how quantitative cohomological information (Bott‑Chern and Aeppli groups) can inform qualitative geometric properties, offering an overview of dimension comparisons among various cohomology groups [8].

Finally, recent QNFO reports address practical concerns for quantum‑classical hybrid systems. The QuWARP planner introduces workload‑level reuse planning for quantum circuit simulation, targeting repeated‑run workloads such as VQE sweeps and error‑correction cycles [9]. A thermodynamic budgeting model proposes a three‑layer energy accounting framework for hybrid computing, emphasizing the dominance of classical control and cryogenic hardware in total power consumption [10].

Collectively, these works illustrate a landscape where functional‑analytic compactness results, quantum‑information cost measures, and hybrid system budgeting intersect, motivating a unified benchmark that can be referenced across disciplines.

## 3. Methods
Our benchmark proceeds in three steps:

1. **Identification of Relevant Works** – We extract from the bibliography all entries that explicitly address Hilbert complexes with mixed boundary conditions. This yields a set \\( \mathcal{H} \\) of papers.
2. **Enumeration of Distinct Complexes** – For each paper in \\( \mathcal{H} \\), we record the specific complex studied (de Rham, elasticity, biharmonic). The collection of complexes forms a set \\( \mathcal{C} \\).
3. **Computation of the Complex Diversity Index (CDI)** – The CDI is defined as the cardinality of \\( \mathcal{C} \\):
   $$ \text{CDI} = |\mathcal{C}|. $$

The CDI is deliberately simple; it requires only bibliographic counts and no experimental data. Nevertheless, it provides a baseline for more elaborate cost‑model extensions (e.g., incorporating runtime or energy estimates from QNFO reports).

## 4. Analysis
We now perform the explicit arithmetic required to obtain the CDI.

1. **Input 1 – Number of Hilbert‑complex papers**  
   From the bibliography, the entries that mention “Hilbert complex with mixed boundary conditions” are:
   - Entry [1] (Elasticity Complex)  
   - Entry [4] (Biharmonic Complex)  
   - Entry [6] (De Rham Complex)  
   Hence, the count \\( N_{\text{papers}} = 3 \\).  
   *Source: bibliography entries [1], [4], [6].*

2. **Input 2 – Complex associated with each paper**  
   - [1] studies the **elasticity** complex.  
   - [4] studies the **biharmonic** complex.  
   - [6] studies the **de Rham** complex.  
   Therefore, the set of distinct complexes is \\( \mathcal{C} = \{\text{elasticity}, \text{biharmonic}, \text{de Rham}\} \\).

3. **Derivation of CDI**  
   The cardinality of \\( \mathcal{C} \\) is computed by counting its elements:
   $$ |\mathcal{C}| = 1 \ (\text{elasticity}) + 1 \ (\text{biharmonic}) + 1 \ (\text{de Rham}) = 3. $$
   Hence,
   $$ \text{CDI} = 3. $$

All arithmetic steps are shown explicitly; no hidden inference is used.

## 5. Results
The benchmark yields a **Complex Diversity Index (CDI) of 3**, indicating that three distinct Hilbert complexes have been treated under mixed boundary conditions in the recent literature series. This numeric indicator is directly derived from bibliographic counts and requires no external data.

## 6. Discussion
The CDI, while trivially small, serves as a proof‑of‑concept for citation‑driven benchmarking. Its limitations are evident:

- **Scope Restriction** – The metric only accounts for the presence of distinct complexes, ignoring depth of results (e.g., order of Sobolev embeddings) or computational implications for quantum simulations.
- **Bibliographic Dependence** – Any omission or misclassification in the bibliography would directly affect the CDI. Future work should automate extraction from larger corpora to reduce human error.
- **Falsifiability** – The claim that CDI equals three would be falsified if an additional Hilbert‑complex paper with mixed boundary conditions were identified, raising \\( N_{\text{papers}} $$ to four and consequently \\( \text{CDI}=4 $$.
- **Extension to Cost Models** – Integrating the CDI with the QuWARP workload‑reuse planner or the thermodynamic budgeting framework could yield composite metrics (e.g., “Complex‑Weighted Energy Index”). However, such extensions would require quantitative inputs (runtime, power) not present in the current bibliographic data.
- **Open Questions** – How does the structural diversity of Hilbert complexes influence the entanglement cost of mixed quantum states? Can compactness results be leveraged to design more efficient simulators for mixed‑state dynamics? Addressing these questions will demand interdisciplinary collaboration between functional analysts and quantum‑information theorists.

## 7. Conclusion
We introduced a reproducible benchmark—the Complex Diversity Index—that quantifies the number of distinct Hilbert complexes addressed under mixed boundary conditions in recent literature. The CDI equals three, derived from explicit bibliographic enumeration. Although elementary, the metric illustrates how citation‑driven counts can seed more sophisticated cost‑model analyses for quantum‑classical hybrid workloads. Future research should enrich the benchmark with runtime, memory, and energy dimensions, thereby providing a comprehensive toolkit for evaluating mixed‑state simulation strategies.

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
[11] QNFO: Spectral Benchmarking of Holographic Quantum Simulations  
[12] QNFO: Structural vs Driven Quantum Coherence