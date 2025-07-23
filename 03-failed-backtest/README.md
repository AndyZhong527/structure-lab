## ✅ README.md

This repository documents my failed attempt to backtest a simple SMA crossover strategy on AAPL stock using Python. While the strategy never worked as intended, the process exposed deeper flaws in my thinking and forced me to reflect on modeling structure.

## What I Tried

- Downloaded AAPL data using `yfinance`
- Computed 20-day and 50-day simple moving averages
- Planned to buy when SMA20 > SMA50 and sell otherwise
- Tried simulating trades using a `for` loop and `if-else` blocks

## What Went Wrong

- Encountered ambiguous Series comparison errors
- Realized I hadn’t designed a proper state-tracking system
- Misunderstood how variables and conditions interact in vectorized logic
- Failed to define transitions and memory in a discrete system

## Key Takeaways

- Backtesting is a **discrete-time state simulation problem**, not just rule evaluation
- Code that runs may still be **semantically broken**
- Modeling requires thinking about **structure**, not just syntax
- A failed build can teach more than a polished result

## Files

- `explanation.md`: My full reflection on what went wrong and what I learned
- `backtest_attempt.ipynb`: The incomplete or buggy notebook used in the experiment
- (Optional) `images/`: Any related screenshots or visuals

## Why This Matters

This project stays in my portfolio not because it succeeded, but because it exposed my gaps—and showed me what kind of thinking I need to grow into. It marks the point where I began to shift from coding toward structural modeling.
