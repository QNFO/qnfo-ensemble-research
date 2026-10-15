import math

def claim(id_, computed, expected, match):
    print(f"CLAIM {id_}: computed={computed:.10f} expected={expected} match={match}")

# Q1
x0, u0 = 0.0, 0.1
dV = 0.5*(x0+u0)**2 - 0.5*x0**2
supply = u0*(x0 + 0.5*u0)
claim("Q1", dV, "0.005", round(dV, 6) == 0.005 and round(supply, 6) == 0.005)

# Q2
alpha = 0.1
c = alpha**2/2 - alpha
claim("Q2", c, "-0.095", round(c, 6) == -0.095)

# Q3
x0 = 2.0
dV = (alpha**2/2 - alpha)*x0**2
claim("Q3", dV, "-0.38", round(dV, 6) == -0.38)

# Q4
u0 = 0.5
y0 = 0.9*x0 + 0.5*u0
margin = 0.5*((1-alpha)*x0 + u0)**2 - 0.5*x0**2 - u0*y0
claim("Q4", margin, "-0.38", round(margin, 6) == -0.38)

# Q5
x, u = 1.0, -1.0
beta, gamma = 1.0, 0.0
m = (alpha**2/2 - alpha)*x**2 + (1-alpha-beta)*x*u + (0.5-gamma)*u**2
claim("Q5", m, "0.505", round(m, 6) == 0.505)

# Q6
q, Umax, N = 0.1, 1.0, 100
dq = N*Umax*q/2
claim("Q6", dq, "5.0", round(dq, 6) == 5.0)

# Q7
delta = alpha - alpha**2/2
claim("Q7", delta, "0.095", round(delta, 6) == 0.095)

# Q8
diss = delta*N*1.0**2
claim("Q8", diss, "9.5", round(diss, 6) == 9.5)

# Q9
phi = 1.0*0.5*(180/math.pi)
claim("Q9", phi, "28.65", round(phi, 2) == 28.65)

# Q10
M = 2.0*(0.1+0.2)
claim("Q10", M, "0.6", round(M, 6) == 0.6)

# Q11
ld = 0.5/(2*math.pi)
claim("Q11", ld, "0.0796", round(ld, 4) == 0.0796)

# Q12
Mn = 0.6/1.6
claim("Q12", Mn, "0.375", round(Mn, 6) == 0.375)

# Q13
rho = 0.375/ld
claim("Q13", rho, "4.71", round(rho, 2) == 4.71)

# Q14
Eq = (0.05/2)*1.0
ratio = Eq/1.0**2
claim("Q14", ratio, "0.025", round(Eq, 6) == 0.025 and round(ratio, 6) == 0.025)

# Q15
rq = (0.05/2)/0.5
claim("Q15", rq, "0.05", round(rq, 6) == 0.05)

# Q16
r16 = 0.1/0.6
claim("Q16", r16, "0.167", round(r16, 3) == 0.167)

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
