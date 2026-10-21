import math
from decimal import Decimal, getcontext

getcontext().prec = 100  # high precision for tiny probabilities

def sci(val, sig=3):
    """Return a string like 4.17e4 with `sig` significant figures."""
    if val == 0:
        return "0"
    exponent = int(math.floor(math.log10(abs(val))))
    mantissa = val / (10 ** exponent)
    # round mantissa to (sig-1) decimal places
    fmt = f"{{:.{sig-1}f}}".format(mantissa)
    return f"{fmt}e{exponent}"

def sci_decimal(val, sig=3):
    """Scientific notation for Decimal values."""
    if val == 0:
        return "0"
    exponent = int(val.log10().to_integral(rounding="ROUND_FLOOR"))
    mantissa = val / (Decimal(10) ** exponent)
    # round mantissa
    mantissa = mantissa.quantize(Decimal(10) ** -(sig-1))
    return f"{mantissa}e{exponent}"

def check(id_str, computed, expected):
    match = "yes" if str(computed) == expected else "no"
    print(f"CLAIM {id_str}: computed={computed} expected={expected} match={match}")

# Q1
L = math.ceil(math.log2(1_000_000))
check("Q1", L, "20")

# Q2
N_node = 2 * 1_000_000 - 1
check("Q2", N_node, "1999999")

# Q3
overhead = N_node / 1_000_000
overhead_rounded = round(overhead, 1)  # one decimal place
check("Q3", overhead_rounded, "2.0")

# Q4
alpha_T = 1_000_000 / N_node
alpha_T_rounded = round(alpha_T, 8)  # eight decimal places
check("Q4", alpha_T_rounded, "0.50000025")

# Q5
C_BMR = 20 + 4
check("Q5", C_BMR, "24")

# Q6
speedup = 1_000_000 / C_BMR
speedup_str = sci(speedup, sig=3)
check("Q6", speedup_str, "4.17e4")

# Q7
speedup_fail = 1_000_000 / 84
speedup_fail_str = sci(speedup_fail, sig=3)
check("Q7", speedup_fail_str, "1.19e4")

# Q8
n = Decimal(1_000_000_000)
b_h = 256
P_coll = (n ** 2) / (Decimal(2) ** (b_h + 1))
P_coll_str = sci_decimal(P_coll, sig=3)
check("Q8", P_coll_str, "4.31e-60")

# Q9
two_pow = Decimal(2) ** (b_h + 1)  # 2^257
two_pow_str = sci_decimal(two_pow, sig=3)
check("Q9", two_pow_str, "2.32e77")

# Q10
i = 1_000_000_000 // 2
check("Q10", i, "5e8")

# Q11
checks = math.ceil(math.log2(1_000_000_000))
check("Q11", checks, "30")

# Q12
overhead_bytes = 30 * 32
check("Q12", overhead_bytes, "960")

# Q13
edges = 4 * 1_000_000
check("Q13", edges, "4000000")

# Q14
storage_bytes = edges * 64
# Convert to MiB using decimal megabytes (10^6) as in the paper
storage_mib = storage_bytes / 1_000_000
storage_str = f"{int(storage_mib)} MiB"
check("Q14", storage_str, "256 MiB")

# Q15
linear_scan = 1_000_000
check("Q15", linear_scan, "1000000")
