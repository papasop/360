from pi_structured import pi_structured
from mpmath import mp, mpf

mp.dps = 50

def run_tests():
    print("Testing Structured π Approximation using Nilakantha + φ(n)")
    print("=" * 65)
    for n in [10, 100, 500, 1000, 5000, 10000]:
        approx_pi = pi_structured(n, alpha=1.0)
        residual = abs(approx_pi - mp.pi)
        print(f"n = {n:<6} | Structured π ≈ {approx_pi}")
        print(f"         | Residual     = {residual}")
        print("-" * 65)

if __name__ == "__main__":
    run_tests()
