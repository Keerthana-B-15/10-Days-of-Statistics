#question https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem?isFullScreen=true

# Inputs
numerator, denominator = map(int, input().split())  # Probability of a defect
n = int(input())  # The item number where the first defect occurs

# Calculate the probability p of a defect
p = numerator / denominator

# Calculate the probability that the first defect occurs on the nth item
probability = (1 - p) ** (n - 1) * p

# Print the result rounded to 3 decimal places
print(f"{probability:.3f}")
