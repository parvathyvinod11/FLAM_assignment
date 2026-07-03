# Parametric Curve Fitting — FlamApp AI Assignment

## Problem

Given a set of (x, y) data points sampled from a parametric curve, estimate the unknown parameters **θ (theta)**, **M**, and **X** that best fit the data.

The curve is defined by:

```
x(t) = t·cos(θ) − exp(M·|t|)·sin(0.3t)·sin(θ) + X
y(t) = 42 + t·sin(θ) + exp(M·|t|)·sin(0.3t)·cos(θ)
```

**Parameter constraints:**
- `0° < θ < 50°`
- `-0.05 < M < 0.05`
- `0 < X < 100`
- `6 ≤ t ≤ 60`

---

## Approaches Evaluated

### 1. Basic Optimization (`basic_minimize/`)
Uses `scipy.optimize.minimize` (Nelder-Mead). While simpler, it is prone to getting stuck in local minima due to the highly non-convex nature of the parameter space (specifically the `sin(0.3t)` oscillation term). 

### 2. Global Optimization (`differential_evolution/`)
Uses `scipy.optimize.differential_evolution`. This performs a global search across the parameter bounds, avoiding local minima to reliably find the optimal fit.

---

## Results

| Parameter | Estimated Value |
|-----------|----------------|
| θ (theta) | **30.0004°** |
| M         | **0.029999**  |
| X         | **55.0006**   |
| Mean L1 score | **0.0194** |

*(Check the `differential_evolution/results.png` for the final plot).*

### Desmos / LaTeX Submission String
As required, here is the LaTeX string representation of the fitted curve (using the optimal parameters), ready to be copied into Desmos:

```latex
\left(t*\cos(0.5236)-e^{0.0300\left|t\right|} \cdot\sin(0.3t)\sin(0.5236)+55.0006, 42+t*\sin(0.5236)+e^{0.0300\left|t\right|} \cdot\sin(0.3t)\cos(0.5236)\right)
```

---

## How to Run

**1. Install dependencies:**
```bash
pip install -r requirements.txt
```

**2. Run the basic fit:**
```bash
python basic_minimize/fit_curve.py
```

**3. Run the optimized fit:**
```bash
python differential_evolution/fit_curve.py
```

---

## Dependencies

- Python 3.9+
- numpy, pandas, scipy, matplotlib
