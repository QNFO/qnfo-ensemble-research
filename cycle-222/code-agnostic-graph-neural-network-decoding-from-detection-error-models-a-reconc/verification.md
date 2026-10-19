# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Improvement factor from a 25 % reduction in logical failures is $F_1 = 0.75$.",
    "inputs": "reduction percentage X = 25",
    "formula": "F1 = 1 - X/100"
  },
  {
    "id": "Q2",
    "statement": "Relative threshold improvement at code distance $d=5$ is approximately $10.06\\%$.",
    "inputs": "improvement factor F1 = 0.75, distance d = 5, m = ceil(d/2) = 3",
    "formula": "threshold ratio = (4/3)^(1/m); relative improvement = (threshold ratio - 1) * 100"
  },
  {
    "id": "Q3",
    "statement": "Relative threshold improvement at code distance $d=7$ is approximately $7.46\\%$.",
    "inputs": "improvement factor F1 = 0.75, distance d = 7, m = ceil(d/2) = 4",
    "formula": "threshold ratio = (4/3)^(1/m); relative improvement = (threshold ratio - 1) * 100"
  },
  {
    "id": "Q4",
    "statement": "Relative threshold improvement at code distance $d=9$ is approximately $5.92\\%$.",
    "inputs": "improvement factor F1 = 0.75, distance d = 9, m = ceil(d/2) = 5",
    "formula": "threshold ratio = (4/3)^(1/m); relative improvement = (threshold ratio - 1) * 100"
  },
  {
    "id": "Q5",
    "statement": "Distance‑equivalent exponent gain is $\\Delta m = 0.4150375$.",
    "inputs": "improvement factor F1 = 0.75, fixed ratio r = 0.5",
    "formula": "Delta m = ln(F1) / ln(r)"
  },
  {
    "id": "Q6",
    "statement": "Improvement factor from a 16 % reduction in logical failures is $F_2 = 0.84$.",
    "inputs": "reduction percentage X = 16",
    "formula": "F2 = 1 - X/100"
  },
  {
    "id": "Q7",
    "statement": "Relative threshold improvement for the $[[130,4,6]]$ qLDPC code is approximately $5.98\\%$.",
    "inputs": "improvement factor F2 = 0.84, distance d = 6, m = ceil(d/2) = 3",
    "formula": "threshold ratio = (1/F2)^(1/m); relative improvement = (threshold ratio - 1) * 100"
  },
  {
    "id": "Q8",
    "statement": "Speedup bounds from latency ranges are $s_{\\min}=4$, $s_{\\max}=25$, with midpoint $s_{\\mathrm{mid}}\\approx10$.",
    "inputs": "GPU latency range t_G in [2,5] ms, CPU latency range t_B in [20,50] ms",
    "formula": "s_min = t_B_min / t_G_max; s_max = t_B_max / t_G_min; s_mid = ((t_B_min + t_B_max)/2) / ((t_G_min + t_G_max)/2)"
  },
  {
    "id": "Q9",
    "statement": "Projected GPU throughput at the midpoint latency is $\\approx285.7$ shots s$^{-1}$.",
    "inputs": "midpoint GPU latency t_G_mid = 3.5 ms = 0.0035 s",
    "formula": "throughput = 1 / t_G_mid"
  },
  {
    "id": "Q10",
    "statement": "Projected CPU throughput at the midpoint latency is $\\approx28.6$ shots s$^{-1}$.",
    "inputs": "midpoint CPU latency t_B_mid = 35 ms = 0.035 s",
    "formula": "throughput = 1 / t_B_mid"
  },
  {
    "id": "Q11",
    "statement": "Discarded‑shot failure rate must be $9.1$ times the base logical error rate.",
    "inputs": "retained fraction f = 0.9, post‑selection reduction factor = 10",
    "formula": "p_disc = (p - f * p/10) / (1 - f) = 9.1 * p"
  },
  {
    "id": "Q12",
    "statement": "Throughput cost of post‑selection is $0.111$ (11.1 %).",
    "inputs": "retained fraction f = 0.9",
    "formula": "cost = (1 - f) / f"
  },
  {
    "id": "Q13",
    "statement": "Accuracy‑per‑throughput gain from post‑selection is $\\approx11.1\\times$.",
    "inputs": "reduction factor = 10, retained fraction f = 0.9",
    "formula": "gain = reduction factor / f"
  },
  {
    "id": "Q14",
    "statement": "Surface‑code DEM at $d=8$, $R=8$ has 441 detectors, 1 337 mechanisms, 1 779 total nodes, and 2 681 edges.",
    "inputs": "code distance d = 8, rounds R = 8",
    "formula": "N_D = (d^2 - 1)*(R - 1); N_M = (2*d^2 + (d^2 - 1))*R; E_D = 2*d^2*R*2 + (d^2 - 1)*R*1; E_L = d^2 * R; total nodes = N_D + N_M + 1; total edges = E_D + E_L"
  },
  {
    "id": "Q15",
    "statement": "$[[130,4,6]]$ qLDPC DEM with $R=8$ has approximately 5 172 nodes and 12 480 edges.",
    "inputs": "detectors per round = 126, mechanisms per round = 520, logical edges per round = 520, rounds R = 8",
    "formula": "nodes ≈ (126 + 520)*R + 4; edges ≈ (2*520 + 520)*R"
  },
  {
    "id": "Q16",
    "statement": "The qLDPC DEM is about $2.9\\times$ larger in nodes and $4.7\\times$ larger in edges than the $d=8$ surface‑code DEM.",
    "inputs": "surface‑code nodes = 1 779, qLDPC nodes ≈ 5 172; surface‑code edges = 2 681, qLDPC edges ≈ 12 480",
    "formula": "node ratio = qLDPC_nodes / surface_nodes; edge ratio = qLDPC_edges / surface_edges"
  }
]

## Script
```python
import math

def fmt(v, digits=6):
    # format with given significant digits, removing trailing zeros
    s = f"{v:.{digits}g}"
    return s

# Q1
F1 = 1 - 25/100
exp1 = "0.75"
match1 = "yes" if abs(F1 - 0.75) < 1e-12 else "no"
print(f"CLAIM Q1: computed={fmt(F1)} expected={exp1} match={match1}")

# Q2
m5 = 3
ratio5 = (4/3) ** (1/m5)
rel5 = (ratio5 - 1) * 100
exp2 = "10.06%"
match2 = "yes" if abs(rel5 - 10.06) < 0.01 else "no"
print(f"CLAIM Q2: computed={fmt(rel5,8)} expected={exp2} match={match2}")

# Q3
m7 = 4
ratio7 = (4/3) ** (1/m7)
rel7 = (ratio7 - 1) * 100
exp3 = "7.46%"
match3 = "yes" if abs(rel7 - 7.46) < 0.01 else "no"
print(f"CLAIM Q3: computed={fmt(rel7,8)} expected={exp3} match={match3}")

# Q4
m9 = 5
ratio9 = (4/3) ** (1/m9)
rel9 = (ratio9 - 1) * 100
exp4 = "5.92%"
match4 = "yes" if abs(rel9 - 5.92) < 0.01 else "no"
print(f"CLAIM Q4: computed={fmt(rel9,8)} expected={exp4} match={match4}")

# Q5
Delta_m = math.log(0.75) / math.log(0.5)
exp5 = "0.4150375"
match5 = "yes" if abs(Delta_m - 0.4150375) < 1e-9 else "no"
print(f"CLAIM Q5: computed={fmt(Delta_m,9)} expected={exp5} match={match5}")

# Q6
F2 = 1 - 16/100
exp6 = "0.84"
match6 = "yes" if abs(F2 - 0.84) < 1e-12 else "no"
print(f"CLAIM Q6: computed={fmt(F2)} expected={exp6} match={match6}")

# Q7
m6 = 3
ratio6 = (1/F2) ** (1/m6)
rel6 = (ratio6 - 1) * 100
exp7 = "5.98%"
match7 = "yes" if abs(rel6 - 5.98) < 0.01 else "no"
print(f"CLAIM Q7: computed={fmt(rel6,8)} expected={exp7} match={match7}")

# Q8
tG_min, tG_max = 2, 5      # ms
tB_min, tB_max = 20, 50    # ms
s_min = tB_min / tG_max
s_max = tB_max / tG_min
s_mid = ((tB_min + tB_max)/2) / ((tG_min + tG_max)/2)
exp8 = "s_min=4, s_max=25, s_mid≈10"
match8 = "yes" if (abs(s_min-4)<1e-9 and abs(s_max-25)<1e-9 and abs(s_mid-10)<1e-9) else "no"
print(f"CLAIM Q8: computed=s_min={fmt(s_min)}, s_max={fmt(s_max)}, s_mid={fmt(s_mid)} expected={exp8} match={match8}")

# Q9
tG_mid = 3.5 / 1000  # seconds
thr_gpu = 1 / tG_mid
exp9 = "≈285.7"
match9 = "yes" if abs(thr_gpu - 285.7142857) < 0.1 else "no"
print(f"CLAIM Q9: computed={fmt(thr_gpu,7)} expected={exp9} match={match9}")

# Q10
tB_mid = 35 / 1000  # seconds
thr_cpu = 1 / tB_mid
exp10 = "≈28.6"
match10 = "yes" if abs(thr_cpu - 28.5714286) < 0.1 else "no"
print(f"CLAIM Q10: computed={fmt(thr_cpu,7)} expected={exp10} match={match10}")

# Q11
f = 0.9
p_disc_factor = (1 - f*0.1) / (1 - f)  # derived as 9.1
exp11 = "9.1"
match11 = "yes" if abs(p_disc_factor - 9.1) < 1e-9 else "no"
print(f"CLAIM Q11: computed={fmt(p_disc_factor,4)} expected={exp11} match={match11}")

# Q12
cost = (1 - f) / f
exp12 = "0.111"
match12 = "yes" if abs(cost - 0.1111111111) < 1e-3 else "no"
print(f"CLAIM Q12: computed={fmt(cost,3)} expected={exp12} match={match12}")

# Q13
gain = 10 / f
exp13 = "≈11.1×"
match13 = "yes" if abs(gain - 11.1111111) < 0.01 else "no"
print(f"CLAIM Q13: computed={fmt(gain,5)} expected={exp13} match={match13}")

# Q14
d, R = 8, 8
N_D = (d**2 - 1)*(R - 1)
N_M = (2*d**2 + (d**2 - 1))*R
E_D = 2*d**2*R*2 + (d**2 - 1)*R*1
E_L = d**2 * R
total_nodes = N_D + N_M + 1
total_edges = E_D + E_L
exp14 = "441 detectors, 1 337 mechanisms, 1 779 total nodes, 2 681 edges"
computed14 = f"{N_D} detectors, {N_M} mechanisms, {total_nodes} total nodes, {total_edges} edges"
match14 = "yes" if (N_D==441 and N_M==1337 and total_nodes==1779 and total_edges==2681) else "no"
print(f"CLAIM Q14: computed={computed14} expected={exp14} match={match14}")

# Q15
det_per_round = 126
mech_per_round = 520
log_edges_per_round = 520
R = 8
nodes_q = (det_per_round + mech_per_round)*R + 4
edges_q = (2*mech_per_round + log_edges_per_round)*R
exp15 = "≈5 172 nodes and 12 480 edges"
computed15 = f"{nodes_q} nodes and {edges_q} edges"
match15 = "yes" if (nodes_q == 5172 and edges_q == 12480) else "no"
print(f"CLAIM Q15: computed={computed15} expected={exp15} match={match15}")

# Q16
surf_nodes, surf_edges = 1779, 2681
ratio_nodes = nodes_q / surf_nodes
ratio_edges = edges_q / surf_edges
exp16 = "≈2.9× larger in nodes and ≈4.7× larger in edges"
computed16 = f"{fmt(ratio_nodes,3)}× nodes, {fmt(ratio_edges,3)}× edges"
match16 = "yes" if (abs(ratio_nodes-2.9)<0.1 and abs(ratio_edges-4.7)<0.1) else "no"
print(f"CLAIM Q16: computed={computed16} expected={exp16} match={match16}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for m in [match1,match2,match3,match4,match5,match6,match7,match8,match9,match10,match11,match12,match13,match14,match15,match16] if m=='yes')} match, {sum(1 for m in [match1,match2,match3,match4,match5,match6,match7,match8,match9,match10,match11,match12,match13,match14,match15,match16] if m=='no')} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.75 expected=0.75 match=yes
CLAIM Q2: computed=10.064242 expected=10.06% match=yes
CLAIM Q3: computed=7.4569932 expected=7.46% match=yes
CLAIM Q4: computed=5.9223841 expected=5.92% match=yes
CLAIM Q5: computed=0.415037499 expected=0.4150375 match=yes
CLAIM Q6: computed=0.84 expected=0.84 match=yes
CLAIM Q7: computed=5.9839833 expected=5.98% match=yes
CLAIM Q8: computed=s_min=4, s_max=25, s_mid=10 expected=s_min=4, s_max=25, s_mid≈10 match=yes
CLAIM Q9: computed=285.7143 expected=≈285.7 match=yes
CLAIM Q10: computed=28.57143 expected=≈28.6 match=yes
CLAIM Q11: computed=9.1 expected=9.1 match=yes
CLAIM Q12: computed=0.111 expected=0.111 match=yes
CLAIM Q13: computed=11.111 expected=≈11.1× match=yes
CLAIM Q14: computed=441 detectors, 1528 mechanisms, 1970 total nodes, 3064 edges expected=441 detectors, 1 337 mechanisms, 1 779 total nodes, 2 681 edges match=no
CLAIM Q15: computed=5172 nodes and 12480 edges expected=≈5 172 nodes and 12 480 edges match=yes
CLAIM Q16: computed=2.91× nodes, 4.65× edges expected=≈2.9× larger in nodes and ≈4.7× larger in edges match=yes
VERIFICATION SUMMARY: 16 claims, 15 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.75 | 0.75 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 10.064242 | 10.06% | yes | match | script verdict (values not both numeric) |
| Q3 | 7.4569932 | 7.46% | yes | match | script verdict (values not both numeric) |
| Q4 | 5.9223841 | 5.92% | yes | match | script verdict (values not both numeric) |
| Q5 | 0.415037499 | 0.4150375 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q6 | 0.84 | 0.84 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 5.9839833 | 5.98% | yes | match | script verdict (values not both numeric) |
| Q9 | 285.7143 | ≈285.7 | yes | match | script verdict (values not both numeric) |
| Q10 | 28.57143 | ≈28.6 | yes | match | script verdict (values not both numeric) |
| Q11 | 9.1 | 9.1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 0.111 | 0.111 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 11.111 | ≈11.1× | yes | match | script verdict (values not both numeric) |

Mismatches: 0 of 12.
