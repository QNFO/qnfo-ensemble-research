# notes.md — writer-b research trail, cycle 1

## Environment status: TOOL ACCESS BLOCKED

Three probes were dispatched; all subtools were refused synchronously by the
frozen View ceiling before any network I/O occurred:

1. `update_plan`  -> ToolCallError: "Tool 'update_plan' is outside the frozen View ceiling."
2. `arxiv-mcp-server_search_papers` -> same refusal (query: Margolus-Levitin).
3. `web_search` AND `write` -> same refusal for both.

This is the known CHILD-FROZEN-VIEW-1 environmental block (child sessions hit a
frozen View ceiling that refuses ALL tool calls at dispatch; delegation of
read-heavy and file-writing work to children is structurally ineffective in
this environment). Per working rule 5, this file documents the fallback.

## Searches run: ZERO (all blocked)

- arXiv searches intended: Margolus-Levitin; resource-constraints limitations
  paper; cryo-CMOS control power; scalable decoder micro-architecture;
  Willow below-threshold; 100-qubit cryogenic setups; photonic-link control;
  quantum-data-center power surveys.
- Web searches intended: dilution-refrigerator wall-power efficiency; Bardin
  JSSC 2019 DOI; Patra JSSC 2018 DOI.

## Sources found: ZERO verified live

Every reference in draft.md is from prior knowledge and is marked
[UNVERIFIED - needs parent check]. The parent ensemble MUST verify each arXiv
ID / DOI before any use. Priority verification list (highest risk first):

- arXiv:2001.06598 (Das et al. decoder) — moderate prior confidence.
- arXiv:1806.07862 (Krinner et al. cryo setups) — moderate-high.
- arXiv:2007.01966 (Fellous-Asiani et al.) — high.
- arXiv:2408.13687 (Willow) — high.
- arXiv:quant-ph/9710043 (Margolus-Levitin) — high.
- DOIs 10.1147/rd.53.0183, 10.1147/rd.176.0525 — high.
- DOIs 10.1109/JSSC.2019.2937234, 10.1109/JSSC.2017.2737549 — moderate-high.
- arXiv:2207.06431, PRL 103, 160502 (2009), Nature 591, 575 (2021) — high/moderate.

## Decisions made

1. Platform: superconducting surface code as the reference platform (largest
   published data at threshold; cleanest cryogenic-cost story). Rejected
   trapped ions as primary (laser/optical cost structure differs; no mK
   cryogenics) — noted in limitations; rejected photonic FBQC as primary
   (fewer published system-level numbers).
2. Code distance d = 25–35 for p_L ≈ 1e-12 at p ≈ 1e-3: own order-of-magnitude
   scaling estimate. Rejected quoting a single d.
3. Single-point estimates rejected throughout Section 3: ranges plus an
   order-of-magnitude midpoint, so the draft remains defensible under source
   verification.
4. Rejected per-physical-gate normalization as headline (conflates d² overhead
   with progress; perversely rewards worse decoders).
5. All numbers self-checked arithmetically (ML floors, Landauer products,
   budget sums, J/QLOP division). No fabricated data.

## Rejected approaches

- Waiting/retrying tools after the frozen-View refusal (documented as
  ineffective in this environment; three probes sufficient).
- Fabricating verification status for citations (hard failure under working
  rules).
- Producing a shorter draft to hedge the word count (target ~3,000 words;
  minimum 1,500 met with margin).

## What the parent must do next

1. Verify all 11 references; remove [UNVERIFIED] markers for confirmed ones;
   drop any that fail.
2. Materialize the three files into cycle-1/writer-b/.
3. Machine-count the draft word count.
4. Cross-check writer-b's numbers against sibling writers' (independent inputs).
