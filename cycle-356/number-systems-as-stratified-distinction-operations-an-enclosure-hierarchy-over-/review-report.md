{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The stratified‑β‑numbers paper introduces a modified version of Jones’s β‑numbers for Carnot groups and proves that an analogue of Jones’s traveling‑salesman theorem holds when the earlier β’s are replaced by stratified ones; Section 3 shows that the non‑stratified β’s cannot provide sharp two‑sided inequalities for certain Carnot groups [4].",
      "reason": "No excerpt for reference [4] is provided; the paper cannot verify that the cited work makes the specific claims about stratified β‑numbers and the traveling‑salesman theorem.",
      "fix": "Remove the unsupported claim or replace it with a statement that is directly supported by an available excerpt from a cited work."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The super‑powers paper studies sequences s_{n}=... and proves that the number ω(s_{n}) of distinct prime factors exceeds a super‑logarithmic bound for infinitely many n, using the p‑adic valuation ν_{p} [9].",
      "reason": "Reference [9] is about distinct prime factors of a sum of super‑powers, but no excerpt is provided that contains the specific claim about the super‑logarithmic bound; thus the citation lacks verifiable support.",
      "fix": "Delete the sentence or replace it with a claim that can be directly supported by an excerpt from a cited source."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The non‑canonical‑number‑systems paper studies positional systems (ℤ,b,𝔇) with digit sets that do not contain 0, proves that such digit sets exist for every base |b|≥4, and exhibits {1,2} as a valid digit set for base −2 [7].",
      "reason": "No excerpt for reference [7] is provided that confirms these specific results about digit sets; the citation is unsupported.",
      "fix": "Remove or rephrase the statement to only include information that can be verified from the available excerpt."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The Caccetta‑Häggkvist survey records Kemperman’s theorem, which gives an upper bound for the growth of product sets A·B via the quantity k(A,B)=|A|+|B|-|A+B| [6].",
      "reason": "Reference [6] is listed but no excerpt is given that contains Kemperman’s theorem or the described bound; the citation lacks grounding.",
      "fix": "Delete the sentence or replace it with a claim supported by an available excerpt."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The adelic‑physics program references Ostrowski’s theorem, which states that every non‑trivial absolute value on ℚ is equivalent either to the standard Archimedean absolute value (completion ℝ) or to a p‑adic absolute value for some prime p (completion ℚ_{p}). This theorem underwrites falsifier F3 and justifies the operator list of Section 3.2;",
      "reason": "Reference [8] is a paper on binomial coefficients and Apéry‑like numbers; it does not contain Ostrowski’s theorem. The citation is incorrect.",
      "fix": "Replace the citation with a correct source that actually states Ostrowski’s theorem, or remove the claim if no such source is available."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The measurement‑stratigraphy framework explicitly identifies each historical number‑system era with a corresponding distinction operation… The present paper adopts the same mapping for the operators E_{1},…,E_{6} and attaches quantitative analyses to each step.",
      "reason": "Reference [8] does not contain the described measurement‑stratigraphy framework; no excerpt supports this claim.",
      "fix": "Delete or re‑attribute the statement to a source that actually provides the measurement‑stratigraphy description (e.g., [12] if available), or remove the citation."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "The computable‑real‑boundary paper derives ℕ from iterated marking under the Calling rule, positional notation from nested enclosures, and ℚ from enclosures of ratio groups; it identifies the fixed point of finite enclosure operations with the computable reals ℝ_{comp} and places everything beyond that closure in a category that cannot be reduced by any finite sequence of the two primitive laws [9].",
      "reason": "Reference [9] is about distinct prime factors of super‑powers, not the computable‑real‑boundary work; the citation is mismatched.",
      "fix": "Replace the citation with the correct reference (e.g., [13] if it covers the computable‑real‑boundary) or remove the unsupported claim."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "## 9. Conclusion",
      "reason": "The required section heading is ## 8. Conclusion; the paper misnumbers the conclusion as section 9, violating the required structure.",
      "fix": "Rename the heading to ## 8. Conclusion and adjust any internal cross‑references accordingly."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "By Ostrowski’s theorem as stated in [7] every non‑trivial absolute value on ℚ is equivalent either to the Archimedean absolute value or to a p‑adic one (F3).",
      "reason": "Reference [7] is about noncanonical number systems and does not contain Ostrowski’s theorem; the citation is incorrect.",
      "fix": "Remove the citation or replace it with a correct source that actually states Ostrowski’s theorem."
    }
  ],
  "soft": []
}