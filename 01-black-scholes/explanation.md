## 01 – Replicating Uncertainty: Black-Scholes

In this module, I implement the classical Black-Scholes formula and reflect on its structural implications. The key idea is **replication**: constructing a portfolio that continuously mimics the option's price path using a dynamic combination of stock and risk-free assets.

This is not just a pricing formula. It's a statement:
> We can create certainty out of randomness — not by predicting, but by structuring.

---

### Model Overview

- **Core Idea**: Build a replicating portfolio such that its value evolution matches the option's value path in a continuous world.
- **Mathematical Assumptions**:
  - Stock price follows geometric Brownian motion.
  - Markets are frictionless and continuous.
  - Hedging is done infinitely frequently.
- **Key Formula**:
C = S0 * N(d1) - K * exp(-rT) * N(d2)
This elegant formula hides a deep structural insight: we’re not guessing outcomes — we’re constructing a world where they don’t matter.

---

### 📁 Files

- `bs_pricer.py`: Python implementation of Black-Scholes pricing (European call).
- `bs_curve.png`: Optional visualization showing how price changes with volatility.
- Blog: [bs-reflection.md](../06-essays/bs-reflection.md)

---

### 💬 Reflection Snapshot

I used to think Black-Scholes was about guessing how much a right to buy something was worth. Then I learned it was about constructing a **structure that works under uncertainty**.

The first time I saw the formula, I didn’t understand it. The first time I tried to build it, I realized I didn’t have to — I only had to build the logic behind it.


