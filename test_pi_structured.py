from pi_structured import pi_structured, compute_phi
from mpmath import mp, mpf

mp.dps = 50

def run_tests():
    print("Testing Structured π Approximation using Nilakantha + α·φ(n)")
    print("=" * 65)
    for n in [10, 100, 500, 1000, 5000, 10000]:
        alpha = mpf(1) / n  # or tune as alpha = c / n
        approx_pi = pi_structured(n, alpha=alpha)
        residual = abs(approx_pi - mp.pi)
        print(f"n = {n:<6} | α = {alpha}")
        print(f"         | Structured π ≈ {approx_pi}")
        print(f"         | Residual     = {residual}")
        print("-" * 65)

if __name__ == "__main__":
    run_tests()
