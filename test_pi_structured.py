from pi_structured_nilakantha import pi_structured_nilakantha, alpha_n
from mpmath import mp, mpf, pi

mp.dps = 50  # Set precision

def run_tests():
    print("Testing Structured π Approximation using Nilakantha + α(n)·φ(n)")
    print("="*65)
    for n in [10, 100, 500, 1000, 5000, 10000]:
        approx = pi_structured_nilakantha(n)
        residual = abs(pi - approx)
        alpha = alpha_n(n)
        print(f"n = {n:<8} | α(n) = {alpha}")
        print(f"         | Structured π ≈ {approx}")
        print(f"         | Residual     = {residual}")
        print("-"*65)

if __name__ == "__main__":
    run_tests()
