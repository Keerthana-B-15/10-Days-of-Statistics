#question https://www.hackerrank.com/challenges/s10-standard-deviation/problem?isFullScreen=true


import math

def stdDev(arr):
    # Calculate the mean of the array
    n = len(arr)
    mean = sum(arr) / n
    
    # Calculate the sum of squared deviations from the mean
    squared_deviations = sum((x - mean) ** 2 for x in arr)
    
    # Calculate the standard deviation
    std_deviation = math.sqrt(squared_deviations / n)
    
    # Print the standard deviation rounded to 1 decimal place
    print(f"{std_deviation:.1f}")

# Sample input
n = int(input())  # Size of the array
arr = list(map(int, input().split()))  # Array elements

# Call the function
stdDev(arr)