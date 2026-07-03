"""
fit_curve.py (Basic minimize approach)
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize
import sys
import os

# Import visualize from parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from visualize import plot_results

# 1. Load data
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "xy_data.csv")
df = pd.read_csv(data_path)
df.columns = [c.strip().lower() for c in df.columns]
df = df[["x", "y"]].dropna()
data = df.values

# 2. Parametric curve model
T_opt = np.linspace(6, 60, 300) # Faster grid for optimization

def generate_curve(theta, M, X, t_vals):
    exp_part = np.exp(M * np.abs(t_vals))
    sin_part = np.sin(0.3 * t_vals)
    x = t_vals * np.cos(theta) - exp_part * sin_part * np.sin(theta) + X
    y = 42 + t_vals * np.sin(theta) + exp_part * sin_part * np.cos(theta)
    return np.column_stack([x, y])

# 3. Objective function
def mean_l1_distance(params):
    theta, M, X = params
    curve = generate_curve(theta, M, X, T_opt)
    l1 = np.abs(data[:, None, :] - curve[None, :, :]).sum(axis=2)
    return l1.min(axis=1).mean()

# 4. Optimization
print("Running basic scipy.optimize.minimize...")

x0 = [np.radians(25), 0.01, 50]

result = minimize(
    mean_l1_distance, 
    x0=x0, 
    method='Nelder-Mead',
    options={'disp': True, 'maxiter': 1000}
)

theta, M, X = result.x
theta_deg = np.degrees(theta)
score = result.fun

print("  Final Estimated Parameters (Basic Minimize)")
print()
print(f"  theta = {theta_deg:.4f} degrees  ({theta:.6f} rad)")
print(f"  M     = {M:.6f}")
print(f"  X     = {X:.4f}")
print(f"  L1 score = {score:.6f}  (lower is better)")
print()

# Save Desmos equation
desmos = (
    "Desmos Parametric Equations\n"
    "Domain: 6 <= t <= 60\n\n"
    f"x(t) = t*cos({theta:.6f}) - exp({M:.6f}*abs(t))*sin(0.3*t)*sin({theta:.6f}) + {X:.4f}\n"
    f"y(t) = 42 + t*sin({theta:.6f}) + exp({M:.6f}*abs(t))*sin(0.3*t)*cos({theta:.6f})\n"
)
out_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(out_dir, "desmos_equation.txt"), "w") as f:
    f.write(desmos)
print("Desmos equation saved to desmos_equation.txt")

# Plot and save
T_plot = np.linspace(6, 60, 800)
fitted_curve = generate_curve(theta, M, X, T_plot)
plot_results(data, fitted_curve, theta_deg, M, X, score, save_path=os.path.join(out_dir, "results.png"))
