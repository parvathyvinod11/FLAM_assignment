"""
visualize.py
------------
Plot actual data points against the fitted parametric curve.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_results(actual, fitted, theta_deg, M, X, score, save_path="results.png"):
    """
    Create a scatter + line overlay plot and save to results.png.

    Parameters
    ----------
    actual    : np.ndarray  shape (N, 2)  actual (x, y) data points
    fitted    : np.ndarray  shape (M, 2)  predicted curve points
    theta_deg : float       estimated theta in degrees
    M         : float       estimated M
    X         : float       estimated X
    score     : float       final mean L1 distance
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot actual data points
    ax.scatter(
        actual[:, 0], actual[:, 1],
        s=8, alpha=0.5, color="steelblue",
        label=f"Actual data ({len(actual)} points)",
        zorder=2,
    )

    # Plot fitted curve
    ax.plot(
        fitted[:, 0], fitted[:, 1],
        color="orangered", linewidth=2,
        label="Fitted curve",
        zorder=3,
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(
        f"Parametric Curve Fitting — FlamApp Assignment\n"
        f"θ = {theta_deg:.4f}°   M = {M:.6f}   X = {X:.4f}   "
        f"Mean L1 = {score:.4f}"
    )
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    # plt.show()
    print(f"Plot saved → {save_path}")
