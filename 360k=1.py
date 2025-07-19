import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# 移除中文字体设置，使用默认字体
# plt.rcParams['font.sans-serif'] = ['Arial']  # 可选，保持英文清晰

# === 第 2-4 节：结构-熵比率 K(t) ===
def phi(t):
    """Structure function Φ(t) = πt"""
    return np.pi * t

def h(t):
    """Entropy function H(t) = |π cos(πt)|"""
    return np.abs(np.pi * np.cos(np.pi * t))

def d_log_phi_dt(t):
    """d/dt log Φ(t) = log π"""
    return np.log(np.pi)

def d_log_h_dt(t):
    """d/dt log H(t) = -π tan(πt), detect singularities"""
    if np.abs(np.cos(np.pi * t)) < 1e-10:
        return np.nan
    return -np.pi * np.tan(np.pi * t)

def K(t):
    """K(t) = d log H(t) / d log Φ(t)"""
    phi_dt = d_log_phi_dt(t)
    h_dt = d_log_h_dt(t)
    if np.isnan(h_dt) or phi_dt == 0:
        return np.nan
    return h_dt / phi_dt

# === 第 7.1 节：求解 t ≈ 0.888774 ===
def t_equation(t):
    """Equation: tan(πt) = -log π / π"""
    return np.tan(np.pi * t) + np.log(np.pi) / np.pi

t_solution = fsolve(t_equation, 0.9)[0]
print(f"Solved t: {t_solution}")
delta = 1 - t_solution
print(f"Calculated δ: {delta}")

# === 第 7.2 节：逆向计算 π ===
def g(p):
    """g(p) = p - exp(p tan(δp))"""
    return p - np.exp(p * np.tan(delta * p))

def g_prime(p):
    """g'(p) = 1 - exp(p tan(δp)) [tan(δp) + p δ sec^2(δp)]"""
    tan_dp = np.tan(delta * p)
    sec2_dp = 1 / np.cos(delta * p)**2
    du_dp = tan_dp + p * delta * sec2_dp
    exp_u = np.exp(p * tan_dp)
    return 1 - exp_u * du_dp

# 牛顿迭代
p = 3.0
tol = 1e-15
iteration = 0
max_iter = 100
print(f"\nNewton iteration initial value: p = {p}, g(p) = {g(p)}")
while abs(g(p)) > tol and iteration < max_iter:
    gp = g_prime(p)
    if gp == 0:
        print("Derivative zero, stopping iteration.")
        break
    p_new = p - g(p) / gp
    print(f"Iteration {iteration+1}: p = {p_new}, g(p) = {g(p_new)}")
    p = p_new
    iteration += 1
print(f"Final p: {p} (close to π = {np.pi})")

# === 第 6 节：数值模拟 K(t) ===
t1 = np.linspace(0.01, 0.49, 100)
t2 = np.linspace(0.51, 0.99, 100)
t = np.concatenate([t1, t2])
K_values = [K(t_val) for t_val in t]

# 可视化 K(t)
plt.figure(figsize=(10, 6))
plt.plot(t, K_values, label='K(t)', color='blue')
plt.axhline(y=1, color='red', linestyle='--', label='K = 1')
plt.axvline(x=t_solution, color='green', linestyle=':', label=f't ≈ {t_solution:.6f}')
plt.xlabel('t')
plt.ylabel('K(t)')
plt.title(r'$K(t) = -\frac{\pi \tan(\pi t)}{\log \pi}$ Simulation')
plt.ylim(0.5, 1.5)
plt.legend()
plt.grid(True)
plt.savefig('K_t_simulation.png', dpi=300)
plt.show()

print(f"\nCheck K(t) at t ≈ {t_solution}: K(t) = {K(t_solution)}")