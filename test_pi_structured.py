# Test for Structured Pi Approximation (Nilakantha + φₙ)
# Author: Y.Y.N. Li

from pi_structured_nilakantha import pi_structured_nilakantha
from mpmath import mp, mpf, pi

mp.dps = 50  # Set precision

def run_tests():
    print("Testing Structured π Approximation using Nilakantha + φₙ(n)")
    print("="*65)
    
    # You can tune these parameters:
    α_values = {
        10: 0.8,
        100: 0.79,
        500: 0.7855,
        1000: 0.7854,
        5000: 0.7853985,
        10000: 0.7853982,
    }
    p = 1.0  # Decay exponent (can also try 1.1 or 0.95)

    for n in [10, 100, 500, 1000, 5000, 10000]:
        α = α_values.get(n, 0.7854)  # Use closest pre-tuned α
        approx_pi = pi_structured_nilakantha(n, alpha=α, p=p)
        residual = abs(approx_pi - mp.pi)
        print(f"n = {n:<6} | α = {α}")
        print(f"         | Structured π ≈ {approx_pi}")
        print(f"         | Residual     = {residual}")
        print("-" * 65)

        # Optional strict test assertion:
        assert residual < mpf('0.001'), f"Residual too large for n = {n}"

if __name__ == "__main__":
    run_tests()
