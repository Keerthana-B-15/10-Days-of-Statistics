#Question https://www.hackerrank.com/challenges/s10-interquartile-range/problem?isFullScreen=true

def median(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]

def interQuartile(values, freqs):
    # Construct the dataset based on values and frequencies
    data = []
    for value, freq in zip(values, freqs):
        data.extend([value] * freq)
    
    # Sort the dataset
    data.sort()
    
    # Find the median (Q2)
    n = len(data)
    q2 = median(data)
    
    # Split the data into lower and upper halves
    if n % 2 == 0:
        lower_half = data[:n // 2]
        upper_half = data[n // 2:]
    else:
        lower_half = data[:n // 2]  # Exclude the median for odd
        upper_half = data[n // 2 + 1:]  # Exclude the median for odd
    
    # Find Q1 and Q3
    q1 = median(lower_half)
    q3 = median(upper_half)
    
    # Calculate and print the interquartile range
    interquartile_range = q3 - q1
    print(f"{interquartile_range:.1f}")

# Sample input
n = int(input())  # Number of elements
values = list(map(int, input().split()))  # List of values
freqs = list(map(int, input().split()))  # List of frequencies

# Call the function
interQuartile(values, freqs)