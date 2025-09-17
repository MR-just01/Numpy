import numpy as np 

#creating the array from list 
# arr_id = np.array([1,23,3,4,5])
# print("1d array : " ,arr_id)

# arr_2d = np.array([[11,334,54 ] ,[34,56,45]])
# print("2d Array : " ,arr_2d )


# list vs numpy what is the difference
# py_list = [1,34,44]   
# print("print list multiplications : " ,py_list*2) #this just double the list i.e. create the same list two times

# numpy_arr = np.array([2,3,5])
# print("the multiplication of the numpy array : " ,numpy_arr*2) #numpy multiplication is same as the matrix multiplication

# numpy_arrange = np.arange(0,5,1)
# print(numpy_arrange) ## use to create the array in numpy for a specific range 
# 0 is the starting  
# 5 is the stopping point it is no include i.e  exclusive 
# 1 is the consecutive gap between the 0 and 5


#note:- 
# numpy arrays are excute more fast than the py_lists 


 ## creating the array from the scratch 

zeros = np.zeros((2,3))
print(zeros)

one = np.ones((2,4))
print(one)

full = np.full((5,5) ,7)
print(full)


# randomnum = np.random.random((2,5))
# print(randomnum)
   


   ##vector, matrix and tensor

# vector = np.array([1,23,4]) 
# print(f"vector : {vector} ")

# matrix = np.array([[1,234,45,2] , [24,34,5,35,]])
# print("matrix : " ,matrix )
  
# tensor = np.array([[[11,22],[25,46]],
#                    [[30,35], [40,57]]])  
# print("tensor : " ,tensor)


# ### num array properties 
arr = np.array([[1,2,4],[2,45,24]])
shape = arr.shape
print(shape)
  

