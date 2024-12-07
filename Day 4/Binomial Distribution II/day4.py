#question https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem?isFullScreen=true

from math import comb

# Inputs
p = 0.12  # Probability of rejection
n = 10    # Batch size

# Function to compute P(X = k)
def binomial_probability(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Calculate P(X <= 2)
p_x_leq_2 = sum(binomial_probability(n, k, p) for k in range(3))

# Calculate P(X >= 2)
p_x_geq_2 = 1 - sum(binomial_probability(n, k, p) for k in range(2))

# Print results rounded to 3 decimal places
print(f"{p_x_leq_2:.3f}")
print(f"{p_x_geq_2:.3f}")
