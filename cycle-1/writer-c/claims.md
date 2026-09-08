# Claims — WRITER-C, cycle 1

| # | Claim | Evidence | Confidence |
|---|-------|----------|------------|
| 1 | Margolus–Levitin: t⊥ ≥ h/(4E), so E ≥ h/(4τ) ≈ 1.7e-28 J for τ = 1 μs | Model knowledge of the theorem; arXiv:quant-ph/9710043 [UNVERIFIED] | High (derivation); citation unverified |
| 2 | Landauer: k_B T ln 2 per erased bit (2.9e-21 J @300K, 3.8e-23 J @4K, 1.9e-25 J @20mK) | Model knowledge; Landauer 1961 + arXiv:1203.1212 [UNVERIFIED] | High (derivation); citations unverified |
| 3 | ML dominates Landauer only for τ < ~58 fs @300K (~4.3 ps @4K); at μs cycle times Landauer dominates | Arithmetic from claims 1–2 | High |
| 4 | Distance-30 logical op erases ~2.7e4 ancilla bits → Landauer floor ~1e-18 J/op @4K (~5e-21 J @20mK) | Architecture estimate (d² ancillas × d rounds); no source | Medium (order-of-magnitude) |
| 5 | p_L ≤ 1e-10 needs d ≈ 19–28 at p/p_th = 0.1–0.2; engineering d ≈ 30 | Standard phenomenological scaling [UNVERIFIED: arXiv:1208.0928] | Medium |
| 6 | 1,000 logical qubits at d=30 ≈ 2.25e6 physical qubits (range 1–3e6) | 2.5d² overhead rule [UNVERIFIED: arXiv:1208.0928] | Medium |
| 7 | Fleet logical throughput ≈ 1e7 logical ops/s (τ_c ≈ 1 μs, 30–100 μs/logical gate) | Cycle time [UNVERIFIED: arXiv:2408.13687]; arithmetic | Medium |
| 8 | Full-system wall power ≈ 10 MW central (range 0.1–100 MW); control ≈ cryogenics > decoding ≫ coherent physics | Order-of-magnitude budget, Section 3 of draft; no published full-stack budget found (couldn't search) | Low |
| 9 | ≈ 1 J per logical operation (range 0.01–10 J); ≈ 10 kWh per logical-qubit-hour | Claim 8 ÷ claim 7 | Low |
| 10 | Thermodynamic gap η = E_floor/E_actual ≈ 1e-18 (18–20 orders) | Claims 4 and 9 | Low–Medium |
| 11 | Proposed benchmark headline (J/op_L at p_L=1e-10) is an improvement over per-physical-gate normalization | Argument in Section 4; benchmark repo state unverified [UNVERIFIED: github.com/rwnq8/joules-per-compute-benchmark] | Medium (argument); Low (fit to current benchmark state) |
| 12 | Falsification conditions listed (per-channel <1 W power budget → est. falsified downward; p ≈ 1e-2 → d≈50 → est. falsified upward; >1 μJ/syndrome-bit decoder → dominance ranking overturned) | Constructed from the budget's sensitivities | Medium (logical; empirically untested) |
| 13 | All arXiv IDs in References exist and are correctly attributed | Model knowledge only; zero verifications possible this session | Low — ALL need parent verification |

**Global note:** no claim in this table was verified with any tool this session (frozen View ceiling blocked all subtools). "High (derivation)" refers only to the internal arithmetic of well-known theorems; "citation unverified" applies to every reference.
