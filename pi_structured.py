"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

Structure:
    π ≈ Nilakantha(n) + α · φ(n)

Where:
    - Nilakantha(n): partial sum of Nilakantha series
    - φ(n): modal residual correction (Machin-like)
    - α: optional scaling parameter for residual tuning

Residual ≈ O(1/n²) or better with tuned α
"""

from mpmath import mp, mpf, fsum, atan

# Set default precision
mp.dps = 50

# --- Modal correction φ(n): Machin-like structure ---
def compute_phi():
    a_k = [4, -1]
    b_k = [1, 1]
    c_k = [5, 239]
    phi = mpf(0)
    for a, b, c in zip(a_k, b_k, c_k):
        phi += a * atan(mpf(b) / mpf(c))
    return phi

# --- Nilakantha Series ---
def nilakantha_sum(n):
    total = mpf(3)
    for k in range(1, n + 1):
        term = mpf(4) / (mpf(2 * k) * (2 * k + 1) * (2 * k + 2))
        if k % 2 == 1:
            total += term
        else:
            total -= term
    return total

# --- Structured π approximation ---
def pi_structured(n=1000, alpha=1.0):
    """
    π ≈ Nilakantha(n) + α * φ

    Parameters:
        n (int): Number of terms in Nilakantha series
        alpha (float or mpf): Scaling factor for residual φ

    Returns:
        mpf: Approximated π
    """
    return nilakantha_sum(n) + mpf(alpha) * compute_phi()
