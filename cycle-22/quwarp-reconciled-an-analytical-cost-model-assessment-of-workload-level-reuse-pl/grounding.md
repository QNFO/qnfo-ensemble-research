# Grounding block - source: 951436b5-24af-41b7-849e-44e27a2f1217

## Research idea

QuWARP: A Workload-Aware Reuse Planner for simulating Quantum Circuits — arXiv 2609.23664v1. Auto-candidate from daily research scan; triage for QNFO research fit.

## Existing paper under revision (remediation only)

(none - new paper)

## Source material (fetched from arXiv)

TITLE: arXiv Query: search_query=&amp;id_list=2609.23664&amp;start=0&amp;max_results=1

ABSTRACT: Quantum circuit simulation often appears as repeated-run workloads rather than isolated circuits: variational quantum eigensolver (VQE) sweeps, noisy multishot studies, and quantum error correction (QEC) cycles revisit closely related structure across many runs. Existing simulators optimise individual executions well, but they largely ignore cross-task shared state and therefore repeat work that could be reused safely. We propose QuWARP, a planner-based workload optimiser for a bounded state of the art simulator execution surface: it performs workload-level planning over related tasks, identifies shared prefixes, and chooses when to materialize exact typed boundary artifacts for later reuse across the evaluated statevector mode, and stabilizer-hybrid mode. Its planner treats continuation legality as a narrow correctness guardrail, abstains when reuse is unprofitable, and keeps each reuse, abstention, or refusal decision auditable through EXPLAIN-style traces, meaning inspectable planner reports with provenance and realized-cost summaries. Across real world quantum application workloads QuWARP delivers 2.95x-32.84x speedups over this work's main direct per-task Qrack denominator on reuse-positive workloads. These results show workload-level reuse planning improves repeated-run simulation while keeping unsupported handoffs auditable and out of the execution path.

## Related literature (arXiv, real identifiers)

arXiv:2609.23664v1 | QuWARP: A Workload-Aware Reuse Planner for simulating Quantum Circuits
  Quantum circuit simulation often appears as repeated-run workloads rather than isolated circuits: variational quantum eigensolver (VQE) sweeps, noisy multishot studies, and quantum error correction (QEC) cycles revisit closely related structure across many runs. Existing simulators optimise individual executions well, but they largely ignore cross-task shared state and therefore repeat work that c
arXiv:1905.09692v3 | Structure optimization for parameterized quantum circuits
  We propose an efficient method for simultaneously optimizing both the structure and parameter values of quantum circuits with only a small computational overhead. Shallow circuits that use structure optimization perform significantly better than circuits that use parameter updates alone, making this method particularly suitable for noisy intermediate-scale quantum computers. We demonstrate the met
arXiv:2006.16817v2 | Proof of monotonic increase in the cost function for Krotov algorithm for open quantum systems
  A great number of quantum control papers have used one of the variants of the monotonically convergent variational control algorithm of Krotov (as described in Maday and Turinici (2003), Tannor et al. (1992), Zhu and Rabitz (1998), etc). The paper "Speeding up Thermalisation via Open Quantum System Variational Optimisation" by N, Suri, et al. [EPJST 227, 203 -216 (2018), arXiv:1711.08776] provides
arXiv:1304.1836v2 | A Simulation and Modeling of Access Points with Definition Language
  This submission has been withdrawn by arXiv administrators because it contains fictitious content and was submitted under a pseudonym, which is against arXiv policy.
arXiv:2407.04826v1 | Multi-strategy Based Quantum Cost Reduction of Quantum Boolean Circuits
  The construction of quantum computers is based on the synthesis of low-cost quantum circuits. The quantum circuit of any Boolean function expressed in a Positive Polarity Reed-Muller $PPRM$ expansion can be synthesized using Multiple-Control Toffoli ($MCT$) gates. This paper proposes two algorithms to construct a quantum circuit for any Boolean function expressed in a Positive Polarity Reed-Muller
arXiv:2106.13995v1 | Fast quantum circuit simulation using hardware accelerated general purpose libraries
  Quantum circuit simulators have a long tradition of exploiting massive hardware parallelism. Most of the times, parallelism has been supported by special purpose libraries tailored specifically for the quantum circuits. Quantum circuit simulators are integral part of quantum software stacks, which are mostly written in Python. Our focus has been on ease of use, implementation and maintainability w
arXiv:1712.02806v3 | From estimation of quantum probabilities to simulation of quantum circuits
  Investigating the classical simulability of quantum circuits provides a promising avenue towards understanding the computational power of quantum systems. Whether a class of quantum circuits can be efficiently simulated with a probabilistic classical computer, or is provably hard to simulate, depends quite critically on the precise notion of "classical simulation" and in particular on the required
arXiv:1610.03438v2 | Introduction to Quantum Electromagnetic Circuits
  The article is a short opinionated review of the quantum treatment of electromagnetic circuits, with no pretension to exhaustiveness. This review, which is an updated and modernized version of a previous set of Les Houches School lecture notes, has 3 main parts. The first part describes how to construct a Hamiltonian for a general circuit, which can include dissipative elements. The second part de

## QNFO corpus context (Vectorize)

QNFO: TETRIS-Q: Tiling-based Effective Transient-fault Reduction and Parallelism Optimizations for Quantum Circuit Mapping | DOI 10.5281/zenodo.22739633
  Quantum circuit mapping on Noisy Intermediate-Scale Quantum (NISQ) devices must satisfy physical connectivity constraints while minimizing both SWAP overhead and exposure to transient faults like decoherence. Existing compilers typically optimize qubit routing and noise-aware placement independently
QNFO: QWAV Strategy v2.4.1: The Energy-Standard Playbook — Consortium Governance, Verified Precedents, and the JPCUB Road to a Quantum Computing Energy Benchmark | DOI 10.5281/zenodo.21978952
  QWAV Quantum Software possesses a validated technical differentiator in JPCUB, but the SaaS go-to-market model carries a structural weakness. This paper proposes the JPCUB Consortium model combined with grant-funded core R&D, transforming JPCUB from a single-vendor product into a multi-stakeholder s
QNFO: JPCUB Competitive Landscape v2.0: System-Level Joules-per-Solution Estimates for 17 Quantum Computing Platforms from Published Specifications | DOI 10.5281/zenodo.21821767
  The JPCUB P0 protocol (DOI 10.5281/zenodo.21637028) defines the joules-per-solution metric — total system energy per correct answer — as a universal, physics-grounded benchmark for computational platforms. The qwav.tech competitive landscape displays six platforms with one published measurement (IBM
QNFO: Due Diligence Report: QuiX Quantum | DOI 10.5281/zenodo.21515894
  Multi-source due diligence assessment of QuiX Quantum (Enschede, NL), the European market leader in photonic quantum computing.

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] TITLE: arXiv Query: search_query=&amp;id_list=2609.23664&amp;start=0&amp;max_results=1

ABSTRACT: Quantum circuit simulation often appears as repeated-run workloads rather than isolated circuits: variational quantum eigensolver (VQE) sweeps, noisy multishot studies, and quantum error correction (QEC) cycles revisit closely related structure across many runs. Existing simulators optimise individual executions well, but they largely ignore cross-task shared state and therefore repeat work that could be reused safely. We propose QuWARP, a planner-based workload optimiser for a bounded state of the art simulator execution surface: it performs workload-level planning over related tasks, identifies shared prefixes, and chooses when to materialize exact typed boundary artifacts for later reuse across the evaluated statevector mode, and stabilizer-hybrid mode. Its planner treats continuation legality as a narrow correctness guardrail, abstains when reuse is unprofitable, and keeps each reuse, abstention, or refusal decision auditable through EXPLAIN-style traces, meaning inspectable planner reports with provenance and realized-cost summaries. Across real world quantum application workloads
[2] arXiv:2609.23664v1 | QuWARP: A Workload-Aware Reuse Planner for simulating Quantum Circuits
  Quantum circuit simulation often appears as repeated-run workloads rather than isolated circuits: variational quantum eigensolver (VQE) sweeps, noisy multishot studies, and quantum error correction (QEC) cycles revisit closely related structure across many runs. Existing simulators optimise individual executions well, but they largely ignore cross-task shared state and therefore repeat work that c
[3] arXiv:1905.09692v3 | Structure optimization for parameterized quantum circuits
  We propose an efficient method for simultaneously optimizing both the structure and parameter values of quantum circuits with only a small computational overhead. Shallow circuits that use structure optimization perform significantly better than circuits that use parameter updates alone, making this method particularly suitable for noisy intermediate-scale quantum computers. We demonstrate the met
[4] arXiv:2006.16817v2 | Proof of monotonic increase in the cost function for Krotov algorithm for open quantum systems
  A great number of quantum control papers have used one of the variants of the monotonically convergent variational control algorithm of Krotov (as described in Maday and Turinici (2003), Tannor et al. (1992), Zhu and Rabitz (1998), etc). The paper "Speeding up Thermalisation via Open Quantum System Variational Optimisation" by N, Suri, et al. [EPJST 227, 203 -216 (2018), arXiv:1711.08776] provides
[5] arXiv:1304.1836v2 | A Simulation and Modeling of Access Points with Definition Language
  This submission has been withdrawn by arXiv administrators because it contains fictitious content and was submitted under a pseudonym, which is against arXiv policy.
[6] arXiv:2407.04826v1 | Multi-strategy Based Quantum Cost Reduction of Quantum Boolean Circuits
  The construction of quantum computers is based on the synthesis of low-cost quantum circuits. The quantum circuit of any Boolean function expressed in a Positive Polarity Reed-Muller $PPRM$ expansion can be synthesized using Multiple-Control Toffoli ($MCT$) gates. This paper proposes two algorithms to construct a quantum circuit for any Boolean function expressed in a Positive Polarity Reed-Muller
[7] arXiv:2106.13995v1 | Fast quantum circuit simulation using hardware accelerated general purpose libraries
  Quantum circuit simulators have a long tradition of exploiting massive hardware parallelism. Most of the times, parallelism has been supported by special purpose libraries tailored specifically for the quantum circuits. Quantum circuit simulators are integral part of quantum software stacks, which are mostly written in Python. Our focus has been on ease of use, implementation and maintainability w
[8] arXiv:1712.02806v3 | From estimation of quantum probabilities to simulation of quantum circuits
  Investigating the classical simulability of quantum circuits provides a promising avenue towards understanding the computational power of quantum systems. Whether a class of quantum circuits can be efficiently simulated with a probabilistic classical computer, or is provably hard to simulate, depends quite critically on the precise notion of "classical simulation" and in particular on the required
[9] arXiv:1610.03438v2 | Introduction to Quantum Electromagnetic Circuits
  The article is a short opinionated review of the quantum treatment of electromagnetic circuits, with no pretension to exhaustiveness. This review, which is an updated and modernized version of a previous set of Les Houches School lecture notes, has 3 main parts. The first part describes how to construct a Hamiltonian for a general circuit, which can include dissipative elements. The second part de
[10] QNFO: TETRIS-Q: Tiling-based Effective Transient-fault Reduction and Parallelism Optimizations for Quantum Circuit Mapping | DOI 10.5281/zenodo.22739633
  Quantum circuit mapping on Noisy Intermediate-Scale Quantum (NISQ) devices must satisfy physical connectivity constraints while minimizing both SWAP overhead and exposure to transient faults like decoherence. Existing compilers typically optimize qubit routing and noise-aware placement independently
[11] QNFO: QWAV Strategy v2.4.1: The Energy-Standard Playbook — Consortium Governance, Verified Precedents, and the JPCUB Road to a Quantum Computing Energy Benchmark | DOI 10.5281/zenodo.21978952
  QWAV Quantum Software possesses a validated technical differentiator in JPCUB, but the SaaS go-to-market model carries a structural weakness. This paper proposes the JPCUB Consortium model combined with grant-funded core R&D, transforming JPCUB from a single-vendor product into a multi-stakeholder s
[12] QNFO: JPCUB Competitive Landscape v2.0: System-Level Joules-per-Solution Estimates for 17 Quantum Computing Platforms from Published Specifications | DOI 10.5281/zenodo.21821767
  The JPCUB P0 protocol (DOI 10.5281/zenodo.21637028) defines the joules-per-solution metric — total system energy per correct answer — as a universal, physics-grounded benchmark for computational platforms. The qwav.tech competitive landscape displays six platforms with one published measurement (IBM
[13] QNFO: Due Diligence Report: QuiX Quantum | DOI 10.5281/zenodo.21515894
  Multi-source due diligence assessment of QuiX Quantum (Enschede, NL), the European market leader in photonic quantum computing.