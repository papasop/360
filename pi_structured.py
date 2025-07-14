"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

π ≈ Nilakantha(n) + α · φ(n)
where:
    - Nilakantha(n): Partial sum of the Nilakantha series
    - φ(n): Modal correction (Machin-like)
    - α: scaling parameter to avoid overcorrection
"""

from mpmath import mp, mpf, fsum, atan

mp.dps = 50  # Set high precision

# --- φ(n): Machin-like constant correction ---
def compute_phi():
    a_k = [4, -1]
    b_k = [1, 1]
    c_k = [5, 239]
    phi = mpf(0)
    for a, b, c in zip(a_k, b_k, c_k):
        phi += a * atan(mpf(b) / mpf(c))
    return phi

# --- Nilakantha series: starts from 3 and adds terms from k=1 ---
def nilakantha_sum(n):
    result = mpf(3)
    for k in range(1, n + 1):
        term = mpf(4) / ( (2*k)*(2*k+1)*(2*k+2) )
        if k % 2 == 1:
            result += term
        else:
            result -= term
    return result

# --- Structured π approximation ---
def pi_structured(n=1000, alpha=mpf(0.0)):
    """
    π ≈ Nilakantha(n) + α · φ(n)

    Parameters:
        n (int): Number of terms in Nilakantha series
        alpha (mpf): scaling for φ(n)

    Returns:
        mpf: Structured approximation of π
    """
    return nilakantha_sum(n) + alpha * compute_phi()

