import matplotlib.pyplot as plt
import networkx as nx

S0 = 100
u = 1.2
d = 0.8
r = 0.05
T = 3
K = 100
u_t = 2


q = (1 + r - d) / (u - d)

def build_price_tree(S0, u, d, T):
    tree = {}
    for t in range(T + 1):
        for i in range(t + 1):
            tree[(t, i)] = S0 * (u ** i) * (d ** (t - i))
    return tree

def backward_induction(payoff_terminal, q, r, T, start_t):
    value_tree = {}
    for key in payoff_terminal:
        value_tree[key] = payoff_terminal[key]
    for t in range(T - 1, start_t - 1, -1):
        for i in range(t + 1):
            value_tree[(t, i)] = (q * value_tree[(t + 1, i + 1)] + (1 - q) * value_tree[(t + 1, i)]) / (1 + r)
    return value_tree

price_tree = build_price_tree(S0, u, d, T)

payoff_call_T = {(T, i): max(price_tree[(T, i)] - K, 0) for i in range(T + 1)}
payoff_put_T = {(T, i): max(K - price_tree[(T, i)], 0) for i in range(T + 1)}

call_value_tree = backward_induction(payoff_call_T, q, r, T, u_t)
put_value_tree = backward_induction(payoff_put_T, q, r, T, u_t)

chooser_value_tree = {}
for i in range(u_t + 1):
    chooser_value_tree[(u_t, i)] = max(call_value_tree[(u_t, i)], put_value_tree[(u_t, i)])

for t in range(u_t - 1, -1, -1):
    for i in range(t + 1):
        chooser_value_tree[(t, i)] = (q * chooser_value_tree[(t + 1, i + 1)] +
                                      (1 - q) * chooser_value_tree[(t + 1, i)]) / (1 + r)

G = nx.DiGraph()
labels = {}
for t in range(T + 1):
    for i in range(t + 1):
        node = f"{t},{i}"
        G.add_node(node, pos=(t, -i))
        if t < T:
            G.add_edge(node, f"{t+1},{i}")
            G.add_edge(node, f"{t+1},{i+1}")
        labels[node] = f"{price_tree[(t, i)]:.1f}"

pos = nx.get_node_attributes(G, 'pos')
plt.figure(figsize=(12, 6))
nx.draw(G, pos, with_labels=False, node_size=1200, node_color='lightyellow')
nx.draw_networkx_labels(G, pos, labels, font_size=9)
nx.draw_networkx_edges(G, pos)
plt.title("Stock Price Tree (3-step Binomial Model)")
plt.axis('off')
plt.tight_layout()
plt.show()

chooser_option_price = chooser_value_tree[(0, 0)]
print(f"Chooser Option Price: {chooser_option_price:.4f}")
