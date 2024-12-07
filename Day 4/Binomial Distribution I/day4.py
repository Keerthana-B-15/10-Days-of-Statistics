#question https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem?isFullScreen=true

from math import comb

# Inputs
p = 1.09 / (1.09 + 1)  # Probability of a boy
n = 6  # Number of children

# Calculate P(X >= 3)
probability = 0
for k in range(3, 7):
    probability += comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Print the result rounded to 3 decimal places
print(f"{probability:.3f}")