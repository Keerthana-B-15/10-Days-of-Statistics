#Question https://www.hackerrank.com/challenges/s10-weighted-mean/problem?isFullScreen=true

def weightedMean(X, W):
    # Calculate the weighted mean
    weighted_sum = sum(x * w for x, w in zip(X, W))
    total_weights = sum(W)
    mean = weighted_sum / total_weights
    
    # Print the weighted mean rounded to 1 decimal place
    print(f"{mean:.1f}")

# Input
n = int(input())  # Number of elements
X = list(map(int, input().split()))  # Array of values
W = list(map(int, input().split()))  # Array of weights

# Calculate and print the weighted mean
weightedMean(X, W)