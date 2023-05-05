# Name: Shiwen An 
# Date: 2023/05/04
# Purpose: Geometric Brownian Motion
# Paper references: https://galton.uchicago.edu/~mykland/paperlinks/I.A.1-Econometrics_of_High_Frequency_Data.pdf

import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the model
mu = 0.1  # mean return
sigma = 0.2  # volatility
S0 = 100  # initial price
T = 1  # time horizon
N = 252  # number of time steps
dt = T / N  # time step

# Generate random normal variables for the Wiener process
np.random.seed(2077)
z = np.random.normal(size=N)

# Simulate the geometric Brownian motion
S = np.zeros(N+1)
S[0] = S0
for i in range(1, N+1):
    S[i] = S[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z[i-1])

# Plot the results
t = np.linspace(0, T, N+1)
plt.plot(t, S)
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Geometric Brownian Motion Simulation')
plt.show()
