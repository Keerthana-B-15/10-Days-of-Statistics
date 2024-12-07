#question https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem?isFullScreen=true

import math

def calculate_percentage(mean, std_dev, value, greater_than=True):
    z_score = (value - mean) / std_dev
   
    cdf = 0.5 * (1 + math.erf(z_score / math.sqrt(2)))
    
    return 100 * (1 - cdf) if greater_than else 100 * cdf

mean, std_dev = 70, 10
grade1 = 80  # For question 1
threshold = 60  # For questions 2 and 3

percentage_higher_than_80 = calculate_percentage(mean, std_dev, grade1, greater_than=True)

percentage_passing = calculate_percentage(mean, std_dev, threshold, greater_than=True)

percentage_failing = calculate_percentage(mean, std_dev, threshold, greater_than=False)


print(f"{percentage_higher_than_80:.2f}")
print(f"{percentage_passing:.2f}")
print(f"{percentage_failing:.2f}")
