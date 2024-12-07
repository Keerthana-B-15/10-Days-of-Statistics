#question https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem?isFullScreen=true

import math

# Input values
mean = 2.5
k = 5

# Poisson formula
probability = (mean**k * math.exp(-mean)) / math.factorial(k)

# Output rounded to 3 decimal places
print(f"{probability:.3f}")