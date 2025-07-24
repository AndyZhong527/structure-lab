Explanation: Pricing American Options via Binomial Tree with Early Exercise Logic
In the Black-Scholes world, European options are priced through backward induction—computing expected payoffs under the risk-neutral measure and discounting them step by step. But this method assumes the option can only be exercised at maturity.

American options introduce a new layer of decision-making: at every single node, the holder may choose to exercise the option early.

This transforms the pricing process from simple expectation into a local optimization problem at each node.

Modeling Shift: From Expectation to max(Immediate, Continuation)
We begin with a standard binomial model:

At each step t, the asset price either moves up by factor u or down by factor d.

The risk-neutral probability is:

q = ((1 + r) - d) / (u - d)

For European options, the value at node (t, i) is given by:

V(t, i) = (1 / (1 + r)) * [ q * V(t+1, i+1) + (1 - q) * V(t+1, i) ]

But for American options, we embed early exercise by taking the maximum between immediate exercise and continuation:

V(t, i) = max( Payoff(S(t, i)), Continuation )

Where:

For a call: Payoff(S) = max(0, S - K)

For a put: Payoff(S) = max(0, K - S)

This max operation is applied at every step of the recursion.

Recursive Algorithm with Early Exercise
Build the price tree using:

S(t, i) = S0 * u^i * d^(t - i)

Initialize payoffs at maturity (t = T):

Call: max(0, S(T, i) - K)

Put: max(0, K - S(T, i))

Perform backward induction with early exercise logic:

Continuation = (1 / (1 + r)) * [ q * V(t+1, i+1) + (1 - q) * V(t+1, i) ]

Then:

V(t, i) = max( Payoff(S(t, i)), Continuation )

The final result V(0, 0) gives the theoretical price of the American option.

What’s New Structurally?
This isn’t just a numerical tweak—it’s a conceptual upgrade:

The max operation at each node turns the tree into a dynamic programming structure.

We no longer solve a pure expectation problem but a sequential decision process.

Early exercise is no longer an edge case—it’s embedded into the core of the valuation structure.

This recursive design reflects the true flexibility granted to American option holders and shows how pricing becomes a locally optimal control problem over a discrete-time process.

