```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Average greedy-additive symbol count over 1–3999 is 'about 11.5 symbols' (Sections 4.5, 4.6, 5, Abstract), giving compactness ratio 2.9.",
      "reason": "Arithmetic error in a headline number. The paper's own displayed sum evaluates to about 4.45, not 11.5. Derivation: for N in 1..999 the expected greedy count is E[floor(N/500)] + E[floor((N mod 500)/100)] + E[floor((N mod 100)/50)] + E[floor((N mod 50)/10)] + E[floor((N mod 10)/5)] + E[floor(N mod 5)] = 0.5 + 0.9 + 0.5 + 0.9 + 0.5 + 0.4 = 3.7; each thousands-block 1000–1999, 2000–2999, 3000–3999 adds exactly 1 thousand-symbol plus the same 3.7 remainder average, giving 4.7 per block; overall average = (3.7 + 3×4.7)/4 = 17.8/4 = 4.45. The compactness ratio is therefore 4.45/4 ≈ 1.11, not 2.9.",
      "fix": "Replace 11.5 with 4.45 (showing the block-by-block derivation), replace the ratio 2.9 with 4.45/4 ≈ 1.11 in the Abstract, Section 4.5, Section 4.6, Table 1, and Introduction, and recompute the crossover in H4 accordingly."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Worst-case positional deletion error over the stated range: 'delete the leading digit of 9999, giving 999; error = 9·10^3 = 9000', worst-case ratio 9000/1000 = 9.",
      "reason": "9999 is outside the paper's own stated domain N ∈ [1, 3999] (Sections 3.2, 4.2). Within the range the worst case is N = 3999: deleting the leading digit 3 leaves 999, so the error is 3999 − 999 = 3000 = 3·10^3, and the worst-case ratio is 3000/1000 = 3, not 9.",
      "fix": "Replace the 9999 example with N = 3999, error 3·10^3 = 3000, ratio 3000/1000 = 3, and change the general statement 'worst-case ratio is 9·10^(d−4)' to 3·10^(d−4) for the range ending at 4·10^(d−1) − 1 (or state the range explicitly for the factor 9)."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Expected positional transposition error 'projected as 30·10^k per position' (Sections 4.4, 5, Abstract).",
      "reason": "Contradicts the paper's own derivation two lines earlier: E[|Δ|] = 10^k · E[|d_{k+1} − d_k|] = 3.3·10^k, which is correct (E[|X − Y|] = 3.3 for independent uniform digits on {0,…,9}). The jump from 3.3·10^k to 30·10^k is a factor-of-10 inconsistency presented as a projection with no stated assumption that could produce it.",
      "fix": "Delete the '30·10^k' projection and report the derived value 3.3·10^k per adjacent pair (or, if a per-number figure is wanted, state the number of pairs n − 1 explicitly and use 3.3·(n − 1)·10^k with k specified per pair)."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Expected four-digit deletion errors: positional 4500 and additive ≈174 (Abstract, Sections 4.6, 5), and the crossover λ/μ ≈ 1.73 built on them.",
      "reason": "Quantitative honesty: these numbers are labeled projections but no inputs, assumptions, or derivation are stated anywhere in the paper — Section 4 never computes 4500 or 174, yet Section 4.6 uses them as 'projected averages' in the crossover arithmetic. A projection requires stated assumptions; these have none, and the crossover 1.73 inherits the unsupported inputs (and the erroneous 11.5 from H1).",
      "fix": "Either derive E_pos and E_add under explicitly stated distributional assumptions with shown arithmetic (e.g., uniform N, uniform deletion position, and for the additive case the expected deleted symbol value (sum of symbol values)/L for a representation of length L), or remove 4500, 174, the ratio 25.9, and the 1.73 crossover from Abstract, Sections 4.6, 5, and 7, retaining only the qualitative statement that a crossover exists."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Section 4.2: 'More generally, deleting the leading digit of a d-digit number gives error ≤ 9·10^(d−1), so the worst-case ratio is 9·10^(d−4): constant.'",
      "reason": "Follows from the out-of-range 9999 example (H2). For the paper's stated range [1, 3999] the leading digit is at most 3, so the worst-case leading-deletion error is 3·10^(d−1) and the ratio is 3·10^(d−4); the bound 9·10^(d−1) holds only for ranges reaching 10^d − 1, which is not the stated domain.",
      "fix": "Restate with the range-specific constant: error ≤ 3·10^(d−1) for N < 4·10^(d−1), worst-case ratio 3·10^(d−4), noting explicitly that the constant depends on the top of the range."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "References [10], [11], [12] are listed as 'NUMERATA v2.0.', 'Tree-based numeration synthesis.', 'Ten-Fingered Trap.' without the machine identifiers.",
      "reason": "The bibliography titles are 'QNFO: NUMERATA: A Multi-Axis Framework for Evaluating Numeral Systems | DOI 10.5281/zenodo.21441847', 'QNFO: Nonlinear Tree-Based Numeration Systems: A Consolidated Synthesis | DOI 10.5281/zenodo.22749402', and 'QNFO: Ten-Fingered Trap'; the instructions require exact copying of titles and identifiers.",
      "fix": "Copy the bibliography titles and DOIs verbatim into the References entries for [10], [11], and [12]."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Stray markup artifacts: '$$\\' after the display equations in Sections 4.3 and 4.4, and '\\nwhich' / '\\nevaluates' in Section 4.5.",
      "reason": "Typographical corruption from draft conversion; harmless to claims but unprofessional in a preprint.",
      "fix": "Remove the trailing backslashes and stray 'n' characters so the display equations and following sentences read cleanly."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Section 4.4: 'Summing over the n − 1 possible adjacent pairs yields an expected positional error of approximately 3.3(n − 1)·10^k.'",
      "reason": "Dimensionally sloppy: k differs for each adjacent pair, so a single 10^k cannot be factored out of the sum; the sum should be 3.3·Σ_k 10^k over the pair positions.",
      "fix": "Rewrite as E = 3.3·Σ_{k=0}^{n−2} 10^k and, if a closed form is wanted, 3.3·(10^(n−1) − 1)/9, stating the leading-digit restriction."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "The arithmetic-tractability axis is argued only qualitatively and the Discussion's falsification criterion references the unsupported 174/4500 projections.",
      "reason": "Depth: the third landscape axis has no metric, and the falsification condition is stated in terms of numbers that H4 shows are underived, so the criterion is not currently actionable.",
      "fix": "After fixing H4, restate the falsification criterion in terms of the derived quantities (e.g., measured mean transcription error for positional notation exceeding the additive bound v_max = 1000 under comparable deletion rates), and briefly discuss candidate tractability metrics."
    }
  ]
}
```