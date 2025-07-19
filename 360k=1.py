import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def phi(t): return np.pi * t
def h(t): return np.abs(np.pi * np.cos(np.pi * t))
def d_log_phi_dt(t): return np.log(np.pi)
def d_log_h_dt(t):
    if np.abs(np.cos(np.pi * t)) < 1e-10: return np.nan
    return -np.pi * np.tan(np.pi * t)
def K(t):
    phi_dt = d_log_phi_dt(t)
    h_dt = d_log_h_dt(t)
    if np.isnan(h_dt) or phi_dt == 0: return np.nan
    return h_dt / phi_dt

def t_equation(t): return np.tan(np.pi * t) + np.log(np.pi) / np.pi
t_solution = fsolve(t_equation, 0.9)[0]
delta = 0.111226

def g(p): return p - np.exp(p * np.tan(delta * p))
def g_prime(p):
    tan_dp = np.tan(delta * p)
    sec2_dp = 1 / np.cos(delta * p)**2
    du_dp = tan_dp + p * delta * sec2_dp
    exp_u = np.exp(p * tan_dp)
    return 1 - exp_u * du_dp

p = 3.0
tol = 1e-15
iteration = 0
max_iter = 100
print(f"Solved t: {t_solution}")
print(f"Calculated δ: {delta}")
print(f"\nNewton iteration initial value: p = {p}, g(p) = {g(p)}")
while abs(g(p)) > tol and iteration < max_iter:
    gp = g_prime(p)
    if gp == 0: print("Derivative zero, stopping."); break
    p_new = p - g(p) / gp
    print(f"Iteration {iteration+1}: p = {p_new}, g(p) = {g(p_new)}")
    p = p_new
    iteration += 1
print(f"Final p: {p} (close to π = {np.pi})")

t1 = np.linspace(0.8, 0.95, 200)
K_values = [K(t_val) for t_val in t1]

plt.figure(figsize=(10, 6))
plt.plot(t1, K_values, label='K(t)', color='blue')
plt.axhline(y=1, color='red', linestyle='--', label='K = 1')
plt.axvline(x=t_solution, color='green', linestyle=':', label=f't ≈ {t_solution:.6f}')
plt.xlabel('t')
plt.ylabel('K(t)')
plt.title(r'$K(t) = -\frac{\pi \tan(\pi t)}{\log \pi}$ Simulation near K = 1')
plt.ylim(0.9, 1.1)
plt.legend()
plt.grid(True)
plt.savefig('K_t_simulation_improved.png', dpi=300)
plt.show()

print(f"\nCheck K(t) at t ≈ {t_solution}: K(t) = {K(t_solution)}")