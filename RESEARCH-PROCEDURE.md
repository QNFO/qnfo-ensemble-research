# QNFO Autonomous Research Procedure (v1, 2026-09-09)

The single encoded procedure that BOTH the local (DeepChat) path and the autonomous
(Cloudflare worker) path must execute. Parity goal: a paper generated locally and a
paper generated autonomously are indistinguishable in structure, evidence, and rigor.
Any stage may be skipped only with a recorded rationale in the cycle manifest.

## Stage 0 - Idea intake
Sources: public edge form, idea-miner (research chat mining), arXiv auto-scan
(jobResearchScan, up to 5/day, h32 ip_hash dedupe). Every idea lands in
qnfo-audit.idea_proposals with triage score. No idea becomes a paper without a row.

## Stage 1 - Independent drafts (ensemble)
Three isolated writer legs, byte-identical SHARED-PROMPT, real-source-only rule
(fabrication = HARD finding), per-leg sha256 provenance in MANIFEST.json.
Outputs: cycle-N/writer-{a,b,c}/.

## Stage 2 - Adversarial citation audit + reconciliation
Every cited source resolved to a real arXiv ID / DOI; claim-attribution table in
RECONCILIATION.md; reconciled master.

## Stage 3 - Literature review + due diligence
Prior-work section with >=5 resolved references (arXiv ID or DOI). Adjacent-domain
scan (>=2 domains, CROSSWALK-TRANSLATION-1). Terminology bridge for domain terms.

## Stage 4 - Verify-in-code (COMPUTATIONAL-VERIFICATION-1)
Every quantitative claim carries a computation: deposited script, table, or explicit
derivation. Verification artifacts committed to the program repo and deposited with
the record.

## Stage 5 - Iteration
revise_count >= 1 before publish. Reviewer disagreement or depth-gap findings
(categories 7-9) trigger another cycle, never a surgical patch.

## Stage 6 - Publication quality gate
qnfo-research-exec publishV2 refuses rows failing ALL of: body >= 8000 chars;
lit-review section OR >=5 refs; >=1 verification marker (code fence/table/numeric).
Blocked rows -> version_queue status=gate-blocked + gov_gate_log + cloud_ops_events.
Escape hatch env QUALITY_GATE_OFF=1 (documented use only).

## Stage 7 - Publish + revision loop
Zenodo newversion deposit with full provenance (PUBLICATION SOURCE COMPLETENESS).
qnfo-paper-reviser depth audit: categories 1-9 incl. literature-coverage,
quantitative-justification, computational-verification (all HIGH severity).
Bodies < 8000 chars are auto-classified stub-fragment and NEVER version-bumped.

## Stage 8 - Artifact deposition
publishV2 deposits paper.md + README.md to
QNFO/qnfo-research/<program>/<slug>/ via GitHub contents API and inserts
publication_artifacts rows. Program mapping: programFor() (jpcub, silent-radix,
alpha-pi-helix, adelic-freedom, arithmetic-quantum-thermodynamics, margolus-levitin,
topological-spin, jpcub-qec, else papers/).

## Stage 9 - Quality score + quarantine feedback
qnfo-cloud-ops jobQualityScore (cron 20 4 * * * = 06:20 AMS daily) scores every
published paper (body_len, refs, lit, verif) into qnfo-audit.quality_scores.
score < 25 -> quarantine-candidate (review for quarantine); < 50 -> thin
(queued for substantive revision). Quarantined rows are excluded from
papers.qnfo.org by the gateway (status NOT IN (...,'quarantined')).

## Failure modes this procedure is designed against
- Stub publication (97-char v2.0.0 records): Stage 6 + Stage 7 stub-skip.
- Zero-citation flagships: Stage 3 minimum-refs + Stage 7 citation audit.
- Missing artifacts/GitHub: Stage 4 + Stage 8.
- Mechanical version bumps as "revision": Stage 5 depth categories.
