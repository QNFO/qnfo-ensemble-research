```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Abstract: \"We derive a determinacy rule — a disparity threshold $\\delta_{\\min}$ is certifiable only if $m < \\delta_{\\min}$ —\" (repeated in Section 4.3: \"at least one of the two certifications is possible only if: $m < \\delta_{\\min}$.\").",
      "reason": "The necessity direction is mathematically false as stated. Certification is possible whenever the interval [p_min,A, p_max,A] does not contain the action threshold δ_min + p_B, which can hold with m > δ_min. Counterexample from the paper's own framework: p̂_A = 0.9, m = 0.5, p_B = 0.35, δ_min = 0.28 gives p_min,A = 0.9 × 0.5 = 0.45 ≥ 0.28, so compliance is certifiable even though m = 0.5 > δ_min = 0.28. The inference in Section 4.3 from 'p_max,A − p_min,A = m' to 'only if m < δ_min' is invalid; m < δ_min is neither necessary nor (without further conditions) the exact characterization.",
      "fix": "Restate the rule with its actual scope: either present m < δ_min as a necessary condition only under the additional premise that certification must be possible for every admissible point estimate (or for the specific interval straddling case), or replace it with the exact condition that certification is impossible if and only if δ_min + p_B lies within [p_min,A, p_max,A]; correct the Abstract, Section 4.3, and any echo in Section 5 and Section 8."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Abstract and Section 1 contribution bullet: \"a reported positive gap survives scrutiny only if $\\hat{g} > m_1 + m_2$\".",
      "reason": "This directly contradicts Section 4.4, which proves the condition is sufficient but NOT necessary and demonstrates a counter-example (r̂1 = 0.8, m1 = 0.2, r̂2 = 0.2, m2 = 0.5: Δmin = 0.04 > 0 so the gap survives, while ĝ = 0.6 < m1 + m2 = 0.7 so the condition fails). The contribution bullet even acknowledges 'a counter-example showing the shortcut is not necessary' in the same sentence in which it asserts 'only if'.",
      "fix": "Change 'only if' to 'if' in the Abstract and the contribution bullet (and check Section 8 for the same overstatement), keeping Section 4.3/4.4's sufficient-versus-exact distinction intact."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Section 4.5: \"Under the assumption-free model, therefore, no finite recovery of labels *guarantees* a determinate verdict, because the guarantee must hold for every outcome pattern the recovery could reveal.\" (Echoed in Section 5 item 6: \"no finite target under the adversarial assumption\" and in Section 8: \"no finite price under the adversarial model.\")",
      "reason": "False as stated: full recovery of all 200 unlabeled labels is finite and yields exact knowledge of p_A, after which the audit can certify whichever verdict is true — a determinate verdict in every outcome pattern. What the paper's own arithmetic actually shows is that no PARTIAL recovery guarantees a determinate verdict (compliance requires p_min,A ≥ 0.28 but p_min,A = 240/1000 = 0.24 for any partial recovery under the adversarial model; adverse impact requires p_max,A < 0.28 but p_max,A = 0.44 regardless of Δk < 200).",
      "fix": "Restrict the claim to partial recovery: 'no recovery short of the full 200 unlabeled labels guarantees a determinate verdict; full recovery guarantees one.' Update Section 4.5, Section 5 item 6, and Section 8 consistently."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Abstract: \"and $134$ labels must be recovered to change that.\"",
      "reason": "The number 134 is derived in Section 4.5 only under the explicitly flagged expected-case assumption (recovered labels behave like the labeled subset); the Abstract states it unconditionally, and 'must be recovered' overstates a conditional target.",
      "fix": "Add the condition in the Abstract, e.g. 'an estimated 134 labels must be recovered, assuming recovered labels resemble the labeled subset.'"
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Abstract and Section 1: \"missingness contributes roughly $7$ times more uncertainty than sampling\".",
      "reason": "Section 4.6 computes the factor as 6.30; 'roughly 7' rounds up beyond the stated precision and 'of order 7' in Section 4.6 is the defensible phrasing.",
      "fix": "Use 'about 6.3 times' in the Abstract and contribution bullet, matching the computed value."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Section 2, discussion of [9]: \"its supplied summary gives no further detail on its methods.\"",
      "reason": "The supplied summary does describe the cluster's claims (photonic circulation rest-energies, helical electron spin, mass ratios on Bruhat–Tits trees); saying it gives no further detail is slightly inaccurate, though the paper correctly refrains from using [9] for anything substantive.",
      "fix": "Rephrase to say the summary describes the claims covered but provides no methodological detail usable here."
    }
  ]
}
```