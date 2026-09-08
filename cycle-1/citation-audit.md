# Citation Audit — cycle-1

Verifier: parent session (2026-09-08, tool access restored; writers were tool-blocked).
Method: arXiv MCP get_abstract per arXiv ID; Crossref REST API per DOI.

## Result summary

- 16 unique arXiv IDs cited across writers a/b/c: **15 verified** (title + author attribution match),
  **1 wrong** (writer-c reference 3: arXiv:1203.1212 belongs to an unrelated paper).
- 6 journal DOIs cited: **6/6 verified**.
- Title-attribution errors: **1** (writer-a reference 5, Auffeves title).
- Year note: **1** (Nature 638 issued 2024 online / 2025 in print; drafts cite 2025).

## Per-ID table

| arXiv ID | Cited by | Status | Actual title (verified) |
|---|---|---|---|
| quant-ph/9710043 | a,b,c | OK | The maximum speed of dynamical evolution (Margolus, Levitin) |
| quant-ph/9908043 | a,c | OK | Ultimate physical limits to computation (Lloyd) |
| 1705.08023 | a | OK | Quantum speed limits... (Deffner, Campbell) |
| 2111.09241 | a,c | TITLE-FIX | Quantum technologies need a Quantum Energy Initiative (Auffeves) |
| 2205.12092 | a | OK | Is quantum computing green?... (Jaschke, Montangero) |
| 2007.01966 | a,b,c | OK | Limitations in quantum computing from resource constraints (Fellous-Asiani et al.) |
| 1208.0928 | a,c | OK | Surface codes: Towards practical large-scale quantum computation (Fowler et al.) |
| 2001.06598 | a,b | OK | A Scalable Decoder Micro-architecture... (Das et al.) |
| 2408.13687 | a,b,c | OK | Quantum error correction below the surface code threshold (Acharya et al.; Nature 638, 920-926, print 2025) |
| 1806.07862 | b | OK | Engineering cryogenic setups for 100-qubit scale... (Krinner et al.) |
| 2207.06431 | b | OK | Suppressing quantum errors by scaling a surface code logical qubit (Acharya et al.; Nature 614, 676-681, 2023) |
| 0905.3417 | c | OK | The fundamental limit on the rate of quantum dynamics... (Levitin, Toffoli; PRL 103, 160502) |
| 1203.1212 | c | **WRONG** | Codes Satisfying the Chain Condition with a Poset Weights (Panek, Firer) — unrelated |
| 1905.09749 | c | OK | How to factor 2048 bit RSA integers... (Gidney, Ekerå) |
| 2209.05469 | c | OK | Optimizing resource efficiencies for scalable full-stack quantum computers (Fellous-Asiani et al.) |
| 2308.07915 | c | OK | High-threshold and low-overhead fault-tolerant quantum memory (Bravyi et al.; Nature 627, 778-782, 2024) |

## DOI table

| DOI | Cited by | Status | Actual (verified) |
|---|---|---|---|
| 10.1147/rd.53.0183 | b,c | OK | Landauer, IBM J. Res. Dev. 5, 183-191 (1961) |
| 10.1147/rd.176.0525 | b | OK | Bennett, IBM J. Res. Dev. 17, 525-532 (1973) |
| 10.1109/JSSC.2019.2937234 | b | OK | Bardin et al., IEEE JSSC 54, 3043-3060 (2019) |
| 10.1109/JSSC.2017.2737549 | b,c | OK | Patra et al., IEEE JSSC 53, 309-321 (2018) |
| 10.1038/s41586-024-08449-y | (check) | OK | Acharya et al., Nature 638, 920-926 (2024 online) |
| 10.1038/s41586-022-05434-1 | (check) | OK | Acharya et al., Nature 614, 676-681 (2023) |

## Corrections applied in the reconciled paper

1. **writer-c ref 3 (Bérut):** arXiv:1203.1212 removed. Correct citation: A. Bérut et al.,
   "Experimental verification of Landauer's principle linking information and thermodynamics,"
   Nature 483, 187-189 (2012), DOI 10.1038/nature10872. No arXiv ID verified; cite the DOI.
2. **writer-a ref 5 (Auffeves):** title corrected to "Quantum technologies need a Quantum Energy
   Initiative," PRX Quantum 3, 020101 (2022).
3. **Nature 638 (Acharya et al.):** print year 2025 retained; Crossref online year 2024 noted.

## Per-writer integrity summary

| Writer | Refs | Real | Wrong ID | Title error | Notes |
|---|---|---|---|---|---|
| a | 10 + 1 internal | 10/10 | 0 | 1 (Auffeves) | internal QNFO repo entry is a program pointer, not a citation |
| b | 11 | 11/11 | 0 | 0 | Levitin-Toffoli cited without arXiv ID (PRL data correct) |
| c | 12 | 11/12 | 1 (Bérut) | 0 | Landauer DOI written from memory — correct |

Ensemble citation-integrity rate: 32/33 external entries real (97%). The [UNVERIFIED - needs parent
check] flagging protocol caught both defects before any downstream use.

