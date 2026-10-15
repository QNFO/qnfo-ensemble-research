```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "## 5. Results\n\nAll results below are the direct outputs of Section 4's derivations from the stated inputs and illustrative parameters; none are empirical.\n\n## 5. Results (continued)\n\nAll results below are the direct outputs of Section 4's derivations from the stated inputs and illustrative parameters; none are empirical.",
      "reason": "Structural defect: the Section 5 heading and its opening sentence are duplicated verbatim ('## 5. Results' immediately followed by '## 5. Results (continued)' repeating the same sentence), an editing artifact that breaks the required one-heading-per-section structure.",
      "fix": "Delete the first '## 5. Results' block with its duplicate sentence, keeping a single '## 5. Results' heading followed once by the opening sentence and the results list R1-R7."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The quantization budget scales as $\\Delta_{\\text{quant}} = N U_{\\max} q/2$: at the Section 4.3 operating point this is $5.0$ energy units, and it halves if the resolution doubles to $q = 0.2$ at fixed $N$ and $U_{\\max}$.",
      "reason": "Arithmetic error. By the paper's own formula, at $N=100$, $U_{\\max}=1$, $q=0.2$ the budget is $100 \\times 1 \\times 0.2/2 = 10.0$, i.e. it doubles, not halves, when $q$ goes from $0.1$ to $0.2$; the stated 'halves' contradicts the derived formula in the same sentence.",
      "fix": "Replace with the correct direction: the budget doubles to $10.0$ energy units if $q$ doubles to $0.2$, and halves to $2.5$ energy units if the resolution is refined to $q = 0.05$, at fixed $N$ and $U_{\\max}$."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "and that with it, exponential decay ratios almost twice as large as those suggested in the literature are attainable.",
      "reason": "Source support: the supplied text of [2] ends its concluding remarks at 'it is possible to attain exponential decay ratios that are almost twice as'; the completion 'large as those suggested in the literature' is not stated in the entry and is asserted as what the work reports.",
      "fix": "Trim the claim to what the source states: report only that with the optimal scattering-transformation parameter, exponential decay ratios almost twice as large are attainable, or reword to 'exponential decay ratios almost twice as large (per its concluding remarks)'."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "(i) The Signal output is quantized with uniform resolution $q = 0.1$ ... **Input list.** ... $\\Delta = 0.05$ (uniform quantization step, chosen)",
      "reason": "Section 4.3 uses quantization resolution $q = 0.1$ while Section 4.4 uses quantization step $\\Delta = 0.05$; both are labeled chosen parameters, but the inconsistent symbols and values for the same physical quantity invite misreading of R3 versus R5.",
      "fix": "Add one sentence in Section 4.4 noting that $\\Delta$ there is an independent illustrative choice, deliberately different from the $q = 0.1$ of Section 4.3, and that R3 and R5 therefore describe different operating points."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "$\\Delta_{\\text{quant}} = 5.0$ energy units ... $E_q \\le 0.025\\ \\mathrm{J}$",
      "reason": "R3 is reported in dimensionless 'energy units' while R5 is reported in joules for a normalized example; the unit mixing is unexplained and could suggest a physical measurement where none exists.",
      "fix": "State once in Section 4.4 that all energies, including those written with $\\mathrm{J}$, are normalized illustrative quantities, not physical measurements."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "The paper contains no '## Appendix A. Divergence report' or '## Appendix B. Claim attribution' sections.",
      "reason": "The reconciled-output structure requires Appendix A (divergence report) and Appendix B (claim attribution); both are absent, so any divergences resolved between drafts are undocumented.",
      "fix": "Append Appendix A documenting any conventions chosen where drafts disagreed and Appendix B with the claim table C1..Cn, or state explicitly that no substantive divergences remained."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "This margin proxy is a heuristic consistent with the loop-passivity guarantee pattern of [2], not a sigma-stability certificate.",
      "reason": "The term 'sigma-stability' is used without definition in the paper's own text, although [2]'s entry defines it via real parts of characteristic quasipolynomial roots; an adjacent-field reader of this paper alone cannot parse the caveat.",
      "fix": "Define sigma-stability in one clause at first use (all closed-loop characteristic roots having real parts below $-\\sigma$), citing [2]."
    }
  ]
}
```