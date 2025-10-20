# Author : Engr. Muhammad Javed




# This is a list...

temperature = [23.45 , 98.34, 56.78, 34.67 , 90.45, 67.09]
total = 0
for temp in temperature:
    total += temp
avg = total / len(temperature)
print(round(avg , 4))


# This is a array....

import numpy as np


temperature = np.array([23.45 , 98.34, 56.78, 34.67 , 90.45, 67.09])
avg = np.mean(temperature)
print(avg)




# 1. Creation of array with numpy...


# 1-D array:
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)

# 2-D array:
arr2d = np.array([[6, 7, 8, 9, 10],[12,23,45,65,77]])
print(arr2d)

# 3-D array:
arr3d = np.array([[[1, 2, 3, 4,5], [6, 7, 8, 9, 10], [12, 23, 45, 65, 77]], [[13,14, 15, 16, 17], [18, 19,20, 21, 22], [24, 25, 26,27, 28]]])
print(arr3d)




# 2. Creation of array with random number:

    # Syntax:
    #   arr = np.random.rand(dimension of arrray)
    #   arr = np.random.randint(start, stop, shape)

# 2-D array with random number..
arr_2d = np.random.rand(3,3)
print(arr_2d)


# 3-D array with random number..
arr_3d = np.random.rand(4,5,6)
print(arr_3d)


# 4-D array with random number in range 10 to 100..
arr_4d = np.random.randint(10 , 100 , (3,4,7,5))
print(arr_4d)
                                                                   




# 3.  Creation of array with default number..

    # Syntax:
    #   arr = np.ones((shape of array))
    #   arr = np.zeros((shape of array))
    #   arr = np.full((shape of array), fill_value)
    #   arr = np.full_like(dimension of array, fill_value)
    #   arr = np.empty(dimension of array, dtype)



# Fill all element with zero.
arr1 = np.zeros((3,4,6))
print(arr1)


# Fill all element with one.
arr2 = np.ones((2,4,7))
print(arr2)


# Fill all element with 8.
arr3 = np.full((3,6,8) , 8)
print(arr3)


# Fill all element with Garbage.
arr4 = np.empty((3,6,8), dtype=int)
print(arr4)





# 4.  Creating a array with sequence of numbers....

    # Syntax:
        # arr = np.arange(start, stop, step, dtype)
        # arr = np.arange(start, stop, step, dtype).reshape(dim1, dim2, dim3)


# 1-D array with sequence of number..

arr5 = np.arange(1, 15 ,2)
print(arr5)
arr6 = np.arange(1,15,2,float)
print(arr6)


# n-D array with sequence of number...

arr6 = np.arange(20 ,80).reshape(3,4,5)
print(arr6)





# 5. Creation indentity matrix..
#       Syntax:
#           arr = np.eye(n, M, k, dtype)


# Creat a indentity matrix with 3 row and 4 column and data type is flaot..
arr7 = np.eye(3,4 , dtype = float)
print(arr7)








