import numpy as np
import matplotlib.pyplot as plt

# Redefine the function to compute K(t) for a given pi value with numerically stable methods
def compute_K_stable(t, pi_value):
    # Using log to prevent overflow: Phi(t) = pi^t becomes log(Phi(t)) = t * log(pi)
    log_phi = t * np.log(pi_value)
    
    # Entropy-like function H(t) = |d/dt sin(pi t)|
    h = np.abs(np.gradient(np.sin(pi_value * t), t))
    
    # Avoid log(0) by replacing zeros with a small value
    h[h == 0] = 1e-20
    
    # Compute K(t) = d log H / d log Phi
    log_h = np.log(h)
    dlog_h = np.gradient(log_h, t)
    dlog_phi = np.gradient(log_phi, t)
    K = dlog_h / dlog_phi
    
    return K

# Gradient descent to optimize pi value to minimize |K(t) - 1| with the new stable method
def gradient_descent_stable(t, initial_pi, learning_rate=0.001, iterations=1000):
    pi_value = initial_pi
    errors = []
    
    for i in range(iterations):
        K = compute_K_stable(t, pi_value)
        error = np.abs(K - 1).mean()  # Mean absolute error to 1
        
        # Gradient calculation (approximate using central difference)
        grad_error = np.gradient(np.abs(K - 1)).mean()
        
        # Update pi using the gradient descent step
        pi_value -= learning_rate * grad_error
        
        errors.append(error)
        
        # Early stop if error is sufficiently small
        if error < 1e-6:
            break
    
    return pi_value, errors

# Define time domain (from 1 to 1000, 1000 points)
t_extended = np.linspace(1, 1000, 1000)

# Initial guess for pi
initial_pi = 3.1416

# Run gradient descent to optimize pi with the stable method
optimized_pi_stable, error_history_stable = gradient_descent_stable(t_extended, initial_pi)

# Output the optimized pi and final error
optimized_pi_stable, error_history_stable[-1]

# Compute K(t) using the optimized pi
K_optimized = compute_K_stable(t_extended, optimized_pi_stable)

# Display the first few values of K(t) and the corresponding t values
output_optimized = np.column_stack((t_extended, K_optimized))

# Plot error convergence
plt.figure(figsize=(10, 6))
plt.plot(error_history_stable, label='Error Convergence')
plt.yscale('log')
plt.title('Error Convergence During Optimization of pi to Approach K=1')
plt.xlabel('Iteration')
plt.ylabel('Log(Error)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Display the first 10 values of t and K(t)
output_optimized[:10], optimized_pi_stable, error_history_stable[-1]
