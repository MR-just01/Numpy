#filtering = refers to the process of selecting elements 
#from an array that match a given condition

import numpy as np 

array = np.array([[23,12,43,45,15,20,17,92],
                  [17,19,64,18,36,65,89,90]])
teens = array[array <18]
print(" the teens in the array ",teens)
adutls = array[(array >=18 )& (array<65) ]
print(adutls)

seniors = array[(array>=89)]
print(seniors)
 
even = array[array%2== 0]
print(even)

# odd = array[array%2 != 0]
# print(odd)


## we can use the different method of filtering in case of preserving 
# original array ,,but it is lot more slower than the boolean indexing(above)

odd = np.where(array%2 != 0 ,array,0)
print(odd)
