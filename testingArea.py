from numpy import array
# array=array([['---' for _ in range(12)] for _ in range(12)])

# print(array)
# for i in range(5):
#     print((1-i)%5)
import numpy as np

# Set print options to show more precision and prevent scientific notation
np.set_printoptions(precision=2, suppress=True)

# Create an array with large numbers
a = np.array([12345, 67890, 1234567, 987654321])

print(a)
