# Black-Scholes Option Pricer

This module implements a simple **European call option pricer** based on the Black-Scholes model, using Python and Streamlit.

It is part of the [Structure-Lab](https://github.com/yourname/structure-lab) project, which explores how abstract mathematical structures can be operationalized as functional models.

---

## Core Idea

> A mathematical formula is not just something to calculate with, but something to construct with.

The Black-Scholes model provides a closed-form solution for option pricing under specific assumptions about the market. This module implements it as a real-time, interactive web tool. Rather than solving the equation once, the model is re-expressed as a **computational function**, mapping current market states to fair prices.

---

## Demo

To run locally:

```bash
pip install streamlit numpy scipy
streamlit run app.py
