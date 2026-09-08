# RECONCILIATION — cycle-1

Reconciling agent: parent session (2026-09-08). Writers: a, b, c (knowledge-only drafts; child
sessions were tool-blocked at the frozen View ceiling, so citations were flagged unverified and
drafts materialized verbatim by the parent — see MANIFEST.json).

Input block: cycle-1/SHARED-PROMPT.md (sha256 b5369c0085d067de78948fbe390d26014255b61510db217eb6dfe09596bc5709).
Method: full read of all three drafts; claim extraction; convergence/divergence classification;
synthesis into reconciled-paper.md; every claim below cites its source draft + section.

## Claim-attribution table (master claims -> source drafts)

| # | Master claim | Sources | Agreement |
|---|---|---|---|
| M1 | ML bound: E >= πħ/(2τ); 1.66e-28 J at 1 μs clock | a §2, b §2.1, c §2 | CONVERGENT (all three; b and c note h-form equivalence) |
| M2 | Landauer: kT ln2 per erased bit; 2.87e-21 / 3.83e-23 / 1.91e-25 J at 300K/4K/20mK | a §2, b §2.2, c §2 | CONVERGENT (arithmetic identical) |
| M3 | Combined floor = max(πħ/2τ, kT ln2 · N_irr); ML dominates only below ~58 fs at 300 K | a §2, b §2.3, c §2 | CONVERGENT (crossover 58 fs / 4.3 ps) |
| M4 | QEC is classically irreversible: syndrome rounds erase ~d^3-2d^3 bits per logical op | a §2, b §2.2, c §2 | CONVERGENT (bit counts differ: a per-round 1.4e3, b/c 2.7e4-5e4 over d rounds) |
| M5 | Landauer bookkeeping floor ~1e-18 J per logical op at 4 K (a: 5.4e-20 per round) | a §2, b §2.2, c §2 | CONVERGENT (within the round-counting convention of M4) |
| M6 | Physics floors are 16-18 orders below engineering reality; energy problem is engineering, not physics | a §4/§7, b §2.3, c §2 | CONVERGENT (the headline result) |
| M7 | Physical overhead: ~2.25-2.8M qubits for 1,000 logical at d ≈ 27-30, p ≈ 1e-3 | a §3, b §3.1, c §3 | CONVERGENT (2.8M / 1.3-2.4M / 2.25M; see D2) |
| M8 | Wall power: central ~10 MW, range ~1-50 MW | a §4, b §3.2, c §3 | PARTIAL (a 1-10, b 10-50 midpoint 20, c 0.1-100 central 10; see D3) |
| M9 | Dominant terms: cryogenic refrigeration + control/readout electronics; decoder ~1 order below; coherent physics ~5+ orders below | a §4, b §3.3, c §3 | CONVERGENT (a ranks cooling first, c ranks control ≈ cryogenics jointly) |
| M10 | J/LO: ~2 mJ (a) vs ~1 J (b, c) — resolved as a convention difference (see D1) | a §4, b §3.3, c §3 | DIVERGENT — root-caused and resolved in D1 |
| M11 | Gap to floor: E_actual/E_floor ≈ 1e16-1e18 vs Landauer; ≈ 1e24-1e25 vs ML | a §4, b §3.3, c §3 | CONVERGENT (a: 1e16 Landauer / 1e25 ML; b: 1e16-1e18; c: 18-20 orders) |
| M12 | JPCUB 2026 revision: joules per logical operation at declared (p_L, d) as headline; per-logical-qubit normalization; physical-gate count demoted | a §5, b §4, c §4 | CONVERGENT (three independent writers reached nearly identical proposals) |
| M13 | Companion metrics: decoder energy share, cryogenic overhead factor, gap-to-floor ratio, idle-power handling, error-rate ladder | a §5, b §4, c §4 | CONVERGENT (see D4 on η convention) |
| M14 | Falsifiers: cryo-CMOS μW/channel (-1e2), photonic links, decoder >1 μJ/bit, p ≈ 1e-2 → d ≈ 50, round-time sensitivity | a §6, b §5, c §5 | CONVERGENT (independently overlapping lists) |
| M15 | Platform-transfer limit: numbers apply to superconducting surface-code machines only | a §6, b §5, c §5 | CONVERGENT |

## Divergences (reported, never silently resolved)

### D1 — Logical-operation definition (the central divergence)
- a: one logical operation ≈ one syndrome round (0.5-2 μs) → J/LO ≈ 0.5-20 mJ (central 2 mJ).
- b: logical Clifford = ~d syndrome cycles (~30 μs) → J/LO ≈ 0.1-10 J (midpoint 1 J).
- c: lattice surgery over ~3d cycles (30-100 μs) → J/LO ≈ 0.01-10 J (central ~1 J).
- Resolution (state-of-the-world): both are consistent given their conventions; the disagreement is
  about what counts as a logical operation. The reconciled paper reports a convention-free primitive —
  joules per syndrome round per logical qubit (≈ 5-20 mJ, central 10 mJ) — plus J/LO under the
  explicit d-rounds convention (≈ 0.1-1 J central). Question flagged as definitionally open for the
  benchmark program to standardize.

### D2 — Physical overhead formula
- a uses the unrotated (2d-1)^2 = 2,809 at d=27; b uses 2d^2 = 1,800 at d=30; c uses 2.5d^2 = 2,250
  at d=30. These are different planar/rotated conventions; reconciled paper cites the range
  2.25-2.8M at d ≈ 27-30 and notes the formula dependence.

### D3 — Wall-power midpoint
- a: 1-10 MW; b: 10-50 MW (midpoint 20 MW); c: 0.1-100 MW (central 10 MW). Difference driven by
  cooling realization factors (a 300-700 W/W; b 300-1000 W/W + separate mK stage) and control-power
  assumptions. Reconciled paper reports central 10 MW, range 1-50 MW, and keeps the term-level table.

### D4 — Gap-ratio convention (η)
- b defines η = E_actual/E_floor ≈ 1e16-1e18 (overhead ratio, falls with progress).
- c defines η = E_floor/E_actual ≈ 1e-18 (efficiency ratio, rises with progress).
- Resolution: the reconciled paper standardizes η = E_actual/E_floor (b's convention; matches a's
  "gap-to-floor" usage) and explicitly deprecates the inverse form to avoid sign-of-progress confusion.

### D5 — Citation defects (found in parent verification, see citation-audit.md)
- writer-c ref 3: arXiv:1203.1212 is an unrelated paper; corrected to DOI 10.1038/nature10872.
- writer-a ref 5: Auffeves title corrected to "...Quantum Energy Initiative".

## Ensemble-method confounds (adversarial self-assessment)

1. **Model-twin contamination (REAL, undisclosed in cycle-1):** all three writers were child sessions
   of the same underlying model family; independence here is contextual (disjoint sessions, no
   cross-talk, byte-identical input), not cross-model. Convergence therefore measures
   context-independence, not model diversity. Planned cycle-2 improvement: legs on distinct models
   (e.g. deepseek-v4-flash / glm-4.7-flash / qwen3-30b via the qnfo-ai gateway).
2. **Tool-access asymmetry:** writers had zero tool access (all numbers from model knowledge);
   the parent verified citations post hoc. Knowledge-only drafts systematically under-source their
   quantitative claims — visible in the low confidence labels on M7-M10.
3. **Prompt-echo bias:** identical input block guarantees stylistic/conceptual priming; divergence
   therefore underestimates what unprimed independent groups would produce.
4. **Single reconciler:** the synthesis is one agent's judgment; mitigated by the verbatim draft
   archive + claim table so any reader can re-derive the synthesis.

## Convergent findings (the signal)

Three independent writers converged on: (1) the physics floor is ~16-18 orders below engineering
reality (ML never binding; Landauer on QEC bookkeeping ~1e-18 J/op); (2) dominant energy terms are
cryogenic refrigeration and control electronics, with decoding secondary and coherent physics
negligible; (3) an essentially identical six-point JPCUB 2026 revision (J/LO headline at declared
p_L and d, per-logical-qubit normalization, physical-gate demotion, companion metrics); (4) nearly
the same falsification list. Convergence on the benchmark proposal is the pilot's strongest result.

