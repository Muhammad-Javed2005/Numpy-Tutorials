# Author : Engr. Muhammad Javed

import numpy as np 


# Handling Missing Values:



arr = np.array([1,2,np.nan ,4,5,np.nan])
print(arr)
 

# Use np.isnan() to detect NaN (missing) values in the array and return a boolean array.
print(np.isnan(arr))


# Use nan_to_num() function use to replace NaN value with a specified value.

cleared_arr = np.nan_to_num(arr , nan=100)
print(cleared_arr)



# Infinite values can be handled using np.isinf() function.

arrr = np.array([1,2, np.inf ,4,5,-np.inf])
print(arrr)
print(np.isinf(arrr))

clear_arrr = np.nan_to_num(arrr , posinf = 100 , neginf = -100)
print(clear_arrr) 


arr = np.arange(23,45).reshape(2,3)