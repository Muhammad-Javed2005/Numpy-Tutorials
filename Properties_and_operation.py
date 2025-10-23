# Author : Engr. Muhammad Javed


import numpy as np


# 1.Properties:


arr_1 = np.arange(20 ,56).reshape(3,4,3)
print(arr_1)
arr_2 = np.arange(20,56,1.).reshape(3,4,3)
print(arr_2)



# 1.Find shape of the arr_1.
print(f"Shape of arr_1 is {arr_1.shape}")



# 2.Find the number of element in arr_1.
print(f"Number of elements in arr_1 is {arr_1.size}")



# 3. Find the dimension of arr_1.
print(f"Dimension of arr_1 is {arr_1.ndim}")



# 4. Find the data type of arr_1.
print(f"Data type of arr_1 is {arr_2.dtype}")



# 5. Find the memory size of arr_1.
print(f"Memory size of arr_1 is {arr_1.itemsize}")



# 6. Type casting of arr_2 in int64.
arr_2 = arr_2.astype(np.int64)
print(arr_2 , arr_2.dtype)





# 2. Operator when shape is not equal:


arr_3 = np.arange(20 ,40).reshape(5,4,)
print(arr_3)

# 1. Update every element with +5
print(arr_3 + 5)


# 2. Update every element with -5
print(arr_3 -5)


# 3. Update every element with *5
print(arr_3 * 5)


# 4. Update every element with /5
print(arr_3 / 5)


# 5. Update every element with square 
print(arr_3 ** 2)




# 3.Operator when shape is equal:


arr_4= np.arange(24).reshape(2 , 3 , 4)
print(arr_4)

arr_5 = np.arange(24 , 48).reshape(2 , 3 , 4)
print(arr_5)

# 1.Addition of two arrays:
print(arr_4 + arr_5)

# 2.Subtraction of two arrays:
print(arr_4 - arr_5)

# 3.Multiplication of two arrays:
print(arr_4 * arr_5)

# 4.Division of two arrays:
print(arr_4 / arr_5)

# 5.Square of two arrays:
print(arr_4 ** arr_5)






