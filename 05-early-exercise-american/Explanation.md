# Explanation: American Option Pricing with Early Exercise

This explanation outlines the core logic, model structure, and implementation details behind pricing **American-style options** using a **binomial tree** with **early exercise** logic.

## Background

European options can only be exercised at expiry. American options, however, allow the holder to **exercise at any time** before maturity. This flexibility makes them **more valuable**—and **harder to price**.

In a binomial model, pricing a European option involves simple **backward induction**:

$$
V_{t,i} = \frac{1}{1 + r} \left[ q \cdot V_{t+1, i+1} + (1 - q) \cdot V_{t+1, i} \right]
$$

However, for American options, we must **check at every node** whether it is optimal to **exercise early**, or continue holding the option.

## Pricing Logic

At each node $(t, i)$ of the binomial tree:

- Compute the **stock price** at that node:

$$
S_{t,i} = S_0 \cdot u^i \cdot d^{t - i}
$$

- Compute the **exercise value**:
  - For call: $\max(S_{t,i} - K, 0)$  
  - For put: $\max(K - S_{t,i}, 0)$

- Compute the **continuation value**:

$$
V_{t,i}^{\text{cont}} = \frac{1}{1 + r} \left[ q \cdot V_{t+1, i+1} + (1 - q) \cdot V_{t+1, i} \right]
$$

- Final value at node:

$$
V_{t,i} = \max\left( V_{t,i}^{\text{cont}},\ \text{exercise value} \right)
$$

This process ensures **local optimality** at each node, which builds into a **globally consistent solution** via backward induction.

## Implementation Notes

1. The model is fully implemented in Python.
2. The algorithm builds a binomial tree of prices, then performs backward induction from $t = T$ to $t = 0$.
3. At each step, we evaluate and store the maximum of:
   - Immediate exercise payoff
   - Discounted expected continuation value

The option’s fair price is then the value at the root node $(0,0)$.

## Why This Matters

This model taught me how **decision-making logic** can be embedded into a **recursive system**. Pricing is no longer just expectation—it becomes a form of **control**, where the system must “choose” the optimal path at every point in time.

It also reinforced key modeling principles:

- **Finite-state modeling** with transition logic
- **Backward induction** over recursive structures
- **Optimal stopping problems** in discrete-time finance

Ultimately, this was more than a pricing task—it was an exercise in turning mathematical reasoning into structural logic.
