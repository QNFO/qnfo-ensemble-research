```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Section 4.6 / Result 6: under dispersed offers the marginal value of a thread 'decays polynomially rather than geometrically' and 'the optimal team size scales as a power law (approximately square-root) in the dispersion parameter'.",
      "reason": "These are quantitative structural claims with no derivation, no model of dispersion, no shown arithmetic, and no projection label with stated assumptions. No dispersed-offer objective is ever written down; the polynomial decay rate, the exponent, and the square-root scaling are asserted from nothing.",
      "fix": "Either derive the dispersed-offer marginal (specify the offer distribution, write the resulting failure probability and ΔC, and show the decay exponent explicitly), or relabel the entire subsection as an unproven conjecture/projection with stated assumptions and remove the square-root scaling claim from Abstract and Results."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Margin check ΔC(1) = 5.28570 − 5.51016 = −0.22446 and same-cap comparison C(1) = 70.28574.",
      "reason": "Exact values are 270/49 = 5.510204, giving ΔC(1) = −0.224490, and 60 + 40/7 + 1 + 25/7 = 70.285714. The paper's rounded intermediates (0.85714 × 0.14286) introduce errors in the 4th–5th decimal; not headline-changing but inconsistent with the 'fully explicit arithmetic' standard.",
      "fix": "Carry fractions (6/7, 1/49, 270/49) through the margin and comparison calculations and report exact or consistently rounded values."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Reference [1] is an arXiv API query string ('arXiv Query: search_query=&id_list=2610.06017...') cited as a distinct source alongside [2].",
      "reason": "It is present in the bibliography so it is not an integrity violation, but it is a malformed query-result stub duplicating [2]; citing it as a separate antecedent ([1],[2]) is sloppy and inflates the reference list.",
      "fix": "Merge [1] and [2] into a single canonical citation to arXiv:2610.06017, or replace the query-string entry with a proper bibliographic record."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Section 4.6 and Result 6 treat the dispersed-offer regime in two paragraphs with no formalism.",
      "reason": "The dispersion extension is the paper's third headline result but receives the shallowest treatment: no distributional assumption, no equation, no worked number, and no statement of when the polynomial regime applies.",
      "fix": "Add a minimal formal dispersed-offer model (e.g., i.i.d. reserve prices from a named distribution), derive the failure probability and marginal-value decay, and work one numerical example, or explicitly demote the section to 'informal discussion / future work'."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "Limitations do not state that the acceptance curve a(p) is assumed known, stationary, and correctly calibrated, beyond the brief 'curve drift' bullet.",
      "reason": "All closed-form results (4) and (6) depend on knowing λ and the curve family; misestimation of λ propagates into both n* and p*, and the paper never quantifies this sensitivity.",
      "fix": "Add a sensitivity remark (or small table) showing how the fixed point (2, 13.89182) moves under perturbations of λ and c_t."
    }
  ]
}
```