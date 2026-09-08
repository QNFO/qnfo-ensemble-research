# claims.md — writer-b claims table, cycle 1

| # | Claim | Evidence | Confidence |
|---|---|---|---|
| C1 | Margolus–Levitin: orthogonal evolution requires E·t ≥ πħ/2; per-op floor ≈ 5.5e-30 J at τ = 30 μs | Textbook result; arithmetic self-checked; source arXiv:quant-ph/9710043 cited [UNVERIFIED] | Medium (physics), Unverified (citation) |
| C2 | Landauer bound: E ≥ kT ln 2 per erased bit | Established result (1961); cited [UNVERIFIED] | Medium (physics), Unverified (citation) |
| C3 | QEC erases ~d³–2d³ classical bits per logical op (surface code, ~2d² physical qubits, ~d cycles) | Standard surface-code structure; own counting; no source verified | Low-medium |
| C4 | Landauer floor for QEC bookkeeping ≈ 1e-18–1e-16 J per logical op (4 K / 300 K, d=30) | Product of C3 × kT ln 2; arithmetic self-checked | Low-medium |
| C5 | Combined floor = max(πħ/2τ, kT ln 2 · N_irr); Landauer term dominates by 12–14 orders | Derivation in §2.3; follows from C1–C4 | Medium |
| C6 | Practical energy ≈ 0.1–10 J per logical op (midpoint ~1 J) at 1,000 logical qubits | Own order-of-magnitude budget (Table 1); no source verified | Low |
| C7 | Physical qubits ≈ 1.3–2.4e6 at d = 25–35 for p_L ≈ 1e-12, p ≈ 1e-3 | Own scaling estimate; Willow below-threshold cited as motivation [UNVERIFIED] | Low |
| C8 | Wall power ≈ 10–50 MW (midpoint ~20 MW); dominant term = cryogenic control + cooling | Sum of Table 1 ranges; cooling factors from prior knowledge [UNVERIFIED sources] | Low |
| C9 | Overhead vs Landauer floor ≈ 1e16–1e18 | Ratio of C6 to C4 | Low-medium |
| C10 | ML bound is never the binding constraint in FTQC; the floor is engineering, not physics | Argument in §2.1, §2.3; falsifiable via C6 collapse if cryo-CMOS reaches μW/channel | Medium |
| C11 | Headline benchmark metric should be J/QLOP at declared (p_L, d), with Landauer-overhead ratio as efficiency index | Proposal §4; no external evidence (design recommendation) | Medium (recommendation), n/a (empirical) |
| C12 | Physical-gate-count normalization conflates d² overhead with progress | Argument §4.5; follows from C7 scaling | Medium |
| C13 | All 11 references real and correctly attributed | NONE — blocked environment; all marked [UNVERIFIED - needs parent check] | Unverified |

Honesty note: rows C6–C8 are the load-bearing quantitative claims and are the
least verified. They are stated as ranges with explicit assumptions precisely
so that source verification by the parent can tighten them without breaking
the draft's structure.
