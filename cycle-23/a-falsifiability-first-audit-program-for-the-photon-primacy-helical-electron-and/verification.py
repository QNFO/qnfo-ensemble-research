#!/usr/bin/env python3
"""
Self-contained verifier (stdlib only: math, fractions).

Independently re-derives each numeric claim from its stated inputs and
compares against the paper's stated/expected value when one is given.
Floating-point comparisons use math.isclose(rel_tol=1e-6).

Precision design note
---------------------
The JSON "formula" strings for Q5/Q6 carry rounded intermediates
(Delta_mu = 0.2317170, relative_deviation = 1.1206e-3).  Rather than
re-injecting those rounded values (which would make the check circular),
each claim is recomputed from its *primary* inputs using exact/directed
precision, and the expected value from the paper is compared against that
independent derivation.  Both the "from stated literal inputs" and the
"from primary inputs" results are reported for the claims where they
differ, so the effect of intermediate rounding is visible.
"""

import math
from fractions import Fraction

# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------

REL = 1e-6


def close(computed, expected):
    """Return True/False/None for a float comparison against an expected value."""
    if expected is None:
        return None
    try:
        return math.isclose(float(computed), float(expected), rel_tol=REL)
    except (TypeError, ValueError):
        return None


def fmt(value):
    """Readable, round-trippable string for either a number or None."""
    if value is None:
        return "none"
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        if value != value:  # NaN
            return "nan"
        return repr(value)
    return str(value)


class Report:
    def __init__(self):
        self.rows = []

    def claim(self, cid, computed, expected=None):
        match = close(computed, expected)
        self.rows.append((cid, computed, expected, match))
        print(
            "CLAIM {}: computed={} expected={} match={}".format(
                cid, fmt(computed), fmt(expected),
                "n/a" if match is None else ("yes" if match else "no"),
            )
        )
        return computed

    def summary(self):
        n = len(self.rows)
        m = sum(1 for _, _, _, ok in self.rows if ok is True)
        k = sum(1 for _, _, _, ok in self.rows if ok is False)
        print("VERIFICATION SUMMARY: {} claims, {} match, {} mismatch".format(n, m, k))
        return n, m, k


R = Report()

# ----------------------------------------------------------------------
# Q1 -- combinatorial test space: N_t = N_c * N_r * N_k
# ----------------------------------------------------------------------
N_c = 16      # claims
N_r = 2       # regimes (Standard-Model vs condensed-matter)
N_k = 2       # catalogs (elementary vs quasiparticle)
N_t = N_c * N_r * N_k
Q1 = R.claim("Q1", N_t, 64)

# ----------------------------------------------------------------------
# Q2 -- Bonferroni-adjusted per-test level: alpha_0 / N_t
# ----------------------------------------------------------------------
alpha_0 = 0.05
alpha_bonf = alpha_0 / N_t
# exact rational check (independent of float arithmetic)
alpha_bonf_frac = Fraction(5, 100) / N_t          # 1/1280
assert alpha_bonf_frac == Fraction(1, 1280), alpha_bonf_frac
Q2 = R.claim("Q2", alpha_bonf, 7.8125e-4)

# ----------------------------------------------------------------------
# Q3 -- naive (uncorrected) family-wise error rate: 1 - (1-a0)^N_t
# ----------------------------------------------------------------------
fwer_naive = 1.0 - (1.0 - alpha_0) ** N_t          # 1 - 0.95**64
# independent recomputation via log-space to guard against fp drift
ln_fwer = N_t * math.log1p(-alpha_0)
fwer_naive_alt = -math.expm1(ln_fwer)
Q3 = R.claim("Q3", fwer_naive, 0.9624)
# cross-check the two float routes agree
assert math.isclose(fwer_naive, fwer_naive_alt, rel_tol=1e-12), (
    fwer_naive, fwer_naive_alt)

# ----------------------------------------------------------------------
# Q4 -- absolute deviation of muon/electron ratio from integer 207
# ----------------------------------------------------------------------
claimed_int_mu = 207
R_mu = 206.7682830                                  # CODATA 2022
delta_mu_primary = claimed_int_mu - R_mu
Q4 = R.claim("Q4", delta_mu_primary, 0.2317170)
# also derive from the (rounded) literal input quoted in the JSON formula
delta_mu_literal = 207 - 206.7682830
assert math.isclose(delta_mu_primary, delta_mu_literal, rel_tol=1e-15)

# ----------------------------------------------------------------------
# Q5 -- relative deviation from 207: Delta_mu / R_mu
# ----------------------------------------------------------------------
rel_dev = delta_mu_primary / R_mu                   # from primary inputs
Q5 = R.claim("Q5", rel_dev, 1.1206e-3)
# show the effect of using the JSON's rounded Delta_mu literal
rel_dev_literal = 0.2317170 / 206.7682830
print("# note Q5: rel_dev(primary)={!r}  rel_dev(rounded Delta_mu)={!r}".format(
    rel_dev, rel_dev_literal))

# ----------------------------------------------------------------------
# Q6 -- muon/electron integer hypothesis significance in sigma
# ----------------------------------------------------------------------
sigma_rel = 1.1e-8
sigma_mu = (rel_dev / sigma_rel)                    # primary-input route
Q6 = R.claim("Q6", sigma_mu, 1.02e5)
# JSON-literal route (rounded relative deviation) for transparency
sigma_mu_literal = (1.1206e-3) / (1.1e-8)
print("# note Q6: sigma(primary)={!r}  sigma(from rounded 1.1206e-3)={!r}".format(
    sigma_mu, sigma_mu_literal))

# ----------------------------------------------------------------------
# Q7 -- tau/electron mass ratio from PDG 2024/CODATA masses
# ----------------------------------------------------------------------
m_tau = 1776.86      # MeV
m_e = 0.51099895     # MeV
R_tau = m_tau / m_e
Q7 = R.claim("Q7", R_tau, 3477.224)

# ----------------------------------------------------------------------
# Q8 -- absolute deviation of tau/electron ratio from integer 3477
# ----------------------------------------------------------------------
claimed_int_tau = 3477
delta_tau = R_tau - claimed_int_tau                 # from recomputed R_tau
Q8 = R.claim("Q8", delta_tau, 0.224)
# JSON-literal route, using the rounded R_tau = 3477.224
delta_tau_literal = 3477.224 - 3477
print("# note Q8: Delta_tau(primary)={!r}  Delta_tau(from rounded 3477.224)={!r}".format(
    delta_tau, delta_tau_literal))

# ----------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------
R.summary()
