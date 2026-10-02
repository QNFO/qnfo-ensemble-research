```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "CIT-01",
      "severity": "HARD",
      "claim": "All 12 entries in '## References' carry machine identifiers that do not match the provided BIBLIOGRAPHY.",
      "reason": "Every reference is unverifiable against the bibliography: [1] cites arXiv:2210.01530 but the bibliography entry is arXiv:1705.00365v2; [2] cites arXiv:2406.01569 vs arXiv:2512.10504v2; [3] cites arXiv:2303.08844 vs arXiv:2112.04501v3; [4] cites DOI:10.1017/jfm.2020.105 vs arXiv:2110.02266v1; [5] cites arXiv:1907.05321 vs arXiv:2506.02131v2; [6] cites arXiv:1610.08997 vs arXiv:1612.07324v3; [7] cites arXiv:2004.04203 vs arXiv:2210.10776v3; [8] cites arXiv:2106.02915 vs arXiv:2104.00572v3; [9] cites arXiv:2311.07526 vs a QNFO record with DOI pending; [10] cites arXiv:2409.01366 vs QNFO DOI 10.5281/zenodo.22025544; [11] cites arXiv:2302.06639 vs QNFO DOI pending; [12] cites DOI:10.1007/978-3-031-21432-5_8 vs QNFO DOI 10.5281/zenodo.21208346. The topical descriptions match the bibliography, but the identifiers as printed are invented or wrong, making every citation unverifiable as written.",
      "fix": "Replace all reference identifiers with the exact machine identifiers from the BIBLIOGRAPHY (arXiv IDs for [1]-[8]; QNFO/DOI designations for [9]-[12]), preserving the bibliography's numbering and order."
    }
  ],
  "soft": [
    {
      "id": "DIV-01",
      "severity": "SOFT",
      "claim": "The paper repeatedly defers modeling-convention conflicts to 'Appendix A' (e.g., 'see Appendix A, D1 for the convention choice').",
      "reason": "No Appendix A appears in the manuscript; the divergence-honesty documentation promised in Section 1 and Section 4.1 is missing, so the claimed convention conflicts are unresolved and unverifiable.",
      "fix": "Include Appendix A enumerating each draft divergence (D1, ...) with the adopted convention and the rejected alternative."
    },
    {
      "id": "ARITH-01",
      "severity": "SOFT",
      "claim": "Section 4.3 cross-check: 'at e = 4.4e-3 this gives 1 - (0.986862 + 0.013089) = 4.9e-5'.",
      "reason": "The term 3e(1-e)^2 = 3 x 0.0044 x 0.991219 = 0.013084, not 0.013089; the correct value is 1 - 0.999946 = 5.4e-5, not 4.9e-5. Not a headline number, but the paper's stated policy is that all arithmetic is shown and exact.",
      "fix": "Recompute and correct the cross-check value to ~5.4e-5 (still below 1e-4, so the qualitative conclusion stands)."
    },
    {
      "id": "DEPTH-01",
      "severity": "SOFT",
      "claim": "Reference [4] (flow through cylinder clusters) is included as a 'methodological analogy only'.",
      "reason": "No quantitative or qualitative result from [4] is used; the analogy (a 'solidity parameter' playing an 'averaging role') is superficial and does not support any claim, weakening the literature treatment.",
      "fix": "Either develop the analogy into a concrete decoding criterion or drop [4] and adjust the reference list."
    }
  ]
}
```