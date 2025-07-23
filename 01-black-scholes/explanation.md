# Black-Scholes: From Formula to Structure

> *"A mathematical model only becomes yours once you can run it."*

After I first studied the Black-Scholes model, I couldn’t stop thinking about it. To truly *understand* such a formula, I felt it wasn’t enough to read the derivation — I had to implement it myself.

So I built a simple European call option pricing tool using Python and Streamlit. Given five input parameters, it returns the theoretical price in real time.

It may seem like a small “finance utility” project, but to me it was a deeper transformation — from understanding a formula to constructing a working structure. It was my first attempt at turning a canonical mathematical model into an actual programmable system.

---

## 📘 A Brief Overview of Black-Scholes

The Black-Scholes model prices European-style options under several key assumptions:

- The underlying follows geometric Brownian motion;
- Markets are frictionless (no transaction costs, infinitely divisible assets);
- No arbitrage;
- Constant risk-free rate.

Its famous closed-form solution is:

$$
C = S_0 N(d_1) - Ke^{-rT} N(d_2)
$$

Where:

- \( S_0 \): current stock price  
- \( K \): strike price  
- \( T \): time to maturity  
- \( r \): risk-free rate  
- \( \sigma \): volatility (estimated from historical data)  
- \( N(d) \): standard normal CDF

And:

$$
d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma \sqrt{T}}, \quad d_2 = d_1 - \sigma \sqrt{T}
$$

This model is deeply mathematical — it begins from stochastic processes and uses tools like Itô's Lemma and PDEs to arrive at a pricing equation. Although I haven’t yet learned PDE derivation in full, I understand the goal: to use probabilistic and differential structures to represent a nonlinear payoff.

---

## 💻 Code Implementation

The entire app is about 30 lines of Python, using:

- `numpy` for math operations (log, sqrt, etc.);
- `scipy.stats.norm.cdf` for the cumulative normal function;
- `streamlit` for the user interface and real-time interactivity.

Although I’m more familiar with Java, I intentionally chose Python — it's the default language in quantitative finance, supported by a powerful data science ecosystem. It also encouraged me to write cleaner, more expressive code for demonstration.

Here are a few core implementation choices that shaped my thinking:

- Turning abstract variables into interactive inputs;
- Handling edge cases like \(\sigma = 0\) or \(T = 0\);
- Structuring code to preserve mathematical clarity and logical flow.

This wasn’t just “coding a formula” — it was a shift in mindset: from symbolic math to computational structures.

---

## 🧠 What I Really Learned

### 1. Models are State Functions, Not Just Formulas

Black-Scholes isn’t just a solution — it’s a **mapping** from market state to fair value. Behind it lies the concept of **risk-neutral valuation**, where the expected return of assets equals the risk-free rate in a transformed probability space:

> "In this rescaled world, pricing becomes a weighted average — a probabilistic expectation over future paths."

This reframed how I think about modeling: not as predicting the future, but compressing uncertainty into interpretable structure.

### 2. Implementing a Model = Rewriting Mathematics into Structure

The act of implementing a formula in code is an act of **mathematical translation**. I wasn’t just computing — I was learning how to turn:

- variables → inputs  
- expressions → executable functions  
- limits → algorithms

This transformation is what I now see as the core of modeling.

### 3. Even If I Can’t Derive the PDE, I Can Grasp the Design Intent

I don’t yet have the tools to derive the full Black-Scholes PDE. But I do understand its purpose: **to create a structure that controls uncertainty** — to ask which parameters can be moved, adjusted, or hedged.

That’s the kind of structural control I want to understand better — from probability measures to partial derivatives, from diffusion to delta hedging.

---

## 🧩 Future Extensions

This tool is simple for now, but I have several ideas:

- Add support for put options;
- Visualize how price changes with volatility and time;
- Deploy the app to the web (via Streamlit Cloud or HuggingFace Spaces);
- Rebuild the same tool in Java, starting from zero, as a way to challenge myself with lower-level construction.

---

## 🎯 Final Thought

I don’t want to be just a student who can “solve problems.”  
I want to be someone who can **build systems** that bring mathematical models to life.

