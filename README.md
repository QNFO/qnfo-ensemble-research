# QNFO Ensemble Research

Pilot program (user directive 2026-09-08): writing multiple SEPARATE papers around the same
theme/title/questions independently, then reconciling and publishing with full provenance,
all artifacts, collateral files, and interim/intermediate drafts.

**Protocol (governance):** https://github.com/QNFO/qnfo-ops/blob/main/docs/ENSEMBLE-RESEARCH-PILOT.md

## Cycles

| cycle | theme | writers | status |
|-------|-------|---------|--------|
| cycle-1 | Energy floor of fault-tolerant quantum computing at the 1,000-logical-qubit scale | a, b, c | in progress (due 2026-09-10) |

## Repository layout

`cycle-N/`
  `SHARED-PROMPT.md`    - byte-identical input block (title + questions + constraints)
  `MANIFEST.json`       - sha256 of every artifact (provenance manifest)
  `RECONCILIATION.md`   - claim-attribution table + reported divergences
  `writer-<id>/`        - independent interim drafts (never modified after collection)
  `reconciled-paper.md` - final paper

## Independence rules (writers)

- Isolated sessions; no cross-communication; no sibling-directory reads.
- Only real, verifiable sources (arXiv IDs / DOIs). Fabrication = HARD finding.
- Write only inside your own `writer-<id>/` directory. No git operations.
