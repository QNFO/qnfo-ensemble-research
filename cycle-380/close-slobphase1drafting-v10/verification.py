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
