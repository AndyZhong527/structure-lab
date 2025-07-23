import streamlit as st
import numpy as np
from scipy.stats import norm

st.title("Black-Scholes Call Option Pricer")

S = st.number_input("Current stock price (S)", value=100.0)
K = st.number_input("Strike price (K)", value=100.0)
T = st.number_input("Time to maturity (T, in years)", value=1.0)
r = st.number_input("Risk-free interest rate (r)", value=0.05)
sigma = st.number_input("Annual volatility (σ)", value=0.2)

def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

if T > 0 and sigma > 0:
    price = black_scholes_call(S, K, T, r, sigma)
    st.success(f"The estimated call option price is: ${price:.2f}")
else:
    st.warning("Please ensure that time to maturity and volatility are greater than 0.")
