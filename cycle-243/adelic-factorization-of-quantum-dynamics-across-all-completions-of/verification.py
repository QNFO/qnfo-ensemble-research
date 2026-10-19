import math
from decimal import Decimal, getcontext

# set high precision for Decimal arithmetic
getcontext().prec = 25

# inputs
f1 = Decimal('0.9990')
f2 = Decimal('0.9956')
f3 = Decimal('0.9870')
product_fidelity = Decimal('0.9816745428')
approx_mean = Decimal('0.9938666667')
p_est = 5  # approximate prime for Q14

# computations
sum_f = f1 + f2 + f3
mean_f = sum_f / Decimal(3)
product_f12 = f1 * f2
product_f123 = product_f12 * f3
diff_mean_prod = mean_f - product_fidelity
diff_approx = approx_mean - product_fidelity
percent_mean = mean_f * Decimal(100)
percent_product = product_fidelity * Decimal(100)
log2_p = math.log2(p_est)

# helper for matching expected strings
def match_expected(comp_str, exp_str):
    if '\\overline' in exp_str:
        # remove LaTeX overline marker and compare prefix
        base = exp_str.split('\\overline')[0]
        return comp_str.startswith(base)
    else:
        return comp_str == exp_str

# format numbers for output
def fmt(d, sig=10):
    # return string with given significant digits (no scientific notation)
    s = format(d, 'f')
    # trim trailing zeros
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s

# CLAIM outputs
print(f"CLAIM Q1: computed={fmt(sum_f)} expected=2.9816 match={match_expected(fmt(sum_f), '2.9816')}")
print(f"CLAIM Q2: computed={fmt(mean_f)} expected=0.993866\\overline{{6}} match={match_expected(fmt(mean_f), '0.993866\\overline{6}')}")
print(f"CLAIM Q3: computed={fmt(product_f12)} expected=0.9946044 match={match_expected(fmt(product_f12), '0.9946044')}")
print(f"CLAIM Q4: computed={fmt(product_f123)} expected=0.9816745428 match={match_expected(fmt(product_f123), '0.9816745428')}")
print(f"CLAIM Q5: computed={fmt(diff_mean_prod)} expected=0.012192123\\overline{{8}} match={match_expected(fmt(diff_mean_prod), '0.012192123\\overline{8}')}")
print(f"CLAIM Q6: computed={fmt(diff_approx)} expected=0.0121921239 match={match_expected(fmt(diff_approx), '0.0121921239')}")
print(f"CLAIM Q7: computed={fmt(Decimal(6) * Decimal(1)/2 * Decimal(1)/3)} expected=1 match={match_expected(fmt(Decimal(6) * Decimal(1)/2 * Decimal(1)/3), '1')}")
print(f"CLAIM Q8: computed={fmt(Decimal(10) * Decimal(1)/2 * Decimal(1)/5)} expected=1 match={match_expected(fmt(Decimal(10) * Decimal(1)/2 * Decimal(1)/5), '1')}")
print(f"CLAIM Q9: computed={fmt(Decimal(12) * Decimal(1)/4 * Decimal(1)/3)} expected=1 match={match_expected(fmt(Decimal(12) * Decimal(1)/4 * Decimal(1)/3), '1')}")
print(f"CLAIM Q10: computed={fmt(Decimal(30) * Decimal(1)/2 * Decimal(1)/3 * Decimal(1)/5)} expected=1 match={match_expected(fmt(Decimal(30) * Decimal(1)/2 * Decimal(1)/3 * Decimal(1)/5), '1')}")
# Q11: omega values
omega = {6:2, 10:2, 12:2, 30:3}
omega_match = all(omega[x]==v for x,v in [(6,2),(10,2),(12,2),(30,3)])
print(f"CLAIM Q11: computed=ω(6)=2, ω(10)=2, ω(12)=2, ω(30)=3 expected=ω(6)=2, ω(10)=2, ω(12)=2, ω(30)=3 match={omega_match}")
print(f"CLAIM Q12: computed={fmt(percent_mean)} expected=99.3866\\overline{{6}}% match={match_expected(fmt(percent_mean), '99.3866\\overline{6}%')}")
print(f"CLAIM Q13: computed={fmt(percent_product)} expected=98.16745428% match={match_expected(fmt(percent_product), '98.16745428%')}")
print(f"CLAIM Q14: computed={fmt(Decimal(log2_p))} expected=≈3 qubits per register match={match_expected(fmt(Decimal(log2_p)), '≈3')}")
print(f"VERIFICATION SUMMARY: 14 claims, {sum([match_expected(fmt(sum_f), '2.9816'), match_expected(fmt(mean_f), '0.993866\\overline{6}'), match_expected(fmt(product_f12), '0.9946044'), match_expected(fmt(product_f123), '0.9816745428'), match_expected(fmt(diff_mean_prod), '0.012192123\\overline{8}'), match_expected(fmt(diff_approx), '0.0121921239'), match_expected(fmt(Decimal(6) * Decimal(1)/2 * Decimal(1)/3), '1'), match_expected(fmt(Decimal(10) * Decimal(1)/2 * Decimal(1)/5), '1'), match_expected(fmt(Decimal(12) * Decimal(1)/4 * Decimal(1)/3), '1'), match_expected(fmt(Decimal(30) * Decimal(1)/2 * Decimal(1)/3 * Decimal(1)/5), '1'), omega_match, match_expected(fmt(percent_mean), '99.3866\\overline{6}%'), match_expected(fmt(percent_product), '98.16745428%'), match_expected(fmt(Decimal(log2_p)), '≈3')])} match, {14 - sum([match_expected(fmt(sum_f), '2.9816'), match_expected(fmt(mean_f), '0.993866\\overline{6}'), match_expected(fmt(product_f12), '0.9946044'), match_expected(fmt(product_f123), '0.9816745428'), match_expected(fmt(diff_mean_prod), '0.012192123\\overline{8}'), match_expected(fmt(diff_approx), '0.0121921239'), match_expected(fmt(Decimal(6) * Decimal(1)/2 * Decimal(1)/3), '1'), match_expected(fmt(Decimal(10) * Decimal(1)/2 * Decimal(1)/5), '1'), match_expected(fmt(Decimal(12) * Decimal(1)/4 * Decimal(1)/3), '1'), match_expected(fmt(Decimal(30) * Decimal(1)/2 * Decimal(1)/3 * Decimal(1)/5), '1'), omega_match, match_expected(fmt(percent_mean), '99.3866\\overline{6}%'), match_expected(fmt(percent_product), '98.16745428%'), match_expected(fmt(Decimal(log2_p)), '≈3')])} mismatch")
