#Broadcasting allows numpy to perform operations on array 
#with different shapes by virtually expanding dimensions 
#so they match the larger array's shape 
#


#the dimension have the same size 
#or 
# one of the dimension has size of 1


import numpy as np 
array1 = np.array([[1,2,4,5,]])
array2 = np.array([[2],[1],[3],[4]])
print(array1.shape)
print(array2.shape)

print(array1*array2) 

arr1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[10]])
print(arr1.shape)
print(arr2.shape)
print(arr1*arr2)