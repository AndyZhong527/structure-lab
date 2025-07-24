# 05-early-exercise-american

This project implements a binomial model for pricing American-style options, where early exercise is allowed at each node of the tree. Unlike European options, American options introduce an optimal stopping rule: the holder can choose to exercise at any point before maturity.

## Core Idea

At each node $(t, i)$, we compare:

1. The immediate exercise value:
   - For call: $\max(S - K, 0)$  
   - For put: $\max(K - S, 0)$

2. The continuation value:

$$
V_{t,i} = \frac{1}{1 + r} \left[ q \cdot V_{t+1, i+1} + (1 - q) \cdot V_{t+1, i} \right]
$$

Then we take the maximum of the two:

$$
V_{t,i} = \max\left( \text{exercise value},\ \text{continuation value} \right)
$$

This logic ensures that the optimal decision (exercise or continue) is embedded directly in the recursive structure.

## Features

- General binomial tree with parameters $(S_0, u, d, r, K, T)$
- Early-exercise logic at every node
- Supports both call and put payoff structures
- Written in Python, designed for readability and extendability

## What I Learned

This project made me realize that pricing American options is essentially a problem of **dynamic programming with local optimality**. At every point in the tree, a decision must be made based on two competing values.

This forced me to structure the code as a recursive control system, rather than a plain calculator. I learned to think in terms of:

- Finite state spaces
- Backward induction with branching conditions
- Local decision rules that preserve global consistency

## Example Output

![option_tree](./density_plot.png)

## Future Work

- Add visualization of early-exercise regions
- Extend to dividend-paying stocks
- Experiment with different trees (e.g., trinomial or adaptive grid)

