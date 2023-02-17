import numpy as np

numbers = [1, 2, 3, 4, 5]

n = 75  # The desired percentile, expressed as a percentage

percentile = np.percentile(numbers, n)

print(percentile)
