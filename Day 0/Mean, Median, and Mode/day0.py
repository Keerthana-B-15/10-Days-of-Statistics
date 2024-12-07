#Question https://www.hackerrank.com/challenges/s10-basic-statistics/problem?isFullScreen=true

from collections import Counter

# Input
n = int(input())  # Number of elements in the array
arr = list(map(int, input().split()))  # Array elements

# Mean
mean = sum(arr) / n

# Median
arr.sort()
if n % 2 == 0:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2
else:
    median = arr[n // 2]

# Mode
freq = Counter(arr)
max_freq = max(freq.values())
modes = [k for k, v in freq.items() if v == max_freq]
mode = min(modes)

# Output
print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)
