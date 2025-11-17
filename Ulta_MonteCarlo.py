import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Monte Carlo Assumptions
# ---------------------------
num_simulations = 10000
S0 = 550                # starting ULTA share price
mu = 0.08               # expected annual return (8%)
sigma = 0.25            # annual volatility (25%)
T = 1                   # 1-year forecast

# ---------------------------
# Run Monte Carlo Simulation
# ---------------------------
final_prices = []

for _ in range(num_simulations):
    # Geometric Brownian Motion formula:
    # S_T = S0 * exp((mu - 0.5*sigma^2)*T + sigma*sqrt(T)*Z)
    Z = np.random.normal(0, 1)
    ST = S0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    final_prices.append(ST)

final_prices = np.array(final_prices)

# ---------------------------
# Print Results
# ---------------------------
print("Monte Carlo Stock Price Projection for ULTA:")
print(f"Median projected price: ${np.median(final_prices):.2f}")
print(f"5th percentile: ${np.percentile(final_prices, 5):.2f}")
print(f"95th percentile: ${np.percentile(final_prices, 95):.2f}")