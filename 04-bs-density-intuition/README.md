# 04-bs-density-intuition

A visual exploration of the role that probability **density functions** play in the Black-Scholes model. This project investigates a subtle but important misconception: **high density ≠ high contribution to option value**.

While the Black-Scholes formula is often taught as a deterministic pricing tool, it fundamentally rests on **integrating Gaussian density** across regions of interest. This notebook uses Python to visualize standard normal PDFs under different volatilities and re-examines the mathematical structure of:

- $N(d_1)$ and $N(d_2)$ in the call price formula;
- The influence of $\sigma$ (volatility) on the shape and weight of the density;
- The shift from **point value** to **cumulative mass** understanding.

## Key Outputs

![Density Comparison under Different Volatilities](./assets/density_plot.png)

> Visualizing the standard normal PDF for various $\sigma$ values reveals how **weight distribution** (not density height) drives option price changes.

## Why This Matters

In Black-Scholes pricing:
- $N(d_2)$ is not just a lookup from a normal distribution—it represents the **probability-weighted discount factor** of the strike price.
- Misinterpreting densities as weights leads to false intuitions about model sensitivity.
- By viewing the formula through the lens of integration, we gain better control over **which parts of the uncertainty space contribute most**.

This project emphasizes a structural view: from “just calculating” to **understanding how models embed probability mass into valuation**.

## How to Run

1. Clone the repo:

```bash
git clone https://github.com/your-username/04-bs-density-intuition.git
cd 04-bs-density-intuition
