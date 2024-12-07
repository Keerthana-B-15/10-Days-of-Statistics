#question https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem?isFullScreen=true


# Given values
mean_A, mean_B = 0.88, 1.55

# Daily cost for Machine A: 160 + 40 * (repairs)^2
cost_A = 160 + 40 * (mean_A + mean_A**2)

# Daily cost for Machine B: 128 + 40 * (repairs)^2
cost_B = 128 + 40 * (mean_B + mean_B**2)

# Print the expected daily costs rounded to 3 decimal places
print(f"{cost_A:.3f}")
print(f"{cost_B:.3f}")