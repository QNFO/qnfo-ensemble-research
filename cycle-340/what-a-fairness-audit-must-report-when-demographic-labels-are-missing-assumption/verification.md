# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The width of the worst‑case interval for a single group’s rate equals the group’s missingness rate $m_{g}$.",
    "inputs": "m_g (missingness rate)",
    "formula": "r_max - r_min = m_g"
  },
  {
    "id": "Q2",
    "statement": "The width of the assumption‑free interval on a two‑group disparity equals the sum of the two groups’ missingness rates, $m_{1}+m_{2}$.",
    "inputs": "m_1 (missingness rate of group 1), m_2 (missingness rate of group 2)",
    "formula": "Δ_max - Δ_min = m_1 + m_2"
  },
  {
    "id": "Q3",
    "statement": "In the worked example, the missingness rates are $m_{1}=0.6$ and $m_{2}=0.5$, the labeled‑subset rates are $\\hat{r}_{1}=0.25$ and $\\hat{r}_{2}=0.15$, and the reported gap is $\\hat{g}=0.10$.",
    "inputs": "N_1=1000, n_1=400, k_1=100, N_2=1000, n_2=500, k_2=75",
    "formula": "m_1 = 1 - n_1/N_1; m_2 = 1 - n_2/N_2; hat_r1 = k_1/n_1; hat_r2 = k_2/n_2; hat_g = hat_r1 - hat_r2"
  },
  {
    "id": "Q4",
    "statement": "The disparity interval bounds in the worked example are $\\Delta^{\\min}=-0.475$ and $\\Delta^{\\max}=0.625$, giving a width of $1.100$ which equals $m_{1}+m_{2}$.",
    "inputs": "m_1=0.6, m_2=0.5, hat_r1=0.25, hat_r2=0.15",
    "formula": "ell1 = hat_r1*(1-m_1); u1 = ell1 + m_1; ell2 = hat_r2*(1-m_2); u2 = ell2 + m_2; Δ_min = ell1 - u2; Δ_max = u1 - ell2; width = Δ_max - Δ_min"
  },
  {
    "id": "Q5",
    "statement": "In the counter‑example, $\\Delta^{\\min}=0.04>0$ while the shortcut condition $\\hat{g}>m_{1}+m_{2}$ fails because $0.6<0.7$.",
    "inputs": "hat_r1=0.8, m_1=0.2, hat_r2=0.2, m_2=0.5",
    "formula": "ell1 = hat_r1*(1-m_1); u2 = hat_r2*(1-m_2) + m_2; Δ_min = ell1 - u2; hat_g = hat_r1 - hat_r2; shortcut = hat_g > (m_1 + m_2)"
  },
  {
    "id": "Q6",
    "statement": "In the pooled‑regime audit, the rate interval for group A is $[0.24,\\,0.44]$, the four‑fifths ratio interval is $[0.686,\\,1.257]$, the point‑estimate ratio is $0.857$, and the label‑recovery target under the expected‑case assumption is $\\Delta k = 134$ labels.",
    "inputs": "n=1000, k=800, m=0.2, hat_p_A=0.30, p_B=0.35",
    "formula": "p_min_A = hat_p_A * (1-m); p_max_A = p_min_A + m; R_min = p_min_A / p_B; R_max = p_max_A / p_B; hat_R = hat_p_A / p_B; required_fraction = 0.8 * p_B / hat_p_A; k_plus_Delta = required_fraction * n; Δk = ceil(k_plus_Delta - k)"
  },
  {
    "id": "Q7",
    "statement": "For a group with $n_{g}=980$, $m_{g}=0.02$, and $\\hat{r}_{g}=0.25$, the standard error is $0.013832$, the 95 % half‑width is $0.027111$, the disparity sampling contribution (two groups) is $0.054221$, the missingness contribution to disparity is $0.04$, and the total disparity half‑width is $0.09422177$.",
    "inputs": "n_g=980, m_g=0.02, hat_r_g=0.25",
    "formula": "SE = sqrt(hat_r_g*(1-hat_r_g)/n_g); half_width_95 = 1.96 * SE; disparity_sampling = 2 * half_width_95; missingness = 2 * m_g; total_half_width = disparity_sampling + missingness"
  },
  {
    "id": "Q8",
    "statement": "In the moderate‑missingness example ($m=0.2$, $k=800$, $\\hat{p}_{A}=0.30$), the missingness width is $0.2$, the 95 % sampling half‑width is $0.031756$, their ratio is $6.30$, the combined per‑rate half‑width is $0.231756$, and the two‑group disparity combined half‑width is $0.464$.",
    "inputs": "m=0.2, k=800, n=1000, hat_p_A=0.30",
    "formula": "SE_A = sqrt(hat_p_A*(1-hat_p_A)/(k)); half_width_95_A = 1.96 * SE_A; ratio = m / half_width_95_A; combined_per_rate = m + half_width_95_A; combined_disparity = 2 * combined_per_rate"
  },
  {
    "id": "Q9",
    "statement": "The additive uncertainty combination in Section 4.6 yields a total disparity half‑width of $0.09422177$ for $m_{1}=m_{2}=0.02$ and $n_{g}=980$, confirming that sampling error dominates when missingness is low.",
    "inputs": "m_1=0.02, m_2=0.02, n_g=980, hat_r_g=0.25",
    "formula": "SE = sqrt(hat_r_g*(1-hat_r_g)/n_g); half_width_95 = 1.96 * SE; disparity_sampling = 2 * half_width_95; missingness = m_1 + m_2; total_half_width = disparity_sampling + missingness"
  }
]

## Script
```python
import math
import sys

def claim_line(cid, computed, expected, match):
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: width = m_g
# Choose example values
hat_r_g = 0.3
m_g = 0.4
r_min = hat_r_g * (1 - m_g)
r_max = r_min + m_g
width = r_max - r_min
expected_q1 = m_g
match_q1 = "yes" if abs(width - expected_q1) < 1e-12 else "no"
claim_line("Q1", f"{width:.8g}", f"{expected_q1:.8g}", match_q1)

# Q2: disparity width = m1 + m2
# Choose example values
hat_r1 = 0.5
hat_r2 = 0.4
m1 = 0.2
m2 = 0.3
ell1 = hat_r1 * (1 - m1)
u1 = ell1 + m1
ell2 = hat_r2 * (1 - m2)
u2 = ell2 + m2
delta_min = ell1 - u2
delta_max = u1 - ell2
width2 = delta_max - delta_min
expected_q2 = m1 + m2
match_q2 = "yes" if abs(width2 - expected_q2) < 1e-12 else "no"
claim_line("Q2", f"{width2:.8g}", f"{expected_q2:.8g}", match_q2)

# Q3: compute missingness rates and gap
N1, n1, k1 = 1000, 400, 100
N2, n2, k2 = 1000, 500, 75
m1_q3 = 1 - n1 / N1
m2_q3 = 1 - n2 / N2
hat_r1_q3 = k1 / n1
hat_r2_q3 = k2 / n2
hat_g_q3 = hat_r1_q3 - hat_r2_q3
expected_q3 = "m1=0.6,m2=0.5,hat_r1=0.25,hat_r2=0.15,hat_g=0.10"
computed_q3 = f"m1={m1_q3:.8g},m2={m2_q3:.8g},hat_r1={hat_r1_q3:.8g},hat_r2={hat_r2_q3:.8g},hat_g={hat_g_q3:.8g}"
match_q3 = "yes" if (abs(m1_q3-0.6)<1e-12 and abs(m2_q3-0.5)<1e-12 and
                    abs(hat_r1_q3-0.25)<1e-12 and abs(hat_r2_q3-0.15)<1e-12 and
                    abs(hat_g_q3-0.10)<1e-12) else "no"
claim_line("Q3", computed_q3, expected_q3, match_q3)

# Q4: disparity interval bounds and width
ell1_q4 = hat_r1_q3 * (1 - m1_q3)
u1_q4 = ell1_q4 + m1_q3
ell2_q4 = hat_r2_q3 * (1 - m2_q3)
u2_q4 = ell2_q4 + m2_q3
delta_min_q4 = ell1_q4 - u2_q4
delta_max_q4 = u1_q4 - ell2_q4
width_q4 = delta_max_q4 - delta_min_q4
expected_q4 = "Δ_min=-0.475,Δ_max=0.625,width=1.100"
computed_q4 = f"Δ_min={delta_min_q4:.8g},Δ_max={delta_max_q4:.8g},width={width_q4:.8g}"
match_q4 = "yes" if (abs(delta_min_q4+0.475)<1e-12 and abs(delta_max_q4-0.625)<1e-12 and abs(width_q4-1.100)<1e-12) else "no"
claim_line("Q4", computed_q4, expected_q4, match_q4)

# Q5: counter‑example
hat_r1_q5 = 0.8
m1_q5 = 0.2
hat_r2_q5 = 0.2
m2_q5 = 0.5
ell1_q5 = hat_r1_q5 * (1 - m1_q5)
u2_q5 = hat_r2_q5 * (1 - m2_q5) + m2_q5
delta_min_q5 = ell1_q5 - u2_q5
hat_g_q5 = hat_r1_q5 - hat_r2_q5
shortcut_q5 = hat_g_q5 > (m1_q5 + m2_q5)
expected_q5 = "Δ_min=0.04>0,shortcut=False"
computed_q5 = f"Δ_min={delta_min_q5:.8g},shortcut={shortcut_q5}"
match_q5 = "yes" if (abs(delta_min_q5-0.04)<1e-12 and shortcut_q5==False) else "no"
claim_line("Q5", computed_q5, expected_q5, match_q5)

# Q6: pooled‑regime audit
n = 1000
k = 800
m = 1 - k / n
hat_p_A = 0.30
p_B = 0.35
p_min_A = hat_p_A * (1 - m)
p_max_A = p_min_A + m
R_min = p_min_A / p_B
R_max = p_max_A / p_B
hat_R = hat_p_A / p_B
# label‑recovery target under expected‑case
required_fraction = 0.8 * p_B / hat_p_A   # 0.8 * 0.35 / 0.30 = 0.93333...
k_plus_Delta = required_fraction * n
Delta_k = math.ceil(k_plus_Delta - k)
expected_q6 = "interval=[0.24,0.44],ratio_interval=[0.686,1.257],hat_R=0.857,Δk=134"
computed_q6 = f"interval=[{p_min_A:.8g},{p_max_A:.8g}],ratio_interval=[{R_min:.8g},{R_max:.8g}],hat_R={hat_R:.8g},Δk={Delta_k}"
match_q6 = "yes" if (abs(p_min_A-0.24)<1e-12 and abs(p_max_A-0.44)<1e-12 and
                    abs(R_min-0.686)<1e-3 and abs(R_max-1.257)<1e-3 and
                    abs(hat_R-0.857)<1e-3 and Delta_k==134) else "no"
claim_line("Q6", computed_q6, expected_q6, match_q6)

# Q7: sampling and missingness contributions
n_g = 980
m_g = 0.02
hat_r_g = 0.25
SE = math.sqrt(hat_r_g * (1 - hat_r_g) / n_g)
half_width_95 = 1.96 * SE
disparity_sampling = 2 * half_width_95
missingness = 2 * m_g
total_half_width = disparity_sampling + missingness
expected_q7 = "SE=0.013832,half_width=0.027111,disparity_sampling=0.054221,missingness=0.04,total=0.09422177"
computed_q7 = f"SE={SE:.8g},half_width={half_width_95:.8g},disparity_sampling={disparity_sampling:.8g},missingness={missingness:.8g},total={total_half_width:.8g}"
match_q7 = "yes" if (abs(SE-0.013832)<1e-6 and abs(half_width_95-0.027111)<1e-6 and
                    abs(disparity_sampling-0.054221)<1e-6 and abs(missingness-0.04)<1e-12 and
                    abs(total_half_width-0.09422177)<1e-6) else "no"
claim_line("Q7", computed_q7, expected_q7, match_q7)

# Q8: moderate‑missingness example
m = 0.2
k = 800
n = 1000
hat_p_A = 0.30
SE_A = math.sqrt(hat_p_A * (1 - hat_p_A) / k)
half_width_95_A = 1.96 * SE_A
ratio = m / half_width_95_A
combined_per_rate = m + half_width_95_A
combined_disparity = 2 * combined_per_rate
expected_q8 = "missingness=0.2,half_width=0.031756,ratio=6.30,combined_per_rate=0.231756,combined_disparity=0.464"
computed_q8 = f"missingness={m:.8g},half_width={half_width_95_A:.8g},ratio={ratio:.8g},combined_per_rate={combined_per_rate:.8g},combined_disparity={combined_disparity:.8g}"
match_q8 = "yes" if (abs(half_width_95_A-0.031756)<1e-6 and abs(ratio-6.30)<1e-2 and
                    abs(combined_per_rate-0.231756)<1e-6 and abs(combined_disparity-0.464)<1e-3) else "no"
claim_line("Q8", computed_q8, expected_q8, match_q8)

# Q9: additive uncertainty combination (same as Q7)
m1 = 0.02
m2 = 0.02
SE_q9 = math.sqrt(hat_r_g * (1 - hat_r_g) / n_g)
half_width_95_q9 = 1.96 * SE_q9
disparity_sampling_q9 = 2 * half_width_95_q9
missingness_q9 = m1 + m2
total_half_width_q9 = disparity_sampling_q9 + missingness_q9
expected_q9 = "total=0.09422177"
computed_q9 = f"total={total_half_width_q9:.8g}"
match_q9 = "yes" if abs(total_half_width_q9-0.09422177)<1e-6 else "no"
claim_line("Q9", computed_q9, expected_q9, match_q9)

print(f"VERIFICATION SUMMARY: 9 claims, {sum(1 for line in sys.stdout.getvalue().splitlines() if 'match=yes' in line)} match, {sum(1 for line in sys.stdout.getvalue().splitlines() if 'match=no' in line)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.4 expected=0.4 match=yes
CLAIM Q2: computed=0.5 expected=0.5 match=yes
CLAIM Q3: computed=m1=0.6,m2=0.5,hat_r1=0.25,hat_r2=0.15,hat_g=0.1 expected=m1=0.6,m2=0.5,hat_r1=0.25,hat_r2=0.15,hat_g=0.10 match=yes
CLAIM Q4: computed=Δ_min=-0.475,Δ_max=0.625,width=1.1 expected=Δ_min=-0.475,Δ_max=0.625,width=1.100 match=yes
CLAIM Q5: computed=Δ_min=0.04,shortcut=False expected=Δ_min=0.04>0,shortcut=False match=yes
CLAIM Q6: computed=interval=[0.24,0.44],ratio_interval=[0.68571429,1.2571429],hat_R=0.85714286,Δk=134 expected=interval=[0.24,0.44],ratio_interval=[0.686,1.257],hat_R=0.857,Δk=134 match=yes
CLAIM Q7: computed=SE=0.013832083,half_width=0.027110883,disparity_sampling=0.054221767,missingness=0.04,total=0.094221767 expected=SE=0.013832,half_width=0.027111,disparity_sampling=0.054221,missingness=0.04,total=0.09422177 match=yes
CLAIM Q8: computed=missingness=0.2,half_width=0.031755629,ratio=6.2980959,combined_per_rate=0.23175563,combined_disparity=0.46351126 expected=missingness=0.2,half_width=0.031756,ratio=6.30,combined_per_rate=0.231756,combined_disparity=0.464 match=yes
CLAIM Q9: computed=total=0.094221767 expected=total=0.09422177 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 145, in <module>
AttributeError: '_io.TextIOWrapper' object has no attribute 'getvalue'

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.4 | 0.4 | yes | match | 3 significant digits (as printed, at least 3) |
| Q2 | 0.5 | 0.5 | yes | match | 3 significant digits (as printed, at least 3) |
| Q3 | m1=0.6,m2=0.5,hat_r1=0.25,hat_r2=0.15,hat_g=0.1 | m1=0.6,m2=0.5,hat_r1=0.25,hat_r2=0.15,hat_g=0.10 | yes | match | script verdict (values not both numeric) |
| Q4 | Δ_min=-0.475,Δ_max=0.625,width=1.1 | Δ_min=-0.475,Δ_max=0.625,width=1.100 | yes | match | script verdict (values not both numeric) |
| Q5 | Δ_min=0.04,shortcut=False | Δ_min=0.04>0,shortcut=False | yes | match | script verdict (values not both numeric) |
| Q6 | interval=[0.24,0.44],ratio_interval=[0.68571429,1.2571429],hat_R=0.85714286,Δk=134 | interval=[0.24,0.44],ratio_interval=[0.686,1.257],hat_R=0.857,Δk=134 | yes | match | script verdict (values not both numeric) |
| Q7 | SE=0.013832083,half_width=0.027110883,disparity_sampling=0.054221767,missingness=0.04,total=0.094221767 | SE=0.013832,half_width=0.027111,disparity_sampling=0.054221,missingness=0.04,total=0.09422177 | yes | match | script verdict (values not both numeric) |
| Q8 | missingness=0.2,half_width=0.031755629,ratio=6.2980959,combined_per_rate=0.23175563,combined_disparity=0.46351126 | missingness=0.2,half_width=0.031756,ratio=6.30,combined_per_rate=0.231756,combined_disparity=0.464 | yes | match | script verdict (values not both numeric) |
| Q9 | total=0.094221767 | total=0.09422177 | yes | match | script verdict (values not both numeric) |

Mismatches: 0 of 9.
