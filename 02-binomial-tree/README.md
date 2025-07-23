# Binomial Model for Pricing a Chooser Option

This project implements a multi-period binomial tree to price a **chooser option**—a financial derivative where the holder decides at a future time whether the option becomes a call or a put.

It is inspired by my research participation under Professor Johannes Ruf at LSE, and serves as a structural modeling exercise in recursive pricing under uncertainty.

## Key Features

- Recursive valuation using backward induction
- Embedded decision logic at the chooser moment \( t = U \)
- Risk-neutral pricing with clear model assumptions
- Visualization of the price tree using NetworkX and Matplotlib
- Fully written in Python with modular design

## Project Structure

- `binomial_chooser.py`: core implementation of the pricing algorithm
- `price_tree_plot.py`: visualization of the price tree structure
- `explanation.md`: mathematical rationale and modeling insight
- `demo_output.png`: example of tree visualization output
- `README.md`: project overview

## How to Run

```bash
# Clone repository
git clone https://github.com/your-username/binomial-chooser.git
cd binomial-chooser

# Install dependencies
pip install matplotlib networkx

# Run pricing + plot
python binomial_chooser.py
python price_tree_plot.py
