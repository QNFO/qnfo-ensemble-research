import math
from fractions import Fraction


def parse_dec(s):
    """Parse a decimal string exactly into a Fraction."""
    return Fraction(s)


def round_sig(x, n):
    """Round a Fraction to n significant digits (half-up), returning a Fraction."""
    if x == 0:
        return Fraction(0)
    ax = abs(x)
    e = int(math.floor(math.log10(float(ax))))
    while ax < Fraction(10) ** e:
        e -= 1
    while ax >= Fraction(10) ** (e + 1):
        e += 1
    unit = Fraction(10) ** (e - n + 1)
    q = x / unit
    if q >= 0:
        fl = q.numerator // q.denominator
        if q - fl >= Fraction(1, 2):
            fl += 1
        rq = Fraction(fl)
    else:
        aq = -q
        fl = aq.numerator // aq.denominator
        if aq - fl >= Fraction(1, 2):
            fl += 1
        rq = Fraction(-fl)
    return rq * unit


def sig_digits(s):
    """Count the significant digits carried by a plain decimal string."""
    t = s.strip().lstrip("+-")
    for ch in ("e", "E"):
        if ch in t:
            t = t.split(ch)[0]
    t = t.replace(".", "").lstrip("0")
    return len(t) if t else 1


def fmt(x, min_sig=8):
    """Format a Fraction exactly with at least min_sig significant digits."""
    if x == 0:
        return "0." + "0" * (min_sig - 1)
    neg = x < 0
    ax = -x if neg else x
    e = int(math.floor(math.log10(float(ax))))
    while ax < Fraction(10) ** e:
        e -= 1
    while ax >= Fraction(10) ** (e + 1):
        e += 1
    decimals = max(min_sig - 1 - e, 0)
    while True:
        scaled = ax * Fraction(10) ** decimals
        n = scaled.numerator // scaled.denominator
        if Fraction(n) != scaled:
            decimals += 1
            continue
        if decimals > 0:
            ip = n // 10 ** decimals
            fp = n % 10 ** decimals
            s = str(ip) + "." + format(fp, "0" + str(decimals) + "d")
        else:
            s = str(n)
        if sig_digits(s) >= min_sig:
            return ("-" if neg else "") + s
        decimals += 1


def check(cid, computed, expected_str):
    """Recompute-then-adjudicate: round computed to the paper's significant
    digits and compare against the expected value parsed from its string."""
    n = sig_digits(expected_str)
    rounded = round_sig(computed, n)
    expected = Fraction(expected_str)
    match = "yes" if rounded == expected else "no"
    print("CLAIM {}: computed={} expected={} match={}".format(
        cid, fmt(computed), expected_str, match))
    return match


def main():
    results = []

    # ---- Q1: symmetric case, expected utility of action u0 ----
    # Inputs: P(h0|o)=0.5, P(h1|o)=0.5, U(u0,h0)=10, U(u0,h1)=0
    # Formula: E[U|u0,o] = P(h0|o)*U(u0,h0) + P(h1|o)*U(u0,h1)
    p_h0 = parse_dec("0.5")
    p_h1 = parse_dec("0.5")
    eu0_sym = p_h0 * 10 + p_h1 * 0
    results.append(check("Q1", eu0_sym, "5"))

    # ---- Q2: symmetric case, expected utility of action u1 ----
    # Inputs: P(h0|o)=0.5, P(h1|o)=0.5, U(u1,h0)=0, U(u1,h1)=10
    # Formula: E[U|u1,o] = P(h0|o)*U(u1,h0) + P(h1|o)*U(u1,h1)
    eu1_sym = p_h0 * 0 + p_h1 * 10
    results.append(check("Q2", eu1_sym, "5"))

    # ---- Q3: collapsed agent that always selects u0, symmetric case ----
    # Inputs: P(h0)=0.5, P(h1)=0.5, U(u0,h0)=10, U(u0,h1)=0
    # Formula: E[U_collapsed] = 0.5*10 + 0.5*0
    eu_collapsed = p_h0 * 10 + p_h1 * 0
    results.append(check("Q3", eu_collapsed, "5"))

    # ---- Q4: asymmetric case, expected utility of action u0 ----
    # Inputs: P(h0|o)=0.7, P(h1|o)=0.3, U(u0,h0)=8, U(u0,h1)=2
    # Formula: E[U|u0,o] = 0.7*8 + 0.3*2 = 5.6 + 0.6
    p0 = parse_dec("0.7")
    p1 = parse_dec("0.3")
    eu0_asym = p0 * 8 + p1 * 2
    results.append(check("Q4", eu0_asym, "6.2"))

    # ---- Q5: asymmetric case, expected utility of action u1 ----
    # Inputs: P(h0|o)=0.7, P(h1|o)=0.3, U(u1,h0)=1, U(u1,h1)=9
    # Formula: E[U|u1,o] = 0.7*1 + 0.3*9 = 0.7 + 2.7
    eu1_asym = p0 * 1 + p1 * 9
    results.append(check("Q5", eu1_asym, "3.4"))

    # ---- Q6: epistemic-possibility advantage in the asymmetric case ----
    # Inputs: E[U|u0,o] and E[U|u1,o], each derived above from the stated
    # payoffs and probabilities (0.7/0.3 prior, payoffs {8,2} and {1,9})
    # Formula: Delta_EU = E[U|u0,o] - E[U|u1,o]
    delta = eu0_asym - eu1_asym
    results.append(check("Q6", delta, "2.8"))

    # ---- Q7: belief-storage footprint ----
    # Inputs: |H|=10 hidden states, 8 bytes per floating-point number
    # (implied by the paper's figure of 10 numbers = 80 bytes)
    # Formula: bytes = |H| * bytes_per_float = 10 * 8
    hidden_states = 10
    bytes_per_float = 8
    storage_bytes = hidden_states * bytes_per_float
    results.append(check("Q7", Fraction(storage_bytes), "80"))

    # ---- Q8: expected-utility computation cost per decision step ----
    # Inputs: |U|=5 actions, |H|=10 hidden states
    # Formula: operations = |U| * |H| = 5 * 10
    actions = 5
    ops = actions * hidden_states
    results.append(check("Q8", Fraction(ops), "50"))

    n_total = len(results)
    n_match = sum(1 for r in results if r == "yes")
    n_mismatch = n_total - n_match
    print("VERIFICATION SUMMARY: {} claims, {} match, {} mismatch".format(
        n_total, n_match, n_mismatch))


if __name__ == "__main__":
    main()
