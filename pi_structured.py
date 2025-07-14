"""
Structured π Approximation using Nilakantha Series + α·φ(n)
Author: Y.Y.N. Li
Date: 2025-07-14

This module approximates π using:
    π ≈ Nilakantha(n) + α(n) · φ(n)
Where:
    - Nilakantha(n): partial sum of Nilakantha series
    - φ(n): correction term (≈ π)
    - α(n): dynamic scaling coefficient ~ C/n
"""

from mpmath import mp, mpf, atan, fsum

# Set default precision
mp.dps = 50

# --- Modal correction φ(n) (Machin-like) ---
def compute_phi():
    a_k = [4, -1]
    b_k = [1, 1]
    c_k = [5, 239]
    return fsum([a * atan(mpf(b) / mpf(c)) for a, b, c in zip(a_k, b_k, c_k)])

# --- Nilakantha series: 3 + 4/(2·3·4) - 4/(4·5·6) + ...
def nilakantha_sum(n):
    terms = [mpf(3)]
    sign = 1
    for k in range(1, n + 1):
        a, b, c = 2*k, 2*k+1, 2*k+2
        terms.append(sign * mpf(4) / (a * b * c))
        sign *= -1
    return fsum(terms)

# --- Dynamic α controller ---
def alpha_n(n, C=mp.pi):  # or use empirical C ≈ 0.78539816...
    return C / n

# --- Structured π Approximation ---
def pi_structured_nilakantha(n):
    alpha = alpha_n(n)
    return nilakantha_sum(n) + alpha * compute_phi()

