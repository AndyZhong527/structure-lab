# A Recursive Structure for Path-Dependent Decisions: Pricing the Chooser Option

In this project, I explore how to price a chooser option using a multi-period binomial tree. This work emerged from my participation in a research project led by Professor Johannes Ruf at the London School of Economics, where we are studying discrete-time asset pricing under uncertainty.

What fascinates me about the chooser option is that it doesn’t just ask for a price—it asks for a structural answer. Its value is not defined purely by terminal payoffs, but by a decision made halfway through the option’s life: at a predetermined time \( U \), the holder chooses whether the instrument becomes a call or a put. This introduces a recursive structure with embedded logic.

## Modeling as a Decision Process

A binomial tree is not just a tool for computing expectations; it is a finite state space with controllable transitions. At each node \((t, i)\), we compute the underlying asset value using:

\[
S_{t,i} = S_0 \cdot u^i \cdot d^{t-i}
\]

The probability of an upward move under the risk-neutral measure is:

\[
q = \frac{(1 + r) - d}{u - d}
\]

This structure defines a deterministic, directed graph of state evolution. But the chooser option modifies the semantics of the rollback: at time \( U \), the node value is no longer derived from a single continuation—it is chosen as the maximum of two competing subtrees (call and put).

## From Payoff to Policy: Embedding Choice in Recursion

The standard backward induction formula is:

\[
V_{t,i} = \frac{1}{1 + r} \cdot \left( q \cdot V_{t+1,i+1} + (1 - q) \cdot V_{t+1,i} \right)
\]

For the chooser, we introduce a choice at time \( U \):

\[
V^{\text{chooser}}_{U,i} = \max \left( V^{\text{call}}_{U,i},\ V^{\text{put}}_{U,i} \right)
\]

This is not just a change in value—it’s a shift in recursion logic. We're placing a local policy decision into a global valuation structure. Mathematically, this move is consistent with Bellman’s principle: optimal global value is composed of locally optimal actions.

## From Structure to Code

The implementation follows a three-stage pipeline:

1. Build the price tree with all states \((t, i)\);
2. Roll back put and call payoffs separately from \( T \to U \);
3. At layer \( U \), assign each node the max of two branches, then continue rolling back to \( t = 0 \).

The entire model fits into a compact structure, yet it simulates a complex valuation logic: branching decisions under future uncertainty.

## What This Taught Me About Modeling

- A model is not just an equation—it is a machine for conditional value transformation.
- By embedding choice into structure, I moved from computing to **designing a decision system**.
- This project deepened my appreciation for **recursive models as programmable structures**, capable of expressing policies, branching paths, and dynamic control.

This exercise was more than a pricing tool. It was an attempt to understand how decisions and uncertainty intertwine within formal structures—and to simulate that logic through a model of my own design.
