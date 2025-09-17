import numpy as np

array  = np.array([[1,2,3,4],
                  [5,6,7,8],
                   [9,10,11,12],
                    [13,14,15,16]])

print(array.shape)


#array [Start : end  : step ] ------SLICING  end part  is exclusive 
 
# print(array[1:4:2])
 
#   Negative slicing 

# print(array[::-2])


 # for slicing  the columns 
# print(array[:,-1])  #return the last column

# print(array[:, 1::2]) 


### slicing combinig the rows and column 

print(array[2:4 , 2:4])
