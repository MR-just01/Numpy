import numpy as np 

# -----------------------3-D Array ------------------------

arr = np.array([[[1,2,3], [4,5,6],[7,8,9]],
                [[11,12,13], [14,15,16],[17,18,19]],
                [[21,22,23], [24,25,26],[27,28,29]]]) 
               
# print(arr.ndim)

# -----------------------2-D Array ------------------------
# arr = np.array([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]])

 

 ##chainn Indexing 
print(arr[0][2][2])


##multidimensional indexing 
print(arr[0,1,0])
print(arr[0,0,0])
print(arr[1,0,0])
print(arr[2,0,0])
 