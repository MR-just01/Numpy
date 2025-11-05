import numpy as np
zeroes = np.zeros(10)
print(zeroes)

ones = np.ones(10)
print(ones)

###Basic Questions on array
a = np.arange(20)
print(" array : ",a)
b=a[:5]  #extracting first five elements 
print(" first five elements : " , b)
c= a[::2] #extracting the even number index
print("even index elements: ", c)
d = a[5:16:4] #slicing from the 5th index to 15 index with a step of 4
print("elemets from the 5th to 15th index with a step of 4: ", d)