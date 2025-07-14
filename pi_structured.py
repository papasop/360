from mpmath import mp, mpf, fsum, pi

mp.dps = 50  # Precision

# --- Nilakantha series: π = 3 + Σ 4 / (n(n+1)(n+2)) with alternating signs ---
def nilakantha_sum(n):
    terms = []
    for k in range(1, n + 1):
        sign = mpf(1) if k % 2 else mpf(-1)
        denom = (2*k) * (2*k + 1) * (2*k + 2)
        terms.append(sign * mpf(4) / denom)
    return mpf(3) + fsum(terms)

# --- Residual structure φₙ(n): fitted to match π - Nilakantha(n) ---
def residual_phi_n(n, alpha=1.0, p=1.0):
    return mpf(alpha) / n**p

# --- Structured π using Nilakantha + φₙ(n) ---
def pi_structured_nilakantha(n, alpha=1.0, p=1.0):
    return nilakantha_sum(n) + residual_phi_n(n, alpha, p)

# --- Test over range of n ---
def test_structured_nilakantha():
    true_pi = mp.pi
    print("Structured π Approximation: Nilakantha + φₙ(n)")
    print("="*65)
    for n in [10, 100, 500, 1000, 5000, 10000]:
        # You can tune alpha and p for best fit
        alpha = 0.7854  # Close to π − Nilakantha(∞)
        p = 1.0
        approx = pi_structured_nilakantha(n, alpha, p)
        residual = abs(approx - true_pi)
        print(f"n = {n:<6} | Structured π ≈ {approx}")
        print(f"         | Residual     = {residual}")
        print("-"*65)

if __name__ == "__main__":
    test_structured_nilakantha()
