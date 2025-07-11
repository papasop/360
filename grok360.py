import numpy as np

delta = 1 - 0.8887740553300749

def g(p):
    return p - np.exp(p * np.tan(delta * p))

def g_prime(p):
    tan_dp = np.tan(delta * p)
    sec2_dp = 1 / np.cos(delta * p)**2
    du_dp = tan_dp + p * delta * sec2_dp
    exp_u = np.exp(p * tan_dp)
    return 1 - exp_u * du_dp

p = 3.0  # initial guess
tol = 1e-15
iteration = 0
max_iter = 100
print(f"Initial p: {p}, g(p): {g(p)}")
while abs(g(p)) > tol and iteration < max_iter:
    gp = g_prime(p)
    if gp == 0:
        print("Derivative zero, stopping.")
        break
    p_new = p - g(p) / gp
    print(f"Iteration {iteration+1}: p = {p_new}, g(p) = {g(p_new)}")
    p = p_new
    iteration += 1
print(f"Final p: {p}")