"""
Structured Pi Approximation (Route A)
Author: Y.Y.N. Li
Date: 2025-07-14

π ≈ Leibniz(n) + α(n) · φ(n)
Where:
    - Leibniz(n): Alternating series sum
    - φ(n): Machin-like correction term (fixed)
    - α(n): decaying modulation (e.g., α = 1/n^p)

This model preserves structural modularity, suitable for future Riemann extension.
"""

from mpmath import mp, mpf, fsum, atan, pi
import matplotlib.pyplot as plt
import numpy as np

# Set high precision
mp.dps = 50

# --- Machin-like residual φ(n) ---
def compute_phi():
    # Machin: π = 16 arctan(1/5) - 4 arctan(1/239)
    a_k = [4, -1]
    b_k = [1, 1]
    c_k = [5, 239]
    phi = mpf(0)
    for a, b, c in zip(a_k, b_k, c_k):
        phi += a * atan(mpf(b) / mpf(c))
    return phi

# --- Modulation α(n): decaying with n ---
def alpha(n, p=1.0):
    return mpf(1) / mpf(n)**p

# --- Leibniz partial sum ---
def leibniz_sum(n):
    return fsum([mpf(4) * (-1)**k / (2*k + 1) for k in range(n)])

# --- Structured approximation ---
def pi_structured(n, p=1.0):
    return leibniz_sum(n) + alpha(n, p) * compute_phi()

# --- Run test cases ---
def run_tests():
    true_pi = mp.pi
    phi_fixed = compute_phi()
    ns = [10, 100, 500, 1000, 5000, 10000]
    residuals = []

    print("Testing Structured π Approximation with decay p = {:.1f}".format(p))
    print("="*65)
    for n in ns:
        approx = pi_structured(n, p)
        res = abs(approx - true_pi)
        residuals.append(res)
        print(f"n = {n:<8} | α(n) = {alpha(n, p)}")
        print(f"         | Structured π ≈ {approx}")
        print(f"         | Residual     = {res}")
        print("-"*65)

    # Estimate C: max(|δ(n)| · n)
    C_est = max([residuals[i] * ns[i] for i in range(len(ns))])
    print(f"Estimated C ≈ {C_est}")

    # --- Plot log-log residual curve ---
    plt.figure(figsize=(8,5))
    plt.loglog(ns, [float(r) for r in residuals], marker='o')
    plt.title("Log-Log Residual of Structured π Approximation")
    plt.xlabel("n (terms)")
    plt.ylabel("Residual |π - ρ(n)|")
    plt.grid(True, which='both', ls='--')
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    p = 1.0  # Decay rate
    run_tests()
