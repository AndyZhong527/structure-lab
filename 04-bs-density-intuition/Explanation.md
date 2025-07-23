A Visual Insight into Black-Scholes Density and Impact
When I first learned the Black-Scholes formula:

$$
C = S_0 \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
$$
…I thought I understood it. But soon I realized: I didn’t understand why the standard normal distribution appears here, or how it shapes the final option value.

I decided to take a detour and ask one basic question:

What does the density curve really do in this model?

🔍 Step 1 – Defining the Density
The Black-Scholes model assumes that the log return of the asset is normally distributed. That gives rise to the standard normal PDF:

$$
\phi(x) = \frac{1}{\sqrt{2\pi}} \cdot e^{-x^2 / 2}
$$
The call option price involves the cumulative probability:

$$
N(x) = \int_{-\infty}^{x} \phi(t) \, dt
$$
So we have:

$$
d_1 = \frac{\ln(S_0 / K) + (r + \frac{1}{2} \sigma^2)T}{\sigma \sqrt{T}}, \quad
d_2 = d_1 - \sigma \sqrt{T}
$$
And the full pricing formula:

$$
C = S_0 \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
$$
But here’s the surprising part:

Even though the formula looks deterministic, it hides a distribution underneath—a shifted and scaled Gaussian.

🧠 Step 2 – Misconception: "Density = Importance"
At first, I naively believed: “The density at a point tells us how important that point is to pricing.”

But I was wrong. A higher density does not mean higher influence.

A probability density is not a weight—it’s a “density of weight.” The real influence comes from integrating that density over a region.

So although a spike in the middle of the distribution looks prominent, it only contributes proportionally to the area under the curve.

This distinction is subtle but crucial. It changed how I read $N(d_2)$: not as a value from the curve, but as a measure of cumulative probability weight—that is, the total “mass” under the curve to the left of $d_2$.

📈 Step 3 – Visualizing Density Under Different Volatilities
To explore this, I plotted $\phi(x)$ for different values of $\sigma$.

What I found:

Higher $\sigma$ spreads the curve wider and flattens it;

$d_1$ and $d_2$ shift in response, changing the values of $N(d_1)$ and $N(d_2)$;

But the shape of $\phi$ doesn’t determine pricing—it’s how the cumulative weight shifts.

This helped me see Black-Scholes not as a fixed formula, but as a re-weighting mechanism under uncertainty.

🧭 What I Learned
Mathematical models like Black-Scholes don’t predict, they compress uncertainty into structural expectations.

Visualizing densities helped me break free from symbolic manipulation and actually see the logic behind the math.

I used to believe understanding meant derivation. Now I think it means: knowing what part of a formula actually moves, and why.

This project reminded me that mathematical intuition often comes after the formula—not before.

