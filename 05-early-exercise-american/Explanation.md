Pricing American Options via Binomial Tree with Early Exercise Logic
In the Black-Scholes world, European options are priced by backward induction—calculating the expected payoff under the risk-neutral measure and discounting it step by step. But this logic assumes the option can only be exercised at maturity.

American options are different. They introduce an extra layer of decision-making: at every single step, the holder may choose to exercise the option early.

This transforms the model from a simple recursive expectation to a local optimization problem at every node.

The Modeling Shift: From Expectation to Max(Immediate, Continuation)
Let’s consider a standard binomial model:

At each time step t, the asset price either moves up by a factor u or down by a factor d.

The risk-neutral probability q is computed as:

q = ((1 + r) - d) / (u - d)
For a European option, the value at node (t, i) is computed by taking the discounted expected value from the next step:

V(t, i) = (1 / (1 + r)) * (q * V(t+1, i+1) + (1 - q) * V(t+1, i))
But for an American option, we modify this as:

V(t, i) = max( Payoff(S(t, i)), ContinuationValue )
Where:

Payoff(S) = immediate exercise value at the current node

ContinuationValue = same as the European-style expected discounted value

This logic must be applied at every step of the backward induction, starting from the terminal payoff and moving backward to the root.

Algorithm Logic: Early Exercise Embedded in Recursion
The structure of the valuation process:

Build the price tree using:

S(t, i) = S0 * (u^i) * (d^(t - i))
Initialize final payoffs at t = T, using:

Call: max(0, S(T, i) - K)
Put:  max(0, K - S(T, i))
Roll back the tree:

At each (t, i), compute:

Continuation = (1 / (1 + r)) * (q * V(t+1, i+1) + (1 - q) * V(t+1, i))
Exercise = max(0, S(t, i) - K)    # for call
          or
          max(0, K - S(t, i))     # for put

V(t, i) = max(Continuation, Exercise)
This recursive step embeds an early-exercise decision rule directly inside the model structure.

Why This Matters: Embedding Decisions into Models
What makes this powerful is not just the pricing result, but the structural change it introduces. You’re no longer computing pure expectations—you’re encoding local decision logic into the recursion.

This reflects a higher-dimensional modeling mindset:

From valuation → optimization

From single path → decision at every node

From expected future → maximum controllable present

It’s not just a math trick. It’s the beginning of turning a financial formula into a decision-aware system.
