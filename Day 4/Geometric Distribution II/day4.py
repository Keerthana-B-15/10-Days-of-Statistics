#question https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT# Input
numerator, denominator = map(int, input().split())
n = int(input())

# Probability of a defect
p = numerator / denominator

# Calculate the probability
probability = 1 - (1 - p) ** n

# Print the result rounded to 3 decimal places
print(f"{probability:.3f}")