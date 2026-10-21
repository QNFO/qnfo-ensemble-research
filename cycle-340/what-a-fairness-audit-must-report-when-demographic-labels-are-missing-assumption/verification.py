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
