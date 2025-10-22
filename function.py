# Author : Engr. Muhammad Javed


import numpy as np


# 1. Insert Function:

#       Syntax:
#           new_arr =np.array(array_name , index , insert_value , axis)
#           axis = 0 for row insertion 
#           axis = 1 for column insertion


# For 1-D array:


arr1 = np.arange(10)
print("Original array: ", arr1)
arr1 = np.insert(arr1, 4, 15, axis=0)
print("Array after inserting 15 at index 4: ", arr1)


# For 2-D array:


arr2 = np.arange(12).reshape(3, 4)
print("\nOriginal array: ", arr2)
arr3 = np.insert(arr2 , 2 ,[12,34,56,78] , axis=0)
print("Array after inserting [12,34,56,78] at index 2: ",arr3)
arr2 = np.insert(arr2, 2, 15, axis=1)
print("Array after inserting 15 at index 2: ", arr2)





# 2. Append Function:

#       Syntax :
#           new_arr = np.append(array_name , value , axis)
#           axis = 0 for row insertion
#           axis = 1 for column insertion
#           axis = None for 1-D array          

# For 1-D array:

arr4 = np.arange(10 , 20)
print("\nOriginal array: ", arr4)
arr4 = np.append(arr4 , [23,76,98,65,89])
print("Array after appending [23,76,98,65,89]: ", arr4)


# For 2-D array:
arr5 = np.arange(12).reshape(3, 4)
print("\nOriginal array: ", arr5)
arr5 = np.append(arr5 , [[12,34,56,78] , [90 , 23,34, 45] , [67, 89, 12, 34]], axis=0)
print("\nArray after appending: ", arr5)






# 3. Concatenate Function:

#       Syntax:
#           new_arr = np.concatenate((array1 , array2 , array3 , ...), axis )
#           axis = 0 for vertical concatenation
#           axis = 1 for horizontal concatenation



arr6 = np.array([34,56,54,56])
arr7 = np.array([12,89,34,67,87])
arr8 = np.array([23,45,67,89,90,12,34,10])

n_arr = np.concatenate((arr6,arr7,arr8))
print("\nArray after concatenation: ", n_arr)






# 4. Stack Function:
#       Syntax:
#           new_arr = np.stack((array1 , array2 , array3 , ...), axis
#           new_arr = np.vstack((arr1 ,arr2)) -> for vertical stacking
#           new_arr = np.hstack((arr1 ,arr2)) -> for horizontal stacking
#           axis = 0 for vertical stacking
#           axis = 1 for horizontal stacking
#           axis = None for 1-D array stacking



# For 1-D array:

arr8 = np.array([1, 2, 3])
arr9 = np.array([4, 5, 6])

stacked = np.stack((arr8, arr9), axis=0)
print("Stacked (axis=0):\n", stacked)
print("Shape:", stacked.shape)

stacked_axis1 = np.stack((arr8, arr9), axis=1)
print("\nStacked (axis=1):\n", stacked_axis1)
print("Shape:", stacked_axis1.shape)



# For 2-D array :

arr10 = np.array([[1, 2],
              [3, 4]])

arr11 = np.array([[5, 6],
              [7, 8]])

stacked_2d = np.stack((arr10, arr11), axis=0)
print("\nStacked 2D (axis=0):\n", stacked_2d)
print("Shape:", stacked_2d.shape)


stacked_2d_axis1 = np.stack((arr10, arr11), axis=1)
print("\nStacked 2D (axis=1):\n", stacked_2d_axis1)
print("Shape:", stacked_2d_axis1.shape)





# 5. Delete Function:
#       The delete function is used to delete rows or columns from a numpy array.
#       It returns a new array with the specified rows or columns removed.

#       Syntax:
#           new_arr = np.delete(array_name , index , axis)



# For 1-D array:

arr13 = np.arange(7)
print("\nOriginal array:\n", arr13)
arr14 = np.delete(arr13, 3)
print("\nArray after deleting the 3rd element:\n", arr14)




# For 2-D array:

arr15 = np.arange(12,24).reshape(3,4)
print("\nOriginal array:\n", arr15)
arr16 = np.delete(arr15, 1, axis=1)
print("\nArray after deleting the 2nd column:\n", arr16)




# 6. Spilt Function:
#       The split function is used to split a numpy array into sub-arrays.

#       Syntax:
#           new_arr = np.split(array_name, split_size)
#           new_arr = np.split(array_name split_size , axis=0_or_1)


# For 1-D array:

arr17 = np.arange(23,44)
print("\nOriginal array:\n", arr17)
arr18 = np.split(arr17, 3)
print("\nSplit array:\n", arr18)



# For 2-D array:


arr19 = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
    [11, 12]
])

# Split into 3 parts along rows
result = np.split(arr19, 3, axis=0)

for i, part in enumerate(result):
    print(f"\nPart {i+1}:\n{part}")




arr20 = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])

# Split into 2 parts along columns
result2 = np.split(arr20, 2, axis=1)

for i, part in enumerate(result2):
    print(f"\nColumn Split {i+1}:\n{part}")