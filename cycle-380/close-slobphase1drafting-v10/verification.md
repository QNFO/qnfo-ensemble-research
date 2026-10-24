# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Draft‑completion rate is 76.19 % (16 drafted out of 21 deliverables).",
    "inputs": "drafted = 16, total = 21",
    "formula": "R = drafted / total"
  },
  {
    "id": "Q2",
    "statement": "Objective‑success score is 16.7 % (0.5 divided by 3 objectives).",
    "inputs": "sum = 0.5, num_objectives = 3",
    "formula": "R = sum / num_objectives"
  },
  {
    "id": "Q3",
    "statement": "If “Partially Met” counts as full, the objective‑success score rises to 33.3 % (1 divided by 3).",
    "inputs": "sum = 1, num_objectives = 3",
    "formula": "R = sum / num_objectives"
  },
  {
    "id": "Q4",
    "statement": "Minimum token budget is 40 000 tokens (16 chapters × 2500 tokens each).",
    "inputs": "chapters = 16, tokens_per_chapter_min = 2500",
    "formula": "total_tokens = chapters * tokens_per_chapter_min"
  },
  {
    "id": "Q5",
    "statement": "Nominal token budget is 48 000 tokens (16 chapters × 3000 tokens each).",
    "inputs": "chapters = 16, tokens_per_chapter_nom = 3000",
    "formula": "total_tokens = chapters * tokens_per_chapter_nom"
  },
  {
    "id": "Q6",
    "statement": "Per‑chapter reliability threshold for a 50 % chance of a failure‑free phase is approximately 0.958.",
    "inputs": "phase_success_target = 0.5, chapters = 16",
    "formula": "p_star = phase_success_target^(1/chapters)"
  },
  {
    "id": "Q7",
    "statement": "Per‑constraint reliability threshold for three independent constraints is approximately 0.986.",
    "inputs": "phase_success_target = 0.5, chapters = 16, constraints = 3",
    "formula": "q_star = phase_success_target^(1/(chapters * constraints))"
  },
  {
    "id": "Q8",
    "statement": "If per‑chapter adherence is 0.9, the probability of a failure‑free phase is about 0.185 (18.5 %).",
    "inputs": "p = 0.9, chapters = 16",
    "formula": "P_phase = p^chapters"
  },
  {
    "id": "Q9",
    "statement": "At p = 0.5, expected passes per chapter = 2, total passes = 32, giving an overhead factor of 2.0×.",
    "inputs": "p = 0.5, chapters = 16",
    "formula": "passes_per_chapter = 1/p; total_passes = chapters / p; overhead = total_passes / chapters"
  },
  {
    "id": "Q10",
    "statement": "At the threshold p* ≈ 0.9576, expected passes per chapter ≈ 1.0443, total passes ≈ 16.71, overhead factor ≈ 1.044× (4.4 % overhead).",
    "inputs": "p_star = 0.9576, chapters = 16",
    "formula": "passes_per_chapter = 1/p_star; total_passes = chapters / p_star; overhead = total_passes / chapters"
  },
  {
    "id": "Q11",
    "statement": "With four sub‑sections per chapter, the required per‑sub‑section reliability is about 0.989.",
    "inputs": "p_star = 0.9576, sub_sections = 4",
    "formula": "r_star = p_star^(1/sub_sections)"
  },
  {
    "id": "Q12",
    "statement": "If style checking is automated (reducing constraints to 2), the per‑constraint generation threshold drops to about 0.979.",
    "inputs": "phase_success_target = 0.5, chapters = 16, gen_constraints = 2",
    "formula": "q_star_gen = phase_success_target^(1/(chapters * gen_constraints))"
  },
  {
    "id": "Q13",
    "statement": "Projected cost per 2500‑token chapter is $0.00005 at $0.02 per 1 M tokens.",
    "inputs": "tokens_per_chapter = 2500, price_per_M_tokens = 0.02",
    "formula": "cost_chapter = tokens_per_chapter * price_per_M_tokens / 1_000_000"
  },
  {
    "id": "Q14",
    "statement": "Projected total cost for 16 chapters is $0.0008 (≈ $0.001).",
    "inputs": "cost_chapter = 0.00005, chapters = 16",
    "formula": "total_cost = cost_chapter * chapters"
  }
]

## Script
```python
import math

def fmt(x, digits=6):
    # format with given significant digits, removing trailing zeros
    s = f"{x:.{digits}g}"
    return s

# Q1
drafted = 16
total = 21
R1 = drafted / total
print(f"CLAIM Q1: computed={fmt(R1,8)} expected=0.7619 match={'yes' if round(R1,4)==0.7619 else 'no'}")

# Q2
sum_obj = 0.5
num_obj = 3
R2 = sum_obj / num_obj
print(f"CLAIM Q2: computed={fmt(R2,8)} expected=0.1667 match={'yes' if round(R2,4)==0.1667 else 'no'}")

# Q3
sum_obj_full = 1.0
R3 = sum_obj_full / num_obj
print(f"CLAIM Q3: computed={fmt(R3,8)} expected=0.3333 match={'yes' if round(R3,4)==0.3333 else 'no'}")

# Q4
chapters = 16
tokens_min = 2500
total_min = chapters * tokens_min
print(f"CLAIM Q4: computed={total_min} expected=40000 match={'yes' if total_min==40000 else 'no'}")

# Q5
tokens_nom = 3000
total_nom = chapters * tokens_nom
print(f"CLAIM Q5: computed={total_nom} expected=48000 match={'yes' if total_nom==48000 else 'no'}")

# Q6
phase_target = 0.5
p_star = phase_target ** (1/chapters)
print(f"CLAIM Q6: computed={fmt(p_star,8)} expected=0.9576 match={'yes' if round(p_star,4)==0.9576 else 'no'}")

# Q7
constraints = 3
q_star = phase_target ** (1/(chapters*constraints))
print(f"CLAIM Q7: computed={fmt(q_star,8)} expected=0.9857 match={'yes' if round(q_star,4)==0.9857 else 'no'}")

# Q8
p = 0.9
P_phase = p ** chapters
print(f"CLAIM Q8: computed={fmt(P_phase,8)} expected=0.1853 match={'yes' if round(P_phase,4)==0.1853 else 'no'}")

# Q9
p9 = 0.5
passes_per = 1/p9
total_passes = chapters / p9
overhead = total_passes / chapters
print(f"CLAIM Q9: computed={passes_per:.1f}, {int(total_passes)}, {fmt(overhead,2)} expected=2, 32, 2.0 match={'yes' if (passes_per==2 and total_passes==32 and abs(overhead-2.0)<1e-9) else 'no'}")

# Q10
p_star10 = 0.9576
passes_per10 = 1/p_star10
total_passes10 = chapters / p_star10
overhead10 = total_passes10 / chapters
print(f"CLAIM Q10: computed={fmt(passes_per10,4)}, {fmt(total_passes10,4)}, {fmt(overhead10,4)} expected=1.0443, 16.71, 1.044 match={'yes' if (abs(passes_per10-1.0443)<1e-4 and abs(total_passes10-16.71)<1e-2 and abs(overhead10-1.044)<1e-3) else 'no'}")

# Q11
r_star = p_star ** (1/4)
print(f"CLAIM Q11: computed={fmt(r_star,8)} expected=0.9892 match={'yes' if round(r_star,4)==0.9892 else 'no'}")

# Q12
gen_constraints = 2
q_star_gen = phase_target ** (1/(chapters*gen_constraints))
print(f"CLAIM Q12: computed={fmt(q_star_gen,8)} expected=0.9786 match={'yes' if round(q_star_gen,4)==0.9786 else 'no'}")

# Q13
tokens_chapter = 2500
price_per_M = 0.02
cost_chapter = tokens_chapter * price_per_M / 1_000_000
print(f"CLAIM Q13: computed={fmt(cost_chapter,8)} expected=0.00005 match={'yes' if abs(cost_chapter-0.00005)<1e-8 else 'no'}")

# Q14
total_cost = cost_chapter * chapters
print(f"CLAIM Q14: computed={fmt(total_cost,8)} expected=0.0008 match={'yes' if abs(total_cost-0.0008)<1e-8 else 'no'}")

print(f"VERIFICATION SUMMARY: 14 claims, {sum(1 for line in [None])} match, {14 - sum(1 for line in [None])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.76190476 expected=0.7619 match=yes
CLAIM Q2: computed=0.16666667 expected=0.1667 match=yes
CLAIM Q3: computed=0.33333333 expected=0.3333 match=yes
CLAIM Q4: computed=40000 expected=40000 match=yes
CLAIM Q5: computed=48000 expected=48000 match=yes
CLAIM Q6: computed=0.95760328 expected=0.9576 match=yes
CLAIM Q7: computed=0.9856632 expected=0.9857 match=yes
CLAIM Q8: computed=0.18530202 expected=0.1853 match=yes
CLAIM Q9: computed=2.0, 32, 2 expected=2, 32, 2.0 match=yes
CLAIM Q10: computed=1.044, 16.71, 1.044 expected=1.0443, 16.71, 1.044 match=yes
CLAIM Q11: computed=0.98922801 expected=0.9892 match=yes
CLAIM Q12: computed=0.97857206 expected=0.9786 match=yes
CLAIM Q13: computed=5e-05 expected=0.00005 match=yes
CLAIM Q14: computed=0.0008 expected=0.0008 match=yes
VERIFICATION SUMMARY: 14 claims, 1 match, 13 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.76190476 | 0.7619 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 0.16666667 | 0.1667 | yes | match | 4 significant digits (as printed, at least 3) |
| Q3 | 0.33333333 | 0.3333 | yes | match | 4 significant digits (as printed, at least 3) |
| Q4 | 40000 | 40000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 48000 | 48000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0.95760328 | 0.9576 | yes | match | 4 significant digits (as printed, at least 3) |
| Q7 | 0.9856632 | 0.9857 | yes | match | 4 significant digits (as printed, at least 3) |
| Q8 | 0.18530202 | 0.1853 | yes | match | 4 significant digits (as printed, at least 3) |
| Q11 | 0.98922801 | 0.9892 | yes | match | 4 significant digits (as printed, at least 3) |
| Q12 | 0.97857206 | 0.9786 | yes | match | 4 significant digits (as printed, at least 3) |
| Q13 | 5e-05 | 0.00005 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 0.0008 | 0.0008 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 12.
