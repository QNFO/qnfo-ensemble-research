# Writer-A cycle-1 notes.md (retry attempt)

## Environment status
Both tool-capability probes in this child session were refused by the frozen View ceiling: every Code Mode subtool call — update_plan, web_search, arxiv-mcp-server_search_papers, write, exec — was rejected at dispatch (codeModeUtilityHost.js:474) with "Tool '<name>' is outside the frozen View ceiling." This is the known CHILD-FROZEN-VIEW-1 block. No network I/O occurred, no citations were verified, and no files were written. Per working rule 5, this retry delivers draft.md, notes.md, and claims.md inline for the parent to materialize.

## Searches planned but not run (parent should execute these during verification)
arXiv (arxiv-mcp-server_search_papers):
- "Margolus-Levitin quantum speed limit" (expect quant-ph/9710043; review 1705.08023)
- "Landauer principle quantum computation energy bound"
- "quantum technologies need an energy agenda" (expect 2111.09241)
- "is quantum computing green energy efficiency quantum advantage" (expect 2205.12092)
- "cryogenic cooling overhead superconducting quantum computer scaling energy"
- "limitations quantum computing resource constraints" (expect 2007.01966)
- "surface code decoder micro-architecture power FPGA" (expect 2001.06598)
- "surface codes towards practical large-scale quantum computation" (expect 1208.0928)
Web (web_search):
- "joules-per-compute benchmark github" (confirm internal program status)
- "Google Willow Nature below threshold arXiv 2408.13687"
- "1000 logical qubits roadmap 2026 superconducting"

## Sources used
None verified. All 11 references come from the author's internal knowledge and carry [UNVERIFIED - needs parent check] markers. All constant arithmetic uses CODATA values (ħ = 1.054571817e-34 J·s; k_B = 1.380649e-23 J/K), which are established.

## Decisions
1. Delivered the draft inline (working rule 5) rather than failing.
2. Every external citation marked [UNVERIFIED - needs parent check]; every machine-scale number labeled order-of-magnitude estimate with assumptions stated inline.
3. Reference architecture = superconducting surface code (Q2 names surface-code protection explicitly); distance-27 as the worked example, d = 15–31 range stated.
4. Rejected the naive per-op classical comparison as the headline claim; kept the ~10^7 ratio only as magnitude context and routed the honest comparison to per-problem-instance energy.
5. Added a falsification test for the benchmark revision itself (Section 5, final paragraph).
6. Validation performed as pure computation (no subtools): all arithmetic in the draft re-derived in code — see Validation in the handoff.

## Rejected approaches
- Further tool retries: 2 probe cells (5 distinct subtools) failed identically at dispatch; per CHILD-FROZEN-VIEW-1, further retries are noise.
- Downloading full papers to extract numbers: impossible without tool access; headline numbers therefore come only from internal knowledge and are flagged accordingly.
