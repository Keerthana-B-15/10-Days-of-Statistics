#Question https://www.hackerrank.com/challenges/s10-quartiles/problem?isFullScreen=true

def median(arr):
    n = len(arr)
    if n % 2 == 0:
        # For even-length array, return the median as the average of the two middle elements
        return (arr[n // 2 - 1] + arr[n // 2]) // 2
    else:
        # For odd-length array, return the middle element
        return arr[n // 2]

def quartiles(arr):
    # Sort the array
    arr.sort()
    
    n = len(arr)
    # Find Q2 (the median of the entire array)
    q2 = median(arr)
    
    # Split into lower and upper halves for Q1 and Q3
    if n % 2 == 0:
        lower_half = arr[:n // 2]
        upper_half = arr[n // 2:]
    else:
        lower_half = arr[:n // 2]  # Exclude the median element for odd
        upper_half = arr[n // 2 + 1:]  # Exclude the median element for odd
    
    # Find Q1 and Q3 by finding the median of the halves
    q1 = median(lower_half)
    q3 = median(upper_half)
    
    # Print the quartile values separately
    print(q1)
    print(q2)
    print(q3)

# Read input
n = int(input())  # Number of elements in the array
arr = list(map(int, input().split()))  # The array elements

# Call the quartiles function
quartiles(arr)