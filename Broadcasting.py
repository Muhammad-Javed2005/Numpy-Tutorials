import numpy as np

# Broadcasting:
#       Important note:
            # Matching the dimension of the arrays is required for broadcasting or else it will throw an error.
#       When we perform operations on arrays with different shapes, NumPy   
#       will automatically broadcast the arrays to a
#       common shape. This is done by repeating the elements of the smaller 
#       array until it has the same shape as the larger array.


prices = np.arange(0,1000 , 100)
discount = 10
print(prices)
final_prices = prices - (discount/100 * prices)
print(final_prices)



result = prices * 2
print(result)



matrix = np.array([[1,2,3] , [4,5,6]])
vector = np.array([10,20,30])

result = matrix + vector
print(result)


