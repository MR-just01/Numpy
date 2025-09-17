# aggregate functions that allow you to summarize and analyze array data efficiently

import numpy as np 
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

# print(np.sum(array))
# print(np.mean(array))
print(np.std(array))
print(np.var(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))
# print(np.argmax(array))

#we can select an axis =0 
print(np.sum(array,axis=0)) # sum the element of the colunms 
print(np.sum(array,axis=1))# sun the elements of the rows 