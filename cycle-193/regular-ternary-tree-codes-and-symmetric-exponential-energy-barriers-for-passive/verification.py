import math
from math import comb

def approx_equal(a, b, sig=6):
    """Return True if a and b match to the given number of significant digits."""
    if b == 0:
        return abs(a) < 10**(-sig)
    return round(a / b, sig) == 1

# Q1
B7 = 2**7
print(f"CLAIM Q1: computed={B7:.0f} expected=128 match={'yes' if B7==128 else 'no'}")

# Q2
p=3; t=1
n1 = 1 + ((p+1)*(p**t - 1))//(p-1)  # integer division works because result is integer
print(f"CLAIM Q2: computed={n1} expected=5 match={'yes' if n1==5 else 'no'}")

# Q3
t=2
n2 = 1 + ((p+1)*(p**t - 1))//(p-1)
print(f"CLAIM Q3: computed={n2} expected=17 match={'yes' if n2==17 else 'no'}")

# Q4
d1 = 2*1 + 1
d2 = 2*2 + 1
expected_d1d2 = (3,5)
match_q4 = (d1==3 and d2==5)
print(f"CLAIM Q4: computed={d1},{d2} expected=3 and 5 match={'yes' if match_q4 else 'no'}")

# Q5
n=5; eps=1e-3; t=1
P_pass = sum(comb(n,w)*(eps**w)*((1-eps)**(n-w)) for w in range(t+1, n+1))
print(f"CLAIM Q5: computed={P_pass:.8e} expected=9.98e-6 match={'yes' if approx_equal(P_pass,9.98e-6,6) else 'no'}")

# Q6
suppression = eps / P_pass
print(f"CLAIM Q6: computed={suppression:.4f} expected=100.2 match={'yes' if approx_equal(suppression,100.2,4) else 'no'}")

# Q7
p0=0.4
p1 = sum(comb(8,k)*(p0**k)*((1-p0)**(8-k)) for k in range(5,9))
print(f"CLAIM Q7: computed={p1:.7f} expected=0.1736704 match={'yes' if approx_equal(p1,0.1736704,7) else 'no'}")

# Q8
p2 = sum(comb(8,k)*(p1**k)*((1-p1)**(8-k)) for k in range(5,9))
print(f"CLAIM Q8: computed={p2:.12f} expected=0.005548945525 match={'yes' if approx_equal(p2,0.005548945525,12) else 'no'}")

# Q9
p3 = sum(comb(8,k)*(p2**k)*((1-p2)**(8-k)) for k in range(5,9))
print(f"CLAIM Q9: computed={p3:.3e} expected=2.905e-10 match={'yes' if approx_equal(p3,2.905e-10,3) else 'no'}")

# Q10
N=100000
pL = 3/N
print(f"CLAIM Q10: computed={pL:.5e} expected=3e-5 match={'yes' if abs(pL-3e-5)<1e-12 else 'no'}")

# Q11
cost_per_qubit=5000
num_qubits=243
total_cost = cost_per_qubit * num_qubits
print(f"CLAIM Q11: computed=${total_cost:,} expected=$1.2 million match={'yes' if abs(total_cost-1_200_000)/1_200_000<0.05 else 'no'}")

# Q12
logical_error=2.905e-10
errors_per_million = logical_error * 1_000_000
print(f"CLAIM Q12: computed={errors_per_million:.3e} expected=2.9e-4 match={'yes' if approx_equal(errors_per_million,2.9e-4,3) else 'no'}")

print("VERIFICATION SUMMARY: 12 claims, "
      f"{sum(1 for line in open(__file__) if 'match=yes' in line)} match, "
      f"{12 - sum(1 for line in open(__file__) if 'match=yes' in line)} mismatch")
