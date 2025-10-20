# Author : Engr. Muhammad Javed


import numpy as np



# 1. Indexing:

# Syntax:
    # For 1-D array : arr[index]
    # For 2-D array : arr[row_index, column_index]
    # For 3-D array : arr[block_index, row_index, column_index]



arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d[0])  # Output: 1
print(arr1d[-3]) # Output: 3

arr2d = np.array([[6, 7, 8, 9, 10],[12,23,45,65,77]])
print(arr2d[0, 0])  # Output: 6
print(arr2d[-1, -3])  # Output: 45

arr3d = np.array([[[1, 2, 3, 4,5], [6, 7, 8, 9, 10], [12, 23, 45, 65, 77]], [[13,14, 15, 16, 17], [18, 19,20, 21, 22], [24, 25, 26,27, 28]]])

print(arr3d[1,2,4]) # Output: 28
print(arr3d[-1, -1, -1])   # Output: 28 







# 2. Slicing:

# Syntax without step:
    # For 1-D array : arr[start:stop]
    # For 2-D array : arr[row_start:row_stop, column_start:column_stop]
    # For 3-D array : arr[block_start:block_stop, row_start:row_stop ,column_start:column_stop]

# Syntax with step:
    # For 1-D array : arr[start:stop:step]
    # For 2-D array : arr[row_start:row_stop:step, column_start:column_stop:step]
    # For 3-D array : arr[block_start:block_stop:step, row_start:row_stop:step, column_start:column_stop:step]

# For 1-D array:
print(arr1d[1:4]) # Output : [2 3 4]
print(arr1d[1:4:2]) # Output : [2 4]

# For 2-D array:
print(arr2d[0:1, 0:3]) # Output : [[6 7 8]]
print(arr2d[0:1, 0:3:2]) # Output : [[ 6 8]]

# For 3-D array:
print(arr3d[0:1, 0:1, 0:4]) # Output : [[[ 1  2  3  4]]]
print(arr3d[0:1, 0:1, 0:4:2]) # Output : [[[ 1  3]]]






# Print form start to stop index
print(arr1d[:3]) # Output : [1 2 3]


# Print form start index to end
print(arr1d[3:]) # Output : [4 5]


# Print form start to end with step
print(arr1d[::2]) # Output : [4 5]


# Print reverse array
print(arr1d[::-1]) # Output : [5 4 3 2 1]







# 3. Fancy Indexing:

    # 1) Fancy indexing is a way to access elements in a numpy array using a list of indices.
    # 2) The list of indices can be a list of integers, a list of slices, or a list of boolean arrays.
    # 3) The syntax for fancy indexing is arr[indices], where indices is a list of indices.



# Syntax:
    # For 1-D array : arr[[i1, i2, i3, ...]]
    # For 2-D array : arr[[row1, row2], [col1, col2]]
    # For 3-D array : arr[[b1, b2], [r1, r2], [c1, c2]]




# For 1-D array:  
print(arr1d[[0, 2, 4]])    # Output: [1 3 5]




# For 2-D array
print(arr2d[[0, 1], [1, 2]])  # Output: [7 45]


# Select full rows by index
print(arr2d[[0, 1], :])       # Output: both rows


# Select specific columns from all rows
print(arr2d[:, [0, 2, 4]])    # Output: cols 0, 2, and 4 from both rows




# For 3-D array:
print(arr3d[[0, 1], [1, 2], [2, 4]])  # Output: [8 28]






# 4. Boolean Indexing:
    # 1) Boolean indexing is a way to access elements in a numpy array using a boolean array.
    # 2) The boolean array is used to select elements from the original array.
    # 3) The syntax for boolean indexing is arr[condition], where condition is a boolean array.

arr = np.array([10, 15, 20, 25, 30])
# Boolean condition
marks = arr > 20

print(marks)   # Output : [False False False  True  True]


# Print all element which is divisible by 5
print(arr[arr%5==0])


# Print all odd element
print(arr[arr%2!=0])


# Print all even element
print(arr[arr%2==0])








# 5. Filtering :
    # 1) Filtering indexing is a way to access elements in a numpy array based on a condition.
    # 2) The syntax for filtering indexing is arr[condition], where condition is a boolean array.
    # 3) The elements in the array that satisfy the condition are selected.




arr = np.array([10, 15, 20, 25, 30])
# Filtering condition
marks = arr >13
print(arr[marks])  # Output: [15 20 25 30]



# 6. Reshaping array:
    # 1) Reshaping is a way to change the shape of a numpy array without
    #    changing its data.
    # 2) The syntax for reshaping is arr.reshape(new_shape), where new_shape is the new shape of the array.


arr1d = np.arange(6)
print(arr1d)  

# Reshaping the array to 2-D array of shape (2, 3)
arr2d = arr1d.reshape(2, 3)
print(arr2d)  



# Flatten and Ravel :
    # 1) Flatten is a function that returns a copy of the array collapsed into one dimension.
    # 2) Ravel is a function that returns a copy of the array collapsed into on dimension.


arr_3d = np.arange(26,50).reshape(3,4,2)
print(arr_3d)   

arr_1 = arr_3d.flatten()
print(arr_1)
arr_2 = arr_3d.ravel()
print(arr_2)

