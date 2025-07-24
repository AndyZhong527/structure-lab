import math

def build_price_tree(S0, u, d, T):
    price_tree = {}
    for t in range(T + 1):
        for i in range(t + 1):
            S = S0 * (u ** i) * (d ** (t - i))
            price_tree[(t, i)] = S
    return price_tree

def price_american_option(S0, K, T, r, u, d, option_type="call"):
    # Risk-neutral probability
    q = (1 + r - d) / (u - d)

    # Step 1: Build stock price tree
    price_tree = build_price_tree(S0, u, d, T)

    # Step 2: Initialize option value at maturity
    value_tree = {}
    for i in range(T + 1):
        S = price_tree[(T, i)]
        if option_type == "call":
            value_tree[(T, i)] = max(S - K, 0)
        elif option_type == "put":
            value_tree[(T, i)] = max(K - S, 0)

    # Step 3: Backward induction with early exercise
    for t in reversed(range(T)):
        for i in range(t + 1):
            S = price_tree[(t, i)]
            continuation = (q * value_tree[(t + 1, i + 1)] + (1 - q) * value_tree[(t + 1, i)]) / (1 + r)
            if option_type == "call":
                exercise = max(S - K, 0)
            elif option_type == "put":
                exercise = max(K - S, 0)
            value_tree[(t, i)] = max(continuation, exercise)

    return value_tree[(0, 0)]
