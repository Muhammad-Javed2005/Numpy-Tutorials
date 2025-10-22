# Author : Muhammad Javed


import numpy as np

# Important Note:
    # If you want to perform operation **column-wise**, use "axis = 0"
    # If you want to perform operation **row-wise**, use "axis = 1"



# Aggregation Function:


arr_4= np.arange(50 , 98 , 2).reshape(2 , 3 , 4)
print(arr_4)


# 1. Find total sum of all elements of arr_4
print(f"Total sum of all element : {np.sum(arr_4)}")


# 2. Find average value of arr_4
print(f"Average value: {np.mean(arr_4)}")


# 3. Find maximum value of arr_4
print(f"Maximum value: {np.max(arr_4)}")


# 4. Find minimum value of arr_4
print(f"Minimum value: {np.min(arr_4)}")


# 5. Find median value of arr_4
print(f"Median value: {np.median(arr_4)}")


# 6. Find standard deviation of arr_4
print(f"Standard deviation: {np.std(arr_4)}")


# 7. Find product of all values of arr_4
print(f"Product of all values: {np.prod(arr_4)}")


# 8. Find unique values of arr_4
print(f"Unique values: {np.unique(arr_4)}")


# 9. Find the index of the maximum value of arr_4
print(f"Index of maximum value: {np.argmax(arr_4)}")


# 10. Find the index of the minimum value of arr_4
print(f"Index of minimum value: {np.argmin(arr_4)}")


# 11. Find Variance of arr_4
print(f"Variance: {np.var(arr_4)}")


# 12. Find the sum of each row of arr_4
print(f"Sum of each row: {np.sum(arr_4, axis=1)}")


# 13. Find the sum of each column of arr_4
print(f"Sum of each column: {np.sum(arr_4, axis=0)}")


